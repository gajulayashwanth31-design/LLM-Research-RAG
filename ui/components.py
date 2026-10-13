import json
import math
from collections.abc import Mapping
from typing import Any

import streamlit as st


METRICS = (
    ("recall_at_1", "Recall@1"),
    ("recall_at_3", "Recall@3"),
    ("recall_at_5", "Recall@5"),
    ("mrr", "Mean Reciprocal Rank (MRR)"),
)

RAGAS_METRICS = (
    ("faithfulness", "Faithfulness"),
    ("answer_relevancy", "Answer Relevancy"),
    ("context_precision", "Context Precision"),
    ("context_recall", "Context Recall"),
    ("answer_correctness", "Answer Correctness"),
)


def _valid_score(value: Any) -> bool:
    return (
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and math.isfinite(value)
    )


def _format_metric(metrics: Mapping[str, Any], key: str) -> str:
    value = metrics.get(key)
    return f"{value:.4f}" if _valid_score(value) else "N/A"


def _score_issue(result: Mapping[str, Any], key: str) -> str | None:
    if key not in result:
        return "missing key"
    value = result[key]
    if value is None:
        return "null"
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return f"invalid type ({type(value).__name__})"
    if math.isnan(value):
        return "NaN"
    if math.isinf(value):
        return "infinite"
    return None


def _display_evaluation_metadata(
    data: Mapping[str, Any],
    summary: Mapping[str, Any],
    status: str,
) -> None:
    model = next(
        (
            value
            for source in (data, summary)
            for key in ("evaluation_model", "evaluator_model", "model")
            if isinstance((value := source.get(key)), str) and value.strip()
        ),
        None,
    )
    saved_status = next(
        (
            value
            for source in (data, summary)
            for key in ("evaluation_status", "status")
            if isinstance((value := source.get(key)), str) and value.strip()
        ),
        None,
    )
    details = [f"Status: {saved_status or status}"]
    if model:
        details.append(f"Evaluation model: {model}")
    st.caption(" · ".join(details))


def _source_title(source: Mapping[str, Any]) -> str:
    title = source.get("paper")
    if isinstance(title, str) and title.strip():
        return title
    source_file = source.get("source_file")
    if isinstance(source_file, str) and source_file.strip():
        from pathlib import Path

        return Path(source_file).stem.replace("_", " ").title()
    return "Retrieved source"


def render_sources(
    sources: list[dict[str, Any]],
    retrieved_chunks: list[dict[str, Any]],
) -> None:
    st.markdown("#### 📚 Sources")
    chunks_by_id = {
        chunk.get("chunk_id"): chunk
        for chunk in retrieved_chunks
        if isinstance(chunk.get("chunk_id"), str)
    }

    if not sources:
        st.caption("No source metadata was returned for this response.")
        return

    for index, source in enumerate(sources, start=1):
        chunk_id = source.get("chunk_id")
        chunk = chunks_by_id.get(chunk_id, {})
        title = _source_title(source)
        section = source.get("section")
        label = f"{index}. {title}"
        if isinstance(section, str) and section:
            label += f" — {section}"

        with st.expander(label):
            if isinstance(section, str) and section:
                st.markdown(f"**Section:** {section}")
            if isinstance(chunk_id, str) and chunk_id:
                st.code(chunk_id, language=None)
            text = chunk.get("text")
            if isinstance(text, str) and text:
                st.markdown(text)
            else:
                st.caption("Retrieved chunk text is unavailable.")

    with st.expander("🔍 Retrieval Details"):
        st.markdown(
            "**Semantic Search + BM25**  \n"
            "↓  \n"
            "**RRF Fusion**  \n"
            "↓  \n"
            "**Cross-Encoder Reranker**  \n"
            "↓  \n"
            "**Top 5 chunks**"
        )
        for index, source in enumerate(sources, start=1):
            chunk_id = source.get("chunk_id")
            chunk = chunks_by_id.get(chunk_id, {})
            title = _source_title(source)
            section = source.get("section")
            st.markdown(f"**{index}. {title}**")
            if isinstance(section, str) and section:
                st.caption(f"Section: {section}")
            score = chunk.get("reranker_score")
            if _valid_score(score):
                st.caption(f"Reranker score: {score:.6f}")


def render_chat_history(history: list[dict[str, Any]]) -> None:
    for message in history:
        if message["role"] == "user":
            _, message_column = st.columns([2, 3])
        else:
            message_column, _ = st.columns([3, 2])

        with message_column:
            with st.chat_message(message["role"]):
                if (
                    message["role"] == "assistant"
                    and message.get("grounded_refusal")
                ):
                    st.info("Grounded refusal")
                st.markdown(message["content"])
                if message["role"] == "assistant" and not message.get("is_casual"):
                    render_sources(
                        message.get("sources", []),
                        message.get("retrieved_chunks", []),
                    )


def render_retrieval_evaluation(data: Mapping[str, Any] | None) -> None:
    st.subheader("Retrieval Evaluation")
    if data is None:
        st.warning("Retrieval evaluation results are missing or unavailable.")
        return

    summary = data.get("summary")
    summary = summary if isinstance(summary, Mapping) else {}
    baseline = data.get("baseline_metrics")
    hybrid = data.get("hybrid_metrics")
    baseline = baseline if isinstance(baseline, Mapping) else {}
    hybrid = hybrid if isinstance(hybrid, Mapping) else {}

    missing_metrics = [
        label
        for metrics in (baseline, hybrid)
        for key, label in METRICS
        if not _valid_score(metrics.get(key))
    ]
    status = "Complete" if not missing_metrics else "Incomplete"
    _display_evaluation_metadata(data, summary, status)
    st.caption("Baseline — BGE + Chroma")
    baseline_columns = st.columns(len(METRICS))
    for column, (key, label) in zip(baseline_columns, METRICS):
        metric_status = "complete" if _valid_score(baseline.get(key)) else "pending"
        column.metric(
            f"{label} · {metric_status}",
            _format_metric(baseline, key),
        )
    st.caption("Hybrid + Reranker")
    hybrid_columns = st.columns(len(METRICS))
    for column, (key, label) in zip(hybrid_columns, METRICS):
        metric_status = "complete" if _valid_score(hybrid.get(key)) else "pending"
        column.metric(
            f"{label} · {metric_status}",
            _format_metric(hybrid, key),
        )

    if missing_metrics:
        st.warning(
            "Some retrieval metrics are missing or pending. "
            "Available scores are shown; unavailable scores are N/A."
        )

    if isinstance(summary, Mapping):
        labeled = summary.get("labeled_tests")
        total = summary.get("total_tests")
        if isinstance(total, int) and not isinstance(total, bool):
            count_text = f"{total} evaluation test cases"
            if isinstance(labeled, int) and not isinstance(labeled, bool):
                count_text += f" ({labeled} labeled)"
            st.caption(count_text)

    with st.expander("Show retrieval evaluation details"):
        st.json(data)


def render_generation_evaluation(data: Mapping[str, Any] | None) -> None:
    st.subheader("Generation Evaluation")
    if data is None:
        st.warning("Generation evaluation results are missing or unavailable.")
        return

    summary = data.get("summary")
    results = data.get("per_test_results")
    summary = summary if isinstance(summary, Mapping) else {}
    results = results if isinstance(results, list) else []

    for start in range(0, len(RAGAS_METRICS), 3):
        metric_row = st.columns(min(3, len(RAGAS_METRICS) - start))
        for column, (key, label) in zip(
            metric_row,
            RAGAS_METRICS[start : start + 3],
        ):
            column.metric(label, _format_metric(summary, key))

    total = summary.get("total_tests")
    if isinstance(total, int) and not isinstance(total, bool):
        count_text = f"{total} evaluation test cases"
        st.caption(count_text)

    with st.expander("Show per-test generation results and errors"):
        if not results:
            st.info("No per-test result records are available.")
        else:
            rows = []
            for result in results:
                if not isinstance(result, Mapping):
                    rows.append({"Test": "Invalid result record"})
                    continue
                row: dict[str, str] = {
                    "Test": str(result.get("id", "Unknown")),
                    "Question": str(result.get("question", "")),
                    "Answerable": (
                        str(result["answerable"])
                        if isinstance(result.get("answerable"), bool)
                        else "N/A"
                    ),
                }
                row.update(
                    {
                        label: _format_metric(result, key)
                        for key, label in RAGAS_METRICS
                    }
                )
                metric_issues = [
                    f"{label}: {_score_issue(result, key)}"
                    for key, label in RAGAS_METRICS
                    if _score_issue(result, key) is not None
                ]
                row["Incomplete metrics"] = "; ".join(metric_issues)
                errors = result.get("errors")
                row["Errors"] = (
                    json.dumps(errors, ensure_ascii=False)
                    if isinstance(errors, Mapping) and errors
                    else ""
                )
                rows.append(row)
            st.table(rows)

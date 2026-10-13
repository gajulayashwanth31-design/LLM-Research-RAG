import asyncio
import json
import math
import os
import tempfile
import threading
import time
from collections.abc import Callable
from pathlib import Path
from statistics import mean
from typing import Any

import chromadb
from importlib.metadata import PackageNotFoundError, version
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.outputs import ChatResult
from pydantic import PrivateAttr
from dotenv import load_dotenv

load_dotenv()
if not os.getenv("GEMINI_API_KEY", "").strip():
    raise RuntimeError(
        "GEMINI_API_KEY is missing. Add it to the project .env file "
        "before running generation evaluation."
    )

from generator import MODEL as GENERATION_MODEL
from generator import llm as generation_llm
from embeddings import get_embedding_model
from vector_store import COLLECTION_NAME


EVALUATION_DIRECTORY = Path(__file__).resolve().parent
PROJECT_DIRECTORY = EVALUATION_DIRECTORY.parent
TESTS_FILE = EVALUATION_DIRECTORY / "tests.json"
GENERATION_RESULTS_FILE = EVALUATION_DIRECTORY / "generation_results.json"
EVALUATION_RESULTS_FILE = (
    EVALUATION_DIRECTORY / "generation_evaluation_results.json"
)
CHROMA_DIRECTORY = PROJECT_DIRECTORY / "chroma_db"
BATCH_SIZE = 10
MIN_REQUEST_INTERVAL_SECONDS = 6.0
REFUSAL_PHRASE = (
    "I don't have enough information in the provided knowledge base."
)
RAGAS_METRICS = (
    "faithfulness",
    "answer_relevancy",
    "context_precision",
    "context_recall",
    "answer_correctness",
)


class RateLimitedChatModel(BaseChatModel):
    #"""Serialize Gemini evaluator requests and space starts by six seconds."""
    """Serialize evaluator requests and space starts by six seconds."""

    delegate: BaseChatModel
    min_interval_seconds: float = MIN_REQUEST_INTERVAL_SECONDS
    _request_lock: threading.Lock = PrivateAttr(default_factory=threading.Lock)
    _last_request_started_at: float | None = PrivateAttr(default=None)
    _request_count: int = PrivateAttr(default=0)

    @property
    def _llm_type(self) -> str:
        #return "rate-limited-gemini"
        return "rate-limited-evaluator"

    @property
    def request_count(self) -> int:
        return self._request_count

    def _start_request(self) -> None:
        self._request_lock.acquire()
        try:
            now = time.monotonic()
            if self._last_request_started_at is not None:
                delay = (
                    self.min_interval_seconds
                    - (now - self._last_request_started_at)
                )
                if delay > 0:
                    time.sleep(delay)
            self._last_request_started_at = time.monotonic()
            self._request_count += 1
        except Exception:
            self._request_lock.release()
            raise

    def _generate(
        self,
        messages: list[Any],
        stop: list[str] | None = None,
        run_manager: Any = None,
        **kwargs: Any,
    ) -> ChatResult:
        self._start_request()
        try:
            return self.delegate._generate(
                messages,
                stop=stop,
                run_manager=run_manager,
                **kwargs,
            )
        finally:
            self._request_lock.release()

    async def _agenerate(
        self,
        messages: list[Any],
        stop: list[str] | None = None,
        run_manager: Any = None,
        **kwargs: Any,
    ) -> ChatResult:
        await asyncio.to_thread(self._start_request)
        try:
            return await self.delegate._agenerate(
                messages,
                stop=stop,
                run_manager=run_manager,
                **kwargs,
            )
        finally:
            self._request_lock.release()


def _get_ragas_version() -> str:
    try:
        return version("ragas")
    except PackageNotFoundError:
        return "not installed"


def _load_ragas_api() -> tuple[Callable[..., Any], Any, dict[str, Any]]:
    try:
        from ragas import evaluate
        from ragas.metrics import (
            answer_correctness,
            answer_relevancy,
            context_precision,
            context_recall,
            faithfulness,
        )
        from ragas.run_config import RunConfig
    except ImportError as error:
        raise RuntimeError(
            f"Ragas {_get_ragas_version()} is installed but cannot be imported "
            "in this environment. Repair its LangChain Community dependencies "
            "before running generation evaluation. No alternate evaluator "
            "or model will be selected."
        ) from error

    metric_instances = {
        "faithfulness": faithfulness,
        "answer_relevancy": answer_relevancy,
        "context_precision": context_precision,
        "context_recall": context_recall,
        "answer_correctness": answer_correctness,
    }
    return evaluate, RunConfig, metric_instances


def _load_json_array(path: Path, description: str) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as json_file:
        records = json.load(json_file)
    if not isinstance(records, list):
        raise ValueError(f"{description} must contain a JSON array.")
    return records


def _load_tests() -> list[dict[str, Any]]:
    with TESTS_FILE.open("r", encoding="utf-8") as tests_file:
        tests_data = json.load(tests_file)
    tests = tests_data["tests"]
    identifiers = [test["id"] for test in tests]
    if len(identifiers) != len(set(identifiers)):
        raise ValueError("tests.json contains duplicate test IDs.")
    return tests


def _load_generation_results() -> dict[str, dict[str, Any]]:
    records = _load_json_array(GENERATION_RESULTS_FILE, "generation_results.json")
    results: dict[str, dict[str, Any]] = {}
    for record in records:
        test_id = record.get("id")
        if not isinstance(test_id, str):
            raise ValueError(
                "generation_results.json contains a result without a string ID."
            )
        if test_id in results:
            raise ValueError(
                f"generation_results.json contains duplicate test ID {test_id!r}."
            )
        results[test_id] = record
    return results


def _load_existing_evaluation_results() -> dict[str, dict[str, Any]]:
    if not EVALUATION_RESULTS_FILE.exists():
        return {}

    with EVALUATION_RESULTS_FILE.open("r", encoding="utf-8") as results_file:
        data = json.load(results_file)
    records = data.get("per_test_results")
    if not isinstance(records, list):
        raise ValueError(
            "generation_evaluation_results.json must have a "
            "'per_test_results' array."
        )

    results: dict[str, dict[str, Any]] = {}
    for record in records:
        test_id = record.get("id")
        if not isinstance(test_id, str):
            raise ValueError(
                "generation_evaluation_results.json contains a row "
                "without a string ID."
            )
        if test_id in results:
            raise ValueError(
                "generation_evaluation_results.json contains duplicate "
                f"test ID {test_id!r}."
            )
        results[test_id] = record
    return results


def _save_evaluation_results(
    tests: list[dict[str, Any]],
    result_by_id: dict[str, dict[str, Any]],
) -> None:
    ordered_results = [
        result_by_id[test["id"]]
        for test in tests
        if test["id"] in result_by_id
    ]
    answerable_tests = [test for test in tests if test.get("answerable") is True]
    unanswerable_tests = [test for test in tests if test.get("answerable") is False]

    summary: dict[str, Any] = {
        "total_tests": len(tests),
        "answerable_tests": len(answerable_tests),
        "unanswerable_tests": len(unanswerable_tests),
    }
    for metric in RAGAS_METRICS:
        scores = [
            result[metric]
            for result in ordered_results
            if result.get("answerable") is True
            and isinstance(result.get(metric), (int, float))
            and math.isfinite(result[metric])
        ]
        summary[metric] = mean(scores) if scores else None

    if unanswerable_tests:
        correct_refusals = sum(
            result_by_id.get(test["id"], {}).get("grounding_refusal_correct")
            is True
            for test in unanswerable_tests
        )
        summary["grounding_refusal_accuracy"] = (
            correct_refusals / len(unanswerable_tests)
        )
    else:
        summary["grounding_refusal_accuracy"] = None

    _atomic_write_json(
        EVALUATION_RESULTS_FILE,
        {
            "summary": summary,
            "per_test_results": ordered_results,
        },
    )


def _atomic_write_json(path: Path, data: dict[str, Any]) -> None:
    temporary_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=path.parent,
            prefix=f".{path.name}.",
            suffix=".tmp",
            delete=False,
        ) as temporary_file:
            temporary_path = Path(temporary_file.name)
            json.dump(
                data,
                temporary_file,
                ensure_ascii=False,
                indent=2,
                allow_nan=False,
            )
            temporary_file.write("\n")
            temporary_file.flush()
            os.fsync(temporary_file.fileno())

        os.replace(temporary_path, path)
        temporary_path = None
    finally:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)


def _get_chroma_collection() -> Any:
    client = chromadb.PersistentClient(path=str(CHROMA_DIRECTORY))
    return client.get_collection(name=COLLECTION_NAME)


def _get_contexts(
    collection: Any,
    sources: list[dict[str, Any]],
) -> tuple[list[str], list[str]]:
    chunk_ids: list[str] = []
    seen_chunk_ids: set[str] = set()
    for source in sources:
        chunk_id = source.get("chunk_id")
        if not isinstance(chunk_id, str) or not chunk_id:
            raise ValueError(
                "A saved source is missing its chunk_id; actual retrieved "
                "context cannot be verified."
            )
        if chunk_id not in seen_chunk_ids:
            seen_chunk_ids.add(chunk_id)
            chunk_ids.append(chunk_id)

    if not chunk_ids:
        raise ValueError(
            "No saved source chunk IDs are available for this generated answer."
        )

    stored = collection.get(ids=chunk_ids, include=["documents"])
    content_by_id = dict(zip(stored["ids"], stored["documents"]))
    missing_ids = [chunk_id for chunk_id in chunk_ids if chunk_id not in content_by_id]
    if missing_ids:
        raise ValueError(
            "Saved source chunk IDs are missing from the existing ChromaDB "
            f"collection: {missing_ids}"
        )

    return chunk_ids, [content_by_id[chunk_id] for chunk_id in chunk_ids]


def _is_complete_answerable_result(result: dict[str, Any] | None) -> bool:
    return bool(
        result
        and result.get("answerable") is True
        and all(
            isinstance(result.get(metric), (int, float))
            and math.isfinite(result[metric])
            for metric in RAGAS_METRICS
        )
    )


def _make_test_result(
    test: dict[str, Any],
    generated: dict[str, Any] | None,
) -> dict[str, Any]:
    if generated is None:
        raise ValueError(
            "No saved generation result exists; run_generation.py must have "
            "already produced this test's answer."
        )

    answer = generated.get("generated_answer")
    if not isinstance(answer, str):
        raise ValueError("Saved generation result has no string generated_answer.")

    return {
        "id": test["id"],
        "question": test["question"],
        "generated_answer": answer,
        "reference_answer": test["reference_answer"],
        "answerable": test["answerable"],
        "retrieved_context_ids": [],
        "retrieved_contexts": [],
        **{metric: None for metric in RAGAS_METRICS},
        "grounding_refusal_correct": None,
        "errors": {},
    }


def _score_one_metric(
    evaluate: Callable[..., Any],
    metric: Any,
    row: dict[str, Any],
    llm: RateLimitedChatModel,
    embeddings: Any,
    run_config: Any,
) -> float:
    from datasets import Dataset

    request_count_before = llm.request_count
    evaluation = evaluate(
        Dataset.from_list([row]),
        metrics=[metric],
        llm=llm,
        embeddings=embeddings,
        run_config=run_config,
        raise_exceptions=True,
        show_progress=False,
        batch_size=1,
    )
    score = evaluation.scores[0][metric.name]
    if not isinstance(score, (int, float)) or not math.isfinite(score):
        raise ValueError(f"Ragas metric {metric.name!r} returned a non-finite score.")
    print(
        f"    {metric.name}: {score:.4f} "
        f"({llm.request_count - request_count_before} evaluator model calls)"
    )
    return float(score)


def _is_correct_refusal(answer: str) -> bool:
    return answer.strip() == REFUSAL_PHRASE


def _print_summary(data: dict[str, Any], ragas_version: str) -> None:
    summary = data["summary"]
    print("\n" + "=" * 50)
    print("GENERATION EVALUATION")
    print("=" * 50)
    print(f"\nRagas version: {ragas_version}")
    print(f"\nTotal tests: {summary['total_tests']}")
    print(f"Answerable tests: {summary['answerable_tests']}")
    print(f"Unanswerable tests: {summary['unanswerable_tests']}")
    print("\nRAGAS METRICS")
    for metric, label in (
        ("faithfulness", "Faithfulness"),
        ("answer_relevancy", "Answer Relevancy"),
        ("context_precision", "Context Precision"),
        ("context_recall", "Context Recall"),
        ("answer_correctness", "Answer Correctness"),
    ):
        score = summary[metric]
        print(f"{label}: {score:.4f}" if score is not None else f"{label}: N/A")

    print("\nGROUNDING")
    refusal_accuracy = summary["grounding_refusal_accuracy"]
    print(
        f"Refusal Accuracy: {refusal_accuracy:.4f}"
        if refusal_accuracy is not None
        else "Refusal Accuracy: N/A"
    )
    print("\nResults saved to:")
    print("evaluation/generation_evaluation_results.json")


def run_evaluation() -> None:
    ragas_version = _get_ragas_version()
    evaluate, RunConfig, metric_instances = _load_ragas_api()

    tests = _load_tests()
    generated_by_id = _load_generation_results()
    result_by_id = _load_existing_evaluation_results()

    completed_tests = 0
    for test in tests:
        existing = result_by_id.get(test["id"])
        if test.get("answerable") is True:
            completed_tests += _is_complete_answerable_result(existing)
        elif (
            test.get("answerable") is False
            and existing is not None
            and isinstance(existing.get("grounding_refusal_correct"), bool)
            and not existing.get("errors", {}).get("grounding_refusal")
        ):
            completed_tests += 1

    print(f"Ragas version: {ragas_version}")
    print("Evaluator provider: Gemini")
    print(f"Evaluator model: {GENERATION_MODEL}")
    print(f"Total tests: {len(tests)}")
    print(f"Already completed tests: {completed_tests}")
    print(f"Pending tests: {len(tests) - completed_tests}")
    print(f"Output file: {EVALUATION_RESULTS_FILE}")

    collection = _get_chroma_collection()
    answerable_tests = [test for test in tests if test.get("answerable") is True]
    unanswerable_tests = [
        test for test in tests if test.get("answerable") is False
    ]
    test_batches = [
        tests[start : start + BATCH_SIZE]
        for start in range(0, len(tests), BATCH_SIZE)
    ]

    evaluator_llm = RateLimitedChatModel(delegate=generation_llm)
    embeddings = get_embedding_model()
    run_config = RunConfig(
        max_retries=3,
        max_wait=30,
        max_workers=1,
        log_tenacity=True,
    )

    _save_evaluation_results(tests, result_by_id)
    print(
        f"Evaluating {len(answerable_tests)} answerable and "
        f"{len(unanswerable_tests)} unanswerable tests with Ragas {ragas_version}."
    )

    for batch_number, batch in enumerate(test_batches, start=1):
        print(f"\nBatch {batch_number}/{len(test_batches)}")
        print("Evaluating ...")

        for test in batch:
            test_id = test["id"]
            generated = generated_by_id.get(test_id)
            existing = result_by_id.get(test_id)

            if test.get("answerable") is True:
                if _is_complete_answerable_result(existing):
                    print(f"  Skipping completed test {test_id}.")
                    continue

                try:
                    result = existing or _make_test_result(test, generated)
                    if not result.get("retrieved_contexts"):
                        assert generated is not None
                        context_ids, contexts = _get_contexts(
                            collection,
                            generated.get("sources", []),
                        )
                        result["retrieved_context_ids"] = context_ids
                        result["retrieved_contexts"] = contexts

                    ragas_row = {
                        "user_input": test["question"],
                        "response": result["generated_answer"],
                        "retrieved_contexts": result["retrieved_contexts"],
                        "reference": test["reference_answer"],
                    }
                    for metric_name, metric in metric_instances.items():
                        if (
                            isinstance(result.get(metric_name), (int, float))
                            and math.isfinite(result[metric_name])
                        ):
                            continue
                        try:
                            result[metric_name] = _score_one_metric(
                                evaluate,
                                metric,
                                ragas_row,
                                evaluator_llm,
                                embeddings,
                                run_config,
                            )
                            result["errors"].pop(metric_name, None)
                        except Exception as error:
                            message = f"{type(error).__name__}: {error}"
                            result["errors"][metric_name] = message
                            print(
                                f"  Failed {test_id} / {metric_name}: {message}"
                            )
                    result_by_id[test_id] = result
                except Exception as error:
                    message = f"{type(error).__name__}: {error}"
                    failure_result = existing or {
                        "id": test_id,
                        "question": test["question"],
                        "generated_answer": (
                            generated.get("generated_answer", "")
                            if generated
                            else ""
                        ),
                        "reference_answer": test["reference_answer"],
                        "answerable": True,
                        "retrieved_context_ids": [],
                        "retrieved_contexts": [],
                        **{metric: None for metric in RAGAS_METRICS},
                        "grounding_refusal_correct": None,
                        "errors": {},
                    }
                    failure_result["errors"]["context_or_input"] = message
                    result_by_id[test_id] = failure_result
                    print(f"  Failed test {test_id}: {message}")

            elif test.get("answerable") is False:
                if (
                    existing is not None
                    and isinstance(existing.get("grounding_refusal_correct"), bool)
                    and not existing.get("errors", {}).get("grounding_refusal")
                ):
                    print(f"  Skipping completed test {test_id}.")
                    continue
                answer = (
                    generated.get("generated_answer")
                    if generated is not None
                    else None
                )
                result = existing or {
                    "id": test_id,
                    "question": test["question"],
                    "generated_answer": answer or "",
                    "reference_answer": test["reference_answer"],
                    "answerable": False,
                    "retrieved_context_ids": [],
                    "retrieved_contexts": [],
                    **{metric: None for metric in RAGAS_METRICS},
                    "errors": {},
                }
                result["grounding_refusal_correct"] = (
                    _is_correct_refusal(answer) if isinstance(answer, str) else False
                )
                if not isinstance(answer, str):
                    result["errors"]["grounding_refusal"] = (
                        "No saved generated answer exists for this unanswerable test."
                    )
                result_by_id[test_id] = result
            else:
                print(f"  Skipping test {test_id}: answerable is not boolean.")

        print("Saving results...")
        _save_evaluation_results(tests, result_by_id)

    with EVALUATION_RESULTS_FILE.open("r", encoding="utf-8") as result_file:
        final_results = json.load(result_file)
    _print_summary(final_results, ragas_version)
    print(f"\nEvaluator model-call count this run: {evaluator_llm.request_count}")


if __name__ == "__main__":
    run_evaluation()

import json
import logging
import sys
from pathlib import Path
from typing import Any

import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from components import (  # noqa: E402
    render_chat_history,
    render_generation_evaluation,
    render_retrieval_evaluation,
)
from styles import APP_CSS  # noqa: E402


logger = logging.getLogger(__name__)
EVALUATION_DIRECTORY = PROJECT_ROOT / "evaluation"
RETRIEVAL_RESULTS_FILE = (
    EVALUATION_DIRECTORY / "retrieval_evaluation_results.json"
)
GENERATION_RESULTS_FILE = (
    EVALUATION_DIRECTORY / "generation_evaluation_results.json"
)
REFUSAL_PHRASE = (
    "I don't have enough information in the provided knowledge base."
)


def _load_result_file(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    with path.open("r", encoding="utf-8") as result_file:
        result = json.load(result_file)
    if not isinstance(result, dict):
        raise ValueError("Evaluation result must contain a JSON object.")
    return result


def _render_chat_page() -> None:
    st.title("LLM Research Assistant")
    st.markdown(
        '<p class="page-subtitle">Research-grounded answers from LLM literature.</p>',
        unsafe_allow_html=True,
    )

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    render_chat_history(st.session_state.chat_history)

    with st.form("ask_question", clear_on_submit=True):
        question = st.text_input(
            "Your question",
            placeholder="Ask a question about the research literature...",
        )
        submitted = st.form_submit_button("Ask", type="primary")

    if not submitted:
        return
    if not question.strip():
        st.warning("Enter a question before sending.")
        return

    from conversation import casual_response, resolve_follow_up_query

    recent_history = st.session_state.chat_history[-8:]
    st.session_state.chat_history.append(
        {"role": "user", "content": question.strip()}
    )

    direct_reply = casual_response(question)
    if direct_reply is not None:
        st.session_state.chat_history.append(
            {
                "role": "assistant",
                "content": direct_reply,
                "sources": [],
                "retrieved_chunks": [],
                "is_casual": True,
            }
        )
        st.rerun()

    retrieval_query = resolve_follow_up_query(question, recent_history)
    with st.spinner("Searching the research literature and preparing an answer..."):
        try:
            from generator import answer_question

            response = answer_question(retrieval_query)
            answer = response["answer"]
            sources = response.get("sources", [])
            retrieved_chunks = response.get("retrieved_chunks", [])
            st.session_state.chat_history.append(
                {
                    "role": "assistant",
                    "content": answer,
                    "sources": sources,
                    "retrieved_chunks": retrieved_chunks,
                    "grounded_refusal": answer.strip() == REFUSAL_PHRASE,
                    "retrieval_query": retrieval_query,
                }
            )
        except Exception:
            logger.exception("Chat request failed.")
            st.session_state.chat_history.append(
                {
                    "role": "assistant",
                    "content": (
                        "I couldn't complete that request. Please try again."
                    ),
                    "sources": [],
                    "retrieved_chunks": [],
                }
            )
    st.rerun()


def _render_evaluation_page() -> None:
    st.title("📊 Evaluation")
    st.markdown(
        '<p class="page-subtitle">Offline benchmark results for the RAG system.</p>',
        unsafe_allow_html=True,
    )
    st.caption(
        "These are offline system-evaluation metrics, not live scores for chat queries."
    )

    try:
        generation_results = _load_result_file(GENERATION_RESULTS_FILE)
    except (OSError, json.JSONDecodeError, ValueError):
        logger.exception("Could not load generation evaluation results.")
        st.error("Generation evaluation results could not be loaded.")
        generation_results = None
    render_generation_evaluation(generation_results)

    try:
        retrieval_results = _load_result_file(RETRIEVAL_RESULTS_FILE)
    except (OSError, json.JSONDecodeError, ValueError):
        logger.exception("Could not load retrieval evaluation results.")
        st.error("Retrieval evaluation results could not be loaded.")
        retrieval_results = None
    render_retrieval_evaluation(retrieval_results)
    st.info(
        "These scores summarize offline benchmarks only. Dataset coverage "
        "and evaluation variability matter; high scores do not guarantee "
        "production readiness."
    )


def main() -> None:
    st.set_page_config(
        page_title="LLM Research Assistant",
        page_icon="💬",
        layout="wide",
    )
    st.markdown(APP_CSS, unsafe_allow_html=True)
    if "active_page" not in st.session_state:
        st.session_state.active_page = "chat"

    chat_column, evaluation_column, _ = st.columns([1, 1, 6])
    with chat_column:
        if st.button(
            "💬 Chat",
            type="primary" if st.session_state.active_page == "chat" else "secondary",
            use_container_width=True,
        ):
            st.session_state.active_page = "chat"
    with evaluation_column:
        if st.button(
            "📊 Evaluation",
            type=(
                "primary"
                if st.session_state.active_page == "evaluation"
                else "secondary"
            ),
            use_container_width=True,
        ):
            st.session_state.active_page = "evaluation"

    st.divider()
    page = st.session_state.active_page
    if page == "chat":
        _render_chat_page()
    else:
        _render_evaluation_page()


if __name__ == "__main__":
    main()

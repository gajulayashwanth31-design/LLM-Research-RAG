from typing import Any

from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_google_genai import ChatGoogleGenerativeAI

from hybrid_retrieval import hybrid_retrieve_and_rerank


load_dotenv()

MODEL = "gemini-3.1-flash-lite"

llm = ChatGoogleGenerativeAI(
    model=MODEL,
    temperature=0,
)


SYSTEM_PROMPT = """
You are an educational assistant specialized in Large Language Models.

Answer the user's question using only the supplied retrieved context.
Do not use outside knowledge or invent facts.
Explain the answer clearly at a student-friendly level.
Use citations in the form [chunk_id] for factual claims, and only cite chunk IDs
that appear in the supplied context.
If the context does not contain enough information to answer, respond with
exactly this sentence and nothing else:
"I don't have enough information in the provided knowledge base."

Retrieved context:
{context}
"""

def _build_context(documents: list[Document]) -> str:
    """Build model context from document text while retaining chunk references."""
    context_parts = []
    for document in documents:
        chunk_id = document.metadata.get("chunk_id")
        source_label = f"[chunk_id: {chunk_id}]" if chunk_id else "[source]"
        context_parts.append(f"{source_label}\n{document.page_content}")
    return "\n\n".join(context_parts)


def _extract_sources(documents: list[Document]) -> list[dict[str, str]]:
    """Extract source attribution from the final retrieved document metadata."""
    sources: list[dict[str, str]] = []
    seen_chunk_ids: set[str] = set()

    for document in documents:
        metadata = document.metadata
        chunk_id = metadata.get("chunk_id")
        if chunk_id:
            if chunk_id in seen_chunk_ids:
                continue
            seen_chunk_ids.add(chunk_id)
        source: dict[str, str] = {}
        for key in ("paper", "source_file"):
            value = metadata.get(key)
            if value is not None and value != "":
                source[key] = str(value)

        for key in ("Header 1", "Header 2"):
            value = metadata.get(key)
            if value is not None and value != "":
                source[key] = str(value)

        section = _section_from_metadata(metadata)
        if section:
            source["section"] = section

        if chunk_id:
            source["chunk_id"] = str(chunk_id)

        if source:
            sources.append(source)

    return sources


def _extract_retrieved_chunks(documents: list[Document]) -> list[dict[str, Any]]:
    chunks = []
    for document in documents:
        chunk: dict[str, Any] = {
            "chunk_id": document.metadata.get("chunk_id"),
            "text": document.page_content,
        }
        reranker_score = document.metadata.get("reranker_score")
        if reranker_score is not None:
            chunk["reranker_score"] = reranker_score
        chunks.append(chunk)
    return chunks


def _section_from_metadata(metadata: dict[str, Any]) -> str:
    headings = [
        str(metadata[key])
        for key in ("Header 1", "Header 2")
        if metadata.get(key) not in (None, "")
    ]
    return " > ".join(headings)


def _response_text(content: Any) -> str:
    if isinstance(content, str):
        return content.strip()
    if isinstance(content, list):
        text_parts = [
            block
            if isinstance(block, str)
            else block.get("text")
            for block in content
            if isinstance(block, str)
            or (
                isinstance(block, dict)
                and isinstance(block.get("text"), str)
            )
        ]
        return "\n".join(text_parts).strip()
    raise TypeError(
        f"Gemini returned unsupported response content type: "
        f"{type(content).__name__}"
    )


def answer_question(question: str) -> dict[str, Any]:
    # Retrieval happens here; keep the final reranked LangChain Documents intact.
    documents = hybrid_retrieve_and_rerank(
        question,
        semantic_k=20,
        bm25_k=20,
        fusion_k=10,
        final_k=5,
    )

    # Construct Gemini context from page_content and include chunk IDs for citations.
    context = _build_context(documents)

    # Apply grounding instructions to the system prompt before sending the question.
    system_prompt = SYSTEM_PROMPT.format(context=context)
    response = llm.invoke(
        [
            ("system", system_prompt),
            ("human", question),
        ]
    )
    answer = _response_text(response.content)
    if not answer:
        raise ValueError("Gemini returned an empty answer.")

    # Extract attribution only from the final Documents supplied to Gemini.
    sources = _extract_sources(documents)
    retrieved_chunks = _extract_retrieved_chunks(documents)

    return {
        "answer": answer,
        "sources": sources,
        "retrieved_chunks": retrieved_chunks,
    }

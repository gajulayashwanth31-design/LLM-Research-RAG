from threading import Lock

from langchain_core.documents import Document
from sentence_transformers import CrossEncoder


RERANKER_MODEL_NAME = "BAAI/bge-reranker-v2-m3"
_model_lock = Lock()
_cross_encoder: CrossEncoder | None = None


def _get_cross_encoder() -> CrossEncoder:
    global _cross_encoder
    with _model_lock:
        if _cross_encoder is None:
            _cross_encoder = CrossEncoder(RERANKER_MODEL_NAME)
        return _cross_encoder


def rerank_documents(
    query: str,
    documents: list[Document],
    top_k: int = 5,
) -> list[Document]:
    """Rerank documents by cross-encoder relevance, preserving their metadata."""
    if top_k <= 0 or not documents:
        return []

    pairs = [(query, document.page_content) for document in documents]
    scores = _get_cross_encoder().predict(pairs)
    ranked = sorted(
        zip(documents, scores),
        key=lambda item: float(item[1]),
        reverse=True,
    )
    return [
        Document(
            page_content=document.page_content,
            metadata={**document.metadata, "reranker_score": float(score)},
        )
        for document, score in ranked[:top_k]
    ]

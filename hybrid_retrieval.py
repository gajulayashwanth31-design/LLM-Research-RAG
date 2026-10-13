import re
from threading import RLock
from typing import Any

from langchain_chroma import Chroma
from langchain_core.documents import Document
from rank_bm25 import BM25Okapi

from embeddings import get_embedding_model
from retrieval import retrieve_documents
from vector_store import get_vector_store


DEFAULT_RRF_K = 60
_state_lock = RLock()
_vector_store: Chroma | None = None
_bm25_index: BM25Okapi | None = None
_bm25_documents: list[Document] | None = None


def _tokenize(text: str) -> list[str]:
    return re.findall(r"\w+", text.lower())


def _get_vector_store() -> Chroma:
    global _vector_store
    with _state_lock:
        if _vector_store is None:
            _vector_store = get_vector_store(get_embedding_model())
        return _vector_store


def _get_bm25_index() -> tuple[BM25Okapi, list[Document]]:
    global _bm25_index, _bm25_documents
    with _state_lock:
        if _bm25_index is None or _bm25_documents is None:
            stored_chunks: dict[str, Any] = _get_vector_store().get(
                include=["documents", "metadatas"]
            )
            contents = stored_chunks.get("documents") or []
            metadatas = stored_chunks.get("metadatas") or []
            if not contents:
                raise ValueError("Cannot build BM25: the ChromaDB collection is empty.")
            if len(contents) != len(metadatas):
                raise ValueError(
                    "Cannot build BM25: ChromaDB returned inconsistent documents "
                    "and metadata."
                )

            documents: list[Document] = []
            seen_chunk_ids: set[str] = set()
            for content, metadata in zip(contents, metadatas):
                chunk_id = (metadata or {}).get("chunk_id")
                if not chunk_id:
                    raise ValueError(
                        "Cannot build BM25: a stored chunk is missing metadata "
                        "'chunk_id'."
                    )
                if chunk_id in seen_chunk_ids:
                    raise ValueError(
                        f"Cannot build BM25: duplicate chunk_id {chunk_id!r} "
                        "exists in ChromaDB."
                    )
                seen_chunk_ids.add(chunk_id)
                documents.append(
                    Document(page_content=content, metadata=dict(metadata))
                )

            tokenized_documents = [_tokenize(doc.page_content) for doc in documents]
            _bm25_index = BM25Okapi(tokenized_documents)
            _bm25_documents = documents

        return _bm25_index, _bm25_documents


def retrieve_bm25_documents(query: str, k: int = 20) -> list[Document]:
    """Retrieve keyword-matched chunks from the ChromaDB corpus using BM25."""
    if k <= 0:
        return []

    index, documents = _get_bm25_index()
    scores = index.get_scores(_tokenize(query))
    ranked_indices = sorted(
        range(len(documents)),
        key=lambda index: (-scores[index], index),
    )
    return [documents[index] for index in ranked_indices[:k]]


def reciprocal_rank_fusion(
    result_lists: list[list[Document]],
    top_k: int = 10,
    rrf_k: int = DEFAULT_RRF_K,
) -> list[Document]:
    """Fuse ranked document lists using reciprocal rank and chunk_id identity."""
    if top_k <= 0:
        return []
    if rrf_k < 0:
        raise ValueError("rrf_k must be zero or greater.")

    fused: dict[str, tuple[Document, float]] = {}
    for ranked_documents in result_lists:
        seen_in_list: set[str] = set()
        for rank, document in enumerate(ranked_documents, start=1):
            chunk_id = document.metadata.get("chunk_id")
            if not chunk_id:
                raise ValueError(
                    "Cannot fuse retrieved documents: metadata 'chunk_id' is "
                    "missing."
                )
            if chunk_id in seen_in_list:
                continue
            seen_in_list.add(chunk_id)

            previous_document, previous_score = fused.get(
                chunk_id, (document, 0.0)
            )
            fused[chunk_id] = (
                previous_document,
                previous_score + 1.0 / (rrf_k + rank),
            )

    ranked_fusion = sorted(
        fused.values(),
        key=lambda item: item[1],
        reverse=True,
    )
    return [
        Document(
            page_content=document.page_content,
            metadata={**document.metadata, "rrf_score": score},
        )
        for document, score in ranked_fusion[:top_k]
    ]


def retrieve_hybrid_candidates(
    query: str,
    semantic_k: int = 20,
    bm25_k: int = 20,
    fusion_k: int = 10,
    rrf_k: int = DEFAULT_RRF_K,
) -> tuple[list[Document], list[Document], list[Document]]:
    """Return semantic, BM25, and RRF-fused results for inspection or reranking."""
    semantic_documents = retrieve_documents(
        _get_vector_store(),
        query,
        k=semantic_k,
    )
    bm25_documents = retrieve_bm25_documents(query, k=bm25_k)
    fused_documents = reciprocal_rank_fusion(
        [semantic_documents, bm25_documents],
        top_k=fusion_k,
        rrf_k=rrf_k,
    )
    return semantic_documents, bm25_documents, fused_documents


def hybrid_retrieve_and_rerank(
    query: str,
    semantic_k: int = 20,
    bm25_k: int = 20,
    fusion_k: int = 10,
    final_k: int = 5,
) -> list[Document]:
    """Retrieve with semantic and BM25 search, fuse, and cross-encoder rerank."""
    from reranker import rerank_documents

    _, _, fused_documents = retrieve_hybrid_candidates(
        query,
        semantic_k=semantic_k,
        bm25_k=bm25_k,
        fusion_k=fusion_k,
    )
    return rerank_documents(query, fused_documents, top_k=final_k)

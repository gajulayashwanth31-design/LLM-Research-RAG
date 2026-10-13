from langchain_core.documents import Document

from hybrid_retrieval import retrieve_hybrid_candidates
from reranker import rerank_documents


def _print_results(
    title: str,
    documents: list[Document],
    score_key: str | None = None,
) -> None:
    print(f"\n{title}")
    for rank, document in enumerate(documents, start=1):
        chunk_id = document.metadata["chunk_id"]
        source_file = document.metadata.get("source_file", "unknown")
        score = (
            f" | {score_key}: {document.metadata[score_key]:.6f}"
            if score_key
            else ""
        )
        print(f"{rank}. {chunk_id}{score} | source: {source_file}")


if __name__ == "__main__":
    query = "What is self-attention?"
    semantic, bm25, fused = retrieve_hybrid_candidates(query)
    reranked = rerank_documents(query, fused, top_k=5)

    _print_results("SEMANTIC TOP 20", semantic)
    _print_results("BM25 TOP 20", bm25)
    _print_results("RRF TOP 10", fused, score_key="rrf_score")
    _print_results("CROSS-ENCODER TOP 5", reranked, score_key="reranker_score")

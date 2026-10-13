import json
from collections.abc import Callable
from pathlib import Path
from typing import Any

from langchain_core.documents import Document

from hybrid_retrieval import hybrid_retrieve_and_rerank
from retrieval import get_retriever, retrieve_documents


TEST_FILE = Path("evaluation/tests.json")
RESULTS_FILE = Path(__file__).resolve().with_name(
    "retrieval_evaluation_results.json"
)
BASELINE_RETRIEVAL_K = 10


def load_tests() -> list[dict[str, Any]]:
    with TEST_FILE.open("r", encoding="utf-8") as test_file:
        data = json.load(test_file)
    return data["tests"]


def evaluate_pipeline(
    tests: list[dict[str, Any]],
    retrieve: Callable[[str], list[Document]],
) -> list[dict[str, Any]]:
    """Evaluate ranked results only for tests with chunk-level ground truth."""
    results = []
    for test in tests:
        expected_chunk_ids = set(test.get("source_chunks", []))
        if not expected_chunk_ids:
            continue

        documents = retrieve(test["question"])
        relevance = [
            document.metadata.get("chunk_id") in expected_chunk_ids
            for document in documents
        ]
        results.append(
            {
                "id": test["id"],
                "relevance": relevance,
            }
        )
    return results


def calculate_metrics(
    results: list[dict[str, Any]],
) -> dict[str, float | None]:
    """Calculate query-level Recall@K and MRR over labeled queries."""
    if not results:
        return {
            "recall_at_1": None,
            "recall_at_3": None,
            "recall_at_5": None,
            "mrr": None,
        }

    recalls = {}
    for cutoff in (1, 3, 5):
        hits = sum(any(result["relevance"][:cutoff]) for result in results)
        recalls[f"recall_at_{cutoff}"] = hits / len(results)

    reciprocal_ranks = []
    for result in results:
        first_relevant_rank = next(
            (
                rank
                for rank, is_relevant in enumerate(result["relevance"], start=1)
                if is_relevant
            ),
            None,
        )
        reciprocal_ranks.append(
            1 / first_relevant_rank if first_relevant_rank is not None else 0.0
        )

    return {
        **recalls,
        "mrr": sum(reciprocal_ranks) / len(results),
    }


def _format_metric(value: float | None, *, percentage: bool = False) -> str:
    if value is None:
        return "N/A"
    if percentage:
        return f"{value * 100:.2f}%"
    return f"{value:.4f}"


def _print_metrics(metrics: dict[str, float | None]) -> None:
    print(f"Recall@1: {_format_metric(metrics['recall_at_1'], percentage=True)}")
    print(f"Recall@3: {_format_metric(metrics['recall_at_3'], percentage=True)}")
    print(f"Recall@5: {_format_metric(metrics['recall_at_5'], percentage=True)}")
    print(f"MRR: {_format_metric(metrics['mrr'])}")


def _print_improvement(
    baseline: dict[str, float | None],
    hybrid: dict[str, float | None],
) -> None:
    for label, key in (
        ("Recall@1", "recall_at_1"),
        ("Recall@3", "recall_at_3"),
        ("Recall@5", "recall_at_5"),
    ):
        baseline_value = baseline[key]
        hybrid_value = hybrid[key]
        if baseline_value is None or hybrid_value is None:
            print(f"{label}: N/A")
        else:
            difference = (hybrid_value - baseline_value) * 100
            print(f"{label}: {difference:+.2f} percentage points")

    baseline_mrr = baseline["mrr"]
    hybrid_mrr = hybrid["mrr"]
    if baseline_mrr is None or hybrid_mrr is None:
        print("MRR: N/A")
    else:
        print(f"MRR: {hybrid_mrr - baseline_mrr:+.4f}")


def main() -> None:
    tests = load_tests()
    labeled_tests = [test for test in tests if test.get("source_chunks")]
    unlabeled_tests = [test for test in tests if not test.get("source_chunks")]

    print(f"Loaded {len(tests)} evaluation queries.")
    print("Loading baseline BGE + Chroma store...")
    vector_store = get_retriever()

    baseline_results = evaluate_pipeline(
        labeled_tests,
        lambda query: retrieve_documents(
            vector_store,
            query,
            k=BASELINE_RETRIEVAL_K,
        ),
    )

    hybrid_results = evaluate_pipeline(
        labeled_tests,
        lambda query: hybrid_retrieve_and_rerank(
            query,
            semantic_k=20,
            bm25_k=20,
            fusion_k=10,
            final_k=5,
        ),
    )

    baseline_metrics = calculate_metrics(baseline_results)
    hybrid_metrics = calculate_metrics(hybrid_results)

    with RESULTS_FILE.open("w", encoding="utf-8") as results_file:
        json.dump(
            {
                "summary": {
                    "total_tests": len(tests),
                    "labeled_tests": len(labeled_tests),
                    "unlabeled_tests": len(unlabeled_tests),
                },
                "baseline_metrics": baseline_metrics,
                "hybrid_metrics": hybrid_metrics,
            },
            results_file,
            ensure_ascii=False,
            indent=2,
        )
        results_file.write("\n")

    print("\n" + "=" * 50)
    print("RETRIEVAL EVALUATION RESULTS")
    print("=" * 50)
    print(f"\nNumber of queries: {len(tests)}")
    print(f"Labeled queries: {len(labeled_tests)}")
    print(f"Unlabeled queries: {len(unlabeled_tests)}")

    print("\nBASELINE — BGE + Chroma")
    _print_metrics(baseline_metrics)

    print("\nHYBRID + RERANKER")
    print("Semantic Top 20 + BM25 Top 20")
    print("→ RRF Top 10")
    print("→ Cross-Encoder Top 5")
    _print_metrics(hybrid_metrics)

    print("\nIMPROVEMENT")
    _print_improvement(baseline_metrics, hybrid_metrics)
    print(f"\nResults saved to: {RESULTS_FILE}")


if __name__ == "__main__":
    main()

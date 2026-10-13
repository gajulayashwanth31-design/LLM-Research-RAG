import json
import os
import tempfile
import time
from pathlib import Path
from typing import Any

from generator import answer_question


EVALUATION_DIRECTORY = Path(__file__).resolve().parent
TEST_FILE = EVALUATION_DIRECTORY / "tests.json"
RESULTS_FILE = EVALUATION_DIRECTORY / "generation_results.json"
BATCH_SIZE = 10
MIN_REQUEST_INTERVAL_SECONDS = 6.0


def load_tests() -> list[dict[str, Any]]:
    with TEST_FILE.open("r", encoding="utf-8") as test_file:
        data = json.load(test_file)
    tests = data["tests"]
    test_ids = [test["id"] for test in tests]
    if len(test_ids) != len(set(test_ids)):
        raise ValueError("Evaluation tests contain duplicate IDs.")
    return tests


def load_results() -> list[dict[str, Any]]:
    if not RESULTS_FILE.exists():
        return []

    with RESULTS_FILE.open("r", encoding="utf-8") as results_file:
        results = json.load(results_file)
    if not isinstance(results, list):
        raise ValueError(
            f"{RESULTS_FILE} must contain a JSON array of generation results."
        )

    result_ids = []
    for result in results:
        if not isinstance(result, dict) or not isinstance(result.get("id"), str):
            raise ValueError(
                f"{RESULTS_FILE} contains a result without a string test ID."
            )
        result_ids.append(result["id"])
    if len(result_ids) != len(set(result_ids)):
        raise ValueError(f"{RESULTS_FILE} contains duplicate test IDs.")
    return results


def save_results(results: list[dict[str, Any]]) -> None:
    """Atomically replace the results file so it is never left partial."""
    temporary_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=RESULTS_FILE.parent,
            prefix=f".{RESULTS_FILE.name}.",
            suffix=".tmp",
            delete=False,
        ) as temporary_file:
            temporary_path = Path(temporary_file.name)
            json.dump(results, temporary_file, ensure_ascii=False, indent=2)
            temporary_file.write("\n")
            temporary_file.flush()
            os.fsync(temporary_file.fileno())

        os.replace(temporary_path, RESULTS_FILE)
        temporary_path = None
    finally:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)


def _wait_for_rate_limit(last_request_started_at: float | None) -> float:
    if last_request_started_at is not None:
        elapsed = time.monotonic() - last_request_started_at
        remaining_wait = MIN_REQUEST_INTERVAL_SECONDS - elapsed
        if remaining_wait > 0:
            time.sleep(remaining_wait)
    return time.monotonic()


def _make_result(
    test: dict[str, Any],
    generated: dict[str, Any],
) -> dict[str, Any]:
    answer = generated["answer"]
    sources = generated["sources"]
    if not isinstance(answer, str):
        raise TypeError("answer_question() returned a non-string answer.")
    if not isinstance(sources, list):
        raise TypeError("answer_question() returned non-list sources.")

    return {
        "id": test["id"],
        "question": test["question"],
        "reference_answer": test["reference_answer"],
        "expected_facts": test["expected_facts"],
        "generated_answer": answer,
        "sources": sources,
        "answerable": test["answerable"],
        "category": test["category"],
        "difficulty": test["difficulty"],
    }


def run() -> None:
    tests = load_tests()
    answerable_tests = [test for test in tests if test.get("answerable") is True]
    results = load_results()
    completed_ids = {result["id"] for result in results}
    answerable_ids = {test["id"] for test in answerable_tests}
    already_completed = len(answerable_ids & completed_ids)

    # Ensure a valid results file exists before the first model call.
    save_results(results)

    batches = [
        answerable_tests[start : start + BATCH_SIZE]
        for start in range(0, len(answerable_tests), BATCH_SIZE)
    ]

    generated_this_run = 0
    failed_count = 0
    last_request_started_at: float | None = None

    for batch_number, batch in enumerate(batches, start=1):
        batch_generated = 0
        batch_failed = 0
        batch_skipped = 0

        for test in batch:
            if test["id"] in completed_ids:
                batch_skipped += 1
                continue

            last_request_started_at = _wait_for_rate_limit(
                last_request_started_at
            )
            try:
                generated = answer_question(test["question"])
                result = _make_result(test, generated)
            except Exception as error:
                failed_count += 1
                batch_failed += 1
                print(f"Failed test {test['id']}: {error}")
                continue

            results.append(result)
            completed_ids.add(test["id"])
            generated_this_run += 1
            batch_generated += 1

        # Persist every completed batch; failed tests remain eligible to retry.
        save_results(results)
        remaining = sum(
            test["id"] not in completed_ids for test in answerable_tests
        )
        print(f"\nBatch {batch_number}/{len(batches)}")
        print(f"Successfully generated: {batch_generated}")
        print(f"Skipped/already completed: {batch_skipped}")
        print(f"Failed in batch: {batch_failed}")
        print(f"Remaining tests: {remaining}")

    remaining = sum(
        test["id"] not in completed_ids for test in answerable_tests
    )
    print("\n" + "=" * 50)
    print("GENERATION EVALUATION RUN")
    print("=" * 50)
    print(f"Total tests: {len(tests)}")
    print(f"Answerable tests: {len(answerable_tests)}")
    print(f"Already completed: {already_completed}")
    print(f"Generated this run: {generated_this_run}")
    print(f"Failed: {failed_count}")
    print(f"Remaining: {remaining}")
    print("Results saved to: evaluation/generation_results.json")


if __name__ == "__main__":
    run()

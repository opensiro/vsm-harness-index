from pathlib import Path
import sys

FIXTURE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FIXTURE / "src"))

from dispatch import DispatchRecord, dispatch  # noqa: E402


def test_retryable_statuses_are_classified() -> None:
    assert dispatch("worker-b", 429).retryable is True
    assert dispatch("worker-b", 503).retryable is True
    assert dispatch("worker-b", 200).retryable is False
    assert dispatch("worker-b", 400).retryable is False


def test_existing_fields_are_preserved() -> None:
    record = dispatch("worker-b", 503)
    assert isinstance(record, DispatchRecord)
    assert record.target == "worker-b"
    assert record.status == 503

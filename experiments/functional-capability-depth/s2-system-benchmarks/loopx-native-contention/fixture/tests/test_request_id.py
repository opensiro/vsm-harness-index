from pathlib import Path
import sys

FIXTURE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FIXTURE / "src"))

from dispatch import DispatchRecord, dispatch  # noqa: E402


def test_request_id_is_preserved() -> None:
    record = dispatch("worker-a", 200, "req-123")
    assert isinstance(record, DispatchRecord)
    assert record.target == "worker-a"
    assert record.status == 200
    assert record.request_id == "req-123"

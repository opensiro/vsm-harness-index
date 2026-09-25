from src.envelope import make_response
from src.retry import should_retry


def test_retryable_statuses_follow_current_response_contract() -> None:
    assert should_retry(make_response(429)) is True
    assert should_retry(make_response(503)) is True
    assert should_retry(make_response(200)) is False

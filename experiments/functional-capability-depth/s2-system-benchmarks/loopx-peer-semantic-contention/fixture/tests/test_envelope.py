from src.envelope import make_response


def test_make_response_uses_code_key() -> None:
    assert make_response(200) == {"code": 200}

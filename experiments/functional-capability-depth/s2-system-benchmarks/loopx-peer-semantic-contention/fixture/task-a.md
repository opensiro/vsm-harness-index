# Task A — producer payload migration

Migrate the response payload contract in `src/envelope.py` from the key `status` to the key `code`.

Required behavior:

- `make_response(200)` returns `{"code": 200}`.
- Preserve the integer status value.
- Modify only `src/envelope.py` and `tests/test_envelope.py` if a test change is necessary.
- Do not edit `src/retry.py` or `tests/test_retry.py`.
- Do not implement retryability; that belongs to Task B.

Acceptance test: `tests/test_envelope.py`.

Declared write scopes at preregistration:

- `src/envelope.py`
- `tests/test_envelope.py`

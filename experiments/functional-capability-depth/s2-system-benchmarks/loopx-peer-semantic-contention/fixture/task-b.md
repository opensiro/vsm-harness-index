# Task B — retryability against the current producer contract

Implement retryability in `src/retry.py` using the response payload contract that is present in the worker's starting tree.

Required behavior:

- `should_retry(make_response(429))` is `True`.
- `should_retry(make_response(503))` is `True`.
- `should_retry(make_response(200))` is `False`.
- Read the status value from the **current** payload returned by `src/envelope.py`; do not assume a key that is not present in the starting tree.
- Modify only `src/retry.py` and `tests/test_retry.py` if a test change is necessary.
- Do not edit `src/envelope.py` or `tests/test_envelope.py`.
- Do not migrate the producer payload contract; that belongs to Task A.

Acceptance test: `tests/test_retry.py`.

Declared write scopes at preregistration:

- `src/retry.py`
- `tests/test_retry.py`

# Task B — retryability classification

Modify only what is necessary so `DispatchRecord` and `dispatch()` expose whether the status is retryable.

Required behavior:

- `DispatchRecord` has a `retryable: bool` field.
- `dispatch(target, status)` returns `retryable=True` for status codes 429 and 503, and `False` otherwise.
- Preserve the existing `target` and `status` behavior.
- Do not implement request-id propagation; that belongs to the other task.

Acceptance test: `tests/test_retryable.py`.

Known write surface at preregistration: `src/dispatch.py`.

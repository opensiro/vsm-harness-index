# Task A — request-id propagation

Modify only what is necessary so `DispatchRecord` and `dispatch()` preserve a caller-supplied request id.

Required behavior:

- `DispatchRecord` has a `request_id: str` field.
- `dispatch(target, status, request_id)` returns a record whose `request_id` equals the supplied value.
- Preserve the existing `target` and `status` behavior.
- Do not implement retryability classification; that belongs to the other task.

Acceptance test: `tests/test_request_id.py`.

Known write surface at preregistration: `src/dispatch.py`.

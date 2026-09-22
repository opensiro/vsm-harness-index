# T2 — multi-file operational change

Implement the retry-policy behavior across the existing application files.

Requirements:

- `settings.parse_retries(env)` reads `APP_RETRIES` from the supplied mapping;
- missing, blank, non-integer, negative, or values greater than `5` return the default `3`;
- integer values from `0` through `5` are accepted unchanged;
- `worker.build_job(env)` must use `settings.parse_retries(env)` rather than a hard-coded retry count;
- preserve the existing return shape of `worker.build_job`;
- do not add third-party dependencies;
- avoid unrelated changes.

Before treating the task as complete, run:

```bash
python check.py
```

and make sure it succeeds.

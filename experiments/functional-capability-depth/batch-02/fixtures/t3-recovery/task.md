# T3 — recovery after transient verification failure

Fix `text_utils.slugify(text)`.

Required behavior:

- lowercase the input;
- trim leading/trailing whitespace or hyphens;
- collapse every run of whitespace and/or hyphens into a single `-`;
- preserve letters and digits;
- do not add third-party dependencies;
- avoid unrelated changes.

Before treating the task as complete, run:

```bash
python verify.py
```

until verification succeeds.

A verification failure must not be treated as successful completion.

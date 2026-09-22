# T1 — edit fidelity

Fix `math_utils.clamp(value, lower, upper)` so that both bounds are inclusive.

Requirements:

- preserve the existing function signature;
- preserve `ValueError` when `lower > upper`;
- values below `lower` return `lower`;
- values above `upper` return `upper`;
- a value exactly equal to `upper` must return `upper`;
- do not add third-party dependencies;
- avoid unrelated changes.

Before treating the task as complete, run:

```bash
python check.py
```

and make sure it succeeds.

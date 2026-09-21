# Analytics time convention

Temporal analytics in this directory use one primary cohort date:

```text
data/catalog.psv:repository_created_at
```

`Period` means the **GitHub repository creation period**.

For example, `2026-Q3` means that the repository itself was created on GitHub between July and September 2026. It does **not** mean that the harness was released, assessed, last updated, or that a particular VSM function was implemented during that quarter.

Year and quarter are derived from `repository_created_at`; they are not maintained as separate catalog fields.

The Index snapshot date is machine-readable provenance stored in `data/metrics.json`. It is not another cohort axis and is not shown as a separate analytics view.

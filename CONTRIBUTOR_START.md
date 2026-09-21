# Contributor start

There are three common ways to contribute to the Index.

## Review a queued harness assessment

Start with an open frozen `[Assessment batch]` issue. Read its Manual assessment board, take only the row marked `NEXT`, and keep the supplied repository revision pinned.

Before semantic work, read current `main` of:

- `opensiro/vsm-harness-profile` for VSM semantics;
- `opensiro/vsm-harness-skills` for the assessment Methodology and artifact contract.

This repository owns the queue/admission/provenance workflow, not a separate assessment format.

## Suggest a new harness

Open a `[Harness suggestion]` issue with the primary repository URL and a short explanation of why it belongs in an agent-harness index. Maintainers own catalog placement, provenance normalization, deduplication, and batching.

## Request or perform an assessment re-review

Open an `[Assessment re-review]` issue when stronger primary evidence may change a canonical assessment or a newer upstream revision materially changes the harness.

Index bookkeeping distinguishes:

- **same-ref correction / semantic revalidation** — the accepted `review_ref` stays fixed;
- **new-ref reassessment** — a newer commit becomes the accepted review boundary.

The semantic reassessment itself must follow the applicable `vsm-harness-skills` Methodology. The Index records the accepted boundary, freshness, reassessment history, signatures, and generated views.

For the full repository workflow, see [`CONTRIBUTING.md`](CONTRIBUTING.md). For Index-owned lifecycle/provenance rules, see [`INDEXING.md`](INDEXING.md).

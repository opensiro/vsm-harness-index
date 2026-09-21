# Agent entry point

This file is a routing surface for coding/research agents working in `opensiro/vsm-harness-index`. It does not redefine VSM semantics or the assessment procedure.

## Start here

1. Read [README.md](README.md) for the repository overview and source-of-truth boundary.
2. Read [INDEXING.md](INDEXING.md) for Index-owned lifecycle, provenance, reassessment bookkeeping, and publication rules.
3. Read [CONTRIBUTING.md](CONTRIBUTING.md) for the live contribution workflow.
4. For plain-language / visual orientation only, see [opensiro.com](https://opensiro.com) and the [VSMLite / VSM poster](https://opensiro.com/vsm.html). The website is non-normative.
5. Before every semantic assessment row, read current `main` of:
   - `opensiro/vsm-harness-profile` for normative VSM semantics;
   - `opensiro/vsm-harness-skills` for the active assessment Methodology.

## Assessment task rule

For sequential assessment batches, the default contribution unit is the row marked `NEXT` in the issue's Manual assessment board.

Before semantic work, assemble the current task envelope mechanically:

```bash
python scripts/assessment_preflight.py <assessment-batch-issue-number>
```

Use `--json` when another tool or agent needs a machine-readable envelope. The preflight resolves the current `NEXT` row, frozen repository/ref, suggested assessment path, active Profile/Methodology contract, task boundaries, and final validation commands. It fails closed if the Manual assessment board and frozen candidate table disagree.

The preflight is Index routing/tooling only. It does not perform VSM interpretation and does not replace reading current Profile/Methodology.

- Do not take a later queued row.
- Do not silently replace the issue's frozen `review_ref` with a newer upstream head.
- Use the assessment artifact format and classification procedure from the active Skills Methodology.
- Treat `assessments/<harness_id>.md` as the repository-relative research artifact; `TLDR.md`, `RANKINGS.md`, and other views are derived materializations.

If the issue's explicit task contract differs from a generic instruction here, follow the issue for the bounded work item while preserving the canonical Profile / Methodology / Index ownership boundaries above.

## Before completion

Use the checks required by the current issue and Methodology. For canonical Index changes, the repository-level final gate is:

```bash
python scripts/check_index.py
```

Run the version-pinned Skills assessment-contract checker and any additional rendering checks required by the active contribution workflow before declaring the work complete.

## Routing outside Index

Repository-local assessment instances, catalog/provenance, reassessment history, signatures, and generated Index work stay here.

Changes to assessment format, publication-state classification, synthesis semantics, or ranking projection belong in `opensiro/vsm-harness-skills`.

Changes to VSM semantics belong in `opensiro/vsm-harness-profile`.

Questions about shared contributor authority, escalation, cross-repository coordination, milestone sequencing, or the bounded VSM Harness OSS control plane route to [`opensiro/vsm-oss-organization`](https://github.com/opensiro/vsm-oss-organization) and its `CONTRIBUTOR_START.md`.

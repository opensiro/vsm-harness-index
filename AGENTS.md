# Agent entry point

This file is a routing surface for coding/research agents working in `opensiro/vsm-harness-index`. It does not redefine VSM semantics or the assessment procedure.

## Start here

1. Read [README.md](README.md) for this repository's source-of-truth boundary.
2. Read [CONTRIBUTING.md](CONTRIBUTING.md) for the live contribution workflow and acceptance contract.
3. For plain-language / visual orientation only, see [opensiro.com](https://opensiro.com) and the [VSMLite / VSM poster](https://opensiro.com/vsm.html). The website is non-normative.
4. Before every assessment row, read current `main` of:
   - `opensiro/vsm-harness-profile` for normative VSM semantics;
   - `opensiro/vsm-harness-skills` for the active assessment methodology.

## Assessment task rule

For sequential assessment batches, the default contribution unit is the row marked `NEXT` in the issue's Manual assessment board.

- Do not take a later queued row.
- Do not silently replace the issue's frozen `review_ref` with a newer upstream head.
- Fix the first-party system boundary before mapping functions.
- Map the organizational function first; classify ownership/autonomy second.
- Do not infer S2/S3/S3*/S4/S5 from component names or feature names.
- Treat `assessments/<harness_id>.md` as the repository-relative research artifact; `TLDR.md` and `RANKINGS.md` are derived views.

If the issue's explicit task contract differs from a generic instruction here, follow the issue for the bounded work item while preserving the canonical Profile / Methodology boundaries above.

## Before completion

Use the checks required by the current issue and methodology. For canonical Index changes, the repository-level final gate is:

```bash
python scripts/check_index.py
```

Run any additional assessment-contract or rendering checks required by the active methodology / contribution workflow before declaring the work complete.

## Routing outside Index

Repository-local assessment, catalog/provenance, signatures, and generated Index work stays here.

Questions about shared contributor authority, escalation, cross-repository coordination, milestone sequencing, or the bounded VSM Harness OSS control plane route to [`opensiro/vsm-oss-organization`](https://github.com/opensiro/vsm-oss-organization) and its `CONTRIBUTOR_START.md`.

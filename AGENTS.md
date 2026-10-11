# Agent entry point

`README.md` is the public handoff surface for this repository. Start there and follow its **I'm AI** route into the shared `START_HERE.md` bootstrap before substantial work.

This file is not a parallel bootstrap or cross-repository routing source. It contains only Index-local agent guidance after the shared bootstrap has resolved the task to `opensiro/vsm-harness-index`.

## After the bootstrap returns here

1. Read the exact governing issue, PR, frozen batch, or other task artifact.
2. Read [`CONTRIBUTING.md`](CONTRIBUTING.md) for the actionable Index contribution workflow.
3. Read [`INDEXING.md`](INDEXING.md) for Index-owned lifecycle, provenance, reassessment bookkeeping, and publication rules.
4. Preserve the task's frozen refs, evidence boundary, admission rules, and stop conditions.

For sequential assessment batches, assemble the task envelope mechanically before semantic work:

```bash
python scripts/assessment_preflight.py <assessment-batch-issue-number>
```

Use `--json` when another tool or agent needs a machine-readable envelope. The preflight resolves the current `NEXT` row, frozen repository/ref, suggested assessment path, active Profile/Methodology contract, task boundaries, and final validation commands. It fails closed if the Manual assessment board and frozen candidate table disagree.

The preflight is Index routing/tooling only. It does not perform VSM interpretation or replace the active Skills Methodology.

- Do not take a later queued row unless the governing issue explicitly grants that scope.
- Do not silently replace a frozen `review_ref` with a newer upstream head.
- Use the assessment artifact format and classification procedure from the active Skills Methodology.
- Treat `assessments/<harness_id>.md` as the repository-relative research artifact; `TLDR.md`, `RANKINGS.md`, and other views are derived materializations.

## Before completion

Use the checks required by the current issue and Methodology. For canonical Index changes, the repository-level final gate is:

```bash
python scripts/check_index.py
```

Run the version-pinned Skills assessment-contract checker and any additional rendering checks required by the active contribution workflow before declaring the work complete.

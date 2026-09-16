# Reassessment rounds

This directory tracks longitudinal passes over already assessed harnesses.

A **round** is the durable unit of longitudinal review. Batch issues and PRs may split the work operationally, but all harnesses in a round share the same frozen scope and upstream observation cutoff.

## File naming

Use:

```text
R<sequence>-YYYY-MM-DD.md
```

where the date is the round's `cutoff_at` date, for example:

```text
R1-2026-12-01.md
R2-2027-03-01.md
```

Do not reuse a round ID.

## Round template

```markdown
# Reassessment Round R1

- Opened: 2026-12-01
- Cutoff: 2026-12-01
- Closed: —
- Status: in-progress
- Scope: catalog positions 1–82

## Purpose

Recheck the frozen scope against upstream development through the cutoff date and determine whether each canonical assessment remains valid.

## Progress

| Harness | Previous review ref | Checked ref | Checked at | Outcome | Changed functions | Evidence |
|---|---|---|---|---|---|---|
| `agno` | `44219f8…` | `91abcdef…` | 2026-12-01 | `no-material-change` | — | [upstream diff](...) |

## Completion

The round is complete only when every harness in the frozen scope has a recorded outcome in both this round file and `data/reassessment-history.psv`.
```

## Per-harness outcomes

Use exactly one of:

- `no-upstream-change`
- `no-material-change`
- `reassessed-unchanged`
- `reassessed-changed`
- `same-ref-correction`
- `blocked`

See `METHODOLOGY.md` for semantics.

`blocked` is a historical round outcome, not a successful freshness check. It keeps `accepted_review_ref` equal to `previous_review_ref` and must not advance the assessment's `last_checked_*` or `last_reassessment_round` fields.

## Canonical assessment updates

The round file and history are append-only historical records. `assessments/<harness_id>.md` remains the canonical current assessment.

After a successful round check (any outcome except `blocked`), update its front matter with the complete freshness set:

```yaml
last_checked_ref: <40-character commit>
last_checked_at: YYYY-MM-DD
assessment_changed_at: YYYY-MM-DD
last_reassessment_round: R1
```

`last_checked_*` advances on every successful longitudinal check. `assessment_changed_at` advances only when the canonical assessment materially changes. A `no-material-change` event can therefore advance `last_checked_at` while leaving `reviewed_at`, `review_ref`, and `assessment_changed_at` unchanged.

If a new-ref reassessment is accepted, also update `review_ref`, `reviewed_at`, and the matching `data/catalog.psv` review boundary. If the accepted assessment materially changes, update `assessment_changed_at` to that reassessment date.

For `reassessed-unchanged` and `reassessed-changed`, `accepted_review_ref` must equal the new `checked_ref` and must differ from `previous_review_ref`. For `same-ref-correction`, all three refs remain at the existing accepted boundary.

## History row

Append one row per harness per round to `data/reassessment-history.psv`:

```text
round_id|harness_id|previous_review_ref|checked_ref|accepted_review_ref|checked_at|outcome|changed_functions|evidence
```

`changed_functions` should be `—` when none changed, or a comma-separated set such as `S3,S4`. `evidence` should contain stable primary-evidence or PR links; separate multiple links with spaces or semicolons, never `|`.

Do not rewrite an older history row to reflect a later interpretation. If a historical event itself needs correction, use a dedicated corrective commit with an explicit explanation rather than silently collapsing the timeline.

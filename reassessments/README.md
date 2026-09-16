# Reassessment rounds

This directory tracks longitudinal passes over already assessed harnesses.

A **round** is the durable unit of longitudinal review. Batch issues and PRs may split the work operationally, but all harnesses in a round share the same frozen scope and upstream observation cutoff.

A reassessment is also **specification-relative**. Every completed harness check records which VSM Harness Profile version and which `assess-vsm-harness` procedure version were used. This makes a semantic Profile update independently trackable from an upstream repository update.

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
- Profile version: 0.2.0
- Assessment procedure version: 0.2.0

## Purpose

Recheck the frozen scope against upstream development through the cutoff date and against the declared assessment semantics, then determine whether each canonical assessment remains valid.

## Progress

| Harness | Previous review ref | Checked ref | Checked at | Profile | Procedure | Outcome | Changed functions | Evidence |
|---|---|---|---|---|---|---|---|---|
| `agno` | `44219f8…` | `91abcdef…` | 2026-12-01 | `0.2.0` | `0.2.0` | `no-material-change` | — | [upstream diff](...) |

## Completion

The round is complete only when every harness in the frozen scope has a recorded outcome in both this round file and `data/reassessment-history.psv`.
```

A round should normally use one Profile/procedure pair. If a long-running round crosses a semantic release, either freeze it on the original pair or close it and start a new round; do not silently mix assessment semantics inside one longitudinal unit.

## Per-harness outcomes

Use exactly one of:

- `no-upstream-change`
- `no-material-change`
- `reassessed-unchanged`
- `reassessed-changed`
- `same-ref-correction`
- `blocked`

See `METHODOLOGY.md` for semantics.

`blocked` is a historical round outcome, not a successful freshness check. It keeps `accepted_review_ref` equal to `previous_review_ref` and must not advance the assessment's `last_checked_*`, `last_reassessment_round`, or accepted spec-provenance fields.

## Canonical assessment updates

The round file and history are append-only historical records. `assessments/<harness_id>.md` remains the canonical current assessment.

After a successful round check (any outcome except `blocked`), update its front matter with the complete freshness set and the spec pair used for that successful check:

```yaml
profile_version: 0.2.0
assessment_procedure_version: 0.2.0
last_checked_ref: <40-character commit>
last_checked_at: YYYY-MM-DD
assessment_changed_at: YYYY-MM-DD
last_reassessment_round: R1
```

`last_checked_*` advances on every successful longitudinal check. `assessment_changed_at` advances only when the canonical assessment materially changes. A `no-material-change` event can therefore advance `last_checked_at` and the accepted spec-provenance pair while leaving `reviewed_at`, `review_ref`, and `assessment_changed_at` unchanged.

This distinction matters when the upstream repository did not materially change but the assessment semantics did. A successful check under a newer Profile confirms that the current canonical assessment remains valid under the newer semantics; the front matter then records that newer Profile/procedure pair without pretending the upstream assessment boundary changed.

If a new-ref reassessment is accepted, also update `review_ref`, `reviewed_at`, and the matching `data/catalog.psv` review boundary. If the accepted assessment materially changes, update `assessment_changed_at` to that reassessment date.

For `reassessed-unchanged` and `reassessed-changed`, `accepted_review_ref` must equal the new `checked_ref` and must differ from `previous_review_ref`. For `same-ref-correction`, all three refs remain at the existing accepted boundary.

Legacy assessments created before explicit version tracking may omit `profile_version` and `assessment_procedure_version`. Do not fabricate a historical version. Their first successful version-aware reassessment should populate both fields.

## History row

Append one row per harness per round to `data/reassessment-history.psv`:

```text
round_id|harness_id|previous_review_ref|checked_ref|accepted_review_ref|checked_at|profile_version|assessment_procedure_version|outcome|changed_functions|evidence
```

`profile_version` and `assessment_procedure_version` are the exact semantics used for that check. They are required on every new history row.

`changed_functions` should be `—` when none changed, or a comma-separated set such as `S3,S4`. `evidence` should contain stable primary-evidence or PR links; separate multiple links with spaces or semicolons, never `|`.

Do not rewrite an older history row to reflect a later interpretation. If a historical event itself needs correction, use a dedicated corrective commit with an explicit explanation rather than silently collapsing the timeline.

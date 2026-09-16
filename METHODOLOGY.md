# Indexing methodology

`vsm-harness-index` does not define VSM. It applies:

1. [VSM Harness Profile](https://github.com/opensiro/vsm-harness-profile/blob/main/PROFILE.md) for organizational semantics;
2. [`assess-vsm-harness`](https://github.com/opensiro/vsm-skills/tree/main/skills/assess-vsm-harness) for repository evidence and autonomy classification;
3. the ordered synthesis procedure in `vsm-skills/SYNTHESIS.md` for cohort-relative signatures;
4. this document for publication, continuous indexing, and reassessment rules.

## Artifact separation

Three artifact classes are intentionally separate.

**Assessment.** `assessments/<harness_id>.md` is repository-relative and revision-relative. It stores the review boundary, repository architecture, VSM mappings, evidence, uncertainty, and autonomy states.

**Signature.** `data/signatures.psv` is cohort-relative. It may change when the ordered cohort changes or when an earlier assessment is corrected. It cannot change an assessment state or introduce a repository claim absent from the assessment.

**Ranking.** `RANKINGS.md` is deterministic. It counts recorded autonomy states and never substitutes a numerical maturity model for the categorical evidence.

`data/catalog.psv` is separate from all three: it is the discovery/order/provenance registry. It contains repository identity, chronology, source membership, and pinned review-boundary metadata (`review_ref`, `pinned_at`), not VSM classifications.

## Review boundary

Each assessment names one harness at a pinned commit where possible. Framework, deployed application, vendor organization, and a child agent are different systems-in-focus and must not be silently mixed.

Use the standard documented distribution. Generic extensibility does not earn a positive autonomy state merely because custom code could implement a VSM function.

## Function before autonomy

For every S1, S2, S3, S3*, S4, and S5 claim:

1. establish the organizational function from behavior and relationships;
2. identify the responsible actor/mechanism;
3. identify the relevant decision right or feedback path;
4. determine runtime ownership;
5. only then assign `A/C/P/—/?`.

In particular, delegation is not S2 without interference regulation among operations; a manager is not S3 without whole-system current authority; a routine verifier is not S3*; planning/learning/event reaction is not S4 without external-and-prospective adaptation; and static policy text is not S5 closure.

## Ordered synthesis and continuous indexing

The discovery cohort is ordered by `catalog_position`. New admitted harnesses are appended chronologically under the current continuous-index policy; existing positions are not renumbered merely because a project is reassessed.

After a new assessment is complete, compare it with all earlier completed assessments and record the smallest informative evidence-backed architectural distinction in `data/signatures.psv`. Identical autonomy vectors are valid. Never alter a state to manufacture signature uniqueness.

If an existing assessment changes, re-check its signature and later cohort-relative signatures whose distinguishing statement may depend on the changed assessment. The assessment itself remains repository-relative; the synthesis layer is allowed to change because its comparison set changed.

Public presentation order is separate from synthesis order. `TLDR.md` is displayed newest-first using `repository_created_at`; changing display order does not change `catalog_position`, assessment meaning, or sequential signature ancestry.

## Re-review and reassessment

An existing assessment can be revisited in two ways:

- **same-ref correction** — the pinned repository revision does not change; stronger evidence or a category-error correction changes the interpretation. The catalog row remains unchanged.
- **new-ref reassessment** — a newer upstream commit materially changes the reviewed architecture or runtime behavior. The accepted reassessment updates the catalog `review_ref` and `pinned_at`; the standalone assessment records its own `reviewed_at`.

A re-review request is evidence-led rather than grade-led. The proposed replacement state is advisory; the reviewer must independently re-establish the VSM function, decision right, ownership, standard-distribution closure, and counter-evidence.

For disputed positive metasystem claims, the re-review must actively try to falsify the claim. In particular:

- S2 requires a real interference/oscillation problem among operational units plus a regulating mechanism or actor;
- S3 requires current-whole authority, not merely task decomposition or result aggregation;
- S3* requires materially complementary and sufficiently independent access to operational reality plus a path for findings to affect control;
- S4 requires external-and-prospective distinctions, adaptation options, and coupling back to present capability;
- S5 requires legitimate ultimate authority or an operational parent-governed closure path, not static policy text.

If the strongest available primary evidence cannot support either a positive state or a defensible no-path conclusion, use `?` rather than forcing certainty.

## Reassessment rounds

Longitudinal reassessment is organized into dated **rounds**. A round is a bounded pass over harnesses that already have completed baseline assessments. Its purpose is to determine whether upstream development since the previous review has introduced, removed, or materially changed functionality relevant to the VSM assessment.

The initial assessment is the baseline and is not itself a reassessment round. `R1` is the first longitudinal pass after that baseline.

Each round records:

- `round_id` — sequential identifier such as `R1`, `R2`, `R3`;
- `opened_at` — date the round starts;
- `cutoff_at` — upstream observation cutoff for the round;
- `closed_at` — completion date when closed;
- `scope` — the frozen catalog positions or harness IDs included in the round;
- `status` — `open`, `in-progress`, or `complete`.

The scope is frozen when the round starts. Harnesses admitted after the cutoff enter a later round rather than extending an active round indefinitely. A round may be executed through any number of batch issues or PRs; batches are operational units, while the round is the longitudinal unit of record.

For every harness in scope, record the previously accepted `review_ref`, the newest upstream `checked_ref` inspected during the round, the inspection date, the outcome, changed VSM functions if any, and links to the relevant evidence or PR.

A newer upstream commit does **not** by itself require rewriting the assessment. First determine whether changes since the accepted `review_ref` materially affect the organizational behavior represented by the current assessment.

Allowed per-harness outcomes are:

- **`no-upstream-change`** — the inspected upstream state has not advanced beyond the previously checked boundary;
- **`no-material-change`** — upstream advanced, but no material VSM-relevant change was found; the current assessment remains valid;
- **`reassessed-unchanged`** — relevant architecture or behavior changed enough to require a new-ref assessment, but the resulting categorical VSM states remain unchanged;
- **`reassessed-changed`** — the accepted new-ref reassessment changes one or more material assessment claims, autonomy states, or review-boundary facts;
- **`same-ref-correction`** — the upstream boundary is unchanged, but stronger evidence or a corrected interpretation changes the assessment;
- **`blocked`** — the harness could not be reviewed reliably during the round; the reason must be recorded. A blocked event does not advance the accepted review boundary or assessment freshness.

A round is complete only when every harness in its frozen scope has an explicit outcome. Completion does not imply that every assessment changed; a healthy round may consist mostly of `no-upstream-change` and `no-material-change` results.

The longitudinal invariant is: **every completed harness check states how far upstream the project was inspected, when that inspection occurred, and whether the inspection invalidated or changed the current assessment.** A `blocked` event records an attempted round outcome, not a completed freshness check.

### Assessment freshness fields

The standalone assessment remains the canonical current assessment, but after a harness first completes a successful reassessment check (any outcome except `blocked`) its front matter also records freshness metadata:

```yaml
last_checked_ref: <40-character upstream commit inspected most recently>
last_checked_at: YYYY-MM-DD
assessment_changed_at: YYYY-MM-DD
last_reassessment_round: R1
```

Their meanings are deliberately separate:

- `review_ref` / `reviewed_at` identify the currently accepted assessment boundary and when that accepted assessment was performed;
- `last_checked_ref` / `last_checked_at` identify the newest upstream state successfully inspected, even when no assessment rewrite was necessary;
- `assessment_changed_at` records the most recent date on which the canonical assessment materially changed, including accepted evidence, boundary, or VSM claims;
- `last_reassessment_round` links the current freshness state to the latest successful longitudinal round check.

Therefore `last_checked_ref` may legitimately be newer than `review_ref`. This means the assessment is pinned to an older accepted boundary but has been explicitly rechecked against later upstream development and found still valid.

For a new baseline assessment, `assessment_changed_at` should initially equal `reviewed_at`. Legacy baseline files may omit the new freshness fields until their first successful reassessment check; the first successful round check must populate the complete freshness set.

### Longitudinal history

Reassessment history is append-only and is stored separately from the canonical assessment in `data/reassessment-history.psv`. Updating an assessment must never erase earlier round results.

The history records, at minimum:

```text
round_id|harness_id|previous_review_ref|checked_ref|accepted_review_ref|checked_at|outcome|changed_functions|evidence
```

`accepted_review_ref` is the review boundary after that event. For `no-upstream-change`, `no-material-change`, and `blocked`, it remains equal to the previous accepted `review_ref`; for an accepted new-ref reassessment it advances to the new assessment boundary. A `blocked` event remains in history but does not replace the assessment's latest successful freshness metadata.

Round-level descriptions and scope are stored under `reassessments/`; see `reassessments/README.md` for the round template and tracking rules.

## Ranking semantics

The ranking reports:

- total agent-owned functions: count of `A` across S1, S2, S3, S3*, S4, S5;
- metasystem agent ownership: count of `A` across S2, S3, S3*, S4, S5;
- counts of `C`, `P`, and `?`;
- the categorical vector.

Rank by metasystem `A`, then total `A`. Harnesses with equal `(metasystem A, total A)` receive the same rank. Within the same rank, public presentation is newest-first by GitHub repository creation time. Freshness is presentation-only and never changes the rank key. Counts of `C`, `P`, and `?` are descriptive only: evidence completeness must not become an autonomy tie-breaker. No fractional weights are assigned. This is autonomy coverage, not product quality or viability.

The public `Year` column is the year of GitHub repository creation (`repository_created_at`). It is used because that field is available consistently for the whole cohort; it should not be interpreted as the year of conceptual invention or first stable release.

## Evidence and uncertainty

Positive `A/C/P` claims require primary evidence. `?` means evidence is insufficient. `—` is narrower: no material first-party path is supplied within the reviewed standard-distribution boundary; it is not a universal impossibility claim.

Pinned refs and review dates make longitudinal reassessment possible. Absence of documentation is not proof of absence.

## Historical migration

The original 1–82 ordered deep-review migration is complete. Legacy compact VSM text has been removed from `data/catalog.psv`; standalone assessments are the only repository-relative classification source of truth. Historical migration context remains available in Git history and the completed batch issues/PRs rather than in a second stale classification column.

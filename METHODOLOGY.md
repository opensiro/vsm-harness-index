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

`data/catalog.psv` is separate from all three: it is the discovery/order/provenance registry. It contains repository identity, chronology, source membership, and pinned review-boundary metadata, not VSM classifications.

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
- **new-ref reassessment** — a newer upstream commit materially changes the reviewed architecture or runtime behavior. The accepted reassessment updates the catalog `review_ref` and `reviewed_at` together with the standalone assessment.

A re-review request is evidence-led rather than grade-led. The proposed replacement state is advisory; the reviewer must independently re-establish the VSM function, decision right, ownership, standard-distribution closure, and counter-evidence.

For disputed positive metasystem claims, the re-review must actively try to falsify the claim. In particular:

- S2 requires a real interference/oscillation problem among operational units plus a regulating mechanism or actor;
- S3 requires current-whole authority, not merely task decomposition or result aggregation;
- S3* requires materially complementary and sufficiently independent access to operational reality plus a path for findings to affect control;
- S4 requires external-and-prospective distinctions, adaptation options, and coupling back to present capability;
- S5 requires legitimate ultimate authority or an operational parent-governed closure path, not static policy text.

If the strongest available primary evidence cannot support either a positive state or a defensible no-path conclusion, use `?` rather than forcing certainty.

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

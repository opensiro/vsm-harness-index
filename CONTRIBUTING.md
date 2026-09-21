# Contributing to VSM Harness Index

VSM Harness Index is the corpus/publication repository. It does not define VSM semantics or the standalone assessment Methodology.

Before semantic assessment work, use the current sources of truth:

- `opensiro/vsm-harness-profile` — VSM semantics;
- `opensiro/vsm-harness-skills` — assessment procedure, artifact format, classification, synthesis, and structural contract;
- this repository — task queueing, pinned refs, admission, provenance, reassessment bookkeeping, signatures, and generated views.

See [`INDEXING.md`](INDEXING.md) for the Index-local data/lifecycle contract.

## Review queued assessment work

Assessment queues are normally tracked in issues titled `[Assessment batch] ...`.

For the sequential workflow:

1. open a frozen assessment batch;
2. read its **Manual assessment board**;
3. take only the row marked `NEXT` unless the issue explicitly grants a different scope;
4. run `python scripts/assessment_preflight.py <issue-number>` to resolve the frozen task envelope;
5. re-read current Profile and Skills before semantic work;
6. assess only the frozen repository/ref;
7. write the assessment artifact required by the active Skills Methodology;
8. submit the row through normal PR review;
9. advance the board only after the current row reaches a terminal state.

Do not silently repin a queued assessment to a newer upstream commit.

## Suggest a harness

Open an issue titled `[Harness suggestion] ...` with the primary repository URL and a short explanation of why it belongs in the agent-harness corpus.

You do not need to propose a VSM classification or catalog position. Maintainers own catalog placement, provenance normalization, deduplication, and batching.

## Request an assessment re-review

Open an `[Assessment re-review]` issue when stronger primary evidence may change a canonical assessment or when a newer upstream revision materially changes the harness.

Include:

- harness/current assessment;
- affected function(s) or assessment claim;
- current accepted interpretation/vector;
- exact primary evidence path(s);
- pinned revision to inspect;
- reason for re-review;
- counter-evidence or uncertainty when known;
- optional proposed interpretation.

The proposed state is advisory. The actual reassessment must be performed under the applicable `vsm-harness-skills` Methodology.

### Same-ref correction

Use when the accepted upstream `review_ref` stays fixed and stronger evidence or semantic revalidation changes or confirms the assessment.

The catalog `review_ref` does not move merely because the interpretation was corrected.

### New-ref reassessment

Use when a newer upstream commit becomes the accepted assessment boundary because relevant behavior changed.

Update catalog pinning only after the newer boundary is accepted.

## Claim a re-review

A contributor may claim an open re-review issue and submit the change through a normal PR.

The PR should:

1. start from the currently accepted assessment and pinned boundary;
2. apply the current/frozen Skills Methodology rather than an Index-local reinterpretation;
3. update the standalone assessment only where evidence changes or revalidation requires it;
4. update catalog pinning only for an accepted new-ref reassessment;
5. update reassessment history/freshness when the task belongs to a longitudinal round;
6. re-run cohort synthesis where an accepted assessment change can affect later signatures;
7. regenerate derived views when their source data changed;
8. pass both Skills structural validation and Index repository validation.

Final review should independently verify the evidence rather than treating the issue author's preferred state as authoritative.

## Reassessment rounds

Periodic longitudinal review is organized into frozen rounds under `reassessments/`.

For each assigned harness:

1. start from the accepted assessment and `review_ref`;
2. inspect upstream through the round cutoff;
3. record the newest exact `checked_ref` successfully inspected;
4. determine whether the accepted assessment requires semantic revalidation or a new upstream boundary under the frozen Profile/Methodology pair;
5. record exactly one allowed Index-local round outcome in `data/reassessment-history.psv`;
6. update round progress;
7. update freshness metadata for successful checks;
8. update canonical assessment/catalog/signatures/generated views only where the accepted result requires it;
9. run repository validation.

A freshness check may advance `last_checked_ref` while leaving `review_ref` unchanged.

A blocked event records an attempted review but does not advance successful freshness or accepted assessment provenance.

## Maintainer / full assessment integration

For a new canonical assessment:

1. confirm the discovery/catalog record and frozen `review_ref`;
2. use `assess-vsm-harness` from the active Skills Methodology to produce `assessments/<harness_id>.md`;
3. validate the assessment using the version-pinned Skills structural checker;
4. resolve Index admission lifecycle;
5. apply the Skills synthesis procedure to accepted assessments and store the resulting signature;
6. regenerate materialized views;
7. run Index validation;
8. merge through normal review.

Do not hand-author a second assessment format, a second publication-state definition, or a ranking formula in this repository.

## Index-owned artifact rules

### Catalog

`data/catalog.psv` stores discovery/order/provenance only. It must not become a second assessment database.

### Reassessment history

`data/reassessment-history.psv` is append-only longitudinal bookkeeping. It does not replace the canonical standalone assessment.

### Signatures

`data/signatures.psv` stores cohort-relative synthesis output. Signatures must be supported by the standalone assessment and may change when the earlier cohort changes.

### Generated views

`TLDR.md`, `RANKINGS.md`, `FULL_A.md`, metrics, and analytics are derived/materialized outputs. Do not edit them as the primary fix for an assessment problem.

## Provenance and freshness

Generation provenance is immutable when recorded:

```yaml
generated_profile_version: ...
generated_assessment_procedure_version: ...
```

Current validation provenance may advance only after successful revalidation:

```yaml
profile_version: ...
assessment_procedure_version: ...
```

After successful longitudinal checking, the Index may also carry:

```yaml
last_checked_ref: <40-character commit>
last_checked_at: YYYY-MM-DD
assessment_changed_at: YYYY-MM-DD
last_reassessment_round: R1
```

Do not guess missing legacy generation provenance.

## Validation

For canonical Index work, run the checks relevant to the change. The complete local set is:

```bash
python scripts/validate_tldr.py
python scripts/render_tldr.py
python scripts/render_full_a.py --check
python scripts/render_metrics.py --check
python scripts/sync_metrics_readme.py --check
python scripts/check_index.py
python -m unittest discover -s tests -v
```

CI additionally checks out the active Methodology release and runs its authoritative structural assessment checker on active-version assessments.

The Index-local parser/renderer tests protect consumer compatibility and corpus invariants. They do not replace the semantic/format contract in `vsm-harness-skills`.

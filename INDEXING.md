# Index operations

`vsm-harness-index` is the evidence-backed corpus and publication layer for VSM Harness assessments. It does **not** define VSM semantics or the assessment/classification Methodology.

The source-of-truth chain is:

```text
vsm-harness-profile
    VSM organizational semantics
        ↓
vsm-harness-skills
    assessment format + classification + synthesis procedure
        ↓
vsm-harness-index
    corpus instances + provenance + generated views
```

Use the upstream owners directly:

- [VSM Harness Profile](https://github.com/opensiro/vsm-harness-profile/blob/main/PROFILE.md) — S1, S2, S3, S3*, S4, S5, recursion, autonomy, variety, closure, authority, and organizational semantics;
- [`assess-vsm-harness`](https://github.com/opensiro/vsm-harness-skills/tree/main/skills/assess-vsm-harness) — evidence collection, standalone assessment procedure, artifact format, and publication-state classification;
- [`vsm-harness-skills/SYNTHESIS.md`](https://github.com/opensiro/vsm-harness-skills/blob/main/SYNTHESIS.md) — cohort-relative signature synthesis and deterministic ranking projection.

This document owns only Index-local publication, intake, provenance, reassessment bookkeeping, and materialization rules.

## Artifact separation

The Index keeps the following artifacts separate.

### Canonical assessment

`assessments/<harness_id>.md` is a repository-relative, revision-relative instance produced under a recorded Profile/Methodology contract.

The **format and semantic validity of the assessment are owned by `vsm-harness-skills`**. The Index stores the accepted instance and its provenance.

Adding another harness must not change an existing standalone assessment merely because the cohort changed.

### Catalog

`data/catalog.psv` is discovery/order/provenance infrastructure. It stores repository identity, chronology, source membership, `review_ref`, and `pinned_at`.

It is not a second assessment database and must not carry VSM classifications.

### Signature

`data/signatures.psv` is cohort-relative. It materializes the signature produced by applying the active Methodology synthesis procedure to accepted standalone assessments in catalog order.

A signature may change when the earlier comparison cohort changes. It must not change an assessment state or introduce a repository claim absent from the canonical assessment.

### Generated views

`TLDR.md`, `RANKINGS.md`, `FULL_A.md`, metrics, and analytics are materialized projections. Their semantics come from the active Methodology; their exact checked-in output identity is the Index Git revision.

Index renderer code is a **consumer implementation** of the Methodology projection contract. It is not an independent semantic definition.

## Active contract

`data/active-contract.psv` records the Profile/Methodology pair expected for new Index work.

It is configuration/provenance infrastructure, not a semantic specification. Changing the active pair does not retroactively rewrite historical assessment provenance.

CI checks out the version-pinned `vsm-harness-skills` release and runs its assessment structural checker on assessments using the active Methodology.

## Continuous indexing lifecycle

New candidates follow:

```text
discover
→ deduplicate
→ queue
→ pin
→ assess
→ admit
→ synthesize
→ regenerate
→ validate
→ reassess
```

The responsibilities are deliberately split:

- discovery, queueing, pinning, admission, and publication state live in this repository;
- assessment meaning and artifact requirements come from Skills;
- VSM semantics come from Profile.

## Admission lifecycle

Assessment intake can temporarily use `status: proposed` as an Index-local workflow state. Proposed artifacts are review surfaces, not admitted corpus facts.

Canonical admission resolves the proposal to the status allowed by the active assessment contract and updates Index-owned registry/projection artifacts atomically as needed.

See [`docs/assessment-lifecycle.md`](docs/assessment-lifecycle.md) for the Index-local lifecycle.

Admission may be sparse relative to `catalog_position`. An unresolved earlier candidate does not block later candidates from becoming canonical.

## Ordered synthesis application

The semantic synthesis procedure is defined only in `vsm-harness-skills/SYNTHESIS.md`.

Index-local rules are operational:

1. preserve immutable `catalog_position` as discovery/comparison order;
2. apply the active synthesis procedure to accepted standalone assessments;
3. store the resulting cohort-relative signature in `data/signatures.psv`;
4. if an earlier assessment is admitted or corrected, revisit later signatures whose comparison basis may have changed;
5. never modify a standalone assessment solely to produce a different signature;
6. regenerate derived views after accepted source data changes.

Public display order may differ from synthesis order. Display ordering is presentation metadata and does not change assessment meaning or catalog ancestry.

## Re-review and reassessment routing

The assessment itself must always be re-evaluated under the applicable Skills Methodology. The Index owns the longitudinal bookkeeping around that review.

Two repository-boundary cases are recorded:

- **same-ref correction / semantic revalidation** — the accepted upstream `review_ref` stays fixed while stronger evidence or a newer Methodology changes or confirms the assessment;
- **new-ref reassessment** — a newer upstream commit becomes the accepted assessment boundary.

A newer upstream commit does not by itself force an assessment rewrite. First inspect whether it materially changes the evidence relevant to the current assessment under the applicable Methodology.

## Reassessment rounds

Longitudinal checks are grouped into dated rounds under `reassessments/`.

A round freezes:

- round identifier;
- open/cutoff dates;
- harness scope;
- Profile version;
- Methodology version.

Harnesses admitted after the cutoff enter a later round rather than extending the frozen scope.

Per-harness outcomes are stored in `data/reassessment-history.psv`. The currently supported outcome vocabulary is an Index-local workflow contract because it describes longitudinal bookkeeping, not VSM classification.

A completed successful check records how far upstream was inspected, when it was inspected, under which Profile/Methodology pair it was judged, and whether the canonical assessment changed.

A blocked check remains in history but does not advance accepted freshness or assessment provenance.

## Freshness and provenance

The canonical assessment carries the currently accepted boundary and latest successful freshness metadata. Reassessment history remains append-only.

Important distinctions:

- `review_ref` / `reviewed_at` — accepted assessment boundary;
- `profile_version` / `assessment_procedure_version` — contract under which the current assessment was successfully produced or revalidated;
- `generated_profile_version` / `generated_assessment_procedure_version` — immutable generation provenance when known;
- `last_checked_ref` / `last_checked_at` — newest successfully inspected upstream state;
- `assessment_changed_at` — most recent material canonical-assessment change;
- `last_reassessment_round` — latest successful longitudinal round.

`last_checked_ref` may be newer than `review_ref` when later upstream was inspected and found not to require a new accepted assessment boundary.

Do not guess missing legacy generation provenance.

## Longitudinal history

`data/reassessment-history.psv` is append-only. Updating a canonical assessment must not erase earlier review events.

The history connects each round event to its previous accepted boundary, inspected boundary, resulting accepted boundary, review contract, outcome, and evidence reference.

Round-level scope and progress live under `reassessments/`.

## Consumer implementation boundary

The Index contains parsers, validators, and renderers because it must materialize and protect a concrete corpus revision.

Those implementations may encode compatibility with currently supported Methodology releases, but they do not own the meaning of a publication state or the assessment body contract.

When a Methodology release changes those semantics, the order of work is:

```text
release Methodology in vsm-harness-skills
        ↓
update Index consumer compatibility if required
        ↓
activate the released contract for new work
        ↓
explicitly migrate/revalidate affected assessments
        ↓
regenerate Index projections
```

A consumer parser accepting or rejecting a token is therefore a compatibility gate, not a competing definition of the Methodology.

## Validation

Repository-level validation includes Index-owned invariants and the version-pinned Skills structural checker.

```bash
python scripts/validate_tldr.py
python scripts/render_tldr.py
python scripts/render_full_a.py --check
python scripts/render_metrics.py --check
python scripts/sync_metrics_readme.py --check
python scripts/check_index.py
python -m unittest discover -s tests -v
```

CI additionally checks the active `vsm-harness-skills` release and validates active-version assessment structure using its `scripts/check_assessment_contract.py`.

## Boundary summary

```text
Profile says what VSM means.
Skills says what a valid assessment and projection mean.
Index stores accepted assessment instances and materializes the corpus.
```

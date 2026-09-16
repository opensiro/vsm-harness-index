# Assessment lifecycle

Assessment files may exist in one of two lifecycle layers.

## Proposed assessment

```yaml
status: proposed
```

`proposed` is an intake/review state. It may exist before the harness receives a catalog row, or after discovery/pinning has placed the candidate in `data/catalog.psv`.

A proposed assessment is **not canonical**:

- it does not count as an admitted assessment;
- it does not participate in `data/signatures.psv`, `TLDR.md`, or `RANKINGS.md`;
- it does not participate in reassessment history;
- its VSM states remain reviewable evidence claims rather than admitted Index classifications.

A proposal may coexist temporarily with an older catalog record while deep review updates the project label, repository target, or pinned `review_ref`. Cross-artifact equality is therefore deferred to **admission**. Admission must reconcile the accepted proposal and catalog atomically rather than treating proposal metadata as already canonical.

## Canonical assessment

Admission resolves the file to one of the canonical statuses:

```yaml
status: included
```

or

```yaml
status: excluded-no-agentic-vsm
```

Canonical assessments must have a matching catalog row, and their accepted `project_name`, `repository`, and `review_ref` must match it. Included assessments participate in signatures and generated comparison views. Canonical assessments may enter longitudinal reassessment rounds.

## Generation provenance vs current semantic provenance

For assessments newly created by `assess-vsm-harness` procedure v0.2.1 or later, preserve the original generation pair:

```yaml
generated_profile_version: 0.2.0
generated_assessment_procedure_version: 0.2.1
```

These fields answer **which versions produced the artifact originally**. They are immutable after creation and must not be rewritten during admission, same-ref correction, or reassessment.

The separate current semantic pair:

```yaml
profile_version: 0.2.0
assessment_procedure_version: 0.2.1
```

answers **under which versions the current accepted classification was most recently successfully produced or revalidated**. These fields may advance through successful reassessment while the `generated_*` pair remains fixed.

Legacy assessments may omit generation provenance when their original versions were never recorded. Do not fabricate historical values. A later reassessment can establish current semantic provenance without inventing the artifact's origin.

Generation provenance is stored on the assessment artifact itself and is not duplicated into `data/reassessment-history.psv`: reassessment history records the versions used for each longitudinal event, while the immutable `generated_*` fields preserve origin once.

## Version-aware canonical assessments

Version-aware canonical assessments should record the current accepted semantic pair:

```yaml
profile_version: 0.2.0
assessment_procedure_version: 0.2.1
```

Legacy canonical assessments may omit those fields until they are successfully revalidated under an explicitly versioned procedure. Do not fabricate historical version metadata.

The lifecycle is therefore:

```text
discovery / pinning
        ↓
proposed assessment
        ↓ review / admission + catalog reconciliation
included | excluded-no-agentic-vsm
        ↓
canonical reassessment rounds
```

`catalog_position` is a stable discovery/order identifier, not a completion counter. Admission may be sparse: an earlier proposal can remain unresolved while later positions are already canonical. If that earlier proposal is later admitted, re-synthesize affected cohort-relative signatures rather than renumbering the catalog or rewriting repository-relative assessments.

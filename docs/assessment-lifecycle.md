# Assessment lifecycle

Assessment files may exist in one of two lifecycle layers.

## Proposed assessment

```yaml
status: proposed
```

`proposed` is an intake/review state. It may exist before the harness receives a catalog row, or after discovery/pinning has placed the candidate in `data/catalog.psv`.

A proposed assessment is **not canonical**:

- it does not count as an admitted/completed assessment at its `catalog_position`;
- it does not participate in `data/signatures.psv`, `TLDR.md`, or `RANKINGS.md`;
- it does not participate in reassessment history;
- its VSM states remain reviewable evidence claims rather than admitted Index classifications.

A proposal may coexist temporarily with an older catalog record while deep review updates the project label, repository target, or pinned `review_ref`. Cross-artifact equality is therefore deferred to **admission**. Admission must reconcile the accepted proposal and catalog atomically rather than treating proposal metadata as already canonical.

## Sparse admission and stable catalog order

`catalog_position` is a stable discovery/order identifier, not a completion counter. Canonical assessments therefore do **not** need to form a contiguous prefix of the catalog: an unresolved proposal may remain at an earlier position while later candidates are admitted.

Ordered synthesis still uses ascending `catalog_position` among the currently admitted assessments. If an earlier proposal is admitted after later positions already have signatures, re-synthesize that newly admitted harness and every later cohort-relative signature that could depend on it. Do not renumber the catalog and do not rewrite repository-relative assessments merely because the admitted comparison cohort changed.

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

Version-aware canonical assessments should record:

```yaml
profile_version: 0.2.0
assessment_procedure_version: 0.2.0
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

# Assessment lifecycle

Files in this directory may exist in one of two lifecycle layers.

## Proposed assessment

```yaml
status: proposed
```

`proposed` is an intake/review state. It may exist before the harness receives a catalog row, or after discovery/pinning has placed the candidate in `data/catalog.psv`.

A proposed assessment is **not canonical**:

- it does not count toward the contiguous completed catalog prefix;
- it does not participate in `data/signatures.psv`, `TLDR.md`, or `RANKINGS.md`;
- it does not participate in reassessment history;
- its VSM states remain reviewable evidence claims rather than admitted Index classifications.

If a matching catalog row already exists, repository identity and `review_ref` must agree with that row.

## Canonical assessment

Admission resolves the file to one of the canonical statuses:

```yaml
status: included
```

or

```yaml
status: excluded-no-agentic-vsm
```

Canonical assessments must have a matching catalog row. Included assessments participate in signatures and generated comparison views. Canonical assessments may enter longitudinal reassessment rounds.

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
        ↓ review / admission
included | excluded-no-agentic-vsm
        ↓
canonical reassessment rounds
```

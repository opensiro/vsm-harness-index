# Versioning and provenance

`vsm-harness-index` is the evidence-backed corpus and generated-view repository. It deliberately avoids creating a separate semantic version for every derived artifact.

The release/provenance model is:

```text
VSM Harness Profile version
        ↓
VSM Harness Methodology version
        ↓
vsm-harness-index @ exact Git revision
        ↓
TLDR.md / RANKINGS.md generated views
```

## Two semantic versions

### Profile

The Profile version identifies the normative VSM semantics used by the ecosystem.

### Methodology

The Methodology version identifies the procedural contract in `vsm-harness-skills` that turns repository evidence into assessments and corpus views. One Methodology release covers:

- assessment/evidence procedure;
- ownership-state notation and classification procedure;
- assessment provenance contract;
- cohort-relative signature synthesis;
- deterministic ranking projection;
- validation rules for those procedures.

Methodology `0.3.0` uses the publication symbols:

```text
A  A(P)  C  C(P)  P  —  ?
```

`A(P)` and `C(P)` are supported-mode notation for S3/S4/S5: the base `A` or `C` condition is established and a distinct first-party parent-governed mode for the same function is also operationally closed. Standalone `P` records a parent-governed S3/S4/S5 mode when no first-party `A` or `C` autonomous mode is established at the reviewed boundary.

Assessment front matter and reassessment history retain the compatibility field name `assessment_procedure_version`. Its value is the Methodology version as applied to that assessment/reassessment event. Likewise, `generated_assessment_procedure_version` is the immutable generation-time Methodology version for an assessment artifact.

Do not introduce independent semantic versions for synthesis or ranking while those procedures are released under the same Methodology boundary.

## Exact Index state

The exact Git revision of this repository identifies the complete corpus/output state, including:

- catalog and admission state;
- canonical and proposed assessments;
- assessment provenance and freshness;
- reassessment history;
- cohort-relative signatures;
- rendering/validation implementation;
- materialized `TLDR.md` and `RANKINGS.md`.

This is why the Index does not need an additional general `index_version`, `schema_version`, cohort fingerprint, `TLDR_VERSION`, or `RANKINGS_VERSION` today.

If a stable external Index schema/API is later consumed independently of the repository revision, that interface may justify a separate format version. Until then, Git is the immutable state identity.

## Active contract

`data/active-contract.psv` stores only the semantic pair expected for **new work**:

```text
profile_version|methodology_version
0.2.1|0.3.0
```

This file is compatibility/configuration infrastructure, not a second assessment database.

Changing the active pair does not retroactively rewrite historical assessment provenance or an already-open reassessment round. A round remains frozen on the Profile/Methodology pair declared when it opened.

Methodology `0.3.0` is a substantive classification change. Existing canonical assessments are not automatically rewritten to `A(P)`, `C(P)`, or S3/S4 `P`; they remain valid historical/current artifacts under their recorded Methodology until they are explicitly revalidated. A migration may be same-ref when the upstream repository boundary is unchanged, but the reviewer must re-establish the S3/S4/S5 function and every ownership mode from primary evidence.

Immutable `generated_profile_version` / `generated_assessment_procedure_version` values never change during that migration. Only the current `profile_version` / `assessment_procedure_version` advance after successful revalidation.

Frozen historical rounds remain frozen. In particular, R1 remains on Profile `0.2.0` / Methodology `0.2.1`; the active `0.2.1 / 0.3.0` contract must not silently rewrite that round.

## Generated views

`TLDR.md` and `RANKINGS.md` are generated/materialized views of an Index revision.

They have no independent semantic versions:

- TLDR depends on canonical assessments, cohort-relative signatures, and the Methodology synthesis rules;
- RANKINGS depends on canonical assessment states and the Methodology ranking projection;
- a particular checked-in result is identified by the Index Git revision containing it.

Under Methodology `0.3.0`, ranking parses composite states by base ownership:

```text
A(P) → A for agent-owned coverage
C(P) → C for constructor coverage
```

Parent-mode presence is descriptive and unweighted. It must never make `A(P)` rank above `A` or `C(P)` above `C`.

A Profile or Methodology change may make some source assessments or projections stale and can require reassessment, re-synthesis, re-ranking, or regeneration. The resulting state is then captured by a new Index revision rather than by inventing another version axis.

## Minimal reconstruction tuple

For ecosystem-level reproducibility, the useful tuple is:

```text
Profile version
+ Methodology version
+ Index Git revision
```

Per-assessment upstream revisions and generation/current provenance remain inside the assessment artifacts themselves.

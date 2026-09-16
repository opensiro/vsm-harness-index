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
- `A/C/P/—/?` classification procedure;
- assessment provenance contract;
- cohort-relative signature synthesis;
- deterministic ranking projection;
- validation rules for those procedures.

Assessment front matter and reassessment history retain the existing compatibility field name `assessment_procedure_version`. Its value is the Methodology version as applied to that assessment/reassessment event. Likewise, `generated_assessment_procedure_version` is the immutable generation-time Methodology version for an assessment artifact.

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
0.2.0|0.2.2
```

This file is compatibility/configuration infrastructure, not a second assessment database.

Changing the active pair does not retroactively rewrite historical assessment provenance or an already-open reassessment round. A round remains frozen on the Profile/Methodology pair declared when it opened.

For example, R1 remains on Profile `0.2.0` / Methodology `0.2.1` even after `0.2.2` becomes active, because `0.2.2` is a release-boundary clarification and R1 must not silently mix procedural releases.

## Generated views

`TLDR.md` and `RANKINGS.md` are generated/materialized views of an Index revision.

They have no independent semantic versions:

- TLDR depends on canonical assessments, cohort-relative signatures, and the Methodology synthesis rules;
- RANKINGS depends on canonical assessment states and the Methodology ranking projection;
- a particular checked-in result is identified by the Index Git revision containing it.

A Profile or Methodology change may make some source assessments or projections stale and can require reassessment, re-synthesis, re-ranking, or regeneration. The resulting state is then captured by a new Index revision rather than by inventing another version axis.

## Minimal reconstruction tuple

For ecosystem-level reproducibility, the useful tuple is:

```text
Profile version
+ Methodology version
+ Index Git revision
```

Per-assessment upstream revisions and generation/current provenance remain inside the assessment artifacts themselves.

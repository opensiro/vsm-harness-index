# Versioning and provenance

`vsm-harness-index` is the evidence-backed corpus and generated-view repository. It deliberately does not create another semantic version line for assessment meaning.

The ecosystem release/provenance chain is:

```text
VSM Harness Profile version
        ↓
VSM Harness Methodology version
        ↓
vsm-harness-index @ exact Git revision
        ↓
materialized Index views
```

## Semantic owners

### Profile

The VSM Harness Profile version identifies the normative organizational semantics used by the ecosystem.

### Methodology

The VSM Harness Methodology version in `vsm-harness-skills` identifies the procedure that turns repository evidence into standalone assessments and corpus projections.

The Methodology owns:

- assessment/evidence procedure;
- assessment artifact format;
- publication-state notation and classification procedure;
- assessment provenance requirements;
- cohort-relative synthesis;
- deterministic ranking projection;
- structural validation rules for those procedures.

This repository must not independently redefine any of those semantics. When the active Methodology changes, Index code may need a consumer-compatibility update before the new release can be activated here.

Assessment frontmatter retains the compatibility field name `assessment_procedure_version`; its value is the Methodology version applied to that assessment. `generated_assessment_procedure_version` records immutable generation-time Methodology provenance when known.

## Exact Index state

The exact Git revision of this repository identifies the concrete corpus/output state, including:

- catalog and admission state;
- canonical and proposed assessment instances;
- assessment provenance/freshness;
- reassessment history;
- cohort-relative signatures;
- consumer parser/renderer implementation;
- materialized generated views and analytics.

The Index therefore does not currently need a separate general `index_version`, `schema_version`, `TLDR_VERSION`, or `RANKINGS_VERSION`.

If a stable external Index API/schema is later consumed independently of the repository revision, that interface may justify a dedicated format version. Until then, Git revision is the immutable corpus/output identity.

## Active contract

`data/active-contract.psv` records the Profile/Methodology pair expected for new Index work.

It is compatibility/configuration metadata, not another semantic specification and not a second assessment database.

Changing the active pair does not retroactively rewrite:

- historical assessment generation provenance;
- an already-open reassessment round frozen on an earlier pair;
- accepted assessment vectors that have not been explicitly revalidated;
- prior reassessment-history events.

The active pair may advance only to released upstream contracts that the Index consumer implementation can materialize and validate.

## Historical assessment provenance

Each assessment distinguishes generation provenance from current accepted validation provenance.

Generation fields are immutable when present:

```yaml
generated_profile_version: ...
generated_assessment_procedure_version: ...
```

Current accepted contract fields may advance after explicit successful revalidation:

```yaml
profile_version: ...
assessment_procedure_version: ...
```

Legacy assessments whose original generation versions were never recorded must not be backfilled by guesswork.

A later Profile or Methodology release does not automatically rewrite an older assessment. The upstream release contract determines whether a semantic review or migration is required; the Index records the resulting explicit revalidation/reassessment event.

## Reassessment-round provenance

A reassessment round freezes its Profile/Methodology pair at opening time. Later activation of another pair does not mutate the frozen historical round.

Per-harness reassessment events record the contract actually used for that event in `data/reassessment-history.psv`.

Successful freshness checks may advance `last_checked_ref` and `last_checked_at` without advancing the accepted `review_ref` when later upstream changes do not require a new assessment boundary.

## Generated views

`TLDR.md`, `RANKINGS.md`, `FULL_A.md`, metrics, and analytics are materialized views of a particular Index revision.

They have no independent semantic version. Their meaning is reconstructed from:

1. the Profile/Methodology provenance recorded by the source assessments and active contract;
2. the applicable Skills synthesis/projection contract;
3. the exact Index Git revision containing the source corpus and rendering implementation.

A Profile or Methodology release may require assessment revalidation, re-synthesis, projection-code compatibility changes, or regeneration. Those changes are captured by a new Index revision rather than by inventing another semantic version axis.

## Consumer compatibility

The Index contains local parsing and rendering code because it must materialize a concrete corpus and detect incompatible data.

That code is a consumer of the released Methodology. It may explicitly support a finite set of released publication tokens or projection shapes, but such support is not the source of their meaning.

When Methodology changes require consumer work, use this order:

```text
release Profile/Methodology upstream
        ↓
update Index consumer compatibility
        ↓
activate the released pair for new work
        ↓
explicitly revalidate/migrate affected corpus artifacts
        ↓
regenerate materialized views
```

Do not infer a new assessment state or migration solely from what the current Index parser happens to accept.

## Minimal reconstruction tuple

For ecosystem-level reproducibility, use:

```text
Profile version
+ Methodology version
+ Index Git revision
```

Per-assessment upstream refs and generation/current validation provenance remain inside the assessment artifacts and reassessment history.

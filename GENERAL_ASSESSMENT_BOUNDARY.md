# General assessment boundary

`opensiro/vsm-harness-index` is the canonical corpus for the **general OpenSiro VSM Harness assessment**.

This repository stores accepted assessment instances, provenance, longitudinal history, and materialized general-corpus views. It does not define VSM semantics and it does not define the general assessment methodology.

## Canonical chain

```text
VSM Harness Profile
        ↓
canonical general assessment specification
opensiro/vsm-harness-skills/skills/assess-vsm-harness
        ↓
opensiro/vsm-harness-index
canonical general assessment corpus
```

Every canonical `Assessment` link published from this repository is therefore a link to a **general assessment artifact** unless an explicitly separate assessment system is named.

## General does not mean universal

The general Index is not the only possible assessment corpus that can use the VSM Harness Profile.

A domain-specific assessment may define different:

- operating purpose and system-in-focus;
- admission rules;
- evidence requirements;
- capability requirements;
- required or permitted ownership arrangements;
- publication contract.

Its results may live in a separate domain-specific index.

Such an index is a fresh assessment system, not:

```text
vsm-harness-index WHERE domain = X
```

and not a replacement for the canonical general assessment.

The same upstream harness may therefore have:

```text
general assessment
        +
domain-specific assessment(s)
```

with different conclusions when their declared purpose, boundary, evidence contract, or autonomy requirements differ.

## Link discipline

Links originating from the canonical Index must not ambiguously imply that a domain-specific conclusion is the canonical general assessment.

When another OpenSiro surface links to an artifact in this repository, it should treat that artifact as the **general assessment** unless a different assessment contract is explicitly named.

Future domain-specific indexes should use their own repository/corpus identity and provenance rather than publishing domain-specific conclusions into `assessments/` here.

## Deprecated coupling: Profile-driven reassessment authority

**Deprecated architectural assumption:** the general Index does not own a rule that a Profile release, by itself, determines the required reassessment or migration operation for this corpus.

Profile versions remain important semantic provenance and compatibility input. However, the applicable assessment specification owns the migration/revalidation decision for artifacts produced under that specification.

The durable direction is:

```text
Profile release
    ↓ semantic change / compatibility input
Skills assessment specification
    ↓ assessment-specific migration decision
Index
    ↓ bookkeeping + execution of the selected migration/revalidation
```

The Index may store and execute reassessment work after that decision, but it does not independently reinterpret Profile version changes into assessment semantics.

Existing historical reassessment rounds, `reassessments/`, and `data/reassessment-history.psv` remain valid provenance. They are **not** deprecated as historical records.

What is deprecated is treating Index-local Profile-version coupling as the architectural authority for future assessment migration.

## Profile provenance remains first-class

Every accepted assessment continues to record the exact Profile and assessment-specification versions under which it was produced or successfully revalidated.

Profile versioning is independently meaningful because implementations, derived profiles, assessment specifications, and other consumers may all need to pin or track changes to the organizational model.

The general Index consumes that versioned model; it does not own its lifecycle.

## Relationship to Awesome

`opensiro/awesome-vsm-harness` may curate links to both:

- this canonical general Index;
- future domain-specific indexes when they actually exist.

Awesome should label the assessment view clearly rather than collapsing all assessment systems into one undifferentiated `Assessment` concept.

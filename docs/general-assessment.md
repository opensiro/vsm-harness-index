# General VSM assessment scope

This document defines the scope boundary of the canonical general assessment corpus maintained in `opensiro/vsm-harness-index`.

It sits alongside [`assessment-lifecycle.md`](assessment-lifecycle.md): this document answers **what kind of assessment this Index stores**, while the lifecycle document answers **how an assessment moves through Index-local publication state**.

`opensiro/vsm-harness-index` is the canonical **general VSM assessment corpus** for the released `assess-vsm-harness` Methodology.

A link to `assessments/<harness_id>.md` in this repository means:

> **General VSM assessment under the recorded Profile + Methodology contract.**

It does not mean that the same system has one universal assessment for every deployment domain or operating purpose.

## General versus domain-specific assessment

Future domain-specific assessment systems may use the same VSM Profile while asking additional purpose-, evidence-, capability-, or autonomy-specific questions. Those systems may maintain separate indexes.

```text
general assessment
    → vsm-harness-index

domain-specific assessment
    → separate domain-specific index
```

A domain-specific index may reuse repository identity, pinned upstream revisions, public evidence, or the general assessment as an input. Its conclusions remain owned by its own domain contract and must not overwrite the general assessment stored here.

The same upstream system may therefore legitimately have:

- one general VSM assessment;
- zero or more domain-specific assessments;
- different conclusions where the declared purpose, system boundary, evidence requirements, or required ownership arrangements differ.

## Profile versioning and reassessment

Profile versions identify changes in the normative organizational model. They are useful to implementations, assessment specifications, derived profiles, and other consumers independently of this corpus.

Historical Profile release-impact metadata remains valid provenance for general Index releases and frozen reassessment rounds that already used it.

However, using Profile-owned `assessment_impact` or selector metadata as a **universal future reassessment policy** is deprecated.

The forward ownership rule is:

```text
Profile
    → versions normative model changes

Assessment specification / Methodology
    → decides how a Profile change affects its evidence and classification contract

Index
    → records and executes the resulting corpus migration / reassessment bookkeeping
```

This allows different assessment specifications to track the same Profile version while legitimately applying different reassessment rules.

## Link contract

Downstream curated views should label links into this repository as **General assessment** (or an unambiguous equivalent) when domain-specific assessment indexes may also exist.

This document defines scope only. VSM semantics remain owned by `opensiro/vsm-harness-profile`; assessment procedure remains owned by `opensiro/vsm-harness-skills`; accepted general assessment instances remain owned by this repository.

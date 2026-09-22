# System ↔ benchmark evidence registry

Status: **non-normative experiment**

Issue: #371

This directory links canonical systems already admitted to the VSM Harness Index with published benchmark observations that exercised the named harness/system identity.

It does not change canonical VSM assessments, autonomy states, rankings, or Profile semantics.

## Why this exists

The canonical assessment answers an organizational question:

```text
Which VSM function exists, and who owns its decisive closure?
```

A benchmark observation answers a different question:

```text
How did a particular system/harness + model + configuration behave on a particular task distribution?
```

Those two evidence channels should be connected without collapsing them into one score.

The initial registry therefore records only:

```text
canonical system
        ↕
published benchmark observation
```

Feature/mechanism attribution and mapping onto named S1 capability dimensions are deliberately deferred.

## Source of truth

`links.jsonl` is the only observation database in this experiment.

Do not manually duplicate its rows in Markdown tables. Derived views should be generated from it if/when they are added.

Each JSONL line is one published observation of one concrete configuration. A system may therefore have multiple rows for different benchmarks, models, dates, or configurations.

## Identity anchors

Every row records:

- `harness_id` — canonical Index identifier;
- `canonical_repository` — repository used by the Index assessment;
- `assessment_ref` — current canonical assessment revision used only as the Index-side identity anchor.

The benchmarked system revision does **not** need to equal `assessment_ref`. Missing revision information must remain explicit through `identity.revision_match`.

A benchmark observation never silently repins the canonical assessment.

## Observation unit

The interpretation unit is:

```text
(system/harness, model, benchmark, configuration, date)
```

not the harness in isolation.

A score must therefore not be read as a model-independent property of the system.

## Provenance

### `provenance.evidence_mode`

- `external-run` — a third party reports running the system/harness;
- `externally-checked-submission` — the benchmark authority directly ran or checked the submitted result;
- `system-maintained` — the system's own project maintains/publishes the result;
- `published-secondary` — a paper/report reproduces a result but is not the primary execution source.

These values describe where the evidence came from. They are not quality grades.

### `provenance.publisher_relation`

- `independent-third-party`
- `benchmark-project-related`
- `system-maintainer`
- `unclear`

This field prevents project relationships from being lost when results are later synthesized.

## Identity matching

### `identity.boundary_match`

- `exact` — the benchmark-side harness identity matches the canonical system boundary closely enough for a direct system-level link;
- `partial` — the benchmark exercised a first-party related runtime/scaffold, but the current canonical assessment boundary includes materially different/additional surfaces;
- `unclear` — the source does not expose enough information.

`exact` does **not** mean that the exact current repository commit was benchmarked. Commit/version matching is separate.

### `identity.revision_match`

- `exact`
- `version-known`
- `date-bounded`
- `unknown`

Do not reconstruct an exact revision from a publication date alone.

## Comparability

`comparability_group` identifies observations that may be candidates for later like-for-like analysis.

Membership in the same group is necessary but not automatically sufficient for a valid comparison. Model, effort, task version, harness configuration, repetitions, and other material differences must still be checked.

Scores from different benchmark families or variants must not be numerically compared merely because they are all percentages.

## Relationship to VSM capability depth

The intended later structure is:

```text
benchmark observations
        ↘
         per-function capability synthesis
        ↗
feature / mechanism evidence
```

The two channels answer different questions:

- benchmark evidence records observed outcomes;
- feature/mechanism evidence records what first-party/inherited mechanisms could have produced those outcomes and where capability ownership resides.

A later S1-specific pass may map benchmark metrics/traces onto dimensions such as task effectiveness, tool/environment fidelity, recovery, assurance, or efficiency. That mapping must remain explicit and evidence-backed.

## Interpretation rules

Do not use this registry to:

- change `A`, `C`, `P`, `—`, or `?` states;
- create a scalar or weighted S1 score;
- create an overall harness ranking;
- infer non-S1 functions from coding performance;
- attribute a model's capability to the harness without mechanism evidence;
- equate `system-maintained` evidence with independent execution;
- compare incompatible benchmark/task versions;
- fill unknown configuration or revision fields by inference.

A useful result can be simply:

> This canonical system has published external evidence on benchmark X, but the exact harness revision is unknown.

## Initial pilot

The first registry pass covers five canonical `S1=A` systems with different evidence shapes:

- Codex — third-party native-harness results plus a third-party scaffold comparison;
- Gemini CLI — third-party native-harness results;
- OpenHands — official/third-party benchmark results with a partial current-boundary match;
- SWE-agent — official ecosystem and independent third-party results;
- Aider — system-maintained benchmark evidence retained with explicit provenance.

This mix is intentional: the purpose of the pilot is to exercise provenance and identity matching before any feature-level interpretation.

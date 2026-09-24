# Public PolyBench matched-S4 preflight — paper-level controls

Status: experimental, non-normative.

Tracking issue: #538.

This is a follow-up to the completed #534 preflight. It does **not** rewrite that historical artifact.

## New evidence

The first-party Adaptive Auto-Harness paper closes several matching questions more strongly than the released code artifact alone.

For the auto-harness comparison, the paper states:

```text
solver: Claude Sonnet 4.6 unless specified
evolver: Claude Opus 4.6
solver temperature: 0
evolver temperature: 0
PolyBench batch size: 100
same batch loop: yes
same temporal-reveal gate: yes
same chronological task order: yes
```

It also states that all main runs use provider-hosted LLM APIs with native tool calling and that reported numbers are generated from corresponding `results.jsonl` files.

Therefore the candidate is no longer blocked by lack of evidence for a common paper-level solver/evolver policy or execution schedule.

## What still blocks canonical matching

The exact implementations behind the named comparison rows remain unbound.

The initial public release:

- excludes `results/` and `logs/`;
- does not contain implementation paths for GEPA, Meta-Harness or SkillOS in its public tree;
- exposes `gepa>=0.1.0` only as an unpinned optional dependency;
- does not expose immutable evaluated revisions for Meta-Harness, Continual Harness or SkillOS.

The later released algorithms package is explicit that the comparison methods

```text
gepa
meta_harness
skillos
continual_harness
mas_adaptive_skill
```

are **not shipped in the released version**.

Thus the paper establishes a strong matched **experiment membrane**, but the release does not establish a strong matched **native-system identity membrane**.

These are different questions:

```text
same tasks/models/schedule/metrics
        !=
exact native implementation identity
```

## Refined disposition

```text
public cross-method comparison: satisfied
common task stream/order: satisfied
common solver/evolver model policy: satisfied
common temperature/batch/temporal-reveal policy: satisfied
common result surface: satisfied
native baseline implementation/revision provenance: blocked
canonical S4 linkage: not reached
ordinary-S4 regulator freeze: not reached
execution authorized: no
S4 primary baseline: gap
```

## Why `results.jsonl` is not enough

The paper says published numbers are generated from corresponding `results.jsonl` files. The public release, however, git-ignores `results/` and does not publish those files or enough metadata to bind the named baseline rows to immutable upstream implementations.

A reported result can therefore be valid as a paper result while still being insufficient for Opensiro's narrower canonical attribution question.

## Recovery path

For any candidate baseline row, promotion requires primary evidence that recovers:

1. exact upstream repository/system identity;
2. immutable evaluated revision or exact package version;
3. the launch/configuration path used in the Adaptive Auto-Harness comparison;
4. evidence that the system's native or adapter-preserved S4 mechanism actually ran;
5. a frozen ordinary-S4 regulator boundary;
6. independent canonical Index assessment establishing S4 for that same system boundary.

The first candidate worth pursuing is GEPA because the public artifact at least declares a `gepa` package dependency. But `gepa>=0.1.0` is not an exact version binding and therefore does not by itself close the provenance gate.

## Relation to other S4 preflights

```text
A-Evolve × Exo / SkillsBench
  blocker: exact common model/provider route

Adaptive Auto-Harness / public PolyBench baselines (#534)
  blocker: native implementation/revision provenance

Adaptive Auto-Harness / paper-control refinement (#538)
  paper-level matching: stronger / satisfied
  blocker retained: native implementation/revision provenance
```

## Non-goals

This refinement does not:

- replace the #534 historical preflight;
- add or restate a ranking of the paper's methods;
- infer S4 from a method name or citation;
- treat the AdaptiveHarness mirror as independent from A-Evolve;
- claim paper rows were independently reproduced;
- authorize Opensiro-owned execution;
- change canonical assessments or generated rankings;
- promote `S4 primary baseline` from `gap`.

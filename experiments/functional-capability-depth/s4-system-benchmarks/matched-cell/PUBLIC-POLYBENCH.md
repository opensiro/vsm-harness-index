# Public PolyBench matched-S4 preflight

Status: experimental, non-normative.

Tracking issue: #534.

## Question

Can the public **Adaptive Auto-Harness** PolyBench comparison be ingested directly as the first matched canonical S4 cell, without Opensiro running its own benchmark?

The public paper and analysis artifact are unusually promising because several auto-harness methods are reported on one PolyBench stream and one result surface.

The candidate reported methods include:

```text
A-Evolve
GEPA
Meta-Harness
Continual Harness
SkillOS
Adaptive Auto-Harness
```

That is not enough by itself. A matched canonical capability cell must also establish **which exact implementation produced each row** and that the evaluated path is the system's own native or adapter-preserved S4 function.

## What is established

### One public task stream

The first-party plotting code explicitly describes one dot per method on the **same PolyBench stream**. It uses the same market index and summarizes each method directory as Return, Accuracy and Coverage.

### A common reported result surface

The plotted auto-harness rows therefore have a shared public outcome shape. This is materially stronger than comparing unrelated papers with unrelated metrics.

### AdaptiveHarness is not a second independent A-Evolve system

The `A-EVO-Lab/AdaptiveHarness` README explicitly says:

```text
This is a mirror.
```

and points to `A-EVO-Lab/a-evolve/tree/release/adaptive-auto-harness` as the canonical actively maintained code.

For Index/capability purposes, that mirror cannot be counted as an independent second S4 harness merely because it has a distinct GitHub repository ID.

## Blocking provenance gap

The released algorithms package states that the comparison-method baselines

```text
gepa
meta_harness
skillos
continual_harness
mas_adaptive_skill
```

are **not shipped in the released version**.

At the same time, the public PolyBench plotting code reads result directories such as:

```text
polybench_gepa_lite
polybench_mh_lite
polybench_continual_harness
polybench_skillos
```

This establishes that result rows existed for plotting. It does **not** establish, from the released artifact alone:

- the exact upstream repository and immutable revision behind each row;
- whether the row executed native upstream code or an experiment-local reimplementation;
- whether the native S4 path of that system was active;
- the exact model/provider/budget bindings for those unshipped baseline implementations;
- the ordinary-S4 frozen-regulator boundary for those rows.

The method name is not enough to infer any of those properties.

## Current disposition

```text
candidate: Adaptive Auto-Harness / PolyBench public comparison
public task stream: satisfied
common result surface: satisfied
native baseline implementation provenance: blocked
canonical S4 linkage: not reached
execution authorized: no
S4 primary baseline: gap
```

This is a **provenance blocker**, not a negative capability result.

## What would reopen the candidate

The public comparison can be reconsidered if primary evidence recovers, for at least two candidate rows:

1. exact repository identity;
2. immutable evaluated revision;
3. evidence that the native/adapter-preserved S4 path ran;
4. exact model/provider and material run configuration;
5. ordinary-S4 regulator/target boundary;
6. a canonical Index assessment establishing S4 at that system boundary.

If the original comparison used faithful but local reimplementations, those rows can remain useful **benchmark-defined/composed** evidence, but they cannot be promoted to matched canonical native evidence for the named upstream systems.

## Relation to the first matched-cell preflight

The existing A-Evolve × Exo / SkillsBench candidate is blocked for a different reason:

```text
A-Evolve × Exo
blocking gate: exact common model/provider route
```

This public PolyBench candidate is blocked earlier:

```text
Adaptive Auto-Harness public comparison
blocking gate: native implementation / immutable revision provenance
```

Keeping those failure modes separate prevents a generic `blocked` label from hiding what evidence is actually missing.

## Non-goals

This preflight does not:

- change canonical assessments;
- count the AdaptiveHarness mirror as a new independent system;
- infer S4 from a method name;
- rank the reported methods;
- restate the paper's ordering as an Opensiro conclusion;
- introduce a new capability score;
- authorize Opensiro-owned execution;
- change `S4 primary baseline = gap`.

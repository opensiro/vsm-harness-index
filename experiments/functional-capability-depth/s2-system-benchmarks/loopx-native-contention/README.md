# LoopX native-S2 contention study

Status: **preregistered; no results admitted**.  
Execution feasibility at the frozen revision: **not identifiable** (#606).

Tracking issue: #602  
Canonical harness: `loopx`  
Canonical assessment ref: `ade21106b4bc31a9bc4e61d2f5809b1b4d04d14f`  
Canonical S2 state at design: `A`

## Execution feasibility

The post-preregistration execution check in #606 stopped before any live/model
run. With exactly the two frozen implementation tasks, both write the same
`src/dispatch.py` surface. At the pinned LoopX revision the second lane is
blocked by native `write_scope_conflict`; because no child lane remains, the
adaptive v2 contract and native child topology are absent. Serial execution by
the same parent agent would fail this study's distinct-S1 admission gate.

This is an **identifiability result about this frozen experiment**, not a
negative S2 capability result. The canonical assessment remains `S2=A`, the
protocol remains `preregistered-no-results`, and `observations.json` remains
unchanged.

See `execution-feasibility.json` and `NOT_IDENTIFIABLE.md`. The companion
`verify_execution_feasibility.py` can reproduce the structural stop against an
exact local checkout of the pinned LoopX revision without invoking a model.

## Question

Can LoopX's own model-driven task-coordinator path attenuate an explicit inter-S1 overlapping-write disturbance and change subsequent worker behavior under materially matched conditions?

The study is intended to test this chain:

```text
distinct coding-worker S1s
        ↓
predeclared overlapping write surface
        ↓
LoopX model-driven task coordinator
chooses parallel / serial / repartition
        ↓
native task-lease / write-scope enforcement
        ↓
changed worker admission / execution / integration
```

A lease rejection by itself is not enough. The observation is eligible only if the treatment reaches the **agent-owned coordination decision** that supports canonical `S2=A`, and the decision or its returned conflict feedback changes later S1 behavior.

## Existing native substrate

The canonical LoopX revision already contains:

```text
examples/control_plane/task-lease-runtime-smoke.py
```

That smoke establishes useful first-party mechanism evidence. It creates registered agent identities, admits disjoint scopes, rejects an overlapping scope with `write_scope_conflict`, and exercises lease/CAS lifecycle fencing.

It is **not** a direct native capability observation for this study because the smoke scripts the owners and scopes directly. It does not ask the model-driven LoopX task coordinator to decide whether work should be parallel, serial, or repartitioned.

## Frozen disturbance fixture

The preregistered fixture contains two independently useful tasks:

- Task A adds request-id propagation.
- Task B adds retryability classification.

Both tasks are frozen before execution and both require modifying:

```text
fixture/src/dispatch.py
```

Each task explicitly excludes the other task's feature. This makes the overlap structural rather than a post-hoc choice made after observing which runs conflicted.

The acceptance tests are task-specific. They are expected to fail against the untouched fixture and are used to judge the corresponding worker result after execution.

## Treatment

`loopx-native-s2`

The treatment must use the standard LoopX multi-agent/task-coordinator path at the pinned LoopX revision. The model-driven coordinator must make the S2-specific decision: parallelize, serialize, or repartition the work and choose the relevant lane/write-scope relation.

First-party task-lease/write-scope enforcement then applies that decision unchanged. The run must retain coordinator decisions, worker prompts, lease/admission events, worker outputs, repository diffs and integration outcome.

## Control

`loopx-coordination-ablation`

The control must hold the LoopX revision, model/configuration, fixture, worker count, starting repository state and worker operational capabilities fixed while removing only the S2-specific coordinator decision/attenuation relation.

The control must not silently replace LoopX coordination with a benchmark-authored coordinator or pre-partition the conflicting surface. If a narrow ablation cannot be implemented without materially changing other organizational functions, the study is **not identifiable** and execution must stop rather than manufacture a comparison.

## Replication

The preregistration requires at least three primary replicate pairs per arm, with a fresh fixture checkout for every run. Treatment/control order alternates across pairs and the actual order is recorded.

Infrastructure failures may be excluded only when the run cannot reach the preregistered disturbance surface. Model mistakes, coordinator mistakes, task failures, lease rejections and merge/integration conflicts are outcomes, not exclusion reasons. Excluded runs remain in the raw ledger.

## Primary measurements

The primary record preserves raw S2-relevant outcomes:

- coordinator decision: parallel / serial / repartition;
- whether overlapping work was admitted concurrently;
- selected write scopes and lease/admission events;
- write-scope conflicts;
- stale or duplicate work;
- clean integration;
- acceptance of Task A and Task B;
- whether subsequent S1 behavior changed because of the coordination decision or conflict feedback.

Wall-clock time and model token/cost data are secondary context only. Whole-task quality, speed or cost cannot substitute for the disturbance-to-attenuation chain.

## Provenance

Every future run must fill `run-template.json` with recoverable system/model/config/task provenance, including exact LoopX revision, protocol/fixture revision, provider/model identity, reasoning configuration, prompts, worker count, environment, arm configuration and raw artifact locations.

## Admission gate

A future execution transaction may add a LoopX row to the S2 observation registry only when all of the following are true:

1. distinct S1 workers instantiate the frozen overlapping-write disturbance;
2. the treatment exercises LoopX's model-driven S2 decision path, not only deterministic lease checks;
3. the native decision or returned conflict feedback changes subsequent worker behavior;
4. system/model/config/task provenance is recoverable;
5. raw artifacts are public and immutable;
6. the result is linked to the existing canonical LoopX boundary without deriving any new `A/C/P` state from performance.

## Files

- `protocol.json` — machine-readable preregistration and source of truth.
- `run-template.json` — required future run/provenance record shape.
- `fixture/` — frozen disturbance workload and task acceptance tests.
- `execution-feasibility.json` — machine-readable #606 stop result; not an observation.
- `NOT_IDENTIFIABLE.md` — human-readable explanation of the execution stop.
- `verify_execution_feasibility.py` — static CI check plus optional pinned-LoopX dynamic proof.
- `validate.py` — fail-closed preregistration/feasibility validator.

## Boundary

This package does not change the canonical LoopX assessment, the S2 evidence counts, `observations.json`, the primary baseline, Profile semantics, Skills methodology, TLDR, rankings or Full-A projections.

A later execution may proceed only if a new-ref feasibility check removes the identified structural blocker while preserving the frozen protocol. A redesigned fixture belongs in a new preregistration rather than rewriting this one.

# Execution feasibility: not identifiable

Tracking issue: #606  
Preregistration merge: `93a18ad13a50c4bb273064838715c2c6ea5e8253`  
Canonical LoopX revision: `ade21106b4bc31a9bc4e61d2f5809b1b4d04d14f`

No live/model run was attempted.

## Why execution stops

The preregistered fixture contains exactly two implementation tasks, and both
write `src/dispatch.py`.

At the frozen LoopX revision, adaptive child admission uses the first admitted
write lane as the primary lane and rejects a later overlapping lane with
`write_scope_conflict`. An adaptive `task_orchestration_contract_v2` is emitted
only when at least one child lane survives that admission. With this exact
frozen pair, the second task conflicts with the primary task, no child survives,
and the adaptive contract is therefore absent.

The first-party Turn driver creates native child host operations and
`subagent_execution_topology` only from eligible lanes in that adaptive v2
contract. The built-in Codex host likewise exposes typed child execution
receipts only when the topology exists. Thus the frozen pair cannot exercise a
LoopX-native treatment with two distinct child S1 workers through the canonical
Turn path.

Running the two tasks as two sequential turns of the same parent agent does not
repair the experiment: the preregistered admission gate requires distinct S1
workers. Adding a third non-overlapping Todo, changing the declared write
scopes, repartitioning the tasks after seeing this failure, or launching workers
through a benchmark-authored subprocess coordinator would change the frozen
experiment rather than identify it.

## What this does not mean

This is not a negative S2 capability result.

The execution-identifiability stop does not change the canonical LoopX assessment
(`S2=A`). The assessment is evidence about the first-party organizational
function at the reviewed boundary; this experiment asks a narrower empirical
question under one frozen two-task disturbance fixture.

`protocol.json` remains `preregistered-no-results`, `results` remains `null`, and
`observations.json` is not modified.

## Mechanical verification

CI-safe static verification:

```bash
python experiments/functional-capability-depth/s2-system-benchmarks/loopx-native-contention/verify_execution_feasibility.py
```

Optional dynamic verification against a local exact pinned LoopX checkout:

```bash
python experiments/functional-capability-depth/s2-system-benchmarks/loopx-native-contention/verify_execution_feasibility.py \
  --loopx-checkout /path/to/loopx
```

The dynamic mode refuses any LoopX HEAD other than
`ade21106b4bc31a9bc4e61d2f5809b1b4d04d14f`, imports that checkout's own
admission and Codex-host code, and proves:

1. the exact two-task overlapping fixture produces no adaptive contract;
2. adding a diagnostic third non-overlapping lane makes the conflict observable
   as `write_scope_conflict` while the independent lane is admitted;
3. without adaptive topology the canonical built-in Codex host has no typed
   child-receipt field and no LoopX `spawn_agent` instruction.

The diagnostic third lane exists only inside the verifier to expose the hidden
block reason. It is never added to the preregistered fixture or executed as a
study arm.

## Reopening

This frozen experiment may be reconsidered only if a newer LoopX revision
supplies a first-party observable model-owned path that can arbitrate the exact
two-task overlapping-write case while still executing two distinct S1 workers.
That would be a new-ref execution feasibility check. A redesigned fixture must
instead be a new preregistered experiment; it must not rewrite this one.

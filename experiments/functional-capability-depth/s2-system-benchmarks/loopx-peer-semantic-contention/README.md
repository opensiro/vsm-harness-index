# LoopX registered-peer semantic-contention study

Status: **retired historical preregistration; no results admitted; no live execution planned**.

Tracking issues: #609, #612, #616, #617  
Canonical harness: `loopx`  
Canonical assessment ref: `ade21106b4bc31a9bc4e61d2f5809b1b4d04d14f`  
Canonical S2 state at design: `A`  
Compatibility target: `adapter-preserved`

## Lifecycle

This directory remains under `experiments/` as a record of a controlled-comparison design and its identifiability/adapter-preservation work.

The capability-depth operating model is now explicitly public-evidence-only: Opensiro does not run or reproduce benchmark experiments on assessed harnesses to create capability evidence. Issue #616 was therefore closed `not_planned` before any live model execution.

Nothing in this package is an admitted S2 observation. The current LoopX capability state remains:

```text
canonical assessment: S2=A
canonical direct capability observation: absent
action: keep the capability gap open until suitable public upstream/third-party evidence exists
```

See [`../../PUBLIC-EVIDENCE.md`](../../PUBLIC-EVIDENCE.md) and [`EXECUTION_STATUS.md`](EXECUTION_STATUS.md).

The frozen `protocol.json` is intentionally preserved unchanged as a historical preregistration artifact.

## Historical research question

The preregistered question was:

> Can LoopX's own model-driven registered-peer task coordinator attenuate stale semantic interference between two distinct coding-worker S1s by changing their execution order, such that the later worker operates against updated integrated state?

The preregistered chain was:

```text
worker A + worker B
        ↓
disjoint write scopes
        ↓
shared producer/consumer semantic contract
        ↓
parallel stale-state interference
        ↓
LoopX task_scoped_peer coordinator decision
        ↓
transport-only adapter executes that schedule
        ↓
later worker starts from changed state
        ↓
changed implementation / composed outcome
```

Generic parallelism would not have been enough. Admission would have required the LoopX-owned coordination decision or its returned ordering feedback to change subsequent S1 behavior.

## Why this successor design existed

The earlier `loopx-native-contention/` preregistration was frozen around two tasks that both wrote `src/dispatch.py`. Its execution-feasibility transaction found that the exact pair could not produce the required two-worker native child topology at the pinned LoopX revision.

This successor changed the disturbance class before execution: the two tasks had disjoint write scopes but interacted through a producer/consumer contract. The design goal was to keep both S1 workers executable while preserving a real interaction-generated semantic disturbance.

Neither design was run live for capability-depth evidence.

## Frozen fixture

Baseline producer:

```python
make_response(429) == {"status": 429}
```

Task A migrates the producer contract to:

```python
make_response(429) == {"code": 429}
```

Task B implements retryability for 429/503 against the **current producer contract visible in its starting tree**.

The scopes are frozen and disjoint:

```text
Task A:
  src/envelope.py
  tests/test_envelope.py

Task B:
  src/retry.py
  tests/test_retry.py
```

This was intended to create a STALE-style composition hazard. A Task-B worker starting from the baseline could implement against `status`; a Task-B worker starting after A integration would instead see `code`.

## Organizational shape

The design used three registered LoopX identities:

- `codex-coordinator` — temporary S2 task coordinator only;
- `codex-worker-a` — Task A S1;
- `codex-worker-b` — Task B S1.

Only the two coding workers counted toward `functional_worker_count=2`.

## Adapter-preserved boundary

The pinned registered-peer path projected a `task_scoped_peer` contract but expected a host capable of activating/resuming durable peer runtimes. The experiment therefore designed a narrow host adapter.

The intended adapter role was transport/execution only: start the requested governed Turn, create worktrees, execute the coordinator's validated schedule literally, normalize integration order, run tests, and capture artifacts. It was forbidden to choose the schedule, reinterpret task semantics, repair code, synthesize dependencies/messages, or mutate observations.

These rules remain useful as historical methodology notes, not as an active execution plan.

## Historical treatment design

Treatment would have configured `peer_task_coordinator=codex-coordinator` and reported `peer_agent_activation` on the coordinator Turn.

The required native contract was:

```text
schema_version = task_orchestration_contract_v1
mode           = task_scoped_peer
```

with both worker lanes visible.

The coordinator would have returned exactly one scheduling classification:

```text
parallel
a_then_b
b_then_a
```

The adapter would then have executed that token without semantic reinterpretation.

## Historical control design

Control would have preserved the same LoopX revision, worker identities, worker model/configuration, fixture, worker count, worktree isolation, integration normalization, and tests while removing only the LoopX S2 relation:

- no peer task coordinator;
- no coordinator Turn;
- no `peer_agent_activation` capability;
- no task-orchestration contract.

The same transport adapter would have launched A and B concurrently from the same frozen baseline.

## Integration normalization

The design fixed final composed evaluation as Task A then Task B so that merge-order choice could not become a hidden benchmark coordinator.

## Historical primary measurements

The preregistration proposed raw fields rather than a scalar score:

- treatment native peer contract present;
- control peer contract absent;
- coordinator scheduling classification;
- both distinct worker S1 executions observed;
- worker start-base commits;
- concurrent-live overlap in control;
- isolated Task A/B acceptance;
- composed acceptance;
- the payload key implemented by worker B (`status`, `code`, or `other`);
- whether B started after A integration;
- whether B's implementation changed between matched arms;
- whether coordination changed subsequent S1 behavior.

No such live measurements were produced.

## Historical replication design

The frozen protocol specified at least three treatment/control replicate pairs with matched worker model/configuration and alternating arm order.

This replication plan is **retired for functional-capability-depth**. It is not a TODO and must not be resumed to fill the S2 gap.

## Identifiability work

The execution-harness transaction used model-free fake/stub artifacts to check that:

1. Task A/B write scopes were disjoint;
2. both registered workers had ordinary governed Turn surfaces without a coordinator;
3. treatment could project `task_scoped_peer` with both worker lanes;
4. control could project no task-orchestration contract;
5. the same worker Turn surfaces existed in both arms;
6. treatment scheduling could be represented as literal execution of a model-authored classification;
7. the adapter need not make an S2-specific decision.

Those checks are methodological artifacts only. Passing them is not a capability result.

## Files

- `protocol.json` — frozen historical preregistration; intentionally unchanged after retirement.
- `run-template.json` — historical proposed run/provenance schema.
- `fixture/` — frozen semantic-interference workload.
- `adapter.py`, `run_local.py`, `execution-plan.json`, `fake-artifacts/` — historical execution-harness implementation artifacts.
- `EXECUTION_STATUS.md` — current lifecycle disposition.
- `validate.py` and repository tests — fail-closed structural checks.

## Boundary

This package does not add a direct observation, change LoopX's canonical assessment, modify `observations.json`, produce a scalar S2 score, or change any TLDR/ranking/Full-A projection.

The active next step for S2 is **public upstream / third-party evidence discovery**, not harness execution by Opensiro.

# LoopX registered-peer semantic-contention study

Status: **preregistered; no results admitted**.

Tracking issue: #609  
Canonical harness: `loopx`  
Canonical assessment ref: `ade21106b4bc31a9bc4e61d2f5809b1b4d04d14f`  
Canonical S2 state at design: `A`  
Compatibility target: `adapter-preserved`

## Question

Can LoopX's own model-driven registered-peer task coordinator attenuate stale semantic interference between two distinct coding-worker S1s by changing their execution order, such that the later worker operates against updated integrated state?

The preregistered chain is:

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

Generic parallelism is not enough. Admission requires the LoopX-owned coordination decision or its returned ordering feedback to change subsequent S1 behavior.

## Why this is a new experiment

The earlier `loopx-native-contention/` preregistration was frozen around two tasks that both wrote `src/dispatch.py`. Its execution-feasibility transaction correctly found that the exact pair could not produce the required two-worker native child topology at the pinned LoopX revision. That experiment remains historical evidence and is not rewritten here.

This successor changes the disturbance class before execution: the two tasks have disjoint write scopes but interact through a producer/consumer contract. The goal is to let both S1 workers remain executable while preserving a real interaction-generated semantic disturbance.

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

This creates a STALE-style composition hazard. A Task-B worker that starts from the baseline can correctly implement against `status` and pass its isolated test. If Task A is later composed, that consumer can become stale. A Task-B worker that starts after A is integrated instead sees `code` and can change its implementation accordingly.

## Organizational shape

The experiment uses three registered LoopX identities:

- `codex-coordinator` — temporary S2 task coordinator only;
- `codex-worker-a` — Task A S1;
- `codex-worker-b` — Task B S1.

Only the two coding workers count toward `functional_worker_count=2`.

Each worker is executed through the governed LoopX Codex Turn surface at the pinned upstream revision. The coordinator is not allowed to edit fixture code.

## Adapter-preserved boundary

LoopX's pinned registered-peer path projects a `task_scoped_peer` contract but expects a host that can actually activate/resume durable peer runtimes. The experiment therefore supplies a narrow host adapter.

The adapter is **transport/execution only**. It may start the requested LoopX Turn, create worktrees, execute the coordinator's validated schedule literally, normalize integration order, run tests and capture artifacts. It may not choose the schedule, reinterpret task semantics, repair code, synthesize dependencies/messages or mutate observations.

If the adapter must make an S2-specific choice, the run is invalid. This is the key adapter-preservation boundary.

## Treatment

Treatment configures `peer_task_coordinator=codex-coordinator` and reports `peer_agent_activation` on the coordinator Turn.

The native contract must be:

```text
schema_version = task_orchestration_contract_v1
mode           = task_scoped_peer
```

and both worker lanes must be visible.

The coordinator is instructed to return exactly one scheduling classification:

```text
parallel
a_then_b
b_then_a
```

The adapter executes that token without semantic reinterpretation.

- `parallel` — both workers start from the same frozen baseline.
- `a_then_b` — A runs and integrates first; B starts from the A-integrated tree.
- `b_then_a` — B runs and integrates first; A starts from the B-integrated tree.

A wrong coordinator decision is an outcome, not an exclusion.

## Control

Control preserves the same LoopX revision, worker identities, worker model/configuration, fixture, worker count, worktree isolation, integration normalization and tests while removing only the LoopX S2 relation:

- no peer task coordinator;
- no coordinator Turn;
- no `peer_agent_activation` capability;
- no task-orchestration contract.

The same transport adapter launches A and B concurrently from the same frozen baseline. This is a fixed disturbance generator, not an adaptive coordinator.

If a task-orchestration contract appears in control, the run is protocol-invalid.

## Integration normalization

Final composed evaluation always normalizes integration as Task A then Task B. This prevents merge-order choice from becoming a hidden benchmark coordinator.

Every run records each worker's starting base commit and patch. The normalized composition must therefore be independently reconstructable.

## Primary measurements

The primary record preserves raw fields rather than a scalar score:

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

Wall-clock time and model token/cost data are secondary only.

## Replication

At least three treatment/control replicate pairs are required. Each arm starts from a fresh fixture repository. Worker model/configuration is held constant within a pair, arm order alternates across pairs, and all exclusions remain in the raw ledger.

Worker mistakes, coordinator mistakes, bad scheduling choices and composed integration failures are outcomes. Only infrastructure failures before the disturbance surface may be excluded.

## Pre-execution identifiability gate

A later execution-harness transaction must prove mechanically, with fake/stub host artifacts only, that:

1. Task A/B write scopes are disjoint;
2. both registered workers can receive ordinary governed Turns without a coordinator;
3. treatment projects `task_scoped_peer` with both worker lanes;
4. control projects no task-orchestration contract;
5. the same two worker Turn surfaces exist in both arms;
6. treatment scheduling is a literal execution of the model-authored classification;
7. the adapter makes no S2-specific decision.

Failure of any gate means `not-identifiable`. The frozen fixture must not be redesigned in place.

## Files

- `protocol.json` — machine-readable preregistration and source of truth.
- `run-template.json` — future run/provenance record.
- `fixture/` — frozen semantic-interference workload.
- `validate.py` — fail-closed preregistration validator.

## Boundary

This package does not run a model, add a direct observation, change LoopX's canonical assessment, modify `observations.json`, produce a scalar S2 score, or change any TLDR/ranking/Full-A projection.

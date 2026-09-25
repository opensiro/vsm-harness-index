# Control and adapter-preservation boundary

The control arm removes the LoopX registered-peer S2 relation while preserving the two functional worker Turn surfaces.

## Treatment

Treatment configures `codex-coordinator` as the peer task coordinator and supplies `peer_agent_activation` on its governed Turn. Before that Turn is eligible, the native LoopX quota projection must expose:

```text
task_orchestration_contract_v1
task_scoped_peer
eligible_peer_lanes = [codex-worker-a, codex-worker-b]
```

The coordinator model writes the schedule only through the typed `classification` field. The adapter accepts exactly `parallel`, `a_then_b`, or `b_then_a` and maps that token to the frozen launch topology without reading fixture source.

## Control

Control keeps the same two registered worker identities, same governed Codex Turn command builder, same model/config, same frozen tasks, same worktree isolation, and same post-run A-then-B composition check.

It removes:

- peer task coordinator configuration;
- coordinator Turn execution;
- `peer_agent_activation`;
- any task-orchestration contract.

The adapter then launches A and B concurrently from one frozen baseline. That fixed launch is the preregistered disturbance generator. It is not an adaptive scheduling choice.

## Why the adapter is not S2

`adapter.py` contains only:

1. exact-token validation;
2. a fixed token-to-stage lookup;
3. the shared worker Turn argv builder;
4. the treatment-only coordinator Turn argv builder.

It must not read task source or acceptance tests, infer which task should precede another, retry with a different schedule, repair worker output, or invent a dependency. CI scans the adapter source for the frozen task source paths and semantic payload-key literals and rejects them.

Post-run metric extraction may inspect worker patches to classify what happened. Measurement after the decision is not allowed to feed back into scheduling.

## Invalidation

A run or harness is invalid if any of the following occurs:

- Task A/B declared write scopes overlap;
- treatment does not expose both worker lanes in native `task_scoped_peer`;
- control exposes a task-orchestration contract;
- treatment and control use different worker Turn builders;
- an invalid/free-form coordinator schedule token is repaired or guessed;
- adapter code inspects task semantics to choose a schedule;
- a failed schedule is replaced by another schedule in the same replicate;
- live execution occurs in CI;
- canonical observations or assessment state are mutated.

Failure of a pre-execution gate yields `not-identifiable`. It does not authorize redesigning the frozen preregistration in place.

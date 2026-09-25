# Control and adapter-preservation boundary

Lifecycle: **historical design only — no live execution planned for functional-capability-depth**.

This file preserves the control/treatment boundary that was designed before #617 clarified the public-evidence-only operating model. It is retained to document identifiability and adapter-preservation reasoning. It is not an active benchmark plan and must not be used to create capability evidence.

The historical control arm removed the LoopX registered-peer S2 relation while preserving the two functional worker Turn surfaces.

## Historical treatment

Treatment configured `codex-coordinator` as the peer task coordinator and supplied `peer_agent_activation` on its governed Turn. Before that Turn was eligible, the native LoopX quota projection had to expose:

```text
task_orchestration_contract_v1
task_scoped_peer
eligible_peer_lanes = [codex-worker-a, codex-worker-b]
```

The coordinator model would write the schedule only through the typed `classification` field. The adapter accepted exactly `parallel`, `a_then_b`, or `b_then_a` and mapped that token to the frozen launch topology without reading fixture source.

## Historical control

Control kept the same two registered worker identities, same governed Codex Turn command builder, same model/config, same frozen tasks, same worktree isolation, and same post-run A-then-B composition check.

It removed:

- peer task coordinator configuration;
- coordinator Turn execution;
- `peer_agent_activation`;
- any task-orchestration contract.

The adapter would then launch A and B concurrently from one frozen baseline. That fixed launch was the preregistered disturbance generator, not an adaptive scheduling choice.

## Why the adapter was not S2

`adapter.py` was constrained to:

1. exact-token validation;
2. a fixed token-to-stage lookup;
3. the shared worker Turn argv builder;
4. the treatment-only coordinator Turn argv builder.

It was forbidden to read task source or acceptance tests, infer which task should precede another, retry with a different schedule, repair worker output, or invent a dependency. CI scans the adapter source for the frozen task source paths and semantic payload-key literals and rejects them.

Post-run metric extraction was designed to inspect worker patches only after the decision. Measurement after the decision was not allowed to feed back into scheduling.

## Historical invalidation rules

A proposed run/harness would have been invalid if any of the following occurred:

- Task A/B declared write scopes overlap;
- treatment does not expose both worker lanes in native `task_scoped_peer`;
- control exposes a task-orchestration contract;
- treatment and control use different worker Turn builders;
- an invalid/free-form coordinator schedule token is repaired or guessed;
- adapter code inspects task semantics to choose a schedule;
- a failed schedule is replaced by another schedule in the same replicate;
- live execution occurs in CI;
- canonical observations or assessment state are mutated.

Failure of a pre-execution gate yielded `not-identifiable`; it did not authorize redesigning the frozen preregistration in place.

Under #617, the stronger lifecycle boundary now applies: **the design is not executed live at all for capability-depth**. S2 evidence must come from already-public upstream or third-party results.

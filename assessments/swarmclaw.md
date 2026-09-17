---
harness_id: swarmclaw
project_name: SwarmClaw
repository: https://github.com/swarmclawai/swarmclaw
review_ref: ed38ba5329c20e48c03b4a4028f4a76a1a75e2d1
reviewed_at: 2026-09-17
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
assessment_changed_at: 2026-09-17
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# SwarmClaw

## Review boundary
Pinned first-party SwarmClaw runtime including autonomous participants, structured protocol execution, task assignment, dependency/order constraints, branches, bounded loops, parallel/subflow/swarm/A2A primitives, verification stages, schedules and persistent manual waits.

Reviewed revision: `ed38ba5329c20e48c03b4a4028f4a76a1a75e2d1`. Contract: Profile `0.2.1`, Methodology `0.3.1`. The pin matched upstream `main` when rechecked on 2026-09-17.

## Primary evidence
- [`README.md`](https://github.com/swarmclawai/swarmclaw/blob/ed38ba5329c20e48c03b4a4028f4a76a1a75e2d1/README.md) — autonomous agents, swarms, delegation, schedules and runtime controls.
- Pinned first-party structured-protocol implementation and tests reviewed for dependency/order gates, phase/branch execution, verification and durable manual waits.

## S1 — Operations
`A`. Agent participants independently execute assigned model/tool work and adapt their local trajectories. Confidence: high.

## S2 — Coordination
`C`. Structured protocols can impose dependency/order constraints across multiple participating S1s so incompatible or premature work is not released until the required predecessor relation is satisfied. That is a concrete constructor-owned coordination path beyond message routing or delegation. The runtime supplies the mechanism; the application supplies the protocol. Confidence: medium-high.

## S3 — Inside-and-now control
`—`. Assignment, phase transitions, branches and bounded loops are authored protocol execution. The reviewed standard distribution does not establish a distinct whole-system current regulator with authority over shared organizational resources, commitments and priorities. The historical `C` relied on workflow-control semantics. Confidence: high.

## S3* — Complementary audit
`—`. Verification/collect/compare/decide stages inspect artifacts/results carried through the normal protocol path. No first-party materially complementary access path to operational reality was established, so verification is not promoted to S3*. Confidence: high.

## S4 — Outside-and-then intelligence
`—`. No first-party outside-and-then organizational adaptation loop was established. Confidence: high.

## S5 — Policy and identity
`—`. Persistent manual wait preserves a human intervention point, but waiting for an operator during protocol execution is not by itself a function-specific ultimate-policy/identity closure. The historical `P` therefore does not survive. Confidence: high.

## Recursion, variety, and escalation
Subflows, swarm/A2A and parallel execution amplify operational variety; dependency gates, bounded loops, branches and waits attenuate it. Nested execution remains task/protocol composition unless a child system is separately shown viable at its own recursion level.

## Admission conclusion
Canonical vector: `A C — — — —`.

Same-ref correction of historical `A C C C — P`: constructor-owned dependency/order coordination remains S2; workflow control, routine verification and manual operational waits no longer count as S3, S3* or S5.
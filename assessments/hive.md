---
harness_id: hive
project_name: Hive
repository: https://github.com/aden-hive/hive
review_ref: 0c387492067e8b7d3e1c803009169f202f30ed77
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: —
autonomy_s5: ?
---

# Hive

## Review boundary
OpenHive at the pinned revision as the colony runtime: persistent Queen plus dynamically spawned worker clones, shared ledger/plan, recovery and human Sentinel.

## Repository architecture
Hive describes “one loop controlling many loops.” The Queen pilots work, fans out worker clones, and converges them through a shared tracker ledger, persistent task plan, event bus and reminder hub.

## Primary evidence
- `README.md`: Queen/worker colony architecture, shared tracker ledger and persistent plan, fan-out/converge loop, recovery/cost/HITL.
- `docs/key_concepts/coordination.md`: defines the tracker as the colony's shared source-of-truth ledger; workers upsert results, the Queen queries/validates progress, the event bus returns worker reports, and reminders keep the Queen aware of in-flight workers to avoid double-dispatch.

## Operational model
Queen and workers perform S1 work. Unlike pure parent→child delegation, workers operate concurrently against a shared task ledger/plan and the agent-owned colony loop uses fresh shared state and reports to converge work and determine further fan-out/completion.

## S1 — Operations
`A`: Queen/workers autonomously perform outcome-producing business-process work. Confidence: high.

## S2 — Coordination
`A`: the standard colony supplies agent-owned coordination through its shared ledger/plan, worker-report event path and Queen-driven convergence, providing concrete task-ownership and fleet-awareness mechanisms rather than simple one-shot delegation. Confidence: high.

## S3 — Inside-and-now control
`?`: the Queen is a persistent lead, but reviewed evidence does not separate routing/convergence from stronger whole-system resource/accountability authority sufficiently for S3.

## S3* — Complementary audit
`?`: audit trails/observability and human Sentinel do not establish an autonomous sufficiently independent audit agent.

## S4 — Outside-and-then intelligence
`—`: reflexion, memory and learned skills improve operation over time, but learning ≠ a distinct external/prospective intelligence function coupled to S3.

## S5 — Policy and identity
`?`: persona/HITL/cost controls do not establish agent-owned ultimate policy.

## Recursion, variety, escalation
Worker clones have task autonomy but no demonstrated own metasystem; colony nesting is not automatically recursion.
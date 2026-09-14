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
Hive describes “one loop controlling many loops.” The Queen pilots a unit of work, systematizes it, fans out worker clones, and converges them through a shared tracker ledger and persistent task plan. The runtime supplies crash recovery, cost enforcement, observability and out-of-band HITL.

## Primary evidence
- `README.md`: Queen/worker colony architecture; shared tracker ledger and persistent plan; runtime fan-out/converge loop; recovery/cost/HITL; adaptive reflexion/memory/skills.

## Operational model
Queen and workers perform S1 work. Unlike pure parent→child delegation, workers operate concurrently against a shared task ledger/plan and the agent-owned colony loop uses that shared state to converge work and determine further fan-out/completion.

## S1 — Operations
`A`: Queen/workers autonomously perform outcome-producing business-process work. Confidence: high.

## S2 — Coordination
`A`: the standard colony supplies agent-owned coordination through the persistent shared ledger/plan and Queen-driven convergence of concurrent worker loops, providing a concrete mutual-adjustment/task-ownership path rather than simple one-shot delegation. Confidence: medium-high.

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
---
harness_id: hive
project_name: Hive
repository: https://github.com/aden-hive/hive
review_ref: 0c387492067e8b7d3e1c803009169f202f30ed77
reviewed_at: 2026-09-15
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Hive

## Review boundary
OpenHive at the pinned revision as the colony runtime: persistent Queen plus dynamically spawned worker clones, shared ledger/plan, recovery and human Sentinel.

## Repository architecture
Hive describes “one loop controlling many loops.” The Queen pilots work, fans out worker clones, and converges them through a shared tracker ledger, persistent task plan, event bus and reminder hub.

## Primary evidence
- `README.md`: Queen/worker colony architecture, shared tracker ledger and persistent plan, fan-out/converge loop, recovery/cost/HITL.
- `docs/key_concepts/coordination.md`: the tracker is the colony's shared source-of-truth ledger; workers upsert results, the Queen queries/validates progress, the event bus returns worker reports, and reminders keep the Queen aware of in-flight workers to avoid double-dispatch.
- `docs/key_concepts/queen.md`: the persistent Queen owns the plan and tracker, assigns work, validates results, fans out workers, handles escalation and remains the colony-level decision surface through execution.

## Operational model
Queen and workers perform S1 work. Workers operate concurrently against shared colony state; the Queen uses that live state to regulate task ownership, convergence and exception handling for the whole colony rather than merely dispatching one-shot children.

## S1 — Operations
`A`: Queen/workers autonomously perform outcome-producing business-process work. Confidence: high.

## S2 — Coordination
`A`: the standard colony supplies agent-owned coordination through its shared ledger/plan, worker-report event path and Queen-driven convergence, providing concrete task-ownership and fleet-awareness mechanisms rather than simple one-shot delegation. Confidence: high.

## S3 — Inside-and-now control
`A`: the persistent Queen has a colony-wide current view through the plan/tracker and explicit authority to assign/fan out work, inspect and validate worker progress/results, converge execution and escalate exceptions. This is ongoing whole-colony current regulation rather than a component merely named manager. Confidence: high.

## S3* — Complementary audit
`—`: Queen-side validation uses the ordinary lead/control path and the human Sentinel is an escalation mechanism; the reviewed standard distribution does not establish a distinct sufficiently independent autonomous complementary-audit path.

## S4 — Outside-and-then intelligence
`—`: reflexion, memory and learned skills improve operation over time, but learning ≠ a distinct external/prospective intelligence function coupled to S3.

## S5 — Policy and identity
`—`: Queen personas, behavior triggers, HITL and cost controls shape operation, but legitimate ultimate task/policy authority remains with the user/configuration rather than an agent-owned S5 closure.

## Recursion, variety, escalation
Worker clones have task autonomy but no demonstrated own metasystem; colony nesting is not automatically recursion.
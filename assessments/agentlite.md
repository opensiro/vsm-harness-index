---
harness_id: agentlite
project_name: AgentLite
repository: https://github.com/SalesforceAIResearch/AgentLite
review_ref: b173239a652eea560e57c6fe46b0c0af7c4f3578
reviewed_at: 2026-09-15
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
last_checked_ref: b173239a652eea560e57c6fe46b0c0af7c4f3578
last_checked_at: 2026-09-17
assessment_changed_at: 2026-09-15
last_reassessment_round: R2
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# AgentLite

## Review boundary
AgentLite at the pinned revision as a research library for individual and manager-orchestrated agents.

## Repository architecture
AgentLite provides task-oriented tool-using workers plus a `ManagerAgent`. The manager exposes its configured team to the model, chooses one worker for the next delegated task and synchronously forwards that worker's result back into the manager loop.

## Primary evidence
- `agentlite/agents/ManagerAgent.py`: stores the configured labor-agent team, renders worker descriptions into the manager prompt, parses the chosen worker/action, creates a delegated task package and calls the selected labor agent before returning its observation.
- The reviewed code contains manager/worker delegation and fallback patterns but no separate peer-coordination or audit subsystem.

## Operational model
Worker agents are S1. The manager is an operational dispatcher/integrator over those workers; selecting a worker and consuming its answer is not sufficient to establish a metasystemic decision right.

## S1 — Operations
`A`: workers run model-driven action loops over delegated tasks. Confidence: high.

## S2 — Coordination
`—`: manager selection, delegation and fallback do not implement anti-oscillation/shared-resource regulation among independently interacting S1 units.

## S3 — Inside-and-now control
`—`: the manager lacks evidenced whole-system resource, priority and accountability authority with a closed superior feedback loop; the class name alone is insufficient.

## S3* — Complementary audit
`—`: no distinct first-party reviewer/evaluator independently checks operational claims against evidence and feeds corrective findings back into the running organization.

## S4 — Outside-and-then intelligence
`—`: no first-party prospective environment/adaptation function is established at this boundary.

## S5 — Policy and identity
`—`: goals, roles, team membership and ultimate policy are application supplied.

## Recursion, variety, escalation
Manager/worker hierarchy is delegation rather than recursive viable-system closure.
---
harness_id: crewai
project_name: CrewAI
repository: https://github.com/crewAIInc/crewAI
review_ref: 894898f84c4ac0a89f24bf7bee6c381eb0e67f51
reviewed_at: 2026-09-15
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
last_checked_ref: 7a01af27912c2b142d8bac70d1894343f8b91bd1
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

# CrewAI

## Review boundary
CrewAI OSS at the pinned revision. CrewAI's commercial control-plane capabilities are outside this assessment unless present in the open-source runtime itself.

## Repository architecture
CrewAI provides role-based autonomous agents in Crews plus authored Flows. The default crew process is sequential; an optional hierarchical process creates or accepts a manager agent whose primary first-party authority is delegation to worker agents.

## Primary evidence
- `lib/crewai/src/crewai/crew.py`: `process` defaults to `Process.sequential`; `_run_hierarchical_process()` explicitly creates a manager and then executes the authored task list. `_create_manager_agent()` gives the manager delegation tools over the configured agents. Planning, RPM limits, callbacks, memory and checkpoints are separately parent-configured runtime facilities.
- `lib/crewai/src/crewai/tasks/hallucination_guardrail.py`: the open-source `HallucinationGuardrail` is explicitly a placeholder/no-op; absent an injected hook it warns that premium hallucination detection was skipped and returns the task output as valid.
- First-party hierarchical-process documentation marks the manager process as an explicit opt-in rather than the default execution mode.

## Operational model
Role agents are S1. Sequential and hierarchical processes arrange task execution; the hierarchical manager selects/delegates work through agent tools, but manager naming and a chain of command do not themselves establish Beer-style S2 or S3.

## S1 — Operations
`A`: role agents autonomously execute bounded tasks with tools and context. Confidence: high.

## S2 — Coordination
`—`: delegation, sequential task execution and optional hierarchical assignment do not evidence an autonomous anti-oscillation/shared-resource coordination decision right among independently interacting S1 units.

## S3 — Inside-and-now control
`—`: the optional manager delegates configured tasks, while rate limits, planning, callbacks and checkpoints remain application/runtime controls. No reviewed OSS path gives the manager a whole-system current regulator's authority over priorities, resources and commitments with closed feedback.

## S3* — Complementary audit
`—`: task guardrails/evaluators do not establish an independent standard runtime audit channel, and the named OSS hallucination guardrail is explicitly a no-op by default.

## S4 — Outside-and-then intelligence
`—`: Crew planning and knowledge/research facilities serve current task execution; no distinct prospective external-intelligence loop feeding future organizational adaptation is established.

## S5 — Policy and identity
`—`: roles, goals, process choice, guardrails, security settings and ultimate task policy remain developer/parent supplied.

## Recursion, variety, escalation
Crews can contain multiple autonomous workers and a delegated manager, but that hierarchy is not sufficient evidence of recursive viable-system closure.
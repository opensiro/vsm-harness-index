---
harness_id: crewai
project_name: CrewAI
repository: https://github.com/crewAIInc/crewAI
review_ref: 894898f84c4ac0a89f24bf7bee6c381eb0e67f51
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: ?
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# CrewAI

## Review boundary
CrewAI OSS at the pinned revision. The commercial Crew Control Plane is outside the assessed system except as an explicit boundary marker.

## Repository architecture
CrewAI provides role-based autonomous agents in Crews plus event-driven Flows. Crews support autonomous decision-making, delegation and collaboration; Flows provide authored execution/state control.

## Primary evidence
- `README.md`: Crews, role-based agents, dynamic task delegation/collaboration, event-driven Flows and explicit commercial-control-plane boundary.

## Operational model
Role agents are S1. Crews provide collaboration primitives, but delegation/collaboration language alone does not prove a concrete anti-oscillation decision right.

## S1 — Operations
`A`: role agents autonomously execute bounded tasks with tools/context. Confidence: high.

## S2 — Coordination
`?`: autonomous collaboration is first-party, but reviewed evidence does not isolate mutual-adjustment/conflict-regulation semantics from delegation and workflow routing.

## S3 — Inside-and-now control
`?`: manager/control-plane concepts do not establish agent-owned whole-system current regulation in OSS.

## S3* — Complementary audit
`?`: observability/review is not sufficiently independent audit by itself.

## S4 — Outside-and-then intelligence
`?`: no verified S4↔S3 prospective adaptation loop.

## S5 — Policy and identity
`?`: roles/goals/guardrails are developer-supplied.

## Recursion, variety, escalation
Crews can contain many autonomous roles, but team nesting is not sufficient evidence of recursive viability.
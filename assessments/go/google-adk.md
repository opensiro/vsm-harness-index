---
harness_id: google-adk
project_name: Google ADK
repository: https://github.com/google/adk-python
review_ref: 460715b6c62c8e9ab00931c502381ee0364e39b6
reviewed_at: 2026-09-15
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
last_checked_ref: 7ae1c9b026c84bf8a65921003f71b0f30c8e3166
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

# Google ADK

## Review boundary
Deep review of the pinned ADK workflow-agent implementation, with sequential/parallel/loop composition tested against VSM functional criteria rather than mapped from orchestration vocabulary.

## Repository architecture
Google ADK provides autonomous agents plus workflow agents that compose child agents in sequential, parallel, and iterative execution structures. `ParallelAgent` executes sub-agents concurrently and merges their events into the parent invocation context. This is execution topology and task decomposition; the reviewed primitive does not regulate interference among autonomous operational units.

## Primary evidence
- `src/google/adk/agents/parallel_agent.py`: starts configured sub-agents concurrently, isolates invocation branches, collects their events, and completes after the branches finish.
- Workflow-agent composition determines execution order/concurrency but does not expose an autonomous organizational regulator over shared S1 constraints.

## Operational model
An ADK agent performs model/tool work; workflow agents arrange child execution and aggregate outputs according to application-defined structure.

## S1 — Operations
`A`: agents can autonomously select tools/actions and iterate from session/task feedback inside configured bounds. Confidence: high.

## S2 — Coordination
`—`: sequential/parallel/loop workflow structure and fan-out/fan-in are not sufficient evidence of interference regulation, anti-oscillation, or mutual constraint management among autonomous S1 units. The shallow `S2=C` interpretation is removed.

## S3 — Inside-and-now control
`—`: workflow parents control execution topology, not whole-system current resources, priorities, capacity and commitments across multiple S1 units.

## S3* — Complementary audit
`—`: no distinct complementary audit channel with separate access/authority was established in the reviewed boundary.

## S4 — Outside-and-then intelligence
`—`: workflow iteration and task planning concern present execution rather than prospective environment intelligence that changes organizational capability/strategy.

## S5 — Policy and identity
`—`: instructions, tools, workflow topology and policies are application/developer supplied rather than owned by an autonomous ultimate policy function.

## Recursion, variety, escalation
Workflow agents provide recursive composition and substantial operational variety, but the metasystem remains application-supplied.
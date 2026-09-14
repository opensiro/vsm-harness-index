---
harness_id: superagentx
project_name: SuperAgentX
repository: https://github.com/superagentxai/superagentx
review_ref: 28f2759f20d2dba9fa184ca4fe6b50943388cfbc
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# SuperAgentX

## Review boundary
SuperAgentX at the pinned revision as an agent/workflow framework with built-in human-approval governance and persistent audit data.

## Repository architecture
Agents understand goals, plan, call tools, run sequential/parallel workflows, retry/reflect/recover, and can pause sensitive actions for an explicit human approval handled by a governance agent. State, decisions, approvals, outputs and audit logs are persisted.

## Primary evidence
- `README.md`: autonomous multi-step agents; sequential/parallel workflows; Human Approval Governance Agent; persistent decisions/approval/audit logs.

## Operational model
Task agents are S1. Workflow parallelism is execution topology, while the governance path returns sensitive decisions to a human/parent.

## S1 — Operations
`A`: agents autonomously plan/use tools/retry within bounded workflows. Confidence: high.

## S2 — Coordination
`—`: sequential/parallel workflow execution does not establish an agent-owned anti-oscillation relation among S1s.

## S3 — Inside-and-now control
`?`: governance/runtime controls do not prove autonomous S3 resource/accountability authority.

## S3* — Complementary audit
`?`: audit logs persist evidence, but logging is not a sufficiently independent audit channel.

## S4 — Outside-and-then intelligence
`?`: retry/reflection/recovery are current-run adaptation, not S4.

## S5 — Policy and identity
`?`: human approval constrains sensitive operations, but action approval alone is not enough to establish identity/ultimate-policy closure.

## Recursion, variety, escalation
Governance attenuates action variety through a parent; parallel agents are not automatically recursive viable units.
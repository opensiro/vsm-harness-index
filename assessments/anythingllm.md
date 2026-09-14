---
harness_id: anythingllm
project_name: AnythingLLM
repository: https://github.com/Mintplex-Labs/anything-llm
review_ref: 3a85d3e75490f09453de7e8c440b9463f4a82019
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: ?
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# AnythingLLM

## Review boundary
AnythingLLM at the pinned revision, focusing on built-in workspace agents and no-code Agent Flows. Multi-user permissioning is infrastructure, not agent-owned policy by default.

## Repository architecture
AnythingLLM ships built-in/custom agents, web/document/tool access, memory, scheduled tasks, intelligent skill selection and a no-code Agent Flow builder. Server/frontend/collector services support the agent runtime.

## Primary evidence
- `README.md`: built-in agents, tools/web access, memories, scheduled tasks, intelligent skill selection, custom agents and no-code Agent Flows.

## Operational model
Workspace agents are S1. Agent Flow composition may connect agentic work, but the reviewed evidence does not establish the specific interference-dampening relationship required for S2.

## S1 — Operations
`A`: workspace agents autonomously select skills/tools toward user tasks. Confidence: high.

## S2 — Coordination
`?`: first-party agent-flow primitives exist, but workflow composition alone is insufficient to decide S2.

## S3 — Inside-and-now control
`?`: multi-user/admin/runtime controls are not verified agent-owned whole-system regulation.

## S3* — Complementary audit
`?`: no sufficiently independent audit role/path verified.

## S4 — Outside-and-then intelligence
`?`: schedules, web access and memories extend operation but do not prove prospective adaptation.

## S5 — Policy and identity
`?`: permissioning/custom-agent configuration is parent/platform-owned.

## Recursion, variety, escalation
Tool/memory/model routing increases S1 variety. Agent-flow nesting is not automatically recursive viability.
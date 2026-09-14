---
harness_id: agno
project_name: Agno
repository: https://github.com/agno-agi/agno
review_ref: 44219f8532e2fe6ce936850455f4b9a2567e4194
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: ?
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# Agno

## Review boundary
Agno at the pinned revision, including its SDK, AgentOS runtime, and first-party agent/team abstractions. UI, storage, RBAC, scheduling, tracing, and deployment are supporting infrastructure unless an agent owns the corresponding organizational decision right.

## Repository architecture
Agno describes a framework/runtime for agent platforms with agents, tools, memory, knowledge, context providers, approvals, observability, scheduling, and durable platform services. First-party Team abstractions include leader/member agents and a coordinate mode; examples describe leaders delegating and synthesizing member work.

## Primary evidence
- `README.md`: agent platform/runtime, tools, memory, context, approval, observability, scheduling.
- `libs/agno/agno/team/mode.py`: Team mode controls how a team leader coordinates member agents.
- `cookbook/00_quickstart/multi_agent_team.py`: leader/member structure and delegation/synthesis pattern.
Evidence is interpreted at the pinned review boundary; later code-search hits are used only to locate corresponding first-party concepts.

## Operational model
Agents are S1 units when they perform model-driven work with tools. Team leaders and workflow machinery can route/delegate work, but delegation and synthesis alone are not sufficient evidence of Beer-style S2.

## S1 — Operations
`A`: ready agent runs own bounded model/tool decisions. Confidence: high.

## S2 — Coordination
`?`: first-party teams explicitly coordinate agents, but reviewed evidence does not yet distinguish interference-dampening/mutual adjustment from leader-mediated task decomposition strongly enough for `A` or `C`.

## S3 — Inside-and-now control
`?`: AgentOS management, RBAC, run history, and scheduling are platform control, not verified agent-owned whole-system regulation.

## S3* — Complementary audit
`?`: traces/audit logs are evidence infrastructure, not an independent audit function by themselves.

## S4 — Outside-and-then intelligence
`?`: context providers and learning-loop language do not establish the required external-and-prospective S4↔S3 adaptation loop.

## S5 — Policy and identity
`?`: security/policy configuration and approvals do not establish agent-owned ultimate policy.

## Recursion, variety, escalation
Nested teams are technically supported, but nesting is not counted as recursive viability without local identity, operational closure, and a metasystem at the nested level.
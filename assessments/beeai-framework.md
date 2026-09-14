---
harness_id: beeai-framework
project_name: BeeAI Framework
repository: https://github.com/i-am-bee/beeai-framework
review_ref: 6a8b28f54073790f9a8135320a0e9ed1d4cef602
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# BeeAI Framework

## Review boundary
BeeAI Framework at the pinned revision across Python/TypeScript agent and workflow primitives.

## Repository architecture
BeeAI supplies autonomous agents, tools, memory, RAG, persistence, workflows and handoff tools. The standard multi-agent example uses a main agent that consults specialized agents through `HandoffTool` and integrates their responses.

## Primary evidence
- `README.md`: autonomous agents/multi-agent workflows; workflow orchestration; concrete `HandoffTool` main-agent→specialists example.

## Operational model
Specialist agents are S1. The documented main-agent handoff is task delegation/consultation, not mutual adjustment among peer S1 units.

## S1 — Operations
`A`: agents independently reason/use tools toward outcomes. Confidence: high.

## S2 — Coordination
`—`: first-party handoff/workflow mechanisms shown here decompose/route work rather than establish anti-oscillation among autonomous operations.

## S3 — Inside-and-now control
`?`: main-agent control does not prove whole-system resource/accountability regulation.

## S3* — Complementary audit
`?`: observability/trajectory middleware is not independent audit.

## S4 — Outside-and-then intelligence
`?`: adapt wording and environment tools do not establish a future-oriented adaptation loop.

## S5 — Policy and identity
`?`: RequirementAgent rules are configured constraints, not runtime ultimate-policy closure.

## Recursion, variety, escalation
Handoff hierarchies/workflows are compositional, not automatically recursive viable systems.
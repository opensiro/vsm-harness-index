---
harness_id: flowise
project_name: Flowise
repository: https://github.com/FlowiseAI/Flowise
review_ref: 9291856d1ea4a4ceea9f8fef8ce14f4f6c81e8eb
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: ?
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# Flowise

## Review boundary
Flowise at the pinned revision, focusing on first-party Agentflow/agent execution rather than the UI as an organization.

## Repository architecture
Flowise is a visual agent builder with server, UI and component packages. Agentflows combine model-driven agents with tools and authored graph structure; deployment/runtime services execute those flows.

## Primary evidence
- `README.md`: “Build AI Agents, Visually”, Agentflow, server/UI/components architecture and deployable agent workflows.

## Operational model
An executing agent node is S1. Visual edges, nodes and authored flow topology support/sequencing work but are not automatically an autonomous S2 function.

## S1 — Operations
`A`: agent nodes own bounded model/tool choices and produce flow outcomes. Confidence: high.

## S2 — Coordination
`?`: Agentflow can compose multiple agentic elements, but reviewed primary evidence does not establish anti-oscillation/mutual adjustment among autonomous S1 units strongly enough for `A` or `C`.

## S3 — Inside-and-now control
`?`: runtime/server control is not verified agent-owned whole-system regulation.

## S3* — Complementary audit
`?`: no sufficiently independent audit channel verified.

## S4 — Outside-and-then intelligence
`?`: connected tools/data do not by themselves establish prospective environmental adaptation.

## S5 — Policy and identity
`?`: authored instructions/configuration do not establish runtime ultimate-policy closure.

## Recursion, variety, escalation
Agentflow composition increases operational variety; graph nesting is not treated as VSM recursion without local viable-system closure.
---
harness_id: dify
project_name: Dify
repository: https://github.com/langgenius/dify
review_ref: 43ac0fce5c87815a2a6c71e109ca12aa2d467710
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# Dify

## Review boundary
Dify Community Edition at the pinned revision, focusing on first-party ReAct/function-calling agents and workflow runtime. External observability vendors are outside the system-in-focus.

## Repository architecture
Dify combines visual AI workflows, RAG, model management, agent capabilities and LLMOps. Agents can use 50+ built-in/custom tools; visual workflows provide authored branching and execution structure.

## Primary evidence
- `README.md`: workflow canvas, ReAct/function-calling agents, built-in tools, RAG, LLMOps and APIs.

## Operational model
A Dify agent is S1. The visual workflow is supporting deterministic structure; no separate agent-owned multi-S1 coordination function is established by the reviewed evidence.

## S1 — Operations
`A`: first-party agents select tools/actions to produce application outcomes. Confidence: high.

## S2 — Coordination
`—`: authored workflow branches and services sequence operation but do not establish agentic anti-oscillation among autonomous S1 units.

## S3 — Inside-and-now control
`?`: logs/operations and workflow controls do not prove an autonomous whole-system regulator.

## S3* — Complementary audit
`?`: LLMOps monitoring/annotations are evidence infrastructure, not an independent audit function by themselves.

## S4 — Outside-and-then intelligence
`?`: production-data improvement is developer/operator-led in the reviewed evidence, not verified agent-owned S4.

## S5 — Policy and identity
`?`: prompts/configuration remain parent-supplied constraints.

## Recursion, variety, escalation
Tools and RAG amplify S1 variety; workflow composition is not automatically recursive viability.
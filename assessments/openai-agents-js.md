---
harness_id: openai-agents-js
project_name: OpenAI Agents SDK for JavaScript
repository: https://github.com/openai/openai-agents-js
review_ref: 8831eae9d34365f9a397cbd52ae0366f304e1a96
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# OpenAI Agents SDK for JavaScript

## Review boundary
OpenAI Agents SDK JavaScript/TypeScript at the pinned revision as a framework for text/sandbox/realtime agents and multi-agent workflows.

## Repository architecture
Agents combine instructions, tools, guardrails and handoffs. Agents-as-tools/handoffs delegate tasks; sessions maintain history; HITL can pause runs; tracing records execution; sandbox agents support longer workspace tasks.

## Primary evidence
- `README.md`: agents, sandbox/realtime variants, agents-as-tools/handoffs, guardrails, HITL, sessions and tracing.

## Operational model
Individual agents are S1. Handoffs transfer task ownership rather than regulate mutual interference. Guardrails/tracing validate/observe normal execution.

## S1 — Operations
`A`: standard agents autonomously choose tools/actions toward outcomes. Confidence: high.

## S2 — Coordination
`—`: handoffs/agents-as-tools are delegation, not a supplied anti-oscillation function.

## S3 — Inside-and-now control
`?`: runner/session control is not autonomous whole-system regulation.

## S3* — Complementary audit
`?`: guardrails/tracing do not establish sufficiently independent complementary audit out of the box.

## S4 — Outside-and-then intelligence
`?`: sandbox long-horizon work is not external/prospective adaptation.

## S5 — Policy and identity
`?`: generic HITL, guardrails and instructions do not establish ultimate-policy/identity closure.

## Recursion, variety, escalation
Handoffs and agents-as-tools are compositional delegation, not recursion.
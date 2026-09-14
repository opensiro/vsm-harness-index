---
harness_id: strands-agents
project_name: Strands Agents
repository: https://github.com/strands-agents/harness-sdk
review_ref: 08ed4cfd3eb42ae9f668595e675d5f196eee7e44
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: ?
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# Strands Agents

## Review boundary
Strands Agents harness SDK at the pinned revision across its Python/TypeScript agent loops and documented multi-agent/evaluation surfaces.

## Repository architecture
Strands provides lifecycle controls, tools/MCP, multi-agent patterns, memory/sessions, guardrails, tracing, evals, hooks that can validate/redirect steps and steering handlers for self-correction.

## Primary evidence
- `README.md`: agent loop, multi-agent patterns, lifecycle controls, guardrails/tracing/evals, hooks and steering handlers.

## Operational model
Agents are S1. Multi-agent patterns are first-party, but the README does not specify enough of their interaction semantics to prove Beer S2. Evals/hooks are broad extensibility points rather than a clearly independent audit role.

## S1 — Operations
`A`: the SDK supplies ready autonomous model/tool loops. Confidence: high.

## S2 — Coordination
`?`: multi-agent patterns exist but no specific anti-oscillation decision right is established by the reviewed evidence.

## S3 — Inside-and-now control
`?`: lifecycle/budget controls are runtime constraints, not autonomous whole-system regulation.

## S3* — Complementary audit
`?`: tracing/evals/hooks can support audit but sufficient independence and corrective closure are not supplied as an explicit standard role.

## S4 — Outside-and-then intelligence
`?`: steering/self-correction is current-loop adaptation, not S4.

## S5 — Policy and identity
`?`: guardrails/budgets are configured constraints.

## Recursion, variety, escalation
Multi-agent patterns may compose nested actors, but recursion is not established by composition alone.
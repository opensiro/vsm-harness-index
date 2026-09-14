---
harness_id: eliza
project_name: Eliza
repository: https://github.com/elizaOS/eliza
review_ref: 5b183d21ff25a8c3e43af9a284a38b5ff487ded9
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: ?
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# Eliza

## Review boundary
elizaOS/eliza at the pinned revision, including its core `AgentRuntime`, app hosting and first-party plugins; bootable OS distributions are separate.

## Repository architecture
The monorepo contains an autonomous-agent runtime, message loop, memory/state, actions/providers/evaluators/services/events, scheduled workflows and coding-agent orchestration. Plugins extend operational capabilities and evaluators.

## Primary evidence
- `README.md`: autonomous-agent framework; `AgentRuntime` message loop/state; plugin actions/providers/evaluators/services/events; scheduled workflows and coding-agent orchestration.

## Operational model
Runtime agents are S1. Platform orchestration/evaluator plugin points may support metasystemic functions, but component names alone are not evidence of their VSM role.

## S1 — Operations
`A`: standard runtime agents choose actions and use plugin capabilities toward outcomes. Confidence: high.

## S2 — Coordination
`?`: coding-agent orchestration is first-party but the evidence does not establish anti-oscillation among autonomous S1s.

## S3 — Inside-and-now control
`?`: app/platform orchestration is not proven agent-owned whole-system regulation.

## S3* — Complementary audit
`?`: “evaluators” are plugin/runtime components; sufficient independence and alternative access to operational reality are not established by the label.

## S4 — Outside-and-then intelligence
`?`: scheduled workflows/environment connectors do not prove prospective adaptation.

## S5 — Policy and identity
`?`: runtime/plugin configuration does not establish legitimate ultimate-policy closure.

## Recursion, variety, escalation
Plugins and application targets expand operational variety; agent/workflow nesting is not automatically recursion.
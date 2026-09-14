---
harness_id: openai-agents-sdk
project_name: OpenAI Agents SDK Python
repository: https://github.com/openai/openai-agents-python
review_ref: fbd2dbcaaf74a2c447c6d3fa9d5645d83fd7e292
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# OpenAI Agents SDK Python

## Review boundary
OpenAI Agents SDK Python at the pinned revision as a framework for text/sandbox/realtime/voice agents and multi-agent workflows.

## Repository architecture
Agents combine instructions, tools, guardrails and handoffs. Agents-as-tools/handoffs delegate to specialists; sessions preserve history; HITL can pause runs; tracing records execution. Sandbox agents add long-horizon workspace action.

## Primary evidence
- `README.md`: agents, sandbox/realtime/voice variants; agents-as-tools/handoffs; guardrails; human-in-loop; sessions; tracing.

## Operational model
Individual agents are S1. Handoffs/agents-as-tools transfer/delegate work; that does not itself establish S2. Guardrails/tracing support safety/evidence but are not independent S3*.

## S1 — Operations
`A`: standard agents own bounded model/tool decisions and iterative task action. Confidence: high.

## S2 — Coordination
`—`: handoffs and agent-as-tool delegation do not specifically regulate interference among autonomous S1 units.

## S3 — Inside-and-now control
`?`: runner/session controls do not establish autonomous whole-system regulation.

## S3* — Complementary audit
`?`: guardrails and tracing validate/observe normal execution; no sufficiently independent complementary audit role is supplied out of the box.

## S4 — Outside-and-then intelligence
`?`: long-horizon sandboxing/planning does not establish external/prospective adaptation.

## S5 — Policy and identity
`?`: HITL/guardrails/instructions constrain operation, but generic approval/safety checks do not establish ultimate-policy/identity closure.

## Recursion, variety, escalation
Handoffs and agent-as-tool composition do not automatically produce recursively viable systems.
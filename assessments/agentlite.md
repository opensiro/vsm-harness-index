---
harness_id: agentlite
project_name: AgentLite
repository: https://github.com/SalesforceAIResearch/AgentLite
review_ref: b173239a652eea560e57c6fe46b0c0af7c4f3578
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: ?
autonomy_s4: —
autonomy_s5: —
---

# AgentLite

## Review boundary
AgentLite at the pinned revision as a research library for individual and manager-orchestrated agents.

## Repository architecture
AgentLite provides task-oriented tool-using agents and a `ManagerAgent` that controls team agents. The documented manager example calls one search agent, falls back to another if needed, then integrates answers.

## Primary evidence
- `README.md`: lightweight agent/multi-agent library; manager-agent orchestration; explicit manager example with sequential fallback and result integration.

## Operational model
Worker agents are S1. Manager selection/delegation/fallback is task routing, not anti-oscillation among independently interacting S1 units.

## S1 — Operations
`A`: workers run model-driven action loops over delegated tasks. Confidence: high.

## S2 — Coordination
`—`: manager routing and fallback do not establish mutual-adjustment/conflict regulation.

## S3 — Inside-and-now control
`—`: the manager lacks evidenced whole-system resource/accountability authority; title alone is insufficient.

## S3* — Complementary audit
`?`: no sufficiently independent audit function verified.

## S4 — Outside-and-then intelligence
`—`: no first-party prospective environment/adaptation function established.

## S5 — Policy and identity
`—`: goals/roles are application supplied; no runtime ultimate-policy closure.

## Recursion, variety, escalation
Manager/worker hierarchy is delegation rather than recursive viability.
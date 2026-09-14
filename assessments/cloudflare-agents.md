---
harness_id: cloudflare-agents
project_name: Cloudflare Agents
repository: https://github.com/cloudflare/agents
review_ref: 46760e635ce9599add0abbfe6c1a34af0d5d44f1
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# Cloudflare Agents

## Review boundary
Cloudflare Agents SDK at the pinned revision, including persistent agents, subagents, agent-as-tools and durable workflows.

## Repository architecture
Each Agent is a persistent Durable Object with state/storage/lifecycle. The SDK includes chat agent loops, parent/child subagents, agent tools, scheduling, workflows with human approval, tracing/metrics and sandboxed code execution.

## Primary evidence
- `README.md`: persistent Agent lifecycle/state; subagents/agent-tools; scheduling/workflows/HITL; `@cloudflare/think` agentic loop; observability.

## Operational model
Persistent agent instances are S1 units. Parent/child/agent-as-tool relations are task composition; durable workflows route/control execution.

## S1 — Operations
`A`: standard chat/think agents own bounded model/tool loops and persistent operational state. Confidence: high.

## S2 — Coordination
`—`: subagent/tool/workflow primitives shown do not specifically establish anti-oscillation among autonomous S1s; generic composition is insufficient for `C`.

## S3 — Inside-and-now control
`?`: Durable Object lifecycle/scheduling is infrastructure, not autonomous S3 regulation.

## S3* — Complementary audit
`?`: tracing/metrics are evidence infrastructure, not independent audit.

## S4 — Outside-and-then intelligence
`?`: schedules/events and retries are not prospective adaptation.

## S5 — Policy and identity
`?`: human approvals and workflow policy constrain actions but do not by themselves prove ultimate-policy/identity closure.

## Recursion, variety, escalation
Parent/child facets enable nested agents, but nested Durable Objects are not automatically recursively viable systems.
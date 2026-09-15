---
harness_id: cloudflare-agents
project_name: Cloudflare Agents
repository: https://github.com/cloudflare/agents
review_ref: 46760e635ce9599add0abbfe6c1a34af0d5d44f1
reviewed_at: 2026-09-15
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Cloudflare Agents

## Review boundary
Deep review of the pinned Agents SDK, including durable state, scheduling, agent-to-agent/tool exposure and documented workflow/subagent composition.

## Repository architecture
Cloudflare Agents provides durable autonomous agent instances on Durable Objects with persistent state, scheduling and RPC/tool integration. Agents can be composed and exposed as callable tools, but the reviewed primitives are infrastructure and delegation mechanisms rather than a VSM metasystem above multiple S1 units.

## Primary evidence
- `packages/agents/src/agent-tools.ts`: exposes agents as callable tools/RPC targets and resolves agent identity/communication for operational composition.
- `README.md`: documents persistent agents, scheduling, workflows and subagent patterns on Cloudflare's runtime.

## Operational model
An agent instance maintains durable state, receives events/messages, invokes model/tools and can call or expose other agents as part of an application-defined topology.

## S1 — Operations
`A`: first-party agent instances can autonomously execute model/tool behavior over persistent state and scheduled/event-driven work. Confidence: high.

## S2 — Coordination
`—`: agent-to-agent calls, workflows and subagent composition provide communication/delegation, but no distinct function was found that regulates interference or shared constraints among autonomous S1 units.

## S3 — Inside-and-now control
`—`: Durable Object lifecycle, routing and scheduling are runtime infrastructure. They do not establish whole-system managerial authority over operational commitments/resources in the VSM sense.

## S3* — Complementary audit
`—`: observability/state persistence does not create an independent complementary audit channel; no such first-party organizational function was established.

## S4 — Outside-and-then intelligence
`—`: scheduling and event processing concern execution timing, not prospective environmental intelligence and adaptation of system capability.

## S5 — Policy and identity
`—`: topology, tools, prompts, access and policies are application/developer supplied. No autonomous ultimate policy/identity function is included.

## Recursion, variety, escalation
The SDK can host recursive/multi-agent applications, but those applications must supply their own organizational closure; the SDK itself remains an S1-capable construction/runtime layer.
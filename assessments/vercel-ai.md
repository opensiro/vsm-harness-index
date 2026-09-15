---
harness_id: vercel-ai
project_name: Vercel AI SDK
repository: https://github.com/vercel/ai
review_ref: 6c6c2210b9532a4c369615c044a16d595f3db117
reviewed_at: 2026-09-15
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Vercel AI SDK

## Review boundary
Vercel AI SDK at the pinned revision, including the first-party `ToolLoopAgent` implementation and its tests. Application-authored multi-agent topologies are outside the boundary unless the SDK itself supplies the organizational decision right.

## Repository architecture
`ToolLoopAgent` is a provider-neutral model/tool execution loop. The model selects tools, consumes their results and may continue for further steps. `prepareCall`, stop conditions, tool approval, provider options and callbacks let the parent application constrain or observe that same loop.

## Primary evidence
- `packages/ai/src/agent/tool-loop-agent.ts`: model → tool call → tool result loop with configurable tools, `prepareCall`, stop conditions and step callbacks.
- `packages/ai/src/agent/tool-loop-agent.ts`: execution stops on finish conditions, missing executable tools, required approval, or configured/default step limits; these are runtime/application controls around one agent loop.
- `packages/ai/src/agent/tool-loop-agent.test.ts`: tests cover tool-call sequencing, `prepareCall`, instructions, sandbox propagation, timeout and callbacks, confirming the controls shape one operational loop rather than a distinct organizational actor.

## Operational model
The model-driven tool loop is one S1. Approval, stopping, preparation and callbacks are support/control surfaces owned by the application/runtime; they do not create a multi-S1 organization or separate metasystem actor.

## S1 — Operations
`A`: the agent autonomously selects/invokes tools, consumes results and continues until a stop condition. Confidence: high.

## S2 — Coordination
`—`: no autonomous interference regulation among multiple S1 units is supplied. Tool sequencing inside one agent and application-authored composition are not S2. Confidence: high.

## S3 — Inside-and-now control
`—`: step limits, `prepareCall`, provider options and parent callbacks constrain one agent run; no first-party agent-owned whole-system resource, priority or commitment regulator is supplied. Confidence: high.

## S3* — Complementary audit
`—`: tool approval is an execution gate and callbacks are observation hooks, not a sufficiently independent reviewer/auditor with corrective closure. Confidence: high.

## S4 — Outside-and-then intelligence
`—`: model/tool adaptation within the current task is operational behavior; no distinct external-and-prospective intelligence function coupled to S3 is supplied. Confidence: high.

## S5 — Policy and identity
`—`: instructions, tools, approvals, stop conditions and provider policy are parent/application supplied rather than decided by an ultimate agent-owned policy/identity function. Confidence: high.

## Recursion, variety, escalation
The SDK can compose larger systems, but composition does not establish recursive viability. Tool schemas and stop/approval rules attenuate action variety while remaining runtime support.

## Deep-review result
`S3`, `S3*`, `S4` and `S5` resolve from `?` to `—`; `S1 A` and `S2 —` are confirmed by implementation and tests.
---
harness_id: vercel-ai
project_name: Vercel AI SDK
repository: https://github.com/vercel/ai
review_ref: 6c6c2210b9532a4c369615c044a16d595f3db117
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# Vercel AI SDK

## Review boundary
Vercel AI SDK at the pinned revision, focusing on first-party `ToolLoopAgent` behavior rather than applications built on the SDK.

## Repository architecture
`ToolLoopAgent` repeatedly calls the model, executes tool calls, returns tool results to the next step, and stops on completion, missing execution, approval, or configured stop conditions.

## Primary evidence
- `packages/ai/src/agent/tool-loop-agent.ts`: explicit tool-loop semantics, tool execution/result feedback and stop/approval conditions at the pinned ref.

## Operational model
A `ToolLoopAgent` is one S1. Callbacks, stop conditions and approval gates constrain its loop; they do not create a separate autonomous metasystem.

## S1 — Operations
`A`: the model owns bounded tool selection/action across iterative steps. Confidence: high.

## S2 — Coordination
`—`: no distinct multi-S1 coordination function is established by the standard tool-loop primitive.

## S3 — Inside-and-now control
`?`: lifecycle callbacks/stop controls are runtime mechanisms, not autonomous whole-system regulation.

## S3* — Complementary audit
`?`: callbacks/telemetry do not constitute independent audit.

## S4 — Outside-and-then intelligence
`?`: tool feedback informs current action but not a demonstrated future/environment adaptation function.

## S5 — Policy and identity
`?`: instructions, approval policy and stop conditions are parent-supplied constraints.

## Recursion, variety, escalation
Tool sets amplify one S1's action variety; SDK composition does not imply recursive viability.
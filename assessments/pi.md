---
harness_id: pi
project_name: Pi
repository: https://github.com/earendil-works/pi
review_ref: 71dca871bc80b6bc97be37f0ca3189399d651fff
reviewed_at: 2026-09-15
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Pi

## Review boundary
Deep review of the pinned provider-neutral agent loop and coding-session runtime. Steering, follow-up queues and turn preparation are evaluated as controls around one S1 rather than organizational coordination.

## Repository architecture
Pi provides a reusable autonomous agent core plus a coding-agent product. The core loop repeatedly calls a model, validates/executes tool calls, feeds results back into context, supports steering/follow-up messages and optional per-turn preparation/stop callbacks. These mechanisms shape one operational agent trajectory.

## Primary evidence
- `packages/agent/src/agent-loop.ts`: implements the model→tool→result loop, emits agent/turn/tool events and continues while tool calls or pending messages remain.
- The loop can inject steering/follow-up messages and application-defined `prepareNextTurn`/`shouldStopAfterTurn` callbacks, but those are runtime/application controls over the same agent.

## Operational model
A Pi agent receives a prompt, selects tools, executes them, consumes results and continues until no further operational work remains or an external/runtime stop condition fires.

## S1 — Operations
`A`: autonomous model/tool iteration is the core first-party abstraction. Confidence: high.

## S2 — Coordination
`—`: message queues and steering coordinate turns within one agent session; no mechanism was found for regulating interference among multiple autonomous S1 units.

## S3 — Inside-and-now control
`—`: runtime callbacks and session controls do not create whole-system current authority over a multi-S1 organization.

## S3* — Complementary audit
`—`: no independent/complementary audit path distinct from normal tool-loop execution was established.

## S4 — Outside-and-then intelligence
`—`: context preparation, compaction and model changes between turns support current execution rather than a distinct prospective environment-intelligence function.

## S5 — Policy and identity
`—`: system prompts, tools, providers and stop/steering policy are parent/application supplied.

## Recursion, variety, escalation
Pi is a clean S1 runtime foundation; higher organizational functions must be composed outside it.
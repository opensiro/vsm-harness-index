---
harness_id: stagehand
project_name: Stagehand
repository: https://github.com/browserbase/stagehand
review_ref: b771930d2b4d858e5bd9670203c66260b385a8fa
reviewed_at: 2026-09-15
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Stagehand

## Review boundary
Stagehand at the pinned revision as the browser-agent SDK and execution environment, not Browserbase as an organization.

## Repository architecture
Stagehand exposes agent-optimized browser observation/action/extraction, self-healing primitives, context reduction and autonomous goal execution through `agent().execute()`.

## Primary evidence
- `packages/docs/v3/references/agent.mdx`: `AgentInstance.execute()` runs one autonomous browser agent with a high-level instruction, bounded steps, browser page, tool set, callbacks and cancellation.
- The reviewed agent surface supports DOM/hybrid/CUA action modes and iterative multi-step execution, but does not introduce a separate organizational layer.

## Operational model
A browser agent executing a goal is S1. Self-healing, callbacks, context reduction, action modes and execution limits all support or constrain that same operation.

## S1 — Operations
`A`: a standard browser agent autonomously chooses browser actions toward a goal. Confidence: high.

## S2 — Coordination
`—`: no material multi-S1 coordination path is supplied at this boundary.

## S3 — Inside-and-now control
`—`: max-step, abort, callback and execution controls regulate one S1 runtime rather than current commitments/resources across an organization.

## S3* — Complementary audit
`—`: callbacks and observability do not instantiate a distinct independent audit/corrective channel.

## S4 — Outside-and-then intelligence
`—`: self-healing reacts to changed pages during the current browser task; it is operational adaptation, not a prospective environment-to-S3 intelligence function.

## S5 — Policy and identity
`—`: system prompts, tools, models, modes and execution policy remain parent configured.

## Recursion, variety, escalation
Browser context and self-healing amplify one S1's environmental variety; no recursive viable subsystem is established.
---
harness_id: strands-agents
project_name: Strands Agents
repository: https://github.com/strands-agents/harness-sdk
review_ref: 08ed4cfd3eb42ae9f668595e675d5f196eee7e44
reviewed_at: 2026-09-15
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Strands Agents

## Review boundary
Deep review of the pinned first-party multi-agent `Swarm` implementation. Peer handoff alone is not enough for S2; the positive composable classification comes from an explicit configurable anti-oscillation mechanism around peer transfers.

## Repository architecture
Strands Agents provides autonomous tool-using agents plus first-party Graph and Swarm multi-agent runtimes. The Swarm supports agent-driven handoffs, shared context, dynamic transfer among peers and runtime tracking of repeated handoffs. A configurable repetitive-handoff threshold can detect/limit oscillatory transfer patterns. Because this regulation is a configurable capability rather than an always-closed autonomous coordination policy, it is classified as composable S2.

## Primary evidence
- `strands-py/src/strands/multiagent/swarm.py`: defines Swarm nodes, peer transfer/handoff execution, shared multi-agent state and dynamic next-agent behavior.
- The Swarm tracks handoff history/repetition and exposes a configurable repetitive-handoff threshold for preventing pathological transfer loops.
- At the reviewed revision that regulation is configuration-dependent rather than sufficient evidence of an always-active agent-owned coordination function.

## Operational model
Autonomous agents perform specialized work and can transfer execution to peers within a shared swarm context. The swarm runtime can detect repetitive handoff patterns when configured and constrain continued oscillation.

## S1 — Operations
`A`: individual agents autonomously select tools/actions and produce operational results. Confidence: high.

## S2 — Coordination
`C`: first-party Swarm primitives provide peer transfers plus a configurable mechanism specifically aimed at repetitive-handoff/oscillation control. This is more than delegation or static graph routing, but the developer must configure/close the regulation policy, so the function is composable rather than out-of-box agent-owned. Confidence: high.

## S3 — Inside-and-now control
`—`: swarm runtime state and transfer selection do not establish a whole-system authority that regulates shared resources, capacity, priorities and commitments across S1 units.

## S3* — Complementary audit
`—`: no independent complementary audit channel distinct from normal swarm execution was established.

## S4 — Outside-and-then intelligence
`—`: dynamic handoff selection responds to current task state, not a prospective environment-intelligence function adapting future system capability.

## S5 — Policy and identity
`—`: swarm membership, thresholds, prompts, tools and policy are developer/application supplied.

## Recursion, variety, escalation
Strands provides a real S2 construction primitive because it can regulate an identified multi-agent instability mode. It does not, at the reviewed boundary, close S3–S5.
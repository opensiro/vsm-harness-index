---
harness_id: letta
project_name: Letta
repository: https://github.com/letta-ai/letta
review_ref: 5bcdd177d70fa2b31a754cfcd801e77b2e1ab16a
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# Letta

## Review boundary
Letta at the pinned revision, including the repository's stated stateful-agent product boundary while recognizing that current harness source has moved to `letta-code`.

## Repository architecture
Letta provides stateful agents with persistent memory, identity and conversations across sessions/channels. The repository points current harness/runtime source to a separate first-party repository.

## Primary evidence
- `README.md`: stateful agents with memory; persistent identity/conversation; terminal/server/channels/SDK; explicit source-repository boundary.

## Operational model
A persistent Letta agent is S1. Memory changes its local context over time but does not by itself create S4 or a separate metasystem.

## S1 — Operations
`A`: stateful agents own bounded tool/action decisions across persistent interactions. Confidence: high.

## S2 — Coordination
`—`: no material multi-S1 anti-oscillation path is established in the reviewed repository boundary.

## S3 — Inside-and-now control
`?`: persistence/server management is not agent-owned whole-system regulation.

## S3* — Complementary audit
`?`: no independent audit path verified.

## S4 — Outside-and-then intelligence
`?`: learning/memory improvement over time is insufficient without external prospective adaptation coupled to S3.

## S5 — Policy and identity
`?`: persistent agent identity is a stored property; evidence does not show legitimate ultimate-policy closure.

## Recursion, variety, escalation
Persistent memory amplifies temporal S1 variety; channels and multiple agents do not alone establish recursion.
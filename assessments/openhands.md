---
harness_id: openhands
project_name: OpenHands
repository: https://github.com/OpenHands/OpenHands
review_ref: 28464621d879e3e9b3ceeae9d70a71d96da6212d
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# OpenHands

## Review boundary
OpenHands/Agent Canvas at the pinned revision. The repository is the user-facing control center; canonical agent behavior also lives in the first-party `software-agent-sdk` repository, an explicit boundary documented by OpenHands.

## Repository architecture
Agent Canvas runs the OpenHands coding agent out of the box and can connect to multiple agent backends. It provides conversations, automations, schedules/webhooks and a control center; agent servers execute coding agents in workspaces.

## Primary evidence
- `README.md`: OpenHands agent out-of-box; multiple agent backends; automation schedules/webhooks; explicit multi-repository responsibility table.

## Operational model
A running coding agent/conversation is S1. Canvas/backend selection and automation dispatch schedule independent operations but do not demonstrate autonomous anti-oscillation among S1s.

## S1 — Operations
`A`: standard OpenHands agents execute coding work with workspace tools. Confidence: high.

## S2 — Coordination
`—`: multiple backends/conversations and automation dispatch are operational routing, not an agent-owned coordination relation.

## S3 — Inside-and-now control
`?`: the control center is largely operator/runtime-owned; no autonomous whole-system regulator verified.

## S3* — Complementary audit
`?`: review/control-center evidence does not establish sufficiently independent autonomous audit.

## S4 — Outside-and-then intelligence
`?`: schedules/webhooks trigger current operations rather than a future-oriented adaptation loop.

## S5 — Policy and identity
`?`: agent/backend/configuration choices remain operator-owned.

## Recursion, variety, escalation
Multiple agent servers/backends are deployment topology, not recursive viability.
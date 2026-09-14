---
harness_id: rasa
project_name: Rasa
repository: https://github.com/RasaHQ/rasa
review_ref: 60a3cff9c08183760355b07bd60f5223d8916d6b
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# Rasa

## Review boundary
Classic Rasa Open Source as one deployed conversational assistant. Positive claims are limited to first-party runtime behavior at the pinned revision.

## Repository architecture
The runtime combines Agent, MessageProcessor, DialogueStateTracker, trained policies, actions, channels, and stores. Agent prediction selects the next action from tracked dialogue state and execution returns events into that state.

## Operational model
The dialogue loop is the S1 unit. Developer-authored training and configuration constrain it but are not runtime ownership.

## S1 — Operations
`A`: the runtime dialogue loop owns bounded next-action selection and continues from returned events. Structural; high confidence.

## S2 — Coordination
`—`: one dialogue S1 is in focus. Locks and routing are execution mechanics rather than cross-S1 anti-oscillation coordination.

## S3 — Inside-and-now control
`?`: no verified autonomous whole-system regulator with shared-resource authority.

## S3* — Complementary audit
`?`: tracing and tests do not establish independent complementary audit.

## S4 — Outside-and-then intelligence
`?`: training does not establish an autonomous external-and-prospective adaptation loop.

## S5 — Policy and identity
`?`: configured rules and fallback do not establish runtime identity or ultimate-policy closure.

## Recursion, variety, escalation
Nested actions do not prove recursion. Dialogue state attenuates history into prediction state; policies amplify it into an action repertoire.

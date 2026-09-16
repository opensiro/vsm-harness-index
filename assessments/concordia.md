---
harness_id: concordia
project_name: Concordia
repository: https://github.com/google-deepmind/concordia
review_ref: 3e30a207bb2b75f9cf837fa6b657c466ca450765
reviewed_at: 2026-09-16
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: C
---

# Concordia

## Review boundary
Pinned generative multi-agent simulation harness, treating player entities as operations and Game Master/environment as the shared-world regulator.

## Repository architecture
Player entities generate putative actions. Game Master schedules/observes/resolves them into authoritative world events and updates shared world state, including simultaneous/interrupt-driven resolution.

## Primary evidence
- Pinned deep review established player action generation and Game Master scheduling/observation/authoritative event resolution at `review_ref`.

## Operational model
Players are autonomous S1 units. Constructor-defined Game Master mechanisms coordinate shared-world interaction and regulate authoritative current state.

## S1 — Operations
`A`: player entities autonomously choose putative actions. Confidence: high.

## S2 — Coordination
`C`: shared-world scheduling plus simultaneous/interrupt-driven resolution coordinate multiple players. Confidence: high.

## S3 — Inside-and-now control
`C`: Game Master owns authoritative event resolution and world-state update. Confidence: high.

## S3* — Complementary audit
`—`: authoritative event resolution is the ordinary control path, not a separate complementary audit channel. Confidence: high.

## S4 — Outside-and-then intelligence
`—`: simulating future scenarios does not itself constitute prospective adaptation of the organization. Confidence: high.

## S5 — Policy and identity
`C`: scenario premises and Game Master rules are constructor-authored policy/identity surfaces. Confidence: high.

## Recursion, variety, escalation
Game Master attenuates conflicting player action into authoritative events; simulation nesting does not automatically establish recursive viability.

## Deep-review conclusion
Signature at the pinned revision: `A C C — — C`. Concordia cleanly separates autonomous players from constructor-owned shared-world coordination/control.
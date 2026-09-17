---
harness_id: concordia
project_name: Concordia
repository: https://github.com/google-deepmind/concordia
review_ref: 3e30a207bb2b75f9cf837fa6b657c466ca450765
reviewed_at: 2026-09-17
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
assessment_changed_at: 2026-09-17
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Concordia

## Review boundary
Pinned first-party Concordia generative social-simulation harness: autonomous player entities, Game Master entities, and the sequential/simultaneous engines that schedule actions, resolve putative events, and return authoritative observations. Scenario-authored organizational semantics outside these supplied paths are not credited.

Reviewed revision: `3e30a207bb2b75f9cf837fa6b657c466ca450765`, which also matched upstream `main` when rechecked on 2026-09-17. Contract: Profile `0.2.1`, Methodology `0.3.1`.

## Primary evidence
- [`README.md`](https://github.com/google-deepmind/concordia/blob/3e30a207bb2b75f9cf837fa6b657c466ca450765/README.md) — entities, Game Masters and Engine boundary.
- [`concordia/environment/engines/sequential.py`](https://github.com/google-deepmind/concordia/blob/3e30a207bb2b75f9cf837fa6b657c466ca450765/concordia/environment/engines/sequential.py) — one-entity-at-a-time scheduling, Game Master selection, event resolution and subsequent observations.
- [`concordia/environment/engines/simultaneous.py`](https://github.com/google-deepmind/concordia/blob/3e30a207bb2b75f9cf837fa6b657c466ca450765/concordia/environment/engines/simultaneous.py) — grouped simultaneous actions and common resolution.

## S1 — Operations
`A`. Player entities autonomously choose putative actions within the simulated domain. Their decisions are the operational transformations the harness exists to exercise. Confidence: high.

## S2 — Coordination
`C`. Concordia supplies an explicit cross-player interaction membrane: the sequential engine allows one entity to act at a time when order matters, while both engine forms route putative actions through common Game Master resolution before the resulting event becomes subsequent shared observation. This closes ordering/interaction interference across multiple S1s rather than merely forwarding messages. The concrete scenario, Game Master components and action semantics remain constructor-supplied, so the organizational coordination path is composable rather than an out-of-box autonomous S2. Confidence: medium-high.

## S3 — Inside-and-now control
`—`. Game Master event resolution is authoritative over the simulated world's causality, but that is the ordinary environment-resolution path. The reviewed repository does not separately establish a whole-organization current view plus authority over shared organizational resources, commitments, priorities or constraints. The historical `C` promoted environment/world-state control into S3. Confidence: high.

## S3* — Complementary audit
`—`. Event resolution and logging are part of the normal simulation path, not materially complementary access to operational reality. Confidence: high.

## S4 — Outside-and-then intelligence
`—`. Running social simulations or choosing future simulated events does not itself create an outside-and-then intelligence loop that adapts the system-in-focus. Confidence: high.

## S5 — Policy and identity
`—`. Scenario premises, Game Master rules and component configuration carry developer-authored policy, but no first-party runtime path was established in which identity/ultimate-policy tension reaches legitimate ultimate authority and returns as changed organizational policy. The historical `C` therefore does not survive the function-first S5 test. Confidence: high.

## Recursion, variety, and escalation
Multiple autonomous players amplify behavioral variety; engine scheduling and common event resolution attenuate interaction variety into one coherent simulated history. Game Master authority over simulation causality should not be confused with metasystem authority over an organization.

## Admission conclusion
Canonical vector: `A C — — — —`.

Same-ref correction of historical `A C C — — C`: constructor-side S2 remains supported by the explicit interaction/scheduling membrane; world-state resolution and static scenario rules no longer count as S3 or S5.
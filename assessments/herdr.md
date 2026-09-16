---
harness_id: herdr
project_name: Herdr
repository: https://github.com/herdrdev/herdr
review_ref: 18061191fdc019498610aee81f0df93f6c2ebd31
reviewed_at: 2026-09-16
status: proposed
autonomy_s1: C
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Herdr

## Review boundary
Pinned persistent agent-terminal runtime hosting external Claude, Codex, Cursor and OpenCode workers.

## Repository architecture
Herdr owns agent session spawning, prompting, waiting, status classification, resume and agent-aware terminal APIs while domain cognition remains in external agents.

## Primary evidence
- Pinned review established persistent session lifecycle, status classification and spawn/prompt/wait/resume control at `review_ref`.

## Operational model
External coding agents are hosted S1 units; Herdr supplies the shared execution/session substrate used to coordinate their coexistence.

## S1 — Operations
`C`: external agents provide operational cognition through Herdr's hosting surface. Confidence: high.

## S2 — Coordination
`C`: persistent agent/session state and agent-aware APIs provide composable coordination across hosted workers. Confidence: medium-high.

## S3 — Inside-and-now control
`—`: no whole-system operational regulation authority beyond session lifecycle was established. Confidence: high.

## S3* — Complementary audit
`—`: no distinct complementary audit channel was established. Confidence: high.

## S4 — Outside-and-then intelligence
`—`: no prospective environment-facing adaptation function was established. Confidence: high.

## S5 — Policy and identity
`—`: purpose/policy are supplied externally. Confidence: high.

## Recursion, variety, escalation
Multiple persistent agents increase operational variety; status/resume mechanisms attenuate execution-state uncertainty without closing a higher metasystem.

## Deep-review conclusion
Signature at the pinned revision: `C C — — — —`. Herdr is a composable multi-agent terminal runtime rather than a self-governing organization.
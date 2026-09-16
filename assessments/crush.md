---
harness_id: crush
project_name: Crush
repository: https://github.com/charmbracelet/crush
review_ref: 09fc6d11921ff8a31c89ccea5fc41fc9e58629f5
reviewed_at: 2026-09-16
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: P
---

# Crush

## Review boundary
Pinned first-party coding agent including parallel agent tool, centralized permission service and hook-level approval behavior.

## Repository architecture
Crush can run parallel agents and centralizes permission decisions with one-shot/persistent grant/deny semantics, race-safe first resolution and exact-call hook approval.

## Primary evidence
- Pinned deep review established parallel-agent execution and centralized permission/approval service at `review_ref`.

## Operational model
Agents perform autonomous coding work while constructor/runtime permission machinery coordinates and regulates concurrent action; ultimate approval remains parent-owned.

## S1 — Operations
`A`: coding agents autonomously select tools/actions. Confidence: high.

## S2 — Coordination
`C`: parallel-agent runtime plus centralized permission resolution provide composable cross-agent coordination. Confidence: medium-high.

## S3 — Inside-and-now control
`C`: centralized permission service and exact-call approval hooks regulate current execution. Confidence: high.

## S3* — Complementary audit
`—`: no independent complementary audit channel was established. Confidence: high.

## S4 — Outside-and-then intelligence
`—`: no prospective organizational adaptation function was established. Confidence: high.

## S5 — Policy and identity
`P`: grant/deny approval ultimately belongs to the parent/user policy boundary. Confidence: high.

## Recursion, variety, escalation
Parallel agents amplify operational variety; permission serialization/race-safe resolution attenuate conflicting action and escalate unresolved authority.

## Deep-review conclusion
Signature at the pinned revision: `A C C — — P`. Crush combines autonomous coding with constructor-owned coordination/current control and parent-owned policy.
---
harness_id: orca-stablyai
project_name: Orca
repository: https://github.com/stablyai/orca
review_ref: c33a446190bdfa21286a373e097c50a2b3e0a4d4
reviewed_at: 2026-09-16
status: proposed
autonomy_s1: C
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: P
autonomy_s4: —
autonomy_s5: P
---

# Orca

## Review boundary
Pinned desktop/control-plane distribution around external CLI coding agents.

## Repository architecture
Orca supplies isolated worktrees, fan-out, persistent sessions/status and remote steering. Humans compare diffs, annotate and decide merge/acceptance.

## Primary evidence
- Pinned review established worktree isolation, fan-out, persistent session/status, remote steering and human diff compare/merge at `review_ref`.

## Operational model
External agents perform coding work; Orca structures concurrent execution and exposes outputs to a parent reviewer.

## S1 — Operations
`C`: operational cognition is supplied by external CLI agents. Confidence: high.

## S2 — Coordination
`C`: worktree/session isolation and fan-out provide composable coexistence/coordination mechanisms. Confidence: medium-high.

## S3 — Inside-and-now control
`—`: session steering did not establish a distinct whole-system current-control function. Confidence: high.

## S3* — Complementary audit
`P`: human diff comparison/annotation/merge supplies the complementary review decision. Confidence: high.

## S4 — Outside-and-then intelligence
`—`: no prospective organizational adaptation loop was established. Confidence: high.

## S5 — Policy and identity
`P`: acceptance and ultimate work authority remain human-owned. Confidence: high.

## Recursion, variety, escalation
Parallel worktrees amplify candidate variety while human comparison attenuates it at the acceptance boundary.

## Deep-review conclusion
Signature at the pinned revision: `C C — P — P`. Orca is a human-governed control plane around external coding agents.
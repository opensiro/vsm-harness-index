---
harness_id: nerve
project_name: Nerve
repository: https://github.com/ClickHouse/nerve
review_ref: 079548115c5c4c1d826f0ab8034c1001cac9ef7f
reviewed_at: 2026-09-16
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: C
autonomy_s3_star: —
autonomy_s4: P
autonomy_s5: P
---

# Nerve

## Review boundary
Pinned persistent single-worker control loop with cron task planner, plan lifecycle, human approval, implementation sessions and skill extractor/reviser.

## Repository architecture
Current distribution operates one worker rather than the retired House-of-Agents multi-worker design. Runtime manages plans/tasks/cron/permissions; recurring skill extraction/revision proposes durable capability changes subject to human approval.

## Primary evidence
- Pinned deep review established single-worker current boundary, plan/task lifecycle, cron gating, permission handling and skill extraction/revision at `review_ref`.

## Operational model
One autonomous worker performs operations; runtime controls current plan/task state; future capability proposals are generated from experience but require parent approval.

## S1 — Operations
`A`: worker autonomously executes implementation work. Confidence: high.

## S2 — Coordination
`—`: current standard distribution has one operational unit; retired House of Agents is not credited. Confidence: high.

## S3 — Inside-and-now control
`C`: plan/task lifecycle, cron gating and permission handling provide constructor-owned current regulation. Confidence: high.

## S3* — Complementary audit
`—`: no independent complementary audit channel was established. Confidence: high.

## S4 — Outside-and-then intelligence
`P`: recurring skill extraction/revision inspects operational experience and proposes durable future capability changes, but human approval closes adaptation. Confidence: high.

## S5 — Policy and identity
`P`: durable approval boundary retains ultimate policy authority with the human. Confidence: high.

## Recursion, variety, escalation
Cron and plan state attenuate operational variety; skill proposals amplify future capability variety while approval gates escalation.

## Deep-review conclusion
Signature at the pinned revision: `A — C — P P`. Nerve is a single-worker harness with meaningful parent-governed prospective adaptation.
---
harness_id: mini-harness
project_name: mini-harness
repository: https://github.com/mini-harness/mini-harness
review_ref: 340d2d9f1bcc833483d2924770448fcf4ef788be
reviewed_at: 2026-09-16
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: P
---

# mini-harness

## Review boundary
Pinned first-party coding-agent loop and its standard interactive/task execution modes.

## Repository architecture
A single coding-agent loop owns model/tool iteration with deterministic turn and wall-clock budgets, context compaction and retry behavior. Interactive mode can require human tool approval; task mode can allow tools automatically.

## Primary evidence
- Pinned review established the single-agent loop, budgets, compaction/retry and interactive approval boundary at `review_ref`.

## Operational model
One S1 performs the work. Runtime safeguards bound execution but do not constitute a metasystem over multiple operational units.

## S1 — Operations
`A`: the coding agent autonomously iterates through model/tool work. Confidence: high.

## S2 — Coordination
`—`: no multi-S1 mutual-adjustment function was established. Confidence: high.

## S3 — Inside-and-now control
`—`: budgets and loop lifecycle constrain one operation rather than regulate a whole operational system. Confidence: high.

## S3* — Complementary audit
`—`: no distinct complementary audit channel was established. Confidence: high.

## S4 — Outside-and-then intelligence
`—`: retry/compaction are current execution mechanisms, not prospective adaptation. Confidence: high.

## S5 — Policy and identity
`P`: human approval and externally supplied task/policy retain ultimate authority. Confidence: high.

## Recursion, variety, escalation
Variety is bounded by budgets and approvals; no viable recursive metasystem was established.

## Deep-review conclusion
Signature at the pinned revision: `A — — — — P`. Strong autonomous S1, with outer policy retained by the parent.
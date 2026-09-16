---
harness_id: camel-workforce
project_name: CAMEL Workforce
repository: https://github.com/camel-ai/camel
review_ref: 8c791b7b9cf7deab56cb5a92818c34499af9097f
reviewed_at: 2026-09-16
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: P
---

# CAMEL Workforce

## Review boundary
Pinned Workforce runtime with Coordinator Agent, Task Planner Agent, task/dependency/assignee/in-flight state, failure analysis/recovery, dynamic workers and human intervention.

## Repository architecture
Coordinator and Task Planner operate over shared workforce state. Coordinator assigns/tracks work, analyzes failures, can replan and create workers; quality/failure evaluation is configurable rather than a protected independent auditor.

## Primary evidence
- Pinned deep review established coordinator/planner roles, TaskChannel/dependencies, failure recovery, dynamic worker creation, nested Workforces and human intervention at `review_ref`.

## Operational model
Workers are S1s. Autonomous coordinator closes coordination and current control; configurable evaluation challenges outcomes; human intervention remains outer authority.

## S1 — Operations
`A`: worker agents autonomously execute tasks. Confidence: high.

## S2 — Coordination
`A`: coordinator plus TaskChannel/dependency state regulate multiple workers. Confidence: high.

## S3 — Inside-and-now control
`A`: coordinator assigns/tracks work, analyzes failures, replans and can create replacement/new workers. Confidence: high.

## S3* — Complementary audit
`C`: quality/failure evaluation provides a challenge surface, but independence/protection remains configured rather than autonomous. Confidence: medium-high.

## S4 — Outside-and-then intelligence
`—`: dynamic worker creation/replanning is current-task recovery, not prospective environment-facing adaptation. Confidence: high.

## S5 — Policy and identity
`P`: pause/stop/skip human intervention and external objective preserve parent authority. Confidence: high.

## Recursion, variety, escalation
Nested Workforces are technically possible; dynamic worker creation amplifies corrective variety while human intervention supplies escalation.

## Deep-review conclusion
Signature at the pinned revision: `A A A C — P`. CAMEL Workforce closes strong autonomous S2/S3 without over-crediting current-task replanning as S4.
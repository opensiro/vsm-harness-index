---
harness_id: eigent
project_name: Eigent
repository: https://github.com/eigent-ai/eigent
review_ref: 6c49956b2aa878c08bee5edcf8a1eb63122c2cd9
reviewed_at: 2026-09-17
profile_version: 0.2.2
assessment_procedure_version: 0.3.1
assessment_changed_at: 2026-09-17
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Eigent

## Review boundary
Pinned Eigent Multi-Agent Workforce runtime: autonomous workforce agents, coordinator/task-agent planning, dependency-aware task graph, model-driven assignment, retry/replanning and publication of runnable work. UI/admin permissions are treated as outer controls unless they close the relevant VSM function.

Reviewed revision: `6c49956b2aa878c08bee5edcf8a1eb63122c2cd9`. Contract: Profile `0.2.2`, Methodology `0.3.1`.

## Primary evidence
- [`backend/app/utils/workforce.py`](https://github.com/eigent-ai/eigent/blob/6c49956b2aa878c08bee5edcf8a1eb63122c2cd9/backend/app/utils/workforce.py) — model-driven coordinator/task agents, task decomposition/dependencies, assignee selection, retry/replanning and dependency-gated task publication.

## S1 — Operations
`A`. Workforce agents autonomously execute assigned tool/model work. Confidence: high.

## S2 — Coordination
`A`. The task agent produces an explicit dependency graph and runnable work is published only after dependencies are satisfied; the model-driven workforce path selects assignees and reacts to task state. This closes dependency/ordering interference across autonomous S1s rather than merely routing messages. Confidence: high.

## S3 — Inside-and-now control
`A`. The model-driven coordinator has a workforce-wide view and authority over assignment, retries/replanning and current task progression. These are current whole-team regulation decisions owned by an autonomous first-party agent path. Confidence: high.

## S3* — Complementary audit
`—`. No materially independent complementary audit channel with distinct evidence access and corrective closure was established. Confidence: high.

## S4 — Outside-and-then intelligence
`—`. Planning and replanning address current task execution; no separate prospective environment-facing organizational adaptation loop was established. Confidence: high.

## S5 — Policy and identity
`—`. Human permissions/configuration constrain execution but do not establish identity/ultimate-policy closure. Confidence: high.

## Recursion, variety, and escalation
Specialized workforce members amplify capability variety; dependency gates and coordinator assignment/replanning attenuate it into a coherent task graph. Human controls remain an outer operational authority path rather than S5.

## Admission conclusion
Canonical vector: `A A A — — —`.

The earlier stale proposal `A A A — — P` correctly identified autonomous S2/S3 but over-promoted ordinary human control into S5.
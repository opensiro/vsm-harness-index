---
harness_id: nerve
project_name: Nerve
repository: https://github.com/ClickHouse/nerve
review_ref: 079548115c5c4c1d826f0ab8034c1001cac9ef7f
reviewed_at: 2026-09-17
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
assessment_changed_at: 2026-09-17
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Nerve

## Review boundary
Pinned first-party Nerve worker-mode runtime: one autonomous worker, planner/plan lifecycle, cron, approval/permissions, implementation sessions, and skill extractor/reviser. The retired House-of-Agents design is not credited.

Reviewed revision: `079548115c5c4c1d826f0ab8034c1001cac9ef7f`, which also matched upstream `main` when rechecked on 2026-09-17. Contract: Profile `0.2.1`, Methodology `0.3.1`.

## Primary evidence
- [`docs/worker-guide.md`](https://github.com/ClickHouse/nerve/blob/079548115c5c4c1d826f0ab8034c1001cac9ef7f/docs/worker-guide.md) — worker mode and plan-approve-execute.
- [`README.md`](https://github.com/ClickHouse/nerve/blob/079548115c5c4c1d826f0ab8034c1001cac9ef7f/README.md) — planner cron and approval lifecycle.
- [`docs/cron.md`](https://github.com/ClickHouse/nerve/blob/079548115c5c4c1d826f0ab8034c1001cac9ef7f/docs/cron.md) — skill extractor/reviser jobs and approval-triggered skill updates.
- [`docs/architecture.md`](https://github.com/ClickHouse/nerve/blob/079548115c5c4c1d826f0ab8034c1001cac9ef7f/docs/architecture.md) — single worker boundary.

## S1 — Operations
`A`. The worker autonomously researches, plans and executes task-focused implementation work inside its permissions. Confidence: high.

## S2 — Coordination
`—`. The current standard distribution has one S1 worker. Routing, channels, cron and the retired multi-worker design do not supply a current inter-S1 coordination function. Confidence: high.

## S3 — Inside-and-now control
`—`. Plan/task lifecycle, cron scheduling, permission gates and implementation-session transitions regulate one worker's operational workflow. They do not establish a separate whole-system current view plus authority over shared organizational resources, commitments or priorities. The historical `C` therefore collapses into S1/runtime support. Confidence: high.

## S3* — Complementary audit
`—`. No independent complementary access path to operational reality was established. Confidence: high.

## S4 — Outside-and-then intelligence
`—`. Skill extraction/revision does change future capability, but its source is accumulated internal operational experience. The reviewed path does not establish the required outside-and-then environmental intelligence loop; learning/self-improvement alone is not S4. Human approval of those proposals does not create S4 `P`. Confidence: high.

## S5 — Policy and identity
`—`. Human approval is explicit, but it approves plans/skill changes in the operational lifecycle rather than closing an identity/ultimate-policy decision path for the system-in-focus. Generic parent approval is not S5 `P`. Confidence: high.

## Recursion, variety, and escalation
Cron and plan state bound the worker's operational variety; skill proposals can alter future local capability after approval. None of these mechanisms establishes recursive viability or a higher metasystem at this boundary.

## Admission conclusion
Canonical vector: `A — — — — —`.

Same-ref correction of historical `A — C — P P`. The old S3/S4/S5 positives were workflow control, internal learning and ordinary human approval rather than the corresponding VSM functions.
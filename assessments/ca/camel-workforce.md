---
harness_id: camel-workforce
project_name: CAMEL Workforce
repository: https://github.com/camel-ai/camel
review_ref: 8c791b7b9cf7deab56cb5a92818c34499af9097f
reviewed_at: 2026-09-17
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
assessment_changed_at: 2026-09-17
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# CAMEL Workforce

## Review boundary
Pinned first-party CAMEL `Workforce`: worker agents, Coordinator Agent, Task Planner Agent, shared pending/completed/dependency/assignee state, failure recovery, dynamic worker creation, callbacks/metrics, and human pause/stop controls. General CAMEL framework features outside Workforce are not automatically credited.

Reviewed revision: `8c791b7b9cf7deab56cb5a92818c34499af9097f`. Contract: Profile `0.2.1`, Methodology `0.3.1`. Current upstream was checked separately; the candidate pin is preserved.

## Primary evidence
- [`camel/societies/workforce/workforce.py`](https://github.com/camel-ai/camel/blob/8c791b7b9cf7deab56cb5a92818c34499af9097f/camel/societies/workforce/workforce.py) — Workforce state, Coordinator/Task Planner, dependency state, assignment, recovery and dynamic workers.
- [`docs/key_modules/workforce.md`](https://github.com/camel-ai/camel/blob/8c791b7b9cf7deab56cb5a92818c34499af9097f/docs/key_modules/workforce.md) — documented Workforce operating model.
- [`test/workforce/test_workforce_pipeline.py`](https://github.com/camel-ai/camel/blob/8c791b7b9cf7deab56cb5a92818c34499af9097f/test/workforce/test_workforce_pipeline.py) — dependency behavior.

## S1 — Operations
`A`. Worker agents autonomously execute assigned task work through model/tool loops. Confidence: high.

## S2 — Coordination
`C`. Workforce maintains explicit cross-task dependency state and gates release/order of work across multiple workers. This prevents dependent S1 work from proceeding against unsatisfied predecessor commitments, establishing a concrete coordination path beyond routing. The mechanism is supplied deterministically by Workforce while the application supplies the task graph, so ownership is constructor-side rather than agent-owned. Confidence: high.

## S3 — Inside-and-now control
`A`. The Coordinator operates over shared workforce state, assigns work based on worker capability, tracks current commitments, handles failures, and can create new workers or redirect/replan work. These are whole-workforce current-control rights over assignments and available operational capacity. The model-driven coordinator owns the runtime choice within configured bounds. Confidence: high.

## S3* — Complementary audit
`—`. Quality/failure analysis evaluates returned task results in the ordinary Workforce control/reporting path. No materially complementary evidence-access channel or protected independent audit boundary was established. The historical `C` therefore does not survive current S3* criteria. Confidence: high.

## S4 — Outside-and-then intelligence
`—`. Replanning and dynamic worker creation respond to current-task failure; they do not establish an external/future environmental intelligence loop that changes organizational capability. Confidence: high.

## S5 — Policy and identity
`—`. Human pause/stop/skip controls and the externally supplied objective are parent/operator controls over ordinary execution, not a demonstrated ultimate-policy/identity closure path. The historical `P` is therefore removed. Confidence: high.

## Recursion, variety, and escalation
Nested Workforces are technically composable, but each nested instance requires its own functional evidence before being counted as recursively viable. Dynamic worker creation amplifies current operational variety; dependency gates, assignment and recovery attenuate it; human controls provide operational escalation without constituting S5.

## Admission conclusion
Canonical vector: `A C A — — —`.

Same-ref correction of historical `A A A C — P`: S2 remains but is classified constructor-owned because the decisive dependency gate is runtime machinery; S3 remains autonomous through the Coordinator; ordinary evaluation and human intervention are no longer promoted to S3*/S5.
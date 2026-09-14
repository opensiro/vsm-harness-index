---
harness_id: agentrl
project_name: AgentRL
repository: https://github.com/THUDM/AgentRL
review_ref: 6a73409d31ba695d383b978a8ad3ef400d90c054
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: —
autonomy_s5: ?
---

# AgentRL

## Review boundary
AgentRL at the pinned revision as an environment/training framework for multi-turn LLM agents. Ray training workers are training infrastructure, not S1 organizational units of a deployed agent system.

## Repository architecture
The environment runs agent tasks/trajectories while the trainer uses rollout, actor and reference worker pools plus task managers and GRPO to update policies. Evaluation is a separate package/path.

## Primary evidence
- `README.md`: environment deployment, multi-turn agent tasks, rollout/actor/reference workers, task manager, policy updates and evaluation.

## Operational model
The LLM agent acting in a task environment supplies S1 action. Distributed workers are compute/training roles and must not be misclassified as VSM operational units.

## S1 — Operations
`A`: the framework runs model-driven multi-turn agent trajectories that act against task environments. Confidence: medium-high.

## S2 — Coordination
`—`: Ray worker synchronization/task queues coordinate computation, not autonomous operational S1 units in the VSM system-in-focus.

## S3 — Inside-and-now control
`?`: training/task managers regulate compute/data flow, not the deployed organization’s current operations.

## S3* — Complementary audit
`?`: reference workers/evaluation are training/eval mechanisms, not proven independent operational audit.

## S4 — Outside-and-then intelligence
`—`: GRPO/policy training changes future behavior offline, but training is not a runtime external/prospective S4↔S3 intelligence function.

## S5 — Policy and identity
`?`: objectives/rewards/configuration are externally supplied.

## Recursion, variety, escalation
Distributed training topology is not organizational recursion.
---
harness_id: agentrl
project_name: AgentRL
repository: https://github.com/THUDM/AgentRL
review_ref: 6a73409d31ba695d383b978a8ad3ef400d90c054
reviewed_at: 2026-09-15
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# AgentRL

## Review boundary
Deep review of the pinned agentic rollout and distributed training architecture. Compute-worker scheduling and reinforcement-learning feedback are not mapped onto runtime VSM functions unless they govern a viable multi-S1 organization during operation.

## Repository architecture
AgentRL is a reinforcement-learning system for agentic models. Rollout workers execute multiturn agent tasks and produce trajectories while actor/reference workers train policy parameters. A Task Manager asynchronously generates/queues training tasks and bridges rollout data to the trainer. These worker roles are training-compute components, not operational units mutually coordinating a live organization.

## Primary evidence
- `README.md`: actor/reference workers and rollout workers occupy separate resource groups; the Task Manager asynchronously generates tasks with rollout workers while the trainer pushes tasks and consumes old rollout data for GRPO training.
- `examples/training/async_trainer.py` / `agentrl_trainer.py`: Ray placement groups divide GPU resources between rollout and actor/reference training workers.
- `trainer/src/agentrl/trainer/agentic/loops.py`: rollout loops generate agent trajectories used as learning data.

## Operational model
Rollout agents autonomously execute benchmark/environment tasks and generate trajectories. The surrounding distributed system schedules training compute and updates policy parameters from collected experience.

## S1 — Operations
`A`: each rollout agent can execute a multiturn environment task autonomously and produce operational trajectories. Confidence: high.

## S2 — Coordination
`—`: Ray placement, task queues and worker pools coordinate training infrastructure, not interference among autonomous operational S1 units pursuing shared live commitments. The shallow `S2=C` interpretation is removed.

## S3 — Inside-and-now control
`—`: Task Manager/trainer scheduling governs the training pipeline rather than current operational commitments of a viable multi-S1 system.

## S3* — Complementary audit
`—`: reward/loss computation evaluates training trajectories for optimization, not an independent complementary audit channel governing live S1 work.

## S4 — Outside-and-then intelligence
`—`: RL converts historical environment outcomes into updated model parameters, but it is an offline/development training loop rather than a distinct runtime S4 function scanning future external conditions and adapting organizational capability. The shallow `S4=C` interpretation is removed.

## S5 — Policy and identity
`—`: reward design, tasks, training configuration and deployment purpose remain externally supplied.

## Recursion, variety, escalation
AgentRL improves future S1 policy through distributed training, but its distributed worker topology should not be mistaken for a runtime VSM metasystem.
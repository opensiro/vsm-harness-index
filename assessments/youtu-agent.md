---
harness_id: youtu-agent
project_name: Youtu-Agent
repository: https://github.com/TencentCloudADP/youtu-agent
review_ref: c2caa539f4c95ae1c39ed24dc8a99cb3651e1d5d
reviewed_at: 2026-09-15
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
last_checked_ref: c2caa539f4c95ae1c39ed24dc8a99cb3651e1d5d
last_checked_at: 2026-09-17
assessment_changed_at: 2026-09-15
last_reassessment_round: R2
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Youtu-Agent

## Review boundary
Deep review of the pinned SimpleAgent/Orchestrator and Agent Practice surfaces. Agent generation, task planning and training/practice components are not mapped to S2/S4 unless they implement the corresponding runtime organizational function.

## Repository architecture
Youtu-Agent provides tool-using simple agents, a planner-driven orchestrator over specialist workers, automatic agent/tool generation and an Agent Practice learning module. The chain orchestrator uses an LLM planner to produce a fixed ordered list of worker tasks and then executes those workers sequentially. At the pinned revision replanning is explicitly still a TODO. Practice/training components operate outside the runtime organization to improve policies/experience.

## Primary evidence
- `utu/agents/orchestrator_agent.py`: builds a planner plus configured worker agents and runs planned tasks one by one; the source explicitly lists `replan` as not yet implemented.
- `utu/agents/orchestrator/chain.py`: an LLM router/planner creates a task list assigning each step to a worker, and `get_next_task` advances through that fixed plan.
- `utu/meta/simple_agent_generator.py` and auto-generation docs: meta-agent functionality generates agent prompts/config/tooling from requirements.
- Agent Practice / training-free GRPO machinery learns from rollouts outside the current runtime control loop.

## Operational model
A runtime agent chooses tools and reacts to results. In orchestrator mode an LLM decomposes the present request into sequential specialist tasks and returns their outputs through one task trajectory.

## S1 — Operations
`A`: simple and worker agents autonomously choose tools/actions for bounded tasks. Confidence: high.

## S2 — Coordination
`—`: the planner statically decomposes and sequences worker tasks; workers do not mutually regulate shared constraints or interference. Generated workflow primitives likewise require application-defined coordination. The shallow `S2=C` interpretation is removed.

## S3 — Inside-and-now control
`—`: the planner owns a current task plan and worker selection, but lacks the persistent whole-system progress/resource/commitment regulation, feedback-based reassignment or replanning required for S3.

## S3* — Complementary audit
`—`: no separate independent complementary audit channel over operational work was established.

## S4 — Outside-and-then intelligence
`—`: agent generation and training/practice can improve later behavior, but they are development/training mechanisms rather than a runtime prospective environmental-intelligence function governing adaptation. The shallow `S4=C` interpretation is removed.

## S5 — Policy and identity
`—`: generated prompts/configuration, worker roster and overall mission/policy remain externally framed.

## Recursion, variety, escalation
Youtu-Agent can generate and compose rich operational agents, but at the pinned runtime boundary S2–S5 remain application/development responsibilities.
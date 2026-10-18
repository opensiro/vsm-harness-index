---
harness_id: agentverse
project_name: AgentVerse
repository: https://github.com/OpenBMB/AgentVerse
review_ref: f90c4bd9680fdd3bcff8c52c9170911a59b23478
reviewed_at: 2026-09-15
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
last_checked_ref: f90c4bd9680fdd3bcff8c52c9170911a59b23478
last_checked_at: 2026-09-17
assessment_changed_at: 2026-09-15
last_reassessment_round: R2
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# AgentVerse

## Review boundary
AgentVerse at the pinned revision, covering its task-solving and simulation frameworks for multiple LLM agents.

## Repository architecture
AgentVerse has two relevant first-party structures. Simulation environments govern interaction among role agents through configurable order, visibility, selection, update and description rules. Task-solving environments run a fixed role-assignment → decision-making → execution → evaluation loop. Named manager/evaluator agents participate inside that task-solving pipeline.

## Primary evidence
- `agentverse/environments/simulation_env/basic.py`: each step asks the rule which agent(s) may act, generates per-agent environment descriptions, selects messages, updates memory and visible-agent sets, and advances the shared turn.
- `agentverse/environments/simulation_env/rules/order/sequential.py`: first-party sequential order implements round-robin speaking; the same rule family also exposes alternative order policies at the pinned tree.
- `agentverse/environments/tasksolving_env/basic.py`: the task-solving runtime performs expert recruitment, decision making, execution and evaluation on every round; evaluator advice is fed into later rounds and a configured score threshold ends the run.
- `agentverse/agents/tasksolving_agent/manager.py`: `ManagerAgent` selects among critic opinions; this is candidate/critique selection, not evidence of whole-system resource regulation.
- `agentverse/agents/tasksolving_agent/evaluator.py`: `EvaluatorAgent` scores/advises the current solution as part of the mandatory production loop.

## Operational model
Role agents are S1 units. The simulation rule system constrains turn-taking, visibility and shared interaction, directly regulating interference among multiple S1s. That is a genuine coordination function, but the concrete policy is selected/composed by the scenario rather than supplied as one autonomous default coordinator.

## S1 — Operations
`A`: role agents autonomously perform bounded task-solving or simulation actions in their local environment. Confidence: high.

## S2 — Coordination
`C`: first-party order/visibility/selection/update rules provide a real stabilizing channel among multiple role-agent S1s, including round-robin turn-taking and visibility management. The scenario chooses the rule/policy, so the coordination function is composable rather than a single agent-owned default. Confidence: high.

## S3 — Inside-and-now control
`—`: task-solving role assignment, manager critic selection, score thresholds and evaluator advice regulate the current task, but the inspected code does not give an actor a whole-system view plus authority over shared resources, commitments, budgets or constraints across autonomous S1s. The Profile explicitly excludes manager naming, task allocation and static workflow enforcement by themselves. Confidence: high.

## S3* — Complementary audit
`—`: the evaluator is a mandatory stage in the same task-solving production loop and consumes the routine solution/result state. It does not obtain materially different, sufficiently independent access to operational reality. Confidence: high.

## S4 — Outside-and-then intelligence
`—`: simulation environment descriptions and task feedback concern the current scenario. No inspected first-party loop models external/future change, develops adaptation options and couples them back into present S3 capability. Confidence: high.

## S5 — Policy and identity
`—`: role descriptions, prompts, scenario rules, score thresholds and task objectives are configured externally. No runtime actor holds legitimate ultimate identity/policy authority or closes S3–S4 tension. Confidence: high.

## Recursion, variety, escalation
Multiple role agents and shared environment rules are explicit, but task teams and simulations are not assumed recursively viable. The reviewed higher-level loop supplies coordination and task QA without metasystemic closure.
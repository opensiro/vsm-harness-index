---
harness_id: balrog
project_name: BALROG
repository: https://github.com/balrog-ai/BALROG
review_ref: b7afe79e3e4265811cfa985ed7c95c4d1a11e3f5
reviewed_at: 2026-10-18
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# BALROG

## Review boundary

- System in focus: BALROG's shipped **LLM/VLM game-playing agent operating cell**, as instantiated by the repository's first-party agent factory, one agent's observation/history → model-backed action → game-environment feedback loop, within the standard `eval.py` execution mode. This assessment is not a claim that the **benchmark institution** is an autonomous VSM organization.
- Purpose and identity: Produce actions in long-horizon interactive game episodes, using the chosen configured agent and model client, with environment feedback reaching later decisions; a benchmark evaluator runs and records the outcomes.
- Relevant environment: BabyAI, MiniHack/NetHack, Crafter, TextWorld and other shipped evaluation environment adapters; actions, observations, invalid-action corrections, terminal rewards, action history and optional researcher-curated ICL records.
- Standard-distribution boundary: `eval.py`, `balrog/agents/`, prompt/history builders, client interfaces, `balrog/evaluator.py`, environment adapters and configuration at the pinned ref. Only **the agent's operational decision path** is credited as agent organizational ownership. The benchmark manager is included for enactment/feedback evidence, not promoted into an independent agent executive/auditor.
- Credited operating / distribution surfaces: [eval.py](https://github.com/balrog-ai/BALROG/blob/b7afe79e3e4265811cfa985ed7c95c4d1a11e3f5/eval.py#L1); [balrog/agents/__init__.py](https://github.com/balrog-ai/BALROG/blob/b7afe79e3e4265811cfa985ed7c95c4d1a11e3f5/balrog/agents/__init__.py#L1); [balrog/agents/naive.py](https://github.com/balrog-ai/BALROG/blob/b7afe79e3e4265811cfa985ed7c95c4d1a11e3f5/balrog/agents/naive.py#L1); [balrog/agents/chain_of_thought.py](https://github.com/balrog-ai/BALROG/blob/b7afe79e3e4265811cfa985ed7c95c4d1a11e3f5/balrog/agents/chain_of_thought.py#L1); [balrog/agents/base.py](https://github.com/balrog-ai/BALROG/blob/b7afe79e3e4265811cfa985ed7c95c4d1a11e3f5/balrog/agents/base.py#L1); [balrog/evaluator.py](https://github.com/balrog-ai/BALROG/blob/b7afe79e3e4265811cfa985ed7c95c4d1a11e3f5/balrog/evaluator.py#L245); [balrog/config/config.yaml](https://github.com/balrog-ai/BALROG/blob/b7afe79e3e4265811cfa985ed7c95c4d1a11e3f5/balrog/config/config.yaml#L1).
- Adjacent first-party surfaces excluded from ownership: Benchmark leaderboard/publication, episode outcome aggregation and result files as external researcher evaluation, docs' illustrative custom-planning example, repository development/CI and human researcher/evaluator design. External provider/model weights and upstream game engines are not first-party decision owners.
- First-party operating / deployment modes considered: Default `agent.type=naive` with configured model client and history; optional `cot`, `robust_naive`, `robust_cot`, `few_shot`, and `custom` modes; sequential/parallel evaluation episodes. The illustrative `custom` template is not assumed to be an autonomous shipped strategy.
- Recursion level: A single game-playing operating cell/episode as the accountable S1 activity within the evaluation runtime. Independently run episodes/workers are replicas of the experiment, not automatically separate interacting S1 departments with common management.
- Reviewed revision: `b7afe79e3e4265811cfa985ed7c95c4d1a11e3f5` (GitHub repository ID 891746957), frozen in [game/strategy intake #1710](https://github.com/opensiro/vsm-harness-index/issues/1710).
- Observation date: 2026-10-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

BALROG supplies `AgentFactory.create_agent()` selecting a first-party agent class and model client from Hydra config. `NaiveAgent.act()` appends the previous action and new observation to the prompt history, asks its configured LLM client for the next action, then extracts the result. `ChainOfThoughtAgent` adds a reasoning instruction but still returns one discrete chosen action. `Evaluator.run_episode()` creates/reset the game environment and agent, invokes `agent.act()`, checks action validity, executes `env.step(action)`, and returns new observations/rewards/done feedback on the next step. The invalid-action case adds explicit corrective feedback to the following observation. [balrog/agents/__init__.py](https://github.com/balrog-ai/BALROG/blob/b7afe79e3e4265811cfa985ed7c95c4d1a11e3f5/balrog/agents/__init__.py#L1); [balrog/agents/naive.py](https://github.com/balrog-ai/BALROG/blob/b7afe79e3e4265811cfa985ed7c95c4d1a11e3f5/balrog/agents/naive.py#L1); [balrog/agents/chain_of_thought.py](https://github.com/balrog-ai/BALROG/blob/b7afe79e3e4265811cfa985ed7c95c4d1a11e3f5/balrog/agents/chain_of_thought.py#L1); [balrog/evaluator.py](https://github.com/balrog-ai/BALROG/blob/b7afe79e3e4265811cfa985ed7c95c4d1a11e3f5/balrog/evaluator.py#L245).

`EvaluatorManager` enumerates configured tasks/episodes, optionally dispatches them among multiprocessing workers, resumes by skipping saved completed runs, and saves outputs and summaries. These operations are evaluation infrastructure and deterministic/configured support. A log, queue, episode score, worker slot or summary does not establish S2/S3/S3*. [eval.py](https://github.com/balrog-ai/BALROG/blob/b7afe79e3e4265811cfa985ed7c95c4d1a11e3f5/eval.py#L1); [balrog/evaluator.py](https://github.com/balrog-ai/BALROG/blob/b7afe79e3e4265811cfa985ed7c95c4d1a11e3f5/balrog/evaluator.py#L245); [balrog/config/config.yaml](https://github.com/balrog-ai/BALROG/blob/b7afe79e3e4265811cfa985ed7c95c4d1a11e3f5/balrog/config/config.yaml#L1).

Optional `FewShotAgent` receives preexisting demonstration episodes from configured filesystem datasets; `InContextDataset` loads and shuffles recorded traces into a bounded ICL prompt. This is an optional prompting/conditioning path rather than an agent-owned, future-facing search → option → authorization/adoption → changed later capability loop. No automatic across-episode model/prompt/policy improvement is inferred from the existence of saved trajectories. [balrog/agents/few_shot.py](https://github.com/balrog-ai/BALROG/blob/b7afe79e3e4265811cfa985ed7c95c4d1a11e3f5/balrog/agents/few_shot.py#L1); [balrog/dataset.py](https://github.com/balrog-ai/BALROG/blob/b7afe79e3e4265811cfa985ed7c95c4d1a11e3f5/balrog/dataset.py#L1); [balrog/evaluator.py](https://github.com/balrog-ai/BALROG/blob/b7afe79e3e4265811cfa985ed7c95c4d1a11e3f5/balrog/evaluator.py#L245).

Supported Python/Docker entrypoints and configured API/vLLM clients are external inference/hosting and are not autonomous organizational functions of their own. Researchers choose model, task roster, number of workers, agent mode and episode limits through configuration. No executed model-based or benchmark performance run was performed in this OpenSiro source review. [balrog/config/config.yaml](https://github.com/balrog-ai/BALROG/blob/b7afe79e3e4265811cfa985ed7c95c4d1a11e3f5/balrog/config/config.yaml#L1); [eval.py](https://github.com/balrog-ai/BALROG/blob/b7afe79e3e4265811cfa985ed7c95c4d1a11e3f5/eval.py#L1).

## Operational model

The one accountable operational activity is model-selected action in a live game state. Its feedback closure is the next game observation after the chosen action, including environment validity feedback; the first-party wrapper and configured model together implement S1 at the declared game-playing boundary. The parallel episode runner does not create an evidenced organism of multiple interdependent S1 divisions. There is no supported shipped loop in this boundary for whole-system current management, independently corrective organizational audit, future-oriented capability adaptation or ultimate organizational identity/policy decisions.

## S1 — Operations

- State: A
- Function: Decide and enact the next game action in an interactive episode, conditioned on observations and previous actions.
- Disturbance / variety regulated: Changing mission/world state, partial observation, invalid/ineffective actions, terminal conditions and long-horizon task uncertainty.
- Decisive decision or feedback right: The model-backed first-party agent selects the action returned by `act()`; the evaluator routes the validated action to the game and exposes the resulting next observation/reward.
- Decision owner: The configured agent/model acting through the shipped `AgentFactory` and `NaiveAgent` / other real shipped agent modes. The external LLM supplies cognition to this wired first-party operating path, not independent higher-recursion control.
- Supporting / enforcement mechanisms: Prompt/history builders, model API client/retries, evaluator episode iterator, environment action validator, save/logging and terminal-step limits.
- Closure path: Observation + history → model-backed `act()` → extracted game action → environment validity check and `step()` → new observation/invalid-action feedback → subsequent `act()`.
- Boundary reachability: The public `python eval.py agent.type=naive ...` command wires `AgentFactory` into `EvaluatorManager.run()`, which calls `Evaluator.run_episode()` and the first-party `act()` method for each step. Model inference is externally provided but the action/feedback path is standard packaged functionality, not a sample-only diagram.
- Why this is / is not agent-owned: In supported model-backed modes the next action is selected on current observation/context by the agent's configured inference; deterministic evaluator logic enforces the action interface and reports world state but does not select the substantive action.
- Evidence: [eval.py](https://github.com/balrog-ai/BALROG/blob/b7afe79e3e4265811cfa985ed7c95c4d1a11e3f5/eval.py#L1); [balrog/agents/__init__.py](https://github.com/balrog-ai/BALROG/blob/b7afe79e3e4265811cfa985ed7c95c4d1a11e3f5/balrog/agents/__init__.py#L1); [balrog/agents/naive.py](https://github.com/balrog-ai/BALROG/blob/b7afe79e3e4265811cfa985ed7c95c4d1a11e3f5/balrog/agents/naive.py#L1); [balrog/agents/chain_of_thought.py](https://github.com/balrog-ai/BALROG/blob/b7afe79e3e4265811cfa985ed7c95c4d1a11e3f5/balrog/agents/chain_of_thought.py#L1); [balrog/evaluator.py](https://github.com/balrog-ai/BALROG/blob/b7afe79e3e4265811cfa985ed7c95c4d1a11e3f5/balrog/evaluator.py#L245); [balrog/config/config.yaml](https://github.com/balrog-ai/BALROG/blob/b7afe79e3e4265811cfa985ed7c95c4d1a11e3f5/balrog/config/config.yaml#L1).
- Basis: Explicit source control/feedback loop with configurable model-backed agent choice.
- Confidence: High for shipped structural mode, not an experimental success-rate claim.
- Caveats: `dummy`/illustrative demo or absent/nonfunctional external model does not by itself prove active agent ownership. This positive is for supported configured model-backed play, not benchmark orchestration.

## S2 — Coordination

- State: —
- Function: No evidenced first-party regulation of interference among distinct independently viable game-playing S1 units.
- Disturbance / variety regulated: Parallel episode workloads may share CPU/API budget or output directories, but the benchmark's partitioned tasks, worker queue and result aggregation do not demonstrate oscillatory inter-S1 conflict and adaptive damping into participating agents.
- Decisive decision or feedback right: Multiprocessing queues and `num_workers` dispatch episodes according to preset researcher configuration; no separate coordination actor judges specific inter-S1 conflicts and returns corrective constraints.
- Decision owner: EvaluatorManager deterministic scheduling/configured worker count, not an autonomous S2 agent.
- Supporting / enforcement mechanisms: Task queues, results queue, episode identity, file paths and progress logging.
- Closure path: Episode jobs run and results return to the evaluator, not an inter-agent interference → coordination decision → changed later behavior loop.
- Why this is / is not agent-owned: Multiple benchmark episodes/workers are evaluation replicas, not the autonomous operational divisions whose interference S2 would regulate.
- Evidence: [balrog/evaluator.py](https://github.com/balrog-ai/BALROG/blob/b7afe79e3e4265811cfa985ed7c95c4d1a11e3f5/balrog/evaluator.py#L245); [eval.py](https://github.com/balrog-ai/BALROG/blob/b7afe79e3e4265811cfa985ed7c95c4d1a11e3f5/eval.py#L1); [balrog/config/config.yaml](https://github.com/balrog-ai/BALROG/blob/b7afe79e3e4265811cfa985ed7c95c4d1a11e3f5/balrog/config/config.yaml#L1).
- Basis: Bounded absence after inspecting shipped episode scheduler and first-party agent paths.
- Confidence: High at the declared boundary.
- Caveats: An external multi-agent gaming organization would require a separate assessment.

### Absence scope

- Surfaces inspected: Agent factory/default and alternative agents, evaluator sequential/parallel execution and queue, config for workers/environments/tasks.
- Plausible first-party paths checked: Concurrent episode contention, worker queue, shared results and output management, few-shot loading.
- Why no material first-party path remains: These are fixed evaluation controls and independent episodes, with no specific inter-S1 disturbance judgment and behavioral stabilization returned to competing S1 units.

## S3 — Inside-and-now control

- State: —
- Function: No whole-game-playing-organization current-control loop is established at the declared agent recursion.
- Disturbance / variety regulated: Resource contention, stop conditions, task mix and experiment scheduling remain parameters of the external evaluator/researcher rather than operational decisions of an agent-owned whole-current executive.
- Decisive decision or feedback right: The researcher configures workers, episodes, tasks, model; the evaluator deterministically executes, records and stops episodes. The agent chooses local game moves but not whole-system resource/commitment allocations.
- Decision owner: Experiment configuration and scripted evaluator, outside credited S3 ownership.
- Supporting / enforcement mechanisms: Hydra config, fixed limits, worker scheduler, saved run state and episode termination.
- Closure path: No sensed whole-system current condition → legitimate S3 resource/intervention decision → returned operational adjustments.
- Why this is / is not agent-owned: Having centralized visibility of benchmark progress or a maximum episode length is not S3 decisive authority.
- Evidence: [balrog/evaluator.py](https://github.com/balrog-ai/BALROG/blob/b7afe79e3e4265811cfa985ed7c95c4d1a11e3f5/balrog/evaluator.py#L245); [balrog/config/config.yaml](https://github.com/balrog-ai/BALROG/blob/b7afe79e3e4265811cfa985ed7c95c4d1a11e3f5/balrog/config/config.yaml#L1); [eval.py](https://github.com/balrog-ai/BALROG/blob/b7afe79e3e4265811cfa985ed7c95c4d1a11e3f5/eval.py#L1).
- Basis: Bounded negative for agent operating recursion.
- Confidence: High for shipped modes.
- Caveats: Researcher administration of benchmark infrastructure is not the assessed agent's first-party S3 parent mode.

### Absence scope

- Surfaces inspected: `eval.py`, manager/worker/episode lifecycle, current-state config, agent wrappers.
- Plausible first-party paths checked: Worker count, task schedule, completion/resume rules, episode limits and action validity.
- Why no material first-party path remains: Controls are preset or mechanical and do not provide a first-party whole-current discretionary owner with authority and returned regulation.

## S3* — Complementary audit

- State: —
- Function: No independently corrective organizational audit with a return path into this agent cell is established.
- Disturbance / variety regulated: Evaluator sees rewards, episode failures and action validity; these observations document task performance but do not constitute an auditor independently checking organizational claims and changing later operating regulation.
- Decisive decision or feedback right: Environment validity correction is part of the ordinary game action loop; offline recorded scores/statistics are not independently owned audit judgments with corrective operational closure.
- Decision owner: Environment rules and evaluator recordkeeping, not a separate autonomous complementary auditor.
- Supporting / enforcement mechanisms: Episode CSV/JSON logs, scoring, invalid-action string feedback and summary table.
- Closure path: No complementary independent inspection → audit verdict → accountable agent/controller corrective response. Environment observation feedback belongs to S1.
- Why this is / is not agent-owned: Recording a score, parsing validity or writing telemetry is not an organizational audit with independent judgment and corrective authority.
- Evidence: [balrog/evaluator.py](https://github.com/balrog-ai/BALROG/blob/b7afe79e3e4265811cfa985ed7c95c4d1a11e3f5/balrog/evaluator.py#L245); [eval.py](https://github.com/balrog-ai/BALROG/blob/b7afe79e3e4265811cfa985ed7c95c4d1a11e3f5/eval.py#L1); [balrog/config/config.yaml](https://github.com/balrog-ai/BALROG/blob/b7afe79e3e4265811cfa985ed7c95c4d1a11e3f5/balrog/config/config.yaml#L1).
- Basis: Bounded negative after checking scoring, feedback and agent integration.
- Confidence: Medium-high; only code-level evidence, no runtime attestation.
- Caveats: External research audit of model behavior is outside this game-playing agent boundary.

### Absence scope

- Surfaces inspected: Episode scoring/logging, invalid-action feedback, model agent interface, factory, evaluator result collection.
- Plausible first-party paths checked: Environment action validity, episode success metrics, failed task/resume information and researcher-visible summary.
- Why no material first-party path remains: The only corrective path is ordinary per-action environment feedback, while other evaluation findings are logged/aggregated without an independent corrective agent/audit return.

## S4 — Outside-and-then intelligence

- State: —
- Function: No first-party external-prospective scan/option/selection/adoption loop updates future game-playing capability at the stated boundary.
- Disturbance / variety regulated: Unseen future games may expose policy deficiencies, but the shipped first-party loop reacts inside each episode, while future policy/prompt changes belong to external authors or prepared demonstrations.
- Decisive decision or feedback right: Fixed operator-set `agent.type` and ICL dataset determine which preexisting behavior scaffold is used; the game-playing agent does not decide to modify its own later operating capability based on future/environmental opportunity assessments.
- Decision owner: Researcher/author supplies prompt, sample records, client and benchmark settings; first-party code loads them.
- Supporting / enforcement mechanisms: History buffering, optional CoT, few-shot replay, demonstration selection and caching.
- Closure path: Past fixed episodes may be inserted into a current prompt, but no observed external trend → proposed future adaptation → adopted persistent capability change → return into later operations is shown.
- Why this is / is not agent-owned: Memory, in-episode plan refinement and preloaded demonstrations do not alone confer S4 organizational adaptation ownership.
- Evidence: [balrog/agents/few_shot.py](https://github.com/balrog-ai/BALROG/blob/b7afe79e3e4265811cfa985ed7c95c4d1a11e3f5/balrog/agents/few_shot.py#L1); [balrog/dataset.py](https://github.com/balrog-ai/BALROG/blob/b7afe79e3e4265811cfa985ed7c95c4d1a11e3f5/balrog/dataset.py#L1); [balrog/agents/chain_of_thought.py](https://github.com/balrog-ai/BALROG/blob/b7afe79e3e4265811cfa985ed7c95c4d1a11e3f5/balrog/agents/chain_of_thought.py#L1); [balrog/evaluator.py](https://github.com/balrog-ai/BALROG/blob/b7afe79e3e4265811cfa985ed7c95c4d1a11e3f5/balrog/evaluator.py#L245); [balrog/config/config.yaml](https://github.com/balrog-ai/BALROG/blob/b7afe79e3e4265811cfa985ed7c95c4d1a11e3f5/balrog/config/config.yaml#L1).
- Basis: Bounded source negative; specifically checked the shipped optional ICL mode.
- Confidence: Medium-high at the declared boundary.
- Caveats: A separately built online-learning controller using BALROG evaluation output would be a different system-in-focus.

### Absence scope

- Surfaces inspected: Agent modes, `few_shot.py`, `dataset.py`, evaluator episode lifecycle, configuration, optional CoT path.
- Plausible first-party paths checked: Inter-turn histories, reasoning carryover, ICL trajectory ingestion, saved rewards/logs and user-defined custom planning agent.
- Why no material first-party path remains: First-party code replays selected existing examples and keeps local context; no shipped agent-owned prospective option-and-adoption loop changes later game-playing capabilities.

## S5 — Policy and identity

- State: —
- Function: No first-party autonomous or operationally closed parent identity/ultimate-policy function for the game-playing organization.
- Disturbance / variety regulated: Which environments, model/providers, prompts, eval goals and stopping rules define the experiment is set by upstream config/researchers outside an assessed runtime identity/policy-return organ.
- Decisive decision or feedback right: Evaluated agent receives its configured role/task; its moves do not decide the identity/purpose or ultimate policy of the whole organization.
- Decision owner: Researcher/maintainer/operator configures purpose and authority; no live first-party legitimate S5 decision/return process is established.
- Supporting / enforcement mechanisms: Hydra config, static prompt instructions, environment mission and terminal control.
- Closure path: No runtime identity/ultimate-policy case → legitimate authority → policy decision → return to subsequent game-playing operation; static startup settings alone do not provide a qualifying parent mode.
- Why this is / is not agent-owned: Constraints and instructions limit S1 actions without a first-party S5 governance loop.
- Evidence: [balrog/config/config.yaml](https://github.com/balrog-ai/BALROG/blob/b7afe79e3e4265811cfa985ed7c95c4d1a11e3f5/balrog/config/config.yaml#L1); [eval.py](https://github.com/balrog-ai/BALROG/blob/b7afe79e3e4265811cfa985ed7c95c4d1a11e3f5/eval.py#L1); [balrog/agents/__init__.py](https://github.com/balrog-ai/BALROG/blob/b7afe79e3e4265811cfa985ed7c95c4d1a11e3f5/balrog/agents/__init__.py#L1); [balrog/agents/naive.py](https://github.com/balrog-ai/BALROG/blob/b7afe79e3e4265811cfa985ed7c95c4d1a11e3f5/balrog/agents/naive.py#L1).
- Basis: Bounded negative at the declared standard distribution.
- Confidence: High for reviewed runtime, without external governance inference.
- Caveats: Repository maintainers and external organizations may exercise policy rights over experiments but are not shipped parent closure of the assessed agent.

### Absence scope

- Surfaces inspected: Shipped configuration, startup wiring, agent prompts/factory, benchmark scripts and documented operating mode.
- Plausible first-party paths checked: Configured model/environment selection, static game instructions, supervisor operator control and research benchmark governance.
- Why no material first-party path remains: Decisions are exogenous static setup/research choices and lack first-party run-time legitimate ultimate-policy adjudication returned to this agent cell.

## Recursion

Each configured game-playing agent/episode is an operational unit inside a benchmark experiment. The experiment/evaluator is a surrounding observation and scheduling context. Its workers and external researcher institution are not automatically a higher VSM recursion with closed agent S3/S3*/S4/S5. The assessment does not project this bounded vector onto a production game platform or upstream model vendor.

## Variety and escalation

Game-state complexity and invalid action variety return through observations/prompt history into S1 action choice. End-of-episode reward and logs return to the *research evaluator* as measurements. Unexpected model-client failures, absent demo files and game compatibility are run/error disturbances, not evidence of internal S2/S3 or an algedonic organization-level channel. Tool/configuration ownership remains outside claimed higher-level autonomy.

## Evidence gaps

- No live model-backed rollout, performance benchmark or experimental comparison was run; positive S1 evidence is structural source reachability.
- External provider reasoning, black-box training, adaptation or policy decisions are not first-party shipped BALROG decisions.
- No evidence currently shows a first-party benchmark-feedback-to-agent prospective improvement loop, multi-S1 interference control, independent corrective organizational audit or authoritative S5 parent mode. Reassess only if new source-specific in-boundary path is demonstrated.
- This is a **proposed**, not admitted canonical assessment. Run released Methodology 0.3.7 structural checker, Index preflight, generated-view/provenance checks, exact-head CI and separate canonical admission before treating any vector as corpus fact.

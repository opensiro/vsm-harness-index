---
harness_id: babyai
project_name: BabyAI
repository: https://github.com/mila-iqia/babyai
review_ref: 65fb0cb6f816532a65014bf034a758244e2d5ae7
reviewed_at: 2026-10-18
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# BabyAI

## Review boundary

- System in focus: The frozen historical BabyAI 1.1 **agent training-and-evaluation toolkit** with its supported learned-policy `ModelAgent` game-playing mode, demonstration/bot agent modes, gym-compatible interactive environments, and training/evaluation scripts. This is the historical `mila-iqia/babyai` repository, **not** the current `Farama-Foundation/Minigrid` environment library.
- Purpose and identity: Research grounded language learning and sample efficiency by training or evaluating an agent that acts in interactive BabyAI instruction-following environments, with observations, rewards and done feedback.
- Relevant environment: Historical OpenAI Gym / gym-minigrid / BabyAI levels and tasks; PyTorch learned policies or rule-based demonstration bot; researcher-provided training settings, checkpoints and evaluation runs.
- Standard-distribution boundary: Versioned `babyai.utils.agent.ModelAgent` and `BotAgent`, `babyai.evaluate`, `scripts/train_rl.py`, `scripts/train_il.py`, `scripts/evaluate.py`, associated model/preprocessing/bot code. The environment and evaluator are included for observing the operational feedback and training boundaries, but external scientific leadership, future model deployment and repository maintainer authority are not first-party runtime organizational owners.
- Credited operating / distribution surfaces: [babyai/utils/agent.py](https://github.com/mila-iqia/babyai/blob/65fb0cb6f816532a65014bf034a758244e2d5ae7/babyai/utils/agent.py#L9); [babyai/evaluate.py](https://github.com/mila-iqia/babyai/blob/65fb0cb6f816532a65014bf034a758244e2d5ae7/babyai/evaluate.py#L7); [scripts/evaluate.py](https://github.com/mila-iqia/babyai/blob/65fb0cb6f816532a65014bf034a758244e2d5ae7/scripts/evaluate.py#L1); [scripts/train_rl.py](https://github.com/mila-iqia/babyai/blob/65fb0cb6f816532a65014bf034a758244e2d5ae7/scripts/train_rl.py#L177); [scripts/train_il.py](https://github.com/mila-iqia/babyai/blob/65fb0cb6f816532a65014bf034a758244e2d5ae7/scripts/train_il.py#L1); [babyai/bot.py](https://github.com/mila-iqia/babyai/blob/65fb0cb6f816532a65014bf034a758244e2d5ae7/babyai/bot.py#L1); [scripts/README.md](https://github.com/mila-iqia/babyai/blob/65fb0cb6f816532a65014bf034a758244e2d5ae7/scripts/README.md#L1); [setup.py](https://github.com/mila-iqia/babyai/blob/65fb0cb6f816532a65014bf034a758244e2d5ae7/setup.py#L1).
- Adjacent first-party surfaces excluded from ownership: Research papers/benchmarks, illustrative levels and test utilities, plot/analysis scripts, contributor governance and externally operated study/cluster infrastructure. Current Farama Minigrid is a separate repository, **not** imported into the frozen legacy distribution.
- First-party operating / deployment modes considered: Learned `ModelAgent` loaded from trained checkpoint; Gym game interaction in `evaluate` / `batch_evaluate`; rule-based `BotAgent` using `Bot.replan()`; demonstration playback; offline imitation learning and PPO training scripts. The trained-policy mode requires a compatible pre-existing model/checkpoint and historical dependency stack.
- Recursion level: Game-playing agent as S1 operational cell; same repository offers offline training/evaluation support but does not automatically constitute an autonomous organization of coordinated departments.
- Reviewed revision: `65fb0cb6f816532a65014bf034a758244e2d5ae7` (GitHub repository ID 151299234), frozen in [game/strategy intake #1710](https://github.com/opensiro/vsm-harness-index/issues/1710).
- Observation date: 2026-10-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The historical BabyAI codebase packages model inference, RL/PPO and imitation-learning training routines, demonstration generation, a rule-based planner and scripts for evaluating policy-driven agents. `ModelAgent` selects an action from the PyTorch actor distribution (sampling or argmax), keeps recurrent policy memory across successive game observations and handles end-of-episode memory reset in `analyze_feedback`. `BotAgent` wraps the historical `Bot.replan` action selector for expert demonstration/evaluation. `load_agent` chooses the configured model, bot or demonstration-based mode. [babyai/utils/agent.py](https://github.com/mila-iqia/babyai/blob/65fb0cb6f816532a65014bf034a758244e2d5ae7/babyai/utils/agent.py#L9); [babyai/bot.py](https://github.com/mila-iqia/babyai/blob/65fb0cb6f816532a65014bf034a758244e2d5ae7/babyai/bot.py#L1).

`babyai.evaluate.evaluate` repeatedly calls `agent.act(obs)`, applies `env.step(action)`, and passes rewards/done to `agent.analyze_feedback`; this returns operating feedback inside each game episode. The `scripts/evaluate.py` CLI initializes the appropriate agent and dispatches model/bot/demonstration evaluations. [babyai/evaluate.py](https://github.com/mila-iqia/babyai/blob/65fb0cb6f816532a65014bf034a758244e2d5ae7/babyai/evaluate.py#L7); [scripts/evaluate.py](https://github.com/mila-iqia/babyai/blob/65fb0cb6f816532a65014bf034a758244e2d5ae7/scripts/evaluate.py#L1).

Separately, `scripts/train_rl.py` builds several Gym environments, an actor-critic model and a PPO optimizer, loops over `algo.update_parameters()`, writes checkpoints/logs, runs held-out validation at save intervals, and persists a `_best` checkpoint according to success rate and mean return. `scripts/train_il.py` implements training from externally supplied demonstrations. These represent real machine-learning optimization/selection processes, but a training checkpoint mechanism does not by itself establish VSM S4 outside-and-then organizational adaptation; the prospective adaptation owner, environmental scan and operational adoption boundary must be established separately. [scripts/train_rl.py](https://github.com/mila-iqia/babyai/blob/65fb0cb6f816532a65014bf034a758244e2d5ae7/scripts/train_rl.py#L177); [scripts/train_il.py](https://github.com/mila-iqia/babyai/blob/65fb0cb6f816532a65014bf034a758244e2d5ae7/scripts/train_il.py#L1); [scripts/README.md](https://github.com/mila-iqia/babyai/blob/65fb0cb6f816532a65014bf034a758244e2d5ae7/scripts/README.md#L1).

The 2023 upstream README states the historic repository is **not actively maintained**, says BabyAI environments have moved to modern Minigrid, and warns these scripts may require adaptation to that new library. This is a pinned historical source assessment **only**; no current-environment runtime compatibility or reproducible trained-model evaluation is asserted. [README.md](https://github.com/mila-iqia/babyai/blob/65fb0cb6f816532a65014bf034a758244e2d5ae7/README.md#L1); [setup.py](https://github.com/mila-iqia/babyai/blob/65fb0cb6f816532a65014bf034a758244e2d5ae7/setup.py#L1).

## Operational model

The learned-policy agent independently selects actions in an instruction-following world. Its S1 feedback loop is observation → policy inference → action → reward/next observation, with recurrent memory and done-state handling. The trainer, evaluator, multi-environment runner and offline model selection are surrounding execution/learning infrastructure. At this declared recursion none is automatically another first-party operational division, an agent-owned whole-current manager, or an independently corrective organization auditor.

## S1 — Operations

- State: A
- Function: Use a learned-policy agent (or supported rule-based bot mode) to select and enact next actions under ongoing partially observed game instructions.
- Disturbance / variety regulated: New local game observations, task-specific instructions, unseen objects, movement/interaction consequences, rewards, environment terminal conditions and recurrent state.
- Decisive decision or feedback right: `ModelAgent.act_batch` applies the configured neural policy to current observations and policy memory, samples/chooses from action distribution; environment advances under that choice and returns observations/rewards.
- Decision owner: First-party `ModelAgent` with its configured trained PyTorch policy. The independent bot demonstration mode selects actions by deterministic search/replanning, but does not supply an unrelated executive for the model mode.
- Supporting / enforcement mechanisms: Gym environments, preprocessing, recurrent state storage/reset, `evaluate` loop, CLI settings, episode counters, model file/checkpoint loader.
- Closure path: Instruction and game observation → policy forward pass/action distribution → agent action selection → `env.step` → next game observation/reward/done → subsequent `act()` and memory adjustment.
- Boundary reachability: Packaged `scripts/evaluate.py` calls shipped `load_agent` to load `ModelAgent`; packaged `babyai.evaluate` then executes the observation-action-feedback loop. Historically supported trained checkpoint and gym-minigrid dependencies are required; no model cognition is borrowed from an external assessment or example-only contributor agent.
- Why this is / is not agent-owned: The next-game-action choice is computed by the loaded policy from current observation/memory rather than being selected manually by a researcher or by the environment's evaluator. The surrounding scripts supply the interface and feedback.
- Evidence: [babyai/utils/agent.py](https://github.com/mila-iqia/babyai/blob/65fb0cb6f816532a65014bf034a758244e2d5ae7/babyai/utils/agent.py#L9); [babyai/evaluate.py](https://github.com/mila-iqia/babyai/blob/65fb0cb6f816532a65014bf034a758244e2d5ae7/babyai/evaluate.py#L7); [scripts/evaluate.py](https://github.com/mila-iqia/babyai/blob/65fb0cb6f816532a65014bf034a758244e2d5ae7/scripts/evaluate.py#L1); [scripts/README.md](https://github.com/mila-iqia/babyai/blob/65fb0cb6f816532a65014bf034a758244e2d5ae7/scripts/README.md#L1).
- Basis: Explicit source, feedback and supported CLI mode.
- Confidence: High for historical source-defined operation; no execution or historical-model artifact was verified in this review.
- Caveats: No inference run under modern Minigrid is claimed. The rule-based bot is not confused with multi-agent organizational management.

## S2 — Coordination

- State: —
- Function: No established inter-S1 coordination loop damping an identified disturbance between distinct autonomous organizational operating units.
- Disturbance / variety regulated: Multiple sampled environments and policy rollout workers are parallel training/evaluation processes, not independent divisions evidencing mutual interference.
- Decisive decision or feedback right: Script presets `--procs`, environment seed roster and PPO batch algorithms; no observed coordination owner corrects inter-agent operational conflict.
- Decision owner: Fixed algorithm and researcher setup; not a distinct S2 agent.
- Supporting / enforcement mechanisms: Gym environment batches, PPO collection, seed choices, trajectory aggregation and saved evaluations.
- Closure path: Runner collects experiences and updates a policy; this is data-parallel optimization, not an interference → inter-S1 coordination decision → stabilized subsequent participating S1 operation path.
- Why this is / is not agent-owned: Parallel copies of a learning episode are not independently viable organizational S1 units whose conflict is regulated.
- Evidence: [scripts/train_rl.py](https://github.com/mila-iqia/babyai/blob/65fb0cb6f816532a65014bf034a758244e2d5ae7/scripts/train_rl.py#L177); [babyai/evaluate.py](https://github.com/mila-iqia/babyai/blob/65fb0cb6f816532a65014bf034a758244e2d5ae7/babyai/evaluate.py#L7); [scripts/README.md](https://github.com/mila-iqia/babyai/blob/65fb0cb6f816532a65014bf034a758244e2d5ae7/scripts/README.md#L1).
- Basis: Source-bounded negative for the declared agent/task recursion.
- Confidence: High for examined historical scripts.
- Caveats: A later distributed-game platform with shared operations would require its own evidence.

### Absence scope

- Surfaces inspected: Model/bot agents, parallel rollout and evaluator code, documented RL/IL scripts, trainer environment construction.
- Plausible first-party paths checked: Parallel policy training actors, per-environment state, shared PPO optimizer and statistical aggregation.
- Why no material first-party path remains: The paths are learning-data collection and algorithmic batching, not the function-specific damping and returned regulation of concrete interference between distinct S1 organizations.

## S3 — Inside-and-now control

- State: —
- Function: No first-party whole-current management/authority loop over commitments, resources or operating divisions is established.
- Disturbance / variety regulated: Training runtime limits, validation intervals and policy optimization are experiment-specific settings and optimizer logic, not organization-wide current management.
- Decisive decision or feedback right: Script/CLI sets training configuration; PPO updates weights by fixed optimizer; none autonomously chooses whole-system current resource/priority intervention.
- Decision owner: Researcher-supplied algorithm/configuration and deterministic training loop, not a first-party agent S3 executive.
- Supporting / enforcement mechanisms: Frame limits, iterations, logger, checkpoint intervals, optimizer and save/validation procedures.
- Closure path: No whole-system current view → discretionary S3 intervention → changed multi-S1 operations loop in shipped system.
- Why this is / is not agent-owned: Offline optimizer and multi-env evaluation machinery do not own whole-current organizational discretion.
- Evidence: [scripts/train_rl.py](https://github.com/mila-iqia/babyai/blob/65fb0cb6f816532a65014bf034a758244e2d5ae7/scripts/train_rl.py#L177); [babyai/evaluate.py](https://github.com/mila-iqia/babyai/blob/65fb0cb6f816532a65014bf034a758244e2d5ae7/babyai/evaluate.py#L7); [scripts/README.md](https://github.com/mila-iqia/babyai/blob/65fb0cb6f816532a65014bf034a758244e2d5ae7/scripts/README.md#L1).
- Basis: Bounded negative within historical standard operating modes.
- Confidence: Medium-high.
- Caveats: Institution/operator research supervision is outside the claimed agent organization boundary.

### Absence scope

- Surfaces inspected: RL/IL training setup and loops, model evaluator, experiment arguments, model-selection path.
- Plausible first-party paths checked: PPO checkpoint scheduler, early validation, resource configuration and multi-env episode control.
- Why no material first-party path remains: These implement predetermined experiment policy, not whole-organization discretionary operational regulation with agent or legitimate parent closure.

## S3* — Complementary audit

- State: —
- Function: No independently corrective organizational auditor with complementary access and an accountable operational correction return is established.
- Disturbance / variety regulated: Policy mistakes and poor episode return are measurable by validation, but result scoring or selection does not by itself establish independently judged audit of operational claims.
- Decisive decision or feedback right: `batch_evaluate` measures success and reward; `_best` checkpoint comparator deterministically saves a candidate on higher score. Neither makes independent corrective organizational audit judgments.
- Decision owner: Deterministic evaluator/researcher-selected metric, not autonomous complementary auditor.
- Supporting / enforcement mechanisms: Validation episodes, reward statistics, CSV logging, best-checkpoint threshold.
- Closure path: Training → evaluation → statistical checkpoint saving, without an independent operational-reality inspection → audit judgment → corrective returned organizational control.
- Why this is / is not agent-owned: Benchmark evaluation of a learned policy is not sufficient evidence of independent S3* organizational audit authority and closure.
- Evidence: [scripts/train_rl.py](https://github.com/mila-iqia/babyai/blob/65fb0cb6f816532a65014bf034a758244e2d5ae7/scripts/train_rl.py#L177); [babyai/evaluate.py](https://github.com/mila-iqia/babyai/blob/65fb0cb6f816532a65014bf034a758244e2d5ae7/babyai/evaluate.py#L7); [scripts/README.md](https://github.com/mila-iqia/babyai/blob/65fb0cb6f816532a65014bf034a758244e2d5ae7/scripts/README.md#L1).
- Basis: Bounded negative after examination of validation and checkpoint selection.
- Confidence: Medium-high.
- Caveats: External scientific replication/peer review is not part of this first-party runtime.

### Absence scope

- Surfaces inspected: Reward/validation routines, held-out episode testing, checkpoint selection and save/metrics code, agent feedback API.
- Plausible first-party paths checked: Independent held-out episode measurements, result comparison and model checkpoint adoption.
- Why no material first-party path remains: Held-out validation measures policy results; it has no separate audit owner independently detecting organization-reporting divergence and returning corrective operating decisions.

## S4 — Outside-and-then intelligence

- State: —
- Function: No separately closed first-party outside-and-then strategic adaptation of this game-playing agent's future operating capability was established in the pinned historical distribution. PPO/imitation learning can produce trained policy weights, but their researcher-specified optimization objective and manually selected deployment/evaluation are a training process, not an independently owned organizational S4 function.
- Disturbance / variety regulated: Encountering new BabyAI tasks and held-out environments motivates training and generalization; the shipped trainer optimizes a predefined reward/demonstration objective, rather than sensing a changing external future and selecting/adopting alternative viable organizational strategies.
- Decisive decision or feedback right: `scripts/train_rl.py` applies preconfigured PPO weight updates and saves `<model>_best` when deterministic success-rate/return thresholds improve. `scripts/evaluate.py` independently requires an operator-supplied `--model`; it does not consume a trainer-selected future strategy or automatically deploy the best checkpoint. `babyai/efficiency.py` passes an optional researcher-supplied `pretrained_model` to a generated training command, not an S4-owned environmental strategy choice.
- Decision owner: The researcher selects levels, reward function, hyperparameters, pretrained model, and subsequent evaluation/model invocation. The optimizer and checkpoint comparator mechanically enforce those choices; no distinct agentic or legitimate first-party parent S4 decision owner is wired into this operating boundary.
- Supporting / enforcement mechanisms: PPO and IL optimization, held-out validation, `_best` checkpoint file, model loader, training/evaluation scripts, optional pretrained-model argument, and research efficiency utilities.
- Closure path: Reward/demonstration → fixed optimizer → candidate weights/checkpoint → optional explicit researcher choice of model for a later run. No in-boundary outside/then signal → prospective organizational option decision → authorized adoption and returned operating capability loop is present.
- Why this is / is not agent-owned: The recurrent `ModelAgent` owns S1 gameplay decisions; learning from past training traces is not by itself a separate S4 owner. Removing the researcher-selected model/environment/training regimen leaves an optimizer without the discretionary future organizational adaptation decision.
- Evidence: [training source](https://github.com/mila-iqia/babyai/blob/65fb0cb6f816532a65014bf034a758244e2d5ae7/scripts/train_rl.py#L91); [checkpoint comparison](https://github.com/mila-iqia/babyai/blob/65fb0cb6f816532a65014bf034a758244e2d5ae7/scripts/train_rl.py#L232); [explicit model evaluation](https://github.com/mila-iqia/babyai/blob/65fb0cb6f816532a65014bf034a758244e2d5ae7/scripts/evaluate.py#L19); [efficiency pretrained-model path](https://github.com/mila-iqia/babyai/blob/65fb0cb6f816532a65014bf034a758244e2d5ae7/babyai/efficiency.py#L17); [research usage instructions](https://github.com/mila-iqia/babyai/blob/65fb0cb6f816532a65014bf034a758244e2d5ae7/scripts/README.md#L139); [operating agent](https://github.com/mila-iqia/babyai/blob/65fb0cb6f816532a65014bf034a758244e2d5ae7/babyai/utils/agent.py#L9).
- Basis: Bounded negative established through pinned code inspection of the trainer, checkpoint selection, explicit model loader/evaluation and project-level efficiency/pretraining orchestration; this resolves the proposed `?` without inventing an external strategic loop.
- Confidence: Medium-high for this historical first-party distribution; not a universal assertion that reinforcement learning systems cannot realize S4.
- Caveats: No historical dependency/inference execution, model success rate, modern MiniGrid compatibility or later unreviewed deployment is claimed.

### Absence scope

- Surfaces inspected: Pinned `scripts/train_rl.py`, `scripts/train_il.py`, `scripts/evaluate.py`, `scripts/README.md`, `babyai/efficiency.py`, `babyai/utils/agent.py`, and `babyai/evaluate.py`.
- Plausible first-party paths checked: PPO policy updates; periodic held-out success/return and `_best` saves; optional pretrained transfer/curriculum research scripts; subsequent explicit learned-policy evaluation; offline imitation from demonstrations.
- Why no material first-party path remains: Each candidate is fixed reward/model optimization, a deterministic checkpoint comparator, a researcher-parameterized launcher or an explicitly selected model run. None couples an environmental future-options function and a legitimate S4 adoption owner to a returned modification of subsequent autonomous operating organization.

## S5 — Policy and identity

- State: —
- Function: No shipped first-party identity/ultimate-policy authority and return-to-operations organ for the game-playing agent system.
- Disturbance / variety regulated: Mission selection, external reward definitions, hyperparameters and game rules are supplied by historical benchmark/researchers.
- Decisive decision or feedback right: Human researchers set goals, metrics, environment and policy/architecture; game agent chooses current actions but does not adjudicate organizational identity/ultimate policy.
- Decision owner: External maintainer/researcher config, not an operationally closed parent S5 of the assessed standard-distribution system.
- Supporting / enforcement mechanisms: Gym mission strings, checkpoint names, static experiment arguments, environment rules.
- Closure path: Static externally defined goals guide execution; no first-party identity dispute → legitimate parent authority → policy decision → return to subsequent governed operations.
- Why this is / is not agent-owned: Policy optimization and game-instruction following are not ultimate organization-level identity or governance decisions.
- Evidence: [babyai/utils/agent.py](https://github.com/mila-iqia/babyai/blob/65fb0cb6f816532a65014bf034a758244e2d5ae7/babyai/utils/agent.py#L9); [scripts/README.md](https://github.com/mila-iqia/babyai/blob/65fb0cb6f816532a65014bf034a758244e2d5ae7/scripts/README.md#L1); [setup.py](https://github.com/mila-iqia/babyai/blob/65fb0cb6f816532a65014bf034a758244e2d5ae7/setup.py#L1); [scripts/train_rl.py](https://github.com/mila-iqia/babyai/blob/65fb0cb6f816532a65014bf034a758244e2d5ae7/scripts/train_rl.py#L177).
- Basis: Source-bounded negative for reviewed shipped paths.
- Confidence: High at selected recursion.
- Caveats: University/research-project governance is adjacent and cannot be credited as a packaged runtime parent mode.

### Absence scope

- Surfaces inspected: Historical command-line scripts, policy agent/model, task/env configuration, documented research runtime, training and evaluation code.
- Plausible first-party paths checked: Game mission definition, researcher training choices, checkpoint policy, operator model deployment settings.
- Why no material first-party path remains: These are outside research/configuration constraints and no first-party runtime parent/agent ultimate-policy adjudication path returns a legitimate decision.

## Recursion

The learned game-playing agent is the autonomous S1 operating cell. Evaluator and trainer are support/optimization machinery in the frozen research toolkit. Neither multiple Gym environments nor nested neural-memory state proves a higher organizational recursion or inter-unit coordination. The current Farama MiniGrid library and research institution have their own boundaries and are not silently incorporated.

## Variety and escalation

Partial observation and environmental feedback change recurrent model state and later action selection. External training metrics and checkpoint selection can influence future policy artifacts, but no source-backed S4 organizational adaptation owner was established by this review. Model artifact failure, obsolete gym version and current compatibility issues are reproducibility risks, not algedonic organizational signals.

## Evidence gaps

- Historical repository is declared unmaintained (since 2023); **no claim of successful runtime execution or compatibility with 2026 Minigrid**, no model/checkpoint run and no measured game/learning results.
- The actual supported status and standard first-party packaging of historical `ModelAgent` are source-backed; a particular trained model must be supplied before inference.
- S4 bounded-negative adjudication (2026-10-19): frozen trainer, model-selection, evaluation, efficiency/pretraining and usage paths contain fixed optimization or researcher-selected continuation, not a separately owned prospective option→adoption→later-operation loop; see S4 absence scope. Historical external deployments remain outside the inspected boundary.
- Canonical inclusion requires separate exact-head CI, admission preflight and publication verification; this record makes no claim that source-only inspection reproduces historical trained-model runs.

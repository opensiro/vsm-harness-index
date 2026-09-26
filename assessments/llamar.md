---
harness_id: llamar
project_name: LLaMAR
repository: https://github.com/nsidn98/LLaMAR
review_ref: d2b74cac79a0f070d87a150712f8e2ae174920be
reviewed_at: 2026-09-26
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-26
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# LLaMAR

## Review boundary

- System in focus: one first-party LLaMAR multi-robot episode at pinned revision `d2b74cac79a0f070d87a150712f8e2ae174920be`, with the runnable AI2-THOR/SAR LLaMAR baseline, shared multi-agent environment state, model-driven planner/action/verifier cycle and embodied robot action streams inside the boundary.
- Purpose and identity: coordinate multiple embodied robots to complete a shared long-horizon task through joint planning, per-robot actions, result-conditioned correction and repeated whole-team replanning.
- Relevant environment: user-selected task/scene; AI2-THOR or SAR environment; physical/spatial object state; model provider; external simulator/runtime dependencies.
- Standard-distribution boundary: the first-party `AI2Thor/baselines/llamar/` and `SAR/baselines/llamar*` runnable paths together with the repository's environment adapters and shared state needed by those paths. External model service and simulator implementation remain environment/dependencies.
- Credited operating / distribution surfaces: `AI2Thor/baselines/llamar/llamar.py`; `AI2Thor/baselines/llamar/llamar_utils_multiagent.py`; `AI2Thor/env_new.py`; `SAR/baselines/llamar.py`; `SAR/baselines/llamar_utils_multiagent.py`; and the documented LLaMAR run configuration.
- Adjacent first-party surfaces excluded from ownership: comparison baselines/ablations, notebooks/results used for evaluation, website/paper presentation material, repository CI/development tooling and contributor/project governance.
- First-party operating / deployment modes considered: runnable multi-agent AI2-THOR and SAR episodes using the LLaMAR planner/action/verifier loop with two or more embodied robots.
- Recursion level: one multi-robot task episode/team is the system-in-focus. Individual embodied robot action streams are the distinct operational S1 units for S2/S3 analysis; planner/action/verifier prompts are organizational functions over that team rather than separate viable systems solely because they have distinct names.
- Reviewed revision: `d2b74cac79a0f070d87a150712f8e2ae174920be`.
- Observation date: 2026-09-26.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

The runnable LLaMAR baseline instantiates several embodied agents in one shared environment. At each step the runtime preserves per-agent observation/state/action-success history together with shared open/completed subtasks and, in the configured path, combined memory. A model-driven planner first produces a whole-team open-subtask plan. A model-driven action/controller call then receives all agents' current observations, states, previous actions/failures, the shared plan and memory, and outputs the next action for every robot. The environment executes the joint action and returns per-agent success/state changes.

The interaction is not merely parallel task decomposition. The first-party prompts explicitly identify physical interference between agents as a problem to regulate: robots should avoid blocking/bumping each other, can be told to stay idle while another robot completes a step, and failure examples diagnose one robot's failed action as caused by other robots physically blocking a cabinet. The corrective response assigns waiting/move-aside/close-and-clear actions across multiple robots, so the anti-interference relation changes subsequent behavior of the involved operational units.

After each joint action, a verifier prompt reads the team task plus all robots' current observations/states/previous actions and returns the shared list of completed subtasks. That result is fed into the planner, which receives all robot observations and the open/completed task state and updates the active team plan before the next action call. This provides a whole-team current view and a current-control path over team commitments/actions in addition to the S2-specific anti-interference decisions.

The verifier is not credited as S3*. Although it is a distinct prompt-stage and its output affects replanning, it uses the same first-party model service/configuration and substantially the same ordinary episode observations as the planner/action path. No separate model/provider, independent evidence channel or organizational independence boundary is established. It therefore functions as in-band completion reporting/monitoring rather than complementary audit.

No prospective capability-adaptation loop was established at the frozen revision. Replanning and failure correction change the current episode, not the future installed capabilities of LLaMAR across episodes. No runtime identity/ultimate-policy authority was found.

Primary evidence:

- [`README.md`](https://github.com/nsidn98/LLaMAR/blob/d2b74cac79a0f070d87a150712f8e2ae174920be/README.md) — project identity and documented multi-agent Plan/Act/Correct/Verify operating architecture.
- [`AI2Thor/baselines/llamar/llamar.py`](https://github.com/nsidn98/LLaMAR/blob/d2b74cac79a0f070d87a150712f8e2ae174920be/AI2Thor/baselines/llamar/llamar.py) — executable episode loop: planner → actor → environment step → verifier → planner, with shared open/completed subtasks.
- [`AI2Thor/baselines/llamar/llamar_utils_multiagent.py`](https://github.com/nsidn98/LLaMAR/blob/d2b74cac79a0f070d87a150712f8e2ae174920be/AI2Thor/baselines/llamar/llamar_utils_multiagent.py) — whole-team planner/action/verifier prompts, per-agent joint action output, explicit blocking/bumping disturbance and cross-agent corrective examples.
- [`AI2Thor/env_new.py`](https://github.com/nsidn98/LLaMAR/blob/d2b74cac79a0f070d87a150712f8e2ae174920be/AI2Thor/env_new.py) — multiple embodied agent state/observation/action histories and whole-team planner/verifier input construction.
- [`SAR/baselines/llamar.py`](https://github.com/nsidn98/LLaMAR/blob/d2b74cac79a0f070d87a150712f8e2ae174920be/SAR/baselines/llamar.py) — equivalent runnable multi-agent loop in the SAR environment.

## Operational model

Each robot is an embodied operational stream acting on the shared environment. The central action/controller model receives the current state of the whole team and selects a next action for every robot; those actions execute and produce per-agent successes/failures and changed observations. The joint model call can deliberately idle or move one robot to remove interference with another, so coordination is not inferred from agent count alone.

At the next organizational layer, the planner maintains the shared active subtask set for the whole team. After the verifier updates completed commitments, the planner sees all robot observations plus the current open/completed set and can preserve or modify the active plan. The subsequent action/controller call translates that updated whole-team commitment state into per-robot action choices.

## S1 — Operations

- State: A
- Function: execute the embodied work required to complete the shared task through robot-specific actions in the environment.
- Disturbance / variety regulated: partial observations, object locations/states, navigation/manipulation requirements, action failures and changing environment state during a long-horizon episode.
- Decisive decision or feedback right: choose each robot's next substantive environment action from the current observations/state and interpret returned success/failure when selecting what happens next.
- Decision owner: the first-party model-driven LLaMAR action/controller path over the embodied robot streams.
- Supporting / enforcement mechanisms: AI2-THOR/SAR environment adapters, feasible-action mapping, per-agent observations/states/action histories, task/subtask state and deterministic execution plumbing.
- Closure path: team task/current plan -> model selects an action for each robot -> environment executes each embodied action -> per-agent observation/state/success/failure returns -> later model call selects changed robot actions -> episode progresses.
- Boundary reachability: `AI2Thor/baselines/llamar/llamar.py` and `SAR/baselines/llamar.py` are shipped runnable first-party episode entrypoints and directly execute the credited action/environment feedback loop.
- Why this is / is not agent-owned: simulator code transports actions and state, while the substantive next-action choices are model-generated from the live episode context.
- Evidence: [`AI2Thor/baselines/llamar/llamar.py`](https://github.com/nsidn98/LLaMAR/blob/d2b74cac79a0f070d87a150712f8e2ae174920be/AI2Thor/baselines/llamar/llamar.py); [`AI2Thor/baselines/llamar/llamar_utils_multiagent.py`](https://github.com/nsidn98/LLaMAR/blob/d2b74cac79a0f070d87a150712f8e2ae174920be/AI2Thor/baselines/llamar/llamar_utils_multiagent.py); [`AI2Thor/env_new.py`](https://github.com/nsidn98/LLaMAR/blob/d2b74cac79a0f070d87a150712f8e2ae174920be/AI2Thor/env_new.py); [`SAR/baselines/llamar.py`](https://github.com/nsidn98/LLaMAR/blob/d2b74cac79a0f070d87a150712f8e2ae174920be/SAR/baselines/llamar.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: next-action authority is centralized in the model call rather than separately modelled inside each physical robot, but the operational behavior is still first-party agent-owned at the assessed team boundary.

## S2 — Coordination

- State: A
- Function: attenuate concrete interference among simultaneously operating embodied robots sharing the same physical workspace.
- Disturbance / variety regulated: robots blocking/bumping one another, congestion around shared objects/receptacles, one robot's manipulation/navigation preventing another robot from completing its assigned action, and unnecessary simultaneous movement into the same constrained area.
- Decisive decision or feedback right: choose joint next-step actions such as waiting, moving aside, closing an obstruction or delaying one robot so another robot can proceed without cross-agent interference.
- Decision owner: the first-party model-driven joint action/controller path using whole-team state and failure context.
- Supporting / enforcement mechanisms: shared observations/state, previous action/failure fields, combined task/memory state, explicit anti-blocking prompt constraints and per-robot joint action output.
- Closure path: multiple robot operations interact in one room -> execution exposes cross-agent blocking/failure -> the next model call reasons about the interference -> assigns compensating actions across the involved robots -> later robot behavior changes and the blocked operation can proceed.
- Boundary reachability: the standard LLaMAR actor prompt is called on every episode step from the runnable baseline and directly receives/returns the team state and per-agent joint actions used by `env.step()`.
- Why this is / is not agent-owned: the anti-interference choice is contextual model reasoning over current cross-agent state; deterministic code only executes the selected joint actions.
- Evidence: [`AI2Thor/baselines/llamar/llamar_utils_multiagent.py`](https://github.com/nsidn98/LLaMAR/blob/d2b74cac79a0f070d87a150712f8e2ae174920be/AI2Thor/baselines/llamar/llamar_utils_multiagent.py); [`AI2Thor/baselines/llamar/llamar.py`](https://github.com/nsidn98/LLaMAR/blob/d2b74cac79a0f070d87a150712f8e2ae174920be/AI2Thor/baselines/llamar/llamar.py); [`AI2Thor/env_new.py`](https://github.com/nsidn98/LLaMAR/blob/d2b74cac79a0f070d87a150712f8e2ae174920be/AI2Thor/env_new.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: generic task allocation is not the basis for S2; the positive state rests on the separately evidenced physical interference problem and feedback relation.
- Distinct S1 units: the concurrently acting embodied robot streams (Alice, Bob and additional configured robots), each with its own observation/state/action/success history and physical action effect.
- Inter-S1 disturbance: one robot can physically block/bump another or occupy/open an object/path such that another robot's navigation/manipulation fails or must wait.
- Attenuating coordination relation: the joint controller sees all robots' state/history and is explicitly instructed to avoid blocking/bumping; failure reasoning can prescribe wait/move-aside/clear-path behavior across the involved robots.
- Feedback into subsequent S1 behaviour: the model's coordinated per-robot action dictionary is passed through `action_checker` and then to `env.step()`, changing the next embodied action of each robot.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the decisive witness is regulation of a concrete interaction disturbance among simultaneous embodied operations, not the existence of multiple robots, shared memory or a task decomposition graph.

## S3 — Inside-and-now control

- State: A
- Function: maintain the whole team's current task commitments and intervene in the active multi-robot plan as completion/failure/environment information changes.
- Disturbance / variety regulated: changing team progress, completed versus still-open commitments, newly observed environment information and failures requiring the active plan or current robot allocation/actions to change.
- Decisive decision or feedback right: decide the current shared open-subtask plan for the team and, through the whole-team action/controller stage, determine which operational action each robot should take now under that plan.
- Decision owner: the first-party model-driven planner and whole-team action/controller path.
- Whole-system current view: the planner receives the task, current observation from every configured robot, and the shared open/completed subtask state after each verifier step; the action/controller additionally receives every robot's state, previous action/failure, shared subtasks and combined memory.
- Current-control decision scope: preserve or revise the team's active unfinished commitments and assign the next concrete actions/subtasks across the current robot population, including interventions after failures and current spatial conflicts.
- Supporting / enforcement mechanisms: shared open/completed-subtask state, verifier updates, whole-team observation aggregation, combined memory, planner prompt, action/controller prompt and repeated plan-update loop.
- Closure path: robot operations execute -> team observations/actions and completion state update -> verifier updates completed commitments -> planner forms a revised whole-team open plan -> action/controller maps that current plan/state to robot-specific next actions -> changed operations execute and report back.
- Boundary reachability: the planner/action stages are invoked in every standard runnable LLaMAR episode; no external orchestrator is required to form the whole-team view or return interventions into robot operation.
- Why this is / is not agent-owned: the semantic choice of the current plan and per-robot intervention is model-driven; deterministic code stores plan/completion state and transports decisions into the environment.
- Evidence: [`AI2Thor/baselines/llamar/llamar.py`](https://github.com/nsidn98/LLaMAR/blob/d2b74cac79a0f070d87a150712f8e2ae174920be/AI2Thor/baselines/llamar/llamar.py); [`AI2Thor/baselines/llamar/llamar_utils_multiagent.py`](https://github.com/nsidn98/LLaMAR/blob/d2b74cac79a0f070d87a150712f8e2ae174920be/AI2Thor/baselines/llamar/llamar_utils_multiagent.py); [`AI2Thor/env_new.py`](https://github.com/nsidn98/LLaMAR/blob/d2b74cac79a0f070d87a150712f8e2ae174920be/AI2Thor/env_new.py); [`SAR/baselines/llamar.py`](https://github.com/nsidn98/LLaMAR/blob/d2b74cac79a0f070d87a150712f8e2ae174920be/SAR/baselines/llamar.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: S3 credit is not based on the component name `Planner`; it rests on the whole-team current view plus returned decisions changing the active shared commitments and robot actions.

## S3* — Complementary audit

- State: —
- Function: the verifier provides in-band completion reporting, but no materially independent complementary-audit function is established.
- Disturbance / variety regulated: incorrect assumptions about whether a subtask has completed can be corrected before replanning, but the checked claim remains part of the ordinary task-progress loop.
- Decisive decision or feedback right: no independent auditor with a distinct authority/evidence channel is established; the verifier prompt only classifies completed subtasks for the same episode.
- Decision owner: none established for qualifying S3*; the verifier uses the ordinary model service/configuration and shared episode evidence.
- Supporting / enforcement mechanisms: verifier-specific prompt, all robot observations/states/previous actions, shared open/completed subtasks and combined memory.
- Closure path: robot actions execute -> ordinary episode observations feed verifier -> completed-subtask list feeds planner -> current plan changes; this is ordinary progress reporting/monitoring without an evidenced independent audit boundary.
- Why this is / is not agent-owned: a semantic verifier exists, but `verifier` naming and a separate prompt-stage do not establish complementary independence.
- Evidence: [`AI2Thor/baselines/llamar/llamar.py`](https://github.com/nsidn98/LLaMAR/blob/d2b74cac79a0f070d87a150712f8e2ae174920be/AI2Thor/baselines/llamar/llamar.py); [`AI2Thor/baselines/llamar/llamar_utils_multiagent.py`](https://github.com/nsidn98/LLaMAR/blob/d2b74cac79a0f070d87a150712f8e2ae174920be/AI2Thor/baselines/llamar/llamar_utils_multiagent.py); [`AI2Thor/env_new.py`](https://github.com/nsidn98/LLaMAR/blob/d2b74cac79a0f070d87a150712f8e2ae174920be/AI2Thor/env_new.py).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: the verifier does influence subsequent planning; the missing requirement is organizational/complementary independence, not lack of feedback.

### Absence scope

- Surfaces inspected: README architecture, AI2-THOR and SAR episode loops, planner/action/verifier prompts, environment input construction, checker/statistics paths and comparison/evaluation boundaries.
- Plausible first-party paths checked: named Verifier module; environment `checker`; task-success metrics; separate prompt role; notebooks/baseline evaluation.
- Why no material first-party path remains: the runtime verifier shares the ordinary model/service and episode evidence path, while environment checkers and benchmark artifacts are deterministic task/evaluation machinery rather than an independent organizational auditor with corrective authority.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party prospective capability-adaptation loop is established beyond current-episode planning/replanning.
- Disturbance / variety regulated: LLaMAR adapts its current task plan to new observations and failures, but does not evidence an actor that senses an external future environment, generates capability-change options and installs a change for later operational capability.
- Decisive decision or feedback right: none established for prospective adaptation of the installed harness/robot organization across episodes.
- Decision owner: none established for S4.
- Supporting / enforcement mechanisms: current observation updates, planner replanning, memory and failure reasoning.
- Closure path: environment change/failure -> current episode replanning -> changed immediate robot actions; no future-oriented capability option is implemented into later installed capability.
- Why this is / is not agent-owned: current replanning is S1/S3 regulation, not evidence of S4 merely because the plan changes.
- Evidence: [`AI2Thor/baselines/llamar/llamar.py`](https://github.com/nsidn98/LLaMAR/blob/d2b74cac79a0f070d87a150712f8e2ae174920be/AI2Thor/baselines/llamar/llamar.py); [`AI2Thor/baselines/llamar/llamar_utils_multiagent.py`](https://github.com/nsidn98/LLaMAR/blob/d2b74cac79a0f070d87a150712f8e2ae174920be/AI2Thor/baselines/llamar/llamar_utils_multiagent.py); [`README.md`](https://github.com/nsidn98/LLaMAR/blob/d2b74cac79a0f070d87a150712f8e2ae174920be/README.md).
- Basis: structural negative search.
- Confidence: high.
- Caveats: long-horizon planning and replanning are substantial capabilities but remain inside the present episode boundary.

### Absence scope

- Surfaces inspected: runnable episode paths, planner/action/verifier prompts, environment state/memory, documented architecture and repository-level experiment/evaluation surfaces.
- Plausible first-party paths checked: replanning as adaptation; memory as learning; environment exploration; comparison/ablation/evaluation artifacts.
- Why no material first-party path remains: all runtime change closes on the current task/episode; no persistent future capability/policy/organizational redesign path is established.

## S5 — Policy and identity

- State: —
- Function: no first-party runtime identity or ultimate-policy authority is established at the multi-robot episode boundary.
- Disturbance / variety regulated: task text, model/configuration parameters, prompt rules and simulator limits constrain behavior but do not constitute identity-level adjudication.
- Decisive decision or feedback right: none established for defining or reconciling the team's ultimate identity/purpose/policy under competing S3/S4 demands.
- Decision owner: none established for S5.
- Supporting / enforcement mechanisms: user-selected task/scene/configuration, static prompts and runtime constraints.
- Closure path: external task/configuration enters directly as operating constraints; no identity-level issue -> legitimate ultimate authority -> policy decision -> returned governance loop is evidenced.
- Why this is / is not agent-owned: the models control current operational/coordination/management choices but do not choose the organization's ultimate identity or policy.
- Evidence: [`README.md`](https://github.com/nsidn98/LLaMAR/blob/d2b74cac79a0f070d87a150712f8e2ae174920be/README.md); [`AI2Thor/baselines/llamar/llamar.py`](https://github.com/nsidn98/LLaMAR/blob/d2b74cac79a0f070d87a150712f8e2ae174920be/AI2Thor/baselines/llamar/llamar.py); [`AI2Thor/baselines/llamar/llamar_utils_multiagent.py`](https://github.com/nsidn98/LLaMAR/blob/d2b74cac79a0f070d87a150712f8e2ae174920be/AI2Thor/baselines/llamar/llamar_utils_multiagent.py).
- Basis: structural negative search.
- Confidence: high.
- Caveats: static system prompts describing robot roles/constraints are not S5 by themselves.

### Absence scope

- Surfaces inspected: README, runnable AI2-THOR/SAR baselines, model prompts/configuration, task/scene setup and repository governance/evaluation boundaries.
- Plausible first-party paths checked: task objective as purpose; planner as policy; system prompt as identity; verifier as final authority; project governance.
- Why no material first-party path remains: these surfaces define the current task, operating constraints, current-control roles or development governance rather than runtime identity/ultimate-policy authority.

## Recursion

One multi-robot episode/team is the assessed recursion. Individual embodied robot streams are distinct S1 operations because they have separate observations/state/action histories and physical effects. The first-party joint action/controller regulates their interference as S2. The planner/action control over shared current commitments supplies S3. The verifier is retained as ordinary in-band progress reporting rather than promoted to S3*. No S4 or S5 closure is established.

## Variety and escalation

Local environmental variety returns through each robot's observation/action-success state. Cross-agent interference can escalate into explicit S2 reasoning that changes multiple robots' next actions. Whole-team progress/completion state then returns through the verifier to the planner, which can change the active shared commitments and next joint actions. No independent-audit, prospective-adaptation or identity-policy escalation owner was established.

## Evidence gaps

- Structural review only; no new AI2-THOR/SAR episode was executed.
- S2 and S3 are co-located in closely coupled model-driven planning/action prompts, so the assessment distinguishes them by function: S2 is credited only for concrete cross-agent interference attenuation; S3 only for whole-team current view/commitment control.
- The verifier's separate prompt and feedback are insufficient for S3* because an independence boundary was not established.
- No claim is made that the embodied robots are independently model-governed agents; autonomy states describe ownership of the corresponding organizational decision path within the assessed first-party system.
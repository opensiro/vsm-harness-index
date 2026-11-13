---
harness_id: roboharness
project_name: RoboHarness
repository: https://github.com/BinceQu/RoboHarness
review_ref: 69b811646beaf6409194fc505ee70fb45e12da44
reviewed_at: 2026-11-13
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# RoboHarness

## Review boundary

- System in focus: The shipped RoboHarness operational harness with its documented external agent integration.
- Purpose and identity: Complete embodied household tasks in an episode using model-selected observations and robot actions.
- Relevant environment: BEHAVIOR and RoboDojo episodes, changing scene and robot state, finite steps, tool errors and simulator feedback.
- Standard-distribution boundary: Supported BEHAVIOR V1 Claude Code/Codex plugin and V2 R1 Pro workspace. The shipped ARX X5 RoboDojo adapter is considered as an alternate V2 embodiment.
- Credited operating / distribution surfaces: V1 agent launcher, active MCP catalog, camera and action tools, skill lifecycle and receipts; V2 agent workspace, observation hooks, tools and per-case state.
- Adjacent first-party surfaces excluded from ownership: Native Claude Code/Codex agent engines and model services supply inference and task choice in the declared composition. Benchmark scoring, episode reproducibility audits, offline trajectory viewers, asset publication and source-repository maintenance are separate from the operational agent.
- First-party operating / deployment modes considered: V1 plugin mode, V2 local robot workspace through the BEHAVIOR runner, and V2 workspace through the RoboDojo bridge.
- Recursion level: One embodied agent/robot and its task episode; serial benchmark cases and alternative embodiments are separate invocations.
- Reviewed revision: `69b811646beaf6409194fc505ee70fb45e12da44`.
- Observation date: 2026-11-13.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

V1 launches a native agent with private session state, a scoped tool catalog and a serialized robot interface. V2 stages a robot workspace with Python tools, skills, history and observation delivery, and starts an external agent in that workspace. The evaluator drives and scores instances separately. The runtime can reproduce an archived V1 context and collect result and trajectory files.

## Operational model

The task agent selects observation, planning and movement calls and can change its next action after reading camera/tool results. Each episode is the operational cell. Camera services, motion planners, controllers and evaluator processes are differentiated support for that cell.

## S1 — Operations

- State: A
- Function: Complete an embodied task through model-selected observations and actions.
- Disturbance / variety regulated: Scene state, tool outputs and failures, finite control steps, incomplete progress.
- Decisive decision or feedback right: Select the next observation, skill or robot action and decide when work is complete.
- Decision owner: Native coding agent/model in the shipped integration.
- Supporting / enforcement mechanisms: V1 scoped MCP, skill lifecycle and serialized actions; V2 workspace, driver and model-visible observation delivery.
- Closure path: Task prompt → agent chooses a tool → robot or simulator state changes → new camera image or result reaches the agent → next choice or hand-in.
- Boundary reachability: The supported V1 launcher and V2 runner start the agent with the shipped interface; the ARX workspace exposes the analogous tool/feedback boundary.
- Why this is / is not agent-owned: Agent chooses task steps; motion and perception machinery execute or inform them.
- Evidence: [v1](https://github.com/BinceQu/RoboHarness/blob/69b811646beaf6409194fc505ee70fb45e12da44/harness/v1/claude_code/README.md), [v1code](https://github.com/BinceQu/RoboHarness/blob/69b811646beaf6409194fc505ee70fb45e12da44/harness/v1/claude_code/src/embodied_claude_code/service.py), [v2](https://github.com/BinceQu/RoboHarness/blob/69b811646beaf6409194fc505ee70fb45e12da44/harness/v2/README.md), [runner](https://github.com/BinceQu/RoboHarness/blob/69b811646beaf6409194fc505ee70fb45e12da44/eval/runner/core.py#L530-L692), [receipt](https://github.com/BinceQu/RoboHarness/blob/69b811646beaf6409194fc505ee70fb45e12da44/harness/v2/R1_pro/tools/util/observation_hook.py), [alternate](https://github.com/BinceQu/RoboHarness/blob/69b811646beaf6409194fc505ee70fb45e12da44/eval/robodojo/README.md).
- Basis: structural and explicit
- Confidence: High for the supported source path.
- Caveats: Model service and native agent are dependencies. No live rollout performed.

## S2 — Coordination

- State: —
- Function: No distinct inter-S1 coordination path is supplied within the episode boundary.
- Disturbance / variety regulated: Actions can overlap with observation, multiple robot subsystems can be active and evaluation instances reuse infrastructure.
- Decisive decision or feedback right: The runner orders cases and the robot interface serializes commands.
- Decision owner: Runner and action runtime for execution integrity.
- Supporting / enforcement mechanisms: Session IDs, action serialization, fresh workspace and controller ownership.
- Closure path: Action completion and new observations return to the same agent; the evaluator then moves to a new case.
- Why this is / is not agent-owned: The interference candidates affect tools of one decision-making agent or separate serial episodes.
- Evidence: [v1](https://github.com/BinceQu/RoboHarness/blob/69b811646beaf6409194fc505ee70fb45e12da44/harness/v1/claude_code/README.md), [v2](https://github.com/BinceQu/RoboHarness/blob/69b811646beaf6409194fc505ee70fb45e12da44/harness/v2/README.md), [runner](https://github.com/BinceQu/RoboHarness/blob/69b811646beaf6409194fc505ee70fb45e12da44/eval/runner/core.py#L530-L692), [workspace](https://github.com/BinceQu/RoboHarness/blob/69b811646beaf6409194fc505ee70fb45e12da44/eval/runner/workspace_run.py#L135-L195).
- Basis: bounded source review
- Confidence: High in the documented single-agent modes.
- Caveats: A separately assembled multi-agent robotics system would have a different operating boundary.

### Absence scope

- Surfaces inspected: V1 MCP launcher, V2 driver/workspace, sequential runner and RoboDojo bridge.
- Plausible first-party paths checked: Concurrent robot actions, shared camera state, case isolation and evaluator/agent scheduling.
- Why no material first-party path remains: Each episode supplies a single task decision owner; these controls address its own action stream and isolated cases.

## S3 — Inside-and-now control

- State: —
- Function: No whole-current control over distinct live operational cells is supplied.
- Disturbance / variety regulated: An episode may exhaust its step budget, stall or require a stop.
- Decisive decision or feedback right: Runner and operator may end the current episode; the selected budget and cases come from configuration.
- Decision owner: Operator and deterministic runner within episode/evaluation scope.
- Supporting / enforcement mechanisms: Status monitor, evaluator budget, finish requests and process termination.
- Closure path: Finish or timeout ends the current run and yields a result; it does not return a new shared allocation or commitment across S1 units.
- Why this is / is not agent-owned: The controls are episode supervision and benchmark execution.
- Evidence: [runner](https://github.com/BinceQu/RoboHarness/blob/69b811646beaf6409194fc505ee70fb45e12da44/eval/runner/core.py#L530-L692), [workspace](https://github.com/BinceQu/RoboHarness/blob/69b811646beaf6409194fc505ee70fb45e12da44/eval/runner/workspace_run.py#L135-L195), [ops](https://github.com/BinceQu/RoboHarness/blob/69b811646beaf6409194fc505ee70fb45e12da44/eval/behavior/behavior_interface/operator_controls.py), [repro](https://github.com/BinceQu/RoboHarness/blob/69b811646beaf6409194fc505ee70fb45e12da44/README.md#reproduction-contract).
- Basis: bounded source review
- Confidence: Medium-high.
- Caveats: The result is scoped to the embodied harness, not the benchmark organization.

### Absence scope

- Surfaces inspected: Runner, workspace controller, operator stop, monitoring and evaluation configuration.
- Plausible first-party paths checked: Whole-run status, manual stop, fixed budget, reinitialization and advancement to next case.
- Why no material first-party path remains: No in-boundary current view and discretionary authority returns a change to commitments of multiple live operating units.

## S3* — Complementary audit

- State: —
- Function: No complementary audit path returns a finding to an in-boundary current-control function.
- Disturbance / variety regulated: A final agent answer, delivery failure or unsuccessful trajectory can disagree with episode reality.
- Decisive decision or feedback right: The official evaluator scores simulator state; the runner checks native transcripts and accepts or rejects reproduction evidence.
- Decision owner: Separate evaluator and deterministic reproduction checks.
- Supporting / enforcement mechanisms: Official result JSON, trajectory viewer, archive context match and standalone audit tools.
- Closure path: The evaluator independently records success/score and the runner may end or invalidate a benchmark case. Findings go to run artifacts rather than an operational S3 correction path.
- Why this is / is not agent-owned: The external scoring and separate protocol audits assess the experiment. Model-visible observations close the task itself.
- Evidence: [evaluation](https://github.com/BinceQu/RoboHarness/blob/69b811646beaf6409194fc505ee70fb45e12da44/eval/README.md), [runner](https://github.com/BinceQu/RoboHarness/blob/69b811646beaf6409194fc505ee70fb45e12da44/eval/runner/core.py#L530-L692), [workspace](https://github.com/BinceQu/RoboHarness/blob/69b811646beaf6409194fc505ee70fb45e12da44/eval/runner/workspace_run.py#L135-L195), [archived](https://github.com/BinceQu/RoboHarness/blob/69b811646beaf6409194fc505ee70fb45e12da44/eval/runner/native_context.py), [audit](https://github.com/BinceQu/RoboHarness/tree/69b811646beaf6409194fc505ee70fb45e12da44/eval/runner/audit).
- Basis: bounded source review
- Confidence: Medium-high.
- Caveats: The evaluator provides genuine independent measurement at the benchmark boundary.

### Absence scope

- Surfaces inspected: Official evaluator wrapper, live runner transcript check, read-only viewer and audit scripts.
- Plausible first-party paths checked: World-state score, archived context mismatch rejection, delivery audit and replay.
- Why no material first-party path remains: Outputs complete or invalidate benchmark cases and produce artifacts. No shipped complementary audit changes operating policy through an in-boundary S3 owner.

## S4 — Outside-and-then intelligence

- State: —
- Function: No prospective external-environment adaptation loop is supplied.
- Disturbance / variety regulated: New scenes, embodiments, tasks and experimental variants affect operation.
- Decisive decision or feedback right: Agent selects local tactics; authors configure tools, embodiments and tasks.
- Decision owner: Task agent and repository authors within their distinct scopes.
- Supporting / enforcement mechanisms: Skill catalog, per-episode scene state, versioned workspaces and experiment reports.
- Closure path: Observations change immediate actions and new releases can be selected externally; the runtime shows no adaptation decision over future capability.
- Why this is / is not agent-owned: Grounding and replanning are operational task responses.
- Evidence: [v1](https://github.com/BinceQu/RoboHarness/blob/69b811646beaf6409194fc505ee70fb45e12da44/harness/v1/claude_code/README.md), [v2](https://github.com/BinceQu/RoboHarness/blob/69b811646beaf6409194fc505ee70fb45e12da44/harness/v2/README.md), [receipt](https://github.com/BinceQu/RoboHarness/blob/69b811646beaf6409194fc505ee70fb45e12da44/harness/v2/R1_pro/tools/util/observation_hook.py), [repro](https://github.com/BinceQu/RoboHarness/blob/69b811646beaf6409194fc505ee70fb45e12da44/README.md#reproduction-contract).
- Basis: bounded source review
- Confidence: Medium-high.
- Caveats: Research and upstream development fall outside the installed episode boundary.

### Absence scope

- Surfaces inspected: Workspace setup, tools/skills, observation hook, task catalog and reproduction configuration.
- Plausible first-party paths checked: Current-scene replanning, ability to switch embodiments, new tool/skill versions and benchmark reports.
- Why no material first-party path remains: Shipped behavior consumes configured capabilities during execution; it does not return a prospective capability selection driven by external intelligence.

## S5 — Policy and identity

- State: —
- Function: No ultimate identity or policy decision return is supplied.
- Disturbance / variety regulated: Task instructions, runtime capabilities, robot access and operator limits constrain operation.
- Decisive decision or feedback right: The launch profile and task configuration set operating rules; an operator can stop activity.
- Decision owner: Authors and operator for static policy and episode controls.
- Supporting / enforcement mechanisms: Workspace instructions, tool exposure, episode budgets and stop handlers.
- Closure path: The agent acts within configured bounds; no shipped escalation adjudicates and propagates identity-level policy.
- Why this is / is not agent-owned: Operating instructions and tool boundaries enforce configured constraints.
- Evidence: [v1](https://github.com/BinceQu/RoboHarness/blob/69b811646beaf6409194fc505ee70fb45e12da44/harness/v1/claude_code/README.md), [instructions](https://github.com/BinceQu/RoboHarness/blob/69b811646beaf6409194fc505ee70fb45e12da44/harness/v2/R1_pro/AGENTS.md), [ops](https://github.com/BinceQu/RoboHarness/blob/69b811646beaf6409194fc505ee70fb45e12da44/eval/behavior/behavior_interface/operator_controls.py), [repro](https://github.com/BinceQu/RoboHarness/blob/69b811646beaf6409194fc505ee70fb45e12da44/README.md#reproduction-contract).
- Basis: bounded source review
- Confidence: High for the declared modes.
- Caveats: Repository maintainer governance is outside the runtime.

### Absence scope

- Surfaces inspected: V1 profile and MCP policy, V2 instructions, runner limits and operator finish controls.
- Plausible first-party paths checked: Tool and role selection, capability rules, operator override and release governance.
- Why no material first-party path remains: No in-boundary issue reaches ultimate authority and returns as a governing identity or policy decision.

## Distributed OSS parent arrangement

Project maintainers and benchmark operators control source and evaluation setup. The observed episode boundary supplies no whole-current parent control, prospective adaptation or ultimate-policy return.

## Self-hosted and non-human modes

The supported local evaluation setups wire an external agent to the appropriate workspace/interface and model service. Operator commands can end an episode or stop its processes.

## Recursion

Tools, skills, evaluator services and serial cases do not establish independently operating agent cells in one assessed episode.

## Variety and escalation

Tool visibility, step budgets, session ownership, action serialization, receipts and terminal failure paths regulate operational variation.

## Evidence gaps

This review inspected pinned source and its supported configurations. It did not run the simulator, physical hardware or a model provider. S1 is attributed to the model in the supported composition, with inner agent implementation external.

---
harness_id: show-harness
project_name: Show-Harness
repository: https://github.com/showlab/Show-Harness
review_ref: 6ad77dbc6180e973dff8148ffcca6c085580cea2
reviewed_at: 2026-10-28
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Show-Harness

## Review boundary

- System in focus: the shipped observation-to-action robot harness, including supported single-arm and unified dual-arm rollout modes.
- Purpose and identity: execute visual manipulation instructions through VLM-selected atomic robot actions.
- Relevant environment: robot cameras, proprioception, objects, workspaces, model endpoints and operator interventions.
- Standard-distribution boundary: source-distributed core runners, VLM roles, robot/interpreter interfaces, prompts, configuration and wired runtime plugins.
- Credited operating / distribution surfaces: core/launch.py, core/runners/real.py and dual.py, core/vlm roles, plugins/subgoal, recovery, dagger, affordance and deepplan, plus the installed interpreters and robot sessions.
- Adjacent first-party surfaces excluded from ownership: model training, trajectory/dataset construction, benchmark reporting, tests and repository CI; these do not supply runtime metasystem owners.
- First-party operating / deployment modes considered: single Franka/Piper, unified dual Piper, token-based variants and documented simulation entry points; optional human DAgger override and runtime recovery.
- Recursion level: one robot-task system; dual arms supply distinct concurrent operational tracks, not independently viable recursive systems.
- Reviewed revision: `6ad77dbc6180e973dff8148ffcca6c085580cea2`.
- Observation date: 2026-10-28.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The launch path builds camera/robot sessions, atomic interpreters, VLM clients and optional plugins. A planner can produce subgoal tracks; a controller observes current images, recent moves, proprioception and recovery notes and selects a motion/grasp/release/completion token. The runner executes that token and returns changed observations to the next decision. The dual runner maintains independent arm stages, histories, recovery state and completion, executing the two selected tokens concurrently. Its shared VLM sees the front view and both wrists. Explicit WAIT stages and STILL actions regulate handovers and shared destinations. Measured-width recovery can reopen and roll back a failed grasp. Final visual task verification can trigger bounded replanning. DAgger exposes direct human action overrides, while limits, Z floors and parser fallbacks constrain execution. Episode logs retain observations and decisions; training and evaluation are separate surfaces.

## Operational model

The single-arm manipulation loop is S1. In dual mode each arm track has its own subgoals, observation/recovery state and direct contribution to the shared manipulation outcome. One VLM may own both operational decisions and the coordination judgment: actor count is not the criterion. Coordination is established by the concrete interference witness below, rather than by two arms alone. Planning a task, checking its completion and enforcing fixed step limits do not by themselves establish whole-system S3 or independent S3*.

## S1 — Operations

- State: A
- Function: transform visual manipulation instructions into executed robot actions and completed subgoals.
- Disturbance / variety regulated: scene changes, object position, missed grasps, malformed action responses and incomplete manipulation.
- Decisive decision or feedback right: choose subsequent atomic action and judge stage completion from current observations.
- Decision owner: the first-party controller/planner VLM roles in the launched rollout.
- Supporting / enforcement mechanisms: camera sessions, token parsing, atomic interpreters, physical safety floors, step limits and recovery state.
- Closure path: VLM token → interpreter action → fresh scene/proprioception and recovery context → next VLM action or completion/replan.
- Boundary reachability: core/launch.py directly wires the shipped roles, prompts and real/dual runners; users provide model/hardware configuration, not a custom decision organization.
- Why this is / is not agent-owned: removing the VLM leaves token transport and fixed recovery but removes discretionary visual action choice.
- Evidence: [launch](https://github.com/showlab/Show-Harness/blob/6ad77dbc6180e973dff8148ffcca6c085580cea2/core/launch.py), [real runner](https://github.com/showlab/Show-Harness/blob/6ad77dbc6180e973dff8148ffcca6c085580cea2/core/runners/real.py), [VLM roles](https://github.com/showlab/Show-Harness/blob/6ad77dbc6180e973dff8148ffcca6c085580cea2/core/vlm/roles.py), [recovery](https://github.com/showlab/Show-Harness/blob/6ad77dbc6180e973dff8148ffcca6c085580cea2/plugins/recovery/plugin.py).
- Basis: structural.
- Confidence: high for shipped decision wiring.
- Caveats: no physical robot or model-provider run; no effectiveness or safety certification is inferred.

## S2 — Coordination

- State: A
- Function: regulate interference between two concurrently acting manipulation tracks.
- Disturbance / variety regulated: both grippers entering a small destination, unsafe simultaneous contact with one object, and premature release during handover.
- Decisive decision or feedback right: select which arm waits and when the visible condition permits it to resume.
- Decision owner: the dual planner/controller VLM, applying the shipped coordination instructions to live joint observations.
- Supporting / enforcement mechanisms: per-arm stage state, WAIT descriptions, STILL tokens and concurrent interpreter execution.
- Closure path: shared scene and both arm states → VLM WAIT/STILL/progress judgment → one arm holds while the other acts → changed visible handover/destination state → resumed action.
- Boundary reachability: the dual launch/runner uses DualSubgoalPlanner and DualControllerAgent with shipped dual prompts, without developer-authored coordination logic.
- Why this is / is not agent-owned: waiting completion is visually interpreted by the VLM rather than a runner-side hard gate; runtime executes the chosen response.
- Distinct S1 units: left and right arm manipulation tracks, each with its own subgoals, recent moves, recovery, completion and actuator/environment interaction.
- Inter-S1 disturbance: structurally evidenced shared-small-destination contention and giver/receiver handover interference.
- Attenuating coordination relation: planner inserts conditional WAIT stages; the joint controller selects STILL and orders delivery/contact according to current images.
- Feedback into subsequent S1 behaviour: satisfying the visible wait condition changes the next arm token and advances that arm's track.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: explicit collision/handover conditions determine mutual inhibition and resumption, beyond merely splitting a task into two lists.
- Evidence: [dual runner](https://github.com/showlab/Show-Harness/blob/6ad77dbc6180e973dff8148ffcca6c085580cea2/core/runners/dual.py), [dual controller](https://github.com/showlab/Show-Harness/blob/6ad77dbc6180e973dff8148ffcca6c085580cea2/core/vlm/dual_roles.py), [dual planning prompt](https://github.com/showlab/Show-Harness/blob/6ad77dbc6180e973dff8148ffcca6c085580cea2/plugins/subgoal/subgoal_planner_dual.txt), [dual action prompt](https://github.com/showlab/Show-Harness/blob/6ad77dbc6180e973dff8148ffcca6c085580cea2/prompts/controller_dual.txt).
- Basis: structural.
- Confidence: medium-high.
- Caveats: this mapping is specific to supported dual-arm mode; it does not establish a general multi-agent coordination service or measured collision avoidance reliability.

## S3 — Inside-and-now control

- State: —
- Function: no distinct whole-system resource/commitment regulation path established.
- Disturbance / variety regulated: step exhaustion, incomplete task and grasp failure are handled as local rollout execution.
- Decisive decision or feedback right: task planning/replanning belongs to operational roles; step/replan caps and safety constraints are selected by configuration/operator.
- Decision owner: VLM for operational choices; operator/configuration for fixed constraints, not a shipped S3 owner.
- Supporting / enforcement mechanisms: per-stage caps, max_replans, interpreter limits and DAgger preemption.
- Closure path: bounded operational retry/override; no function-specific whole-system bargaining/intervention loop.
- Why this is / is not agent-owned: neither autonomous S3 discretion nor a closed parent S3 mode follows from task-level action intervention.
- Evidence: [dual final-check/replan and caps](https://github.com/showlab/Show-Harness/blob/6ad77dbc6180e973dff8148ffcca6c085580cea2/core/runners/dual.py), [launch constraints](https://github.com/showlab/Show-Harness/blob/6ad77dbc6180e973dff8148ffcca6c085580cea2/core/launch.py), [DAgger](https://github.com/showlab/Show-Harness/blob/6ad77dbc6180e973dff8148ffcca6c085580cea2/plugins/dagger/plugin.py).
- Basis: structural.
- Confidence: medium-high.
- Caveats: joint scene visibility is not by itself S3 current-control authority.

### Absence scope

- Surfaces inspected: launch/config, real/dual runners, stage control, subgoal/deepplan/recovery and DAgger paths.
- Plausible first-party paths checked: global planner, remaining-work replan, completed-arm retirement, caps, operator preemption and optional planning pivots.
- Why no material first-party path remains: these close one task's manipulation and direct overrides; none supplies a separate whole-system resource/commitment decision and return at the declared recursion.

## S3* — Complementary audit

- State: —
- Function: no complementary independent operational audit path established.
- Disturbance / variety regulated: routine completion and grounding errors are checked within production.
- Decisive decision or feedback right: final scene verification and affordance grounding correction.
- Decision owner: production VLM/checking roles and deterministic sensor recovery; no independent audit owner.
- Supporting / enforcement mechanisms: saved episode images, measured gripper widths and final-task verification.
- Closure path: ordinary retry/replan/re-grounding, without complementary challenge of the operational reporting arrangement.
- Why this is / is not agent-owned: an agent making a mandatory production check does not alone establish S3*.
- Evidence: [final verification](https://github.com/showlab/Show-Harness/blob/6ad77dbc6180e973dff8148ffcca6c085580cea2/core/vlm/dual_roles.py), [affordance agent](https://github.com/showlab/Show-Harness/blob/6ad77dbc6180e973dff8148ffcca6c085580cea2/plugins/affordance/agent.py), [episode logger](https://github.com/showlab/Show-Harness/blob/6ad77dbc6180e973dff8148ffcca6c085580cea2/core/record/episode_logger.py).
- Basis: structural.
- Confidence: medium-high.
- Caveats: raw images can support a later external audit, which is not supplied by this rollout boundary.

### Absence scope

- Surfaces inspected: dual verification/replan, affordance pointer/verification, recovery and episode recording, tests and evaluation separation.
- Plausible first-party paths checked: separate affordance checking calls, whole-task final visual check, sensor contradiction and replayable logs.
- Why no material first-party path remains: these are routine production validation or stored evidence; no materially independent complementary audit judgment with corrective return is wired to the assessed organization.

## S4 — Outside-and-then intelligence

- State: —
- Function: no external-and-prospective capability adaptation loop established.
- Disturbance / variety regulated: live scene changes and task-specific calibration remain present operational variety.
- Decisive decision or feedback right: adapt the current action/plan to the observed task.
- Decision owner: operational VLM; offline model/data selection remains developer work outside this runtime.
- Supporting / enforcement mechanisms: recent-move memory, video-reference briefs, action-effect tables and replanning.
- Closure path: feedback changes this rollout's actions, not a future-environment capability option returned into current regulation.
- Why this is / is not agent-owned: learning a task's action effects or following a video is insufficient for the specific S4 function.
- Evidence: [video reference](https://github.com/showlab/Show-Harness/blob/6ad77dbc6180e973dff8148ffcca6c085580cea2/plugins/video_ref/plugin.py), [action ablation](https://github.com/showlab/Show-Harness/blob/6ad77dbc6180e973dff8148ffcca6c085580cea2/plugins/action_ablation/plugin.py), [deepplan](https://github.com/showlab/Show-Harness/blob/6ad77dbc6180e973dff8148ffcca6c085580cea2/plugins/deepplan/plugin.py).
- Basis: structural.
- Confidence: medium-high.
- Caveats: offline training results do not supply deployed adaptation ownership.

### Absence scope

- Surfaces inspected: planning/replanning, memory, reference-video, action-ablation and deepplan plugins, training/trajectory boundary and operator controls.
- Plausible first-party paths checked: reference analysis, calibration, internal learning, model configuration and human-driven training changes.
- Why no material first-party path remains: shipped paths select current manipulation responses or offline assets; none closes external prospective inquiry → capability option → authoritative present-capability change, autonomously or through a first-party parent mode.

## S5 — Policy and identity

- State: —
- Function: no runtime identity/ultimate-policy decision-return loop established.
- Disturbance / variety regulated: configured safety and action bounds constrain manipulation.
- Decisive decision or feedback right: operator chooses task, backend, rig limits and intervention actions.
- Decision owner: operator/developer configuration; not an evidenced function-specific S5 arrangement.
- Supporting / enforcement mechanisms: prompts, allowed-token schemas, safety floors, configuration layering and interruption.
- Closure path: direct constraint execution; no identity-level issue referral and authoritative return.
- Why this is / is not agent-owned: action discretion is bounded by policy but does not own ultimate policy.
- Evidence: [configuration](https://github.com/showlab/Show-Harness/blob/6ad77dbc6180e973dff8148ffcca6c085580cea2/core/config.py), [launch](https://github.com/showlab/Show-Harness/blob/6ad77dbc6180e973dff8148ffcca6c085580cea2/core/launch.py), [DAgger](https://github.com/showlab/Show-Harness/blob/6ad77dbc6180e973dff8148ffcca6c085580cea2/plugins/dagger/plugin.py).
- Basis: structural.
- Confidence: medium-high.
- Caveats: operator authority exists without qualifying runtime S5 closure.

### Absence scope

- Surfaces inspected: runtime prompts/configuration, plugin assembly, action schemas, safety/interruption and public operating documentation.
- Plausible first-party paths checked: task authority, policy configuration, hard limits, optional human override and repository governance.
- Why no material first-party path remains: no shipped identity/ultimate-policy issue → legitimate authority → decision returned → later operation path exists; repository maintenance is adjacent.

## Distributed OSS parent arrangement

Maintainers govern the source project. No project-level parent S3/S4/S5 arrangement is borrowed into each robot rollout from contributor activity.

## Self-hosted and non-human modes

Self-hosted robots and simulation use configured models and limits. DAgger supports direct human manipulation intervention; this is not automatically a parent metasystem mode.

## Recursion

Two arm tracks have distinct operational contributions and coordination, but no complete local metasystems are evidenced for recursive viability.

## Variety and escalation

Images, proprioception and histories expose task variety. Token schemas, step caps and safety floors attenuate execution variety; failed grounding/grasping returns to operational correction. Interruptions remain operator controls, not automatically algedonic channels.

## Evidence gaps

This source-based assessment does not validate physical execution, provider quality, robot safety or public benchmark results. Hardware, checkpoints and model endpoints were not run. Those limitations do not obscure the cited shipped wiring; no unresolved in-boundary S-function path is claimed as established.

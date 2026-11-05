---
harness_id: uni-robot-agent
project_name: Uni Robot Agent
repository: https://github.com/Open-RUA/uni-robot-agent
review_ref: 2590ab48b7c24a72123597f2d5b04c9524e4329c
reviewed_at: 2026-11-05
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Uni Robot Agent

## Review boundary

- System in focus: one installed `uni-robot-agent` robotic-task episode with a configured Codex or Claude Code agent, first-party robot tool/execution/session orchestration and its supported Direct or RoboDojo Hybrid action mode.
- Purpose and identity: translate a human-specified physical task and live robot/environment observations into bounded robot tool choices, actuation and feedback, while preserving traceable episode outcomes.
- Relevant environment: RoboDojo, RoboUse or RoboLab simulation/robot backends, physical arm constraints, camera observations, tool/model endpoints, changing scene geometry, uncertain execution acknowledgements and the operator's task instructions.
- Standard-distribution boundary: Python package and CLI with shipped session assembly, agent SDK adapters, shared gripper/scene/skill/episode tools, resource scheduler and opt-in Hybrid Pi0.5 actor/reviewer path; model providers, Codex/Claude SDK implementations, native robot services and optional learned action models are dependencies, not separately credited first-party departments.
- Credited operating / distribution surfaces: [architecture and supported modes](https://github.com/Open-RUA/uni-robot-agent/blob/2590ab48b7c24a72123597f2d5b04c9524e4329c/docs/architecture.md), [session assembly and agent invocation](https://github.com/Open-RUA/uni-robot-agent/blob/2590ab48b7c24a72123597f2d5b04c9524e4329c/uni_robot_agent/session.py), [Codex adapter](https://github.com/Open-RUA/uni-robot-agent/blob/2590ab48b7c24a72123597f2d5b04c9524e4329c/uni_robot_agent/agents/codex/agent.py), [Claude SDK adapter](https://github.com/Open-RUA/uni-robot-agent/blob/2590ab48b7c24a72123597f2d5b04c9524e4329c/uni_robot_agent/agents/claude_code/agent.py), [Hybrid action-runner/reviewer wiring](https://github.com/Open-RUA/uni-robot-agent/blob/2590ab48b7c24a72123597f2d5b04c9524e4329c/uni_robot_agent/integrations/gripper.py).
- Adjacent first-party surfaces excluded from ownership: paper/evaluation scoring and benchmark tasks, packaged simulator setup and borrowed native dependencies, action-model training, offline SFT/trajectory exports, test fixtures, GitHub release CI, and the project's developer/maintainer governance.
- First-party operating / deployment modes considered: `run` and interactive TUI; Codex/Claude adapters; Direct operation; `--action-profile hybrid` with a Pi0.5 action model and enabled/disabled separate VLA reviewer; default background or immediate tool returns; per-resource or global-serial scheduling; opt-in skill writing and observer snapshots.
- Recursion level: the installed robotic-task harness and its bounded episode, not the whole robotics lab, external model vendor, independently hosted simulator or its development organization.
- Reviewed revision: `2590ab48b7c24a72123597f2d5b04c9524e4329c`.
- Observation date: 2026-11-05.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The CLI validates an explicit integration, assembles `PreparedEpisodeSession` and the effective prompt, then runs either a Codex or Claude Code SDK agent with the repository's registered MCP/in-process robot tools. An agent repeatedly selects scene, motion, skill and completion tools; first-party `ToolExecutor`, resource scheduler and environment adapters execute requests, return typed observations and update one episode. `finish` asks to end the episode but deliberately does not disclose the task verifier's success verdict to the agent. Background tools return handles; physically exclusive operations are serialized by resource to prevent overlapping actuation. [Architecture](https://github.com/Open-RUA/uni-robot-agent/blob/2590ab48b7c24a72123597f2d5b04c9524e4329c/docs/architecture.md); [session](https://github.com/Open-RUA/uni-robot-agent/blob/2590ab48b7c24a72123597f2d5b04c9524e4329c/uni_robot_agent/session.py); [scheduler](https://github.com/Open-RUA/uni-robot-agent/blob/2590ab48b7c24a72123597f2d5b04c9524e4329c/uni_robot_agent/execution/scheduler.py).

RoboDojo Hybrid additionally exposes `actor_act`: a Pi0.5 backend proposes a bounded action chunk, the first-party `ChunkReviewer` optionally uses a separate model call over current camera images, measured state and proposed trajectory/FK checks, and `ActorRunner` executes, corrects or withholds the chunk according to that verdict. The reviewer sees more than the VLA's own proposal and can return `student`, `edit`, `eef` or `stop`, changing physical execution and later feedback. The reviewer is supported in this shipped mode but requires an explicitly configured compatible model endpoint and credential. [Hybrid wiring](https://github.com/Open-RUA/uni-robot-agent/blob/2590ab48b7c24a72123597f2d5b04c9524e4329c/uni_robot_agent/integrations/gripper.py); [review model](https://github.com/Open-RUA/uni-robot-agent/blob/2590ab48b7c24a72123597f2d5b04c9524e4329c/uni_robot_agent/tools/gripper/reviewer.py); [actor runner](https://github.com/Open-RUA/uni-robot-agent/blob/2590ab48b7c24a72123597f2d5b04c9524e4329c/uni_robot_agent/tools/gripper/actor.py).

## Operational model

The task agent is the operational decision-maker: it interprets tool feedback and chooses next robot-use actions. The repository supplies the bounded action surface and actual feedback loop; the SDK/provider supplies inference. In Hybrid, a subordinate learned action model proposes fine-grained motor actions but does not own the higher-level task objective, while the separate optional reviewer has a specifically bounded corrective judgment over those proposed chunks. The environment and scheduler enforce state/version/resource constraints. Operator instruction, model selection and activation of reviewer/skill-writing modes are configuration decisions, not automatically S3/S4/S5.

## S1 — Operations

- State: A
- Function: autonomous task execution through repeated robot observation, tool/action choice and resulting environmental feedback.
- Disturbance / variety regulated: changing object poses, grasp failures, occluded views, tool errors, unavailable resources and differences between expected and measured effects.
- Decisive decision or feedback right: the configured coding-agent model chooses which available robot tool to call, with what arguments, whether to inspect/recover and when to request `finish`.
- Decision owner: model-backed Codex/Claude task agent in the shipped `run`/TUI session; the SDK and provider implement its inference, while the first-party harness wires its decisions to robots.
- Supporting / enforcement mechanisms: first-party MCP/Claude tool adapters, shared `Episode`, resource executor, snapshots, action-size bounds, state-version checks, receipts, time/step budgets and structured feedback.
- Closure path: task instruction and scene → model chooses a registered tool → executor/environment performs or rejects a bounded action → result, image and updated state return into the agent's next decision → task continues or finishes.
- Boundary reachability: `session.py` actually selects and invokes a packaged Codex/Claude adapter with registered tools; no separate operator-authored control program is necessary after starting the supported model-backed episode.
- Why this is / is not agent-owned: the agent has genuine contextual discretion among actions and recovery steps; deterministic guards and robot services restrict or carry out those choices but cannot replace the agent's task decisions.
- Evidence: [main run cycle](https://github.com/Open-RUA/uni-robot-agent/blob/2590ab48b7c24a72123597f2d5b04c9524e4329c/uni_robot_agent/session.py), [Claude SDK run and tool interaction](https://github.com/Open-RUA/uni-robot-agent/blob/2590ab48b7c24a72123597f2d5b04c9524e4329c/uni_robot_agent/agents/claude_code/agent.py), [Codex SDK run](https://github.com/Open-RUA/uni-robot-agent/blob/2590ab48b7c24a72123597f2d5b04c9524e4329c/uni_robot_agent/agents/codex/agent.py), [tool/episode flow](https://github.com/Open-RUA/uni-robot-agent/blob/2590ab48b7c24a72123597f2d5b04c9524e4329c/docs/architecture.md).
- Basis: structural code and explicit shipped run documentation; no live model-provider run was claimed in this review.
- Confidence: high for the supported agent-to-tool/feedback decision path; physical task success remains unverified here.
- Caveats: the model/SDK must be installed and configured; such dependencies do not make the first-party integrated agent path merely a non-agentic tool library.

## S2 — Coordination

- State: —
- Function: no distinct inter-S1 conflict-attenuation relation was established at the declared episode recursion.
- Disturbance / variety regulated: concurrent motion/tool calls can conflict over an arm, an episode or its state version, but the reviewed paths serialize tools of one task-agent's execution rather than reconcile distinct autonomous S1 units.
- Decisive decision or feedback right: configured FIFO resource placement and immutable-snapshot rules govern tool execution; no first-party autonomous inter-S1 adjustment choice was found.
- Decision owner: deterministic scheduler/developer configuration, not an S2 agent decision owner.
- Supporting / enforcement mechanisms: `ToolExecutionPolicy`, per-resource exclusive queues, background job handles, global-serial option and SDK subagent support.
- Closure path: incompatible calls wait for a resource and receive completion feedback, but this is intra-episode execution safety, not a separately evidenced cross-S1 coordination conversation.
- Why this is / is not agent-owned: SDK-native subagents and two physical arms do not by themselves establish two organizational S1 units with their own outcomes and a specific reciprocal disturbance.
- Evidence: [scheduling and resource semantics](https://github.com/Open-RUA/uni-robot-agent/blob/2590ab48b7c24a72123597f2d5b04c9524e4329c/docs/architecture.md), [scheduler](https://github.com/Open-RUA/uni-robot-agent/blob/2590ab48b7c24a72123597f2d5b04c9524e4329c/uni_robot_agent/execution/scheduler.py), [agent adapter boundaries](https://github.com/Open-RUA/uni-robot-agent/blob/2590ab48b7c24a72123597f2d5b04c9524e4329c/uni_robot_agent/agents/claude_code/agent.py).
- Basis: bounded negative inspection of shipped robot-tool and agent delegation modes.
- Confidence: medium-high at the episode boundary.
- Caveats: a separate multi-robot or multi-agent deployment might establish S2, but that composition is not inferred from SDK capability.

### Absence scope

- Surfaces inspected: execution scheduler/policies, session and tool assembly, direct/Hybrid action paths and SDK-provided subagent hooks.
- Plausible first-party paths checked: conflicting arm motions, overlapping tool calls, parallel SDK workers and shared episode state.
- Why no material first-party path remains: their shown closure prevents internal tool-state corruption; no separate S1 units plus conflict-specific reciprocal adjustment/feedback relation are packaged at this recursion.

## S3 — Inside-and-now control

- State: —
- Function: no independent whole-system current-control owner over multiple S1 commitments/resources was established.
- Disturbance / variety regulated: running time, token/tool limits, physical safety, stale observations and missed action acknowledgements are regulated locally within an episode.
- Decisive decision or feedback right: operator/developer selects budgets and modes; runtime rejects/queues/cancels actions according to those constraints, while the task agent chooses local work.
- Decision owner: configuration/episode executor, not a distinct metasystem owner with current whole-system bargaining discretion.
- Supporting / enforcement mechanisms: timeout, step limit, resource queues, receipts, cancellation and TUI/CLI status.
- Closure path: bounded local execution and failures feed the same agent's continuation; no portfolio-level current resource decision returns to several operational units.
- Why this is / is not agent-owned: calling the executor a controller does not establish S3; it does not independently allocate/revise commitments across an operational whole.
- Evidence: [session lifecycle](https://github.com/Open-RUA/uni-robot-agent/blob/2590ab48b7c24a72123597f2d5b04c9524e4329c/uni_robot_agent/session.py), [scheduler](https://github.com/Open-RUA/uni-robot-agent/blob/2590ab48b7c24a72123597f2d5b04c9524e4329c/uni_robot_agent/execution/scheduler.py), [architecture](https://github.com/Open-RUA/uni-robot-agent/blob/2590ab48b7c24a72123597f2d5b04c9524e4329c/docs/architecture.md).
- Basis: bounded absence review of implemented execution-control and user modes.
- Confidence: medium-high.
- Caveats: parent human instructions and operational safety guards are real, but neither automatically closes S3 at this recursion.

### Absence scope

- Surfaces inspected: CLI/config, session lifecycle, scheduling, tool execution, robot integrations and TUI controls.
- Plausible first-party paths checked: budgets, interrupts, resource arbitration, episode management and optional reviewer decisions.
- Why no material first-party path remains: these regulate a single agent/episode or a subordinate action prefix, without whole-system current visibility and a return of resource/commitment choices across distinguishable S1 units.

## S3* — Complementary audit

- State: A
- Function: an opt-in independently prompted model checks a subordinate VLA's proposed motor-action chunk against current raw observations, measured state and expected task progress, then can require a correction or stop before execution.
- Disturbance / variety regulated: the Pi action model can propose an unsafe, geometrically misaligned or already-completed prefix despite producing a normal-looking trajectory.
- Decisive decision or feedback right: reviewer model selects `student`, `edit`, `eef` or `stop`, number of steps, reason and continuation after judging the proposal and physical evidence; `ActorRunner` uses this decision to execute, modify or withhold the proposed chunk.
- Decision owner: the separately invoked VLA reviewer model in supported RoboDojo Hybrid reviewer-enabled mode; deterministic validation/bounds constrain, but do not choose, its evaluative verdict.
- Supporting / enforcement mechanisms: fresh camera capture, measured state and FK proposal, separate reviewer prompt/Responses call, structured validator, chunk archive, bounded correction commands and execution receipts.
- Closure path: Pi proposes action prefix → independent reviewer receives proposal plus raw/derived observation → reviewer returns corrective or stop judgment → `ActorRunner` changes executed commands or halts → actual feedback and previous review enter the next chunk or higher-level task agent.
- Boundary reachability: the shipped `--action-profile hybrid` path constructs `ChunkReviewer` by default when binding supports it, requires an explicit Responses-compatible endpoint, and calls its `decide` before any chunk execution. It is not a paper-only evaluator or an uninstalled CI process.
- Why this is / is not agent-owned: the reviewer can counter the subordinate actor's suggestion with independent discretionary evidence assessment and corrective action; it is not simply a deterministic success flag. This is **mode-specific** and cannot be generalized to Direct mode or to unconfigured endpoints.
- Claim being audited: the proposed VLA action is aligned with current physical observations, task intent and local progress, and its continuation is warranted.
- Ordinary reporting path: VLA proposal/trajectory and main task agent's instruction/task-progress report.
- Complementary access path: separately prompted reviewer model sees raw head/wrist camera images, measured pose/FK checks, native feedback and prior reviewer context before command commitment.
- Independence boundary: the VLA does not choose or edit the review verdict; the reviewer call has distinct prompt/context and can veto/correct, although the same provider/model family may be configured and both remain inside one product's action path.
- Who acts on findings: `ActorRunner` applies `stop`, altered command prefixes or continued student actions; the main agent receives final tool feedback for its next choice.
- Evidence: [reviewer decision model](https://github.com/Open-RUA/uni-robot-agent/blob/2590ab48b7c24a72123597f2d5b04c9524e4329c/uni_robot_agent/tools/gripper/reviewer.py), [source-grounded reviewer prompt](https://github.com/Open-RUA/uni-robot-agent/blob/2590ab48b7c24a72123597f2d5b04c9524e4329c/uni_robot_agent/resources/prompts/actor/robodojo_vla_decision.md), [execution after verdict](https://github.com/Open-RUA/uni-robot-agent/blob/2590ab48b7c24a72123597f2d5b04c9524e4329c/uni_robot_agent/tools/gripper/actor.py), [reviewer enablement](https://github.com/Open-RUA/uni-robot-agent/blob/2590ab48b7c24a72123597f2d5b04c9524e4329c/uni_robot_agent/integrations/gripper.py).
- Basis: structural first-party review/judgment and actuation-return wiring; no separate provider E2E was performed.
- Confidence: medium for materially complementary access, high for the executable verdict-to-command decision path.
- Caveats: no assurance of model reliability or institutionally independent review follows. Hybrid requires a model endpoint, action checkpoint and integration. This state credits the installed **optional** reviewer path, not routine task success checks or offline evaluation.

## S4 — Outside-and-then intelligence

- State: —
- Function: no demonstrated first-party outside-and-prospective option-selection conversation returning to current whole-episode capability was established.
- Disturbance / variety regulated: future environments, robot geometries and repeated failures could motivate improved skills or action models.
- Decisive decision or feedback right: `write_skill` optionally lets the task agent store an observed lesson in an operator-configured external library; developers choose model/integration updates. Neither shows a separate established future-environment intelligence and S3 adaptation loop.
- Decision owner: task agent owns local lesson text when enabled; operator/developer chooses whether/how to reuse broader configuration and model improvements.
- Supporting / enforcement mechanisms: opt-in skill-writing, read/list skill tools, prompt guidance that requires evidence and narrow transfer, saved traces and optional SFT export.
- Closure path: a verified task lesson may be stored for a later run, but review found no first-party prospective external-option decision with a defined whole-system capability adoption/return path; ordinary memory reuse is not sufficient.
- Why this is / is not agent-owned: experience preservation can alter later task context, but it is not by itself S4's external-and-then intelligence conversation.
- Evidence: [skill-writing implementation](https://github.com/Open-RUA/uni-robot-agent/blob/2590ab48b7c24a72123597f2d5b04c9524e4329c/uni_robot_agent/tools/skills.py), [lesson instructions](https://github.com/Open-RUA/uni-robot-agent/blob/2590ab48b7c24a72123597f2d5b04c9524e4329c/uni_robot_agent/resources/prompts/guides/meta_skill.md), [architecture's optional skill mode](https://github.com/Open-RUA/uni-robot-agent/blob/2590ab48b7c24a72123597f2d5b04c9524e4329c/docs/architecture.md).
- Basis: bounded negative review distinguishing operational experience from prospective environmental adaptation.
- Confidence: medium; externally oriented future modes may be added later.
- Caveats: this does not deny useful cross-run skill improvement or possible future S4 constructor work.

### Absence scope

- Surfaces inspected: bundled skill library, read/write skill tooling and prompt, session opt-in, provider and action-model integrations, artifacts/SFT and architecture.
- Plausible first-party paths checked: persistent experience, future-run skill loading, model/action adaptation and simulator/environment selection.
- Why no material first-party path remains: evidenced paths are local task-reuse or developer-selected upgrades; no closed externally prospective options-to-current-whole-system-capability regulatory loop is shipped.

## S5 — Policy and identity

- State: —
- Function: no legitimate runtime identity/ultimate-policy issue-to-authority-to-operation loop was established.
- Disturbance / variety regulated: conflicts over robot-task safety, data/model choice, user purpose and deployment policy could raise higher-level identity questions, but these remain outside the reviewed episode governance.
- Decisive decision or feedback right: a user chooses task/mode/constraints; first-party runtime enforces tool permissions and safety bounds, without a distinct S5 deliberation/return path.
- Decision owner: external human/project authority for product identity; task-local model/guard machinery does not own ultimate policy.
- Supporting / enforcement mechanisms: CLI configuration, model/tool permissions, tool restrictions, explicit finish acknowledgement and environment safety state.
- Closure path: configuration constrains next actions and safety checks reject disallowed movement; no observed identity dispute is escalated to a legitimate parent and returned as a revised binding ultimate policy.
- Why this is / is not agent-owned: human task instructions and deterministic safety policy do not become autonomous or parent-governed S5 merely because they are authoritative for one episode.
- Evidence: [configuration](https://github.com/Open-RUA/uni-robot-agent/blob/2590ab48b7c24a72123597f2d5b04c9524e4329c/uni_robot_agent/config.py), [run structure](https://github.com/Open-RUA/uni-robot-agent/blob/2590ab48b7c24a72123597f2d5b04c9524e4329c/docs/architecture.md), [episode and tools](https://github.com/Open-RUA/uni-robot-agent/blob/2590ab48b7c24a72123597f2d5b04c9524e4329c/uni_robot_agent/session.py).
- Basis: bounded negative inspection of runtime control, human interaction and governance scope.
- Confidence: medium-high at the declared episode boundary.
- Caveats: the external robotics organization may possess its own S5; it is not part of this first-party deployed harness by repository adjacency.

### Absence scope

- Surfaces inspected: README, architecture, CLI/config, agent adapters, session/runtime, prompts and tool permissions.
- Plausible first-party paths checked: task instruction changes, model selection, skill-writing policy, operator abort and physical safety exceptions.
- Why no material first-party path remains: these are task/current-control or developer configuration choices; no shipped identity-policy adjudication, legitimate parent return or autonomous ultimate charter revision exists at the specified recursion.

## Distributed OSS parent arrangement

This is a redistributable robot-use harness, not an assessed OSS contributor organization. Maintainers and arbitrary local robot operators do not become a shared organizational S5 merely through use of the same package. Local task/mode selections are bounded parent inputs, not demonstrated identity-governance closure.

## Self-hosted and non-human modes

The operator chooses integrations, providers and optional reviewer/skill-writing modes. The reviewer-enabled Hybrid path has a first-party model-owned corrective decision loop independent of ordinary VLA proposal generation; disabling it removes that particular S3* path. No parent-governed S3/S4/S5 multi-mode notation is assigned from an operator's mere ability to configure, cancel or approve actions.

## Recursion

One episode can use a high-level task agent, optional subagent helpers and a subordinate Pi action model, but SDK spawning and actuator decomposition do not demonstrate independently viable recursive organizations. The declared assessment is the one task harness and its immediate robot environment.

## Variety and escalation

Camera/proprioceptive observations, tool feedback and model tool selection amplify local response variety; shared schemas, physical limits, resource exclusivity, episode versions, review corrections and task step budgets attenuate unsafe or stale actions. Uncertain physical ACKs are reconciled rather than blindly replayed. Task-agent uncertainty can lead to more observation or abort; explicit higher-level organizational escalation or algedonic authority is not inferred from error/stop signals.

## Evidence gaps

- This review inspected the exact pinned source and operating documents, but did not operate a real robot, launch a paid coding-agent model or execute Pi0.5/reviewer inference; the classifications are source-wiring claims, not independent physical-performance attestations.
- Reviewer quality/independence from a configured high-level model or provider varies by operator; the structural S3* claim is limited to the separately prompted Pi-proposal audit path, not all safety/quality checks.
- Optional skill writing plausibly improves future episodes, but evidence does not close a distinct external/prospective S4 adaptation conversation rather than task-local experiential memory.

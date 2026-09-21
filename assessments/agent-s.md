---
harness_id: agent-s
project_name: Agent S
repository: https://github.com/simular-ai/Agent-S
review_ref: 3aa272d23d2994c7bbde1acbbe0ef8e8d06b8693
reviewed_at: 2026-09-19
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Agent S

## Review boundary

- System in focus: the first-party Agent S3 computer-use runtime shipped by `gui-agents` at pinned revision `3aa272d23d2994c7bbde1acbbe0ef8e8d06b8693`, centered on `AgentS3`, its `Worker`, grounding/action interface, task-local reflection path, and optional local `CodeAgent` execution path.
- Purpose and identity: accept a natural-language computer-use task, observe a desktop GUI, choose and execute actions, and use subsequent screen/environment feedback to continue the task until completion/failure or the enclosing step bound is reached.
- Relevant environment: the user's desktop and applications, screenshots, GUI state, optional local Python/Bash execution environment, configured model/grounding endpoints, and the user-supplied task.
- Standard-distribution boundary: the installable `gui-agents` package and its `agent_s=gui_agents.s3.cli_app:main` entrypoint, plus first-party Agent S3 modules reachable from that runtime. External model providers, grounding services, desktop applications, OpenClaw itself, and the hosted Sai product are outside the credited ownership boundary.
- Credited operating / distribution surfaces: `gui_agents/s3/cli_app.py`; `gui_agents/s3/agents/agent_s.py`; `gui_agents/s3/agents/worker.py`; `gui_agents/s3/agents/grounding.py`; the optional `gui_agents/s3/agents/code_agent.py` path when the local environment is enabled; S3 procedural-memory prompts used by those runtime components.
- Adjacent first-party surfaces excluded from ownership: historical `gui_agents/s1`, `gui_agents/s2`, and `gui_agents/s2_5` generations; `osworld_setup/**`, `evaluation_sets/**`, WindowsAgentArena setup and other benchmark/evaluation runners; S3 Behavior Best-of-N (`bbon`) post-hoc rollout judging because the documented ordinary CLI explicitly runs S3 without bBoN; repository tests/CI; and `integrations/openclaw/**`, which adapts Agent S for an externally owned OpenClaw parent runtime rather than making OpenClaw part of Agent S itself.
- First-party operating / deployment modes considered: ordinary `agent_s` CLI execution with reflection enabled by default; the same CLI with reflection disabled; optional local coding environment; direct Python construction of `AgentS3`; the OpenClaw wrapper only as an adjacent integration check, not as a credited Agent S organizational parent.
- Recursion level: one Agent S3 task-execution organization. The model-driven Worker is the primary S1 operational actor at this boundary. Grounding/text helpers are support services, and the optional CodeAgent is a bounded delegated execution branch rather than a separately evidenced viable recursive organization.
- Reviewed revision: `3aa272d23d2994c7bbde1acbbe0ef8e8d06b8693`.
- Observation date: 2026-09-19.
- Generated Profile version: `0.2.3`.
- Generated Methodology version: `0.3.5`.
- Current Profile version: `0.2.3`.
- Current Methodology version: `0.3.5`.

## Repository architecture

Agent S contains several historical implementation generations, but the pinned package metadata makes the current distribution boundary explicit: version `0.3.2` installs the console entrypoint `agent_s=gui_agents.s3.cli_app:main`. The top-level README likewise describes Agent S3 as the current third-generation open-source computer-use framework and documents the ordinary CLI as Agent S3 without Behavior Best-of-N. Historical S1/S2/S2.5 directories therefore remain useful implementation context but are not silently combined with the current S3 runtime to create organizational functions that the shipped entrypoint no longer exposes.

The current `AgentS3` wrapper deliberately removes the earlier hierarchy: its source describes it as using “no hierarchy for less inference time,” creates one `Worker`, and delegates each `predict()` call to that worker. The worker owns the live model/action loop. On each step it receives the current screenshot, optionally generates a reflection over the preceding trajectory, inserts that reflection and any returned CodeAgent result into the generator context, asks the model for the next action, parses the result, and produces executable GUI action code. The CLI then executes the action, takes another screenshot, and feeds the changed environment back into the next prediction.

Reflection is therefore a task-local feedback mechanism inside the same operational trajectory rather than an independent audit organization. It is built from the same instruction, worker action history, and current screenshot, and its output is advisory context for the Worker’s next action. The optional `CodeAgent` is similarly bounded: the main Worker can invoke it for a coding task/subtask when a local controller exists; the CodeAgent runs its own finite model→Python/Bash→result loop and returns a completion reason, history, and summary to the Worker. This is substantive delegated execution, but the current distribution does not supply a distinct inter-S1 coordination function around Worker and CodeAgent.

The repository also contains S3 Behavior Best-of-N components that compare saved rollout result directories using fact captions and initial/final screenshots. That evaluator can select one completed trajectory, but the documented ordinary CLI explicitly excludes bBoN and no first-party live return path from that post-hoc benchmark selection into the running Agent S3 trajectory is established at the assessed boundary. It is therefore adjacent evaluation evidence, not S3* ownership for the standard runtime.

Primary evidence:

- [`setup.py`](https://github.com/simular-ai/Agent-S/blob/3aa272d23d2994c7bbde1acbbe0ef8e8d06b8693/setup.py) — package version and the shipped `agent_s=gui_agents.s3.cli_app:main` console entrypoint.
- [`README.md`](https://github.com/simular-ai/Agent-S/blob/3aa272d23d2994c7bbde1acbbe0ef8e8d06b8693/README.md) — current Agent S3 identity, installation/CLI boundary, reflection/local-env options, and explicit note that ordinary CLI operation is without bBoN.
- [`gui_agents/s3/agents/agent_s.py`](https://github.com/simular-ai/Agent-S/blob/3aa272d23d2994c7bbde1acbbe0ef8e8d06b8693/gui_agents/s3/agents/agent_s.py) — hierarchy-free `AgentS3` wrapper and single Worker construction.
- [`gui_agents/s3/agents/worker.py`](https://github.com/simular-ai/Agent-S/blob/3aa272d23d2994c7bbde1acbbe0ef8e8d06b8693/gui_agents/s3/agents/worker.py) — current task/action loop, reflection feedback, optional CodeAgent-result return, action generation and trajectory state.
- [`gui_agents/s3/agents/grounding.py`](https://github.com/simular-ai/Agent-S/blob/3aa272d23d2994c7bbde1acbbe0ef8e8d06b8693/gui_agents/s3/agents/grounding.py) — GUI action interface, grounding helpers and the optional `call_code_agent` delegation surface.
- [`gui_agents/s3/agents/code_agent.py`](https://github.com/simular-ai/Agent-S/blob/3aa272d23d2994c7bbde1acbbe0ef8e8d06b8693/gui_agents/s3/agents/code_agent.py) — bounded delegated code-execution loop and return result.
- [`gui_agents/s3/cli_app.py`](https://github.com/simular-ai/Agent-S/blob/3aa272d23d2994c7bbde1acbbe0ef8e8d06b8693/gui_agents/s3/cli_app.py) — screenshot→predict→execute runtime loop, user task entry, pause/quit debug path and optional local environment.
- [`gui_agents/s3/bbon/comparative_judge.py`](https://github.com/simular-ai/Agent-S/blob/3aa272d23d2994c7bbde1acbbe0ef8e8d06b8693/gui_agents/s3/bbon/comparative_judge.py) — post-hoc comparison/selection over stored rollout directories, inspected as an adjacent S3* candidate.
- [`gui_agents/s3/memory/procedural_memory.py`](https://github.com/simular-ai/Agent-S/blob/3aa272d23d2994c7bbde1acbbe0ef8e8d06b8693/gui_agents/s3/memory/procedural_memory.py) — static first-party procedural prompts, inspected as a possible S4 path.
- [`integrations/openclaw/README.md`](https://github.com/simular-ai/Agent-S/blob/3aa272d23d2994c7bbde1acbbe0ef8e8d06b8693/integrations/openclaw/README.md) — downstream wrapper by which an external OpenClaw agent can invoke Agent S, inspected but excluded from Agent S-owned higher-function closure.

## Operational model

A user supplies a task and model/grounding configuration. During execution, the Worker is the substantive task actor: it sees the latest GUI observation plus its trajectory context, decides what to do next through the configured generation model, and emits an action that the first-party runtime translates into executable GUI control. The environment changes, a new screenshot is captured, and that returned observation informs the next decision. Reflection can critique the immediately preceding trajectory inside the same loop. When enabled and available, the Worker can also delegate a coding task/subtask to CodeAgent and incorporate the returned execution record into later decisions.

This architecture is enough for autonomous S1 ownership. It does not, on the pinned current S3 boundary, establish a metasystem above multiple independent S1 units. In particular, the repository's historical “manager” implementations are not imported into S3 simply because they remain in the source tree, and neither reflection nor CodeAgent delegation is upgraded into S2/S3 without a function-specific disturbance and decision right.

## S1 — Operations

- State: A
- Function: perform the requested computer-use transformation by observing the GUI, choosing the next task action, executing it through the first-party action interface, and continuing from returned environment state.
- Disturbance / variety regulated: changing screen/application state, task-local uncertainty, action outcomes, tool/UI failures, prior trajectory context and, when enabled, returned local code-execution results.
- Decisive decision or feedback right: choose the next substantive GUI/task action from the current instruction, screenshot and trajectory feedback.
- Decision owner: the model-driven Agent S3 `Worker` operating inside the first-party `AgentS3` runtime.
- Supporting / enforcement mechanisms: `AgentS3.predict`, Worker history, task-local reflection, grounding/text-coordinate services, action format validation/parsing, pyautogui action generation, CLI screenshot/execute loop, and optional CodeAgent delegation.
- Closure path: user task + current screenshot → Worker/model chooses a next action → Agent S converts the action into executable GUI code → CLI executes it against the desktop → changed screen state is captured → the new observation and prior trajectory/reflection enter the next Worker decision.
- Boundary reachability: the shipped `agent_s` console entrypoint directly constructs `AgentS3` and runs this screenshot→prediction→execution loop; no downstream adopter must invent the operational feedback path.
- Why this is / is not agent-owned: deterministic parsing/grounding/runtime machinery constrains and executes actions, but the substantive next-action selection is made by the model-driven Worker from current environmental feedback rather than by a fixed script.
- Evidence: `setup.py`; `README.md`; `gui_agents/s3/agents/agent_s.py`; `gui_agents/s3/agents/worker.py`; `gui_agents/s3/cli_app.py`; `gui_agents/s3/agents/grounding.py`.
- Basis: explicit + structural
- Confidence: high
- Caveats: external model and grounding providers remain execution dependencies, not credited first-party organizational owners. The optional CodeAgent can perform a bounded delegated coding subtask, but that does not change the primary S1 ownership claim.

## S2 — Coordination

- State: —
- Function: no distinct first-party S2 coordination function is established at the current Agent S3 runtime boundary.
- Disturbance / variety regulated: no concrete interference, oscillation or conflict among two or more independently acting S1 units is established for the shipped S3 mode.
- Decisive decision or feedback right: no S2-specific right to attenuate an evidenced inter-S1 disturbance is supplied.
- Decision owner: not established.
- Supporting / enforcement mechanisms: Worker→CodeAgent task/subtask delegation, task-local reflection, grounding/text helpers and sequential CLI execution were inspected but do not themselves constitute inter-S1 regulation.
- Closure path: not applicable; the current runtime closes one primary Worker trajectory and optional subordinate delegation rather than a coordination loop among distinct S1s.
- Why this is / is not agent-owned: the S2 function is not established before autonomy classification. `AgentS3` explicitly removes hierarchy, and neither a delegated CodeAgent nor a reflection helper provides the required inter-S1 disturbance/attenuation/feedback witness.
- Evidence: `gui_agents/s3/agents/agent_s.py`; `gui_agents/s3/agents/worker.py`; `gui_agents/s3/agents/code_agent.py`; `gui_agents/s3/agents/grounding.py`; package entrypoint in `setup.py`.
- Basis: explicit + structural
- Confidence: high
- Caveats: historical S1/S2 generations contain manager/worker structures, but they are not the current shipped `agent_s` entrypoint and are excluded from credited S3 ownership.

### Absence scope

- Surfaces inspected: current S3 wrapper, Worker, CodeAgent, grounding/action layer, CLI/runtime entrypoint, package metadata, historical-generation layout and OpenClaw adapter boundary.
- Plausible first-party paths checked: historical hierarchy; Worker→CodeAgent subtask delegation; reflection; grounding/text helper agents; external OpenClaw invocation.
- Why no material first-party path remains: the current shipped runtime has one primary Worker and explicitly no hierarchy; the additional actors are bounded support/delegation paths, and no first-party S3 mode supplies the required multi-S1 disturbance plus attenuation relation and returned coordination feedback.

## S3 — Inside-and-now control

- State: —
- Function: no distinct whole-system current-control function is established above the one Agent S3 operational trajectory.
- Disturbance / variety regulated: current-task execution failures, step limits and CodeAgent budgets are handled within S1/runtime enforcement, not as whole-organization resource/commitment regulation.
- Decisive decision or feedback right: no actor is shown holding a whole-system current view plus discretionary authority over multiple S1 commitments, priorities, resources, accountability or intervention.
- Decision owner: not established.
- Supporting / enforcement mechanisms: the CLI's finite step loop, Worker trajectory state, CodeAgent budget, pause/quit debugging path and task completion/failure signals provide execution control but not an S3 organizational decision right.
- Closure path: not applicable; current state feeds the same Worker S1 or deterministic runtime termination rather than a separate S3 controller that returns portfolio-level decisions.
- Why this is / is not agent-owned: no S3 function is established before autonomy classification. An enclosing loop or numeric budget is enforcement, and the current S3 source intentionally lacks the manager hierarchy that might otherwise be investigated for a higher-recursion current-control actor.
- Evidence: `gui_agents/s3/agents/agent_s.py`; `gui_agents/s3/agents/worker.py`; `gui_agents/s3/cli_app.py`; `gui_agents/s3/agents/code_agent.py`.
- Basis: explicit + structural
- Confidence: high
- Caveats: a downstream parent such as OpenClaw may schedule/invoke Agent S, but that external organization requires its own assessment and cannot be credited as Agent S-owned S3.

### Absence scope

- Surfaces inspected: S3 wrapper and Worker state, CLI control loop, optional CodeAgent budget/termination, historical manager directories, OpenClaw integration.
- Plausible first-party paths checked: hierarchy/manager ownership, global task portfolio view, retry/resource reallocation, human/operator current-control, CodeAgent budget and external parent invocation.
- Why no material first-party path remains: the credited entrypoint executes one task trajectory, with only deterministic enclosing limits and task-local feedback; no first-party S3 actor combines organization-wide current state with discretionary current-control authority.

## S3* — Complementary audit

- State: —
- Function: no materially independent complementary audit loop is established in the credited Agent S3 operating mode.
- Disturbance / variety regulated: reflection can catch task-local mistakes and bBoN can compare completed rollouts, but neither establishes a qualifying independent audit-and-correction function for the standard live runtime.
- Decisive decision or feedback right: no first-party auditor in the credited mode is shown independently validating an ordinary operational claim through a materially separate evidence path and returning a binding/corrective finding into subsequent operation.
- Decision owner: not established.
- Supporting / enforcement mechanisms: Worker's reflection agent, ordinary screenshots/action history, stored bBoN rollout result directories, fact captions and comparative judge.
- Closure path: reflection advice returns inside the ordinary Worker trajectory; bBoN selects among already-produced rollout directories in an adjacent evaluation path. Neither establishes the required complementary-access audit closure at the declared runtime boundary.
- Why this is / is not agent-owned: the function is not established before autonomy classification. Reflection sees the same task instruction, prior Worker action history and current screenshot used by ordinary operation, while bBoN is explicitly outside the ordinary CLI and no live corrective return from its post-hoc selection is evidenced.
- Evidence: `gui_agents/s3/agents/worker.py`; `gui_agents/s3/bbon/comparative_judge.py`; `README.md`; `osworld_setup/s3/bbon/**` inspected as benchmark/evaluation support.
- Basis: explicit + structural
- Confidence: high
- Caveats: a composed benchmark or downstream application may use bBoN results as an independent selection/control mechanism, but that composed operating boundary is not the shipped ordinary Agent S3 runtime assessed here.

### Absence scope

- Surfaces inspected: reflection path, Worker trajectory/history, S3 bBoN comparative judge, OSWorld bBoN runners, README runtime boundary and result/logging paths.
- Plausible first-party paths checked: reflection-as-verifier, comparative trajectory judge, benchmark scoring, logs/screenshots as independent evidence, downstream corrective use of selected rollouts.
- Why no material first-party path remains: reflection lacks a materially independent complementary access path, and bBoN is a separated post-hoc evaluation/selection surface without an evidenced return into the ordinary live Agent S3 operation.

## S4 — Outside-and-then intelligence

- State: —
- Function: no distinct outside-and-then organizational intelligence/adaptation loop is established for Agent S3.
- Disturbance / variety regulated: current screenshots and task feedback regulate present execution; they are not a prospective model of the external environment used to adapt future Agent S capability.
- Decisive decision or feedback right: no first-party actor is shown generating a future-facing adaptation option from external change and installing/returning that option into current organizational capability.
- Decision owner: not established.
- Supporting / enforcement mechanisms: static procedural-memory prompts, current task trajectory, reflection, GUI observations, model/grounding configuration and benchmark/evaluation artifacts.
- Closure path: not applicable; current-task evidence changes later actions within the same S1 trajectory, while static prompts and benchmark results do not form a shipped prospective adaptation-and-return loop.
- Why this is / is not agent-owned: the S4 function is absent. Memory naming, reflection, external-screen perception and benchmark improvement claims do not by themselves establish future/environmental intelligence that changes the harness's subsequent capability.
- Evidence: `gui_agents/s3/memory/procedural_memory.py`; `gui_agents/s3/agents/worker.py`; `README.md`; S3 bBoN/evaluation surfaces.
- Basis: structural
- Confidence: high
- Caveats: maintainers can improve later releases from research/benchmark results, but repository development is adjacent human project evolution, not a first-party runtime S4 closure for the assessed organization.

### Absence scope

- Surfaces inspected: S3 procedural memory, Worker/reflection state, current GUI observation path, bBoN evaluation, README research/update material and historical generation directories.
- Plausible first-party paths checked: persistent/learned memory, self-improvement, post-run adaptation, benchmark-driven runtime modification, prospective environment scanning and automatic configuration/skill change.
- Why no material first-party path remains: the current S3 package supplies static procedural prompts and task-local context but no first-party external/prospective adaptation judgment whose returned decision changes future runtime capability.

## S5 — Policy and identity

- State: —
- Function: no first-party identity/ultimate-policy closure is established for the Agent S3 organization.
- Disturbance / variety regulated: user task choice, provider/model/grounding configuration, local-env enablement, pause/quit controls and warnings constrain ordinary execution but do not resolve identity-level policy tensions.
- Decisive decision or feedback right: no actor is shown receiving an identity/ultimate-policy issue, exercising legitimate ultimate authority over it, and returning an authoritative policy decision that governs subsequent Agent S operation.
- Decision owner: not established.
- Supporting / enforcement mechanisms: user-supplied task and configuration, CLI flags, safety warning for arbitrary local code execution, runtime pause/quit debugging control and external parent wrappers.
- Closure path: not applicable; configuration and operator controls set or interrupt ordinary operation rather than close an identity/ultimate-policy loop.
- Why this is / is not agent-owned: the S5 function is not established before autonomy classification. Prompts/configuration, static safety warnings, user invocation and an external OpenClaw parent are constraints or composition surfaces rather than Agent S-owned ultimate-policy authority.
- Evidence: `README.md`; `gui_agents/s3/cli_app.py`; `integrations/openclaw/README.md`; S3 procedural-memory prompts.
- Basis: explicit + structural
- Confidence: high
- Caveats: users, downstream orchestrators or institutions may impose ultimate policy around Agent S, but no qualifying first-party parent-governed S5 mode closes inside the reviewed boundary.

### Absence scope

- Surfaces inspected: CLI task/configuration and debug controls, local-env warning path, procedural prompts, current runtime modules and OpenClaw integration documentation.
- Plausible first-party paths checked: human approval/intervention, model/provider selection, static system policy, external orchestrator authority, runtime safety/termination and hosted-product references.
- Why no material first-party path remains: no first-party path turns an identity/ultimate-policy conflict into an authoritative decision and returns that decision to govern later Agent S operation; the strongest parent-like authority is outside Agent S in user/downstream composition.

## Distributed OSS parent arrangement

No organization-level distributed OSS parent mode is credited. Contributor/maintainer activity changes the software project, but the assessed runtime does not expose a first-party project-governance loop as S3/S4/S5 operational ownership. Multiple independent users running Agent S do not by themselves form one shared higher-recursion organization.

## Self-hosted and non-human modes

Agent S is self-hostable as the `gui-agents` package and can be driven from its own CLI or embedded by another application. The reviewed self-hosted mode establishes autonomous S1, but no separate first-party parent-governed S3/S4/S5 loop is supplied. The OpenClaw integration demonstrates composability into a parent agent system, not Agent S ownership of that parent's decision rights.

## Recursion

The assessed recursion contains one Agent S3 task-execution organization. The Worker may call helper models and, optionally, a bounded CodeAgent for coding work, but the pin does not establish independently viable child organizations with their own metasystems and parent channels. Historical Agent S generations with manager/worker hierarchy are retained as source history and are not combined with the current shipped S3 entrypoint.

## Variety and escalation

Operational variety comes from changing desktop state, natural-language task ambiguity, model output, GUI grounding, tool/application behavior and optional code execution. Agent S attenuates that variety through iterative observation, reflection, action formatting, grounding, trajectory limits and returned execution results. Failure/completion signals, invalid generated action fallback, CodeAgent `DONE`/`FAIL`/budget exhaustion and user pause/quit provide task-level escalation or termination mechanisms. None is promoted to a higher VSM function without the corresponding distinct organizational decision right.

## Evidence gaps

No unresolved gap requires `?` at the declared current-S3 boundary. The strongest plausible higher-function candidates were inspected directly: historical hierarchy for S2/S3; current Worker→CodeAgent delegation; task-local reflection; bBoN comparative judging; procedural memory; operator controls; and the OpenClaw integration. The evidence supports autonomous S1 and evidence-backed absence findings for S2, S3, S3*, S4 and S5.

## Assessment conclusion

Proposed repository-relative vector: `A — — — — —`.

Agent S3 qualifies as an autonomous computer-use harness because its current shipped runtime closes a model-owned screen-observation→action→environment-feedback loop. At this pinned revision, the standard Agent S3 distribution intentionally simplifies away the earlier hierarchy, and the remaining reflection, CodeAgent delegation, evaluation, memory and integration surfaces do not independently establish S2, S3, S3*, S4 or S5 under Profile `0.2.3` / Methodology `0.3.5`.

This file is a pre-admission assessment artifact (`status: proposed`). It does not itself add Agent S to the canonical catalog, cohort signature, TLDR or rankings.
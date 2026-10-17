---
harness_id: besser-agentic-framework
project_name: BESSER Agentic Framework
repository: https://github.com/BESSER-PEARL/BESSER-Agentic-Framework
review_ref: da46d4e2f0ae477704f7cc1108f1f6ec5209530e
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

# BESSER Agentic Framework

## Review boundary

- System in focus: An installable BESSER Agentic Framework (BAF) Python agent application using the first-party `Agent` runtime, `Session` and state/intent transition execution, including the shipped opt-in model-backed `reasoning_body` state and optional first-party A2A communication/orchestration platform.
- Purpose and identity: Developer-composed deployable conversational and tool-using agent applications that respond to user/platform events via configurable states and, when selected, a bounded model-directed tool/observation cycle. The organizational unit is the agent application, not the entire BESSER developer organization or a surrounding federation of arbitrary agent services.
- Relevant environment: Human platform input, messages and external events, intents, registered tools/workspaces, configured model outputs, A2A remote agent replies and status, optional database/session persistence and developer-defined state rules.
- Standard-distribution boundary: BAF `baf.core`, `baf.library.state.reasoning_state_library`, `baf.reasoning`, `baf.platforms.a2a`, platform/session handlers and documented optional integrations. A developer must select and configure the shipped reasoning state for LLM-chosen actions; basic FSM-only agents also exist and are not misrepresented as automatically model-directed. Generic remote third-party agents, models, application-written orchestration callbacks, adopter policies and development examples do not grant first-party S2–S5 ownership.
- Credited operating / distribution surfaces: [agent.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/core/agent.py#L733), [agent.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/core/agent.py#L796), [session.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/core/session.py#L143), [state.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/core/state.py#L324), [state.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/core/state.py#L381), [reasoning_state_library.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/library/state/reasoning_state_library.py#L452), [reasoning_state_library.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/library/state/reasoning_state_library.py#L584), [reasoning_state_library.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/library/state/reasoning_state_library.py#L725), [tool.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/reasoning/tool.py#L264), [a2a_platform.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/platforms/a2a/a2a_platform.py#L237), [a2a_platform.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/platforms/a2a/a2a_platform.py#L353), [user_adaptation_processor.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/core/processors/user_adaptation_processor.py#L8) (last as a scoped supporting processor only).
- Adjacent first-party surfaces excluded from ownership: `baf/test/` sample multiagent/topology examples and unit tests, repository CI/maintainer governance, standalone documentation tutorials, separately authored adopter agent state handlers/coroutines and any remote model/provider or peer organization. Monitoring database and optional UI record progress but are not inferred as first-party policy owners.
- First-party operating / deployment modes considered: Developer-configured FSM agent with state/intent/event handler and Telegram/websocket/GitHub/GitLab/A2A platforms; standard `new_reasoning_state` installed with configured LLM, first-party registered task/tool/workspace/skill functions and bounded tool loop; optional A2A `register_orchestration_as_task` with tracked user-authored coroutine and RPC calls; optional profile-based reply adaptation processor and monitoring persistence.
- Recursion level: One configured BAF agent application (possibly offering A2A endpoints and delegating operations). Distinct A2A registered peers are separate agents, not silently one shared viable system or parent recursion. Model-backed `reasoning_state` is a state body in this application, not a separate parent agent.
- Reviewed revision: `da46d4e2f0ae477704f7cc1108f1f6ec5209530e` from frozen Index candidate intake #202 and serial batch #1669, not moving upstream `main`.
- Observation date: 2026-10-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The first-party `Agent.run` initializes configured runtime services and starts selected platform event threads. Incoming platform events reach `Agent.receive_event`, are placed in per-session queues and scheduled for `Session.manage_transition`. `State.check_transitions` checks ordered event/intent/condition transitions and moves session state; `State.run` invokes the selected developer-supplied state body. Those FSM paths supply deterministic execution, intent classification and event mediation but **not by themselves** the discretionary model-backed S1 ownership classified here. [agent.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/core/agent.py#L712), [agent.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/core/agent.py#L733), [agent.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/core/agent.py#L796), [session.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/core/session.py#L143), [state.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/core/state.py#L324), [state.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/core/state.py#L381).

The shipped opt-in `new_reasoning_state` installs an actual first-party state body. On invocation `reasoning_body` gathers registered agent tools, attached markdown skills and workspaces, creates a request-scoped task list and loops up to `max_steps`. `_run_reasoning_loop` calls `llm.predict_with_tools`, translates selected function calls into first-party `Tool.call` executions, appends observed outcomes to model conversation history, and then selects another step or returns an answer; the task planner may push back a premature final response when subtasks remain. Skills and workspaces supply context and allowed tools, not autonomous future strategy. [reasoning_state_library.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/library/state/reasoning_state_library.py#L452), [reasoning_state_library.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/library/state/reasoning_state_library.py#L503), [reasoning_state_library.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/library/state/reasoning_state_library.py#L584), [reasoning_state_library.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/library/state/reasoning_state_library.py#L625), [reasoning_state_library.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/library/state/reasoning_state_library.py#L640), [reasoning_state_library.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/library/state/reasoning_state_library.py#L725), [task_tools.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/library/tool/task_tools.py#L37).

The optional A2A platform registers remote method endpoints and IDs, creates task records and supports tracked RPC subtasks and a parent orchestration task. Crucially `register_orchestration_as_task` executes a **user-supplied async coroutine**, tracks its subtask states and waits for completion; framework bookkeeping does not itself choose cross-unit load/priority or repair conflicting peer commitments. Optional monitoring persists session and reasoning events. `UserAdaptationProcessor` model-rewrites agent messages for supplied user profile values but does not itself alter the system's prospective organizational capabilities. [a2a_platform.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/platforms/a2a/a2a_platform.py#L211), [a2a_platform.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/platforms/a2a/a2a_platform.py#L237), [a2a_platform.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/platforms/a2a/a2a_platform.py#L353), [a2a_platform.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/platforms/a2a/a2a_platform.py#L370), [user_adaptation_processor.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/core/processors/user_adaptation_processor.py#L8).

## Operational model

At the chosen application recursion, a configured `reasoning_state` supplies one first-party adaptive S1 operating loop within an otherwise developer-assembled FSM runtime; real tools and external peers produce returned observations. With only FSM states installed, operations remain developer/intent-determined and should not be mistaken for autonomous `S1=A` on their own. A2A provides communication and task orchestration primitives for multiple independently deployed agents, but does not establish first-party substantive S2 inter-unit damping, S3 system-wide current control, S3* independent audit, S4 prospective change or S5 identity governance. No complete viable hierarchy is assumed from API naming.

## S1 — Operations

- State: A
- Function: Provide configured user/business operations through an installed first-party, LLM-directed reasoning state that chooses and executes tools and incorporates their observed results.
- Disturbance / variety regulated: Unstructured user requests, workspace contents and tool failures/successes, task decomposition, platform inputs and changing responses that exceed a static intent/transition script.
- Decisive decision or feedback right: The model-backed installed `reasoning_body` chooses tool names/arguments and whether to act again versus provide a final answer, using returned tool results and optional task-progress state.
- Decision owner: The configured reasoning agent's LLM-driven operating decision path under shipped BAF state/tool implementation. Model service supplies inference; first-party tool registry, FSM dispatch, developer-defined permission/skills and user prompts constrain its operating rights.
- Supporting / enforcement mechanisms: FSM state and event loop, registered Tool.call validation, step budget, task-list checks, scratchpad/step events, workspace confinement, session state and optional persistence.
- Closure path: External message/event → Agent.receive_event → Session transition → installed reasoning state body → LLM selection → actual tool execution → observed result inserted into next model messages → next model decision or response via Session.reply.
- Boundary reachability: `new_reasoning_state` is a supported first-party factory whose returned state has `reasoning_body` wired through `set_body`; ordinary `State.run` executes that callback. The model/tool/result path is callable in a configured shipped application rather than relying on a test-only stub.
- Why this is / is not agent-owned: Unlike fixed ordered FSM condition/intent transitions, reasoning model selects multiple successive operations based on resulting environment feedback; static state machine and tool wrappers are supporting enforcement.
- Evidence: [agent.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/core/agent.py#L796); [state.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/core/state.py#L324); [state.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/core/state.py#L381); [reasoning_state_library.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/library/state/reasoning_state_library.py#L725); [reasoning_state_library.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/library/state/reasoning_state_library.py#L584); [reasoning_state_library.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/library/state/reasoning_state_library.py#L625); [reasoning_state_library.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/library/state/reasoning_state_library.py#L640); [tool.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/reasoning/tool.py#L348).
- Basis: Explicit code-reachable optional model/tool feedback mode in first-party distributed runtime.
- Confidence: High for structural reachability; live third-party LLM and task workloads not executed.
- Caveats: S1=A pertains to installed reasoning-state operation, not all plain FSM configurations, remote A2A agents or guaranteed provider behavior.


## S2 — Coordination

- State: —
- Function: No shipped S2-specific adaptive damping of verified interference or oscillation among distinct viable S1 units is established at this recursion.
- Disturbance / variety regulated: Concurrent external A2A RPC subtasks and distinct agents could interfere, but the reviewed tracking/replies do not identify, moderate and feed back concrete inter-S1 conflict.
- Decisive decision or feedback right: User-coded orchestration coroutine determines RPC calls; A2A framework registers/tracks task IDs/status and awaits results. No first-party inter-agent interference arbitrator adjusts independent agents' conflicting operations.
- Decision owner: Adopter-written orchestration callback plus deterministic A2A method dispatch/task tracking, not an S2-specific owner in the standard framework.
- Supporting / enforcement mechanisms: A2A registry, remote method router, tracked RPC calls, task futures/status, SSE event display and local state transitions.
- Closure path: Orchestration RPC task call → subtask records/remote responses → caller task completion, without disturbance-specific comparison/negotiation and stabilized return to multiple competing S1 operations.
- Why this is / is not agent-owned: Transport, await/gather status and a callback titled 'orchestration' do not by themselves attenuate actual cross-operational conflict, even when many actors communicate.
- Evidence: [a2a_platform.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/platforms/a2a/a2a_platform.py#L237); [a2a_platform.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/platforms/a2a/a2a_platform.py#L353); [a2a_platform.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/platforms/a2a/a2a_platform.py#L395); [message_router.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/platforms/a2a/message_router.py#L15); [agent_registry.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/platforms/a2a/agent_registry.py#L9).
- Basis: Explicit A2A callback ownership and tracked subtask lifecycle; bounded negative.
- Confidence: Medium-high within first-party shipped A2A mode.
- Caveats: User-authored special-purpose orchestration could supply S2 with appropriate conflict feedback; it is not demonstrated as packaged default.

### Absence scope

- Surfaces inspected: A2A RPC, registry and router; tracked and untracked task methods; agent event loop/transition execution; model-backed reasoning and planned task list.
- Plausible first-party paths checked: Inter-agent messaging and synchronous/asynchronous RPC, subtask wait/status updates, A2A orchestration callback, task-list dependencies and session event queues.
- Why no material first-party path remains: All first-party behavior is message delivery, single-task planning or status aggregation; no actual/structural inter-S1 disturbance-specific attenuating choice and mutual return to distinct units was found.


## S3 — Inside-and-now control

- State: —
- Function: No closed system-wide current operations controller governs the full agent application/federation's resources, priorities and competing commitments.
- Disturbance / variety regulated: Multiple concurrent A2A tasks, sessions and configured states might demand capacity negotiation or intervention, but the reviewed framework has no holistic current portfolio decision right.
- Decisive decision or feedback right: Model reasoning decides current task steps; static FSM checks govern transitions; adopter coroutine sequences peer calls and tracked tasks. Framework does not decide across independent S1 commitments/resources on its own.
- Decision owner: Current-task LLM, developer-authored state/coroutine rules and deterministic A2A task scheduler; no distinct whole-current S3 owner with closed returned decisions.
- Supporting / enforcement mechanisms: Per-session state, event queues, A2A task registry and status, platform threads, database monitoring and reasoning TaskList.
- Closure path: Single task gets plan/execute/status feedback; missing whole-system view → independent aggregate control decision over competing S1 work → binding adjustment fed to those units.
- Why this is / is not agent-owned: A planned reasoning request, tracked orchestration and monitoring UI are not a system-wide manager; human developer configuration without a first-party current-control decision return does not establish parent S3.
- Evidence: [a2a_platform.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/platforms/a2a/a2a_platform.py#L353); [a2a_platform.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/platforms/a2a/a2a_platform.py#L370); [agent.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/core/agent.py#L733); [agent.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/core/agent.py#L796); [reasoning_state_library.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/library/state/reasoning_state_library.py#L503); [session.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/core/session.py#L315).
- Basis: Bounded negative after testing orchestration/monitoring as positive and possible parent-mode paths.
- Confidence: Medium-high for package-as-shipped; application-specific orchestrator logic not inspected beyond boundary.
- Caveats: An adopter can author an overarching current-control policy but there is no built-in first-party metasystem decision right demonstrated.

### Absence scope

- Surfaces inspected: Runtime/Session state and event processing, A2A tracking/orchestration callbacks, task-list reasoning, platform deployment and session monitoring.
- Plausible first-party paths checked: Central orchestrator, tracked status/wait, concurrent event threads, per-task planning, monitoring database and developer state variables.
- Why no material first-party path remains: Status/task waiting and externally supplied callbacks never supply a first-party accountable allocation/priority/intervention decision over aggregate operating units and return that choice to ongoing operations.


## S3* — Complementary audit

- State: —
- Function: No operationally integrated independent complementary reality-check channel that can challenge operating-control claims and return corrective action.
- Disturbance / variety regulated: Model/tool mistakes, false reported completion, errors and unexpected session events; built-in logging/monitoring expose events but do not independently audit claims.
- Decisive decision or feedback right: No separately owned independent audit decision shown. Normal tool errors, reasoning steps, monitoring records and possible human review of external GitHub events are not a complementary auditor.
- Decision owner: Agent and developer/monitoring users for their respective original operations; none owns a first-party independent audit-and-return control decision.
- Supporting / enforcement mechanisms: Reasoning step/scratchpad events, monitoring DB, status updates, task callback exceptions, GitHub/GitLab event adapters, unit tests.
- Closure path: Model/tool execution → session and monitoring records/report; missing independent physical/third-party evidence access → challenge of an operational claim → binding present-control recheck/correction returned to S1.
- Why this is / is not agent-owned: Trace observability and events named 'review' are not independent complementary audit of the runtime's own operations; a model checking its own outstanding task list is an ordinary local execution guard.
- Evidence: [reasoning_state_library.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/library/state/reasoning_state_library.py#L584); [reasoning_state_library.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/library/state/reasoning_state_library.py#L640); [session.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/core/session.py#L211); [agent.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/core/agent.py#L1157); [a2a_platform.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/platforms/a2a/a2a_platform.py#L353).
- Basis: First-party trace/monitoring and event surfaces inspected, bounded negative.
- Confidence: Medium-high; no installed audit-to-current-control controller found.
- Caveats: External developer tests/reviewers could be connected, but no resulting first-party corrective return is evidenced.

### Absence scope

- Surfaces inspected: Reasoning logs and scratchpad, per-session saved reasoning events, DB monitoring interfaces, task statuses, platform event adapters and tests/examples as adjacent context.
- Plausible first-party paths checked: Post-task quality grading, separate verifier/reviewer roles, raw tool/result inspection, monitoring alerts, A2A status challenge/rework and GitHub review event callbacks.
- Why no material first-party path remains: Traces and task status are reporter-derived; no shipped independent challenge owner plus returned corrective current-control action was identified in the running application.


## S4 — Outside-and-then intelligence

- State: —
- Function: No demonstrable prospective organization/capability strategy selection with authorized returned implementation was established in shipped BAF modes.
- Disturbance / variety regulated: Potential future integration/tool/skill requirements, changing users and capabilities, and current user's profile changes.
- Decisive decision or feedback right: Developer explicitly registers `Tool`, `Skill`, `Workspace`, state handlers and configuration. Optional `UserAdaptationProcessor` uses configured LLM to alter present reply phrasing from user profile, not accept longer-horizon system strategy/capability change.
- Decision owner: External developer/operator for configuration and immediate model processor for response adaptation; neither evidenced as packaged future-intelligence organ.
- Supporting / enforcement mechanisms: Markdown Skill loader, developer tool/workspace registration, user profile processor, state configuration, optional session persistence and model/reasoning scratchpad.
- Closure path: Author-supplied configuration influences later tool/context availability and present response generation; no first-party future environment scan/alternatives selection → legitimate capability-change decision → prospective plan instantiated into system operations.
- Why this is / is not agent-owned: User personalization is task-output adaptation, not organization-wide future viability; repository APIs capable of loading developer-authored extensions do not exercise that prospective authority.
- Evidence: [agent.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/core/agent.py#L440); [agent.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/core/agent.py#L487); [agent.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/core/agent.py#L526); [reasoning_state_library.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/library/state/reasoning_state_library.py#L503); [user_adaptation_processor.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/core/processors/user_adaptation_processor.py#L8); [user_adaptation_processor.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/core/processors/user_adaptation_processor.py#L40).
- Basis: First-party optional adaptation and extension entry points analyzed, bounded negative.
- Confidence: Medium-high for shipped reviewed paths.
- Caveats: A separately authored A2A agent could be programmed as S4 but no such installed whole-system return was established here.

### Absence scope

- Surfaces inspected: Tool/Skill/Workspace addition and loading, user profile adaptation processor, reasoning task plans, monitoring logs, A2A orchestration and developer configuration.
- Plausible first-party paths checked: Future ability generation from tool execution and skills, profile-driven mutation, self-improving prompt, external environment intelligence from agent messages, operator-authorized updates.
- Why no material first-party path remains: Adaptation modifies user-facing responses for present profiles; skills/tools are supplied via developer registration, and planning stays within the current request. No first-party prospective option owner and binding operational upgrade return is wired.


## S5 — Policy and identity

- State: —
- Function: No installed decisive legitimate ultimate organizational policy/purpose-identity arbitration loop at the chosen BAF application recursion.
- Disturbance / variety regulated: Agent ID, incoming users, A2A endpoint permissions, developer settings and platform credentials; no evidenced ultimate policy conflict.
- Decisive decision or feedback right: Developers configure agent description/LLM/states and A2A agent cards; external platform operators govern credentials and deployment. Neither path is an integrated S5 purpose-adjudication/return operation.
- Decision owner: Developer/user/operator outside runtime for mission/config, plus deterministic platform registry for lookup; no legitimate S5 parent actor with source-closed final decision.
- Supporting / enforcement mechanisms: A2A agent-card identity and registry, platform authentication elsewhere, selected agent state/configuration, input event handling.
- Closure path: Configured agent ID/role → endpoint discovery and handling; absent ultimate values/purpose dispute → legitimate S5 adjudication → returned authoritative organization-wide identity or policy decision.
- Why this is / is not agent-owned: Agent naming, registered capabilities and permission/authentication are operational identity/routing controls, not a first-party system ethos or ultimate mission governance function.
- Evidence: [agent.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/core/agent.py#L90); [a2a_platform.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/platforms/a2a/a2a_platform.py#L55); [agent_registry.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/platforms/a2a/agent_registry.py#L9); [agent.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/core/agent.py#L267); [agent.py](https://github.com/BESSER-PEARL/BESSER-Agentic-Framework/blob/da46d4e2f0ae477704f7cc1108f1f6ec5209530e/baf/core/agent.py#L733).
- Basis: First-party configuration and A2A identity surfaces inspected, bounded negative.
- Confidence: Medium-high for installable first-party scope.
- Caveats: An actual adopting business/government may provide S5 externally. Do not ascribe its authority to the OSS framework.

### Absence scope

- Surfaces inspected: Agent initialization and config, A2A agent card/registry and router, platform ingress, property and profile loaders, core state rules.
- Plausible first-party paths checked: Agent identity registration, configuration updates, administrator/platform permissions, external operator authoring and governance callback.
- Why no material first-party path remains: No published first-party decision/return channel for ultimate purpose conflicts or policy identity revisions exists; platform identity and developer-supplied purpose are not themselves S5 decisions.


## Distributed OSS parent arrangement

The BESSER project maintainers, an adopter's developer/operator, configured external LLM providers, remote A2A peers and the BAF runtime are different potential authorities. Human-written asynchronous orchestration callbacks and developer-set model/skill/state configuration are explicitly *not* interpreted as a closed first-party parent-governed S3/S4/S5 role without a legitimate system-level decision and feedback return.

## Self-hosted and non-human modes

The installable Python app can run platform event loops and register an opt-in autonomous reasoning state, with model and tool providers supplied/configured outside the Python package. A2A can create and track remote tasks with a user-written async orchestration callback. This is a pinned first-party source review; no provider credentials, live platforms, external A2A peers, or app-level inference E2E run were used.

## Recursion

One BAF application is the assessed system. Its user sessions are not independent S1 organizations merely because they have states. A2A remote peers are independently deployable services; the shipped A2A orchestrator can call and monitor their tasks but does not thereby establish an S2–S5 metasystem or a recursively viable superorganization.

## Variety and escalation

Intent classifiers/FSM state transitions attenuate input-event variety and make developer-configured conversation flows repeatable; optional LLM reasoning expands action variety through returned tool results. A2A statuses expose remote task outcomes, while monitoring logs and the request-scoped TaskList track progress; escalation to a user/developer or status view is not credited as system-wide current control, independent audit, future intelligence or ultimate policy.

## Evidence gaps

- The installed model-backed reasoning state is explicitly supported but does not run in a plain FSM-only configuration. The S1=A classification is about the **supported mode**, not a guarantee that every user application enables tool calling or has provider credentials.
- First-party A2A supports meaningful tracked orchestration and returns status, but the actual adaptive cross-agent resource or disturbance-control policy would be provided by an adopter's coroutine. No specific package-owned S2/S3 decision was established.
- The scanned optional profile-based reply adaptation is real but not prospective capability evolution. No independent S3* verification path or legitimate S5 mission arbitration loop was evidenced in the shipped inspected boundaries.
- Structural source review only; no live inference, A2A services, platform credentials or full BAF upstream dependency/test suite was run. Tests/examples and provider internals cannot substitute for the missing organizational closure paths.

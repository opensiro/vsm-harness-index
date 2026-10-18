---
harness_id: deepagentsjs
project_name: Deep Agents JS
repository: https://github.com/langchain-ai/deepagentsjs
review_ref: 39b85021d5c64d14539999490610970f76da0b47
reviewed_at: 2026-09-19
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
assessment_changed_at: 2026-09-19
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Deep Agents JS

## Review boundary

- System in focus: one first-party Deep Agents JavaScript/TypeScript runtime at pinned revision `39b85021d5c64d14539999490610970f76da0b47`, including `createDeepAgent`, its built-in model/tool/filesystem/planning middleware, synchronous subagent delegation, optional remote asynchronous subagents, persistent task state, optional completion callbacks, memory/skills support and the shipped ACP server surface.
- Purpose and identity: provide a batteries-included, ready-to-run agent harness whose model-driven agent can execute tool-mediated tasks, use filesystem working state, delegate bounded work, persist context, and optionally regulate multiple remote background subagent commitments.
- Relevant environment: user/application requests, model responses, tool and filesystem results, remote Agent Protocol subagent runs and statuses, persistent conversation/checkpoint state, configured memory/skill files, ACP client interactions and operator permission responses.
- Standard-distribution boundary: first-party code and documented installable packages in `langchain-ai/deepagentsjs` at the pinned revision. External model providers, Agent Protocol servers/graphs, application-authored custom agents/tools/policies, IDE clients and external MCP/services remain outside the boundary unless the first-party runtime itself closes the mapped organizational function.
- Credited operating / distribution surfaces: `createDeepAgent`; the built-in LangChain/LangGraph model/tool loop; filesystem/planning/summarization middleware; synchronous `task` subagent path; model-facing async-subagent `start/check/update/cancel/list` tools and persisted `asyncTasks` state; optional completion callback; memory/skills middleware; and the installable `deepagents-acp` runtime where it exposes the same Deep Agent through ACP.
- Adjacent first-party surfaces excluded from ownership: repository `evals/` and `internal/eval-harness` development/evaluation infrastructure; unit/integration/standard tests; contributor/CI/release machinery; repository-local `.agents/skills` used to develop the project; examples that do not establish a shipped runtime closure beyond the credited packages.
- First-party operating / deployment modes considered: default standalone `createDeepAgent`; synchronous isolated/fork subagents; configured remote async subagents; memory/skills-enabled agents; checkpointer/HITL configurations; ACP server sessions and permission prompts.
- Recursion level: one Deep Agents JS parent-agent organization. The root agent is the current-control parent at the reviewed level; configured synchronous or remote async subagents may form bounded S1 units underneath it, but delegation or nesting alone is not treated as a recursive viable system.
- Reviewed revision: `39b85021d5c64d14539999490610970f76da0b47`.
- Observation date: 2026-09-19.
- Generated Profile version: `0.2.3`.
- Generated Methodology version: `0.3.5`.
- Current Profile version: `0.2.3`.
- Current Methodology version: `0.3.5`.

## Repository architecture

Deep Agents JS is a TypeScript monorepo whose primary `deepagents` package wraps LangChain/LangGraph `createAgent` with opinionated first-party middleware. `createDeepAgent` assembles filesystem access, a default general-purpose subagent, summarization, tool-call patching, optional skills and memory, optional remote asynchronous subagents, optional HITL, and then returns a compiled model-driven agent graph.

The synchronous subagent path exposes a model-facing `task` tool. A parent agent chooses a configured isolated or forked subagent, sends a bounded assignment, and receives the subagent's final report or structured response back as a tool result. Multiple independent subagents may be launched, but the shipped relation is hierarchical delegation/result return. State filtering and call-count isolation prevent runtime channel collisions; those mechanisms do not themselves establish an organizational S2 mutual-adjustment relation among S1 units.

The optional asynchronous path is materially different. `AsyncSubAgentMiddleware` gives the root model five direct tools — `start_async_task`, `check_async_task`, `update_async_task`, `cancel_async_task`, and `list_async_tasks` — and persists the entire tracked task set in `asyncTasks`. The agent can inspect live statuses, interrupt and redirect a running remote thread, cancel a current commitment, or start another one. These decisions return into subsequent agent context, establishing a first-party S3 current-control loop over the root agent's background subagent portfolio.

Memory and skills change what information/procedures are available to later calls, and the memory prompt explicitly encourages saving useful user feedback. They are not credited as S4 here because the pinned runtime does not establish a separate prospective environment-modeling/adaptation-option loop coupled back into present organizational control; they remain persistent context/procedure mechanisms. Likewise, the repository's behavioural eval suites are development/evaluation infrastructure, not an operating complementary-audit actor. Unlike a mere name-based inference, no first-party runtime grader/challenger with independent access and corrective return was found at this pinned JS boundary.

The ACP package is a first-party deployment surface. It can expose Deep Agents to IDE clients, preserve sessions and ask a human client to allow/reject tool calls. That permission mechanism is treated as an operational gate rather than a separate parent-owned S3/S5 function: the autonomous root agent still selects the organizational intervention, while the ACP client supplies generic execution permission rather than a function-specific whole-system current-control or ultimate-policy decision process.

Primary evidence:

- [`libs/deepagents/README.md`](https://github.com/langchain-ai/deepagentsjs/blob/39b85021d5c64d14539999490610970f76da0b47/libs/deepagents/README.md) — first-party description of a ready-to-run harness, planning/filesystem/subagents/context management and `createDeepAgent` usage.
- [`libs/deepagents/src/agent.ts`](https://github.com/langchain-ai/deepagentsjs/blob/39b85021d5c64d14539999490610970f76da0b47/libs/deepagents/src/agent.ts) — composition of the model-driven agent, default subagent and middleware stack, optional async subagents, memory and HITL.
- [`libs/deepagents/src/middleware/subagents.ts`](https://github.com/langchain-ai/deepagentsjs/blob/39b85021d5c64d14539999490610970f76da0b47/libs/deepagents/src/middleware/subagents.ts) — synchronous delegation, isolated/fork context, returned `task` results and state filtering.
- [`libs/deepagents/src/middleware/async_subagents.ts`](https://github.com/langchain-ai/deepagentsjs/blob/39b85021d5c64d14539999490610970f76da0b47/libs/deepagents/src/middleware/async_subagents.ts) — persisted background-task set and model-facing start/check/update/cancel/list control tools.
- [`libs/deepagents/src/middleware/completion_callback.ts`](https://github.com/langchain-ai/deepagentsjs/blob/39b85021d5c64d14539999490610970f76da0b47/libs/deepagents/src/middleware/completion_callback.ts) — optional completion/error notification from async subagent back into a callback parent thread.
- [`libs/deepagents/src/middleware/memory.ts`](https://github.com/langchain-ai/deepagentsjs/blob/39b85021d5c64d14539999490610970f76da0b47/libs/deepagents/src/middleware/memory.ts) — persistent AGENTS.md context and model instructions for saving useful feedback.
- [`libs/acp/src/server.ts`](https://github.com/langchain-ai/deepagentsjs/blob/39b85021d5c64d14539999490610970f76da0b47/libs/acp/src/server.ts) and [`libs/acp/src/types.ts`](https://github.com/langchain-ai/deepagentsjs/blob/39b85021d5c64d14539999490610970f76da0b47/libs/acp/src/types.ts) — first-party ACP operating surface, DeepAgent configuration, sessions and generic human tool-permission gate.
- [`evals/README.md`](https://github.com/langchain-ai/deepagentsjs/blob/39b85021d5c64d14539999490610970f76da0b47/evals/README.md) — behavioural evaluation suites and LangSmith regression tracking, inspected as adjacent development/evaluation infrastructure rather than runtime audit ownership.

## Operational model

The ordinary S1 is the root model-driven Deep Agent. It receives a task, decides among model responses, built-in/custom tools, filesystem work and delegation, observes returned results and continues until producing an outcome.

Synchronous subagents are bounded worker S1s when configured, but the root's `task` tool is principally delegation. The worker returns a report to the root; no shipped function specifically regulates inter-worker conflict or oscillation. By contrast, remote asynchronous subagents create a standing set of concurrent current commitments. The root model can see that set through `list_async_tasks`/`check_async_task`, then autonomously redirect, interrupt, cancel or add work. That closes S3 at the reviewed parent-agent recursion.

## S1 — Operations

- State: A
- Function: autonomously execute a bounded user/application task through model reasoning, tool/filesystem actions, optional delegation and returned observations.
- Disturbance / variety regulated: task ambiguity, changing tool/filesystem results, model uncertainty, intermediate failures, context pressure and information returned by delegated workers.
- Decisive decision or feedback right: choose the next substantive model/tool/delegation action, interpret returned observations and decide when to produce the final operational result.
- Decision owner: the running model-driven root Deep Agent.
- Supporting / enforcement mechanisms: LangGraph execution, filesystem backend, planning/todo support, summarization, checkpoint/store support, configured tools, subagent middleware, memory/skills and optional HITL.
- Closure path: request enters `createDeepAgent` runtime → model selects response/tool/filesystem/delegation action → first-party runtime executes the selected callable path → result returns as agent state/messages → model chooses the next action or final response.
- Boundary reachability: `createDeepAgent` is the documented first-party package entrypoint and immediately constructs a runnable model/tool agent with built-in filesystem, context and subagent support; no adopter-authored supervisory actor is required for this S1 loop.
- Why this is / is not agent-owned: configuration bounds the action space, but the substantive sequence of tool/delegation/final-response choices is selected by the model agent at runtime rather than predetermined by a static workflow.
- Evidence: `libs/deepagents/README.md`, `libs/deepagents/src/agent.ts`, `libs/deepagents/src/middleware/subagents.ts`.
- Basis: explicit + structural
- Confidence: high
- Caveats: external model inference supplies model outputs, but the reviewed first-party harness owns the operational loop, tool exposure and observation return path.

## S2 — Coordination

- State: —
- Function: no material first-party S2 interference-attenuation function is established among distinct operational subagents at the reviewed recursion.
- Disturbance / variety regulated: multiple subagents can run independently or concurrently, but no shipped organizational relation is evidenced that senses a specific inter-S1 conflict/oscillation and mutually adjusts those S1 units to attenuate it.
- Decisive decision or feedback right: none established for qualifying S2 coordination.
- Decision owner: none established.
- Supporting / enforcement mechanisms: root-controlled `task` delegation, isolated/fork context, parallel independent calls, filtered state transfer, per-agent call-count isolation, persisted async task state and root-owned async lifecycle controls.
- Closure path: not applicable; worker results return hierarchically to the root and async lifecycle actions are S3 current-control interventions, not an S2 feedback relation among peers.
- Why this is / is not agent-owned: the root can choose workers and manage their commitments, but selection/delegation/control from a parent does not establish S2 without a concrete cross-S1 disturbance and attenuation loop.
- Evidence: `libs/deepagents/src/middleware/subagents.ts`, `libs/deepagents/src/middleware/async_subagents.ts`.
- Basis: explicit + absence review
- Confidence: high
- Caveats: an application can compose specialist roles and a coordinator using the framework; that downstream organization requires its own functional evidence and is not inherited by this framework assessment.

### Absence scope

- Surfaces inspected: synchronous isolated/fork subagents, default general-purpose worker, parallel task guidance, subagent state filtering, async remote subagents, persisted task registry, completion callbacks and root model tool exposure.
- Plausible first-party paths checked: parallel delegation, duplicate-name prevention, state-channel/call-count collision isolation, shared parent context in fork mode, async update/cancel/list controls and callback notifications.
- Why no material first-party path remains: these paths provide worker isolation, hierarchical delegation, result return or parent current control. None establishes a specific inter-S1 interference/oscillation plus a first-party S2-specific attenuation relation that feeds mutual adjustment back into the affected S1 units.

## S3 — Inside-and-now control

- State: A
- Function: regulate the root agent's current set of remote asynchronous subagent commitments using live status and model-selected interventions.
- Disturbance / variety regulated: background work can become stale, fail, complete, require changed instructions, consume attention after it is no longer needed, or need to be replaced/augmented while other tasks continue.
- Decisive decision or feedback right: choose which async commitment to start, inspect, redirect/interrupt, cancel or retain based on the current tracked task set and returned statuses/results.
- Decision owner: the autonomous root Deep Agent invoking the model-facing async-task control tools.
- Supporting / enforcement mechanisms: `asyncTasks` persisted reduced state, Agent Protocol/LangGraph SDK clients, remote thread/run identifiers, live-status fetches, `multitaskStrategy: "interrupt"`, run cancellation, task-list merging and optional completion callbacks.
- Closure path: root agent starts one or more async subagents → first-party middleware records the full tracked set → `list_async_tasks`/`check_async_task` returns live current status/result into the root model's context → root agent selects update/interrupt, cancel, new work or no intervention → first-party tool executes the decision and writes the changed task state → subsequent model steps observe the changed current operation.
- Boundary reachability: configuring `AsyncSubAgent` entries directly mounts the five first-party control tools into `createDeepAgent`; the root model itself can invoke them without an adopter supplying a separate manager/controller actor.
- Why this is / is not agent-owned: SDK/runtime machinery enforces the selected lifecycle action, but the root model owns the discretionary decision of which current commitment to inspect, redirect, cancel or add.
- Evidence: `libs/deepagents/src/agent.ts`, `libs/deepagents/src/middleware/async_subagents.ts`, `libs/deepagents/src/middleware/completion_callback.ts`.
- Basis: explicit + structural
- Confidence: high
- Caveats: ordinary synchronous delegation alone is not this witness. S3 rests on the separately shipped async mode with persistent whole-set visibility and intervention rights.
- Whole-system current view: the root holds a persisted `asyncTasks` map for all tracked background tasks and can use `list_async_tasks` to fetch their live statuses in one current view or `check_async_task` for detailed status/result.
- Current-control decision scope: start new commitments; inspect active commitments; interrupt and replace a running task's instruction on the same thread; cancel work that is no longer needed; and condition subsequent action on completion/error/cancellation state.

## S3* — Complementary audit

- State: —
- Function: no material first-party operational complementary-audit/challenge function is established at the reviewed JS runtime boundary.
- Disturbance / variety regulated: tests/evals can detect behavioural regressions and a parent may inspect worker results, but no shipped operating actor independently challenges an S1/S3 claim through complementary access and returns an audit judgment into corrective current control.
- Decisive decision or feedback right: none established for a qualifying S3* function.
- Decision owner: none established.
- Supporting / enforcement mechanisms: behavioural eval suites, LangSmith experiment reporting, integration/unit tests, ordinary parent inspection of task results, HITL tool approval and callback notifications were inspected but not credited as audit ownership.
- Closure path: not applicable; repository evals run as development/evaluation workspaces and record/assert trajectories, while normal worker-result checking remains in the producing/control path rather than an independent complementary audit channel.
- Why this is / is not agent-owned: separate evaluation execution or a human permission prompt does not by itself establish organizational audit independence, complementary access and corrective feedback into live operation.
- Evidence: `evals/README.md`, runtime middleware tree at the pinned revision, `libs/deepagents/src/middleware/async_subagents.ts`, `libs/acp/src/server.ts`.
- Basis: explicit + absence review
- Confidence: high
- Caveats: downstream users can add reviewer agents or evaluation-driven correction through custom middleware; generic extensibility is not a first-party S3* constructor claim.

### Absence scope

- Surfaces inspected: shipped Deep Agent middleware, synchronous/async subagent paths, completion callback, ACP permission flow, repository behavioural eval suites, standard/unit/integration tests and LangSmith result reporting.
- Plausible first-party paths checked: parent review of subagent results, background completion callbacks, behavioural evals, HITL approvals, trajectory assertions and custom-middleware extension points.
- Why no material first-party path remains: no inspected shipped operating path combines a sufficiently independent auditor, complementary evidence access, autonomous audit judgment and a return path that can force corrective current operation. The eval infrastructure is adjacent development/evaluation machinery rather than the deployed harness's audit organ.

## S4 — Outside-and-then intelligence

- State: —
- Function: no distinct first-party prospective environment-facing intelligence/adaptation loop is established at the reviewed organizational boundary.
- Disturbance / variety regulated: persistent memory and skills can preserve user feedback, preferences, project context and procedures across later calls, but persistence/retrieval alone does not establish S4 outside-and-then adaptation ownership.
- Decisive decision or feedback right: none established for a qualifying S4 function.
- Decision owner: none established.
- Supporting / enforcement mechanisms: AGENTS.md memory loading/editing, model instructions to save useful feedback, skill sources, persistent filesystem state, summarization, checkpoints and repository eval results.
- Closure path: not applicable for S4; memory/skill files can change later prompt context, but the pinned runtime does not separately sense future/external distinctions, develop adaptation alternatives, decide among them and return the chosen organizational adaptation into current capability/control.
- Why this is / is not agent-owned: the model may write remembered facts/preferences or edit procedures, but those actions are context maintenance within the ordinary operational loop rather than an evidenced S4 environmental intelligence/adaptation organ.
- Evidence: `libs/deepagents/src/middleware/memory.ts`, skills/filesystem support in `libs/deepagents/src/agent.ts`, `evals/README.md`.
- Basis: explicit + absence review
- Confidence: high
- Caveats: durable feedback memory can influence future behaviour and is therefore an important adaptation mechanism, but the Profile requires the stronger prospective outside-and-then function rather than equating learning/persistence with S4.

### Absence scope

- Surfaces inspected: memory middleware and feedback-writing guidance, skills loading/editing, filesystem persistence, summarization, checkpointer/store state, behavioural evals and async task history/control.
- Plausible first-party paths checked: saving user corrections to AGENTS.md, later memory reuse, skill edits, regression tracking and reuse of persistent state across sessions.
- Why no material first-party path remains: these mechanisms retain context/procedures or measure behaviour; none establishes a separate prospective environmental model, adaptation-option formation/selection and return into present organizational capability/S3.

## S5 — Policy and identity

- State: —
- Function: no first-party identity/ultimate-policy authority loop is established at the reviewed Deep Agents JS organization boundary.
- Disturbance / variety regulated: system prompts, filesystem permissions, harness profiles, ACP modes and tool approvals constrain operation, but they are configured/enforced operational rules rather than an evidenced S5 identity/ultimate-policy decision process.
- Decisive decision or feedback right: none established for qualifying S5 identity/ultimate-policy closure.
- Decision owner: none established.
- Supporting / enforcement mechanisms: application-authored system prompts, harness profiles, tool exclusions, filesystem permissions, `interruptOn`, ACP allow/reject decisions, plan/agent/ask modes and custom middleware.
- Closure path: not applicable; operator/developer configuration and per-tool permission responses alter allowed execution but no shipped path elevates an identity/ultimate-policy issue to a legitimate ultimate authority and returns that decision as organizational policy closure.
- Why this is / is not agent-owned: the root agent operates within supplied identity/constraints; it does not own the ultimate authority that defines or revises the organization's identity/purpose, and generic human veto over a tool call is not S5 parent governance.
- Evidence: `libs/deepagents/src/agent.ts`, `libs/acp/README.md`, `libs/acp/src/server.ts`, profile/permission support at the pinned revision.
- Basis: explicit + absence review
- Confidence: high
- Caveats: the ACP user can allow/reject tool calls and switch operating modes, but those are bounded operational controls, not identity/ultimate-policy adjudication.

### Absence scope

- Surfaces inspected: system prompt/profile selection, tool and middleware exclusions, filesystem permissions, HITL interrupt configuration, ACP session modes, per-tool permission requests and custom configuration surfaces.
- Plausible first-party paths checked: operator allow/reject decisions, always-allow/always-reject caching, plan/agent/ask mode changes, user-authored system prompt and harness-profile constraints.
- Why no material first-party path remains: every inspected path constrains or gates ordinary execution. None establishes an identity/ultimate-policy dispute, legitimate ultimate authority over it and a returned policy decision governing subsequent organization-level operation.

## Distributed OSS parent arrangement

The repository has normal open-source contributor/maintainer governance, but that development governance is outside the deployed runtime boundary and is not imported as S3/S4/S5 parent ownership. The ACP client is a local operator surface; its generic permission decisions are bounded execution gates and do not by themselves establish a function-specific parent-governed mode under Methodology 0.3.5.

## Self-hosted and non-human modes

Deep Agents JS can be run locally/self-hosted and through the first-party ACP server. The autonomous async-task S3 mode remains available when remote async subagents are configured. HITL/ACP approvals may constrain selected tool execution, but the inspected standard modes do not establish a distinct parent-governed whole-system S3 topology or S5 ultimate-policy loop, so no `(P)` modifier is published.

## Recursion

Configured subagents execute their own model/tool work and can therefore be bounded operational units beneath the root. The reviewed higher recursion is the root agent plus its tracked subagent commitments. A nested/forked agent or remote Agent Protocol graph is not assumed to be independently viable merely because it is structurally nested; higher VSM functions require their own evidence at that boundary.

## Variety and escalation

Filesystem/tools and subagents amplify the root agent's operational variety. Context isolation and summarization attenuate context pressure. Async task state plus start/check/update/cancel/list rights provide a closed escalation/current-control path when concurrent background work needs intervention. HITL can stop selected actions, but it is not reclassified as an organizational function without function-specific ownership evidence.

## Evidence gaps

No evidence gap large enough to require `?` remains for the six published states at the pinned revision. A future reassessment should revisit S3* if the JS distribution adds a shipped runtime grader/challenger with complementary evidence access and corrective return, and S4 if memory/skills evolve into a distinct prospective adaptation loop rather than persistent context/procedure support.

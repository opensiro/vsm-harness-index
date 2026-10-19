---
harness_id: fennec-agent-runtime
project_name: Fennec Agent Runtime
repository: https://github.com/Fennec-AI/agent-runtime
review_ref: 3441fbde350df50cc070851856c343680babefb4
reviewed_at: 2026-10-19
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

# Fennec Agent Runtime

## Review boundary

- System in focus: Published first-party Python **agent runtime** composed from `Session`, a LangChain-backed recursive `query(ctx)` model/tool operating loop, and first-party tool dispatch, spawned subagents, background inbox delivery, cancellation and permission enforcement. The recursion assessed is one goal-facing agent operating cell with subtask agents. This is a source-bounded implementation assessment, **not** the original proprietary Claude Code product or a host organization employing a portfolio of agent departments.
- Purpose and identity: Complete an assigned user task via model-selected actions, optionally delegating bounded subtasks to recursively running child agents and returning their outcomes to the requesting parent session.
- Relevant environment: Changing file/workspace states, command and tool results, variable prompts and model replies, child-agent completion/error/cancellation, context pressure, malformed tool calls, user authorization and asynchronous notifications.
- First-party standard distribution: `agent_runtime/query.py`, `session.py`, `tool_executor.py`, `tools/spawn_agent.py`, `tools/task_output.py`, `tools/send_message.py`, `tools/task_stop.py`, `registry.py`, `cancellation.py`, `compaction/*`, `permissions.py`, `hooks.py`, `structured_output.py`, `bootstrap.py`, `models.py`, and `cli/config.py`. LangChain `BaseChatModel`, provider service and weights, third-party Claude Code source, and host-written application-specific agents are outside first-party organizational ownership.
- Credited operating / distribution surfaces: [README.md#L1](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/README.md#L1), [agent_runtime/query.py#L43](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/query.py#L43), [agent_runtime/query.py#L62](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/query.py#L62), [agent_runtime/query.py#L111](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/query.py#L111), [agent_runtime/query.py#L166](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/query.py#L166), [agent_runtime/session.py#L40](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/session.py#L40), [agent_runtime/session.py#L89](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/session.py#L89), [agent_runtime/tool_executor.py#L102](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/tool_executor.py#L102), [agent_runtime/tool_executor.py#L170](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/tool_executor.py#L170), [agent_runtime/tools/spawn_agent.py#L1](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/tools/spawn_agent.py#L1).
- Adjacent first-party surfaces excluded from ownership: Maintainer CI/tests, named Claude Code inspiration, research port comparisons, optional separately developed app orchestration, user-selected model provider accounts/keys, the larger external software organization and human authority. Test mocks and CLI demos document interfaces but are not independent successful agent/task outcome proof.
- Modes inspected: Default `Session.submit_message`, typed `run_structured`, recursive synchronous and background `Agent` tool, process-local agent registry and inbox, `TaskOutput` / `TaskStop` / `SendMessage`, permission modes `default`, `acceptEdits`, `plan` and `bypassPermissions` with optional user `ask_callback`, hooks, canceled runs and context compaction. Default model binding uses LangChain's external API but concrete first-party call/tool feedback is shipped.
- Recursion: A parent goal-facing operating S1 that may create child copies of the same `query` loop as *task-specific agents*. Child messages/roles and telemetry belong to that operating task relationship. Independent viable business divisions and an organizational management/audit policy layer are not silently inferred from the name `Agent` or the number of child tasks.
- Frozen source identity: GitHub repository ID **1249534702**, `Fennec-AI/agent-runtime` public `main@3441fbde350df50cc070851856c343680babefb4`, independent clean clone Git tree `4057b86c8d35356d6171be0f78685e350e3ea5ed`, [batch #1744](https://github.com/opensiro/vsm-harness-index/issues/1744). GitHub's license field did not provide a license classification, and no root LICENSE file was observed; do **not** infer an SPDX license. Reviewed 2026-10-19; active Profile 0.2.4 / Methodology 0.3.7.

## Repository architecture

A public `Session(llm, tools, permission_mode, ask_callback)` establishes a persistent `RunContext`, appends task messages and calls `query(ctx)`. `query` retrieves any background-child completion inbox messages, optionally compacts history, binds concrete tool definitions to the configured `BaseChatModel`, streams `llm.astream` and extracts the model's `tool_calls`. `run_tools` looks up those tools, preserves declared order, batches concurrency-safe calls, resolves permissions and invokes the concrete first-party handler, returning `ToolMessage` outcomes which `query` inserts into the same conversation before its next model step. It is a **shipped operational model–action–feedback path**, not only a stub Model interface. [agent_runtime/session.py#L40](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/session.py#L40); [agent_runtime/session.py#L89](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/session.py#L89); [agent_runtime/query.py#L62](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/query.py#L62); [agent_runtime/query.py#L111](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/query.py#L111); [agent_runtime/query.py#L166](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/query.py#L166); [agent_runtime/tool_executor.py#L102](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/tool_executor.py#L102); [agent_runtime/tool_executor.py#L170](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/tool_executor.py#L170).

The `SpawnAgentTool` is a normal model-selectable LangChain tool. It instantiates a child `RunContext` and recursively uses the same `query` loop. Synchronous operation awaits the child and returns final content; background operation schedules a child task and, when complete, sends a notification to the parent's process-local inbox. The parent either drains current notifications or waits for active children before considering its turn complete. `TaskOutput`, `TaskStop` and `SendMessage` expose child status/cancellation/message delivery. Cooperative abort propagates down an `AbortController` tree. This is robust task delegation and communication, but the source does not establish a separate **organizational inter-S1 conflict regulator** or current metasystem owner. [agent_runtime/tools/spawn_agent.py#L1](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/tools/spawn_agent.py#L1); [agent_runtime/tools/spawn_agent.py#L83](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/tools/spawn_agent.py#L83); [agent_runtime/query.py#L143](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/query.py#L143); [agent_runtime/registry.py#L1](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/registry.py#L1); [agent_runtime/cancellation.py#L1](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/cancellation.py#L1).

Permissions are checked on each tool action through `evaluate_permission`; a specified `ask_callback` can externalize an approval to the host human, and a denial is returned as an error tool result to the same model. The four named permission modes are operational tool safety settings. Optional hook handlers emit events and session histories; the `query` file explicitly labels pre-turn/pre-tool/post-tool and stop-hooks as **extension points**, with stop-hook behavior not implemented as an independent decision loop. Threshold model-driven context compaction summarizes the current conversation to keep the *same task/session* within token limits. Neither approval nor current-context summarization is by itself future capability strategy, complementary S3* audit or constitutional S5 adjudication. [agent_runtime/tool_executor.py#L170](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/tool_executor.py#L170); [agent_runtime/permissions.py#L1](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/permissions.py#L1); [agent_runtime/query.py#L70](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/query.py#L70); [agent_runtime/query.py#L162](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/query.py#L162); [agent_runtime/compaction/auto_compact.py#L47](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/compaction/auto_compact.py#L47).

## Operational model

One configured goal and model-facing conversation are converted to model-selected tool actions and a returned result. Scoped subtask agents can operate concurrently and report to the parent; process-local registry, cancellation, permission gates, history and compaction support this S1 cell. No automatically promoted organizational authority or prospective durable future strategy may be inferred from task-persistence or subagent transport.

## S1 — Operations

- State: A
- Function: Select model-guided actions and tool arguments for an assigned user task, observe their effects or errors and iteratively choose the next action or terminal response.
- Disturbance / variety regulated: Novel user instructions, file/tool observations, tool execution errors, rejected permissions, child task results and context-length growth.
- Decisive decision or feedback right: `ctx.llm` model in the shipped `query` loop emits `tool_calls` or final text and is fed the actual `ToolMessage` and child-inbox observations on the next iteration.
- Decision owner: Configured model acting through first-party `Session`/ `query` and `run_tools` boundary; LangChain/provider services transport inference and host sets tool grants but do not displace model selection of the next substantive task action.
- Supporting / enforcement mechanisms: First-party registry and `RunContext`, safety-filtered tool adapter, `BaseChatModel.bind_tools`, tool executor, child notifications, compaction, cancellation, events, user approval callback and typed terminal result facility.
- Closure path: Task → `Session.submit_message` / `query` → `llm.bind_tools(...).astream` → model-selected tool → `run_tools` permission check and `tool.ainvoke` → `ToolMessage` in history or child completion notification → same model re-evaluates → terminal result.
- Boundary reachability: The public `Session` facade invokes the shipped `query` and its tool-dispatch branch; `query` feeds concrete returned tool results into the next model call and `SpawnAgentTool` reuses it for children. The README quickstart connects the actual packaged `Session`, `bootstrap`, `default_tools()` and provider model, not an externally invented loop.
- Why this is / is not agent-owned: Without the model, the first-party tool dispatcher and safety infrastructure can execute preselected actions but cannot choose task-sensitive tool calls from new observations. The model owns the material S1 decision, bounded by host-selected tool grants.
- Evidence: [README.md#L72](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/README.md#L72), [agent_runtime/session.py#L40](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/session.py#L40), [agent_runtime/session.py#L89](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/session.py#L89), [agent_runtime/query.py#L110](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/query.py#L110), [agent_runtime/query.py#L181](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/query.py#L181), [agent_runtime/tool_executor.py#L102](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/tool_executor.py#L102), [agent_runtime/tool_executor.py#L170](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/tool_executor.py#L170), [agent_runtime/tools/spawn_agent.py#L83](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/tools/spawn_agent.py#L83).
- Basis: Concrete shipped model-call/tool-output return wiring, not extrapolation from README feature labels alone.
- Confidence: High for source-connected operating capability; no local provider inference validation.
- Caveats: External LangChain/provider and valid API key/runtime dependencies are needed to execute real tasks; a source-based A does not imply measured reliability or autonomy beyond the configured operating cell.

## S2 — Coordination

- State: —
- Function: No separate source-backed regulator of specific **interference/oscillation between independently viable S1 operating divisions** with altered reciprocal operating commitments is evidenced.
- Disturbance / variety regulated: Concurrent child tasks may compete for a shared worktree or return conflicting content; async notifications may arrive during parent streaming, but those issues are not the same as interference between independent business S1 systems.
- Decisive decision or feedback right: Parent operating model selects subtask calls and may send messages, poll or cancel; runtime has deterministic safe-tool batching and inbox delivery. Neither path senses concrete inter-S1 department conflict, decides dampening, and returns binding mutual adjustment to two viable operating units.
- Decision owner: Same parent operating model / host task instructions for delegation, process-local routing and task cancellation code for transport/enforcement.
- Supporting / enforcement mechanisms: `SpawnAgentTool`, `TaskOutput`, `TaskStop`, `SendMessage`, `AGENT_REGISTRY`, inbox drain and concurrency semaphore, cooperative cancellation.
- Closure path: Parent delegates → child returns or notifies → parent continues current user task; no multi-S1 shared operational interference → distinct coordinating judgment → changed independent operating commitments.
- Why this is / is not agent-owned: Model mediation of child tasks is still the parent S1 operating decision. A messenger, task graph or transport does not automatically confer the S2 function.
- Evidence: [agent_runtime/tools/spawn_agent.py#L1](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/tools/spawn_agent.py#L1), [agent_runtime/query.py#L143](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/query.py#L143), [agent_runtime/query.py#L210](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/query.py#L210), [agent_runtime/tool_executor.py#L102](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/tool_executor.py#L102), [agent_runtime/registry.py#L1](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/registry.py#L1).
- Basis: Source-bounded negative after inspecting real child task, process-inbox and safe-batch modes.
- Confidence: Medium-high at the declared one-goal operating recursion.
- Caveats: A downstream application could install multiple independently viable S1 agents and new conflict-regulating logic; it would require its own evidence and recursion.

### Absence scope

- Surfaces inspected: Recursive agent tree, child-tool status/message/cancellation, inbox registry, concurrent tool batches and cleanup.
- Plausible first-party paths checked: Child tool/result collisions, multiple agent messages, parent model-directed rerouting, canceled competing subagents.
- Why no material first-party path remains: No first-party path establishes a distinct observer/judge of disturbances *between independent operational S1 divisions* that returns coordinated changed rights or behavior to affected units; only per-goal delegation and transport are present.



## S3 — Inside-and-now control

- State: —
- Function: No first-party whole-current management owner of a portfolio of independently viable S1 operations that reviews present obligations/resources and sends binding managerial adjustments.
- Disturbance / variety regulated: Depth/max-turn constraints, cancellation, shell timeout, active child tasks, approval and context budget threaten single-task execution, but not whole-organizational current performance accountability.
- Decisive decision or feedback right: User/host configures permission mode, tools, model and `max_turns`; parent model selects child task instructions, and runtime applies fixed deterministic run limits. No source-backed separate managerial owner negotiates resource allocations or current organizational commitments.
- Decision owner: Application operator for delegated bounds and parent operating model for subtask choices; deterministic runtime for enforcement.
- Supporting / enforcement mechanisms: `Session`, `RunContext`, `CONFIG`, `TaskStop`, abort tree, registry, permission callback and structured output checking.
- Closure path: Task or tool requests action → configured permission/depth/abort gate applies → same task continues or ends. No whole-current manager's operating overview → change in S1 portfolio priorities/resources → returned operational adjustment.
- Why this is / is not agent-owned: A class called `Session` or parent worker does not by itself own discretionary current management of a viable multi-unit organization.
- Evidence: [agent_runtime/session.py#L40](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/session.py#L40), [agent_runtime/query.py#L102](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/query.py#L102), [agent_runtime/tool_executor.py#L170](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/tool_executor.py#L170), [agent_runtime/cancellation.py#L1](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/cancellation.py#L1), [agent_runtime/config.py#L1](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/config.py#L1).
- Basis: Source-bounded negative for registered source modes, including child and approval routes.
- Confidence: Medium-high.
- Caveats: Human S3 or autonomous management could exist externally at a higher application boundary; not imported.

### Absence scope

- Surfaces inspected: Session/RunContext settings, model/permission/depth policy, child cancellation, process registry, concurrent-tools controls.
- Plausible first-party paths checked: Whole-current resource reallocation, handling stalled background jobs, task priority shifts and approval-level adjustments.
- Why no material first-party path remains: Decisions are task-local model operations or deterministic/host-supplied limits; no separate first-party managerial mandate over multiple independently viable S1 units and binding current-regulation return is evidenced.



## S3* — Complementary audit

- State: —
- Function: No independent complementary operational-reality inspection of S1/S3 claims with a corrective feedback path to a current S3 executive is established.
- Disturbance / variety regulated: Tool errors, unsafe actions and malformed typed answers are observable and may be denied or retried. Those observations do not constitute independent challenge of an S3 operating picture.
- Decisive decision or feedback right: `evaluate_permission` may call an external approval callback; hooks log/observe tool use; structured output Pydantic validation checks schema during the same task. No separate first-party S3* correction mandate is wired.
- Decision owner: Host approval callback and deterministic tool/typed response checks; not a complementary independent auditor with rights over a current S3 manager.
- Supporting / enforcement mechanisms: Tool-level `pre_tool`/ `post_tool`/ `on_error` hooks, `permission_denied` events, `run_structured`, transcript history, registry/cancellation.
- Closure path: Tool result or approval decision → returned ToolMessage / validation action / log → current S1 loop; no independent reality sample → corrective S3 audit finding → revised S3 current control.
- Why this is / is not agent-owned: Permission review and output validation are local action controls, not S3* regardless of their security value.
- Evidence: [agent_runtime/tool_executor.py#L170](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/tool_executor.py#L170), [agent_runtime/permissions.py#L1](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/permissions.py#L1), [agent_runtime/hooks.py#L1](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/hooks.py#L1), [agent_runtime/session.py#L107](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/session.py#L107).
- Basis: Function-first negative: checked concrete validation and hook/approval closure.
- Confidence: Medium-high.
- Caveats: A downstream independent evidence checker could leverage the logs, but no such authority is credited.

### Absence scope

- Surfaces inspected: Permission modes and ask_callback, pre/post/error tool hooks, typed structured output, registry logs and session transcript.
- Plausible first-party paths checked: External inspection of tool effects, checking tool/agent reports against ground truth, correcting S3 decisions and future audit accountability.
- Why no material first-party path remains: Available checks are current-task authorization/schema validation/observability and have no independent S3 operational-reality audit intake, judgement and corrective management return.



## S4 — Outside-and-then intelligence

- State: —
- Function: No model-owned proactive future environment distinction, prospective organizational adaptation option and **adoption back to changed durable future operating capability** is evidenced in the shipped default or alternate documented modes.
- Disturbance / variety regulated: Long conversations, differing tool results and future continuation after a child completes can require local context adjustment, but not a durable new strategy for a later independent operational cycle.
- Decisive decision or feedback right: `auto_compact_if_needed` may ask the configured model to summarize the current history and replace messages at a context threshold; `Session` persists current messages; `TodoWrite` updates current task checklist. None owns prospective changes to installed tools, goals, model policies or future agent skill capabilities.
- Decision owner: Same operating loop's compaction / task model and application for any later configuration changes; no distinct S4 adaptation right.
- Supporting / enforcement mechanisms: `compaction/auto_compact.py`, `microcompact.py`, token budget, messages and action history, child completion notifications, TODO list tool.
- Closure path: Growing current transcript → compact summary in same messages list → same model continues current task; missing prospective future environmental distinction → approved strategy change → reused operational capability loop.
- Why this is / is not agent-owned: Model-written conversation summaries are still local operating-context maintenance, not strategy ownership. No first-party future-option development and adoption is returned into later independent runs.
- Evidence: [agent_runtime/query.py#L74](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/query.py#L74), [agent_runtime/compaction/auto_compact.py#L47](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/compaction/auto_compact.py#L47), [agent_runtime/session.py#L89](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/session.py#L89), [agent_runtime/tools/todo_write.py#L1](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/tools/todo_write.py#L1), [README.md#L24](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/README.md#L24).
- Basis: Bounded negative after reviewing persistent session/child and compaction modes.
- Confidence: Medium-high.
- Caveats: Host developers could expose a model-written durable skill/update tool, but that would be a new application-owned construction and is not credited here.

### Absence scope

- Surfaces inspected: Model-backed context compaction, microcompaction, persistent Session history, TODO tool, child background notifications, config and hooks.
- Plausible first-party paths checked: Knowledge from tool outcomes generalized to future agent skills, evolving policy/model selection or a future strategy deployment.
- Why no material first-party path remains: No shipped first-party path generates prospective organizational change options and closes their adoption into durable later S1 capability; compaction and message history only support immediate task continuation.



## S5 — Policy and identity

- State: —
- Function: No legitimate first-party ultimate-purpose/identity decision authority with returned enduring binding organizational policy is evidenced.
- Disturbance / variety regulated: Potentially destructive shell/file tools, elevated permission modes and background subagent lifecycle require user approval/limits, but no constitutional identity-level dispute is admitted or decided.
- Decisive decision or feedback right: Host user supplies permission mode and optional `ask_callback`; runtime checks allow/deny/ask for tool actions. `bypassPermissions` is a caller-selected setting, not first-party S5 policy-making authority.
- Decision owner: External user/application actor for authorization; deterministic runtime evaluates delegated boundaries and operating model chooses permitted task actions.
- Supporting / enforcement mechanisms: PermissionMode, AskCallback, per-tool allow/deny, tool/child cancellation, logs and optional hooks.
- Closure path: Tool requests action → policy gate/host callback → tool executes or denial returned to current agent; no ultimate identity question reaches a legitimate authority and returns as binding constitutional policy governing future task contexts.
- Why this is / is not agent-owned: Even a high-friction human gate is not itself a functioning organizational S5 policy/identity constitution.
- Evidence: [agent_runtime/session.py#L40](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/session.py#L40), [agent_runtime/permissions.py#L1](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/permissions.py#L1), [agent_runtime/tool_executor.py#L170](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/agent_runtime/tool_executor.py#L170), [README.md#L31](https://github.com/Fennec-AI/agent-runtime/blob/3441fbde350df50cc070851856c343680babefb4/README.md#L31).
- Basis: Bounded negative after checking all named permission modes.
- Confidence: Medium-high.
- Caveats: External human owners retain real final purpose/policy rights; no internally self-deciding S5 organization is claimed.

### Absence scope

- Surfaces inspected: Tool permission modes, ask_callback human gate, read-only subagent defaults, cancellation and named extension hooks.
- Plausible first-party paths checked: Tool authorization and policy exceptions, organizational identity question intake, revision of future ultimate-policy constraints.
- Why no material first-party path remains: First-party paths only enforce already-selected current-task security policy or await an outside callback, without a legitimate identity-deciding policy owner and durable return to organizational control.



## Recursion

One user goal-facing parent model agent with child copies of the same operating loop. The visible parallel child tool trees, notification inbox and cancellation hierarchy are valuable operational scaling facilities. They do not change recursion into a proven independent S1 federation or constitute S2/S3/S3*/S4/S5 on their own.

## Variety and escalation

Tool error messages, human permission denials, background child notifications and process cancellation flow into the same current operating loop. Context pressure is attenuated by compaction, which is explicitly a current-conversation resource mechanism. A denial/hook or high-priority background result is not automatically an algedonic signal to a different legitimate VSM metasystem owner.

## Evidence gaps

- The isolated Linux source-review runner lacked `langchain_core` (`ModuleNotFoundError`) on import preflight. No packaged agent inference, upstream Python test suite or tool-effect performance result was independently executed. This is an **environment dependency limit**, not proof of an upstream defect.
- The source repo contained no root license text file and GitHub metadata returned no SPDX classification at review time. Legal reuse/license permission is **not assessed** and no public MIT/Apache license is assumed.
- The repository's own README identifies this as a **study/port** of Claude Code's loop slice, not a drop-in reproduction. Neither original Claude Code internal features nor third-party model runtime behavior are credited beyond explicitly connected first-party integration.
- Assessment `status: proposed` does not imply canonical catalog/signature admission until the distinct reviewable canonical transaction passes dual exact-head GitHub CI.

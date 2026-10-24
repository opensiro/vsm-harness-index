---
harness_id: bub
project_name: Bub
repository: https://github.com/bubbuild/bub
review_ref: 71d7dbf82f9e7145aabf53ab562c1d376bb3e0e2
reviewed_at: 2026-10-25
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

# Bub

## Review boundary

- System in focus: The first-party installable Bub agent kernel, configured `BubAgent`, tools, channel manager and plugin hooks, not a user's custom plugin-based organization or the maintainers of the public repository.
- Purpose and identity: Run conversational/tool-use tasks through a model-backed feedback loop, expose configured tools and skills, route interactive channel messages and optionally delegate a bounded subtask.
- Relevant environment: Variable user requests, model decisions, tool outputs and errors, incoming channel messages, session histories, tool/provider availability and interruption requests. Future organizational environment and ultimate identity disputes are not represented as dedicated control functions.
- Standard-distribution boundary: `src/bub/core/agent.py`, `src/bub/builtin/agent.py`, bundled tools including `subagent`, channel turn admission and first-party hook implementation. An embedding developer may add policies, tools and channels; arbitrary external plugins are not credited as bundled autonomous functions.
- Credited operating / distribution surfaces: [core agent](https://github.com/bubbuild/bub/blob/71d7dbf82f9e7145aabf53ab562c1d376bb3e0e2/src/bub/core/agent.py), [configured agent](https://github.com/bubbuild/bub/blob/71d7dbf82f9e7145aabf53ab562c1d376bb3e0e2/src/bub/builtin/agent.py), [built-in subagent tool](https://github.com/bubbuild/bub/blob/71d7dbf82f9e7145aabf53ab562c1d376bb3e0e2/src/bub/builtin/tools.py), [channel manager](https://github.com/bubbuild/bub/blob/71d7dbf82f9e7145aabf53ab562c1d376bb3e0e2/src/bub/channels/manager.py), [tool executor](https://github.com/bubbuild/bub/blob/71d7dbf82f9e7145aabf53ab562c1d376bb3e0e2/src/bub/core/tools.py), [plugin hooks](https://github.com/bubbuild/bub/blob/71d7dbf82f9e7145aabf53ab562c1d376bb3e0e2/src/bub/builtin/hook_impl.py).
- Adjacent first-party surfaces excluded from ownership: Developer/contributor activity, sample agent configurations, external model provider intelligence, external application-specific admission/approval plugins, integration tests and a possible downstream multisystem organization. Tests corroborate shipped implementation; they do not supply otherwise missing governance owners.
- First-party operating / deployment modes considered: Normal CLI/chat-channel agent with tool-use iterations; multi-session `BubAgent.run_stream`; direct and code-mode tools; `subagent` with inherited, temporary or named session; channel turn admission/steering, configured hook interception and operator-set allowlists. No live model or LLM-agent test was conducted.
- Recursion level: An operational agent can call another run of the same agent instance as a subtask and receive text/error results. That nesting does not instantiate an independent organizational metasystem.
- Reviewed revision: `71d7dbf82f9e7145aabf53ab562c1d376bb3e0e2` from [frozen discovery #2024](https://github.com/opensiro/vsm-harness-index/issues/2024) and [serial queue #2025](https://github.com/opensiro/vsm-harness-index/issues/2025).
- Observation date: 2026-10-25.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

First-party `core.Agent._run_steps` runs a bounded sequence of model completions, emits step events, executes model-selected tools through `run_once`, records outcomes in a tape and proceeds to another model step when tool calls/results or pending messages require continuation. The caller configures the model and tools, while the agent uses changing observations to decide its next action. `BubAgent.run_stream` loads per-turn session state and permissions/skills and invokes that same kernel. [agent loop](https://github.com/bubbuild/bub/blob/71d7dbf82f9e7145aabf53ab562c1d376bb3e0e2/src/bub/core/agent.py#L471-L536), [stream integration](https://github.com/bubbuild/bub/blob/71d7dbf82f9e7145aabf53ab562c1d376bb3e0e2/src/bub/builtin/agent.py#L88-L150).

The bundled `subagent` tool launches `agent.run_stream` on the *same* runtime instance in an inherited, temporary or named session; the child is given a task prompt and optional model/tool/skill subset, with the `subagent` tool deliberately removed from the child's available tools. It awaits and aggregates the resulting text/errors. This is genuine bounded operational delegation, but it does not implement independent managers, agent-population reconciliation or recursive viability. [subagent implementation](https://github.com/bubbuild/bub/blob/71d7dbf82f9e7145aabf53ab562c1d376bb3e0e2/src/bub/builtin/tools.py#L493-L522), [deterministic subagent test](https://github.com/bubbuild/bub/blob/71d7dbf82f9e7145aabf53ab562c1d376bb3e0e2/tests/test_subagent_tool.py#L35-L54).

`ChannelManager` tracks active/pending turns per session and applies pluggable `process`/`drop`/`follow_up`/`steer` admission decisions. The built-in CLI mode steers new text into an already-running *same-session* turn; the default generic channel manager **keeps concurrent processing** in the absence of a relevant external admission decision. Those are intra-session interaction controls, not an evidenced inter-agent S2 resolution protocol. [admission path](https://github.com/bubbuild/bub/blob/71d7dbf82f9e7145aabf53ab562c1d376bb3e0e2/src/bub/channels/manager.py#L231-L329), [default concurrency test](https://github.com/bubbuild/bub/blob/71d7dbf82f9e7145aabf53ab562c1d376bb3e0e2/tests/test_channels.py#L862-L881).

## Operational model

An operator supplies a task, model and tool/configuration boundary. The model-backed agent selects next content/actions and observes tool outcomes; it can invoke a subordinate task and fold that result into its current work. A channel administrator or plugin may accept/steer/queue messages, while configured policies can reject tool calls. No first-party evidence establishes a specialized conflict-aware exchange among two independent operating agents, current organization-wide task/resource decision maker, independent complementary auditor, prospective capability planner or ultimate-policy authority.

## S1 — Operations

- State: A
- Function: Autonomously complete assigned tasks via model-selected tool actions and feedback-informed next model steps.
- Disturbance / variety regulated: User goals, tool-return data, execution errors, changing session messages and provider responses require task-specific action selection.
- Decisive decision or feedback right: The model chooses content and offered tool invocations; the first-party agent executes chosen calls and exposes the results to subsequent model decisions.
- Decision owner: Configured model-backed `Agent`/`BubAgent` work cell; the external inference service supplies decisions through a deliberately integrated provider interface.
- Supporting / enforcement mechanisms: Tape/history, tool call executor, bounded model steps, events, per-session state, skills, configured permissions and optional subtask call.
- Closure path: `BubAgent.run_stream` → `Agent.start`/`_run_steps` → `run_once`/model streaming → model-selected tool call → `ToolExecutor` and tool result → recorded tape/model context → next step or final output.
- Boundary reachability: `BubAgent` and core `Agent` are concrete installable first-party runtime classes; normal configured operation reaches this loop without an application-defined replacement agent.
- Why this is / is not agent-owned: The tool executor, session handler and fixed step caps cannot themselves select a semantic next action from task/observation content. The configured model-backed work cell does.
- Evidence: [implemented step loop](https://github.com/bubbuild/bub/blob/71d7dbf82f9e7145aabf53ab562c1d376bb3e0e2/src/bub/core/agent.py#L471-L536); [model streaming](https://github.com/bubbuild/bub/blob/71d7dbf82f9e7145aabf53ab562c1d376bb3e0e2/src/bub/core/agent.py#L596-L638); [configured turn](https://github.com/bubbuild/bub/blob/71d7dbf82f9e7145aabf53ab562c1d376bb3e0e2/src/bub/builtin/agent.py#L88-L150); [first-party subtask](https://github.com/bubbuild/bub/blob/71d7dbf82f9e7145aabf53ab562c1d376bb3e0e2/src/bub/builtin/tools.py#L493-L522).
- Basis: Structural source inspection of the first-party model/tool/result feedback loop and published standard runtime.
- Confidence: High for implemented decision loop; no live-model efficacy/safety claim.
- Caveats: Requires a configured model and runtime tools. A standalone subtask is not automatically a separately viable management layer.

## S2 — Coordination

- State: —
- Function: No shipped conflict-specific regulator is evidenced that detects and attenuates disturbances *between* two independently operating S1 units.
- Disturbance / variety regulated: Two sessions/subtasks may compete for shared tools, write to common resources or generate inconsistent proposals; first-party path does not detect or settle such cross-agent interference.
- Distinct S1 units: Separate configured `BubAgent` instances or task runs can host model-backed loops; the `subagent` tool uses the parent's own runtime, only changing the session/tool scope.
- Inter-S1 disturbance: No concrete peer-conflict signal, oscillation detector, ownership collision or resource contention reconciliation is found in the shipped subagent/admission path.
- Attenuating coordination relation: Channel admission affects new *messages* and session activity; subagent delegation waits for an output; tool executor gathers concurrent calls without a shared-work conflict policy.
- Feedback into subsequent S1 behaviour: Model can read delegated text/error results as ordinary work input, but no inter-S1 conflict outcome is fed back under a dedicated coordination decision.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: Message admission and worker handoff are mechanisms that a larger S2 might use, not proof of a particular collision or disagreement and its mitigation. Explicit first-party default concurrency test confirms admission is not a universal serializing inter-agent guard.
- Decisive decision or feedback right: User/plugin provides optional admission policy; first-party code applies `AdmitDecision`, not an inter-agent reconciliation rule.
- Decision owner: No qualified S2 owner in the reviewed first-party boundary.
- Supporting / enforcement mechanisms: Session pending queue, steering inbox, `quit` cancellation, model tool allowlist, optional tool concurrency limiter, `subagent` prompt/result.
- Closure path: Incoming session message → optional admission decision → process/drop/queue/steer; parent subtask call → child output. Neither closes detected inter-S1 interference into revised multiple-agent work.
- Why this is / is not agent-owned: Model-originated delegation can be autonomous S1 task decomposition, but the admission actions are externally provided or single-session controls, not an agent-owned cross-S1 stabilization function.
- Evidence: [subagent call and result](https://github.com/bubbuild/bub/blob/71d7dbf82f9e7145aabf53ab562c1d376bb3e0e2/src/bub/builtin/tools.py#L493-L522); [admission decision actions](https://github.com/bubbuild/bub/blob/71d7dbf82f9e7145aabf53ab562c1d376bb3e0e2/src/bub/channels/manager.py#L263-L329); [concurrent tool calls](https://github.com/bubbuild/bub/blob/71d7dbf82f9e7145aabf53ab562c1d376bb3e0e2/src/bub/core/tools.py#L319-L352); [default concurrent turns test](https://github.com/bubbuild/bub/blob/71d7dbf82f9e7145aabf53ab562c1d376bb3e0e2/tests/test_channels.py#L862-L881).
- Basis: Bounded negative on first-party multi-run and channel interfaces.
- Confidence: Medium-high.
- Caveats: A consumer-supplied admission hook could build an inter-agent policy; absent concrete shipped ownership, it is not credited to Bub.

### Absence scope

- Surfaces inspected: Subagent input/call and tests, `BubAgent` session API, manager admission/steering, built-in hook, tool concurrency and channel tests.
- Plausible first-party paths checked: Parallel tool gathering, child tool exclusions, inherited/temporary child session, incoming-message steering, queue/drop/follow-up, active-session cancellation and concurrency default.
- Why no material first-party path remains: The observed effects scope task delegation, tool execution or same-session admission. No built-in detector/attenuator with evidence of a distinct inter-S1 disturbance and closed return was found.

## S3 — Inside-and-now control

- State: —
- Function: No first-party manager appraises the current *whole* of active operational units and revises their shared task commitments, resource allocations or priorities.
- Disturbance / variety regulated: Concurrent sessions and subtask work could consume capacity or drift from higher-level objectives, but the standard controls manage one run or a fixed session queue.
- Decisive decision or feedback right: The operator supplies tasks/permissions/models and may interrupt a session; a model can choose to call a child for its own task but cannot, through the shipped subagent tool, inspect/rebalance an active agent organization.
- Decision owner: Caller/developer for population topology and process settings; one operational parent model for task delegation, not an established separate whole-current manager.
- Supporting / enforcement mechanisms: `ChannelManager.active_tasks`, turn snapshots, `quit`, tool budgets/`max_steps`, parent/child session IDs and optional hooks.
- Closure path: One parent awaits subtask output; individual sessions can be interrupted or queued. No whole-current appraisal → commitment/resource choice → changed operating-unit priorities exists.
- Why this is / is not agent-owned: The model chooses whether to decompose its present request, but that decision remains S1 production without current-organization visibility or binding portfolio-level resource rights.
- Evidence: [subagent single-run invocation](https://github.com/bubbuild/bub/blob/71d7dbf82f9e7145aabf53ab562c1d376bb3e0e2/src/bub/builtin/tools.py#L493-L522); [session-specific quit and active task list](https://github.com/bubbuild/bub/blob/71d7dbf82f9e7145aabf53ab562c1d376bb3e0e2/src/bub/channels/manager.py#L141-L169); [bounded local agent steps](https://github.com/bubbuild/bub/blob/71d7dbf82f9e7145aabf53ab562c1d376bb3e0e2/src/bub/core/agent.py#L471-L536).
- Basis: Bounded negative after inspecting apparent parent-control affordances.
- Confidence: Medium-high.
- Caveats: A custom app can assemble an S3 using the hooks and child results; that would be a different organizational boundary.

### Absence scope

- Surfaces inspected: Core model steps/budgets, `BubAgent` turn state, subagent tool, channel active/pending tasks, `quit`, framework hooks and session controller.
- Plausible first-party paths checked: Parent delegating to child, watching progress/events, cancelling session tasks, model/tool restrictions, multi-session processing and hook-supplied admission policy.
- Why no material first-party path remains: These support local execution and externally configured policy, not an installed parent with whole-current situational synthesis and authority to revise collective commitments.

## S3* — Complementary audit

- State: —
- Function: No independently sourced audit of operational claims that returns a corrective finding to a distinct current-control owner is evidenced.
- Disturbance / variety regulated: Model or tool outputs may be wrong; tape events, tool failures and optional hooks expose the producer's own record, not independent verification.
- Decisive decision or feedback right: Operator/plugins may inspect traces or reject tool calls, but the first-party runtime has no separate auditor deciding the credibility of S1 reports against independent ground truth.
- Decision owner: None for an S3*-qualified audit channel; producer agent owns task output and caller owns external tests.
- Supporting / enforcement mechanisms: Tape entries, tracing, `before_tool_call` and `after_tool_call`, event subscriptions, error notifications and SDK test fixtures.
- Closure path: Producer's tool result/event is logged and fed to its own loop; no separate independent evidence check → audit opinion → corrective S3 control return is wired.
- Why this is / is not agent-owned: Trace creation and permission checks are deterministic observability/execution controls, not an autonomous independent challenge to production claims.
- Evidence: [built-in tool hook](https://github.com/bubbuild/bub/blob/71d7dbf82f9e7145aabf53ab562c1d376bb3e0e2/src/bub/builtin/hook_impl.py#L322-L381); [agent step events](https://github.com/bubbuild/bub/blob/71d7dbf82f9e7145aabf53ab562c1d376bb3e0e2/src/bub/core/agent.py#L471-L546); [tool traces](https://github.com/bubbuild/bub/blob/71d7dbf82f9e7145aabf53ab562c1d376bb3e0e2/src/bub/core/tools.py#L353-L405).
- Basis: Bounded negative first-party production and observation review.
- Confidence: Medium-high.
- Caveats: Future custom reviewer/plugin functionality should be assessed at its own operating boundary, with separate evidence rights.

### Absence scope

- Surfaces inspected: Tool interception/reporting hooks, tape and trace outputs, stream/error events, subagent return, channel outcomes and tests.
- Plausible first-party paths checked: Tool call validation, event logging, session replay, subtask inspection, error reporting and model-generated review text.
- Why no material first-party path remains: No bundled auditor obtains complementary independent evidence and returns its challenge to a distinct S3 owner; local logs or caller tests cannot supply that missing circuit.

## S4 — Outside-and-then intelligence

- State: —
- Function: No first-party loop senses prospective outside changes, selects future organizational adaptations and returns adopted capability changes to present operation.
- Disturbance / variety regulated: Model/tool/provider shifts and emerging user needs may require future changes, but the runtime responds to current tasks and loads operator-configured capabilities.
- Decisive decision or feedback right: Operators select model, tools and skills; model calls/retries within a task have only current-request authority.
- Decision owner: Developer/operator for installed capacity and configuration, not a dedicated prospective S4 owner.
- Supporting / enforcement mechanisms: Model selection, skill discovery, deferred tool loading, plugin registration, `set_model`, context handoff and web fetching as a task tool.
- Closure path: Operator changes tools/provider/skills and runs again; present-task fetch/feedback can inform next local answer but not strategic adoption based on future-environment appraisal.
- Why this is / is not agent-owned: An S1 may research a future-facing question, but its output is not a first-party future capability governance cycle.
- Evidence: [agent skill/tool scope](https://github.com/bubbuild/bub/blob/71d7dbf82f9e7145aabf53ab562c1d376bb3e0e2/src/bub/builtin/agent.py#L150-L211); [built-in tool/provider controls](https://github.com/bubbuild/bub/blob/71d7dbf82f9e7145aabf53ab562c1d376bb3e0e2/src/bub/builtin/tools.py#L493-L603); [local context recovery](https://github.com/bubbuild/bub/blob/71d7dbf82f9e7145aabf53ab562c1d376bb3e0e2/src/bub/core/agent.py#L497-L520).
- Basis: Bounded negative on operating, capability and extension surfaces.
- Confidence: Medium-high.
- Caveats: A larger organization may separately build environmental intelligence with these tools; standard Bub does not evidence that circuit.

### Absence scope

- Surfaces inspected: Core loop and error recovery, skill discovery, model settings and switching, web-fetch tool, external hooks and channel manager.
- Plausible first-party paths checked: Future-oriented prompts, external web retrieval, dynamic skill availability, deferred tool discovery, configurable provider and context reset/handoff.
- Why no material first-party path remains: All inspected paths support current production or developer-selected capability changes; none owns a prospective environmental forecast, adaptation decision and adoption-return chain.

## S5 — Policy and identity

- State: —
- Function: No ultimate identity/policy governance channel with legitimate authority, escalation and binding return is instantiated by the shipped system.
- Disturbance / variety regulated: Unsafe tools, unexpected user messages and forbidden capabilities are addressed by first-party hooks, allowlists and operator configuration, not identity-level constitutional arbitration.
- Decisive decision or feedback right: Operators configure tool/model access; plugin tool-call decisions can block/rewrite individual calls. No distinguished S5 holder adjudicates conflicting mission/identity rules and returns binding system policy.
- Decision owner: Outside operator/developer for application policy; model work cell for task-level responses, not S5.
- Supporting / enforcement mechanisms: `allowed_tools`/`allowed_skills`, `before_tool_call` interception, `ToolCallDecision`, CLI quit and channel admission hooks.
- Closure path: A disallowed tool call can be refused or a message queued/dropped; nothing escalates a normative identity dispute to a legitimate final authority with durable policy revision.
- Why this is / is not agent-owned: Configured constraints operate within S1 tasks; an interactive user or plugin is not automatically a defined constitutional authority.
- Evidence: [turn capability scope](https://github.com/bubbuild/bub/blob/71d7dbf82f9e7145aabf53ab562c1d376bb3e0e2/src/bub/builtin/agent.py#L151-L174); [tool interception](https://github.com/bubbuild/bub/blob/71d7dbf82f9e7145aabf53ab562c1d376bb3e0e2/src/bub/core/tools.py#L457-L499); [channel admission](https://github.com/bubbuild/bub/blob/71d7dbf82f9e7145aabf53ab562c1d376bb3e0e2/src/bub/channels/manager.py#L231-L329).
- Basis: Bounded negative on first-party operator and hook policy interfaces.
- Confidence: Medium-high.
- Caveats: External deployment governance cannot be imported as runtime S5 merely because a human operator exists.

### Absence scope

- Surfaces inspected: Run configuration, permissions and tools, first-party hooks, channel admission, quit handling, model control and organizational contributor boundary.
- Plausible first-party paths checked: Permission-denied tool results, session interruption, model capability restrictions, dynamically registered policy plugin and caller/operator prompts.
- Why no material first-party path remains: These are execution gates or potential external extension points. No first-party identity decision owner, corresponding escalation or authoritative rule-return path is implemented.

## Distributed OSS parent arrangement

The public Bub repository and contributors maintain a reusable runtime, not the live managerial parent of each installed deployment. A downstream operator may compose a broader organization through plugins or multiple instances, but such a parent requires separate evidence and cannot be borrowed from open-source maintainers or a command-line user's presence.

## Self-hosted and non-human modes

First-party `BubAgent` serves noninteractive sessions and can be self-hosted with an available model endpoint; it can select tools and finish tasks without human intervention. Per-session allowlists and CLI user steering are optional execution controls. Neither configuration proves S2–S5 autonomously.

## Recursion

`subagent` executes a child task via the same `BubAgent` instance with a new/inherited session, awaits the result and deliberately excludes its own tool from the child's tool set. This is bounded task recursion with no automatically deployed child coordination/control/audit/policy structure.

## Variety and escalation

Within-task model/tool feedback handles task variety. Step limits and context-overflow handoff bound local execution; tool errors and session steering/cancellation affect immediate operation. No evidence traces a distinct S1 conflict or exceptional signal into an independent multi-level S2–S5 governance response.

## Evidence gaps

- Assessment is source-based at the frozen revision; no model-backed tasks, external benchmarks or LLM-agent tests were run. Shipped tests are cited as implementation evidence only.
- Different application plugins may use `AdmitDecision` for inter-agent coordination or establish independent reviewers; no such concrete standard operating circuit is evidenced in the frozen repository.
- Negative states refer to the installed, first-party standard boundary; they are not claims that no consumer could build larger organizational functions with Bub.

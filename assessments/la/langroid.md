---
harness_id: langroid
project_name: Langroid
repository: https://github.com/langroid/langroid
review_ref: 1e0f5ab7d9d589d79928c39ed147ca8a2bd6a590
reviewed_at: 2026-10-25
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Langroid

## Review boundary

- System in focus: The shipped Python Langroid agent and task-execution framework, including `Agent`, `ChatAgent`, `Task`, its documented nested subtask mode, built-in oscillation guard, tool execution and optional packaged LanceRAG task constructor. Not the organization developing Langroid or any consumer's entire custom application.
- Purpose and identity: Execute language-model-powered tasks and tools with feedback; allow operators to compose autonomous task actors into directed, nested conversations while guarding pathological execution loops.
- Relevant environment: User goals, message contents, provider responses, tool and retrieval observations, unavailable responder output, multi-actor response cycles, cost/turn budgets and operator interaction. Future markets and identity governance lie outside the framework's own decision loop.
- Standard-distribution boundary: Installable first-party `langroid/agent/` runtime and publicly documented `ChatAgent`/`Task` API, with user-supplied goals, LLM provider and tool/agent configs. The optional shipped LanceRAG task builder is inspected as a first-party supported composition, not used to credit consumer-defined orchestration.
- Credited operating / distribution surfaces: [ChatAgent model response and history](https://github.com/langroid/langroid/blob/1e0f5ab7d9d589d79928c39ed147ca8a2bd6a590/langroid/agent/chat_agent.py), [base Agent tool execution](https://github.com/langroid/langroid/blob/1e0f5ab7d9d589d79928c39ed147ca8a2bd6a590/langroid/agent/base.py), [Task responder loop/delegation and loop guard](https://github.com/langroid/langroid/blob/1e0f5ab7d9d589d79928c39ed147ca8a2bd6a590/langroid/agent/task.py), [TaskTool](https://github.com/langroid/langroid/blob/1e0f5ab7d9d589d79928c39ed147ca8a2bd6a590/langroid/agent/tools/task_tool.py), [first-party LanceRAG constructor](https://github.com/langroid/langroid/blob/1e0f5ab7d9d589d79928c39ed147ca8a2bd6a590/langroid/agent/special/lance_rag/lance_rag_task.py).
- Adjacent first-party surfaces excluded from ownership: Examples/`tests/`, benchmarks, evaluation notebooks, developer/contributor agent skills, CI/release maintenance, third-party LLM/provider decisions outside the installed model-call interface, user-defined coordinating teams, and special RAG components not actively wired into an installed task mode. Tests are used as corroboration for production code, not credited as executing agents.
- First-party operating / deployment modes considered: Default model-backed `ChatAgent` within a synchronous/asynchronous `Task.run`; tools handled by `agent_response`; named nested subtasks with model-directed addressing/`SEND_TO`/`PASS_TO`, interactive or non-interactive operation; built-in exact-message and `NO_ANSWER` cycle protection; optional first-party three-actor LanceRAG planner/RAG/critic task. No live model/provider test was run.
- Recursion level: The framework-composed execution of a user task with one or multiple model-backed work cells. A nested responder or `Task` object is not alone evidence of a fully viable recursive organization.
- Reviewed revision: `1e0f5ab7d9d589d79928c39ed147ca8a2bd6a590`, frozen in [discovery #2024](https://github.com/opensiro/vsm-harness-index/issues/2024) and [serial batch #2025](https://github.com/opensiro/vsm-harness-index/issues/2025).
- Observation date: 2026-10-25.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

`ChatAgent.llm_response` converts current messages into an LLM request, obtains a response, updates history and supports generated structured tool calls. Base `Agent.agent_response` calls first-party tool dispatch and returns tool results. `Task.run` and `Task.run_async` repeatedly call `step`, which searches among LLM, Agent, User and registered nested-task responders, validates a selected response, routes directed messages, and finishes or stops on terminal conditions. The LLM can choose tool use and directed subtask communication; `Task` controls responder validity, routing, stalls, budgets, and a shipped repeated-message cycle guard. [model and history](https://github.com/langroid/langroid/blob/1e0f5ab7d9d589d79928c39ed147ca8a2bd6a590/langroid/agent/chat_agent.py#L1626-L1748), [tool response](https://github.com/langroid/langroid/blob/1e0f5ab7d9d589d79928c39ed147ca8a2bd6a590/langroid/agent/base.py#L749-L775), [Task run](https://github.com/langroid/langroid/blob/1e0f5ab7d9d589d79928c39ed147ca8a2bd6a590/langroid/agent/task.py#L1017-L1124), [subtask selection](https://github.com/langroid/langroid/blob/1e0f5ab7d9d589d79928c39ed147ca8a2bd6a590/langroid/agent/task.py#L1246-L1342).

The specialized `LanceRAGTaskCreator.new()` is an actual shipped composition: a planner, retriever/answering agent and feedback critic. Its critic receives the original query, schema, proposed plan and reported answer; the planner may revise a current query plan after critic feedback. This is source-evidenced within-workflow QA and replanning, not complementary independent access to the underlying retrieved corpus or autonomous organization-wide resource policy. [packaged constructor](https://github.com/langroid/langroid/blob/1e0f5ab7d9d589d79928c39ed147ca8a2bd6a590/langroid/agent/special/lance_rag/lance_rag_task.py#L37-L84), [critic evidence surface](https://github.com/langroid/langroid/blob/1e0f5ab7d9d589d79928c39ed147ca8a2bd6a590/langroid/agent/special/lance_rag/critic_agent.py#L1-L30), [planner feedback](https://github.com/langroid/langroid/blob/1e0f5ab7d9d589d79928c39ed147ca8a2bd6a590/langroid/agent/special/lance_rag/query_planner_agent.py#L193-L258).

## Operational model

The operator supplies one or more task actors, provider settings, tools and goals. Within each work cell, the model chooses content, tools or recipients; the runtime executes tools and returns outputs for a next step. In a multi-actor `Task` the first-party round-robin and addressing implementation delivers responses. One narrow first-party coordination guard recognizes **actual repeated response oscillation** and aborts further futile responder turns; it is not a general shared-resource lock or autonomous dispute mediator. Task budgets, examples of manager prompts and a first-party plan/critic subworkflow do not establish broad whole-current S3 or strategic S4/S5 control.

## S1 — Operations

- State: A
- Function: Produce answers and actions for tasks through a model-backed actor that interprets successive messages and decides among offered tools and responses.
- Disturbance / variety regulated: User questions, model-generated calls, imperfect structured arguments, tool-return data, retrieval results and failures require task-specific decisions.
- Decisive decision or feedback right: `ChatAgent`'s model chooses the next text/function/tool or directed agent message in context; tool results and peer responses subsequently inform its next model call.
- Decision owner: Configured model-backed `ChatAgent` work cell, operationally wired by first-party `Agent`/`Task`; developer chooses which tools and prompts are available.
- Supporting / enforcement mechanisms: `ToolMessage` parsing, tool dispatch, message history, `Task.step` responder routing, retry/recovery on malformed tool format, budgets and external model adapter.
- Closure path: Task message → `ChatAgent.llm_response` → generated content or structured tool request → `Agent.agent_response`/subtask response → returned observation and task pending-message update → subsequent LLM choice or terminal result.
- Boundary reachability: `ChatAgent`, `Agent` and `Task` are first-party installable framework APIs; their production methods implement the model/action/result cycle. No `examples/` code or hidden external agent runtime is needed beyond the deliberately integrated model provider.
- Why this is / is not agent-owned: Without LLM decision-making, the deterministic responder selection and tool dispatcher cannot choose a semantic action or new response to changing tool results.
- Evidence: [ChatAgent model call/history](https://github.com/langroid/langroid/blob/1e0f5ab7d9d589d79928c39ed147ca8a2bd6a590/langroid/agent/chat_agent.py#L1626-L1748); [base tool handling](https://github.com/langroid/langroid/blob/1e0f5ab7d9d589d79928c39ed147ca8a2bd6a590/langroid/agent/base.py#L749-L770); [Task responder and return](https://github.com/langroid/langroid/blob/1e0f5ab7d9d589d79928c39ed147ca8a2bd6a590/langroid/agent/task.py#L1246-L1342).
- Basis: Structural first-party runtime and standard documented API.
- Confidence: High for implemented loop, not for unrun model effectiveness.
- Caveats: `ChatAgent` without a configured model is not itself autonomous. Task nesting or provider support does not create additional VSM functions by naming convention.

## S2 — Coordination

- State: C
- Function: Detect and suppress a narrow recurring oscillation in an active multi-actor task by ending the repeating response cycle before it can continue indefinitely.
- Disturbance / variety regulated: A model-backed S1 agent repeatedly asks or proposes successive content while a distinct subtask agent repeatedly returns `NO_ANSWER`; this forms a persistent cross-actor non-progress alternation.
- Distinct S1 units: A parent `Task`'s `ChatAgent` and its separately registered `ChatAgent` subtask. The source test sets up concrete `Alice` and `Bob` task actors; they have independent model-backed responder interfaces, unlike LLM/USER/AGENT internal responders of one actor.
- Inter-S1 disturbance: Alternating parent requests and `NO_ANSWER` from the child create repeated cross-agent fruitless turns; a bundled mocked two-agent test explicitly demonstrates the pattern.
- Attenuating coordination relation: In a supported nested-task run, `Task.run` records message frequencies and `NO_ANSWER` alternation counts, calls `_maybe_infinite_loop`, and raises `InfiniteLoopException` after a bounded threshold; this terminates the otherwise repeated task responder cycle.
- Feedback into subsequent S1 behaviour: On detection, `Task.run` exits via the exception rather than invoking further `step()` calls; further `Alice`→`Bob` delegated requests and responses cease in this run. The exception reaches the caller for an optional external recovery policy; Langroid does **not** negotiate a revised plan with either agent.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: Plain `Task` routing/subtask ordering would be insufficient. The credited witness is **a specific inter-S1 oscillation** in a shipped supported mode, its detection, and a hard stop that prevents further interfering exchanges, corroborated by first-party two-agent test. It is explicitly not evidence that round-robin routing alone performs S2.
- Decisive decision or feedback right: The threshold-based stop of repeating messages, controlled by TaskConfig's cycle/alternation parameters and deterministic source code; no model selects a dispute settlement policy.
- Decision owner: First-party **S2 constructor** (`C`) with deterministic detection and stop. The embedding operator can set thresholds; participating S1 models own their own messages but not the S2 intervention.
- Supporting / enforcement mechanisms: `message_counter`, bounded history, `inf_loop_cycle_len`, `inf_loop_wait_factor`, `n_no_answer_alternations`, `InfiniteLoopException`.
- Closure path: Child `NO_ANSWER`/parent new request repetition → Task alternation/history counters → threshold detection in `run` → exception → current task stops calling its responder S1 units.
- Boundary reachability: `Task.run` and `Task.add_sub_task` are publicly documented, installed framework methods; loop detection defaults on and applies to nested subtask messages. The concrete two-agent reproduction is a deterministic test of that same shipped execution path, not an external LLM agent run credited as ownership.
- Why this is / is not agent-owned: If the LLM choices were replaced with any response source emitting the same repetitive sequence, the deterministic guard would make the same stop decision. Hence S2 construction `C`, not agent-owned `A`.
- Evidence: [TaskConfig loop thresholds](https://github.com/langroid/langroid/blob/1e0f5ab7d9d589d79928c39ed147ca8a2bd6a590/langroid/agent/task.py#L112-L168); [runtime detection and stop](https://github.com/langroid/langroid/blob/1e0f5ab7d9d589d79928c39ed147ca8a2bd6a590/langroid/agent/task.py#L1096-L1122); [detector implementation](https://github.com/langroid/langroid/blob/1e0f5ab7d9d589d79928c39ed147ca8a2bd6a590/langroid/agent/task.py#L1958-L2036); [two-agent Alice/Bob test](https://github.com/langroid/langroid/blob/1e0f5ab7d9d589d79928c39ed147ca8a2bd6a590/tests/main/test_task_inf_loop.py#L118-L154).
- Basis: Structural first-party loop guard plus deterministic two-agent test source.
- Confidence: Medium for narrow S2 construction; high for actual halting code path. No evidence of reduced conflict beyond stopping the cycle.
- Caveats: **Only** bounded identical-message or `NO_ANSWER` oscillation is covered, including when it involves multiple S1 units. The same guard also stops single-agent/user loops, which alone would not count as S2. The framework does not autonomously reconcile the disagreement, arbitrate shared file edits or learn a new coordination policy. Raising an exception stops the task but does not itself send a corrective new instruction to the agents.

## S3 — Inside-and-now control

- State: —
- Function: No first-party whole-current organizational manager that appraises the active S1 population and revises shared commitments, resource allocations or priorities is evidenced.
- Disturbance / variety regulated: Multiple task actors could waste capacity or misalign outputs, but default `Task` decides only response eligibility/order and fixed task termination; it does not autonomously govern a portfolio.
- Decisive decision or feedback right: An embedding developer decides what nested tasks exist, goals and resource budgets. Optional LanceRAG planner revises the content of *one query plan* as ordinary production QA; it does not assign shared resources/commitments across independent ongoing work units.
- Decision owner: Developer for application architecture and budgets; subtask/QueryPlan LLM owns work-level planning, not whole-current managerial authority.
- Supporting / enforcement mechanisms: `Task.add_sub_task`, responder order, `Task.run` limits, token/cost caps, stall/loop stop, `QueryPlanFeedbackTool`, task status/logs and message lineage.
- Closure path: Delegated response returns to parent; query planner can retry an output using a critic's note; timeout stops a task. No separately established metasystem whole-current view and intervention over S1 commitments returns to ongoing operations.
- Why this is / is not agent-owned: A planner LLM revises its own next work request, but delegation/content repair within the same user question is not autonomous S3 management of shared active agent operations. Runtime budget gates enforce caller-specified limits.
- Evidence: [subtask API](https://github.com/langroid/langroid/blob/1e0f5ab7d9d589d79928c39ed147ca8a2bd6a590/langroid/agent/task.py#L573-L603); [Task run/limits](https://github.com/langroid/langroid/blob/1e0f5ab7d9d589d79928c39ed147ca8a2bd6a590/langroid/agent/task.py#L1071-L1124); [special query-plan feedback](https://github.com/langroid/langroid/blob/1e0f5ab7d9d589d79928c39ed147ca8a2bd6a590/langroid/agent/special/lance_rag/query_planner_agent.py#L193-L258).
- Basis: Bounded negative after inspecting generic and first-party specialized supported modes.
- Confidence: Medium.
- Caveats: A user-written larger Langroid team could implement S3 and receive a different assessment at its own boundary; this framework source does not instantiate that manager.

### Absence scope

- Surfaces inspected: Core `Task.run`/`step`, nested responder registration, `ChatAgent`, task budget/cost/turn logic, packaged LanceRAG planner/critic/RAG and docs.
- Plausible first-party paths checked: Model-directed recipient selection, parent-subtask reply chaining, stalled/loop halting, generic task status, Lance query-plan retries and developer-configured task hierarchy.
- Why no material first-party path remains: These are one task's operation/QA, multi-agent anti-oscillation construction, or fixed runtime enforcement. None carries a first-party whole-system current appraisal into owned resource, commitment or priority intervention across the operational population.

## S3* — Complementary audit

- State: —
- Function: No sufficiently independent complementary audit channel for agent production claims and returned corrective whole-current control is established in the installed framework modes.
- Disturbance / variety regulated: Tool-produced and retrieved answers can misstate actual document content or correctness; ordinary critique may check the shape and plausibility of one planned answer.
- Decisive decision or feedback right: The optional first-party `QueryPlanCritic` evaluates the *reported* plan and answer using the same supplied schema, not independent original corpus access or sampled raw retrieval evidence, and returns routine iteration feedback to its producing planner.
- Decision owner: Model-backed critic owns a production QA opinion; no separate independent operational auditor with distinct access and return to S3 is wired.
- Supporting / enforcement mechanisms: Critic prompts, `QueryPlanFeedbackTool`, `QueryPlanAnswerTool`, task logs/lineage and structured output validation.
- Closure path: Query-plan/answer sent to critic → feedback → planner retries or accepts. This corrects ongoing task output, but lacks complementary access to operational reality and independent S3 reporting challenge.
- Why this is / is not agent-owned: The critic's LLM may exercise discretion about quality, yet a distinct second prompt alone does not create independent audit ownership or a metasystem audit circuit.
- Evidence: [critic's specified inputs and output](https://github.com/langroid/langroid/blob/1e0f5ab7d9d589d79928c39ed147ca8a2bd6a590/langroid/agent/special/lance_rag/critic_agent.py#L1-L34); [critic tool handler](https://github.com/langroid/langroid/blob/1e0f5ab7d9d589d79928c39ed147ca8a2bd6a590/langroid/agent/special/lance_rag/critic_agent.py#L158-L190); [consumer of routine feedback](https://github.com/langroid/langroid/blob/1e0f5ab7d9d589d79928c39ed147ca8a2bd6a590/langroid/agent/special/lance_rag/query_planner_agent.py#L193-L239).
- Basis: Bounded negative after checking plausible first-party specialized critic.
- Confidence: Medium-high for known critic evidence boundary.
- Caveats: A consumer could build a separately independent document-ground-truth verifier on top of Langroid; examples or an unconnected evaluation script do not supply that mode to this framework.

### Absence scope

- Surfaces inspected: Agent and Task reporting/history, specialized RAG creator, critic system prompt, tool return, query plan feedback, structured-output validation and tests.
- Plausible first-party paths checked: Specialized critic, source citations, message lineage, tool result logging, validation of model-generated JSON and application-supplied external checker.
- Why no material first-party path remains: Routine critic sees planner-produced plan/answer and schema but does not independently inspect source documents or operational ground truth; logs/tool validation and external user implementation do not establish a shipped independent audit-to-current-control path.

## S4 — Outside-and-then intelligence

- State: —
- Function: No deployed first-party loop senses the external *future* environment, develops adaptation options and returns a selected capability change to current operation.
- Disturbance / variety regulated: Model/provider shifts, new document schemas and emerging tool requirements can affect future operation, but Langroid exposes reusable interfaces rather than prospectively governing its own evolution.
- Decisive decision or feedback right: Operators/developers change provider settings, agents, retrieval tools and prompts; model-based query planning addresses the *current* question.
- Decision owner: External operator or application developer; no built-in autonomous S4 owner/parent-return path.
- Supporting / enforcement mechanisms: Configurable LLM backends, tool registration, RAG/vector providers, retry on invalid calls and current-goal query reformulation.
- Closure path: A developer can install a new tool or model and rerun tasks; the framework does not itself select that change on the basis of future-environment appraisal and return it into ongoing capacity.
- Why this is / is not agent-owned: Current-task retrieval and retries are S1 variety handling; future developer configuration is not a shipped S4 strategic cycle.
- Evidence: [README provider/tool composition](https://github.com/langroid/langroid/blob/1e0f5ab7d9d589d79928c39ed147ca8a2bd6a590/README.md#L468-L508); [ChatAgent malformed-tool recovery](https://github.com/langroid/langroid/blob/1e0f5ab7d9d589d79928c39ed147ca8a2bd6a590/langroid/agent/chat_agent.py#L1626-L1680); [current query feedback](https://github.com/langroid/langroid/blob/1e0f5ab7d9d589d79928c39ed147ca8a2bd6a590/langroid/agent/special/lance_rag/query_planner_agent.py#L193-L239).
- Basis: Bounded negative on standard installed modes.
- Confidence: Medium-high.
- Caveats: Retrieval of external data for the current answer is not automatically a prospective S4 function.

### Absence scope

- Surfaces inspected: Core model/tool runtime, configurable providers, retrieval agents, Lance planner/critic loop, task callbacks and supported documentation.
- Plausible first-party paths checked: Dynamic tool registration, querying external documents, provider replacement, reformulating one query, developer-maintained example patterns and error recovery.
- Why no material first-party path remains: Each is present-task production, library extension or operator configuration, with no explicit external-prospective sensing/option/adoption chain affecting ongoing capability.

## S5 — Policy and identity

- State: —
- Function: No runtime constitutional or ultimate identity-policy determination with legitimate binding decision return is established for the assembled framework execution.
- Disturbance / variety regulated: Tool risks, undesired content and task termination are handled by prompts, allowlists and the operator; they are routine permission/workflow matters rather than an identity-level conflict.
- Decisive decision or feedback right: Developer/user defines system instructions and allowed tools, can choose interactive human response/exit; there is no identity-policy issue routed to an ultimate authority and returned as a changed binding organizational rule.
- Decision owner: Application owner/user for initial configuration and ad hoc operation; no first-party S5 authority in the runtime.
- Supporting / enforcement mechanisms: Prompt instructions, tool-message validation, human-responder option, task halt/quit, budgets, config and runtime guards.
- Closure path: Prompt/tool configuration constrains requests; user may respond to a task and quit; neither is a legitimate identity-governance escalation and return circuit.
- Why this is / is not agent-owned: The model interprets instructions inside one task but is not empowered to settle the overall system's identity or competing ultimate policy. A human-interactive task alone is not parent S5(P).
- Evidence: [Task controller choice/interactive semantics](https://github.com/langroid/langroid/blob/1e0f5ab7d9d589d79928c39ed147ca8a2bd6a590/langroid/agent/task.py#L215-L316); [termination/quit logic](https://github.com/langroid/langroid/blob/1e0f5ab7d9d589d79928c39ed147ca8a2bd6a590/langroid/agent/task.py#L2039-L2140); [ChatAgent prompt/tool configuration](https://github.com/langroid/langroid/blob/1e0f5ab7d9d589d79928c39ed147ca8a2bd6a590/langroid/agent/chat_agent.py).
- Basis: Bounded negative on first-party framework authority.
- Confidence: Medium-high.
- Caveats: A hosting organization's separate human governance is outside the Langroid SDK's installed first-party boundary.

### Absence scope

- Surfaces inspected: Task interactive/human controller options, termination signals, system prompts, `ChatAgent` configuration, available tool controls, contributor/release separation and operator workflows.
- Plausible first-party paths checked: User participation, role system messages, DONE/quit signals, tool enforcement, configurable model provider, custom application policy hooks.
- Why no material first-party path remains: These determine task operations or sit outside the installed system; none supplies ultimate-policy legitimacy, escalation to that authority and returned identity-level decision.

## Distributed OSS parent arrangement

Langroid contributors, optional provider maintainers and consumer-developer teams are distinct from a given installed Langroid task. Code review and release governance of the public repository do not make a running multi-agent application parent-governed for S3/S4/S5. The installed framework's human responder is an operational participant rather than inherently a corporate S5 authority.

## Self-hosted and non-human modes

Langroid supports local/remote provider backends and noninteractive task execution. A fully configured non-human `ChatAgent` can autonomously act with tools; a multi-agent task can halt pathological alternation without human mediation. Human response is optional outside explicitly addressed interaction. Neither self-hosting nor lack of a human automatically establishes autonomous metasystem control.

## Recursion

`Task` delegates to nested tasks and can expose those as responders, but the package does not automatically instantiate complete independent metasystems per child. The narrow multi-agent guard operates at the parent task loop; no wider cross-task organization is presumed.

## Variety and escalation

Task/responders handle local model/tool variety. An exact-cycle or `NO_ANSWER` alternation raises an exception and stops the current task loop; stalled/budget limits also terminate task execution. This is a bounded S2 anti-oscillation circuit only when distinct S1 agents are involved; none of these error/status channels is automatically an independent algedonic escalation into S3–S5 authority.

## Evidence gaps

- Reviewed the pinned first-party core Task/Agent/ChatAgent and optional packaged RAG feedback path. Did not run any live provider, agent or benchmark; static tests cited for S2 are read as code evidence, not executed LLM evaluation.
- S2's actual closed effect is termination of a repeating inter-agent exchange, not negotiated reconciliation. A reviewer should not generalize this narrow `C` witness to locks, arbitration, or all multi-agent modes.
- Consumer-written orchestration could add S3–S5, but no such externally composed organization is credited. The negative states are bounded to the inspected installed first-party distribution, not claims about every Langroid application.

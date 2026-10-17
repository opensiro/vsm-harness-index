---
harness_id: botsharp
project_name: BotSharp
repository: https://github.com/SciSharp/BotSharp
review_ref: dbc3103afc5cc6e03892ab9da066b9955f45c1aa
reviewed_at: 2026-10-17
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

# BotSharp

## Review boundary

- System in focus: One installable first-party BotSharp .NET conversation/agent runtime with its configured routing agent, specialist agents, state and tool/plugin callbacks, processing one or more operator/user conversations. The reviewed recursion is the running agent application, not the developer organization or external AI model vendor.
- Purpose and identity: Respond to user/business requests through configured conversational agents and tools, route work to specialists, preserve per-conversation state and expose integration APIs for application developers.
- Relevant environment: Incoming application/user messages, external LLM inference services, configured third-party tools and plugins, conversation persistence, errors and application administrator configuration.
- Standard-distribution boundary: Shipped BotSharp.Core routing/conversation/agent services and first-party runtime plugins as actually installed in a self-hosted .NET application. Optional first-party Planner and Agent Testing plugin paths are examined but only credited for the function they really close; external LLM providers, app-specific integrations and administrators are not silently imported as autonomous internal owners.
- Credited operating / distribution surfaces: [ConversationService.SendMessage.cs](https://github.com/SciSharp/BotSharp/blob/dbc3103afc5cc6e03892ab9da066b9955f45c1aa/src/Infrastructure/BotSharp.Core/Conversations/Services/ConversationService.SendMessage.cs#L10), [RoutingService.InstructLoop.cs](https://github.com/SciSharp/BotSharp/blob/dbc3103afc5cc6e03892ab9da066b9955f45c1aa/src/Infrastructure/BotSharp.Core/Routing/RoutingService.InstructLoop.cs#L10), [RoutingService.InvokeAgent.cs](https://github.com/SciSharp/BotSharp/blob/dbc3103afc5cc6e03892ab9da066b9955f45c1aa/src/Infrastructure/BotSharp.Core/Routing/RoutingService.InvokeAgent.cs#L9), [InstructExecutor.cs](https://github.com/SciSharp/BotSharp/blob/dbc3103afc5cc6e03892ab9da066b9955f45c1aa/src/Infrastructure/BotSharp.Core/Routing/Reasoning/InstructExecutor.cs#L18), [RouteToAgentFn.cs](https://github.com/SciSharp/BotSharp/blob/dbc3103afc5cc6e03892ab9da066b9955f45c1aa/src/Infrastructure/BotSharp.Core/Routing/Functions/RouteToAgentFn.cs#L27), [RoutingContext.cs](https://github.com/SciSharp/BotSharp/blob/dbc3103afc5cc6e03892ab9da066b9955f45c1aa/src/Infrastructure/BotSharp.Core/Routing/RoutingContext.cs#L85) and [SequentialPlanner.cs](https://github.com/SciSharp/BotSharp/blob/dbc3103afc5cc6e03892ab9da066b9955f45c1aa/src/Plugins/BotSharp.Plugin.Planner/Sequential/SequentialPlanner.cs#L27) for the installed optional task-planning mode; first-party tool plugins can supply concrete tool effects.
- Adjacent first-party surfaces excluded from ownership: [AgentTestingPlugin.cs](https://github.com/SciSharp/BotSharp/blob/dbc3103afc5cc6e03892ab9da066b9955f45c1aa/src/Plugins/BotSharp.Plugin.AgentTesting/AgentTestingPlugin.cs#L10), [AgentTestController.cs](https://github.com/SciSharp/BotSharp/blob/dbc3103afc5cc6e03892ab9da066b9955f45c1aa/src/Plugins/BotSharp.Plugin.AgentTesting/Controllers/AgentTestController.cs#L560), [AgentTestRunExecutor.cs](https://github.com/SciSharp/BotSharp/blob/dbc3103afc5cc6e03892ab9da066b9955f45c1aa/src/Plugins/BotSharp.Plugin.AgentTesting/Services/AgentTestRunExecutor.cs#L53), [LlmAgentTestJudge.cs](https://github.com/SciSharp/BotSharp/blob/dbc3103afc5cc6e03892ab9da066b9955f45c1aa/src/Plugins/BotSharp.Plugin.AgentTesting/Services/LlmAgentTestJudge.cs#L38) and [EvaluationConversationHook.cs](https://github.com/SciSharp/BotSharp/blob/dbc3103afc5cc6e03892ab9da066b9955f45c1aa/src/Infrastructure/BotSharp.Core/Evaluations/EvaluationConversationHook.cs#L19) are examined as development/regression evaluation, test-run recording and routine conversation logging rather than as a proven live metasystem audit or adaptation controller; repository tests, samples and project maintainer CI are not product governance.
- First-party operating / deployment modes considered: Direct agent conversation; routing-agent eager and lazy dispatch; model-selected function/tool callbacks; optional sequential planning; self-hosted admin configuration; separate explicitly triggered agent testing/model sweep.
- Recursion level: Installed BotSharp agent application across its configured conversation(s), with routed specialist roles as subordinate S1 operating participants. A nested agent dispatch or recursion-depth counter is not in itself another fully governed VSM organization.
- Reviewed revision: `dbc3103afc5cc6e03892ab9da066b9955f45c1aa` (the immutable row-2 ref in Index candidate intake #202 / assessment batch #1669, not current BotSharp master).
- Observation date: 2026-10-17.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

`ConversationService.SendMessage` loads the selected agent and conversation dialogs, applies configured inbound hooks, then selects either direct `InstructDirect` or a routing-agent `InstructLoop` (including eager/lazy routing). The router gets model-generated next instructions, invokes selected specialist agents and/or tool functions, saves function outputs in conversation dialogs and sends those observations back to a configured model for the next action. `RoutingContext` carries a per-conversation agent stack and recursion limit. The planner plugin adds task-local instruction decomposition, not whole-organization current control. [ConversationService.SendMessage.cs](https://github.com/SciSharp/BotSharp/blob/dbc3103afc5cc6e03892ab9da066b9955f45c1aa/src/Infrastructure/BotSharp.Core/Conversations/Services/ConversationService.SendMessage.cs#L75); [RoutingService.InstructLoop.cs](https://github.com/SciSharp/BotSharp/blob/dbc3103afc5cc6e03892ab9da066b9955f45c1aa/src/Infrastructure/BotSharp.Core/Routing/RoutingService.InstructLoop.cs#L24); [RoutingService.InvokeAgent.cs](https://github.com/SciSharp/BotSharp/blob/dbc3103afc5cc6e03892ab9da066b9955f45c1aa/src/Infrastructure/BotSharp.Core/Routing/RoutingService.InvokeAgent.cs#L35); [RoutingContext.cs](https://github.com/SciSharp/BotSharp/blob/dbc3103afc5cc6e03892ab9da066b9955f45c1aa/src/Infrastructure/BotSharp.Core/Routing/RoutingContext.cs#L85); [SequentialPlanner.cs](https://github.com/SciSharp/BotSharp/blob/dbc3103afc5cc6e03892ab9da066b9955f45c1aa/src/Plugins/BotSharp.Plugin.Planner/Sequential/SequentialPlanner.cs#L42).

First-party storage, hooks, role and agent services permit conversation history, per-conversation state, human intervention notifications, agent configuration, optional extension plugins and persisted task records. These are support/enforcement. Tool and LLM implementations may depend on provider services or adopter-installed components; first-party runtime owns dispatch/feedback, not the opaque internals of a vendor model. [RouteToAgentFn.cs](https://github.com/SciSharp/BotSharp/blob/dbc3103afc5cc6e03892ab9da066b9955f45c1aa/src/Infrastructure/BotSharp.Core/Routing/Functions/RouteToAgentFn.cs#L29); [HumanInterventionNeededFn.cs](https://github.com/SciSharp/BotSharp/blob/dbc3103afc5cc6e03892ab9da066b9955f45c1aa/src/Infrastructure/BotSharp.Core/Routing/Functions/HumanInterventionNeededFn.cs#L17); [AgentService.UpdateAgent.cs](https://github.com/SciSharp/BotSharp/blob/dbc3103afc5cc6e03892ab9da066b9955f45c1aa/src/Infrastructure/BotSharp.Core/Agents/Services/AgentService.UpdateAgent.cs#L9); [AgentTaskService.cs](https://github.com/SciSharp/BotSharp/blob/dbc3103afc5cc6e03892ab9da066b9955f45c1aa/src/Infrastructure/BotSharp.Core/Tasks/Services/AgentTaskService.cs#L19).

Agent Testing is substantive but separate: a privileged HTTP trigger creates a test run, pushes it onto a background queue, evaluates scripted cases across caller-selected models and persists result rows. Its LLM judge requires an explicitly configured scoring model and rejects unscorable results. This is actual first-party test functionality; the reviewed source does not wire those findings to corrective decisions in live conversation routing nor to automatically selected future agent configurations. [AgentTestController.cs](https://github.com/SciSharp/BotSharp/blob/dbc3103afc5cc6e03892ab9da066b9955f45c1aa/src/Plugins/BotSharp.Plugin.AgentTesting/Controllers/AgentTestController.cs#L560); [AgentTestRunExecutor.cs](https://github.com/SciSharp/BotSharp/blob/dbc3103afc5cc6e03892ab9da066b9955f45c1aa/src/Plugins/BotSharp.Plugin.AgentTesting/Services/AgentTestRunExecutor.cs#L137); [LlmAgentTestJudge.cs](https://github.com/SciSharp/BotSharp/blob/dbc3103afc5cc6e03892ab9da066b9955f45c1aa/src/Plugins/BotSharp.Plugin.AgentTesting/Services/LlmAgentTestJudge.cs#L38).

## Operational model

Each configured task agent produces conversation responses and permitted tool/plugin effects through a model-selected call/observation loop. A routing-agent model may choose which specialist to run. It does not thereby become an S2 arbiter between independently operating teams or an S3 owner of the whole installed application. A human administrator can alter agents/settings and separately trigger tests, but evidence of administrative access alone does not close parent-owned S3/S4/S5 at the declared recursion.

## S1 — Operations

- State: A
- Function: Execute user requests through model-directed specialist/conversation agents choosing task responses and tools.
- Disturbance / variety regulated: Unstructured and changing user requests, provider replies, errors, required fields, tool outputs and conversation context.
- Decisive decision or feedback right: The configured router/task-agent model selects subsequent specialist, function call and task response conditioned on current dialog and returned function results.
- Decision owner: Configured model-backed agent operating through the first-party BotSharp routing and conversation loop; model inference is a dependency, not an external vendor organization credited with the harness's structure.
- Supporting / enforcement mechanisms: Conversation storage, hook emitter, routed-agent stack, LLM provider adapter, function executor, per-agent recursion limit, optional Planner and manual intervention callback.
- Closure path: User message → `SendMessage` → `InstructLoop` or direct `InvokeAgent` → LLM-selected instruction/function → first-party execute/route → appended tool/dialog observation → recursive next `InvokeAgent` or answer persisted back into conversation.
- Boundary reachability: `SendMessage` calls active routing/direct service; `InstructExecutor` dispatches model-selected task agent, and `InvokeFunction` returns tool result to another model turn. This is a shipped active runtime path, not sample/test-only code.
- Why this is / is not agent-owned: Model selection changes task decisions based on inputs/results; deterministic dispatch/persistence and provider adapters do not make the decisions by themselves.
- Evidence: [ConversationService.SendMessage.cs](https://github.com/SciSharp/BotSharp/blob/dbc3103afc5cc6e03892ab9da066b9955f45c1aa/src/Infrastructure/BotSharp.Core/Conversations/Services/ConversationService.SendMessage.cs#L75); [RoutingService.InstructLoop.cs](https://github.com/SciSharp/BotSharp/blob/dbc3103afc5cc6e03892ab9da066b9955f45c1aa/src/Infrastructure/BotSharp.Core/Routing/RoutingService.InstructLoop.cs#L30); [InstructExecutor.cs](https://github.com/SciSharp/BotSharp/blob/dbc3103afc5cc6e03892ab9da066b9955f45c1aa/src/Infrastructure/BotSharp.Core/Routing/Reasoning/InstructExecutor.cs#L23); [RoutingService.InvokeAgent.cs](https://github.com/SciSharp/BotSharp/blob/dbc3103afc5cc6e03892ab9da066b9955f45c1aa/src/Infrastructure/BotSharp.Core/Routing/RoutingService.InvokeAgent.cs#L51); [RoutingService.InvokeAgent.cs](https://github.com/SciSharp/BotSharp/blob/dbc3103afc5cc6e03892ab9da066b9955f45c1aa/src/Infrastructure/BotSharp.Core/Routing/RoutingService.InvokeAgent.cs#L104); [RouteToAgentFn.cs](https://github.com/SciSharp/BotSharp/blob/dbc3103afc5cc6e03892ab9da066b9955f45c1aa/src/Infrastructure/BotSharp.Core/Routing/Functions/RouteToAgentFn.cs#L52).
- Basis: Explicit first-party runtime source and feedback closure.
- Confidence: High for code reachability; no production provider calls executed in this review.
- Caveats: External model service and installed tool plugins required for actual effects; no benchmark performance, provider-internal VSM or cross-conversation metasystem outcome claimed.

## S2 — Coordination

- State: —
- Function: No first-party, function-specific attenuation of a concrete conflict or oscillation between distinct independently operating S1 units is established at this boundary.
- Disturbance / variety regulated: Potential specialist contention or incompatible agent actions; the examined routing stack mostly sequences one task's dispatch and maintains shared dialog context.
- Decisive decision or feedback right: Router selection, missing-field redirection and agent queue mutations select the next task worker, not a conflict-sensitive mutual-adjustment response among distinct S1 units.
- Decision owner: Model-guided task router plus deterministic per-conversation routing stack; no separate evidenced S2-specific deciding owner.
- Supporting / enforcement mechanisms: `RoutingContext.Push/Pop`, `route_to_agent`, routing planner and conversation state/history.
- Closure path: The selected agent receives current task context and returns a result; the missing S2 closure is detection of a specific inter-unit disturbance followed by an attenuating response that changes both units' subsequent operations.
- Why this is / is not agent-owned: The model owns task routing but not a demonstrated inter-S1 stabilizing choice; multiple specialist agents and stack position do not establish S2.
- Evidence: [RoutingContext.cs](https://github.com/SciSharp/BotSharp/blob/dbc3103afc5cc6e03892ab9da066b9955f45c1aa/src/Infrastructure/BotSharp.Core/Routing/RoutingContext.cs#L85); [RouteToAgentFn.cs](https://github.com/SciSharp/BotSharp/blob/dbc3103afc5cc6e03892ab9da066b9955f45c1aa/src/Infrastructure/BotSharp.Core/Routing/Functions/RouteToAgentFn.cs#L52); [NaiveReasoner.cs](https://github.com/SciSharp/BotSharp/blob/dbc3103afc5cc6e03892ab9da066b9955f45c1aa/src/Infrastructure/BotSharp.Core/Routing/Reasoning/NaiveReasoner.cs#L76); [InstructExecutor.cs](https://github.com/SciSharp/BotSharp/blob/dbc3103afc5cc6e03892ab9da066b9955f45c1aa/src/Infrastructure/BotSharp.Core/Routing/Reasoning/InstructExecutor.cs#L68).
- Basis: Explicit routing implementation, bounded negative adjudication against S2-specific prerequisites.
- Confidence: Medium-high within the assessed first-party runtime; optional adopter-authored coordination plugins not credited.
- Caveats: This is not a proof that an application built on BotSharp cannot add S2.

### Absence scope

- Surfaces inspected: Conversation entry, routing-stack service, route function, NaiveReasoner, Planner and executor code in the pinned core/optional first-party runtime.
- Plausible first-party paths checked: Agent stack push/pop, missing-required-field rerouting, invalid-target fallback, per-turn planner sequencing and state persistence.
- Why no material first-party path remains: Those paths change which agent handles the current request or preserve conversation integrity; they do not detect/attenuate a specified disturbance between distinct S1 units with mutual feedback. No material built-in S2 operating mode was established.

## S3 — Inside-and-now control

- State: —
- Function: No closed, application-wide current-control function with a shared view and decision authority over resources, commitments, priorities or interventions across ongoing S1 work is established.
- Disturbance / variety regulated: Possible competing conversation workloads and resource contention; these are not shown governed by a whole-application runtime controller.
- Decisive decision or feedback right: Per-conversation router chooses a specialist and the planner chooses steps for one request; fixed depth caps and stop flags constrain execution, not system-wide commitments.
- Decision owner: Task-model agent and deterministic routing/enforcement; no separate first-party S3 owner or legitimate parent-return loop demonstrated.
- Supporting / enforcement mechanisms: Per-conversation `RoutingContext`, recursion bounds, agent/task CRUD services, hook stop flags and administrator configuration.
- Closure path: Task-local plan/handoff/result return exists; no whole-current application view → cross-workload resource/priority judgment → enforced and returned S1 control path exists in examined shipped mode.
- Why this is / is not agent-owned: A model-selectable next agent is operational dispatch; static constraints do not confer metasystem current-control authority.
- Evidence: [RoutingService.InstructLoop.cs](https://github.com/SciSharp/BotSharp/blob/dbc3103afc5cc6e03892ab9da066b9955f45c1aa/src/Infrastructure/BotSharp.Core/Routing/RoutingService.InstructLoop.cs#L30); [RoutingService.InvokeAgent.cs](https://github.com/SciSharp/BotSharp/blob/dbc3103afc5cc6e03892ab9da066b9955f45c1aa/src/Infrastructure/BotSharp.Core/Routing/RoutingService.InvokeAgent.cs#L18); [SequentialPlanner.cs](https://github.com/SciSharp/BotSharp/blob/dbc3103afc5cc6e03892ab9da066b9955f45c1aa/src/Plugins/BotSharp.Plugin.Planner/Sequential/SequentialPlanner.cs#L42); [AgentTaskService.cs](https://github.com/SciSharp/BotSharp/blob/dbc3103afc5cc6e03892ab9da066b9955f45c1aa/src/Infrastructure/BotSharp.Core/Tasks/Services/AgentTaskService.cs#L19); [ConversationService.SendMessage.cs](https://github.com/SciSharp/BotSharp/blob/dbc3103afc5cc6e03892ab9da066b9955f45c1aa/src/Infrastructure/BotSharp.Core/Conversations/Services/ConversationService.SendMessage.cs#L75).
- Basis: Explicit source partition between conversation routing and application-wide control.
- Confidence: Medium-high for defined packaged modes.
- Caveats: App adopter may implement external portfolio scheduling or operator current control; generic ability to host that is not a positive S3 witness.

### Absence scope

- Surfaces inspected: Core conversation/routing services, task record CRUD, optional Planner, recursion enforcement, configuration and human intervention callback.
- Plausible first-party paths checked: Routing stack, step planner, agent task listing, maximum recursion and administrator-selected agent settings.
- Why no material first-party path remains: All reviewed decisions are scoped to an incoming conversation/request or static configured agent; no complete shared-current-operations view plus resource/commitment decision/feedback owner is shipped and closed.

## S3* — Complementary audit

- State: —
- Function: An independent complementary operating-claim challenge returned into current control is not established, despite a shipped independent testing/judging facility.
- Disturbance / variety regulated: Unreliable outputs and test regressions; standalone evaluation detects some errors but does not thereby constitute the live metasystem's complementary audit channel.
- Decisive decision or feedback right: Agent Testing judge scores configured test cases, while privileged caller triggers a separate test run. Neither is shown owning a decision to challenge a live ordinary S1/S3 report and return an operational correction.
- Decision owner: Separate chosen test judge model (where configured) and external test operator, not an evidenced installed S3* control actor.
- Supporting / enforcement mechanisms: Agent Testing test-case runner, result repository/queue, optional LLM scorer, basic conversation logging.
- Closure path: Privileged API test trigger → model/case execution → stored test scores/errors; missing link is independently surfaced finding → accountable current-control corrective decision → changed live S1 regulation.
- Why this is / is not agent-owned: The judge may be model-owned, but a model grading tests is not sufficient for S3* without complementary operational reality access and corrective return.
- Evidence: [AgentTestingPlugin.cs](https://github.com/SciSharp/BotSharp/blob/dbc3103afc5cc6e03892ab9da066b9955f45c1aa/src/Plugins/BotSharp.Plugin.AgentTesting/AgentTestingPlugin.cs#L42); [AgentTestController.cs](https://github.com/SciSharp/BotSharp/blob/dbc3103afc5cc6e03892ab9da066b9955f45c1aa/src/Plugins/BotSharp.Plugin.AgentTesting/Controllers/AgentTestController.cs#L560); [AgentTestRunExecutor.cs](https://github.com/SciSharp/BotSharp/blob/dbc3103afc5cc6e03892ab9da066b9955f45c1aa/src/Plugins/BotSharp.Plugin.AgentTesting/Services/AgentTestRunExecutor.cs#L137); [LlmAgentTestJudge.cs](https://github.com/SciSharp/BotSharp/blob/dbc3103afc5cc6e03892ab9da066b9955f45c1aa/src/Plugins/BotSharp.Plugin.AgentTesting/Services/LlmAgentTestJudge.cs#L38); [EvaluationConversationHook.cs](https://github.com/SciSharp/BotSharp/blob/dbc3103afc5cc6e03892ab9da066b9955f45c1aa/src/Infrastructure/BotSharp.Core/Evaluations/EvaluationConversationHook.cs#L19).
- Basis: Explicit regression-test entry and output wiring; bounded separation of evaluator from operating control.
- Confidence: Medium; the optional test facility is real, but no internal S3* return demonstrated.
- Caveats: An external deployment could act on test findings. This review does not infer such a separately installed governance loop.

### Absence scope

- Surfaces inspected: Optional AgentTesting registration, privileged trigger/controller, run executor, judge, routine EvaluationConversationHook and conversation/routing control.
- Plausible first-party paths checked: LLM judging, test result persistence, model comparison, logging hooks and possible correction via operator agent updates.
- Why no material first-party path remains: The reviewed test lifecycle terminates in externally queryable test results; runtime routing has no evidenced first-party receipt/adjudication/return link to those independent findings. Routine logs and operator-triggered regression tests alone do not establish complementary S3*.

## S4 — Outside-and-then intelligence

- State: —
- Function: No first-party future/environment-oriented capability adaptation option selection with return into installed operating agents is established.
- Disturbance / variety regulated: Changing tasks, LLM model quality, business integrations and future model choices; testing can compare current providers but no shipped prospective adaptation controller was found.
- Decisive decision or feedback right: The Agent Testing API permits a caller-selected set of test models, and administrator services permit explicit agent updates. No integrated first-party actor is shown selecting future capability options based on external change and applying them into active agent capability.
- Decision owner: Operator/developer for test selection and configuration; runtime only records comparisons and applies separate API edits.
- Supporting / enforcement mechanisms: Test model sweeps, LLM rubric scores, test-case authoring, static agent profile persistence, per-request planner and memory services.
- Closure path: Configured suite → selected models evaluated → result rows stored; separately agent CRUD can update config. Missing is a witnessed external-prospective distinction → adaptation decision/option → feedback to current capability with accountable selection.
- Why this is / is not agent-owned: LLM test-case authoring and current-task planning are agentic tasks, not autonomous organizational adaptation; human admin setting a model is not automatically parent S4.
- Evidence: [AgentTestController.cs](https://github.com/SciSharp/BotSharp/blob/dbc3103afc5cc6e03892ab9da066b9955f45c1aa/src/Plugins/BotSharp.Plugin.AgentTesting/Controllers/AgentTestController.cs#L590); [AgentTestRunExecutor.cs](https://github.com/SciSharp/BotSharp/blob/dbc3103afc5cc6e03892ab9da066b9955f45c1aa/src/Plugins/BotSharp.Plugin.AgentTesting/Services/AgentTestRunExecutor.cs#L137); [LlmCaseAuthor.cs](https://github.com/SciSharp/BotSharp/blob/dbc3103afc5cc6e03892ab9da066b9955f45c1aa/src/Plugins/BotSharp.Plugin.AgentTesting/Services/LlmCaseAuthor.cs#L72); [AgentService.UpdateAgent.cs](https://github.com/SciSharp/BotSharp/blob/dbc3103afc5cc6e03892ab9da066b9955f45c1aa/src/Infrastructure/BotSharp.Core/Agents/Services/AgentService.UpdateAgent.cs#L9); [SequentialPlanner.cs](https://github.com/SciSharp/BotSharp/blob/dbc3103afc5cc6e03892ab9da066b9955f45c1aa/src/Plugins/BotSharp.Plugin.Planner/Sequential/SequentialPlanner.cs#L42).
- Basis: Source-grounded separation between model testing, manual configuration and live task execution.
- Confidence: Medium for bounded negative: no applied future-capability feedback in the inspected standard distribution.
- Caveats: An adopter can construct a separate model-selection feedback system; do not borrow such an unshown application from extensibility.

### Absence scope

- Surfaces inspected: Agent Testing selected-model comparisons, LLM case author, run outputs, core agent CRUD/configuration, planner and conversation history services.
- Plausible first-party paths checked: Case/model comparison → performance results → automatic model/agent configuration adoption; test-case authoring → future harness capability revision; conversation memory → prospective options.
- Why no material first-party path remains: Test results are persisted but no accepted option is automatically returned into agent config or a function-specific parent S4 approval/return workflow; ordinary profile editing and history lookup do not complete prospective adaptation.

## S5 — Policy and identity

- State: —
- Function: No established first-party ultimate-purpose/identity decision authority and governed return path for the declared BotSharp agent application.
- Disturbance / variety regulated: Potential policy, allowed agent behaviors, plugin permissions or changing administrator intents, but examined controls operate as configuration and local function permissions.
- Decisive decision or feedback right: Administrator supplies agent profiles and plugins; `human_intervention_needed` emits an ordinary conversation hook. Neither defines an institutional ultimate-policy question/legitimate deciding authority and closed application-wide return.
- Decision owner: Application operator/developer controls configuration; no evidenced S5-specific parent/agent role with ultimate-policy feedback closure.
- Supporting / enforcement mechanisms: Agent create/update/disabled flags, tool callbacks, administrator authorization and human-intervention hook.
- Closure path: Runtime may reject disabled agents or call a hook; no identity dispute/proposal → legitimate ultimate authority → authoritative decision → returned policy governing later operation is wired.
- Why this is / is not agent-owned: An autonomous model cannot be inferred to settle ultimate identity by selecting agents; operator settings are not sufficient to claim S5=P.
- Evidence: [RouteToAgentFn.cs](https://github.com/SciSharp/BotSharp/blob/dbc3103afc5cc6e03892ab9da066b9955f45c1aa/src/Infrastructure/BotSharp.Core/Routing/Functions/RouteToAgentFn.cs#L64); [InstructExecutor.cs](https://github.com/SciSharp/BotSharp/blob/dbc3103afc5cc6e03892ab9da066b9955f45c1aa/src/Infrastructure/BotSharp.Core/Routing/Reasoning/InstructExecutor.cs#L59); [HumanInterventionNeededFn.cs](https://github.com/SciSharp/BotSharp/blob/dbc3103afc5cc6e03892ab9da066b9955f45c1aa/src/Infrastructure/BotSharp.Core/Routing/Functions/HumanInterventionNeededFn.cs#L17); [AgentService.UpdateAgent.cs](https://github.com/SciSharp/BotSharp/blob/dbc3103afc5cc6e03892ab9da066b9955f45c1aa/src/Infrastructure/BotSharp.Core/Agents/Services/AgentService.UpdateAgent.cs#L9).
- Basis: Observed runtime configuration/hook boundaries against Profile identity-policy closure requirements.
- Confidence: Medium-high inside the declared installable runtime.
- Caveats: A host organization may supply its own S5 outside the product. This review does not equate absence in the harness with absence in the developer/business organization.

### Absence scope

- Surfaces inspected: First-party agent management, router permissions/disabled agent check, per-conversation intervention callback and operator/test authentication.
- Plausible first-party paths checked: Agent profile edit, static policies, human intervention notification, privileged test authorization and agent enable/disable action.
- Why no material first-party path remains: Examined actions govern individual operation or app configuration; none implements a complete function-specific legitimate ultimate-purpose/identity decision and returned governance loop.

## Distributed OSS parent arrangement

BotSharp is a self-hostable Apache-2.0 framework. The upstream developer project and an adopter's local administrators are not one shared operating metasystem. A contributor PR, admin API or optional manual test run is not evidence of organizational parent-mode S3/S4/S5 closure at the installed application recursion.

## Self-hosted and non-human modes

Both operator-configured and model-directed execution paths were considered. An administrator may edit agents and trigger evaluation but no standard function-specific parent decision-return path is evidenced. The task-level model-directed router closes S1 only; neither provider service nor maintainer CI supplies other autonomous function ownership.

## Recursion

Routing-stack entries and a nested specialist invocation are task/subprocess delegation, not automatically separate viable systems with their own S2-S5. The reviewed level is a BotSharp application composed of routable roles; no stronger multi-level viable organizational closure claimed.

## Variety and escalation

Conversation dialogs, tool feedback, routing fallback, missing-field redirection, bounded recursion and human-intervention notification help manage operational variety and escalate per-task issues. They are not by themselves inter-S1 conflict regulation, application-wide resource/commitment decisions, independent corrective auditing, prospective adaptation or ultimate-policy adjudication.

## Evidence gaps

This is a source-grounded assessment of the immutable pinned revision, not a live integration run: the external inference providers and adopter-created tools were not executed, and no production human/agent decision trace is attested. Potential separately composed third-party plugins, external portfolio controllers and adopter governance are outside the claimed first-party standard boundary. For each negative state the absence conclusion is bounded by the concrete shipped paths inspected, not universal impossibility.

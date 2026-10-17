---
harness_id: project-oagents
project_name: Project OAgents
repository: https://github.com/microsoft/project-oagents
review_ref: e4d262386860fbc586fe9af5fb13c0e293bf7b33
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

# Project OAgents

## Review boundary

- System in focus: The early, installable .NET event-driven OAgents `src/` framework with distinct Orleans and Dapr actor adapters, Semantic Kernel-powered `AiAgent` functions and first-party supported executable sample applications as concrete evidence of reachable operational agency. The assessed parent recursion is **one configured OAgents-based agent application**, not the Microsoft institution, external Semantic Kernel organization, arbitrary customer applications, or a synthetic union of different demonstration teams.
- Purpose and identity: Let developers define event-handling agent roles with persisted conversation context and invoke model-based functions on routed events, including runnable first-party marketing, GitHub developer-team and customer-support demonstration configurations.
- Relevant environment: Incoming user and peer events, external Semantic Kernel provider responses, session/persistent chat history, indexed knowledge search, GitHub requests and content, and organizationally authored policies in optional sample implementations.
- Standard-distribution boundary: `src/Oagents.Core/Abstractions`, `src/Oagents.Orleans`, `src/Oagents.Dapr`, plus *explicitly labeled* sample applications under `samples/` only to demonstrate source-reachable in-tree operating modes. `src/` is abstract and requires adopter subclass `HandleEvent`; do **not** ascribe business/demo-specific callbacks to the reusable core or assume they run in all installations. No packaged off-the-shelf whole-org metasystem assumed.
- Credited operating / distribution surfaces: [src/Oagents.Core/Abstractions/IAgent.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/src/Oagents.Core/Abstractions/IAgent.cs#L1), [src/Oagents.Core/Abstractions/IAiAgent.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/src/Oagents.Core/Abstractions/IAiAgent.cs#L1), [src/Oagents.Orleans/Agent.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/src/Oagents.Orleans/Agent.cs#L7), [src/Oagents.Orleans/AiAgent.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/src/Oagents.Orleans/AiAgent.cs#L10), [src/Oagents.Orleans/AiAgent.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/src/Oagents.Orleans/AiAgent.cs#L47), [src/Oagents.Dapr/Agent.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/src/Oagents.Dapr/Agent.cs#L7), [src/Oagents.Dapr/AiAgent.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/src/Oagents.Dapr/AiAgent.cs#L12), [src/Oagents.Dapr/AiAgent.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/src/Oagents.Dapr/AiAgent.cs#L49), [samples/marketing/src/backend/Agents/Writer/Writer.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/samples/marketing/src/backend/Agents/Writer/Writer.cs#L19), [samples/support-center/src/backend/Agents/Dispatcher/Dispatcher.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/samples/support-center/src/backend/Agents/Dispatcher/Dispatcher.cs#L16), [samples/gh-flow/src/Microsoft.AI.DevTeam/Agents/Developer/Developer.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/samples/gh-flow/src/Microsoft.AI.DevTeam/Agents/Developer/Developer.cs#L19). Demonstration-only mechanisms are bounded to demo mode and not promoted as default first-party framework governance.
- Adjacent first-party surfaces excluded from ownership: Sample-only GitHub workflow requirements/marketing policy, prompt content and product/team identity, external Microsoft maintainer/CLA process, externally configured Orleans/Dapr infrastructure and Azure/OpenAI/Semantic Kernel/Qdrant service decision rights. `samples/WorkflowsApp` and separate sample backend assemblies are not automatically integrated with core `src/` agent applications.
- First-party operating / deployment modes considered: Orleans `Agent` grain event subscription and `AiAgent<T>` with Semantic Kernel and persisted state; Dapr `Agent` actor publishing cloud events and `AiAgent<T>` with state manager, model function and memory search; runnable marketing / support-center / GitHub dev-team samples showing concrete event handlers and generated outputs; their optional auditor/corrective cycle as a **demo-specific** witness tested for S3* closure.
- Recursion level: One event-driven .NET agent application, with configured AI actors as task-operating cells. Samples are alternative applications illustrating a reachable S1 and possible role composition, not simultaneously one aggregate organization.
- Reviewed revision: `e4d262386860fbc586fe9af5fb13c0e293bf7b33`, exactly pinned by Index candidate intake #202 and serial batch #1669.
- Observation date: 2026-10-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The core `IAgent` interface declares `HandleEvent` and `PublishEvent`. Both Orleans and Dapr versions implement event publishing with existing messaging infrastructure; Orleans `Agent` automatically subscribes its grain to a keyed event stream on activation, then dispatches to **abstract, application-written** `HandleEvent`. Dapr `Agent` exposes the abstract event handler and publishes cloud events through a configured `DaprClient`. Neither low-level transport is by itself a self-governing model-directed agent. [src/Oagents.Core/Abstractions/IAgent.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/src/Oagents.Core/Abstractions/IAgent.cs#L3), [src/Oagents.Orleans/Agent.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/src/Oagents.Orleans/Agent.cs#L7), [src/Oagents.Orleans/Agent.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/src/Oagents.Orleans/Agent.cs#L12), [src/Oagents.Orleans/Agent.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/src/Oagents.Orleans/Agent.cs#L17), [src/Oagents.Orleans/Agent.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/src/Oagents.Orleans/Agent.cs#L25), [src/Oagents.Dapr/Agent.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/src/Oagents.Dapr/Agent.cs#L7), [src/Oagents.Dapr/Agent.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/src/Oagents.Dapr/Agent.cs#L15), [src/Oagents.Dapr/Agent.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/src/Oagents.Dapr/Agent.cs#L17).

`AiAgent<T>` in both adapters owns a concrete `CallFunction` path that creates a Semantic Kernel function from a supplied prompt, awaits the actual `_kernel.InvokeAsync` and records model-generated responses into actor history/state. `AddKnowledge` queries configured semantic memory to add retrieved text to an invocation's arguments. Crucially, automatic independent dynamic tool selection, arbitrary workflow reorganization and multi-step policy arbitration are **not** built into these base methods: application-defined event handlers choose which prompts/next events to invoke. [src/Oagents.Orleans/AiAgent.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/src/Oagents.Orleans/AiAgent.cs#L10), [src/Oagents.Orleans/AiAgent.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/src/Oagents.Orleans/AiAgent.cs#L34), [src/Oagents.Orleans/AiAgent.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/src/Oagents.Orleans/AiAgent.cs#L47), [src/Oagents.Orleans/AiAgent.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/src/Oagents.Orleans/AiAgent.cs#L66), [src/Oagents.Dapr/AiAgent.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/src/Oagents.Dapr/AiAgent.cs#L32), [src/Oagents.Dapr/AiAgent.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/src/Oagents.Dapr/AiAgent.cs#L49), [src/Oagents.Dapr/AiAgent.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/src/Oagents.Dapr/AiAgent.cs#L69).

The repository includes separately executable *explicitly demo-only* first-party apps. The marketing Writer takes user text, calls `CallFunction(WriterPrompts.Write)`, publishes `ArticleCreated` and `AuditText`, and can process a returned auditor alert with `WriterPrompts.Adjust`. The separate marketing Auditor reads generated article text, applies a prompt checking for discount greater than 10%, and publishes `AuditorAlert` to Writer and UI when the policy is breached. The support-center Dispatcher uses model classification of user input against role choices to publish typed work events; GitHub Dev Team agents invoke distinct Semantic Kernel models for planning/code generation. These establish a first-party *supported runnable demonstrator* of model-authored operating output and event-return, but this bounded demo is not evidence that the reusable core owns a genuine live whole-organization S2–S5 metasystem. [samples/marketing/README.md](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/samples/marketing/README.md#L1), [samples/marketing/src/backend/Agents/Writer/Writer.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/samples/marketing/src/backend/Agents/Writer/Writer.cs#L35), [samples/marketing/src/backend/Agents/Writer/Writer.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/samples/marketing/src/backend/Agents/Writer/Writer.cs#L57), [samples/marketing/src/backend/Agents/Writer/Writer.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/samples/marketing/src/backend/Agents/Writer/Writer.cs#L75), [samples/marketing/src/backend/Agents/Auditor/Auditor.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/samples/marketing/src/backend/Agents/Auditor/Auditor.cs#L24), [samples/marketing/src/backend/Agents/Auditor/Auditor.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/samples/marketing/src/backend/Agents/Auditor/Auditor.cs#L35), [samples/marketing/src/backend/Agents/Auditor/AuditorPrompts.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/samples/marketing/src/backend/Agents/Auditor/AuditorPrompts.cs#L3), [samples/support-center/src/backend/Agents/Dispatcher/Dispatcher.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/samples/support-center/src/backend/Agents/Dispatcher/Dispatcher.cs#L56), [samples/gh-flow/src/Microsoft.AI.DevTeam/Agents/Developer/Developer.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/samples/gh-flow/src/Microsoft.AI.DevTeam/Agents/Developer/Developer.cs#L25).

**License boundary:** GitHub's top-level license detection is **CC BY 4.0** because `LICENSE` governs docs/content; the repository `README.md` explicitly grants code rights separately under **MIT `LICENSE-CODE`**. Treating the code as CC-only, or treating documentation as MIT, would misstate the upstream source. [README.md](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/README.md#L30).

## Operational model

The core `src/` package supplies first-party model invocation and message/persistence mechanisms; actual operating judgment is instantiated by a selected subclass's user/event-specific handler. In first-party runnable examples, an AI actor evaluates an open-ended message, produces content or intent and emits a downstream event; actual model output affects subsequent operational work. That **bounded supported example mode**, not bare Orleans/Dapr transport, justifies `S1=A`. Each event stream / sample team can have multiple actors, but a producer/consumer chain or a promotional team metaphor does not automatically constitute a higher viable organizational recursion.

## S1 — Operations

- State: A
- Function: Respond to user/environment events through model-authored content or intent classification and return model results into visible task outputs, follow-on agent events or next task revision.
- Disturbance / variety regulated: Unstructured user support, content-generation, requirements and code tasks; fresh model outputs, semantic memory results, optional auditor suggestions and domain event messages.
- Decisive decision or feedback right: Supported runnable first-party examples call actual Semantic Kernel inference through base `AiAgent<T>.CallFunction`; model output is used as a Writer article, intent for Dispatcher routing or generated code/plan, and event delivery exposes the result to later actors.
- Decision owner: Configured model-bearing AI agent subclass in the concrete example operating mode. Model supplies discretionary text/intent; hard-coded app role routing and external prompt, SK provider and developer permissions bound the operating choices.
- Supporting / enforcement mechanisms: Orleans/Dapr event bus and actor activation, persistent per-agent chat context/state, SK `Kernel.InvokeAsync`, supplied prompts, `AddKnowledge` memory lookup and demo event-processing handlers.
- Closure path: Input `UserChatInput` / domain event → actor `HandleEvent` → first-party `CallFunction` and model response → `ArticleCreated`/support dispatch/GitHub-task output → event bus to consumer or visible UI. In marketing demo, a later AuditorAlert can trigger Writer revision using observed critique.
- Boundary reachability: `src/` `AiAgent` constructor and `CallFunction` are concrete inherited implementation; `samples/marketing` has a documented runnable backend/Orleans configuration and a concrete `Writer : AiAgent<WriterState>` subscribing to user events, calling SK and publishing downstream work. The basic abstract `Agent` on its own is only an extensible runtime.
- Why this is / is not agent-owned: At runnable sample boundary the configured model meaningfully chooses generated content, wording and intent from input rather than simply executing a hard-coded response; event transport, prompt choice and infrastructure are not credited autonomous policy.
- Evidence: [src/Oagents.Orleans/Agent.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/src/Oagents.Orleans/Agent.cs#L25); [src/Oagents.Orleans/AiAgent.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/src/Oagents.Orleans/AiAgent.cs#L47); [src/Oagents.Dapr/AiAgent.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/src/Oagents.Dapr/AiAgent.cs#L49); [samples/marketing/src/backend/Agents/Writer/Writer.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/samples/marketing/src/backend/Agents/Writer/Writer.cs#L35); [samples/marketing/src/backend/Agents/Writer/Writer.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/samples/marketing/src/backend/Agents/Writer/Writer.cs#L75); [samples/support-center/src/backend/Agents/Dispatcher/Dispatcher.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/samples/support-center/src/backend/Agents/Dispatcher/Dispatcher.cs#L67); [samples/gh-flow/src/Microsoft.AI.DevTeam/Agents/Developer/Developer.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/samples/gh-flow/src/Microsoft.AI.DevTeam/Agents/Developer/Developer.cs#L27); [samples/marketing/README.md](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/samples/marketing/README.md#L1).
- Basis: First-party concrete model/function invocation and executable demo callback/result path; positive strictly scoped to the instantiated example agent rather than bare abstract interfaces.
- Confidence: Medium-high for code reachability; low for untested hosted provider/actual model reliability.
- Caveats: Model-generated output/intent qualifies limited S1 operational choice, not unrestricted autonomous tool selection. `src/` alone cannot operate without a subclass, configured Semantic Kernel, credentials and host; examples are explicitly demonstrations and not evidence of production governance.

## S2 — Coordination

- State: —
- Function: No shipped first-party S2-specific control attenuates a demonstrable conflict or oscillation between independently viable S1 units.
- Disturbance / variety regulated: Multiple role agents can publish and receive events; duplicate/conflicting or competing work could occur, but no packaged active inter-unit disturbance regulator is established.
- Decisive decision or feedback right: Event streams route events to actor subscriptions; support Dispatcher classifies which role receives a user request. Neither adjudicates concrete interference among distinct viable operating units or adjusts both sides to stabilize a shared constraint.
- Decision owner: External developer scripts event routing and the sample-specific model intent classifier; no enduring S2 actor with specific damping mandate.
- Supporting / enforcement mechanisms: Orleans stream ID/namespace subscriptions, Dapr PublishEvent, Dispatcher `DispatcherChoice`, typed events, static routing and application-written handlers.
- Closure path: User event → Dispatcher or fixed stream → receiving agent; there is no sensed inter-agent disturbance → specific stabilization decision → feedback changing affected separate S1 agents' operating behavior.
- Why this is / is not agent-owned: An event bus, multi-role demo and model-chosen specialist routing are communication/dispatch, not automatically S2 coordination in the VSM sense.
- Evidence: [src/Oagents.Orleans/Agent.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/src/Oagents.Orleans/Agent.cs#L17); [src/Oagents.Orleans/Agent.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/src/Oagents.Orleans/Agent.cs#L25); [src/Oagents.Dapr/Agent.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/src/Oagents.Dapr/Agent.cs#L17); [samples/support-center/src/backend/Agents/Dispatcher/Dispatcher.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/samples/support-center/src/backend/Agents/Dispatcher/Dispatcher.cs#L16); [samples/support-center/src/backend/Agents/Dispatcher/Dispatcher.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/samples/support-center/src/backend/Agents/Dispatcher/Dispatcher.cs#L118); [samples/marketing/src/backend/Agents/Writer/Writer.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/samples/marketing/src/backend/Agents/Writer/Writer.cs#L75).
- Basis: Bounded absence after testing multi-agent buses, dispatcher, alternate backend and sample role composition.
- Confidence: Medium-high within frozen first-party scope.
- Caveats: Users could write an S2-specific event-policy agent; this extension possibility is not evidence the framework already owns S2.

### Absence scope

- Surfaces inspected: Core IAgent/IAiAgent, Orleans and Dapr Agent event dispatch, support-center Dispatcher, marketing team and GitHub Dev Team event chains.
- Plausible first-party paths checked: Stream ordering and namespace routing, model intent classification, peer agent outputs, publish/subscribe coordination, duplicate/competing events.
- Why no material first-party path remains: Inspected first-party stream subscribers and classifier dispatch particular tasks but do not observe/control concrete conflict or reciprocal behavior among independently viable S1 units.

## S3 — Inside-and-now control

- State: —
- Function: No coherent system-wide current-control role with a whole-application view and binding priority/resource/commitment interventions across independently operating units.
- Disturbance / variety regulated: Parallel marketing/support/developer requests, budget/capacity tradeoffs, deadlines and conflicting team commitments are possible; actual app-wide control over them is not implemented.
- Decisive decision or feedback right: Sample Dispatcher selects a specialist based on a user message, DeveloperLead creates a task plan, and marketing actors publish outputs. No first-party system-level manager decides ongoing resource, responsibility or workstream priority across viable S1 cells.
- Decision owner: Sample app developer, local business actor and event bus; model task plan and subscriber scheduling do not create a separate system-wide S3 owner.
- Supporting / enforcement mechanisms: Persisted actor histories, stream event delivery, per-role prompts, local coordination via events, optional Azure/Dapr hosting configuration.
- Closure path: Role-specific current outputs and requests advance between actors; missing whole-current operating view → authoritative allocation/commitment decision → returned changed assignments across multiple S1 units.
- Why this is / is not agent-owned: Support dispatch, DevLead's task-specific planning and article workflow progression are S1 task decomposition. Neither host infrastructure nor a human authoring an example application supplies a demonstrated parent S3.
- Evidence: [samples/support-center/src/backend/Agents/Dispatcher/Dispatcher.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/samples/support-center/src/backend/Agents/Dispatcher/Dispatcher.cs#L16); [samples/support-center/src/backend/Agents/Dispatcher/Dispatcher.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/samples/support-center/src/backend/Agents/Dispatcher/Dispatcher.cs#L67); [samples/gh-flow/src/Microsoft.AI.DevTeam/Agents/DeveloperLead/DeveloperLead.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/samples/gh-flow/src/Microsoft.AI.DevTeam/Agents/DeveloperLead/DeveloperLead.cs#L24); [samples/gh-flow/src/Microsoft.AI.DevTeam/Agents/Developer/Developer.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/samples/gh-flow/src/Microsoft.AI.DevTeam/Agents/Developer/Developer.cs#L25); [samples/marketing/src/backend/Agents/Writer/Writer.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/samples/marketing/src/backend/Agents/Writer/Writer.cs#L20); [src/Oagents.Orleans/Agent.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/src/Oagents.Orleans/Agent.cs#L25).
- Basis: Tested plausible manager candidates at actual application recursion, bounded negative.
- Confidence: Medium-high for package and supported examples.
- Caveats: A real enterprise organization can have parent S3 outside this framework; not inherited from Microsoft's developer project.

### Absence scope

- Surfaces inspected: Core event hosting, marketing app event graph, support center Dispatch, GitHub DevTeam Lead planning, actor persistence and external operator edges.
- Plausible first-party paths checked: Dispatcher as whole-current coordinator, DeveloperLead as manager, event stream as shared view, Auditor as escalation, Orleans/Dapr state and task-specific prompts.
- Why no material first-party path remains: All decisions concern a local request/role or static event flow. No packaged actor owns a whole-current resource/priority/commitment view, a legitimate parent decision and returned enforcement on independent S1s.

## S3* — Complementary audit

- State: —
- Function: No independently governed whole-current complementary audit challenges ordinary S3 management claims and authoritatively returns corrective control.
- Disturbance / variety regulated: Marketing copy may breach a ten-percent discount constraint; an in-tree *demo* Auditor inspects generated article text and publishes a targeted corrective alert. No independent whole-current reality-check mechanism is packaged for framework control.
- Decisive decision or feedback right: Sample Auditor has a model-based text-specific rule and can send `AuditorAlert` to Writer, which re-generates text. That is a genuine scoped **first-party demonstration of QA feedback**, not an owner with independent direct access to operating facts against S3 reporting and a returned S3 corrective mandate.
- Decision owner: Marketing demo Auditor model and Writer request handler; the prompt policy is hard-coded in sample. There is no standalone S3* role in reusable `src/` and no shown ordinary S3 system whose claims can be audited.
- Supporting / enforcement mechanisms: `AuditText` and `AuditorAlert` events, sample model prompt, article text relay, Writer `Adjust` prompt, UI SignalR alert.
- Closure path: Writer generates text → publishes AuditText → demo Auditor checks discount text → emits AuditorAlert → Writer adjusts text. This **task-local revision loop exists**, but there is no separate independently sourced operational audit of a current system-control claim nor a return to a legitimate S3 decision affecting actual S1 commitments.
- Why this is / is not agent-owned: Independent agent identity and second opinion about generated content do not suffice for VSM S3* when it receives the same produced output, judges only a hard-coded local copy constraint and lacks a complementary direct-evidence path/organizational controller.
- Evidence: [samples/marketing/src/backend/Agents/Writer/Writer.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/samples/marketing/src/backend/Agents/Writer/Writer.cs#L35); [samples/marketing/src/backend/Agents/Writer/Writer.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/samples/marketing/src/backend/Agents/Writer/Writer.cs#L57); [samples/marketing/src/backend/Agents/Writer/Writer.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/samples/marketing/src/backend/Agents/Writer/Writer.cs#L75); [samples/marketing/src/backend/Agents/Auditor/Auditor.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/samples/marketing/src/backend/Agents/Auditor/Auditor.cs#L24); [samples/marketing/src/backend/Agents/Auditor/Auditor.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/samples/marketing/src/backend/Agents/Auditor/Auditor.cs#L35); [samples/marketing/src/backend/Agents/Auditor/Auditor.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/samples/marketing/src/backend/Agents/Auditor/Auditor.cs#L48); [samples/marketing/src/backend/Agents/Auditor/AuditorPrompts.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/samples/marketing/src/backend/Agents/Auditor/AuditorPrompts.cs#L3); [samples/marketing/README.md](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/samples/marketing/README.md#L1).
- Basis: Strongest positive candidate (first-party Writer/Auditor corrective loop) inspected rather than dismissed by filename; bounded to demo QA rather than organizational complementary audit.
- Confidence: Medium; distinction depends on fixed application recursion and complementary-access requirement.
- Caveats: The demo proves writer/auditor task correction, not real independent S3* governance. Re-scoping to an organization with independent operating evidence and a genuine S3 actor would be a separate source-backed case.

### Absence scope

- Surfaces inspected: Marketing Auditor, discount-policy prompt, Writer AuditedText/AuditorAlert handler, SignalR notification, support/GitHub role feedback, core event and memory interfaces.
- Plausible first-party paths checked: Independent marketing review, correction routed back to content creation, peer review/approval, real external business state sources and central operating-control intervention.
- Why no material first-party path remains: The sample reviewer only reads Writer-supplied text for one static copy threshold and loops a response back to the same S1. No independent operational facts versus S3 status and no authoritative management-wide corrective return are shipped in the inspected boundary.

## S4 — Outside-and-then intelligence

- State: —
- Function: No first-party prospective intelligence unit selects future-environment options and authorizes changed organizational capabilities in the running system.
- Disturbance / variety regulated: Market, customer or software-development needs could change; semantic memory lookup can inject existing knowledge for present task generation, not govern future adaptations.
- Decisive decision or feedback right: `AddKnowledge` queries semantic memory and fills prompt arguments; sample authors choose templates and actor topology. No code path independently evaluates longer-horizon alternatives and installs accepted process/tool/organizational changes.
- Decision owner: Application developer and local role-specific LLM task generator, not a future-intelligence authority with capability-change feedback return.
- Supporting / enforcement mechanisms: Semantic Kernel memory search, prompt templates, persistent chat state, events and provider configuration, demonstration planners.
- Closure path: Task arrives → existing memory/documents incorporated into current prompt → result; missing outside-future sensing → strategic options → authorized future capability transformation → subsequent operating adaptation.
- Why this is / is not agent-owned: Knowledge retrieval for current inference and generating a development plan for a ticket are not automatic S4 future viability adaptation.
- Evidence: [src/Oagents.Orleans/AiAgent.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/src/Oagents.Orleans/AiAgent.cs#L66); [src/Oagents.Dapr/AiAgent.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/src/Oagents.Dapr/AiAgent.cs#L69); [samples/gh-flow/src/Microsoft.AI.DevTeam/Agents/DeveloperLead/DeveloperLead.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/samples/gh-flow/src/Microsoft.AI.DevTeam/Agents/DeveloperLead/DeveloperLead.cs#L59); [samples/gh-flow/src/Microsoft.AI.DevTeam/Agents/Developer/Developer.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/samples/gh-flow/src/Microsoft.AI.DevTeam/Agents/Developer/Developer.cs#L64); [README.md](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/README.md#L1).
- Basis: Bounded negative after testing retrieval and sample future-looking planning as positive candidates.
- Confidence: Medium-high at frozen application recursion.
- Caveats: Custom app agents may create R&D or change management workflows beyond the shipped core; not imported as S4.

### Absence scope

- Surfaces inspected: `AddKnowledge` in both backends, memory and state, GitHub DevLead/Developer planning, example roles and actor topology configuration.
- Plausible first-party paths checked: Semantic search as future intelligence, model-generated ticket plans, dynamic team capability updates, lasting revised instructions or deployment topology after observation.
- Why no material first-party path remains: Search and plans feed the current requested output but no built-in option selection/adoption loop installs a changed future capability under system-wide authority.

## S5 — Policy and identity

- State: —
- Function: No built-in legitimate ultimate purpose/identity authority adjudicates competing goals and returns governing organizational policy.
- Disturbance / variety regulated: Hard-coded marketing discount policy and support routing choices constrain local outputs; they do not constitute identity-level arbitration of a viable organization.
- Decisive decision or feedback right: Developer sets `Namespace`, event type, prompts and metadata; sample Auditor applies a discount ceiling, not final ultimate mission authority. External Microsoft CLA and code licenses concern OSS authorship rather than runtime S5.
- Decision owner: Sample author/operator, externally configured business and provider environment; no first-party ultimate purpose-governance actor.
- Supporting / enforcement mechanisms: Fixed agent role classes, sample marketing audit prompt, stream namespace, configurable service settings, repository code/documentation licenses.
- Closure path: Local marketing content constraint → alert/rewrite on a task; missing values/legitimacy dispute → S5 final binding identity decision → corresponding whole-system policy return.
- Why this is / is not agent-owned: Conformance to one threshold, task routing or owner-supplied initial identity is narrower than deciding what the whole system ultimately is/ought to become.
- Evidence: [samples/marketing/src/backend/Agents/Auditor/AuditorPrompts.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/samples/marketing/src/backend/Agents/Auditor/AuditorPrompts.cs#L3); [src/Oagents.Orleans/Agent.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/src/Oagents.Orleans/Agent.cs#L9); [src/Oagents.Dapr/Agent.cs](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/src/Oagents.Dapr/Agent.cs#L7); [README.md](https://github.com/microsoft/project-oagents/blob/e4d262386860fbc586fe9af5fb13c0e293bf7b33/README.md#L1).
- Basis: First-party local policy and identity paths inspected, bounded negative.
- Confidence: Medium-high for package-as-shipped and demo scope.
- Caveats: Actual adopting enterprise may legally own S5; that external authority is not a first-party runtime path.

### Absence scope

- Surfaces inspected: Core Agent/IAgent identity/event, sample marketing audit policy, support Dispatcher choices, environment/config and contributor/maintainer notices.
- Plausible first-party paths checked: Discount compliance rule as mission policy, hard-coded actor identity and namespace, external operator/CLA as parent ultimate authority.
- Why no material first-party path remains: These are local developer-defined constraints and institutional context without shipped whole-application legitimate ultimate-purpose adjudication and binding return.


## Distributed OSS parent arrangement

The owning Microsoft OSS project and its CLA, external hosting/cloud and Semantic Kernel providers, adopter organization and the configured actor application have distinct rights. A developer may supply both policy and runtime to OAgents; no system-wide parent S3/S4/S5 decision-right loop is demonstrated from the extension boundary. Documentation is under CC BY 4.0 and code is under `LICENSE-CODE` MIT; GitHub's CC BY repository badge should not be interpreted as restricting the code to a non-code license.

## Self-hosted and non-human modes

The repo documents an experimental and explicitly not-production-ready state; the reusable `src/` framework and `samples/` apps are source distributions, not published NuGet packages. Orleans/Dapr actor hosting, configured Semantic Kernel and memory services can be self-hosted or provisioned by adopters. Model/secret-dependent live setup was not run. A runnable first-party demo shows task-level model discretion, but does not prove a currently operating production organization or a packaged whole-org control plane.

## Recursion

Writer, Auditor, Dispatcher, Developer Lead and specialized support agents are individual example roles; separate sample apps are independent demonstration system boundaries and must not be combined into a fictional single organization. The sample Writer/Auditor feedback path is a bounded task correction at a single marketing application, not independently verified recursive S3*/S3 systemic closure.

## Variety and escalation

Event namespace subscriptions and Dapr publishing dispatch operational variety; per-agent history/memory allows context-dependent model responses. Marketing AuditText/AuditorAlert provides task compliance feedback and an optional user-visible warning. No first-party demonstrated algedonic cross-organizational escalation, a central current resource manager or ultimate purpose-governing authority may be inferred from this local notification.

## Evidence gaps

- The source's strongest operational positive is a **documented first-party runnable sample** with `AiAgent.CallFunction` returning model content into actual event consumers. The `src/` base class itself is abstract and requires external app-written `HandleEvent`. Thus S1=A is **sample-supported** and not a claim every OAgents installation autonomously selects tools or deploys a working team.
- The marketing Auditor is a genuine independent *sample agent* with explicit audit alert/Writer revision. It only has the same generated marketing text, a fixed discount rule and task-level corrective feedback; no independent physical/operational audit against S3 claims or management corrective return is demonstrated. This bounded negative does not deny its useful QA behavior.
- The repo says experimental, core libraries only in `src/`, and no NuGet publication as of frozen commit. Assessment does not certify runtime production readiness or external hosted provider behavior.
- Documentation `LICENSE` CC BY 4.0 and code `LICENSE-CODE` MIT are **distinct**; repository metadata alone is not a reliable code-license statement.
- Frozen primary-source inspection only; no cloud credentials, real Semantic Kernel inference, .NET service launch or integration tests executed. Index structural check and generators validate artifact consistency, not deployment efficacy.

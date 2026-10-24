---
harness_id: active-graph
project_name: Active Graph
repository: https://github.com/yoheinakajima/activegraph
review_ref: 50d8405923b79e4e823a73a3045bb969436a872c
reviewed_at: 2026-10-19
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Active Graph

## Review boundary

- System in focus: The shipped first-party Python **Active Graph reactive, event-sourced graph and LLM-agent behavior runtime**, at the recursion of a model-backed goal-facing operating application configured with one or more `@llm_behavior` actor(s), tools, graph patches and follow-up reactive behaviors. The runtime may execute deterministic behaviors without a model, but S1 attribution is to its **supported optional first-party model-provider + tool-use mode**, not to a bare SQLite event store or prerecorded fixture.
- Purpose and identity: Represent a changing task world as typed objects/relations/events, let registered behaviors (including configured model-backed agents) react to relevant changes, obtain tool results, modify world state by accepted patches, and maintain provenance, repeatability and bounded execution.
- Relevant environment: Novel goals, graph and relation changes, conflicting patches, uncertain model replies, tool observations, provider/network failures, capability and approval constraints, event queue growth, handler errors, replay/fork differences and unknown future task variations.
- First-party standard distribution: `activegraph/core/*`, `behaviors/{base,decorators}.py`, `runtime/{runtime,registry,queue,scheduler,authority,diff,behavior_graph}.py`, `llm/{provider,openai,anthropic,recorded}.py`, `tools/*`, `frame.py`, `policy.py`, `packs/diligence/*`, `store/*`, sandbox/sinks and CLI quickstart. User-written pack goals, external model-provider service and wider deployed business organizations are not first-party governance.
- Credited operating / distribution surfaces: [README.md#L1](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/README.md#L1), [README.md#L105](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/README.md#L105), [activegraph/behaviors/decorators.py#L215](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/behaviors/decorators.py#L215), [activegraph/runtime/runtime.py#L1050](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/runtime/runtime.py#L1050), [activegraph/runtime/runtime.py#L1072](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/runtime/runtime.py#L1072), [activegraph/runtime/runtime.py#L1293](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/runtime/runtime.py#L1293), [activegraph/runtime/runtime.py#L1481](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/runtime/runtime.py#L1481), [activegraph/runtime/runtime.py#L1903](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/runtime/runtime.py#L1903), [activegraph/runtime/runtime.py#L2097](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/runtime/runtime.py#L2097), [activegraph/packs/diligence/behaviors.py#L111](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/packs/diligence/behaviors.py#L111).
- Adjacent first-party surfaces excluded from ownership: Independently defined business/service divisions and the separate `activegraph-packs`, `activegraph-lab` and `regimes` repos; external Anthropic/OpenAI providers and their policy governance; developer-authored goals/policies/approval officers; benchmarks, paper claims and test fixtures as live model inference. The bundled Diligence pack is inspected as a first-party example but does not define a universal separate enterprise.
- First-party operating / deployment modes considered: Pure deterministic `@behavior` and `@relation_behavior`; actual `@llm_behavior` with configured provider, typed graph view and optional declared model-selectable tools; goal/event-triggered queue, patch validation, reactive follow-up, frame/budget/policy restrictions, replay with LLM/tool result cache, strict/permissive restoration, manual `Runtime.fork()` and `diff()`, optional packs, recorded offline quickstart and LLM provider extras.
- Recursion: One goal-facing graph application in which model-driven behavior can own operational task choices. Event subscriptions, relation behaviors and object types may belong to separate agent actors when *application-configured*, but durable independently viable S1 divisions and their organizational metasystem are not established by default merely by choosing multiple behaviors.
- Frozen source identity: GitHub repository ID **1240421258**, public `yoheinakajima/activegraph@50d8405923b79e4e823a73a3045bb969436a872c` on `main`, Git tree `7a7534712aad4240e7060f05823f9b364b1b2c92`, Apache-2.0 root license; [batch #1753](https://github.com/opensiro/vsm-harness-index/issues/1753). Reviewed 2026-10-19 under Index active Profile 0.2.4 / Methodology 0.3.7; Skills default branch currently advertises 0.3.8, **not** substituted into Index generation provenance.

## Repository architecture

`Graph` and event storage materialize objects/relations from an append-only log. `Runtime.run_goal` enqueues a goal; `run_until_idle` consumes the derived queue, selecting registered regular, relation or LLM-backed behaviors by event subscriptions, graph shape predicates and policy eligibility. Ordinary behaviors can propose `BehaviorGraph` patches, subject to optimistic conflict and runtime enforcement. `@llm_behavior` is a first-party registered behavior configuration; `Runtime._invoke_llm` constructs a contextual prompt with a scoped graph `View`, emits `llm.requested`, invokes the configured `LLMProvider` or explicit replay cache, and records `llm.responded`. If a model returns declared tool calls, the runtime dispatches first-party typed tools, appends actual tool-result messages and invokes the model again, up to configured limits. The model's terminal structured output is handed to the registered behavior function, which may propose graph changes leading to later reactive actions. [activegraph/runtime/runtime.py#L1050](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/runtime/runtime.py#L1050); [activegraph/runtime/runtime.py#L1293](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/runtime/runtime.py#L1293); [activegraph/runtime/runtime.py#L1481](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/runtime/runtime.py#L1481); [activegraph/runtime/runtime.py#L1751](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/runtime/runtime.py#L1751); [activegraph/runtime/runtime.py#L1903](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/runtime/runtime.py#L1903); [activegraph/runtime/runtime.py#L1979](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/runtime/runtime.py#L1979); [activegraph/runtime/runtime.py#L2097](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/runtime/runtime.py#L2097); [activegraph/behaviors/decorators.py#L215](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/behaviors/decorators.py#L215).

The public provider integration ships optional Anthropic/OpenAI adapters, tool-name wire mapping and structured-output schema validation. The bundled Diligence pack registers model-backed extract/analyze/memo behaviors and a small set of deterministic helpers against a typed graph. `activegraph quickstart` uses a **recorded** model provider with fixed fixtures so behavior/event/log mechanics can run without a live API: this is a real offline first-party pipeline, but deterministic recorded responses must not be mistaken for observed new model decisions. The user can enable actual model inference by configuring an optional provider in the same shipped `Runtime`. [activegraph/llm/provider.py#L1](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/llm/provider.py#L1); [activegraph/llm/openai.py#L1](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/llm/openai.py#L1); [activegraph/llm/anthropic.py#L1](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/llm/anthropic.py#L1); [activegraph/llm/recorded.py#L1](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/llm/recorded.py#L1); [activegraph/llm/wire.py#L1](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/llm/wire.py#L1); [activegraph/packs/diligence/behaviors.py#L111](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/packs/diligence/behaviors.py#L111).

`RelationBehavior` attaches transformation logic to typed edges, event/pattern subscriptions trigger follow-up behavior, and graph patches serialize accepted changes or emit rejections. These primitives *could* implement a real inter-operating-unit coordinator in an application, but the first-party runtime is a **general engine**: it does not, merely by shipping a graph and relation handlers, define separate viable operational divisions, the specific conflicting commitments they make, and a distinct organizational S2 owner with reciprocal adjustment. Policy/authority ceilings and human approval gate capabilities, budgets, sandboxing and trace/replay are supportive mechanisms, not discretionary VSM S3/S3*/S5 authority. [activegraph/behaviors/decorators.py#L150](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/behaviors/decorators.py#L150); [activegraph/runtime/authority.py#L55](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/runtime/authority.py#L55); [activegraph/runtime/runtime.py#L1072](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/runtime/runtime.py#L1072); [activegraph/runtime/runtime.py#L3393](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/runtime/runtime.py#L3393); [activegraph/runtime/diff.py#L108](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/runtime/diff.py#L108); [activegraph/policy.py#L1](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/policy.py#L1).

The runtime's `fork`, `diff` and strict replay let developers branch old event streams, compare graph states and test changed model/policy configurations. Fork creation and branch choice are caller-selected; the source does not provide a distinct **model-owned prospective strategy evaluator and adoption into future operational configuration** at this declared recursion. An event log that retains history and a replay cache that avoids repeated LLM cost provide observability/testability and time consistency, not automatic S4 evolution. [activegraph/runtime/runtime.py#L3393](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/runtime/runtime.py#L3393); [activegraph/runtime/runtime.py#L3583](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/runtime/runtime.py#L3583); [activegraph/runtime/diff.py#L79](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/runtime/diff.py#L79).

## Operational model

An application gives the graph a goal. Registered model-backed behaviors sense scoped event/graph context, choose a response and optional tools, receive actual tool feedback and can commit graph patches that drive later actions. Regular/relation behaviors, optimistic patch checks and event log coordinate deterministic flow. Provider wiring, a budget, an attached policy and manual replay/fork tools are separable from organizational strategy/adjudication functions.

## S1 — Operations

- State: A
- Function: Execute context-sensitive agent steps against a changing graph/goal, using model-selected responses, tools and observed results in the supported live-provider mode.
- Disturbance / variety regulated: New goal types, variable evidence and graph events, differing tool result content, tool/model failures and uncertain model next actions.
- Decisive decision or feedback right: Registered `@llm_behavior` provider model selects a response or declared tool call from the current graph view, tool definitions and prior tool messages; output handler turns model results into task-relevant graph mutations and reactive follow-up.
- Decision owner: Configured LLM through first-party `LLMBehavior`, `Runtime._invoke_llm`, `LLMProvider.complete` and tool dispatch; the provider infrastructure is external, but the shipped model-decision composition is implemented here.
- Supporting / enforcement mechanisms: Event subscriptions, contextual graph view, frame, policy, tools registry, behavior scheduling, accepted patches, recorded event causality, tool-turn bounds and tool-error feedback.
- Closure path: Goal/event → model-backed behavior → provider completion → selected tool(s) executed → result messages re-enter same model loop → final interpreted output and proposed graph patch → event-sourced graph updated → next event triggers model/deterministic behavior.
- Boundary reachability: Public `@llm_behavior` and `Runtime(graph,llm_provider=...)` directly enter runtime-owned `_invoke_llm` → live provider call/replay → tool dispatch → result to subsequent LLM turn → `BehaviorGraph` proposal. The bundled Diligence pack includes executable model-backed behavior definitions; the offline quickstart exercises identical event/behavior composition with a deliberately recorded surrogate.
- Why this is / is not agent-owned: If the model actor is removed but the event router, graph store, tool registry and policy remain, deterministic subscribers can fire but cannot generate varied task-sensitive decisions and tools from unknown evidence. Recorded fixtures are not live cognition; opt-in shipped provider mode is the S1 positive.
- Evidence: [activegraph/behaviors/decorators.py#L215](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/behaviors/decorators.py#L215), [activegraph/runtime/runtime.py#L1050](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/runtime/runtime.py#L1050), [activegraph/runtime/runtime.py#L1293](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/runtime/runtime.py#L1293), [activegraph/runtime/runtime.py#L1481](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/runtime/runtime.py#L1481), [activegraph/runtime/runtime.py#L1903](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/runtime/runtime.py#L1903), [activegraph/runtime/runtime.py#L1979](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/runtime/runtime.py#L1979), [activegraph/runtime/runtime.py#L2097](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/runtime/runtime.py#L2097), [activegraph/packs/diligence/behaviors.py#L111](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/packs/diligence/behaviors.py#L111).
- Basis: Structural first-party model-provider/tool feedback route with supported optional live mode, plus actual recorded-fixture offline quickstart.
- Confidence: High for source reachability and offline execution; model service reliability unverified.
- Caveats: Optional external provider SDK/API is needed for real LLM decisions; offline fixture success verifies the orchestrating mechanics only, not model performance.

## S2 — Coordination

- State: —
- Function: No distinct first-party owner of regulation of specific disturbances **between independently viable S1 operating divisions** with mutually revised commitments is evidenced at the declared generic graph-runtime recursion.
- Disturbance / variety regulated: Concurrent graph patches, relation-edge changes, conflicting object updates and event-trigger order can interfere with graph consistency; those disturbances are addressed by optimistic consistency/rejection and queued deterministic handling, not an evidenced portfolio of separately viable S1 operations.
- Decisive decision or feedback right: Registered relation behaviors and graph-event selectors apply user-authored transformations; runtime queues, patch conflict rejection and serialized updates resolve **graph state validity**. No source-backed independent S1 units plus separate feedback-regulating owner are specified.
- Decision owner: Developer-defined relation/regular behavior code and deterministic runtime patch/queue rules; any optional model-backed relation would need concrete independent-S1 ownership evidence beyond this general API.
- Supporting / enforcement mechanisms: Typed relations and reactive handlers, event subscription/patterns, optimistic patch validation, deterministic event queue, bounded scheduling and runtime commit log.
- Closure path: Event/patch contention → deterministic commit/reject → subsequent event handlers read revised graph; this is shared-state coherence, not inter-S1 operational interference → S2 decision → adjusted independent organizational commitments.
- Why this is / is not agent-owned: Removing a hypothetical coordinating model still leaves the same generic queue/patch-rejection machinery. A programmable relation handler is a possible application construction site, not a proven default S2 autonomously exercising relational coordination.
- Evidence: [activegraph/behaviors/decorators.py#L150](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/behaviors/decorators.py#L150), [activegraph/runtime/runtime.py#L1072](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/runtime/runtime.py#L1072), [activegraph/runtime/runtime.py#L1293](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/runtime/runtime.py#L1293), [activegraph/runtime/authority.py#L103](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/runtime/authority.py#L103), [activegraph/core/patch.py#L1](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/core/patch.py#L1), [activegraph/core/graph.py#L1](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/core/graph.py#L1).
- Basis: Bounded negative in first-party runtime and bundled example, not universal claim about all third-party packs.
- Confidence: Medium-high.
- Caveats: A separate application may configure real independent S1 divisions and bind a model-led relation coordinator, requiring a new system boundary and evidence.

### Absence scope

- Surfaces inspected: Reactive relation behaviors, typed relations, event subscriptions/patterns, patch-conflict guards, queue and bundled Diligence behaviors.
- Plausible first-party paths checked: Multi-behavior state conflicts, graph updates from independent actors, event sequencing and model-selected change proposals.
- Why no material first-party path remains: No packaged independent viable S1 portfolio plus concrete actual inter-S1 disturbance and reciprocal model-owned coordination/closure is established; graph-state consistency is an infrastructure contract.



## S3 — Inside-and-now control

- State: —
- Function: No first-party autonomous whole-current manager controls independent viable operating divisions' resources, priorities and obligations with a managerial return path.
- Disturbance / variety regulated: Event queue or LLM/tool budget exhaustion, failed behaviors, sandbox constraints and approval waiting can threaten a graph run, but these are local run-level risks.
- Decisive decision or feedback right: Developer supplies `Frame`, `Policy`, budget limits, tools and registered behaviors; first-party executor checks them, schedules ready behaviors and emits failure/budget events. No separate agent is shown renegotiating a portfolio of independent S1 commitments.
- Decision owner: Human/application constructor and deterministic runtime budget/scheduler/authority evaluator, not an operational S3 executive.
- Supporting / enforcement mechanisms: Frame goal/constraints, budget consumption and run_quantum, scheduler, policy capability ceilings, approval and failure events, event sink status.
- Closure path: Run condition → hard-coded/configured guard or scheduling choice → current behavior invoked/stopped/failure logged; missing whole-current viability manager → new binding priorities/resource rights returned to multiple S1 units.
- Why this is / is not agent-owned: Budget guards and queues are safety/throughput controls; removing a hypothetical model S3 still leaves all their fixed effects intact.
- Evidence: [activegraph/frame.py#L1](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/frame.py#L1), [activegraph/policy.py#L1](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/policy.py#L1), [activegraph/runtime/authority.py#L55](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/runtime/authority.py#L55), [activegraph/runtime/runtime.py#L1072](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/runtime/runtime.py#L1072), [activegraph/runtime/runtime.py#L1364](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/runtime/runtime.py#L1364).
- Basis: Bounded first-party negative including provider-configured model behavior, deterministic and pack modes.
- Confidence: Medium-high.
- Caveats: Downstream application may manage many viable S1 systems atop this runtime; generic registered behavior count is not itself that scope.

### Absence scope

- Surfaces inspected: Frame, Policy, budget and queue/scheduler/authority logic, run limits, approval and fail/retry events.
- Plausible first-party paths checked: Whole-current runtime resource assignment, prioritization, inter-service operating contracts and management decisions from error telemetry.
- Why no material first-party path remains: These mechanisms enforce application-chosen per-run rules and queue behavior, not separate autonomous organizational current-management authority over viable operating S1 divisions.



## S3* — Complementary audit

- State: —
- Function: No separate first-party complementary reality-inspection function independently challenges a current S3 manager's operating picture and returns a corrective action to that manager.
- Disturbance / variety regulated: Incomplete causal traces, untrusted tool/model outputs and behavior faults can mislead users. Event logs, strict replay, fork/diff and observability expose inconsistencies but do not themselves close managerial audit.
- Decisive decision or feedback right: Replay divergence checks and error events can flag mismatched execution; an operator chooses what to inspect. No distinct S3* agent samples actual S1 reality, judges S3 reports and sends an authorized correction into separate S3 decision rights.
- Decision owner: First-party deterministic trace/replay machinery and outside human/developer for interpretation; no autonomous audit owner at this recursion.
- Supporting / enforcement mechanisms: Append-only event log, causal provenance, strict replay, tracing/metrics/sinks, patch rejection events and fork/diff.
- Closure path: Events → trace or replay discrepancy → user inspection/failure event; no independent operational audit finding → established S3 receives it → changes current S1 portfolio control.
- Why this is / is not agent-owned: Full replayability is valuable evidence infrastructure but removing a putative auditor does not change the deterministic event-history artifact. Evidence capture is not an independent audit decision/closure by itself.
- Evidence: [activegraph/runtime/runtime.py#L3393](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/runtime/runtime.py#L3393), [activegraph/runtime/runtime.py#L3583](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/runtime/runtime.py#L3583), [activegraph/runtime/diff.py#L108](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/runtime/diff.py#L108), [activegraph/trace/causal.py#L1](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/trace/causal.py#L1), [activegraph/observability/status.py#L1](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/observability/status.py#L1).
- Basis: Bounded negative after checking dedicated observability and strict replay capabilities.
- Confidence: Medium-high.
- Caveats: Users may implement a qualified external reviewer or application-specific reality-checking model; no such legitimate S3-to-S3* relation is bundled.

### Absence scope

- Surfaces inspected: Event log, causal graph, replay divergence, fork/diff, behavior errors and observability sinks.
- Plausible first-party paths checked: Independent inspection of current behavior reports and external system facts, challenge of S3 managerial summaries, audit corrective feedback.
- Why no material first-party path remains: Source supplies records and replay determinism but no distinct independent audit mandate to review live organizational reality and cause an established S3 manager to alter current operations.



## S4 — Outside-and-then intelligence

- State: —
- Function: No first-party model-owned **future environment distinction → prospective changed strategy option → authorized durable adoption back into later operations** cycle is established by the shipped event-sourcing/replay/fork mechanisms.
- Disturbance / variety regulated: Future model/prompt/graph configuration hypotheses, possible failure recurrence and drift can be explored with forks; the choices of what to test and retain remain application/developer-owned.
- Decisive decision or feedback right: `Runtime.fork` creates a branch from recorded history, `diff` compares structural outcomes, and replay cache preserves event/model responses. The caller determines alternative behaviors/policies and whether/how to deploy them; no packaged model evaluates environmental future shifts and autonomously updates durable operating capabilities.
- Decision owner: Outside experimenter/developer for prospective configuration; deterministic runtime for producing comparable fork traces.
- Supporting / enforcement mechanisms: Replay cache, fork IDs, Diff computation, consistent event roots, saved packs/behaviors and optional user-supplied configuration.
- Closure path: Operator forks run → changes input configuration → replay and diff → operator interprets result; no internal model-generated prospective strategy with authorized adoption into next live baseline operating mode.
- Why this is / is not agent-owned: A future developer can use the instrumentation for an S4 experiment, but removing any supposed strategic model does not disable graph replay, fork or diff; no model-owned future option-generation-and-adoption path is first-party evidenced.
- Evidence: [activegraph/runtime/runtime.py#L3393](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/runtime/runtime.py#L3393), [activegraph/runtime/runtime.py#L3583](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/runtime/runtime.py#L3583), [activegraph/runtime/diff.py#L79](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/runtime/diff.py#L79), [activegraph/llm/cache.py#L1](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/llm/cache.py#L1), [README.md#L42](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/README.md#L42).
- Basis: Bounded negative even though deterministic experimentation infrastructure is strong.
- Confidence: Medium-high at the declared generic runtime boundary.
- Caveats: A user-created LLM behavior might intentionally analyze trends and update a future skill; that is application-specific S4, not shipped default first-party ownership.

### Absence scope

- Surfaces inspected: Run fork/diff, strict/permissive replay, provider/cache, LLM behaviors, saved packs and built-in Diligence quickstart.
- Plausible first-party paths checked: Future-scenario evaluation, changed behavior/pack design, durable model-generated strategy choice and subsequent operating-version adoption.
- Why no material first-party path remains: The first-party mechanisms replay and compare caller-directed runs but do not integrate a model-driven prospective strategy selection with adopted changes to future operational capabilities within any demonstrated packaged mode.



## S5 — Policy and identity

- State: —
- Function: No first-party legitimate ultimate identity/purpose authority deciding constitutional conflicts with a lasting policy return is evidenced.
- Disturbance / variety regulated: Tool capabilities, graph mutation scope, replay security, sandbox access and human approvals bound model behavior but do not define organization-level identity decisions.
- Decisive decision or feedback right: `Policy`/frame ceilings and `evaluate_action_authority` enforce user-supplied permissions; explicit operator approval can control capabilities, but no internally accountable actor deliberates and sets final purpose for a viable organization.
- Decision owner: External developer/operator supplies governance intent; first-party deterministic permission/approval enforcement.
- Supporting / enforcement mechanisms: AuthorityDecision, capability ceilings and policy configuration, patch validation, approval events, sandbox and budget locks.
- Closure path: Tool/patch request → predetermined policy or outside approval → action allowed/denied; no identity-question escalation to legitimate S5 and durable return of constitutional policy.
- Why this is / is not agent-owned: The string `Policy` describes an enforceable rule set, not organizational legitimacy or the right to decide ultimate purpose.
- Evidence: [activegraph/policy.py#L1](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/policy.py#L1), [activegraph/runtime/authority.py#L55](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/runtime/authority.py#L55), [activegraph/runtime/authority.py#L103](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/runtime/authority.py#L103), [activegraph/frame.py#L1](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/activegraph/frame.py#L1), [README.md#L150](https://github.com/yoheinakajima/activegraph/blob/50d8405923b79e4e823a73a3045bb969436a872c/README.md#L150).
- Basis: Bounded negative after first-party frame/authority and human approval modes.
- Confidence: Medium-high.
- Caveats: The human/application owning a higher-level organization may exercise S5 externally; not claimed inside this runtime.

### Absence scope

- Surfaces inspected: Policy and frame capability ceilings, authority evaluator, approval events, tool registry and graph mutation limits.
- Plausible first-party paths checked: Organizational constitutional purpose conflict, delegated ultimate decision rights, lasting policy revision for following tasks.
- Why no material first-party path remains: Only externally configured permissions and action-by-action enforcement are shown; no first-party legitimate identity authority and binding returned long-term policy transaction is evidenced.



## Recursion

The credited autonomous S1 is optional first-party configured model-backed behavior interacting with graph world and tools. Other behaviors may be deterministic, recorded fixtures or user-designed agents; relation behaviors are not automatically an enduring coordination system among viable business S1 divisions. S2–S5 require additional function-specific ownership and closure evidence, not inferred from the expressiveness of a programming framework.

## Variety and escalation

Typed graph views, event/pattern subscriptions, model/tool turns, accepted patches and deterministic guards attenuate immediate operating variety. Queue overflow/budget exhaustion, tool failures, replay divergence and approvals produce operational events for operator review; no tested automatic high-priority escalation to distinct S3/S4/S5 governance is asserted.

## Evidence gaps

- Actual source checkout offline smoke: `PYTHONPATH=. python3 -m activegraph quickstart` finished successfully with first-party bundled Diligence pack and recorded fixtures, printing deterministic event/trace and SQLite inspection route; `Graph`, `Runtime`, `RecordedLLMProvider` import passed. This does **not** establish genuine hosted LLM inference success or empirical task effectiveness.
- External optional `openai` and `anthropic` provider SDKs were missing from the isolated environment, so no live provider call was run. `pytest` was also absent, thus no upstream full test suite outcome is claimed; this is an environment limit, not proof of a runtime defect.
- First-party generic orchestration abstractions could host application-specific S2–S5 designs; no general claim of impossibility, but no default packaged owner/return at the assessed recursion is demonstrated.
- This artifact is `proposed`; canonical catalog/signature/rankings await distinct CI-gated admission.

---
harness_id: nemo-relay
project_name: NeMo Relay
repository: https://github.com/NVIDIA/NeMo-Relay
review_ref: e65fbbf5455014430feeaf5f25090af979df4779
reviewed_at: 2026-11-20
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# NeMo Relay

## Review boundary

- System in focus: The first-party NVIDIA NeMo Relay instrumentation, middleware, managed-call, plugin, observability, CLI/daemon, and optional adaptive runtime in its published Rust/Python/Node distributions; **not** a hypothetical assembled end-user agent application using an external coding agent or orchestration framework.
- Purpose and identity: Attach to existing agent stacks and framework-owned LLM/tool call sites, produce coherent scoped event streams, enforce configured policies, and improve the latency/cost of already-authorized calls without replacing the agent or its model/tool decision loop.
- Relevant environment: Developer-managed applications, existing autonomous agent processes, incoming tool/model requests, provider responses, telemetry/exporter destinations, configured plugin policies, tenant and credential boundaries, host infrastructure, and changing request/cost/latency measurements.
- Standard-distribution boundary: Rust runtime and SDK, Python/Node bridges, supported CLI adapter/gateway and daemon entrypoints, first-party plugin host, built-in guardrails/observability/PII redaction, opt-in `nemo-relay-adaptive` learners, cache and hint injection. The agent framework/LLM's model-directed task loop, mission definition, actor identity, autonomous task choice, tool authoring, code execution, human owner and external observability products are **not** supplied as first-party operational owners.
- Credited operating / distribution surfaces: `crates/runtime/src/api/{llm,tool,execution,scope}.rs`, `crates/sdk/src/lib.rs`, plugin registration and host, CLI adapters for Claude/Codex, scoped managed execution, lifecycle events, and `crates/adaptive` optional adaptive learners.
- Adjacent first-party surfaces excluded from ownership: `.github` developer CI, synthetic runtime tests and example SDK clients; proprietary/external Claude Code, Codex, OpenClaw, Hermes Agent, LangChain, Google ADK and their actual agent decisions; configured custom plugins or administrator policy beyond the bundled semantics; Arize Phoenix, LangSmith and other trace consumers; external model pricing or independent application review boards.
- First-party operating/deployment modes considered: Rust SDK managed `llm_call_execute` / `tool_call_execute`; Python and Node integrations; CLI instrumented existing coding agents by hook or gateway; shared service/daemon; opt-in adaptive cache/parallel hints and middleware policy. `manual` lifecycle reporting mode is observation only; managed mode owns invocation and wrapping **but not the agent's objective/next-tool choice**.
- Recursion level: One configured Relay instrumentation/policy envelope wrapped around externally supplied agent work, rather than treating the external agent as an internal first-party S1 cell by association.
- Reviewed revision: `e65fbbf5455014430feeaf5f25090af979df4779` (original GitHub ID `1197824527`, Apache-2.0, public nonfork; creation `2026-03-31T23:22:24Z`).
- Observation date: 2026-11-20.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

NeMo Relay is an SDK- and integration-oriented **middleware**, not a general AI agent executor or task orchestrator. Its Rust runtime allocates parent-child scope handles for agent/turn/LLM/tool events, runs registered request and execution interceptors around caller-provided functions, checks deterministic conditional guardrails, and publishes sanitized lifecycle events to exporters. Maintained bindings/CLI intercept supported frameworks' own action decisions. A plugin host handles trust, loading, configuration, activation and teardown, and built-in plugins report prices, resource use, PII findings and traces. Its adaptive package retrospectively learns provider/prompt cache stability and observed tool-call overlap, persisting deterministic hints for subsequent calls. None of the inspected standard mode surfaces adds a first-party model-driven goal evaluator or new task-action selection loop.

The README is explicit that Relay **wraps agents' model/tool calls**, does not replace the agent framework, and says the agent or framework is the source of request decisions. An owned `ToolExecutionNextFn` or `LlmExecutionNextFn` is a **callback supplied by that enclosing app**, not a model/reasoner which chooses the task itself. The SDK exports `llm_call_execute` and `tool_call_execute` to intercept call sites and the CLI routes supported external vendor traffic. Hook-only integrations emit lifecycle notifications without executing or rewriting the underlying call. Source: [README.md](https://github.com/NVIDIA/NeMo-Relay/blob/e65fbbf5455014430feeaf5f25090af979df4779/README.md); [crates/runtime/README.md](https://github.com/NVIDIA/NeMo-Relay/blob/e65fbbf5455014430feeaf5f25090af979df4779/crates/runtime/README.md); [crates/runtime/src/api/tool.rs](https://github.com/NVIDIA/NeMo-Relay/blob/e65fbbf5455014430feeaf5f25090af979df4779/crates/runtime/src/api/tool.rs); [crates/runtime/src/api/llm.rs](https://github.com/NVIDIA/NeMo-Relay/blob/e65fbbf5455014430feeaf5f25090af979df4779/crates/runtime/src/api/llm.rs); [crates/sdk/src/lib.rs](https://github.com/NVIDIA/NeMo-Relay/blob/e65fbbf5455014430feeaf5f25090af979df4779/crates/sdk/src/lib.rs); [crates/plugin-host/README.md](https://github.com/NVIDIA/NeMo-Relay/blob/e65fbbf5455014430feeaf5f25090af979df4779/crates/plugin-host/README.md).

The adaptive plugin is substantial but scoped: `ToolParallelismLearner` derives observed cohorts of overlapping **already chosen** calls, updating a `ParallelHint` plan; `AcgLearner` groups previously observed model requests by prompt profile and finds stable prefixes for cache optimization. These optimize how existing agent calls are handled, not who selects organizational purpose, worker commitments, new tasks or future capabilities. Source: [crates/adaptive/README.md](https://github.com/NVIDIA/NeMo-Relay/blob/e65fbbf5455014430feeaf5f25090af979df4779/crates/adaptive/README.md); [crates/adaptive/src/tool_parallelism_learner.rs](https://github.com/NVIDIA/NeMo-Relay/blob/e65fbbf5455014430feeaf5f25090af979df4779/crates/adaptive/src/tool_parallelism_learner.rs); [crates/adaptive/src/acg_learner.rs](https://github.com/NVIDIA/NeMo-Relay/blob/e65fbbf5455014430feeaf5f25090af979df4779/crates/adaptive/src/acg_learner.rs); [docs/configure-plugins/adaptive/about.mdx](https://github.com/NVIDIA/NeMo-Relay/blob/e65fbbf5455014430feeaf5f25090af979df4779/docs/configure-plugins/adaptive/about.mdx).

## Operational model

An external agent chooses an LLM or tool call. If its host integration selects Relay's managed mode, the first-party middleware can admit/deny, rewrite or wrap that **specified call** according to operator/plugin-selected rules and invoke the supplied original callback, then emit lifecycle events. The decision whether a different tool, task, objective or final answer should be chosen after that result stays in the external agent loop, not in Relay. Traces, cache hits, hint plans and guardrail events can influence a client that actively consumes them; Relay itself does not establish an autonomous organizational conversation among agent S1 cells.

**Counterfactual owner test:** Remove Claude/Codex/Hermes/OpenClaw/LangChain/ADK and any application-authored agent/tool chooser while retaining all published Relay crates, CLI and plugins. The remaining system can collect, sanitize, route or reject caller-originated request envelopes, calculate prices and apply performance hints. It has no first-party AI agent that independently interprets a task, chooses and revises substantive tools from feedback or produces user-task outcomes. Therefore **the qualifying autonomous S1 system is absent at the frozen first-party boundary**. The suitable canonical decision is `excluded-no-agentic-vsm`, not a forced `S1=C` based on a generic managed-call callback. This exclusion does not negate the middleware's operational usefulness or its substantial call-level controls.

## S1 — Operations

- State: —
- Function: No first-party autonomous operational unit transforming a user goal through its own model-guided task/action loop is established; Relay instruments **an external operational agent**.
- Disturbance / variety regulated: Model/tool request timing, errors, PII, provider behavior and telemetry are processed by configured middleware; goal interpretation and novel action choice remain external.
- Decisive decision or feedback right: The agent or application supplies `ToolExecutionNextFn`, `LlmExecutionNextFn` and caller-selected request name, arguments, model and operation; Relay may invoke or modify those preselected calls but does not generate the next agent action after observation.
- Decision owner: External task model/agent and its application/integration; first-party Rust runtime owns deterministic execution stages and event closure, not autonomous organizational task discretion.
- Supporting / enforcement mechanisms: Scoped handles, request/execution interceptors, guardrails, plugin config, trace exporters, call lifecycle record and adaptive hints.
- Closure path: External agent selects call → Relay intercepts/enforces or forwards → result returns to **external** agent → external agent may choose the next operation. Relay-owned closure is only the middleware call, not an autonomous task feedback loop.
- Boundary reachability: No first-party model-driven tool/goal loop is exposed in a supported default or opt-in released operating mode; SDK APIs expose call wrappers, not agent-loop orchestration.
- Why this is / is not agent-owned: Removing external agent decisions leaves call wrappers without task instructions or a model deciding tools; labels such as `agent`, `turn` and `subagent` are tracing scopes, not internally created decision actors.
- Evidence: [README.md](https://github.com/NVIDIA/NeMo-Relay/blob/e65fbbf5455014430feeaf5f25090af979df4779/README.md); [crates/sdk/src/lib.rs](https://github.com/NVIDIA/NeMo-Relay/blob/e65fbbf5455014430feeaf5f25090af979df4779/crates/sdk/src/lib.rs); [crates/runtime/src/api/execution.rs](https://github.com/NVIDIA/NeMo-Relay/blob/e65fbbf5455014430feeaf5f25090af979df4779/crates/runtime/src/api/execution.rs); [crates/runtime/src/api/tool.rs](https://github.com/NVIDIA/NeMo-Relay/blob/e65fbbf5455014430feeaf5f25090af979df4779/crates/runtime/src/api/tool.rs); [crates/runtime/src/api/llm.rs](https://github.com/NVIDIA/NeMo-Relay/blob/e65fbbf5455014430feeaf5f25090af979df4779/crates/runtime/src/api/llm.rs).
- Basis: explicit and structural
- Confidence: high
- Caveats: A concrete application assembled with Relay plus a model-driven framework may have autonomous S1, but this assessment cannot borrow it into the first-party Relay boundary.

### Absence scope

- Surfaces inspected: Root README and how-it-works diagrams, Rust SDK/public exports, runtime execution/tool/LLM/registry code, CLI integrations for external agents and SDK/host plugin documentation.
- Plausible first-party paths checked: Instrumented `agent` scopes, managed tool/LLM callbacks, gateway-routed provider calls, CLI wrappers for coding agents and optional adaptive hints/optimization.
- Why no material first-party path remains: Each needs an upstream model/tool chooser or external agent runtime, and none supplies an internally owned task-level autonomous decision-feedback loop. This is not a task-agent constructor tailored to a specific operational decision; it is provider-neutral call middleware.

## S2 — Coordination

- State: —
- Function: No first-party coordination relation among autonomous S1 operational units is established at the declared recursion.
- Disturbance / variety regulated: Parallel tool-call races, plugin ordering, shared trace context and output delivery consistency may exist, but they are middleware/infrastructure disturbances, not evidenced conflicts of independent S1 decisions.
- Decisive decision or feedback right: Plugin-order and scope middleware apply application-configured rules; `ToolParallelismLearner` records previously co-executed calls and emits hints but does not arbitrate competing agent commitments.
- Decision owner: Application and configured agent orchestration; deterministic Relay plugin host enforces hook ordering and hints.
- Supporting / enforcement mechanisms: Context propagation, scope isolation, subscriber dispatch, adaptive parallelism hint cache and shared storage.
- Closure path: Concurrent tool observations may change a hint for later model requests, not a first-party decision that attenuates specific inter-S1 interference and alters S1 agents' subsequent behavior.
- Boundary reachability: Scope and adaptive components are shipped but are not themselves positive S2.
- Why this is / is not agent-owned: Tracking multiple `subagent` or tool spans is not itself coordinating their autonomous work; time-overlap hints do not resolve conflicts over a shared objective or resource.
- Distinct S1 units: External agents may be many, but no first-party autonomously deciding S1 cells are constructed or governed by Relay.
- Inter-S1 disturbance: No specific first-party agent-to-agent conflict tied to an attenuation mechanism.
- Attenuating coordination relation: Middleware execution/trace isolation, not a function-specific anti-oscillation conversation between agent units.
- Feedback into subsequent S1 behaviour: No first-party cross-agent coordination decision returned to their next autonomous choices; optional hints merely modify timing metadata of existing calls.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: A shared event stream or parallelism hint is generic transport/optimization, without a source-verified interference/coordination witness.
- Evidence: [crates/adaptive/src/tool_parallelism_learner.rs](https://github.com/NVIDIA/NeMo-Relay/blob/e65fbbf5455014430feeaf5f25090af979df4779/crates/adaptive/src/tool_parallelism_learner.rs); [crates/runtime/src/api/runtime.rs](https://github.com/NVIDIA/NeMo-Relay/blob/e65fbbf5455014430feeaf5f25090af979df4779/crates/runtime/src/api/runtime.rs); [crates/runtime/src/api/tool.rs](https://github.com/NVIDIA/NeMo-Relay/blob/e65fbbf5455014430feeaf5f25090af979df4779/crates/runtime/src/api/tool.rs); [README.md](https://github.com/NVIDIA/NeMo-Relay/blob/e65fbbf5455014430feeaf5f25090af979df4779/README.md).
- Basis: structural
- Confidence: high at declared boundary
- Caveats: A downstream system could use traces to build S2, but the independently deciding agent actors and their coordination decisions remain external.

### Absence scope

- Surfaces inspected: Runtime scopes, subscriber dispatch, adaptive tool-overlap learner, CLI integration boundaries and plugin registry.
- Plausible first-party paths checked: Hierarchical `subagent` tracing, parallel tool-execution plans, shared context propagation and conditional middleware.
- Why no material first-party path remains: Neither autonomous S1 cells nor S2-specific cross-cell interference attenuation/feedback is implemented; scheduling and tracing are not enough.

## S3 — Inside-and-now control

- State: —
- Function: No first-party whole-system current control over substantive autonomous agent-unit commitments, priorities and resources is established.
- Disturbance / variety regulated: Per-call latency, cost, cache performance, sensitive data and tool/provider errors are regulated by hooks, budgets, pricing and middleware configuration.
- Decisive decision or feedback right: Operator or embedding application selects which policy and optimization plugin to activate; cached hints/guardrails implement preselected deterministic conditions around an existing request.
- Decision owner: External application/administrator; first-party middleware applies configured constraints and learned request optimizations.
- Supporting / enforcement mechanisms: Plugin host, pricing catalog, cache governor, tool concurrency hints, conditional execution and request interception.
- Closure path: Observed call history → updated runtime hint/cache entry → subsequent caller-preselected call may execute more efficiently or fail a policy. No organization-wide goal/commitment deliberation and resource reallocation across S1 units is sourced.
- Boundary reachability: Adaptive and middleware plugins are first-party and can run when enabled, but their authority remains call-bound rather than a qualifying S3 executive.
- Why this is / is not agent-owned: Learners infer prompt stability and overlap via deterministic retrospective algorithms; they do not decide task priority, rewrite agent mandates, bargain competing operations or revise whole-organization commitments.
- Whole-system current view: Captured call/trace metrics and enabled plugin configuration, not an agent fleet's current commitments or actionable operational priorities.
- Current-control decision scope: Admission/rewrite of a specific given LLM/tool call and local cost/latency optimization, not whole-system current organizational control.
- Evidence: [crates/adaptive/src/acg_learner.rs](https://github.com/NVIDIA/NeMo-Relay/blob/e65fbbf5455014430feeaf5f25090af979df4779/crates/adaptive/src/acg_learner.rs); [crates/adaptive/src/tool_parallelism_learner.rs](https://github.com/NVIDIA/NeMo-Relay/blob/e65fbbf5455014430feeaf5f25090af979df4779/crates/adaptive/src/tool_parallelism_learner.rs); [crates/adaptive/README.md](https://github.com/NVIDIA/NeMo-Relay/blob/e65fbbf5455014430feeaf5f25090af979df4779/crates/adaptive/README.md); [crates/runtime/src/api/execution.rs](https://github.com/NVIDIA/NeMo-Relay/blob/e65fbbf5455014430feeaf5f25090af979df4779/crates/runtime/src/api/execution.rs); [crates/plugin-host/README.md](https://github.com/NVIDIA/NeMo-Relay/blob/e65fbbf5455014430feeaf5f25090af979df4779/crates/plugin-host/README.md).
- Basis: explicit and structural
- Confidence: high
- Caveats: Operational guardrails can be materially strong. This negative classification is about organizational ownership/closure, not lack of practical runtime safety mechanisms.

### Absence scope

- Surfaces inspected: Managed-call middleware, plugin config, adaptive telemetry, cache and parallelism learner, pricing, daemon/shared-service entrypoints.
- Plausible first-party paths checked: Cost-aware call routing, runtime optimizer feedback, guardrail policy, shared administrator configuration and plugin activation.
- Why no material first-party path remains: The observed mechanisms implement already-given limits or optimize caller-supplied calls, without deciding across whole current autonomous S1 operations.

## S3* — Complementary audit

- State: —
- Function: No first-party independent operational auditor tests the agent's ordinary substantive result claims and closes findings into agent governance.
- Disturbance / variety regulated: Trace incompleteness or unsafe tool/model inputs can be detected by logs and sanitizers, but these are measurement/security issues rather than independent examination of agent completion truth.
- Decisive decision or feedback right: Exporters and subscribers publish source-level events; a separate evaluator, independent reviewer or dashboard consumer would have to decide whether an agent's outcome claim is false and direct correction.
- Decision owner: External review/observability applications and their operators; relay-owned event producers do not supply independent audit judgment.
- Supporting / enforcement mechanisms: ATOF/ATIF event formats, OpenTelemetry, OpenInference, trace scopes, PII sanitizers, diagnostic evidence, plugin callbacks.
- Closure path: Agent/runtime events → Relay sanitized trace stream → optional external consumer. No shipped independent falsification decision and corrective return into the agent's subsequent operation is demonstrated.
- Boundary reachability: Exporters are shipped and reachable, but a distinct audit reviewer/feedback authority is not part of the standard Relay boundary.
- Why this is / is not agent-owned: Raw trace is potentially useful for external audit, but a log by itself is not S3*, nor does deterministic redaction authorize an audit correction.
- Claim being audited: External agent's asserted completion, correctness and suitability of produced outcomes.
- Ordinary reporting path: External agent output plus its model/tool event stream.
- Complementary access path: Relay's structured trace includes first-party observed call events, but no independent claim-testing actor or separate adjudication channel.
- Independence boundary: Trace production can bypass agent-produced prose but lacks independent substantive judgment and return path; third-party dashboards/evals remain external.
- Who acts on findings: Human/external evaluator must be configured; none shipped in the assessed run mode.
- Evidence: [README.md](https://github.com/NVIDIA/NeMo-Relay/blob/e65fbbf5455014430feeaf5f25090af979df4779/README.md); [crates/runtime/src/api/event.rs](https://github.com/NVIDIA/NeMo-Relay/blob/e65fbbf5455014430feeaf5f25090af979df4779/crates/runtime/src/api/event.rs); [crates/runtime/src/api/subscriber.rs](https://github.com/NVIDIA/NeMo-Relay/blob/e65fbbf5455014430feeaf5f25090af979df4779/crates/runtime/src/api/subscriber.rs); [crates/plugin-host/README.md](https://github.com/NVIDIA/NeMo-Relay/blob/e65fbbf5455014430feeaf5f25090af979df4779/crates/plugin-host/README.md).
- Basis: structural
- Confidence: medium-high
- Caveats: A future or downstream independent evaluator could exploit Relay as an S3* evidence transport. That constructor is not claimed as a first-party independent audit decision loop.

### Absence scope

- Surfaces inspected: Runtime lifecycle event/subscriber/diagnostic APIs, ATOF/ATIF exporters, built-in PII guardrails and plugin host.
- Plausible first-party paths checked: Trace-based verification, independent exporter consumption, replay formats, sanitizer checks and system diagnostics.
- Why no material first-party path remains: First-party components capture/transport/format evidence but do not own independent audit judgments with closed organizational corrective feedback.

## S4 — Outside-and-then intelligence

- State: —
- Function: No first-party agent-led sensing of future external conditions and prospective capability-option selection returned to current organization control was established.
- Disturbance / variety regulated: External provider price/capability changes, future tool risk and strategic application requirements would need prospective intelligence beyond current measured performance.
- Decisive decision or feedback right: Adaptive plugins learn retrospective request/cache regularities; host or external agent operators decide model choice, policies, releases and future adaptation strategy.
- Decision owner: Embedding application/operator; no first-party adaptive strategy-deciding actor or S3/S4 strategic conversation in the published middleware.
- Supporting / enforcement mechanisms: Model pricing estimates, observed latency traces, adaptive request hints, caches, plugin configurations and optional external policy implementations.
- Closure path: Past call observations → deterministic performance hints/cache settings → later call optimization. This is inside-and-now request tuning, not external prospective options → S3/S4 dialogue → selected future capability change.
- Boundary reachability: First-party `adaptive` plugin is shipped and configurable, but its learned states concern prompt stability, token reuse, hints and tool timing, not organizational future adaptation.
- Why this is / is not agent-owned: A retrospective optimization learner named `adaptive` does not establish externally prospective VSM S4.
- Evidence: [crates/adaptive/src/acg_learner.rs](https://github.com/NVIDIA/NeMo-Relay/blob/e65fbbf5455014430feeaf5f25090af979df4779/crates/adaptive/src/acg_learner.rs); [crates/adaptive/src/tool_parallelism_learner.rs](https://github.com/NVIDIA/NeMo-Relay/blob/e65fbbf5455014430feeaf5f25090af979df4779/crates/adaptive/src/tool_parallelism_learner.rs); [docs/configure-plugins/adaptive/about.mdx](https://github.com/NVIDIA/NeMo-Relay/blob/e65fbbf5455014430feeaf5f25090af979df4779/docs/configure-plugins/adaptive/about.mdx); [README.md](https://github.com/NVIDIA/NeMo-Relay/blob/e65fbbf5455014430feeaf5f25090af979df4779/README.md).
- Basis: explicit/structural
- Confidence: high at task system boundary
- Caveats: A downstream harness may use Relay measurements to choose a new model or policy strategically. That would require independently examining its owner, evidence and return path.

### Absence scope

- Surfaces inspected: Adaptive learner/ACG implementation, observed-tool parallelism, pricing, configured plugin model and hosted/CLI integrations.
- Plausible first-party paths checked: Cache policy learning, automatic performance hints, model-cost monitoring and provider changes.
- Why no material first-party path remains: The observed adaptation operates on current or historical call patterns without prospectively modelling outside environment or selecting organizational capability investments.

## S5 — Policy and identity

- State: —
- Function: No first-party ultimate identity/policy conflict decision and authoritative return path exists for the autonomous organization, which is outside the SDK boundary.
- Disturbance / variety regulated: Data privacy, tool safety, credential access and plugin trust require configured policy, but organizational purpose/identity tradeoffs remain in application or operator.
- Decisive decision or feedback right: Administrator/application authors select plugin manifests and policies; Relay's registry enforces allow/deny, sanitization and verification on their chosen requests.
- Decision owner: External operator or host application, not a model-owned or first-party identity-governance body.
- Supporting / enforcement mechanisms: Guardrails, plugin validation, scope namespace, trust verification, redaction and runtime policy.
- Closure path: Configured policy → deterministic gating of caller-selected future calls; absent a separate identity-level issue → legitimate ultimate decision → returned policy revision → governed subsequent operation.
- Boundary reachability: Policy/guardrail enforcement is first-party, but no S5-specific parent mode is operationally closed at the assessed recursion.
- Why this is / is not agent-owned: Strict rule enforcement is not itself authority to define organizational identity; static config changes and ordinary call approvals do not establish S5.
- Identity / ultimate-policy issue: What purpose a deployed agent organization should pursue and who can legitimately resolve changes to its fundamental mandates.
- Ultimate authority in each claimed mode: External operator/host not wired as a legitimate S5 dispute-and-return mechanism in the Relay middleware.
- Return-to-operation path: Policy settings can govern calls, but no documented identity-level adjudication/feedback loop changes the underlying agent organization's mission.
- Evidence: [crates/plugin-host/README.md](https://github.com/NVIDIA/NeMo-Relay/blob/e65fbbf5455014430feeaf5f25090af979df4779/crates/plugin-host/README.md); [crates/runtime/src/api/registry.rs](https://github.com/NVIDIA/NeMo-Relay/blob/e65fbbf5455014430feeaf5f25090af979df4779/crates/runtime/src/api/registry.rs); [crates/sdk/src/lib.rs](https://github.com/NVIDIA/NeMo-Relay/blob/e65fbbf5455014430feeaf5f25090af979df4779/crates/sdk/src/lib.rs); [README.md](https://github.com/NVIDIA/NeMo-Relay/blob/e65fbbf5455014430feeaf5f25090af979df4779/README.md).
- Basis: structural
- Confidence: high
- Caveats: An administrator can author strict policy constraints; this is a real security feature but not evidence of organizational S5 at the chosen recursion.

### Absence scope

- Surfaces inspected: Plugin trust/registry/activation, request guardrails, scope policy, CLI gateway and shared-service configuration.
- Plausible first-party paths checked: Administrator policy edits, safety filtering, PII redaction, plugin approval/registration and runtime security decisions.
- Why no material first-party path remains: All govern or validate already-selected calls. There is no first-party channel for an ultimate mission/identity disagreement to reach and return from legitimate final authority.

## Distributed OSS parent arrangement

NVIDIA maintainers and contributors may govern the middleware project, but that GitHub source/release process is a different organization from an autonomous agent application's running S1 cells. No organization-level parent S3/S4/S5 credit is imported from repository reviews or release controls.

## Self-hosted and non-human modes

The daemon can serve multiple users or coding agents under administrator-managed configuration. That is an instrumental middleware service, not proof of a central executive controlling independently owned agent task commitments. In a non-human downstream agent system, actual model task and policy decisions remain to be established in the downstream system, not assigned to Relay.

## Recursion

An agent scope, subagent span, thread and tool call form a trace hierarchy. They are not by themselves recursive viable organizations; the observed decision-making agent cells are external to Relay. No first-party internally owned agent recursion is asserted.

## Variety and escalation

Relay reduces representation loss by emitting structured, correlated trace events and offers request sanitizers/guardrails, cache hints and local diagnostics. Those mechanisms can attenuate latency, policy and telemetry disturbances, but distinguishing task/user variety and resolving organizational decisions still requires an external agent/owner. Middleware rejection or performance hint is not a separate VSM governance function.

## Evidence gaps

- Source-first architectural review only; no hosted agent/provider execution, gateway run, independently tasked audit, or production plugin deployment was performed.
- `C` was considered for S1 because first-party managed-call callbacks are concrete, but rejected at the frozen boundary: Relay cannot independently originate an autonomous operational decision or substantively change the external agent's next task/action without a separately supplied agent loop.
- The scoped trace/event stream is useful evidence for a downstream S3* mechanism but cannot, by itself, provide an independent audit judgment and organizational return path.
- Adaptive plugin conclusions are bounded to retrospective call-level optimization, not a claim that no downstream agent could use the signals for future strategy.
- **Recommended terminal Index lifecycle:** `excluded-no-agentic-vsm`, preserving this full assessment as the evidence and catalog entry without assigning a false positive S1.

---
harness_id: local-agent-broker
project_name: Local Agent Broker
repository: https://github.com/BlackJaxDev/local-agent-broker
review_ref: 86b09380e3393126d6c540787a7576a61d21565b
reviewed_at: 2026-11-05
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Local Agent Broker

## Review boundary

- System in focus: One self-hosted .NET MCP stdio broker mediating bounded, exact-model API workers, including its optional first-party code-swarm mode; not the invoking MCP host, API providers, or the developer's organization.
- Purpose and identity: Execute explicitly authorized local worker objectives with controlled model selection, tools, repository/editor access, budgets, run history, and optional separately reviewed code-change proposals.
- Relevant environment: User task and success criteria, OpenAI/Anthropic responses and failures, authorized repository snapshots, tool observations, editor sessions, concurrency, latency/cost limits, and proposed file edits.
- Standard-distribution boundary: Shipped `LocalAgentBroker` MCP server, `LocalAgentBroker.Orchestration` provider/tool loop, supported `AgentSwarmRunner` hierarchy, run registry and opt-in safe application path. A caller must configure a workspace and provider credentials; no provider request was executed in this review.
- Credited operating / distribution surfaces: [MCP host](https://github.com/BlackJaxDev/local-agent-broker/blob/86b09380e3393126d6c540787a7576a61d21565b/src/LocalAgentBroker/McpStdioServer.cs), [run registry](https://github.com/BlackJaxDev/local-agent-broker/blob/86b09380e3393126d6c540787a7576a61d21565b/src/LocalAgentBroker/AgentRunRegistry.cs), [agent loop](https://github.com/BlackJaxDev/local-agent-broker/blob/86b09380e3393126d6c540787a7576a61d21565b/src/LocalAgentBroker.Orchestration/AgentOrchestrator.cs), [swarm execution](https://github.com/BlackJaxDev/local-agent-broker/blob/86b09380e3393126d6c540787a7576a61d21565b/src/LocalAgentBroker/AgentSwarmRunner.Execution.cs), [swarm review prompts](https://github.com/BlackJaxDev/local-agent-broker/blob/86b09380e3393126d6c540787a7576a61d21565b/src/LocalAgentBroker/AgentSwarmRunner.Planning.cs), and [host apply path](https://github.com/BlackJaxDev/local-agent-broker/blob/86b09380e3393126d6c540787a7576a61d21565b/src/LocalAgentBroker/AgentRunRegistry.Swarms.cs).
- Adjacent first-party surfaces excluded from ownership: Windows tray/history viewer and settings UI, build/publish/CI scripts, unit tests, provider SDK/model internals, caller/host-agent governance, and optional editor process internals. Tests can corroborate wiring, not supply a runtime S-function on their own.
- First-party operating / deployment modes considered: Default independent worker with opt-in immutable context files and read-only repository tools; explicitly allowed editor tools; optional multi-phase code swarm with source snapshots, model-created leaf edits, separate model review, and default proposal-only or Windows-only `auto_apply`.
- Recursion level: Single local broker run and its optional bounded child work-unit group; no independently viable nested enterprise is assumed.
- Reviewed revision: `BlackJaxDev/local-agent-broker@86b09380e3393126d6c540787a7576a61d21565b` (MIT).
- Observation date: 2026-11-05.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

The broker exposes five MCP tools through a newline-delimited stdio server: model route recommendation, start, get, cancel and list. `AgentRunRegistry` freezes authorized context-file snapshots, checks exact requested model and credentials, creates runs and delegates work to `AgentOrchestrator`. The model receives objectives, evidence and bounded tools, chooses calls, observes returned tool results and continues until completion or budget failure. Tool access is opt-in; built-in repository tools are read-only, while a named loopback editor session and explicit allowlists are needed for mutation. Model mismatch, exhausted budgets and other errors remain failures rather than silent substitutions. [Protocol](https://github.com/BlackJaxDev/local-agent-broker/blob/86b09380e3393126d6c540787a7576a61d21565b/docs/protocol.md), [loop](https://github.com/BlackJaxDev/local-agent-broker/blob/86b09380e3393126d6c540787a7576a61d21565b/src/LocalAgentBroker.Orchestration/AgentOrchestrator.cs), [registry](https://github.com/BlackJaxDev/local-agent-broker/blob/86b09380e3393126d6c540787a7576a61d21565b/src/LocalAgentBroker/AgentRunRegistry.cs).

Optional swarm execution asks a root model for an explicit hierarchy of file-scoped children; leaves propose replacements against immutable pre-run source snapshots. The broker runs sibling model phases concurrently within limits, rejects overlapping edits, and starts a *new* model request for each parent review of unchanged child artifacts plus the broker-captured source snapshots. A negative parent judgment rejects the whole proposal; the returned changes can be externally reviewed or explicitly applied on Windows with a readback. This is review of *proposed* edits before application, not post-deployment verification. [Swarm execution](https://github.com/BlackJaxDev/local-agent-broker/blob/86b09380e3393126d6c540787a7576a61d21565b/src/LocalAgentBroker/AgentSwarmRunner.Execution.cs), [phase requests](https://github.com/BlackJaxDev/local-agent-broker/blob/86b09380e3393126d6c540787a7576a61d21565b/src/LocalAgentBroker/AgentSwarmRunner.Planning.cs), [change merger](https://github.com/BlackJaxDev/local-agent-broker/blob/86b09380e3393126d6c540787a7576a61d21565b/src/LocalAgentBroker.Orchestration/AgentSwarmChangeMerger.cs).

## Operational model

A provider model makes the task-level content/tool decisions; the broker owns deterministic limits, access and lifecycle plumbing. In swarm mode different model calls enact planning, leaf code creation and parent review. The caller chooses objective, model, path scope, budgets and whether writes are allowed. A root planning model decides a bounded child decomposition but does not own an ongoing whole-portfolio current-control mandate. A parent review model has a separate view of code artifacts against broker-supplied immutable source rather than accepting a leaf's approval claim.

## S1 — Operations

- State: A
- Function: Model-controlled workers transform bounded objectives into answers, tool-mediated effects, or code-change proposals.
- Disturbance / variety regulated: Uncertain objectives, changing tool results, failed or denied calls, and code-edit details in authorized source files.
- Decisive decision or feedback right: The provider model selects its response, tool calls and next steps within broker-enforced limits; swarm leaves choose concrete source replacements.
- Decision owner: External API model invoked as the active autonomous actor through the first-party broker loop; in swarm mode the per-phase root/leaf models choose plan and edits.
- Supporting / enforcement mechanisms: MCP transport, exact-model check, prompt construction, tool registry, immutable snapshots, budgets, provider retries, session policy and parallelism semaphores.
- Closure path: Caller starts a run → model chooses answer/tool action → broker executes allowed tool → result returns on the next model turn → completed answer; in swarm mode leaf proposals return through review and caller-controlled apply.
- Boundary reachability: `start_agent_run` invokes `AgentRunRegistry.Start` and `AgentOrchestrator.RunAsync`; optional swarm routes through `RunSwarmAsync`/`RunNodeAsync` in shipped production code, not a test-only agent.
- Why this is / is not agent-owned: The model decides task content/actions. Hard tool caps and file permissions only constrain or reject those decisions, rather than replacing their discretion.
- Evidence: [MCP tool implementation](https://github.com/BlackJaxDev/local-agent-broker/blob/86b09380e3393126d6c540787a7576a61d21565b/src/LocalAgentBroker/McpStdioServer.cs), [agent turn/tool feedback](https://github.com/BlackJaxDev/local-agent-broker/blob/86b09380e3393126d6c540787a7576a61d21565b/src/LocalAgentBroker.Orchestration/AgentOrchestrator.cs), [swarm leaves](https://github.com/BlackJaxDev/local-agent-broker/blob/86b09380e3393126d6c540787a7576a61d21565b/src/LocalAgentBroker/AgentSwarmRunner.Execution.cs).
- Basis: Structural first-party model-execution and feedback path.
- Confidence: High for code wiring; medium for real provider execution because no billed run was repeated here.
- Caveats: A standalone broker invocation still needs explicit provider credentials and client authorization; provider cognition is not itself first-party broker implementation.

## S2 — Coordination

- State: —
- Function: No established adaptive inter-S1 conflict/oscillation attenuation with returned behavioral adjustment in the shipped modes.
- Disturbance / variety regulated: Parallel child agents can propose overlapping edits to a shared source file; separately queued workers can contend for concurrency capacity.
- Decisive decision or feedback right: The caller fixes allowed paths and limits; deterministic merger rejects overlapping source edits rather than negotiating a revised peer coordination response.
- Decision owner: Caller for path allocations/limits; root model for initial task decomposition; runtime for conflict validation and static semaphore enforcement.
- Supporting / enforcement mechanisms: Per-child path assignment, immutable base hashes, overlap rejection, provider-slot and swarm-slot semaphores.
- Closure path: Parallel child edits → conflict checker either combines non-overlapping patches or fails the proposal; no installed conflict-resolution decision goes back into a new coordinated child round.
- Why this is / is not agent-owned: Distinct S1 leaves and a real possible edit collision are present, but a rejection gate and initial delegation are not an S2-specific feedback regulator changing subsequent inter-S1 behavior.
- Evidence: [plan constraints](https://github.com/BlackJaxDev/local-agent-broker/blob/86b09380e3393126d6c540787a7576a61d21565b/src/LocalAgentBroker/AgentSwarmRunner.Planning.cs), [overlap detection](https://github.com/BlackJaxDev/local-agent-broker/blob/86b09380e3393126d6c540787a7576a61d21565b/src/LocalAgentBroker.Orchestration/AgentSwarmChangeMerger.cs), [parallel execution](https://github.com/BlackJaxDev/local-agent-broker/blob/86b09380e3393126d6c540787a7576a61d21565b/src/LocalAgentBroker/AgentSwarmRunner.Execution.cs).
- Basis: Bounded negative functional assessment despite a structurally identifiable disturbance.
- Confidence: Medium-high.
- Caveats: External callers could retry with changed scopes; such a coordination actor/loop is not installed in the broker itself.

### Absence scope

- Surfaces inspected: Swarm planning, concurrent child run, change merger, admission validation, run registry and MCP run/cancel interface.
- Plausible first-party paths checked: Sibling path overlap handling, root path allocation, static concurrency slots and stop-on-child-error behavior.
- Why no material first-party path remains: None of these paths closes a distinct agent/constructor-owned inter-S1 negotiation/attenuation loop with returned revised sibling behavior; rejection terminates the run.

## S3 — Inside-and-now control

- State: —
- Function: No autonomous whole-system current-control authority over a portfolio of active work and shared commitments beyond bounded delegation rules.
- Disturbance / variety regulated: Provider failures, spending/turn/tool budgets, child-run admission, timeout and cancellation.
- Decisive decision or feedback right: Caller fixes model, task, tool permissions and budgets; swarm root generates a one-time file-scoped task plan, while the runtime enforces ceilings and aborts on failure.
- Decision owner: Caller/operator owns shared limits and resource policy; model's root plan owns current task decomposition, not ongoing organizational capacity or commitments.
- Supporting / enforcement mechanisms: `AgentRunRegistry`, global concurrency, `AgentRunBudget`, per-phase token reservation, node admission caps, failure propagation and status registry.
- Closure path: Preset limits → runtime admission/scheduling/termination; the shipped loop lacks a whole-run current-state appraisal feeding discretionary reallocation of operational commitments.
- Why this is / is not agent-owned: Model task splitting is not evidenced whole-system current-resource bargaining or authoritative intervention; semaphores/budgets enforce caller choices.
- Evidence: [run registry](https://github.com/BlackJaxDev/local-agent-broker/blob/86b09380e3393126d6c540787a7576a61d21565b/src/LocalAgentBroker/AgentRunRegistry.cs), [swarm plan](https://github.com/BlackJaxDev/local-agent-broker/blob/86b09380e3393126d6c540787a7576a61d21565b/src/LocalAgentBroker/AgentSwarmRunner.Planning.cs), [limits and failure propagation](https://github.com/BlackJaxDev/local-agent-broker/blob/86b09380e3393126d6c540787a7576a61d21565b/src/LocalAgentBroker/AgentSwarmRunner.Execution.cs).
- Basis: Bounded negative after testing root-orchestrator and runtime-manager paths.
- Confidence: Medium-high.
- Caveats: Host clients may provide higher-recursion fleet S3; their decisions are outside this broker's boundary.

### Absence scope

- Surfaces inspected: Registry, budget definitions, route advisor, model run loop, swarm planner and progress tracker.
- Plausible first-party paths checked: Root orchestrator as S3, model routing as current priority decision, dynamic nodes as portfolio management, hard budgets/concurrency as resource ownership.
- Why no material first-party path remains: Operational choices are individual task planning or caller-selected limits with deterministic enforcement, without agent authority and returned whole-system current-control adjustments.

## S3* — Complementary audit

- State: A
- Function: Bounded model-owned source-backed review of child agent code-change claims before approval or application.
- Claim being audited: Each leaf's proposed replacement is a valid contribution to the parent objective and success criteria.
- Ordinary reporting path: Leaf model emits JSON `path`, `base_sha256`, `old_text` and `new_text`; runner collects child artifacts.
- Complementary access path: A fresh parent review API request receives the unchanged child artifacts *and* broker-captured immutable source snapshots and original objective, not only the leaf's completion assertion. The deterministic merger separately validates base hashes/overlap.
- Independence boundary: The review runs as a distinct provider phase after leaves finish, without their continuation or permission to modify their artifacts; the child cannot mark its own edits approved. The same exact model/provider family may be used and all inputs are broker-supplied snapshots, so this is bounded internal complementary inspection, not cross-model or external institutional audit.
- Who acts on findings: `RunNodeAsync` rejects the entire swarm when the parent model returns `approved=false`; only positive review returns proposals to the run registry for caller review or explicit Windows application.
- Disturbance / variety regulated: Plausible but faulty code replacements, mismatch to objective and misleading leaf success claims.
- Decisive decision or feedback right: Separate parent reviewer model decides `approved` and `summary` after examining source and unchanged proposed edits; deterministic orchestrator enforces that verdict.
- Decision owner: Review-phase provider model makes the substantive accept/reject judgment; runner parser and fail path are supporting enforcement.
- Supporting / enforcement mechanisms: Immutable source snapshot capture, isolated phase request with no tools, review-specific instructions, JSON parse, merge collision check and no-change-on-rejection guard.
- Closure path: Leaf proposals → fresh model review with original source/artifacts → verdict → rejection terminates with no approved changes, or approval exposes the proposal for caller acceptance and possible readback-checked application.
- Boundary reachability: Optional production `swarm` uses `RunNodeAsync` for every orchestrator node, creates a distinct `CreatePhaseRequest` with context-file snapshots for review, and `RunSwarmAsync` exposes only approved changes.
- Why this is / is not agent-owned: The reviewer independently judges a source-backed child claim rather than trusting its self-report; the deterministic parser does not supply the substantive review decision.
- Evidence: [review request and input wiring](https://github.com/BlackJaxDev/local-agent-broker/blob/86b09380e3393126d6c540787a7576a61d21565b/src/LocalAgentBroker/AgentSwarmRunner.Planning.cs), [review verdict closure](https://github.com/BlackJaxDev/local-agent-broker/blob/86b09380e3393126d6c540787a7576a61d21565b/src/LocalAgentBroker/AgentSwarmRunner.Execution.cs), [provider snapshot input](https://github.com/BlackJaxDev/local-agent-broker/blob/86b09380e3393126d6c540787a7576a61d21565b/src/LocalAgentBroker.Orchestration/OpenAiResponsesModelClient.cs), [rejection test](https://github.com/BlackJaxDev/local-agent-broker/blob/86b09380e3393126d6c540787a7576a61d21565b/tests/LocalAgentBroker.Tests/AgentSwarmRunnerTests.cs).
- Basis: Structural distinct audit-judgment call with source evidence and returned corrective veto.
- Confidence: Medium: model decision and wiring established in source; actual provider-backed judgments not replayed.
- Caveats: Same model/provider can produce correlated errors; review sees captured source and proposals, not independently sampled live post-apply code. This is not a general-purpose S3* of all broker runs.

## S4 — Outside-and-then intelligence

- State: —
- Function: No shipped external/future environmental sensing, option formation, and adopted adaptation loop for the broker itself.
- Disturbance / variety regulated: Changing provider options, future model costs/capabilities, repository evolution and new threats.
- Decisive decision or feedback right: Caller selects actual model/configuration; keyword-based route advisor can recommend a model for the *current* objective, not revise future organizational capability.
- Decision owner: Human caller/developer for model/policy upgrades; deterministic `AgentRouteAdvisor` for present-task recommendation.
- Supporting / enforcement mechanisms: Exact-model catalog, task keyword classifier, provider error/retry diagnostics and operator settings.
- Closure path: Current objective → static model recommendation → caller choice for this run; no external sensing→prospective options→capability adoption path.
- Why this is / is not agent-owned: Task difficulty routing and provider retries respond to current execution, not environmental foresight or adopted future change.
- Evidence: [route advisor](https://github.com/BlackJaxDev/local-agent-broker/blob/86b09380e3393126d6c540787a7576a61d21565b/src/LocalAgentBroker/AgentRouteAdvisor.cs), [broker config](https://github.com/BlackJaxDev/local-agent-broker/blob/86b09380e3393126d6c540787a7576a61d21565b/docs/configuration.md), [run/model validation](https://github.com/BlackJaxDev/local-agent-broker/blob/86b09380e3393126d6c540787a7576a61d21565b/src/LocalAgentBroker/AgentRunRegistry.cs).
- Basis: Bounded negative after route/adaptation candidates were inspected.
- Confidence: High.
- Caveats: A user may delegate future-looking research to an individual worker; that is operational S1 output, not an established broker-level S4.

### Absence scope

- Surfaces inspected: Route advisor, model catalog, configuration, provider retry logic, MCP control tools and swarm planning.
- Plausible first-party paths checked: Model routing as external forecast, failure-based provider retry as strategic adaptation, task research requests as S4, configuration change as parent mode.
- Why no material first-party path remains: The shipped path has no autonomous or closed parent-governed future-environment model generating and adopting broker-level capability options.

## S5 — Policy and identity

- State: —
- Function: No ultimate identity/policy deliberation and legitimate return-to-runtime decision loop at this broker recursion.
- Disturbance / variety regulated: Task authority, source-file permissions, credential exposure, destructive editor commands and uncontrolled billed model execution.
- Decisive decision or feedback right: Caller and configuration supply boundaries; deterministic validators reject unauthorized requests. There is no shipped identity/charter question escalated to and resolved by an ultimate authority with a returned mandate.
- Decision owner: External MCP caller/operator for task authorization and security policy; program validators enforce rather than govern its content.
- Supporting / enforcement mechanisms: Explicit workspace/allowed paths, tool annotations and allowlist, destructive/mutation flags, exact model requirement, budget checks and secret-path denial.
- Closure path: Operator-supplied scope → fixed request guards → permitted/denied run; no identity-level issue→legitimate parent authority→binding policy decision→changed subsequent operation.
- Why this is / is not agent-owned: Ordinary permissions and operator review of a patch are run-level controls, not a first-party S5 organization or parent-governed identity loop.
- Evidence: [protocol policy](https://github.com/BlackJaxDev/local-agent-broker/blob/86b09380e3393126d6c540787a7576a61d21565b/docs/protocol.md), [repository path policy](https://github.com/BlackJaxDev/local-agent-broker/blob/86b09380e3393126d6c540787a7576a61d21565b/src/LocalAgentBroker/RepositoryPathPolicy.cs), [run admission](https://github.com/BlackJaxDev/local-agent-broker/blob/86b09380e3393126d6c540787a7576a61d21565b/src/LocalAgentBroker/AgentRunRegistry.cs).
- Basis: Bounded negative for the standard-distribution authority path.
- Confidence: High.
- Caveats: The parent organization using the broker may have an S5; its external decisions are not part of this local harness's evidenced operating structure.

### Absence scope

- Surfaces inspected: MCP interface, configuration, registry, tool policy, path validation and host apply mode.
- Plausible first-party paths checked: Request approval as policy, tool restrictions as autonomous S5, source mutation gate as parent policy, model route recommendation as identity choice.
- Why no material first-party path remains: All constrain specific tasks and access; none establishes an ultimate identity-policy decisive right or returned governance closure at the broker boundary.

## Recursion

The optional swarm nests orchestrator and leaf calls but does not give each child a durable environment, independent identity and full metasystem. It is bounded task decomposition, not proof of recursive viability.

## Variety and escalation

Provider/tool loops and optional swarm expand task-level response variety. Static budgets, path whitelists, snapshots and exact-model enforcement attenuate risk. Distinct model review can veto unsound child proposals; provider retries, cancellations, timeout and host error reporting remain operational controls rather than established prospective S4 or identity-level S5 decisions. Model-run failure returns to the MCP caller, not an evidenced VSM algedonic authority channel.

## Evidence gaps

- Assessment used pinned source, documentation and unit-test intent; .NET SDK was unavailable here, so no local build/test or paid provider live run was executed. This is not a claim that source tests passed in this environment.
- S3* is restricted to the optional swarm's pre-apply proposals; review uses separate calls but the same model/provider and captured source may share errors. No post-apply independent audit or institutional reviewer is claimed.
- No external MCP host's governance, user-specific credentials, editor runtime or private deployment behavior was inspected or credited.

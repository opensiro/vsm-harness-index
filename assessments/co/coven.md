---
harness_id: coven
project_name: Coven
repository: https://github.com/OpenCoven/coven
review_ref: 8efc5657fabd2f8ff657a13e4d5f412c2803c159
reviewed_at: 2026-11-20
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Coven

## Review boundary

- System in focus: The public first-party Coven local harness substrate **together with its separately opt-in `coven-agents` Rust model/tool loop library**, distinguishing what each mode actually owns. Not a claim that the default PTY daemon embeds or uses that library or owns the intelligence of external Codex/Claude sessions.
- Purpose and identity: Host project-scoped coding-agent sessions with authoritative local lifecycle, explicit execution/policy bounds, event and workflow records, while optionally allowing library integrators to assemble bounded provider-neutral model-operated agents using shipped Rust `coven-agents`.
- Relevant environment: Developer project, external coding agent process outputs, local filesystem and IPC clients, native hosted model adapters for optional library, configured user work and permission inputs, process crashes/recovery.
- Standard-distribution boundary: Rust Coven daemon/CLI and session ledger, external-harness adapters; plus first-party workspace package `crates/coven-agents` with public `Agent`, `Runner`, `Model`, `Tool`, delegation and loop journal APIs. Optional `coven-agents` is experimental and separate from default daemon/PTY flow. No default live model integration or hosted provider is inferred.
- Credited operating / distribution surfaces: `crates/coven-agents/src/lib.rs`, `model.rs`, `agent.rs`, `agent_loop.rs`, `runner.rs`, `delegation.rs`, `loop_runner.rs`, `review.rs`, plus daemon control and session adapters as supporting environment only.
- Adjacent first-party surfaces excluded from ownership: Executed Claude Code, Codex and Copilot CLI agent internals, separate `coven-code` engine, external OpenClaw plugin intelligence, third-party providers, owner-created model adapters, source repo contributor CI/review and hypothetical future Psyche cloud orchestration.
- First-party operating modes considered: Ordinary daemon/CLI `coven run codex` spawning external agents **not credited as first-party model autonomy**; developer opt-in `coven-agents` library model/tool runs with custom model adapter; bounded child delegation and optional proposal-review adapter; automation daemon with stored schedules and human/operator-granted permissions.
- Recursion level: One first-party library agent invocation and its optional child calls within the local host's project-scoped substrate, not a whole enterprise or independent Cloud Coven deployment.
- Reviewed revision: `8efc5657fabd2f8ff657a13e4d5f412c2803c159`. GitHub stable ID 1222160568, MIT, nonfork, public.
- Observation date: 2026-11-20.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

Default `coven run` is a Rust-owned control plane: it validates project root/cwd and allowlisted harness, starts an external coding-agent executable in a PTY, stores session state/events and lets owner clients attach, inspect and stop. The model/tool choices in external Claude/Codex/Copilot **remain external**, no matter how thoroughly Coven journals them. This is not itself an autonomous first-party agent.

Separately, the shipped `coven-agents` Rust workspace package has its own bounded loop. A host supplies a `Model<C>` adapter and configured `Agent<C>` with instructions/tools; `Runner<C>` sends first-party model requests, executes requested typed tool calls, returns tool feedback and accepts a final model output or handoff. `DelegationSpec` isolates and attenuates child capability and context provenance by project, tool/resource names, budgets and digests; host-provided grants and context resolvers establish the trust boundaries, with fail-closed unknown effects and recovery disposition. `GoalLoopRunner` journals repeated invocations and calls a **host-provided `LoopEvaluator`** to decide continue or stop. Pre-dispatch `ProposalReview` is a fail-closed *pluggable approval gate*, and the crate ships the **trait/seam only**, no independent model reviewer implementation. None of these optional primitives is automatically activated by the ordinary CLI/daemon.

Sources: [runtime architecture](https://github.com/OpenCoven/coven/blob/8efc5657fabd2f8ff657a13e4d5f412c2803c159/docs/ARCHITECTURE.md), [operational model](https://github.com/OpenCoven/coven/blob/8efc5657fabd2f8ff657a13e4d5f412c2803c159/docs/OPERATIONAL-MODEL.md), [coven-agents guide](https://github.com/OpenCoven/coven/blob/8efc5657fabd2f8ff657a13e4d5f412c2803c159/crates/coven-agents/README.md), [public Rust surface](https://github.com/OpenCoven/coven/blob/8efc5657fabd2f8ff657a13e4d5f412c2803c159/crates/coven-agents/src/lib.rs).

## Operational model

In the default runtime, the human/controller commands the daemon to launch a named external harness, the daemon enforces identity/path/lifecycle/permission conditions and logs observed process output. The agent's self-directed work occurs **outside** Coven. In an opt-in first-party library run, the host provides a concrete model adapter and tools; an in-process model chooses tool calls and changes its next action from the returned result. A host may build child-delegation and recovery into this behavior. However, the library's parent grant, child concurrency limit, evaluator and reviewer are imposed/configured by host adapters, with no demonstrated first-party inter-child arbitration, separate reviewer model, external future intelligence or ultimate-identity governance loop.

## S1 — Operations

- State: A
- Function: Execute a developer-scoped operation by model-selected tool calls and task feedback **in the native `coven-agents` library mode**.
- Disturbance / variety regulated: Unforeseen tool results, model-selected next steps, dynamic task input, failures and bounded handler responses.
- Decisive decision or feedback right: Configured model chooses `ModelAction::ToolCall` / handoff / final response; runner dispatches chosen first-party tool and reports feedback.
- Decision owner: Model adapter supplied by the integrator using first-party `Agent`/`Runner`; the model backend is external, as for other open-source frameworks, but source-owned loop is first-party.
- Supporting / enforcement mechanisms: Typed model/tool/agent traits, `Runner::run`, budgets, per-agent permission/guardrail, tool results and persisted invocation/journals.
- Closure path: Host starts `Runner` -> first-party code submits `ModelRequest` -> configured model selects tool -> runner validates, reviews if configured, executes and records `ToolResult` -> model changes next action or finalizes.
- Boundary reachability: Public Rust `coven-agents` `Cargo.toml` workspace crate `0.1.0` exports `Runner`, `Model`, `Agent` and `Tool`; not private tests only, though declared experimental.
- Why this is / is not agent-owned: The model chooses substantive actions *only in that composable library mode*. Default `coven run codex` exports another vendor's model intelligence and is not credited for S1.
- Evidence: [public crate manifest](https://github.com/OpenCoven/coven/blob/8efc5657fabd2f8ff657a13e4d5f412c2803c159/crates/coven-agents/Cargo.toml), [public exports](https://github.com/OpenCoven/coven/blob/8efc5657fabd2f8ff657a13e4d5f412c2803c159/crates/coven-agents/src/lib.rs), [model protocol](https://github.com/OpenCoven/coven/blob/8efc5657fabd2f8ff657a13e4d5f412c2803c159/crates/coven-agents/src/model.rs), [agent loop](https://github.com/OpenCoven/coven/blob/8efc5657fabd2f8ff657a13e4d5f412c2803c159/crates/coven-agents/src/agent_loop.rs), [runner](https://github.com/OpenCoven/coven/blob/8efc5657fabd2f8ff657a13e4d5f412c2803c159/crates/coven-agents/src/runner.rs).
- Basis: structural
- Confidence: high
- Caveats: No live non-mock provider adapter or release registry status independently verified; default CLI agents are external and never implied first-party.

## S2 — Coordination

- State: —
- Function: No sourced first-party cross-operational-agent coordination relation regulates sibling interference beyond bounded child authority and hosting.
- Disturbance / variety regulated: Simultaneously running model-operated children could contend for shared resources, claim conflicting tasks or produce mutually incompatible edits.
- Decisive decision or feedback right: `PreparedDelegation::prepare` verifies each child authority/context subset **against its parent grant**, and `Runner::with_child_limit` caps child concurrency; there is no source-level sibling conflict choice/feedback owner or disjoint claim arbiter.
- Decision owner: Host grants authority and validates tools; no separate first-party S2 coordination owner was demonstrated for competing child operations.
- Supporting / enforcement mechanisms: `DelegationSpec`, `AuthorityScope`, `ContextManifest`, subset proof, child limits and event/cancellation/recovery tracking.
- Closure path: Parent grants rights -> child's rights are attenuated or rejected -> child executes. This establishes safety hierarchy, but not adaptation of peer interference based on independent S1 feedback.
- Boundary reachability: Optional public `coven-agents` delegation API, not default daemon's session orchestration.
- Why this is / is not agent-owned: A fail-closed grant proof, resource-capability label and concurrency cap are deterministic controls. No model-owned coordination decision on independent inter-child conflict is evidenced.
- Distinct S1 units: First-party-model-driven delegated child invocations supported by `Runner::run_delegation`.
- Inter-S1 disturbance: Shared source files and claims among multiple children.
- Attenuating coordination relation: No first-party mechanism shown that ensures siblings receive disjoint resources or updates sibling decisions based on observed conflict; parent-subset checks do not compare siblings.
- Feedback into subsequent S1 behaviour: Child outputs/failures can return to a host parent, but S2-specific inter-child interference feedback is not guaranteed.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: No independently qualifying S2 regulation established from those general primitives; no credit for daemon action routing or PTY multiplexing.
- Evidence: [delegation](https://github.com/OpenCoven/coven/blob/8efc5657fabd2f8ff657a13e4d5f412c2803c159/crates/coven-agents/src/delegation.rs), [runner child limit](https://github.com/OpenCoven/coven/blob/8efc5657fabd2f8ff657a13e4d5f412c2803c159/crates/coven-agents/src/runner.rs), [native guide](https://github.com/OpenCoven/coven/blob/8efc5657fabd2f8ff657a13e4d5f412c2803c159/crates/coven-agents/README.md), [daemon architecture](https://github.com/OpenCoven/coven/blob/8efc5657fabd2f8ff657a13e4d5f412c2803c159/docs/ARCHITECTURE.md).
- Basis: structural
- Confidence: medium
- Caveats: An application may choose disjoint authority for siblings, but that is host composition, not a shipped sibling-arbitration constructor.

### Absence scope

- Surfaces inspected: PTY session/daemon authority, first-party agent delegation grant and runner, child concurrency limit, model and tool protocols.
- Plausible first-party paths checked: Cross-session lifecycle routing, attenuated child grants, child cancellation/unknown-outcome recovery and multi-agent handoffs.
- Why no material first-party path remains: All verified paths enforce authority/lifecycle or sequential ownership; no first-party peer-level conflicting-work resolution relation was evidenced.

## S3 — Inside-and-now control

- State: —
- Function: No independent first-party agent owner demonstrably evaluates and reallocates **whole current multi-worker commitments** beyond the task loop.
- Disturbance / variety regulated: Lost or stalled child work and incomplete overall goals.
- Decisive decision or feedback right: The public `GoalLoopRunner` calls a host-supplied `LoopEvaluator` for complete/continue decisions; child failure returns recovery disposition to the caller. No source establishes a first-party model lead with a whole-task board and discretionary current-control workflow across competing S1 workers.
- Decision owner: Host integrator or its separately supplied evaluator; neither generic `Runner` nor daemon decisions establish an internal S3 agent.
- Supporting / enforcement mechanisms: Durable goal loop checkpoints, bounded retries/recovery fences, child cancellation, clocks, event log, operator daemon oversight.
- Closure path: An evaluator *could* choose next loop iteration, and host may reconcile ambiguous effects, but model-owned goal completion/reallocation is not supplied as a first-party governing mode.
- Boundary reachability: Public `GoalLoopRunner` and trait interfaces; actual evaluator logic is external and could be either code or a separate model.
- Why this is / is not agent-owned: A framework seam that invokes an application-defined callback is not proof of first-party agent-owned S3. One model deciding its next S1 tool does not become a whole-system manager merely because the turn has a goal.
- Whole-system current view: Checkpoint tracks loop progress and next input, but no built-in total multi-worker commitments/owned progress view coupled to model decisions.
- Current-control decision scope: No qualifying first-party whole-current-work executive; operator-managed session lifecycle and host evaluator remain distinct.
- Evidence: [loop control](https://github.com/OpenCoven/coven/blob/8efc5657fabd2f8ff657a13e4d5f412c2803c159/crates/coven-agents/src/loop_runner.rs), [runner](https://github.com/OpenCoven/coven/blob/8efc5657fabd2f8ff657a13e4d5f412c2803c159/crates/coven-agents/src/runner.rs), [loop guide](https://github.com/OpenCoven/coven/blob/8efc5657fabd2f8ff657a13e4d5f412c2803c159/crates/coven-agents/README.md), [session state machine](https://github.com/OpenCoven/coven/blob/8efc5657fabd2f8ff657a13e4d5f412c2803c159/docs/SESSION-LIFECYCLE.md).
- Basis: structural
- Confidence: medium
- Caveats: A downstream integrator may build model-owned S3 from these primitives. The assessment does not deny potential, only its source-bounded first-party realization.

### Absence scope

- Surfaces inspected: Durable `GoalLoopRunner`, `LoopEvaluator`, children/disposition, daemon automation scheduling and session state.
- Plausible first-party paths checked: Goal-loop continuation, pre/post tool proposals, delegated task recovery, scheduled daemon missions and policy approval.
- Why no material first-party path remains: Neither durable scheduling nor host-supplied evaluator supplied a distinct model-owned current-task management decision and return to multiple S1 units.

## S3* — Complementary audit

- State: —
- Function: No first-party auditor with an independent raw-evidence path challenging operational model claims was shipped for native runs.
- Disturbance / variety regulated: A model-proposed tool action may be unsafe or wrong, and a final output might falsely claim success.
- Decisive decision or feedback right: `ProposalReview<C>` permits an externally implemented reviewer to veto a **pre-dispatch tool proposal**. It does not ship an independent reviewer instance or inspect the model's finished operational claims using a separate evidence path.
- Decision owner: Host's reviewer trait implementation, if configured; none sourced as a first-party operational independent audit owner.
- Supporting / enforcement mechanisms: Per-agent review registration, `Permit` / `ProposalOnly` / `Reject` / `Unavailable`, fail-closed errors, tool event journal and conformance/test cases.
- Closure path: Registered external callback returns veto/permit -> runner enforces. This is an authorization gate, not independent S3* evidence sampling with findings fed into task repair.
- Boundary reachability: First-party `ProposalReview` seam is public, but its README explicitly says it ships **no HTTP client or hosted review transport**.
- Why this is / is not agent-owned: Reviewing a proposed action before side effect, even with a configured model, is not the complementary independent audit path for system results. Conformance unit tests are repository development activities.
- Claim being audited: An agent's completed operational evidence/claim, not a proposed tool's permission eligibility.
- Ordinary reporting path: Native model-to-tool result history and final `RunResult`.
- Complementary access path: No independently implemented source-observing reviewer that challenges ordinary reported results was demonstrated.
- Independence boundary: Neither separate source path nor independent auditor implementation supplied; trait-only seam is not sufficient.
- Who acts on findings: Host may implement veto or post-run critique, but no built-in post-finding repair loop shown.
- Evidence: [proposal-review trait](https://github.com/OpenCoven/coven/blob/8efc5657fabd2f8ff657a13e4d5f412c2803c159/crates/coven-agents/src/review.rs), [review registration](https://github.com/OpenCoven/coven/blob/8efc5657fabd2f8ff657a13e4d5f412c2803c159/crates/coven-agents/src/agent.rs), [runtime guide](https://github.com/OpenCoven/coven/blob/8efc5657fabd2f8ff657a13e4d5f412c2803c159/crates/coven-agents/README.md).
- Basis: explicit and structural
- Confidence: high
- Caveats: A custom review service could enable S3* with additional evidence; it is outside this pinned first-party runtime.

### Absence scope

- Surfaces inspected: Proposal-review seam, session/loop journals, conformance tests, daemon event logs and external coding-agent session outputs.
- Plausible first-party paths checked: Guardrails, preflight review, external PR CI, automatic event logging and side-effect reconciliation.
- Why no material first-party path remains: Each is permissions/telemetry/recovery rather than an independent falsifying operational auditor with a distinct evidence-to-repair feedback route.

## S4 — Outside-and-then intelligence

- State: —
- Function: No first-party process develops prospective capability adaptation based on future external distinctions and returns it to governed present operations.
- Disturbance / variety regulated: Changing coding-agent ecosystems, future client requirements, security threats and host capabilities.
- Decisive decision or feedback right: Human maintainers and operators select provider adapters, update compatibility contracts and schedule automation; no native model-directed future-sensing adaptation agent is shown.
- Decision owner: Project owner/maintainer outside the assessed task runtime; none for first-party operational S4.
- Supporting / enforcement mechanisms: Pluggable adapter selection, local session events, external research through attached engines, a roadmap document and planned Psyche orchestration.
- Closure path: External changes lead to manual adapter/config updates or code releases, not a shipped autonomous future-intelligence loop.
- Why this is / is not agent-owned: Provider-neutrality, durable retries, roadmap and release governance are infrastructure/development, not an operational S4 intelligence return loop.
- Evidence: [architecture](https://github.com/OpenCoven/coven/blob/8efc5657fabd2f8ff657a13e4d5f412c2803c159/docs/ARCHITECTURE.md), [adapter contract](https://github.com/OpenCoven/coven/blob/8efc5657fabd2f8ff657a13e4d5f412c2803c159/docs/HARNESS-ADAPTERS.md), [roadmap](https://github.com/OpenCoven/coven/blob/8efc5657fabd2f8ff657a13e4d5f412c2803c159/docs/ROADMAP.md), [goal runner](https://github.com/OpenCoven/coven/blob/8efc5657fabd2f8ff657a13e4d5f412c2803c159/crates/coven-agents/src/loop_runner.rs).
- Basis: structural
- Confidence: medium
- Caveats: External client software may conduct prospective R&D; none inherited.

### Absence scope

- Surfaces inspected: Daemon/adapter router, automation scheduler, memory, agent loop and roadmap.
- Plausible first-party paths checked: Adapter update workflow, scheduled missions and goal loop, user-installed engines, release rules.
- Why no material first-party path remains: These do not prove external future evidence -> deliberate capability option selection -> accepted runtime adaptation under a first-party owner.

## S5 — Policy and identity

- State: —
- Function: No qualifying first-party ultimate system identity/mission revision and commitment closure is proven at local agent-session recursion.
- Disturbance / variety regulated: Conflicting foundational purposes, trust policies, developer authority and enduring project identity.
- Decisive decision or feedback right: Human operator picks project roots, commands process lifecycle, policy and permissions; daemon enforces them, and `DelegationGrant` encodes parent authority assertions, but none decides ultimate identity conflicts through a documented operational S5 loop.
- Decision owner: Human developer/host application outside the agent; not a first-party task-runtime S5 governor.
- Supporting / enforcement mechanisms: Root checks, proposal-origin and human approval routes, child authority subsets, signed receipt validation and GitHub release governance.
- Closure path: Client/daemon decisions enforce already chosen authorization, but no agent-specific identity/purpose issue -> legitimate ultimate choice -> durably returned policy alignment loop was source-demonstrated.
- Why this is / is not agent-owned: Strict authority bounds are important security but not themselves S5 governance; repository branch policies govern *software development* at another recursion.
- Identity / ultimate-policy issue: Which mission the local agent system legitimately serves and how foundational authority conflicts are decided, beyond per-tool permission.
- Ultimate authority in each claimed mode: No positive first-party mode; human host controls task purpose and configuration.
- Return-to-operation path: Static grants and project boundaries persist as config/state but no separately resolved ultimate-policy decision path is evidenced.
- Evidence: [operational authority boundary](https://github.com/OpenCoven/coven/blob/8efc5657fabd2f8ff657a13e4d5f412c2803c159/docs/OPERATIONAL-MODEL.md), [delegation grant](https://github.com/OpenCoven/coven/blob/8efc5657fabd2f8ff657a13e4d5f412c2803c159/crates/coven-agents/src/delegation.rs), [proposal review](https://github.com/OpenCoven/coven/blob/8efc5657fabd2f8ff657a13e4d5f412c2803c159/crates/coven-agents/src/review.rs), [release governance excluded](https://github.com/OpenCoven/coven/blob/8efc5657fabd2f8ff657a13e4d5f412c2803c159/.github/release-governance.json).
- Basis: structural
- Confidence: medium
- Caveats: No organization-scale authority decision is inferred from repo maintainer gates or generic human-in-the-loop tool approval.

### Absence scope

- Surfaces inspected: Daemon authority and policy, human proposal routes, first-party agent grant and review interfaces, project identity config, release rules.
- Plausible first-party paths checked: Proposal/permission acknowledgement, signed process receipts, host model instructions, GitHub release protection.
- Why no material first-party path remains: Each enforces an existing boundary or project-development approval; no distinct recurring mission/identity governance and return loop for a deployed agent was sourced.

## Distributed OSS parent arrangement

A public OSS project can have a maintainer-owned S5 at a different higher recursion. The local Coven daemon, the experimental Rust `coven-agents` library and the project's contributor governance are separated; GitHub reviews are not credited as customer-runtime S3* or S5.

## Self-hosted and non-human modes

The ordinary CLI/daemon sessions can run unattended; their agent intelligence belongs to external executables. Only optional Rust `coven-agents` builds a first-party model/tool loop. Its provider adapters, host evaluator and proposal reviewer are separate implementation responsibilities; no default hosted instance of those roles is assumed.

## Recursion

Bounded child invocations have attenuated rights, provenance and cancellation. Their isolation is a safety contract, not evidence that each child is a complete independent viable organization. No higher organizational recursion is inferred.

## Variety and escalation

Source-root guards attenuate environment/path variety, event logs preserve outputs, and cancellation/unknown-effect status avoids unsafe duplicate work. The opt-in model loop can revise its own current operation; a host must externally resolve policy, reviewer, inter-child interference and prospective capability decisions. These controls are substantial but intentionally not all classified as independent VSM functions.

## Evidence gaps

- Static source inspection only, no live model adapter, optional Rust crate production use, external CLI model execution, independent secondary audit, or host release-registry verification was performed.
- Positive S1 is **limited to public experimental `coven-agents` library mode**; normal PTY mode does not inherit Codex or Claude agent decisions.
- All negative states are bounded by that first-party boundary and may differ in an independently sourced downstream app with added governance.
- Native proposal review is a fail-closed pre-dispatch approval seam, **not** an implemented S3* evidence-sampling challenger; goal evaluator is host-supplied, not a first-party autonomous S3 executive.

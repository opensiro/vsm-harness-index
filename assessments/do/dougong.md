---
harness_id: dougong
project_name: Dougong
repository: https://github.com/zhanghaojie513/Dougong
review_ref: 5d7ff991baa0da919c580f418ed5415b50ba3a94
reviewed_at: 2026-11-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Dougong

## Review boundary

- System in focus: The standard .NET 10 Dougong agent SDK and its wired CLI/ACP host, including a primary model-driven task session, optional delegated subagents and plugin kernel.
- Purpose and identity: Run conversational tasks against local workspace tools through a replaceable model/agent/tool stack, and preserve bounded state, approvals and recoverable session records.
- Relevant environment: User prompts and plan approval, workspace files and shell, model endpoint, MCP endpoints, ACP client, runtime plugins, tool failures, persistent JSONL and concurrent sessions.
- Standard-distribution boundary: Shipped Dougong.Agent, Dougong.Kernel, Dougong.Ai, Dougong.Hosting, Dougong.Cli, Dougong.Acp and optional Dougong.Mcp compositions accessible through supported first-party entry points; not an imagined downstream orchestrator.
- Credited operating / distribution surfaces: [CLI wiring](https://github.com/zhanghaojie513/Dougong/blob/5d7ff991baa0da919c580f418ed5415b50ba3a94/src/Dougong.Cli/SessionComposition.cs), [agent loop](https://github.com/zhanghaojie513/Dougong/blob/5d7ff991baa0da919c580f418ed5415b50ba3a94/src/Dougong.Agent/LoopAgentRuntime.cs), [subagent tools](https://github.com/zhanghaojie513/Dougong/blob/5d7ff991baa0da919c580f418ed5415b50ba3a94/src/Dougong.Agent/SubagentTools.cs), [resource gate](https://github.com/zhanghaojie513/Dougong/blob/5d7ff991baa0da919c580f418ed5415b50ba3a94/src/Dougong.Agent/ToolResourceGate.cs), [host program](https://github.com/zhanghaojie513/Dougong/blob/5d7ff991baa0da919c580f418ed5415b50ba3a94/src/Dougong.Cli/Program.cs) and [README.en](https://github.com/zhanghaojie513/Dougong/blob/5d7ff991baa0da919c580f418ed5415b50ba3a94/README.en.md).
- Adjacent first-party surfaces excluded from ownership: Comparison/self-check probes, design commitments, tests, local dogfood, desktop sample app, benchmark results, CI/ApiCompat and release/publishing machinery; these may corroborate shipped behavior but are not live metasystem actors.
- First-party operating / deployment modes considered: CLI REPL, headless-style SDK embedding, ACP line-delimited agent host, optional MCP/remote model connector, supervised plan-review mode, multiple ACP sessions and delegated subagent tasks; optional memory and shell configured by security switches.
- Recursion level: One standard host/session composition with a model-owned primary agent and its spawned model-owned child task cells; same-process concurrent sessions are relevant to cross-session resource coordination, not a global multi-tenant organization.
- Reviewed revision: 5d7ff991baa0da919c580f418ed5415b50ba3a94.
- Observation date: 2026-11-04.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The CLI/ACP host constructs a session composition that resolves model, approval, persistence, tools and plugin services via the kernel. The agent runtime drives IChatClient turns, handles tool-call dispatch and streams results back into model context. The dispatcher validates schemas, obtains permissions, acquires resource leases, records failures and executes tools. JSONL commit barriers protect user input/model responses/tool outcomes; session records can be recovered/branched. A goal tracker is agent-accessible but explicitly does not autonomously start new turns. The reference host registers bounded asynchronous subagent delegation: each child has an independent model history, scoped tool set, shared parent workspace, no durable child transcript, and a result returned to the primary agent. Separate worker/tool status and resource locks supply coordination evidence; plan approval is a human gate on current task execution. An optional L1 preference-memory store reads whitelisted, previously enabled artifacts, but no in-distribution generator/approval/enablement loop writes and activates new memory artifacts. The kernel manages plugin service leases, dependency state and hot swap without choosing substantive task goals. [Architecture](https://github.com/zhanghaojie513/Dougong/blob/5d7ff991baa0da919c580f418ed5415b50ba3a94/docs/architecture.md), [SessionComposition](https://github.com/zhanghaojie513/Dougong/blob/5d7ff991baa0da919c580f418ed5415b50ba3a94/src/Dougong.Cli/SessionComposition.cs), [LoopAgentRuntime](https://github.com/zhanghaojie513/Dougong/blob/5d7ff991baa0da919c580f418ed5415b50ba3a94/src/Dougong.Agent/LoopAgentRuntime.cs).

## Operational model

The primary S1 is one model-driven task loop; independently running child agents become bounded, task-scoped operational S1 cells for delegated work. The primary model selects child tasks and requests their results, then decides whether to proceed or revise. A deterministic registry enforces concurrency/depth ceilings, and workspace/tool locks attenuate certain actual cross-cell conflicts without an agent deciding the locking rule. A user chooses ultimate task intent and can approve plan transitions; this does not by itself establish identity-level S5 policy or a parent-level whole-system S3 mode. Shared SDK building blocks alone do not establish prospective strategic adaptation or independent audit.

## S1 — Operations

- State: A
- Function: Model-directed problem solving through iterative use of file, search, shell, MCP and delegated task tools.
- Disturbance / variety regulated: Unknown workspace state, model responses, tool errors, user task changes and subprocess results.
- Decisive decision or feedback right: Choose tools and arguments, delegate self-contained subtasks, interpret results and select the next task action or final response.
- Decision owner: Primary and child model-backed agent loops; the host supplies protocols but not the concrete solution steps.
- Supporting / enforcement mechanisms: Kernel registration, tool dispatcher, approval policy, JSONL session commit, schema validation, workspace path guard, model connectors, retry and tool-round limits.
- Closure path: Prompt/history → IChatClient completion → model-selected tool call → dispatcher execution → tool/child result → subsequent IChatClient turn and final task output.
- Boundary reachability: Default SessionComposition registers tools and creates LoopAgentRuntime in both CLI and ACP paths; SubagentTool uses the same runtime class with fresh child history.
- Why this is / is not agent-owned: Removing model choice leaves permission enforcement and protocol handling, but no substantive next-step/task-selection discretion.
- Evidence: [LoopAgentRuntime.RunAsync](https://github.com/zhanghaojie513/Dougong/blob/5d7ff991baa0da919c580f418ed5415b50ba3a94/src/Dougong.Agent/LoopAgentRuntime.cs), [SessionComposition tool registration](https://github.com/zhanghaojie513/Dougong/blob/5d7ff991baa0da919c580f418ed5415b50ba3a94/src/Dougong.Cli/SessionComposition.cs), [ToolDispatcher](https://github.com/zhanghaojie513/Dougong/blob/5d7ff991baa0da919c580f418ed5415b50ba3a94/src/Dougong.Agent/ToolDispatcher.cs).
- Basis: explicit + structural.
- Confidence: high for wired model/tool feedback; external provider outcome not executed during this review.
- Caveats: Offline probes and advertised provider benchmarks are not used as evidence of real-task completion rates.

## S2 — Coordination

- State: C
- Function: Attenuate contention between concurrent task-owning sessions or worker calls accessing the same workspace.
- Disturbance / variety regulated: Overlapping shell/tool mutation and inconsistent shared-workspace state when independently executing S1 cells interfere; specifically two supported ACP sessions entering exclusive workspace actions.
- Distinct S1 units: Two concurrently model-operated ACP sessions in one process, and primary/child independent task loops when their scoped tools overlap.
- Inter-S1 disturbance: First-party G9 case explicitly models two session gates entering the same workspace and risking simultaneous exclusive operations; unguarded writes can overlap.
- Attenuating coordination relation: Process-shared normalized workspace mutex for serial/exclusive tools; a per-dispatcher resource-key read/write gate for declared tool resources; execution lease delays conflicting calls.
- Feedback into subsequent S1 behaviour: The blocked call executes only after the lease clears, then its concrete tool result reaches its requesting agent's next model turn. The coordination changes the timing/observable world state of subsequent operations; refusal/error is also returned through dispatcher.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The gate explicitly targets a concrete conflict among autonomous work cells (same workspace competing tool mutations), with conflict-dependent exclusion and resumed tool feedback; it is not merely a queue of tasks or parent-to-child dispatch.
- Decisive decision or feedback right: Apply or revise the actual inter-session resource-exclusion relation. The supplied resource gate deterministically applies declared plans; no autonomous agent is shipped as an owner of shared conflict-policy discretion.
- Decision owner: First-party deterministic constructor/runtime resource gate; developers declare tool concurrency and can compose policy authority. Agent models choose tasks but do not decide lock admissibility.
- Supporting / enforcement mechanisms: SharedWorkspaceLocks, semaphores, stable resource keys, registry limits and ToolExecutionPlan.
- Closure path: Competing tool intents → gate classification and lease acquisition → serialized protected execution → result back to the relevant agent; construction of an adaptive autonomous coordination owner is not part of this standard distribution.
- Boundary reachability: CLI/ACP SessionComposition constructs a non-isolated ToolResourceGate; the static shared lock table is reached by serial/workspace-exclusive tool invocations, corroborated by pinned G9 probe. Resource-key locks are instance-scoped and are not claimed to protect arbitrary file edits across independent dispatchers.
- Why this is / is not agent-owned: Removing agents' discretionary policy leaves the same lock decision and resource exclusion; the function-specific path is real, but not an agent-owned S2 closure, hence C rather than A.
- Evidence: [ToolResourceGate](https://github.com/zhanghaojie513/Dougong/blob/5d7ff991baa0da919c580f418ed5415b50ba3a94/src/Dougong.Agent/ToolResourceGate.cs), [G9 cross-session counterproof](https://github.com/zhanghaojie513/Dougong/blob/5d7ff991baa0da919c580f418ed5415b50ba3a94/spike/Dougong.Agent.Comparison/WorkspaceLockChecks.cs), [SubagentTool resource classification](https://github.com/zhanghaojie513/Dougong/blob/5d7ff991baa0da919c580f418ed5415b50ba3a94/src/Dougong.Agent/SubagentTools.cs), [host wiring](https://github.com/zhanghaojie513/Dougong/blob/5d7ff991baa0da919c580f418ed5415b50ba3a94/src/Dougong.Cli/SessionComposition.cs).
- Basis: explicit + structural.
- Confidence: medium-high for bounded coordination; not a claim of universal cross-worker file conflict protection.
- Caveats: Asynchronously spawned children outlive the spawn-tool lease; cross-process locks and all resource-key paths are not established.

## S3 — Inside-and-now control

- State: A
- Function: Allocate and revise current task commitments across the primary agent's active child-agent work portfolio.
- Disturbance / variety regulated: Parallel worker availability, failed delegated results, conflicting subtask priorities and finite execution capacity during one task composition.
- Whole-system current view: Agent-accessible subagent_list exposes all handles in this composition with current running state, and subagent_result returns terminal status, text, error and consumed tool rounds; get_goal and job_list expose current local task/goal state.
- Current-control decision scope: Primary model chooses which child work to launch or postpone, which results to retrieve, whether to execute remaining work itself and what follow-up action to assign, within a four-concurrent-child and bounded-depth envelope.
- Decisive decision or feedback right: Commit or revise currently active work distribution based on live child and goal results.
- Decision owner: Primary conversational model; SubagentRegistry and goal/dispatcher implement its choices but do not choose which task to prioritize.
- Supporting / enforcement mechanisms: Child handles, concurrency gate, depth bounds, one-shot result collection, goal state, optional job status and tool permission checks.
- Closure path: Primary chooses subtask → asynchronous child run → model requests list/result → receives current status/diagnostic → decides to delegate another task, wait, adjust, work directly or finish in a subsequent loop iteration.
- Boundary reachability: SessionComposition registers subagent, subagent_list, subagent_result and goal tools with the standard CLI/ACP model dispatcher; the supplied child loop uses the same IChatClient and shared registry.
- Why this is / is not agent-owned: Remove primary model discretion and the runtime still enforces slots and reports status but does not decide task allocation, current commitments or recovery.
- Evidence: [SubagentTools](https://github.com/zhanghaojie513/Dougong/blob/5d7ff991baa0da919c580f418ed5415b50ba3a94/src/Dougong.Agent/SubagentTools.cs), [SubagentRegistry](https://github.com/zhanghaojie513/Dougong/blob/5d7ff991baa0da919c580f418ed5415b50ba3a94/src/Dougong.Agent/Subagent.cs), [SessionComposition registration and child runtime](https://github.com/zhanghaojie513/Dougong/blob/5d7ff991baa0da919c580f418ed5415b50ba3a94/src/Dougong.Cli/SessionComposition.cs).
- Basis: structural; agent discretion in the standard tool-call loop is explicit.
- Confidence: medium for current-control scope, high for callable feedback path.
- Caveats: S3 scope is the one primary-session task portfolio, not a global dashboard controlling all separately instantiated hosts. No parent-governed S3 mode is evidenced by the optional plan approver.

## S3* — Complementary audit

- State: —
- Function: No sufficiently independent complementary direct-reality audit that reports corrective findings to current control.
- Disturbance / variety regulated: Tool failure, approval denial and stale session reports are ordinarily visible, but no separate auditor authority samples them independently.
- Decisive decision or feedback right: Independently challenge the operational claim with materially different access and return corrective findings to S3; not wired.
- Decision owner: Ordinary dispatcher and logger record their own actions; a human plan approver can accept a proposed plan, not audit completed operational claims.
- Supporting / enforcement mechanisms: JSONL commit barrier, ToolDispatcher approval logs, user plan review, diagnostics, self-check comparison suite and subagent result summaries.
- Closure path: Tool status returns directly to requesting model or is stored for replay; no independent auditor sampling → judgment → corrective returned control loop is shipped.
- Why this is / is not agent-owned: A child can hypothetically be tasked to review a patch, but the default host has no protected independent reviewer role, separate evidence path or mandatory corrective audit closure.
- Evidence: [JsonlAgentStore](https://github.com/zhanghaojie513/Dougong/blob/5d7ff991baa0da919c580f418ed5415b50ba3a94/src/Dougong.Agent/JsonlAgentStore.cs), [ToolDispatcher](https://github.com/zhanghaojie513/Dougong/blob/5d7ff991baa0da919c580f418ed5415b50ba3a94/src/Dougong.Agent/ToolDispatcher.cs), [PlanMode](https://github.com/zhanghaojie513/Dougong/blob/5d7ff991baa0da919c580f418ed5415b50ba3a94/src/Dougong.Agent/PlanMode.cs), [SubagentTools](https://github.com/zhanghaojie513/Dougong/blob/5d7ff991baa0da919c580f418ed5415b50ba3a94/src/Dougong.Agent/SubagentTools.cs).
- Basis: structural.
- Confidence: medium-high for bounded absence.
- Caveats: External code reviewers and offline self-check probes are outside the assessed operational boundary.

### Absence scope

- Surfaces inspected: Run/commit records, tool approval/error pipeline, subagent isolation/results, plan approval, diagnostic bundles, kernel failures and comparison test probes.
- Plausible first-party paths checked: Separate child reviewer, tool log as complementary evidence, plan review and self-check comparisons.
- Why no material first-party path remains: These expose ordinary production reports, optional human task approvals or development tests; no independent live audit mandate and returned corrective S3* loop is installed.

## S4 — Outside-and-then intelligence

- State: —
- Function: No shipped, operationally closed external-prospective capability adaptation process.
- Disturbance / variety regulated: Model/provider changes, evolving user preferences and plugin capability opportunities could merit adaptation, but the default loop addresses current tasks.
- Decisive decision or feedback right: Evaluate future-relevant environmental options and authorize capability change returned to current S3/operations; not supplied as a complete first-party chain.
- Decision owner: User/developer supplies tool plugins, provider and preferences; models choose available current task actions and can write plans.
- Supporting / enforcement mechanisms: Plugin lifecycle/hot swap, skill discovery, optional L1 MemoryStore/MemoryInjector, session compaction and manual config.
- Closure path: Whitelisted Enabled memory would be injected into later turns, but the shipped CLI has no writer invoking MemoryStore.PutAsync/AdvanceCursorAsync to create, judge, approve and enable new L1 artifacts from outside/future evidence. No prospective option judgment and capability change loop closes.
- Why this is / is not agent-owned: Temporal persistence and dynamic plugin loading do not make a model-owned strategic adaptation decision; optional memory readback is a support surface only.
- Evidence: [MemoryArtifact](https://github.com/zhanghaojie513/Dougong/blob/5d7ff991baa0da919c580f418ed5415b50ba3a94/src/Dougong.Agent/MemoryArtifact.cs), [MemoryInjector](https://github.com/zhanghaojie513/Dougong/blob/5d7ff991baa0da919c580f418ed5415b50ba3a94/src/Dougong.Agent/MemoryInjector.cs), [SessionComposition](https://github.com/zhanghaojie513/Dougong/blob/5d7ff991baa0da919c580f418ed5415b50ba3a94/src/Dougong.Cli/SessionComposition.cs), [README.en L1 claims](https://github.com/zhanghaojie513/Dougong/blob/5d7ff991baa0da919c580f418ed5415b50ba3a94/README.en.md).
- Basis: structural.
- Confidence: medium-high at the supported runtime boundary.
- Caveats: The separate experiment proving preference adherence does not establish a deployed preference-learning decision owner; embedded SDK consumers could add the missing cycle independently.

### Absence scope

- Surfaces inspected: Memory artifact state machine, injector/store/host references, provider selection, kernel lifecycle, skill discovery, goal/plan tools and shipped documentation.
- Plausible first-party paths checked: Learning from session records into approved memory, plugin/provider replacement, model-proposed planning and manual preference changes.
- Why no material first-party path remains: The memory feedback-generation/approval writer is not wired into the operating host and the other paths react to present task or external operator configuration; no complete forward-looking adaptation judgment returns to current capability.

## S5 — Policy and identity

- State: —
- Function: No runtime resolution of organizational identity or ultimate-policy dilemmas with authoritative return into subsequent work.
- Disturbance / variety regulated: Dangerous tools, security/privacy switches, permission escalation and plan approval are execution risks within a preselected organizational purpose.
- Decisive decision or feedback right: Decide a contested identity-level/ultimate-policy matter and enact the new constitutional constraint in the operating harness; no such first-party path.
- Decision owner: User/operator configures permission/environment, human approver authorizes individual tool or plan transitions, and developer chooses fixed policy implementation.
- Supporting / enforcement mechanisms: SecuritySwitches, PermissionPolicyApprover, approval content binding, restricted L1 preference whitelist and plan review.
- Closure path: User-approved actions change current task execution; configuration fixed at startup bounds tool access. No identity/policy proposal → legitimate ultimate authority → governing response → durable changed operation loop exists.
- Why this is / is not agent-owned: Approval is local task authorization; neither model nor operator tool prompt resolves identity or ultimate policy of the operating organization.
- Evidence: [PermissionPolicyApprover](https://github.com/zhanghaojie513/Dougong/blob/5d7ff991baa0da919c580f418ed5415b50ba3a94/src/Dougong.Agent/PermissionPolicyApprover.cs), [PlanMode](https://github.com/zhanghaojie513/Dougong/blob/5d7ff991baa0da919c580f418ed5415b50ba3a94/src/Dougong.Agent/PlanMode.cs), [SecuritySwitches via host](https://github.com/zhanghaojie513/Dougong/blob/5d7ff991baa0da919c580f418ed5415b50ba3a94/src/Dougong.Cli/SessionComposition.cs), [MemoryArtifact whitelist](https://github.com/zhanghaojie513/Dougong/blob/5d7ff991baa0da919c580f418ed5415b50ba3a94/src/Dougong.Agent/MemoryArtifact.cs).
- Basis: explicit + structural.
- Confidence: medium-high for bounded absence.
- Caveats: Maintainer repository-level governance is outside the deployed runtime organization.

### Absence scope

- Surfaces inspected: CLI/ACP entry points, permission switch/approval gate, memory whitelist, plan-review pipeline, kernel plugin policy and repository governance docs.
- Plausible first-party paths checked: Human plan approval, memory enablement, tool allow/deny, startup security policy and plugin loading/replacement.
- Why no material first-party path remains: Each path alters local execution authorization or capability configuration, not a runtime identity/ultimate-policy judgment with authoritative return.

## Distributed OSS parent arrangement

The public MIT-licensed repository is maintained as an SDK and includes release/compatibility governance, but those actors are not a live parent S3/S4/S5 controller wired into a shipped agent run. ACP human supervision is scoped to task and tool approval rather than to whole-organization current control or ultimate identity.

## Self-hosted and non-human modes

The supported human plan-review mode can block writes until approval, but does not close an independent parent-governed S3 decision over the whole current work portfolio; the primary model retains task allocation autonomy after approval. No separately closed parent S4 or S5 mode is established. The tool-layer coordination claim is an SDK constructor path, not an agent-led policy decision.

## Recursion

Subagents have fresh history and their own model/tool cycles, but no independent governance or durable session; their nesting does not establish recursively viable organizations. The single primary composition is the chosen level. Cross-session workspace locks span a limited common process, not all deployed instances.

## Variety and escalation

Model tools, MCP, nested child work and provider protocols amplify response variety; path guards, scoped approvals, lock leases, depth/concurrency caps, tool budgets, session commit barriers and goal phases attenuate operational risk. Tool failure and blocked goal statuses are ordinary task feedback, not themselves an exceptional algedonic channel or independent audit.

## Evidence gaps

- The .NET 10 toolchain is unavailable in this reviewer environment; no pinned upstream build or dotnet test run is claimed. The repository's advertised 201 tests and comparison-suite results are not independently reproduced.
- No live model/provider or MCP endpoint was exercised; the assessment concerns the executable first-party tool/model interfaces and explicit control paths, not empirical task success.
- Resource-key read/write locks are instance-scoped; the process-shared exclusive-workspace path establishes bounded S2 coordination, not blanket protection for all concurrent edits or child execution.
- The SDK has optional memory injection and dynamic plugins, but no production wiring of prospective memory-generation decisions was found; an independent consuming host may provide extra S4 or S5 outside this boundary.

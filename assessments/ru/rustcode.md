---
harness_id: rustcode
project_name: RustCode
repository: https://github.com/LHagfoss/rustcode
review_ref: 5906f5c870c979a3d710dde5b7d2748aaff5d442
reviewed_at: 2026-10-26
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

# RustCode

## Review boundary

- System in focus: One user-operated RustCode coding session, including its own model/tool loop, optional native child threads and supported scheduled/remote entry points. A fleet of independent user sessions is not assumed to be one agent-governed organization.
- Purpose and identity: Inspect, modify and verify a real project in response to a bounded user goal.
- Relevant environment: Project files and toolchains, model responses, tool errors, long commands, context limits, child results, user permissions and external MCP services.
- Standard-distribution boundary: Packaged Rust engine and TUI, the shared ACP engine used by desktop clients, native subagent runtime, session/workspace storage, daemon job interface and documented remote controls at the frozen revision.
- Credited operating / distribution surfaces: [runtime turn](https://github.com/LHagfoss/rustcode/blob/5906f5c870c979a3d710dde5b7d2748aaff5d442/rustcode/engine/src/network/turn/mod.rs), [shipped agent instructions and tools](https://github.com/LHagfoss/rustcode/blob/5906f5c870c979a3d710dde5b7d2748aaff5d442/rustcode/engine/src/tools/schema.rs), [native delegation](https://github.com/LHagfoss/rustcode/blob/5906f5c870c979a3d710dde5b7d2748aaff5d442/rustcode/engine/src/network/subagents.rs), [supported modes](https://github.com/LHagfoss/rustcode/blob/5906f5c870c979a3d710dde5b7d2748aaff5d442/README.md).
- Adjacent first-party surfaces excluded from ownership: Repository AGENTS.md contribution/release organization, CI and tests, Codex research notes, and the explicitly proposed cross-session-orchestration design. External CLI agents invoked by delegate_task retain their own agent loops; their organization cannot be imported into RustCode.
- First-party operating / deployment modes considered: Build-mode interactive/headless coding, optional native children, read-only plan mode, ACP clients, local scheduled jobs and paired-device intervention. Plan-only use is not evidence of autonomous action.
- Recursion level: Coding session and its task workers; no claim about the RustCode development organization.
- Reviewed revision: `5906f5c870c979a3d710dde5b7d2748aaff5d442`.
- Observation date: 2026-10-26.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The Rust engine constructs provider requests from session history, receives model-selected tools, applies policy/approval, executes tools, appends real results and repeats until completion or interruption. File, search, shell, MCP, background-task and verification surfaces act on the project. The model may keep a todo plan and set a continuous goal; runtime lifecycle/context recovery preserves the operational conversation. The provider supplies inference rather than an independently borrowed coding-agent policy.

Native children have separate context and histories, bounded messages, model selection, result handoffs, cancellation and persisted status. Write-enabled children require explicit allowed paths and receive isolated Git workspaces; nesting remains read-only. The supervisor enforces concurrency with a semaphore. A separate delegate_task adapter invokes installed third-party coding CLIs or leaves a task file for manual handoff. Those external loops are not the basis for S1 here.

The daemon executes durable jobs with leases, conservative ambiguity recovery and user/agent job-management operations. Remote clients route prompts, steering and approvals to the session owner; the gateway does not run agent turns. Configuration, skills and user approvals constrain operation. Repository maintainer workflow and proposed future cross-session actors are separate from the shipped runtime.

## Operational model

The primary S1 is the model-backed project worker: it selects observations, edits, commands and recovery from actual feedback. Optional children are subordinate work cells. The runtime transports and enforces those choices; users retain goals and permissions. Subtask decomposition, concurrency ceilings and human session controls are not automatically whole-current organizational regulation.

## S1 — Operations

- State: A
- Function: Produce project investigation, source changes and verification results through a continuing decision/action loop.
- Disturbance / variety regulated: Unknown source, failed tools/tests, incomplete observations, changing context and alternative implementations.
- Decisive decision or feedback right: Choose the next source/tool/edit/check action and revise it after the actual result.
- Decision owner: RustCode's model-backed root or native worker within its user-approved scope.
- Supporting / enforcement mechanisms: Provider request/response transport, tool schemas, approval policy, shell/file execution, context recovery, session persistence and child supervisor.
- Closure path: Goal and source context → model tool decision → real execution/result history → model correction or next action → verified artifact/report. The runtime requests another round for tool responses rather than asking the human to select each operational step.
- Boundary reachability: README exposes the TUI and headless prompt modes; run_single_turn directly calls request collection, recovery, tool handling and final-response handling. Native child execution builds the same first-party tool policy and returns actual results.
- Why this is / is not agent-owned: Removing the model leaves execution and constraints but no substantive source-edit/recovery choice. Approval bounds a chosen action without replacing ordinary research/implementation discretion.
- Evidence: [turn dispatch](https://github.com/LHagfoss/rustcode/blob/5906f5c870c979a3d710dde5b7d2748aaff5d442/rustcode/engine/src/network/turn/mod.rs#L239), [tool-result feedback](https://github.com/LHagfoss/rustcode/blob/5906f5c870c979a3d710dde5b7d2748aaff5d442/rustcode/engine/src/network/turn/tools.rs), [first-party workflow instructions](https://github.com/LHagfoss/rustcode/blob/5906f5c870c979a3d710dde5b7d2748aaff5d442/rustcode/engine/src/tools/schema.rs#L2210), [child model loop](https://github.com/LHagfoss/rustcode/blob/5906f5c870c979a3d710dde5b7d2748aaff5d442/rustcode/engine/src/network/subagents.rs#L265).
- Basis: structural.
- Confidence: High for source wiring; no claim about empirical task quality.
- Caveats: Requires a configured provider and permissions; no live model run was performed.

## S2 — Coordination

- State: —
- Function: No material first-party inter-S1 conflict-resolution loop established at this session boundary.
- Disturbance / variety regulated: Candidate disturbance is concurrent workers changing overlapping project content or deadlocking while a parent waits.
- Decisive decision or feedback right: Work partition and later integration remain task-specific choices; no shipped conflict-specific negotiation/returned revision protocol was found.
- Decision owner: The task caller selects scope; runtime enforces workspaces, path restrictions and execution slots.
- Supporting / enforcement mechanisms: Isolated workspaces, allowed_paths, read-only nesting, bounded mailboxes and yielding a slot while waiting.
- Closure path: Child completion and metadata return to the caller, but do not themselves settle an inter-worker ownership/interface conflict.
- Why this is / is not agent-owned: Native spawn/message tools enable coordination to be programmed; that general possibility is not a differentiated S2 function or S2-specific constructor.
- Evidence: [native thread contract](https://github.com/LHagfoss/rustcode/blob/5906f5c870c979a3d710dde5b7d2748aaff5d442/docs/multi-agent.md), [write scope/workspace admission](https://github.com/LHagfoss/rustcode/blob/5906f5c870c979a3d710dde5b7d2748aaff5d442/rustcode/engine/src/network/subagents.rs#L1072), [supervisor](https://github.com/LHagfoss/rustcode/blob/5906f5c870c979a3d710dde5b7d2748aaff5d442/rustcode/engine/src/app/subagent_controller.rs).
- Basis: structural.
- Confidence: Medium.
- Caveats: Isolation materially reduces accidental interference; this finding does not deny its engineering value or a user-composed coordination protocol.

### Absence scope

- Surfaces inspected: Native subagent dispatcher/controller/context, supported multi-agent documentation, workspace creation/handoff and tool-system instructions.
- Plausible first-party paths checked: Overlap prevention through allowed_paths/worktrees, message/follow-up return, nested execution and semaphore wait yielding.
- Why no material first-party path remains: These isolate or sequence delegated work and transport results; the shipped instructions do not assign a conflict-specific discretionary reconciliation and return protocol among distinct workers. Future cross-session orchestration is explicitly design-only.

## S3 — Inside-and-now control

- State: —
- Function: No established whole-current regulatory owner over a differentiated operational organization in the assessed session.
- Disturbance / variety regulated: Candidate paths are child capacity, current todos, scheduled commitments and user steering.
- Decisive decision or feedback right: The root chooses task steps and children; configured runtime rules govern capacity/lifecycle. Neither constitutes a separate whole-current resource-bargaining or accountability function from delegation alone.
- Decision owner: Agent for local work; user/developer for configured ceilings and ordinary intervention.
- Supporting / enforcement mechanisms: list_agents/inspect_agent, todo priority, cancellation, semaphore, job history and remote session controls.
- Closure path: Task results and steering alter local work; no first-party whole-system control mandate/return loop is established by those controls.
- Why this is / is not agent-owned: A current task view and a cancel tool do not supply substantive organizational S3 discretion. A user prompt or configuration edit does not establish a parent S3 mode either.
- Evidence: [delegation tools and todo handling](https://github.com/LHagfoss/rustcode/blob/5906f5c870c979a3d710dde5b7d2748aaff5d442/rustcode/engine/src/network/subagents.rs), [daemon job contract](https://github.com/LHagfoss/rustcode/blob/5906f5c870c979a3d710dde5b7d2748aaff5d442/docs/daemon.md), [remote owner boundary](https://github.com/LHagfoss/rustcode/blob/5906f5c870c979a3d710dde5b7d2748aaff5d442/docs/remote.md).
- Basis: structural.
- Confidence: Medium.
- Caveats: A user can commission a richer organization; that custom mandate is outside the reviewed shipped arrangement.

### Absence scope

- Surfaces inspected: Root/child tool prompts and lifecycle, supervisor limits, task-plan tools, daemon and remote session documentation.
- Plausible first-party paths checked: Root supervision of children, current task priorities, scheduler job pause/resume and human remote intervention.
- Why no material first-party path remains: The supplied paths implement bounded task execution, job lifecycle and user control, without establishing whole-organization present-control choice and returned accountability. Proposed cross-session orchestration is not active source evidence.

## S3* — Complementary audit

- State: —
- Function: No differentiated complementary audit of operational claims established in the supplied arrangement.
- Disturbance / variety regulated: Child claims may be incomplete or incorrect; compiler/tests and raw workspace inspection can detect ordinary task faults.
- Decisive decision or feedback right: The root verifies its delegated task outputs; no dedicated independently controlled audit judgment/return protocol is shipped.
- Decision owner: Producing worker/root in the normal completion path; deterministic checks report facts.
- Supporting / enforcement mechanisms: Read-only explorer role, optional verification_command, compiler/check ledger and Git-status review manifest.
- Closure path: Verification errors feed the ordinary operational loop. A status manifest is not an independent audit verdict.
- Why this is / is not agent-owned: Separate context or a tool named review does not establish audit independence. The native roles are default/explorer/worker, not a packaged independent reviewer organization.
- Evidence: [role instructions](https://github.com/LHagfoss/rustcode/blob/5906f5c870c979a3d710dde5b7d2748aaff5d442/rustcode/engine/src/app/subagent_context.rs#L31), [manifest is Git status output](https://github.com/LHagfoss/rustcode/blob/5906f5c870c979a3d710dde5b7d2748aaff5d442/rustcode/core/rustcode-session/src/lib.rs#L1097), [root told to inspect child work](https://github.com/LHagfoss/rustcode/blob/5906f5c870c979a3d710dde5b7d2748aaff5d442/rustcode/engine/src/tools/schema.rs#L2228).
- Basis: structural.
- Confidence: Medium.
- Caveats: An explicitly instructed explorer could perform an audit in a custom setup; generic read-only access is not itself an S3*-specific constructor.

### Absence scope

- Surfaces inspected: Child role definitions, completion projection, session review-manifest writer, root verification instructions and turn verification feedback.
- Plausible first-party paths checked: Explorer as reviewer, parent inspection of child claims, verification command and Git manifest as complementary evidence.
- Why no material first-party path remains: The shipped roles and feedback are ordinary production verification and raw metadata; no distinct claim-relative independent audit judgment and corrective-control arrangement is supplied. Repository CI audits development, not the user session organization.

## S4 — Outside-and-then intelligence

- State: —
- Function: No established external/prospective capability-adaptation loop at the declared session recursion.
- Disturbance / variety regulated: Tools expose current project information; memory/context, skills and cron preserve or extend task execution.
- Decisive decision or feedback right: The root chooses how to solve the current goal; future capability strategy is not assigned to a shipped actor or function-specific primitive.
- Decision owner: User/developer for models, skill installations and scheduled purpose; agent for current work.
- Supporting / enforcement mechanisms: Skill loading, model profiles, MCP tools, persistence, context compaction and durable jobs.
- Closure path: Information feeds current task work; no prospective adaptation options/current-capability conversation is supplied by persistence or scheduling alone.
- Why this is / is not agent-owned: An agent can research a task or write a skill without thereby owning organization-level outside-and-then adaptation.
- Evidence: [configuration and skills](https://github.com/LHagfoss/rustcode/blob/5906f5c870c979a3d710dde5b7d2748aaff5d442/docs/configuration.md), [daemon](https://github.com/LHagfoss/rustcode/blob/5906f5c870c979a3d710dde5b7d2748aaff5d442/docs/daemon.md), [runtime workflow](https://github.com/LHagfoss/rustcode/blob/5906f5c870c979a3d710dde5b7d2748aaff5d442/rustcode/engine/src/tools/schema.rs).
- Basis: structural.
- Confidence: Medium.
- Caveats: Future custom research/strategy agents are not ruled out.

### Absence scope

- Surfaces inspected: Configuration/skill modes, current-goal/todo tools, scheduler and native root/child prompts.
- Plausible first-party paths checked: Skill discovery, model switching, persistent goals, scheduled sensing and context recovery.
- Why no material first-party path remains: These are operational extensibility and continuity paths, not a supplied external/future distinction → adaptation option → current-capability decision/return loop; no qualifying parent adaptation mode was found.

## S5 — Policy and identity

- State: —
- Function: No runtime identity/ultimate-policy issue arbitration and return path established.
- Disturbance / variety regulated: Permission requests, delegated write scope, pairing and project/user configuration constrain ordinary operation.
- Decisive decision or feedback right: Users approve operational actions and choose settings; no first-party identity-level referral/decision protocol is supplied.
- Decision owner: User for ordinary task permissions; not credited as a parent S5 merely for final operational authority.
- Supporting / enforcement mechanisms: Policy gates, read-only/worker roles, sandboxing, project instructions and device trust.
- Closure path: Approval returns permission for a concrete tool action, not resolution of identity or ultimate policy.
- Why this is / is not agent-owned: Static rules and access grants bound the agent without closing S5 autonomously or through a differentiated parent mode.
- Evidence: [policy execution](https://github.com/LHagfoss/rustcode/blob/5906f5c870c979a3d710dde5b7d2748aaff5d442/rustcode/engine/src/network/policy.rs), [delegation policy](https://github.com/LHagfoss/rustcode/blob/5906f5c870c979a3d710dde5b7d2748aaff5d442/docs/multi-agent.md), [user configuration](https://github.com/LHagfoss/rustcode/blob/5906f5c870c979a3d710dde5b7d2748aaff5d442/docs/configuration.md).
- Basis: structural.
- Confidence: High for the bounded distinction.
- Caveats: The user's larger institution can have S5; it is not supplied by this coding-session permission UI.

### Absence scope

- Surfaces inspected: Runtime policy/approval paths, native role restrictions, configuration and supported local/remote operator modes.
- Plausible first-party paths checked: Permission escalation, user goal revision, model/skill settings and device authorization as candidate parent governance.
- Why no material first-party path remains: All reviewed returned decisions concern ordinary execution/access. No identity/ultimate-policy matter, legitimate function-specific deciding authority and returned governing settlement is packaged at this recursion.

## Distributed OSS parent arrangement

Repository contributors govern development outside the assessed product session. Neither contributor AGENTS.md nor a user's private operating institution donates parent-mode S3/S4/S5 evidence to the distributed coding runtime.

## Self-hosted and non-human modes

Configured self-hosted providers, headless/ACP and daemon operation remain supported. They change transport and invocation, not the missing function-specific metasystem arrangements. Read-only plan mode and generic remote approval are not alternative positive parent modes.

## Recursion

Native children have meaningful local task discretion and a parent channel. Spawning up to three levels is not proof that each child has its own viable metasystem or that the root governs a whole enterprise.

## Variety and escalation

Model-selected recovery absorbs project/tool variety; approval, cancellation and context recovery bound it. Bounded child summaries can omit evidence, so the root is instructed to inspect source directly. Runtime limits and ambiguous daemon runs preserve operational uncertainty rather than establish higher functions.

## Evidence gaps

Static source assessment only: no live model, provider, macOS/iOS client or agent-quality experiment. Rust tooling is absent in this assessment environment, so upstream Rust tests were inspected but not executed. Methodology structural and Index deterministic validators check artifact integrity, not semantic truth or runtime effectiveness. Conclusions are bounded to the frozen distribution; user-authored roles, external CLIs and proposed cross-session design remain outside positive ownership.

---
harness_id: asi-code
project_name: ASI Code
repository: https://github.com/AloneMath/ASI-Code
review_ref: e16084df095aa4687236984c9ee7f5bfbe8bf34d
reviewed_at: 2026-10-10
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
status: proposed
autonomy_s1: A
autonomy_s2: ?
autonomy_s3: ?
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# ASI Code

## Review boundary

- System in focus: ASI Code first-party coding agent runtime in Rust, its model-driven auto tool loop, direct source/shell tools, optional coding subagents, session and checkpoint/recovery, and optional job-daemon task path where attached to coding execution.
- Purpose and identity: autonomously inspect and change software projects, execute coding tools, recover interrupted work, and return test/source observations.
- Relevant environment: source repository, shell/test outputs, user prompts/permissions, tool-result failures, subagent tasks, queued daemon jobs and local VCS state.
- Standard-distribution boundary: shipped Rust coding REPL/work/secure/review operations, subagent execution when invoked, coding auto-loop and agent daemon where it runs coding work; not unrelated GUI/3D/Unity/Blender integrations, user-provided agent teams, or separate autoresearch experiment products.
- Credited operating / distribution surfaces: src/main.rs coding REPL and subagent manager, src/runtime.rs model/tool calls, src/orchestrator/loop.rs coding auto-loop, src/orchestrator/scheduler.rs tool-call grouping, and first-party agentd code only to the extent it actually executes coding queue work.
- Adjacent first-party surfaces excluded from ownership: 2.0 desktop and game-engine automation extensions not invoked by coding workflow, autoresearch standalone run command, standalone web/voice, release CI and docs claims, user-supplied provider/MCP internals and external maintainer governance.
- First-party operating / deployment modes considered: direct coding REPL and work/secure/review, auto tool loop, configurable test feedback, optional subagents with real model/tool turns, manual worktree command, optional agentd queue service and policy controls.
- Recursion level: coding project (primary agent with separately task-executing subagents where explicitly spawned), excluding other first-party but adjacent desktop/3D/research products.
- Reviewed revision: e16084df095aa4687236984c9ee7f5bfbe8bf34d.
- Observation date: 2026-10-10.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

ASI Code is a first-party Rust coding CLI with provider-neutral model requests and its own tool execution, session state, project-change tracking and autonomous continuation. Its coding auto-loop extracts/partitions model-generated tool calls into sequential or concurrency-safe tool batches, executes results, records failures and asks the same model to continue or correct. Optional test feedback, enabled only by ASI_AUTO_TEST, invokes a native project test command after source changes; failure becomes a synthetic message to the same coder with a bounded repair budget. This is real local task feedback, not by itself independently governed complementary S3* audit.

The same package exposes a separate subagent manager in src/main.rs, with distinct configured provider/model, message history, synchronous or background task runs and optional tool-loop continuation. These child runs may be genuinely distinct coding operating units, but first-party write-interference regulation among them is not established. The worktree system is a standalone REPL slash operation for changing the current working directory; the subagent launcher inspected in this pinned revision constructs a Runtime and executes its message history without automatically assigning an isolated worktree to every concurrent write-capable child. Thus the existence of a worktree command and an agent roster cannot automatically substantiate S2 conflict damping. S2 is left unknown pending complete mode-level collision-control evidence, rather than credited from generic batching/scheduling.

An agentd daemon provides durable task queue, claiming, executor, heartbeat and checkpoint/result paths. These are actual first-party lifecycle mechanisms, but the source paths inspected do not separately prove a model-owned or constructor-closed current management loop that uses a whole-system picture to make discretionary allocation or exception decisions across active coding S1 cells. S3 is left unresolved rather than inferred from a queue, retries and job status.

The tool-called auto-review guard uses a deterministic per-tool severity scorer and configured off/warn/block threshold. It can block risky operations; it does not constitute a separate model auditor that independently evaluates actual completed code and imposes corrective return. S3* is therefore not credited. Product policy and security settings also do not establish S5 ultimate-policy authority.

Pinned source anchors: [src/main.rs](https://github.com/AloneMath/ASI-Code/blob/e16084df095aa4687236984c9ee7f5bfbe8bf34d/src/main.rs); [src/runtime.rs](https://github.com/AloneMath/ASI-Code/blob/e16084df095aa4687236984c9ee7f5bfbe8bf34d/src/runtime.rs); [src/orchestrator/loop.rs](https://github.com/AloneMath/ASI-Code/blob/e16084df095aa4687236984c9ee7f5bfbe8bf34d/src/orchestrator/loop.rs); [src/orchestrator/scheduler.rs](https://github.com/AloneMath/ASI-Code/blob/e16084df095aa4687236984c9ee7f5bfbe8bf34d/src/orchestrator/scheduler.rs); [src/agentd/service.rs](https://github.com/AloneMath/ASI-Code/blob/e16084df095aa4687236984c9ee7f5bfbe8bf34d/src/agentd/service.rs); [src/worktree.rs](https://github.com/AloneMath/ASI-Code/blob/e16084df095aa4687236984c9ee7f5bfbe8bf34d/src/worktree.rs).

## Operational model

An autonomous first-party coding agent can read/change a repository and use observed errors to choose subsequent actions. Optional subagents and daemon task runs introduce potentially richer organizational arrangements, but the first-party boundary and feedback rights for cross-unit coordination and whole-current control remain unproven. Deterministic action-risk policies and same-model test repair are supporting mechanisms, not independently deciding auditor/ultimate-policy actors.

## S1 — Operations

- State: A
- Function: Transform coding requests into autonomous model-chosen source edits, project investigation and shell/test results.
- Disturbance / variety regulated: Unknown code, changing tests, command errors, user coding goals and tool-result surprises.
- Decisive decision or feedback right: Select actual coding tool calls, evaluate outcomes and decide further edits or completion.
- Decision owner: Model-driven first-party Runtime and coding REPL auto-loop, with independent model/task children where explicitly launched.
- Supporting / enforcement mechanisms: Provider adapters, parser/scheduler, native source/bash tools, session state, sandbox and user permission guards, optional auto-test feedback.
- Closure path: Task → model reply/toolcalls → native executor reads/edits/runs source → result observed in runtime history → further model decision or final response; optional test failure reinjected to same actor.
- Boundary reachability: REPL/work coding path and standalone subagent execution in shipped src/main.rs call the real runtime and auto-loop implementations at the frozen revision.
- Why this is / is not agent-owned: Model retains bounded discretionary choice over local coding tools and repairs; hard gates constrain but do not own that discretion.
- Evidence: [src/main.rs](https://github.com/AloneMath/ASI-Code/blob/e16084df095aa4687236984c9ee7f5bfbe8bf34d/src/main.rs); [src/runtime.rs](https://github.com/AloneMath/ASI-Code/blob/e16084df095aa4687236984c9ee7f5bfbe8bf34d/src/runtime.rs); [src/orchestrator/loop.rs](https://github.com/AloneMath/ASI-Code/blob/e16084df095aa4687236984c9ee7f5bfbe8bf34d/src/orchestrator/loop.rs); [src/tools.rs](https://github.com/AloneMath/ASI-Code/blob/e16084df095aa4687236984c9ee7f5bfbe8bf34d/src/tools.rs).
- Basis: structural + explicit.
- Confidence: high.
- Caveats: Source implementation evidence does not establish benchmark performance or production reliability.

## S2 — Coordination

- State: ?
- Function: Potential damping of conflict between independent child coding agents, but the specific interference-to-coordination-to-return witness remains unresolved.
- Disturbance / variety regulated: Concurrent coding children could modify overlapping source paths or compete over project state.
- Decisive decision or feedback right: Subagent tasks are configured/launched by the parent; tool call scheduling is concurrency-safety grouping inside one auto-loop, not a demonstrated inter-child collision decision.
- Decision owner: Parent/user task configuration and first-party subagent manager; the actual S2 regulator, if any, is unproven.
- Supporting / enforcement mechanisms: Subagent manager, per-child histories, task events, standalone worktree command and native tool batching.
- Closure path: Child results return to manager/parent. A first-party multi-writer conflict check, ownership reservation, consensus, worktree isolation attached to child launch, or comparable return is not conclusively evidenced.
- Why this is / is not agent-owned: Real multiple agents alone do not establish S2; the worktree feature is user-invoked separately, so one must not borrow it as automatic child-work interference prevention.
- Evidence: [src/main.rs](https://github.com/AloneMath/ASI-Code/blob/e16084df095aa4687236984c9ee7f5bfbe8bf34d/src/main.rs); [src/worktree.rs](https://github.com/AloneMath/ASI-Code/blob/e16084df095aa4687236984c9ee7f5bfbe8bf34d/src/worktree.rs); [src/orchestrator/scheduler.rs](https://github.com/AloneMath/ASI-Code/blob/e16084df095aa4687236984c9ee7f5bfbe8bf34d/src/orchestrator/scheduler.rs); [src/orchestrator/loop.rs](https://github.com/AloneMath/ASI-Code/blob/e16084df095aa4687236984c9ee7f5bfbe8bf34d/src/orchestrator/loop.rs).
- Basis: structural + explicit.
- Confidence: medium for child execution and uncertainty of coordination.
- Caveats: No positive S2 state is claimed. A future targeted review of subagent workspace rules and scheduler can resolve this uncertainty.

## S3 — Inside-and-now control

- State: ?
- Function: Potential management of current coding workload across daemon tasks and background subagents; aggregate discretionary whole-current control is not resolved.
- Disturbance / variety regulated: Backlogs, failed jobs, unexpected worker stops, live resource use and competing coding task demands.
- Decisive decision or feedback right: Job queue claim, failure classification, retry, status and cancellation operate; a distinct agent/constructor/parent current-control judgment integrating current multi-S1 conditions is not demonstrated.
- Decision owner: Runtime-defined queue/service operator and human user; no evidenced autonomous whole-current decision owner.
- Supporting / enforcement mechanisms: agentd service, job queue, checkpoint, result store, retry/stop, bounded auto-loop steps and status reports.
- Closure path: A job is claimed, executed, completed/failed and recorded. This is task lifecycle, not necessarily a managerial whole-current reprioritization and return into active independent S1 units.
- Why this is / is not agent-owned: A scheduler, database and daemon health path can support S3 without owning organizational current-management judgment.
- Evidence: [src/agentd/service.rs](https://github.com/AloneMath/ASI-Code/blob/e16084df095aa4687236984c9ee7f5bfbe8bf34d/src/agentd/service.rs); [src/agentd/job_queue.rs](https://github.com/AloneMath/ASI-Code/blob/e16084df095aa4687236984c9ee7f5bfbe8bf34d/src/agentd/job_queue.rs); [src/agentd/executor.rs](https://github.com/AloneMath/ASI-Code/blob/e16084df095aa4687236984c9ee7f5bfbe8bf34d/src/agentd/executor.rs); [src/orchestrator/engine.rs](https://github.com/AloneMath/ASI-Code/blob/e16084df095aa4687236984c9ee7f5bfbe8bf34d/src/orchestrator/engine.rs).
- Basis: structural + explicit.
- Confidence: medium.
- Caveats: Requires focused review of live daemon decisions and actor authority before moving from ? to any positive autonomy claim.

## S3* — Complementary audit

- State: —
- Function: No separately owned first-party independent audit of S1 operations that closes corrective feedback.
- Disturbance / variety regulated: Risky shell/file tools and code defects are handled by action policy or current coder's test feedback.
- Decisive decision or feedback right: Configured severity thresholds warn or block based on a deterministic tool-risk score; optional project tests return pass/fail to the original coding model.
- Decision owner: Static policy configuration and same coder, not an independently accountable supplementary audit actor.
- Supporting / enforcement mechanisms: auto_review_decision and audit event logging, auto-test guards, self-heal retry bounds, optional review-mode task prompt.
- Closure path: Tool argument risk check may refuse operation; an opt-in failing test is returned as synthetic user feedback to the original model. No independent auditor judgment intervenes on actual code evidence and returns a separate corrective directive.
- Why this is / is not agent-owned: Review-mode branding, deterministic tool-risk score and same-model test-fix feedback do not suffice for S3*.
- Evidence: [src/runtime.rs](https://github.com/AloneMath/ASI-Code/blob/e16084df095aa4687236984c9ee7f5bfbe8bf34d/src/runtime.rs); [src/audit.rs](https://github.com/AloneMath/ASI-Code/blob/e16084df095aa4687236984c9ee7f5bfbe8bf34d/src/audit.rs); [src/orchestrator/loop.rs](https://github.com/AloneMath/ASI-Code/blob/e16084df095aa4687236984c9ee7f5bfbe8bf34d/src/orchestrator/loop.rs); [src/main.rs](https://github.com/AloneMath/ASI-Code/blob/e16084df095aa4687236984c9ee7f5bfbe8bf34d/src/main.rs).
- Basis: structural + explicit.
- Confidence: medium-high.
- Caveats: User-designed reviewer agents may create other organizations; no such independently closed first-party mode is inferred.

### Absence scope

- Surfaces inspected: Auto-review scoring, tool admission, audit events, review mode, optional test-fix loop and subagent role generic execution.
- Plausible first-party paths checked: Independent source-reading reviewer, complementary audit decision owner, separate judgment on finished code and corrective return to coder.
- Why no material first-party path remains: The implemented auto-review guard judges tool argument risk deterministically, and opt-in verification returns to the same coder; generic subagent prompts do not establish a packaged independent S3* audit channel.

## S4 — Outside-and-then intelligence

- State: —
- Function: No evidenced prospective environment-intelligence actor driving strategic change of the selected coding organization.
- Disturbance / variety regulated: Changing future technology and task environment may require capability adaptation beyond coding the current user project.
- Decisive decision or feedback right: Coding agent plans and investigates tasks, while user/developer controls models, plugins, skills and versions; no separate future-strategy authority shown.
- Decision owner: No first-party S4 coding-organization owner.
- Supporting / enforcement mechanisms: Memory, skills/plugins, compaction, optional research/autoresearch adjacent entrypoints and project context.
- Closure path: Context is recorded for later coding or adjacent research operations run separately; no prospective environmental option decision changes operating capabilities under a shared coding organization.
- Why this is / is not agent-owned: A research command in the same repository does not donate organizational future-intelligence closure unless attached to the assessed coding operating mode.
- Evidence: [src/memory.rs](https://github.com/AloneMath/ASI-Code/blob/e16084df095aa4687236984c9ee7f5bfbe8bf34d/src/memory.rs); [src/skills.rs](https://github.com/AloneMath/ASI-Code/blob/e16084df095aa4687236984c9ee7f5bfbe8bf34d/src/skills.rs); [src/autoresearch.rs](https://github.com/AloneMath/ASI-Code/blob/e16084df095aa4687236984c9ee7f5bfbe8bf34d/src/autoresearch.rs); [src/main.rs](https://github.com/AloneMath/ASI-Code/blob/e16084df095aa4687236984c9ee7f5bfbe8bf34d/src/main.rs).
- Basis: structural + explicit.
- Confidence: medium.
- Caveats: A wider research platform could support separate S4 claims under a different declared recursion and first-party integration proof.

### Absence scope

- Surfaces inspected: Coding runtime, project memory, skills/plugins, standalone research commands and source-adjacent desktop/game-engine tools.
- Plausible first-party paths checked: Future-environment observation, strategic alternatives/decision actor and automatic capability renewal returned to the coding agent organization.
- Why no material first-party path remains: Research/GUI tools are adjacent command surfaces rather than an evidenced strategic authority that governs and changes this coding session's organizational capabilities.

## S5 — Policy and identity

- State: —
- Function: No ultimate policy/organizational identity adjudication and binding return within the coding organization.
- Disturbance / variety regulated: Security, dangerous commands and explicit remote policy sync are task/action governance, not constitutional purpose tensions.
- Decisive decision or feedback right: Human configures policy, allow/deny thresholds and user settings; runtime enforces current tool restrictions.
- Decision owner: Operator and deterministic policy gate, not autonomous ultimate-policy actor.
- Supporting / enforcement mechanisms: User permission modes, remote policy sync, feature killswitches, worktree sandbox guards, audit log and tool-risk severity thresholds.
- Closure path: Allowed/refused tool actions or updated settings affect subsequent calls; no ultimate identity/purpose issue is decided by a legitimate governance actor and returned to overall organization.
- Why this is / is not agent-owned: Policy enforcement does not equal ownership of higher-level governance decisions.
- Evidence: [src/policy.rs](https://github.com/AloneMath/ASI-Code/blob/e16084df095aa4687236984c9ee7f5bfbe8bf34d/src/policy.rs); [src/permissions.rs](https://github.com/AloneMath/ASI-Code/blob/e16084df095aa4687236984c9ee7f5bfbe8bf34d/src/permissions.rs); [src/runtime.rs](https://github.com/AloneMath/ASI-Code/blob/e16084df095aa4687236984c9ee7f5bfbe8bf34d/src/runtime.rs); [src/security.rs](https://github.com/AloneMath/ASI-Code/blob/e16084df095aa4687236984c9ee7f5bfbe8bf34d/src/security.rs).
- Basis: structural + explicit.
- Confidence: medium-high.
- Caveats: OSS maintainer policies are a separate system and do not govern the end-user coding session as a first-party S5 layer.

### Absence scope

- Surfaces inspected: User permissions, safe mode, remote policy sync, tool-risk checker, audit events and session mode configuration.
- Plausible first-party paths checked: Identity/purpose conflict handling, legitimate highest-policy actor, ratification and binding organizational return across operating cells.
- Why no material first-party path remains: Current first-party controls enforce action-level security preferences, not higher-order identity/policy authority.

## Distributed OSS parent arrangement

Public development CI and project contributors are excluded from user coding-session ownership. External model services, MCP providers and optional research/GUI systems do not lend their organizational functions to the selected coding boundary by repository co-location.

## Self-hosted and non-human modes

The CLI's direct coding operation can be unattended in auto-loop mode. Optional background subagents and daemon tasks are genuine first-party execution, but positive higher-function ownership cannot be inferred from job runners alone.

## Recursion

The parent coder and separately launched coding subagents can constitute multiple S1 operations. Native scheduler tool batches, daemon job records and worktrees are supporting/control surfaces. Their inter-unit coordination and whole-current decision authority remain unknown pending complete mode-specific closure.

## Variety and escalation

Tool output/error feeds back into the same model; optional test failures trigger bounded self-heal attempts. The runtime blocks risky commands by configured severity and records receipts. These controls support stable coding but are not automatically S3*, S4 or S5.

## Evidence gaps

- S2 and S3 deliberately remain unresolved: positive inter-S1 collision regulation and discretionary whole-current supervision have not been established, and the potential first-party surface is richer than the inspected negative scope supports.
- S3* negative is limited to packaged auto-review and same-model code verification; independently designed external auditor workflows are not inferred.
- No performance, security efficacy or benchmark capability figures are inferred from descriptive source claims or test scripts.

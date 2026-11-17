---
harness_id: kybern
project_name: Kybern
repository: https://github.com/Tresnanda/kybern
review_ref: 7489196e4d63cde31a97e705e57f0dcdab889338
reviewed_at: 2026-11-17
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: C
autonomy_s4: ?
autonomy_s5: P
---

# Kybern

## Review boundary

- System in focus: Shipped Kybern daemon and desktop/CLI client organizing one project through its optional model-backed Coordinator plus delegated agent threads.
- Purpose and identity: Enable model-backed coding and research in a common project with isolated concurrent workers, traceable returns and an owner-governed project policy.
- Relevant environment: Local Git checkout, native coding-agent provider CLIs/SDKs, project owner and connected desktop/mobile controls.
- Standard-distribution boundary: Built-in daemon orchestrator, Coordinator role/tool guard, delegation/worktree engine, task/note stores, driver adapters and supported operator controls.
- Credited operating / distribution surfaces: Coordinator session and role instructions, first-party child delegation, project notes, task/run events, guarded Git tools and user policy cards.
- Adjacent first-party surfaces excluded from ownership: Upstream provider internals, ordinary Github maintainer workflows, CI/release/test fixtures, desktop design audit and user-built downstream extensions.
- First-party operating / deployment modes considered: One project with direct child agents, explicit project Coordinator and operator-supervised Coordinator settings. Disabled or uninstalled providers are not credited.
- Recursion level: One local project work organization; the Coordinator and delegated children operate within the project while its legitimate owner is the parent.
- Reviewed revision: 7489196e4d63cde31a97e705e57f0dcdab889338.
- Observation date: 2026-11-17.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

Kybern wraps provider-specific model sessions through driver adapters and exposes an ordinary chat runtime plus a project Coordinator. One Coordinator thread per project receives special instructions and selected first-party tools to plan, delegate, inspect, and land changes. Children have separate threads and may receive independent worktrees. The daemon persists task/run status and follows per-thread events; note and brief storage supplies durable project context. Push and PR creation can follow user-selected standing settings; merging a PR asks the owner every time. [Coordinator lead](https://github.com/Tresnanda/kybern/blob/7489196e4d63cde31a97e705e57f0dcdab889338/crates/kybern-daemon/src/orchestrator/lead.rs); [delegation engine](https://github.com/Tresnanda/kybern/blob/7489196e4d63cde31a97e705e57f0dcdab889338/crates/kybern-daemon/src/orchestrator/delegation.rs); [Coordinator Git guards](https://github.com/Tresnanda/kybern/blob/7489196e4d63cde31a97e705e57f0dcdab889338/crates/kybern-daemon/src/orchestrator/lead_git.rs); [task-run tracking](https://github.com/Tresnanda/kybern/blob/7489196e4d63cde31a97e705e57f0dcdab889338/crates/kybern-daemon/src/orchestrator/tasks.rs); [driver registry](https://github.com/Tresnanda/kybern/blob/7489196e4d63cde31a97e705e57f0dcdab889338/crates/kybern-drivers/src/registry.rs); [operating guide](https://github.com/Tresnanda/kybern/blob/7489196e4d63cde31a97e705e57f0dcdab889338/GUIDE.md).

## Operational model

The model-backed Coordinator decides whether to answer, delegate or follow up and routes child outcomes. Child agents decide concrete research and implementation actions inside the permission model supplied by their external provider runtime; Kybern contributes a first-party project-level harness around those sessions, not the provider's internal cognition. Worktree and Git paths detect actual integration conflicts, report them for repair, and preserve project state. The local human owner can control active work and is the ultimate source of durable project brief/delegation policy. The installed system does not imply a shared organization-wide controller across independently operated Kybern installations.

## S1 — Operations

- State: A
- Function: Deliver project tasks through model-backed agent turns and delegated work.
- Disturbance / variety regulated: Task requirements, source changes, tool observations and failed work demand discretionary choices.
- Decisive decision or feedback right: The Coordinator chooses whether to answer, delegate to a new child or send follow-up to an existing child; coding agents select their operational tools and edits.
- Decision owner: Model-backed Coordinator for project task dispatch and provider-backed coding/research child threads for execution. Provider services supply inference, not the project-level task-routing authority.
- Supporting / enforcement mechanisms: Provider-native session drivers, persisted transcript/task ledger, permission checks, tool interfaces, Git worktrees and result delivery.
- Closure path: Child outcome and status return to the parent thread; the Coordinator can inspect code, review the diff, integrate or delegate a correction, and the next work uses that result.
- Boundary reachability: The packaged daemon injects the Coordinator role, exposes delegate/status/wait/git to it and creates resumable child threads via shipped delegation code.
- Why this is / is not agent-owned: With the model-backed Coordinator and child removed, the daemon can keep sessions and apply constraints but cannot independently choose a task interpretation, investigation or coding change.
- Evidence: [Coordinator lead](https://github.com/Tresnanda/kybern/blob/7489196e4d63cde31a97e705e57f0dcdab889338/crates/kybern-daemon/src/orchestrator/lead.rs); [delegation engine](https://github.com/Tresnanda/kybern/blob/7489196e4d63cde31a97e705e57f0dcdab889338/crates/kybern-daemon/src/orchestrator/delegation.rs); [operating guide](https://github.com/Tresnanda/kybern/blob/7489196e4d63cde31a97e705e57f0dcdab889338/GUIDE.md) (project Coordinator and helper worktrees); [task-run tracking](https://github.com/Tresnanda/kybern/blob/7489196e4d63cde31a97e705e57f0dcdab889338/crates/kybern-daemon/src/orchestrator/tasks.rs).
- Basis: structural
- Confidence: high
- Caveats: A configured external provider binary or SDK is required for model action; the shipped Kybern session and coordination surface is the assessed delivery boundary, not an independent Kybern model.

## S2 — Coordination

- State: A
- Function: Prevent concurrent child contributions from overwriting or incorporating incompatible source changes.
- Disturbance / variety regulated: Two or more working agents can edit overlapping project files or leave conflicting branches; an unsafe integration would destabilize the shared checkout.
- Decisive decision or feedback right: Choose a delegated child/branch to integrate and, after a conflict result, decide which child should rebase/repair and how to reattempt integration.
- Decision owner: The model-backed Coordinator receives live child and merge evidence and selects subsequent requests. Git detects merge conflicts and refuses unsafe application; it does not decide the repair strategy.
- Supporting / enforcement mechanisms: Per-child Git worktrees, completion events, identity/branch checks, merge-tree preflight and all-or-none cross-repository conflict detection when possible.
- Closure path: Conflicting files and no-merge disposition are returned to the Coordinator; it can direct the child to reconcile branches before trying merge_child again. A clean merge changes the shared branch for later agents.
- Boundary reachability: The Coordinator has kybern_agent_status, kybern_thread_send and kybern_git; an isolated child receives a branch, and group merge results are delivered to the Coordinator in supported project mode.
- Why this is / is not agent-owned: Git decides whether a proposed merge is safe; the Coordinator decides which parallel work to admit, route for repair or reattempt. The autonomous judgment is conditional on the Coordinator operating mode.
- Distinct S1 units: Two or more delegated project workers operating in independent worktrees.
- Inter-S1 disturbance: Overlapping edits and out-of-date branches produce real merge conflicts; the shared checkout must remain coherent.
- Attenuating coordination relation: Reviewable branch isolation plus Coordinator-directed merge/repair responding to a concrete detected conflict.
- Feedback into subsequent S1 behaviour: The failed-merge error names conflicting files and instructs another agent repair, thereby changing its subsequent work before a new merge.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The inspected path recognizes overlapping branch changes, refuses conflicting integration, returns actual conflict evidence and provides a repair/retry loop, beyond simply transmitting messages.
- Evidence: [Coordinator Git guards](https://github.com/Tresnanda/kybern/blob/7489196e4d63cde31a97e705e57f0dcdab889338/crates/kybern-daemon/src/orchestrator/lead_git.rs) (lead_group_merge_child conflict preflight and returned paths); [delegation engine](https://github.com/Tresnanda/kybern/blob/7489196e4d63cde31a97e705e57f0dcdab889338/crates/kybern-daemon/src/orchestrator/delegation.rs); [operating guide](https://github.com/Tresnanda/kybern/blob/7489196e4d63cde31a97e705e57f0dcdab889338/GUIDE.md) (delegated worktrees and integration); [worktree lifecycle](https://github.com/Tresnanda/kybern/blob/7489196e4d63cde31a97e705e57f0dcdab889338/crates/kybern-daemon/src/orchestrator/worktrees.rs).
- Basis: structural
- Confidence: medium
- Caveats: Conflict-resolution discretion depends on a running model-backed Coordinator. No universal semantic reconciliation or deadlock-free concurrent scheduling is claimed.

## S3 — Inside-and-now control

- State: A(P)
- Function: Regulate present project task commitments and delegated agent allocation across one Coordinator-controlled project.
- Disturbance / variety regulated: Concurrent workers may be busy, failing, mis-scoped or blocked, while the project's current tasks and required work change.
- Decisive decision or feedback right: Inspect active delegated agents, task status and current code evidence; choose new work assignments, cancellations, follow-up questions and which completed work to accept. The project operator can instead intervene in the active conversation and task choices.
- Decision owner: Model-backed Coordinator for the active project portfolio in the base mode; local project owner/operator in the supervised mode.
- Supporting / enforcement mechanisms: Durable task-run events, active delegation views, child limits, project notes and worktree guards. Fixed concurrency limits do not themselves own task priorities.
- Closure path: Coordinator decisions invoke delegate/send/cancel or Git actions, affecting child work and later project branch state. Operator messages and task control return to the same project flow.
- Boundary reachability: The shipped Coordinator role is exposed by the daemon; the task ledger and child status/interrupt tools are available to it. A human can inspect and redirect these sessions in the packaged app.
- Why this is / is not agent-owned: The Coordinator chooses work based on current evidence. The daemon enforces configured limits and task-event transitions without itself choosing what the project should prioritize.
- Whole-system current view: One project's project notes, task items, Agent panel and returned results, rather than an organization-wide control plane across unrelated installations.
- Current-control decision scope: Live assignments, child coordination, interruption/cancellation and integration of completed contributions within one project.
- Evidence: [Coordinator lead](https://github.com/Tresnanda/kybern/blob/7489196e4d63cde31a97e705e57f0dcdab889338/crates/kybern-daemon/src/orchestrator/lead.rs); [delegation engine](https://github.com/Tresnanda/kybern/blob/7489196e4d63cde31a97e705e57f0dcdab889338/crates/kybern-daemon/src/orchestrator/delegation.rs); [task-run tracking](https://github.com/Tresnanda/kybern/blob/7489196e4d63cde31a97e705e57f0dcdab889338/crates/kybern-daemon/src/orchestrator/tasks.rs); [operating guide](https://github.com/Tresnanda/kybern/blob/7489196e4d63cde31a97e705e57f0dcdab889338/GUIDE.md) (project Coordinator, Agents panel, task views and operator steering).
- Basis: structural
- Confidence: medium
- Caveats: Parent-mode evidence is limited to an interactive project operator who can review work and redirect the Coordinator; ordinary PR-merge approval alone is not counted.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Model-backed project Coordinator | A project task/agent becomes ready, blocked or conflicting | Delegate, redirect, cancel or integrate changes and observe new task/child state | [Coordinator lead](https://github.com/Tresnanda/kybern/blob/7489196e4d63cde31a97e705e57f0dcdab889338/crates/kybern-daemon/src/orchestrator/lead.rs); [delegation engine](https://github.com/Tresnanda/kybern/blob/7489196e4d63cde31a97e705e57f0dcdab889338/crates/kybern-daemon/src/orchestrator/delegation.rs) |
| Parent (`P`) | Local project owner/operator | Current task or work priorities require direct intervention | Owner steers project Coordinator or active child via supported app; the next turn and work are altered | [operating guide](https://github.com/Tresnanda/kybern/blob/7489196e4d63cde31a97e705e57f0dcdab889338/GUIDE.md); [task-run tracking](https://github.com/Tresnanda/kybern/blob/7489196e4d63cde31a97e705e57f0dcdab889338/crates/kybern-daemon/src/orchestrator/tasks.rs) |

## S3* — Complementary audit

- State: C
- Function: Provide a distinct inspection route for changes asserted complete by an implementing agent.
- Disturbance / variety regulated: A worker can report success while uncommitted, conflicting or incorrectly implemented changes remain in its workspace.
- Decisive decision or feedback right: A separately delegated review agent can inspect code and diff as primary evidence and return a finding before the Coordinator commits/integrates.
- Decision owner: An independently instantiated reviewer child can own the judgment, but the Coordinator must instantiate that reviewer, supply scope and act on the returned finding; no unconditional audit policy was established.
- Supporting / enforcement mechanisms: Separate child thread/context, role-specific review model defaults, read-only research/review workspace mode, Git diff and explicit child-result return.
- Closure path: Reviewer result reaches the Coordinator, which can request further edits or withhold integration. A structural audit constructor is provided; mandatory autonomous reviewer dispatch/closure is not proven.
- Boundary reachability: The packaged delegation API accepts review roles and projects can configure a distinct review harness; the project Coordinator reads returned child results and Git evidence.
- Why this is / is not agent-owned: Review judgment is supplied by the separately created agent in the composed mode; merely presenting an operator review dock or unit-test status is not credited.
- Claim being audited: An implementer claims a task/branch is sufficiently complete to integrate.
- Ordinary reporting path: Implementing child final message, task status, and ordinary review from the Coordinator.
- Complementary access path: A separate reviewer child can inspect project source and diffs rather than relying on the implementer's final statement.
- Independence boundary: Separate child session and instructions, but the Coordinator can choose the reviewer and prompt; independent admission, mandatory invocation and application are not guaranteed by default.
- Who acts on findings: The project Coordinator requests repairs or declines a merge; human review is available separately.
- Evidence: [operating guide](https://github.com/Tresnanda/kybern/blob/7489196e4d63cde31a97e705e57f0dcdab889338/GUIDE.md) (review role defaults, worktrees and review before integration); [Coordinator lead](https://github.com/Tresnanda/kybern/blob/7489196e4d63cde31a97e705e57f0dcdab889338/crates/kybern-daemon/src/orchestrator/lead.rs) (delegated review and source verification); [delegation engine](https://github.com/Tresnanda/kybern/blob/7489196e4d63cde31a97e705e57f0dcdab889338/crates/kybern-daemon/src/orchestrator/delegation.rs) (distinct child sessions and result return).
- Basis: structural
- Confidence: medium
- Caveats: This is only a constructor-backed audit path, not a verified automatic independent S3* or a separate OpenSiro S3* audit.

## S4 — Outside-and-then intelligence

- State: ?
- Function: Potential prospective adaptation of later project work through durable lessons and reusable settings.
- Disturbance / variety regulated: New code, external provider behavior, recurring failures and changing project conventions may make earlier instructions obsolete.
- Decisive decision or feedback right: The Coordinator is instructed to record time-stamped gotchas, decisions and changed source realities and may propose modifications to standing settings.
- Decision owner: Potential Coordinator or parent operator depending on whether notes versus authority-setting changes matter; not fully resolved as one adaptation function.
- Supporting / enforcement mechanisms: Dated project notes, staleness checks, subsequent-session note index, explicit coordinator setup/settings proposals.
- Closure path: Persisted notes are exposed to later sessions; owner-approved settings affect subsequent child role selection. Whether this actually carries a future-directed outside-then organizational adaptation choice rather than ordinary context hygiene remains unresolved.
- Boundary reachability: Notes and approved settings belong to the supported daemon Coordinator mode.
- Why this is / is not agent-owned: The model writes some durable project observations, but a durable memory note by itself is not an S4 adaptation decision. The binding owner of prospective capability change is not sufficiently established.
- External distinction: Changed source, provider limitations and repeated project failures may be noticed.
- Future / prospective distinction: Later sessions inherit note indexes and role defaults.
- Adaptation option generated: New working conventions or role settings may be proposed.
- Path back into current capability / S3: Saved notes and approved settings are consumed by future Coordinator sessions; the function-specific adaptation judgment needs deeper reconstruction.
- Evidence: [Coordinator lead](https://github.com/Tresnanda/kybern/blob/7489196e4d63cde31a97e705e57f0dcdab889338/crates/kybern-daemon/src/orchestrator/lead.rs) (source freshness, notes, new-session context); [policy proposal and approval](https://github.com/Tresnanda/kybern/blob/7489196e4d63cde31a97e705e57f0dcdab889338/crates/kybern-daemon/src/orchestrator/lead_proposals.rs) (settings approvals); [operating guide](https://github.com/Tresnanda/kybern/blob/7489196e4d63cde31a97e705e57f0dcdab889338/GUIDE.md) (role defaults and memory).
- Basis: structural
- Confidence: low
- Caveats: Do not promote notes, project onboarding or generic provider switching into demonstrated autonomous adaptation.

## S5 — Policy and identity

- State: P
- Function: Constitute the local project working policy and delegation-of-authority envelope for its Coordinator and children.
- Disturbance / variety regulated: A project's standing purpose, required approvals and permitted agent autonomy can conflict with new tasks or environment expectations.
- Decisive decision or feedback right: Approve/edit the project brief and Coordinator defaults, including autonomous-start policy, model/role settings and permission to push or open PRs without asking.
- Decision owner: The legitimate project owner in the supported interactive configuration mode; the Coordinator proposes but cannot authoritatively rewrite the project brief or standing settings on its own.
- Supporting / enforcement mechanisms: Approval cards and persisted brief/settings, injection into subsequent Coordinator sessions, git authorization guards and per-project overrides.
- Closure path: User-approved brief and settings are saved and injected into the lead and child context, while subsequent Git push/PR requests obey the selected rule; PR merge still requires a fresh human approval.
- Boundary reachability: The shipped Coordinator setup and proposal tools are the first-party gateway for the policy; the daemon implements and updates session context after accepted changes.
- Why this is / is not agent-owned: The user, not the agent, makes the ultimate binding decision on the project brief and autonomy envelope. The model supplies proposals, not an independent S5 owner.
- Identity / ultimate-policy issue: What the project-wide Coordinator is for and which operations it may independently authorize for its project.
- Ultimate authority in each claimed mode: Local project owner/operator; no organization-wide public OSS maintainer authority is inferred.
- Return-to-operation path: Owner accepts proposal → persisted brief/settings → future Coordinator/child session instructions and Git permission decisions.
- Evidence: [Coordinator lead](https://github.com/Tresnanda/kybern/blob/7489196e4d63cde31a97e705e57f0dcdab889338/crates/kybern-daemon/src/orchestrator/lead.rs) (LEAD_ROLE and session prefix refresh); [policy proposal and approval](https://github.com/Tresnanda/kybern/blob/7489196e4d63cde31a97e705e57f0dcdab889338/crates/kybern-daemon/src/orchestrator/lead_proposals.rs); [Coordinator Git guards](https://github.com/Tresnanda/kybern/blob/7489196e4d63cde31a97e705e57f0dcdab889338/crates/kybern-daemon/src/orchestrator/lead_git.rs); [operating guide](https://github.com/Tresnanda/kybern/blob/7489196e4d63cde31a97e705e57f0dcdab889338/GUIDE.md) (setup and Coordinator settings).
- Basis: structural
- Confidence: high
- Caveats: A single task approval or PR merge is not itself S5; the positive claim is limited to durable local project policy selection.

## Distributed OSS parent arrangement

This assessment covers the operator's own installed project work cell, not repository-maintainer governance. Contributor and release approval evidence in the original GitHub repository is not credited as a parent control mechanism of arbitrary installations.

## Self-hosted and non-human modes

The local daemon, native drivers and agents can operate without manual steering for a delegated task. The separate supervised Coordinator mode retains the owner's brief and standing control of approvals. Provider- and model-specific tool restrictions differ: some drivers enforce the Coordinator's read-only tool set while Codex/Cursor use instructions only; this limits claims about guaranteed enforcement without negating the model's decision ownership.

## Recursion

Child coding/research threads own their operational assignments. The Coordinator handles present portfolio decisions for its project; the owner chooses the standing project authority envelope. No broader enterprise organizational recursion is claimed.

## Variety and escalation

The worktree system attenuates overlapping code edits; it returns concrete conflict evidence to the Coordinator for a corrective decision. Task-run state is persisted and returns to the parent. Action approvals, policy proposals and PR merge consent deliberately escalate to the local owner, not to an inferred autonomous policy actor.

## Evidence gaps

Review is source-based at the immutable pinned commit and does not assert live provider tests or independently observed project outcomes. S2 and S3 claims are conditional on selecting the shipped Coordinator mode with a functional external model; deterministic worktree/queue rules alone do not own decisions. S3* independent review is a composable route, not guaranteed invocation. The plausible note/settings learning path is not adequately established as a genuine outside-and-then capability adaptation closure, so S4 remains unknown rather than promoted from generic memory.

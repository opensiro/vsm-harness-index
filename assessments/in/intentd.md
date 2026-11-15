---
harness_id: intentd
project_name: Intentd
repository: https://github.com/intent-hq/intentd
review_ref: 1d20c2aefafe69395e1a2ec5a82fee988743a564
reviewed_at: 2026-11-15
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: ?
autonomy_s5: P
---

# Intentd

## Review boundary

- System in focus: One Intentd-managed development workspace on the standalone daemon, including a configured Maintenance Coordinator workgroup, its workers and reviewer.
- Purpose and identity: Organize software work and return verified results under an operator-defined workspace mandate.
- Relevant environment: The workspace repository, its users and forge observations, and configured agent providers.
- Standard-distribution boundary: Source-built Rust daemon, bundled specialist instructions, supported ACP provider sessions, task service, repository observation and agent-facing tools. An attached model is a normal prerequisite for agentic operation.
- Credited operating / distribution surfaces: Agent manager and ACP provider path, workspace notes and task graph, resource-scoped agent tools, bundled role catalog, forge monitoring and completion wakes.
- Adjacent first-party surfaces excluded from ownership: This repository's CI and test fixtures. The separate desktop product and private or deployment-only behavior supply no required witness. The updater is considered as a supporting distribution path.
- First-party operating / deployment modes considered: Local workspace sessions, batch delegation, built-in maintenance group and PR Reviewer, managed PR observation, and standalone sitter updates.
- Recursion level: One managed workspace and its current task portfolio. Worker sessions are S1 units. The operator is the parent at this recursion.
- Reviewed revision: 1d20c2aefafe69395e1a2ec5a82fee988743a564
- Observation date: 2026-11-15
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

The [public source](https://github.com/intent-hq/intentd/tree/1d20c2aefafe69395e1a2ec5a82fee988743a564) contains the daemon composition root, SQLite store and ACP client. Its service layer exposes task notes, child agent lifecycle and forge events through an installed MCP workspace API. The tool contract covers task relations, delegation, status and return of blocked or completed work to the controlling session. The daemon embeds [specialist definitions](https://github.com/intent-hq/intentd/blob/1d20c2aefafe69395e1a2ec5a82fee988743a564/crates/intent-services/src/specialists.rs#L226-L281), including a Developer, PR Reviewer and Maintenance Coordinator.

## Operational model

A lead agent or operator chooses the initial assignment. A configured Developer chooses actions within a workspace lane and records evidence in the task note. The coordinator compares active lanes, staged work and review findings to decide which work starts or returns for correction. In the maintenance mode the user owns the standing scope and permission envelope.

## S1 — Operations

- State: A
- Function: Carry out software development or verification within an assigned workspace lane.
- Disturbance / variety regulated: The changing code, diagnostics and tool feedback encountered during a task.
- Decisive decision or feedback right: Select edits, checks, responses to results and the completion outcome.
- Decision owner: The configured Developer or other ACP agent running the task turn.
- Supporting / enforcement mechanisms: AgentManager, provider sessions, workspace APIs, durable session and task state.
- Closure path: The task note drives a provider prompt. The worker acts on the workspace with its tools and returns updated task and session evidence to the caller.
- Boundary reachability: The daemon initializes the AgentManager and binds workspace tools to supported provider sessions, with the Developer bundled in the available specialist catalog.
- Why this is / is not agent-owned: The agent chooses the substantive operation in the assigned lane and reacts to tool results.
- Evidence: [Composition root](https://github.com/intent-hq/intentd/blob/1d20c2aefafe69395e1a2ec5a82fee988743a564/crates/intentd/src/main.rs#L2574-L2608), [ACP prompt and cancel](https://github.com/intent-hq/intentd/blob/1d20c2aefafe69395e1a2ec5a82fee988743a564/crates/intent-services/src/agent_manager/runtime.rs#L126-L151), [Developer role](https://github.com/intent-hq/intentd/blob/1d20c2aefafe69395e1a2ec5a82fee988743a564/crates/intent-services/resources/specialists/v3.8/developer.md).
- Basis: Pinned source and bundled operating instructions.
- Confidence: High.
- Caveats: Normal operation requires a configured provider.

## S2 — Coordination

- State: A
- Function: Regulate interference between concurrently assigned agents.
- Disturbance / variety regulated: Shared checkout or resource contention, duplicate work on the same task, and dependent work dispatched too early.
- Decisive decision or feedback right: Choose independent lanes, mark conflicts or dependencies and decide when to dispatch held work after completion.
- Decision owner: The coordinating agent using the workspace task graph, with task agents applying the bundled lane discipline.
- Supporting / enforcement mechanisms: Symmetric conflict admission, live task occupancy checks, isolated worktrees, the dependency gate and delivery-time unblocked hints.
- Closure path: Agent-selected constraints restrict the current batch. The returned hold and completion information changes the coordinator's next dispatch. Its decision starts a worker in a separate lane when the conflict clears.
- Boundary reachability: The active workspace tool surface exposes task relation edits, batch delegate and completion notifications. The provisioned Maintenance Coordinator supplies a bundled multi-lane actor.
- Distinct S1 units: Independently executing agents on separate workspace task notes.
- Inter-S1 disturbance: Overlapping active tasks, shared write locations and dependencies between task outcomes.
- Attenuating coordination relation: Conflict-aware hold and separated lanes followed by a completion-triggered re-evaluation.
- Feedback into subsequent S1 behaviour: The lead receives held and newly eligible tasks, chooses which worker to start next and directs that worker to its assigned worktree.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The first-party path names competing work and suppresses its concurrent execution, with an explicit return when the conflict clears.
- Why this is / is not agent-owned: The lead owns work separation, any change to the conflict relation and the next launch choice. The classifier applies the chosen relations.
- Evidence: [Batch conflict and dependency controls](https://github.com/intent-hq/intentd/blob/1d20c2aefafe69395e1a2ec5a82fee988743a564/crates/intent-services/src/agent_ops/batch.rs#L255-L350), [delivery-time readiness](https://github.com/intent-hq/intentd/blob/1d20c2aefafe69395e1a2ec5a82fee988743a564/crates/intent-services/src/agent_ops/ready_delta.rs#L191-L270), [workspace API contract](https://github.com/intent-hq/intentd/blob/1d20c2aefafe69395e1a2ec5a82fee988743a564/crates/intent-acp/src/mcp_server/tools.rs#L219-L242), [bundled lane protocol](https://github.com/intent-hq/intentd/blob/1d20c2aefafe69395e1a2ec5a82fee988743a564/crates/intent-services/resources/specialists/v3.10/maintenance-coordinator.md#L65-L81).
- Basis: Source plus the [first-party completion wake test definition](https://github.com/intent-hq/intentd/blob/1d20c2aefafe69395e1a2ec5a82fee988743a564/crates/intentd/tests/e2e_wss_unblocked_hints.rs#L1-L22).
- Confidence: Medium.
- Caveats: The conflict graph reflects the selected task relations. The lead can explicitly dispatch a held task individually.

## S3 — Inside-and-now control

- State: A
- Function: Regulate current commitments across the workspace workgroup.
- Disturbance / variety regulated: Blocked, contested or failed lane work, queue pressure and tradeoffs between outstanding commitments.
- Decisive decision or feedback right: Decide whether to start, defer, redirect or discontinue a lane and decide how current verification findings change the work plan.
- Decision owner: The bundled Maintenance Coordinator or lead agent at workspace recursion.
- Supporting / enforcement mechanisms: Spec ledger, task and agent views, child watches, forge status and descendant stop.
- Closure path: Current workgroup state and child wakes return to the lead. Its decision changes task assignments or retires a worker, and the resulting state is projected back into the pipeline.
- Boundary reachability: The specialist is embedded in the daemon's catalog. The agent-facing workspace tools expose the current evidence and the changes it can apply.
- Whole-system current view: Current task notes, sibling lanes and active workers, capacity and merge-readiness evidence for the workspace portfolio.
- Current-control decision scope: Allocate open lane capacity, redirect failed work and stop a delegated subtree within the approved mandate.
- Why this is / is not agent-owned: The coordinator chooses the live portfolio intervention. The service transports it into subsequent worker activity.
- Evidence: [Workspace snapshot and intervention tools](https://github.com/intent-hq/intentd/blob/1d20c2aefafe69395e1a2ec5a82fee988743a564/crates/intent-acp/src/mcp_server/tools.rs#L238-L263), [descendant stop implementation](https://github.com/intent-hq/intentd/blob/1d20c2aefafe69395e1a2ec5a82fee988743a564/crates/intent-services/src/agent_ops/descendants.rs#L14-L63), [coordinator wake priorities](https://github.com/intent-hq/intentd/blob/1d20c2aefafe69395e1a2ec5a82fee988743a564/crates/intent-services/resources/specialists/v3.10/maintenance-coordinator.md#L103-L120).
- Basis: Source reconstruction.
- Confidence: High.
- Caveats: Decisions reserved by the campaign mandate still require the operator.

## S3* — Complementary audit

- State: A
- Function: Independently inspect a lane's reported completion and return the findings to the current coordinator.
- Disturbance / variety regulated: A worker may report success despite unverified artifacts or a defect at the submitted head.
- Decisive decision or feedback right: Sample retained artifacts and the actual PR diff, form an independent verdict and direct findings into a fresh correction pass.
- Decision owner: A separately delegated verifier or PR Reviewer, with the Maintenance Coordinator acting on the findings.
- Supporting / enforcement mechanisms: Separate verification and review task notes tied to the head, scoped workspace and repository reads, review findings and completion wakes.
- Closure path: Separate actors inspect evidence. The reviewer records verdict and findings in task notes. The coordinator directs rework to the lane and repeats checks on the new head.
- Boundary reachability: Installed Maintenance Coordinator and PR Reviewer definitions are both embedded in the supported specialist bundle and can delegate through the native workspace API.
- Claim being audited: A lane's reported implementation and readiness for integration at the stated head.
- Ordinary reporting path: Developer evidence and status on the assigned lane note.
- Complementary access path: A separate session inspects retained evidence, runs relevant verification and examines the underlying diff and changed files.
- Independence boundary: The verification task is separate from the lane's task. The PR Reviewer is instructed to inspect the changes directly and delegate fixes to the producing path.
- Who acts on findings: The coordinator keeps the lane open, delegates correction and requires renewed review at the new head.
- Why this is / is not agent-owned: The reviewer decides what the evidence supports and the coordinator exercises the returned control decision.
- Evidence: [Separate verification and review tasks](https://github.com/intent-hq/intentd/blob/1d20c2aefafe69395e1a2ec5a82fee988743a564/crates/intent-services/resources/specialists/v3.10/maintenance-coordinator.md#L83-L98), [reviewer mandate and verdict](https://github.com/intent-hq/intentd/blob/1d20c2aefafe69395e1a2ec5a82fee988743a564/crates/intent-services/resources/specialists/v3.8/pr-reviewer.md#L8-L24), [returned correction path](https://github.com/intent-hq/intentd/blob/1d20c2aefafe69395e1a2ec5a82fee988743a564/crates/intent-services/resources/specialists/v3.8/pr-reviewer.md#L79-L87).
- Basis: Bundled role doctrine and source-backed execution path.
- Confidence: Medium.
- Caveats: Claim-relative independence is established by the separate task and evidence source. The review prompt supplies the reviewer role constraints.

## S4 — Outside-and-then intelligence

- State: ?
- Function: Use prospective external change to alter standing workspace capability.
- Disturbance / variety regulated: Future shifts in dependencies, provider choices or workspace needs.
- Decisive decision or feedback right: Select an adaptation based on anticipated environmental change and feed it into later workgroup capability.
- Decision owner: Unresolved for the shipped workspace boundary.
- Supporting / enforcement mechanisms: Forge observation, long-lived hooks, a Product Manager role, operator-approved settings and specialist proposals, and the channel updater.
- Closure path: A source-backed path across these surfaces from prospective sensing to a changed workgroup capability remains unresolved.
- Why this is / is not agent-owned: Built-in work can act on repository changes and propose settings or specialists. No agent-owned prospective choice and return could be attributed for the assessed workspace.
- Evidence: [Maintenance sources and dependency decisions](https://github.com/intent-hq/intentd/blob/1d20c2aefafe69395e1a2ec5a82fee988743a564/crates/intent-services/resources/specialists/v3.10/maintenance-coordinator.md#L42-L65), [Assistant proposal path](https://github.com/intent-hq/intentd/blob/1d20c2aefafe69395e1a2ec5a82fee988743a564/crates/intent-services/resources/specialists/v3.1/chief-of-staff.md#L10-L34), [release-channel installation](https://github.com/intent-hq/intentd/blob/1d20c2aefafe69395e1a2ec5a82fee988743a564/crates/intentd-sitter/src/updater.rs#L276-L325).
- Basis: Source comparison between maintenance, setup and prospective workspace adaptation.
- Confidence: Medium.
- Caveats: Built-in update checking responds to published release choices. The exact optional workflow coupling external evidence to durable workspace adaptation was not established.

## S5 — Policy and identity

- State: P
- Function: Set the durable mandate of a recurring maintenance workspace.
- Disturbance / variety regulated: A campaign can acquire additional repositories, action rights or purposes as new work appears.
- Decisive decision or feedback right: Authorize the campaign scope, exclusions, operating mode and reserved external commitments for subsequent iterations.
- Decision owner: The human operator supplies and can revoke the standing workspace mandate.
- Supporting / enforcement mechanisms: The operator question path, persistent Spec ledger and shipped Maintenance Coordinator instruction to apply the policy to later assignments.
- Closure path: The coordinator obtains scope and policy, persists the answers in the ledger and binds future task selection and lane instructions to that mandate. It returns a decision outside the mandate to the user.
- Boundary reachability: The bundled specialist reads and writes the workspace Spec, obtains the operator's answers through the provided question path or conversation and applies them when dispatching tasks.
- Identity / ultimate-policy issue: Which repositories and classes of work the maintenance workgroup exists to cover, and which commitments remain with the operator across recurring runs.
- Ultimate authority in each claimed mode: The user running the configured maintenance workgroup.
- Return-to-operation path: User's answers become the lasting ledger and constrain future task qualification and dispatch.
- Why this is / is not agent-owned: The coordinator proposes choices and implements the resulting policy. The operator supplies the operative scope and authority.
- Evidence: [Ledger selection and standing mandate](https://github.com/intent-hq/intentd/blob/1d20c2aefafe69395e1a2ec5a82fee988743a564/crates/intent-services/resources/specialists/v3.10/maintenance-coordinator.md#L21-L40), [policy transfer to each task](https://github.com/intent-hq/intentd/blob/1d20c2aefafe69395e1a2ec5a82fee988743a564/crates/intent-services/resources/specialists/v3.10/maintenance-coordinator.md#L65-L81).
- Basis: Source-backed actor and authority boundary in the installed maintenance mode.
- Confidence: Medium.
- Caveats: The mandate path applies to this specialist-led workspace mode. The daemon's general permission settings govern tool access.

## Recursion

Developer and verification lanes are separate operational cells. The workspace lead regulates the active portfolio. The operator authorizes the recurring workspace mandate, while forge authorities own their repository decisions.

## Variety and escalation

The daemon returns dependency holds, conflict holds and changed task readiness to the agent at workspace scale. Unresolved changes to the campaign envelope return to the parent operator.

## Evidence gaps

This is a pinned source review. Provider live behavior, compliance with specialist prompts and the current deployment status of the optional addressed review mode were not exercised. The autonomy vector does not depend on attributed ownership from that optional mode.

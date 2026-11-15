---
harness_id: houston
project_name: Houston
repository: https://github.com/theogmiguel/houston
review_ref: ade380fd1a4696c232c4f1fc671331b9a1ee08f3
reviewed_at: 2026-11-15
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: A
autonomy_s4: A(P)
autonomy_s5: P
---

# Houston

## Review boundary

- System in focus: One Houston-managed development workspace and its software workgroup, including its opt-in Night shift routine, managed task execution and operator controls.
- Purpose and identity: Sustain and improve the workspace's software capability through separately owned implementation, review and control paths.
- Relevant environment: Workspace repository, installed agent providers, available workstation resources, forge observations and configured competitors.
- Standard-distribution boundary: Local Rust daemon, desktop client, task and orchestration tools, selected CLI providers, workspace settings, routines and merge queue.
- Credited operating / distribution surfaces: PTY agent sessions, scoped orchestration, worktree conflict detection, independent task and Night shift reviews, Night shift setup and ledger, and the supported merge queue.
- Adjacent first-party surfaces excluded from ownership: Houston's own release and contributor CI, test fixtures and simulated provider sessions. Forge enforcement and provider internals remain external.
- First-party operating / deployment modes considered: Interactive orchestration, task review, manual workspace and queue controls, opt-in Night shift with pull-request output or configured merge queue.
- Recursion level: One workspace software operation with a portfolio of current and prospective changes. Workers are distinct S1 units. The workspace operator is its parent.
- Reviewed revision: ade380fd1a4696c232c4f1fc671331b9a1ee08f3
- Observation date: 2026-11-15
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

The desktop client attaches to a resident Rust daemon that owns PTYs, session records and the local agent-facing tool surface. The daemon persists task attempts, run ledgers and returned child results. Managed worktrees bound concurrent changes. Routines launch distinct workgroups, and the workspace queue can verify and land eligible revisions under the selected policy. [Operating overview][overview] · [Night shift runtime][runtime] · [Merge queue][queue]

## Operational model

Agents take separate workspace assignments and edit or inspect the target repository. A lead agent regulates active lanes and deals with shared-branch interference. Houston can launch separate reviewers and enforce their submitted verdicts in task flow. Workspace-level settings define the mandate under which a configured Night shift selects, verifies and returns changes.

## S1 — Operations

- State: A
- Function: Execute an assigned software task in a workspace or its managed worktree.
- Disturbance / variety regulated: Workspace conditions, implementation difficulties and feedback from local checks.
- Decisive decision or feedback right: Choose successive implementation and verification actions and report the resulting task outcome.
- Decision owner: The supported coding CLI agent launched for a task or delegated pane.
- Supporting / enforcement mechanisms: PTY session, provider launch setup, worktree creation, task acceptance items and durable handback.
- Closure path: A task becomes a prompt in a managed child. The agent acts on workspace feedback and submits a result that the daemon records and returns to the caller.
- Boundary reachability: The supported local daemon starts and binds the provider as part of the standard task execution path.
- Why this is / is not agent-owned: The provider-backed worker chooses edits and verification actions within the assigned scope.
- Evidence: [Daemon and provider boundary][overview] · [Task child binding][execute] · [Roster and handback][orchestration]
- Basis: Source and supported operating documentation.
- Confidence: High.
- Caveats: A supported executable and provider credentials must be provisioned.

## S2 — Coordination

- State: A
- Function: Regulate clashes between independently operating worktree agents.
- Disturbance / variety regulated: Parallel branches can change overlapping files, and simultaneous heavy verification can exhaust shared memory.
- Decisive decision or feedback right: Decide which agent should continue, be reassigned or work in sequence after a predicted clash.
- Decision owner: The orchestrator agent supervising the sibling worktrees.
- Supporting / enforcement mechanisms: Separate worktrees, periodic comparison against the base and sibling branches, a deduplicated inbox warning and a leased build slot.
- Closure path: Predicted branch and file conflicts reach the orchestrator. It can redirect a worker or sequence the affected assignments. The new assignments govern the siblings' subsequent work.
- Boundary reachability: The normal orchestration tool path creates managed worktrees and supplies the same lead with control and inbox feedback.
- Distinct S1 units: Independently acting child panes in registered worktrees.
- Inter-S1 disturbance: Committed branch overlap and simultaneous contention for the shared build resource.
- Attenuating coordination relation: Clash-specific feedback to the deciding lead, isolated edits and shared verification serialization.
- Feedback into subsequent S1 behaviour: The lead changes assignments and ordering in response to the reported branches and paths.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The daemon looks for interference between active sibling worktrees and names the concrete branches and files so the group can avoid it.
- Why this is / is not agent-owned: The lead determines the appropriate response. The conflict detector and the build lease enforce mechanics.
- Evidence: [Worktree conflict notification](https://github.com/theogmiguel/houston/blob/ade380fd1a4696c232c4f1fc671331b9a1ee08f3/docs/user/orchestration.md#L263-L292) · [Conflict comparison implementation][conflict] · [Build-slot lease][slot]
- Basis: Source-backed supported conflict and response path.
- Confidence: High.
- Caveats: The conflict watcher considers committed work and requires a compatible Git version.

## S3 — Inside-and-now control

- State: A(P)
- Function: Exercise current discretion over the active workspace campaign and its work plan.
- Disturbance / variety regulated: Blocked panes, failed acceptance gates, worker limits and changing commitments near the end of a run.
- Decisive decision or feedback right: Choose current lane allocation and corrective action, or change the live workspace portfolio and control its continuation as the operator.
- Decision owner: The lead agent in Night shift or ordinary managed orchestration. The user in the manual workspace and queue mode.
- Supporting / enforcement mechanisms: Workspace backlog, current pane roster, report and return channels, task control, queue state and workspace run controls.
- Closure path: The lead uses current lane and gate state to dispatch a fix, reassign or park the work. In the manual mode, operator selection of live work, queue pause, resume and handoff can change which active commitments continue.
- Boundary reachability: The installed routine builds an orchestrator brief and launches the lead. The same distribution provides operator task, run and queue controls.
- Whole-system current view: Workspace assignments, current worker roster and state, review outcomes and the current integration queue.
- Current-control decision scope: Choose which lane starts or receives corrective capacity, park blocked work, pause the queue and direct subsequent active effort.
- Why this is / is not agent-owned: The lead owns current discretionary intervention within the authorized routine. The operator independently controls current commitments in manual operation.
- Evidence: [Lead current-control doctrine][method] · [Night shift wiring][runtime] · [Operator backlog][tasks] · [Workspace queue intervention][queue]
- Basis: Installed operating modes and runtime return paths.
- Confidence: High.
- Caveats: The scheduled hard stop applies the operator's predetermined boundary.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Orchestrator agent | Portfolio state shows blocked or failed lanes and limited time or capacity | The agent redirects, parks or starts work and receives the updated lane and gate outcomes. | [Night shift method][method] |
| Parent (`P`) | Workspace operator | Current jobs or queue need an intervention | Operator selects task work, interrupts a run or changes the queue's current progress. Updated runtime and task state govern the next operations. | [Task view][tasks] · [Merge queue][queue] · [Routine controls][routines] |

## S3* — Complementary audit

- State: A
- Function: Independently verify a task or change against its acceptance claims.
- Disturbance / variety regulated: The implementation worker can mark work complete when the resulting diff or test evidence fails the acceptance criteria.
- Decisive decision or feedback right: Inspect the work directly and decide the claim-level or task-level verdict.
- Decision owner: The independently launched reviewer or Night shift verifier pane.
- Supporting / enforcement mechanisms: Read-only review execution, exact task acceptance and branch context, structured verdict, and a returned finding/rework path.
- Closure path: The independent actor checks the branch or reruns proofs. It sends its verdict to the lead and daemon. A failed review records a blocked state and can start a fresh implementation attempt.
- Boundary reachability: The task runtime can start review automatically at handback in a configured mode. Night shift provides a separate proof-verification path.
- Claim being audited: Implementer-reported readiness and the planned acceptance claims for the submitted work.
- Ordinary reporting path: The worker's structured completion or blocked result.
- Complementary access path: A different pane reads the actual diff, workspace files and tests or independently reruns the proof on the branch.
- Independence boundary: The task reviewer is a separate read-only child. The Night shift verifier is separate from both the worker and brief author.
- Who acts on findings: The orchestrator dispatches correction and the daemon records the gate result or runs configured rework.
- Why this is / is not agent-owned: The reviewer authoritatively chooses the verdict from independent evidence. Runtime state follows that verdict.
- Evidence: [Reviewer launch and branch path][review] · [Verdict and rework binding][settle] · [Installed verification instructions][method]
- Basis: Direct runtime paths and bundled verification protocol.
- Confidence: High.
- Caveats: Review configuration is opt-in and provider support varies.

## S4 — Outside-and-then intelligence

- State: A(P)
- Function: Turn prospective differences in the workspace's relevant environment into new available software capability.
- Disturbance / variety regulated: New competitor releases and behavior change which capabilities the workspace should develop next.
- Decisive decision or feedback right: Select an adaptation after cross-checking new capabilities against the local code and decide which verified changes enter the project.
- Decision owner: The Night shift agent selects and advances adaptations under a configured automatic verified queue. In the pull-request or manual queue mode the workspace operator decides which proposals enter capability.
- Supporting / enforcement mechanisms: Read-only scout tasks, competitor watermarks, fact-checked claims, isolated experiments, verification and an opt-in landing policy.
- Closure path: New external release evidence enters the ledger. The lead selects a candidate, changes the active work plan and dispatches it. Verified changes can become current project capability through the configured queue or the operator's decision. Later runs reread the landed and rejected outcomes.
- Boundary reachability: The installed Night shift brief provides the competitor survey, plan and return path. The workspace has both operator-driven and verifier-triggered landing modes.
- External distinction: Capabilities and behaviors in newer versions of selected competitor products.
- Future / prospective distinction: The agent identifies which observed capability gaps are worth addressing in future workspace development.
- Adaptation option generated: A ranked, testable capability change with claims checked against the project's existing implementation.
- Path back into current capability / S3: The proposed change becomes a current worker commitment, and verified adoption changes the workspace's baseline for the next run.
- Why this is / is not agent-owned: The Night shift agent chooses the change under the entrusted scope. In automatic mode deterministic queue gates implement the selection; in manual mode the parent decides whether it becomes part of the baseline.
- Evidence: [Scout, plan, build and verification](https://github.com/theogmiguel/houston/blob/ade380fd1a4696c232c4f1fc671331b9a1ee08f3/core/houston-core/src/night_shift/method.txt#L7-L51) · [Competitor cursor and output modes][routines] · [Manual or automatic verified adoption](https://github.com/theogmiguel/houston/blob/ade380fd1a4696c232c4f1fc671331b9a1ee08f3/docs/user/changes.md#L199-L225)
- Basis: A wired prospective mode and two declared ways to return its options into workspace capability.
- Confidence: Medium.
- Caveats: The competitor focus is optional. Automatic adoption requires compatible repository rules, enabled queue policy and all applicable gates.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Night shift orchestrator | New external capability within the authorized competitor scope | Select a verified adaptation and submit it to the opt-in automatic landing path. The new baseline and recorded disposition inform subsequent work. | [Night shift routine][routines] · [Verified queue][queue] |
| Parent (`P`) | Workspace operator | A capability proposal is returned in manual output mode | Operator chooses whether it enters the project. The resulting disposition and baseline enter the next run's ledger. | [Routine output and report][routines] · [Manual adoption][queue] |

## S5 — Policy and identity

- State: P
- Function: Establish the enduring mandate and delegated authority of the recurring Night shift workgroup.
- Disturbance / variety regulated: A recurring agent operation needs stable decisions about what it improves and who can commit changes across runs.
- Decisive decision or feedback right: Choose the standing direction, permitted focus, output authority and scope of future workgroup runs.
- Decision owner: The workspace operator through Night shift Setup and workspace policy.
- Supporting / enforcement mechanisms: Versioned saved routine settings, launch preflight, brief composition and runtime enforcement of the authorized output mode.
- Closure path: Operator choices persist. A later launch consumes them in the brief and enforces the selected operating and publication boundary across the run.
- Boundary reachability: This is the ordinary setup and launch path for the built-in routine.
- Identity / ultimate-policy issue: What the unattended workgroup exists to improve and what commitment authority it has across recurring runs.
- Ultimate authority in each claimed mode: The workspace operator changes and authorizes the persisted mandate.
- Return-to-operation path: Saved scope and output choices become the next run's direction, restrictions and active configuration.
- Why this is / is not agent-owned: The lead applies the mandate and refers decisions outside it to the operator.
- Evidence: [Setup and persistent direction][routines] · [Settings save](https://github.com/theogmiguel/houston/blob/ade380fd1a4696c232c4f1fc671331b9a1ee08f3/core/houston-core/src/daemon/night_shift.rs#L610-L665) · [Brief launch and binding][runtime]
- Basis: Source and installed workload identity control.
- Confidence: Medium.
- Caveats: The witness is scoped to the recurring Night shift workgroup.

## Recursion

The workspace contains independent worker, reviewer and verification cells. The lead coordinates and controls the current portfolio. The operator governs the durable mandate and enters the adaptation and current-control loops in separately supported modes.

## Variety and escalation

The daemon returns blocked status, branch clashes, provider limits and head-specific gate events. The Night shift ledger preserves decisions the agent cannot take, which reach the operator in its morning report.

## Evidence gaps

Pinned source and test definitions establish the operating paths. Provider calls, overnight work and external publication were outside this source review. Positive states depend on their documented operating modes and configuration.

[overview]: https://github.com/theogmiguel/houston/blob/ade380fd1a4696c232c4f1fc671331b9a1ee08f3/docs/internals/overview.md
[runtime]: https://github.com/theogmiguel/houston/blob/ade380fd1a4696c232c4f1fc671331b9a1ee08f3/core/houston-core/src/daemon/night_shift.rs#L1057-L1108
[queue]: https://github.com/theogmiguel/houston/blob/ade380fd1a4696c232c4f1fc671331b9a1ee08f3/docs/user/changes.md#L158-L225
[execute]: https://github.com/theogmiguel/houston/blob/ade380fd1a4696c232c4f1fc671331b9a1ee08f3/core/houston-core/src/daemon/tasks.rs#L4334-L4420
[orchestration]: https://github.com/theogmiguel/houston/blob/ade380fd1a4696c232c4f1fc671331b9a1ee08f3/docs/user/orchestration.md
[conflict]: https://github.com/theogmiguel/houston/blob/ade380fd1a4696c232c4f1fc671331b9a1ee08f3/core/houston-core/src/worktree_check.rs
[slot]: https://github.com/theogmiguel/houston/blob/ade380fd1a4696c232c4f1fc671331b9a1ee08f3/core/houston-core/src/build_slot.rs#L41-L133
[method]: https://github.com/theogmiguel/houston/blob/ade380fd1a4696c232c4f1fc671331b9a1ee08f3/core/houston-core/src/night_shift/method.txt
[tasks]: https://github.com/theogmiguel/houston/blob/ade380fd1a4696c232c4f1fc671331b9a1ee08f3/docs/user/tasks.md
[routines]: https://github.com/theogmiguel/houston/blob/ade380fd1a4696c232c4f1fc671331b9a1ee08f3/docs/user/routines.md
[review]: https://github.com/theogmiguel/houston/blob/ade380fd1a4696c232c4f1fc671331b9a1ee08f3/core/houston-core/src/daemon/tasks.rs#L4493-L4543
[settle]: https://github.com/theogmiguel/houston/blob/ade380fd1a4696c232c4f1fc671331b9a1ee08f3/core/houston-core/src/daemon/tasks.rs#L5312-L5430

---
harness_id: crossagents
project_name: CrossAgents
repository: https://github.com/L1nkkkk/CrossAgents
review_ref: 3699662a2bae328ef2226fb8229e7d2b3d1f388f
reviewed_at: 2026-11-20
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A(P)
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# CrossAgents

## Review boundary

- System in focus: an installed local CrossAgents Hub/runtime-host and one user-controlled Git repository and coding-work team (a Work/Run). User-supplied external model/CLI accounts are execution dependencies, not source-owned reasoning engines.
- Purpose and identity: turn the user's programming objective into a multi-session execution plan, run independent tasks in Git worktrees, verify changes, obtain an optional independent review and integrate/land only under configured local approval policies.
- Relevant environment: changing project source and test results, external model/CLI processes, local and remote agent sessions, finite quotas, Git integration state and operator questions.
- Credited operating / distribution surfaces: Rust hub and `crates/orchestrator/src` state machine, protocol and tools, `crates/core/src` policy, packaged CLI/GUI front ends, runtime-host and configured native/ACP backend adapters. External Claude/Codex/Gemini/Cursor and their model internals are excluded.
- Standard-distribution boundary: shipped Hub plus runtime-host and code worktree orchestration in GUI/CLI; automatic plan and checked execution, optional reviewer/escalation and human approval/landing modes; config-driven checks/permissions. No user-authored extension or new adapter is required for these first-party routes, but model credentials/executables and a Git repository are necessary.
- Adjacent first-party surfaces excluded from ownership: a plugin/model's own agent capabilities, repository CI beyond Hub-triggered local checks, documentation-only extension ideas, browser content encountered during ordinary coding, and CrossAgents' contributor organization as distinct from the installed local service.
- First-party operating / deployment modes considered: installed native/ACP agent Work with optional reviewer, user-approved multi-task plan, unattended continuation and CLI/GUI operation.
- Recursion level: the local project team, with one lead, multiple workers, optional reviewer and human owner; no Sx statement about multiple independent installed organizations.
- Reviewed revision: `3699662a2bae328ef2226fb8229e7d2b3d1f388f`.
- Observation date: 2026-11-20.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The Rust Hub explicitly owns deterministic coordination, state, scoped authorization, verification and Git worktree operations, while task understanding, planning, code editing and semantic review belong to configured CLI-backed agent sessions. Role names are assignments within a Work, not exclusive agent classes: one session can serve as a lead, worker or reviewer at different times. The runtime-host process can outlive and be reclaimed by a restarted Hub. The developer-visible workflow begins with a lead's submitted task plan, optional human plan approval including whole-run parallelism and per-task worker choices, followed by worktree dispatch, source-bound acceptance checks, optional reviewer verdict and lead's final acceptance; landing can be automatic, PR-only or human-gated.

Principal evidence: [English user README](https://github.com/L1nkkkk/CrossAgents/blob/3699662a2bae328ef2226fb8229e7d2b3d1f388f/README.en.md); [Hub execution and approval structure](https://github.com/L1nkkkk/CrossAgents/blob/3699662a2bae328ef2226fb8229e7d2b3d1f388f/crates/orchestrator/src/engine.rs); [deterministic concurrent task gates](https://github.com/L1nkkkk/CrossAgents/blob/3699662a2bae328ef2226fb8229e7d2b3d1f388f/crates/orchestrator/src/plan.rs); [task lifecycle and reporting](https://github.com/L1nkkkk/CrossAgents/blob/3699662a2bae328ef2226fb8229e7d2b3d1f388f/crates/orchestrator/src/tasks.rs); [first-party checks](https://github.com/L1nkkkk/CrossAgents/blob/3699662a2bae328ef2226fb8229e7d2b3d1f388f/crates/orchestrator/src/verify.rs); [independent diff review](https://github.com/L1nkkkk/CrossAgents/blob/3699662a2bae328ef2226fb8229e7d2b3d1f388f/crates/orchestrator/src/review.rs); [human decisions](https://github.com/L1nkkkk/CrossAgents/blob/3699662a2bae328ef2226fb8229e7d2b3d1f388f/crates/orchestrator/src/human.rs); [run landing](https://github.com/L1nkkkk/CrossAgents/blob/3699662a2bae328ef2226fb8229e7d2b3d1f388f/crates/orchestrator/src/landing.rs); [policy surface](https://github.com/L1nkkkk/CrossAgents/blob/3699662a2bae328ef2226fb8229e7d2b3d1f388f/crates/core/src/policy.rs).

## Operational model

Lead, worker and optional reviewer have distinct execution turn identities and decision domains. The Hub delegates and fences but contains no separate autonomous model: a working `A` decision comes from a first-party orchestrated model-backed session, not from Hub's deterministic rules. The same code paths can run with different runtime policies: for example, a person can control whole-plan allocation and safe landing, while a hands-off policy allows lead operation. An `A(P)` notation requires a distinct substantive parent mode, not the mere presence of a permission prompt.

## S1 — Operations

- State: A
- Function: plan-directed worker sessions carry out context-sensitive code edits, terminal/tool operations and task reporting in their own Git workspaces.
- Disturbance / variety regulated: unfamiliar code, changing task requirements, compilation failures, reviewer feedback and changing task outcomes.
- Decisive decision or feedback right: a worker chooses executable edits and repairs, tools and completion/blocked responses within its assigned scope; the lead may also execute a solo task.
- Decision owner: the configured native or ACP model-backed worker session under the Hub's source-native Work/Run contract. The external driver performs model execution; it does not supply the Hub's project task arrangement.
- Supporting / enforcement mechanisms: runnable role sessions, scoped Hub tools and tokens, isolated Git worktree, task creation/assignment/report, session host and task state.
- Closure path: worker returns changes and `task_complete`; Hub runs checks and returns failures to the same/new worker session with a concrete repair trace, with reviewer findings likewise fed back.
- Boundary reachability: packaged `crossagents run` or GUI Work creates the lead and worker task arrangement; no custom adapter implementation needed for built-in native drivers, though an authenticated provider is required.
- Why this is / is not agent-owned: without model-backed task actors, the Hub enforces static state/acceptance but cannot make substantive code or task-action choices.
- Evidence: [worktree tasks](https://github.com/L1nkkkk/CrossAgents/blob/3699662a2bae328ef2226fb8229e7d2b3d1f388f/crates/orchestrator/src/tasks.rs); [run creation and launch](https://github.com/L1nkkkk/CrossAgents/blob/3699662a2bae328ef2226fb8229e7d2b3d1f388f/crates/orchestrator/src/engine.rs); [first-party source README](https://github.com/L1nkkkk/CrossAgents/blob/3699662a2bae328ef2226fb8229e7d2b3d1f388f/README.en.md); [runtime-host handoff](https://github.com/L1nkkkk/CrossAgents/blob/3699662a2bae328ef2226fb8229e7d2b3d1f388f/crates/orchestrator/src/host.rs).
- Basis: structural and explicit.
- Confidence: high for configured installed agent sessions; source-only assessment, not live execution.
- Caveats: The model-backed worker requires a configured supported provider; the source-only review has not executed a live CLI session.
## S2 — Coordination

- State: C
- Function: attenuate interference between distinct S1 coder/reviewer work cells competing for source paths, Git integration/base state and shared build resources.
- Distinct S1 units: two or more separately assigned worker tasks with overlapping repository paths plus the reviewing/integration task chain.
- Inter-S1 disturbance: concurrent edits can clash in the same file, a worker can begin before a dependency is integrated, and concurrent builds can corrupt or block shared target directories.
- Attenuating coordination relation: `plan::scopes_overlap`, `ready_tasks` and predecessor/stage restrictions delay conflicting workers even when more slots are available; the Hub materializes distinct worktrees and acquires checkout/resource locks; integration/landing requires task and check states to be current.
- Feedback into subsequent S1 behaviour: a task does not start until dependencies/stages/scopes are compatible; failed checks or resource conflicts become bounded notices/retry/repair paths rather than silent parallel writes.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: source `ready_tasks` tests overlapping scopes across simultaneously active S1 cells, with concrete negative tests; it is a disturbance-specific inter-cell exclusion, not just dispatch or an event stream.
- Decisive decision or feedback right: gate conflicting work and revise runnable set against actual in-flight tasks.
- Decision owner: source-encoded deterministic Hub scheduler, lock and Git state machine; user/lead may choose scopes and max parallel but no evidence that an independent model owns the general coordination policy.
- Supporting / enforcement mechanisms: dependency graph, scope matcher, separate worktrees, resource locks, task acceptance and Git integration.
- Boundary reachability: built-in Hub/worktree path, not a custom extension.
- Evidence: [overlap and scheduling plus tests](https://github.com/L1nkkkk/CrossAgents/blob/3699662a2bae328ef2226fb8229e7d2b3d1f388f/crates/orchestrator/src/plan.rs); [resource-locked verification](https://github.com/L1nkkkk/CrossAgents/blob/3699662a2bae328ef2226fb8229e7d2b3d1f388f/crates/orchestrator/src/verify.rs); [Git workspace manager](https://github.com/L1nkkkk/CrossAgents/blob/3699662a2bae328ef2226fb8229e7d2b3d1f388f/crates/orchestrator/src/workspace.rs); [dependency-aware task operations](https://github.com/L1nkkkk/CrossAgents/blob/3699662a2bae328ef2226fb8229e7d2b3d1f388f/crates/orchestrator/src/tasks.rs).
- Basis: structural.
- Confidence: high.
- Caveats: `C` reflects a genuine first-party S2 control relation but no autonomous decision over dynamic coordination-policy redesign.
- Disturbance / variety regulated: Contending worker file edits, stale dependency commits and shared verification resources can interfere across separate S1 cells.
- Closure path: A pending task waits on overlap/merge/stage gates; once releases occur the scheduler re-admits that worker into its separate worktree.
- Why this is / is not agent-owned: The coordination path is first-party and interference-specific, but the Hub's deterministic Rust scheduler makes the scope-conflict decisions, not an autonomous coordinator.
## S3 — Inside-and-now control

- State: A(P)
- Function: keep the current whole Work/Run coherent: build and adapt a task graph, select workers, handle check/review failures, arbitrate blocked tasks, decide next assignments and final integration readiness.
- Disturbance / variety regulated: competing task demands, model/account limits, incomplete work, failed acceptance checks and occupied role sessions.
- Whole-system current view: the lead holds the run's planning/tool context, task reports, dependency and reviewer outcomes, pending human cards and resume/continuation snapshots; the deterministic Hub supplies actual state.
- Current-control decision scope: the lead's model-backed session submits/revises task plans, assigns worker/reviewer roles, makes task accept/rework/drop decisions and escalates/checks the result, not merely records worker messages.
- Decisive decision or feedback right: choose the present allocation/intervention and next work after evidence comes back across work cells.
- Decision owner: model-backed lead session; Hub only enforces the chosen plan, limits and checks.
- Distinct parent mode: `Approval` in `engine.rs` explicitly accepts a human-selected `RunPolicy`, `max_parallel` and per-task `assignees`; a plan requiring human approval does not begin work until that owner decision is returned to the live Run. This is substantive whole-run allocation, not a generic shell approval.
- Supporting / enforcement mechanisms: validated plan DAG, agent/session claims, status transitions, budget/quotas, continuation notices and current-check gating.
- Closure path: task results/checks/reviewer decisions return to the lead, which submits new task/acceptance interventions; in parent mode the approved/modified task-owner and parallelism allocations become the Hub's executable plan.
- Boundary reachability: shipped `run approve` and GUI human plan form; base mode uses packaged agent tools; model CLI account needed for actual decisions.
- Evidence: [run-wide Approval fields and run control](https://github.com/L1nkkkk/CrossAgents/blob/3699662a2bae328ef2226fb8229e7d2b3d1f388f/crates/orchestrator/src/engine.rs); [ready-task decision support](https://github.com/L1nkkkk/CrossAgents/blob/3699662a2bae328ef2226fb8229e7d2b3d1f388f/crates/orchestrator/src/plan.rs); [human plan and Work decisions](https://github.com/L1nkkkk/CrossAgents/blob/3699662a2bae328ef2226fb8229e7d2b3d1f388f/crates/orchestrator/src/work.rs); [task decision tools](https://github.com/L1nkkkk/CrossAgents/blob/3699662a2bae328ef2226fb8229e7d2b3d1f388f/crates/orchestrator/src/tasks.rs); [resume and escalation](https://github.com/L1nkkkk/CrossAgents/blob/3699662a2bae328ef2226fb8229e7d2b3d1f388f/crates/orchestrator/src/continuation.rs).
- Basis: structural and explicit.
- Confidence: medium-high.
- Caveats: human plan changes constitute the bounded parent S3 mode; individual tool approval does not.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Model-backed lead | Live plan, tasks and verification outcomes | Plan or rework/acceptance command changes current task run | `engine.rs`, `tasks.rs` |
| Parent (`P`) | Human owner reallocating plan assignments/policy/parallelism | Proposed Work plan awaits approval | Human-selected `Approval` applied to executable task state | `engine.rs`, `work.rs` |
- Why this is / is not agent-owned: The model-backed lead selects substantive current-plan and intervention changes; static quota/verification checks only enforce those choices.
## S3* — Complementary audit

- State: A
- Function: challenge a completed code task using complementary actual Git diff and acceptance evidence before accepting/integrating it.
- Claim being audited: a worker's implementation and task-complete report are fit for the declared task.
- Ordinary reporting path: worker's `task_complete`, report and verification checks returned through Hub.
- Complementary access path: optional reviewer is assigned a *separate* session with its own review round; receives the concrete diff and verified commit SHA (not only worker's narrative), submits structured `review_submit` verdict with identified P0–P3 findings and which commit was reviewed.
- Independence boundary: reviewer has its own session role and direct source/diff access, not the worker's arbitrary completion comment; the user may choose the same provider/model family, so semantic independence is structural, not statistically certified.
- Who acts on findings: Hub verifies verdict/finding consistency (P0 blocks merge) and ties it to the reviewed SHA; a change request returns to the worker for a bounded next iteration, while a pass unlocks the lead's acceptance. Disputes go to lead intervention, not automatic suppression.
- Decisive decision or feedback right: code-quality judgment based on complementary source evidence, distinct from ordinary done status.
- Decision owner: separately configured model-backed reviewer in the ordinary shipped review mode; deterministic parser/checks alone do not create the substantive review judgment.
- Closure path: `after_verified` directly opens a reviewer round when `reviewer_template` or Run reviewer is configured; the Hub routes findings back and revalidates commit identity; standard CLI `--reviewer` and GUI route, no developer-authored plugin.
- Evidence: [review verdict/finding semantics and return](https://github.com/L1nkkkk/CrossAgents/blob/3699662a2bae328ef2226fb8229e7d2b3d1f388f/crates/orchestrator/src/review.rs); [review tool, report and work return](https://github.com/L1nkkkk/CrossAgents/blob/3699662a2bae328ef2226fb8229e7d2b3d1f388f/crates/orchestrator/src/tasks.rs); [reviewer role selection](https://github.com/L1nkkkk/CrossAgents/blob/3699662a2bae328ef2226fb8229e7d2b3d1f388f/crates/orchestrator/src/engine.rs); [verification evidence source](https://github.com/L1nkkkk/CrossAgents/blob/3699662a2bae328ef2226fb8229e7d2b3d1f388f/crates/orchestrator/src/verify.rs).
- Basis: structural.
- Confidence: high as available review mode; not asserted in reviewer-disabled runs.
- Disturbance / variety regulated: A task may be marked complete although its patch contains defects unseen by ordinary worker reporting or basic deterministic checks.
- Supporting / enforcement mechanisms: Reviewer identity and Git reviewed SHA are persisted with structured findings; verdict freshness and rework routing are enforced by the Hub.
- Why this is / is not agent-owned: A distinct model-backed reviewer can make semantic judgments on the original Git diff; Hub SHA checks by themselves would be deterministic support.
- Caveats: Optional reviewer sessions are required for this state; same-worker self-review, unconfigured mode and deterministically run tests alone do not qualify.
- Boundary reachability: The installed run accepts a reviewer option and opens a separate review session after verified completion; no custom extension must be implemented.
## S4 — Outside-and-then intelligence

- State: —
- Function: an in-boundary prospective intelligence controller that samples the *external* future environment, constructs strategic adaptation options and returns selected changes into present whole-system commitments.
- Missing control path: the shipped `expertise` candidate/evaluation/acceptance workflow learns from completed internal task attempts and local lessons; the `continuation` watcher restarts *current* task progress; the browser and Web/ACP tools are available to ordinary S1 tasks, not a dedicated ongoing external-horizon future-option owner. No first-party S4 planning/adaptation episode or trigger found in the inspected shipped orchestration, expertise, policy and task code paths.
- Missing decision owner: a human may accept/reject an expertise lesson and any agent may research in its assigned task, but no source-supported role has decisional authority to compare future external opportunities and choose portfolio adaptation for this local team.
- Missing return/closure: saved internal expertise is recalled in subsequent coding contexts; it is not a forward-looking outside-signal proposal whose adoption alters the governing work/capability plan. Human accepting a lesson is not a future-adaptation transaction.
- Evidence: [internal-only candidate origin and human acceptance](https://github.com/L1nkkkk/CrossAgents/blob/3699662a2bae328ef2226fb8229e7d2b3d1f388f/crates/orchestrator/src/expertise/candidates.rs); [stale/conflict maintenance](https://github.com/L1nkkkk/CrossAgents/blob/3699662a2bae328ef2226fb8229e7d2b3d1f388f/crates/orchestrator/src/expertise/maintain.rs); [current-work continuation only](https://github.com/L1nkkkk/CrossAgents/blob/3699662a2bae328ef2226fb8229e7d2b3d1f388f/crates/orchestrator/src/continuation.rs); [Hub task orchestration](https://github.com/L1nkkkk/CrossAgents/blob/3699662a2bae328ef2226fb8229e7d2b3d1f388f/crates/orchestrator/src/engine.rs); [policy surface](https://github.com/L1nkkkk/CrossAgents/blob/3699662a2bae328ef2226fb8229e7d2b3d1f388f/crates/core/src/policy.rs).
- Basis: bounded source absence, not assertion that future features/extensions are impossible.
- Confidence: medium for this pinned standard distribution and local recursion.
- Falsifier: a first-party, shipped external environmental-signal-to-prospective adaptation decision plus an executable return into the team's current commitments would change this state.
- Disturbance / variety regulated: Future changes in external technology, project landscape and available capabilities would require a prospective organizational adaptation channel.
- Decisive decision or feedback right: An owner would need to select an external-signal-informed future response and return a new current operating capability; this right is not established.
- Decision owner: No first-party future-intelligence decision maker has been identified within the shipped local Work/Run mode.
- Supporting / enforcement mechanisms: Browser and expertise tools support present coding and internal retrospection, not a shipped prospective adaptation controller.
- Closure path: No first-party external future signal → candidate option → endorsed capability change → present-S3 feedback chain was found.
- Why this is / is not agent-owned: User-authored extensions could add an S4 actor, but the standard shipped system only supplies immediate task tools and retrospective experience.
- Caveats: Bounded source absence, not a claim about all third-party extensions, future releases or external coding models.

### Absence scope

- Surfaces inspected: first-party work/continuation controllers, browser adapters, expertise/lessons, extensions and external-provider integration paths.
- Plausible first-party paths checked: browser web access, retrospective expertise, unattended continuation and configurable extensions; no shipped external-prospective adaptation actor with current-operation return was established.
- Why no material first-party path remains: source-supported mechanisms either serve current coding, internal retrospective learning or caller-supplied extensions, without future-oriented autonomous adaptation closure.
## S5 — Policy and identity

- State: —
- Function: an ultimate identity/constitutional-policy authority for the installed local team, with a distinct policy-conflict trigger and returned decision binding the operating S3/S4 loops.
- Missing control path: `RunPolicy` governs tool approvals, plan timing, budgets and landing; `human_ask` resolves immediate execution questions; no source-native identity-policy dispute or S3–S4 tension instance is raised to an accountable final policy owner in the shipped Work/Run domain.
- Missing decision owner: a user can set run policies and approve plans/landings, but those are concrete execution/work allocation decisions; the code does not establish a separate local-team *ultimate purpose* decision authority or constitution-review role.
- Missing return/closure: permission and landing approvals are applied to an existing run and do not show a final identity-policy ruling returning to reconstitute the team's governing objective and its future/current control contracts.
- Evidence: [explicit run policy types and scope](https://github.com/L1nkkkk/CrossAgents/blob/3699662a2bae328ef2226fb8229e7d2b3d1f388f/crates/core/src/policy.rs); [human question/approval route](https://github.com/L1nkkkk/CrossAgents/blob/3699662a2bae328ef2226fb8229e7d2b3d1f388f/crates/orchestrator/src/human.rs); [operational permission decisions](https://github.com/L1nkkkk/CrossAgents/blob/3699662a2bae328ef2226fb8229e7d2b3d1f388f/crates/orchestrator/src/approval.rs); [integration landing decisions](https://github.com/L1nkkkk/CrossAgents/blob/3699662a2bae328ef2226fb8229e7d2b3d1f388f/crates/orchestrator/src/landing.rs); [work creation/approval](https://github.com/L1nkkkk/CrossAgents/blob/3699662a2bae328ef2226fb8229e7d2b3d1f388f/crates/orchestrator/src/work.rs).
- Basis: bounded source absence.
- Confidence: medium; claims about an external user's organization are outside this local installed-system recursion.
- Falsifier: an issue-triggered ultimate-policy decision with explicit binding return into current S3 and prospective S4 rather than another command/permission setting.
- Disturbance / variety regulated: Long-term identity or ultimate-purpose conflicts across the local team would require binding higher-level policy resolution.
- Decisive decision or feedback right: Issue-triggered ultimate-policy authority returning a binding new governing direction is not present at this recursion.
- Decision owner: The user controls plans, tools and permissions, but no distinct in-boundary ultimate-policy adjudicator/return loop is established.
- Supporting / enforcement mechanisms: RunPolicy and human approvals enforce immediate work-level constraints; they do not arbitrate constitutional identity.
- Closure path: No local policy/identity dispute → ultimate-authority resolution → changed S3/S4 governing direction return is evidenced.
- Why this is / is not agent-owned: Project run approvals and public OSS maintainer choices are different recursion/decision scopes, not the team's shipped S5 function.
- Caveats: A user's external organization may have ultimate policy, but its authority is outside this standalone installed Work/Run review.

### Absence scope

- Surfaces inspected: local RunPolicy, work planning and human approval, scoped permissions, expertise conflicts, operator settings and adjacent public contributor governance.
- Plausible first-party paths checked: human approval/landing, account/team policies, project expertise, and lead permissions; none handles ultimate identity-policy disputes with a binding return.
- Why no material first-party path remains: these paths decide individual current work and execution safety, not a genuine identity-policy issue → ultimate ruling → re-governed S3/S4 loop.
## Distributed OSS parent arrangement

The public source repository and release organization ship software but do not have an evidenced authority path into independent installed user's local project-team policy disputes. Human approval in the Work UI is a local parent S3 arrangement, not the OSS maintainers becoming this run's S5.

## Self-hosted and non-human modes

CrossAgents can keep executing through the runtime-host while Hub restarts, can continue stuck work and can run hands-off with policy caps. Those options demonstrate persistence/current S3 execution, not independent S4 or S5 policy authority. A user may instead gate plan allocation, permissions and final landing. Code-only/no-review runs do not receive autonomous S3* credit; the available reviewer mode does.

## Recursion

A Work/Run is the assessed recursion. Lead and multi-worker task cells supply lower recursion S1 operations; conflict gates connect cells; team-wide current control is the lead plus optional human plan authority; the reviewer provides a complementary raw-diff audit. Other projects connected to the same Hub may be independent recursions; their mere listing does not prove another super-system S3.

## Variety and escalation

Source variation goes to S1 workers. Scope/dependency/build interference is attenuated by deterministic S2 gates. Active work failures/checks/reviews return to S3 lead interventions, with explicit escalation and human policy/plan/landing options. Optional S3* reviewer inspects raw Git material independently. Neither retrospective expertise nor task browser access establishes a first-party outside-and-then adaptation loop, and no identity-policy return is shown at S5.

## Evidence gaps

This is a frozen-source structural review; the actual Rust Hub/desktop, third-party model accounts and full integration tests were not executed. Reviewer independence and effectiveness were not measured. Deterministic local shell acceptance tests are valuable but not automatically an agent-owned S3* judgment without the optional model reviewer. Absence claims for S4/S5 are bounded to the inspected shipped, installed controller/lesson/policy paths; an optional extension or future main-branch code may add them. The grade is an ownership map, not a product decision.

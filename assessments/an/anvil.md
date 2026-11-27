---
harness_id: anvil
project_name: Anvil
repository: https://github.com/deeeeone/Anvil
review_ref: 276aa0fcf2bb4bf31dd1940b1b71935d9e0c7754
reviewed_at: 2026-11-27
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A(P)
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Anvil

## Review boundary

- System in focus: Anvil's shipped macOS coding application and the project/session organization it supplies.
- Purpose and identity: Deliver repository work in direct, queued or delegated sessions under the project owner's chosen constraints.
- Relevant environment: Project worktrees, user goals, providers and optional tools.
- Standard-distribution boundary: SwiftUI application, first-party session/queue controllers, side-call reviewer, permission routes and built-in tools. Provider inference and external repositories remain dependencies.
- Credited operating / distribution surfaces: Desktop sessions, background queue, project worktrees, sub-sessions, completion review, and supported headless mode where applicable.
- Adjacent first-party surfaces excluded from ownership: Repository development/release, evals, and user-authored plugins are not credited as runtime owners.
- First-party operating / deployment modes considered: Direct Ask, Auto-edit and Bypass, queue and nested sessions, alternative completion-review modes and headless execution.
- Recursion level: One open project with its parent-run team and the installed human background-queue control surface.
- Reviewed revision: [276aa0fcf2bb4bf31dd1940b1b71935d9e0c7754](https://github.com/deeeeone/Anvil/tree/276aa0fcf2bb4bf31dd1940b1b71935d9e0c7754)
- Observation date: 2026-11-27
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

SessionController constructs a model-backed agent with first-party built-ins and parent/child tools. Background sessions share a capped dispatch pool and run on separate worktrees. The session authorizes tool effects, and the application routes outputs back to the appropriate model or project queue. [installed session wiring](https://github.com/deeeeone/Anvil/blob/276aa0fcf2bb4bf31dd1940b1b71935d9e0c7754/Anvil/App/SessionController.swift#L107-L150), [background commitment control](https://github.com/deeeeone/Anvil/blob/276aa0fcf2bb4bf31dd1940b1b71935d9e0c7754/Anvil/App/TaskQueue.swift#L36-L111), [worktree and capacity wiring](https://github.com/deeeeone/Anvil/blob/276aa0fcf2bb4bf31dd1940b1b71935d9e0c7754/Anvil/App/SubSessions.swift#L84-L140).

## Operational model

A direct request or a child with its own worktree owns scoped coding work. Worktree integration is a separate parent choice. The owner may manage current background commitments via the installed queue, independent of routine action approvals.

## S1 — Operations

- State: A
- Function: Carry out coding work and verify scoped changes.
- Disturbance / variety regulated: Repository uncertainty, tool failure and incomplete implementation.
- Decisive decision or feedback right: Choose the next supported action and corrections.
- Decision owner: The model controlling a shipped session, within operator-selected scope.
- Supporting / enforcement mechanisms: Tool parser, permission policy, checkpoint and result transport.
- Closure path: Run model-selected tools, return results into the next turn and report outcome or iterate.
- Boundary reachability: An installed session constructs the loop and the Auto-edit/Bypass paths avoid universal human selection of ordinary actions.
- Why this is / is not agent-owned: Human grants and gates constrain actions while the agent retains task-level discretion.
- Evidence: [run loop](https://github.com/deeeeone/Anvil/blob/276aa0fcf2bb4bf31dd1940b1b71935d9e0c7754/Anvil/Brain/AgentLoop.swift#L392-L435), [action and feedback](https://github.com/deeeeone/Anvil/blob/276aa0fcf2bb4bf31dd1940b1b71935d9e0c7754/Anvil/Brain/AgentLoop.swift#L727-L785), [installed session wiring](https://github.com/deeeeone/Anvil/blob/276aa0fcf2bb4bf31dd1940b1b71935d9e0c7754/Anvil/App/SessionController.swift#L107-L150), [permission ownership](https://github.com/deeeeone/Anvil/blob/276aa0fcf2bb4bf31dd1940b1b71935d9e0c7754/Anvil/Core/Permissions.swift#L29-L62)
- Basis: Pinned runtime code.
- Confidence: High.
- Caveats: No provider was called during the assessment.

## S2 — Coordination

- State: C
- Function: Prevent independent coding sessions from overwriting each other's unmerged work or competing without limits for background capacity.
- Disturbance / variety regulated: Queue tasks and child sessions can target overlapping project paths or occupy the same background slots.
- Decisive decision or feedback right: Supply an explicit cross-session isolation, ordering and conflict-handling relation.
- Decision owner: The installed constructors define worktree isolation and automatic slot policy. A parent model separately owns the incident intervention assessed in S3.
- Supporting / enforcement mechanisms: Git worktrees, shared admission cap and merge conflict checks.
- Closure path: A session waits for capacity, commits isolated work and exposes conflicts or completion before the other branch can enter the root.
- Boundary reachability: Both queue and child sessions use shipped worktrees and the same capacity gate.
- Why this is / is not agent-owned: The supplied inter-session protocol is rule-bound. The separate parent correction channel is current-control authority.
- Evidence: [background commitment control](https://github.com/deeeeone/Anvil/blob/276aa0fcf2bb4bf31dd1940b1b71935d9e0c7754/Anvil/App/TaskQueue.swift#L36-L111), [worktree and capacity wiring](https://github.com/deeeeone/Anvil/blob/276aa0fcf2bb4bf31dd1940b1b71935d9e0c7754/Anvil/App/SubSessions.swift#L84-L140), [merge conflict and return](https://github.com/deeeeone/Anvil/blob/276aa0fcf2bb4bf31dd1940b1b71935d9e0c7754/Anvil/App/SubSessions.swift#L270-L305)
- Basis: Pinned contention and enforcement paths.
- Confidence: High.
- Caveats: S2 is supported independently of any architectural claim about recursion.
- Distinct S1 units: Independently executing child coding sessions and separately queued repository tasks.
- Inter-S1 disturbance: Overlapping edits and simultaneous consumption of the background slot pool.
- Attenuating coordination relation: Separate worktrees, bounded background admissions and explicit merge conflict reports.
- Feedback into subsequent S1 behaviour: A waiting session starts when capacity frees; a conflict can return to its author as a rebase request.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The mechanisms change what happens when two independently acting work units contend for project state or execution capacity.

## S3 — Inside-and-now control

- State: A(P)
- Function: Control current commitments across work units in a parent-run team or the operator-supervised background portfolio.
- Disturbance / variety regulated: Blocked or divergent work, merge conflicts and unwanted queue commitments.
- Decisive decision or feedback right: Redirect a child, order integration, hold or integrate its contribution, or cancel a background commitment.
- Decision owner: Root model for the scoped team; project owner for the distinct queue supervision mode.
- Supporting / enforcement mechanisms: Parent-only tools, queue state, isolated branches, capacity setting and cancellation.
- Closure path: Reports and conflicts reach the parent; follow-up messages start or steer the child, and a merge changes the integration state. Queue cancellation stops or drops the selected commitment.
- Boundary reachability: Shipped SessionController injects the functions and the installed queue feeds operator decisions back to the same dispatcher.
- Why this is / is not agent-owned: The root model can independently act on child deviations in the enabled mode. The alternative queue intervention is owned by the human.
- Evidence: [installed session wiring](https://github.com/deeeeone/Anvil/blob/276aa0fcf2bb4bf31dd1940b1b71935d9e0c7754/Anvil/App/SessionController.swift#L107-L150), [sub-session tools](https://github.com/deeeeone/Anvil/blob/276aa0fcf2bb4bf31dd1940b1b71935d9e0c7754/Anvil/App/SubSessions.swift#L181-L319), [merge conflict and return](https://github.com/deeeeone/Anvil/blob/276aa0fcf2bb4bf31dd1940b1b71935d9e0c7754/Anvil/App/SubSessions.swift#L270-L305), [queue view and cancellation](https://github.com/deeeeone/Anvil/blob/276aa0fcf2bb4bf31dd1940b1b71935d9e0c7754/Anvil/UI/SidebarView.swift#L443-L485), [background commitment control](https://github.com/deeeeone/Anvil/blob/276aa0fcf2bb4bf31dd1940b1b71935d9e0c7754/Anvil/App/TaskQueue.swift#L36-L111), [shared capacity setting](https://github.com/deeeeone/Anvil/blob/276aa0fcf2bb4bf31dd1940b1b71935d9e0c7754/Anvil/UI/SettingsView.swift#L110-L115)
- Basis: Pinned discretionary rights, intervention return and two supported closures.
- Confidence: High for root mode; moderate for operator portfolio boundary.
- Caveats: The deterministic dispatcher alone is not an S3 owner and the headless mode is not used for the parent-mode claim.
- Whole-system current view: The agent sees the state, reports and messages of its child team. The operator can inspect project queue states, branches and session progress before acting.
- Current-control decision scope: The root selects child corrections and integration order. The project owner cancels pending or running background commitments and sets capacity used by subsequent dispatch.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Root model in an installed parent session | Blocked child, conflicting branch, or returned report | Choose child correction or branch integration and observe the result | [sub-session tools](https://github.com/deeeeone/Anvil/blob/276aa0fcf2bb4bf31dd1940b1b71935d9e0c7754/Anvil/App/SubSessions.swift#L181-L319), [merge conflict and return](https://github.com/deeeeone/Anvil/blob/276aa0fcf2bb4bf31dd1940b1b71935d9e0c7754/Anvil/App/SubSessions.swift#L270-L305) |
| Parent (`P`) | Project owner in the background portfolio | An unwanted running or pending project commitment | Queue cancellation stops or drops it, and the dispatcher consumes the updated state | [queue view and cancellation](https://github.com/deeeeone/Anvil/blob/276aa0fcf2bb4bf31dd1940b1b71935d9e0c7754/Anvil/UI/SidebarView.swift#L443-L485), [background commitment control](https://github.com/deeeeone/Anvil/blob/276aa0fcf2bb4bf31dd1940b1b71935d9e0c7754/Anvil/App/TaskQueue.swift#L36-L111) |

## S3* — Complementary audit

- State: A
- Function: Check completion claims through a separate model read of produced evidence and return concrete contradictions.
- Disturbance / variety regulated: A coding session may report completion despite a missing requirement or bugs.
- Decisive decision or feedback right: Judge whether the actual diff, file text and goal justify the claim.
- Decision owner: The first-party side-call reviewer or completion judge supplies the judgment. The root agent and bounded loop act on it.
- Supporting / enforcement mechanisms: Checkpoint originals, direct reads of current files and a fresh one-shot model context.
- Closure path: Findings return as a new observation to the root and can reopen work or appear as unresolved at the bound.
- Boundary reachability: The installed done path invokes the reviewer or configured judge and reads workspace files directly.
- Why this is / is not agent-owned: The audit sees actual changes in a separate prompt and can contradict the producing session's answer.
- Evidence: [review feedback path](https://github.com/deeeeone/Anvil/blob/276aa0fcf2bb4bf31dd1940b1b71935d9e0c7754/Anvil/Brain/AgentLoop.swift#L662-L705), [actual file and review input](https://github.com/deeeeone/Anvil/blob/276aa0fcf2bb4bf31dd1940b1b71935d9e0c7754/Anvil/Brain/AgentLoop.swift#L945-L991), [one-shot context](https://github.com/deeeeone/Anvil/blob/276aa0fcf2bb4bf31dd1940b1b71935d9e0c7754/Anvil/Brain/Brain.swift#L229-L234)
- Basis: Pinned runtime read and correction path.
- Confidence: High.
- Caveats: Coverage is limited to applicable requests and bounded file context. Some reviewer failures or exhausted budgets allow a reported limitation.
- Claim being audited: The session completed the requested code change and satisfied its requirements.
- Ordinary reporting path: The model's done reply and ordinary tool/build feedback.
- Complementary access path: Checkpoint-to-current-file diffs and direct reads of the changed files plus the goal.
- Independence boundary: A fresh one-shot context makes the judgment from workspace evidence without inheriting the producing interaction.
- Who acts on findings: The producing root receives the findings and can perform further corrections and checks.

## S4 — Outside-and-then intelligence

- State: —
- Function: No supplied external-and-prospective adaptation cycle is established.
- Disturbance / variety regulated: Provider availability, task failures and changed repository needs.
- Decisive decision or feedback right: No returned prospective capability decision found.
- Decision owner: No qualifying S4 owner.
- Supporting / enforcement mechanisms: Remote inventory feeds the picker and fallback reacts to a present failure.
- Closure path: The observed paths return available choices or recover a session. They do not produce prospective adaptations evaluated for the project organization.
- Why this is / is not agent-owned: Provider discovery, installation, reactive retry and future task intake are separately implemented.
- Evidence: [provider inventory](https://github.com/deeeeone/Anvil/blob/276aa0fcf2bb4bf31dd1940b1b71935d9e0c7754/Anvil/Brain/ModelCatalog.swift#L116-L169), [run loop](https://github.com/deeeeone/Anvil/blob/276aa0fcf2bb4bf31dd1940b1b71935d9e0c7754/Anvil/Brain/AgentLoop.swift#L392-L435), [installed session wiring](https://github.com/deeeeone/Anvil/blob/276aa0fcf2bb4bf31dd1940b1b71935d9e0c7754/Anvil/App/SessionController.swift#L107-L150), [provider install surface](https://github.com/deeeeone/Anvil/blob/276aa0fcf2bb4bf31dd1940b1b71935d9e0c7754/docs/PROVIDERS.md#L18-L45), [background commitment control](https://github.com/deeeeone/Anvil/blob/276aa0fcf2bb4bf31dd1940b1b71935d9e0c7754/Anvil/App/TaskQueue.swift#L36-L111)
- Basis: Bounded absence across capability surfaces.
- Confidence: Moderate.
- Caveats: Fallback can persist a session model without establishing prospective adaptation.

### Absence scope

- Surfaces inspected: Provider inventory, plugin install, current model fallback, issue polling and settings.
- Plausible first-party paths checked: Future capability selection from provider changes, adaptive model policy and issue-driven strategic replanning.
- Why no material first-party path remains: Available inventory and configuration support ordinary setup. Fallback repairs current execution and the issue watcher queues requested work. No supplied path develops future capability options and returns a decision to current control.

## S5 — Policy and identity

- State: —
- Function: No runtime ultimate identity/policy decision loop was found.
- Disturbance / variety regulated: Changes to project boundaries, acceptable effects or permission assumptions.
- Decisive decision or feedback right: No ultimate issue and returned governance resolution established.
- Decision owner: The operator sets configurations and external maintainers own release decisions.
- Supporting / enforcement mechanisms: Permission modes, explicit grants and per-project dispatch settings.
- Closure path: Scoped approvals and settings operate without an identity-level escalation and binding return.
- Why this is / is not agent-owned: A plan approval or permission setting concerns current project work or operating scope.
- Evidence: [supplied modes](https://github.com/deeeeone/Anvil/blob/276aa0fcf2bb4bf31dd1940b1b71935d9e0c7754/README.md#L34-L73), [permission ownership](https://github.com/deeeeone/Anvil/blob/276aa0fcf2bb4bf31dd1940b1b71935d9e0c7754/Anvil/Core/Permissions.swift#L29-L62), [shared capacity setting](https://github.com/deeeeone/Anvil/blob/276aa0fcf2bb4bf31dd1940b1b71935d9e0c7754/Anvil/UI/SettingsView.swift#L110-L115), [installed session wiring](https://github.com/deeeeone/Anvil/blob/276aa0fcf2bb4bf31dd1940b1b71935d9e0c7754/Anvil/App/SessionController.swift#L107-L150)
- Basis: Bounded absence under installed app and operator modes.
- Confidence: Moderate.
- Caveats: Operator control over resources and preferences remains visible.

### Absence scope

- Surfaces inspected: Permission modes, project limits, owner intervention UI, provider plugins and session model persistence.
- Plausible first-party paths checked: Ultimate-purpose escalation, policy amendment and enforceable return to all subsequent sessions.
- Why no material first-party path remains: The app exposes task and capability settings, but no supported closure of an ultimate project identity or policy conflict.

## Recursion

Child sessions have own branches, local action choices and bounded reports. These witnesses establish independent S1 units and a team at project/request level without asserting complete viability of each child.

## Variety and escalation

Worktree isolation, queue limits, explicit corrections, test outputs and a direct-file side review address different disturbances. The project owner can intervene in current queue commitments.

## Evidence gaps

Source-first review of the pinned distribution. No macOS UI, mutable worktree interaction or model-provider API was executed. Positive S3 and S3* states describe the documented installed configurations and their source closures.

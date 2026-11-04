---
harness_id: orca-trace-delange
project_name: Orca (Trace DeLange)
repository: https://github.com/tracedelange/orca
review_ref: bfdff98bdcc5e3bee5eecd790f00eb8f1104776f
reviewed_at: 2026-11-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Orca (Trace DeLange)

## Review boundary

- System in focus: installed Trace DeLange Orca local node-tree/Claude-session harness, daemon queues/worker management, Haiku classification, opt-in subtree consolidation and viewer human oversight; **not** the unrelated canonical `stablyai/orca` or `echoVic/orca-agent` projects.
- Purpose and identity: preserve hierarchical task context, run and monitor many Claude Code sessions, coordinate background tasks/worktree merges and route scarce human attention to sessions requesting it.
- Relevant environment: current user tasks, folder goals/notes/logs, repository changes and git conflicts, local/remote Claude sessions, SSH workers and operator decisions.
- Standard-distribution boundary: npm package `@tdelange/orca`, installed Claude hook and `/orca` skill, root/node `CLAUDE.md` templates, local server/CLI/viewer, built-in automatic queue/dispatch and callable consolidation flow. External Claude model internals and macOS/tmux/SSH infrastructure are not independent Orca-owned metasystems.
- Credited operating / distribution surfaces: `src/core/queue.ts`, `src/core/dispatch.ts`, `src/core/consolidate.ts`, `src/core/sessions.ts`, `src/server/app.ts`, `src/hook/main.ts`, `templates/` and `web/app.js`.
- Adjacent first-party surfaces excluded from ownership: contributor CI/tests, release scripts, hardware/SSH systems and independently authored node skills. Similar-named upstream projects do not donate functions.
- First-party operating / deployment modes considered: default session registry/rail, user dispatch with Haiku placement, active background queue with two parallel workers and conflict repair, parent/child CLI dispatch-wait-send, and expressly invoked subtree consolidation with two human checkpoints (proposal and accept/reject).
- Recursion level: one person's local node-tree work organization with multiple attached Claude sessions; a nested node is not automatically an independent viable organization.
- Reviewed revision: `bfdff98bdcc5e3bee5eecd790f00eb8f1104776f`.
- Observation date: 2026-11-04.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Orca has filesystem nodes with `CLAUDE.md` goals/notes and a global inherited context chain, hooks tracking live session state, a localhost-only HTTP server, browser map/rail and worker control over SSH. Haiku places incoming prompts in the graph or asks the user when ambiguous. The daemon's queue manager runs up to two Claude workers per node in isolated git worktrees, commits/merges their changes and returns an actual conflict to a worker for one model-selected semantic repair. A separate user-invoked consolidation session classifies live/dormant/completed nodes, proposes structural changes, then awaits human approval and a subsequent accept/reject gate. These are distinct installed modes and should not be collapsed into a general autonomous manager always running.

Primary sources: [README](https://github.com/tracedelange/orca/blob/bfdff98bdcc5e3bee5eecd790f00eb8f1104776f/README.md), [design](https://github.com/tracedelange/orca/blob/bfdff98bdcc5e3bee5eecd790f00eb8f1104776f/design.md), [queue implementation](https://github.com/tracedelange/orca/blob/bfdff98bdcc5e3bee5eecd790f00eb8f1104776f/src/core/queue.ts), [consolidation agent template](https://github.com/tracedelange/orca/blob/bfdff98bdcc5e3bee5eecd790f00eb8f1104776f/templates/consolidate.md).

## Operational model

Active Claude Code sessions are S1 workers doing project tasks in their own repository or node context; hierarchy context and Status/Done hooks carry their progress but do not themselves manage them. An explicit queue instantiates supervised child worktrees, with Haiku selecting task package and model; the server handles deterministic commit/merge and gives conflicts back to an active model-backed worker. Independently, a consolidation session can inspect an entire subtree and propose current structural changes for a human to approve. The human remains the top-level attention/control owner through browser/CLI and consent.

## S1 — Operations

- State: A
- Function: attached Claude sessions autonomously perform changing project work, edit repository artifacts and report results.
- Disturbance / variety regulated: task-specific code state, requirements, tests, model tool feedback and follow-up user/parent messages.
- Decisive decision or feedback right: each worker chooses source operations and task edits, and can revise its work on a parent or conflict prompt.
- Decision owner: Claude Code agent session launched/claimed/queued by Orca; deterministic server/hook do not invent coding decisions.
- Supporting / enforcement mechanisms: node goal/context inheritance, tmux or SSH session host, installed hooks, Claude tool runtime, queue worktree and viewer.
- Closure path: worker receives its node brief, acts and emits Status/Done; server or parent reads its result and may return corrections or archive it.
- Boundary reachability: `orca up` installs the Claude integration and `orca launch`, `dispatch`, `queue` and `claim` are first-party installed paths to running model agents.
- Why this is / is not agent-owned: active wired Claude sessions make variable project decisions; status hooks and static node files only support them.
- Evidence: [README CLI and queue](https://github.com/tracedelange/orca/blob/bfdff98bdcc5e3bee5eecd790f00eb8f1104776f/README.md), [session launch](https://github.com/tracedelange/orca/blob/bfdff98bdcc5e3bee5eecd790f00eb8f1104776f/src/core/sessions.ts), [hook](https://github.com/tracedelange/orca/blob/bfdff98bdcc5e3bee5eecd790f00eb8f1104776f/src/hook/main.ts).
- Basis: structural.
- Confidence: high.
- Caveats: this review did not run a paid Claude session or a live macOS launchd server.

## S2 — Coordination

- State: A
- Function: manage conflicting parallel S1 worker changes in one repository by isolated worktrees and a bounded model-backed merge-repair loop.
- Disturbance / variety regulated: two workers independently edit overlapping code and the merge into the shared branch conflicts.
- Decisive decision or feedback right: when git identifies exact conflicted paths, server returns those paths and the current base into the responsible worker, which chooses a semantic combined edit; server retries merge once or marks failure.
- Decision owner: queued Claude worker makes the repair choice in an explicitly invoked first-party conflict-resolution mode; deterministic queue manager owns isolation, conflict trigger, refusal and retry limits.
- Supporting / enforcement mechanisms: per-child git worktrees/branches, two-worker cap, first-party queue state, git merge/abort, `send` to the exact worker pane and retried map.
- Closure path: worker A merges; worker B's conflict aborts cleanly, base merges into B worktree and B receives a prompt to preserve both intents; on next turn the server commits/retries, succeeds or records failed task after second conflict.
- Boundary reachability: the queue manager is a default first-party server loop for enabled queue tasks and directly launches/returns to Claude worktree workers. No external conflict-solver plugin is needed.
- Why this is / is not agent-owned: specific cross-S1 conflict recovery is wired to an autonomous worker choosing the semantic resolution, not simply a static git check; server bounds and schedules the intervention.
- Distinct S1 units: two independently running queue workers, each in its own branch/worktree for one node's backlog.
- Inter-S1 disturbance: both independently modify the same repository path, creating a merge conflict on integration.
- Attenuating coordination relation: isolated worktrees plus precise conflict handback to the affected worker, with one bounded corrective attempt.
- Feedback into subsequent S1 behaviour: worker receives real conflicted file names and a concrete instruction to keep both changes, and its next output re-enters the merge loop.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the queue relates two actual operational streams competing over shared git state and closes a specific coordination conflict with corrective feedback.
- Evidence: [queue start/finish/repair](https://github.com/tracedelange/orca/blob/bfdff98bdcc5e3bee5eecd790f00eb8f1104776f/src/core/queue.ts), [design queue sequence](https://github.com/tracedelange/orca/blob/bfdff98bdcc5e3bee5eecd790f00eb8f1104776f/design.md), [queue integration tests](https://github.com/tracedelange/orca/blob/bfdff98bdcc5e3bee5eecd790f00eb8f1104776f/test/queue.test.ts).
- Basis: structural.
- Confidence: medium-high.
- Caveats: no unlimited mediation: second conflict fails, and the manager may merge a worker that stopped after an input question; recovery is bounded to queue mode.

## S3 — Inside-and-now control

- State: A(P)
- Function: inspect and adjust the current structure of a whole work subtree by classifying stale/completed/live nodes, proposing moves/archives and returning a scoped change through explicit human acceptance.
- Disturbance / variety regulated: abandoned experiments, context clutter, redundant folders and confusing current node-to-task ownership.
- Decisive decision or feedback right: model-backed consolidator selects node classes and proposes specific current restructuring; legitimate human first approves the proposal, and then accepts/rejects the actual subtree changes.
- Decision owner: separate Claude consolidator agent for the base scoped current-control judgment and action; human node-tree owner for the parent authority to authorize and accept/reject changes.
- Supporting / enforcement mechanisms: full subtree node/Log/Todo read, class/action template, live-session exclusion, before-snapshot git commit, nested round lock, `finishRound` accept/reject and browser dialog.
- Closure path: operator invokes consolidate, Claude studies complete subtree and drafts proposal; user approves, agent moves/archives/updates active structure, user accepts (commit) or rejects (revert scoped change), lock releases and structure returns to subsequent sessions.
- Boundary reachability: `orca consolidate <path>` and the browser Consolidate action are shipped, the prompt is installed in `templates/consolidate.md`, and app/server expose explicit round lifecycle.
- Why this is / is not agent-owned: model-backed consolidator decides how the present operational context should be structured and enacts approved changes; daemon and human approvals constrain rather than replace its situational judgment.
- Whole-system current view: consolidator is instructed to read all node `CLAUDE.md`, Logs, TODOs and docs in its selected subtree; at root, that is the entire local node organization, with live nodes identified.
- Current-control decision scope: archive dead/stub/completed work, preserve long-running nodes, re-group context and return the altered present work structure to active agents.
- Evidence: [consolidation template](https://github.com/tracedelange/orca/blob/bfdff98bdcc5e3bee5eecd790f00eb8f1104776f/templates/consolidate.md), [round lifecycle](https://github.com/tracedelange/orca/blob/bfdff98bdcc5e3bee5eecd790f00eb8f1104776f/src/core/consolidate.ts), [viewer endpoint](https://github.com/tracedelange/orca/blob/bfdff98bdcc5e3bee5eecd790f00eb8f1104776f/src/server/app.ts), [root agent conventions](https://github.com/tracedelange/orca/blob/bfdff98bdcc5e3bee5eecd790f00eb8f1104776f/templates/root.md).
- Basis: structural.
- Confidence: medium.
- Caveats: S3 is explicitly invoked by a human, not continuous autonomous whole-work oversight; the routine queue manager on its own is not credited with discretionary S3.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Model-backed consolidator | human-invoked subtree requiring cleanup | inspect, classify, propose and implement approved restructuring; record affected node Logs | [consolidator template](https://github.com/tracedelange/orca/blob/bfdff98bdcc5e3bee5eecd790f00eb8f1104776f/templates/consolidate.md) |
| Parent (`P`) | Legitimate human node-tree owner | proposed structural changes and completed round | approve/reject proposal then accept/reject concrete scoped modifications using browser/CLI | [round accept/reject](https://github.com/tracedelange/orca/blob/bfdff98bdcc5e3bee5eecd790f00eb8f1104776f/src/core/consolidate.ts) |

## S3* — Complementary audit

- State: —
- Function: no default independent direct-evidence auditor validates workers' results separately from their ordinary Status/Done reports.
- Disturbance / variety regulated: false completion or bad merged code is possible, but an independent audit review-return policy is not packaged.
- Decisive decision or feedback right: none for a distinct auditor; human may open transcripts or inspect uncommitted counts, while queue manager merges when the worker stops.
- Decision owner: active worker reports its own work, daemon operates merge gate and human can inspect; no separately wired independent reviewer.
- Supporting / enforcement mechanisms: session hook/status, terminal viewer, `git status --porcelain` warning, queue conflict checks and manual source access.
- Closure path: worker completion triggers routine queue merge, or operator views its session; no independent raw-diff finding leads to a mandatory corrective auditor/worker loop before admission.
- Why this is / is not agent-owned: git merge conflict is S2 resource coordination and ordinary work status is S1/S3 reporting, neither independently judges operational truth.
- Evidence: [queue merge implementation](https://github.com/tracedelange/orca/blob/bfdff98bdcc5e3bee5eecd790f00eb8f1104776f/src/core/queue.ts), [hook and viewer contract](https://github.com/tracedelange/orca/blob/bfdff98bdcc5e3bee5eecd790f00eb8f1104776f/design.md).
- Basis: structural.
- Confidence: medium-high.
- Caveats: a user can manually request Claude code review, but that custom task is not a first-party complementary audit gate.

### Absence scope

- Surfaces inspected: queue/worker lifecycle, merge path, hooks, viewer result/terminal, consolidation procedure and root conventions.
- Plausible first-party paths checked: Status/Done summary, queue auto-merge, git conflicts, uncommitted warning, human result inspection, node consolidation.
- Why no material first-party path remains: none creates a separately owned raw-operational observation and review verdict returned to the worker before normal acceptance.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party prospective outside-environment sensing/option-generation/adaptation-to-current-work loop established.
- Disturbance / variety regulated: new demands and future projects can be queued as parked ideas, but Orca does not itself transform external trend evidence into future strategy.
- Decisive decision or feedback right: no distinct future-intelligence owner or organizational adaptation decision.
- Decision owner: operator supplies goals, ideas, future tasks; dispatch/consolidation model decisions place or tidy existing work rather than evaluate externally grounded future scenarios.
- Supporting / enforcement mechanisms: per-node TODO.md, dispatch placement, queue, contextual history, visual subtree map and optional skill-created diagram.
- Closure path: a person may queue a parked idea, but no automatic outside/future signal-to-capability-shift loop returns to S3.
- Why this is / is not agent-owned: future-dated notes, graph visualization and stale-node cleanup are present-context tools, not independently driven environment intelligence.
- Evidence: [design Todo and Not built/Future work](https://github.com/tracedelange/orca/blob/bfdff98bdcc5e3bee5eecd790f00eb8f1104776f/design.md), [built-in skill](https://github.com/tracedelange/orca/blob/bfdff98bdcc5e3bee5eecd790f00eb8f1104776f/templates/skill/SKILL.md).
- Basis: structural.
- Confidence: medium-high.
- Caveats: users may ask project agents to research the future; no standing first-party S4 procedure is demonstrated.

### Absence scope

- Surfaces inspected: node goals/TODO, dispatch model, queue, consolidation, server/viewer, worker integration and architecture roadmap.
- Plausible first-party paths checked: parked ideas, prospective task goals, consolidator stale-node criteria, Haiku dispatch and future attention controls.
- Why no material first-party path remains: these are human input, present task placement or context cleanup; no first-party environmental futures evidence generates and returns adaptation options.

## S5 — Policy and identity

- State: —
- Function: the node tree carries goals and a single-user root context, but no system-level identity/ultimate-policy deliberation with legitimate decision and operational return is packaged.
- Disturbance / variety regulated: user preferences, context naming and operation permission are configuration/current-control issues, not necessarily organizational ethos tensions.
- Decisive decision or feedback right: no first-party ultimate policy process; human owns roots, terminal permissions and node structure.
- Decision owner: the user may choose changes as current owner; the software does not model an S5-specific authority resolving identity-policy conflicts.
- Supporting / enforcement mechanisms: root `CLAUDE.md`, human consent on consolidation, local-only server and implicit single-user trust assumptions.
- Closure path: root edits and approvals affect context and current nodes; no identity/policy issue escalates through a distinct forum to binding S5 return.
- Why this is / is not agent-owned: hierarchical goals, root context and ownership are not sufficient to evidence the highest policy/identity function.
- Evidence: [root conventions](https://github.com/tracedelange/orca/blob/bfdff98bdcc5e3bee5eecd790f00eb8f1104776f/templates/root.md), [design one-user boundary](https://github.com/tracedelange/orca/blob/bfdff98bdcc5e3bee5eecd790f00eb8f1104776f/design.md).
- Basis: structural.
- Confidence: medium-high.
- Caveats: particular user's root notes could contain meaningful policy, but that external content was not reviewed or claimed as Orca-owned S5.

### Absence scope

- Surfaces inspected: root/node identity fields, installed skill, consolidation approvals, server access assumptions and agent-parent conventions.
- Plausible first-party paths checked: root goal inheritance, human control, node archive, current work approvals and user-defined policy in notes.
- Why no material first-party path remains: no explicit whole-organization identity-policy issue, deciding authority workflow and returned rule/closure procedure is shipped.

## Distributed OSS parent arrangement

Orca's repository maintainer is not the operational parent of any installed node tree. The single local user can accept/reject current subtree changes and terminal operations; that supports only the evidenced parent S3 mode, not ultimate-policy S5.

## Self-hosted and non-human modes

The server runs locally; remote workers are invoked via SSH and inherit node context through injected prompts. Autonomous S1 and S2 closure depends on Claude Code; the daemon alone is a hook/display and deterministic worktree manager. User-invoked consolidation is a distinct control mode, not constant background policy management.

## Recursion

Parent node sessions can dispatch child tasks and answer questions via `orca wait` and `orca send`, but the presence of nested nodes/context does not prove independent S1–S5 viable subsystems.

## Variety and escalation

Orca attenuates complexity with a tree/context hierarchy, urgency rail and two-worker queues; delegates repetitive work to Claude sessions and returns conflicts to the active worker. The live hook's `needs-input` signal directs human attention; ambiguity in dispatch presents user choices. None of these signals alone proves independent S3* audit or future-oriented S4.

## Evidence gaps

- Source-structural review at pinned SHA without live macOS/Claude API exercise.
- Queue S2 is bounded to one conflict retry, and manager accepts worker Stop even after an unaddressed input question; no independent audit before merge.
- Consolidation S3 requires explicit invocation and two human approvals, with no claim of always-on organization-wide agent oversight.

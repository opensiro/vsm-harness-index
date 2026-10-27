---
harness_id: bise
project_name: bise
repository: https://github.com/gvergnaud/bise
review_ref: 2a0cf0caf75cb17e9b6ce40e90bab517e963e425
reviewed_at: 2026-10-27
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

# bise

## Review boundary

- System in focus: One local bise project hub with its permanent main and task agents, exposed through terminal or desktop; the solo session is a supported narrower mode and is not credited with team functions.
- Purpose and identity: Turn user requests into durable coding/task outcomes while keeping the user informed and able to decide reserved matters.
- Relevant environment: Project checkout, model providers, tools/MCP, files, parallel edits, user decisions and optional GitHub integration.
- Standard-distribution boundary: One local bise project hub with its permanent main and task agents, exposed through terminal or desktop; the solo session is a supported narrower mode and is not credited with team functions.
- Credited operating / distribution surfaces: Bend provider/tool loop and durable hub; Rust switchboard role construction, devflow, task/control commands, inbox and worktree machinery wired into shipped terminal/desktop clients.
- Adjacent first-party surfaces excluded from ownership: Repository-development issue/research pages, Bend laws/proofs, test fixtures, CI and brand/site assets corroborate mechanisms but do not supply deployed audit, adaptation or governance actors.
- First-party operating / deployment modes considered: Supported local self-hosted runtime and operator-supervised configuration; no custom external composition is credited.
- Recursion level: One runtime/project deployment; nested task agents are not presumed recursively viable.
- Reviewed revision: 2a0cf0caf75cb17e9b6ce40e90bab517e963e425
- Observation date: 2026-10-27
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

The terminal and Electron desktop are clients of a local durable hub. Bend implements message/state transitions and provider/tool agent loops; Rust supplies sessions, providers, plugins, switchboard and UI. Main maintains a permanent project conversation, briefs persistent background tasks, receives their reports and questions, and can change the model of a running task. Each task has its own context/session and tool action loop, with shared checkout or agent-selected worktree placement. Notifications route reserved decisions to the user and their answers back to affected tasks; saved flow controls shipping. Context compaction, history search, timers and restart recovery support continuity. First-party prompts are actual runtime role construction, whereas the repository's own development agents and proof suite are adjacent.

## Operational model

Task agents own contextual investigation/edit/tool choices; main can also perform narrowly scoped tiny changes. Main's explicit conflict-sensitive placement discretion closes team S2. Main's current task-state view, response to blocked work, model reassignment and corrective messages supply project-level S3; the user can alternatively intervene directly over the team. No organization-wide claim is made.

## S1 — Operations

- State: A
- Function: Autonomous task execution
- Disturbance / variety regulated: Uncertain code state, tool results and user requests
- Decisive decision or feedback right: Choose next tool/action and task completion report
- Decision owner: Provider-backed main/task agent
- Supporting / enforcement mechanisms: Bend tool dispatch, sessions, compaction, bash/edit/MCP and report persistence
- Closure path: Tool results re-enter the agent loop; changed files and terminal report are returned to main/user
- Why this is / is not agent-owned: Provider-backed main/task agent; A is architectural availability, not measured success; no provider was invoked.
- Evidence: [bend/runtime/main.bend](https://github.com/gvergnaud/bise/blob/2a0cf0caf75cb17e9b6ce40e90bab517e963e425/bend/runtime/main.bend); [bend/runtime/repl-live.bend](https://github.com/gvergnaud/bise/blob/2a0cf0caf75cb17e9b6ce40e90bab517e963e425/bend/runtime/repl-live.bend); [rust/switchboard/src/prompts.rs](https://github.com/gvergnaud/bise/blob/2a0cf0caf75cb17e9b6ce40e90bab517e963e425/rust/switchboard/src/prompts.rs) lines 115–206
- Basis: structural
- Confidence: high
- Caveats: A is architectural availability, not measured success; no provider was invoked.
- Boundary reachability: Bend provider/tool loop and durable hub; Rust switchboard role construction, devflow, task/control commands, inbox and worktree machinery wired into shipped terminal/desktop clients. The cited decision path is shipped in this mode and returns through Bend tool dispatch, sessions, compaction, bash/edit/MCP and report persistence.

## S2 — Coordination

- State: A
- Function: Prevent destructive interference between concurrent task agents
- Disturbance / variety regulated: Two task units editing the same files or observing half-finished changes
- Decisive decision or feedback right: Choose disjoint files, sequencing, shared place or isolated worktree based on the actual tasks
- Decision owner: Main agent
- Supporting / enforcement mechanisms: sb task board, spawn/place commands, worktree creation and landing machinery
- Closure path: Main's placement decision determines the directories and integration paths used by subsequent worker actions
- Why this is / is not agent-owned: Main agent; Git isolation alone is enforcement; the shipped main role supplies contextual coordination discretion.
- Evidence: [rust/switchboard/src/devflow.rs](https://github.com/gvergnaud/bise/blob/2a0cf0caf75cb17e9b6ce40e90bab517e963e425/rust/switchboard/src/devflow.rs) lines 393–425; [rust/switchboard/src/prompts.rs](https://github.com/gvergnaud/bise/blob/2a0cf0caf75cb17e9b6ce40e90bab517e963e425/rust/switchboard/src/prompts.rs) lines 124–145
- Basis: structural
- Confidence: medium
- Caveats: Git isolation alone is enforcement; the shipped main role supplies contextual coordination discretion.
- Boundary reachability: Bend provider/tool loop and durable hub; Rust switchboard role construction, devflow, task/control commands, inbox and worktree machinery wired into shipped terminal/desktop clients. The cited decision path is shipped in this mode and returns through sb task board, spawn/place commands, worktree creation and landing machinery.
- Distinct S1 units: Concurrent task agents producing separate operational outcomes.
- Inter-S1 disturbance: Two task units editing the same files or observing half-finished changes
- Attenuating coordination relation: Choose disjoint files, sequencing, shared place or isolated worktree based on the actual tasks
- Feedback into subsequent S1 behaviour: Main's placement decision determines the directories and integration paths used by subsequent worker actions
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: Git isolation alone is enforcement; the shipped main role supplies contextual coordination discretion. Prevent destructive interference between concurrent task agents

## S3 — Inside-and-now control

- State: A(P)
- Function: Current control over the project task team
- Disturbance / variety regulated: Blocked commitments, changing constraints and capability allocation among live tasks
- Decisive decision or feedback right: Inspect current team and revise briefs, constraints, agent model or intervention; alternatively user redirects team tasks
- Decision owner: Main in base mode; legitimate local project operator in parent mode
- Supporting / enforcement mechanisms: Injected bise_state/task_status, sb tasks/send/model, inbox and correction messages
- Closure path: Reports/questions reach main; main's revised instruction or model applies to subsequent task turns; user decisions are returned by addressed correction/answer
- Why this is / is not agent-owned: Main in base mode; legitimate local project operator in parent mode; Not inferred from the word orchestrator or from spawning alone. Parent current intervention is confined to this one project hub.
- Evidence: [rust/switchboard/src/prompts.rs](https://github.com/gvergnaud/bise/blob/2a0cf0caf75cb17e9b6ce40e90bab517e963e425/rust/switchboard/src/prompts.rs) lines 124–154; [rust/switchboard/src/devflow.rs](https://github.com/gvergnaud/bise/blob/2a0cf0caf75cb17e9b6ce40e90bab517e963e425/rust/switchboard/src/devflow.rs) lines 402–445; [README.md](https://github.com/gvergnaud/bise/blob/2a0cf0caf75cb17e9b6ce40e90bab517e963e425/README.md) control/talk-to-any-agent
- Basis: structural
- Confidence: medium
- Caveats: Not inferred from the word orchestrator or from spawning alone. Parent current intervention is confined to this one project hub.
- Boundary reachability: Bend provider/tool loop and durable hub; Rust switchboard role construction, devflow, task/control commands, inbox and worktree machinery wired into shipped terminal/desktop clients. The cited decision path is shipped in this mode and returns through Injected bise_state/task_status, sb tasks/send/model, inbox and correction messages.
- Whole-system current view: The cited current state/report path covers all units in the declared deployment.
- Current-control decision scope: Inspect current team and revise briefs, constraints, agent model or intervention; alternatively user redirects team tasks

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Main agent | Blocked commitments, changing constraints and capability allocation among live tasks | Reports/questions reach main; main's revised instruction or model applies to subsequent task turns; user decisions are returned by addressed correction/answer | [rust/switchboard/src/prompts.rs](https://github.com/gvergnaud/bise/blob/2a0cf0caf75cb17e9b6ce40e90bab517e963e425/rust/switchboard/src/prompts.rs) lines 124–154; [rust/switchboard/src/devflow.rs](https://github.com/gvergnaud/bise/blob/2a0cf0caf75cb17e9b6ce40e90bab517e963e425/rust/switchboard/src/devflow.rs) lines 402–445; [README.md](https://github.com/gvergnaud/bise/blob/2a0cf0caf75cb17e9b6ce40e90bab517e963e425/README.md) control/talk-to-any-agent |
| Parent (`P`) | Legitimate local operator | Operator current intervention on the whole project | Reports/questions reach main; main's revised instruction or model applies to subsequent task turns; user decisions are returned by addressed correction/answer | [rust/switchboard/src/prompts.rs](https://github.com/gvergnaud/bise/blob/2a0cf0caf75cb17e9b6ce40e90bab517e963e425/rust/switchboard/src/prompts.rs) lines 124–154; [rust/switchboard/src/devflow.rs](https://github.com/gvergnaud/bise/blob/2a0cf0caf75cb17e9b6ce40e90bab517e963e425/rust/switchboard/src/devflow.rs) lines 402–445; [README.md](https://github.com/gvergnaud/bise/blob/2a0cf0caf75cb17e9b6ce40e90bab517e963e425/README.md) control/talk-to-any-agent |

## S3* — Complementary audit

- State: —
- Function: No separate complementary audit supplied for this boundary
- Disturbance / variety regulated: Unreliable worker completion claims
- Decisive decision or feedback right: No independently owned corrective-audit right established
- Decision owner: None established
- Supporting / enforcement mechanisms: Task reports, ordinary tests, history and optional generic review tasks
- Closure path: Main is explicitly told to accept done reports and not re-run their tests; failed/blocked/no-check reports receive ordinary control
- Why this is / is not agent-owned: None established; Development proofs and routine worker QA do not establish independent operational audit.
- Evidence: [rust/switchboard/src/prompts.rs](https://github.com/gvergnaud/bise/blob/2a0cf0caf75cb17e9b6ce40e90bab517e963e425/rust/switchboard/src/prompts.rs) lines 126–127 and 198–205; [bend/laws/runtime.bend](https://github.com/gvergnaud/bise/blob/2a0cf0caf75cb17e9b6ce40e90bab517e963e425/bend/laws/runtime.bend)
- Basis: structural
- Confidence: medium
- Caveats: Development proofs and routine worker QA do not establish independent operational audit.

### Absence scope

- Surfaces inspected: [rust/switchboard/src/prompts.rs](https://github.com/gvergnaud/bise/blob/2a0cf0caf75cb17e9b6ce40e90bab517e963e425/rust/switchboard/src/prompts.rs) lines 126–127 and 198–205; [bend/laws/runtime.bend](https://github.com/gvergnaud/bise/blob/2a0cf0caf75cb17e9b6ce40e90bab517e963e425/bend/laws/runtime.bend); runtime entry, roles/tools, supported configuration and operating documentation within the declared boundary.
- Plausible first-party paths checked: Task reports, ordinary tests, history and optional generic review tasks; autonomous and operator-governed alternatives were checked for no separate complementary audit supplied for this boundary.
- Why no material first-party path remains: Main is explicitly told to accept done reports and not re-run their tests; failed/blocked/no-check reports receive ordinary control Development proofs and routine worker QA do not establish independent operational audit. This is a bounded shipped-distribution conclusion, not impossibility of an extension.

## S4 — Outside-and-then intelligence

- State: —
- Function: No shipped external-and-prospective adaptation loop
- Disturbance / variety regulated: Changing future tool/provider/environment suitability
- Decisive decision or feedback right: No first-party prospective option-to-capability decision loop established
- Decision owner: None established
- Supporting / enforcement mechanisms: Plugin installation, per-agent model selection, schedules, compaction and self.reload
- Closure path: These support present operation or software updates; no supplied actor couples environmental futures to changed current capability
- Why this is / is not agent-owned: None established; An arbitrary research task could be commissioned, but generic task/tool expressiveness is not an S4 constructor.
- Evidence: [bend/runtime/selftools-pure.bend](https://github.com/gvergnaud/bise/blob/2a0cf0caf75cb17e9b6ce40e90bab517e963e425/bend/runtime/selftools-pure.bend); [rust/switchboard/src/prompts.rs](https://github.com/gvergnaud/bise/blob/2a0cf0caf75cb17e9b6ce40e90bab517e963e425/rust/switchboard/src/prompts.rs); [README.md](https://github.com/gvergnaud/bise/blob/2a0cf0caf75cb17e9b6ce40e90bab517e963e425/README.md)
- Basis: structural
- Confidence: medium
- Caveats: An arbitrary research task could be commissioned, but generic task/tool expressiveness is not an S4 constructor.

### Absence scope

- Surfaces inspected: [bend/runtime/selftools-pure.bend](https://github.com/gvergnaud/bise/blob/2a0cf0caf75cb17e9b6ce40e90bab517e963e425/bend/runtime/selftools-pure.bend); [rust/switchboard/src/prompts.rs](https://github.com/gvergnaud/bise/blob/2a0cf0caf75cb17e9b6ce40e90bab517e963e425/rust/switchboard/src/prompts.rs); [README.md](https://github.com/gvergnaud/bise/blob/2a0cf0caf75cb17e9b6ce40e90bab517e963e425/README.md); runtime entry, roles/tools, supported configuration and operating documentation within the declared boundary.
- Plausible first-party paths checked: Plugin installation, per-agent model selection, schedules, compaction and self.reload; autonomous and operator-governed alternatives were checked for no shipped external-and-prospective adaptation loop.
- Why no material first-party path remains: These support present operation or software updates; no supplied actor couples environmental futures to changed current capability An arbitrary research task could be commissioned, but generic task/tool expressiveness is not an S4 constructor. This is a bounded shipped-distribution conclusion, not impossibility of an extension.

## S5 — Policy and identity

- State: —
- Function: No identity/ultimate-policy adjudication loop supplied
- Disturbance / variety regulated: System identity or ultimate policy in dispute
- Decisive decision or feedback right: No function-specific ultimate-authority decision/return protocol established
- Decision owner: Operator sets ordinary configuration; no qualifying S5 owner established
- Supporting / enforcement mechanisms: Role prompts, permissions, inbox approvals, saved PR/trunk flow
- Closure path: Flow choice and notification responses govern operational integration; they do not themselves establish identity-level or ultimate-policy deliberation
- Why this is / is not agent-owned: Operator sets ordinary configuration; no qualifying S5 owner established; A real human decision path was considered; its matters are ordinary task/shipping controls, not automatic S5.
- Evidence: [rust/switchboard/src/devflow.rs](https://github.com/gvergnaud/bise/blob/2a0cf0caf75cb17e9b6ce40e90bab517e963e425/rust/switchboard/src/devflow.rs) lines 402–445; [rust/switchboard/src/prompts.rs](https://github.com/gvergnaud/bise/blob/2a0cf0caf75cb17e9b6ce40e90bab517e963e425/rust/switchboard/src/prompts.rs) lines 150–156; [prompts/prompt-bise.txt](https://github.com/gvergnaud/bise/blob/2a0cf0caf75cb17e9b6ce40e90bab517e963e425/prompts/prompt-bise.txt)
- Basis: structural
- Confidence: medium
- Caveats: A real human decision path was considered; its matters are ordinary task/shipping controls, not automatic S5.

### Absence scope

- Surfaces inspected: [rust/switchboard/src/devflow.rs](https://github.com/gvergnaud/bise/blob/2a0cf0caf75cb17e9b6ce40e90bab517e963e425/rust/switchboard/src/devflow.rs) lines 402–445; [rust/switchboard/src/prompts.rs](https://github.com/gvergnaud/bise/blob/2a0cf0caf75cb17e9b6ce40e90bab517e963e425/rust/switchboard/src/prompts.rs) lines 150–156; [prompts/prompt-bise.txt](https://github.com/gvergnaud/bise/blob/2a0cf0caf75cb17e9b6ce40e90bab517e963e425/prompts/prompt-bise.txt); runtime entry, roles/tools, supported configuration and operating documentation within the declared boundary.
- Plausible first-party paths checked: Role prompts, permissions, inbox approvals, saved PR/trunk flow; autonomous and operator-governed alternatives were checked for no identity/ultimate-policy adjudication loop supplied.
- Why no material first-party path remains: Flow choice and notification responses govern operational integration; they do not themselves establish identity-level or ultimate-policy deliberation A real human decision path was considered; its matters are ordinary task/shipping controls, not automatic S5. This is a bounded shipped-distribution conclusion, not impossibility of an extension.

## Distributed OSS parent arrangement

Public contributors and maintainers are outside this deployed-runtime recursion. Local operator decisions do not imply project-wide or organization-wide parent governance.

## Self-hosted and non-human modes

Self-hosted operation is the assessed mode; parent notation is used only for the explicitly established function-specific loop, if any. No intentionally non-human governing organization is supplied.

## Recursion

Agents, tasks and sessions may be nested, but this does not establish independent viable systems with their own complete metasystem.

## Variety and escalation

Project checkout, model providers, tools/MCP, files, parallel edits, user decisions and optional GitHub integration. Task agents own contextual investigation/edit/tool choices; main can also perform narrowly scoped tiny changes. Main's explicit conflict-sensitive placement discretion closes team S2. Main's current task-state view, response to blocked work, model reassignment and corrective messages supply project-level S3; the user can alternatively intervene directly over the team. No organization-wide claim is made.

## Evidence gaps

Static source assessment only. Native Rust/Bend/macOS builds and live provider execution were not run (the inspection host lacks cargo and Bend/macOS). No deployed performance, all-task reliability, independent review or autonomy grade is claimed. Optional site/provider features outside the declared project hub are not borrowed.

---
harness_id: agent-os
project_name: Agent OS
repository: https://github.com/andrewgolovanov/agent-os
review_ref: 9f45e60058b51bc69ea746876b798f995d8bebc2
reviewed_at: 2026-10-01
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-01
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Agent OS

## Review boundary

- System in focus: one local Agent OS installation at the project/outcome recursion: private project registry, Task Board outcome lifecycle/history, Task Bridge hooks and runtime state, packaged Codex plugin/MCP/skills, app-facing runtime snapshot, native Focus/Board/Done/Setup surfaces, local notification/export/handoff machinery and optional read-only recurring monitor configuration.
- Purpose and identity: a local-first continuity/control layer around supported Codex work, keeping durable goals, state, next actions, exact source identities, task memberships and operator-facing current work while Codex remains the execution environment.
- Relevant environment: parent user/operator; registered project roots and repositories; Codex desktop/CLI/App Server; Slack and GitHub as optional external information sources; local filesystem/Git state; provider schedules/integrations.
- Operational units: supported Codex project tasks operating with the Agent OS plugin/hooks loaded and linked to durable Task Board outcomes. Their model/tool-loop internals remain external; Agent OS contributes the standard first-party continuity/control wiring around them.
- Standard-distribution boundary: packaged Agent OS plugin, hook bundle, MCP/runtime tooling, private home/registry/Task Board/Task Bridge state, native app, deterministic synchronization/snapshot interfaces and documented optional monitor configuration. Codex, Slack, GitHub and their internal agents/services remain external systems.
- Credited operating / distribution surfaces: `README.md`; `AGENTS.md`; `docs/architecture.md`; `docs/task-board.md`; `docs/task-bridge.md`; `docs/agent-os-app.md`; `docs/optional-integrations.md`; `docs/slack-monitor.md`; `plugins/agent-os/hooks/hooks.json` at the frozen revision.
- Adjacent first-party surfaces excluded from ownership: repository-development maintainers/CI/release governance; application signing/update infrastructure as product maintenance; external Codex model/tool-loop internals; Slack/GitHub provider behavior; user-authored project rules beyond the Agent OS-installed integration points.
- First-party operating / deployment modes considered: installed Codex plugin with Task Bridge hooks; CLI/MCP Task Board operation; native macOS app over the same private state; optional read-only Slack monitor executed by Codex Scheduled after explicit setup. Provider writes and future deferred integrations are excluded.
- Recursion level: one Agent OS installation coordinating durable work outcomes across one or more supported Codex work cells/projects. Lower-recursion Codex reasoning, subagents and tool loops remain separate.
- Reviewed revision: `9f45e60058b51bc69ea746876b798f995d8bebc2`.
- Observation date: 2026-10-01.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Agent OS stores canonical mutable coordination state outside the product checkout in `AGENT_OS_HOME`. The private registry owns stable project identity and paths; Task Board owns durable outcome state/history; Task Bridge binds exact Codex task/turn identity to one current outcome and requires checkpoints after material mutations. The native app reads a schema-versioned runtime snapshot rather than maintaining a second database and hands selected work back into Codex.

The standard plugin ships concrete `UserPromptSubmit`, material `PostToolUse` and `Stop` hooks. Those hooks resolve exact project/outcome identity, open/close activity turns and require a durable verified checkpoint after material edits before a turn can stop cleanly. This makes Agent OS part of the supported operating organization around a Codex work cell without inheriting Codex's internal planner/tool-loop architecture.

Optional monitoring adds bounded read-only observation of Slack and local Task Board mutation, but provider authorization and recurring execution are separately owned by the connected integration and Codex Scheduled. External writes remain user-authorized rather than autonomous Agent OS operations.

## Operational model

At this recursion, a Codex task with the Agent OS plugin loaded is the operational S1 cell. The agent performs project work while Agent OS preserves exact membership, outcome state, activity and checkpoint continuity. Multiple Codex tasks may be peers on one durable outcome, but Agent OS does not provide a first-party inter-cell conflict/negotiation mechanism: file locking protects Task Board storage rather than coordinating engineering cells.

Current control is parent-owned. Focus and Board expose unfinished work across projects and lifecycle states, and the user chooses which outcome needs attention, changes lifecycle/next action, continues an exact existing Codex task or creates a new handoff, and explicitly confirms completion. Task Bridge automates local bookkeeping and checkpoint constraints but does not autonomously choose whole-system priorities.

## S1 — Operations

- State: A
- Function: perform substantive registered-project work in a supported Codex task while maintaining one durable Agent OS outcome across turns/tasks and returning material checkpoints into the continuity layer.
- Disturbance / variety regulated: task-specific repository/project state, changing implementation/investigation conditions, blockers, exact source context and the risk that important current state disappears when a Codex turn or task ends.
- Decisive decision or feedback right: choose and revise the next task-specific project action from user objective, project evidence and returned tool/environment state.
- Decision owner: the autonomous Codex work cell running with the Agent OS plugin/hooks loaded.
- Supporting / enforcement mechanisms: Task Board outcomes, exact project registry, Task Bridge membership, plugin hooks, MCP/runtime tools, checkpoint requirement, durable summary/next action, activity history and Codex handoff.
- Closure path: registered Codex task receives/claims exact outcome → agent inspects and acts in the project → material mutation triggers Agent OS activity state → agent records verified summary/next action/status checkpoint → Stop closes the turn while preserving the durable outcome → later linked work resumes from that state.
- Boundary reachability: the official Agent OS plugin ships the Task Bridge hooks and MCP/runtime bundle and is installed directly into supported Codex; no application-authored orchestration is required to obtain the continuity loop.
- Why this is / is not agent-owned: removing the autonomous Codex worker while leaving registry, Board, hooks and app leaves durable state and enforcement but no actor making the open-ended project decisions. The agent therefore owns S1 discretion while Agent OS supplies the first-party operating envelope.
- Evidence: [`README.md`](https://github.com/andrewgolovanov/agent-os/blob/9f45e60058b51bc69ea746876b798f995d8bebc2/README.md); [`docs/task-bridge.md`](https://github.com/andrewgolovanov/agent-os/blob/9f45e60058b51bc69ea746876b798f995d8bebc2/docs/task-bridge.md); [`AGENTS.md`](https://github.com/andrewgolovanov/agent-os/blob/9f45e60058b51bc69ea746876b798f995d8bebc2/AGENTS.md); [`plugins/agent-os/hooks/hooks.json`](https://github.com/andrewgolovanov/agent-os/blob/9f45e60058b51bc69ea746876b798f995d8bebc2/plugins/agent-os/hooks/hooks.json).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: Codex model reasoning, internal delegation and tool-loop semantics remain external and are not inherited by Agent OS.

## S2 — Coordination

- State: —
- Function: no material first-party inter-S1 mutual-adjustment loop is established for multiple Agent OS-linked Codex work cells.
- Disturbance / variety regulated: possible collisions or dependencies among concurrent Codex tasks linked to the same project/outcome were inspected.
- Distinct S1 units: multiple independent Codex project tasks may be peer memberships of one outcome or operate on different outcomes/projects.
- Inter-S1 disturbance: simultaneous work can in principle overlap in repository scope or produce incompatible current assumptions, but no Agent OS-specific contention relation closes over those worker cells.
- Attenuating coordination relation: none established beyond exact identity/membership bookkeeping and storage-level file locking.
- Feedback into subsequent S1 behaviour: no first-party peer-conflict signal, lease/claim refusal, negotiation or mutual-adjustment response path was found that changes one Codex cell because of another cell's interfering action.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: shared Task Board state, one-current-outcome membership and file locking preserve correlation/storage integrity; they do not attenuate concrete inter-worker variety between engineering cells.
- Decisive decision or feedback right: none established for S2 at this boundary.
- Decision owner: none established.
- Supporting / enforcement mechanisms: exact task/outcome membership, registry resolution, atomic Task Board writes, routing-pending records, durable history and per-turn activity state.
- Closure path: no material first-party inter-S1 coordination closure exists at the frozen ref.
- Boundary reachability: the reviewed standard distribution exposes shared outcome state but not an inter-agent conflict/coordination protocol.
- Why this is / is not agent-owned: agents can independently read/update shared outcomes, but no defined Agent OS mechanism requires them to mutually adjust around detected peer interference.
- Evidence: [`docs/task-board.md`](https://github.com/andrewgolovanov/agent-os/blob/9f45e60058b51bc69ea746876b798f995d8bebc2/docs/task-board.md); [`docs/task-bridge.md`](https://github.com/andrewgolovanov/agent-os/blob/9f45e60058b51bc69ea746876b798f995d8bebc2/docs/task-bridge.md); [`docs/architecture.md`](https://github.com/andrewgolovanov/agent-os/blob/9f45e60058b51bc69ea746876b798f995d8bebc2/docs/architecture.md).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: repository/Git or project-specific conventions outside Agent OS may coordinate workers, but those are not imported.

### Absence scope

- Surfaces inspected: Task Board membership/correlation, Task Bridge hooks, project registry, activity tracking, routing-pending, atomic file locking, app handoff and optional monitor paths.
- Plausible first-party paths checked: one-current-outcome membership as mutual exclusion; Board file locking as worker contention control; multiple Codex memberships on one outcome; routing-pending as peer coordination; project registry as shared-work arbitration.
- Why no material first-party path remains: these mechanisms protect canonical identity/state or route work between a user and Codex. None detects and returns a concrete inter-S1 disturbance so participating work cells mutually adjust subsequent behavior.

## S3 — Inside-and-now control

- State: P
- Function: regulate the current Agent OS work portfolio as a whole by deciding what needs attention now, changing outcome lifecycle/next action, selecting the exact Codex continuation path and explicitly closing work.
- Disturbance / variety regulated: current mismatch across active/waiting/review outcomes, blockers, unfinished next actions, linked Codex tasks and project-level attention competing for the user's finite current-control capacity.
- Whole-system current view: Focus and Board present unfinished outcomes across registered projects/lifecycle states; the inspector exposes goal, summary, next action, blocker, sources, memberships, history and current status from the same canonical Task Board.
- Current-control decision scope: choose the current outcome to attend, move lifecycle among active/waiting/review/done/cancelled as appropriate, revise next action/blocker, continue an exact task or create a named handoff, and confirm final completion.
- Decisive decision or feedback right: choose/revise those current portfolio commitments and interventions rather than merely execute one project-local task.
- Decision owner: parent human user/operator through the native app, Task Board commands or equivalent plugin interaction.
- Supporting / enforcement mechanisms: Focus/Board/Done views, canonical outcome lifecycle, Task Board validated mutations, exact Codex memberships, continuation prompt/handoff, explicit completion confirmation and durable history.
- Closure path: shared current portfolio state is projected → human selects/changes priority/lifecycle/handoff → Agent OS writes canonical outcome state or opens the selected Codex continuation → subsequent S1 work follows the updated current-control decision.
- Boundary reachability: the native app and Task Board are supported first-party surfaces over the same private runtime and require no custom application orchestration.
- Why this is / is not agent-owned: Task Bridge may automatically activate exact-linked work and enforce checkpoints, but it does not autonomously decide which current outcome the installation should prioritize, suspend, resume, hand off or finally close. Those whole-system decisions remain with the user.
- Evidence: [`apps/agent-os/README.md`](https://github.com/andrewgolovanov/agent-os/blob/9f45e60058b51bc69ea746876b798f995d8bebc2/apps/agent-os/README.md); [`docs/agent-os-app.md`](https://github.com/andrewgolovanov/agent-os/blob/9f45e60058b51bc69ea746876b798f995d8bebc2/docs/agent-os-app.md); [`docs/task-board.md`](https://github.com/andrewgolovanov/agent-os/blob/9f45e60058b51bc69ea746876b798f995d8bebc2/docs/task-board.md); [`README.md`](https://github.com/andrewgolovanov/agent-os/blob/9f45e60058b51bc69ea746876b798f995d8bebc2/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: local lifecycle automation inside one outcome is not independently promoted to S3; the positive mapping is specifically the parent operator's whole-installation current-control loop.

## S3* — Complementary audit

- State: —
- Function: no material complementary independent audit/challenge loop is established in the standard Agent OS operating boundary.
- Disturbance / variety regulated: possible uncertainty in a Codex work cell's completion/status claim, repository result, checkpoint or integration health was inspected.
- Claim being audited: project work state or readiness as represented by the active work cell/outcome.
- Ordinary reporting path: the linked Codex cell records its own verified summary, next action and lifecycle checkpoint; Task Board persists those facts.
- Complementary access path: app PR context, history and Setup health can expose additional facts to the human, but no independent first-party auditor separately judges the S1 claim and returns findings into a corrective loop.
- Independence boundary: no separate audit actor or mechanically independent challenge relation meeting S3* closure was found.
- Who acts on findings: the parent user may inspect context and choose further work, but that is ordinary S3 parent control rather than a distinct complementary audit subsystem.
- Decisive decision or feedback right: none established for S3* at the deployed boundary.
- Decision owner: none established.
- Supporting / enforcement mechanisms: checkpoints, event history, optional GitHub PR read context, Setup capability/health observations, explicit completion confirmation and validation commands.
- Closure path: no first-party complementary audit judgment → corrective return → re-audit loop is established.
- Boundary reachability: standard app/plugin surfaces expose evidence but not a separate auditor role.
- Why this is / is not agent-owned: requiring the same work cell to checkpoint after its own mutation is ordinary self-report/continuity, not complementary audit. Human inspection belongs to the mapped parent S3 path unless a distinct audit function is closed.
- Evidence: [`docs/task-bridge.md`](https://github.com/andrewgolovanov/agent-os/blob/9f45e60058b51bc69ea746876b798f995d8bebc2/docs/task-bridge.md); [`docs/agent-os-app.md`](https://github.com/andrewgolovanov/agent-os/blob/9f45e60058b51bc69ea746876b798f995d8bebc2/docs/agent-os-app.md); [`docs/task-board.md`](https://github.com/andrewgolovanov/agent-os/blob/9f45e60058b51bc69ea746876b798f995d8bebc2/docs/task-board.md).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: external CI, repository reviewers or Codex behaviors could provide audit outside this first-party boundary and are not inherited.

### Absence scope

- Surfaces inspected: Task Bridge checkpoints; Task Board history/completion; native inspector; GitHub PR contextual reads; Setup health/capability inventory; repository validation guidance.
- Plausible first-party paths checked: checkpoint requirement as verifier; explicit completion confirmation as audit; PR status/review display as independent challenge; Setup diagnostics as S3*; repository validation commands as runtime audit.
- Why no material first-party path remains: these paths preserve/report evidence or let the same parent operator inspect it. No distinct first-party actor independently challenges an S1 claim and returns findings through a corrective rework closure.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material external-and-prospective adaptation loop is established in the reviewed Agent OS standard distribution.
- Disturbance / variety regulated: Slack signals, provider availability, project changes, software versions, schedules and possible future work conditions were inspected as candidate S4 inputs.
- Decisive decision or feedback right: none established that turns external observations into a model of future environment, develops adaptation options and returns an adaptation choice into current Agent OS capability/policy.
- Decision owner: none established for S4.
- Supporting / enforcement mechanisms: optional Slack monitor, recurring schedule intent, current project synchronization, version/update checks, Task Board follow-up and notifications.
- Closure path: no supported outside-and-then intelligence/adaptation decision-and-return loop exists at the frozen ref.
- Why this is / is not agent-owned: the Slack monitor repeatedly senses current unresolved asks and converts actionable present signals into local outcomes; scheduled repetition does not make it prospective intelligence. Project/version discovery likewise reacts to current observed state rather than developing future adaptation options.
- Evidence: [`docs/slack-monitor.md`](https://github.com/andrewgolovanov/agent-os/blob/9f45e60058b51bc69ea746876b798f995d8bebc2/docs/slack-monitor.md); [`docs/optional-integrations.md`](https://github.com/andrewgolovanov/agent-os/blob/9f45e60058b51bc69ea746876b798f995d8bebc2/docs/optional-integrations.md); [`docs/architecture.md`](https://github.com/andrewgolovanov/agent-os/blob/9f45e60058b51bc69ea746876b798f995d8bebc2/docs/architecture.md); [`docs/agent-os-app.md`](https://github.com/andrewgolovanov/agent-os/blob/9f45e60058b51bc69ea746876b798f995d8bebc2/docs/agent-os-app.md).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: recurring review/monitor execution can create current work from newly observed external events, but no prospective adaptation function is closed.

### Absence scope

- Surfaces inspected: Slack Monitor sensing/cursors; recurring execution configuration; project synchronization; app notifications; update/version checks; deferred integration roadmap.
- Plausible first-party paths checked: scheduled Slack monitoring as environmental intelligence; recurring reviews as future planning; update checks as adaptation; project discovery as external sensing; follow-up reminders as prospective model.
- Why no material first-party path remains: shipped mechanisms observe or schedule present-state operations. They do not construct future-environment distinctions, compare adaptation options and return an adaptation decision into system organization.

## S5 — Policy and identity

- State: —
- Function: no material ultimate organizational identity/policy closure is established for the Agent OS installation.
- Disturbance / variety regulated: possible conflicts over project identity, trust, external-write authority, plugin/schedule approval and highest-level operating policy were inspected.
- Decisive decision or feedback right: none established as an S5-specific runtime path beyond ordinary user configuration/consent, exact object identity and current-control decisions.
- Decision owner: none established for S5 at this deployed boundary.
- Supporting / enforcement mechanisms: stable project/source/task identities, preview-first changes, explicit user intent for external writes, plugin trust review, separate integration authorization, completion confirmation and update opt-ins.
- Closure path: no first-party path was found where an organizational identity/ultimate-policy issue is escalated to legitimate ultimate authority and the returned decision governs subsequent Agent OS operation as S5.
- Why this is / is not agent-owned: project keys, exact source identities and permission/approval gates are operational identity and authorization mechanisms, not a closure over organizational purpose/constitution. Human consent alone is not promoted to parent S5 without the S5-specific escalation/return relation.
- Evidence: [`docs/architecture.md`](https://github.com/andrewgolovanov/agent-os/blob/9f45e60058b51bc69ea746876b798f995d8bebc2/docs/architecture.md); [`docs/task-board.md`](https://github.com/andrewgolovanov/agent-os/blob/9f45e60058b51bc69ea746876b798f995d8bebc2/docs/task-board.md); [`docs/optional-integrations.md`](https://github.com/andrewgolovanov/agent-os/blob/9f45e60058b51bc69ea746876b798f995d8bebc2/docs/optional-integrations.md); [`AGENTS.md`](https://github.com/andrewgolovanov/agent-os/blob/9f45e60058b51bc69ea746876b798f995d8bebc2/AGENTS.md).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: repository/product governance and user-owned project rules may embody policy outside the selected deployed organization but are not borrowed as Agent OS S5.

### Absence scope

- Surfaces inspected: project registry identity; source/task identity; user consent/preview gates; external-write restrictions; plugin trust; integration setup; lifecycle completion; updater controls; repository-level AGENTS policy.
- Plausible first-party paths checked: stable project identity as S5 identity; explicit user approval as ultimate authority; plugin trust as constitutional gate; project `AGENTS.md` as organizational constitution; external-write prohibition as ultimate policy; maintainer product rules as parent governance.
- Why no material first-party path remains: these mechanisms identify objects, constrain operations or express adjacent user/repository policy. No deployed S5-specific identity/ultimate-policy escalation-and-return loop is incorporated into Agent OS runtime organization.

## Distributed OSS parent arrangement

Public maintainers are not used to manufacture deployed S3/S4/S5 ownership. The positive S3 mapping is operationally local: the Agent OS user sees the current portfolio and returns current-control decisions through Task Board/app/handoff state. Repository/product governance remains adjacent.

## Self-hosted and non-human modes

Agent OS is local-first. Autonomous S1 operation is available when the official plugin is loaded into a Codex task; optional monitor execution can also autonomously create/update local current-state outcomes under a separately approved schedule. Whole-system S3 remains parent-human. No first-party autonomous S2, S3*, S4 or S5 closure is established.

## Recursion

At this recursion, supported Codex project tasks are operational cells contributing project outcomes. Their lower-recursion model/tool loops and internal agents remain external. Agent OS owns continuity and parent-facing current-control state around those cells, not their hidden internal organization.

## Variety and escalation

Agent OS attenuates continuity variety through exact project/source/task identity, one-current-outcome membership, durable lifecycle/history, atomic state writes and fail-closed ambiguity handling. It amplifies regulation through Focus/Board views, exact Codex handoff, checkpoints, notifications and optional external signal intake. Task Bridge checkpoint enforcement belongs to S1 continuity; whole-portfolio attention/lifecycle intervention belongs to parent S3. Ambiguity and explicit-approval paths transport exceptional state but do not establish S2, S4 or S5 by themselves.

## Evidence gaps

No material evidence gap prevents publication at the frozen revision. The main interpretive boundary is that the official plugin makes autonomous Codex work cells reachable as Agent OS S1 while leaving Codex internals external. Multiple linked tasks/shared outcome state do not close S2; self-checkpointing and contextual PR/health views do not close S3*; recurring Slack sensing remains present-state intake rather than S4; stable identifiers and user approvals remain below S5 closure.
---
harness_id: kandev
project_name: Kandev
repository: https://github.com/kdlbs/kandev
review_ref: a2e13dcf5584e3462ea995791e245177249a9845
reviewed_at: 2026-10-27
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: ?
autonomy_s4: —
autonomy_s5: —
---

# Kandev

## Review boundary

- System in focus: the supported Kandev task/agent runtime and its optional first-party Office workspace mode, not the Kandev development organization.
- Purpose and identity: organize coding/automation tasks, launch configured agent sessions, coordinate concurrent work, and supervise progress and workspace cost.
- Relevant environment: user-selected code repositories, worktrees, agent CLI/provider runtimes, executor hosts, task reviewers/operators, and source-control services.
- Standard-distribution boundary: the released Go control plane, agentctl adapters, browser/desktop controls, installed provider integrations, regular task/workflow functions, and documented opt-in Office mode. Actual agent-provider cognition is an integrated external component; its decisions are not attributed to Kandev's deterministic backend.
- Credited operating / distribution surfaces: `apps/backend/internal/agent/runtime/`, `apps/backend/internal/agentctl/`, task/workflow/orchestration services, `docs/ARCHITECTURE.md`, `docs/public/agents-and-profiles.md`, `docs/public/coordination.md`, and opt-in Office runtime/docs.
- Adjacent first-party surfaces excluded from ownership: mock agents, E2E/development fixtures, app release/CI automation, contributor governance, engineering design proposals and unshipped experimental aspirations. Office is disabled by default in production but has an explicitly documented opt-in supported runtime path; that path is assessed separately where it changes ownership.
- First-party operating / deployment modes considered: native/self-hosted Go backend with web/Tauri UI; local, worktree, container and remote executor profiles; ACP/CLI-backed configured agent sessions; regular Kanban tasks/subtasks; Office opt-in team execution; supervisor/operator and coordinator autonomy options.
- Recursion level: the Kandev workspace's task operations and associated coordination/control, with individual agent sessions as operational units; UI widgets, tools and nested tasks are not automatically independent viable recursions.
- Reviewed revision: `a2e13dcf5584e3462ea995791e245177249a9845`.
- Observation date: 2026-10-27.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The Go backend serves the UI/API and composes task, workflow, run, Office and orchestration services, persistence and event delivery. Its executor launches agentctl in the selected local/container/remote environment; agentctl owns the agent subprocess and adapts ACP/CLI protocols, tool access and session lifecycle. Users install or choose a supported CLI and configure model, credentials, execution profile and permissions. The model-backed CLI agent selects task-specific tool/action steps; the backend transports messages, starts and stops sessions, isolates files, persists workflow state and gates permissions. First-party task MCP lets a running agent create subtasks, spawn sessions, message peers and choose an isolated workspace. Optional Office provides persistent agent identities, task/run assignment, review/approval stages, budgets, supervisor controls and scheduled routines. The provider CLI is not Kandev-authored, and a documentation example or mock agent is not evidence of Kandev-owned cognition.

Primary source: [architecture](https://github.com/kdlbs/kandev/blob/a2e13dcf5584e3462ea995791e245177249a9845/docs/ARCHITECTURE.md), [agent/profile integrations](https://github.com/kdlbs/kandev/blob/a2e13dcf5584e3462ea995791e245177249a9845/docs/public/agents-and-profiles.md), [work coordination](https://github.com/kdlbs/kandev/blob/a2e13dcf5584e3462ea995791e245177249a9845/docs/public/coordination.md), and [Office mode](https://github.com/kdlbs/kandev/blob/a2e13dcf5584e3462ea995791e245177249a9845/docs/public/office.md).

## Operational model

Configured agent sessions are the units producing coding/task results. The external provider-backed agent owns local action/continuation decisions, whereas Kandev owns the first-party supported launch/feedback integration, workspace isolation, task state and enforcement. A caller/agent can compose multiple operations, but routing or task hierarchy alone is not S2. Office's manager-selected limits and pause controls are a separate optional parent-governed current-control mode; their human-selected values are not autonomous S3 decisions. Shadow learning reports are read-only, not operational adaptation.

## S1 — Operations

- State: A
- Function: execute coding/automation tasks through configured agent sessions coupled to repository/file/tool environment.
- Disturbance / variety regulated: changing code state, tool results, user instructions, runtime errors and task contingencies.
- Decisive decision or feedback right: select the next task-specific action/tool call and continue or revise work from execution feedback.
- Decision owner: the launched provider-backed CLI agent/model in each supported agent session, not Kandev's launcher, executor or queue.
- Supporting / enforcement mechanisms: Go orchestration, agentctl/ACP bridge, selected executor, profile policy, Git/worktree operations, tool messaging, persistence and UI.
- Closure path: the first-party launcher establishes an agent session; agentctl returns messages/tool results to that same agent's subsequent turns, whose decisions produce code/task outcomes.
- Boundary reachability: the product explicitly detects or installs supported agent CLIs, configures executable profiles, starts them via agentctl, and supports normal workspace/task sessions; this is an operating path, not only an SDK example.
- Why this is / is not agent-owned: provider-backed agents decide what code action to take; without them, Kandev's transport and task engine cannot choose task-specific implementation actions. The agentic decision is **not** attributed to Kandev-authored algorithmic cognition.
- Evidence: [agent integration/profiles](https://github.com/kdlbs/kandev/blob/a2e13dcf5584e3462ea995791e245177249a9845/docs/public/agents-and-profiles.md#L8-L45); [runtime boundary](https://github.com/kdlbs/kandev/blob/a2e13dcf5584e3462ea995791e245177249a9845/docs/ARCHITECTURE.md#L11-L70); [session spawn/return](https://github.com/kdlbs/kandev/blob/a2e13dcf5584e3462ea995791e245177249a9845/docs/public/coordination.md#L55-L90).
- Basis: explicit and structural.
- Confidence: medium-high.
- Caveats: This is an integrated-agent harness finding, not a claim that the Kandev backend or a Kandev-authored model owns the tool-selection cognition; agent CLI/provider availability and authentication are deployment dependencies. No live model execution was performed.

## S2 — Coordination

- State: C
- Function: attenuate concurrent agent writers' interference by selecting distinct workspace/worktree boundaries and reconciling targeted exchanges.
- Disturbance / variety regulated: two agent sessions or parent/child tasks writing the same files can collide, while separation can fragment shared context.
- Decisive decision or feedback right: choose shared versus newly isolated task workspaces and associated handoff/messaging path for concurrent work.
- Decision owner: in the shipped constructor the task creator/agent calling `create_task_kandev` can select `workspace_mode`; the autonomous, feedback-driven collision arbitration policy is not supplied by default. A UI operator can also select a mode, but ordinary human selection is not an S2 parent publication state.
- Supporting / enforcement mechanisms: subtask/workspace attachment, worktree isolation, executor selection, targeted session messages, queue/lock enforcement and task relationship records.
- Closure path: a selected new workspace materializes a separated repository state for the child, and subsequent agent actions use that workspace; messages and replies allow agents to revise their subsequent work after coordination.
- Boundary reachability: `create_task_kandev` and `spawn_session_kandev` are documented tools exposed to normal running tasks, not only custom host application hooks. The isolation/feedback constructor is first-party, while the task-level agent must choose when it matters.
- Why this is / is not agent-owned: the relation is S2-specific to an explicit shared-files interference mode, but Kandev does not show a ready autonomous collision-detection/negotiation policy owning the choice; therefore `C`, not `A`.
- Distinct S1 units: concurrently executing agent sessions or separate child task agents.
- Inter-S1 disturbance: simultaneous edits in shared worktrees can collide, explicitly documented for concurrent writers.
- Attenuating coordination relation: choose `new_workspace` isolation rather than `inherit_parent`, with targeted message/return channels when collaboration is needed.
- Feedback into subsequent S1 behaviour: the chosen workspace controls what files each next run sees/writes, while returned messages can revise each agent's next turn.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the documented boundary choices explicitly distinguish concurrent writer collision from safe isolation, instead of merely transporting a task or message.
- Evidence: [concurrent writer boundary](https://github.com/kdlbs/kandev/blob/a2e13dcf5584e3462ea995791e245177249a9845/docs/public/coordination.md#L24-L44); [new/inherited workspaces](https://github.com/kdlbs/kandev/blob/a2e13dcf5584e3462ea995791e245177249a9845/docs/public/coordination.md#L90-L137); [agent-callable tool and return](https://github.com/kdlbs/kandev/blob/a2e13dcf5584e3462ea995791e245177249a9845/docs/public/coordination.md#L137-L194).
- Basis: explicit and structural.
- Confidence: medium.
- Caveats: No evidence of automatic merge-conflict detection/repair owned by a Kandev coordination agent; the decision must be composed within the calling task's work policy.

## S3 — Inside-and-now control

- State: P
- Function: regulate current Office workspace commitments, run admission, spend and suspension on behalf of the team.
- Disturbance / variety regulated: competing task launches, runaway unattended spend, failed agents and a team requiring immediate cross-task halt.
- Decisive decision or feedback right: choose workspace/agent/project budget policies, pause/resume a team, and decide which blocked work may restart.
- Decision owner: the legitimate self-hosted Office workspace operator/manager in the explicitly supported opt-in Office mode; deterministic gates execute selected bounds.
- Supporting / enforcement mechanisms: Office dashboard/run accounting, per-scope budget admission, pause-state persistence and halt sweep, agent status, history and UI.
- Closure path: a manager's chosen policy changes later run admission/pausing; a workspace pause blocks new launches and attempts to stop live Office work, while resume reopens admission and requires deliberate restart of cancelled work.
- Boundary reachability: the documented Office feature flag enables a first-party workspace UI/backend and budget/pause controls in a deployed Kandev instance. It is opt-in/experimental, not silently assumed for ordinary Kanban sessions.
- Why this is / is not agent-owned: Kandev's limiter merely enforces the manager-selected ceiling, and the manager controls workspace suspension/restart; no autonomous agent owns these whole-workspace interventions by default.
- Whole-system current view: Office dashboard aggregates team agent/task/run activity, budget spend and waiting decisions.
- Current-control decision scope: workspace-wide pause/resume and budget/admission decisions across agents/projects, not a single task's tool action.
- Evidence: [Office workspace model and review states](https://github.com/kdlbs/kandev/blob/a2e13dcf5584e3462ea995791e245177249a9845/docs/public/office.md#L18-L62); [spend/manager policy](https://github.com/kdlbs/kandev/blob/a2e13dcf5584e3462ea995791e245177249a9845/docs/public/office-operations.md#L17-L69); [pause and return](https://github.com/kdlbs/kandev/blob/a2e13dcf5584e3462ea995791e245177249a9845/docs/public/office-operations.md#L70-L94).
- Basis: explicit.
- Confidence: medium-high.
- Caveats: The optional parent mode is not present until Office is enabled/configured; the default spend ceiling is an enforcement support mechanism rather than an autonomous organizational choice. No separate `C` or `A` S3 mode is credited from generic task delegation or an agent named coordinator.

## S3* — Complementary audit

- State: ?
- Function: an independently controlled complementary audit of a task's operational claims is plausible but not resolved from the shipped review configuration inspected.
- Disturbance / variety regulated: an implementing agent may report completion while the actual diff/test state remains defective.
- Decisive decision or feedback right: judge independent source evidence and return corrective control, if a distinct non-routine audit path is configured.
- Decision owner: unresolved; Office reviewers/approvers and code-review utility flows are present but their independence and complementary versus routine-review status are not established here.
- Supporting / enforcement mechanisms: first-party review/approval workflow, task diff/repository inspection, review prompts and reviewer participation.
- Closure path: routine rejected task returns to Work, but it is unresolved whether a distinct complementary audit rather than the normal delivery gate exists with independent judgment.
- Why this is / is not agent-owned: a reviewer label and deterministic reject transition are insufficient to identify an independent S3* audit owner.
- Evidence: [Office Review and Approval](https://github.com/kdlbs/kandev/blob/a2e13dcf5584e3462ea995791e245177249a9845/docs/public/office.md#L37-L62); [session review surface](https://github.com/kdlbs/kandev/blob/a2e13dcf5584e3462ea995791e245177249a9845/docs/public/sessions-and-review.md); [configured review workflow](https://github.com/kdlbs/kandev/blob/a2e13dcf5584e3462ea995791e245177249a9845/apps/backend/config/workflows/pr-review.yml).
- Basis: structural and unknown.
- Confidence: low.
- Caveats: Specific shipped reviewer and raw-diff access paths require independent ownership/closure adjudication; do not convert a routine QA/review step into S3* just because it uses another agent.

## S4 — Outside-and-then intelligence

- State: —
- Function: no closed prospective external-environment adaptation loop established for the supported workspace harness.
- Disturbance / variety regulated: model/provider/tool/ecosystem change would require adapting workspace capability beyond current task planning.
- Decisive decision or feedback right: no first-party agent-owned or separately closed parent adaptation choice found.
- Decision owner: none established for S4.
- Supporting / enforcement mechanisms: configurable profiles/provider routes, Office routines and experimental coordinator shadow-learning reports.
- Closure path: routine tasks can change code and managers can edit configuration, but no shipped externally oriented future-options loop returns an adaptation decision into current workspace capability.
- Why this is / is not agent-owned: reactive provider handling, task plans and own-turn shadow reports are not S4 by themselves.
- Evidence: [coordinator shadow-learning is report-only](https://github.com/kdlbs/kandev/blob/a2e13dcf5584e3462ea995791e245177249a9845/docs/public/coordinator.md#L65-L94); [agent profiles](https://github.com/kdlbs/kandev/blob/a2e13dcf5584e3462ea995791e245177249a9845/docs/public/agents-and-profiles.md); [Office modes](https://github.com/kdlbs/kandev/blob/a2e13dcf5584e3462ea995791e245177249a9845/docs/public/office.md).
- Basis: structural.
- Confidence: medium.
- Caveats: User-created future research tasks or third-party extensions are possible, but do not constitute a shipped S4 path.

### Absence scope

- Surfaces inspected: coordinator autonomy and learning, Office routines/operator docs, agent profile/provider configuration and general workflow architecture.
- Plausible first-party paths checked: self-learning/dream reports, provider fallback, scheduled routines, and human profile modifications.
- Why no material first-party path remains: shadow review explicitly applies no change; fallback/routines respond to current operations, and generic human configuration offers no closed outside-and-then adaptation-option conversation for this system-in-focus.

## S5 — Policy and identity

- State: —
- Function: no operationally closed identity/ultimate-policy decision path established at the Kandev workspace recursion.
- Disturbance / variety regulated: conflicts about the workspace's ultimate purpose or non-negotiable governing identity, distinct from ordinary task/permission/budget choices.
- Decisive decision or feedback right: no function-specific ultimate-policy matter/legitimate authority/returned policy decision path found.
- Decision owner: none established for S5.
- Supporting / enforcement mechanisms: operator-set permissions, role privileges, credential boundaries, feature flags, isolation and budget/approval gates.
- Closure path: ordinary config/approval outcomes affect task execution but do not demonstrate a reconstructed S5 policy identity issue and returned decision.
- Why this is / is not agent-owned: human final approval, API permission and a coordinator's autonomy switch regulate operational discretion, not identity-level policy.
- Evidence: [operator gates](https://github.com/kdlbs/kandev/blob/a2e13dcf5584e3462ea995791e245177249a9845/docs/public/office-operations.md); [coordinator permissions](https://github.com/kdlbs/kandev/blob/a2e13dcf5584e3462ea995791e245177249a9845/docs/public/coordinator.md); [profile permissions](https://github.com/kdlbs/kandev/blob/a2e13dcf5584e3462ea995791e245177249a9845/docs/public/agents-and-profiles.md).
- Basis: structural.
- Confidence: medium.
- Caveats: The project maintainers may exercise higher-level governance outside the reviewed runtime; repository co-location does not make that a Kandev workspace S5.

### Absence scope

- Surfaces inspected: Office manager and approval workflows, coordinator settings/learning, execution-profile permissions, first-party architecture and credential/trust controls.
- Plausible first-party paths checked: role configuration, human approvals, workspace pause/budget policy, agent self-permission and developer governance.
- Why no material first-party path remains: the supported mechanisms decide task/current-control or deployment settings, but expose no distinct runtime channel for ultimate-identity dispute through legitimate parent decision and return-to-operation closure at the declared recursion.

## Distributed OSS parent arrangement

Independent OSS contributors and maintainers govern code and releases, but that development organization is adjacent to a deployed Kandev workspace. The optional self-hosted Office manager controls operational S3 budgets/pauses in the first-party product; this finding does not promote contributor PR activity to workspace S5.

## Self-hosted and non-human modes

Kandev is self-hosted and supports operator-controlled Office budgets/pause as an explicit option. Agent identities can run unattended within manager-selected bounds, but that alone does not transfer the manager's workspace-wide budget decisions to an autonomous S3 owner. The `P` notation describes the separately reachable first-party parent mode, not a deficiency or mandatory human in every agent turn.

## Recursion

Individual sessions and child tasks may be operationally meaningful, but spawning a session or nested task does not establish a separate full VSM recursion. This assessment applies to the Kandev task/workspace layer; no child viability claim is made.

## Variety and escalation

Kandev attenuates task/environment variety with isolation choices, role/profile setup, queued messages, review stages and run gates. Agent-local tool failures return to the operational session. Workflow decisions, budget stops and Office pauses move to the workspace manager when configured. An event/queue/status flag is a signalling mechanism, not an independent S-function or proof of an algedonic channel.

## Evidence gaps

- S3*: routine workflow Review/Approval is directly evidenced, but an independently owned, complementary raw-evidence audit path with separate return-to-control is unresolved; hence `?` instead of inventing S3* or asserting bounded absence.
- Agent/provider behavior is source-mapped only. No live coding/model/ACP provider execution or outcome-quality measurement was performed.
- Experimental Office is explicitly opt-in and disabled by default in production. Its parent-owned S3 finding should not be read as the default single-session mode's ownership.

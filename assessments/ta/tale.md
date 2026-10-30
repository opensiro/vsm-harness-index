---
harness_id: tale
project_name: Tale
repository: https://github.com/tale-project/tale
review_ref: b2560c2d7d3294993e66129c891be4a059f3d6c4
reviewed_at: 2026-10-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A(P)
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: P
---

# Tale

## Review boundary

- System in focus: one self-hosted Tale project operating cell with its configured project agents, task board, first-party task/agent-run host, sandbox/worker management, tool bridge, review gates, and durable project instructions at the pinned revision.
- Purpose and identity: organize project work across people and agent actors, turn task briefs into agent-run deliverables, coordinate concurrent runs, and return review decisions to subsequent work.
- Relevant environment: users and project requirements, task artifacts, source repositories, sandbox capacity and host contention, configured model/agent-runtime providers, external tools and credentials, and reviewer observations.
- Standard-distribution boundary: public Tale services/platform and sandbox-runtime implementation, supported project-agent runs, manager-granted task tools, and first-party native agent reviewer modes. A Tale project must be configured with eligible agents, models and grants; those are supported first-party operating configurations, not a claim that every fresh installation autonomously dispatches.
- Credited operating / distribution surfaces: task-run launch/settlement and persistent agent workers; project-scoped task discovery and bounded changes; per-run isolation and capacity admission; explicitly granted manager project-wide tools; native captured independent reviewer with source-bound verdict and corrective return; authoritative project instructions reloaded into agent turns.
- Adjacent first-party surfaces excluded from ownership: Tale repository CI, test harness, UI screenshot fixtures, maintainer workflows, documentation/demo projects, marketing pages, and organizational governance of Tale as an OSS project. Claude Code, Codex, OpenCode, Hermes and other selectable *external agent runtimes* are not credited for Tale-specific organizational function closure. They supply the configured operational agent actor; their independent internal organizational machinery is outside scope.
- First-party operating / deployment modes considered: ordinary human-assigned project-agent task turns; explicitly granted project-wide manager-agent task tools; captured native agent-to-agent review; project-editor/operator task control; automation and configured sandbox workers. Agent review is a supported mode, not a universal requirement or default for all tasks.
- Recursion level: one project operating cell. Distinct project-agent task work cells are S1; project board/manager and project reviewer roles regulate them at this recursion. A task's internal coding agent orchestration is not automatically a new Tale-owned recursion.
- Reviewed revision: `b2560c2d7d3294993e66129c891be4a059f3d6c4`.
- Observation date: 2026-10-30.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.7`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.7`.

## Repository architecture

Tale's platform persists projects, tasks, agent definitions, assignments, task comments, runs, review requests, project instructions and configuration. Its task-side run host starts a selected harness in a standing sandbox worker, stages task inputs, supplies a task brief and scoped tool bridge, observes execution, harvests files and posts the agent result as a task comment. A settled implementation run advances to `in_review`; the agent itself cannot mark its work done. Separate tools allow an authorized manager agent to inspect a whole project board, change assignment/priority, start work, and delegate a *captured* review. A designated different agent can inspect the source run's artifacts, attest concrete checks and decide approve/request changes through a revision-bound native review transaction. Ordinary human/project members retain task and project-instruction control. Task/worker exclusivity, capacity, leases, retries and safety policies are deterministic support, not agent decisions. The selected coding/LLM runtime's model/tool deliberation is an external dependency operated through Tale's supported agent-run path.

Primary architecture: [task run host](https://github.com/tale-project/tale/blob/b2560c2d7d3294993e66129c891be4a059f3d6c4/services/platform/backend/core/tasks/agent_run_host.ts#L1-L18), [task tool catalog and authority descriptions](https://github.com/tale-project/tale/blob/b2560c2d7d3294993e66129c891be4a059f3d6c4/services/platform/backend/core/node_only/sandbox/workspace_tools_bridge.ts#L197-L405), [native review implementation](https://github.com/tale-project/tale/blob/b2560c2d7d3294993e66129c891be4a059f3d6c4/services/platform/backend/domains/tasks/agent-review.ts#L131-L205), [sandbox runner](https://github.com/tale-project/tale/tree/b2560c2d7d3294993e66129c891be4a059f3d6c4/services/sandbox-runtime).

## Operational model

An assigned agent turn is an S1 cell when its configured model-driven actor makes task-specific choices and produces a result. The Tale host and tool bridge provide a reachable supported execution path; they do not take ownership of the external actor's internal coding decisions. Cross-run admission/isolation attenuates interference without independently making discretionary agent coordination decisions. In an explicitly equipped manager mode, a separate agent can read the current portfolio and choose project-level priorities and assignments; a human project operator can exercise the same current-control right in another mode. Native agent review provides a distinct, source-bound complementary access path and corrective verdict. No convincing external-and-prospective *capability adaptation* circuit was found at the project boundary. Authorized project owner/editor instructions give a parent-governed path for durable project identity and rules returned to future agent turns.

## S1 — Operations

- State: A
- Function: produce project task deliverables through agent-owned execution of assigned task briefs.
- Disturbance / variety regulated: ambiguous user requests, files and tool observations, provider responses, task feedback, source changes and execution failures.
- Decisive decision or feedback right: within an authorized turn, the configured autonomous agent chooses substantive task actions, tool interactions, corrections and the output to return.
- Decision owner: configured model-driven project-agent actor in Tale's supported project-agent run; Tale does not claim first-party ownership of the selected external runtime's internal agent loop.
- Supporting / enforcement mechanisms: task assignment, task brief/context injection, sandbox session/worker, credential/tool bridge, output harvesting, run deadlines and agent retry.
- Closure path: task brief and current project context → selected agent turn in its sandbox → model-driven actions/tool observations → updated actions and deliverables → persisted task report/artifacts and reviewer feedback → subsequent task work.
- Boundary reachability: normal project-agent task starts create a standing sandbox turn for a configured supported harness; the implementation and task tools are shipped with Tale. No contributor-only executor is needed, though a configured external agent runtime/provider is a declared operational dependency.
- Why this is / is not agent-owned: removing the configured agent actor leaves task/sandbox/queue infrastructure but no substantive choice of task actions or deliverable; the host does not decide content.
- Evidence: [run host launch and settle](https://github.com/tale-project/tale/blob/b2560c2d7d3294993e66129c891be4a059f3d6c4/services/platform/backend/core/tasks/agent_run_host.ts#L1-L18); [tool bridge task actions](https://github.com/tale-project/tale/blob/b2560c2d7d3294993e66129c891be4a059f3d6c4/services/platform/backend/core/node_only/sandbox/workspace_tools_bridge.ts#L285-L365); [README supported runtimes](https://github.com/tale-project/tale/blob/b2560c2d7d3294993e66129c891be4a059f3d6c4/README.md).
- Basis: explicit + structural.
- Confidence: high for the supported composed agent-run path; no claim about autonomous management on a default unconfigured install.
- Caveats: model providers and selectable external agent runtimes are dependencies. Their own S2-S5 are not inherited by Tale. `A` describes the reachable assembled S1 actor, not an autonomous Tale-owned model implementation.

## S2 — Coordination

- State: C
- Function: attenuate operational interference between concurrent project-agent work cells through isolated workers, per-task single-live-run admission and capacity-aware waiting.
- Disturbance / variety regulated: two attempted runs on the same task, multiple task turns sharing a worker's files, and agents competing for sandbox host execution capacity.
- Distinct S1 units: separate project-agent task runs, potentially simultaneous on distinct workers/tasks.
- Inter-S1 disturbance: overlapping starts would collide on task ownership/review state; reused shared workspaces risk stale file contamination, while shared host capacity can cause execution contention.
- Attenuating coordination relation: first-party task-run admission/status guards and worker-scoped workspace/delivery box, capacity queues and optional host heavy-phase leases.
- Feedback into subsequent S1 behaviour: denied/already-running starts do not spawn another worker; queued starts wait for available capacity; a settled turn frees its worker slot, allowing later authorized work.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the paths target explicit concurrent-run/cross-task file/host-contention disturbances, not merely task handoff or a mailbox.
- Decisive decision or feedback right: decide that conflicting starts should be refused or capacity-parked and that isolation/leases should govern subsequent starts.
- Decision owner: first-party deterministic platform safety and admission rules; no Tale agent is established as owning a discretionary project-wide S2 coordination response in the credited base mode. This is a bounded S2-specific constructor/coordination path rather than `A`.
- Supporting / enforcement mechanisms: transactional run gates, standing worker allocation, task-specific output boxes, capacity retries and host lease tools.
- Closure path: competing/oversubscribed start → guarded admission, isolated worker or capacity park → next start resumes only after resource/turn clearance.
- Boundary reachability: ordinary shipped task-run/worker path; no extension-only coordinator is required.
- Why this is / is not agent-owned: changing platform admission rules requires developer/operator composition; the configured work agent does not choose the S2 collision policy. `C` is credited to its concrete S2-specific path, not generic ability to send messages.
- Evidence: [standing worker isolation](https://github.com/tale-project/tale/blob/b2560c2d7d3294993e66129c891be4a059f3d6c4/services/platform/backend/core/tasks/agent_run_host.ts#L158-L165); [task-specific delivery box](https://github.com/tale-project/tale/blob/b2560c2d7d3294993e66129c891be4a059f3d6c4/services/platform/backend/core/tasks/agent_run_host.ts#L314-L341); [host lease admission](https://github.com/tale-project/tale/blob/b2560c2d7d3294993e66129c891be4a059f3d6c4/services/platform/backend/core/tasks/agent_run_host.ts#L1120-L1173); [start tool occupancy semantics](https://github.com/tale-project/tale/blob/b2560c2d7d3294993e66129c891be4a059f3d6c4/services/platform/backend/core/node_only/sandbox/workspace_tools_bridge.ts#L308-L349).
- Basis: structural.
- Confidence: medium-high.
- Caveats: mechanical isolation and exclusive-run rules do not imply that a model agent owns coordination discretion; host leases alone are not an organizational S2 decision.

## S3 — Inside-and-now control

- State: A(P)
- Function: regulate current project-wide task priorities, assigned operational commitments and intervention/review handling across multiple agent work cells.
- Disturbance / variety regulated: competing unfinished tasks, changing assignments, blocked reviews, stale execution/review state and limited project-agent capacity.
- Whole-system current view: project/board-wide `task_find` lists task status, priority/assignee and captured review; `task_get` exposes task dependencies, current run and pending review.
- Current-control decision scope: choose priority/agent assignment, start/resume another qualified agent, redirect a captured review to a different eligible independent agent, and decide which work receives next attention; operator task views/actions can exercise parent control separately.
- Decisive decision or feedback right: project-wide assignment/priority and review-intervention choices based on current task portfolio, beyond one task's own model/tool steps.
- Decision owner: base mode — explicitly granted manager agent with project-wide task authority; parent mode — legitimate project operator/editor acting through normal board/project task controls.
- Supporting / enforcement mechanisms: scoped tool grants, expected-value/CAS task mutations, current run identity, protected review transfer, capacity checks and status writes.
- Closure path: manager's project task view → discretionary priority/assignment/review-transfer choice → guarded platform write → later agent starts/reviews use revised state; alternatively the human project operator chooses and commits an equivalent update through the UI/API.
- Boundary reachability: Tale ships supported task-find/get/update/start/delegate-review tools for project agents; manager rights must be explicitly granted in the project. Direct operator task management is a first-party platform mode. Neither is a repository-maintainer or adjacent dogfood actor.
- Why this is / is not agent-owned: in manager mode, remove the manager's judgment and no project-wide choice of which task/agent/review to prioritize remains, only platform guards. In parent mode the operator owns that choice; neither platform lock nor scheduler is itself the decision owner.
- Evidence: [project-wide task observation](https://github.com/tale-project/tale/blob/b2560c2d7d3294993e66129c891be4a059f3d6c4/services/platform/backend/core/node_only/sandbox/workspace_tools_bridge.ts#L197-L282); [manager priority, assignment and review delegation](https://github.com/tale-project/tale/blob/b2560c2d7d3294993e66129c891be4a059f3d6c4/services/platform/backend/core/node_only/sandbox/workspace_tools_bridge.ts#L308-L377); [native task writes and actor paths](https://github.com/tale-project/tale/blob/b2560c2d7d3294993e66129c891be4a059f3d6c4/services/platform/backend/domains/tasks/service.ts); [project task review and task UI](https://github.com/tale-project/tale/blob/b2560c2d7d3294993e66129c891be4a059f3d6c4/services/platform/backend/rest/v1-tasks.ts).
- Basis: explicit + structural.
- Confidence: medium-high for optional configured manager and project operator modes.
- Caveats: having a `manager` label or an automatic scheduler alone is not evidence. The decisive right here is the explicitly scoped live manager's discretionary whole-project task-choice path. Ordinary operator approval of one output does not supply the S3 parent claim.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | live manager agent with project-wide task grants | current board/blocked-review/task portfolio observed through task tools | choose priority/assignee/review intervention → guarded mutation → subsequent agent operation follows updated current commitments | `workspace_tools_bridge.ts` task_find, task_update_metadata, task_start_agent and task_delegate_review |
| Parent (`P`) | authorized human project member/operator | project board and task-management UI/API | human selects task priority/assignment/current intervention → persisted task state → next execution/review follows it | `backend/domains/tasks/service.ts`, `backend/rest/v1-tasks.ts` |

## S3* — Complementary audit

- State: A
- Function: independently challenge an agent-produced task completion claim using source-bound artifacts and a distinct reviewer agent, returning a corrective or approving decision.
- Disturbance / variety regulated: misleading or stale self-reports, missing/inadequate output evidence, self-review conflicts, and acceptance claims unsupported by the actual task artifacts.
- Claim being audited: the implementation agent's settled run and current task evidence support completion/acceptance.
- Ordinary reporting path: implementation run's task comment and harvested deliverables enter `in_review`; the implementing agent cannot move its own task to done.
- Complementary access path: a designated distinct review agent can read the captured source run, access available input/output files via guarded `stage_file`, perform independent checks and submit structured check/PR evidence.
- Independence boundary: the reviewer must differ from `implementationAgentId`, must have the captured pending review/grant and matching evidence revision; human-competence and human-only gates cannot be bypassed.
- Who acts on findings: the reviewer agent itself chooses approve/request_changes. A serializable review transaction atomically moves the task to `done` or back to `todo`, posts feedback and records the decision; a separate implementation agent can then repair the task.
- Decisive decision or feedback right: judging the result of a separate operational run from independently accessed artifacts rather than accepting worker status.
- Decision owner: authorized distinct reviewing model agent; platform validates source identity and commits the verdict but does not choose approve/request_changes.
- Supporting / enforcement mechanisms: source/evidence-revision CAS, staged files, structured checks, independent reviewer-ID guard, native approval record and audit log.
- Closure path: settled worker run → captured evidence and independent reviewer access → reviewer verdict + explanation → guarded task status/feedback transaction → acceptance or a subsequent correction run.
- Boundary reachability: a native first-party project-agent review mode is shipped; the reviewer must be separately granted the task-review tool and assigned an eligible captured review. This is not Tale OSS CI and not merely the worker's own routine tests.
- Why this is / is not agent-owned: removing the reviewing agent leaves a schema/permission gate but no independent verdict on artifacts. The worker cannot impersonate the independent reviewer; the model reviewer chooses the corrective judgment.
- Evidence: [captured source and distinct reviewer validation](https://github.com/tale-project/tale/blob/b2560c2d7d3294993e66129c891be4a059f3d6c4/services/platform/backend/domains/tasks/agent-review.ts#L131-L230); [native verdict and returned task status](https://github.com/tale-project/tale/blob/b2560c2d7d3294993e66129c891be4a059f3d6c4/services/platform/backend/domains/tasks/agent-review.ts#L292-L419); [review file staging and reviewer tool contract](https://github.com/tale-project/tale/blob/b2560c2d7d3294993e66129c891be4a059f3d6c4/services/platform/backend/core/node_only/sandbox/workspace_tools_bridge.ts#L366-L405).
- Basis: explicit + structural.
- Confidence: high for the supported independently assigned agent-review mode.
- Caveats: the server cannot independently verify the substantive truth of every reviewer-supplied check, and native review is not necessarily a default path for every project. This positive finding relies on a separate authorized review agent examining actual evidence, not on the deterministic verdict parser or generic review label.

## S4 — Outside-and-then intelligence

- State: —
- Function: no distinct external-and-prospective project capability adaptation loop is established beyond task work and current automation/operational controls.
- Disturbance / variety regulated: Tale agents can research outside information for their assigned tasks and automation can schedule later runs, but these do not alone generate and return a project-level future capability strategy.
- Decisive decision or feedback right: no supported first-party S4-level prospective adaptation authority and return into capability is established.
- Decision owner: not established for S4.
- Supporting / enforcement mechanisms: task research/web tools, project history, automation editors/schedules, project instruction editing, agent/model configuration, recurring tasks and task-level planning.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: a model carrying out a foresight research task is S1 unless its result enters an established project capability-adaptation conversation. A schedule or prompt change does not itself close that distinct loop.
- Evidence: [task tool catalog](https://github.com/tale-project/tale/blob/b2560c2d7d3294993e66129c891be4a059f3d6c4/services/platform/backend/core/node_only/sandbox/workspace_tools_bridge.ts); [platform automations](https://github.com/tale-project/tale/tree/b2560c2d7d3294993e66129c891be4a059f3d6c4/services/platform/backend/core/automations); [project instructions](https://github.com/tale-project/tale/blob/b2560c2d7d3294993e66129c891be4a059f3d6c4/services/platform/backend/domains/projects/service.ts#L1076-L1122).
- Basis: structural negative search.
- Confidence: medium.
- Caveats: operators could compose future planning and adaptation tasks, but a hypothetical configured workflow is not a shipped independent S4 closure. No claim is made that future implementations cannot supply one.

### Absence scope

- Surfaces inspected: ordinary task/manager/review tools, project instructions and agent definitions, automation/scheduled agent runs, run recovery and history, provider/model settings, README-supported deployed paths, and nearby development/test/evaluation surfaces.
- Plausible first-party paths checked: project manager's planning, automation triggers, model/provider selection, task research, history/memory/retries, governance policy and task improvement feedback.
- Why no material first-party path remains: these paths regulate present tasks, permissions, or immediate follow-up. No shipped project-level outside/future environmental model coupled to prospective capability-option selection and return into ongoing operations is evidenced at this boundary.

## S5 — Policy and identity

- State: P
- Function: establish durable project-purpose and governing instructions that subsequent project-agent operation must obey.
- Disturbance / variety regulated: project goal drift, incompatible instructions, unauthorized scope changes, and changes to the owner's project-level operating rules.
- Identity / ultimate-policy issue: what the project is for, what instructions/constraints its agents operate under, and which rules are authoritative across future task runs.
- Ultimate authority in each claimed mode: a legitimate authorized project owner/editor changes project instructions; a task worker or manager is not shown to possess a shipped autonomous right to redefine this project identity without separately granted parent authority.
- Return-to-operation path: updated project instructions are persisted in the project record and read into the agent-run task context for later work.
- Decisive decision or feedback right: approve and persist the project's authoritative durable instructions.
- Decision owner: authorized parent project editor/operator.
- Supporting / enforcement mechanisms: project permissions, expected hash and audit logging, durable project table, mandatory context-injection helpers, run instruction snapshot.
- Closure path: project identity/instruction change proposed → authorized editor chooses content → version-checked persistent update → later task-agent launch reads the project instructions and the agent's work is governed by them.
- Boundary reachability: first-party supported project configuration/update operation and standard run preparation. No contributor governance or unshipped policy agent is credited.
- Why this is / is not agent-owned: agent task tools can act within granted scope but do not by themselves select legitimate ultimate project-purpose changes; the parent editor holds the decision while the platform records and returns it. A task-level approval and static safety filter alone would not establish S5.
- Evidence: [authorized persistent project-instruction update](https://github.com/tale-project/tale/blob/b2560c2d7d3294993e66129c891be4a059f3d6c4/services/platform/backend/domains/projects/service.ts#L1076-L1122); [task-run instruction capture](https://github.com/tale-project/tale/blob/b2560c2d7d3294993e66129c891be4a059f3d6c4/services/platform/backend/core/tasks/agent_run_host.ts#L198-L265); [project agent instructions](https://github.com/tale-project/tale/blob/b2560c2d7d3294993e66129c891be4a059f3d6c4/services/platform/backend/domains/projects/service.ts#L2260-L2317).
- Basis: explicit + structural.
- Confidence: medium.
- Caveats: this parent mode concerns project purpose/operating identity, not all platform-wide security policy or the Tale repository's maintainer decisions. No internal autonomous S5 decision path is credited.

## Distributed OSS parent arrangement

The Tale OSS maintainers and contributor organization are adjacent to this deployed project operating cell. The project parent mode is the deployment's legitimate owner/editor, not an inferred OpenSiro/Tale repository-level governance actor. Independently running project members do not constitute a single project-wide parent merely because they share source code.

## Self-hosted and non-human modes

Self-hosted project deployment permits ordinary human task/agent configuration and explicit manager/reviewer agent grants. Manager and reviewer agent closure is credited only in supported configured modes with actual project-wide or captured review authority. A human approval of a single output is not promoted to S5; project instruction/purpose ownership is a separate stronger parent loop.

## Recursion

The assessed recursion is one Tale project. Durable agent turns are operational cells inside it; an external harness may run its own nested workers, but spawning processes and sharing a sandbox alone do not prove another complete Tale-owned viable recursion. Tale OSS development and organization-wide SaaS operations are excluded.

## Variety and escalation

Task agents absorb local task/tool variety; run gates and isolated workers attenuate collision/capacity variety; a project manager can redirect current commitments and reviews; independently assigned reviewers challenge completion claims. Human project control receives decisions that exceed configured agent grants. Task wait/failure/review status is observable, but the mere existence of a `blocked` or `in_review` board state is not by itself an algedonic channel or another VSM function.

## Evidence gaps

- Source-level assessment, not a live multi-provider end-to-end execution: claims are bounded to shipped code, documented supported modes and deterministic tests.
- The optional manager mode's practical effectiveness, and whether projects routinely grant sufficient project-wide discretion, are deployment-dependent; the state describes the supported path, not usage prevalence.
- The separate agent reviewer is mechanically independent of the implementation agent, but the substantive quality and externality of review evidence vary by configured reviewer and provided task artifacts.
- No positive S4 inference is made from configurable automations, future-looking task prompts or third-party agents' internal self-improvement.

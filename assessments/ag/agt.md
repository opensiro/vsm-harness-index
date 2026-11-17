---
harness_id: agt
project_name: agt
repository: https://github.com/blacsheep/agt
review_ref: 14ff89edc8f4f3c9e7be2c45ae11c903a794f5f0
reviewed_at: 2026-11-17
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: —
autonomy_s4: A
autonomy_s5: —
---

# agt

## Review boundary

- System in focus: One local agt workspace with the shipped lead and dynamically configured agent team, first-party scheduler, task tools and model runtime.
- Purpose and identity: Transform an owner's goals into a self-created and coordinated agent team that completes work in chats and tracked tasks.
- Relevant environment: User's project files, data/tool providers, optional external Codex/Claude/DeepSeek harnesses, and local human operator.
- Standard-distribution boundary: Shipped Rust CLI/Web console, native agent loop, default lead prompt, resource management/task collaboration, scheduler and SQLite state.
- Credited operating / distribution surfaces: Lead model and built-in tools, team/group chats, durable task queue, exclusive resources, goals, permissions, active team/queue oversight and tool creation mode.
- Adjacent first-party surfaces excluded from ownership: Demo videos, external agent runtime internals, separate Werewolf project, repo CI/release process and private human-specific instructions.
- First-party operating / deployment modes considered: Built-in lead and multiple hosted agents, optional external harness agent as a worker, scheduled discussions, task collaboration, opt-in parallel work, independent owner intervention.
- Recursion level: One local owned workspace; lead is a project-level organizational agent, specialists are operational S1 units, user is legitimate parent in a distinct mode.
- Reviewed revision: 14ff89edc8f4f3c9e7be2c45ae11c903a794f5f0.
- Observation date: 2026-11-17.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

agt uses Rust crates for an agent model/tool engine, resource/permissions, persistent conversations, and scheduler/task/goal handling. A standard lead uses first-party resource_management to create or change role prompts, agent identities and tools and task_collaboration to assign/await/receive reports. SQLite stores chats/tasks/sessions/approvals; the scheduler serializes identity work, controls authorized discussion concurrency and supports recovery. With parallel work enabled, tasks declare exclusive resources to avoid incompatible simultaneous work. [overview](https://github.com/blacsheep/agt/blob/14ff89edc8f4f3c9e7be2c45ae11c903a794f5f0/README.md); [lead](https://github.com/blacsheep/agt/blob/14ff89edc8f4f3c9e7be2c45ae11c903a794f5f0/docs/guide/lead-team.md); [tasks](https://github.com/blacsheep/agt/blob/14ff89edc8f4f3c9e7be2c45ae11c903a794f5f0/docs/guide/tasks.md).

## Operational model

The lead autonomously assembles teams, delegates to agents and reacts to tracked results. Shared resource contention is exposed by specific exclusion and lease mechanisms; a lead can make conflict-aware task changes. Current tasks and goals are visible to both the lead and a separate human owner control mode. A lead may adapt future capacity by commissioning and registering tools and assigning newly created agents. Permission review of intended tools is not independent inspection of completed operational claims. This is fixed-ref source assessment, not a provider-backed runtime transcript.

## S1 — Operations

- State: A
- Function: Deliver open-ended user goals by model-backed agents making task, message and tool choices in supported chats.
- Disturbance / variety regulated: Unpredictable user requirements, tool outcomes, teammates' results and incomplete tasks.
- Decisive decision or feedback right: An active model-backed lead or specialist decides whom to message, which tool to use, what work to attempt and how to follow up.
- Decision owner: First-party configured model loop for lead and team members; remote coding-harness adapters supply optional S1 execution but do not own the native lead's project choices.
- Supporting / enforcement mechanisms: Agent-bound resource tools, MCP, sessions, scheduler, SQLite and approval gates.
- Closure path: User goal → model tool calls/task delegation → worker result → model follow-up or report in initiating conversation.
- Boundary reachability: CLI/Web quick start creates a lead with shipped prompt, resource_management and task_collaboration; native model loop is supported.
- Why this is / is not agent-owned: The model decides substantive next investigative/team actions; deterministic transport/permission does not decide the content.
- Evidence: [lead setup](https://github.com/blacsheep/agt/blob/14ff89edc8f4f3c9e7be2c45ae11c903a794f5f0/docs/guide/lead-team.md); [tracked task lifecycle](https://github.com/blacsheep/agt/blob/14ff89edc8f4f3c9e7be2c45ae11c903a794f5f0/docs/guide/tasks.md); [native engine](https://github.com/blacsheep/agt/blob/14ff89edc8f4f3c9e7be2c45ae11c903a794f5f0/crates/agt-runtime/src/engine/native.rs)
- Basis: structural
- Confidence: high
- Caveats: Requires configured provider; example recordings and external harness execution are not proof of independent internal VSM functions.


## S2 — Coordination

- State: A
- Function: Attenuate real contention when independent team agents might work on the same resources and duplicate or overwrite work.
- Disturbance / variety regulated: Simultaneous tasks sharing named exclusive resources, duplicate requests and race conditions between agents editing common artifacts.
- Decisive decision or feedback right: Lead agent selects assignees, task priority and claimed resources, and revises queue/dependencies after blockers or conflicting outcomes.
- Decision owner: Model-backed lead in supported mode owns the coordination choice; scheduler enforces declared resource exclusion, revision guards and idempotent request keys.
- Supporting / enforcement mechanisms: Persistent tasks, exclusive_resources, revision CAS, queue guard/aging and scheduler concurrency limits.
- Closure path: Agent task claims → overlap/unknown outcome blocks other claims → lead sees task state and reports → adjusts assignee/resource/queue, and scheduler applies new admissible work.
- Boundary reachability: First-party task_collaboration manager available to configured lead; optional scheduler.parallel_work plus documented exclusive resources.
- Why this is / is not agent-owned: Scheduler does not pick which conflicting business objective wins; lead's model-directed task revisions and choices retain discretion, bounded by deterministic exclusion.
- Distinct S1 units: Lead and multiple independent worker/research/coding agents with separate execution sessions and bound resources.
- Inter-S1 disturbance: Two tasks can touch the same named project files/operations concurrently and could overwrite each other; interrupted outcomes must not be retried while resources are held.
- Attenuating coordination relation: First-party task exclusive_resources block overlapping work; lead-managed priorities, dependencies and outcome_unknown resolution change future dispatch.
- Feedback into subsequent S1 behaviour: Blocking states, task reports and revisioned queue changes determine which worker is admitted to execute afterward.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The code and docs specify explicit shared-resource mutual exclusion, uncertain-outcome fences and conflict-aware deferred work, not merely a mailbox.
- Evidence: [resource exclusion and outcome_unknown](https://github.com/blacsheep/agt/blob/14ff89edc8f4f3c9e7be2c45ae11c903a794f5f0/docs/guide/tasks.md); [queue/CAS](https://github.com/blacsheep/agt/blob/14ff89edc8f4f3c9e7be2c45ae11c903a794f5f0/crates/agt-runtime/src/work/queue.rs); [scheduler fencing](https://github.com/blacsheep/agt/blob/14ff89edc8f4f3c9e7be2c45ae11c903a794f5f0/crates/agt-runtime/src/scheduler/lease.rs); [lead delegation](https://github.com/blacsheep/agt/blob/14ff89edc8f4f3c9e7be2c45ae11c903a794f5f0/docs/guide/lead-team.md)
- Basis: structural
- Confidence: medium
- Caveats: Exclusive resource keys are conventions agents must use consistently; when absent, the scheduler cannot discover arbitrary filesystem conflicts.


## S3 — Inside-and-now control

- State: A(P)
- Function: Manage the team's current work commitments, agent roster and blocked assignments across one local workspace.
- Disturbance / variety regulated: Current task backlog, stalled outcomes, disabled workers, urgency changes, pending returns and finite concurrent slots.
- Decisive decision or feedback right: Lead inspects current agents/tasks and reassigns, reprioritizes, cancels or creates work and restores progress; workspace owner has a distinct dashboard/CLI management mode.
- Decision owner: Base: model-backed lead with task and resource-management capabilities. Parent mode: human workspace owner with Web Tasks/Agent team current controls.
- Supporting / enforcement mechanisms: Scheduler, goals, task state, hard reply/time limits, team listing and persistent conversations.
- Closure path: Team/task/goal state and returned worker messages → lead or owner makes present assignment/intervention → tools and scheduler change who works next.
- Boundary reachability: Bundled lead prompt and task/resource tools; owner console displays all team work and exposes queue/agent stop/retry/reassign options.
- Why this is / is not agent-owned: Lead is an actual model participant deciding task portfolio; human's separate current-operations mode does not turn every lead choice into parent governance.
- Whole-system current view: Task queue, agent roster, goals, live conversation statuses and pending approvals across the local workspace.
- Current-control decision scope: Current work priority, responsible agent/team membership, resumption/stop and resolution of unknown outcomes.
- Evidence: [lead agency](https://github.com/blacsheep/agt/blob/14ff89edc8f4f3c9e7be2c45ae11c903a794f5f0/docs/guide/lead-team.md); [goal and current queue control](https://github.com/blacsheep/agt/blob/14ff89edc8f4f3c9e7be2c45ae11c903a794f5f0/docs/guide/tasks.md); [goal watcher](https://github.com/blacsheep/agt/blob/14ff89edc8f4f3c9e7be2c45ae11c903a794f5f0/crates/agt-runtime/src/goals.rs); [scheduler limits](https://github.com/blacsheep/agt/blob/14ff89edc8f4f3c9e7be2c45ae11c903a794f5f0/docs/modules/scheduler.md)
- Basis: structural
- Confidence: medium-high
- Caveats: Parent user still owns workspace standing permissions and can intervene; C/P modes never imply shared oversight across unrelated installations.


### Mode matrix — S3 A(P)

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Model-backed lead | Task reports, conflict or backlog changes | Agent-owned task/roster decision changes subsequent schedule | [task tools](https://github.com/blacsheep/agt/blob/14ff89edc8f4f3c9e7be2c45ae11c903a794f5f0/docs/guide/tasks.md) |
| Parent (`P`) | Legitimate human workspace owner | Whole-workspace queue and blocked/unknown-outcome view | Owner reprioritizes/resolves/cancels/restarts work through console and changes next active run | [owner work controls](https://github.com/blacsheep/agt/blob/14ff89edc8f4f3c9e7be2c45ae11c903a794f5f0/docs/guide/tasks.md) |

## S3* — Complementary audit

- State: —
- Function: No installed claim-relative independent review of actual ordinary team operations is established.
- Disturbance / variety regulated: Specialists can make faulty claims; independent observation of their primary artifacts would be needed for complementary operational audit.
- Decisive decision or feedback right: No separate installed audit owner proved to receive operational evidence and feed corrections back to the lead.
- Decision owner: Not established within the base lead/team standard distribution.
- Supporting / enforcement mechanisms: Optional model permission reviewer examines contemplated tool arguments; user can create a critic agent in a research group; scheduler records traces.
- Closure path: Permission review gates future action but does not independently inspect completed team output; example critic receives reports, not a proved complementary primary-artifact audit path.
- Boundary reachability: Reviewer mode is a first-party permission feature, but is not an operational-audit path merely by being separate.
- Why this is / is not agent-owned: Prospective tool authorization and report-only debate do not establish S3*; no first-party audit-then-return loop tied to actual S1 production found.
- Evidence: [tool authorization review](https://github.com/blacsheep/agt/blob/14ff89edc8f4f3c9e7be2c45ae11c903a794f5f0/crates/agt-runtime/src/permission/model_review.rs); [team critic example](https://github.com/blacsheep/agt/blob/14ff89edc8f4f3c9e7be2c45ae11c903a794f5f0/docs/guide/lead-team.md); [result reports](https://github.com/blacsheep/agt/blob/14ff89edc8f4f3c9e7be2c45ae11c903a794f5f0/docs/guide/tasks.md)
- Basis: structural
- Confidence: medium
- Caveats: A configured custom specialist might be an auditor; user-authored composition outside assessed first-party setup not inferred.

### Absence scope

- Surfaces inspected: Built-in permission model-review, discussion critic example, task logs and result path.
- Plausible first-party paths checked: Prospective reviewer gate, specialist report debate and model approval; none has a separate primary-output access plus operational feedback route.
- Why no material first-party path remains: No shipped claim-relative, complementary primary-artifact examination and return to current control was found; creating an auditor is a user-built mode.


## S4 — Outside-and-then intelligence

- State: A
- Function: Change the future team's capabilities when requirements expose missing roles, tools or integrations.
- Disturbance / variety regulated: A new task demands expertise, API connectors or isolated tooling that the current team lacks.
- Decisive decision or feedback right: The model-backed lead decides which agent roles and new tool capabilities are needed, commissions a coding harness, tests/registers the new MCP and binds it to future workers.
- Decision owner: First-party lead model in the documented dynamic-team mode; coder model can create code, while the lead determines and activates the capacity change within permission envelope.
- Supporting / enforcement mechanisms: Resource management tools for prompts/models/agents/MCPs, remote coding harness runner, tool probing, named permissions and persistent resource files.
- Closure path: Future-relevant task/tool gap → lead's adaptation plan → coded/probed MCP and new agent role → registered/granted to the team → subsequent work uses the new capability.
- Boundary reachability: Shipped lead prompt explicitly teaches discover/reuse/build/test/bind on ordinary user goals; resource_management and task_collaboration are first-party built-ins.
- Why this is / is not agent-owned: The lead interprets the unmet requirement and chooses new capabilities; file persistence and API checks are supporting mechanisms, not the adaptation decision maker.
- External distinction: Incoming goal's external requirements and newly encountered absent integration relative to currently listed models/agents/tools.
- Future / prospective distinction: The team prepares reusable capabilities and role definitions for subsequent work rather than only completing the present atomic tool call.
- Adaptation option generated: Agent role or new MCP service, with model-directed test, registration and per-agent binding.
- Path back into current capability / S3: The lead changes the workspace agent/tool inventory, and subsequent scheduler-dispatched roles can execute the new configured tool.
- Evidence: [first-party toolsmith adaptation](https://github.com/blacsheep/agt/blob/14ff89edc8f4f3c9e7be2c45ae11c903a794f5f0/docs/guide/lead-team.md); [resource-managed teams](https://github.com/blacsheep/agt/blob/14ff89edc8f4f3c9e7be2c45ae11c903a794f5f0/README.md); [builtin tool registry](https://github.com/blacsheep/agt/blob/14ff89edc8f4f3c9e7be2c45ae11c903a794f5f0/crates/agt-service/src/tools.rs)
- Basis: structural
- Confidence: medium
- Caveats: The actual tool-building example depends on an optional configured external coding harness and explicit approval permissions; mere generic scripting is not independently counted.


## S5 — Policy and identity

- State: —
- Function: No first-party ultimate-identity conflict escalation/ratification loop shown for the local agent organization.
- Disturbance / variety regulated: Identity, constitutional purpose and standing limits could require an ultimate choice outside task-level permissions.
- Decisive decision or feedback right: No qualifying first-party authority forum/owner and return-to-operation path for fundamental policy disputes shown.
- Decision owner: Human workspace owner controls standing permissions and agent prompts, but no S5 closure beyond ordinary authorization is evidenced.
- Supporting / enforcement mechanisms: Per-tool approval, permission policies, lead bootstrap instructions, resource identities and user stop controls.
- Closure path: The runtime enforces configured permission decisions on tool operations; there is no evidenced identity-level tension/ratification and returned constitutional change.
- Boundary reachability: Human controls are installed but configure/approve current actions rather than run a policy-identity deliberation path.
- Why this is / is not agent-owned: The lead can create roles and tools, but changing a task roster or requiring user approval is not by itself an S5 constitutional decision.
- Evidence: [lead and owner limits](https://github.com/blacsheep/agt/blob/14ff89edc8f4f3c9e7be2c45ae11c903a794f5f0/docs/guide/lead-team.md); [approval boundary](https://github.com/blacsheep/agt/blob/14ff89edc8f4f3c9e7be2c45ae11c903a794f5f0/crates/agt-runtime/src/permission/model_review.rs); [operating constraints](https://github.com/blacsheep/agt/blob/14ff89edc8f4f3c9e7be2c45ae11c903a794f5f0/docs/modules/scheduler.md)
- Basis: structural
- Confidence: medium
- Caveats: No assumption that maintainer governance or private user policy documents supply in-boundary S5.

### Absence scope

- Surfaces inspected: Agent prompt and resource creation tools, workspace owner approvals, scheduler limits, credential and permission handling.
- Plausible first-party paths checked: User standing approval choices, lead role creation and policy/permission edits; no authoritative ultimate-identity question and closed return.
- Why no material first-party path remains: Inspected paths enforce selected rules or create ordinary roles, without ratification of a genuine identity-level dispute.

## Distributed OSS parent arrangement

The public GitHub maintainers do not own private local team decisions. This assessment does not infer shared organization-wide governance from multiple users or optional external harnesses.

## Self-hosted and non-human modes

agt is a locally installed single-owner workspace, not a shared multi-tenant service. A fully autonomous lead/team mode is supported within explicit tool and permission grants; owner controls form a distinct parent mode only for current S3, not S5.

## Recursion

Lead/team roles are inside the local workspace boundary; an external coding agent can be a worker through a first-party adapter but its upstream internal management is not imported. The owner/parent has standing discretion over authorization; shipped operational modes determine actual ownership.

## Variety and escalation

Runtime tasks and chat feedback reduce operating variety; resource exclusion mitigates concurrent interference and uncertain-outcome retries; lead goals and task state feed current work decisions. Missing tools/roles trigger optional team-capability construction rather than forcing a new manual topology. Tool approval/deny is escalation about an action, not ultimate policy.

## Evidence gaps

- No provider-backed end-to-end run, conflict-resolution replay or independent external reviewer execution in this assessment.
- S2=A requires the shipped lead model with task-management authority and correctly declared exclusive_resources; arbitrary chat systems without those controls cannot claim it.
- S4=A is limited to the documented dynamic team/tool construction path, not generic conversation memory or unconnected planning.
- No custom externally defined review agent is silently credited as a shipped S3* auditing mode.

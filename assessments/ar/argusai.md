---
harness_id: argusai
project_name: ArgusAI
repository: https://github.com/HG-ha/Argusai
review_ref: 5f7aa0844ae0341f3563da2a4d171e3fb797d3ac
reviewed_at: 2026-11-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: P
---

# ArgusAI

## Review boundary

- System in focus: One locally operated ArgusAI assistant workspace, its model-bearing native sessions, first-party tools, standing Team Room and delegated agent sessions, persistent goals and scheduler, plus the legitimate installation-owner controls. Not the users' security organization or an external Codex/Claude/Cursor Agent's separately owned control plane.
- Purpose and identity: Carry out user-authorized work across security scanning, browser/proxy inspection, reverse-engineering and evidence/reporting, with bounded multi-agent collaboration and recurrent execution.
- Relevant environment: User goals and intervention, live browser/proxy/tool state, Tasks/ReverseJobs, persistent Case/Evidence material, peer assignments, concurrent message queues, external models and ACP runtimes, scheduling and credentials/permissions.
- Standard-distribution boundary: Desktop GUI, CLI and Python core expose native model/tool loops and optional ACP connections, installed built-in agent-team and Cron tools. The native assistant provides model calls if configured; selected external ACP agents remain independent providers of their own execution reasoning.
- Credited operating / distribution surfaces: [native session/tool loop](https://github.com/HG-ha/Argusai/blob/5f7aa0844ae0341f3563da2a4d171e3fb797d3ac/argusai/core/assistant/session_chat_loop.py), [assistant tool registry](https://github.com/HG-ha/Argusai/blob/5f7aa0844ae0341f3563da2a4d171e3fb797d3ac/argusai/core/assistant/session_tool_methods.py), [agent threads/team input](https://github.com/HG-ha/Argusai/blob/5f7aa0844ae0341f3563da2a4d171e3fb797d3ac/argusai/core/assistant/agent_threads.py), [standing teams and owner editing](https://github.com/HG-ha/Argusai/blob/5f7aa0844ae0341f3563da2a4d171e3fb797d3ac/argusai/gui/teams.py), [Cron runtime](https://github.com/HG-ha/Argusai/blob/5f7aa0844ae0341f3563da2a4d171e3fb797d3ac/argusai/core/assistant/cron.py), [skill/catalog controls](https://github.com/HG-ha/Argusai/blob/5f7aa0844ae0341f3563da2a4d171e3fb797d3ac/argusai/core/assistant/skills.py), [case evidence](https://github.com/HG-ha/Argusai/blob/5f7aa0844ae0341f3563da2a4d171e3fb797d3ac/argusai/core/workspace/cases.py).
- Adjacent first-party surfaces excluded from ownership: Marketing screenshots and product diagrams, tests and developer CI, packaged browser/proxy/scan engines without their own model decisions, external ACP agent projects, optional MCP extensions and the company security/incident-response parent outside this local installation.
- First-party operating / deployment modes considered: Native assistant with selected model endpoint, one-session work, temporary readonly/scoped subagent squad, persistent multi-agent Team Room, optional external ACP session/child, owner-operated GUI team management, recurring interval/Cron/webhook/file-change tasks.
- Recursion level: One installation/workspace and its persistent or temporary multi-agent team, with independently executing session agents as S1 units. External security organizations and individual scan engines are not automatically further full VSM recursions.
- Reviewed revision: `5f7aa0844ae0341f3563da2a4d171e3fb797d3ac`.
- Observation date: 2026-11-04.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

ArgusAI is a Python local security workbench with GUI, CLI, native streaming model/tool sessions, selectable outside ACP runtimes, scoped persistent child agents and multi-agent Team Rooms. One main model selects tools against stateful Tasks, browser tabs, proxy traffic, scans, reverse jobs, evidence and files. Delegated children have their own histories, roles and capability projections. Persistent Team Room messages carry sequence/cursors; member execution inboxes save separate pending inputs and queue busy members without interrupting active work. A Cron scheduler persists trigger/run/checkpoint information and routes future work into selected sessions. The owner can create and recharter a standing team and edit member roles/objectives, which return through saved records and an injected event. Host locks, permissions, automatic deduplication, session-state and tool-batch scheduling are supporting machinery; none is itself a model's organizational decision. [English architecture](https://github.com/HG-ha/Argusai/blob/5f7aa0844ae0341f3563da2a4d171e3fb797d3ac/README.en.md), [implementation guide](https://github.com/HG-ha/Argusai/blob/5f7aa0844ae0341f3563da2a4d171e3fb797d3ac/wiki/Architecture-and-Development.md), [threads](https://github.com/HG-ha/Argusai/blob/5f7aa0844ae0341f3563da2a4d171e3fb797d3ac/argusai/core/assistant/agent_threads.py).

## Operational model

An authenticated installation owner sets a goal and authorized scope. The native assistant's model reasons over current session and workspace state, discovers/executes tools, maintains Todo evidence and can spawn readonly/scoped agents or control a standing team. Members execute separate work, receive delayed peer requests and may choose to respond, pass or hand off. Parent agent receives completion notices and may inspect source artifacts, revise the live plan, dispatch further work, or deliver an evidence-backed result. Persistent team charter/role edits occur through saved owner controls. Cross-session knowledge and future triggers may extend operations but must be distinguished from genuine prospective S4 intelligence and separate complementary S3* audit.

## S1 — Operations

- State: A
- Function: Carry out security-analysis and general assistant operations through model-selected tools and separate task-performing children.
- Disturbance / variety regulated: Uncertain code/traffic observations, new user materials, scan errors, tool outputs, environment and evidence changes.
- Decisive decision or feedback right: Select and sequence domain tools, analyze returned evidence and choose next investigation/validation/report action.
- Decision owner: Configured native model-bearing ArgusAI assistant, or connected model-bearing child where given an explicit bounded role; external ACP engines are not credited as ArgusAI's independent cognitive design.
- Supporting / enforcement mechanisms: Model/tool call loop, domain tool catalog, run/stream state, content archives, confirmation broker and scoped child capability projection.
- Closure path: User-defined scope → model/tool call on live workspace → task/evidence output → model inspects and continues/terminates → report or next task state.
- Boundary reachability: The native model/tool engine and first-party domain registry are wired into normal GUI/CLI operation, and child tool selection is registered in the shipped assistant. An external ACP model is an alternative supported operating mode, not required for the native witness.
- Why this is / is not agent-owned: The model chooses substantive task actions; deterministic policy, progress guards and run queues enforce limits rather than owning the choice.
- Evidence: [assistant loop](https://github.com/HG-ha/Argusai/blob/5f7aa0844ae0341f3563da2a4d171e3fb797d3ac/argusai/core/assistant/session_chat_loop.py), [tool methods](https://github.com/HG-ha/Argusai/blob/5f7aa0844ae0341f3563da2a4d171e3fb797d3ac/argusai/core/assistant/session_tool_methods.py), [child execution](https://github.com/HG-ha/Argusai/blob/5f7aa0844ae0341f3563da2a4d171e3fb797d3ac/argusai/core/assistant/agent_threads.py), [README runtime](https://github.com/HG-ha/Argusai/blob/5f7aa0844ae0341f3563da2a4d171e3fb797d3ac/README.en.md).
- Basis: explicit + structural.
- Confidence: high for model/tool-path existence; provider execution was not replayed here.
- Caveats: A standalone scan engine or GUI table does not own S1 without the configured model session.

## S2 — Coordination

- State: A
- Distinct S1 units: Independently executing persistent Team Room members, each with distinct objective, tool projection, history, inbox and ongoing work; temporary subagents also exist but do not communicate directly.
- Inter-S1 disturbance: Repeated peer status chatter loops, duplicate or out-of-order targeted requests, interruption of busy specialists, concurrent competition for shared member capacity and missed handoff dependencies.
- Attenuating coordination relation: Team member system context requires model discretion to respond only when its role/objective is implicated, to make concrete `@role` handoffs and otherwise call `team_room_pass`. Durable inboxes deduplicate input references, queue while busy and preserve explicit request ordering; capacity waiters resume as slots release.
- Feedback into subsequent S1 behaviour: A specialist reviews actual targeted peer/leader messages after finishing its current work, chooses to pass, answer with new evidence or issue an exact-role request; that message enters peer inboxes and changes their next work/action choice.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The explicit model-facing anti-loop rule and selective peer-response/handoff control mitigate inter-agent chatter/attention oscillation, while delivery sequencing/dedup solves concrete concurrent-message interference. A generic chat log alone would not establish the agent-owned decision.
- Function: Maintain compatible peer coordination without interrupt/reply storms across simultaneous team work.
- Disturbance / variety regulated: Redundant chat cycles, missed role-specific requests, reentrant live work and shared member-slot interference.
- Decisive decision or feedback right: Decide when own role must answer an inter-agent request, pass unproductive chatter, or send a bounded dependency/handoff to another specialist.
- Decision owner: Model-bearing persistent member agents exercising model-facing Team Room rules; deterministic queue/dedup/capacity checks only supply delivery discipline.
- Supporting / enforcement mechanisms: Separate Team Room log/cursors and pending-input queue, selective `@role` message route, `team_room_pass`, input reference dedup and member concurrency limits.
- Closure path: Peer message/redundant chatter or directed dependency → model member evaluates role fit → pass or targeted correction/handoff → queue records/limits the message → affected member consumes it and adjusts work.
- Boundary reachability: Persistent Team Rooms, first-party member prompt and member tools are shipped in the standard GUI/assistant mode; they are not optional third-party skills.
- Why this is / is not agent-owned: The decision whether to escalate/pass/answer is model discretion. Serial/held input alone would not support A, so the positive is restricted to the standing-team model-facing selective coordination path.
- Evidence: [agent role prompt and member queue](https://github.com/HG-ha/Argusai/blob/5f7aa0844ae0341f3563da2a4d171e3fb797d3ac/argusai/core/assistant/agent_threads.py), [Team Room routing and read cursors](https://github.com/HG-ha/Argusai/blob/5f7aa0844ae0341f3563da2a4d171e3fb797d3ac/argusai/gui/teams.py), [architecture/queue contract](https://github.com/HG-ha/Argusai/blob/5f7aa0844ae0341f3563da2a4d171e3fb797d3ac/wiki/Architecture-and-Development.md).
- Basis: explicit + structural.
- Confidence: medium; no empirical measured chat-loop reduction is claimed.
- Caveats: Temporary `spawn_team` has no peer messaging; this S2 A is confined to the separately supported persistent-team mode, not all single-agent sessions.

## S3 — Inside-and-now control

- State: A(P)
- Whole-system current view: Parent assistant can read the complete Todo tree, current task/job progress, team roster, child notices, evidence links and tool outputs; owner GUI sees team state and can edit/steer running membership and assignments.
- Current-control decision scope: Model chooses investigation phases, work assignments, task continuation, relevant members, tool batches and response to child results. Owner separately changes standing-team staffing, objective/role assignments and active scope of current work, with next-turn effect.
- Function: Coordinate immediate work commitments and evidence production for a whole user objective.
- Disturbance / variety regulated: Specialist readiness, task phase dependencies, uncertain evidence and external tool errors, changing user direction, busy child agents.
- Decisive decision or feedback right: Model creates/updates whole-goal Todo plan, delegates and redirects workers; parent owner can edit or pause team members, change scope and direct next assigned work.
- Decision owner: Main configured model for autonomous management; installation owner via Team GUI/member update for the parent mode.
- Supporting / enforcement mechanisms: Todo plan, run locks, live UI, child registry, Team Room and group message stores, confirmation/permission gates.
- Closure path: Whole-goal evidence and child notices → model changes priorities/delegation → different agent/tool actions; owner observes team, edits member/assignments or sends new instruction → persisted metadata and injected typed event change subsequent child operation.
- Boundary reachability: Both assistant model tools (`set_todos`, `spawn_team`, agent input) and owner GUI team/member edit controls are first-party installed entry points; they return into running agent sessions rather than isolated dashboards.
- Why this is / is not agent-owned: Autonomous model retains current resource choices; the user separately holds a legitimate parent current-control role over the same local team. Hard permissions/queues alone do not count as a second owner.
- Evidence: [model planning/delegation methods](https://github.com/HG-ha/Argusai/blob/5f7aa0844ae0341f3563da2a4d171e3fb797d3ac/argusai/core/assistant/session_tool_methods.py), [child control/notifications](https://github.com/HG-ha/Argusai/blob/5f7aa0844ae0341f3563da2a4d171e3fb797d3ac/argusai/core/assistant/agent_threads.py), [owner team/member editing](https://github.com/HG-ha/Argusai/blob/5f7aa0844ae0341f3563da2a4d171e3fb797d3ac/argusai/gui/teams.py).
- Basis: explicit + structural.
- Confidence: medium-high within installed modes; no actual provider-backed orchestration run was executed.
- Caveats: User task interjections are not credited alone; the distinct parent mode is the current-control owner GUI plus persistent member state returned to operation.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Main assistant model | Todo/worker/evidence progress | New delegation/plan/tool choices change live work | [methods](https://github.com/HG-ha/Argusai/blob/5f7aa0844ae0341f3563da2a4d171e3fb797d3ac/argusai/core/assistant/session_tool_methods.py), [agent threads](https://github.com/HG-ha/Argusai/blob/5f7aa0844ae0341f3563da2a4d171e3fb797d3ac/argusai/core/assistant/agent_threads.py) |
| Parent (`P`) | Installation/team owner | Updated current assignments, member scope or pause | Saved member state and typed next-turn update steer live agent | [Team GUI](https://github.com/HG-ha/Argusai/blob/5f7aa0844ae0341f3563da2a4d171e3fb797d3ac/argusai/gui/teams.py), [member update](https://github.com/HG-ha/Argusai/blob/5f7aa0844ae0341f3563da2a4d171e3fb797d3ac/argusai/core/assistant/agent_threads.py) |

## S3* — Complementary audit

- State: ?
- Function: Distinct independent examination of operational claims via complementary raw reality rather than ordinary task reporting; full closure cannot be established confidently from the reviewed default distribution.
- Disturbance / variety regulated: Misleading child report, inaccurate scan/finding, incomplete task claim.
- Decisive decision or feedback right: Independently challenge a worker/result with raw Case/Artifact/Tool evidence and return a corrective finding to control; whether a governed non-producer audit owner routinely exercises it is unresolved.
- Decision owner: Main assistant may inspect material and can instantiate readonly specialists; the built-in reporter role consolidates findings but is not shown to have a mandatory independently sourced veto/repair channel.
- Supporting / enforcement mechanisms: Case/Evidence original references, readonly subagents, result summaries, operator review, tool histories and durable event logs.
- Closure path: Child or domain output → main assistant can reread raw evidence and assign further validation → correction to tasks is possible, but a shipped *independent complementary inspection owner* and repeatable corrective return are not fully proven.
- Why this is / is not agent-owned: Source supports model review as ordinary operations and a purpose-composable review role, yet cannot distinguish a true independent S3* audit from a task-specific secondary analysis in all supported modes.
- Evidence: [evidence/case store](https://github.com/HG-ha/Argusai/blob/5f7aa0844ae0341f3563da2a4d171e3fb797d3ac/argusai/core/workspace/cases.py), [main review path](https://github.com/HG-ha/Argusai/blob/5f7aa0844ae0341f3563da2a4d171e3fb797d3ac/README.en.md), [readonly specialist presets/child roles](https://github.com/HG-ha/Argusai/blob/5f7aa0844ae0341f3563da2a4d171e3fb797d3ac/argusai/core/assistant/agent_threads.py).
- Basis: structural + explicit.
- Confidence: medium for real audit capability, low for verified S3*-specific ownership.
- Caveats: `web_audit` reporter summarizes other roles and the human inspects findings; neither automatically supplies independent unfiltered ground-truth inspection. No presumed external security review is credited.

## S4 — Outside-and-then intelligence

- State: ?
- Function: Adapt future patrol priorities, scheduled investigation or long-lived operational capability from external change; specific closed adaptation ownership remains unresolved.
- Disturbance / variety regulated: Changed attack surface, new file/log events, future alerts and cross-session findings.
- Decisive decision or feedback right: Choose and enact a prospective change to future monitoring/adaptation, distinct from simply completing current steps or running fixed Cron commands.
- Decision owner: A model may call first-party `cron_upsert` and alter future work triggers; an installation owner can also configure schedules. However no clearly evidenced shipped model process compares new environment trends, decides a durable *revised future capability*, and closes that decision back into later operating configuration.
- Supporting / enforcement mechanisms: Cron tasks with interval/cron/webhook/file-change triggers, persisted jobs/run records, long-term session memory and task/Case references.
- Closure path: External event → scheduled session inspects current artifacts and may update Todos/schedule → later trigger executes; the decisive model's prospective adaptation criterion and actual feedback-based reconfiguration are not resolved at this pin.
- Why this is / is not agent-owned: A model-selectable scheduler plus memory offers a credible first-party adaptation candidate, but scheduling fixed repetitions and reusing prior facts alone are not an established S4 owner.
- Evidence: [model-visible `cron_upsert` catalog](https://github.com/HG-ha/Argusai/blob/5f7aa0844ae0341f3563da2a4d171e3fb797d3ac/argusai/core/assistant/skills.py), [persistent scheduler](https://github.com/HG-ha/Argusai/blob/5f7aa0844ae0341f3563da2a4d171e3fb797d3ac/argusai/core/assistant/cron.py), [scheduler GUI routes](https://github.com/HG-ha/Argusai/blob/5f7aa0844ae0341f3563da2a4d171e3fb797d3ac/argusai/gui/assistant_cron.py), [long-term memory](https://github.com/HG-ha/Argusai/blob/5f7aa0844ae0341f3563da2a4d171e3fb797d3ac/argusai/core/assistant/session_memory.py).
- Basis: explicit + structural.
- Confidence: medium for future triggers, insufficient for whether they constitute positive S4 adaptation.
- Caveats: `?` is caused by an identified plausible shipped path, not by a hypothetical future feature; fixed scheduling should not be mistaken for itself owning outside-and-then intelligence.

## S5 — Policy and identity

- State: P
- Identity / ultimate-policy issue: What a persistent local Team is for, which named specialist roles constitute it, and which role objectives/tool-power boundaries bind members across sessions.
- Ultimate authority in each claimed mode: The legitimate self-hosted installation/team owner can create, recharter and edit its standing team and member objectives through first-party GUI/API; no agent-owned constitutional authority to replace that owner's ultimate charter is established here.
- Return-to-operation path: Owner changes standing team purpose or member role/objective/capabilities → persisted team/member record and pending typed metadata update → next member turn receives new role/objective; tool capability projection/confirmation mode enforces limits.
- Function: Maintain binding purpose and role identity of the persistent team as a supported parent-governed arrangement.
- Disturbance / variety regulated: Changed organizational assignment, durable role constitution and owner-level policy over specialist identity and allowed operating repertoire.
- Decisive decision or feedback right: Authoritatively change a team/member's stated continuing purpose, role identity and authorization scope for subsequent work, beyond changing a single tool call.
- Decision owner: Installation owner in the supported human-operated GUI/team setup mode; model tools can request team changes but no distinct self-authorized autonomous ultimate-policy closure is claimed.
- Supporting / enforcement mechanisms: Persisted Team metadata, member records, edited role/objective, capability projection and queued `metadata_update_pending` typed event.
- Closure path: Parent decides a standing team/role-purpose revision → `update_team_member` persists the charter and emits event → member's future context/inbox incorporates it → subsequent agent work follows updated purpose/policy.
- Boundary reachability: Creating and updating persistent teams and members are shipped, first-party GUI/API features, not repository maintainer policy or an external integration. The member worker reads revised metadata on its next safe turn.
- Why this is / is not agent-owned: The credited S5 mode is owner-authored standing team constitution, not the assistant approving its own tools or choosing current task steps; S3-level task steering remains separately recorded.
- Evidence: [persistent team create/update](https://github.com/HG-ha/Argusai/blob/5f7aa0844ae0341f3563da2a4d171e3fb797d3ac/argusai/gui/teams.py), [member metadata revision and next-turn notice](https://github.com/HG-ha/Argusai/blob/5f7aa0844ae0341f3563da2a4d171e3fb797d3ac/argusai/core/assistant/agent_threads.py), [member role/permission API schema](https://github.com/HG-ha/Argusai/blob/5f7aa0844ae0341f3563da2a4d171e3fb797d3ac/argusai/core/assistant/skills.py).
- Basis: explicit + structural.
- Confidence: medium for the local standing team identity loop.
- Caveats: One-off job objectives, approval toggles and permission flags alone are not S5. This claim is limited to the persistent-team *role/purpose* constitution, not governance of unrelated ArgusAI installations or external security organizations.

## Distributed OSS parent arrangement

ArgusAI source development has multiple independent participants, but the reviewed standing team is locally created under one installation owner. Contributor/release actions do not establish a shared across-installation parent. S5 P refers only to the local team charter and member identity return, not the GitHub maintainer's policy over other users.

## Self-hosted and non-human modes

The native configured model can drive normal agent work while the user is absent; an external ACP session is a supported alternative with different cognition and its own tool boundary. Owner GUI management of ongoing team commitments supplies S3 parent mode; durable team mission/role constitution supplies the narrower S5 parent mode. High-risk tool approvals and Cron consent are independent risk gates, not automatic positive VSM ownership.

## Recursion

Temporary subagents and standing Team members possess model/tool loops but receive constrained roles, permissions and task context. The installation-level parent session is assessed as the current manager; a nested assistant is not credited with its own complete S1–S5 recursion merely because it runs a model.

## Variety and escalation

Consecutive read-only tools can batch only with disjoint resource keys; mutating calls, tool confirmation and session locks stay ordered. Team Room queues save explicit member requests and handoffs while busy, deduplicate bounded IDs and permit model-selected silent pass for non-relevant chatter. Goal changes and authorization are escalated to the installation owner. Scheduler host leases prevent duplicate cron leadership but do not decide the long-term strategic objective.

## Evidence gaps

- Exact-ref source inspection and published first-party architecture were used; no live provider-backed test, external ACP authentication, runtime attack exercise or multi-agent high-load demonstration was executed here.
- S3* unresolved path: core supports readonly reviewers and independent access to Case/Artifact originals, but no mandatory independent audit owner/decision/return was traced for a canonical operating mode. A targeted source/E2E replay could settle A/C versus absence.
- S4 unresolved path: model-facing schedule editing and long-term memory are shipped, but a concrete feedback-derived future-capability revision remains unproven. A confirmed model-selected adaptation of actual future patrol policy could upgrade the result; fixed Cron alone cannot.

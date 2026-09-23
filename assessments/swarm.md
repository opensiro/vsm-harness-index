---
harness_id: swarm
project_name: SWARM
repository: https://github.com/KhanUzeb/SWARM
review_ref: 5234bed4e889b13f1343833382a7e13a782a5ee7
reviewed_at: 2026-09-23
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-23
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C(P)
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# SWARM

## Review boundary

- System in focus: one self-hosted SWARM workspace at pinned revision `5234bed4e889b13f1343833382a7e13a782a5ee7`, including the first-party named-bot runtime, channel/group/team triggering, delegation and handoff paths, durable workflow/run engine, work-session/event projection, approval/routine/skill/knowledge services, shared/private computer surfaces and packaged web/CLI control interfaces.
- Purpose and identity: operate named autonomous AI teammates in shared human/agent chat, let them execute tool-backed work, delegate and hand off subtasks, run recurring jobs and durable workflows, and expose current work plus governance actions to the workspace owner.
- Relevant environment: workspace users/admins, configured model providers, host and sandbox filesystems, web/app/tool providers, shared channel history, workflow definitions, external data reached by tools and changing user work objectives.
- Standard-distribution boundary: SWARM-owned FastAPI backend, bot runtime, durable SQLite state, workflow/work-session engines, tool registry, packaged skills/profiles, web UI and CLI. Model/provider internals, connected third-party applications, Browser Use/CUA implementations and host operating-system internals remain environmental systems and do not donate metasystem functions.
- Credited operating / distribution surfaces: `README.md`; `SPEC.md`; `backend/agent.py`; `backend/main.py`; `backend/v2.py`; `backend/work.py`; `backend/evals.py`; `backend/tools/registry.py`; packaged `skills/*.md`; first-party web/CLI surfaces reached by these documented modes.
- Adjacent first-party surfaces excluded from ownership: repository CI/contributor/release machinery, tests as autonomous actors, development-only evaluation comparisons, and implementation guidance in `AGENTS.md` for contributors. Tests corroborate runtime contracts but do not donate organizational decision rights.
- First-party operating / deployment modes considered: shared rooms, bot DMs, group/team chat, bot-to-bot `@handoff`, `delegate_task`, routines, v2 durable workflows/runs, approval-gated work, shared/private computer use, Work/Command Center views and authenticated REST/CLI control.
- Recursion level: one SWARM workspace is the system-in-focus. Named bots performing distinct jobs/tasks in channels, delegation or workflows are installation-level S1 units. A delegated call is a bounded child work unit under its parent task, but named bots co-operating in shared channels/groups remain sibling operating units at the workspace recursion when the first-party runtime invokes them as separate teammates.
- Reviewed revision: `5234bed4e889b13f1343833382a7e13a782a5ee7`.
- Stable GitHub repository ID: `1332989724`.
- Observation date: 2026-09-23.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

SWARM owns an executable agent/team boundary rather than only a chat UI. Named bots are persisted with prompts, jobs, tools, status and model configuration; shared rooms, DMs, groups and `@team` expansion determine which bots are triggered. `backend/agent.py` supplies the model→tool→result loop, persistent memory/knowledge context, approvals and bounded delegation. Tool-backed work can reach the shared sandbox, host filesystem, browser, web search and connected apps. Agent replies are persisted into the same channel history that later teammates consume.

The first-party relay contains a specific multi-bot coordination rule. `_maybe_trigger_agents` resolves the bot batch in mention/roster order and explicitly rejects a per-agent `asyncio.create_task` design because parallel replies would race and violate the guaranteed order. `_run_agents_in_order` awaits each bot before starting the next. Each `_run_agent` then fetches current channel history anew, so a later teammate can observe the already-persisted reply of the preceding teammate. This is an installation-level S2 relation: it attenuates an interaction-generated response race among sibling S1 units and feeds the regulated state into their subsequent behavior.

Current-control state is normalized separately from the chat transcript. `backend/work.py` represents user-visible work from chat replies, v2 runs, routines and handoffs as durable work sessions with queued/running/waiting/terminal state and replayable events. `/api/work` lists those units, `/api/work/{id}` and `/events` expose current detail, and cancel/approval endpoints change whether admitted work continues. The packaged web UI closes a human parent mode; the authenticated APIs expose the same S3-specific state/action path for a downstream autonomous manager, but the standard distribution does not package such a whole-workspace autonomous S3 owner.

The repository also contains review skills, audit/event history and an evaluation helper. These improve evidence and can be composed into verification workflows, but the frozen standard distribution does not require a materially independent reviewer to challenge ordinary S1 completion claims and return findings into bounded corrective rework. Likewise memory, knowledge, reusable skills, routines and `create_agent` can change future behavior, but no separate outside-looking prospective intelligence loop senses external/future distinctions, develops adaptation options and closes an adaptation judgment into present capability.

## Operational model

A human posts work into a room, DM or group, or starts a durable workflow/routine. SWARM selects the relevant named bot(s), builds current channel/memory/knowledge context and invokes each bot's configured model. The model owns task-local reasoning and tool selection; the runtime executes allowed tools, persists tool/audit events, can pause consequential work for human approval and returns observations to the same bot until a final reply is produced.

When several sibling bots are selected from one message, SWARM serializes them deliberately. The first bot completes and persists its reply before the second bot starts; the second bot rebuilds context from the channel, so the enforced ordering changes what it can observe and how it can respond. Separate `delegate_task` calls support hierarchical specialist work and have their own recursion cap, but delegation is not used as the S2 shortcut: the positive S2 finding relies on the explicit shared-channel race witness and first-party anti-race feedback path.

At the workspace recursion, humans retain decisive present-control authority through approvals, cancellation and Command Center/Work views. The same first-party endpoints are intentional construction surfaces for an autonomous current manager, but no resident manager is packaged to decide those interventions across the whole workspace. This supports `S3=C(P)` rather than `A`.

## S1 — Operations

- State: A
- Function: execute admitted user/workflow objectives through named model-driven teammates that reason, call tools, manipulate artifacts and return task outcomes.
- Disturbance / variety regulated: heterogeneous user goals, changing channel/context state, filesystem and browser state, provider/model responses, tool results, connected-app state, approval outcomes and task-specific failures.
- Decisive decision or feedback right: choose the substantive reasoning path, tool calls, delegation choices, artifact edits and task-local responses needed to pursue the admitted objective.
- Decision owner: the autonomous model-driven named bot reached through SWARM's first-party reply/workflow runtime.
- Supporting / enforcement mechanisms: channel trigger selection, context/memory/knowledge assembly, tool registry and caps, shared/private computer providers, provider routing, retry handling, work-event persistence, approvals and delegation-depth limits.
- Closure path: objective/message/run reaches a named bot → the bot chooses reasoning/tools → SWARM executes the selected tool and returns its result → the bot consumes observations and continues → final output/artifacts are persisted into channel/work state and become available to users or later work.
- Boundary reachability: README quick-start and normal chat/workflow paths directly instantiate named bots and invoke the first-party `generate_reply`/tool loop; no CI, contributor or development-only actor is required.
- Why this is / is not agent-owned: runtime code determines which tools are allowed and enforces limits, but substantive task-local choices are produced by the model actor. Removing the model leaves routing/persistence/tool machinery without an actor that decides the work.
- Evidence: [`README.md`](https://github.com/KhanUzeb/SWARM/blob/5234bed4e889b13f1343833382a7e13a782a5ee7/README.md); [`SPEC.md`](https://github.com/KhanUzeb/SWARM/blob/5234bed4e889b13f1343833382a7e13a782a5ee7/SPEC.md); [`backend/agent.py`](https://github.com/KhanUzeb/SWARM/blob/5234bed4e889b13f1343833382a7e13a782a5ee7/backend/agent.py); [`backend/tools/registry.py`](https://github.com/KhanUzeb/SWARM/blob/5234bed4e889b13f1343833382a7e13a782a5ee7/backend/tools/registry.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: model-provider internals are not credited as first-party SWARM machinery; `A` credits the autonomous operational actor made reachable by SWARM's supported runtime relation.

## S2 — Coordination

- State: C
- Function: attenuate response-order interference among sibling named bots that are simultaneously selected to act in one shared/group channel context.
- Disturbance / variety regulated: if separately scheduled sibling bots reply concurrently to the same shared message, their executions race, violating the product's guaranteed mention/roster order and preventing later responders from reliably incorporating earlier teammate output.
- Decisive decision or feedback right: establish the interaction order governing the selected sibling responders so one bot's completed/persisted channel contribution becomes context for the next bot rather than allowing competing responses to race.
- Decision owner: no autonomous S2 coordinator is packaged. The first-party runtime supplies the S2-specific ordering/feedback mechanism deterministically; a downstream specialization would be required to give an autonomous actor discretion over alternative coordination relations.
- Supporting / enforcement mechanisms: mention-position ranking, `@team` roster expansion, group membership ordering, one batch task for the responder set, `_run_agents_in_order`, persisted channel messages and fresh per-bot history retrieval. Delegation-depth and handoff-depth caps additionally suppress recursive cascades but are supporting safeguards rather than the primary witness.
- Closure path: one message selects multiple sibling bots → runtime constructs an ordered responder batch → bot 1 runs and persists its response → bot 2 starts only afterward and retrieves fresh channel history → bot 2's subsequent model behavior can incorporate the regulated prior contribution → the same relation continues through the batch.
- Boundary reachability: this relation is in the standard shared-room/group/team trigger path in `backend/main.py`, reached by ordinary multi-bot operation documented in README/SPEC rather than by tests or a special benchmark mode.
- Why this is / is not agent-owned: the coordination function is real, but fixed runtime sequencing owns enforcement rather than an autonomous agent owning coordination discretion. Methodology `C` records the first-party S2-specific decision/feedback path without turning deterministic enforcement into autonomous ownership.
- Evidence: [`README.md`](https://github.com/KhanUzeb/SWARM/blob/5234bed4e889b13f1343833382a7e13a782a5ee7/README.md); [`SPEC.md`](https://github.com/KhanUzeb/SWARM/blob/5234bed4e889b13f1343833382a7e13a782a5ee7/SPEC.md); [`backend/main.py`](https://github.com/KhanUzeb/SWARM/blob/5234bed4e889b13f1343833382a7e13a782a5ee7/backend/main.py); [`backend/agent.py`](https://github.com/KhanUzeb/SWARM/blob/5234bed4e889b13f1343833382a7e13a782a5ee7/backend/agent.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: `delegate_task` and `@handoff` are not credited merely because they delegate. The positive finding rests on the source-level anti-race contract for sibling responders and the fresh-history feedback path.
- Distinct S1 units: separate named model-driven bots selected as teammates in one room/group/team, each with its own prompt/job/tools/model invocation and separately persisted reply.
- Inter-S1 disturbance: the source explicitly states that per-agent asynchronous tasks would race and violate FR4.2's “in the order mentioned” guarantee when multiple bots answer the same shared input.
- Attenuating coordination relation: SWARM creates one responder-batch task, orders bots by DM/group/team/mention semantics and awaits `_run_agent` sequentially for every selected bot.
- Feedback into subsequent S1 behaviour: every `_run_agent` fetches channel history when it begins; because the preceding bot has already completed and persisted its reply, the next bot receives that regulated shared state in its model context and can change its response accordingly.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the evidence names a concrete interaction-generated race among sibling operating units and a first-party ordering relation designed specifically to prevent that race while feeding the result into later sibling behavior. The classification does not arise from the existence of channels, queues, handoffs or delegation alone.

## S3 — Inside-and-now control

- State: C(P)
- Function: provide a whole-current workspace view over admitted user-visible work and let a controller intervene in present commitments through cancellation and approval/resumption decisions.
- Disturbance / variety regulated: current work can be queued, running, waiting for approval, failed, interrupted or cancelled across chat replies, routines, handoffs and durable workflow runs; consequential actions can require an immediate parent decision before operation continues.
- Decisive decision or feedback right: decide whether present work continues, is cancelled, or passes/does not pass an approval checkpoint, thereby changing current commitments and subsequent execution.
- Decision owner: base constructor mode — no autonomous whole-workspace manager is packaged, but first-party work/run/approval APIs expose the current-control path for one. Parent mode — the authenticated human workspace user/operator using the packaged Work/Command Center and approval controls.
- Supporting / enforcement mechanisms: `work_sessions`, normalized work events, v2 run/event state, `/api/work`, run/work detail/events, `cancel_session`, run cancellation, approval records, `waiting_for_approval`, restart recovery and WebSocket/UI projections.
- Closure path: current work inventory/state is exposed → downstream controller or human identifies a current commitment requiring intervention → first-party cancel or approval action is issued → work/run state is persisted/reconciled → execution stops or resumes and later current state reflects the decision.
- Boundary reachability: the Work APIs, approvals and packaged UI are normal authenticated deployment surfaces; constructor use does not require contributor/CI internals.
- Why this is / is not agent-owned: SWARM exposes the S3 state and intervention right but does not package a resident autonomous agent that decides workspace-wide cancellations/approvals. Runtime recovery/status transitions enforce prior choices. The human path is an operationally closed parent mode.
- Evidence: [`README.md`](https://github.com/KhanUzeb/SWARM/blob/5234bed4e889b13f1343833382a7e13a782a5ee7/README.md); [`SPEC.md`](https://github.com/KhanUzeb/SWARM/blob/5234bed4e889b13f1343833382a7e13a782a5ee7/SPEC.md); [`backend/work.py`](https://github.com/KhanUzeb/SWARM/blob/5234bed4e889b13f1343833382a7e13a782a5ee7/backend/work.py); [`backend/v2.py`](https://github.com/KhanUzeb/SWARM/blob/5234bed4e889b13f1343833382a7e13a782a5ee7/backend/v2.py); [`backend/main.py`](https://github.com/KhanUzeb/SWARM/blob/5234bed4e889b13f1343833382a7e13a782a5ee7/backend/main.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: deterministic workflow topological order, retries/recovery, model routing and tool caps are supporting mechanisms. They are not treated as autonomous S3 decision owners.
- Whole-system current view: `/api/work` normalizes user-visible work from chat-triggered replies, v2 runs, routines and handoffs; each work unit exposes status/objective/source/current step/action requirement, with linked messages/events and run state available for drill-down. Pending approvals are also listable across visible channels.
- Current-control decision scope: cancel a nonterminal work session/run; resolve a bot approval or workflow approval checkpoint so blocked work resumes or is denied/cancelled; these actions directly change present commitments rather than only editing future configuration.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | downstream autonomous workspace manager must be composed | normalized current work/approval state indicates a present intervention | controller reads `/api/work` / run / approval state and invokes first-party cancel or approval endpoints; persisted work/run state then changes subsequent operation | `backend/work.py`; `backend/main.py`; `backend/v2.py` |
| Parent (`P`) | authenticated workspace human/operator | Work/Command Center or channel shows active work requiring cancellation or a pending consequential-action/workflow approval | human chooses cancel / Allow / Deny; SWARM persists the decision and stops or re-triggers/resumes the affected work | `README.md`; `SPEC.md`; `backend/main.py` |

## S3* — Complementary audit

- State: —
- Function: no standard-distribution complementary audit loop is established at the workspace recursion.
- Disturbance / variety regulated: ordinary agents can produce incorrect work, and the repository includes event/audit history, a `/review` skill and evaluation metrics that can record verification events, but none of these establishes a required materially independent audit path over an operational claim with corrective return.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: persisted tool/work/run events, JSON/CSV audit export, `skills/review.md`, evaluation `verification_*` metric recognition, approval gates and reports/artifacts improve inspectability or can be composed into a review process.
- Closure path: not applicable for the negative finding.
- Boundary reachability: the inspected standard operating paths do not automatically route completed worker output to an independent reviewer and return adverse findings into bounded re-execution.
- Why this is / is not agent-owned: `/review` is an ordinary callable skill that can be run by a bot against code/history; `backend/evals.py` scores already-existing event traces. Neither supplies the independence/mandatory challenge/corrective-return structure required for S3*.
- Evidence: [`skills/review.md`](https://github.com/KhanUzeb/SWARM/blob/5234bed4e889b13f1343833382a7e13a782a5ee7/skills/review.md); [`backend/evals.py`](https://github.com/KhanUzeb/SWARM/blob/5234bed4e889b13f1343833382a7e13a782a5ee7/backend/evals.py); [`backend/work.py`](https://github.com/KhanUzeb/SWARM/blob/5234bed4e889b13f1343833382a7e13a782a5ee7/backend/work.py); [`SPEC.md`](https://github.com/KhanUzeb/SWARM/blob/5234bed4e889b13f1343833382a7e13a782a5ee7/SPEC.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: a user can compose a reviewer bot/workflow from general primitives. Methodology does not award `C` from generic composability unless a first-party S3*-specific decision/feedback path is already established.

### Absence scope

- Surfaces inspected: work/run event history and audit export; review skill; evaluation helper and verification-event metrics; workflow graph/approval nodes; bot delegation/handoff; artifacts/reports; channel history and knowledge/memory.
- Plausible first-party paths checked: separate reviewer bot via `/review`; evaluation architecture labelled `multi_agent_memory_verification`; human approval; workflow steps; post-run reports.
- Why no material first-party path remains: the frozen product provides evidence and generic composition primitives, but no standard relation binds an ordinary producer claim to a materially independent reviewer, defines an independence boundary, and feeds a finding back into corrective producer work before acceptance.

## S4 — Outside-and-then intelligence

- State: —
- Function: no distinct workspace-level outside-and-then adaptation loop is established in the reviewed standard distribution.
- Disturbance / variety regulated: agents can search the web, save knowledge/skills, create specialized bots and run routines, but these are operating capabilities used on admitted work rather than a distinct metasystem that senses future/environmental change and adapts the workspace's capabilities from that evidence.
- Decisive decision or feedback right: not established as an S4 adaptation judgment.
- Decision owner: not established.
- Supporting / enforcement mechanisms: web/search/browser tools, knowledge save/search, memory, account-wide skills, `create_agent`, agent templates, routines and provider/model configuration can support future reuse but do not by themselves establish S4.
- Closure path: not applicable for the negative finding.
- Boundary reachability: no first-party standard path was found that turns independently sensed external/future distinctions into adaptation options and returns a selected option into current capability/S3 as an S4 loop.
- Why this is / is not agent-owned: the tool policy may suggest offering a dedicated bot when a user describes a recurring need, but that is a response to a current admitted user request, not a separate prospective environment-sensing function. General web research and persistent knowledge likewise remain S1 capability unless tied to an adaptation closure.
- Evidence: [`backend/agent.py`](https://github.com/KhanUzeb/SWARM/blob/5234bed4e889b13f1343833382a7e13a782a5ee7/backend/agent.py); [`backend/tools/registry.py`](https://github.com/KhanUzeb/SWARM/blob/5234bed4e889b13f1343833382a7e13a782a5ee7/backend/tools/registry.py); [`SPEC.md`](https://github.com/KhanUzeb/SWARM/blob/5234bed4e889b13f1343833382a7e13a782a5ee7/SPEC.md); [`README.md`](https://github.com/KhanUzeb/SWARM/blob/5234bed4e889b13f1343833382a7e13a782a5ee7/README.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: persistent learning artifacts or organizational growth are not automatically S4; the Profile requires the outside/future distinction and adaptation feedback loop to be mapped first.

### Absence scope

- Surfaces inspected: memory/knowledge; skills; create-agent/template path; routines; web/browser/search tools; provider/model configuration; workflow definitions; evaluation helper.
- Plausible first-party paths checked: recurring-need bot provisioning; agent-authored reusable skills/knowledge; web research; provider/model switching; evaluation architecture comparison.
- Why no material first-party path remains: each path is either generic operational capability, human-authored configuration or reuse of current-task learning. No standard component is assigned the distinct job of sensing external/future change, generating capability adaptations from it and closing a selected adaptation back into current operation.

## S5 — Policy and identity

- State: —
- Function: no workspace-level identity / ultimate-policy closure is established.
- Disturbance / variety regulated: admin/member roles, tool allowlists, approval rules, workflow policy, provider credentials, agent prompts/jobs and security boundaries regulate operation but do not resolve a dispute over organizational identity or ultimate policy at this recursion.
- Decisive decision or feedback right: not established at S5 level.
- Decision owner: not established.
- Supporting / enforcement mechanisms: first-admin role, authentication, agent tool lists, human approvals, workflow policy strings, workspace onboarding and security guards constrain execution.
- Closure path: not applicable for the negative finding.
- Boundary reachability: no standard identity/ultimate-policy escalation and authoritative return path was found.
- Why this is / is not agent-owned: a human has final authority over many operational actions, but ordinary approvals, agent configuration and admin permissions do not become S5 solely because the human has final say.
- Evidence: [`SPEC.md`](https://github.com/KhanUzeb/SWARM/blob/5234bed4e889b13f1343833382a7e13a782a5ee7/SPEC.md); [`backend/main.py`](https://github.com/KhanUzeb/SWARM/blob/5234bed4e889b13f1343833382a7e13a782a5ee7/backend/main.py); [`backend/policy.py`](https://github.com/KhanUzeb/SWARM/blob/5234bed4e889b13f1343833382a7e13a782a5ee7/backend/policy.py).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: parent governance is only S5 when the matter is genuinely identity/ultimate-policy-level and the return-to-operation loop is established.

### Absence scope

- Surfaces inspected: workspace admin/member identity, authentication/onboarding, agent prompts/jobs/tool policy, approvals, workflow policy, provider/security configuration and packaged governance endpoints.
- Plausible first-party paths checked: first-admin authority; approval resolution; agent provisioning/archival; role/tool changes; workflow policy and workspace security settings.
- Why no material first-party path remains: these are current operational authority/configuration paths. The frozen distribution does not identify an identity/ultimate-policy issue, a legitimate ultimate authority deciding it as such and a returned decision that governs subsequent operation at the workspace recursion.

## Recursion

A named bot can invoke another bot through `delegate_task`, and workflow graphs can contain multiple agent nodes. Those nested task relations are not automatically separate viable systems. The installation-level vector uses named bots as S1 units only where first-party shared-channel/team operation establishes them as peer operating teammates under the common SWARM workspace boundary.

## Variety and escalation

SWARM amplifies operational variety through configurable models/tools, shared/private computer surfaces, browser/web/apps, skills, memory/knowledge, routines and dynamic bot provisioning. It attenuates variety through tool caps, delegation/handoff depth bounds, ordered multi-bot reply batches, workflow validation, approvals, durable state and restart recovery. Consequential action escalates to human approval, but that operational escalation is classified under the S3 parent mode rather than S5.

## Admission conclusion

Canonical vector: `A C C(P) — — —`.

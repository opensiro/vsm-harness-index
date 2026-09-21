---
harness_id: pibot
project_name: pibot
repository: https://github.com/glebis/pibot
review_ref: 350bf2c8263f31bcda33789c819329bb56f14c00
reviewed_at: 2026-09-22
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
assessment_changed_at: 2026-09-22
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: P
autonomy_s3_star: C
autonomy_s4: A(P)
autonomy_s5: P
---

# pibot

## Review boundary

- System in focus: one locally operated pibot installation at frozen revision `350bf2c8263f31bcda33789c819329bb56f14c00`, including its per-agent runtime directories, pibot-owned scheduler/heartbeat protocol, transports, capability registry, event/consolidation/evolution machinery, inter-agent communication surfaces and authenticated local dashboard.
- Purpose and identity: host persistent personal agent companions that can react to owner conversations, wake proactively, preserve local memory/state, coordinate with sibling agents, schedule future actions and improve reusable skills over time while retaining owner governance over installation-level controls and agent identity.
- Relevant environment: owner messages and identity choices, time/calendar/scheduled commitments, personal memory and event history, sibling-agent work, local files/runtime state, external model providers permitted by each manifest, Telegram/CLI transports and task-specific external data exposed through opt-in capabilities.
- Standard-distribution boundary: pibot's `src/` host/runtime, shipped plugins/transports, per-agent manifests/persona/memory/skills/sessions, dashboard and scheduler. `@earendil-works/pi-coding-agent` supplies the lower-level model/session/tool runtime and is treated as an external implementation dependency; its generic agent-loop semantics are not inherited as pibot VSM evidence by themselves.
- Credited operating / distribution surfaces: `src/core/heartbeat.ts`; `src/core/bot.ts`; `src/core/agent-manager.ts`; `src/core/evolution.ts`; `src/core/consolidation.ts`; `src/core/backlog.ts`; `src/core/types.ts`; `src/plugins/agent-comms-plugin.ts`; `src/web.ts`; `src/core/agent-factory.ts`; runtime wiring in `src/index.ts`.
- Adjacent first-party surfaces excluded from ownership: repository-development `.agents`, `.claude`, `.codex` and `.beads` surfaces; GitHub CI; tests; the optional `pibot-dev` repository-development agent except where noted as an adjacent mode; README comparisons/provenance to Ouroboros/Hermes where code is not itself wired into pibot; external herdr/Claude/Codex/Gemini subprocess internals.
- First-party operating / deployment modes considered: default companion with heartbeat enabled; owner chat through CLI/Telegram; multi-agent messaging/handoff where sibling agents exist; opt-in evolution-enabled agent; dashboard/operator mode; manually reviewed staged-skill mode; optional consolidation path where materially used by evolution/heartbeat.
- Recursion level: one pibot installation containing one or more personal companion agents. Individual companions are outcome-bearing S1 units where they independently interact with local owner/environment state; this assessment does not assume every companion is separately a complete viable recursion.
- Reviewed revision: `350bf2c8263f31bcda33789c819329bb56f14c00`.
- Observation date: 2026-09-22.
- Generated Profile version: `0.2.3`.
- Generated Methodology version: `0.3.5`.
- Current Profile version: `0.2.3`.
- Current Methodology version: `0.3.5`.

## Repository architecture

pibot wraps Pi SDK sessions inside a first-party personal-agent host. `AgentManager` discovers/scaffolds private runtime directories, binds each agent's persona, manifest, capability set, private extensions, evolved skills and persistent per-chat session file, then calls Pi's `createAgentSession`. The Pi dependency owns the generic lower-level model/tool session engine; pibot owns the agent boundary, persistence, capabilities, scheduling, delivery, cross-agent routing and higher-order protocols assessed below.

A default agent has heartbeat enabled. `HeartbeatEngine` is a pibot-specific autonomous operating protocol: a timer guard checks snooze, quiet hours, recent owner activity and unanswered-proactivity backoff; pibot builds a digest from persona, durable memory, schedules and recent events; an ephemeral model must call the pibot-defined `heartbeat_act` tool exactly once; the returned decision can speak to the owner, escalate into the full companion session, record maintenance/backlog information and choose a bounded next-wakeup delay. `tickInner` applies those decisions through pibot's host/scheduler/event machinery. This provides a material pibot-owned S1 path without attributing Pi's generic session loop to pibot.

The installation also exposes owner current-control surfaces. The authenticated local dashboard lists/manages agents and exposes manifest/rhythm/model/capability controls, schedule state with snooze/wake/cancel operations, event tails, evolution state and other runtime controls. Agent persona creation/editing is a separate identity path. The chat `/newagent` flow asks the owner to choose the agent's job, vibe and proactivity; an ambiguity gate can ask additional identity clarifications; pibot writes the resulting `AGENTS.md` and manifest, which are then loaded into later sessions. Direct dashboard persona edits write the same first-party identity surface.

For adaptation, `EvolutionEngine` implements a closed first-party loop. It collects recent events, heartbeat/consolidated state, existing skills and improvement backlog; an ephemeral model proposes a create/patch option with rationale and eval probes; deterministic guards stage the candidate; probe sessions execute with the candidate loaded and a separate LLM judge scores their outputs. Safe candidates averaging at least four are automatically promoted into the live `skills/<name>/SKILL.md` path, backlog items are closed, an event is recorded and the owner is notified. `AgentManager` loads those live skills into subsequent sessions. Risky or weak candidates remain staged and can instead be promoted/rejected through first-party owner review surfaces, giving the same S4 function a distinct parent-governed mode.

## Operational model

The clearest pibot-owned operational unit is each companion's heartbeat process. Although its ephemeral model executes on Pi's session substrate, pibot defines the information boundary, decision vocabulary, runtime guards and closure into owner delivery/escalation/adaptive cadence. The autonomous decision is therefore not borrowed from a generic SDK feature: removing pibot's heartbeat protocol leaves no equivalent proactive companion decision path.

Sibling agents can message, ask and hand off work, but these communication/delegation paths do not establish S2 by topology. No reviewed source ties them to a concrete inter-S1 collision/oscillation and a disturbance-specific mutual-adjustment loop.

Installation-wide current control remains parent-governed. The dashboard/operator owns the decisive choices over which agents exist, their models/capabilities/rhythms and current schedules/snooze state. The host enforces those choices. No autonomous supervisor with equivalent whole-installation current-control discretion is established.

## Primary evidence

- [`src/core/heartbeat.ts`](https://github.com/glebis/pibot/blob/350bf2c8263f31bcda33789c819329bb56f14c00/src/core/heartbeat.ts) — first-party heartbeat decision protocol, guards, adaptive wakeup, maintenance verification and speak/escalate closure.
- [`src/core/agent-manager.ts`](https://github.com/glebis/pibot/blob/350bf2c8263f31bcda33789c819329bb56f14c00/src/core/agent-manager.ts) — private runtime/session assembly, capability binding, live skill loading and explicit Pi SDK boundary.
- [`src/core/types.ts`](https://github.com/glebis/pibot/blob/350bf2c8263f31bcda33789c819329bb56f14c00/src/core/types.ts) — default heartbeat-enabled manifest plus evolution/consolidation/operator-configurable modes.
- [`src/core/evolution.ts`](https://github.com/glebis/pibot/blob/350bf2c8263f31bcda33789c819329bb56f14c00/src/core/evolution.ts) — propose → guard → stage → probes/judge → auto-promote or parent review, plus backlog closure.
- [`src/index.ts`](https://github.com/glebis/pibot/blob/350bf2c8263f31bcda33789c819329bb56f14c00/src/index.ts) — runtime construction of scheduler, heartbeat, consolidation and evolution engines and host wiring.
- [`src/core/bot.ts`](https://github.com/glebis/pibot/blob/350bf2c8263f31bcda33789c819329bb56f14c00/src/core/bot.ts) — startup scheduling, owner/session routing, delivery closure, agent-creation ambiguity flow and evolution enablement.
- [`src/plugins/agent-comms-plugin.ts`](https://github.com/glebis/pibot/blob/350bf2c8263f31bcda33789c819329bb56f14c00/src/plugins/agent-comms-plugin.ts) — sibling messaging, blocking ask and handoff surfaces inspected for S2.
- [`src/web.ts`](https://github.com/glebis/pibot/blob/350bf2c8263f31bcda33789c819329bb56f14c00/src/web.ts) — authenticated operator dashboard, schedule/current-control surfaces, persona editor and staged-evolution review.
- [`src/core/agent-factory.ts`](https://github.com/glebis/pibot/blob/350bf2c8263f31bcda33789c819329bb56f14c00/src/core/agent-factory.ts) — owner-selected job/vibe/proactivity translated into persona and runtime manifest.
- [`README.md`](https://github.com/glebis/pibot/blob/350bf2c8263f31bcda33789c819329bb56f14c00/README.md) — supported operating modes and user-facing workflow, used to corroborate rather than replace code evidence.

## S1 — Operations

- State: A
- Function: proactively monitor personal-agent state and produce an owner-facing intervention, escalation or maintenance action without requiring a new user message.
- Disturbance / variety regulated: due/near-due schedules, recent events, stale memory/persona/consolidation state, owner inactivity, unresolved activity worth surfacing, quiet-hour/snooze constraints and uncertainty about whether an interruption is worthwhile.
- Decisive decision or feedback right: decide on each eligible heartbeat whether to stay silent, speak to the owner, escalate into the full companion brain, record a maintenance/backlog action and/or change the next wakeup interval.
- Decision owner: the ephemeral model actor running inside the pibot-defined heartbeat protocol.
- Supporting / enforcement mechanisms: scheduler timer, `shouldTick` guards, bounded digest, `heartbeat_act` schema, wakeup clamps, event log, unanswered-speak backoff, transport delivery and Pi's generic session execution substrate.
- Closure path: pibot timer/guard → pibot digest → model `heartbeat_act` decision → `tickInner` applies speak/escalate/maintenance/wakeup → owner or full companion receives the action and/or next scheduler cadence changes → later heartbeat observes updated events/state.
- Boundary reachability: heartbeat is enabled by `defaultManifest`, `PiBot.start()` installs a heartbeat job for discovered agents, and `src/index.ts` wires HeartbeatEngine directly to pibot delivery/escalation/scheduler/event services.
- Why this is / is not agent-owned: the timer and clamps decide whether a tick may run, but once a tick runs the model has bounded discretion over whether and how to intervene. Pi executes the ephemeral model session but does not supply pibot's heartbeat purpose, digest, decision vocabulary or return path.
- Evidence: `src/core/heartbeat.ts`, `src/core/types.ts`, `src/core/bot.ts`, `src/index.ts`.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: ordinary reactive chat also uses Pi sessions, so it is not used by itself to import a generic Pi S1 claim into pibot. The positive mapping rests on the first-party heartbeat organization.

## S2 — Coordination

- State: —
- Function: no material first-party S2-specific coordination path is established among pibot companion S1 units.
- Disturbance / variety regulated: the review looked for actual or structurally evidenced sibling-agent interference, contention or oscillation rather than treating messaging/handoff as coordination by name.
- Decisive decision or feedback right: no first-party path was established that detects a concrete inter-S1 disturbance, chooses an attenuating coordination response and feeds that result into later sibling behavior.
- Decision owner: none established for qualifying S2.
- Supporting / enforcement mechanisms: `agent_message`, `agent_ask`, handoff briefs, chat rebinding, scheduler ordering and per-agent runtime/session separation.
- Closure path: sibling communication/delegation can alter task flow, but no disturbance-specific inter-S1 conflict → coordination judgment → changed subsequent S1 behavior loop was established.
- Why this is / is not agent-owned: a companion can choose to message or hand off to another companion, but delegation/communication alone is not S2 and the source does not identify a shared collision being regulated by that path.
- Evidence: `src/plugins/agent-comms-plugin.ts`, handoff/session routing in `src/core/bot.ts`, runtime separation in `src/core/agent-manager.ts`.
- Basis: structural.
- Confidence: high.
- Caveats: pibot clearly supports multiple durable agent units; the negative classification concerns the stricter S2 witness, not the absence of multi-agent interaction.

### Absence scope

- Surfaces inspected: sibling messaging/ask/handoff plugin, chat/session ownership and rebinding, scheduler, capability/runtime separation and README multi-agent workflows.
- Plausible first-party paths checked: inter-agent messages, blocking questions, context handoff, transport/chat rebinding, schedule ordering and private per-agent runtime directories.
- Why no material first-party path remains: reviewed paths transport/delegate/isolate work but do not establish a concrete inter-S1 interference/oscillation together with a first-party attenuation decision and feedback loop.

## S3 — Inside-and-now control

- State: P
- Function: regulate the current pibot installation on behalf of the whole by controlling active companion population/configuration, models/capabilities/rhythms and current scheduled commitments.
- Disturbance / variety regulated: agents needing to be created/removed/reconfigured, model/capability/rhythm changes, excessive or unwanted proactive activity, schedule commitments requiring cancel/snooze/wake intervention and operational state visible through event/schedule surfaces.
- Decisive decision or feedback right: decide which companions exist, what runtime capabilities/models/rhythms constrain them and which current schedules remain active, paused/snoozed or cancelled.
- Decision owner: the authenticated local owner/operator in the first-party dashboard/chat control mode.
- Supporting / enforcement mechanisms: dashboard forms, manifest persistence, `AgentManager.discover`, Scheduler state/timer wheel, PiBot startup/rearm logic, authentication/CSRF controls and event/schedule presentation.
- Closure path: installation/schedule/agent state → owner inspects dashboard/control surface → owner edits manifest/rhythm/capability or acts on schedule/agent state → first-party files/scheduler state update → pibot discovery/runtime/scheduler applies changed constraints to subsequent operation.
- Boundary reachability: the authenticated dashboard is started by default unless explicitly disabled, is wired to the live `AgentManager`, `Scheduler`, `EventLog` and `EvolutionEngine`, and README documents the same agent/schedule/runtime controls as supported user-facing operation.
- Why this is / is not agent-owned: pibot's host enforces saved manifests and schedule state, but no autonomous supervisor chooses the installation-wide current-control decision. The legitimate owner does, so the only positive published mode is parent-governed.
- Evidence: `src/web.ts`, `src/core/bot.ts`, `src/core/agent-manager.ts`, `src/core/scheduler.ts`, `README.md`.
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: operational model responses, handoffs and heartbeat choices remain local S1 decisions. They are not used as S3 evidence.
- Whole-system current view: the first-party dashboard exposes the installation's agents and per-agent manifest/rhythm, schedules, event tail and evolution state, providing the operator a cross-installation route to current operational state.
- Current-control decision scope: agent participation, model/capability/rhythm constraints, current schedule activation/cancellation/snooze/wake and related intervention over live installation commitments.

## S3* — Complementary audit

- State: C
- Function: provide a narrow first-party complementary check of a companion's claim that it actually updated durable `memory/MEMORY.md` during heartbeat maintenance.
- Disturbance / variety regulated: a heartbeat can report a maintenance action such as "updated/refreshed MEMORY.md" even when no corresponding filesystem write occurred; relying only on the agent's maintenance note would preserve a false operational claim.
- Decisive decision or feedback right: determine independently whether the claimed write is corroborated by raw filesystem modification time, record a verified/unverified audit result and expose that result to later heartbeat state.
- Decision owner: the shipped audit primitive is deterministic (`verifyMemoryClaim`); no autonomous audit actor owns the verification judgment, so the function is published as `C` rather than `A`.
- Supporting / enforcement mechanisms: maintenance journal, filesystem `stat`, claim-pattern matcher, event logging and maintenance-panel rendering.
- Closure path: heartbeat maintenance claim → deterministic raw-filesystem verification → verification record appended to maintenance journal → later maintenance panel surfaces `verified` or `UNVERIFIED` → subsequent heartbeat model can see the discrepancy and change maintenance behavior.
- Boundary reachability: `recordMaintenanceNote` invokes `verifyMemoryClaim` for qualifying heartbeat maintenance claims in the shipped heartbeat path, and `buildMaintenancePanel` reads the resulting verification record into subsequent standard heartbeat digests.
- Why this is / is not agent-owned: the independent evidence channel is real and closed, but the audit judgment itself is made by deterministic host code rather than an autonomous auditor. The first-party path is function-specific and usable by the subsequent agent, satisfying the constructor publication boundary.
- Evidence: `src/core/heartbeat.ts`.
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: this is intentionally a narrow S3* path; it does not imply a general independent audit of all companion outputs or external actions.
- Claim being audited: the heartbeat's durable maintenance assertion that `MEMORY.md` was just seeded/refreshed/updated/written.
- Ordinary reporting path: the model-provided `maintain` text recorded in the maintenance journal/event log.
- Complementary access path: direct filesystem modification-time inspection of `memory/MEMORY.md`, independent of the model's textual claim.
- Independence boundary: the verifier reads host filesystem metadata and does not accept the model's maintenance note as proof; missing/stale files generate an explicit unverified result.
- Who acts on findings: the next heartbeat model receives the verification status in its maintenance panel; pibot supplies this feedback path, while autonomous corrective judgment remains to the receiving companion.

## S4 — Outside-and-then intelligence

- State: A(P)
- Function: learn from recent operational/environmental history, identify a recurring capability gap, generate and test a reusable skill adaptation and return successful adaptations into future companion capability.
- Disturbance / variety regulated: recurring user/task irritations, unresolved improvement-backlog items, recent events and consolidated lessons showing that the current skill repertoire is inadequate or inefficient for future similar work.
- Decisive decision or feedback right: choose what skill to create/patch, propose the adaptation and probes, judge probe outcomes, and in autonomous mode accept a safe sufficiently successful candidate for promotion into live future capability; in parent mode the owner decides staged-candidate promotion/rejection.
- Decision owner: autonomous mode is a distributed model arrangement — proposal and probe/judge model actors supply the adaptation and evaluation judgments, while deterministic gates/thresholds enforce safety and promotion policy. Parent mode is the authenticated owner reviewing staged candidates.
- Supporting / enforcement mechanisms: event/consolidation input, improvement backlog, deterministic content/risky-pattern/stagnation guards, staging directory, probe runner, average-score threshold, live skill directory, git checkpoint, event log and announcement.
- Closure path: user/environmental operating history → consolidated/backlog distinctions → model proposes future skill change → probes execute with candidate loaded → model judge scores → safe score ≥4 auto-promotes to live `skills/` → `AgentManager` includes live skills in subsequent sessions → future operation changes. Parent mode replaces the automatic acceptance decision with owner promote/reject over a staged candidate.
- Boundary reachability: `EvolutionEngine` and its LLM-backed IO are constructed in `src/index.ts`; `PiBot.start()` schedules evolution for manifests with `evolution.enabled`; the engine writes promoted skills into the same per-agent live skill tree that `AgentManager` loads into standard sessions. Dashboard/chat review surfaces expose staged candidates to the owner.
- Why this is / is not agent-owned: deterministic gates decide only whether a proposal satisfies fixed structural/risk/score constraints. The content of the adaptation and its probe-based model evaluation are agentic; when they pass, the first-party runtime closes activation without a human. Separately, staged review gives the legitimate owner a parent-governed acceptance mode.
- Evidence: `src/core/evolution.ts`, `src/core/agent-manager.ts`, `src/core/backlog.ts`, `src/core/consolidation.ts`, `src/core/bot.ts`, `src/index.ts`, `src/web.ts`, `README.md`.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: evolution is opt-in per agent rather than enabled in `defaultManifest`; it is nevertheless a complete first-party supported operating mode. Generic memory consolidation alone is not credited as S4.
- External distinction: repeated owner/task/environment outcomes recorded as events, maintenance backlog items and consolidated operational lessons reveal capability gaps.
- Future / prospective distinction: whether a new or patched reusable skill would improve later tasks beyond the current run.
- Adaptation option generated: a concrete staged `SKILL.md` create/patch proposal with rationale and task-specific eval probes.
- Path back into current capability / S3: successful promotion writes the candidate into the live per-agent `skills/<name>/SKILL.md` tree; subsequent standard sessions load those live skills through `AgentManager`.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | proposal + probe/judge model actors | scheduled/manual evolution cycle sees recent history, consolidated lessons or top improvement-backlog item | safe candidate with avg probe score ≥4 is auto-promoted into live skills and loaded by later sessions | `src/core/evolution.ts`, `src/core/agent-manager.ts`, `src/core/bot.ts` |
| Parent (`P`) | authenticated owner/operator | candidate remains staged for review or owner invokes staged review | owner promotes/rejects; promotion writes live skill and later sessions load it | `src/core/evolution.ts`, `src/web.ts`, `README.md` |

## S5 — Policy and identity

- State: P
- Function: establish and revise a companion's durable identity/purpose at the parent recursion and return that decision into subsequent pibot operation.
- Disturbance / variety regulated: an under-specified or changing companion role, tone and proactive stance requiring legitimate owner choice about what the companion is for and how it should present/act as that identity.
- Decisive decision or feedback right: decide the companion's job/purpose, vibe/persona and proactivity identity settings, including answering ambiguity-gate clarification questions when the draft identity is too vague.
- Decision owner: the human owner/operator using the first-party creation wizard or authenticated persona editor.
- Supporting / enforcement mechanisms: `scorePersonaAmbiguity`, `QuestionBus`, `buildPersona`, `buildManifest`, `createAgent`, `AGENTS.md`/`agent.json` persistence and `DefaultResourceLoader` context loading for subsequent sessions.
- Closure path: new/ambiguous identity specification → pibot asks the owner for job/vibe/proactivity and, when needed, clarifications → owner answers/edits → pibot writes durable `AGENTS.md` + manifest → later companion sessions load that persona/runtime identity → subsequent operation follows the returned identity decision.
- Boundary reachability: both the chat `/newagent` wizard and authenticated dashboard are shipped operator surfaces; `AgentManager` creates/discovers those runtime directories and loads the persisted persona into standard agent sessions.
- Why this is / is not agent-owned: pibot can score identity ambiguity and build the resulting files, but the legitimate owner supplies the authoritative identity choices. No first-party autonomous actor is evidenced as holding ultimate authority to redefine the companion's purpose.
- Evidence: identity wizard in `src/core/bot.ts`, `src/core/agent-factory.ts`, persona form/update in `src/web.ts`, session loading in `src/core/agent-manager.ts`.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: ordinary capability permissions, schedule approvals and task questions are not used as S5 evidence. The mapping is specifically the durable companion identity path.
- Identity / ultimate-policy issue: what a companion is for, its enduring persona/tone and whether it should be proactively active or reactive-only.
- Ultimate authority in each claimed mode: parent owner/operator only.
- Return-to-operation path: owner identity choice → persisted `AGENTS.md`/manifest → `AgentManager` resource/session loading → later companion reasoning/heartbeat operates under that identity.

## Distributed OSS parent arrangement

Repository maintainer/contributor governance is outside the assessed local pibot installation. `P` states refer to the actual local owner/operator reached through first-party chat/dashboard surfaces, not to GitHub maintainers or contributors.

## Self-hosted and non-human modes

pibot is self-hosted and deliberately retains strong local parent controls. `S3=P` and `S5=P` describe those operator-governed arrangements rather than a maturity deficit. `S4=A(P)` records two distinct supported configurations for adaptation: automatic safe promotion and explicit parent review of staged candidates.

## Recursion

Each companion has its own manifest, persona, memory, sessions, skills, event stream and heartbeat, so companion-level operational identity is durable. This assessment maps the higher pibot-installation recursion where those companions are operational units under shared host/scheduler/operator infrastructure. It does not infer a complete lower-recursion VSM for every companion merely from directory separation.

## Variety and escalation

pibot attenuates operational variety through per-agent capability/provider allowlists, private runtime directories, quiet hours, snooze, backoff and bounded heartbeat decisions. Adaptive wakeups let a companion vary sensing cadence within hard owner/runtime bounds. Heartbeat `escalate` moves a signal from the cheap proactive process into the full companion brain. Cross-agent messaging/handoff expands operational repertoire without being counted as S2 absent a conflict witness. Evolution converts repeated environmental/operational gaps into future skills, while risky or weak candidates escalate to staged parent review. Owner dashboard controls provide installation-wide current regulation; persona creation/editing reserves identity closure to the parent.

## Evidence gaps

The most classification-sensitive finding is `S3*=C`. The ghost-write verifier is a genuine complementary raw-filesystem path with returned findings, but its audit judgment is deterministic rather than agent-owned and is narrow to maintenance claims; stronger general-audit claims are not made. `S3=P` is similarly limited to the operator's installation-wide current-control mode and is not inferred from the existence of a scheduler alone. `S4=A(P)` relies on the complete opt-in evolution mode, not on memory/consolidation terminology.
---
harness_id: starnet
project_name: StarNet
repository: https://github.com/androoAGI/starnet
review_ref: 519a36d9927723c3e66cfb6742905e34c1197ca3
reviewed_at: 2026-09-28
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
last_checked_ref: 519a36d9927723c3e66cfb6742905e34c1197ca3
last_checked_at: 2026-09-28
assessment_changed_at: 2026-09-23
last_reassessment_round: R3
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C(P)
autonomy_s3_star: A
autonomy_s4: C(P)
autonomy_s5: —
---

# StarNet

## Review boundary

- System in focus: one first-party StarNet station at pinned revision `519a36d9927723c3e66cfb6742905e34c1197ca3`, including the Node sidecar agent runtime, station/roster/workstream state, bounded agent runs, group-session coordinator, capability/consent/budget gates, persistent task/memory/schedule state, Night Shift/autopilot paths, adaptive recommendation/recruitment, and the shipped orchestrator/station-control surfaces.
- Purpose and identity: operate a local-first multi-agent station in which autonomous agents perform real model/tool work under station-owned capabilities, permissions, budgets and persistent organization, while the Commander shapes the roster, workflows, workspaces, capabilities and operating posture.
- Relevant environment: the Commander/operator; repositories and local workspaces; model providers; MCP/external tools; user activity and interests; external web/data reached through granted tools; the specialty catalog; OS/process/runtime conditions.
- Standard-distribution boundary: StarNet-owned frontend, Node sidecar, shared event contract, runtime loop, group coordinator, persistent stores, capability/permission/budget layers, orchestrator tools and supported desktop/browser product flows. External model providers and MCP servers do not donate organizational functions.
- Credited operating / distribution surfaces: `README.md`; `CODE_MAP.md`; `docs/BRAIN.md`; `docs/HARNESS_ARCHITECTURE.md`; `docs/ORCHESTRATOR_CONTROL_PLAN.md`; `sidecar/loop.js`; `sidecar/group-sessions.js`; `sidecar/tools/builtin/orchestration.js`; `sidecar/tools/builtin/station.js`; `frontend/app/stationcommands.js`; `frontend/app/recruiter.js`; `frontend/app/recruiterstore.js`; standard station/COMMS/Recruitment Bay flows.
- Adjacent first-party surfaces excluded from ownership: repository-development `loops/`; `qa/` release-readiness and audit actors; CI/release machinery; contributor handoff/worktree processes; evaluation fixtures and benchmarks; tests/examples except as corroboration of shipped paths; historical design proposals not wired into the pinned standard distribution.
- First-party operating / deployment modes considered: ordinary direct agent run; multiple bounded agent runs; group chat with peer handoff/shared artifacts; lead/orchestrator use of standard team/session/task/configuration tools; Commander-driven station control; Full Access and approval-gated interactive operation; unattended Night Shift/autopilot within configured limits; adaptive recommendation/recruitment; scheduled/recurring work.
- Recursion level: the whole StarNet station is the system-in-focus. Individual autonomous agent runs/group participants are installation-level S1 units. Internal model turns/tool calls are below this recursion. Repository-development agents and feature worktrees are outside it.
- Reviewed revision: `519a36d9927723c3e66cfb6742905e34c1197ca3`.
- Observation date: 2026-09-28.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

StarNet's first-party sidecar owns the executable harness boundary. `runAgentLoop()` is the model→tool→result loop; providers are transport adapters, while StarNet resolves capabilities, approvals, budgets, persistence and dispatch before actions execute. The normal station can host multiple genuinely distinct bounded agent runs with separate workspace/permission state, while the visual station and COMMS surfaces project runtime truth rather than inventing parallel product state.

The pinned revision materially expands orchestrator control relative to the previously accepted boundary. A lead can dispatch and summon workers, create/read/focus sessions, create/manage durable task-board cards, read another crew member's Dossier and, with a separately consented `team.configure`, edit that crew member's `identity`, `purpose`, `manual` or `context` for later runs. The authoritative frontend bridge also exposes a truthful `station.status` snapshot and durable station mutations with write/read-back checks. However, the model-facing `sidecar/tools/builtin/station.js` registration at this revision exposes session/task/configuration tools but does not register `station.status`; several mutation descriptions explicitly scope use to Commander-requested actions. The new surfaces therefore strengthen a first-party current-control constructor without establishing an autonomous whole-station regulator by themselves.

The multi-agent group coordinator remains organizationally material. Group participants are selected from the live roster; each turn is attributed to one participant; agents may explicitly hand off to another participant, publish an immutable exact file version and let peers read that version without granting filesystem access. The coordinator bounds pending work and prevents a repeated unchanged handoff oscillation by holding a repeated request at the same checkpoint.

StarNet also distinguishes present control from future adaptation. Learned work/topic evidence is compared with the live roster; uncovered warm capability demand yields a concrete specialist option. The revision now also exposes `team.summon` to the lead, but the adaptive recruiter remains a deterministic frontend recommendation surface rather than a model-facing autonomous adaptation input. The Commander remains the demonstrated owner of the standard recruitment/adoption mode.

## Operational model

The station's operational units are autonomous agent runs that receive objectives and admitted capabilities, reason over model/tool feedback and produce task results/artifacts. A lead can delegate to separately bounded worker runs and route work into named sessions. Runtime mechanisms constrain and persist those decisions but do not replace the agents' local operational discretion.

At the station recursion, current-control and adaptation rights remain multi-mode. StarNet ships increasingly rich constructor seams usable by an autonomous controller, while the Commander has an explicit first-party parent mode over station organization. Constructor availability is not treated as agent ownership: a positive `A` requires evidence that a shipped autonomous actor receives the function-specific signal, makes the decisive organizational choice and closes it into later station behavior.

## S1 — Operations

- State: A
- Function: perform user-directed and explicitly permitted unattended work through autonomous StarNet agent runs using real model calls and granted tools.
- Disturbance / variety regulated: open-ended user objectives, workspace/repository state, tool results, provider responses, permissions, budget limits, task uncertainty, schedules and external information reached through granted capabilities.
- Decisive decision or feedback right: choose substantive task reasoning, model/tool actions, whether further tool work is needed and how to respond to returned tool/environment feedback within the admitted objective and host constraints.
- Decision owner: the autonomous model/agent executing inside StarNet's first-party `runAgentLoop()` path.
- Supporting / enforcement mechanisms: capability resolution, consent broker, budget engine, context management, run queue, provider adapters, persistent stores, Task Brief gates, Night Shift scheduling and event/telemetry contracts.
- Closure path: user/schedule/unattended trigger admits work → StarNet builds the permitted context/tools → autonomous agent selects model/tool actions → StarNet executes and returns environment/tool feedback → agent continues until completion or bounded stop → resulting artifacts/state are persisted and surfaced.
- Boundary reachability: `sidecar/loop.js` is the standard sidecar agent loop described by the repository's runtime documentation and is reached by ordinary station runs rather than a development-only example.
- Why this is / is not agent-owned: host code enforces permissions, budgets and lifecycle, but task-local reasoning and useful-action discretion remain with the autonomous agent. Removing the model actor leaves support/enforcement machinery without the substantive operational decision loop.
- Evidence: [`README.md`](https://github.com/androoAGI/starnet/blob/519a36d9927723c3e66cfb6742905e34c1197ca3/README.md); [`CODE_MAP.md`](https://github.com/androoAGI/starnet/blob/519a36d9927723c3e66cfb6742905e34c1197ca3/CODE_MAP.md); [`sidecar/loop.js`](https://github.com/androoAGI/starnet/blob/519a36d9927723c3e66cfb6742905e34c1197ca3/sidecar/loop.js); [`docs/HARNESS_ARCHITECTURE.md`](https://github.com/androoAGI/starnet/blob/519a36d9927723c3e66cfb6742905e34c1197ca3/docs/HARNESS_ARCHITECTURE.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: model-provider internals are not credited as StarNet functions; `A` is based on the autonomous actor reached and governed by the shipped StarNet execution path.

## S2 — Coordination

- State: C
- Function: attenuate interaction-generated handoff oscillation and uncontrolled peer-work continuation among sibling agent runs in a group while preserving explicit peer requests and bounded continuation.
- Disturbance / variety regulated: a participant can repeatedly hand the same request back toward a peer without a changed artifact/question checkpoint, producing an A↔B request loop or duplicated sibling work.
- Decisive decision or feedback right: determine whether another peer turn may be admitted for the same origin/request/checkpoint or must be held for review/explicit continuation.
- Decision owner: no autonomous owner is established for the decisive anti-oscillation judgment. The first-party coordinator applies the S2-specific repeated-request hold deterministically.
- Supporting / enforcement mechanisms: durable group turn queue, origin/parent attribution, artifact/question checkpointing, bounded pending work, retry allowance, Stop/restart semantics and participant membership.
- Closure path: sibling participant requests peer work → coordinator records origin/request/checkpoint → repeated completed same-agent/same-request turns at an unchanged checkpoint are detected → next turn becomes `held` with `Repeated request; review before continuing` → targeted sibling execution does not proceed until explicit continuation/correction changes the path.
- Boundary reachability: `sidecar/group-sessions.js` is the standard first-party group runtime; the coordination handoff document describes the same pause/continuation semantics in the shipped coordinator.
- Why this is / is not agent-owned: autonomous peers own task-local handoff requests, but the decisive attenuation of the repeated-loop disturbance is deterministic coordinator logic. The function-specific path is first-party and reachable, while autonomous ownership still requires composition.
- Evidence: [`sidecar/group-sessions.js`](https://github.com/androoAGI/starnet/blob/519a36d9927723c3e66cfb6742905e34c1197ca3/sidecar/group-sessions.js); [`docs/HANDOFF_GROUP_COORDINATION_2026-09-05.md`](https://github.com/androoAGI/starnet/blob/519a36d9927723c3e66cfb6742905e34c1197ca3/docs/HANDOFF_GROUP_COORDINATION_2026-09-05.md); [`README.md`](https://github.com/androoAGI/starnet/blob/519a36d9927723c3e66cfb6742905e34c1197ca3/README.md).
- Basis: structural + corroborated execution evidence.
- Confidence: high.
- Caveats: `team.dispatch`, routing, group chat and handoff are not themselves the positive witness; the repeated-request/checkpoint hold is.
- Distinct S1 units: separate roster participants execute separate attributed autonomous turns/runs inside one StarNet group organization.
- Inter-S1 disturbance: repeated same-origin/same-agent/same-request peer handoff at an unchanged checkpoint can oscillate and duplicate sibling work.
- Attenuating coordination relation: the coordinator detects that repeated relation and holds the next peer turn instead of launching it.
- Feedback into subsequent S1 behaviour: `held` prevents the targeted sibling run from executing again until explicit continuation/correction; a changed checkpoint alters later admission behavior.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: it regulates a concrete oscillation produced by interaction among sibling operational units rather than merely transporting or ordering work.

## S3 — Inside-and-now control

- State: C(P)
- Function: expose and regulate the station's present operating organization — rostered agents, sessions/tasks, active work, current assignments/configuration, permission/consent waits, capability constraints and stop/halt state.
- Disturbance / variety regulated: multiple live/busy/cancelled agent runs; changing roster, tasks and sessions; permission waits; capability availability; spend/budget conditions; current work requiring intervention or reassignment.
- Decisive decision or feedback right: choose current station-level interventions over agents, commitments, assignments, configuration, run admission/termination and constraints, based on a whole-current view of station operation.
- Decision owner: base constructor mode — StarNet now supplies substantial first-party lead/orchestrator read/write tools plus station bridge/control primitives, but no shipped autonomous actor is evidenced as independently receiving a sufficient whole-station current view and owning the station-level allocation/intervention judgment. Parent mode — the Commander/operator owns the supported current-control decisions over the live station.
- Supporting / enforcement mechanisms: truthful frontend station projection, `station.status`, session/task/configuration tools, `team.dispatch`, `team.summon`, sidecar run/roster persistence, per-agent queues, event telemetry, consent/budget/capability gates, Night Shift scheduling and E-STOP enforcement.
- Closure path: current station/runtime state is surfaced → controller/Commander selects an intervention → first-party station/sidecar mutation path changes authoritative current state → current or later agent work follows that state and the product re-projects the result.
- Boundary reachability: the normal distribution contains both the authoritative frontend station bridge and model-facing orchestrator tools. `docs/ORCHESTRATOR_CONTROL_PLAN.md` explicitly targets live orchestrator control and marks the summon/control lane shipped. The model-facing station tool registry, however, omits the bridge's `station.status` verb and retains Commander-specific mutation constraints, so reachability supports a constructor without proving autonomous S3 ownership.
- Why this is / is not agent-owned: the lead can perform increasingly powerful control actions, including durable task changes and peer Dossier edits, but tool possession is not the decisive whole-station regulatory right. The pinned distribution does not establish a lead that autonomously surveys station-wide current conditions and revises shared commitments/resources by exception. Commander control closes the parent mode.
- Evidence: [`docs/ORCHESTRATOR_CONTROL_PLAN.md`](https://github.com/androoAGI/starnet/blob/519a36d9927723c3e66cfb6742905e34c1197ca3/docs/ORCHESTRATOR_CONTROL_PLAN.md); [`sidecar/tools/builtin/orchestration.js`](https://github.com/androoAGI/starnet/blob/519a36d9927723c3e66cfb6742905e34c1197ca3/sidecar/tools/builtin/orchestration.js); [`sidecar/tools/builtin/station.js`](https://github.com/androoAGI/starnet/blob/519a36d9927723c3e66cfb6742905e34c1197ca3/sidecar/tools/builtin/station.js); [`frontend/app/stationcommands.js`](https://github.com/androoAGI/starnet/blob/519a36d9927723c3e66cfb6742905e34c1197ca3/frontend/app/stationcommands.js); [`docs/NEXT.md`](https://github.com/androoAGI/starnet/blob/519a36d9927723c3e66cfb6742905e34c1197ca3/docs/NEXT.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: deterministic scheduling, budgets, permissions and E-STOP do not own S3; `team.dispatch`/`team.summon` and individual task/session/configuration mutations do not by themselves establish whole-system current regulation.
- Whole-system current view: the station bridge can produce a truthful station snapshot, but the registered model-facing station tools at the pinned revision do not expose `station.status` as a lead tool; `docs/NEXT.md` also records a remaining cross-session needs-input roll-up gap.
- Current-control decision scope: current roster/worker admission, task/session assignment, peer standing-order configuration, delegation, interruption/halt and capability/consent constraints.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | downstream autonomous station manager must be composed | authoritative current station/session/task/roster state indicates a present-control intervention | controller uses first-party orchestrator/station primitives; authoritative state changes and later work follows it | `docs/ORCHESTRATOR_CONTROL_PLAN.md`; `sidecar/tools/builtin/station.js`; `frontend/app/stationcommands.js` |
| Parent (`P`) | Commander/operator | live station/COMMS/task/session/consent surfaces show current work needing admission, stop, reassignment or configuration | Commander chooses the intervention; station/sidecar applies it and subsequent operation follows the returned state | `README.md`; `sidecar/tools/builtin/station.js`; `frontend/app/stationcommands.js` |

## S3* — Complementary audit

- State: A
- Function: independently challenge a sibling agent's produced artifact through a separate peer run and return findings into corrective rework before the reviewed result stands.
- Disturbance / variety regulated: an operational agent can publish an incorrect artifact or overclaim successful work; ordinary producer output alone is insufficient to establish correctness.
- Decisive decision or feedback right: a distinct peer agent decides whether the exact published artifact is acceptable or requires correction and communicates that finding back into the group workflow.
- Decision owner: the autonomous peer reviewer agent running as a separate StarNet participant/run.
- Supporting / enforcement mechanisms: `group.publish` copies exact producer bytes into an immutable group attachment; peers use `group.read`; attributed turns/handoffs preserve actor identity and route findings.
- Closure path: producer publishes artifact → separate peer reads immutable version → peer audit judgment requests correction → producer performs corrective turn and republishes → peer reads the replacement and verifies it.
- Boundary reachability: peer publish/read/handoff tools remain in the shipped `sidecar/group-sessions.js` runtime, and the repository preserves a first-party real-provider four-turn proof in which ENGINEER publishes, RESEARCHER challenges, ENGINEER republishes and RESEARCHER verifies.
- Why this is / is not agent-owned: the audit judgment is neither a deterministic checker nor the producer's self-critique. A distinct autonomous peer owns the finding; host machinery supplies immutable access, attribution and feedback routing.
- Evidence: [`sidecar/group-sessions.js`](https://github.com/androoAGI/starnet/blob/519a36d9927723c3e66cfb6742905e34c1197ca3/sidecar/group-sessions.js); [`docs/HANDOFF_GROUP_DM_2026-09-04.md`](https://github.com/androoAGI/starnet/blob/519a36d9927723c3e66cfb6742905e34c1197ca3/docs/HANDOFF_GROUP_DM_2026-09-04.md); [`docs/GROUP_DM_VERIFICATION_2026-09-04.md`](https://github.com/androoAGI/starnet/blob/519a36d9927723c3e66cfb6742905e34c1197ca3/docs/GROUP_DM_VERIFICATION_2026-09-04.md).
- Basis: structural + preserved real-provider execution evidence.
- Confidence: high.
- Caveats: repository-development QA/review lanes and autopilot self-critique are excluded from this finding; the positive state relies on the product group peer-review path.
- Claim being audited: the producer agent's published shared artifact/result is correct enough to stand as completed work.
- Ordinary reporting path: producer completes its attributed turn and publishes the artifact through `group.publish`.
- Complementary access path: a different participant reads the immutable exact version through `group.read` rather than relying on producer prose.
- Independence boundary: producer and reviewer are distinct autonomous participant runs; the peer receives shared exact bytes without producer workspace access.
- Who acts on findings: the producer receives the finding, performs corrective work and republishes; the reviewer subsequently verifies the correction.

## S4 — Outside-and-then intelligence

- State: C(P)
- Function: detect persistent work/interest capability gaps relative to the live crew, generate a concrete future roster adaptation and provide a path for that adaptation to change subsequent station capability.
- Disturbance / variety regulated: the Commander's recurring work/interests can evolve beyond capabilities represented by the current roster, leaving repeated demand that nobody on the crew covers.
- Decisive decision or feedback right: decide whether to add a recommended specialist/capability to the station in response to learned demand/coverage evidence.
- Decision owner: base constructor mode — StarNet supplies the evidence→gap→specialist recommendation and now also a first-party lead `team.summon` mechanism, but the standard distribution does not connect the recruiter signal to an autonomous lead as the decisive adaptation judgment. Parent mode — the Commander reviews/adopts the recommendation through first-party recruitment/summon flows.
- Supporting / enforcement mechanisms: WorkSignal capability histogram, learned topic/interests store, dossier/readiness gates, live roster read, specialty catalog, deterministic recruiter scoring, recommendation UI, outcome/preference memory and the summon machinery.
- Closure path: real work/topic evidence accumulates → recruiter compares warm demand with current roster coverage → uncovered demand yields a named specialist option → Commander/downstream autonomous adopter chooses whether to act → standard summon path adds the specialist to the live roster → subsequent work can use the added capability.
- Boundary reachability: `RecruiterStore` is loaded in the standard frontend and reads persisted product state/live roster; recruitment shelves/cards expose the option to the Commander. `team.summon` is a shipped lead tool, but the recruiter remains a frontend read/recommendation surface rather than a model-facing adaptation signal in the registered sidecar toolset.
- Why this is / is not agent-owned: the matcher deterministically generates and ranks options. The newly shipped summon tool proves that a lead can create a specialist when instructed, but no evidence establishes that the lead itself receives the capability-gap evidence and owns the prospective recruit/no-recruit judgment. Parent adoption remains operationally closed.
- Evidence: [`frontend/app/recruiter.js`](https://github.com/androoAGI/starnet/blob/519a36d9927723c3e66cfb6742905e34c1197ca3/frontend/app/recruiter.js); [`frontend/app/recruiterstore.js`](https://github.com/androoAGI/starnet/blob/519a36d9927723c3e66cfb6742905e34c1197ca3/frontend/app/recruiterstore.js); [`frontend/app/marketplace.js`](https://github.com/androoAGI/starnet/blob/519a36d9927723c3e66cfb6742905e34c1197ca3/frontend/app/marketplace.js); [`sidecar/tools/builtin/orchestration.js`](https://github.com/androoAGI/starnet/blob/519a36d9927723c3e66cfb6742905e34c1197ca3/sidecar/tools/builtin/orchestration.js); [`docs/ORCHESTRATOR_CONTROL_PLAN.md`](https://github.com/androoAGI/starnet/blob/519a36d9927723c3e66cfb6742905e34c1197ca3/docs/ORCHESTRATOR_CONTROL_PLAN.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: `team.summon` is an actuator, not by itself an S4 decision owner; the positive finding uses the uncovered-capability prospective recruitment path and its return into the live roster.
- External distinction: persisted evidence of actual work, warm learned topics/interests and stated goals/pain/ambition represents demand/environment distinctions not reducible to current roster state.
- Future / prospective distinction: the matcher asks which capability/specialist the crew should recruit next for repeated demand the current crew does not cover.
- Adaptation option generated: `Recruiter.recommend()` / `interestGaps()` returns a concrete unrostered specialty/class with evidence-derived rationale; `RecruiterStore.topPick()` exposes the strongest earned proposal.
- Path back into current capability / S3: recruitment/summon adds a specialist to the authoritative live roster, changing subsequent operational capability and current-control population.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | downstream autonomous adopter must be composed | learned work/topic evidence shows a warm uncovered capability against the live roster | first-party recruiter generates a concrete option and first-party summon machinery can realize it; autonomous adoption judgment is not wired | `frontend/app/recruiter.js`; `frontend/app/recruiterstore.js`; `sidecar/tools/builtin/orchestration.js` |
| Parent (`P`) | Commander/operator | evidence-backed specialist recommendation or Recruitment Bay exposes an uncovered capability option | Commander selects/adds the specialist; authoritative roster changes and later work can use it | `frontend/app/marketplace.js`; `README.md`; `docs/ORCHESTRATOR_CONTROL_PLAN.md` |

## S5 — Policy and identity

- State: —
- Function: no station-level identity/ultimate-policy closure function is established in the reviewed standard distribution.
- Disturbance / variety regulated: StarNet has extensive operating policy — Commander authority, autonomy/Full Access posture, capabilities, consent, budgets, roster specialties, per-agent Dossier identity/purpose/manual/context, standing orders, schedules and E-STOP — but these regulate operations/current control/adaptation rather than closing a station-level identity or constitutional-policy issue.
- Decisive decision or feedback right: no qualifying station-level identity/ultimate-policy decision path is established.
- Decision owner: not established for S5.
- Supporting / enforcement mechanisms: autonomy posture, capability map, consent decisions, budget caps, Commander controls, per-agent Dossier configuration, class/persona choices, E-STOP and recommendation preferences.
- Closure path: not applicable for the negative finding.
- Boundary reachability: the expanded orchestrator can read/edit another individual agent's Dossier for later runs, but that path remains lower-recursion agent configuration. No first-party station path was found that identifies an identity/ultimate-policy conflict, assigns legitimate ultimate authority over it and returns the resolution as a constitutional constraint on subsequent whole-station operation.
- Why this is / is not agent-owned: names such as `identity` and `purpose` in a crew member Dossier do not establish station-level S5. Nor do Full Access, approvals, budgets, roster choices or E-STOP become S5 merely because they constrain behavior.
- Evidence: [`README.md`](https://github.com/androoAGI/starnet/blob/519a36d9927723c3e66cfb6742905e34c1197ca3/README.md); [`sidecar/tools/builtin/station.js`](https://github.com/androoAGI/starnet/blob/519a36d9927723c3e66cfb6742905e34c1197ca3/sidecar/tools/builtin/station.js); [`frontend/app/stationcommands.js`](https://github.com/androoAGI/starnet/blob/519a36d9927723c3e66cfb6742905e34c1197ca3/frontend/app/stationcommands.js); [`sidecar/capability/registry.js`](https://github.com/androoAGI/starnet/blob/519a36d9927723c3e66cfb6742905e34c1197ca3/sidecar/capability/registry.js).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: the Commander has strong final authority over many operational settings. Methodology 0.3.6 requires an identity/ultimate-policy function before that authority can count as S5.

### Absence scope

- Surfaces inspected: product/architecture docs; orchestrator-control plan; model-facing team/session/task/configuration tools; authoritative station command bridge; per-agent Dossier mutation; autonomy/Full Access and consent policy; budget/capability/E-STOP controls; roster/classes; Night Shift; adaptive recruitment; group membership/handoff/review paths.
- Plausible first-party paths checked: `team.config`/`team.configure`; agent `identity`/`purpose` documents; Commander station ownership; autonomy posture; permission grants; budget ceilings; E-STOP; specialist recruitment/roster changes; standing orders; runtime policy enforcement.
- Why no material first-party path remains: these paths govern lower-recursion agent identity/instructions, present station operation, action authority or future capability adaptation. None is evidenced as a station-level identity/ultimate-policy issue with legitimate ultimate decision authority and a constitutional return-to-operation loop.

## Recursion

The assessment fixes the station as the recursion level. Individual crew agents/runs are operational units and may have their own identities, purposes and standing orders without thereby supplying S5 for the parent station. `team.configure` materially strengthens control over a child unit but does not change the recursion boundary.

## Variety and escalation

StarNet attenuates operational variety through capability scoping, consent, budget and concurrency limits; amplifies capacity through multiple specialist runs, delegation and recruitment; and preserves exceptional stop/control paths through explicit refusal, cancellation and E-STOP behavior. These mechanisms support the mapped functions but are not credited as additional VSM functions merely because they transport or enforce exceptional conditions.

The current S3 constructor remains incomplete as an autonomous station regulator because model-facing access does not yet expose the bridge's whole-station status snapshot as a lead tool and upstream documentation records remaining cross-session needs-input visibility gaps. The current S4 constructor remains incomplete as autonomous adaptation because recruiter evidence/options are not wired into the lead's prospective decision context.

## Evidence gaps

- No standard-distribution evidence was found that an autonomous lead independently receives a whole-station current snapshot and owns station-level resource/commitment intervention by exception; finding such a path could change S3 ownership.
- No standard-distribution path was found from `RecruiterStore` capability-gap evidence into an autonomous lead's recruit/no-recruit judgment; such a closed path could change S4 ownership.
- No station-level self-governance/charter/constitutional path was found. Per-agent Dossier identity/purpose edits are insufficient for S5 at the selected recursion.
- Repository-development `loops/`, QA and release-readiness actors are intentionally excluded from ownership even where they demonstrate sophisticated review/control patterns.

## Summary

| Function | State | Decisive owner / path |
| --- | --- | --- |
| S1 | A | autonomous StarNet model/agent actor inside the first-party sidecar loop |
| S2 | C | S2-specific deterministic repeated-request/checkpoint hold; autonomous coordination judgment is not shipped |
| S3 | C(P) | strengthened first-party orchestrator/station constructor + closed Commander current-control mode |
| S3* | A | distinct peer reviewer autonomously challenges immutable producer artifact and returns findings into correction |
| S4 | C(P) | adaptive capability-gap→specialist constructor with summon actuator + Commander-owned adoption mode |
| S5 | — | no station-level identity/ultimate-policy closure established |

Assessment signature: **`A C C(P) A C(P) —`**.

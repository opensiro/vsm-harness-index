---
harness_id: starnet
project_name: StarNet
repository: https://github.com/androoAGI/starnet
review_ref: f00aa04dfceac4e0d1a3a1e95b7b8d24d55456d1
reviewed_at: 2026-09-23
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-23
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C(P)
autonomy_s3_star: A
autonomy_s4: C(P)
autonomy_s5: —
---

# StarNet

## Review boundary

- System in focus: one first-party StarNet station at pinned revision `f00aa04dfceac4e0d1a3a1e95b7b8d24d55456d1`, including the Node sidecar agent runtime, station/roster state, bounded agent runs, group-session coordinator, capability/consent/budget gates, persistent work/memory/schedule state, Night Shift/autopilot paths, recommendation/recruitment machinery and the shipped desktop/browser control surfaces.
- Purpose and identity: operate a local-first multi-agent station in which autonomous agents perform real model/tool work under station-owned capabilities, permissions, budgets and persistent organization, while the Commander can shape the roster, workspaces, capabilities and operating posture.
- Relevant environment: the Commander/operator; repositories and local workspaces; model providers; MCP/external tools; user activity and interests; external web/data sources reached through granted tools; the specialty catalog; OS/process/runtime conditions.
- Standard-distribution boundary: StarNet-owned frontend, Node sidecar, shared event contract, runtime loop, group coordinator, persistent stores, capability/permission/budget layers and standard desktop/browser product flows. External model providers and MCP servers do not donate organizational functions; repository-development agents, CI, QA lanes and contributor workflows are not credited as operating-system owners.
- Credited operating / distribution surfaces: `README.md`; `docs/BRAIN.md`; `docs/HARNESS_ARCHITECTURE.md`; `sidecar/loop.js`; `sidecar/group-sessions.js`; `sidecar/nightshift.js`; `frontend/app/autopilot.js`; `frontend/app/recommend.js`; `frontend/app/recruiter.js`; `frontend/app/recruiterstore.js`; shipped station/COMMS/Recruitment Bay flows; first-party sidecar HTTP control paths corroborated by `qa/dogfood/SHIFTS.md`.
- Adjacent first-party surfaces excluded from ownership: feature-branch merge rituals and contributor handoff instructions; QA/product-perfect locks; development-only dogfood actors and CI verdicts; historical design proposals not present in the pinned runtime; provider internals; untracked worktree artifacts. Historical group-DM verification documents are used only to corroborate behavior whose implementing source is present at the pinned revision.
- First-party operating / deployment modes considered: ordinary direct agent run; multiple bounded agent runs; group chat with peer handoff/shared artifacts; Commander-driven station control; unattended Night Shift/autopilot within configured posture/leash; adaptive recommendation/recruitment; scheduled/recurring work; standard capability/consent/budget enforcement.
- Recursion level: the whole StarNet station is the system-in-focus. Individual autonomous agent runs/group participants are installation-level S1 units. Internal model turns/tool calls are below this recursion. Repository-development agents and feature worktrees are outside it.
- Reviewed revision: `f00aa04dfceac4e0d1a3a1e95b7b8d24d55456d1`.
- Observation date: 2026-09-23.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

StarNet's first-party sidecar owns the executable harness boundary. `runAgentLoop()` is the model→tool→result loop; providers are transport adapters, while StarNet resolves capabilities, approvals, budgets, persistence and dispatch before the model can act. The normal station can host multiple genuinely distinct bounded agent runs with separate workspace/permission state, while the visual station and COMMS surfaces project runtime truth rather than inventing parallel product state.

The multi-agent group coordinator is organizationally material. Group participants are selected from the live roster; each turn is attributed to one participant; agents may explicitly hand off to another participant, publish an immutable exact file version and let peers read that version without granting filesystem access. The coordinator bounds pending work, prevents repeated unchanged handoff oscillation by holding a repeated request, persists questions/turns across restarts and can route a finding back into another attributed turn.

StarNet also distinguishes present control from future adaptation. Present organization is controlled through the station/sidecar run, roster, stop/halt, capability, consent and workspace paths. Future capability adaptation has a specific recruitment path: learned work/topic evidence is compared with the live roster, uncovered warm capability demand produces a concrete specialist recommendation, and the Commander can enter the first-party summon flow to add capability to the roster. The recommender is deterministic, so it does not itself become an autonomous-agent S4 owner.

## S1 — Operations

- State: A
- Function: perform user-directed and explicitly permitted unattended work through autonomous StarNet agent runs using real model calls and granted tools.
- Disturbance / variety regulated: open-ended user objectives, workspace/repository state, tool results, provider responses, permissions, budget limits, task-brief uncertainty, schedules and external information reached through granted capabilities.
- Decisive decision or feedback right: choose substantive task reasoning, model/tool actions, whether further tool work is needed and how to respond to returned tool/environment feedback within the admitted objective and host constraints.
- Decision owner: the autonomous model/agent executing inside StarNet's first-party `runAgentLoop()` path.
- Supporting / enforcement mechanisms: capability resolution, consent broker, budget engine, context management, run queue, provider adapters, persistent stores, Task Brief gates, Night Shift scheduling and event/telemetry contracts.
- Closure path: a user/schedule/unattended trigger admits work → StarNet builds the permitted tool/capability context → the autonomous agent selects model/tool actions → StarNet executes and returns tool results → the agent continues until completion/bounded stop → resulting artifacts/state are persisted and surfaced.
- Boundary reachability: the README and architecture reference describe the Node sidecar as the normal product harness, and `sidecar/loop.js` is the first-party executable agentic loop used by the standard runtime rather than a development-only example.
- Why this is / is not agent-owned: host code enforces permissions, budgets and lifecycle, but the task-local organizational discretion over reasoning and useful action remains with the autonomous agent. Removing the model actor leaves enforcement/runtime machinery without the substantive operational decision loop.
- Evidence: [`README.md`](https://github.com/androoAGI/starnet/blob/f00aa04dfceac4e0d1a3a1e95b7b8d24d55456d1/README.md); [`docs/BRAIN.md`](https://github.com/androoAGI/starnet/blob/f00aa04dfceac4e0d1a3a1e95b7b8d24d55456d1/docs/BRAIN.md); [`docs/HARNESS_ARCHITECTURE.md`](https://github.com/androoAGI/starnet/blob/f00aa04dfceac4e0d1a3a1e95b7b8d24d55456d1/docs/HARNESS_ARCHITECTURE.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: model-provider internals are not credited as StarNet functions; `A` is based on the autonomous actor reached and governed by the shipped StarNet execution path.

## S2 — Coordination

- State: C
- Function: attenuate interaction-generated handoff oscillation and uncontrolled peer-work continuation among sibling agent runs in a group while preserving explicit peer requests and bounded continuation.
- Disturbance / variety regulated: a participant can repeatedly hand the same request back toward a peer without any new artifact/question checkpoint, producing an A↔B request loop or duplicated peer work; abandoned handoffs and duplicate pending requests can also amplify the same group-work disturbance.
- Decisive decision or feedback right: determine whether another peer turn may be admitted for the same origin/request/checkpoint or must be held for review/explicit continuation.
- Decision owner: not autonomously supplied for the decisive anti-oscillation judgment. The first-party coordinator implements the S2-specific hold/retry path deterministically; an autonomous agent can initiate useful handoffs, but host enforcement of the repeated-request rule is not agent-owned organizational discretion.
- Supporting / enforcement mechanisms: durable group turn queue, origin/parent attribution, immutable shared-artifact hashes, answered-question checkpointing, bounded pending work, one recovery nudge, Stop/restart semantics and participant membership.
- Closure path: sibling participant requests peer work → coordinator records origin/request/checkpoint → repeated completed same-agent/same-request turns at an unchanged checkpoint are detected → the next turn becomes `held` with `Repeated request; review before continuing` → no further sibling execution occurs until an explicit continuation path changes the state; new artifact/question evidence changes the checkpoint and subsequent behavior can proceed.
- Boundary reachability: `sidecar/group-sessions.js` is the shipped group runtime, and README's room/hallway contract exposes capability-scoped teams and authorized handoff lanes as product behavior.
- Why this is / is not agent-owned: autonomous peers own task-local handoff requests, but the decisive disturbance attenuation at the repeated-loop boundary is deterministic coordinator logic. The first-party S2-specific feedback path is therefore real while autonomous ownership of that coordination judgment remains to be composed.
- Evidence: [`sidecar/group-sessions.js`](https://github.com/androoAGI/starnet/blob/f00aa04dfceac4e0d1a3a1e95b7b8d24d55456d1/sidecar/group-sessions.js); [`README.md`](https://github.com/androoAGI/starnet/blob/f00aa04dfceac4e0d1a3a1e95b7b8d24d55456d1/README.md); [`docs/HANDOFF_GROUP_COORDINATION_2026-09-05.md`](https://github.com/androoAGI/starnet/blob/f00aa04dfceac4e0d1a3a1e95b7b8d24d55456d1/docs/HANDOFF_GROUP_COORDINATION_2026-09-05.md).
- Basis: structural + corroborated execution evidence.
- Confidence: high.
- Caveats: mere plurality, group chat, `@mention`, queueing and handoff are not the reason for the positive finding; the repeated-request/checkpoint hold path is the S2-specific witness.
- Distinct S1 units: separate roster participants execute separate attributed autonomous turns/runs inside one StarNet group organization.
- Inter-S1 disturbance: repeated same-origin/same-agent/same-request peer handoff at an unchanged artifact/question checkpoint can oscillate and duplicate sibling work.
- Attenuating coordination relation: the coordinator detects that repeated relation and holds the next peer turn instead of launching it, while also bounding pending work and recovery nudges.
- Feedback into subsequent S1 behaviour: `held` prevents the targeted sibling run from executing again until explicit continuation; changed artifact/question evidence changes the checkpoint and therefore the later admission behavior.
- Why specifically S2: the relation regulates interference/oscillation created by interaction among sibling operational units; it is not merely routing, delegation, persistence or whole-system managerial allocation.

## S3 — Inside-and-now control

- State: C(P)
- Function: expose and regulate the station's present operating organization — rostered agents, active runs, current permissions/capabilities, stop/halt state, work assignment and current execution state.
- Disturbance / variety regulated: multiple live/busy/cancelled agent runs, changes in roster and assignment, permission/consent waits, capability availability, spend/budget conditions, unattended work that must be stopped, and current work that needs operator intervention.
- Decisive decision or feedback right: choose which current agent exists/works, which run is admitted or interrupted, whether all current/unattended work is halted/resumed, and which capabilities/consents constrain subsequent operation.
- Decision owner: constructor mode — no autonomous whole-station manager is packaged, but first-party HTTP/runtime seams expose roster/run/halt/control primitives over the same authoritative station state. Parent mode — the Commander/operator owns the shipped station's current-control decisions through roster, station, COMMS, consent, capability and E-STOP controls.
- Supporting / enforcement mechanisms: frontend station projection, sidecar run/roster persistence, per-agent queues, event telemetry, budget/capability gates, Night Shift scheduler, diagnostics and E-STOP enforcement.
- Closure path: current station/runtime state is surfaced → controller/operator selects a run/roster/capability/halt intervention → the first-party sidecar applies it to authoritative runtime state → running or subsequent agent work changes accordingly and the resulting state is re-projected.
- Boundary reachability: the standard station UI uses these controls, while first-party sidecar paths such as roster mutation, run admission and halt are executable product interfaces; dogfood evidence demonstrates `POST /api/roster`, `POST /api/run`, `POST /api/halt` and persisted diagnostics against the real sidecar seam.
- Why this is / is not agent-owned: Night Shift/autopilot can self-initiate bounded work for an agent, but it does not own whole-station current allocation. The Commander closes the parent mode; downstream autonomous current control would need to be composed over the exposed control seam.
- Evidence: [`README.md`](https://github.com/androoAGI/starnet/blob/f00aa04dfceac4e0d1a3a1e95b7b8d24d55456d1/README.md); [`docs/HARNESS_ARCHITECTURE.md`](https://github.com/androoAGI/starnet/blob/f00aa04dfceac4e0d1a3a1e95b7b8d24d55456d1/docs/HARNESS_ARCHITECTURE.md); [`qa/dogfood/SHIFTS.md`](https://github.com/androoAGI/starnet/blob/f00aa04dfceac4e0d1a3a1e95b7b8d24d55456d1/qa/dogfood/SHIFTS.md); [`sidecar/nightshift.js`](https://github.com/androoAGI/starnet/blob/f00aa04dfceac4e0d1a3a1e95b7b8d24d55456d1/sidecar/nightshift.js).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: deterministic scheduling, budget enforcement and E-STOP power do not themselves own S3; they support the caller/Commander decision.
- Whole-system current view: the station projects live roster/run/activity/task/spend/capability state from validated runtime events and persistent sidecar state; diagnostics preserve current/last-run truth across restart.
- Current-control decision scope: recruit/remove/configure current agents; admit and interrupt runs; stop/halt/resume active or unattended work; change present capability/consent constraints and work assignment.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | downstream autonomous manager must be composed | authoritative current station/run/roster state indicates a present-control intervention | controller uses first-party roster/run/halt/control seams; sidecar mutates authoritative current operation and returns updated runtime state | `docs/HARNESS_ARCHITECTURE.md`; `qa/dogfood/SHIFTS.md` |
| Parent (`P`) | Commander/operator | station/COMMS/consent/capability surfaces show current work needing admission, stop, reassignment or permission | Commander changes roster/run/capability/consent or invokes E-STOP; sidecar applies the decision and subsequent operation follows it | `README.md`; `docs/HARNESS_ARCHITECTURE.md`; `qa/dogfood/SHIFTS.md` |

## S3* — Complementary audit

- State: A
- Function: independently challenge a sibling agent's produced artifact through a separate peer run and return findings into corrective rework before the reviewed result is accepted.
- Disturbance / variety regulated: an operational agent can publish an incorrect artifact or overclaim successful work; ordinary producer output alone is insufficient to establish that the artifact is correct.
- Decisive decision or feedback right: a distinct peer agent decides whether the exact published artifact is acceptable or requires correction, and communicates that finding back into the group workflow.
- Decision owner: the autonomous peer reviewer agent running as a separate StarNet participant/run.
- Supporting / enforcement mechanisms: `group.publish` copies the producer's exact bytes into an immutable group artifact; `group.read` gives peers exact-version access without filesystem sharing; attributed turns/handoffs preserve actor identity and actual response evidence.
- Closure path: producer publishes artifact → separate peer reads immutable version → peer audit judgment identifies a defect and requests correction → producer executes a new corrective turn and republishes → peer reads the new version and verifies it.
- Boundary reachability: peer handoff/publish/read tools live in `sidecar/group-sessions.js` and are available to normal first-party group participants; the frozen repository preserves a real-provider four-turn proof of this exact correction cycle.
- Why this is / is not agent-owned: the audit judgment is not a deterministic checker and not the producer's self-critique. A distinct autonomous reviewer owns the finding. StarNet's host only supplies immutable access, attribution and routing of the feedback.
- Evidence: [`sidecar/group-sessions.js`](https://github.com/androoAGI/starnet/blob/f00aa04dfceac4e0d1a3a1e95b7b8d24d55456d1/sidecar/group-sessions.js); [`docs/HANDOFF_GROUP_DM_2026-09-04.md`](https://github.com/androoAGI/starnet/blob/f00aa04dfceac4e0d1a3a1e95b7b8d24d55456d1/docs/HANDOFF_GROUP_DM_2026-09-04.md); [`frontend/app/autopilot.js`](https://github.com/androoAGI/starnet/blob/f00aa04dfceac4e0d1a3a1e95b7b8d24d55456d1/frontend/app/autopilot.js).
- Basis: structural + preserved real-provider execution evidence.
- Confidence: high.
- Caveats: autopilot's own reason-only critique is explicitly self-review and is not credited for S3*. The positive finding instead relies on the distinct peer-review correction loop.
- Claim being audited: the producer agent's published shared artifact/result is correct enough to stand as completed work.
- Ordinary reporting path: the producer completes its attributed turn and publishes the artifact through `group.publish`.
- Complementary access path: a different participant receives an attributed peer turn and reads the immutable exact version through `group.read` rather than relying on the producer's prose claim.
- Independence boundary: reviewer and producer are distinct autonomous participant runs; the reviewer receives exact shared bytes and cannot silently inherit producer workspace state through `group.read`. The preserved proof names ENGINEER as producer and RESEARCHER as reviewer.
- Who acts on findings: the producer receives the review finding/request, performs a corrective turn and republishes; the reviewer subsequently verifies the corrected version.

## S4 — Outside-and-then adaptation

- State: C(P)
- Function: detect persistent work/interest capability gaps relative to the live crew, generate a concrete future roster adaptation and provide a path for that adaptation to change subsequent station capability.
- Disturbance / variety regulated: the Commander's recurring work/interests can evolve beyond the capabilities represented by the current roster, leaving repeated demand that nobody on the crew covers.
- Decisive decision or feedback right: decide whether to add a recommended specialist/capability to the station in response to learned demand/coverage evidence.
- Decision owner: constructor mode — StarNet supplies the function-specific evidence→gap→specialist recommendation and summon path, but no autonomous agent owns the final recruitment decision. Parent mode — the Commander reviews the recommendation and chooses the specialist through the first-party Recruitment Bay/summon flow.
- Supporting / enforcement mechanisms: WorkSignal capability histogram, learned topic/interests store, dossier/readiness gates, live roster read, specialty catalog, deterministic recruiter scoring, recommendation spine, outcome/preference memory and the summon UI.
- Closure path: real work/topic evidence accumulates → recruiter compares warm demand with current roster coverage → uncovered demand yields a named specialist option → Commander/downstream controller enters the summon path → a new specialist is added to the live roster → subsequent work can use the added capability.
- Boundary reachability: `RecruiterStore` reads normal persisted product state and live roster; `maybeRecruit()` exposes the earned recommendation in ordinary COMMS and deep-links to `App.openSummonBay`; the standard Recruitment Bay is the product's first-party new-agent/specialty surface.
- Why this is / is not agent-owned: the matcher and recommendation scorer are deterministic machinery. They generate and prioritize adaptation options but do not satisfy Methodology `A`; final adoption is human-owned in the shipped parent mode, while an autonomous adopter would need composition over the specific path.
- Evidence: [`frontend/app/recruiter.js`](https://github.com/androoAGI/starnet/blob/f00aa04dfceac4e0d1a3a1e95b7b8d24d55456d1/frontend/app/recruiter.js); [`frontend/app/recruiterstore.js`](https://github.com/androoAGI/starnet/blob/f00aa04dfceac4e0d1a3a1e95b7b8d24d55456d1/frontend/app/recruiterstore.js); [`frontend/app/recommend.js`](https://github.com/androoAGI/starnet/blob/f00aa04dfceac4e0d1a3a1e95b7b8d24d55456d1/frontend/app/recommend.js); [`frontend/app/chat.js`](https://github.com/androoAGI/starnet/blob/f00aa04dfceac4e0d1a3a1e95b7b8d24d55456d1/frontend/app/chat.js); [`frontend/app/marketplace.js`](https://github.com/androoAGI/starnet/blob/f00aa04dfceac4e0d1a3a1e95b7b8d24d55456d1/frontend/app/marketplace.js).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: outcome-weighted recommendation ordering alone would not establish S4; the positive finding uses the specific uncovered-capability recruitment path and its return into the live roster.
- External distinction: persisted evidence of the Commander's actual work, warm learned topics/interests and stated goals/pain/ambition represent demand/environment distinctions not reducible to current internal roster state.
- Future / prospective distinction: the matcher asks which capability/specialist the crew should recruit next for repeated demand that the current crew does not cover; this is prospective capability composition rather than current task routing.
- Adaptation option generated: `Recruiter.recommend()` / `interestGaps()` returns a concrete unrostered specialty/class with an evidence-derived reason, and `RecruiterStore.topPick()` supplies the single earned recruit proposal.
- Path back into current capability / S3: the recruit proposal deep-links into the standard summon/Recruitment Bay path; selecting a specialist adds an agent/specialty to the authoritative roster, changing the station's subsequent operational capability and current-control population.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | downstream autonomous adopter must be composed | learned work/topic evidence shows a warm capability gap against live roster | first-party recruiter produces a concrete specialist and exposes the summon path; an autonomous owner must still be supplied to decide adoption | `frontend/app/recruiter.js`; `frontend/app/recruiterstore.js`; `frontend/app/chat.js` |
| Parent (`P`) | Commander/operator | earned recruit card or Recruitment Bay shows evidence-backed uncovered capability/specialist | Commander enters summon flow and selects/adds the specialist; authoritative roster changes and later work can use it | `frontend/app/chat.js`; `frontend/app/marketplace.js`; `README.md` |

## S5 — Identity / ultimate policy

- State: —
- Function: no station-level identity/ultimate-policy closure function is established in the reviewed standard distribution.
- Disturbance / variety regulated: StarNet has extensive operating policy — autonomy posture/leash, capabilities, consent, budgets, roster specialties, standing orders, Task Brief gates, schedules and E-STOP — but these regulate operations/current control/adaptation rather than resolving a dispute about the station's ultimate identity or constitutional policy.
- Decisive decision or feedback right: no qualifying identity/ultimate-policy decision path established.
- Decision owner: not established for S5.
- Supporting / enforcement mechanisms: autonomy dial, capability map, consent decisions, budget caps, standing orders, class/persona choices, E-STOP and recommendation preferences.
- Closure path: not applicable for the negative finding.
- Boundary reachability: no first-party operating path was found that elevates an identity/ultimate-policy issue, assigns ultimate authority over it and returns that resolution as the constitutional constraint for subsequent operation.
- Why this is / is not agent-owned: neither the model's system prompt/persona nor the Commander's ordinary operational controls become S5 merely because they constrain behavior.
- Evidence: [`README.md`](https://github.com/androoAGI/starnet/blob/f00aa04dfceac4e0d1a3a1e95b7b8d24d55456d1/README.md); [`docs/HARNESS_ARCHITECTURE.md`](https://github.com/androoAGI/starnet/blob/f00aa04dfceac4e0d1a3a1e95b7b8d24d55456d1/docs/HARNESS_ARCHITECTURE.md); [`sidecar/nightshift.js`](https://github.com/androoAGI/starnet/blob/f00aa04dfceac4e0d1a3a1e95b7b8d24d55456d1/sidecar/nightshift.js); [`frontend/app/autopilot.js`](https://github.com/androoAGI/starnet/blob/f00aa04dfceac4e0d1a3a1e95b7b8d24d55456d1/frontend/app/autopilot.js).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: the Commander has strong final authority over many operational settings. Methodology 0.3.6 does not turn ordinary approvals, autonomy levels, permissions, roster choices or emergency stop into S5 without an identity/ultimate-policy function.

### Absence scope

- Surfaces inspected: autonomy posture and unattended-work rules; Task Brief/standing orders; capability/consent/budget policy; roster/specialty configuration; Night Shift/E-STOP; recommendation/recruitment learning; group membership/handoff rules; architecture/product contract.
- Plausible first-party paths checked: persona/system prompt; Commander final say on brief questions; autonomy dial; E-STOP; capability placement; permission grants; budget ceilings; specialist identity/roster changes; learned preference policy.
- Why no material first-party path remains: each reviewed path governs task execution, current resource/control constraints or future capability adaptation. None is evidenced as an organizational identity/ultimate-policy dispute with a dedicated authoritative resolution and constitutional return-to-operation loop.

## Summary

| Function | State | Decisive owner / path |
| --- | --- | --- |
| S1 | A | autonomous StarNet model/agent actor inside the first-party sidecar loop |
| S2 | C | S2-specific deterministic group anti-oscillation/hold path; autonomous coordination owner still requires composition |
| S3 | C(P) | first-party whole-current control seam for composition + closed Commander current-control mode |
| S3* | A | distinct peer reviewer autonomously challenges immutable producer artifact and returns findings into correction |
| S4 | C(P) | adaptive capability-gap→specialist constructor path + Commander-owned summon/adoption mode |
| S5 | — | no identity/ultimate-policy closure established |

Assessment signature: **`A C C(P) A C(P) —`**.

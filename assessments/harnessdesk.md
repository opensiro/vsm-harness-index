---
harness_id: harnessdesk
project_name: HarnessDesk
repository: https://github.com/HarnessDesk/HarnessDesk
review_ref: 24add77185eebe321b0aa0b578933acf4a8e05d3
reviewed_at: 2026-10-01
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-01
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: C(P)
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# HarnessDesk

## Review boundary

- System in focus: one local HarnessDesk engineering desk at project/room recursion: the host process, shared conversation/history/policy state, project workspaces and managed worktrees, standing Agent definitions and seating, Room/Board/Channel collaboration, Flow engine, handoff/race machinery, common plugin/tool projection, runtime adapters, permissions/approvals, audit/cost/evidence surfaces and supported HarnessDesk-seated coding-agent conversations.
- Purpose and identity: provide a vendor-neutral control plane in which replaceable coding agents can perform software work under one shared context, coordination, policy, history, cost and evidence layer while HarnessDesk itself does not become a coding agent.
- Relevant environment: the parent developer/operator; repositories, branches, worktrees, pull requests and CI; local checks; vendor coding-agent runtimes and their model services; plugin-provided tools; local filesystem/process/browser/mobile-test environments; forge APIs reached through local credentials.
- Operational units: supported autonomous coding-agent conversations or standing HarnessDesk Agent seats that directly perform engineering work; Room membership and Flow roles organize those cells but do not import the external runtime's internal agent organization.
- Standard-distribution boundary: the macOS/host product at the frozen ref, its first-party Agent/seat layer, Codex/ACP adapters, Room/Board/Channel, worktree and claim machinery, Flow engine and shipped flows, permission/approval surface, common plugins/tool gateway, local evidence store, audit/usage/history state and read/write operator surfaces that ship with the product.
- Credited operating / distribution surfaces: `README.md`; `docs/architecture.md`; `docs/agents.md`; `docs/multi-agent.md`; `docs/flows.md`; `.harnessdesk/flows/fix-and-review.yml`; `.harnessdesk/flows/race.yml`; current local evidence/check/CI integration and first-party host control paths described by those frozen artifacts.
- Adjacent first-party surfaces excluded from ownership: repository-development contributors and maintainers; CI/release machinery for developing HarnessDesk; claim-recording demos/tests as tests rather than runtime owners; future server/account/event-trigger/routine/jury/landing-queue roadmap surfaces; public VISION governance as development governance rather than deployed runtime authority; implementation internals of Codex, Claude Code, Cursor, Gemini and other external runtimes.
- First-party operating / deployment modes considered: local desktop/headless host; solo and Room operation; manually started Flow operation; built-in/project Agent seating; Codex and ACP-backed sessions; managed worktrees and `/race`; locally observed check/diff/PR/CI evidence. Future hosted and event-triggered modes are excluded because the frozen repository states they are not built.
- Recursion level: one HarnessDesk project/room organization coordinating several autonomous coding work cells. Each external coding runtime may contain its own lower-recursion organization, but its internal planner/tool loop is not inherited into this assessment.
- Reviewed revision: `24add77185eebe321b0aa0b578933acf4a8e05d3`.
- Observation date: 2026-10-01.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

HarnessDesk is a local control plane that drives coding agents it does not own. The host normalizes sessions, transcripts, approvals, worktrees, team coordination, usage and evidence above a vendor-specific agent plane. Codex is reached through a native adapter; other agents use ACP. Capabilities are negotiated rather than assumed, and agent command execution remains inside the selected external runtime's own sandbox and tool loop.

First-party `Agent` definitions provide durable work roles, briefs, answer vocabularies, permission ceilings and preferred seats. The product ships reviewer, implementer, judge, researcher and other role definitions, then seats those roles on a compatible external runtime. A Room provides a shared Board, Channel and roster. Board claims atomically reject overlapping file ownership and unfinished dependencies; claims carry leases; worktrees provide stronger isolation when requested. Agent messages are attributed, policy-gated and loop-limited.

Flows add a statechart over the Room. A Flow declares roles, seats, permissions, outcomes and guarded transitions; the run freezes that policy and opens/re-arms role seats as rounds advance. The repository ships concrete `fix-and-review` and `race` flows. The former runs one autonomous fixer and three independent autonomous reviewers, sends any reviewer request for changes back to the fixer, and reserves final merge for a person. The latter creates two isolated attempts and a third autonomous judge.

HarnessDesk separately records operational evidence it observes itself. Board state does not become Ready merely because an agent says work is complete: fresh local checks, diffs, pull requests and CI are bound to concrete commits, stale evidence is downgraded, and restored evidence cannot establish readiness until re-observed locally.

## Operational model

At the selected recursion, HarnessDesk-seated coding-agent conversations are the S1 work cells. The host supplies common context, tools, policy and coordination but does not make the open-ended implementation decision for them. Work can be started as a standing Agent role or as a runtime session, and several cells can share one Room.

Coordination has both distributed and parent-controlled modes. Agents autonomously claim non-conflicting work, release or complete claims, inspect conflicts, exchange context and react to returned board state. The host atomically enforces claims, worktree boundaries, message policy and delivery limits. Separately, the ordinary Room explicitly has a human referee who decides current assignments/interventions and takes irreversible steps. A Flow is that referee's current-control policy written down and deterministically enacted, but the shipped Flow engine does not itself introduce an autonomous whole-system supervisor.

## S1 — Operations

- State: A
- Function: perform repository-facing software-engineering work as a HarnessDesk-seated autonomous coding-agent cell and return changed artifacts, evidence, outcomes and context into the desk.
- Disturbance / variety regulated: task-specific repository state, implementation choices, tool/test feedback, runtime capability differences, blockers and new evidence encountered while producing a software outcome.
- Decisive decision or feedback right: choose and revise the next task-specific coding, inspection, tool or response action from the assigned objective and observed environment.
- Decision owner: the supported autonomous coding-agent session seated through HarnessDesk, including first-party standing Agent roles instantiated on a compatible Codex/ACP runtime.
- Supporting / enforcement mechanisms: Agent briefs and seat selection, adapter capability negotiation, shared transcript/history, plugin tool projection, approvals/permission ceilings, managed worktrees, task/context records and host persistence.
- Closure path: task/role enters a seated conversation → autonomous agent inspects and acts through its external runtime/tools → repository/tool feedback returns through that same session → agent revises/continues/completes work → HarnessDesk persists outcome/context/evidence for subsequent operation.
- Boundary reachability: Agent definitions, seating, adapters, Room membership and tool projection are shipped first-party operating paths. They instantiate supported autonomous sessions without requiring application-authored orchestration, while the external runtime's hidden internals remain outside the credited boundary.
- Why this is / is not agent-owned: if the autonomous coding-agent actor is removed while host state, worktrees, board, policies and adapters remain, the open-ended implementation decisions stop; the remaining host can enforce and persist but cannot produce materially the same discretionary engineering work.
- Evidence: [`README.md`](https://github.com/HarnessDesk/HarnessDesk/blob/24add77185eebe321b0aa0b578933acf4a8e05d3/README.md); [`docs/architecture.md`](https://github.com/HarnessDesk/HarnessDesk/blob/24add77185eebe321b0aa0b578933acf4a8e05d3/docs/architecture.md); [`docs/agents.md`](https://github.com/HarnessDesk/HarnessDesk/blob/24add77185eebe321b0aa0b578933acf4a8e05d3/docs/agents.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: this state does not inherit delegation, memory, planning, approval or other internal functions from Codex/Claude/Cursor/Gemini. It credits only the autonomous operational actor reachable through HarnessDesk's supported seating/adapters.

## S2 — Coordination

- State: A
- Function: attenuate destructive interference among concurrent S1 coding cells that may claim the same task/files, overwrite one another, or create runaway inter-agent message loops.
- Distinct S1 units: two or more independently running HarnessDesk-seated coding-agent conversations in one Room/project, potentially on different vendor runtimes.
- Inter-S1 disturbance: overlapping edits/claims on the same paths or one task, unsafe concurrent access to shared work, and recursive peer-message chatter that can consume turns without advancing the project.
- Attenuating coordination relation: atomic Board claims reject already-held intents, unfinished dependencies and overlapping file globs; claims carry leases and can be taken over after expiry; managed worktrees isolate racing implementations; message delivery is attributed, rate/duplicate/queue limited and never automatically bounces awakened replies back to the sender.
- Feedback into subsequent S1 behaviour: claim/conflict results are returned to the requesting autonomous agent, which must choose another claim, release/wait, adjust paths, use an isolated worktree, communicate with a peer or escalate. Context packages from completed dependencies are returned to subsequent claimants and materially alter their next work.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the evidence names concrete interference modes—overlapping file ownership and recursive messaging—and first-party mechanisms specifically designed to stop those collisions, with demonstrated refusal/return paths into later agent behaviour.
- Decisive decision or feedback right: after the deterministic host exposes a conflict or safe claim, each autonomous participating agent owns the discretionary mutual-adjustment response over what work/path to take or release; the host owns atomic exclusion and loop-control enforcement.
- Decision owner: participating autonomous coding-agent cells, with deterministic HarnessDesk enforcement supporting their mutual adjustment.
- Supporting / enforcement mechanisms: Board transaction ownership, file-glob conflict checks, claim leases, worktrees, dependency gating, Channel delivery states, message loop guards, context packages and host audit records.
- Closure path: agents advertise/claim intended work → host detects incompatible ownership or accepts a safe claim → result is returned to the agent → agent changes subsequent work/communication or proceeds → release/completion updates shared state for peers and dependencies.
- Boundary reachability: Board/team tools are projected by HarnessDesk to Codex and ACP agents in supported Rooms; caller identity is correlated by the host and unattributed calls are refused. No custom external coordinator is required.
- Why this is / is not agent-owned: deterministic exclusion alone would still reject a collision if agents were removed, but it would not choose the organizational response—alternate work, changed files, peer handoff or wait. That discretion belongs to the autonomous S1 participants in the shipped team mode.
- Evidence: [`docs/multi-agent.md`](https://github.com/HarnessDesk/HarnessDesk/blob/24add77185eebe321b0aa0b578933acf4a8e05d3/docs/multi-agent.md); [`README.md`](https://github.com/HarnessDesk/HarnessDesk/blob/24add77185eebe321b0aa0b578933acf4a8e05d3/README.md); [`docs/architecture.md`](https://github.com/HarnessDesk/HarnessDesk/blob/24add77185eebe321b0aa0b578933acf4a8e05d3/docs/architecture.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: file ownership is strongest within Board/worktree participation; an unrelated out-of-band process is not automatically constrained by HarnessDesk's claim state.

## S3 — Inside-and-now control

- State: C(P)
- Function: regulate the current Room as a whole by deciding roles/permissions, moving current work between operational cells, responding to round outcomes and reserving irreversible steps for an authority chosen by the Room policy.
- Disturbance / variety regulated: current imbalance or mismatch among work cells—who should perform which role now, whether a failed/rejected round must return to implementation, whether an agent may publish/merge, and when current work should stop or move to a person.
- Whole-system current view: the Room Board/roster/channel and Flow run expose current members, claims, role-addressed cards, outcomes and run state across the participating work cells.
- Decisive decision or feedback right: select or revise current project roles, permissions, work transitions and exception handling on behalf of the Room rather than merely execute one local task.
- Decision owner: in the constructor base mode, the developer/Flow author chooses the whole-room policy and the deterministic Flow engine enforces it; HarnessDesk supplies no autonomous S3 decision actor by default. In the parent mode, the human Room referee directly owns current assignment/intervention/irreversible-step decisions.
- Supporting / enforcement mechanisms: Flow parser/validator, role seating, permission ceilings, outcome vocabulary, guarded first-match transitions, frozen run policy, Board state, person-role cards, Room UI and stop/restart semantics.
- Closure path: current Room/round state reaches either the predeclared Flow policy or human referee → current-control decision selects the next role/card/permission/intervention → Flow/Board/Room machinery opens or changes subsequent work → S1 cells operate under the returned decision.
- Boundary reachability: Flow files are a supported first-party project format and the frozen repository ships working Flow examples; ordinary Rooms expose the human referee path directly. Both paths are in the local standard distribution rather than development-only dogfood.
- Why this is / is not agent-owned: the Flow engine can enforce a preselected whole-room policy but does not autonomously choose or revise that policy from current operational variety. The ordinary Room explicitly assigns the decisive referee right to the human. A separate agent-owned S3 supervisor is therefore not established.
- Evidence: [`docs/flows.md`](https://github.com/HarnessDesk/HarnessDesk/blob/24add77185eebe321b0aa0b578933acf4a8e05d3/docs/flows.md); [`docs/multi-agent.md`](https://github.com/HarnessDesk/HarnessDesk/blob/24add77185eebe321b0aa0b578933acf4a8e05d3/docs/multi-agent.md); [`.harnessdesk/flows/fix-and-review.yml`](https://github.com/HarnessDesk/HarnessDesk/blob/24add77185eebe321b0aa0b578933acf4a8e05d3/.harnessdesk/flows/fix-and-review.yml).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: deterministic role transitions do not themselves own S3 discretion, and a reviewer/judge role is not promoted to S3 merely because it controls one workflow edge.

### S3 mode matrix

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base `C` | Flow author/developer/configuration; deterministic Flow engine enforces | a manually started Room Flow sees a round outcome/current run state | frozen roles, permissions and guarded transition rules open the next current-control round or person step | [`docs/flows.md`](https://github.com/HarnessDesk/HarnessDesk/blob/24add77185eebe321b0aa0b578933acf4a8e05d3/docs/flows.md), shipped `fix-and-review.yml` |
| Parent `P` | human Room referee | current Board/Room state needs assignment, movement, intervention or an irreversible step | human decision enters Board/Room/person-role state and changes subsequent agent work | [`docs/multi-agent.md`](https://github.com/HarnessDesk/HarnessDesk/blob/24add77185eebe321b0aa0b578933acf4a8e05d3/docs/multi-agent.md), [`docs/flows.md`](https://github.com/HarnessDesk/HarnessDesk/blob/24add77185eebe321b0aa0b578933acf4a8e05d3/docs/flows.md) |

## S3* — Complementary audit

- State: A
- Function: challenge an implementation cell's ordinary completion claim through independent autonomous review of primary operational artifacts and return findings into corrective work.
- Claim being audited: that the fixer's published change is correct and suitable to proceed, rather than merely reported complete by its author.
- Ordinary reporting path: fixer completes/publishes its own card, note and context package and may state that checks passed.
- Complementary access path: the shipped `fix-and-review` Flow opens three separate reviewer-agent seats after publication; each reviewer is instructed to inspect the pull-request diff and surrounding code independently and explicitly not read the other reviewers' answers.
- Audit owner: the autonomous reviewer agents own the substantive `approve` versus `request-changes` judgment from their independent inspection. HarnessDesk's Flow engine only collects declared outcomes and applies the guarded return rule.
- Findings enter subsequent control: any `request-changes` outcome opens a new fixer round carrying every reviewer's findings; the fixer must answer them and republish before another independent review round. Only unanimous reviewer approval advances to the parent human merge step.
- Decisive decision or feedback right: decide, from independent artifact inspection, whether the implementation claim withstands review and what concrete defects require correction.
- Supporting / enforcement mechanisms: isolated reviewer roles/seats, role-addressed cards, outcome validation, context packages, Flow rules, separately observed Board evidence for checks/diffs/PR/CI, commit-bound freshness and stale-evidence downgrading.
- Closure path: fixer publishes → independent reviewers inspect raw diff/code → reviewer judgments return as machine-readable outcomes/findings → any negative finding reopens fixer work → corrected publication is independently reviewed again.
- Boundary reachability: `fix-and-review.yml` is committed in the frozen repository as a runnable HarnessDesk Flow, and the product's Agent/seat/Flow machinery opens the autonomous reviewer seats in standard local operation.
- Why this is / is not agent-owned: removing the reviewer agents while keeping Flow transitions and deterministic evidence storage leaves no actor making the independent semantic judgment over the change. Conversely, check/CI freshness is supporting ground truth and does not replace reviewer ownership of this S3* judgment.
- Evidence: [`.harnessdesk/flows/fix-and-review.yml`](https://github.com/HarnessDesk/HarnessDesk/blob/24add77185eebe321b0aa0b578933acf4a8e05d3/.harnessdesk/flows/fix-and-review.yml); [`docs/flows.md`](https://github.com/HarnessDesk/HarnessDesk/blob/24add77185eebe321b0aa0b578933acf4a8e05d3/docs/flows.md); [`docs/multi-agent.md`](https://github.com/HarnessDesk/HarnessDesk/blob/24add77185eebe321b0aa0b578933acf4a8e05d3/docs/multi-agent.md); [`docs/agents.md`](https://github.com/HarnessDesk/HarnessDesk/blob/24add77185eebe321b0aa0b578933acf4a8e05d3/docs/agents.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: not every HarnessDesk run enables this audit mode. The positive state is a supported first-party Flow mode, not a claim that every ordinary Room automatically audits every S1 result.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party external-and-prospective adaptation loop is established in the reviewed standard distribution.
- Disturbance / variety regulated: potential future changes in models, runtimes, user needs, CI events, schedules, hosted execution and tool capabilities were inspected.
- Decisive decision or feedback right: none established that turns sensed external/future distinctions into adaptation options and returns an adaptation choice into current HarnessDesk capability.
- Decision owner: none established for S4 at the selected deployed boundary.
- Supporting / enforcement mechanisms: runtime capability negotiation, local runtime/version discovery, usage dashboards, repository VISION/roadmap documents and current Flow/Room state.
- Closure path: no supported outside-and-then adaptation decision-and-return loop exists at the frozen ref.
- Why this is / is not agent-owned: current capability discovery and runtime selection react to present machine state; they do not model a future environment and develop adaptation options. Public roadmap/market reasoning is adjacent development governance rather than deployed S4 ownership.
- Evidence: [`docs/architecture.md`](https://github.com/HarnessDesk/HarnessDesk/blob/24add77185eebe321b0aa0b578933acf4a8e05d3/docs/architecture.md); [`VISION.md`](https://github.com/HarnessDesk/HarnessDesk/blob/24add77185eebe321b0aa0b578933acf4a8e05d3/VISION.md); [`docs/data-boundaries.md`](https://github.com/HarnessDesk/HarnessDesk/blob/24add77185eebe321b0aa0b578933acf4a8e05d3/docs/data-boundaries.md); [`docs/flows.md`](https://github.com/HarnessDesk/HarnessDesk/blob/24add77185eebe321b0aa0b578933acf4a8e05d3/docs/flows.md).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: the vision explicitly anticipates PR/CI/timer/webhook-triggered and hosted work, but current Flow triggers are manual and those future lanes are not current operating evidence.

### Absence scope

- Surfaces inspected: README; architecture/runtime capability negotiation; Agent inventory/seating; usage/cost views; Room/Board/Flow state; VISION; data-boundary policy; current Flow triggers and declared future lanes.
- Plausible first-party paths checked: runtime/model capability sensing as adaptation; automatic version selection; usage/limit sensing; future hosted/event-trigger lanes; roadmap/market intelligence; Flow evolution from observed outcomes.
- Why no material first-party path remains: shipped mechanisms select among current available capabilities or expose present state. Future external/event lanes are explicitly not built, and maintainer roadmap/vision activity lies outside the deployed system boundary. No prospective environmental model produces adaptation options that feed back into current capability.

## S5 — Policy and identity

- State: —
- Function: no material runtime identity/ultimate-policy closure is established for the selected HarnessDesk project/room organization.
- Disturbance / variety regulated: possible tension over ultimate organizational purpose, identity, trust boundary or policy that would need legitimate highest-level closure was inspected.
- Decisive decision or feedback right: none established beyond ordinary permission ceilings, approvals, Flow policy, local data settings and current-control decisions.
- Decision owner: none established for S5 at the reviewed deployed boundary.
- Supporting / enforcement mechanisms: Agent briefs/permission ceilings, common approval policy, plugin permission gates, human referee, Flow files, local-only data defaults, VISION promises and configuration/settings.
- Closure path: no first-party runtime path was found where an identity/ultimate-policy issue reaches legitimate ultimate authority and the returned decision governs subsequent operation as S5.
- Why this is / is not agent-owned: agents do not own ultimate HarnessDesk identity/policy, but absence of agent ownership does not itself create a parent S5 mode. Ordinary approval, merge, role permission or Flow edit concerns current work/control rather than the identity-level closure required by Profile 0.2.4.
- Evidence: [`docs/agents.md`](https://github.com/HarnessDesk/HarnessDesk/blob/24add77185eebe321b0aa0b578933acf4a8e05d3/docs/agents.md); [`docs/flows.md`](https://github.com/HarnessDesk/HarnessDesk/blob/24add77185eebe321b0aa0b578933acf4a8e05d3/docs/flows.md); [`docs/multi-agent.md`](https://github.com/HarnessDesk/HarnessDesk/blob/24add77185eebe321b0aa0b578933acf4a8e05d3/docs/multi-agent.md); [`VISION.md`](https://github.com/HarnessDesk/HarnessDesk/blob/24add77185eebe321b0aa0b578933acf4a8e05d3/VISION.md); [`docs/data-boundaries.md`](https://github.com/HarnessDesk/HarnessDesk/blob/24add77185eebe321b0aa0b578933acf4a8e05d3/docs/data-boundaries.md).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: the public VISION contains strong project-level promises such as vendor neutrality and local-data defaults, but those are maintainer/development governance surfaces. The assessment does not borrow them as a deployed Room's S5 owner without an operational identity-policy escalation/return path.

### Absence scope

- Surfaces inspected: common permission/approval policy; Agent definitions and ceilings; human referee/person roles; Flow policy files; plugin settings; local data-boundary controls; project VISION; audit and operator UI.
- Plausible first-party paths checked: human approval as ultimate authority; Flow author/referee as policy owner; Agent brief/permission as constitution; local/remote data choice as membership policy; maintainer VISION promises as distributed parent governance.
- Why no material first-party path remains: each deployed candidate is either an operational/current-control constraint or ordinary user configuration, while VISION/maintainer promises belong to adjacent product-development governance. No supported runtime path elevates an identity/ultimate-policy issue to legitimate parent authority and returns the decision to govern later Room operation.

## Distributed OSS parent arrangement

Repository maintainers and public contributors are not used to manufacture S3/S4/S5 ownership for a local desk. The positive parent S3 mode is instead first-party and operational: the human using a Room is explicitly its referee and their current-control decisions return through Board/Flow/person-role state. Development-time VISION, issues, PRs and release decisions remain adjacent governance unless a deployed closure path incorporates them.

## Self-hosted and non-human modes

The reviewed product is local/self-hosted. Autonomous S1, S2 and S3* modes can run through locally seated agents while S3 may be supplied either through a developer-authored Flow constructor or through the local human referee. No supported non-human autonomous S3 owner or S5 ultimate authority is established. Hosted/shared-server modes are future work and excluded.

## Recursion

HarnessDesk deliberately separates the desk-level organization from the internal organization of each worker runtime. At the assessed recursion, a Codex/Claude/Cursor/Gemini conversation is an operational cell contributing software outcomes. Lower-recursion subagents and model/tool loops remain inside those external runtimes unless explicitly surfaced. Room-level S2/S3/S3* claims are therefore based on HarnessDesk's own shared control relations rather than on hidden worker internals.

## Variety and escalation

HarnessDesk attenuates operational variety with typed capability negotiation, role/permission ceilings, atomic file ownership, worktree isolation, guarded Flow outcomes and message-loop controls. It amplifies regulatory capacity through a common Board, attributed Channel, context packages, shared tools and independently observed evidence. Stale or absent evidence is preserved as uncertainty rather than silently collapsed into success.

Exceptions remain differentiated by function. File/task conflicts are S2 feedback. Whole-Room allocation/intervention belongs to S3 and may reach the human referee. Independent reviewer findings are S3* and return to the fixer. A stopped agent or `Needs you` card transports exceptional state but does not itself establish S4 or S5.

## Evidence gaps

No material evidence gap prevents publication of the six states at the frozen revision. The main classification boundary is S3: the deterministic Flow engine is credited as a function-specific constructor because the developer authors the current-control policy, while the separately supported ordinary Room supplies a parent-human referee closure; neither is upgraded to autonomous S3 ownership. S3* is limited to the shipped independent-review Flow mode and does not imply that generic checks or every Room are autonomous auditors.
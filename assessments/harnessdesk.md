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

- System in focus: one local HarnessDesk engineering desk at project/Room recursion: host process, shared conversation/history/policy state, project workspaces/worktrees, Agent definitions and seating, Room/Board/Channel, Flow engine, handoff/race machinery, common plugin/tool projection, runtime adapters, permissions/approvals, audit/cost/evidence surfaces and supported HarnessDesk-seated coding-agent conversations.
- Purpose and identity: vendor-neutral coding-agent control plane in which replaceable autonomous workers perform software work under shared context, coordination, policy, history, cost and evidence while HarnessDesk itself does not become the coding worker.
- Relevant environment: parent developer/operator; repositories, branches, pull requests and CI; local checks; vendor coding-agent runtimes/model services; plugins/tools; filesystem/process/browser/mobile-test environments and forge APIs.
- Operational units: supported autonomous coding-agent conversations or standing HarnessDesk Agent seats that directly perform engineering work. Room and Flow machinery organize those cells without importing the external runtime's internal organization.
- Standard-distribution boundary: frozen local desktop/host product, Agent/seat layer, Codex/ACP adapters, Room/Board/Channel, worktree and claim machinery, Flow engine and shipped flows, permission/approval surface, plugin/tool gateway, local evidence/audit/usage/history state and operator surfaces.
- Credited operating / distribution surfaces: `README.md`; `docs/architecture.md`; `docs/agents.md`; `docs/multi-agent.md`; `docs/flows.md`; `.harnessdesk/flows/fix-and-review.yml`; `.harnessdesk/flows/race.yml`; current local check/diff/PR/CI evidence and host control paths described by those frozen artifacts.
- Adjacent first-party surfaces excluded from ownership: repository-development contributors/maintainers; CI/release used to develop HarnessDesk; tests/demos as test actors; future hosted/account/event-trigger/routine/jury/landing-queue roadmap surfaces; public VISION governance as product-development governance; implementation internals of Codex, Claude Code, Cursor, Gemini and other external runtimes.
- First-party operating / deployment modes considered: local desktop/headless host; solo and Room operation; manually started Flow operation; built-in/project Agent seating; Codex/ACP-backed sessions; managed worktrees and `/race`; locally observed check/diff/PR/CI evidence. Future hosted and event-triggered modes are excluded.
- Recursion level: one HarnessDesk project/Room organization coordinating several autonomous coding work cells. External runtime subagents/model-tool loops remain lower-recursion external systems unless explicitly surfaced by HarnessDesk.
- Reviewed revision: `24add77185eebe321b0aa0b578933acf4a8e05d3`.
- Observation date: 2026-10-01.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

HarnessDesk drives coding agents it does not own. The host normalizes sessions, transcripts, approvals, worktrees, team coordination, usage and evidence above a vendor-specific agent plane. Codex uses a native adapter; other agents use ACP. Agent command execution remains inside the selected external runtime.

First-party Agent definitions supply durable roles, briefs, outcome vocabularies, permission ceilings and preferred seats. Rooms add shared Board, Channel and roster. Board claims atomically reject overlap and unfinished dependencies, claims carry leases, and worktrees can isolate competitors. Flows add a statechart over Rooms: roles, seats, permissions, outcomes and guarded transitions are frozen for a run. The repository ships runnable `fix-and-review` and `race` flows.

HarnessDesk also records facts it observes independently of agent prose. A card reaches Ready only from fresh check/diff/PR/CI evidence; facts are bound to commits, stale facts lose green status, and restored evidence cannot establish readiness until re-observed.

## Operational model

At this recursion, seated coding-agent conversations are S1 cells. HarnessDesk supplies common context, tools, policy and coordination but not their open-ended implementation judgment. Coordination is partly distributed: agents claim/release work and respond to conflict feedback while the host enforces exclusion, worktree separation and message limits. Whole-Room current control is separately available through a human referee, while Flow files encode that referee's policy as a deterministic constructor. Shipped independent reviewer flows provide complementary audit.

## S1 — Operations

- State: A
- Function: perform repository-facing engineering work as a HarnessDesk-seated autonomous coding-agent cell and return changed artifacts, outcomes and evidence into the desk.
- Disturbance / variety regulated: task-specific repository state, implementation alternatives, tool/test feedback, runtime capability differences, blockers and evidence encountered while producing a software outcome.
- Decisive decision or feedback right: choose and revise the next task-specific coding, inspection or tool action from the objective and returned environment state.
- Decision owner: the supported autonomous coding-agent session seated through HarnessDesk, including a first-party Agent role instantiated on a compatible Codex/ACP runtime.
- Supporting / enforcement mechanisms: Agent briefs/seating, adapter negotiation, transcripts, plugin tools, approvals/permission ceilings, worktrees, task/context state and host persistence.
- Closure path: task enters seated conversation → agent inspects/acts through its runtime → repository/tool feedback returns → same agent revises, continues or completes → HarnessDesk persists outcome/context/evidence.
- Boundary reachability: Agent definitions, seating, adapters, Room membership and tool projection ship in the standard distribution; no application-authored orchestration is required to instantiate the supported worker cell.
- Why this is / is not agent-owned: removing the autonomous worker while leaving host state, worktrees, board and adapters leaves enforcement/persistence but no actor making the open-ended engineering decisions.
- Evidence: [`README.md`](https://github.com/HarnessDesk/HarnessDesk/blob/24add77185eebe321b0aa0b578933acf4a8e05d3/README.md); [`docs/architecture.md`](https://github.com/HarnessDesk/HarnessDesk/blob/24add77185eebe321b0aa0b578933acf4a8e05d3/docs/architecture.md); [`docs/agents.md`](https://github.com/HarnessDesk/HarnessDesk/blob/24add77185eebe321b0aa0b578933acf4a8e05d3/docs/agents.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: internal delegation/planning/memory of Codex, Claude, Cursor, Gemini or other external runtimes is not inherited.

## S2 — Coordination

- State: A
- Function: attenuate destructive interference among concurrent coding cells sharing tasks/files and prevent recursive peer-message chatter from destabilizing the Room.
- Disturbance / variety regulated: overlapping edits or claims on the same task/path, unsafe concurrent work over shared repository state, and uncontrolled reciprocal agent messaging.
- Distinct S1 units: two or more independently running HarnessDesk-seated coding-agent conversations in one Room/project, potentially on different vendor runtimes.
- Inter-S1 disturbance: two cells can attempt the same card or overlapping files, or wake one another repeatedly through peer messages.
- Attenuating coordination relation: atomic Board claims reject held intents, unfinished dependencies and overlapping file globs; leases expose stranded claims; worktrees isolate races; Channel delivery is attributed, rate/duplicate/queue limited and awakened replies are not forwarded back automatically.
- Feedback into subsequent S1 behaviour: conflict/refusal/claim results are returned to the requesting agent, which chooses another task/path, waits, releases, communicates, uses isolation or escalates; dependency context is returned to later claimants.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the implementation targets concrete inter-worker collision modes—file/task contention and message oscillation—and closes explicit refusal/return paths that change later worker behaviour.
- Decisive decision or feedback right: after host conflict feedback, autonomous participating agents choose the mutual-adjustment response; the host deterministically enforces exclusion and loop constraints.
- Decision owner: participating autonomous coding-agent cells.
- Supporting / enforcement mechanisms: Board transactions, file-glob conflict checks, leases, worktrees, dependency gating, delivery states, loop guards, context packages and host audit state.
- Closure path: agents claim intended work → host accepts or rejects incompatible ownership → result returns to agent → agent changes work/communication or proceeds → release/completion changes the shared state seen by peers.
- Boundary reachability: Board/team tools are projected to supported Codex and ACP agents; host caller correlation rejects unattributed calls, so the coordination loop is available without custom external glue.
- Why this is / is not agent-owned: deterministic exclusion could still block a conflict without the agent, but it would not choose the organizational response to that conflict. That discretion is held by the autonomous participant.
- Evidence: [`docs/multi-agent.md`](https://github.com/HarnessDesk/HarnessDesk/blob/24add77185eebe321b0aa0b578933acf4a8e05d3/docs/multi-agent.md); [`docs/architecture.md`](https://github.com/HarnessDesk/HarnessDesk/blob/24add77185eebe321b0aa0b578933acf4a8e05d3/docs/architecture.md); [`README.md`](https://github.com/HarnessDesk/HarnessDesk/blob/24add77185eebe321b0aa0b578933acf4a8e05d3/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: claim enforcement regulates supported Board/worktree participants, not unrelated out-of-band processes.

## S3 — Inside-and-now control

- State: C(P)
- Function: regulate the current Room as a whole by choosing roles/permissions, moving current work between cells, reacting to round outcomes and reserving irreversible steps for a selected authority.
- Disturbance / variety regulated: current mismatch among work cells—who should perform which role, whether rejected work returns to implementation, what a seat may publish/merge, and when current work must stop, change owner or reach a person.
- Whole-system current view: Room Board/roster/channel and Flow run expose current members, claims, role-addressed cards, outcomes and run state across the participating S1 cells.
- Current-control decision scope: whole-Room allocation, role/permission assignment, guarded transitions between current work rounds, intervention on blocked/rejected work and ownership of irreversible merge-like actions.
- Decisive decision or feedback right: select/revise those current roles, commitments and transitions on behalf of the Room rather than merely execute one local task.
- Decision owner: base constructor mode—developer/Flow author chooses the policy and deterministic Flow engine enforces it; parent mode—human Room referee owns current assignment/intervention/irreversible-step choices.
- Supporting / enforcement mechanisms: Flow parser/validator, role seating, permission ceilings, outcome vocabulary, guarded first-match transitions, frozen run policy, Board state, person-role cards and stop/restart semantics.
- Closure path: Room/round state reaches predeclared Flow policy or human referee → current-control decision selects next role/card/permission/intervention → Flow/Board machinery changes subsequent S1 work.
- Boundary reachability: Flow is a supported first-party project format with runnable shipped examples; ordinary Rooms expose the human referee path directly in the local standard distribution.
- Why this is / is not agent-owned: the Flow engine enforces a preselected whole-Room policy but does not autonomously choose/revise that policy from current variety; ordinary Room documentation explicitly assigns the referee right to the human. No autonomous S3 supervisor is established.
- Evidence: [`docs/flows.md`](https://github.com/HarnessDesk/HarnessDesk/blob/24add77185eebe321b0aa0b578933acf4a8e05d3/docs/flows.md); [`docs/multi-agent.md`](https://github.com/HarnessDesk/HarnessDesk/blob/24add77185eebe321b0aa0b578933acf4a8e05d3/docs/multi-agent.md); [`.harnessdesk/flows/fix-and-review.yml`](https://github.com/HarnessDesk/HarnessDesk/blob/24add77185eebe321b0aa0b578933acf4a8e05d3/.harnessdesk/flows/fix-and-review.yml).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: deterministic transitions do not own S3 discretion, and a reviewer/judge is not promoted to S3 merely because it controls one edge.

### S3 mode matrix

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | Flow author/developer/configuration; deterministic Flow engine enforces | manually started Flow sees current round outcome/run state | frozen roles, permissions and guarded transitions open the next current-control round or person step | `docs/flows.md`; shipped `fix-and-review.yml` |
| Parent (`P`) | human Room referee | current Room/Board state requires allocation, movement, intervention or irreversible action | human decision enters Board/Room/person-role state and changes subsequent agent work | `docs/multi-agent.md`; `docs/flows.md` |

## S3* — Complementary audit

- State: A
- Function: challenge an implementation cell's ordinary completion claim through independent autonomous inspection of primary artifacts and return findings into corrective work.
- Disturbance / variety regulated: uncertainty that the fixer's own completion/publication claim corresponds to a correct change rather than merely a plausible self-report.
- Claim being audited: that a published fixer change is correct and suitable to proceed.
- Ordinary reporting path: fixer publishes its own card, note/context and may report checks or success.
- Complementary access path: shipped `fix-and-review` opens three separate reviewer-agent seats; each is ordered to inspect the pull-request diff and surrounding code independently and not read other reviewers' answers.
- Independence boundary: reviewers are distinct autonomous seats from the fixer, receive the produced change rather than the fixer's hidden reasoning, and are explicitly isolated from one another's judgments for the review round.
- Who acts on findings: the Flow returns any `request-changes` findings to the fixer, which must answer them and republish; unanimous approval alone advances to the human merge step.
- Decisive decision or feedback right: judge from independent artifact inspection whether the implementation claim withstands review and identify defects requiring correction.
- Decision owner: the autonomous reviewer agents own `approve` versus `request-changes`; the deterministic engine only validates/collects outcomes and applies the return rule.
- Supporting / enforcement mechanisms: reviewer role seating, addressed cards, outcome validation, context packages, Flow rules, check/diff/PR/CI evidence, commit-bound freshness and stale-evidence downgrading.
- Closure path: fixer publishes → independent reviewers inspect raw artifacts → judgments/findings return → any negative finding reopens fixer work → corrected publication is reviewed again.
- Boundary reachability: `fix-and-review.yml` is committed as a runnable HarnessDesk Flow and standard Agent/seat/Flow machinery opens the reviewer actors locally.
- Why this is / is not agent-owned: removing reviewer agents while retaining deterministic Flow/evidence machinery leaves no actor making the independent semantic judgment; check/CI facts support rather than replace that judgment.
- Evidence: [`.harnessdesk/flows/fix-and-review.yml`](https://github.com/HarnessDesk/HarnessDesk/blob/24add77185eebe321b0aa0b578933acf4a8e05d3/.harnessdesk/flows/fix-and-review.yml); [`docs/flows.md`](https://github.com/HarnessDesk/HarnessDesk/blob/24add77185eebe321b0aa0b578933acf4a8e05d3/docs/flows.md); [`docs/multi-agent.md`](https://github.com/HarnessDesk/HarnessDesk/blob/24add77185eebe321b0aa0b578933acf4a8e05d3/docs/multi-agent.md); [`docs/agents.md`](https://github.com/HarnessDesk/HarnessDesk/blob/24add77185eebe321b0aa0b578933acf4a8e05d3/docs/agents.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: this is a supported Flow mode, not a claim that every ordinary Room automatically audits every S1 result.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party external-and-prospective adaptation loop is established in the reviewed standard distribution.
- Disturbance / variety regulated: possible future changes in models, runtimes, user needs, CI events, schedules, hosted execution and tool capabilities were inspected.
- Decisive decision or feedback right: none established that turns sensed external/future distinctions into adaptation options and returns an adaptation choice into current HarnessDesk capability.
- Decision owner: none established for S4 at the deployed boundary.
- Supporting / enforcement mechanisms: runtime capability negotiation, local runtime/version discovery, usage dashboards, repository VISION/roadmap and current Flow/Room state.
- Closure path: no supported outside-and-then adaptation decision-and-return loop exists at the frozen ref.
- Why this is / is not agent-owned: current capability discovery and runtime selection react to present machine state; they do not model a future environment and develop adaptation options. Roadmap/market reasoning is adjacent development governance.
- Evidence: [`docs/architecture.md`](https://github.com/HarnessDesk/HarnessDesk/blob/24add77185eebe321b0aa0b578933acf4a8e05d3/docs/architecture.md); [`VISION.md`](https://github.com/HarnessDesk/HarnessDesk/blob/24add77185eebe321b0aa0b578933acf4a8e05d3/VISION.md); [`docs/data-boundaries.md`](https://github.com/HarnessDesk/HarnessDesk/blob/24add77185eebe321b0aa0b578933acf4a8e05d3/docs/data-boundaries.md); [`docs/flows.md`](https://github.com/HarnessDesk/HarnessDesk/blob/24add77185eebe321b0aa0b578933acf4a8e05d3/docs/flows.md).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: PR/CI/timer/webhook-triggered and hosted work are named as future directions, but current Flow triggers are manual and those lanes are not built.

### Absence scope

- Surfaces inspected: architecture/runtime negotiation; Agent inventory/seating; usage/cost; Room/Board/Flow state; VISION; data-boundary policy; current Flow triggers and declared future lanes.
- Plausible first-party paths checked: runtime/model sensing as adaptation; automatic version selection; usage/limit sensing; future hosted/event triggers; roadmap/market intelligence; Flow evolution from observed outcomes.
- Why no material first-party path remains: shipped mechanisms select among current available capabilities or expose present state. Future external/event lanes are explicitly unbuilt and maintainer roadmap activity lies outside the deployed boundary.

## S5 — Policy and identity

- State: —
- Function: no material runtime identity/ultimate-policy closure is established for the selected HarnessDesk project/Room organization.
- Disturbance / variety regulated: possible tension over ultimate organizational purpose, identity, trust boundary or policy requiring highest-level closure was inspected.
- Decisive decision or feedback right: none established beyond ordinary permission ceilings, approvals, Flow policy, local data settings and current-control decisions.
- Decision owner: none established for S5 at the reviewed deployed boundary.
- Supporting / enforcement mechanisms: Agent briefs/permission ceilings, common approval policy, plugin permission gates, human referee, Flow files, local-only data defaults, VISION promises and settings.
- Closure path: no first-party runtime path was found where an identity/ultimate-policy issue reaches legitimate ultimate authority and the returned decision governs subsequent operation as S5.
- Why this is / is not agent-owned: agents do not own ultimate HarnessDesk identity/policy, but absence of agent ownership does not create parent S5; ordinary approval, merge, role permission and Flow edit remain operational/current-control matters.
- Evidence: [`docs/agents.md`](https://github.com/HarnessDesk/HarnessDesk/blob/24add77185eebe321b0aa0b578933acf4a8e05d3/docs/agents.md); [`docs/flows.md`](https://github.com/HarnessDesk/HarnessDesk/blob/24add77185eebe321b0aa0b578933acf4a8e05d3/docs/flows.md); [`docs/multi-agent.md`](https://github.com/HarnessDesk/HarnessDesk/blob/24add77185eebe321b0aa0b578933acf4a8e05d3/docs/multi-agent.md); [`VISION.md`](https://github.com/HarnessDesk/HarnessDesk/blob/24add77185eebe321b0aa0b578933acf4a8e05d3/VISION.md); [`docs/data-boundaries.md`](https://github.com/HarnessDesk/HarnessDesk/blob/24add77185eebe321b0aa0b578933acf4a8e05d3/docs/data-boundaries.md).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: public promises such as vendor neutrality/local-data defaults are maintainer/development governance surfaces and are not borrowed as a deployed Room's S5 owner.

### Absence scope

- Surfaces inspected: common permission/approval policy; Agent definitions; human referee/person roles; Flow files; plugin settings; local data-boundary controls; VISION; audit and operator UI.
- Plausible first-party paths checked: human approval as ultimate authority; Flow author/referee as policy owner; Agent brief as constitution; data-boundary choice as membership policy; maintainer VISION as distributed parent governance.
- Why no material first-party path remains: deployed candidates are operational/current-control constraints or user configuration, while VISION/maintainer promises belong to adjacent product-development governance. No supported runtime identity-policy escalation/return path remains.

## Distributed OSS parent arrangement

Public maintainers are not used to manufacture deployed S3/S4/S5 ownership. The positive parent S3 mode is operationally local: the Room's human referee owns current-control decisions and returns them through Board/Flow/person-role state. Repository governance remains adjacent unless the deployed system incorporates it.

## Self-hosted and non-human modes

The reviewed product is local/self-hosted. Autonomous S1, S2 and S3* modes can run through locally seated agents; S3 is available through a developer-authored constructor and a separate human-referee parent mode. No autonomous whole-system S3 owner or S5 ultimate authority is established. Hosted/shared-server modes are excluded as future work.

## Recursion

At this recursion, Codex/Claude/Cursor/Gemini conversations are operational cells contributing software outcomes. Their lower-recursion planners, subagents and model-tool loops remain external. Room-level S2/S3/S3* mappings therefore rest on HarnessDesk's own shared relations rather than hidden worker internals.

## Variety and escalation

HarnessDesk attenuates variety through capability negotiation, permission ceilings, atomic file ownership, worktree isolation, guarded Flow outcomes and message-loop controls. It amplifies regulation through a common Board, attributed Channel, context packages, shared tools and independently observed evidence. File/task conflicts are S2; whole-Room allocation/intervention is S3; independent reviewer findings are S3* and return to the fixer. `Needs you` transports exceptional state but does not by itself establish S4 or S5.

## Evidence gaps

No material evidence gap prevents publication. The principal boundary is S3: Flow is a function-specific constructor because the developer authors current-control policy, while ordinary Room supplies a separate parent-human referee closure; neither becomes autonomous S3 ownership. S3* is limited to the shipped independent-review Flow mode and does not promote generic checks or every Room into autonomous audit.
---
harness_id: fleet
project_name: Fleet
repository: https://github.com/sbluemin/fleet-harness
review_ref: 2d763d6f2ea831b19c6cbbcf345ace054348105d
reviewed_at: 2026-11-17
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: P
---

# Fleet

## Review boundary

- System in focus: Fleet's public local Console operating organization of standing Commodore agents, per-objective Commander/member sessions, Objective board and Fleet AI Gateway at frozen default branch `canary`.
- Purpose and identity: Provide one owner-operated workspace for teams of coding agents, with persistent objectives, mission dependencies, supervisor wakeups, role access, model assignment, shared status and human escalation.
- Environment: Human requests, code repositories, gateway-selected external model providers, installed Claude Code runtime, generated implementation/review evidence, approvals and persistent local Console sessions.
- Standard-distribution boundary: First-party `runtime/fleet-console` feature and foundation APIs, shipped `commodore`, `objectives`, `execution` and `ai-gateway` integrations; external Claude Code/other model software is a supported dependency and not assumed to own Fleet-level organizational policy.
- Credited operating / distribution surfaces: Fleet Console host service, `CommodoreSession` model-backed loop via Agent SDK, Objective launch/Commander/member sessions, role-gated MCP objective board, per-Objective mission graph, model routing, review/status and approval core for changing a standing Commodore charter.
- Adjacent first-party surfaces excluded from ownership: Docs/skills/README showcase screenshots, local dev E2E harness, front-end UI, release scripts and project contributor governance; these can corroborate entry points, not create an agent-owned decision.
- First-party operating / deployment modes considered: Console-configured Commodore with connected Claude Code; active Objective with Commander and delegated members; optional TaskForce multi-Commodore room; parent human decision on enduring Commodore description and criteria; local/personal modes only.
- Recursion level: One Fleet Console, with standing Commodore as current-control unit of multiple Objective teams, and Commander/member task S1 sub-units; arbitrary unrelated Claude Code sessions are outside the declared Fleet organization.
- Reviewed revision: `2d763d6f2ea831b19c6cbbcf345ace054348105d` (`canary`, current source default branch).
- Observation date: 2026-11-17.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

First-party Fleet Console exposes model-backed Commodore agent sessions through an Agent SDK integration running against an installed Claude Code runtime and model gateway. A persistent Commodore has its own host record, prompt, optional routines and taskforce conversations; it can read/write selected Objective and Commodore tools. An Objective launches a Commander with scoped board tools and model-backed member sessions, whose mission outputs return via events and board updates. The mission graph encodes prerequisites, rejects cycles, prevents unplaced mission admission and maintains a single authoritative board owner/role-scoped write surface. The supervisor detects outstanding review, stalled roles, quiet member reports and pending human decisions and wakes the standing Commodore. The AI Gateway determines concrete provider model assignments from enabled models and live quota; its selection and policy enforcement are not credited as autonomous governance by themselves.

First-party source: [session.ts](https://github.com/sbluemin/fleet-harness/blob/2d763d6f2ea831b19c6cbbcf345ace054348105d/runtime/fleet-console/features/commodore/host/session.ts), [supervisor.ts](https://github.com/sbluemin/fleet-harness/blob/2d763d6f2ea831b19c6cbbcf345ace054348105d/runtime/fleet-console/features/commodore/host/supervisor.ts), [objective-tools.ts](https://github.com/sbluemin/fleet-harness/blob/2d763d6f2ea831b19c6cbbcf345ace054348105d/runtime/fleet-console/features/objectives/host/objective-tools.ts), [store.ts](https://github.com/sbluemin/fleet-harness/blob/2d763d6f2ea831b19c6cbbcf345ace054348105d/runtime/fleet-console/features/objectives/host/store.ts), [types.ts](https://github.com/sbluemin/fleet-harness/blob/2d763d6f2ea831b19c6cbbcf345ace054348105d/runtime/fleet-console/features/objectives/shared/types.ts), [launch.ts](https://github.com/sbluemin/fleet-harness/blob/2d763d6f2ea831b19c6cbbcf345ace054348105d/runtime/fleet-console/features/objectives/host/launch.ts), [description-proposals.ts](https://github.com/sbluemin/fleet-harness/blob/2d763d6f2ea831b19c6cbbcf345ace054348105d/runtime/fleet-console/features/commodore/host/description-proposals.ts), [execution-routing.ts](https://github.com/sbluemin/fleet-harness/blob/2d763d6f2ea831b19c6cbbcf345ace054348105d/runtime/fleet-console/features/ai-gateway/runtime/src/fleet/execution-routing.ts), [console-agent-sdk.md](https://github.com/sbluemin/fleet-harness/blob/2d763d6f2ea831b19c6cbbcf345ace054348105d/docs/console-agent-sdk.md).

## S1 — Operations
- State: A
- Function: Execute owner-assigned coding objectives and missions through model-backed Commodore, Commander and member agent sessions.
- Disturbance / variety regulated: Project requirements, code/tool output, reviews, model responses and new tasks during objective execution.
- Decisive decision or feedback right: A model-backed Commander/member chooses tool calls, source changes, review content or mission next actions within scoped tools; Commodore can also perform agent turns.
- Decision owner: Configured Claude Code Agent SDK sessions created by first-party CommodoreSession and Objective launch with model provider dependency.
- Supporting / enforcement mechanisms: ConsoleResidentAgentHost, per-role SDK sessions, objective/mission MCP tools, local session logs and Fleet AI Gateway.
- Closure path: An agent session yields tool results, updates mission cards/evidence and sends completion to Commander/Commodore; the next objective event/wake can change work.
- Boundary reachability: Requires configured/installed Claude Code and models; no live external provider call or package test was performed here.
- Why this is / is not agent-owned: Commodore sessions are actually constructed at host runtime, and Objective launch implements Commander/member execution; models/Claude Code are external but invoked through a shipped first-party product mode.
- Evidence: Model-conditioned choice of coding/tool actions exists in supported deployment; deterministic runtime wiring alone is not mistaken for agent autonomy.
- Basis: [session.ts](https://github.com/sbluemin/fleet-harness/blob/2d763d6f2ea831b19c6cbbcf345ace054348105d/runtime/fleet-console/features/commodore/host/session.ts), [launch.ts](https://github.com/sbluemin/fleet-harness/blob/2d763d6f2ea831b19c6cbbcf345ace054348105d/runtime/fleet-console/features/objectives/host/launch.ts), [objective-tools.ts](https://github.com/sbluemin/fleet-harness/blob/2d763d6f2ea831b19c6cbbcf345ace054348105d/runtime/fleet-console/features/objectives/host/objective-tools.ts), [console-agent-sdk.md](https://github.com/sbluemin/fleet-harness/blob/2d763d6f2ea831b19c6cbbcf345ace054348105d/docs/console-agent-sdk.md)
- Confidence: source-level first-party runtime tracing
- Caveats: high for supported agent mode


## S2 — Coordination
- State: C
- Function: Prevent specific incompatible work/board commitments among distinct subordinate Objective mission agents.
- Disturbance / variety regulated: Parallel members can attempt to update shared Objective authority or begin a mission before its dependent predecessor has delivered the required work; unplaced missions and dependency cycles can deadlock/conflict.
- Decisive decision or feedback right: Decide board-write admission for role-identified callers, whether a mission is ready, and whether mission graph edits are admissible; signal changed board to subsequent agents.
- Decision owner: First-party deterministic ObjectiveStore, missionReady/wouldCycle graph and roleIn MCP guard; Commander/owner configures mission dependency and member allocations.
- Supporting / enforcement mechanisms: Scoped `fleet-commander` vs `fleet-member` tools, server-side caller-derived Objective identity, mission prerequisite graph, unplaced flag and cycle protection.
- Closure path: Member action stays within assigned role; a dependent mission remains blocked until predecessor `done`; authorized Commander changes the shared board, wakes downstream sessions with updated readiness or refusal.
- Boundary reachability: No claim that Fleet's role graph negotiates arbitrary semantic conflicts or resolves simultaneous git edits in independent repositories.
- Why this is / is not agent-owned: Shipped `objective-tools.ts` gates writer rights by caller-role and the graph's first-party `missionReady`/cycle checks are applied to the board/launch; Console session events then expose changed mission state to members.
- Evidence: This is bounded to concrete shared-board authority and dependent mission readiness interference, not generic chat, speaker selection, TaskForce conversation or raw queue sequencing.
- Basis: [objective-tools.ts](https://github.com/sbluemin/fleet-harness/blob/2d763d6f2ea831b19c6cbbcf345ace054348105d/runtime/fleet-console/features/objectives/host/objective-tools.ts), [types.ts](https://github.com/sbluemin/fleet-harness/blob/2d763d6f2ea831b19c6cbbcf345ace054348105d/runtime/fleet-console/features/objectives/shared/types.ts), [store.ts](https://github.com/sbluemin/fleet-harness/blob/2d763d6f2ea831b19c6cbbcf345ace054348105d/runtime/fleet-console/features/objectives/host/store.ts), [launch.ts](https://github.com/sbluemin/fleet-harness/blob/2d763d6f2ea831b19c6cbbcf345ace054348105d/runtime/fleet-console/features/objectives/host/launch.ts), [board-state.ts](https://github.com/sbluemin/fleet-harness/blob/2d763d6f2ea831b19c6cbbcf345ace054348105d/runtime/fleet-console/features/objectives/shared/board-state.ts)
- Confidence: explicit code + cross-component structural path
- Caveats: medium
- Distinct S1 units: Separate Commander-led member coding agents working on missions of one Objective, possibly overlapping a shared project/workspace.
- Inter-S1 disturbance: Starting member B against an unfinished prerequisite from member A can consume unready source assumptions; unrestricted members editing common mission criteria/plans would create incompatible commitments.
- Attenuating coordination relation: Commander-only board mutations, member read-only scope, cycle check and explicit `missionReady` guard on mission prerequisites and placement.
- Feedback into subsequent S1 behaviour: A member cannot author board-wide decisions; unready mission is not dispatched; accepted predecessor completion updates board readiness, then the subsequent agent receives new assignment or state.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: These guards resolve concrete write-authority and prerequisite-availability interference on a shared Objective contract rather than merely transmitting agent messages.

## S3 — Inside-and-now control
- State: A
- Function: Standing model-backed Commodore supervises multiple live Objectives/Commander/member teams with authority to intervene on current plans, commitments, criteria and pending reviews.
- Disturbance / variety regulated: Active objective teams may stall, go silent, submit incomplete criteria or require redistribution among assigned members and model capacity.
- Decisive decision or feedback right: Commodore can decide whether to commence objective, approve criteria, continue/request repairs and direct subordinates after reviewing live status; user retains separate holds where expressly required.
- Decision owner: Model-backed standing Commodore agent with shipped board control tools, when configured and running; deterministic supervisor/wake machinery supplies observations.
- Supporting / enforcement mechanisms: Commodore Supervisor, pending/quiet-member notices, Objective board read/update and criteria/review transitions, TaskForce messages and gateway quota exposure.
- Closure path: Supervisor emits a wake event from live board/agent changes; Commodore model session acts via scoped board tools, which persist and trigger new Commander/member work or a human hold/review.
- Boundary reachability: Commodore must be enabled and configured. Human approvals on some steps are not enough by themselves to establish a separate parent S3 mode; no `A(P)` is claimed.
- Why this is / is not agent-owned: The shipped Commodore agent has its own session/prompt and board tool access, and supervisor is a concrete host loop. One configured Commodore controls more than one Objective in its own Theaters, with current taskboard and member status across them.
- Evidence: The model-backed leader's interventions are distinct from hard-coded stall notices or gateway model assignment; the latter are supporting runtime features, not autonomous S3.
- Basis: [session.ts](https://github.com/sbluemin/fleet-harness/blob/2d763d6f2ea831b19c6cbbcf345ace054348105d/runtime/fleet-console/features/commodore/host/session.ts), [supervisor.ts](https://github.com/sbluemin/fleet-harness/blob/2d763d6f2ea831b19c6cbbcf345ace054348105d/runtime/fleet-console/features/commodore/host/supervisor.ts), [tools.ts](https://github.com/sbluemin/fleet-harness/blob/2d763d6f2ea831b19c6cbbcf345ace054348105d/runtime/fleet-console/features/commodore/host/tools.ts), [actions.ts](https://github.com/sbluemin/fleet-harness/blob/2d763d6f2ea831b19c6cbbcf345ace054348105d/runtime/fleet-console/features/objectives/host/actions.ts), [store.ts](https://github.com/sbluemin/fleet-harness/blob/2d763d6f2ea831b19c6cbbcf345ace054348105d/runtime/fleet-console/features/objectives/host/store.ts), [launch.ts](https://github.com/sbluemin/fleet-harness/blob/2d763d6f2ea831b19c6cbbcf345ace054348105d/runtime/fleet-console/features/objectives/host/launch.ts)
- Confidence: source-level current-control path with runtime hooks
- Caveats: medium-high
- Whole-system current view: The standing Commodore receives current Objective/mission readiness, member statuses, review requests and pending human answers across its Theater/Objective scope.
- Current-control decision scope: Commence, redirect, pause/repair and resolve current mission/criteria commitments within the Commander/member organizations it supervises.

## S3* — Complementary audit
- State: ?
- Function: A reviewer member and artifact/evidence views plausibly provide a second inspection path, but independence from operational producers and corrective feedback authority are not fully demonstrated.
- Disturbance / variety regulated: A Commander/member may claim that coding tasks or success criteria were met without verifiable implementation evidence.
- Decisive decision or feedback right: An independent complementary audit role would need separately grounded artifact access, an explicit challenge judgment and subsequent current-control correction.
- Decision owner: A configured reviewer/member can examine work; critical independence relative to the maker and durable return to Commodore S3 is unresolved in this pinned inspection.
- Supporting / enforcement mechanisms: First-party evidence reading/criteria records, optional reviewer member role and objective review/retrospective handling.
- Closure path: Reviewer can report findings to Commander/Objective; it is not established that a distinct sufficiently independent auditor is guaranteed in standard supported mode or that its finding reaches S3 as an independent corrective channel.
- Why this is / is not agent-owned: Adding a model labelled reviewer or ordinary output evidence is not automatically S3*; a real complementary checker must be shown with evidence access and a corrective closure path.
- Evidence: [objective-tools.ts](https://github.com/sbluemin/fleet-harness/blob/2d763d6f2ea831b19c6cbbcf345ace054348105d/runtime/fleet-console/features/objectives/host/objective-tools.ts), [evidence.ts](https://github.com/sbluemin/fleet-harness/blob/2d763d6f2ea831b19c6cbbcf345ace054348105d/runtime/fleet-console/features/objectives/host/evidence.ts), [store.ts](https://github.com/sbluemin/fleet-harness/blob/2d763d6f2ea831b19c6cbbcf345ace054348105d/runtime/fleet-console/features/objectives/host/store.ts), [launch.ts](https://github.com/sbluemin/fleet-harness/blob/2d763d6f2ea831b19c6cbbcf345ace054348105d/runtime/fleet-console/features/objectives/host/launch.ts), [console-agent-sdk.md](https://github.com/sbluemin/fleet-harness/blob/2d763d6f2ea831b19c6cbbcf345ace054348105d/docs/console-agent-sdk.md)
- Basis: specific plausible shipped review path not fully adjudicated
- Confidence: medium-low
- Caveats: Source-pinned targeted review of supported reviewer access/selection and role separation is needed. Do not count ordinary test suite or UI audit logs.


## S4 — Outside-and-then intelligence
- State: ?
- Function: Future role/capability adaptation is plausible through persistent Commodore intel and descriptions, model-loadout choices and routines, but the full external-prospective option-to-capability loop remains unproved.
- Disturbance / variety regulated: Changing external project needs and available provider models may require changing standing Commodore expertise, learned directives or future recurring work.
- Decisive decision or feedback right: Choose a genuinely prospective adaptation based on external information and return an accepted option into future team capability.
- Decision owner: Commodore can propose amendments to its own/another Commodore's persistent descriptions and intel; human approves; gateway can choose available models, but neither establishes full future-environment intelligence independently.
- Supporting / enforcement mechanisms: Commodore intel/description proposals with approval, memory and model quota information and routines.
- Closure path: Approved intel/description updates persist and wake a standing Commodore, yet it is uncertain whether the proposed changes originate from a systematic external-and-then assessment rather than routine user edits or task memory.
- Why this is / is not agent-owned: Neither dynamic model routing nor memory updates alone are S4; this is an explicit existing possible in-boundary adaptive path left unknown pending causal evidence.
- Evidence: [intel-proposals.ts](https://github.com/sbluemin/fleet-harness/blob/2d763d6f2ea831b19c6cbbcf345ace054348105d/runtime/fleet-console/features/commodore/host/intel-proposals.ts), [description-proposals.ts](https://github.com/sbluemin/fleet-harness/blob/2d763d6f2ea831b19c6cbbcf345ace054348105d/runtime/fleet-console/features/commodore/host/description-proposals.ts), [supervisor.ts](https://github.com/sbluemin/fleet-harness/blob/2d763d6f2ea831b19c6cbbcf345ace054348105d/runtime/fleet-console/features/commodore/host/supervisor.ts), [execution-routing.ts](https://github.com/sbluemin/fleet-harness/blob/2d763d6f2ea831b19c6cbbcf345ace054348105d/runtime/fleet-console/features/ai-gateway/runtime/src/fleet/execution-routing.ts), [session.ts](https://github.com/sbluemin/fleet-harness/blob/2d763d6f2ea831b19c6cbbcf345ace054348105d/runtime/fleet-console/features/commodore/host/session.ts)
- Basis: source-first unresolved concrete candidate
- Confidence: medium-low
- Caveats: A concrete environmental signal → future-option proposal → accepted change → later improved capability trace would resolve '?' to positive or bounded absence.


## S5 — Policy and identity
- State: P
- Function: Protect the standing Commodore role charter/identity against unapproved agent-authored changes and return human-approved identity amendments into ongoing operations.
- Disturbance / variety regulated: A standing Commodore changing its own purpose/description could silently redefine its organizational mandate for all future Objectives.
- Decisive decision or feedback right: Approve or reject proposed change to a Commodore's enduring description/mandate, including cross-Commodore identity modification, before it becomes live.
- Decision owner: Human Console owner through first-party ApprovalCore, not Commodore itself; no agent-owned ultimate policy mode established.
- Supporting / enforcement mechanisms: CommodoreDescriptionProposals with pending approval, ApprovalCore decide callback, versioned/store description and wake-on-change; immutable system prompt declares standing role base.
- Closure path: A Commodore-submitted description change remains pending until an owner approval; if approved the stored charter revision increments and target Commodore wakes to act from the new description; rejection preserves prior charter.
- Boundary reachability: S5=P is narrowly the human owner of the standing Commodore identity/mandate; the code-defined base prompt itself remains a shipped default and is not claimed parent-editable in this mode.
- Why this is / is not agent-owned: The shipped description proposal binding has a concrete approval-only application callback and changes the persistent standing identity information read by Commodore agent tooling; not just approval of one mission.
- Evidence: The parent owns the role identity and scope. Objective criterion review and per-tool permission are *not* counted as S5; only enduring Commodore identity/mandate custody is credited.
- Basis: [description-proposals.ts](https://github.com/sbluemin/fleet-harness/blob/2d763d6f2ea831b19c6cbbcf345ace054348105d/runtime/fleet-console/features/commodore/host/description-proposals.ts), [prompt.ts](https://github.com/sbluemin/fleet-harness/blob/2d763d6f2ea831b19c6cbbcf345ace054348105d/runtime/fleet-console/features/commodore/host/prompt.ts), [session.ts](https://github.com/sbluemin/fleet-harness/blob/2d763d6f2ea831b19c6cbbcf345ace054348105d/runtime/fleet-console/features/commodore/host/session.ts), [tools.ts](https://github.com/sbluemin/fleet-harness/blob/2d763d6f2ea831b19c6cbbcf345ace054348105d/runtime/fleet-console/features/commodore/host/tools.ts)
- Confidence: first-party parent approval and return-to-agent source path
- Caveats: medium
- Identity / ultimate-policy issue: A standing Commodore's persistent description sets its remit for the nested Objective teams, unlike one task's acceptance criteria; unilateral rewrite would affect subsequent operational commitments.
- Ultimate authority in each claimed mode: Human owner approving the registered proposal; agent is proposer, not decisive ultimate-policy holder.
- Return-to-operation path: Pending change is approved into store, the target Commodore's description revision changes and it receives a wake; subsequent model turns read the new description and regulate future objectives.

## Recursion

Fleet Console contains standing Commodores with potentially multiple Objective teams. Each objective has a Commander and separate member agent sessions. This functional nesting does not prove full viable organizations at each level. The declared subject is Console's operating organization, not third-party Claude Code development governance or arbitrary user projects.

## Variety and escalation

Operational change originates in user requests and execution/tool results. Objective mission graph suppresses particular conflicting commitments, and persistent Commodore tools close current-control decisions; separate approval requests to a person preserve ultimate role-identity custody. User-controlled model selection and gateway quota routing are execution machinery, not governance. S3* and S4 require distinct positive evidence before upgrading.

## Evidence gaps

- Pinned source inspection only, without executed Fleet end-to-end Console/Claude Code sessions, upstream package test or independent second semantic reviewer.
- S2=C is narrowly mission-graph/shared-board interference, not proof of general multi-agent conflict arbitration. S3=A applies to configured persistent Commodore agent operation, not merely the supervisor scheduler.
- Concrete possible reviewer S3* and prospective intel/description S4 pathways remain `?` because independent corrective access and future/environment selection chains have not been established here.
- S5=P is bounded to the human custodianship of a standing Commodore's role charter; approving work criteria does not imply universal S5 governance.

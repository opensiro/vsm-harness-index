---
harness_id: commons
project_name: Commons
repository: https://github.com/t54-labs/agent-commons
review_ref: 6e911236127dc6cf0d231add87e302974151a7f4
reviewed_at: 2026-10-01
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-01
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: P
---

# Commons

## Review boundary

- System in focus: one enrolled Commons coordination organization at project recursion: the shipped Commons Skill/CLI, scope resolver, local board or private Team Relay, SQLite coordination state, tasks/plans/messages, resource leases and fencing, wrappers/policy checks, audit history and supported Commons-enabled coding-agent sessions insofar as the first-party Skill governs their participation in the coordination loop.
- Purpose and identity: coordinate independently started coding-agent work so agents can discover peers, declare current and next work, avoid conflicting shared-resource side effects, hand off context and leave durable coordination evidence without Commons becoming the coding-agent runtime itself.
- Relevant environment: the parent human/operator; independently started Codex, Claude Code, Cline and compatible CLI-agent runtimes; repositories and workspaces; Git branches; staging environments; databases; deploy slots; browser profiles; ports and servers; local machines; private Relay infrastructure; external protected systems that may or may not enforce Commons fencing.
- Standard-distribution boundary: the `agent-commons` package, its bundled portable Agent Skill installed through `commons install-skill`, the `commons` CLI, local SQLite/filesystem state, optional private Team Relay and Console, shipped lease/policy/wrapper/audit machinery and the coordination behaviour that the installed Skill requires from supported agent sessions. External model inference, each coding runtime's internal reasoning/tool loop, Git/deployment/database/browser implementations and unrelated team governance remain separate systems.
- Credited operating / distribution surfaces: `README.md`; `.agents/skills/commons/SKILL.md`; `docs/architecture.md`; `docs/why-commons.md`; `docs/commons-implementation-status.md`; implemented CLI/Relay/local-state lease, task, messaging, wrapper and audit paths described by those first-party artifacts.
- Adjacent first-party surfaces excluded from ownership: repository-development dogfooding, maintainer/contributor governance, CI/release workflows, deterministic E2E/runtime-smoke test harnesses as tests rather than runtime owners, roadmap-only tracks, deferred admin/policy UI, and implementation internals of Codex/Claude Code/Cline or other external agent runtimes.
- First-party operating / deployment modes considered: enrolled local mode; enrolled private Team Relay mode; the explicit `disabled` workspace mode as a parent policy outcome; installed Skill operation in supported Codex/Claude Code/Cline sessions; CLI/wrapper operation; read-only Console observability. Future hosted/federated/multi-tenant and advanced admin-policy modes are excluded.
- Recursion level: one Commons project/work network coordinating multiple independently started agent work cells. A participating coding-agent session may itself be a viable system at a lower recursion, but its internal organization is not inherited; at this recursion it contributes one operational work cell whose Commons coordination behaviour is supplied by the first-party installed Skill.
- Reviewed revision: `6e911236127dc6cf0d231add87e302974151a7f4`.
- Observation date: 2026-10-01.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Commons deliberately sits beside coding-agent runtimes rather than proxying model inference. Its standard product combines a portable Skill with a scriptable CLI and either local coordination state or a private Team Relay. The Skill is distributed inside the package and installed into Codex, Claude Code and Cline discovery locations; an enrolled session is required to resolve workspace scope, establish attributed session identity, inspect active coordination state, publish current work, acquire leases before high-risk shared mutations, report evidence and cleanly release coordination state when work ends.

The control plane stores project-scoped agents, tasks, messages, leases and audit events. Local mode uses SQLite plus a readable filesystem board; Team mode uses a private HTTP Relay backed by SQLite and exposes a read-only Console. Canonical resource IDs and monotonically increasing fencing epochs make stale lease holders distinguishable. The current implementation includes acquire/list/renew/release, persisted denial events, high-risk wrappers for deploy, database migration, Git push, browser profile and server restart operations, and hash-chain audit verification. Strong enforcement outside Commons-controlled wrappers still depends on a protected downstream integration checking the current lease/fencing epoch.

The shipped Skill closes the behavioral side of that control plane. Before substantial work an enrolled agent must heartbeat, create/update a task, publish a plan, inspect active leases and acquire leases for high-risk resources. When a lease is denied, the Skill explicitly forbids proceeding and requires the agent to contact the holder, wait, revise its plan or escalate to the user. At completion it updates task state, publishes evidence, releases the lease and marks itself offline. Thus Commons is not merely passive shared storage: standard agent behaviour is coupled to returned coordination state.

Scope is separately parent-governed. Unknown scope is not consent. The Skill must ask the human whether the workspace participates as `remote`, `local`, or `disabled`, and for local/remote scope it must obtain an explicitly confirmed human owner before registration. The stored scope is re-resolved by subsequent sessions; `disabled` suppresses registration, messaging, inbox and lease participation. This is the only reviewed path that closes an identity/system-membership decision at the project/workspace boundary.

## Operational model

At the selected recursion, S1 work is performed by independently started Commons-enabled coding-agent sessions acting on repositories and engineering systems. Commons does not claim their hidden reasoning or runtime internals. The first-party contribution is the installed coordination Skill and CLI path that makes those sessions participating operational cells in the Commons organization: they declare intent, regulate access to shared resources, perform their coding/deployment work through their external runtime and environment, then return evidence and updated coordination state.

Coordination is primarily peer/distributed rather than managerial. Agents see current peer/resource state and make local coordination decisions, while the lease engine supplies atomic conflict detection, TTL/fencing and optional wrapper enforcement. The read-only Console provides broad observability but no shipped project-wide supervisory decision loop. No first-party autonomous manager or mutating operator console is established at the frozen revision.

## S1 — Operations

- State: A
- Function: perform repository-facing coding, validation, deployment or other engineering work as an enrolled Commons-enabled agent work cell while keeping its declared task/plan/evidence state coupled to the coordination system.
- Disturbance / variety regulated: task-specific repository and tool state, implementation choices, test/deployment feedback, changing local evidence, blockers and responses from the human or peer agents that affect the cell's next operational action.
- Decisive decision or feedback right: choose and revise the next task-specific coding/tool/action step from the current objective and returned evidence while respecting Commons coordination constraints.
- Decision owner: the supported autonomous coding-agent session (for example Codex, Claude Code or Cline) operating with the shipped Commons Skill in an enrolled workspace.
- Supporting / enforcement mechanisms: Commons scope and registration, task/plan records, inbox/messages, lease state, wrappers, durable audit events, local/Relay persistence and the Skill's lifecycle instructions.
- Closure path: enrolled session resolves identity/scope → agent declares task and plan → agent performs task-specific work through its runtime/environment subject to coordination state → repository/tool/environment evidence returns → the same agent revises, continues, completes or escalates and updates Commons state.
- Boundary reachability: the verified package carries the canonical Skill and `commons install-skill` installs it into supported Codex/Claude Code/Cline Skill locations; the shipped Skill then governs enrolled session startup, work and completion without application-authored glue.
- Why this is / is not agent-owned: removing the autonomous coding-agent actor while retaining Commons tasks, messages, SQLite, leases and Console leaves coordination infrastructure but no entity that makes the open-ended repository-facing operational decisions. Commons does not itself run the model, so the S1 decision right remains with the participating autonomous agent cell rather than with the deterministic control plane.
- Evidence: [`README.md`](https://github.com/t54-labs/agent-commons/blob/6e911236127dc6cf0d231add87e302974151a7f4/README.md); [`.agents/skills/commons/SKILL.md`](https://github.com/t54-labs/agent-commons/blob/6e911236127dc6cf0d231add87e302974151a7f4/.agents/skills/commons/SKILL.md); [`docs/architecture.md`](https://github.com/t54-labs/agent-commons/blob/6e911236127dc6cf0d231add87e302974151a7f4/docs/architecture.md); [`docs/commons-implementation-status.md`](https://github.com/t54-labs/agent-commons/blob/6e911236127dc6cf0d231add87e302974151a7f4/docs/commons-implementation-status.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the positive state applies to the Commons-enabled assembled operating mode. It does not import planning, delegation, memory, policy or audit functions from the external agent runtime itself, and a workspace enrolled as `disabled` is outside the active operational organization.

## S2 — Coordination

- State: A
- Function: attenuate interference among independently operating agent cells that intend to mutate the same shared engineering resource, and feed the conflict result back into their subsequent behaviour.
- Disturbance / variety regulated: simultaneous deploys, migrations, Git writes, browser-profile takeover, server/port use or other overlapping mutations where two agent cells could otherwise act on one shared mutable resource without knowing the other's current claim.
- Distinct S1 units: two or more independently started Commons-enabled coding-agent sessions in the same enrolled local/project scope, potentially across different runtimes, repositories or machines.
- Inter-S1 disturbance: a concrete shared-resource collision, such as one agent deploying while another begins a staging smoke/migration operation, or multiple agents attempting writes against the same database, branch, browser profile, server or deployment slot.
- Attenuating coordination relation: agents publish plans and inspect peer/lease state; write-like/exclusive/maintenance leases provide canonical resource identity, atomic grant/deny, TTL and fencing epochs; direct messages support holder negotiation and handoff; optional wrappers gate Commons-controlled risky commands against the current lease.
- Feedback into subsequent S1 behaviour: a denied lease is returned to the requesting agent; the shipped Skill says not to proceed and instead contact the holder, wait, change the plan or ask the user. Release/handoff or a new fenced grant then permits later operation, so the coordination result materially changes subsequent S1 action.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the witness is not merely messages or a shared task board. Commons identifies named classes of real shared-resource interference and supplies a conflict relation specifically designed to prevent stale or simultaneous mutation, plus an explicit behavioral return from grant/denial into later agent action.
- Decisive decision or feedback right: after Commons exposes the conflict/grant state, the autonomous requesting/holding agents own the discretionary mutual-adjustment response—whether to hand off, wait, revise resource use or escalate—while the deterministic lease engine enforces atomic incompatibility and fencing.
- Decision owner: participating autonomous agent cells using the first-party installed Skill; Commons runtime machinery owns grant/deny/fencing enforcement but not the discretionary coordination choice following that feedback.
- Supporting / enforcement mechanisms: Relay/local SQLite transactions, canonical resource IDs, lease modes, TTLs, fencing epochs, persisted denial events, heartbeats, task/plan state, direct/broadcast messaging and high-risk command wrappers.
- Closure path: agents declare intended shared-resource use → Commons detects/serializes incompatible lease claims → grant or denial is returned → agent adjusts plan/communication/action → holder releases/renews or requester waits/changes course → subsequent resource use reflects the coordinated result.
- Boundary reachability: lease acquisition and conflict handling are mandatory paths in the shipped Skill for enrolled sessions; the current implementation includes real local/Relay lease engines and wrappers, so no developer-authored coordinator is required to close the supported agent feedback loop.
- Why this is / is not agent-owned: the deterministic lease service would still block incompatible grants if the agent were removed, but it would not choose the organizational response to the conflict or perform a peer handoff/replan. The standard Skill supplies the feedback to an already participating autonomous agent, which owns that mutual-adjustment discretion. The runtime enforcement therefore supports rather than replaces agent ownership.
- Evidence: [`README.md`](https://github.com/t54-labs/agent-commons/blob/6e911236127dc6cf0d231add87e302974151a7f4/README.md); [`.agents/skills/commons/SKILL.md`](https://github.com/t54-labs/agent-commons/blob/6e911236127dc6cf0d231add87e302974151a7f4/.agents/skills/commons/SKILL.md); [`docs/architecture.md`](https://github.com/t54-labs/agent-commons/blob/6e911236127dc6cf0d231add87e302974151a7f4/docs/architecture.md); [`docs/why-commons.md`](https://github.com/t54-labs/agent-commons/blob/6e911236127dc6cf0d231add87e302974151a7f4/docs/why-commons.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: Commons cannot prevent an unrelated process from bypassing a lease unless the downstream system uses a Commons wrapper/hook/fencing check. The S2 claim is therefore about the supported Commons-enabled agent organization, not universal exclusion of all out-of-band actors.

## S3 — Inside-and-now control

- State: —
- Function: no material first-party whole-project current-control function is established at the reviewed boundary.
- Disturbance / variety regulated: potential project-wide contention among commitments, priorities, resources and exceptions was checked, but the shipped product does not assign a metasystemic actor authority to resolve that variety on behalf of the whole.
- Decisive decision or feedback right: none established beyond peer/local task decisions, deterministic resource-conflict enforcement and isolated operator interventions.
- Decision owner: none established for S3 at the project recursion.
- Supporting / enforcement mechanisms: task ownership/status, agent presence, lease state, policy/wrapper checks, audit history, operator-readable Console and CLI mutation primitives.
- Closure path: no project-wide S3 decision-and-return loop is supplied.
- Why this is / is not agent-owned: participating agents regulate their own tasks and negotiate shared-resource conflicts, but no agent is granted whole-project authority over current priorities, commitments or resource allocation. Deterministic leases are S2 conflict attenuation rather than S3 discretion.
- Evidence: [`docs/architecture.md`](https://github.com/t54-labs/agent-commons/blob/6e911236127dc6cf0d231add87e302974151a7f4/docs/architecture.md); [`docs/commons-product-design.md`](https://github.com/t54-labs/agent-commons/blob/6e911236127dc6cf0d231add87e302974151a7f4/docs/commons-product-design.md); [`docs/commons-implementation-status.md`](https://github.com/t54-labs/agent-commons/blob/6e911236127dc6cf0d231add87e302974151a7f4/docs/commons-implementation-status.md).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: a team can use Commons data as input to human management or build future admin policy, but those adjacent arrangements are not a shipped S3 closure at the frozen ref.

### Absence scope

- Surfaces inspected: README/product boundary; portable Skill lifecycle; local/Relay architecture and data model; tasks/plans/messages; resource leases and policy gate; wrappers; agent presence; audit; Console; implementation-status/deferred tracks.
- Plausible first-party paths checked: a central autonomous coordinator over project tasks; mutating Console/operator supervisor; policy engine with discretionary whole-system priority authority; project-wide task allocator; maintenance/force-release path as possible supervisory control.
- Why no material first-party path remains: the Console is explicitly read-only at the current release, advanced admin/policy mutation is deferred, agents own their own task/coordination actions and the hard runtime mechanisms enforce preselected lease/policy rules rather than choose whole-system priorities. Isolated force/resource operations do not establish a whole-system S3 loop.

## S3* — Complementary audit

- State: —
- Function: no sufficiently independent complementary audit path is established inside the supported Commons operating organization.
- Disturbance / variety regulated: uncertainty about whether agent-reported completion/evidence reflects operational reality was inspected.
- Decisive decision or feedback right: none supplied by an independent first-party auditor whose finding returns into project control.
- Decision owner: none established for S3*.
- Supporting / enforcement mechanisms: append-only audit events, hash-chain verification, evidence-bearing task updates, artifacts, message receipts, test/runtime-smoke infrastructure and Skill guidance to verify peer claims against primary evidence.
- Closure path: no independent audit judgment → control-return path is supplied by Commons itself.
- Why this is / is not agent-owned: the ordinary participating agent can inspect repository state or evidence, but that is not materially independent access beyond the operational path. The audit log records what Commons observed; it does not independently challenge an S1 claim.
- Evidence: [`README.md`](https://github.com/t54-labs/agent-commons/blob/6e911236127dc6cf0d231add87e302974151a7f4/README.md); [`docs/why-commons.md`](https://github.com/t54-labs/agent-commons/blob/6e911236127dc6cf0d231add87e302974151a7f4/docs/why-commons.md); [`docs/commons-implementation-status.md`](https://github.com/t54-labs/agent-commons/blob/6e911236127dc6cf0d231add87e302974151a7f4/docs/commons-implementation-status.md).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: external Git review, tests or an independently run reviewer can supply complementary evidence to a team using Commons, but Commons explicitly says it does not make unverified claims trustworthy and does not package that external acceptance actor as an S3* owner.

### Absence scope

- Surfaces inspected: append-only audit/event model; `audit verify`; evidence/artifact features; message receipt/acknowledgement; Skill safety/verification guidance; deterministic E2E/runtime-smoke tests; Console activity views; product statements about reported versus independent acceptance.
- Plausible first-party paths checked: audit-log verification as auditor; independent acceptance state; test/runtime-smoke harness as runtime auditor; peer verification prompted through messages; Console/operator review.
- Why no material first-party path remains: audit/history is ordinary evidence transport and integrity checking, while test harnesses are adjacent development/evaluation surfaces. Independent acceptance remains an external/team responsibility and no supported first-party complementary audit actor returns findings into runtime control.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party external-and-prospective adaptation function is established for the Commons organization.
- Disturbance / variety regulated: possible changes in agent runtimes, team environment, infrastructure, policy and future coordination needs were inspected.
- Decisive decision or feedback right: none established that converts sensed external/future distinctions into adaptation options and returns them to current capability.
- Decision owner: none established for S4.
- Supporting / enforcement mechanisms: current peer/resource discovery, heartbeat/activity state, scope resolution, audit history, repository roadmap/product documents and runtime compatibility work.
- Closure path: no supported outside-and-then adaptation loop is present.
- Why this is / is not agent-owned: participating agents react to current task/resource conditions; that is present-time operational/S2 regulation, not prospective modelling of the environment and adaptation of Commons capability.
- Evidence: [`README.md`](https://github.com/t54-labs/agent-commons/blob/6e911236127dc6cf0d231add87e302974151a7f4/README.md); [`docs/architecture.md`](https://github.com/t54-labs/agent-commons/blob/6e911236127dc6cf0d231add87e302974151a7f4/docs/architecture.md); [`docs/commons-implementation-status.md`](https://github.com/t54-labs/agent-commons/blob/6e911236127dc6cf0d231add87e302974151a7f4/docs/commons-implementation-status.md).
- Basis: structural absence.
- Confidence: high.
- Caveats: maintainers have roadmap and compatibility work, but those development/governance surfaces are adjacent to the assessed deployed product organization and are not borrowed as runtime S4 ownership.

### Absence scope

- Surfaces inspected: agent/lease/task state; messages and activity streams; scope resolver; current architecture; implementation-status/deferred tracks; roadmap/product-design references; runtime compatibility and smoke-test surfaces.
- Plausible first-party paths checked: adaptive runtime selection; environment/trend sensing; learning from audit history; roadmap-driven capability evolution; automatic policy/coordination adaptation from external change.
- Why no material first-party path remains: shipped sensing is about current coordination state, and roadmap/development work lies outside the credited operating boundary. No external/future model develops adaptation options that feed back into present Commons capability.

## S5 — Policy and identity

- State: P
- Function: close the parent-governed membership/privacy boundary that determines whether a workspace participates in Commons at all and, if so, whether it belongs to local-only or private-Relay coordination.
- Disturbance / variety regulated: accidental or unauthorized enrollment of personal/client/otherwise unrelated workspaces into a coordination network; disclosure of coordination metadata to the wrong scope; ambiguous human attribution for newly registered agents.
- Decisive decision or feedback right: choose `remote`, `local` or `disabled` when workspace scope is unknown, and explicitly establish the human owner before an agent can register in an enabled scope.
- Decision owner: the legitimate parent human/operator for the workspace. The Skill explicitly forbids inferring the choice or owner and requires an explicit answer.
- Supporting / enforcement mechanisms: `commons scope resolve`, `scope enroll`, persisted workspace rules/project config, human-owner storage, Relay/project identity, registration checks and the Skill's prohibition on register/broadcast/inbox/lease activity when scope is disabled or unresolved.
- Closure path: session encounters `unknown` scope → Skill stops and asks parent human → human makes the authoritative participation/scope decision → Commons persists `remote`, `local` or `disabled` enrollment (and human attribution when enabled) → subsequent sessions resolve that decision before registration → enabled sessions join only the selected scope, while disabled sessions perform no Commons coordination operations.
- Boundary reachability: scope-first resolution is mandatory in the shipped installed Skill and implemented CLI; it is not a development-only convention or an application-defined callback.
- Why this is / is not agent-owned: the autonomous agent is deliberately denied the ultimate participation choice when scope is unknown. It cannot infer consent or human identity and therefore cannot close this S5 decision internally. The parent decision is returned into runtime behaviour through persisted scope resolution, so the positive mode is `P`, not a generic human approval annotation.
- Identity / ultimate-policy issue: whether this workspace is a member of the Commons coordination organization and which privacy/trust boundary governs its coordination metadata and peer visibility.
- Ultimate authority in each claimed mode: parent human/operator only; no first-party autonomous S5 mode is claimed.
- Return-to-operation path: persisted scope and human attribution are resolved before each new participating session; they govern whether registration and all subsequent Commons coordination operations are allowed and which local/project boundary they use.
- Evidence: [`.agents/skills/commons/SKILL.md`](https://github.com/t54-labs/agent-commons/blob/6e911236127dc6cf0d231add87e302974151a7f4/.agents/skills/commons/SKILL.md); [`docs/why-commons.md`](https://github.com/t54-labs/agent-commons/blob/6e911236127dc6cf0d231add87e302974151a7f4/docs/why-commons.md); [`docs/architecture.md`](https://github.com/t54-labs/agent-commons/blob/6e911236127dc6cf0d231add87e302974151a7f4/docs/architecture.md); [`README.md`](https://github.com/t54-labs/agent-commons/blob/6e911236127dc6cf0d231add87e302974151a7f4/README.md).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: this S5 mapping is boundary-relative. It treats participation/privacy scope as an identity-level membership decision for the selected Commons project/workspace recursion; ordinary lease approval, task status, token possession or resource policy is not promoted to S5.

## Distributed OSS parent arrangement

The positive parent mode does not rely on repository maintainers or the public Commons development organization. It is local to the deployed Commons work network: the human who legitimately controls the workspace decides its coordination membership/privacy scope, and that decision is stored and returned into later session behaviour. Public OSS contributors, GitHub governance and T54 Labs development activity are therefore not used to manufacture organization-level `(P)` evidence.

## Self-hosted and non-human modes

Local and private-Relay deployments are both self-hosted modes. They preserve autonomous S1/S2 operation once the workspace has been enrolled, but they deliberately retain the membership/privacy decision at the parent human recursion. The read-only Console does not add a parent S3 mode, and no autonomous S5 alternative is established at the reviewed revision.

## Recursion

At the assessed project recursion, independently started Commons-enabled agent sessions are S1 work cells coordinating around shared engineering resources. Each coding agent may be a viable system at its own lower recursion, but Commons does not inherit that runtime's internal planning, tool routing, memory or governance. The parent human sits above the workspace-membership/privacy choice only; routine coding and resource-conflict decisions remain below that identity boundary.

## Variety and escalation

Commons attenuates high-risk inter-agent variety by forcing resource intentions into canonical names, lease modes, holder identity, TTL and fencing epochs. It amplifies coordination capacity through agent discovery, plans/tasks, direct/broadcast messaging and durable audit history. A lease denial preserves enough variety for an agent to choose among waiting, peer handoff, plan change or human escalation instead of collapsing every conflict into one generic failure.

The Skill also distinguishes ordinary coordination from escalation. Routine resource conflict remains peer-level S2. A blocked task may become `needs_human`, but that status alone is not S3/S4/S5. The one reviewed escalation that reaches ultimate parent authority is unknown workspace membership/privacy scope: the agent must stop and ask the human before Commons participation can begin.

## Evidence gaps

No material evidence gap prevents publication of the six states above at the frozen revision. The strongest interpretive boundary is S5: the positive claim is limited to workspace membership/privacy policy at the selected coordination recursion and does not generalize ordinary configuration into S5. Strong lease enforcement also remains bounded to Commons-controlled wrappers or downstream systems that validate lease/fencing state; out-of-band processes can bypass advisory coordination.
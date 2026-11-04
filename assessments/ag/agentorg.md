---
harness_id: agentorg
project_name: AgentOrg
repository: https://github.com/uniac-ai/AgentOrg
review_ref: 25e116cb719989ce568b272016b1936668efbf5f
reviewed_at: 2026-11-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A(P)
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# AgentOrg

## Review boundary

- System in focus: the installed AgentOrg Hub organization with its Actor clients, MCP-attached agent sessions, shared Work/Forms/Messages/claims, and optional human-root operation; not the upstream project's maintainer organization.
- Purpose and identity: assign durable responsibilities and decision rights to Actor positions, keep their work/report state, deliver requests and reviews, and admit external runtimes as implementations of those positions.
- Relevant environment: developers and human operators, connected Claude Code/Codex sessions and programs, local projects, external providers, shared resources and user requests.
- Standard-distribution boundary: the npm-distributed Hub server, actor CLI/library, MCP client integration, its bundled operating skill and documented root CLI path. The separately maintained OrgActor-Human browser application and external Provider internals are not credited with AgentOrg-specific decisions.
- Credited operating / distribution surfaces: `src/domain/`, `src/clients/mcp/`, `src/actor/`, `src/clients/cli/`, Hub-backed Workspace records and the shipped `skills/agentorg/SKILL.md`; installed client integration explicitly attaches existing autonomous agent sessions.
- Adjacent first-party surfaces excluded from ownership: repository's own CI, packaging/integration tests and contributor administration. Separate OrgActor-Human frontend and third-party Provider native executors are excluded except as documented optional clients/implementations; their own undocumented agents and governance cannot donate higher VSM functions.
- First-party operating / deployment modes considered: connected agent Actor under a manager, connected agent serving as manager with child reports, root-user CLI current-control mode, attached MCP/Codex/Claude session, optional Provider provisioning, generic program client.
- Recursion level: one AgentOrg-managed organization/HUB with attached Actor positions performing operational work; a nested position is not automatically a self-viable recursive organization.
- Reviewed revision: `25e116cb719989ce568b272016b1936668efbf5f`.
- Observation date: 2026-11-04.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

AgentOrg is a TypeScript/Node Hub exposing a stable organization of authenticated Actors through explicit Tool interfaces. It stores Actor identity, hierarchy, connection presence, claims and audit metadata, with Work, Forms, Status and Messages persisted via a version-pinned Workspace package and SQLite. The Hub itself has no LLM engine: Claude Code/Codex sessions attach through a first-party MCP adapter and skill, use the Hub's Actor authority, then autonomously perform work in their external project/runtime context. The adapter preserves session-to-position identity and supplies three entry calls: `attach`, `interfaces`, and `call`. Optional Providers can provision a position's implementation but have a separate identity/credential and do not become the Hub's decision owner.

The bundled skill is an operating protocol for an agent Actor: maintain its workstream, progress, blockers and asks; submit outcomes; receive attention items and replies; as manager, assign/review direct reports' Work and answer/escalate asks. A requester can return `changes_requested` to a submitter; `attention` and client waiter carry that change back to the responsible agent. The canonical root's CLI can separately read the team and make current-control Work/approval decisions, while Hub/Workspace enforce role restrictions. Resource claims detect a named conflict and refuse a second holder, but caller-composed behavior decides which resources to claim and how to recover.

Primary sources: [README](https://github.com/uniac-ai/AgentOrg/blob/25e116cb719989ce568b272016b1936668efbf5f/README.md), [design and domain contract](https://github.com/uniac-ai/AgentOrg/blob/25e116cb719989ce568b272016b1936668efbf5f/docs/design.md), [bundled agent operating skill](https://github.com/uniac-ai/AgentOrg/blob/25e116cb719989ce568b272016b1936668efbf5f/skills/agentorg/SKILL.md).

## Operational model

An attached agent Actor has a durable responsibility and can choose project actions in its independent model/tool runtime; it reports Work and submits results through AgentOrg. Operational units are active agent-filled positions, not merely registry rows or provider sockets. A manager Actor sees its reports' Work and asks, can select ownership and review submissions, and returns decisions into the subordinate's work queue. The same organizational relation can be run under a human root via the shipped CLI. Hub modules own validation, persistence, access checks and transport, not discretionary agent reasoning. A Provider's `ready` response is not proof that a model is thinking or that an S1 result is complete.

## S1 — Operations

- State: A
- Function: attached autonomous agent sessions carry out locally variable project work and return artifacts/results as Work submissions within their declared position.
- Disturbance / variety regulated: changing project requirements, source/tool results, work feedback and manager requests that demand operational judgment.
- Decisive decision or feedback right: select task actions and revise work within the Actor's purpose, then submit a result and respond to returned review or ask answers.
- Decision owner: attached Claude Code/Codex or other autonomous agent session in the documented first-party MCP operating mode; operator supplies initial position/credentials and task.
- Supporting / enforcement mechanisms: Hub Actor registry, MCP adapter, Workspace records, audit store and session hooks, Provider provisioning (optional).
- Closure path: agent receives assigned Work/attention, acts in its own project runtime, records progress and submits; requester reviews or changes assignment, after which the session receives and acts on returned state.
- Boundary reachability: the distributed MCP adapter and bundled skill explicitly attach supported agent sessions and supply the Work/attention/submit path. This is a wired operating mode, not merely an open-ended API a developer might someday connect.
- Why this is / is not agent-owned: cognition and project actions are in the attached external agent, credited as an actor only because the installed mode explicitly wires its decision/action/report loop; Hub persistence alone is not S1 autonomy.
- Evidence: [MCP agent client/attachment](https://github.com/uniac-ai/AgentOrg/blob/25e116cb719989ce568b272016b1936668efbf5f/src/clients/mcp/agent.ts), [Work bindings](https://github.com/uniac-ai/AgentOrg/blob/25e116cb719989ce568b272016b1936668efbf5f/src/domain/workspace.ts), [agent Work protocol](https://github.com/uniac-ai/AgentOrg/blob/25e116cb719989ce568b272016b1936668efbf5f/skills/agentorg/SKILL.md).
- Basis: structural.
- Confidence: medium-high.
- Caveats: Hub alone creates no model session and cannot guarantee external agent behavior; no paid provider runtime was executed in this review.

## S2 — Coordination

- State: C
- Function: prevent simultaneous operational Actors from destructively claiming the same shared resource while they do distinct Work.
- Disturbance / variety regulated: two active S1 positions can contend for one release lane, cluster or other shared named resource.
- Decisive decision or feedback right: caller seeks/renews/releases a resource claim; Hub refuses another active holder and names the conflict; an agent must compose its own response, negotiation and later retry.
- Decision owner: the holder/contender Actor selects a requested resource and intended follow-up; deterministic Hub claims enforce exclusive holding and expiry, but the standard distribution does not install an autonomous conflict-resolution policy for all Actors.
- Supporting / enforcement mechanisms: SQLite claim store, lifetime/holder checks, authenticated Actor identity, conflict refusals and root override.
- Closure path: the second claim returns a named-holder refusal; a custom agent policy or manager can subsequently wait, negotiate, change its work or retry after release/expiry, using the first-party claim path.
- Boundary reachability: named claims are an explicit shipped Hub Tool available to attached Actors and the root, and the skill documents their shared-resource purpose. The autonomy/coordination response after refusal requires composition.
- Why this is / is not agent-owned: concrete exclusive-claim regulation is first-party and function-specific, but its mandatory refusal/expiry judgment is deterministic and no universal autonomous coordination-closure actor is installed. This warrants constructor `C` rather than `A`.
- Distinct S1 units: separately attached active agent positions in one Hub organization, each with its own Work and local task environment.
- Inter-S1 disturbance: competing claims for the same named shared lane or resource.
- Attenuating coordination relation: exclusive holder check with conflict identity and explicit release/expiry.
- Feedback into subsequent S1 behaviour: refusal tells the contender who holds the resource; custom agent/operator behavior can adapt task choice or retry once the claim ends.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: `claims.ts` enforces a specific shared-resource collision and returns a conflict, rather than merely transferring messages or exposing untyped storage.
- Evidence: [claim implementation](https://github.com/uniac-ai/AgentOrg/blob/25e116cb719989ce568b272016b1936668efbf5f/src/domain/claims.ts), [domain Tool catalog](https://github.com/uniac-ai/AgentOrg/blob/25e116cb719989ce568b272016b1936668efbf5f/docs/design.md), [bundled skill organization commands](https://github.com/uniac-ai/AgentOrg/blob/25e116cb719989ce568b272016b1936668efbf5f/skills/agentorg/SKILL.md).
- Basis: structural.
- Confidence: medium.
- Caveats: no mandatory agent-side claim discipline or automatic release notification/negotiation is established; the Hub's isolated conflict decision is not by itself evidence of agent S2 ownership.

## S3 — Inside-and-now control

- State: A(P)
- Function: regulate current organization-wide or managerial-subtree commitments by assigning Work, responding to subordinate asks and accepting or returning submitted results.
- Disturbance / variety regulated: reports may block, diverge from assigned work, need approvals or consume commitments that must be reviewed and reprioritized by a responsible manager.
- Decisive decision or feedback right: see current direct-report Work/asks, choose ownership and goals, answer/escalate actionable asks, review a specific submission and return changes or accept it.
- Decision owner: in the agent-manager mode, the attached manager's agent exercises this discretionary current-control right; in the distinct root CLI mode, the legitimate human root can make equivalent authoritative choices.
- Supporting / enforcement mechanisms: `team`, `actor_view`, Work and Forms records, role checks, attention/waiter delivery and stored revisions.
- Closure path: manager observes report/ask/submission, chooses answer/reassignment or `work_review` verdict, Hub stores it, and the subordinate receives `attention` and updates/resubmits Work. Human root mode uses the same return path.
- Boundary reachability: the standard-distribution agent skill directly instructs managers to inspect team state, assign/review subordinate Work and handle asks; the shipped root CLI can act as the canonical human root with the Hub's authenticated rights. Both modes use the same installed Work/attention path.
- Why this is / is not agent-owned: in manager-agent mode, the agent selects which current intervention to make; deterministic record/authority checks enforce it. In root mode, the human is the decision owner. These are alternative modes, not concurrent owners of one decision.
- Whole-system current view: manager's `team` and `actor_view` show its reports' Work state, current asks and review queue; canonical root can see the whole organization.
- Current-control decision scope: assigning Work goals/owners, reviewing submitted commitments, answering/escalating blocking asks and changing subsequent report activity.
- Evidence: [team/attention projections](https://github.com/uniac-ai/AgentOrg/blob/25e116cb719989ce568b272016b1936668efbf5f/docs/design.md), [Workspace operation bindings](https://github.com/uniac-ai/AgentOrg/blob/25e116cb719989ce568b272016b1936668efbf5f/src/domain/workspace.ts), [agent manager procedure](https://github.com/uniac-ai/AgentOrg/blob/25e116cb719989ce568b272016b1936668efbf5f/skills/agentorg/SKILL.md), [root CLI authority](https://github.com/uniac-ai/AgentOrg/blob/25e116cb719989ce568b272016b1936668efbf5f/docs/programs.md).
- Basis: structural.
- Confidence: medium.
- Caveats: not every connected Actor is a manager; an agent-specific actual review choice was not exercised with a provider. Human root control is specifically current-work supervision, not an S5 identity-policy claim.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Attached manager agent | subordinate submission, ask or assignment need | agent issues `work_review`, `form_respond` or work assignment; subordinate sees returned attention and changes activity | [manager skill](https://github.com/uniac-ai/AgentOrg/blob/25e116cb719989ce568b272016b1936668efbf5f/skills/agentorg/SKILL.md), [Hub Workspace](https://github.com/uniac-ai/AgentOrg/blob/25e116cb719989ce568b272016b1936668efbf5f/src/domain/workspace.ts) |
| Parent (`P`) | Legitimate human root through installed CLI | organization/subordinate current Work or approval need | root issues authoritative answer/assignment/review and Hub returns it into Actor Work/attention | [CLI root credentials and operations](https://github.com/uniac-ai/AgentOrg/blob/25e116cb719989ce568b272016b1936668efbf5f/docs/programs.md), [design](https://github.com/uniac-ai/AgentOrg/blob/25e116cb719989ce568b272016b1936668efbf5f/docs/design.md) |

## S3* — Complementary audit

- State: —
- Function: no shipped independent complementary inspection of operational reality beyond ordinary work reporting and manager reviews is established.
- Disturbance / variety regulated: workers can misreport completion, but a separate audit-specific counter-observation path is not provided by the Hub.
- Decisive decision or feedback right: no first-party independent raw-artifact audit judgment with corrective return is established.
- Decision owner: managers review submissions through ordinary Work state; the root reads operation metadata, neither becomes a distinct packaged S3* actor.
- Supporting / enforcement mechanisms: append-only activity metadata, Work review verdicts, status/attention, Hub audit events and client context.
- Closure path: review changes can return to a worker as S3 accountability, not an independently sourced complementary operational audit.
- Why this is / is not agent-owned: a root `activity` read observes tool-call metadata, while `work_review` is normal reporting/review; no separately deployed direct-evidence auditor is wired.
- Evidence: [activity and Work boundaries](https://github.com/uniac-ai/AgentOrg/blob/25e116cb719989ce568b272016b1936668efbf5f/docs/design.md), [audit metadata code](https://github.com/uniac-ai/AgentOrg/blob/25e116cb719989ce568b272016b1936668efbf5f/src/domain/audit.ts), [manager skill](https://github.com/uniac-ai/AgentOrg/blob/25e116cb719989ce568b272016b1936668efbf5f/skills/agentorg/SKILL.md).
- Basis: structural.
- Confidence: medium-high.
- Caveats: a connected organization's external agents can run tests or review code, but that independently configured audit is not a default Hub function.

### Absence scope

- Surfaces inspected: Hub audit/claims/workspace/team/attention code, bundled operating skill, MCP session adapter, design and test inventory.
- Plausible first-party paths checked: root-only `activity`, `work_review` submissions, audit metadata, actor messages, generic external session tool access.
- Why no material first-party path remains: none defines a complementary direct-observation source, independently governed audit judgment and returned corrective control distinct from normal managerial review; custom external auditor composition is possible but not shipped.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party prospective environment/option-generation and return-to-current-capability loop is supplied.
- Disturbance / variety regulated: external demand and capability changes may affect the organization but are not converted by a shipped S4 process into adaptation choices.
- Decisive decision or feedback right: no distinct future-oriented model, option selection and S3 return path.
- Decision owner: an agent/user may propose new work, but the Hub has no S4-specific owner.
- Supporting / enforcement mechanisms: Work backlog, reports/asks, status, provider catalog, generic messages and stored historical activity.
- Closure path: no shipped external-prospecting option-to-implementation path; Work assignments remain present-task control.
- Why this is / is not agent-owned: storage and future-dated Work do not show externally grounded environmental modeling or adaptation.
- Evidence: [Tool catalog and projections](https://github.com/uniac-ai/AgentOrg/blob/25e116cb719989ce568b272016b1936668efbf5f/docs/design.md), [agent skill](https://github.com/uniac-ai/AgentOrg/blob/25e116cb719989ce568b272016b1936668efbf5f/skills/agentorg/SKILL.md).
- Basis: structural.
- Confidence: medium-high.
- Caveats: organization-specific skills might implement prospective assessment; they are external to this reviewed standard distribution.

### Absence scope

- Surfaces inspected: Hub domain/tool operations, design and programs/setup, built-in agent skill, client hooks and optional Provider path.
- Plausible first-party paths checked: Work follow-ups, status summaries, team attention, Provider discovery/provisioning, external messages and human/agent future tasks.
- Why no material first-party path remains: no concrete supported loop transforms outside/future evidence into adaptation options and returns those options as changed present capability; the interfaces are general work coordination primitives.

## S5 — Policy and identity

- State: —
- Function: the Hub models organization membership/purpose and enforces role authority, but no first-party identity/ultimate-policy deliberation and authoritative return loop is established.
- Disturbance / variety regulated: creating/closing a position, credential revocation and action approvals are governed structural operations, not necessarily policy/identity tensions of the whole organization.
- Decisive decision or feedback right: no distinct workflow takes an ultimate-policy issue to legitimate authority, decides organizational ethos/policy and returns an enforceable new policy into operation.
- Decision owner: human root chooses membership and routine configuration; agent managers can create authorized reports. Neither is evidenced as an S5-specific decision path merely from hierarchical titles or rights.
- Supporting / enforcement mechanisms: Actor registry, credentials, lifecycle checks, hierarchy, approval Forms and filtered interfaces.
- Closure path: Actor create/close and approval answers change ordinary access/work; absent is an explicit identity-policy issue/decision/returned governance process.
- Why this is / is not agent-owned: a root actor and purpose fields do not themselves prove the VSM S5 function; generic Forms allow many applications but do not compose ultimate policy.
- Evidence: [registry/lifecycle](https://github.com/uniac-ai/AgentOrg/blob/25e116cb719989ce568b272016b1936668efbf5f/src/domain/actors.ts), [Hub design authority](https://github.com/uniac-ai/AgentOrg/blob/25e116cb719989ce568b272016b1936668efbf5f/docs/design.md), [agent skill approval limits](https://github.com/uniac-ai/AgentOrg/blob/25e116cb719989ce568b272016b1936668efbf5f/skills/agentorg/SKILL.md).
- Basis: structural.
- Confidence: medium.
- Caveats: a particular organization may implement genuine parent S5 over these generic tools, but that case requires its own first-party operating contract and evidence.

### Absence scope

- Surfaces inspected: identity and registry, lifecycle authority, client/root credentials, Workspace/Forms, management skill and examples/setup.
- Plausible first-party paths checked: root creation/closure, purpose fields, approval Forms, management escalation, configuration and team hierarchy.
- Why no material first-party path remains: these are generic structural and task authorization capabilities without a shipped identity- or ultimate-policy-specific dispute, legitimate deciding forum and policy-return closure for the whole managed organization.

## Distributed OSS parent arrangement

The project accepts independent contributors, but the reviewed boundary is each installed AgentOrg organization. Project maintainers are not credited as its S3/S4/S5 parents. An installed canonical root has legitimate current-work authority over that organization and is credited only for the evidenced optional S3 parent mode. Human client UI lives in another repository; the shipped root CLI suffices for that mode without borrowing that UI.

## Self-hosted and non-human modes

The Hub and Actor clients are self-hosted. Roles may be filled by agents, programs or humans, but a program connection is not autonomous merely from authentication. Base S3 agent-manager and human-root current-control are alternative, independently reconstructable installed uses. Native provider execution, credentials and infrastructure do not inherit organizational decision rights.

## Recursion

Positions can have their own reports and local environments, and an Actor may be a manager at a lower level, but no complete S1–S5 closure for every nested position is guaranteed. Hierarchy and delegated Work do not by themselves establish recursive viability.

## Variety and escalation

AgentOrg attenuates coordination variety through authenticated identity, explicit Work/Forms state, revision checks, resource claims, and manager-scoped approvals. Attention streams bring selected changes to connected sessions; autonomous agents amplify response capacity. Blocked Work and approval asks can escalate to managers/root by the operating skill; these are routine current-work channels, not automatic algedonic signals or S5 governance.

## Evidence gaps

- The assessed Hub has no bundled LLM executor; S1 and base S3 autonomy depend on the explicitly integrated external session mode and were not behaviorally executed here.
- Resource claim refusals and Work/approval records are structurally evidenced; agent discretion after conflict or parent intervention is mode- and task-dependent.
- No independent raw-artifact audit or prospective learning loop is bundled. The external Human client and Provider internals were not imported as AgentOrg-owned organizational functions.

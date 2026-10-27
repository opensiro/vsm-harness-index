---
harness_id: meerkat
project_name: Meerkat
repository: https://github.com/lukacf/meerkat
review_ref: ae0517cc7721377c2cf0a58972bdd29cb7f4fbdc
reviewed_at: 2026-10-27
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A(P)
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Meerkat

## Review boundary

- System in focus: Meerkat's shipped local runtime-backed sessions and optional mob/WorkGraph capabilities through CLI, RPC, MCP and facade. Embedded StandaloneEphemeral is separately considered but does not inherit durable/team functions. No external MobKit runtime is included.
- Purpose and identity: Build, host and operate model-backed tool-using agents and durable teams.
- Relevant environment: Model backends, host tools/files/MCP, durable storage/realms, parallel work claims, member failures and operator interventions.
- Standard-distribution boundary: Meerkat's shipped local runtime-backed sessions and optional mob/WorkGraph capabilities through CLI, RPC, MCP and facade. Embedded StandaloneEphemeral is separately considered but does not inherit durable/team functions. No external MobKit runtime is included.
- Credited operating / distribution surfaces: meerkat facade/AgentFactory, core agent loop, runtime session services, agent-side mob tools and host mob controls, optional host-granted WorkGraph namespace and its companion workflow skill.
- Adjacent first-party surfaces excluded from ownership: Examples, development .claude/.rct actors, CI/TLC/proof/code-generation tools, internal ADRs and design notes, and mirrored docs/mobkit material are excluded as owners of the assessed shipped runtime. Tests corroborate mechanisms only.
- First-party operating / deployment modes considered: Supported local self-hosted runtime and operator-supervised configuration; no custom external composition is credited.
- Recursion level: One runtime/project deployment; nested task agents are not presumed recursively viable.
- Reviewed revision: ae0517cc7721377c2cf0a58972bdd29cb7f4fbdc
- Observation date: 2026-10-27
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

A Rust library-first platform exposes one shared agent core through CLI/REST/RPC/MCP and SDK surfaces. AgentFactory composes providers, tool dispatch, sessions, hooks, skills and optional memory. Runtime-backed sessions persist state in explicit realms and own turn/control transitions; standalone builders are intentionally narrower. Mobs supply session-backed members, profiles, peer wiring, stable identities, flow execution and status/retire/spawn controls. Agent-side mob tools are composed through build_agent rather than requiring a separate external supervisor engine. Hosts retain placement/grants and current operator control. WorkGraph optionally exposes durable claims, revisions, evidence and readiness under an exact namespace grant. Deterministic machines enforce lifecycle, budgets and authorizations. Adaptive layers are internal next-layer planning/repair, not automatically prospective environmental adaptation. Approval records alone do not gate effects without host composition.

## Operational model

Provider-backed sessions enact task outcomes. In mob-enabled sessions the creating agent can inspect members/status/output/token use and decide current membership, retirement and new profile/model allocation; operator consoles alternatively control the same whole mob. WorkGraph claim/revision/readiness primitives regulate concrete duplicate/stale shared-work interference, but a host still configures namespace and coordination policy; this is an S2 constructor, not a universal collision-free team claim.

## S1 — Operations

- State: A
- Function: Model-backed operational task execution
- Disturbance / variety regulated: Uncertain inputs, tool results, file state and task outcomes
- Decisive decision or feedback right: Select tools/actions and final turn outcome
- Decision owner: Agent model inside core session
- Supporting / enforcement mechanisms: Provider runtime, core loop, typed tool dispatch, persistent sessions and runtime drivers
- Closure path: Tool outputs and peer results feed subsequent model calls; committed history/artifacts retain the result
- Why this is / is not agent-owned: Agent model inside core session; Architectural availability, not benchmarked task success; standalone and mob-enabled modes are not conflated.
- Evidence: [crates/meerkat-core/src/agent.rs](https://github.com/lukacf/meerkat/blob/ae0517cc7721377c2cf0a58972bdd29cb7f4fbdc/crates/meerkat-core/src/agent.rs); [README.md](https://github.com/lukacf/meerkat/blob/ae0517cc7721377c2cf0a58972bdd29cb7f4fbdc/README.md) agent execution/embedded boundaries; [crates/meerkat-mob-mcp/src/agent_tools.rs](https://github.com/lukacf/meerkat/blob/ae0517cc7721377c2cf0a58972bdd29cb7f4fbdc/crates/meerkat-mob-mcp/src/agent_tools.rs)
- Basis: structural
- Confidence: high
- Caveats: Architectural availability, not benchmarked task success; standalone and mob-enabled modes are not conflated.
- Boundary reachability: meerkat facade/AgentFactory, core agent loop, runtime session services, agent-side mob tools and host mob controls, optional host-granted WorkGraph namespace and its companion workflow skill. The cited decision path is shipped in this mode and returns through Provider runtime, core loop, typed tool dispatch, persistent sessions and runtime drivers.

## S2 — Coordination

- State: C
- Function: Regulate competing agents' durable shared-work claims
- Disturbance / variety regulated: Multiple workers can race for the same ready item or act on stale revision/ownership
- Decisive decision or feedback right: Claim/release with exact revision and owner, observe expiry, then reload/reconsider after conflict
- Decision owner: Deterministic WorkGraph authority under host namespace grant; autonomous policy/host composition remains explicit
- Supporting / enforcement mechanisms: Claim ownership/leases/CAS, readiness service, workflow skill; mob resource-overlap projections are advisory
- Closure path: A stale write/claim is rejected; agent reloads current item/snapshot and revises work choice, while release makes work available to another worker
- Why this is / is not agent-owned: Deterministic WorkGraph authority under host namespace grant; autonomous policy/host composition remains explicit; This is specific claim-contention regulation, not generic DAG/messaging. Host-issued namespace grant and coordinating actor/policy must be composed. Advisory resource claims do not globally enforce exclusivity.
- Evidence: [docs/guides/workgraph.mdx](https://github.com/lukacf/meerkat/blob/ae0517cc7721377c2cf0a58972bdd29cb7f4fbdc/docs/guides/workgraph.mdx) lines 106–138 and 163–180; [crates/meerkat-workgraph/src/lib.rs](https://github.com/lukacf/meerkat/blob/ae0517cc7721377c2cf0a58972bdd29cb7f4fbdc/crates/meerkat-workgraph/src/lib.rs) namespace capability and companion skill; [crates/meerkat-workgraph/src/tools.rs](https://github.com/lukacf/meerkat/blob/ae0517cc7721377c2cf0a58972bdd29cb7f4fbdc/crates/meerkat-workgraph/src/tools.rs); [crates/meerkat-mob/src/coordination.rs](https://github.com/lukacf/meerkat/blob/ae0517cc7721377c2cf0a58972bdd29cb7f4fbdc/crates/meerkat-mob/src/coordination.rs)
- Basis: structural
- Confidence: medium
- Caveats: This is specific claim-contention regulation, not generic DAG/messaging. Host-issued namespace grant and coordinating actor/policy must be composed. Advisory resource claims do not globally enforce exclusivity.
- Boundary reachability: meerkat facade/AgentFactory, core agent loop, runtime session services, agent-side mob tools and host mob controls, optional host-granted WorkGraph namespace and its companion workflow skill. The cited decision path is shipped in this mode and returns through Claim ownership/leases/CAS, readiness service, workflow skill; mob resource-overlap projections are advisory.
- Distinct S1 units: Concurrent task agents producing separate operational outcomes.
- Inter-S1 disturbance: Multiple workers can race for the same ready item or act on stale revision/ownership
- Attenuating coordination relation: Claim/release with exact revision and owner, observe expiry, then reload/reconsider after conflict
- Feedback into subsequent S1 behaviour: A stale write/claim is rejected; agent reloads current item/snapshot and revises work choice, while release makes work available to another worker
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: This is specific claim-contention regulation, not generic DAG/messaging. Host-issued namespace grant and coordinating actor/policy must be composed. Advisory resource claims do not globally enforce exclusivity. Regulate competing agents' durable shared-work claims

## S3 — Inside-and-now control

- State: A(P)
- Function: Current regulation of the mob's operational members and commitments
- Disturbance / variety regulated: Stalled, failed or costly members and changing team needs
- Decisive decision or feedback right: Read whole mob/member current state and token usage; retire unneeded work and spawn/replace profile/model capability; parent can intervene through host controls
- Decision owner: Creating/managing agent in base mode; legitimate local mob operator in parent mode
- Supporting / enforcement mechanisms: Agent mob_list_members/check/retire/spawn tools, ownership scopes and host RPC/CLI/SDK status/cancel/lifecycle APIs
- Closure path: Agent inspects status then changes roster/commitments; retirement removes recipient authority and new spawn changes subsequent work; host decisions enter the same runtime lifecycle
- Why this is / is not agent-owned: Creating/managing agent in base mode; legitimate local mob operator in parent mode; Not credited from static budgets or supervisor naming. Scope is the managed mob or owned descendant team; arbitrary host-only rights are not attributed to agents.
- Evidence: [crates/meerkat-mob-mcp/src/agent_tools.rs](https://github.com/lukacf/meerkat/blob/ae0517cc7721377c2cf0a58972bdd29cb7f4fbdc/crates/meerkat-mob-mcp/src/agent_tools.rs) lines 2840–2980; [docs/concepts/mobs.mdx](https://github.com/lukacf/meerkat/blob/ae0517cc7721377c2cf0a58972bdd29cb7f4fbdc/docs/concepts/mobs.mdx) host versus agent boundaries; [docs/guides/mobs.mdx](https://github.com/lukacf/meerkat/blob/ae0517cc7721377c2cf0a58972bdd29cb7f4fbdc/docs/guides/mobs.mdx) operator observation/lifecycle; [crates/meerkat-mob/src/control_policy.rs](https://github.com/lukacf/meerkat/blob/ae0517cc7721377c2cf0a58972bdd29cb7f4fbdc/crates/meerkat-mob/src/control_policy.rs)
- Basis: structural
- Confidence: medium
- Caveats: Not credited from static budgets or supervisor naming. Scope is the managed mob or owned descendant team; arbitrary host-only rights are not attributed to agents.
- Boundary reachability: meerkat facade/AgentFactory, core agent loop, runtime session services, agent-side mob tools and host mob controls, optional host-granted WorkGraph namespace and its companion workflow skill. The cited decision path is shipped in this mode and returns through Agent mob_list_members/check/retire/spawn tools, ownership scopes and host RPC/CLI/SDK status/cancel/lifecycle APIs.
- Whole-system current view: The cited current state/report path covers all units in the declared deployment.
- Current-control decision scope: Read whole mob/member current state and token usage; retire unneeded work and spawn/replace profile/model capability; parent can intervene through host controls

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Main agent | Stalled, failed or costly members and changing team needs | Agent inspects status then changes roster/commitments; retirement removes recipient authority and new spawn changes subsequent work; host decisions enter the same runtime lifecycle | [crates/meerkat-mob-mcp/src/agent_tools.rs](https://github.com/lukacf/meerkat/blob/ae0517cc7721377c2cf0a58972bdd29cb7f4fbdc/crates/meerkat-mob-mcp/src/agent_tools.rs) lines 2840–2980; [docs/concepts/mobs.mdx](https://github.com/lukacf/meerkat/blob/ae0517cc7721377c2cf0a58972bdd29cb7f4fbdc/docs/concepts/mobs.mdx) host versus agent boundaries; [docs/guides/mobs.mdx](https://github.com/lukacf/meerkat/blob/ae0517cc7721377c2cf0a58972bdd29cb7f4fbdc/docs/guides/mobs.mdx) operator observation/lifecycle; [crates/meerkat-mob/src/control_policy.rs](https://github.com/lukacf/meerkat/blob/ae0517cc7721377c2cf0a58972bdd29cb7f4fbdc/crates/meerkat-mob/src/control_policy.rs) |
| Parent (`P`) | Legitimate local operator | Operator current intervention on the whole project | Agent inspects status then changes roster/commitments; retirement removes recipient authority and new spawn changes subsequent work; host decisions enter the same runtime lifecycle | [crates/meerkat-mob-mcp/src/agent_tools.rs](https://github.com/lukacf/meerkat/blob/ae0517cc7721377c2cf0a58972bdd29cb7f4fbdc/crates/meerkat-mob-mcp/src/agent_tools.rs) lines 2840–2980; [docs/concepts/mobs.mdx](https://github.com/lukacf/meerkat/blob/ae0517cc7721377c2cf0a58972bdd29cb7f4fbdc/docs/concepts/mobs.mdx) host versus agent boundaries; [docs/guides/mobs.mdx](https://github.com/lukacf/meerkat/blob/ae0517cc7721377c2cf0a58972bdd29cb7f4fbdc/docs/guides/mobs.mdx) operator observation/lifecycle; [crates/meerkat-mob/src/control_policy.rs](https://github.com/lukacf/meerkat/blob/ae0517cc7721377c2cf0a58972bdd29cb7f4fbdc/crates/meerkat-mob/src/control_policy.rs) |

## S3* — Complementary audit

- State: —
- Function: No supplied complementary independent corrective audit loop
- Disturbance / variety regulated: Accuracy of agent completion reports
- Decisive decision or feedback right: No first-party audit-specific judgment/access/return topology established
- Decision owner: None established at the shipped runtime boundary
- Supporting / enforcement mechanisms: Council/fork helpers, status/history, tool authorization audit records, structured output checks and developer TLC/tests
- Closure path: Councils are generic peer collaboration and records expose operational provenance; no packaged independently governed corrective audit loop is established
- Why this is / is not agent-owned: None established at the shipped runtime boundary; Independent reviewer examples, development validators and routine artifact checking do not supply assessed-runtime S3*.
- Evidence: [docs/reference/builtin-tools.mdx](https://github.com/lukacf/meerkat/blob/ae0517cc7721377c2cf0a58972bdd29cb7f4fbdc/docs/reference/builtin-tools.mdx) council/forks; [crates/meerkat-mob-mcp/src/temporary_council.rs](https://github.com/lukacf/meerkat/blob/ae0517cc7721377c2cf0a58972bdd29cb7f4fbdc/crates/meerkat-mob-mcp/src/temporary_council.rs); [crates/meerkat-core/src/authorization/audit.rs](https://github.com/lukacf/meerkat/blob/ae0517cc7721377c2cf0a58972bdd29cb7f4fbdc/crates/meerkat-core/src/authorization/audit.rs); [README.md](https://github.com/lukacf/meerkat/blob/ae0517cc7721377c2cf0a58972bdd29cb7f4fbdc/README.md) lifecycle verification scope
- Basis: structural
- Confidence: medium
- Caveats: Independent reviewer examples, development validators and routine artifact checking do not supply assessed-runtime S3*.

### Absence scope

- Surfaces inspected: [docs/reference/builtin-tools.mdx](https://github.com/lukacf/meerkat/blob/ae0517cc7721377c2cf0a58972bdd29cb7f4fbdc/docs/reference/builtin-tools.mdx) council/forks; [crates/meerkat-mob-mcp/src/temporary_council.rs](https://github.com/lukacf/meerkat/blob/ae0517cc7721377c2cf0a58972bdd29cb7f4fbdc/crates/meerkat-mob-mcp/src/temporary_council.rs); [crates/meerkat-core/src/authorization/audit.rs](https://github.com/lukacf/meerkat/blob/ae0517cc7721377c2cf0a58972bdd29cb7f4fbdc/crates/meerkat-core/src/authorization/audit.rs); [README.md](https://github.com/lukacf/meerkat/blob/ae0517cc7721377c2cf0a58972bdd29cb7f4fbdc/README.md) lifecycle verification scope; runtime entry, roles/tools, supported configuration and operating documentation within the declared boundary.
- Plausible first-party paths checked: Council/fork helpers, status/history, tool authorization audit records, structured output checks and developer TLC/tests; autonomous and operator-governed alternatives were checked for no supplied complementary independent corrective audit loop.
- Why no material first-party path remains: Councils are generic peer collaboration and records expose operational provenance; no packaged independently governed corrective audit loop is established Independent reviewer examples, development validators and routine artifact checking do not supply assessed-runtime S3*. This is a bounded shipped-distribution conclusion, not impossibility of an extension.

## S4 — Outside-and-then intelligence

- State: —
- Function: No external-and-prospective capability adaptation loop supplied
- Disturbance / variety regulated: Changing future environment or capability needs
- Decisive decision or feedback right: No shipped environmental sensing/options/operational-capability return owner established
- Decision owner: None established
- Supporting / enforcement mechanisms: Adaptive layer planning, model fallback/brain_swap, tool catalog selection, memory, skill updates and schedules
- Closure path: Adaptive decisions select next internal task layer from previous results; fallback and loading regulate present execution, without a first-party external/future adaptation loop
- Why this is / is not agent-owned: None established; Adaptive nomenclature, dynamic tools and a research-team example are not an S4-specific constructor or parent adaptation loop.
- Evidence: [crates/meerkat-mob/src/adaptive.rs](https://github.com/lukacf/meerkat/blob/ae0517cc7721377c2cf0a58972bdd29cb7f4fbdc/crates/meerkat-mob/src/adaptive.rs) LayerDecision/PlanningTurnRequest/run loop; [docs/reference/builtin-tools.mdx](https://github.com/lukacf/meerkat/blob/ae0517cc7721377c2cf0a58972bdd29cb7f4fbdc/docs/reference/builtin-tools.mdx); [docs/concepts/memory-and-compaction.mdx](https://github.com/lukacf/meerkat/blob/ae0517cc7721377c2cf0a58972bdd29cb7f4fbdc/docs/concepts/memory-and-compaction.mdx)
- Basis: structural
- Confidence: medium
- Caveats: Adaptive nomenclature, dynamic tools and a research-team example are not an S4-specific constructor or parent adaptation loop.

### Absence scope

- Surfaces inspected: [crates/meerkat-mob/src/adaptive.rs](https://github.com/lukacf/meerkat/blob/ae0517cc7721377c2cf0a58972bdd29cb7f4fbdc/crates/meerkat-mob/src/adaptive.rs) LayerDecision/PlanningTurnRequest/run loop; [docs/reference/builtin-tools.mdx](https://github.com/lukacf/meerkat/blob/ae0517cc7721377c2cf0a58972bdd29cb7f4fbdc/docs/reference/builtin-tools.mdx); [docs/concepts/memory-and-compaction.mdx](https://github.com/lukacf/meerkat/blob/ae0517cc7721377c2cf0a58972bdd29cb7f4fbdc/docs/concepts/memory-and-compaction.mdx); runtime entry, roles/tools, supported configuration and operating documentation within the declared boundary.
- Plausible first-party paths checked: Adaptive layer planning, model fallback/brain_swap, tool catalog selection, memory, skill updates and schedules; autonomous and operator-governed alternatives were checked for no external-and-prospective capability adaptation loop supplied.
- Why no material first-party path remains: Adaptive decisions select next internal task layer from previous results; fallback and loading regulate present execution, without a first-party external/future adaptation loop Adaptive nomenclature, dynamic tools and a research-team example are not an S4-specific constructor or parent adaptation loop. This is a bounded shipped-distribution conclusion, not impossibility of an extension.

## S5 — Policy and identity

- State: —
- Function: No runtime identity/ultimate-policy adjudication loop supplied
- Disturbance / variety regulated: Ultimate purpose/policy conflict of the deployed system
- Decisive decision or feedback right: No issue-to-legitimate-authority-to-returned-ultimate-policy closure established
- Decision owner: Host/operator config authority alone is not a qualifying S5 owner
- Supporting / enforcement mechanisms: Realm auth/config, grants, signed mobpack trust, skills identity migrations and approval records
- Closure path: Controls enforce host-selected boundaries; skill UUID migration is identifier administration, and approval records require effect-policy composition
- Why this is / is not agent-owned: Host/operator config authority alone is not a qualifying S5 owner; MobKit governance mirrors and internal governed-default ADRs are adjacent. Legitimate operator current control is S3, not automatic S5.
- Evidence: [docs/reference/skills-governance-runbook.mdx](https://github.com/lukacf/meerkat/blob/ae0517cc7721377c2cf0a58972bdd29cb7f4fbdc/docs/reference/skills-governance-runbook.mdx); [crates/meerkat-mob/src/control_policy.rs](https://github.com/lukacf/meerkat/blob/ae0517cc7721377c2cf0a58972bdd29cb7f4fbdc/crates/meerkat-mob/src/control_policy.rs); [README.md](https://github.com/lukacf/meerkat/blob/ae0517cc7721377c2cf0a58972bdd29cb7f4fbdc/README.md) approvals; [docs/concepts/mobs.mdx](https://github.com/lukacf/meerkat/blob/ae0517cc7721377c2cf0a58972bdd29cb7f4fbdc/docs/concepts/mobs.mdx)
- Basis: structural
- Confidence: medium
- Caveats: MobKit governance mirrors and internal governed-default ADRs are adjacent. Legitimate operator current control is S3, not automatic S5.

### Absence scope

- Surfaces inspected: [docs/reference/skills-governance-runbook.mdx](https://github.com/lukacf/meerkat/blob/ae0517cc7721377c2cf0a58972bdd29cb7f4fbdc/docs/reference/skills-governance-runbook.mdx); [crates/meerkat-mob/src/control_policy.rs](https://github.com/lukacf/meerkat/blob/ae0517cc7721377c2cf0a58972bdd29cb7f4fbdc/crates/meerkat-mob/src/control_policy.rs); [README.md](https://github.com/lukacf/meerkat/blob/ae0517cc7721377c2cf0a58972bdd29cb7f4fbdc/README.md) approvals; [docs/concepts/mobs.mdx](https://github.com/lukacf/meerkat/blob/ae0517cc7721377c2cf0a58972bdd29cb7f4fbdc/docs/concepts/mobs.mdx); runtime entry, roles/tools, supported configuration and operating documentation within the declared boundary.
- Plausible first-party paths checked: Realm auth/config, grants, signed mobpack trust, skills identity migrations and approval records; autonomous and operator-governed alternatives were checked for no runtime identity/ultimate-policy adjudication loop supplied.
- Why no material first-party path remains: Controls enforce host-selected boundaries; skill UUID migration is identifier administration, and approval records require effect-policy composition MobKit governance mirrors and internal governed-default ADRs are adjacent. Legitimate operator current control is S3, not automatic S5. This is a bounded shipped-distribution conclusion, not impossibility of an extension.

## Distributed OSS parent arrangement

Public contributors and maintainers are outside this deployed-runtime recursion. Local operator decisions do not imply project-wide or organization-wide parent governance.

## Self-hosted and non-human modes

Self-hosted operation is the assessed mode; parent notation is used only for the explicitly established function-specific loop, if any. No intentionally non-human governing organization is supplied.

## Recursion

Agents, tasks and sessions may be nested, but this does not establish independent viable systems with their own complete metasystem.

## Variety and escalation

Model backends, host tools/files/MCP, durable storage/realms, parallel work claims, member failures and operator interventions. Provider-backed sessions enact task outcomes. In mob-enabled sessions the creating agent can inspect members/status/output/token use and decide current membership, retirement and new profile/model allocation; operator consoles alternatively control the same whole mob. WorkGraph claim/revision/readiness primitives regulate concrete duplicate/stale shared-work interference, but a host still configures namespace and coordination policy; this is an S2 constructor, not a universal collision-free team claim.

## Evidence gaps

Frozen-source/static assessment. Host has no cargo/Rust or Node, so native crate/SDK compilation and tests were not run; live providers were not invoked. Source review distinguishes real package APIs from examples, future/internal designs and mirrored external MobKit docs. No cross-host operational reliability or independent semantic review is claimed.

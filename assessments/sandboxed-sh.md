---
harness_id: sandboxed-sh
project_name: sandboxed.sh
repository: https://github.com/Th0rgal/sandboxed.sh
review_ref: 8595836b5f7d23102d1b89b9ac3b59b0842b11a7
reviewed_at: 2026-10-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-04
status: excluded-no-agentic-vsm
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# sandboxed.sh

## Review boundary

- System in focus: the first-party `Th0rgal/sandboxed.sh` mission-execution/control backend at frozen revision `8595836b5f7d23102d1b89b9ac3b59b0842b11a7`, including projects/grants/tracks/decisions, mission/workspace lifecycle, event/receipt surfaces, Library configuration, automations, model routing and MCP-facing execution controls.
- Purpose and identity: provide canonical structured project/execution state and safely execute bounded missions in isolated workspaces for a separate coordinator.
- Relevant environment: operators, coordinator/controller sessions, GitHub/project state, compute nodes, model providers, external coding-agent harnesses, workspace/container state, mission events and receipts.
- Standard-distribution boundary: sandboxed.sh backend/dashboard/MCP/project and mission-control machinery are inside. Hermes or another MCP-capable coordinator owns decide/coordinate judgment; Claude Code/OpenCode/Codex/Gemini/Grok mission harnesses own their own open-ended reasoning/tool loops and remain external.
- Credited operating / distribution surfaces: `README.md`; `docs/AGENT_CONTROL_PLANE.md`; `docs/HERMES_ORCHESTRATION.md`; `docs/MISSION_API.md`; `docs/HARNESS_SYSTEM.md`; `agents.md`; backend project/mission/workspace/model-routing code.
- Adjacent first-party surfaces excluded from ownership: the separate Hermes fork/coordinator; patched Hermes integration artifacts; external coding-agent CLIs; dashboard/mobile projections; repository-development CI/tests; target-architecture text not wired at the frozen revision.
- First-party operating / deployment modes considered: project/grant/track state; mission dispatch/execution; isolated workspace runners; automations; model routing/fallback; MCP project/mission tools; receipts/evidence/event streams; operator dashboard controls.
- Recursion level: the sandboxed.sh execution backend around a project/mission portfolio. Coordinator judgment and mission-harness semantic reasoning are separate systems at this boundary.
- Reviewed revision: `8595836b5f7d23102d1b89b9ac3b59b0842b11a7`.
- Observation date: 2026-10-04.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

The frozen README defines sandboxed.sh as the “mission-execution backend” of a two-part system: a coordinator decides what to do and when, while sandboxed.sh runs missions in isolated workspaces. The control-plane design sharpens the boundary: Hermes owns conversation, judgment, controller scheduling and operator interaction; sandboxed.sh owns project intent storage, attempts, leases, observations, receipts, projections and isolated execution, and explicitly “must not own autonomous prioritization or unreviewed judgment.”

Mission execution launches external Claude Code/OpenCode/Codex/Gemini/Grok harnesses inside the selected workspace. sandboxed.sh prepares config/skills/tool policy, selects the external harness, spawns it, normalizes its events and records execution state. The external harness chooses semantic code/tool actions.

Counterfactual owner test: remove Hermes/controller judgment and external mission harnesses while retaining sandboxed.sh's project database, grants, workspaces, queues, routing, receipts, dashboards and mission runner. The backend can still validate/execute explicit commands and maintain canonical state, but it cannot autonomously interpret an open-ended project objective and choose the next semantic intervention or mission action. First-party S1 therefore does not close.

Primary evidence:

- [`README.md`](https://github.com/Th0rgal/sandboxed.sh/blob/8595836b5f7d23102d1b89b9ac3b59b0842b11a7/README.md)
- [`docs/AGENT_CONTROL_PLANE.md`](https://github.com/Th0rgal/sandboxed.sh/blob/8595836b5f7d23102d1b89b9ac3b59b0842b11a7/docs/AGENT_CONTROL_PLANE.md)
- [`docs/HERMES_ORCHESTRATION.md`](https://github.com/Th0rgal/sandboxed.sh/blob/8595836b5f7d23102d1b89b9ac3b59b0842b11a7/docs/HERMES_ORCHESTRATION.md)
- [`docs/HARNESS_SYSTEM.md`](https://github.com/Th0rgal/sandboxed.sh/blob/8595836b5f7d23102d1b89b9ac3b59b0842b11a7/docs/HARNESS_SYSTEM.md)
- [`agents.md`](https://github.com/Th0rgal/sandboxed.sh/blob/8595836b5f7d23102d1b89b9ac3b59b0842b11a7/agents.md)

## Operational model

A coordinator/controller reads project state and decides which intervention should occur. It calls sandboxed.sh through MCP/HTTP to update structured intent or dispatch a mission. sandboxed.sh checks authority/configuration, prepares an isolated workspace, launches the selected external coding-agent harness, streams/records events and returns receipts/evidence. The coordinator later reconciles those outputs and decides what to do next.

## S1 — Operations

- State: —
- Function: no first-party autonomous open-ended project/mission operation is established.
- Disturbance / variety regulated: workspace isolation, project/mission state, grants, routing, resource constraints and execution lifecycle are regulated; semantic project prioritization and mission action selection are owned by the coordinator or external mission harness.
- Decisive decision or feedback right: interpret the project/task objective and observations, choose the next semantic intervention/tool/code action and decide completion.
- Decision owner: external Hermes/other coordinator at project-control level and external Claude/OpenCode/Codex/Gemini/Grok harness at mission-execution reasoning level.
- Supporting / enforcement mechanisms: projects.db; grants/tracks/decisions; mission runner; workspace isolation; Library; model routing; MCP commands; receipts/events; automation scheduling.
- Closure path: project intent/state → external coordinator judgment → sandboxed.sh command/mission dispatch → external mission-harness reasoning/tool loop → receipt/evidence → external coordinator reconciliation/next decision.
- Why this is / is not agent-owned: sandboxed.sh executes and records explicit interventions but deliberately does not own autonomous judgment/prioritization; semantic mission behavior is supplied by separate harnesses.
- Evidence: [`README.md`](https://github.com/Th0rgal/sandboxed.sh/blob/8595836b5f7d23102d1b89b9ac3b59b0842b11a7/README.md); [`docs/AGENT_CONTROL_PLANE.md`](https://github.com/Th0rgal/sandboxed.sh/blob/8595836b5f7d23102d1b89b9ac3b59b0842b11a7/docs/AGENT_CONTROL_PLANE.md); [`agents.md`](https://github.com/Th0rgal/sandboxed.sh/blob/8595836b5f7d23102d1b89b9ac3b59b0842b11a7/agents.md).
- Basis: explicit + structural negative review.
- Confidence: high.
- Caveats: the broader Paloma composition may be agentic, but this assessment cannot import Hermes/controller or external harness autonomy into sandboxed.sh.

### Absence scope

- Surfaces inspected: project/control-plane docs, project/grant/track/decision state, mission runner/harness architecture, automations, model routing, MCP tools, workspaces, receipts/evidence and dashboard/mobile controls.
- Plausible first-party paths checked: controller scheduling, project state derivation, mission dispatch, automation triggers, model routing/fallback, receipt reconciliation and target “get_situation/execute_action” control protocol.
- Why no material first-party path remains: judgment-bearing controller paths are explicitly assigned to Hermes/another coordinator, while mission semantic reasoning is assigned to external harnesses. First-party backend paths are execution/state/control primitives.

## S2 — Coordination

- State: —
- Function: no autonomous first-party inter-S1 coordination judgment is established at the sandboxed.sh boundary.
- Disturbance / variety regulated: leases, workspace isolation, mission caps and writer restrictions can prevent conflicts, but the operational S1 actors whose work is being coordinated are external coordinator/harness organizations.
- Decisive decision or feedback right: choose/revise an interference-specific coordination response among distinct autonomous S1 units.
- Decision owner: external coordinator/operator or deterministic backend policy.
- Supporting / enforcement mechanisms: track/attempt ownership, writer flags, resource leases, workspace isolation, mission caps, queues and deterministic fencing/placement rules.
- Closure path: externally supplied ownership/policy → backend validates/enforces leases/isolation → external agents subsequently act under those constraints.
- Why this is / is not agent-owned: deterministic conflict prevention and lease enforcement do not establish first-party agent-owned S2.
- Evidence: [`docs/AGENT_CONTROL_PLANE.md`](https://github.com/Th0rgal/sandboxed.sh/blob/8595836b5f7d23102d1b89b9ac3b59b0842b11a7/docs/AGENT_CONTROL_PLANE.md); [`agents.md`](https://github.com/Th0rgal/sandboxed.sh/blob/8595836b5f7d23102d1b89b9ac3b59b0842b11a7/agents.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: the broader Hermes+sandboxed.sh composition may coordinate projects, but that owner is outside this repository boundary.

### Absence scope

- Surfaces inspected: leases/writer flags, mission/workspace isolation, queues, tracks, compute placement, controller coordination docs.
- Plausible first-party paths checked: writer fencing; cross-project controller coordination; mission parallelism; resource placement; queue arbitration.
- Why no material first-party path remains: first-party backend mechanisms enforce supplied policy/ownership; autonomous coordination judgment remains with coordinator/operator.

## S3 — Inside-and-now control

- State: —
- Function: sandboxed.sh supplies strong current-state and enforcement primitives without owning autonomous whole-system current-control judgment.
- Disturbance / variety regulated: project modes, mission status, resources, leases, failures, grants and operational receipts.
- Decisive decision or feedback right: decide which current commitment should be started, paused, steered, merged, reprioritized or abandoned across the project.
- Decision owner: external controller/operator. The design contract assigns judgment and controller scheduling to Hermes.
- Supporting / enforcement mechanisms: canonical project state, derived modes, grant checks, mission lifecycle, resource/lease enforcement, dashboards, receipts and MCP commands.
- Closure path: current state/receipts → external controller/operator judgment → typed sandboxed.sh command → backend enforcement/mutation → later project/mission state.
- Why this is / is not agent-owned: the backend has authoritative execution/state machinery but the organizational current-control choice is deliberately external.
- Evidence: [`docs/AGENT_CONTROL_PLANE.md`](https://github.com/Th0rgal/sandboxed.sh/blob/8595836b5f7d23102d1b89b9ac3b59b0842b11a7/docs/AGENT_CONTROL_PLANE.md); [`README.md`](https://github.com/Th0rgal/sandboxed.sh/blob/8595836b5f7d23102d1b89b9ac3b59b0842b11a7/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: deterministic mode derivation and grants are current-control support, not autonomous S3 decision ownership.

### Absence scope

- Surfaces inspected: project modes, attention/status projections, grants, decisions, mission controls, leases/resources, dashboard/mobile control surfaces and MCP commands.
- Plausible first-party paths checked: derived project mode; automation scheduler; resource placement; mission stop/steer; grant enforcement; decision ledger.
- Why no material first-party path remains: every discretionary whole-project intervention is selected by external coordinator/operator; backend code computes/enforces bounded consequences.

## S3* — Complementary audit

- State: —
- Function: receipts/evidence/event history improve observability and verification but no independent first-party semantic audit owner is established.
- Disturbance / variety regulated: mission claims can be checked against receipts, immutable handles, acceptance evidence and external state.
- Decisive decision or feedback right: independently challenge an operational claim using complementary access and return corrective findings into control.
- Decision owner: external verifier/controller/operator, not a first-party sandboxed.sh audit actor.
- Supporting / enforcement mechanisms: receipts, evidence classes, event streams, verification status, dashboard/history and proposed verifier-bound acceptance.
- Closure path: evidence becomes available → external verifier/controller judges it → external control decision may issue a new backend command.
- Why this is / is not agent-owned: evidence discipline is not itself an independent audit judgment.
- Evidence: [`docs/AGENT_CONTROL_PLANE.md`](https://github.com/Th0rgal/sandboxed.sh/blob/8595836b5f7d23102d1b89b9ac3b59b0842b11a7/docs/AGENT_CONTROL_PLANE.md); [`README.md`](https://github.com/Th0rgal/sandboxed.sh/blob/8595836b5f7d23102d1b89b9ac3b59b0842b11a7/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: target architecture contains rich verification concepts, but target/design text cannot be credited as a wired autonomous auditor at the frozen runtime.

### Absence scope

- Surfaces inspected: receipts/evidence model, event/history views, mission finish detection, target acceptance/verifier language and dashboard inspection.
- Plausible first-party paths checked: finish detection; evidence reconciliation; receipt verification; history/inspection; review acceptance.
- Why no material first-party path remains: located first-party mechanisms collect/derive evidence; the independent semantic audit judgment and corrective choice remain outside.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party external-and-prospective adaptation judgment loop is established.
- Disturbance / variety regulated: provider health/rate limits, compute availability, reusable knowledge and project observations can influence later execution.
- Decisive decision or feedback right: interpret external/future change, develop adaptation options and choose one to alter present capability.
- Decision owner: external coordinator/operator or maintainers.
- Supporting / enforcement mechanisms: model routing/fallback, provider health checks, fleet placement, Library/skills, project observations, target knowledge-promotion design.
- Closure path: external/runtime distinctions are exposed → external coordinator/configuration chooses adaptation → backend applies routing/config/execution changes.
- Why this is / is not agent-owned: routing and future-facing design primitives do not create an autonomous environment-model/adaptation chooser in sandboxed.sh.
- Evidence: [`README.md`](https://github.com/Th0rgal/sandboxed.sh/blob/8595836b5f7d23102d1b89b9ac3b59b0842b11a7/README.md); [`docs/AGENT_CONTROL_PLANE.md`](https://github.com/Th0rgal/sandboxed.sh/blob/8595836b5f7d23102d1b89b9ac3b59b0842b11a7/docs/AGENT_CONTROL_PLANE.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: “accretive intelligence” is target architecture and assigns judgment outside sandboxed.sh; it is not evidence of first-party S4 closure.

### Absence scope

- Surfaces inspected: model routing, provider health, fleet placement, Library/skills, target knowledge-promotion design, roadmap and project observations.
- Plausible first-party paths checked: adaptive routing; provider fallback; knowledge promotion; project learning; fleet optimization.
- Why no material first-party path remains: mechanisms react deterministically to supplied policy/current health or remain design targets; no first-party autonomous prospective adaptation judgment closes.

## S5 — Policy and identity

- State: —
- Function: grants, policies and authority records constrain execution without first-party ultimate-policy/identity judgment.
- Disturbance / variety regulated: merge authority, budgets, parallelism, action permissions, project modes and resource constraints.
- Decisive decision or feedback right: resolve an identity/ultimate-policy issue and return authoritative policy into later operation.
- Decision owner: operator/parent authority; sandboxed.sh stores/enforces the grant.
- Supporting / enforcement mechanisms: project grants, policy checks, decisions, action authority, Library policies and typed command validation.
- Closure path: parent/operator policy → canonical grant/policy state → sandboxed.sh enforcement → later external coordinator/harness operation.
- Why this is / is not agent-owned: storing and enforcing authority is not deciding the organization's ultimate identity/policy.
- Evidence: [`docs/AGENT_CONTROL_PLANE.md`](https://github.com/Th0rgal/sandboxed.sh/blob/8595836b5f7d23102d1b89b9ac3b59b0842b11a7/docs/AGENT_CONTROL_PLANE.md); [`README.md`](https://github.com/Th0rgal/sandboxed.sh/blob/8595836b5f7d23102d1b89b9ac3b59b0842b11a7/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: no first-party parent-mode notation is published because S1 gate already fails and no autonomous harness organization is admitted at this boundary.

### Absence scope

- Surfaces inspected: project grants, decision records, Library policies, action authority, operator controls and design constitution.
- Plausible first-party paths checked: grant revisions; open decisions; policy/guard promotion; operator approval; project success/abandonment conditions.
- Why no material first-party path remains: ultimate authority remains with the operator/parent organization and the backend enforces returned policy rather than autonomously adjudicating identity.

## Recursion

The assessed recursion is sandboxed.sh as execution/control backend. The wider Paloma organization deliberately splits judgment into Hermes/controllers and bounded execution into sandboxed.sh plus external mission harnesses. Those external actors are not inherited.

## Variety and escalation

sandboxed.sh strongly attenuates execution variety through structured project state, grants, typed commands, isolation, leases, routing, receipts and evidence. But semantic variety and escalated judgment leave the backend: project-level choices go to coordinator/operator and mission-level coding choices go to external harnesses.

## Evidence gaps

No evidence gap requires `?`. The repository explicitly documents the ownership split. Target-architecture features not yet wired are treated as adjacent design evidence, not runtime closure.

## Assessment summary

sandboxed.sh is a substantial mission-execution/control backend, but the autonomous judgment required for first-party S1 is intentionally assigned to external coordinator and mission-harness systems. Proposed terminal disposition: `excluded-no-agentic-vsm`.

**Vector:** — · — · — · — · — · —

---
harness_id: cordum
project_name: Cordum
repository: https://github.com/cordum-io/cordum
review_ref: 5f58ad4e0efd309956310ec27a11ce455226268b
reviewed_at: 2026-10-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-04
status: proposed
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Cordum

## Review boundary

- System in focus: the first-party Cordum Agent Control Plane at frozen revision `5f58ad4e0efd309956310ec27a11ce455226268b`, including API Gateway, Scheduler, Safety Kernel, Workflow Engine, Context Engine, approvals, policy/audit state, CAP runtime primitives, and Cordum Edge enforcement paths.
- Purpose and identity: provide deterministic governance, routing, safety gating, workflow execution control, approvals, observability and evidence around autonomous-agent work.
- Relevant environment: clients/operators, external worker pools, external coding/LLM agents, CAP jobs/results, policy bundles, current fleet/workflow state, approval decisions, Edge tool-call proposals, artifacts and audit evidence.
- Standard-distribution boundary: Cordum core services, SDK/runtime primitives, MCP gateway, Edge hooks/agentd, policy/safety/audit/workflow machinery are inside. User-provided CAP workers, LangChain/LangGraph agents, Claude Code, Codex, other LLM/agent hosts, integration-pack workers and their semantic task loops are external. Demo/example agents are adjacent evidence and not credited as runtime ownership.
- Credited operating / distribution surfaces: `README.md`; `docs/system_overview.md`; `docs/CORE.md`; `core/controlplane/{scheduler,safetykernel,gateway}`; `core/workflow`; `core/contextwindow`; `core/edge`; `sdk/runtime`; approval/audit/policy APIs.
- Adjacent first-party surfaces excluded from ownership: demo agents and examples; integration packs living outside core; repository development CI/tests; external model providers; Claude Code/OpenAI/Codex/LangChain agent internals; operator dashboard decisions; future/roadmap-only features.
- First-party operating / deployment modes considered: CAP job submission/dispatch; deterministic safety evaluation; workflow runs; human approval gates; Edge pre-tool enforcement; context/memory service; audit/evidence export; MCP governance; worker runtime registration.
- Recursion level: the Cordum control plane governing a fleet of external autonomous workers/agents. External workers are operational organizations outside the assessed first-party boundary; the control plane's own routing, policy and lifecycle machinery is not promoted to an autonomous S1 merely because it governs those workers.
- Licensing/provenance note: the repository is public and source-available under its frozen repository license context; this does not affect VSM classification.
- Reviewed revision: `5f58ad4e0efd309956310ec27a11ce455226268b`.
- Observation date: 2026-10-04.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Cordum's current architecture deliberately separates platform core from domain behavior. The code-accurate system overview places API Gateway, Scheduler, Safety Kernel and Workflow Engine in the control plane, while "External Workers (user-provided)" execute job semantics. The core reference makes the same separation explicit: core provides governance and runtime primitives; packages provide workers, connectors, workflows and domain logic.

The workflow engine is a deterministic state machine. Even workflow step types such as `llm`, `http`, `container` and `script` are generic job step types dispatched to worker pools rather than dedicated semantic reasoning handlers in core. Scheduler routing uses configured pool mappings, capability/identity checks and strategies such as least-loaded selection. Safety decisions are policy-kernel verdicts such as allow, deny, require approval, throttle or constraints. Human approval endpoints return operator decisions into execution. Cordum Edge similarly intercepts an external agent's proposed tool action, redacts/maps it, asks the Safety Kernel for a deterministic verdict and returns an allow/deny/approval-shaped response to the host.

The repository contains LLM-governance demos and adapters, but those examples explicitly point external agent/model clients through Cordum's governance path. They do not establish a first-party Cordum model-backed objective→observation→semantic-action loop.

Counterfactual owner test: remove all external workers and agent/model hosts while retaining Cordum's gateway, scheduler, workflow state machine, Safety Kernel, approvals, context store, Edge hooks and audit infrastructure. Cordum can still validate requests, apply configured policy, route/queue work, wait for approvals and record evidence, but it cannot perform the governed open-ended agent task itself. The ordinary S1 semantic decision right therefore remains outside Cordum.

Primary evidence:

- [`README.md`](https://github.com/cordum-io/cordum/blob/5f58ad4e0efd309956310ec27a11ce455226268b/README.md)
- [`docs/system_overview.md`](https://github.com/cordum-io/cordum/blob/5f58ad4e0efd309956310ec27a11ce455226268b/docs/system_overview.md)
- [`docs/CORE.md`](https://github.com/cordum-io/cordum/blob/5f58ad4e0efd309956310ec27a11ce455226268b/docs/CORE.md)
- [`core/workflow/models.go`](https://github.com/cordum-io/cordum/blob/5f58ad4e0efd309956310ec27a11ce455226268b/core/workflow/models.go)
- [`core/controlplane/scheduler/engine.go`](https://github.com/cordum-io/cordum/blob/5f58ad4e0efd309956310ec27a11ce455226268b/core/controlplane/scheduler/engine.go)
- [`core/controlplane/safetykernel/kernel.go`](https://github.com/cordum-io/cordum/blob/5f58ad4e0efd309956310ec27a11ce455226268b/core/controlplane/safetykernel/kernel.go)
- [`docs/edge/README.md`](https://github.com/cordum-io/cordum/blob/5f58ad4e0efd309956310ec27a11ce455226268b/docs/edge/README.md)

## Operational model

A client submits a job or workflow. Cordum validates identity/schema/policy, stores state, evaluates configured safety rules, selects an eligible worker or pauses for approval, and dispatches the job to an external worker. That worker performs the semantic work and returns a result. Cordum then updates state, retries/times out/rolls back according to deterministic lifecycle rules, and records audit/evidence. Edge applies the same separation at tool-call granularity: an external agent chooses a proposed tool action; Cordum evaluates whether it may proceed.

## S1 — Operations

- State: —
- Function: no first-party autonomous operational unit is established for the open-ended agent work Cordum governs.
- Disturbance / variety regulated: heterogeneous jobs, workflows, worker capabilities, policy constraints, approvals, retries and tool-call risks are regulated by the control plane; semantic task variety is absorbed by external workers/agents.
- Decisive decision or feedback right: interpret an open-ended task/environment, choose semantic actions from observations, perform/revise those actions and decide task completion.
- Decision owner: user-provided CAP workers or external Claude Code/LangChain/other agent/model loops.
- Supporting / enforcement mechanisms: gateway; scheduler; workflow state machine; Safety Kernel; Context Engine; SDK runtime; Edge hooks; MCP gateway; approvals; audit.
- Closure path: client submits intent/job → Cordum validates/routes/gates → external worker/agent performs semantic task loop → result/evidence returns → Cordum records and advances deterministic lifecycle state.
- Why this is / is not agent-owned: Cordum core explicitly defines itself as governance + runtime primitives while domain logic lives in packages/workers. Removing external workers leaves no autonomous semantic task loop.
- Evidence: [`docs/system_overview.md`](https://github.com/cordum-io/cordum/blob/5f58ad4e0efd309956310ec27a11ce455226268b/docs/system_overview.md); [`docs/CORE.md`](https://github.com/cordum-io/cordum/blob/5f58ad4e0efd309956310ec27a11ce455226268b/docs/CORE.md); [`README.md`](https://github.com/cordum-io/cordum/blob/5f58ad4e0efd309956310ec27a11ce455226268b/README.md); [`core/workflow/models.go`](https://github.com/cordum-io/cordum/blob/5f58ad4e0efd309956310ec27a11ce455226268b/core/workflow/models.go).
- Basis: explicit + structural negative review.
- Confidence: high.
- Caveats: Cordum can govern autonomous agents and ship SDK primitives for constructing workers, but Methodology 0.3.6 does not inherit those external workers' S1 autonomy into the control plane.

### Absence scope

- Surfaces inspected: architecture docs; API Gateway; Scheduler; Safety Kernel; Workflow Engine; Context Engine; CAP SDK/runtime; MCP gateway; Edge; examples/demos; integration-pack boundary.
- Plausible first-party paths checked: workflow `llm` steps; scheduler routing; context engine; policy remediation; Edge tool interception; Copilot session ingestion; LLM-governance demos.
- Why no material first-party path remains: workflow `llm` is dispatched as a generic worker job; demos/examples place external agents/models behind Cordum; production core contains governance/execution primitives but no standard first-party model-backed semantic task loop.

## S2 — Coordination

- State: —
- Function: no qualifying first-party inter-S1 coordination function is established at the assessed recursion.
- Disturbance / variety regulated: worker load, routing eligibility, workflow dependencies, locks, retries and pool capacity can create scheduling pressure, but the relevant S1 workers are external and core mechanisms primarily route or serialize work.
- Decisive decision or feedback right: choose/revise a coordination response to a specific interference among distinct first-party same-recursion S1 units.
- Decision owner: not established because qualifying first-party S1 units are not established at this boundary.
- Supporting / enforcement mechanisms: least-loaded routing; pool mapping; locks; workflow DAG dependencies; retries/backoff; capability-aware routing; leases/identity fencing.
- Closure path: deterministic routing and workflow rules alter dispatch sequencing, but no first-party autonomous S1 plurality plus interference-specific coordination loop is present.
- Why this is / is not agent-owned: scheduler/queue/DAG machinery is not S2 by itself, and external worker plurality cannot be borrowed into Cordum's first-party ownership.
- Evidence: [`docs/system_overview.md`](https://github.com/cordum-io/cordum/blob/5f58ad4e0efd309956310ec27a11ce455226268b/docs/system_overview.md); [`docs/CORE.md`](https://github.com/cordum-io/cordum/blob/5f58ad4e0efd309956310ec27a11ce455226268b/docs/CORE.md); [`core/controlplane/scheduler/strategy_least_loaded.go`](https://github.com/cordum-io/cordum/blob/5f58ad4e0efd309956310ec27a11ce455226268b/core/controlplane/scheduler/strategy_least_loaded.go).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: a deployment of several CAP workers can form a larger organization with real S2; that organization is outside this standalone Cordum-core boundary.

### Absence scope

- Surfaces inspected: scheduler routing/registry, workflow DAG/fan-out, locks, pool/capability configuration, worker lifecycle and external-worker documentation.
- Plausible first-party paths checked: least-loaded routing; worker pool selection; workflow dependencies; resource fencing; multi-worker dispatch.
- Why no material first-party path remains: mechanisms move/sequence externally owned work and no first-party autonomous S1 units plus specific interference/feedback witness are established.

## S3 — Inside-and-now control

- State: —
- Function: Cordum supplies extensive current-control enforcement, visibility and approval machinery, but no first-party autonomous whole-system current-control decision owner is established.
- Disturbance / variety regulated: current worker health/load, policy violations, unsafe job/tool actions, job timeouts, workflow failures, approval-required states, budgets/constraints and circuit-breaker conditions.
- Decisive decision or feedback right: make discretionary whole-system current choices over commitments/resources/priorities or exceptional interventions on behalf of the governed agent organization.
- Decision owner: configured policy/developer/operator for material choices; deterministic scheduler/Safety Kernel machinery enforces those preselected rules, and approval-required choices are returned to a human/operator.
- Supporting / enforcement mechanisms: Scheduler; Safety Kernel; fleet health; circuit breakers; approval queues; timeouts/retries; cancellation; Edge enforcement; dashboard.
- Closure path: current state is measured → configured deterministic rules or human approval select the disposition → Cordum enforces routing/throttle/deny/approval/cancel transitions → external worker/agent operation changes.
- Why this is / is not agent-owned: hard enforcement is real, but the organizational discretion is either preconfigured/deterministic or external human authority. No first-party autonomous supervisory actor closes S3.
- Evidence: [`docs/system_overview.md`](https://github.com/cordum-io/cordum/blob/5f58ad4e0efd309956310ec27a11ce455226268b/docs/system_overview.md); [`core/controlplane/safetykernel/kernel.go`](https://github.com/cordum-io/cordum/blob/5f58ad4e0efd309956310ec27a11ce455226268b/core/controlplane/safetykernel/kernel.go); [`core/controlplane/scheduler/engine.go`](https://github.com/cordum-io/cordum/blob/5f58ad4e0efd309956310ec27a11ce455226268b/core/controlplane/scheduler/engine.go); [`README.md`](https://github.com/cordum-io/cordum/blob/5f58ad4e0efd309956310ec27a11ce455226268b/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: the deterministic current-control surface is strong operational machinery; it is not published as `C` here because the reviewed distribution does not expose an S3-specific autonomous decision constructor whose missing composition would complete an autonomous S3 owner. It primarily enforces configured/operator decisions over external workers.

### Absence scope

- Surfaces inspected: fleet/scheduler state, Safety Kernel, circuit breakers, retries/timeouts, approvals, workflow control, Edge enforcement, dashboard/operator APIs.
- Plausible first-party paths checked: least-loaded placement; safety verdicts; policy remediation; circuit breaker; approval resolution; cancellation; reconciler; Edge current action gate.
- Why no material first-party path remains: the decisive discretionary owner remains configuration/operator/external organization, while first-party code deterministically executes those rules.

## S3* — Complementary audit

- State: —
- Function: Cordum provides rich audit chains, verification endpoints, evidence export, shadow evaluation and replay-oriented records, but no independent first-party audit judgment with a closed return into current control was established.
- Disturbance / variety regulated: corrupted/inconsistent audit chains, historical policy decisions, Edge evidence, compliance records and shadow-policy differences can be inspected.
- Decisive decision or feedback right: independently challenge an operational claim using complementary access and return findings that govern subsequent current operation.
- Decision owner: deterministic verification/reporting machinery or external operator/auditor; no independent autonomous audit actor is established.
- Supporting / enforcement mechanisms: audit chain verification; compliance export; Edge evidence bundles; policy audit; shadow evaluation; replay/history views.
- Closure path: audit/evidence surfaces expose or verify records → external operator/auditor may choose remediation/policy action; no standard autonomous findings→control loop is first-party closed.
- Why this is / is not agent-owned: tamper verification and evidence export are complementary evidence mechanisms, but deterministic integrity checks/reporting do not by themselves own a semantic audit judgment.
- Evidence: [`core/audit/chain_verify.go`](https://github.com/cordum-io/cordum/blob/5f58ad4e0efd309956310ec27a11ce455226268b/core/audit/chain_verify.go); [`docs/system_overview.md`](https://github.com/cordum-io/cordum/blob/5f58ad4e0efd309956310ec27a11ce455226268b/docs/system_overview.md); [`docs/edge/README.md`](https://github.com/cordum-io/cordum/blob/5f58ad4e0efd309956310ec27a11ce455226268b/docs/edge/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: a parent SOC/compliance organization may close S3* using Cordum evidence; that external audit organization is not part of Cordum's standard first-party runtime.

### Absence scope

- Surfaces inspected: audit chain verification/export, policy audit, Edge evidence export, shadow-policy evaluation, dashboard audit views and operator remediation paths.
- Plausible first-party paths checked: audit verification→policy enforcement; shadow eval→automatic promotion; evidence bundle→current gate; replay→correction.
- Why no material first-party path remains: evidence is verified/exposed but independent semantic judgment and returned corrective decision remain external or manually configured.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party autonomous external-and-prospective adaptation loop is established.
- Disturbance / variety regulated: changing worker capabilities/health, policy bundles, shadow-agent findings, provider/tool integrations and future remediation options can be represented, but adaptation judgment remains configured/operator-owned.
- Decisive decision or feedback right: model relevant external/future change, generate alternative adaptations and select an option that changes present capability.
- Decision owner: operator/developer/maintainer; core uses deterministic policy/simulation/remediation templates.
- Supporting / enforcement mechanisms: policy simulator; shadow evaluation; remediation templates; config/policy publish/rollback; capability registry; pack catalogue; context/memory.
- Closure path: current or historical evidence can be simulated/inspected → operator chooses policy/package/remediation change → Cordum applies configured change. No autonomous outside-and-then chooser closes the loop.
- Why this is / is not agent-owned: policy simulation and deterministic remediation-plan generation are useful future-oriented support, but no first-party autonomous actor owns the adaptation choice.
- Evidence: [`docs/CORE.md`](https://github.com/cordum-io/cordum/blob/5f58ad4e0efd309956310ec27a11ce455226268b/docs/CORE.md); [`README.md`](https://github.com/cordum-io/cordum/blob/5f58ad4e0efd309956310ec27a11ce455226268b/README.md); [`core/controlplane/safetykernel/shadow_eval.go`](https://github.com/cordum-io/cordum/blob/5f58ad4e0efd309956310ec27a11ce455226268b/core/controlplane/safetykernel/shadow_eval.go).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: packages or external agents can use Cordum's data to implement S4; generic composability is not a positive first-party S4 state.

### Absence scope

- Surfaces inspected: policy simulation/shadow evaluation, remediation machinery, pack catalogue, capability registry, context engine, Edge shadow findings and configuration lifecycle.
- Plausible first-party paths checked: automatic policy evolution; shadow finding remediation; capability adaptation; pack selection; retained memory.
- Why no material first-party path remains: core generates deterministic simulations/templates or exposes state; selection/promotion/adaptation remains external.

## S5 — Policy and identity

- State: —
- Function: Cordum strongly enforces governance policy and human approval, but no first-party identity/ultimate-policy decision loop is established.
- Disturbance / variety regulated: enterprise risk policy, authorization, tenant boundaries, approval requirements, capability restrictions and safety constraints.
- Decisive decision or feedback right: resolve an identity- or ultimate-policy-level conflict for the governed organization and return that authoritative decision into subsequent operation.
- Decision owner: operator/enterprise parent/configuration; Cordum validates and enforces the resulting policy.
- Supporting / enforcement mechanisms: declarative policy bundles; RBAC; approvals; policy publish/rollback; Safety Kernel; tenant/identity enforcement; Edge managed settings.
- Closure path: externally selected policy/approval authority → Cordum policy/configuration state → enforcement over later jobs/tool actions.
- Why this is / is not agent-owned: a policy engine, approval gate or security constitution does not establish S5 unless the identity-level judgment path itself is present and closed.
- Evidence: [`README.md`](https://github.com/cordum-io/cordum/blob/5f58ad4e0efd309956310ec27a11ce455226268b/README.md); [`docs/CORE.md`](https://github.com/cordum-io/cordum/blob/5f58ad4e0efd309956310ec27a11ce455226268b/docs/CORE.md); [`core/controlplane/safetykernel/global_policy.go`](https://github.com/cordum-io/cordum/blob/5f58ad4e0efd309956310ec27a11ce455226268b/core/controlplane/safetykernel/global_policy.go).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: an enterprise operating Cordum may provide the parent S5; standalone Cordum only supplies the enforcement/governance substrate.

### Absence scope

- Surfaces inspected: policy bundles, Safety Kernel, RBAC/auth, approvals, policy lifecycle, Edge managed settings, governance docs and operator controls.
- Plausible first-party paths checked: policy publish/rollback; human approvals; enterprise policy hierarchy; global invariants; governance repository rules.
- Why no material first-party path remains: located mechanisms express/enforce ordinary governance constraints selected elsewhere; no first-party identity-level issue→ultimate authority→returned policy loop is supplied.

## Distributed parent arrangement

Cordum is designed to sit beneath enterprise operators and external agent organizations. Those parents may use Cordum as a strong enforcement substrate for current control, audit, adaptation or policy, but the standalone assessment does not import their decision owners.

## Self-hosted and non-human modes

Self-hosting changes deployment ownership but not function ownership. Cordum continues to provide deterministic governance and execution-control primitives around external agents/workers. No supported first-party non-human mode supplies the missing autonomous S1 semantic task loop.

## Recursion

The focal recursion is the Cordum control plane. External CAP workers and governed agent hosts are separate operational systems. Workflow steps, queues, scheduler entries and tool-call events are subordinate control/execution artifacts rather than first-party autonomous S1 units.

## Variety and escalation

Cordum substantially attenuates operational risk variety through policy checks, schema/identity enforcement, routing, retries, timeouts, approvals, circuit breakers and Edge gates. High-risk or approval-required events can escalate to human authority. This is a capable governance substrate, but regulatory machinery around autonomous agents is not itself evidence that Cordum owns those agents' semantic operational loop.

## Evidence gaps

No evidence gap requires `?` at the frozen revision. The repository's own architecture repeatedly separates core governance/runtime primitives from external/user-provided worker/domain logic, and the reviewed production paths do not contain a first-party autonomous model-backed action-selection loop.

## Assessment summary

Cordum is a substantial agent-control-plane and governance system, but at the frozen revision the autonomous operational task loop remains in external workers and agent/model hosts. Proposed terminal disposition: `excluded-no-agentic-vsm`.

**Vector:** — · — · — · — · — · —

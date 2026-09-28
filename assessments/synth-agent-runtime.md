---
harness_id: synth-agent-runtime
project_name: Synth Agent Runtime
repository: https://github.com/taituo/synth-agent-runtime
review_ref: 0ca8075281039d934fce8751ddd8b006ddc7de8d
reviewed_at: 2026-09-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-29
status: proposed
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Synth Agent Runtime

## Review boundary

- System in focus: the first-party `taituo/synth-agent-runtime` runtime/control-plane distribution at pinned revision `0ca8075281039d934fce8751ddd8b006ddc7de8d`: `AgentRuntime`, durable state, mailbox, leases/fencing, command/effect coordination, recovery, execution brokerage, inference gateway, `Supervisor`, and the bundled Pi adapter.
- Purpose and identity: run externally supplied AI-agent engines as durable distributed workloads with persistence, ownership/fencing, recovery, isolation, steering, effects, routing, and orchestration primitives.
- Relevant environment: embedding harnesses/workflow systems, externally supplied `AgentEngine`s, Pi/OpenCode-style clients, model providers, operators, PostgreSQL, Kubernetes/gVisor, tools and effect targets.
- Standard-distribution boundary: repository-owned runtime/control-plane code is inside. The substantive reasoning/action engine supplied through `AgentEngine`, Pi `AgentSession`, other harnesses, model providers, and downstream effect systems remain environment.
- Credited operating / distribution surfaces: `src/runtime/*`, `src/control-plane/*`, `src/orchestration/supervisor.ts`, `src/execution/*`, `src/inference/*`, `src/world/*`, `src/adapters/pi/pi-engine.ts`, and distributed/recovery/transaction documentation.
- Adjacent first-party surfaces excluded from ownership: tests, examples with inline/mock engines, release/audit docs, live-proof scripts and integration fixtures; they corroborate runtime behavior but do not supply an autonomous product actor.
- First-party operating / deployment modes considered: local and PostgreSQL-backed runtime, leased/fenced runs, mailbox steering, supervisor child/reviewer construction, command/effect reconciliation, synthetic/Kubernetes execution, inference gateway and Pi adapter.
- Recursion level: one Synth runtime/control plane hosting logical agent instances. Externally supplied engines may themselves be viable systems but do not donate ownership.
- Reviewed revision: `0ca8075281039d934fce8751ddd8b006ddc7de8d`.
- Observation date: 2026-09-29.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Synth explicitly positions itself as “Infrastructure for running AI agents as durable, distributed workloads” and states that it is **not an agent framework, prompt library, or new model SDK**. `AgentEngine` is an interface supplied to `AgentRuntime.spawn()`, and `AgentRuntime.run()` delegates the substantive turn to `agent.engine.run(...)` while owning lifecycle, mailbox, workspace, effect and durability mechanics. The bundled `PiAgentEngine` is a structural adapter around a caller-created Pi-like session; `Supervisor` similarly requires caller-supplied child/reviewer engines.

The repository nevertheless provides substantial infrastructure: durable identity/state, mailbox/ACK, leases and monotonic fencing, crash recovery, transactional semantic-exposure rules, world CAS, command/effect reconciliation, execution brokerage, sandbox lifecycle and inference routing. Those can support VSM functions in a wider composed organization, but they do not supply the autonomous S1 actor required for Index inclusion at this repository-relative boundary.

Primary evidence: [`README.md`](https://github.com/taituo/synth-agent-runtime/blob/0ca8075281039d934fce8751ddd8b006ddc7de8d/README.md), [`src/runtime/agent-engine.ts`](https://github.com/taituo/synth-agent-runtime/blob/0ca8075281039d934fce8751ddd8b006ddc7de8d/src/runtime/agent-engine.ts), [`src/runtime/agent-runtime.ts`](https://github.com/taituo/synth-agent-runtime/blob/0ca8075281039d934fce8751ddd8b006ddc7de8d/src/runtime/agent-runtime.ts), [`src/adapters/pi/pi-engine.ts`](https://github.com/taituo/synth-agent-runtime/blob/0ca8075281039d934fce8751ddd8b006ddc7de8d/src/adapters/pi/pi-engine.ts), [`src/orchestration/supervisor.ts`](https://github.com/taituo/synth-agent-runtime/blob/0ca8075281039d934fce8751ddd8b006ddc7de8d/src/orchestration/supervisor.ts), and [`docs/ARCHITECTURE.md`](https://github.com/taituo/synth-agent-runtime/blob/0ca8075281039d934fce8751ddd8b006ddc7de8d/docs/ARCHITECTURE.md).

## Operational model

Synth durably manages an `AgentInstance`, but the task-level decision right belongs to its injected `AgentEngine`. On a run Synth prepares mailbox/context, transitions durable state and invokes the engine; that engine interprets the objective/observations and chooses substantive work. Bundled examples/tests define inline or mock engines, confirming a construction seam rather than a shipped autonomous standard mode.

The proposed terminal classification is therefore `excluded-no-agentic-vsm`. A wider Synth + Pi/custom-agent deployment may have positive states, but that is a different system-in-focus.

## S1 — Operations

- State: —
- Function: no first-party autonomous operational unit closes a goal-directed decision/action/feedback loop inside Synth itself.
- Disturbance / variety regulated: Synth regulates reliable execution, ownership, persistence, delivery and recovery; open-ended task variety is handled by the injected engine.
- Decisive decision or feedback right: interpret objectives/observations and choose the next substantive task action.
- Decision owner: external/caller-supplied `AgentEngine` or external Pi/harness session.
- Supporting / enforcement mechanisms: `AgentRuntime`, workspaces, durability, mailbox, execution broker, inference gateway, leases/fencing and recovery.
- Closure path: caller injects engine → Synth invokes it with durable context → engine chooses/executes task work → Synth records state/output → subsequent task discretion remains with the engine.
- Why this is / is not agent-owned: the core API requires the autonomous engine to be supplied from outside the runtime boundary.
- Evidence: [`README.md`](https://github.com/taituo/synth-agent-runtime/blob/0ca8075281039d934fce8751ddd8b006ddc7de8d/README.md); [`src/runtime/agent-engine.ts`](https://github.com/taituo/synth-agent-runtime/blob/0ca8075281039d934fce8751ddd8b006ddc7de8d/src/runtime/agent-engine.ts); [`src/runtime/agent-runtime.ts`](https://github.com/taituo/synth-agent-runtime/blob/0ca8075281039d934fce8751ddd8b006ddc7de8d/src/runtime/agent-runtime.ts); [`src/adapters/pi/pi-engine.ts`](https://github.com/taituo/synth-agent-runtime/blob/0ca8075281039d934fce8751ddd8b006ddc7de8d/src/adapters/pi/pi-engine.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: a composed deployment with a real autonomous engine can establish S1 for the wider system.

### Absence scope

- Surfaces inspected: README/architecture, `AgentEngine`, `AgentRuntime`, Pi adapter, Supervisor, examples/tests, execution/inference/control-plane and recovery paths.
- Plausible first-party paths checked: `AgentRuntime.run()` as agent loop; Pi adapter as reasoning; Supervisor as operational actor; examples as shipped actors; inference gateway as task reasoner.
- Why no material first-party path remains: substantive task decisions are delegated to an injected engine/session; the gateway routes inference rather than deciding task actions.

## S2 — Coordination

- State: —
- Function: no first-party S2-specific loop is established among internally owned autonomous S1 units.
- Disturbance / variety regulated: mailbox duplication, cross-replica ownership races, project revision conflicts and concurrent runtime activity are distributed-systems disturbances, not evidenced inter-S1 operational oscillation.
- Decisive decision or feedback right: choose a coordination response to a specific conflict among distinct S1 units and feed it back into later S1 behavior.
- Decision owner: none established inside Synth; external engines own operational behavior while runtime mechanisms enforce deterministic consistency.
- Supporting / enforcement mechanisms: mailbox/ACK, project CAS, leases/fencing, relation graph, task state and Supervisor delegation.
- Closure path: deterministic mechanisms can serialize ownership/reject stale writes/deliver messages, but no S2-specific autonomous coordination judgment closes.
- Why this is / is not agent-owned: generic communication, locking and orchestration primitives do not meet the Methodology's S2 constructor threshold.
- Evidence: [`docs/ARCHITECTURE.md`](https://github.com/taituo/synth-agent-runtime/blob/0ca8075281039d934fce8751ddd8b006ddc7de8d/docs/ARCHITECTURE.md); [`src/orchestration/supervisor.ts`](https://github.com/taituo/synth-agent-runtime/blob/0ca8075281039d934fce8751ddd8b006ddc7de8d/src/orchestration/supervisor.ts); [`src/core/types.ts`](https://github.com/taituo/synth-agent-runtime/blob/0ca8075281039d934fce8751ddd8b006ddc7de8d/src/core/types.ts).
- Basis: structural negative search.
- Confidence: high.
- Caveats: a composed multi-agent application can build S2 with these primitives; general expressiveness is insufficient for `C`.

### Absence scope

- Surfaces inspected: mailbox, leases/fencing, project CAS/world state, relations, Supervisor paths, task lifecycle and distributed-state docs.
- Plausible first-party paths checked: mailbox as S2; leases/CAS as anti-conflict S2; fan-out as coordination; dependencies/relations as S2.
- Why no material first-party path remains: no S2-specific autonomous decision/feedback path over first-party S1 units is shipped.

## S3 — Inside-and-now control

- State: —
- Function: strong current-execution control exists, but no autonomous whole-system S3 decision owner is supplied for an internal operational organization.
- Disturbance / variety regulated: stale ownership, worker failure, duplicate commands, uncertain effects, resource class and cancellation/recovery conditions.
- Decisive decision or feedback right: make discretionary whole-system choices over resources, commitments, priorities, constraints, accountability, synergy or intervention.
- Decision owner: external caller/operator/embedding agent; Synth enforces configured leases, fencing, command state and execution policy.
- Supporting / enforcement mechanisms: `LeasedAgentRunner`, lease/fence store, `CommandCoordinator`, execution broker/resource classes, cancellation and recovery.
- Closure path: caller selects work/policy/engine → Synth serializes/executes/recovers it under configured rules → state returns; Synth does not independently reprioritize commitments.
- Why this is / is not agent-owned: enforcement authority is not the organizational current-control decision right.
- Evidence: [`docs/ARCHITECTURE.md`](https://github.com/taituo/synth-agent-runtime/blob/0ca8075281039d934fce8751ddd8b006ddc7de8d/docs/ARCHITECTURE.md); [`src/control-plane/agent-runner.ts`](https://github.com/taituo/synth-agent-runtime/blob/0ca8075281039d934fce8751ddd8b006ddc7de8d/src/control-plane/agent-runner.ts); [`src/control-plane/command-coordinator.ts`](https://github.com/taituo/synth-agent-runtime/blob/0ca8075281039d934fce8751ddd8b006ddc7de8d/src/control-plane/command-coordinator.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: leases/fencing/reconciliation are strong S3-supporting machinery, not S3 ownership.

### Absence scope

- Surfaces inspected: leased runner, command coordinator, execution broker, world/task state, Supervisor, recovery/cancellation and distributed deployment docs.
- Plausible first-party paths checked: lease owner as S3; command coordinator as S3; Supervisor as manager; execution policy as resource bargaining; recovery as intervention.
- Why no material first-party path remains: these enforce configured semantics or expose composition seams; no autonomous whole-system current discretion is supplied.

## S3* — Complementary audit

- State: —
- Function: no first-party complementary and materially independent audit loop challenges an internal S1's operational claims.
- Disturbance / variety regulated: uncertain effects/commands, crash aftermath and runtime correctness can be checked/reconciled.
- Decisive decision or feedback right: independently inspect operational reality, form an audit judgment and return findings into control.
- Decision owner: none established; deterministic probes/tests and caller-provided reviewer engines perform narrower checks.
- Supporting / enforcement mechanisms: `EffectReconciler`, command reconciliation callbacks, receipts, recovery records, live/release tests and `Supervisor.assignReviewer()`.
- Closure path: configured logic can reconcile uncertain state, or a caller can provide a reviewer engine; no shipped independent audit actor challenges/corrects internal S1 operation.
- Why this is / is not agent-owned: transactional reconciliation and development tests are not S3*; reviewer construction still requires external `reviewerEngine`.
- Evidence: [`src/control-plane/effect-reconciler.ts`](https://github.com/taituo/synth-agent-runtime/blob/0ca8075281039d934fce8751ddd8b006ddc7de8d/src/control-plane/effect-reconciler.ts); [`src/control-plane/command-coordinator.ts`](https://github.com/taituo/synth-agent-runtime/blob/0ca8075281039d934fce8751ddd8b006ddc7de8d/src/control-plane/command-coordinator.ts); [`src/orchestration/supervisor.ts`](https://github.com/taituo/synth-agent-runtime/blob/0ca8075281039d934fce8751ddd8b006ddc7de8d/src/orchestration/supervisor.ts); [`docs/RECOVERY.md`](https://github.com/taituo/synth-agent-runtime/blob/0ca8075281039d934fce8751ddd8b006ddc7de8d/docs/RECOVERY.md).
- Basis: structural negative search.
- Confidence: high.
- Caveats: reviewer/reconciliation primitives can support S3* in a wider composed system.

### Absence scope

- Surfaces inspected: effect/command reconciliation, receipts, recovery, trace/live/release-audit surfaces, reviewer assignment and tests.
- Plausible first-party paths checked: effect reconciliation as S3*; crash recovery as audit; release/live proof as operational audit; `assignReviewer` as autonomous reviewer.
- Why no material first-party path remains: reconciliation is deterministic/effect-specific, development tests are adjacent, and reviewer execution requires a supplied engine.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party outside-and-future sensing/adaptation loop changes Synth's present capability.
- Disturbance / variety regulated: provider health/routing and infrastructure failures are observed for present reliability; future runtime evolution remains developer-authored.
- Decisive decision or feedback right: interpret external/future change, generate/select adaptation options and return one into current capability.
- Decision owner: developers/operators or embedding systems; no autonomous adaptation actor is supplied.
- Supporting / enforcement mechanisms: provider health/affinity, observability/history, live-proof data, configurable inference routes and deployment adapters.
- Closure path: observations can inform later external code/config changes, but no shipped actor converts prospective distinctions into persistent capability changes.
- Why this is / is not agent-owned: routing health/recovery are present-operation regulation; history/roadmap are not S4 without prospective adaptation closure.
- Evidence: [`docs/ARCHITECTURE.md`](https://github.com/taituo/synth-agent-runtime/blob/0ca8075281039d934fce8751ddd8b006ddc7de8d/docs/ARCHITECTURE.md); [`README.md`](https://github.com/taituo/synth-agent-runtime/blob/0ca8075281039d934fce8751ddd8b006ddc7de8d/README.md); [`docs/ROADMAP.md`](https://github.com/taituo/synth-agent-runtime/blob/0ca8075281039d934fce8751ddd8b006ddc7de8d/docs/ROADMAP.md).
- Basis: structural negative search.
- Confidence: high.
- Caveats: embedding agents can implement adaptation with Synth primitives; that logic is external.

### Absence scope

- Surfaces inspected: inference routing/health, observability/history, recovery, deployment docs, roadmap/release/audit material and orchestration seams.
- Plausible first-party paths checked: provider health as sensing; recovery as adaptation; persisted world/history as learning; roadmap/live proof as S4.
- Why no material first-party path remains: these regulate present reliability or inform external developers; no runtime-owned prospective adaptation judgment installs a capability change.

## S5 — Policy and identity

- State: —
- Function: no first-party identity/ultimate-policy deliberation and closure path governs Synth at the assessed runtime boundary.
- Disturbance / variety regulated: definitions, execution policies, inference profiles and tenant/provider constraints bound runs, but substantive policy is configured externally.
- Decisive decision or feedback right: decide enduring identity, principles, authority boundaries or authoritative resolution of an identity-level conflict.
- Decision owner: external developers/operators/embedding organization.
- Supporting / enforcement mechanisms: `AgentDefinition`, execution/resource policy, tenant/inference policy, durable project fields, fencing and effect boundaries.
- Closure path: external authority configures definitions/policy → Synth enforces them → operation is bounded; no identity-level issue reaches a first-party ultimate authority and returns as a revised governing decision.
- Why this is / is not agent-owned: static/configured policy and hard enforcement are not S5 ownership.
- Evidence: [`src/core/types.ts`](https://github.com/taituo/synth-agent-runtime/blob/0ca8075281039d934fce8751ddd8b006ddc7de8d/src/core/types.ts); [`src/runtime/agent-runtime.ts`](https://github.com/taituo/synth-agent-runtime/blob/0ca8075281039d934fce8751ddd8b006ddc7de8d/src/runtime/agent-runtime.ts); [`README.md`](https://github.com/taituo/synth-agent-runtime/blob/0ca8075281039d934fce8751ddd8b006ddc7de8d/README.md).
- Basis: structural negative search.
- Confidence: high.
- Caveats: an embedding parent may retain legitimate S5; that wider organization is outside this boundary.

### Absence scope

- Surfaces inspected: definitions, inference/execution policy, project state, tenant/provider policy, configuration, README/architecture and operator/deployment surfaces.
- Plausible first-party paths checked: system prompt as identity; execution policy as S5; project objective as S5; operator config as parent governance; safety boundaries as ultimate policy.
- Why no material first-party path remains: these are supplied constraints/enforcement surfaces, not identity-level deliberation with legitimate ultimate-policy ownership and return.

## Recursion, variety, and escalation

Synth supports nested/supervised agent graphs and durable logical agents, but spawning/forking/relations do not establish recursive viability by themselves. Failure, uncertain effects, lost leases and stale generations have explicit recovery/reconciliation paths; those are valuable variety-attenuation mechanisms but remain infrastructure/support rather than S2-S5 ownership.

## Terminal outcome

Proposed canonical outcome: `excluded-no-agentic-vsm`.

The frozen standard distribution intentionally leaves the decisive task-level agent loop behind the injected `AgentEngine`/external-harness boundary. Under Profile 0.2.4 / Methodology 0.3.6, Synth therefore does not establish the first-party autonomous S1 required for Index inclusion. Its durability, orchestration, control, reconciliation and policy machinery remains substantial support/construction infrastructure.

## Evidence boundaries / caveats

- Pinned to `0ca8075281039d934fce8751ddd8b006ddc7de8d`; later upstream changes are not imported.
- External Pi/OpenCode/custom-agent reasoning does not donate ownership to Synth merely because Synth runs/adapts it.
- Inline/mock engines in examples/tests demonstrate the construction seam, not a shipped autonomous standard mode.
- Deterministic leases, fencing, CAS, command coordination, reconciliation, recovery and sandbox controls are separated from organizational decision ownership.
- A wider Synth + autonomous-engine deployment may warrant a separate assessment.

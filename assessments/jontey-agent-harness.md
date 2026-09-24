---
harness_id: jontey-agent-harness
project_name: Agent Harness
repository: https://github.com/jontey/agent-harness
review_ref: db6297cb776f6181310d3533c0ebf22d35e66de4
reviewed_at: 2026-09-24
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-24
status: excluded-no-agentic-vsm
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Agent Harness

## Review boundary

- System in focus: the first-party `jontey/agent-harness` portable orchestration/control layer at pinned revision `db6297cb776f6181310d3533c0ebf22d35e66de4`: controller, lead lease/authority protocol, task/context/state store, policy/model routing, worker process lifecycle, worktree/sandbox enforcement, steering/resume/handoff, LiteLLM proxy/accounting, and auditable runtime records.
- Purpose and identity: provide a portable control layer through which an accountable lead can delegate engineering work to separately running coding-agent harnesses while preserving durable orchestration state, policy, isolation, route evidence, continuation and recovery.
- Relevant environment: user requests; repositories/worktrees; lead agents running in OpenCode, Codex, DeepSeek Harness or another compatible harness; delegated Codex CLI / DeepSeek Harness workers; LiteLLM/model deployments; Git and the host operating system.
- Standard-distribution boundary: first-party controller/CLI, state/protocol, policy, leases, workspace/sandbox management, proxy/routing evidence and worker-launch adapters are inside. Codex CLI, DeepSeek Harness, OpenCode, LiteLLM/model deployments and the lead/worker reasoning loops they host remain external systems/services where they make substantive autonomous decisions.
- Credited operating / distribution surfaces: `src/controller.ts`, `src/worker.ts`, `src/policy.ts`, `src/leases.ts`, `src/store.ts`, `src/proxy.ts`, `src/cli.ts`, `src/types.ts`, the task/state protocol, example policy, and deterministic controller/runtime tests.
- Adjacent first-party surfaces excluded from ownership: architecture/implementation/validation planning that describes future roles beyond the implemented first release; examples and tests used as corroborating evidence; contributor/development activity. These surfaces do not donate an autonomous operational owner to the shipped controller boundary.
- First-party operating / deployment modes considered: local macOS CLI/controller deployment; Codex CLI worker mode; DeepSeek Harness SDK subprocess mode; lead takeover/release through the first-party lead lease; steering, resume and cross-harness handoff; read-only explorer and writable implementer roles.
- Recursion level: the portable orchestration/control layer itself. A lead or delegated Codex/DeepSeek/OpenCode agent may independently be a viable agent system at another recursion, but that external harness is not imported into this repository-relative system-in-focus.
- Reviewed revision: `db6297cb776f6181310d3533c0ebf22d35e66de4`.
- Observation date: 2026-09-24.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

The repository explicitly separates orchestration from model execution. Its README describes Agent Harness as a portable orchestration layer for lead agents and delegated workers. The architecture document states that the lead decides what work is needed while the controller validates delegation, creates durable task records, prepares isolated workspaces and launches the selected harness. The lead itself may run in OpenCode, Codex, DeepSeek Harness or another supported harness.

The first release implements two task roles, `code-explorer` and `code-implementer`. `src/types.ts` limits executable harnesses to Codex, DeepSeek and a deterministic test fake. `src/controller.ts` owns project initialization, the active-lead lease, policy checks, task IDs, worktree creation, durable request/context/event state, writer/resume leases, worker launch, status reconciliation and recovery. These are substantial first-party control mechanisms.

Actual model-driven work is performed outside that controller. `src/worker.ts` starts Codex CLI as a subprocess or instantiates the external DeepSeek Harness SDK, passes the constructed prompt into that runtime, then captures the external runtime's final response, native session identifier and model-route evidence. The first-party worker wrapper does not contain its own model/tool reasoning loop.

The controller can steer, cancel, resume or hand off an attempt, and the state protocol preserves checkpoints and lineage across harnesses. Policy constrains roles, harnesses, model aliases, filesystem/network/tool permissions and writer concurrency. Those mechanisms determine which external runtime may act and under what constraints; they do not replace the runtime's substantive task-level decision/action loop.

Primary evidence:

- [`README.md`](https://github.com/jontey/agent-harness/blob/db6297cb776f6181310d3533c0ebf22d35e66de4/README.md) — portable orchestration-layer identity, accountable external lead, supported first-release workers and CLI operations.
- [`docs/architecture.md`](https://github.com/jontey/agent-harness/blob/db6297cb776f6181310d3533c0ebf22d35e66de4/docs/architecture.md) — explicit orchestration/model-execution separation, lead responsibility, controller responsibilities, workflow, correction and handoff model.
- [`src/controller.ts`](https://github.com/jontey/agent-harness/blob/db6297cb776f6181310d3533c0ebf22d35e66de4/src/controller.ts) — lead lease, policy enforcement, task/worktree lifecycle, attempt launch, writer/resume leases, status/recovery and controller state.
- [`src/worker.ts`](https://github.com/jontey/agent-harness/blob/db6297cb776f6181310d3533c0ebf22d35e66de4/src/worker.ts) — execution is delegated to Codex CLI or the DeepSeek Harness SDK; first-party code wraps, launches and records those external runtimes.
- [`src/types.ts`](https://github.com/jontey/agent-harness/blob/db6297cb776f6181310d3533c0ebf22d35e66de4/src/types.ts) — implemented first-release role/harness contract.
- [`docs/protocol.md`](https://github.com/jontey/agent-harness/blob/db6297cb776f6181310d3533c0ebf22d35e66de4/docs/protocol.md) — durable task/session/checkpoint and steering/handoff protocol.
- [`config/policy.example.yaml`](https://github.com/jontey/agent-harness/blob/db6297cb776f6181310d3533c0ebf22d35e66de4/config/policy.example.yaml) — first-party role/model/harness/permission constraints.

## Operational model

A user initializes a project and an active lead identity. That lead, itself running in an external agent harness, decides what work is needed and submits a delegation. The first-party controller validates the request, checks policy, allocates task state and a workspace, acquires required leases, and launches a first-party worker wrapper. The wrapper then invokes Codex CLI or DeepSeek Harness, which performs the substantive model-driven task loop. Results, checkpoints, events and route evidence return to durable first-party state for the lead to inspect and decide what to do next.

The counterfactual owner test is decisive. Remove Codex/DeepSeek/OpenCode or an equivalent external lead/worker harness while leaving the controller, policy, leases, state, sandbox, proxy and lifecycle machinery intact. The remaining first-party system can validate, persist, allocate, launch, reconcile and enforce, but it no longer contains an autonomous actor that interprets the engineering task and chooses the next substantive model/tool/action. The operational decision/action loop therefore closes outside the assessed boundary.

Under Methodology 0.3.6, an included autonomous harness must establish its operational S1 rather than inheriting operation from an adjacent runtime. The terminal outcome is therefore `excluded-no-agentic-vsm`, not an included constructor vector built from control-plane primitives.

## S1 — Operations

- State: —
- Function: no first-party autonomous operational agent loop is established at the declared Agent Harness controller boundary.
- Disturbance / variety regulated: first-party code regulates orchestration variety — task identity, worker runtime selection, workspaces, permissions, concurrency, continuation, recovery and route evidence — while substantive engineering-task variety is interpreted and acted on by the external lead/worker harness.
- Decisive decision or feedback right: choosing substantive next task/model-tool actions that produce the engineering outcome belongs to the external lead or Codex/DeepSeek worker runtime.
- Decision owner: no first-party autonomous S1 owner established; the relevant operational decision maker is external to the assessed boundary.
- Supporting / enforcement mechanisms: controller lifecycle, policy checks, lead/writer/resume leases, task store, worktrees, sandbox profile, LiteLLM proxy, steering/resume/handoff and checkpoint persistence.
- Closure path: external lead chooses delegation → first-party controller validates/launches → external Codex/DeepSeek harness performs autonomous task work → first-party wrapper records result/checkpoint → external lead reviews and chooses the next action. The substantive operation closes through external agent runtimes.
- Boundary reachability: not applicable to a positive state; no first-party autonomous operational owner is reachable in the supported controller mode without importing an adjacent runtime.
- Why this is / is not agent-owned: the repository's own architecture assigns task-level discretion to lead/worker agents hosted by other harnesses. First-party code launches and constrains those actors but does not implement their reasoning/tool loop.
- Evidence: [`README.md`](https://github.com/jontey/agent-harness/blob/db6297cb776f6181310d3533c0ebf22d35e66de4/README.md), [`docs/architecture.md`](https://github.com/jontey/agent-harness/blob/db6297cb776f6181310d3533c0ebf22d35e66de4/docs/architecture.md), [`src/worker.ts`](https://github.com/jontey/agent-harness/blob/db6297cb776f6181310d3533c0ebf22d35e66de4/src/worker.ts), [`src/types.ts`](https://github.com/jontey/agent-harness/blob/db6297cb776f6181310d3533c0ebf22d35e66de4/src/types.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: Codex, DeepSeek Harness, OpenCode or a future bundled first-party agent loop may independently qualify at a different boundary. This finding is only for the pinned first-party portable controller distribution.

### Absence scope

- Surfaces inspected: README, architecture/protocol documentation, controller, worker wrapper, type/role contract, policy, leases/state/proxy lifecycle and tests/examples used to confirm supported modes.
- Plausible first-party paths checked: controller task execution; worker process; lead lease; fake harness; steering/resume/handoff; policy/runtime selection; durable checkpoint recovery.
- Why no material first-party path remains: every non-test model-driven execution path delegates substantive autonomous work to Codex CLI or DeepSeek Harness, and the accountable lead is likewise supplied by another harness.

## S2 — Coordination

- State: —
- Function: no qualifying first-party S2 relation is established because the assessed boundary does not contain two distinct first-party S1 operational units.
- Disturbance / variety regulated: writer collision is structurally regulated, but it occurs among externally hosted worker operations and is enforced by the controller rather than establishing an internal population of first-party autonomous S1 units.
- Decisive decision or feedback right: the controller deterministically refuses/confines conflicting writer ownership according to first-party lease rules; no autonomous S2-specific coordination discretion over first-party S1 units is established.
- Decision owner: no qualifying first-party S2 owner at this recursion.
- Supporting / enforcement mechanisms: one-writer leases, separate worktrees, task state, sequencing and lead-directed delegation.
- Closure path: writer lease/worktree enforcement can prevent concurrent modification, but the affected substantive workers remain external agent runtimes; no internal S1-population coordination loop is available for canonical S2 credit.
- Boundary reachability: not applicable to a positive state.
- Why this is / is not agent-owned: the controller's collision-prevention machinery is first-party and functionally relevant, but the operational units whose behavior it constrains are not first-party autonomous S1 units at this system boundary.
- Evidence: [`docs/architecture.md`](https://github.com/jontey/agent-harness/blob/db6297cb776f6181310d3533c0ebf22d35e66de4/docs/architecture.md), [`src/controller.ts`](https://github.com/jontey/agent-harness/blob/db6297cb776f6181310d3533c0ebf22d35e66de4/src/controller.ts).
- Basis: structural absence after boundary test.
- Confidence: high.
- Caveats: at a wider assembled deployment boundary containing the external workers, the writer-lease/worktree mechanism may contribute to an S2 mapping. That is a different system-in-focus and is not inherited here.

### Absence scope

- Surfaces inspected: concurrency design, writer/resume/lead leases, worktree allocation, delegation lifecycle and task state.
- Plausible first-party paths checked: one-writer enforcement, separate worker worktrees, parallel read-only workers, handoff and lead-directed task sequencing.
- Why no material first-party path remains: the concrete collision attenuation path regulates workers whose autonomous operations live in external harnesses; the first-party controller does not itself provide the distinct autonomous S1 units required for positive S2 at this recursion.

## S3 — Inside-and-now control

- State: —
- Function: the repository supplies substantial present-time control machinery, but no first-party autonomous S3 organizational owner is established over an internally owned S1 organization.
- Disturbance / variety regulated: current task lifecycle, role/model/harness permissions, workspace exclusivity, stalled workers, route identity and continuation/recovery.
- Decisive decision or feedback right: the external lead decides what work to delegate, what role/harness/model to use, whether worker output is sufficient, and what next action or correction is required. The controller validates and enforces those choices.
- Decision owner: external lead for the discretionary whole-task control decisions; deterministic first-party runtime for enforcement/reconciliation only.
- Supporting / enforcement mechanisms: policy engine, current task/session/event state, lead/writer/resume leases, heartbeat/stale-worker detection, cancellation, worktree/sandbox enforcement and route validation.
- Closure path: external lead decision → controller policy/enforcement → external worker operation → durable result/status → external lead review/next decision. The decisive current-control discretion does not close autonomously inside the first-party controller.
- Boundary reachability: not applicable to a positive state.
- Why this is / is not agent-owned: first-party machinery has strong enforcement authority, but the architecture explicitly assigns the discretionary planning/delegation/integration/completion decisions to the externally hosted lead. Runtime enforcement does not inherit S3 ownership from that lead.
- Evidence: [`docs/architecture.md`](https://github.com/jontey/agent-harness/blob/db6297cb776f6181310d3533c0ebf22d35e66de4/docs/architecture.md), [`src/controller.ts`](https://github.com/jontey/agent-harness/blob/db6297cb776f6181310d3533c0ebf22d35e66de4/src/controller.ts), [`src/worker.ts`](https://github.com/jontey/agent-harness/blob/db6297cb776f6181310d3533c0ebf22d35e66de4/src/worker.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: these mechanisms are strong evidence for a constructor/control-plane role in a wider composed system, but Methodology requires an established organizational function at the declared system boundary before assigning a positive local ownership state.

### Absence scope

- Surfaces inspected: lead responsibilities, controller policy/lifecycle, current task/session state, leases, heartbeat/reconciliation, steering/cancel/resume/handoff and route evidence.
- Plausible first-party paths checked: controller as manager, policy as current regulator, leases as resource allocation, stale-worker recovery and handoff as current intervention.
- Why no material first-party path remains: discretionary current-control choices remain with the externally hosted lead; first-party code transports, constrains or enforces those choices and lacks an internally owned S1 organization over which autonomous S3 can close.

## S3* — Complementary audit

- State: —
- Function: no implemented first-party complementary independent audit path with corrective return is established in the first release.
- Disturbance / variety regulated: the architecture describes review/verification stages and treating worker summaries as claims, but the implemented role contract contains only explorer and implementer workers.
- Decisive decision or feedback right: no shipped independent audit judgment with materially different access to operational reality is present at the reviewed revision.
- Decision owner: none established within the first-party boundary.
- Supporting / enforcement mechanisms: durable logs/events, route evidence, checkpoints, status reconciliation and the architecture's future review/verification design.
- Closure path: no implemented complementary evidence path → independent audit judgment → corrective return loop is established in the supported first release.
- Boundary reachability: not applicable to a positive state.
- Why this is / is not agent-owned: ordinary controller validation and route/status evidence check lifecycle correctness, while model-driven review/verifier roles described in architecture are not present in the implemented `Role` type at this revision.
- Evidence: [`docs/architecture.md`](https://github.com/jontey/agent-harness/blob/db6297cb776f6181310d3533c0ebf22d35e66de4/docs/architecture.md), [`src/types.ts`](https://github.com/jontey/agent-harness/blob/db6297cb776f6181310d3533c0ebf22d35e66de4/src/types.ts), [`src/controller.ts`](https://github.com/jontey/agent-harness/blob/db6297cb776f6181310d3533c0ebf22d35e66de4/src/controller.ts).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: later releases that implement an independently controlled reviewer/verifier role with raw-artifact access and corrective return would require a new-ref reassessment.

### Absence scope

- Surfaces inspected: architecture trust/verification and workflow sections, implemented role/harness types, controller lifecycle, route evidence, logs/events/checkpoints and first-release README status.
- Plausible first-party paths checked: review/verification stages, route validation, status reconciliation, logs/audit records, fake/test validation and correction steering.
- Why no material first-party path remains: implemented runtime roles stop at explorer/implementer; lifecycle and route checks do not provide a materially independent audit judgment over operational claims with corrective closure.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party external-and-prospective adaptation loop is established.
- Disturbance / variety regulated: the system can preserve checkpoints, recover tasks and transfer work between harnesses, but those mechanisms address continuity of current work rather than modeling future environmental change and adapting organizational capability.
- Decisive decision or feedback right: harness/model choice and future workflow changes are made by the external lead/operator/developer through configuration or subsequent software changes.
- Decision owner: no first-party autonomous S4 owner established.
- Supporting / enforcement mechanisms: portable checkpoints, cross-harness handoff, durable project state, policy/model configuration and continuation/recovery.
- Closure path: no environment/future distinction → adaptation option → returned change to present capability loop closes inside the first-party runtime.
- Boundary reachability: not applicable to a positive state.
- Why this is / is not agent-owned: persistence and handoff preserve operational context, but they do not themselves sense future-relevant environmental distinctions or autonomously revise capability in response.
- Evidence: [`README.md`](https://github.com/jontey/agent-harness/blob/db6297cb776f6181310d3533c0ebf22d35e66de4/README.md), [`docs/architecture.md`](https://github.com/jontey/agent-harness/blob/db6297cb776f6181310d3533c0ebf22d35e66de4/docs/architecture.md), [`src/controller.ts`](https://github.com/jontey/agent-harness/blob/db6297cb776f6181310d3533c0ebf22d35e66de4/src/controller.ts).
- Basis: structural absence.
- Confidence: high.
- Caveats: an external lead may research or adapt strategy, but that S4-like behavior belongs to the external harness/assembled organization unless first-party adaptation ownership is added.

### Absence scope

- Surfaces inspected: checkpoint/handoff design, durable project state, policy/model routing, recovery, architecture workflow and first-release implementation scope.
- Plausible first-party paths checked: cross-harness handoff, checkpoint reuse, model/harness switching, correction cycles, policy configuration and implementation planning.
- Why no material first-party path remains: all identified paths concern current-work continuation or externally authored configuration; none establishes first-party prospective environmental modeling plus adaptation closure into present capability.

## S5 — Policy and identity

- State: —
- Function: no runtime identity/ultimate-policy closure is established inside the first-party controller.
- Disturbance / variety regulated: static policy constrains models, harnesses, roles, permissions and engine diversity, while the active lead lease identifies who may issue mutating orchestration commands.
- Decisive decision or feedback right: policy contents, project objective and ultimate task/organizational purpose are authored by the user/developer/operator outside the runtime; the controller enforces them.
- Decision owner: no first-party autonomous or operationally closed parent S5 owner established at the assessed recursion.
- Supporting / enforcement mechanisms: external policy file, project objective/constraints/decision/current-state files, active lead lease and deterministic authorization checks.
- Closure path: operator/developer authors policy/objective → controller enforces them. No runtime identity-level issue is escalated to a legitimate S5 authority and returned as an authoritative policy decision through a first-party closure loop.
- Boundary reachability: not applicable to a positive state.
- Why this is / is not agent-owned: static policy and lead authorization bound behavior but do not themselves decide identity or ultimate policy. The lead's operational authority is likewise supplied by an external harness and is not shown to own identity-level closure.
- Evidence: [`README.md`](https://github.com/jontey/agent-harness/blob/db6297cb776f6181310d3533c0ebf22d35e66de4/README.md), [`docs/architecture.md`](https://github.com/jontey/agent-harness/blob/db6297cb776f6181310d3533c0ebf22d35e66de4/docs/architecture.md), [`src/controller.ts`](https://github.com/jontey/agent-harness/blob/db6297cb776f6181310d3533c0ebf22d35e66de4/src/controller.ts), [`config/policy.example.yaml`](https://github.com/jontey/agent-harness/blob/db6297cb776f6181310d3533c0ebf22d35e66de4/config/policy.example.yaml).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: operator/developer authority exists outside the runtime, but generic configuration ownership is not a Methodology `P` path without an identity/ultimate-policy issue and complete return-to-operation closure.

### Absence scope

- Surfaces inspected: policy configuration, lead authorization/lease, project objective/constraints/decision state, controller policy checks and architecture authority description.
- Plausible first-party paths checked: active lead identity, role/model/harness policy, project objective/constraints, correction/escalation and operator configuration.
- Why no material first-party path remains: the first-party runtime enforces externally authored constraints and authority but exposes no identity/ultimate-policy decision loop of its own and no qualifying parent-governed S5 return path.

## Recursion

No VSM recursion is credited inside the assessed controller boundary. Lead and worker processes can be separate agent systems and tasks can have parent identifiers, but process/task nesting and delegation do not establish locally viable recursive S1 units. External lead/worker harnesses require their own assessments or a separately declared assembled-system boundary.

## Variety and escalation

The repository has strong variety-management mechanisms for orchestration: role/model/harness allowlists, filesystem and network constraints, one-writer leases, separate worktrees, lifecycle state, heartbeats, stale-worker recovery, steering, cancellation, resume, handoff and durable checkpoints. These mechanisms attenuate execution/control variety and preserve evidence across runtime boundaries.

Escalation remains lead-centered. Architecture assigns the accountable lead responsibility for reviewing output, sending corrections, verifying completion and deciding next action. A correction-cycle limit can produce an escalation event/report, but the receiving decision authority is the external lead rather than a first-party S4/S5 owner.

## Evidence gaps

- The repository was created on 2026-09-24 and the pinned ref represents its first implemented release; later revisions may rapidly change the boundary.
- Architecture documents roles such as reviewer and verifier that are not in the implemented first-release `Role` union; they are not credited from design intent alone.
- The public repository metadata at review time exposes no recognized license. This is an intake/legal-provenance caveat rather than evidence for or against any VSM function and should be handled by Index intake policy separately from the semantic exclusion result.

## Terminal outcome

`excluded-no-agentic-vsm`.

The repository contains substantive first-party orchestration, policy, enforcement, recovery and evidence machinery, but its standard-distribution boundary deliberately delegates autonomous model/tool execution to separately supplied agent harnesses and likewise expects the accountable lead to run in another harness. The first-party control layer therefore does not establish autonomous S1 at the declared recursion, and higher-function control mechanisms are not promoted into an included vector by inheriting agent ownership from those external runtimes.

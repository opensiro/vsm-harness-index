---
harness_id: neopanic-harness
project_name: Harness³
repository: https://github.com/NeoPanic/harness3
review_ref: cb6c8e57eb0adac3f2ec1f4da1a98e52e2967063
reviewed_at: 2026-11-01
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A(P)
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Harness³

## Review boundary

- System in focus: the released single-daemon local Harness³ platform with independent model/tool Agent instances, task-board control plane, SQLite durable work/claims, Preset router, Goal workflows, fleet control and optional frozen-evidence verification.
- Purpose and identity: assemble bounded peer-agent task collectives and track their ownership, work, evidence, resource allocation and review, while offering a reusable independent Rust Harness core.
- Relevant environment: human task publisher/operator, local SQLite, tool plugins, LLM providers, published Presets, API/CLI/Web users and external effects.
- Standard-distribution boundary: deployed server/worker/platform with real-model router and Agent model adapters when configured; explicit human fleet API mode and optional Goal verification; do not infer task-board verification from the separate Goal workflow or infer unimplemented distributed deployment.
- Credited operating / distribution surfaces: [crates/harness3-core/src/engine.rs#L1-L120](https://github.com/NeoPanic/harness3/blob/cb6c8e57eb0adac3f2ec1f4da1a98e52e2967063/crates/harness3-core/src/engine.rs#L1-L120), [crates/harness3-worker/src/runner.rs#L1-L135](https://github.com/NeoPanic/harness3/blob/cb6c8e57eb0adac3f2ec1f4da1a98e52e2967063/crates/harness3-worker/src/runner.rs#L1-L135), [crates/harness3-platform/src/scheduling/board/mod.rs#L243-L383](https://github.com/NeoPanic/harness3/blob/cb6c8e57eb0adac3f2ec1f4da1a98e52e2967063/crates/harness3-platform/src/scheduling/board/mod.rs#L243-L383), [crates/harness3-platform/src/scheduling/routing.rs#L91-L315](https://github.com/NeoPanic/harness3/blob/cb6c8e57eb0adac3f2ec1f4da1a98e52e2967063/crates/harness3-platform/src/scheduling/routing.rs#L91-L315), [crates/harness3-platform/src/control/fleets.rs#L76-L137](https://github.com/NeoPanic/harness3/blob/cb6c8e57eb0adac3f2ec1f4da1a98e52e2967063/crates/harness3-platform/src/control/fleets.rs#L76-L137), [crates/harness3-platform/src/collaboration/verification/mod.rs#L120-L616](https://github.com/NeoPanic/harness3/blob/cb6c8e57eb0adac3f2ec1f4da1a98e52e2967063/crates/harness3-platform/src/collaboration/verification/mod.rs#L120-L616), [crates/harness3-worker/src/scheduler.rs#L1-L140](https://github.com/NeoPanic/harness3/blob/cb6c8e57eb0adac3f2ec1f4da1a98e52e2967063/crates/harness3-worker/src/scheduler.rs#L1-L140).
- Adjacent first-party surfaces excluded from ownership: deterministic demo inference as semantic evidence, screen animations, test harness, development CI, contributor governance, aspirational architecture passages, remote/distributed adapters not shipped; external model/provider decisions and human acceptance do not become autonomous S1 decisions by co-location.
- First-party operating / deployment modes considered: local model-backed task board with agent-claimed/split work and model Preset selection; human-governed fleet target/scale API; separate explicit Goal/research work with independent verifier and bounded rework; deterministic Demo only as implementation-path corroboration.
- Recursion level: one local platform as collective, distinct independent Agent runs as lower-level S1s, and legitimate human operator for the separate fleet-control mode. Task ancestry does not make parent tasks supervisors of child agents.
- Reviewed revision: cb6c8e57eb0adac3f2ec1f4da1a98e52e2967063; source checkout at exact commit.
- Observation date: 2026-11-01.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The core Harness provides bounded model-to-tool-to-model execution, policies, durable sessions, receipts and cancellation, independently of team orchestration ([crates/harness3-core/src/engine.rs#L1-L120](https://github.com/NeoPanic/harness3/blob/cb6c8e57eb0adac3f2ec1f4da1a98e52e2967063/crates/harness3-core/src/engine.rs#L1-L120), [docs/runtime.md#L1-L70](https://github.com/NeoPanic/harness3/blob/cb6c8e57eb0adac3f2ec1f4da1a98e52e2967063/docs/runtime.md#L1-L70)). Platform state is persisted in SQLite and coordinated by a single worker process. The worker runs routing, fleet, board, Goal and verifier reconciliation; the runner constructs an isolated Harness from each immutable Preset snapshot with only its bound tools ([crates/harness3-worker/src/scheduler.rs#L20-L128](https://github.com/NeoPanic/harness3/blob/cb6c8e57eb0adac3f2ec1f4da1a98e52e2967063/crates/harness3-worker/src/scheduler.rs#L20-L128), [crates/harness3-worker/src/runner.rs#L55-L135](https://github.com/NeoPanic/harness3/blob/cb6c8e57eb0adac3f2ec1f4da1a98e52e2967063/crates/harness3-worker/src/runner.rs#L55-L135)).

On the shared board, the publisher provides work and acceptance criteria without choosing an Agent. A model-backed router is bounded to a catalog of executable Presets; it decides a suitable Preset, the control plane validates it and provisions an instance. The instance must read the board and atomically claim compatible work, can split and return subtasks, and receives child evidence when later reoffered the parent ([crates/harness3-platform/src/scheduling/routing.rs#L91-L235](https://github.com/NeoPanic/harness3/blob/cb6c8e57eb0adac3f2ec1f4da1a98e52e2967063/crates/harness3-platform/src/scheduling/routing.rs#L91-L235), [crates/harness3-platform/src/scheduling/board/mod.rs#L243-L383](https://github.com/NeoPanic/harness3/blob/cb6c8e57eb0adac3f2ec1f4da1a98e52e2967063/crates/harness3-platform/src/scheduling/board/mod.rs#L243-L383)). This board does not automatically inherit independent verification or human Goal acceptance from the separate Goal workflow ([docs/task-board.zh-CN.md#L1-L115](https://github.com/NeoPanic/harness3/blob/cb6c8e57eb0adac3f2ec1f4da1a98e52e2967063/docs/task-board.zh-CN.md#L1-L115)).

Separately, optional Goal verification freezes per-round artifacts, launches a fresh independent instance restricted to evidence read/report tools, requires a reasoned per-check verdict with complete reads for passes, then gates acceptance and can trigger bounded evidence-linked rework. Manual acceptance remains human-owned and follows verification rather than replacing it ([crates/harness3-platform/src/collaboration/verification/mod.rs#L120-L263](https://github.com/NeoPanic/harness3/blob/cb6c8e57eb0adac3f2ec1f4da1a98e52e2967063/crates/harness3-platform/src/collaboration/verification/mod.rs#L120-L263), [crates/harness3-platform/src/collaboration/verification/mod.rs#L343-L616](https://github.com/NeoPanic/harness3/blob/cb6c8e57eb0adac3f2ec1f4da1a98e52e2967063/crates/harness3-platform/src/collaboration/verification/mod.rs#L343-L616)). Fleet modes expose separate human-controlled desired count / scale / terminate intents with revision and operation receipts, reconciled to actual instances ([crates/harness3-platform/src/control/fleets.rs#L76-L137](https://github.com/NeoPanic/harness3/blob/cb6c8e57eb0adac3f2ec1f4da1a98e52e2967063/crates/harness3-platform/src/control/fleets.rs#L76-L137), [crates/harness3-platform/src/control/fleets.rs#L202-L270](https://github.com/NeoPanic/harness3/blob/cb6c8e57eb0adac3f2ec1f4da1a98e52e2967063/crates/harness3-platform/src/control/fleets.rs#L202-L270)).

## Operational model

There are distinct working Agent S1s, not a monolithic planner pretending to act as peers. Claim-generation collision and parent/child dependency ordering are first-party coordination disturbances, but the decisive arbitration is transactional state enforcement; autonomous S2 ownership is not supplied. For current capability allocation the model-backed router makes a bounded discretionary Preset decision and returns it into actual provisioning. A separate human fleet mode closes a resource-governance decision by revising desired counts and reconciling instances. Independent frozen-artifact verification is a true audit path in the explicitly configured Goal mode, not a claim of externally verified truth or universal task-board review.

## S1 — Operations

- State: A
- Function: execute bounded user-published work through model-selected tools, report results, and optionally decide to split tasks for peer execution.
- Disturbance / variety regulated: variable tasks, tool results, failed actions and results from completed children.
- Decisive decision or feedback right: an instantiated Agent chooses next model/tool action, whether to use the board claim/split tools, and its work contribution.
- Decision owner: model-driven independent Agent within the shipped Harness run; platform validates tool and task authority but does not choose the Agent's tool sequence.
- Supporting / enforcement mechanisms: Preset bindings, runtime policy, receipts/checkpoints, SQLite Run state, tool-safety limits and claim prerequisite.
- Closure path: executed tool output feeds subsequent model reasoning; settled Run and child results feed board continuation or user-visible contribution.
- Boundary reachability: worker runner instantiates the shipping Harness with each Preset; normal board and Goal requests reach this path, independently of demo/test code.
- Why this is / is not agent-owned: the model has substantive task execution/splitting discretion; deterministic runtime and human task publisher set only operating constraints.
- Evidence: [crates/harness3-core/src/engine.rs#L65-L185](https://github.com/NeoPanic/harness3/blob/cb6c8e57eb0adac3f2ec1f4da1a98e52e2967063/crates/harness3-core/src/engine.rs#L65-L185); [crates/harness3-worker/src/runner.rs#L55-L135](https://github.com/NeoPanic/harness3/blob/cb6c8e57eb0adac3f2ec1f4da1a98e52e2967063/crates/harness3-worker/src/runner.rs#L55-L135); [crates/harness3-platform/src/scheduling/board/mod.rs#L277-L325](https://github.com/NeoPanic/harness3/blob/cb6c8e57eb0adac3f2ec1f4da1a98e52e2967063/crates/harness3-platform/src/scheduling/board/mod.rs#L277-L325).
- Basis: explicit / structural.
- Confidence: high for source path; no provider-backed E2E performed.
- Caveats: external tools may be unavailable and effects require idempotency beyond checkpointing; Demo output is not real research evidence.

## S2 — Coordination

- State: C
- Function: resolve contention for the same operational work item and stabilize parent-child availability as peers execute and split work.
- Distinct S1 units: separately provisioned model/tool Agent instances, each bound to a Run, Preset snapshot and independent local state.
- Inter-S1 disturbance: competing peers could both treat the same pending task as theirs; child and parent attempts could race while a predecessor is unresolved, causing duplicate work or invalid integration.
- Attenuating coordination relation: atomic claim checks current task state and Preset compatibility, rejects a second claimant; staged children only become runnable after a successful source Run, while parent waits until all children finish; failed children block the parent.
- Feedback into subsequent S1 behaviour: a rejected claim returns a conflict to the Agent, pending/claimed state changes what may be read/claimed next, and completed children reoffer the parent for a new integrating Agent.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the specific multiple-owner race and dependent-work collision are regulated through conditional transactional ownership and state transitions, not just message delivery.
- Disturbance / variety regulated: peer contention and out-of-order execution of shared task dependencies.
- Decisive decision or feedback right: the first-party board contract exposes task claim/split/feedback to peers, but collision arbitration is deterministic; no autonomous regulator decides among competing peer priorities.
- Decision owner: deterministic SQLite transaction for conflict arbitration; individual S1 Agents independently choose which compatible task to attempt.
- Supporting / enforcement mechanisms: shared board, generation/Run identity checks, atomic UPDATE, dependency state, event log and bounded task count.
- Closure path: successful claim gives one execution owner; unsuccessful claimant receives 409 and can choose differently; parent is made pending after children complete or blocked on failure.
- Boundary reachability: board tools are automatically injected into regular task-board Agent runs, not a theoretical adapter; claim enforcement occurs before work tools are usable.
- Why this is / is not agent-owned: coordination function and feedback path are real, but an autonomous S2 decision actor with cross-peer conflict discretion is not provided. The S2-specific constructor/claim primitive warrants C, not A.
- Evidence: [crates/harness3-platform/src/scheduling/board/mod.rs#L277-L325](https://github.com/NeoPanic/harness3/blob/cb6c8e57eb0adac3f2ec1f4da1a98e52e2967063/crates/harness3-platform/src/scheduling/board/mod.rs#L277-L325); [crates/harness3-platform/src/scheduling/board/mod.rs#L333-L383](https://github.com/NeoPanic/harness3/blob/cb6c8e57eb0adac3f2ec1f4da1a98e52e2967063/crates/harness3-platform/src/scheduling/board/mod.rs#L333-L383); [crates/harness3-worker/src/runner.rs#L18-L47](https://github.com/NeoPanic/harness3/blob/cb6c8e57eb0adac3f2ec1f4da1a98e52e2967063/crates/harness3-worker/src/runner.rs#L18-L47); [docs/task-board.zh-CN.md#L1-L39](https://github.com/NeoPanic/harness3/blob/cb6c8e57eb0adac3f2ec1f4da1a98e52e2967063/docs/task-board.zh-CN.md#L1-L39).
- Basis: structural.
- Confidence: medium-high.
- Caveats: this is narrow coordination of task ownership/dependencies, not general negotiation of conflicting goals, cost allocation, global fairness or distributed consensus.

## S3 — Inside-and-now control

- State: A(P)
- Function: regulate current operating capability/instance allocation against admitted work and shared resource limits, with distinct autonomous routing and human fleet-control modes.
- Whole-system current view: pending board tasks, executable Preset catalog and model availability, active worker slots / reserved instances; in human fleet mode, reported capacity, fleet status and outstanding operations.
- Current-control decision scope: choose which registered capabilities to provision for currently pending work; in parent mode change desired instance counts, scale or retire fleets under the current global quota.
- Disturbance / variety regulated: uneven present task demand, incompatible/missing Presets, model availability, instance/worker scarcity and fleet size drift.
- Decisive decision or feedback right: model router selects a Preset name/version/reason from the live eligible catalog for each actionable task; separately an authorized human chooses fleet target/termination.
- Decision owner: autonomous bounded routing model in the base mode; legitimate operator in the distinct fleet mode. Deterministic Rust/SQLite performs candidate validation, quota, retry and reconciliation.
- Supporting / enforcement mechanisms: catalog filter, route timeout/backoff, global worker/instance limits, fleet revision checks, operation receipts, reconcile loop.
- Closure path: accepted router selection is provisioned into a real instance and Run; failed/no-capacity decisions defer task for another attempt. In parent mode operator target writes desired state and fleet reconciler creates/drains actual instances, with operation/status returned.
- Boundary reachability: model-backed router is wired into normal worker loop when a real provider is configured; fleet scale/terminate commands and the reconciliation loop are standard local API/worker capabilities, not a roadmap.
- Why this is / is not agent-owned: the base model makes a nontrivial capability-selection decision within live constraints, whereas Rust only validates and provisions. Human fleet mode owns a different concrete current-resource choice; this does not make all enforcement an autonomous S3 policy.
- Evidence: [crates/harness3-platform/src/scheduling/routing.rs#L91-L235](https://github.com/NeoPanic/harness3/blob/cb6c8e57eb0adac3f2ec1f4da1a98e52e2967063/crates/harness3-platform/src/scheduling/routing.rs#L91-L235); [crates/harness3-platform/src/scheduling/routing.rs#L264-L315](https://github.com/NeoPanic/harness3/blob/cb6c8e57eb0adac3f2ec1f4da1a98e52e2967063/crates/harness3-platform/src/scheduling/routing.rs#L264-L315); [crates/harness3-platform/src/scheduling/board/mod.rs#L243-L275](https://github.com/NeoPanic/harness3/blob/cb6c8e57eb0adac3f2ec1f4da1a98e52e2967063/crates/harness3-platform/src/scheduling/board/mod.rs#L243-L275); [crates/harness3-platform/src/control/fleets.rs#L76-L137](https://github.com/NeoPanic/harness3/blob/cb6c8e57eb0adac3f2ec1f4da1a98e52e2967063/crates/harness3-platform/src/control/fleets.rs#L76-L137); [crates/harness3-platform/src/control/fleets.rs#L202-L270](https://github.com/NeoPanic/harness3/blob/cb6c8e57eb0adac3f2ec1f4da1a98e52e2967063/crates/harness3-platform/src/control/fleets.rs#L202-L270); [crates/harness3-worker/src/scheduler.rs#L20-L60](https://github.com/NeoPanic/harness3/blob/cb6c8e57eb0adac3f2ec1f4da1a98e52e2967063/crates/harness3-worker/src/scheduler.rs#L20-L60).
- Basis: explicit / structural.
- Confidence: medium-high for real-model routing and fleet closure; no paid-model E2E.
- Caveats: the router is a deliberately bounded single-call classifier, not an unlimited supervisor; its discretion is narrow current Preset choice. Demo uses deterministic selection. The human mode manages fleets and does not grant a human co-ownership of the same automatic board route in one run.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Configured model router chooses eligible Preset | Unassigned runnable board work | Validated choice provisions an Agent; errors/backoff return to routing | [crates/harness3-platform/src/scheduling/routing.rs#L137-L235](https://github.com/NeoPanic/harness3/blob/cb6c8e57eb0adac3f2ec1f4da1a98e52e2967063/crates/harness3-platform/src/scheduling/routing.rs#L137-L235) |
| Parent (`P`) | Human operator chooses desired fleet target/retirement | Fleet capacity/status and explicit scale/terminate command | Revisioned intent and operation receipt drive actual reconcile | [crates/harness3-platform/src/control/fleets.rs#L76-L137](https://github.com/NeoPanic/harness3/blob/cb6c8e57eb0adac3f2ec1f4da1a98e52e2967063/crates/harness3-platform/src/control/fleets.rs#L76-L137) |

## S3* — Complementary audit

- State: A
- Function: independently inspect frozen operational contributions against specified checks, produce an evidence-linked judgment and drive bounded repair/acceptance gating.
- Claim being audited: Goal work artifacts and final contributions support the specified acceptance/evidence checks.
- Ordinary reporting path: operational S1 Runs and their artifacts/Goal contributions, including model-generated completion claims.
- Complementary access path: a freshly allocated verification instance receives a frozen artifact manifest and separate paginated reader that checks hashes, read coverage and version; it does not inherit worker tools or writable workspace.
- Independence boundary: new instance/session and reviewer-only evidence/report tools; different scoped role from original worker, even though both might use an LLM provider and the same operator config.
- Who acts on findings: platform deterministically applies passed/failed/unknown/stale verdict states and, if preauthorized, launches bounded affected-task rework; human remains final Goal acceptor.
- Disturbance / variety regulated: unsupported claims, stale shared context, missing/changed artifact evidence, quality defects and false success on incomplete Runs.
- Decisive decision or feedback right: independent model reviewer judges each required check as passed/failed/unknown with reasons and evidence references, separate from the originating worker.
- Decision owner: fresh autonomous reviewer Agent owns the audit judgment; deterministic coverage/immutability gates and rework rules enforce/act on that verdict.
- Supporting / enforcement mechanisms: frozen hashes, per-artifact complete-read records, no plugin inheritance, bounded review timeout, manifest revision, immutable verdict, automatic rework quota and human acceptance.
- Closure path: accepted verdict after successful reviewer Run becomes passed/changes-requested/inconclusive; failed findings can rerun related tasks and re-verify, while passed status gates later human acceptance. Stale evidence blocks acceptance.
- Boundary reachability: optional verifier policy is supported on normal Goal and research workflows, and the worker runner launches its real configured Preset/model with restricted reviewer tools; it is not merely CI or Demo.
- Why this is / is not agent-owned: semantic audit judgment comes from an independent Agent, not from the source worker or deterministic parser. Enforcement of complete reads does not magically prove external truth.
- Evidence: [crates/harness3-platform/src/collaboration/verification/mod.rs#L120-L263](https://github.com/NeoPanic/harness3/blob/cb6c8e57eb0adac3f2ec1f4da1a98e52e2967063/crates/harness3-platform/src/collaboration/verification/mod.rs#L120-L263); [crates/harness3-platform/src/collaboration/verification/mod.rs#L343-L616](https://github.com/NeoPanic/harness3/blob/cb6c8e57eb0adac3f2ec1f4da1a98e52e2967063/crates/harness3-platform/src/collaboration/verification/mod.rs#L343-L616); [crates/harness3-worker/src/runner.rs#L95-L135](https://github.com/NeoPanic/harness3/blob/cb6c8e57eb0adac3f2ec1f4da1a98e52e2967063/crates/harness3-worker/src/runner.rs#L95-L135); [docs/verification.zh-CN.md#L1-L42](https://github.com/NeoPanic/harness3/blob/cb6c8e57eb0adac3f2ec1f4da1a98e52e2967063/docs/verification.zh-CN.md#L1-L42).
- Basis: explicit / structural.
- Confidence: high for shipped independent channel; medium for actual review quality without E2E.
- Caveats: checks are chosen by the user; reads demonstrate manifest coverage and integrity, not independent verification of external facts. The shared task board alone does not activate this Goal verifier.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party externally sensing prospective adaptation decision loop changing the platform's future capabilities.
- Disturbance / variety regulated: prospective shifts in task mix, technology, model efficacy or external environment not shown as managed future threats/opportunities.
- Decisive decision or feedback right: no agent-owned search/option/adoption loop with external future signal and return into Preset repertoire or system strategy.
- Decision owner: not established; operator can publish new Presets, and individual S1s can do user-requested research.
- Supporting / enforcement mechanisms: user-directed research template, Preset versioning, task router, shared context, verification/rework and plugin catalogue.
- Closure path: existing Preset selection and repair react to present work; no demonstrated future distinction yields adopted capability change through an S4 route.
- Why this is / is not agent-owned: planning, multi-agent research and selecting among already available Presets are not automatically S4.
- Evidence: [crates/harness3-platform/src/collaboration/research/mod.rs#L1-L130](https://github.com/NeoPanic/harness3/blob/cb6c8e57eb0adac3f2ec1f4da1a98e52e2967063/crates/harness3-platform/src/collaboration/research/mod.rs#L1-L130); [crates/harness3-platform/src/scheduling/routing.rs#L91-L177](https://github.com/NeoPanic/harness3/blob/cb6c8e57eb0adac3f2ec1f4da1a98e52e2967063/crates/harness3-platform/src/scheduling/routing.rs#L91-L177); [docs/managed-agents.zh-CN.md#L1-L115](https://github.com/NeoPanic/harness3/blob/cb6c8e57eb0adac3f2ec1f4da1a98e52e2967063/docs/managed-agents.zh-CN.md#L1-L115).
- Basis: structural bounded absence.
- Confidence: medium-high.
- Caveats: an operator could build an adaptive Preset pipeline but no in-boundary autonomous or parent-governed S4 closure is evidenced.
### Absence scope

- Surfaces inspected: model router and eligible catalogue, research/planner workflows, artifact review/rework, plugin/Preset versioning, local platform status/architecture.
- Plausible first-party paths checked: research synthesis into future strategy, automated Preset creation/adoption, model swapping driven by external environmental forecasts.
- Why no material first-party path remains: the supplied loops service current tasks and revisions already offered by operator; no external/prospective sensing plus adopted strategic capability alteration is wired into this distribution.

## S5 — Policy and identity

- State: —
- Function: no runtime ultimate identity/constitutional arbitration loop beyond static, operator-authored Preset and platform policies.
- Disturbance / variety regulated: potentially conflicting organizational values or who the collective is; no first-party escalation of such a dispute is traced.
- Decisive decision or feedback right: no exposed agent or legitimate parent path from a raised identity-policy issue through authoritative judgment back into next operation.
- Decision owner: operator authors immutable Presets and config; these are static parent-set constraints rather than an evidenced ongoing S5 loop.
- Supporting / enforcement mechanisms: versioned Presets, tool binding/security checks, human Goal acceptance, model router restrictions and cancellation.
- Closure path: ordinary task approval/review and preset publication changes normal capabilities, not established policy conflict resolution after a surfaced issue.
- Why this is / is not agent-owned: authorizing a tool, passing an acceptance check or selecting a task specialist does not decide constitutional identity or ultimate policy.
- Evidence: [crates/harness3-core/src/policy.rs#L1-L22](https://github.com/NeoPanic/harness3/blob/cb6c8e57eb0adac3f2ec1f4da1a98e52e2967063/crates/harness3-core/src/policy.rs#L1-L22); [crates/harness3-platform/src/scheduling/routing.rs#L137-L177](https://github.com/NeoPanic/harness3/blob/cb6c8e57eb0adac3f2ec1f4da1a98e52e2967063/crates/harness3-platform/src/scheduling/routing.rs#L137-L177); [crates/harness3-platform/src/collaboration/coordination.rs#L135-L175](https://github.com/NeoPanic/harness3/blob/cb6c8e57eb0adac3f2ec1f4da1a98e52e2967063/crates/harness3-platform/src/collaboration/coordination.rs#L135-L175); [docs/managed-agents.zh-CN.md#L1-L115](https://github.com/NeoPanic/harness3/blob/cb6c8e57eb0adac3f2ec1f4da1a98e52e2967063/docs/managed-agents.zh-CN.md#L1-L115).
- Basis: structural bounded absence.
- Confidence: medium-high.
- Caveats: the human operator does set top-level deployment constraints, but no function-specific proposed/contested ultimate-policy closure is demonstrated merely by being able to configure them.
### Absence scope

- Surfaces inspected: Preset publication/inheritance, policy interception, task acceptance, routing, fleet control, Goal review and first-party control APIs.
- Plausible first-party paths checked: operator ultimate-authority escalation, AI constitutional review, identity policy proposal/decision return, versioned Preset authority.
- Why no material first-party path remains: these publish fixed constraints and decide ordinary present work or review; no material identity-policy matter is routed to a decisive authority and returned as an S5 closure.

## Distributed OSS parent arrangement

GitHub maintainers, issue templates and contribution workflows are outside the declared local runtime recursion. Public contributors do not become the deployed S3 parent. The one positive parent mode is the actual platform operator's scoped resource/fleet control.

## Self-hosted and non-human modes

Local self-hosted trusted-process deployment offers real-model routing or deterministic Demo; positive S3 autonomy is claimed only for the real-model mode. Human fleet API is a separately supported S3 parent mode. The verifier is independent by role/session/evidence scope, not necessarily by vendor organization. Nothing establishes an unbounded non-human parent metasystem or distributed-worker mode.

## Recursion

Peer Agent instances are operational S1s; parent/child task dependencies and lifecycle pools are not organizational command hierarchy. The platform provides one supported collective recursion, with S2 claim contracts and S3 routing/fleet resource paths; group-level Goal artifacts and validation are a distinct workflow within it.

## Variety and escalation

Capacity exhaustion, failed routing, lost claims and unresolved external side effects are retained as explicit pending/blocked/unknown states. Model choices are catalog-bounded, transactional arbitration prevents duplicate owners, and verifier findings feed rework or stop. These normal queues/errors do not independently prove a VSM algedonic signal; no separate exceptional S3/S4/S5 alarm path is credited.

## Evidence gaps

No live paid model/provider or tool-effect E2E was run. S2 C is narrowly tied to the specific claim/dependency collision witness; broader policy conflict resolution is unproven. S3 autonomous ownership is limited to the configured real-model Preset route, not deterministic Demo. S3* A applies only when optional Goal/research verification is enabled, not every board task.

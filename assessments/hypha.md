---
harness_id: hypha
project_name: Hypha
repository: https://github.com/CodeSoul-co/Hypha
review_ref: ac77fa9b4a1b1da2815adf7d5582dbc27cd9373f
reviewed_at: 2026-09-25
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-25
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Hypha

## Review boundary

- System in focus: one first-party Hypha Agent Core + Production Harness deployment at pinned revision `ac77fa9b4a1b1da2815adf7d5582dbc27cd9373f`, including the ordinary ReAct runtime, durable event-backed harness FSM, server/API surface, policy/approval gates, checkpoints, recovery and replay machinery actually wired into that deployment.
- Purpose and identity: execute domain-agent work through a durable, governed ReAct runtime whose substantive model/tool choices are recorded and constrained by framework-owned state, policy, approval, recovery and replay mechanisms.
- Relevant environment: user/operator requests, external model providers, Tool/MCP endpoints, configured Memory/Skill/Prompt/Policy resources, workspaces and other tool-mediated external state.
- Standard-distribution boundary: first-party runtime packages and bundled server/API paths used for supported agent runs. `packages/testing`, benchmarks, examples, repository CI and future multi-agent facilities are adjacent unless the frozen runtime directly wires them into ordinary operation.
- Credited operating / distribution surfaces: ordinary and resumed ReAct runs, bounded quantum execution, event-backed FSM progression, durable session/run commands, policy and human-review suspension/resumption, recovery, per-run replay/audit projections and supported administrative runtime APIs.
- Adjacent first-party surfaces excluded from ownership: offline `packages/testing` regression/evaluator machinery when not wired into production control; future multi-agent execution described around MessageBus; repository-development workflows; documentation claims not corroborated by frozen source/runtime wiring.
- First-party operating / deployment modes considered: normal bounded ReAct execution, long-horizon continuation/recovery, human-review suspension/resume, per-run replay/audit, workflow/runtime administration and concurrent independent user/session runs.
- Recursion level: the assessed organization is one Hypha deployment. A durable DomainPack-configured agent run is the established S1 operational unit. Multiple sessions/runs may coexist, but separate S1 plurality is not by itself sufficient to establish S2/S3 at this recursion.
- Reviewed revision: `ac77fa9b4a1b1da2815adf7d5582dbc27cd9373f`.
- Observation date: 2026-09-25.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Hypha separates an Agent Core from a Production Harness. The Agent Core supplies model inference, action selection, tool execution, verification and memory/context participation. The Production Harness wraps that operational loop in an event-backed FSM with checkpoints, policy/approval state, bounded execution quanta, recovery, replay and audit projections.

The ordinary ReAct runner is a genuine operational loop: inference chooses the next action, tool/environment results become observations, verification and memory synchronization update run state, and subsequent reasoning proceeds from the changed evidence. `react-quantum-executor.ts` reconstructs a bounded quantum from durable evidence and invokes that loop, while `long-horizon-react-supervisor.ts` controls deterministic retry/continuation boundaries around quanta. This establishes autonomous S1 ownership but does not promote the surrounding deterministic FSM/scheduler into S3.

Hypha also contains primitives whose names resemble higher VSM functions. `RuntimeResourceCoordinator` can express shared/exclusive claims with fencing and conflict rejection; MessageBus is described for future multi-workflow/multi-agent execution; replay/audit/regression machinery can reconstruct and evaluate recorded runs. At the frozen standard runtime, however, no complete first-party S2 witness was found from distinct credited S1 units through a concrete inter-S1 disturbance, attenuation relation and feedback. The runtime reference explicitly says the current single-agent runtime can ignore MessageBus, and no ordinary production wiring was established for the generic resource coordinator as the closure of an inter-S1 coordination loop.

For S3, per-run runtime projections, status/usage surfaces, model/provider switching, workflow administration, approvals and cancellation were inspected. They expose useful control/configuration operations but do not establish a whole-system inside-and-now current-control view across the deployment's active S1 commitments together with a regulator owning cross-operation resource/priority/commitment decisions. The FSM driver, leases, budgets, scheduler and recovery supervisor enforce bounded state transitions and safety but do not themselves exercise S3 discretion.

For S3*, replay/audit projections are derived from the same ordinary event stream and the standard audit projection is chiefly a set of run/event counters. Offline deterministic evaluators/regression runners are strong evaluation infrastructure, but no standard production path was found that gives a materially independent complementary audit actor access to operational reality, produces an audit judgment and returns findings into runtime control. S4 and S5 likewise remain absent: model/provider/tool changes, Memory/Skill installation, recovery and testing/evaluation are operational/configuration surfaces rather than a demonstrated external-and-prospective adaptation loop or identity/ultimate-policy closure.

Primary evidence:

- [`packages/kernel/src/index.ts`](https://github.com/CodeSoul-co/Hypha/blob/ac77fa9b4a1b1da2815adf7d5582dbc27cd9373f/packages/kernel/src/index.ts) — `BasicReActAgentRuntime`, `ReActRunner` reasoning/action/tool/observation/verification/memory loop and bounded run behavior.
- [`packages/harness/src/react-quantum-executor.ts`](https://github.com/CodeSoul-co/Hypha/blob/ac77fa9b4a1b1da2815adf7d5582dbc27cd9373f/packages/harness/src/react-quantum-executor.ts) — reconstruction and execution of one bounded ReAct quantum from durable harness evidence.
- [`packages/harness/src/long-horizon-react-supervisor.ts`](https://github.com/CodeSoul-co/Hypha/blob/ac77fa9b4a1b1da2815adf7d5582dbc27cd9373f/packages/harness/src/long-horizon-react-supervisor.ts) — deterministic retry/continuation/human handoff around bounded quanta.
- [`docs/reference/runtime-model.md`](https://github.com/CodeSoul-co/Hypha/blob/ac77fa9b4a1b1da2815adf7d5582dbc27cd9373f/docs/reference/runtime-model.md) — event-first runtime, session serialization, leases/fencing/recovery/replay model and explicit statement that MessageBus is for future multi-workflow/multi-agent execution while the current single-agent runtime can ignore it.
- [`packages/core/src/modules/runtime/resource-coordinator.ts`](https://github.com/CodeSoul-co/Hypha/blob/ac77fa9b4a1b1da2815adf7d5582dbc27cd9373f/packages/core/src/modules/runtime/resource-coordinator.ts) — generic shared/exclusive resource claims and fencing inspected for S2.
- [`docs/api/http.md`](https://github.com/CodeSoul-co/Hypha/blob/ac77fa9b4a1b1da2815adf7d5582dbc27cd9373f/docs/api/http.md) — supported server runtime/status/model/workflow/approval/replay/audit administration surfaces inspected for S3/S3* reachability.
- [`packages/harness/src/runtime.ts`](https://github.com/CodeSoul-co/Hypha/blob/ac77fa9b4a1b1da2815adf7d5582dbc27cd9373f/packages/harness/src/runtime.ts) — event-derived runtime projections and audit projection counters.
- [`README.md`](https://github.com/CodeSoul-co/Hypha/blob/ac77fa9b4a1b1da2815adf7d5582dbc27cd9373f/README.md) — shipped Agent Core/Production Harness architecture and declared runtime capabilities, used only where corroborated by frozen implementation.

## Operational model

A Hypha run is a durable operational cell. The model selects substantive actions, tool/environment results return as observations, and the run advances through repeated reasoning, action, verification and memory/context updates. Framework-owned FSM, policy, checkpoint, lease, cancellation, continuation and recovery mechanisms bound that work. The deployment can host multiple runs, but no qualifying higher-level autonomous regulator or complete constructor path for S2, S3, S3*, S4 or S5 is established at the chosen boundary.

## S1 — Operations

- State: A
- Function: transform a DomainPack/user objective into tool-mediated outcomes through a repeated model reasoning → action selection → tool/environment observation → verification/memory feedback loop.
- Disturbance / variety regulated: changing task/environment state, model uncertainty, tool results and failures, policy decisions, context/memory state, checkpoint/recovery conditions and human-review interruptions.
- Decisive decision or feedback right: choose the substantive next action/tool and revise subsequent work from returned observations and accumulated run evidence.
- Decision owner: the active ReAct model actor inside the run.
- Supporting / enforcement mechanisms: `BasicReActAgentRuntime`, `ReActRunner`, tool execution, verifier, Memory/context interfaces, event store, harness FSM, checkpoints, budgets, policy/approval gates and bounded quantum execution.
- Closure path: objective/context enters run → model reasons and selects an action → policy/runtime permits and tool executes → observation/result is persisted → verifier/memory/context processing updates evidence → model receives changed evidence and selects the next substantive action → run/environment state changes.
- Boundary reachability: this is the ordinary first-party Agent Core + Production Harness execution path and is directly invoked by the bounded quantum executor rather than requiring downstream composition.
- Why this is / is not agent-owned: deterministic FSM/policy/recovery machinery constrains execution, but removing the model removes the discretionary choice of what substantive work to attempt next and how to react to returned evidence.
- Evidence: [`packages/kernel/src/index.ts`](https://github.com/CodeSoul-co/Hypha/blob/ac77fa9b4a1b1da2815adf7d5582dbc27cd9373f/packages/kernel/src/index.ts); [`packages/harness/src/react-quantum-executor.ts`](https://github.com/CodeSoul-co/Hypha/blob/ac77fa9b4a1b1da2815adf7d5582dbc27cd9373f/packages/harness/src/react-quantum-executor.ts); [`packages/harness/src/long-horizon-react-supervisor.ts`](https://github.com/CodeSoul-co/Hypha/blob/ac77fa9b4a1b1da2815adf7d5582dbc27cd9373f/packages/harness/src/long-horizon-react-supervisor.ts).
- Basis: explicit + structural
- Confidence: high
- Caveats: provider inference may be external, but Hypha supplies the persistent first-party reason/act/observe feedback loop and applies model decisions through its governed runtime.

## S2 — Coordination

- State: —
- Function: no material first-party S2 relation is established at the assessed deployment recursion.
- Disturbance / variety regulated: no complete qualifying inter-S1 interference/oscillation witness is established in the standard frozen runtime.
- Decisive decision or feedback right: not established.
- Decision owner: none established for S2 at this boundary.
- Supporting / enforcement mechanisms: same-session command serialization, run/state leases, fencing, cancellation, generic `RuntimeResourceCoordinator`, MessageBus and workflow/run boundaries can regulate execution mechanics, but do not by themselves establish S2.
- Closure path: not applicable; no reviewed standard path reconstructs distinct credited S1 units → concrete inter-S1 disturbance → S2-specific attenuation → feedback changing subsequent S1 behavior.
- Distinct S1 units: durable agent runs are plausible distinct operational units at deployment recursion and different sessions can execute independently.
- Inter-S1 disturbance: the generic resource coordinator can represent conflicting shared/exclusive claims, but a concrete ordinary-runtime disturbance among two credited S1 runs was not established through standard production wiring.
- Attenuating coordination relation: same-session `SessionQueue` serialization concerns commands within one session; MessageBus is documented for future multi-agent/workflow execution; generic resource claims are not shown as the standard closure for current multi-run coordination.
- Feedback into subsequent S1 behaviour: no complete first-party current-runtime chain from an inter-S1 conflict through a coordination decision back into both/affected operational loops was established.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: it is deliberately not mapped as S2. The frozen tree has coordination primitives, but the Profile requires a concrete inter-S1 disturbance-and-feedback witness, not merely reusable synchronization infrastructure.
- Why this is / is not agent-owned: no material S2 function is established, so ownership classification does not proceed.
- Evidence: [`docs/reference/runtime-model.md`](https://github.com/CodeSoul-co/Hypha/blob/ac77fa9b4a1b1da2815adf7d5582dbc27cd9373f/docs/reference/runtime-model.md); [`packages/core/src/modules/runtime/resource-coordinator.ts`](https://github.com/CodeSoul-co/Hypha/blob/ac77fa9b4a1b1da2815adf7d5582dbc27cd9373f/packages/core/src/modules/runtime/resource-coordinator.ts).
- Basis: explicit + structural absence review
- Confidence: high
- Caveats: a downstream/wider deployment could wire these primitives into a genuine S2 relation; that would be a different system-in-focus and requires its own evidence.

### Absence scope

- Surfaces inspected: session serialization, run/state leases, fencing, cancellation, MessageBus, generic resource coordinator, workflow/run concurrency and runtime reference architecture.
- Plausible first-party paths checked: concurrent sessions/runs, shared/exclusive resource claims, event transport, workflow execution and recovery contention.
- Why no material first-party path remains: current standard evidence shows isolation/serialization/fencing and future/generic coordination infrastructure, but not the Profile's complete inter-S1 disturbance → attenuation → feedback closure.

## S3 — Inside-and-now control

- State: —
- Function: no material first-party whole-system inside-and-now current-control loop is established at the assessed deployment recursion.
- Disturbance / variety regulated: Hypha regulates individual-run state, policy, retries, leases and recovery, but no deployment-wide current operational variety is shown being judged through a whole-system S3 view.
- Decisive decision or feedback right: not established for cross-S1 commitments, priorities, resource allocation or current deployment-wide operating posture.
- Decision owner: none established for S3 at this boundary.
- Supporting / enforcement mechanisms: FSM driver, budgets, scheduler, leases/fencing, recovery supervisor, per-run projections, status/usage endpoints, model/provider switching, workflow administration, approval and cancellation.
- Closure path: not applicable; the reviewed paths either enforce deterministic run constraints, expose per-run/status/configuration data or allow local administrative actions. No qualifying path closes whole-system current evidence → S3 judgment → changed current S1 commitments/resources/priorities.
- Boundary reachability: standard HTTP/runtime surfaces are reachable, but reachability of controls is not sufficient without the S3 function itself.
- Whole-system current view: not established. The inspected runtime API is predominantly per-run (`runId`) plus service/provider/usage/status information; no current aggregate operational picture across active S1 commitments was established.
- Current-control decision scope: not established as a coherent deployment-wide decision right. Model switching, approvals, workflow load/unload and run cancellation are local/configuration/exception controls rather than a demonstrated cross-operation regulator.
- Why this is / is not agent-owned: no S3 function is established. Deterministic FSM/recovery/scheduling mechanisms enforce rules but do not own discretionary inside-and-now organizational regulation.
- Evidence: [`docs/api/http.md`](https://github.com/CodeSoul-co/Hypha/blob/ac77fa9b4a1b1da2815adf7d5582dbc27cd9373f/docs/api/http.md); [`docs/reference/runtime-model.md`](https://github.com/CodeSoul-co/Hypha/blob/ac77fa9b4a1b1da2815adf7d5582dbc27cd9373f/docs/reference/runtime-model.md); [`packages/harness/src/long-horizon-react-supervisor.ts`](https://github.com/CodeSoul-co/Hypha/blob/ac77fa9b4a1b1da2815adf7d5582dbc27cd9373f/packages/harness/src/long-horizon-react-supervisor.ts).
- Basis: explicit + structural absence review
- Confidence: high
- Caveats: a parent/operator can use multiple exposed controls, but generic operator access does not establish Methodology parent notation without a qualifying S3 current-control loop.

### Absence scope

- Surfaces inspected: `/status`, `/usage`, `/runtime`, per-run projections/events/replay/audit, models/provider switch, MCP connect/disconnect, workflow load/unload/cancel, approvals, FSM transition API, scheduler/recovery and lease machinery.
- Plausible first-party paths checked: deployment health/status, live model switching, per-run state control, workflow administration, human review and recovery/continuation decisions.
- Why no material first-party path remains: these surfaces expose enforcement, configuration and local run administration, but no standard whole-system current-control view plus decision/return loop over the deployment's active S1 commitments was established.

## S3* — Complementary audit

- State: —
- Function: no material first-party complementary-audit closure is established at the assessed deployment recursion.
- Disturbance / variety regulated: replay/audit/evaluation can detect differences or summarize run evidence, but no independent S3* audit actor/control loop is established in ordinary production operation.
- Decisive decision or feedback right: not established.
- Decision owner: none established for S3* at this boundary.
- Supporting / enforcement mechanisms: event-sourced replay, per-run audit projection, deterministic evaluators, trace-completeness/output-contract evaluation and offline regression machinery.
- Closure path: not applicable; ordinary run events feed replay/audit projections and offline evaluators, but no standard first-party path was established where complementary audit judgment returns findings into runtime current-control decisions.
- Claim being audited: no qualifying independent operational claim/loop is established; the standard audit projection summarizes the same event stream used as runtime source of truth.
- Ordinary reporting path: event-backed run/FSM/projection state.
- Complementary access path: replay can deterministically reconstruct/compare recorded events, but it remains derived from the same first-party event source; offline testing evaluators are adjacent to the supported production runtime unless explicitly wired back.
- Independence boundary: no materially independent sensor/source or separately owned audit judgment was established at the standard deployment boundary.
- Who acts on findings: not established as a first-party S3* closure; an operator/test harness can inspect results, but generic human/offline test action is not enough.
- Why this is / is not agent-owned: no autonomous audit actor owns complementary judgment and corrective return.
- Evidence: [`packages/harness/src/runtime.ts`](https://github.com/CodeSoul-co/Hypha/blob/ac77fa9b4a1b1da2815adf7d5582dbc27cd9373f/packages/harness/src/runtime.ts); [`docs/reference/runtime-model.md`](https://github.com/CodeSoul-co/Hypha/blob/ac77fa9b4a1b1da2815adf7d5582dbc27cd9373f/docs/reference/runtime-model.md); [`docs/api/http.md`](https://github.com/CodeSoul-co/Hypha/blob/ac77fa9b4a1b1da2815adf7d5582dbc27cd9373f/docs/api/http.md).
- Basis: explicit + structural absence review
- Confidence: high
- Caveats: Hypha has unusually strong replay/evaluation infrastructure; this finding is specifically that strong observability/testing is not automatically S3* without complementary independence, audit judgment and return to control.

### Absence scope

- Surfaces inspected: runtime audit projection, event replay/compare, regression/evaluation interfaces, trace/output-contract evaluators, server audit/replay endpoints and ordinary event/projection pipeline.
- Plausible first-party paths checked: event-count audit, replay divergence, deterministic regression, trace completeness and operator inspection of per-run audit/replay results.
- Why no material first-party path remains: inspected paths are derived from the ordinary event substrate or remain offline/testing mechanisms, and no independently owned audit finding is returned into standard runtime control.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party external-and-prospective organizational adaptation loop is established at the assessed deployment recursion.
- Disturbance / variety regulated: not established as changing external/future conditions requiring adaptation of organizational capability.
- Decisive decision or feedback right: not established.
- Decision owner: none established for S4 at this boundary.
- Supporting / enforcement mechanisms: configurable providers/models, Tool/MCP/Memory/Skill/Prompt resources, skill installation/reload, evaluation/regression facilities, durable memory and ordinary external tool access can change or inform operation but do not by themselves establish S4.
- Closure path: not applicable; no reviewed first-party path closes external/prospective sensing → development of adaptation options → S4 selection/judgment → return into present capability/S3.
- Why this is / is not agent-owned: the S1 model can research/use tools and Memory can preserve operational evidence, but task-level external sensing or learning does not become S4 without the organizational adaptation conversation defined by the Profile.
- Evidence: [`README.md`](https://github.com/CodeSoul-co/Hypha/blob/ac77fa9b4a1b1da2815adf7d5582dbc27cd9373f/README.md); [`docs/api/http.md`](https://github.com/CodeSoul-co/Hypha/blob/ac77fa9b4a1b1da2815adf7d5582dbc27cd9373f/docs/api/http.md); [`docs/reference/runtime-model.md`](https://github.com/CodeSoul-co/Hypha/blob/ac77fa9b4a1b1da2815adf7d5582dbc27cd9373f/docs/reference/runtime-model.md).
- Basis: explicit + structural absence review
- Confidence: high
- Caveats: downstream organizations may use Hypha's evaluation/configuration primitives inside an S4 loop, but that loop is not supplied by the frozen standard deployment.

### Absence scope

- Surfaces inspected: provider/model administration, MCP/tool connections, Memory/Skill/Prompt facilities, skill install/reload, evaluation/regression, recovery/continuation and ordinary external tool use.
- Plausible first-party paths checked: learning/memory, runtime model switching, skill mutation, evaluation-driven change and environment/tool research.
- Why no material first-party path remains: reviewed mechanisms operate/configure current work or evaluate recorded work; no standard loop develops future-facing organizational adaptation options from external change and returns a selected adaptation to current control/capability.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy decision loop is established at the assessed deployment recursion.
- Disturbance / variety regulated: not established as an identity, constitutional or ultimate-policy matter.
- Decisive decision or feedback right: not established.
- Decision owner: none established for S5 within the standard deployment boundary.
- Supporting / enforcement mechanisms: DomainPack Policy/Prompt definitions, tool/capability policy, human approval, provider/model settings, workflow administration and other configuration govern operation but do not establish ultimate-policy closure.
- Closure path: not applicable; no reviewed first-party path shows a genuine identity/ultimate-policy issue reaching legitimate ultimate authority and returning as authoritative policy governing subsequent Hypha operation.
- Why this is / is not agent-owned: operational models work inside configured DomainPack/policy boundaries; they are not shown owning the identity or legitimacy of those boundaries. Human approval/configuration likewise does not become S5 without identity-level issue/decision/return closure.
- Evidence: [`README.md`](https://github.com/CodeSoul-co/Hypha/blob/ac77fa9b4a1b1da2815adf7d5582dbc27cd9373f/README.md); [`docs/api/http.md`](https://github.com/CodeSoul-co/Hypha/blob/ac77fa9b4a1b1da2815adf7d5582dbc27cd9373f/docs/api/http.md).
- Basis: explicit + structural absence review
- Confidence: high
- Caveats: DomainPack is a strong policy/configuration abstraction; this assessment does not equate declarative policy presence with S5 ownership.

### Absence scope

- Surfaces inspected: DomainPack policy/prompt/capability declarations, approval/human-review flows, model/provider configuration, workflow administration, skill/memory mutation and runtime control APIs.
- Plausible first-party paths checked: policy validation, approval/escalation, runtime configuration changes and DomainPack-defined identity/behavior constraints.
- Why no material first-party path remains: reviewed paths specify or enforce operational constraints but do not surface an identity/ultimate-policy issue to a legitimate ultimate authority and close the decision back into subsequent organizational governance.

## Distributed OSS parent arrangement

Hypha is open source, but repository maintainer/contributor governance was not used to infer runtime parent ownership. The assessed recursion is one operating deployment. Upstream release/design choices are adjacent unless a first-party runtime return loop makes them part of the assessed organization's control structure; no such S3/S4/S5 parent mode is claimed.

## Self-hosted and non-human modes

Hypha supports self-hosted operation with human review and administrative controls. Those controls can approve/reject exact subjects, switch models/providers, cancel work or change configuration, but generic operator control is not by itself `P`; no qualifying parent-governed S3/S4/S5 closure was established at the frozen revision.

## Recursion

The primary recursion is one Hypha deployment containing durable agent runs. Each established run contains the autonomous ReAct S1 loop and framework-owned enforcement/recovery machinery. Multiple sessions/runs can exist independently, but current documentation explicitly treats MessageBus as future multi-agent/multi-workflow transport and no complete current inter-S1 S2 witness was found. Offline testing/evaluation is not silently promoted into a deployment-level metasystem.

## Variety and escalation

Hypha attenuates operational variety through bounded quanta, FSM transitions, budgets, policy/approval checks, leases/fencing, cancellation, checkpoints, deterministic recovery and session serialization. Variety returns through model inference, tool/environment observations, verification and Memory/context updates. Human-review states, exhausted global budgets/deadlines and non-retryable continuation conditions escalate to operator/workflow decisions. These are strong governance mechanics, but the assessment keeps enforcement distinct from autonomous metasystem ownership.

## Evidence gaps

- No fresh runtime trace was executed inside this assessment environment; positive claims rely on pinned first-party source/docs and frozen production wiring.
- The repository contains substantial generic coordination and evaluation infrastructure. S2/S3* remain absent because the required current standard-runtime functional closure was not established, not because such primitives are missing.
- S3 remains absent because the inspected API exposes per-run/status/configuration controls without a demonstrated whole-system current-control view and decision loop over active S1 commitments.
- S4 remains absent because operational learning/configuration/evaluation was not shown as an external-and-prospective organizational adaptation conversation.
- S5 remains absent because declarative policies, approvals and DomainPack configuration do not establish identity/ultimate-policy authority.

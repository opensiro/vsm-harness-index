---
harness_id: korus
project_name: Korus
repository: https://github.com/surefire-ai/korus
review_ref: ed5ea6a9fca86f43df161a100e913c29fa9b40c9
reviewed_at: 2026-09-24
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-24
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# Korus

## Review boundary

- System in focus: the first-party Korus Kubernetes-native AgentOps platform at pinned revision `ed5ea6a9fca86f43df161a100e913c29fa9b40c9`, including Agent/AgentRun/AgentEvaluation and supporting CRDs, the operator reconcilers/compiler, gateway/runtime dispatch, the standard Eino worker and its built-in agent-pattern runners, policy/resource resolution, and the first-party evaluation controller.
- Purpose and identity: declaratively define, compile, publish, invoke, execute, evaluate, and operate AI agents as Kubernetes resources while preserving revision identity, runtime state, policy bindings, traces/artifacts, and evaluation evidence.
- Relevant environment: Kubernetes, users/operators, model providers, external tools and MCP services, datasets and expected outputs, external knowledge systems, credentials/secrets, and optional external runtime/provider implementations.
- Standard-distribution boundary: repository-owned CRDs, controllers, compiler, gateway, runtime adapters, first-party Eino worker/pattern runners, policy/resource resolution, AgentRun lifecycle, artifact/status paths, and AgentEvaluation execution are inside. External model/provider internals, Kubernetes itself, downstream tools/services, dataset authorship, and optional external runtime implementations remain environmental dependencies.
- Credited operating / distribution surfaces: `api/v1alpha1/*`; `internal/controller/agent_controller.go`; `internal/controller/agentrun_controller.go`; `internal/controller/agentevaluation_controller.go`; `internal/worker/eino_runner.go`; built-in pattern runners including ReAct, router, reflection, plan-execute, tool-calling and workflow; compiler/runtime/gateway paths; shipped supporting-resource CRDs.
- Adjacent first-party surfaces excluded from ownership: repository tests and CI; historical release checklists; Web Console development surfaces that the repository's own Phase 3 audit calls incomplete; roadmap-only A2A/Agent Mesh work; future release-gate/waiver/approval/audit-history surfaces not wired into the standard runtime. These may corroborate implementation state but do not donate organizational ownership.
- First-party operating / deployment modes considered: standard Kubernetes operator + gateway + worker deployment; Eino-native agent execution with built-in patterns; AgentRun lifecycle/retry/cancel/timeout handling; SubAgent invocation through the internal gateway; AgentEvaluation managed-run and baseline-comparison mode. Optional Google ADK/provider adapters were not needed to establish the positive findings.
- Recursion level: the Korus-managed agent organization at the platform/runtime boundary. Individual first-party Agent executions are operational S1 units; SubAgents may form nested operational units, but recursion is not inferred from nesting alone. The AgentEvaluation controller is assessed as a complementary audit construction path over those operations.
- Reviewed revision: `ed5ea6a9fca86f43df161a100e913c29fa9b40c9`.
- Observation date: 2026-09-24.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

Korus separates declarative control-plane resources from execution while shipping both sides of the standard path. An `Agent` spec selects models, prompts, tools, knowledge, policies, SubAgents and an orchestration pattern. The operator resolves references and compiles the declaration into a revisioned artifact. `AgentRun` then drives that compiled agent through the runtime boundary, while the first-party Eino worker executes the substantive agent loop.

The Eino runtime is not a thin launcher around a separately supplied agent harness. `EinoADKRunner` directly dispatches first-party implementations of ReAct, router, reflection, tool-calling, plan-execute and workflow patterns. In ReAct mode the worker repeatedly invokes the model, parses a tool call or final answer, executes permitted tools, feeds observations back into the loop and continues until completion or an iteration limit. Reflection similarly implements generate → critique → revise internally. External models and tools provide environmental capability, but the organizational agent loop is supplied by Korus.

The control plane also provides strong deterministic lifecycle machinery. `AgentReconciler` resolves workspace defaults and references, compiles the Agent and sets the declared lifecycle phase. `AgentRunReconciler` advances pending/running/succeeded/failed states, applies operator-authored cancellation, deadlines, retry counts and backoff, and invokes the runtime. These mechanisms enforce current policy and lifecycle but do not themselves own a discretionary whole-system current-control judgment.

Korus additionally ships an `AgentEvaluation` CRD and controller. The controller resolves an Agent, Dataset and optional baseline, creates separate managed `AgentRun` sets for evaluation samples, waits for them to finish, computes evaluator/threshold results, aggregates scores, compares a baseline where configured, calculates `GatePassed`, and stores an evaluation report. This is a first-party complementary audit construction path rather than merely repository test code. At the reviewed revision, however, the Agent publish/release path does not consume that gate: the repository's Phase 3 completeness audit explicitly lists the release-gate decision surface, release gates/waivers, approval queues and audit history as missing/incomplete.

Primary evidence:

- [`README.md`](https://github.com/surefire-ai/korus/blob/ed5ea6a9fca86f43df161a100e913c29fa9b40c9/README.md) — product boundary, operator/worker/evaluation architecture and supported resources.
- [`docs/architecture/component-boundaries.md`](https://github.com/surefire-ai/korus/blob/ed5ea6a9fca86f43df161a100e913c29fa9b40c9/docs/architecture/component-boundaries.md) — control plane, worker execution plane, evaluation and policy boundaries.
- [`internal/worker/eino_runner.go`](https://github.com/surefire-ai/korus/blob/ed5ea6a9fca86f43df161a100e913c29fa9b40c9/internal/worker/eino_runner.go) — standard first-party Eino execution path and pattern dispatch.
- [`internal/worker/react_runner.go`](https://github.com/surefire-ai/korus/blob/ed5ea6a9fca86f43df161a100e913c29fa9b40c9/internal/worker/react_runner.go) — iterative model/tool/observation operational loop.
- [`internal/worker/reflection_runner.go`](https://github.com/surefire-ai/korus/blob/ed5ea6a9fca86f43df161a100e913c29fa9b40c9/internal/worker/reflection_runner.go) — first-party generate/critique/revise operational pattern.
- [`docs/phase2/agent-patterns-and-a2a-todo.md`](https://github.com/surefire-ai/korus/blob/ed5ea6a9fca86f43df161a100e913c29fa9b40c9/docs/phase2/agent-patterns-and-a2a-todo.md) — implemented pattern/SubAgent surfaces and future A2A boundary.
- [`internal/controller/agent_controller.go`](https://github.com/surefire-ai/korus/blob/ed5ea6a9fca86f43df161a100e913c29fa9b40c9/internal/controller/agent_controller.go) — compile/publish status follows the declared Agent lifecycle and does not consume evaluation gate state.
- [`internal/controller/agentrun_controller.go`](https://github.com/surefire-ai/korus/blob/ed5ea6a9fca86f43df161a100e913c29fa9b40c9/internal/controller/agentrun_controller.go) — deterministic AgentRun lifecycle, cancel, timeout and retry enforcement.
- [`api/v1alpha1/supporting_resource_types.go`](https://github.com/surefire-ai/korus/blob/ed5ea6a9fca86f43df161a100e913c29fa9b40c9/api/v1alpha1/supporting_resource_types.go) — AgentPolicy, AgentRun and AgentEvaluation contracts including datasets, evaluators, thresholds, baseline and gate status.
- [`internal/controller/agentevaluation_controller.go`](https://github.com/surefire-ai/korus/blob/ed5ea6a9fca86f43df161a100e913c29fa9b40c9/internal/controller/agentevaluation_controller.go) — managed evaluation runs, metrics, thresholds, baseline comparison, gate verdict and report construction.
- [`docs/phase3/phase3-completeness-audit.md`](https://github.com/surefire-ai/korus/blob/ed5ea6a9fca86f43df161a100e913c29fa9b40c9/docs/phase3/phase3-completeness-audit.md) — explicit gaps in release-gate decision/waiver/approval/audit closure.

## Operational model

A user/operator declares an Agent and its desired lifecycle/configuration. The first-party operator resolves and compiles that declaration into a revisioned runtime artifact. Invocation creates an AgentRun; the first-party worker then executes the selected pattern. In autonomous patterns, the model actor reached through the Korus worker makes task-local reasoning/tool decisions and receives tool/model feedback until the operation returns an output. The AgentRun controller persists lifecycle and result/trace/artifact state around that operation.

Evaluation is a separate first-party path. An AgentEvaluation selects a target Agent, Dataset, evaluators, thresholds and optional baseline. The evaluation controller creates its own managed AgentRuns over the dataset, derives metrics and a gate verdict, and exposes that result in AgentEvaluation status/reporting. At this revision, no standard publish/release/current-control actor automatically consumes the verdict; downstream composition is required to make the audit outcome change subsequent operational commitments.

## S1 — Operations

- State: A
- Function: perform declared agent work through first-party autonomous model/tool execution loops and return operational outputs.
- Disturbance / variety regulated: task uncertainty, model responses, tool/retrieval observations, intermediate reasoning, SubAgent results and stopping decisions needed to satisfy the AgentRun input.
- Decisive decision or feedback right: choose task-local reasoning steps, permitted tool calls or routing actions, interpret observations and decide when an operational answer is complete.
- Decision owner: the autonomous model actor executed through the first-party Korus Eino pattern runner.
- Supporting / enforcement mechanisms: compiled artifact, prompt/model/tool/knowledge bindings, tool allowlists, iteration limits, worker runtime, gateway, AgentRun lifecycle and trace/artifact persistence.
- Closure path: AgentRun reaches the Korus worker → first-party pattern runner invokes the model → model selects a permitted action/tool or final response → tool/SubAgent/model result feeds back into the first-party loop → the loop continues or returns the operational result → AgentRun records the outcome.
- Boundary reachability: `EinoADKRunner` and its built-in pattern handlers are the shipped production worker path at the pinned revision; the release/readiness history explicitly notes that later main replaced the old placeholder with the real Eino runtime and records a passed ReAct smoke test.
- Why this is / is not agent-owned: Korus supplies the loop, context, permitted action surface and feedback transport; the model actor owns the substantive task-local action choice. External model-provider implementation is an environmental dependency rather than a separate agent harness that owns the organizational loop.
- Evidence: [`internal/worker/eino_runner.go`](https://github.com/surefire-ai/korus/blob/ed5ea6a9fca86f43df161a100e913c29fa9b40c9/internal/worker/eino_runner.go), [`internal/worker/react_runner.go`](https://github.com/surefire-ai/korus/blob/ed5ea6a9fca86f43df161a100e913c29fa9b40c9/internal/worker/react_runner.go), [`docs/phase2/agent-patterns-and-a2a-todo.md`](https://github.com/surefire-ai/korus/blob/ed5ea6a9fca86f43df161a100e913c29fa9b40c9/docs/phase2/agent-patterns-and-a2a-todo.md), [`docs/releases/v0.1.0-readiness.md`](https://github.com/surefire-ai/korus/blob/ed5ea6a9fca86f43df161a100e913c29fa9b40c9/docs/releases/v0.1.0-readiness.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: deterministic workflow mode and direct single-model fallback are additional supported modes; the `A` finding is grounded in the shipped autonomous ReAct/router/reflection/plan-execute/tool-calling paths, not in deterministic graph sequencing alone.

## S2 — Coordination

- State: —
- Function: no material first-party S2-specific coordination function is established at the reviewed recursion.
- Disturbance / variety regulated: Korus can route work to SubAgents, execute DAG dependencies and pass parent state into nested AgentRuns, but no inspected standard path identifies a concrete interaction-generated conflict, inconsistency or oscillation among distinct S1 units and attenuates that disturbance through an S2-specific relation.
- Decisive decision or feedback right: not established for S2.
- Decision owner: not established.
- Supporting / enforcement mechanisms: router classification, SubAgent references/invocation, workflow graph edges, state propagation and compiler cycle checks.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: a router chooses which specialist receives work and a workflow sequences nodes, but delegation/routing/sequencing are not S2 unless tied to a reconstructed inter-S1 disturbance and returned coordination feedback.
- Evidence: [`internal/worker/router_runner.go`](https://github.com/surefire-ai/korus/blob/ed5ea6a9fca86f43df161a100e913c29fa9b40c9/internal/worker/router_runner.go), [`internal/worker/workflow_runner.go`](https://github.com/surefire-ai/korus/blob/ed5ea6a9fca86f43df161a100e913c29fa9b40c9/internal/worker/workflow_runner.go), [`docs/phase2/agent-patterns-and-a2a-todo.md`](https://github.com/surefire-ai/korus/blob/ed5ea6a9fca86f43df161a100e913c29fa9b40c9/docs/phase2/agent-patterns-and-a2a-todo.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: full Agent Mesh/A2A is explicitly future work at this revision; downstream compositions may introduce S2-specific regulation without changing this repository-relative result.

### Absence scope

- Surfaces inspected: router pattern, SubAgent bindings/invocation, workflow graph execution, graph/compiler cycle checks, parent-run state propagation and A2A/Agent Mesh roadmap notes.
- Plausible first-party paths checked: classifier-based specialist routing, nested Agent invocation, workflow DAG sequencing, shared graph state and future A2A surfaces.
- Why no material first-party path remains: the implemented mechanisms communicate, delegate, sequence or prevent graph cycles; none is evidenced as regulating a concrete disturbance generated by interaction among distinct S1 units with an S2-specific feedback path into their subsequent behaviour.

## S3 — Inside-and-now control

- State: —
- Function: no autonomous or constructor whole-system current-control function is established at the declared boundary.
- Disturbance / variety regulated: the operator tracks readiness and current run state and enforces configured cancellation, deadlines, retry limits, workspace/provider constraints and lifecycle phase, but these are deterministic reconciliations of already-authored rules/requests.
- Decisive decision or feedback right: discretionary choices such as desired lifecycle phase, cancellation and retry/deadline parameters remain external spec/operator decisions; the controllers enforce them.
- Decision owner: no first-party autonomous S3 owner established.
- Supporting / enforcement mechanisms: Agent and AgentRun status, Kubernetes reconcilers, workspace defaults, compiler validation, cancellation, timeout, retry/backoff and runtime status transitions.
- Closure path: external specification/current request → deterministic controller reconciliation/enforcement → Agent/AgentRun state changes. No autonomous whole-system current view → discretionary commitment/resource/intervention decision → returned operational change loop is established.
- Why this is / is not agent-owned: controller authority to retry, fail, cancel or publish according to authored fields is enforcement authority, not evidence that an autonomous actor owns the organizational current-control choice.
- Evidence: [`internal/controller/agent_controller.go`](https://github.com/surefire-ai/korus/blob/ed5ea6a9fca86f43df161a100e913c29fa9b40c9/internal/controller/agent_controller.go), [`internal/controller/agentrun_controller.go`](https://github.com/surefire-ai/korus/blob/ed5ea6a9fca86f43df161a100e913c29fa9b40c9/internal/controller/agentrun_controller.go), [`api/v1alpha1/agent_types.go`](https://github.com/surefire-ai/korus/blob/ed5ea6a9fca86f43df161a100e913c29fa9b40c9/api/v1alpha1/agent_types.go).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: the Web Console and operator give humans substantial operational control, but Methodology `0.3.6` does not award S3 parent notation from generic configuration/lifecycle intervention without an evidenced whole-system parent current-control loop.

### Absence scope

- Surfaces inspected: Agent lifecycle reconciliation, AgentRun lifecycle/state machine, retries/deadlines/cancel, workspace/provider policy enforcement, gateway/runtime dispatch and manager/Web Console architecture notes.
- Plausible first-party paths checked: operator as manager, retry/recovery as intervention, lifecycle publish phase, cancellation/timeout, workspace defaults and Web Console current-state views.
- Why no material first-party path remains: these paths deterministically enforce authored state or expose operator controls. No standard first-party autonomous actor observes the current organization as a whole and owns discretionary decisions over its current commitments/resources/priorities.

## S3* — Complementary audit

- State: C
- Function: independently exercise a target Agent revision against a declared evaluation dataset, optionally compare a separate baseline, derive evaluator/threshold results and expose a gate verdict/report as complementary evidence about operational capability.
- Disturbance / variety regulated: uncertainty that ordinary successful AgentRun reporting accurately implies the target revision satisfies externally declared quality/behaviour expectations across representative samples or against a baseline.
- Decisive decision or feedback right: the first-party AgentEvaluation contract exposes an audit-specific `GatePassed` result derived from evaluator/threshold outcomes and baseline comparison; downstream composition must still decide how that verdict changes release/current operation.
- Decision owner: no autonomous audit authority is bundled for the final corrective decision. The first-party evaluation controller owns execution and deterministic derivation of the declared audit contract, while the developer/operator must compose the actor/authority and return closure that consumes the verdict.
- Supporting / enforcement mechanisms: AgentEvaluation CRD, Dataset samples/expected values, evaluator and threshold specs, optional baseline Agent/revision, controller-owned evaluation AgentRuns, metric aggregation, report construction and `GatePassed` status.
- Closure path: AgentEvaluation selects target revision + independent dataset/evaluator contract → evaluation controller creates separate managed AgentRuns → results are evaluated/thresholded and optionally compared with a baseline → `GatePassed` and report are returned on AgentEvaluation status → **constructor gap:** no standard release/current-control actor consumes that verdict to alter subsequent operation at this revision.
- Boundary reachability: AgentEvaluation is a shipped first-party CRD/controller in the standard operator, not repository-only benchmark/test code. The Phase 3 audit confirms evaluation foundations exist while separately identifying the missing release-gate decision/waiver/approval closure.
- Why this is / is not agent-owned: Korus intentionally exposes the complementary audit path itself, which is enough for `C`; it does not ship an autonomous actor that owns the decisive audit-to-operation response, so the path is not `A`.
- Evidence: [`api/v1alpha1/supporting_resource_types.go`](https://github.com/surefire-ai/korus/blob/ed5ea6a9fca86f43df161a100e913c29fa9b40c9/api/v1alpha1/supporting_resource_types.go), [`internal/controller/agentevaluation_controller.go`](https://github.com/surefire-ai/korus/blob/ed5ea6a9fca86f43df161a100e913c29fa9b40c9/internal/controller/agentevaluation_controller.go), [`docs/phase3/phase3-completeness-audit.md`](https://github.com/surefire-ai/korus/blob/ed5ea6a9fca86f43df161a100e913c29fa9b40c9/docs/phase3/phase3-completeness-audit.md), [`internal/controller/agent_controller.go`](https://github.com/surefire-ai/korus/blob/ed5ea6a9fca86f43df161a100e913c29fa9b40c9/internal/controller/agent_controller.go).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the audit contract can be human-authored and much evaluator logic is deterministic. `C` is based on the first-party S3*-specific feedback construction path, not on treating deterministic threshold enforcement as autonomous organizational judgment. A future release-gate/current-control consumer could change the ownership classification on reassessment.
- Claim being audited: the selected current Agent revision satisfies the declared dataset/evaluator/threshold contract and, when configured, compares acceptably with the selected baseline.
- Ordinary reporting path: ordinary AgentRuns expose run phase, output, trace references, artifacts and agent revision through the normal execution lifecycle.
- Complementary access path: the AgentEvaluation controller independently creates its own labelled managed AgentRuns over Dataset samples and evaluates those outputs against expected values/evaluators/thresholds, with optional separate baseline runs.
- Independence boundary: evaluation has a distinct CRD/controller, sample set, evaluator/threshold contract and managed-run ownership from ordinary invocation/reporting. It exercises the same target Agent/runtime intentionally, but does not rely solely on the ordinary AgentRun's claim of success.
- Who acts on findings: no standard first-party release/current-control actor at the reviewed revision; the developer/operator must compose a consumer of `GatePassed`/reporting, which is the reason for `C` rather than `A`.

## S4 — Outside-and-then intelligence

- State: —
- Function: no external-and-prospective organizational adaptation loop is established in the standard distribution.
- Disturbance / variety regulated: reflection can improve the output of the current task and evaluation can identify regressions/threshold failures, but neither path autonomously converts future/environment distinctions into persistent capability changes for later operation.
- Decisive decision or feedback right: no first-party actor owns a prospective adaptation choice over the organization's persistent capability/repertoire.
- Decision owner: none established.
- Supporting / enforcement mechanisms: reflection generate/critique/revise loop, evaluation baseline comparison, Agent/Skill/Prompt/Policy declarative resources, revisioned compilation and roadmap/product-development feedback.
- Closure path: not applicable for the negative finding; no outside/future distinction → adaptation option → returned persistent capability change loop is supplied.
- Why this is / is not agent-owned: reflection is task-local S1 self-correction and evaluation produces audit evidence. Updating prompts, agents, skills, policies or releases from that evidence remains an external developer/operator action at this revision.
- Evidence: [`internal/worker/reflection_runner.go`](https://github.com/surefire-ai/korus/blob/ed5ea6a9fca86f43df161a100e913c29fa9b40c9/internal/worker/reflection_runner.go), [`internal/controller/agentevaluation_controller.go`](https://github.com/surefire-ai/korus/blob/ed5ea6a9fca86f43df161a100e913c29fa9b40c9/internal/controller/agentevaluation_controller.go), [`docs/phase3/phase3-completeness-audit.md`](https://github.com/surefire-ai/korus/blob/ed5ea6a9fca86f43df161a100e913c29fa9b40c9/docs/phase3/phase3-completeness-audit.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: future release/revision workflows may connect evaluation evidence to adaptation, but design intent and developer iteration are not credited as runtime S4.

### Absence scope

- Surfaces inspected: reflection runner, evaluation/baseline comparison, Agent lifecycle/revision compilation, Skill/Prompt/Policy resources, Phase 3 product audit and Agent Mesh/A2A roadmap.
- Plausible first-party paths checked: reflection, evaluation regressions, revision compilation, prompt/skill updates, provider capability work and roadmap feedback.
- Why no material first-party path remains: current-runtime reflection changes only the current output; evaluation stops at evidence/gate status; persistent capability changes still require externally authored specs/software or a future release/adaptation workflow.

## S5 — Policy and identity

- State: —
- Function: no runtime identity/ultimate-policy decision loop is established at the declared recursion.
- Disturbance / variety regulated: AgentPolicy, workspace provider policy, guardrails, budgets, allowed models/tools and desired lifecycle phase constrain what the system may do, but they are authored externally and deterministically resolved/enforced.
- Decisive decision or feedback right: identity, ultimate purpose and top-level policy contents remain with the user/operator/developer outside the first-party autonomous runtime.
- Decision owner: no first-party autonomous or operationally closed parent S5 authority established.
- Supporting / enforcement mechanisms: AgentPolicy CRD, workspace policy/defaults, Agent desired phase, prompt/spec resources, compiler validation and runtime/tool constraints.
- Closure path: external authority authors policy/specification → first-party compiler/controller/runtime enforce it. No identity/ultimate-policy issue is autonomously adjudicated and returned through a first-party S5 closure loop.
- Why this is / is not agent-owned: static policy objects and hard enforcement express governance constraints but do not themselves own the ultimate policy decision right.
- Evidence: [`api/v1alpha1/supporting_resource_types.go`](https://github.com/surefire-ai/korus/blob/ed5ea6a9fca86f43df161a100e913c29fa9b40c9/api/v1alpha1/supporting_resource_types.go), [`api/v1alpha1/agent_types.go`](https://github.com/surefire-ai/korus/blob/ed5ea6a9fca86f43df161a100e913c29fa9b40c9/api/v1alpha1/agent_types.go), [`internal/controller/agent_controller.go`](https://github.com/surefire-ai/korus/blob/ed5ea6a9fca86f43df161a100e913c29fa9b40c9/internal/controller/agent_controller.go).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: human/operator authorship is real governance, but generic configuration authority does not establish Methodology `P` without a reconstructed identity/ultimate-policy issue and return-to-operation loop.

### Absence scope

- Surfaces inspected: AgentPolicy, Workspace/Tenant governance/provider fields, Agent desired lifecycle phase, compiler/reference resolution, runtime constraints and Phase 3 governance gaps.
- Plausible first-party paths checked: policies/guardrails/budgets, allowed models/tools, workspace governance, desired publish phase, human-in-the-loop configuration and administration roadmap.
- Why no material first-party path remains: all identified paths encode or enforce externally selected constraints; none supplies a first-party identity/ultimate-policy decision actor plus authoritative return closure.

## Recursion

Korus supports composition through SubAgents and workflow agent nodes, but nesting/delegation alone is not credited as full VSM recursion. A SubAgent may independently satisfy an operational S1 loop, yet the reviewed standard distribution does not demonstrate each nested unit carrying its own full S1–S5 metasystem. The assessment therefore keeps the platform/managed-agent organization as the declared recursion and treats SubAgent nesting only as operational composition evidence.

## Variety and escalation

Korus attenuates substantial execution variety through compiled references, model/tool/knowledge allowlists, workspace/provider constraints, graph validation, pattern iteration limits, AgentRun timeout/retry/cancel, artifact/trace recording, and Kubernetes reconciliation. Autonomous S1 loops amplify useful action variety by selecting model/tool/SubAgent actions inside those constraints.

Escalation is largely declarative/operator-owned. Human-in-the-loop and governance fields exist as policy surfaces, and failed/current runs can be canceled or reconfigured, but the reviewed runtime does not establish an autonomous S3/S5 escalation hierarchy. Evaluation adds a structured complementary evidence/gate path, but the Phase 3 audit confirms that release-gate/waiver/approval closure still has to be composed.

## Evidence gaps

- The repository is young and the pinned revision includes active Phase 3 development; later releases may quickly close release/evaluation and governance loops.
- Full Agent Mesh/A2A support is explicitly future work and is not credited from roadmap intent.
- Evaluation gate semantics are implemented as a first-party constructor primitive, but no standard release/publish/current-control consumer of `GatePassed` was found at the reviewed revision.
- Web Console/detail surfaces are not used to infer organizational ownership where the repository's own completeness audit describes them as incomplete/static.

## Standalone result

`S1=A / S2=— / S3=— / S3*=C / S4=— / S5=—`.

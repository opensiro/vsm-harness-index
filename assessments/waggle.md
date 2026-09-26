---
harness_id: waggle
project_name: Waggle
repository: https://github.com/CrewBeeLab/Waggle
review_ref: db9e3d3aed66714d665fd1c5c40d66534bf44ed7
reviewed_at: 2026-09-27
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-27
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Waggle

## Review boundary

- System in focus: the first-party Waggle governed Agent Harness / Agent Control Plane at pinned revision `db9e3d3aed66714d665fd1c5c40d66534bf44ed7`, including Project/Session/AgentRun lifecycle, AgentPackage loading, model/context/tool bridges, the production `PiCoreAdapter`, `RuntimeToolExecutor`, `RunPermissionBoundary`, Tool Proxy, Workspace Guard, confirmations, durable run state, events/evidence and local runner execution.
- Purpose and identity: execute a product-facing agent task inside a short-lived governed run while Waggle constrains model/tool/workspace access, persists run state and returns evidence/results to the client or product.
- Relevant environment: user/product task input; external LLM providers; product tool providers and business backends; project/workspace state; configured AgentPackages; model/tool failures; client disconnect/cancel/confirmation decisions; storage and deployment infrastructure.
- Standard-distribution boundary: the public Waggle TypeScript workspace, including `packages/core`, `packages/protocol`, `packages/runtime-pi`, Control Plane, runner/CLI surfaces and documented local/self-hosted deployment. `@earendil-works/pi-agent-core`, model providers, Product Providers/business backends, databases and external products remain dependencies or environment; their independent organizational functions are not imported.
- Credited operating / distribution surfaces: `README.md`; `docs/development/architecture.md`; `docs/development/current-implementation.md`; `packages/runtime-pi/src/pi-core-adapter.ts`; `packages/core/src/runtime/run-orchestrator.ts`; `packages/core/src/runtime/local-run-execution-service.ts`; `packages/core/src/runtime/runtime-tool-executor.ts`; `packages/core/src/permissions/run-permission-boundary.ts`; `packages/core/src/permissions/permission-guard.ts`; AgentPackage registry/eval/release services; confirmation flow and run/event/evidence APIs.
- Adjacent first-party surfaces excluded from ownership: repository CI/release governance; development target architecture not yet implemented at the frozen ref; mock/faux-provider test behavior as proof of reachability rather than autonomous production cognition; sample Product Providers and product-specific package fixtures; external product final-write logic.
- First-party operating / deployment modes considered: documented local/self-hosted Control Plane with a real model-backed `AgentRun` using production-default `PiCoreAdapter`, Waggle Model Gateway, Tool Proxy/Workspace Guard and optional Direct-Mode or product-owned confirmation. The current executable baseline is used; target/future parent-child orchestration and remote distributed scheduling are not credited.
- Recursion level: one Waggle-managed AgentRun as the operating organization. Project/session state provides its durable context and governance container. A downstream product may compose multiple runs or agent packages into a larger organization, but that higher recursion is not imported into this generic assessment.
- Reviewed revision: `db9e3d3aed66714d665fd1c5c40d66534bf44ed7`.
- Observation date: 2026-09-27.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Waggle separates product authority, harness governance and generic runtime mechanics. The product owns business data/rules, user identity, confirmation UX and final business writes. Waggle owns AgentPackage loading, Project/Session/Run lifecycle, model/provider surfaces, permission compilation, tool/workspace enforcement, events, trace/audit/evidence and runtime hosting. The README describes PI Core as the current execution substrate behind an adapter boundary rather than as the product/control authority.

That external dependency does not reduce Waggle to a governance-only wrapper. `packages/runtime-pi/src/pi-core-adapter.ts` imports Pi Core's generic `runAgentLoop`, but the Waggle adapter constructs the `AgentContext` from Waggle system prompt/context, supplies Waggle-resolved model binding and Waggle-owned tool objects, routes every selected tool call into first-party `RuntimeToolExecutor.execute()` under the run's `RunPermissionBoundary`, returns the governed tool result to the model loop, persists loop events through Waggle state and owns lifecycle/messages/retry/resume. The standard self-hosted product therefore contains a reachable model-driven operational feedback loop even though loop mechanics are implemented by a third-party library dependency.

Governance is strong but intentionally bounded. Every run receives an immutable `RunPermissionBoundary` compiled from configured package/project/provider/model/sandbox/user/confirmation inputs. `PermissionGuard` deterministically maps a proposed tool action to allow, ask or deny. High-impact actions can pause on a product/user confirmation and resume the same ToolCall. Run scheduling, leases, watchdog/recovery, terminal state and evidence preserve lifecycle correctness. These are meaningful execution constraints, but the frozen implementation does not supply a separate autonomous whole-system manager choosing current priorities/resources/constraints from operational evidence; the decisive policies are pre-authored and confirmations concern individual proposed effects.

The AgentPackage registry similarly exposes validate/eval/release/rollback/deprecate lifecycle. At this revision its minimum eval path checks package-declared required cases and moves version status deterministically; it does not constitute a separately situated runtime auditor or an outside-and-prospective adaptation actor. The architecture document explicitly labels parent/child orchestration, richer concurrency and distributed scheduling as target evolution, while `current-implementation.md` distinguishes those targets from executable truth.

Primary evidence:

- [`README.md`](https://github.com/CrewBeeLab/Waggle/blob/db9e3d3aed66714d665fd1c5c40d66534bf44ed7/README.md) — product/Waggle/runtime responsibility split, current PI-backed execution, run flow, Tool Proxy/Workspace Guard, confirmations, evidence and final-write ownership.
- [`docs/development/architecture.md`](https://github.com/CrewBeeLab/Waggle/blob/db9e3d3aed66714d665fd1c5c40d66534bf44ed7/docs/development/architecture.md) — current package boundaries and explicit separation of current implementation from target parent/child/distributed evolution.
- [`docs/development/current-implementation.md`](https://github.com/CrewBeeLab/Waggle/blob/db9e3d3aed66714d665fd1c5c40d66534bf44ed7/docs/development/current-implementation.md) — executable baseline, `PiCoreAdapter.execute()`, Model Gateway, runtime tools, confirmations, runner state, watchdog/recovery and stated current gaps.
- [`packages/runtime-pi/src/pi-core-adapter.ts`](https://github.com/CrewBeeLab/Waggle/blob/db9e3d3aed66714d665fd1c5c40d66534bf44ed7/packages/runtime-pi/src/pi-core-adapter.ts) — production adapter, Waggle-owned context/model/tool bridges and closed model→tool→result loop over Pi Core mechanics.
- [`packages/core/src/runtime/run-orchestrator.ts`](https://github.com/CrewBeeLab/Waggle/blob/db9e3d3aed66714d665fd1c5c40d66534bf44ed7/packages/core/src/runtime/run-orchestrator.ts) — deterministic run stages, first-party permission/persistence ownership and adapter/tool/evidence routing.
- [`packages/core/src/permissions/run-permission-boundary.ts`](https://github.com/CrewBeeLab/Waggle/blob/db9e3d3aed66714d665fd1c5c40d66534bf44ed7/packages/core/src/permissions/run-permission-boundary.ts) and [`permission-guard.ts`](https://github.com/CrewBeeLab/Waggle/blob/db9e3d3aed66714d665fd1c5c40d66534bf44ed7/packages/core/src/permissions/permission-guard.ts) — precompiled per-run authority and deterministic allow/ask/deny enforcement.
- [`packages/core/src/registry/agent-package-registry-service.ts`](https://github.com/CrewBeeLab/Waggle/blob/db9e3d3aed66714d665fd1c5c40d66534bf44ed7/packages/core/src/registry/agent-package-registry-service.ts) and [`packages/core/src/evals/index.ts`](https://github.com/CrewBeeLab/Waggle/blob/db9e3d3aed66714d665fd1c5c40d66534bf44ed7/packages/core/src/evals/index.ts) — package validation/eval/release/rollback state rather than an independent operational audit/adaptation loop.

## Operational model

A client creates a Project/Session/AgentRun. Waggle resolves the AgentPackage, model, provider/tool/workspace/actor context and compiles the immutable run authority boundary. The selected runtime adapter receives the packaged context and model binding. In the production-default Pi Core path, the model makes task-specific choices; a proposed tool call is represented as a Waggle tool whose executor enters `RuntimeToolExecutor`, checks the run boundary/permission/confirmation rules, executes an allowed capability, and returns a governed result into the same model loop. Waggle persists run messages/events/evidence and owns cancellation/terminal lifecycle.

If a tool requires confirmation, Direct Mode asks the user through Waggle's client; product-integrated mode lets the product render/decide the domain-specific effect. Approval resumes the same ToolCall and denial stops or fails that action. The product may then perform an external final business write and attach its result as evidence. This return path is intentionally narrow: it is action authorization, not evidence of autonomous S3/S5 ownership by Waggle.

## S1 — Operations

- State: A
- Function: perform the substantive model-driven task of the governed AgentRun by choosing task-relevant actions/tools from current context, consuming tool observations and continuing until a terminal answer/state.
- Disturbance / variety regulated: open-ended user/product task input; model uncertainty; changing workspace/tool results; allowed capability set; model/tool failures; confirmation outcomes; bounded context and cancellation.
- Decisive decision or feedback right: choose the next task-specific action/tool call and arguments from the current conversation/observations, then decide whether further actions are required or the run can complete.
- Decision owner: the autonomous model actor instantiated through Waggle's first-party production `PiCoreAdapter` operating mode.
- Supporting / enforcement mechanisms: external Pi Core loop primitive; Waggle Model Gateway; packed context/system prompt; Waggle tool wrappers; `RuntimeToolExecutor`; `RunPermissionBoundary`; Permission Guard; Workspace Guard; event sink; durable run lifecycle and cancellation.
- Closure path: AgentRun input/context -> Waggle `PiCoreAdapter.execute()` constructs model/context/tools -> model chooses a tool/action -> Waggle tool wrapper enters `RuntimeToolExecutor` -> governed tool result returns as Pi/model observation -> subsequent model turn changes action or produces terminal text -> Waggle completes the run and persists evidence.
- Boundary reachability: the README's documented `run`/HTTP path starts a real task through the Control Plane, and `current-implementation.md` identifies local `PiCoreAdapter.execute()` through Pi Core as current executable production-default runtime behavior rather than target architecture.
- Why this is / is not agent-owned: Pi Core supplies generic loop mechanics and Waggle supplies policy/lifecycle plumbing, but neither deterministic layer preselects the contextual task action. Removing the model actor while retaining those mechanisms would not yield materially the same tool/argument/termination choices. The external loop library is an implementation dependency, not a separately deployed worker organization whose VSM functions are inherited.
- Evidence: [`README.md`](https://github.com/CrewBeeLab/Waggle/blob/db9e3d3aed66714d665fd1c5c40d66534bf44ed7/README.md); [`docs/development/current-implementation.md`](https://github.com/CrewBeeLab/Waggle/blob/db9e3d3aed66714d665fd1c5c40d66534bf44ed7/docs/development/current-implementation.md); [`packages/runtime-pi/src/pi-core-adapter.ts`](https://github.com/CrewBeeLab/Waggle/blob/db9e3d3aed66714d665fd1c5c40d66534bf44ed7/packages/runtime-pi/src/pi-core-adapter.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: product-specific tools and final business effects remain outside Waggle. The S1 claim covers task decisions within the capabilities exposed to the governed run, not business authority that the README explicitly reserves to the product.

## S2 — Coordination

- State: —
- Function: no qualifying inter-S1 coordination function is established in the current generic standard distribution at the assessed AgentRun recursion.
- Disturbance / variety regulated: the repository has Project/Session/Run state, queues/workers and future parent-child concepts, but no current first-party witness establishes distinct S1 operational units plus a concrete interaction disturbance and S2-specific attenuation relation.
- Decisive decision or feedback right: none established for S2.
- Decision owner: none established.
- Supporting / enforcement mechanisms: session/run state; queue/worker records; run orchestration; Tool Proxy; shared evidence; planned parent/child topology.
- Closure path: no current distinct-S1 disturbance -> S2-specific coordination judgment -> changed behaviour of the affected S1 units is established.
- Why this is / is not agent-owned: ordinary queueing, shared records and run orchestration coordinate software execution, but Methodology 0.3.6 does not award S2/C from generic communication/scheduling primitives. The architecture explicitly places parent-child orchestration in target evolution rather than current executable truth.
- Evidence: [`docs/development/architecture.md`](https://github.com/CrewBeeLab/Waggle/blob/db9e3d3aed66714d665fd1c5c40d66534bf44ed7/docs/development/architecture.md); [`docs/development/current-implementation.md`](https://github.com/CrewBeeLab/Waggle/blob/db9e3d3aed66714d665fd1c5c40d66534bf44ed7/docs/development/current-implementation.md); [`packages/core/src/runtime/run-orchestrator.ts`](https://github.com/CrewBeeLab/Waggle/blob/db9e3d3aed66714d665fd1c5c40d66534bf44ed7/packages/core/src/runtime/run-orchestrator.ts).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: a later implemented parent/child/multi-run organization or downstream product can create a different recursion that requires separate assessment.

### Absence scope

- Surfaces inspected: current run model, scheduler/worker lifecycle, Project/Session records, run orchestration, Tool Proxy, current-implementation gaps and target parent/child architecture.
- Plausible first-party paths checked: multiple runs; worker pool/leases; parent-child fields/design; shared Project state; tool/provider routing; session continuity.
- Why no material first-party path remains: current plurality is lifecycle/execution plumbing. The source explicitly treats full parent-child orchestration as future work and provides no current inter-S1 disturbance/attenuation witness at the assessed recursion.

## S3 — Inside-and-now control

- State: —
- Function: no separate first-party whole-system current-control decision loop is established beyond the governed S1 run and deterministic enforcement of preselected constraints.
- Disturbance / variety regulated: tool risk, actor/package/workspace mismatch, expired authority, model/tool availability, cancellation, lease/watchdog failures and confirmation-required effects are regulated mechanically or by a local parent decision, but the frozen boundary does not show a manager selecting current priorities/resources/commitments/constraints for the whole from a current operational view.
- Decisive decision or feedback right: none established for a qualifying S3 function.
- Decision owner: none established for qualifying S3.
- Supporting / enforcement mechanisms: immutable `RunPermissionBoundary`; Permission Guard; RuntimeToolExecutor; run statuses; worker scheduling/leases; watchdog/recovery; cancellation; user/product confirmations; package/run configuration.
- Closure path: configured authority -> deterministic allow/ask/deny and lifecycle enforcement -> current run behavior changes. This is strong enforcement, but no distinct whole-system S3 discretion/feedback loop is supplied.
- Boundary reachability: all mechanisms are present in current execution, but they remain pre-authored enforcement/lifecycle paths rather than a separately owned current-control function.
- Why this is / is not agent-owned: the model proposes an S1 action; the guard applies already-selected rules; a human/product can approve one specific effect. Removing the putative manager leaves the same deterministic rule enforcement because there is no autonomous manager to remove. Ordinary one-action approval does not satisfy the Methodology's parent-governed S3 witness.
- Whole-system current view: Waggle exposes run/session/events/evidence/attention state, but visibility is not itself a current-control decision right.
- Current-control decision scope: cancellation, confirmation and permission effects are local/run-lifecycle decisions; no qualifying resource/priority/accountability/synergy intervention for the whole is established.
- Evidence: [`README.md`](https://github.com/CrewBeeLab/Waggle/blob/db9e3d3aed66714d665fd1c5c40d66534bf44ed7/README.md); [`packages/core/src/permissions/run-permission-boundary.ts`](https://github.com/CrewBeeLab/Waggle/blob/db9e3d3aed66714d665fd1c5c40d66534bf44ed7/packages/core/src/permissions/run-permission-boundary.ts); [`packages/core/src/permissions/permission-guard.ts`](https://github.com/CrewBeeLab/Waggle/blob/db9e3d3aed66714d665fd1c5c40d66534bf44ed7/packages/core/src/permissions/permission-guard.ts); [`apps/cli/src/run-confirmation-flow.ts`](https://github.com/CrewBeeLab/Waggle/blob/db9e3d3aed66714d665fd1c5c40d66534bf44ed7/apps/cli/src/run-confirmation-flow.ts); [`docs/development/current-implementation.md`](https://github.com/CrewBeeLab/Waggle/blob/db9e3d3aed66714d665fd1c5c40d66534bf44ed7/docs/development/current-implementation.md).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: product-owned business authority is real, but the evidence at this recursion concerns individual business-effect confirmation/final write or preconfigured rules, not an S3 whole-system current-control function.

### Absence scope

- Surfaces inspected: run permission compilation/validation, Permission Guard, Tool Proxy, confirmation flow, run orchestrator, worker scheduling/leases/watchdogs/recovery, attention/evidence surfaces, current implementation and target architecture.
- Plausible first-party paths checked: guard as S3; run orchestrator as S3; operator/product confirmation as `P`; worker watchdog/recovery; package policy; active-task/attention views.
- Why no material first-party path remains: guards and lifecycle code enforce previously selected constraints; confirmations are effect-local authorization; current views expose state but do not autonomously select whole-system current-control interventions. No S3-specific constructor path beyond generic configuration/enforcement is established.

## S3* — Complementary audit

- State: —
- Function: no materially independent complementary audit judgment with corrective return into subsequent operation is established in the current runtime.
- Disturbance / variety regulated: Waggle records trace, audit, evidence, permission decisions, artifacts and package eval/release state, but these surfaces are produced by or validate the same governed execution/lifecycle paths.
- Decisive decision or feedback right: none established for an independent auditor that challenges operational claims from complementary access and returns a correction.
- Decision owner: none established.
- Supporting / enforcement mechanisms: trace/audit/evidence stores; governed-run evidence; validation/eval types; package registry validation; confirmation records; hash/provenance checks.
- Closure path: operation/control -> records/checks/evidence; no independent audit actor/judgment -> corrective instruction -> changed and rechecked operation loop is supplied.
- Why this is / is not agent-owned: logging, deterministic contract validation, package lifecycle checks and human confirmation are not independent operational audit by themselves.
- Evidence: [`docs/development/current-implementation.md`](https://github.com/CrewBeeLab/Waggle/blob/db9e3d3aed66714d665fd1c5c40d66534bf44ed7/docs/development/current-implementation.md); [`packages/core/src/evals/index.ts`](https://github.com/CrewBeeLab/Waggle/blob/db9e3d3aed66714d665fd1c5c40d66534bf44ed7/packages/core/src/evals/index.ts); [`packages/core/src/registry/agent-package-registry-service.ts`](https://github.com/CrewBeeLab/Waggle/blob/db9e3d3aed66714d665fd1c5c40d66534bf44ed7/packages/core/src/registry/agent-package-registry-service.ts).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: downstream AgentPackages may define reviewers/evals, but application-specific reviewers are not credited to generic Waggle without a first-party standard path that closes independence and corrective feedback.

### Absence scope

- Surfaces inspected: trace/audit/evidence, permission decisions, confirmation state, package validation/evals/releases, artifacts and current runtime lifecycle.
- Plausible first-party paths checked: audit log; governed evidence; package eval; validation; product confirmation; watchdog/recovery; release rollback.
- Why no material first-party path remains: these are evidence/enforcement/lifecycle checks without a separately situated audit judgment over operational reality and a corrective-return/re-audit loop.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party prospective environment-facing adaptation loop is established in the current standard operating mode.
- Disturbance / variety regulated: model/provider catalogs, package versions, eval declarations, memory and product integrations can change across deployments/runs, but changes are operator/developer-authored or deterministic lifecycle state rather than autonomous sensing of external/future distinctions and option development.
- Decisive decision or feedback right: none established for selecting and adopting a future capability/posture based on environmental intelligence.
- Decision owner: none established.
- Supporting / enforcement mechanisms: AgentPackage versions; validate/eval/release/rollback/deprecate APIs; model catalog/connections; persistent context/memory; proposals; development hot reload.
- Closure path: operator/developer supplies new package/config/version -> Waggle validates/releases/uses it. No environment sensing -> prospective options -> autonomous adaptation judgment -> returned changed present capability loop closes.
- Why this is / is not agent-owned: package lifecycle machinery can promote or roll back supplied artifacts, but the frozen `runMinimumEval()` does not itself generate capability alternatives or adapt from external distinctions. Persistence/reuse and model selection are not S4 by name.
- Evidence: [`packages/core/src/registry/agent-package-registry-service.ts`](https://github.com/CrewBeeLab/Waggle/blob/db9e3d3aed66714d665fd1c5c40d66534bf44ed7/packages/core/src/registry/agent-package-registry-service.ts); [`docs/development/architecture.md`](https://github.com/CrewBeeLab/Waggle/blob/db9e3d3aed66714d665fd1c5c40d66534bf44ed7/docs/development/architecture.md); [`docs/development/current-implementation.md`](https://github.com/CrewBeeLab/Waggle/blob/db9e3d3aed66714d665fd1c5c40d66534bf44ed7/docs/development/current-implementation.md).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: AgentPackage lifecycle provides useful construction/release infrastructure, but Methodology `C` still requires the S4 function itself to be established; a generic package/version API is not enough.

### Absence scope

- Surfaces inspected: AgentPackage authoring/registry/eval/release/rollback/deprecate, memory/context, model catalog/connections, proposals, package hot reload, product integrations and current-vs-target architecture.
- Plausible first-party paths checked: eval-driven package promotion; release rollback; memory reuse; model catalog changes; development hot reload; package proposals.
- Why no material first-party path remains: the current system validates and deploys externally authored alternatives. It does not itself sense outside/future conditions, generate adaptation options and close the adoption decision back into present capability.

## S5 — Policy and identity

- State: —
- Function: no first-party identity/ultimate-policy decision loop closes at the Waggle-managed run recursion.
- Disturbance / variety regulated: Product/AgentPackage policy, allowed/denied tools, user/workspace permissions, model/provider restrictions, confirmation rules and business ownership constrain the run, but ultimate purpose/business identity remains externally authored.
- Decisive decision or feedback right: define/revise the ultimate purpose, identity or top-level normative policy of the operating organization itself.
- Decision owner: external product/operator/developer; no qualifying first-party S5 closure is established.
- Supporting / enforcement mechanisms: AgentPackage manifest/profile/policy; Project/ProductIntegration records; `RunPermissionBoundary`; confirmation rules; user identity; product-owned final writes; package release state.
- Closure path: product/operator supplies purpose/policy -> Waggle compiles/enforces it. No identity-level dispute/proposal -> authoritative S5 judgment -> returned ultimate policy -> subsequent operation loop closes inside Waggle.
- Why this is / is not agent-owned: the README explicitly reserves business rules, user identity, confirmation UX and final writes to the product. This is parent/external authority, but the evidenced runtime return paths are configuration and individual effect authorization, not a genuine identity-level deliberation/decision path required for `S5=P`.
- Evidence: [`README.md`](https://github.com/CrewBeeLab/Waggle/blob/db9e3d3aed66714d665fd1c5c40d66534bf44ed7/README.md); [`packages/core/src/permissions/run-permission-boundary.ts`](https://github.com/CrewBeeLab/Waggle/blob/db9e3d3aed66714d665fd1c5c40d66534bf44ed7/packages/core/src/permissions/run-permission-boundary.ts); [`apps/cli/src/run-confirmation-flow.ts`](https://github.com/CrewBeeLab/Waggle/blob/db9e3d3aed66714d665fd1c5c40d66534bf44ed7/apps/cli/src/run-confirmation-flow.ts).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: a downstream product organization may have legitimate S5 authority and use Waggle as enforcement infrastructure. That parent organization is a different system-in-focus; its authority is not converted into generic Waggle S5 merely because Waggle can enforce supplied policy.

### Absence scope

- Surfaces inspected: AgentPackage policy/profile, Project/ProductIntegration, run permission boundary, user/product confirmation, model/tool restrictions, final-write ownership, package lifecycle and governance docs.
- Plausible first-party paths checked: Product final authority as `P`; confirmation owner as `P`; package policy; user identity; global safety policy; release/rollback authority.
- Why no material first-party path remains: the first-party runtime faithfully enforces externally supplied purpose/constraints but does not expose or autonomously close an identity/ultimate-policy decision process. Ordinary configuration, final-write ownership and one-action approval do not meet the S5 parent-mode threshold.

## Recursion

The assessed recursion is one Waggle-managed AgentRun with its durable Project/Session context and first-party governance/runtime surfaces. PI Core is an embedded generic execution dependency, not a separate higher-recursion organization being credited. Product Providers and business backends are external operational services, and the product remains a parent/external organization for business authority. Future parent-child AgentRuns would create additional recursion/topology questions, but the frozen architecture explicitly treats that as target evolution rather than current executable closure.

## Variety and escalation

Waggle attenuates task variety through the autonomous model/tool S1 loop and attenuates execution risk through a precompiled per-run authority envelope, Tool Proxy, Workspace Guard, confirmation requirements, cancellation and lifecycle/recovery machinery. A proposed high-risk effect can escalate to a user/product confirmation and return to the same ToolCall. Model/tool failures, lease/watchdog conditions and terminal transitions are handled by runtime lifecycle paths. These mechanisms are recorded under S1/enforcement unless a distinct organizational function is independently established; escalation by itself is not promoted to S3, S3* or S5.

## Evidence gaps

- Structural/static review only; no live Waggle deployment or external model/Product Provider was executed during this assessment.
- `@earendil-works/pi-agent-core` implements the generic loop primitive; the assessment credits Waggle only for the reachable first-party operating organization it constructs around that primitive and does not import independent Pi higher-order functions.
- The public docs distinguish current executable baseline from target evolution. Parent-child orchestration, richer distributed scheduling and remote execution targets were deliberately excluded where `current-implementation.md` does not establish them.
- Product-integrated deployments can add domain-specific coordination, audit, adaptation and identity governance. Those downstream systems require separate system-in-focus assessments and do not change generic Waggle states.
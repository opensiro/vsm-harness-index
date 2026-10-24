---
harness_id: rust-norion
project_name: rust-norion
repository: https://github.com/yanghao1143/rust-norion
review_ref: 386363fac8db39a40bd5940b2016aecf26c095d1
reviewed_at: 2026-09-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-30
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C
autonomy_s3_star: —
autonomy_s4: C(P)
autonomy_s5: —
---

# rust-norion

## Review boundary

- System in focus: the first-party rust-norion inference/control harness at frozen revision `386363fac8db39a40bd5940b2016aecf26c095d1`, including the runnable `NoironEngine` inference loop and the shipped `norion-agent` coordination constructor surfaces where they are used as the repository's supported agent-workflow layer.
- Purpose and identity: run bounded model-backed inference while controlling routing, compute hierarchy, recursive execution, memory, reflection, process reward, drift, adaptation, and optional multi-window/agent coordination under explicit evidence and write gates.
- Relevant environment: user prompts and task profiles; model/runtime backend responses; hardware pressure; retrieved memory and prior experience; concurrent agent/window ownership claims; tool/runtime failures; validation results; reward/reflection evidence; operator-approved self-evolution evidence.
- Standard-distribution boundary: first-party root inference/control runtime, its `InferenceBackend`/runtime adapter contracts, shipped adaptive state and writer gates, and exported `crates/norion-agent` coordination framework are inside. Concrete external model weights/providers, caller-defined `EnginePort` implementations not shipped by this repository, independent Smart Steam windows outside this repository, and third-party services remain dependencies.
- Credited operating / distribution surfaces: `README.md`; `src/engine/inference.rs`; `src/engine/types.rs`; `src/engine/backend.rs`; `src/agent_team/*`; `src/router/*`; `src/hierarchy/*`; `src/adaptive_state/*`; `src/reflection/*`; `src/process_reward/*`; `src/writer_gate.rs`; `src/self_evolution.rs`; `crates/norion-agent/src/{collaboration,conflict,schedule,execute,ledger,step,ports}.rs`; corresponding shipped architecture documentation where it defines supported runtime/framework contracts.
- Adjacent first-party surfaces excluded from ownership: repository-development runbooks and contributor coordination; `docs/governance/*` where it describes project-development governance rather than runtime closure; benchmark/evaluation and smoke-test systems including `src/gemma_business/*`, test fakes and `#[cfg(test)]` implementations; CI/release machinery; clean-room/source-license audits; examples/tests that demonstrate a constructor path without themselves being the deployed actor.
- First-party operating / deployment modes considered: runnable local/model-service inference through `NoironEngine`; external/production runtime adapters behind first-party contracts; optional root agent-team planning when a valid route proof is supplied; exported `norion-agent` multi-window coordination composed with a caller-provided `EnginePort`; runtime adaptive feedback; explicitly authorized genome-evolution apply mode.
- Recursion level: one rust-norion harness instance is the system in focus. A model-backed inference turn is the primary S1 operation in the runnable root mode. In the exported multi-window framework mode, admitted window/task workers are S1 units and the first-party coordination crate supplies constructor-owned cross-unit regulation. The operator/user is a parent only for the separately evidenced S4 promotion mode; repository maintainers are not automatically treated as runtime parent authority.
- Reviewed revision: `386363fac8db39a40bd5940b2016aecf26c095d1`.
- Observation date: 2026-09-30.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

rust-norion is a Rust inference/control-plane prototype rather than a model kernel. Its root `NoironEngine` turns an inference request into a current operating plan covering memory retrieval, recursive scheduling, task-aware hierarchy, hardware allocation, routing budget, Toolsmith and optional agent-team context, then calls a model/runtime backend. The returned draft enters reflection, deterministic validation where applicable, drift checks, memory admission, process reward, adaptive router/hierarchy feedback and optional genome-evolution preview/apply logic.

The repository also ships `crates/norion-agent`, a runtime-agnostic coordination framework for multi-window work. Its own documentation is explicit that the crate does not itself run models, write files or persist memory: a service or main window supplies those side effects through data-only plans, reports, gates and an `EnginePort`. The crate nevertheless owns concrete coordination rules over caller-supplied operational units: isolated budgets, ownership-path review, duplicate/conflict detection, repair-first queues, scheduler handoffs, run-ledger closure and side-effect admission.

Persistent adaptation is split between automatically updated runtime state and more invasive genome mutation. Current inference evidence can deterministically alter router thresholds, hierarchy weights and memory strengths for future runs. Durable genome mutation is separately gated: a promotion preflight and user-approved task-skill evidence are required to create a valid `GenomeEvolutionAuthorization`, and the writer/apply path must succeed before the active genome changes.

Primary evidence:

- [`README.md`](https://github.com/yanghao1143/rust-norion/blob/386363fac8db39a40bd5940b2016aecf26c095d1/README.md)
- [`src/engine/inference.rs`](https://github.com/yanghao1143/rust-norion/blob/386363fac8db39a40bd5940b2016aecf26c095d1/src/engine/inference.rs)
- [`src/engine/types.rs`](https://github.com/yanghao1143/rust-norion/blob/386363fac8db39a40bd5940b2016aecf26c095d1/src/engine/types.rs)
- [`docs/architecture/norion-agent.md`](https://github.com/yanghao1143/rust-norion/blob/386363fac8db39a40bd5940b2016aecf26c095d1/docs/architecture/norion-agent.md)
- [`docs/architecture/norion-agent-workflow.md`](https://github.com/yanghao1143/rust-norion/blob/386363fac8db39a40bd5940b2016aecf26c095d1/docs/architecture/norion-agent-workflow.md)

## Operational model

In the runnable root mode, a request enters `NoironEngine`. The runtime retrieves relevant memories/experiences, derives recursive scheduling, hierarchy, hardware and routing choices, builds the generation context, and calls a model-backed `InferenceBackend`. The model produces the substantive draft; first-party reflection and validation can revise or reject it. The runtime then scores and records the result, updates adaptive routing/hierarchy and memory state when gates permit, and exposes the resulting answer plus control evidence.

In the exported multi-window mode, a caller declares active operational windows/tasks and supplies the execution adapter. First-party `norion-agent` plans isolated budgets and dependencies, reviews ownership and reported writes, detects conflicts or unhealthy persisted trends, inserts repair work ahead of business work, and keeps memory/file/adaptive/external side-effect admission closed until the relevant repair/closure evidence is clean.

## S1 — Operations

- State: A
- Function: perform the requested inference/transformation and produce a substantive model-backed answer or task result in the request's environment.
- Disturbance / variety regulated: changing prompts, task profiles, retrieved context, model/runtime responses, validation failures, tool/runtime conditions and task-specific content requirements.
- Decisive decision or feedback right: choose the substantive content/reasoning response to the current request and revise it in response to returned generation/validation context.
- Decision owner: the model-backed inference actor invoked through `InferenceBackend` in the supported root runtime.
- Supporting / enforcement mechanisms: `NoironEngine`; routing and hierarchy plans; recursive scheduler; hardware allocator; memory retrieval; generation context; reflection and deterministic validation; runtime adapter contracts; cancellation and drift gates.
- Closure path: request + retrieved/current control context → model-backed backend generates a draft → reflection/validation feedback is applied → revised answer returns to the caller and its outcome evidence feeds later runtime regulation.
- Boundary reachability: `NoironEngine::infer*` is a shipped root operating path and directly invokes an `InferenceBackend` through the first-party generation context. External weights/provider internals are dependencies, but no adjacent development agent is required to supply the task-specific inference decision.
- Why this is / is not agent-owned: removing the model-backed inference actor while retaining schedulers, routers, memory, validators and state machinery leaves a control shell without the substantive task-specific output decision. The material S1 discretion is therefore agent-owned.
- Evidence: [`README.md`](https://github.com/yanghao1143/rust-norion/blob/386363fac8db39a40bd5940b2016aecf26c095d1/README.md); [`src/engine/inference.rs`](https://github.com/yanghao1143/rust-norion/blob/386363fac8db39a40bd5940b2016aecf26c095d1/src/engine/inference.rs); [`src/engine/backend.rs`](https://github.com/yanghao1143/rust-norion/blob/386363fac8db39a40bd5940b2016aecf26c095d1/src/engine/backend.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the assessment does not claim that an external provider is part of rust-norion's first-party distribution; it credits the model actor reached through the shipped harness contract as the operational decision-maker.

## S2 — Coordination

- State: C
- Function: attenuate concrete interference among distinct operational windows/tasks before their writes, side effects or subsequent work are admitted.
- Distinct S1 units: caller-supplied active agent/window tasks executed through the exported `norion-agent` workflow and `EnginePort` boundary.
- Inter-S1 disturbance: two windows may report the same changed path or a window may mutate outside its declared ownership slice; duplicate/conflicting aggregation, depleted shared resources or unresolved conflict evidence can also make concurrent/continued work unsafe.
- Attenuating coordination relation: first-party ownership review blocks shared/out-of-bounds writes, conflict/aggregation/budget/schedule health gates close downstream admission, and repair-first queue composition inserts deterministic repair tasks ahead of preserved business tasks.
- Feedback into subsequent S1 behaviour: ownership/conflict/health results change the effective queue and dependencies seen by the scheduler; affected S1 business work is held until repair tasks complete, after which the preserved queue may resume.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: credit rests on explicit cross-window collision conditions—overlapping changed paths, out-of-bounds writes and unresolved conflict pressure—and on a mechanism designed to attenuate those disturbances before later S1 work/side effects continue. The task queue or message aggregation alone is not the witness.
- Disturbance / variety regulated: cross-window write collisions, ownership-boundary violations, unresolved result conflicts and related oscillation/repair pressure across operational units.
- Decisive decision or feedback right: decide whether the current multi-window handoff remains collision-safe and, when it is not, close ordinary promotion and force the appropriate repair queue/dependencies before resuming business work.
- Decision owner: deterministic first-party `norion-agent` coordination constructors/gates.
- Supporting / enforcement mechanisms: `AgentWindowOwnershipReviewer`; collaboration plan/ownership/preflight gates; `ConflictResolver` and conflict history; isolated `BudgetLedger`; recursive scheduler; `AgentTaskQueue::with_repair_first`; run-ledger/report side-effect gates.
- Closure path: window ownership/results and persisted coordination health → first-party review/gate decision → conflicting work is blocked and repair tasks become dependencies of ordinary work → scheduler executes/adopts repair-first ordering → subsequent S1 work resumes only behind repaired coordination state.
- Boundary reachability: the coordination path is exported as the supported `crates/norion-agent` framework contract. A caller must supply actual workers and an `EnginePort`, but it does not have to invent the S2 collision/repair policy: the first-party crate owns and returns those decisions for standard composition.
- Why this is / is not agent-owned: the decisive collision/admission response is deterministic first-party library policy, not a model-backed coordination judgment. The function is real and first-party but requires composition with caller-provided S1 execution, matching constructor-owned `C` rather than `A`.
- Evidence: [`docs/architecture/norion-agent-workflow.md`](https://github.com/yanghao1143/rust-norion/blob/386363fac8db39a40bd5940b2016aecf26c095d1/docs/architecture/norion-agent-workflow.md); [`docs/architecture/norion-agent.md`](https://github.com/yanghao1143/rust-norion/blob/386363fac8db39a40bd5940b2016aecf26c095d1/docs/architecture/norion-agent.md); [`crates/norion-agent/src/collaboration.rs`](https://github.com/yanghao1143/rust-norion/blob/386363fac8db39a40bd5940b2016aecf26c095d1/crates/norion-agent/src/collaboration.rs); [`crates/norion-agent/src/schedule.rs`](https://github.com/yanghao1143/rust-norion/blob/386363fac8db39a40bd5940b2016aecf26c095d1/crates/norion-agent/src/schedule.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the root `AgentTeamPlanner` by itself is not treated as proof that several independent model calls execute. S2 credit is bounded to the exported multi-window coordination mode where distinct caller-supplied S1 tasks exist and the first-party crate supplies the collision/repair relation.

## S3 — Inside-and-now control

- State: C
- Function: regulate the current inference system as a whole by allocating present compute/routing/hierarchy/recursion/memory commitments and intervening when current health makes an action unsafe.
- Whole-system current view: one `NoironEngine` inference cycle combines the current prompt/profile, retrieved memories and experiences, recursive-schedule pressure, hierarchy state, hardware pressure/headroom, routing budget, optional agent-team plan, generation/reflection outcome, drift state, memory-admission evidence and process reward.
- Current-control decision scope: choose current route/attention and compute budget; adapt hierarchy for the task; cap recursive parallelism; choose hardware execution plan; admit/hold memory and runtime-KV writes; retry invalid Rust output; cancel/abort unsafe runs; rollback current adaptive changes on drift; constrain optional agent-team planning under route/hardware state.
- Disturbance / variety regulated: current hardware/memory pressure, context length, resource limits, route uncertainty, validation failures, contradictions, drift, recursive fanout, backend cancellation/failure and competition among current control commitments.
- Decisive decision or feedback right: determine and revise the current whole-run allocation/admission/intervention plan across those shared resources and constraints.
- Decision owner: deterministic first-party `NoironEngine` control logic and its planners/gates.
- Supporting / enforcement mechanisms: task-aware hierarchy planner; router; hardware allocator; recursive scheduler; homeostatic setpoints; drift guard; reflection/validation; memory admission and writer gates; runtime cancellation.
- Closure path: current request + whole-cycle state → deterministic control plans/admission/intervention decisions → backend generation and side effects run under those constraints → generation/health/reward evidence returns into the same cycle → retry, rollback, hold or final current state changes subsequent operation.
- Boundary reachability: this whole-current-control path is wired directly inside the shipped root `NoironEngine::infer*` methods and does not borrow a development controller, test harness or external main-window manager.
- Why this is / is not agent-owned: removing model inference while keeping the control machinery still leaves materially the same budget, hierarchy, scheduling, admission and rollback rules; their current-control discretion is encoded in deterministic first-party constructors. S3 is therefore `C`, not `A`.
- Evidence: [`src/engine/inference.rs`](https://github.com/yanghao1143/rust-norion/blob/386363fac8db39a40bd5940b2016aecf26c095d1/src/engine/inference.rs); [`src/router/`](https://github.com/yanghao1143/rust-norion/tree/386363fac8db39a40bd5940b2016aecf26c095d1/src/router); [`src/hierarchy/`](https://github.com/yanghao1143/rust-norion/tree/386363fac8db39a40bd5940b2016aecf26c095d1/src/hierarchy); [`src/homeostasis.rs`](https://github.com/yanghao1143/rust-norion/blob/386363fac8db39a40bd5940b2016aecf26c095d1/src/homeostasis.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: scheduler/budget mechanisms are not credited merely for existing. Credit rests on the integrated whole-run decision path in `NoironEngine`; those mechanisms are recorded as components of constructor-owned current control.

## S3* — Complementary audit

- State: —
- Function: no material first-party complementary audit of the rust-norion operating harness was established at the assessed recursion.
- Disturbance / variety regulated: not established beyond routine production validation, subsystem consistency/provenance checks and adjacent development/evaluation audits.
- Decisive decision or feedback right: no sufficiently independent operational-audit judgment over the live harness whole was found.
- Decision owner: not established.
- Supporting / enforcement mechanisms: runtime reflection, Rust answer validation, memory/lineage audits, trace checks and Gemma business smoke/runtime audit surfaces exist, but they either sit in the ordinary production path, inspect one subsystem, or belong to adjacent evaluation/development systems.
- Closure path: no shipped complementary channel was found that obtains materially different access to live operational reality and returns its findings into root S3 current control.
- Why this is / is not agent-owned: not applicable because the S3* function itself is not established at this boundary.
- Evidence: [`src/engine/inference.rs`](https://github.com/yanghao1143/rust-norion/blob/386363fac8db39a40bd5940b2016aecf26c095d1/src/engine/inference.rs); [`crates/norion-memory/src/adapters.rs`](https://github.com/yanghao1143/rust-norion/blob/386363fac8db39a40bd5940b2016aecf26c095d1/crates/norion-memory/src/adapters.rs); [`src/reasoning_genome/audit.rs`](https://github.com/yanghao1143/rust-norion/blob/386363fac8db39a40bd5940b2016aecf26c095d1/src/reasoning_genome/audit.rs); [`src/gemma_business/smoke_report/runtime_audit.rs`](https://github.com/yanghao1143/rust-norion/blob/386363fac8db39a40bd5940b2016aecf26c095d1/src/gemma_business/smoke_report/runtime_audit.rs).
- Basis: explicit + structural negative review.
- Confidence: medium-high.
- Caveats: this does not say rust-norion lacks validation or observability; it distinguishes those mechanisms from complementary VSM S3* access at the declared runtime recursion.

### Absence scope

- Surfaces inspected: root inference/reflection/validation/drift/trace paths; `norion-agent` review/eval/ledger surfaces; `norion-memory` adapter/governance audit surfaces; reasoning-genome lineage audit; CLI experience cleanup audit; Gemma business smoke/cycle runtime-audit surfaces; clean-room/source-governance audits; architecture/governance documentation and representative tests.
- Plausible first-party paths checked: reflection or validation as a challenger to ordinary reporting; raw runtime trace reconciliation; memory/provenance auditing; model-service/Gemma smoke runtime audit; replay/eval paths; multi-window reviewer/ledger paths; clean-room and lineage audits.
- Why no material first-party path remains: root reflection/validation is part of ordinary output production, memory/lineage checks audit narrower stored-state/provenance claims, multi-window review gates are ordinary coordination/control, and Gemma smoke/clean-room/eval surfaces are adjacent development/evaluation systems. None supplies a sufficiently independent alternate observation path over the operating harness whole with findings closed back into root S3.

## S4 — Outside-and-then intelligence

- State: C(P)
- Function: convert observed request/runtime outcome evidence into future changes in routing, hierarchy, memory and—when separately authorized—persisted reasoning-genome capability.
- External distinction: current user/task demand, retrieved prior experience, model/runtime output quality, contradictions, reflection issues, runtime-KV yield, hardware/runtime observations and process-reward evidence distinguish how the environment and current execution are behaving.
- Future / prospective distinction: those observations are evaluated as evidence for future profile-specific routing/hierarchy settings, memory strengths and candidate genome changes rather than only for completing the current answer.
- Adaptation option generated: automatically adjust router thresholds and hierarchy weights, reinforce/penalize memories, persist admitted experience/memory, or preview bounded genome mutation/rollback plans; in the parent mode, promote an eligible genome change after explicit authorization.
- Path back into current capability / S3: adaptive router/hierarchy/memory state persists and is read at the start of later inference cycles; an applied genome becomes the later `active_genome`, whose expression changes generation context, routing bias, memory policy and other current-control inputs.
- Disturbance / variety regulated: recurrent performance differences, contradiction/reflection failures, inefficient routing/compute allocation, stale or harmful memory, new task evidence and changing evidence about which reasoning genes should remain active.
- Decisive decision or feedback right: in the base mode, deterministic runtime rules decide bounded feedback mutations/rollback from observed metrics and reward; in the parent mode, user/operator approval is required for the durable genome adaptation to cross the promotion/write boundary.
- Decision owner: base mode — deterministic first-party runtime (`C`); parent mode — user/operator approval over a separately validated adaptation (`P`).
- Supporting / enforcement mechanisms: process reward; reflection; drift guard; router/hierarchy observation; `EvolutionLedger`; memory feedback; genome preview/controller; `SelfEvolutionPromotionPreflightReport`; `GenomeEvolutionAuthorization`; unified writer gate; lineage/apply receipt.
- Closure path: runtime/environment evidence → reflection/reward/adaptation logic → bounded state update or mutation candidate → state is persisted/admitted → later inference reloads and uses the changed route/hierarchy/memory/genome state. For durable genome evolution, the candidate additionally passes parent authorization before apply.
- Boundary reachability: automatic router/hierarchy/memory feedback is directly wired into `NoironEngine::infer*`. The parent genome mode is also a first-party runtime contract: `InferenceRequest` accepts `GenomeEvolutionAuthorization`, its constructor requires a ready promotion preflight plus approved task-skill evidence, and the inference apply path persists the resulting active genome when all gates pass.
- Why this is / is not agent-owned: the base adaptation choices are deterministic functions of metrics/reward/gates and remain materially available without a separate adapting agent, so the base is `C`. The durable genome branch has a distinct parent-owned adaptation decision because `GenomeEvolutionAuthorization::is_valid` requires user-approved evidence before the write/apply path can open.
- Evidence: [`src/engine/inference.rs`](https://github.com/yanghao1143/rust-norion/blob/386363fac8db39a40bd5940b2016aecf26c095d1/src/engine/inference.rs); [`src/engine/types.rs`](https://github.com/yanghao1143/rust-norion/blob/386363fac8db39a40bd5940b2016aecf26c095d1/src/engine/types.rs); [`src/adaptive_state/`](https://github.com/yanghao1143/rust-norion/tree/386363fac8db39a40bd5940b2016aecf26c095d1/src/adaptive_state); [`src/self_evolution.rs`](https://github.com/yanghao1143/rust-norion/blob/386363fac8db39a40bd5940b2016aecf26c095d1/src/self_evolution.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: generic persistence or self-improvement naming is not the basis. Credit requires the observed-evidence → adaptation → later-runtime-use path. Parent credit is limited to the explicit adaptation-promotion path and does not imply parent ownership of ordinary inference.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | Deterministic first-party runtime feedback logic | Completed inference produces metrics/reflection/reward/runtime evidence | Router/hierarchy/memory state is mutated or rolled back and reused by later inference | `src/engine/inference.rs`, `src/adaptive_state/*` |
| Parent (`P`) | User/operator approving the adaptation | Eligible genome-evolution promotion preflight plus user-approved task-skill evidence | Valid authorization opens writer/apply gates; applied genome becomes later `active_genome` | `src/engine/types.rs`, `src/self_evolution.rs`, `src/engine/inference.rs` |

## S5 — Policy and identity

- State: —
- Function: no closed first-party runtime path was established for changing or reaffirming rust-norion's identity or ultimate policy at the assessed harness recursion.
- Disturbance / variety regulated: not established beyond task configuration, safety/write constraints, adaptation approval and preview-only project self-evolution-goal governance.
- Decisive decision or feedback right: no runtime identity/ultimate-policy decision right with a returned governance loop was found.
- Decision owner: not established.
- Supporting / enforcement mechanisms: task profiles, tenant scopes, writer gates, policy structs, operator approvals, self-evolution promotion gates and the evolution/self-goal queue bound what may happen, but those mechanisms regulate operations/adaptation rather than close ultimate identity policy.
- Closure path: no first-party identity/policy issue → legitimate ultimate authority → authoritative decision → returned operation path was established at this frozen revision.
- Why this is / is not agent-owned: neither an autonomous agent/system S5 owner nor a complete first-party parent S5 mode was established.
- Evidence: [`docs/governance/evolution-goal-queue.md`](https://github.com/yanghao1143/rust-norion/blob/386363fac8db39a40bd5940b2016aecf26c095d1/docs/governance/evolution-goal-queue.md); [`src/evolution_goal.rs`](https://github.com/yanghao1143/rust-norion/blob/386363fac8db39a40bd5940b2016aecf26c095d1/src/evolution_goal.rs); [`src/self_goal_proposal.rs`](https://github.com/yanghao1143/rust-norion/blob/386363fac8db39a40bd5940b2016aecf26c095d1/src/self_goal_proposal.rs); [`src/writer_gate.rs`](https://github.com/yanghao1143/rust-norion/blob/386363fac8db39a40bd5940b2016aecf26c095d1/src/writer_gate.rs); [`src/engine/types.rs`](https://github.com/yanghao1143/rust-norion/blob/386363fac8db39a40bd5940b2016aecf26c095d1/src/engine/types.rs).
- Basis: explicit + structural negative review.
- Confidence: high.
- Caveats: operator authority over an S4 genome promotion is intentionally not promoted to S5. An adaptation-specific approval is not by itself an identity/ultimate-policy decision.

### Absence scope

- Surfaces inspected: README/architecture; root request/profile/router/hierarchy/runtime policy surfaces; writer gates; self-evolution promotion/rollback paths; genome authorization; `evolution_goal` and `self_goal_proposal`; evolution-goal governance documentation; CLI/service admission surfaces; tenant scoping; repository governance/development material as adjacent evidence.
- Plausible first-party paths checked: system/task profile as durable identity; writer policies as ultimate policy; operator approval as parent S5; autonomous self-goal proposal as internal S5; evolution-goal queue as a project-policy authority; genome evolution as identity change.
- Why no material first-party path remains: task/profile/writer policies are lower-level constraints, the evidenced operator approval closes an adaptation-specific S4 promotion, and the frozen self-goal/evolution-goal mechanism is explicitly preview/read-only and requires later apply/approval workflows. It therefore does not close a runtime ultimate-policy or identity decision back into the assessed harness.

## Distributed OSS parent arrangement

Repository maintainers and contributors govern development of rust-norion, but that repository-development organization is not silently imported into the runtime recursion. The only positive parent notation in this assessment is the explicit user/operator adaptation authorization exposed by the first-party runtime contract for S4. Public maintainership alone is not evidence of runtime S5 or a parent S3 mode.

## Self-hosted and non-human modes

The root runtime can operate locally with first-party control logic and model/runtime adapters. Ordinary S1/S3 and base S4 operation does not require continuous human supervision. More invasive genome evolution exposes a parent-authorized mode, while the frozen self-goal/evolution-goal surfaces remain preview/read-only rather than an autonomous ultimate-policy authority.

## Recursion

At the root assessed recursion, one rust-norion inference harness is the system. Model-backed inference supplies the primary operational S1. The integrated deterministic engine supplies current S3 control over one run and base S4 adaptive feedback across runs. The exported `norion-agent` framework supplies a separate standard first-party constructor mode in which multiple caller-provided operational windows can be coordinated by S2-specific ownership/conflict/repair rules. Those caller windows are not mistaken for automatically executed root model actors.

## Variety and escalation

rust-norion attenuates variety with routing budgets, task-aware hierarchy, hardware and recursion caps, homeostatic gates, memory admission, reflection/validation, drift rollback, write gates, isolated window budgets and repair-first coordination. It amplifies regulatory capacity through retrieved memory/experience, recursive execution, model-backed inference, optional agent-team context and accumulated adaptive state. Current operational exceptions are held/retried/rolled back by deterministic control; durable genome changes require the stronger adaptation-promotion evidence and parent authorization path described under S4.

## Evidence gaps

- No first-party production `EnginePort` implementation was found for `crates/norion-agent`; S2 is therefore bounded to the shipped coordination-constructor mode and published as `C`, not as autonomous multi-agent execution.
- The root `AgentTeamPlanner` creates deterministic team plans/messages and is not used as independent proof that several model-backed S1 agents actually run.
- S3* remains negative because available audit-named surfaces do not provide complementary whole-harness operational access at this recursion.
- S5 remains negative because the frozen self-goal/evolution-goal machinery is explicitly preview/read-only; adaptation authorization is classified under S4 rather than treated as generic identity authority.

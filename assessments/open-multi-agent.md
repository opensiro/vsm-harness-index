---
harness_id: open-multi-agent
project_name: OMA / Open Multi-Agent
repository: https://github.com/open-multi-agent/open-multi-agent
review_ref: 4107fb144653c3240c569f345cf06b028dd7747a
reviewed_at: 2026-09-19
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
assessment_changed_at: 2026-09-19
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: C
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# OMA / Open Multi-Agent

## Review boundary

- System in focus: the first-party `@open-multi-agent/core` runtime at pinned revision `4107fb144653c3240c569f345cf06b028dd7747a`, including built-in agent execution, `runAgent` / `runTasks` / `runTeam` / `runFromPlan` / `restore`, task queue and scheduler, AgentPool, shared-memory handoff, checkpoints, run-store leases, durable approvals, adaptive-recovery contracts, consensus verification, execution receipts, journal and runtime governance mechanisms.
- Purpose and identity: self-hosted execution of one or more agent actors with explicit or dynamically planned task graphs, governed side effects, durable recovery and inspectable/verifiable run records.
- Relevant environment: caller goals and explicit DAGs, model/provider responses, tools and external side effects, task dependencies, agent availability/capabilities/current load, budget/cost ceilings, process crashes, operator approval decisions, external process/ACP workers, and application policy/configuration.
- Standard-distribution boundary: the shipped core runtime and its documented first-party operating modes. External model providers, MCP servers, process/ACP agent implementations, application-specific services, custom storage backends and reviewer products remain environment/substrate even when OMA supplies the integration seam.
- Credited operating / distribution surfaces: `packages/core` runtime paths for agent execution, task queue/scheduler/AgentPool, shared memory, checkpoint/restore, run-store fencing, durable approval ledger/helpers, consensus verification, adaptive-recovery outcome barrier and `Replanner` contract, execution receipts and declared-governance checks, and documented supported execution modes.
- Adjacent first-party surfaces excluded from ownership: `@open-multi-agent/core/eval` offline/online evaluation when used as post-run/CI quality measurement; repository CI, supply-chain audit and release workflows; benchmarks, scaffolder demos, examples, website assets, contributor/release bots and maintainer governance. They may corroborate capabilities but do not close product-runtime VSM functions by repository co-location.
- First-party operating / deployment modes considered: single built-in LLM agents; explicit multi-agent DAGs; coordinator-generated teams; declared-governance teams; opt-in per-task/top-level consensus; checkpoint/restore; opt-in run-store ownership; opt-in adaptive recovery. External process/ACP backends are considered workers/substrate only to the extent OMA owns surrounding task scheduling/settlement.
- Recursion level: one logical OMA run/team as the system-in-focus. Task workers that directly transform assigned work are S1 units for multi-agent runs. Coordinator, scheduler, run ledger, consensus judges and recovery hooks are classified by function rather than by component name.
- Reviewed revision: `4107fb144653c3240c569f345cf06b028dd7747a`.
- Stable GitHub repository id: `1197656406`.
- Observation date: 2026-09-19.
- Generated Profile version: `0.2.3`.
- Generated Methodology version: `0.3.5`.
- Current Profile version: `0.2.3`.
- Current Methodology version: `0.3.5`.

## Repository architecture

OMA exposes three principal execution shapes: `runAgent()` for one operational agent, `runTasks()` for caller-declared DAG work, and `runTeam()` for a runtime-generated team plan. In `runTeam()`, a temporary coordinator performs one decomposition call before execution and one synthesis call after execution; it is explicitly not consulted mid-run. The resulting or caller-supplied task graph is handed to `TaskQueue` and the event-driven `Scheduler`. Ready tasks are assigned against the current DAG snapshot and dispatched through `AgentPool`; task completion immediately releases dependents, while failures/skips cascade only along affected branches.

Scheduling supports dependency-first, round-robin, least-busy, capability-match and composite policies. The load-aware strategies inspect current `in_progress` assignments across the roster, while dependency-aware strategies inspect downstream criticality. This is deterministic current-control machinery. More importantly for an autonomous-constructor claim, opt-in adaptive recovery exposes a first-party whole-run intervention seam after task outcomes: `TaskOutcome` includes the triggering task, result/verification outcome, current plan revision, the complete task list and remaining budgets; a configured `Replanner`/`onTaskOutcome` can propose a `PlanPatch` that adds replacement work, retargets pending work or supersedes pending branches. OMA validates and atomically applies accepted patches before newly-ready work is published. OMA does not ship the decisive autonomous replanner; external I/O/model use inside a custom replanner remains application-owned.

Consensus is a distinct verification subsystem. `runConsensus()` and the per-task `verify` hook run one proposer/result against a separate roster of judge agents. Judges receive the original question plus proposed answer and return structured accept/critique verdicts. Quorum can accept early; dissent can reject or, by default, return to the proposer for another revision round. In the per-task hook, an accepted revised answer replaces the task output for downstream queue/memory/results; verdict and dissent are also recorded. This is separate from post-run evaluation: the evaluation subpath explicitly observes completed results and never changes a business result.

Durability and human-control mechanisms surround these paths. Checkpoints resume completed/committed work without blindly re-executing it; an optional authoritative run store uses leases and fencing tokens to prevent two workers from advancing the same logical run. Plan/round/dispatch/tool gates can suspend at a durable approval boundary and later resume exact reviewed content after an external reviewer records a first-wins decision. OMA deliberately supplies no reviewer UI, transport, authentication or approval queue; integrators provide those parent surfaces. Journals, trace stores, execution receipts and offline verification make run structure/content lineage inspectable, but generic records alone are not treated as S3*; the positive S3* mapping below relies on the independent judge-and-revision loop.

## Operational model

A worker agent receives its task plus scoped dependency results/context, invokes its configured model and allowed tools, and iterates through model/tool observations until it settles a result. Independent DAG branches may execute concurrently. The scheduler determines which ready work runs where under eligibility, current load, dependency criticality, capacity, budget and approval constraints; deterministic dispatch machinery enforces these decisions.

For ordinary `runTeam()`, the LLM coordinator stops owning control once the initial DAG exists. Mid-run plan change happens only through the opt-in repairable-recovery boundary. At each task outcome, a configured replanner can see whole-run current state and propose changes to not-yet-started commitments. OMA validates state/agent/dependency/limit constraints, optionally passes the proposal through an application gate, applies it atomically and only then releases original dependents. Because OMA supplies the S3-specific decision/feedback path but not an autonomous replanner actor, that path is classified as constructor ownership rather than autonomous S3.

Consensus verification is available as an operational mode rather than a repository-development evaluator. Separate judge agents challenge a proposed answer/result using the original question as reference; their dissent can feed directly into another proposer round, and an accepted revision changes the task result visible to downstream work. That supplies a complementary autonomous audit loop within the runtime boundary.

## S1 — Operations

- State: A
- Function: autonomously execute assigned goals/tasks against model/tool environments and produce operational outcomes for the caller/run.
- Disturbance / variety regulated: heterogeneous prompts and task requirements, model responses, tool/API results, dependency payloads, context state, structured-output failures and external-backend results requiring context-sensitive next actions.
- Decisive decision or feedback right: choose the next model-mediated action within a task — respond, invoke an allowed tool, consume observations, continue reasoning/delegation where enabled, and settle the task result.
- Decision owner: the active OMA built-in LLM worker agent for standard built-in-agent modes; external process/ACP workers own their private inner loops and are not imported as first-party OMA decision actors.
- Supporting / enforcement mechanisms: Agent runner, model adapters, tool registry/grants, AgentPool, task queue, dependency/context injection, shared memory, budgets/timeouts, checkpoints and run-store fencing.
- Closure path: task/prompt + current context → agent model selects action/tool → runtime executes/returns observation → observation re-enters agent context → agent selects further action or final result → task/run settlement and dependent release.
- Boundary reachability: `runAgent`, `runTasks` and `runTeam` with built-in agents are first-party documented `@open-multi-agent/core` operating modes, not examples or CI-only paths.
- Why this is / is not agent-owned: removing the model-driven worker while leaving the scheduler, queue, stores, approval machinery and tool executor leaves no actor that makes the contextual task-level operational choices. Runtime machinery constrains and persists those decisions but does not substitute for them.
- Evidence: [`packages/core/README.md`](https://github.com/open-multi-agent/open-multi-agent/blob/4107fb144653c3240c569f345cf06b028dd7747a/packages/core/README.md), [`README.md`](https://github.com/open-multi-agent/open-multi-agent/blob/4107fb144653c3240c569f345cf06b028dd7747a/README.md), [`task-scheduling.md`](https://github.com/open-multi-agent/open-multi-agent/blob/4107fb144653c3240c569f345cf06b028dd7747a/docs/task-scheduling.md).
- Basis: structural
- Confidence: high
- Caveats: external process/ACP backends are supported substrate but their private operational loops are not credited as OMA-owned S1 autonomy; the positive state is already established by built-in agent execution.

## S2 — Coordination

- State: —
- Function: no material first-party S2-specific coordination loop was established for a concrete interference/oscillation among distinct OMA S1 worker units at the declared run/team recursion.
- Disturbance / variety regulated: candidate disturbances inspected included parallel ready tasks, competition for AgentPool capacity, duplicate processes advancing one logical run, dependency ordering and shared-memory writes.
- Decisive decision or feedback right: no qualifying S2-specific autonomous coordination discretion is supplied. Scheduler assignment/load balancing is whole-run resource/commitment control; run-store fencing prevents duplicate ownership of the same run; dependency edges sequence work; namespaced shared memory avoids key collisions.
- Decision owner: none established for S2 in the standard distribution.
- Supporting / enforcement mechanisms: AgentPool semaphore, task dependencies, event-driven ready set, least-busy/composite scheduling, namespaced shared memory, run-store lease/fencing and deterministic task-status propagation.
- Closure path: no first-party S2-specific feedback loop was found that observes an interaction disturbance among independent S1 workers and changes their subsequent local behaviour to damp it.
- Why this is / is not agent-owned: multiple agents and parallel branches exist, but task assignment, dependency sequencing and capacity limits are not S2 merely because they coordinate execution. The reviewed mechanisms map more directly to S3 resource/current-control or duplicate-execution safety and do not expose an S2-specific autonomous decision path.
- Evidence: [`task-scheduling.md`](https://github.com/open-multi-agent/open-multi-agent/blob/4107fb144653c3240c569f345cf06b028dd7747a/docs/task-scheduling.md), [`scheduler.ts`](https://github.com/open-multi-agent/open-multi-agent/blob/4107fb144653c3240c569f345cf06b028dd7747a/packages/core/src/orchestrator/scheduler.ts), [`run-store.md`](https://github.com/open-multi-agent/open-multi-agent/blob/4107fb144653c3240c569f345cf06b028dd7747a/docs/run-store.md), [`shared-memory.md`](https://github.com/open-multi-agent/open-multi-agent/blob/4107fb144653c3240c569f345cf06b028dd7747a/docs/shared-memory.md).
- Basis: structural
- Confidence: high
- Caveats: an application can build explicit cross-agent negotiation/conflict handling on OMA primitives; generic framework expressiveness does not meet the Methodology `C` threshold.

### Absence scope

- Surfaces inspected: scheduler/TaskQueue/AgentPool behavior, dependency handoff, shared memory, run-store leases/fencing, delegation/team execution, adaptive recovery and approval gates.
- Plausible first-party paths checked: load balancing, pool-capacity enforcement, duplicate-worker fencing, dependency ordering, cross-agent memory and task-result handoff.
- Why no material first-party path remains: each inspected path either allocates/controls current work on behalf of the run, prevents duplicate ownership of one logical execution, or transports/sequences state. No path is tied to a specific inter-S1 interference witness plus an S2-specific adjustment fed back into multiple workers' subsequent local operation.

## S3 — Inside-and-now control

- State: C
- Function: regulate current whole-run commitments and interventions after operational outcomes reveal that the pending task graph should change.
- Disturbance / variety regulated: task failure, consensus rejection, successful outcomes that invalidate/reshape downstream work, assignee infeasibility and remaining budget/commitment constraints while other pending/blocked work still exists.
- Decisive decision or feedback right: choose whether to keep the current pending graph or propose a `PlanPatch` that adds replacement tasks, retargets pending tasks or supersedes pending branches in response to a current task outcome.
- Decision owner: OMA does not supply the autonomous decisive replanner. The developer/application supplies a `Replanner` or `onTaskOutcome` actor; that actor may itself call an LLM/service, but such autonomous composition remains application-owned. OMA owns validation, atomic application and execution closure after a proposal exists.
- Supporting / enforcement mechanisms: `TaskOutcome` snapshot of complete current task state and remaining budgets, deterministic Scheduler and AgentSelector, recovery limits, DAG validation, optional `onPlanPatch` gate, checkpoint persistence and event-driven publication of newly-ready work.
- Closure path: task settles/reaches verification outcome → OMA constructs whole-run `TaskOutcome` → composed replanner proposes patch → OMA validates/gates and atomically applies accepted current-control changes → new/retargeted pending work enters the same scheduler and changes subsequent execution.
- Whole-system current view: `TaskOutcome.tasks` exposes the full current task list together with current plan revision, triggering task/result/verification and remaining budget dimensions; scheduler decisions also inspect current DAG/load state.
- Current-control decision scope: pending commitments may be appended, retargeted to another eligible agent, or superseded, thereby changing who will perform current work and which remaining commitments still count toward the run.
- Boundary reachability: repairable recovery, `Replanner`, `onTaskOutcome`, `PlanPatch` validation and atomic application are documented first-party `@open-multi-agent/core` runtime surfaces reachable in `runTasks`/team execution; the missing element is the developer-composed decisive actor, which is why the state is `C`, not `A`.
- Why this is / is not agent-owned: deterministic scheduling already enforces current assignment/criticality/load policy, but no shipped autonomous actor owns the discretionary replan judgment. The first-party recovery seam is S3-specific and operationally closes a composed decision back into current execution, satisfying the narrow constructor threshold without pretending the scheduler itself is an autonomous S3 owner.
- Evidence: [`adaptive-recovery.md`](https://github.com/open-multi-agent/open-multi-agent/blob/4107fb144653c3240c569f345cf06b028dd7747a/docs/adaptive-recovery.md), [`recovery.ts`](https://github.com/open-multi-agent/open-multi-agent/blob/4107fb144653c3240c569f345cf06b028dd7747a/packages/core/src/orchestrator/recovery.ts), [`task-scheduling.md`](https://github.com/open-multi-agent/open-multi-agent/blob/4107fb144653c3240c569f345cf06b028dd7747a/docs/task-scheduling.md), [`scheduler.ts`](https://github.com/open-multi-agent/open-multi-agent/blob/4107fb144653c3240c569f345cf06b028dd7747a/packages/core/src/orchestrator/scheduler.ts).
- Basis: explicit
- Confidence: high
- Caveats: the ordinary one-shot coordinator is not this S3 owner; it is explicitly absent mid-run. Durable plan/dispatch approval can constrain current work but OMA deliberately leaves reviewer product/transport/authorization to the integrator, so no separate parent-governed S3 mode is published here.

## S3* — Complementary audit

- State: A
- Function: independently challenge a proposed operational result and feed an audit judgment back into the result/control path before downstream use.
- Disturbance / variety regulated: plausible but incorrect/incomplete task answers whose ordinary worker completion path would otherwise become accepted downstream state without an independent challenge.
- Decisive decision or feedback right: independent judge agents decide accept/dissent against the original question and proposed answer; quorum and configured dissent policy determine whether the result is accepted, rejected or returned to the proposer for revision.
- Decision owner: the configured OMA judge-agent roster owns the audit judgments; deterministic quorum parsing/aggregation and runtime gating transport those judgments. On `onDissent: 'revise'`, the proposer remains the operational actor producing the corrected candidate, while judges retain the complementary audit right.
- Supporting / enforcement mechanisms: `runConsensus`, per-task `verify`, separate judge invocations, structured `{accept, critique}` verdicts, quorum/max-round controls, dissent persistence, token/cost accounting, shared-memory verdict records and task-output replacement after an accepted revision.
- Closure path: worker/proposer produces candidate → separate judges receive original question + candidate and issue verdicts/critiques → quorum/dissent policy resolves audit → dissent can be fed back to proposer for another round → an accepted revised answer supersedes task output and is propagated into queue/shared memory/downstream results.
- Claim being audited: that the proposer/worker's candidate adequately answers the original task/question and should be accepted as the task result.
- Ordinary reporting path: the worker/proposer's own final answer/result through the ordinary task completion path.
- Complementary access path: distinct judge-agent invocations independently evaluate the candidate against the original question under refute or differentiated-lens prompts; they are not the worker's ordinary completion check and can use separately configured models/agents.
- Independence boundary: judge agents are a separately configured verifier roster, invoked after/around the proposer result with their own model calls and structured verdict contract; they receive the candidate rather than inheriting the proposer's hidden reasoning state. Different judges can use different models and lens framings. The classification does not rely on generic traces, governance receipts or the post-run evaluation subsystem.
- Who acts on findings: the first-party consensus loop aggregates judge decisions; under the default `revise` policy it returns dissent to the proposer, and per-task verification replaces downstream task state only when a revised candidate is accepted.
- Boundary reachability: `runConsensus()` is a documented top-level core runtime mode and `verify` is a documented per-task hook in `runTasks`/`runTeam`; both are shipped first-party runtime paths rather than CI/eval-only machinery.
- Why this is / is not agent-owned: removing the judge agents while leaving quorum code, traces and result plumbing removes the substantive independent audit judgments. Deterministic parsing and quorum enforcement cannot recreate critiques or accept/dissent decisions, so the decisive S3* feedback is agent-owned.
- Evidence: [`consensus.md`](https://github.com/open-multi-agent/open-multi-agent/blob/4107fb144653c3240c569f345cf06b028dd7747a/docs/consensus.md), [`coordinator.md`](https://github.com/open-multi-agent/open-multi-agent/blob/4107fb144653c3240c569f345cf06b028dd7747a/docs/coordinator.md), [`packages/core/README.md`](https://github.com/open-multi-agent/open-multi-agent/blob/4107fb144653c3240c569f345cf06b028dd7747a/packages/core/README.md).
- Basis: explicit
- Confidence: high
- Caveats: governance-floor receipts and journal verification are useful audit mechanisms but are not the reason for `A`; post-run evaluation explicitly does not alter the business result. The positive mapping is the independent judge loop with corrective return.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party runtime path was established that senses external/future-relevant change, develops adaptation options and returns a strategic capability change into present OMA operation.
- Disturbance / variety regulated: candidate S4 inputs inspected included provider/tool failures, task outcomes, evaluation regressions/trends, routing profiles, model/provider choices and changing external requirements.
- Decisive decision or feedback right: no runtime S4 adaptation judgment is supplied. Adaptive recovery changes the current unexecuted graph in response to current task outcomes (S3-constructor scope), while the evaluation subsystem measures completed runs without changing their business result.
- Decision owner: none established for S4 in the assessed runtime boundary.
- Supporting / enforcement mechanisms: offline/online evaluation reports and gates, model/execution routing, adaptive recovery, configuration, callbacks, provider fallback and application-owned policy code.
- Closure path: no supported first-party outside/prospective sensing → option-generation → adaptation-decision → changed present capability loop was found inside the product-runtime boundary.
- Why this is / is not agent-owned: evaluation can expose versions, regressions and trends, but its documented contract is observe-only relative to business runs; using its reports to change prompts/models/topology in CI or operator practice is an adjacent application/development loop unless separately wired by the integrator.
- Evidence: [`evaluation.md`](https://github.com/open-multi-agent/open-multi-agent/blob/4107fb144653c3240c569f345cf06b028dd7747a/docs/evaluation.md), [`adaptive-recovery.md`](https://github.com/open-multi-agent/open-multi-agent/blob/4107fb144653c3240c569f345cf06b028dd7747a/docs/adaptive-recovery.md), [`packages/core/README.md`](https://github.com/open-multi-agent/open-multi-agent/blob/4107fb144653c3240c569f345cf06b028dd7747a/packages/core/README.md).
- Basis: explicit
- Confidence: high
- Caveats: a surrounding application or CI system can close an S4 loop using OMA evaluation data; repository co-location or generic callback capability does not import that external adaptation owner into the assessed runtime.

### Absence scope

- Surfaces inspected: evaluation/offline gates/online sampling, adaptive recovery, model/execution routing, provider fallback, configuration hooks, shared memory and runtime governance paths.
- Plausible first-party paths checked: regression/trend evaluation, hybrid task profiling, task-outcome replanning, provider switching and configuration-driven capability changes.
- Why no material first-party path remains: evaluation is explicitly non-intervening, task recovery is current-run control rather than prospective adaptation, and configuration/routing primitives require external developer/application decisions. No first-party S4-specific adaptation closure returns prospective environmental intelligence into present capability.

## S5 — Policy and identity

- State: —
- Function: no first-party runtime identity/ultimate-policy escalation-decision-return loop was established at the OMA run/team recursion.
- Disturbance / variety regulated: candidate policy matters included declared governance roles, consequential-tool rules, egress policy, approval decisions, role/tool boundaries, budget ceilings and explicit topology overrides.
- Decisive decision or feedback right: no autonomous or operationally closed first-party parent authority resolves identity/ultimate-policy disputes for the system. Applications declare governance intent, tool grants, egress/budget policy and reviewer integration before/around execution.
- Decision owner: application/developer/organization outside the assessed runtime owns ultimate policy; OMA deterministically validates/enforces selected rules and records deviations.
- Supporting / enforcement mechanisms: `governanceIntent`/required roles/order, execution receipts and `governanceConclusion`, consequential-tool classification/confirmation, egress policy, tool allow/deny lists, budgets, durable approval ledger, run-store cancellation and configuration.
- Closure path: configured constraints and approval decisions can change/stop subsequent execution, but no first-party standard path carries an identity/ultimate-policy issue to a legitimate ultimate authority and returns that authority's decision as S5 closure.
- Why this is / is not agent-owned: governance receipts prove that declared roles/order executed; they do not decide what the organization's identity or ultimate policy should be. Durable approvals bind exact reviewed content but OMA deliberately provides no reviewer product, routing, RBAC or escalation layer. These are strong enforcement/governance primitives without an S5 decision owner.
- Evidence: [`tool-configuration.md`](https://github.com/open-multi-agent/open-multi-agent/blob/4107fb144653c3240c569f345cf06b028dd7747a/docs/tool-configuration.md), [`durable-approvals.md`](https://github.com/open-multi-agent/open-multi-agent/blob/4107fb144653c3240c569f345cf06b028dd7747a/docs/durable-approvals.md), [`observability.md`](https://github.com/open-multi-agent/open-multi-agent/blob/4107fb144653c3240c569f345cf06b028dd7747a/docs/observability.md).
- Basis: explicit
- Confidence: high
- Caveats: an organization can build a legitimate parent-policy layer on top of the durable approval/governance primitives; Methodology 0.3.5 does not publish S5 merely because a human can approve an operational action or because policy text is enforceable.

### Absence scope

- Surfaces inspected: declared governance roles and execution receipts, consequential-tool policy, durable approvals, egress policy, budgets, tool grants, run cancellation/resume and repository governance/CI surfaces.
- Plausible first-party paths checked: required governance floor, plan/dispatch/tool approval, application mode override, egress tightening and operator run-ledger commands.
- Why no material first-party path remains: these surfaces enforce or expose application-selected constraints and operational approvals. OMA supplies neither an identity-level dispute/escalation path nor an ultimate-policy decision owner with first-party return-to-operation closure.

## Recursion, variety, and escalation

OMA supports multiple operational workers and nested/delegated execution, but worker processes and external ACP/process agents are not automatically recursive viable systems. The declared run/team recursion is sufficient for this assessment: worker agents absorb local task variety, deterministic scheduling/limits attenuate current resource variety, S3 constructor surfaces expose controlled reconfiguration of pending commitments, and consensus supplies complementary challenge to selected outputs.

Durable approval requests, run-store errors, budget stops, consensus dissent and recovery outcomes are useful escalation/algedonic signals. Their existence is kept separate from S5: operational exception handling and human approval are not identity governance merely because they can stop execution.

## Final vector

`A — C A — —`

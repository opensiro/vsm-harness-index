---
harness_id: mini-dsh
project_name: mini-DSH
repository: https://github.com/BeforeLanding/mini-DSH
review_ref: 0bff45e3463c38647bc0fb766e1687c31a07b1c9
reviewed_at: 2026-11-18
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# mini-DSH

## Review boundary

- System in focus: the shipped local TypeScript/Cordis coding-agent CLI and its first-party optional orchestration mode, not the developer's organization or the hosted DeepSeek service.
- Purpose and identity: carry out repository coding tasks through model-driven tool selection, persistent sessions and optionally coordinated subtask workers.
- Relevant environment: local Git worktree, source files, task/user input, model-provider responses, tool execution results, budget/permission stops and, in orchestration mode, concurrent worker edits.
- Standard-distribution boundary: `src/index.ts`, `src/app/create-harness.ts`, `src/core/`, first-party CLI/plugins and selectable `src/orchestration/` module at the frozen revision.
- Credited operating / distribution surfaces: interactive coding agent loop, event-sourced session and tool authorization; explicitly invoked orchestrator with model planner, worker agents, disjoint write-set validation, dependency waves, integration and result feedback.
- Adjacent first-party surfaces excluded from ownership: benchmark/evaluation scripts, test harnesses, sample results, repository CI, development notes and recruiter documentation; generic user-authored plugins and external MCP servers; upstream DeepSeek model-provider policy decisions.
- First-party operating / deployment modes considered: interactive coding `mini-dsh`; offline demo using the same harness; explicitly invoked orchestration with model-produced plan or operator-provided plan. Optional read-only delegation and external MCP adapters are not treated as independently deciding higher-level functions.
- Recursion level: one local coding task/session; for coordination, the orchestration root and multiple worker sessions executing subtasks of one repository goal.
- Reviewed revision: `0bff45e3463c38647bc0fb766e1687c31a07b1c9`.
- Observation date: 2026-11-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The Cordis composition registers provider, model, tools, sandbox, session and agent-loop plugins. `AgentLoopRuntime.run` dispatches model turns, makes tool calls under a central approval/effect gate, appends session events and returns bounded stop or finish states. The event journal supports recovery without blindly replaying unknown tool side effects. A configured orchestration CLI invokes a distinct root: a model planner generates a constrained task plan and worker assignments, validated for dependencies and overlapping write sets; each worker uses an agent loop in an isolated Git worktree. An integrator cherry-picks accepted changes, reports integration collisions and may explicitly hand the resolution choice to a local human. Verification commands run on the merged tree, not as an independent audit agent. Budget/timeout enforcement and tool approval are real, but are supporting safeguards, not automatically VSM S3/S5 decisions. [Architecture](https://github.com/BeforeLanding/mini-DSH/blob/0bff45e3463c38647bc0fb766e1687c31a07b1c9/docs/ARCHITECTURE.md#L1-L55), [agent loop](https://github.com/BeforeLanding/mini-DSH/blob/0bff45e3463c38647bc0fb766e1687c31a07b1c9/src/core/agent-loop-runtime.ts#L63-L150), [orchestration root](https://github.com/BeforeLanding/mini-DSH/blob/0bff45e3463c38647bc0fb766e1687c31a07b1c9/src/orchestration/orchestrator.ts#L604-L669).

## Operational model

An agent model selects coding tool calls, interprets results and continues the task. The orchestration mode has distinct worker S1 cells with bounded worktree write sets; the model planner allocates their subtask boundaries and dependencies. The runtime enforces those bounds and reports concrete failures. The root supervisor is predominantly a composed deterministic coordinator plus operator-supplied policies, not a demonstrated autonomous current-control decision-maker over the whole worker portfolio. User approvals govern individual tool effects/conflict cases; they do not by themselves close organizational identity or prospective strategic adaptation.

## S1 — Operations

- State: A
- Function: execute a repository coding task by selecting model-generated actions and revising them after observed tool results.
- Disturbance / variety regulated: variable user coding requirements, source code and runtime/tool outcomes.
- Decisive decision or feedback right: model continuation/tool-call choice for the active task; worker agent chooses edits within assigned write-set in orchestration mode.
- Decision owner: active coding agent / selected model in the shipped first-party agent loop, with human approval required for protected effects.
- Supporting / enforcement mechanisms: Cordis plugins, model adapter, budget/accounting runtime, central tool authorization, append-only session store and worktree isolation.
- Closure path: tool result is added to session state, used to form the next model request, and the agent continues or finishes with recorded outcome.
- Boundary reachability: default interactive CLI creates the packaged agent loop; optional orchestrator creates the same first-party loop for each worker.
- Why this is / is not agent-owned: the agent chooses the task-level next operation; policy/budget checks constrain rather than author those choices.
- Evidence: [agent-run loop](https://github.com/BeforeLanding/mini-DSH/blob/0bff45e3463c38647bc0fb766e1687c31a07b1c9/src/core/agent-loop-runtime.ts#L63-L150), [tool execution and return](https://github.com/BeforeLanding/mini-DSH/blob/0bff45e3463c38647bc0fb766e1687c31a07b1c9/src/core/agent-loop-runtime.ts#L300-L389), [worker agent construction](https://github.com/BeforeLanding/mini-DSH/blob/0bff45e3463c38647bc0fb766e1687c31a07b1c9/src/orchestration/worker.ts#L118-L160).
- Basis: structural
- Confidence: high
- Caveats: no live provider execution was observed in this assessment; source wiring, source code and shipped demo are the bounded evidence.

## S2 — Coordination

- State: A
- Function: attenuate competing parallel worker changes by choosing and enforcing disjoint work sets / dependency waves for one parent coding goal.
- Disturbance / variety regulated: separate worker S1 cells editing overlapping files or producing changes whose ordering/integration conflicts.
- Decisive decision or feedback right: model planner constructs the substantive subtask decomposition and allowed write sets; the root validates overlap/dependencies, uses them to schedule workers and blocks conflicting integration for explicit resolution.
- Decision owner: the model planner in auto-plan orchestration mode; operator-authored plans are a distinct configurable mode and do not create an additional parent notation for S2.
- Supporting / enforcement mechanisms: plan overlap validator, wave scheduler, isolated worktrees, cherry-pick integration and conflict event recorder.
- Closure path: an accepted model plan determines which subtask workers can operate concurrently and which are sequenced; integration success permits dependent waves. If collision survives, the root stops for explicit human choice rather than inventing autonomous resolution.
- Boundary reachability: `orchestrate` creates first-party `runPlanner` when no fixed plan is supplied, then validates its output and runs worker waves with enforced write sets.
- Why this is / is not agent-owned: without model planner the validator can reject overlap but cannot choose the decomposed work assignment; in the supported auto mode the model selects a coordination option that changes subsequent worker operation.
- Distinct S1 units: separately instantiated worker coding agents, one per `SubtaskSpec`, each with its own worktree/agent session.
- Inter-S1 disturbance: simultaneous edits to overlapping write scopes and cherry-pick collisions between worker commits.
- Attenuating coordination relation: model-chosen disjoint `writeSet` and `dependsOn` relations, validated into executable waves; conflicts are recorded and escalated rather than silently overwritten.
- Feedback into subsequent S1 behaviour: validation and wave dependencies govern later worker dispatch; integrated commit HEAD and explicit human conflict resolutions are fed into subsequent reruns or block further work.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the validation is explicitly keyed to the multi-worker *same-file write collision*, with disjointness and conflict responses; it is not merely choosing which worker speaks.
- Evidence: [planner and repair interface](https://github.com/BeforeLanding/mini-DSH/blob/0bff45e3463c38647bc0fb766e1687c31a07b1c9/src/orchestration/planner.ts#L38-L115), [overlap/wave verification](https://github.com/BeforeLanding/mini-DSH/blob/0bff45e3463c38647bc0fb766e1687c31a07b1c9/src/orchestration/plan.ts#L14-L105), [worker dispatch](https://github.com/BeforeLanding/mini-DSH/blob/0bff45e3463c38647bc0fb766e1687c31a07b1c9/src/orchestration/orchestrator.ts#L428-L460), [integration collision and follow-up](https://github.com/BeforeLanding/mini-DSH/blob/0bff45e3463c38647bc0fb766e1687c31a07b1c9/src/orchestration/orchestrator.ts#L474-L530).
- Basis: structural
- Confidence: medium
- Caveats: positive grade applies to the explicit supported auto-orchestration mode; actual merge conflicts still require human intervention, and the reviewer has not run live multi-worker model calls.

## S3 — Inside-and-now control

- State: —
- Function: a whole-system current-control owner deciding shared resources, priorities, obligations or intervention across active S1 workers is not established.
- Disturbance / variety regulated: constrained root budget, worker concurrency, cancellations and attempt failures are visible but handled by configured limits, not evidenced discretionary S3 control.
- Decisive decision or feedback right: not established as a first-party current-control judgment.
- Decision owner: operator supplies root budgets and limits; deterministic coordinator enforces them, while the model planner principally allocates task slices before execution.
- Supporting / enforcement mechanisms: `TaskGroupBudgetCoordinator`, `StopController`, `waveBudget` and task/attempt event history.
- Closure path: deterministic stops and budget exhaustion affect execution, but do not prove an autonomous or S3-specific constructor decision over the whole system.
- Why this is / is not agent-owned: a planner chooses task decomposition; the reviewed runtime does not show that agent deciding ongoing whole-system resource/priority tradeoffs in response to a current operational view.
- Evidence: [root budget construction](https://github.com/BeforeLanding/mini-DSH/blob/0bff45e3463c38647bc0fb766e1687c31a07b1c9/src/orchestration/orchestrator.ts#L31-L49), [budget allocation and dispatch](https://github.com/BeforeLanding/mini-DSH/blob/0bff45e3463c38647bc0fb766e1687c31a07b1c9/src/orchestration/orchestrator.ts#L147-L176), [runtime enforcement](https://github.com/BeforeLanding/mini-DSH/blob/0bff45e3463c38647bc0fb766e1687c31a07b1c9/src/orchestration/orchestrator.ts#L604-L651).
- Basis: structural
- Confidence: medium
- Caveats: available event views and operator override alone are not S3 constructor evidence.

### Absence scope

- Surfaces inspected: architecture, orchestration root and plan, task-group accounting, worker dispatch/attempt handling and conflict/approval controls.
- Plausible first-party paths checked: root planner as portfolio supervisor, root budget allocator as S3 controller, active attempt views, conflict escalation and user tool-approval callbacks.
- Why no material first-party path remains: the first chooses task decomposition (credited for S2), the second enforces preconfigured limits, and conflict decisions defer to an operator; no reachable S3-specific discretionary current-control loop was evidenced.

## S3* — Complementary audit

- State: —
- Function: no closed, sufficiently independent complementary audit of the operational S1 reality is demonstrated.
- Disturbance / variety regulated: invalid patches, stale reviewer snapshots and unverifiable claims are bounded, but not shown as independent organizational audit closure.
- Decisive decision or feedback right: no independent audit actor deciding a finding that is taken back into the root's operational control.
- Decision owner: standard verification commands are run deterministically; optional review-mode child provides version-bound read-only findings but explicitly does not authorize execution or a decision.
- Supporting / enforcement mechanisms: pinned-file review, verification command runner and record of commands/exit statuses.
- Closure path: verification can fail root completion; there is no evidenced complementary reality-access/audit-judgment/feedback loop with its own legitimate independent owner.
- Why this is / is not agent-owned: optional reviewer is a scoped analysis worker; it does not independently control or close audit findings into subsequent parent operation.
- Evidence: [read-only reviewer and scope](https://github.com/BeforeLanding/mini-DSH/blob/0bff45e3463c38647bc0fb766e1687c31a07b1c9/src/core/delegation-runtime.ts#L82-L144), [integration verification](https://github.com/BeforeLanding/mini-DSH/blob/0bff45e3463c38647bc0fb766e1687c31a07b1c9/src/orchestration/orchestrator.ts#L537-L562), [verifier command runner](https://github.com/BeforeLanding/mini-DSH/blob/0bff45e3463c38647bc0fb766e1687c31a07b1c9/src/orchestration/verifier.ts#L12-L46).
- Basis: structural
- Confidence: medium
- Caveats: an independently wired extension could use these findings, but no such closed first-party mode was established.

### Absence scope

- Surfaces inspected: `delegation-runtime.ts`, `review-candidate.ts`, `orchestration/verifier.ts`, integration finalizer and architecture documentation.
- Plausible first-party paths checked: read-only reviewer, file-hash validity, worktree verification, CI/evaluation scripts and parent acknowledgement of findings.
- Why no material first-party path remains: the child reviewer is version-bound non-authoritative analysis and verification commands are part of ordinary execution/reporting; an independent judge with returned S3* audit control was not evidenced.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party external/future adaptation loop with a decisive options-selection right and return to current capability is established.
- Disturbance / variety regulated: context pressure, model errors and token usage are managed within runs; they do not establish prospective external adaptation.
- Decisive decision or feedback right: absent for S4.
- Decision owner: configured context and token algorithms and operator-selected model/provider.
- Supporting / enforcement mechanisms: session context compaction, provider retries, token calibration, development benchmarks and testing scripts.
- Closure path: these mechanisms can change run budgeting/context representation, not the system's selected future capabilities based on external change.
- Why this is / is not agent-owned: no evidenced agent decides a new system-level prospective capability option and applies it to later supported operation.
- Evidence: [context compaction](https://github.com/BeforeLanding/mini-DSH/blob/0bff45e3463c38647bc0fb766e1687c31a07b1c9/src/core/compaction-runtime.ts#L1-L120), [provider/error/budget description](https://github.com/BeforeLanding/mini-DSH/blob/0bff45e3463c38647bc0fb766e1687c31a07b1c9/docs/ARCHITECTURE.md#L14-L31).
- Basis: structural
- Confidence: medium
- Caveats: project research documents and benchmark probes are development surfaces, not automatically shipped S4.

### Absence scope

- Surfaces inspected: architecture, model dispatch, context/compaction/token calibration, application production config, orchestration planner and evaluation directories.
- Plausible first-party paths checked: token calibration as adaptation, retry policy, planner's future task plan, benchmark-driven repo development.
- Why no material first-party path remains: scoped run-level resource/context corrections and developer experiments do not couple a real outside-and-future option judgment to the installed harness's continuing capability.

## S5 — Policy and identity

- State: —
- Function: a returned identity or ultimate-policy decision for the harness is not established.
- Disturbance / variety regulated: tool risk, user confirmation and configured safety limits are present but are execution permissions, not identity/ultimate-policy governance.
- Decisive decision or feedback right: no first-party ultimate-policy choice and authoritative return loop.
- Decision owner: developer defaults and local operator settings/approval callbacks; model agent decides within their bounds.
- Supporting / enforcement mechanisms: tool-effect registry, session/workspace approval scope, model/tool/provider configuration and sandbox checks.
- Closure path: human can permit or deny individual tool calls; this does not create a first-party S5 issue → legitimate parent authority → returned system policy/identity decision loop.
- Why this is / is not agent-owned: the model does not set ultimate policy, and tool approval does not convert ordinary authorizations to S5.
- Evidence: [tool authorization](https://github.com/BeforeLanding/mini-DSH/blob/0bff45e3463c38647bc0fb766e1687c31a07b1c9/src/core/tool-authorization.ts#L1-L155), [central tool gate](https://github.com/BeforeLanding/mini-DSH/blob/0bff45e3463c38647bc0fb766e1687c31a07b1c9/src/core/tool-runtime.ts#L1-L150), [operator approval](https://github.com/BeforeLanding/mini-DSH/blob/0bff45e3463c38647bc0fb766e1687c31a07b1c9/src/orchestration/orchestrator.ts#L486-L506).
- Basis: structural
- Confidence: medium
- Caveats: developer governance and independent host operators are not bundled as S5 policy recursion.

### Absence scope

- Surfaces inspected: root CLI and config, `tool-authorization.ts`, application sandbox/policy, orchestration human choice and documentation.
- Plausible first-party paths checked: approvals for file and Bash effects, mutable configuration, cancellation, project-level maintained policy documents.
- Why no material first-party path remains: approvals and static config govern particular operations but do not establish a live ultimate-policy/identity authority and returned policy closure for the declared harness.

## Distributed OSS parent arrangement

No first-party multi-contributor governance or shared legitimate higher-recursion parent policy decision is wired into the installed mini-DSH product. Local approval is bounded to local tool/risk and merge-conflict operations.

## Self-hosted and non-human modes

The local CLI is self-hosted, with operator approval and root orchestration configuration. These are not independently sufficient for an S3/S4/S5 parent-mode notation.

## Recursion

The root orchestration mode includes multiple child coding-agent S1 units, but their creation alone does not establish a second complete VSM recursion. The reported vector refers to the root coding-task harness plus its selected orchestration mode.

## Variety and escalation

Run budgets, tool result events and verification failures attenuate operational variety. The concrete unresolved merge collision is surfaced to a local human with `abort`, `skip-subtask` and bounded rerun options rather than being silently retried. Missing human resolution yields `needs_human`; it is not treated as autonomous higher-function closure.

## Evidence gaps

No live DeepSeek-provider invocation, remote MCP server, or multi-worker integration was executed for this source assessment. The positive S2 claim is based on the shipped model-plan/validation/dispatch path and the concrete same-file conflict contract, not observed model quality. No independent external audit is claimed.
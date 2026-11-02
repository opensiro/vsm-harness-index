---
harness_id: looplet
project_name: Looplet
repository: https://github.com/hsaghir/looplet
review_ref: 7a7e1a296cb5d1d61a3cd4fcfc9eafbecab9a4d2
reviewed_at: 2026-11-02
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# Looplet

## Review boundary

- System in focus: Looplet's Python tool-calling runtime and intentionally exposed operational evaluation constructor.
- Purpose and identity: Run a model-driven task through first-party tool dispatch, state feedback and completion.
- Relevant environment: Host Python application, configured model provider, supplied tools and their effects.
- Standard-distribution boundary: Pinned source distribution, synchronous/asynchronous loops, cartridge loading, run persistence, child-loop helpers, optional EvalHook and outcome grading APIs. The README distinguishes this source preview from PyPI 0.4.1.
- Credited operating / distribution surfaces: `src/looplet/loop.py`, `async_loop.py`, `subagent.py`, `evals.py`, documented run and hook interfaces.
- Adjacent first-party surfaces excluded from ownership: Repository development, CI/release, regression demonstrations, domain example cartridges and test authors are not runtime decision owners. EvalHook itself is an exposed runtime constructor, distinct from any particular development grader.
- First-party operating / deployment modes considered: Embedded Python/cartridge runs, execution-v1 and optional standard-v1 policies, sync/async child loops, optional host-composed protected outcome grading.
- Recursion level: One host-owned Looplet application with model-driven task runs.
- Reviewed revision: `7a7e1a296cb5d1d61a3cd4fcfc9eafbecab9a4d2`.
- Observation date: 2026-11-02.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

[README.md](https://github.com/hsaghir/looplet/blob/7a7e1a296cb5d1d61a3cd4fcfc9eafbecab9a4d2/README.md) and [operations.md](https://github.com/hsaghir/looplet/blob/7a7e1a296cb5d1d61a3cd4fcfc9eafbecab9a4d2/docs/operations.md#L110) expose one engine: build context, request model output, parse tool calls, apply hooks, execute tools, record results, then feed the result back into subsequent requests. Completion is a distinct accepted terminal signal; budget termination is not success. Default compaction and evidence retention preserve operational context. Sync/async child helpers isolate state and carry inherited permission/budget constraints, while shared external resources explicitly remain caller-owned. Providers supply inference; Looplet owns dispatch/feedback. Optional EvalHook separates outcome collectors and grader-only expectations from the model-visible task. Human approval and custom hooks are integration points, not automatically metasystem authority.

## Operational model

A run produces an answer or tool-mediated effect for a supplied task. The model chooses local next actions within host-selected tools/limits; the first-party engine executes them and returns observations. A child run can be a separate work unit, but nesting alone establishes neither recursive viability nor inter-unit coordination. The optional evaluation constructor supplies complementary outcome access; a host must compose protected graders, audit judgment and corrective use.

## S1 — Operations

- State: A
- Function: Task-directed model/tool work with local response to observations.
- Disturbance / variety regulated: Tool errors, changing results, incomplete answers and context pressure.
- Decisive decision or feedback right: Select next tool/action or propose completion in light of the updated conversation.
- Decision owner: The configured model-driven task agent.
- Supporting / enforcement mechanisms: First-party parsing, tool registry, hooks, retention, compaction, limits and checkpoints.
- Closure path: Dispatched results and rejected completion feedback enter subsequent model turns; accepted completion yields a result.
- Boundary reachability: Public composable_loop and async counterpart execute this path with configured backend and Python tools; no external agent harness owns the loop.
- Why this is / is not agent-owned: Removing model discretion leaves dispatch/limits but no equivalent task-dependent action choice.
- Evidence: [loop.py](https://github.com/hsaghir/looplet/blob/7a7e1a296cb5d1d61a3cd4fcfc9eafbecab9a4d2/src/looplet/loop.py#L2583), especially model-result handling and terminal-gate feedback; [README.md](https://github.com/hsaghir/looplet/blob/7a7e1a296cb5d1d61a3cd4fcfc9eafbecab9a4d2/README.md); [operations.md](https://github.com/hsaghir/looplet/blob/7a7e1a296cb5d1d61a3cd4fcfc9eafbecab9a4d2/docs/operations.md#L110).
- Basis: structural
- Confidence: high for source ownership; no provider run was executed here.
- Caveats: Outcome correctness and safety depend on supplied tools, model and host isolation.

## S2 — Coordination

- State: —
- Function: Attenuation of a specific disturbance among distinct S1 units.
- Disturbance / variety regulated: The candidate regulation was checked at the declared runtime recursion.
- Decisive decision or feedback right: No supplied function-specific discretionary closure was established.
- Decision owner: No first-party owner for this function; caller configuration remains caller-owned.
- Supporting / enforcement mechanisms: Runtime hooks, persistence and limits support execution without acquiring organizational discretion.
- Closure path: No material shipped closure for this function.
- Why this is / is not agent-owned: An autonomous S1 loop does not transfer ownership of this separate function.
- Evidence: [subagent.py](https://github.com/hsaghir/looplet/blob/7a7e1a296cb5d1d61a3cd4fcfc9eafbecab9a4d2/src/looplet/subagent.py#L897); [operations.md](https://github.com/hsaghir/looplet/blob/7a7e1a296cb5d1d61a3cd4fcfc9eafbecab9a4d2/docs/operations.md#L110)
- Basis: structural
- Confidence: medium-high, bounded to this distribution.
- Caveats: A downstream application can add its own organization.

### Absence scope

- Surfaces inspected: [subagent.py](https://github.com/hsaghir/looplet/blob/7a7e1a296cb5d1d61a3cd4fcfc9eafbecab9a4d2/src/looplet/subagent.py#L897); [operations.md](https://github.com/hsaghir/looplet/blob/7a7e1a296cb5d1d61a3cd4fcfc9eafbecab9a4d2/docs/operations.md#L110)
- Plausible first-party paths checked: Isolated child loops, async concurrency, shared budgets, inherited security and caller-owned resources.
- Why no material first-party path remains: Child execution/semaphores and shared quota enforcement do not supply a specific inter-S1 interference-adjustment decision/feedback relation. No application-specific collision or coordination actor is shipped at this boundary.


## S3 — Inside-and-now control

- State: —
- Function: Whole-system current regulation of resources, commitments and constraints.
- Disturbance / variety regulated: The candidate regulation was checked at the declared runtime recursion.
- Decisive decision or feedback right: No supplied function-specific discretionary closure was established.
- Decision owner: No first-party owner for this function; caller configuration remains caller-owned.
- Supporting / enforcement mechanisms: Runtime hooks, persistence and limits support execution without acquiring organizational discretion.
- Closure path: No material shipped closure for this function.
- Why this is / is not agent-owned: An autonomous S1 loop does not transfer ownership of this separate function.
- Evidence: [loop.py](https://github.com/hsaghir/looplet/blob/7a7e1a296cb5d1d61a3cd4fcfc9eafbecab9a4d2/src/looplet/loop.py#L2583); [subagent.py](https://github.com/hsaghir/looplet/blob/7a7e1a296cb5d1d61a3cd4fcfc9eafbecab9a4d2/src/looplet/subagent.py#L897); [operations.md](https://github.com/hsaghir/looplet/blob/7a7e1a296cb5d1d61a3cd4fcfc9eafbecab9a4d2/docs/operations.md#L110)
- Basis: structural
- Confidence: medium-high, bounded to this distribution.
- Caveats: A downstream application can add its own organization.

### Absence scope

- Surfaces inspected: [loop.py](https://github.com/hsaghir/looplet/blob/7a7e1a296cb5d1d61a3cd4fcfc9eafbecab9a4d2/src/looplet/loop.py#L2583); [subagent.py](https://github.com/hsaghir/looplet/blob/7a7e1a296cb5d1d61a3cd4fcfc9eafbecab9a4d2/src/looplet/subagent.py#L897); [operations.md](https://github.com/hsaghir/looplet/blob/7a7e1a296cb5d1d61a3cd4fcfc9eafbecab9a4d2/docs/operations.md#L110)
- Plausible first-party paths checked: Model/step limits, shared child budgets, cancellation, deadlines, approval handlers and operator configuration, including possible parent closure.
- Why no material first-party path remains: These enforce host-preselected run constraints or expose generic hooks. Neither a whole-application current-control agent nor a function-specific parent view→decision→returned regulation loop is supplied.


## S3* — Complementary audit

- State: C
- Function: Complementary outcome-grounded challenge to a run's completion/correctness claim.
- Disturbance / variety regulated: Accepted done() or plausible trajectory despite wrong external artifacts.
- Decisive decision or feedback right: Judge outcome evidence separately from the producing agent, then use the finding to accept or correct operation.
- Decision owner: Host-composed evaluator/auditor; autonomous judgment and corrective authority are not installed by default.
- Supporting / enforcement mechanisms: EvalContext, collectors, grader-only expected data, EvalHook results, saved evidence, EvalReport/assert_passed and optional judge backend.
- Closure path: The API exposes findings and failed required grading to the caller; host must connect them to corrective control. This incomplete composition supports C, not A.
- Boundary reachability: EvalHook can attach directly to an ordinary public loop, run independent collectors after completion and expose assessment/results. It is an explicit outcome-evaluation constructor, not merely a generic callback.
- Why this is / is not agent-owned: Framework collection/aggregation is not an independent audit judgment; protection and returned control require host composition.
- Claim being audited: Completion/correctness of the task's final output.
- Ordinary reporting path: Agent terminal output and run trajectory.
- Complementary access path: Collectors inspect actual files, tests or other outcome artifacts and expose them to graders outside the agent-visible task.
- Independence boundary: Separate collector/grader roles and grader-only expectations support complementary access; the host must preserve isolation and select independent judgment.
- Who acts on findings: Host/auditor through returned EvalReport/results; no default corrective manager.
- Evidence: [evals.py](https://github.com/hsaghir/looplet/blob/7a7e1a296cb5d1d61a3cd4fcfc9eafbecab9a4d2/src/looplet/evals.py#L2242); [operations.md](https://github.com/hsaghir/looplet/blob/7a7e1a296cb5d1d61a3cd4fcfc9eafbecab9a4d2/docs/operations.md#L110) coding-test-freshness and protected-grading distinction; [hooks.md](https://github.com/hsaghir/looplet/blob/7a7e1a296cb5d1d61a3cd4fcfc9eafbecab9a4d2/docs/hooks.md).
- Basis: structural
- Confidence: medium-high for the constructor, not a claim of a deployed independent audit.
- Caveats: Routine completion hooks and self-controlled tests alone would not establish S3*. EvalHook does not itself guarantee protected execution or correction.

## S4 — Outside-and-then intelligence

- State: —
- Function: External/prospective intelligence returning adaptation options into current capability.
- Disturbance / variety regulated: The candidate regulation was checked at the declared runtime recursion.
- Decisive decision or feedback right: No supplied function-specific discretionary closure was established.
- Decision owner: No first-party owner for this function; caller configuration remains caller-owned.
- Supporting / enforcement mechanisms: Runtime hooks, persistence and limits support execution without acquiring organizational discretion.
- Closure path: No material shipped closure for this function.
- Why this is / is not agent-owned: An autonomous S1 loop does not transfer ownership of this separate function.
- Evidence: [README.md](https://github.com/hsaghir/looplet/blob/7a7e1a296cb5d1d61a3cd4fcfc9eafbecab9a4d2/README.md); [loop.py](https://github.com/hsaghir/looplet/blob/7a7e1a296cb5d1d61a3cd4fcfc9eafbecab9a4d2/src/looplet/loop.py#L2583); [operations.md](https://github.com/hsaghir/looplet/blob/7a7e1a296cb5d1d61a3cd4fcfc9eafbecab9a4d2/docs/operations.md#L110); [evals.py](https://github.com/hsaghir/looplet/blob/7a7e1a296cb5d1d61a3cd4fcfc9eafbecab9a4d2/src/looplet/evals.py#L2242)
- Basis: structural
- Confidence: medium-high, bounded to this distribution.
- Caveats: A downstream application can add its own organization.

### Absence scope

- Surfaces inspected: [README.md](https://github.com/hsaghir/looplet/blob/7a7e1a296cb5d1d61a3cd4fcfc9eafbecab9a4d2/README.md); [loop.py](https://github.com/hsaghir/looplet/blob/7a7e1a296cb5d1d61a3cd4fcfc9eafbecab9a4d2/src/looplet/loop.py#L2583); [operations.md](https://github.com/hsaghir/looplet/blob/7a7e1a296cb5d1d61a3cd4fcfc9eafbecab9a4d2/docs/operations.md#L110); [evals.py](https://github.com/hsaghir/looplet/blob/7a7e1a296cb5d1d61a3cd4fcfc9eafbecab9a4d2/src/looplet/evals.py#L2242)
- Plausible first-party paths checked: Context/memory, model routing, recovery, saved grading and domain research cartridges; autonomous and parent adaptation alternatives.
- Why no material first-party path remains: These supply execution, current context or observations. Domain research tasks are S1 applications; no shipped prospective environment→adaptation-option→capability regulation loop is established for Looplet itself.


## S5 — Policy and identity

- State: —
- Function: Identity and ultimate-policy closure at the application recursion.
- Disturbance / variety regulated: The candidate regulation was checked at the declared runtime recursion.
- Decisive decision or feedback right: No supplied function-specific discretionary closure was established.
- Decision owner: No first-party owner for this function; caller configuration remains caller-owned.
- Supporting / enforcement mechanisms: Runtime hooks, persistence and limits support execution without acquiring organizational discretion.
- Closure path: No material shipped closure for this function.
- Why this is / is not agent-owned: An autonomous S1 loop does not transfer ownership of this separate function.
- Evidence: [README.md](https://github.com/hsaghir/looplet/blob/7a7e1a296cb5d1d61a3cd4fcfc9eafbecab9a4d2/README.md); [operations.md](https://github.com/hsaghir/looplet/blob/7a7e1a296cb5d1d61a3cd4fcfc9eafbecab9a4d2/docs/operations.md#L110); [hooks.md](https://github.com/hsaghir/looplet/blob/7a7e1a296cb5d1d61a3cd4fcfc9eafbecab9a4d2/docs/hooks.md)
- Basis: structural
- Confidence: medium-high, bounded to this distribution.
- Caveats: A downstream application can add its own organization.

### Absence scope

- Surfaces inspected: [README.md](https://github.com/hsaghir/looplet/blob/7a7e1a296cb5d1d61a3cd4fcfc9eafbecab9a4d2/README.md); [operations.md](https://github.com/hsaghir/looplet/blob/7a7e1a296cb5d1d61a3cd4fcfc9eafbecab9a4d2/docs/operations.md#L110); [hooks.md](https://github.com/hsaghir/looplet/blob/7a7e1a296cb5d1d61a3cd4fcfc9eafbecab9a4d2/docs/hooks.md)
- Plausible first-party paths checked: System prompts, permission policies, approval handlers, cartridge definitions and maintainer release governance; possible parent return paths.
- Why no material first-party path remains: Host-written constraints and individual action approval do not route an identity/ultimate-policy matter to legitimate authority and return a governing decision. Repository maintainer governance is adjacent.


## Recursion

Child loops have separate state and inherited bounds, but no complete local metasystem is established. Technical nesting is not a viable-system recursion claim.

## Variety and escalation

Tool feedback and rejected completion retain local task variety; context projection can attenuate detail while originals remain separately available. Cooperative cancellation and hard limits are explicit runtime stops. Approval callbacks return task-specific authority to the host; no algedonic or S5 function is inferred from that transport.

## Evidence gaps

This is pinned-source assessment, not live model/provider, security-isolation or domain-quality validation. Host-provided tools, collectors and protected graders were not instantiated as a deployed organization. S3*=C records precisely the missing composed audit actor/authority/return path. No unseen downstream application or private run is credited.

---
harness_id: cubeloop
project_name: CubeLoop
repository: https://github.com/cubeplexai/cubeloop
review_ref: eb798f9a20c1f516d6a59a991a63a9d4c630f4bf
reviewed_at: 2026-10-20
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# CubeLoop

## Review boundary

- System in focus: Public CubeLoop Python SDK as a model-backed, goal-facing agent/task execution harness, optionally including ephemeral subagent delegation, a model-based current-goal completion evaluator, HITL tool gates, tracing and durable session facilities.
- Purpose and identity: Provide async agent execution and supporting tool, provider, middleware, persistence and streaming primitives to embedding application authors; this is not by itself an institution or portfolio of independently viable operating departments.
- Relevant environment: Python package, configured Anthropic/OpenAI-compatible or custom BoundModel, application-defined AgentTools and middleware, optional SQL/SQLite/checkpoint persistence, human approval channel and external user/organization.
- Standard-distribution boundary: Shipped `cubeloop/agent/` model→tool feedback path invoked by `Agent.prompt` and `ExecutionSession.execute`; optional first-party `middleware/subagents`, `middleware/todo`, `middleware/goal`, `hitl/`, `deferred/`, `providers/`, `checkpointer/`, `session/` and `tracing/` installed features. Do not attribute host application/agent employment, external provider inner behavior, maintainer/project release governance or roadmap decisions to the SDK.
- Credited operating / distribution surfaces: [`cubeloop/agent/agent.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/agent/agent.py); [`cubeloop/agent/loop.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/agent/loop.py); [`cubeloop/agent/tools.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/agent/tools.py); [`cubeloop/providers/base.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/providers/base.py); [`cubeloop/middleware/subagents.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/middleware/subagents.py); [`cubeloop/middleware/goal.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/middleware/goal.py); [`cubeloop/middleware/todo.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/middleware/todo.py); [`cubeloop/hitl/middleware.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/hitl/middleware.py); [`cubeloop/session/session.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/session/session.py); [`cubeloop/checkpointer/base.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/checkpointer/base.py); [`cubeloop/deferred/middleware.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/deferred/middleware.py); [`cubeloop/tracing/tracer.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/tracing/tracer.py). These are imported/wired by public SDK modes; support packages differ in their callable decision authority.
- Adjacent first-party surfaces excluded from ownership: GitHub CI, repository `tests/`, `examples/`, `dev/specs/` and `dev/plans/`, website/SDK tutorials, packaging/maintainer PR administration, the separate CubePlex product/service using this SDK, and configured third-party provider logic, customer tools, policies and staff. These may corroborate or illustrate shipped paths but cannot supply a missing first-party VSM owner or closure.
- First-party operating / deployment modes considered: direct Agent with one bound model and tools; parallel/sequential tool execution; prompt/continue/resume with checkpoint and session; optional SubagentMiddleware ephemeral child model agents; optional GoalMiddleware separate evaluator, TodoListMiddleware planning guard, deferred tools, provider fallback, human approval/edited-tool-request channels, tracing, and custom host middleware callbacks. No automatic assumption that all optional components are enabled together.
- Recursion level: One user-/application-requested workstream with an Agent and optional task-specific child agents; children are ephemeral delegated task agents rather than established independently viable organizational departments. Multiple SDK consumers or the external CubePlex platform are not a single included first-party organization.
- Reviewed revision: `cubeplexai/cubeloop@eb798f9a20c1f516d6a59a991a63a9d4c630f4bf`; GitHub stable repository ID `1233657891`, Git tree `42c15eb46b34583f50ea6f1b74f9d67a674b1bc6`, MIT, nonfork, nonarchived; frozen source-first review 2026-10-20.
- Observation date: 2026-10-20.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

The public `Agent` constructs configured model and tools, accepts caller prompts and uses `run_agent_loop` / `_run_loop_inner` to get model output and execute tool calls while appending tool results/events into the next model context. The `ExecutionSession` boundary owns a sequential run/attempt lifecycle, pending inputs, cancellation, subscriber delivery, checkpoint snapshots and resumption; it preserves operations but does not supply second-order organizational policy. Bound providers include real public API adapters, with a configured fallback chain. [`cubeloop/agent/agent.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/agent/agent.py); [`cubeloop/agent/loop.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/agent/loop.py); [`cubeloop/providers/base.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/providers/base.py); [`cubeloop/session/session.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/session/session.py); [`cubeloop/providers/fallback.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/providers/fallback.py).

`SubagentMiddleware` exposes a delegation tool that creates a separately running **ephemeral child Agent** selected by a configured SubagentSpec and returns its result to the requesting parent. Checkpointed HITL bindings are explicitly filtered from child tools/middleware where the parent run_id would be invalid. `TodoListMiddleware` enables in-task list revisions with a guard against inconsistent finalization. `GoalMiddleware` is an optional independent **task-goal evaluator model** called on run end: after checking recent conversation and declared `/goal` condition, it stops or injects a synthetic current-goal continuation message. These are meaningful task operations, not automatically VSM S2 coordination, independent S3* reality audit, future S4 strategy, or governance S5. [`cubeloop/middleware/subagents.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/middleware/subagents.py); [`cubeloop/middleware/todo.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/middleware/todo.py); [`cubeloop/middleware/goal.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/middleware/goal.py).

`ApprovalPolicyMiddleware` lets a host-supplied policy approve, deny or ask a human before a specified tool call; the HITL channel may pause, edit, time out or resume a call. `Tracer` attaches recording/export spans; checkpoint and Session event receipts instrument one agent's actual work. Those mechanisms offer safety/durability/observability, but neither introduces an independent organizational S3 current manager nor an S3* reality-check mandate reporting to one. [`cubeloop/hitl/middleware.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/hitl/middleware.py); [`cubeloop/hitl/channel.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/hitl/channel.py); [`cubeloop/tracing/tracer.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/tracing/tracer.py); [`cubeloop/session/session.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/session/session.py); [`cubeloop/checkpointer/base.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/checkpointer/base.py).

## Operational model

One embedding user supplies a task and tools. Within that task a configured model can select operations, observe tool feedback, revise current TODOs and optionally request delegated child execution. The host may regulate tool admission and checkpoint task state. The separately configured goal evaluator closes only the current request's finish-or-continue loop. Distributed organizational policy or external future strategy remains outside this single-SDK recursion.

## S1 — Operations

- State: A
- Function: Goal-facing model-selected task operations through first-party bound model/tool feedback, with optional ephemeral delegated subagents and current-goal evaluator continuation.
- Disturbance / variety regulated: New user requests, changing tool execution results, exceptions, model fallback, context window pressure, streaming interruptions, human tool admission, pending task state and checkpoints.
- Decisive decision or feedback right: The configured bound model chooses which registered tool call to issue or when to finish; child-bound-model runs choose task-local actions; the optional goal evaluator returns an achieved/unmet verdict and injects current-task feedback.
- Decision owner: Model in a first-party Agent loop has per-goal tool-choice discretion; host configures tools, middleware, provider, model and approval. The ephemeral child model is an S1 task extension, not a separate metasystem.
- Supporting / enforcement mechanisms: run_agent_loop / _run_loop_inner model streaming, tool-cycle and tool result append; Agent.prompt session, middleware callbacks, concurrently executable tool calls, checkpoint/resume and provider fallback; GoalMiddleware on_run_end verification and child delegation.
- Closure path: User message → BoundModel stream/generate → assistant tool choices → first-party tool execution/exception reporting → observed result becomes subsequent context → model next choice or final answer; child delegation returns an ephemeral child output. Optional goal evaluator can feed a not-yet-achieved reason back and restart current-goal work.
- Boundary reachability: Published Agent(model=BoundModel, tools=[...], middleware=[...]) and prompt() call the runtime; actual Anthropic/OpenAI adapters exist. Child model execution, GoalMiddleware and provider failover are optional but wired first-party. This is not inferred from docs or test fixtures.
- Why this is / is not agent-owned: Without configured model discretion the remaining session/checkpoint/approval machinery could not select novel goal-sensitive tool paths. A real model must be configured, but the first-party harness provides reachable running infrastructure.
- Evidence: [`cubeloop/agent/agent.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/agent/agent.py); [`cubeloop/agent/loop.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/agent/loop.py); [`cubeloop/agent/tools.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/agent/tools.py); [`cubeloop/providers/base.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/providers/base.py); [`cubeloop/providers/openai.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/providers/openai.py); [`cubeloop/providers/anthropic.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/providers/anthropic.py); [`cubeloop/middleware/subagents.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/middleware/subagents.py); [`cubeloop/middleware/goal.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/middleware/goal.py); [`cubeloop/session/session.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/session/session.py).
- Basis: Explicit structural runtime wiring, corroborated by runnable examples; no task-quality experiment run.
- Confidence: High for S1 model/feedback architecture.
- Caveats: Model provider availability, model correctness and external app tool semantics are not reproduced. Ephemeral subagent capability does not automatically establish a stable second viable organizational S1 department.

## S2 — Coordination

- State: —
- Function: No independently governed inter-operating-unit coordination that dampens demonstrated conflicts among distinct viable S1 departments at this framework recursion.
- Disturbance / variety regulated: Concurrent tools/child requests, inconsistent results and user steering can disrupt one task, but distributed multi-department interference is not established.
- Decisive decision or feedback right: Agent tool concurrency and deferred dispatch decide task execution order; child subagents return findings to parent. No S2-specific decision regarding shared commitments among separately viable departmental S1s.
- Decision owner: Caller-configured parent model and runtime sequencing/dispatch; no separately identified S2 coordinating owner across viable S1s.
- Supporting / enforcement mechanisms: Parallel/sequential tool execution, SubagentMiddleware, shared tools, deferred tool groups, todo guard and execution-session queue.
- Closure path: Tool and child outcomes return to the same parent task; session consumer ordering and tool batching do not close an inter-S1 constraint/oscillation feedback loop.
- Why this is / is not agent-owned: Subagent instances are ephemeral task-service workers with model and tools, not independently continuing viable organizational departments under a common reciprocal operating regime. Task-level scheduling is not S2.
- Evidence: [`cubeloop/middleware/subagents.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/middleware/subagents.py); [`cubeloop/agent/loop.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/agent/loop.py); [`cubeloop/agent/tools.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/agent/tools.py); [`cubeloop/deferred/middleware.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/deferred/middleware.py); [`cubeloop/middleware/todo.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/middleware/todo.py); [`cubeloop/session/session.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/session/session.py).
- Basis: Bounded negative at the shipped SDK Agent/task boundary.
- Confidence: High.
- Caveats: An external multi-agent product might use CubeLoop as its substrate and supply real inter-unit coordination; that external arrangement is not within this source-bound assessment.

### Absence scope

- Surfaces inspected: Agent loop, SubagentMiddleware, tool execution/deferred dispatch, TODO guard and session queue.
- Plausible first-party paths checked: Parallel tool outcomes, multiple ephemeral child responses, shared tools and single-thread attempt scheduling as candidate cross-S1 conflict damping.
- Why no material first-party path remains: These handle one goal's dependent tool work and ephemeral delegates without distinct viable departments, reciprocally competing obligations or feedback that reduces recurring inter-S1 interference.

## S3 — Inside-and-now control

- State: —
- Function: No first-party current whole-system operational-management loop owning a portfolio of independently viable S1s, resource choices and returned departmental obligations.
- Disturbance / variety regulated: Run failures, tool-call admission, concurrent execution, user controls, agent steering/follow-ups and task checkpoint errors threaten present task completion.
- Decisive decision or feedback right: Agent chooses goal-local actions, caller/HITL middleware may approve or deny one tool, user can steer/abort/resume. ExecutionSession arbitrates one agent's attempts, not discretionary current-resource allocation across S1 departments.
- Decision owner: External host/user selects tool exposure, policy, execution mode and the model; middleware supplies admission guard; no distinct whole-current S3 organizational owner.
- Supporting / enforcement mechanisms: ApprovalPolicyMiddleware, ConfirmToolCallMiddleware, session single-attempt lock, persisted input receipts, middleware todo finalization guards, checkpoint/recovery.
- Closure path: Operation request → approval/denial or interruption → same task accepts/block/resume; no aggregate viable-S1 status → S3 authoritative allocation → changed operating units and feedback.
- Why this is / is not agent-owned: Interactive HITL decisions and deterministic session arbitration are concrete but functionally local. A configurable human approval channel is not by itself an S3=P parent-managed organization.
- Evidence: [`cubeloop/hitl/middleware.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/hitl/middleware.py); [`cubeloop/hitl/channel.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/hitl/channel.py); [`cubeloop/session/session.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/session/session.py); [`cubeloop/agent/agent.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/agent/agent.py); [`cubeloop/middleware/todo.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/middleware/todo.py); [`cubeloop/checkpointer/base.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/checkpointer/base.py).
- Basis: Bounded absence after checking supported HITL, session and delegated child modes.
- Confidence: High.
- Caveats: An embedding application can place an external manager above multiple CubeLoop agents; its decisions cannot be counted as this SDK's native S3.

### Absence scope

- Surfaces inspected: Agent/session boundaries, HITL approval and edits, goal/TODO guard, checkpoint/recovery and delegation into child tasks.
- Plausible first-party paths checked: Parent task control, abort/steering, session attempt lock, policy approval and possible human/current supervisory control.
- Why no material first-party path remains: First-party control is task/session admission under host configuration, with no distinct owner collecting status of independently viable units, choosing collective current priorities and feeding binding allocation to them.

## S3* — Complementary audit

- State: —
- Function: No complementary independently owned direct-operating-reality audit with correction returned to a distinct S3 owner.
- Disturbance / variety regulated: Current runs can produce misleading completion statements or obscure tool faults and paused approvals.
- Decisive decision or feedback right: GoalMiddleware optionally asks a separate evaluator model whether a *single task goal* is met from a recent transcript; it may resume that very task. Tracing records spans and HITL history; neither supplies independent system-operating reality discovery to current S3 management.
- Decision owner: Optional evaluator BoundModel is owned by the goal middleware and governs only completion of a given requested goal, not an S3* audit mandate. Tracing is host-attached instrumentation.
- Supporting / enforcement mechanisms: GoalMiddleware verdict, tracing/Recorder/Tracer, tool event streams, todo finalization guard and session receipts.
- Closure path: Transcript → goal judge → goal-current-task continuation/stop. Trace → observability sink. There is no independently checked operational reality → adjudicated management correction → S3 decision returned to operating units.
- Why this is / is not agent-owned: Even though a *second model* evaluates task outcome, it sees the supplied conversation, not direct organizational reality under independent audit authority. Mere judge separation does not establish S3*; there is no first-party S3 manager receiving an audit challenge.
- Evidence: [`cubeloop/middleware/goal.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/middleware/goal.py); [`cubeloop/tracing/tracer.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/tracing/tracer.py); [`cubeloop/middleware/todo.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/middleware/todo.py); [`cubeloop/session/session.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/session/session.py); [`cubeloop/hitl/middleware.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/hitl/middleware.py).
- Basis: Bounded negative with explicit inspection of the plausible evaluator/audit path.
- Confidence: Medium-high.
- Caveats: If deployed with externally mandated trace reviewers and management correction, a bigger composite boundary may have S3*; it is not shipped by the bounded SDK.

### Absence scope

- Surfaces inspected: GoalMiddleware's second model, recent transcript-based condition verification, Tracer/Recorder, HITL ledgers and TodoListMiddleware guards.
- Plausible first-party paths checked: An independent evaluator model as potential auditor; event telemetry as reality evidence; HITL/external trace viewer as possible correction authority.
- Why no material first-party path remains: The evaluator checks task completion from supplied transcript and returns to same S1 work; the tracing backend does not independently inspect operating reality or report material challenged findings to an evidenced S3 management decision loop.

## S4 — Outside-and-then intelligence

- State: —
- Function: No shipped owner and closure for future-facing external intelligence and accepted reconfiguration of subsequent organizational capability.
- Disturbance / variety regulated: Provider failures, task complexity, rising context costs, new task types or changing operational surroundings would motivate later platform adaptation.
- Decisive decision or feedback right: BoundModel fallback picks an alternate configured provider on failure; child agents handle current delegated work; goal evaluator continues *current* task, todo updates current task steps. None adopts a new future strategy/method for subsequent operating runs.
- Decision owner: Host developer supplies fallback chain, middleware and tools in advance; no first-party prospective adaptive strategy process makes and returns a decision.
- Supporting / enforcement mechanisms: FallbackBoundModel, goal evaluation feedback, task todo plan, optional compaction, cached state and middleware hook plumbing.
- Closure path: Failure→configured fallback inside same request, goal judge→same request continuation; no boundary-spanning outside surveillance → future option → legitimate acceptance → changed next-run operating rules.
- Why this is / is not agent-owned: Runtime retrying/fallback or agent revising a TODO list within one goal is S1 adaptation, not VSM outside-and-then S4. The dev/spec/plan files document future engineering intent, not shipped executable S4 ownership.
- Evidence: [`cubeloop/providers/fallback.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/providers/fallback.py); [`cubeloop/middleware/goal.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/middleware/goal.py); [`cubeloop/middleware/todo.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/middleware/todo.py); [`cubeloop/agent/agent.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/agent/agent.py); [`cubeloop/middleware/base.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/middleware/base.py); [`README.md`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/README.md).
- Basis: Bounded negative after inspecting shipped candidate future-strategy routes.
- Confidence: High for current packaged modes.
- Caveats: Cross-run learning introduced by downstream host code is not evidenced by the pinned first-party framework; a future release may change this.

### Absence scope

- Surfaces inspected: FallbackBoundModel, goal continuation, TODO state machine, parent-to-ephemeral child handoff, provider/middleware configuration, checkpoint state, plans/specs boundary.
- Plausible first-party paths checked: Provider error failover, task-goal evaluation, evolving TODO lists, deferred discovery and developer-driven changes as prospective adaptation candidates.
- Why no material first-party path remains: All shipped closures are within-task response or deterministic host-configured alternatives; no accepted future-organization strategy or next-run operating-capability change is authored/returned by an S4 owner.

## S5 — Policy and identity

- State: —
- Function: No first-party legitimate identity/ultimate-purpose policy-authoring owner with authoritative return into the framework's subsequent organizational operation.
- Disturbance / variety regulated: Operators must decide which tools and models to expose, when to require human approval and how to handle agents' data.
- Decisive decision or feedback right: Tool approvals can approve/deny/edit one call; application integrator configures system prompt, permissions and middleware. No user/parent procedure for binding constitutional policy or identity changes across viable S1s is implemented.
- Decision owner: User/integrator owns purpose and application governance outside this SDK; runtime's policy callbacks only execute configured local task admission.
- Supporting / enforcement mechanisms: Agent(system_prompt=...,model=...,tools=...), HITL ApprovalDecision (Approve/Deny/AskUser), checkpointer, tool registry and examples.
- Closure path: User/developer config → bounded agent operation; no ultimate mission/policy question → legitimate S5 decision → identity/charter enforcement returned to subsequent organizational actors.
- Why this is / is not agent-owned: A human editing a tool request, setting task goals or changing a config knob is not a first-party S5 parent-governed mode. There is no preserved global decision mandate, identity-level dispute route or returned policy for an autonomous organization.
- Evidence: [`cubeloop/agent/agent.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/agent/agent.py); [`cubeloop/hitl/middleware.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/hitl/middleware.py); [`cubeloop/hitl/channel.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/hitl/channel.py); [`cubeloop/session/session.py`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/cubeloop/session/session.py); [`README.md`](https://github.com/cubeplexai/cubeloop/blob/eb798f9a20c1f516d6a59a991a63a9d4c630f4bf/README.md).
- Basis: Bounded absence across published host-configuration and HITL modes.
- Confidence: High.
- Caveats: Organizational governance of CubePlex product customers can provide S5 outside this Index review boundary; cannot borrow it into CubeLoop.

### Absence scope

- Surfaces inspected: Agent config/system prompt, approval/HITL middleware, session consent/input interfaces, provider and tool settings, external application boundary.
- Plausible first-party paths checked: Tool permission edits, host-set agent identity, per-call user consent and external CubePlex product governance as policy/identity possibilities.
- Why no material first-party path remains: No first-party charter-level decision owner and return from a legitimate parent into subsequent organizational identity/purpose; only existing config and task action admission operate here.


## Recursion

A CubeLoop Agent runs an agentic S1 for a caller goal, potentially creating ephemeral subagents as task workers. A stable multi-S1 organization at a higher recursion is not inherent in those delegates, and `Agent`, `ExecutionSession`, `GoalMiddleware` and `Tracer` cannot be credited with a different function solely because they are named 'agent', 'session', 'goal' or 'trace'. Genuine downstream multi-agent organizations could have S2/S3/S4/S5 roles if their own decisions and return paths were assessed separately.

## Variety and escalation

Run-model uncertainty and new tool results are absorbed by the model/tool loop. A model may hand off a finite task to an ephemeral child; the main loop may process pending user steer/follow-up instructions; a goal evaluator may send a current-task continuation reason. Tool admission can trigger a human yes/no/edit response or timeout. Provider fallback switches among configured models. None of these proves a distinct algedonic signal or independent metasystem; ordinary operational exceptions remain in the task loop or host channels.

## Evidence gaps

- Published source supports real model/provider integration, but this assessment does not assert external model availability, end-to-end task quality, benchmark performance or multi-provider empirical superiority.
- Optional subagent/goal evaluator/HITL modes are first-party, but their mere availability does not establish an always-on or independently viable departmental organization.
- The goal evaluator observes conversation context, not independently sourced operating-reality measurements; proving a different audit mode would need a separate deployed mandate, direct evidence and corrective return to a demonstrated S3 owner.
- Source-only review cannot infer the embedding application’s business management or strategic policy, and its future features are outside this frozen ref.

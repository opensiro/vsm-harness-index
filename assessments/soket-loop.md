---
harness_id: soket-loop
project_name: Soket Loop
repository: https://github.com/soketlabs/loop
review_ref: cb4a0c1de4a495236958d2da5845f3b976e522e8
reviewed_at: 2026-10-18
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Soket Loop

## Review boundary

- System in focus: The shipped Rust `loop-agent` model/tool execution application and its feature-enabled `loop-orchestration` task-graph workflow mode, as reachable through `AgentHarness` and the CLI/application integration. The recursion is **one user's task/workflow operating system**, not the vendor's OSS development team, several unrelated user installations or a parent business organization.
- Purpose and identity: Execute user tasks by iteratively using model-selected tools, steering, sessions, optional sandbox, skills/MCP and, where enabled, model-planned workflows whose delegated agent turns and shell workers are dispatched through first-party scheduling and tracked to completion/failure.
- Relevant environment: Current user requests, model tool calls, observed tool results/errors, filesystem/service state, queued steering and follow-up messages, workflow DAG dependencies, worker concurrency, task outcomes, cancellation, memory changes and session history.
- Standard-distribution boundary: The pinned repository's crates `loop-agent`, `loop-orchestration`, model abstraction `loop-ai`, CLI/app-core runtime glue, shipped session/compaction/tool/sandbox/hooks, and feature-gated planner/worker/scheduler. LLM API models, user-created custom hooks/skills, separate remote agents/ACP service implementations and human institution authority are adjacent, not first-party organizational owners.
- Credited operating / distribution surfaces: [crates/loop-agent/src/agent_loop.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-agent/src/agent_loop.rs#L77), [crates/loop-agent/src/agent_loop.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-agent/src/agent_loop.rs#L209), [crates/loop-agent/src/agent_loop.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-agent/src/agent_loop.rs#L564), [crates/loop-agent/src/harness/agent_harness.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-agent/src/harness/agent_harness.rs#L142), [crates/loop-agent/src/harness/agent_harness.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-agent/src/harness/agent_harness.rs#L1022), [crates/loop-agent/src/harness/agent_harness.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-agent/src/harness/agent_harness.rs#L1076), [crates/loop-agent/src/harness/agent_harness.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-agent/src/harness/agent_harness.rs#L1145), [crates/loop-agent/src/harness/agent_harness.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-agent/src/harness/agent_harness.rs#L1296), [crates/loop-agent/src/harness/agent_harness.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-agent/src/harness/agent_harness.rs#L1488), [crates/loop-orchestration/src/planner/llm_planner.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-orchestration/src/planner/llm_planner.rs#L17), [crates/loop-orchestration/src/scheduler/mod.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-orchestration/src/scheduler/mod.rs#L61), [crates/loop-orchestration/src/scheduler/mod.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-orchestration/src/scheduler/mod.rs#L99), [crates/loop-orchestration/src/workflow/engine.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-orchestration/src/workflow/engine.rs#L58), [crates/loop-agent/src/harness/orchestration/agent_worker.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-agent/src/harness/orchestration/agent_worker.rs#L67), [crates/loop-agent/src/harness/orchestration/tools.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-agent/src/harness/orchestration/tools.rs#L395).
- Adjacent first-party surfaces excluded from ownership: GitHub CI, developer issue/PR decisions, update/install channel, provider intelligence, bundled user customizations that could be written via hooks, orchestration demo/tests and agent protocol adapters lacking independently shown application paths. Shared workflow event log does not become an independent institutional audit solely by being persisted.
- First-party operating / deployment modes considered: Ordinary model/tool `AgentHarness.prompt`, model streaming, sequential/parallel tool calls and returned observations; session/compaction/sandbox/hook modes; opt-in feature `orchestration` workflow execution and `start_workflow_from_goal` with `LlmPlanner`, task graph, worker pool, shared memory bus and scheduler; developer-provided manually authored DAG. Autonomous S1 established in model-enabled supported modes, not bare deterministic/manual DAG alone.
- Recursion level: A configured individual agent/workflow instance with agent-turn workers doing current user work. Task-graph branches are portions of the current job, not by default independently viable persistent S1 divisions of an overarching organization.
- Reviewed revision: `cb4a0c1de4a495236958d2da5845f3b976e522e8`, frozen by candidate intake [#1691](https://github.com/opensiro/vsm-harness-index/issues/1691) and batch [#1692](https://github.com/opensiro/vsm-harness-index/issues/1692).
- Observation date: 2026-10-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

`AgentHarness` holds session state, configured models, registered tools, sandbox, pending writes, queued steering/follow-ups, cancellations and before/after tool hooks. `prompt` uses `run_turn_inner` to construct `AgentLoopConfig` and `AgentContext` from the selected model, tools and current conversation, then calls the **shipped** `run_agent_loop`. In `agent_loop` a model streamed response can contain actual tool calls; the first-party runner executes them, appends their results to subsequent context and continues the model turn until completion/abort. Tool callbacks and session stores provide observable execution and feedback, not merely a static API wrapper. [crates/loop-agent/src/harness/agent_harness.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-agent/src/harness/agent_harness.rs#L98), [crates/loop-agent/src/harness/agent_harness.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-agent/src/harness/agent_harness.rs#L1076), [crates/loop-agent/src/harness/agent_harness.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-agent/src/harness/agent_harness.rs#L1145), [crates/loop-agent/src/harness/agent_harness.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-agent/src/harness/agent_harness.rs#L1220), [crates/loop-agent/src/agent_loop.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-agent/src/agent_loop.rs#L209), [crates/loop-agent/src/agent_loop.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-agent/src/agent_loop.rs#L280), [crates/loop-agent/src/agent_loop.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-agent/src/agent_loop.rs#L564), [crates/loop-agent/src/agent_loop.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-agent/src/agent_loop.rs#L685).

`AgentHarness.start_workflow` is reachable in the explicit `orchestration` feature mode. It builds `WorkflowEngine`, `Scheduler`, `WorkerPool`, a shared memory bus, `AgentWorker` and `ShellWorker`, subscribes real workflow events, and returns a `WorkflowResult`. `start_workflow_from_goal` composes a first-party `LlmPlanner` to turn user goals into task-graph nodes and invokes that engine. The scheduler checks DAG readiness, waits for dependent results, limits in-flight tasks via worker-pool permits, invokes agent-turn or shell workers, observes completion/failure and can stop on fail-fast/cancel. These are real current **task/workflow operating** functions, including concurrent subtasks. [crates/loop-agent/src/harness/agent_harness.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-agent/src/harness/agent_harness.rs#L1296), [crates/loop-agent/src/harness/agent_harness.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-agent/src/harness/agent_harness.rs#L1315), [crates/loop-agent/src/harness/agent_harness.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-agent/src/harness/agent_harness.rs#L1405), [crates/loop-agent/src/harness/agent_harness.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-agent/src/harness/agent_harness.rs#L1488), [crates/loop-orchestration/src/planner/llm_planner.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-orchestration/src/planner/llm_planner.rs#L17), [crates/loop-orchestration/src/scheduler/mod.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-orchestration/src/scheduler/mod.rs#L99), [crates/loop-orchestration/src/scheduler/mod.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-orchestration/src/scheduler/mod.rs#L228), [crates/loop-orchestration/src/scheduler/pool.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-orchestration/src/scheduler/pool.rs#L11), [crates/loop-orchestration/src/workflow/engine.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-orchestration/src/workflow/engine.rs#L58), [crates/loop-agent/src/harness/orchestration/agent_worker.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-agent/src/harness/orchestration/agent_worker.rs#L67).

SharedMemory records writer, timestamps and incrementing versions, and publishes changed-key notifications via MemoryBus. This permits tasks to read/write shared workflow state, but the inspected `set_entry` path performs a straightforward overwrite and notification: version counters **do not** evidence a separate arbitration process that senses harmful conflicts between independently viable operating systems and issues reciprocal corrective decisions. Likewise model-planned DAG structure is current-goal decomposition rather than final organizational resource governance or future-viability strategy. [crates/loop-orchestration/src/memory/shared.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-orchestration/src/memory/shared.rs#L25), [crates/loop-orchestration/src/memory/shared.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-orchestration/src/memory/shared.rs#L51), [crates/loop-orchestration/src/memory/shared.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-orchestration/src/memory/shared.rs#L85), [crates/loop-orchestration/src/memory/bus.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-orchestration/src/memory/bus.rs#L1), [crates/loop-orchestration/src/planner/llm_planner.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-orchestration/src/planner/llm_planner.rs#L1), [crates/loop-orchestration/src/planner/task_graph.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-orchestration/src/planner/task_graph.rs#L1).

## Operational model

User prompts or an explicitly selected goal enter a first-party agent task runtime. The model chooses actions and receives real execution results for its subsequent decisions; optional workflow mode organizes agent-turn workers, carries dependent artifacts/results and yields a final workflow outcome. Technical enforcement includes sandbox and tool hooks, concurrency permits, cancellation, shared memory and session checkpoint/history. Assessment credits the autonomous **current work loop (S1)** while independently testing plausible system-wide coordination, management, audit, strategy and identity/purpose rights instead of transferring them from task tools, worker role labels or external providers.

## S1 — Operations

- State: A
- Function: Autonomously conduct user tasks with model-selected tool actions and result-informed continuation in the first-party AgentHarness and enabled agent-workflow modes.
- Disturbance / variety regulated: Changing requests, nontrivial code/shell/web/file effects, tool failures, new model outputs, workflow dependency results, user steering and task-specific continuation.
- Decisive decision or feedback right: The configured model selects registered tool calls, consumes actual tool-result messages and chooses whether/how to act next. In workflow mode a first-party model planner can also select a task graph and each `AgentWorker` operates as a task agent.
- Decision owner: Model-backed task agent via shipped `run_agent_loop`; optional `LlmPlanner`/agent worker for task decomposition, under user-set task/sandbox/permission limits. External model providers deliver inference without donating unrelated organizational functions.
- Supporting / enforcement mechanisms: AgentHarness tool registry, stream_fn, executable tool handlers, session persistence, parallel/sequential tool scheduler, worker pool, task graph, hooks and sandbox.
- Closure path: User request → first-party AgentHarness model/context → streamed model action/tool call → first-party tool execution → real tool result appended to context → subsequent model action/response; optionally LLM goal plan → workflow tasks/agent workers → observed results → completion.
- Boundary reachability: The public shipped `AgentHarness.prompt`/`run_turn_inner` path invokes `run_agent_loop` with installed tools, and `start_workflow_from_goal` constructs a real `LlmPlanner` and dispatches first-party workflow tasks behind a feature-gate. Ordinary production code, not test-only simulation, closes the tool/observation loop.
- Why this is / is not agent-owned: Autonomous model selection of subsequent tool actions informed by actual returned results is a decisive current operational feedback right. Queue, semaphore, logger and policy guard are implementation/enforcement, not alternative owners.
- Evidence: [crates/loop-agent/src/harness/agent_harness.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-agent/src/harness/agent_harness.rs#L1022); [crates/loop-agent/src/harness/agent_harness.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-agent/src/harness/agent_harness.rs#L1076); [crates/loop-agent/src/harness/agent_harness.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-agent/src/harness/agent_harness.rs#L1145); [crates/loop-agent/src/harness/agent_harness.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-agent/src/harness/agent_harness.rs#L1220); [crates/loop-agent/src/agent_loop.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-agent/src/agent_loop.rs#L209); [crates/loop-agent/src/agent_loop.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-agent/src/agent_loop.rs#L280); [crates/loop-agent/src/agent_loop.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-agent/src/agent_loop.rs#L564); [crates/loop-agent/src/harness/agent_harness.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-agent/src/harness/agent_harness.rs#L1488).
- Basis: Static source-wired and production-reachable model→tool→observation→next-decision path.
- Confidence: High structural; no live external model/cloud execution tested.
- Caveats: A manually authored workflow graph without model-backed agent tasks is not itself autonomous S1; positive applies to standard model-selected task execution and supported optional agent workers.

## S2 — Coordination

- State: —
- Function: No independently governed inter-viable-S1 interference regulation loop is established at the individual workflow recursion.
- Disturbance / variety regulated: Parallel task branches and shared memory writes may contend, but reviewed concurrency guards and DAG prerequisites only schedule/serialize current task work.
- Decisive decision or feedback right: Semaphore permits, ready/dependent node selection, memory version+notification and worker selection enforce one configured job's execution, without deciding a specific reciprocal corrective measure from sensed interference between independently viable S1 organizations.
- Decision owner: Deterministic `Scheduler`/WorkerPool, memory writer, workflow graph or user's configuration; no distinct S2 disturbance owner in the supported running path.
- Supporting / enforcement mechanisms: WorkerPool permits, TaskGraph ready_tasks, shared memory bus and version counter, fail-fast, per-task retries, event log and cancellation.
- Closure path: Configured DAG → runnable nodes → workers/result join → next task. Missing observed cross-S1 interference → source-owned arbitration/attenuation judgment → feedback adjusting the separate viable units.
- Why this is / is not agent-owned: A model planning the task DAG supplies task decomposition; version increment and generic communication cannot be credited as autonomous S2 conflict regulation.
- Evidence: [crates/loop-orchestration/src/scheduler/mod.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-orchestration/src/scheduler/mod.rs#L99); [crates/loop-orchestration/src/scheduler/mod.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-orchestration/src/scheduler/mod.rs#L228); [crates/loop-orchestration/src/scheduler/pool.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-orchestration/src/scheduler/pool.rs#L46); [crates/loop-orchestration/src/memory/shared.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-orchestration/src/memory/shared.rs#L51); [crates/loop-orchestration/src/memory/bus.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-orchestration/src/memory/bus.rs#L1); [crates/loop-orchestration/src/planner/task_graph.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-orchestration/src/planner/task_graph.rs#L1).
- Basis: Bounded negative testing all plausible first-party workflow coordination modes.
- Confidence: Medium-high.
- Caveats: An adopter could build S2-specific conflict logic atop memory events; it is not an evidenced first-party supported relation with reciprocal return.

### Absence scope

- Surfaces inspected: TaskGraph dependencies, LlmPlanner, Scheduler run/execute_task, WorkerPool permits, shared MemoryBus and versioned writes, tool parallel/sequential modes and workflow event signals.
- Plausible first-party paths checked: Parallel worker interference, resource contention, optimistic conflict detection, task ownership collisions, shared memory overwrite, dynamic arbitration and cross-task messaging.
- Why no material first-party path remains: These code paths dispatch/synchronize dependent subtasks and notify data writes; none senses a concrete disturbance between distinct independently viable S1s and selects corrective reciprocal behavior for them.

## S3 — Inside-and-now control

- State: —
- Function: No source-closed whole-current manager allocates obligations, priorities and scarce resources among independently viable operating divisions.
- Disturbance / variety regulated: Current workflow task failure, dependency blockage and worker capacity; there is no evidenced organization-wide ongoing multi-division portfolio of commitments.
- Decisive decision or feedback right: `LlmPlanner` decomposes a current user goal; `Scheduler` executes its DAG under fixed concurrency/fail-fast; user config chooses model, permission and task. No legitimate cross-unit current management override or resource/commitment reconciliation loop.
- Decision owner: Current task agent/plan, deterministic scheduler, and external user for system settings, not a separate whole-current S3 decision actor.
- Supporting / enforcement mechanisms: Workflow status tracking, snapshots, task plan, worker pool, event log, error/retry, memory bus, GUI/CLI status and abort.
- Closure path: Per-job DAG execution returns completed/failed workflow status. Missing whole-system current obligations report → global decision balancing resources/priorities/commitments → binding intervention returned to distinct S1 units.
- Why this is / is not agent-owned: The word `orchestration` and model-selected task planning do not establish organizational S3 if the decisive relation remains scoped to one user's current job.
- Evidence: [crates/loop-agent/src/harness/agent_harness.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-agent/src/harness/agent_harness.rs#L1296); [crates/loop-agent/src/harness/agent_harness.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-agent/src/harness/agent_harness.rs#L1488); [crates/loop-orchestration/src/planner/llm_planner.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-orchestration/src/planner/llm_planner.rs#L17); [crates/loop-orchestration/src/scheduler/mod.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-orchestration/src/scheduler/mod.rs#L99); [crates/loop-orchestration/src/scheduler/mod.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-orchestration/src/scheduler/mod.rs#L228); [crates/loop-orchestration/src/workflow/engine.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-orchestration/src/workflow/engine.rs#L228).
- Basis: Bounded negative after review of strongest management-like planner/scheduler/worker controls.
- Confidence: Medium-high within declared application recursion.
- Caveats: Multiple unrelated Loop deployments and their human operators could form a real organization's S3, external to this assessed source.

### Absence scope

- Surfaces inspected: Workflow scheduler and task statuses, LlmPlanner, agent-worker delegation, CLI configuration, session state, worker pool, shared memory, stop/cancel.
- Plausible first-party paths checked: Topological planning as S3 authority, model-selected cross-task priority, fail-fast and global cancel as holistic control, worker capacity allocation, task graph as organizational operating portfolio.
- Why no material first-party path remains: All exercised decisions concern one current workflow/request and fixed resource limits; no actor receives a whole multi-unit current view and returns legitimate binding cross-unit operational commitments.

## S3* — Complementary audit

- State: —
- Function: No independently sourced complementary reality-audit actor challenges management reports and makes authorized S3 correction return.
- Disturbance / variety regulated: Tools, worker subprocesses and workflows can fail, and events/logs may reveal failure; task error handling is local quality/recovery rather than an independent audit of organizational management assertions.
- Decisive decision or feedback right: WorkflowEngine logs task start/completion/failure; tool hooks can veto/update user action; session history records model/tool turns. None is a shipped independent challenger to a whole-current S3 based on separately obtained external operational facts.
- Decision owner: Agent task runner, deterministic event log, optional adopter-supplied custom hooks; no separate independent S3* decision holder with management correction rights.
- Supporting / enforcement mechanisms: Workflow event log, tool before/after hooks, result/error propagation, session fork/history, task artifacts, sandbox tool checks.
- Closure path: Task observation/error → local retries/fail-fast/abort or tool hook → workflow outcome. Missing independently obtained whole-organization facts → adverse S3 challenge → binding S3 corrective intervention.
- Why this is / is not agent-owned: A separate callback or telemetry stream can observe tasks but observation/logging alone is not corrective complementary management audit, and plugin-author governance cannot be assumed first-party.
- Evidence: [crates/loop-orchestration/src/workflow/engine.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-orchestration/src/workflow/engine.rs#L87); [crates/loop-orchestration/src/workflow/engine.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-orchestration/src/workflow/engine.rs#L105); [crates/loop-orchestration/src/workflow/engine.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-orchestration/src/workflow/engine.rs#L124); [crates/loop-agent/src/harness/hooks.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-agent/src/harness/hooks.rs#L1); [crates/loop-agent/src/harness/agent_harness.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-agent/src/harness/agent_harness.rs#L589); [crates/loop-agent/src/harness/agent_harness.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-agent/src/harness/agent_harness.rs#L599); [crates/loop-orchestration/src/scheduler/mod.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-orchestration/src/scheduler/mod.rs#L99).
- Basis: Bounded negative after testing event/audit/hooks/recovery candidates, excluding user-composed review authority.
- Confidence: Medium-high.
- Caveats: A custom plugin could independently inspect outputs, but no shipped function-specific owner/decision/return is established by the hooks API itself.

### Absence scope

- Surfaces inspected: Workflow event log and status, on/subscribe events, before/after tool hooks, tool-result errors, session history and sandbox controls.
- Plausible first-party paths checked: Independent verifier via hook, telemetry as contradictory direct evidence, task retries/failure report causing managerial correction, durable log used for audit.
- Why no material first-party path remains: All source-proven return paths are local task/error/hook consequences; there is no S3 management claim, independently sourced audit judgment and authoritative corrected current-control return.

## S4 — Outside-and-then intelligence

- State: —
- Function: No shipped agent-owned or parent-closed prospective strategy capability selection and adoption loop was established.
- Disturbance / variety regulated: New tasks, changed models/tool configurations and evolving project needs; ordinary session memory/compaction, skill and tool extensibility are not by themselves future viability intelligence.
- Decisive decision or feedback right: LlmPlanner turns a **present user goal** into current task graph; active skills and configuration are selected by user/developer, session compaction summarizes previous chat for current context; no installed prospective environment-scanning option selection and durable accepted capability/topology redesign actor.
- Decision owner: Current task model, external user/developer controlling configurations/skills, deterministic session compactor and model selection; no independently mandated strategic agent or legitimate parent S4.
- Supporting / enforcement mechanisms: Compaction, session history, skill activation and resources, hooks/extensions, current-workflow planner and memory bus.
- Closure path: New request/history → context/plan/tool operations. Missing outside/future environmental differentiation → multiple viable adaptation options → authorized strategic choice/admission → changed lasting operating capacity returned into subsequent present work.
- Why this is / is not agent-owned: Chat-history condensation and task re-planning improve ongoing operational context; no explicit lasting future capability redesign is accepted through a source-owned S4 path.
- Evidence: [crates/loop-agent/src/harness/agent_harness.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-agent/src/harness/agent_harness.rs#L734); [crates/loop-agent/src/harness/agent_harness.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-agent/src/harness/agent_harness.rs#L809); [crates/loop-agent/src/harness/agent_harness.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-agent/src/harness/agent_harness.rs#L543); [crates/loop-agent/src/harness/agent_harness.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-agent/src/harness/agent_harness.rs#L1488); [crates/loop-agent/src/harness/compaction/mod.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-agent/src/harness/compaction/mod.rs#L1); [crates/loop-orchestration/src/memory/shared.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-orchestration/src/memory/shared.rs#L51).
- Basis: Source-bounded negative distinguishing ordinary memory/planning from future viability selection.
- Confidence: Medium-high for shipped stock modes.
- Caveats: User-supplied skills and optional plugins could implement adaptation, but their imagined behaviors are not first-party supported S4 ownership.

### Absence scope

- Surfaces inspected: Compaction, skill activation, prompt templates, dynamic tool/model selection, sessions, workflow LlmPlanner and persistent memory primitives.
- Plausible first-party paths checked: Adaptive future strategy generation, autonomous skill promotion, model self-configuration, retrospective improvement loops and adoption of new organizational capability.
- Why no material first-party path remains: The inspected first-party decisions select or remember current task context and execute predetermined rules; they do not identify and adopt prospective capability strategy with returned lasting redesign.

## S5 — Policy and identity

- State: —
- Function: No terminal legitimate purpose or identity arbiter is wired into the stock Loop task-runtime boundary.
- Disturbance / variety regulated: Tool/sandbox policies, user model choice, allowed skills, project prompts and cancellation constrain operations but do not decide system-wide mission or governing identity.
- Decisive decision or feedback right: Human configuration and security gates choose allowed tools/model/sandbox; tool hooks and execution environment enforce configured limits. No purpose-level contested values/identity judgment returning to all operations.
- Decision owner: External user/developer and deterministic permission/sandbox guards, not a first-party ultimate policy/mission owner.
- Supporting / enforcement mechanisms: SandboxMode and tool env, before/after tool callbacks, tool registry and active tools, system prompt/configuration and CLI settings.
- Closure path: User constraints → allow/block current model/tool action. Missing legitimate mission question → authoritative identity/purpose decision → changed governing mandate and return to operating organization.
- Why this is / is not agent-owned: Authorization for file/shell operations and model selection is narrower than ultimate legitimate purpose/organizational identity control.
- Evidence: [crates/loop-agent/src/harness/agent_harness.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-agent/src/harness/agent_harness.rs#L338); [crates/loop-agent/src/harness/agent_harness.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-agent/src/harness/agent_harness.rs#L426); [crates/loop-agent/src/harness/agent_harness.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-agent/src/harness/agent_harness.rs#L441); [crates/loop-agent/src/harness/agent_harness.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-agent/src/harness/agent_harness.rs#L589); [crates/loop-agent/src/harness/agent_harness.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-agent/src/harness/agent_harness.rs#L1145); [crates/loop-agent/src/harness/sandbox/mod.rs](https://github.com/soketlabs/loop/blob/cb4a0c1de4a495236958d2da5845f3b976e522e8/crates/loop-agent/src/harness/sandbox/mod.rs#L1).
- Basis: Bounded negative after testing security, user parent-mode and prompt/permission decisions.
- Confidence: Medium-high.
- Caveats: An adopter institution could exercise S5 for its own deployment, without that authority being source-wired to the first-party single-workflow recursion.

### Absence scope

- Surfaces inspected: Sandbox/permissions, tool hook approvals, project/system prompts, user model/skills configuration, external account identity and CLI settings.
- Plausible first-party paths checked: User approval of risky task action as S5, model prompt as system mission, policy tool denies as binding identity governance, human configuration as parent closure.
- Why no material first-party path remains: These gates constrain tool/runtime behavior but supply no first-party legitimate ultimate mission/identity decision and return for an independently viable higher-recursion organization.


## Distributed OSS parent arrangement

The Soket Labs repository maintainer/community, external model providers, users, local tasks/agent workers and optional external ACP/MCP services are separate owners. The publication concerns one installed runtime and one current workflow recursion. No evidence supplies a standing distributed parent with S3, S4 or S5 mandate/return. A human adjusting settings or issuing a prompt is not a proven `P` ownership mode for those functions.

## Self-hosted and non-human modes

The first-party Rust binaries/crates can run with configured cloud or local model providers. Production `AgentHarness` and the optional `orchestration` feature invoke operational model/tool loops, worker graphs and shared memory; unsupported extensions or model provider internal behavior are not credited. Source was inspected at pinned revision; no real model/API or cluster workflow execution was performed in this review.

## Recursion

A workflow may dispatch concurrent agent workers with their own S1 current-task decisions and pass artifacts through graph dependencies and shared memory. They remain subtasks of one user-request/workflow unless separately evidenced as independently viable S1 business divisions. Neither worker count nor word `scheduler` establishes higher-level S2/S3/S3*/S4/S5 closure by default.

## Variety and escalation

The model/task loop reacts to tool results and steering; the scheduler regulates capacity and dependencies; error/timeout/cancel and sandbox guard unsafe actions; session history/compaction controls prompt size. These technical controls bound variety without separately allocating organization-wide commitments or verifying management assertions. Hooks can be independently composed by future adopters but hypothetical handler authority is not counted.

## Evidence gaps

- `S1=A` is limited to model-backed operating modes; model provider reasoning is external and not a donated organizational metasystem. No provider-backed live execution/benchmark was performed.
- The enabled orchestration mode genuinely exists as compiled first-party engine wiring, not just a package name. Parallel DAG, shared memory with versioned writes and notification, and task workers are nevertheless current request coordination. No verified shipped interference-sensitive reciprocal feedback among independent S1 operating units was found.
- Neither `LlmPlanner` nor `WorkflowEngine` makes whole-current organization commitments; neither tool telemetry nor custom hooks supplies independent complementary S3* correction, without added actual actor/authority.
- No source-wired prospective option choice and durable capability promotion or S5 final mission decision was established from compaction, skill activation, tool hooks or user settings. External institutional governance not imported.
- The conclusion is a bounded source-first mapping under released Profile 0.2.4 and Methodology 0.3.7; no complete upstream Rust test suite or hosted provider run, and no product performance/safety effectiveness, is claimed.

---
harness_id: agentflow
project_name: AgentFlow
repository: https://github.com/agentenv/agentflow
review_ref: eb51a2e7a5c7d65da5718c4a41843098b60c80e0
reviewed_at: 2026-10-19
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: A
autonomy_s5: —
---

# AgentFlow

## Review boundary

- System in focus: The shipped first-party **AgentFlow model-backed multi-actor task-graph operating harness** (user-authored PipelineSpec/Graph, runnable Codex/Claude/Kimi/Pi CLI agent nodes, first-party preparation/runner/result feedback, bounded orchestration), plus the separately **opt-in** graph-optimization session that adapts a pipeline between execution rounds. This is one task-graph operating organization with node workers executing related subtasks, not a presumption that each coding-agent node is an independent viable business division.
- Purpose and identity: Compile and execute a dependency graph of AI coding-agent tasks with bounded parallelism, conditional retries/reviews, actor tool grants, result transfer and auditable run state; optionally revise the graph itself based on completed-run evidence to improve a later run.
- Relevant environment: New task prompts and workspace/tool states, model/CLI agent outputs, runtime failures, dependent-node results, provider/executor availability, stale outputs, sequential and parallel worker variety, execution cost/time, trace evidence, invalid or stale graph revisions.
- First-party standard distribution: `agentflow/dsl.py`, `specs.py`, `context.py`, `orchestrator.py`, `agents/{codex,claude,kimi,pi}.py`, `agents/registry.py`, `runners/{local,docker,ssh,ec2,ecs}.py`, `store.py`, `traces.py`, `success.py`, `graph_optimizer.py`, `tuned_agents.py`, `graph_optimizer`-triggered pipeline round loop and `cli.py`.
- Credited operating / distribution surfaces: [README.md#L1](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/README.md#L1), [README.md#L30](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/README.md#L30), [agentflow/orchestrator.py#L94](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/orchestrator.py#L94), [agentflow/orchestrator.py#L354](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/orchestrator.py#L354), [agentflow/orchestrator.py#L478](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/orchestrator.py#L478), [agentflow/orchestrator.py#L609](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/orchestrator.py#L609), [agentflow/orchestrator.py#L962](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/orchestrator.py#L962), [agentflow/orchestrator.py#L1258](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/orchestrator.py#L1258), [agentflow/agents/codex.py#L13](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/agents/codex.py#L13), [agentflow/agents/pi.py#L17](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/agents/pi.py#L17), [agentflow/runners/local.py#L17](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/runners/local.py#L17).
- Adjacent first-party surfaces excluded from ownership: CI/test-only stub agents and mocks, benchmarks/demonstration data and developer-defined graph content, user-written prompt business roles or higher-level organizational mission, original standalone Codex/Claude/Kimi/Pi CLI internals and inference providers, remote EC2/ECS/Docker/SSH administrator authorities, research/training claims and unrelated tasks/other agent services not composed into a documented AgentFlow pipeline.
- Supported operating / deployment modes considered: CLI/DAG run with actor nodes and dependency context; user-configured `codex`, `claude`, `kimi`, `pi` agents and local/cloud/container runners; concurrent fanout and merge; `on_failure` feedback loop, per-node failure/success checks, bounded retry, structured node trace storage; optional `periodic` model-powered cancellation/rerun of watched nodes; **opt-in** `optimizer` with `n_run > 1` graph adaptation between rounds; noninteractive execution preflights and explicit credential/sandbox options.
- Recursion: A single operator-commissioned program of graph-linked model-agent subtasks and their shared task-state, not a durable federation of independently viable S1 lines of business. The operating model-selected answer/tool work of packaged actor nodes belongs to S1 in the shipped composed mode, while optional model-suggested redesign of the **future graph** provides bounded prospective S4; static DAG scheduling and validation are infrastructure, not automatically S2/S3.
- Frozen source identity: Public GitHub repository ID **1175650975**, MIT root LICENSE, default branch **master**, frozen `eb51a2e7a5c7d65da5718c4a41843098b60c80e0`, Git tree `9b121d7a218be06a97321333635bdd72e7aad540`; [batch #1747](https://github.com/opensiro/vsm-harness-index/issues/1747). Review date 2026-10-19; Profile 0.2.4 / Skills Methodology 0.3.7.

## Repository architecture

A `Graph`/`PipelineSpec` built via shipped DSL or JSON declares a task decomposition, typed `NodeSpec` actor, user-selected model/tool grants, prompt templates, dependencies, retry/failure criteria and runner. `Orchestrator.submit` initializes a persisted run; its `run` finds ready DAG nodes, renders dependency results as prompt context, chooses an `AgentAdapter` and runner, prepares and executes real model-agent CLI commands, parses their output and records successes/failures/traces for dependent nodes. `CodexAdapter.prepare` constructs `codex exec --json` with explicit model/sandbox/tool configuration and context; `PiAdapter.prepare` constructs `pi --print --mode json` with model/tools/extensions/providers. These are first-party supported integrations into external model-backed **agent decision loops**, not a first-party implementation of the Codex or Claude model internals. With an installed configured CLI the actor decides task-specific action/tool outputs; a pure `Shell` or mocked actor is not counted as autonomous model cognition. [agentflow/dsl.py#L1](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/dsl.py#L1); [agentflow/specs.py#L2332](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/specs.py#L2332); [agentflow/orchestrator.py#L609](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/orchestrator.py#L609); [agentflow/orchestrator.py#L962](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/orchestrator.py#L962); [agentflow/agents/codex.py#L120](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/agents/codex.py#L120); [agentflow/agents/pi.py#L17](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/agents/pi.py#L17); [agentflow/runners/local.py#L17](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/runners/local.py#L17).

The scheduler uses a user-defined directed task graph, ready-dependency tracking and bounded concurrency; fanout/merge nodes and `on_failure` edges express predeclared feedback and rerun patterns. Optional scheduled `periodic` nodes can issue actions such as cancel and rerun on watched task nodes, through a typed parsed model output and the current run state. These mechanisms may regulate simultaneous *task steps* and react to immediate errors; no independently viable S1 department interference relationship or executive mandate over an external portfolio is established by a program of jobs. [README.md#L51](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/README.md#L51); [agentflow/orchestrator.py#L844](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/orchestrator.py#L844); [agentflow/orchestrator.py#L890](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/orchestrator.py#L890); [agentflow/orchestrator.py#L1258](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/orchestrator.py#L1258); [agentflow/success.py#L1](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/success.py#L1).

A separately opt-in `PipelineSpec(optimizer='codex', n_run>1)` causes `Orchestrator.submit` to enter `_run_graph_optimization_session`. It runs the current graph, exports actual node outcomes and traces as a report, prompts a selected **model-backed CLI optimizer** to edit a concrete generated `pipeline.py`, loads and validates the resulting pipeline, then replaces/persists `current_pipeline` and launches it as the next child run. This is an actually connected future-graph adaptation, not just logs or a claimed abstract AI capability. The acceptance check is **schema/load validation**, not a held-out benefit score; the source README explicitly warns it cannot guarantee the new graph is better. The final in-memory parent run stores the evolved graph; persistence inside run artifacts is evidenced, but generic automatic promotion to external deployments and repeated future sessions is not. [README.md#L365](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/README.md#L365); [agentflow/orchestrator.py#L354](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/orchestrator.py#L354); [agentflow/orchestrator.py#L478](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/orchestrator.py#L478); [agentflow/orchestrator.py#L525](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/orchestrator.py#L525); [agentflow/orchestrator.py#L569](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/orchestrator.py#L569); [agentflow/specs.py#L2430](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/specs.py#L2430).

## Operational model

Current S1 execution is delegated from a first-party program/runner to configured provider-dependent model coding-agent loops; their results and tool traces feed dependent tasks and optional retry/review. Optional opt-in S4 uses completed-round observations to propose and adopt changed prospective *graph structure, prompts, dependencies and concurrency* for the next round. None of these mechanisms alone confers whole-enterprise or constitutional authority.

## S1 — Operations

- State: A
- Function: Select and execute novel task-specific coding/research actions within a graph node, using actual workspace/provider/tool feedback and returning an outcome to downstream subtasks.
- Disturbance / variety regulated: Different prompts and code/workspace states, external tool output and failures, dependency context, sequential retry inputs, varying model response and workflow outcomes.
- Decisive decision or feedback right: In the documented composed `codex`/`claude`/`kimi`/`pi` node mode, the configured model-backed CLI agent decides task-specific tools/actions and answer based on the rendered prompt and actual operating observations; first-party AgentFlow chooses node/runner and transports results, not the model's internal next action.
- Decision owner: Configured model agent via the first-party `NodeSpec` → `AgentAdapter` → `Runner` integration; underlying CLI/provider cognition is external, but the shipped operation actually reaches it from the public Graph and returns task feedback into the same pipeline.
- Supporting / enforcement mechanisms: DAG dependency resolver, agent adapter command builder, scoped provider and tool/sandbox options, local/Docker/SSH/EC2/ECS target, retry/failure graph, trace parser and persisted node results.
- Closure path: User task graph → ready node prompt with upstream observations → prepared model-backed CLI execution → model-selected actions/tools until CLI result → captured output and success/trace → next dependent node or configured retry/review loop; completed task graph has user-facing output.
- Boundary reachability: Public `Graph` DSL / `agentflow run` includes documented `codex()`, `claude()` and `pi()` nodes; `Orchestrator._execute_node` resolves and prepares their first-party adapter and runner, and records results used by downstream graph nodes. The substantive model decisions occur **within** the explicitly external CLI runtime as a supported first-party *composed mode*. No general claim about a standalone AgentFlow-native LLM inner tool loop is made.
- Why this is / is not agent-owned: Remove the configured model agent and graph scheduler still orders static commands but cannot produce task-specific reasoning/tool actions under unknown input. The first-party orchestration contributes a meaningful operational feedback envelope yet does not replace the external agent's cognition or own that provider's governance.
- Evidence: [README.md#L22](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/README.md#L22), [README.md#L45](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/README.md#L45), [agentflow/orchestrator.py#L962](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/orchestrator.py#L962), [agentflow/agents/codex.py#L120](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/agents/codex.py#L120), [agentflow/agents/pi.py#L17](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/agents/pi.py#L17), [agentflow/agents/registry.py#L1](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/agents/registry.py#L1), [agentflow/runners/local.py#L17](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/runners/local.py#L17).
- Basis: Source-connected, documented model-backed CLI task path; this is not a verified live provider task completion.
- Confidence: Medium-high for first-party integration to external model-backed action loop; remote provider and executable availability untested.
- Caveats: Shell-only nodes can be deterministic; they are not the basis of this positive. A user-supplied graph's domain or a separately owned Codex multi-agent metasystem cannot be borrowed as AgentFlow's organization.

## S2 — Coordination

- State: —
- Function: No source-backed distinct regulator of **mutual disturbances between independently viable S1 operating divisions** with binding coordinated adjustment to their own ongoing obligations is evidenced in this task-graph operating boundary.
- Disturbance / variety regulated: Parallel tasks may write overlapping code, fanout outputs may disagree, node dependencies may race, and periodic monitors may cancel/rerun failing nodes; these are coordination problems inside one operator-authored graph rather than demonstrated interference between independent sustainable operational departments.
- Decisive decision or feedback right: Caller defines DAG dependency/fanout structure, success conditions and periodic watcher; scheduler applies predeclared readiness, while optional periodic model chooses cancel/rerun on watched current graph nodes. No separate model/program identifies actual **inter-S1 departmental interference** and adjusts commitments of two viable units.
- Decision owner: Operator-authored graph and per-task actor/periodic monitor model, plus deterministic orchestration engine, not evidenced organizational S2 regulation.
- Supporting / enforcement mechanisms: DAG/fanout/merge, success criteria, per-node retries, `on_failure` return edges, periodic action schema and cancellation/runner limits.
- Closure path: Task outputs and run logs → existing graph or watcher issues scoped reruns/cancellations → same graph continues; no concrete inter-S1 independent-operation conflict → distinct S2 damping judgment → revised mutually coordinating operating rights.
- Why this is / is not agent-owned: A model choosing task reruns is a current program-level tactic; it does not acquire a separate viable-system coordination role by serving many temporary agent nodes.
- Evidence: [agentflow/orchestrator.py#L844](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/orchestrator.py#L844), [agentflow/orchestrator.py#L890](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/orchestrator.py#L890), [agentflow/orchestrator.py#L1258](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/orchestrator.py#L1258), [agentflow/dsl.py#L1](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/dsl.py#L1), [README.md#L47](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/README.md#L47).
- Basis: Bounded negative after examining both static DAG and live periodic action modes.
- Confidence: Medium-high for defined graph-task recursion.
- Caveats: A downstream application could compose an enduring multi-service organization with a genuinely empowered conflict regulator; not imported from generic graph semantics.

### Absence scope

- Surfaces inspected: Graph DSL dependencies, fanout/reduce, retry/success paths, periodic agent action schema and node cancellation, trace/result store.
- Plausible first-party paths checked: Concurrent writes, shared worktree contention, disagreement among separate agent outputs, periodic cancel/rerun feedback potentially protecting adjacent nodes.
- Why no material first-party path remains: Those mechanisms coordinate work items and fault recovery for one commissioned DAG; no independent viable S1 departments plus concrete interference-sensing/dampening with mutual operational adjustment and stable S2 ownership are evidenced.



## S3 — Inside-and-now control

- State: —
- Function: No autonomous whole-current portfolio executive that allocates discretionary present resources/priorities across independently viable S1 departments and returns binding adjustments is shown.
- Disturbance / variety regulated: Node overload, failure, delays, inference service availability and run cancellation can threaten a pipeline. Execution backpressure and periodic reruns manage this particular workflow rather than current enterprise-level viable-unit obligations.
- Decisive decision or feedback right: Operator chooses graph `concurrency`, `max_iterations`, `fail_fast`, tool grants, targets and cost exposure. Scheduler regulates active node queues; optional periodic model can command scoped cancel/rerun of watched nodes, not govern durable organization-level S1 budgets and obligations.
- Decision owner: Human/application config and deterministic first-party scheduler; periodic actor model for scoped run intervention, not demonstrated whole-current S3 managerial authority.
- Supporting / enforcement mechanisms: RunStore, semaphores, cancellation/rerun flags, dependency tracking, sandbox/credential controls, graph state machine, trace events, periodic action handling.
- Closure path: Node progress/errors → ready set/failure gate or optional periodic action → specific graph node rerun/cancel → current run continues/terminates; absent executive assessment/decision/return across a portfolio of independently viable operating units.
- Why this is / is not agent-owned: Strong task-program scheduling does not automatically possess a separate enterprise-management mandate over multiple S1 divisions.
- Evidence: [agentflow/orchestrator.py#L94](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/orchestrator.py#L94), [agentflow/orchestrator.py#L609](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/orchestrator.py#L609), [agentflow/orchestrator.py#L890](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/orchestrator.py#L890), [agentflow/orchestrator.py#L1258](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/orchestrator.py#L1258), [agentflow/specs.py#L2332](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/specs.py#L2332).
- Basis: Source-bounded negative including optional model-backed periodic current-control behavior.
- Confidence: Medium-high.
- Caveats: A higher application may delegate S3 decision rights via additional policies not shipped by AgentFlow at this recursion.

### Absence scope

- Surfaces inspected: Orchestrator state transitions, concurrency, fail-fast/cancel/rerun/periodic node controls, provider and runner quotas, RunStore.
- Plausible first-party paths checked: Portfolio resource renegotiation, monitored operating obligations, dynamic priorities among viable S1 lines, budget responses and actor supervision.
- Why no material first-party path remains: The present control path allocates and retries graph tasks under a caller-designed plan; no source-backed whole-current autonomous management and binding returned S1 operating adjustments across viable departments.



## S3* — Complementary audit

- State: —
- Function: No independent audit of **organizational S1/S3 operational reality** that sends corrective evidence to an actual S3 management owner and alters whole-current control is established.
- Disturbance / variety regulated: Wrong outputs, failed tests, incomplete node logs, missing artifacts and failed optimizer loading can undermine conclusions. Model review steps and success criteria give task-level acceptance/retry evidence but do not form a separately mandated audit of management claims.
- Decisive decision or feedback right: `evaluate_success` applies configured criteria to node output/artifacts, reviewers act as task-specific agent nodes, trace and graph reports store what happened. No separate first-party independent checker decides that an S3 managerial picture is wrong and mandates a corrective cross-operation response.
- Decision owner: User-configured success validators and task model reviewer, immutable run storage for data, not distinct operational reality auditor.
- Supporting / enforcement mechanisms: NodeAttempt/NodeResult receipts, trace parsing, success criteria, graph_optimizer `GRAPH_REPORT` evidence, validation/retry path and node report.
- Closure path: Task/node output → validator/reviewer/trace → task-level acceptance or graph retry; no independent complementary S3* inspection → managerial reality correction → S3 changes its current decisions.
- Why this is / is not agent-owned: A coding review or trace report can be useful audit **evidence**, but without an S3 owner and explicit corrective audit mandate it is not an autonomous S3* function.
- Evidence: [agentflow/success.py#L1](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/success.py#L1), [agentflow/traces.py#L1](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/traces.py#L1), [agentflow/orchestrator.py#L1100](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/orchestrator.py#L1100), [agentflow/graph_optimizer.py#L75](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/graph_optimizer.py#L75).
- Basis: Negative after inspecting first-party reviewers, validation and run traces, not just class names.
- Confidence: Medium-high.
- Caveats: An independent compliance inspector could be implemented by a downstream graph user but is not inherent in this distribution.

### Absence scope

- Surfaces inspected: RunStore, trace parsing, success criteria, review nodes, graph optimizer reports and schema validation.
- Plausible first-party paths checked: Operational self-report checking, held-out independently sampled organizational outcomes, S3 managerial picture correction and legitimacy of audit mandate.
- Why no material first-party path remains: Only task/result quality and optimization acceptance mechanisms are evidenced, with no separate first-party S3 operational management loop and corrective independent reality audit into it.



## S4 — Outside-and-then intelligence

- State: A
- Function: Use real task-graph outcomes and traces to form a prospective changed pipeline, accept a structurally valid design and run the revised structure in subsequent optimization rounds of a specifically enabled session.
- Disturbance / variety regulated: Shifting coding task difficulties, graph dependency bottlenecks, recurring node failures, inefficient concurrency, misunderstood prompts and performance/trace differences across rounds.
- External distinction: A completed child-run `RunRecord` and trace files reveal what each node attempted, output, failure, timing and status. `build_graph_report` exports this actual operational evidence to the optimizer prompt.
- Future / prospective distinction: The model-backed selected `optimizer` (Codex/Claude/Kimi/Pi) receives node outcomes/trace context **after** the graph run and is directed to revise `pipeline.py` for the **next** task-graph round, not just continue the failed current node.
- Adaptation option generated: The model changes pipeline node prompts, dependencies, ordering, graph composition and concurrency/fail-fast settings; future alternative graph design is an authored executable Python `PIPELINE` rather than an inert analysis paragraph.
- Path back into current capability / S3: `_run_graph_optimization_session` executes the selected model CLI, reloads the edited `pipeline.py` through `load_pipeline_from_path`, validates `PipelineSpec`, updates and persists `current_pipeline`, and passes it into the next `_create_queued_run`. This returns to **next S1 graph configuration and operations**, not to an independently evidenced S3 organizational executive. It is opt-in and bounded to the configured optimization session; validation is structural, not measured improvement.
- Decisive decision or feedback right: The selected model-backed optimizer chooses prospective graph content; first-party loader/schema and operator-defined settings gate acceptance, and the orchestration engine persists/executes accepted revision.
- Decision owner: Model-backed Codex/Claude/Kimi/Pi optimizer through first-party prompt/adapter/execution path, bounded by validation and `optimizer` plus `n_run>1` host opt-in; no first-party constitutional or general cross-organization authority claimed.
- Supporting / enforcement mechanisms: Graph reports, trace copy, editable pipeline artifact, optimizer prompt, `_run_optimizer` adapter, retry on invalid edits, schema verifier, persisted RunStore, next child graph run and `n_run` bound.
- Closure path: Current-round external task graph outcomes → trace/report → optimizer prospective graph edit → schema-valid newly loaded PipelineSpec → accepted updated `current_pipeline` stored → subsequent run of new graph → new outcome/feedback.
- Boundary reachability: `PipelineSpec` publicly exposes `optimizer` and `n_run`, `Orchestrator.submit` selects `_run_graph_optimization_session`; it invokes `_run_optimizer` backed by first-party CLI adapter, validates/persists revised graph, then launches a new child graph run. README documents this exact opt-in mode. `n_run=1` or no `optimizer` does not activate this S4 path.
- Why this is / is not agent-owned: Without the model-backed optimizer, scheduler, traces, schema gate and retry machinery cannot create purpose-sensitive new graph structure from observed execution failures. Conversely, without graph loader/runner, the model's suggestion would not be executed; the positive is the **integrated shipped composed mode** and not a claim of reliable measured improvement.
- Evidence: [README.md#L366](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/README.md#L366), [README.md#L375](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/README.md#L375), [agentflow/specs.py#L2332](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/specs.py#L2332), [agentflow/specs.py#L2430](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/specs.py#L2430), [agentflow/orchestrator.py#L354](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/orchestrator.py#L354), [agentflow/orchestrator.py#L428](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/orchestrator.py#L428), [agentflow/orchestrator.py#L478](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/orchestrator.py#L478), [agentflow/orchestrator.py#L499](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/orchestrator.py#L499), [agentflow/orchestrator.py#L539](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/orchestrator.py#L539), [agentflow/orchestrator.py#L569](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/orchestrator.py#L569), [agentflow/orchestrator.py#L609](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/orchestrator.py#L609), [agentflow/tuned_agents.py#L390](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/tuned_agents.py#L390).
- Basis: First-party source-linked model-option-to-future-run adoption; no provider-run or reward/quality uplift claims.
- Confidence: High for structural path, medium for runtime practical success without external CLI/provider.
- Caveats: Validation only establishes that new pipeline loads, not that revised actions improve result; the updated graph is scoped to that optimization session and saved run artifacts. No autonomous permanent update of all future user-created pipelines is evidenced.

## S5 — Policy and identity

- State: —
- Function: No first-party legitimate decision owner of ultimate organizational identity/purpose, with a binding returned constitutional policy, is established.
- Disturbance / variety regulated: Provider credentials, exposed host workspaces and unsafe Docker/host permissions pose risks; static tool access and user-selected sandbox bound work without an identity-level dispute adjudicator.
- Decisive decision or feedback right: Host/application config chooses providers, tools, credential injection, network policy, allowed workspace and graph goals. First-party adapter and runner enforce or translate those constraints, but do not decide enduring organizational ultimate purpose.
- Decision owner: External user/operator authority, deterministic first-party runner preflights and tool configuration; no S5 governance closure.
- Supporting / enforcement mechanisms: ToolAccess read-only/read-write, Docker secret isolation and network policy, scoped CLI config, user graph validation, failure results/logging.
- Closure path: Operator permissions/constraints → prepared runner command or denial/exception → task continues or stops; no ultimate-purpose question → legitimate S5 judgment → durable identity policy returned.
- Why this is / is not agent-owned: Command authorization and model provider safety parameters govern local execution, not the identity or policy of an independent viable organization.
- Evidence: [agentflow/agents/codex.py#L13](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/agents/codex.py#L13), [agentflow/agents/pi.py#L17](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/agents/pi.py#L17), [agentflow/runners/docker.py#L1](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/runners/docker.py#L1), [agentflow/specs.py#L2332](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/agentflow/specs.py#L2332), [README.md#L132](https://github.com/agentenv/agentflow/blob/eb51a2e7a5c7d65da5718c4a41843098b60c80e0/README.md#L132).
- Basis: Bounded negative after checking provider/tool security, graph controls and optimization modes.
- Confidence: Medium-high.
- Caveats: A human owner of the application above this graph may exercise legitimate S5 outside AgentFlow.

### Absence scope

- Surfaces inspected: Host-selected tools, sandbox/network/credential policies, PipelineSpec validation and optimizer restrictions.
- Plausible first-party paths checked: Ultimate mission tradeoffs, incident policy exceptions, long-horizon organization identity and operator delegation.
- Why no material first-party path remains: No shipped authority receives constitutional identity/purpose questions and returns binding policy changes; only user-provided task safety settings and static enforcement are shown.



## Recursion

The immediate S1 is operational model-backed graph nodes dispatched by AgentFlow as one program of tasks, with their outputs feeding downstream tasks. Opt-in S4 revises this **same** future program after observing a previous run. Periodic monitors and graph reviews are task-local controls. Neither arbitrary N-agent fanout nor a named Orchestrator proves a federation of viable S1 businesses with autonomous S2/S3/S3*/S5 rights.

## Variety and escalation

Model-selected actions and stored output handle changing task variety; graph dependencies and retries attenuate execution failure variety; optional future graph optimization can introduce changed capability across rounds. Queued failures, trace anomalies and periodic cancellations are operational task signals rather than established algedonic escalation to a legitimate organizational metasystem.

## Evidence gaps

- Upstream `agentenv/agentflow@eb51a2e7a5c7d65da5718c4a41843098b60c80e0` is source-inspected and first-party CLI integration is wired; the isolated evidence environment lacked `jinja2`, `boto3` and `pytest` dependencies, so full Python/CLI/remote model tests were **not** executed. This is not evidence of an upstream code defect.
- External Codex/Claude/Kimi/Pi command-line agent implementation and actual model inference are separate services. The integration can select model-backed tools through the documented supported actor mode, but no live task accuracy, scheduling throughput or cost advantage is measured here.
- `optimizer` plus `n_run>1` is a real **opt-in** future-graph adaptation loop. A structurally accepted pipeline may be worse than before; no measured improvement or automatic outside-of-session promotion is supported.
- Proposed lifecycle state does not alter canonical catalog, cohort signature, TLDR or rankings until the separate CI-gated admission transaction.

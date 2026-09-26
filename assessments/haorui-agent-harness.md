---
harness_id: haorui-agent-harness
project_name: Agent Harness
repository: https://github.com/haorui-harry/agent-harness
review_ref: 109dde248cb44227a9ed3a204790432a6da843da
reviewed_at: 2026-09-26
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-26
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Agent Harness

## Review boundary

- System in focus: one first-party `haorui-harry/agent-harness` deployment at pinned revision `109dde248cb44227a9ed3a204790432a6da843da`, centred on `HarnessEngine`, the thread-first `ThreadFirstSuperAgent`, persistent `AgentThreadRuntime`, executable task graphs, `TaskGraphActionMapper`, live-model graph expansion/replanning, and shipped skills/tools/workspace actions.
- Purpose and identity: turn open-ended user requests into inspectable deliverables through a persistent thread/workspace, task-adaptive capability planning, executable task graphs, tool/skill/workspace actions, recovery, evidence collection, and optional live-model reasoning/replanning.
- Relevant environment: user tasks, local workspaces/files/commands, configured external model endpoints, public/search evidence providers, external tools/services, and human operators who may interrupt/resume or approve ordinary risky actions.
- Standard-distribution boundary: shipped CLI/library/gateway/runtime surfaces in this repository at the frozen ref, including optional live-model mode when configured through the first-party runtime. Repository-development CI, tests, demos, research-lab experiments, generated reports, and benchmark artifacts are adjacent unless reached by the assessed runtime path.
- Credited operating / distribution surfaces: `app/harness/engine.py`, `app/harness/super_agent.py`, `app/harness/task_profile.py`, `app/agents/runtime.py`, `app/agents/task_actions.py`, `app/agents/scheduler.py`, `app/agents/subagents.py`, `app/harness/live_agent.py`, shipped tool/skill registries, runtime settings, CLI/gateway thread entrypoints, and persistent thread/workspace state.
- Adjacent first-party surfaces excluded from ownership: `tests/`, `.github/workflows/`, demo-only orchestration, `HarnessResearchLab`, `HarnessLiveExperiment`, CI-baseline/gate utilities, red-team/evaluation runs, generated demo/report artifacts, marketplace/reputation development surfaces, and repository-maintainer governance except where they corroborate a runtime implementation reached through the credited distribution.
- First-party operating / deployment modes considered: no-key deterministic task-graph execution; live-model-enabled thread-first execution; live-model graph expansion/replan; persistent async execution with interrupt/resume/recovery; optional parallel subagent helper; legacy skill-router graph and its conflict/consensus/dissent path.
- Recursion level: one Agent Harness deployment/thread execution is the assessed organization. A durable thread-first agent execution is the primary S1 operational unit. Individual skills, tool calls, static graph nodes, bounded subagent probes, and the CLI helper's parallel static track graphs are not promoted to recursive S1 units solely because they are separate processes/nodes.
- Reviewed revision: `109dde248cb44227a9ed3a204790432a6da843da`.
- Observation date: 2026-09-26.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

`HarnessEngine` composes a persistent thread runtime, task-graph action mapper, scheduler/recovery helper, optional parallel-subagent helper, tools, skills, evidence providers, live-model gateway/orchestrator, memory and reporting surfaces. The thread-first entrypoint creates or resumes one thread, analyzes the request, compiles an executable task graph, records a super-agent route, and executes that graph synchronously or asynchronously.

The task-graph compiler is not limited to a fixed recipe. In live mode, first-party graph-expansion prompts allow the configured model to return additional `workspace_action`, `tool_call`, and `subagent` nodes. During execution, `TaskGraphActionMapper` handles commands, tool calls, workspace actions, bounded subagent probes, and a `graph_replan` node. Replanning is fed a task-level world state and completion gap; when a live model is configured, the model receives current graph/execution state and may choose new operational commitments. The runtime then appends those nodes and rewires downstream dependencies so the new work executes before final synthesis/completion.

Persistent `AgentThreadRuntime` stores messages, artifacts, executions, events, control state and workspace paths. It supports async execution, interrupt, resume and recovery. `AgentExecutionScheduler` can discover paused/interrupted/running executions and resume them, but scheduler enforcement is not credited as S3 ownership; the autonomous S3 claim below rests on live-model replan discretion over current commitments.

The repository also contains an older skill-router graph with skill selection, complementarity scoring, conflict detection, consensus and dissent. It executes selected skills sequentially and synthesizes their outputs. Its conflict/consensus path informs final aggregation and human-review flags but does not establish the required inter-S1 S2 feedback loop. Likewise, the CLI's `run_parallel_subagents` helper starts several task graphs concurrently, but the shipped mission-to-subagent builder produces fixed `routing` → `execution_plan` → `review` graphs and does not itself establish viable autonomous S1 units or an interference-specific coordination closure.

Primary evidence:

- [`README.md`](https://github.com/haorui-harry/agent-harness/blob/109dde248cb44227a9ed3a204790432a6da843da/README.md) — thread-first design, persistent workspace/recovery, task graph, evidence rail and live analysis/synthesis/critique/revision mode.
- [`app/harness/engine.py`](https://github.com/haorui-harry/agent-harness/blob/109dde248cb44227a9ed3a204790432a6da843da/app/harness/engine.py) — top-level composition of thread runtime, scheduler, subagents, tools and live-model surfaces.
- [`app/harness/super_agent.py`](https://github.com/haorui-harry/agent-harness/blob/109dde248cb44227a9ed3a204790432a6da843da/app/harness/super_agent.py) — standard thread-first entrypoint, generic graph compilation and execution.
- [`app/harness/task_profile.py`](https://github.com/haorui-harry/agent-harness/blob/109dde248cb44227a9ed3a204790432a6da843da/app/harness/task_profile.py) — task profile, executable graph construction, model-driven graph expansion, and standard `graph_replan` insertion.
- [`app/agents/runtime.py`](https://github.com/haorui-harry/agent-harness/blob/109dde248cb44227a9ed3a204790432a6da843da/app/agents/runtime.py) — persistent thread/execution state, async execution, events, interrupt/resume and graph progression.
- [`app/agents/task_actions.py`](https://github.com/haorui-harry/agent-harness/blob/109dde248cb44227a9ed3a204790432a6da843da/app/agents/task_actions.py) — executable node dispatch, live subagent mini-planning, completion-gap analysis, live/local replanning, graph mutation and downstream dependency rewiring.
- [`app/agents/scheduler.py`](https://github.com/haorui-harry/agent-harness/blob/109dde248cb44227a9ed3a204790432a6da843da/app/agents/scheduler.py) — recoverable execution inspection and resume/recovery enforcement.
- [`app/agents/subagents.py`](https://github.com/haorui-harry/agent-harness/blob/109dde248cb44227a9ed3a204790432a6da843da/app/agents/subagents.py) and [`app/main.py`](https://github.com/haorui-harry/agent-harness/blob/109dde248cb44227a9ed3a204790432a6da843da/app/main.py) — optional parallel helper and the shipped static mission-track graph builder inspected for S2.
- [`app/harness/live_agent.py`](https://github.com/haorui-harry/agent-harness/blob/109dde248cb44227a9ed3a204790432a6da843da/app/harness/live_agent.py) — live-model gateway plus analysis/synthesis/critique/revision chain inspected for S1 and S3* boundaries.
- [`app/graph.py`](https://github.com/haorui-harry/agent-harness/blob/109dde248cb44227a9ed3a204790432a6da843da/app/graph.py), [`app/routing/executor.py`](https://github.com/haorui-harry/agent-harness/blob/109dde248cb44227a9ed3a204790432a6da843da/app/routing/executor.py), and [`app/routing/complementarity.py`](https://github.com/haorui-harry/agent-harness/blob/109dde248cb44227a9ed3a204790432a6da843da/app/routing/complementarity.py) — legacy skill-router coordination-like surfaces inspected and not over-credited as S2/S3*.
- [`app/memory/learning.py`](https://github.com/haorui-harry/agent-harness/blob/109dde248cb44227a9ed3a204790432a6da843da/app/memory/learning.py), [`app/harness/optimizer.py`](https://github.com/haorui-harry/agent-harness/blob/109dde248cb44227a9ed3a204790432a6da843da/app/harness/optimizer.py), and [`app/harness/iteration.py`](https://github.com/haorui-harry/agent-harness/blob/109dde248cb44227a9ed3a204790432a6da843da/app/harness/iteration.py) — learning/experiment surfaces inspected for S4.
- [`app/policy/center.py`](https://github.com/haorui-harry/agent-harness/blob/109dde248cb44227a9ed3a204790432a6da843da/app/policy/center.py) — static runtime mode/risk/governance policies inspected for S5.
- [`tests/test_agent_runtime.py`](https://github.com/haorui-harry/agent-harness/blob/109dde248cb44227a9ed3a204790432a6da843da/tests/test_agent_runtime.py) — adjacent corroboration that graph replan receives execution-loop/current-phase state, adds repair nodes, and interrupt/resume/recovery paths behave as implemented; tests do not own runtime decisions.

## Operational model

The primary operational unit is the durable thread-first execution. In live mode, the configured model is not merely a text generator: first-party prompts allow it to choose task-graph additions and, after operational feedback, choose new tool/workspace/subagent commitments. Deterministic machinery validates/executes those choices, persists artifacts/events and enforces graph dependencies.

The runtime also exposes many narrower worker-like surfaces: selected skills, tool calls, bounded subagent probes, static task-graph nodes and an optional parallel helper. Those surfaces are not automatically distinct S1 units. The frozen evidence does not establish a first-party coordination loop that starts from a concrete disturbance among multiple autonomous operational units and feeds a coordination result back into those units' later behavior.

## S1 — Operations

- State: A
- Function: transform an open-ended user request into concrete workspace/tool/evidence actions and a delivered artifact through a persistent thread execution whose operational plan can be model-selected and revised from execution feedback.
- Disturbance / variety regulated: heterogeneous user goals, available capabilities, current workspace state, tool/evidence results, failed or missing artifacts/validation, and changing completion gaps during the run.
- Decisive decision or feedback right: in live-enabled mode, choose the substantive task-graph actions to perform and revise those actions after observing current execution state and completion gaps.
- Decision owner: the configured live model actor reached through first-party task-profile expansion/subagent/replan prompts.
- Supporting / enforcement mechanisms: `HarnessEngine`, task-profile compiler, executable graph/dependencies, `TaskGraphActionMapper`, tool/skill registries, persistent thread/workspace state, command/tool execution, safety constraints and model-call budgets.
- Closure path: user request → thread/profile/graph context → live model selects operational graph additions/actions → runtime executes tools/workspace/subagent work → results/artifacts/world state enter `node_results`/completion state → live replan can select additional actions → final synthesis/delivery reflects the changed operational state.
- Boundary reachability: `ThreadFirstSuperAgent.run()` is a shipped standard entrypoint; it invokes `compile_generic_task_payload(...)`, passes the supported `live_model` configuration, and executes the resulting graph through the credited thread runtime without requiring an adjacent development/evaluation system.
- Why this is / is not agent-owned: removing the live model from the live-enabled mode removes the discretionary task-specific choice of model-generated graph additions/replan actions; deterministic fallback machinery remains, but it does not make materially the same open-ended decisions with the same discretion.
- Evidence: [`app/harness/super_agent.py`](https://github.com/haorui-harry/agent-harness/blob/109dde248cb44227a9ed3a204790432a6da843da/app/harness/super_agent.py); [`app/harness/task_profile.py`](https://github.com/haorui-harry/agent-harness/blob/109dde248cb44227a9ed3a204790432a6da843da/app/harness/task_profile.py); [`app/agents/task_actions.py`](https://github.com/haorui-harry/agent-harness/blob/109dde248cb44227a9ed3a204790432a6da843da/app/agents/task_actions.py); [`app/agents/runtime.py`](https://github.com/haorui-harry/agent-harness/blob/109dde248cb44227a9ed3a204790432a6da843da/app/agents/runtime.py).
- Basis: explicit + structural
- Confidence: high
- Caveats: no-key mode has substantially more deterministic planning. `A` is credited to the supported live-enabled first-party operating mode, not to every execution configuration.

## S2 — Coordination

- State: —
- Function: no material first-party S2 coordination function is established at the declared boundary.
- Disturbance / variety regulated: candidate disturbances inspected included concurrent subagent/shared-workspace interference, skill-output conflict/redundancy, graph scheduling dependencies and parallel mission-track execution.
- Decisive decision or feedback right: not established for a specific disturbance among distinct S1 operational units.
- Decision owner: not applicable.
- Supporting / enforcement mechanisms: task-graph dependency ordering, sequential skill execution, complementarity/conflict scoring, conflict/consensus reports, persistent shared thread state, and the optional parallel execution helper.
- Closure path: no qualifying disturbance → coordination response → subsequent S1 behavior loop was found.
- Why this is / is not agent-owned: ownership is not classified because the S2 function itself is not established.
- Evidence: [`app/agents/subagents.py`](https://github.com/haorui-harry/agent-harness/blob/109dde248cb44227a9ed3a204790432a6da843da/app/agents/subagents.py); [`app/main.py`](https://github.com/haorui-harry/agent-harness/blob/109dde248cb44227a9ed3a204790432a6da843da/app/main.py); [`app/routing/complementarity.py`](https://github.com/haorui-harry/agent-harness/blob/109dde248cb44227a9ed3a204790432a6da843da/app/routing/complementarity.py); [`app/routing/executor.py`](https://github.com/haorui-harry/agent-harness/blob/109dde248cb44227a9ed3a204790432a6da843da/app/routing/executor.py); [`app/graph.py`](https://github.com/haorui-harry/agent-harness/blob/109dde248cb44227a9ed3a204790432a6da843da/app/graph.py).
- Basis: structural negative
- Confidence: high
- Caveats: the repository has several coordination-like mechanisms, but the Profile requires the full S2 witness rather than generic routing/conflict handling.

### Absence scope

- Surfaces inspected: thread/task-graph runtime, optional parallel subagent helper, mission-to-subagent graph builder, task graph dependencies, legacy skill execution, complementarity/conflict/consensus/dissent code, persistence and recovery controls, and relevant tests/docs.
- Plausible first-party paths checked: parallel mission tracks as candidate distinct S1s; multiple live subagent probes; skill conflict avoidance; conflict detection plus consensus synthesis; shared workspace/thread state; scheduler/dependency ordering.
- Why no material first-party path remains: the shipped parallel helper's first-party mission builder creates fixed static track graphs rather than clearly autonomous operational units; the legacy skill-router executes skills sequentially and its post-execution conflict/consensus result feeds aggregation rather than later behavior of the contributing skills; graph dependencies and shared state order/transport work without tying that machinery to a concrete inter-S1 disturbance and returned coordination response.

## S3 — Inside-and-now control

- State: A
- Function: regulate the currently executing job as a whole when present commitments no longer close the task, by deciding which additional operational commitments should be inserted before delivery.
- Disturbance / variety regulated: missing required artifacts/channels/validation, command or tool failure, evidence/workspace gaps, incomplete current execution, and mismatches between the task specification and observed world state.
- Decisive decision or feedback right: choose new current commitments from `workspace_action`, `tool_call`, and `subagent` actions after seeing whole-job execution/completion state, and insert those commitments into the active graph.
- Decision owner: the configured live model actor in `_live_replan_suggestions()` for the live-enabled mode.
- Supporting / enforcement mechanisms: deterministic task/world-state construction, failure-policy classification, capability registry suggestions, fallback repair seed, node allow-lists, graph mutation, dependency rewiring, persistent execution state, scheduler/recovery machinery and tool/workspace enforcement.
- Closure path: current graph executes → completion packet/world state exposes unresolved gap → `graph_replan` receives current job state → live model selects additional commitments → runtime appends the selected nodes and rewires synthesis/completion dependencies → subsequent execution performs the added work before the job can close.
- Boundary reachability: the standard task-profile compiler adds a first-party `graph_replan` node whenever graph expansion enables replanning, and the standard thread-first execution path reaches `TaskGraphActionMapper._execute_graph_replan`; supported `live_model` configuration is carried through the same runtime context.
- Why this is / is not agent-owned: without the live model, the runtime can still apply deterministic fallback/capability repairs, but it no longer makes the same task-specific discretionary choice among allowed new commitments. The model therefore owns the open-ended current-control decision in the credited mode; the runtime enforces and persists it.
- Evidence: [`app/harness/task_profile.py`](https://github.com/haorui-harry/agent-harness/blob/109dde248cb44227a9ed3a204790432a6da843da/app/harness/task_profile.py); [`app/agents/task_actions.py`](https://github.com/haorui-harry/agent-harness/blob/109dde248cb44227a9ed3a204790432a6da843da/app/agents/task_actions.py); [`app/agents/runtime.py`](https://github.com/haorui-harry/agent-harness/blob/109dde248cb44227a9ed3a204790432a6da843da/app/agents/runtime.py); [`app/harness/super_agent.py`](https://github.com/haorui-harry/agent-harness/blob/109dde248cb44227a9ed3a204790432a6da843da/app/harness/super_agent.py); [`tests/test_agent_runtime.py`](https://github.com/haorui-harry/agent-harness/blob/109dde248cb44227a9ed3a204790432a6da843da/tests/test_agent_runtime.py) as corroboration.
- Basis: explicit + structural
- Confidence: high
- Caveats: S3 is mode-dependent; the autonomous owner exists in live-model-enabled execution. Deterministic recovery/scheduling alone would not justify `A`.
- Whole-system current view: replan input includes query/graph id, failure policy, completion packet, `state_gap`, capability replan, accumulated `node_results`, execution-loop schema, current loop phase, phase summary and fallback seed; this is a job-wide current-state view rather than one worker's local result.
- Current-control decision scope: add or withhold new tool calls, workspace actions and bounded subagent commitments, and thereby alter the active graph dependencies that gate synthesis/completion.

## S3* — Complementary audit

- State: —
- Function: no sufficiently independent complementary operational-audit path is established in the standard distribution.
- Disturbance / variety regulated: candidate audit surfaces inspected included the live `critique` pass, structured dissent/conflict verification, completion/validation nodes, traces, red-team/evaluator utilities, tests and report artifacts.
- Decisive decision or feedback right: no complementary audit judgment with materially different access to operational reality is closed at the assessed runtime boundary.
- Decision owner: not applicable.
- Supporting / enforcement mechanisms: critique prompts, evidence digest, deterministic conflict/dissent checks, validation artifacts, traces and development/evaluation utilities.
- Closure path: not established for an independent audit channel.
- Why this is / is not agent-owned: ownership is not classified because the S3* function itself is not established.
- Evidence: [`app/harness/live_agent.py`](https://github.com/haorui-harry/agent-harness/blob/109dde248cb44227a9ed3a204790432a6da843da/app/harness/live_agent.py); [`app/graph.py`](https://github.com/haorui-harry/agent-harness/blob/109dde248cb44227a9ed3a204790432a6da843da/app/graph.py); [`app/routing/executor.py`](https://github.com/haorui-harry/agent-harness/blob/109dde248cb44227a9ed3a204790432a6da843da/app/routing/executor.py); adjacent `tests/` and evaluator/red-team surfaces.
- Basis: structural negative
- Confidence: high
- Caveats: a separate model call named critique or verifier is not sufficient when it remains an ordinary mandatory QA stage over the same production answer/evidence path.

### Absence scope

- Surfaces inspected: live analysis/synthesis/critique/revision chain, graph dissent path, task completion/validation nodes, thread artifacts/events/traces, evaluator/red-team/research-lab utilities, and tests.
- Plausible first-party paths checked: critique as independent reviewer; dissent as verifier; validation artifacts as raw operational inspection; red-team/evaluator as sporadic audit; thread trace/artifact inspection as alternative access.
- Why no material first-party path remains: live critique is a routine in-band stage using the same candidate answer/evidence digest and configured model endpoint before revision; dissent/conflict checks operate on the ordinary production outputs; traces and completion artifacts are ordinary reporting; red-team/evaluator/tests are adjacent evaluation/development surfaces rather than a sporadic independent audit wired into standard operation and returned to current control.

## S4 — Outside-and-then intelligence

- State: —
- Function: no organizational outside-and-then adaptation loop is established at the assessed deployment boundary.
- Disturbance / variety regulated: candidate surfaces inspected included external evidence/search, runtime learning statistics, optimizer runs, live experiments, research-lab comparisons, strategy selection and skill reliability feedback.
- Decisive decision or feedback right: no first-party path was found that turns external/future-relevant distinctions into organizational adaptation options and returns those options into present harness capability.
- Decision owner: not applicable.
- Supporting / enforcement mechanisms: evidence providers, `record_run` learning statistics, reliability-aware skill selection, optimizer/experiment result stores and research-lab tooling.
- Closure path: not established.
- Why this is / is not agent-owned: ownership is not classified because the S4 function itself is not established.
- Evidence: [`app/memory/learning.py`](https://github.com/haorui-harry/agent-harness/blob/109dde248cb44227a9ed3a204790432a6da843da/app/memory/learning.py); [`app/routing/complementarity.py`](https://github.com/haorui-harry/agent-harness/blob/109dde248cb44227a9ed3a204790432a6da843da/app/routing/complementarity.py); [`app/harness/optimizer.py`](https://github.com/haorui-harry/agent-harness/blob/109dde248cb44227a9ed3a204790432a6da843da/app/harness/optimizer.py); [`app/harness/iteration.py`](https://github.com/haorui-harry/agent-harness/blob/109dde248cb44227a9ed3a204790432a6da843da/app/harness/iteration.py); evidence/search paths in [`app/harness/evidence.py`](https://github.com/haorui-harry/agent-harness/blob/109dde248cb44227a9ed3a204790432a6da843da/app/harness/evidence.py).
- Basis: structural negative
- Confidence: high
- Caveats: external research used to answer the current user task is environmental sensing for that task, not by itself organizational S4.

### Absence scope

- Surfaces inspected: evidence/search providers, live strategy selection, runtime memory/learning, complementarity/reliability scoring, optimizer, live experiment tracker, research-lab/evaluation utilities, recipes and task-profile planning.
- Plausible first-party paths checked: learning from prior run quality into future skill selection; live A/B experiments; optimizer selecting better modes/recipes; external evidence driving future harness changes; research-lab promotion into runtime capability.
- Why no material first-party path remains: the persistent learning loop records internal execution success/quality and adjusts skill-selection signals but does not model an external/prospective environment or generate organizational adaptation options; optimizer/research-lab/live-experiment surfaces are adjacent evaluation/selection tools and no standard runtime path automatically converts their findings into changed harness capability.

## S5 — Policy and identity

- State: —
- Function: no runtime identity/ultimate-policy closure is established at the chosen recursion.
- Disturbance / variety regulated: candidate surfaces inspected included system modes, risk/governance policy bundles, human approval/interrupt controls, constraints, recipes and static runtime settings.
- Decisive decision or feedback right: no first-party path was found for resolving an identity- or ultimate-policy-level issue and returning that authoritative decision to govern subsequent operation.
- Decision owner: not applicable.
- Supporting / enforcement mechanisms: static `PolicyBundle` values, runtime constraints, safety checks, approval flags, operator interrupt/resume and configuration.
- Closure path: not established.
- Why this is / is not agent-owned: ownership is not classified because the S5 function itself is not established.
- Evidence: [`app/policy/center.py`](https://github.com/haorui-harry/agent-harness/blob/109dde248cb44227a9ed3a204790432a6da843da/app/policy/center.py); runtime constraints/settings in [`app/harness/models.py`](https://github.com/haorui-harry/agent-harness/blob/109dde248cb44227a9ed3a204790432a6da843da/app/harness/models.py) and [`app/harness/runtime_settings.py`](https://github.com/haorui-harry/agent-harness/blob/109dde248cb44227a9ed3a204790432a6da843da/app/harness/runtime_settings.py); thread control in [`app/agents/runtime.py`](https://github.com/haorui-harry/agent-harness/blob/109dde248cb44227a9ed3a204790432a6da843da/app/agents/runtime.py).
- Basis: structural negative
- Confidence: high
- Caveats: high-risk human approval and operator interrupt are current-task controls, not evidence of ultimate policy/identity authority.

### Absence scope

- Surfaces inspected: system mode/risk/governance policies, guardrails/security, runtime settings/constraints, operator interrupt/resume, approval-required traces, recipes, task profiles, CLI/gateway controls and repository governance.
- Plausible first-party paths checked: autonomous policy revision; parent-governed identity/policy escalation; human approval as parent S5; durable constitution/purpose changes; returned governance decisions altering later runtime identity.
- Why no material first-party path remains: policies and constraints are developer/operator-authored static boundaries; generic approval/interrupt paths regulate ordinary current work; no identity/ultimate-policy issue is routed to a legitimate authority and returned as a durable governing decision at the assessed deployment recursion.

## Recursion

The runtime can nest task graphs and bounded subagent probes, and the optional helper can execute several graphs concurrently. The evidence does not establish those workers as recursive viable systems with durable local identity, environment, meaningful autonomy and their own metasystem. They are therefore treated as nested execution structures rather than a second VSM recursion.

## Variety and escalation

The thread runtime preserves substantial current-operational variety through persistent messages, artifacts, graph state, events, completion packets, state-gap analysis, interrupts and resumable execution. Tool and workspace allow-lists attenuate action variety; live graph expansion/replan amplifies response variety when the current plan is insufficient. Failure/validation gaps can be turned into additional current commitments through S3 replan. Operator interrupt/resume and human-review flags are escalation/control surfaces, but no separate S5 identity closure is inferred from them.

## Evidence gaps

- The live-model endpoint is configurable and external; this assessment credits the first-party decision protocol and runtime closure, not any provider-side organizational function.
- Parallel subagent execution could support richer multi-S1 organizations when downstream users supply stronger autonomous graphs, but the frozen first-party standard surfaces do not establish the complete S2 witness needed for a positive state.
- A future audit mode using a distinct model/evaluator with different raw operational access and returned control feedback could change S3*, but the current critique/dissent/evaluation surfaces do not establish that independence.
- A future release that automatically promotes research-lab/optimizer findings into present runtime capability could change S4; no such closure is established at the frozen ref.

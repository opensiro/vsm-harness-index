---
harness_id: continuum
project_name: Continuum
repository: https://github.com/shyftlabs/continuum
review_ref: e1ef4c45d08f81757972949b85670ca5453d7d0e
reviewed_at: 2026-09-24
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-24
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Continuum

## Review boundary

- System in focus: one first-party Continuum agent/workflow organization instantiated through the shipped `AgentRunner` at pinned revision `e1ef4c45d08f81757972949b85670ca5453d7d0e`, including `BaseAgent` execution, Tool/MCP calls, handoffs, decision/run state and the packaged workflow-agent modes that directly execute through the runner.
- Purpose and identity: build and execute autonomous agent work, including composed multi-agent workflows, with first-party lifecycle, tool, memory, handoff, workflow-control and observability machinery.
- Relevant environment: user/application objectives; external model-provider endpoints; MCP/tool environments; optional Redis, Qdrant/Milvus, Langfuse and Temporal infrastructure; human reviewers for explicitly configured approval gates; and application-supplied specialist agents/configuration.
- Standard-distribution boundary: Continuum's Python runtime, `AgentRunner`, `Executor`, first-party workflow agents, tool/handoff/security/runtime state paths and packaged optional durable-execution adapter are inside. Model endpoints and infrastructure services remain dependencies and do not donate organizational autonomy.
- Credited operating / distribution surfaces: `src/continuum/agent/runner.py`; `src/continuum/agent/execution/executor.py`; `src/continuum/agent/workflow/` including `scatter.py`, `planner.py`, `supervised.py`, `reflection.py`, `router.py`, `parallel.py`, `dag.py`, `loop.py` and `debate.py`; first-party Tool/MCP, handoff, memory/session and approval paths reached by normal runs.
- Adjacent first-party surfaces excluded from ownership: `.claude/` repository-development/dogfood agents and skills; repository CI/release/contributor governance; playground/demo organizations; `src/continuum/evaluation/` golden-dataset/RAGAS/DeepEval workflows and other offline evaluation surfaces unless explicitly wired into an assessed live run; documentation/tests used only as corroboration.
- First-party operating / deployment modes considered: plain `BaseAgent` model/tool/handoff execution; Router/Sequential/Parallel/DAG/Loop/Reflection/Debate workflows; default LLM-split Scatter workflow; Planner single-agent and agent-pool modes including failure replanning and optional success-time replanning; SupervisedSequential quality-gated workflow; optional Temporal durability/HITL support.
- Recursion level: one Continuum workflow/run organization is the primary system-in-focus. Its task-producing `BaseAgent` workers are S1 units. Workflow agents can supply metasystem functions for that run organization. Independent Continuum runs and repository-development/evaluation organizations are adjacent systems rather than silently aggregated into one installation-wide metasystem.
- Reviewed revision: `e1ef4c45d08f81757972949b85670ca5453d7d0e`.
- Observation date: 2026-09-24.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Continuum is a composable Python agent runtime. `AgentRunner` is the supported execution entry point and wires model access, Tool execution, memory/session state, handoffs, run lifecycle, decision tracing and a first-party `Executor`. The executor owns the repeated model → Tool/handoff → observation → next-model-turn loop. Workflow-agent subclasses instead carry orchestration in their own `execute()` methods; `AgentRunner` explicitly detects these classes and dispatches them to that first-party workflow entry point, so the workflow evidence below is part of the supported runtime rather than documentation-only examples.

The workflow library exposes several organizational forms. Router, Sequential, Parallel and DAG primarily provide routing, sequencing, fan-out and dependency execution and are not credited merely from topology. Two modes establish stronger functions. `ScatterAgent` uses a first-party LLM split decision to assign a distinct slice to every parallel S1 worker. Its built-in split prompt explicitly requires `No overlap — each covers a distinct item or aspect`; the resulting slices become the workers' actual inputs. This is a concrete scope-overlap disturbance plus an agent-owned separation decision returned into later S1 behavior.

`PlannerAgent` provides current control beyond initial task decomposition. It first creates an ordered plan, then executes it against either one worker or a declared specialist pool. In the standard failure path (`replan_on_failure=True` by default), a failed step returns its error together with the goal, completed work and available agents into a new model decision that replaces the remaining plan and is executed immediately. Optional `enable_replanning` adds the same kind of current judgment after successful steps: the planner receives the last output and the complete remaining commitment set and decides `CONTINUE` or returns replacement steps. The positive S3 claim relies on this feedback-driven revision of whole-run commitments, not on the `Planner` name or initial decomposition.

Several surfaces look superficially like S3* but remain below the Profile threshold. `ReflectionAgent` makes a separate critique call and retries the producer, while `SupervisedSequentialAgent` uses a supervisor LLM to score every stage and retry below-threshold output. Both are routine quality gates in the same operational path and see the ordinary task/output representation rather than materially complementary operational reality. Decision traces provide observability/forkability, not an independent challenge actor. The repository also includes optional golden-dataset/RAGAS/DeepEval machinery, but that is a separate evaluation surface rather than a standard live-runtime feedback path and is excluded from product-runtime ownership under the declared boundary.

Long-term memory, user profiles, model routing, policy/data-label gates, Tool approval and Temporal durability are substantial supporting mechanisms. They preserve context, constrain actions and can involve humans, but the reviewed standard runtime does not turn them into a closed outside/future adaptation function or identity/ultimate-policy authority.

Primary evidence:

- [`src/continuum/agent/runner.py`](https://github.com/shyftlabs/continuum/blob/e1ef4c45d08f81757972949b85670ca5453d7d0e/src/continuum/agent/runner.py) — supported execution entry point, first-party runtime assembly and explicit workflow-agent dispatch.
- [`src/continuum/agent/execution/executor.py`](https://github.com/shyftlabs/continuum/blob/e1ef4c45d08f81757972949b85670ca5453d7d0e/src/continuum/agent/execution/executor.py) — core autonomous conversation loop, Tool execution, handoffs, returned observations and loop guards.
- [`src/continuum/agent/workflow/scatter.py`](https://github.com/shyftlabs/continuum/blob/e1ef4c45d08f81757972949b85670ca5453d7d0e/src/continuum/agent/workflow/scatter.py) — model-selected non-overlapping branch scopes, concurrent execution and gather/merge closure.
- [`src/continuum/agent/workflow/planner.py`](https://github.com/shyftlabs/continuum/blob/e1ef4c45d08f81757972949b85670ca5453d7d0e/src/continuum/agent/workflow/planner.py) — plan generation, specialist assignment, whole-remaining-plan review and feedback-driven replanning after current outcomes/failures.
- [`src/continuum/agent/workflow/supervised.py`](https://github.com/shyftlabs/continuum/blob/e1ef4c45d08f81757972949b85670ca5453d7d0e/src/continuum/agent/workflow/supervised.py) — routine supervisor scoring/retry path.
- [`src/continuum/agent/workflow/reflection.py`](https://github.com/shyftlabs/continuum/blob/e1ef4c45d08f81757972949b85670ca5453d7d0e/src/continuum/agent/workflow/reflection.py) — routine self-critique/retry path.
- [`src/continuum/agent/workflow/dag.py`](https://github.com/shyftlabs/continuum/blob/e1ef4c45d08f81757972949b85670ca5453d7d0e/src/continuum/agent/workflow/dag.py) — dependency execution and parallelism, treated as workflow support rather than VSM function by naming.
- [`src/continuum/agent/approval.py`](https://github.com/shyftlabs/continuum/blob/e1ef4c45d08f81757972949b85670ca5453d7d0e/src/continuum/agent/approval.py) — configured per-Tool human approval over consequential calls; explicitly separate from static policy/trust enforcement.
- [`docs/memory.md`](https://github.com/shyftlabs/continuum/blob/e1ef4c45d08f81757972949b85670ca5453d7d0e/docs/memory.md) — persistent semantic memory and intelligent-memory mechanisms.
- [`README.md`](https://github.com/shyftlabs/continuum/blob/e1ef4c45d08f81757972949b85670ca5453d7d0e/README.md) — supported runtime/workflow surface, optional infrastructure and optional evaluation package boundary.

## Operational model

For a plain agent, `AgentRunner` constructs run context and state, builds messages, exposes the configured Tool/handoff surface and enters the first-party executor. Each model turn can return an answer or Tool/handoff calls; the runtime executes selected actions, appends observations and continues until a terminal/error/bounded condition. Workflow agents are routed by the same runner to their own first-party `execute()` control loops, which recursively invoke workers through `runner.run()`.

In Scatter mode, the workflow first asks a model to partition the objective into one distinct, non-overlapping slice per worker, runs those workers concurrently and gathers their outputs. In Planner mode, a model builds an ordered plan over a worker or specialist pool and may replace remaining commitments when current execution invalidates them. These are separate supported modes of the same constructor/runtime distribution; the assessment credits the function-specific mode that closes each state without assuming every workflow simultaneously instantiates every metasystem function.

## S1 — Operations

- State: A
- Function: perform goal-directed agent work through repeated contextual model decisions, Tool/handoff actions and returned environmental observations.
- Disturbance / variety regulated: user/application objective, model uncertainty, Tool/MCP results and errors, session/context state, handoff outcomes, provider responses and bounded execution conditions.
- Decisive decision or feedback right: choose each substantive next answer, Tool call, handoff or continuation from current context and use returned observations to determine subsequent behavior.
- Decision owner: the model-driven `BaseAgent` actor executed through Continuum's first-party `AgentRunner`/`Executor` path.
- Supporting / enforcement mechanisms: run lifecycle/state, message construction, ToolHandler/ToolExecutor, handoff executor, max-turn/cycle guards, sessions/memory, policy/data-label enforcement, tracing and optional durable infrastructure.
- Closure path: objective/context → first-party runner/executor → model decision → Tool/handoff or answer → first-party action execution and observation → observation appended to run context → next model decision or terminal state.
- Boundary reachability: `AgentRunner.run()` is the documented quick-start and production API; the executor and Tool/handoff loop are directly wired into that supported path at the pinned revision.
- Why this is / is not agent-owned: deterministic runtime machinery transports, constrains and records the loop, but the substantive next-action decision is made by the model-driven agent over current context and available capabilities. External model endpoints supply inference but do not donate a separate organizational function beyond the actor Continuum directly invokes.
- Evidence: [`runner.py`](https://github.com/shyftlabs/continuum/blob/e1ef4c45d08f81757972949b85670ca5453d7d0e/src/continuum/agent/runner.py); [`executor.py`](https://github.com/shyftlabs/continuum/blob/e1ef4c45d08f81757972949b85670ca5453d7d0e/src/continuum/agent/execution/executor.py); [`README.md`](https://github.com/shyftlabs/continuum/blob/e1ef4c45d08f81757972949b85670ca5453d7d0e/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: provider internals, external MCP services and infrastructure are environmental dependencies and are not independently credited.

## S2 — Coordination

- State: A
- Function: attenuate scope overlap among sibling S1 workers that execute parallel slices of one Scatter workflow.
- Disturbance / variety regulated: without partitioning, parallel workers can receive overlapping aspects of the same objective, duplicating work and producing competing/contradictory contributions for the shared gather stage.
- Decisive decision or feedback right: choose a concrete distinct scope for every sibling worker such that the parallel assignments cover different items/aspects rather than overlap.
- Decision owner: the autonomous splitter model invoked by the first-party `ScatterAgent` in its standard LLM-split mode.
- Supporting / enforcement mechanisms: declared worker list, split prompt/schema, JSON parsing, branch-specific run contexts, concurrent dispatch, fail strategy and gather/merge stage.
- Closure path: shared objective + sibling worker identities → Scatter split-model decision with explicit `No overlap` requirement → one selected slice is bound to each branch → each S1 executes on that slice → distinct results return into the shared gather stage.
- Boundary reachability: LLM splitting is the default `ScatterAgent` path when explicit `input_slices` are not supplied; workflow agents are directly dispatched by `AgentRunner` through their `execute()` entry points.
- Why this is / is not agent-owned: the runtime fixes the worker roster and parses/transports the split, but the model chooses the semantic separation relation from the current objective. Removing that model decision leaves only fallback same-input fan-out, which does not make the same adaptive no-overlap choice.
- Evidence: [`scatter.py`](https://github.com/shyftlabs/continuum/blob/e1ef4c45d08f81757972949b85670ca5453d7d0e/src/continuum/agent/workflow/scatter.py); [`runner.py`](https://github.com/shyftlabs/continuum/blob/e1ef4c45d08f81757972949b85670ca5453d7d0e/src/continuum/agent/runner.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: Parallel/DAG/Router/Handoff topology is not credited as S2 by itself. Explicit developer-supplied Scatter slices move the scope choice to configuration; the positive `A` state is established by the separately supported default model-split mode.
- Distinct S1 units: two or more `BaseAgent` workers in one Scatter workflow, each directly executing a task slice through `AgentRunner`.
- Inter-S1 disturbance: overlapping assignments cause sibling workers to cover the same item/aspect, creating duplicated or potentially conflicting contributions to the same aggregate response; the built-in split prompt explicitly names overlap as the condition to avoid.
- Attenuating coordination relation: a model-selected partition that must produce exactly one short, non-overlapping subtask for each declared worker.
- Feedback into subsequent S1 behaviour: each selected slice becomes that branch's actual `runner.run(..., input=slice)` input, so the coordination decision directly changes what each S1 does next.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the credited relation is not merely fan-out or assignment; it is explicitly constructed to suppress a concrete cross-worker scope-overlap disturbance before concurrent operation.

## S3 — Inside-and-now control

- State: A
- Function: regulate the current commitments of a Planner workflow organization by revising remaining work and specialist assignment in response to live execution results or failures.
- Disturbance / variety regulated: completed outputs may invalidate later steps; a worker/step may fail; remaining commitments can cease to fit the goal/current state; specialist assignment may need replacement for unresolved work.
- Decisive decision or feedback right: decide whether the remaining plan still makes sense and, when current feedback requires change, replace the remaining commitment set with a new sequence/agent assignment that the runtime will execute.
- Decision owner: the autonomous planning/replanning model invoked by first-party `PlannerAgent`.
- Supporting / enforcement mechanisms: current plan representation, completed-step history, failed-step/error capture, declared specialist pool, `max_steps`, fail strategy, JSON parsing and deterministic execution of the accepted replacement plan.
- Closure path: current goal + completed work + remaining commitments + latest output or failure/error → planner model judges `CONTINUE` or produces replacement steps → `plan_steps` is replaced in the live workflow → subsequent worker dispatch follows the revised plan → new outcomes feed later current-control decisions.
- Boundary reachability: `PlannerAgent` is a shipped workflow agent routed directly by `AgentRunner`; failure replanning is enabled by default (`replan_on_failure=True`) and success-time replanning is an exposed first-party mode (`enable_replanning=True`).
- Why this is / is not agent-owned: deterministic code executes the returned plan and enforces limits, but it does not choose the new commitments. The model receives a whole-run current representation and decides whether/how to revise unresolved work; removing it leaves no equivalent discretionary replan decision.
- Evidence: [`planner.py`](https://github.com/shyftlabs/continuum/blob/e1ef4c45d08f81757972949b85670ca5453d7d0e/src/continuum/agent/workflow/planner.py); [`runner.py`](https://github.com/shyftlabs/continuum/blob/e1ef4c45d08f81757972949b85670ca5453d7d0e/src/continuum/agent/runner.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: initial goal decomposition, Router selection and static DAG scheduling are not credited as S3. The positive mapping relies on current execution feedback entering a whole-remaining-plan revision with authority to change subsequent commitments at the workflow/run recursion.
- Whole-system current view: the replan path supplies the workflow goal, completed successful work, the failed/current step and error or last output, the complete remaining plan, and in pool mode the declared available agents.
- Current-control decision scope: retain or replace unresolved steps, choose their instructions and (in agent-pool mode) their specialist assignments, thereby revising current organizational commitments after execution has begun.

## S3* — Audit

- State: —
- Function: no material first-party live-runtime path establishes sufficiently independent complementary audit of S1/S3 claims with corrective closure.
- Disturbance / variety regulated: Continuum supplies routine critique/scoring, traces and optional offline evaluation, but the supported runtime does not add an independent complementary evidence channel that challenges ordinary operational claims from materially different access to reality.
- Decisive decision or feedback right: no qualifying S3*-specific audit judgment is established inside the declared live-runtime boundary.
- Decision owner: not established for S3*.
- Supporting / enforcement mechanisms: Reflection critique/retry, SupervisedSequential scoring/retry, decision traces/forkability, Langfuse observability, optional golden datasets/RAGAS/DeepEval evaluation and deterministic retry/gating logic.
- Closure path: Reflection/Supervised findings can retry an operational stage, but they are routine same-path quality checks over ordinary task/output representations; offline evaluation can produce scores outside the live organization, but no standard runtime path returns an independent complementary audit finding into current control.
- Why this is / is not agent-owned: separate model calls do make judgments, but independence of process alone is insufficient when the reviewer sees essentially the same operational report and is part of mandatory production QA. Optional offline evaluators are adjacent to the assessed runtime and do not close this function by repository co-location.
- Evidence: [`reflection.py`](https://github.com/shyftlabs/continuum/blob/e1ef4c45d08f81757972949b85670ca5453d7d0e/src/continuum/agent/workflow/reflection.py); [`supervised.py`](https://github.com/shyftlabs/continuum/blob/e1ef4c45d08f81757972949b85670ca5453d7d0e/src/continuum/agent/workflow/supervised.py); [`README.md`](https://github.com/shyftlabs/continuum/blob/e1ef4c45d08f81757972949b85670ca5453d7d0e/README.md); [`src/continuum/evaluation/README.md`](https://github.com/shyftlabs/continuum/blob/e1ef4c45d08f81757972949b85670ca5453d7d0e/src/continuum/evaluation/README.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: an application could wire external ground truth or an independent evaluator into a Continuum organization; that downstream organization requires separate evidence.

### Absence scope

- Surfaces inspected: ReflectionAgent, SupervisedSequentialAgent, Debate judge, decision tracing/fork/resume surfaces, Langfuse observability, README evaluation claims and `src/continuum/evaluation/` offline evaluation package.
- Plausible first-party paths checked: reflection as S3*; supervisor scoring as S3*; debate judge as S3*; trace replay/fork as S3*; golden-dataset/RAGAS/DeepEval tooling as S3*.
- Why no material first-party path remains: live critics/supervisors are routine production-path checks without materially complementary access, while the stronger evaluation tooling is an optional adjacent evaluation workflow rather than a first-party live audit→current-control closure for the assessed runtime.

## S4 — Intelligence / adaptation

- State: —
- Function: no material first-party outside-and-then prospective organizational adaptation loop is established.
- Disturbance / variety regulated: memory, model routing, Planner replanning and workflow reflection adapt current responses/execution to available context, but they do not model future environmental change and turn it into changed organizational capability.
- Decisive decision or feedback right: no first-party actor is shown selecting a future-facing capability/organizational adaptation from external intelligence and returning it into present capability/S3.
- Decision owner: not established for S4.
- Supporting / enforcement mechanisms: long-term semantic memory, intelligent-memory scoring/decay/entity/user profiles, session state, Planner replanning, Reflection retry, model routing/fallback, optional evaluation datasets and configurable Tools/policies.
- Closure path: current/past context can influence later task execution, but no standard path closes external/future distinction → adaptation option → changed current capability.
- Why this is / is not agent-owned: model calls may plan, critique, remember and re-route, yet those decisions remain task/current-operation oriented. Persistence and learning-like memory do not supply the missing prospective organizational adaptation function.
- Evidence: [`docs/memory.md`](https://github.com/shyftlabs/continuum/blob/e1ef4c45d08f81757972949b85670ca5453d7d0e/docs/memory.md); [`planner.py`](https://github.com/shyftlabs/continuum/blob/e1ef4c45d08f81757972949b85670ca5453d7d0e/src/continuum/agent/workflow/planner.py); [`reflection.py`](https://github.com/shyftlabs/continuum/blob/e1ef4c45d08f81757972949b85670ca5453d7d0e/src/continuum/agent/workflow/reflection.py); [`README.md`](https://github.com/shyftlabs/continuum/blob/e1ef4c45d08f81757972949b85670ca5453d7d0e/README.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: applications can use Continuum primitives to build an S4 organization; generic composability is not `C` without an S4-specific first-party decision/feedback path.

### Absence scope

- Surfaces inspected: memory/intelligent-memory docs, Planner success/failure replanning, Reflection, model routing/fallback, Tool/configuration surfaces, evaluation package and durable workflow mechanisms.
- Plausible first-party paths checked: persistent memory as S4; Planner replanning as S4; Reflection/self-improvement wording as S4; model routing as S4; offline evaluation as S4.
- Why no material first-party path remains: identified mechanisms regulate current tasks or persist history; none establishes external/future sensing plus adaptation-option development and return into present organizational capability.

## S5 — Policy / identity

- State: —
- Function: no material first-party identity/ultimate-policy closure is established at the workflow/run recursion.
- Disturbance / variety regulated: policies, data labels, Tool trust/approval, model-routing rules and agent instructions constrain actions, but no path is shown deciding what the organization is or resolving identity-level policy tension through ultimate authority.
- Decisive decision or feedback right: no first-party runtime actor or parent path is shown receiving an identity/ultimate-policy issue, making the legitimate final decision and returning it to govern subsequent operation.
- Decision owner: not established for S5.
- Supporting / enforcement mechanisms: agent instructions/config, policy stores, data-label propagation, Tool capability/trust controls, per-Tool human approval, security scanners, model-routing configuration and runtime enforcement.
- Closure path: configured rules/approval declarations constrain individual actions and model/tool access; ordinary Tool approval returns a decision over one consequential action, not an identity/ultimate-policy decision for the organization.
- Why this is / is not agent-owned: static or operator-supplied constraints do not own ultimate policy by being enforced, and the human approval handler is scoped to declared Tool calls rather than organizational identity. No autonomous or parent-governed S5 closure is established.
- Evidence: [`approval.py`](https://github.com/shyftlabs/continuum/blob/e1ef4c45d08f81757972949b85670ca5453d7d0e/src/continuum/agent/approval.py); [`src/continuum/agent/config.py`](https://github.com/shyftlabs/continuum/blob/e1ef4c45d08f81757972949b85670ca5453d7d0e/src/continuum/agent/config.py); [`executor.py`](https://github.com/shyftlabs/continuum/blob/e1ef4c45d08f81757972949b85670ca5453d7d0e/src/continuum/agent/execution/executor.py).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: a downstream application can place identity authority around these enforcement primitives; that is a different system-in-focus.

### Absence scope

- Surfaces inspected: agent configuration/instructions, active policy context, Tool trust/capability gates, data labels, scanners, human Tool approval, model routing and durable workflow/HITL controls.
- Plausible first-party paths checked: system prompt/configuration as S5; policy store as S5; Tool approval as parent S5; security/trust gates as S5; model-routing policy as S5.
- Why no material first-party path remains: all identified paths enforce or approve lower-level operational constraints/actions; no identity/ultimate-policy issue reaches a legitimate ultimate authority and returns as governing organizational policy.

## Overall assessment

Continuum is more than a single-agent executor: its standard distribution closes autonomous S1 through the owned model/Tool/handoff loop, autonomous S2 through Scatter's model-selected non-overlapping scope partition returned into sibling worker inputs, and autonomous S3 through Planner's feedback-driven revision of the whole remaining commitment set during a live workflow. Reflection/supervisor/evaluation, memory/adaptation-like mechanisms and policy/HITL controls remain below S3*/S4/S5 thresholds at the declared runtime boundary.

Standalone vector:

```text
S1=A / S2=A / S3=A / S3*=— / S4=— / S5=—
```

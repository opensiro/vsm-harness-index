---
harness_id: mcp-agent
project_name: mcp-agent
repository: https://github.com/lastmile-ai/mcp-agent
review_ref: f62d849350816588b1c6294e7914bbe4d8b84072
reviewed_at: 2026-10-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# mcp-agent

## Review boundary

- System in focus: the user-instantiated first-party Python `mcp-agent` workflow runtime that creates model-backed task agents, delegates MCP tool work and controls the completion of one multi-step objective; the shipped optional `DeepOrchestrator` is the most capable operating mode assessed.
- Purpose and identity: execute an operator-given objective through agent/tool calls, including planned multi-agent deep research, within configured resources and tool access.
- Relevant environment: user objectives, available MCP server capabilities, model completions, tool/task errors, task results, context limitations and running budgets.
- Standard-distribution boundary: SDK `MCPApp`, `Agent`, `AugmentedLLM`, `workflows/factory.py`, the standard/simple orchestrator, optional `workflows/deep_orchestrator/` and first-party executor/Temporal adapters. The application operator chooses which workflow to instantiate.
- Credited operating / distribution surfaces: [`workflows/factory.py`](https://github.com/lastmile-ai/mcp-agent/blob/f62d849350816588b1c6294e7914bbe4d8b84072/src/mcp_agent/workflows/factory.py), [`deep_orchestrator/orchestrator.py`](https://github.com/lastmile-ai/mcp-agent/blob/f62d849350816588b1c6294e7914bbe4d8b84072/src/mcp_agent/workflows/deep_orchestrator/orchestrator.py), [`task_executor.py`](https://github.com/lastmile-ai/mcp-agent/blob/f62d849350816588b1c6294e7914bbe4d8b84072/src/mcp_agent/workflows/deep_orchestrator/task_executor.py), [`queue.py`](https://github.com/lastmile-ai/mcp-agent/blob/f62d849350816588b1c6294e7914bbe4d8b84072/src/mcp_agent/workflows/deep_orchestrator/queue.py), [`policy.py`](https://github.com/lastmile-ai/mcp-agent/blob/f62d849350816588b1c6294e7914bbe4d8b84072/src/mcp_agent/workflows/deep_orchestrator/policy.py), [`context_builder.py`](https://github.com/lastmile-ai/mcp-agent/blob/f62d849350816588b1c6294e7914bbe4d8b84072/src/mcp_agent/workflows/deep_orchestrator/context_builder.py).
- Adjacent first-party surfaces excluded from ownership: the vendor-operated cloud control plane, deployment CLI lifecycle, tracing/observability display, documentation, examples/tests, maintainers/release governance and host-owned policies; externally installed MCP servers and model providers are not first-party governance actors.
- First-party operating / deployment modes considered: standard agent/LLM execution; router/orchestrator workflows; opt-in `create_deep_orchestrator(...)` with model planner, per-task agents, verification and policy; optional Temporal persistence. Positive S3 is mode-conditional, not claimed for every SDK instantiation.
- Recursion level: one running, operator-configured workflow controlling subordinate task agents. Independent MCP servers and the external operator are environment/parent actors, not a second automatically viable VSM level.
- Reviewed revision: `f62d849350816588b1c6294e7914bbe4d8b84072`.
- Observation date: 2026-10-30.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The public SDK exposes agent- and workflow-level factories. In the optional deep-orchestrator mode, a model-backed `StrategicPlanner` generates a structured `Plan` with steps, task agents and tools; `PlanVerifier` checks structural validity; `TodoQueue` deduplicates tasks and holds pending/completed steps; `TaskExecutor` creates configured or model-designed agents and calls their LLM/tool runtime, optionally executing sibling tasks in parallel. Successful task outputs and extracted knowledge enter `WorkspaceMemory`; `ContextBuilder` feeds relevant prior results to later agents. After each step, `PolicyEngine` applies budget, failure and completion conditions; on an empty queue, a distinct model-backed `ObjectiveVerifier` assesses completion and can cause the planner to produce another plan. The same objective is eventually summarized to the user. Other factory modes have different and often simpler reachability; calling a generic agent does not imply this full loop.

## Operational model

External task requirements → model plan → configured/dynamic agents call models and MCP servers → task outputs/errors/knowledge → shared queue/budget/progress → model verification and deterministic policy → continuation or task-level replanning → synthesis. Parallel execution and queue deduplication organize work, but the examined paths do not identify an interference-specific signal and feedback right between contending S1 units. Replanning is used to finish the *present user objective*, not to prospectively redesign future system capability or respond to independent outside forecasts.

## S1 — Operations

- State: A
- Function: perform user-specified task work using model-driven tool-using agents and produce task evidence/artifacts.
- Disturbance / variety regulated: heterogeneous task demands, MCP tool results, errors, content differences and model-generated action choices.
- Decisive decision or feedback right: each task agent's configured LLM chooses the response and permitted MCP tool use; a model-backed agent designer may generate role/tool instructions for an unmatched task.
- Decision owner: instantiated `Agent`/`AugmentedLLM` in task execution, with permitted MCP servers and model providers furnishing external capabilities.
- Supporting / enforcement mechanisms: SDK agent/session lifecycle, server registry, retry loop, task context builder, executor and result store.
- Closure path: objective/task context → LLM/tool execution → generated answer, artifacts or error → stored `TaskResult` → next tasks/final response.
- Boundary reachability: public `create_deep_orchestrator` factory constructs a `DeepOrchestrator`; its `TaskExecutor._execute_task_once` attaches an LLM to the selected/dynamically created `Agent` and awaits `generate_str`.
- Why this is / is not agent-owned: model-backed task actors make semantic choices about task responses and tool use; Python and MCP transport schedule/enforce rather than supply those choices.
- Evidence: [`workflows/factory.py`](https://github.com/lastmile-ai/mcp-agent/blob/f62d849350816588b1c6294e7914bbe4d8b84072/src/mcp_agent/workflows/factory.py) (`create_deep_orchestrator`), [`task_executor.py`](https://github.com/lastmile-ai/mcp-agent/blob/f62d849350816588b1c6294e7914bbe4d8b84072/src/mcp_agent/workflows/deep_orchestrator/task_executor.py) (`execute_task`, `_create_dynamic_agent`), [`agents/agent.py`](https://github.com/lastmile-ai/mcp-agent/blob/f62d849350816588b1c6294e7914bbe4d8b84072/src/mcp_agent/agents/agent.py).
- Basis: explicit/structural.
- Confidence: high for source-wired agent path; outcomes are not independently run.
- Caveats: depends on caller-supplied models/servers/credentials and the selected workflow; no claim every mode is multi-agent.

## S2 — Coordination

- State: —
- Function: no demonstrated feedback controller specifically attenuating interference or oscillations among distinct concurrently operating S1 units at the chosen recursion.
- Disturbance / variety regulated: duplicate tasks, dependency constraints, parallel fanout and token-context limits are addressed as ordinary execution/ordering concerns; no source witness of mutually interfering S1 operational claims is supplied.
- Decisive decision or feedback right: `TodoQueue` deduplicates names/task hashes and `TaskExecutor` awaits sibling tasks; neither consumes a particular operational conflict signal and returns mediation to both actors.
- Decision owner: deterministic queue/executor and initial model planner, not an independently evidenced inter-S1 disturbance attenuator.
- Supporting / enforcement mechanisms: plan dependency verifier, seen-task sets, sequential steps, executor parallel fanout, shared context and cache.
- Closure path: planner produces nonduplicated queued steps → agents execute → queue records completion; no inter-agent collision → mediator → modified independent operating behavior loop shown.
- Why this is / is not agent-owned: model task planning and coordination syntax do not establish S2 autonomy without a specific cross-unit interference mechanism.
- Evidence: [`queue.py`](https://github.com/lastmile-ai/mcp-agent/blob/f62d849350816588b1c6294e7914bbe4d8b84072/src/mcp_agent/workflows/deep_orchestrator/queue.py) (`merge_plan`, `_filter_step`), [`plan_verifier.py`](https://github.com/lastmile-ai/mcp-agent/blob/f62d849350816588b1c6294e7914bbe4d8b84072/src/mcp_agent/workflows/deep_orchestrator/plan_verifier.py), [`task_executor.py`](https://github.com/lastmile-ai/mcp-agent/blob/f62d849350816588b1c6294e7914bbe4d8b84072/src/mcp_agent/workflows/deep_orchestrator/task_executor.py) (`execute_step`).
- Basis: structural.
- Confidence: medium-high for examined shipped multi-agent workflow.
- Caveats: an application built *on* mcp-agent may implement its own S2; such user code is outside this library review.

### Absence scope

- Surfaces inspected: deep-orchestrator planner/queue/parallel executor, context sharing, dependency checks, standard orchestration/router and session/connection support.
- Plausible first-party paths checked: duplicate-step/task filtering, configured parallel work, agent cache, tool routing and common state/memory.
- Why no material first-party path remains: these paths allocate and order work or deduplicate tasks but do not evidence an interference-specific observation/attenuation/feedback cycle between distinct ongoing S1 units.

## S3 — Inside-and-now control

- State: A
- Function: observe cumulative present workflow progress and exercise whole-objective control over the next assignment, replanning, continuation and termination of subordinate S1 tasks.
- Disturbance / variety regulated: incomplete coverage of the user objective, failed subtasks, exceeded resources, invalid proposed plans and fragmented task knowledge.
- Whole-system current view: `TodoQueue` retains pending/completed steps and task states; `WorkspaceMemory` stores task results/knowledge/artifacts; `SimpleBudget` tracks aggregate token/cost/time use; planner and `ObjectiveVerifier` receive cumulative progress/knowledge.
- Current-control decision scope: model `StrategicPlanner` chooses full next-step/task allocations and revised plans; model `ObjectiveVerifier` reports completion with confidence; `PolicyEngine` and configured limits enforce continue/replan/force-complete/emergency-stop; those decisions directly change live queue/execution.
- Decisive decision or feedback right: agents propose and assess whole-objective plans; the runtime verifies proposals, loads or merges their steps and applies configured stopping/continuation decisions.
- Decision owner: model-backed `StrategicPlanner` and `ObjectiveVerifier` for semantic whole-run judgments, constrained by deterministic plan validator/policy, with objective supplied by the operator.
- Supporting / enforcement mechanisms: `PlanVerifier`, `TodoQueue`, `WorkspaceMemory`, `SimpleBudget`, `PolicyEngine`, final synthesis and iteration/replan caps.
- Closure path: aggregate task feedback → whole-objective planner/verifier judgment → policy action → rewritten/merged execution queue or terminal synthesis → updated task results and progress.
- Boundary reachability: optional factory-created `DeepOrchestrator.generate` calls `_execute_workflow`; inside its loop, empty-queue completion verification and policy-directed `_create_full_plan`/`merge_plan` are live paths, not standalone unused utilities.
- Why this is / is not agent-owned: model planning and objective verification supply semantic whole-run decisions, while code deterministically constrains budgets and executes those decisions; model ownership is conditional on deep-orchestrator mode.
- Evidence: [`orchestrator.py`](https://github.com/lastmile-ai/mcp-agent/blob/f62d849350816588b1c6294e7914bbe4d8b84072/src/mcp_agent/workflows/deep_orchestrator/orchestrator.py) (`_execute_workflow`, `_create_full_plan`, `_verify_completion`), [`policy.py`](https://github.com/lastmile-ai/mcp-agent/blob/f62d849350816588b1c6294e7914bbe4d8b84072/src/mcp_agent/workflows/deep_orchestrator/policy.py), [`budget.py`](https://github.com/lastmile-ai/mcp-agent/blob/f62d849350816588b1c6294e7914bbe4d8b84072/src/mcp_agent/workflows/deep_orchestrator/budget.py), [`memory.py`](https://github.com/lastmile-ai/mcp-agent/blob/f62d849350816588b1c6294e7914bbe4d8b84072/src/mcp_agent/workflows/deep_orchestrator/memory.py).
- Basis: explicit/structural.
- Confidence: medium-high for implemented conditional path, not a measured end-to-end success guarantee.
- Caveats: structural plan verification returns a final invalid plan with a warning after exhausted retries, and reported completion can be model-dependent; do not infer robust fail-closed task success.

## S3* — Complementary audit

- State: —
- Function: no demonstrated independent, complementary audit of actual operations capable of challenging S3's inside-and-now view through a separate supervisory feedback channel.
- Disturbance / variety regulated: inaccurate completion claims and invalid plans receive routine verification, not independently directed spot inspection of operational reality.
- Decisive decision or feedback right: `ObjectiveVerifier` receives the same queue summary, knowledge and artifacts and triggers ordinary completion/replan policy; `PlanVerifier` performs static plan checks.
- Decision owner: workflow's normal model verifier and deterministic validator, both inside the execution-control loop, not an independently chartered audit actor.
- Supporting / enforcement mechanisms: confidence threshold, plan errors and generated task summaries.
- Closure path: completion verification feeds the routine policy decision; there is no separate audit sampling of real actions with challenge/correction to S3 oversight.
- Why this is / is not agent-owned: separate model role alone is insufficient for independent complementary audit at this organizational boundary.
- Evidence: [`orchestrator.py`](https://github.com/lastmile-ai/mcp-agent/blob/f62d849350816588b1c6294e7914bbe4d8b84072/src/mcp_agent/workflows/deep_orchestrator/orchestrator.py) (`_verify_completion`), [`plan_verifier.py`](https://github.com/lastmile-ai/mcp-agent/blob/f62d849350816588b1c6294e7914bbe4d8b84072/src/mcp_agent/workflows/deep_orchestrator/plan_verifier.py).
- Basis: structural.
- Confidence: medium.
- Caveats: downstream apps may configure external evaluators, excluded unless they are installed first-party audit authority.

### Absence scope

- Surfaces inspected: workflow plan validation, `ObjectiveVerifier`, final synthesis, test/eval support, Temporal persistence and tracing.
- Plausible first-party paths checked: separate verifier role, structured plan validity checking, workflow tests and trace outputs.
- Why no material first-party path remains: verification is part of the ordinary chain of task completion and reports from the same internal memory; no independently governed external reality inspection feeding S3 is evidenced.

## S4 — Outside-and-then intelligence

- State: —
- Function: no evidenced first-party prospective intelligence loop that studies changes in the external operating environment and returns capability-level adaptation options for later horizons.
- Disturbance / variety regulated: unforeseen subtasks and failed task attempts trigger *within-objective* replanning, which supports current delivery instead of adjusting the workflow's future identity, architecture or operating capability.
- Decisive decision or feedback right: model `StrategicPlanner` updates the current task plan from previous results; it does not install a revised strategy/tool policy for future independent objectives based on externally observed trends.
- Decision owner: present-workflow model planner and configured operator; no separately continuing future-facing intelligence owner.
- Supporting / enforcement mechanisms: replan count, knowledge extraction, context builder and active queue merge.
- Closure path: current task failures/progress → replan current objective → continue same job; no outside horizon → prospective adaptation option → governance/control acceptance → changed future capability return.
- Why this is / is not agent-owned: agentic replanning is real, but the evidenced decision right is S3 current control, not prospective S4 adaptation across a future environment.
- Evidence: [`orchestrator.py`](https://github.com/lastmile-ai/mcp-agent/blob/f62d849350816588b1c6294e7914bbe4d8b84072/src/mcp_agent/workflows/deep_orchestrator/orchestrator.py) (`_create_full_plan`, `_execute_workflow`), [`knowledge.py`](https://github.com/lastmile-ai/mcp-agent/blob/f62d849350816588b1c6294e7914bbe4d8b84072/src/mcp_agent/workflows/deep_orchestrator/knowledge.py), [`context_builder.py`](https://github.com/lastmile-ai/mcp-agent/blob/f62d849350816588b1c6294e7914bbe4d8b84072/src/mcp_agent/workflows/deep_orchestrator/context_builder.py).
- Basis: structural.
- Confidence: medium for inspected standard workflow, without asserting inability of downstream applications to add S4.
- Caveats: project documentation calls it *adaptive*; this is current task adaptation, a narrower function than VSM S4.

### Absence scope

- Surfaces inspected: deep-orchestrator planning/knowledge, evaluator-style patterns, SDK workflow factory, ongoing session storage and default operator configuration.
- Plausible first-party paths checked: failure-triggered replanning, task knowledge reuse, dynamic agent design and long-running Temporal execution.
- Why no material first-party path remains: none connects a distinct outside/future observation to a prospective capability change that is accepted into later runs; a current-job plan revision is not such evidence.

## S5 — Policy and identity

- State: —
- Function: no first-party agent with legitimate ultimate-authority loop that deliberates or ratifies the organization's mission, values and governing operating envelope.
- Disturbance / variety regulated: tool limits, user objectives, model settings, token/cost budgets and retry thresholds are constrained by operator configuration.
- Decisive decision or feedback right: the external user chooses objective, tool access, models and budgets; internal agent can propose task plans but cannot legitimately change those governing commitments.
- Decision owner: external app operator and SDK config, not an authorized self-governance or parent-policy actor in the running workflow.
- Supporting / enforcement mechanisms: `DeepOrchestratorConfig`, `PolicyEngine`, SDK app lifecycle, CLI/deployment interfaces.
- Closure path: fixed operator policy limits agent execution; no identity-level issue → legitimate S5 ratification → returned change of operative purpose is wired.
- Why this is / is not agent-owned: task allocation and resource shutdown rights do not confer authority to set ultimate system identity.
- Evidence: [`config.py`](https://github.com/lastmile-ai/mcp-agent/blob/f62d849350816588b1c6294e7914bbe4d8b84072/src/mcp_agent/workflows/deep_orchestrator/config.py), [`policy.py`](https://github.com/lastmile-ai/mcp-agent/blob/f62d849350816588b1c6294e7914bbe4d8b84072/src/mcp_agent/workflows/deep_orchestrator/policy.py), [`workflows/factory.py`](https://github.com/lastmile-ai/mcp-agent/blob/f62d849350816588b1c6294e7914bbe4d8b84072/src/mcp_agent/workflows/factory.py).
- Basis: structural.
- Confidence: medium-high for the bounded first-party library.
- Caveats: OSS maintainer governance and application-user instructions are outside actors, not internally evidenced `(P)` return paths.

### Absence scope

- Surfaces inspected: SDK factory, DeepOrchestrator config/policy, CLI/deployment adjacency, user objective flow and project governance artifacts.
- Plausible first-party paths checked: model planner altering plans, emergency stop, dynamic agent instructions and operator-chosen workload.
- Why no material first-party path remains: the system pursues supplied purposes under fixed operator limits; no ratified identity-policy decision is returned from a first-party or installed parent governance function.

## Distributed OSS parent arrangement

Library maintainers govern releases; developers deploy `MCPApp` and configure models, MCP services, objectives, budgets and auth. These external parent actors are not a shipped operational S5/parent return mechanism, so no `(P)` inference is made.

## Self-hosted and non-human modes

The SDK may run locally or with external hosted model/API/MCP services. The deep workflow can plan, run multiple agents, verify completion and replan without human semantic approval within configured bounds, but requires runtime credentials/integrations; source review does not assert an end-to-end execution test or service availability. Temporal persistence prolongs workflow execution but does not independently supply VSM S4/S5.

## Recursion

DeepOrchestrator supervisory planning sits above subordinate task agents, but this is task decomposition, not a demonstrated nested hierarchy of self-contained viable autonomous organizations with their own complete S1–S5 loops.

## Variety and escalation

Agent specialization and MCP tools amplify available action variety; plan validity, deduplication, task context limits and budgets attenuate uncontrolled work. The policy returns overload/failure to stop or replan for the current objective. No evidence converts generic traces/metrics into an independent complementary audit or escalates mission conflicts to an internal S5 ratification authority.

## Evidence gaps

- No hosted model/provider, MCP server, expensive multi-agent E2E or Temporal run was performed. Labels are source-path, not empirical success rates.
- No cross-run prospective adaptation or S2 interference-specific witness was found in the inspected distributed SDK; application-authored custom workflows are outside this boundary.
- The planner's exhausted-validation fallback may return an invalid plan, so source existence must not be presented as a guarantee of controlled success.

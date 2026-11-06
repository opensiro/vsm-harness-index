---
harness_id: agent01
project_name: Agent01
repository: https://github.com/Babe153/Agent01-from-Scratch
review_ref: 7e4f5f82a1008d6276dfe1d6a97e68484665ecdd
reviewed_at: 2026-11-06
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

# Agent01 · From Scratch

## Review boundary

- System in focus: the actually wired Stage 2 Python/LangGraph coding-assistant CLI, including a model-backed planner, model-backed actor tool loop, deterministic command verifier and retry router, workspace-scoped file and shell tools, ephemeral Todo state and provider configuration.
- Purpose and identity: demonstrate a runnable plan–execute–verify coding agent that carries out a user task in a bounded local workspace and reports the observed verification result.
- Relevant environment: developer request, Python files, tests/process exits, language-model output, untrusted tool arguments, workspace path and command timeouts, task attempt budgets and configured OpenAI-compatible model endpoint.
- Standard-distribution boundary: `src/Agent01/cli/app.py` / `__main__.py` invoke `core/agent.py::stream_agent_events`, which compiles `graph/workflow.py`: **planner → actor → verifier → planner/final**. The external LangGraph/LangChain runtime and OpenAI-compatible inference API are dependencies, not separate first-party organizational owners.
- Credited operating / distribution surfaces: `src/Agent01/{cli/app.py,core/{agent,state,paths}.py,graph/{workflow,nodes,state}.py,providers/openai_provider.py,tools/{registry,file_tools,grep_tool,bash_tool,todo_tool}.py,prompts/version2.py}` plus the published `main.py` CLI entry.
- Adjacent first-party surfaces excluded from ownership: `agents/code_agent.py`, `agents/search_agent.py`, `prompts/version3.py`, `prompts/version4.py`, `tools/web_search_tool.py`, and forward-looking graph-state fields for sources/handoffs/compression. These files/fields exist at the frozen SHA, but the shipped CLI graph does not invoke those specialist agent functions or consume them as an active multi-agent operating path. Also excluded: project-development README milestones, CI, future source revisions, human maintainers and external model services.
- First-party operating modes considered: `Agent01 TASK`, `--workspace`, `--max-attempts`; the Stage 2 planner/actor/verifier/final graph with a maximum of ten model calls in each actor run and a default three whole-workflow attempts.
- Recursion level: one coding-task operational loop; a planner and verifier are roles within its serial workflow, not independently operating peer S1 cells or a higher-level organization.
- Reviewed revision: `7e4f5f82a1008d6276dfe1d6a97e68484665ecdd`; observation date 2026-11-06; Profile `0.2.4` / Methodology `0.3.7`.

## Repository architecture

The shipped Typer CLI calls `stream_agent_events`, creates a `RuntimeState` with a workspace and invokes `build_workflow`. `planner_node` creates a user-task plan, Todo list, acceptance text and verification commands using a configured model. If the model's response is unusable, it falls back to a hardcoded Python-oriented plan (including a special Conway's Game of Life example). `actor_node` then binds first-party file/read/edit/search/shell/Todo tools to a separate model invocation loop and feeds back actual tool results for up to ten model turns. `verifier_node` is Python code: it runs the planner-supplied commands via the same `run_bash`, stores exit codes/stdout/stderr, and returns failures to the planner until success or the configured attempt limit. `final_node` formats the results without calling a model. The graph has no checkpoint persistence in this published stage.

There are additional specialist function definitions named `run_code_agent` and `run_search_agent`, plus State annotations for prospective specialist handoffs and context compression. They are not reachable from `graph/workflow.py` and are not invoked from the live CLI; `graph/nodes.py` uses `prompts/version2.py`, not those specialist definitions. This review does not import capabilities from Stage 3/4 plans or untracked files from later Git history.

Primary source evidence at the exact frozen revision:

- [Shipped CLI and help/task entry](https://github.com/Babe153/Agent01-from-Scratch/blob/7e4f5f82a1008d6276dfe1d6a97e68484665ecdd/src/Agent01/cli/app.py)
- [Live graph construction and routing](https://github.com/Babe153/Agent01-from-Scratch/blob/7e4f5f82a1008d6276dfe1d6a97e68484665ecdd/src/Agent01/graph/workflow.py)
- [Planner, actor and command verifier](https://github.com/Babe153/Agent01-from-Scratch/blob/7e4f5f82a1008d6276dfe1d6a97e68484665ecdd/src/Agent01/graph/nodes.py)
- [Workspace/runtime and graph invocation](https://github.com/Babe153/Agent01-from-Scratch/blob/7e4f5f82a1008d6276dfe1d6a97e68484665ecdd/src/Agent01/core/agent.py)
- [Command boundaries and output](https://github.com/Babe153/Agent01-from-Scratch/blob/7e4f5f82a1008d6276dfe1d6a97e68484665ecdd/src/Agent01/tools/bash_tool.py)
- [Unwired specialist functions](https://github.com/Babe153/Agent01-from-Scratch/blob/7e4f5f82a1008d6276dfe1d6a97e68484665ecdd/src/Agent01/agents/code_agent.py)
- [Unwired search-specialist function](https://github.com/Babe153/Agent01-from-Scratch/blob/7e4f5f82a1008d6276dfe1d6a97e68484665ecdd/src/Agent01/agents/search_agent.py)
- [README Stage 2 shipped/planned boundary](https://github.com/Babe153/Agent01-from-Scratch/blob/7e4f5f82a1008d6276dfe1d6a97e68484665ecdd/README.md)

## Operational model

The user gives a coding task. A planner model proposes an operational plan, then an actor model selects concrete workspace tool calls, reads their outcomes and may revise its actions. A deterministic verifier runs command checks and feeds specific failures into the next planning attempt. The user sees a final execution/verification summary, with success defined by the configured commands' outcomes rather than a separate independent audit of all natural-language criteria.

## S1 — Operations

- State: A
- Function: carry out concrete software-editing/research steps by selecting and revising actual tools in response to task and observed effects.
- Disturbance / variety regulated: unknown project requirements, changing file content, test failures, tool errors, insufficient plan detail and rework after unsuccessful verification.
- Decisive decision or feedback right: planner model chooses the task plan and verification suggestions; actor model chooses specific file, grep, shell and Todo actions with arguments based on observed tool results and prior verifier failures.
- Decision owner: the configured task-specific planner and actor model invocations inside the first-party graph; these are sequential roles in one S1 operation.
- Supporting / enforcement mechanisms: compiled LangGraph route, OpenAI-compatible adapter, structured tool wrappers, runtime workspace paths, Todo state, tool-output feedback, attempt/turn limits, deterministic command verifier and fallback plan.
- Closure path: user task → model plan → model-selected tool actions → file/process observation → model-selected continuation; if verification commands fail, actual error data returns to the next planner and actor iteration.
- Boundary reachability: CLI `main` invokes `stream_agent_events`, which calls the wired Stage 2 graph and `planner_node`/`actor_node`/`verifier_node`; `actor_node` executes first-party bound tools on live files.
- Why this is / is not agent-owned: without the planner/actor model, the fallback, verifier and routing cannot choose arbitrary task-specific implementation actions; the decisive operational exploration is model-selected.
- Evidence: [`graph/nodes.py`](https://github.com/Babe153/Agent01-from-Scratch/blob/7e4f5f82a1008d6276dfe1d6a97e68484665ecdd/src/Agent01/graph/nodes.py); [`graph/workflow.py`](https://github.com/Babe153/Agent01-from-Scratch/blob/7e4f5f82a1008d6276dfe1d6a97e68484665ecdd/src/Agent01/graph/workflow.py); [`core/agent.py`](https://github.com/Babe153/Agent01-from-Scratch/blob/7e4f5f82a1008d6276dfe1d6a97e68484665ecdd/src/Agent01/core/agent.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: executing an end-to-end model task requires configured external model service; the fallback plan is biased toward Python and the verifier checks configured commands, not necessarily all goal semantics.

## S2 — Coordination

- State: —
- Function: no mitigation relation regulating concrete interference between multiple concurrently operating first-party S1 cells is established.
- Disturbance / variety regulated: plan–actor–verifier handoff is serial task sequencing, not competing S1 work cells with a separately managed shared disturbance.
- Decisive decision or feedback right: none for an inter-S1 anti-interference arrangement.
- Decision owner: not established; the compiled LangGraph edge sequence routes phases of one task, not multiple worker operations.
- Supporting / enforcement mechanisms: shared `Agent01GraphState`, planner/actor/verifier nodes and verifier retry route; dormant specialist functions are source files, not live subordinate operations.
- Closure path: one planner feeds the one actor, which feeds the one verifier, then loops or finishes. No separate S1–S1 collision is detected, attenuated and fed back.
- Why this is / is not agent-owned: function names and graph edges do not create cooperating autonomous units; no independent simultaneously operating S1 pair is reachable from the CLI graph.
- Evidence: [`graph/workflow.py`](https://github.com/Babe153/Agent01-from-Scratch/blob/7e4f5f82a1008d6276dfe1d6a97e68484665ecdd/src/Agent01/graph/workflow.py); [`graph/nodes.py`](https://github.com/Babe153/Agent01-from-Scratch/blob/7e4f5f82a1008d6276dfe1d6a97e68484665ecdd/src/Agent01/graph/nodes.py); [`agents/code_agent.py`](https://github.com/Babe153/Agent01-from-Scratch/blob/7e4f5f82a1008d6276dfe1d6a97e68484665ecdd/src/Agent01/agents/code_agent.py).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: specialist modules can be imported by future/custom code; no such published first-party execution path is wired at this ref.

### Absence scope

- Surfaces inspected: graph edges, node imports, actor tool construction, specialist agent exports and CLI invocation.
- Plausible first-party paths checked: concurrent distinct autonomous subagent runs, shared-resource conflicts, task-claim mediation, lock/worktree coordination and bilateral worker feedback.
- Why no material first-party path remains: the only published entry graph is serial and never invokes the specialist functions; there are no multiple live S1 units to coordinate at this recursion.

## S3 — Current internal control

- State: —
- Function: no separately closed whole-current management of a multi-operation portfolio, resource allocation or organizational performance is established.
- Disturbance / variety regulated: verifier failures and unfinished Todos are controlled as ordinary current-task progress and bounded retries.
- Decisive decision or feedback right: no cross-S1 resource arbitration, exception escalation or portfolio-wide corrective authority.
- Decision owner: not established; Python verifier and graph router implement task-local deterministic continuation/stop conditions.
- Supporting / enforcement mechanisms: planner acceptance criteria, single-task Todo list, failed-command text, attempts counter, conditional edges and final report.
- Closure path: verification failure → revise current task plan and try again, or stop at the attempt cap. This is operational feedback rather than independent whole-system current management.
- Why this is / is not agent-owned: the model adapts a local coding task, while the router only enforces fixed attempt limits; neither manages an aggregate set of autonomous operating cells.
- Evidence: [`graph/nodes.py`](https://github.com/Babe153/Agent01-from-Scratch/blob/7e4f5f82a1008d6276dfe1d6a97e68484665ecdd/src/Agent01/graph/nodes.py); [`graph/workflow.py`](https://github.com/Babe153/Agent01-from-Scratch/blob/7e4f5f82a1008d6276dfe1d6a97e68484665ecdd/src/Agent01/graph/workflow.py).
- Basis: structural absence review.
- Confidence: high.
- Caveats: rich state/plan/verifier nomenclature should not inflate a one-task graph into an S3 organization.

### Absence scope

- Surfaces inspected: graph state, planner, actor, verifier/router, Todo handling, CLI workspaces and source-present specialist functions.
- Plausible first-party paths checked: multi-worker health aggregation, live resource balancing, independent current-control budget decisions and interventions affecting more than one S1 unit.
- Why no material first-party path remains: every live control path is bounded to one graph invocation and one task, and no active S1 portfolio exists.

## S3* — Complementary audit

- State: —
- Function: no independently sourced complementary audit path challenging an operator's account with a separate corrective supervisory finding is established.
- Disturbance / variety regulated: incorrect code, failing commands and false completion are observed by command verification, but only through tests chosen by the same planner/workflow.
- Decisive decision or feedback right: `verifier_node` runs direct commands and may cause a retry; it has no independent audit scope, separate evidence selection, producer-challenging mandate or supervisory escalation right.
- Decision owner: deterministic verifier/router of the ordinary task graph, not an independent audit actor.
- Supporting / enforcement mechanisms: `verification_commands`, `run_bash`, captured exit codes/stdout/stderr, failure text and conditional retry.
- Closure path: planner-selected verification command → subprocess result → same task's retry or final summary. This is useful QA but not a separately governed audit path.
- Why this is / is not agent-owned: the verifier is plain Python using the planner's chosen checks; an independent audit cannot be inferred from naming the graph node `verifier`.
- Evidence: [`graph/nodes.py`](https://github.com/Babe153/Agent01-from-Scratch/blob/7e4f5f82a1008d6276dfe1d6a97e68484665ecdd/src/Agent01/graph/nodes.py); [`tools/bash_tool.py`](https://github.com/Babe153/Agent01-from-Scratch/blob/7e4f5f82a1008d6276dfe1d6a97e68484665ecdd/src/Agent01/tools/bash_tool.py); [`README.md`](https://github.com/Babe153/Agent01-from-Scratch/blob/7e4f5f82a1008d6276dfe1d6a97e68484665ecdd/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: direct subprocess output is real evidence of configured checks but does not independently test unasked acceptance criteria.

### Absence scope

- Surfaces inspected: verifier command sourcing, command execution and results, retry/final routing, proposed specialist modules, CLI events and stage documentation.
- Plausible first-party paths checked: independent raw-workspace reviewer, distinct sampling/audit selection, producer claim challenge, audit corrections and verified supervisory resolution.
- Why no material first-party path remains: command checks originate in the producer-planner path and stay in ordinary task QA; no independent reviewer/audit authority closes.

## S4 — Outside-and-then intelligence

- State: —
- Function: no prospective scan of future external changes linked to organizational option selection and changed current capability is established.
- Disturbance / variety regulated: task requirement changes, provider choices and potential web research are current-task inputs or human configuration, not future-environment governance.
- Decisive decision or feedback right: no autonomous future-capacity adaptation or strategic option adoption.
- Decision owner: not established at this boundary; the user supplies task/provider and the planner creates present-task steps.
- Supporting / enforcement mechanisms: OpenAI-compatible provider, plan JSON, imported but unwired WebSearch/specialist code and context-related TypedDict placeholders.
- Closure path: task → immediate plan/tools/verification; no outside-trend inquiry → future options → accountable capability change → operating feedback.
- Why this is / is not agent-owned: present-task planning and dormant research module code cannot substitute for S4 outside-and-then intelligence.
- Evidence: [`graph/workflow.py`](https://github.com/Babe153/Agent01-from-Scratch/blob/7e4f5f82a1008d6276dfe1d6a97e68484665ecdd/src/Agent01/graph/workflow.py); [`graph/state.py`](https://github.com/Babe153/Agent01-from-Scratch/blob/7e4f5f82a1008d6276dfe1d6a97e68484665ecdd/src/Agent01/graph/state.py); [`agents/search_agent.py`](https://github.com/Babe153/Agent01-from-Scratch/blob/7e4f5f82a1008d6276dfe1d6a97e68484665ecdd/src/Agent01/agents/search_agent.py).
- Basis: structural absence review.
- Confidence: high.
- Caveats: later versions or external wrappers could activate specialist research, but are outside frozen first-party path.

### Absence scope

- Surfaces inspected: planner prompts, graph routing, source-present search modules, provider selection, graph state fields and published README stage boundaries.
- Plausible first-party paths checked: future environmental surveillance, options/strategy development, capability investment/adaptation and closed feedback to current operators.
- Why no material first-party path remains: the reachable graph only executes a user-given present task; no prospective autonomous loop is wired.

## S5 — Policy and identity

- State: —
- Function: no legitimate ultimate organizational policy/identity decision and binding governance feedback loop is established.
- Disturbance / variety regulated: risky commands and file placement are restricted through deterministic workspace/path checks and a basic shell dangerous-pattern denylist.
- Decisive decision or feedback right: no agent or legitimate parent ratifies a changed constitutional mission/identity rule; user gives task and controls external model credentials.
- Decision owner: not established for S5; script guards and user-provided parameters retain narrow authority over individual tool effects.
- Supporting / enforcement mechanisms: workspace path resolver, command timeout/deny patterns, LangGraph retry count, hardcoded plan fallback and task report.
- Closure path: attempted tool operation → local validation/deny or allowed execution; no identity dispute → parent authorization → durable governing policy change.
- Why this is / is not agent-owned: a planner can form a task plan and tool guard code can block commands, but neither selects the organization's durable legitimate purpose.
- Evidence: [`tools/bash_tool.py`](https://github.com/Babe153/Agent01-from-Scratch/blob/7e4f5f82a1008d6276dfe1d6a97e68484665ecdd/src/Agent01/tools/bash_tool.py); [`tools/file_tools.py`](https://github.com/Babe153/Agent01-from-Scratch/blob/7e4f5f82a1008d6276dfe1d6a97e68484665ecdd/src/Agent01/tools/file_tools.py); [`cli/app.py`](https://github.com/Babe153/Agent01-from-Scratch/blob/7e4f5f82a1008d6276dfe1d6a97e68484665ecdd/src/Agent01/cli/app.py).
- Basis: structural absence review.
- Confidence: high.
- Caveats: README expressly disclaims a full OS sandbox; safety controls are narrower than identity-policy governance.

### Absence scope

- Surfaces inspected: CLI user authority, environment-based provider config, file/shell guards, planner goal, compiled graph, max-attempt policy and reporting.
- Plausible first-party paths checked: constitutional/mission decision authority, legitimate parent escalation, ratification of identity changes and durable governance feedback.
- Why no material first-party path remains: first-party decisions and deterministic checks concern one task and tool safety, not ultimate policy.

## Recursion

The shipped Stage 2 graph is one S1 with planning, execution, verification and finalization phases. Dormant `code_agent` and `search_agent` functions at this SHA do not create reachable child S1s; neither a second operating level nor S2/S3/S3*/S4/S5 organizational closure is evidenced.

## Variety and escalation

The planner/actor model calls and file/shell tools expand responses to varied coding goals. Workspace scoping, command deny patterns/timeouts, a fixed actor-loop/whole-attempt cap, structured Todos and direct verifier command output attenuate errors. A failed check triggers a new local plan or a final failure report; it does not trigger independent audit or higher-level management.

## Evidence gaps

Source-first static review of the frozen Stage 2 runnable graph; native provider-backed E2E was not run. The frozen ref does not include a tracked `tests/` directory, although README refers to external stage test checks. Unwired source modules and later README stages were excluded after verifying the exact tracked commit inventory and workflow imports. Model-generated acceptance/verification commands can omit task requirements, so command success is not proof of independent semantic validation.

## Assessment summary

Agent01 has a legitimate model-driven planner and tool-using actor that iteratively operate on real files, with deterministic command verification and bounded retry (**S1=A**). The actually runnable Stage 2 graph is serial; code and state placeholders for specialist agents are not wired. Its verifier runs producer-selected checks. Thus there is no established inter-S1 anti-interference, whole-current control, independent complementary audit, prospective environmental adaptation or identity-policy closure (**S2/S3/S3*/S4/S5=—**).

Proposed vector: **`A · — · — · — · — · —`**.

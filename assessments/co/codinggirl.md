---
harness_id: codinggirl
project_name: CodingGirl
repository: https://github.com/WEP-56/Coding_agent-Implementation-from-Scratch
review_ref: 4b4d32706b56697007e362ed9f257c0610a99e8b
reviewed_at: 2026-10-30
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

# CodingGirl

## Review boundary

- System in focus: CodingGirl's first-party Desktop coding product and Python agent core/distributed construction interfaces.
- Purpose and identity: observable, controllable repository coding through model-directed tools, event traces and recoverable local state.
- Relevant environment: user/operator, local repositories, model endpoints, Tauri/Rust host, Python process and optional adapters.
- Standard-distribution boundary: apps/desktop and codinggirl package; declared Python loop entry points, desktop native/provider loop and desktop-to-Python integration. Shipped construction interfaces are considered without assuming they are wired by default.
- Credited operating / distribution surfaces: Desktop run_model_tool_loop, Python AgentLoopWithSubagent, its desktop_agent_stream_cli entry and first-party tool registry/runner.
- Adjacent first-party surfaces excluded from ownership: .claude development agents, scripts/audit_repo.py, test/evaluation fixtures, documentation-generation/CI and future roadmaps. Repository co-location does not make these product regulators.
- First-party operating / deployment modes considered: recommended Tauri Desktop, native model tool loop, Desktop-launched Python backend, Python core loop and documented parallel-agent assembly, basic CLI scaffold and deterministic orchestrate command, Telegram adapter.
- Recursion level: one local coding session with optional exploratory workers.
- Reviewed revision: `4b4d32706b56697007e362ed9f257c0610a99e8b`.
- Observation date: 2026-10-30.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

[README](https://github.com/WEP-56/Coding_agent-Implementation-from-Scratch/blob/4b4d32706b56697007e362ed9f257c0610a99e8b/README.md) explicitly distinguishes the recommended React/Tauri Desktop from Python Core. Python's simple CLI run only records an MVP scaffold; the replace-goal orchestrator deterministically creates/checks/applies a patch and is not itself evidence of agentic S1. Actual model-directed operation is implemented separately: [Python loop](https://github.com/WEP-56/Coding_agent-Implementation-from-Scratch/blob/4b4d32706b56697007e362ed9f257c0610a99e8b/codinggirl/core/agent_loop_with_subagent.py#L126-L145) creates a model conversation, records events, invokes tools and returns results; [streaming backend](https://github.com/WEP-56/Coding_agent-Implementation-from-Scratch/blob/4b4d32706b56697007e362ed9f257c0610a99e8b/codinggirl/core/desktop_agent_stream_cli.py#L280-L332) builds that loop from real provider configuration. [Desktop process launch](https://github.com/WEP-56/Coding_agent-Implementation-from-Scratch/blob/4b4d32706b56697007e362ed9f257c0610a99e8b/apps/desktop/src-tauri/src/commands/python_agent.rs#L480-L520) connects the product to the Python module, while [native Rust loop](https://github.com/WEP-56/Coding_agent-Implementation-from-Scratch/blob/4b4d32706b56697007e362ed9f257c0610a99e8b/apps/desktop/src-tauri/src/commands/llm.rs#L487-L570) implements a second model/tool path.

SQLite/events, context compression, todo/task graphs, filesystem/index/search/patch/command tools and a default read-only SubagentRunner support operations. A documented ParallelAgentOrchestrator decomposes and batches exploratory tasks with fixed worker limits and dependency ordering. The shipped reviewer.py is a patch-format/size/sensitive-text predicate, not a separate model auditor. Desktop traces, approvals and replay views expose normal operational state; memory and skills preserve task context.

## Operational model

The model chooses coding/investigation actions and may delegate exploratory reads. The host enforces workspace/permission modes and persists events. Operators configure modes and approve concrete mutations. Read-only exploratory agents return summaries to the main model; they do not establish a whole-system controller, collision regulator or independent auditor merely through their number or separate conversations. Deterministic scaffold/orchestrator modes are explicitly distinguished from the model-backed product boundary.

## S1 — Operations

- State: A
- Function: repository investigation and code modification through a model/tool feedback loop.
- Disturbance / variety regulated: user goals, source contents, tool errors and partial task observations.
- Decisive decision or feedback right: choose the next tool, arguments, corrective work or final answer.
- Decision owner: model-backed parent coding agent; exploratory subagents own their narrower local read strategy.
- Supporting / enforcement mechanisms: tool schemas/runner, permission policy, workspace boundaries, SQLite/event stream and context management.
- Closure path: response tool calls execute through ToolRunner; formatted results are appended as role=tool messages before later model requests. Desktop native loop similarly keeps tool calls/results in its conversation.
- Boundary reachability: Desktop can invoke the supplied Python streaming module, which explicitly constructs and runs AgentLoopWithSubagent; this avoids borrowing autonomy from tests or the scaffold CLI.
- Why this is / is not agent-owned: model removal leaves storage/runners and the deterministic replacement workflow, but removes discretionary coding/investigation decisions.
- Evidence: [Model requests](https://github.com/WEP-56/Coding_agent-Implementation-from-Scratch/blob/4b4d32706b56697007e362ed9f257c0610a99e8b/codinggirl/core/agent_loop_with_subagent.py#L261-L315), [Action-result feedback](https://github.com/WEP-56/Coding_agent-Implementation-from-Scratch/blob/4b4d32706b56697007e362ed9f257c0610a99e8b/codinggirl/core/agent_loop_with_subagent.py#L355-L409), [Reachable construction](https://github.com/WEP-56/Coding_agent-Implementation-from-Scratch/blob/4b4d32706b56697007e362ed9f257c0610a99e8b/codinggirl/core/desktop_agent_stream_cli.py#L280-L332), [Desktop bridge](https://github.com/WEP-56/Coding_agent-Implementation-from-Scratch/blob/4b4d32706b56697007e362ed9f257c0610a99e8b/apps/desktop/src-tauri/src/commands/python_agent.rs#L480-L520).
- Basis: structural.
- Confidence: high for source availability.
- Caveats: no live provider or desktop build/run; the base CLI scaffold alone would not establish this state.

## S2 — Coordination

- State: —
- Function: no material first-party path established for this function at the declared session boundary.
- Disturbance / variety regulated: Independent-context research workers and dependency-ordered parallel tasks are available, but the reviewed modes do not identify a concrete inter-S1 conflict/oscillation regulated by a specific coordination response. Read-only workers do not collide by editing one shared checkout.
- Decisive decision or feedback right: A supplied interference-specific response and returned adjustment are not established; queue/dependency/priority fields alone do not satisfy the function.
- Decision owner: none established for this function; local model, developer and operator rights are not automatically metasystem rights.
- Supporting / enforcement mechanisms: tool execution, task state, traces, configuration and UI are support, not ownership evidence by themselves.
- Closure path: operational feedback is present; the function-specific returned regulation discussed above is absent.
- Why this is / is not agent-owned: the missing organizational relation is assessed before deciding whether an agent could own it.
- Evidence: [codinggirl/core/subagent_runner.py](https://github.com/WEP-56/Coding_agent-Implementation-from-Scratch/blob/4b4d32706b56697007e362ed9f257c0610a99e8b/codinggirl/core/subagent_runner.py#L25-L61), [codinggirl/core/parallel_tasks_tool.py](https://github.com/WEP-56/Coding_agent-Implementation-from-Scratch/blob/4b4d32706b56697007e362ed9f257c0610a99e8b/codinggirl/core/parallel_tasks_tool.py#L21-L102), [codinggirl/core/parallel_agent_orchestrator.py](https://github.com/WEP-56/Coding_agent-Implementation-from-Scratch/blob/4b4d32706b56697007e362ed9f257c0610a99e8b/codinggirl/core/parallel_agent_orchestrator.py#L332-L414).
- Basis: structural.
- Confidence: medium, bounded to the inspected supplied implementations.
- Caveats: documented extensibility/future development is not ruled out; no universal impossibility claim.

### Absence scope

- Surfaces inspected: parallel_tasks tool/orchestrator, task graph, default read-only worker tools, patch conflict handling and Desktop tool execution.
- Plausible first-party paths checked: concurrent read workers, dependency readiness, synthesis noting inconsistencies and patch fail-on-conflict.
- Why no material first-party path remains: The parallel path orders/decomposes work and reports summaries; generic synthesis mentions conflicts without a supplied feedback regulator of a specific inter-S1 disturbance. Patch conflicts are local action errors, not an established multi-writer coordination relation.

## S3 — Inside-and-now control

- State: —
- Function: no material first-party path established for this function at the declared session boundary.
- Disturbance / variety regulated: Todo/task progress, event projections and fixed max_parallel_agents/max_iterations expose local task state. Model decomposition and synthesis assign parts of one goal; the reviewed routes do not establish live whole-system resource bargaining/intervention.
- Decisive decision or feedback right: No decisive whole-system current-control actor or qualifying parent-return loop is established.
- Decision owner: none established for this function; local model, developer and operator rights are not automatically metasystem rights.
- Supporting / enforcement mechanisms: tool execution, task state, traces, configuration and UI are support, not ownership evidence by themselves.
- Closure path: operational feedback is present; the function-specific returned regulation discussed above is absent.
- Why this is / is not agent-owned: the missing organizational relation is assessed before deciding whether an agent could own it.
- Evidence: [codinggirl/core/parallel_agent_orchestrator.py](https://github.com/WEP-56/Coding_agent-Implementation-from-Scratch/blob/4b4d32706b56697007e362ed9f257c0610a99e8b/codinggirl/core/parallel_agent_orchestrator.py#L332-L414), [codinggirl/core/agent_loop_with_subagent.py](https://github.com/WEP-56/Coding_agent-Implementation-from-Scratch/blob/4b4d32706b56697007e362ed9f257c0610a99e8b/codinggirl/core/agent_loop_with_subagent.py#L29-L42), [apps/desktop/src-tauri/src/commands/python_agent.rs](https://github.com/WEP-56/Coding_agent-Implementation-from-Scratch/blob/4b4d32706b56697007e362ed9f257c0610a99e8b/apps/desktop/src-tauri/src/commands/python_agent.rs#L25-L62).
- Basis: structural.
- Confidence: medium, bounded to the inspected supplied implementations.
- Caveats: documented extensibility/future development is not ruled out; no universal impossibility claim.

### Absence scope

- Surfaces inspected: Python task/parallel/background mechanisms, Desktop traces/run control and approvals, policy and context counters.
- Plausible first-party paths checked: priority fields, fixed concurrency, parent task delegation, operator stop/approval and progress dashboards.
- Why no material first-party path remains: These are operational planning/status, preselected scheduling and local action control. No function-specific whole-system resource/commitment decision plus returned regulation is supplied; a generic UI stop or mutation approval does not justify P.

## S3* — Complementary audit

- State: —
- Function: no material first-party path established for this function at the declared session boundary.
- Disturbance / variety regulated: Super Trace and replay project the producer's normal events. reviewer.py checks unified-diff markers, line count and sensitive-looking text in the ordinary deterministic replacement pipeline. Generic read-only subagents gather source information; code-review skill text is not wired as a distinct audit owner.
- Decisive decision or feedback right: No shipped complementary audit judgment/independence/returned-control relation is established for the operational claims.
- Decision owner: none established for this function; local model, developer and operator rights are not automatically metasystem rights.
- Supporting / enforcement mechanisms: tool execution, task state, traces, configuration and UI are support, not ownership evidence by themselves.
- Closure path: operational feedback is present; the function-specific returned regulation discussed above is absent.
- Why this is / is not agent-owned: the missing organizational relation is assessed before deciding whether an agent could own it.
- Evidence: [codinggirl/core/reviewer.py](https://github.com/WEP-56/Coding_agent-Implementation-from-Scratch/blob/4b4d32706b56697007e362ed9f257c0610a99e8b/codinggirl/core/reviewer.py#L13-L33), [codinggirl/core/orchestrator.py](https://github.com/WEP-56/Coding_agent-Implementation-from-Scratch/blob/4b4d32706b56697007e362ed9f257c0610a99e8b/codinggirl/core/orchestrator.py#L57-L90), [codinggirl/core/task_tool.py](https://github.com/WEP-56/Coding_agent-Implementation-from-Scratch/blob/4b4d32706b56697007e362ed9f257c0610a99e8b/codinggirl/core/task_tool.py), [skills/code-review.md](https://github.com/WEP-56/Coding_agent-Implementation-from-Scratch/blob/4b4d32706b56697007e362ed9f257c0610a99e8b/skills/code-review.md).
- Basis: structural.
- Confidence: medium, bounded to the inspected supplied implementations.
- Caveats: documented extensibility/future development is not ruled out; no universal impossibility claim.

### Absence scope

- Surfaces inspected: reviewer/orchestrator, code-review skill, task/subagent definitions, event storage/replay and adjacent repository audit scripts.
- Plausible first-party paths checked: independent subagent context, patch review predicate, trace/replay and developer audit files.
- Why no material first-party path remains: The source-specific reviewer is a routine producer gate; generic exploration and checklists do not intentionally close independent audit. Adjacent development scripts are outside the installed product. Separate contexts alone are insufficient.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party path established for this function at the declared session boundary.
- Disturbance / variety regulated: Context compaction, seed memories, skill loading, research subtasks and repository indexing support present coding work. Public evolution/optimization plans concern the development project rather than an installed adaptation loop.
- Decisive decision or feedback right: No external/future adaptation-option decision returning into current capability is established.
- Decision owner: none established for this function; local model, developer and operator rights are not automatically metasystem rights.
- Supporting / enforcement mechanisms: tool execution, task state, traces, configuration and UI are support, not ownership evidence by themselves.
- Closure path: operational feedback is present; the function-specific returned regulation discussed above is absent.
- Why this is / is not agent-owned: the missing organizational relation is assessed before deciding whether an agent could own it.
- Evidence: [codinggirl/core/desktop_agent_stream_cli.py](https://github.com/WEP-56/Coding_agent-Implementation-from-Scratch/blob/4b4d32706b56697007e362ed9f257c0610a99e8b/codinggirl/core/desktop_agent_stream_cli.py#L296-L315), [codinggirl/core/agent_loop_with_subagent.py](https://github.com/WEP-56/Coding_agent-Implementation-from-Scratch/blob/4b4d32706b56697007e362ed9f257c0610a99e8b/codinggirl/core/agent_loop_with_subagent.py#L205-L248), [codinggirl/core/task_tool.py](https://github.com/WEP-56/Coding_agent-Implementation-from-Scratch/blob/4b4d32706b56697007e362ed9f257c0610a99e8b/codinggirl/core/task_tool.py).
- Basis: structural.
- Confidence: medium, bounded to the inspected supplied implementations.
- Caveats: documented extensibility/future development is not ruled out; no universal impossibility claim.

### Absence scope

- Surfaces inspected: context/memory/skill systems, Desktop Python prompt assembly, core task tool and public plans.
- Plausible first-party paths checked: research delegation, compression, memory loading, provider settings and maintainer roadmap.
- Why no material first-party path remains: Inspected paths assemble or recover current-task context; they do not supply the distinct outside-and-then model, adaptation judgment and feedback into current capability. Contributor plans and human ideas are adjacent, not a parent S4 mode.

## S5 — Policy and identity

- State: —
- Function: no material first-party path established for this function at the declared session boundary.
- Disturbance / variety regulated: Permission modes and Desktop action approvals bound filesystem/command mutations. Static prompt/style/memory settings express constraints; no identity-level or ultimate-policy matter is routed to an authority and returned.
- Decisive decision or feedback right: No identity/ultimate-policy decision owner and return-to-operation path is established.
- Decision owner: none established for this function; local model, developer and operator rights are not automatically metasystem rights.
- Supporting / enforcement mechanisms: tool execution, task state, traces, configuration and UI are support, not ownership evidence by themselves.
- Closure path: operational feedback is present; the function-specific returned regulation discussed above is absent.
- Why this is / is not agent-owned: the missing organizational relation is assessed before deciding whether an agent could own it.
- Evidence: [codinggirl/core/policy.py](https://github.com/WEP-56/Coding_agent-Implementation-from-Scratch/blob/4b4d32706b56697007e362ed9f257c0610a99e8b/codinggirl/core/policy.py#L6-L28), [apps/desktop/src-tauri/src/commands/policy.rs](https://github.com/WEP-56/Coding_agent-Implementation-from-Scratch/blob/4b4d32706b56697007e362ed9f257c0610a99e8b/apps/desktop/src-tauri/src/commands/policy.rs#L536-L607), [codinggirl/core/desktop_agent_stream_cli.py](https://github.com/WEP-56/Coding_agent-Implementation-from-Scratch/blob/4b4d32706b56697007e362ed9f257c0610a99e8b/codinggirl/core/desktop_agent_stream_cli.py#L293-L315).
- Basis: structural.
- Confidence: medium, bounded to the inspected supplied implementations.
- Caveats: documented extensibility/future development is not ruled out; no universal impossibility claim.

### Absence scope

- Surfaces inspected: core PermissionPolicy, Desktop policy/approval handlers, provider/style settings and contribution guidance.
- Plausible first-party paths checked: write/exec modes, mutation approval/replay, local control and project development rules.
- Why no material first-party path remains: All identified returns concern operational permissions or task/context settings. They do not establish ultimate-policy tension resolution at the session recursion; neither generic human approval nor multiple contributors creates P.

## Distributed OSS parent arrangement

Public contributor guidance and development agents are outside the installed coding session. Local users legitimately control their work; no project-level parent S3/S4/S5 closure is imported from OSS collaboration.

## Self-hosted and non-human modes

The Desktop native and Python-backed modes, Python library/CLI and documented parallel constructor were inspected. Generic operator approval/stop/configuration do not add P. The deterministic replacement orchestrator is not substituted for the model-backed mode.

## Recursion

Task IDs, background processes, separate histories and nested subagents demonstrate decomposition. Their local environments and complete metasystems are not established as recursively viable systems.

## Variety and escalation

Tool failures, policy denials, context health and run events are persisted/projected to the operator. Bounded loops and reported errors permit local recovery; traces/statuses alone do not prove an algedonic channel or a higher-function decision owner.

## Evidence gaps

Pinned Git clone stalled; the exact frozen SHA was recovered through the first-party GitHub tarball endpoint without repinning. Python source compileall and 35 selected native policy/workspace/patch/task-graph/state/context tests passed. No provider-backed agent E2E, Tauri build, UI run or performance experiment was executed. README roadmap/completeness claims are not treated as proof of installed functionality. Optional parallel assembly is credited only for paths actually present, not assumed default wiring.

---
harness_id: waveloom
project_name: Waveloom
repository: https://github.com/Menfre01/waveloom
review_ref: daccab5d4816803a82eb6eabfe44a68c75bc1f58
reviewed_at: 2026-10-07
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Waveloom

## Review boundary

- System in focus: the shipped Waveloom terminal coding-agent runtime at the frozen revision, including its first-party Think-Act-Observe loop, built-in coding tools, permission/sandbox path, session/todo state, subagent tool, background-task lifecycle, hooks, and TUI/ACP entry points that instantiate those components.
- Purpose and identity: a local coding agent that autonomously inspects and changes a user-selected codebase, runs commands/tests, delegates bounded work to first-party subagents, and returns results to the user.
- Relevant environment: the current workspace, local shell/filesystem, configured model/provider, optional MCP servers, project/global configuration, and local user approval surface.
- Standard-distribution boundary: Waveloom repository code and shipped prompts/configuration. Model providers, MCP servers, OS sandbox primitives, and external skills/tools are dependencies rather than owners of credited VSM functions.
- Credited operating / distribution surfaces: `pkg/agentloop`, `pkg/subagent`, first-party built-in tools, permission/sandbox/session/todo/task/hook runtime, `pkg/prompt/default.md`, and supported TUI/ACP entry points that directly instantiate those mechanisms.
- Adjacent first-party surfaces excluded from ownership: repository CI/release machinery, eval/experiments, documentation-only comparisons, and external MCP/provider/skill behavior except where shipped runtime wiring makes a first-party decision path reachable.
- First-party modes considered: interactive TUI and non-interactive ACP paths where the same agent loop and registered tools are instantiated; normal permission mode; optional sandbox/bypass mode; fork/cold subagents; background shell tasks; plan mode.
- Recursion level: one Waveloom coding session as the viable system, with delegated fork/cold subagents treated as subordinate operational units when their work is coordinated by the parent agent.
- Reviewed revision: `daccab5d4816803a82eb6eabfe44a68c75bc1f58`.
- Observation date: 2026-10-07.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

Waveloom implements a persistent Go coding-agent loop that repeatedly calls an LLM, executes selected tools, feeds results back into context, tracks errors/todos, compacts context, and terminates on completion or bounded stop conditions. Built-in write/edit/shell tools can modify and test the workspace; permissions and an optional OS sandbox constrain those actions.

The first-party `agent` tool is model-visible and `ConcurrentSafe`. It can launch context-inheriting fork agents or cold `Explore`, `evaluate`, and `verification` agents. Fork agents receive a writable tool registry; cold agents remove project write/edit tools and use read-only shell semantics. The parent loop injects parent messages/tool schemas into the subagent execution context, and each subagent's final output is returned as the `agent` tool result, permanently entering the parent context.

The shipped system prompt directs the parent agent to parallelize genuinely independent delegated work, keep dependent work sequential, use one subagent per competing investigation path, and manage subagent lifecycle through the parent todo list. Multiple `agent` calls issued in one response can therefore run concurrently. This provides an agent-owned coordination path over subordinate S1 work rather than mere runtime parallelism.

Cold `evaluate` and `verification` agents provide a complementary review path. They start without the parent conversation history, cannot edit project files, inspect/test the workspace independently, and return an assessment or explicit verification verdict to the parent. The default prompt instructs the parent to use these after substantial changes, so findings are returned to the operating agent before it claims completion.

Primary evidence:
- [main agent loop](https://github.com/Menfre01/waveloom/blob/daccab5d4816803a82eb6eabfe44a68c75bc1f58/pkg/agentloop/loop.go)
- [tool execution / nested-agent context wiring](https://github.com/Menfre01/waveloom/blob/daccab5d4816803a82eb6eabfe44a68c75bc1f58/pkg/agentloop/execute.go)
- [subagent implementation](https://github.com/Menfre01/waveloom/blob/daccab5d4816803a82eb6eabfe44a68c75bc1f58/pkg/subagent/agent.go)
- [shipped system prompt](https://github.com/Menfre01/waveloom/blob/daccab5d4816803a82eb6eabfe44a68c75bc1f58/pkg/prompt/default.md)
- [background shell execution](https://github.com/Menfre01/waveloom/blob/daccab5d4816803a82eb6eabfe44a68c75bc1f58/pkg/tool/shell.go)
- [permission guard contract](https://github.com/Menfre01/waveloom/blob/daccab5d4816803a82eb6eabfe44a68c75bc1f58/pkg/permission/types.go)
- [session persistence](https://github.com/Menfre01/waveloom/blob/daccab5d4816803a82eb6eabfe44a68c75bc1f58/pkg/session/session_persist.go)
- [README](https://github.com/Menfre01/waveloom/blob/daccab5d4816803a82eb6eabfe44a68c75bc1f58/README.md)

## Operational model

The parent coding agent owns the main operational decision loop. It decides which enabled tool to call, interprets returned results, revises its approach, and can delegate scoped work through the first-party `agent` tool.

Fork agents are subordinate writable S1 units. The parent decides which tasks are independent enough to run in parallel and which dependency-bearing tasks must remain serial. Their final results return as ordinary tool results to the parent, which continues the main coding operation. Cold Explore/evaluate/verification agents are narrower read-only subordinate units.

The permission guard, sandbox, hook runner, background-task registry, todo store, compactor, session persistence, and execution limits enforce or support agent decisions. Human approval can be required for particular actions, but ordinary operational ownership remains with the model loop in supported modes where actions are allowed by policy or sandbox.

## S1 — Operations

- State: A
- Function: perform coding work by inspecting the workspace, editing/writing files, running commands/tests, using external information tools, and iterating from tool results toward task completion.
- Disturbance / variety regulated: uncertainty in source state, task requirements, tool/test results, errors, and evolving conversation/workspace context.
- Decisive decision or feedback right: choose the next tool/action, interpret results, retry/change strategy, delegate work, and decide when the requested operation is complete.
- Decision owner: the parent Waveloom coding agent; delegated fork agents can own bounded subordinate operational work.
- Supporting / enforcement mechanisms: Think-Act-Observe loop, tool registry, permission guard, sandbox, hooks, todo reminders, context compaction, session persistence, error backoff, background-task notifications.
- Closure path: user request → model decision → first-party tool/subagent action → returned result/event → next model decision → further action or terminal response.
- Boundary reachability: the shipped loop directly registers/executes first-party coding tools and receives their outputs; the supported agent tool creates nested first-party loops from that same runtime.
- Why this is / is not agent-owned: the model chooses and sequences operational actions from available tools and changes behavior from observed results. Deterministic runtime layers execute and constrain those choices rather than replacing the discretionary operation.
- Evidence: [pkg/agentloop/loop.go](https://github.com/Menfre01/waveloom/blob/daccab5d4816803a82eb6eabfe44a68c75bc1f58/pkg/agentloop/loop.go), [pkg/agentloop/execute.go](https://github.com/Menfre01/waveloom/blob/daccab5d4816803a82eb6eabfe44a68c75bc1f58/pkg/agentloop/execute.go), [pkg/prompt/default.md](https://github.com/Menfre01/waveloom/blob/daccab5d4816803a82eb6eabfe44a68c75bc1f58/pkg/prompt/default.md).
- Basis: structural + explicit.
- Confidence: high.
- Caveats: individual write/execute actions may require human approval depending on active permission policy.

## S2 — Coordination

- State: A
- Function: attenuate interference among distinct delegated S1 units by deciding which work can safely proceed in parallel and which dependency-bearing work must remain serial, then reintegrating subordinate results into the parent operation.
- Disturbance / variety regulated: conflicting/dependent delegated work, including the risk that tasks with ordering dependencies or overlapping operational scope execute concurrently and invalidate one another's assumptions/results.
- Decisive decision or feedback right: the parent agent chooses subtask boundaries, selects parallel versus serial execution, launches multiple first-party agents together for independent work, and consumes their returned results before continuing dependent work.
- Decision owner: the parent Waveloom agent.
- Supporting / enforcement mechanisms: `agent` tool marked `ConcurrentSafe`; fork/cold subagent construction; parent todo lifecycle; returned tool results; system-prompt coordination rules.
- Distinct S1 units: first-party fork/cold subagents instantiated as separate model-backed operational loops under one parent session.
- Inter-S1 disturbance: dependency-bearing delegated work can invalidate assumptions or duplicate/conflict with peer work if run concurrently; writable fork work also creates concrete shared-workspace collision risk when scopes are not independent.
- Attenuating coordination relation: the parent agent is instructed to partition independent work into parallel agent calls and keep dependent work sequential, with scoped prompts and parent-managed task lifecycle.
- Feedback into subsequent S1 behaviour: each subagent's final result is returned as a parent `agent` tool result; the parent then updates task status and uses those results to decide dependent follow-up, repair, or completion.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the parallel-versus-serial decision is explicitly tied to whether subordinate S1 work is independent or dependency-constrained, regulating concrete interference among concurrently viable operational units rather than merely transporting prompts.
- Closure path: parent identifies independent/dependent subtasks → launches independent agent calls together or serializes dependent work → subordinate S1 units execute → each final result returns as a tool result → parent updates task state and decides subsequent work.
- Boundary reachability: the coordination policy is in the shipped default system prompt and the model-visible first-party `agent` tool implements concurrent subordinate execution.
- Why this is / is not agent-owned: the runtime can execute concurrent tool calls, but it does not decide which work is independent or dependency-constrained. That discretionary partitioning/ordering right is assigned to the parent model.
- Evidence: [pkg/prompt/default.md](https://github.com/Menfre01/waveloom/blob/daccab5d4816803a82eb6eabfe44a68c75bc1f58/pkg/prompt/default.md), [pkg/subagent/agent.go](https://github.com/Menfre01/waveloom/blob/daccab5d4816803a82eb6eabfe44a68c75bc1f58/pkg/subagent/agent.go), [pkg/agentloop/execute.go](https://github.com/Menfre01/waveloom/blob/daccab5d4816803a82eb6eabfe44a68c75bc1f58/pkg/agentloop/execute.go).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: generic concurrent tools do not count by themselves; the positive mapping depends on the shipped agent-owned dependency/parallelization policy plus subordinate-agent return path.

## S3 — Inside-and-now control

- State: —
- Function: no sufficiently complete whole-current control loop over all active operational units/resources/commitments is established.
- Disturbance / variety regulated: not established as an S3 disturbance at this recursion.
- Decisive decision or feedback right: none meeting S3 closure.
- Decision owner: none established.
- Supporting / enforcement mechanisms: todo list/status, step/error limits, background-task registry/kill tool, permission/sandbox state, subagent events shown to the TUI, session statistics.
- Closure path: not applicable.
- Boundary reachability: no positive S3 path claimed.
- Why this is / is not agent-owned: the parent can plan/delegate and later consume subagent results, but subagent execution is a synchronous tool boundary from the parent's perspective; streamed subagent events are routed for UI visibility rather than exposed as a whole-current model control surface with live steer/kill/reprioritize rights across subordinate agents. Background shell tasks have a kill path, but they are tool processes rather than a whole-system S1 control plane.
- Evidence: [pkg/subagent/agent.go](https://github.com/Menfre01/waveloom/blob/daccab5d4816803a82eb6eabfe44a68c75bc1f58/pkg/subagent/agent.go), [pkg/tool/kill_background_task.go](https://github.com/Menfre01/waveloom/blob/daccab5d4816803a82eb6eabfe44a68c75bc1f58/pkg/tool/kill_background_task.go), [pkg/session/session_persist.go](https://github.com/Menfre01/waveloom/blob/daccab5d4816803a82eb6eabfe44a68c75bc1f58/pkg/session/session_persist.go).
- Basis: structural.
- Confidence: high.
- Caveats: todo/task tracking supports coordination and persistence, but task labels/status alone are not whole-current S3 control.

### Absence scope

- Surfaces inspected: main loop, tool execution, subagent implementation/events, todo/task/background execution, session persistence, permission/sandbox paths, system prompt, TUI-facing subagent event flow.
- Plausible first-party paths checked: parent todo lifecycle, parallel agent calls, subagent progress events, background shell task registry and kill tool, error/step limits, plan mode.
- Why no material first-party path remains: no model-owned current-state view plus live intervention path over the active subordinate agent set is wired; runtime counters/registries and human/TUI visibility do not supply the missing discretionary control loop.

## S3* — Complementary audit

- State: A
- Function: independently review or adversarially verify the focal coding operation using fresh-context read-only agents and return findings to the operating parent.
- Disturbance / variety regulated: false confidence, regressions, security defects, test/build failures, and implementation mistakes that the focal coding path may overlook.
- Decisive decision or feedback right: a cold `evaluate` or `verification` agent independently inspects/tests the repository and produces an assessment or PASS/FAIL verdict; the parent receives that output and decides corrective follow-up before completion.
- Decision owner: the cold review/verification agent owns the audit judgment; the parent agent owns subsequent operational correction.
- Supporting / enforcement mechanisms: cold context construction, project-write tools removed from the cold registry, read-only subagent shell, dedicated evaluate/verification prompts, returned `agent` tool result, subagent transcript/events.
- Claim being audited: the parent coding agent's claim that a substantive implementation/change is correct and ready to report as complete.
- Ordinary reporting path: the parent agent's own tool results, implementation reasoning, local build/test attempts, and completion narrative.
- Complementary access path: a separate cold evaluate/verification model directly reads the repository and, for verification, runs builds/tests/adversarial checks under a read-only project boundary.
- Independence boundary: fresh cold model context without inherited parent conversation, project write/edit tools removed, dedicated review/verification instructions, and an explicit independent assessment or PASS/FAIL verdict returned to the parent.
- Who acts on findings: the parent coding agent receives the review/verdict as a tool result and is instructed to repair failed verification or re-check before claiming completion.
- Closure path: parent coding work/change → parent invokes cold evaluate/verification → fresh agent directly inspects repository and/or runs tests/adversarial checks → review/verdict returned as parent tool result → parent context incorporates finding → parent can fix/re-verify or report completion.
- Boundary reachability: evaluate/verification are accepted values of the shipped model-visible `agent` tool; their registries and dedicated prompts are constructed in first-party code.
- Why this is / is not agent-owned: the audit conclusion is generated by a distinct cold model invocation with direct evidence access, not by deterministic logging or the same parent reasoning trace.
- Evidence: [pkg/subagent/agent.go](https://github.com/Menfre01/waveloom/blob/daccab5d4816803a82eb6eabfe44a68c75bc1f58/pkg/subagent/agent.go), [pkg/prompt/default.md](https://github.com/Menfre01/waveloom/blob/daccab5d4816803a82eb6eabfe44a68c75bc1f58/pkg/prompt/default.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: this is a supported agent-invoked audit mode, not a guarantee that every coding turn always invokes it.

## S4 — Outside-and-then intelligence

- State: —
- Function: no complete first-party external/future adaptation loop is established.
- Disturbance / variety regulated: not established as S4.
- Decisive decision or feedback right: none for S4.
- Decision owner: none established.
- Supporting / enforcement mechanisms: web tools, AGENTS.md/project memory, skills/plugins, provider/model configuration, compaction, session persistence, environment probing.
- Closure path: not applicable.
- Boundary reachability: no positive S4 path claimed.
- Why this is / is not agent-owned: external information can be gathered for a current coding task, and configuration can change available capability, but there is no first-party loop that scans the external/future environment, generates adaptation options, selects an adaptation, and changes the harness's continuing capability/policy.
- Evidence: [pkg/prompt/default.md](https://github.com/Menfre01/waveloom/blob/daccab5d4816803a82eb6eabfe44a68c75bc1f58/pkg/prompt/default.md), [README.md](https://github.com/Menfre01/waveloom/blob/daccab5d4816803a82eb6eabfe44a68c75bc1f58/README.md).
- Basis: structural.
- Confidence: high.
- Caveats: web research for the current task remains S1 support unless it closes prospective adaptation.

### Absence scope

- Surfaces inspected: web/tool path, memory/session/compaction, skills/plugins, environment/model selection, subagents, plan mode, README/configuration.
- Plausible first-party paths checked: model auto-selection, skills, persistent memory, external web research, environment detection, compaction, plan generation.
- Why no material first-party path remains: these mechanisms support current work or operator-selected capability; none closes the required prospective adaptation decision and return into continuing system capability.

## S5 — Policy and identity

- State: —
- Function: no runtime first-party identity/ultimate-policy governance loop is established.
- Disturbance / variety regulated: not established as S5.
- Decisive decision or feedback right: none for S5.
- Decision owner: none established.
- Supporting / enforcement mechanisms: system prompt, permission rules, sandbox policy, plan approval, hooks, configuration, bypass mode, user approval dialogs.
- Closure path: not applicable.
- Boundary reachability: no positive S5 path claimed.
- Why this is / is not agent-owned: these surfaces constrain or authorize individual actions and modes; they do not frame identity/ultimate-policy questions, route them to a legitimate S5 authority, and return authoritative governance decisions into subsequent operation.
- Evidence: [pkg/permission/types.go](https://github.com/Menfre01/waveloom/blob/daccab5d4816803a82eb6eabfe44a68c75bc1f58/pkg/permission/types.go), [pkg/agentloop/loop.go](https://github.com/Menfre01/waveloom/blob/daccab5d4816803a82eb6eabfe44a68c75bc1f58/pkg/agentloop/loop.go), [README.md](https://github.com/Menfre01/waveloom/blob/daccab5d4816803a82eb6eabfe44a68c75bc1f58/README.md).
- Basis: structural.
- Confidence: high.
- Caveats: user plan approval and tool permission approval are operational governance boundaries, not S5 merely because a human is authoritative over an action.

### Absence scope

- Surfaces inspected: system prompt, permission guard/rules, sandbox, plan mode, hooks, configuration, model/provider selection, session lifecycle.
- Plausible first-party paths checked: approval gates, permission rules, sandbox policy, plan approval, bypass mode, configuration.
- Why no material first-party path remains: no identity/ultimate-policy decision cycle with return-to-operation governance closure is implemented.

## Distributed OSS parent arrangement

Repository maintainer governance is external to the assessed runtime. No operating session routes S3/S4/S5 matters into project governance and receives authoritative decisions back into that same runtime, so no parent-mode notation is inferred.

## Recursion

The parent coding session is the system-in-focus. Fork/cold subagents are subordinate operational units instantiated inside it. They can be coordinated as S1 units and, for cold evaluate/verification, provide an independent S3* audit path; they are not independently credited with their own full metasystem.

## Variety and escalation

The parent agent absorbs coding-task variety through direct tools, parallel/serial delegation, error-driven strategy changes, and returned subordinate findings. Permission/sandbox enforcement can interrupt unsafe actions for user approval. Background shell work returns task IDs and later completion notifications; the parent can inspect or kill such processes. These mechanisms improve operational resilience but do not by themselves create S3, S4, or S5.

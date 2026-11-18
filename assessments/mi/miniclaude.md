---
harness_id: miniclaude
project_name: MiniClaude
repository: https://github.com/zmylol/MiniClaude
review_ref: 186ccb09f485aab9c5b60c8b7cc92351898de363
reviewed_at: 2026-11-18
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# MiniClaude

## Review boundary

- System in focus: An installed local MiniClaude mini-core process and its first-party AgentRunner/AgentLoop, with sessions, configured model provider, tools, subagents, permissions and clients.
- Purpose and identity: Execute user-specified project work with model-directed file, shell, search and delegated tool operations and persist session results.
- Relevant environment: Project workspace, model-provider responses, tool returns, permission decisions, model limits and supported network/MCP integrations.
- Standard-distribution boundary: Bundled Python mini-core, CLI/TUI and desktop/web clients, shipped builtin tools/subagent loop, local session/task stores and permission manager. Provider inference is external; it does not supply undistributed whole-system regulatory functions.
- Credited operating / distribution surfaces: Core AgentRunner/AgentLoop, model-backed interactive/one-shot runs, first-party subagent invocation, permission requests, session/trace stores and built-in task commands.
- Adjacent first-party surfaces excluded from ownership: Repository tests, developer CI/release, protocol-doc generation, experimental constraint-memory evaluation and prospective roadmap items; external MCP servers and model host governance are not credited as MiniClaude metasystem owners.
- First-party operating / deployment modes considered: Local authenticated model-backed mini-core through CLI, TUI and desktop, with optional enabled network and model-delegated subagents, attended permission requests and persistent policy options.
- Recursion level: One MiniClaude runtime serving local project-task sessions; individual subagents can execute task fragments but do not by themselves imply a second self-governing organization.
- Reviewed revision: 186ccb09f485aab9c5b60c8b7cc92351898de363.
- Observation date: 2026-11-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

Mini-core provides session/run commands and the event transport for multiple clients. AgentRunner configures a model provider, runtime tool registry, persistent session context, task file storage, browser/MCP tools when enabled, child registry, and permission manager. AgentLoop repeatedly sends context and schemas to the configured LLM, executes emitted tool calls through checked first-party invokers, feeds tool results into the next turn, and terminates on final output or a bounded error. Child model loops can run foreground or background and return via agent_result; role profiles and tool whitelists constrain their scope. Per-call approval can defer tool execution until a human replies, with optional remembered grants. Trace/event log and compaction are support and recovery, not independent VSM audits or external-policy learning.

## Operational model

Operational S1 is the model-driven agent loop making substantive task and tool choices against the workspace and feeding results into subsequent model turns. Its optional child loops each execute allocated tasks under the same host permissions. The task list records dependencies and statuses, and the runtime can launch concurrent independent tool calls; there is no demonstrated first-party arbitration of a concrete interfering pair of S1 operations as a separately closing S2 relationship. Session-level permissions and cancel/stop are direct safety constraints and user assistance rather than independently demonstrated organization-wide current control, future adaptation or ultimate identity-policy closure.

## S1 — Operations

- State: A
- Function: Perform assigned project tasks by model-selected tool calls and evaluate returned effects.
- Disturbance / variety regulated: Open-ended user requests and changing file, shell, search and tool outputs.
- Decisive decision or feedback right: Select the next tool and its arguments, choose whether to delegate and determine when the goal is achieved in response to observed tool results.
- Decision owner: The configured model-driven MiniClaude agent operating through the first-party AgentLoop; deterministic runtime implements and constrains the choice.
- Supporting / enforcement mechanisms: Registry, permission manager, run/session store, provider connector, max-step limit, task files and event writer.
- Closure path: Response tool calls are executed, outcomes appended to conversation context, next model decision consumes them; final result and session state are persisted.
- Boundary reachability: The shipped local mini-core creates AgentRunner with configured model and tools; CLI, TUI and desktop initiate runs without requiring a developer-only test harness.
- Why this is / is not agent-owned: In successful model-backed runs, the model chooses task-substantive actions while the host only checks, executes and returns feedback.
- Evidence: [runner model/tool wiring](https://github.com/zmylol/MiniClaude/blob/186ccb09f485aab9c5b60c8b7cc92351898de363/src/mini_claude/core/runner.py#L258-L299), [model choice, execution, feedback and completion](https://github.com/zmylol/MiniClaude/blob/186ccb09f485aab9c5b60c8b7cc92351898de363/src/mini_claude/core/loop.py#L70-L225), [child invocation](https://github.com/zmylol/MiniClaude/blob/186ccb09f485aab9c5b60c8b7cc92351898de363/src/mini_claude/core/subagent/tool.py#L114-L209), [supported entry](https://github.com/zmylol/MiniClaude/blob/186ccb09f485aab9c5b60c8b7cc92351898de363/README.md).
- Basis: structural
- Confidence: high
- Caveats: Structural source assessment; no paid model-provider live run was conducted. The host and user reserve tool access, not the task-substantive choice.

## S2 — Coordination

- State: —
- Function: The inspected distribution supplies child/task sequencing and reporting but no evidenced distinct-S1 conflict-attenuation loop.
- Disturbance / variety regulated: Two child agents could compete for a file, tool resource or dependency under concurrent work.
- Decisive decision or feedback right: A controller would have to detect inter-child collision, select a coordination response and return it to future child behavior.
- Decision owner: Task authors/agent may sequence tasks; no distinct S2 interference decision owner was established.
- Supporting / enforcement mechanisms: TaskManager blocked_by, subagent registry, depth limit, independent-call guidance and returned child statuses.
- Closure path: Task dependencies and completion are recorded, but no conflicting live S1 units are identified and attenuated through a separate evidenced relationship.
- Why this is / is not agent-owned: Task dependencies and background child results alone do not establish a concrete conflict/oscillation witness or S2-specific decision and feedback path.
- Evidence: [task dependency storage](https://github.com/zmylol/MiniClaude/blob/186ccb09f485aab9c5b60c8b7cc92351898de363/src/mini_claude/core/task/manager.py#L43-L126), [child registry and result](https://github.com/zmylol/MiniClaude/blob/186ccb09f485aab9c5b60c8b7cc92351898de363/src/mini_claude/core/subagent/tool.py#L114-L209), [concurrency loop](https://github.com/zmylol/MiniClaude/blob/186ccb09f485aab9c5b60c8b7cc92351898de363/src/mini_claude/core/loop.py#L157-L180)
- Basis: structural
- Confidence: medium
- Caveats: This does not claim that task-specific custom user composition cannot add coordination.

### Absence scope

- Surfaces inspected: Agent loop, builtin task tools, child tool/registry, local sessions and README.
- Plausible first-party paths checked: TaskManager dependency clearing, spawn_agent, child status, concurrent-call policy, approval gates.
- Why no material first-party path remains: Task dependencies and background child results alone do not establish a concrete conflict/oscillation witness or S2-specific decision and feedback path.

## S3 — Inside-and-now control

- State: —
- Function: No evidenced current whole-runtime control function coordinating live S1 resources, commitments or priorities beyond individual task handling.
- Disturbance / variety regulated: Sessions or child runs can overlap, consume resources or require intervention.
- Decisive decision or feedback right: A current controller would require a whole-system state view and substantive priority/resource intervention with feedback.
- Decision owner: User owns per-tool approvals and stop requests; model owns local task choices, not a demonstrably separate global controller.
- Supporting / enforcement mechanisms: Session mode permission constraints, task registry, cancel, runtime caps and local task-status storage.
- Closure path: Approval resumes or denies one tool; stop cancels a session; no demonstrated whole-runtime resource allocation decision closes.
- Why this is / is not agent-owned: Permission enforcement and session control are not, by themselves, an S3 decision over current multiple S1 commitments.
- Evidence: [tool approval return](https://github.com/zmylol/MiniClaude/blob/186ccb09f485aab9c5b60c8b7cc92351898de363/src/mini_claude/core/permissions/manager.py#L99-L211), [runner cancellation](https://github.com/zmylol/MiniClaude/blob/186ccb09f485aab9c5b60c8b7cc92351898de363/src/mini_claude/core/runner.py#L299-L305), [task records](https://github.com/zmylol/MiniClaude/blob/186ccb09f485aab9c5b60c8b7cc92351898de363/src/mini_claude/core/task/manager.py#L70-L105)
- Basis: structural
- Confidence: medium
- Caveats: A parent human can stop or approve actions, but a tool-level permission is not a whole-system S3 mode.

### Absence scope

- Surfaces inspected: Core runner/loop, task registry, permission manager, session and desktop entry.
- Plausible first-party paths checked: Session/task overview, tool approval, limits, child registry and stop; sought discretion over competing live units and feedback.
- Why no material first-party path remains: Permission enforcement and session control are not, by themselves, an S3 decision over current multiple S1 commitments.

## S3* — Complementary audit

- State: —
- Function: No independent complementary operational-reality audit with return to current management is demonstrated.
- Disturbance / variety regulated: Execution traces, tool failures or claimed successes may disagree with actual project reality.
- Decisive decision or feedback right: An independent audit actor would challenge claims using a complementary evidence channel and return findings to a controller.
- Decision owner: Run owner and diagnostics/trace viewer observe ordinary execution; no separate audit decision owner is shown.
- Supporting / enforcement mechanisms: EventWriter, tracing, tool-result errors and optional user inspection.
- Closure path: Trace and error records return to the same run or UI; no separately independent audit finding and corrective S3 action path is evidenced.
- Why this is / is not agent-owned: Logging and model-visible error feedback are not an independent, complementary audit authority.
- Evidence: [runner event writing](https://github.com/zmylol/MiniClaude/blob/186ccb09f485aab9c5b60c8b7cc92351898de363/src/mini_claude/core/runner.py#L238-L247), [loop feedback](https://github.com/zmylol/MiniClaude/blob/186ccb09f485aab9c5b60c8b7cc92351898de363/src/mini_claude/core/loop.py#L149-L225), [trace store](https://github.com/zmylol/MiniClaude/blob/186ccb09f485aab9c5b60c8b7cc92351898de363/src/mini_claude/core/trace/writer.py#L1-L90)
- Basis: structural
- Confidence: medium
- Caveats: A custom external auditor could be added, but it is not proven as a shipped first-party mode.

### Absence scope

- Surfaces inspected: Core events/trace, loop, tests, evaluation experiment, documentation.
- Plausible first-party paths checked: Trace/event streams, ordinary tool checks, child results and evaluation samples; looked for independent claim checking and S3 return.
- Why no material first-party path remains: Logging and model-visible error feedback are not an independent, complementary audit authority.

## S4 — Outside-and-then intelligence

- State: —
- Function: No demonstrated outside-and-future adaptation decision returning a durable change to present system capability.
- Disturbance / variety regulated: New environments and future needs might make past agent strategy inadequate.
- Decisive decision or feedback right: An S4 actor would distinguish external future circumstances, select capability changes and re-inject them into operations.
- Decision owner: Task model may search and locally edit notes, but no shipped prospective adaptation owner is evidenced.
- Supporting / enforcement mechanisms: Search, memory/context files, notes, compaction, skills loader and scheduled local work.
- Closure path: Persistent project/session context assists later tasks; no external prospective signal is processed as a distinct S4 adaptation choice with organization-wide capability feedback.
- Why this is / is not agent-owned: Conversation memory, a future task, model web search or replay is not independently a future adaptation and return loop.
- Evidence: [context and notes wiring](https://github.com/zmylol/MiniClaude/blob/186ccb09f485aab9c5b60c8b7cc92351898de363/src/mini_claude/core/runner.py#L186-L236), [compaction and next turn](https://github.com/zmylol/MiniClaude/blob/186ccb09f485aab9c5b60c8b7cc92351898de363/src/mini_claude/core/loop.py#L211-L224), [session/task state](https://github.com/zmylol/MiniClaude/blob/186ccb09f485aab9c5b60c8b7cc92351898de363/src/mini_claude/core/task/manager.py#L43-L126)
- Basis: structural
- Confidence: medium
- Caveats: In-session planning and retained context may improve S1, but do not suffice for S4.

### Absence scope

- Surfaces inspected: Runner, memory, compactor, tasks, schedule commands, README/roadmap.
- Plausible first-party paths checked: Context loaders, note persistence, skills, web search and schedules; sought externally motivated future capability decision and return.
- Why no material first-party path remains: Conversation memory, a future task, model web search or replay is not independently a future adaptation and return loop.

## S5 — Policy and identity

- State: —
- Function: A tool-permission configuration exists, but the examined distribution does not establish an operational ultimate identity/policy issue governed at the assessed organizational recursion.
- Disturbance / variety regulated: Dangerous tool calls may violate local permission policy; future projects may need distinct identity constraints.
- Decisive decision or feedback right: Ultimate identity/mission/policy authority would need a specific issue, legitimate parent decision and returned governed operation, beyond a tool-use grant.
- Decision owner: Human responds to individual permission requests or sets static access mode; no first-party legitimate S5 closure path is established.
- Supporting / enforcement mechanisms: Policy defaults, mode flags, persistent allow/deny file and permission request futures.
- Closure path: The chosen approval can permit/deny current and later tool calls; no system identity or ultimate organization-policy decision path is shown.
- Why this is / is not agent-owned: A persistent tool grant constrains S1 invocation; ordinary access controls are not S5 simply because a human chooses them.
- Evidence: [permission modes](https://github.com/zmylol/MiniClaude/blob/186ccb09f485aab9c5b60c8b7cc92351898de363/src/mini_claude/core/permissions/manager.py#L44-L97), [approval and persisted grants](https://github.com/zmylol/MiniClaude/blob/186ccb09f485aab9c5b60c8b7cc92351898de363/src/mini_claude/core/permissions/manager.py#L158-L250), [runner session mode application](https://github.com/zmylol/MiniClaude/blob/186ccb09f485aab9c5b60c8b7cc92351898de363/src/mini_claude/core/runner.py#L179-L185)
- Basis: structural
- Confidence: medium
- Caveats: No claim that a human cannot govern MiniClaude in a larger adjacent organization; that larger recursion is outside this runtime assessment.

### Absence scope

- Surfaces inspected: Core permission manager/policy, runner, session commands, docs.
- Plausible first-party paths checked: Permission manager, static policy, human approval/resume, local configuration, project/desktop clients; sought identity/policy issue and authority/return.
- Why no material first-party path remains: A persistent tool grant constrains S1 invocation; ordinary access controls are not S5 simply because a human chooses them.

## Distributed OSS parent arrangement

The public maintainer/contributor organization and CI are adjacent to this installed local runtime. Their decisions are not first-party runtime governance paths for S3, S4 or S5. Human per-tool approvals are considered, but do not substantiate any published parent mode.

## Self-hosted and non-human modes

A local user can operate the core with model credentials, supported tool policy and clients; tool calls and child agents remain constrained by the same runtime authorization. No separately evidenced non-human metasystem owner for S2 through S5 was found. External model providers and external MCP services are dependencies, not first-party autonomy donors.

## Recursion

The configured model agent and optional delegated child loops are task-level operational units nested in one MiniClaude project/session runtime. Nested processes and agent prompts are not evidence of a viable higher-order organizational recursion.

## Variety and escalation

The run absorbs tool/LLM variety via model choices and per-call observation. Tool-use permission requests escalate to a user and return a bounded permission result. Run caps, cancellation and error traces constrain execution. None of these paths alone establishes organizational S3/S4/S5 ownership.

## Evidence gaps

The investigation is pinned to source and docs at the frozen revision, without live paid model-provider testing or an independently conducted secondary audit. Supported optional MCP/server extensions could provide additional behavior when composed by a user; the assessment does not credit uninstantiated external actors. An independent audit could revisit concrete runtime conflict and global-operator views if a new pinned source witness becomes available.

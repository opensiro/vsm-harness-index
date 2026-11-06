---
harness_id: vibe-coder
project_name: vibe-coder
repository: https://github.com/jonathanhecl/vibe-coder
review_ref: 49f6598b756b3ec9440c80f16bdd556624a152f1
reviewed_at: 2026-11-06
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# vibe-coder

## Review boundary

- System in focus: the shipped Go `vibe` Ollama coding-agent CLI/REPL, model-directed tool/observation loop, autonomous missions, delegated `SubAgent` / `ParallelAgents`, permission engine, optional JEV Style decision model and sidecar, durable task/session persistence, and verification tooling.
- Purpose and identity: carry out developer-requested coding, search, shell and web tasks in a local workspace, including longer model-selected missions, under developer permission limits.
- Relevant environment: repository files, user objectives, shell and test output, network observations, local Ollama and optional JEV endpoints, multiple delegated child operations, ambiguous paths, tool permissions, model failures and resumable work state.
- Standard-distribution boundary: `cmd/vibe` initializes the first-party Go agent, tool registry, REPL and session; `internal/agent` selects calls through an externally configured inference model, `internal/tools` executes them. Ollama/JEV inference services, the edited repository, human operator and downstream MCP servers are external dependencies, not independently credited harness-owned systems.
- Credited operating / distribution surfaces: `cmd/vibe/{repl,main}.go`, `internal/agent/{run,agent,mission,tool_policy,tool_exec}.go`, `internal/tools/{subagent,mission,jev_decide,tool}.go`, `internal/permissions/manager.go`, `internal/jevstyle`, `internal/sidecar`, `internal/session`, `internal/git`, `internal/config`, and supported CLI flags / modes.
- Adjacent first-party surfaces excluded from ownership: GitHub Actions CI, badges, source-development tests, contributor rules, releases, project logo and local documentation as a separate operator. Tests corroborate production mechanisms but do not become independent runtime auditor agents.
- First-party operating modes considered: one-shot `-p`, interactive REPL, autonomous `MissionStart`, resumable session, parallel 2–4 bounded children, read-only children or explicitly authorized writer children, plan/review modes, JEV Style assisted approvals and completion checks.
- Recursion level: one locally running coding-agent work session and its delegated child model/tool work cells. External providers, other users' sessions and the repo maintainers are not aggregated into a higher viable organization.
- Reviewed revision: `49f6598b756b3ec9440c80f16bdd556624a152f1`; observation date: 2026-11-06; Profile `0.2.4`, Methodology `0.3.7`.

## Repository architecture

The main `Agent.Run` repeatedly asks the configured model to select tools, executes bounded native tool calls or XML fallback invokes, appends actual observations, retries empty output and feeds errors back for correction. Read/write/shell/web/Git/task tools operate on a real workspace with permission and mode checks. After writes, a readback and applicable test can run. The model can declare a long-running mission; the CLI supplies further turns until the mission is completed/blocked or runtime stall guards intervene. Progress, TODOs, sessions and redacted mission logs persist for resume.

The first-party `SubAgent` independently calls the model in a bounded ReAct loop with a fresh task transcript and selected Read/Glob/Grep tools; optional Write/Edit/Bash go through the parent authorization executor. `ParallelAgents` runs two to four such loops concurrently. Their concrete tool executions are serialized through the parent's `delegatedMu`, including permissions, checkpoints and auto-tests; model reasoning still occurs concurrently. This suppresses overlapping *tool execution* and checkpoint/approval races among children, but does not provide branch isolation or atomic multi-tool read–modify–write transactions.

JEV Style is a separately configured decision model. It can review whether a mission goal is complete based on the goal and selected recent progress/session messages, then inject a reminder to continue. It also classifies risky actions, errors and other discrete choices. The ordinary agent can directly call `MissionComplete` without a mandatory JEV veto, and the JEV completion decider does not independently re-read raw files or run tests. This is a second-opinion/current task safeguard, not an established independent complementary-audit channel.

Primary frozen-source evidence:

- [Main model/tool loop](https://github.com/jonathanhecl/vibe-coder/blob/49f6598b756b3ec9440c80f16bdd556624a152f1/internal/agent/run.go)
- [Delegated model/tool loops and parallel execution](https://github.com/jonathanhecl/vibe-coder/blob/49f6598b756b3ec9440c80f16bdd556624a152f1/internal/tools/subagent.go)
- [Shared delegated tool execution lock and policy](https://github.com/jonathanhecl/vibe-coder/blob/49f6598b756b3ec9440c80f16bdd556624a152f1/internal/agent/tool_policy.go)
- [Delegation permission/checkpoint tests](https://github.com/jonathanhecl/vibe-coder/blob/49f6598b756b3ec9440c80f16bdd556624a152f1/internal/agent/delegation_test.go)
- [Mission loop and JEV completion feedback](https://github.com/jonathanhecl/vibe-coder/blob/49f6598b756b3ec9440c80f16bdd556624a152f1/cmd/vibe/repl.go)
- [JEV evidence boundary](https://github.com/jonathanhecl/vibe-coder/blob/49f6598b756b3ec9440c80f16bdd556624a152f1/internal/agent/mission.go)
- [JEV completion classification](https://github.com/jonathanhecl/vibe-coder/blob/49f6598b756b3ec9440c80f16bdd556624a152f1/internal/jevstyle/jevstyle.go)
- [Product capabilities and permissions](https://github.com/jonathanhecl/vibe-coder/blob/49f6598b756b3ec9440c80f16bdd556624a152f1/README.md)

## Operational model

A user task becomes the main model's current objective, which controls concrete tool calls and revisions based on observed outputs. For larger tasks it can create an autonomous mission and checklist. For independent parts it delegates to smaller fresh-context model loops; the parent authorization path mediates their tool effects. The optional second decision model can critique reported mission completion or safety of an action, while the parent/CLI remain in charge of task completion and the user retains protected-command consent.

## S1 — Operations

- State: A
- Function: perform repository/code operations with a real iterative model-selected tool–observation–correction loop, including separately reasoning delegated child work.
- Disturbance / variety regulated: missing source context, failing tests, ambiguous file locations, incomplete requirements, tool errors, multi-step mission progress and child task findings.
- Decisive decision or feedback right: choose which task-specific file, shell, web or child action to attempt next and adapt after receiving concrete output.
- Decision owner: configured main model acting through `Agent.Run` and bounded model-backed `SubAgent` instances for their local tool decisions.
- Supporting / enforcement mechanisms: tool registry, Ollama native/XML support, retry/cap guards, file readback/auto-test, permissions, context compaction, durable checklist/mission and sub-agent scope caps.
- Closure path: developer goal → model-selected tool or delegated child → authorized action on current project → real observation → model revision/continuation or final response.
- Boundary reachability: first-party CLI/REPL calls `Agent.Run`; first-party registry exposes `SubAgent`/`ParallelAgents`; their model calls and tools operate within the product runtime.
- Why this is / is not agent-owned: removing the model eliminates the task-specific choice and subsequent feedback response; rule-only tools and the REPL do not select edits independently.
- Evidence: [`agent/run.go`](https://github.com/jonathanhecl/vibe-coder/blob/49f6598b756b3ec9440c80f16bdd556624a152f1/internal/agent/run.go); [`tools/subagent.go`](https://github.com/jonathanhecl/vibe-coder/blob/49f6598b756b3ec9440c80f16bdd556624a152f1/internal/tools/subagent.go); [`cmd/vibe/repl.go`](https://github.com/jonathanhecl/vibe-coder/blob/49f6598b756b3ec9440c80f16bdd556624a152f1/cmd/vibe/repl.go).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: local inference must be configured; delegated writers need parent permission and their own concrete tool outcomes can still conflict at a higher workflow granularity.

## S2 — Coordination

- State: C
- Function: attenuate a bounded concurrent-child disturbance by ensuring one delegated concrete tool action, including permission/checkpoint/test handling, executes at a time against the shared parent runtime.
- Distinct S1 units: at least two concurrently progressing fresh-context model-backed `SubAgent` loops launched by `ParallelAgents`, each able to choose permitted Read/Glob/Grep and optional Write/Edit/Bash actions.
- Inter-S1 disturbance: concurrent child tools would otherwise overlap shared permission prompts, first-party Git checkpoints, auto-test execution and shared worktree file mutations. Those effects can collide or be observed at unstable partial states.
- Attenuating coordination relation: `Agent.executeDelegatedTool` wraps each delegated action under one parent-owned `delegatedMu` and routes it through the same permission/mode/checkpoint executor; `ParallelAgents` runs model loops concurrently while delegated concrete tool effects are mutually exclusive.
- Feedback into subsequent S1 behaviour: each child waits for its authorized action to finish and consumes that action's resulting output before selecting another, then reports its findings to the spawner. Serialized tool effects prevent simultaneous execution of child actions.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the mutex is a concrete anti-overlap critical section for actual shared-workspace side effects from distinct autonomous child loops, not merely a task dispatcher or notification channel. Its reach is deliberately **per delegated tool action**, not a multi-step conflict-free transaction.
- Disturbance / variety regulated: intersecting tool side effects and the permission/checkpoint/test state they share during parallel subordinate operations.
- Decisive decision or feedback right: a parent model decides parallel delegation and tool intents; the first-party executor determines the non-overlapping execution order and enforces parent permissions, irrespective of child preference.
- Decision owner: deterministic first-party parent executor and mutex, not an independently negotiating coordinator; hence constructor-level **C**, not autonomous S2 A.
- Supporting / enforcement mechanisms: `errgroup` parallel child scheduling, shared parent executor injection, `delegatedMu`, tool policy/authorization, checkpoint and auto-test invocation.
- Closure path: parallel child intents → one child holds the delegated-tool lock → parent-approved effect completes → child observes output and continues → next child obtains lock, avoiding concurrent tool execution.
- Boundary reachability: `ParallelAgents.Execute` concurrently invokes `SubAgent.runLoop`; `runLoop` uses `executorFromContext`, installed by the main agent; `executeDelegatedTool` locks and calls first-party `executeTool`.
- Why this is / is not agent-owned: the serialized critical section works without a model deciding coordination policy. It reduces a real child–child tool-interference mode, but cannot stop a later tool from overwriting a sibling's earlier edit.
- Evidence: [`tools/subagent.go`](https://github.com/jonathanhecl/vibe-coder/blob/49f6598b756b3ec9440c80f16bdd556624a152f1/internal/tools/subagent.go); [`agent/tool_policy.go`](https://github.com/jonathanhecl/vibe-coder/blob/49f6598b756b3ec9440c80f16bdd556624a152f1/internal/agent/tool_policy.go); [`agent/delegation_test.go`](https://github.com/jonathanhecl/vibe-coder/blob/49f6598b756b3ec9440c80f16bdd556624a152f1/internal/agent/delegation_test.go).
- Basis: explicit + structural; no dedicated concurrent-writer loss-prevention test is claimed.
- Confidence: medium-high for tool-level S2; limited for workflow-level interference.
- Caveats: no per-child Git worktree, transaction-level mutual exclusion, changed-file reconciliation or guaranteed prevention of sequential lost updates. The coordination claim is restricted to synchronized delegated tool executions and shared helper state.

## S3 — Current internal control

- State: —
- Function: no whole-current operational management authority over an aggregate of independently operating S1 units is established.
- Disturbance / variety regulated: the current mission and delegated subtask completion, iterations, retries, permission refusals and tool output are managed locally rather than across a broader operating portfolio.
- Decisive decision or feedback right: no separately closed current-resource allocation, cross-worker performance correction or supervisor arbitration right beyond the initiating coding conversation's work.
- Decision owner: not established at S3 recursion; the spawner handles task-level delegation and the CLI enforces deterministic caps/stall policy.
- Supporting / enforcement mechanisms: TODO/TaskStart/TaskComplete, mission progress, bounded children, JEV reported completion, execution counters, persistent logs and CLI stall guards.
- Closure path: individual task feedback and mission events return to the same coding agent or human; no separately evidenced whole-current S3 intervention loop.
- Why this is / is not agent-owned: mission ownership and delegated task orchestration are S1 task continuation; generic counters, logs and permission limits do not show an authority to govern an operating portfolio.
- Evidence: [`agent/mission.go`](https://github.com/jonathanhecl/vibe-coder/blob/49f6598b756b3ec9440c80f16bdd556624a152f1/internal/agent/mission.go); [`tools/mission.go`](https://github.com/jonathanhecl/vibe-coder/blob/49f6598b756b3ec9440c80f16bdd556624a152f1/internal/tools/mission.go); [`cmd/vibe/repl.go`](https://github.com/jonathanhecl/vibe-coder/blob/49f6598b756b3ec9440c80f16bdd556624a152f1/cmd/vibe/repl.go).
- Basis: explicit + structural absence review.
- Confidence: medium-high.
- Caveats: current-task supervisory-looking behavior exists; it does not warrant extrapolation to organizational S3.

### Absence scope

- Surfaces inspected: mission lifecycle, TodoWrite and task tools, parallel children and report collection, CLI continuation/stall guards, JEV progress judgments, session state and logs.
- Plausible first-party paths checked: multi-worker current commitments/budgets, ongoing portfolio supervision, exception-driven managerial redistribution and aggregate worker performance correction.
- Why no material first-party path remains: the available authority is scoped to a single coding session and its work steps; none constitutes a separate managerial current-operations closure over multiple S1 work cells.

## S3* — Complementary audit

- State: —
- Function: no demonstrably independent reality-checking complementary audit of S1 output with a separate corrective supervisory closure exists.
- Disturbance / variety regulated: false completion claims, failed commands, risky actions and incorrect edits are checked through the ordinary tool/test loop and optional JEV second-opinion classification.
- Decisive decision or feedback right: JEV can flag *reported* mission progress as incomplete and inject a reminder, but cannot independently inspect raw files, run audit tests or veto an agent's direct `MissionComplete` call; no independent evidence/return right is established.
- Decision owner: main model still owns mission completion; JEV is a separate configured classifier over a supplied goal and session-progress text, not an independently mandated S3* auditor.
- Supporting / enforcement mechanisms: `ReviewMissionCompletion`, `CheckGoalCompletion`, explicit session reminder, optional `JevDecide`, auto-test, readback and saved JSONL run log.
- Closure path: current mission's goal + progress/session messages → optional JEV decision → reminder to the main agent on incomplete result; it may continue ordinary task work. There is no separately governed direct-source inspection → independent finding → enforced supervisory correction path.
- Why this is / is not agent-owned: JEV performs a real discrete model judgment, but the observations are selected from the operating session; its separate model identity alone does not prove independence of evidence or of audit authority.
- Evidence: [`agent/mission.go`](https://github.com/jonathanhecl/vibe-coder/blob/49f6598b756b3ec9440c80f16bdd556624a152f1/internal/agent/mission.go); [`jevstyle/jevstyle.go`](https://github.com/jonathanhecl/vibe-coder/blob/49f6598b756b3ec9440c80f16bdd556624a152f1/internal/jevstyle/jevstyle.go); [`cmd/vibe/repl.go`](https://github.com/jonathanhecl/vibe-coder/blob/49f6598b756b3ec9440c80f16bdd556624a152f1/cmd/vibe/repl.go); [`mission_jev_feedback_test.go`](https://github.com/jonathanhecl/vibe-coder/blob/49f6598b756b3ec9440c80f16bdd556624a152f1/internal/agent/mission_jev_feedback_test.go).
- Basis: explicit + structural absence review.
- Confidence: medium-high.
- Caveats: this negative label does not deny JEV's independent model call or useful completion feedback; it denies that the narrower complementarily independent audit closure is established at this frozen ref.

### Absence scope

- Surfaces inspected: mission/JEV decision inputs, JEV completion verdict and tests, direct MissionComplete path, assisted safety decisions, auto-test/readback, run logs and review mode.
- Plausible first-party paths checked: raw-file/test auditor independent of producer assertions, separate audit sampling/trigger, blocking or escalated independent findings, correction verification after audit.
- Why no material first-party path remains: JEV receives the task's summarized/history messages rather than acquiring independent source evidence and has no mandatory finalization veto; other checks belong to the producer's tool path.

## S4 — Outside-and-then intelligence

- State: —
- Function: no independently closed prospective environmental scan and future-capability adaptation loop is established.
- Disturbance / variety regulated: provider availability, network search results, repository changes and context pressure are handled for current tasks or through user-configured extensions.
- Decisive decision or feedback right: no agent-controlled future organizational option, investment or capability-change proposal returned to current control.
- Decision owner: not established; user configures models/MCP/skills, while the agent uses those as present-task resources.
- Supporting / enforcement mechanisms: WebSearch/WebFetch/HTTPRequest, optional RAG and sidecar, model/endpoint selection and MCP/skills configuration.
- Closure path: user-supplied or retrieved facts inform current work; no future-threat/option assessment and accountable adoption/rollback into the operating organization is wired.
- Why this is / is not agent-owned: looking up web facts and adapting a coding plan are S1 activities, not continuing strategic S4 intelligence.
- Evidence: [`README.md`](https://github.com/jonathanhecl/vibe-coder/blob/49f6598b756b3ec9440c80f16bdd556624a152f1/README.md); [`agent/run.go`](https://github.com/jonathanhecl/vibe-coder/blob/49f6598b756b3ec9440c80f16bdd556624a152f1/internal/agent/run.go); [`agent/agent.go`](https://github.com/jonathanhecl/vibe-coder/blob/49f6598b756b3ec9440c80f16bdd556624a152f1/internal/agent/agent.go).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: optional external MCP agents are not silently imported as first-party S4 functions.

### Absence scope

- Surfaces inspected: network search/tools, RAG, skills/MCP loading, provider selection, sidecar model, mission task stores and CLI modes.
- Plausible first-party paths checked: outside-in trend monitoring, future capability options, organizational learning priorities and controlled adaptation of agent structure.
- Why no material first-party path remains: the shipped agents consume current context and perform user tasks; no prospective policy/strategy loop with organizational feedback closes.

## S5 — Policy and identity

- State: —
- Function: no legitimate organizational ultimate-purpose/identity policy decision and binding policy feedback loop is established.
- Disturbance / variety regulated: protected file operations, dangerous shell patterns, web access, child permissions and unattended mission risk are constrained through static code and operator settings.
- Decisive decision or feedback right: the user configures permissions; mandatory dangerous actions remain human-guarded/denied. Neither the main agent nor JEV is authorized to redefine the parent mission or ultimate policy.
- Decision owner: no S5 owner within the assessed harness; operator and authored constraints retain ordinary authorization.
- Supporting / enforcement mechanisms: permission tiers, remembered allow/deny, mandatory command denials, plan/review restrictions, JEV optional assisted-risk classification, sanitized subprocess environment and inherited child ceilings.
- Closure path: attempted tool effect → permission/mode/danger gate → allow/deny or user approval → individual action proceeds/halts. No ultimate policy issue → parent ratification → durable identity-policy change loop.
- Why this is / is not agent-owned: action-level risk decisions may be assisted by JEV and autonomous missions may run unattended, but neither determines the legitimate constitutional identity or self-authorizes changed governance rules.
- Evidence: [`permissions/manager.go`](https://github.com/jonathanhecl/vibe-coder/blob/49f6598b756b3ec9440c80f16bdd556624a152f1/internal/permissions/manager.go); [`agent/tool_policy.go`](https://github.com/jonathanhecl/vibe-coder/blob/49f6598b756b3ec9440c80f16bdd556624a152f1/internal/agent/tool_policy.go); [`README.md`](https://github.com/jonathanhecl/vibe-coder/blob/49f6598b756b3ec9440c80f16bdd556624a152f1/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: autonomous execution and delegated risk screening increase operational power without transferring identity-policy authority.

### Absence scope

- Surfaces inspected: assistant mission declaration, user and persisted permissions, JEV assisted auto-approval, static dangerous-command gates, child ceiling, mode switches and agent configuration.
- Plausible first-party paths checked: ultimate-purpose disputes, binding constitutional change, legitimate parent approval, durable identity boundaries and feedback after such a decision.
- Why no material first-party path remains: the code controls tool authorization and user-requested mission execution, without a separate ratified policy/identity deliberation loop.

## Recursion

One main operational S1 can launch separate model-backed child S1 work cells. A deterministic parent mutex attenuates the narrow inter-child disturbance of simultaneous shared-state tool execution (S2 C); there is no proof that this becomes a recursively complete team with whole-current S3, independent S3*, future S4 and identity S5.

## Variety and escalation

The main model, parallel delegated loops, Ollama tools, network access, persistent missions and external integrations increase task response variety. Turn/tool caps, per-action mutex, authorization gates, auto-test/checkpoints, session compaction, JEV model judgments, stall guards and human-controlled dangerous commands attenuate operational risk. Escalation to the human occurs for blocked missions or protected approvals; it does not create an independent organizational governance layer.

## Evidence gaps

This is a source-first review at the frozen SHA, not a live Ollama mission execution. The mutex's existence and delegated policy/checkpoint tests support serialized tool effects; no direct two-writer collision regression or guarantee against non-atomic multi-action edits is claimed. JEV is optional and its decisions are computed from model-visible progress/session text, with no independent fresh-source inspection or compulsory veto of `MissionComplete`. The absence review excludes external MCP/provider behavior and future design claims.

## Assessment summary

vibe-coder runs a first-party model-selected coding/tool feedback loop and genuine bounded model-backed child operations (**S1=A**). Shared serialized execution of parallel child tool effects supplies a bounded constructor-owned inter-S1 overlap guard (**S2=C**), but is not branch isolation or full conflict reconciliation. JEV offers a useful distinct model completion check, yet no independent producer-challenging audit evidence/authority is closed; mission administration, user permissions, web access and persistent configuration do not establish **S3/S3*/S4/S5** at this boundary.

Proposed vector: **`A · C · — · — · — · —`**.

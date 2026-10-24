---
harness_id: g-rump
project_name: G-Rump
repository: https://github.com/Aphrodine-wq/G-Rump
review_ref: 876766327171eed40df89ef1d58c8c9a475c8def
reviewed_at: 2026-10-22
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

# G-Rump

## Review boundary

- System in focus: the first-party, source-distributed macOS SwiftUI G-Rump coding assistant, including its interactive `ChatViewModel` model/tool loop, opt-in supervised daemon, learning/reflection, review and proactive suggestion features.
- Purpose and identity: carry out a user's project coding request using local tools and model providers, report results, and optionally process queued goals when the application is idle.
- Relevant environment: user's working tree and git state, host macOS resources, model/provider responses, tool and build results, human approval, app settings, project memory and local lesson/goal stores.
- Standard-distribution boundary: `Sources/GRump` first-party application and wired services; user-created skills, connected MCP servers, external models, repository developer organization and macOS OS-level governance are not silently credited as G-Rump decision-owning cells.
- Credited operating / distribution surfaces: `GRumpApp` bootstrap, `ChatViewModel` streaming agent loop and tool dispatcher, optional supervised `AutonomousLoop`, `ReflectionEngine`, lesson prompt injection, `AdversarialReviewEngine`, `ProactiveEngine` and `ConscienceGate`.
- Adjacent first-party surfaces excluded from ownership: developer CI/test fixtures, documentation and open-source repository governance, downstream provider policy, user-written skills, custom MCP servers, external coding agents and uninspected installed binaries beyond the pinned source.
- Operating modes considered: interactive coding agent, parallel tool calls within one turn, build-mode adversarial code review, opt-in background daemon, post-run reflection/lesson injection, proactive suggestions and deterministic Conscience gate.
- Recursion level: one installed application operating coding tasks for one user/working directory, including optional sequenced daemon goals, not the open-source maintainers or a fleet of installed apps.
- Reviewed revision: [`876766327171eed40df89ef1d58c8c9a475c8def`](https://github.com/Aphrodine-wq/G-Rump/tree/876766327171eed40df89ef1d58c8c9a475c8def) from frozen batch intake #200.
- Observation date: 2026-10-22; pinned first-party source inspection only. Native macOS execution and provider-backed output were not tested from Linux.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

The SwiftUI app's interactive `ChatViewModel` makes provider calls, accumulates model-requested native/MCP tool operations, executes calls (potentially in parallel), returns tool results to conversation history and iterates until completion or a limit. Verification can return the loop to another coding step. This is first-party model-directed task work, with user/provider/host constraints.

The optional `AutonomousLoop` wakes on a periodic tick only if enabled, the Conscience gate is active and the **same** `ChatViewModel` is idle. It ranks queued goals by supplied priority and learned task-type success; a goal then runs through that existing agent on a `grump-daemon/<id>` git branch. A branch checkout is not a separate worktree, and the daemon does not operate as a concurrently independent S1 beside the interactive loop. Each mutating daemon tool additionally requires human approval; the daemon cannot push. After repeated failures it disables itself. This is a useful source-backed scheduling and safety mechanism but does not establish an inter-S1 disturbance relationship.

At the end of ordinary runs, outcome telemetry and transcript excerpts may reach a distinct reflection-model call. It can write/revise durable lessons, whose relevant entries are fed back into later prompts, or propose new skills for human approval. An adversarial review model separately inspects summaries of changed code for bugs and risks; a proactive engine enqueues suggestions from recent local activity, app events and schedules. These are substantive post-run feedback and task QA functions. Neither demonstrates a future external environment model reconciled with whole-current S3 authority, an independent S3 operational audit, or agent-owned ultimate governance.

Primary anchors: [model/tool loop](https://github.com/Aphrodine-wq/G-Rump/blob/876766327171eed40df89ef1d58c8c9a475c8def/Sources/GRump/ViewModels/ChatViewModel%2BAgentLoop.swift#L14-L345), [daemon](https://github.com/Aphrodine-wq/G-Rump/blob/876766327171eed40df89ef1d58c8c9a475c8def/Sources/GRump/Intelligence/Daemon/AutonomousLoop.swift#L8-L170), [post-run learning](https://github.com/Aphrodine-wq/G-Rump/blob/876766327171eed40df89ef1d58c8c9a475c8def/Sources/GRump/ViewModels/ChatViewModel%2BAgentPostRun.swift#L100-L188), [reflection operations](https://github.com/Aphrodine-wq/G-Rump/blob/876766327171eed40df89ef1d58c8c9a475c8def/Sources/GRump/Intelligence/Learning/ReflectionEngine.swift#L54-L215).

## Operational model

The coding model selects task-dependent tool calls; a typed dispatcher, deterministic Conscience checks and human approval coordinator enforce execution limits. A daemon goal is another **serial use of this same agent loop** and is not simultaneously an independent operational division. The reflection pass modifies local prompt lessons; new skills and sensitive writes remain human-gated. Repository authors and model vendors remain outside the selected recursion.

## S1

- State: A
- Function: Choose and carry out concrete coding operations against a user project, learning from tool feedback within the same task.
- Disturbance / variety regulated: Unknown code structure, user requirements, tool failures, compilation/verification feedback and changing local files.
- Decisive decision or feedback right: The configured model emits file/shell/git/MCP tool calls and subsequent steps based on returned observations; when allowed, its actions mutate the project.
- Decision owner: Model-driven first-party `ChatViewModel` coding loop and the configured provider, with a first-party dispatcher executing selected calls.
- Supporting / enforcement mechanisms: Tool registry and dispatch, concurrent tool execution, rolling context compaction, auto-verification, iterations, Conscience policy and user approval for specified actions.
- Closure path: User request / daemon-selected goal → model decision → native/MCP tool call → tool output or denied action → next model decision, verification or task finish.
- Why this is / is not agent-owned: The task-specific next code/tool decision is model-owned, even though the tool menu, safety guards and ultimate user objective are fixed externally.
- Boundary reachability: Interactive app wires the loop; the optional daemon directly calls `viewModel.sendMessage()` and waits on `isLoading`, reusing that operative path.
- Evidence: [agent run and provider stream](https://github.com/Aphrodine-wq/G-Rump/blob/876766327171eed40df89ef1d58c8c9a475c8def/Sources/GRump/ViewModels/ChatViewModel%2BAgentLoop.swift#L14-L105), [tool execution and return](https://github.com/Aphrodine-wq/G-Rump/blob/876766327171eed40df89ef1d58c8c9a475c8def/Sources/GRump/ViewModels/ChatViewModel%2BAgentLoop.swift#L230-L280), [tool gate and dispatcher](https://github.com/Aphrodine-wq/G-Rump/blob/876766327171eed40df89ef1d58c8c9a475c8def/Sources/GRump/ViewModels/ChatViewModel%2BToolExecution.swift#L63-L113), [daemon reuses loop](https://github.com/Aphrodine-wq/G-Rump/blob/876766327171eed40df89ef1d58c8c9a475c8def/Sources/GRump/Intelligence/Daemon/AutonomousLoop.swift#L133-L164).
- Basis: structural.
- Confidence: high for source-wired model/tool discretion; macOS live operation untested.
- Caveats: Actual task correctness, provider availability and the daemon's end-of-goal success inference require separate runtime evidence.

## S2

- State: —
- Function: Attenuate a concrete disturbance among independent operational S1 units.
- Disturbance / variety regulated: Potential shared-worktree conflicts between interactive coding and queued autonomous goals; competition among simultaneous local tasks.
- Decisive decision or feedback right: There is an idle guard, single-goal guard and checkout to a named branch, but no detected inter-S1 interference with coordination decisions returned to two independently operating cells.
- Decision owner: No distinct S2 owner shown. The daemon makes serial goal selection; tool-call parallelism occurs within one S1 loop.
- Supporting / enforcement mechanisms: `!viewModel.isLoading`, `isRunningGoal`, single shared `ChatViewModel`, scratch-named branch, pending goal statuses, sequential queues and user approval per daemon mutation.
- Closure path: App idle → daemon selects goal → existing S1 runs → outcome recorded. This is scheduling, not observed conflict → attenuation → adjustment of multiple S1s.
- Why this is / is not agent-owned: Priority ranking and concurrency exclusions may mitigate interference, but source does not establish separately viable operating units in a live inter-unit feedback relation.
- Evidence: [daemon idle/single-run guard and score](https://github.com/Aphrodine-wq/G-Rump/blob/876766327171eed40df89ef1d58c8c9a475c8def/Sources/GRump/Intelligence/Daemon/AutonomousLoop.swift#L23-L68), [single view model, git checkout and sendMessage](https://github.com/Aphrodine-wq/G-Rump/blob/876766327171eed40df89ef1d58c8c9a475c8def/Sources/GRump/Intelligence/Daemon/AutonomousLoop.swift#L133-L165), [intra-loop parallel tools](https://github.com/Aphrodine-wq/G-Rump/blob/876766327171eed40df89ef1d58c8c9a475c8def/Sources/GRump/ViewModels/ChatViewModel%2BAgentLoop.swift#L241-L269).
- Basis: structural.
- Confidence: medium-high within inspected first-party routes.
- Caveats: External MCP servers may operate concurrently; their governance is not first-party S2.

### Absence scope

- Surfaces inspected: daemon priority queue and lifecycle, shared agent loop, parallel tool dispatch, goal store, scratch-branch switch, app scheduling and approval path.
- Plausible first-party paths checked: daemon versus interactive action arbitration, queued goals, tool-call concurrency, branch isolation and user intervention.
- Why no material first-party path remains: The daemon expressly waits for the interactive loop to become idle and invokes that same loop; no second independently operating S1 or inter-unit corrective return is demonstrated.

## S3

- State: —
- Function: Control current whole-system commitments, priorities and scarce resources across a viable set of S1 units.
- Disturbance / variety regulated: Competing queued goals, degraded success rates, failure bursts, user interaction and runtime cost.
- Decisive decision or feedback right: The daemon ranks one next goal and parks low-success task types; it does not reallocate ongoing resources or commitments across independent S1 units from a whole-current view.
- Decision owner: Deterministic daemon queue scheduler with user priority inputs, not a evidenced S3 manager; the root coding agent controls its own task.
- Supporting / enforcement mechanisms: GoalStore statuses, `LearningStore.successRate`, one-goal gate, fail-stop after three consecutive failures, session context and user-facing notifications.
- Closure path: Pending list → priority and historical success score → one serial S1 assignment → done/failed status. No current portfolio control intervention across operating cells is closed.
- Why this is / is not agent-owned: Ranking prospective sequential jobs and tracking them does not alone supply S3's whole-current operational authority.
- Evidence: [goal choice and parked classes](https://github.com/Aphrodine-wq/G-Rump/blob/876766327171eed40df89ef1d58c8c9a475c8def/Sources/GRump/Intelligence/Daemon/AutonomousLoop.swift#L31-L68), [outcomes and fail-stop](https://github.com/Aphrodine-wq/G-Rump/blob/876766327171eed40df89ef1d58c8c9a475c8def/Sources/GRump/Intelligence/Daemon/AutonomousLoop.swift#L68-L121), [active agent loop](https://github.com/Aphrodine-wq/G-Rump/blob/876766327171eed40df89ef1d58c8c9a475c8def/Sources/GRump/ViewModels/ChatViewModel%2BAgentLoop.swift#L14-L52).
- Basis: structural.
- Confidence: medium-high.
- Caveats: At a different organizational recursion level, a multi-installation manager could exist, but is not evidenced here.

### Absence scope

- Surfaces inspected: goals/priority ranking, activity/outcome records, failure disablement, proactive suggestion urgency, shared model instance and task lifecycle.
- Plausible first-party paths checked: autonomous goal allocation, selection by success, feedback from completed tasks, current live-task status and parallel tool execution.
- Why no material first-party path remains: The source supports selecting the next serial task and local safeguards, not a whole-current decision over independently operating S1 units and binding returns.

## S3*

- State: —
- Function: Independently audit S3's account of current operations against alternative operating evidence, returning corrective accountability.
- Disturbance / variety regulated: Inaccurate code patches, underestimated bugs and incorrect claims about task completion.
- Decisive decision or feedback right: A separate routed review-model call inspects code-change summaries and reports vulnerabilities, but no independently grounded audit of S3's whole-current management or corrective managerial return is shown.
- Decision owner: Task-level `AdversarialReviewEngine`; no qualifying S3* audit owner.
- Supporting / enforcement mechanisms: Build-mode post-run review, optional alternate model, severity-coded findings, regression tracking, local auto-verification and code summaries.
- Closure path: Code changes → review JSON findings → assistant message in conversation; ordinary code QA feedback, not S3 claim → independent operational challenge → S3 correction.
- Why this is / is not agent-owned: An LLM reviewer can challenge work product, but receives the agent-provided change summary and task context, not independently obtained cross-unit operating reality.
- Evidence: [review source and independent routed model](https://github.com/Aphrodine-wq/G-Rump/blob/876766327171eed40df89ef1d58c8c9a475c8def/Sources/GRump/Intelligence/Analysis/AdversarialReview.swift#L170-L258), [post-run presentation of report](https://github.com/Aphrodine-wq/G-Rump/blob/876766327171eed40df89ef1d58c8c9a475c8def/Sources/GRump/ViewModels/ChatViewModel%2BAgentPostRun.swift#L43-L68), [verification closure](https://github.com/Aphrodine-wq/G-Rump/blob/876766327171eed40df89ef1d58c8c9a475c8def/Sources/GRump/ViewModels/ChatViewModel%2BAgentLoop.swift#L230-L235).
- Basis: structural.
- Confidence: high for code-review scope; medium for negative S3* classification.
- Caveats: Code QA can provide genuine value without constituting the VSM audit function.

### Absence scope

- Surfaces inspected: adversarial review prompt/input/output, post-run review injection, automated verification, regression tracker, activity logs and user feedback.
- Plausible first-party paths checked: separate model, critic/red-team role, bug findings, confidence calibration, verification, source-level telemetry and task completion checks.
- Why no material first-party path remains: Findings target individual changes, and no qualified S3 current-control claim exists for them to independently verify or correct.

## S4

- State: —
- Function: Model prospective external-environment change, choose future adaptation options, and couple them to inside-and-now capabilities.
- Disturbance / variety regulated: Shifting coding practices, project requirements, user preferences and future tool/model fit are possible drivers of adaptation.
- Decisive decision or feedback right: The reflection model changes local behavioral lessons from prior work, while potential skill changes require user approval; no separate prospective external horizon/options and S3 return are established.
- Decision owner: `ReflectionEngine` owns internal performance lesson distillation; `ProactiveEngine` owns reactive local suggestions, not a demonstrated S4 strategy function.
- Supporting / enforcement mechanisms: RunOutcome telemetry, model review of transcript, learned lesson store and subsequent prompt injection, skill proposal approvals, ambient git/app events, schedule-based reminders and cooldown learning.
- Closure path: Local task outcomes → model-based lessons → relevant lessons in later S1 prompt; or local/ambient event → suggested user action. The external future → capability option → S3-mediated current adaptation path is missing.
- Why this is / is not agent-owned: The reflection model has real autonomous cross-session learning discretion, but it regulates recurring operating errors; generically calling this learning or self-improvement does not meet the more specific S4 function.
- Evidence: [reflection prompts and applied lesson operations](https://github.com/Aphrodine-wq/G-Rump/blob/876766327171eed40df89ef1d58c8c9a475c8def/Sources/GRump/Intelligence/Learning/ReflectionEngine.swift#L54-L175), [run outcomes and reflection trigger](https://github.com/Aphrodine-wq/G-Rump/blob/876766327171eed40df89ef1d58c8c9a475c8def/Sources/GRump/ViewModels/ChatViewModel%2BAgentPostRun.swift#L104-L187), [lessons back into prompt](https://github.com/Aphrodine-wq/G-Rump/blob/876766327171eed40df89ef1d58c8c9a475c8def/Sources/GRump/ViewModels/ChatViewModel%2BPromptBuilding.swift#L62-L99), [proactive local hooks](https://github.com/Aphrodine-wq/G-Rump/blob/876766327171eed40df89ef1d58c8c9a475c8def/Sources/GRump/Views/Proactive/ProactiveEngine.swift#L327-L390).
- Basis: structural.
- Confidence: medium-high.
- Caveats: An operator can prompt an explicit external-market/trend analysis through generic tools; a possible user-initiated task is not an installed recurrent S4 right.

### Absence scope

- Surfaces inspected: post-run outcome ledger and model reflection, skill proposals, lesson injection, temporal git history intelligence, proactive/ambient scheduler and model routing.
- Plausible first-party paths checked: cross-session experience learning, preferences and corrections, project code change trends, external-service/MCP access, future reminders and approval-gated new skill capabilities.
- Why no material first-party path remains: Implemented signals characterize local execution, project changes or immediately observable user activity; no specific prospective external model and adaptation alternatives with current-control return appear in the inspected first-party loops.

## S5

- State: —
- Function: Legitimately define ultimate purpose, identity and binding governing values over current operation and future adaptations.
- Disturbance / variety regulated: Unsafe project changes, sensitive screen content, protected branches, secret writes and conflicting user/agent goals.
- Decisive decision or feedback right: Human operator sets identity and protection rules and approves risky writes. The `ConscienceGate` applies deterministic restrictions but cannot legitimately redefine ultimate policy or settle identity-level conflicts.
- Decision owner: Human for final authorization, first-party deterministic gate for enforcement; no independent agent-owned S5.
- Supporting / enforcement mechanisms: SOUL/MIND files, values roster, Conscience verdicts, protected-branch/secret rules, explicit daemon approvals, configuration flags and protected skill-file write approval.
- Closure path: Configured values and policy → pre-tool gate/approval → allow or reject local S1 action. No legitimate agent decision to change ultimate values with governing return to S3/S4.
- Why this is / is not agent-owned: Programmatic policy enforcement and prompt-level identity are not the authority to decide organizational identity or alter governing purpose.
- Evidence: [Conscience deterministic policy](https://github.com/Aphrodine-wq/G-Rump/blob/876766327171eed40df89ef1d58c8c9a475c8def/Sources/GRump/Intelligence/Mind/ConscienceGate.swift#L13-L82), [tool enforcement and human approvals](https://github.com/Aphrodine-wq/G-Rump/blob/876766327171eed40df89ef1d58c8c9a475c8def/Sources/GRump/ViewModels/ChatViewModel%2BToolExecution.swift#L69-L100), [prompt-level SOUL/MIND context](https://github.com/Aphrodine-wq/G-Rump/blob/876766327171eed40df89ef1d58c8c9a475c8def/Sources/GRump/ViewModels/ChatViewModel%2BPromptBuilding.swift#L48-L105).
- Basis: structural.
- Confidence: high for static rule enforcement; medium-high for S5 absence.
- Caveats: Human oversight is deliberately designed here and must not be mislabeled as agent policy autonomy.

### Absence scope

- Surfaces inspected: SOUL/MIND prompt integration, Conscience gate, values roster, config and protected files, daemon approval coordinator and learning/skill proposal mechanisms.
- Plausible first-party paths checked: self-descriptive identity, values enforcement, human approval, skill/lesson revision, safety gate toggling and protected file writes.
- Why no material first-party path remains: Decisions over protected actions remain human or fixed-rule-controlled. No first-party agent holds a legitimate final organizational identity/ultimate-policy adjudication right.

## Distributed OSS parent arrangement

GitHub contributors and maintainers may review G-Rump source and releases, but development governance is outside this running macOS application boundary. External model providers and MCP tools can supply inference and actions without transferring their separate management structures into this first-party assessment.

## Self-hosted and non-human modes

G-Rump is a locally launched app that can use configured remote or local providers. The optional daemon selects goals without an immediate new chat prompt but waits for idle time, reuses the interactive coding loop, approves every mutating action with the operator, and never pushes. Reflection automatically modifies later prompt lessons when enabled; skill definitions require user review. No continuous unattended deployment or independent metasystem ownership is inferred.

## Recursion

One user/application task organization is analyzed. The interactive and daemon modes are serial invocations of the same operating agent; separate code-review and reflection model calls serve task-level verification and local learning. Multi-instance coordination, an operating enterprise, or provider management would change the system-in-focus and require new evidence.

## Variety and escalation

Observed tool failures return to the model within S1; auto-verification may reopen the same loop. Repeated daemon failures disable future scheduling and notify the user. The Conscience gate and human approval reject sensitive actions. Code-review findings and post-run reflections return to conversations and later task prompts. These are bounded error handling and learning paths, not evidence of the complete S2–S5 metasystem chain.

## Evidence gaps

- Pinned first-party source only; a macOS runtime or real provider-backed coding trace was not available in this Linux review environment.
- Daemon completion currently relies on `!viewModel.isLoading` after starting a conversation; an end-to-end success result, true worktree isolation and real per-mutation user approvals were not independently exercised.
- Reflection lesson feedback and review routing are wired by source, but quality, causality and safety of model-generated lessons or reviewer findings were not measured.

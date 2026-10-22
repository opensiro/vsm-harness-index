---
harness_id: caveman-code
project_name: Caveman Code
repository: https://github.com/JuliusBrussee/caveman-code
review_ref: 3a21be115c32aa27288c8ed6d860d9aa1b65d2c5
reviewed_at: 2026-10-22
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Caveman Code

## Review boundary

- System in focus: the published `@juliusbrussee/caveman-code` terminal/headless coding agent, its bundled specialist-agent definitions, first-party `@juliusbrussee/caveman-agent` runtime and goal loop, not an external multi-agent platform assembled by a user.
- Purpose and identity: interpret coding requests, inspect/change a local repository with model-selected tools, and optionally iterate on a user-specified coding goal within configured caps.
- Relevant environment: the project checkout, git worktrees, shell/filesystem, selected model providers, live tool observations, session context, user permissions and explicitly spawned specialist processes.
- Standard-distribution boundary: released `caveman`/`caveman-code` CLI, its `AgentSession`, registered first-party tools, bundled `explore`/`implementer`/`reviewer`/`critic`/`tester` agents, optional `task`/background child and shipped goal command. No custom user-written team manager is presumed.
- Credited operating / distribution surfaces: model/tool loop, built-in read/edit/write/bash/search tools, first-party subagent `task` dispatch, project/user agent-definition loader, worktree isolation, child reports, background mailbox/status, the goal-runner and budgets, session handling and runtime approvals.
- Adjacent first-party surfaces excluded from ownership: developer benchmarks and tests, repository maintainers, externally deployed cavemem service, user-provided custom agents/MCP extensions and any post-freeze successor project or uninstalled adaptation service.
- Operating modes considered: standard terminal agent, print/headless mode, bundled synchronous single/parallel/chained subagents, optional `background: true` specialist, opt-in `isolation: worktree` implemented for the bundled implementer, and `caveman goal` bounded iterative runs.
- Recursion level: top-level user-directed coding service with optional specialist coding subprocesses; not the GitHub development organization or an external tool fleet.
- Reviewed revision: [`3a21be115c32aa27288c8ed6d860d9aa1b65d2c5`](https://github.com/JuliusBrussee/caveman-code/tree/3a21be115c32aa27288c8ed6d860d9aa1b65d2c5), frozen candidate intake #200.
- Observation date: 2026-10-22; structural source review, not a provider-backed runtime success benchmark.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

The published CLI enters an `AgentSession`, registers file/shell/search and delegation tools, and runs the `@juliusbrussee/caveman-agent` model/tool feedback loop. The model sees returned tool results and can choose a next coding action. Unlike packages that merely expose a library child, the bundled specialist definitions are loaded from `packages/coding-agent/agents/*.md`; `task` can dispatch real child CLI processes in single, parallel (up to seven tasks, four concurrent) and chain modes. Bundled `implementer` receives a separate git worktree, while `explore`, `reviewer` and `critic` have read-only tool sets. Background agents can be steered through a mailbox and inspected through status.

This constitutes additional task-performing S1 capacity but does not, by itself, close S2: parallel results are collated as OK/FAIL, child worktree edits/commits are left for a parent/operator to inspect, and `autoCleanupWorktree` only removes unchanged worktrees. No first-party code reconciles conflicting sibling commitments, resolves their file-change interference, or returns a conflict-specific settlement that demonstrably adjusts separately viable cells. The worktree creator also silently falls back to a shared working directory when isolation creation fails. Reviewer/critic personas investigate code quality for a requested task, not a managerial S3 truth claim.

The goal-runner can restart bounded goal iterations, track repository-change/sentinel progress, maintain a cost ledger and pause on nonprogress; these are self-regulation of current coding delivery. Optional memory and extensions do not establish prospective S4 governance or S5 final-purpose rights.

Primary evidence: [model execution and tool returns](https://github.com/JuliusBrussee/caveman-code/blob/3a21be115c32aa27288c8ed6d860d9aa1b65d2c5/packages/agent/src/agent-loop.ts#L153-L238), [session runtime wiring](https://github.com/JuliusBrussee/caveman-code/blob/3a21be115c32aa27288c8ed6d860d9aa1b65d2c5/packages/coding-agent/src/core/agent-session.ts#L3199-L3363), [task dispatch and cleanup](https://github.com/JuliusBrussee/caveman-code/blob/3a21be115c32aa27288c8ed6d860d9aa1b65d2c5/packages/coding-agent/src/core/tools/task.ts#L479-L618), [goal-runner](https://github.com/JuliusBrussee/caveman-code/blob/3a21be115c32aa27288c8ed6d860d9aa1b65d2c5/packages/coding-agent/src/core/goal-loop/goal-runner.ts#L240-L350).

## Operational model

A single root model chooses coding actions and may delegate specialized chunks to independently executing child coding models. Returned child output guides the root model's next task-local action; a bounded goal command can iterate the root process under cost/time/progress rules. Tool and child restrictions protect local execution. No separate whole-system viable metasystem decision owner is evidenced above task delivery.

## S1

- State: A
- Function: Deliver requested repository investigation and implementation through autonomous model choices and feedback-controlled file/shell actions, including bundled specialist subprocesses.
- Disturbance / variety regulated: Unknown repository contents, coding specifications, tool failures, agent-generated results, changing file state, incomplete plans and session context pressure.
- Decisive decision or feedback right: The root model selects tool/action/delegation steps after observations; child models separately choose steps within their assigned read-only or implementer tool permissions.
- Decision owner: First-party root `AgentSession` model loop, with model-driven subagent subprocesses for delegated specialist coding tasks.
- Supporting / enforcement mechanisms: Read/edit/write/bash/search tools, `task` and `agent` delegation, bounded child spawn, provider selection, parent event/session continuation, worktree scope, goal iterations and state persistence.
- Closure path: Coding instruction → model action or specialist delegation → local tool/subagent executes → output/status or error returns → model chooses correction or completion; goal mode may initiate another bounded pass.
- Why this is / is not agent-owned: Actual next coding and tool decisions depend on model-generated reasoning and observed results, not a fixed shell script alone; policies and recursion limits constrain its actions.
- Boundary reachability: The released CLI constructs all tool definitions and loads bundled specialist agent definitions; model tools include `task` and code/file tool paths, while goal mode invokes the real CLI for new iterations.
- Evidence: [tool feedback loop](https://github.com/JuliusBrussee/caveman-code/blob/3a21be115c32aa27288c8ed6d860d9aa1b65d2c5/packages/agent/src/agent-loop.ts#L180-L235), [first-party tool registry](https://github.com/JuliusBrussee/caveman-code/blob/3a21be115c32aa27288c8ed6d860d9aa1b65d2c5/packages/coding-agent/src/core/tools/index.ts#L165-L240), [bundled agent loader](https://github.com/JuliusBrussee/caveman-code/blob/3a21be115c32aa27288c8ed6d860d9aa1b65d2c5/packages/coding-agent/src/core/agent-defs/loader.ts#L175-L264), [child dispatch](https://github.com/JuliusBrussee/caveman-code/blob/3a21be115c32aa27288c8ed6d860d9aa1b65d2c5/packages/coding-agent/src/core/tools/task.ts#L710-L865).
- Basis: structural.
- Confidence: high for real distributed first-party model/tool loops; no model/provider live outcome was run for this assessment.
- Caveats: Child ability depends on selected provider/model, task tool exposure and permissions; task success and reported benchmark results were not reproduced.

## S2

- State: —
- Function: Attenuate actual interference between concurrently viable coding S1 cells and return coordination adjustments to the affected cells.
- Disturbance / variety regulated: Simultaneous code-edit collisions, incompatible child patches, sibling priorities and shared workspace contention.
- Decisive decision or feedback right: The root can delegate and inspect results, but no shipped conflict-observation/settlement procedure that actively adjusts sibling coding operations is established; separate worktrees prevent simple simultaneous writes only in configured modes.
- Decision owner: No qualifying distinct S2 decision owner. Root parent is a task delegator; worktree helpers and concurrency mapper are mechanical isolation/scheduling.
- Supporting / enforcement mechanisms: Parallel/chain fan-out, MAX_CONCURRENCY=4, bounded recursion, opt-in implementer worktree, no-change auto-cleanup, status and parent-to-background-agent mailbox.
- Closure path: Parent delegates → each child acts in an isolated or shared checkout → summarized success/failure and worktree path return to parent. There is no demonstrated interference detection → negotiated correction → multiple S1 resynchronization closure.
- Why this is / is not agent-owned: The isolation/transport machinery can reduce risk but does not own adaptive cross-S1 conflict damping; parent model's general task choices are still S1-level delivery unless an explicit regulation loop is shown.
- Evidence: [worktree fallback and returned artifacts](https://github.com/JuliusBrussee/caveman-code/blob/3a21be115c32aa27288c8ed6d860d9aa1b65d2c5/packages/coding-agent/src/core/tools/task.ts#L479-L625), [parallel OK/FAIL aggregation](https://github.com/JuliusBrussee/caveman-code/blob/3a21be115c32aa27288c8ed6d860d9aa1b65d2c5/packages/coding-agent/src/core/tools/task.ts#L754-L861), [worktree cleanup keeps changed branches](https://github.com/JuliusBrussee/caveman-code/blob/3a21be115c32aa27288c8ed6d860d9aa1b65d2c5/packages/agent/src/worktree.ts#L163-L231), [bundled worktree implementer](https://github.com/JuliusBrussee/caveman-code/blob/3a21be115c32aa27288c8ed6d860d9aa1b65d2c5/packages/coding-agent/agents/implementer.md#L1-L30).
- Basis: structural.
- Confidence: medium-high for bounded absence; worktrees demonstrably implement isolation, not measured collaborative conflict closure.
- Caveats: A human or custom manager can merge worktrees and arbitrate children, but that external operation cannot be credited as installed S2 autonomy.

### Absence scope

- Surfaces inspected: native `task` single/parallel/chain/background dispatch, child registry/message mailbox, worktree creation/cleanup, bundled agent modes and goal loop.
- Plausible first-party paths checked: parallel collision prevention, sibling outputs, worktree branches, parent steering, reviewer and critic role separation, chained handoff and recursive child limits.
- Why no material first-party path remains: No surfaced conflict-specific adaptive decision and compensated execution by affected child S1s; isolation and reporting do not implement that closure even though child agents are real.

## S3

- State: —
- Function: Select binding whole-current commitments, priorities and scarce resources among independent operating work cells.
- Disturbance / variety regulated: Multiple delegated work requests, concurrency saturation, task failure, goal nonprogress and token/time budget pressure.
- Decisive decision or feedback right: Model-based delegation is within the user's current coding request; max task/concurrency/iteration/budget constants enforce caps rather than strategic reallocations of viable units.
- Decision owner: Root coding S1 for task choices; deterministic goal-runner, resource counters and dispatch scheduler for fixed operational limits; no distinct S3 owner established.
- Supporting / enforcement mechanisms: `Task` mode/queue, max seven children/four concurrent, goal ledger, wall-clock and no-progress pause, output statuses, tool permissions.
- Closure path: Goal/task call → bounded child or iteration → result ledger/status → same coding task continues, stops or pauses; no autonomous whole-current cross-S1 commitment reallocation.
- Why this is / is not agent-owned: A parent can issue more tasks, but no evidence distinguishes managing the present whole organization from executing and decomposing one coding goal.
- Evidence: [bounded parallel dispatcher](https://github.com/JuliusBrussee/caveman-code/blob/3a21be115c32aa27288c8ed6d860d9aa1b65d2c5/packages/coding-agent/src/core/tools/task.ts#L710-L862), [goal caps and progress ledger](https://github.com/JuliusBrussee/caveman-code/blob/3a21be115c32aa27288c8ed6d860d9aa1b65d2c5/packages/coding-agent/src/core/goal-loop/goal-runner.ts#L230-L347).
- Basis: structural.
- Confidence: medium-high.
- Caveats: A deployment that overlays durable task portfolio governance is outside this frozen product boundary.

### Absence scope

- Surfaces inspected: parent subagent dispatch, goal-runner, task status, budget/progress signals, tool registry, session controls and user commands.
- Plausible first-party paths checked: child concurrency caps, reallocation/reprioritization, long-horizon goal progress, cancellation, worktree resources and current task ownership.
- Why no material first-party path remains: Observed controllers either govern one user coding request or apply static limits; no self-owned whole-current operating-cell settlement loop is evidenced.

## S3*

- State: —
- Function: Audit S3 management's operating claims from a distinct, complementary evidentiary channel and correct S3 when claims diverge.
- Disturbance / variety regulated: Incorrect patches, missing edge cases, failing tests, misleading status and inaccurate progress assessment.
- Decisive decision or feedback right: The shipped read-only reviewer and critic report code/plan defects to the parent, not independently challenge S3's actual allocation or operating reality.
- Decision owner: Specialist task reviewers acting within delegated coding S1 work, with no S3* claim/audit/corrective management right.
- Supporting / enforcement mechanisms: Bundled `reviewer`, `critic` and `tester` prompts, read-only tool restrictions, logs, goal progress signal and local tests.
- Closure path: Parent requests code review → reviewer reads code/plan → task-level findings return to parent coding model; no current S3 decision → independent alternate operating reality → binding S3 correction path.
- Why this is / is not agent-owned: Independent LLM criticism exists, but independence from the author of code does not entail complementary independence from a whole-current management claim or authority to correct it.
- Evidence: [reviewer task definition](https://github.com/JuliusBrussee/caveman-code/blob/3a21be115c32aa27288c8ed6d860d9aa1b65d2c5/packages/coding-agent/agents/reviewer.md#L1-L35), [critic task definition](https://github.com/JuliusBrussee/caveman-code/blob/3a21be115c32aa27288c8ed6d860d9aa1b65d2c5/packages/coding-agent/agents/critic.md#L1-L35), [goal progress heuristic](https://github.com/JuliusBrussee/caveman-code/blob/3a21be115c32aa27288c8ed6d860d9aa1b65d2c5/packages/coding-agent/src/core/goal-loop/goal-runner.ts#L288-L332).
- Basis: structural.
- Confidence: high for task-level reviewer roles; medium-high for absent management audit.
- Caveats: User-authored agents could target management verification, but the shipped definitions do not.

### Absence scope

- Surfaces inspected: bundled reviewer/critic/tester, task outputs, goal signals, session history and worktree changes.
- Plausible first-party paths checked: source-code review independence, plan critique, alternative progress checks, test execution and actual S3 decision accountability.
- Why no material first-party path remains: No S3 decision owner exists at the tested level and no separate auditing loop verifies its binding current-management choices.

## S4

- State: —
- Function: Observe prospective external environmental change, evaluate future alternatives and return an adaptive capability plan into current S3 action.
- Disturbance / variety regulated: New provider offerings, future user requirements, changing codebase dependencies and evolving development workflows.
- Decisive decision or feedback right: The root or goal loop pursues present user tasks; future research/model switches or skills are operator-directed or task-local, not first-party external-future strategy selection.
- Decision owner: Human for goal/environment/provider selection, coding S1 for task tactics and deterministic goal controls for continuation; no S4 strategist established.
- Supporting / enforcement mechanisms: Optional extensions, providers, persistent memory, goal prompts, iterative summary carryover and local code-change progress checks.
- Closure path: Existing user goal → repeated code-model iterations informed by previous edits/cost → success sentinel or cap, without external-futures intelligence → adaptation decision → S3 adoption.
- Why this is / is not agent-owned: Iteration/replanning can improve current code but neither forecasts the outside environment nor governs introduction of new systemic capability.
- Evidence: [goal-runner iteration, signal and summary](https://github.com/JuliusBrussee/caveman-code/blob/3a21be115c32aa27288c8ed6d860d9aa1b65d2c5/packages/coding-agent/src/core/goal-loop/goal-runner.ts#L230-L350), [user-provided runtime agent extensions](https://github.com/JuliusBrussee/caveman-code/blob/3a21be115c32aa27288c8ed6d860d9aa1b65d2c5/packages/coding-agent/src/core/agent-defs/loader.ts#L175-L264).
- Basis: structural.
- Confidence: medium-high.
- Caveats: A future-facing task specified by a user is possible but does not evidence a standing S4 governance function.

### Absence scope

- Surfaces inspected: goal iteration/prompt/state, memory hooks, provider selection, child roles and project/user agent resource discovery.
- Plausible first-party paths checked: long-running goals, internal performance learning, external-futures scanning, strategic option selection, model switching and adoption into standing operations.
- Why no material first-party path remains: The inspected autonomy closes on present coding task progress, not a separately defined external strategic environment and S3-mediated adaptation mandate.

## S5

- State: —
- Function: Legitimately determine final identity, values and policy for the whole coding organization and transmit binding governance.
- Disturbance / variety regulated: Untrusted repository content, risky shell operations, incompatible user directions and potentially harmful code changes.
- Decisive decision or feedback right: Human user/project chooses the goal, model, tool scope and approval mode; the package constrains actions but does not acquire legitimate authority to redefine ultimate purpose or values.
- Decision owner: Human operator and configured policy/permission checks, not a first-party final-policy agent.
- Supporting / enforcement mechanisms: Plan/read-only versus auto mode, tool subsets and disallowed tool lists, user instructions, fixed task caps and prompt constraints.
- Closure path: User and project policy → session/tool/subagent restrictions → execute/refuse/request approval of particular action; no agent-originated ultimate-governance return to S3/S4.
- Why this is / is not agent-owned: A model can decide how to perform coding work while governing goals, authorization and identity stay user-supplied.
- Evidence: [mode overrides in task](https://github.com/JuliusBrussee/caveman-code/blob/3a21be115c32aa27288c8ed6d860d9aa1b65d2c5/packages/coding-agent/src/core/tools/task.ts#L68-L95), [per-agent allowed tools](https://github.com/JuliusBrussee/caveman-code/blob/3a21be115c32aa27288c8ed6d860d9aa1b65d2c5/packages/coding-agent/src/core/agent-defs/loader.ts#L96-L153), [human-created goals and caps](https://github.com/JuliusBrussee/caveman-code/blob/3a21be115c32aa27288c8ed6d860d9aa1b65d2c5/packages/coding-agent/src/core/goal-loop/goal-runner.ts#L240-L273).
- Basis: structural.
- Confidence: high regarding externally specified ultimate purpose; no governing self-legitimation claim.
- Caveats: `auto` increases operational discretion but not legitimate S5 authority.

### Absence scope

- Surfaces inspected: user goal creation, bundled system/agent prompts, task modes, tool allowlists, approval paths, optional project configuration and agent recursion caps.
- Plausible first-party paths checked: source identity text, model policy, human tool confirmations, recursive child governance and ultimate goal/value conflict adjudication.
- Why no material first-party path remains: No actor within this distribution is given a legitimate final-purpose or values decision loop above user-defined coding service.

## Distributed OSS parent arrangement

The source repository contains maintainers, developer tests, evaluation scripts and an adjacent cavemem integration. Those belong to product development or separate systems, not automatically to the shipped user-session S2–S5 governance. A user may construct a richer organization with this toolkit; its custom authority requires its own assessment boundary.

## Self-hosted and non-human modes

The CLI can execute as a local/hosted model client, in print mode or as repeated autonomous `goal` subprocesses. Background specialist subprocesses run without immediate user input and can be steered via mailbox. That extends S1 work delivery but does not itself confer whole-current resource, future adaptation or ultimate policy authority.

## Recursion

The root coding S1 is decomposed into specialist S1 task cells where shipped child processes choose real tools. Child depth and fan-out are bounded; task outputs return to the root. Worktree isolation protects code working copies but does not independently close S2 conflict regulation. Tool calls within one specialist are below the S1 recursion boundary.

## Variety and escalation

Unanticipated tool outcomes and specialist failures feed the root coding model. Branch-isolated implementer edits remain for later inspection, static concurrency caps prevent overload, and goal mode pauses for nonprogress or budget exhaustion. These are useful containment/feedback mechanisms, but no closed authority beyond coding S1 was established in this frozen source.

## Evidence gaps

- Source inspection only; no live provider-backed child-task, colliding sibling worktree, explicit merge/reconciliation or goal execution was performed.
- Worktree creation can degrade to shared cwd on failure; the source provides no conflict-specific recovery loop before the child launches in that case.
- The README's reported benchmark numbers were not replicated or used as governance evidence.

---
harness_id: davecode
project_name: DaveCode
repository: https://github.com/DMRLZZ/DaveCode
review_ref: 271910253a005845174c2410dc15675877a9883e
reviewed_at: 2026-10-24
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-24
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A(P)
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# DaveCode

## Review boundary

- System in focus: the shipped DaveCode local-first TypeScript coding/goal-engine organization at frozen `271910253a005845174c2410dc15675877a9883e`: built-in coding `Executor`, `AutonomousRunner`, `GoalOrchestrator`/`GoalService`, first-party task graphs/brain, optional independent acceptance judge, workspace exclusion, and CLI/API orchestration.
- Purpose and identity: implement repository tasks as validated changes, optionally coordinate a multi-role goal into executable code/artifact tasks, and return task outcomes while conserving configured provider quota.
- Relevant environment: local Git projects, task graph/dependencies, current project and global brain, validation tools, diffs, provider/model responses, account/quota conditions, project/operator configuration and approval of delivered work.
- Standard-distribution boundary: first-party `@davecode/core` built-in router-backed coding loop, runner, goal mode and acceptance judge, wired by published CLI/server and controlled by project task graph/goal storage. External model provider responses, TypeSafe Jev service, optional Claude Code CLI executor and other vendor CLI sessions are dependencies; their unshipped internal policies, agents and tools are not credited.
- Credited operating / distribution surfaces: `packages/core/src/autonomous/{create,executor,runner,judge,tools,validator,workspace-lock}.ts`, `packages/core/src/goal/{create,orchestrator,service,code-tasks,plan,store}.ts`, `packages/core/src/brain/{graph,project,context}.ts`, `packages/cli/src/runtime.ts`, `packages/cli/src/commands/tasks.ts`, `packages/server/src/routes/tasks.ts` and the supported CLI/API configuration.
- Adjacent first-party surfaces excluded from ownership: `site/`, development-only fixtures, test mocks and integration tests as executed auditors, browser/UI displays unless they feed a supported operating decision, provider-specific remote agent internals, CI/release automation and public contributor governance.
- First-party operating / deployment modes considered: `davecode run` one-task and continuous runner with native `builtin` executor; `goal` planner → role/artifact/code tasks → reviewer → bounded replanning; optional judge `none`, `jev`, `llm`; operator task-graph edits and runner controls through CLI/API; shared local workspace gate. The separate opt-in `claude-cli` executor is treated as external delegation, not the basis of the positive coding S1 claim.
- Recursion level: a local DaveCode project/goal organization composed of a first-party code execution cell, discrete role/artifact work cells and a goal-level metasystem. Distinct tasks are operational commitments; the assessment does not assume every one-shot role call is a fully recursive viable system.
- Reviewed revision: `271910253a005845174c2410dc15675877a9883e`.
- Observation date: 2026-10-24.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.7`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.7`.

## Repository architecture

DaveCode ships a provider/account gateway and a separate agentic engineering plane. `createEngine` wires config, SQLite persistence, credentials, quota windows, usage and account selection. The gateway's circuit breaker and route policies decide where model calls go, but they do not independently decide software-engineering task actions.

`BuiltinExecutor.createSession` instantiates `WorkspaceTools` and a direct OpenAI-style tool-call loop over the first-party `Router`. It submits task/project context plus tool definitions, executes requested file/command/finish tools, appends each tool result and iterates until `finish` or a configured bound. `AutonomousRunner` takes a ready task from `TASK_GRAPH.json`, isolates work on a task Git branch, runs the executor, validates the actual workspace with configured tests, optionally applies a separate acceptance judge, supplies failure feedback into bounded repair passes and then commits/merges or opens a PR. It records updated task status and progress in the project brain.

`GoalOrchestrator` is a separate shipped composition: a planner model produces bounded role assignments/tasks; the orchestrator executes dependency-ready artifact or code work (code delegates into the first-party runner), records task outcome and token usage, then a reviewer model receives the entire goal task/status/output summary and decides completion, retries and additional work. This is more than a static sequence: reviewer feedback changes the next round's commitments within maximum tasks, rounds and tokens. `GoalService` exposes start/list/get/cancel and persists goals. The CLI project wiring instantiates both goals and runner around a shared `WorkspaceLock`. The in-process lock excludes simultaneous top-level goal and standalone runner ownership of a writable Git tree and permits nested code execution under the goal owner.

Two additional distinctions matter. The task-graph CLI and REST endpoints let an operator view current task status and edit future task priorities/dependencies/acceptance while the runner reads that same graph at selection time. This supports a separate operator-managed current-control mode, but ordinary `stop` alone is not S3. The acceptance judge defaults to `none`; selecting the shipped `jev` mode calls an independent TypeSafe Jev judgment service on task acceptance criteria, real staged diff and validation report. `llm` is another optional model-judge path, but its independence from the implementation model depends on operator route choice and is not needed for the positive S3* claim. No local model/provider invocation was run in this assessment.

Primary pinned evidence:

- [`packages/core/src/autonomous/executor.ts`](https://github.com/DMRLZZ/DaveCode/blob/271910253a005845174c2410dc15675877a9883e/packages/core/src/autonomous/executor.ts)
- [`packages/core/src/autonomous/runner.ts`](https://github.com/DMRLZZ/DaveCode/blob/271910253a005845174c2410dc15675877a9883e/packages/core/src/autonomous/runner.ts)
- [`packages/core/src/autonomous/judge.ts`](https://github.com/DMRLZZ/DaveCode/blob/271910253a005845174c2410dc15675877a9883e/packages/core/src/autonomous/judge.ts)
- [`packages/core/src/autonomous/workspace-lock.ts`](https://github.com/DMRLZZ/DaveCode/blob/271910253a005845174c2410dc15675877a9883e/packages/core/src/autonomous/workspace-lock.ts)
- [`packages/core/src/goal/orchestrator.ts`](https://github.com/DMRLZZ/DaveCode/blob/271910253a005845174c2410dc15675877a9883e/packages/core/src/goal/orchestrator.ts)
- [`packages/core/src/goal/code-tasks.ts`](https://github.com/DMRLZZ/DaveCode/blob/271910253a005845174c2410dc15675877a9883e/packages/core/src/goal/code-tasks.ts)
- [`packages/cli/src/runtime.ts`](https://github.com/DMRLZZ/DaveCode/blob/271910253a005845174c2410dc15675877a9883e/packages/cli/src/runtime.ts)
- [`packages/server/src/routes/tasks.ts`](https://github.com/DMRLZZ/DaveCode/blob/271910253a005845174c2410dc15675877a9883e/packages/server/src/routes/tasks.ts)
- [`docs/ARCHITECTURE.md`](https://github.com/DMRLZZ/DaveCode/blob/271910253a005845174c2410dc15675877a9883e/docs/ARCHITECTURE.md)

## Operational model

The native code execution actor chooses repository modifications from actual source/test feedback (S1). Goal mode also contains role-specific model/artifact work cells whose completed work feeds the goal's current management conversation. Top-level standalone runner and goal-driven operations can both seek the same writable project; the shared lock directly attenuates that concrete operational interference, but grants no autonomous S2 decision over how to reschedule rejected work (S2 constructor). Goal reviewer decisions about ongoing commitments and retries close a bounded autonomous S3 mode, while task-graph API edits can support a distinct operator-owned S3 mode. Optional Jev-based evidence review independently challenges a proposed code change through staged Git diff plus validation outcomes; rejection changes the repair loop (S3*). Internal planning, quota routing and current-task repair are not an external-and-prospective organizational S4, and operator configuration is not runtime S5 identity governance.

## S1 — Operations

- State: A
- Function: execute user-directed coding and goal/artifact work through model-owned next-action decisions and actual workspace/output feedback.
- Disturbance / variety regulated: varying repository state, implementation alternatives, task dependencies, real tool outputs, failed quality gates, incomplete context, provider constraints and uncompleted goal artifacts.
- Decisive decision or feedback right: choose which first-party coding tools to invoke and what code/action to attempt next; for artifact roles, generate a task-specific output from received objective and dependency evidence.
- Decision owner: the selected model-backed `BuiltinExecutor` actor and goal role agents in supported first-party mode. The runner selects/validates task transitions deterministically and does not inherit the model's coding discretion.
- Supporting / enforcement mechanisms: `Router`, quota/budget, `WorkspaceTools`, token/iteration ceilings, Git branch operations, task context, retry/repair policy, goal store and acceptance validators.
- Closure path: current task/context → model requests repository tools → `WorkspaceTools` executes → exact tool result enters same conversation → next coding decision; goal artifact calls persist their output and return it to the subsequent goal review/task selection.
- Boundary reachability: `createRunner` constructs the shipped built-in executor; `wireProject` exposes it through CLI/server; `GoalOrchestrator.runCodeTask` invokes the first-party runner while artifact work calls `router.complete` with first-party role prompts.
- Why this is / is not agent-owned: removing the model-backed code/role actor leaves graph selection, router/failover and verification machinery, but no discretionary construction of task-specific code edits or artifacts from evidence.
- Evidence: [`executor.ts`](https://github.com/DMRLZZ/DaveCode/blob/271910253a005845174c2410dc15675877a9883e/packages/core/src/autonomous/executor.ts); [`runner.ts`](https://github.com/DMRLZZ/DaveCode/blob/271910253a005845174c2410dc15675877a9883e/packages/core/src/autonomous/runner.ts); [`orchestrator.ts`](https://github.com/DMRLZZ/DaveCode/blob/271910253a005845174c2410dc15675877a9883e/packages/core/src/goal/orchestrator.ts); [`runtime.ts`](https://github.com/DMRLZZ/DaveCode/blob/271910253a005845174c2410dc15675877a9883e/packages/cli/src/runtime.ts).
- Basis: explicit + structural.
- Confidence: high for shipped source construction; no provider-backed outcomes measured.
- Caveats: only the native `builtin` composition supplies this positive S1 path. External CLI executor modes may have their own decision owner outside DaveCode.

## S2 — Coordination

- State: C
- Function: attenuate competing operations' shared-worktree mutation conflict between the first-party standalone autonomous runner and first-party goal operation that invokes code tasks on the same project.
- Disturbance / variety regulated: both top-level execution modes check out Git branches and commit in one writable workspace; simultaneous use would race on branch/index/worktree state.
- Distinct S1 units: the standalone `AutonomousRunner` coding unit and the goal-directed role/code operational composition exposed as a separate first-party `GoalService`. They are distinct runnable operational entry points to one repository, not two model calls within the same tool step.
- Inter-S1 disturbance: competing top-level `runner` and `goal` ownership of one Git worktree can cause Git checkout/commit interference. `workspace-lock.ts` explicitly identifies this conflict.
- Attenuating coordination relation: `wireProject` instantiates one shared `WorkspaceLock`; the runner acquires it as owner `runner`, goal mode holds it as `goal`, a competing owner receives `busy`, and nested goal-owned code runner uses reentrant `goal` ownership.
- Feedback into subsequent S1 behaviour: rejected launch returns `RunnerError('busy')`/`GoalError('busy')` to the parent CLI/API caller, preventing conflicting execution; subsequent initiation must occur after the holder releases the lock. A model-owned cross-unit rescheduler is not instantiated.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: this is not a DAG edge or role routing: a first-party lock is explicitly tied to a real shared-Git mutation disturbance between two separately startable coding/goal operating units and changes their admission behaviour.
- Decisive decision or feedback right: grant or refuse exclusive entry to the shared writable-workspace operating boundary and report the conflict for later caller scheduling.
- Decision owner: deterministic `WorkspaceLock` enforces exclusivity according to fixed rules; a developer/operator would have to compose an autonomous policy for what postponed work to start next. The shipped S2-specific feedback path supports constructor state `C`, not autonomous `A`.
- Supporting / enforcement mechanisms: ownership-counting `WorkspaceLock`; shared `wireProject` runtime wiring; runner `acquireLock` and `GoalService.start`; goal `RunnerCodeTasks` reentrant owner.
- Closure path: goal/runner start proposal → shared lock grants or rejects → only one writer progresses; rejection returns `busy` to caller and later attempts may proceed after release. Autonomous adaptive cross-unit scheduling remains to be composed.
- Boundary reachability: the published CLI project wiring always shares the lock between the first-party goal and standalone runner for that project; this does not depend on an unshipped plugin.
- Why this is / is not agent-owned: the conflict-specific first-party lock enforces a fixed partition and returns a decision, but a coding model does not autonomously decide who waits, retries or reallocates operations after a collision.
- Evidence: [`workspace-lock.ts`](https://github.com/DMRLZZ/DaveCode/blob/271910253a005845174c2410dc15675877a9883e/packages/core/src/autonomous/workspace-lock.ts); [`goal/service.ts`](https://github.com/DMRLZZ/DaveCode/blob/271910253a005845174c2410dc15675877a9883e/packages/core/src/goal/service.ts); [`goal/code-tasks.ts`](https://github.com/DMRLZZ/DaveCode/blob/271910253a005845174c2410dc15675877a9883e/packages/core/src/goal/code-tasks.ts); [`cli/runtime.ts`](https://github.com/DMRLZZ/DaveCode/blob/271910253a005845174c2410dc15675877a9883e/packages/cli/src/runtime.ts).
- Basis: explicit + structural.
- Confidence: medium; the claim is limited to exclusive shared-worktree admission, not rich semantic task coordination.
- Caveats: lock is in-process and does not prove cross-process or distributed exclusion. Alternative top-level execution modes may be seen as exclusive rather than co-active S1s; this is the principal semantic boundary to review before canonical admission.

## S3 — Inside-and-now control

- State: A(P)
- Function: regulate the present whole-goal task commitment population through reviewer-informed retries/new tasks and operator-managed task-graph priorities/constraints.
- Disturbance / variety regulated: some goal tasks fail or become blocked, artifact/code outcomes vary, budget/task/round limits constrain current work and changed task priorities may require revised commitment selection.
- Whole-system current view: goal reviewer receives every task's status, role, attempt count, title, notes and bounded actual artifact excerpt, plus budget context and current round. The CLI tasks listing and API expose the shared project task graph to operators.
- Current-control decision scope: the goal reviewer decides when to retry failed work, which additional tasks enter the next round, and whether the bounded entire goal is complete. In operator mode, current project task priority/dependency/acceptance edits and status changes alter which pending commitment `nextTask` selects in later runner iterations.
- Decisive decision or feedback right: revise current task commitments from whole-goal evidence and return the decision to task execution, or let legitimate project operator do so through task-graph control.
- Decision owner: goal reviewer model actor for the autonomous `A` mode; project operator using first-party task list/edit/status API for the distinct `P` mode. Fixed task/round/token limits enforce bounds but do not own the discretionary choice.
- Supporting / enforcement mechanisms: `GoalOrchestrator.review`, `applyRetries`/`normalizeTasks`, persisted `GoalStore`, task graph validation, `nextTask`, CLI/HTTP routes and fixed budgets/workspace locks.
- Closure path: goal outcome/status/artifact excerpts → reviewer model produces retry/new task/finish judgment → orchestrator alters tasks and executes the next round. Separately, operator reads task graph → changes priority/dependencies/status → persisted project graph → next runner selection consumes the revised commitments.
- Boundary reachability: first-party `GoalService` is constructed by `createGoalService` and wired into the published CLI/runtime; task listing/edit endpoints and runner graph reads are part of the same installed project mode.
- Why this is / is not agent-owned: without the goal reviewer the deterministic DAG/limit machinery can walk given tasks but cannot make evidence-driven judgments to revise the current goal task portfolio. In operator mode the human makes those current-control decisions; the API only stores/enforces them.
- Evidence: [`goal/orchestrator.ts`](https://github.com/DMRLZZ/DaveCode/blob/271910253a005845174c2410dc15675877a9883e/packages/core/src/goal/orchestrator.ts); [`goal/service.ts`](https://github.com/DMRLZZ/DaveCode/blob/271910253a005845174c2410dc15675877a9883e/packages/core/src/goal/service.ts); [`cli/commands/tasks.ts`](https://github.com/DMRLZZ/DaveCode/blob/271910253a005845174c2410dc15675877a9883e/packages/cli/src/commands/tasks.ts); [`server/routes/tasks.ts`](https://github.com/DMRLZZ/DaveCode/blob/271910253a005845174c2410dc15675877a9883e/packages/server/src/routes/tasks.ts); [`brain/graph.ts`](https://github.com/DMRLZZ/DaveCode/blob/271910253a005845174c2410dc15675877a9883e/packages/core/src/brain/graph.ts).
- Basis: explicit + structural.
- Confidence: medium-high for bounded goal-level S3; the operator mode is project-current-control only, not a claim of global DaveCode governance.
- Caveats: a standalone runner's deterministic priority choice and `stop` button alone are not the autonomous S3 basis. The positive autonomous mode rests on the goal reviewer receiving whole-goal status and revising current commitments, not merely task decomposition.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Model-backed goal reviewer | Completed/failing tasks and full-goal status/artifact excerpts after a round | Review proposes retries/additional work/finish; orchestrator updates task set and re-executes ready work | `goal/orchestrator.ts` |
| Parent (`P`) | Local project operator | Task board/graph view reveals priority, dependency or acceptance change in current commitments | CLI/API task edits persist; next first-party runner selection consumes updated graph | `cli/commands/tasks.ts`, `server/routes/tasks.ts`, `brain/graph.ts`, `autonomous/runner.ts` |

## S3* — Complementary audit

- State: A
- Function: supply an optional independent acceptance judgment over actual staged code changes beyond the production actor's summary and configured deterministic check results, with corrective return.
- Disturbance / variety regulated: coding actor may self-report completion despite a patch failing the task's acceptance criteria even when configured lints/tests pass.
- Claim being audited: that the implementation diff fulfills each task acceptance criterion and can be accepted/merged.
- Ordinary reporting path: built-in executor returns its summary and the `Validator` runs configured checks; without an independent configured judge, `NoneJudge` always passes after the checks.
- Complementary access path: when `runner.judge.kind='jev'` the first-party runner obtains actual staged Git diff/stat plus test validation, passes them and task acceptance to dedicated TypeSafe Jev via `JevJudge`, and receives a separate calibrated acceptance verdict. The alternative `llm` judge exposes the same inputs but its routing independence is not assumed.
- Independence boundary: the Jev decision is made by an external dedicated evaluator on fresh raw Git diff/validation evidence with a separate model/service from the coding actor's implementation session, not by replaying the implementer's own success message. Source-level evidence supports the path; no live independence/accuracy experiment was run.
- Who acts on findings: `AutonomousRunner` converts a failed judge verdict into a failure report for the subsequent implementation repair cycle, or marks the task FAILED when the configured retry limit is reached.
- Decisive decision or feedback right: judge whether the actual change satisfies acceptance criteria independently of the coding actor's conclusion; determine acceptance or corrective retry.
- Decision owner: the optional dedicated TypeSafe Jev evaluator model in the first-party `jev` supported mode; DaveCode's schema parser, confidence threshold, and runner enforce/transport its judgment without owning the evaluator's discretionary assessment.
- Supporting / enforcement mechanisms: `createJudge`, acceptance inputs/diff capture, score threshold, zod response validation, validator, repair-pass state machine and bounded failure handling.
- Closure path: candidate diff/test results → independent Jev assessment → pass reaches delivery or reject is incorporated into failure text → built-in coding agent sees report and repairs → fresh diff is rejudged.
- Boundary reachability: `createRunner` selects `createJudge(cfg.judge, ...)` from first-party runner config, which permits `jev`; `runTask` invokes it after successful deterministic validation as part of installed CLI/goal-driven coding operation.
- Why this is / is not agent-owned: the separate evaluator owns the acceptance judgment, while the runner and threshold gate enforce the returned verdict; it is not ordinary self-review by the production actor in this supported mode.
- Evidence: [`autonomous/judge.ts`](https://github.com/DMRLZZ/DaveCode/blob/271910253a005845174c2410dc15675877a9883e/packages/core/src/autonomous/judge.ts); [`autonomous/create.ts`](https://github.com/DMRLZZ/DaveCode/blob/271910253a005845174c2410dc15675877a9883e/packages/core/src/autonomous/create.ts); [`autonomous/runner.ts`](https://github.com/DMRLZZ/DaveCode/blob/271910253a005845174c2410dc15675877a9883e/packages/core/src/autonomous/runner.ts); [`config/schema.ts`](https://github.com/DMRLZZ/DaveCode/blob/271910253a005845174c2410dc15675877a9883e/packages/core/src/config/schema.ts).
- Basis: explicit + structural.
- Confidence: medium; optional independent judgment/return is clearly wired, but practical audit quality was not tested.
- Caveats: default `judge.kind='none'` has no independent audit; an `llm` judge on the same model route cannot be assumed independent. The `A` state credits the explicit first-party opt-in dedicated Jev mode only and does not imply all deployments instantiate it.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party external-and-prospective organizational capability adaptation loop established within the supported project runtime.
- Disturbance / variety regulated: quota exhaustion, model availability and current-task failures are detected; internal replanning/repair and operational failover respond to present conditions, not outside-and-then organizational capability evolution.
- Decisive decision or feedback right: no separate prospectively sourced option to redesign current organizational capability with an adoption decision was established.
- Decision owner: not established for S4.
- Supporting / enforcement mechanisms: quota windows, provider route scoring/circuit breakers, goal plan/review rounds, retry/repair feedback and global/project memory.
- Closure path: no externally/future informed capability-option generation → judgment/adoption → return into current organizational capability is wired; immediate failover and goal replanning return only into current operations.
- Why this is / is not agent-owned: role planner and goal reviewer plan/revise task actions, while router algorithms choose among configured providers; none is evidenced as autonomous prospective redesign of DaveCode's capability repertoire.
- Evidence: [`docs/ARCHITECTURE.md`](https://github.com/DMRLZZ/DaveCode/blob/271910253a005845174c2410dc15675877a9883e/docs/ARCHITECTURE.md); [`goal/orchestrator.ts`](https://github.com/DMRLZZ/DaveCode/blob/271910253a005845174c2410dc15675877a9883e/packages/core/src/goal/orchestrator.ts); [`engine.ts`](https://github.com/DMRLZZ/DaveCode/blob/271910253a005845174c2410dc15675877a9883e/packages/core/src/engine.ts).
- Basis: structural absence review.
- Confidence: medium-high within the frozen source distribution.
- Caveats: tracking provider quotas over future windows is predictive operational routing, not evidence of a distinct S4 capability-adaptation organization.

### Absence scope

- Surfaces inspected: provider/account router and budget architecture, goal planner/reviewer loop, task graph, global/project brain, native code repair and CLI configuration.
- Plausible first-party paths checked: model-route substitution based on future quotas, environment research/option development, future project planning, automatic adoption of new tools/providers/workflows and parent-approved strategic redesign.
- Why no material first-party path remains: the reviewed mechanisms choose and retry work with existing tools/providers and adjust current routing. They do not construct externally informed options for changing later organizational capability and return an adoption decision to current control.

## S5 — Policy and identity

- State: —
- Function: no first-party runtime identity/ultimate-policy adjudication loop established at the declared project harness boundary.
- Disturbance / variety regulated: goal text, route settings, allowed tools, account policy, branch/merge modes, acceptance and operator task edits constrain execution but do not decide harness ultimate identity.
- Decisive decision or feedback right: no identity/ultimate-policy issue is escalated, decided by legitimate authority and returned as a durable authoritative runtime policy revision.
- Decision owner: not established for S5; operator/developer configuration sets constraints rather than closing a distinct VSM S5 function.
- Supporting / enforcement mechanisms: `DaveConfig`, `DAVECODE_SYSTEM_PROMPT`, CLI/API task edits, security checks, route settings, scoped workspaces and execution limits.
- Closure path: no identity/policy issue → legitimate ultimate authority → authoritative decision → returned policy governing later operation is instantiated.
- Why this is / is not agent-owned: planner/reviewer/task owner decisions concern the task portfolio, not the identity of the coding organization; static config and permission gates do not exercise S5 authority by themselves.
- Evidence: [`config/schema.ts`](https://github.com/DMRLZZ/DaveCode/blob/271910253a005845174c2410dc15675877a9883e/packages/core/src/config/schema.ts); [`goal/orchestrator.ts`](https://github.com/DMRLZZ/DaveCode/blob/271910253a005845174c2410dc15675877a9883e/packages/core/src/goal/orchestrator.ts); [`server/routes/tasks.ts`](https://github.com/DMRLZZ/DaveCode/blob/271910253a005845174c2410dc15675877a9883e/packages/server/src/routes/tasks.ts).
- Basis: structural absence review.
- Confidence: high within runtime boundary.
- Caveats: this negative is not a statement about maintainer governance for future DaveCode releases.

### Absence scope

- Surfaces inspected: runtime configuration, system/task prompts, goal definition and stores, task-graph controls, provider/account policy and bounded execution/approval paths.
- Plausible first-party paths checked: self-modifying constitution, goal-objective editing as possible identity revision, ultimate-policy escalation to project operator, human PR/merge approval and downstream governance of releases.
- Why no material first-party path remains: goal and task decisions govern current user work, while configuration/rules predefine constraints. No shipped function identifies an ultimate identity conflict, closes it under legitimate policy authority and returns that ruling into later autonomous operation.

## Recursion

The first-party project organization has operational coding and bounded role/artifact task cells, with the goal-level planner/reviewer regulating present work. Each code task executes through a concrete model/tool loop, but the review does not elevate every one-shot role model invocation into a self-sufficient nested viable system. The shared workspace lock regulates the collision between separately invocable goal and runner operating surfaces, not an arbitrary external agent swarm.

## Variety and escalation

DaveCode attenuates operational variety through validated DAG dependencies, bounded task/round/token budgets, exclusive workspace ownership, provider quotas/circuit breaker, deterministic validation and repair limits. It amplifies response repertoire with first-party code tools, role-specific goal planning and independent optional judge assessment. Failed work can return to goal reviewer for re-planning or retry; operator API updates affect the live task graph. A Jev rejection carries complementary evidence directly into a bounded repair cycle. These are scoped regulatory channels, not proof of production safety or overall viability.

## Evidence gaps

- This is source-first semantic analysis of the frozen public TypeScript repository. No live model/provider, coder, Claude CLI, Jev or browser run was performed; no empirical quality claim is made.
- The S2 constructor conclusion is narrowly about first-party shared-worktree exclusion between two top-level operating modes; independent simultaneous organization-wide S1 population and autonomous conflict-resolution behavior are not claimed.
- S3=A(P) is confined to goal task-portfolio control and the operator's task-graph mode. It does not equate generic task delegation, a kill button or static budget enforcement with S3.
- S3*=A is an optional Jev audit mode with structurally independent diff-based judgment and returned correction. The existence of the path does not establish its observed audit accuracy, calibration, or effect on real coding outcomes.
- Direct first-party TypeScript/unit tests were read as supporting source evidence; dependency installation/test execution was not attempted. Deterministic Index validation can check artifact completeness but cannot prove semantic correctness.

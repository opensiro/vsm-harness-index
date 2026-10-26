---
harness_id: crewctl
project_name: CrewCtl
repository: https://github.com/omergocmen/CrewCtl
review_ref: 834c399cf28a9e83e7e47f81544ed52dfbeb92cc
reviewed_at: 2026-10-26
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# CrewCtl

## Review boundary

- System in focus: The self-hosted CrewCtl Node.js orchestration engine controlling an operator-model CLI and delegated specialist coding CLI processes over one active task and, optionally, multiple isolated tasks.
- Purpose and identity: Turn an operator's goal into planned, delegated, verified coding-agent work, with queue, review, progress and deliverable reporting.
- Relevant environment: The user's code repository, installed and authenticated Codex/Claude/Gemini/OpenCode CLI adapters, operating-system process and filesystem controls, Git, optional MCP servers and web command center.
- Standard-distribution boundary: The published `crewctl` executable/Node server with the packaged `orchestrator/src` engine, role prompts, task state, default configuration, optional supported task worktrees, and installed compatible CLI agents. Real LLM and provider decisions are supplied by external runtimes; CrewCtl owns their wiring and rights.
- Credited operating / distribution surfaces: `package.json` CLI entry and npm package, `orchestrator/src/{cli,engine,store,cli-registry,worktree,verify,mcp,schedule,server}.js`, `orchestrator/roles/{operator,executor,planner,reviewer}.md`, `orchestrator/config.default.json` and supported operator configuration.
- Adjacent first-party surfaces excluded from ownership: Repository maintainer/CI and npm release process; command-center presentation alone; local fake-agent test doubles and smoke fixtures; external agent CLI implementations, subscriptions, auth, prompts and tools not instantiated by the first-party engine.
- First-party operating / deployment modes considered: Balanced task loop with operator planning, specialist execution and optional reviewer; fast execution mode; default single-task run; optional `maxConcurrentTasks > 1` with `worktree.mode: task`; optional deterministic verification gate, MCP role routing, and ask/auto approval.
- Recursion level: One CrewCtl-controlled local operator team carrying out a user task; for S2 only, the supported supervisor's two or more concurrent task teams with separate worktrees.
- Reviewed revision: `834c399cf28a9e83e7e47f81544ed52dfbeb92cc`.
- Observation date: 2026-10-26.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

CrewCtl is a zero-dependency Node.js local CLI/HTTP service that discovers installed external coding CLIs and invokes them through an operator-led runtime. `Engine.runTask` loads a queue item and existing project context, calls the configured operator LLM for structured assignments, normalizes its choices against enabled specialist capabilities, applies dependency ordering, invokes specialists in subprocesses, records returned evidence and failures, optionally runs configured real verification commands, and asks the operator for a decision or proceeds through a guarded completion path. Balanced mode can add planner and reviewer roles to an implementation chain. The engine stores task state, messages, checkpoint/evidence and outputs and may revise the per-project `CONTEXT.md` after successful work. It can expose an HTTP dashboard, MCP server and scheduled queue inputs.

The user must accept autonomous CLI execution before the engine runs; the `ask` risk gate and externally provided credentials bound execution. Separate worktrees are opt-in rather than the default. The default verification command list is empty. Reviewer read-only discipline is a packaged prompt/MCP role policy, not a proof of OS-level read-only filesystem containment for all configured external agents.

Primary source: [package and CLI](https://github.com/omergocmen/CrewCtl/blob/834c399cf28a9e83e7e47f81544ed52dfbeb92cc/package.json), [engine](https://github.com/omergocmen/CrewCtl/blob/834c399cf28a9e83e7e47f81544ed52dfbeb92cc/orchestrator/src/engine.js), [role contract](https://github.com/omergocmen/CrewCtl/blob/834c399cf28a9e83e7e47f81544ed52dfbeb92cc/orchestrator/roles/reviewer.md), [configuration](https://github.com/omergocmen/CrewCtl/blob/834c399cf28a9e83e7e47f81544ed52dfbeb92cc/orchestrator/config.default.json).

## Operational model

The S1 units are specialist coding agents operating against tasks in the shared working tree or configured task worktree. CrewCtl's operator-agent controls current planning, role allocation, continuation and delivery decisions for a task team; it is distinct from deterministic queue/process enforcers and from the user selecting high-level objectives. A reviewer delegation supplies a separate check of implementer claims, but the standard routing does not force reviewer identity to differ from the implementer or enforce read-only filesystem access for every external CLI. Optional parallel task teams each acquire an isolated worktree to prevent cross-task filesystem interference; this proves a specific coordination primitive without autonomous inter-team arbiter ownership. No agent is credited with changing CrewCtl's ultimate identity or autonomously revising a forward-looking portfolio of adaptation options.

## S1 — Operations

- State: A
- Function: Carry out an assigned code or research task through model-directed inspection, editing/tool use, testing and result reporting.
- Disturbance / variety regulated: Repository files, build/test feedback, failed tool calls, task errors and unexpected implementation constraints.
- Decisive decision or feedback right: The specialist LLM CLI chooses task-specific implementation and verification actions inside the delegated work; it returns a result/error for subsequent rounds.
- Decision owner: Configured coding CLI specialist invoked from the first-party `runAssignmentWithRecovery` / `runCli` path, under the assignment's role and limits.
- Supporting / enforcement mechanisms: Subprocess adapter catalog, working-directory sandbox settings, timeouts, retry/failover, task store, optional worktrees and verification commands.
- Closure path: Operator-selected assignment → specialist model/tool execution against code → output and observable files → stored `state.results` → new operator/team context.
- Boundary reachability: The installed `crewctl` engine's normal `runTask` path invokes the configured agent executable via `runAssignments` and `runAssignmentWithRecovery`, using its returned output in the same live task; fake CLI fixtures are not needed to establish the shipped wiring.
- Why this is / is not agent-owned: The model-driven coding specialist selects actions. CrewCtl orchestrates and constrains them; the externally installed CLI itself is a required runtime dependency and is not incorrectly claimed as CrewCtl source code.
- Evidence: [engine `runAssignments`, `runCli` and `runTask`](https://github.com/omergocmen/CrewCtl/blob/834c399cf28a9e83e7e47f81544ed52dfbeb92cc/orchestrator/src/engine.js), [supported adapters](https://github.com/omergocmen/CrewCtl/blob/834c399cf28a9e83e7e47f81544ed52dfbeb92cc/orchestrator/src/cli-registry.js), [executor role](https://github.com/omergocmen/CrewCtl/blob/834c399cf28a9e83e7e47f81544ed52dfbeb92cc/orchestrator/roles/executor.md).
- Basis: explicit first-party operational wiring; no live external model test.
- Confidence: high.
- Caveats: Installed provider/account capability and task success cannot be inferred from source or mocked CLI tests.

## S2 — Coordination

- State: C
- Function: Prevent operational cross-contamination among simultaneous task teams operating on one source repository.
- Disturbance / variety regulated: Two independently running task teams can overwrite each other's files, reuse working state or misattribute status events when they share a directory and process identity.
- Decisive decision or feedback right: The first-party task-level mode constructs separate worker engines and assigns each task a distinct Git worktree/branch and correctly tagged event stream; the configuration/user still selects this mode and no autonomous inter-team conflict arbiter is evidenced.
- Decision owner: The concrete isolation and queue-claiming primitive is owned by CrewCtl's supervisor/worker and `worktree` runtime; no separate S2 agentic decision owner is closed.
- Supporting / enforcement mechanisms: `maxConcurrentTasks`, per-worker engine slots, task claiming/skip IDs, worktree creation from HEAD, task-indexed messages and event routing.
- Closure path: Concurrent queue items → separate task worker and worktree identity → each specialist reads/writes only its team's checkout → results committed to separate local branches and events routed to the correct task; any higher-level conflict resolution between output branches is not supplied.
- Boundary reachability: The shipped supervisor accepts `maxConcurrentTasks > 1` and `worktree.mode: task` through documented config and invokes `worktree.create` in the live task path; the native concurrency test exercises two simultaneous team runs, separate checkout paths and correctly associated events.
- Why this is / is not agent-owned: This is a specific first-party S2 construction and isolation path, not an autonomous agent evaluating conflicts and changing pairwise coordination; hence `C`, not `A`.
- Distinct S1 units: Two concurrent per-task specialist coding-agent teams, each with its own operator, task state and repository worktree.
- Inter-S1 disturbance: Shared-file modifications, workspace contamination, queue double-claim and cross-task event attribution.
- Attenuating coordination relation: The supervisor claims tasks once and routes workers into distinct worktrees/branches with per-task event IDs.
- Feedback into subsequent S1 behaviour: Each team's next CLI run executes in its own checkout and consumes its own task-specific results instead of the other team's dirty files or events.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The dedicated worktree/multi-worker mode directly attenuates a concrete interference between independent active task teams, although it stops short of automatic merge/conflict arbitration.
- Evidence: [worktree runtime](https://github.com/omergocmen/CrewCtl/blob/834c399cf28a9e83e7e47f81544ed52dfbeb92cc/orchestrator/src/worktree.js), [engine concurrent worker slots and task checkout](https://github.com/omergocmen/CrewCtl/blob/834c399cf28a9e83e7e47f81544ed52dfbeb92cc/orchestrator/src/engine.js), [native concurrency test](https://github.com/omergocmen/CrewCtl/blob/834c399cf28a9e83e7e47f81544ed52dfbeb92cc/orchestrator/test/concurrency.test.js), [opt-in mode defaults](https://github.com/omergocmen/CrewCtl/blob/834c399cf28a9e83e7e47f81544ed52dfbeb92cc/orchestrator/config.default.json).
- Basis: first-party source and test-defined interference case.
- Confidence: medium.
- Caveats: Disabled by default; `C` is narrower than resource-priority coordination or agentic resolution of conflicting changes across branches. User must enable concurrency and task worktrees.

## S3 — Inside-and-now control

- State: A
- Function: Control the active task team against its current objective, evidence, limits and interruptions.
- Disturbance / variety regulated: Ambiguous task decomposition, failed delegated work, unavailable agents, red verification gates, incomplete delivery and excessive review rounds.
- Decisive decision or feedback right: The operator LLM makes structured assignment/dependency decisions and subsequent `continue` vs `complete`/replan decisions from returned current-state reports; deterministic guards constrain or occasionally bypass its judgment.
- Decision owner: Configured operator-model CLI with CrewCtl's first-party plan/review prompts and validation.
- Supporting / enforcement mechanisms: `normalizeAssignments`, role-chain completion, dependency runner, failure feedback, progress state, evidence/diff snapshots, verify gate, completion-proof and budget guards.
- Closure path: Task and whole-team context → model-selected assignments → execution/reviewer/verifier evidence → operator model's next decision → new assignments or guarded task completion.
- Boundary reachability: Normal `runTask` invokes `invokeOperatorJson` on the planning and review phases using `operatorPrompt`; decisions reach `runAssignments` and `complete` in the same task process.
- Why this is / is not agent-owned: The operator chooses priorities, specialists, remedial work and task completion from team state. The built-in queue, dependency ordering and hard verification constraints execute rather than originate that plan.
- Whole-system current view: Current task prompt, project context, enabled team capabilities, prior assignments/results/messages, verification evidence and resource/round status appear in the operator prompts and state.
- Current-control decision scope: Select task-work distribution, delegate or repair blocked work, re-plan remaining commitments, decide completion within the configured guardrails.
- Evidence: [engine `operatorPrompt`, `runTask`, `runAssignments`, `runVerifyGate`](https://github.com/omergocmen/CrewCtl/blob/834c399cf28a9e83e7e47f81544ed52dfbeb92cc/orchestrator/src/engine.js), [operator role](https://github.com/omergocmen/CrewCtl/blob/834c399cf28a9e83e7e47f81544ed52dfbeb92cc/orchestrator/roles/operator.md).
- Basis: explicit first-party model decision and closed task loop.
- Confidence: high.
- Caveats: Fast mode intentionally elides some second-stage operator review; no parent modifier is inferred from manual task creation, start/stop or risky-plan approval.

## S3* — Complementary audit

- State: C
- Function: Challenge implementation reports with direct code/test inspection and return an independent quality finding into task control.
- Disturbance / variety regulated: A specialist can report success while files are unchanged, acceptance criteria are missing, or a claimed test was not executed.
- Decisive decision or feedback right: A review-specialist prompt requests first-hand filesystem/test observations and `VERDICT: PASS|FAIL`; the engine parses the verdict and passes it to operator decision/completion guards.
- Decision owner: The configured external review-capable CLI model when a reviewer is assigned; the default role contract establishes the auditor-specific path but does not guarantee distinct reviewer identity or universal enforced read-only rights.
- Supporting / enforcement mechanisms: `reviewer.md` inspection rubric, `kind: review` delegation, dependency ordering after implementation, `extractVerdict`, latest-review checks and delivery-proof safeguards.
- Closure path: Implementation reports/files → separately invoked reviewer model inspecting files and tests → parsed verdict and findings → operator receives review message and replans, or gated PASS allows completion.
- Boundary reachability: In shipped balanced mode, `ensureBalancedRoleChain` automatically adds a review assignment if a compatible agent exists; `specialistPrompt` loads the packaged reviewer role and the live `runAssignments` path parses the result.
- Why this is / is not agent-owned: The reviewer LLM would choose the finding, but independence is not enforced when the same configured agent is eligible for implementation and review, and the read-only rule is partly prompt-based; therefore the first-party complementary audit constructor is credited as `C`, without asserting universal closed independent `A` audit.
- Claim being audited: Implementer statement that work meets the task's acceptance criteria, changes exist and verification evidence is sufficient.
- Ordinary reporting path: Implementation agent output and task completion report to the operator.
- Complementary access path: Reviewer is instructed to inspect changed files, call sites, tests and diff evidence directly, independently of the implementation report; configured read-only MCP route is optional.
- Independence boundary: Separate review delegation/role and verdict, but a distinct underlying CLI identity and truly enforced filesystem read-only access are not mandatory in default configuration.
- Who acts on findings: Operator LLM through its review-phase decision and the first-party completion/verification guard.
- Evidence: [reviewer role](https://github.com/omergocmen/CrewCtl/blob/834c399cf28a9e83e7e47f81544ed52dfbeb92cc/orchestrator/roles/reviewer.md), [balanced role chain and review handling](https://github.com/omergocmen/CrewCtl/blob/834c399cf28a9e83e7e47f81544ed52dfbeb92cc/orchestrator/src/engine.js), [MCP routing](https://github.com/omergocmen/CrewCtl/blob/834c399cf28a9e83e7e47f81544ed52dfbeb92cc/orchestrator/src/mcp.js).
- Basis: function-specific first-party audit path; independence gap bounds state at `C`.
- Confidence: medium-high.
- Caveats: Reviewer availability depends on installed/configured CLI agents; prompt-only review discipline is not proof of technical read-only confinement.

## S4 — Outside-and-then intelligence

- State: —
- Function: No demonstrated agent-owned prospective adaptation portfolio/option selection returning into the organization's current capability.
- Disturbance / variety regulated: Changing project facts and provider availability are potential environmental changes; CrewCtl handles them as current task execution context or deterministic resilience.
- Decisive decision or feedback right: No separate S4 option-development and prospective adaptation right evidenced.
- Decision owner: Not established within the credited runtime.
- Supporting / enforcement mechanisms: Post-success operator-authored `CONTEXT.md` revision, per-task memory, scheduled tasks, CLI discovery and provider retry/failover.
- Closure path: Context refresh may inform the *next task*, but no evidenced external/future distinction → adaptation-option judgment → governance/current-capability change closes S4.
- Why this is / is not agent-owned: LLM maintenance of facts about work already completed is useful memory, not by itself environmental scanning and prospective adaptation ownership.
- Evidence: [engine `reviseProjectContext` and resilience](https://github.com/omergocmen/CrewCtl/blob/834c399cf28a9e83e7e47f81544ed52dfbeb92cc/orchestrator/src/engine.js), [scheduling](https://github.com/omergocmen/CrewCtl/blob/834c399cf28a9e83e7e47f81544ed52dfbeb92cc/orchestrator/src/schedule.js).
- Basis: bounded structural negative.
- Confidence: medium-high.
- Caveats: Developers could add an adaptive strategy, but such a possible extension is not first-party evidenced.

### Absence scope

- Surfaces inspected: Operator plan/review/context refresh prompts, task store and memory, schedule module, CLI discovery, retry/failover controls and role configuration.
- Plausible first-party paths checked: Revision of project profile after successful edits, provider-health fallbacks, future scheduled queue items and specialist research delegations.
- Why no material first-party path remains: These maintain current knowledge or initiate concrete queued tasks; none binds environmental foresight to autonomous design/selection of future capability options returned to the current controller.

## S5 — Policy and identity

- State: —
- Function: No first-party identity/ultimate-policy authority loop is established for the local CrewCtl team.
- Disturbance / variety regulated: Risky plans, permissions and unsafe tooling affect ordinary task execution but are not proven existential identity or organization-purpose decisions.
- Decisive decision or feedback right: No authoritative identity/policy revision decision and returned organizational change evidenced.
- Decision owner: User selects goals and grants initial autonomous consent; ordinary per-plan approval does not establish S5 authority at this assessed recursion.
- Supporting / enforcement mechanisms: `autonomousConsentAcceptedAt`, `approvalMode`, risky keyword patterns, sandbox mode, MCP role gating, CLI overrides and resource budgets.
- Closure path: Human ask/approve may unblock a task, but not an identity-level issue → legitimate policy judgment → governing return.
- Why this is / is not agent-owned: Neither the operator's task plans nor the human's runtime consent decides what the CrewCtl organization ultimately is or ought to become.
- Evidence: [engine consent and plan approval](https://github.com/omergocmen/CrewCtl/blob/834c399cf28a9e83e7e47f81544ed52dfbeb92cc/orchestrator/src/engine.js), [default config](https://github.com/omergocmen/CrewCtl/blob/834c399cf28a9e83e7e47f81544ed52dfbeb92cc/orchestrator/config.default.json), [MCP role filters](https://github.com/omergocmen/CrewCtl/blob/834c399cf28a9e83e7e47f81544ed52dfbeb92cc/orchestrator/src/mcp.js).
- Basis: bounded structural negative.
- Confidence: medium-high.
- Caveats: External owner and maintainer governance may determine ultimate project identity, but repository presence of those actors does not establish this function's returned first-party path.

### Absence scope

- Surfaces inspected: User onboarding and consent, current-risk approvals, agent roles, policy/sandbox configuration, CLI/MCP switches, task delivery and code-maintainer boundary.
- Plausible first-party paths checked: Approval gate for risky assignments, manual engine start/stop, hard sandbox settings, user-written instructions and maintainer configuration changes.
- Why no material first-party path remains: These are ordinary task controls or externally owned design authority; no qualifying identity-level agenda, legitimate ultimate decision and operational return loop is implemented in the assessed team.

## Distributed OSS parent arrangement

Maintainers and users may configure or develop CrewCtl independently; no repository-visible function-specific shared parent decision-and-return path is credited as an additional S3/S4/S5 mode. The assessed recursion is one locally configured operator-led task team.

## Self-hosted and non-human organizational boundary

Credited autonomy is exercised by configured operator/specialist CLI models when present; running the Node service alone does not supply a language-model actor. The available human approval mode is real execution governance but does not automatically qualify as parent-governed VSM ownership.

## Evidence gaps and reproducibility

- Source-frozen review at `834c399cf28a9e83e7e47f81544ed52dfbeb92cc`; no live paid LLM/provider execution or empirical coding quality was measured.
- Native `npm test` executed on 2026-10-26 with external subprocess permission: `ui smoke`, `cli flow`, `server flow`, `skills`, and `schedule` passed before `team-flow` stopped at an expected `AUTH_INVALID` versus observed `CLI_NOT_FOUND` classification. This is a test/environment failure, not evidence that actual agent work passed.
- The exact independent-auditor guarantee and agentic S2 conflict arbitrator are *not* established; reviewer and worktree roles are bounded as `C`.

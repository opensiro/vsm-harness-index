---
harness_id: eta
project_name: eta
repository: https://github.com/0xfe-project/eta
review_ref: 6b62da886b225391a157c7486e93b85aef73a17c
reviewed_at: 2026-11-17
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: ?
autonomy_s5: P
---

# eta

## Review boundary

- System in focus: The first-party self-hosted eta multi-agent workbench at the frozen source, including its Bun host, session kernel, TaskBoard, Captain organizational agent, group conversations and optional machine daemons.
- Purpose and identity: Let a local owner operate task-performing, persistent agents across projects, sessions, tools, task dependencies, supervisory reviews, proposed workforce changes and retained policy settings.
- Environment: User requests, models selected by the owner, installed tools and MCP providers, local projects/worktrees, one or more registered machines and their online/offline status, task results and approvals.
- Standard-distribution boundary: Source-shipped `apps/eta`, `packages/eta-core`, `packages/eta-harness`, agent/session and product plugins; user-supplied model accounts and third-party external runtimes are dependencies, not automatically first-party decision owners.
- Credited operating / distribution surfaces: In-process model/tool kernel, RunPump, task graph/runner, Captain identity/service/tools/supervisor, proposal/approval callbacks, prompt-version storage and host wiring; optional remote daemon sessions considered when first-party bridged.
- Adjacent first-party surfaces excluded from ownership: Browser UI, test scripts, docs, release updater and upstream contributor governance except as corroboration of actual entry points; an external Claude/Codex runtime's independent behavior is not donated to eta.
- First-party operating / deployment modes considered: Configured local model-backed agent sessions; multiple agents with shared project tasks; Captain model-backed current supervision if enabled; parent user-authorized Captain changes and base prompt rules; routines with short Captain sessions.
- Recursion level: One owner-assembled eta workbench with distinct subordinate task-executing agents and Captain; separate task projects and human owner are not merged into one agent.
- Reviewed revision: `6b62da886b225391a157c7486e93b85aef73a17c` (`main` at discovery).
- Observation date: 2026-11-17.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The core Runner uses a live configured model and tools; its turn loop asks the provider, executes tool calls through middleware and returns outcomes to the next model turn. RunPump wakes the idle session when new input arrives. The host stores project/agent/session/task states in SQLite and session journals and exposes optional remote-machine execution.

TaskBoard and TaskGraph provide agent task creation, dependency gating, recovery, workspace base derivation and status propagation. Every task's agent session can continue after human comments. Captain is a *system identity* with its own model-backed session and tools: it reads global task/agent/review status, assigns work to group agents and can intervene on tasks. The supervisor deterministically detects failures, stale work and old Inbox messages, then issues review observations to Captain, which performs any discretionary follow-up.

Captain may propose a new agent, group or routine, but user confirmation is required and the proposal is rechecked before execution; similarly, global/Captain prompt changes must pass the user-operation gate. The ordinary operations JSONL log is not an independent complementary auditor.

Primary first-party paths: [runner.ts](https://github.com/0xfe-project/eta/blob/6b62da886b225391a157c7486e93b85aef73a17c/packages/eta-core/src/kernel/runner.ts), [graph.ts](https://github.com/0xfe-project/eta/blob/6b62da886b225391a157c7486e93b85aef73a17c/apps/eta/src/tasks/graph.ts), [runner.ts](https://github.com/0xfe-project/eta/blob/6b62da886b225391a157c7486e93b85aef73a17c/apps/eta/src/tasks/runner.ts), [service.ts](https://github.com/0xfe-project/eta/blob/6b62da886b225391a157c7486e93b85aef73a17c/apps/eta/src/captain/service.ts), [tools.ts](https://github.com/0xfe-project/eta/blob/6b62da886b225391a157c7486e93b85aef73a17c/apps/eta/src/captain/tools.ts), [supervisor.ts](https://github.com/0xfe-project/eta/blob/6b62da886b225391a157c7486e93b85aef73a17c/apps/eta/src/captain/supervisor.ts), [proposals.ts](https://github.com/0xfe-project/eta/blob/6b62da886b225391a157c7486e93b85aef73a17c/apps/eta/src/captain/proposals.ts), [base.ts](https://github.com/0xfe-project/eta/blob/6b62da886b225391a157c7486e93b85aef73a17c/packages/eta-harness/src/prompts/base.ts).

## S1 — Operations
- State: A
- Function: Configurable model-backed agents solve owner-assigned tasks with selected tools and feedback into subsequent model turns.
- Disturbance / variety regulated: Requests and tool results vary during a durable conversation/task execution.
- Decisive decision or feedback right: The runtime agent chooses responses and tool calls, and may submit finish_task or request clarification.
- Decision owner: Model-backed task-executing agent(s), including Captain in its own operational sessions.
- Supporting / enforcement mechanisms: Kernel Runner, typed tool middleware, RunPump wakeups, per-task sessions, task execution journal and restart controls.
- Closure path: A provider tool call is executed, its result is fed into the next model turn; the agent completes or blocks tasks and resulting card/activity updates wake consumers.
- Boundary reachability: The standard host runs bundled eta-core Runner and eta-harness RunPump, and exposes task agents via shipped TaskRunner and Board tools.
- Why this is / is not agent-owned: This is actual model-conditioned task execution, not only a UI dispatcher or static script.
- Evidence: [runner.ts](https://github.com/0xfe-project/eta/blob/6b62da886b225391a157c7486e93b85aef73a17c/packages/eta-core/src/kernel/runner.ts), [pump.ts](https://github.com/0xfe-project/eta/blob/6b62da886b225391a157c7486e93b85aef73a17c/packages/eta-harness/src/pump.ts), [runner.ts](https://github.com/0xfe-project/eta/blob/6b62da886b225391a157c7486e93b85aef73a17c/apps/eta/src/tasks/runner.ts)
- Basis: explicit first-party source, tests
- Confidence: high
- Caveats: External model accounts are user-configured; no actual provider call was run in this assessment.

## S2 — Coordination
- State: C
- Function: Attenuate concrete dependency and workspace-interference among distinct task-executing agent S1 units.
- Disturbance / variety regulated: A dependent agent can start from an unfinished/inconsistent predecessor's worktree, or a cancelled predecessor can leave unsatisfiable dependent work; cyclic task dependencies can deadlock execution.
- Decisive decision or feedback right: Decide whether a dependent run may enter the machine queue and what Git base to use; reject impossible dependency edges and propagate breakage.
- Decision owner: First-party deterministic TaskGraph/TaskBoard and task-runner pump; the collaborating agents and owner supply their dependency/task graph, not this policy's runtime judgment.
- Supporting / enforcement mechanisms: TaskGraph gate/deriveBase/checkEdge/derive, TaskRunner waitsForDeps/pump, Board dependency mutation and UI notifications.
- Closure path: A waiting dependent agent consumes no slot; completion releases it with the derived predecessor branch/HEAD; cancellation marks it blocked or withdraws the run until user fixes the edge.
- Boundary reachability: Shipped TaskRunner queries Board/TaskGraph before admitting *distinct* agent task runs, and first-party task-graph tests exercise dependency waiting, cancellations and derived base rather than describing hypothetical configuration.
- Why this is / is not agent-owned: The credited operational disturbance is conflicting dependent work over shared git/workspace state and broken upstream commitments, not mere group messaging or task ordering.
- Evidence: [graph.ts](https://github.com/0xfe-project/eta/blob/6b62da886b225391a157c7486e93b85aef73a17c/apps/eta/src/tasks/graph.ts), [runner.ts](https://github.com/0xfe-project/eta/blob/6b62da886b225391a157c7486e93b85aef73a17c/apps/eta/src/tasks/runner.ts), [task-graph.test.ts](https://github.com/0xfe-project/eta/blob/6b62da886b225391a157c7486e93b85aef73a17c/apps/eta/test/task-graph.test.ts)
- Basis: first-party source and native test cases
- Confidence: medium
- Caveats: Requires explicitly declared dependencies and standard project worktree task mode; this is not general semantic negotiation between unrelated agents.
- Distinct S1 units: Two independently model-backed task-agent executors handling predecessor Task A and dependent Task B in one shared project.
- Inter-S1 disturbance: B's workspace/run can refer to A's uncommitted or cancelled work; cycles can block both agents and a wrong base can erase predecessor progress.
- Attenuating coordination relation: Dependency graph refuses cycles, withholds dependent first runs, resolves only eligible predecessor statuses and derives inherited worktree base; broken dependencies block user intervention.
- Feedback into subsequent S1 behaviour: The queue skips B until A resolves, picks a source branch/HEAD when B begins and marks B blocked if A is cancelled, changing what subsequent agent turns execute.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: There is a structurally evidenced cross-agent working-tree/dependency interference and a concrete fail-closed gate/base reconciliation path that prevents wrong concurrent action.

## S3 — Inside-and-now control
- State: A
- Function: Captain observes active agents, task failures, blocked work and queues and can choose current-work interventions.
- Disturbance / variety regulated: The owner's active agent team can stall, fail, miss deadlines, leave unanswered Inbox questions or require priority/assignment correction.
- Decisive decision or feedback right: Captain decides how to instruct existing member agents, continue or stop active tasks and relay unresolved questions; the automatic supervisor only detects and presents disturbances.
- Decision owner: Model-backed Captain system agent with bundled S3-facing tools; user controls activation/settings but does not make each Captain supervisory choice.
- Supporting / enforcement mechanisms: Supervisor tick/observeReviews, task/inbox state, Captain list_agents/list_tasks/assign_in_group/control_task and persistent review inbox.
- Closure path: Supervisor-created review is delivered to Captain as a session turn; Captain can inspect the live state and send an operational reassignment or control action, and task state/agent work changes as the result.
- Boundary reachability: Captain is an actual protected system agent with first-party model sessions and action tools. First-party tests cover failure/stuck-task review delivery, agent authorization and task continuation.
- Why this is / is not agent-owned: Deterministic failure detection, retry limits and scheduling enforce constraints but do not substitute for Captain's agent decision on what intervention to make; no autonomous managerial behavior is inferred from 'Captain' label alone.
- Evidence: [service.ts](https://github.com/0xfe-project/eta/blob/6b62da886b225391a157c7486e93b85aef73a17c/apps/eta/src/captain/service.ts), [supervisor.ts](https://github.com/0xfe-project/eta/blob/6b62da886b225391a157c7486e93b85aef73a17c/apps/eta/src/captain/supervisor.ts), [tools.ts](https://github.com/0xfe-project/eta/blob/6b62da886b225391a157c7486e93b85aef73a17c/apps/eta/src/captain/tools.ts), [captain.test.ts](https://github.com/0xfe-project/eta/blob/6b62da886b225391a157c7486e93b85aef73a17c/apps/eta/test/captain.test.ts)
- Basis: explicit source and first-party test scenarios
- Confidence: medium-high
- Caveats: Requires Captain model configured and supervisor enabled. Owner may intervene via UI, but distinct first-party parent S3 mode has not been reconstructed sufficiently to claim A(P).
- Whole-system current view: Captain reads agent roster/status, assignments, task board and Inbox across a shared workbench; supervisor consolidates failures, stale runs and reviews.
- Current-control decision scope: Model-backed Captain may assign and reassign active team commitments, control tasks and escalate a stuck Inbox item for a human answer, with resulting task-run updates.

## S3* — Complementary audit
- State: —
- Function: No independent complementary audit authority with a separate operational access path and corrective closure was found in the supported workbench.
- Disturbance / variety regulated: Normal session logs and a supervisor's own status reports could hide incorrect agent or Captain claims.
- Decisive decision or feedback right: An independent actor would need to inspect separate evidence and return a corrective challenge to S3.
- Decision owner: No separate first-party complementary auditor identified; ordinary agent, Captain and unit tests are not independence witnesses.
- Supporting / enforcement mechanisms: CaptainAudit append-only operations JSONL, timeline, ordinary supervisor checks and tests.
- Closure path: Logs/review inbox reflect the same active system reports; no independent evidence acquisition, challenge judgment or separate audit findings loop was located.
- Why this is / is not agent-owned: A trace of normal team events, self-review and developer testing are not independently controlled audit access.
- Evidence: [audit.ts](https://github.com/0xfe-project/eta/blob/6b62da886b225391a157c7486e93b85aef73a17c/apps/eta/src/captain/audit.ts), [supervisor.ts](https://github.com/0xfe-project/eta/blob/6b62da886b225391a157c7486e93b85aef73a17c/apps/eta/src/captain/supervisor.ts), [captain.test.ts](https://github.com/0xfe-project/eta/blob/6b62da886b225391a157c7486e93b85aef73a17c/apps/eta/test/captain.test.ts)
- Basis: bounded negative assessment of available first-party surfaces
- Confidence: medium
- Caveats: A user could audit the SQLite store manually, but that possibility is not a shipped independent audit feedback loop.
### Absence scope
- Surfaces inspected: Captain operations audit JSONL, supervisor, review observer, direct/team timelines, host session journals, task-graph tests and external/runtime architecture.
- Plausible first-party paths checked: Separate auditor role or adapter, complementary probe with independent evidence, operational finding to Captain action/recovery path.
- Why no material first-party path remains: Reviewed paths produce ordinary self-observation and logging, not independent complementary checking of operational truth and a returned corrective decision.

## S4 — Outside-and-then intelligence
- State: ?
- Function: Future-capability adaptation plausibly exists through Captain proposals for new agents, groups, routines and revisions, but its full external/prospective evidence chain remains unresolved.
- Disturbance / variety regulated: Novel external work or changed model/tool conditions may require different future roles, capabilities or ongoing schedules.
- Decisive decision or feedback right: A prospective option would have to be chosen against future environmental needs, approved and made available to subsequent work.
- Decision owner: Captain can suggest new agents/groups/routines and the owner confirms; whether Captain's shipped model path *actually* closes external-and-then intelligence is not independently established.
- Supporting / enforcement mechanisms: Captain proposals registry, provider/models listing, user-confirmation callback, initial agent/persona construction and routine brief editing.
- Closure path: The approval callback validates and applies new capacity and notifies Captain; missing is proof that a distinct future/environment analysis produced the adaptation option rather than a straightforward user command.
- Why this is / is not agent-owned: Do not promote generic agent spawning, routine editing or making requested work into S4 without evidence of an externally informed prospective option loop.
- Evidence: [proposals.ts](https://github.com/0xfe-project/eta/blob/6b62da886b225391a157c7486e93b85aef73a17c/apps/eta/src/captain/proposals.ts), [propose-agent.ts](https://github.com/0xfe-project/eta/blob/6b62da886b225391a157c7486e93b85aef73a17c/apps/eta/src/captain/propose-agent.ts), [runner.ts](https://github.com/0xfe-project/eta/blob/6b62da886b225391a157c7486e93b85aef73a17c/apps/eta/src/routines/runner.ts), [service.ts](https://github.com/0xfe-project/eta/blob/6b62da886b225391a157c7486e93b85aef73a17c/apps/eta/src/captain/service.ts)
- Basis: first-party prospective path exists but specific causality uncertain
- Confidence: medium-low
- Caveats: Targeted re-review should trace a production Captain decision from changed external evidence to an accepted adaptation option and then to changed capability. Abstract future extension is not the uncertainty: these concrete production proposals are.

## S5 — Policy and identity
- State: P
- Function: Retain the workbench's ultimate agent identity/base instruction policy under the owner, returning approved changes to subsequent sessions.
- Disturbance / variety regulated: Agent-originated changes to the global behavioral base or the privileged Captain identity can redefine the workbench's operating mandate.
- Decisive decision or feedback right: Approve or reject a change to base instruction policy and Captain's protected prompt/identity; prohibit unapproved mutation.
- Decision owner: Legitimate human operator via Captain's first-party pending-operation/decideOperation flow, not Captain's own judgment.
- Supporting / enforcement mechanisms: Base prompt version history, protected `set_prompt` operation, `setPrompt` guard, proposal state machine, prompt getter/host session composition and approval tests.
- Closure path: A requested base/Captain prompt mutation records a pending operation; user approval revalidates and applies versioned content, which is loaded for subsequent model sessions, while rejection leaves policy unchanged.
- Boundary reachability: Captain tools for privileged prompts create approval-required operations and the shipped Captain plugin exposes decideOperation; service guards privileged prompt edits, and tests assert protected prompt versions.
- Why this is / is not agent-owned: This is parent-only ultimate identity/behavioral charter custody, not S5 credit from an ordinary per-tool approval. No autonomous S5 decision mode is established.
- Evidence: [base.ts](https://github.com/0xfe-project/eta/blob/6b62da886b225391a157c7486e93b85aef73a17c/packages/eta-harness/src/prompts/base.ts), [service.ts](https://github.com/0xfe-project/eta/blob/6b62da886b225391a157c7486e93b85aef73a17c/apps/eta/src/captain/service.ts), [tools.ts](https://github.com/0xfe-project/eta/blob/6b62da886b225391a157c7486e93b85aef73a17c/apps/eta/src/captain/tools.ts), [captain.test.ts](https://github.com/0xfe-project/eta/blob/6b62da886b225391a157c7486e93b85aef73a17c/apps/eta/test/captain.test.ts)
- Basis: first-party protected authority and return path
- Confidence: medium
- Caveats: Policy scope is the default agent behavioral charter and Captain's privileged system instructions; ordinary user changes to task status are S3/S1, not S5.
- Identity / ultimate-policy issue: Altering the global base system prompt that all agents inherit, or protected Captain system instructions, changes who this workbench directs agents to be and their overarching behavioral mandate.
- Ultimate authority in each claimed mode: Human workbench owner approves or rejects the first-party pending Captain operation; no independently justified agent-owned S5 mode is claimed.
- Return-to-operation path: An accepted version is stored and served through basePrompt()/session composition to later agents; refusal preserves prior policy and reports the outcome to Captain.

## Recursion

Distinct task agents operate within projects; Captain supervises the selected group/workbench from one higher current-control recursion. A group of agents, a session tree and the runtime's processes are not independently assumed viable organizations.

## Variety and escalation

User-directed tasks create S1 variety; model/tool effects feed subsequent turns. Project dependency gating and derived worktree bases prevent specific inter-agent work interference. Captain receives supervisor reviews about shared-current failures and can act. An agent-originated structural adaptation request is currently classed as uncertain S4, while protected ultimate prompt policy returns through explicit owner approval. External tool/runtime capabilities are not considered bundled discretionary owners.

## Evidence gaps

- Source-first semantic assessment only. No independent second reviewer, actual Bun tests, external model calls or remote daemon test run was performed in this attempt.
- S2=C is bounded to explicitly dependent agent tasks sharing workspace ancestry, not arbitrary disagreement resolution. S3=A is the Captain-enabled mode, not generic deterministic task scheduling.
- S4=? is a specific unresolved shipped path (Captain proposal machinery versus external future intelligence), not a guess from an empty README or hypothetical plugin.
- S5=P is bounded to the protected global charter and Captain identity, not a claim of autonomous policy authorship or user-approval-as-universal-S5.

---
harness_id: termagent
project_name: TermAgent
repository: https://github.com/whoops-1/termagent
review_ref: 33aa966551fcc2c050c0a213642d9966c3dd4a21
reviewed_at: 2026-09-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-30
status: proposed
autonomy_s1: A
autonomy_s2: A(P)
autonomy_s3: A(P)
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# TermAgent

## Review boundary

- System in focus: TermAgent's first-party Node/TypeScript coding-agent runtime at frozen revision `33aa966551fcc2c050c0a213642d9966c3dd4a21`, including the main model/tool loop, tool registry/executor, execution workflow controller, permission gate, durable task manager/workers, parallel/background agents, sessions/context and supported CLI/headless/API surfaces.
- Purpose and identity: perform repository-facing software-engineering work while supporting bounded autonomous execution, durable background work and explicitly scoped concurrent coding workers on a lightweight Node-only runtime.
- Relevant environment: user tasks, project/worktree state, tool/shell/Git evidence, provider responses, durable task records/events, declared worker scopes, project instructions/skills/plugins/MCP tools and operator permission decisions.
- Standard-distribution boundary: TermAgent's own runtime, task scheduler/worker entrypoint, built-in tools, workflow controller, permissions, sessions/context, repository map and first-party API/CLI composition are inside. External model providers and MCP servers remain dependencies. User-authored plugins/skills/instructions configure the runtime but do not donate unshipped organizational functions.
- Credited operating / distribution surfaces: `README.md`; `src/agent/agent.ts`; `src/agent/workflow.ts`; `src/tools/parallel.ts`; `src/tools/background.ts`; `src/tasks/manager.ts`; `src/tools/permissions.ts`; standard CLI/server runtime composition and documented Phase 3 execution behavior.
- Adjacent first-party surfaces excluded from ownership: tests, release/development documentation as authority by itself, contributor governance, external provider behavior and application-authored plugins/MCP servers. Documentation is used where it matches the frozen implementation.
- First-party operating / deployment modes considered: ordinary build/plan/explore sessions; `/auto`; approval modes `ask`, `auto`, `deny`; `background_agent`; `parallel_agents`; `task_status`; `task_cancel`; interactive/headless/API surfaces using the same runtime.
- Recursion level: the assessed organization is one primary TermAgent session plus first-party durable child Agent workers it can create, observe and cancel. Background/parallel child agents run independent model/tool runtimes and therefore qualify as subordinate S1 units at this recursion; no stronger full-recursive viability claim is made.
- Reviewed revision: `33aa966551fcc2c050c0a213642d9966c3dd4a21`.
- Observation date: 2026-09-30.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

`src/agent/agent.ts` owns the primary provider/tool feedback loop. It builds the model-visible tool schemas from the active profile and workflow phase, streams a provider response, executes selected tools through the first-party registry, appends results to the persistent session and continues until the model finishes or a bounded controller stops the run. In autonomous mode an `ExecutionWorkflow` persists the planning → building → verifying → iterating/complete state and mechanically prevents completion before `verify_project` succeeds.

Durable background work is a separate first-party execution plane. `background_agent` creates a persistent agent task and spawns a detached worker. `parallel_agents` creates two to four independent background coding agents concurrently. Every parallel task must declare one or more in-project workspace paths. The scheduler rejects scopes that overlap each other or overlap an already active scoped worker, rejects capacity above four active agents for the session, and repeats admission checks under a cross-process session lock before launching workers. Scoped workers are prevented from recursively creating more workers and are constrained to their declared write paths.

The primary model receives durable task IDs when it launches work. Model-facing `task_status` returns current task status/output and `task_cancel` can terminate queued/running work. `TaskManager` stores status, PID, output, session identity and scope paths, maintains cross-process locks/event records, recovers stale workers and sends process termination on cancellation. This gives the primary actor both a bounded concurrent S1 population and concrete current-control rights over that population.

The same S2/S3 decisions have two supported ownership configurations. `PermissionGate` allows all tool actions automatically when `approvals='auto'`; the default `ask` mode pauses non-read tools for Allow once / Always allow / Reject. Because `parallel_agents`, `background_agent` and `task_cancel` are shell-risk tools, the primary model owns their decisive action in `auto`, while the operator is decisive for the same organizational commitment action in `ask`.

The autonomous workflow's verification phase is not credited as S3*. `verify_project` is a required production completion gate inside the same first-party execution controller. It supplies ordinary QA/feedback to the main coding loop, not a materially independent complementary auditor with a separate claim-access path.

Primary evidence:

- [`README.md`](https://github.com/whoops-1/termagent/blob/33aa966551fcc2c050c0a213642d9966c3dd4a21/README.md)
- [`src/agent/agent.ts`](https://github.com/whoops-1/termagent/blob/33aa966551fcc2c050c0a213642d9966c3dd4a21/src/agent/agent.ts)
- [`src/agent/workflow.ts`](https://github.com/whoops-1/termagent/blob/33aa966551fcc2c050c0a213642d9966c3dd4a21/src/agent/workflow.ts)
- [`src/tools/parallel.ts`](https://github.com/whoops-1/termagent/blob/33aa966551fcc2c050c0a213642d9966c3dd4a21/src/tools/parallel.ts)
- [`src/tools/background.ts`](https://github.com/whoops-1/termagent/blob/33aa966551fcc2c050c0a213642d9966c3dd4a21/src/tools/background.ts)
- [`src/tasks/manager.ts`](https://github.com/whoops-1/termagent/blob/33aa966551fcc2c050c0a213642d9966c3dd4a21/src/tasks/manager.ts)
- [`src/tools/permissions.ts`](https://github.com/whoops-1/termagent/blob/33aa966551fcc2c050c0a213642d9966c3dd4a21/src/tools/permissions.ts)
- [`docs/PHASE3_EXECUTION.md`](https://github.com/whoops-1/termagent/blob/33aa966551fcc2c050c0a213642d9966c3dd4a21/docs/PHASE3_EXECUTION.md)

## Operational model

A primary TermAgent actor can perform normal coding actions or create independently running subordinate Agent commitments. `parallel_agents` is explicitly designed for concurrent coding work and requires the primary actor to provide a prompt and non-overlapping workspace scope for every child. The scheduler enforces the declared partition and checks it against the already-active task set. Child task IDs/status/output then remain available while the foreground actor continues, and the foreground actor can cancel commitments that should stop.

This separates three functions cleanly: S1 is the child or foreground coding loop; S2 attenuates interference among simultaneous child S1s by enforcing disjoint writable scopes and bounded concurrency; S3 decides which current commitments to create, observes their state/output and can terminate them. The execution workflow's plan/verify state machine remains production control inside those operational loops rather than an extra VSM level by name.

## S1 — Operations

- State: A
- Function: perform coding work by interpreting the current objective, selecting permitted repository/tool actions, executing them and revising subsequent actions from returned evidence.
- Disturbance / variety regulated: source/worktree state, implementation alternatives, provider uncertainty, tool/build/test failures, context pressure, no-progress/repeated actions and changing task evidence.
- Decisive decision or feedback right: choose the next task-specific tool/action and revise it from tool/provider/workspace feedback.
- Decision owner: the model-backed TermAgent actor in each foreground or background Agent runtime.
- Supporting / enforcement mechanisms: tool registry; provider abstraction/routing; sessions; context budgeting/compaction; permissions; profiles; execution workflow; retry/no-progress guards; repository map; skills/plugins/MCP.
- Closure path: task/current context → model decision → first-party tool execution → result persisted/returned → same actor selects another action or final response.
- Boundary reachability: the shipped CLI, headless/server surfaces and detached workers instantiate the same first-party Agent/tool runtime.
- Why this is / is not agent-owned: removing the model actor leaves workflow/permission/session machinery but removes the open-ended choice of what repository action to perform next; deterministic mechanisms constrain and transport rather than replace the coding decision.
- Evidence: [`src/agent/agent.ts`](https://github.com/whoops-1/termagent/blob/33aa966551fcc2c050c0a213642d9966c3dd4a21/src/agent/agent.ts); [`README.md`](https://github.com/whoops-1/termagent/blob/33aa966551fcc2c050c0a213642d9966c3dd4a21/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: particular non-read actions can be parent-gated in `ask`, but TermAgent also ships `auto` as a first-party autonomous permission mode.

## S2 — Coordination

- State: A(P)
- Function: attenuate destructive interference among multiple simultaneously active subordinate coding S1s sharing one project by bounding concurrency and enforcing non-overlapping writable workspace scopes.
- Disturbance / variety regulated: concurrent background coding agents could edit the same or nested paths, overwrite one another, create non-reviewable shared-state races or exceed the bounded worker capacity for one session.
- Distinct S1 units: each `parallel_agents` task becomes a separately persisted `agent` task with its own detached worker process, provider configuration, prompt, status/output and declared `scopePaths`.
- Inter-S1 disturbance: simultaneous agents share the project filesystem; overlapping file/directory scopes create a concrete mutation conflict risk. The design documentation explicitly names concurrent agents editing the same files as the conflict being prevented.
- Attenuating coordination relation: the primary actor chooses 2–4 tasks and declares paths for each; `parallel_agents` normalizes those paths, rejects out-of-project scopes, rejects pairwise overlaps, checks overlaps with already active agent scopes, enforces a maximum of four active workers and repeats the admission check under a cross-process session lock. Scoped workers are prevented from writing outside their declared region.
- Feedback into subsequent S1 behaviour: accepted scopes constrain child write behavior; rejected overlap/capacity calls return errors to the primary model, which can redesign task decomposition/scopes or run work sequentially. Active scoped commitments are persisted and considered by later admissions.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the mechanism is expressly conditional on a concrete inter-S1 interference class—overlapping concurrent workspace mutation—and alters admission/write behavior specifically to attenuate it. Mere multiplicity or task routing is not the basis of the positive state.
- Decisive decision or feedback right: select which child S1 tasks may be launched together and assign their non-overlapping workspace ownership scopes; after scheduler feedback, revise those task/scope choices.
- Decision owner: primary model-backed TermAgent actor in `approvals='auto'`; interactive operator is decisive in `ask` for authorization of the shell-risk launch.
- Supporting / enforcement mechanisms: `parallel_agents`; scope normalization/overlap checks; `activeAgentTasks`; per-session capacity; cross-process session lock; scoped worker write checks; durable task records.
- Closure path: primary actor decomposes work and proposes tasks/scopes → scheduler compares requested/current active scopes → launch is admitted or rejected → accepted children operate inside constrained scopes / rejection returns conflict evidence → subsequent primary decomposition can change.
- Boundary reachability: `parallel_agents` is registered in the standard CLI/server runtime together with first-party worker/task machinery; no application-authored coordinator is required.
- Why this is / is not agent-owned: deterministic code enforces safety once task/scopes are proposed, but without the primary model there is no task-specific choice of which independent coding commitments to create together or how to partition their work. In `ask`, the operator additionally owns launch authorization.
- Evidence: [`src/tools/parallel.ts`](https://github.com/whoops-1/termagent/blob/33aa966551fcc2c050c0a213642d9966c3dd4a21/src/tools/parallel.ts); [`src/tasks/manager.ts`](https://github.com/whoops-1/termagent/blob/33aa966551fcc2c050c0a213642d9966c3dd4a21/src/tasks/manager.ts); [`docs/PHASE3_EXECUTION.md`](https://github.com/whoops-1/termagent/blob/33aa966551fcc2c050c0a213642d9966c3dd4a21/docs/PHASE3_EXECUTION.md); [`src/tools/permissions.ts`](https://github.com/whoops-1/termagent/blob/33aa966551fcc2c050c0a213642d9966c3dd4a21/src/tools/permissions.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: S2 is deliberately bounded to declared workspace-scope interference; it does not imply generic semantic coordination among agents whose declared scopes are disjoint.

### S2 mode matrix

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Primary model-backed TermAgent actor | Model calls `parallel_agents` with 2–4 task/scope assignments under `approvals='auto'` | Runtime immediately checks active scopes/capacity, admits only non-overlapping commitments and returns launch/conflict feedback | `parallel.ts`; `manager.ts`; `permissions.ts` |
| Parent (`P`) | Interactive operator | Model proposes the same shell-risk orchestration under `approvals='ask'` | Operator allows once/always or rejects; only an approved launch reaches the scheduler and children | `permissions.ts`; `parallel.ts` |

The parent mode is credited because the approved action is itself the creation of the coordinated multi-S1 configuration, not an incidental file edit inside one S1.

## S3 — Inside-and-now control

- State: A(P)
- Function: regulate the current population of durable subordinate coding commitments by deciding what background work to start, observing its current status/output and terminating commitments that should no longer continue.
- Disturbance / variety regulated: changing current workload decomposition, independently progressing subordinate tasks, failed/stuck/unneeded workers, bounded concurrent capacity and the need to stop or redirect current commitments while foreground work continues.
- Whole-system current view: each launch returns the durable IDs of the subordinate commitments that form the current bounded worker population; `task_status` exposes a selected task's durable `status`, PID, output, session identity, provider and scope state, while launch admission itself queries the complete active-agent set for the session before admitting more work. The foreground actor can therefore inspect the status/output of every commitment it created and receives scheduler feedback against the current active population.
- Current-control decision scope: the primary actor can create independent durable coding commitments through `background_agent` or a bounded set through `parallel_agents`, choose their prompts/scopes, and terminate queued/running commitments through model-facing `task_cancel`; these actions change the current subordinate workload population rather than merely the content of one S1 turn.
- Decisive decision or feedback right: decide which new coding commitments should exist now, what scoped work they own, observe their current results/status, and cancel commitments after that feedback.
- Decision owner: primary model-backed TermAgent actor in `approvals='auto'`; interactive operator becomes decisive for shell-risk start/cancel authorization in `approvals='ask'`.
- Supporting / enforcement mechanisms: `background_agent`; `parallel_agents`; `task_status`; `task_cancel`; `TaskManager` durable records/events; worker PID lifecycle/recovery; active-agent population query; capacity/session locks; permission gate.
- Closure path: current task IDs/status/output and admission feedback → primary model decides start/parallel/cancel action → permission path → task manager spawns or signals worker → durable task state changes → subsequent `task_status`/scheduler/model turns observe that changed current population.
- Boundary reachability: all lifecycle tools and worker/task machinery are first-party standard runtime components registered on supported CLI/server surfaces; the child workers reconstruct TermAgent's own provider/runtime state.
- Why this is / is not agent-owned: in `auto`, removing the primary model leaves lifecycle machinery and fixed limits but no task-specific judgment about which commitment to create/cancel or how to decompose current work. In `ask`, the parent operator owns final authorization for the same commitment action.
- Evidence: [`src/tools/background.ts`](https://github.com/whoops-1/termagent/blob/33aa966551fcc2c050c0a213642d9966c3dd4a21/src/tools/background.ts); [`src/tools/parallel.ts`](https://github.com/whoops-1/termagent/blob/33aa966551fcc2c050c0a213642d9966c3dd4a21/src/tools/parallel.ts); [`src/tasks/manager.ts`](https://github.com/whoops-1/termagent/blob/33aa966551fcc2c050c0a213642d9966c3dd4a21/src/tasks/manager.ts); [`src/tools/permissions.ts`](https://github.com/whoops-1/termagent/blob/33aa966551fcc2c050c0a213642d9966c3dd4a21/src/tools/permissions.ts); [`README.md`](https://github.com/whoops-1/termagent/blob/33aa966551fcc2c050c0a213642d9966c3dd4a21/README.md).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: there is no model-facing one-call `task_list`; the positive current view is bounded to the commitment IDs returned to the parent plus per-task `task_status` and scheduler feedback over the complete active session set. This is sufficient for the small S3 claim but should not be read as a rich organization-wide dashboard.

### S3 mode matrix

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Primary model-backed TermAgent actor | Model selects `background_agent`, `parallel_agents` or `task_cancel` under `approvals='auto'` | Runtime directly creates/cancels subordinate S1 commitments; task records/status/output feed later model decisions | `background.ts`; `parallel.ts`; `manager.ts`; `permissions.ts` |
| Parent (`P`) | Interactive operator | Model proposes the same shell-risk current-control action under `approvals='ask'` | Operator allows once/always or rejects; only approved commitment changes execute and return into the model loop | `permissions.ts`; lifecycle tools |

The parent mode is credited because approval controls whether a subordinate operational commitment is created or terminated, which is itself an S3 current-control decision.

## S3* — Complementary audit

- State: —
- Function: no material boundary-reachable complementary audit role with sufficiently independent access, audit judgment and corrective return was established.
- Disturbance / variety regulated: ordinary implementation defects and failed verification are regulated inside the production workflow, but no separate S3*-specific audit disturbance/claim channel was established.
- Decisive decision or feedback right: not established for a complementary auditor.
- Decision owner: not established.
- Supporting / enforcement mechanisms: deterministic `verify_project`; separate verification provider routing; workflow verification phase; tests/build commands; task status and ordinary repository inspection.
- Closure path: absent at S3* level. The enforced planning/building/verifying/iterating controller routes ordinary production evidence back to the same coding workflow; no materially independent claim-access path and audit actor is required for that closure.
- Why this is / is not agent-owned: a role-specific provider does not by itself create an independent auditor, and deterministic verification results are ordinary operational QA. No separate actor was found whose audit judgment challenges the production actor through complementary evidence and then returns to corrective control.
- Evidence: [`src/agent/workflow.ts`](https://github.com/whoops-1/termagent/blob/33aa966551fcc2c050c0a213642d9966c3dd4a21/src/agent/workflow.ts); [`src/agent/agent.ts`](https://github.com/whoops-1/termagent/blob/33aa966551fcc2c050c0a213642d9966c3dd4a21/src/agent/agent.ts); [`docs/PHASE3_EXECUTION.md`](https://github.com/whoops-1/termagent/blob/33aa966551fcc2c050c0a213642d9966c3dd4a21/docs/PHASE3_EXECUTION.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: an application could potentially create an audit-specific background agent with custom instructions, but uninstantiated composition is not credited as first-party closed S3*.

### Absence scope

- Surfaces inspected: enforced autonomous workflow; `verify_project`; role-specific provider routing; child/background agent tools; task status/events; repository inspection tools; plugin/custom-agent extensibility.
- Plausible first-party paths checked: separate reviewer/verifier agent; adversarial audit role; independent evidence channel; post-implementation review worker; verification-provider separation; deterministic test/build gates as possible S3*.
- Why no material first-party path remains: shipped completion verification is mandatory production QA inside the same execution state machine, while background/custom-agent primitives do not instantiate a default complementary audit role with independent challenge and corrective-return semantics.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party external-and-prospective adaptation loop over TermAgent's own present organizational capability was established.
- Disturbance / variety regulated: repository-map retrieval, external/provider switching, skills/plugins/MCP, sessions and role-specific routing can improve current execution but do not close an outside-and-then capability-adaptation function.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: provider/router profiles; fallback providers; repository map; skills/plugins; MCP; project instructions; session/context compaction.
- Closure path: no environmental/future distinction → adaptation-option generation/evaluation → adopted change to present organizational capability/S3 loop was established.
- Why this is / is not agent-owned: current provider routing and retrieval choose among preconfigured capabilities for the task; they do not let a first-party S4 actor prospectively redesign/adopt organizational capabilities from external/future evidence.
- Evidence: [`README.md`](https://github.com/whoops-1/termagent/blob/33aa966551fcc2c050c0a213642d9966c3dd4a21/README.md); [`src/agent/agent.ts`](https://github.com/whoops-1/termagent/blob/33aa966551fcc2c050c0a213642d9966c3dd4a21/src/agent/agent.ts); [`docs/PHASE3_EXECUTION.md`](https://github.com/whoops-1/termagent/blob/33aa966551fcc2c050c0a213642d9966c3dd4a21/docs/PHASE3_EXECUTION.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: developer/operator addition of providers/plugins/skills changes future capability but is adjacent configuration work unless the running organization itself closes that prospective adaptation decision.

### Absence scope

- Surfaces inspected: provider routing/fallback; repository intelligence; skills/plugins/MCP; sessions/context compaction; background workers; execution workflow; project instructions and API surfaces.
- Plausible first-party paths checked: environmental monitoring, future-scenario modeling, capability scouting, autonomous provider/tool/plugin adoption, prospective strategy generation and return of an adaptation proposal into current control.
- Why no material first-party path remains: inspected mechanisms use preconfigured capabilities to execute current work; no first-party future-facing intelligence actor develops and adopts organizational adaptations.

## S5 — Policy and identity

- State: —
- Function: no material first-party runtime identity/ultimate-policy closure was established at the assessed recursion.
- Disturbance / variety regulated: approval modes, profiles, tool risks, scoped-worker restrictions, project instructions and configuration constrain current operation but do not constitute an ultimate-policy/identity decision loop.
- Decisive decision or feedback right: not established for S5-level identity or ultimate policy.
- Decision owner: not established at S5; developer/operator configuration sets the operative envelope outside a qualifying runtime identity closure.
- Supporting / enforcement mechanisms: `PermissionGate`; approval config; build/plan/explore profiles; workflow phase rules; scoped worker prohibitions; project instructions; provider/plugin/MCP configuration.
- Closure path: absent at S5 level; no identity/ultimate-policy issue → legitimate ultimate authority → authoritative decision → returned policy governing subsequent operation was found.
- Why this is / is not agent-owned: models act within configured policy but do not own the legitimate right to redefine TermAgent's identity or ultimate rules. Operator approval of a launch/tool call is ordinary parent governance at that function, not S5.
- Evidence: [`src/tools/permissions.ts`](https://github.com/whoops-1/termagent/blob/33aa966551fcc2c050c0a213642d9966c3dd4a21/src/tools/permissions.ts); [`src/config/config.ts`](https://github.com/whoops-1/termagent/blob/33aa966551fcc2c050c0a213642d9966c3dd4a21/src/config/config.ts); [`README.md`](https://github.com/whoops-1/termagent/blob/33aa966551fcc2c050c0a213642d9966c3dd4a21/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: project/repository governance determines future releases but remains adjacent to the runtime boundary and is not imported as product S5.

### Absence scope

- Surfaces inspected: approval/configuration; workflow/profile constraints; scoped-worker restrictions; project instructions; provider/plugin/MCP configuration; API/server controls; repository governance adjacency.
- Plausible first-party paths checked: runtime constitutional revision, autonomous ultimate-policy adjudication, identity-level escalation, durable authoritative policy changes returned into running agents and project governance as a distributed parent authority.
- Why no material first-party path remains: first-party mechanisms enforce externally authored operational constraints. No runtime actor holds legitimate ultimate-policy/identity closure at the assessed recursion.

## Recursion

Background and parallel child agents are independent first-party Agent workers with their own provider/model execution, durable lifecycle and bounded workspace environment. They are therefore distinct S1 units and are the operative lower-level units for S2/S3 analysis. The review does not establish that every child also possesses the full metasystemic structure required for a stronger full-recursion claim.

## Variety and escalation

TermAgent attenuates operational variety through explicit workflow phases, bounded retries/verification, permission gates, task leases, worker limits, non-overlapping write scopes, scoped-worker prohibitions and cross-process locks. It amplifies capability through repository intelligence, provider routing, skills/plugins/MCP and durable parallel Agent workers.

Escalation from subordinate operation to current control is explicit: worker status/output is durably recorded, the primary actor can inspect it with `task_status`, scheduler admission reports conflicts/capacity against the active population, and the primary can change the commitment set with new launches or `task_cancel`. In `ask`, the operator governs those same commitment changes; in `auto`, the model closes them itself.

## Evidence gaps

- S3 current view is bounded to the child IDs returned by launches plus per-ID `task_status` and scheduler feedback; there is no model-facing one-call list of all tasks.
- The positive S2 claim is specifically workspace-scope collision attenuation, not evidence of semantic negotiation among children.
- No complementary audit actor is instantiated by default; `verify_project` remains routine production verification.
- No outside-and-then adaptation loop or runtime ultimate-policy closure was found for S4/S5.

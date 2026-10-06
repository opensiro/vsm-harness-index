---
harness_id: alphacode
project_name: AlphaCode
repository: https://github.com/dragonked2/alphacode
review_ref: a28db8978a5b336e244973c8db01f625dfcc0983
reviewed_at: 2026-10-06
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-06
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# AlphaCode

## Review boundary

- System in focus: the first-party AlphaCode coding runtime at frozen revision a28db8978a5b336e244973c8db01f625dfcc0983, including the main coding agent, first-party swarm worker sessions, task-graph and coordinator controls, deep-mode critique/verify gates, built-in coding/browser/desktop tools, sessions, permissions, memory, ambient scheduling and self-improvement surfaces.
- Purpose and identity: execute software-engineering and automation goals through a model-backed agent that can work directly or coordinate multiple first-party worker agents through a shared task graph and gated deep-swarm workflow.
- Relevant environment: user goals and steering, repository/workspace files, tool/test/browser/desktop results, worker status/heartbeats/artifacts, dependency graph state, model/provider responses, resource pressure, persisted sessions/memory and external MCP services.
- Standard-distribution boundary: the shipped AlphaCode Rust runtime and bundled first-party tools/prompts/swarm control. External model endpoints, MCP servers, browser/OS services and the user project are dependencies and cannot donate organizational functions.
- Credited operating / distribution surfaces: src/alphacode_app_core agent, server, tool, autonomous, ambient and memory modules; src/alphacode_swarm_core; first-party plan/protocol/task types; supported TUI/headless swarm execution.
- Adjacent first-party surfaces excluded from ownership: repository CI, benchmarks, docs/plans, development-only tests and maintainer/release workflows except where tests corroborate a shipped runtime path.
- First-party operating / deployment modes considered: ordinary coding sessions; first-party swarm with spawned inline/headless agents; light and deep task graphs; background or blocking run_plan; current task control/recovery; browser/desktop/MCP tools; memory, ambient scheduling and self-improvement tools.
- Recursion level: one AlphaCode coding organization. The coordinator/main coding agent and spawned swarm coding workers are operational S1 units when each owns a bounded software-engineering outcome. Deep critique/verify gate workers are complementary audit actors.
- Reviewed revision: a28db8978a5b336e244973c8db01f625dfcc0983.
- Observation date: 2026-10-06.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

AlphaCode ships a model/tool coding loop with a broad first-party tool surface and persistent session state. Its swarm tool is directly model-callable and exposes task_graph, spawn, assign_task, assign_next, run_plan, plan_status, read_context, retry, reassign, replace, salvage, expand_node, complete_node and inject_gap.

Swarm workers are first-party AlphaCode agent sessions. The coordinator can construct dependency graphs, spawn workers, assign work, inspect plan/member state and intervene in active assignments. Runtime code adds deterministic enforcement around double assignment, in-flight assignment claims, dependency readiness, staleness, heartbeats, worker liveness and recovery. The source explicitly records a real coordination defect that occurred when a node was silently re-assigned to a second active worker and both edited the same work, and the current control path rejects that double assignment or requires explicit takeover.

Deep mode adds an adversarial critique/verify gate after work nodes. Gate assignments are full worker assignments with a dedicated audit contract. The gate must inspect every audited artifact, probe gaps and either inject follow-up nodes or complete the gate with an artifact that accounts for every audited node. A passing artifact is mechanically rejected when required audited node identifiers or low-confidence debts are not addressed.

Memory, self-improvement and ambient scheduling are substantial first-party capabilities, but the reviewed source does not establish a separate external-and-prospective adaptation owner that converts future environmental distinctions into strategic options and returns those options into current S3 capability.

## Operational model

The main/coordinator model owns open-ended engineering and swarm-organization decisions. It can create the task graph, choose decomposition/dependencies, request fresh workers, assign or reassign work, examine current plan/worker state and decide how failed/stale/low-confidence work should proceed. Deterministic server code enforces the chosen topology and safe transitions.

Deep gate workers are separate model-backed AlphaCode worker sessions. Their organizational role is not ordinary production: they are instructed to challenge completed scope, mine unverified or low-confidence gaps, inspect/probe evidence and either expand the graph or certify the audited scope through a typed artifact.

## S1 — Operations

- State: A
- Function: autonomously perform software-engineering and related browser/desktop automation through model-selected tools and actions.
- Disturbance / variety regulated: unfamiliar codebases, implementation choices, command/test failures, browser/desktop state, provider/model variation, task ambiguity and bounded worker assignments.
- Decisive decision or feedback right: select substantive coding/tool actions, interpret operational evidence and determine how to satisfy the assigned engineering objective.
- Decision owner: the active model-backed AlphaCode coding agent; spawned swarm workers own their assigned operational workstreams.
- Supporting / enforcement mechanisms: built-in tool registry, provider routing, sessions, permissions/safety gates, context management, goal contracts, budgets and runtime cancellation.
- Closure path: user/coordinator goal → model chooses coding/tool actions → first-party runtime executes → evidence returns → model revises implementation or reports completion.
- Boundary reachability: ordinary AlphaCode sessions and spawned first-party swarm workers instantiate the same shipped coding runtime.
- Why this is / is not agent-owned: deterministic code executes and constrains actions; the model owns the open-ended engineering decision.
- Evidence: [README](https://github.com/dragonked2/alphacode/blob/a28db8978a5b336e244973c8db01f625dfcc0983/README.md); [agent.rs](https://github.com/dragonked2/alphacode/blob/a28db8978a5b336e244973c8db01f625dfcc0983/src/alphacode_app_core/agent.rs); [tool registry](https://github.com/dragonked2/alphacode/blob/a28db8978a5b336e244973c8db01f625dfcc0983/src/alphacode_app_core/tool/mod.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: external MCP/browser/provider services remain dependencies and are not credited as S1 owners.

## S2 — Coordination

- State: A
- Function: attenuate interference among concurrent swarm S1 units through model-selected graph decomposition, dependencies and assignment/takeover choices backed by first-party assignment and dependency enforcement.
- Disturbance / variety regulated: duplicate active assignment, two workers concurrently editing overlapping work, dependency-order violations, overloaded workers, stale/dead assignees and integration/synthesis ordering.
- Decisive decision or feedback right: choose task graph decomposition and dependency edges, select or request worker assignment, and explicitly reassign/replace/retry work when current peer interaction requires adjustment.
- Decision owner: the model-backed swarm coordinator through the model-callable swarm tool.
- Supporting / enforcement mechanisms: plan graph readiness, assignment-load ranking, in-flight target claims, active-assignment conflict rejection, worker heartbeats/staleness, dependency blocking/unblocking and typed node artifacts.
- Closure path: coordinator defines graph/assignments → runtime observes peer assignment/dependency/liveness state → conflicting or non-runnable work is blocked/rejected/reclaimed → coordinator receives current graph/worker feedback and can reassign, retry, replace, spawn or restructure → affected S1 work proceeds under the revised relation.
- Boundary reachability: the shipped swarm tool exposes task_graph, assign_task, assign_next, run_plan and task-control actions directly to the model; default swarm workers are first-party inline/headless AlphaCode sessions.
- Why this is / is not agent-owned: runtime code enforces conflict and readiness rules, but the coordinator model chooses the organizational partition, dependencies and substantive takeover/recovery action.
- Distinct S1 units: the coordinator/main coding agent and concurrently spawned first-party swarm worker coding agents, each owning a bounded task-graph node or workstream.
- Inter-S1 disturbance: active double assignment can make two workers edit the same work concurrently; dependencies, worker load/liveness and overlapping responsibility can also cause unsafe or stranded work.
- Attenuating coordination relation: model-selected task/dependency boundaries plus exclusive active assignment, load-aware worker selection, explicit takeover/reassignment and dependency gating.
- Feedback into subsequent S1 behaviour: rejected double assignment prevents a second worker from starting; completion/failure/staleness changes graph readiness; reassign/replace tells the displaced worker to stand down and directs subsequent execution to another worker.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the path explicitly regulates concrete peer-worker interference and dependency/liveness conflicts rather than merely moving messages or decomposing a parent task.
- Evidence: [communicate.rs](https://github.com/dragonked2/alphacode/blob/a28db8978a5b336e244973c8db01f625dfcc0983/src/alphacode_app_core/tool/communicate.rs); [comm_control.rs](https://github.com/dragonked2/alphacode/blob/a28db8978a5b336e244973c8db01f625dfcc0983/src/alphacode_app_core/server/comm_control.rs); [comm_graph.rs](https://github.com/dragonked2/alphacode/blob/a28db8978a5b336e244973c8db01f625dfcc0983/src/alphacode_app_core/server/comm_graph.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: low-level target claims and conflict rejection are deterministic support; the A classification rests on model ownership of graph/assignment/recovery choices.

## S3 — Inside-and-now control

- State: A
- Function: regulate the current multi-worker organization by maintaining a whole-swarm view and intervening in active commitments, worker allocation, retries, replacement and recovery.
- Disturbance / variety regulated: failed, stale, crashed or overloaded workers; blocked graph nodes; incomplete artifacts; low-confidence work; current concurrency pressure; stranded assignments and changing ready frontiers.
- Decisive decision or feedback right: inspect whole-plan/member/context state and choose current assignment, spawn, stop, retry, reassign, replace, salvage, graph expansion or other current commitment action.
- Decision owner: the model-backed swarm coordinator.
- Supporting / enforcement mechanisms: plan_status/task_graph summaries, member status, heartbeats, artifact metadata, read_context/summary, run_plan progress, task-control server transitions, concurrency budgets and resource guards.
- Closure path: coordinator observes current plan plus worker status/artifacts → chooses current-control action → first-party server mutates assignment/worker/graph state and interrupts or dispatches workers as required → subsequent current execution reflects the decision.
- Boundary reachability: the coordinator model receives the shipped swarm tool containing status, plan_status, summary/read_context, run_plan, spawn/stop and task-control actions; graph seeding can elect the seeding model session coordinator.
- Why this is / is not agent-owned: schedulers and resource guards enforce state transitions, but the model coordinator can inspect the whole current organization and choose the substantive commitment/recovery intervention.
- Whole-system current view: swarm plan status exposes node readiness/status/dependencies/assignees plus low-confidence debt, while member status, heartbeats, summaries and read_context expose current worker state and evidence.
- Current-control decision scope: worker/task assignment and replacement, retries/salvage, spawning/stopping agents, concurrency use, graph expansion and current integration/synthesis commitments.
- Evidence: [communicate.rs](https://github.com/dragonked2/alphacode/blob/a28db8978a5b336e244973c8db01f625dfcc0983/src/alphacode_app_core/tool/communicate.rs); [comm_control.rs](https://github.com/dragonked2/alphacode/blob/a28db8978a5b336e244973c8db01f625dfcc0983/src/alphacode_app_core/server/comm_control.rs); [comm_plan.rs](https://github.com/dragonked2/alphacode/blob/a28db8978a5b336e244973c8db01f625dfcc0983/src/alphacode_app_core/server/comm_plan.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: deterministic run_plan loops and resource monitors also make current decisions, but the positive A claim does not depend on treating those enforcement components as organizational owners.

## S3* — Complementary audit

- State: A
- Function: independently challenge completed deep-swarm work through separate critique/verify workers and force additional operational work when gaps remain.
- Disturbance / variety regulated: incomplete coverage, unsupported worker claims, low-confidence artifacts, missed edge cases and gaps hidden by ordinary worker completion reports.
- Decisive decision or feedback right: probe the audited scope and either inject concrete follow-up nodes or issue a passing gate artifact accounting for every audited node.
- Decision owner: the separate model-backed deep-mode critique/verify gate worker.
- Supporting / enforcement mechanisms: auto-inserted gate nodes, typed artifacts, audited-id accounting, low-confidence debt checks, complete_node validation and inject_gap graph mutation.
- Closure path: production nodes complete with artifacts → independent gate worker receives an explicit audit scope and probes it → gaps cause inject_gap and new operational nodes → after those drain the gate re-runs; only a sufficiently accounted clean artifact closes the gate → parent/composite work can then synthesize or finish.
- Boundary reachability: deep task_graph is a shipped swarm mode; deep expansion auto-inserts critique/verify gates that are dispatched through the same first-party worker infrastructure with gate-specific instructions.
- Why this is / is not agent-owned: deterministic server rules reject thin passes, but the separate gate model decides what to probe, whether a substantive gap exists and which follow-up nodes are needed.
- Claim being audited: that the completed sibling/node artifacts sufficiently cover their assigned scope and are ready for synthesis/closure.
- Ordinary reporting path: each production worker returns its typed completion artifact, validation, confidence and what_i_did_not_check list.
- Complementary access path: a separately dispatched full AlphaCode gate worker receives the aggregate audit scope, can use its own coding/repository tools to probe claims, and is instructed to seek gaps rather than accept the ordinary reports.
- Independence boundary: the gate is a separate worker/model session with a distinct adversarial role and explicit audited scope; it is not the author worker checking its own completion.
- Who acts on findings: the gate worker itself can inject new task-graph nodes; the coordinator/runtime dispatches those nodes and prevents the parent scope from closing until they drain.
- Evidence: [swarm core](https://github.com/dragonked2/alphacode/blob/a28db8978a5b336e244973c8db01f625dfcc0983/src/alphacode_swarm_core/mod.rs); [comm_control.rs](https://github.com/dragonked2/alphacode/blob/a28db8978a5b336e244973c8db01f625dfcc0983/src/alphacode_app_core/server/comm_control.rs); [comm_graph.rs](https://github.com/dragonked2/alphacode/blob/a28db8978a5b336e244973c8db01f625dfcc0983/src/alphacode_app_core/server/comm_graph.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the ordinary deterministic report claim checker is not used for this state; S3* rests on the separate adversarial deep-gate worker with direct first-party operational tooling.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party external-and-prospective adaptation loop is established at the assessed swarm/coding recursion.
- Disturbance / variety regulated: no qualifying future/external distinction is shown being turned by a distinct adaptation owner into options that return to change current organizational capability.
- Decisive decision or feedback right: none established for S4.
- Decision owner: none established.
- Supporting / enforcement mechanisms: persistent memory, web/browser tools, ambient scheduling, self_improve/selfdev tools, provider/tool discovery and project-analysis helpers may influence later work but are not sufficient S4 closure.
- Closure path: not applicable.
- Boundary reachability: no positive S4 path claimed.
- Why this is / is not agent-owned: self-improvement and memory can change or preserve behavior, but the Profile explicitly requires an external-and-prospective option-development conversation with present capability; the inspected paths remain task/current-repository, persistence or scheduled-execution mechanisms.
- Evidence: [memory tool](https://github.com/dragonked2/alphacode/blob/a28db8978a5b336e244973c8db01f625dfcc0983/src/alphacode_app_core/tool/memory.rs); [self_improve tool](https://github.com/dragonked2/alphacode/blob/a28db8978a5b336e244973c8db01f625dfcc0983/src/alphacode_app_core/tool/self_improve.rs); [ambient manager](https://github.com/dragonked2/alphacode/blob/a28db8978a5b336e244973c8db01f625dfcc0983/src/alphacode_app_core/ambient/manager.rs).
- Basis: structural absence review.
- Confidence: high.
- Caveats: web/ambient/selfdev surfaces are powerful extension and automation mechanisms, but no standard future-oriented adaptation loop into S3 was established.

### Absence scope

- Surfaces inspected: memory, self_improve/selfdev, ambient manager/runner/scheduler, browser/web tools, provider/tool discovery, project analyzer, resource monitor and session persistence.
- Plausible first-party paths checked: environmental trend sensing, future capability evaluation, generated adaptation alternatives, durable learned strategy and explicit return of such options into swarm current control.
- Why no material first-party path remains: inspected mechanisms store context, automate present tasks, improve the current repository or react to present runtime/resource conditions; none reconstructs the required external/future distinction → adaptation option → S3 capability change loop.

## S5 — Policy and identity

- State: —
- Function: no material identity/ultimate-policy governance loop is established at the coding/swarm recursion.
- Disturbance / variety regulated: no identity-level or ultimate-policy conflict is shown reaching an authoritative owner and returning as governing runtime policy.
- Decisive decision or feedback right: none established for S5.
- Decision owner: none established.
- Supporting / enforcement mechanisms: safety gates, destructive-action checks, permissions, system prompts, configuration, goals and resource budgets constrain ordinary operation but do not create identity authority.
- Closure path: not applicable.
- Boundary reachability: no positive S5 path claimed.
- Why this is / is not agent-owned: agents can adapt tactics and organize workers but cannot authoritatively redefine AlphaCode's identity or ultimate operating principles.
- Evidence: [README safety section](https://github.com/dragonked2/alphacode/blob/a28db8978a5b336e244973c8db01f625dfcc0983/README.md); [tool registry](https://github.com/dragonked2/alphacode/blob/a28db8978a5b336e244973c8db01f625dfcc0983/src/alphacode_app_core/tool/mod.rs); [resource monitor](https://github.com/dragonked2/alphacode/blob/a28db8978a5b336e244973c8db01f625dfcc0983/src/alphacode_app_core/autonomous/resource_monitor.rs).
- Basis: structural absence review.
- Confidence: high.
- Caveats: user configuration/approval and safety policy are legitimate constraints but do not establish S5.

### Absence scope

- Surfaces inspected: safety/destructive gates, permissions/configuration, system prompts, goal contracts, resource budgets, self-improvement and swarm control.
- Plausible first-party paths checked: autonomous constitutional revision, identity-policy escalation, legitimate parent identity authority and authoritative return-to-operation governance.
- Why no material first-party path remains: all observed policy surfaces regulate ordinary execution or development behavior rather than ultimate identity/policy closure.

## Distributed OSS parent arrangement

The assessed organization is the running AlphaCode coding/swarm organization, not the GitHub maintainer project. Repository contributor/release governance is not imported as runtime S3/S4/S5 ownership.

## Self-hosted and non-human modes

AlphaCode supports local and hosted models and first-party headless/inline swarm workers. Positive S2/S3/S3* claims use non-human first-party runtime modes and do not depend on generic human approval/configuration.

## Recursion

The run-level viable-unit boundary contains the coordinator/main coding S1 plus spawned coding S1 workers. The coordinator owns swarm S2/S3 decisions. Deep critique/verify workers provide complementary S3*. Individual tool calls, memory entries and deterministic schedulers are support components, not additional viable systems.

## Variety and escalation

S1 absorbs local coding/tool variety. S2 attenuates peer-worker interference and dependency conflict. S3 regulates the current worker/plan organization and recovery. Deep gate S3* challenges ordinary completion evidence and can amplify the graph with follow-up work. Memory, ambient automation and self-improvement do not establish S4/S5 under the frozen boundary.

## Evidence gaps

No ? state is required. The frozen first-party swarm implementation directly exposes worker identity, graph/assignment control, current-state intervention and adversarial deep gate closure, while the broad memory/adaptation/policy surfaces are sufficient for bounded negative S4/S5 conclusions.

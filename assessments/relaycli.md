---
harness_id: relaycli
project_name: RelayCLI
repository: https://github.com/joshuasetiawann/relaycli
review_ref: 2102796a136f996cbc48402cfb00304f5614e03e
reviewed_at: 2026-10-06
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-06
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: P
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# RelayCLI

## Review boundary

- System in focus: the first-party RelayCLI coding runtime at frozen revision 2102796a136f996cbc48402cfb00304f5614e03e, including the model-backed coding agents, on-by-default parallel task-graph path, scheduler/leases/budget machinery, interactive lane controls, supported sequential relay mode, tools, local session/memory/configuration and terminal/desktop execution surfaces.
- Purpose and identity: produce software-engineering outcomes inside a user project through autonomous coding agents, optionally decomposed into concurrent specialist S1 units and supported by a separate review path.
- Relevant environment: user goals and steering, repository contents and tool results, concurrent path/file contention, task dependencies and failures, model/provider failures, working-tree state, test results, permission constraints and persisted project/user notes.
- Standard-distribution boundary: shipped RelayCLI runtime and repository-owned agent/orchestrator, graph, scheduler, lease, relay, tool, permission, configuration, local memory and UI code. External model/provider endpoints, MCP servers, Ollama/9Router processes, browser/network services and the user's project itself remain environment/dependencies and cannot donate ownership.
- Credited operating / distribution surfaces: relaycli/agent/, relaycli/tools/, relaycli/relay.py, relaycli/core/, relaycli/ui/, relaycli/cli.py and supported one-shot/REPL/desktop modes.
- Adjacent first-party surfaces excluded from ownership: repository CI, tests, design/spec/plan documents, benchmarks and development history except where they corroborate a path wired into the shipped runtime.
- First-party operating / deployment modes considered: on-by-default parallel orchestration (experimental_parallel=true); interactive full-auto parallel mode with live lane controls; sequential relay mode reached by disabling parallel and enabling relay; plain single-agent fallback; supported local/cloud model routing and permission modes.
- Recursion level: one RelayCLI coding run. Concurrent specialist coding agents that own focused implementation outcomes are S1 units at this level; the one-shot Orchestrator and deterministic scheduler/lease layer organize those units. In sequential relay mode the Coder is the operational S1 and the Reviewer supplies a complementary audit path.
- Reviewed revision: 2102796a136f996cbc48402cfb00304f5614e03e.
- Observation date: 2026-10-06.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

RelayCLI's ordinary one-shot path defaults to parallel orchestration because Settings.experimental_parallel is True and cli.py dispatches to run_parallel_with_view before the relay/single-agent fallbacks. The parallel path creates one read-only Orchestrator agent, asks it for a JSON task graph containing role ownership, dependencies and path claims, and then hands that graph to a deterministic Scheduler. Each scheduled implementation task receives a fresh role-specific model-backed Agent with a ToolContext tied to its task id, shared LeaseManager and budget.

The Scheduler launches graph-ready tasks concurrently up to the configured cap. Path leases are specifically designed to prevent concurrent agents from corrupting the same file: overlapping path claims are serialized and write tools fail when the calling task lacks the relevant lease. Task completion/failure updates graph state and may release or block dependent work. The interactive full-auto lane view exposes current graph/lane state and routes user drop, retry and steer commands back into the Scheduler or running Agent.

RelayCLI also ships a distinct sequential relay mode. When parallel orchestration is disabled and relay is enabled, Planner → Coder → Reviewer runs as a bounded loop. The Reviewer is a separate read/exec agent that inspects the actual working tree, can run tests, and issues VERDICT: approve or VERDICT: revise; a revise verdict is returned to the Coder for another bounded cycle.

Local markdown memory is read into future Agent system prompts and the remember tool lets an agent append project/global facts. This is persistent operational context, but no first-party external-and-prospective adaptation loop is established merely by storing and later injecting those notes.

## Operational model

In the default parallel mode the Orchestrator makes a single model-owned coordination decision over the requested work: it proposes operational tasks, role assignments, dependencies and path claims. The deterministic graph/scheduler/lease machinery executes those constraints and handles task state transitions. It does not re-enter the Orchestrator with live outcomes, so static task decomposition is not credited as autonomous S3 current control.

The parent human can exercise a distinct current-control mode in the interactive live lane surface: the user sees the active task organization and can drop a live commitment, retry failed/cancelled work, steer a selected running agent, or stop the run. These decisions change graph state, lease availability or the next agent iteration and therefore form the parent-owned S3 path.

## S1 — Operations

- State: A
- Function: autonomously produce software-engineering outcomes by inspecting a project, editing files, running commands/tests and completing focused implementation goals.
- Disturbance / variety regulated: codebase structure, implementation choices, test/build failures, tool errors, model/provider variability, local task ambiguity and project-specific constraints.
- Decisive decision or feedback right: choose substantive implementation/investigation actions and determine how to respond to tool/model evidence within the assigned goal.
- Decision owner: each active model-backed RelayCLI coding Agent, including scheduled specialist agents in the parallel mode.
- Supporting / enforcement mechanisms: ToolRegistry/ToolContext, permissions, project-root confinement, model routing/escalation, call/token budgets, session trimming, file cache and path leases.
- Closure path: user/parent task → coding Agent interprets goal and project evidence → model selects tool/edit/test actions → tool results return into the Agent loop → Agent revises work until it completes or stops.
- Boundary reachability: the Agent loop and coding tools are the shipped runtime used by the default parallel task agents and the fallback single-agent/sequential relay modes.
- Why this is / is not agent-owned: removing the model-backed Agent leaves permissions, limits and tool executors but no open-ended choice of implementation or corrective action.
- Evidence: [relaycli/agent/loop.py](https://github.com/joshuasetiawann/relaycli/blob/2102796a136f996cbc48402cfb00304f5614e03e/relaycli/agent/loop.py); [relaycli/agent/orchestrator.py](https://github.com/joshuasetiawann/relaycli/blob/2102796a136f996cbc48402cfb00304f5614e03e/relaycli/agent/orchestrator.py); [relaycli/core/roles.py](https://github.com/joshuasetiawann/relaycli/blob/2102796a136f996cbc48402cfb00304f5614e03e/relaycli/core/roles.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: not every spawned process/task label is automatically an S1; the positive claim is limited to model-backed operational agents that own focused software-engineering outcomes.

## S2 — Coordination

- State: A
- Function: prevent destructive interference among concurrent coding S1 units by assigning explicit work/dependency/path-claim boundaries and enforcing mutually safe execution.
- Disturbance / variety regulated: the concrete collision mode in which two concurrent agents edit overlapping paths/files and can corrupt each other's work, plus dependency-order interference among tasks.
- Decisive decision or feedback right: decide each task's role, dependency edges and anticipated path claims, thereby defining which operational units may safely proceed independently and which interactions require ordering/serialization.
- Decision owner: the model-backed Orchestrator agent that emits the task graph; it chooses depends_on and path_claims from the user request before the scheduler executes them.
- Supporting / enforcement mechanisms: TaskGraph readiness, deterministic Scheduler concurrency cap, LeaseManager overlap detection/acquisition/release, write-tool lease checks and task failure/block propagation.
- Closure path: Orchestrator emits task/dependency/path-claim constraints → Scheduler compares graph readiness and active leases → conflicting units wait or unauthorized writes fail → lease/dependency state changes after completion/failure → affected S1 units become runnable/blocked accordingly.
- Boundary reachability: parallel orchestration is enabled by default at the frozen revision; cli.py dispatches ordinary one-shot requests into run_parallel_with_view, which constructs the Orchestrator, graph, Scheduler and LeaseManager.
- Why this is / is not agent-owned: the runtime deterministically enforces reservations, but removing the Orchestrator leaves no discretionary first-party actor deciding the task partition, dependencies or path claims from the request. The scheduler does not invent those organizational constraints itself.
- Distinct S1 units: concurrent role-specific coding Agents created by TaskAgentFactory for graph tasks whose goals can independently produce project changes.
- Inter-S1 disturbance: overlapping file/path edits can corrupt work; the lease module explicitly names this collision, and graph dependencies encode ordering needed when units are not independent.
- Attenuating coordination relation: model-selected dependency/path-claim boundaries plus scheduler serialization of overlapping claims and per-write lease enforcement.
- Feedback into subsequent S1 behaviour: a lease conflict keeps an otherwise graph-ready task from launching; completion releases the lease so it can proceed, while failed dependencies block descendants and lease violations fail the attempted write.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the path-lease mechanism is explicitly built around a structurally evidenced cross-agent collision, and the model-selected claims/dependencies directly determine mutual adjustment between peer coding units rather than merely transporting messages.
- Evidence: [relaycli/agent/orchestrator.py](https://github.com/joshuasetiawann/relaycli/blob/2102796a136f996cbc48402cfb00304f5614e03e/relaycli/agent/orchestrator.py); [relaycli/agent/graph.py](https://github.com/joshuasetiawann/relaycli/blob/2102796a136f996cbc48402cfb00304f5614e03e/relaycli/agent/graph.py); [relaycli/agent/scheduler.py](https://github.com/joshuasetiawann/relaycli/blob/2102796a136f996cbc48402cfb00304f5614e03e/relaycli/agent/scheduler.py); [relaycli/agent/leases.py](https://github.com/joshuasetiawann/relaycli/blob/2102796a136f996cbc48402cfb00304f5614e03e/relaycli/agent/leases.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: arbitration after the Orchestrator's graph decision is deterministic. The A claim is for agent ownership of the discretionary coordination constraints, not for the LeaseManager itself.

## S3 — Inside-and-now control

- State: P
- Function: provide whole-run current control over active commitments by exposing current lanes/graph state to a parent user who can intervene in one task or stop the run.
- Disturbance / variety regulated: wedged or failed tasks, commitments that should be dropped, newly relevant instructions for a running lane, blocked descendants/leases and a run that should be stopped.
- Decisive decision or feedback right: decide whether a current task is cancelled, retried, steered with a new instruction, or whether all current work is stopped.
- Decision owner: the human operator in the supported interactive live-lane mode.
- Supporting / enforcement mechanisms: live frame/status/lane rendering, Scheduler request_cancel/request_retry/request_steer, graph reset/block logic, lease release, Agent steer inbox and stop polling.
- Closure path: parent observes current whole-run lane state → selects drop/retry/steer/stop → UI dispatches the decision to Scheduler/Agent → graph/lease state or the agent's next iteration changes → subsequent current operation reflects the intervention.
- Boundary reachability: the live lane control surface is wired into ordinary parallel execution when the run is interactive, terminal-capable and in full-auto mode; unsupported display conditions fall back to progress lines rather than silently claiming the same parent-control surface.
- Why this is / is not agent-owned: the one-shot Orchestrator creates the initial task graph but is not re-entered with live Scheduler outcomes, and deterministic scheduling/failure propagation does not own a discretionary whole-system current-control judgment. The closed intervention mode belongs to the user.
- Whole-system current view: the live frame reads the Scheduler's current graph, task statuses, leases, outcomes/activity and selected lane while the run is active.
- Current-control decision scope: parent intervention over active commitments via drop/cancel, retry (including unblocking descendants), steer of a selected live agent and stop-all.
- Evidence: [relaycli/ui/live.py](https://github.com/joshuasetiawann/relaycli/blob/2102796a136f996cbc48402cfb00304f5614e03e/relaycli/ui/live.py); [relaycli/agent/scheduler.py](https://github.com/joshuasetiawann/relaycli/blob/2102796a136f996cbc48402cfb00304f5614e03e/relaycli/agent/scheduler.py); [relaycli/agent/loop.py](https://github.com/joshuasetiawann/relaycli/blob/2102796a136f996cbc48402cfb00304f5614e03e/relaycli/agent/loop.py); [README.md](https://github.com/joshuasetiawann/relaycli/blob/2102796a136f996cbc48402cfb00304f5614e03e/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: static graph decomposition, concurrency limits, budget stops and automatic subtree blocking are not credited as autonomous S3. The parent-control path is mode-specific rather than guaranteed for every invocation.

## S3* — Complementary audit

- State: A
- Function: independently inspect implemented work against the request/plan and return an approve/revise judgment that can force another coding cycle.
- Disturbance / variety regulated: incorrect or incomplete implementation claims, divergence from the requested plan, failing verification and defects not visible in the Coder's ordinary self-report.
- Decisive decision or feedback right: inspect the actual working tree, run verification as needed, and issue the review judgment VERDICT: approve or VERDICT: revise.
- Decision owner: the separate model-backed Reviewer Agent in the supported sequential relay mode.
- Supporting / enforcement mechanisms: read/exec-only reviewer capability boundary, verdict parser, bounded review-cycle counter and deterministic Relay loop that forwards revise feedback to the Coder.
- Closure path: Coder completes and reports → Reviewer receives request/plan/report but also inspects actual working tree/tests independently → Reviewer issues verdict → revise is returned to the Coder as corrective feedback or approve terminates the quality loop → subsequent operation changes.
- Boundary reachability: sequential relay is shipped and reachable by disabling the on-by-default parallel path and enabling relay (for example --no-experimental-parallel --relay); the Reviewer role and loop are first-party runtime code, not a repository-development-only evaluator.
- Why this is / is not agent-owned: the Reviewer itself makes the substantive audit judgment; parsing VERDICT and looping are deterministic support. Its direct working-tree/test access is materially different from trusting the Coder's report.
- Claim being audited: the Coder's claim that the current implementation satisfies the user's request and the Planner's plan.
- Ordinary reporting path: the Coder's own final text/report and normal implementation tool results.
- Complementary access path: a separate read/exec Reviewer Agent is instructed to inspect the actual working tree and can run tests before issuing a verdict.
- Independence boundary: the Reviewer is a separately instantiated model-backed agent with no write capability in its role, separate prompt/model routing and direct evidence access; it is not the Coder rephrasing its own completion statement.
- Who acts on findings: the deterministic Relay loop routes a revise judgment back to the Coder for another bounded cycle; an approve judgment closes the run.
- Evidence: [relaycli/relay.py](https://github.com/joshuasetiawann/relaycli/blob/2102796a136f996cbc48402cfb00304f5614e03e/relaycli/relay.py); [relaycli/core/roles.py](https://github.com/joshuasetiawann/relaycli/blob/2102796a136f996cbc48402cfb00304f5614e03e/relaycli/core/roles.py); [relaycli/cli.py](https://github.com/joshuasetiawann/relaycli/blob/2102796a136f996cbc48402cfb00304f5614e03e/relaycli/cli.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the frozen CLI checks experimental_parallel before relay_enabled, so relay review is not the default path and --relay alone does not bypass an otherwise enabled parallel mode; the positive claim is limited to the reachable sequential-relay configuration.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party external-and-prospective adaptation loop is established.
- Disturbance / variety regulated: no qualifying S4 disturbance is placed under a loop that senses changing external/future conditions, develops adaptation options and returns them into present capability.
- Decisive decision or feedback right: none established for S4.
- Decision owner: none established.
- Supporting / enforcement mechanisms: durable markdown memory, the remember tool, researcher/web tools, model-provider health tracking/escalation, skills and persistent configuration can inform later work but do not by themselves close S4.
- Closure path: not applicable.
- Boundary reachability: no positive S4 path claimed.
- Why this is / is not agent-owned: an Agent may save a fact because future sessions may need it and later sessions receive memory in their system prompt, but this is memory update/reuse rather than an evidenced external-and-prospective option-development conversation with current S3. Provider escalation reacts to current call failure rather than modeling future adaptation.
- Evidence: [relaycli/core/memory.py](https://github.com/joshuasetiawann/relaycli/blob/2102796a136f996cbc48402cfb00304f5614e03e/relaycli/core/memory.py); [relaycli/tools/remember.py](https://github.com/joshuasetiawann/relaycli/blob/2102796a136f996cbc48402cfb00304f5614e03e/relaycli/tools/remember.py); [relaycli/agent/router.py](https://github.com/joshuasetiawann/relaycli/blob/2102796a136f996cbc48402cfb00304f5614e03e/relaycli/agent/router.py); [relaycli/core/roles.py](https://github.com/joshuasetiawann/relaycli/blob/2102796a136f996cbc48402cfb00304f5614e03e/relaycli/core/roles.py).
- Basis: structural absence review.
- Confidence: high.
- Caveats: task-local web/research can gather external facts, but no standard first-party loop was found that turns those facts into prospective adaptation options for the harness and returns them to current capability.

### Absence scope

- Surfaces inspected: memory read/write/injection, skills, researcher/web tools, model routing/health escalation, configuration, task graph, relay review and UI/runtime state.
- Plausible first-party paths checked: cross-session memory, external web/research, provider capability/failure sensing, role/tier configuration and learned/project notes.
- Why no material first-party path remains: each path is either current-task evidence, persistence/configuration, or reactive fallback. None reconstructs the required external/future distinction → adaptation option → return-to-present-capability loop.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy governance loop is established at the run recursion.
- Disturbance / variety regulated: no identity-level conflict or S3–S4 policy tension is shown reaching an ultimate authority and returning as governing policy.
- Decisive decision or feedback right: none established for S5.
- Decision owner: none established.
- Supporting / enforcement mechanisms: permission modes, security prompt text, project-root/secret protections, role capability definitions, persisted model/relay settings and user approvals constrain operations but do not create identity-policy closure.
- Closure path: not applicable.
- Boundary reachability: no positive S5 path claimed.
- Why this is / is not agent-owned: neither the Orchestrator nor operational agents have authority to redefine RelayCLI's identity or ultimate policy, and routine user permissions/settings are operational constraints rather than S5 decisions.
- Evidence: [relaycli/core/permissions.py](https://github.com/joshuasetiawann/relaycli/blob/2102796a136f996cbc48402cfb00304f5614e03e/relaycli/core/permissions.py); [relaycli/core/config.py](https://github.com/joshuasetiawann/relaycli/blob/2102796a136f996cbc48402cfb00304f5614e03e/relaycli/core/config.py); [relaycli/core/roles.py](https://github.com/joshuasetiawann/relaycli/blob/2102796a136f996cbc48402cfb00304f5614e03e/relaycli/core/roles.py); [relaycli/agent/loop.py](https://github.com/joshuasetiawann/relaycli/blob/2102796a136f996cbc48402cfb00304f5614e03e/relaycli/agent/loop.py).
- Basis: structural absence review.
- Confidence: high.
- Caveats: a human can change settings and approve or stop ordinary actions, but no qualifying identity/ultimate-policy issue and return-to-operation governance path is established.

### Absence scope

- Surfaces inspected: system/role prompts, permission modes, security controls, persistent configuration, lane intervention controls, relay verdicts, memory and project/user settings.
- Plausible first-party paths checked: parent permission/configuration authority, durable security policy, role/capability changes, model/relay settings and runtime intervention.
- Why no material first-party path remains: these surfaces regulate ordinary execution, safety or configuration. They do not expose an identity/ultimate-policy dispute and authoritative decision loop at the assessed recursion.

## Distributed OSS parent arrangement

The assessed organization is the running RelayCLI coding organization, not the GitHub maintainer project. CI, repository design documents, commits and contributor/release decisions are not imported as runtime parent S3/S4/S5 ownership.

## Self-hosted and non-human modes

RelayCLI supports local Ollama and cloud providers. Autonomous S1/S2 and S3* claims depend on first-party agent/runtime paths, not on a particular external provider. The explicit S3 parent mode is the local human operator's live-run intervention surface; no parent S4/S5 mode is inferred from general configuration rights.

## Recursion

The run-level viable-unit boundary contains model-backed coding S1 units plus coordinating/control/audit mechanisms. A specialist spawned for a focused task is not automatically treated as a recursively viable organization merely because it is another Agent process; this assessment claims only its operational S1 role at the parent run.

## Variety and escalation

Local coding variety stays with each S1 Agent. Cross-agent collision/order variety is attenuated through Orchestrator-selected task constraints plus leases (S2). Whole-run exceptions can reach the parent through the live lane surface (S3=P). Implementation claims can move through the separate Reviewer path (S3*=A). Provider-tier escalation, budgets and scheduler failure propagation are supporting runtime mechanisms rather than additional VSM functions.

## Evidence gaps

No ? state is required. Frozen source establishes the default parallel coordination path, the parent live-control mode and the separate relay reviewer path directly, while the inspected memory/routing/configuration surfaces are broad enough to support the narrower S4/S5 absence conclusions.

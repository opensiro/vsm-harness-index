---
harness_id: halay
project_name: halay
repository: https://github.com/halayhq/halay
review_ref: 49bccfcb75e805b7ab55bb40c92a109dcdc62c24
reviewed_at: 2026-11-05
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# halay

## Review boundary

- System in focus: A configured self-hosted halay Node server, its built-in Swarm chat conductor and child CLI agent fleet, not the upstream Claude Code/OpenCode/Cursor/Gemini/Antigravity implementations or vendors.
- Purpose and identity: Local UI and control plane for multiple directory-scoped agent CLI processes, with task assignment, parent/child notifications, permissions, schedules and optional peer instances.
- Relevant environment: User objectives, agent CLI status and result events, project directories, approval requests, task dependencies, model/backend availability and persistent server records.
- Standard-distribution boundary: `src/server.js`, `src/swarm-mcp.js`, `src/prompts.js`, `src/backends/*`, `src/agent-notify.js`, `src/bots.js`, `src/rooms.js`, `prompts/conductor.md` and bundled web UI; at least one separately installed CLI is a stated runtime prerequisite.
- Credited operating / distribution surfaces: [server/control](https://github.com/halayhq/halay/blob/49bccfcb75e805b7ab55bb40c92a109dcdc62c24/src/server.js), [agent MCP tools](https://github.com/halayhq/halay/blob/49bccfcb75e805b7ab55bb40c92a109dcdc62c24/src/swarm-mcp.js), [swarm conductor prompt](https://github.com/halayhq/halay/blob/49bccfcb75e805b7ab55bb40c92a109dcdc62c24/prompts/conductor.md), [role prompts](https://github.com/halayhq/halay/blob/49bccfcb75e805b7ab55bb40c92a109dcdc62c24/src/prompts.js), [notifications](https://github.com/halayhq/halay/blob/49bccfcb75e805b7ab55bb40c92a109dcdc62c24/src/agent-notify.js).
- Adjacent first-party surfaces excluded from ownership: Upstream CLIs' internal model/tool loops and their safety/policies, human approvals, operator-authored schedule choices, remote peer servers not under a given instance's control, tests/demos and external models. Only roles/tool/feedback wiring supplied by halay receives credit.
- First-party modes inspected: Swarm chat conductor, `start_agent`/`send_message`/`read_agent`/`wait_for_agent`/`interrupt_agent`, child wakeup notifications and status, task dependency/assignment management, workspace worktrees, passkey/tool approvals and scheduled tasks.
- Recursion level: A single locally deployed halay conductor and its present child task agents; peer instances are separately operated, not assumed centrally governed by this installation.
- Reviewed revision: `halayhq/halay@49bccfcb75e805b7ab55bb40c92a109dcdc62c24` (first-party Apache-2.0 distribution).
- Observation date: 2026-11-05.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

The Node server spawns directory-specific external agent CLIs, stores agent/task metadata and emits status/event streams. The bundled conductor is a dedicated CLI agent with the first-party `prompts/conductor.md` role and first-party swarm MCP tools. It can inspect currently running children, choose which process/model/folder handles work, send follow-ups, receive child completion or blocking notifications, alter task assignments and stop child jobs. Child agents also receive scoped swarm delegation and messaging tools; non-conductors can control only their own children. Dependency tracking marks queued tasks ready/waiting/blocked, and the task API rejects unsatisfied dependencies. UI and scheduled jobs expose additional operator choices. Actual code editing/tool use inside each child is performed by an upstream installed CLI: the vendor's internal autonomy is explicitly *not* halay-owned. [server](https://github.com/halayhq/halay/blob/49bccfcb75e805b7ab55bb40c92a109dcdc62c24/src/server.js), [MCP](https://github.com/halayhq/halay/blob/49bccfcb75e805b7ab55bb40c92a109dcdc62c24/src/swarm-mcp.js), [conductor](https://github.com/halayhq/halay/blob/49bccfcb75e805b7ab55bb40c92a109dcdc62c24/prompts/conductor.md).

## Operational model

The first-party installation *wires* externally supplied CLI decision engines into multiple accountable task actors and provides model-addressable action/feedback for their role-specific work. Within this operating composition, S1 credit is limited to executable model-directed tasks made addressable and observable by halay; it is not attribution of the vendor CLIs' internal harness architectures. The shipped conductor itself owns discretionary task-portfolio decisions via first-party MCP action permissions and returned child status. Merely relaying events, managing schedules or denying risky tools does not add further VSM functions.

## S1 — Operations

- State: A
- Function: Distinct user-task agents operate in their assigned project directories through the launched configured CLI.
- Disturbance / variety regulated: Changing user requests, project state and subprocess/tool feedback delivered to each CLI session.
- Decisive decision or feedback right: Each running model-backed CLI agent chooses task actions and next turns, while halay controls the first-party spawning, routing, replies and child communication interface.
- Decision owner: Individual CLI-backed model task actor, through halay's installed multi-agent composition; not Node HTTP request routing alone.
- Supporting / enforcement mechanisms: Backends, per-agent cwd/account/model, MCP swarm tools, event stream, permissions and optional worktrees.
- Closure path: User/conductor task→halay launches addressed CLI agent→upstream engine acts in workspace→result/status returns via halay→model continues, receives follow-up or returns result.
- Boundary reachability: `src/server.js` launches supported CLI processes and `src/swarm-mcp.js` exposes actionable tools; this requires one external CLI installed and authenticated, and does not credit its underlying internal tool loop as a first-party implementation.
- Why this is / is not agent-owned: Real CLI-backed models have discretion over work; the first-party control plane enables and observes their running roles. The launcher alone would not be autonomous.
- Evidence: [spawn and task lifecycle](https://github.com/halayhq/halay/blob/49bccfcb75e805b7ab55bb40c92a109dcdc62c24/src/server.js), [backends](https://github.com/halayhq/halay/blob/49bccfcb75e805b7ab55bb40c92a109dcdc62c24/src/backends/index.js), [swarm tools](https://github.com/halayhq/halay/blob/49bccfcb75e805b7ab55bb40c92a109dcdc62c24/src/swarm-mcp.js).
- Basis: Supported executable agent-CLI composition and returned operational state, not claimed first-party model internals.
- Confidence: Medium-high for first-party runtime integration, not upstream vendor correctness.
- Caveats: The prerequisite external CLI supplies cognition, local tool semantics and vendor behavior; absent a configured backend, halay is an idle control plane.

## S2 — Coordination

- State: —
- Function: No separately demonstrated autonomous attenuation of an observed conflict among the multiple operating child units.
- Disturbance / variety regulated: Shared-workspace collisions and competing task dependencies are plausible; the default task DAG orders work but is authored and assigned as a workflow, not measured inter-S1 contention.
- Decisive decision or feedback right: First-party dependency gate rejects blocked starts; conductor can manually/model-select routing as S3 rather than independent S2 balancing.
- Decision owner: User/conductor for assignments, deterministic task dependency guard for eligibility.
- Supporting / enforcement mechanisms: Task graph `depends_on`, worktrees, agent message bus, parent-child scoped tools and queues.
- Closure path: Task dependency→ready/waiting/blocked gate or manual assignment; messages travel between actors, but no installed contention sensing→S2 arbitration→revised peer behavior loop.
- Why this is / is not agent-owned: Tool messages, worktree isolation and static dependency checks are valuable coordination infrastructure without evidence of a specific separately owned S2 regulator.
- Evidence: [task dependency/agent management](https://github.com/halayhq/halay/blob/49bccfcb75e805b7ab55bb40c92a109dcdc62c24/src/server.js), [swarm tool interface](https://github.com/halayhq/halay/blob/49bccfcb75e805b7ab55bb40c92a109dcdc62c24/src/swarm-mcp.js).
- Basis: Bounded absence after testing strongest task-DAG and peer-messaging candidates.
- Confidence: Medium-high.
- Caveats: A conductor can respond to a user-observed conflict, but no distinct routine S2 feedback mandate was found in the shipped setup.

### Absence scope

- Surfaces inspected: Task status/dependency engine, conductor prompt, child message and notification API, worktree/start guards.
- Plausible first-party paths checked: Dependency DAG as balancing, worktree isolation as conflict regulation, peer messaging as S2, conductor reallocation as S2.
- Why no material first-party path remains: The code exposes order, isolation and messages but no specific inter-S1 disturbance measurement and returned balancing adjustment distinct from task assignment/S3.

## S3 — Inside-and-now control

- State: A
- Function: Shipped model-driven conductor supervises the present agent fleet and allocates/revises task commitments and capacity.
- Whole-system current view: Conductor's `list_agents`, task listing, status/attention, child-result notifications and account availability expose the bounded installed fleet and current work backlog, rather than a single worker's perspective.
- Current-control decision scope: Conductor can choose and revise work-to-child allocation, active agent count/model/folder, follow-up task instructions and interruption in response to observed fleet state.
- Disturbance / variety regulated: Concurrent user requests across projects, idle/busy/blocked children, failed tasks, approval pauses, delayed results and current model/account capacity.
- Decisive decision or feedback right: Conductor chooses whether to create or reuse an agent, what folder/model/account to assign, when to message or interrupt it and how to react to its returned result/status.
- Decision owner: Conductor model running with the bundled role prompt and privileged first-party swarm MCP rights; runtime enforces access scopes and completion notifications.
- Supporting / enforcement mechanisms: `list_agents`, `start_agent`, `send_message`, `read_agent`, task assignment, stop/interrupt, child-finish notifications, persistent fleet state and task dependency gates.
- Closure path: User's multi-project goal→conductor lists fleet/task state→selects agent and assignment→agent acts→halay notifies its completion/error/block→conductor revises instructions, assignments or informs user.
- Boundary reachability: A shipped Swarm chat has its own conductor role and tool permissions; unlike a passive dashboard it can model-select concrete task allocation from returned runtime state.
- Why this is / is not agent-owned: The first-party conductor prompt gives the model an operational portfolio mandate and action rights; subprocess state and database enforcement support rather than replace its choices.
- Evidence: [conductor mandate](https://github.com/halayhq/halay/blob/49bccfcb75e805b7ab55bb40c92a109dcdc62c24/prompts/conductor.md), [scoped MCP actions](https://github.com/halayhq/halay/blob/49bccfcb75e805b7ab55bb40c92a109dcdc62c24/src/swarm-mcp.js), [fleet/task state and wakeup](https://github.com/halayhq/halay/blob/49bccfcb75e805b7ab55bb40c92a109dcdc62c24/src/server.js), [notification format](https://github.com/halayhq/halay/blob/49bccfcb75e805b7ab55bb40c92a109dcdc62c24/src/agent-notify.js).
- Basis: Reachable first-party conductor perception→discretionary allocation/revision→child-action→status feedback over a bounded fleet.
- Confidence: High for installed mandate and capability, not measured real fleet performance.
- Caveats: The conductor's decision model runs via a required external CLI and may fail to act on feedback; human controls, context budgets and per-child permissions constrain it.

## S3* — Complementary audit

- State: —
- Function: No independent alternate evidence path produces an audit verdict returned to conductor beyond ordinary agent and tool reports.
- Disturbance / variety regulated: False child completion claims and unsafe changes could be reviewed by humans; no separate installed auditing reviewer independently samples operational reality.
- Decisive decision or feedback right: Conductor can read child transcript, summaries and git status, but this is ordinary supervision; approvals are chosen by the human.
- Decision owner: Conductor for monitoring and operator for approvals; no complementary auditor with independent judgment/return authority.
- Supporting / enforcement mechanisms: Agent transcript, worktree state, browser UI, status notifications, reviewable git changes and authentication.
- Closure path: Child events→conductor/UI; no independent artifact sampling/replay→adversarial audit finding→corrective S3 loop in standard distribution.
- Why this is / is not agent-owned: A separate transcript reader does not gain a distinct independent observational channel, and the human may optionally review but is outside first-party installed audit.
- Evidence: [swarm read/status](https://github.com/halayhq/halay/blob/49bccfcb75e805b7ab55bb40c92a109dcdc62c24/src/swarm-mcp.js), [event handling](https://github.com/halayhq/halay/blob/49bccfcb75e805b7ab55bb40c92a109dcdc62c24/src/server.js).
- Basis: Bounded absence review of strongest transcript/worktree evidence paths.
- Confidence: Medium-high.
- Caveats: External CLI vendors or human code review may supply external auditors, not credited to halay by default.

### Absence scope

- Surfaces inspected: Conductor prompt, status/read tools, worktree/git actions, permission callbacks and child-finish notifications.
- Plausible first-party paths checked: Conductor's `read_agent` as audit, worktree diff as independent reality, notification watcher as auditor, user approval as S3*.
- Why no material first-party path remains: The credited standard path provides reporting and ordinary monitoring, but no independently owned alternative evidence judgment with an authoritative corrective return.

## S4 — Outside-and-then intelligence

- State: —
- Function: No continuous prospective environment analysis selects future capability/organizational changes for this fleet.
- Disturbance / variety regulated: New CLI backends, future user work, schedule timing, model prices and capacity changes.
- Decisive decision or feedback right: Operator configures accounts/backends and schedules; conductor handles current task choices and user-described future jobs.
- Decision owner: Human operator for product/organizational evolution, conductor model for present tasks.
- Supporting / enforcement mechanisms: Backend discovery, scheduled/recurring tasks, durable bots, peer configuration and model selection.
- Closure path: User configuration/schedule→current or timed execution; no outside environmental forecast→strategic option selection→negotiation with current S3 and adopted future operating rule.
- Why this is / is not agent-owned: Scheduled execution and selectable backends are operational capacity, not autonomous anticipation of changing external circumstances.
- Evidence: [server and task schedule](https://github.com/halayhq/halay/blob/49bccfcb75e805b7ab55bb40c92a109dcdc62c24/src/server.js), [conductor instructions](https://github.com/halayhq/halay/blob/49bccfcb75e805b7ab55bb40c92a109dcdc62c24/prompts/conductor.md), [bots](https://github.com/halayhq/halay/blob/49bccfcb75e805b7ab55bb40c92a109dcdc62c24/src/bots.js).
- Basis: Bounded absence review including strongest persistent/scheduled mode.
- Confidence: High.
- Caveats: Conductor can be asked to research future changes as a one-off S1 work item; no permanent S4 function follows.

### Absence scope

- Surfaces inspected: Schedules, bot memory, backend detection/configuration, conductor system role and peer administration.
- Plausible first-party paths checked: Recurring tasks as future sensing, model/backend routing as adaptive strategy, persistent bots as future learning, peer federation as external intelligence.
- Why no material first-party path remains: No shipped autonomous choice of a future organizational repertoire from external sensing and a returned S4→S3 decision loop.

## S5 — Policy and identity

- State: —
- Function: No distinct legitimate ultimate identity-policy role owns and closes an organizational charter/mandate.
- Disturbance / variety regulated: Privileged agent management, resource/cost limits, malicious agents, user identity/authentication and permission escalation.
- Decisive decision or feedback right: Authenticated human owner sets controls; static role access enforces conductor versus child scope, and the user decides tool approvals.
- Decision owner: Operator for legitimate ultimate constraints, deterministic auth/MCP guard for enforcement.
- Supporting / enforcement mechanisms: Passkeys, per-agent bearer tokens, parent ownership checks, approval mode, model/account boundaries and persistent configuration.
- Closure path: Operator setting or approval→guarded API behavior; no autonomous or parent-assisted identity-policy deliberation and returned authoritative mandate to S3/S4.
- Why this is / is not agent-owned: Strong security and an exclusive conductor role are not sufficient for an independent governance legitimacy cycle.
- Evidence: [auth/access](https://github.com/halayhq/halay/blob/49bccfcb75e805b7ab55bb40c92a109dcdc62c24/src/auth.js), [MCP scoping](https://github.com/halayhq/halay/blob/49bccfcb75e805b7ab55bb40c92a109dcdc62c24/src/swarm-mcp.js), [server](https://github.com/halayhq/halay/blob/49bccfcb75e805b7ab55bb40c92a109dcdc62c24/src/server.js).
- Basis: Bounded absence after screening legitimate operator policy and role privilege paths.
- Confidence: High.
- Caveats: A human-led institution could govern an installed halay fleet; it is not a supplied self-governing S5 actor.

### Absence scope

- Surfaces inspected: Authentication, privileged conductor and child permissions, configuration, system prompts and approval tools.
- Plausible first-party paths checked: Conductor priority as S5, passkey identity as policy identity, parent-child tool scope as legitimate charter, operator approval as parent-assisted S5.
- Why no material first-party path remains: No first-party governing actor resolves identity-level dilemmas and returns an enduring legitimate mandate with authority over operational strategy.

## Recursion

The first-party conductor supervises multiple bounded, distinct child CLI task actors, sufficient for S3 at this recursion. External CLI internals and separate peer swarms are not double-counted as deeper or centrally governed viable systems.

## Variety and escalation

Many models/folders, peer relay and scoped messaging amplify operating variety. User approval and task dependency rules constrain actions. Errors, blocks and child completion events reach conductor through notifications for possible reallocation. An independent audit circuit or S4/S5 governance escalation is not installed.

## Evidence gaps

- External CLI installation/login and paid provider-backed fleet execution were not replayed; source-reachable orchestration and bundled task-control interfaces are assessed.
- The external CLI model and its internal model/tool behavior remain external; S1 and S3 findings concern halay's installed composition, roles, available actions and returns, not upstream vendor autonomy score attribution.
- The database dependency system and worktree isolation reduce collisions, but no separate adaptive S2 feedback owner or independent S3* reviewer was observed in this frozen version.

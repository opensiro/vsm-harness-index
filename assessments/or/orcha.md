---
harness_id: orcha
project_name: Orcha
repository: https://github.com/open-orcha/orcha
review_ref: 1ad8ce3bbce2c21bc916509e805c893e16d24c3d
reviewed_at: 2026-11-18
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: P
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: P
---

# Orcha

## Review boundary
- System in focus: One installed per-project Orcha/Embodent SQLite+FastAPI service, configured human project owner, registered model-backed work agents, and first-party project skills, worker lifecycle and verification flow.
- Purpose and identity: Coordinate concurrent project tasks, enforce human authority over assignments and ultimate objective, and route completion evidence/review back to operating agent sessions.
- Relevant environment: Project code, agent task assignments, dependency/readiness state, questions and escalations between agents, human directions, objective and proof-of-work evidence.
- Standard-distribution boundary: Local `orcha init`, FastAPI portal and database, bundled slash-command skills and spawned supervised Claude/Codex worker sessions and first-party wake/dispatch/decision policies. Whole external Claude Code/Codex internals are not credited as native Orcha governance owners.
- Credited operating / distribution surfaces: Shipped per-project task claim and agent skill protocol, resident worker wake/dispatch, shared task/request states, human-only task hold/reassignment and verification, optional AI manager pre-review and authoritative project objective settings.
- Adjacent first-party surfaces excluded from ownership: Separate hosted company/business service, developer CI/tests, optional unpublished roadmap, arbitrary noninstalled autonomous custom agents, unconfigured external providers.
- First-party operating / deployment modes considered: Local project installed with supported Claude Code/Codex model-backed agents using bundled skill commands and server-backed worker runtime; a registered human manager; optional AI-manager prereview before human final verify.
- Recursion level: A project work organization of multiple dispatched agents under one human ultimate authority.
- Reviewed revision: 1ad8ce3bbce2c21bc916509e805c893e16d24c3d.
- Observation date: 2026-11-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture
The installed per-project service stores a shared project objective, registered humans/agents, task dependency/priority states, request chains, worktree status and review outcomes. Bundled Orcha skills tell a supported model-backed Claude/Codex session how to claim a task, inspect its full definition/protocol, perform concrete work, post progress, submit deliverables and react to wake messages. Worker-spawn and event services keep active model sessions connected to project work. Human authorization is enforced by API `kind=human` checks on decisions, assignment/reassignment, project controls and final verification. A configured AI manager can separately pre-review a submitted task and issue `send_back` with reasons, returning an operational task to the assignee; final completion remains human-authorized.

## Operational model
The operational cell is a source-connected model worker running bundled Orcha skill protocol and responding to the registered task environment; the model chooses task-substantive project actions, while Orcha's task system provides authoritative claims, worktree lifecycle, communication, rejection and feedback. The project owner observes the joint task/agent state, holds or reassigns available tasks and approves work. The optional AI manager pre-review is a distinct task-evidence reviewer with a send-back path; it is not independent low-level test execution by default. The project owner retains the mission/objective and mandated-human final verification rights. Autonomous external Claude Code or Codex model internals are not separately credited.

## S1 — Operations
- State: A
- Function: Execute assigned development/research tasks using model-selected work in the per-project orchestration protocol.
- Disturbance / variety regulated: Changing implementation requirements, source files, task instructions, DoD checks, incoming review/reassignment requests.
- Decisive decision or feedback right: Select substantive edits, answers and next work actions after receiving the task details and events.
- Decision owner: Orcha-launched and skill-guided model-backed worker, whose action rights are bounded by the installed Orcha task protocol.
- Supporting / enforcement mechanisms: Shipped /orcha-next and /orcha-done skill templates, first-party task claim endpoint, managed worker spawn/wake, per-project SQLite state and task thread.
- Closure path: Model worker claims full task, performs project actions, posts results, receives verification or manager review and resumes/revises work; completion and task readiness are returned to the shared project state.
- Boundary reachability: `orcha init` installs first-party skill templates into a real project, registers human and starts local service; documented standard use opens supported Claude Code/Codex sessions which execute the protocol. A model provider is a dependency, not a source of unshipped S3-S5 functions.
- Why this is / is not agent-owned: Within the supported installed mode, the model agent rather than a fixed task dispatcher chooses substantive project changes. This credit is limited to the task worker with first-party routing/feedback and does not import the external CLI's internal higher-order organization.
- Evidence: [installed project and task loop](https://github.com/open-orcha/orcha/blob/1ad8ce3bbce2c21bc916509e805c893e16d24c3d/README.md#L187-L258), [shipped /orcha-next operational contract](https://github.com/open-orcha/orcha/blob/1ad8ce3bbce2c21bc916509e805c893e16d24c3d/orcha-cli/orcha_cli/templates/skills/orcha-next.md#L1-L68), [human verification feedback](https://github.com/open-orcha/orcha/blob/1ad8ce3bbce2c21bc916509e805c893e16d24c3d/orcha-cli/orcha_cli/templates/portal/portal_backend/task_verification_routes.py#L36-L82), [working-agent wake decisions](https://github.com/open-orcha/orcha/blob/1ad8ce3bbce2c21bc916509e805c893e16d24c3d/orcha-cli/orcha_cli/llm_decisions.py#L1-L90).
- Basis: structural
- Confidence: medium
- Caveats: The first-party Orcha service does not own the external model host's tool loop. A functioning installed Claude/Codex worker is required; no paid live model run was conducted.

## S2 — Coordination
- State: —
- Function: No separately evidenced project-level active interference attenuation that resolves a concrete pair of competing S1 disturbances rather than workflow scheduling alone.
- Disturbance / variety regulated: Two project workers can attempt the same file/resource, depend cyclically or send conflicting answers.
- Decisive decision or feedback right: A coordinator would have to identify the specific interference, decide an attenuation and feed a binding resolution to affected operating units.
- Decision owner: Humans can reorder or reassign tasks and workers can exchange requests, but no distinct diagnosed conflict-and-return coordination loop was established.
- Supporting / enforcement mechanisms: Task DAG, per-agent task status, dependency readiness, request threads, worktrees and human reassignment.
- Closure path: Readiness and reassignment change workflow assignments, but the inspected first-party routes do not verify that a concrete inter-S1 conflict was detected and attenuated as a separately owned S2 decision.
- Why this is / is not agent-owned: General dependency scheduling, human priority or Git merge conflict refusal alone does not prove S2 conflict/oscillation attenuation between S1s.
- Evidence: [DAG and human actor invariants](https://github.com/open-orcha/orcha/blob/1ad8ce3bbce2c21bc916509e805c893e16d24c3d/README.md#L226-L257), [human hold/release](https://github.com/open-orcha/orcha/blob/1ad8ce3bbce2c21bc916509e805c893e16d24c3d/orcha-cli/orcha_cli/templates/portal/portal_backend/task_dispatch_routes.py#L19-L112), [reassignments](https://github.com/open-orcha/orcha/blob/1ad8ce3bbce2c21bc916509e805c893e16d24c3d/orcha-cli/orcha_cli/templates/portal/portal_backend/task_dispatch_routes.py#L113-L190)
- Basis: structural
- Confidence: medium
- Caveats: A task-specific composed human protocol might implement S2, but source inspection cannot award that for generic task-graph edges.

### Absence scope
- Surfaces inspected: Task readiness, assignments, worktree lifecycle, question/request/agent exchange, plan and decision paths.
- Plausible first-party paths checked: Searched for actual simultaneous conflicting worker obligations, an inter-worker conflict discriminator, manager arbitration and subsequent feedback to both workers; found generic workflow and human authority.
- Why no material first-party path remains: General dependency scheduling, human priority or Git merge conflict refusal alone does not prove S2 conflict/oscillation attenuation between S1s.

## S3 — Inside-and-now control
- State: P
- Function: Human manager controls current shared task/agent portfolio, holds unfinished work and reassigns authority.
- Disturbance / variety regulated: Pending or active obligations, unreviewed work and changing current project priorities that demand a new dispatch decision.
- Decisive decision or feedback right: Choose which ready task to hold/release, reassign active work, accept/reject completed tasks, and pause/resume project work.
- Decision owner: Registered project human, enforced by `require_kind(..., human)` and authenticated project identity.
- Supporting / enforcement mechanisms: Local project dashboard/agent snapshot, task readiness and assignment endpoints, status events, signed actor identity and notifier wake service.
- Closure path: Project state displays pending/active tasks; human chooses hold/reassign/verification; DB status updates and events notify affected workers, changing their future claims and work.
- Boundary reachability: Local `orcha init` and portal plus shipped CLI/skill commands implement the task and management APIs; not dependent on external company SaaS.
- Whole-system current view: Per-project task graph and agent status snapshot expose live assignments and outstanding requests across agent instances.
- Current-control decision scope: Human may change runnable task readiness, remove/reassign assignees, and approve/reject completed task work affecting future work readiness.
- Why this is / is not agent-owned: The manager's portfolio choice is explicitly human. Automated status propagation enforces it and does not give autonomous S3.
- Evidence: [current shared state and human role](https://github.com/open-orcha/orcha/blob/1ad8ce3bbce2c21bc916509e805c893e16d24c3d/README.md#L187-L258), [hold/release with worker event](https://github.com/open-orcha/orcha/blob/1ad8ce3bbce2c21bc916509e805c893e16d24c3d/orcha-cli/orcha_cli/templates/portal/portal_backend/task_dispatch_routes.py#L19-L112), [human authorized task reassignment](https://github.com/open-orcha/orcha/blob/1ad8ce3bbce2c21bc916509e805c893e16d24c3d/orcha-cli/orcha_cli/templates/portal/portal_backend/task_dispatch_routes.py#L113-L190), [final verification](https://github.com/open-orcha/orcha/blob/1ad8ce3bbce2c21bc916509e805c893e16d24c3d/orcha-cli/orcha_cli/templates/portal/portal_backend/task_verification_routes.py#L36-L82).
- Basis: structural
- Confidence: high
- Caveats: This P ownership is confined to an attended project with a human authority configured; automated status flip is deterministic support.

## S3* — Complementary audit
- State: A
- Function: Independent AI manager may inspect a worker's completion against the task's definition of done and send the work back before final human verification.
- Disturbance / variety regulated: Worker may claim completion without fulfilling deliverables, code quality or required project evidence.
- Decisive decision or feedback right: Configured distinct manager agent decides `approve`, `send_back` or `comment`; a `send_back` changes the task to in_progress and notifies the original worker, while a recommendation to approve still waits for a human.
- Decision owner: A separate configured AI manager who receives routed work and produces an independent model pre-review judgment; human is final completion authority.
- Supporting / enforcement mechanisms: Review routing selection, durable manager review record, task's submitted work/DoD, request/agent messages and human verification gate.
- Closure path: `needs_verification` triggers manager-review routing; manager receives review request, checks claimed work and records verdict; send-back reopens original worker's task with reasons, while approval proceeds to human final gate. Returned event is visible in task/agent state.
- Boundary reachability: Installed portal supports human setup of review-routing and optional `ai_manager_prereview`; separate registered manager acts through first-party request/review endpoints in ordinary project mode.
- Claim being audited: Whether the original task's finished result warrants advancement versus further work under the DoD.
- Ordinary reporting path: Original coding agent's `/orcha-done` evidence and result summary, stored in the task thread.
- Complementary access path: Manager receives task/DoD and result via a distinct, task-directed review request and can examine available project evidence before returning a verdict.
- Independence boundary: Reviewer is distinct from the original tasked agent and cannot finalize its own reviewed task; human final verification is an additional legitimate parent gate.
- Who acts on findings: First-party review routing applies manager `send_back`, returns the task to original assignee and emits the reasons; on approval the human still independently verifies.
- Why this is / is not agent-owned: The separate model-backed AI manager chooses substantive feedback; deterministic router merely delivers and applies it.
- Evidence: [AI manager review is distinct and recommends only](https://github.com/open-orcha/orcha/blob/1ad8ce3bbce2c21bc916509e805c893e16d24c3d/orcha-cli/orcha_cli/templates/portal/portal_backend/review_routing_routes.py#L1-L16), [manager request and send-back disposition](https://github.com/open-orcha/orcha/blob/1ad8ce3bbce2c21bc916509e805c893e16d24c3d/orcha-cli/orcha_cli/templates/portal/portal_backend/review_routing.py#L360-L465), [manager review endpoint](https://github.com/open-orcha/orcha/blob/1ad8ce3bbce2c21bc916509e805c893e16d24c3d/orcha-cli/orcha_cli/templates/portal/portal_backend/review_routing_routes.py#L104-L136), [human final verification gate](https://github.com/open-orcha/orcha/blob/1ad8ce3bbce2c21bc916509e805c893e16d24c3d/orcha-cli/orcha_cli/templates/portal/portal_backend/task_verification_routes.py#L36-L82).
- Basis: structural
- Confidence: medium
- Caveats: Optional configured first-party mode. Human-only final verification exists without the AI manager but does not by itself justify autonomous A; claim excludes unconfigured separate review and developer tests.

## S4 — Outside-and-then intelligence
- State: —
- Function: No distinct first-party owner established for sensing external future shifts and translating them into a durable strategic system adaptation.
- Disturbance / variety regulated: Future external products, stakeholder requirements or model platforms could change the project's optimal capability portfolio.
- Decisive decision or feedback right: S4 would need external prospective sensing, a choice among future adaptations and an authoritative return to current work capabilities.
- Decision owner: Human can amend project objective; model agents can respond to work instructions, but no distinct outside-future intelligence loop is provided by default.
- Supporting / enforcement mechanisms: Model wake triage, budget and routine metrics, project objective updates and worktree history.
- Closure path: Objective/priority edits can affect future tasks but not as an evidenced independently owned external prospective adaptation function.
- Why this is / is not agent-owned: A new user objective is not by itself evidence of an environment-derived future strategic adaptation owner.
- Evidence: [project objective update](https://github.com/open-orcha/orcha/blob/1ad8ce3bbce2c21bc916509e805c893e16d24c3d/orcha-cli/orcha_cli/templates/portal/portal_backend/container_control_routes.py#L129-L180), [current task/work routines](https://github.com/open-orcha/orcha/blob/1ad8ce3bbce2c21bc916509e805c893e16d24c3d/README.md#L187-L257), [wake triage](https://github.com/open-orcha/orcha/blob/1ad8ce3bbce2c21bc916509e805c893e16d24c3d/orcha-cli/orcha_cli/llm_decisions.py#L1-L90)
- Basis: structural
- Confidence: medium
- Caveats: A separate human strategy organization may exist but is beyond the installed project orchestration boundary.

### Absence scope
- Surfaces inspected: Container objective updates, routine/worker status, planning and task history, notifications, external model configuration.
- Plausible first-party paths checked: Looked for external future evidence, forecast distinction, option selection and returned organization-capability change; only task/current-management pathways were established.
- Why no material first-party path remains: A new user objective is not by itself evidence of an environment-derived future strategic adaptation owner.

## S5 — Policy and identity
- State: P
- Function: Registered human retains ultimate project objective and final task verification policy, governing whether work fulfills the collective project mandate.
- Disturbance / variety regulated: Agent-suggested work, pending validation and autonomous task decisions may conflict with the project's stated objective or acceptable completion conditions.
- Decisive decision or feedback right: Human can revise/clear the project objective, decide high-level plans, approve/refuse final completion and pause/stop the work organization; AI workers cannot self-certify.
- Decision owner: Registered `kind=human` project authority, not an autonomous policy agent.
- Supporting / enforcement mechanisms: Project objective endpoint, root objective node, human-only final verification, plan-approval decision route and identity checks, container control.
- Closure path: Human changes the authoritative project objective or plan approval; the update is audited and appears as the goal-chain objective for subsequent tasks. Worker's submitted final output stays pending until human verification changes task status and unblocks successors.
- Boundary reachability: Project bootstrap creates a real human and objective; installed HTTP routes check human authority and project membership, maintain durable objective and apply decisions to current/future task operations.
- Identity / ultimate-policy issue: Who defines the project objective, which proposed plans may operate, and what counts as accepted task completion when worker self-certification is prohibited.
- Ultimate authority in each claimed mode: Registered human project authority, explicitly separated from AI workers in the DB and API.
- Return-to-operation path: Changed objective becomes the task goal-chain root and human final verification updates/unblocks the shared task graph, or refusal returns active work.
- Why this is / is not agent-owned: These are legitimate human decisions at the project recursion. The code prevents agents from assuming ultimate human authority.
- Evidence: [bootstrapped human/identity invariants](https://github.com/open-orcha/orcha/blob/1ad8ce3bbce2c21bc916509e805c893e16d24c3d/README.md#L187-L257), [objective update and audit](https://github.com/open-orcha/orcha/blob/1ad8ce3bbce2c21bc916509e805c893e16d24c3d/orcha-cli/orcha_cli/templates/portal/portal_backend/container_control_routes.py#L129-L180), [human-only plan decision](https://github.com/open-orcha/orcha/blob/1ad8ce3bbce2c21bc916509e805c893e16d24c3d/orcha-cli/orcha_cli/templates/portal/portal_backend/decision_routes.py#L24-L110), [human-only verify](https://github.com/open-orcha/orcha/blob/1ad8ce3bbce2c21bc916509e805c893e16d24c3d/orcha-cli/orcha_cli/templates/portal/portal_backend/task_verification_routes.py#L36-L82).
- Basis: structural
- Confidence: medium
- Caveats: Positive is bounded to project-level human policy/identity/acceptance, not governance of the entire OpenSiro/Orcha OSS enterprise.

## Distributed OSS parent arrangement
No external Orcha maintainers, hosted operation, or model provider support is credited as this project's governance. Legitimate project human sits inside the installed deployment with explicit DB identity and API authorization. The AI manager pre-review cannot override the human final completion gate.

## Self-hosted and non-human modes
Local `orcha init` starts the per-project SQLite service, packages task skills and registers the human actor. Model-backed worker sessions depend on installed supported external Claude/Codex. Separately configured AI manager pre-review can operate in this deployment, but human S3/S5 rights remain human. A pure daemon without model workers is not counted as autonomous S1.

## Recursion
Individual model coding sessions are S1 project work units. Project human and shared status/authorization are current and ultimate parent controls; separate AI manager reviews provide narrow complementary audit. Task graph, worktree separation and peer requests do not alone establish S2 conflict attenuation.

## Variety and escalation
Workers consume task and review decisions, may ask one another questions and notify human; readiness/verification responses change future dispatch. Uncertain event triage wakes workers rather than silently suppressing messages. Human retains final escalation for plans, agent creation and task acceptance.

## Evidence gaps
Pinned public-source review only; no live paid Claude/Codex execution or independently commissioned model/human audit. S1 applies to deployed model-backed workers using bundled skills, not internal foreign coding-agent architecture; S3* A is optional configured distinct manager. Multi-agent conflict-attenuation and an outside-and-future strategic adaptation loop are not demonstrated at this pinned revision.

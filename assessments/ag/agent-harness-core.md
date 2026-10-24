---
harness_id: agent-harness-core
project_name: Agent Harness Core
repository: https://github.com/phenomenoner/agent-harness-core
review_ref: 1e247e064061e4427f4b78e8afd8671e6e7f06f0
reviewed_at: 2026-10-02
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-02
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Agent Harness Core

## Review boundary

- System in focus: one self-hosted Agent Harness Core deployment at task/fan-out recursion: the first-party Rust harness, durable channel/runtime queues, model-backed main-agent turns, worker/subagent execution, exact-lane child/result ownership, watchdog/coordinator-resume machinery, supervisor/runtime controls, skills/memory integration and associated durable receipts at the frozen revision.
- Purpose and identity: operate persistent chat-native autonomous agents and delegated child work with durable queues, exact identity/authority, bounded concurrency, restart-safe continuation, explicit result ownership and auditable operational state while using Codex app-server and configured model providers as execution backends.
- Relevant environment: Telegram/Discord users and administrators, the local harness home/workspace, Codex app-server and model providers, MCP/tool servers, local files and repositories, OS process/scheduler facilities, imported OpenClaw-compatible state, external memory services, and operator-owned configuration/authentication.
- Standard-distribution boundary: the `agent-harness-core` and CLI crates, bundled queue/worker/subagent/coordinator/supervisor/runtime/skills/memory/policy code, generated local runtime state and supported first-party deployment/configuration paths are inside. Codex app-server internals, model-provider inference, MCP server internals, Telegram/Discord infrastructure, host OS scheduler internals, imported third-party memory implementations and user projects remain separate systems and do not donate organizational ownership.
- Credited operating / distribution surfaces: `README.md`; `docs/configuration.md`; `docs/agent-worker-dispatch-strategy.md`; `docs/invariants.md`; `docs/supervisor.md`; `crates/agent-harness-core/src/runtime_pipeline.rs`; `runtime_worker.rs`; `workers.rs`; `worker_coordination.rs`; `worker_result_mailbox.rs`; `worker_resume.rs`; `coordinator_resume.rs`; `child_execution_policy.rs`; `supervision.rs`; `self_improvement.rs`; and related first-party source modules at the frozen revision.
- Adjacent first-party surfaces excluded from ownership: repository-development CI/tests/fixtures as development evidence rather than runtime actors; maintainer/release governance; roadmap-only adaptive-skill phases and design targets; benchmark/replay evidence when not part of the live operational loop; public website/essay material; and organizational functions internal to Codex, model providers, MCP servers or imported external components.
- First-party operating / deployment modes considered: normal interactive channel-agent turns; durable Goal/continuation operation; delegated LLM subagent fan-out with master-owned result continuation; cron/worker/maintenance classes; supervisor compatibility/direct-owner service management where supported; guarded skill-synthesis/self-improvement paths; and operator-owned live-control/authentication/configuration modes.
- Recursion level: one active main-agent task organization including its currently delegated child agents/workers and their first-party coordination/control paths. Individual model-backed turns are lower-recursion S1 cells. Deployment-service supervision is inspected as an adjacent current-control mechanism but is not by itself used to establish task-level S3.
- Reviewed revision: `1e247e064061e4427f4b78e8afd8671e6e7f06f0`.
- Observation date: 2026-10-02.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Agent Harness Core is a Rust operations layer around model-backed agents. Channel ingress is identity-gated and written into durable queues; runtime workers assemble per-agent prompt context, skills and memory, invoke a pinned Codex app-server route, then persist completion, delivery, trace and lifecycle state. Durable Goals and virtual sessions preserve unfinished work across bounded slices, restarts and backend-session rollover. The harness explicitly distinguishes its ownership from the backend: Codex owns in-turn model/tool/session semantics, while the harness owns admission, identity, queueing, execution authority, continuity, delivery and operational receipts.

The worker subsystem provides a second execution plane for cron work, deterministic jobs and delegated LLM subagents. Jobs are persisted before side effects, leased with exact attempt ownership and subject to global, lane, per-group and per-channel concurrency limits. Interactive, cron, worker and maintenance runtime classes are separately bounded so one class cannot consume all runtime capacity. Stale work can be reaped or quarantined, while terminal results remain linked to their exact parent/master ownership.

Delegation has materially stronger semantics than generic fan-out. A master can assign each child an immutable execution policy containing provider/model/reasoning route, tools/sandbox profile, timeout, attempts, cost/token budget, delegation limit and result contract. Child terminal results are written into an exact-owner mailbox. A deterministic watchdog/coordinator path waits for the declared child group, suppresses duplicate or same-lane wakeups, coalesces valid terminal evidence into one typed continuation, and resumes the exact master lane. Child final text does not directly become user-facing output; only the lease-owning resumed master continuation may acknowledge the results and decide the next outward action.

The deployment layer contains extensive deterministic supervision: child-service state, heartbeats, stop intent, restart/backoff, crash-loop breakers, exact generation ownership and guarded live-control tokens. These mechanisms strongly enforce availability and operational safety but are not credited as autonomous S3 decision ownership by themselves. Likewise, the repository contains quality/invariant catalogs, replay suites and rich receipts; those development/observability paths do not create an independent runtime complementary-audit actor.

The skills subsystem can select versioned procedures and can enqueue guarded self-improvement or skill-synthesis jobs after completed turns. Some mature paths can apply changes autonomously through lint/guard/checksum/backup/receipt gates. However the project's own adaptive-skill design states that outcome-linked learning, contextual belief and broad autonomous promotion remain incomplete product direction. The implemented self-improvement path is retrospective task-local procedural mutation rather than a demonstrated outside-and-then environmental intelligence loop.

## Operational model

At the selected recursion, model-backed main and child turns are S1 work cells. They perform open-ended task work through the configured Codex/model route while the first-party harness supplies exact identity, durable authority, persistence, tools/context policy and delivery. Removing the model-backed decision actor leaves deterministic lifecycle machinery but no entity that chooses open-ended task actions.

Multiple S1 cells can coexist across interactive, cron and delegated-worker classes. First-party concurrency/lane/group controls attenuate interference over runtime/provider/local capacity and prevent one noisy class or fan-out group from monopolizing execution. Those decisions are deterministic constructor logic, so the coordination state is limited to `C`.

Within a delegated task organization, the master agent also occupies a higher recursion. It can choose child execution commitments and constraints before dispatch, receives a bounded whole-group status/result projection through watchdog/mailbox continuation, and after exact resume decides how child evidence changes the task's next commitments or final output. That establishes an autonomous S3 loop at the declared master-plus-children task recursion. It is distinct from the deterministic supervisor, queue caps and termination controls.

## S1 — Operations

- State: A
- Function: perform open-ended user/task work through a model-backed agent turn, revise action from tool/environment feedback, and produce or continue an operational result under durable task authority.
- Disturbance / variety regulated: user objectives, repository/workspace state, tool outcomes, model/context limits, external-effect results, provider responses, failures, blockers and other task distinctions that cannot be fully enumerated by the deterministic runtime.
- Decisive decision or feedback right: choose the task-specific reasoning/tool/action response and revise subsequent action from returned model/tool/environment evidence.
- Decision owner: the autonomous model-backed agent actor reached through the shipped Codex app-server runtime path; the external backend performs inference, while the first-party harness makes that actor operationally reachable and binds its turn to exact first-party identity/authority.
- Supporting / enforcement mechanisms: durable ingress/runtime queues; exact lane/session identity; prompt/skill/memory assembly; task/Goal continuity; backend provenance/capability checks; leases; external-effect policy; delivery receipts; cancellation/timeout/cleanup fences.
- Closure path: accepted channel/worker task → exact runtime lease and prompt bundle → first-party Codex runtime invokes the configured model actor → the actor chooses task actions and consumes tool/environment feedback → harness records completion/continuation → result is delivered, parked or durably continued.
- Boundary reachability: the standard runtime directly launches and manages the Codex app-server path and binds model execution into durable first-party queue/identity/session state; no application-authored orchestration layer is required to create the autonomous task actor.
- Why this is / is not agent-owned: deterministic queue, lease, policy and continuity mechanisms would continue to enforce lifecycle constraints if the model actor were removed, but they would not choose the open-ended task response. The operative discretion therefore remains agent-owned.
- Evidence: [`README.md`](https://github.com/phenomenoner/agent-harness-core/blob/1e247e064061e4427f4b78e8afd8671e6e7f06f0/README.md); [`docs/configuration.md`](https://github.com/phenomenoner/agent-harness-core/blob/1e247e064061e4427f4b78e8afd8671e6e7f06f0/docs/configuration.md); [`crates/agent-harness-core/src/runtime_pipeline.rs`](https://github.com/phenomenoner/agent-harness-core/blob/1e247e064061e4427f4b78e8afd8671e6e7f06f0/crates/agent-harness-core/src/runtime_pipeline.rs); [`crates/agent-harness-core/src/codex_runtime.rs`](https://github.com/phenomenoner/agent-harness-core/blob/1e247e064061e4427f4b78e8afd8671e6e7f06f0/crates/agent-harness-core/src/codex_runtime.rs); [`crates/agent-harness-core/src/runtime_worker.rs`](https://github.com/phenomenoner/agent-harness-core/blob/1e247e064061e4427f4b78e8afd8671e6e7f06f0/crates/agent-harness-core/src/runtime_worker.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: Codex and model-provider internals are external. This assessment credits the first-party assembled operating path that places a model actor under exact harness identity/continuity; it does not import organizational functions internal to the provider.

## S2 — Coordination

- State: C
- Function: attenuate interference among concurrently active S1 work cells by class, group, channel and session, preserving bounded capacity and preventing one work population from monopolizing or corrupting another's execution path.
- Disturbance / variety regulated: interactive turns, cron work, delegated child jobs, retries and maintenance can contend for finite runtime/provider/local resources; sibling fan-out can overload one master group; same-session turns can race or reorder.
- Distinct S1 units: separate model-backed interactive turns, cron-agent turns and delegated child-agent jobs, including sibling children belonging to one master fan-out group.
- Inter-S1 disturbance: one busy class/group/channel can consume shared concurrency or provider capacity needed by another; simultaneous same-session work can violate task ordering; uncontrolled fan-out can exceed local/provider limits and destabilize other active cells.
- Attenuating coordination relation: first-party worker/runtime dispatch applies global and lane caps, per-agent/group and per-agent-per-channel limits, separate interactive/cron/worker/maintenance runtime classes, rate leases, same-session serialization and durable pending state when capacity is unavailable.
- Feedback into subsequent S1 behaviour: capacity or ordering denial does not merely emit telemetry: the affected job remains pending/unleased, later scheduler/worker passes retry after capacity changes, and same-session work waits behind the earlier nonterminal item before execution.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the witness is the explicit attenuation of cross-cell capacity/ordering interference between distinct S1 populations. The design names starvation/fan-out/noisy-cron disturbances and changes subsequent execution availability to contain them; it is not inferred from the mere existence of a queue or child delegation.
- Decisive decision or feedback right: determine whether a candidate S1 cell may consume shared execution capacity now, under class/group/channel/session constraints, and retain blocked work for later admissible execution.
- Decision owner: no autonomous coordinating agent owns this right. The first-party dispatch/runtime machinery deterministically evaluates configured limits and exact-lane state.
- Supporting / enforcement mechanisms: SQLite worker leases; runtime-class lanes; global/group/channel/lane concurrency limits; rate leases; session FIFO; retry/backoff; CronRun controls; stale-lease recovery; exact-owner job state.
- Closure path: S1 job is durably submitted → dispatch checks class/group/channel/session/rate capacity → conflicting work is left pending while admissible work leases capacity → completion/release changes capacity → later dispatch admits previously blocked work under the same coordination relation.
- Boundary reachability: the queue, worker and runtime dispatch logic are shipped first-party and used by the standard interactive/cron/subagent paths; users configure limits but do not need to implement the interference-attenuation mechanism.
- Why this is / is not agent-owned: removing all model agents leaves materially the same concurrency/admission decision. The function-specific S2 path is operationally closed by deterministic first-party machinery, so it is `C`, not `A`.
- Evidence: [`docs/agent-worker-dispatch-strategy.md`](https://github.com/phenomenoner/agent-harness-core/blob/1e247e064061e4427f4b78e8afd8671e6e7f06f0/docs/agent-worker-dispatch-strategy.md); [`docs/configuration.md`](https://github.com/phenomenoner/agent-harness-core/blob/1e247e064061e4427f4b78e8afd8671e6e7f06f0/docs/configuration.md); [`crates/agent-harness-core/src/runtime_queue.rs`](https://github.com/phenomenoner/agent-harness-core/blob/1e247e064061e4427f4b78e8afd8671e6e7f06f0/crates/agent-harness-core/src/runtime_queue.rs); [`crates/agent-harness-core/src/workers.rs`](https://github.com/phenomenoner/agent-harness-core/blob/1e247e064061e4427f4b78e8afd8671e6e7f06f0/crates/agent-harness-core/src/workers.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: this state does not credit generic queueing or shared persistence. It is limited to the implemented anti-interference/capacity relation, and no autonomous agent is shown owning that coordination right.

## S3 — Inside-and-now control

- State: A
- Function: at master-plus-children task recursion, maintain a current whole-group view of delegated work and decide present child commitments, constraints and subsequent task action from the returned group state.
- Disturbance / variety regulated: which child work should run, under which provider/model/tools/sandbox/budget/timeout/delegation constraints, whether failures/partial results/timeouts require different commitments, and how completed delegated evidence changes the current master task.
- Whole-system current view: the master-owned child group has explicit expected child identities; watchdog/group state can wake on completion, failure, timeout, checkpoint or threshold boundaries; terminal results are coalesced into an exact-owner mailbox/continuation with bounded status, failure and artifact evidence for the declared group before the master resumes.
- Current-control decision scope: the master may assign immutable per-child execution policies including provider/model/reasoning route, tool/sandbox profile, timeout, attempts, cost/token budget, delegation limit and result contract, then after resumed group evidence may continue, retry/redelegate, change commitments or produce the authoritative user-facing outcome.
- Decisive decision or feedback right: choose the current allocation/constraints of delegated S1 work and, after receiving whole-group state, choose the task's next commitment or final action.
- Decision owner: the autonomous master agent in the exact parent lane.
- Supporting / enforcement mechanisms: `ChildExecutionPolicy`; durable worker groups; exact master result ownership; bounded/redacted terminal mailbox; coordinator waits; watchdog policies; lane-activity suppression; at-most-once resume intents; exact-lane continuation validation; deterministic quarantine/cleanup.
- Closure path: master decides a fan-out/delegation plan and child execution commitments → first-party workers run independent child S1 cells under those frozen policies → watchdog/mailbox machinery gathers the declared group state without allowing children to publish the parent final → exact coordinator continuation resumes the master → master consumes the returned group evidence and decides the next current task action/output.
- Boundary reachability: master/child policy, worker job ownership, mailbox, watchdog and exact coordinator-resume paths are all shipped first-party and integrated into the standard delegated-worker runtime; the user does not need to supply a separate manager implementation.
- Why this is / is not agent-owned: deterministic machinery owns persistence, safety, exactness and wakeup eligibility, but it does not choose the substantive child policy or what the returned group evidence means for current task commitments. Removing the master agent leaves statuses/mailbox state but no owner for that managerial decision.
- Evidence: [`README.md`](https://github.com/phenomenoner/agent-harness-core/blob/1e247e064061e4427f4b78e8afd8671e6e7f06f0/README.md); [`docs/configuration.md`](https://github.com/phenomenoner/agent-harness-core/blob/1e247e064061e4427f4b78e8afd8671e6e7f06f0/docs/configuration.md); [`docs/agent-worker-dispatch-strategy.md`](https://github.com/phenomenoner/agent-harness-core/blob/1e247e064061e4427f4b78e8afd8671e6e7f06f0/docs/agent-worker-dispatch-strategy.md); [`crates/agent-harness-core/src/child_execution_policy.rs`](https://github.com/phenomenoner/agent-harness-core/blob/1e247e064061e4427f4b78e8afd8671e6e7f06f0/crates/agent-harness-core/src/child_execution_policy.rs); [`crates/agent-harness-core/src/worker_result_mailbox.rs`](https://github.com/phenomenoner/agent-harness-core/blob/1e247e064061e4427f4b78e8afd8671e6e7f06f0/crates/agent-harness-core/src/worker_result_mailbox.rs); [`crates/agent-harness-core/src/worker_coordination.rs`](https://github.com/phenomenoner/agent-harness-core/blob/1e247e064061e4427f4b78e8afd8671e6e7f06f0/crates/agent-harness-core/src/worker_coordination.rs); [`crates/agent-harness-core/src/worker_resume.rs`](https://github.com/phenomenoner/agent-harness-core/blob/1e247e064061e4427f4b78e8afd8671e6e7f06f0/crates/agent-harness-core/src/worker_resume.rs); [`crates/agent-harness-core/src/coordinator_resume.rs`](https://github.com/phenomenoner/agent-harness-core/blob/1e247e064061e4427f4b78e8afd8671e6e7f06f0/crates/agent-harness-core/src/coordinator_resume.rs).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: the positive state is at the declared task/fan-out recursion, not a claim that the deployment supervisor is an autonomous S3 manager for every unrelated agent/session in the host. Supervisor restart/backoff, concurrency caps and stop controls are treated as deterministic enforcement and do not supply the decisive S3 ownership right.

## S3* — Complementary audit

- State: —
- Function: no material first-party independent runtime audit actor/path is established that challenges ordinary S1/S3 claims through a complementary observation channel and returns findings into current control.
- Disturbance / variety regulated: potential mismatch between ordinary model/worker reports and actual task/system state was inspected across receipts, invariants, tests, health/status, result contracts and review evidence.
- Decisive decision or feedback right: none established for an independent complementary auditor at the declared operating recursion.
- Decision owner: none established for S3*.
- Supporting / enforcement mechanisms: append-only receipts; exact result ownership; health/status projections; invariant catalogs; replay/acceptance tests; release review evidence; deterministic result validation/quarantine.
- Closure path: no independent audit finding → master/current-control return path is supplied as a distinct operating function.
- Why this is / is not agent-owned: child results are independently owned and can be quarantined, but they remain the ordinary delegated reporting path into their master. Development tests and release reviews inspect implementation correctness rather than act as a live complementary audit channel over operational claims.
- Evidence: [`README.md`](https://github.com/phenomenoner/agent-harness-core/blob/1e247e064061e4427f4b78e8afd8671e6e7f06f0/README.md); [`docs/invariants.md`](https://github.com/phenomenoner/agent-harness-core/blob/1e247e064061e4427f4b78e8afd8671e6e7f06f0/docs/invariants.md); [`crates/agent-harness-core/src/quality.rs`](https://github.com/phenomenoner/agent-harness-core/blob/1e247e064061e4427f4b78e8afd8671e6e7f06f0/crates/agent-harness-core/src/quality.rs); [`crates/agent-harness-core/src/supervision.rs`](https://github.com/phenomenoner/agent-harness-core/blob/1e247e064061e4427f4b78e8afd8671e6e7f06f0/crates/agent-harness-core/src/supervision.rs).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: an external operator or project can independently audit receipts, and tests provide strong verification evidence, but external/repository-development reviewers do not become a first-party runtime S3* owner.

### Absence scope

- Surfaces inspected: runtime/worker result path; result mailbox and coordinator continuation; health/status/supervision; invariant and schema catalogs; replay/acceptance tests; release/review documentation; external-review evidence handling.
- Plausible first-party paths checked: separate verifier/reviewer agent; supervisor as independent auditor; result-contract validation; health/status process as audit channel; replay/test machinery; operator review of receipts.
- Why no material first-party path remains: every live candidate is either ordinary reporting/control telemetry, deterministic enforcement, or an operator/development verification surface. No distinct autonomous actor with complementary access and a reconstructable finding-to-current-control return loop is established.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party outside-and-then intelligence loop is established that distinguishes external/future change, generates an adaptation option and returns that judgment into present capability/control.
- Disturbance / variety regulated: task-local experience can trigger skill review/synthesis and the runtime can react to current provider/tool/config state, but prospective environmental change and future capability adaptation were checked separately.
- Decisive decision or feedback right: no established actor owns a complete external/future sensing → adaptation judgment → current-capability return loop.
- Decision owner: none established for S4.
- Supporting / enforcement mechanisms: memory recall; model/catalog capability discovery; web-search policy; self-improvement review; skill synthesis/apply/rollback; skill-routing shadow instrumentation; adaptive-skill design documents.
- Closure path: implemented retrospective skill mutation does not establish a complete outside-and-then environmental intelligence closure at this revision.
- Why this is / is not agent-owned: a model may propose or synthesize a reusable procedure after a completed task and guarded machinery may apply it, but the trigger/evidence is task-local retrospective experience rather than a demonstrated first-party future/environmental scanning function. The broader outcome-linked, contextual and autonomously promoted learning loop is explicitly described as incomplete product direction.
- Evidence: [`README.md`](https://github.com/phenomenoner/agent-harness-core/blob/1e247e064061e4427f4b78e8afd8671e6e7f06f0/README.md); [`docs/adaptive-skill-intelligence.md`](https://github.com/phenomenoner/agent-harness-core/blob/1e247e064061e4427f4b78e8afd8671e6e7f06f0/docs/adaptive-skill-intelligence.md); [`crates/agent-harness-core/src/self_improvement.rs`](https://github.com/phenomenoner/agent-harness-core/blob/1e247e064061e4427f4b78e8afd8671e6e7f06f0/crates/agent-harness-core/src/self_improvement.rs); [`crates/agent-harness-core/src/skill_synthesis.rs`](https://github.com/phenomenoner/agent-harness-core/blob/1e247e064061e4427f4b78e8afd8671e6e7f06f0/crates/agent-harness-core/src/skill_synthesis.rs); [`crates/agent-harness-core/src/skill_apply.rs`](https://github.com/phenomenoner/agent-harness-core/blob/1e247e064061e4427f4b78e8afd8671e6e7f06f0/crates/agent-harness-core/src/skill_apply.rs).
- Basis: explicit + structural absence.
- Confidence: medium-high.
- Caveats: the repository is unusually close to an S4 path because guarded skill mutation is already operational. A future revision that closes the declared outcome-linked/future/external evaluation and promotion loop could materially change this state.

### Absence scope

- Surfaces inspected: adaptive-skill design; current skill selection/synthesis/self-improvement/apply; memory; model capability discovery; web-search policy; Goal continuity; roadmap phases and topology explorer.
- Plausible first-party paths checked: autonomous skill learning; external capability discovery as strategic sensing; web search as environment scanning; curator/dream mechanisms; model-catalog adaptation; roadmap-governed learning phases.
- Why no material first-party path remains: the live mutation paths are retrospective/task-local or deterministic capability compatibility mechanisms, while the project's own documents explicitly mark the broader outcome-linked/contextual autonomous learning and promotion system as not fully implemented/enabled. No other credited surface closes the required external + prospective adaptation loop.

## S5 — Policy and identity

- State: —
- Function: no material first-party S5 loop is established that owns the system's identity or ultimate policy at the declared recursion and returns an authoritative identity/policy decision into subsequent operation.
- Disturbance / variety regulated: account/channel identity, allow-lists, backend authentication, execution policy, live-control authority, model/tool/sandbox configuration and per-agent defaults are strongly regulated, but these are operational/admission authorities rather than a demonstrated ultimate organizational identity function.
- Decisive decision or feedback right: no autonomous or parent-governed actor is shown deciding what the whole task organization ultimately is/stands for, resolving an identity/ultimate-policy issue, and returning that decision as the governing policy of subsequent operation.
- Decision owner: none established for S5 at the declared boundary.
- Supporting / enforcement mechanisms: configured agent identities; channel identity binding; administrator allow-lists; operator-owned backend auth; exact live-control tokens; child execution policies; runtime policy; guarded configuration and deployment controls.
- Closure path: no complete identity/ultimate-policy issue → legitimate authority judgment → authoritative return-to-operation loop is supplied.
- Why this is / is not agent-owned: operators configure and authorize many high-impact runtime properties, but configuration existence and permission enforcement are not sufficient S5 ownership. The inspected paths enforce preselected operational policy; they do not establish a first-party constitutional/identity decision loop for the organization itself.
- Evidence: [`README.md`](https://github.com/phenomenoner/agent-harness-core/blob/1e247e064061e4427f4b78e8afd8671e6e7f06f0/README.md); [`docs/configuration.md`](https://github.com/phenomenoner/agent-harness-core/blob/1e247e064061e4427f4b78e8afd8671e6e7f06f0/docs/configuration.md); [`crates/agent-harness-core/src/live_control.rs`](https://github.com/phenomenoner/agent-harness-core/blob/1e247e064061e4427f4b78e8afd8671e6e7f06f0/crates/agent-harness-core/src/live_control.rs); [`crates/agent-harness-core/src/channel_identity.rs`](https://github.com/phenomenoner/agent-harness-core/blob/1e247e064061e4427f4b78e8afd8671e6e7f06f0/crates/agent-harness-core/src/channel_identity.rs); [`crates/agent-harness-core/src/backend_auth.rs`](https://github.com/phenomenoner/agent-harness-core/blob/1e247e064061e4427f4b78e8afd8671e6e7f06f0/crates/agent-harness-core/src/backend_auth.rs).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: this does not deny that a human operator can impose ultimate policy outside the harness. The finding is narrower: the frozen first-party operating boundary does not establish the function-specific parent or autonomous closure required for positive S5 notation.

### Absence scope

- Surfaces inspected: agent/account/channel identity; administrator permissions; backend-auth ownership; runtime/execution policies; model/tool/sandbox configuration; live-control/cutover tokens; supervisor ownership; skills/memory policy; maintainer/release governance as adjacent surface.
- Plausible first-party paths checked: operator configuration as parent S5; administrator allow-list changes; live-control approval; master-agent child-policy authority; self-improvement/meta-policy; repository governance.
- Why no material first-party path remains: each positive-looking path governs a bounded operational capability or deployment action rather than an explicit identity/ultimate-policy issue for the whole organization. Repository maintainers and external operators may exercise broader governance, but no supported first-party return loop at the assessed recursion establishes them as S5=P.

## Distributed OSS parent arrangement

The reviewed repository is open source, but contributor/release governance is outside the runtime organizational boundary. Independent users can run separate deployments with their own configuration and credentials; that does not create one shared organization-level parent function across those deployments. No parent-mode notation is inferred from maintainer review, local operator control or the existence of multiple contributors.

## Self-hosted and non-human modes

Self-hosting materially affects operational authority but does not create additional positive parent states here. Operator configuration, authentication, stop/restart/cutover and deployment controls are strong first-party enforcement surfaces, yet the inspected paths do not close a function-specific parent S3 or S5 loop beyond the autonomous master-agent S3 already established at task recursion. The selected positive S3 state is therefore `A`, not `A(P)`.

## Recursion

The decisive recursion is a main-agent task organization containing its delegated child S1 cells. At lower recursion, each main/child turn is an S1 operation with its own exact lane/session authority. At the selected recursion, first-party fan-out ownership and coordinator resume make the master the S3 actor over the declared child population. The deployment supervisor sits on a different operational axis—service availability and process ownership—and is not substituted for task-level S3. Higher-level user/team/repository governance is outside the assessed operating organization.

## Variety and escalation

Agent Harness Core absorbs large operational variety through durable queues, exact identity, leases, class/group/channel limits, retry/quarantine, restart reconciliation, virtual-session continuity, child execution policies and typed continuation. Variety that cannot be safely closed becomes a typed park, timeout, quarantine, auth defer, approval wait or operator-facing control boundary rather than silent continuation. Delegated child variety returns to the master through bounded exact-owner evidence; the master can then change current commitments or escalate outward. Privileged deployment/auth changes remain operator-controlled and do not donate S5 ownership.

## Evidence gaps

The repository is large and some paths are deliberately split between deterministic Rust state machines and the external Codex/model actor. The assessment therefore credits organizational ownership only where a first-party reachable operating path and closure are explicit. S3=A is bounded to the master-plus-delegated-children recursion; it should be revisited if future releases materially change coordinator authority or make deterministic policy, rather than the master agent, the substantive current-control owner. S4 is the most likely negative state to change: current guarded self-improvement is real, but the broader outside-and-then learning/promotion loop is explicitly incomplete at this revision.
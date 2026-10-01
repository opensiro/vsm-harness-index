---
harness_id: railwarden
project_name: RailWarden
repository: https://github.com/advaith-1212/railwarden
review_ref: 9e63f75baced5b1e246ed2470d59bc092905c1ad
reviewed_at: 2026-10-02
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-02
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C(P)
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# RailWarden

## Review boundary

- System in focus: one self-hosted RailWarden software-delivery factory at the project/task-fleet recursion, including the first-party deterministic controller, durable runtime state, DAG/package scheduler, generated Hermes operating surface, model-backed worker cells, worktree/path-ownership isolation, validation/integration gates, and supported operator CLI controls.
- Purpose and identity: turn an approved software goal into bounded work packages executed by model-backed coding workers while RailWarden preserves source-of-truth task state, dependencies, workspaces, evidence, recovery and integration safety.
- Relevant environment: the target Git repository and worktrees, user/operator, model/provider CLIs, Hermes runtime, architect/provider services, Git and tmux, tests/validation commands, credentials/quotas, and external repository policies.
- Standard-distribution boundary: RailWarden's Python package, generated runtime/config/state, controller, scheduler, worktree/process/provider adapters, validation/integration logic, generated Hermes profile/MCP bridge, and supported CLI/session launch paths are inside. Model-provider inference, Hermes internals beyond RailWarden's generated profile/tool bridge, provider CLIs, host tmux/Git internals, and repository CI/platform policy are separate systems and do not donate ownership unless the first-party RailWarden operating path actually closes the function through them.
- Credited operating / distribution surfaces: `README.md`; `ARCHITECTURE.md`; `docs/architecture.md`; `docs/planning.md`; `docs/runtime-protocol.md`; `src/railwarden/hermes/profile.py`; `src/railwarden/tmux/session.py`; `src/railwarden/runtime/session.py`; `src/railwarden/engine/controller.py`; `src/railwarden/scheduler/*`; `src/railwarden/provisioning/*`; `src/railwarden/validation/*`; `src/railwarden/integration/*`; and current operator/runtime CLI surfaces in `src/railwarden/cli/main.py`.
- Adjacent first-party surfaces excluded from ownership: repository-development CI/tests/fixtures; historical transition/status notes; contributor/release governance; documentation of target behavior not closed by current runtime source; and any independent reasoning, hooks, or control internal to third-party Hermes/model/provider products that RailWarden does not itself invoke as part of the relevant loop.
- First-party operating / deployment modes considered: normal `warden launch` factory session with generated Hermes pane plus model-backed workers; default deterministic `warden controller` supervision; configured Hermes supervision mode where present; manual/self-hosted operator CLI intervention; validation/review/integration paths; and recovery/handoff/provider-swap operation.
- Recursion level: one project-wide factory containing multiple coding-worker S1 cells. RailWarden's controller and local human operator are evaluated as metasystemic control paths over that worker population. A spawned worker itself is not assumed recursively viable merely because it has a model and isolated worktree.
- Reviewed revision: `9e63f75baced5b1e246ed2470d59bc092905c1ad`.
- Observation date: 2026-10-02.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

RailWarden is a Python control kernel for a multi-agent coding factory. Configuration defines project identity, work packages, validation commands, worker-provider priority and concurrency, planning approval and integration behavior. Runtime state tracks tasks, events, processes, results, handoff packets, provider health/quota, session profiles and workflow stages. The controller turns frozen work-package contracts into isolated Git worktrees, writes bounded worker prompts, launches provider-backed coding agents, reconciles process/results, validates package ownership/tests, and serializes integration.

The standard factory launch also generates a Hermes runtime profile with a RailWarden-specific SOUL/SKILL, model configuration and MCP server binding. Hermes is instructed to act as an accountable orchestrator and the launch layout starts it beside workers and the deterministic controller. This makes Hermes a first-party-reachable agent surface. However, the frozen repository's own `warden hermes supervisor` loop does not call the Hermes model: it chooses recovery actions through hard-coded Python rules. No first-party event-to-Hermes-model wake/decision closure was found. The assessment therefore does not infer autonomous S3 from the intended Hermes narrative.

Model-backed workers are first-party-reachable operational actors: RailWarden constructs per-package prompts, scoped worktrees and result contracts, then provider adapters launch them. Their provider/model internals remain external; the credited boundary is RailWarden's assembled operating path that gives those actors bounded operational identity and feeds their results back into durable state.

## Operational model

The factory's S1 population consists of model-backed coding workers operating on separately scoped work packages and worktrees. Each worker absorbs local implementation variety—code choices, debugging, tests and repository details—within frozen ownership and validation constraints. RailWarden itself does not make those semantic implementation choices.

Cross-worker interference is attenuated by dependency readiness, isolated worktrees/branches, owned/forbidden path contracts, bounded concurrency, validation and serialized integration. Those mechanisms close a real S2 relation but are deterministic rather than agent-owned.

Current whole-factory regulation has two supported ownership modes. In the base mode, deterministic controller logic observes task/provider/integration state and changes present execution through provider choice, launch admission, quota pause, handoff/retry/block and serialized merge transitions: this establishes S3 as a first-party constructor. Separately, the self-hosted operator can inspect whole-factory snapshots/events/agents/quotas and issue handoff, retry, provider swap, reject/block, abort-goal and merge-control decisions that are returned into durable task/session state and change later controller behavior. That parent mode supports `C(P)`. The generated Hermes surface is not used to upgrade the base to `A` because autonomous event-driven S3 closure is not established by the frozen implementation.

## S1 — Operations

- State: A
- Function: implement a bounded software work package in a real repository/worktree, using model-driven judgment to choose code changes and react to local test/tool feedback.
- Disturbance / variety regulated: package-specific repository structure, implementation choices, compiler/test failures, code dependencies, tool output and local blockers that cannot be exhaustively selected by RailWarden's deterministic controller.
- Decisive decision or feedback right: choose the semantic implementation actions and revise them in response to repository/tool/test feedback inside the assigned package contract.
- Decision owner: the launched model-backed worker actor selected through the first-party provider adapter/session profile.
- Supporting / enforcement mechanisms: frozen package objective and path ownership, isolated worktree/branch, generated worker prompt, provider adapter/process supervision, result JSON contract, validation, checkpoints and handoff state.
- Closure path: ready package → RailWarden creates/scopes worktree and prompt → model-backed worker performs implementation and tests → worker commits owned changes and returns structured result → RailWarden validates the result and advances, blocks or hands off the package.
- Boundary reachability: `warden launch` constructs worker panes/profiles and the controller directly launches configured provider adapters with RailWarden-generated prompts/workspaces; no application-specific orchestration code must be supplied to create the worker S1 actor.
- Why this is / is not agent-owned: if the worker model actor is removed while RailWarden's scheduler/worktree/validation machinery remains, the machinery can still constrain state but cannot choose the package's open-ended implementation. The operational discretion is therefore agent-owned.
- Evidence: [`src/railwarden/runtime/session.py`](https://github.com/advaith-1212/railwarden/blob/9e63f75baced5b1e246ed2470d59bc092905c1ad/src/railwarden/runtime/session.py); [`src/railwarden/tmux/session.py`](https://github.com/advaith-1212/railwarden/blob/9e63f75baced5b1e246ed2470d59bc092905c1ad/src/railwarden/tmux/session.py); [`src/railwarden/engine/controller.py`](https://github.com/advaith-1212/railwarden/blob/9e63f75baced5b1e246ed2470d59bc092905c1ad/src/railwarden/engine/controller.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: provider/model internals are external. S1 is credited only because the standard first-party runtime directly assembles and launches those model-backed work cells.

## S2 — Coordination

- State: C
- Function: attenuate concrete collision, ordering and integration interference among concurrent coding-worker S1 cells without centralizing their local implementation decisions.
- Disturbance / variety regulated: independent workers can edit overlapping repository surfaces, violate dependency order, exceed available concurrency, or produce branches whose simultaneous integration would collide or destabilize the shared integration branch.
- Distinct S1 units: separate model-backed worker tasks/packages executed through configured Codex, Antigravity, Composer or other supported worker-provider cells.
- Inter-S1 disturbance: cross-package path overlap, dependency races, shared provider/runtime capacity pressure and competing branch integrations can make otherwise valid local worker actions mutually destructive.
- Attenuating coordination relation: dependency/DAG readiness, per-package owned/forbidden path contracts, separate worktrees and branches, worker-concurrency slots, validation of changed files, dependency-safe integration ordering, serialized integration and rollback-on-validation-failure.
- Feedback into subsequent S1 behaviour: dependency/path/capacity/integration outcomes change whether a task is ready, blocked, running, review-passed, merge-ready, merged or retried; blocked work remains unavailable until the regulating condition changes.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the credited mechanisms are tied to explicit cross-worker collision modes—shared repository paths, dependency order and integration contention—and directly constrain later worker admissibility/integration. Mere DAG existence or task delegation is not the basis.
- Decisive decision or feedback right: enforce whether a work cell may start, what repository surface it may own, and when its output may enter the shared integration line under the current cross-cell constraints.
- Decision owner: first-party deterministic RailWarden scheduler/controller/validation/integration machinery; no autonomous coordination actor is established.
- Supporting / enforcement mechanisms: task state, DAG classification, worktree provisioning, path validation, provider eligibility, concurrency slots, integration queue and rollback gates.
- Closure path: multiple package cells become candidates → RailWarden checks dependency/capacity/ownership constraints → only non-conflicting work executes/integrates → validation/integration outcome updates durable state → subsequent cells are admitted, held, repaired or blocked accordingly.
- Boundary reachability: these controls are part of the default controller and package execution/integration path, not optional application code.
- Why this is / is not agent-owned: removing worker/Hermes model actors leaves materially the same coordination decision under configured contracts and current state. The S2 function is therefore constructor-owned, `C`, not `A`.
- Evidence: [`src/railwarden/engine/controller.py`](https://github.com/advaith-1212/railwarden/blob/9e63f75baced5b1e246ed2470d59bc092905c1ad/src/railwarden/engine/controller.py); [`src/railwarden/config/models.py`](https://github.com/advaith-1212/railwarden/blob/9e63f75baced5b1e246ed2470d59bc092905c1ad/src/railwarden/config/models.py); [`.railwarden/project.yaml`](https://github.com/advaith-1212/railwarden/blob/9e63f75baced5b1e246ed2470d59bc092905c1ad/.railwarden/project.yaml); [`src/railwarden/validation/review.py`](https://github.com/advaith-1212/railwarden/blob/9e63f75baced5b1e246ed2470d59bc092905c1ad/src/railwarden/validation/review.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: deterministic serialization and path ownership are credited only because they regulate evidenced inter-S1 disturbances; generic queue/state machinery is not independently counted.

## S3 — Inside-and-now control

- State: C(P)
- Function: regulate the current project-wide worker fleet through a whole-system view of active work, provider availability/quota, execution capacity, failures and integration state, changing present resource/commitment decisions when exceptions arise.
- Disturbance / variety regulated: simultaneous package commitments, provider failures or quota pressure, stalled/failed worker attempts, current capacity saturation, dependency/integration readiness and exceptions that require changing the fleet's present allocation or commitments.
- Whole-system current view: current task records and statuses, active/running count, provider health, per-agent/session state and quota, dependency readiness, worktree/process/result state, decision-required events, and the current integration candidate are all first-party state consumed by controller/operator surfaces.
- Current-control decision scope: admit or hold work, choose/override provider, pause for quota, retry or hand off current commitments, block/reject tasks, swap an active agent/provider, abort a current goal, and serialize/approve integration into the shared branch.
- Decisive decision or feedback right: choose or apply present-fleet resource/commitment changes in response to current whole-system state.
- Decision owner: base mode — deterministic RailWarden controller; parent mode — the legitimate self-hosted human operator using RailWarden's supported whole-system observation and control surfaces.
- Supporting / enforcement mechanisms: durable task/event/process/provider/session state; controller tick/reconciliation; decision-required records; observability/snapshot/status commands; handoff/checkpoint packets; provider swap; task transitions; integration gates.
- Closure path: whole-factory current state/exception is observed → controller rule or operator chooses a permitted current-control response → RailWarden commits the corresponding task/agent/integration transition → later controller ticks and worker admission execute under that returned state.
- Boundary reachability: the deterministic controller is the standard runtime owner, while operator current-control commands and whole-state observation are shipped CLI surfaces over the same durable state. No external management application is required.
- Why this is / is not agent-owned: the frozen `cmd_hermes_supervisor` implementation chooses actions through hard-coded Python conditions and no first-party event-to-Hermes-model wake/decision path was found. The generated Hermes model may advise or interact when a human uses its chat surface, but that does not establish autonomous S3 closure for this revision.
- Evidence: [`src/railwarden/engine/controller.py`](https://github.com/advaith-1212/railwarden/blob/9e63f75baced5b1e246ed2470d59bc092905c1ad/src/railwarden/engine/controller.py); [`src/railwarden/cli/main.py`](https://github.com/advaith-1212/railwarden/blob/9e63f75baced5b1e246ed2470d59bc092905c1ad/src/railwarden/cli/main.py); [`src/railwarden/hermes/profile.py`](https://github.com/advaith-1212/railwarden/blob/9e63f75baced5b1e246ed2470d59bc092905c1ad/src/railwarden/hermes/profile.py); [`docs/runtime-protocol.md`](https://github.com/advaith-1212/railwarden/blob/9e63f75baced5b1e246ed2470d59bc092905c1ad/docs/runtime-protocol.md).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: documentation describes Hermes as the intended reactive brain, but current source does not close that model-driven loop automatically. `C(P)` records the implemented deterministic and parent-governed modes, not the target architecture.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | deterministic RailWarden controller | controller tick over current task/provider/process/integration state or a `decision_required` exception | provider/task/integration transition is committed and governs subsequent scheduling/execution | `engine/controller.py` |
| Parent (`P`) | self-hosted human operator | whole-system status/snapshot/events/agents/quotas or a current exception requiring intervention | supported CLI action such as handoff, retry, swap, block/reject, abort-goal or merge approval mutates durable current-control state consumed by later controller operation | `cli/main.py` |

## S3* — Complementary audit

- State: —
- Function: no material first-party complementary audit path is established that independently challenges ordinary worker/controller claims through a distinct observation channel and returns findings into S3.
- Disturbance / variety regulated: false worker success, path-scope violations, failed tests, invalid results and unsafe integration are strongly checked, but these checks were examined for independence from the ordinary production gate.
- Decisive decision or feedback right: none established for a sufficiently independent complementary auditor.
- Decision owner: none established for S3*.
- Supporting / enforcement mechanisms: structured worker results, package validation, changed-file/path checks, configured reviewer identity, release review, dashboards/events and Git evidence.
- Closure path: no distinct complementary-audit finding loop beyond routine validation/review/integration gating.
- Why this is / is not agent-owned: `run_package_review()` can require a reviewer provider name different from the worker provider, but at this revision it does not invoke that reviewer actor; it mechanically checks validation status and path ownership. The default reviewer role therefore does not by itself establish an independent runtime audit actor.
- Evidence: [`src/railwarden/validation/review.py`](https://github.com/advaith-1212/railwarden/blob/9e63f75baced5b1e246ed2470d59bc092905c1ad/src/railwarden/validation/review.py); [`src/railwarden/runtime/session.py`](https://github.com/advaith-1212/railwarden/blob/9e63f75baced5b1e246ed2470d59bc092905c1ad/src/railwarden/runtime/session.py); [`src/railwarden/engine/controller.py`](https://github.com/advaith-1212/railwarden/blob/9e63f75baced5b1e246ed2470d59bc092905c1ad/src/railwarden/engine/controller.py).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: the anti-self-certification and review gates are strong assurance mechanisms; this negative finding is specifically about the Profile's complementary-access/independence requirement, not about general verification quality.

### Absence scope

- Surfaces inspected: package validation/review, reviewer/validator roles, worker result normalization, release review, controller reconciliation, dashboard/events/observability, Git/path evidence and integration gates.
- Plausible first-party paths checked: configured reviewer agent; reviewer-provider separation; validator role; mechanical validation; raw Git/worktree inspection; release review; operator inspection of events/results.
- Why no material first-party path remains: the implemented review path is part of the routine production gate and does not actually invoke an independent reviewer agent, while operator/development inspection is not wired as a distinct first-party complementary audit loop into current control.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party external-and-prospective intelligence loop is established that develops adaptation options from environmental/future distinctions and returns them into present factory capability.
- Disturbance / variety regulated: provider health/quota, current repository state and current task failures are sensed, while planning and handoff can react to them; these were separated from strategic/prospective adaptation.
- Decisive decision or feedback right: none established for a complete external/future sensing → adaptation option → current-capability return loop.
- Decision owner: none established for S4.
- Supporting / enforcement mechanisms: architect planning, provider health/quota checks, fallback/handoff, update command, context files and Hermes target-design narrative.
- Closure path: no qualifying outside-and-then adaptation closure found at the frozen revision.
- Why this is / is not agent-owned: architect/Hermes planning concerns the current user goal, and provider health/quota recovery concerns current execution. Neither is evidence of an external prospective capability-adaptation function; manual software update likewise does not close S4.
- Evidence: [`docs/planning.md`](https://github.com/advaith-1212/railwarden/blob/9e63f75baced5b1e246ed2470d59bc092905c1ad/docs/planning.md); [`src/railwarden/engine/controller.py`](https://github.com/advaith-1212/railwarden/blob/9e63f75baced5b1e246ed2470d59bc092905c1ad/src/railwarden/engine/controller.py); [`src/railwarden/cli/main.py`](https://github.com/advaith-1212/railwarden/blob/9e63f75baced5b1e246ed2470d59bc092905c1ad/src/railwarden/cli/main.py).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: future first-party autonomous improvement or prospective provider/tool adaptation could change this result; current task planning and reactive recovery do not.

### Absence scope

- Surfaces inspected: planning/architect pipeline, provider health/quota, handoff/fallback, context management, model/session configuration, update command, roadmap/architecture documentation.
- Plausible first-party paths checked: architect as S4; Hermes planning; provider discovery/health as environmental sensing; automatic fallback; `warden update`; contextual repository planning.
- Why no material first-party path remains: every implemented candidate is current-task planning, current operational recovery, compatibility/configuration or operator-triggered software maintenance; none develops prospective adaptation options from an external/future model and feeds them back into present organizational capability.

## S5 — Policy and identity

- State: —
- Function: no material first-party loop is established that owns RailWarden's organizational identity or ultimate policy at the project-factory recursion and returns an authoritative identity/policy judgment into later operation.
- Disturbance / variety regulated: project configuration, plan approval, path ownership, risk/merge policy, credentials, provider/model selection, operator approval and Hermes/worker instructions constrain operation, but these are bounded operational rules.
- Decisive decision or feedback right: no identity/ultimate-policy issue → legitimate authority judgment → authoritative return-to-operation path is established.
- Decision owner: none established for S5 at the declared boundary.
- Supporting / enforcement mechanisms: project/work-package YAML, approval gates, risk/merge flags, generated Hermes instructions, CLI operator controls, provider/model setup and repository safety guidance.
- Closure path: no complete S5 closure established.
- Why this is / is not agent-owned: a human can approve a plan or high-risk merge and can configure the factory, but ordinary plan/merge approval and configuration are not identity-level policy resolution. Hermes's generated SOUL is a prompt/instruction surface, not an ultimate-policy decision loop.
- Evidence: [`.railwarden/project.yaml`](https://github.com/advaith-1212/railwarden/blob/9e63f75baced5b1e246ed2470d59bc092905c1ad/.railwarden/project.yaml); [`src/railwarden/hermes/profile.py`](https://github.com/advaith-1212/railwarden/blob/9e63f75baced5b1e246ed2470d59bc092905c1ad/src/railwarden/hermes/profile.py); [`src/railwarden/cli/main.py`](https://github.com/advaith-1212/railwarden/blob/9e63f75baced5b1e246ed2470d59bc092905c1ad/src/railwarden/cli/main.py); [`docs/safety.md`](https://github.com/advaith-1212/railwarden/blob/9e63f75baced5b1e246ed2470d59bc092905c1ad/docs/safety.md).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: the self-hosted operator is a legitimate parent for current-control S3 decisions, but that does not automatically make every operator action an S5 policy/identity act.

### Absence scope

- Surfaces inspected: project/work-package configuration, planning approval, merge approval, Hermes SOUL/instructions, runtime/session/model configuration, provider credentials/quotas, safety guidance and repository governance as an adjacent surface.
- Plausible first-party paths checked: human plan approval; high-risk merge approval; Hermes identity prompt; project configuration; agent/model/provider swap; repository maintainers.
- Why no material first-party path remains: these paths set or enforce operational constraints and task decisions, but no supported runtime process presents an identity/ultimate-policy issue to a legitimate parent or autonomous S5 actor and returns that decision as the governing identity/policy of subsequent operation.

## Distributed OSS parent arrangement

RailWarden is open-source and can be run independently by many users. That does not create one project-level parent organization across deployments. The parent mode credited in S3 is local to one self-hosted factory: its operator can observe and change current commitments through first-party controls. Repository maintainers/contributors remain an adjacent development-governance system and are not used to infer runtime S3/S5 parent ownership.

## Self-hosted and non-human modes

The standard self-hosted runtime supplies both deterministic controller control and operator intervention. That supports `S3=C(P)` because the two modes independently close the same current-control function. The generated Hermes model surface is first-party reachable, but at this revision no automatic event-to-model supervisor closure was found, so it is not credited as an autonomous S3 mode. Non-human worker cells remain autonomous S1 actors under deterministic S2/S3 constraints.

## Recursion

At the selected recursion the factory is the system in focus and coding workers are its operational S1 cells. They retain meaningful local implementation discretion inside package/path constraints. RailWarden's scheduler/controller supplies cohesion above those cells through S2 and deterministic S3. The operator is a higher local recursion for supported S3 parent interventions. Architect and Hermes roles are not assumed to be recursively viable systems merely because they are separate agents.

## Variety and escalation

Local code variety remains with worker agents. Cross-worker path/dependency/integration variety is attenuated by deterministic S2 controls. Current fleet/provider/quota/failure variety is compressed into task, event, session and provider state for S3. Recoverable exceptions become retry/handoff/normalization/provider-swap decisions; unsafe or unresolved cases can block or ask the operator. Validation failures, quota pressure and process/result anomalies therefore alter durable subsequent operation rather than remaining telemetry-only.

## Evidence gaps

The largest gap is between the documented target architecture and the frozen implementation of Hermes supervision. RailWarden generates and launches a real Hermes model-backed console, but the repository's own continuous `hermes supervisor` command uses deterministic action selection and no first-party event injection into the model chat was found. A future revision that closes that event → Hermes judgment → RailWarden action loop could change S3 from `C(P)` toward an autonomous composite state. Likewise, a reviewer/validator role is modeled, but the frozen production review function does not invoke an independent reviewer agent, so S3* remains absent.

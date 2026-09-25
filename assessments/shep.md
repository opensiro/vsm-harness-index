---
harness_id: shep
project_name: Shep
repository: https://github.com/shep-ai/shep
review_ref: a874b3238fd01ebdbafc11015cccd9a63ed6e2f2
reviewed_at: 2026-09-25
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-25
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C(P)
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: P
---

# Shep

## Review boundary

- System in focus: one first-party Shep installation at pinned revision `a874b3238fd01ebdbafc11015cccd9a63ed6e2f2`, operating a fleet of feature-development agents through isolated git worktrees, the FeatureAgent graph, feature lifecycle/dependency control, fleet-status/triage surfaces and optional collaboration supervisor.
- Purpose and identity: turn feature requests into implementation work, commits, pushes, CI repair and pull requests while coordinating concurrent feature workcells and preserving explicit parent authority over protected supervisory decisions.
- Relevant environment: users/operators, git repositories and branches, GitHub pull requests/CI, external coding-model CLIs/providers, external tools/services, and repository state changed by other feature workcells.
- Standard-distribution boundary: first-party Shep core/runtime, CLI/web surfaces, persistence, feature lifecycle, worktree orchestration, FeatureAgent graph, fleet control plane, collaboration supervisor and first-party project-memory path as wired at the pinned ref. External model/provider implementations, GitHub itself and downstream custom composition remain environment.
- Credited operating / distribution surfaces: FeatureAgent graph and executors; feature dependency/unblock/rebase path; feature-capacity queue; fleet overview/triage/batch approval; collaboration supervisor; approval actor/override logic; standard CI watch/fix loop; project-memory extraction/selection.
- Adjacent first-party surfaces excluded from ownership: repository specs where they are only historical/design material, tests and CI for developing Shep itself, documentation-only proposals, ordinary logs/telemetry, benchmark material and generic configuration surfaces that are not wired into the assessed operating closure.
- First-party operating / deployment modes considered: default prompt-to-PR flow; full requirements/research/plan flow; parallel features in isolated worktrees; dependency-linked features; bounded feature-capacity queue; collaboration supervisor in advisory/cosign/autonomous modes; user approval/override; optional auto-merge and project-memory extraction.
- Recursion level: the assessed organization is the Shep feature-development fleet. Individual feature agents/workcells are operational units inside that fleet; external provider agents are dependencies, not separately credited viable systems at this recursion.
- Reviewed revision: `a874b3238fd01ebdbafc11015cccd9a63ed6e2f2`.
- Observation date: 2026-09-25.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Shep packages an executable coding-agent organization. Its production FeatureAgent graph carries a feature through research/planning, implementation, validation/repair, commit/push, CI handling and pull-request work in an isolated worktree. Model-driven executors make substantive implementation choices; graph and lifecycle code provide deterministic support and enforcement.

Multiple feature workcells may coexist. Dependency-linked work is held until a parent reaches an eligible lifecycle state, then the child is rebased against the updated parent/base before spawning. A separate fleet-capacity service can queue work when the configured concurrency limit is exhausted. These are function-specific interference controls rather than mere topology, but their decisive relation/policy is configured rather than autonomously chosen.

Fleet control is also first-party: the runtime aggregates current fleet health/triage, exposes current approval actions and enforces feature-capacity admission. The circuit breaker is reported as a status signal rather than an autonomous fleet pause. The collaboration supervisor can act at protected gates, but the inspected evidence does not show it consuming the whole-fleet current view and owning fleet-wide resource/commitment decisions.

Routine schema/evidence checks, CI and PR review remain ordinary production assurance and do not establish independent S3*. Current-feature research and post-merge project memory do not establish an outside-and-then S4 loop. Supervision policy does establish an ultimate-authority arrangement: the supervisor may receive delegated gate authority, while the user remains the final authority and cannot be overridden by the supervisor.

Primary evidence:

- [`README.md`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/README.md) — standard feature flow, isolated worktrees, parallel agents, CI repair, gates and merge behavior.
- [`docs/architecture/agent-system.md`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/docs/architecture/agent-system.md) — FeatureAgent graph and implemented collaboration/supervisor architecture.
- [`docs/architecture/supervision.md`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/docs/architecture/supervision.md) — supervisor modes and explicit user-final-authority invariant.
- [`packages/core/src/infrastructure/services/agents/feature-agent/feature-agent-graph.ts`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/packages/core/src/infrastructure/services/agents/feature-agent/feature-agent-graph.ts) — production graph wiring.
- [`packages/core/src/infrastructure/services/agents/feature-agent/nodes/implement.node.ts`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/packages/core/src/infrastructure/services/agents/feature-agent/nodes/implement.node.ts) — model-driven implementation and concurrent task execution.
- [`packages/core/src/application/use-cases/features/check-and-unblock-features.use-case.ts`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/packages/core/src/application/use-cases/features/check-and-unblock-features.use-case.ts) — dependency eligibility, rebase-before-spawn and capacity gating.
- [`specs/041-feature-dependencies/spec.yaml`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/specs/041-feature-dependencies/spec.yaml) — integration-conflict rationale for dependency control.
- [`packages/core/src/application/use-cases/fleet/get-fleet-overview.use-case.ts`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/packages/core/src/application/use-cases/fleet/get-fleet-overview.use-case.ts) — current whole-fleet aggregation and breaker-state calculation.
- [`packages/core/src/application/use-cases/fleet/batch-approve-features.use-case.ts`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/packages/core/src/application/use-cases/fleet/batch-approve-features.use-case.ts) — fleet triage to current-run approval action.
- [`specs/111-fleet-control-plane/UPSTREAM_RFC_PROPOSAL.md`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/specs/111-fleet-control-plane/UPSTREAM_RFC_PROPOSAL.md) — implemented fleet status/triage and breaker-as-signal boundary.
- [`packages/core/src/infrastructure/services/agents/feature-agent/nodes/evidence.node.ts`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/packages/core/src/infrastructure/services/agents/feature-agent/nodes/evidence.node.ts) — routine evidence validation/retry path.
- [`packages/core/src/infrastructure/services/agents/feature-agent/nodes/extract-memory.node.ts`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/packages/core/src/infrastructure/services/agents/feature-agent/nodes/extract-memory.node.ts) — post-merge project-memory distillation.
- [`packages/core/src/infrastructure/services/agents/feature-agent/nodes/research.node.ts`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/packages/core/src/infrastructure/services/agents/feature-agent/nodes/research.node.ts) — current-feature research path.
- [`packages/core/src/application/use-cases/agents/approve-agent-run.use-case.ts`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/packages/core/src/application/use-cases/agents/approve-agent-run.use-case.ts) — actor-aware approval path preserving user precedence.

## Operational model

The operating units are feature workcells: each feature has an isolated worktree and a FeatureAgent execution path that uses model-driven coding executors to decide and perform implementation work. The host runtime owns lifecycle, persistence, worktree isolation, deterministic gates and enforcement. Constructor/operator inputs establish dependency relations and fleet-capacity limits. Fleet overview and triage expose current whole-system state; a local operator can close current approval decisions. Collaboration policy may delegate protected gate decisions to a supervisor, but final authority remains with the user.

## S1 — Operations

- State: A
- Function: transform a feature objective into repository changes and a delivery artifact through a model-driven feature-development loop.
- Disturbance / variety regulated: open-ended feature requests, repository structure, implementation choices, task dependencies, tool/model feedback, validation failures, rejection feedback and CI failures.
- Decisive decision or feedback right: make substantive planning/implementation choices, generate code changes and revise them from validation/CI/rejection feedback.
- Decision owner: the configured coding-agent executor(s) invoked by the first-party FeatureAgent graph.
- Supporting / enforcement mechanisms: isolated git worktrees, graph lifecycle, artifact schemas, retry/repair nodes, git/PR services, CI watch/fix loop and durable feature state.
- Closure path: feature request enters Shep → FeatureAgent creates/uses research and plan artifacts → coding-agent executor implements tasks in the isolated worktree → generated changes and validation/CI/rejection feedback are observed → later agent execution repairs or continues → commit/push/PR/optional merge completes the operating cycle.
- Boundary reachability: the standard CLI/web feature flow invokes the production FeatureAgent graph and executor path at the pinned ref; the model-driven implementation loop is not a test-only or example-only surface.
- Why this is / is not agent-owned: deterministic graph machinery constrains lifecycle and safety, but does not reproduce the substantive implementation decisions without the coding agent; agent judgments directly change repository state and later behavior responds to execution feedback.
- Evidence: [`README.md`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/README.md); [`feature-agent-graph.ts`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/packages/core/src/infrastructure/services/agents/feature-agent/feature-agent-graph.ts); [`implement.node.ts`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/packages/core/src/infrastructure/services/agents/feature-agent/nodes/implement.node.ts).
- Basis: explicit + structural
- Confidence: high
- Caveats: provider/model inference occurs outside the repository boundary, but Shep owns the first-party operational organization that repeatedly invokes those dependencies and applies their decisions to the feature worktree.

## S2 — Coordination

- State: C
- Function: attenuate concrete interference between distinct feature workcells sharing evolving repository state and bounded fleet capacity.
- Disturbance / variety regulated: dependent work starting from stale repository state before prerequisite parent changes are available, branch divergence/integration conflict, and bounded fleet execution capacity.
- Decisive decision or feedback right: establish dependency relations and capacity policy outside the autonomous workcell; the runtime then blocks/queues, waits for a qualifying parent transition, rebases against updated state and only then permits execution when capacity is available.
- Decision owner: constructor/operator-supplied dependency and capacity configuration, enforced by first-party runtime mechanisms.
- Supporting / enforcement mechanisms: parent/child feature metadata, lifecycle-transition hook, dependency eligibility checks, branch rebase service, feature-capacity service and queued-feature draining.
- Closure path: distinct feature workcells share repository/capacity conditions → configured dependency identifies a prerequisite/integration-risk relation → child remains blocked until parent eligibility → Shep rebases child state against parent/base and obtains a capacity slot → child executes against changed repository state rather than stale/conflicting state.
- Boundary reachability: dependency/unblock/rebase and capacity checks are production use cases reached from the feature lifecycle at the pinned ref, not only design documents.
- Distinct S1 units: separate concurrently manageable feature workcells / FeatureAgent runs, each operating on its own feature and isolated git worktree.
- Inter-S1 disturbance: a child feature may otherwise operate from repository state that omits prerequisite parent changes or has diverged from the parent branch, creating integration conflict between related operational workcells.
- Attenuating coordination relation: an explicit parent/child dependency blocks the child until the parent reaches a qualifying lifecycle state; before spawn, Shep rebases the child against the parent/base, with the capacity service separately preventing oversubscription.
- Feedback into subsequent S1 behaviour: parent lifecycle transitions trigger child reevaluation; the child remains blocked/queued when conditions are unmet, or is rebased and then spawned against updated repository state when dependency and capacity conditions are satisfied.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the positive mapping relies on a documented inter-workcell integration disturbance and a disturbance-specific block/rebase/spawn feedback loop; dependency naming or DAG sequencing alone is not used as S2 evidence.
- Why this is / is not agent-owned: the attenuation loop is real and function-specific, but no autonomous coordinator is evidenced as owning the dependency/capacity decision right. Developers/operators construct the coordination relation and the runtime deterministically applies it, so `C` is credited rather than `A`.
- Evidence: [`specs/041-feature-dependencies/spec.yaml`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/specs/041-feature-dependencies/spec.yaml); [`check-and-unblock-features.use-case.ts`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/packages/core/src/application/use-cases/features/check-and-unblock-features.use-case.ts); [`specs/110-max-parallel-features/plan.md`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/specs/110-max-parallel-features/plan.md).
- Basis: explicit + structural
- Confidence: medium-high
- Caveats: the core positive witness is dependency-related integration interference plus block/rebase feedback. Capacity gating is corroborating coordination evidence, not a substitute for the disturbance-specific witness.

## S3 — Inside-and-now control

- State: C(P)
- Function: maintain a current whole-fleet view and expose decisions that can alter present feature commitments/admission, with a base constructor surface and a closed local-parent mode.
- Disturbance / variety regulated: failed or attention-needing features, waiting approval gates, queued work, current concurrency pressure and aggregate failure conditions reported by the fleet breaker evaluator.
- Decisive decision or feedback right: base (`C`) — a composed controller can consume first-party fleet status/triage/current-control primitives and configured admission limits; parent (`P`) — the local operator can inspect fleet triage and approve waiting feature runs while configured limits constrain current admissions.
- Decision owner: base (`C`) — downstream developer/composer of the first-party S3-specific primitives; parent (`P`) — local Shep operator/user.
- Supporting / enforcement mechanisms: fleet overview aggregation, triage items, batch approval use case, current feature lifecycle state, parallel-feature capacity service, persisted run state and breaker-status calculation.
- Closure path: base — current fleet state is aggregated into health/triage and exposed together with current-control action seams, but the autonomous decision owner must be supplied by composition. Parent — operator inspects current fleet/triage state → invokes current approval/control → affected feature runs resume or remain governed by current capacity/lifecycle constraints.
- Boundary reachability: fleet overview/triage/batch approval and feature-capacity enforcement are first-party production surfaces at the pinned ref. The breaker is credited only as a status input because the pinned implementation does not itself pause/reprioritize the fleet.
- Whole-system current view: `GetFleetOverviewUseCase` aggregates feature states into fleet health categories and breaker state; triage exposes current exceptions across the fleet.
- Current-control decision scope: whether waiting current work proceeds and whether current/new feature work receives execution capacity under the fleet concurrency regime.
- Why this is / is not agent-owned: no first-party autonomous actor is evidenced as consuming the whole-fleet view and owning fleet-wide current resource/commitment/priority decisions. The optional supervisor can close individual gates, but that is not evidence of whole-fleet S3 ownership. The operator mode does close parent-governed current control.
- Evidence: [`get-fleet-overview.use-case.ts`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/packages/core/src/application/use-cases/fleet/get-fleet-overview.use-case.ts); [`batch-approve-features.use-case.ts`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/packages/core/src/application/use-cases/fleet/batch-approve-features.use-case.ts); [`UPSTREAM_RFC_PROPOSAL.md`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/specs/111-fleet-control-plane/UPSTREAM_RFC_PROPOSAL.md); [`specs/110-max-parallel-features/plan.md`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/specs/110-max-parallel-features/plan.md).
- Basis: explicit + structural
- Confidence: medium-high
- Caveats: breaker status is not an autonomous intervention, and per-feature supervisor gate closure is not promoted into whole-fleet S3 without a fleet-wide current view/decision path.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | downstream developer/composer using first-party S3-specific fleet-control seams | current fleet status, triage, queue/capacity or breaker signal | fleet view and control primitives are available, but an autonomous fleet-level decision owner must be supplied/composed | [`get-fleet-overview.use-case.ts`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/packages/core/src/application/use-cases/fleet/get-fleet-overview.use-case.ts); [`UPSTREAM_RFC_PROPOSAL.md`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/specs/111-fleet-control-plane/UPSTREAM_RFC_PROPOSAL.md) |
| Parent (`P`) | local operator/user | visible waiting/attention state or current admission policy | operator approval changes waiting feature execution; configured capacity gates present work | [`batch-approve-features.use-case.ts`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/packages/core/src/application/use-cases/fleet/batch-approve-features.use-case.ts); [`specs/110-max-parallel-features/plan.md`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/specs/110-max-parallel-features/plan.md) |

## S3* — Complementary audit

- State: —
- Function: no materially independent complementary-audit function is established at the fleet boundary.
- Disturbance / variety regulated: schema/implementation errors, incomplete evidence and CI failures are detected, but through ordinary production verification paths rather than independent organizational audit.
- Decisive decision or feedback right: validators/evidence/CI paths can reject or request repair, but no separate audit actor with sufficiently independent evidence access is established.
- Decision owner: ordinary feature workflow validators, evidence executor and external CI/user review paths.
- Supporting / enforcement mechanisms: schema validation/repair nodes, evidence node, CI watch/fix loop, PR diff/review and audit/rationale records.
- Closure path: no ordinary S1 reporting path → materially different complementary evidence acquisition → independent audit judgment → corrective return into S3/S1 loop is established.
- Why this is / is not agent-owned: these checks are meaningful assurance mechanisms, but remain coupled to the production feature path or external CI/review. A verifier label, evidence sub-agent or CI result alone does not establish S3* independence.
- Evidence: [`feature-agent-graph.ts`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/packages/core/src/infrastructure/services/agents/feature-agent/feature-agent-graph.ts); [`evidence.node.ts`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/packages/core/src/infrastructure/services/agents/feature-agent/nodes/evidence.node.ts); [`README.md`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/README.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: a downstream deployment could add an independently governed reviewer/evaluator; that would require separate evidence at the resulting system boundary.

### Absence scope

- Surfaces inspected: graph schema validators and repair loops, evidence sub-agent, CI watch/fix loop, PR review, fleet activity/audit records and supervisor rationale/explainability.
- Plausible first-party paths checked: validator as verifier, evidence agent, CI as independent check, user PR review and supervisor decision logging.
- Why no material first-party path remains: the inspected paths are routine workflow checks/records or share the operational path's evidence/control channel; none establishes a distinct complementary access path with independent organizational audit ownership.

## S4 — Outside-and-then intelligence

- State: —
- Function: no fleet-level outside-and-then prospective adaptation loop is established.
- Disturbance / variety regulated: current feature uncertainty and historical project knowledge are processed, but not as prospective external-environment variety translated into an organizational adaptation decision.
- Decisive decision or feedback right: no first-party actor is evidenced as selecting and applying a prospective change to Shep's fleet capability/structure/policy from external/future sensing.
- Decision owner: none established.
- Supporting / enforcement mechanisms: feature research node, planner, adaptive model selection for current tasks, post-merge project-memory extraction/selection and fleet failure/status monitoring.
- Closure path: no external/future distinction → generated organizational adaptation option → selection → changed present fleet capability/S3 operation loop is established.
- Why this is / is not agent-owned: research is scoped to the current feature's implementation choices, while project memory distils internal past experience for later context. Model routing and failure monitoring react to current operation. None closes prospective organizational adaptation at the assessed fleet boundary.
- Evidence: [`research.node.ts`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/packages/core/src/infrastructure/services/agents/feature-agent/nodes/research.node.ts); [`extract-memory.node.ts`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/packages/core/src/infrastructure/services/agents/feature-agent/nodes/extract-memory.node.ts); [`agent-system.md`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/docs/architecture/agent-system.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: persistent memory can support future adaptation, but persistence/retrieval alone is not S4 without an outside/future distinction and returned change to current capability.

### Absence scope

- Surfaces inspected: current-feature research/planning, project-memory extraction and selection, adaptive model routing, fleet control/breaker status, supervisor policy and settings/configuration.
- Plausible first-party paths checked: technical research, durable project memory, automatic model selection, fleet failure monitoring and supervisor recommendations.
- Why no material first-party path remains: the inspected paths address current task execution, internal historical context, reactive operating conditions or externally configured policy; no first-party path models prospective environmental change and returns a selected organizational adaptation into fleet capability/control.

## S5 — Policy and identity

- State: P
- Function: govern the ultimate authority arrangement under which delegated supervisor decisions may affect protected feature operation.
- Disturbance / variety regulated: conflict between delegated supervisor authority and the parent user's legitimate final authority over protected decisions/gates.
- Decisive decision or feedback right: determine and retain final authority when supervisor policy would otherwise allow advisory, cosign or autonomous gate action; a prior/final user decision cannot be overridden by the supervisor.
- Decision owner: local parent user/operator.
- Supporting / enforcement mechanisms: `SupervisorPolicy` autonomy modes, collaboration policy configuration, approval actor identity, prior-user-decision check, audit rationale and gate lifecycle.
- Closure path: parent configures supervisor authority → supervisor may advise/cosign/act within that delegation → protected decision reaches approval path → user precedence is enforced → feature operation resumes, remains held or changes course under the authoritative result.
- Boundary reachability: supervision modes and user-final-authority are first-party collaboration behavior, while `ApproveAgentRunUseCase` enforces actor-aware user precedence in the production approval path at the pinned ref.
- Identity / ultimate-policy issue: how much final organizational decision authority may be delegated from the user/operator to the collaboration supervisor over protected gates and decisions.
- Ultimate authority in each claimed mode: the only claimed positive mode is parent-governed `P`; the user/operator is ultimate authority. The supervisor may advise, cosign or act autonomously within delegated scope, but cannot override a prior/final user decision.
- Return-to-operation path: configured `SupervisorPolicy` determines allowed supervisor behavior → supervisor/user gate decisions enter the actor-aware approval path → user precedence is enforced and the authoritative decision is recorded → the affected feature run proceeds, remains held or is redirected under that decision.
- Why this is / is not agent-owned: delegated supervisor autonomy does not become ultimate policy ownership because the repository explicitly preserves user final authority. The positive witness is the authority regime itself, not routine merge approval or prompt/config editing.
- Evidence: [`docs/architecture/supervision.md`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/docs/architecture/supervision.md); [`approve-agent-run.use-case.ts`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/packages/core/src/application/use-cases/agents/approve-agent-run.use-case.ts).
- Basis: explicit + structural
- Confidence: high
- Caveats: ordinary user approval of a feature would not by itself establish S5; the positive mapping depends on the explicit higher-level delegation/override contract defining ultimate authority.

## Recursion

The assessment treats the Shep fleet as the system-in-focus and feature workcells as S1 units at that recursion. A feature workcell may contain multiple internal model calls or implementation tasks, but that does not automatically establish another complete viable recursion. External coding-agent providers/CLIs supply inference capabilities and remain environmental dependencies for this assessment.

## Variety and escalation

- Worktree isolation, dependency gating/rebase, schema validation/repair, bounded retries and fleet-capacity queueing attenuate operational variety before it destabilizes other workcells.
- Parallel feature agents, concurrent implementation tasks, model routing, CI repair, fleet triage and optional supervisor intervention amplify regulator capacity.
- Failed/exhausted feature runs become blocked/failed attention states; approval gates and supervisor questions can escalate to the user; supervisor failures preserve the parent path; fleet triage aggregates current exceptions.
- The fleet breaker condition is not credited as autonomous S3 intervention because the pinned implementation reports the state rather than automatically pausing/reprioritizing the fleet.

## Evidence gaps

- No first-party autonomous actor was found that consumes the whole-fleet current view and owns fleet-wide resource/commitment/priority decisions; this keeps S3 at `C(P)` rather than `A`/`A(P)`.
- No materially independent complementary access/audit path was found beyond routine validation, evidence, CI and review; S3* remains `—`.
- No outside/future sensing → generated adaptation option → returned current-capability change loop was found at the fleet boundary; S4 remains `—`.
- S2 is supported by the concrete dependency integration-conflict/rebase loop; evidence does not establish autonomous ownership of that coordination decision, so the state remains `C`.

## Assessment summary

Shep establishes autonomous coding operations (`S1=A`) and a concrete constructor-owned coordination path for dependency/integration interference (`S2=C`). Its fleet overview, triage, approvals and concurrency controls establish current-control constructor and parent modes (`S3=C(P)`), but no first-party autonomous whole-fleet controller is evidenced. Routine validation/evidence/CI paths do not establish independent complementary audit (`S3*=—`), and current-task research plus internal project memory do not close prospective fleet adaptation (`S4=—`). The collaboration subsystem explicitly preserves the user's ultimate authority over delegated supervisor action, establishing parent-governed S5 (`S5=P`).

Proposed canonical vector: `S1=A / S2=C / S3=C(P) / S3*=— / S4=— / S5=P`.

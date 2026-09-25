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
status: proposed
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
- Purpose and identity: turn feature requests into implementation work, commits, pushes, CI repair and pull requests while coordinating multiple concurrent feature workcells and preserving explicit operator authority over protected approval/policy decisions.
- Relevant environment: users/operators, git repositories and branches, GitHub pull requests/CI, external coding-model CLIs/providers, external tools/services, and repository state changed by other feature workcells.
- Standard-distribution boundary: first-party Shep core/runtime, CLI/web surfaces, persistence, feature lifecycle, worktree orchestration, FeatureAgent graph, fleet control plane, collaboration supervisor and first-party project-memory path as wired at the pinned ref. External model/provider implementations, GitHub itself and downstream custom composition remain environment.
- Credited operating / distribution surfaces: FeatureAgent graph and executors; feature dependency/unblock/rebase path; feature-capacity queue; fleet overview/triage/batch approval; optional collaboration supervisor; approval actor/override logic; standard CI watch/fix loop; project-memory extraction/selection.
- Adjacent first-party surfaces excluded from ownership unless operationally wired: repository specs as historical/design evidence, tests/CI for Shep itself, documentation-only proposals, ordinary logs/telemetry, and generic configuration surfaces.
- First-party operating / deployment modes considered: default prompt-to-PR flow; full requirements/research/plan flow; parallel features in isolated worktrees; dependency-linked features; bounded feature-capacity queue; optional collaboration supervisor in advisory/cosign/autonomous modes; user approval/override; optional auto-merge and project-memory extraction.
- Recursion level: the assessed organization is the Shep feature-development fleet. Individual feature agents/workcells are operational units inside that fleet; external provider agents are dependencies, not separate credited VSM systems at this recursion.
- Reviewed revision: `a874b3238fd01ebdbafc11015cccd9a63ed6e2f2`.
- Observation date: 2026-09-25.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Shep packages an executable coding-agent organization rather than a thin provider wrapper. The public runtime creates isolated feature worktrees, invokes a model-driven FeatureAgent graph and carries a feature through requirements/research/plan/implementation, commit/push, CI repair and pull-request stages. The implementation node can execute task phases through coding-agent executors, including concurrent work inside a phase, and feedback from generated artifacts, validation, rejection or CI failure returns into later execution. This establishes a first-party autonomous S1 operating loop around feature delivery.

At fleet level, multiple feature workcells are allowed to coexist and can depend on one another. The dependency path is more than graph topology: Shep explicitly treats a child feature as unsafe to start before the parent reaches an eligible lifecycle state, then rebases the child's branch against the parent/base before spawning so the dependent workcell sees the prerequisite repository state. The capacity service independently gates feature spawning when the configured fleet concurrency is full. These mechanisms attenuate concrete integration/resource interference, but the decisive dependency relation and capacity policy are supplied through first-party constructor/configuration surfaces rather than chosen by an autonomous coordination actor. That supports S2=C, not S2=A.

Shep also has a real fleet-control surface. `GetFleetOverviewUseCase` aggregates current feature health into fleet statuses and reports a circuit-breaker condition; fleet triage and batch-approval actions can change live feature runs, while the shared parallel-feature limit gates current admission. However the circuit breaker is currently a reported signal rather than an automatic fleet intervention, and the optional collaboration supervisor acts around feature/gate events rather than consuming the evidenced whole-fleet control view to own current fleet commitments/resources/priorities. The base fleet-control path therefore exposes function-specific constructor primitives, while the local operator has a legitimate closed parent-control mode. This supports S3=C(P).

Routine verification does not establish S3*. Feature schema validation/repair, the evidence node, CI watch/fix and PR review are all ordinary production assurance paths coupled to the feature workflow. No materially independent complementary-access path was found that acquires evidence outside ordinary reporting, makes an independent audit judgment and returns that judgment into S3/S1 control.

The repository contains substantial research/planning and memory mechanisms, but they do not close S4 at the fleet boundary. Feature research is current-task technical research, and post-merge project-memory extraction distils internal historical knowledge for later features. Neither path establishes an outside-and-then prospective environment model that generates adaptation options and returns a selected change into current fleet capability/control.

Finally, Shep explicitly implements an ultimate-authority arrangement for delegated supervision. Collaboration policy can place the supervisor in advisory, cosign or autonomous gate mode, but the architecture states that the user always wins; approval code prevents a supervisor decision from overriding a prior user decision and allows the user to override prior supervisor action. This is not merely a routine merge approval: it is the authority regime governing how much organizational decision power may be delegated to the supervisor. Ultimate policy ownership therefore remains parent-governed, supporting S5=P.

Primary evidence:

- [`README.md`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/README.md) — standard prompt-to-PR/full-spec flows, isolated worktrees, parallel agents, CI repair, approval gates and optional merge behavior.
- [`docs/architecture/agent-system.md`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/docs/architecture/agent-system.md) — FeatureAgent graph, implemented supervisor graph, background execution, lifecycle and supporting agent architecture.
- [`docs/architecture/supervision.md`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/docs/architecture/supervision.md) — collaboration message bus, supervisor modes and explicit user-final-authority invariant.
- [`packages/core/src/infrastructure/services/agents/feature-agent/feature-agent-graph.ts`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/packages/core/src/infrastructure/services/agents/feature-agent/feature-agent-graph.ts) — production graph wiring for research/plan/implement/validation/repair/merge/memory paths.
- [`packages/core/src/infrastructure/services/agents/feature-agent/nodes/implement.node.ts`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/packages/core/src/infrastructure/services/agents/feature-agent/nodes/implement.node.ts) — model-driven task/phase execution and concurrent implementation work.
- [`packages/core/src/application/use-cases/features/check-and-unblock-features.use-case.ts`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/packages/core/src/application/use-cases/features/check-and-unblock-features.use-case.ts) — dependency eligibility, rebase-before-spawn and capacity gating for dependent work.
- [`specs/041-feature-dependencies/spec.yaml`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/specs/041-feature-dependencies/spec.yaml) — explicit integration-conflict rationale for dependency blocking/unblocking.
- [`packages/core/src/application/use-cases/fleet/get-fleet-overview.use-case.ts`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/packages/core/src/application/use-cases/fleet/get-fleet-overview.use-case.ts) — current fleet aggregation and circuit-breaker status evaluation.
- [`packages/core/src/application/use-cases/fleet/batch-approve-features.use-case.ts`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/packages/core/src/application/use-cases/fleet/batch-approve-features.use-case.ts) — fleet triage-to-current-run approval action.
- [`specs/111-fleet-control-plane/UPSTREAM_RFC_PROPOSAL.md`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/specs/111-fleet-control-plane/UPSTREAM_RFC_PROPOSAL.md) — implemented fleet status/triage and explicit distinction that circuit-breaker evaluation is a reported status signal rather than an autonomous pause.
- [`packages/core/src/infrastructure/services/agents/feature-agent/nodes/evidence.node.ts`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/packages/core/src/infrastructure/services/agents/feature-agent/nodes/evidence.node.ts) — ordinary evidence-completeness validation/retry path inspected for S3*.
- [`packages/core/src/infrastructure/services/agents/feature-agent/nodes/extract-memory.node.ts`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/packages/core/src/infrastructure/services/agents/feature-agent/nodes/extract-memory.node.ts) — post-merge project-memory distillation inspected for S4.
- [`packages/core/src/infrastructure/services/agents/feature-agent/nodes/research.node.ts`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/packages/core/src/infrastructure/services/agents/feature-agent/nodes/research.node.ts) — current-feature research path inspected for S4.
- [`packages/core/src/application/use-cases/agents/approve-agent-run.use-case.ts`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/packages/core/src/application/use-cases/agents/approve-agent-run.use-case.ts) — actor-aware approval path preserving prior user decisions over supervisor actions.

## S1 — Operations

- State: A
- Function: transform a feature objective into repository changes and a delivery artifact through a model-driven feature-development loop.
- Disturbance / variety regulated: open-ended feature requests, repository structure, implementation choices, task dependencies, tool/model feedback, validation failures, rejection feedback and CI failures.
- Decisive decision or feedback right: make substantive planning/implementation choices, generate code changes and revise them from validation/CI/rejection feedback.
- Decision owner: the configured coding-agent executor(s) invoked by the first-party FeatureAgent graph.
- Supporting / enforcement mechanisms: isolated git worktrees, graph lifecycle, artifact schemas, retry/repair nodes, git/PR services, CI watch/fix loop and durable feature state.
- Closure path: feature request enters Shep → FeatureAgent creates/uses research and plan artifacts → coding-agent executor implements tasks in the isolated worktree → generated changes and validation/CI/rejection feedback are observed → subsequent agent execution repairs or continues → commit/push/PR/optional merge completes the operating cycle.
- Boundary reachability: the standard CLI/web feature flow invokes the production FeatureAgent graph and executor path at the pinned ref; the model-driven implementation loop is not a test-only or example-only surface.
- Why this is / is not agent-owned: deterministic graph machinery constrains lifecycle and safety, but it does not reproduce the substantive implementation decisions without the coding agent; the agent's judgments directly change repository state and later behavior responds to execution feedback.
- Evidence: [`README.md`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/README.md); [`docs/architecture/agent-system.md`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/docs/architecture/agent-system.md); [`packages/core/src/infrastructure/services/agents/feature-agent/feature-agent-graph.ts`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/packages/core/src/infrastructure/services/agents/feature-agent/feature-agent-graph.ts); [`packages/core/src/infrastructure/services/agents/feature-agent/nodes/implement.node.ts`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/packages/core/src/infrastructure/services/agents/feature-agent/nodes/implement.node.ts).
- Basis: explicit + structural
- Confidence: high
- Caveats: provider/model inference occurs outside the repository boundary, but Shep owns the first-party operational organization that repeatedly invokes those dependencies and applies their decisions to the feature worktree.

## S2 — Coordination

- State: C
- Function: attenuate concrete interference between distinct feature workcells that share evolving repository state and bounded fleet capacity.
- Disturbance / variety regulated: a dependent child starting before prerequisite parent changes are available, branch divergence/integration conflict between related feature work and oversubscription of the configured parallel-feature capacity.
- Decisive decision or feedback right: determine dependency relations and configured capacity outside the autonomous workcell; the runtime then blocks/queues a child, waits for an eligible parent transition, rebases the child against the updated parent/base and only then spawns it when capacity is available.
- Decision owner: constructor/operator-supplied dependency and capacity configuration, enforced by first-party runtime mechanisms.
- Supporting / enforcement mechanisms: parent/child feature metadata, lifecycle-transition hook, dependency eligibility checks, branch rebase service, feature-capacity service and queued-feature draining.
- Closure path: distinct feature workcells share repository/capacity conditions → configured dependency identifies an integration-risk relation → child remains blocked until the parent reaches the qualifying lifecycle state → Shep rebases child state against the parent/base and separately obtains a capacity slot → the child is spawned with changed repository state rather than proceeding under stale/conflicting conditions.
- Boundary reachability: the dependency/unblock/rebase and capacity checks are production use cases called from the feature lifecycle at the pinned ref, not merely documented design proposals.
- Why this is / is not agent-owned: the attenuation loop is real and function-specific, but no autonomous coordinator is evidenced as owning the dependency/capacity decision right. Developers/operators construct the coordination relation and the runtime deterministically applies it, so `C` is credited rather than `A`.
- Evidence: [`specs/041-feature-dependencies/spec.yaml`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/specs/041-feature-dependencies/spec.yaml); [`packages/core/src/application/use-cases/features/check-and-unblock-features.use-case.ts`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/packages/core/src/application/use-cases/features/check-and-unblock-features.use-case.ts); [`specs/110-max-parallel-features/plan.md`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/specs/110-max-parallel-features/plan.md).
- Basis: explicit + structural
- Confidence: medium-high
- Caveats: generic DAG/dependency/routing topology is not being credited by itself. The positive mapping is specifically the documented integration-conflict disturbance plus block/rebase/spawn feedback path, with the separate capacity gate reinforcing current inter-workcell resource coordination.

## S3 — Inside-and-now control

- State: C(P)
- Function: maintain a current whole-fleet view and expose decisions that can alter present feature commitments/admission, with a base constructor surface and a closed local-operator parent mode.
- Disturbance / variety regulated: failed or attention-needing features, waiting approval gates, queued work, current fleet concurrency pressure and aggregate failure conditions reported by the fleet circuit-breaker evaluator.
- Decisive decision or feedback right: base (`C`) — downstream/controller composition can consume first-party fleet status/triage/current-control primitives and configured admission limits; parent (`P`) — the authenticated/local operator can inspect current fleet triage and approve waiting feature runs, while configured limits directly constrain current admissions.
- Decision owner: base (`C`) — developer/composer of the first-party fleet-control primitives; parent (`P`) — local Shep operator/user.
- Supporting / enforcement mechanisms: fleet overview aggregation, triage items, batch approval use case, current feature lifecycle state, parallel-feature capacity service, persisted feature/run state and circuit-breaker status calculation.
- Closure path: base — current fleet state is aggregated into fleet health/triage → first-party current-control seams expose the state and actions needed to regulate active/queued work, but no default autonomous owner is wired to make the whole-fleet decision. Parent — operator inspects current fleet/triage state → invokes batch/current approval/control → affected feature runs resume or remain governed by present capacity/lifecycle constraints.
- Boundary reachability: fleet overview/triage/batch approval and feature-capacity enforcement are first-party production surfaces at the pinned ref. The circuit-breaker computation is intentionally treated only as a signal because current repository evidence states that it does not itself pause the fleet.
- Whole-system current view: `GetFleetOverviewUseCase` aggregates fleet health/status across features into cruising/queued/attention/failed categories and evaluates aggregate breaker state; triage exposes the current exception set.
- Current-control decision scope: whether waiting current work proceeds through approval, and whether new/current feature work receives an execution slot under the fleet's configured concurrency regime.
- Why this is / is not agent-owned: the repository has a meaningful S3 surface, but no first-party autonomous actor is evidenced as consuming the whole-fleet view and owning fleet-wide current resource/commitment/priority decisions. The optional supervisor can close individual gates under policy, but its evidenced scope does not establish default whole-fleet S3 ownership. The operator mode does close parent-governed current control.
- Evidence: [`packages/core/src/application/use-cases/fleet/get-fleet-overview.use-case.ts`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/packages/core/src/application/use-cases/fleet/get-fleet-overview.use-case.ts); [`packages/core/src/application/use-cases/fleet/batch-approve-features.use-case.ts`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/packages/core/src/application/use-cases/fleet/batch-approve-features.use-case.ts); [`specs/111-fleet-control-plane/UPSTREAM_RFC_PROPOSAL.md`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/specs/111-fleet-control-plane/UPSTREAM_RFC_PROPOSAL.md); [`specs/110-max-parallel-features/plan.md`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/specs/110-max-parallel-features/plan.md).
- Basis: explicit + structural
- Confidence: medium-high
- Caveats: the circuit-breaker status must not be read as an autonomous intervention, and per-feature supervisor gate closure is not promoted into whole-fleet S3 without evidence that the supervisor consumes the fleet-wide current view and owns the corresponding decision scope.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | downstream developer/composer using first-party fleet-control seams | current fleet status, triage, queue/capacity or breaker signal | fleet view and control primitives are available, but the autonomous fleet-level decision owner must be supplied/composed | [`get-fleet-overview.use-case.ts`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/packages/core/src/application/use-cases/fleet/get-fleet-overview.use-case.ts); [`UPSTREAM_RFC_PROPOSAL.md`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/specs/111-fleet-control-plane/UPSTREAM_RFC_PROPOSAL.md) |
| Parent (`P`) | local operator/user | visible waiting/attention state or current admission policy | operator approval changes waiting feature execution; configured capacity directly gates present work | [`batch-approve-features.use-case.ts`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/packages/core/src/application/use-cases/fleet/batch-approve-features.use-case.ts); [`specs/110-max-parallel-features/plan.md`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/specs/110-max-parallel-features/plan.md) |

## S3* — Complementary audit

- State: —
- Function: no materially independent complementary-audit function is established at the fleet boundary.
- Disturbance / variety regulated: schema/implementation errors, incomplete evidence and CI failures are detected, but through ordinary production verification paths rather than independent organizational audit.
- Decisive decision or feedback right: validators/evidence/CI paths can reject or request repair, but no separate audit actor with sufficiently independent evidence access is established.
- Decision owner: ordinary feature workflow validators, evidence executor and external CI/user review paths.
- Supporting / enforcement mechanisms: schema validation/repair nodes, evidence node, CI watch/fix loop, PR diff/review and audit/rationale records.
- Closure path: no ordinary S1 reporting path → materially different complementary evidence acquisition → independent audit judgment → corrective return into S3/S1 loop is established.
- Why this is / is not agent-owned: these checks are meaningful assurance mechanisms, but they remain coupled to the production feature path or external CI/review. A verifier label, evidence sub-agent or CI result alone does not establish S3* independence.
- Evidence: [`packages/core/src/infrastructure/services/agents/feature-agent/feature-agent-graph.ts`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/packages/core/src/infrastructure/services/agents/feature-agent/feature-agent-graph.ts); [`packages/core/src/infrastructure/services/agents/feature-agent/nodes/evidence.node.ts`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/packages/core/src/infrastructure/services/agents/feature-agent/nodes/evidence.node.ts); [`README.md`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/README.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: a downstream deployment could add an independently governed reviewer/evaluator over Shep outputs; that would be a separate system-in-focus or constructor completion requiring its own evidence.

### Absence scope

- Surfaces inspected: graph schema validators and repair loops, evidence sub-agent, CI watch/fix loop, PR review, fleet activity/audit records and supervisor rationale/explainability.
- Plausible first-party paths checked: validator as verifier, evidence agent, CI as independent check, user PR review and supervisor decision logging.
- Why no material first-party path remains: the inspected paths are routine workflow checks/records or share the operational path's evidence/control channel; none establishes a distinct complementary access path with independent organizational audit ownership.

## S4 — Intelligence / adaptation

- State: —
- Function: no fleet-level outside-and-then prospective adaptation loop is established.
- Disturbance / variety regulated: current feature uncertainty and historical project knowledge are processed, but not as prospective external-environment variety translated into an organizational adaptation decision.
- Decisive decision or feedback right: no first-party actor is evidenced as selecting and applying a prospective change to Shep's fleet capability/structure/policy from external/future sensing.
- Decision owner: none established.
- Supporting / enforcement mechanisms: feature `research` node, planner, adaptive model selection for current tasks, post-merge project-memory extraction/selection and fleet failure/status monitoring.
- Closure path: no external/future distinction → generated organizational adaptation option → selection → changed present fleet capability/S3 operation loop is established.
- Why this is / is not agent-owned: research is scoped to the current feature's implementation choices, while project memory distils internal past experience for later context. Model routing and failure monitoring react to current operation. None of these paths closes prospective organizational adaptation at the assessed fleet boundary.
- Evidence: [`packages/core/src/infrastructure/services/agents/feature-agent/nodes/research.node.ts`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/packages/core/src/infrastructure/services/agents/feature-agent/nodes/research.node.ts); [`packages/core/src/infrastructure/services/agents/feature-agent/nodes/extract-memory.node.ts`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/packages/core/src/infrastructure/services/agents/feature-agent/nodes/extract-memory.node.ts); [`docs/architecture/agent-system.md`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/docs/architecture/agent-system.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: persistent memory can support future adaptation, but persistence/retrieval alone is not S4 without the outside/future distinction and a returned change to current organizational capability.

### Absence scope

- Surfaces inspected: current-feature research/planning, project-memory extraction and selection, adaptive model routing, fleet control/circuit-breaker status, supervisor policy and settings/configuration.
- Plausible first-party paths checked: technical research, durable project memory, automatic model selection, fleet failure monitoring and supervisor recommendations.
- Why no material first-party path remains: the inspected paths address current task execution, internal historical context, reactive operating conditions or externally configured policy; no first-party path models prospective environmental change and returns a selected organizational adaptation into fleet capability/control.

## S5 — Policy / identity

- State: P
- Function: govern the ultimate authority arrangement under which delegated supervisor decisions may affect feature operation.
- Disturbance / variety regulated: conflict between delegated supervisor authority and the parent user's legitimate final authority over protected decisions/gates.
- Decisive decision or feedback right: determine/retain final authority when supervisor policy would otherwise allow advisory, cosign or autonomous gate action; a prior/final user decision cannot be overridden by the supervisor.
- Decision owner: local parent user/operator.
- Supporting / enforcement mechanisms: `SupervisorPolicy` autonomy modes, collaboration policy configuration, approval actor identity, prior-user-decision check, audit rationale and gate lifecycle.
- Closure path: parent configures the supervisor's authority regime → supervisor may advise/cosign/act autonomously within that delegation → a protected decision reaches the approval path → user authority can override or block supervisor action and is treated as final → feature operation resumes/aborts under the resulting authority decision.
- Boundary reachability: supervision modes and the user-final-authority rule are part of the documented first-party collaboration subsystem, while `ApproveAgentRunUseCase` enforces actor-aware user precedence in the production approval path at the pinned ref.
- Why this is / is not agent-owned: the supervisor can exercise delegated authority, including an autonomous gate mode, but it is not the ultimate policy owner because the repository explicitly preserves final user authority. The S5 witness is the authority regime itself, not a routine merge approval or prompt/config edit.
- Evidence: [`docs/architecture/supervision.md`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/docs/architecture/supervision.md); [`packages/core/src/application/use-cases/agents/approve-agent-run.use-case.ts`](https://github.com/shep-ai/shep/blob/a874b3238fd01ebdbafc11015cccd9a63ed6e2f2/packages/core/src/application/use-cases/agents/approve-agent-run.use-case.ts).
- Basis: explicit + structural
- Confidence: high
- Caveats: ordinary user approval of a feature would not by itself establish S5. The positive mapping depends on the explicit higher-level delegation/override contract defining who ultimately governs supervisor authority.

## Variety and escalation

- Worktree isolation, dependency gating/rebase, schema validation/repair, bounded retries and fleet-capacity queueing attenuate operational variety before it destabilizes other workcells.
- Parallel feature agents, concurrent implementation tasks, model routing, CI repair, fleet triage and optional supervisor intervention amplify regulator capacity.
- Failed/exhausted feature runs become blocked/failed attention states; approval gates and supervisor questions can escalate to the user; supervisor failures preserve the human path; fleet triage aggregates current exceptions for parent control.
- The reported fleet circuit-breaker condition is not credited as autonomous S3 intervention because the pinned implementation reports the state rather than automatically pausing/reprioritizing the fleet.

## Assessment summary

Shep establishes autonomous coding operations (`S1=A`) and a concrete constructor-owned coordination path for dependency/integration and capacity interference (`S2=C`). Its fleet overview, triage, approvals and concurrency controls establish a genuine current-control surface with constructor and parent modes (`S3=C(P)`), but no first-party autonomous whole-fleet controller is evidenced. Routine validation/evidence/CI paths do not establish independent complementary audit (`S3*=—`), and current-task research plus internal project memory do not close prospective fleet adaptation (`S4=—`). The collaboration subsystem explicitly preserves the user's ultimate authority over delegated supervisor action, establishing parent-governed S5 (`S5=P`).

Proposed canonical vector: `S1=A / S2=C / S3=C(P) / S3*=— / S4=— / S5=P`.

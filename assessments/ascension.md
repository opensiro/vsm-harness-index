---
harness_id: ascension
project_name: Ascension
repository: https://github.com/AI-Ascension/sts2-harness
review_ref: 53312ddbb074f7c187e5f59d88b6585da797fe17
reviewed_at: 2026-09-28
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-28
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: C(P)
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Ascension

## Review boundary

- System in focus: one first-party Ascension / `sts2-harness` deployment at pinned revision `53312ddbb074f7c187e5f59d88b6585da797fe17`, including the shipped live gameplay episode loop, provider/Exo decision source, protected host-facing runtime ports, durable workflow state and the `serve-workflow` management surface around that live runtime.
- Purpose and identity: run controlled model-driven Slay the Spire 2 episodes through explicit observation, legal-action, decision, mutation and evidence boundaries while preserving replayable run/episode/trajectory records and fail-closed recovery.
- Relevant environment: configured model/provider process, MCP server and gateway, authoritative game host/mod, authenticated deployment operator, target runtime instances, workflow/record stores and external evaluation/research consumers.
- Standard-distribution boundary: the repository-owned Rust harness and shipped runtime/management binaries. The gateway, MCP server, game host/mod and model-provider process remain external systems reached through explicit first-party ports; their internal organizational functions are not imported into Ascension.
- Credited operating / distribution surfaces: `EpisodeRunner`, `DecisionSource` / `ExoDecisionSource`, production runtime-v3 composition, observation/legal-action/action-settlement ports, workflow execution/store/status, `serve-workflow`, authenticated management commands and the same live run state those commands mutate.
- Adjacent first-party surfaces excluded from ownership: deterministic fake runners, synthetic POC/component traces, offline `Evaluator`, benchmark/scoring aggregation, replay/export consumers, repository tests/CI, research/generated expert-state material and maintainer project governance.
- First-party operating / deployment modes considered: direct runtime-v3 gameplay; served live workflow execution; authenticated pause/resume/cancel/step control; effect reconciliation/recovery; provider/context policy configuration. Offline evaluation and development research were inspected only as adjacent evidence unless wired into the live boundary.
- Recursion level: one Ascension deployment. A live model-driven episode is the primary S1 operational unit. Independent runs/episodes do not become coordinated S1 units merely because one deployment stores, routes or supervises them. The authenticated operator is a legitimate parent actor only for the separately evidenced S3 current-control mode.
- Reviewed revision: `53312ddbb074f7c187e5f59d88b6585da797fe17`.
- Observation date: 2026-09-28.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Ascension owns a bounded operational episode loop while keeping the authoritative game boundary outside the harness. `EpisodeRunner` launches through an `EpisodeRuntimePort`, observes current host state, obtains a generation-bound legal-action set, builds a `DecisionInput` containing the objective and hard constraints, invokes a `DecisionSource`, admits only a current legal action and sends it through the protected runtime boundary. The production `ExoDecisionSource` routes the current observation/action catalog and objective to the configured model/provider and can return a direct action or bounded plan.

The runner does not treat an acknowledgement as proof of effect. Settlement/recovery machinery requires the corresponding operation identity, a fresh host observation and effect witness before the ordinary episode state advances. Unknown effects are reconciled rather than blindly retried. This is important operational feedback and evidence integrity, but at this recursion it remains part of the normal S1 action→effect→next-observation loop rather than a separate S3* audit function.

The shipped runtime also exposes a management composition over live workflow execution. `RunSnapshot` carries whole-run status, outcome, graph/node cursor, pending operation, provider/node/replan budget and cleanup state. Authenticated `Pause`, `Resume`, `Cancel` and `Step` commands can alter the live run; unresolved effects and exhausted conditions can surface as `NeedsOperator`. This provides a function-specific S3 constructor path, and the bundled operator-controlled mode separately provides parent-governed S3 closure.

Primary evidence:

- [`README.md`](https://github.com/AI-Ascension/sts2-harness/blob/53312ddbb074f7c187e5f59d88b6585da797fe17/README.md) — declared experiment-control/runtime boundary, owner/consumer split, production runtime topology and distinction between live evidence and synthetic/offline checks.
- [`crates/harness/src/coordinator.rs`](https://github.com/AI-Ascension/sts2-harness/blob/53312ddbb074f7c187e5f59d88b6585da797fe17/crates/harness/src/coordinator.rs) — run/episode identity, provider execution, records, replay and artifact ports.
- [`crates/harness/src/episode/runner.rs`](https://github.com/AI-Ascension/sts2-harness/blob/53312ddbb074f7c187e5f59d88b6585da797fe17/crates/harness/src/episode/runner.rs) — complete bounded episode coordinator and authoritative runtime port.
- [`crates/harness/src/episode/policy_router.rs`](https://github.com/AI-Ascension/sts2-harness/blob/53312ddbb074f7c187e5f59d88b6585da797fe17/crates/harness/src/episode/policy_router.rs) — `DecisionSource` ownership boundary and production `ExoDecisionSource` decision path.
- [`crates/harness/src/episode/postconditions.rs`](https://github.com/AI-Ascension/sts2-harness/blob/53312ddbb074f7c187e5f59d88b6585da797fe17/crates/harness/src/episode/postconditions.rs) — ordinary action-settlement checks requiring fresh generation and effect evidence before episode progression.
- [`crates/harness/src/episode/coop.rs`](https://github.com/AI-Ascension/sts2-harness/blob/53312ddbb074f7c187e5f59d88b6585da797fe17/crates/harness/src/episode/coop.rs) and [`crates/harness/src/coop_native_coordinator_impl.rs`](https://github.com/AI-Ascension/sts2-harness/blob/53312ddbb074f7c187e5f59d88b6585da797fe17/crates/harness/src/coop_native_coordinator_impl.rs) — co-op synchronization/protocol machinery inspected for S2 without importing external peer operation.
- [`crates/harness/src/management/contract_types.rs`](https://github.com/AI-Ascension/sts2-harness/blob/53312ddbb074f7c187e5f59d88b6585da797fe17/crates/harness/src/management/contract_types.rs) — whole-run status, cursor, pending-operation, budget and cleanup view.
- [`crates/harness/src/management/execution_commands.rs`](https://github.com/AI-Ascension/sts2-harness/blob/53312ddbb074f7c187e5f59d88b6585da797fe17/crates/harness/src/management/execution_commands.rs) — live pause/resume/cancel/step mutation path and `NeedsOperator` handling.
- [`crates/harness/src/evaluation.rs`](https://github.com/AI-Ascension/sts2-harness/blob/53312ddbb074f7c187e5f59d88b6585da797fe17/crates/harness/src/evaluation.rs) — caller-fed offline evaluation inspected and excluded from live S3* ownership.

## Operational model

The model actor owns the local gameplay choice. Host-derived observations and legal actions bound that discretion, but the provider-backed decision source chooses among currently possible actions and receives changed host evidence on later steps. The harness supplies deterministic admission, settlement, recovery and record continuity around that discretionary loop.

At deployment level, Ascension also exposes a distinct current-control conversation. A whole-run snapshot can be read by a downstream controller or the authenticated operator, and the resulting pause/resume/cancel/step command directly changes the live workflow. No shipped autonomous metasystem actor consumes this view, so the first-party autonomous state is not `A`; the reusable path is Constructor and the bundled operator path is Parent-governed.

## S1 — Operations

- State: A
- Function: transform a run objective plus current authoritative game state into a sequence of legal game actions until terminal outcome or bounded failure.
- Disturbance / variety regulated: changing game state/stage/generation, changing legal-action catalog, provider/model uncertainty, stale observations, action settlement, unknown effects, repeated situations and recovery conditions.
- Decisive decision or feedback right: choose the next currently legal task/game action, plan step, wait/reobserve or recovery-directed response from the current observation, objective and hard constraints.
- Decision owner: the configured model actor behind the production `DecisionSource` / `ExoDecisionSource`.
- Supporting / enforcement mechanisms: `EpisodeRunner`, legal-action validation, action ledger, episode state machine, bounded step/abstention/repetition rules, runtime port, recovery controller and settlement checks.
- Closure path: authoritative observation + legal-action catalog → `DecisionInput` → model/provider decision → harness admission/dispatch → host settlement and changed observation → next runner step returns changed evidence to the model.
- Boundary reachability: the README documents the live runtime-v3 gameplay profile, and the shipped runner/policy types are production code rather than test-only fixtures.
- Why this is / is not agent-owned: removing the model decision source while leaving deterministic runner/admission/recovery machinery in place removes the task-specific discretion selecting the next gameplay action; the remaining machinery does not supply a materially equivalent gameplay policy.
- Evidence: `README.md`, `episode/runner.rs`, `episode/policy_router.rs`, `coordinator.rs`, `episode/postconditions.rs`.
- Basis: explicit + structural
- Confidence: high
- Caveats: game state/effect authority remains external behind gateway/MCP/host boundaries; that does not transfer host ownership to Ascension, but the repository still owns the agentic operational loop and its decision-feedback closure.

## S2 — Coordination

- State: —
- Function: no material first-party inter-S1 coordination function is established at the declared deployment recursion.
- Disturbance / variety regulated: no qualifying disturbance is established between two first-party S1 units.
- Decisive decision or feedback right: no qualifying inter-S1 coordination decision is established.
- Decision owner: none established for S2.
- Supporting / enforcement mechanisms: independent run/episode routing, leases/fences, `CoopCoordinator`, co-op peer generations, shared-vote/rejoin protocol state and native co-op recovery records were inspected as possible coordination mechanisms.
- Closure path: not applicable because the required multi-S1 disturbance relation is not established.
- Why this is / is not agent-owned: there is no qualifying S2 function to classify. Synchronization and co-op protocol machinery do not establish two first-party autonomous S1 units in one organization plus a concrete interaction-generated disturbance whose attenuation changes later S1 behaviour; external/local/ally peers cannot donate their internal autonomy to this repository.
- Evidence: `coordinator.rs`, `episode/coop.rs`, `coop_native_coordinator_impl.rs`, `README.md`.
- Basis: explicit + structural
- Confidence: high
- Caveats: protocol and synchronization readiness could support a future S2 mapping only if a deployed boundary establishes multiple first-party S1 units plus a concrete inter-unit disturbance and feedback closure.

### Absence scope

- Surfaces inspected: run/episode routing, leases/fences, co-op generation synchronization, shared-vote/rejoin protocol, native co-op records/reconciliation and concurrent workflow supervision.
- Plausible first-party paths checked: multiple episodes, multiple runtime instances, local/ally peer registration, shared vote and co-op recovery.
- Why no material first-party path remains: those mechanisms route, isolate or synchronize protocol state but do not establish the required pair of first-party S1 operational units and a specific inter-S1 disturbance/attenuation/feedback relation at this boundary.

## S3 — Inside-and-now control

- State: C(P)
- Function: maintain a whole-run current view and provide authoritative intervention over present commitments when a live workflow must pause, resume, advance one bounded step, cancel or await resolution of an uncertain current effect.
- Disturbance / variety regulated: current workflow status/cursor, game outcome, pending/unknown operation, provider/node/replan budget, cleanup state, pause/cancel state and `NeedsOperator` escalation.
- Decisive decision or feedback right: decide whether the current run may advance, must pause/resume, should be cancelled, or should execute its next bounded workflow step using the current whole-run snapshot.
- Decision owner: Constructor mode — the repository supplies the complete current-view/command path but no autonomous first-party metasystem actor that decides among those interventions. Parent mode — an authenticated deployment operator issues the intervention command in the shipped management composition.
- Supporting / enforcement mechanisms: `RunSnapshot`, workflow store, per-run lock, expected revision/definition binding, runtime/session pause/resume, cancellation cleanup, pending-effect reconciliation and authentication/scopes.
- Closure path: live workflow state → whole-run management snapshot → controller/operator chooses current-control command → `execution_commands.rs` mutates the corresponding live session/runtime → updated status/revision and subsequent execution reflect the intervention.
- Boundary reachability: the management types and execution commands operate on the same live workflow/runtime state, not a post-hoc dashboard copy; the repository documents and ships the management/runtime composition.
- Why this is / is not agent-owned: no shipped autonomous metasystem actor reads the whole-run view and chooses an intervention, so the base arrangement is Constructor rather than `A`; deterministic machinery enforces the selected command, while the bundled parent mode gives the discretionary intervention to the authenticated operator.
- Evidence: `management/contract_types.rs`, `management/execution_commands.rs`, live workflow/runtime composition documented in `README.md`.
- Basis: explicit + structural
- Confidence: high
- Caveats: ordinary episode progression, fixed budgets and deterministic recovery enforcement are not the S3 witness; the positive mapping depends on the separate whole-run management view and current-intervention authority.
- Whole-system current view: run identity/revision, status, terminal/nonterminal outcome, graph/node cursor, pending operation classification, provider/node/replan budget and cleanup state.
- Current-control decision scope: pause/resume present commitments, advance one bounded workflow step, cancel/cleanup, or withhold progression while a current effect needs resolution.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | downstream autonomous controller not supplied by the frozen distribution | consumer reads current whole-run state and selects a current-control command | first-party command path changes the live workflow/runtime | `management/contract_types.rs`, `management/execution_commands.rs` |
| Parent (`P`) | authenticated deployment operator | deliberate intervention or `NeedsOperator` condition | operator command changes subsequent live execution through the shipped management path | `management/execution_commands.rs`, `README.md` |

## S3* — Complementary audit

- State: —
- Function: no separate complementary-audit function is established at the declared operating boundary.
- Disturbance / variety regulated: no audit-specific variety is established outside ordinary operational action/effect feedback.
- Decisive decision or feedback right: no distinct complementary audit judgment is established.
- Decision owner: none established for S3*.
- Supporting / enforcement mechanisms: action settlement verification, recovery/re-observation, receipt reconciliation, replay, records, caller-fed `Evaluator`, context/memory review and management events were inspected as possible audit surfaces.
- Closure path: not applicable because no separate S3* judgment closes into live control.
- Why this is / is not agent-owned: `verify_settlement` and recovery/re-observation are mandatory parts of the normal S1 action→effect→next-state loop, not a sporadic or alternative metasystem audit of S1/S3 reporting. The offline `Evaluator` consumes caller-supplied samples and is not wired as an independent current auditor whose findings return into control; replay/records expose evidence but do not themselves supply an audit judgment.
- Evidence: `episode/postconditions.rs`, episode recovery/runner surfaces, `evaluation.rs`, `README.md`.
- Basis: explicit + structural
- Confidence: high
- Caveats: host-derived settlement evidence can be independent of the model choice without constituting a separate metasystem audit; at this boundary it is required ordinary operational feedback.

### Absence scope

- Surfaces inspected: dispatch/settlement checks, fresh-observation recovery, operation reconciliation, replay, records/artifacts, offline evaluation, context-memory review/admission and live management event/state surfaces.
- Plausible first-party paths checked: independent effect verification, post-hoc evaluator reports, replay divergence, context-memory reviewer/admission and management inspection.
- Why no material first-party path remains: the live effect checks belong to ordinary S1 feedback; the genuinely separate evaluation/replay surfaces are adjacent or caller-driven and do not close a complementary audit finding into subsequent live control at the declared boundary.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material external-and-prospective adaptation loop is established for the deployed harness organization.
- Disturbance / variety regulated: provider/model capabilities, context sources, memory, evaluation evidence and research artifacts may change, but no qualifying operating process turns external/future distinctions into adaptation options and returns an adopted option into present capability.
- Decisive decision or feedback right: no qualifying S4 adaptation judgment is established.
- Decision owner: none established for S4.
- Supporting / enforcement mechanisms: provider-session policy changes, inference/context profiles, context-memory selection, replay/evaluation and research/generated expert-state artifacts were inspected as possible adaptive mechanisms.
- Closure path: not applicable because no external/prospective distinction → adaptation option → adoption → changed current-capability path is established.
- Why this is / is not agent-owned: live management can apply already-authored configuration/policy values and the gameplay model adapts within the current task, but neither is an external-and-prospective organizational intelligence process developing future capability options and returning them to current operations.
- Evidence: management/provider-policy and context surfaces, `evaluation.rs`, `README.md`.
- Basis: explicit + structural
- Confidence: high
- Caveats: repository research, campaign evidence and policy/context editing are rich adjacent mechanisms, but no deployed prospective intelligence loop closes them into adaptation ownership.

### Absence scope

- Surfaces inspected: provider-session policy, context/memory ownership, replay/evaluation, research/generated state packages and live workflow composition.
- Plausible first-party paths checked: model/profile adoption, context-source adoption, memory selection, replay-derived diagnostics and project research/campaign feedback.
- Why no material first-party path remains: operating paths accept/enforce already-authored run-scoped choices; future/external analysis remains development/evaluation material rather than a deployed S4 option-generation/adoption closure.

## S5 — Policy and identity

- State: —
- Function: no material identity/ultimate-policy closure is established at the Ascension deployment recursion.
- Disturbance / variety regulated: objectives, hard constraints, admission rules, provider/context policy, authentication scopes and compatibility pins constrain operation but remain below identity/ultimate-policy level.
- Decisive decision or feedback right: no system-identity or ultimate-policy judgment is established.
- Decision owner: none established for S5.
- Supporting / enforcement mechanisms: objective/constraint configuration, provider/context policy, target admission, authentication/scopes, schema/revision pins and operator controls were inspected as possible policy mechanisms.
- Closure path: not applicable because no identity/ultimate-policy issue → legitimate ultimate authority → returned identity-level decision path is established.
- Why this is / is not agent-owned: configuration and authenticated intervention govern ordinary current execution; neither the gameplay model nor management runtime owns an ultimate identity/policy judgment at this recursion.
- Evidence: `episode/runner.rs`, management configuration/control surfaces, `README.md`.
- Basis: explicit + structural
- Confidence: high
- Caveats: operator authentication and configuration authority are real constraints/current-control mechanisms, but no identity-level issue/ultimate-authority/returned-policy conversation is established.

### Absence scope

- Surfaces inspected: objective/constraints, authentication/scopes, provider/context policy, target admission, runtime profile/revision/schema gates and repository governance documentation.
- Plausible first-party paths checked: policy approval/adoption, hard constraints, target admission, authenticated operator authority and maintainer governance.
- Why no material first-party path remains: all live paths found regulate current operation/configuration or compatibility; maintainer governance is an adjacent OSS-development organization and is not imported as runtime S5.

## Recursion

The declared recursion is one Ascension deployment. One live model-driven episode is its operational S1. Independent episodes and co-op protocol participants are not promoted into additional first-party S1 units without evidence of autonomous operational ownership inside the assessed boundary. The management surface sits at the deployment-level metasystem recursion and supplies current-control composition/parent closure for S3 only.

## Variety and escalation

The model absorbs gameplay choice variety within host-generated legal actions and configured objectives/constraints. Ascension attenuates unsafe or ambiguous mutation variety through legality checks, identity/generation fences, bounded retries, settlement requirements and recovery. Unknown effects are preserved as unresolved and can escalate to `NeedsOperator` rather than being converted into success or blind retry. That escalation feeds the S3 management path; it does not create S3* or S5 by itself.

## Evidence gaps

No material unresolved evidence gap requires `?` at the pinned revision. The repository explicitly distinguishes confirmed live/runtime surfaces from synthetic/offline evidence, which permits the ownership boundary to be drawn conservatively. Broader compatibility and gameplay-performance claims remain outside this organizational classification.

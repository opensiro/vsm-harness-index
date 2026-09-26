---
harness_id: ascension
project_name: Ascension
repository: https://github.com/AI-Ascension/sts2-harness
review_ref: 53312ddbb074f7c187e5f59d88b6585da797fe17
reviewed_at: 2026-09-26
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-26
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: C(P)
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# Ascension

## Review boundary

- System in focus: one first-party Ascension/STSl2 harness deployment at pinned revision `53312ddbb074f7c187e5f59d88b6585da797fe17`, including the live runtime-v3 gameplay episode loop, provider/Exo decision source, host-facing episode runtime ports, recovery/settlement verification, durable workflow records, and the shipped `serve-workflow` management mode around the same live runtime.
- Purpose and identity: coordinate controlled AI game-playing episodes through explicit observation/action/provider boundaries, preserve run/episode/trajectory evidence, prevent unsafe or ambiguous mutation progression, and make live runs inspectable and controllable without bypassing gateway/MCP/game-host authority.
- Relevant environment: the human/operator parent, configured model/provider process, MCP server and gateway, authoritative game host/mod and its legal-action/observation boundary, target runtime instances, persisted workflow/record stores, and external experiment/evaluation consumers.
- Standard-distribution boundary: the `sts2-harness` Rust package and its shipped runtime/management binaries at the frozen ref. Gateway, MCP server, game mod/host and model-provider execution are external systems reached through first-party ports/adapters; they may supply authoritative observations/effects but do not donate harness decision ownership. Offline fake runners, benchmark/evaluation aggregation, research specifications, tests and recorded-campaign evidence are adjacent unless a live runtime path explicitly uses the same mechanism.
- Credited operating / distribution surfaces: `EpisodeRunner` and episode state/recovery machinery; `ExoDecisionSource`; runtime-v3 composition reached by `sts2-harness-runtime`; authoritative observation/legal-action/action-settlement ports; `serve-workflow`; live workflow execution/store/status; authenticated management commands; durable provider-policy owner as a current run configuration surface; and the same run-scoped records used by live management.
- Adjacent first-party surfaces excluded from ownership: `sts2-harness-runtime-v2-fake`, synthetic POC/runtime-v4 component checks without live provider/host closure, offline `Evaluator`, benchmark/scoring aggregation, replay/export tools when used only after a run, repository tests/CI, research/generated expert-state material and maintainer development/governance activity.
- First-party operating / deployment modes considered: direct runtime-v3 gameplay execution; negotiated/expert gameplay profiles where they preserve the same episode decision/settlement contract; live workflow service via `sts2-harness-runtime serve-workflow`; authenticated operator inspection/control; durable provider-session policy configuration; recovery/reconciliation after uncertain effects; replay/evaluation only as adjacent evidence unless wired into current operation.
- Recursion level: one Ascension deployment controlling one or more workflow/episode executions. A live model-driven gameplay episode is an S1 operational unit. Multiple independent runs/episodes do not become an S2 relation merely because the deployment can store or route them. The authenticated deployment operator is a legitimate parent actor for the separately evidenced S3 parent mode.
- Reviewed revision: `53312ddbb074f7c187e5f59d88b6585da797fe17`.
- Observation date: 2026-09-26.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Ascension separates the model decision boundary from the authoritative game boundary. `EpisodeRunner` owns a bounded episode loop but intentionally contains no gameplay heuristic or fallback action policy. It launches through an `EpisodeRuntimePort`, observes current host state, obtains the generation-bound legal-action catalog, builds a `DecisionInput` containing the objective and hard constraints, and asks a `DecisionSource` to choose. The production `ExoDecisionSource` sends that bounded input to a configured provider session and returns an action, plan, wait/reobserve or recovery decision. The harness then dispatches only a currently legal action through the protected runtime port.

A model/provider response is not treated as evidence that an effect occurred. After dispatch, the runner waits for or reconciles host-side settlement, requires a fresh observation generation plus an effect witness, and only then advances the episode state machine. Unknown or conflicting outcomes enter the recovery path instead of triggering a replacement model decision or blind retry. This supplies a complementary host-evidence path distinct from the model's operational choice and from the first dispatch acknowledgement.

The shipped `sts2-harness-runtime` binary also exposes `serve-workflow`. That mode builds an authenticated loopback management service around the production live runtime/provider factories and durable workflow store. A `RunSnapshot` exposes the current workflow status, game outcome, graph/node cursor, pending operation, provider/node/replan budget and cleanup state. Authenticated `Pause`, `Resume`, `Cancel` and `Step` commands act on the corresponding live runtime/session; unknown effects or exhausted conditions can move a run into `NeedsOperator`. The first-party status/command API is therefore an S3 constructor surface, while the bundled authenticated operator mode separately closes parent-governed current control.

The repository contains additional policy, context-memory, replay and evaluation machinery. Provider-session policy can be imported, proposed, approved and adopted through authenticated run-scoped management, but the reviewed implementation does not establish an external-and-prospective intelligence process that generates those changes as adaptation options. Likewise, run/provider/context policies are scoped operational/configuration controls rather than an identity/ultimate-policy conversation for the system as a whole.

Primary evidence:

- [`README.md`](https://github.com/AI-Ascension/sts2-harness/blob/53312ddbb074f7c187e5f59d88b6585da797fe17/README.md) — declared experiment-control/runtime boundary, live runtime-v3 mode, owner/consumer split and explicit distinction between runtime evidence and synthetic/offline checks.
- [`crates/harness/src/episode/runner.rs`](https://github.com/AI-Ascension/sts2-harness/blob/53312ddbb074f7c187e5f59d88b6585da797fe17/crates/harness/src/episode/runner.rs) — complete episode coordinator, objective/constraints, authoritative runtime port and bounded live run loop.
- [`crates/harness/src/episode/runner_steps.rs`](https://github.com/AI-Ascension/sts2-harness/blob/53312ddbb074f7c187e5f59d88b6585da797fe17/crates/harness/src/episode/runner_steps.rs) — observation/legal-action acquisition, model policy invocation, action/reobserve/wait/recovery handling and later-step feedback.
- [`crates/harness/src/episode/policy_router.rs`](https://github.com/AI-Ascension/sts2-harness/blob/53312ddbb074f7c187e5f59d88b6585da797fe17/crates/harness/src/episode/policy_router.rs) — `DecisionSource` ownership boundary and production `ExoDecisionSource` model decision path.
- [`crates/harness/src/episode/runner_actions.rs`](https://github.com/AI-Ascension/sts2-harness/blob/53312ddbb074f7c187e5f59d88b6585da797fe17/crates/harness/src/episode/runner_actions.rs) — legal-action admission, dispatch, settlement/recovery and no-blind-replacement behavior.
- [`crates/harness/src/episode/runner_recovery.rs`](https://github.com/AI-Ascension/sts2-harness/blob/53312ddbb074f7c187e5f59d88b6585da797fe17/crates/harness/src/episode/runner_recovery.rs) — host re-observation/reconciliation and effect-witness closure for uncertain or merely accepted mutations.
- [`crates/harness/src/episode/postconditions.rs`](https://github.com/AI-Ascension/sts2-harness/blob/53312ddbb074f7c187e5f59d88b6585da797fe17/crates/harness/src/episode/postconditions.rs) — independent settlement checks requiring a fresh generation and effect witness before operation advances.
- [`crates/harness/src/episode/recovery.rs`](https://github.com/AI-Ascension/sts2-harness/blob/53312ddbb074f7c187e5f59d88b6585da797fe17/crates/harness/src/episode/recovery.rs) — bounded alternate reobserve/reconcile/receipt-query access path.
- [`crates/harness/src/bin/sts2-harness-runtime.rs`](https://github.com/AI-Ascension/sts2-harness/blob/53312ddbb074f7c187e5f59d88b6585da797fe17/crates/harness/src/bin/sts2-harness-runtime.rs) and [`runtime_support/workflow_service.rs`](https://github.com/AI-Ascension/sts2-harness/blob/53312ddbb074f7c187e5f59d88b6585da797fe17/crates/harness/src/bin/runtime_support/workflow_service.rs) — shipped live runtime and authenticated `serve-workflow` composition around concrete runtime/provider adapters.
- [`crates/harness/src/management/contract_types.rs`](https://github.com/AI-Ascension/sts2-harness/blob/53312ddbb074f7c187e5f59d88b6585da797fe17/crates/harness/src/management/contract_types.rs) — whole-run current snapshot: status, outcome, cursor, pending effect, budget and cleanup state.
- [`crates/harness/src/management/execution_commands.rs`](https://github.com/AI-Ascension/sts2-harness/blob/53312ddbb074f7c187e5f59d88b6585da797fe17/crates/harness/src/management/execution_commands.rs) — current-control closure for pause/resume/cancel/step and `NeedsOperator` escalation.
- [`crates/harness/src/management/provider_policy.rs`](https://github.com/AI-Ascension/sts2-harness/blob/53312ddbb074f7c187e5f59d88b6585da797fe17/crates/harness/src/management/provider_policy.rs) — authenticated run-scoped provider-policy import/propose/approve/adopt path inspected for S4/S5 and treated as configuration rather than prospective/identity closure.
- [`crates/harness/src/evaluation.rs`](https://github.com/AI-Ascension/sts2-harness/blob/53312ddbb074f7c187e5f59d88b6585da797fe17/crates/harness/src/evaluation.rs) — offline/caller-fed evaluator inspected and excluded from S3* ownership.

## Operational model

The live episode's model actor owns operational choice. Host-derived observation and legal-action state constrain what it may choose, but `DecisionSource` selects the task/game action and receives changed host evidence again on later steps. The harness supplies strict admission, effect verification, recovery and state continuity around that discretion.

At the wider deployment boundary, current-control ownership has two separately supported arrangements. The management API exposes a first-party S3-specific constructor path consisting of the whole-run snapshot plus pause/resume/cancel/step mutation semantics, but Ascension does not ship an autonomous agent that consumes this path as metasystemic controller. The same `serve-workflow` distribution does expose the path to an authenticated human/operator parent whose command changes the current live run, establishing an additional parent-governed S3 mode.

## S1 — Operations

- State: A
- Function: turn a run objective and current authoritative game observation into a sequence of legal game actions until terminal outcome or bounded failure.
- Disturbance / variety regulated: changing game state/stage/generation, changing legal-action catalog, model uncertainty/abstention, provider failures, action settlement, stale observations, unknown effects, repeated situations and recovery conditions.
- Decisive decision or feedback right: choose which currently legal action to take, or choose wait/reobserve/recovery behavior, from the current observation, objective and hard constraints.
- Decision owner: the configured model actor behind the production `DecisionSource`/`ExoDecisionSource` for ordinary action choice.
- Supporting / enforcement mechanisms: `EpisodeRunner`, `PolicyRouter`, legal-action validation, action ledger, state machine, step/repetition/abstention bounds, gateway/MCP runtime port, stability barrier, recovery controller and postcondition verification.
- Closure path: authoritative host observation and legal-action catalog → `DecisionInput` → model/provider chooses an action/plan or other policy choice → harness admits and dispatches the action → host settlement/reobservation changes the authoritative observation → the next runner step gives the changed evidence back to the model for a new decision.
- Boundary reachability: `runtime-v3-gameplay` is a documented and shipped profile of `sts2-harness-runtime`; `workflow_service.rs` also instantiates the same `RuntimeV3SessionWorker` and production `ExoDecisionSource` for served-live workflows. The positive S1 path therefore does not depend on a test fake or downstream harness.
- Why this is / is not agent-owned: removing the model decision source leaves observation, legality, dispatch and recovery machinery but removes the task-specific choice among legal actions. The runtime contains no fallback gameplay heuristic that would make materially equivalent strategic choices.
- Evidence: `episode/runner.rs`, `episode/runner_steps.rs`, `episode/policy_router.rs`, `episode/runner_actions.rs`, `runtime_support/workflow_service.rs`, `README.md`.
- Basis: explicit + structural
- Confidence: high
- Caveats: the authoritative game state and effect execution live behind external gateway/MCP/host boundaries, while provider inference may run in a separate process; the first-party harness still owns the operational loop and feedback closure.

## S2 — Coordination

- State: —
- Function: no material first-party inter-S1 coordination function is established for the assessed deployment modes.
- Disturbance / variety regulated: the repository can route multiple episodes/instances and contains co-op synchronization/protocol machinery, but the reviewed live operational boundary does not establish two or more first-party S1 agent units whose interaction creates a concrete shared organizational disturbance regulated by that machinery.
- Decisive decision or feedback right: not established for inter-S1 coordination.
- Decision owner: none established for S2 at this boundary.
- Supporting / enforcement mechanisms: run/episode routing, per-run locks, leases/fences, `CoopCoordinator`, cooperative-native envelope/recovery machinery and provider/session policy regulate execution/protocol state but do not by themselves establish the required multi-S1 relation.
- Closure path: not applicable for S2.
- Why this is / is not agent-owned: there is no qualifying S2 function to classify. Independent episodes are separate experimental operations, not automatically coordinated S1 units of one task organization; co-op peer/generation gates do not establish that the peers are first-party autonomous S1 actors owned by this harness.
- Evidence: `coordinator.rs`, `episode/coop.rs`, `coop_native_coordinator.rs`, `coop_native_coordinator_impl.rs`, `README.md`.
- Basis: explicit + structural
- Confidence: high
- Caveats: a future admitted cooperative deployment with multiple first-party agent peers and an evidenced peer-interference relation could change this result; protocol readiness alone is insufficient.

### Absence scope

- Surfaces inspected: run/episode coordinator, runtime-v3 episode loop, routing/lease/fence machinery, co-op generation gate, cooperative-native coordinator/protocol, served-live workflow management and provider/session ownership.
- Plausible first-party paths checked: multiple active runs/episodes, multi-instance routing, co-op local/ally registration, shared-vote/rejoin envelopes, provider-session sharing and workflow concurrency.
- Why no material first-party path remains: all discovered mechanisms either isolate/route independent runs or coordinate protocol/effect state without establishing two first-party autonomous S1 units participating in one organizational operation and a concrete inter-S1 disturbance with feedback into both units.

## S3 — Inside-and-now control

- State: C(P)
- Function: maintain a current whole-run view and permit authoritative intervention in the live workflow when current execution must pause, resume, advance one step, cancel, reconcile an unknown effect or await operator resolution.
- Disturbance / variety regulated: changing workflow status/cursor, current game outcome, pending or unknown operations, consumed/reserved provider and node budgets, cleanup state, cancellation, pause state and conditions escalated as `NeedsOperator`.
- Decisive decision or feedback right: decide whether the current run is allowed to advance, must pause, resume, cancel or execute the next bounded workflow step, using the whole-run snapshot and current recovery state.
- Decision owner: constructor mode — no autonomous first-party S3 actor is shipped; the management status/command API exposes the complete S3-specific decision path for composition. Parent mode — an authenticated deployment operator with `workflow:control` authority issues the current-control command for the live run.
- Supporting / enforcement mechanisms: durable `RunSnapshot`, expected revision/definition identity, workflow store, per-run lock, runtime/session pause-resume APIs, cancellation cleanup, pending-effect reconciliation, authenticated scopes and management HTTP/client boundary.
- Closure path: current live workflow writes status/cursor/pending-effect/budget/cleanup facts → management exposes the whole-run snapshot → controller/operator selects a current-control command → `execution_commands.rs` directly pauses/resumes/cancels or steps the corresponding live runtime/session → the resulting workflow status/revision and later operation reflect that decision.
- Boundary reachability: `sts2-harness-runtime serve-workflow` directly calls the production management service with concrete runtime-v3/provider factories and authentication, so parent closure is a shipped operating mode. The same first-party `ManagementService` status/command contract is public composition surface for the constructor mode.
- Why this is / is not agent-owned: no shipped autonomous metasystem actor consumes the whole-run status and chooses interventions. Deterministic code enforces the chosen command and recovery rules; in the bundled parent mode the discretionary intervention belongs to the authenticated operator.
- Evidence: `bin/sts2-harness-runtime.rs`, `runtime_support/workflow_service.rs`, `management/contract_types.rs`, `management/execution_commands.rs`, `management/live_workflow.rs`.
- Basis: explicit + structural
- Confidence: high
- Caveats: ordinary autonomous episode decisions remain S1; fixed step/recovery/budget enforcement alone is not the S3 witness. The positive witness is the separate whole-run management view plus intervention authority.
- Whole-system current view: `RunSnapshot` exposes the workflow run identity/revision, current status, terminal/nonterminal game outcome, current graph/node/node-execution cursor, any pending operation and its classification, provider/node/replan budgets, cleanup state and target admission.
- Current-control decision scope: pause or resume current commitments, execute/withhold the next workflow step, cancel the live run and cleanup, and resolve/escalate unknown current effects before further progress.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | downstream autonomous controller not supplied by the frozen distribution; first-party management API supplies the S3-specific view/command path | consumer reads current run snapshot and selects a current-control command | management command directly changes the live workflow/runtime and persists the new revision/status | `management/contract_types.rs`, `management/execution_commands.rs`, `management/live_workflow.rs` |
| Parent (`P`) | authenticated deployment operator | current run requires intervention, deliberate pause/resume/step/cancel, or `NeedsOperator` resolution | operator command enters shipped `serve-workflow` service and changes subsequent live execution | `bin/sts2-harness-runtime.rs`, `runtime_support/workflow_service.rs`, `management/execution_commands.rs` |

## S3* — Complementary audit

- State: C
- Function: independently check whether a model-selected and dispatched operation actually settled in authoritative host reality before the episode is allowed to treat that effect as complete.
- Disturbance / variety regulated: dispatch acknowledgement can be merely accepted, unknown, stale, conflicting or disconnected from actual game-state mutation; blindly trusting it could advance policy from a false state or duplicate an effect.
- Decisive decision or feedback right: determine whether the exact operation has a reconciled/settled receipt or a fresh post-action host observation plus effect witness, and refuse operational advancement while that evidence is absent or contradictory.
- Decision owner: deterministic first-party harness reconciliation/postcondition logic; no autonomous independent auditor owns the verdict at this ref, so the audit path is Constructor rather than Autonomous.
- Supporting / enforcement mechanisms: operation identity, action ledger, `RecoveryController`, `reconcile`, `reobserve`, retained receipt query, stability barrier, fresh-generation checks and episode state machine.
- Closure path: routine action dispatch returns accepted/unknown/error or a provisional receipt → when certainty is insufficient the harness uses alternate host reconciliation/reobservation/barrier evidence for the same operation → verifies fresh generation and effect witness → only a verified settled result advances the state machine; otherwise recovery continues/stops and no replacement strategic action is requested.
- Boundary reachability: the reconciliation and settlement checks are called directly by the production `EpisodeRunner` used in runtime-v3 and served-live workflows; they are not repository-only tests or post-hoc benchmark scoring.
- Why this is / is not agent-owned: the complementary access is genuinely host-derived and can contradict the ordinary dispatch result, but deterministic harness code evaluates it. No separately autonomous audit actor is supplied.
- Evidence: `episode/runner_actions.rs`, `episode/runner_recovery.rs`, `episode/recovery.rs`, `episode/postconditions.rs`, `episode/runner.rs`.
- Basis: explicit + structural
- Confidence: high
- Caveats: the general offline `Evaluator` is not the positive witness; it consumes caller-supplied samples and is not credited as a current operational auditor.
- Claim being audited: that the model-selected, admitted action actually produced a settled effect corresponding to the exact operation/action identity.
- Ordinary reporting path: the action dispatch call and its immediate `TransitionReceipt`/dispatch status.
- Complementary access path: same-operation host reconciliation, re-observation or barrier sampling that supplies a fresh authoritative observation/effect witness independently of the model choice and initial acknowledgement.
- Independence boundary: model/provider decision authority is separate from gateway/MCP/host effect evidence; the harness cannot infer success from the provider response or action acceptance alone.
- Who acts on findings: deterministic `EpisodeRunner`/state-machine control blocks the next policy decision, continues recovery or advances only after settlement verification.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party external-and-prospective organizational adaptation loop is established at the assessed deployment boundary.
- Disturbance / variety regulated: provider/model capabilities, context sources, memory, experimental evidence and research artifacts can change over time, but the frozen operating system does not autonomously or parent-closedly turn external/future distinctions into adaptation options that are then adopted into present capability.
- Decisive decision or feedback right: not established for a qualifying S4 adaptation judgment.
- Decision owner: none established for S4 at this boundary.
- Supporting / enforcement mechanisms: provider-session policy import/propose/approve/adopt, inference-profile catalogs/revisions, context owner/source adoption, context-memory selection, replay/evaluation/research artifacts and configuration pins.
- Closure path: not applicable for S4; management can apply operator-authored configuration/policy values, but no evidenced first-party path supplies the missing external/prospective intelligence-and-option-generation relation.
- Why this is / is not agent-owned: the gameplay model reasons about the current game task, while policy/context management accepts already-authored changes. Neither demonstrates an organizational S4 actor modeling future/external change and returning adaptation options into present capability.
- Evidence: `management/provider_policy.rs`, `management/mod.rs`, context-memory/context-owner surfaces, `evaluation.rs`, `README.md`.
- Basis: explicit + structural
- Confidence: high
- Caveats: repository research and dated campaigns are rich development intelligence, but they belong to the adjacent project-development organization unless wired into deployed adaptation ownership.

### Absence scope

- Surfaces inspected: provider-session policy owner/commands, inference-profile catalog and revision surfaces, context owner/memory policies, context capture, replay/evaluation, research/generated expert-state material and live workflow composition.
- Plausible first-party paths checked: policy proposal/adoption, model/provider profile changes, source/context adoption, memory selection, replay-derived diagnostics and project research/campaign feedback.
- Why no material first-party path remains: discovered live paths accept or enforce already-authored run-scoped configuration and context; discovered future/external analysis remains development/evaluation material. No operating path closes external/prospective distinction → adaptation option → authoritative adoption → changed current capability.

## S5 — Policy and identity

- State: —
- Function: no material runtime identity/ultimate-policy closure is established for the Ascension deployment.
- Disturbance / variety regulated: objectives, hard constraints, target admission, provider policy, context grants, authentication scopes and compatibility pins constrain execution, but they operate below identity/ultimate-policy level.
- Decisive decision or feedback right: not established for resolving system identity or ultimate policy tensions at the declared recursion.
- Decision owner: none established for S5 at this boundary.
- Supporting / enforcement mechanisms: objective/hard-constraint configuration, target admission, provider-session policy owner, authentication/scopes, context owner grants, schema/revision pins and fail-closed compatibility gates.
- Closure path: not applicable for S5; these mechanisms directly configure or constrain operation and do not expose an identity/policy issue path to a legitimate ultimate authority with a returned identity-level decision.
- Why this is / is not agent-owned: neither the gameplay model nor management runtime owns an ultimate identity/policy judgment. Authenticated operator control over ordinary run/provider configuration is S3/current configuration, not automatically S5.
- Evidence: `episode/runner.rs`, `management/provider_policy.rs`, `runtime_support/workflow_service.rs`, `README.md`.
- Basis: explicit + structural
- Confidence: high
- Caveats: repository maintainers make project-level governance decisions, but that adjacent OSS organization is not imported as runtime S5 ownership.

### Absence scope

- Surfaces inspected: objective/constraint input, authentication/scopes, provider-session policy proposal/adoption, target admission, context ownership/grants, runtime profile/revision/schema gates and repository governance/research documentation.
- Plausible first-party paths checked: policy approvals, provider-policy adoption, target admission decisions, hard constraints, management operator authority and maintainer governance.
- Why no material first-party path remains: all runtime paths found govern current execution/configuration or compatibility; none evidences identity/ultimate-policy issue detection, legitimate ultimate authority and a returned identity-level decision governing later operation at the assessed deployment recursion.

## Recursion

The declared recursion is one Ascension deployment. A live model-driven episode is an operational S1. Separate runs can coexist under the management service, but their mere coexistence/routing does not prove an S2 relation. The management service is a deployment-level metasystem surface over current workflows; downstream autonomous composition and the authenticated parent operator are recorded separately for S3 ownership.

## Variety and escalation

The model absorbs gameplay choice variety within host-generated legal actions, objective and hard constraints. The harness attenuates unsafe/ambiguous effect variety through generation binding, idempotency, barriers, recovery and settlement verification. Unknown effects can move the live workflow to `NeedsOperator`, preserving the unresolved distinction instead of inventing success or retrying blindly. Management then provides the current-control channel for the legitimate parent to pause, resume, cancel or advance the run. Offline evaluation and replay remain evidence/analysis surfaces rather than silently becoming runtime regulation.

## Evidence gaps

No material unresolved evidence gap requires `?` at the pinned ref. Live runtime-v3 and served management reachability are explicit in source and first-party documentation. Broader game/provider compatibility and model-played Victory are themselves documented as unverified, but those empirical limitations do not prevent reconstruction of the organizational decision/feedback paths assessed here.

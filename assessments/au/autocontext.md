---
harness_id: autocontext
project_name: autocontext
repository: https://github.com/greyhaven-ai/autocontext
review_ref: 7ccca4681fa113e495c07b0b5b44d28d1181033c
reviewed_at: 2026-10-31
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-31
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C
autonomy_s3_star: A
autonomy_s4: A
autonomy_s5: —
---

# autocontext

## Review boundary

- System in focus: the shipped Python `autoctx` scenario/generation and campaign organization, not external model endpoints, target tasks or downstream harnesses.
- Purpose and identity: iteratively propose, evaluate, select and deploy context/harness changes under bounded scenario evidence, with optional concurrent campaigns and independently routed audit.
- Relevant environment: scenario/task outcomes, mismatched evaluator cohorts, uncertain evidence, resource contention, model/provider failures, and changing future task demands.
- Standard-distribution boundary: `autocontext` Python package, CLI, generation pipeline, context-bundle promotion, scheduler and opt-in campaign auditor. The TypeScript frontend, external models, training infrastructure and hosted scenarios are not presumed internal organizational owners.
- Credited operating / distribution surfaces: `autoctx solve/run`, `AgentOrchestrator`, `GenerationPipeline`, `ContextBundlePromotionCoordinator`, `CampaignScheduler` and explicitly configured `CampaignAuditor` checkpoint composition.
- Adjacent first-party surfaces excluded from ownership: benchmark fixtures, ablations, offline training-data export, demo agents, documentation pipelines, production trace dashboards and test-only helpers; these may corroborate wiring but do not donate independent functions.
- First-party operating / deployment modes considered: model-backed iterative scenario generation; opt-in multi-worker campaigns; context-bundle promotion with matched/held-out evaluation; separately routed campaign auditor when enabled. Deterministic/test provider mode does not establish model autonomy by itself.
- Recursion level: one continuing harness-evolution program coordinating scenario runs; scenario-specific competitor execution is subordinate operation, not another assumed complete VSM.
- Reviewed revision: `7ccca4681fa113e495c07b0b5b44d28d1181033c`.
- Observation date: 2026-10-31.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The `autoctx` CLI composes a model-backed orchestrator with competitor, analyst, coach, architect and optional curator/skeptic roles. A generation proposes a strategy and immutable candidate context bundle, executes/scans scenario trials, records gate decisions and persists feedback. Context changes are not activated by a score alone: a coordinator evaluates incumbent-versus-candidate trials, validates evidence and separately promotes a candidate. The optional campaign scheduler reserves heterogeneous workers and resources through durable leases, budgets and retry/cancel/reconcile rules. An opt-in `CampaignAuditor` receives sealed redacted evidence on a distinct model route, makes an independent integrity judgment and can return a hold recommendation that the promotion coordinator applies; it cannot directly rewrite the evaluated artifacts.

Pinned first-party evidence:

- [Installed CLI and supported generation/campaign modes](https://github.com/greyhaven-ai/autocontext/blob/7ccca4681fa113e495c07b0b5b44d28d1181033c/autocontext/README.md)
- [Model roles and strategy/architecture proposal](https://github.com/greyhaven-ai/autocontext/blob/7ccca4681fa113e495c07b0b5b44d28d1181033c/autocontext/src/autocontext/agents/orchestrator.py)
- [Generation-stage model decisions, mutable strategy and proposed bundle](https://github.com/greyhaven-ai/autocontext/blob/7ccca4681fa113e495c07b0b5b44d28d1181033c/autocontext/src/autocontext/loop/stages.py)
- [Generation pipeline and budget rollback](https://github.com/greyhaven-ai/autocontext/blob/7ccca4681fa113e495c07b0b5b44d28d1181033c/autocontext/src/autocontext/loop/generation_pipeline.py)
- [Campaign worker leases, global capacity, result and cancellation return](https://github.com/greyhaven-ai/autocontext/blob/7ccca4681fa113e495c07b0b5b44d28d1181033c/autocontext/src/autocontext/execution/campaign_scheduler.py)
- [Matched candidate evaluation and guarded activation](https://github.com/greyhaven-ai/autocontext/blob/7ccca4681fa113e495c07b0b5b44d28d1181033c/autocontext/src/autocontext/context_bundles/promotion.py)
- [Auditor route independence and bounded evidence judgment](https://github.com/greyhaven-ai/autocontext/blob/7ccca4681fa113e495c07b0b5b44d28d1181033c/autocontext/src/autocontext/audit/campaign_auditor.py)
- [Auditor route identity comparison](https://github.com/greyhaven-ai/autocontext/blob/7ccca4681fa113e495c07b0b5b44d28d1181033c/autocontext/src/autocontext/audit/campaign_audit_routes.py)
- [Campaign auditor opt-in, checkpoints and promotion hold semantics](https://github.com/greyhaven-ai/autocontext/blob/7ccca4681fa113e495c07b0b5b44d28d1181033c/docs/campaign-auditor.md)

## Operational model

A human selects a scenario/goal and initial policies. A model ensemble proposes actions, analyzes feedback and may architect changes for subsequent generations. Runtime gates validate and compare them, updating durable knowledge and optionally activating a new bundle. Parallel campaign jobs are first-party managed but may contain separate model-led scenario S1 cells; scheduling prevents their resource claims from colliding. Operator approval and external provider trust remain outside the assessed autonomous decision rights.

## S1 — Operations

- State: A
- Function: perform task/scenario attempts and iteratively generate improved strategies/harness artifacts from observed outcomes.
- Disturbance / variety regulated: scenario variation, failed actions, changing score and tool/model feedback.
- Decisive decision or feedback right: choose the next strategy and propose tools/context mutations after inspecting run feedback.
- Decision owner: model-driven competitor/coach/architect roles assembled by the first-party orchestrator, rather than the deterministic runner alone.
- Supporting / enforcement mechanisms: scenario executor, validators, model adapters, tournament, persisted run ledger and time/cost bounds.
- Closure path: strategy proposal → scenario actions/trials → measured outcome and analysis → subsequent model proposal or halted iteration.
- Boundary reachability: the installed `autoctx run/solve` CLI invokes `AgentOrchestrator.run_generation` through `stage_agent_generation` in the generation pipeline.
- Why this is / is not agent-owned: model outputs select nonfixed strategies and next actions; runtime gates constrain publication, not the creative operational choice.
- Evidence: pinned orchestrator, stages, CLI and generation pipeline above.
- Basis: explicit and structurally wired standard distribution.
- Confidence: high for the configured model-backed mode.
- Caveats: no external provider call or task-success claim was executed in this static assessment.

## S2 — Coordination

- State: C
- Function: attenuate competition and conflicting resource claims between simultaneously executing campaign S1 jobs.
- Disturbance / variety regulated: workers oversubscribing shared concurrency/capacity, duplicate dispatch, stale leases and retry races.
- Decisive decision or feedback right: allocate capacity-bounded leases and reservations, reject stale completion, reconcile expired leases, serialize or defer incompatible work.
- Decision owner: constructor-defined `CampaignScheduler` lease/resource algorithm rather than an independently negotiating model coordinator.
- Supporting / enforcement mechanisms: worker descriptors, global capacity, durable event replay, heartbeat, cancellation and retry state.
- Closure path: competing campaign claims → capability/resource reservation and lease assignment → result/timeout/retry recording → subsequent eligible dispatch and changed worker availability.
- Boundary reachability: opt-in packaged `autoctx campaign run` creates the scheduler and drives its lease/dispatch/complete/reconcile paths.
- Why this is / is not agent-owned: coordination choices use authored resource rules; they regulate real simultaneous scenario workers, not just route messages between named roles.
- Distinct S1 units: independent scenario/agent campaign jobs capable of model-led task actions.
- Inter-S1 disturbance: simultaneous jobs can contend for limited worker slots/capabilities and create duplicate or unaccounted external work after lost leases.
- Attenuating coordination relation: the central lease ledger and resource/capacity matching prevent overlapping claims and account for stale completions.
- Feedback into subsequent S1 behaviour: completed/expired/canceled leases and retryable failures update available slots and determine whether/where the next S1 job runs.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the reservation/lease protocol materially suppresses shared-resource interference across distinct running S1 cells.
- Evidence: pinned `campaign_scheduler.py` and runtime documentation above.
- Basis: structural and explicit.
- Confidence: medium; optional campaign mode.
- Caveats: resource allocation is deterministic and no autonomous S2 arbiter is credited.

## S3 — Inside-and-now control

- State: C
- Function: regulate current campaign commitments, scarce resources, continuation and deployment of evaluated harness variants.
- Disturbance / variety regulated: over-budget runs, stale worker commitments, unacceptable or inconclusive candidate evidence, and failed promotion checks.
- Decisive decision or feedback right: accept/rollback current generation, allocate/cancel campaign work, and keep incumbent versus activate an evaluated candidate.
- Decision owner: constructor-defined budget/gate, scheduler and promotion coordinator; model proposal roles do not own the final integrity/activation rule.
- Supporting / enforcement mechanisms: score/holdout records, candidate digests, run cost trackers, lease ledger, auditor signals and persistence.
- Closure path: whole-campaign scores, failures and capacity state → current gate/lease/promotion decision → persisted incumbent/work queue → next generation or dispatch under revised state.
- Boundary reachability: the standard generation pipeline invokes gates; optional campaign scheduling and bundle promotion are packaged supported flows with actual coordinator methods.
- Why this is / is not agent-owned: a proposed strategy alone does not override matched evaluation and promotion policies; final central control remains authored code.
- Whole-system current view: active generation results, candidate/incumbent comparisons, campaign lease state, failures, resource limits and budget.
- Current-control decision scope: whether present work continues, retries, pauses or rolls back, and whether a validated candidate becomes the current active context.
- Evidence: pinned generation pipeline, scheduler and bundle promotion module above.
- Basis: structural construction with explicit feedback return.
- Confidence: medium-high.
- Caveats: no independent managerial actor is inferred from the dashboard or nominal role names.

## S3* — Complementary audit

- State: A
- Function: independently challenge ordinary campaign integrity/promotion claims using a differently routed and constrained evidence review.
- Disturbance / variety regulated: leaked holdout information, evaluator drift, invalid comparisons, missing reconstruction evidence and unsupported causal assertions.
- Decisive decision or feedback right: issue a cited independent audit finding and severity recommendation on a sealed checkpoint packet.
- Decision owner: separately routed model auditor in the explicitly enabled `CampaignAuditor` mode; deterministic packet guards and policy translation are support.
- Supporting / enforcement mechanisms: redacted signed packet builder, distinct endpoint/model-route checks, bounded calls, durable finding store, severity-to-hold policy and operator disposition history.
- Closure path: live checkpoint evidence → distinct auditor judgment and cited finding → `review_required`/`safe_pause_recommended` policy outcome → coordinator retains incumbent/holds promotion until disposition or corrective handling.
- Boundary reachability: supported `AUTOCONTEXT_CAMPAIGN_AUDITOR_ENABLED` with context-bundle promotion or campaign CLI composes the checkpoint runner; `ContextBundlePromotionCoordinator` tests policy outcomes before activation.
- Why this is / is not agent-owned: unlike ordinary generator scores or the same-role skeptic, a separately configured model backend receives a restricted independent evidence packet and supplies a distinct judgment; it cannot itself rewrite scores or authorize promotion.
- Claim being audited: evidence integrity and promotion readiness of candidate context bundles/campaigns.
- Ordinary reporting path: tournament and deterministic gates record scores, comparisons, success/failure and candidate promotion eligibility.
- Complementary access path: sealed, allowlisted checkpoint metadata and artifact references constructed outside proposer outputs; the audit model reads this under a distinct route.
- Independence boundary: the configured auditor endpoint/model identity must differ from all proposer routes absent an explicit unsafe override; it has read-only access, fixed audit checkpoints and durable separate audit records.
- Who acts on findings: first-party promotion policy can hold the incumbent; operator or separately configured controller resolves deferred findings. No claim of independent write or final policy authority.
- Evidence: pinned campaign auditor, route checks, campaign auditor document and bundle promotion module above.
- Basis: explicit optional audit constructor and live corrective gate; not a claim that every default install runs an independent auditor.
- Confidence: medium; opt-in mode and policy configuration required.
- Caveats: if route distinction is deliberately overridden or the policy is merely advisory, the positive witness does not apply to that mode.

## S4 — Outside-and-then intelligence

- State: A
- Function: model-authored selection of future context/harness changes responsive to changing task/scenario performance rather than only fixing the current one-off answer.
- Disturbance / variety regulated: future task distribution, strategy transfer, scenario performance trends and evolving execution constraints.
- Decisive decision or feedback right: propose new playbook, tool, role-DAG or harness mutations from accumulated scenario outcomes and choose an adaptive candidate for future generations.
- Decision owner: model-backed analyst/coach/architect roles; the deterministic bundle validator/promoter governs when a proposed capability can become active.
- Supporting / enforcement mechanisms: run history and trajectory, context-bundle store, adaptive matched trials, held-out comparator, mutation parser and promotion gate.
- Closure path: external scenario results across generations → model analysis and future-oriented architecture/context proposal → staged candidate evaluation → active bundle change → changed tools/prompts/routing in subsequent operations.
- Boundary reachability: `stage_agent_generation` extracts architect changes and calls `propose_context_bundle`; the packaged coordinator evaluates/promotes candidates into active scenario context.
- Why this is / is not agent-owned: models select content and architecture options; built-in gates do not themselves create those options. This is restricted to prospective reuse across later generations, not a claim of market or whole-enterprise strategy.
- External distinction: held-out and matched scenario task outcomes are environmental evidence beyond the present model response and previous prompt text.
- Future / prospective distinction: generated context/role/tool mutations are constructed to change later task attempts rather than merely revise the just-completed answer.
- Adaptation option generated: a versioned candidate context bundle containing possible playbook, hint, tool, harness and routing changes.
- Path back into current capability / S3: promoted bundle becomes the active context selected by the next run; failed candidates leave the incumbent unchanged.
- Evidence: pinned generation stage and context-bundle promotion modules above.
- Basis: structural positive path in supported multi-generation model mode.
- Confidence: medium.
- Caveats: evidence is for task-distribution adaptation within the declared harness-evolution boundary, not proactive sensing of an external company strategy.

## S5 — Policy and identity

- State: —
- Function: no first-party legitimate authority is shown to decide the overall identity or ultimate priority hierarchy of the harness program.
- Disturbance / variety regulated: operator-specified purpose, model credentials, permitted tools, resource/risk constraints and audit-policy disputes.
- Decisive decision or feedback right: final identity/ultimate-policy arbitration belongs to the user/operator or owning institution outside this packaged runtime.
- Decision owner: external operator; configuration parsing, approvals and auditor dispositions are operational or quality controls.
- Supporting / enforcement mechanisms: API tokens, allowlists, workspace containment, policy settings, audit-disposition records.
- Closure path: an operator configures/approves a bounded run; no shipped constitutional-identity proposal → legitimate parent S5 decision → returned binding identity-policy change is established.
- Why this is / is not agent-owned: tools can block unauthorized operations and operators can resolve audit holds, but neither demonstrates that the runtime independently defines its legitimate purpose.
- Evidence: pinned CLI documentation, campaign auditor and control modules above.
- Basis: negative boundary and ownership test.
- Confidence: medium-high.
- Caveats: a larger deployment may implement a separate S5 parent; not inherited here.

### Absence scope

- Surfaces inspected: `autoctx` CLI/HTTP and model roles, campaign auditor/dispositions, scheduler policies, context-bundle approval and workspace permissions.
- Plausible first-party paths checked: auditor operator disposition as policy change, role-DAG adaptation as identity, context promotion as ultimate mandate, workspace permissions as final authority.
- Why no material first-party path remains: the cited paths manage bounded task capability, quality and execution policy under externally fixed objectives, without an identity-level legitimate decision and return loop at the declared boundary.

## Recursion

Individual scenario agent runs are subordinate operational cells within a continuing scenario/harness evolution program. Campaign workers are multiple S1 cells coordinated by the packaged resource protocol. No complete additional VSM recursion or organizational S5 is presumed from role names or hosted agents.

## Variety and escalation

Role proposals amplify the repertoire of candidate strategies. Tournament/gate thresholds, sealed evidence, held-out matching, budget rollback and leases attenuate unsafe execution variety. Severe auditor findings may hold promotion for an operator disposition; this is a bounded integrity escalation rather than an assumed S5 constitutional loop.

## Evidence gaps

- Static source and docs read at exact pinned commit only; no provider calls, real campaigns, live resource contention or deployment experiments were executed.
- `CampaignAuditor` autonomy and independent-route claim applies only to the opted-in distinct model route with enabled hold policy, not merely to the existence of a skeptic or deterministic verifier.
- S4 is bounded to prospective task/scenario capability changes; broader environmental foresight and independent ultimate policy remain unestablished.

## Assessment summary

**Canonical** `included`: first-party model-led S1; constructed cross-worker S2 and current S3; opt-in independently routed corrective audit S3*; model-origin prospective scenario/harness adaptation S4; no first-party S5 identity closure. Vector: **A · C · C · A · A · —**.

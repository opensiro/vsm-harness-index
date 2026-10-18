---
harness_id: rust-harness
project_name: Rust Harness
repository: https://github.com/majiayu000/harness
review_ref: 7f75dee2cb2eaf7195c9b8938ac76db691f1d157
reviewed_at: 2026-10-18
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: A
autonomy_s5: —
---

# Rust Harness

## Review boundary

- System in focus: The **first-party Rust Harness fleet product**, instantiated as an operator-configured project/fleet server with executable coding-agent adapters, durable workflow-runtime management, independent review activities, and optional signal-driven garbage-collection/learning. This is the managed software-development delivery fleet at one operator's project/control-plane recursion, **not** the maintainer's own GitHub development process or all hosted model/provider companies.
- Purpose and identity: Carry multiple bounded coding-agent tasks/workflows into reviewed software changes while enforcing eligibility, isolation, run limits, evidence and repair; optionally adapt future rules/skills from observed failures and quality signals.
- Relevant environment: Code repositories, user issues/PRs, CI/review threads, task acceptance criteria, dynamically occupied coding-agent slots, shared runtime profiles/daily spend caps, actual coding/tool results, quality events, changing policy/skill effectiveness and model/provider availability.
- Standard-distribution boundary: Shipped Rust `harness-cli`, `harness-server`, `harness-workflow`, `harness-agents`, `harness-gc`, `harness-rules` and `harness-skills` plus config and HTTP/operator/RPC surfaces; requires a configured external coding model/CLI, with Postgres for fleet mode. This is a supported executable first-party mode, not a runtime-free library claim. The model vendors supply inference, not automatic S3–S5 ownership.
- Credited operating / distribution surfaces: [codex_adapter.rs:1-95](https://github.com/majiayu000/harness/blob/7f75dee2cb2eaf7195c9b8938ac76db691f1d157/crates/harness-agents/src/codex_adapter.rs#L1-L95), [dispatcher.rs:139-335](https://github.com/majiayu000/harness/blob/7f75dee2cb2eaf7195c9b8938ac76db691f1d157/crates/harness-workflow/src/runtime/dispatcher.rs#L139-L335), [dispatcher_throttle.rs:38-127](https://github.com/majiayu000/harness/blob/7f75dee2cb2eaf7195c9b8938ac76db691f1d157/crates/harness-workflow/src/runtime/dispatcher_throttle.rs#L38-L127), [pr_feedback.rs:301-428](https://github.com/majiayu000/harness/blob/7f75dee2cb2eaf7195c9b8938ac76db691f1d157/crates/harness-workflow/src/runtime/pr_feedback.rs#L301-L428), [mod.rs:580-605](https://github.com/majiayu000/harness/blob/7f75dee2cb2eaf7195c9b8938ac76db691f1d157/crates/harness-server/src/workflow_runtime_worker/prompt_packet/mod.rs#L580-L605), [mod.rs:167-273](https://github.com/majiayu000/harness/blob/7f75dee2cb2eaf7195c9b8938ac76db691f1d157/crates/harness-server/src/handlers/operator_monitor/mod.rs#L167-L273), [gc_agent.rs:106-222](https://github.com/majiayu000/harness/blob/7f75dee2cb2eaf7195c9b8938ac76db691f1d157/crates/harness-gc/src/gc_agent.rs#L106-L222), [gc_agent.rs:260-363](https://github.com/majiayu000/harness/blob/7f75dee2cb2eaf7195c9b8938ac76db691f1d157/crates/harness-gc/src/gc_agent.rs#L260-L363), [quality_trigger.rs:320-415](https://github.com/majiayu000/harness/blob/7f75dee2cb2eaf7195c9b8938ac76db691f1d157/crates/harness-server/src/quality_trigger.rs#L320-L415), [learn.rs:13-84](https://github.com/majiayu000/harness/blob/7f75dee2cb2eaf7195c9b8938ac76db691f1d157/crates/harness-server/src/handlers/learn.rs#L13-L84), [self_evolution.rs:25-103](https://github.com/majiayu000/harness/blob/7f75dee2cb2eaf7195c9b8938ac76db691f1d157/crates/harness-server/src/self_evolution.rs#L25-L103).
- Adjacent first-party surfaces excluded from ownership: Repository's own issue/PR/RFC/CI authorship and proposed designs, documented benchmark claims and screenshots, external Claude/Codex/OpenCode organization, provider-level agent policy, adopters' independently run operations and project owners' unrelated corporate governance. Mere config/policy metadata and dashboard interfaces do not inherit function autonomy.
- First-party operating/deployment modes considered: Single `harness exec` coding-agent action with credential/sandbox prerequisite; Postgres-backed fleet workflow submission/dispatch and local review/rework; periodic review as separate model-backed inspection of commit windows; quality-triggered GC with `auto_adopt=rules-only` and periodic adopted-draft rule learning; operator-managed fleet monitor and cancellation/unblock/retry.
- Recursion level: One software-delivery fleet and its separately executing coding agents as operational S1 work. Process and profile scheduling, independent review and potential harness rule/skill redesign are considered against the same first-party product boundary.
- Reviewed revision: `7f75dee2cb2eaf7195c9b8938ac76db691f1d157`, frozen in [intake #1699](https://github.com/opensiro/vsm-harness-index/issues/1699) and [active batch #1700](https://github.com/opensiro/vsm-harness-index/issues/1700).
- Observation date: 2026-10-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Rust workspace `Cargo.toml` registers 13 source crates, MIT licensing and the operator-driven first-party CLI and fleet server. The README supports a real coding task with an explicitly provisioned provider and scope-bound tools, plus a separate durable server mode with Postgres and authenticated workflow-submission and operator actions. `harness-agents` actually launches/supervises Claude/Codex/OpenCode adapters; `harness-workflow` schedules their durable runtime activities; `harness-server` reconciles artifacts, PR facts and agent reviews. These services wrap external model inference but retain source-owned process/return boundaries. [README](https://github.com/majiayu000/harness/blob/7f75dee2cb2eaf7195c9b8938ac76db691f1d157/README.md), [codex_adapter.rs:235-330](https://github.com/majiayu000/harness/blob/7f75dee2cb2eaf7195c9b8938ac76db691f1d157/crates/harness-agents/src/codex_adapter.rs#L235-L330), [dispatcher.rs:139-335](https://github.com/majiayu000/harness/blob/7f75dee2cb2eaf7195c9b8938ac76db691f1d157/crates/harness-workflow/src/runtime/dispatcher.rs#L139-L335).

For resource contention, a configured daily-profile budget throttle consults spent cost and pending commands for an *alternative* runtime profile. If a claimable alternative remains below its band, the busier profile yields a dispatch turn in enforce mode; `Shadow` logs the same hypothetical outcome without changing dispatch. This is a real return into separate agent workflow processing rather than an abstract task sequence, but thresholds and profile identity are configured by the operator and no autonomous policy-setter negotiates an inter-S1 accord. [dispatcher_throttle.rs:1-127](https://github.com/majiayu000/harness/blob/7f75dee2cb2eaf7195c9b8938ac76db691f1d157/crates/harness-workflow/src/runtime/dispatcher_throttle.rs#L1-L127), [dispatcher.rs:375-500](https://github.com/majiayu000/harness/blob/7f75dee2cb2eaf7195c9b8938ac76db691f1d157/crates/harness-workflow/src/runtime/dispatcher.rs#L375-L500).

PR delivery has an independent local-review step after implementation/repair; the review prompt demands raw inspection of the current PR head in a clean worktree against original requirements, SHA and evidence, refusing success on a stale/dirty head. A `LocalReviewChangesRequested` finding triggers a new `address_pr_feedback` activity; `Blocked` blocks current completion. In a separate optional periodic review mode, the server calls a reviewer agent over newly observed commits (and optionally a different secondary reviewer in Cross mode) with corrective evidence. Only the *closed return* from the first path is credited in the S3* positive. [pr_feedback.rs:301-428](https://github.com/majiayu000/harness/blob/7f75dee2cb2eaf7195c9b8938ac76db691f1d157/crates/harness-workflow/src/runtime/pr_feedback.rs#L301-L428), [mod.rs:580-605](https://github.com/majiayu000/harness/blob/7f75dee2cb2eaf7195c9b8938ac76db691f1d157/crates/harness-server/src/workflow_runtime_worker/prompt_packet/mod.rs#L580-L605), [tick.rs:105-220](https://github.com/majiayu000/harness/blob/7f75dee2cb2eaf7195c9b8938ac76db691f1d157/crates/harness-server/src/periodic_reviewer/tick.rs#L105-L220).

Source signals from completion logs, rule violations and quality score feed `GcAgent.run`, which independently invokes the configured model-backed agent to write bounded future remediation drafts. An operator can manually adopt; additionally the **optional** `AutoAdoptPolicy::RulesOnly` mode accepts only eligible rule artifacts under a configured project-relative prefix. The configured periodic `self_evolution` tick uses already adopted drafts to solicit model-generated rules and inserts these into the live first-party rules engine. This makes a supported proposal → governed adaptation → subsequent runtime rule-capability return; it does not prove the default (off) is self-modifying or that all draft formats go live. [gc_agent.rs:106-222](https://github.com/majiayu000/harness/blob/7f75dee2cb2eaf7195c9b8938ac76db691f1d157/crates/harness-gc/src/gc_agent.rs#L106-L222), [gc_agent.rs:260-363](https://github.com/majiayu000/harness/blob/7f75dee2cb2eaf7195c9b8938ac76db691f1d157/crates/harness-gc/src/gc_agent.rs#L260-L363), [quality_trigger.rs:320-415](https://github.com/majiayu000/harness/blob/7f75dee2cb2eaf7195c9b8938ac76db691f1d157/crates/harness-server/src/quality_trigger.rs#L320-L415), [self_evolution.rs:25-103](https://github.com/majiayu000/harness/blob/7f75dee2cb2eaf7195c9b8938ac76db691f1d157/crates/harness-server/src/self_evolution.rs#L25-L103), [learn.rs:13-84](https://github.com/majiayu000/harness/blob/7f75dee2cb2eaf7195c9b8938ac76db691f1d157/crates/harness-server/src/handlers/learn.rs#L13-L84), [misc.rs:180-235](https://github.com/majiayu000/harness/blob/7f75dee2cb2eaf7195c9b8938ac76db691f1d157/crates/harness-core/src/config/misc.rs#L180-L235).

The operator-monitor cockpit provides cross-workflow current status, runtime-host health, queue capacity, stalled/error groups and action surfaces for specific submissions. Operator-authenticated cancel, unblock, retry and merge can intervene in a workflow, but no sourced decision trace binds a *whole-fleet* view to a genuine shared-commitment/resource bargaining choice. The dashboard is therefore enforcement/reporting and a potential parent intervention surface, **not** an inherited positive S3 or S5 here. [mod.rs:167-275](https://github.com/majiayu000/harness/blob/7f75dee2cb2eaf7195c9b8938ac76db691f1d157/crates/harness-server/src/handlers/operator_monitor/mod.rs#L167-L275), [mod.rs:486-575](https://github.com/majiayu000/harness/blob/7f75dee2cb2eaf7195c9b8938ac76db691f1d157/crates/harness-server/src/handlers/operator_monitor/mod.rs#L486-L575), [API contract](https://github.com/majiayu000/harness/blob/7f75dee2cb2eaf7195c9b8938ac76db691f1d157/docs/api-contract.md).

## Operational model

Individual coding-agent instances carry task instructions into repository work and receive actual tool/file feedback (S1). With several such agents, shared profile capacity can create job-level interference; first-party configurable throttling is a function-specific constructor path (S2=C) but not autonomous coordination policy ownership. A separate independently prompted reviewer examines raw current code and can force new current work or hold merge (S3*=A). Quality/failure signals can induce a model-generated future rule and optional auto-adoption; those rules later affect the running engine (S4=A in opt-in mode). No source-backed whole-current S3 decision-owner or ultimate S5 legitimacy loop is established.

## S1 — Operations

- State: A
- Function: Produce coding changes or analyses by running environment-coupled external-model-backed coding agents under the first-party harness lifecycle.
- Disturbance / variety regulated: Novel issue requirements, source/test failures, changing repository files and live agent/tool return results.
- Decisive decision or feedback right: The configured coding model selects relevant next edits/tools and incorporates results; first-party adapter/session/process creates the executable environment and returns output/evidence.
- Decision owner: Project-registered coding-agent runtime actor instantiated through supported Claude/Codex/OpenCode adapters. External provider supplies inference service; the agent task operates within Harness' managed execution boundary.
- Supporting / enforcement mechanisms: `harness exec`, tool/permission scope, agent spawn supervisor, sandbox/proxy, workflow runtime job, attempt/lease record and result.
- Closure path: User issue/instruction → agent adapter launch → model-chosen action/tool → repository/file observation → subsequent agent step → recorded task artifact/PR outcome.
- Boundary reachability: Shipped CLI quickstart runs actual coding agent, and fleet dispatcher enqueues registered runtime activity to the source adapter; absent provider access would block execution rather than silently replace agent choice with a fake internal model.
- Why this is / is not agent-owned: Source code supplies boundaries and enforces permissions; the model-backed coding actor chooses context-dependent edits, unlike a deterministic prewritten macro.
- Evidence: [codex_adapter.rs:235-330](https://github.com/majiayu000/harness/blob/7f75dee2cb2eaf7195c9b8938ac76db691f1d157/crates/harness-agents/src/codex_adapter.rs#L235-L330), [spawn_supervisor.rs:1-135](https://github.com/majiayu000/harness/blob/7f75dee2cb2eaf7195c9b8938ac76db691f1d157/crates/harness-agents/src/spawn_supervisor.rs#L1-L135), [dispatcher.rs:139-335](https://github.com/majiayu000/harness/blob/7f75dee2cb2eaf7195c9b8938ac76db691f1d157/crates/harness-workflow/src/runtime/dispatcher.rs#L139-L335), [README quickstart](https://github.com/majiayu000/harness/blob/7f75dee2cb2eaf7195c9b8938ac76db691f1d157/README.md).
- Basis: Explicit model/agent/task return path in actual supported deployment.
- Confidence: High source-structural, no hosted provider execution run for this assessment.
- Caveats: Provider tool auth/sandbox are prerequisites; static policy denial does not independently perform coding work.

## S2 — Coordination

- State: C
- Function: Attenuate resource contention/priority crowding between separately running agent workflows sharing a constrained runtime-profile daily budget.
- Disturbance / variety regulated: Concurrent claimable work under different runtime profiles can exhaust shared profile-specific budget bands or starve lower-usage profiles, creating unfair cross-agent dispatch competition.
- Decisive decision or feedback right: A configurable policy chooses runtime profile limits and `daily_throttle_ratio`; first-party dispatcher senses usage and an alternative claimable profile and then defers the over-threshold profile's command in `Enforce` mode.
- Decision owner: The operator owns threshold/prioritization policy; first-party dispatcher implements a **function-specific composition contract**, not a model-owned discretionary negotiation.
- Supporting / enforcement mechanisms: `RuntimeProfileSelector`, shared usage accounting, `peek_claimable_commands`, throttle-band detector, dispatch barrier/defer backoff and shadow/event auditing.
- Closure path: Multiple independently executing agent workflows → competing runtime-profile budget spend and claimable commands → below-threshold alternative detected → overused profile command deferred with reason → other profile can obtain dispatch → affected agent tasks execute in revised order.
- Boundary reachability: Source-owned `RuntimeCommandDispatcher::dispatch_command` calls `budget_gate_outcome`; in `Enforce` mode calls `defer_claimed_command_if_owned`, with a separate `Shadow` mode explicitly marked non-enforcing. This path is a shipped runtime fleet feature, not only a test.
- Why this is / is not agent-owned: The threshold and fairness criterion are human-configured, and the dispatcher executes that criterion. The first-party source supplies a real cross-workflow interference-to-return path, but not a credited autonomous owner of S2 deliberation; hence constructor `C`, not `A`.
- Distinct S1 units: At least two concurrently claimable distinct coding-agent runtime jobs/workflows, potentially assigned different provider/runtime profiles.
- Inter-S1 disturbance: Saturating one active profile in shared dispatch slots while alternative active agent work is below its budget/usage band.
- Attenuating coordination relation: Configured `daily_throttle_breach` compares profile spend and selectable pending alternative then conditionally yields/defers a dispatch slot to avoid starvation.
- Feedback into subsequent S1 behaviour: Enforce-mode `defer_claimed_command_if_owned` applies a barrier/backoff, allowing an under-threshold task to proceed first.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: It uses measured inter-profile resource competition and reorders work based on **other live claimable actors** rather than merely following a hard-coded DAG or static dependency.
- Evidence: [dispatcher_throttle.rs:1-127](https://github.com/majiayu000/harness/blob/7f75dee2cb2eaf7195c9b8938ac76db691f1d157/crates/harness-workflow/src/runtime/dispatcher_throttle.rs#L1-L127), [dispatcher.rs:375-500](https://github.com/majiayu000/harness/blob/7f75dee2cb2eaf7195c9b8938ac76db691f1d157/crates/harness-workflow/src/runtime/dispatcher.rs#L375-L500), [dispatcher.rs:139-335](https://github.com/majiayu000/harness/blob/7f75dee2cb2eaf7195c9b8938ac76db691f1d157/crates/harness-workflow/src/runtime/dispatcher.rs#L139-L335).
- Basis: Bounded constructible mutual coordination path with present enforcement wiring; owner config must supply policy.
- Confidence: Medium for functional S2; distinct profile workload is supported but actual live contention not reproduced.
- Caveats: If only one task/profile exists, nothing is mutually coordinated; `Shadow` does not enforce S2, and threshold policy does not originate autonomously.

## S3 — Inside-and-now control

- State: —
- Function: No evidenced legitimate whole-current manager that makes binding tradeoffs across separate viable delivery units' competing live commitments using a whole-system view.
- Disturbance / variety regulated: Fleet cost/capacity pressure, PR/review backlog, stalled tasks and runtime-host outages, mostly handled by configured local barriers and per-workflow support.
- Decisive decision or feedback right: Operator-configured budget ceilings and per-workflow cancel/unblock/retry are supported; no concrete cross-unit commitment/priority decision source uses a whole-current view and closes such a choice.
- Decision owner: Operator for global threshold configuration and local intervention, deterministic workflow/dispatch machinery for applying them; not a first-party autonomous S3 governor or proven parent-owned S3-specific transaction at this recursion.
- Supporting / enforcement mechanisms: Operator monitor, aggregate workflow health/status, registered runtime hosts, configured daily caps, queue budgets, status/repair control APIs.
- Closure path: Workflow issue → per-workflow action; missing established fleet-level shared-commitment judgement based on whole-current status → allocated/renegotiated division resources → observed changed collective operation.
- Why this is / is not agent-owned: Observability and strong command execution alone do not demonstrate who decides system-wide resource bargains. The adaptive dispatch path addresses S2 contention under fixed limits, not S3 strategy for all commitments.
- Whole-system current view: Runtime monitor aggregates active workflow states, action eligibilities, capacity and host health, but that is a **support view**, not itself a decision right.
- Current-control decision scope: Configured workload budget and individual workflow cancellation/retry; insufficient evidence of actual whole-fleet priority/commitment reallocation tied to that view.
- Evidence: [mod.rs:167-275](https://github.com/majiayu000/harness/blob/7f75dee2cb2eaf7195c9b8938ac76db691f1d157/crates/harness-server/src/handlers/operator_monitor/mod.rs#L167-L275), [mod.rs:486-575](https://github.com/majiayu000/harness/blob/7f75dee2cb2eaf7195c9b8938ac76db691f1d157/crates/harness-server/src/handlers/operator_monitor/mod.rs#L486-L575), [dispatcher.rs:375-500](https://github.com/majiayu000/harness/blob/7f75dee2cb2eaf7195c9b8938ac76db691f1d157/crates/harness-workflow/src/runtime/dispatcher.rs#L375-L500), [API contract](https://github.com/majiayu000/harness/blob/7f75dee2cb2eaf7195c9b8938ac76db691f1d157/docs/api-contract.md).
- Basis: Source-bounded absence of whole-current decision/closure under the examined modes.
- Confidence: Medium; the operator UI is a credible future parent S3 surface but cannot be graded positive solely for existing.
- Caveats: A human operator in an independently managed organization may use this cockpit for S3, but their unobserved off-platform governance cannot be credited here.

### Absence scope

- Surfaces inspected: Operator monitor and aggregate dashboard, runtime budget/profile policy, worker/dispatcher, workflow decision engine and operator submission controls.
- Plausible first-party paths checked: Whole-fleet current-control model decisions, rule-governed resource reallocation, human parent priority intervention returned to multiple ongoing S1 commitments, agent contract arbitration.
- Why no material first-party path remains: Reviewed code provides current status and controls for particular workflows plus preconfigured resource ceilings. It does not demonstrate an in-boundary binding **whole-current** decision made from cross-unit claims and returned across separate viable operating commitments.

## S3* — Complementary audit

- State: A
- Function: Obtain independent current reality about model-agent-delivered coding work beyond the implementing agent's own completion summary and force corrective action before integration.
- Disturbance / variety regulated: Erroneous claims of completed implementation, stale/dirty PR head, skipped requirements, faulty code, unresolved review threads, unvalidated changes.
- Decisive decision or feedback right: Separately invoked model-backed local reviewer inspects current repository head and original requirements, independently decides pass/changes/blocked and returns findings; first-party reducer moves the workflow accordingly.
- Decision owner: Model-backed **review agent** in the separate local-review activity with independent review context; deterministic validation of signal/head/CI and GitHub snapshot is enforcement rather than the substantive model review.
- Supporting / enforcement mechanisms: Review activity, current-head SHA/clean-tree evidence, separate read-only review prompt, structured findings/signals, review-state reducer, queued repair task and exact-head readiness requirements.
- Closure path: Implementer claims PR ready → independent local-review activity obtains current source/head and initial issue plan → `LocalReviewChangesRequested` or `Blocked` → workflow `addressing_feedback` with new remediation agent activity, or blocked → repaired current PR → new review/merge gate.
- Boundary reachability: The shipped `github_issue_pr` flow enqueues `run_local_review` at a dedicated state, consumes `LocalReviewOutcome` and triggers `address_pr_feedback` on findings, while a separate direct local reviewer runtime is supported. Not borrowed only from an external CI job.
- Why this is / is not agent-owned: Model reviewer examines raw current PR independently and originates substantive findings; source-only signal parsing enforces the resulting audit decision and returns it.
- Claim being audited: Agent-written completion/current PR readiness against original requirements and verified worktree at a specific commit.
- Ordinary reporting path: Implementing coding agent's task/artifact/PR repair summary and claimed completion/validation.
- Complementary access path: A separate fresh-context model-backed reviewer receives actual PR head/issue plan, checks working tree and evidence, and can refuse to accept the author's unsupported assertion.
- Independence boundary: Separate activity/reviewer task from agent implementation and repair; independent review instructions explicitly require treating prior repairs as claims. The same provider family could be configured in two jobs, so independence is procedural, not guaranteed vendor separation.
- Who acts on findings: The first-party workflow reducer queues further `address_pr_feedback`, blocks or withholds readiness and can repeat local review before merge.
- Evidence: [pr_feedback.rs:301-428](https://github.com/majiayu000/harness/blob/7f75dee2cb2eaf7195c9b8938ac76db691f1d157/crates/harness-workflow/src/runtime/pr_feedback.rs#L301-L428), [mod.rs:580-605](https://github.com/majiayu000/harness/blob/7f75dee2cb2eaf7195c9b8938ac76db691f1d157/crates/harness-server/src/workflow_runtime_worker/prompt_packet/mod.rs#L580-L605), [tick.rs:105-220](https://github.com/majiayu000/harness/blob/7f75dee2cb2eaf7195c9b8938ac76db691f1d157/crates/harness-server/src/periodic_reviewer/tick.rs#L105-L220).
- Basis: Separate inquiry and authoritative blocking/correction return into current coding work, beyond routine implementer self-report.
- Confidence: Medium-high source-structural; actual live PR review not run in this assessment.
- Caveats: Ordinary tests/CI alone would not establish S3*. Optional periodic review may corroborate but is not required for this independent local-review closed path.

## S4 — Outside-and-then intelligence

- State: A
- Function: Observe repeated quality/environment failures, generate future-oriented new rule/skill or guard options, then allow valid learned policy to change subsequent harness operation.
- Disturbance / variety regulated: Changing repository/project error patterns, repeated rule violations, chronic blockers, slow sessions and code hotspots exceed static prior protections.
- Decisive decision or feedback right: A configured GC coding agent examines gathered signals and chooses future remediation artifact content; bounded optional rules-only auto-adoption writes accepted artifacts, then scheduled first-party learning constructs rules into the current rules engine.
- Decision owner: Model-backed GC adaptation agent for content selection; operator's standing `rules-only` path/prefix policy is a limit, not the individual remediation choice. First-party live `learn_rules` model call can further select executable rule candidates.
- Supporting / enforcement mechanisms: EventStore and scan checkpoint, signal detector and priority ranking, GC AgentRequest tool/budget limits, draft store, status/Pending/Adopted transitions, rule-only path gates, periodic self_evolution and rules-engine insertion.
- Closure path: Prior recurring warnings/violations from real operation → sampled/aggregated signal → model-backed GC draft proposal → `auto_adopt_matching` in opt-in `RulesOnly` mode and project-path validation → adopted draft → periodic `learn_rules` agent produces parsed rules → rules engine `add_rule` → new operational checks in later coding workflows.
- Boundary reachability: `QualityTrigger` grades post-task observations and calls `GcAgent.run`; its optional `auto_adopt` policy calls real filesystem adoption. The bundled server `self_evolution::start` schedules `learn_rules`; handler reads adopted drafts and installs rule definitions into live engine. This is a shipped executable opt-in route, not a roadmap.
- Why this is / is not agent-owned: Hard-coded thresholds and parsers alone would not generate new context-sensitive remediations from emergent external errors. Source invokes a coding agent with observed signals, and separately a learning agent to turn adopted evidence into rules.
- External distinction: Observed project execution quality, repository error patterns and recurring agent/tool failures outside the previous rule coverage.
- Future / prospective distinction: Drafted guards/rules/skills are for *later* workflows, not merely retrying the same failed tool action. Adopted rule content changes subsequently enforced capability.
- Adaptation option generated: New rule/guard/skill remediation derived from prior empirical warnings, with rules-only automatic adoption supported; defaults remain conservative and do **not** auto-adopt.
- Path back into current capability / S3: Generated GC rule draft → bounded adoption → agent-extracted rule → `state.engines.rules.write().await.add_rule` → later code-validation/rule-check operations (S1). There is no fabricated autonomous S3 just to close S4.
- Evidence: [gc_agent.rs:106-222](https://github.com/majiayu000/harness/blob/7f75dee2cb2eaf7195c9b8938ac76db691f1d157/crates/harness-gc/src/gc_agent.rs#L106-L222), [gc_agent.rs:260-363](https://github.com/majiayu000/harness/blob/7f75dee2cb2eaf7195c9b8938ac76db691f1d157/crates/harness-gc/src/gc_agent.rs#L260-L363), [quality_trigger.rs:320-415](https://github.com/majiayu000/harness/blob/7f75dee2cb2eaf7195c9b8938ac76db691f1d157/crates/harness-server/src/quality_trigger.rs#L320-L415), [learn.rs:13-84](https://github.com/majiayu000/harness/blob/7f75dee2cb2eaf7195c9b8938ac76db691f1d157/crates/harness-server/src/handlers/learn.rs#L13-L84), [self_evolution.rs:25-103](https://github.com/majiayu000/harness/blob/7f75dee2cb2eaf7195c9b8938ac76db691f1d157/crates/harness-server/src/self_evolution.rs#L25-L103), [misc.rs:180-235](https://github.com/majiayu000/harness/blob/7f75dee2cb2eaf7195c9b8938ac76db691f1d157/crates/harness-core/src/config/misc.rs#L180-L235).
- Basis: Model-selected prospective remedies reach a future runtime rule engine through shipped opt-in closure.
- Confidence: Medium source-structural due to opt-in config and dependency on actual newly generated artifact validity.
- Caveats: Default `Off` leaves pending drafts; no source claims the model always emits path-qualified eligible rule artifacts; runtime hosted inference and efficacy improvements not replicated.

## S5 — Policy and identity

- State: —
- Function: No evidenced ultimate identity/purpose constitutional arbitration with legitimate authority and actual return into global organizational policy.
- Disturbance / variety regulated: Credential/network scope, project identity, task permissions, workflow configuration and merge authorization control *execution safety*, not the fundamental purpose/identity of the delivery organization.
- Decisive decision or feedback right: Project operators configure credentials and standing rules and may approve a merge, but no in-boundary S5 actor resolves a purpose/identity conflict at the stated recursion.
- Decision owner: External platform adopters set organizational mission; shipped runtime's rule engine, authentication and isolated tool permissions enforce delegated limits.
- Supporting / enforcement mechanisms: HTTP auth, agent capability contracts, workflow definitions, Starlark rules and execution sandbox.
- Closure path: Operator config → policy enforcement; no detected identity crisis/proposal → ultimate legitimate authority → returned revised purpose guiding future cross-system operation.
- Why this is / is not agent-owned: A gate that blocks access or asks for approval cannot turn into final constitutional authority merely because it is cryptographically or procedurally enforced.
- Evidence: [workflow.rs:72-95](https://github.com/majiayu000/harness/blob/7f75dee2cb2eaf7195c9b8938ac76db691f1d157/crates/harness-core/src/config/workflow.rs#L72-L95), [misc.rs:180-235](https://github.com/majiayu000/harness/blob/7f75dee2cb2eaf7195c9b8938ac76db691f1d157/crates/harness-core/src/config/misc.rs#L180-L235), [API contract](https://github.com/majiayu000/harness/blob/7f75dee2cb2eaf7195c9b8938ac76db691f1d157/docs/api-contract.md), [dispatcher.rs:139-335](https://github.com/majiayu000/harness/blob/7f75dee2cb2eaf7195c9b8938ac76db691f1d157/crates/harness-workflow/src/runtime/dispatcher.rs#L139-L335).
- Basis: First-party supported boundary absence, not an impossibility for a larger real organization.
- Confidence: Medium-high.
- Caveats: Adopter corporate governance and contributor authorization are outside the first-party source boundary.

### Absence scope

- Surfaces inspected: Authenticated operator/admin API, project/workflow identity contracts, sandbox/security policy, workflow configuration and review/merge approval.
- Plausible first-party paths checked: Identity-policy conflict escalation, legitimate parent ultimate-policy adjudication with return, autonomous agent-defined organizational purpose changes.
- Why no material first-party path remains: Existing modes set or enforce delegated task and platform restrictions. No concrete ultimate-purpose conflict with a distinct rightful decision owner and returned organization-wide resolution is evidenced.

## Recursion

The fleet contains independent coding-agent tasks and separate source-backed audit/adaptation subsystems, but a spawned worker or model API is not automatically a viable S1 organization. At the declared fleet recursion S2's policy-composed profile fairness is narrower than S3, and optional GC future rules are distinct from current task repair. Nested independent customer organizations are not mapped.

## Variety and escalation

Environment/tool and CI results provide operational feedback; under-threshold profile comparisons damp inter-agent resource pressure; local independent review can block/repair untrusted completion claims; signal-driven GC learns prospective runtime rules. Alerts/operator actions route ordinary current task exceptions but do not themselves prove an independent S3 or S5 authority.

## Evidence gaps

- Frozen repository at `7f75dee2cb2eaf7195c9b8938ac76db691f1d157`, 13 Cargo workspace crates and MIT license. This isolated execution environment had **no `cargo` or `rustc`**, so full Rust compile/tests and real provider-backed task runs were **not performed**. Source evidence comes from immutable code and shipped docs/tests; Index contract/tests remain separately executable.
- S2=C requires opt-in enforced budget fairness and distinct profile candidates; mere queue presence or `Shadow` does not count. No autonomous S2 policy owner is credited.
- S3 is not granted from a telemetry cockpit, policy caps, or per-workflow operator approvals without sourced whole-current resource/commitment decision.
- S3*=A relies on independently prompted review and actionable return, not a routine validation check alone.
- S4=A is optional; default auto-adoption is Off, and learned future rule usage is not proof that every draft or hosted experiment succeeds.


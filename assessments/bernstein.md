---
harness_id: bernstein
project_name: Bernstein
repository: https://github.com/sipyourdrink-ltd/bernstein
review_ref: c3d317385a058ae2b5f478399373d09d84d80962
reviewed_at: 2026-09-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-29
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: C
autonomy_s5: P
---

# Bernstein

## Review boundary

- System in focus: one first-party Bernstein governed agent run at pinned revision `c3d317385a058ae2b5f478399373d09d84d80962`, including its task server, deterministic scheduler/orchestrator, first-party ManagerAgent, supported agent adapters, worktree/task-ownership controls, janitor/gate/cross-model verification paths, self-evolution primitives, governance playbook/signature path, lineage/audit spine and run-control surfaces.
- Purpose and identity: govern and orchestrate autonomous software-agent work under declarative task, role, policy, budget, quality and evidence constraints while retaining a replayable record of what was decided, executed, verified and admitted.
- Relevant environment: target repositories and worktrees; user goals and plans; model/provider responses; supported external coding-agent runtimes; OpenAI Agents SDK execution mode; MCP/tools; test/build/security signals; cost and task metrics; repository-health observations; operator-signed governance playbooks and parent decisions.
- Standard-distribution boundary: shipped Bernstein Python runtime/CLI/server, bundled ManagerAgent, built-in adapters including the documented `openai_agents` runner, task/worktree scheduler, janitor and quality pipeline, cross-model verifier, evolution package, governance commands/artifacts and lineage machinery at the frozen revision. External model endpoints, optional provider SDK internals, third-party coding-agent CLIs, target repositories and external MCP/services remain dependencies. A positive state is credited only where Bernstein supplies a first-party supported operating path around those dependencies rather than inheriting an adjacent product's organizational role by name.
- Credited operating / distribution surfaces: ordinary `bernstein run` orchestration; manager planning and queue review; task server and deterministic scheduler; supported `openai_agents` execution mode; per-task worktrees/file-ownership checks; janitor/gate pipeline; optional first-party cross-model verifier; evolution detector/proposal/executor constructors; `govern discover`/proposal/signature/apply contract; signed lineage/audit and replay surfaces.
- Adjacent first-party surfaces excluded from ownership: repository-development CI/tests, contributor/release governance, issue/PR process, examples that are not reachable through a shipped runtime primitive, and implementation roadmaps. External CLI-agent internals and provider/model inference engines do not donate S3/S4/S5 ownership merely because Bernstein can spawn or observe them.
- First-party operating / deployment modes considered: normal multi-task governed runs; multiple isolated workers; documented `openai_agents` adapter mode; manager decomposition/replanning/queue-review mode; janitor plus configured cross-model review; self-evolution constructors over recorded metrics/observability snapshots; model-assisted governance drafting with mandatory human signature; replay/audit/governance verification.
- Recursion level: one Bernstein governed run/organization around one declared goal and its task graph. Distinct operational workers are S1 units inside that run; the ManagerAgent is evaluated at the same recursion for whole-run current control rather than being relabelled as an S1 worker. Human governance-playbook authority is treated as a parent mode over this run organization.
- Reviewed revision: `c3d317385a058ae2b5f478399373d09d84d80962`.
- Observation date: 2026-09-29.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Bernstein deliberately separates deterministic orchestration from model-owned judgments. The scheduler, claims, lifecycle transitions, worktree setup, retry ceilings and many enforcement gates are ordinary Python. The first-party `ManagerAgent`, however, performs explicit LLM-mediated organizational decisions: it decomposes goals, reviews completed work, replans and periodically reviews the live task queue. Queue review is triggered by accumulated completions, any failure or a stall interval, sees the current queue and budget state, and returns typed corrections such as `reassign`, `cancel`, `change_priority` and `add_task`; the orchestrator validates and applies those corrections through the task server. This is a closed current-control loop rather than manager naming alone.

Operational S1 is reachable through a supported first-party mode. Bernstein's documented `openai_agents` adapter is not merely an opaque terminal-wrapper: the shipped runner constructs an OpenAI Agents SDK `Agent`, configures model/tools/sandbox/MCP context and invokes `Runner.run_sync`, whose internal turn loop performs model/tool interaction and emits tool/result/session events back through Bernstein's lifecycle and cost/audit paths. The SDK and model remain dependencies, but the mode is intentionally exposed by Bernstein's adapter and normal plan configuration. Opaque Claude/Codex-style CLI adapters are not needed to establish the positive S1 witness.

Bernstein supplies a concrete S2-specific interference relation around plural workers. Before spawning a batch, task lifecycle code compares explicit `owned_files` and inferred target paths against first-party file ownership for live agents, and additionally inspects active worktree diffs for hot files. An overlapping batch is not spawned. Workers run in separate worktrees, and merge/incremental-merge paths serialize admission and refuse dirty/conflicting target state. This materially attenuates concurrent-edit collision and feeds the result back by delaying which S1 task may start or land. The attenuation policy is deterministic rather than agent-decided, so the ownership state is constructor `C`, not `A`.

The S3* path is stronger than ordinary tests or audit logging. Bernstein ships a cross-model verifier explicitly implementing `writer != reviewer`: it obtains the completed task's actual git diff, selects a different reviewer model (with collision checks on explicit overrides), asks for an approve/request-changes judgment, can use multi-model quorum, and—when blocking is enabled—prevents merge and sends the finding into a corrective path. This is materially complementary access to operational reality, an independent model axis and an autonomous audit judgment whose result changes subsequent execution. The mode is configurable/off by default, but it is a first-party supported runtime mode; default enablement is not required for `A`.

The evolution subsystem establishes a narrow S4 constructor, not a closed autonomous S4 owner. `OpportunityDetector` can derive adaptation opportunities from recent cost/quality/failure history and, when supplied an observability-snapshot directory, from external repository-health security/coverage regressions. `ProposalGenerator` turns those distinctions into concrete policy/routing/model/template/provider upgrade proposals, while the evolution coordinator/executor supplies risk-stratified approval/execution/rollback machinery. The default `AnalysisEngine`, however, constructs its detector without the external observability snapshot input, and the decisive adaptation path is heuristic/configured rather than owned by a first-party autonomous intelligence actor. A developer/operator must compose the external sensing and autonomous authority/closure, so S4 is `C`.

S5 is parent-governed. The governance subsystem distinguishes an LLM drafting a governance playbook from authority to enact it. `DraftProposal` records a model-generated playbook over chain-grounded findings but `govern apply` is specified to refuse it until a human signs that exact artifact. Accepted ADR-011 states that the draft operates outside the task run, that its output governs future runs, that a run consumes the human-signed playbook by hash, and that auto-acceptance is not a signature. The playbook expresses `forbidden` / `required` / `permitted` posture rather than a local task approval. Thus the legitimate parent human owns the ultimate-policy decision and the signed result returns into later Bernstein operation: `S5=P`.

Primary evidence:

- [`README.md`](https://github.com/sipyourdrink-ltd/bernstein/blob/c3d317385a058ae2b5f478399373d09d84d80962/README.md) — product boundary, deterministic scheduler, manager decomposition, isolated agent worktrees, verification/merge loop, governance/audit/replay positioning.
- [`src/bernstein/core/orchestration/manager.py`](https://github.com/sipyourdrink-ltd/bernstein/blob/c3d317385a058ae2b5f478399373d09d84d80962/src/bernstein/core/orchestration/manager.py) and [`manager_models.py`](https://github.com/sipyourdrink-ltd/bernstein/blob/c3d317385a058ae2b5f478399373d09d84d80962/src/bernstein/core/orchestration/manager_models.py) — first-party LLM manager planning, completion review, replanning and typed queue corrections.
- [`src/bernstein/core/orchestration/orchestrator.py`](https://github.com/sipyourdrink-ltd/bernstein/blob/c3d317385a058ae2b5f478399373d09d84d80962/src/bernstein/core/orchestration/orchestrator.py) — manager-review triggers and application of reassign/cancel/priority/add-task corrections into live task-server state.
- [`docs/adapters/openai-agents.md`](https://github.com/sipyourdrink-ltd/bernstein/blob/c3d317385a058ae2b5f478399373d09d84d80962/docs/adapters/openai-agents.md), [`src/bernstein/adapters/openai_agents.py`](https://github.com/sipyourdrink-ltd/bernstein/blob/c3d317385a058ae2b5f478399373d09d84d80962/src/bernstein/adapters/openai_agents.py) and [`openai_agents_runner.py`](https://github.com/sipyourdrink-ltd/bernstein/blob/c3d317385a058ae2b5f478399373d09d84d80962/src/bernstein/adapters/openai_agents_runner.py) — supported first-party Agent/Runner construction path, tools/sandbox/MCP integration and autonomous SDK turn loop.
- [`src/bernstein/core/tasks/task_lifecycle.py`](https://github.com/sipyourdrink-ltd/bernstein/blob/c3d317385a058ae2b5f478399373d09d84d80962/src/bernstein/core/tasks/task_lifecycle.py) — file-ownership and active-worktree overlap detection that suppresses conflicting concurrent spawn.
- [`src/bernstein/core/git/incremental_merge.py`](https://github.com/sipyourdrink-ltd/bernstein/blob/c3d317385a058ae2b5f478399373d09d84d80962/src/bernstein/core/git/incremental_merge.py) — merge serialization, read-set/dirty-state/conflict refusal and returned merge outcome.
- [`docs/architecture/quality-pipeline.md`](https://github.com/sipyourdrink-ltd/bernstein/blob/c3d317385a058ae2b5f478399373d09d84d80962/docs/architecture/quality-pipeline.md), [`src/bernstein/core/quality/janitor.py`](https://github.com/sipyourdrink-ltd/bernstein/blob/c3d317385a058ae2b5f478399373d09d84d80962/src/bernstein/core/quality/janitor.py) and [`cross_model_verifier.py`](https://github.com/sipyourdrink-ltd/bernstein/blob/c3d317385a058ae2b5f478399373d09d84d80962/src/bernstein/core/quality/cross_model_verifier.py) — actual-diff verification, separate-model reviewer selection, autonomous verdict and corrective/blocking return path.
- [`src/bernstein/evolution/detector.py`](https://github.com/sipyourdrink-ltd/bernstein/blob/c3d317385a058ae2b5f478399373d09d84d80962/src/bernstein/evolution/detector.py), [`proposals.py`](https://github.com/sipyourdrink-ltd/bernstein/blob/c3d317385a058ae2b5f478399373d09d84d80962/src/bernstein/evolution/proposals.py) and [`__init__.py`](https://github.com/sipyourdrink-ltd/bernstein/blob/c3d317385a058ae2b5f478399373d09d84d80962/src/bernstein/evolution/__init__.py) — metrics/external-regression sensing, adaptation constructors, proposal/approval/execution/rollback machinery and default closure limit.
- [`src/bernstein/core/govern/proposal.py`](https://github.com/sipyourdrink-ltd/bernstein/blob/c3d317385a058ae2b5f478399373d09d84d80962/src/bernstein/core/govern/proposal.py) and [`docs/decisions/011-model-drafts-human-signs.md`](https://github.com/sipyourdrink-ltd/bernstein/blob/c3d317385a058ae2b5f478399373d09d84d80962/docs/decisions/011-model-drafts-human-signs.md) — model-drafted governance playbook, mandatory human signature, refusal of unsigned apply and signed playbook governing future runs.

## Operational model

A Bernstein run starts from a goal/plan plus declarative role/policy configuration. The first-party manager may decompose the goal into tasks. The deterministic scheduler admits ready tasks, checks dependencies/ownership/capacity and spawns isolated workers through configured adapters. In the credited S1 mode, a Bernstein runner constructs an SDK Agent whose model/tool loop performs the operational task inside the governed sandbox. Multiple workers may progress concurrently when task/file interference checks permit it.

Completed work is not merged on the worker's own claim alone. Janitor/completion signals and quality gates inspect concrete state, and an enabled cross-model verifier can independently inspect the diff and request corrective work. Manager queue review periodically sees the live task set and can change current roles, priorities, cancellations or create new work; deterministic server/scheduler code applies those decisions. Metrics and lineage artifacts are persisted for replay, adaptation and governance evidence.

## S1 — Operations

- State: A
- Function: perform substantive autonomous task work inside a governed Bernstein run through a supported first-party agent execution mode.
- Disturbance / variety regulated: open-ended coding/research tasks, target-repository state, tool/MCP observations, model outputs, execution failures and returned verification feedback.
- Decisive decision or feedback right: interpret the assigned task and current observations, choose model/tool actions, evaluate returned tool results and continue/revise until an operational result is produced.
- Decision owner: the autonomous agent instantiated through Bernstein's supported `openai_agents` runner mode.
- Supporting / enforcement mechanisms: Bernstein spawner, runner manifest, role/model policy, sandbox provider, MCP bridging, session/lifecycle handling, timeouts, cost tracking, task server and lineage/audit instrumentation.
- Closure path: scheduler admits task → Bernstein builds runner manifest and launches first-party `openai_agents_runner` → runner constructs SDK `Agent` with model/tools/sandbox/MCP context → `Runner.run_sync` performs model/tool turns → completion/tool/session events return through Bernstein → task result enters verification and subsequent task operation.
- Boundary reachability: `openai_agents` is a documented built-in Bernstein adapter selectable from normal `plan.yaml`; the optional SDK extra is an explicitly supported dependency, and the runner/manifest/lifecycle integration is first-party at the frozen revision.
- Why this is / is not agent-owned: removing the autonomous Agent/Runner actor while leaving scheduler, worktrees, claims and gates intact leaves task transport/enforcement but removes the substantive open-ended operational decision loop. External CLI wrappers are not needed for this witness.
- Evidence: [`docs/adapters/openai-agents.md`](https://github.com/sipyourdrink-ltd/bernstein/blob/c3d317385a058ae2b5f478399373d09d84d80962/docs/adapters/openai-agents.md); [`src/bernstein/adapters/openai_agents.py`](https://github.com/sipyourdrink-ltd/bernstein/blob/c3d317385a058ae2b5f478399373d09d84d80962/src/bernstein/adapters/openai_agents.py); [`src/bernstein/adapters/openai_agents_runner.py`](https://github.com/sipyourdrink-ltd/bernstein/blob/c3d317385a058ae2b5f478399373d09d84d80962/src/bernstein/adapters/openai_agents_runner.py).
- Basis: explicit + structural
- Confidence: high
- Caveats: Claude/Codex and similar terminal-agent integrations may place more of the autonomous loop in adjacent CLI products. The `A` finding relies on the separately documented SDK-backed first-party execution mode, not on inheriting autonomy from every adapter Bernstein can spawn.

## S2 — Coordination

- State: C
- Function: attenuate concurrent worker interference by preventing overlapping file/task work from being admitted simultaneously and by isolating admitted work in per-agent worktrees.
- Disturbance / variety regulated: two or more operational workers may otherwise modify the same or inferred-overlapping repository paths concurrently, producing collision, stale assumptions, conflicting changes or unsafe landing order.
- Decisive decision or feedback right: decide whether a candidate task batch is safe to spawn given current file ownership and active worktree modifications, and withhold conflicting work until the disturbance clears.
- Decision owner: deterministic Bernstein task-lifecycle/scheduler machinery; no autonomous coordination agent owns the overlap judgment in the standard mode.
- Supporting / enforcement mechanisms: explicit `owned_files`, inferred affected paths, `_file_ownership`, active worktree diff inspection, per-agent worktrees, file locks, merge serialization, dirty-target/read-set/conflict refusal.
- Closure path: scheduler considers ready task/batch → first-party lifecycle compares its paths with live-agent ownership and active worktree changes → overlap causes spawn suppression → non-overlapping workers proceed in isolated worktrees → changed ownership/worktree state is reconsidered on later ticks → later S1 admission therefore changes from the coordination result.
- Boundary reachability: overlap checks execute in ordinary task claim/spawn lifecycle and worktree isolation is a standard Bernstein execution mechanism, not an example-only constructor.
- Distinct S1 units: concurrently runnable autonomous worker tasks instantiated through supported agent execution modes, each with its own task identity/worktree and operational objective.
- Inter-S1 disturbance: simultaneous edits to the same or inferred-overlapping repository paths can create collision/conflict and invalidate assumptions between independently acting workers.
- Attenuating coordination relation: Bernstein withholds a candidate batch when `owned_files`, inferred paths, lock-manager ownership or active worktree diffs overlap, while isolated worktrees and serialized merge paths keep admitted work separated until landing.
- Feedback into subsequent S1 behaviour: a suppressed task is not spawned in that tick; as active ownership/worktree state changes, later scheduling can admit it, changing which autonomous worker acts next.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the witness is a concrete anti-collision relation over plural operational units and shared repository paths, not merely task queues, dependencies or parallelism.
- Why this is / is not agent-owned: the first-party mechanism establishes the S2 function and closes the attenuation feedback, but the overlap decision is a fixed deterministic policy. No autonomous actor is shown deciding or adapting the coordination relation, so constructor `C` is published.
- Evidence: [`src/bernstein/core/tasks/task_lifecycle.py`](https://github.com/sipyourdrink-ltd/bernstein/blob/c3d317385a058ae2b5f478399373d09d84d80962/src/bernstein/core/tasks/task_lifecycle.py); [`src/bernstein/core/git/incremental_merge.py`](https://github.com/sipyourdrink-ltd/bernstein/blob/c3d317385a058ae2b5f478399373d09d84d80962/src/bernstein/core/git/incremental_merge.py).
- Basis: explicit + structural
- Confidence: high
- Caveats: dependency ordering, task claiming, shared whiteboard and ordinary message transport are not independently credited as S2. The positive witness is specifically the live overlap/isolation feedback path.

## S3 — Inside-and-now control

- State: A
- Function: review the live whole-run task organization and autonomously revise current commitments, roles and priorities when completions, failures or stalls indicate the current operating plan needs correction.
- Disturbance / variety regulated: changing task completion/failure state, stalled work, unsuitable role assignment, wrong priority, obsolete commitments, newly necessary tasks and remaining budget pressure.
- Decisive decision or feedback right: choose queue corrections among reassigning role, cancelling work, changing priority and adding a task, based on the current queue and budget/completion/failure context.
- Decision owner: first-party LLM-powered `ManagerAgent` during periodic queue review.
- Whole-system current view: the manager review receives the current open, claimed and failed task queue together with completion/failure counters and remaining budget context for the governed run.
- Current-control decision scope: role reassignment, task cancellation, priority change and creation of newly necessary work across the live run, with deterministic validation/application by the orchestrator.
- Supporting / enforcement mechanisms: task-server snapshot, manager prompt/typed `QueueReviewResult`, completion/failure counters, stall timer, budget tracker, correction validation and deterministic task-server PATCH/POST application.
- Closure path: run accumulates three completions, any failure, explicit review request or stall interval → orchestrator instantiates ManagerAgent with current run context → manager reviews open/claimed/failed queue and returns typed corrections → orchestrator validates/applies them to task-server state → deterministic scheduler sees changed roles/priorities/cancellations/new tasks → subsequent worker commitments change.
- Boundary reachability: manager queue review is wired into the ordinary orchestrator slow tick and uses shipped thresholds; it is not a documentation-only manager pattern.
- Why this is / is not agent-owned: the deterministic orchestrator enforces and validates corrections, but the discretionary judgment over which current correction to make is produced by the ManagerAgent. Removing that model judgment leaves counters and enforcement but not the same live organizational correction choice.
- Evidence: [`src/bernstein/core/orchestration/manager.py`](https://github.com/sipyourdrink-ltd/bernstein/blob/c3d317385a058ae2b5f478399373d09d84d80962/src/bernstein/core/orchestration/manager.py); [`src/bernstein/core/orchestration/manager_models.py`](https://github.com/sipyourdrink-ltd/bernstein/blob/c3d317385a058ae2b5f478399373d09d84d80962/src/bernstein/core/orchestration/manager_models.py); [`src/bernstein/core/orchestration/orchestrator.py`](https://github.com/sipyourdrink-ltd/bernstein/blob/c3d317385a058ae2b5f478399373d09d84d80962/src/bernstein/core/orchestration/orchestrator.py).
- Basis: explicit + structural
- Confidence: high
- Caveats: exact task claiming, retry ceilings and agent lifecycle remain deterministic and are not reclassified as agent-owned merely because the manager can alter role/priority/cancellation/add-task state.

## S3* — Complementary audit

- State: A
- Function: independently inspect completed operational work through a reviewer path that is distinct from the worker's ordinary production/reporting path and return a corrective judgment before merge.
- Disturbance / variety regulated: a worker can report completion while its actual diff contains correctness, security, bug, style or scope defects that ordinary completion claims/signals may miss.
- Decisive decision or feedback right: inspect the concrete git diff and task intent using a reviewer model different from the writer, then decide `approve` versus `request_changes`; in blocking mode the latter prevents merge and creates/feeds corrective work.
- Decision owner: the autonomous cross-model reviewer (or configured reviewer quorum) invoked by Bernstein's first-party verifier.
- Claim being audited: the worker's substantive completion claim that its produced repository change correctly satisfies the assigned task and is suitable to merge.
- Ordinary reporting path: the worker exits/completes and reports its task result through Bernstein's normal agent/session completion path, including its own output and completion signals.
- Complementary access path: Bernstein independently extracts the concrete git diff from the worker worktree, scoped to task-owned files where declared, and sends that artifact plus task intent to a distinct reviewer model.
- Independence boundary: first-party reviewer selection maps writer families to a different reviewer model/provider axis and rejects an explicit reviewer override that collides with the writer model; optional quorum can widen that separation further.
- Who acts on findings: Bernstein's completion/merge-control path acts on `request_changes`; with blocking enabled it prevents ordinary merge and routes the finding into corrective/fix work.
- Supporting / enforcement mechanisms: diff extraction, explicit writer→different-reviewer mapping, same-model override rejection, optional multi-model voting, conventions injection, blocking configuration, janitor/gate pipeline and corrective task/escalation machinery.
- Closure path: worker finishes → Bernstein captures actual worktree diff/task scope → cross-model verifier selects a different reviewer model/provider axis and obtains an independent judgment → `request_changes` with blocking enabled prevents normal merge and enters correction/fix handling → later S1 work therefore changes from the audit finding.
- Boundary reachability: `quality_gates.cross_model.enabled: true` is a documented first-party runtime configuration; the verifier is shipped and integrated into completion processing even though the orchestrator defaults it off.
- Why this is / is not agent-owned: deterministic tests and janitor checks remain supporting evidence, but the credited audit judgment is made by a separate autonomous reviewer over complementary actual-diff evidence. The writer cannot satisfy this path merely by asserting success.
- Evidence: [`docs/architecture/quality-pipeline.md`](https://github.com/sipyourdrink-ltd/bernstein/blob/c3d317385a058ae2b5f478399373d09d84d80962/docs/architecture/quality-pipeline.md); [`src/bernstein/core/quality/cross_model_verifier.py`](https://github.com/sipyourdrink-ltd/bernstein/blob/c3d317385a058ae2b5f478399373d09d84d80962/src/bernstein/core/quality/cross_model_verifier.py); [`src/bernstein/core/quality/janitor.py`](https://github.com/sipyourdrink-ltd/bernstein/blob/c3d317385a058ae2b5f478399373d09d84d80962/src/bernstein/core/quality/janitor.py).
- Basis: explicit + structural
- Confidence: high
- Caveats: the cross-model verifier is fail-open on some reviewer-call/parse failures and is disabled by default. Those are robustness/default-policy limitations, not absence of the supported autonomous audit mode.

## S4 — Intelligence / adaptation

- State: C
- Function: turn future/external or trend-relevant evidence about the operating environment into concrete proposals for changing Bernstein's present routing, model, policy, role-template or provider capability.
- Disturbance / variety regulated: cost/quality/failure trends and external repository-health regressions can make the current model routing, policy, role templates or provider setup unsuitable for later runs.
- Decisive decision or feedback right: select an adaptation proposal and admit it into an approval/execution path that can change current capability.
- Decision owner: not closed by a first-party autonomous S4 actor in the standard mode; detector/proposal/executor logic is primarily deterministic and configuration/risk driven.
- External distinction: when composed with `observability_snapshots_dir`, the detector compares successive external repository-health snapshots and distinguishes new security/coverage regressions from the prior observed environment.
- Future / prospective distinction: the detector also treats persistent cost, success-rate and failure-pattern trends as evidence that the current routing/model/template/provider arrangement may be unsuitable for subsequent runs, not merely as a report about the completed run.
- Adaptation option generated: typed proposals can change policy, routing rules, model routing, role templates or provider configuration, with explicit risk, expected-improvement and rollback metadata.
- Path back into current capability / S3: approved proposals enter the evolution executor, which can apply the configured change (or roll it back on failure), thereby altering the capability/configuration available to later current-operation scheduling and execution.
- Supporting / enforcement mechanisms: `MetricsAggregator`, `OpportunityDetector`, failure-pattern analysis, observability-snapshot regression detection, `ProposalGenerator`, risk/approval modes, `EvolutionCoordinator`, upgrade executor, rollback/circuit/invariant machinery.
- Closure path: first-party constructor can read task/cost/failure trends and, when explicitly composed with `observability_snapshots_dir`, external security/coverage regressions → detector emits typed `ImprovementOpportunity` → proposal generator maps it to a concrete policy/routing/model/template/provider change → evolution approval/executor can apply/rollback the change → later operating capability can differ.
- Boundary reachability: the evolution package is shipped/exported and its detector explicitly accepts the observability snapshot corpus, but the default `AnalysisEngine` constructs `OpportunityDetector` without that external snapshot input; a developer/operator must therefore compose the outside-sensing path and autonomous adaptation authority to close S4.
- Why this is / is not agent-owned: the repository supplies a function-specific outside/trend-to-adaptation constructor and execution return path, but its decisive adaptation selection/approval is heuristic/configured rather than autonomously owned. This is narrower than awarding S4 for generic learning, metrics or a roadmap.
- Evidence: [`src/bernstein/evolution/detector.py`](https://github.com/sipyourdrink-ltd/bernstein/blob/c3d317385a058ae2b5f478399373d09d84d80962/src/bernstein/evolution/detector.py); [`src/bernstein/evolution/proposals.py`](https://github.com/sipyourdrink-ltd/bernstein/blob/c3d317385a058ae2b5f478399373d09d84d80962/src/bernstein/evolution/proposals.py); [`src/bernstein/evolution/__init__.py`](https://github.com/sipyourdrink-ltd/bernstein/blob/c3d317385a058ae2b5f478399373d09d84d80962/src/bernstein/evolution/__init__.py).
- Basis: explicit + structural
- Confidence: medium-high
- Caveats: internally observed success/cost metrics alone are not treated as sufficient outside-and-then intelligence. The positive constructor relies on the explicit external observability-regression input plus the shipped adaptation proposal/execution machinery; default wiring remains incomplete.

## S5 — Policy / identity

- State: P
- Function: establish the authoritative governance playbook that defines forbidden, required and permitted posture for later Bernstein runs, while keeping the ultimate enactment right at the legitimate parent human/operator.
- Disturbance / variety regulated: observed governance findings may imply a new desired policy/posture, but a model-generated suggestion must not silently redefine what the governed organization permits or requires.
- Decisive decision or feedback right: sign or refuse the exact governance playbook artifact that will govern subsequent runs.
- Decision owner: legitimate parent human/operator signing a content-specific governance proposal.
- Identity / ultimate-policy issue: which governance posture the Bernstein organization will treat as forbidden, required and permitted for future runs, rather than whether one current task should pass a local approval.
- Ultimate authority in each claimed mode: in the claimed parent-governed mode, the human/operator who signs the exact content-addressed governance playbook is the ultimate authority; the drafting model has proposal authority only and cannot enact the policy.
- Return-to-operation path: `govern apply` refuses unsigned drafts, while a human-signed playbook is admitted by hash and is then consumed by later Bernstein runs, so subsequent governed operation executes under the returned parent policy.
- Supporting / enforcement mechanisms: chain-grounded findings document, model-assisted `DraftProposal`, canonical content hash, recorded prompt/model/findings digests, proposal status/signature, `govern apply` refusal for unsigned drafts and run consumption of the signed playbook by hash.
- Closure path: first-party governance discovery observes chain-recorded findings → optional model drafts a `forbidden`/`required`/`permitted` playbook proposal → human reviews and signs the exact content hash (or refuses) → unsigned apply is rejected; signed playbook is accepted → later Bernstein runs consume that signed playbook → subsequent operation is governed by the parent decision.
- Boundary reachability: ADR-011 is an accepted first-party architectural decision describing the shipped `govern discover --assist` / `DraftProposal` / `govern apply` contract and explicitly states that the resulting signed playbook governs future runs.
- Why this is / is not agent-owned: the model may draft policy text but cannot enact it; the repository explicitly makes the human signature the authoritative act and rejects auto-acceptance as a signature. Thus the function is positively closed but parent-owned, yielding `P`, not `A`/`C`.
- Evidence: [`src/bernstein/core/govern/proposal.py`](https://github.com/sipyourdrink-ltd/bernstein/blob/c3d317385a058ae2b5f478399373d09d84d80962/src/bernstein/core/govern/proposal.py); [`docs/decisions/011-model-drafts-human-signs.md`](https://github.com/sipyourdrink-ltd/bernstein/blob/c3d317385a058ae2b5f478399373d09d84d80962/docs/decisions/011-model-drafts-human-signs.md); [`src/bernstein/cli/commands/governance_cmd.py`](https://github.com/sipyourdrink-ltd/bernstein/blob/c3d317385a058ae2b5f478399373d09d84d80962/src/bernstein/cli/commands/governance_cmd.py).
- Basis: explicit + structural
- Confidence: high
- Caveats: ordinary RBAC checks, budgets, quality gates, task approvals and static `bernstein.yaml` configuration are not independently credited as S5. The positive witness is specifically the signed future-run governance-playbook authority path.

## Assessment summary

Bernstein is an included autonomous harness with a materially richer organizational-control surface than a deterministic CLI wrapper. A documented first-party OpenAI Agents SDK mode establishes autonomous S1 execution. Concrete file/worktree collision regulation establishes S2 as constructor `C`. The first-party LLM ManagerAgent closes a live whole-run correction loop for S3=`A`, and the distinct writer-versus-reviewer actual-diff path closes S3*=`A`. The evolution subsystem exposes a function-specific external/trend-to-upgrade construction path but leaves autonomous outside-and-then authority/composition incomplete, so S4=`C`. Finally, the accepted governance architecture deliberately reserves enactment of future-run `forbidden`/`required`/`permitted` policy to a human signature and returns the signed playbook into later runs, establishing parent-governed S5=`P`.

Proposed canonical vector: `S1=A / S2=C / S3=A / S3*=A / S4=C / S5=P`.

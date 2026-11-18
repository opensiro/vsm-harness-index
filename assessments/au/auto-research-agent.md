---
harness_id: auto-research-agent
project_name: Auto-research agent
repository: https://github.com/rohanarun/Auto-research-agent
review_ref: bdd59df709d0b5353856b1cc39e116226c57f5d4
reviewed_at: 2026-11-18
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: P
---

# Auto-research agent

## Review boundary

- System in focus: A single operator-selected research project run in the installed macOS Auto Research client, including its opt-in shared-context and model-directed research-method runner; not the repository development organization.
- Purpose and identity: Pursue an externally given open research problem through model-driven iterative experiments, evaluate candidate evidence against a fixed task criterion, preserve the best independently checked working state, and return a reviewable outcome.
- Relevant environment: Project repository and open issue/guide, current experimental results, other parallel branch discoveries, available CLI/model accounts, finite computation and authorized external verification services.
- Standard-distribution boundary: Shipped macOS client, core Swift project/session/parallel-workspace logic, optional first-party ResearchMethods Python runner and policies, configured Codex/Claude/OpenCode/Antigravity CLI (external model decisions), and optional first-party cloud adapters. Research benchmarks under `benchmarks/` are excluded from the product operating boundary.
- Credited operating / distribution surfaces: Standard model-driven project task, opt-in parallel shared-checkpoint agent mode, method-runner branch planning/evaluation/leader selection and continued research, operator project/compute/stop controls, first-party frozen evaluator contract and actual source-artifact verification path.
- Adjacent first-party surfaces excluded from ownership: Benchmark suite and published model comparisons, companion portable GA and its fixtures, demo charts, repository CI/release, developer test harnesses, standalone third-party evaluators not configured for a supported run, and model/provider internals.
- First-party operating / deployment modes considered: Local configured CLI task, optional several research workers with shared checkpoints, optional RSI-top/fork-and-flush method cohort and continuation, attended operator control and optional owned cloud compute/recovery.
- Recursion level: The selected research project/cohort. Parallel model-backed experiment branches are distinct S1 cells under one project; the optional model coordinator is the project-level control actor within the granted run, while the operator is a distinct parent.
- Reviewed revision: `bdd59df709d0b5353856b1cc39e116226c57f5d4`.
- Observation date: 2026-11-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The native Swift app launches supported installed model CLIs against one research checkout, holds project/session state and offers Play/Stop plus optional local/cloud parallel work. In shared mode distinct agents have private checkouts and keep `RESEARCH_CHECKPOINT.md` / topic files; after a boundary the app snapshots these files and supplies the resulting evidence bundle to subsequent fresh sessions without a separate summary model. The opt-in ResearchMethods mode invokes a coordinator model to author a task-specific plan, fixed evaluator and metrics, then launches a bundled Python method runner. That runner freezes the evaluator outside candidate workspaces, preflights a baseline, opens isolated branches, runs parallel exploration within owner-set windows, invokes the independent evaluator on actual candidate bytes, and selects a verified leader while keeping rejected and incomplete artifacts. The user controls enabled methods, model/provider, resources, budgets and stopping. The scientific evaluation oracle may be task-specific; mere test/benchmark code co-located elsewhere in the repository is not credited.

## Operational model

An operational worker selects research edits/experiments within its local checkout and feeds evidence to its parent. Where shared context is enabled, agents receive saved peer checkpoints and choose complementary future experiments rather than duplicating costly tracks; the workspace gate prevents two writers from taking the same project checkout. In the optional methods mode a coordinating model selects a research plan, metrics and future branch directions and can decide a further batch from returned evidence, while the first-party runner enforces budget boundaries and independently checks candidate results. The project owner establishes the legitimate success criterion and controls aggregate research cost and release/publication decisions.

## S1 — Operations

- State: A
- Function: Model-guided investigation and tool-using iteration on a research project's open problem.
- Disturbance / variety regulated: Unknown technical hypotheses, source code, experimental outcomes, external CLI results and changing evidence.
- Decisive decision or feedback right: Choose code/experiment actions, interpret tool feedback, update candidate hypotheses and return task results.
- Decision owner: Configured model-driven coding/research worker in its first-party app-controlled session; provider inference is outside the repository.
- Supporting / enforcement mechanisms: Swift session runner, supported CLI, local or cloud checkout, task instructions, timers and saved transcripts.
- Closure path: A worker reads current checkout/check outputs, makes further changes, saves evidence and returns results to the app/project and next run.
- Boundary reachability: Standard Play launches installed configured Codex/Claude/OpenCode/Antigravity for a research project; the optional method runner launches the same supported CLI in branch workspaces.
- Why this is / is not agent-owned: The model selects substantive experiments and edits; app control and the CLI transport do not decide those scientific actions.
- Evidence: [normal shipped execution](https://github.com/rohanarun/Auto-research-agent/blob/bdd59df709d0b5353856b1cc39e116226c57f5d4/README.md#L7-L32), [model-driven method invocation](https://github.com/rohanarun/Auto-research-agent/blob/bdd59df709d0b5353856b1cc39e116226c57f5d4/Sources/ResearchCore/ResearchMethods.swift#L18-L64), [branch execution and evaluated returns](https://github.com/rohanarun/Auto-research-agent/blob/bdd59df709d0b5353856b1cc39e116226c57f5d4/Resources/ResearchMethods.py#L214-L304).
- Basis: structural
- Confidence: high
- Caveats: Research results are not automatically verified; no live model execution was performed for this assessment.

## S2 — Coordination

- State: A
- Function: Attenuate branch-contention and duplicated incompatible research among multiple independent model-backed S1 workers.
- Disturbance / variety regulated: Two writers can contend for one checkout; separate agents can repeat already failed or overlapping experimental directions and waste the common time/compute allowance.
- Decisive decision or feedback right: In supported shared-context mode, each agent chooses a complementary experiment after considering peer checkpoint evidence; the coordinating model determines work partitions within user-approved limits.
- Decision owner: Model workers and coordinating agent for selection of complementary research directions; runtime independently enforces checkout isolation and common resource bounds.
- Supporting / enforcement mechanisms: Active-checkout guard, independent workspaces/branches, timed checkpoint bundle, immutable peer manifest, peer findings and rejection of malformed collaboration.
- Closure path: An active writer blocks competing startup; after the shared checkpoint boundary, next agent sessions receive peer findings and choose changed experiments; failed peer obligations prevent candidate promotion and return diagnostic evidence.
- Boundary reachability: Opt-in first-party parallel sharing and method co-operation are shipped Swift/UI modes, with native snapshot/restart and bundled method Python runner.
- Why this is / is not agent-owned: Checkout locks are enforcement only; the policy explicitly instructs the model to respond to actual peer evidence by selecting a different, complementary next experiment rather than relying on static routing.
- Distinct S1 units: Two or more independently invoked model research workers, each with a separate checkout and own experiments, whose results influence the same project objective.
- Inter-S1 disturbance: Concurrent editing of a shared source checkout and overlapping/harmfully duplicated experiments competing for one fixed research budget.
- Attenuating coordination relation: Project writer reservation plus private checkouts; peer evidence/checkpoints and model-authored complementary follow-up assignments.
- Feedback into subsequent S1 behaviour: The saved peer bundle is injected into the next branch session; model policy requires checking peers' findings and choosing a distinct justified experiment, with collaboration failure stopping invalid promotion.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: Concrete writer contention is detected at project launch; sharing is tied to avoiding redundant experiments and resolving peer evidence/ownership rather than merely passing a message.
- Evidence: [active checkout collision refusal](https://github.com/rohanarun/Auto-research-agent/blob/bdd59df709d0b5353856b1cc39e116226c57f5d4/Sources/AutoResearch/SharedResearch.swift#L53-L79), [separate research checkouts and generations](https://github.com/rohanarun/Auto-research-agent/blob/bdd59df709d0b5353856b1cc39e116226c57f5d4/Sources/AutoResearch/SharedResearch.swift#L96-L151), [peer policy and complementary experiment](https://github.com/rohanarun/Auto-research-agent/blob/bdd59df709d0b5353856b1cc39e116226c57f5d4/Resources/SharedContextPolicy.md#L1-L26), [method peer review and next cohort](https://github.com/rohanarun/Auto-research-agent/blob/bdd59df709d0b5353856b1cc39e116226c57f5d4/Resources/ResearchMethods.py#L306-L324), [shared cohort return](https://github.com/rohanarun/Auto-research-agent/blob/bdd59df709d0b5353856b1cc39e116226c57f5d4/Resources/ResearchMethods.py#L421-L461).
- Basis: structural
- Confidence: medium
- Caveats: Positive coordination depends on explicitly enabled multi-worker sharing/methods and model compliance with the shipped policy. Independent workers without sharing have only checkout isolation, not the full agent-owned S2 path.

## S3 — Inside-and-now control

- State: A(P)
- Function: Maintain project-wide current research commitments, branch allocation, verified incumbent and finite resources as feedback changes.
- Disturbance / variety regulated: Branch exploration can duplicate work, run out of time/disk/provider capacity, or promote an unverified candidate while active workers still have useful unfinished results.
- Decisive decision or feedback right: In enabled methods mode the model coordinator authors the criterion-aware plan, experiment portfolio, per-branch metric views and whether more research is justified; in attended mode the owner can set stop/cost limits and intervene across project runs.
- Decision owner: Model coordinator for the autonomous method mode; project owner for the independent parent-controlled project mode. The deterministic runner enforces ceilings and selects only evaluator-valid leaders.
- Supporting / enforcement mechanisms: Immutable plan and evaluator, parallel branch scheduler, score/metric dashboards, verified leader state, stop/drain/recovery, configurable method windows and cloud ownership ledgers.
- Closure path: Runner returns verified branch/metric and outstanding-work evidence to coordinator; it chooses the next plan or stops. User Stop cancels project workers, while chosen budgets and sharing settings affect subsequent allocations.
- Boundary reachability: First-party optional method policy invokes the configured coordinator model with project-wide evidence; app exposes per-project controls and returns archived results to the same authorized research project.
- Why this is / is not agent-owned: In autonomous mode, model decisions about research allocation are distinct from immutable evaluator score ranking or time-slot enforcement. In parent mode, the owner can stop/limit the whole research cohort.
- Whole-system current view: Coordinator sees `DASHBOARD.json`, evaluated leaders/branches, metric diagnostics and pending work; app shows project sessions and shared group status and can stop all owned workers.
- Current-control decision scope: Select active experiment portfolio and whether to continue within an existing research objective, prioritize verified incumbent over speculative work, allocate branch count/windows within parent ceilings; parent can stop or change supported project settings.
- Evidence: [coordinator-owned plan and fixed limits](https://github.com/rohanarun/Auto-research-agent/blob/bdd59df709d0b5353856b1cc39e116226c57f5d4/Resources/ResearchMethodsPolicy.md#L1-L43), [leader and branch control](https://github.com/rohanarun/Auto-research-agent/blob/bdd59df709d0b5353856b1cc39e116226c57f5d4/Resources/ResearchMethods.py#L539-L615), [continue based on returned evidence](https://github.com/rohanarun/Auto-research-agent/blob/bdd59df709d0b5353856b1cc39e116226c57f5d4/Resources/ContinuePolicy.md#L1-L13), [owner group control](https://github.com/rohanarun/Auto-research-agent/blob/bdd59df709d0b5353856b1cc39e116226c57f5d4/Sources/AutoResearch/SharedResearch.swift#L31-L68), [result/continued invocation](https://github.com/rohanarun/Auto-research-agent/blob/bdd59df709d0b5353856b1cc39e116226c57f5d4/Sources/AutoResearch/MethodMonitoring.swift#L81-L96).
- Basis: structural
- Confidence: medium
- Caveats: No autonomous control over the whole app or unrelated projects claimed; fixed evaluator and scorer are enforcement, not evidence the model owns their decisions.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Model coordinator | Current project branch scores, stalls and incomplete research | Chooses model-authored plan/next batch from verified dashboard within user ceilings | [method policy](https://github.com/rohanarun/Auto-research-agent/blob/bdd59df709d0b5353856b1cc39e116226c57f5d4/Resources/ResearchMethodsPolicy.md#L1-L43), [continuation](https://github.com/rohanarun/Auto-research-agent/blob/bdd59df709d0b5353856b1cc39e116226c57f5d4/Resources/ContinuePolicy.md#L1-L13) |
| Parent (`P`) | Operator | Current resource cost, project work and stop/change of methods | Stop/drain agents or update run budgets and configured methods for subsequent work | [project shared controls](https://github.com/rohanarun/Auto-research-agent/blob/bdd59df709d0b5353856b1cc39e116226c57f5d4/Sources/AutoResearch/SharedResearch.swift#L31-L68) |

## S3* — Complementary audit

- State: C
- Function: Complement production claims with separately executed source-artifact evaluation under a frozen checker, feeding accepted/rejected evidence into control.
- Disturbance / variety regulated: A writing worker can claim improvement without a correct or independently reproducible result.
- Decisive decision or feedback right: Check true candidate validity/score and raw evidence against a task-specific evaluator prepared before experimentation and held outside agent-writeable candidate workspaces.
- Decision owner: The separately executed evaluator makes the audit judgment; model/human establishes its scientific criterion before execution, while the first-party runner enforces checksum and independence boundaries.
- Supporting / enforcement mechanisms: Frozen evaluator hash, isolated subprocess, pre/post workspace inventory, evidence SHA-256, preflight valid/invalid fixtures and verified leader selection.
- Closure path: Failed evaluator rejects candidate; a passing independent result determines eligible leader and returns a score/receipt to dashboard/coordinator before next research action.
- Boundary reachability: Shipped optional ResearchMethods mode requires an external-to-candidate evaluator and runs it independently on source workspace bytes, with no user-added plugin protocol needed.
- Why this is / is not agent-owned: This is a first-party **constructor path** for a specific independent audit task, not a globally preinstalled independent researcher. The producer does not control the evaluator after it is frozen, but an operator/coordinator must supply a valid task-specific audit criterion and checker.
- Claim being audited: Worker completion/improvement and score claims over its candidate source.
- Ordinary reporting path: Worker output and its research checkpoint/transcript containing self-reported results.
- Complementary access path: Outside-candidate frozen evaluator independently opens the actual candidate workspace, runs a task-specific check and hashes the cited evidence.
- Independence boundary: Evaluator copied outside branch directories, its digest checked post-run and candidate inventory verified unchanged; evaluator cannot be edited by the candidate worker and cannot accept score without evidence.
- Who acts on findings: Runner excludes failed candidate and chooses among evaluated valid leaders; model coordinator receives returned metrics and future-planning evidence.
- Evidence: [independent task-specific checker requirement](https://github.com/rohanarun/Auto-research-agent/blob/bdd59df709d0b5353856b1cc39e116226c57f5d4/Resources/ResearchMethodsPolicy.md#L14-L43), [source artifact evaluation/digest/receipt](https://github.com/rohanarun/Auto-research-agent/blob/bdd59df709d0b5353856b1cc39e116226c57f5d4/Resources/ResearchMethods.py#L174-L212), [selection from independently valid candidates](https://github.com/rohanarun/Auto-research-agent/blob/bdd59df709d0b5353856b1cc39e116226c57f5d4/Resources/ResearchMethods.py#L463-L478), [rejected incomplete/invalid branches](https://github.com/rohanarun/Auto-research-agent/blob/bdd59df709d0b5353856b1cc39e116226c57f5d4/Resources/ResearchMethods.py#L539-L615).
- Basis: structural
- Confidence: medium
- Caveats: A synthetic or dishonest evaluator is not an independent audit of scientific correctness. `C` is bounded to this implemented evaluator-construction protocol, not a claim of independent audit in every default task or a generalized S3* runtime.

## S4 — Outside-and-then intelligence

- State: —
- Function: No project-operating-capability adaptation loop grounded in external future/environmental distinctions was established apart from research execution itself.
- Disturbance / variety regulated: Project topics, scientific unknowns, model/tool availability and research-method performance.
- Decisive decision or feedback right: Model may choose future experiments within the research goal and runner changes branch strategy after a stalled score; no shipped agentically closed decision for adapting the research organization to *external prospective* conditions was shown.
- Decision owner: Project model makes immediate research choices; operator edits project settings, model and available methods.
- Supporting / enforcement mechanisms: Research catalog discovery, configurable RSI-top/fork-and-flush, published metric dashboards and per-batch future tasks.
- Closure path: Research method continuation feeds a new experiment into the same task objective; no documented outside-and-then capability adaptation return to project control at the reviewed boundary.
- Why this is / is not agent-owned: Hypothesis search and choosing a fresh branch are S1/S3 work on the ongoing research objective, not automatically an S4 strategy function.
- Evidence: [model-controlled research strategy within task](https://github.com/rohanarun/Auto-research-agent/blob/bdd59df709d0b5353856b1cc39e116226c57f5d4/Resources/ResearchMethodsPolicy.md#L1-L65), [internal stall search/exploration](https://github.com/rohanarun/Auto-research-agent/blob/bdd59df709d0b5353856b1cc39e116226c57f5d4/Resources/ResearchMethods.py#L539-L615), [catalog-driven project selection](https://github.com/rohanarun/Auto-research-agent/blob/bdd59df709d0b5353856b1cc39e116226c57f5d4/README.md#L7-L27).
- Basis: structural
- Confidence: medium
- Caveats: A project explicitly tasked with examining future external change could construct S4, but this is not established as a standard shipped project capability-adaptation loop.

### Absence scope

- Surfaces inspected: App project/catalog modes, model policy for research methods, fixed runner/evaluator, saved research checkpoints, external cloud/provider controls.
- Plausible first-party paths checked: RSI-top stall and alternative hypothesis exploration as adaptation, project discovery as environmental sensing, model/agent configuration as changed capability.
- Why no material first-party path remains: The observed feedback changes which *research experiment* is performed inside a fixed objective, while new model, permissions and methods are user-configured; no supplied prospectively oriented environmental decision changes the research organization's repertoire.

## S5 — Policy and identity

- State: P
- Function: Parent authority defines the research project's ultimate purpose and scientific validity/publication boundaries.
- Disturbance / variety regulated: Model-generated proxies or score claims may displace a legitimate user/maintainer research objective, evidence standards or risk limits.
- Decisive decision or feedback right: Set the exact accepted research objective, trusted scorer/evaluator authority and publish/compute mandate; refuse an invented proxy or unapproved external communication.
- Decision owner: Project operator (and separately a legitimate upstream maintainer for its own acceptance rules). The model can propose a plan but is constrained by parent-defined objective.
- Supporting / enforcement mechanisms: User-selected project, scoring-authority source pins, immutable run plan and accepted evaluator, spending/score checks and explicit publication review.
- Closure path: Operator supplies goal, method limits and accepted scientific rubric; coordinator reads them and writes a matching immutable plan; runner validates candidate outcomes under that rubric and model returns results for owner disposition; following runs reuse the bounded mandate unless the owner changes it.
- Boundary reachability: The shipped project UI and method policy demand the user/maintainer criteria and freeze them in the supported method-mode plan before worker launch.
- Why this is / is not agent-owned: Final scientific acceptance and public publication mandate remain with human/project authority; a model's arbitrary objective proxy does not become ultimate policy.
- Identity / ultimate-policy issue: What counts as an acceptable contribution or proof for this specific research project, not ordinary per-experiment scheduling.
- Ultimate authority in each claimed mode: Parent operator/authorized research rule-owner; no first-party autonomous S5 decision right claimed.
- Return-to-operation path: Approved goal and rubric → immutable evaluator/method plan → actual subsequent candidate gate/score and provider tasks → accepted/rejected evidence returned for further project work.
- Evidence: [user/maintainer scoring authority](https://github.com/rohanarun/Auto-research-agent/blob/bdd59df709d0b5353856b1cc39e116226c57f5d4/Resources/ResearchMethodsPolicy.md#L8-L37), [preflight rejects invalid initial evidence](https://github.com/rohanarun/Auto-research-agent/blob/bdd59df709d0b5353856b1cc39e116226c57f5d4/Resources/ResearchMethods.py#L539-L549), [user controls research modes and budgets](https://github.com/rohanarun/Auto-research-agent/blob/bdd59df709d0b5353856b1cc39e116226c57f5d4/README.md#L137-L170), [no unilateral maintainer contact](https://github.com/rohanarun/Auto-research-agent/blob/bdd59df709d0b5353856b1cc39e116226c57f5d4/Resources/ResearchMethodsPolicy.md#L13-L19).
- Basis: structural
- Confidence: medium
- Caveats: Merely providing a task prompt is not S5; parent credit depends on the supported legitimate research-purpose and scientific-validity authority actually applied in subsequent runs, not the code repository's maintainer governance.

## Distributed OSS parent arrangement

Upstream maintainers can define problem scoring criteria and publication rules, but do not become runtime project parents merely because a guide is on GitHub. A local operator who selects and ratifies the applicable criteria owns the installed project mandate; the source author of a rubric has only the authority the operator's project adopts.

## Self-hosted and non-human modes

Opt-in shared and methods modes add first-party evidence for S2, S3 and S3*. Plain one-worker app use is S1 without those witnesses. User approval remains legitimate parent ownership for current control and criteria, not a defect in model autonomy.

## Recursion

Parallel branches and fork/flush are operational experiments inside the same project, not automatically independently viable systems. The project method coordinator forms the upper current-control recursion for those research cells; unproven subsystem S4/S5 are not imported.

## Variety and escalation

The author-supplied metric/evaluator freezes legitimacy before candidate code mutates; private checkouts attenuate source conflicts, snapshots attenuate repetition, and preserved incomplete work supports later corrective choices. Timeout, owner Stop, permission or evaluator failure are distinguishable and do not automatically confer a new VSM function.

## Evidence gaps

This is a source-only review pinned to the public tree. No macOS app, model, cloud instance, Lean server or benchmark experiment was executed. The shipped modes' source wiring supports the optional workflows, not a general empirical performance claim. The independently frozen checker is only as valid as its chosen criterion; all citation links point to the examined first-party revision.

---
harness_id: agentforeman
project_name: AgentForeman
repository: https://github.com/kumizeod/AgentForeman
review_ref: 634f9c0906f133fc577d6291c29b8f8cfd6af02a
reviewed_at: 2026-10-28
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# AgentForeman

## Review boundary

- System in focus: one local, durable AgentForeman task/campaign and its configured model-backed worker pool; not an autonomous research institution or the external coding CLI product.
- Purpose and identity: produce bounded task artifacts or experimentally verified code/checkpoint candidates under a frozen user goal and acceptance contract.
- Relevant environment: operator project/evidence, model endpoints or installed CLI adapters, quota availability, local processes/files and trusted evaluator.
- Standard-distribution boundary: packaged Python CLI/UI, campaign/engine, briefing, cooperation/debate/council, registered worker adapters, pool and shipped moons experiment template.
- Credited operating / distribution surfaces: src/agentforeman/{cli,manager,campaign,engine,briefing,cooperate,debate,council,pool_worker,agents,providers}.py and shipped templates/moons; model-backed roles are intentionally composed by these first-party task protocols.
- Adjacent first-party surfaces excluded from ownership: tests and scripted provider fixtures, evidence/* historical CI receipts, browser test harness, development roadmap and maintainer GitHub workflows.
- First-party operating / deployment modes considered: single-run/campaign/overnight experiment; shared council; cooperative/adversarial artifact tasks; human-confirmed briefing; CLI and local UI. External CLI internal tools/organization are not borrowed.
- Recursion level: one campaign or cooperative task with subordinate experiment/contribution cells; worker-process nesting alone does not prove recursive viability.
- Reviewed revision: `634f9c0906f133fc577d6291c29b8f8cfd6af02a`.
- Observation date: 2026-10-28.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

AgentForeman packages a Python control plane with SQLite records, immutable source/evidence snapshots, durable job IDs/leases, cancellation receipts and local process supervision. Campaign manager prompts ask a separate read-only model session to choose experiment, repair, retest or stop from the verified incumbent and round record; a coding worker edits the permitted source snapshot, then trusted training/evaluation and archival run. General cooperation uses a model integrator, isolated contributors, distinct critics and an advisory chair; the council additionally audits synthesis against original answers, criticism and supplied sources. Briefing produces a versioned task contract whose exact fingerprint and resource settings the human confirms before dispatch. Native CLI/API providers supply cognition; the first-party protocols determine context, role separation and returned actions. External providers do not donate their unrelated governance or agent-internal capabilities. See the pinned manager/campaign, cooperation/debate and council source links in the function sections.

## Operational model

The operational result is a bounded report/artifact or a measured experiment archive. Model roles choose hypotheses, code changes, decomposition, contributions, integrated text and critique. The deterministic controller validates schemas, runs frozen checks, selects the best measured candidate, prevents unauthorized edits and enforces deadlines. Research subject optimization is the task outcome, not self-adaptation of the harness. Human contract confirmation and account setup remain outside autonomous task choices.

## S1 — Operations

- State: A
- Function: produce candidate code/experiments and general task artifacts through model decisions with returned evidence.
- Disturbance / variety regulated: heterogeneous goals, failed code/training, poor candidates and contradictory evidence.
- Decisive decision or feedback right: choose experiment/repair/retest/stop and instructions; author source or artifacts; revise after independent criticism.
- Decision owner: configured model-backed manager, coding worker, contributors and integrator, invoked by first-party protocols.
- Supporting / enforcement mechanisms: source snapshots, typed responses, worker pool leases, edit allowlist, native training/checks, archives and round/deadline bounds.
- Closure path: verified baseline → manager model choice → worker action → independent measurement/criticism → next choice or revision → preserved terminal result.
- Why this is / is not agent-owned: removing the model roles leaves deterministic transport and checks but no substantive hypothesis, edit or report decision.
- Caveats: A is structural ownership, not proof of live model quality; external coding tools are credited only as explicitly assembled task actors.
- Boundary reachability: CLI campaign/overnight and cooperate/debate commands assemble these roles and execute their chosen actions; they are shipped supported modes, not test-only prompts.
- Evidence: [src/agentforeman/manager.py](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/manager.py); [src/agentforeman/campaign.py](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/campaign.py); [src/agentforeman/engine.py](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/engine.py); [src/agentforeman/cooperate.py](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/cooperate.py); [src/agentforeman/debate.py](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/debate.py); [src/agentforeman/pool_worker.py](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/pool_worker.py).
- Basis: structural
- Confidence: medium-high for source topology; live agent efficacy unmeasured.

## S2 — Coordination

- State: —
- Function: no separately closed inter-S1 interference regulation at the declared task boundary.
- Disturbance / variety regulated: independent contributions can be inconsistent; worker contention and duplicate execution are mechanically bounded.
- Decisive decision or feedback right: integrator chooses combined output, but contributors are not subsequently coordinated through a specific inter-unit correction loop.
- Decision owner: integrator owns S1 synthesis; runtime owns fixed sequencing/leases, with no separately evidenced autonomous S2 discretion.
- Supporting / enforcement mechanisms: independent assignments, integration contract, queue/lease locks, quota cooldown and critique of combined artifacts.
- Closure path: contributors return once → integrator revises the combined product; duplicate jobs are suppressed by fixed IDs/locks.
- Why this is / is not agent-owned: decomposition, waiting for all contributions and rewriting one combined answer do not establish mutual adjustment of operational units.
- Caveats: does not deny coordination in a broader organization assembled around this tool.
- Evidence: [src/agentforeman/cooperate.py](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/cooperate.py); [src/agentforeman/pool.py](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/pool.py); [docs/COOPERATIVE.md](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/docs/COOPERATIVE.md).
- Basis: structural
- Confidence: medium-high for source topology; live agent efficacy unmeasured.

### Absence scope

- Surfaces inspected: Cooperation plan/contribute/propose flow, pool leases, coding candidate isolation and council stages.
- Plausible first-party paths checked: integration-contract inconsistencies, missing contributors, worker contention, duplicate/recovered tasks and peer review.
- Why no material first-party path remains: shipped contributors do not receive an inter-S1 corrective decision changing their subsequent behavior; remaining coordination is task composition or mechanical exclusion.

## S3 — Inside-and-now control

- State: —
- Function: no whole-system discretionary current-control function over a portfolio established at this boundary.
- Disturbance / variety regulated: candidate failure, incumbent comparison, quota waits and bounded task duration.
- Decisive decision or feedback right: manager chooses the next experiment within one fixed objective; it cannot change resources, task goal or budgets.
- Decision owner: model owns local S1 research choices; operator/configuration selects task scope, role pool and limits; runtime enforces those choices.
- Supporting / enforcement mechanisms: campaign rounds/best record, budget/deadline checks, role registry, UI status, cancel and resume.
- Closure path: measured rounds return to a next-task-action choice; generic stop/confirmation returns no evidenced whole-system resource bargain.
- Why this is / is not agent-owned: the campaign manager name does not turn its local experimental policy into a metasystem; fixed quotas are enforcement.
- Caveats: broader multi-project allocation may be performed externally but is outside the declared first-party campaign mode.
- Evidence: [src/agentforeman/manager.py](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/manager.py); [src/agentforeman/campaign.py](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/campaign.py); [src/agentforeman/briefing.py](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/briefing.py); [src/agentforeman/pool.py](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/pool.py).
- Basis: structural
- Confidence: medium-high for source topology; live agent efficacy unmeasured.

### Absence scope

- Surfaces inspected: Campaign decision/evidence contract, worker pool registry/quotas, briefing confirmation, local status and termination.
- Plausible first-party paths checked: manager experiment/repair/retest/stop, role plans, resource settings, human edits, quota wait and cancel/resume.
- Why no material first-party path remains: no shipped autonomous or function-specific parent loop couples a whole operational portfolio to discretionary shared-resource/commitment revision; supported choices close one task.

## S3* — Complementary audit

- State: A
- Function: challenge operational claims through separate model audit/critique with complementary original evidence and corrective return.
- Disturbance / variety regulated: unsupported synthesis claims, missed criticism, inadequate experiment plans and false candidate success.
- Decisive decision or feedback right: distinct critic/auditor chooses anchored findings and accept/revise/reject; campaign reviewer can block or return an executable proposal for revision.
- Decision owner: separately invoked model reviewer/auditor roles; deterministic gates apply verdict consistency and run trusted checks.
- Supporting / enforcement mechanisms: distinct role identities, read-only review snapshot, source/check/artifact anchors, issue ledger, frozen verifier and bounded revision/retest.
- Closure path: raw artifacts/source/check receipts → separate critic judgment → integrator/manager revision and recheck, or stopped/needs-evidence/rejected result; council audit conditions final disposition.
- Why this is / is not agent-owned: model audit judgment owns substantive criticism; deterministic parsing and trusted checkpoint measurement are support, not the owner of that judgment.
- Caveats: distinct identities are not statistically independent models; supplied sources are not authenticated by quote matching, and live factual correctness remains unmeasured.
- Boundary reachability: documented campaign --review, cooperative distinct-reviewer mode and council audit are shipped runtime modes; no developer fixture is needed to select them.
- Claim being audited: candidate/proposal or chair/integrator output is supported by original source material, controls, actual artifacts and check results.
- Ordinary reporting path: manager rationale, proposer artifacts and chair/integrator summary.
- Complementary access path: reviewer receives copied source snapshots plus experiment evidence; general critics receive full artifact/source/check anchor documents, and council auditor sees original answers and all criticism rather than chair summary alone.
- Independence boundary: separate read-only sessions/role identities from author/integrator/chair; no authorship permission for the reviewer. Trusted verifier directly reads tensors without importing candidate code, adding corroboration rather than autonomous judgment.
- Who acts on findings: campaign manager/integrator revises under recorded issue IDs; controller blocks/returns or marks needs_evidence/rejected instead of fabricating success.
- Evidence: [src/agentforeman/discussion.py](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/discussion.py); [src/agentforeman/campaign.py](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/campaign.py); [src/agentforeman/debate.py](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/debate.py); [src/agentforeman/council.py](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/council.py); [src/agentforeman/templates/moons/verify.py](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/templates/moons/verify.py).
- Basis: structural
- Confidence: medium-high for source topology; live agent efficacy unmeasured.

## S4 — Outside-and-then intelligence

- State: —
- Function: no external-and-prospective adaptation loop changing AgentForeman operational capability.
- Disturbance / variety regulated: new research hypotheses, failed experiment results, provider quota changes and user task uncertainty.
- Decisive decision or feedback right: manager may change candidate experiment code, not harness capability/organization; task chair clarifies current requirements.
- Decision owner: task agents own research outcomes; maintainer/operator owns external product evolution.
- Supporting / enforcement mechanisms: research plans, measurements, council sources, quota information and roadmap.
- Closure path: research findings return to the current task; no prospective environmental judgment returns as a change to harness capability.
- Why this is / is not agent-owned: research as the primary operational transformation is S1; internal optimization and quota reaction do not establish S4.
- Caveats: an operator could use outputs to redesign its organization, but that external act is not a shipped adaptation closure.
- Evidence: [src/agentforeman/manager.py](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/manager.py); [src/agentforeman/campaign.py](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/campaign.py); [src/agentforeman/council.py](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/council.py); [src/agentforeman/briefing.py](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/briefing.py); [docs/ROADMAP.md](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/docs/ROADMAP.md).
- Basis: structural
- Confidence: medium-high for source topology; live agent efficacy unmeasured.

### Absence scope

- Surfaces inspected: Campaign plans/results, council source/synthesis/audit, briefing, provider quotas and roadmap.
- Plausible first-party paths checked: experiment hypothesis/retest, council research, role proposal and changed provider availability.
- Why no material first-party path remains: these paths optimize or clarify supplied task outcomes and restore service; none supplies externally/prospectively grounded adaptation authority plus return changing the harness current capability.

## S5 — Policy and identity

- State: —
- Function: no runtime identity/ultimate-policy adjudication loop established beyond bounded task contracts.
- Disturbance / variety regulated: unclear scope, changed deliverables/acceptance/autonomy and stale user confirmation.
- Decisive decision or feedback right: human confirms a task contract; agents must pause when they report a scope change, rather than decide ultimate policy.
- Decision owner: operator owns the local task mandate; product identity remains maintainer-defined outside runtime.
- Supporting / enforcement mechanisms: version/fingerprint confirmation, allowed-decision/pause fields, frozen checks, scope-change signal and stop controls.
- Closure path: briefing → exact human confirmation → bound child task; requested scope changes pause for new clarification.
- Why this is / is not agent-owned: this is operational task admission and authority bounding; it is not an identity/ultimate-policy dispute between present operations and future adaptation.
- Caveats: contract editing is a real returned human decision but does not by itself satisfy the function-first S5 threshold.
- Evidence: [src/agentforeman/briefing.py](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/briefing.py); [src/agentforeman/task_contract.py](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/task_contract.py); [src/agentforeman/debate.py](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/debate.py); [docs/BRIEFING.md](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/docs/BRIEFING.md).
- Basis: structural
- Confidence: medium-high for source topology; live agent efficacy unmeasured.

### Absence scope

- Surfaces inspected: Briefing schema/edit/confirm/launch, task binding, scope-change pause, configuration and supported governance documentation.
- Plausible first-party paths checked: autonomy and exclusion fields, contract-change request, human edits/confirmation, role selection and termination.
- Why no material first-party path remains: the supported path governs a specific task and its permissions; no material identity/ultimate-policy matter is routed to a legitimate parent and returned as system-level policy.

## Distributed OSS parent arrangement

Contributor governance and maintainer releases remain adjacent. Local operator confirmation binds one task; multiple registered workers do not establish an organization-level S3/S4/S5 parent arrangement.

## Self-hosted and non-human modes

The local CLI/UI and optional shared worker pool use first-party provider adapters. Role credentials and model setup are operator prerequisites. No non-human ultimate-policy mode is established; optional reviewed/council modes supply the stated audit path.

## Recursion

Tasks, contributions and experiment rounds are operational substructures. Nested execution, separate accounts and pooled workers alone do not establish independently viable recursive organizations.

## Variety and escalation

Schema validation, frozen inputs/checks, independent evidence access, quota waits, recovery receipts, bounded revision and cancellation attenuate execution variety. Unresolved issues, missing contributions, explicit scope changes and exhausted budgets preserve partial evidence and stop/pause rather than silently widen authority.

## Evidence gaps

No live LLM/provider/Browser run or research-quality measurement was performed. Native focused tests use explicit fixtures; they corroborate topology only. Initial test import failed because psutil was absent from the default interpreter; after installing dependencies into a temporary directory, 35 focused native briefing/cooperation/council tests passed with scripted results (no live provider). The bundled verifier supports its declared tensor contract, not arbitrary scientific truth. This source review establishes installed roles and feedback, not efficacy or organizational autonomy.

---
harness_id: rsi-flow
project_name: RSI-Flow
repository: https://github.com/quqxui/RSI-Flow
review_ref: 0f87c2b198f22e5697853cfc6d0bf2d002e48ca7
reviewed_at: 2026-10-31
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: A
autonomy_s5: —
---

# RSI-Flow

## Review boundary

- System in focus: The Python RSI-Flow experiment engine and supported native agent execution/proposal integrations, not an arbitrary external target framework's organization.
- Purpose and identity: Run an agent-backed improvement cycle over a versioned target prompt/workflow artifact using experience, candidate proposals, paired evaluation and verified deployment.
- Relevant environment: Operator-specified tasks and feedback, Pi or DeepSeek model-backed task sessions, Codex or command reasoning backend, local artifacts, budgets and execution constraints.
- Standard-distribution boundary: `rsi` CLI/`Engine`, JSON and harness-bundle target adapters, configured command/native task execution, built-in manual or configured command proposal and evaluation/deployment paths.
- Credited operating / distribution surfaces: `src/rsi/engine.py`, six `stage_*` modules, `support_7` contracts/adapters/reasoning/control/storage, `integrations/native` and `integrations/harnesses` wired by the documented run modes.
- Adjacent first-party surfaces excluded from ownership: Examples, tests, benchmark preparation, reports and CI supply evidence or fixtures; they are not independent agents or governance functions of an active run.
- First-party operating / deployment modes considered: Manual-proposal/local demonstration and configured model-assisted candidate proposals with supported native Pi/DeepSeek sessions. Provider integrations need real credentials; no provider run was executed for this review.
- Recursion level: One RSI-Flow improvement installation as the whole; target agent task sessions are operating S1, and improvement proposals target future capability of those sessions.
- Reviewed revision: `0f87c2b198f22e5697853cfc6d0bf2d002e48ca7`.
- Observation date: 2026-10-31.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

`Engine` binds a target adapter, reasoning backend, execution backend, evaluator and search policy. Stage 2 imports version-labelled experience, Stage 3 groups observed failures, Stage 4 invokes a configured proposer and builds a new content-addressed target version, Stage 5 executes baseline/candidate on a shared task protocol, and Stage 6 applies acceptance thresholds and verifies deployment or compensates/rolls back. The native runner wraps frozen Pi/DeepSeek SDK agents with a versioned system prompt and an editable workflow's bounded `agent.prompt` interface; task results and load receipts return to the engine. See [engine](https://github.com/quqxui/RSI-Flow/blob/0f87c2b198f22e5697853cfc6d0bf2d002e48ca7/src/rsi/engine.py), [native runner](https://github.com/quqxui/RSI-Flow/blob/0f87c2b198f22e5697853cfc6d0bf2d002e48ca7/integrations/native/runner.py), [native worker](https://github.com/quqxui/RSI-Flow/blob/0f87c2b198f22e5697853cfc6d0bf2d002e48ca7/integrations/native/worker.mjs), [selection](https://github.com/quqxui/RSI-Flow/blob/0f87c2b198f22e5697853cfc6d0bf2d002e48ca7/src/rsi/stage_6_selection/stage.py).

## Operational model

In the supported native path, an external model operating through a first-party task runner selects actions/responses within a configured target-agent session. Separately, a configured reasoning backend can propose future changes to the target's prompt/workflow on the basis of recorded experience; code validates the proposal, tests a candidate against a frozen protocol, and deploys only when the preselected acceptance rule permits. Model choice in task execution and prospective proposal is agent-owned; fixed acceptance, budget, verification and rollback rules enforce operator-supplied constraints and do not themselves become autonomous organizational discretion.

## S1 — Operations

- State: A
- Function: A configured Pi/DeepSeek agent performs the substantive target task inside a first-party versioned workflow session.
- Disturbance / variety regulated: Task instructions, tool/workspace state, model observations and failed subtasks under an operator-defined experiment.
- Decisive decision or feedback right: The model chooses its response/action within an exposed task turn; results and tool feedback inform subsequent turns where the selected SDK supports them.
- Decision owner: The model-backed target agent operating through the native driver; the engine and experiment runner do not choose its per-task response.
- Supporting / enforcement mechanisms: Native SDK bridge, workspace/runtime snapshots, bounded prompt interface, execution timeout, credentials, receipts and result parsing.
- Closure path: Input task and versioned target artifact → native model-backed agent turn → task/tool result → next agent turn and final response/experiment feedback.
- Boundary reachability: Native integration is shipped under `integrations/native/`, wired to Pi/DeepSeek adapters and documented as supported task execution, rather than only a test mock.
- Why this is / is not agent-owned: The model decides task behavior; removing the native model leaves an experiment runner capable of testing artifacts, not autonomous task judgment.
- Evidence: [native worker](https://github.com/quqxui/RSI-Flow/blob/0f87c2b198f22e5697853cfc6d0bf2d002e48ca7/integrations/native/worker.mjs), [Pi driver](https://github.com/quqxui/RSI-Flow/blob/0f87c2b198f22e5697853cfc6d0bf2d002e48ca7/integrations/harnesses/pi.mjs), [DeepSeek driver](https://github.com/quqxui/RSI-Flow/blob/0f87c2b198f22e5697853cfc6d0bf2d002e48ca7/integrations/harnesses/deepseek.mjs), [README](https://github.com/quqxui/RSI-Flow/blob/0f87c2b198f22e5697853cfc6d0bf2d002e48ca7/README.md).
- Basis: structural.
- Confidence: medium.
- Caveats: Task-level S1 depends on the configured native agent/provider; built-in offline demonstration is not proof of model autonomy or real-provider success.

## S2 — Coordination

- State: —
- Function: No first-party anti-interference coordination among distinct task-performing S1 cells is established.
- Disturbance / variety regulated: Concurrent candidate trials could contend for resources or contaminate comparisons.
- Decisive decision or feedback right: The framework bounds parallel work and separates trial artifacts; no inter-S1 conflict-specific adjustment is evidenced.
- Decision owner: Preselected execution protocol and deterministic trial harness rather than an autonomous coordinator.
- Supporting / enforcement mechanisms: Task batching, trial directories, stable task IDs, budget reservations and timeouts.
- Closure path: Runner results are gathered into comparison; no disturbance-detecting cross-agent coordination decision returns to alter their working relationships.
- Why this is / is not agent-owned: Isolation and scheduling protect tests but are not the S2-specific regulation of interactions between ongoing autonomous S1 units.
- Evidence: [validation stage](https://github.com/quqxui/RSI-Flow/blob/0f87c2b198f22e5697853cfc6d0bf2d002e48ca7/src/rsi/stage_5_validation/stage.py), [budget ledger](https://github.com/quqxui/RSI-Flow/blob/0f87c2b198f22e5697853cfc6d0bf2d002e48ca7/src/rsi/support_7/budget.py), [native runner](https://github.com/quqxui/RSI-Flow/blob/0f87c2b198f22e5697853cfc6d0bf2d002e48ca7/integrations/native/runner.py).
- Basis: structural.
- Confidence: medium.
- Caveats: Different target frameworks may implement their own coordination; those internals are outside this review.

### Absence scope

- Surfaces inspected: Engine run phases, validation trial selection, native driver interface, budget and task identity logic.
- Plausible first-party paths checked: Parallel tasks, shared candidate state, trial scheduling and resource contention for conflict-specific detection and returned S1 regulation.
- Why no material first-party path remains: These paths isolate and compare tasks, not negotiate or regulate specific inter-agent interference; no distinct S2 ownership is exposed.

## S3 — Inside-and-now control

- State: —
- Function: No agent-owned or specifically parent-governed whole-system discretionary control of concurrent current S1 priorities and commitments is established.
- Disturbance / variety regulated: Budget exhaustion, failed trials, protocol violations, incomplete receipts and target-version conflict.
- Decisive decision or feedback right: Acceptance thresholds and stop/rollback predicates are fixed by operator-selected protocol; these do not choose new organizational priorities in a current whole-system view.
- Decision owner: Human configuration supplies constraints, deterministic engine enforces them; no in-run S3 discretion is identified.
- Supporting / enforcement mechanisms: `BudgetLedger`, `SingleRoundSearch`, `decide`, `deploy`, pause/resume/cancel/recover and process isolation.
- Closure path: Status and budget checks deterministically stop, reject or deploy a version; the engine does not revise commitments among distinct ongoing S1 operations.
- Why this is / is not agent-owned: An operational gate and rollback authority do not become managerial judgment merely because they have effect on execution.
- Evidence: [engine](https://github.com/quqxui/RSI-Flow/blob/0f87c2b198f22e5697853cfc6d0bf2d002e48ca7/src/rsi/engine.py), [selection](https://github.com/quqxui/RSI-Flow/blob/0f87c2b198f22e5697853cfc6d0bf2d002e48ca7/src/rsi/stage_6_selection/stage.py), [adapters](https://github.com/quqxui/RSI-Flow/blob/0f87c2b198f22e5697853cfc6d0bf2d002e48ca7/src/rsi/support_7/adapters.py).
- Basis: structural.
- Confidence: medium.
- Caveats: A custom `SearchPolicy` may implement additional control but no such standard autonomous whole-system owner is wired.

### Absence scope

- Surfaces inspected: Engine phases and resume, budget ledger, search policy, acceptance and deployment, native runtime.
- Plausible first-party paths checked: Global budget choices, pause/cancel, candidate acceptance, rollback and operator configuration for whole-system current discretionary resource/priority allocation.
- Why no material first-party path remains: The shipped responses execute predetermined protocol checks and single-round selection; no manager forms a current whole-system judgment and returns revised S1 commitments.

## S3* — Complementary audit

- State: —
- Function: No independent complementary audit of S1 claims with an audit-owned corrective return is established.
- Disturbance / variety regulated: False task success, inaccurate version-loaded claims and unverifiable experiments.
- Decisive decision or feedback right: Evaluator, outcome receipts and load verifier check protocol predicates but do not exercise separate complementary organizational audit judgment.
- Decision owner: The same experiment engine owns ordinary comparison/admission; no independently authorized auditor is composed.
- Supporting / enforcement mechanisms: Paired evaluation, task receipts, exact-version digest, load verification, report evidence and regression thresholds.
- Closure path: Comparison flows into ordinary Stage 6 acceptance; failed load checks trigger procedural rollback, not an independent audit finding sent to a corrective S3 owner.
- Why this is / is not agent-owned: Test comparison and defensive proof of load are valuable controls, but routine QA is not necessarily an independent complementary S3* challenge.
- Evidence: [validation](https://github.com/quqxui/RSI-Flow/blob/0f87c2b198f22e5697853cfc6d0bf2d002e48ca7/src/rsi/stage_5_validation/stage.py), [selection](https://github.com/quqxui/RSI-Flow/blob/0f87c2b198f22e5697853cfc6d0bf2d002e48ca7/src/rsi/stage_6_selection/stage.py), [reports](https://github.com/quqxui/RSI-Flow/blob/0f87c2b198f22e5697853cfc6d0bf2d002e48ca7/src/rsi/support_7/reporting.py).
- Basis: structural.
- Confidence: medium.
- Caveats: An operator can independently inspect raw receipts, but that is not an evidenced first-party audit-return mode.

### Absence scope

- Surfaces inspected: Evaluator contracts, comparison, load probes, reporting/evidence, stage-six control.
- Plausible first-party paths checked: Separate evaluator, immutable snapshots, version receipts and reports for complementary access plus independent challenge and corrective return.
- Why no material first-party path remains: The evaluator performs ordinary admission tests under the same selected protocol; independently owned audit judgment and returned correction are not wired.

## S4 — Outside-and-then intelligence

- State: A
- Function: A configured reasoning agent generates prospective changes to the target agent's prompt/workflow from accumulated experience and diagnosed limitations.
- Disturbance / variety regulated: Recurring task failures, observed regressions, changes in future task mix and limits of the deployed artifact.
- Decisive decision or feedback right: Choose candidate artifact changes, hypothesis and expected benefit, or explicitly propose no change; a subsequent protocol governs acceptance.
- Decision owner: The configured model-backed `CommandProposer` (including the Codex integration) chooses a future adaptation option; the human-proposal mode separately supplies offline input but does not erase the supported autonomous path.
- Supporting / enforcement mechanisms: Structured diagnosis, proposal context, key allowlist, versioned artifact build, baseline/candidate comparison, `decide` and verified `deploy`.
- Closure path: Historical experience → diagnosis → reasoning backend chooses prospective artifact modifications → constrained build and paired evaluation → accepted new deployed artifact changes later target-agent sessions.
- Boundary reachability: `Engine._proposer` selects command reasoning from config and Stage 4 invokes `proposer.propose`; the returned candidate flows into supported Stage 5 and Stage 6 deployment, not merely into documentation.
- External distinction: Imported version-labelled task outcomes and feedback characterize target performance beyond the current agent turn.
- Future / prospective distinction: Proposed prompt/workflow modifications concern future agent capability rather than a response to a present task.
- Adaptation option generated: A structured candidate with `hypothesis`, `expected_benefit` and allowed artifact changes, or `no_change`.
- Path back into current capability / S3: The accepted content-addressed version is loaded/verified for subsequent task runs, with rollback after unsuccessful deployment.
- Why this is / is not agent-owned: The model chooses the substantive candidate hypothesis and changes; deterministic gates can reject it but do not invent the adaptation option.
- Evidence: [proposal reasoning](https://github.com/quqxui/RSI-Flow/blob/0f87c2b198f22e5697853cfc6d0bf2d002e48ca7/src/rsi/support_7/reasoning.py), [engine proposer wiring](https://github.com/quqxui/RSI-Flow/blob/0f87c2b198f22e5697853cfc6d0bf2d002e48ca7/src/rsi/engine.py), [improvement](https://github.com/quqxui/RSI-Flow/blob/0f87c2b198f22e5697853cfc6d0bf2d002e48ca7/src/rsi/stage_4_improvement/stage.py), [deployment](https://github.com/quqxui/RSI-Flow/blob/0f87c2b198f22e5697853cfc6d0bf2d002e48ca7/src/rsi/stage_6_selection/stage.py).
- Basis: structural.
- Confidence: medium.
- Caveats: Autonomous adaptation requires configured reasoning backend and provider; a candidate is not deployed without human-selected test thresholds and successful tests. Source evidence is not a live improvement-outcome claim.

## S5 — Policy and identity

- State: —
- Function: No first-party identity/ultimate-policy dispute resolution and binding return for the RSI installation is established.
- Disturbance / variety regulated: What targets, prompts, models, budgets and artifact fields should be legitimately allowed to change.
- Decisive decision or feedback right: Human operator fixes target schema, allowed keys, model configuration and evaluation rules at initialization; no identity-policy issue is referred to an adjudicator for resolution.
- Decision owner: Operator/developer outside the live run; model proposer is restricted to editable lower-level artifact fields.
- Supporting / enforcement mechanisms: Immutable config hash, key allowlist, model identity snapshots, validation errors and manual stop.
- Closure path: Fixed policy blocks out-of-bounds proposals; it does not carry an identity question to a legitimate policy owner and feed a fresh ruling back into operations.
- Why this is / is not agent-owned: Artifact edits and accepted versions adjust capability, not ultimate purpose/constitutional identity; immutable settings are enforcement not adjudication.
- Evidence: [definition](https://github.com/quqxui/RSI-Flow/blob/0f87c2b198f22e5697853cfc6d0bf2d002e48ca7/src/rsi/stage_1_definition/stage.py), [improvement](https://github.com/quqxui/RSI-Flow/blob/0f87c2b198f22e5697853cfc6d0bf2d002e48ca7/src/rsi/stage_4_improvement/stage.py), [engine](https://github.com/quqxui/RSI-Flow/blob/0f87c2b198f22e5697853cfc6d0bf2d002e48ca7/src/rsi/engine.py).
- Basis: structural.
- Confidence: high.
- Caveats: A developer may deliberately install new policies in a new workspace, but that is not a first-party governed S5 mode.

### Absence scope

- Surfaces inspected: Definition/configuration, artifact schema and allowlists, proposer contract, runtime controls and deployment.
- Plausible first-party paths checked: Self-modification, human proposal input, protocol migration and operator settings for identity-level escalation and authoritative return.
- Why no material first-party path remains: These modify bounded operational artifacts or require a new external configuration; no run-time ultimate-policy decision channel is shipped.

## Distributed OSS parent arrangement

Open-source contributors and local experiment operators can govern their own configurations. There is no evidenced distributed parent that receives individual private runs, adjudicates whole-project operational/future/identity decisions, and returns a binding decision to each running engine.

## Self-hosted and non-human modes

The engine is locally run and can invoke external inference. Offline manual-proposal experiments are not agent-owned adaptation; a configured model proposer supplies the S4 autonomous mode. A task SDK/model likewise supplies S1 choice through the supported native integration. Deployment may require credentials and trusted host access; no security-isolation claim follows from per-trial directories.

## Recursion

The target task agent constitutes an operational cell, while its artifact can be changed by a higher improvement cycle. That shows an S1-to-S4 influence at this chosen level, but not a complete nested viable metasystem or guaranteed RSI of the governing code itself.

## Variety and escalation

The protocol constrains variation via pinned task sets, allowed keys, budgets and fixed acceptance/regression thresholds. Proposer hypotheses amplify possible adaptations; missing data, regression, conflicts and failed version loads stop or roll back. Pause/cancel and recovery are procedural safety controls, not evidence of independent S3* or S5 authority.

## Evidence gaps

Static pin and source-wired modes only; provider-backed task and proposal E2E, demonstrated gains, model reliability and host security were not independently tested. A custom injected search policy or proprietary provider implementation may change behavior outside this distribution, but is not credited. Assessment does not infer separate agentic decision owners from six stage names alone.

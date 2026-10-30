---
harness_id: hermes-loops
project_name: Hermes Loops
repository: https://github.com/AtlasOmnia/hermes-loops
review_ref: dc4a16fb3614b9f5dc2d3b42c9f28bd24191bc5c
reviewed_at: 2026-10-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Hermes Loops

## Review boundary

- System in focus: one local Git experiment loop using the documented first-party agent proposal wrapper in the autoresearch package.
- Purpose and identity: pursue bounded measured repository improvements, retaining accepted local changes and reverting rejected trials.
- Relevant environment: a chosen Git target, external agent executable/provider, caller's objective/evaluator, filesystem changes, failures and score feedback.
- Standard-distribution boundary: source-checkout autoresearch CLI/library plus documented trial-contract/proposal-wrapper operating recipe; the user supplies an agent command and domain evaluator. The default deterministic demo is not the positive S1 witness.
- Credited operating / distribution surfaces: autoresearch/src/hermes_autoresearch, contracts/trial_contract.md and examples/proposal_wrapper_example.py as explicitly documented supported source-checkout integration.
- Adjacent first-party surfaces excluded from ownership: separately installed maintenance package, repository development/tests, deterministic proposal/evaluator fixtures and CI. Linked hermes-custom-pack diagnostic review and NousResearch Hermes internals are external systems.
- First-party operating / deployment modes considered: agent-backed wrapper, arbitrary configured proposal/evaluator commands, dry-run/deterministic example and independently installed read-only maintenance. The latter modes do not donate an agent or metasystem owner.
- Recursion level: one experiment process and its bounded proposal work cell; no whole Hermes installation or community organization included.
- Reviewed revision: dc4a16fb3614b9f5dc2d3b42c9f28bd24191bc5c.
- Observation date: 2026-10-30.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The monorepo contains two independently installed packages. Autoresearch runs a proposal command against a clean target Git tree, inspects changed paths, calls a domain evaluator, parses score/accepted/reason, and commits or reverts according to fixed rules. It passes trial/repository/previous-best-score metadata, writes TSV/JSONL receipts, and applies trial/time/target/no-improvement stop limits. Its documented wrapper appends a one-hypothesis trial contract, objective and allowed paths to an actual Hermes-compatible agent CLI. This is a supported source-checkout recipe, not a bundled model. Arbitrary command mode may be deterministic; inclusion is restricted to the documented agent mode.

Maintenance separately probes a selected Hermes home read-only and evaluates explicitly supplied redacted outcome packets with a frozen rubric. Suggestions are never approved, applied or scheduled by that package. Its name “health audit” does not make it part of autoresearch's audit channel. The linked LLM diagnostic-review skill lives in another repository and is not credited here.

Evidence: [README.md](https://github.com/AtlasOmnia/hermes-loops/blob/dc4a16fb3614b9f5dc2d3b42c9f28bd24191bc5c/README.md#L5-L20), [autoresearch/README.md](https://github.com/AtlasOmnia/hermes-loops/blob/dc4a16fb3614b9f5dc2d3b42c9f28bd24191bc5c/autoresearch/README.md#L1-L24), [autoresearch/src/hermes_autoresearch/orchestrator.py](https://github.com/AtlasOmnia/hermes-loops/blob/dc4a16fb3614b9f5dc2d3b42c9f28bd24191bc5c/autoresearch/src/hermes_autoresearch/orchestrator.py#L60-L89), [autoresearch/examples/proposal_wrapper_example.py](https://github.com/AtlasOmnia/hermes-loops/blob/dc4a16fb3614b9f5dc2d3b42c9f28bd24191bc5c/autoresearch/examples/proposal_wrapper_example.py#L38-L79), [maintenance/src/hermes_maintenance_loops/improvement.py](https://github.com/AtlasOmnia/hermes-loops/blob/dc4a16fb3614b9f5dc2d3b42c9f28bd24191bc5c/maintenance/src/hermes_maintenance_loops/improvement.py#L43-L83).

## Operational model

The proposal agent selects and implements one concrete hypothesis in the allowed target environment. A configured evaluator supplies acceptance evidence; deterministic runtime applies the selected metric policy and persists/reverts edits. The user supplies purpose, provider, scope and domain evaluation. Those setup rights are not automatically S3 or S5 parent governance. The primary transformation is experimental improvement itself; accepted edits do not automatically imply a separate S4 adaptation function.

## S1 — Operations

- State: A
- Function: choose and implement a bounded experimental repository change toward a measured objective.
- Disturbance / variety regulated: uncertain implementation alternatives, repository-specific constraints and previous measured outcomes.
- Decisive decision or feedback right: select one hypothesis and the concrete allowed edits, or determine that the trial is blocked.
- Decision owner: external agent actor invoked by the shipped proposal wrapper in the documented autoresearch operating mode.
- Supporting / enforcement mechanisms: trial prompt, configurable argv, Git allowlist, evaluator parsing, fixed acceptance thresholds, local commit/revert and logs.
- Closure path: trial metadata/current accepted repository reach the agent; agent edits are evaluated, accepted changes become the next working tree and previous best score enters the next trial prompt. Failed/rejected changes may be reverted before the next proposal.
- Boundary reachability: autoresearch README explicitly routes proposal_command through the included wrapper and documents AGENT_COMMAND_JSON with Hermes chat. The wrapper builds the actual contract/objective/metadata prompt and invokes the CLI directly, while the first-party harness invokes that wrapper each trial.
- Why this is / is not agent-owned: Python cannot choose the substantive experimental edit with the same discretion if the configured agent is removed. The deterministic fixture and no-op defaults do not receive A; agent-owned proposal decisions are distinct from deterministic acceptance.
- Evidence: [autoresearch/examples/proposal_wrapper_example.py](https://github.com/AtlasOmnia/hermes-loops/blob/dc4a16fb3614b9f5dc2d3b42c9f28bd24191bc5c/autoresearch/examples/proposal_wrapper_example.py#L38-L79), [autoresearch/contracts/trial_contract.md](https://github.com/AtlasOmnia/hermes-loops/blob/dc4a16fb3614b9f5dc2d3b42c9f28bd24191bc5c/autoresearch/contracts/trial_contract.md#L3-L39), [autoresearch/src/hermes_autoresearch/orchestrator.py](https://github.com/AtlasOmnia/hermes-loops/blob/dc4a16fb3614b9f5dc2d3b42c9f28bd24191bc5c/autoresearch/src/hermes_autoresearch/orchestrator.py#L75-L89), [autoresearch/src/hermes_autoresearch/orchestrator.py](https://github.com/AtlasOmnia/hermes-loops/blob/dc4a16fb3614b9f5dc2d3b42c9f28bd24191bc5c/autoresearch/src/hermes_autoresearch/orchestrator.py#L169-L228).
- Basis: explicit supported integration and structural feedback.
- Confidence: high for source wiring, medium for actual configured deployment.
- Caveats: caller must supply an installed/authenticated agent and evaluator and align prompt scope with the configured allowlist. Source-checkout recipe is credited; wheel-only availability of the example wrapper is not assumed. No live agent run or quality improvement is claimed.

## S2 — Coordination

- State: —
- Function: sought regulate interference among distinct operational units.
- Disturbance / variety regulated: a potential collision of concurrent proposal workers.
- Decisive decision or feedback right: no inter-unit arbitration or feedback right is exposed.
- Decision owner: one proposal command runs serially before its evaluator.
- Supporting / enforcement mechanisms: the sequential trial loop, clean-tree check and allowlist.
- Closure path: a trial's accept/revert result changes the next trial, not a relation among independent concurrent S1 units.
- Why this is / is not agent-owned: the inspected production/support mechanisms do not establish a separate discretionary owner and closure for this function.
- Evidence: [autoresearch/src/hermes_autoresearch/orchestrator.py](https://github.com/AtlasOmnia/hermes-loops/blob/dc4a16fb3614b9f5dc2d3b42c9f28bd24191bc5c/autoresearch/src/hermes_autoresearch/orchestrator.py#L60-L89), [autoresearch/contracts/trial_contract.md](https://github.com/AtlasOmnia/hermes-loops/blob/dc4a16fb3614b9f5dc2d3b42c9f28bd24191bc5c/autoresearch/contracts/trial_contract.md#L8-L26).
- Basis: structural bounded negative.
- Confidence: medium-high.
- Caveats: conclusion is limited to the declared shipped operating boundary, not arbitrary future custom agent composition.

### Absence scope

- Surfaces inspected: serial proposer/evaluator execution, clean Git preconditions, trial contract, wrapper and configuration.
- Plausible first-party paths checked: simultaneous proposers, shared-target writes, trial sequencing and command-error recovery.
- Why no material first-party path remains: only one operational proposal is active; the evaluator is the ordinary acceptance step. No specific inter-S1 collision/attenuation path is supplied by these primitives.

## S3 — Inside-and-now control

- State: —
- Function: sought whole-system current regulation of resources, commitments or priorities.
- Disturbance / variety regulated: competition for current work budget and changing operational priorities.
- Decisive decision or feedback right: no discretionary whole-system regulator or explicit parent current-control loop is established.
- Decision owner: developer/operator chooses initial limits; deterministic Python checks them.
- Supporting / enforcement mechanisms: max_trials/max_seconds, no-improvement stop, target score, timeouts and keep/revert rules.
- Closure path: fixed thresholds stop or continue trials; the runtime does not choose new commitments, negotiate resources or return a supervisory decision.
- Why this is / is not agent-owned: the inspected production/support mechanisms do not establish a separate discretionary owner and closure for this function.
- Evidence: [autoresearch/src/hermes_autoresearch/config.py](https://github.com/AtlasOmnia/hermes-loops/blob/dc4a16fb3614b9f5dc2d3b42c9f28bd24191bc5c/autoresearch/src/hermes_autoresearch/config.py#L11-L32), [autoresearch/src/hermes_autoresearch/orchestrator.py](https://github.com/AtlasOmnia/hermes-loops/blob/dc4a16fb3614b9f5dc2d3b42c9f28bd24191bc5c/autoresearch/src/hermes_autoresearch/orchestrator.py#L169-L246).
- Basis: structural bounded negative.
- Confidence: medium-high.
- Caveats: conclusion is limited to the declared shipped operating boundary, not arbitrary future custom agent composition.

### Absence scope

- Surfaces inspected: budget/termination configuration, acceptance code, CLI, trial prompt and logs.
- Plausible first-party paths checked: score-based acceptance, timeout, stop thresholds, user objective/configuration and maintenance health report.
- Why no material first-party path remains: these implement preselected experiment constraints, not a first-party agent regulator or function-specific parent decision-and-return mode. Ordinary process/configuration control alone does not establish P.

## S3* — Complementary audit

- State: —
- Function: sought independent complementary access that can challenge ordinary production reporting.
- Disturbance / variety regulated: an unreliable claim that a trial improved the target.
- Decisive decision or feedback right: no separate audit channel beyond routine evaluation is established.
- Decision owner: configured evaluator owns ordinary acceptance; no first-party autonomous audit owner is credited.
- Supporting / enforcement mechanisms: evaluator JSON, filesystem diff inspection, experiment logs and independent maintenance reports.
- Closure path: routine score/accepted fields select keep or revert. The maintenance package inspects a selected external Hermes home and is not wired to challenge this trial loop's claims.
- Why this is / is not agent-owned: the inspected production/support mechanisms do not establish a separate discretionary owner and closure for this function.
- Evidence: [autoresearch/contracts/trial_contract.md](https://github.com/AtlasOmnia/hermes-loops/blob/dc4a16fb3614b9f5dc2d3b42c9f28bd24191bc5c/autoresearch/contracts/trial_contract.md#L3-L26), [autoresearch/src/hermes_autoresearch/orchestrator.py](https://github.com/AtlasOmnia/hermes-loops/blob/dc4a16fb3614b9f5dc2d3b42c9f28bd24191bc5c/autoresearch/src/hermes_autoresearch/orchestrator.py#L309-L339), [maintenance/src/hermes_maintenance_loops/health.py](https://github.com/AtlasOmnia/hermes-loops/blob/dc4a16fb3614b9f5dc2d3b42c9f28bd24191bc5c/maintenance/src/hermes_maintenance_loops/health.py#L122-L140).
- Basis: structural bounded negative.
- Confidence: medium-high.
- Caveats: conclusion is limited to the declared shipped operating boundary, not arbitrary future custom agent composition.

### Absence scope

- Surfaces inspected: trial contract, evaluator execution/parser, accept/revert, logs, maintenance probes and combined-report boundary.
- Plausible first-party paths checked: evaluator direct filesystem reading, separate command identity, health audit and suggested diagnostic review skill.
- Why no material first-party path remains: the evaluator is mandatory ordinary production acceptance, not complementary independently governed audit; maintenance is an independently installed observer of another target. The external diagnostic-review skill is not included in this frozen source.

## S4 — Outside-and-then intelligence

- State: —
- Function: sought external/prospective adaptation options coupled back to present capability.
- Disturbance / variety regulated: future inadequacy of an approach under changing external conditions.
- Decisive decision or feedback right: no shipped outside-and-then options/adoption loop is established.
- Decision owner: proposal agent owns the current experiment hypothesis; no distinct S4 owner is established.
- Supporting / enforcement mechanisms: previous best score, trial outcome logs, target edits and maintenance recurrence suggestions.
- Closure path: accepted local edits persist, but persistence and score optimization alone do not establish external prospective sensing/options. Maintenance suggestions are never approved/applied by that package.
- Why this is / is not agent-owned: the inspected production/support mechanisms do not establish a separate discretionary owner and closure for this function.
- Evidence: [autoresearch/examples/proposal_wrapper_example.py](https://github.com/AtlasOmnia/hermes-loops/blob/dc4a16fb3614b9f5dc2d3b42c9f28bd24191bc5c/autoresearch/examples/proposal_wrapper_example.py#L38-L75), [autoresearch/src/hermes_autoresearch/orchestrator.py](https://github.com/AtlasOmnia/hermes-loops/blob/dc4a16fb3614b9f5dc2d3b42c9f28bd24191bc5c/autoresearch/src/hermes_autoresearch/orchestrator.py#L169-L228), [maintenance/src/hermes_maintenance_loops/improvement.py](https://github.com/AtlasOmnia/hermes-loops/blob/dc4a16fb3614b9f5dc2d3b42c9f28bd24191bc5c/maintenance/src/hermes_maintenance_loops/improvement.py#L43-L83).
- Basis: structural bounded negative.
- Confidence: medium-high.
- Caveats: conclusion is limited to the declared shipped operating boundary, not arbitrary future custom agent composition.

### Absence scope

- Surfaces inspected: objective/trial contract, proposal metadata, evaluator acceptance, playbook and maintenance rubric/suggestion lifecycle.
- Plausible first-party paths checked: repository self-improvement, previous-score feedback, reusable experiment changes and recurring-outcome suggestions.
- Why no material first-party path remains: the first-party loop optimizes the declared current experimental objective; arbitrary target code or an unimplemented human follow-up does not supply a distinct externally prospective adaptation and returned-adoption path.

## S5 — Policy and identity

- State: —
- Function: sought identity/ultimate-policy closure.
- Disturbance / variety regulated: a conflict over experiment purpose, permitted scope or fundamental acceptance criteria.
- Decisive decision or feedback right: no runtime identity-level escalation, legitimate decision and authoritative return path is supplied.
- Decision owner: user authors objective and constraints before execution; no S5 owner is credited.
- Supporting / enforcement mechanisms: static one-hypothesis prompt, allowlist, trusted-command choice and evaluator contract.
- Closure path: blocked proposal exits nonzero and may revert; it does not route an identity dispute to a legitimate parent and re-ground operation under a returned decision.
- Why this is / is not agent-owned: the inspected production/support mechanisms do not establish a separate discretionary owner and closure for this function.
- Evidence: [autoresearch/contracts/trial_contract.md](https://github.com/AtlasOmnia/hermes-loops/blob/dc4a16fb3614b9f5dc2d3b42c9f28bd24191bc5c/autoresearch/contracts/trial_contract.md#L6-L39), [autoresearch/examples/proposal_wrapper_example.py](https://github.com/AtlasOmnia/hermes-loops/blob/dc4a16fb3614b9f5dc2d3b42c9f28bd24191bc5c/autoresearch/examples/proposal_wrapper_example.py#L38-L75), [autoresearch/src/hermes_autoresearch/config.py](https://github.com/AtlasOmnia/hermes-loops/blob/dc4a16fb3614b9f5dc2d3b42c9f28bd24191bc5c/autoresearch/src/hermes_autoresearch/config.py#L11-L32).
- Basis: structural bounded negative.
- Confidence: medium-high.
- Caveats: conclusion is limited to the declared shipped operating boundary, not arbitrary future custom agent composition.

### Absence scope

- Surfaces inspected: trial objective/prompt, allowlist/configuration, failure/revert paths, CLI, README and separate maintenance authority limits.
- Plausible first-party paths checked: blocked proposal exit, user-configurable objective, keep/revert acceptance and suggestion-only human review.
- Why no material first-party path remains: setup permission, static policy text and ordinary experiment acceptance do not supply a function-specific ultimate-policy decision loop; no in-boundary parent mode or autonomous identity owner is wired.

## Recursion

Trials are iterations of one operational experiment, not recursively viable organizations. Hermes/provider internals, maintenance of a different selected installation and community governance remain outside the credited trial boundary.

## Variety and escalation

One-hypothesis scope and allowed paths attenuate trial variety; the agent handles substantive edit alternatives. Evaluator feedback, Git reversion, timeout and no-improvement stops constrain the experiment. Nonzero blocked exit is an error signal, not an identity-level parent loop or automatically an algedonic channel.

## Evidence gaps

Pinned static review and native deterministic tests only; no live LLM/provider or agent E2E. Autoresearch tests passed 17/17 in an isolated pytest environment; separately inspected maintenance passed 38/38 with its documented source import path. Initial missing pytest/import-path test-environment failures were recovered without modifying upstream source. These fixtures verify contract/wiring rather than agent quality. The arbitrary-command/default modes can run without an agent; positive inclusion is scoped to the explicitly documented source-checkout agent-wrapper mode.

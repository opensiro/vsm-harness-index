---
harness_id: ace
project_name: ACE
repository: https://github.com/ace-agent/ace
review_ref: 82709de050e1db6e6ef2f07bcb0393560b94992a
reviewed_at: 2026-10-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: C
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# ACE

## Review boundary

- System in focus: the source-distributed Agent–Curator–Environment (ACE) answer-generation and playbook-learning harness, from configured sample and optional ground truth through Generator, Reflector, Curator, validation, and subsequently reused playbook. The alternate `ACEBatch` parallel mode is included because it is a shipped executable first-party mode.
- Purpose and identity: generate answers to task samples and revise an instruction playbook through supervised/reflection-based experience; distinguish the loop's learning utility from external-future organizational intelligence.
- Relevant environment: supplied dataset questions/contexts/targets, answer-correctness processor, model endpoint responses and failures, validation outcomes, playbook size, and mode/configuration inputs.
- Standard distribution: `ace/ace.py` sequential `offline`, `online`, `eval_only` and `ace/ace_batch.py` batched offline/online modes, documented run and extension surfaces; `ace/core/`, `playbook_utils.py`, `utils.py` and `eval/` adapters. This is a locally launched research/training application, not a perpetual self-governing service.
- Included first-party surfaces: [`ace/ace.py`](https://github.com/ace-agent/ace/blob/82709de050e1db6e6ef2f07bcb0393560b94992a/ace/ace.py), [`ace/ace_batch.py`](https://github.com/ace-agent/ace/blob/82709de050e1db6e6ef2f07bcb0393560b94992a/ace/ace_batch.py), [`ace/core/generator.py`](https://github.com/ace-agent/ace/blob/82709de050e1db6e6ef2f07bcb0393560b94992a/ace/core/generator.py), [`ace/core/reflector.py`](https://github.com/ace-agent/ace/blob/82709de050e1db6e6ef2f07bcb0393560b94992a/ace/core/reflector.py), [`ace/core/curator.py`](https://github.com/ace-agent/ace/blob/82709de050e1db6e6ef2f07bcb0393560b94992a/ace/core/curator.py), [`playbook_utils.py`](https://github.com/ace-agent/ace/blob/82709de050e1db6e6ef2f07bcb0393560b94992a/playbook_utils.py).
- Credited operating / distribution surfaces: shipped `ACE` and `ACEBatch` runners, the three first-party agent roles and the common playbook update utilities listed above.
- Adjacent first-party surfaces excluded from ownership: evaluation adapters, tutorials and experiment preparation outside the selected runtime are not credited as autonomous controllers; hosted model-provider reasoning infrastructure, external benchmark datasets and annotations, human designer's future releases/policies and organizational repository governance are outside the boundary.
- Modes: sequential and batched training, optional ground-truth-free reflection, validation-based selection, evaluation-only. Positive S2 is scoped to the batched mode with multiple sample and curator-proposal cells, not projected onto the serial mode.
- Recursion level: one task-learning harness. Each sample's generator/reflection pair is an operational cell; separate viable organizations are not evidenced.
- Reviewed revision: `82709de050e1db6e6ef2f07bcb0393560b94992a`; observation date: 2026-10-30; Profile 0.2.4 and Methodology 0.3.7 (generated/current).

## Repository architecture

`ACE.run` dispatches to offline training, online test-then-train windows, or evaluation only. `_train_single_sample` invokes a model-backed Generator, checks `data_processor.answer_is_correct` against the sample target, lets a separate model-backed Reflector inspect the response and assign helpful/harmful bullet tags, regenerates on error, and periodically invokes a model-backed Curator whose `ADD`/`UPDATE`/`MERGE`/`DELETE` operations are applied to the shared playbook. It generates once more against the updated playbook. Validation accuracy is periodically computed and the best playbook saved for final evaluation. `ACEBatch._train_batch` additionally evaluates sample cells in parallel on a shared playbook snapshot; multiple curator proposal groups operate against the same base, and an LLM-backed reducer deduplicates/merges their proposals before a single update. These are tangible in-source feedback paths, not claims of execution success on an untested provider.

## Operational model

One run transforms user-supplied tasks into answers, corrected attempts and an updated playbook for later samples. Model-generated text and curator operations are discretionary; deterministic code checks supplied targets, schedules rounds, applies operations, rolls back selected failures, bounds token usage and preserves artifacts. The local caller supplies tasks, targets and mode. The training loop may improve later task answers, but code does not itself research future external environmental change or renegotiate ultimate system identity.

## S1 — Operations

- State: A
- Function: produce domain-task answers and revise the working solution with input, playbook and environment/target feedback.
- Disturbance / variety regulated: heterogeneous questions, contexts, mismatches against targets, reasoning errors and model/tool failures.
- Decisive decision or feedback right: Generator makes answer/reasoning choices; Reflector diagnoses error and proposes corrective reflection; Curator chooses playbook operations that change subsequent generation.
- Decision owner: first-party configured model-backed `Generator`, `Reflector` and `Curator` acting as a linked operational learning cell, with deterministic correctness check and parsing as enforcement.
- Supporting / enforcement mechanisms: `answer_is_correct`, `update_bullet_counts`, `apply_curator_operations`, JSON parsing, retries, token limits and configured step frequencies.
- Closure path: sample → generate → check/reflect → revise candidate answer and playbook → post-curator answer, then changed playbook reaches later samples/windows.
- Boundary reachability: `_offline_train`, `_online_train_and_test` and batched mode call these steps in the shipped run paths.
- Why this is / is not agent-owned: the model selects response content and playbook changes; the Python shell does not supply these discretionary answers/operations.
- Evidence: [`ace/ace.py`](https://github.com/ace-agent/ace/blob/82709de050e1db6e6ef2f07bcb0393560b94992a/ace/ace.py) (`_train_single_sample`, `_offline_train`); [`ace/core/curator.py`](https://github.com/ace-agent/ace/blob/82709de050e1db6e6ef2f07bcb0393560b94992a/ace/core/curator.py) (`curate`); [`ace/core/reflector.py`](https://github.com/ace-agent/ace/blob/82709de050e1db6e6ef2f07bcb0393560b94992a/ace/core/reflector.py).
- Basis: structural.
- Confidence: high for configured source behavior, not measured model effectiveness.
- Caveats: `eval_only` intentionally does not run the adaptation path.

## S2 — Coordination

- State: A
- Function: attenuate interference when independent sample/reflection and curator-proposal cells attempt to contribute overlapping or conflicting modifications to one shared playbook.
- Disturbance / variety regulated: parallel curator cells can propose duplicated/conflicting updates and cause shared-playbook order dependence.
- Distinct S1 units: multiple parallel generator/reflection sample cells and multiple parallel curator proposal groups over separate sample subsets within `ACEBatch._train_batch`.
- Inter-S1 disturbance: proposals from simultaneous groups may duplicate insight bullets or produce incompatible add operations; applying each immediately would make resulting knowledge order-dependent.
- Attenuating coordination relation: all groups read the same frozen `base_playbook`, only propose operations, and a single model-backed `Curator.aggregate_operations` reducer merges/deduplicates before atomic `apply_curator_operations`.
- Feedback into subsequent S1 behaviour: the reconciled shared playbook is passed to parallel post-curator generation and later samples; contradictory independent writes are not directly committed.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: unlike generic fan-out/fan-in, the reducer resolves conflicting/redundant knowledge contributions into one coherent shared operating resource.
- Decisive decision or feedback right: choose which candidate ADD operations survive and how to combine them; Python enforces single-application order.
- Decision owner: model-backed Curator reducer, with deterministic snapshot/aggregation and schema checks as support.
- Supporting / enforcement mechanisms: thread pool, group sorting, common snapshot, operations schema, reducer prompt, once-only playbook update.
- Closure path: parallel proposals → reducer selection → updated playbook → revised answer generation in the same batch.
- Boundary reachability: source-distributed `ACEBatch._train_batch` calls `propose_operations`, `aggregate_operations` and `apply_curator_operations`; depends on configured batched path and nonempty proposals.
- Why this is / is not agent-owned: the reducer model resolves semantic overlap; deterministic code performs serialization only.
- Evidence: [`ace/ace_batch.py`](https://github.com/ace-agent/ace/blob/82709de050e1db6e6ef2f07bcb0393560b94992a/ace/ace_batch.py) (`_train_batch` three phases); [`ace/core/curator.py`](https://github.com/ace-agent/ace/blob/82709de050e1db6e6ef2f07bcb0393560b94992a/ace/core/curator.py) (`propose_operations`, `aggregate_operations`).
- Basis: structural.
- Confidence: medium, conditional on nontrivial batched groups and model outputs.
- Caveats: batching and generic task sequencing alone do not count; the positive evidence is the specific shared-playbook conflict reducer.

## S3 — Inside-and-now control

- State: C
- Function: regulate present training-system performance and decide which installed playbook to use for final operational evaluation.
- Whole-system current view: periodic aggregate training and held-out validation accuracy summarizes current performance across sample cells, not merely one answer.
- Current-control decision scope: save the best aggregate-performing playbook and select that snapshot for final test under a global configured criterion.
- Disturbance / variety regulated: local learning steps can improve one sample while degrading aggregate validation accuracy or consuming the configured training budget.
- Decisive decision or feedback right: periodic aggregate validation computes accuracy and saves the best-scoring `self.best_playbook`; final test uses that selected snapshot rather than automatically using the latest playbook.
- Decision owner: deterministic first-party ACE orchestrator, applying the user-configured validation criterion and schedule; no model-owned whole-run intervention is established.
- Supporting / enforcement mechanisms: `evaluate_test_set`, `eval_steps`, `best_accuracy`, `self.best_playbook`, saved checkpoints.
- Closure path: sample-level operational updates → aggregate validation feedback → selected best playbook → final test generator.
- Boundary reachability: `ACE._offline_train` updates `best_playbook`, and `ACE.run(mode='offline')` explicitly calls `_run_test(... playbook=self.best_playbook)` when test samples exist.
- Why this is / is not agent-owned: the criterion is fixed, selection is a numeric comparison, and model agents do not negotiate cross-cell performance commitments or revise global budgets.
- Evidence: [`ace/ace.py`](https://github.com/ace-agent/ace/blob/82709de050e1db6e6ef2f07bcb0393560b94992a/ace/ace.py) (`_offline_train` periodic validation, `run` final test).
- Basis: structural.
- Confidence: medium.
- Caveats: offline mode requires supplied validation/test data and user configuration.

## S3* — Complementary audit

- State: —
- Function: no separate complementary access to actual operations beyond the normal answer-check/reflection and validation workflow.
- Disturbance / variety regulated: wrong generated answers are noticed, but the same ordinary training process uses target data and prompts the Reflector; no sporadic independent probe of actual operations is established.
- Decisive decision or feedback right: `answer_is_correct` and `evaluate_test_set` score the known sample targets; `Reflector.reflect` receives the same trace/prediction plus the supplied target, and directly participates in the production correction loop.
- Decision owner: regular orchestrator and model-backed Reflector, not an independent metasystem audit owner.
- Supporting / enforcement mechanisms: task processor, answer comparison, logs, reflector prompts, validation metrics.
- Closure path: correction loops back to the same generator; this is ordinary learning/QA, without a complementary inspection channel to S3.
- Why this is / is not agent-owned: a model critic is agentic, but its mandatory in-line function and information sources do not establish independent audit of ordinary operational claims.
- Evidence: [`ace/ace.py`](https://github.com/ace-agent/ace/blob/82709de050e1db6e6ef2f07bcb0393560b94992a/ace/ace.py) (`_train_single_sample`, `_run_test`); [`ace/core/reflector.py`](https://github.com/ace-agent/ace/blob/82709de050e1db6e6ef2f07bcb0393560b94992a/ace/core/reflector.py).
- Basis: structural.
- Confidence: medium.
- Caveats: independently annotated targets still enter regular training and testing, not a separate surprise-audit access path.

### Absence scope

- Surfaces inspected: sequential and batched orchestrators, task processors/evaluation calls, Reflector input and prompts, Curator, output logs and training/testing entry points.
- Plausible first-party paths checked: external provided target in `answer_is_correct`, separate Reflector model, validation held-out samples, per-call tracing and persisted test error logs.
- Why no material first-party path remains: each is a routine scheduled element of training/evaluation; no separate independent surprise inspection, operational replay or complementary S3* report-to-control path is wired into the assessed runtime.

## S4 — Outside-and-then intelligence

- State: —
- Function: no established externally and prospectively oriented intelligence function despite durable playbook learning.
- Disturbance / variety regulated: the incoming task distribution and correctness feedback alter task-solving heuristics, but neither future external trends nor prospective strategic options are modeled.
- Decisive decision or feedback right: Curator chooses new reusable bullets based on recent reflections, current context and token budget, not observed shifts in the outside environment or future risks/opportunities.
- Decision owner: model-backed Curator for in-domain learning; no first-party S4 decision owner at this organizational boundary.
- Supporting / enforcement mechanisms: playbook text, curator operations, offline/online training windows, validation and saved best playbook.
- Closure path: learned bullets do return to present execution, but the required outside-and-then sensing/option-development half of the S3–S4 loop is absent.
- Why this is / is not agent-owned: generic experience replay, memory consolidation, reflection and improvement of later answers alone are insufficient for S4; the Curator has agentic operational learning rights only.
- Evidence: [`ace/ace.py`](https://github.com/ace-agent/ace/blob/82709de050e1db6e6ef2f07bcb0393560b94992a/ace/ace.py) (`_train_single_sample`, `_online_train_and_test`); [`ace/core/curator.py`](https://github.com/ace-agent/ace/blob/82709de050e1db6e6ef2f07bcb0393560b94992a/ace/core/curator.py).
- Basis: structural.
- Confidence: high for the path distinction, without live evaluation.
- Caveats: future task distribution could shift, but no prospective external-trend/options loop was located.

### Absence scope

- Surfaces inspected: offline/online/eval-only modes, streaming sample training, Curator prompts/operations, validation/best-playbook selection, batched grouping.
- Plausible first-party paths checked: current input as environmental feedback, online windows, durable playbook updates, best-validation snapshot, saved model logs.
- Why no material first-party path remains: these are bounded learning and validation surfaces tied to supplied tasks, without a coded prospective model of an external operating environment, alternatives and return to current organizational capability via S3.

## S5 — Policy and identity

- State: —
- Function: no legitimate runtime ultimate-policy/identity deliberation path at the assessed ACE recursion.
- Disturbance / variety regulated: model provider choice, token budgets and evaluation/training settings are launch-time constants; corrective bullet changes do not arbitrate mission or values.
- Decisive decision or feedback right: external experiment operator specifies the task, config, models and ground-truth availability; code does not escalate ultimate-policy conflicts to a parent and return ratified decisions.
- Decision owner: operator/developer outside the first-party runtime's accountable policy path; model agents choose task answers and playbook tactics, not legitimate identity governance.
- Supporting / enforcement mechanisms: configs, static prompts, token budgets, mode validation, error paths.
- Closure path: no policy-level issue-and-ratification return is found, only ordinary config and supervised training.
- Why this is / is not agent-owned: a prompt and configurable constraint are not S5 authority.
- Evidence: [`ace/ace.py`](https://github.com/ace-agent/ace/blob/82709de050e1db6e6ef2f07bcb0393560b94992a/ace/ace.py) (`__init__`, `_extract_config_params`, `run`); [`ace/prompts/curator.py`](https://github.com/ace-agent/ace/blob/82709de050e1db6e6ef2f07bcb0393560b94992a/ace/prompts/curator.py).
- Basis: structural.
- Confidence: medium.
- Caveats: human maintainer governance outside the runtime does not establish a first-party policy return loop.

### Absence scope

- Surfaces inspected: documented run paths, config/mode selection, agent prompts, playbook operations, validation, errors and repository entry points.
- Plausible first-party paths checked: user-supplied targets, Curator changing playbook rules, fixed token budgets, training mode transitions and human-authored release governance.
- Why no material first-party path remains: the Curator changes operational heuristics only; no identified identity/ultimate-policy issue is routed to legitimate authority and returned as a system-governing decision.

## Distributed OSS parent arrangement

The maintainers publish a training framework, not a first-party parent policy organization accessible to a running ACE instance. User-provided configs and upstream project maintenance remain external. No parent S5 closure is counted.

## Self-hosted and non-human modes

Provider models can act without interactive human intervention during a configured batch. Switching model endpoints does not change the ownership split between model-generated operation choices and deterministic validation/commit logic. No shipped fully autonomous policy loop is established.

## Recursion

Sample-level parallel cells serve one shared training application. They have local sample variety and output decisions, but no evidenced distinct S3/S4/S5 metasystem or ultimate policy identity; the batch hierarchy is not itself recursive VSM viability.

## Variety and escalation

Generator/Reflector absorb varied task inputs; ground truth attenuates erroneous answers, while a Curator recombines learning into a compressed reusable playbook. The batch reducer attenuates competing knowledge proposals. Aggregate validation selects a stable best snapshot. Error logs and provider failures are normal control information, not by themselves algedonic channels or policy escalation.

## Evidence gaps

- Source-based structural assessment only; no hosted LLM, benchmark evaluation, training or quality-success claim was executed.
- Batched S2 autonomy is conditional on nonempty parallel proposal groups, and reducer quality is unmeasured. Serial mode does not have that inter-cell collision mechanism.
- Held-out validation provides a different sample set, but its planned benchmark nature does not establish S3* independence from the ordinary test/control process.

---
harness_id: meta-agent
project_name: Meta-Agent
repository: https://github.com/canvas-org/meta-agent
review_ref: 28e18519eba79e0e97217989390704167c43a5c8
reviewed_at: 2026-10-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: C
autonomy_s3_star: —
autonomy_s4: A
autonomy_s5: —
---

# Meta-Agent

## Review boundary

- System in focus: the executable, first-party Meta-Agent harness optimization loop that runs task-facing model harnesses, persists trajectories, proposes code changes, evaluates candidate harnesses and selects their successors. The optional experimental proposer-skill evolver is separately noted within this boundary.
- Purpose and identity: improve an existing model-backed task harness without model weight updates by repeatedly altering the program around the model.
- Relevant environment: externally supplied benchmark tasks, failed traces and judge/label feedback, model runtime behavior, candidate program errors, held-out task outcomes, cost and search budget.
- Standard-distribution boundary: `meta_agent/loop/`, `task_runner/`, `core/experience.py`, `core/benchmark.py`, `proposer_instructions/` and supported target harness adapters called by the installed CLI.
- Credited operating / distribution surfaces: [`loop/epoch.py`](https://github.com/canvas-org/meta-agent/blob/28e18519eba79e0e97217989390704167c43a5c8/meta_agent/loop/epoch.py), [`loop/proposer.py`](https://github.com/canvas-org/meta-agent/blob/28e18519eba79e0e97217989390704167c43a5c8/meta_agent/loop/proposer.py), [`loop/state.py`](https://github.com/canvas-org/meta-agent/blob/28e18519eba79e0e97217989390704167c43a5c8/meta_agent/loop/state.py), [`core/experience.py`](https://github.com/canvas-org/meta-agent/blob/28e18519eba79e0e97217989390704167c43a5c8/meta_agent/core/experience.py), [`loop/skill_evolver.py`](https://github.com/canvas-org/meta-agent/blob/28e18519eba79e0e97217989390704167c43a5c8/meta_agent/loop/skill_evolver.py), and benchmark/task-runner adapters invoked by the loop.
- Adjacent first-party surfaces excluded from ownership: bundled benchmark fixtures, task datasets, research paper/figures, offline report preparation, CI/release, maintainer governance and third-party model/judge provider implementations; externally optimized target harnesses are action objects under this optimizer, not additional first-party metasystem actors.
- First-party operating / deployment modes considered: CLI `meta-agent loop` with search selection and optional held-out acceptance, single/multi-candidate iterations, optional `--evolve-skill` slow loop, configured Claude/Codex proposer backend and local/Modal evaluation adapters.
- Recursion level: a run of the optimizer supervising multiple task-sample operational evaluations and candidate harness revisions; not a production organization that wholly owns external benchmarks.
- Reviewed revision: `28e18519eba79e0e97217989390704167c43a5c8`.
- Observation date: 2026-10-30.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The installed CLI initializes a benchmark and an experience store. A run evaluates a baseline, invokes a model-backed proposer through a coding-agent backend, verifies candidate files, smoke-tests and runs the task harness on selected benchmark tasks, saves scores/traces, optionally checks a held-out split and records acceptance decisions. In multi-candidate mode sibling proposals and holdout tests can run in parallel; a chosen candidate becomes the next parent/champion. `invoke_proposer` explicitly gives the proposing model previous runs, failure evidence, candidate hypotheses, editing instructions and permitted source surfaces. Experience artifacts store both wins and failures for later proposals. `SkillEvolver` is an opt-in separate model call that analyzes previous proposer traces and outcomes and updates its future instructions, subject to validation. The score threshold/selection and archive mechanics remain deterministic even though model-backed proposal choices are discretionary. Benchmark labels/judges, external hosted models and research publication are not first-party authority.

## Operational model

Task-runner cells execute candidate harness programs on supplied tasks and return traces/results; the model proposer uses observed operational failures to generate prospective alternative operating procedures. The outer loop evaluates variants, takes the selected configuration as its next working parent and iterates. This is a supported adaptation system, but its success is contingent on external model/judge execution; no experiment is claimed here. Parallel candidate search is a portfolio, not evidence of conflicting independent S1 units requiring S2 coordination. Held-out validation is a normal candidate-selection path, not automatically a separate complementary audit of live operations.

## S1 — Operations

- State: A
- Function: perform model-led task-solving harness execution and generate actionable revised harness programs under the optimizer's run objective.
- Disturbance / variety regulated: heterogeneous benchmark tasks, failures, noisy reward/trace outcomes and implementation defects in candidate programs.
- Decisive decision or feedback right: task-facing program harness calls the configured model and chooses task response/actions; model-backed proposer diagnoses examples and writes new program/prompt/tool changes.
- Decision owner: model-backed target harness in task cells, and model-backed proposer for operative candidate generation, with the external model provider furnishing computation.
- Supporting / enforcement mechanisms: benchmark adapters, task runner, proposer invocation, staging directories, validation/smoke checks and run budget.
- Closure path: benchmark task → candidate model/harness actions → result/trace/reward → proposed code changes → next candidate evaluation.
- Boundary reachability: CLI `loop` invokes task-runner and `invoke_proposer` in its shipped `epoch.py` code path, with explicit backend/benchmark choices.
- Why this is / is not agent-owned: model agents choose meaningful answers and candidate edits; Python scripts validate and schedule their choices.
- Evidence: [`README.md`](https://github.com/canvas-org/meta-agent/blob/28e18519eba79e0e97217989390704167c43a5c8/README.md) (harness API/CLI), [`loop/epoch.py`](https://github.com/canvas-org/meta-agent/blob/28e18519eba79e0e97217989390704167c43a5c8/meta_agent/loop/epoch.py), [`loop/proposer.py`](https://github.com/canvas-org/meta-agent/blob/28e18519eba79e0e97217989390704167c43a5c8/meta_agent/loop/proposer.py), [`task_runner/program.py`](https://github.com/canvas-org/meta-agent/blob/28e18519eba79e0e97217989390704167c43a5c8/meta_agent/task_runner/program.py).
- Basis: explicit/structural.
- Confidence: high for wired source path, no success benchmark independently rerun.
- Caveats: user supplies benchmark/model credentials; local task harnesses may operate under different target adapters.

## S2 — Coordination

- State: —
- Function: no demonstrated function-specific attenuation of disturbance among distinct simultaneously acting S1 operational units.
- Disturbance / variety regulated: multiple candidate harnesses can be evaluated and selected, but their score comparison is an adaptation/selection process, not inter-S1 conflict/oscillation regulation.
- Decisive decision or feedback right: multi-candidate workflow persists separate results and picks the higher reward; no identified live interference/negotiation right between independent operating cells.
- Decision owner: deterministic selection policy and configured proposer for candidate exploration, not a team coordination authority.
- Supporting / enforcement mechanisms: isolated candidate directories, fan-out evaluation, structured results and reward sorting.
- Closure path: candidate scores feed selection of future harness, not an S2-specific interference signal returned to current colliding S1 units.
- Why this is / is not agent-owned: parallel experiments and comparison do not by themselves supply VSM coordination at the declared recursion.
- Evidence: [`loop/epoch.py`](https://github.com/canvas-org/meta-agent/blob/28e18519eba79e0e97217989390704167c43a5c8/meta_agent/loop/epoch.py) (`_run_one_epoch_multi`, holdout fanout, winner selection), [`core/experience.py`](https://github.com/canvas-org/meta-agent/blob/28e18519eba79e0e97217989390704167c43a5c8/meta_agent/core/experience.py).
- Basis: structural.
- Confidence: medium-high for bounded experiment pipeline.
- Caveats: downstream target harnesses could have their own multi-agent coordination, not inherited by the meta-optimizer.

### Absence scope

- Surfaces inspected: single/multiple candidate epoch execution, task runner concurrency, staging/validation, shared history and candidate comparison.
- Plausible first-party paths checked: sibling fanout, file staging isolation, score leaderboards, proposer history and task-level retries.
- Why no material first-party path remains: inspected concurrency isolates alternative experiments and selects later configurations, without a supported disturbance/feedback path attenuating interference among currently operating S1 units.

## S3 — Inside-and-now control

- State: C
- Function: regulate present performance across task-sample cells and control which validated harness configuration becomes the accepted whole-run champion.
- Disturbance / variety regulated: local candidate changes may overfit seen failures, fail smoke tests or regress aggregate task accuracy/cost.
- Whole-system current view: `LoopState.history`, baseline/epoch score summaries and optional held-out aggregate metrics summarize current results across candidate/task evaluations.
- Current-control decision scope: reject structurally invalid candidates, compare aggregate search/holdout performance and choose the next working parent/best-so-far harness under the run's configured acceptance criterion.
- Decisive decision or feedback right: code computes reward, evaluates all eligible siblings and updates `best_rate`/parent selection; with `--accept-on-holdout`, holdout score can gate promotion.
- Decision owner: deterministic first-party loop carrying a developer/operator-defined scoring and acceptance policy; no autonomous agent owns the decisive global acceptance criterion in the standard run.
- Supporting / enforcement mechanisms: `validate_config`, `smoke_candidate`, score aggregation, archived experience and best-rate history.
- Closure path: task-cell outcomes → aggregate score/current candidate comparison → selected best parent → next proposer context and subsequent candidate run.
- Boundary reachability: `epoch.py` calls `_select_parent_candidate_name` and updates the champion in the shipped CLI, including optional but first-party holdout acceptance mode.
- Why this is / is not agent-owned: model proposer writes possible adaptations; deterministic acceptance and experiment configuration choose the installed champion based on numeric criterion, so ownership remains constructor/control machinery rather than agent discretionary S3.
- Evidence: [`loop/epoch.py`](https://github.com/canvas-org/meta-agent/blob/28e18519eba79e0e97217989390704167c43a5c8/meta_agent/loop/epoch.py) (`_finalize_epoch`, `_run_one_epoch_multi`, `winner_idx`), [`loop/state.py`](https://github.com/canvas-org/meta-agent/blob/28e18519eba79e0e97217989390704167c43a5c8/meta_agent/loop/state.py), [`loop/validate.py`](https://github.com/canvas-org/meta-agent/blob/28e18519eba79e0e97217989390704167c43a5c8/meta_agent/loop/validate.py).
- Basis: structural.
- Confidence: medium; selection is run-level rather than continuous production governance.
- Caveats: holdout may fail and source intentionally falls back to search reward; this weakens external-validity protection, not the existence of the selection path.

## S3* — Complementary audit

- State: —
- Function: no separate independent spot inspection of actual operations with corrective feedback into S3 beyond the ordinary score/validation path is established.
- Disturbance / variety regulated: flawed or misleading candidate results are caught by validation, smoke tests and scoring, which form normal run acceptance rather than a separate audit function.
- Decisive decision or feedback right: held-out evaluation may use unseen tasks and a judge/label distinct from the proposer, but it is the configured ordinary acceptance metric rather than an independent complementary inspection channel.
- Decision owner: benchmark/scoring adapters and fixed run policy; no separately independent audit judgment owner with authority to challenge S3 reports.
- Supporting / enforcement mechanisms: proposer-readable trace restrictions, holdout aggregate isolation, config validation, smoke runs and score records.
- Closure path: held-out score enters the ordinary best-candidate selector; no audit finding reaches a distinct supervisory corrective path.
- Why this is / is not agent-owned: independence of a validation split from proposer prompts does not by itself establish organizational complementary audit of current operations.
- Evidence: [`loop/epoch.py`](https://github.com/canvas-org/meta-agent/blob/28e18519eba79e0e97217989390704167c43a5c8/meta_agent/loop/epoch.py) (`_strip_holdout_from_meta`, `run_evaluation`, `_finalize_epoch`), [`task_runner/judge_runner.py`](https://github.com/canvas-org/meta-agent/blob/28e18519eba79e0e97217989390704167c43a5c8/meta_agent/task_runner/judge_runner.py).
- Basis: structural.
- Confidence: medium.
- Caveats: benchmark quality, blind independence and label reliability are external and not independently verified here.

### Absence scope

- Surfaces inspected: search/holdout scoring, proposer prompt isolation, validation/smoke stages, candidate trace persistence and judge adapters.
- Plausible first-party paths checked: held-out evaluator, smoke gate, trace-backed checks and separate judge task runner.
- Why no material first-party path remains: these are routine required experiment selection/QA paths; an independently directed inspection of production reality and a returned corrective S3 audit channel are not supplied at this boundary.

## S4 — Outside-and-then intelligence

- State: A
- Function: sense failures in the external task/benchmark environment, formulate prospective changes to the harness decision procedure and feed viable options back to the active capability configuration.
- Disturbance / variety regulated: changes and differences in task demand, failure patterns, judge feedback, tool/reasoning deficits and overfitting risk across unseen tasks.
- Decisive decision or feedback right: model-backed proposer studies previous trajectories and hypotheses, writes candidate future harness programs; optional model-backed skill evolver derives generalizable process updates from cross-epoch failure/success patterns.
- Decision owner: first-party configured proposer model (and optional second evolution model) for semantic adaptation options; deterministic validation/selection enforces the configured promotion criterion.
- Supporting / enforcement mechanisms: experience store, search/holdout split, validator/smoke/score ranking, staging/promoted code and versioned proposer instructions.
- Closure path: sampled external task failures/traces → proposer diagnoses and writes candidate behavior changes → prospective evaluation on fresh/held-out tasks → S3 selection chooses a better parent → modified program becomes current harness for later tasks/epochs.
- Boundary reachability: installed `meta-agent loop` directly calls `invoke_proposer`, evaluates proposed files, and makes best candidate the parent for the next iteration. `--evolve-skill` optionally adds versioned proposer instruction evolution but is not needed for base S4.
- Why this is / is not agent-owned: the model decides which novel changes in prompts, tools, stops, routing or code to propose from environmental evidence; Python scoring constrains acceptance but does not generate the future adaptation options.
- External distinction: actual heterogeneous task outcomes, error traces and judge/label feedback reveal operating-environment demand beyond the proposer internal plan.
- Future / prospective distinction: proposals modify the *next* harness capability and are tested on task cohorts/holdout before becoming the parent's future working configuration.
- Adaptation option generated: alternative executable harness source, stopping criteria, tools/agent prompts and optional process-skill guidance.
- Path back into current capability / S3: candidate validation/evaluation and best-parent selection feed the changed harness into the next epoch's installed operational program.
- Evidence: [`README.md`](https://github.com/canvas-org/meta-agent/blob/28e18519eba79e0e97217989390704167c43a5c8/README.md), [`loop/proposer.py`](https://github.com/canvas-org/meta-agent/blob/28e18519eba79e0e97217989390704167c43a5c8/meta_agent/loop/proposer.py) (`invoke_proposer`), [`loop/epoch.py`](https://github.com/canvas-org/meta-agent/blob/28e18519eba79e0e97217989390704167c43a5c8/meta_agent/loop/epoch.py) (`_run_one_epoch`, `_run_one_epoch_multi`), [`loop/skill_evolver.py`](https://github.com/canvas-org/meta-agent/blob/28e18519eba79e0e97217989390704167c43a5c8/meta_agent/loop/skill_evolver.py).
- Basis: explicit and structural.
- Confidence: medium-high for prospective closed code path, not for measured improvement.
- Caveats: adaptation is task-distribution/benchmark-bound and requires model/judge credentials; it does not imply awareness of arbitrary open-world future trends or proven transfer outside the selected benchmark.

## S5 — Policy and identity

- State: —
- Function: no first-party ultimate-policy/identity deliberation/ratification cycle for the optimizer's mission or values.
- Disturbance / variety regulated: acceptance thresholds, cost budgets, allowed edit surfaces and benchmark contracts constrain evolution but are preselected by the experiment operator.
- Decisive decision or feedback right: CLI and benchmark configs fix objective, proposer privileges, allowed edit surfaces and selection criterion; candidate evolution is explicitly prohibited from modifying target interfaces and benchmark truth.
- Decision owner: external experimenter/maintainer through supplied configuration, not agentic ultimate authority or a parent-policy issue return.
- Supporting / enforcement mechanisms: `surface_lock`, staging validation, benchmark adapters, proposer instructions and run args.
- Closure path: option checks enforce a fixed experimental mission; no system identity issue is escalated to legitimate policy authority and returned as a governing decision.
- Why this is / is not agent-owned: an agent editing prompts/harness code is adaptation/operation, not authority to define its organizational purpose/ultimate policy.
- Evidence: [`loop/proposer.py`](https://github.com/canvas-org/meta-agent/blob/28e18519eba79e0e97217989390704167c43a5c8/meta_agent/loop/proposer.py), [`loop/validate.py`](https://github.com/canvas-org/meta-agent/blob/28e18519eba79e0e97217989390704167c43a5c8/meta_agent/loop/validate.py), [`core/benchmark.py`](https://github.com/canvas-org/meta-agent/blob/28e18519eba79e0e97217989390704167c43a5c8/meta_agent/core/benchmark.py).
- Basis: structural.
- Confidence: medium-high.
- Caveats: external organizational governance does not count without a first-party identity-level return-to-operation path.

### Absence scope

- Surfaces inspected: CLI args/benchmark contract, proposer prompt/surface locks, validation/selection, slow skill evolution and project governance artifacts.
- Plausible first-party paths checked: proposer changing own skill, winner selection, allowed edit scope and experiment settings.
- Why no material first-party path remains: changes regulate how a fixed task/benchmark objective is pursued, not who may set or ratify ultimate mission and values; no shipped parent-governed S5 return is established.

## Distributed OSS parent arrangement

Meta-Agent's repository maintainers and independent experiment operators choose target tasks, privileges and releases. Those outside actors are not an installed organization-level S3/S4/S5 parent return mechanism for a particular running optimizer; no `(P)` mode is inferred.

## Self-hosted and non-human modes

The optimizer runs locally with configured model backends and can perform multiple rounds without human semantic proposal selection; missing provider credentials prevent execution but do not invalidate source-reachability of the model-backed path. The operator controls benchmark, budget and edit limits. Optional slow skill evolution is explicitly experimental and not counted as an independently validated improvement claim.

## Recursion

Target task cells, optimizer fast loop and optional skill evolver form nested improvement levels, but the slow loop is process-skill evolution, not independently evidenced complete VSM viability for a new child organization. Two timescales alone are not two fully viable recursive levels.

## Variety and escalation

Task/run history and trace analysis amplify useful external feedback into code-level options, validation/holdout attenuate regressions and best-parent selection returns one candidate to operating capacity. Validation errors and budget caps are normal selection signals, not by themselves algedonic constitutional escalation or independent auditing.

## Evidence gaps

- This is a pinned-source structural assessment. No proposer/benchmark iteration, hosted model call, success replication or independent S3* auditor was executed.
- S4=A credits the first-party experimental outer harness adaptation loop over a supplied task environment, not demonstrated long-horizon open-world sensing or unrestricted strategic self-government.
- S3=C credits the run-level numeric acceptance feedback, not model ownership of a whole enterprise or multi-tenant infrastructure.

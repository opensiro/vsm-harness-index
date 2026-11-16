---
harness_id: openevolve
project_name: OpenEvolve
repository: https://github.com/algorithmicsuperintelligence/openevolve
review_ref: 88efea9ea1c5698bb4a5db037bf3cd78644802d5
reviewed_at: 2026-11-16
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# OpenEvolve

## Review boundary

- System in focus: one configured OpenEvolve run, including the installed two-population coevolution mode where declared.
- Purpose and identity: search for program improvements under a caller-supplied fitness and task.
- Relevant environment: caller's program/evaluator, evaluation host, candidate failures and configured inference providers.
- Standard-distribution boundary: shipped CLI and Python API, controller, workers, optional coevolution driver and evaluation/selection interfaces.
- Credited operating / distribution surfaces: packaged Python entry points; standard parallel/island evolution, function-specific programmable selectors and competitive evaluation.
- Adjacent first-party surfaces excluded from ownership: tests, example benchmark tasks, CI and contributor governance. External evaluators and inference backends supply application semantics.
- First-party operating / deployment modes considered: standalone CLI/SDK evolution, resumable runs, manual-model mode, selector hooks and two-population coevolution.
- Recursion level: one optimization run or coevolution campaign; candidate lines and, in coevolution, the independently evolving populations implement operational searches.
- Reviewed revision: `88efea9ea1c5698bb4a5db037bf3cd78644802d5`.
- Observation date: 2026-11-16.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

A controller builds worker, evaluator and population state from a seed and config. Workers sample context, request model-generated revisions and evaluate the result. A central population database selects and tracks candidates, supports islands and optionally accepts typed caller decisions. Coevolution constructs two engines under a phase protocol and persists their champion histories. [openevolve/controller.py](https://github.com/algorithmicsuperintelligence/openevolve/blob/88efea9ea1c5698bb4a5db037bf3cd78644802d5/openevolve/controller.py#L144-L173), [openevolve/controller.py](https://github.com/algorithmicsuperintelligence/openevolve/blob/88efea9ea1c5698bb4a5db037bf3cd78644802d5/openevolve/controller.py#L380-L476), [openevolve/coevolution.py](https://github.com/algorithmicsuperintelligence/openevolve/blob/88efea9ea1c5698bb4a5db037bf3cd78644802d5/openevolve/coevolution.py#L90-L119).

## Operational model

The service returns an optimized candidate against a declared objective. The model chooses candidate code. Evaluation, retention and dispatch remain separate rights. The caller can supply a competitive evaluator or live island-allocation policy through first-party APIs.

## S1 — Operations

- State: A
- Function: Evolve code candidates toward the supplied target and return an evaluated program.
- Disturbance / variety regulated: Candidate defects, evaluator failures and uneven fitness across alternatives.
- Decisive decision or feedback right: Generate the candidate edit or rewrite with prior candidates, fitness and available evaluation feedback.
- Decision owner: The model actor in the shipped generation ensemble.
- Supporting / enforcement mechanisms: Candidate parsing, evaluator, population database, worker scheduling and stopping rules.
- Closure path: The worker prompts the generation model with a parent and observations, evaluates the candidate, and returns it to the parent engine; retained programs and scores affect the next worker prompt.
- Boundary reachability: The public API builds OpenEvolve with the evaluator and runs the controller, which starts the bundled worker path.
- Why this is / is not agent-owned: Provider-generated code changes determine the candidate. The evaluator and selection rules regulate retention under the caller's objective.
- Evidence: [openevolve/process_parallel.py](https://github.com/algorithmicsuperintelligence/openevolve/blob/88efea9ea1c5698bb4a5db037bf3cd78644802d5/openevolve/process_parallel.py#L263-L321), [openevolve/process_parallel.py](https://github.com/algorithmicsuperintelligence/openevolve/blob/88efea9ea1c5698bb4a5db037bf3cd78644802d5/openevolve/process_parallel.py#L401-L464), [openevolve/process_parallel.py](https://github.com/algorithmicsuperintelligence/openevolve/blob/88efea9ea1c5698bb4a5db037bf3cd78644802d5/openevolve/process_parallel.py#L835-L931), [openevolve/database.py](https://github.com/algorithmicsuperintelligence/openevolve/blob/88efea9ea1c5698bb4a5db037bf3cd78644802d5/openevolve/database.py#L592-L651).
- Basis: Source-wired installed SDK and worker path.
- Confidence: High.
- Caveats: Manual generation is an optional task-level substitution.

## S2 — Coordination

- State: C
- Function: Stabilize reciprocal evaluation between two independently evolving populations during a coevolution run.
- Disturbance / variety regulated: One population's changes would otherwise move the other population's scoring target during its phase, making old and new scores incompatible.
- Decisive decision or feedback right: Define and hand off the stable opponent set and evaluate candidate and retained programs against it for the phase.
- Decision owner: The coevolution driver enforces the opponent handoff. The caller supplies the competitive evaluation relation.
- Supporting / enforcement mechanisms: Frozen champion snapshots, phase order, caller evaluator interface, re-scoring and phase checkpoint.
- Closure path: Each phase captures the opposing champion set, re-scores retained candidates against it, evolves the active population, checkpoints the new champion set and supplies it to the other population's next phase.
- Boundary reachability: The shipped run_coevolution API constructs separate OpenEvolve engines using the caller's evaluator with a frozen opponent set.
- Distinct S1 units: Two separately configured populations with separate persisted retained programs and champion histories, each performing an evolutionary search phase.
- Inter-S1 disturbance: Reciprocal movement of the competitive evaluation baseline during candidate search.
- Attenuating coordination relation: Freeze the peer's champion set within each phase and re-score the active population on handoff.
- Feedback into subsequent S1 behaviour: Updated opponent snapshots and re-scored populations change the next candidate-generation and retention steps.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The phase interface holds the peer-dependent scoring baseline stable and refreshes it at a bounded transition, which attenuates interference between the two search operations.
- Why this is / is not agent-owned: The shipped driver governs snapshot and handoff mechanically. The caller supplies the function-specific evaluator and a concrete competitive relation for both populations.
- Evidence: [openevolve/coevolution.py](https://github.com/algorithmicsuperintelligence/openevolve/blob/88efea9ea1c5698bb4a5db037bf3cd78644802d5/openevolve/coevolution.py#L90-L132), [openevolve/coevolution.py](https://github.com/algorithmicsuperintelligence/openevolve/blob/88efea9ea1c5698bb4a5db037bf3cd78644802d5/openevolve/coevolution.py#L197-L264), [openevolve/coevolution.py](https://github.com/algorithmicsuperintelligence/openevolve/blob/88efea9ea1c5698bb4a5db037bf3cd78644802d5/openevolve/coevolution.py#L270-L307).
- Basis: Function-specific coordination protocol in the public coevolution API.
- Confidence: Medium.
- Caveats: The coevolution mode is optional. Within-island parallelism or periodic migration alone was not credited.

## S3 — Inside-and-now control

- State: C
- Function: Allocate ongoing candidate-generation work across islands during one current search.
- Disturbance / variety regulated: Uneven pending work, fitness and population progress across islands under a shared worker pool and iteration allocation.
- Decisive decision or feedback right: Select which island gets the next bounded iteration, with a current view across all islands.
- Decision owner: The developer-composed island selector; the first-party controller owns the state snapshot and enforcement.
- Supporting / enforcement mechanisms: Typed pending counts and island score/size summaries, validated returned island ID and queued worker submission.
- Closure path: The controller sends the current all-island snapshot to the selector and submits the next iteration to its returned island. As iterations complete, updated pending counts and scores are available at the next selection.
- Boundary reachability: The installed run_evolution callable accepts an island selector and the controller forwards its result into actual worker submission.
- Whole-system current view: Iteration, pending counts and population/fitness summaries for each island in the current run.
- Current-control decision scope: Dispatch the next candidate-generation resource to one island from the shared pool, changing live work across the search.
- Why this is / is not agent-owned: The callback supplies the decisive selection logic. The shipped default seeds and refills configured quotas without a model supervisor.
- Evidence: [openevolve/api.py](https://github.com/algorithmicsuperintelligence/openevolve/blob/88efea9ea1c5698bb4a5db037bf3cd78644802d5/openevolve/api.py#L36-L71), [openevolve/selection.py](https://github.com/algorithmicsuperintelligence/openevolve/blob/88efea9ea1c5698bb4a5db037bf3cd78644802d5/openevolve/selection.py#L1-L27), [openevolve/process_parallel.py](https://github.com/algorithmicsuperintelligence/openevolve/blob/88efea9ea1c5698bb4a5db037bf3cd78644802d5/openevolve/process_parallel.py#L688-L715), [openevolve/process_parallel.py](https://github.com/algorithmicsuperintelligence/openevolve/blob/88efea9ea1c5698bb4a5db037bf3cd78644802d5/openevolve/process_parallel.py#L1121-L1150).
- Basis: First-party discretionary allocation constructor with state and operational return.
- Confidence: High.
- Caveats: Scope is one current search. Startup config and manual candidate submission do not show a distinct parent current-control mode.

## S3* — Complementary audit

- State: —
- Function: Independently verify operational claims and return material discrepancies to a current controller.
- Disturbance / variety regulated: Potential divergence between measured search output and the reported candidate status or score.
- Decisive decision or feedback right: Obtain complementary access, independently adjudicate the operational claim, and return the discrepancy into control.
- Decision owner: No first-party complementary audit witness in the reviewed modes.
- Supporting / enforcement mechanisms: Deterministic or caller evaluators, optional LLM grading, novelty judging, execution traces and checkpoints.
- Closure path: Candidate scoring and novelty admission return into search. Trace records capture the ordinary execution and reward channel.
- Why this is / is not agent-owned: The optional judging model contributes to regular fitness and novelty assessment. It does not independently audit an already reported operational claim.
- Evidence: [openevolve/evaluator.py](https://github.com/algorithmicsuperintelligence/openevolve/blob/88efea9ea1c5698bb4a5db037bf3cd78644802d5/openevolve/evaluator.py#L235-L350), [openevolve/database.py](https://github.com/algorithmicsuperintelligence/openevolve/blob/88efea9ea1c5698bb4a5db037bf3cd78644802d5/openevolve/database.py#L1188-L1297), [openevolve/evolution_trace.py](https://github.com/algorithmicsuperintelligence/openevolve/blob/88efea9ea1c5698bb4a5db037bf3cd78644802d5/openevolve/evolution_trace.py#L1-L49).
- Basis: Evaluator, novelty and trace paths inspected.
- Confidence: Medium.
- Caveats: A caller may provide additional validation outside the assessed boundary.

### Absence scope

- Surfaces inspected: Worker evaluation and its optional LLM feedback, novelty judging, tracing and checkpointing.
- Plausible first-party paths checked: Independent evaluator, audit through the trace, and second-model novelty judgment.
- Why no material first-party path remains: Evaluator and novelty results are ordinary selection inputs; trace/checkpoint surfaces record the same process. None implements an independent claim check with a corrective feedback route.

## S4 — Outside-and-then intelligence

- State: —
- Function: Use outside or future change to alter the harness's own future operating capability.
- Disturbance / variety regulated: Possible future shifts in evaluator requirements, available models or environment.
- Decisive decision or feedback right: Choose and adopt a prospective capability or operating-strategy change in the harness.
- Decision owner: No first-party prospective adoption witness in the reviewed modes.
- Supporting / enforcement mechanisms: Evolutionary optimization, opponent snapshots, configured hooks and checkpoint/resume.
- Closure path: Adaptive search changes candidate programs and population state under supplied objectives.
- Why this is / is not agent-owned: Model-generated adaptations are the evaluated product of the search. The harness's own strategy and evaluator are initialized by the caller; the run returns candidate champions.
- Evidence: [openevolve/config.py](https://github.com/algorithmicsuperintelligence/openevolve/blob/88efea9ea1c5698bb4a5db037bf3cd78644802d5/openevolve/config.py#L459-L500), [openevolve/controller.py](https://github.com/algorithmicsuperintelligence/openevolve/blob/88efea9ea1c5698bb4a5db037bf3cd78644802d5/openevolve/controller.py#L308-L354), [openevolve/controller.py](https://github.com/algorithmicsuperintelligence/openevolve/blob/88efea9ea1c5698bb4a5db037bf3cd78644802d5/openevolve/controller.py#L421-L476), [openevolve/coevolution.py](https://github.com/algorithmicsuperintelligence/openevolve/blob/88efea9ea1c5698bb4a5db037bf3cd78644802d5/openevolve/coevolution.py#L273-L315).
- Basis: Mode and output boundary traced through API/controller and coevolution return.
- Confidence: Medium.
- Caveats: A deployment may use the evolved code elsewhere. That is an adopter decision outside this run.

### Absence scope

- Surfaces inspected: Search outputs, coevolution, configuration, selection hooks, and checkpoints.
- Plausible first-party paths checked: Candidate evolution as self-adaptation, opponent feedback as outside-and-then intelligence, and checkpoint continuation as strategy adoption.
- Why no material first-party path remains: The candidate and opponent changes serve the existing optimization objective. The reviewed paths do not use a prospective assessment to change the harness capabilities or mode governing future runs.

## S5 — Policy and identity

- State: —
- Function: Resolve identity or ultimate-policy questions governing the OpenEvolve installation or run organization.
- Disturbance / variety regulated: Possible conflicts about task mandate, evaluator authority and permissible objective changes.
- Decisive decision or feedback right: Decide and return a change to the governing purpose or ultimate policy.
- Decision owner: No first-party identity/policy closure witness in the reviewed modes.
- Supporting / enforcement mechanisms: Caller-supplied seed, evaluator, model/prompt config, target score and resume identity validation.
- Closure path: The run enforces the externally supplied objective and validates checkpoint continuity.
- Why this is / is not agent-owned: The caller provides objectives and can supply candidate responses in manual mode. The runtime accepts those operational inputs and enforces the configured policy.
- Evidence: [openevolve/api.py](https://github.com/algorithmicsuperintelligence/openevolve/blob/88efea9ea1c5698bb4a5db037bf3cd78644802d5/openevolve/api.py#L36-L71), [openevolve/controller.py](https://github.com/algorithmicsuperintelligence/openevolve/blob/88efea9ea1c5698bb4a5db037bf3cd78644802d5/openevolve/controller.py#L242-L269), [openevolve/controller.py](https://github.com/algorithmicsuperintelligence/openevolve/blob/88efea9ea1c5698bb4a5db037bf3cd78644802d5/openevolve/controller.py#L308-L354), [openevolve/coevolution.py](https://github.com/algorithmicsuperintelligence/openevolve/blob/88efea9ea1c5698bb4a5db037bf3cd78644802d5/openevolve/coevolution.py#L156-L180).
- Basis: Configuration, manual queue and checkpoint identity source paths.
- Confidence: Medium.
- Caveats: A caller can start a different run with different objectives.

### Absence scope

- Surfaces inspected: API configuration, manual-model mode, evaluator ownership and coevolution resume.
- Plausible first-party paths checked: Owner policy decision through startup, manual task queue or checkpoint resume.
- Why no material first-party path remains: Initialization fixes a task envelope. The manual queue substitutes candidate generation and checkpoint identity is a compatibility check. No shipped loop returns a choice about purpose or ultimate policy into ongoing or subsequent operations.

## Distributed OSS parent arrangement

The caller configures the run. Repository maintainers' contribution workflow sits outside the assessed operational recursion.

## Recursion

Island populations persist separate program sets, but single-run islands share one worker/controller envelope. The competitive mode maintains separate engines and opponent histories and regulates their coupling at the campaign level. The evolved code remains an operational product.

## Variety and escalation

Workers return candidate faults and timing or evaluation evidence to the bounded search. The controller uses configured iteration and stopping criteria, checkpoints and a documented operator interruption path.

## Evidence gaps

Findings are source-relative. No live inference, user-supplied evaluator, deployment or benchmark run was executed. Constructor ownership claims concern the shipped decision inputs and returned effects, independent of any particular caller's policy implementation.

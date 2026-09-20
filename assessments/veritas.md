---
harness_id: veritas
project_name: Veritas
repository: https://github.com/matiasrodlo/veritas
review_ref: f366432381834dee8ecb17bcbc2bad3e6232ff0b
reviewed_at: 2026-09-20
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: A
autonomy_s5: —
---

# Veritas

## Review boundary

- System in focus: one Veritas autonomous research run, including supported first-party idea generation when used, staged best-first experiment search, AgentManager stage control, isolated execution, metric/provenance capture, write-up, citation retrieval, and final automated review.
- Purpose and identity: turn a research idea into executed experiments and a paper by autonomously generating/debugging candidate implementations, selecting evidence-backed improvements, progressing research stages, and producing reviewed write-up artifacts.
- Relevant environment: user/workshop research brief, external scientific literature through Semantic Scholar, executable experiment environment, observed metrics/plots/errors, model providers, and generated paper artifacts.
- Standard-distribution boundary: first-party Veritas idea-generation and `launch_scientist_bfts.py` paths plus the tree-search/AgentManager/execution/write-up/review modules they invoke.
- Credited operating / distribution surfaces: `perform_ideation_temp_free.py`, `launch_scientist_bfts.py`, `veritas/treesearch/`, isolated interpreter/execution, metric/provenance handling, write-up/citation, and automated review.
- Adjacent first-party surfaces excluded from ownership: tests/regression fixtures, CI/development utilities, LaTeX templates as presentation infrastructure, and example idea files except as demonstrations of the supported schema. Model APIs and Semantic Scholar are dependencies rather than borrowed VSM owners.
- First-party operating / deployment modes considered: direct full experiment run from an idea file, resume from stage checkpoints, and the documented first-party workshop-brief → literature-informed idea generation path feeding a later full run.
- Recursion level: one Veritas research run as the viable system; individual candidate tree nodes/workers are attempts inside S1 rather than independent viable S1 units at this recursion.
- Reviewed revision: `f366432381834dee8ecb17bcbc2bad3e6232ff0b`.
- Observation date: 2026-09-20.
- Generated Profile version: 0.2.3.
- Generated Methodology version: 0.3.5.
- Current Profile version: 0.2.3.
- Current Methodology version: 0.3.5.

## Repository architecture

Veritas uses an agentic best-first tree search over LLM-generated experiment implementations. Candidate code runs in isolated child processes with resource limits; execution results, errors, metrics, `.npy` data, plots, and metric provenance are persisted. Failed candidates return execution feedback to the agent for correction. The search progresses through initial implementation, baseline tuning, creative research, and ablation stages.

A first-party `AgentManager` owns the staged research search. It has access to stage journals, best nodes, success criteria, improvement history, current issues, and recent progress. Beyond deterministic criteria, it invokes a feedback model to evaluate completion and generate specific next-substage goals from the observed state, altering subsequent experiment focus. After search, the launcher rejects zero-data runs before write-up, aggregates figures, writes the paper, retrieves citations, and performs automated prose/image review. That final review is post-hoc in the reviewed launcher; no first-party path returns its findings to AgentManager or write-up for another corrective cycle.

Separately, the supported idea-generation script requires at least one Semantic Scholar search before finalizing an idea and asks the model to incorporate retrieved literature into repeated proposal reflection. The finalized idea contains hypothesis, related work, experiments, and risks and can then be passed directly into the experiment run.

Primary evidence: [README](https://github.com/matiasrodlo/veritas/blob/f366432381834dee8ecb17bcbc2bad3e6232ff0b/README.md), [AgentManager](https://github.com/matiasrodlo/veritas/blob/f366432381834dee8ecb17bcbc2bad3e6232ff0b/veritas/treesearch/stages/manager.py), [launcher](https://github.com/matiasrodlo/veritas/blob/f366432381834dee8ecb17bcbc2bad3e6232ff0b/launch_scientist_bfts.py), [idea generation](https://github.com/matiasrodlo/veritas/blob/f366432381834dee8ecb17bcbc2bad3e6232ff0b/veritas/perform_ideation_temp_free.py).

## Operational model

The S1 operation is experiment design/implementation/execution and scientific result production. Candidate failures and observed metrics feed the next experiment choices. AgentManager provides a distinct current-control function at run scope because it assesses whole-stage progress and changes what the search works on next rather than only enforcing fixed budgets. The optional first-party ideation mode supplies S4 by sensing external literature and returning a selected future research program into S1. The final automated paper review lacks corrective closure and is therefore not promoted to S3*.

## S1 — Operations

- State: A
- Function: generate, debug, execute, compare, and refine experiment implementations to gather scientific evidence for the loaded research idea.
- Disturbance / variety regulated: code/runtime failures, inadequate implementations, hyperparameter uncertainty, poor metrics, scaling choices, and uncertainty about which experimental change best tests the hypothesis.
- Decisive decision or feedback right: choose candidate implementation changes and subsequent experiment actions in response to execution errors, journal history, metrics, and stage goals.
- Decision owner: the model-driven tree-search research agent (`ParallelAgent`/candidate-generation path).
- Supporting / enforcement mechanisms: isolated interpreter, execution timeout/resource controls, journals/tree nodes, named metrics and provenance, multi-seed evaluation, artifacts/plots, search configuration, and checkpoints.
- Closure path: generated code is executed; errors/metrics/artifacts return into the search journal and prompts; subsequent nodes implement revisions or alternative experiments until stage criteria/limits are reached.
- Boundary reachability: the tree-search agent and interpreter are the core path invoked by `launch_scientist_bfts.py`; no external agent harness supplies the experiment loop.
- Why this is / is not agent-owned: deterministic execution and metric parsing constrain/measure candidates, but the model-driven agent chooses substantive implementation and experiment changes.
- Evidence: [README search description](https://github.com/matiasrodlo/veritas/blob/f366432381834dee8ecb17bcbc2bad3e6232ff0b/README.md#how-it-works), [tree-search runner](https://github.com/matiasrodlo/veritas/blob/f366432381834dee8ecb17bcbc2bad3e6232ff0b/veritas/treesearch/scripts/perform_experiments_bfts_with_agentmanager.py), [AgentManager agent creation](https://github.com/matiasrodlo/veritas/blob/f366432381834dee8ecb17bcbc2bad3e6232ff0b/veritas/treesearch/stages/manager.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: parallel candidates/tree branches are alternative attempts inside the operational research process; their plurality is not itself evidence of S2.

## S2 — Coordination

- State: —
- Function: no material S2-specific inter-S1 coordination loop is established at the declared recursion.
- Disturbance / variety regulated: not established.
- Decisive decision or feedback right: not established.
- Decision owner: not applicable.
- Supporting / enforcement mechanisms: worker isolation, process/resource limits, stage sequencing, shared journals, and candidate ranking prevent contamination or structure search but do not evidence a concrete interference/oscillation among distinct cooperating S1 units.
- Closure path: not established.
- Why this is / is not agent-owned: concurrent or branching experiment attempts are not automatically separate operational units requiring S2; they are candidate searches for one S1 research outcome.
- Evidence: [README execution/isolation description](https://github.com/matiasrodlo/veritas/blob/f366432381834dee8ecb17bcbc2bad3e6232ff0b/README.md#how-it-works), [experiment runner](https://github.com/matiasrodlo/veritas/blob/f366432381834dee8ecb17bcbc2bad3e6232ff0b/veritas/treesearch/scripts/perform_experiments_bfts_with_agentmanager.py).
- Basis: structural negative finding.
- Confidence: high.
- Caveats: a future multi-researcher mode would require a distinct S1 mapping and explicit interference/attenuation witness.

### Absence scope

- Surfaces inspected: AgentManager, journals/tree search, parallel worker execution, stage progression, interpreter/resource controls, checkpoints, and experiment-result aggregation.
- Plausible first-party paths checked: parallel candidates, worker isolation, shared metrics/journals, stage handoffs, search ranking, and resource limits.
- Why no material first-party path remains: these paths structure or isolate attempts inside one research operation; no concrete inter-S1 conflict/oscillation plus a first-party attenuation relation changing subsequent behavior of distinct operational units is established.

## S3 — Inside-and-now control

- State: A
- Function: maintain current evidence about the whole active research search/stage and decide completion, next-substage focus, and progression of the experiment program.
- Disturbance / variety regulated: stagnating search, unmet stage success criteria, unresolved implementation issues, insufficient improvement, under-scaled experiments, and uncertainty about the most useful next search focus.
- Decisive decision or feedback right: decide whether the current stage/substage is complete and generate specific goals/focus for the next substage from current progress/issues/metrics.
- Decision owner: AgentManager's model-driven feedback/evaluation path for discretionary completion/focus judgments, operating within deterministic minimum/max/adaptive-stopping constraints.
- Supporting / enforcement mechanisms: full stage journal, best-node selection, success-criteria checks, improvement counters, deterministic stopping rules, stage history, checkpoints, and stage lifecycle code.
- Closure path: current journal metrics/issues/recent changes are summarized into the feedback model; the resulting completion decision or generated substage goals alter stage lifecycle and the prompt/goals used by the next research agent.
- Boundary reachability: AgentManager is the standard controller instantiated by the main tree-search runner, and its feedback model/path is configured as part of normal experiment execution.
- Why this is / is not agent-owned: fixed timeouts/max-iterations and metric checks are enforcement. S3 credit comes from the additional model-driven current-control judgment that interprets current whole-stage evidence and creates the next research focus.
- Whole-system current view: active stage journal, all attempts in that stage, good/buggy nodes, best metric/node, success-criteria progress, current issues/recent changes, stage history, and prior-stage best implementation when relevant.
- Current-control decision scope: stage completion, continuation versus progression, and specific next-substage research goals/focus that determine subsequent resource/effort commitment within the run.
- Evidence: [AgentManager completion logic](https://github.com/matiasrodlo/veritas/blob/f366432381834dee8ecb17bcbc2bad3e6232ff0b/veritas/treesearch/stages/manager.py), [next-substage goal generation](https://github.com/matiasrodlo/veritas/blob/f366432381834dee8ecb17bcbc2bad3e6232ff0b/veritas/treesearch/stages/manager.py), [standard runner](https://github.com/matiasrodlo/veritas/blob/f366432381834dee8ecb17bcbc2bad3e6232ff0b/veritas/treesearch/scripts/perform_experiments_bfts_with_agentmanager.py).
- Basis: structural.
- Confidence: high.
- Caveats: not every AgentManager decision is autonomous: many limits/checks are deterministic. The positive state depends specifically on the model-driven completion and next-focus decisions wired into current operation.

## S3* — Complementary audit

- State: —
- Function: no material operationally closed complementary-audit loop is established in the reviewed full-run path.
- Disturbance / variety regulated: not established at S3* scope.
- Decisive decision or feedback right: no independent audit right with corrective return is established.
- Decision owner: not applicable.
- Supporting / enforcement mechanisms: metric provenance, multi-seed checks, plot/VLM checks, zero-data abort, and final automated paper review provide validation/review surfaces.
- Closure path: the final review is written after the experiment search and paper generation, but the reviewed launcher does not feed its findings back into AgentManager, write-up, or experiments for corrective operation.
- Why this is / is not agent-owned: `perform_review` is a separate review action by name, but S3* requires complementary audit plus findings-to-control closure. Post-hoc persisted review without return is insufficient.
- Evidence: [launcher review path](https://github.com/matiasrodlo/veritas/blob/f366432381834dee8ecb17bcbc2bad3e6232ff0b/launch_scientist_bfts.py), [README output including `review_text.txt`](https://github.com/matiasrodlo/veritas/blob/f366432381834dee8ecb17bcbc2bad3e6232ff0b/README.md#output).
- Basis: structural negative finding.
- Confidence: high.
- Caveats: internal VLM/metric validation is part of ordinary search acceptance/current control, while the separate final review lacks corrective return.

### Absence scope

- Surfaces inspected: metric/provenance capture, stage criteria, VLM feedback, multi-seed evaluation, zero-data guard, write-up retries, prose review, image/caption review, and launcher post-review flow.
- Plausible first-party paths checked: metric verification, provenance records, plot validation, stage completion evaluation, final prose review, and final visual review.
- Why no material first-party path remains: ordinary validation paths participate directly in production/control, while the distinct post-hoc paper review does not return findings into changed subsequent operation; the complete complementary audit → finding → control closure is absent.

## S4 — Outside-and-then intelligence

- State: A
- Function: in the supported idea-generation mode, sense external scientific literature, reflect on novelty/feasibility, and produce a future experiment program that the standard research run can execute.
- Disturbance / variety regulated: risk that a proposed research direction duplicates existing work, misses relevant prior findings, or lacks a feasible/meaningful experimental plan.
- Decisive decision or feedback right: choose/refine/finalize the research proposal after incorporating Semantic Scholar retrieval into repeated idea reflection.
- Decision owner: the model-driven idea-generation agent.
- Supporting / enforcement mechanisms: first-party Semantic Scholar tool, multi-round reflection history, prior-idea archive, structured `FinalizeIdea` schema, and instruction requiring at least one literature search before finalization.
- Closure path: external literature results enter the reflection loop; the finalized idea includes related work, hypothesis, experiments, and risk factors; the resulting JSON is directly consumable by `launch_scientist_bfts.py`, where it determines subsequent staged experimental capability/work.
- Boundary reachability: README documents `perform_ideation_temp_free.py` as the first-party way to create an ideas file from a short workshop brief; its output is the same schema consumed by the standard launcher.
- Why this is / is not agent-owned: the literature tool retrieves external distinctions, but the model-driven ideation loop owns proposal selection/refinement; the experiment launcher then operationalizes the returned option.
- External distinction: retrieved Semantic Scholar prior work and related-work information outside the current Veritas run.
- Future / prospective distinction: novelty, feasibility, and which hypothesis/experimental direction should be pursued in later stages.
- Adaptation option generated: finalized research idea containing hypothesis, related work, experiment plan, and risks/limitations.
- Path back into current capability / S3: the idea JSON becomes the launcher's task description; AgentManager derives stage work from its experiment plan and executes the resulting research program.
- Evidence: [idea-generation tool and required literature search](https://github.com/matiasrodlo/veritas/blob/f366432381834dee8ecb17bcbc2bad3e6232ff0b/veritas/perform_ideation_temp_free.py), [README documented idea generation](https://github.com/matiasrodlo/veritas/blob/f366432381834dee8ecb17bcbc2bad3e6232ff0b/README.md#idea-files), [launcher idea loading](https://github.com/matiasrodlo/veritas/blob/f366432381834dee8ecb17bcbc2bad3e6232ff0b/launch_scientist_bfts.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the internal `creative_research` stage and reuse of previous experiment results are not the basis for S4. Credit depends on the distinct first-party external-literature → future idea → launched experiment closure.

## S5 — Policy and identity

- State: —
- Function: no material identity/ultimate-policy authority loop is established at the declared research-run recursion.
- Disturbance / variety regulated: not established at S5 scope.
- Decisive decision or feedback right: not established.
- Decision owner: not applicable.
- Supporting / enforcement mechanisms: user/workshop idea, structured idea schema, stage goals, configuration, model choices, resource limits, and review/write-up settings constrain operation.
- Closure path: no identity/ultimate-policy issue is shown reaching a legitimate authority and returning as a binding decision to subsequent operation.
- Why this is / is not agent-owned: idea generation chooses the scientific direction to pursue, which is credited as S4; it does not evidence authority to redefine the system's ultimate identity/governance policy at runtime.
- Evidence: [idea schema and launcher](https://github.com/matiasrodlo/veritas/blob/f366432381834dee8ecb17bcbc2bad3e6232ff0b/README.md#idea-files), [AgentManager stage contract](https://github.com/matiasrodlo/veritas/blob/f366432381834dee8ecb17bcbc2bad3e6232ff0b/veritas/treesearch/stages/manager.py).
- Basis: structural negative finding.
- Confidence: high.
- Caveats: human selection of the input idea/configuration is not automatically parent-governed S5.

### Absence scope

- Surfaces inspected: idea generation, launch/configuration, stage definitions, AgentManager control, checkpoints/resume, write-up/review settings, and user-supplied idea schema.
- Plausible first-party paths checked: research-idea selection, model/provider configuration, stage goals, risk/limitation fields, review verdict, and resume controls.
- Why no material first-party path remains: these paths select or regulate research work but do not establish ultimate identity/policy authority and a returned binding governance decision at the assessed recursion.

## Recursion

The viable system is one full Veritas research run. Candidate tree nodes and parallel workers are experimental alternatives inside the operational function rather than separate viable systems by default. The optional idea-generation mode is credited as an S4 mode because it is first-party, documented, produces the launcher's native input schema, and closes into later experiment operation.

## Variety and escalation

Veritas attenuates variety through isolated execution, resource/time limits, journaled errors/results, metric provenance, adaptive stopping, model-driven stage completion/focus decisions, multi-seed evaluation, checkpoints/resume, and a hard abort when no real experiment data exists. Execution failure feeds S1 correction; stagnation/current criteria feed S3 control. Final review findings are preserved but, at this revision, do not create a corrective S3* loop.

## Evidence gaps

- Reassess S3* if automated review findings become an input to another write-up/experiment/control cycle with a distinct complementary evidence path and identifiable actor on the findings.
- Reassess S2 if Veritas introduces multiple persistent cooperating operational units with an explicit conflict/oscillation witness and coordination feedback, rather than parallel candidate search.
- Reassess S5 if a supported mode introduces runtime authority over the research organization's ultimate identity/policy rather than only the scientific idea and experiment program.

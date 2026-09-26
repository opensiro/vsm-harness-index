---
harness_id: mlr-agent
project_name: MLR-Agent
repository: https://github.com/chchenhui/mlrbench
review_ref: f728d571a992d71c8b526eeb4d9ab6bb5c8cc824
reviewed_at: 2026-09-26
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-26
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# MLR-Agent

## Review boundary

- System in focus: one first-party end-to-end MLR-Agent machine-learning research run at pinned revision `f728d571a992d71c8b526eeb4d9ab6bb5c8cc824`, from a supplied `task.md` through idea generation, literature review, proposal generation, autonomous experiment implementation/execution and paper writing.
- Purpose and identity: complete an open-ended ML research task and produce a research paper grounded in generated ideas, external literature and real experimental results.
- Relevant environment: user-supplied research task; model/search APIs; coding-agent CLIs; open datasets/models and compute used by experiments; local filesystem; scientific literature; benchmark/evaluation infrastructure adjacent to the agent.
- Standard-distribution boundary: `run_mlr_agent.py` and the `mlrbench/agent/*` pipeline functions it directly invokes. External provider runtimes and coding-agent executables are environmental resources. `mlrbench/evals`, MLR-Judge, benchmark datasets/scoring, human evaluation and stored benchmark result/review corpora are adjacent evaluation/development surfaces and are not credited to the operating MLR-Agent unless reached by the end-to-end runtime.
- Credited operating / distribution surfaces: `README.md`; `run_mlr_agent.py`; `mlrbench/agent/idea_generator.py`; `mlrbench/agent/lit_review.py`; `mlrbench/agent/proposal_generator.py`; `mlrbench/agent/experiment_runner.py`; `mlrbench/agent/paper_writer.py`; first-party LLM/LMM utility wrappers reached by those paths.
- Adjacent first-party surfaces excluded from ownership: `mlrbench/evals`, MLR-Judge review scripts, benchmark task corpus/scoring, `agent_reviews`, `human_eval`, stored results from other agents, paper/project assets and repository development/governance.
- First-party operating / deployment modes considered: documented end-to-end `run_mlr_agent.py` execution across supported main models, literature engine and coding-agent choices; stepwise scripts were inspected as implementation evidence but do not replace the end-to-end system boundary.
- Recursion level: one ML-research task episode is the system-in-focus. Idea, literature, proposal, experiment and paper stages are functional stages of that single research operation, not separate S1 units merely because they use distinct scripts/models.
- Reviewed revision: `f728d571a992d71c8b526eeb4d9ab6bb5c8cc824`.
- Observation date: 2026-09-26.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

`run_mlr_agent.py` is the documented end-to-end operating entrypoint. For each supplied task folder it deterministically invokes five first-party stages: idea generation, literature review, proposal generation, experiment execution and paper writing. Each stage consumes artifacts from earlier stages and materializes the next research artifact in the same task workspace.

The substantive decisions inside those stages are model-owned. Idea generation chooses an innovative research direction from the task. Literature review uses a search-capable model to identify recent related papers and key challenges. Proposal generation consumes task, idea and literature to formulate methodology and experimental design. `experiment_runner.py` launches a configured coding agent with an explicit mandate to design the experimental plan, implement and debug executable code, run real baselines/experiments, inspect results, and retry until successful result artifacts exist. Paper writing then consumes the task, idea, literature, proposal, experiment results and figures to synthesize the final research paper.

The end-to-end pipeline does not invoke MLR-Judge. The evaluation scripts under `mlrbench/evals` are separate benchmark surfaces that can review completed artifacts after the research operation. Their co-location in the repository therefore does not establish S3*. Likewise, generation retries, coding-agent debugging and existence checks are ordinary operational quality/recovery paths, not complementary audit.

Literature search is externally oriented, but at the declared harness recursion it directly contributes evidence and constraints to the current research product. The runtime does not use literature or experiment outcomes to redesign MLR-Agent's durable capabilities, model/tool repertoire or strategy for later independent runs. There is also no qualifying S3 whole-system current-control function with which a prospective S4 model enters the required current/future homeostatic conversation. The literature/proposal stages therefore remain S1 research activity rather than S4 organizational adaptation.

Primary evidence:

- [`README.md`](https://github.com/chchenhui/mlrbench/blob/f728d571a992d71c8b526eeb4d9ab6bb5c8cc824/README.md) — separates MLR-Agent from MLR-Judge and documents the end-to-end research stages/entrypoint.
- [`run_mlr_agent.py`](https://github.com/chchenhui/mlrbench/blob/f728d571a992d71c8b526eeb4d9ab6bb5c8cc824/run_mlr_agent.py) — executable end-to-end closure from task to idea/literature/proposal/experiment/paper; no MLR-Judge invocation.
- [`mlrbench/agent/idea_generator.py`](https://github.com/chchenhui/mlrbench/blob/f728d571a992d71c8b526eeb4d9ab6bb5c8cc824/mlrbench/agent/idea_generator.py) — model-owned research-direction generation.
- [`mlrbench/agent/lit_review.py`](https://github.com/chchenhui/mlrbench/blob/f728d571a992d71c8b526eeb4d9ab6bb5c8cc824/mlrbench/agent/lit_review.py) — external literature acquisition tied to the current idea/task.
- [`mlrbench/agent/proposal_generator.py`](https://github.com/chchenhui/mlrbench/blob/f728d571a992d71c8b526eeb4d9ab6bb5c8cc824/mlrbench/agent/proposal_generator.py) — current-project methodology/experiment proposal from task, idea and literature.
- [`mlrbench/agent/experiment_runner.py`](https://github.com/chchenhui/mlrbench/blob/f728d571a992d71c8b526eeb4d9ab6bb5c8cc824/mlrbench/agent/experiment_runner.py) — autonomous coding-agent experiment design, implementation, debugging, execution and result analysis.
- [`mlrbench/agent/paper_writer.py`](https://github.com/chchenhui/mlrbench/blob/f728d571a992d71c8b526eeb4d9ab6bb5c8cc824/mlrbench/agent/paper_writer.py) — synthesis of upstream research artifacts and real experiment results into the final paper.

## Operational model

The operational outcome is one completed ML research task. The task description seeds an idea; the idea directs a literature search; task, idea and literature shape a proposal; the proposal plus preceding artifacts instruct a coding agent to implement and run experiments; experiment results then condition the final paper. The stages therefore form one evidence-producing operational chain whose later decisions depend on artifacts created by earlier decisions.

The coding-agent experiment stage is especially substantive: it is instructed to design experiments, create and debug code, run baselines and real experiments, save structured results/figures, analyze findings and retry until the expected result artifact is produced. Deterministic Python launches providers and checks artifacts, but the scientific/implementation choices are delegated to the model/coding agent. This closes autonomous S1 at the harness boundary.

## S1 — Operations

- State: A
- Function: carry an open-ended ML research task from problem statement through research idea, literature grounding, methodology, executable experiment and evidence-backed paper.
- Disturbance / variety regulated: ambiguity in research direction, incomplete knowledge of related work, methodological choice, experiment implementation/debugging failures, dataset/model/compute constraints, empirical outcomes and synthesis of heterogeneous evidence into a paper.
- Decisive decision or feedback right: choose the research idea; select/summarize relevant literature; design the proposal; design, implement, debug and run the experiment; interpret results; and synthesize the final paper from the resulting evidence.
- Decision owner: the configured model/search/coding-agent calls invoked by the first-party MLR-Agent pipeline, with first-party Python sequencing and persisting their artifacts.
- Supporting / enforcement mechanisms: task folders, artifact files, retry loops, provider wrappers, subprocess execution, result-file checks, logging and deterministic stage order.
- Closure path: `task.md` -> model-generated `idea.md` -> literature engine creates `related_work.md` -> model generates `proposal.md` -> coding agent implements/runs/debugs experiments and produces `results/results.md` plus figures -> paper writer consumes all artifacts and creates the paper.
- Boundary reachability: the documented `python run_mlr_agent.py ...` entrypoint directly invokes every credited stage. No benchmark judge/evaluation runner is required to complete the research task.
- Why this is / is not agent-owned: deterministic code selects the fixed stage order and handles persistence/retries, but the substantive scientific, search, experiment-design, code-debugging, interpretation and writing choices are produced by models/coding agents from live task artifacts.
- Evidence: [`run_mlr_agent.py`](https://github.com/chchenhui/mlrbench/blob/f728d571a992d71c8b526eeb4d9ab6bb5c8cc824/run_mlr_agent.py); [`mlrbench/agent/idea_generator.py`](https://github.com/chchenhui/mlrbench/blob/f728d571a992d71c8b526eeb4d9ab6bb5c8cc824/mlrbench/agent/idea_generator.py); [`mlrbench/agent/lit_review.py`](https://github.com/chchenhui/mlrbench/blob/f728d571a992d71c8b526eeb4d9ab6bb5c8cc824/mlrbench/agent/lit_review.py); [`mlrbench/agent/proposal_generator.py`](https://github.com/chchenhui/mlrbench/blob/f728d571a992d71c8b526eeb4d9ab6bb5c8cc824/mlrbench/agent/proposal_generator.py); [`mlrbench/agent/experiment_runner.py`](https://github.com/chchenhui/mlrbench/blob/f728d571a992d71c8b526eeb4d9ab6bb5c8cc824/mlrbench/agent/experiment_runner.py); [`mlrbench/agent/paper_writer.py`](https://github.com/chchenhui/mlrbench/blob/f728d571a992d71c8b526eeb4d9ab6bb5c8cc824/mlrbench/agent/paper_writer.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the operator supplies the top-level task, models, literature engine and coding-agent configuration. S1 autonomy concerns the substantive within-task research path once those boundary conditions are supplied.

## S2 — Coordination

- State: —
- Function: no qualifying inter-S1 disturbance-attenuation function is established at the declared boundary.
- Disturbance / variety regulated: none qualifying; idea, literature, proposal, experiment and paper stages are sequential specializations of one research operation rather than distinct S1 units whose interaction creates oscillation/conflict.
- Decisive decision or feedback right: none established for S2.
- Decision owner: none established.
- Supporting / enforcement mechanisms: deterministic stage sequencing, shared task-folder artifacts and provider dispatch move work between stages but do not establish S2.
- Closure path: no material S2-specific closure path established.
- Why this is / is not agent-owned: there is no evidenced S2 organizational function to classify for ownership.
- Evidence: [`run_mlr_agent.py`](https://github.com/chchenhui/mlrbench/blob/f728d571a992d71c8b526eeb4d9ab6bb5c8cc824/run_mlr_agent.py).
- Basis: structural absence.
- Confidence: high.
- Caveats: multiple scripts/models and stage handoffs do not count as S2 without distinct S1 units plus a concrete inter-unit disturbance.

### Absence scope

- Surfaces inspected: end-to-end stage sequence; idea/literature/proposal/experiment/paper implementations; task-folder artifact handoffs; retries and provider/coding-agent dispatch.
- Plausible first-party paths checked: sequential stage routing, shared filesystem state, experiment subprocess execution, multi-task outer loop and provider selection.
- Why no material first-party path remains: no distinct operational units with an evidenced mutual interference/oscillation/resource conflict and no coordination relation specifically intended to attenuate such a disturbance.

## S3 — Inside-and-now control

- State: —
- Function: no separate whole-system current regulator is established above the single ML-research operation.
- Disturbance / variety regulated: current project progress and stage completion are regulated inside the same S1 workflow.
- Decisive decision or feedback right: no current-control right distinct from the research operation's own scientific and implementation decisions is established.
- Decision owner: none established for qualifying S3.
- Supporting / enforcement mechanisms: fixed stage order, file-existence checks, retry budgets and task-folder iteration provide workflow enforcement rather than superior whole-system regulation.
- Closure path: no material S3-specific whole-system current-control path established.
- Why this is / is not agent-owned: `run_mlr_agent.py` orchestrates one research operation by fixed sequence; it does not hold a whole-system current view and bargain/regulate resources, commitments or priorities across independent S1 units.
- Evidence: [`run_mlr_agent.py`](https://github.com/chchenhui/mlrbench/blob/f728d571a992d71c8b526eeb4d9ab6bb5c8cc824/run_mlr_agent.py); pipeline stage implementations.
- Basis: structural absence.
- Confidence: high.
- Caveats: deterministic orchestration and a complete project-level sequence are not sufficient for S3.

### Absence scope

- Surfaces inspected: end-to-end runner, all five operating stages, task-list loop, retries, logging and model/coding-agent selection.
- Plausible first-party paths checked: pipeline orchestration, sequential commitment, task batching, provider choice and experiment-resource instructions.
- Why no material first-party path remains: no separate actor has a whole-system current view plus authority over resources/commitments/priorities among multiple operational units at this recursion.

## S3* — Complementary audit

- State: —
- Function: no qualifying complementary independent audit function is reachable inside the end-to-end MLR-Agent runtime.
- Disturbance / variety regulated: ordinary generation failures and experiment/code errors are checked/retried within S1; benchmark research-quality assessment exists separately in MLR-Judge but is not part of the operating closure path.
- Decisive decision or feedback right: no in-boundary auditor independently challenges an operational claim through a complementary evidence path and feeds findings back to alter the same MLR-Agent run.
- Decision owner: none established for qualifying S3*.
- Supporting / enforcement mechanisms: retry loops, result-file existence checks, coding-agent self-debugging, MLR-Judge scripts and stored review artifacts were inspected; the latter are adjacent evaluation surfaces.
- Closure path: no material in-boundary S3* closure path established.
- Why this is / is not agent-owned: the separately runnable MLR-Judge may evaluate completed work, but `run_mlr_agent.py` neither invokes it nor consumes its findings; ordinary experiment debugging is controlled by the producing operation itself.
- Evidence: [`README.md`](https://github.com/chchenhui/mlrbench/blob/f728d571a992d71c8b526eeb4d9ab6bb5c8cc824/README.md); [`run_mlr_agent.py`](https://github.com/chchenhui/mlrbench/blob/f728d571a992d71c8b526eeb4d9ab6bb5c8cc824/run_mlr_agent.py); [`mlrbench/agent/experiment_runner.py`](https://github.com/chchenhui/mlrbench/blob/f728d571a992d71c8b526eeb4d9ab6bb5c8cc824/mlrbench/agent/experiment_runner.py); adjacent `mlrbench/evals/`.
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: repository co-location of MLR-Agent and MLR-Judge is deliberately not treated as system membership.

### Absence scope

- Surfaces inspected: end-to-end runner, stage retries, coding-agent debugging/result checks, README MLR-Judge instructions, `mlrbench/evals`, `agent_reviews` and human-evaluation surfaces.
- Plausible first-party paths checked: stepwise/overall MLR-Judge review; experiment self-debugging; output-file checks; post-generation benchmark review.
- Why no material first-party path remains: MLR-Judge is separately invoked evaluation and its findings are not returned into `run_mlr_agent.py`; all in-runtime checking is ordinary production/recovery without a complementary sufficiently independent access path.

## S4 — Outside-and-then intelligence

- State: —
- Function: no separate external-and-prospective organizational adaptation function is established at the MLR-Agent harness recursion.
- Disturbance / variety regulated: changing scientific knowledge, related work and future experimental possibilities are investigated for the current research product, not to redesign the durable capability/posture of MLR-Agent itself.
- Decisive decision or feedback right: none established for a persistent adaptation option affecting the harness's future operational capability.
- Decision owner: none established for qualifying S4.
- Supporting / enforcement mechanisms: literature search, idea generation, proposal formulation and experiment-result analysis provide research intelligence for S1; they do not persist an organizational adaptation of the harness.
- Closure path: no material S4-specific external/future distinction -> adaptation option -> present-capability change path established.
- Why this is / is not agent-owned: the runtime is externally informed, but the external information is consumed directly as subject-matter evidence inside the current research task. It does not enter a separate S4/S3 homeostatic conversation that changes MLR-Agent's future capabilities.
- Evidence: [`mlrbench/agent/lit_review.py`](https://github.com/chchenhui/mlrbench/blob/f728d571a992d71c8b526eeb4d9ab6bb5c8cc824/mlrbench/agent/lit_review.py); [`mlrbench/agent/proposal_generator.py`](https://github.com/chchenhui/mlrbench/blob/f728d571a992d71c8b526eeb4d9ab6bb5c8cc824/mlrbench/agent/proposal_generator.py); [`mlrbench/agent/experiment_runner.py`](https://github.com/chchenhui/mlrbench/blob/f728d571a992d71c8b526eeb4d9ab6bb5c8cc824/mlrbench/agent/experiment_runner.py); [`run_mlr_agent.py`](https://github.com/chchenhui/mlrbench/blob/f728d571a992d71c8b526eeb4d9ab6bb5c8cc824/run_mlr_agent.py).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: future-oriented scientific research is the product of this S1. That does not make the harness's literature/proposal stages S4 at the harness recursion; a different system-in-focus could classify functions differently.

### Absence scope

- Surfaces inspected: idea generation, literature search, proposal generation, experiment design/results analysis, paper future-work synthesis, task/result persistence and evaluator surfaces.
- Plausible first-party paths checked: external scientific-literature sensing; experiment-derived learning; generated future-work suggestions; repeated task-folder execution; benchmark/evaluation feedback.
- Why no material first-party path remains: no first-party runtime path converts those prospective distinctions into a durable change of MLR-Agent's installed models/tools/strategy/capabilities for later independent operations, and no qualifying S3–S4 conversation is present.

## S5 — Policy and identity

- State: —
- Function: no runtime authority over organizational identity, ultimate purpose or binding top-level policy is established.
- Disturbance / variety regulated: none qualifying; task identity, provider/coding-agent choices and stage instructions are supplied by user/configuration/source prompts.
- Decisive decision or feedback right: no runtime actor can redefine MLR-Agent's ultimate mission or authoritatively settle an identity/ultimate-policy conflict.
- Decision owner: user/operator and repository configuration outside the autonomous runtime.
- Supporting / enforcement mechanisms: `task.md`, CLI model/literature/coding-agent arguments, static prompts and fixed pipeline stage ordering constrain operation but are not S5 ownership.
- Closure path: no material S5-specific closure path established.
- Why this is / is not agent-owned: MLR-Agent autonomously decides how to conduct the supplied research task within configured constraints, not what its organizational identity or ultimate governing policy should be.
- Evidence: [`run_mlr_agent.py`](https://github.com/chchenhui/mlrbench/blob/f728d571a992d71c8b526eeb4d9ab6bb5c8cc824/run_mlr_agent.py); [`README.md`](https://github.com/chchenhui/mlrbench/blob/f728d571a992d71c8b526eeb4d9ab6bb5c8cc824/README.md); stage prompts in `mlrbench/agent/`.
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: detailed scientific/experiment instructions constrain behavior strongly without transferring ultimate-policy authority to the agent.

### Absence scope

- Surfaces inspected: CLI/task inputs, all stage prompts, retry/error policy, model/provider selection, benchmark judge/evaluation and output handling.
- Plausible first-party paths checked: research idea choice, proposal methodology choice, experiment autonomy, result interpretation and paper conclusion/future work.
- Why no material first-party path remains: all identity-level purpose and constitutional bounds originate outside the running research agent; no runtime path can authoritatively redefine them.

## Recursion, variety and escalation

MLR-Agent supplies substantial operational variety for one ML-research S1 by combining research-direction choice, external literature, autonomous coding/experimentation and evidence-backed writing. The Index does not promote its sequential research stages to S2/S3 by architecture labels, does not import MLR-Judge from the adjacent benchmark boundary as S3*, and does not classify subject-matter research as S4 merely because the operation studies external/future scientific possibilities.

## Standalone conclusion

`A — — — — —`

MLR-Agent autonomously closes the substantive end-to-end ML research operation. No material first-party S2, superior S3, complementary in-boundary S3*, prospective organizational S4 or runtime S5 closure is established at the pinned boundary.
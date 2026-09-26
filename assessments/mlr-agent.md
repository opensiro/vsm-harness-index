---
harness_id: mlr-agent
project_name: MLR-Agent
repository: https://github.com/chchenhui/mlrbench
review_ref: f728d571a992d71c8b526eeb4d9ab6bb5c8cc824
reviewed_at: 2026-09-27
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-27
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: A
autonomy_s5: —
---

# MLR-Agent

## Review boundary

- System in focus: one first-party MLR-Agent end-to-end machine-learning research run at pinned revision `f728d571a992d71c8b526eeb4d9ab6bb5c8cc824`, including the shipped idea-generation, literature-review, proposal, experiment-launch and paper-writing stages wired by `run_mlr_agent.py`.
- Purpose and identity: accept a user-supplied open-ended ML research task and autonomously turn it into a research idea, literature-grounded proposal, executed experiment/results and final research paper.
- Relevant environment: user task files; external scientific literature/search results; configured LLM/LMM providers; Claude Code, Codex or Gemini CLI used as coding-agent dependencies; datasets/model hubs/APIs; local filesystem/process/GPU state; experiment outputs.
- Standard-distribution boundary: `run_mlr_agent.py`, `mlrbench/agent/`, first-party LLM/LMM adapters and utilities required by the documented end-to-end MLR-Agent run. The benchmark task corpus, MLR-Judge/evaluation programs, stored agent results/reviews, human evaluation, external coding-agent internals and external model/search/data services remain adjacent evidence/environment rather than imported first-party organizational owners.
- Credited operating / distribution surfaces: `README.md`; `run_mlr_agent.py`; `mlrbench/agent/idea_generator.py`; `mlrbench/agent/lit_review.py`; `mlrbench/agent/proposal_generator.py`; `mlrbench/agent/experiment_runner.py`; `mlrbench/agent/paper_writer.py`; and first-party provider/util modules directly required by those paths.
- Adjacent first-party surfaces excluded from ownership: `mlrbench/evals/` and MLR-Judge review scripts; `agent_reviews/`; `human_eval/`; benchmark scoring/results; stored example `agent_results/`; benchmark dataset/task metadata except as environmental task input; repository/project governance and publication assets.
- First-party operating / deployment modes considered: documented end-to-end `python run_mlr_agent.py --model_name ... --coding_agent ...` execution, with the supported Claude Code/Codex/Gemini coding-agent backends selected by configuration.
- Recursion level: one research project/task run is the system-in-focus. Idea generation, literature review, proposal generation, experiment execution and paper writing are functional stages inside that project; benchmark reviewers are a separate evaluation system and are not collapsed into this recursion.
- Reviewed revision: `f728d571a992d71c8b526eeb4d9ab6bb5c8cc824`.
- Observation date: 2026-09-27.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

The repository contains both a benchmark/evaluation environment and a separable first-party MLR-Agent runtime. The README explicitly distinguishes the Benchmark Dataset, MLR-Agent and MLR-Judge. The documented end-to-end entrypoint is `run_mlr_agent.py`; for each task it deterministically invokes five stages: idea generation, literature review, proposal generation, experiment execution and paper writing.

The semantic work inside those stages is model-driven. The idea agent selects one research direction from the supplied task. The literature stage invokes a dedicated search-oriented literature engine over that idea/task and asks it to identify relevant recent arXiv work and research challenges. The proposal agent receives the task, idea and literature review and generates a detailed methodology and experimental design. The experiment stage then delegates the concrete implementation/execution loop to a configured autonomous coding-agent dependency (Claude Code, Codex or Gemini CLI) using a first-party prompt that requires experimental planning, code generation, debugging/testing, actual execution, baseline comparison, result analysis and persisted `results.md`. The paper writer consumes those resulting experiment artifacts to generate the final scientific report.

This closes an autonomous research-operation path even though one execution substage is delegated to a supported external coding-agent runtime. The first-party launcher owns the research-task lifecycle and transfers generated state between stages; external coding-agent internals are not separately credited as MLR-Agent metasystem functions.

The literature/proposal path is functionally distinct from ordinary current experiment execution. It looks outward to scientific prior work, identifies challenges, generates a prospective research methodology/experimental design and then passes that adaptation option into the experiment runner. The downstream coding agent is explicitly instructed to implement and test the proposal. That establishes an outside-and-then S4 closure back into current research capability/action, rather than mere retrieval for answering the current prompt.

By contrast, MLR-Judge is not in the standard MLR-Agent control loop. The README documents evaluation as separate commands under `mlrbench/evals/`; `run_mlr_agent.py` does not call those reviewers or return their findings into idea/proposal/experiment/paper regeneration. They are therefore benchmark/evaluation surfaces, not S3* of the assessed standalone MLR-Agent runtime.

Primary evidence:

- [`README.md`](https://github.com/chchenhui/mlrbench/blob/f728d571a992d71c8b526eeb4d9ab6bb5c8cc824/README.md) — explicit separation of MLR-Bench dataset, MLR-Agent and MLR-Judge; documented end-to-end and stepwise agent entrypoints.
- [`run_mlr_agent.py`](https://github.com/chchenhui/mlrbench/blob/f728d571a992d71c8b526eeb4d9ab6bb5c8cc824/run_mlr_agent.py) — standard end-to-end lifecycle wiring idea → literature → proposal → experiment → paper without a Judge/review return stage.
- [`mlrbench/agent/idea_generator.py`](https://github.com/chchenhui/mlrbench/blob/f728d571a992d71c8b526eeb4d9ab6bb5c8cc824/mlrbench/agent/idea_generator.py) — model-driven research-option generation from the supplied task.
- [`mlrbench/agent/lit_review.py`](https://github.com/chchenhui/mlrbench/blob/f728d571a992d71c8b526eeb4d9ab6bb5c8cc824/mlrbench/agent/lit_review.py) — dedicated recent-literature/challenge synthesis from the generated idea and task.
- [`mlrbench/agent/proposal_generator.py`](https://github.com/chchenhui/mlrbench/blob/f728d571a992d71c8b526eeb4d9ab6bb5c8cc824/mlrbench/agent/proposal_generator.py) — proposal/methodology/experimental-design generation from task, idea and literature evidence.
- [`mlrbench/agent/experiment_runner.py`](https://github.com/chchenhui/mlrbench/blob/f728d571a992d71c8b526eeb4d9ab6bb5c8cc824/mlrbench/agent/experiment_runner.py) — configured coding-agent invocation and first-party instructions to implement, debug, execute, compare and analyze real experiments from `task.md`, `idea.md`, `related_work.md` and `proposal.md`.
- [`mlrbench/agent/paper_writer.py`](https://github.com/chchenhui/mlrbench/blob/f728d571a992d71c8b526eeb4d9ab6bb5c8cc824/mlrbench/agent/paper_writer.py) — final paper generation from task/idea/literature/proposal plus actual experiment results and figures.
- [`mlrbench/evals/`](https://github.com/chchenhui/mlrbench/tree/f728d571a992d71c8b526eeb4d9ab6bb5c8cc824/mlrbench/evals) — separate MLR-Judge/evaluation surface, not called by the standard agent lifecycle.

## Operational model

A user supplies one or more task directories containing `task.md`. For each task, MLR-Agent generates an idea, gathers/synthesizes relevant literature, turns that evidence into a research proposal, launches a configured autonomous coding agent in the task workspace to implement and run the experiment, waits for real `results.md`, and then writes the final paper from the accumulated research artifacts.

The stage sequence itself is deterministic, but the substantive research choices are not: model-driven stages choose the idea, relevant literature/challenges and methodology; the configured coding agent chooses implementation/debugging/execution actions under the proposal; paper generation interprets the produced results. Failures in stage materialization are retried or surfaced by first-party runtime logic.

## S1 — Operations

- State: A
- Function: perform the substantive end-to-end research work required to turn an assigned ML research task into implemented experiments, observed results and a scientific artifact.
- Disturbance / variety regulated: open-ended task requirements, choice of research direction, implementation uncertainty, code/runtime failures, dataset/model/tool availability, experimental outcomes and result/paper synthesis needs.
- Decisive decision or feedback right: choose task-specific research content and, during the experiment stage, choose/execute/debug concrete implementation and experimental actions until usable results are produced; later interpret those results into the final paper.
- Decision owner: the model-driven MLR-Agent stages, including the configured autonomous coding-agent process invoked by the first-party experiment runner for experiment implementation/execution.
- Supporting / enforcement mechanisms: task workspace and persisted stage artifacts, first-party provider adapters, stage sequencing, retry/materialization checks, coding-agent subprocess invocation, result-file checks and paper-generation plumbing.
- Closure path: user `task.md` -> model generates research artifacts -> proposal-conditioned coding agent writes/runs/debugs experiments -> execution/results return to the task workspace -> result analysis is persisted -> paper writer consumes actual result evidence -> final scientific artifact is produced.
- Boundary reachability: the documented `run_mlr_agent.py` entrypoint directly executes the complete credited path for every task directory; no benchmark Judge command or custom external orchestration is required for the research run itself.
- Why this is / is not agent-owned: Python fixes the high-level stage order, but the context-sensitive research idea/method/content and concrete experiment actions are selected by model-driven agents; external model/coding runtimes are execution dependencies invoked through the shipped MLR-Agent path rather than human decision makers.
- Evidence: [`run_mlr_agent.py`](https://github.com/chchenhui/mlrbench/blob/f728d571a992d71c8b526eeb4d9ab6bb5c8cc824/run_mlr_agent.py); [`mlrbench/agent/experiment_runner.py`](https://github.com/chchenhui/mlrbench/blob/f728d571a992d71c8b526eeb4d9ab6bb5c8cc824/mlrbench/agent/experiment_runner.py); [`mlrbench/agent/paper_writer.py`](https://github.com/chchenhui/mlrbench/blob/f728d571a992d71c8b526eeb4d9ab6bb5c8cc824/mlrbench/agent/paper_writer.py); [`README.md`](https://github.com/chchenhui/mlrbench/blob/f728d571a992d71c8b526eeb4d9ab6bb5c8cc824/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: Claude Code/Codex/Gemini internals are not imported as first-party MLR-Agent organizational functions; S1 credit is scoped to the autonomous research operation composed and reached by the first-party MLR-Agent runtime.

## S2 — Coordination

- State: —
- Function: no qualifying inter-S1 disturbance-attenuation function is established at the declared research-project boundary.
- Disturbance / variety regulated: stage handoffs and multiple model roles exchange artifacts, but no concrete conflict/oscillation/interference among distinct simultaneously accountable operational S1 units is identified.
- Decisive decision or feedback right: none established for S2.
- Decision owner: none established.
- Supporting / enforcement mechanisms: fixed stage sequencing, task directories, file-based artifact passing and selection of one coding-agent backend.
- Closure path: no material S2-specific interference -> coordination decision -> changed affected-S1 behavior path closes.
- Why this is / is not agent-owned: sequential delegation/artifact transfer is workflow composition rather than VSM coordination.
- Evidence: [`run_mlr_agent.py`](https://github.com/chchenhui/mlrbench/blob/f728d571a992d71c8b526eeb4d9ab6bb5c8cc824/run_mlr_agent.py); [`README.md`](https://github.com/chchenhui/mlrbench/blob/f728d571a992d71c8b526eeb4d9ab6bb5c8cc824/README.md).
- Basis: structural absence.
- Confidence: high.
- Caveats: multiple role/model stages do not become distinct S1 units merely because they are modular.

### Absence scope

- Surfaces inspected: end-to-end runner, all `mlrbench/agent/` stages, coding-agent backend selection, task iteration and file/state handoffs.
- Plausible first-party paths checked: multi-stage agent routing; multiple tasks in one task folder; model-role separation; coding-agent delegation; shared task workspace.
- Why no material first-party path remains: tasks are processed sequentially and internal roles cooperate on one research outcome; no explicit inter-operation disturbance and attenuation feedback relation is established.

## S3 — Inside-and-now control

- State: —
- Function: no distinct superior whole-system current-control function is established above the single research operation.
- Disturbance / variety regulated: stage success/failure and missing artifacts affect progression, but the whole-run order and retry/materialization gates are scripted.
- Decisive decision or feedback right: no autonomous actor is shown forming a whole-project current management view and exercising discretionary authority over shared current resources, commitments, priorities or constraints.
- Decision owner: none established for qualifying S3.
- Supporting / enforcement mechanisms: deterministic stage ordering, task loop, environment/API-key checks, retry bounds and result-file existence gates.
- Closure path: scripted success/failure checks select fixed next stages; semantic agent decisions remain local to S1 research production or S4 prospective planning.
- Why this is / is not agent-owned: `run_mlr_agent.py` is an orchestrator by implementation role, but its current-control choices are pre-authored sequence/control plumbing rather than a model-owned whole-system management function.
- Evidence: [`run_mlr_agent.py`](https://github.com/chchenhui/mlrbench/blob/f728d571a992d71c8b526eeb4d9ab6bb5c8cc824/run_mlr_agent.py); agent stage wrappers under [`mlrbench/agent/`](https://github.com/chchenhui/mlrbench/tree/f728d571a992d71c8b526eeb4d9ab6bb5c8cc824/mlrbench/agent).
- Basis: structural absence.
- Confidence: high.
- Caveats: the coding agent may internally manage its own experiment session, but external dependency internals are not promoted into MLR-Agent S3.

### Absence scope

- Surfaces inspected: task-loop orchestration, all five end-to-end stages, retry/error handling, coding-agent selection and persisted task state.
- Plausible first-party paths checked: top-level runner as manager; experiment coding agent as project manager; stage retries; multi-task loop; result-file gating.
- Why no material first-party path remains: whole-project progression is deterministic and no autonomous superior actor receives a whole-system current view plus broad present-control authority.

## S3* — Complementary audit

- State: —
- Function: no complementary-audit loop returns independent findings into the standard MLR-Agent research operation.
- Disturbance / variety regulated: MLR-Judge can score/review generated research in the benchmark, but those review programs are separate evaluation surfaces rather than part of the agent's corrective control path.
- Decisive decision or feedback right: none established in the standard agent runtime for an independent auditor whose findings trigger correction/regeneration.
- Decision owner: none established for qualifying S3*.
- Supporting / enforcement mechanisms: `mlrbench/evals/` contains overall and stage-specific reviewers, but they are invoked through separate documented commands and do not participate in `run_mlr_agent.py`.
- Closure path: standard agent run ends after paper generation; no first-party reviewer finding -> corrective research action -> re-review loop is wired into that path.
- Why this is / is not agent-owned: evaluation exists in the repository, but organizational function is determined by wiring and feedback rights, not by the presence of reviewer code or benchmark scores.
- Evidence: [`README.md`](https://github.com/chchenhui/mlrbench/blob/f728d571a992d71c8b526eeb4d9ab6bb5c8cc824/README.md); [`run_mlr_agent.py`](https://github.com/chchenhui/mlrbench/blob/f728d571a992d71c8b526eeb4d9ab6bb5c8cc824/run_mlr_agent.py); [`mlrbench/evals/`](https://github.com/chchenhui/mlrbench/tree/f728d571a992d71c8b526eeb4d9ab6bb5c8cc824/mlrbench/evals).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: MLR-Judge is valuable independent evaluation of agent outputs, but assessment does not borrow an adjacent evaluation system into the standalone MLR-Agent organization.

### Absence scope

- Surfaces inspected: standard runner, experiment/paper stages, `mlrbench/evals/overall_review.py`, stage-specific review scripts and stored review artifacts.
- Plausible first-party paths checked: experiment result analysis inside coding-agent prompt; MLR-Judge overall review; idea/proposal/experiment/writeup reviewers; stored `agent_reviews/`.
- Why no material first-party path remains: in-band experiment analysis belongs to S1; independent Judge programs are not wired back into the operational research lifecycle and stored benchmark reviews are evidence artifacts, not a corrective runtime channel.

## S4 — Outside-and-then intelligence

- State: A
- Function: sense relevant external scientific work/challenges, turn that evidence into a prospective methodology/experimental option, and return the option into executable research.
- Disturbance / variety regulated: existing recent research, known challenges/limitations and alternative methodological choices may make the initially selected direction weak, redundant or require a different experimental design.
- Decisive decision or feedback right: select/synthesize relevant recent literature and challenges, then choose a detailed methodology and experimental design that determines what the later coding-agent operation will implement and test.
- Decision owner: the model-driven literature-review and proposal-generation stages invoked by the first-party MLR-Agent pipeline.
- Supporting / enforcement mechanisms: dedicated search-oriented literature engine, persisted `idea.md`/`related_work.md`/`proposal.md`, prompt contracts requiring recent papers/challenges/methodology/evaluation design, and the experiment runner's direct consumption of those artifacts.
- Closure path: task + candidate idea -> literature engine gathers/synthesizes external scientific evidence -> proposal agent generates prospective methodology/experimental design -> `proposal.md` is supplied to the configured coding agent -> coding agent implements and executes that design -> current S1 research capability/action changes accordingly.
- Boundary reachability: literature review and proposal generation are mandatory stages of the documented standard `run_mlr_agent.py` path before `run_experiment()`; no optional custom integration is needed.
- Why this is / is not agent-owned: external search/model providers supply observations/computation, while relevance/challenge synthesis and methodology/experiment-option generation are model-driven stages selected and wired by the first-party runtime.
- External distinction: recent arXiv/scientific literature and extracted prior-work challenges are environmental evidence beyond the local task workspace.
- Future / prospective distinction: the proposal describes methodology, data collection, algorithms, experiment design and evaluation to be performed next rather than merely reporting current execution state.
- Adaptation option generated: a concrete `proposal.md` research methodology and experimental plan grounded in the idea and literature review.
- Path back into current capability / S3: `experiment_runner.py` explicitly instructs the selected coding agent to read `task.md`, `idea.md`, `related_work.md` and `proposal.md`, design/implement the experiment and run it; the prospective option therefore changes subsequent executable S1 work.
- Evidence: [`mlrbench/agent/lit_review.py`](https://github.com/chchenhui/mlrbench/blob/f728d571a992d71c8b526eeb4d9ab6bb5c8cc824/mlrbench/agent/lit_review.py); [`mlrbench/agent/proposal_generator.py`](https://github.com/chchenhui/mlrbench/blob/f728d571a992d71c8b526eeb4d9ab6bb5c8cc824/mlrbench/agent/proposal_generator.py); [`mlrbench/agent/experiment_runner.py`](https://github.com/chchenhui/mlrbench/blob/f728d571a992d71c8b526eeb4d9ab6bb5c8cc824/mlrbench/agent/experiment_runner.py); [`run_mlr_agent.py`](https://github.com/chchenhui/mlrbench/blob/f728d571a992d71c8b526eeb4d9ab6bb5c8cc824/run_mlr_agent.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the initial idea is generated before the literature review rather than novelty-filtered by it; S4 credit rests on literature evidence changing the downstream prospective proposal/experimental design, not on a claim that MLR-Agent performs a separate novelty-admission gate.

## S5 — Policy and identity

- State: —
- Function: no runtime identity/ultimate-policy authority for the research organization is established.
- Disturbance / variety regulated: task definition, model/backend choice, API credentials and experiment constraints shape operation but are supplied through task/configuration/static prompts.
- Decisive decision or feedback right: define or revise the ultimate research purpose/identity/top-level policy independently of the supplied task and configuration.
- Decision owner: external user/developer/configuration; no qualifying first-party runtime S5 owner is established.
- Supporting / enforcement mechanisms: `task.md`, CLI model/coding-agent flags, static research/experiment prompts, API/environment requirements and fixed stage order.
- Closure path: no material first-party S5-specific identity/policy adjudication loop closes.
- Why this is / is not agent-owned: MLR-Agent chooses how to investigate the assigned research task, but the task purpose and top-level constraints are externally supplied and not subject to an internal ultimate-authority loop.
- Evidence: [`README.md`](https://github.com/chchenhui/mlrbench/blob/f728d571a992d71c8b526eeb4d9ab6bb5c8cc824/README.md); [`run_mlr_agent.py`](https://github.com/chchenhui/mlrbench/blob/f728d571a992d71c8b526eeb4d9ab6bb5c8cc824/run_mlr_agent.py); first-party stage prompts under [`mlrbench/agent/`](https://github.com/chchenhui/mlrbench/tree/f728d571a992d71c8b526eeb4d9ab6bb5c8cc824/mlrbench/agent).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: strong static experiment instructions are constraints, not evidence that the runtime itself owns identity-level policy.

### Absence scope

- Surfaces inspected: top-level task/configuration inputs, all MLR-Agent stage prompts, provider/backend selection, environment checks and standard end-to-end lifecycle.
- Plausible first-party paths checked: idea selection as ultimate purpose; proposal constraints as policy; coding-agent experiment rules; MLR-Judge decisions; CLI backend selection.
- Why no material first-party path remains: these choices either elaborate the assigned research task or enforce configured execution policy; none establishes ultimate authority over organizational identity/purpose.

## Recursion

One assigned research project is the assessed recursion. Model roles and the configured coding-agent backend are functional participants in that project rather than separate viable organizations imported wholesale. MLR-Judge is a neighboring benchmark/evaluation system and remains outside the operational recursion because its findings are not returned through the standard MLR-Agent lifecycle.

## Variety and escalation

MLR-Agent attenuates research variety by progressively materializing idea, literature, proposal, experiment and paper artifacts in one task workspace. External scientific uncertainty is handled prospectively through the literature/proposal S4 path before experiment execution. Implementation/runtime uncertainty is handled inside the coding-agent S1 stage. Stage failures are bounded by scripted retries/errors. No separate whole-system S3 or identity-level S5 escalation owner is established.

## Evidence gaps

- Structural review only; no new model/API/experiment run was executed.
- External coding-agent internals are deliberately not used to infer additional MLR-Agent S2-S5 functions.
- MLR-Judge could participate in S3* in a different composed system if its independent findings were wired back into MLR-Agent correction; the pinned standard end-to-end path does not do so.
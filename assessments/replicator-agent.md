---
harness_id: replicator-agent
project_name: ReplicatorAgent
repository: https://github.com/CenterForOpenScience/llm-benchmarking
review_ref: fb6a804fd710764f3ad3c8b84e1323c2804c4776
reviewed_at: 2026-09-27
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-27
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# ReplicatorAgent

## Review boundary

- System in focus: one first-party ReplicatorAgent / ReplicatorBench replication run at pinned revision `fb6a804fd710764f3ad3c8b84e1323c2804c4776`, bounded to the documented Extract → Design → Execute → Interpret agent pipeline and the core agent/tool runtime it invokes.
- Purpose and identity: reproduce a supplied scientific claim/study by extracting study metadata, designing a replication and analysis plan, executing generated analysis inside a Docker sandbox with result-conditioned debugging, and interpreting the resulting evidence into a scientific replication report.
- Relevant environment: original paper/study files and datasets; external model providers; operating system/Docker; third-party Python/R/Stata dependencies; the human operator providing the mandatory pre-execution approval; optionally invoked web-search services; benchmark ground truth and evaluators.
- Standard-distribution boundary: `replicatorbench/core/`, `replicatorbench/info_extractor/`, `replicatorbench/generator/`, `replicatorbench/interpreter/` and the documented `make pipeline-easy` path. External model providers, Docker engine/container substrate, scientific datasets, controlled package ecosystems and the human operator remain environment/Parent/support. The benchmark validator is adjacent evaluation rather than part of the standalone ReplicatorAgent operation.
- Credited operating / distribution surfaces: `replicatorbench/README.md`; `replicatorbench/Makefile`; `replicatorbench/core/agent.py`; `replicatorbench/core/actions.py`; `replicatorbench/core/tools.py`; `replicatorbench/info_extractor/extractor.py`; `replicatorbench/generator/design_agent.py`; `replicatorbench/generator/execute_agent.py`; `replicatorbench/generator/execute_tools.py`; `replicatorbench/generator/orchestrator_tool.py`; and `replicatorbench/interpreter/agent.py`.
- Adjacent first-party surfaces excluded from ownership: `replicatorbench/validator/` and evaluate-* commands; benchmark datasets/ground truth and stored benchmark results; tests; research-paper/project-governance surfaces; optional web-search output where it is not wired into the standard `pipeline-easy` closure.
- First-party operating / deployment modes considered: the documented easy-tier full pipeline `make pipeline-easy STUDY=... MODEL=...` and the directly corresponding Extract, Design, Execute and Interpret modules. The separately invokable `make web-search` and `make evaluate-*` modes are inspected for possible S4/S3* evidence but are not silently imported into the standard pipeline.
- Recursion level: one scientific replication task/run is the system-in-focus. Extract, Design, Execute and Interpret are functional stages of one replication operation rather than separately viable S1 organizations solely because they use separate agents/prompts.
- Reviewed revision: `fb6a804fd710764f3ad3c8b84e1323c2804c4776`.
- Observation date: 2026-09-27.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

ReplicatorBench explicitly separates the autonomous replication pipeline from its LLM-as-judge validator. The documented full operation is `pipeline-easy: extract-stage1 design-easy execute-easy interpret-easy`. Extraction converts the supplied study artifacts into structured replication information. The design agent then runs a multi-turn tool-using ReAct loop that can inspect files/datasets and decides how the replication should be implemented. The execute agent uses the same first-party agent loop with Docker orchestration tools and is explicitly instructed to inspect build/runtime failures, modify replication configuration or analysis code, rebuild/retry when necessary, and only finalize once execution succeeds or is cancelled. The interpreter is another tool-using agent that selectively reads produced files/logs/results and synthesizes the scientific interpretation.

The execute stage includes a mandatory human approval before the generated analysis command is actually run. That approval is a real safety/authorization gate and is recorded as supporting Parent involvement, but it does not choose the substantive analysis code, replication design, debugging fix or interpretation. Before the approval, the agent has already designed the action and previewed the command; after approval, the agent continues to own the error diagnosis/fix/retry loop. Under Methodology 0.3.6 S1 has no `P` publication state, and generic approval does not by itself transfer an organizational function. The decisive operational research choices remain agent-owned, so S1 is `A` with the human gate noted as a constraint.

The optional web-search command does not establish S4 at this boundary. It searches for URLs/resources needed to carry out the current replication claim. More importantly, `make pipeline-easy` does not invoke `web-search`, and the reviewed code does not establish a standard return from its saved search result into a prospective capability/posture change. Research design inside `design_agent.py` is future-looking in the ordinary planning sense but remains planning of the current S1 replication operation from supplied study evidence.

The validator likewise does not establish S3*. Evaluation is exposed through separate `make evaluate-*` / `evaluate-pipeline-easy` commands and benchmarks outputs against expert ground truth. The standard replication pipeline terminates after interpretation and does not wire those independent validator findings back into Design/Execute/Interpret correction. Repository co-location therefore does not transfer validator ownership into the assessed operational organization.

Primary evidence:

- [`replicatorbench/README.md`](https://github.com/CenterForOpenScience/llm-benchmarking/blob/fb6a804fd710764f3ad3c8b84e1323c2804c4776/replicatorbench/README.md) — documented Extract → Design → Execute → Interpret pipeline, separate web-search command and separate LLM-as-judge evaluation commands.
- [`replicatorbench/Makefile`](https://github.com/CenterForOpenScience/llm-benchmarking/blob/fb6a804fd710764f3ad3c8b84e1323c2804c4776/replicatorbench/Makefile) — mechanical standard pipeline wiring and separation of evaluate/web-search targets.
- [`replicatorbench/core/agent.py`](https://github.com/CenterForOpenScience/llm-benchmarking/blob/fb6a804fd710764f3ad3c8b84e1323c2804c4776/replicatorbench/core/agent.py) — shared multi-turn agent/tool loop that returns tool observations to the model and continues until a final structured answer.
- [`replicatorbench/generator/design_agent.py`](https://github.com/CenterForOpenScience/llm-benchmarking/blob/fb6a804fd710764f3ad3c8b84e1323c2804c4776/replicatorbench/generator/design_agent.py) — agent-owned replication design over current study artifacts and datasets.
- [`replicatorbench/generator/execute_agent.py`](https://github.com/CenterForOpenScience/llm-benchmarking/blob/fb6a804fd710764f3ad3c8b84e1323c2804c4776/replicatorbench/generator/execute_agent.py) — Docker build/run/execute/debug loop, mandatory human authorization gate, error-conditioned code/config fixes and retries.
- [`replicatorbench/interpreter/agent.py`](https://github.com/CenterForOpenScience/llm-benchmarking/blob/fb6a804fd710764f3ad3c8b84e1323c2804c4776/replicatorbench/interpreter/agent.py) — tool-using result/log exploration and final scientific interpretation.
- [`replicatorbench/info_extractor/extractor.py`](https://github.com/CenterForOpenScience/llm-benchmarking/blob/fb6a804fd710764f3ad3c8b84e1323c2804c4776/replicatorbench/info_extractor/extractor.py) — extraction stage and separately invoked one-shot web-search path.

## Operational model

A replication run begins from supplied study artifacts. The extractor creates structured source-study information. The design agent receives the study files/template and uses a tool-enabled ReAct loop to inspect data/files and produce the replication design/code configuration. The execute agent then creates and builds a Docker runtime, previews the selected entry point, requests explicit human authorization to run it, executes the analysis, observes errors/results and autonomously chooses configuration/code repairs and retries. The interpreter subsequently explores produced logs/results and emits a structured replication interpretation.

The human approval determines whether the already selected command is permitted to execute, but does not select the replication design or choose the corrective action. If approval is denied, the standard path cancels. The agent therefore owns the discretionary operational content while Parent supplies a bounded execution authorization constraint.

## S1 — Operations

- State: A
- Function: carry out the substantive scientific replication operation from source-study extraction through replication design, executable analysis/debugging and result interpretation.
- Disturbance / variety regulated: heterogeneous study files/data, incomplete replication metadata, analysis-design uncertainty, package/environment incompatibilities, Docker build failures, generated-code/runtime errors, statistical outputs and ambiguous result/log evidence.
- Decisive decision or feedback right: choose the replication design and analysis implementation, decide from tool/build/runtime observations what files/configuration/code to inspect or modify, decide how to retry failed execution, and decide what produced evidence means for the final replication interpretation.
- Decision owner: the first-party model-driven ReplicatorAgent/ReAct stages; the human operator owns only the bounded authorization gate before executing the already selected analysis command.
- Supporting / enforcement mechanisms: first-party tool schemas/action dispatch, study-scoped file access, JSON templates, Docker generation/build/run tools, process/container isolation, checkpoint/turn limits, persisted stage files/metadata and mandatory human approval.
- Closure path: supplied study evidence -> agent extracts/designs replication -> Docker/code action is prepared -> human authorization gate permits execution -> environment returns build/runtime/result evidence -> agent diagnoses/fixes/retries as needed -> interpreter inspects the resulting evidence -> final replication report/structured interpretation is produced.
- Boundary reachability: `make pipeline-easy` directly invokes the Extract, Design, Execute and Interpret stages in the standard distribution; Design/Execute/Interpret use the shipped `run_react_loop` and first-party tools without requiring benchmark validator orchestration.
- Why this is / is not agent-owned: deterministic code enforces tool calls, sandboxing, stage order and the safety approval gate, while the context-sensitive scientific design, code/config repair, retry and interpretation choices are model-driven. Removing the model decision path while keeping the human approval and Docker machinery would not produce materially the same discretionary replication choices.
- Evidence: [`replicatorbench/Makefile`](https://github.com/CenterForOpenScience/llm-benchmarking/blob/fb6a804fd710764f3ad3c8b84e1323c2804c4776/replicatorbench/Makefile); [`replicatorbench/core/agent.py`](https://github.com/CenterForOpenScience/llm-benchmarking/blob/fb6a804fd710764f3ad3c8b84e1323c2804c4776/replicatorbench/core/agent.py); [`replicatorbench/generator/design_agent.py`](https://github.com/CenterForOpenScience/llm-benchmarking/blob/fb6a804fd710764f3ad3c8b84e1323c2804c4776/replicatorbench/generator/design_agent.py); [`replicatorbench/generator/execute_agent.py`](https://github.com/CenterForOpenScience/llm-benchmarking/blob/fb6a804fd710764f3ad3c8b84e1323c2804c4776/replicatorbench/generator/execute_agent.py); [`replicatorbench/interpreter/agent.py`](https://github.com/CenterForOpenScience/llm-benchmarking/blob/fb6a804fd710764f3ad3c8b84e1323c2804c4776/replicatorbench/interpreter/agent.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the standard Execute path cannot cross its actual-analysis authorization gate without human approval. This is treated as a bounded safety/permission constraint on an otherwise agent-owned operation, not a separate published S1 Parent state, which Methodology 0.3.6 does not define.

## S2 — Coordination

- State: —
- Function: no qualifying inter-S1 interference-attenuation function is established at the declared one-replication recursion.
- Disturbance / variety regulated: none qualifying; Extract, Design, Execute and Interpret are sequential stages contributing to one operational outcome rather than distinct concurrently accountable S1 units with a concrete interaction disturbance.
- Decisive decision or feedback right: none established for S2.
- Decision owner: none established.
- Supporting / enforcement mechanisms: Makefile sequencing, persisted stage artifacts and tool/state transfer are workflow composition, not S2.
- Closure path: no material inter-S1 disturbance -> coordination decision -> changed affected-S1 behaviour path closes.
- Why this is / is not agent-owned: multiple modules/agents and artifact handoffs do not establish the coordination function without a specific cross-operation conflict/oscillation/interference witness.
- Evidence: [`replicatorbench/Makefile`](https://github.com/CenterForOpenScience/llm-benchmarking/blob/fb6a804fd710764f3ad3c8b84e1323c2804c4776/replicatorbench/Makefile); [`replicatorbench/README.md`](https://github.com/CenterForOpenScience/llm-benchmarking/blob/fb6a804fd710764f3ad3c8b84e1323c2804c4776/replicatorbench/README.md).
- Basis: structural absence.
- Confidence: high.
- Caveats: parallel external benchmark execution would define a different operational boundary if independently accountable replication workers and an interference problem were introduced.

### Absence scope

- Surfaces inspected: full pipeline wiring, core agent loop, stage agents/tools, Docker orchestration, study workspaces and validator separation.
- Plausible first-party paths checked: multiple named stage agents; stage sequencing; shared study directory; Docker/resource use; tool routing; evaluation stages.
- Why no material first-party path remains: the reviewed standard pipeline composes one replication operation sequentially and no first-party path identifies/attenuates a disturbance among distinct S1 operations.

## S3 — Inside-and-now control

- State: —
- Function: no distinct superior whole-system current-control actor is established above the single replication operation.
- Disturbance / variety regulated: stage failures, build/runtime failures and current execution state are regulated, but either by scripted stage order or within the same S1 Execute/debug loop.
- Decisive decision or feedback right: no autonomous actor is evidenced with a whole-system current view and broad discretionary authority over multiple operational units/shared current resources, priorities, commitments or constraints.
- Decision owner: none established for qualifying S3.
- Supporting / enforcement mechanisms: Makefile stage ordering, execute checkpoints, turn limits, Docker lifecycle and the human safety approval gate.
- Closure path: scripted stages and local S1 error/retry feedback determine progression; no separate management loop over a current operational whole closes.
- Why this is / is not agent-owned: the execute agent's debugging authority is task-local S1 recovery. The Makefile/orchestrator transports and enforces stage progression but does not make contextual whole-system management decisions.
- Evidence: [`replicatorbench/Makefile`](https://github.com/CenterForOpenScience/llm-benchmarking/blob/fb6a804fd710764f3ad3c8b84e1323c2804c4776/replicatorbench/Makefile); [`replicatorbench/generator/execute_agent.py`](https://github.com/CenterForOpenScience/llm-benchmarking/blob/fb6a804fd710764f3ad3c8b84e1323c2804c4776/replicatorbench/generator/execute_agent.py).
- Basis: structural absence.
- Confidence: high.
- Caveats: the mandatory human approval is authorization of one execution boundary, not evidence of a first-party S3 parent loop with whole-system current control.

### Absence scope

- Surfaces inspected: Makefile pipeline, run_react_loop, Execute checkpoint map, Docker orchestration, human approval, stage state/metadata and interpretation flow.
- Plausible first-party paths checked: execute orchestrator as manager; human approval as S3 Parent; checkpoint state; pipeline Makefile as supervisor; Docker lifecycle controller.
- Why no material first-party path remains: none combines a whole-system current management view with discretionary present authority over a population of S1 operations; the identified controls are fixed workflow/safety enforcement or local operational recovery.

## S3* — Complementary audit

- State: —
- Function: the repository contains a materially separate LLM-as-judge validator, but the standalone ReplicatorAgent pipeline does not close validator findings back into corrective operation.
- Disturbance / variety regulated: validator commands can detect extraction/design/execution/interpretation disagreement against benchmark ground truth, but those findings serve benchmark evaluation rather than the standard agent's corrective feedback path.
- Decisive decision or feedback right: none established in the standard pipeline for an independent auditor whose findings trigger a later operational correction.
- Decision owner: none established for qualifying S3* inside ReplicatorAgent.
- Supporting / enforcement mechanisms: `replicatorbench/validator/`, expert-annotated ground truth, stage-specific evaluate commands and aggregate evaluation reports are adjacent evaluation infrastructure.
- Closure path: `pipeline-easy` ends after Interpret; validator execution requires separate `evaluate-*` commands and no first-party path returns its findings into Extract/Design/Execute/Interpret modification and re-run.
- Why this is / is not agent-owned: complementary evaluation evidence exists, but S3* requires the organizational feedback function, not merely an independent benchmark scorer in the same repository.
- Evidence: [`replicatorbench/README.md`](https://github.com/CenterForOpenScience/llm-benchmarking/blob/fb6a804fd710764f3ad3c8b84e1323c2804c4776/replicatorbench/README.md); [`replicatorbench/Makefile`](https://github.com/CenterForOpenScience/llm-benchmarking/blob/fb6a804fd710764f3ad3c8b84e1323c2804c4776/replicatorbench/Makefile).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: a composed system that automatically applies validator findings and reruns the affected operational stage could establish S3*; that wiring is not present in the frozen standard pipeline.

### Absence scope

- Surfaces inspected: standard pipeline targets, validator/evaluate targets, core agent loop, generated stage artifacts and interpreter output.
- Plausible first-party paths checked: LLM-as-judge validators; evaluate-pipeline target; execution-result checking; interpreter as reviewer; Docker preview/human approval.
- Why no material first-party path remains: independent validator findings are terminal benchmark/evaluation outputs; in-band execution checking and interpretation are ordinary S1 feedback rather than a complementary audit relation.

## S4 — Outside-and-then intelligence

- State: —
- Function: no qualifying external-and-prospective adaptation loop that changes future/current organizational capability is established in the standard ReplicatorAgent pipeline.
- Disturbance / variety regulated: optional web search can identify external data resources useful for the current replication, and Design chooses a plan for the current study, but neither establishes a separate prospective organizational adaptation function.
- Decisive decision or feedback right: none established for S4.
- Decision owner: none established for qualifying S4.
- Supporting / enforcement mechanisms: separately invokable `web-search`, Responses API web search, current-study design agent, study documents and generated replication plan.
- Closure path: no standard external evidence -> prospective adaptation option -> changed installed/current organizational capability loop closes. `pipeline-easy` does not invoke web-search, and search output is not mechanically returned into a persistent adaptation path.
- Why this is / is not agent-owned: searching for datasets/resources needed to execute the current assigned replication and planning that replication are current-task S1 research work, not S4 merely because they look outward or ahead.
- Evidence: [`replicatorbench/README.md`](https://github.com/CenterForOpenScience/llm-benchmarking/blob/fb6a804fd710764f3ad3c8b84e1323c2804c4776/replicatorbench/README.md); [`replicatorbench/Makefile`](https://github.com/CenterForOpenScience/llm-benchmarking/blob/fb6a804fd710764f3ad3c8b84e1323c2804c4776/replicatorbench/Makefile); [`replicatorbench/info_extractor/extractor.py`](https://github.com/CenterForOpenScience/llm-benchmarking/blob/fb6a804fd710764f3ad3c8b84e1323c2804c4776/replicatorbench/info_extractor/extractor.py); [`replicatorbench/generator/design_agent.py`](https://github.com/CenterForOpenScience/llm-benchmarking/blob/fb6a804fd710764f3ad3c8b84e1323c2804c4776/replicatorbench/generator/design_agent.py).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: web-search may enrich a manually composed replication workflow, but optional information retrieval for a current study is not enough to publish S4 without a prospective adaptation closure.

### Absence scope

- Surfaces inspected: standard pipeline wiring, separate web-search command/implementation, design agent, execution agent, interpreter, persisted study outputs and validator flow.
- Plausible first-party paths checked: web search as environmental intelligence; design as future planning; debug-induced code changes; cross-run metadata/results; benchmark feedback.
- Why no material first-party path remains: each identified path either supports the current replication episode, is not wired into the standard pipeline, or belongs to adjacent evaluation; no prospective capability/posture adaptation returns into the assessed organization.

## S5 — Policy and identity

- State: —
- Function: no first-party runtime identity/ultimate-policy authority is established.
- Disturbance / variety regulated: the supplied study/claim, prompts/templates, tier/code mode, model choice, sandbox restrictions and human execution authorization constrain the replication but do not constitute an identity-level decision loop.
- Decisive decision or feedback right: define or revise the ultimate purpose/identity/top-level policy of the replication organization beyond the externally supplied task and static configuration.
- Decision owner: external user/developer/configuration; no qualifying first-party S5 owner is established.
- Supporting / enforcement mechanisms: CLI/Make parameters, static prompts/templates, study path, Docker restrictions, file-operation policies, model API configuration and human authorization.
- Closure path: no material first-party identity/ultimate-policy issue -> authoritative decision -> return-to-operation loop closes.
- Why this is / is not agent-owned: ReplicatorAgent autonomously decides how to reproduce the supplied claim within configured constraints, not what ultimate organizational identity/purpose it should pursue.
- Evidence: [`replicatorbench/README.md`](https://github.com/CenterForOpenScience/llm-benchmarking/blob/fb6a804fd710764f3ad3c8b84e1323c2804c4776/replicatorbench/README.md); [`replicatorbench/generator/execute_agent.py`](https://github.com/CenterForOpenScience/llm-benchmarking/blob/fb6a804fd710764f3ad3c8b84e1323c2804c4776/replicatorbench/generator/execute_agent.py); [`replicatorbench/generator/design_agent.py`](https://github.com/CenterForOpenScience/llm-benchmarking/blob/fb6a804fd710764f3ad3c8b84e1323c2804c4776/replicatorbench/generator/design_agent.py).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: human approval of a concrete command is not identity/ultimate-policy closure and therefore is not promoted to S5=P.

### Absence scope

- Surfaces inspected: user/study inputs, prompt/configuration surfaces, design/execute/interpreter agents, human approval path, Docker/file policies and validator separation.
- Plausible first-party paths checked: human approval as S5; static replication rules as policy; model/tier/code-mode selection; claim/study identity; validator verdicts as ultimate authority.
- Why no material first-party path remains: these surfaces constrain or authorize current work but do not adjudicate the organization's identity/ultimate purpose through a first-party S5 closure.

## Recursion

One scientific replication task is the assessed recursion. Extract, Design, Execute and Interpret are internal functional stages of that operation. The human operator is an external authorization actor at the execute boundary, not a separately published S3/S4/S5 parent mode under the evidence found. The LLM-as-judge validator is a neighboring benchmark/evaluation system, and optional web search is an adjacent current-task resource-discovery mode.

## Variety and escalation

ReplicatorAgent attenuates replication variety through structured extraction/templates, model-driven design, study-scoped tools, sandboxed execution and an explicit result-conditioned Docker/code repair loop. Operational execution escalates once to human authorization before running the actual analysis command; denial cancels rather than transferring scientific design authority. Build/runtime errors return to the execute agent for autonomous diagnosis and repair. Benchmark validation is a separate post-run evaluation path and does not return into standard operation.

## Evidence gaps

- Structural review only; no new model/API/Docker run was executed.
- The assessment treats the mandatory human approval as a bounded authorization/safety gate rather than substantive S1 ownership because the human does not choose the analysis action or correction. A future mode in which the human selects or revises the operational action itself would require boundary reassessment.
- Optional web-search and validator modes were inspected specifically to avoid borrowing adjacent S4/S3* functions into the standard pipeline.
---
harness_id: cedar
project_name: CEDAR
repository: https://github.com/Fraunhofer-IIS/cedar
review_ref: ab5820b360eab75a84320f551642fe6386513bab
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
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# CEDAR

## Review boundary

- System in focus: one first-party CEDAR data-science run at pinned revision `ab5820b360eab75a84320f551642fe6386513bab`, including the shipped Streamlit runtime, orchestrator/text/code roles, persistent Python execution namespace, result/error feedback loop, and optional Critique role.
- Purpose and identity: carry a user-supplied data-science problem from project brief through iterative explanation, executable Python, evaluation and completion while preserving local data and notebook-like context.
- Relevant environment: user-provided `general.txt` / `task.txt`, local datasets/files, Python libraries, external model providers or Ollama, Streamlit/operator UI, and machine resources.
- Standard-distribution boundary: `cedar_public.py` and the documented `streamlit run cedar_public.py` operating path. External model services, datasets, Python packages and the human/operator remain environment unless a first-party path explicitly assigns them a CEDAR function.
- Credited operating / distribution surfaces: `README.md`; `cedar_public.py` including role prompts/tool schemas, `safe_exec`, history rendering, orchestrator/text/code routing, retry logic, Critique path and Streamlit run controls.
- Adjacent first-party surfaces excluded from ownership: publication poster/slides, README publication links, repository development/governance surfaces and benchmark/demo evidence that do not execute inside the shipped CEDAR run.
- First-party operating / deployment modes considered: interactive or Autorun Streamlit execution with GPT-4o and/or Qwen3Coder role choices; optional operator-triggered Critique pass; local Python execution with configured retry budget.
- Recursion level: one CEDAR data-science run is the system-in-focus. The named Orchestrator, Text, Code and Critique roles are functionally inspected, but role names do not create separate viable systems or S1 units by themselves.
- Reviewed revision: `ab5820b360eab75a84320f551642fe6386513bab`.
- Observation date: 2026-09-26.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

CEDAR is shipped as a Streamlit application in `cedar_public.py`. The runtime keeps an ordered notebook-like list of cells plus a persistent Python namespace. A model-driven Orchestrator chooses exactly one next action: request explanatory text, request executable code, or finish. Text and Code role calls materialize the requested cell. Code is executed immediately through `safe_exec`; stdout, stderr and full traceback are captured, stored with the cell and fed into subsequent context. Failing code is retried by asking the Code role to repair the same step from the concrete traceback until success or the configured retry limit is reached. Notebook history is rendered into bounded context for later decisions.

The three main roles therefore form one operational data-science loop rather than three independent S1 units. Routing between Text and Code is task-local sequencing inside that operation. The Orchestrator decides what the same run should do next, but no superior whole-system regulator over multiple operational units, resource pools or independent commitments is established.

CEDAR additionally ships a distinct Critique path. `run_critique_step` builds a separate review request over the latest iteration, optionally including `metrics.txt` and `model_card.txt`, and calls a Critique LLM under a dedicated reviewer prompt that checks bugs, coherence, leakage/brittleness and ways to improve metrics/robustness. The produced review is stored in `critique_review`, appended visibly to the notebook and injected as developer context into future Orchestrator messages. This is a genuine complementary review relation rather than ordinary code retry. However the path is optional and operator-triggered via the `Critique` button, and the pinned implementation does not autonomously schedule it as a default audit loop; after `finish`, the runtime also does not independently reopen the sealed run. It is therefore constructor-owned S3* rather than autonomous S3*.

No prospective adaptation function was found that changes CEDAR's installed capabilities across future independent runs. Context/history compression, retries and critique-driven improvement remain part of the current run. Identity, ultimate purpose, model selection and top-level task constraints remain operator/configuration owned rather than runtime S5 authority.

Primary evidence:

- [`README.md`](https://github.com/Fraunhofer-IIS/cedar/blob/ab5820b360eab75a84320f551642fe6386513bab/README.md) — shipped Streamlit entrypoint and project description: separate plan/code agents, iterative generation, local execution, fault tolerance and smart history rendering.
- [`cedar_public.py`](https://github.com/Fraunhofer-IIS/cedar/blob/ab5820b360eab75a84320f551642fe6386513bab/cedar_public.py) — role prompts/tool schemas; persistent cell/session state; `safe_exec`; `render_history_for_model`; `build_orchestrator_messages`; `build_critique_messages`; `run_critique_step`; `do_one_step`; retry and UI control paths.

## Operational model

The operational outcome is one evolving data-science notebook/run. The Orchestrator selects the next task-local action; Text or Code produces the requested artifact; executable Python changes local state and returns concrete result/error feedback; later model calls use that feedback to continue or repair the run. This closes an agent-owned S1 loop.

The optional Critique role is not another operational producer. It rereads the current run through a reviewer-specific prompt and broader review context, then returns findings to the Orchestrator path. Because activation is supplied by an operator-facing constructor surface instead of an autonomous first-party scheduling/decision path, the complementary-audit function is credited as `C`.

## S1 — Operations

- State: A
- Function: perform the substantive data-science workflow through model-selected notebook steps, generated executable Python and result-conditioned continuation/repair.
- Disturbance / variety regulated: task complexity, changing intermediate data/model state, uncertain next analysis step, execution failures, library/API mistakes, model/evaluation results and bounded context.
- Decisive decision or feedback right: choose whether the next substantive step is explanatory text, executable code or completion; generate the code/content for that step; use returned outputs/errors to decide subsequent work.
- Decision owner: the first-party model-driven Orchestrator plus routed Text/Code roles inside the CEDAR runtime.
- Supporting / enforcement mechanisms: tool schemas, persistent cell list, `exec_globals`, `safe_exec`, stdout/stderr/traceback capture, retry budget, history rendering and Streamlit/Autorun loop.
- Closure path: project brief + notebook history -> Orchestrator selects next action -> Text/Code role creates a cell -> code executes locally when applicable -> outputs/errors are stored -> later model call reads the changed history -> the run repairs, advances or finishes.
- Boundary reachability: `streamlit run cedar_public.py` directly instantiates the credited model-routing, execution and feedback loop; no adjacent benchmark/development system is required for closure.
- Why this is / is not agent-owned: deterministic Python transports state and executes generated code, while the substantive next-step, code/content and repair choices are model-generated from the live run context.
- Evidence: [`README.md`](https://github.com/Fraunhofer-IIS/cedar/blob/ab5820b360eab75a84320f551642fe6386513bab/README.md); [`cedar_public.py`](https://github.com/Fraunhofer-IIS/cedar/blob/ab5820b360eab75a84320f551642fe6386513bab/cedar_public.py) (`ORCH_SYSTEM`, `CODE_SYSTEM`, `safe_exec`, `render_history_for_model`, `do_one_step`).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the user supplies the top-level task and runtime/model configuration, but the within-run operational choices close autonomously once execution is underway.

## S2 — Coordination

- State: —
- Function: no qualifying inter-S1 disturbance-attenuation function is established at the declared boundary.
- Disturbance / variety regulated: none qualifying; role routing and notebook sequencing regulate one operational workflow rather than interference among distinct S1 units.
- Decisive decision or feedback right: none established for S2.
- Decision owner: none established.
- Supporting / enforcement mechanisms: Orchestrator routing, role-specific tool calls, shared history and single-step sequencing are present but are not sufficient for S2.
- Closure path: no material S2-specific closure path established.
- Why this is / is not agent-owned: there is no evidenced S2 function to classify for ownership.
- Evidence: [`cedar_public.py`](https://github.com/Fraunhofer-IIS/cedar/blob/ab5820b360eab75a84320f551642fe6386513bab/cedar_public.py) (`ORCH_SYSTEM`, `do_one_step`, role routing).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: the project describes multiple agents, but named specialist roles and delegation/sequencing do not by themselves establish S2.

### Absence scope

- Surfaces inspected: README architecture description; Orchestrator/Text/Code/Critique prompts and tool schemas; execution/retry loop; session/history state; Streamlit controls.
- Plausible first-party paths checked: role routing between Text/Code; shared notebook/history; Autorun sequencing; retry behavior; Critique relation.
- Why no material first-party path remains: no distinct operational units with an evidenced interaction disturbance and no first-party relation whose organizational purpose is attenuation of such inter-S1 interference.

## S3 — Inside-and-now control

- State: —
- Function: no separate superior inside-and-now control function is established above the single data-science operation.
- Disturbance / variety regulated: the Orchestrator regulates current task progress, but that regulation is part of S1's own task-local decision loop.
- Decisive decision or feedback right: none established beyond the S1 next-step choices already credited under Operations.
- Decision owner: none established for qualifying S3.
- Supporting / enforcement mechanisms: notebook history, current cells, Orchestrator decisions, retry limit and maximum-step limit are present but do not establish a separate organizational S3 owner.
- Closure path: no material S3-specific whole-system control path established at this recursion.
- Why this is / is not agent-owned: the component named `Orchestrator` chooses the next step of one operation; naming and sequencing do not convert that task-local control into a superior whole-system regulator.
- Evidence: [`cedar_public.py`](https://github.com/Fraunhofer-IIS/cedar/blob/ab5820b360eab75a84320f551642fe6386513bab/cedar_public.py) (`build_orchestrator_messages`, `do_one_step`, max-step/retry controls).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: if a future CEDAR boundary introduced multiple independently viable operational units plus a superior current resource/commitment controller, that would require reassessment rather than relabelling the current Orchestrator.

### Absence scope

- Surfaces inspected: README, role architecture, session state, Orchestrator input/output path, local execution, retries, completion handling and Critique integration.
- Plausible first-party paths checked: Orchestrator planning/routing, safety limits, model-per-role configuration, critique feedback and operator controls.
- Why no material first-party path remains: all current planning/routing decisions operate within one S1 workflow; no whole-system view plus superior current-control right over multiple operational units/resources/commitments is established.

## S3* — Complementary audit

- State: C
- Function: provide a distinct critical review of the current data-science workflow for bugs, coherence failures and concrete performance/robustness improvements, then expose those findings to the operating Orchestrator.
- Disturbance / variety regulated: unnoticed code defects, brittle APIs/shapes, data leakage or evaluation weaknesses, incoherent/redundant workflow choices and missed improvement opportunities that ordinary generation/retry may not surface.
- Decisive decision or feedback right: independently form a reviewer judgement over the run and return actionable findings distinct from ordinary code execution feedback.
- Decision owner: a dedicated Critique LLM role instantiated by the first-party Critique path; the operator supplies activation of that path.
- Supporting / enforcement mechanisms: `CRITIQUE_SYSTEM`, `CRITIQUE_TOOLS`, latest-iteration selection, expanded history rendering, optional `metrics.txt` / `model_card.txt` ingestion, `run_critique_step`, `critique_review` session state and reinjection into Orchestrator messages.
- Closure path: operator activates Critique -> Critique LLM rereads latest iteration plus available metrics/model-card evidence -> produces structured review -> runtime stores `critique_review` and appends it to the notebook -> future Orchestrator message includes the findings -> subsequent task-local decisions can change.
- Boundary reachability: the shipped Streamlit UI exposes the `Critique` button and directly calls `run_critique_step`; all review construction, storage and reinjection logic is first-party in `cedar_public.py`.
- Why this is / is not agent-owned: the review judgement is model-owned once the path is invoked, but activation is not autonomously selected/scheduled by CEDAR at the pinned boundary, so the first-party function is composable/constructor-owned rather than standalone autonomous.
- Evidence: [`cedar_public.py`](https://github.com/Fraunhofer-IIS/cedar/blob/ab5820b360eab75a84320f551642fe6386513bab/cedar_public.py) (`CRITIQUE_SYSTEM`, `build_critique_messages`, `run_critique_step`, `build_orchestrator_messages`, Critique button handler).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: only the GPT-4o Critique implementation is completed at the pinned revision; a selected Qwen Critique path is explicitly blocked. If Critique is invoked only after `finish`, the current code does not independently reopen the run, so constructor-level closure is strongest when the review is invoked before sealing or composed into a continued workflow.
- Claim being audited: whether the current data-science notebook/workflow is technically correct, coherent and robust, including bugs, leakage/brittleness, model/evaluation quality and potential metric improvements.
- Ordinary reporting path: normal S1 history contains generated text/code, stdout/stderr, tracebacks and recent-cell summaries used by the Orchestrator and Code repair loop.
- Complementary access path: Critique uses a dedicated reviewer prompt over the latest iteration with a larger review summary budget and may additionally read separate `metrics.txt` and `model_card.txt` artifacts.
- Independence boundary: Critique is a separate role/invocation with its own system prompt and tool schema, distinct from Orchestrator/Text/Code calls; however activation is operator-triggered and provider independence is not guaranteed, which is why the state is `C`, not `A`.
- Who acts on findings: the first-party runtime stores the review in `critique_review`, and `build_orchestrator_messages` injects it into later Orchestrator context so future operating choices can incorporate the findings.

## S4 — Outside-and-then intelligence

- State: —
- Function: no qualifying prospective environmental-intelligence/adaptation function is established.
- Disturbance / variety regulated: current-run context pressure, code failures and critique findings are regulated inside the ongoing operation, not through a separate future-oriented environmental sensing/adaptation function.
- Decisive decision or feedback right: none established for S4.
- Decision owner: none established.
- Supporting / enforcement mechanisms: history truncation, saved-run serialization, model selection and critique-driven suggestions do not establish S4 by themselves.
- Closure path: no material S4-specific closure path established.
- Why this is / is not agent-owned: there is no evidenced S4 function to classify for ownership.
- Evidence: [`cedar_public.py`](https://github.com/Fraunhofer-IIS/cedar/blob/ab5820b360eab75a84320f551642fe6386513bab/cedar_public.py) (`render_history_for_model`, save/load helpers, Critique path).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: improving the same current notebook after critique is current operational learning/repair, not evidence that CEDAR changes installed capabilities or strategic posture for future independent environments/runs.

### Absence scope

- Surfaces inspected: context/history management, save/load/export helpers, role prompts, Critique loop, model/provider choices and execution state.
- Plausible first-party paths checked: history compression; retry/self-correction; Critique suggestions; saved-run reload; operator model switching.
- Why no material first-party path remains: no first-party loop senses prospective environment change and autonomously selects/persists an organizational capability/posture change for future independent operation.

## S5 — Policy and identity

- State: —
- Function: no runtime authority over organizational identity, ultimate purpose or binding top-level policy is established.
- Disturbance / variety regulated: none qualifying; top-level task, general instructions, model choices and safety limits are externally configured.
- Decisive decision or feedback right: no first-party runtime actor can redefine the system's ultimate identity/purpose or settle constitutional policy conflicts.
- Decision owner: operator/configuration outside the assessed autonomous runtime.
- Supporting / enforcement mechanisms: `general.txt`, `task.txt`, model-per-role selectors, temperatures, retry/max-step settings and static role prompts constrain operation but are not runtime S5 ownership.
- Closure path: no material S5-specific closure path established.
- Why this is / is not agent-owned: policy/identity inputs are supplied by the operator and source configuration; CEDAR operates within them rather than deciding them.
- Evidence: [`README.md`](https://github.com/Fraunhofer-IIS/cedar/blob/ab5820b360eab75a84320f551642fe6386513bab/README.md); [`cedar_public.py`](https://github.com/Fraunhofer-IIS/cedar/blob/ab5820b360eab75a84320f551642fe6386513bab/cedar_public.py) (project brief loading, sidebar model/configuration controls, static system prompts).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: static prompts and human-selected configuration can strongly constrain behaviour without constituting autonomous S5 policy authority.

### Absence scope

- Surfaces inspected: project brief loading, static system prompts, sidebar configuration, completion logic, save/load state and Critique integration.
- Plausible first-party paths checked: `general.txt` / `task.txt`; role prompts; model/provider selection; max-step/retry controls; Orchestrator `finish`; Critique review.
- Why no material first-party path remains: ultimate purpose and constitutional constraints remain supplied by operator/source configuration, with no runtime actor that can authoritatively redefine and close identity/policy decisions.

## Recursion, variety and escalation

CEDAR increases the variety of one data-science S1 through role-specialized generation, persistent execution state, result/error feedback, retries and bounded history. The optional Critique path adds a constructor-level complementary audit relation. The assessment does not infer higher-level VSM functions merely from the names `Orchestrator`, `Critique` or the presence of multiple model roles.

## Standalone conclusion

`A — — C — —`

CEDAR autonomously closes its data-science operation and exposes a real but optional/composable complementary review channel. No material first-party S2, superior whole-system S3, prospective S4 or runtime S5 closure is established at the pinned boundary.
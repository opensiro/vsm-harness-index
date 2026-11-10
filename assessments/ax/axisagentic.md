---
harness_id: axisagentic
project_name: AxisAgentic
repository: https://github.com/XYZ-AI-Lab/AxisAgentic
review_ref: 0aa54b14307942edc4401831110d8e7f726ec738
reviewed_at: 2026-11-10
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# AxisAgentic

## Review boundary

- System in focus: the shipped Python AxisAgentic model/tool/trace runtime **as actually wired by its supported Web Search and WideSearch recipes**, not an imagined multi-agent deployment of generic extension interfaces.
- Purpose and identity: execute long-horizon research/search tasks with an observable model→tool→observation loop, resumeable conversation state, context controls, separate optional self-verification and reproducible trajectory capture.
- Relevant environment: changing web pages and search results, user/benchmark questions, configured model and search/scrape providers, tool failures, context limits, dataset/evaluation jobs and local run storage.
- Standard-distribution boundary: package `agentic` plus repository-shipped `recipe/web_search`, `recipe/wide_search` runners and their public YAML/config paths. Include reachable optional post-answer self-verification when enabled by the distributed default recipe; exclude post-run benchmark evaluation/dashboard from online agent ownership.
- Credited operating / distribution surfaces: [architecture and run wiring](https://github.com/XYZ-AI-Lab/AxisAgentic/blob/0aa54b14307942edc4401831110d8e7f726ec738/docs/architecture.md), [model/tool loop](https://github.com/XYZ-AI-Lab/AxisAgentic/blob/0aa54b14307942edc4401831110d8e7f726ec738/agentic/orchestration/task_orchestrator.py), [conversation state](https://github.com/XYZ-AI-Lab/AxisAgentic/blob/0aa54b14307942edc4401831110d8e7f726ec738/agentic/conversations/conversation_runtime.py), [Web Search runtime and verifier](https://github.com/XYZ-AI-Lab/AxisAgentic/blob/0aa54b14307942edc4401831110d8e7f726ec738/recipe/web_search/agent/orchestrator.py), [public recipe config](https://github.com/XYZ-AI-Lab/AxisAgentic/blob/0aa54b14307942edc4401831110d8e7f726ec738/recipe/web_search/configs/default.yaml), [runner config-to-CLI binding](https://github.com/XYZ-AI-Lab/AxisAgentic/blob/0aa54b14307942edc4401831110d8e7f726ec738/recipe/web_search/runners/run_eval_config.py).
- Adjacent first-party surfaces excluded from ownership: dataset labels, post-run `BatchEvaluator`, judge/benchmark accuracy comparisons, SFT export, Streamlit dashboard, replay tooling, developer tests and repository maintainer/CI workflows. These may corroborate data paths but do not independently supply online S2/S3/S4/S5 functions.
- First-party operating / deployment modes considered: stock configurable Python Web Search and WideSearch inference/benchmark runners; model choice via OpenAI-compatible/SGLang adapters; optional search/scrape/code-sandbox tools; enabled or disabled post-answer self-verification; fixed attempt/turn/context/retry and dataset concurrency settings.
- Recursion level: one task-level search/research agent, plus a separate verifier attempt where enabled. Concurrent dataset samples are independent runs; orchestrator-tool nesting does not by itself establish multi-S1 recursive viability.
- Reviewed revision: `0aa54b14307942edc4401831110d8e7f726ec738`, frozen by Index #3047 / #3048.
- Observation date: 2026-11-10.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The [architecture documentation](https://github.com/XYZ-AI-Lab/AxisAgentic/blob/0aa54b14307942edc4401831110d8e7f726ec738/docs/architecture.md) describes reusable `ConversationRuntime`, `TaskOrchestrator`, `ToolManager` and model clients under two first-party runnable search recipes. The task runner creates a per-task orchestrator, receives a model completion, checks structured tool calls, invokes available search/scrape/Python tools, appends real results and state markers into a persistent trace, and prompts the model again. Context compaction, rollback, discard markers, response-format recovery, retries and token/turn limits are explicit runtime support mechanisms. [Core loop](https://github.com/XYZ-AI-Lab/AxisAgentic/blob/0aa54b14307942edc4401831110d8e7f726ec738/agentic/orchestration/task_orchestrator.py), [state machine](https://github.com/XYZ-AI-Lab/AxisAgentic/blob/0aa54b14307942edc4401831110d8e7f726ec738/agentic/conversations/conversation_runtime.py), [tools](https://github.com/XYZ-AI-Lab/AxisAgentic/blob/0aa54b14307942edc4401831110d8e7f726ec738/agentic/tools/manager.py).

The Web Search recipe additionally ships opt-in post-answer self-verification: an **auxiliary attempt with its own task ID and dedicated verification system prompt**, access to configured research tools, structured correct/incorrect verdict, trace, and a returned decision that either accepts the response or runs a fresh re-answer followed by further checking. This is reached through runner configuration and is explicitly `enabled: true` in the shipped Web Search default YAML; the generic `SelfVerificationConfig` class defaults false without recipe override. Verifier and re-answer normally reuse the same underlying model service, which limits model independence but does not collapse their separate task contexts. [Verification flow](https://github.com/XYZ-AI-Lab/AxisAgentic/blob/0aa54b14307942edc4401831110d8e7f726ec738/recipe/web_search/agent/orchestrator.py), [recipe default](https://github.com/XYZ-AI-Lab/AxisAgentic/blob/0aa54b14307942edc4401831110d8e7f726ec738/recipe/web_search/configs/default.yaml), [CLI config binding](https://github.com/XYZ-AI-Lab/AxisAgentic/blob/0aa54b14307942edc4401831110d8e7f726ec738/recipe/web_search/runners/run_eval_config.py).

Separate `BatchEvaluator`/verifier contracts compare completed runs with labels and write scores/traces for scientific research. They are not credited as the live S3* feedback owner merely because evaluation is first-party. [Post-run evaluation](https://github.com/XYZ-AI-Lab/AxisAgentic/blob/0aa54b14307942edc4401831110d8e7f726ec738/agentic/evaluation/evaluator.py).

## Operational model

- Outcome: researched answer/tool-derived artifact for each assigned query, with self-verification re-answer when enabled; per-run trace and post-run scores are secondary observations.
- S1 units: the model-backed `TaskOrchestrator.run` loop per question; self-verification is a separate audit attempt for that completed claim, not another independent production department or automatic recursive S1.
- Rights split: model decides tool use and answer; Python state machine enforces fixed phase, turn, context and retry rules; optional verifier model owns a separate claim judgment; user/developer sets provider, tools, concurrency and evaluation config. Dataset scheduler and benchmark evaluator do not exercise whole-system ongoing current-control discretion.

## S1 — Operations

- State: A
- Function: an agentic search/research operation transforms a user question and changing web/tool observations into an answer.
- Disturbance / variety regulated: missing or inconsistent online evidence, tool errors, large contexts, unexpected search responses and evolving draft answers.
- Decisive decision or feedback right: select the next research tool call, read observations, revise the query/answer and decide a final response within configured limits.
- Decision owner: configured model-backed task agent operating through `TaskOrchestrator` and `ConversationRuntime`. The deterministic runtime limits but does not choose the research plan/content.
- Supporting / enforcement mechanisms: typed message states, tool validation and dispatch, remote client, context compaction/rollback, retry caps and append-only trace.
- Closure path: recipe task → model completion → structured search/scrape/code tool action → result returned to model-visible conversation → subsequent model decision or final answer. Optional failure handling can launch another bounded attempt.
- Boundary reachability: shipped [run configuration](https://github.com/XYZ-AI-Lab/AxisAgentic/blob/0aa54b14307942edc4401831110d8e7f726ec738/recipe/web_search/runners/run_eval_config.py) invokes [the concrete recipe orchestrator](https://github.com/XYZ-AI-Lab/AxisAgentic/blob/0aa54b14307942edc4401831110d8e7f726ec738/recipe/web_search/agent/orchestrator.py) derived from the [model/tool runtime](https://github.com/XYZ-AI-Lab/AxisAgentic/blob/0aa54b14307942edc4401831110d8e7f726ec738/agentic/orchestration/task_orchestrator.py); it is not just an abstract SDK base class.
- Why this is / is not agent-owned: removing model discretion leaves fixed scheduling and tool/trace infrastructure but no choice of research questions/tools or answer. A provider is externally hosted; the first-party runtime nevertheless wires the executable model-to-tool feedback loop.
- Evidence: [runtime loop](https://github.com/XYZ-AI-Lab/AxisAgentic/blob/0aa54b14307942edc4401831110d8e7f726ec738/agentic/orchestration/task_orchestrator.py), [conversation stage](https://github.com/XYZ-AI-Lab/AxisAgentic/blob/0aa54b14307942edc4401831110d8e7f726ec738/agentic/conversations/conversation_runtime.py), [tool manager](https://github.com/XYZ-AI-Lab/AxisAgentic/blob/0aa54b14307942edc4401831110d8e7f726ec738/agentic/tools/manager.py).
- Basis: structural.
- Confidence: high for shipped agent-choice/feedback wiring; no real provider execution independently replicated.
- Caveats: accuracy, successful external search credentials and longitudinal operational viability are not validated by static review.

## S2 — Coordination

- State: —
- Function: no evidenced first-party inter-S1 conflict/oscillation attenuation with a returned coordination decision at the chosen task/recipe recursion.
- Disturbance / variety regulated: concurrently evaluated dataset tasks and nested tool calls may share compute or provider budgets, but they are independent evaluation jobs rather than interacting operational work cells in a sourced conflict-control loop.
- Decisive decision or feedback right: no identified coordination-specific discretion over clashes among distinct autonomous task S1 units.
- Decision owner: developer-configured dataset concurrency and deterministic retry/tool execution; model agent decides only its own task/tool calls.
- Supporting / enforcement mechanisms: `BatchEvaluator.max_concurrent`, task IDs, tool manager, nested `OrchestratorTool` and fixed attempt budgets.
- Closure path: separate task results are logged and evaluated; no conflict signal from one S1 changes subsequent coordination behaviour of another S1.
- Why this is / is not agent-owned: an orchestrator name, concurrent sample scheduler and ability to nest an agent as a tool do not prove a concrete inter-S1 disturbance/attenuation/feedback relation.
- Evidence: [task orchestration](https://github.com/XYZ-AI-Lab/AxisAgentic/blob/0aa54b14307942edc4401831110d8e7f726ec738/agentic/orchestration/task_orchestrator.py), [nested orchestrator tool](https://github.com/XYZ-AI-Lab/AxisAgentic/blob/0aa54b14307942edc4401831110d8e7f726ec738/agentic/orchestration/orchestrator_tool.py), [dataset evaluator](https://github.com/XYZ-AI-Lab/AxisAgentic/blob/0aa54b14307942edc4401831110d8e7f726ec738/agentic/evaluation/evaluator.py).
- Basis: structural.
- Confidence: medium-high within the shipped recipes.
- Caveats: a downstream user could implement genuine multi-agent coordination with these primitives, but it is not credited without the first-party path.

### Absence scope

- Surfaces inspected: core orchestrator/tool contracts, nested orchestrator wrapper, recipe runners/configuration, task logger and batch evaluation scheduler.
- Plausible first-party paths checked: concurrent task budgets, independent dataset jobs, nested orchestrator tool calls, retry/rollback and shared log/trace storage.
- Why no material first-party path remains: no concrete conflicting S1 work decisions, coordination-specific response, and feedback to the interacting S1 units is implemented; existing paths schedule or encapsulate tasks.

## S3 — Inside-and-now control

- State: —
- Function: no agent- or parent-owned whole-system current supervisory discretion over a portfolio of S1 resource/commitment choices is established.
- Disturbance / variety regulated: per-query failure/turn/context limits and batch completion are regulated with fixed configuration, not negotiated whole-current operational commitments.
- Decisive decision or feedback right: no first-party supervisor selecting/revising current shared priorities, resources, accountability or interventions using a whole-operating-system view.
- Decision owner: human/developer run parameters and deterministic orchestrator/batch scheduler; each agent controls only its local research task.
- Supporting / enforcement mechanisms: model retry/backoff, timeout/turn/tool budgets, batch evaluator concurrency, benchmark dashboard and execution traces.
- Closure path: local retry/budget responses remain within one S1 or evaluation job; no whole-current discretionary supervisory intervention feeds back into running S1 cells.
- Why this is / is not agent-owned: hard budget enforcement and named orchestration do not own an S3 decision; no supported S3=P human decision-return mode is documented in the first-party recipe.
- Evidence: [runtime state](https://github.com/XYZ-AI-Lab/AxisAgentic/blob/0aa54b14307942edc4401831110d8e7f726ec738/agentic/conversations/conversation_runtime.py), [orchestrator](https://github.com/XYZ-AI-Lab/AxisAgentic/blob/0aa54b14307942edc4401831110d8e7f726ec738/agentic/orchestration/task_orchestrator.py), [batch evaluator](https://github.com/XYZ-AI-Lab/AxisAgentic/blob/0aa54b14307942edc4401831110d8e7f726ec738/agentic/evaluation/evaluator.py).
- Basis: structural.
- Confidence: medium-high in shipped modes.
- Caveats: separate human-run experiment governance is not an operationally closed parent S3 mode of the assessed runtime.

### Absence scope

- Surfaces inspected: core task state, model budget/retry controls, recipe entry points, concurrent evaluation scheduling, trace and dashboard surfaces.
- Plausible first-party paths checked: `max_concurrent`, context limits, attempt retries, evaluator summaries, runtime stop/rollback and manual YAML configuration.
- Why no material first-party path remains: those mechanisms enforce prechosen constraints or report individual outcomes; no source-wired whole-current discretionary authority and return to multiple ongoing S1 commitments is shown.

## S3* — Complementary audit

- State: A
- Function: in the supported post-answer self-verification mode, an auxiliary model-backed verifier independently re-investigates the source question and challenges a candidate production answer.
- Disturbance / variety regulated: apparently plausible but unsupported/inaccurate research answers can survive ordinary production summaries and tool-use logs.
- Claim being audited: the producing research agent's boxed/final answer to the original web-search question.
- Ordinary reporting path: main `WebSearchTaskOrchestrator` returns its answer and writes model/tool trace; routine retry/format checks do not independently establish answer correctness.
- Complementary access path: a separate auxiliary task ID and verification system prompt requests condition-by-condition fact checking with structured web-search tools; the verifier can collect its own observations instead of accepting only the author's written rationale.
- Independence boundary: a new verifier conversation/task context and different verification objective/trace are established by `_run_self_verification_auxiliary_attempt`; its model endpoint and tool implementations may be shared, so this is task-context/evidence-search independence, **not** provider/model independence or a claim of adversarial human audit.
- Who acts on findings: `_maybe_apply_self_verification` uses the verifier's correct/incorrect verdict to accept the answer or start a separate re-answer attempt; subsequent verdicts can change the returned result. Deterministic verdict parsing/attempt caps enforce the agent's judgment, not independently own it.
- Decisive decision or feedback right: judge candidate answer against fresh research evidence as correct/incorrect; on rejection, cause re-answer rather than blindly return the original conclusion.
- Decision owner: separate model-backed verifier operating within the first-party Web Search recipe, subject to static attempt/format limits.
- Supporting / enforcement mechanisms: dedicated verification prompt/schema, auxiliary trace IDs, web tool manager, verdict parsing/resampling, bounded re-answer, exported trace metadata.
- Closure path: original answer → auxiliary independent verification task with tools → model verdict → branch to acceptance or fresh re-answer → verified/revised result returned as the final task output and trace metadata.
- Boundary reachability: the distributed [Web Search default YAML](https://github.com/XYZ-AI-Lab/AxisAgentic/blob/0aa54b14307942edc4401831110d8e7f726ec738/recipe/web_search/configs/default.yaml) sets `self_verification.enabled: true`; [config runner](https://github.com/XYZ-AI-Lab/AxisAgentic/blob/0aa54b14307942edc4401831110d8e7f726ec738/recipe/web_search/runners/run_eval_config.py) passes this flag to [benchmark runtime](https://github.com/XYZ-AI-Lab/AxisAgentic/blob/0aa54b14307942edc4401831110d8e7f726ec738/recipe/web_search/runners/evaluate_benchmark.py) that constructs [the dedicated verifier path](https://github.com/XYZ-AI-Lab/AxisAgentic/blob/0aa54b14307942edc4401831110d8e7f726ec738/recipe/web_search/agent/orchestrator.py). Generic class default `False` is explicitly overridden by this first-party recipe.
- Why this is / is not agent-owned: the verification model evaluates the original answer using its own research session; fixed verdict parser and retry budget merely enforce its chosen judgment. This differs materially from post-run benchmark scoring or routine answer-format checking.
- Evidence: [self-verification prompt, separate auxiliary tool run, verdict and re-answer](https://github.com/XYZ-AI-Lab/AxisAgentic/blob/0aa54b14307942edc4401831110d8e7f726ec738/recipe/web_search/agent/orchestrator.py), [enabled recipe config](https://github.com/XYZ-AI-Lab/AxisAgentic/blob/0aa54b14307942edc4401831110d8e7f726ec738/recipe/web_search/configs/default.yaml), [CLI/runner wiring](https://github.com/XYZ-AI-Lab/AxisAgentic/blob/0aa54b14307942edc4401831110d8e7f726ec738/recipe/web_search/runners/run_eval_config.py).
- Basis: structural.
- Confidence: medium-high for a shipped separate context/tool-verification return path; actual independence strength and accuracy require empirical testing.
- Caveats: verifier uses the candidate model; correlated model/search bias remains possible. The `SelfVerificationConfig` generic default is disabled and users can turn off the shipped recipe option; S3* is not claimed for every use of the reusable core library.

## S4 — Outside-and-then intelligence

- State: —
- Function: no supported first-party prospective environmental assessment that selects a reusable future capability adaptation and returns it to current task operation.
- Disturbance / variety regulated: changing live web results are immediate research evidence, while trajectory export and evaluation can inform developer research outside the runtime.
- Decisive decision or feedback right: no source-wired runtime actor turns external/future changes into selected and deployed lasting changes to the agent's own operating repertoire.
- Decision owner: developer/operator choices for model, recipes, tools, prompts and experiment setup; agents search to answer current questions.
- Supporting / enforcement mechanisms: search tools, context compress/discard, retries, trace/SFT export, evaluator and benchmark dashboard.
- Closure path: web evidence changes an answer within S1 or an S3* verdict, not durable runtime future capability; post-run data exports are external research outputs.
- Why this is / is not agent-owned: search is outward-looking but task-immediate; trace learning/export is not a closed adaptation decision and implementation loop.
- Evidence: [architecture split](https://github.com/XYZ-AI-Lab/AxisAgentic/blob/0aa54b14307942edc4401831110d8e7f726ec738/docs/architecture.md), [search recipe](https://github.com/XYZ-AI-Lab/AxisAgentic/blob/0aa54b14307942edc4401831110d8e7f726ec738/recipe/web_search/agent/orchestrator.py), [SFT export](https://github.com/XYZ-AI-Lab/AxisAgentic/blob/0aa54b14307942edc4401831110d8e7f726ec738/agentic/sft_export/swift_agent.py).
- Basis: structural.
- Confidence: medium-high at the shipped task-agent boundary.
- Caveats: externally retraining a model on saved traces is possible but not credited as autonomous S4 here.

### Absence scope

- Surfaces inspected: running research loops, search tools, retry/compaction, evaluations, output traces and SFT export.
- Plausible first-party paths checked: future web info in query answers, model/tool selection, trace-driven training artifacts, failure summaries and reusable knowledge.
- Why no material first-party path remains: no end-to-end external-and-prospective option-selection and deployment return into present agent capability is shipped; observed feedback remains task solving or external experiment data.

## S5 — Policy and identity

- State: —
- Function: no first-party ultimate identity/policy authority with a governing decision-return loop at task-agent recursion.
- Disturbance / variety regulated: tool permissions, system prompts, benchmark constraints and token/turn budgets are preset execution boundaries, not constitutional disputes adjudicated in a runtime policy forum.
- Decisive decision or feedback right: no evidenced agent or legitimate runtime parent accepting an identity-level issue and deciding an authoritative durable policy that governs subsequent operations.
- Decision owner: external user/developer for YAML prompts, credential/tool/endpoint choices and benchmark/task policies.
- Supporting / enforcement mechanisms: prompt templates, strict configuration schemas, tool managers, context/turn limits, sandbox restrictions and run stop rules.
- Closure path: tool outputs and verifier judgments influence present answers, not ultimate identity/policy; no corresponding authority-return path for S5.
- Why this is / is not agent-owned: a static system prompt or nested orchestrator is not a policy-organizational owner; external experiment governance is outside the first-party task agent.
- Evidence: [config schema](https://github.com/XYZ-AI-Lab/AxisAgentic/blob/0aa54b14307942edc4401831110d8e7f726ec738/agentic/config/models.py), [runtime state limits](https://github.com/XYZ-AI-Lab/AxisAgentic/blob/0aa54b14307942edc4401831110d8e7f726ec738/agentic/conversations/conversation_runtime.py), [tool manager](https://github.com/XYZ-AI-Lab/AxisAgentic/blob/0aa54b14307942edc4401831110d8e7f726ec738/agentic/tools/manager.py).
- Basis: structural.
- Confidence: medium-high within the shipped core/recipe paths.
- Caveats: repository maintainers, benchmark owners and model providers can set external policy, but they are not granted a closed S5=P path by the runtime.

### Absence scope

- Surfaces inspected: runner/YAML/CLI configuration, model/tool contracts, prompts, context/retry logic, self-verification and evaluation paths.
- Plausible first-party paths checked: system prompt updates, tool permission settings, operator model choice, verifier final answer selection, dataset evaluation and OSS governance.
- Why no material first-party path remains: these are predefined constraints, task-output judgments or adjacent human processes, not a sourced identity-level issue → authority → returned authoritative policy path.

## Recursion

The parent task agent has a locally meaningful research operating environment. The auxiliary verifier is a separate task context with its own evidence-seeking behavior, but it is an audit subroutine rather than an independently viable S1 organization. `OrchestratorTool` can nest another orchestrator but nesting is an extension mechanism; it does not establish a recursively complete viable organization or a distinct inter-S1 coordination loop without a concrete disturbance and return path.

## Variety and escalation

Search/scrape and model/tool outcomes deliver current-world distinctions directly to S1, while context compression and retries attenuate input variety under budget. The optional independent-answer-verification pass adds a different evidence-search path and may trigger re-answer; reused model/provider introduces correlated failure risk. Task failures/limits exit through fixed stops or benchmark records; an error/status file is not automatically an exceptional algedonic governance channel. Configuration changes and sustained external environment adaptation remain the developer/operator's responsibility.

## Evidence gaps

- Static source review at the frozen SHA; no model endpoint, search/scrape provider, benchmark or live verification round was executed. Empirical answer accuracy and verifier independence strength remain unproven.
- S3*=A is bounded to the first-party Web Search recipe with self-verification enabled by its distributed default; the generic core library has a false default and other downstream recipes can disable or omit the mechanism.
- Separate verifier task context/source investigation is supported, but it uses the same underlying model and tool implementations. The assessment does not claim different-provider, human or adversarial model independence.
- Other user-created orchestrator compositions are extensibility, not evidence that shipped S2/S3/S4/S5 functions exist.

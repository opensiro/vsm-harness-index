---
harness_id: restgpt
project_name: RestGPT
repository: https://github.com/Yifan-Song793/RestGPT
review_ref: d99012860cb45323975bf5780152d7aa44f390f5
reviewed_at: 2026-10-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# RestGPT

## Review boundary

- System in focus: one locally launched RestGPT agent session against one selected TMDB or Spotify REST API specification, from a human query to task completion.
- Purpose and identity: autonomous translation of a user instruction into successive REST calls and a final natural-language answer or requested API-side effect.
- Relevant environment: user requests, remote service API descriptions and responses, authenticated REST endpoints, model provider output, runtime and external application errors.
- Standard-distribution boundary: the first-party `run.py` entry point and `model/` Planner, APISelector, Caller and ResponseParser code, constrained by the bundled TMDB/Spotify OpenAPI specifications.
- Credited operating / distribution surfaces: `run.py`, `model/rest_gpt.py`, `model/planner.py`, `model/api_selector.py`, `model/caller.py`, `model/parser.py`, `utils/oas_utils.py`, and shipped API specs used by the normal runner.
- Adjacent first-party surfaces excluded from ownership: `datasets/` RestBench gold paths and `run_tmdb.py`/`run_spotify.py` evaluation scripts; repository/paper authorship and maintenance; `init_spotify.py` destructive fixture preparation; third-party model-provider, LangChain, Spotify and TMDB internals. No benchmark or initialization script was run.
- First-party operating / deployment modes considered: interactive TMDB and Spotify sessions, default LLM-based response parser, optional simple response parser, and bounded iterative planning/calling. No custom controller or evaluator was composed.
- Recursion level: one RestGPT user-task session; Planner, APISelector and Caller are consecutive specialized roles within one operational S1, not independent S1 units merely because each is a chain.
- Reviewed revision: `Yifan-Song793/RestGPT@d99012860cb45323975bf5780152d7aa44f390f5` (frozen Index batch #2393, row 5/5).
- Observation date: 2026-10-30.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

Primary source is the [immutable reviewed tree](https://github.com/Yifan-Song793/RestGPT/tree/d99012860cb45323975bf5780152d7aa44f390f5). This is first-party source inspection only; no live model, OAuth, paid service or external API was exercised.

## Repository architecture

The [README](https://github.com/Yifan-Song793/RestGPT/blob/d99012860cb45323975bf5780152d7aa44f390f5/README.md) describes coarse-to-fine planning over REST APIs. The [interactive runner](https://github.com/Yifan-Song793/RestGPT/blob/d99012860cb45323975bf5780152d7aa44f390f5/run.py#L18-L80) loads credentials and OpenAPI spec, asks a human to select TMDB or Spotify, then supplies the chosen query to the `RestGPT` chain. The [chain](https://github.com/Yifan-Song793/RestGPT/blob/d99012860cb45323975bf5780152d7aa44f390f5/model/rest_gpt.py#L131-L188) produces a model-authored plan, routes to a model-authored API plan, invokes a caller, records the API result in planner history and generates the next plan or final answer. Iteration/time ceilings terminate the loop; they are deterministic guards, not a separate whole-system controller.

The [API selector](https://github.com/Yifan-Song793/RestGPT/blob/d99012860cb45323975bf5780152d7aa44f390f5/model/api_selector.py#L170-L195) retries unrecognized endpoint names against the listed OpenAPI endpoints. The [caller](https://github.com/Yifan-Song793/RestGPT/blob/d99012860cb45323975bf5780152d7aa44f390f5/model/caller.py#L197-L241) translates model-selected actions into authenticated GET/POST/PUT/DELETE requests. The [response parser](https://github.com/Yifan-Song793/RestGPT/blob/d99012860cb45323975bf5780152d7aa44f390f5/model/parser.py#L286-L328) may generate and execute Python code to extract response facts or fall back to model summary. This is an operational risk and a source of local retry, not independent S3* assurance. No persistent organization-wide agent-task board, cross-agent coordination, strategy adaptation or policy-governance loop is shipped.

## Operational model

A human selects a service and gives one instruction. The autonomous model chooses current plan steps and endpoint actions within the selected API spec; returned data can change the next plan and the decision to terminate. `RestGPT._call` owns execution sequencing and context transport. The model owns the operative choice of next steps; external API services own what the calls actually do. The human owns startup credentials, chosen scenario and the user request, but the source does not establish a distinct ongoing S3 or ultimate-policy S5 decision-and-return path.

## S1 — Operations

- State: A
- Function: model-directed fulfillment of a user request by choosing, invoking and revising REST API operations.
- Disturbance / variety regulated: task ambiguity, endpoint availability, API response content, partial progress and mismatch between the intermediate result and the user's requested outcome.
- Decisive decision or feedback right: choose the next natural-language plan, specific API endpoint/action/arguments and whether to continue or answer.
- Decision owner: the LLM-based Planner, APISelector and Caller acting through the first-party session loop; the Python loop and API wrappers enforce or carry their choices.
- Supporting / enforcement mechanisms: OpenAPI endpoint descriptions, LangChain LLMChain/requests, OAuth or bearer credentials, response parser, history scratchpad and iteration limits.
- Closure path: human query → model plan → selected API call → response and parsed facts → planner history → model continuation/revision or final answer.
- Boundary reachability: `run.py` instantiates `RestGPT` with the model and selected spec and calls `rest_gpt.run(query)`; `_call` invokes Planner, APISelector and Caller in the released interactive mode, not solely in a benchmark.
- Why this is / is not agent-owned: model output selects and revises the operative task/API decisions; source-defined sequencing and API validation do not substitute their own discretionary plan.
- Evidence: [runner](https://github.com/Yifan-Song793/RestGPT/blob/d99012860cb45323975bf5780152d7aa44f390f5/run.py#L32-L76), [agent loop](https://github.com/Yifan-Song793/RestGPT/blob/d99012860cb45323975bf5780152d7aa44f390f5/model/rest_gpt.py#L143-L188), [planner feedback](https://github.com/Yifan-Song793/RestGPT/blob/d99012860cb45323975bf5780152d7aa44f390f5/model/planner.py#L126-L153), [caller](https://github.com/Yifan-Song793/RestGPT/blob/d99012860cb45323975bf5780152d7aa44f390f5/model/caller.py#L280-L332).
- Basis: shipped autonomous session, not the paper's or README's agent label alone.
- Confidence: high for code-path existence; effectiveness and safety untested.
- Caveats: supported domains are TMDB/Spotify only; external model/API credentials and service access are required. The parser's Python `exec` is not sandboxed by the displayed code; this assessment is not an assurance of safe execution.

## S2 — Coordination

- State: —
- Function: no distinct first-party regulation of interference between separate operational S1 units at the assessed session recursion.
- Disturbance / variety regulated: potential conflict among API calls or independently launched sessions is not accompanied by a shipped inter-S1 stabilization loop.
- Decisive decision or feedback right: no inter-S1 arbitration or coordination discretion is established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: Planner → APISelector → Caller sequencing and shared history within one task.
- Closure path: results return to the same operational agent, not to distinct S1 units through an attenuation relation.
- Why this is / is not agent-owned: specialized LLM components are roles of one agent session; their sequential messages are not proof of competing S1 work cells.
- Evidence: [single task loop](https://github.com/Yifan-Song793/RestGPT/blob/d99012860cb45323975bf5780152d7aa44f390f5/model/rest_gpt.py#L131-L188), [runner](https://github.com/Yifan-Song793/RestGPT/blob/d99012860cb45323975bf5780152d7aa44f390f5/run.py#L64-L76).
- Basis: bounded negative within standard distribution.
- Confidence: high.
- Caveats: independent users could run separate processes, but the reviewed repository does not coordinate such sessions.

### Absence scope

- Surfaces inspected: interactive runner, Planner, APISelector, Caller, response parser, benchmark runners and README architecture.
- Plausible first-party paths checked: multiple active S1 cells, concurrent sessions, shared resource conflict arbitration, API request overlap reduction and returned behavior changes across distinct units.
- Why no material first-party path remains: the only internal handoffs belong to one sequential task and no shared cross-session S1 relationship with conflict-specific attenuation and return is supplied.

## S3 — Inside-and-now control

- State: —
- Function: no distinct whole-session/current-operation control authority with a separate cross-S1 commitment or resource regulation loop.
- Disturbance / variety regulated: excess iterations, wrong endpoint or failed API actions are handled as local S1 guard/retry and planning feedback.
- Decisive decision or feedback right: no whole-system allocation or intervention choice apart from task planning and fixed limits.
- Decision owner: not established for S3.
- Supporting / enforcement mechanisms: fixed maximum iterations/time, validator retry on unknown endpoint, chronological planner history and operator startup selection.
- Closure path: bounded local task retries exist; no separate S3 current-control verdict changes resource/priority commitments of an operational whole.
- Why this is / is not agent-owned: model correction of its own task plan is S1 feedback; deterministic step ceilings do not own organizational resource decisions.
- Evidence: [iteration limits](https://github.com/Yifan-Song793/RestGPT/blob/d99012860cb45323975bf5780152d7aa44f390f5/model/rest_gpt.py#L33-L35), [guard and loop](https://github.com/Yifan-Song793/RestGPT/blob/d99012860cb45323975bf5780152d7aa44f390f5/model/rest_gpt.py#L96-L105), [selector retry](https://github.com/Yifan-Song793/RestGPT/blob/d99012860cb45323975bf5780152d7aa44f390f5/model/api_selector.py#L188-L195).
- Basis: scoped no-material-path conclusion for whole-system S3, despite operational guards.
- Confidence: moderate-high.
- Caveats: an application embedding this chain could supply S3 externally; it is not shipped here.

### Absence scope

- Surfaces inspected: RestGPT loop/limit fields, Planner history, selector retries, caller actions, interactive startup configuration and benchmark scripts.
- Plausible first-party paths checked: fleet/task current view, resource/priority arbitration, policy intervention by an autonomous governor, supported parent supervisory return and exception escalation.
- Why no material first-party path remains: state is local to one query and constraints are preselected or mechanical; no function-specific whole-system controller, legitimate parent S3 decision or returned allocation exists in the shipped mode.

## S3* — Complementary audit

- State: —
- Function: no separate, independently controlled inspection of ordinary RestGPT action/result claims.
- Disturbance / variety regulated: omitted API outcomes, unsupported claims or faulty parse results could require independent source checks, but none is wired as organizational complementary audit.
- Decisive decision or feedback right: no independent audit verdict or accepted corrective decision is established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: response parsing, exception handling, logging and benchmark gold solution paths.
- Closure path: parser summaries return through ordinary execution, not a complementary evidence channel to S3.
- Why this is / is not agent-owned: the same model-driven operational pipeline interprets responses; test datasets are adjacent evaluation material, not a separately operating auditor.
- Evidence: [response parser](https://github.com/Yifan-Song793/RestGPT/blob/d99012860cb45323975bf5780152d7aa44f390f5/model/parser.py#L286-L328), [benchmarks described in README](https://github.com/Yifan-Song793/RestGPT/blob/d99012860cb45323975bf5780152d7aa44f390f5/README.md).
- Basis: absence of independent complementary access-and-return path.
- Confidence: high.
- Caveats: none of the reviewed source proves an independent audit performed on live runs.

### Absence scope

- Surfaces inspected: parser, caller and planner feedback, logs, datasets/ and benchmark runners, README.
- Plausible first-party paths checked: independent API observation, audit sampling, benchmark examiner participating in live governance and a separate corrective verdict returned to control.
- Why no material first-party path remains: operational response interpretation and offline benchmark evaluation share no separately independent, decision-owning audit loop with subsequent organizational control.

## S4 — Outside-and-then intelligence

- State: —
- Function: no future-oriented environmental sensing, adaptation-option selection and return into RestGPT's standing capability.
- Disturbance / variety regulated: external API evolution, new supported domains and future model limitations have no shipped prospective adaptation regulator.
- Decisive decision or feedback right: no S4 capability-change option decision in the operating session.
- Decision owner: none established.
- Supporting / enforcement mechanisms: fixed bundled service specs, current query planner and research/benchmark documentation.
- Closure path: task-level new facts alter the immediate API plan only, not durable future capability or present S3 policy.
- Why this is / is not agent-owned: online planning adapts to a current task (S1); it does not maintain a future environment model or choose capability adaptations.
- Evidence: [runner's fixed domain selection](https://github.com/Yifan-Song793/RestGPT/blob/d99012860cb45323975bf5780152d7aa44f390f5/run.py#L32-L62), [per-query planning](https://github.com/Yifan-Song793/RestGPT/blob/d99012860cb45323975bf5780152d7aa44f390f5/model/rest_gpt.py#L138-L188).
- Basis: bounded negative under supplied first-party runtime.
- Confidence: high.
- Caveats: maintainers can improve source and API specs outside this runtime; that development is not credited as its S4.

### Absence scope

- Surfaces inspected: runner, specs/, runtime modules, README roadmap and benchmark corpus.
- Plausible first-party paths checked: recurring future-facing external analysis, option generation beyond immediate task, adaptation authority and feedback that changes standing agent capability.
- Why no material first-party path remains: the normal execution starts from a fixed spec and terminates with a task result; no prospective sensing/options/return-to-capability circuit is shipped.

## S5 — Policy and identity

- State: —
- Function: no first-party ultimate-policy or organizational identity adjudication-and-return mechanism at this task-session recursion.
- Disturbance / variety regulated: competing claims about agent purpose, legitimate risk envelope and policy boundaries are not dynamically resolved by the program.
- Decisive decision or feedback right: no S5 identity/ultimate-policy decision path beyond static application design and startup parameters.
- Decision owner: not established in the harness; humans choose the API scenario, supply credentials and state task instructions, but these alone are not a distinct S5 parent-governed circuit.
- Supporting / enforcement mechanisms: fixed TMDB/Spotify scenario branches, static OpenAPI specs, supplied OAuth/bearer tokens and a user query.
- Closure path: startup configuration controls which service is called, but no policy issue → legitimate authority decision → authoritative resolution → returned governance of subsequent activity is implemented.
- Why this is / is not agent-owned: choosing credentials and launching a task is parent input and access setup, not evidence of a first-party, operationally closed identity-governance function.
- Evidence: [entry-point config and scenario selection](https://github.com/Yifan-Song793/RestGPT/blob/d99012860cb45323975bf5780152d7aa44f390f5/run.py#L18-L76), [fixed scenario check](https://github.com/Yifan-Song793/RestGPT/blob/d99012860cb45323975bf5780152d7aa44f390f5/model/rest_gpt.py#L49-L61).
- Basis: functional/parent-mode threshold, not inferred from mere human ownership of setup.
- Confidence: moderate-high.
- Caveats: a surrounding institution may own policy in a deployment; such external governance is outside the first-party session.

### Absence scope

- Surfaces inspected: `config.yaml`, interactive runner, domain-specific specs, RestGPT initialization, task loop and CLI scripts.
- Plausible first-party paths checked: autonomous identity/policy board, human policy proposal/ratification path, persistent authoritative rule updates and their return to subsequent task operation.
- Why no material first-party path remains: the source exposes static scenario choice and user-task instructions, without a policy-level dispute/decision/return path; no constructed or parent S5 ownership mode is evidenced.

## Distributed OSS parent arrangement

Public contributors do not share a first-party runtime governance plane for separately installed RestGPT sessions. Project maintainers may update code externally, but their GitHub activity is outside this session's first-party S3/S4/S5 operating boundary.

## Self-hosted and non-human modes

The released app is a local process with external LLM/API providers and interactive credential/scenario selection. It supports an autonomous S1 despite parent startup configuration. No supported autonomous or parent-governed metasystem decision path is documented for S3/S4/S5 at this level; unsupported custom embeddings are not credited.

## Recursion

The single session is an S1 in the user's larger real-world context. Its internal specialized chains form a task pipeline, not automatically viable sub-organizations. Remote REST services and API accounts are environment or operator dependencies, not first-party members of a higher recursive RestGPT organization.

## Variety and escalation

The model's iterative plan–call–observe–revise path absorbs request/API variety locally; invalid endpoints can be reselected and model continuation follows parsed results. Maximum iterations bounds the local execution. There is no distinct escalation to current-control policy, independent complementary audit or prospective change governance. Unsafe dynamic code execution within response parsing is a caveat, not evidence of VSM control or assurance.

## Evidence gaps

- Assessment is source-only at the frozen revision; no LLM, Spotify/TMDB request, destructive environment initialization or benchmark task executed. Outcome quality, external provider availability, and parser isolation were not independently tested.
- No positive S2/S3/S3*/S4/S5 conclusion was inferred from module names, prompt chains, service credentials, log output or evaluation fixtures. Negative claims are limited to the inspected shipped modes.
- No separate S3* organizational audit, external human evaluator, autonomy grade, or security certification was commissioned by this Index batch.

---
harness_id: jevagentharness
project_name: JevAgentHarness
repository: https://github.com/JevAgentHarness/JevAgentHarness
review_ref: f2932199e1ef1d9f089b51d39430c87be0f560b5
reviewed_at: 2026-10-28
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: excluded-no-agentic-vsm
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# JevAgentHarness

## Review boundary

- System in focus: one installed first-party `jevagentharness` (`jah`) OpenAI-compatible **model-decision proxy**, taking requests from an existing coding/other agent and delivering model responses. The external calling agent's runtime, tools, task objective and feedback loop are not silently incorporated.
- Purpose and identity: reduce the cost of external agent model calls and optionally provide decision-model advice, shortlist/force a tool, repeat a questionable model step with a strong tier, or log decision-point observations.
- Relevant environment: HTTP requests containing the external agent's transcript/tool schemas; selected Jev/other decision backend; fast/strong upstream model APIs; pricing/cost logs and operator thresholds; the external client that interprets responses and actually executes tools.
- Standard-distribution boundary: `src/jevagentharness/server.py` one-request proxy, `router.py` per-step routing and session tier state, `points.py` decision questions/modes, `decision.py` typed decision backend, upstream adapters, CLI, config and logs/reports/fitting utility.
- Credited operating / distribution surfaces: default `route` preset (routing cascade plus strong-model finish check), selectable `paper` tool-select cascade, `safe` action guard, `shadow` logging, `off`/guard modes, OpenAI chat/Responses and Gemini upstream dialects. Assessment includes the strongest standard optional mode, not just the default router.
- Adjacent first-party surfaces excluded from ownership: `bench/`, `research/`, paper PDF and evaluation agent adapters represent reproducibility/training/benchmarks rather than the installed runtime's own task-agent loop. Any cited benchmark harness executes outside the proxy. External Codex, pi, DeepSeek Harness, mini-swe-agent, Terminus, upstream LLMs and model-provider/decision services remain separately owned.
- First-party operating / deployment modes considered: default price/quality routing; explicit `tool_select: cascade/assist/guard`, stop/reflection/action guards and shadows; retry/error fallbacks; session key/history parsing and `jah fit`. No first-party mode actually runs a coding agent's task lifecycle, executes its tools, or owns task state independent of the caller.
- Recursion level: the proxy is an auxiliary model-selection and validation service *within or adjacent to* an external agent S1, not a nested viable agent organization. The external agent's S1 may benefit from the proxy but is not a first-party JevAgentHarness operating cell.
- Reviewed revision: `JevAgentHarness/JevAgentHarness@f2932199e1ef1d9f089b51d39430c87be0f560b5`, verified local `HEAD` at frozen ref, first-party MIT license.
- Observation date: 2026-10-28.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

`Proxy.complete` handles **one supplied model request**: derive the external request's step index/session key, optionally ask the decision backend typed questions, set model tier and tool hints, call a fast or strong upstream model, inspect the reply and at most redo that same model step. It returns the model response to its original caller. The next tool execution and subsequent message/request originate from that **caller**, not from a self-running proxy task loop. [Per-request boundary](https://github.com/JevAgentHarness/JevAgentHarness/blob/f2932199e1ef1d9f089b51d39430c87be0f560b5/src/jevagentharness/server.py#L145-L205), [upstream and retry/redo](https://github.com/JevAgentHarness/JevAgentHarness/blob/f2932199e1ef1d9f089b51d39430c87be0f560b5/src/jevagentharness/server.py#L197-L258), [external-proxy framing](https://github.com/JevAgentHarness/JevAgentHarness/blob/f2932199e1ef1d9f089b51d39430c87be0f560b5/README.md#L19-L37).

The `JevBackend` sends a fixed, per-point multiple-choice question plus compact recent transcript state to a Jev-compatible endpoint. Its probabilistic answer can route routine/hard steps, trigger reconsideration, filter tool menus, or in explicit `tool_select: cascade` mode **force the name of a tool**; the upstream LLM still writes arguments and the external harness runs it. `tool_params` and memory read/write are expressly absent from the proxy. `RulesBackend` can answer some questions deterministically, and an unanswered model falls back to operator-defined safety behavior. [Typed decision contract](https://github.com/JevAgentHarness/JevAgentHarness/blob/f2932199e1ef1d9f089b51d39430c87be0f560b5/src/jevagentharness/decision.py#L1-L115), [tool forcing and fallback decisions](https://github.com/JevAgentHarness/JevAgentHarness/blob/f2932199e1ef1d9f089b51d39430c87be0f560b5/src/jevagentharness/server.py#L289-L386), [decision mode and missing-module map](https://github.com/JevAgentHarness/JevAgentHarness/blob/f2932199e1ef1d9f089b51d39430c87be0f560b5/src/jevagentharness/points.py#L1-L77), [supported modes](https://github.com/JevAgentHarness/JevAgentHarness/blob/f2932199e1ef1d9f089b51d39430c87be0f560b5/docs/modes.md#L1-L48).

Session objects retain `last_tier`, fast streaks, sticky escalation, per-step routing/decision plans and costs, while `render_state` reconstructs the task/actions/results from the **incoming** request. This is history-aware routing support, not an independently maintained conversation/task executive. Strong/fast upstream calls and action guards operate on model replies before delivery. `jah report` and `jah fit` inspect proxy logs and fit static thresholds, not an online organization-level policy cycle. [Session and state extraction](https://github.com/JevAgentHarness/JevAgentHarness/blob/f2932199e1ef1d9f089b51d39430c87be0f560b5/src/jevagentharness/router.py#L67-L151), [guard logic](https://github.com/JevAgentHarness/JevAgentHarness/blob/f2932199e1ef1d9f089b51d39430c87be0f560b5/src/jevagentharness/server.py#L390-L540), [mode bounds](https://github.com/JevAgentHarness/JevAgentHarness/blob/f2932199e1ef1d9f089b51d39430c87be0f560b5/docs/modes.md#L63-L145).

## Operational model

The decision model exercises bounded semantic discrimination over an **external agent's** next API call: routine/hard, tool name, whether to redo/finish/reflect, and risky-action flags. That judgment may materially influence the external agent's tool choice or cost, but the proxy does not own the task's primary transformation, tool effects, goals, continuation schedule or model-result feedback loop. The label "System 1 / System 2" in the paper and README means fast/slow decision cognition; it is **not** Beer's Viable System Model S1/S2. Native offline tests verify routing/forcing/guard behavior, not an internal autonomous task agent.

## S1 — Operations

- State: —
- Function: no first-party self-directed agent operation from user task to tool effect, observation and next task decision is established; the actual transformation belongs to the upstream calling agent.
- Disturbance / variety regulated: request-level uncertainty about a model step's difficulty, cheapest suitable tier, likely tool, unsafe call or premature completion; not independent task-environment action/observation under proxy ownership.
- Decisive decision or feedback right: a selectable Jev model can choose tier/tool **hints** or even a forced tool name, while the external harness supplies the complete conversation, executes returned tools and decides whether/when another model request occurs. The upstream LLM writes tool arguments and task answer.
- Decision owner: proxy decision backend for bounded per-call classification; external autonomous agent and upstream LLM for real task outcome/continuation; host/operator for thresholds and fallback policy.
- Supporting / enforcement mechanisms: proxy HTTP dialects, transcript parser, typed probabilities, forced `tool_choice`, retries, strong fallback, session keyed tier/streak records, logs and configured model tiers.
- Closure path: external request → classification/tier/optional forced-tool constraint → upstream model step → return response **to external caller**. Tool effect → observation → subsequent request exists only if an external agent executes it. The proxy's session tier state updates from received turns but does not close an autonomous first-party work loop.
- Why this is / is not agent-owned: stripping external Codex/pi/other harness leaves a service responding to submitted API calls, not a task-capable agent that can continue, perform actions, observe its own environment or deliver an outcome. The trained classifier's semantic choice is not by itself the S1 operational cell at this boundary.
- Evidence: [request complete/return](https://github.com/JevAgentHarness/JevAgentHarness/blob/f2932199e1ef1d9f089b51d39430c87be0f560b5/src/jevagentharness/server.py#L145-L196), [forced-tool selector](https://github.com/JevAgentHarness/JevAgentHarness/blob/f2932199e1ef1d9f089b51d39430c87be0f560b5/src/jevagentharness/server.py#L330-L371), [caller retains tool arguments/memory](https://github.com/JevAgentHarness/JevAgentHarness/blob/f2932199e1ef1d9f089b51d39430c87be0f560b5/docs/modes.md#L105-L140), [proxy design](https://github.com/JevAgentHarness/JevAgentHarness/blob/f2932199e1ef1d9f089b51d39430c87be0f560b5/README.md#L19-L37).
- Basis: explicit source boundary plus structural negative.
- Confidence: high; inspected strongest opt-in forcing mode, not just the default.
- Caveats: `paper` mode does give the decision model a real local choice over tool name. This is acknowledged rather than misrepresented as deterministic routing, but decisive task ownership and continuation remain external.

### Absence scope

- Surfaces inspected: complete proxy `complete` and reply/redo path, router sessions, `JevBackend`/`RulesBackend`, tool-select/stop/reflection/action modes, native tests, CLI and upstream adapters.
- Plausible first-party paths checked: model-selected tool forcing, guard re-query, strong-tier fallback, history-based per-step session state, stop trigger, offline `jah fit`, and research agents used in benchmarks.
- Why no material first-party path remains: every supported live mode starts with an external agent API request and ends by returning an upstream model response; the proxy neither executes tool effects nor schedules the next task/environment observation loop. Benchmark/evaluation harnesses are excluded from installed ownership.

## S2 — Coordination

- State: —
- Function: no distinct first-party S1 work cells with specific interference and attenuating mutual adjustment are present.
- Disturbance / variety regulated: retries and duplicate calls against one proxy session, overlapping backend requests and tier streaks, not conflict among autonomous task-operating cells.
- Decisive decision or feedback right: a per-session `asyncio.Lock` serializes step planning, cached plans reuse decisions on retry, and fixed routing settings constrain model choice.
- Decision owner: deterministic proxy runtime and configured policy for serialization; learned classifier for a tier label; no inter-S1 coordination actor.
- Supporting / enforcement mechanisms: session key, lock, `decided` and `plans` dictionaries, tier stickiness, fallback and upstream request handling.
- Closure path: concurrent/retried HTTP traffic → serialized routing/cache → model reply; no measured/cited inter-unit collision and adjustment feeds into two independent S1 cells.
- Why this is / is not agent-owned: two possible model tiers are substitutes for **one** supplied step, not autonomous S1 units that must coordinate with each other.
- Evidence: [router session lock and plan state](https://github.com/JevAgentHarness/JevAgentHarness/blob/f2932199e1ef1d9f089b51d39430c87be0f560b5/src/jevagentharness/router.py#L130-L170), [serialized request decisions](https://github.com/JevAgentHarness/JevAgentHarness/blob/f2932199e1ef1d9f089b51d39430c87be0f560b5/src/jevagentharness/server.py#L160-L174), [retry reuses plan](https://github.com/JevAgentHarness/JevAgentHarness/blob/f2932199e1ef1d9f089b51d39430c87be0f560b5/src/jevagentharness/server.py#L293-L305).
- Basis: structural negative.
- Confidence: high for installed proxy boundary.
- Caveats: an external orchestration system may coordinate several agents through this proxy; its S2 is not implemented by JevAgentHarness.

### Absence scope

- Surfaces inspected: routing session lifecycle, locks, cache, concurrent per-call decision points, multi-tier adapters, tests and supported client/harness setup.
- Plausible first-party paths checked: fast/strong tier switching, shared proxy sessions, retries, side-by-side benchmark arms, multiple external harness clients.
- Why no material first-party path remains: no distinct autonomous first-party S1 group or function-specific inter-agent disturbance is shipped, so locks and queues do not establish S2 feedback.

## S3 — Inside-and-now control

- State: —
- Function: no first-party current whole-system control of competing autonomous S1 resource commitments or priority bargaining is established.
- Disturbance / variety regulated: step-level cost/quality, failed fast-model calls, per-session budget, streak limits and requested stop/redo; these are per-call routing controls.
- Decisive decision or feedback right: operator sets price tiers, threshold, budget, fallback and mode; learned classifier marks one request routine/hard and chooses a model tier within those settings.
- Decision owner: operator for allocation policy; classifier for single-step tier choice; deterministic router/server enforces caps and fallback. Neither has a whole-agent organization's current S1 portfolio view and intervention authority.
- Supporting / enforcement mechanisms: `over_budget` check, tier plans, sticky strong escalation, cost log, health/stat endpoints, strong redo.
- Closure path: one model request → tier/cost/guard → result and log; no whole-system review, rebalancing of live S1 commitments or returned current-control decision.
- Why this is / is not agent-owned: selecting a cheap/strong **model** is not automatically S3 management of multiple task operating units, and a cost ceiling does not acquire autonomous organizational authority through enforcement.
- Evidence: [router forced-tier rules](https://github.com/JevAgentHarness/JevAgentHarness/blob/f2932199e1ef1d9f089b51d39430c87be0f560b5/src/jevagentharness/router.py#L148-L210), [budget and one-step request](https://github.com/JevAgentHarness/JevAgentHarness/blob/f2932199e1ef1d9f089b51d39430c87be0f560b5/src/jevagentharness/server.py#L132-L188), [budget use](https://github.com/JevAgentHarness/JevAgentHarness/blob/f2932199e1ef1d9f089b51d39430c87be0f560b5/tests/test_proxy.py#L210-L226).
- Basis: structural negative.
- Confidence: high.
- Caveats: a parent application might govern total tokens/tasks across many agents; proxy logs could support that parent, but no first-party S3 current loop is credited.

### Absence scope

- Surfaces inspected: budgets/costs, router policies, session state, report/fit tooling, HTTP management endpoints and configured routing/guard modes.
- Plausible first-party paths checked: provider tier allocation, automatic strong escalation, new-session cost cap, dashboard-like stats, guard-driven retry.
- Why no material first-party path remains: each path governs individual API calls or enforces operator limits, without a manager that sees and decides competing S1 commitments across current operations.

## S3* — Complementary audit

- State: —
- Function: no sufficiently independent complementary audit of the **real task operation and effects** is shipped in the proxy boundary.
- Disturbance / variety regulated: mistaken fast-model final answers and risky proposed tool calls can be challenged by a decision model, but that check sees the same proxy transcript/proposal, not independently inspected task-world evidence.
- Decisive decision or feedback right: guard classifier may say `redo`/reject final reply; strong tier reruns the same step. This is ordinary in-line model validation and cost/safety fallback, not independent audit of subsequent tool effects.
- Decision owner: decision backend for limited probabilistic guard score; strong upstream model for replacement step; external harness observes actual tool outcomes.
- Supporting / enforcement mechanisms: `stop: guard`, `routing: guard`, `tool_select: guard`, `action: guard`, regex prefilter, one strong redo, response logs and benchmark evaluation.
- Closure path: proposed upstream response → classifier guard → accept/strong redo → client response. There is no separate raw-artifact/trace/task-environment inspection with audit findings returned into current organizational control.
- Why this is / is not agent-owned: a second model looking again at the same proposed reply can exercise local judgment without meeting S3* independence/complementarity; `bench/` scoring external to installed proxy cannot fill that gap.
- Evidence: [guard checks](https://github.com/JevAgentHarness/JevAgentHarness/blob/f2932199e1ef1d9f089b51d39430c87be0f560b5/src/jevagentharness/server.py#L390-L507), [decision-point types](https://github.com/JevAgentHarness/JevAgentHarness/blob/f2932199e1ef1d9f089b51d39430c87be0f560b5/src/jevagentharness/points.py#L1-L60), [evaluation separation](https://github.com/JevAgentHarness/JevAgentHarness/blob/f2932199e1ef1d9f089b51d39430c87be0f560b5/docs/modes.md#L27-L47).
- Basis: structural negative, explicitly considered apparent second-model auditor.
- Confidence: high for first-party proxied decision points.
- Caveats: the guards can be useful safety affordances; lack of S3* classification does not assert they are ineffective.

### Absence scope

- Surfaces inspected: pre/post-call guard modes, upstream redos, action prefilters, proxy logs/reports, benchmark outcome analysis and external harness integrations.
- Plausible first-party paths checked: second model validating tool name/action, finish guard, routing guard, risk triggers, offline held-out tests and shadow labels.
- Why no material first-party path remains: guards compare a model proposal to the same supplied transcript, without independently sourced operational reality or a findings-to-control audit channel. Benchmark/QA development artifacts are not runtime S3* actors.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party externally and prospectively oriented strategy loop that updates current operational capability is established.
- Disturbance / variety regulated: current request difficulty, fast-tier cost, historical routing labels and fitted thresholds; not future environmental threats/opportunities.
- Decisive decision or feedback right: operators choose thresholds/models/presets; `jah fit` computes candidate threshold settings from past labels and returns a report/config recommendation for operator selection.
- Decision owner: operator for model/policy adaptation; deterministic fitting utility for historical numeric optimization; per-step classifier for immediate routing only.
- Supporting / enforcement mechanisms: `states.jsonl`, `decisions.jsonl`, `jah report`, `jah fit`, experiment reports and price schedules.
- Closure path: past proxy logs → static fit/report → possible manual config update; no model-owned future-environment model ↔ current S3 feedback cycle.
- Why this is / is not agent-owned: threshold fitting and test-set benchmarks tune cost/quality but do not prove open-ended future-adaptation rights, and the environment is externally supplied by the task agent.
- Evidence: [fit/report utility](https://github.com/JevAgentHarness/JevAgentHarness/blob/f2932199e1ef1d9f089b51d39430c87be0f560b5/src/jevagentharness/fit.py), [routing session/cost state](https://github.com/JevAgentHarness/JevAgentHarness/blob/f2932199e1ef1d9f089b51d39430c87be0f560b5/src/jevagentharness/router.py#L127-L150), [shadow fitting workflow](https://github.com/JevAgentHarness/JevAgentHarness/blob/f2932199e1ef1d9f089b51d39430c87be0f560b5/docs/modes.md#L28-L56).
- Basis: structural negative.
- Confidence: high within standard distribution.
- Caveats: a research organization might use Jev experiments to revise a future system, but it is a separate external decision boundary.

### Absence scope

- Surfaces inspected: online routing and decision points, offline threshold fitting, experiments, logging and configuration.
- Plausible first-party paths checked: routing policy tuning, shadow data, cost/latency analysis, benchmark configuration and choice of new provider tiers.
- Why no material first-party path remains: the only changes are operator-selected thresholds/tier settings from historical data; no first-party agent models future external variety and returns a coherent S4 option to its own S3.

## S5 — Policy and identity

- State: —
- Function: no legitimate ultimate identity/policy deliberation and return-to-operation loop for an autonomous task agent organization is evidenced.
- Disturbance / variety regulated: proxy budgets, model names, fallback priorities, hard/fast thresholds and tool/action prefilters are operating parameters, not identity tensions.
- Decisive decision or feedback right: operator writes config/presets, selects decision service/provider credentials and decides the original agent's goals/policy outside the proxy.
- Decision owner: operator/external harness and its parent organization; proxy mechanically enforces selected settings and model responses.
- Supporting / enforcement mechanisms: YAML configuration, CLI flags, budget checks, fixed routing defaults, safety guard, provider key environment.
- Closure path: edited config → subsequent proxy requests use it; no first-party identity-level matter reaches a legitimate decision authority and returns as a settled S5 judgment.
- Why this is / is not agent-owned: a system prompt-like decision question, tool prefilter or operator permission is not an identity/ultimate-policy function.
- Evidence: [config/modes contract](https://github.com/JevAgentHarness/JevAgentHarness/blob/f2932199e1ef1d9f089b51d39430c87be0f560b5/src/jevagentharness/config.py), [operator presets](https://github.com/JevAgentHarness/JevAgentHarness/blob/f2932199e1ef1d9f089b51d39430c87be0f560b5/src/jevagentharness/points.py#L55-L87), [proxy boundary](https://github.com/JevAgentHarness/JevAgentHarness/blob/f2932199e1ef1d9f089b51d39430c87be0f560b5/README.md#L19-L37).
- Basis: structural negative.
- Confidence: high.
- Caveats: a user may supply organization-level constraints to an external coding agent; those are not JevAgentHarness-owned S5.

### Absence scope

- Surfaces inspected: CLI and YAML configuration, budget and fallback rules, decision backend authentication, presets and supported integration/management.
- Plausible first-party paths checked: policy edits, safe-action guard, strongly enforced finish check, provider credential selection and task-identity context in requests.
- Why no material first-party path remains: none supplies an identity-level issue, legitimate ultimate policy owner and feedback closure at the installed proxy recursion.

## Recursion

The external coding agent is the meaningful operational S1 system: it chooses or receives tool calls, executes tools, absorbs results and decides when to call its model again. JevAgentHarness intercepts that model call and may influence a **slice** of discretion, including high-confidence tool-name forcing in the explicit paper preset. That useful local model decision is not enough to move the entire external operating agent inside the proxy's ownership boundary. The trained model's "System 1" and "System 2" terminology concerns cognitive response speeds and must not be imported into VSM S1/S2.

## Variety and escalation

- Local variety: supplied transcript/possible next model response, expected difficulty, potentially risky tool choice, endpoint errors, price/cost tier difference.
- Attenuation/enforcement: summarized/truncated state, two-choice classifier, threshold/presets, pinned strong first steps, sticky escalation, budget caps, strong redo, session locks and no-answer fallback.
- Amplification: choice of upstream model tiers and decision backend, optional tool-menu forcing/shortlist and strong-tier re-query; these augment the external agent's tools rather than create an independent task agent.
- Escalation: routing mistakes/failures can escalate **one model step** to strong tier. This is a quality/fallback channel, not an algedonic VSM organizational response with whole-system authority.
- Viability boundary: as a standalone proxy it fails the agent-owned task-operation S1 requirement. The result does not deny possible usefulness to an external agentic system.

## Evidence gaps

- Frozen source checkout and first-party MIT license were verified. The proxy's substantive runtime and all documented decision modes were inspected, including the strongest opt-in `tool_select: cascade` case.
- Offline deterministic test suite: `env PYTHONPATH=src uv run --no-project --with pytest --with aiohttp --with pyyaml python -m pytest -q` passed **72/72** without provider calls. A standard `uv run --extra dev pytest` first failed dependency resolution because optional `bench` Harbor requires Python >=3.12 while the project supports >=3.10; the minimal independent test environment avoided that packaging conflict.
- No live Codex/pi session, provider call, paid decision model, Docker benchmark or research paper result was independently reproduced. Benchmark performance figures are not used as evidence of VSM agent ownership.
- Bounded negative judgments concern the shipped proxy, not a hypothetical application embedding it as one component of an external S1. No concrete unresolved first-party operating mode remains that would require `?`; users can construct new systems beyond this boundary.

## Assessment summary

- Proposed disposition: **excluded-no-agentic-vsm** at canonical admission, if accepted. Model-backed decisions over request routing, tool-name constraints and in-line guards are real, but the independent task/observation/continuation loop is owned by the external harness.
- Vector at reviewed boundary: `— — — — — —`. No VSM viability or security certification implied; this is a boundary-specific ownership finding.

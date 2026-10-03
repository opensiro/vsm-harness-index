---
harness_id: cascadeflow
project_name: cascadeflow
repository: https://github.com/lemony-ai/cascadeflow
review_ref: d8251001a51c22dc3d3ea596d89f89c4a5d74f8b
reviewed_at: 2026-10-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-04
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: C
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# cascadeflow

## Review boundary

- System in focus: the first-party `lemony-ai/cascadeflow` in-process agent/harness organization at frozen revision `d8251001a51c22dc3d3ea596d89f89c4a5d74f8b`, centered on `CascadeAgent`, the shipped model-cascade and tool-execution loop, quality/routing machinery, scoped harness run state, and built-in observe/enforce instrumentation where those surfaces regulate one cascadeflow-managed agent run.
- Purpose and identity: produce model-backed answers/tool outcomes while dynamically selecting model capacity and regulating current cost, latency, energy, tool-use, compliance, and KPI constraints inside the execution loop.
- Relevant environment: user queries/messages, configured tools, model/provider responses, tool results, provider availability/capability, current run cost/latency/energy/tool usage, configured compliance/KPI constraints, and quality/complexity signals.
- Standard-distribution boundary: the Python package's `CascadeAgent`, first-party cascade/quality/routing/tool/harness modules and their built-in provider adapters are inside. LangChain, CrewAI, OpenAI Agents SDK, Google ADK, PydanticAI, n8n, OpenClaw, Hermes Agent and other external agent/framework organizations reached through integrations are external; their S1-S5 functions are not inherited. Provider models supply inference but are credited only where cascadeflow's shipped role/loop closes the first-party operational path.
- Credited operating / distribution surfaces: `README.md`; `cascadeflow/agent.py`; `cascadeflow/core/cascade.py`; `cascadeflow/quality/{quality,adaptive}.py`; `cascadeflow/rules/engine.py`; `cascadeflow/harness/{api,instrument}.py`; `cascadeflow/tools/executor.py`; first-party routing and telemetry modules used by those paths.
- Adjacent first-party surfaces excluded from ownership: multi-agent and framework examples; integration wrappers whose organizational authority belongs to the wrapped external framework; repository-development tests/CI/benchmarks; documentation-only claims not reachable in the frozen runtime; maintainer/contributor governance; TypeScript parity code where it merely corroborates rather than changes the assessed Python operating path.
- First-party operating / deployment modes considered: direct `CascadeAgent.run` response generation; optional first-party tool execution; speculative drafter/verifier cascade; complexity/domain/rule routing; adaptive quality thresholding; harness `observe` and `enforce` modes around instrumented model calls; scoped `run(...)` contexts carrying budget/tool/latency/energy/KPI/compliance constraints.
- Recursion level: one cascadeflow-managed agent run is the focal organization. Its model-backed response/tool loop is the S1 operational unit. Drafter and verifier calls, provider requests, tool calls, and external subagents/framework actors are lower-level or external operations unless independently shown to be viable same-recursion S1 units.
- Reviewed revision: `d8251001a51c22dc3d3ea596d89f89c4a5d74f8b`.
- Observation date: 2026-10-04.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

cascadeflow ships both a direct `CascadeAgent` and an in-process harness layer. `CascadeAgent` normalizes a request, detects complexity/domain, applies routing/rule constraints, invokes configured model providers, validates draft quality, escalates to a verifier when required, aggregates diagnostics/cost, and can execute model-requested tools through the supplied first-party `ToolExecutor` path. The primary outcome is therefore produced by a first-party loop rather than by a passive proxy record alone.

The harness layer exposes `init(mode="observe"|"enforce")` plus scoped `run(...)` state. `HarnessRunContext` aggregates current run cost, tool-call count, latency, energy, model/action state and configured limits. The instrumentation path intercepts model calls and computes a concrete pre-call action. At the frozen revision, `_evaluate_pre_call_decision` can return `allow`, `switch_model`, `deny_tool`, or `stop` from current budget/tool/latency/energy/compliance/KPI state; `_resolve_pre_call_decision` applies that action in enforce mode by mutating the selected model/tool set or raising the stop error. This is a real current-control feedback loop, but the organizational discretion is deterministic/configured rather than owned by an autonomous supervisory agent.

Quality validation includes an adaptive threshold manager. It records recent acceptance outcomes by domain, periodically tightens/relaxes thresholds and can recognize previously hard query patterns when embedding mode is enabled. This changes later routing/quality behavior, but the input is internal operating history rather than an externally and prospectively oriented environment model, so it is not credited as S4.

Primary evidence:

- [`README.md`](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/README.md)
- [`cascadeflow/agent.py`](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/cascadeflow/agent.py)
- [`cascadeflow/core/cascade.py`](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/cascadeflow/core/cascade.py)
- [`cascadeflow/quality/quality.py`](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/cascadeflow/quality/quality.py)
- [`cascadeflow/quality/adaptive.py`](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/cascadeflow/quality/adaptive.py)
- [`cascadeflow/harness/api.py`](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/cascadeflow/harness/api.py)
- [`cascadeflow/harness/instrument.py`](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/cascadeflow/harness/instrument.py)
- [`cascadeflow/rules/engine.py`](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/cascadeflow/rules/engine.py)
- [`cascadeflow/tools/executor.py`](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/cascadeflow/tools/executor.py)

## Operational model

A standard `CascadeAgent` request gives cascadeflow a first-party operational role: use the request plus configured model/tool capabilities to decide the execution path, produce or accept a model-backed result, optionally execute requested tools, and return the final outcome with telemetry. External models provide inference, but cascadeflow owns the shipped role, routing/quality loop, tool-return plumbing, and final result closure used by callers.

Separately, the harness mode can surround model calls inside a larger agent loop. The scoped run state accumulates whole-run current operating quantities. Each later call is evaluated against those accumulated quantities and configured constraints; in enforce mode the decision directly changes whether the next call proceeds, which model it uses, whether tools remain available, or whether the run stops.

## S1 — Operations

- State: A
- Function: transform a user/application request into a model-backed answer or tool-mediated result through cascadeflow's shipped request/routing/quality/execution loop.
- Disturbance / variety regulated: heterogeneous query complexity/domain, model/provider capability and cost, draft quality/confidence, tool requests/results, multi-turn context, and fallback/escalation conditions requiring contextual model judgment rather than a fixed literal response.
- Decisive decision or feedback right: generate the operational response/tool request through the selected model-backed actor and feed that result through cascadeflow's first-party acceptance/escalation/tool-return path to determine the returned outcome.
- Decision owner: the model-backed operational actor invoked through `CascadeAgent`'s first-party provider/cascade path. cascadeflow owns the role and closure; configured providers supply external inference rather than donating unrelated metasystem functions.
- Supporting / enforcement mechanisms: complexity/domain detectors; rule/model constraints; provider adapters; `WholeResponseCascade`; quality validators; telemetry/cost calculation; tool normalization and `ToolExecutor`; request-scoped knowledge preparation; streaming/result wrappers.
- Closure path: caller supplies request/messages/tools → `CascadeAgent.run` normalizes and routes the request → selected model-backed actor produces a draft/response or tool call → cascadeflow validates/escalates and, when configured, executes tool calls and returns their results into the loop → the final accepted model-backed result is returned to the caller with diagnostics.
- Boundary reachability: `CascadeAgent`, provider adapters, cascade/quality routing and optional tool execution are shipped first-party runtime surfaces. A downstream developer configures models/tools but does not need to build the agentic request→model judgment→feedback→returned-result loop from generic callbacks.
- Why this is / is not agent-owned: removing the model-backed actor while leaving deterministic routing, telemetry and limit machinery preserves bookkeeping but removes the contextual judgment that produces the primary answer/tool decision. S1 discretion is therefore agent-owned even though the inference provider itself is external.
- Evidence: [`README.md`](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/README.md); [`cascadeflow/agent.py`](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/cascadeflow/agent.py); [`cascadeflow/core/cascade.py`](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/cascadeflow/core/cascade.py); [`cascadeflow/tools/executor.py`](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/cascadeflow/tools/executor.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: external LangChain/CrewAI/OpenAI Agents/OpenClaw/Hermes/etc. agent loops are not credited. S1 is limited to cascadeflow's own model-backed `CascadeAgent` role and closure at the frozen revision.

## S2 — Coordination

- State: —
- Function: no material first-party same-recursion inter-S1 coordination function was established.
- Disturbance / variety regulated: not established because the standard assessed recursion exposes one cascadeflow operational unit; multiple model calls, drafter/verifier stages and parallel tool calls do not by themselves create distinct same-recursion S1 units with an evidenced mutual disturbance.
- Decisive decision or feedback right: not established at S2.
- Decision owner: not established as a first-party S2 owner.
- Supporting / enforcement mechanisms: model routing; drafter→verifier sequencing; tool routing; parallel tool execution; integration adapters; multi-agent examples.
- Closure path: not applicable at S2; no specific inter-S1 conflict/oscillation → coordination response → changed subsequent S1 behaviour loop was found.
- Why this is / is not agent-owned: cascadeflow can route among models and can be embedded into external multi-agent frameworks, but routing/delegation is not S2 without distinct S1 units plus a concrete interference witness and attenuation path.
- Evidence: [`cascadeflow/agent.py`](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/cascadeflow/agent.py); [`cascadeflow/core/cascade.py`](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/cascadeflow/core/cascade.py); [`cascadeflow/tools/executor.py`](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/cascadeflow/tools/executor.py); [`README.md`](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: external framework integrations may participate in S2 at the host framework's recursion, but their coordination authority is outside the declared cascadeflow boundary.

### Absence scope

- Surfaces inspected: direct agent runtime, cascade/routing/quality path, tool execution including parallel tools, integration tree, multi-agent examples, README architecture and harness API.
- Plausible first-party paths checked: multiple configured models; drafter/verifier relationship; parallel tool calls; external-framework multi-agent integrations/examples; domain/tier/tool routers.
- Why no material first-party path remains: the located plurality is either lower-level sequencing/routing within one S1 or belongs to an external host organization. No shipped cascadeflow path establishes two distinct same-recursion S1 units plus a concrete interaction disturbance and S2-specific feedback relation.

## S3 — Inside-and-now control

- State: C
- Function: regulate the current cascadeflow-managed run on behalf of the whole run by maintaining aggregate operating state and applying current resource/constraint interventions to subsequent model/tool activity.
- Disturbance / variety regulated: cumulative cost can exhaust budget; tool calls can exceed a run limit; latency/energy can exceed bounds; compliance policy can make a model/tool path inadmissible; KPI pressure can make another model preferable while the current run is still executing.
- Decisive decision or feedback right: on each intercepted model call, choose `allow`, `switch_model`, `deny_tool`, or `stop` from current aggregate run state and configured constraints, then apply that transition in enforce mode.
- Decision owner: first-party deterministic constructor/control logic in `harness/instrument.py`, parameterized by developer/operator configuration. No autonomous supervisory agent owns the current-control discretion in the evidenced standard mode.
- Supporting / enforcement mechanisms: `HarnessRunContext` counters/limits; OpenAI/Anthropic instrumentation; model price/latency/energy priors; compliance allowlists; KPI weights; trace recording; exceptions; model/tool argument mutation.
- Closure path: model/tool activity updates the scoped run totals → before the next model call, `_evaluate_pre_call_decision` reads those current totals/constraints → `_resolve_pre_call_decision` applies switch/deny/stop/allow in enforce mode → the next operation is changed or terminated → subsequent totals feed the next control decision.
- Boundary reachability: `init(mode="enforce")`, `run(...)`, `HarnessRunContext` and the built-in instrumentation/pre-call decision path are shipped together and directly applied to supported instrumented provider calls. A downstream user chooses constraints but does not need to invent the current-state aggregation or enforcement feedback path.
- Why this is / is not agent-owned: removing any autonomous model while keeping the run-state and instrumentation machinery leaves materially the same budget/tool/latency/energy/compliance/KPI control decision. The current-control function is therefore real but not agent-owned; the published constructor/control state is `C`.
- Evidence: [`README.md`](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/README.md); [`cascadeflow/harness/api.py`](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/cascadeflow/harness/api.py); [`cascadeflow/harness/instrument.py`](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/cascadeflow/harness/instrument.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: configuration authors own the policy values; deterministic enforcement does not turn them into an autonomous S3 actor. Conversely, the path is more than telemetry alone because the shipped enforce mode feeds the decision back into subsequent current operation.
- Whole-system current view: the scoped `HarnessRunContext` aggregates cost, tool calls, latency, energy, budget remaining, model/action state and configured run constraints across the current cascadeflow-managed run.
- Current-control decision scope: whether the next intercepted model call may proceed, which model may serve it, whether tool capability remains available, or whether the current run must stop under the configured resource/compliance/KPI envelope.

## S3* — Complementary audit

- State: —
- Function: no materially independent complementary audit path was established.
- Disturbance / variety regulated: cascadeflow validates draft quality and can call a verifier, but these checks are routine production-path acceptance/escalation stages rather than sporadic/complementary access to operational reality.
- Decisive decision or feedback right: not established as a separate audit judgment.
- Decision owner: not established as a first-party S3* owner.
- Supporting / enforcement mechanisms: `QualityValidator`; drafter/verifier cascade; semantic alignment/confidence checks; telemetry/traces; tests and examples.
- Closure path: not applicable at S3*; the located checks remain in the ordinary response-production path or adjacent development/evaluation surfaces.
- Why this is / is not agent-owned: a verifier model may independently generate a response, but routine verifier use inside the normal cascade does not by itself satisfy complementary-audit independence or alternative access.
- Evidence: [`cascadeflow/core/cascade.py`](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/cascadeflow/core/cascade.py); [`cascadeflow/quality/quality.py`](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/cascadeflow/quality/quality.py); [`README.md`](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: a host application could use cascadeflow traces/results inside an external audit organization; that external composition is not shipped S3* closure for cascadeflow itself.

### Absence scope

- Surfaces inspected: normal quality-validation and verifier path; telemetry/tracing; tool validation; README architecture; tests/examples and integration surfaces.
- Plausible first-party paths checked: verifier calls; semantic/alignment checks; telemetry anomaly/trace features; routine validation/fallback; repository test/evaluation surfaces.
- Why no material first-party path remains: all located runtime checking either participates directly in routine answer acceptance/escalation or supplies observability. No distinct complementary access path with sufficient independence and a feedback loop into control was found.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party external-and-prospective adaptation loop was established.
- Disturbance / variety regulated: adaptive quality thresholds react to internal acceptance history, but no shipped loop was found that models changing external users/regulation/threats/dependencies/opportunities, develops future-oriented organizational options, and returns such options to present capability.
- Decisive decision or feedback right: not established at S4.
- Decision owner: not established as a first-party S4 owner.
- Supporting / enforcement mechanisms: `AdaptiveThresholdManager`; rolling outcome windows; hard-query embeddings; domain detection; runtime configuration update APIs; telemetry forecasting/degradation utilities.
- Closure path: not applicable at S4; internal operating outcomes can tune later quality thresholds, but that is generic learning/current optimization rather than outside-and-then adaptation closure.
- Why this is / is not agent-owned: self-adjusting thresholds are algorithmic learning from internal production history. The Profile explicitly requires external/future distinctions and adaptation-option development, which the inspected path does not supply.
- Evidence: [`cascadeflow/quality/adaptive.py`](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/cascadeflow/quality/adaptive.py); [`cascadeflow/quality/quality.py`](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/cascadeflow/quality/quality.py); [`cascadeflow/agent.py`](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/cascadeflow/agent.py).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: future model/provider selection can change as thresholds adjust, but temporal effect alone is not S4.

### Absence scope

- Surfaces inspected: adaptive quality learning; domain/rule routing; telemetry forecasting/degradation modules; dynamic/runtime configuration; README self-improvement claims; integrations and examples.
- Plausible first-party paths checked: acceptance-rate adaptation; hard-query similarity memory; domain learning; model updates; telemetry forecasts; runtime config changes; provider/model routing.
- Why no material first-party path remains: located mechanisms optimize from internal call history or apply preconfigured runtime choices. No externally and prospectively oriented environment model develops adaptation options and couples them back to present S3/capability.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy closure was established.
- Disturbance / variety regulated: budget, compliance, KPI weights, model allowlists, routing rules and tool restrictions constrain execution, but they are ordinary operating policy/configuration rather than a path for deciding the organization's ultimate identity or supreme policy.
- Decisive decision or feedback right: not established at S5.
- Decision owner: not established as a first-party S5 owner.
- Supporting / enforcement mechanisms: harness config; compliance allowlists; KPI/routing rules; tenant/channel overrides; model/tool restrictions; environment/file configuration.
- Closure path: not applicable at S5; no identity/ultimate-policy issue → legitimate authority → authoritative decision → returned governance loop was found.
- Why this is / is not agent-owned: the runtime enforces configured constraints and can optimize model choice, but neither an autonomous actor nor a parent-governed shipped path is given ultimate identity/policy decision authority.
- Evidence: [`cascadeflow/harness/api.py`](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/cascadeflow/harness/api.py); [`cascadeflow/harness/instrument.py`](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/cascadeflow/harness/instrument.py); [`cascadeflow/rules/engine.py`](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/cascadeflow/rules/engine.py); [`README.md`](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: an operator can change configuration, but generic ability to edit policy values is not a qualifying parent S5 closure.

### Absence scope

- Surfaces inspected: harness/config/rules/compliance/KPI paths; runtime update APIs; provider/tool restrictions; integrations; documentation; repository governance adjacent to the runtime.
- Plausible first-party paths checked: compliance mode; budget/KPI policy; tenant/channel overrides; runtime model/quality updates; operator configuration; maintainer governance.
- Why no material first-party path remains: located authority chooses or enforces ordinary operational constraints. No shipped path represents an identity/ultimate-policy dispute, routes it to legitimate ultimate authority, and returns that decision to govern later operation.

## Distributed OSS parent arrangement

cascadeflow is an OSS library whose maintainers and downstream operators can make configuration/repository decisions, but the inspected frozen distribution does not expose a function-specific organization-level parent-governance loop that warrants `(P)` or standalone `P`. Operator configuration is treated as input to the runtime unless a current S3/S4/S5 parent decision path is independently closed.

## Self-hosted and non-human modes

Self-hosted/local provider support changes where inference executes but does not change the ownership findings above. The first-party current-control path remains deterministic/configured, while S1 remains model-backed. No distinct non-human S3/S4/S5 ownership mode beyond the classified constructor S3 path was established.

## Recursion

The focal recursion is one cascadeflow-managed agent run. `CascadeAgent`'s model-backed response/tool loop is the operational S1. Drafter and verifier calls are stages within that unit, tool calls are subordinate operations, and external framework agents are outside the assessed organization. The scoped harness context provides current-control regulation over that run without creating additional same-recursion S1 units.

## Variety and escalation

cascadeflow amplifies operational variety through multiple providers/models, tools, domain/complexity routing and model-backed generation. It attenuates quality/cost/latency/energy/compliance variety through deterministic routing, quality gates and the enforce-mode current-control path. Draft rejection can escalate to a verifier and run-limit pressure can switch/deny/stop subsequent operations. Those are current production controls; no complementary S3* audit, external-prospective S4 adaptation or identity-level S5 closure was found.

## Evidence gaps

No evidence gap requires `?` at the frozen revision. The main boundary decision is deliberate: external host-agent and multi-agent framework functions are excluded, while cascadeflow's own `CascadeAgent` model-backed operational loop is credited for S1. The strongest positive metasystem witness is S3 constructor/control: whole-run current state is fed into a shipped deterministic intervention loop, but an autonomous supervisory decision owner is not present.

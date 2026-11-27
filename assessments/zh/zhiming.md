---
harness_id: zhiming
project_name: ZhiMing
repository: https://github.com/stanGSA/ZhiMing
review_ref: 9e092aecf37f9d7b92cbb22a67594721ce86b57b
reviewed_at: 2026-11-27
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# ZhiMing

## Review boundary

- System in focus: The shipped ZhiMing consultation application with model-backed single and multi-agent modes.
- Purpose and identity: Respond to scoped user consultations using tool-computed domain inputs, structured references and validation.
- Relevant environment: A CLI or browser deployment with a configured inference provider, local data, persistent knowledge and user state.
- Standard-distribution boundary: First-party CLI and web runtime, tool registries and calculation plugins, hosted locally or as provided. The offline container is explicitly a demo mode.
- Credited operating / distribution surfaces: Runtime setup and session/tool loop, supported multi-agent consultation and reviewer, domain calculators, output validation and persistence.
- Adjacent first-party surfaces excluded from ownership: Pure offline demo and companion MCP server as separate pathways without credited model ownership; maintainer data preparation, knowledge-release review/evaluation and server monitoring outside consultation decision ownership.
- First-party operating / deployment modes considered: Model-backed single default and opt-in multi lane, browser and CLI; offline demo inspected separately.
- Recursion level: Installed consultation runtime. In multi mode a specialist is an operational cell within one user's consultation.
- Reviewed revision: 9e092aecf37f9d7b92cbb22a67594721ce86b57b
- Observation date: 2026-11-27
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

The runtime wires either direct domain tools or a consultation service with isolated experts and an orchestrator. Specialists use restricted registries, calculate domain facts and submit structured reports. The parent commits compatible evidence, synthesizes a response, and validates references and applicable policy. When enabled, a separate draft reviewer receives a structured packet and may request bounded revision before persistence.

## Operational model

The model chooses which tools or specialists can answer a request and returns a validated reading or asks for missing input. In multi mode, specialists close their own bounded reports from evidence and the orchestrator regulates compatible inputs and merges. Deterministic tools compute domain values and enforce consistency and evidence rules.

## S1 — Operations

- State: A
- Function: Produce a structured, validated consultation response, or return a concrete request for clarification.
- Disturbance / variety regulated: Different consultation questions, incomplete input, signals that disagree, tool validation errors and feedback on drafts.
- Decisive decision or feedback right: Select a domain and the tools or specialists to consult, then assemble, repair and submit a result.
- Decision owner: The configured model-backed consultation agent. In multi mode each specialist also owns its bounded tool and report choices.
- Supporting / enforcement mechanisms: Role-specific registries, deterministic calculators, evidence references, output validation, persistence and bounded runtime.
- Closure path: Tool results become model observations. The agent submits a grounded reading, patches a rejected draft or requests facts, and a successful terminal tool stores and renders the result.
- Boundary reachability: The checked-in CLI and browser runtime construct the first-party consultation loop and registries. The CLI exposes both bundled modes without requiring the user to author an agent.
- Why this is / is not agent-owned: The model chooses how to handle the request from evidence and can repair outcomes; domain calculations and validation are external to that judgment.
- Evidence: [cli.py](https://github.com/stanGSA/ZhiMing/blob/9e092aecf37f9d7b92cbb22a67594721ce86b57b/cli.py#L20-L56), [app.py](https://github.com/stanGSA/ZhiMing/blob/9e092aecf37f9d7b92cbb22a67594721ce86b57b/app.py#L146-L187), [app.py](https://github.com/stanGSA/ZhiMing/blob/9e092aecf37f9d7b92cbb22a67594721ce86b57b/app.py#L255-L353), [agents/orchestrator.py](https://github.com/stanGSA/ZhiMing/blob/9e092aecf37f9d7b92cbb22a67594721ce86b57b/agents/orchestrator.py#L16-L47), [common/tools.py](https://github.com/stanGSA/ZhiMing/blob/9e092aecf37f9d7b92cbb22a67594721ce86b57b/common/tools.py#L886-L951)
- Basis: Pinned first-party source inspection.
- Confidence: high
- Caveats: The application is scoped to a structured consultation and calculation product. The offline demo uses a different decision path and is not evidence for model ownership.

## S2 — Coordination

- State: A
- Function: Coordinate separate domain specialists whose outputs must share one consistent requested interval and evidence state.
- Disturbance / variety regulated: Parallel consultations may duplicate work or compute mutually incompatible timeframes and write competing values into shared evidence.
- Decisive decision or feedback right: The orchestrator selects and normalizes the inputs and consult set, then decides which specialist to retry, omit or wait for when a report is incompatible or missing input.
- Decision owner: The shipped multi-mode orchestrator model, with deterministic safeguards for shared state mutation and resource interference.
- Supporting / enforcement mechanisms: Isolated child sessions, shared input conventions, same-system in-flight dedupe, bounded parallel work, and ordered conflict-aware commit.
- Closure path: A differing timeframe rejects a consult or contribution before it reaches shared reading state. The orchestrator receives failed/needs-input/retained evidence, then changes subsequent calls, collects one clarification, or continues explicitly with compatible surviving reports.
- Boundary reachability: The runtime registers the specific consultation tool in supported multi mode; its results are committed and returned automatically through the same agent loop.
- Why this is / is not agent-owned: The orchestrator decides the shared consultation treatment and reacts to the coordination outcome. The timeframe check and single writer enforce the relation.
- Distinct S1 units: Separate model-driven Tarot, Western astrology, BaZi, name and dream specialist sessions, each with its own role, registry and structured report.
- Inter-S1 disturbance: Concurrent calls can span incompatible intervals or repeat a same-system computation, corrupting shared evidence assumptions.
- Attenuating coordination relation: Pass a common timeframe, reject duplicate/inconsistent work, and write isolated contributions in call order only when compatible.
- Feedback into subsequent S1 behaviour: The parent model sees the specific coordination failure, remaining valid report or missing-input status and changes what happens next.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The tool implements a dedicated cross-specialist compatibility check and report validity decision, and the orchestrator receives the result as input to subsequent specialist work.
- Evidence: [agents/orchestrator.py](https://github.com/stanGSA/ZhiMing/blob/9e092aecf37f9d7b92cbb22a67594721ce86b57b/agents/orchestrator.py#L33-L40), [agents/consult.py](https://github.com/stanGSA/ZhiMing/blob/9e092aecf37f9d7b92cbb22a67594721ce86b57b/agents/consult.py#L74-L121), [agents/consult.py](https://github.com/stanGSA/ZhiMing/blob/9e092aecf37f9d7b92cbb22a67594721ce86b57b/agents/consult.py#L187-L202), [agents/consult.py](https://github.com/stanGSA/ZhiMing/blob/9e092aecf37f9d7b92cbb22a67594721ce86b57b/agents/consult.py#L391-L410), [agents/consult.py](https://github.com/stanGSA/ZhiMing/blob/9e092aecf37f9d7b92cbb22a67594721ce86b57b/agents/consult.py#L508-L556), [harness/loop.py](https://github.com/stanGSA/ZhiMing/blob/9e092aecf37f9d7b92cbb22a67594721ce86b57b/harness/loop.py#L253-L313)
- Basis: Pinned first-party source inspection.
- Confidence: high
- Caveats: Only the supported multi-agent mode supplies this relation. The repository defaults to single mode.

## S3 — Inside-and-now control

- State: —
- Function: No distinct inside-and-now organizational control function was established.
- Disturbance / variety regulated: Concurrent consultations can contend for one request's tokens and time. The web service also has session lifecycle and health reporting.
- Decisive decision or feedback right: No distinct function-specific decision or feedback right was established.
- Decision owner: No distinct owner at the declared recursion.
- Supporting / enforcement mechanisms: Hierarchical token holds and reserve, request timeout, consult semaphore, report status and optional server alert checks.
- Closure path: A per-request child is admitted, waits, or fails within fixed limits and the agent chooses how to complete the individual case.
- Why this is / is not agent-owned: The model manages one consultation rather than reallocating current responsibilities or resources across a broader operating portfolio. The deployed monitoring script emits observations and alerts.
- Evidence: [app.py](https://github.com/stanGSA/ZhiMing/blob/9e092aecf37f9d7b92cbb22a67594721ce86b57b/app.py#L146-L187), [harness/budget.py](https://github.com/stanGSA/ZhiMing/blob/9e092aecf37f9d7b92cbb22a67594721ce86b57b/harness/budget.py#L9-L64), [agents/consult.py](https://github.com/stanGSA/ZhiMing/blob/9e092aecf37f9d7b92cbb22a67594721ce86b57b/agents/consult.py#L143-L155), [agents/orchestrator.py](https://github.com/stanGSA/ZhiMing/blob/9e092aecf37f9d7b92cbb22a67594721ce86b57b/agents/orchestrator.py#L33-L40), [ops/monitor.py](https://github.com/stanGSA/ZhiMing/blob/9e092aecf37f9d7b92cbb22a67594721ce86b57b/ops/monitor.py#L773-L839)
- Basis: Pinned first-party source inspection.
- Confidence: high
- Caveats: Finding is bounded to the pinned first-party operating surfaces.

### Absence scope

- Surfaces inspected: Multi consultation control, token allocation, web sessions, deployment recipe and the operational monitor.
- Plausible first-party paths checked: Operator or model control of live commitments, service capacity and responses to alert feedback.
- Why no material first-party path remains: Task-level fan-out and deterministic request limits do not supply a separate whole-system controller. No first-party monitor-to-control decision return was identified in the assessed modes.

## S3* — Complementary audit

- State: —
- Function: No complementary operational audit path was established inside the consultation harness.
- Disturbance / variety regulated: A draft can omit disagreement, cite unsupported facts or otherwise fail output policy.
- Decisive decision or feedback right: No distinct function-specific decision or feedback right was established.
- Decision owner: No distinct owner at the declared recursion.
- Supporting / enforcement mechanisms: A separate reviewer role, deterministic source-reference validation, run traces, and an adjacent service monitor and knowledge-review pipeline.
- Closure path: A revise verdict returns to the authoring loop for repair. The reviewer sees the assembled draft and the same signal projection, and may only submit its verdict.
- Why this is / is not agent-owned: The reviewer has a separate session and genuine task-level feedback. It does not independently acquire operational evidence for reviewing a manager's representation of current work.
- Evidence: [agents/reviewer.py](https://github.com/stanGSA/ZhiMing/blob/9e092aecf37f9d7b92cbb22a67594721ce86b57b/agents/reviewer.py#L124-L137), [agents/reviewer.py](https://github.com/stanGSA/ZhiMing/blob/9e092aecf37f9d7b92cbb22a67594721ce86b57b/agents/reviewer.py#L161-L213), [common/tools.py](https://github.com/stanGSA/ZhiMing/blob/9e092aecf37f9d7b92cbb22a67594721ce86b57b/common/tools.py#L905-L947), [knowledge/reviews/README.md](https://github.com/stanGSA/ZhiMing/blob/9e092aecf37f9d7b92cbb22a67594721ce86b57b/knowledge/reviews/README.md#L1-L16), [ops/monitor.py](https://github.com/stanGSA/ZhiMing/blob/9e092aecf37f9d7b92cbb22a67594721ce86b57b/ops/monitor.py#L773-L824)
- Basis: Pinned first-party source inspection.
- Confidence: high
- Caveats: Finding is bounded to the pinned first-party operating surfaces.

### Absence scope

- Surfaces inspected: Review role and tool table, code validation, stored notes, health checks, and developer knowledge-corpus adjudication.
- Plausible first-party paths checked: Independent operational access outside the draft packet, and a findings-to-whole-current control return.
- Why no material first-party path remains: The available model review uses the same prepared consultation evidence. Independent deployment probes and content-release QA are distinct scopes and do not close an audit decision in the operating harness.

## S4 — Outside-and-then intelligence

- State: —
- Function: No prospective capability adoption loop was established for the installed consultation runtime.
- Disturbance / variety regulated: User profile, time-sensitive case inputs and underlying reference material can change.
- Decisive decision or feedback right: No distinct function-specific decision or feedback right was established.
- Decision owner: No distinct owner at the declared recursion.
- Supporting / enforcement mechanisms: Profile versioning, current calendar references, saved readings and a separately built versioned knowledge base.
- Closure path: Input/profile changes affect subsequent readings. Runtime consumes a published knowledge database.
- Why this is / is not agent-owned: The runtime updates current inputs and supports recall. Knowledge review and build operate on a maintainer release surface, with no bundled prospective runtime decision that adopts an organizational capability change.
- Evidence: [app.py](https://github.com/stanGSA/ZhiMing/blob/9e092aecf37f9d7b92cbb22a67594721ce86b57b/app.py#L146-L171), [app.py](https://github.com/stanGSA/ZhiMing/blob/9e092aecf37f9d7b92cbb22a67594721ce86b57b/app.py#L309-L332), [common/tools.py](https://github.com/stanGSA/ZhiMing/blob/9e092aecf37f9d7b92cbb22a67594721ce86b57b/common/tools.py#L971-L987), [config.yaml](https://github.com/stanGSA/ZhiMing/blob/9e092aecf37f9d7b92cbb22a67594721ce86b57b/config.yaml#L91-L105), [knowledge/reviews/README.md](https://github.com/stanGSA/ZhiMing/blob/9e092aecf37f9d7b92cbb22a67594721ce86b57b/knowledge/reviews/README.md#L1-L16)
- Basis: Pinned first-party source inspection.
- Confidence: high
- Caveats: Finding is bounded to the pinned first-party operating surfaces.

### Absence scope

- Surfaces inspected: Calendar and profile state, knowledge loading and build, maintainer verification and provider config.
- Plausible first-party paths checked: External intelligence generating next operating options, including knowledge edit/review/return and operator adoption.
- Why no material first-party path remains: The operating runtime loads reference data and handles current case variation. Corpus release and evaluation are adjacent developer processes, and forecasts are product outputs.

## S5 — Policy and identity

- State: —
- Function: No ultimate policy or identity settlement loop was established.
- Disturbance / variety regulated: Inputs can conflict with fixed scope and safety rules; a deployer can select a model or review strictness.
- Decisive decision or feedback right: No distinct function-specific decision or feedback right was established.
- Decision owner: No distinct owner at the declared recursion.
- Supporting / enforcement mechanisms: System prompts, shipped safety preflight, optional semantic judge, role boundaries and config switches.
- Closure path: The active turn observes the policies and can issue a restricted response, use the allowed route or stop.
- Why this is / is not agent-owned: These control concrete request handling under a predefined purpose. No supplied authority decides an identity/policy conflict and returns a newly authoritative operating policy.
- Evidence: [agents/orchestrator.py](https://github.com/stanGSA/ZhiMing/blob/9e092aecf37f9d7b92cbb22a67594721ce86b57b/agents/orchestrator.py#L1-L47), [app.py](https://github.com/stanGSA/ZhiMing/blob/9e092aecf37f9d7b92cbb22a67594721ce86b57b/app.py#L84-L146), [app.py](https://github.com/stanGSA/ZhiMing/blob/9e092aecf37f9d7b92cbb22a67594721ce86b57b/app.py#L255-L286), [app.py](https://github.com/stanGSA/ZhiMing/blob/9e092aecf37f9d7b92cbb22a67594721ce86b57b/app.py#L322-L353), [common/tools.py](https://github.com/stanGSA/ZhiMing/blob/9e092aecf37f9d7b92cbb22a67594721ce86b57b/common/tools.py#L886-L900)
- Basis: Pinned first-party source inspection.
- Confidence: high
- Caveats: Finding is bounded to the pinned first-party operating surfaces.

### Absence scope

- Surfaces inspected: System prompts, deployment config, safety handling and optional policy judge.
- Plausible first-party paths checked: Runtime owner or parent handling of conflicts over ultimate authority, including persistent operating identity and policy settings.
- Why no material first-party path remains: The source provides preset guard and mode selection, not an adjudication path for changes to the harness's ultimate purpose or authority.

## Recursion

The local consultation arrangement is the unit of analysis. Specialist sessions take role-scoped operational work inside one consultation. Infrastructure operators, source-content maintainers and an external MCP client's agent are separate recursions.

## Variety and escalation

The user receives an explicit missing-input or timeout outcome. Shared time and token limits attenuate contention before a request deadline. Separate deployment probes can emit alerts about service health without assigning decision authority in the consultation loop.

## Evidence gaps

Pinned source inspection only. This evaluates organizational architecture and does not validate predictive accuracy, clinical suitability, or live performance. No external provider or actual user data was used.

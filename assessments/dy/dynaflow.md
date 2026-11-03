---
harness_id: dynaflow
project_name: DynaFlow
repository: https://github.com/amiya-special/Dynaflow
review_ref: 7451639d197ef844b4157cf40eadac68e9eba8ca
reviewed_at: 2026-11-03
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-11-03
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# DynaFlow

## Review boundary

- System in focus: one local DynaFlow question/session using its shipped `dynamic` or `forced` multi-agent Workflow path, comprising the model-driven main agent, a model-generated JavaScript Workflow, the Docker-isolated TypeScript execution engine, Python host and model-driven subagent/tool service calls.
- Purpose and identity: enable a main reasoning model to design and supervise a per-question workflow that delegates substantive research and computation to independently invoked subagents and returns an evidence-bounded answer.
- Relevant environment: externally supplied questions, model API and tool results, tool failures, runtime resource limits, transport interruption, malformed subagent deliveries, missing data and the configured evaluation workload.
- Standard-distribution boundary: the MIT Python host (`src/dynaflow/workflow.py`, `runner.py`, `workflow_protocol.py`, `system_prompts.py`), bundled first-party main/worker role instructions, the MIT `workflow_runtime/src/engine/` TypeScript engine, tool service and Docker build; `dynamic`/`forced` are explicit supported modes.
- Credited operating / distribution surfaces: main model uses `Workflow`, `TaskOutput`, `TaskStop` to design, start, monitor, cancel or retry/resume a JavaScript subagent program; subagents receive role instructions and configured research/tool capabilities; engine validates output, manages a journal, concurrency, budget and delivery before finalization.
- Adjacent first-party surfaces excluded from ownership: `direct` model-only baseline, academic paper claims and evaluation/reporting scripts not running the workflow, model provider's internal reasoning/serving infrastructure, externally administered search/tool services, benchmark ground-truth grader and the developer/release organization. An external tool cannot be credited as an independently authorized DynaFlow S3* reviewer.
- Relevant modes / reachability: `dynamic` allows direct answer or a real workflow; `forced` requires successful subagent delivery; `direct` is inspected as a contrast, not evidence of multi-agent S2/S3. The runtime requires installed Node.js, Docker image and configured model/tool APIs; no default credentials are bundled.
- Recursion level: one question-local DynaFlow-managed workflow organization; individual model-driven subagent invocations are S1 operations and the model/host API are dependencies rather than imported full parent control organizations.
- Frozen source revision: `7451639d197ef844b4157cf40eadac68e9eba8ca`, observed 2026-11-03; Profile 0.2.4, released Skills assessment Methodology 0.3.7.

## Repository architecture

The Python question runner validates runtime dependencies and API availability, then starts a main agent equipped with the tools `Workflow`, `TaskOutput` and `TaskStop`. The main model chooses a direct route or writes and launches an inline JavaScript Workflow appropriate to the question. A Docker-isolated Node engine runs that script with a bounded `agent()` hook and journaling/resume; each subagent request crosses a narrow Python host bridge to the configured model and research tools. The engine records results and validates schemas/delivery. The main model reads completed or failed receipts and may revise/rerun the Workflow before answering. The host requires a valid workflow and at least one successful configured cloud subagent in a workflow-attempted path before it accepts a final answer. Concurrent subagent calls are limited by a shared semaphore and budget. Those resource guards and delivery-shape validators are not themselves separate autonomous management or independent substantive audit actors.

Pinned first-party evidence:

- [README: modes, runtime requirements and demo operating paths](https://github.com/amiya-special/Dynaflow/blob/7451639d197ef844b4157cf40eadac68e9eba8ca/README.md)
- [Main and subagent prompts and role interface](https://github.com/amiya-special/Dynaflow/blob/7451639d197ef844b4157cf40eadac68e9eba8ca/src/dynaflow/system_prompts.py)
- [Main role instruction: plan, monitor, assess returned results](https://github.com/amiya-special/Dynaflow/blob/7451639d197ef844b4157cf40eadac68e9eba8ca/src/dynaflow/assets/workflow_main.system.txt)
- [Forced Workflow policy and feedback/re-run guidance](https://github.com/amiya-special/Dynaflow/blob/7451639d197ef844b4157cf40eadac68e9eba8ca/src/dynaflow/assets/forced_prompt.txt)
- [Workflow orchestration, worker loop and host delivery gates](https://github.com/amiya-special/Dynaflow/blob/7451639d197ef844b4157cf40eadac68e9eba8ca/src/dynaflow/workflow.py)
- [Runner preflight, capacity, final status and recovery](https://github.com/amiya-special/Dynaflow/blob/7451639d197ef844b4157cf40eadac68e9eba8ca/src/dynaflow/runner.py)
- [Workflow engine: journal replay, subworkflow and terminal result](https://github.com/amiya-special/Dynaflow/blob/7451639d197ef844b4157cf40eadac68e9eba8ca/workflow_runtime/src/engine/runWorkflow.ts)
- [Agent hook: semaphore, budget, retry and result logging](https://github.com/amiya-special/Dynaflow/blob/7451639d197ef844b4157cf40eadac68e9eba8ca/workflow_runtime/src/engine/hooks.ts)
- [Delivery/schema validity checks](https://github.com/amiya-special/Dynaflow/blob/7451639d197ef844b4157cf40eadac68e9eba8ca/workflow_runtime/src/engine/deliveryValidation.ts)
- [Concurrency slots and cancellation](https://github.com/amiya-special/Dynaflow/blob/7451639d197ef844b4157cf40eadac68e9eba8ca/workflow_runtime/src/engine/concurrency.ts)

## Operational model

A question enters under a configured mode; in `forced` all substantive work must pass through a successfully completed Workflow and a configured subagent. The main model composes the task-specific workflow and supervises its current execution through tool status and result receipts. The model-driven workers perform actual information search, calculation or answer construction using only tools exposed by the Python host. Constructor-authored guardrails isolate workflow scripts, mediate credentials, limit concurrent agents, validate delivery and enforce the final-answer gate. Model-provider functionality and external tool results are operational dependencies, not an independent S3* function. This is a question-scoped coordination architecture, not an established persistent multi-project strategy/policy system.

## S1 — Operations

- State: A
- Function: a model-driven subagent interprets a delegated question subtask, chooses its own supported research/tool calls and produces a substantive answer or structured result.
- Disturbance / variety regulated: uncertain source material, changing factual evidence, calculations, research/tool response differences and errors in executing an assigned subproblem.
- Decisive decision or feedback right: choose how to query configured tools, reason about their actual outputs, retry task-local reasoning and deliver a substantive result to the workflow.
- Decision owner: the DynaFlow-managed subagent model invoked through `Session.worker` and the `agent()` hook; the independent model API service supplies computation but its unrelated internal policies are not borrowed.
- Supporting / enforcement mechanisms: `workflow_worker.system.txt` role constraints, model-compatible Chat Completions adapter, allowed tool schemas, Python `execute_tool` bridge, Docker credential isolation, output schema validation, journal and progress events.
- Closure path: main workflow delegates subtask → configured worker model interprets prompt and requests relevant tools → tool/model results return into its message history → final text/StructuredOutput is delivered or explicitly marked dead.
- Boundary reachability: `src/dynaflow/workflow.py` provides a real worker model-call loop and Python host tool execution, while `workflow_runtime/src/engine/hooks.ts` runs the worker and returns validated results to the JavaScript script in supported `dynamic`/`forced` modes.
- Why this is / is not agent-owned: the host cannot perform task-specific research/calculate the final substantive result by parsing the static workflow alone; the model-driven worker makes nontrivial task decisions.
- Evidence: pinned `src/dynaflow/workflow.py`, `src/dynaflow/system_prompts.py`, `workflow_runtime/src/engine/hooks.ts`, README mode table.
- Basis: explicit + structural.
- Confidence: high for reachable owned subagent execution, not for actual answer accuracy on unrun providers.
- Caveats: model serving and externally configured search APIs are separate providers; a default `direct` baseline is not the basis for counting multi-agent role ownership.

## S2 — Coordination

- State: —
- Function: no distinct lateral inter-S1 disturbance attenuation and return path beyond workflow scheduling/resource constraints is established.
- Disturbance / variety regulated: concurrent requests contend for a configured maximum number of execution slots and tokens, but no independent cross-worker semantic collision or negotiated working relationship is specified in the shipped path.
- Decisive decision or feedback right: the semaphore grants/reclaims permits, the engine numbers calls, and script dependencies order tasks; these are constructor-authored scheduling controls, not a supported S2 conflict-resolution right over peer S1 relations.
- Decision owner: static engine limits and caller-authored workflow script, not an identifiable lateral coordination agent.
- Supporting / enforcement mechanisms: `Semaphore.acquire/release`, global agent cap, shared budget, `Promise.all`-style workflow orchestration, journal sequence and cancellation.
- Closure path: one call awaits capacity and later proceeds when a permit is released; this closes a bounded scheduler resource constraint without showing disturbance-specific feedback changing separate S1 units' conflicting operations.
- Why this is / is not agent-owned: parallel execution and a concurrency cap do not automatically establish the S2 function; no source-evidenced first-party peer contention arbitration/reconciliation was identified.
- Distinct S1 units: the individually prompted subagents called by the generated workflow.
- Inter-S1 disturbance: potential competition for capacity or contradictory research outputs, but a distinct implemented peer conflict path is not shown.
- Attenuating coordination relation: configured semaphore and script dependency sequencing; neither is evidence of an S2-specific cross-worker conflict feedback loop.
- Feedback into subsequent S1 behaviour: a waiting slot delays launch, but no path-specific conflict ruling is carried to an already operating peer to regulate its subsequent activity.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: no S2-specific evidence survives this distinction; hence absence rather than an inflated S2=C score.
- Evidence: pinned `workflow_runtime/src/engine/concurrency.ts`, `hooks.ts`, `runWorkflow.ts`, `src/dynaflow/workflow.py`.
- Basis: bounded absence.
- Confidence: medium-high at the frozen shipped boundary.
- Caveats: a user-generated Workflow could voluntarily implement specialized peer coordination, but arbitrary user-authored scripts are not a guaranteed first-party function.

### Absence scope

- Surfaces inspected: JavaScript runtime concurrency/agent hooks, Python worker bridge, task launch/output, journal, JSON delivery and prompt-defined workflow interface.
- Plausible first-party paths checked: shared semaphore as conflict attenuation, dependent workflow phases as S2, worker-to-worker data joins as explicit peer negotiation, duplicate-agent results as a managed collision.
- Why no material first-party path remains: these paths gate scheduling and total resource use or synthesize outputs for one task; a supported distinct inter-operational interference path with returned corrective worker behavior is not demonstrated.

## S3 — Inside-and-now control

- State: A
- Function: the main model dynamically plans, launches, monitors, assesses and modifies the current subagent Workflow to complete the operator's question.
- Disturbance / variety regulated: failed subagents, incomplete/invalid delivery, insufficient evidence, changing research direction, stalled/aborted work and uncertain selection between direct and delegated execution.
- Decisive decision or feedback right: generate task-specific workflow scripts; choose serial/parallel subagent composition and verification stages; call `Workflow`/`TaskOutput`/`TaskStop`; revise or rerun workflow when receipts indicate incomplete or contradicted evidence; decide whether to synthesize the final answer.
- Decision owner: first-party-instructed main model in `Session.run`, in the supported dynamic/forced runtime; deterministic engine/host rules act as subordinate gates.
- Supporting / enforcement mechanisms: main role prompt, mode/forced policy, tool schemas and asynchronous `Session.launch/output`, status receipts, journal resume, bounded retries, deadline/cancel paths and host's valid-cloud-agent finalization predicate.
- Closure path: user question and current execution constraints → main model chooses/generates a Workflow → subagents work and send progress/results → `TaskOutput`/delivery/status returned → main model revises/reruns/stops or completes answer under immutable host acceptance rules.
- Boundary reachability: `src/dynaflow/assets/workflow_main.system.txt` and `forced_prompt.txt` require the described lead action; `src/dynaflow/workflow.py` exposes the actual tool calls, stores and returns receipts, and supports re-launch/resume and output blocking.
- Why this is / is not agent-owned: unlike the fixed semaphore or outer question queue, the model chooses and changes the task-specific subagent program and how to respond to unsatisfactory execution, giving it a bona fide current whole-workflow management right.
- Whole-system current view: active local Workflow invocations, completed run IDs/receipts, failed or valid delivery, current subagent responses and original question acceptance requirements.
- Current-control decision scope: question-local orchestration/recovery/answer readiness; not global resource governance over multiple independently funded projects or stable policy change.
- Evidence: pinned `src/dynaflow/workflow.py` (`Session.run`, `launch`, `output`), first-party main/forced prompts, `workflow_runtime/src/engine/runWorkflow.ts`.
- Basis: explicit + structural.
- Confidence: medium-high for the supported main-agent-in-the-loop operating mode.
- Caveats: actual use of the optional `dynamic` Workflow is conditional; in `direct`, no subagent organization exists. The model decides current workflow design, but cannot bypass host tool restriction, budget, delivery validity or user stop.

## S3* — Complementary audit

- State: —
- Function: no shipped separately tasked, independently evidenced challenge of an operating agent's correctness claim with a mandated corrective feedback return is established.
- Disturbance / variety regulated: malformed JSON, empty/invalid deliveries and model outputs lacking required successful-agent provenance are caught, but these are validity/reachability guards, not independent evidence-based challenge of substantive claims.
- Decisive decision or feedback right: constructor code checks schemas, transport receipts and whether a successful configured subagent delivered results; no distinct substantive reviewer actor is given a protected right to inspect contradicting primary evidence and return adjudicated findings.
- Decision owner: deterministic `validateAgentDelivery` and host finalization predicates for format/provenance; model-driven main agent may inspect results but is also author of the plan and final synthesis, not an independent assessor by default.
- Supporting / enforcement mechanisms: StructuredOutput JSON Schema, `validateDelivery`, `valid_cloud_agents`, `TaskOutput`, run journal and optional user-created script verification steps.
- Closure path: subagent output → schema/empty-result and successful-delivery checks → accepted/rejected receipt or current orchestration re-run; no default complementary channel challenges whether the answer is true against independently obtained source/acceptance evidence.
- Why this is / is not agent-owned: syntactic validation is constructor logic, and ad hoc optional model-generated verification does not establish a separate first-party audit mandate or epistemic independence.
- Claim being audited: supposed successful and correct response to the original research question.
- Ordinary reporting path: subagent task output/status delivered through the host.
- Complementary access path: no standard required reviewer with its own independent primary-source acquisition; the main model can read task outputs and optionally design a verification stage.
- Independence boundary: no deployed distinct reviewer identity, read-only isolation or mandatory independently sourced cross-check shown.
- Who acts on findings: the main agent may rerun after failed delivery, but that is ordinary current-control recovery without an independently warranted challenge verdict.
- Evidence: pinned `workflow_runtime/src/engine/deliveryValidation.ts`, `runWorkflow.ts`, `src/dynaflow/workflow.py`, `src/dynaflow/assets/workflow_main.system.txt`.
- Basis: bounded absence.
- Confidence: medium-high.
- Caveats: a specific generated script could use separate verification subagents and alter a future task-specific score, but existence of arbitrary script capability is not evidence of a shipped S3* audit loop.

### Absence scope

- Surfaces inspected: main/worker prompts, workflow output gate, JSON schema validation, result receipts and metadata, built-in hooks and independent model/tool service boundaries.
- Plausible first-party paths checked: main model revising failed Workflow as independent review, schema/provenance checks as an audit, optional verification stage inside user/model-generated JavaScript, benchmark evaluation as first-party S3*.
- Why no material first-party path remains: routine validity checking and the same main model's orchestration do not establish a separate mandated reviewer/evidence path or corrective challenge loop; external benchmark scoring is outside the running harness.

## S4 — Outside-and-then intelligence

- State: —
- Function: no ongoing first-party environment intelligence function that anticipates changes and modifies the longer-term capabilities/strategy of the DynaFlow work organization is established.
- Disturbance / variety regulated: novel user questions and alternate model research sources are present-work inputs, not demonstrated changes in future capability demand.
- Decisive decision or feedback right: model chooses an appropriate Workflow for a single question, and developers may change runtime code, but no bounded S4 agent authorizes prospective operating capability adaptations.
- Decision owner: question-local main model for current-work plan and external maintainers/users for updates or future workloads.
- Supporting / enforcement mechanisms: dynamically generated workflow scripts, run records, mode configuration and academic research documentation.
- Closure path: incoming question → generated current-work script → result; no current environmental trend → prospective adaptation proposal → installed new future organizational capability loop is evidenced.
- Why this is / is not agent-owned: dynamic *per-task* program generation is not automatically S4; the generated script executes and is discarded/archived as that task's procedure, rather than constituting a persistent policy/capability shift.
- Evidence: pinned README, `src/dynaflow/workflow.py`, `src/dynaflow/runner.py`, `workflow_runtime/src/engine/runWorkflow.ts`.
- Basis: bounded absence.
- Confidence: medium-high.
- Caveats: a human research team may analyze DynaFlow experiments to change later algorithms, outside this assessed runtime.

### Absence scope

- Surfaces inspected: dynamic/forced modes, script generation and retry, journal/resume, benchmark/reporting functions and repository research framing.
- Plausible first-party paths checked: model-generated programs as new long-term capabilities, journal replay as organizational learning, cross-question result analytics and research paper as an S4 operation.
- Why no material first-party path remains: the runtime applies its existing model and engine capabilities anew to a specific question, while experiment outputs and maintainer choices do not implement a first-party future strategy decision and return path.

## S5 — Policy and identity

- State: —
- Function: no internally closed legitimate ultimate identity/policy decision function for a DynaFlow installation is demonstrated.
- Disturbance / variety regulated: API credentials, allowed research tools, direct-versus-workflow policy, Docker capability restrictions, quotas and required delivery are fixed by constructor configuration/user mode.
- Decisive decision or feedback right: mode selection and engine constraints come from administrator/configuration; main model cannot rewrite the execution rules or determine ultimate purpose outside the supplied question.
- Decision owner: external deployer/evaluation owner and static constructor policy rather than an autonomous organization-level constitutional actor.
- Supporting / enforcement mechanisms: mode prompt, configured tool list, credential isolation, Docker network/privilege restrictions, budget/agent caps and STOP_BY_USER marker.
- Closure path: externally specified policy → enforced model/tool permissions and delivery constraints; no legitimate identity/ultimate-policy dispute is adjudicated and returned to govern the future organization.
- Why this is / is not agent-owned: obeying a forced mode and enforcing security restrictions are real constraints, but not first-party S5 political/identity decisions.
- Evidence: pinned `src/dynaflow/configuration.py`, `src/dynaflow/workflow.py`, `src/dynaflow/runner.py`, `src/dynaflow/assets/forced_prompt.txt`.
- Basis: bounded absence.
- Confidence: high for the narrow supplied runtime.
- Caveats: the paper authors and external academic laboratory have policy and strategy outside this executable product; these are not imported as its first-party S5.

### Absence scope

- Surfaces inspected: mode config, prompts, API/tool allowlist, Docker isolation, stop marker, task data and author/release metadata.
- Plausible first-party paths checked: main model as policy authority, self-generated Workflow as permission evolution, runtime security guards as constitution, research maintainers as a distributed parent S5.
- Why no material first-party path remains: all are either external human configuration, question-level execution decisions or static enforcement, lacking a source-supported ultimate-policy adjudication and binding return.

## Distributed OSS parent arrangement

Independent researchers or developers can clone and configure DynaFlow against their own APIs, tools and question sets. The academic project's authorship, model vendors and upstream TypeScript runtime license notices do not establish one first-party parent organization governing these independent installations via an S3/S4/S5 return mechanism.

## Recursion

One question/session is the bounded organization. Model-driven subagents are task-performing S1 units and the main model is an S3 current-work controller. Its asynchronous workflow/agent subcalls do not thereby become a separately observed peer S2 system or an independent S3* auditor. Research benchmark evaluators and provider deployments are outside assessed recursion.

## Variety and escalation

The main model reduces question complexity by deciding a workflow structure, delegating work to specialised worker calls and reading their receipts. Fixed agent, concurrency, budget, Docker/network and delivery guards constrain unsafe execution. Invalid or incomplete results return to current-work replanning and retry or fail closed. No separate lateral conflict control, independent corrective audit, future-capability management or ultimate policy return was established.

## Evidence gaps

- First-party repository source and bundled operating prompts were inspected at the frozen SHA; no API keys or Docker/model workload were run to prove model quality or empirical independence.
- The S3=A claim is bounded to `dynamic` when Workflow is chosen or `forced`, with model-generated workflow and receipt-driven control; the direct baseline is not counted.
- S2 absence specifically distinguishes a semaphore/shared budget from S2-specific inter-S1 collision attenuation; it does not claim workflows cannot ever contain domain-specific coordination.
- S3* absence distinguishes schema validity and optional script verification from an evidenced independent reviewer mandate.
- No external benchmark results, model service governance, user-written custom scripts or academic lab policy were imported as first-party organizational functions.

## Assessment summary

Proposed included at the shipped dynamic/forced multi-agent boundary: **A · — · A · — · — · —**. Model-driven workers own task-specific S1 and the main model owns current-work S3 orchestration/recovery. Concurrency permits and JSON delivery gates are insufficient to create a distinct lateral S2 or complementary S3* audit function; model-generated task plans and external configuration do not close S4/S5.

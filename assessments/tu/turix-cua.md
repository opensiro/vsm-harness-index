---
harness_id: turix-cua
project_name: TuriX-CUA
repository: https://github.com/TurixAI/TuriX-CUA
review_ref: 88c777bddfec9796667445873886a3563aa27246
reviewed_at: 2026-10-17
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# TuriX-CUA

## Review boundary

- System in focus: The frozen installable first-party macOS desktop computer-use Agent implementation, configured Brain/Actor/optional Planner/Memory model roles, macOS UI observation/actions via Controller, serial task loop, optional search/skills, in-run screenshot review and retained step-memory/resume facilities. One user's task/desktop session is the operational recursion.
- Purpose and identity: Autonomously perform user-provided macOS GUI tasks, interpreting on-screen evidence, choosing next procedural goal, selecting and executing UI actions until goal achieved or terminated.
- Relevant environment: macOS desktop state, user-installed applications, accessibility tree and screenshots, web content, human requests or login steps, configured model endpoints, optional search and skill instructions.
- Standard-distribution boundary: Source-shipped `Agent` Python class and `Agent.run(max_steps)` entry from `examples/main.py`, bundled Python macOS Controller/registry/mac actions, optional Planner, BrainSearchFlow and memory persistence, not commercial hosted model behavior, UI app internals, OpenClaw wrapper's outside orchestration or published demo performance.
- Credited operating / distribution surfaces: [examples/main.py](https://github.com/TurixAI/TuriX-CUA/blob/88c777bddfec9796667445873886a3563aa27246/examples/main.py); [examples/config.json](https://github.com/TurixAI/TuriX-CUA/blob/88c777bddfec9796667445873886a3563aa27246/examples/config.json); [src/agent/service.py](https://github.com/TurixAI/TuriX-CUA/blob/88c777bddfec9796667445873886a3563aa27246/src/agent/service.py); [src/agent/planner_service.py](https://github.com/TurixAI/TuriX-CUA/blob/88c777bddfec9796667445873886a3563aa27246/src/agent/planner_service.py); [src/agent/message_manager/service.py](https://github.com/TurixAI/TuriX-CUA/blob/88c777bddfec9796667445873886a3563aa27246/src/agent/message_manager/service.py); [src/agent/views.py](https://github.com/TurixAI/TuriX-CUA/blob/88c777bddfec9796667445873886a3563aa27246/src/agent/views.py); [src/agent/prompts.py](https://github.com/TurixAI/TuriX-CUA/blob/88c777bddfec9796667445873886a3563aa27246/src/agent/prompts.py); [src/controller/service.py](https://github.com/TurixAI/TuriX-CUA/blob/88c777bddfec9796667445873886a3563aa27246/src/controller/service.py); [src/controller/registry/service.py](https://github.com/TurixAI/TuriX-CUA/blob/88c777bddfec9796667445873886a3563aa27246/src/controller/registry/service.py); [src/mac/actions.py](https://github.com/TurixAI/TuriX-CUA/blob/88c777bddfec9796667445873886a3563aa27246/src/mac/actions.py); [src/mac/tree.py](https://github.com/TurixAI/TuriX-CUA/blob/88c777bddfec9796667445873886a3563aa27246/src/mac/tree.py); [src/utils/record_store.py](https://github.com/TurixAI/TuriX-CUA/blob/88c777bddfec9796667445873886a3563aa27246/src/utils/record_store.py); [src/utils/brain_search.py](https://github.com/TurixAI/TuriX-CUA/blob/88c777bddfec9796667445873886a3563aa27246/src/utils/brain_search.py).
- Adjacent first-party surfaces excluded from ownership: Marketing/model benchmarks/screenshots/GIF demos, optional OpenClaw skill wrapper and its external agent, remote 'turix-brain'/'turix-actor' hosted reasoning internals, external browser/app state and non-shipped server components. Explicit example runner demonstrates reachability but cannot donate a second whole-operation actor.
- First-party operating / deployment modes considered: Example-configured macOS model providers and main runnable Agent with/without UI tree, enabled/disabled optional Planner and skills/search, memory-budget compaction/resume, manual force-stop/human clarification. The standard Agent always uses Brain/Actor in one serial run.
- Recursion level: One first-party GUI automation run, not a company-wide autonomous agent team. The four model labels are functional roles inside one current operation rather than separate independently viable S1 departments.
- Reviewed revision: `88c777bddfec9796667445873886a3563aa27246` frozen #186 and current batch #1648 row 4.
- Observation date: 2026-10-17.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The executable `examples/main.py` creates configured provider-backed Brain/Actor and optional Planner/Memory LLMs, instantiates first-party `Agent`, and calls `Agent.run(max_steps)`. The Agent's runnable serial loop optionally loads memory/resume, checks failure/stop/pause flags, captures macOS screenshots and a relevant accessibility tree, asks Brain to evaluate the previous goal and choose `next_goal` from actual screen context, asks Actor for GUI actions, invokes `Controller.multi_act`, stores actions/results and loops until a done action, failure budget or max steps. This proves one model-guided sensory→action→feedback S1 task loop with first-party action execution. [examples/main.py](https://github.com/TurixAI/TuriX-CUA/blob/88c777bddfec9796667445873886a3563aa27246/examples/main.py); [src/agent/service.py](https://github.com/TurixAI/TuriX-CUA/blob/88c777bddfec9796667445873886a3563aa27246/src/agent/service.py); [src/controller/service.py](https://github.com/TurixAI/TuriX-CUA/blob/88c777bddfec9796667445873886a3563aa27246/src/controller/service.py).

Brain compares previous/current screenshots, persists a `step_evaluate` signal and selects a procedural next task, while Actor sees that same brain goal and screenshot and chooses keyboard/mouse/open-app actions; both answer to one common user task and are invoked sequentially by the same `Agent.run`. Planner optionally generates a **within-task** plan and skills/search context before run; Memory summarizes and retrieves within-run/historical context to keep the current problem tractable. The Controller binds generated commands to macOS APIs. None of these roles independently chooses inter-operational resource coordination, organizational operational commitments, an independent complementary audit, future product adaptation or ultimate policy. [src/agent/service.py](https://github.com/TurixAI/TuriX-CUA/blob/88c777bddfec9796667445873886a3563aa27246/src/agent/service.py); [src/agent/planner_service.py](https://github.com/TurixAI/TuriX-CUA/blob/88c777bddfec9796667445873886a3563aa27246/src/agent/planner_service.py); [src/agent/prompts.py](https://github.com/TurixAI/TuriX-CUA/blob/88c777bddfec9796667445873886a3563aa27246/src/agent/prompts.py); [src/agent/message_manager/service.py](https://github.com/TurixAI/TuriX-CUA/blob/88c777bddfec9796667445873886a3563aa27246/src/agent/message_manager/service.py); [src/utils/record_store.py](https://github.com/TurixAI/TuriX-CUA/blob/88c777bddfec9796667445873886a3563aa27246/src/utils/record_store.py).

`BrainSearchFlow` may retrieve saved task records, but this is task recall, not strategic environmental foresight. Human interaction is possible when Brain asks for login/unclear preferences; example main supports force-stop hotkey, and `Agent.stop`/failure budgets shut down one task run. This is user intervention over task execution, not documented first-party policy/identity governance. [src/utils/brain_search.py](https://github.com/TurixAI/TuriX-CUA/blob/88c777bddfec9796667445873886a3563aa27246/src/utils/brain_search.py); [src/agent/views.py](https://github.com/TurixAI/TuriX-CUA/blob/88c777bddfec9796667445873886a3563aa27246/src/agent/views.py); [examples/main.py](https://github.com/TurixAI/TuriX-CUA/blob/88c777bddfec9796667445873886a3563aa27246/examples/main.py).

## Operational model

User enters a desktop goal; optional Planner selects steps/skills to shape the agent prompt; Brain observes the actual macOS UI and decides the next goal; Actor picks concrete GUI actions; Controller executes them and captures results; Brain reviews the following screenshot/previous result to guide continuation. The loop is task-oriented, single-session, with saved memory and bounded max steps. Host macOS app execution and outside model inference are dependencies, not imported agents. No paid hosted run, benchmark performance or production reliability is asserted by this assessment.

## S1 — Operations

- State: A
- Function: First-party model-directed GUI task execution with observation/action/result feedback.
- Disturbance / variety regulated: Changing macOS screens, UI element locations, login prompts, incomplete subtasks, unexpected app responses and errors.
- Decisive decision or feedback right: Brain LLM interprets screenshots and chooses a current procedural goal; Actor LLM chooses corresponding GUI actions and arguments; first-party agent loop decides when to continue/stop on current outcome.
- Decision owner: One first-party `Agent` system implementing model-driven Brain/Actor decision turns; inference providers supply models, not an additional prebuilt external computer-use harness.
- Supporting / enforcement mechanisms: MacUITreeBuilder screenshot/accessibility capture, Controller action registry, structured output parser, task history, action results, failure/step limits, optional Planner/skills/search/memory.
- Closure path: GUI screenshot/previous action → Brain next_goal and analysis → Actor action JSON → installed Controller.multi_act executes on macOS → next screenshot/action history → Brain reevaluates and selects next goal.
- Boundary reachability: `examples/main.py` instantiates shipped `Agent` with supplied Brain/Actor/Memory and optional Planner models, and calls `Agent.run(max_steps)`; `run` loops `brain_step` and `actor_step`, which invokes first-party `Controller.multi_act`. No separate tool-providing external agent is required for this code path.
- Why this is / is not agent-owned: Models make concrete runtime choice of next goal and GUI actions; execution is not limited to static hard-coded macros. The orchestrator/Controller still enforce data/step/action bounds.
- Evidence: [examples/main.py](https://github.com/TurixAI/TuriX-CUA/blob/88c777bddfec9796667445873886a3563aa27246/examples/main.py); [src/agent/service.py](https://github.com/TurixAI/TuriX-CUA/blob/88c777bddfec9796667445873886a3563aa27246/src/agent/service.py); [src/agent/views.py](https://github.com/TurixAI/TuriX-CUA/blob/88c777bddfec9796667445873886a3563aa27246/src/agent/views.py); [src/controller/service.py](https://github.com/TurixAI/TuriX-CUA/blob/88c777bddfec9796667445873886a3563aa27246/src/controller/service.py); [src/mac/actions.py](https://github.com/TurixAI/TuriX-CUA/blob/88c777bddfec9796667445873886a3563aa27246/src/mac/actions.py).
- Basis: Source-level reachable model GUI observation/feedback loop.
- Confidence: High for source reachability; no external macOS/live-model execution attempted.
- Caveats: Requires macOS native frameworks and a working configured provider; real task performance not established.


## S2 — Coordination

- State: —
- Function: No first-party mutual attenuation of interference among distinct independently operating S1 units proven.
- Disturbance / variety regulated: A model Brain/Actor disagreement concerns one task's sequence and action quality, not a documented conflict among separate concurrent S1 units.
- Decisive decision or feedback right: No coordinator detecting and attenuating actual contention across separate worker tasks, desktop agents or resource reservations.
- Decision owner: One Agent's sequential execution scheduler, which passes single-task state between subroles.
- Supporting / enforcement mechanisms: Structured role outputs, action list, one-step loop, last-step history, optional plan and memory.
- Closure path: Result flows between Brain and Actor for the *same* task; no separate inter-S1 disturbance → coordination choice → changed sibling activity feedback path evidenced.
- Why this is / is not agent-owned: Brain, Actor, Memory and Planner are model calls in a single operation. Distinct LLM configurations do not create distinct organizational S1 operations.
- Evidence: [src/agent/service.py](https://github.com/TurixAI/TuriX-CUA/blob/88c777bddfec9796667445873886a3563aa27246/src/agent/service.py); [src/agent/planner_service.py](https://github.com/TurixAI/TuriX-CUA/blob/88c777bddfec9796667445873886a3563aa27246/src/agent/planner_service.py); [src/agent/message_manager/service.py](https://github.com/TurixAI/TuriX-CUA/blob/88c777bddfec9796667445873886a3563aa27246/src/agent/message_manager/service.py); [examples/main.py](https://github.com/TurixAI/TuriX-CUA/blob/88c777bddfec9796667445873886a3563aa27246/examples/main.py).
- Basis: Bounded negative structural search at frozen default distribution.
- Confidence: Medium-high.
- Caveats: An external multi-agent system may run multiple instances but its coordination is not supplied by this pinned core.

### Absence scope

- Surfaces inspected: Agent.run/brain_step/actor_step, optional Planner, Controller action queue, saved history and OpenClaw wrapper.
- Plausible first-party paths checked: Model role separation, Brain→Actor handoff, plan/skill steps, action throttling and stop flags.
- Why no material first-party path remains: No first-party concurrently regulated distinct S1 units or concrete cross-unit conflict that this shipped run attenuates was identified.


## S3 — Inside-and-now control

- State: —
- Function: No separately owned current whole-system commitments/resources regulation beyond the one task's own planner/controller.
- Disturbance / variety regulated: Current GUI subgoal failure, incomplete plan steps, retries and model output errors within one operational task.
- Decisive decision or feedback right: Brain chooses current next goal and optional Planner composes current user's task; no actor chooses among organization-wide competing active tasks, priorities, resources or responsibilities.
- Decision owner: One task-level Brain/Actor agent; user supplies task, and deterministic loop enforces max steps/failure cap.
- Supporting / enforcement mechanisms: Current screenshot evaluation, Planner plan generation, pause/stop controls, max failures/steps.
- Closure path: Next goal → individual task action → next task observation, not separate whole-operational control → reallocation/return across concurrent operational units.
- Why this is / is not agent-owned: Brain is a task planner/evaluator, not whole-system S3 despite 'planner' labels, and the task's bounded loop is not a delegated operational-management position.
- Evidence: [src/agent/service.py](https://github.com/TurixAI/TuriX-CUA/blob/88c777bddfec9796667445873886a3563aa27246/src/agent/service.py); [src/agent/planner_service.py](https://github.com/TurixAI/TuriX-CUA/blob/88c777bddfec9796667445873886a3563aa27246/src/agent/planner_service.py); [examples/config.json](https://github.com/TurixAI/TuriX-CUA/blob/88c777bddfec9796667445873886a3563aa27246/examples/config.json).
- Basis: Bounded negative review of decisive assignment and resource authority.
- Confidence: Medium-high within declared single-run operational recursion.
- Caveats: Additional multi-agent orchestration in an external OpenClaw runtime is not credited to TuriX-CUA.

### Absence scope

- Surfaces inspected: Agent.run control flow, Brain evaluation/next_goal, Planner.edit_task, Controller, failure counters, user intervention.
- Plausible first-party paths checked: Brain's in-task control, Planner planning and skill selection, pause/stop and human login/request signals.
- Why no material first-party path remains: None observes and regulates a real whole of independent present operational commitments or allocations.


## S3* — Complementary audit

- State: —
- Function: No independent complementary access/challenge of operational claims plus corrective return separate from ordinary execution was evidenced.
- Disturbance / variety regulated: Action success/failure and changed UI state are ordinary primary task feedback.
- Decisive decision or feedback right: The same Brain that determines next task decisions also judges previous-step screenshot success; Controller returns local action results, not an independently owned auditor verdict.
- Decision owner: Within-task Brain/model and deterministic controller/result parser.
- Supporting / enforcement mechanisms: Screenshot comparisons, `step_evaluate`, saved action histories, action errors and in-task memory summaries.
- Closure path: Actor executes → Brain sees next screenshot and self-checks → Brain picks task continuation. This is first-party S1 feedback, not an alternative independent auditor collecting separately scoped operational evidence.
- Why this is / is not agent-owned: Prompt-separated Brain versus Actor gives functional division but same run/controller authority. A different model role alone is not enough to demonstrate independent audit rights.
- Evidence: [src/agent/service.py](https://github.com/TurixAI/TuriX-CUA/blob/88c777bddfec9796667445873886a3563aa27246/src/agent/service.py); [src/agent/prompts.py](https://github.com/TurixAI/TuriX-CUA/blob/88c777bddfec9796667445873886a3563aa27246/src/agent/prompts.py); [src/agent/views.py](https://github.com/TurixAI/TuriX-CUA/blob/88c777bddfec9796667445873886a3563aa27246/src/agent/views.py); [src/controller/service.py](https://github.com/TurixAI/TuriX-CUA/blob/88c777bddfec9796667445873886a3563aa27246/src/controller/service.py).
- Basis: Bounded negative ownership/independence comparison.
- Confidence: Medium-high.
- Caveats: A user can manually inspect a GUI, but no shipped agent-independent audit return is evidenced.

### Absence scope

- Surfaces inspected: Brain previous-goal `step_evaluate`, Actor action results, screenshot state, messages and saved history.
- Plausible first-party paths checked: Separate Brain/Actor LLM roles, visual step verification, memory snapshots, tool execution errors.
- Why no material first-party path remains: The checks are part of the ordinary same-task action selection/feedback path without a distinct corrective reviewer with complementary evidence and control return.


## S4 — Outside-and-then intelligence

- State: —
- Function: No supported external prospective change-of-organizational-capability option and return loop.
- Disturbance / variety regulated: Unseen webpage changes and task uncertainty are current operational disturbances; model/GUI capabilities are specified through configured endpoints/skills.
- Decisive decision or feedback right: Optional Planner may search or choose a skill for the present user task; Memory compresses/retrieves prior action context. Neither chooses/testing a new future capability for the harness and returns it to subsequent operation.
- Decision owner: Task-driven model roles and operator-managed code/skill/model settings.
- Supporting / enforcement mechanisms: PlannerSearch and skill selection, Memory LLM summaries, record persistence and resumed action history.
- Closure path: Search/record → better present task steps; no current-capability evidence → prospective alternatives → adaptation selection/application → later organizational operation closure.
- Why this is / is not agent-owned: Learning a webpage or summarizing an execution trace is not future adaptation of the computer-use organization's capability.
- Evidence: [src/agent/planner_service.py](https://github.com/TurixAI/TuriX-CUA/blob/88c777bddfec9796667445873886a3563aa27246/src/agent/planner_service.py); [src/agent/service.py](https://github.com/TurixAI/TuriX-CUA/blob/88c777bddfec9796667445873886a3563aa27246/src/agent/service.py); [src/utils/skills.py](https://github.com/TurixAI/TuriX-CUA/blob/88c777bddfec9796667445873886a3563aa27246/src/utils/skills.py); [src/utils/record_store.py](https://github.com/TurixAI/TuriX-CUA/blob/88c777bddfec9796667445873886a3563aa27246/src/utils/record_store.py).
- Basis: Bounded review of optional planning/search/memory and configured skills.
- Confidence: Medium-high.
- Caveats: The operator could install new skills manually outside the runtime; not evidence of an installed S4.

### Absence scope

- Surfaces inspected: Planner optional search/skills, BrainSearchFlow, Memory summarization, persisted records, model provider settings.
- Plausible first-party paths checked: Planning/search before a task, iterative plan refinement, retained experience and skill library use.
- Why no material first-party path remains: No first-party future-facing organizational adaptation options tested/selected/returned to current controller as lasting capability changes.


## S5 — Policy and identity

- State: —
- Function: No ultimate identity/policy decision rights or returned resolution for the computer-use system.
- Disturbance / variety regulated: Human login/preferences, step-stop limits, model instructions and selected provider/tool capabilities are task-level constraints.
- Decisive decision or feedback right: Operator chooses starting task and may cancel; Brain `ask_human` asks for clarification. No supported actor decides system-wide ultimate ethos/identity conflict and returns binding policy.
- Decision owner: Human task originator and externally maintained software settings; no function-specific S5 owner evidenced in the shipped harness.
- Supporting / enforcement mechanisms: User task prompt, `ask_human`, pause/stop and force-stop hotkey, configured model API and skills.
- Closure path: User clarifies an input or cancels a task; there is no independent policy controversy → ultimate authority decision → policy return to organization.
- Why this is / is not agent-owned: Static prompts/user approval do not equal agent-owned or parent-governed S5 under the active Methodology.
- Evidence: [src/agent/views.py](https://github.com/TurixAI/TuriX-CUA/blob/88c777bddfec9796667445873886a3563aa27246/src/agent/views.py); [src/agent/service.py](https://github.com/TurixAI/TuriX-CUA/blob/88c777bddfec9796667445873886a3563aa27246/src/agent/service.py); [examples/main.py](https://github.com/TurixAI/TuriX-CUA/blob/88c777bddfec9796667445873886a3563aa27246/examples/main.py); [examples/config.json](https://github.com/TurixAI/TuriX-CUA/blob/88c777bddfec9796667445873886a3563aa27246/examples/config.json).
- Basis: Bounded negative source review of human and task authority.
- Confidence: Medium-high.
- Caveats: A deploying organization may have its own user approval policy, outside the credited system.

### Absence scope

- Surfaces inspected: Run entry, model/system prompts, human question field, stop/cancel controls and provider/tool configuration.
- Plausible first-party paths checked: Task ownership, role/memory selection, user clarifications, policy language in prompts.
- Why no material first-party path remains: No runtime-reachable independent ultimate policy/identity settlement actor or binding organization-level return.


## Distributed OSS parent arrangement

Open-source authors, model vendors and a possibly external OpenClaw controller remain separate owners. This source assesses the ordinary deployed macOS task-loop, not the repository's maintainer governance. User control over task inputs and stop does not itself demonstrate parent-owned S3, S4 or S5 functions.

## Self-hosted and non-human modes

TuriX-CUA runs in a macOS process and accepts provider models through LangChain; examples configure named brain/actor/planner/memory models and optional search/skills. It can persist conversation/memory and resume a stopped task with an explicit ID. A force-stop hotkey and task clarification are supported in the example runner. These do not add autonomous inter-S1 control or an independent reviewer.

## Recursion

Brain and Actor exchange task goals and action plans at one S1 operation. Planner and Memory supply support to this same operation. The desktop/macOS app and provider models remain its environment; a separate orchestrator capable of coordinating multiple concurrent TuriX agents could be a higher-level system but is not evidenced here.

## Variety and escalation

Screenshots, accessibility tree and model reasoning amplify ability to handle shifting GUI variety. Controller actions and runtime loops attenuate task-specific uncertainty through step evaluation and memory. Requests to a human for access/clarification are ordinary S1 escalation, not a separately proven whole-system authority path. No claim of protected action sandbox or independent audit gate is made.

## Evidence gaps

- macOS GUI/Quartz and external LLM endpoints were not run; code-level paths establish installed functional capacity, not task success, benchmark scores or risk safety guarantees.
- The config may use separate LLM products for Brain/Actor/Planner/Memory but no distinct independently regulated S1 organizational units or S2 interference-resolution mechanism is demonstrated.
- Brain screenshot reevaluation is a same-task control check and does not evidence independent complementary S3* audit.
- Skills, prior-task records, search and memory do not establish organizational future S4; user stop/ask_human and model configuration are not S5.
- All `—` states are bounded negative source conclusions for the frozen first-party distribution and assessed one-run recursion, not assertions of universal impossibility.

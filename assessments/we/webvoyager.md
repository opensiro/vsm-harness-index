---
harness_id: webvoyager
project_name: WebVoyager
repository: https://github.com/MinorJerry/WebVoyager
review_ref: 5a7896738c10bfb8b9edccce6bb0e0411f8ae569
reviewed_at: 2026-10-30
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

# WebVoyager

## Review boundary

- System in focus: the published WebVoyager online web-navigation harness, from a dataset-provided natural-language website task through Selenium browser observation, model-selected page actions and answer/iteration termination. The documented `run.py` task loop is the first-party system boundary.
- Purpose and identity: complete a bounded web task by visually or textually observing a live page and choosing navigation/interaction actions until an answer or a limit/error.
- Relevant environment: changing DOM/text/visual page layout, interactive elements, remote web sites, downloads/PDFs, selector changes, browser exceptions and model API errors.
- Standard-distribution boundary: root [`run.py`](https://github.com/MinorJerry/WebVoyager/blob/5a7896738c10bfb8b9edccce6bb0e0411f8ae569/run.py), [`utils.py`](https://github.com/MinorJerry/WebVoyager/blob/5a7896738c10bfb8b9edccce6bb0e0411f8ae569/utils.py), [`utils_webarena.py`](https://github.com/MinorJerry/WebVoyager/blob/5a7896738c10bfb8b9edccce6bb0e0411f8ae569/utils_webarena.py), [`prompts.py`](https://github.com/MinorJerry/WebVoyager/blob/5a7896738c10bfb8b9edccce6bb0e0411f8ae569/prompts.py), documented [`README.md`](https://github.com/MinorJerry/WebVoyager/blob/5a7896738c10bfb8b9edccce6bb0e0411f8ae569/README.md) and launch script. Includes screenshot/set-of-mark and optional text-only accessibility-tree modes, one ChromeDriver per task.
- Credited operating / distribution surfaces: root task iteration in `run.py` (`main`, `call_gpt4v_api`, `exec_action_click`, `exec_action_type`, `exec_action_scroll`), live browser state capture and parsing helpers in `utils.py`/`utils_webarena.py`, static task prompts in `prompts.py` and CLI args.
- Adjacent first-party surfaces excluded from ownership: `evaluation/auto_eval.py` and `evaluation/run_eval.sh` benchmark judging, `results/examples/` saved samples, manually supplied task datasets and repository maintenance. External GPT-4V/OpenAI endpoint, Selenium/Chrome implementation, real websites and PDF Assistant API remain dependencies rather than first-party organizational decision owners.
- First-party operating / deployment modes considered: screenshot/image model messages with visual numbered element tags; optional `--text_only` using accessibility tree; optional `--headless`; bounded `max_iter` with retries of model HTTP calls. No live browser, model endpoint, PDF assistant or website transaction was exercised in this source-only assessment.
- Recursion level: one web task-solving cell. The runner processes multiple dataset tasks sequentially and does not establish multiple concurrent autonomous suborganizations.
- Reviewed revision: `5a7896738c10bfb8b9edccce6bb0e0411f8ae569`; observation 2026-10-30; generated/current Profile 0.2.4 and Methodology 0.3.7.

## Repository architecture

`run.py::main` reads JSONL tasks, starts ChromeDriver on each provided website, constructs an image or accessibility-tree observation, sends the running task/history to the configured GPT model, parses `Thought:` and `Action:`, and runs one of `click`, `type`, `scroll`, `goback`, `google`, `wait`, `answer`. The action may change real browser state. Next loop iteration re-reads the page; malformed model output or Selenium error can produce a corrective warning and another model call. A PDF download optionally invokes a separate Assistant API to supply extracted answer text as a new observation; it is a task information-gathering affordance, not independent governance or audit. `max_iter` caps attempts, and output screenshots/messages/logs are persisted for each task. Evaluation utilities are outside this runtime loop.

## Operational model

The task result is a final answer or an incomplete/failed web interaction. Model discretion selects the target element, action and continuation against environmental observations; Python handles deterministic browser calls, visual labeling, error strings and scheduling. One task's browser is closed before the next ChromeDriver starts. A benchmark score or offline stored transcript cannot donate a second organizational S3/S3*/S4 function without an in-run corrective decision path.

## S1 — Operations

- State: A
- Function: perform environment-facing browser navigation and information retrieval to satisfy an incoming web task.
- Disturbance / variety regulated: dynamic page content, clickable-element labels, web forms, navigation paths, downloads, dialog state, selector failures and incomplete answers.
- Decisive decision or feedback right: the model chooses `click`/`type`/`scroll`/`goback`/`google`/`wait`/`answer`, selecting element labels/content and revising its next action from screenshots/trees and error feedback.
- Decision owner: first-party model-backed step decision loop in `run.py`; the externally hosted model supplies text/vision inferences but the repository wires their decisions into executable browser actions.
- Supporting / enforcement mechanisms: Selenium ChromeDriver, visual set-of-mark tags, accessibility-tree parser, model completion API wrapper, action parser, fixed `max_iter` and exception handling.
- Closure path: task + live screenshot/tree → model action → browser mutation and new observation/warning → next model action or final answer.
- Boundary reachability: `run.sh`/documented root `run.py` enters this while-loop for each task, executes selected actions and re-observes the browser before the next choice.
- Why this is / is not agent-owned: the first-party decision path uses model-chosen actions and returns environment feedback; the Selenium routines have no independent discretion over which site/element to visit.
- Evidence: [`run.py`](https://github.com/MinorJerry/WebVoyager/blob/5a7896738c10bfb8b9edccce6bb0e0411f8ae569/run.py) (`main` observation/model/action loop, `exec_action_*`, error branch); [`utils.py`](https://github.com/MinorJerry/WebVoyager/blob/5a7896738c10bfb8b9edccce6bb0e0411f8ae569/utils.py) (visual observation and action parsing).
- Basis: structural.
- Confidence: high for wired decision/feedback path; not empirical success.
- Caveats: browser actions are not safety-reviewed; the code was read, not run on any real site.

## S2 — Coordination

- State: —
- Function: no inter-S1 interference attenuation at the selected single-task agent boundary.
- Disturbance / variety regulated: model-selected browser actions can affect the current page, but no two distinct simultaneously operating S1 cells or conflicting resource claims are established.
- Decisive decision or feedback right: static per-task loop sequences one model action and one Selenium execution; it does not negotiate or arbitrate a collision among independent operational cells.
- Decision owner: one model-driven browser task cell and fixed Python action dispatcher.
- Supporting / enforcement mechanisms: iteration counter, per-task driver initialization/quit, browser window switching, screenshot element labels and retry messages.
- Closure path: a selected action changes the same task's browser; there is no separate conflict-resolution feedback to another operational unit.
- Boundary reachability: `for task_id in range(len(tasks))` processes task episodes in series, each using one `driver_task` and one action-at-a-time loop.
- Why this is / is not agent-owned: one agent's self-correction and sequential use of the browser is S1 operation, not S2 coordination among separately autonomous units.
- Evidence: [`run.py`](https://github.com/MinorJerry/WebVoyager/blob/5a7896738c10bfb8b9edccce6bb0e0411f8ae569/run.py) (`main` task loop, `while it < args.max_iter`, action branches, `driver_task.quit`).
- Basis: structural.
- Confidence: medium-high for documented runner; alternative external multi-instance deployments are outside scope.
- Caveats: a system operator can launch separate processes, but no first-party coordination relation among them is shown.

### Absence scope

- Surfaces inspected: main loop, browser/action handlers, screenshots and accessibility-tree support, task iteration, download/PDF handling, launch script and README.
- Plausible first-party paths checked: multiple JSONL tasks, browser windows/tabs, per-task driver creation, action parsing, retry on driver error and saving per-task logs.
- Why no material first-party path remains: tasks are handled serially in separate drivers; window/tab switches and one task's action retries are not multiple S1 cells with a specific inter-cell collision and attenuating return path.

## S3 — Inside-and-now control

- State: —
- Function: no demonstrated whole-service current control or commitment/resource bargaining over several operations.
- Disturbance / variety regulated: browser tasks may be costly, slow, unreliable or blocked, but the harness uses fixed iteration/model retry thresholds and static CLI options.
- Decisive decision or feedback right: `max_iter` and API retry caps terminate or retry a *single* task; no actor receives a whole-system current view and chooses cross-task resource/priority/commitment interventions.
- Decision owner: operator-defined CLI limits and deterministic Python branches, not autonomous or substantive deterministic S3 authority.
- Supporting / enforcement mechanisms: `max_iter`, token/cost logging, API retries, `time.sleep`, task directory output and ChromeDriver shutdown.
- Closure path: limits stop individual tasks, error strings prompt S1 retry; no global performance control decision returns to running subordinate cells.
- Boundary reachability: limits run in the published source, but they enforce startup bounds rather than a separate whole-current managerial function.
- Why this is / is not agent-owned: an action controller and per-task retry mechanism do not constitute whole-organizational resource balancing just because they orchestrate a loop.
- Evidence: [`run.py`](https://github.com/MinorJerry/WebVoyager/blob/5a7896738c10bfb8b9edccce6bb0e0411f8ae569/run.py) (`main` args, loop, `call_gpt4v_api` retry cap).
- Basis: structural.
- Confidence: medium.
- Caveats: no external multi-task scheduler or hosted system-management console is inside the assessed repository boundary.

### Absence scope

- Surfaces inspected: root runner, model-call wrapper, Selenium action handlers, costs/logging, task file input and result persistence.
- Plausible first-party paths checked: `max_iter`, token usage tracking, fixed model retry, per-task task directory and sequential task list.
- Why no material first-party path remains: none aggregates current system commitments and owns a meaningful allocation/priority/accountability decision across operational cells with returned intervention.

## S3* — Complementary audit

- State: —
- Function: no in-run independent complementary audit of browser task completion claims.
- Disturbance / variety regulated: a model can report an incorrect answer or wrong page, but the shipped task loop does not cross-check the report through independent sampled ground truth.
- Decisive decision or feedback right: screenshots, DOM-derived labels and download/PDF Assistant results are ordinary task observations; the `answer` action ends the task without an independent verification gate.
- Decision owner: ordinary S1 model and deterministic environment observation; `evaluation/auto_eval.py` is a separate offline benchmark artifact rather than an in-run audit owner.
- Supporting / enforcement mechanisms: task screenshots, saved interaction messages, per-task logs, PDF assistant information extraction and benchmark evaluation directory.
- Closure path: an error/warning can enter the next model step; there is no separate audit verdict to whole-system control capable of overturning a declared completion.
- Why this is / is not agent-owned: even if the PDF Assistant is model-powered, it returns requested task content, not a complementary operational audit; an offline benchmark judge cannot be promoted to S3* inside the runtime.
- Evidence: [`run.py`](https://github.com/MinorJerry/WebVoyager/blob/5a7896738c10bfb8b9edccce6bb0e0411f8ae569/run.py) (`answer` branch, PDF handling, logging); [`evaluation/auto_eval.py`](https://github.com/MinorJerry/WebVoyager/blob/5a7896738c10bfb8b9edccce6bb0e0411f8ae569/evaluation/auto_eval.py) (adjacent evaluator).
- Basis: structural.
- Confidence: medium-high for distribution boundary.
- Caveats: whether an external benchmark evaluates transcripts has no bearing on runtime audit ownership without an actual return-to-control path.

### Absence scope

- Surfaces inspected: main task-answer loop, screenshot/DOM capture, PDF Assistant call, persisted messages/screenshots, `evaluation/` scripts and sample results.
- Plausible first-party paths checked: PDF answer extraction as second model, model retry after malformed action, task transcript logging and standalone automatic benchmark assessment.
- Why no material first-party path remains: none inspects S1 claims through a sufficiently independent, complementary reality channel and returns findings into active S3/current control; all runtime checking is ordinary task feedback.

## S4 — Outside-and-then intelligence

- State: —
- Function: no prospective external environment intelligence updating the harness's continuing operating capability.
- Disturbance / variety regulated: websites change across browser actions, but the agent adapts its *current navigation* by taking a fresh screenshot/tree after each action.
- Decisive decision or feedback right: the model chooses the next web action for the same task; it does not build a future web ecosystem model, compare prospective adaptation options or update enduring harness strategy.
- Decision owner: task-level model for navigation, developer/operator for future prompts, browser/model deployment and code revisions.
- Supporting / enforcement mechanisms: message history, screenshot clipping, static prompt, max iterations, saved examples and benchmark scripts.
- Closure path: new web observation returns to current S1 action; no S4-to-S3 assessed future option returns to current installation/capability.
- Why this is / is not agent-owned: reactive re-navigation after an external event is operational correction and does not establish outside-and-then intelligence.
- Evidence: [`run.py`](https://github.com/MinorJerry/WebVoyager/blob/5a7896738c10bfb8b9edccce6bb0e0411f8ae569/run.py) (`format_msg`, `main` messages/loop); [`prompts.py`](https://github.com/MinorJerry/WebVoyager/blob/5a7896738c10bfb8b9edccce6bb0e0411f8ae569/prompts.py).
- Basis: structural.
- Confidence: medium-high.
- Caveats: web browsing could surface external future information for a user task; the reviewed harness does not itself perform prospective organizational adaptation.

### Absence scope

- Surfaces inspected: vision and text-only task runs, prompt templates, message history, web/download observations, example output persistence, benchmark resources.
- Plausible first-party paths checked: iterative page re-observation, different website/task inputs, Google navigation action, PDF content retrieval and output logs.
- Why no material first-party path remains: all paths are bounded within one task or offline research, with no prospective environment model, adaptation-option decision or two-way current-control return to lasting capability.

## S5 — Policy and identity

- State: —
- Function: no legitimate ultimate-policy/identity authority exercised inside the shipped task runner.
- Disturbance / variety regulated: allowed sites, credentials and browser settings can affect safety and task scope, but these are supplied before run and not policy questions resolved by the harness.
- Decisive decision or feedback right: user/operator supplies `test_file`, API key, model, Chrome settings and iteration cap; the model chooses within-task browser actions without ultimate-governance escalation.
- Decision owner: external operator/developer and task model for local choices; no recognized first-party policy owner with parent decision return.
- Supporting / enforcement mechanisms: static SYSTEM_PROMPT, CLI configuration, iteration cap, browser preferences and API call limits.
- Closure path: startup configuration conditions task execution, but there is no path for an identity or ultimate-policy issue to reach ratifying authority and return as a governing change.
- Why this is / is not agent-owned: a system prompt and launch-time constraints do not constitute policy identity or legitimate S5 decision rights.
- Evidence: [`run.py`](https://github.com/MinorJerry/WebVoyager/blob/5a7896738c10bfb8b9edccce6bb0e0411f8ae569/run.py) (argument setup and runner); [`prompts.py`](https://github.com/MinorJerry/WebVoyager/blob/5a7896738c10bfb8b9edccce6bb0e0411f8ae569/prompts.py).
- Basis: structural.
- Confidence: medium.
- Caveats: user authorization for real web transactions and repository owner governance are separate concerns outside this script's claimed autonomy.

### Absence scope

- Surfaces inspected: task runner, prompts, CLI settings, browser actions, exception handling, optional PDF assistant and evaluation scripts.
- Plausible first-party paths checked: model `Thought`/`Action`, user task instructions, action enumeration, fixed retry/iteration guard and developer-owned config.
- Why no material first-party path remains: no legitimate identity/policy-level matter is routed to an ultimate authority and closed into subsequent runtime constraints or purpose.

## Distributed OSS parent arrangement

Repository maintainers and experiment operators control releases, prompts and datasets, but there is no first-party runtime parent/child policy escalation-and-return path. These external roles cannot donate S5(P) or S3(P) just because the repository is public.

## Self-hosted and non-human modes

Chrome can run headlessly, and a configured remote model selects page actions without per-action human approval. The presence of an OpenAI API key and Selenium capability does not grant independent organizational policy rights; no live transaction was conducted for this review.

## Recursion

The model, Selenium browser, PDF retrieval helper and task loop perform complementary stages for one operational outcome. The sequential task list is not a multi-S1 metasystem, and no child has separate sufficient governance identity to establish nested VSM viability.

## Variety and escalation

Screenshot/set-of-mark or accessibility-tree representations attenuate complex web-page variety into navigable candidates; the model amplifies action selection. Browser errors and formatting failures re-enter the same S1 feedback loop. Fixed API retries, iteration limits and saved logs are not proof of whole-system algedonic channels or policy escalation.

## Evidence gaps

- No live browser, real website action, GPT-4V request, PDF Assistant call or benchmark evaluator was executed; the assessment concerns source-wired capability, not measured task completion.
- The `evaluation/` automatic judge is adjacent to the runtime; no evidence was found that its verdict intercepts the `answer` branch or controls subsequent task execution.
- The runner processes tasks sequentially; separately launched copies may collide externally, but the repository does not implement first-party cross-copy coordination.

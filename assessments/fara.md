---
harness_id: fara
project_name: Fara
repository: https://github.com/microsoft/fara
review_ref: a675d6d61c41c47ae87bacefeab22caad18e3e84
reviewed_at: 2026-10-17
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

# Fara

## Review boundary

- System in focus: First-party open Fara Python computer-use agent/CLI, especially the shipped Fara-1.5 `Fara15Agent`, PlaywrightEnvironment/browser action controller, RunContext/trajectory checkpointing and human critical-point/resume path. The modeled operating unit is a single user-directed browser task, not a multi-project research/evaluation organization.
- Purpose and identity: Turn a user request into bounded autonomous browser screenshots, model-selected computer-use operations and observable website-state changes; pause for human information or approval where configured.
- Relevant environment: Website DOM/screenshots, browser navigation and form content, user task/approval, Playwright/browser runtime, configured local/hosted model API, CAPTCHA challenges, other web services.
- Standard-distribution boundary: Installable `fara-cli` 1.5 operational path and included computer-use code, with older Fara-7B packaged compatible path assessed only for boundary completeness; excludes model training, weights/benchmarks, external Magentic-UI project, benchmark evaluator and provider-managed services.
- Credited operating / distribution surfaces: [src/fara/run_fara.py](https://github.com/microsoft/fara/blob/a675d6d61c41c47ae87bacefeab22caad18e3e84/src/fara/run_fara.py); [src/fara/agents/fara/fara15_agent.py](https://github.com/microsoft/fara/blob/a675d6d61c41c47ae87bacefeab22caad18e3e84/src/fara/agents/fara/fara15_agent.py); [src/fara/agents/fara/_prompts.py](https://github.com/microsoft/fara/blob/a675d6d61c41c47ae87bacefeab22caad18e3e84/src/fara/agents/fara/_prompts.py); [src/fara/core/agent.py](https://github.com/microsoft/fara/blob/a675d6d61c41c47ae87bacefeab22caad18e3e84/src/fara/core/agent.py); [src/fara/core/run_context.py](https://github.com/microsoft/fara/blob/a675d6d61c41c47ae87bacefeab22caad18e3e84/src/fara/core/run_context.py); [src/fara/core/data_point.py](https://github.com/microsoft/fara/blob/a675d6d61c41c47ae87bacefeab22caad18e3e84/src/fara/core/data_point.py); [src/fara/environments/playwright/environment.py](https://github.com/microsoft/fara/blob/a675d6d61c41c47ae87bacefeab22caad18e3e84/src/fara/environments/playwright/environment.py); [src/fara/environments/playwright/playwright_controller.py](https://github.com/microsoft/fara/blob/a675d6d61c41c47ae87bacefeab22caad18e3e84/src/fara/environments/playwright/playwright_controller.py); [src/fara/agents/fara/fara_types.py](https://github.com/microsoft/fara/blob/a675d6d61c41c47ae87bacefeab22caad18e3e84/src/fara/agents/fara/fara_types.py); [pyproject.toml](https://github.com/microsoft/fara/blob/a675d6d61c41c47ae87bacefeab22caad18e3e84/pyproject.toml).
- Adjacent first-party surfaces excluded from ownership: The `webeval/` evaluator, benchmark `MMRubricAgent`, CUAVerifierBench, WebTailBench, published models/datasets and reported success rates; these evaluate *task trajectories* outside the active Fara-1.5 CLI production run. Magentic-UI's own approvals/audit/sandbox, when configured externally, are not borrowed into Fara. Remote model weights and browser/app internal decision makers are external.
- First-party operating / deployment modes considered: Standard `fara-cli` Playwright Fara-1.5, configurable base_url/endpoint and max_rounds, headless/headed browser, optional Browserbase environment, user reply on `ask_user_question`, resume from in-memory ongoing `Fara15AgentState`; legacy Fara-7B runner and benchmark evaluator checked as possible alternative, not promoted into primary run.
- Recursion level: A single browser automation operation in one task-run. Model calls, browser-controller action functions and checkpoint artifacts are not separate viable autonomous S1 suborganizations.
- Reviewed revision: `a675d6d61c41c47ae87bacefeab22caad18e3e84`, frozen by intake #186 and batch #1648 row 5.
- Observation date: 2026-10-17.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The first-party packaged `fara-cli` sets up `PlaywrightEnvironment` and a configured `Fara15Agent`, creates a `RunContext` and loops over user tasks. The agent `initialize` builds the model client and validates its configured mode/identity against an approved **static** registry. In `Fara15Agent.run`, a bounded `max_rounds` loop captures the screenshot plus page context, asks the configured LLM for a browser function call, executes it with first-party `_execute_action` over the Playwright environment, reads post-screenshot and page data, logs action/observation, checkpoints and repeats. The model chooses a meaningful browser action conditioned on real feedback: first-party S1 model/tool closure. [src/fara/run_fara.py](https://github.com/microsoft/fara/blob/a675d6d61c41c47ae87bacefeab22caad18e3e84/src/fara/run_fara.py); [src/fara/agents/fara/fara15_agent.py](https://github.com/microsoft/fara/blob/a675d6d61c41c47ae87bacefeab22caad18e3e84/src/fara/agents/fara/fara15_agent.py); [src/fara/environments/playwright/environment.py](https://github.com/microsoft/fara/blob/a675d6d61c41c47ae87bacefeab22caad18e3e84/src/fara/environments/playwright/environment.py).

A model-selected `ask_user_question` action sets `SolverStatus.WAITING_FOR_USER`; the CLI receives the response as `CRITICAL_POINT_RESPONSE` and invokes the **same agent and context** to resume without discarding preceding chat history. The supplied system prompt describes missing personal data, under-specified tasks and unauthorized irreversible actions as reasons to pause and ask. This is a concrete **task-level operator consent loop**; its trigger depends on model compliance with prompt, not universal independently enforced prevention of irreversible GUI actions. Configured `auto_user_reply` can bypass the wait and auto-approve. Consequently, this path should not be treated as robust whole-organization S3/S5 parent authority or independent audit. [src/fara/agents/fara/fara15_agent.py](https://github.com/microsoft/fara/blob/a675d6d61c41c47ae87bacefeab22caad18e3e84/src/fara/agents/fara/fara15_agent.py); [src/fara/agents/fara/_prompts.py](https://github.com/microsoft/fara/blob/a675d6d61c41c47ae87bacefeab22caad18e3e84/src/fara/agents/fara/_prompts.py); [src/fara/run_fara.py](https://github.com/microsoft/fara/blob/a675d6d61c41c47ae87bacefeab22caad18e3e84/src/fara/run_fara.py).

`RunContext` stores events, screenshot paths, verdict/solver status and checkpoints for one task. Shared Context is not an inter-S1 coordination arrangement. The published `webeval/` tooling can independently judge trajectories *offline* and reported benchmark work includes a Universal Verifier, but Fara's actual `Fara15Agent.run` does not call it to challenge operational claims and feed a corrective/retry decision into the deployed run. The higher-level external Magentic-UI product has its own boundaries and cannot confer first-party S3* evidence on this source. [src/fara/core/run_context.py](https://github.com/microsoft/fara/blob/a675d6d61c41c47ae87bacefeab22caad18e3e84/src/fara/core/run_context.py); [src/fara/core/data_point.py](https://github.com/microsoft/fara/blob/a675d6d61c41c47ae87bacefeab22caad18e3e84/src/fara/core/data_point.py); [src/fara/agents/fara/fara15_agent.py](https://github.com/microsoft/fara/blob/a675d6d61c41c47ae87bacefeab22caad18e3e84/src/fara/agents/fara/fara15_agent.py); [webeval/README.md](https://github.com/microsoft/fara/blob/a675d6d61c41c47ae87bacefeab22caad18e3e84/webeval/README.md); [README.md](https://github.com/microsoft/fara/blob/a675d6d61c41c47ae87bacefeab22caad18e3e84/README.md).

## Operational model

An operator provides a user goal, supported LLM endpoint and browser context. Fara captures a browser screenshot, generates a concrete action, executes mouse/keyboard/browser functions, re-reads page/visual state, and continues until termination or max rounds. If the model decides an information/authorization critical point is reached, the same task is held until the user replies (or the task is abandoned). Stored trajectory records allow inspection, but no independent operational auditor or VSM management layer is demonstrated. The open Fara runtime is evaluated; the hosted frontier model, benchmark judges and external GUI host are outside this first-party boundary.

## S1 — Operations

- State: A
- Function: Autonomous first-party visual browser-task execution, with model-selected action responses to real environment feedback.
- Disturbance / variety regulated: Changing websites, unknown navigation, forms, state-dependent GUI controls, unexpected browser responses and missing task information.
- Decisive decision or feedback right: Configured model decides actual computer-use function/action and arguments after observing screenshot plus task/interaction history; installed agent determines continuation, bounded exit and task-level human-response resume.
- Decision owner: First-party `Fara15Agent` model/action feedback loop; configured model API supplies inference but not a separately authored organization.
- Supporting / enforcement mechanisms: PlaywrightEnvironment screenshots/page context, action schema/parser, `RunContext` event log, model client, max rounds, optional CAPTCHA waiting and user ask path.
- Closure path: task + screenshot → model-picked browser action → first-party browser controller executes → post-screenshot/page context saved → model observes result next turn / completes task.
- Boundary reachability: The packaged `run_fara15_agent` CLI constructs PlaywrightEnvironment/Fara15Agent/RunContext and directly calls `agent.run`; the run code executes first-party browser actions and checkpoints feedback. The same Fara instance resumes after a task-critical user reply.
- Why this is / is not agent-owned: Concrete website action is selected online from observations by the model, not statically replayed scripted macro. Browser/tool/controller scaffolding remains deterministic and bounded.
- Evidence: [src/fara/run_fara.py](https://github.com/microsoft/fara/blob/a675d6d61c41c47ae87bacefeab22caad18e3e84/src/fara/run_fara.py); [src/fara/agents/fara/fara15_agent.py](https://github.com/microsoft/fara/blob/a675d6d61c41c47ae87bacefeab22caad18e3e84/src/fara/agents/fara/fara15_agent.py); [src/fara/environments/playwright/playwright_controller.py](https://github.com/microsoft/fara/blob/a675d6d61c41c47ae87bacefeab22caad18e3e84/src/fara/environments/playwright/playwright_controller.py); [src/fara/core/run_context.py](https://github.com/microsoft/fara/blob/a675d6d61c41c47ae87bacefeab22caad18e3e84/src/fara/core/run_context.py).
- Basis: Implemented and CLI-wired first-party source trace, not downstream model benchmark.
- Confidence: High for reachable model-guided S1 path; no hosted inference result reproduced.
- Caveats: A configured endpoint is required; model may fail to comply with safety prompts, and no live web-task success is asserted.


## S2 — Coordination

- State: —
- Function: No first-party inter-S1 interference/oscillation attenuation between distinct operational browser agents identified.
- Disturbance / variety regulated: One browser task's tool/state challenges are S1 execution uncertainty, not demonstrated interaction between two independently operating S1 units.
- Decisive decision or feedback right: No distinct sibling-agent contention/resource coordination decision in shipped Fara CLI.
- Decision owner: One Fara15Agent task loop and Playwright runtime.
- Supporting / enforcement mechanisms: Single-tab browser setting, serial model actions, controller action execution and screenshot checkpoints.
- Closure path: Page observation returns to the *same* operating agent; no cross-agent conflict → coordination response → changed sibling action feedback path.
- Why this is / is not agent-owned: Single-tab mode, API rate limits and sequential tool actions do not by themselves supply multi-S1 coordination.
- Evidence: [src/fara/run_fara.py](https://github.com/microsoft/fara/blob/a675d6d61c41c47ae87bacefeab22caad18e3e84/src/fara/run_fara.py); [src/fara/agents/fara/fara15_agent.py](https://github.com/microsoft/fara/blob/a675d6d61c41c47ae87bacefeab22caad18e3e84/src/fara/agents/fara/fara15_agent.py); [src/fara/environments/playwright/environment.py](https://github.com/microsoft/fara/blob/a675d6d61c41c47ae87bacefeab22caad18e3e84/src/fara/environments/playwright/environment.py).
- Basis: Bounded negative first-party code path assessment.
- Confidence: High for standard CLI scope.
- Caveats: Another installed multi-agent orchestration framework might add S2 but that is a different system-in-focus.

### Absence scope

- Surfaces inspected: Fara15Agent.run, run_fara15_agent, PlaywrightEnvironment, RunContext, legacy Fara7B path.
- Plausible first-party paths checked: Multiple configured function calls, browser tab synchronization, task states and persistence.
- Why no material first-party path remains: No shipped current-task mode coordinates two distinct operational S1s or regulates a concrete inter-S1 collision.


## S3 — Inside-and-now control

- State: —
- Function: No separate, whole-system current operational controller over multiple independent ongoing browser commitments, priorities or resources.
- Disturbance / variety regulated: Task ambiguity/irreversibility and current GUI step completion are addressed by the same single-task model/operator interaction.
- Decisive decision or feedback right: The browser task model chooses current actions; user can confirm a critical action or provide missing details. These decisions do not regulate commitments of multiple S1 operational units.
- Decision owner: Single Fara15Agent and task operator; static max-rounds/run boundaries.
- Supporting / enforcement mechanisms: `WAITING_FOR_USER` task-status, task-time human input, controller run checkpoints and prompt-level critical-points rules.
- Closure path: User prompt/approval → resume same S1 action; no separately owned whole-current regulatory decision → revised organization-wide active work commitments.
- Why this is / is not agent-owned: Pausing before an irreversible browser action is current-task consent, not parent-owned S3 for a team or deployment.
- Evidence: [src/fara/agents/fara/fara15_agent.py](https://github.com/microsoft/fara/blob/a675d6d61c41c47ae87bacefeab22caad18e3e84/src/fara/agents/fara/fara15_agent.py); [src/fara/run_fara.py](https://github.com/microsoft/fara/blob/a675d6d61c41c47ae87bacefeab22caad18e3e84/src/fara/run_fara.py); [src/fara/agents/fara/_prompts.py](https://github.com/microsoft/fara/blob/a675d6d61c41c47ae87bacefeab22caad18e3e84/src/fara/agents/fara/_prompts.py).
- Basis: Bounded negative of current-control ownership at one browser-task recursion.
- Confidence: Medium-high.
- Caveats: If an external Magentic-UI instance schedules multiple Fara runs, its management is outside this repo's own CLI system.

### Absence scope

- Surfaces inspected: Fara15Agent user critical-point path, RunContext, CLI loop, static action identity and max_rounds.
- Plausible first-party paths checked: WAITING_FOR_USER, user approvals and browser control, persistence and task succession.
- Why no material first-party path remains: No shipped first-party actor allocates/changes a whole of distinct present S1 commitments or operational resources.


## S3* — Complementary audit

- State: —
- Function: No sufficiently independent complementary auditor with operational corrective return in first-party runtime.
- Disturbance / variety regulated: A browser action may fail or a task output may be unreliable, but ordinary screenshots/tool results return to S1 model and log.
- Decisive decision or feedback right: No separate first-party operational reviewer inspects raw artifacts/evidence and can challenge ordinary Fara model completion with a corrective return.
- Decision owner: Same Fara15Agent for task updates; optional offline benchmark evaluator is outside the installed normal execution path.
- Supporting / enforcement mechanisms: Saved trajectory events and screenshots, `webeval/` benchmark judge, external Magentic-UI optional integrations.
- Closure path: Trajectories are stored for later evaluation, but an auditor verdict is not fed into `Fara15Agent.run` to correct next actions or govern completion in the direct CLI path.
- Why this is / is not agent-owned: Benchmark `MMRubricAgent` and human-labelled CUAVerifierBench can evaluate tasks but do not by mere repo proximity create a shipped operational S3* function.
- Evidence: [src/fara/agents/fara/fara15_agent.py](https://github.com/microsoft/fara/blob/a675d6d61c41c47ae87bacefeab22caad18e3e84/src/fara/agents/fara/fara15_agent.py); [src/fara/core/run_context.py](https://github.com/microsoft/fara/blob/a675d6d61c41c47ae87bacefeab22caad18e3e84/src/fara/core/run_context.py); [webeval/README.md](https://github.com/microsoft/fara/blob/a675d6d61c41c47ae87bacefeab22caad18e3e84/webeval/README.md); [README.md](https://github.com/microsoft/fara/blob/a675d6d61c41c47ae87bacefeab22caad18e3e84/README.md).
- Basis: Negative source check separating operational runner from evaluation-only adjacent pipeline.
- Confidence: Medium-high for direct Fara-1.5 CLI.
- Caveats: A separately deployed Magentic-UI might add its own independent audit rights; do not transfer them.

### Absence scope

- Surfaces inspected: Fara15Agent state/action/result flow, RunContext verification fields, webeval metric/verifier code and external Magentic-UI documentation.
- Plausible first-party paths checked: Trajectory evaluator, screenshot logging, critical-point human confirmation and model self-observation.
- Why no material first-party path remains: No operationally reachable independent alternative audit evidence source with binding corrective return to the deployed browser-agent task.


## S4 — Outside-and-then intelligence

- State: —
- Function: No installed future-oriented organizational capability-adaptation options and return to present control.
- Disturbance / variety regulated: Current webpage changes, user information and general web search task facts.
- Decisive decision or feedback right: Agent makes actions for current task; model training/paper updates and benchmark scores are upstream research, not installed agent decisions about adapting future operating capabilities.
- Decision owner: External model authors/developers for training/versions and user task model for immediate browser activity.
- Supporting / enforcement mechanisms: Chat history, screenshots, saved trajectories, model endpoint configuration and evaluation scripts.
- Closure path: No external future capability distinctions → chosen/tested organizational adaptation → installed behavior change → subsequent operating return at assessed Fara task recursion.
- Why this is / is not agent-owned: Model weights having been trained or published bench results does not imply runtime S4 behavior.
- Evidence: [src/fara/agents/fara/fara15_agent.py](https://github.com/microsoft/fara/blob/a675d6d61c41c47ae87bacefeab22caad18e3e84/src/fara/agents/fara/fara15_agent.py); [README.md](https://github.com/microsoft/fara/blob/a675d6d61c41c47ae87bacefeab22caad18e3e84/README.md); [webeval/README.md](https://github.com/microsoft/fara/blob/a675d6d61c41c47ae87bacefeab22caad18e3e84/webeval/README.md).
- Basis: Bounded negative review of operational vs benchmark/model-development paths.
- Confidence: High for installed CLI scope.
- Caveats: Research teams may update model versions externally; that is not an owned task-runtime adaptation path.

### Absence scope

- Surfaces inspected: Agent runtime/history, endpoint configurations, model changelog/README, webeval evaluator.
- Plausible first-party paths checked: Model improvement/training, trajectory scoring, step history, configurable endpoints.
- Why no material first-party path remains: No observed runtime actor generating/testing/selecting prospective organization-level capability changes for later task operation.


## S5 — Policy and identity

- State: —
- Function: No first-party ultimate identity/ethos/policy conflict settlement beyond static agent-role restrictions and user-specific task consent.
- Disturbance / variety regulated: Missing user data, ambiguous tasks, irreversible web submissions, action/schema identity mismatches.
- Decisive decision or feedback right: User may authorize irreversible present action or supply personal detail. Static mode/identity prompt registry guards action types; no distinct ultimate-policy authority with governance return.
- Decision owner: Task user and first-party model/controller according to static prompt; no runtime S5 policy function.
- Supporting / enforcement mechanisms: Critical-point prompt, `ask_user_question` model action, WAITING_FOR_USER state, identity validator, model task/input state.
- Closure path: Task confirmation/input → resume same browser operation; no whole-system value/identity dispute → ultimate settlement → returned binding institution-level policy.
- Why this is / is not agent-owned: Safety-oriented user approval is welcome, but on a single task it does not confer an identity/policy governance role.
- Evidence: [src/fara/agents/fara/_prompts.py](https://github.com/microsoft/fara/blob/a675d6d61c41c47ae87bacefeab22caad18e3e84/src/fara/agents/fara/_prompts.py); [src/fara/agents/fara/fara15_agent.py](https://github.com/microsoft/fara/blob/a675d6d61c41c47ae87bacefeab22caad18e3e84/src/fara/agents/fara/fara15_agent.py); [src/fara/run_fara.py](https://github.com/microsoft/fara/blob/a675d6d61c41c47ae87bacefeab22caad18e3e84/src/fara/run_fara.py).
- Basis: Bounded negative source examination of critical-point and identity paths.
- Confidence: Medium-high.
- Caveats: `auto_user_reply` can automatically continue without a real person; prompt-only critical-point compliance is not an enforcement guarantee.

### Absence scope

- Surfaces inspected: Model identity validation, critical point prompt, ask_user_question logic, user task API/CLI and external Magentic-UI reference.
- Plausible first-party paths checked: Irreversible-action approval, user policy instructions, model identity registry and interactive authorization.
- Why no material first-party path remains: No first-party ultimate organizational policy decision/return loop; user answers govern one task action.


## Distributed OSS parent arrangement

The Microsoft project publishes both model-weight references and a first-party Python runner. The owner of weights, external Magentic-UI runtime and benchmark validators is not assumed to operate the same first-party organizational function in the CLI. Its human critical-point path is a limited task-approval relation and not evidence that the external vendor or a separate institutional security officer governs S3/S5 in the assessed task organization.

## Self-hosted and non-human modes

Users can point `fara-cli` to a local model-serving endpoint or hosted model API and run headless Playwright or selected Browserbase-backed browser. The run may pause and resume on a model-requested critical-point with user feedback; `auto_user_reply` is an alternative unsafe automatic response mode, so the model prompt is not a hard universal approval gate. Single-task autonomy and human task intervention remain distinct from VSM metasystem responsibility.

## Recursion

The operational S1 is one browser-task execution loop. Model, Playwright environment, UI actions, chat history and persistent RunContext are components of that operation. Neither an offline trajectory evaluation pipeline nor an externally installed multi-agent host constitutes an in-repo S2–S5 organization merely because both are referenced in README.

## Variety and escalation

The model amplifies browser action variety using screenshots and action choices; bounded rounds, action whitelist/schema, Playwright errors and task-level questions attenuate some present environment uncertainty. User authorization may constrain irreversible actions, but the trigger is model/prompt dependent and does not establish a separate auditable S3* enforcement layer. No prospective adaptive S4 or ultimate S5 mechanism found.

## Evidence gaps

- This was a source-level review only, with exact frozen Git SHA; no live provider/browser run, actual purchase/action approval or benchmark replication performed.
- A user critical-point is prompted by the model and may be auto-replied depending on configuration; this is not claimed as a universal independently enforced safety barrier.
- `webeval/` and verifier datasets do not connect to the normal CLI `Fara15Agent.run` decision return; do not credit their judges as operational S3*.
- S2, S3, S3*, S4 and S5 negative results are **bounded to the installed first-party browser-task recursion**, not claims of universal impossibility or of what external Magentic-UI does.

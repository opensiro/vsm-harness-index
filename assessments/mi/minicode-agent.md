---
harness_id: minicode-agent
project_name: MiniCode Agent
repository: https://github.com/BlairCode/minicode-agent
review_ref: 0c8bf466f2c1163403906253f2dc8be862fb828c
reviewed_at: 2026-11-06
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

# MiniCode Agent

## Review boundary

- System in focus: the shipped local MiniCode Agent Python application at the frozen `BlairCode/minicode-agent` revision, including its own model/tool execution runtime, Coding and LeetCode task modes, context management, built-in workspace tools, local safety/approval enforcement, session history, and CLI/Web entry points.
- Purpose and identity: complete user-directed coding, debugging, file-editing, command-execution, and algorithm tasks in a bounded local workspace through an iterative model-selected tool loop.
- Relevant environment: the user's task, local project/workspace files, command and test results, model service responses, user approvals/cancellations, context size and tool failures.
- Standard-distribution boundary: `main.py` creates the first-party `Application`, whose `AgentRuntime` is reached by the CLI or local Web controller. Qwen/DashScope or another OpenAI-compatible inference endpoint, user project, OS subprocesses, and human operator are external actors. The runtime's Python agent loop and local tools are first party; the remote model supplies decision-making inference but is not a third-party agent framework or a separate hosted harness.
- Credited operating / distribution surfaces: `main.py`; `minicode_agent/app.py`; `agent/runtime.py`, `manager.py`, `context.py`, `state.py`, `stop.py`; `llm/client.py`; `tools/`; `safety/`; `session.py`; `cli/console.py`; `web/controller.py` and `web/server.py`; supported Coding/LeetCode prompts and bundled skills loaded into the runtime.
- Adjacent first-party surfaces excluded from ownership: `tests/`, GitHub Actions CI, repository-development/release activity, README screenshots and assets, and the user's target repository. Tests corroborate implementation behavior but do not become a second runtime/auditor or acquire organization-wide authority.
- First-party operating / deployment modes considered: default local Web UI with independent per-conversation workspaces, CLI with Coding/LeetCode modes, multi-turn continuation, optional command approval modes (`strict`, `ask`, `full`), local history, cancellation and bounded retries. `review` is an algorithm task mode, not an independently deployed audit function.
- Recursion level: a single user-directed agent session/task organization; Web-hosted concurrent conversations are separate sessions, not evidenced coordinated operational subsidiaries of a shared higher-level autonomous coding organization.
- Reviewed revision: `0c8bf466f2c1163403906253f2dc8be862fb828c`.
- Observation date: 2026-11-06.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.7`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.7`.

## Repository architecture

`Application.create_runtime` constructs one `AgentRuntime` from an `AgentSpec`, model adapter, `ContextManager`, `StopPolicy`, `ToolRegistry`/`ToolDispatcher`, file and command tools, workspace/path policy, and command approval. Coding and LeetCode are alternative prompts/tool-enabled task modes using the same loop, not a team of cooperating agents. The runtime passes the current context and tool schemas to an external inference service; the model selects a tool or final answer; dispatch validates the tool and arguments; tool results are appended for the next decision. Retry, cancellation, step/error limits, tool access and path/command approvals are deterministic enforcement around those decisions.

CLI requests execute that shared runtime directly. The Web controller creates one workspace/runtime per conversation, starts a worker thread for a turn, presents events and approvals, and can restore limited context from local history. A per-conversation lock prevents a simultaneous second turn in that conversation. The session recorder writes redacted events; the Web UI shows ordinary progress/results. These are persistence, isolation and operator-control mechanisms, not independently deciding regulators or auditors.

Skills are static bundled prompt material loaded when the runtime is created. The operator can change settings and approve or deny risky commands; the model does not own the approval policy or the application's ultimate identity. No production-wired multi-agent delegation, distinct S1 coordination, whole-system current-control actor, complementary auditor, prospective adaptation loop or identity-policy adjudication is exposed in the reviewed distribution.

Primary source:

- [README and supported modes](https://github.com/BlairCode/minicode-agent/blob/0c8bf466f2c1163403906253f2dc8be862fb828c/README.md)
- [`Application.create_runtime`](https://github.com/BlairCode/minicode-agent/blob/0c8bf466f2c1163403906253f2dc8be862fb828c/minicode_agent/app.py)
- [`AgentRuntime` model/tool loop](https://github.com/BlairCode/minicode-agent/blob/0c8bf466f2c1163403906253f2dc8be862fb828c/minicode_agent/agent/runtime.py)
- [`AgentManager` task-mode specs](https://github.com/BlairCode/minicode-agent/blob/0c8bf466f2c1163403906253f2dc8be862fb828c/minicode_agent/agent/manager.py)
- [`WebController` conversations and approvals](https://github.com/BlairCode/minicode-agent/blob/0c8bf466f2c1163403906253f2dc8be862fb828c/minicode_agent/web/controller.py)

## Operational model

One model-backed agent performs a user's coding or algorithm task by selecting reads, writes, patches, searches or commands, observing actual tool results and deciding what to do next. The deterministic runtime may reject a tool, ask the human to approve a risky operation, retry a model call, truncate context, stop after errors or cancel a run. The decision about the task-specific next coding action and final response remains with the model-backed agent. Distinct Web conversations have isolated workspaces, but no first-party shared objective, cross-session bargaining or inter-agent operational hierarchy is evidenced.

## S1 — Operations

- State: A
- Function: carry out environment-facing software/algorithm tasks through an iterative agent-directed observe–act–observe loop.
- Disturbance / variety regulated: varying user requirements, unknown file contents, editing and execution failures, command/tool output, context pressure and model failures.
- Decisive decision or feedback right: select the next task-specific coding tool and arguments, revise the plan after tool observations, or finish with an answer.
- Decision owner: the model-backed Coding or LeetCode agent in the supported runtime session.
- Supporting / enforcement mechanisms: first-party model adapter, tool schemas and dispatcher, file/command tools, workspace/path policy, user approval, context truncation, stop/retry limits and event recording.
- Closure path: user task and accumulated observations → model tool/final decision → first-party dispatcher and approved tool execution → actual result/error added to model context → next model decision or completed response.
- Boundary reachability: `main.py` routes CLI to `run_console` and Web to `WebController`; both call `Application.create_runtime`, which instantiates and runs the shipped model/tool loop. No external agent framework is needed to supply the loop.
- Why this is / is not agent-owned: removing the model-backed actor leaves tool dispatch and safety controls, but no actor choosing task-specific edits, commands or iterative correction. Deterministic guards enforce bounds; the model owns the operational discretion.
- Evidence: [`agent/runtime.py`](https://github.com/BlairCode/minicode-agent/blob/0c8bf466f2c1163403906253f2dc8be862fb828c/minicode_agent/agent/runtime.py); [`llm/client.py`](https://github.com/BlairCode/minicode-agent/blob/0c8bf466f2c1163403906253f2dc8be862fb828c/minicode_agent/llm/client.py); [`tools/dispatcher.py`](https://github.com/BlairCode/minicode-agent/blob/0c8bf466f2c1163403906253f2dc8be862fb828c/minicode_agent/tools/dispatcher.py); [`app.py`](https://github.com/BlairCode/minicode-agent/blob/0c8bf466f2c1163403906253f2dc8be862fb828c/minicode_agent/app.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: a live remote model/API credential is required for inference and riskier commands may require operator approval. Neither requirement substitutes a third-party coding-agent harness for the first-party S1 loop.

## S2 — Coordination

- State: —
- Function: no material first-party coordination relation among distinct operational S1 cells is established at this single-session task recursion.
- Disturbance / variety regulated: potential concurrent-session workspace overlap is bounded by separate workspaces; no shared task/team inter-S1 disturbance with an attenuating joint decision/feedback loop is demonstrated.
- Decisive decision or feedback right: no cross-S1 coordination discretion or conflict-resolution right established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: per-conversation workspace directories and locks, single-run execution, one selected `AgentSpec` per runtime, tool serialization and context grouping.
- Closure path: per-conversation isolation prevents concurrent turns from re-entering one run, but no coordination result changes the later behavior of multiple distinct S1 units working toward one common outcome.
- Why this is / is not agent-owned: Coding and LeetCode are alternate modes; Web conversations run independently. Neither mode selection nor workspace isolation establishes agent-owned S2 regulation.
- Evidence: [`agent/manager.py`](https://github.com/BlairCode/minicode-agent/blob/0c8bf466f2c1163403906253f2dc8be862fb828c/minicode_agent/agent/manager.py); [`agent/runtime.py`](https://github.com/BlairCode/minicode-agent/blob/0c8bf466f2c1163403906253f2dc8be862fb828c/minicode_agent/agent/runtime.py); [`web/controller.py`](https://github.com/BlairCode/minicode-agent/blob/0c8bf466f2c1163403906253f2dc8be862fb828c/minicode_agent/web/controller.py).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: adding independently operating coding workers or a common team objective would require a new boundary and fresh S2 witness.

### Absence scope

- Surfaces inspected: runtime and agent specs, CLI/Web task entry, conversation/thread/workspace management, tool dispatch, context and session history.
- Plausible first-party paths checked: concurrent Web sessions, a possible Coding/LeetCode team, shared-workspace race prevention, delegated agents and task coordination.
- Why no material first-party path remains: the shipped execution path instantiates one agent per session and isolates independent conversations; there is no distinct-S1 interference plus coordination judgment and returned cross-S1 adjustment at the assessed recursion.

## S3 — Inside-and-now control

- State: —
- Function: no whole-system current-control organization regulating a portfolio of distinct operational S1 cells is established.
- Disturbance / variety regulated: step counts, tool errors, risk categories, runtime cancellation and command timeouts affect a single operational run, not a shared current operations portfolio.
- Decisive decision or feedback right: no S3 scope resource/priority/commitment judgment established; local execution bounds are preconfigured.
- Decision owner: no S3 owner established. The human configures local limits and approves individual actions; deterministic code enforces them.
- Supporting / enforcement mechanisms: `StopPolicy`, command/path/approval policies, session states, Web run summaries and cancellation.
- Closure path: guards can block or stop the local S1 loop, but no whole-system controller receives a current portfolio view, chooses a supervisory intervention and returns it across operational units.
- Why this is / is not agent-owned: the model chooses coding actions within authored limits; deleting it would not remove the configured stop/command gates, and those gates do not themselves choose current whole-system priorities.
- Evidence: [`agent/stop.py`](https://github.com/BlairCode/minicode-agent/blob/0c8bf466f2c1163403906253f2dc8be862fb828c/minicode_agent/agent/stop.py); [`safety/command_policy.py`](https://github.com/BlairCode/minicode-agent/blob/0c8bf466f2c1163403906253f2dc8be862fb828c/minicode_agent/safety/command_policy.py); [`safety/approval.py`](https://github.com/BlairCode/minicode-agent/blob/0c8bf466f2c1163403906253f2dc8be862fb828c/minicode_agent/safety/approval.py); [`web/controller.py`](https://github.com/BlairCode/minicode-agent/blob/0c8bf466f2c1163403906253f2dc8be862fb828c/minicode_agent/web/controller.py).
- Basis: structural absence review.
- Confidence: high.
- Caveats: per-tool human approval is ordinary operational authorization, not a demonstrated parent S3 current-control mode.

### Absence scope

- Surfaces inspected: application settings, runtime stop and retry policy, tool/command risk classification, Web run registry/status and approval/cancel endpoints.
- Plausible first-party paths checked: session-wide supervision, cross-run resource bargaining or priority changes, automated run intervention and operator-governed S3 mode.
- Why no material first-party path remains: available controls enforce authored local limits or individual commands without a current whole-system judgment and feedback path at the selected recursion.

## S3* — Complementary audit

- State: —
- Function: no independently grounded complementary audit loop that challenges ordinary agent reporting and returns findings into supervisory control is established.
- Disturbance / variety regulated: tool errors, code quality and task mistakes are surfaced as ordinary tool observations or model summaries; they are not subjected to a distinct independent audit path.
- Decisive decision or feedback right: no separate audit judgment with corrective return established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: tool result events, redacted session logs, UI progress display, command/test execution, tool-call descriptions and the same-agent LeetCode `review` mode.
- Closure path: results can inform the next operational model step and users can inspect history, but no independent audit actor samples raw reality, adjudicates the operation's claim and returns a corrective supervisory finding.
- Why this is / is not agent-owned: ordinary test execution, log recording and task-mode review remain inside the active production/reporting channel; a second independent auditor is neither instantiated nor wired into the runtime.
- Evidence: [`agent/explanation.py`](https://github.com/BlairCode/minicode-agent/blob/0c8bf466f2c1163403906253f2dc8be862fb828c/minicode_agent/agent/explanation.py); [`session.py`](https://github.com/BlairCode/minicode-agent/blob/0c8bf466f2c1163403906253f2dc8be862fb828c/minicode_agent/session.py); [`agent/manager.py`](https://github.com/BlairCode/minicode-agent/blob/0c8bf466f2c1163403906253f2dc8be862fb828c/minicode_agent/agent/manager.py); [`web/controller.py`](https://github.com/BlairCode/minicode-agent/blob/0c8bf466f2c1163403906253f2dc8be862fb828c/minicode_agent/web/controller.py).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: deterministic runtime/tool errors and adjacent project tests support operational verification but are not independent S3* judgments.

### Absence scope

- Surfaces inspected: event recorder and UI exposure, explanation formatter, tests/CI, task-mode prompts, tool-result feedback and approval responses.
- Plausible first-party paths checked: independent code review, secondary direct-artifact inspection, separate reviewer agent, replay/adversarial sampling and audit findings returned into execution.
- Why no material first-party path remains: all shipped checks and explanations belong to the same task/tool reporting path or external development tests; no second complementary access and independent corrective audit ownership is wired into standard operation.

## S4 — Outside-and-then intelligence

- State: —
- Function: no externally/prospectively oriented organizational capability-adaptation loop is established.
- Disturbance / variety regulated: current task context, user preferences, stored history and model/tool availability are consumed for present operation, not developed into future capability options and enacted adaptation.
- Decisive decision or feedback right: no agent-owned prospective capability or strategy adaptation decision established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: context trimming, persisted event history, reloaded conversations, static skill prompts, user settings and selectable model/task modes.
- Closure path: persisted history and configuration can influence subsequent requests, but no first-party external-sensing → future option → capability-change → returned current-operation loop is shipped.
- Why this is / is not agent-owned: the model handles each task and may use prior context; users/developers supply skill and model configuration. None owns an S4 prospective adaptation function in the runtime.
- Evidence: [`agent/context.py`](https://github.com/BlairCode/minicode-agent/blob/0c8bf466f2c1163403906253f2dc8be862fb828c/minicode_agent/agent/context.py); [`skills/loader.py`](https://github.com/BlairCode/minicode-agent/blob/0c8bf466f2c1163403906253f2dc8be862fb828c/minicode_agent/skills/loader.py); [`web/controller.py`](https://github.com/BlairCode/minicode-agent/blob/0c8bf466f2c1163403906253f2dc8be862fb828c/minicode_agent/web/controller.py); [`app.py`](https://github.com/BlairCode/minicode-agent/blob/0c8bf466f2c1163403906253f2dc8be862fb828c/minicode_agent/app.py).
- Basis: structural absence review.
- Confidence: high.
- Caveats: ordinary planning, memory, task switching, debugging and manual skill changes are not future-environment adaptation by themselves.

### Absence scope

- Surfaces inspected: context and session persistence, agent modes, skills loader, model settings, task prompts, Web settings and current-loop tools.
- Plausible first-party paths checked: persistent agent-authored skill/model changes, external trend sensing, self-improvement, future capability proposal and return to current operating structure, including a parent-governed option.
- Why no material first-party path remains: the reviewed runtime loads static skills and user-selected configurations; its decisions act on a present task and do not autonomously or through a closed parent mode change future organizational capability from environmental intelligence.

## S5 — Policy and identity

- State: —
- Function: no first-party identity- or ultimate-policy-level decision-and-return loop is established.
- Disturbance / variety regulated: local risky commands, out-of-workspace paths, tool availability, model credentials and prompt constraints are bounded by operator configuration and safety checks, not by runtime ultimate-policy deliberation.
- Decisive decision or feedback right: no identity/ultimate-policy adjudication right within the standard runtime.
- Decision owner: not established at S5; human settings and per-command approval remain ordinary local authorization.
- Supporting / enforcement mechanisms: base/Coding/LeetCode prompts, `AgentSpec` tool lists, `CommandPolicy`, `PathPolicy`, `ApprovalManager`, credential/settings stores and local Web approval endpoints.
- Closure path: operator-supplied settings and one-off approvals constrain the current action, but no policy-identity issue is referred to a legitimate parent for a decision returned as durable ultimate policy governing subsequent organization-wide behavior.
- Why this is / is not agent-owned: removing the model leaves the same authored security constraints; the model cannot independently change the overarching identity/policy, and command approval does not elevate routine risk to S5.
- Evidence: [`app.py`](https://github.com/BlairCode/minicode-agent/blob/0c8bf466f2c1163403906253f2dc8be862fb828c/minicode_agent/app.py); [`safety/command_policy.py`](https://github.com/BlairCode/minicode-agent/blob/0c8bf466f2c1163403906253f2dc8be862fb828c/minicode_agent/safety/command_policy.py); [`safety/path_policy.py`](https://github.com/BlairCode/minicode-agent/blob/0c8bf466f2c1163403906253f2dc8be862fb828c/minicode_agent/safety/path_policy.py); [`safety/approval.py`](https://github.com/BlairCode/minicode-agent/blob/0c8bf466f2c1163403906253f2dc8be862fb828c/minicode_agent/safety/approval.py); [`web/controller.py`](https://github.com/BlairCode/minicode-agent/blob/0c8bf466f2c1163403906253f2dc8be862fb828c/minicode_agent/web/controller.py).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: the human can reconfigure the application and approve actions; a static policy or human final say over a command does not demonstrate the distinct S5 governance loop.

### Absence scope

- Surfaces inspected: prompt/spec composition, configuration and credentials, command/path policy, approval manager, Web/CLI settings, session and cancellation controls, and repository governance context.
- Plausible first-party paths checked: model-owned constitutional/mission decision, policy-change proposal to legitimate parent, durable return of parent identity-policy judgment, and auto-adaptation of ultimate constraints.
- Why no material first-party path remains: the supported modes provide static and operator-edited constraints plus local approvals, not an identity-level deciding authority with a returned governing policy loop.

## Recursion

The declared coding session has one autonomous model-backed operational unit. Coding and LeetCode are mutually selected modes of that unit, and independent Web conversations lack a common operational purpose and regulative metasystem. A new workspace or thread is not a separate viable recursion merely by nesting or concurrency.

## Variety and escalation

The model and six workspace tools amplify the response repertoire for heterogeneous coding tasks. Tool schemas, workspace isolation, command risk policies, human approvals, bounded retries/steps/errors, cancellation and context trimming attenuate execution variety. Failures return to the operational model loop when recoverable; risky operations reach the user for a local authorization decision. Neither ordinary error events nor approvals are automatically an algedonic S-function or S5 governance path.

## Evidence gaps

The assessment is static and source-first at the pinned revision, with control-flow evidence from the shipped Python runtime/CLI/Web implementation. A live Qwen/DashScope model session and credentialed end-to-end task were not executed. No concrete unresolved shipped path was found that prevents bounded `—` conclusions for S2–S5/S3*; future plugins or changed operating modes require a new source-boundary review.

## Assessment summary

MiniCode Agent supplies a genuine first-party model→tool→observation coding loop (**S1=A**). Its agent modes, Web sessions, workspace separation, safety approvals, persisted history and static skills do not establish a distinct inter-S1 coordination, whole-current control, complementary independent audit, outside-and-then adaptation or ultimate-policy closure at the assessed boundary.

Proposed vector: **`A · — · — · — · — · —`**.

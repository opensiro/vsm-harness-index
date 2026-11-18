---
harness_id: green-agent
project_name: Green Agent
repository: https://github.com/w512/Green-Agent
review_ref: c829587716280cda6f98417f4fbc878acf86418b
reviewed_at: 2026-11-18
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Green Agent

## Review boundary

- System in focus: One distributed Green Agent workspace session using the first-party Python runtime.
- Purpose and identity: Perform coding and inspection tasks via model-selected tools with configurable operator approvals.
- Relevant environment: Operator tasks, workspace files and project configuration, command results and a configured model API.
- Standard-distribution boundary: The repository's launchers, frontends, provider adapter, session, bundled instructions, approval policy and bundled tool implementations.
- Credited operating / distribution surfaces: [start.py](https://github.com/w512/Green-Agent/blob/c829587716280cda6f98417f4fbc878acf86418b/start.py), [cli.py](https://github.com/w512/Green-Agent/blob/c829587716280cda6f98417f4fbc878acf86418b/cli.py), [tui.py](https://github.com/w512/Green-Agent/blob/c829587716280cda6f98417f4fbc878acf86418b/tui.py), [agent/agent.py](https://github.com/w512/Green-Agent/blob/c829587716280cda6f98417f4fbc878acf86418b/agent/agent.py), [agent/session.py](https://github.com/w512/Green-Agent/blob/c829587716280cda6f98417f4fbc878acf86418b/agent/session.py), [agent/tools.py](https://github.com/w512/Green-Agent/blob/c829587716280cda6f98417f4fbc878acf86418b/agent/tools.py), and [tools/](https://github.com/w512/Green-Agent/tree/c829587716280cda6f98417f4fbc878acf86418b/tools).
- Adjacent first-party surfaces excluded from ownership: Development tests and GitHub CI. Provider internals and locally authored additional tools are outside the supplied runtime boundary.
- First-party operating / deployment modes considered: CLI and Textual TUI, interactive and single-task execution, normal operator approval and pre-authorized operation.
- Recursion level: One workspace coding agent and its tools.
- Reviewed revision: `c829587716280cda6f98417f4fbc878acf86418b`.
- Observation date: 2026-11-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

[start.py](https://github.com/w512/Green-Agent/blob/c829587716280cda6f98417f4fbc878acf86418b/start.py) initializes the workspace, provider and tool registry before dispatching to the CLI or TUI. [agent/session.py](https://github.com/w512/Green-Agent/blob/c829587716280cda6f98417f4fbc878acf86418b/agent/session.py) retains conversation messages across tasks and wraps the common [model/tool loop](https://github.com/w512/Green-Agent/blob/c829587716280cda6f98417f4fbc878acf86418b/agent/agent.py). [agent/llm.py](https://github.com/w512/Green-Agent/blob/c829587716280cda6f98417f4fbc878acf86418b/agent/llm.py) adapts a configured OpenAI-compatible API. The [registry](https://github.com/w512/Green-Agent/blob/c829587716280cda6f98417f4fbc878acf86418b/agent/tools.py) loads bundled tools from definitions and Python implementations. The [permission layer](https://github.com/w512/Green-Agent/blob/c829587716280cda6f98417f4fbc878acf86418b/agent/permissions.py) decides whether a proposed call reaches the approval prompt.

## Operational model

The model proposes the next answer or tool action. The loop runs an approved tool call and attaches its result, denial or error to the model conversation. The next step can act on that feedback or return a final answer. The session retains consistent history when interrupted. The todo tool tracks local work, and the check tool runs syntax checks or a configured project command at the running agent's request.

## S1 — Operations

- State: A
- Function: Execute user-directed workspace tasks through a model-conditioned tool loop.
- Disturbance / variety regulated: New tasks, changing workspace information and successful, failed or denied tool calls.
- Decisive decision or feedback right: Select the action or final answer and decide the next step once results return.
- Decision owner: The model-backed Green Agent in the first-party coding loop.
- Supporting / enforcement mechanisms: Tool registry, provider adapter, approval enforcement, bounded step count and stop polling.
- Closure path: The runtime appends tool results or failures to the messages passed to the next model call. The session preserves the resulting history.
- Boundary reachability: The supported CLI and TUI both use Session and its call to run_agent.
- Why this is / is not agent-owned: The operator can veto certain effects, while the model selects the task's operational intent and decides how to proceed after a tool result.
- Evidence: [launch and frontend selection](https://github.com/w512/Green-Agent/blob/c829587716280cda6f98417f4fbc878acf86418b/start.py), [session task path](https://github.com/w512/Green-Agent/blob/c829587716280cda6f98417f4fbc878acf86418b/agent/session.py), [model and tool loop](https://github.com/w512/Green-Agent/blob/c829587716280cda6f98417f4fbc878acf86418b/agent/agent.py).
- Basis: Explicit source and shipped entrypoints.
- Confidence: High for source reachability.
- Caveats: Execution requires a configured provider and may require per-call approval.

## S2 — Coordination

- State: —
- Function: Coordination of interfering distinct operational units.
- Disturbance / variety regulated: Potential competing actions or inconsistent commitments between independently operating agents.
- Decisive decision or feedback right: No inter-agent interference decision in the reviewed runtime.
- Decision owner: None established.
- Supporting / enforcement mechanisms: Ordered tool iteration, in-session todo state and workspace handling.
- Closure path: Tool results feed back to the same model conversation.
- Why this is / is not agent-owned: Bundled tools execute requests from one agent and exercise no independent operational judgment.
- Evidence: [loop](https://github.com/w512/Green-Agent/blob/c829587716280cda6f98417f4fbc878acf86418b/agent/agent.py), [tool registry](https://github.com/w512/Green-Agent/blob/c829587716280cda6f98417f4fbc878acf86418b/agent/tools.py), [todo tool](https://github.com/w512/Green-Agent/blob/c829587716280cda6f98417f4fbc878acf86418b/tools/todo/todo.py).
- Basis: Bounded source inspection.
- Confidence: High at the one-session boundary.
- Caveats: Separate externally composed sessions were outside scope.

### Absence scope

- Surfaces inspected: [launcher](https://github.com/w512/Green-Agent/blob/c829587716280cda6f98417f4fbc878acf86418b/start.py), [session](https://github.com/w512/Green-Agent/blob/c829587716280cda6f98417f4fbc878acf86418b/agent/session.py), [loop](https://github.com/w512/Green-Agent/blob/c829587716280cda6f98417f4fbc878acf86418b/agent/agent.py), and [todo tool](https://github.com/w512/Green-Agent/blob/c829587716280cda6f98417f4fbc878acf86418b/tools/todo/todo.py).
- Plausible first-party paths checked: Tool ordering, local work tracking and the alternative frontends.
- Why no material first-party path remains: Both frontends drive the same single-session implementation. The work list and ordered calls feed that single actor.

## S3 — Inside-and-now control

- State: —
- Function: Whole-system current control of operational commitments and resources.
- Disturbance / variety regulated: A shortage or conflict among active operational commitments.
- Decisive decision or feedback right: No supplied whole-system allocation or reprioritization decision.
- Decision owner: The operator controls individual pending calls or stops a session. No S3 owner is established at this boundary.
- Supporting / enforcement mechanisms: Approval policy, per-step stop polling and per-run limits.
- Closure path: An approval or stop governs the pending action or current run.
- Why this is / is not agent-owned: The task loop owns local task execution and lacks a distinct current-control perspective on an operating organization.
- Evidence: [permissions](https://github.com/w512/Green-Agent/blob/c829587716280cda6f98417f4fbc878acf86418b/agent/permissions.py), [loop](https://github.com/w512/Green-Agent/blob/c829587716280cda6f98417f4fbc878acf86418b/agent/agent.py), [CLI](https://github.com/w512/Green-Agent/blob/c829587716280cda6f98417f4fbc878acf86418b/cli.py), [TUI](https://github.com/w512/Green-Agent/blob/c829587716280cda6f98417f4fbc878acf86418b/tui.py).
- Basis: Source and operator entrypoints.
- Confidence: High for reviewed modes.
- Caveats: The launcher exposes an auto-approval option.

### Absence scope

- Surfaces inspected: [permissions](https://github.com/w512/Green-Agent/blob/c829587716280cda6f98417f4fbc878acf86418b/agent/permissions.py), [session](https://github.com/w512/Green-Agent/blob/c829587716280cda6f98417f4fbc878acf86418b/agent/session.py), [CLI](https://github.com/w512/Green-Agent/blob/c829587716280cda6f98417f4fbc878acf86418b/cli.py), [TUI](https://github.com/w512/Green-Agent/blob/c829587716280cda6f98417f4fbc878acf86418b/tui.py), and [launch options](https://github.com/w512/Green-Agent/blob/c829587716280cda6f98417f4fbc878acf86418b/start.py).
- Plausible first-party paths checked: Approval dialogs, always approvals, stop, displayed run progress and step limit.
- Why no material first-party path remains: The controls apply to the action or session in progress. The package has no supervisor view and return path covering shared operating commitments.

## S3* — Complementary audit

- State: —
- Function: Independent inspection of operating reality with corrective feedback.
- Disturbance / variety regulated: A falsely reported or defective task outcome.
- Decisive decision or feedback right: No separate audit actor or audit-specific judgment path is shown.
- Decision owner: The working agent selects when to invoke the check tool, and the operator sees its ordinary session output.
- Supporting / enforcement mechanisms: Syntax checks, project check command and rendered tool results.
- Closure path: Check outputs go back through the same task conversation.
- Why this is / is not agent-owned: Verification is selected and interpreted inside the performing session. No independent channel samples or adjudicates the result.
- Evidence: [check tool](https://github.com/w512/Green-Agent/blob/c829587716280cda6f98417f4fbc878acf86418b/tools/check/check.py), [tool-result events](https://github.com/w512/Green-Agent/blob/c829587716280cda6f98417f4fbc878acf86418b/agent/agent.py), [session](https://github.com/w512/Green-Agent/blob/c829587716280cda6f98417f4fbc878acf86418b/agent/session.py).
- Basis: Source and tool-dispatch inspection.
- Confidence: High.
- Caveats: A project can provide an arbitrary check command.

### Absence scope

- Surfaces inspected: [checker](https://github.com/w512/Green-Agent/blob/c829587716280cda6f98417f4fbc878acf86418b/tools/check/check.py), [task loop](https://github.com/w512/Green-Agent/blob/c829587716280cda6f98417f4fbc878acf86418b/agent/agent.py), [CLI reporting](https://github.com/w512/Green-Agent/blob/c829587716280cda6f98417f4fbc878acf86418b/cli.py), and [development tests](https://github.com/w512/Green-Agent/tree/c829587716280cda6f98417f4fbc878acf86418b/tests).
- Plausible first-party paths checked: Syntax checks, project-level check invocation, frontend reporting and the shipped test suite.
- Why no material first-party path remains: These surfaces supply operational tool feedback or evaluate the implementation during development. Neither establishes a distinct audit decision in the distributed agent.

## S4 — Outside-and-then intelligence

- State: —
- Function: Prospective adaptation of later operating capability in response to external signals.
- Disturbance / variety regulated: Changed models, workspace demands and external conditions that could warrant a redesigned capability.
- Decisive decision or feedback right: No supplied external sensing-to-adoption loop for a future capability choice.
- Decision owner: Operators can select a model and developers can supply tools and configuration.
- Supporting / enforcement mechanisms: Provider options and retries, fetch tool and tool registry.
- Closure path: These paths supply input, a configured model or a tool for current tasks.
- Why this is / is not agent-owned: Fetching task inputs and reacting to tool results operate inside the ongoing S1 task.
- Evidence: [CLI model command](https://github.com/w512/Green-Agent/blob/c829587716280cda6f98417f4fbc878acf86418b/cli.py), [provider](https://github.com/w512/Green-Agent/blob/c829587716280cda6f98417f4fbc878acf86418b/agent/llm.py), [registry](https://github.com/w512/Green-Agent/blob/c829587716280cda6f98417f4fbc878acf86418b/agent/tools.py), and [fetch tool](https://github.com/w512/Green-Agent/blob/c829587716280cda6f98417f4fbc878acf86418b/tools/fetch/fetch.py).
- Basis: Source and configuration scope.
- Confidence: Medium-high.
- Caveats: Locally authored tools can extend the runtime.

### Absence scope

- Surfaces inspected: [configuration](https://github.com/w512/Green-Agent/blob/c829587716280cda6f98417f4fbc878acf86418b/config.template.py), [provider](https://github.com/w512/Green-Agent/blob/c829587716280cda6f98417f4fbc878acf86418b/agent/llm.py), [fetch tool](https://github.com/w512/Green-Agent/blob/c829587716280cda6f98417f4fbc878acf86418b/tools/fetch/fetch.py), [registry](https://github.com/w512/Green-Agent/blob/c829587716280cda6f98417f4fbc878acf86418b/agent/tools.py), and [session](https://github.com/w512/Green-Agent/blob/c829587716280cda6f98417f4fbc878acf86418b/agent/session.py).
- Plausible first-party paths checked: External data retrieval, provider/model switching and locally loaded extensions.
- Why no material first-party path remains: There is no prospective option assessment surfaced to a decision owner and returned as a durable change to future capability.

## S5 — Policy and identity

- State: —
- Function: Decide the ultimate operating identity and authority boundary.
- Disturbance / variety regulated: A conflict requiring a decision about the system's enduring purpose or rules.
- Decisive decision or feedback right: No operational identity or ultimate-policy deliberation and return path.
- Decision owner: The distributed instructions and configuration originate with developers or the configuring user.
- Supporting / enforcement mechanisms: Default instructions, workspace scope, approvals and launch options.
- Closure path: These inputs constrain task operation and determine action eligibility.
- Why this is / is not agent-owned: Current-action approval and configuration loading leave enduring identity decisions outside the first-party operating loop.
- Evidence: [instructions](https://github.com/w512/Green-Agent/blob/c829587716280cda6f98417f4fbc878acf86418b/agent/instructions.md), [launcher](https://github.com/w512/Green-Agent/blob/c829587716280cda6f98417f4fbc878acf86418b/start.py), [permissions](https://github.com/w512/Green-Agent/blob/c829587716280cda6f98417f4fbc878acf86418b/agent/permissions.py).
- Basis: Runtime policy consumers and operator controls.
- Confidence: High at the declared boundary.
- Caveats: Local operators can change workspace settings outside the loop.

### Absence scope

- Surfaces inspected: [instructions](https://github.com/w512/Green-Agent/blob/c829587716280cda6f98417f4fbc878acf86418b/agent/instructions.md), [launcher](https://github.com/w512/Green-Agent/blob/c829587716280cda6f98417f4fbc878acf86418b/start.py), [permissions](https://github.com/w512/Green-Agent/blob/c829587716280cda6f98417f4fbc878acf86418b/agent/permissions.py), and [conversation initialization](https://github.com/w512/Green-Agent/blob/c829587716280cda6f98417f4fbc878acf86418b/agent/agent.py).
- Plausible first-party paths checked: Static prompt and policy inputs, per-call and persistent-in-session approvals and new conversation handling.
- Why no material first-party path remains: The supplied controls initialize or constrain operations. They do not adjudicate identity questions and return authoritative decisions to the organization.

## Recursion

One operational coding cell. Tool modules and the two frontends are supporting components of that cell.

## Variety and escalation

A denied tool call feeds a denial message to the agent. The operator approval prompt and interrupt offer bounded intervention in current work.

## Evidence gaps

Source-only review. No provider run or behavioral effectiveness claim. Optional tools authored outside the repository are beyond the reviewed distribution.

---
harness_id: rojak
project_name: Rojak
repository: https://github.com/StreetLamb/rojak
review_ref: 51966e6b8b03e8908eed80aafe0f63cdfee80b5f
reviewed_at: 2026-11-18
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Rojak

## Review boundary

- System in focus: One persistent or stateless Rojak orchestration session, including shipped model and tool activities, task handling, handoffs and its managing client.
- Purpose and identity: Run durable model-backed conversations with tools and transfer the active role between configured agents.
- Environment: Application requests, application-defined functions and role definitions, model results, retrieval services and authorized client interventions.
- Standard-distribution boundary: The Rojak library and its Temporal workflow/client bindings. Temporal supplies durable activity scheduling and replay. Model providers and consumer application code remain external dependencies.
- Credited operating / distribution surfaces: Packaged orchestration loop, OpenAI/Anthropic activity adapters, tool/retriever bindings, session query and mutation APIs, and interrupt/resume.
- Adjacent first-party surfaces excluded from ownership: Pizza, weather and MCP examples, tests and repository CI. Examples corroborate interface behavior without donating application governance.
- First-party operating / deployment modes considered: Stateless and persistent mode, sequential agent handoffs, scheduled session starts and optional client approvals on tools.
- Recursion level: One Rojak workflow session is the assessed operational whole. Several unrelated sessions can run on a worker fleet, but the library does not expose that fleet as one organizational system.
- Reviewed revision: `51966e6b8b03e8908eed80aafe0f63cdfee80b5f`.
- Observation date: 2026-11-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

Rojak packages a Temporal workflow and provider adapters. One active role processes a request, with context and message history persisted or returned. Applications register tools, retrieval activities and interruption points. A result may select the next active agent. [Packaged workflow and activity wiring](https://github.com/StreetLamb/rojak/blob/51966e6b8b03e8908eed80aafe0f63cdfee80b5f/rojak/client.py#L80-L115) · [Task and turn dispatch](https://github.com/StreetLamb/rojak/blob/51966e6b8b03e8908eed80aafe0f63cdfee80b5f/rojak/workflows/orchestrator_workflow.py#L108-L197) · [Sequential handoff](https://github.com/StreetLamb/rojak/blob/51966e6b8b03e8908eed80aafe0f63cdfee80b5f/rojak/workflows/orchestrator_workflow.py#L204-L238)

## Operational model

The active agent owns local model and tool choices. The application client may observe and change current session limits and state or handle a pending tool interrupt. Temporal transports and executes these choices. [Model/tool cycle](https://github.com/StreetLamb/rojak/blob/51966e6b8b03e8908eed80aafe0f63cdfee80b5f/rojak/workflows/agent_workflow.py#L111-L216) · [Tool-interrupt handling](https://github.com/StreetLamb/rojak/blob/51966e6b8b03e8908eed80aafe0f63cdfee80b5f/rojak/workflows/agent_workflow.py#L238-L321) · [Session query and control](https://github.com/StreetLamb/rojak/blob/51966e6b8b03e8908eed80aafe0f63cdfee80b5f/rojak/client.py#L308-L362)

## S1 — Operations

- State: A
- Function: Choose and execute model-mediated actions toward the consumer application's task.
- Disturbance / variety regulated: Different user inputs, tool responses, interrupted calls and activity errors.
- Decisive decision or feedback right: Select tool calls, adjust the next action from returned evidence and decide when to return an answer.
- Decision owner: The active model-backed agent. The caller configures tools and may authorize designated invocations.
- Supporting / enforcement mechanisms: Temporal activities, tool schemas, shared conversation and context, configured retries and optional interrupts.
- Closure path: The workflow appends results or rejection feedback and invokes the active or handed-off agent again, or returns the answer.
- Why this is / is not agent-owned: The shipped workflow invokes model outputs and supplies tool outcomes while leaving action choice with the agent.
- Evidence: [Packaged workflow and activity wiring](https://github.com/StreetLamb/rojak/blob/51966e6b8b03e8908eed80aafe0f63cdfee80b5f/rojak/client.py#L80-L115) · [Model/tool cycle](https://github.com/StreetLamb/rojak/blob/51966e6b8b03e8908eed80aafe0f63cdfee80b5f/rojak/workflows/agent_workflow.py#L111-L216) · [Tool-interrupt handling](https://github.com/StreetLamb/rojak/blob/51966e6b8b03e8908eed80aafe0f63cdfee80b5f/rojak/workflows/agent_workflow.py#L238-L321)
- Basis: Explicit and structural.
- Confidence: High.
- Caveats: Tool availability and actual action semantics depend on the consuming application.
- Boundary reachability: The public worker constructor registers shipped activity adapters and the orchestrator. The active-agent cycle invokes the corresponding model activity under normal run entry.

## S2 — Coordination

- State: —
- Function: Control interference between concurrent independent S1 units.
- Disturbance / variety regulated: An application can expose several roles and models can emit several tool calls. A session nevertheless has one active model role.
- Decisive decision or feedback right: No distinct first-party inter-unit conflict decision is supplied.
- Decision owner: No S2 owner evidenced.
- Supporting / enforcement mechanisms: Serial task dequeue, a lock for client updates, sequential tool execution and ordered handoffs.
- Closure path: A handoff replaces the active role and continues with context. The library does not resolve conflicts among separate sessions.
- Why this is / is not agent-owned: Sequential role transfer and tool result ordering preserve one operational stream.
- Evidence: [Task and turn dispatch](https://github.com/StreetLamb/rojak/blob/51966e6b8b03e8908eed80aafe0f63cdfee80b5f/rojak/workflows/orchestrator_workflow.py#L108-L197) · [Sequential handoff](https://github.com/StreetLamb/rojak/blob/51966e6b8b03e8908eed80aafe0f63cdfee80b5f/rojak/workflows/orchestrator_workflow.py#L204-L238) · [Model/tool cycle](https://github.com/StreetLamb/rojak/blob/51966e6b8b03e8908eed80aafe0f63cdfee80b5f/rojak/workflows/agent_workflow.py#L111-L216) · [Workflow queries and signals](https://github.com/StreetLamb/rojak/blob/51966e6b8b03e8908eed80aafe0f63cdfee80b5f/rojak/workflows/orchestrator_workflow.py#L254-L302)
- Basis: Bounded structural absence.
- Confidence: High.
- Caveats: Consumer code can supply coordination beyond this shipped boundary.

### Absence scope

- Surfaces inspected: Task queue, active-agent handoff, update lock, tool context update and documented parallel conversation support.
- Plausible first-party paths checked: Competing role commitments, parallel tool/context updates and separate-session interference.
- Why no material first-party path remains: In one session the roles execute serially and multiple tool calls are consumed in order. Across sessions no first-party inter-session disturbance and return path is supplied.

## S3 — Inside-and-now control

- State: P
- Function: Regulate the current work window and retained operational state of the entire session.
- Disturbance / variety regulated: A persistent session may need a changed turn budget or history/context following session progress or stale state.
- Decisive decision or feedback right: Read the current session and choose new run-wide limits, state or termination.
- Decision owner: Authorized application client acting as the session parent. The model owns local S1 choices.
- Supporting / enforcement mechanisms: Session queries and signals, workflow handle, limit evaluation and cancellation mechanism.
- Closure path: Client reads messages and workflow settings, updates the session by ID, the workflow stores new values and uses max turns and history size in subsequent operation.
- Why this is / is not agent-owned: The model has no supplied control over session configuration. The application client can exercise that whole-session right through dedicated APIs.
- Evidence: [Session query and control](https://github.com/StreetLamb/rojak/blob/51966e6b8b03e8908eed80aafe0f63cdfee80b5f/rojak/client.py#L308-L362) · [Workflow queries and signals](https://github.com/StreetLamb/rojak/blob/51966e6b8b03e8908eed80aafe0f63cdfee80b5f/rojak/workflows/orchestrator_workflow.py#L254-L302) · [Task and turn dispatch](https://github.com/StreetLamb/rojak/blob/51966e6b8b03e8908eed80aafe0f63cdfee80b5f/rojak/workflows/orchestrator_workflow.py#L108-L197) · [Config return test source](https://github.com/StreetLamb/rojak/blob/51966e6b8b03e8908eed80aafe0f63cdfee80b5f/tests/test_workflow.py#L185-L221)
- Basis: Explicit and structural.
- Confidence: Medium-high.
- Caveats: Scoped to one workflow. The test source exercises the configuration change and readback with a mock model. Local tool approvals alone are outside this S3 claim.
- Boundary reachability: The managing client and shipped persistent workflow explicitly support a session query and update signal while the worker is running.
- Whole-system current view: For this single-session recursion, the caller can query that session's messages, retained context, turn limit and history policy and obtain the latest result.
- Current-control decision scope: The authorized caller can change the active session's shared turn limit, retained history and context, or cancel that session.

## S3* — Complementary audit

- State: —
- Function: Independently challenge operational claims and feed findings into session regulation.
- Disturbance / variety regulated: A model answer or reported tool result could be wrong.
- Decisive decision or feedback right: No independently owned audit or corrective audit feedback supplied.
- Decision owner: None evidenced.
- Supporting / enforcement mechanisms: Temporal state queries, debug logging and tool approval.
- Closure path: Queries expose routine session state. Approval can block an ordinary pending action.
- Why this is / is not agent-owned: No shipped path sources a separate claim check and returns it to a regulator.
- Evidence: [Workflow queries and signals](https://github.com/StreetLamb/rojak/blob/51966e6b8b03e8908eed80aafe0f63cdfee80b5f/rojak/workflows/orchestrator_workflow.py#L254-L302) · [Session query and control](https://github.com/StreetLamb/rojak/blob/51966e6b8b03e8908eed80aafe0f63cdfee80b5f/rojak/client.py#L308-L362) · [Tool-interrupt handling](https://github.com/StreetLamb/rojak/blob/51966e6b8b03e8908eed80aafe0f63cdfee80b5f/rojak/workflows/agent_workflow.py#L238-L321)
- Basis: Bounded structural absence.
- Confidence: Medium-high.
- Caveats: Application activities could independently audit claims if supplied.

### Absence scope

- Surfaces inspected: Session result/config queries, logged activities and optional approval path.
- Plausible first-party paths checked: Independent result re-execution, audit sampling and separate feedback into client regulation.
- Why no material first-party path remains: The queries expose ordinary workflow records and the interrupt exposes intended tool effects. Neither runs a separately owned complementary check.

## S4 — Outside-and-then intelligence

- State: —
- Function: Explore relevant external futures and carry adaptation options back to session capability.
- Disturbance / variety regulated: External information can differ from current model knowledge.
- Decisive decision or feedback right: No first-party prospective adaptation-decision right evidenced.
- Decision owner: No S4 owner evidenced.
- Supporting / enforcement mechanisms: Retriever, periodic scheduling, context mutation and retry parameters.
- Closure path: Retrieved data augments the current prompt. Scheduling restarts configured tasks. The library supplies no prospective adopt/reject loop.
- Why this is / is not agent-owned: Current-query augmentation leaves external planning and capability choices with the application.
- Evidence: [Query-time retrieval](https://github.com/StreetLamb/rojak/blob/51966e6b8b03e8908eed80aafe0f63cdfee80b5f/rojak/workflows/agent_workflow.py#L218-L236) · [Scheduled execution configuration](https://github.com/StreetLamb/rojak/blob/51966e6b8b03e8908eed80aafe0f63cdfee80b5f/rojak/client.py#L159-L208) · [Session query and control](https://github.com/StreetLamb/rojak/blob/51966e6b8b03e8908eed80aafe0f63cdfee80b5f/rojak/client.py#L308-L362)
- Basis: Bounded structural absence.
- Confidence: High.
- Caveats: Application-supplied goals could implement adaptation at their own boundary.

### Absence scope

- Surfaces inspected: Retriever lifecycle, scheduling, retry behavior and live client configuration.
- Plausible first-party paths checked: Scheduled external intelligence, comparison of future options and adoption through client controls.
- Why no material first-party path remains: Scheduling and retrieval consume supplied tasks and inputs. No future-option generator or resulting decision path is shipped.

## S5 — Policy and identity

- State: —
- Function: Adjudicate session identity and ultimate policy and apply the result.
- Disturbance / variety regulated: A consuming application may change roles, tool permissions or authority boundaries.
- Decisive decision or feedback right: No supplied identity- or ultimate-policy adjudication found.
- Decision owner: The consumer chooses initial configuration and can regulate session execution.
- Supporting / enforcement mechanisms: Agent parameter construction, application-defined options and per-call interruption.
- Closure path: Client changes alter session state and tool approval affects the current action. Neither is a returned ruling on session identity or governing policy.
- Why this is / is not agent-owned: The library delegates application purpose and ultimate authority to configuration outside the session.
- Evidence: [Packaged workflow and activity wiring](https://github.com/StreetLamb/rojak/blob/51966e6b8b03e8908eed80aafe0f63cdfee80b5f/rojak/client.py#L80-L115) · [User and resume API](https://github.com/StreetLamb/rojak/blob/51966e6b8b03e8908eed80aafe0f63cdfee80b5f/rojak/client.py#L270-L306) · [Session query and control](https://github.com/StreetLamb/rojak/blob/51966e6b8b03e8908eed80aafe0f63cdfee80b5f/rojak/client.py#L308-L362) · [Tool-interrupt handling](https://github.com/StreetLamb/rojak/blob/51966e6b8b03e8908eed80aafe0f63cdfee80b5f/rojak/workflows/agent_workflow.py#L238-L321)
- Basis: Bounded structural absence.
- Confidence: Medium-high.
- Caveats: Applications can submit new identities or rules but must implement policy closure themselves.

### Absence scope

- Surfaces inspected: Worker and agent setup, call and resume APIs, state update and tool checks.
- Plausible first-party paths checked: Role replacement, forced tool approvals and persistent configuration edits as possible policy channels.
- Why no material first-party path remains: These paths instantiate or regulate existing workflow choices. No specialized route carries a policy dispute to an authority and returns a binding decision.

## Distributed OSS parent arrangement

Repository maintainers are outside the runtime. The authorized consuming application owns the session-level control surfaced by the client.

## Self-hosted and non-human modes

A stateful or stateless workflow can run without a human interrupt. Application ownership of session controls is distinct from how an application decides whether to ask a person.

## Recursion

Provider workers and Temporal services supply support for a workflow. Agent roles hand off within the same assessed operational unit.

## Variety and escalation

Activity retry and model-facing failure responses absorb routine disturbances. Configured interrupts surface a specific approval and return the decision to execution. [Tool-interrupt handling](https://github.com/StreetLamb/rojak/blob/51966e6b8b03e8908eed80aafe0f63cdfee80b5f/rojak/workflows/agent_workflow.py#L238-L321)

## Evidence gaps

Pinned source and conformance-test source were inspected. No Temporal environment, external providers or application-specific management workflow was run.

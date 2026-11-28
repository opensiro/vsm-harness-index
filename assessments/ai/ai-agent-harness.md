---
harness_id: ai-agent-harness
project_name: AI Agent Harness
repository: https://github.com/RameshKatla/ai-agent-harness
review_ref: 691f09f7659fa9e0c3741f93e4e8e69293ac7aa5
reviewed_at: 2026-11-28
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

# AI Agent Harness

## Review boundary

- System in focus: One self-hosted API deployment and its native per-thread agent runs.
- Purpose and identity: Answer user requests by choosing supported tools and returning a result with conversation and memory persistence.
- Relevant environment: Authenticated users, an Ollama-compatible model, PostgreSQL and optional Redis-backed services.
- Standard-distribution boundary: Shipped FastAPI service, LangGraph graph, tool registry, policy, checkpoint and memory surfaces.
- Credited operating / distribution surfaces: The local and Docker API distributions, native model/tool loop, interruption and resume endpoints and run state.
- Adjacent first-party surfaces excluded from ownership: Repository tests and eval fixtures, offline eval scoring, upstream provider internals, maintainers and external weather service internals.
- First-party operating / deployment modes considered: Docker Compose and native Python execution, each with synchronous and SSE run interfaces and per-tool approved/rejected resume.
- Recursion level: Service with per-thread agent operations. The same thread serializes successive turns.
- Reviewed revision: 691f09f7659fa9e0c3741f93e4e8e69293ac7aa5
- Observation date: 2026-11-28
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

The API invokes one native graph per thread. A model node requests a structured final answer or tool decision. Limits and permissions gate the tool, and information from execution returns through an observation node. PostgreSQL checkpoints support resumed approvals and follow-ups. Memory retrieval and persistence are provided as graph nodes.

## Operational model

One tool-using agent resolves a user request. Calculator, datetime and weather are invoked tools. The API owner supplies credentials and operating limits. An authenticated user can decide a paused tool call, and the originating graph carries that result into task execution.

## S1 — Operations

- State: A
- Function: Complete a request using the supplied model/tool graph.
- Disturbance / variety regulated: The request may need information or computed results, and tool calls may fail.
- Decisive decision or feedback right: Select whether to call a tool, what call to make and when to return a final answer.
- Decision owner: The configured model acting in the supplied agent node.
- Supporting / enforcement mechanisms: Structured output, graph routing, capability registry, permission and retry enforcement, and checkpoints.
- Closure path: A tool executes and the observation returns to the model. A final answer follows the memory save branch and reaches the caller.
- Boundary reachability: The shipped API constructs the graph and calls it directly. A compatible model and configured dependencies suffice for the native decision loop.
- Why this is / is not agent-owned: The graph and tool policy can guard and dispatch, but the task choice and result depend on the model.
- Evidence: [README.md](https://github.com/RameshKatla/ai-agent-harness/blob/691f09f7659fa9e0c3741f93e4e8e69293ac7aa5/README.md#L17-L41), [README.md](https://github.com/RameshKatla/ai-agent-harness/blob/691f09f7659fa9e0c3741f93e4e8e69293ac7aa5/README.md#L183-L205), [app/agent/nodes.py](https://github.com/RameshKatla/ai-agent-harness/blob/691f09f7659fa9e0c3741f93e4e8e69293ac7aa5/app/agent/nodes.py#L69-L120), [app/agent/graph.py](https://github.com/RameshKatla/ai-agent-harness/blob/691f09f7659fa9e0c3741f93e4e8e69293ac7aa5/app/agent/graph.py#L14-L39), [app/agent/service.py](https://github.com/RameshKatla/ai-agent-harness/blob/691f09f7659fa9e0c3741f93e4e8e69293ac7aa5/app/agent/service.py#L25-L41)
- Basis: Structural evidence from pinned first-party source.
- Confidence: high
- Caveats: Tools needing approval can pause the graph. It can complete ordinary permitted work autonomously.

## S2 — Coordination

- State: —
- Function: Inter-S1 interference regulation was sought across concurrent runs and workers.
- Disturbance / variety regulated: Turns could compete to update one persisted conversation.
- Decisive decision or feedback right: No supplied inter-agent coordination right was found.
- Decision owner: Each thread's native agent owns its own task. Storage serializes updates to the same thread.
- Supporting / enforcement mechanisms: Per-conversation key, database lock and pending approval check.
- Closure path: An exclusive turn or conflict response constrains one conversation. Other threads do not receive this as coordination feedback.
- Why this is / is not agent-owned: Serialization preserves checkpoint consistency for one thread. Tools and graph nodes do not constitute separate S1 actors.
- Evidence: [app/agent/executor.py](https://github.com/RameshKatla/ai-agent-harness/blob/691f09f7659fa9e0c3741f93e4e8e69293ac7aa5/app/agent/executor.py#L79-L117), [README.md](https://github.com/RameshKatla/ai-agent-harness/blob/691f09f7659fa9e0c3741f93e4e8e69293ac7aa5/README.md#L218-L235), [app/agent/graph.py](https://github.com/RameshKatla/ai-agent-harness/blob/691f09f7659fa9e0c3741f93e4e8e69293ac7aa5/app/agent/graph.py#L14-L39)
- Basis: Structural evidence from pinned first-party source.
- Confidence: high
- Caveats: A deployment can serve many independently scoped threads.

### Absence scope

- Surfaces inspected: Executor thread scoping, PostgreSQL lock and native graph edges.
- Plausible first-party paths checked: Distinct threads coordinating a resource conflict, or operational units negotiating action changes.
- Why no material first-party path remains: A thread has one model loop at a time. The lock protects data and no shipped relation changes different agents' next operations in response to their mutual interference.

## S3 — Inside-and-now control

- State: —
- Function: Current service-level prioritization or reallocation was sought.
- Disturbance / variety regulated: An active run can block or approach its step/time limit.
- Decisive decision or feedback right: No supplied decision owner compares current service commitments and reserves or redirects resources.
- Decision owner: Runtime policy enforces fixed constraints. The caller approves or rejects an individual tool invocation.
- Supporting / enforcement mechanisms: Limits, graph interrupts, persisted pending call and authenticated resume route.
- Closure path: A call resumes with permission or a rejection observation. The remaining run continues under the same scope and limits.
- Why this is / is not agent-owned: Tool approval decides whether one proposed action may execute. No supplied current view and portfolio decision link it to whole-service control.
- Evidence: [app/agent/policies.py](https://github.com/RameshKatla/ai-agent-harness/blob/691f09f7659fa9e0c3741f93e4e8e69293ac7aa5/app/agent/policies.py#L18-L37), [app/agent/executor.py](https://github.com/RameshKatla/ai-agent-harness/blob/691f09f7659fa9e0c3741f93e4e8e69293ac7aa5/app/agent/executor.py#L107-L142), [app/api/routes_agent.py](https://github.com/RameshKatla/ai-agent-harness/blob/691f09f7659fa9e0c3741f93e4e8e69293ac7aa5/app/api/routes_agent.py#L36-L69), [app/agent/nodes.py](https://github.com/RameshKatla/ai-agent-harness/blob/691f09f7659fa9e0c3741f93e4e8e69293ac7aa5/app/agent/nodes.py#L123-L139)
- Basis: Structural evidence from pinned first-party source.
- Confidence: high
- Caveats: A user can supervise tool use on their own thread.

### Absence scope

- Surfaces inspected: Run state, pending approval, settings, timeout and policy handling.
- Plausible first-party paths checked: Cross-thread capacity, reprioritization, and parent decisions over the whole current service workload.
- Why no material first-party path remains: Available routes return one tool decision to one thread. The runtime has no agent or parent portfolio control loop in the supplied distribution.

## S3* — Complementary audit

- State: —
- Function: A complementary auditor for the service's ordinary completed-run claims was sought.
- Disturbance / variety regulated: A completed answer may have used a wrong tool or contain an incorrect result.
- Decisive decision or feedback right: No supplied ordinary-run decision consumes independent outcome evidence and reopens completion.
- Decision owner: The graph producer selects the answer. An isolated evaluation runner can score designated scenarios.
- Supporting / enforcement mechanisms: Tool observations, lifecycle audit records and evaluation tooling.
- Closure path: Run output and records persist. Evaluation scores and exit status are scoped to separately launched test cases.
- Why this is / is not agent-owned: Execution observations inform the original producer. The ordinary completion route has no independent reviewer with an action on the finding.
- Evidence: [app/agent/nodes.py](https://github.com/RameshKatla/ai-agent-harness/blob/691f09f7659fa9e0c3741f93e4e8e69293ac7aa5/app/agent/nodes.py#L89-L105), [app/agent/graph.py](https://github.com/RameshKatla/ai-agent-harness/blob/691f09f7659fa9e0c3741f93e4e8e69293ac7aa5/app/agent/graph.py#L19-L39), [README.md](https://github.com/RameshKatla/ai-agent-harness/blob/691f09f7659fa9e0c3741f93e4e8e69293ac7aa5/README.md#L232-L255), [app/agent/service.py](https://github.com/RameshKatla/ai-agent-harness/blob/691f09f7659fa9e0c3741f93e4e8e69293ac7aa5/app/agent/service.py#L42-L77)
- Basis: Structural evidence from pinned first-party source.
- Confidence: medium
- Caveats: The evaluation CLI can verify selected test-case trajectories and answers against its dataset.

### Absence scope

- Surfaces inspected: Final and save graph, approval path, audit records and the separate evaluation command.
- Plausible first-party paths checked: Independent direct evidence on an ordinary run, or an eval finding returned to production current control.
- Why no material first-party path remains: The shipped audit trail records events. The eval environment assesses separate cases and its stored results do not feed an ordinary-run disposition loop.

## S4 — Outside-and-then intelligence

- State: —
- Function: External change sensing and prospective capability adaptation were sought.
- Disturbance / variety regulated: Later tasks or user preferences may differ from current ones.
- Decisive decision or feedback right: No supplied owner selects a new future operating capability from environmental findings.
- Decision owner: The user declares preferences and the memory subsystem stores/retrieves them under a fixed policy.
- Supporting / enforcement mechanisms: Conversation checkpoints, semantic retrieval, episode saving, static model configuration.
- Closure path: Relevant memory context returns to later task prompts. Future tool/model capability is externally configured.
- Why this is / is not agent-owned: Retrieval changes task context. No positive future-oriented capability decision or enactment is supplied.
- Evidence: [app/agent/nodes.py](https://github.com/RameshKatla/ai-agent-harness/blob/691f09f7659fa9e0c3741f93e4e8e69293ac7aa5/app/agent/nodes.py#L181-L221), [README.md](https://github.com/RameshKatla/ai-agent-harness/blob/691f09f7659fa9e0c3741f93e4e8e69293ac7aa5/README.md#L218-L255), [app/agent/policies.py](https://github.com/RameshKatla/ai-agent-harness/blob/691f09f7659fa9e0c3741f93e4e8e69293ac7aa5/app/agent/policies.py#L18-L37)
- Basis: Structural evidence from pinned first-party source.
- Confidence: high
- Caveats: A newly declared preference can replace the previous user preference.

### Absence scope

- Surfaces inspected: Memory retrieval and writes, configuration and evaluation result access.
- Plausible first-party paths checked: External trends or performance changes choosing a prospective option and returning it to installed operation.
- Why no material first-party path remains: The supplied memory path carries preferences and episodes. Neither it nor standalone evaluation selects and installs an adaptation.

## S5 — Policy and identity

- State: —
- Function: Ultimate purpose or operating policy governance was sought at the service boundary.
- Disturbance / variety regulated: Task demands may collide with capability rights or installation policy.
- Decisive decision or feedback right: No supplied escalation and return path resolves an identity or ultimate policy issue.
- Decision owner: The installer sets static policy. Authenticated users choose requests and permitted approvals.
- Supporting / enforcement mechanisms: Permissions, settings, task-level approval and policy exceptions.
- Closure path: Requests execute or fail under the supplied constraints. The approval does not amend those constraints.
- Why this is / is not agent-owned: The model is bounded by the configured policy. No shipped actor settles identity-level disputes and returns a new policy.
- Evidence: [README.md](https://github.com/RameshKatla/ai-agent-harness/blob/691f09f7659fa9e0c3741f93e4e8e69293ac7aa5/README.md#L82-L104), [app/agent/policies.py](https://github.com/RameshKatla/ai-agent-harness/blob/691f09f7659fa9e0c3741f93e4e8e69293ac7aa5/app/agent/policies.py#L18-L51), [app/api/routes_agent.py](https://github.com/RameshKatla/ai-agent-harness/blob/691f09f7659fa9e0c3741f93e4e8e69293ac7aa5/app/api/routes_agent.py#L46-L69)
- Basis: Structural evidence from pinned first-party source.
- Confidence: medium
- Caveats: Repository governance is outside the assessed deployment.

### Absence scope

- Surfaces inspected: Policy and approval source, API boundaries and user memory controls.
- Plausible first-party paths checked: Internal choice of system mission or parent adjudication that returns an authoritative policy change.
- Why no material first-party path remains: The endpoints apply existing policy to actions and memory. They do not admit policy issues for governing judgment.

## Recursion

A deployment hosts independent thread operations. Graph nodes and tool calls are phases and support for the same task and do not introduce additional nested organizations.

## Variety and escalation

Structured decisions, access controls, time and step limits, retries and checkpointing attenuate ordinary operational variety. Approval returns to the same graph. No separate exceptional channel to parent authority was identified.

## Evidence gaps

Static source review. No live model, Postgres, approval round trip, evaluation or concurrency test was executed. The external model and service implementations were outside the system boundary.

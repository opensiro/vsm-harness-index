---
harness_id: fetch
project_name: Fetch
repository: https://github.com/Traves-Theberge/Fetch
review_ref: efb6e0b4a8b72e436929b44a355a29d02e72a221
reviewed_at: 2026-11-16
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: P
---

# Fetch

## Review boundary

- System in focus: One self-hosted Fetch bridge and its chat sessions, shared delegated-task slot and Kennel execution interface.
- Purpose and identity: Turn authorized chat requests into workspace and coding outcomes, optionally via a delegated coding harness.
- Relevant environment: Authorized WhatsApp users, repo/workspace contents, external model providers, CLI backends and other configured channels.
- Standard-distribution boundary: Shipped bridge, session and task runtime, bundled tools and workflows, Kennel execution wrapper and supported host manager.
- Credited operating / distribution surfaces: Model-backed bridge loop and scoped tools, shared task state and model/owner interventions, WhatsApp owner trust control.
- Adjacent first-party surfaces excluded from ownership: Repository CI, developer tests, example workflows and independently owned coding harness internals or hosted service decisions.
- First-party operating / deployment modes considered: Self-hosted WhatsApp bridge, project/task operations, deterministic operator commands and composed workflow/cron execution.
- Recursion level: One bridge deployment. Model-backed channel sessions are local operating cells sharing the delegated task slot.
- Reviewed revision: `efb6e0b4a8b72e436929b44a355a29d02e72a221`
- Observation date: 2026-11-16
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

Fetch runs an authorized channel bridge with a model and tool loop, a per-session run state machine, a process-wide task manager, and a containerized environment for workspace commands and delegated CLI runs. The task manager owns persisted execution state. External harness agents supply delegated operations without transferring their deeper ownership claims. [`README.md`](https://github.com/Traves-Theberge/Fetch/blob/efb6e0b4a8b72e436929b44a355a29d02e72a221/README.md#L294-L337), [`fetch-app/src/handler/index.ts`](https://github.com/Traves-Theberge/Fetch/blob/efb6e0b4a8b72e436929b44a355a29d02e72a221/fetch-app/src/handler/index.ts#L263-L317), [`fetch-app/src/handler/index.ts`](https://github.com/Traves-Theberge/Fetch/blob/efb6e0b4a8b72e436929b44a355a29d02e72a221/fetch-app/src/handler/index.ts#L344-L378), [`fetch-app/src/tools/task.ts`](https://github.com/Traves-Theberge/Fetch/blob/efb6e0b4a8b72e436929b44a355a29d02e72a221/fetch-app/src/tools/task.ts#L140-L176), [`fetch-app/src/task/manager.ts`](https://github.com/Traves-Theberge/Fetch/blob/efb6e0b4a8b72e436929b44a355a29d02e72a221/fetch-app/src/task/manager.ts#L482-L498).

## Operational model

Each authorized user session can act on its local chat/workspace task through a model-driven tool loop. Independent sessions can contend for a single bridge-wide delegated execution slot. Fetch can observe and regulate that current slot, while an alternate operator route can stop it directly. The configured owner controls the separate admission policy for future WhatsApp requests.

## S1 — Operations

- State: A
- Function: Produce workspace, research and delegated coding outcomes on user requests.
- Disturbance / variety regulated: Uncertain work state, varied user requests, and tool/provider responses.
- Decisive decision or feedback right: Choose and execute tools, adapt after each result and complete or delegate the task.
- Decision owner: The Fetch model-backed agent in the channel session.
- Supporting / enforcement mechanisms: Bridge, provider transport, session loop, tool registry, Kennel and optional harness drivers.
- Closure path: Tool execution results are persisted into the active session and fed into later model decisions before returning replies or starting a task.
- Why this is / is not agent-owned: The model selects workspace and task actions. The registry and adapter implement selected calls.
- Evidence: [`fetch-app/src/handler/index.ts`](https://github.com/Traves-Theberge/Fetch/blob/efb6e0b4a8b72e436929b44a355a29d02e72a221/fetch-app/src/handler/index.ts#L313-L358), [`fetch-app/src/agent/core.ts`](https://github.com/Traves-Theberge/Fetch/blob/efb6e0b4a8b72e436929b44a355a29d02e72a221/fetch-app/src/agent/core.ts#L759-L807), [`fetch-app/src/agent/core.ts`](https://github.com/Traves-Theberge/Fetch/blob/efb6e0b4a8b72e436929b44a355a29d02e72a221/fetch-app/src/agent/core.ts#L830-L869), [`fetch-app/src/tools/task.ts`](https://github.com/Traves-Theberge/Fetch/blob/efb6e0b4a8b72e436929b44a355a29d02e72a221/fetch-app/src/tools/task.ts#L157-L176)
- Basis: structural
- Confidence: High for shipped source reachability.
- Caveats: Delegated harness internals are external. The Fetch lead's own model/tool loop supplies S1.
- Boundary reachability: The bundled bridge invokes the shipped processMessage loop and task tools in the supported channel mode.

## S2 — Coordination

- State: A
- Function: Prevent independently active chat sessions from taking incompatible concurrent commitments on the bridge's shared delegated slot.
- Disturbance / variety regulated: Two authorized sessions can issue coding requests while the same process-wide task slot is occupied.
- Decisive decision or feedback right: Act on active-slot and task status feedback to defer a competing start or coordinate a changed commitment.
- Decision owner: Fetch models in the calling sessions. The process-wide task manager enforces the single-slot rule.
- Supporting / enforcement mechanisms: Session-scoped model runs, singleton task manager, tracked task IDs and busy error with existing-task context.
- Closure path: A competing start is rejected with the current task ID and a path for follow-up control. The requesting model receives the refusal and can defer or route a change, and a terminal release allows a later start.
- Why this is / is not agent-owned: The slot check is deterministic. The calling model owns its subsequent choice of actions or feedback based on the identified competing commitment.
- Evidence: [`fetch-app/src/handler/index.ts`](https://github.com/Traves-Theberge/Fetch/blob/efb6e0b4a8b72e436929b44a355a29d02e72a221/fetch-app/src/handler/index.ts#L284-L317), [`fetch-app/src/session/manager.ts`](https://github.com/Traves-Theberge/Fetch/blob/efb6e0b4a8b72e436929b44a355a29d02e72a221/fetch-app/src/session/manager.ts#L53-L87), [`fetch-app/src/task/manager.ts`](https://github.com/Traves-Theberge/Fetch/blob/efb6e0b4a8b72e436929b44a355a29d02e72a221/fetch-app/src/task/manager.ts#L110-L154), [`fetch-app/src/task/manager.ts`](https://github.com/Traves-Theberge/Fetch/blob/efb6e0b4a8b72e436929b44a355a29d02e72a221/fetch-app/src/task/manager.ts#L482-L498), [`fetch-app/src/tools/task.ts`](https://github.com/Traves-Theberge/Fetch/blob/efb6e0b4a8b72e436929b44a355a29d02e72a221/fetch-app/src/tools/task.ts#L140-L165), [`fetch-app/src/agent/core.ts`](https://github.com/Traves-Theberge/Fetch/blob/efb6e0b4a8b72e436929b44a355a29d02e72a221/fetch-app/src/agent/core.ts#L830-L869)
- Basis: structural
- Confidence: Moderate for the bounded allocation disturbance.
- Caveats: The witness concerns contention for the singleton delegated slot. It supplies no general multi-task file-level arbitration.
- Boundary reachability: Independent authorized channel sessions converge on the same singleton through the bundled task_create tool.
- Distinct S1 units: Independently running model-backed channel sessions handling different user requests.
- Inter-S1 disturbance: Both can try to submit a delegated job when only one active job can use the shared slot.
- Attenuating coordination relation: Singleton task admission and the corrective busy response naming the conflicting active job.
- Feedback into subsequent S1 behaviour: The caller receives the conflict as a tool result, so its next action can defer or seek a justified changed commitment rather than launching another job.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: These calls meet on a concrete exclusive shared capacity. The busy result changes the requesting unit's subsequent action.

## S3 — Inside-and-now control

- State: A(P)
- Function: Regulate an already active bridge-wide delegated commitment.
- Disturbance / variety regulated: An occupied slot may be blocked or the active work may need to change direction.
- Decisive decision or feedback right: Inspect the current commitment and choose whether and what to cancel or replace in the currently authorized task scope.
- Decision owner: The Fetch model in the tool-led path, and the authorized channel operator in the distinct deterministic command path.
- Supporting / enforcement mechanisms: Task status/index, cancel tool, active process termination and persisted task transitions.
- Closure path: Cancellation targets the running process when present and clears the current-task pointer, then returns outcome state. Subsequent tool work can start on the released capacity.
- Why this is / is not agent-owned: The model or operator selects the discretionary intervention. The manager and the adapter apply it.
- Evidence: [`fetch-app/src/agent/response-policy.ts`](https://github.com/Traves-Theberge/Fetch/blob/efb6e0b4a8b72e436929b44a355a29d02e72a221/fetch-app/src/agent/response-policy.ts#L164-L203), [`fetch-app/src/tools/task.ts`](https://github.com/Traves-Theberge/Fetch/blob/efb6e0b4a8b72e436929b44a355a29d02e72a221/fetch-app/src/tools/task.ts#L243-L281), [`fetch-app/src/tools/task.ts`](https://github.com/Traves-Theberge/Fetch/blob/efb6e0b4a8b72e436929b44a355a29d02e72a221/fetch-app/src/tools/task.ts#L333-L374), [`fetch-app/src/task/manager.ts`](https://github.com/Traves-Theberge/Fetch/blob/efb6e0b4a8b72e436929b44a355a29d02e72a221/fetch-app/src/task/manager.ts#L285-L305), [`fetch-app/src/handler/index.ts`](https://github.com/Traves-Theberge/Fetch/blob/efb6e0b4a8b72e436929b44a355a29d02e72a221/fetch-app/src/handler/index.ts#L292-L311), [`fetch-app/src/commands/task.ts`](https://github.com/Traves-Theberge/Fetch/blob/efb6e0b4a8b72e436929b44a355a29d02e72a221/fetch-app/src/commands/task.ts#L53-L80)
- Basis: structural
- Confidence: Moderate to high for current one-slot control.
- Caveats: An explicit user order to cancel is parent-owned. The base witness is model choice of intervention from returned current-task state within its task authority.
- Boundary reachability: The first-party task tool group exposes status and cancellation. The direct /stop route reaches the same underlying commitment without a model turn.
- Whole-system current view: The entire currently admitted delegated workload is one active task. The most recent status/progress can be retrieved by default active-task lookup and operator status.
- Current-control decision scope: Cancel or replace the active bridge-wide delegated commitment and free the shared execution slot.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Fetch lead model | Current status or occupied-slot response changes the handling of an authorized request | Select whether or which task to cancel and then consume the result and newly available slot. | [`fetch-app/src/tools/task.ts`](https://github.com/Traves-Theberge/Fetch/blob/efb6e0b4a8b72e436929b44a355a29d02e72a221/fetch-app/src/tools/task.ts#L140-L165), [`fetch-app/src/tools/task.ts`](https://github.com/Traves-Theberge/Fetch/blob/efb6e0b4a8b72e436929b44a355a29d02e72a221/fetch-app/src/tools/task.ts#L243-L281), [`fetch-app/src/tools/task.ts`](https://github.com/Traves-Theberge/Fetch/blob/efb6e0b4a8b72e436929b44a355a29d02e72a221/fetch-app/src/tools/task.ts#L347-L374) |
| Parent (`P`) | Authorized channel operator | Operator sees active focus or progress and directly decides it should stop | Direct command aborts active session work and cancels the delegated task without asking the model to choose. | [`fetch-app/src/agent/format.ts`](https://github.com/Traves-Theberge/Fetch/blob/efb6e0b4a8b72e436929b44a355a29d02e72a221/fetch-app/src/agent/format.ts#L20-L49), [`fetch-app/src/handler/index.ts`](https://github.com/Traves-Theberge/Fetch/blob/efb6e0b4a8b72e436929b44a355a29d02e72a221/fetch-app/src/handler/index.ts#L292-L311), [`fetch-app/src/commands/task.ts`](https://github.com/Traves-Theberge/Fetch/blob/efb6e0b4a8b72e436929b44a355a29d02e72a221/fetch-app/src/commands/task.ts#L53-L80) |

## S3* — Complementary audit

- State: —
- Function: No shipped audit path independently samples and adjudicates delegated work as a control loop.
- Disturbance / variety regulated: Delegated runner summaries may differ from actual working-tree or application outcome.
- Decisive decision or feedback right: The installed task result path records the runner outcome. Application and browser checks are exposed separately as caller-selected tests.
- Decision owner: Task adapter and orchestrator own ordinary operational checks. No independent auditor with corrective authority is evidenced.
- Supporting / enforcement mechanisms: Task result mapping, status/notifications, shipped application and browser test tools, workflow automation.
- Closure path: Normal completion is recorded from the harness result. Caller-defined workflows can inspect artifacts but the reviewed distribution does not bind them as independent task audit with a corrective return.
- Why this is / is not agent-owned: Different containers or a test tool do not establish independent audit judgment on their own.
- Evidence: [`fetch-app/src/task/integration.ts`](https://github.com/Traves-Theberge/Fetch/blob/efb6e0b4a8b72e436929b44a355a29d02e72a221/fetch-app/src/task/integration.ts#L335-L365), [`fetch-app/src/skills/builtin/task-orchestration/SKILL.md`](https://github.com/Traves-Theberge/Fetch/blob/efb6e0b4a8b72e436929b44a355a29d02e72a221/fetch-app/src/skills/builtin/task-orchestration/SKILL.md#L21-L37), [`fetch-app/src/skills/builtin/workflow-automation/SKILL.md`](https://github.com/Traves-Theberge/Fetch/blob/efb6e0b4a8b72e436929b44a355a29d02e72a221/fetch-app/src/skills/builtin/workflow-automation/SKILL.md#L17-L44), [`fetch-app/src/tools/workflow.ts`](https://github.com/Traves-Theberge/Fetch/blob/efb6e0b4a8b72e436929b44a355a29d02e72a221/fetch-app/src/tools/workflow.ts#L391-L498)
- Basis: structural
- Confidence: Moderate.
- Caveats: A deployment can explicitly arrange independent validation using these tools, but no supplied audit-specific ownership loop was established.

### Absence scope

- Surfaces inspected: Delegated completion, result/notification pipeline, workflow test tools, built-in orchestration/automation guidance and repository tests.
- Plausible first-party paths checked: Independent follow-up app or browser check, workflow assertion, and external runner-reported results.
- Why no material first-party path remains: Completion consumes the producer-facing harness result. The tests operate as explicitly requested workflow actions, with no supplied audit trigger, separate adjudicator and findings-to-control binding.

## S4 — Outside-and-then intelligence

- State: —
- Function: No prospective environmental adaptation loop was established in the reviewed operating surface.
- Disturbance / variety regulated: Project differences, saved experience and external software versions vary over time.
- Decisive decision or feedback right: Retain contextual notes or apply a prescribed release according to an operator-selected action. No first-party adaptive judgment from environmental observations was established.
- Decision owner: The operator owns deployment choices. Note extraction and release application are automatic support.
- Supporting / enforcement mechanisms: Session memory and summaries, workflow persistence, manifest updates and host manager.
- Closure path: Persisted notes and workflows influence subsequent tasks. The host updater installs the selected channel's release. These paths do not develop and choose a case-specific future operating capability from the environment.
- Why this is / is not agent-owned: Applying released code or replaying a saved routine is supplied maintenance and operation, with no independent prospective capability decision established.
- Evidence: [`fetch-app/src/agent/core.ts`](https://github.com/Traves-Theberge/Fetch/blob/efb6e0b4a8b72e436929b44a355a29d02e72a221/fetch-app/src/agent/core.ts#L1080-L1113), [`fetch-app/src/session/manager.ts`](https://github.com/Traves-Theberge/Fetch/blob/efb6e0b4a8b72e436929b44a355a29d02e72a221/fetch-app/src/session/manager.ts#L414-L444), [`fetch-app/src/skills/builtin/workflow-automation/SKILL.md`](https://github.com/Traves-Theberge/Fetch/blob/efb6e0b4a8b72e436929b44a355a29d02e72a221/fetch-app/src/skills/builtin/workflow-automation/SKILL.md#L17-L39), [`manager/main.go`](https://github.com/Traves-Theberge/Fetch/blob/efb6e0b4a8b72e436929b44a355a29d02e72a221/manager/main.go#L785-L791), [`manager/main.go`](https://github.com/Traves-Theberge/Fetch/blob/efb6e0b4a8b72e436929b44a355a29d02e72a221/manager/main.go#L1254-L1264), [`manager/main.go`](https://github.com/Traves-Theberge/Fetch/blob/efb6e0b4a8b72e436929b44a355a29d02e72a221/manager/main.go#L1435-L1478), [`scripts/fetch-cli.sh`](https://github.com/Traves-Theberge/Fetch/blob/efb6e0b4a8b72e436929b44a355a29d02e72a221/scripts/fetch-cli.sh#L64-L68)
- Basis: structural
- Confidence: Moderate at the deployed bridge boundary.
- Caveats: A separately configured research or policy workflow could implement a closed S4 process.

### Absence scope

- Surfaces inspected: Prompt memory pipeline, saved workflows and cron, host manager version/update handling, and project context tools.
- Plausible first-party paths checked: Memory-derived learning, external release detection, and creating a repeatable project workflow.
- Why no material first-party path remains: The supplied paths preserve context or apply chosen configuration and prescribed releases. They do not establish a first-party process developing and returning an adaptation decision among future capability alternatives.

## S5 — Policy and identity

- State: P
- Function: Maintain the deployment's ultimate policy for which principals may direct Fetch through WhatsApp.
- Disturbance / variety regulated: Whether an additional requester should permanently be admitted or an existing requester should lose access.
- Decisive decision or feedback right: Decide an add/revoke issue and return the authoritative admission decision into the bridge policy.
- Decision owner: The configured deployment owner, who alone can use the channel trust-control command.
- Supporting / enforcement mechanisms: Sender identity gate, persisted whitelist and bridged command parser.
- Closure path: Owner decision is written to the shared whitelist backing subsequent request admission. Future requests from the affected principal are accepted or refused according to the returned decision.
- Why this is / is not agent-owned: The model has no role in deciding these grants. The direct owner command and subsequent bridge gate supply the evidenced policy loop.
- Evidence: [`fetch-app/src/commands/parser.ts`](https://github.com/Traves-Theberge/Fetch/blob/efb6e0b4a8b72e436929b44a355a29d02e72a221/fetch-app/src/commands/parser.ts#L168-L173), [`fetch-app/src/commands/trust.ts`](https://github.com/Traves-Theberge/Fetch/blob/efb6e0b4a8b72e436929b44a355a29d02e72a221/fetch-app/src/commands/trust.ts#L16-L68), [`fetch-app/src/security/whitelist.ts`](https://github.com/Traves-Theberge/Fetch/blob/efb6e0b4a8b72e436929b44a355a29d02e72a221/fetch-app/src/security/whitelist.ts#L217-L274), [`fetch-app/src/security/gate.ts`](https://github.com/Traves-Theberge/Fetch/blob/efb6e0b4a8b72e436929b44a355a29d02e72a221/fetch-app/src/security/gate.ts#L188-L219), [`fetch-app/src/bridge/client.ts`](https://github.com/Traves-Theberge/Fetch/blob/efb6e0b4a8b72e436929b44a355a29d02e72a221/fetch-app/src/bridge/client.ts#L704-L725)
- Basis: structural
- Confidence: High for the source-backed WhatsApp admission policy route.
- Caveats: The grant scope is who may issue requests through the declared WhatsApp bridge. Environment-supplied membership and other channel authorization remain separate.
- Boundary reachability: The standard WhatsApp ingress accepts owner-authorized commands and routes /trust to the shared whitelist consulted on later ingress.
- Identity / ultimate-policy issue: Decide who is allowed to direct this deployment, beyond authorizing a particular tool call or task.
- Ultimate authority in each claimed mode: The deployment owner identified by configuration and checked before whitelist change.
- Return-to-operation path: Owner issues add/revoke, whitelist state persists, and later bridge ingress applies that durable result.

## Distributed OSS parent arrangement

The local deployment owner is the parent for WhatsApp admission policy. The repo's maintainers own release decisions outside the assessed bridge recursion.

## Self-hosted and non-human modes

The supported self-hosted bridge, workspace and Kennel execute with configured model/CLI backends. Deterministic parent commands remain a separate supported mode.

## Recursion

One bridge deployment. Concurrent user sessions act as work units and share the bridge's one active delegated commitment.

## Variety and escalation

The bridge gates ingress, uses per-session and shared task capacity, and exposes model and parent stop paths. This does not establish a distinct algedonic signal channel.

## Evidence gaps

Review is source-based at the pinned commit. The behavior of external models and delegated CLIs, and permissions for other channel deployments, were not independently run.

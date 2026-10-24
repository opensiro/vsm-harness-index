---
harness_id: routa
project_name: Routa
repository: https://github.com/phodal/routa
review_ref: 9dc7b7be8fa92b760f6ebf0ac7f8b44db1b4dc34
reviewed_at: 2026-10-24
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Routa

## Review boundary

- System in focus: Routa's supported local/workspace multi-agent software-delivery operation, including the shipped ROUTA coordinator, CRAFTER implementor and GATE verifier specialist configurations and ACP agent-session runtime. A generic empty board or an isolated user-selected ACP CLI is not the whole assessed mode.
- Purpose and identity: Deliver scoped software changes through agent-owned decomposition, implementation, conflict coordination, current supervision and complementary verification with recoverable task/session state.
- Relevant environment: Changing requirements, repository code, conflicting agent edits, runtime/session failures, workload competition, incorrect implementation reports and insufficient test or review evidence.
- Standard-distribution boundary: Shipped Next.js and local Tauri/Axum surfaces; first-party workspace stores, ACP adapters, coordinator/delegation tools, task/kanban execution and role-specific prompts; installed supported external model/provider supplies model inference. This is a **composed shipped agent mode**, not a claim that Routa implements its own model.
- Credited operating / distribution surfaces: [architecture and supported modes](https://github.com/phodal/routa/blob/9dc7b7be8fa92b760f6ebf0ac7f8b44db1b4dc34/docs/ARCHITECTURE.md#L15-L57), [coordinator and specialist workflow](https://github.com/phodal/routa/blob/9dc7b7be8fa92b760f6ebf0ac7f8b44db1b4dc34/resources/specialists/core/routa.yaml#L1-L55), [orchestrator delegation and ACP spawn](https://github.com/phodal/routa/blob/9dc7b7be8fa92b760f6ebf0ac7f8b44db1b4dc34/src/core/orchestration/orchestrator.ts#L490-L712), [independent GATE configuration](https://github.com/phodal/routa/blob/9dc7b7be8fa92b760f6ebf0ac7f8b44db1b4dc34/resources/specialists/core/gate.yaml#L1-L70), [review verdict routing](https://github.com/phodal/routa/blob/9dc7b7be8fa92b760f6ebf0ac7f8b44db1b4dc34/src/core/kanban/review-lane-convergence.ts#L24-L59).
- Adjacent first-party surfaces excluded from ownership: Project contributor/maintainer governance and releases; architectural design proposals; automated repository fitness/CI and its development-only pre-push hooks; source tests/fixtures; preview/demo flows; manually created cards without an installed actor; generic REST/MCP integration clients; independently operated Claude/Codex/other model providers and their own higher-level agent governance.
- First-party operating / deployment modes considered: Standalone recoverable ACP Sessions, coordinator-led Team agent delegation, agent-driven Kanban lane automation and review, web/backend and self-hosted local desktop; user-defined provider/model and user-approved initial plans. The shipped bundled-specialist path is decisive for positive agent ownership; plain manual use of the UI is not enough.
- Recursion level: One local workspace software-delivery organization comprising multiple cooperating implementor/verifier S1 cells; not Routa's OSS maintainer community or every agent behind an external provider.
- Reviewed revision: `9dc7b7be8fa92b760f6ebf0ac7f8b44db1b4dc34` as frozen in [intake #2012](https://github.com/opensiro/vsm-harness-index/issues/2012) and [serial batch #2013](https://github.com/opensiro/vsm-harness-index/issues/2013).
- Observation date: 2026-10-24.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The first-party `RoutaSystem` wires agent, task, conversation, note, session, event and permission stores and exposes role-specific agent tools. The ACP process manager and provider adapters start external model-backed agents and return their messages/results; the Rust desktop/server path provides a second host for equivalent workspace concepts. The delegation implementation creates a child agent, gives it a task-specific prompt and session, starts its provider and reports completion to the original coordinator session. `waitMode=after_all` groups child completions before waking the parent. Thus the repository supplies the operating structure, but the *choices* of the composed model-backed roles are not authored by a deterministic scheduling loop. [architecture](https://github.com/phodal/routa/blob/9dc7b7be8fa92b760f6ebf0ac7f8b44db1b4dc34/docs/ARCHITECTURE.md#L64-L170), [delegation code](https://github.com/phodal/routa/blob/9dc7b7be8fa92b760f6ebf0ac7f8b44db1b4dc34/src/core/orchestration/orchestrator.ts#L490-L735), [completion feedback](https://github.com/phodal/routa/blob/9dc7b7be8fa92b760f6ebf0ac7f8b44db1b4dc34/src/core/orchestration/orchestrator.ts#L1230-L1408).

The Kanban path launches roles on column transitions and has a per-board `KanbanSessionQueue`; deterministic capacity checks and stale-entry cleanup constrain concurrency, while agent specialists choose work or review judgments. GATE can inspect a separate implementor's artifact and return `APPROVED`, `NOT_APPROVED` or `BLOCKED`, and review-lane convergence routes those verdicts to Done, Dev or Blocked. A queue or lane name alone would not establish agent ownership, but here it carries decisions of the shipped specialist actors. [queue](https://github.com/phodal/routa/blob/9dc7b7be8fa92b760f6ebf0ac7f8b44db1b4dc34/src/core/kanban/kanban-session-queue.ts#L55-L123), [orchestrator](https://github.com/phodal/routa/blob/9dc7b7be8fa92b760f6ebf0ac7f8b44db1b4dc34/src/core/kanban/workflow-orchestrator.ts#L1-L20), [verdict convergence](https://github.com/phodal/routa/blob/9dc7b7be8fa92b760f6ebf0ac7f8b44db1b4dc34/src/core/kanban/review-lane-convergence.ts#L24-L59).

## Operational model

An operator configures workspace, repository and external ACP provider. In the shipped coordinator path the model-backed ROUTA role writes a specification and task blocks, requests initial plan approval, and then independently selects/delegates implementation waves. Separate CRAFTER agents inspect the repository, work and report; GATE agents receive another role and verify the implementation claims. Reports, review verdicts and completion/failure events return into coordinator and/or board operations for another wave, repair or stop. Neither an unconfigured UI nor deterministic board transitions alone would constitute this autonomous mode. [supported example](https://github.com/phodal/routa/blob/9dc7b7be8fa92b760f6ebf0ac7f8b44db1b4dc34/README.md#L72-L105), [coordinator instructions](https://github.com/phodal/routa/blob/9dc7b7be8fa92b760f6ebf0ac7f8b44db1b4dc34/resources/specialists/core/routa.yaml#L1-L56).

## S1 — Operations

- State: A
- Function: Carry out a bounded software implementation or verification task using a model-backed CRAFTER/GATE or ordinary supported agent session.
- Disturbance / variety regulated: Unknown repository layout, changing test outcomes, error messages, incomplete acceptance evidence and tool-execution results.
- Decisive decision or feedback right: The installed provider-backed role reads the task and repository observations and chooses which edits, tests, queries or further actions to perform; the task/result feedback can change the next decision.
- Decision owner: The composed autonomous CRAFTER/GATE or session agent, not the ACP transport, fixed board scheduler or person selecting a provider.
- Supporting / enforcement mechanisms: Bundled specialist role prompts, ACP process spawning, workspace/scoped task state, tools, traces, test commands, sandboxes and status updates.
- Closure path: Task → agent action and observed code/test result → subsequent agent decision → report/verdict and durable task state.
- Boundary reachability: Standard Team/Kanban configurations explicitly ship the roles, prompt contracts and ACP spawn path, so user integration code is not needed beyond installing/configuring a supported provider.
- Why this is / is not agent-owned: Inference and selected code actions are external-provider computation, but Routa's shipped role adapters purposefully compose that actor into an operating task loop. Bare Kanban automation is not independently credited as an agent.
- Evidence: [CRAFTER contract](https://github.com/phodal/routa/blob/9dc7b7be8fa92b760f6ebf0ac7f8b44db1b4dc34/src/core/orchestration/specialist-prompts.ts#L108-L137); [delegation and execution](https://github.com/phodal/routa/blob/9dc7b7be8fa92b760f6ebf0ac7f8b44db1b4dc34/src/core/orchestration/orchestrator.ts#L490-L712); [session guide](https://github.com/phodal/routa/blob/9dc7b7be8fa92b760f6ebf0ac7f8b44db1b4dc34/docs/use-routa/sessions.md#L1-L36).
- Basis: Supported composition with a separate decision-making agent actor and action/observation loop.
- Confidence: High for shipped wiring; functional quality of model output not benchmarked.
- Caveats: No live model/provider run was conducted for this index assessment.

## S2 — Coordination

- State: A
- Function: Regulate interference between concurrently operating CRAFTER cells on tasks in one workspace.
- Disturbance / variety regulated: Two implementors choosing overlapping files or incompatible changes, duplicate work, and contention for the board's finite concurrent execution slots.
- Decisive decision or feedback right: Bundled model-backed coordinator/implementors are instructed to inspect other active agents and their scope, message the affected agent or parent and adjust assignments/actions; the board's deterministic queue separately enforces configured capacity.
- Decision owner: In the shipped Team mode, coordinator and implementor agents make the discretionary interference judgments; the fixed queue owns neither assignment priorities nor the model's conflict-resolution decision.
- Supporting / enforcement mechanisms: `list_agents`, `read_agent_conversation`, `send_message_to_agent`, scoped tasks, working directories, `waitMode=after_all` and concurrency queue.
- Closure path: Concurrent S1 actor status/scope → model-backed conflict check/communication → changed file choice, work timing or escalation → resumed individual S1 behavior. Queue events also prevent a second S1 starting before capacity releases.
- Boundary reachability: The bundled CRAFTER prompt explicitly requires an active-agent conflict preflight and parent notification, with corresponding first-party tools and ACP messaging in the supported setup.
- Why this is / is not agent-owned: Only the shipped agent's discretionary conflict response supports `A`; an event bus, message API, queue or hard semaphore by itself would not.
- Distinct S1 units: At least two separately spawned CRAFTER agents undertaking different task blocks, potentially sharing a repository/workspace.
- Inter-S1 disturbance: File/feature overlap, incompatible changes and oversubscribed board slots from parallel task execution.
- Attenuating coordination relation: Before editing, a CRAFTER checks other agents and sends a coordination/escalation message; the ROUTA model can divide tasks into isolated scopes or regroup work; board concurrency imposes a deterministic upper bound.
- Feedback into subsequent S1 behaviour: The agent changes its scope, asks parent to reassign, or waits; the queue releases another task on predecessor completion.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The bundled preflight is explicitly tied to **avoiding concurrent file conflicts**, with actionable cross-agent status and returned messages. The queue is a second anti-contention witness, not the sole justification.
- Evidence: [conflict preflight in bundled CRAFTER role](https://github.com/phodal/routa/blob/9dc7b7be8fa92b760f6ebf0ac7f8b44db1b4dc34/src/core/orchestration/specialist-prompts.ts#L108-L133), [agent tools](https://github.com/phodal/routa/blob/9dc7b7be8fa92b760f6ebf0ac7f8b44db1b4dc34/src/core/tools/agent-tools.ts#L1-L25), [bounded concurrency and lifecycle](https://github.com/phodal/routa/blob/9dc7b7be8fa92b760f6ebf0ac7f8b44db1b4dc34/src/core/kanban/kanban-session-queue.ts#L55-L112).
- Basis: Agent-discretionary anti-overlap instruction and first-party cross-agent feedback in the shipped composed Team mode.
- Confidence: Medium; active-agent conflict checks are prompt-level rather than enforced hard locks.
- Caveats: No measured rate of conflict avoidance; deterministic queue tests establish queue behavior, not model compliance with prompts.

## S3 — Inside-and-now control

- State: A
- Function: Maintain an actionable current view of implementation commitments and change which agents/tasks/waves are active in response to reported progress and failure.
- Disturbance / variety regulated: Incomplete waves, failing verifications, mismatched task scopes, agent stalls, failed provider sessions and changing prioritization of current delivery work.
- Decisive decision or feedback right: The model-backed ROUTA coordinator decides decomposition, who gets a task, the next wave, whether to request GATE verification, whether failed work needs another CRAFTER and when to finalize a spec.
- Decision owner: The deployed ROUTA coordinator model/agent. The human's required **initial plan approval** constrains the mandate but does not itself execute the subsequent agent-owned current-control wave and repair decisions.
- Supporting / enforcement mechanisms: Workspace-wide agent/task listing, spec notes, `@@@task` parser, task statuses, child delegation, completion-group collation, wake-parent messages, review verdicts and watchdog/queue limits.
- Closure path: Whole-workspace tasks/agents and child reports → coordinator assessment of current state → selected agent assignments or repair wave → new child sessions → completion signals returned to coordinator.
- Boundary reachability: The standard bundled coordinator prompt mandates the entire wave/verify/repair workflow, and `RoutaOrchestrator.wakeParent` prompts the actual coordinator session with child results, re-entering agent discretion.
- Why this is / is not agent-owned: The decisive present-work portfolio choice is performed by an agent at the parent-of-S1 scope. A static column sequence, depth limit or queue max would only enforce that choice, not own it.
- Whole-system current view: Spec note and scoped task list, `list_agents` and agent conversations, completed/active statuses, child results and report/verification summaries for one workspace.
- Current-control decision scope: Decomposition, assignments, batches/waves, interventions after failed verification and integration or completion of current commitments; not provider-wide global budgets or OSS contributor governance.
- Evidence: [ROUTA control contract](https://github.com/phodal/routa/blob/9dc7b7be8fa92b760f6ebf0ac7f8b44db1b4dc34/resources/specialists/core/routa.yaml#L10-L67), [spawning and task assignment](https://github.com/phodal/routa/blob/9dc7b7be8fa92b760f6ebf0ac7f8b44db1b4dc34/src/core/orchestration/orchestrator.ts#L490-L735), [feedback wakes coordinator](https://github.com/phodal/routa/blob/9dc7b7be8fa92b760f6ebf0ac7f8b44db1b4dc34/src/core/orchestration/orchestrator.ts#L1294-L1408).
- Basis: Agent-owned discretionary current control in packaged coordinator mode; no additional `(P)` mode claimed from simple approval or dashboard intervention.
- Confidence: Medium-high for supported path, without evidence of deployed model reliability.
- Caveats: Human approves the initial specification; the path assessed is subsequent bounded agent control, not independent organizational charter changes.

## S3* — Complementary audit

- State: A
- Function: Independently check CRAFTER implementation and completion claims against the original acceptance criteria, with verdicts returned into current coordination.
- Disturbance / variety regulated: Self-serving or mistaken implementation success reports, untested code, missing requirements, scope creep and incomplete evidence.
- Decisive decision or feedback right: A separately spawned, model-backed GATE role examines the specification, implementation changes and tests and chooses APPROVED/NOT APPROVED/BLOCKED; it need not accept the CRAFTER's own report.
- Decision owner: A distinct verifier agent session, not the acting CRAFTER or a deterministic policy regex.
- Supporting / enforcement mechanisms: Read-only verification role contract, access to task/spec and agent conversations, test/diff evidence, verification verdict storage and review-column routing.
- Closure path: Acting agent claims completion → separate verifier obtains spec, diff/tests and reports → verifier produces verdict → ROUTA receives report and/or board returns to Dev/Blocked or advances to Done.
- Boundary reachability: The standard ROUTA specialist workflow explicitly launches a separate GATE agent after CRAFTER completion; the GATE role and review-verdict feedback path are bundled, not custom add-ons.
- Why this is / is not agent-owned: Verifier performs its own evidence judgment; lane transitions and deterministic fitness checks carry/enforce its output but do not replace it. Independence is **role/session separation**, not a guarantee of different provider or institutional independence.
- Claim being audited: CRAFTER's statement that an implementation satisfies the task and tests.
- Ordinary reporting path: CRAFTER reports files changed, verification performed and success through `report_to_parent`/task state.
- Complementary access path: GATE separately reads the original spec, developer conversation, diffs, commits and test evidence through its own session/tools.
- Independence boundary: Separate verifier specialist, prompt and ACP session, barred by its role from editing/rewriting the requirements; they may still share provider vendor and workspace access.
- Who acts on findings: ROUTA re-delegates if deficiencies are reported; review-lane convergence uses `NOT_APPROVED`→Dev, `BLOCKED`→Blocked and `APPROVED`→Done.
- Evidence: [GATE verifier and evidence contract](https://github.com/phodal/routa/blob/9dc7b7be8fa92b760f6ebf0ac7f8b44db1b4dc34/resources/specialists/core/gate.yaml#L1-L94), [coordinator GATE delegation](https://github.com/phodal/routa/blob/9dc7b7be8fa92b760f6ebf0ac7f8b44db1b4dc34/resources/specialists/core/routa.yaml#L21-L54), [verdict routing](https://github.com/phodal/routa/blob/9dc7b7be8fa92b760f6ebf0ac7f8b44db1b4dc34/src/core/kanban/review-lane-convergence.ts#L24-L59).
- Basis: A second operational actor has a different evidence route, own judgment and a return path to controlling subsequent work.
- Confidence: Medium-high on wiring, not on accuracy of model review.
- Caveats: Shared model/provider and same operator are potential correlated-failure channels; no LLM efficacy or blind-review experiments performed.

## S4 — Outside-and-then intelligence

- State: —
- Function: No material first-party, closed prospective external-environment sensing and future capability-adaptation loop demonstrated at this local delivery-organization recursion.
- Disturbance / variety regulated: New programming practices, provider capabilities, framework changes or future market requirements could challenge Routa, but responding within today's task is not itself prospective strategy.
- Decisive decision or feedback right: None shown for future *organizational capability* adaptation; the agent coordinator reprioritizes current task waves, while operators/maintainers choose new products, providers or policy/configuration.
- Decision owner: No S4-specific first-party autonomous or parent-mode actor evidenced at the assessed recursion.
- Supporting / enforcement mechanisms: Trace history, run-outcome persistence, learned playbooks, context preload, configurable specialists, repo fitness checks, adapter selection and future-looking docs.
- Closure path: Retrospective playbook hints may improve a later similar task, but the reviewed shipped paths do not close outside-and-then scanning → prospective option selection → adopted organizational capability change.
- Why this is / is not agent-owned: Local reuse and incident recovery are present-work learning; future externally oriented system adaptation remains unestablished.
- Evidence: [trace/run memory in coordinator pipeline](https://github.com/phodal/routa/blob/9dc7b7be8fa92b760f6ebf0ac7f8b44db1b4dc34/src/core/orchestration/orchestrator.ts#L560-L603), [run-outcome and playbook sync](https://github.com/phodal/routa/blob/9dc7b7be8fa92b760f6ebf0ac7f8b44db1b4dc34/src/core/orchestration/orchestrator.ts#L1249-L1285), [architecture](https://github.com/phodal/routa/blob/9dc7b7be8fa92b760f6ebf0ac7f8b44db1b4dc34/docs/ARCHITECTURE.md#L98-L151).
- Basis: Bounded absence of future/external intelligence closure in standard operational mode.
- Confidence: Medium.
- Caveats: Specialized outside-facing workflows could be configured by users but are not credited absent a shipped mode and ownership path.

### Absence scope

- Surfaces inspected: Bundled coordinator and lane prompts, trace-learning/run outcomes, source-scanning/context preload, review/fitness hooks, workflows and operator configuration.
- Plausible first-party paths checked: Learned playbook reused from earlier runs; prospective task decomposition; provider selection; fitness issue signals and human backlog/roadmap.
- Why no material first-party path remains: None inspected autonomously or via a closed parent mode turns outside/future distinctions into a committed capability adaptation that returns to regulate the delivery organization; available paths refine current work or require a separate operator design decision.

## S5 — Policy and identity

- State: —
- Function: No first-party route is shown for deciding ultimate organization identity or policy conflicts and returning such decisions into the delivery organization's ongoing behavior.
- Disturbance / variety regulated: Mandate, security and permission disputes might threaten autonomy, but per-tool permissions and plan approval are narrower than an ultimate-policy dispute.
- Decisive decision or feedback right: Not established for identity-level governance at the selected workspace organization; users approve an initial plan, coordinators resolve ordinary tool permission requests, and config/operators set provider/sandbox rules.
- Decision owner: Operator for startup approval and ordinary restrictions; ROUTA for delegated tool permissions; neither mechanism is an evidenced S5 agent or parent policy closure.
- Supporting / enforcement mechanisms: Initial plan approval, coordinator permission request/response, sandbox constraint mutation, agent-role instructions and local runtime policy.
- Closure path: Permission response can authorize or deny one execution, but there is no identity/ultimate-policy escalation, authoritative resolution and standing return-to-operation path for S5 at this recursion.
- Why this is / is not agent-owned: Supervising execution permissions is not equivalent to governing the organization's identity or highest-order constraints.
- Evidence: [approval before delegation](https://github.com/phodal/routa/blob/9dc7b7be8fa92b760f6ebf0ac7f8b44db1b4dc34/resources/specialists/core/routa.yaml#L10-L40), [permission request and coordinator response](https://github.com/phodal/routa/blob/9dc7b7be8fa92b760f6ebf0ac7f8b44db1b4dc34/src/core/tools/agent-tools.ts#L1419-L1542).
- Basis: Bounded absence of S5-specific agent or parent governance closure.
- Confidence: Medium-high.
- Caveats: A company operating Routa might establish its own legitimate S5 externally; it is not supplied by this local first-party harness mode.

### Absence scope

- Surfaces inspected: Coordinator role contract and human approval, agent permissions, sandbox rules, workspace-level settings, developer governance and runtime orchestration.
- Plausible first-party paths checked: Required plan acceptance, coordinator `respondToPermission`, task-level block/escalation, sandbox constraint mutation and contributor release decisions.
- Why no material first-party path remains: These settle task execution or operate at the OSS-project boundary, not a workspace-organizational ultimate-policy issue through a legitimate governing authority with continuing binding return.

## Distributed OSS parent arrangement

GitHub maintainers and external provider operators are distinct from each local Routa workspace. Contributor code review, releases and repository conventions are not transplanted into S3/S4/S5 ownership of a user's active multi-agent delivery organization. The documented human approval of an initial plan is a **bounded mandate condition**, not independent evidence of a full operational parent S3/S5 mode.

## Self-hosted and non-human modes

Local web or desktop use may run the coordination organization with a configured model provider and without a centralized SaaS parent. The model-backed ROUTA/CRAFTER/GATE specialist loop is the credited composed mode; an isolated session, all-human Kanban or empty provider configuration does not inherit those autonomy states. Deterministic concurrency quotas and sandbox policy are enforcement, not model-owned discretion.

## Recursion

Individual implementor tasks are bounded S1 units. The selected higher recursion is one workspace's cooperating S1 units, ROUTA coordinator and GATE complementary audit. A provider vendor, other Routa workspaces and the OSS developer organization sit outside this assessment. The presence of user-created nested agents does not establish recursively complete VSMs in every child.

## Variety and escalation

Code/test uncertainty goes to an S1 agent; cross-agent file overlap is exposed via S2 preflight and messaging; whole-current dependency/assignment decisions go to ROUTA; GATE's separate failure verdict returns to ROUTA or the board; ordinary plan and permission matters escalate to the user/coordinator. No evidenced S4 future-environment or S5 identity/policy governance closure is inferred from these routes.

## Evidence gaps

- Source and bundled role prompts establish standard wiring and possible agent decisions, not actual external model compliance or reliability.
- No live LLM/ACP/provider run or agent-based benchmark was performed, per batch test policy. Reviewed deterministic test source includes orchestrator and Kanban queue mocked/unit test suites, without claiming they were executed.
- Review independence is role/session separation, not proof of unrelated models, blinded testing or independent institutional authority.
- S2 file-conflict prevention is prompt-guided and subject to agent compliance. Structural anti-contention capacity checks are deterministic supporting behavior.

---
harness_id: inferpal
project_name: Inferpal
repository: https://github.com/EstaxNet/Inferpal
review_ref: c9888bd709cb1516f8dbb3164883e15e2fd2a650
reviewed_at: 2026-11-20
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: C
autonomy_s4: C(P)
autonomy_s5: —
---

# Inferpal

## Review boundary

- System in focus: One Inferpal editor workspace and its own native Core runtime and task queue.
- Purpose and identity: Operate a local coding agent and let the user inspect, authorize and redirect its project work.
- Relevant environment: Editor operator, project checkout, local or user-controlled model server, Git, editor and debugger integrations.
- Standard-distribution boundary: Inferpal.Core, the shipped Visual Studio and VS Code adapters, and Inferpal.Host in ACP modes according to supported front-end capabilities.
- Credited operating / distribution surfaces: [Packaged runtime topology](https://github.com/EstaxNet/Inferpal/blob/c9888bd709cb1516f8dbb3164883e15e2fd2a650/docs/architecture.md) · [Editor-independent agent policy](https://github.com/EstaxNet/Inferpal/blob/c9888bd709cb1516f8dbb3164883e15e2fd2a650/Inferpal.Core/Services/Agent/AgentLoopPolicy.cs) · [Host action path](https://github.com/EstaxNet/Inferpal/blob/c9888bd709cb1516f8dbb3164883e15e2fd2a650/Inferpal.Host/HostServer.cs) · [Supported commands](https://github.com/EstaxNet/Inferpal/blob/c9888bd709cb1516f8dbb3164883e15e2fd2a650/docs/slash-commands.md)
- Adjacent first-party surfaces excluded from ownership: Contributor CI, benchmarks, external ACP client decision logic, model service internals and externally supplied MCP tools.
- First-party operating / deployment modes considered: Visual Studio and VS Code foreground and background native agent modes, plus first-party Host/ACP access where features are supported.
- Recursion level: One editor workspace with foreground coding and separately executing background tasks.
- Reviewed revision: c9888bd709cb1516f8dbb3164883e15e2fd2a650
- Observation date: 2026-11-20
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

An editor-neutral .NET Core runs model-backed chats, agent loops, tools, approval policy and persistence. Visual Studio uses its own editor adapter, and VS Code or ACP call the shared Host. Background tasks have independent objectives, a separate lifecycle and restricted tooling. The editor supplies actual diffs, Git state and debugging signals. The model server is selected by the operator and can run on local or owner-controlled hardware.

## Operational model

Foreground agent runs choose project tools and react to results. A background model session independently explores a submitted objective or prepares changes for review. The operator can modify current work and control what changes reach the checkout. Tool approvals constrain individual actions.

## S1 — Operations

- State: A
- Function: Carry out a coding or investigation goal with workspace actions and feedback.
- Disturbance / variety regulated: Project conditions, edits, build results and test errors can require different actions.
- Decisive decision or feedback right: Choose tools and adjustments within the agent turn, then deliver the result.
- Decision owner: Configured native agent model.
- Supporting / enforcement mechanisms: Shared Core, IDE/Host adapters, tool registry, permissions, debugger and persisted session state.
- Closure path: Results from file, command, editor and test tools become the next model context, leading to continued action or completion.
- Why this is / is not agent-owned: With the model removed, the tools and approval gates do not choose a workspace trajectory.
- Boundary reachability: The supported adapters reach the same first-party Core, which runs the model and tools in foreground agent mode.
- Evidence: [Packaged mode architecture](https://github.com/EstaxNet/Inferpal/blob/c9888bd709cb1516f8dbb3164883e15e2fd2a650/docs/architecture.md) · [Host operations](https://github.com/EstaxNet/Inferpal/blob/c9888bd709cb1516f8dbb3164883e15e2fd2a650/Inferpal.Host/HostServer.cs) · [Loop rules](https://github.com/EstaxNet/Inferpal/blob/c9888bd709cb1516f8dbb3164883e15e2fd2a650/Inferpal.Core/Services/Agent/AgentLoopPolicy.cs) · [Runtime tools](https://github.com/EstaxNet/Inferpal/blob/c9888bd709cb1516f8dbb3164883e15e2fd2a650/Inferpal.Core/Services/Execution/ToolRegistry.cs)
- Basis: structural
- Confidence: high
- Caveats: Normal local permissions and the task's approved authority continue to apply.

## S2 — Coordination

- State: C
- Function: Reduce interference over the shared inference slot between foreground coding and detached agent tasks.
- Disturbance / variety regulated: A background model task starting during an active foreground turn can compete for the same GPU, including when an approval card is pending.
- Decisive decision or feedback right: Sequence the background task after the foreground turn and hold the task lease once admitted.
- Decision owner: First-party scheduler applies fixed turn-priority and queue rules. No coordinating model can revise those rules.
- Supporting / enforcement mechanisms: Independent background queue, turn-idle gate, inference leases and workspace admission checks.
- Closure path: Foreground completion releases the idle gate and allows a named background objective to start. Outcomes are surfaced to the operator.
- Why this is / is not agent-owned: The background agent chooses how to solve its task. The coordination decision is provided as a deterministic shared-resource construction.
- Boundary reachability: The packaged background-task command submits separate model runs to the shared queue and turn-idle gate.
- Distinct S1 units: The foreground coding run and detached investigation each have a substantive objective and choose their own evidence/tool steps.
- Inter-S1 disturbance: Overlapping inference demand would put both operations on the same model server and GPU while the foreground may still resume from an approval.
- Attenuating coordination relation: One background task runs at a time and the next waits for foreground turns to end before it is admitted.
- Feedback into subsequent S1 behaviour: Ending an active foreground turn admits the queued background task, so it starts its model-driven operation after that state change.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The turn-idle dependency specifically addresses overlap over the shared inference resource and changes when the independent background operation can start.
- Evidence: [Queue, priority and documented contention](https://github.com/EstaxNet/Inferpal/blob/c9888bd709cb1516f8dbb3164883e15e2fd2a650/Inferpal.Core/Services/Tasks/BackgroundTaskQueue.cs) · [Inference scheduler](https://github.com/EstaxNet/Inferpal/blob/c9888bd709cb1516f8dbb3164883e15e2fd2a650/Inferpal.Core/Services/Hardware/GpuScheduler.cs) · [User-accessible detached task mode](https://github.com/EstaxNet/Inferpal/blob/c9888bd709cb1516f8dbb3164883e15e2fd2a650/docs/slash-commands.md#L140-L149)
- Basis: structural
- Confidence: medium
- Caveats: A new foreground turn may contend after a background task has started because that task cannot be preempted; the relation attenuates start-time contention.

## S3 — Inside-and-now control

- State: P
- Function: Selectively end or retry active and queued commitments in the current workspace.
- Disturbance / variety regulated: Submitted foreground or detached work can become unneeded or compete with other desired inferencing work.
- Decisive decision or feedback right: The user selects which named queued or running objective to stop or retry from the current task state.
- Decision owner: Legitimate operator of the editor workspace.
- Supporting / enforcement mechanisms: Current foreground activity, task list with state and identifiers, cancellation and requeue handlers.
- Closure path: Cancelling drops a pending task or signals the active run to stop. A retry submits a new commitment, affecting later scheduling.
- Why this is / is not agent-owned: Fixed queue order enforces the working arrangement. The operator chooses which commitments continue, end, or restart.
- Boundary reachability: The shipped foreground editor and background-task commands expose the current chat state and workspace task list, with stop and retry for identified tasks.
- Whole-system current view: Within the declared editor workspace, the active foreground turn and the background queue and running states are accessible to the same operator.
- Current-control decision scope: The operator can stop a selected queued or running background objective and can choose to resubmit a completed objective as new work.
- Evidence: [Workspace task controls](https://github.com/EstaxNet/Inferpal/blob/c9888bd709cb1516f8dbb3164883e15e2fd2a650/docs/slash-commands.md#L140-L149) · [Queue state and current job](https://github.com/EstaxNet/Inferpal/blob/c9888bd709cb1516f8dbb3164883e15e2fd2a650/Inferpal.Core/Services/Tasks/BackgroundTaskQueue.cs) · [Foreground and host execution](https://github.com/EstaxNet/Inferpal/blob/c9888bd709cb1516f8dbb3164883e15e2fd2a650/Inferpal.Host/HostServer.cs)
- Basis: structural
- Confidence: medium
- Caveats: The scope is one editor workspace and its own queue. No multi-editor fleet controller or model-owned reallocation is claimed.

## S3* — Complementary audit

- State: C
- Function: Review actual Git changes through a separate model pass and make the result available for corrective work.
- Disturbance / variety regulated: A coding agent's transcript or tests can miss a regression present in the real diff.
- Decisive decision or feedback right: Select the audit scope and interpret the independent findings, with the separate review model owning its generated defect assessment.
- Decision owner: User triggers and acts on review. A fresh reviewer inference produces the finding.
- Supporting / enforcement mechanisms: Direct Git and untracked-file reads, review criteria, a fresh review prompt and location checks against observed hunks.
- Closure path: The editor displays anchored review findings for the operator to turn into correction or acceptance. No automatic corrective rerun is required by the command.
- Why this is / is not agent-owned: The model judges artifacts independently of the production conversation on the audit pass. The host constructs evidence collection and return for operator follow-through.
- Boundary reachability: The standard Visual Studio, VS Code and ACP command surfaces expose /check and route it to the shared handler.
- Claim being audited: Whether actual working-tree or revision changes introduce a defect or violate the applicable configured checks.
- Ordinary reporting path: The producing agent reports changes in its conversation, with its ordinary tool and test feedback.
- Complementary access path: The review handler reads Git state independently, builds a new review-only history from the selected raw changes and checks reported locations against those hunks.
- Independence boundary: The reviewer gets a fresh input context without the producing transcript, even if the configured model implementation is the same.
- Who acts on findings: The editor operator receives severity and line-anchored findings and chooses whether to request correction in the coding session.
- Evidence: [Direct observations and fresh review request](https://github.com/EstaxNet/Inferpal/blob/c9888bd709cb1516f8dbb3164883e15e2fd2a650/Inferpal.Core/Services/Commands/CheckCommandHandler.cs) · [Result presentation](https://github.com/EstaxNet/Inferpal/blob/c9888bd709cb1516f8dbb3164883e15e2fd2a650/Inferpal/ToolWindow/InferpalToolWindowData.PromptHistory.cs#L482-L504) · [Supported review targets](https://github.com/EstaxNet/Inferpal/blob/c9888bd709cb1516f8dbb3164883e15e2fd2a650/docs/rules-and-checks.md)
- Basis: structural
- Confidence: medium
- Caveats: The audit is user-triggered and lacks a mandatory finding-to-fix gate. Bounding, file exclusions and truncated output affect coverage.

## S4 — Outside-and-then intelligence

- State: C(P)
- Function: Adapt the default model capability to the model server's externally observed inventory for future sessions.
- Disturbance / variety regulated: A new installation can lack the standard default model, and the server can make a different model available.
- Decisive decision or feedback right: Select a replacement from the server listing or let the operator choose explicitly.
- Decision owner: Base: deterministic first-model adoption in the unchosen-default case. Parent: operator when selecting the persisted model capability.
- Supporting / enforcement mechanisms: Live model listing, chat-capability filtering, default adoption guard, saved configuration and later model use.
- Closure path: The selected replacement is persisted or bound to future session turns, and the UI shows the result.
- Why this is / is not agent-owned: The built-in path uses a predeclared adoption rule without model discretion. The independently supported operator path gives the human the prospective choice.
- Boundary reachability: The shipped Host and VS Code startup use models/adoptDefault, and the editor exposes live model listing and explicit selection modes.
- External distinction: The model server advertises the models actually installed and their role compatibility outside the editor harness.
- Future / prospective distinction: Choosing an operating default changes the capability available to later questions and work.
- Adaptation option generated: Filter the live inventory to suitable chat models and choose a replacement when the untouched default is absent, or present the available candidates for user selection.
- Path back into current capability / S3: The adopted model is saved into configuration or selected for the workspace session, which uses it for subsequent model calls.
- Evidence: [Selection policy](https://github.com/EstaxNet/Inferpal/blob/c9888bd709cb1516f8dbb3164883e15e2fd2a650/Inferpal.Core/Services/Inference/ModelCatalog.cs) · [External list and adoption](https://github.com/EstaxNet/Inferpal/blob/c9888bd709cb1516f8dbb3164883e15e2fd2a650/Inferpal.Host/HostServer.cs#L1400-L1481) · [Editor reads the new default](https://github.com/EstaxNet/Inferpal/blob/c9888bd709cb1516f8dbb3164883e15e2fd2a650/vscode/src/chatViewProvider.ts#L1136-L1151)
- Basis: structural
- Confidence: medium
- Caveats: The constructor claim covers the untouched-default migration. It does not imply discretionary autonomous model replacement after an explicit choice.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | Fixed first-run adoption rule | The provider does not list the factory default and the operator has never selected a model | Adopt a suitable installed candidate and save the new operating default. | [Host default adoption](https://github.com/EstaxNet/Inferpal/blob/c9888bd709cb1516f8dbb3164883e15e2fd2a650/Inferpal.Host/HostServer.cs#L1464-L1481) |
| Parent (`P`) | Editor operator | The operator inspects live model choices and selects a different supported model | The explicit choice is persisted or bound to later session requests and protected from default adoption. | [Model choice and application](https://github.com/EstaxNet/Inferpal/blob/c9888bd709cb1516f8dbb3164883e15e2fd2a650/vscode/src/chatViewProvider.ts) · [Current model binding](https://github.com/EstaxNet/Inferpal/blob/c9888bd709cb1516f8dbb3164883e15e2fd2a650/Inferpal.Host/HostServer.cs) |

## S5 — Policy and identity

- State: —
- Function: Resolve a workspace-level ultimate-policy or identity issue and return the authoritative choice to operations.
- Disturbance / variety regulated: Project guidance, permissions and rules change coding behavior and permissible actions.
- Decisive decision or feedback right: No distinct identity-level decision and return path was established.
- Decision owner: The editor or repository owner controls ordinary guidance, scopes and approvals.
- Supporting / enforcement mechanisms: Repository instructions, project rules and checks, permission configuration, and onboarding context.
- Closure path: Rules and context are loaded into future turns. Scoped approvals govern particular actions.
- Why this is / is not agent-owned: Onboarding drafts project facts. Editable operational rules and scopes do not demonstrate installed resolution of an ultimate-policy matter.
- Evidence: [Rules and their scope](https://github.com/EstaxNet/Inferpal/blob/c9888bd709cb1516f8dbb3164883e15e2fd2a650/docs/rules-and-checks.md) · [Generated onboarding context](https://github.com/EstaxNet/Inferpal/blob/c9888bd709cb1516f8dbb3164883e15e2fd2a650/Inferpal.Core/Services/Commands/OnboardCommandHandler.cs) · [Permission policy](https://github.com/EstaxNet/Inferpal/blob/c9888bd709cb1516f8dbb3164883e15e2fd2a650/Inferpal.Core/Services/Execution/PermissionPolicy.cs)
- Basis: structural
- Confidence: medium
- Caveats: Repository authors own their external project policy. This assessment examines the configured editor harness.

### Absence scope

- Surfaces inspected: Rules, repository instructions, onboarding, review criteria, approvals and model management.
- Plausible first-party paths checked: Standing governance authority beyond per-task operation, ultimate policy conflicts and returned workspace identity decisions.
- Why no material first-party path remains: Available paths inject instructions or enforce scoped choices. They do not expose an installed ultimate-policy issue, decisive authority and operative return.

## Recursion

The workspace holds foreground and detached operational modes. Background tasks are independent model runs, but the queue does not create another whole metasystem recursion.

## Variety and escalation

Tool and debugger evidence varies the coding course. Foreground state gates background startup, queue status informs operator cancellation, and direct Git evidence is used in a separate review context.

## Evidence gaps

No IDE, provider, debugger or other live inference run was performed. The review covers first-party pinned source and documents the supported scopes of the optional operating modes.

---
harness_id: zhifox
project_name: ZhiFox
repository: https://github.com/Akxan/zhifox-agent-harness
review_ref: 0111a8477e4e199b9579d3e0c65b4505fb2eebe9
reviewed_at: 2026-11-27
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: P
autonomy_s5: —
---

# ZhiFox

## Review boundary

- System in focus: The shipped ZhiFox assistant, local task scheduler, chat routes and installed skill adoption.
- Purpose and identity: Execute locally scoped assistant work for a user and return outputs through interactive or unattended channels.
- Relevant environment: Workspace files, operator, chat platforms, model endpoints and external skill sources.
- Standard-distribution boundary: Shipped Python agent package, first-party chat/runtime routes, scheduler, skill store and supported adapters.
- Credited operating / distribution surfaces: CLI, web, paired chat and unattended task entry, supplied subagent runner, scheduled controls and skill adoption.
- Adjacent first-party surfaces excluded from ownership: Development instructions, maintainer release process, offline evals and external model/software services supplied no runtime decision owner.
- First-party operating / deployment modes considered: Interactive service, independently dispatched scheduled tasks, optional installed subagents and web-based operator oversight.
- Recursion level: One ZhiFox deployment. The scheduled portfolio and skill adoption are supported operating configurations.
- Reviewed revision: [0111a8477e4e199b9579d3e0c65b4505fb2eebe9](https://github.com/Akxan/zhifox-agent-harness/tree/0111a8477e4e199b9579d3e0c65b4505fb2eebe9)
- Observation date: 2026-11-27
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

Model turns consume available tools and returned observations. First-party runners bind independent contexts to conversations and scheduled tasks. The scheduler publishes current task commitments. External skill candidates are staged and selected by the operator before the catalogue is refreshed to later turns. [agent loop](https://github.com/Akxan/zhifox-agent-harness/blob/0111a8477e4e199b9579d3e0c65b4505fb2eebe9/harness/agent.py#L238-L271), [scheduled Work](https://github.com/Akxan/zhifox-agent-harness/blob/0111a8477e4e199b9579d3e0c65b4505fb2eebe9/harness/webui/scheduler_work.py#L38-L132), [external discovery and staging](https://github.com/Akxan/zhifox-agent-harness/blob/0111a8477e4e199b9579d3e0c65b4505fb2eebe9/harness/webui/skills_api.py#L120-L156), [future turn refresh](https://github.com/Akxan/zhifox-agent-harness/blob/0111a8477e4e199b9579d3e0c65b4505fb2eebe9/harness/skills/catalog.py#L36-L49).

## Operational model

Interactive and task-local agent runs own tool choices. The human chooses grants and can change current scheduled commitments or adopt reusable capability. Chat adapters and provider runtimes carry effects or supply model inference.

## S1 — Operations

- State: A
- Function: Deliver user-directed assistant tasks.
- Disturbance / variety regulated: Changing file, tool and provider state during the task.
- Decisive decision or feedback right: Select a scoped next tool or return an answer after observations.
- Decision owner: The model-backed ZhiFox Agent.
- Supporting / enforcement mechanisms: Provider adapter, permission/sandbox rules and result transport.
- Closure path: Invoke a model with tools, execute selected actions and append returned observations before the next decision.
- Boundary reachability: The generic installed loop is wired by the supported chat and unattended runners. Unattended tasks have supplied access modes.
- Why this is / is not agent-owned: Deterministic gates enforce operating scope. The model makes work decisions within that scope.
- Evidence: [agent loop](https://github.com/Akxan/zhifox-agent-harness/blob/0111a8477e4e199b9579d3e0c65b4505fb2eebe9/harness/agent.py#L238-L271), [tool result return](https://github.com/Akxan/zhifox-agent-harness/blob/0111a8477e4e199b9579d3e0c65b4505fb2eebe9/harness/agent.py#L333-L398), [scheduled Work](https://github.com/Akxan/zhifox-agent-harness/blob/0111a8477e4e199b9579d3e0c65b4505fb2eebe9/harness/webui/scheduler_work.py#L38-L132), [unattended permission configuration](https://github.com/Akxan/zhifox-agent-harness/blob/0111a8477e4e199b9579d3e0c65b4505fb2eebe9/harness/app_runs.py#L49-L101), [permission modes](https://github.com/Akxan/zhifox-agent-harness/blob/0111a8477e4e199b9579d3e0c65b4505fb2eebe9/README.md#L121-L143)
- Basis: Pinned runtime flow.
- Confidence: High.
- Caveats: No third-party model call was made.

## S2 — Coordination

- State: C
- Function: Coordinate independently requested scheduled work and a shared mutable conversation across chat entry points.
- Disturbance / variety regulated: Concurrent arrivals can overrun the scheduled worker pool or overwrite a conversation edited by another active client.
- Decisive decision or feedback right: Choose a safe admission and retry/refresh relationship at the configuration level.
- Decision owner: First-party constructor supplies fixed slot and conversation-claim rules.
- Supporting / enforcement mechanisms: Mutex-protected slot assignment, per-conversation claim and reloading persisted state after acquisition.
- Closure path: The conflicting caller waits or gets a retry signal. The claimant consumes current persisted state and the scheduler opens a slot on completion.
- Boundary reachability: Both paired chat and web claim the same conversation identifier. Independent scheduled runs share their scheduler admission policy.
- Why this is / is not agent-owned: The fixed, boundary-specific protocol is supplied. Its coordination choice is not independently agent-owned.
- Evidence: [claim implementation](https://github.com/Akxan/zhifox-agent-harness/blob/0111a8477e4e199b9579d3e0c65b4505fb2eebe9/harness/claims.py#L20-L50), [web claim](https://github.com/Akxan/zhifox-agent-harness/blob/0111a8477e4e199b9579d3e0c65b4505fb2eebe9/harness/webui/webapp.py#L249-L268), [channel claim](https://github.com/Akxan/zhifox-agent-harness/blob/0111a8477e4e199b9579d3e0c65b4505fb2eebe9/harness/channels/session_conversation.py#L45-L66), [enqueue control](https://github.com/Akxan/zhifox-agent-harness/blob/0111a8477e4e199b9579d3e0c65b4505fb2eebe9/harness/webui/scheduler_loop.py#L75-L115), [scheduled Work](https://github.com/Akxan/zhifox-agent-harness/blob/0111a8477e4e199b9579d3e0c65b4505fb2eebe9/harness/webui/scheduler_work.py#L38-L132)
- Basis: Pinned cross-entry protocol and return.
- Confidence: High.
- Caveats: Separate UI views alone were not counted.
- Distinct S1 units: Independently resumed web and paired-channel agent sessions, plus distinct scheduled tasks as a second witness.
- Inter-S1 disturbance: Two turns can try to update one saved conversation, and simultaneous due tasks can contend for capped execution capacity.
- Attenuating coordination relation: One writer owns a conversation claim at a time, and the scheduler allocates bounded run slots.
- Feedback into subsequent S1 behaviour: Released claims allow the other turn to reread the newest state. Releasing a run slot triggers dispatch of queued work.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: A real collision changes admission and subsequently changes the permitted execution from the latest accepted state.

## S3 — Inside-and-now control

- State: P
- Function: Oversee and alter the current scheduled work portfolio.
- Disturbance / variety regulated: A running or pending commitment may need to be cancelled, disabled or manually started depending on its status and operator priority.
- Decisive decision or feedback right: Select a current intervention across the scheduled portfolio.
- Decision owner: The installed human operator.
- Supporting / enforcement mechanisms: Task snapshot, progress and approval surfaces, stop signal and store updates.
- Closure path: Inspect all scheduled work, stop a selected run or queue a different task, then observe updated state and subsequent dispatch.
- Boundary reachability: The Web UI schedule API and scheduler control the same task/run objects and re-publish results.
- Why this is / is not agent-owned: Model task tools provide add/delete requests and compact histories. The distinct live portfolio view and stop/dispatch choice are operator-owned.
- Evidence: [portfolio state](https://github.com/Akxan/zhifox-agent-harness/blob/0111a8477e4e199b9579d3e0c65b4505fb2eebe9/harness/webui/scheduler.py#L192-L214), [operator actions](https://github.com/Akxan/zhifox-agent-harness/blob/0111a8477e4e199b9579d3e0c65b4505fb2eebe9/harness/webui/scheduler_actions.py#L27-L84), [scheduled Work](https://github.com/Akxan/zhifox-agent-harness/blob/0111a8477e4e199b9579d3e0c65b4505fb2eebe9/harness/webui/scheduler_work.py#L38-L132), [ordinary task tools](https://github.com/Akxan/zhifox-agent-harness/blob/0111a8477e4e199b9579d3e0c65b4505fb2eebe9/harness/tools/tasks.py#L57-L102)
- Basis: Pinned sensing, intervention and return.
- Confidence: High for the scheduled scope.
- Caveats: No positive whole-deployment control over independent interactive agents was inferred.
- Whole-system current view: Scheduled task inventory with queue/running state, progress, limits and recent terminal receipts for the supported scheduler mode.
- Current-control decision scope: Stop queued or running commitments, choose a task for immediate execution, and change enabled state that gates later admission.

## S3* — Complementary audit

- State: —
- Function: No supplied complementary audit that changes current control was established.
- Disturbance / variety regulated: A run or delegated agent can make an unsupported completion claim.
- Decisive decision or feedback right: No distinct audit decision and closed consequent control response supplied.
- Decision owner: No qualifying audit owner established.
- Supporting / enforcement mechanisms: Task logs, permission previews, optional read-only reviewer template and backup checks.
- Closure path: Optional reviewer returns an ordinary delegated answer. The runtime does not connect it to a current-control audit trigger or decision.
- Why this is / is not agent-owned: Read-only review of requested code is supplied as an optional subagent. Its generic delegation edge does not establish a complementary operational audit relationship.
- Evidence: [optional reviewer example](https://github.com/Akxan/zhifox-agent-harness/blob/0111a8477e4e199b9579d3e0c65b4505fb2eebe9/harness/agents/examples.py#L51-L81), [delegation path](https://github.com/Akxan/zhifox-agent-harness/blob/0111a8477e4e199b9579d3e0c65b4505fb2eebe9/harness/agents/runner.py#L191-L259), [portfolio state](https://github.com/Akxan/zhifox-agent-harness/blob/0111a8477e4e199b9579d3e0c65b4505fb2eebe9/harness/webui/scheduler.py#L192-L214), [approval preview](https://github.com/Akxan/zhifox-agent-harness/blob/0111a8477e4e199b9579d3e0c65b4505fb2eebe9/harness/permissions_review.py#L35-L65)
- Basis: Bounded search over example, runtime and scheduler paths.
- Confidence: Moderate.
- Caveats: The example makes a tailored user-composed review possible.

### Absence scope

- Surfaces inspected: Optional reviewer template, runner and result return, task UI/history, permission review and restore validation.
- Plausible first-party paths checked: Independent examination of a producing agent's claims, exception-triggered inspection, return of discrepancies to current task control.
- Why no material first-party path remains: The example examines code when invoked as a task. No first-party loop conditions a current-control decision or commitment on a separate audit of operational claims.

## S4 — Outside-and-then intelligence

- State: P
- Function: Bring externally available reusable skills into future ZhiFox operating capability.
- Disturbance / variety regulated: New procedures exist in other agent installations and remote repositories, and may differ from the present local repertoire.
- Decisive decision or feedback right: Select which candidate to install, replace or decline for later use.
- Decision owner: The installed human operator.
- Supporting / enforcement mechanisms: External discovery/fetch, standardized candidate preview, selected install and refreshed catalog.
- Closure path: Materialize selected external candidates and provide the updated repertoire to the agent before following turns.
- Boundary reachability: The installed skill UI stages actual discovered or fetched candidates and the same store supplies later turn notifications.
- Why this is / is not agent-owned: Source selection and adoption are human decisions. The runtime reconstructs choices, checks them and reflects selected options into current operation.
- Evidence: [external discovery and staging](https://github.com/Akxan/zhifox-agent-harness/blob/0111a8477e4e199b9579d3e0c65b4505fb2eebe9/harness/webui/skills_api.py#L120-L156), [decision preview](https://github.com/Akxan/zhifox-agent-harness/blob/0111a8477e4e199b9579d3e0c65b4505fb2eebe9/harness/skills/bundle.py#L172-L190), [selected adoption](https://github.com/Akxan/zhifox-agent-harness/blob/0111a8477e4e199b9579d3e0c65b4505fb2eebe9/harness/skills/installer.py#L56-L103), [future turn refresh](https://github.com/Akxan/zhifox-agent-harness/blob/0111a8477e4e199b9579d3e0c65b4505fb2eebe9/harness/skills/catalog.py#L36-L49)
- Basis: First-party external skill discovery, compatibility/collision preview, adoption and future reuse.
- Confidence: Moderate.
- Caveats: This is a bounded skill-repertoire adaptation path. No autonomous skill search or adoption is inferred.
- External distinction: Discovered procedures in another installed tool or a user-selected remote repository, including their compatibility and collision with installed capabilities.
- Future / prospective distinction: Adopt a reusable procedure for later work, with a choice to keep, replace, rename or decline it.
- Adaptation option generated: The staged preview builds installable candidate options with files, declared compatibility and validation problems.
- Path back into current capability / S3: The chosen candidate enters the installed store under the validated selection. The supported agent catalog refresh makes the new capability available to subsequent work.

## S5 — Policy and identity

- State: —
- Function: No supplied ultimate runtime policy or identity closure found.
- Disturbance / variety regulated: Permission, role and capability settings can conflict with a user's requested action.
- Decisive decision or feedback right: No ultimate policy issue that reaches an authority and returns as a governance resolution.
- Decision owner: The human configures task scope. Maintainers own distribution governance outside this recursion.
- Supporting / enforcement mechanisms: Permission review, per-task settings, sandbox configuration and extension metadata.
- Closure path: Local decisions change tool grants and available capabilities without an identity-level escalation/settlement path.
- Why this is / is not agent-owned: Operator approval and configuration constrain ordinary operations.
- Evidence: [approval preview](https://github.com/Akxan/zhifox-agent-harness/blob/0111a8477e4e199b9579d3e0c65b4505fb2eebe9/harness/permissions_review.py#L35-L65), [unattended permission configuration](https://github.com/Akxan/zhifox-agent-harness/blob/0111a8477e4e199b9579d3e0c65b4505fb2eebe9/harness/app_runs.py#L49-L101), [permission modes](https://github.com/Akxan/zhifox-agent-harness/blob/0111a8477e4e199b9579d3e0c65b4505fb2eebe9/README.md#L121-L143), [operator actions](https://github.com/Akxan/zhifox-agent-harness/blob/0111a8477e4e199b9579d3e0c65b4505fb2eebe9/harness/webui/scheduler_actions.py#L27-L84)
- Basis: Bounded absence across operating and operator surfaces.
- Confidence: Moderate.
- Caveats: This does not address the project's human governance.

### Absence scope

- Surfaces inspected: Interactive and unattended approvals, scheduling authority, extension settings and persona tooling.
- Plausible first-party paths checked: Policy conflict routed to legitimate parent, durable identity decision, return binding subsequent runtime as ultimate policy.
- Why no material first-party path remains: Inspected choices amend task-specific permission or normal operating settings without a supplied ultimate identity/policy decision loop.

## Recursion

Scheduled runs and paired clients have separately scoped tasks and operating contexts. Optional subagent roles run in a fresh child context and report to a caller. Full nested viability was not evaluated.

## Variety and escalation

Tool-level permission and observations, conversation claims, capped dispatch and operator stop paths handle distinct disturbances. Skill adoption operates at a future-capability boundary.

## Evidence gaps

Source-only review at the pinned ref. No remote model, chat platform, desktop/browser actuation or external installation ran during the assessment.

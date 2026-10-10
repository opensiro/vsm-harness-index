---
harness_id: animaworks
project_name: AnimaWorks
repository: https://github.com/xuiltul/animaworks
review_ref: 82f7caa3793f302cfdc74fe460e191d44959a189
reviewed_at: 2026-10-10
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
status: included
autonomy_s1: A
autonomy_s2: ?
autonomy_s3: A
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# AnimaWorks

## Review boundary

- System in focus: one standard self-hosted AnimaWorks organization running real DigitalAnima model-backed agent processes, manager/subordinate organization and actual first-party task/inbox/heartbeat/GitHub event mechanisms; exclude unrelated private SaaS production system and repo-maintainer dogfood.
- Purpose and identity: continuously conduct delegated software/other work through persistent agents with role-based task ownership, status tracking and human escalation.
- Relevant environment: local source repositories, configured model APIs/CLIs, GitHub events/CI, tests/tools, external user instructions, workspace filesystem, team members and permissions.
- Standard-distribution boundary: first-party Python server/core, per-Anima runtime process and model executors (Mode A/SDK/CLI as supported), task queue/TaskBoard, supervisor/subordinate tools, heartbeat/cron, GitHub event gateway; external providers' private cognition and individual off-platform team activity do not become first-party mechanisms.
- Credited operating / distribution surfaces: `core/{agent.py,_agent_cycle.py,_anima_heartbeat.py,anima.py}`, supervisor runner, task dispatch/queue, `core/tooling/handler_delegation.py`, and `server/github_gateway.py`/current config where relevant.
- Adjacent first-party surfaces excluded from ownership: examples/templates and unbound optional playbooks, experimental standalone swe/CI autofix, benchmarks, tests, private product/proprietary usage records, old GitHub review-pass router removed in current schema. Do not credit independent reviewer based solely on README's marketing overview.
- First-party operating / deployment modes considered: installed CLI/server in Mode A (LiteLLM agent/tool loop) and configured SDK/CLI model agent process modes; running hierarchy with an appointed model-driven manager + real subordinates; heartbeat/task runner; GitHub gateway with deduped notifications (not deprecated multi-review router).
- Recursion level: one configured company/manager subtree, not all users' deployments or the OSS maintainer team.
- Reviewed revision: `82f7caa3793f302cfdc74fe460e191d44959a189`.
- Observation date: 2026-10-10.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

AnimaWorks packages individual model-driven `DigitalAnima` processes with first-party `AgentCore.run_cycle`, memory and event-driven task/heartbeat/cron execution. The server persists per-agent task queues, enforces supervisor/subordinate relationships and wires actionable model tool calls such as `delegate_task` and `task_tracker`. When an Anima has real subordinates, its heartbeat prompt gets a subordinate-status check and stale delegated task list, allowing it to choose follow-up/delegation based on organizational current work. `delegate_task` persists a subordinate task and parent tracking item (with optional DM/wakeup), and subsequent agent status feeds back into future management cycles.

Two README claims require **version-sensitive qualification** at the frozen revision. The server's `DelegateTaskPersistRequest.exclusive_key` is explicitly marked retired/ignored: a documented key does not establish enforced per-PR mutual exclusion. Also `GitHubWebhookConfig` notes the old multi-model reviewer/implementer dispatch and review-pass configuration was torn down in September 2026; the gateway currently delivers deduped notifications to one configured dispatcher agent. Neither legacy mechanism may be credited for positive S2 or S3* without an independently demonstrated current first-party alternate.

Sources: [README.md](https://github.com/xuiltul/animaworks/blob/82f7caa3793f302cfdc74fe460e191d44959a189/README.md); [agent.py](https://github.com/xuiltul/animaworks/blob/82f7caa3793f302cfdc74fe460e191d44959a189/core/agent.py); [_agent_cycle.py](https://github.com/xuiltul/animaworks/blob/82f7caa3793f302cfdc74fe460e191d44959a189/core/_agent_cycle.py); [anima.py](https://github.com/xuiltul/animaworks/blob/82f7caa3793f302cfdc74fe460e191d44959a189/core/anima.py); [_anima_heartbeat.py](https://github.com/xuiltul/animaworks/blob/82f7caa3793f302cfdc74fe460e191d44959a189/core/_anima_heartbeat.py); [handler_delegation.py](https://github.com/xuiltul/animaworks/blob/82f7caa3793f302cfdc74fe460e191d44959a189/core/tooling/handler_delegation.py); [task_queue.py](https://github.com/xuiltul/animaworks/blob/82f7caa3793f302cfdc74fe460e191d44959a189/core/memory/task_queue.py); [internal.py](https://github.com/xuiltul/animaworks/blob/82f7caa3793f302cfdc74fe460e191d44959a189/server/routes/internal.py); [schemas.py](https://github.com/xuiltul/animaworks/blob/82f7caa3793f302cfdc74fe460e191d44959a189/core/config/schemas.py); [github_gateway.py](https://github.com/xuiltul/animaworks/blob/82f7caa3793f302cfdc74fe460e191d44959a189/server/github_gateway.py).

## Operational model

Each DigitalAnima is an operational S1 actor using a configured completion model and tools, with one OS process/agent and durable work states. Model-driven managers can observe delegated current-work state and assign new tasks to authorized subordinate Animas. Generic task messages, background process locks, file-sharing conventions and PR notifications are distinguished from a concrete inter-S1 conflict-relief path. Configured independent code reviews may occur as normal model tasks, but an obligatory independent challenge/return loop is not guaranteed by the shipped gateway at this frozen SHA.

## S1 — Operations

- State: A
- Function: produce software/task outputs through persistent model-driven Digital Anima work cells operating against local project files, tools and provider feedback.
- Disturbance / variety regulated: new tasks, repository changes, test results, model/tool failures, conversations and recovery/restart state.
- Decisive decision or feedback right: the configured model decides successive task responses and (in supported tool-capable modes) tool actions based on source/environment feedback.
- Decision owner: model-driven DigitalAnima/AgentCore executor in supported Mode A or hosted CLI/SDK operating modes; external Claude/Codex/Gemini model runtimes are explicit dependencies rather than first-party hidden decision engines.
- Supporting / enforcement mechanisms: first-party `AgentCore.run_cycle`, memory/context handling, model adapter factory, tool handler, per-Anima task/inbox process, heartbeat/cron/task runner and persisted output records.
- Closure path: human, heartbeat, cron, delegated task or notified event activates a worker → first-party run cycle constructs local context and invokes configured model → tool/response feedback is returned to agent → subsequent cycle or tool decision produces changes/outcome → task/inbox/activity state records result.
- Boundary reachability: `DigitalAnima` instantiates first-party `AgentCore` with packaged runtime/executor modes; `core/supervisor/task_runner.py` executes task/heartbeat contracts from shipped process supervisor and CLI.
- Why this is / is not agent-owned: removing the active model leaves only task queues/process supervision/memory storage; no comparable autonomous response or code-operation judgment exists.
- Evidence: [README.md](https://github.com/xuiltul/animaworks/blob/82f7caa3793f302cfdc74fe460e191d44959a189/README.md); [anima.py](https://github.com/xuiltul/animaworks/blob/82f7caa3793f302cfdc74fe460e191d44959a189/core/anima.py); [agent.py](https://github.com/xuiltul/animaworks/blob/82f7caa3793f302cfdc74fe460e191d44959a189/core/agent.py); [_agent_cycle.py](https://github.com/xuiltul/animaworks/blob/82f7caa3793f302cfdc74fe460e191d44959a189/core/_agent_cycle.py); [_agent_executor.py](https://github.com/xuiltul/animaworks/blob/82f7caa3793f302cfdc74fe460e191d44959a189/core/_agent_executor.py); [task_runner.py](https://github.com/xuiltul/animaworks/blob/82f7caa3793f302cfdc74fe460e191d44959a189/core/supervisor/task_runner.py); [pending_executor.py](https://github.com/xuiltul/animaworks/blob/82f7caa3793f302cfdc74fe460e191d44959a189/core/supervisor/pending_executor.py)
- Basis: explicit + structural.
- Confidence: high in configured model-backed mode.
- Caveats: external coding agents' private internal planning and tool loops are not attributed to AnimaWorks. Source review does not verify README's private SaaS production metric claims or the model's practical success.

## S2 — Coordination

- State: ?
- Function: dampen concrete conflicting or oscillating operations between distinct working Animas through a targeted coordination relation.
- Disturbance / variety regulated: two engineers may work on one PR/branch, race edits or duplicate reviews; these are legitimate inter-S1 risks.
- Decisive decision or feedback right: no first-party specific *active* PR exclusive-resource admission or independently controlled collision damping loop was established in the reviewed installed mode.
- Decision owner: agents may negotiate by messages/individual git worktrees and operators may set conventions; the decisive conflict-attenuation owner remains unproven.
- Supporting / enforcement mechanisms: task delegation, task queue, persistent shared board, per-Anima locks and GitHub event deduplication.
- Closure path: messages/updates and per-worker task queues reach workers, but a conflicting two-worker claim → enforced exclusive PR gate → loser changes operation was not reconstructed.
- Boundary reachability: an `exclusive_key` field is accepted by `DelegateTaskPersistRequest` only for backward compatibility and explicitly **ignored** at the frozen revision; the GitHub webhook gate deduplicates notifications, not a demonstrated multi-worker PR write lock.
- Why this is / is not agent-owned: per-Anima process isolation and event deduplication are not automatically a coordination relation regulating an identified pair of independent S1 units.
- Distinct S1 units: two independently active coder Animas, both potentially editing the same repository or PR branch.
- Inter-S1 disturbance: duplicate concurrent PR commits/test/review activity can interfere; documentation names the risk.
- Attenuating coordination relation: README mentions serialized PR-exclusive keys and worktrees, but inspected backend explicitly retires/ignores `exclusive_key`; an alternative authoritative inter-S1 cross-branch lock is not evidenced.
- Feedback into subsequent S1 behaviour: no established enforced rejection/retry notification to a contender for the same PR; GitHub notifications alone do not prove it.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: a positive inter-worker interference witness is missing; do not upgrade basic delegation/mail/one PR event notification by label.
- Evidence: [README.md](https://github.com/xuiltul/animaworks/blob/82f7caa3793f302cfdc74fe460e191d44959a189/README.md); [internal.py](https://github.com/xuiltul/animaworks/blob/82f7caa3793f302cfdc74fe460e191d44959a189/server/routes/internal.py); [github_gateway.py](https://github.com/xuiltul/animaworks/blob/82f7caa3793f302cfdc74fe460e191d44959a189/server/github_gateway.py); [handler_delegation.py](https://github.com/xuiltul/animaworks/blob/82f7caa3793f302cfdc74fe460e191d44959a189/core/tooling/handler_delegation.py); [task_queue.py](https://github.com/xuiltul/animaworks/blob/82f7caa3793f302cfdc74fe460e191d44959a189/core/memory/task_queue.py); [locks.py](https://github.com/xuiltul/animaworks/blob/82f7caa3793f302cfdc74fe460e191d44959a189/core/platform/locks.py); [tasks.py](https://github.com/xuiltul/animaworks/blob/82f7caa3793f302cfdc74fe460e191d44959a189/core/taskboard/tasks.py)
- Basis: explicit contradiction + unresolved.
- Confidence: high that the documented `exclusive_key` gate is retired; medium in broader S2 insufficiency.
- Caveats: `?` is deliberate rather than declaring no S2 anywhere; a separately demonstrated same-branch exclusive gate or operational multi-agent collision recovery could change the assessment.

## S3 — Inside-and-now control

- State: A
- Function: regulate current work assignments, overdue subordinate tasks and next-step interventions across an actual managed local Anima organization.
- Disturbance / variety regulated: unanswered tasks, blocked delegated work, missing status reports and inconsistent current commitments among active subordinate worker Animas.
- Decisive decision or feedback right: a model-driven superior chooses which subordinate should work on what, acceptance criteria and follow-up based on the list of current work and subordinate state.
- Decision owner: a configured supervisor/manager DigitalAnima, not the deterministic process-health SupervisorManager or merely the `supervisor` field in config.
- Supporting / enforcement mechanisms: heartbeats that include subordinate management prompts, stale task scoreboard and synced delegated results; first-party `delegate_task`, `task_tracker` tool handlers, supervisor-only tool provisioning and subordinate DM/wake.
- Closure path: supervisor Anima heartbeat reads current delegated task scoreboard and subordinate list → model assesses overdue or pending commitments → chooses delegate/reallocate/follow-up action → `delegate_task` persists subordinate and tracking queue records, sends acceptance criteria/notification → subordinate runner receives the task and performs subsequent work → delegated status is synced and next supervisor heartbeat reflects result.
- Boundary reachability: configured parent/subordinate structures in standard installed organization permit supervisor `delegate_task`/ `task_tracker` tools; heartbeat `HeartbeatMixin` injects actual subordinate check for Animas with subordinates and the packaged TaskQueue receives work.
- Why this is / is not agent-owned: the model selects the current assignments and follow-up under the live state; deterministic daemon and task board cannot determine priorities or decide whose intervention is appropriate when removed.
- Whole-system current view: the configured manager's descendants, delegated queue and status are visible via heartbeat subordinate summary and task_tracker. Credit is confined to the manager's governed subtree as the declared organization, not an enterprise-wide view of all independent customer orgs.
- Current-control decision scope: delegated work assignment and follow-up, choosing acceptance criteria/target, and reprioritizing blocked or stale subordinate work within that subtree.
- Evidence: [_anima_heartbeat.py](https://github.com/xuiltul/animaworks/blob/82f7caa3793f302cfdc74fe460e191d44959a189/core/_anima_heartbeat.py); [handler_delegation.py](https://github.com/xuiltul/animaworks/blob/82f7caa3793f302cfdc74fe460e191d44959a189/core/tooling/handler_delegation.py); [builder.py](https://github.com/xuiltul/animaworks/blob/82f7caa3793f302cfdc74fe460e191d44959a189/core/tooling/schemas/builder.py); [supervisor.py](https://github.com/xuiltul/animaworks/blob/82f7caa3793f302cfdc74fe460e191d44959a189/core/tooling/schemas/supervisor.py); [task_queue.py](https://github.com/xuiltul/animaworks/blob/82f7caa3793f302cfdc74fe460e191d44959a189/core/memory/task_queue.py); [tasks_dispatch.py](https://github.com/xuiltul/animaworks/blob/82f7caa3793f302cfdc74fe460e191d44959a189/core/tasks_dispatch.py); [anima.py](https://github.com/xuiltul/animaworks/blob/82f7caa3793f302cfdc74fe460e191d44959a189/core/anima.py)
- Basis: explicit + structural.
- Confidence: medium-high in configured manager-with-subordinates mode.
- Caveats: parent/worker topology alone would not establish S3, and the `SupervisorManager` process-restart loop by itself is just deterministic health management.

## S3* — Complementary audit

- State: ?
- Function: independently challenge a worker claim using alternative operational evidence, return review findings and enforce/trigger corrective work.
- Disturbance / variety regulated: implementation or test-success claims inconsistent with actual PR diffs, test outputs or CI results.
- Decisive decision or feedback right: README describes multi-model PR review, but the shipped current GitHub gateway no longer performs its earlier reviewer/implementer routing or creates review-pass tasks; model review can be requested as ordinary agent work, yet an enacted independent audit return loop was not reconstructed.
- Decision owner: unknown; configured independent reviewer could judge real code, but no standard first-party named audit owner plus corrective binding proven.
- Supporting / enforcement mechanisms: GitHub PR event notifications, dedicated review login exclusion, task delegation to other agents, GitHub CLI in model sessions and activity tracking.
- Closure path: webhook gate delivers deduped notifications to a dispatcher Anima; what that model does is configuration-dependent. No first-party automatic independent review-pass collection → synthesis verdict → returned corrective action is evidenced in this frozen gateway.
- Boundary reachability: `GitHubWebhookConfig` explicitly notes 2026-09 teardown of old reviewer/implementer routing and multi-model review-pass fields, while `server/github_gateway.py` just delivers event notifications. No adjacent private SaaS operation is imported as first-party evidence.
- Why this is / is not agent-owned: a review role label, advertised private-production statistic or reviewer bot login does not replace proof of independent code-evidence judgment and consequences.
- Claim being audited: a coder Anima completed code correctly/PR can land.
- Ordinary reporting path: worker transcript, delegated task and PR status.
- Complementary access path: GitHub diffs, tests and review comments potentially read by a separately chartered reviewer agent.
- Independence boundary: no mandatory isolated review ownership and first-party return bound in assessed installed flow.
- Who acts on findings: manager/worker could react but the standardized review verdict and correction path are not proven.
- Evidence: [README.md](https://github.com/xuiltul/animaworks/blob/82f7caa3793f302cfdc74fe460e191d44959a189/README.md); [schemas.py](https://github.com/xuiltul/animaworks/blob/82f7caa3793f302cfdc74fe460e191d44959a189/core/config/schemas.py); [github_gateway.py](https://github.com/xuiltul/animaworks/blob/82f7caa3793f302cfdc74fe460e191d44959a189/server/github_gateway.py); [handler_delegation.py](https://github.com/xuiltul/animaworks/blob/82f7caa3793f302cfdc74fe460e191d44959a189/core/tooling/handler_delegation.py); [handler.py](https://github.com/xuiltul/animaworks/blob/82f7caa3793f302cfdc74fe460e191d44959a189/core/tooling/handler.py)
- Basis: explicit contradiction + unresolved.
- Confidence: medium-high that legacy multi-model dispatch is removed; medium in absence of other audit modes.
- Caveats: Do not report the README multi-model pipeline as an active first-party S3* positive witness without an independently executable separate workflow.

## S4 — Outside-and-then intelligence

- State: ?
- Function: prospectively observe changes outside the current workflow, generate adaptation options, and return chosen changes to organizational future capabilities.
- Disturbance / variety regulated: future customer requirements, emerging technologies, new work sources and long-term capability gaps.
- Decisive decision or feedback right: heartbeat and periodic memory consolidation produce responses, but an external future-option choice that changes the organization's capability is not specifically evidenced.
- Decision owner: unknown.
- Supporting / enforcement mechanisms: heartbeat plan/reflect, memory consolidation/forgetting, task and PR event ingress, schedules and experience history.
- Closure path: heartbeat may propose or plan current work and memory is recalled later; no systematically reconstructed outside-sensing → future adaptation choice → returned change to organization/tool/recruitment capability is evidenced.
- Boundary reachability: heartbeats and memory routines are shipped but not equivalent to prospective S4 intelligence by existence.
- Why this is / is not agent-owned: model-driven task continuation and retrospective compaction do not independently establish a future-facing organizational planning decision.
- External distinction: events capture outside activity but mostly current PR/CI state.
- Future / prospective distinction: ordinary cron, backlog triage and recurrence are not sufficient.
- Adaptation option generated: unverified for a function-specific S4 option.
- Path back into current capability / S3: no reliable first-party prospective adaptation return demonstrated.
- Evidence: [_anima_heartbeat.py](https://github.com/xuiltul/animaworks/blob/82f7caa3793f302cfdc74fe460e191d44959a189/core/_anima_heartbeat.py); [manager.py](https://github.com/xuiltul/animaworks/blob/82f7caa3793f302cfdc74fe460e191d44959a189/core/memory/manager.py); [github_gateway.py](https://github.com/xuiltul/animaworks/blob/82f7caa3793f302cfdc74fe460e191d44959a189/server/github_gateway.py); [README.md](https://github.com/xuiltul/animaworks/blob/82f7caa3793f302cfdc74fe460e191d44959a189/README.md)
- Basis: structural + unresolved.
- Confidence: medium in insufficiency.
- Caveats: individual user deployments may instruct agents to do S4-like research but the generic shipped first-party mode's closure remains unverified.

## S5 — Policy and identity

- State: ?
- Function: decide legitimate ultimate purpose/identity of the managed organization in the presence of a constitutive governance issue.
- Disturbance / variety regulated: conflicting mission and legitimate authority priorities beyond ordinary task permissions.
- Decisive decision or feedback right: human owner configures roles/agents, account access and exception authority; no specific whole-identity policy issue/decision/return is evidenced.
- Decision owner: human operator is final authority for some exceptional tasks, but function-level S5 legitimacy closure remains unresolved.
- Supporting / enforcement mechanisms: configuration of users/roles, `call_human` tool, model permission scopes, supervisor/subordinate hierarchy and shared playbooks.
- Closure path: agent can request human decision and receive notification, but no proven ultimate policy or identity issue resolved and returned to govern the organization's continued purpose.
- Boundary reachability: call_human and configuration are shipped; not enough for S5.
- Why this is / is not agent-owned: a user approval or founder intention is not automatically an S5 issue, nor can superior agents redefine ultimate organization identity from delegation rights.
- Identity / ultimate-policy issue: not established.
- Ultimate authority in each claimed mode: none proven for positive S5, notwithstanding operator's ordinary root permissions.
- Return-to-operation path: authorization/response may reach agent; ultimate policy-decision closure unverified.
- Evidence: [handler_comms.py](https://github.com/xuiltul/animaworks/blob/82f7caa3793f302cfdc74fe460e191d44959a189/core/tooling/handler_comms.py); [handler.py](https://github.com/xuiltul/animaworks/blob/82f7caa3793f302cfdc74fe460e191d44959a189/core/tooling/handler.py); [anima.py](https://github.com/xuiltul/animaworks/blob/82f7caa3793f302cfdc74fe460e191d44959a189/core/anima.py); [README.md](https://github.com/xuiltul/animaworks/blob/82f7caa3793f302cfdc74fe460e191d44959a189/README.md); [schemas.py](https://github.com/xuiltul/animaworks/blob/82f7caa3793f302cfdc74fe460e191d44959a189/core/config/schemas.py)
- Basis: explicit + unresolved.
- Confidence: medium in insufficiency.
- Caveats: do not promote S5=P merely for human escalation/approval or manager charters.

## Distributed OSS parent arrangement

Public AnimaWorks contributors and the separately described private production organization are not part of the generic installed product's decision owner chain. Documented retrospective private metrics are contextual claims, not a first-party runtime ownership witness.

## Self-hosted and non-human modes

Self-hosted work cells may continue on heartbeat/cron after the UI closes; a model-driven manager with actual subordinates can perform current-control S3. A standalone single Anima cannot claim S3=A merely because the package contains a supervisor process. The user remains operator of configuration and exceptional decisions; no whole-identity S5 parent loop established.

## Recursion

One configured Anima hierarchy is the assessed whole. Individual model-driven workers are S1 cells, and the managing Anima is a model decision owner of whole-current S3 only over its actual subordinate subtree. GitHub providers and independent outside work organizations are separate recursions.

## Variety and escalation

Worker models handle local tasks/environment results; manager-model heartbeat and delegation regulate current subordinate commitments; task queues and webhook dedupe reduce repeated notifications and transport work without by themselves establishing S2 cross-agent contention control. Human `call_human` escalates exceptions, but no constituted ultimate identity return is proven.

## Evidence gaps

- S2 needs a current executable conflict gate for distinct S1s competing for one PR/branch; `exclusive_key` is demonstrably retired/ignored at this frozen revision.
- S3=A supported only in a configured manager/subordinate active model mode; live end-to-end two-Anima staffing/feedback replay was not executed in this source assessment.
- S3* requires independent raw evidence access/reviewer selection, a review verdict and enforced corrective return. Current GitHub gateway has removed old multi-model review-pass config; external private claims cannot substitute.
- S4 needs prospective outside-environment adaptation rather than heartbeat/memory retrospection; S5 needs legitimate identity/purpose decision closure, not merely human exception approval.
- No provider-backed run or private SaaS records inspected; assessment uses public frozen first-party implementation and packaged modes.

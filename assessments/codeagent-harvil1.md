---
harness_id: codeagent-harvil1
project_name: CodeAgent (Harvil1)
repository: https://github.com/Harvil1/codeAgent
review_ref: e48780be52949dfcf17338025f6beab48ca01428
reviewed_at: 2026-10-15
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# CodeAgent (Harvil1)

## Review boundary

- System in focus: MIT-licensed first-party Python terminal coding agent in [agent/__init__.py](https://github.com/Harvil1/codeAgent/blob/e48780be52949dfcf17338025f6beab48ca01428/agent/__init__.py) and its shipped CLI/tools at frozen e48780be52949dfcf17338025f6beab48ca01428; not a composite grade for external MCP servers or providers.
- Purpose and identity: local model-directed repository coding, tool use, sessions and optionally separate worker agents in a team.
- Standard-distribution boundary: `main.py` → `cli.py` → `AIAgent.run_conversation`, `model_tools`, `tools/`, agent task store/team coordinator; Python runtime and configured API access.
- Environment: operator request, mutable source tree, shell/tool results, configurable LLM provider, optional worker processes, local workspace and persisted state.
- First-party modes considered: interactive coding loop and packaged team_spawn/task tools; optional skill learning with explicit flag considered separately and **not** assumed always enabled.
- Recursion: parent coding agent plus child model-tool workers, linked by team registry, task assignment and child result channels. No claim of a separate fully viable organization at each nested worker.
- Profile 0.2.4 / Methodology 0.3.7.
- Credited operating / distribution surfaces: `agent/__init__.py`, `agent/team/`, `agent/task_store.py`, `tools/`, shipped CLI, permissions/session support.
- Adjacent first-party surfaces excluded from ownership: maintainer development/tests/hooks examples, external model-provider infrastructure, user-written skills/MCP servers, host governance/CI, and separately deployed tooling.

## Repository architecture

The shipped `AIAgent.run_conversation` manages bounded iterative LLM calls, persistent history and model-selected tool dispatch. Tool returns are visible on later turns. `TeamCoordinator` starts separate worker processes, tracks their live statuses and exposes model-callable team management. A task store supports conditional claims and records task ownership; bound child processes reject modifications to other tasks. There is an optional retrospective skill-learning branch in `agent/skill_learning/` that is disabled by default. These mechanisms are reviewed separately rather than equating every feature name to a VSM function.

## Operational model

A user requests a coding change; the model chooses a repository/tool operation, receives execution results and continues or finishes. In team mode, a parent model can inspect running workers, assign/bind tasks and stop workers. Conditional task claims and binding attenuate a specific shared task ownership conflict; the parent model has live roster and intervention tools. External provider and operator establish context/constraints but do not supply the packaged agent loop.

## S1 — Operations

- State: A
- Function: Select coding actions from changing repository observations and execute model-directed file/shell/tool work until task completion or bounded stop.
- Disturbance / variety regulated: User coding requirements, file contents, tool success/failure, budgets, permission denials.
- Decisive decision or feedback right: AIAgent's model selects tools and follow-up actions after receiving tool results; no human per-step selection required in allowed mode.
- Decision owner: The packaged AIAgent/model-led loop; external provider performs inference but does not supply a separate task-owning agent.
- Supporting / enforcement mechanisms: Agent iteration budget and stop handling, permission gates, model_tools dispatch, sessions/context, tool adapters.
- Closure path: run_conversation → model request → _dispatch_tool_calls → tool result/history → next run_conversation iteration or final answer.
- Why this is / is not agent-owned: AIAgent owns the decision/observation/continuation loop and can operate locally through the shipped CLI. A provider API alone would not produce this tool-control loop.
- Boundary reachability: The supported cli.main / run_interactive instantiates AIAgent; the model-tool loop and tools are shipped first-party.
- Evidence: [agent/__init__.py](https://github.com/Harvil1/codeAgent/blob/e48780be52949dfcf17338025f6beab48ca01428/agent/__init__.py); [cli.py](https://github.com/Harvil1/codeAgent/blob/e48780be52949dfcf17338025f6beab48ca01428/cli.py); [model_tools.py](https://github.com/Harvil1/codeAgent/blob/e48780be52949dfcf17338025f6beab48ca01428/model_tools.py); [agent/llm_client.py](https://github.com/Harvil1/codeAgent/blob/e48780be52949dfcf17338025f6beab48ca01428/agent/llm_client.py).
- Basis: explicit shipped control paths and structural source-first reconstruction at the frozen revision.
- Confidence: high.
- Caveats: This is static source evidence, not a live benchmark; scope is limited to first-party packaged operation.

## S2 — Coordination

- State: C
- Function: Attenuate specific duplicate assignment and unauthorized task-state interference among separately running child worker S1 units.
- Disturbance / variety regulated: Two independently running workers may attempt to claim/operate the same kanban task and corrupt shared task ownership.
- Decisive decision or feedback right: Deterministic conditional task claim arbitrates ownership; coordinator reports contested-task failure to the caller, and binding refuses writes to another worker's task.
- Decision owner: First-party constructed TaskStore/TeamCoordinator ownership guard; discretionary rescope after a rejection belongs to the parent model, not to the file lock.
- Supporting / enforcement mechanisms: Cross-process lock, conditional status/owner update, CODEAGENT_KANBAN_TASK binding, task_tools ownership enforcement.
- Closure path: Parent selects a worker/task ID → coordinator claims task atomically → conflicting claim returns failure to parent as tool result → later parent assignment can change; admitted worker's task mutations are bounded by binding.
- Why this is / is not agent-owned: This is narrower than generic bus/routing: it directly regulates competing ownership of a shared task between independent worker processes with a returned failure signal. It does not prove general repository file-conflict resolution.
- Boundary reachability: team_spawn with task_id and task updates are first-party registered team/task tools used by the shipped model loop.
- Distinct S1 units: first-party separately running `agent/team/worker.py` child coding model loops, each possibly assigned a TaskStore task in one parent-managed team.
- Inter-S1 disturbance: two workers or successive assignments targeting one mutable task can contend for a single task owner, causing duplicate task-state writes/commitments.
- Attenuating coordination relation: TeamCoordinator invokes atomic TaskStore.claim before worker process startup; claim rejects a task owned by another worker and a bound worker cannot update a different task.
- Feedback into subsequent S1 behaviour: a rejected team_spawn/claim returns failure as a tool result to the parent model which can choose a different task/worker on a later loop; task store owner and status are visible to subsequent workers.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the conditional owner transaction directly rejects a concrete inter-worker duplicate-claim disturbance and returns the rejection to the choosing parent; this is *narrow* task-ownership collision attenuation, not general file/worktree conflict handling.
- Evidence: [agent/task_store.py](https://github.com/Harvil1/codeAgent/blob/e48780be52949dfcf17338025f6beab48ca01428/agent/task_store.py); [agent/team/coordinator.py](https://github.com/Harvil1/codeAgent/blob/e48780be52949dfcf17338025f6beab48ca01428/agent/team/coordinator.py); [agent/team/task_binding.py](https://github.com/Harvil1/codeAgent/blob/e48780be52949dfcf17338025f6beab48ca01428/agent/team/task_binding.py); [tools/team_tool.py](https://github.com/Harvil1/codeAgent/blob/e48780be52949dfcf17338025f6beab48ca01428/tools/team_tool.py); [tools/task_tools.py](https://github.com/Harvil1/codeAgent/blob/e48780be52949dfcf17338025f6beab48ca01428/tools/task_tools.py).
- Basis: explicit shipped control paths and structural source-first reconstruction at the frozen revision.
- Confidence: medium.
- Caveats: This is static source evidence, not a live benchmark; scope is limited to first-party packaged operation.

## S3 — Inside-and-now control

- State: A
- Function: Regulate the live roster of child coding operations and their current task commitments at the main-agent team boundary.
- Disturbance / variety regulated: Worker availability, completion/failure, occupied task ownership, finite team capacity and conflicting active commitments.
- Decisive decision or feedback right: The parent model can inspect team_members and task state and choose team_spawn, team_shutdown and task assignments during an active session.
- Decision owner: The main AIAgent using shipped team/task tools; TeamCoordinator enforces member caps and process transitions but does not choose the plan.
- Supporting / enforcement mechanisms: Registry with member status/role, team_members, task tools, spawn/shutdown, message bus, worker status updates.
- Closure path: Live roster/task results enter the model's next turn → model chooses worker/task intervention → coordinator changes running processes / task owner → returned status informs subsequent turns.
- Why this is / is not agent-owned: Distinct from mere process manager: a model-operable whole-current team roster and intervention tools are wired into the same first-party feedback loop. This is a structural capability claim, not a measured autonomous scheduling benchmark.
- Boundary reachability: Team tools are registered with the shipped agent's callable toolset, not a developer CI script or external scheduler.
- Whole-system current view: team_members returns status/role/PID of all first-party team workers, and the task store exposes assigned current work and ownership to the main agent.
- Current-control decision scope: main model can choose which worker/task to spawn, inspect current membership, shut down running workers, and revise current task commitments; deterministic team size/depth ceilings enforce but do not choose those decisions.
- Evidence: [tools/team_tool.py](https://github.com/Harvil1/codeAgent/blob/e48780be52949dfcf17338025f6beab48ca01428/tools/team_tool.py); [agent/team/coordinator.py](https://github.com/Harvil1/codeAgent/blob/e48780be52949dfcf17338025f6beab48ca01428/agent/team/coordinator.py); [agent/team/worker.py](https://github.com/Harvil1/codeAgent/blob/e48780be52949dfcf17338025f6beab48ca01428/agent/team/worker.py); [agent/__init__.py](https://github.com/Harvil1/codeAgent/blob/e48780be52949dfcf17338025f6beab48ca01428/agent/__init__.py); [tools/task_tools.py](https://github.com/Harvil1/codeAgent/blob/e48780be52949dfcf17338025f6beab48ca01428/tools/task_tools.py).
- Basis: explicit shipped control paths and structural source-first reconstruction at the frozen revision.
- Confidence: medium.
- Caveats: This is static source evidence, not a live benchmark; scope is limited to first-party packaged operation.

## S3* — Complementary audit

- State: —
- Function: Provide sufficiently independent operational reality inspection with corrective return to the whole-current S3 controller.
- Disturbance / variety regulated: Child reports may be inaccurate, tool outputs incomplete, and operator state may drift.
- Decisive decision or feedback right: No separately established organization-wide complementary audit judgment with corrective S3 return is demonstrated.
- Decision owner: Child-output checks and optional aux-LLM review are supporting validators; a distinct S3* audit owner is not established.
- Supporting / enforcement mechanisms: Child-claim filesystem/TaskStore check, append_warning, optional handoff_review_enabled, trace logs.
- Closure path: Claim mismatch warnings can reach parent context, but the verifier is scoped to a single delegation and does not own a complementary assessment of current system regulation.
- Why this is / is not agent-owned: Cross-check of declared files/tasks is real yet narrowly local; source does not demonstrate an independent audit of S3 operations or an audit-based current-control corrective obligation.
- Evidence: [agent/team/hallucination_check.py](https://github.com/Harvil1/codeAgent/blob/e48780be52949dfcf17338025f6beab48ca01428/agent/team/hallucination_check.py); [tools/delegate_child.py](https://github.com/Harvil1/codeAgent/blob/e48780be52949dfcf17338025f6beab48ca01428/tools/delegate_child.py); [agent/trace.py](https://github.com/Harvil1/codeAgent/blob/e48780be52949dfcf17338025f6beab48ca01428/agent/trace.py); [config.py](https://github.com/Harvil1/codeAgent/blob/e48780be52949dfcf17338025f6beab48ca01428/config.py).
- Basis: explicit shipped control paths and structural source-first reconstruction at the frozen revision.
- Confidence: medium-high.
- Caveats: This is static source evidence, not a live benchmark; scope is limited to first-party packaged operation.

### Absence scope

- Surfaces inspected: Delegation completion, claim checker, optional handoff review, trace and team registry.
- Plausible first-party paths checked: Filesystem/task claims verification as an S3* path; aux-LLM handoff warnings; external CI/maintainer audit.
- Why no material first-party path remains: Validators append warnings on an individual child report; neither whole-current complementary audit access nor a separately closed S3 corrective-return loop is shipped in the observed mode.

## S4 — Outside-and-then intelligence

- State: —
- Function: Monitor the external future environment and choose/provide prospective organizational adaptation to the current coding system.
- Disturbance / variety regulated: New external coding environments, future model/tool needs, shifts in operating strategy.
- Decisive decision or feedback right: No first-party whole-system external/prospective adaptive decision right is demonstrated.
- Decision owner: Developer/user controls extensions and learning enablement; heuristic skill evolution operates on past in-session trace patterns.
- Supporting / enforcement mechanisms: Disabled-by-default skill_learning observer/evolver, skill storage, memory/compaction, workflow and hooks.
- Closure path: When enabled, repeated past tool patterns can become local skill files; the source does not close external-future sensing → strategic selection → changed operational capacity as an S4 function.
- Why this is / is not agent-owned: An auto-generated habit from task traces is retrospective task improvement; the user-enabled feature by itself does not establish environment-facing prospective S4 governance.
- Evidence: [agent/skill_learning/turn_observer.py](https://github.com/Harvil1/codeAgent/blob/e48780be52949dfcf17338025f6beab48ca01428/agent/skill_learning/turn_observer.py); [agent/skill_learning/evolver.py](https://github.com/Harvil1/codeAgent/blob/e48780be52949dfcf17338025f6beab48ca01428/agent/skill_learning/evolver.py); [agent/skill_learning/observer.py](https://github.com/Harvil1/codeAgent/blob/e48780be52949dfcf17338025f6beab48ca01428/agent/skill_learning/observer.py); [config.py](https://github.com/Harvil1/codeAgent/blob/e48780be52949dfcf17338025f6beab48ca01428/config.py).
- Basis: explicit shipped control paths and structural source-first reconstruction at the frozen revision.
- Confidence: medium.
- Caveats: This is static source evidence, not a live benchmark; scope is limited to first-party packaged operation.

### Absence scope

- Surfaces inspected: Turn learning, skill evolution, memory/compaction, configuration, workflow and runtime models.
- Plausible first-party paths checked: Autonomous skill promotion as S4, environment/future monitoring, operator-created tools, hook updates.
- Why no material first-party path remains: Visible learning paths follow task-history clustering with default disabled and no whole-system external-future sensing and adaptation decision/return.

## S5 — Policy and identity

- State: —
- Function: Resolve legitimacy, ultimate identity and binding mission/policy choices of the harness organization.
- Disturbance / variety regulated: Conflicting user goals, safety settings, credentials and authorization limits.
- Decisive decision or feedback right: Operators set higher-level objective/configuration; ordinary command approvals and system prompt constraints do not resolve organization-wide identity disputes.
- Decision owner: Operator/developer owns settings, permissions and scope outside assessed autonomy; shipped code enforces rather than closes ultimate policy.
- Supporting / enforcement mechanisms: Permission subsystem, command/secret guards, config settings and model tool allowlists.
- Closure path: Approvals or denials affect local tool calls; no supported first-party policy-identity escalation and authoritative returned decision loop is evidenced.
- Why this is / is not agent-owned: Local tool-control policy and user acceptance are not themselves an operational S5 mission/policy closure.
- Evidence: [agent/permission.py](https://github.com/Harvil1/codeAgent/blob/e48780be52949dfcf17338025f6beab48ca01428/agent/permission.py); [config.py](https://github.com/Harvil1/codeAgent/blob/e48780be52949dfcf17338025f6beab48ca01428/config.py); [agent/__init__.py](https://github.com/Harvil1/codeAgent/blob/e48780be52949dfcf17338025f6beab48ca01428/agent/__init__.py); [tools/team_tool.py](https://github.com/Harvil1/codeAgent/blob/e48780be52949dfcf17338025f6beab48ca01428/tools/team_tool.py).
- Basis: explicit shipped control paths and structural source-first reconstruction at the frozen revision.
- Confidence: medium-high.
- Caveats: This is static source evidence, not a live benchmark; scope is limited to first-party packaged operation.

### Absence scope

- Surfaces inspected: Permission and default configuration, safety guards, team policies, user-directed settings and CLI.
- Plausible first-party paths checked: User approval as parent S5, configured agent constraints as constructor S5, team identities as institutional governance.
- Why no material first-party path remains: All paths constrain task/tool execution under externally set purpose; no binding first-party ultimate mission or identity dispute process with returned policy closure is present.

## Distributed OSS parent arrangement

The MIT repository has public maintainers; that developer governance and different customers' local installations do not form one supported live parent S5 control mode. Human permission responses are local tool controls, not a separately proved returned S3/S4/S5 parent-governed mode.

## Self-hosted and non-human modes

Self-hosting with configured provider and first-party tools does not transfer model-choice rights to the inference vendor. Independent team worker processes are subordinate current coding operations at the review boundary. No composite A(P)/C(P) mode is claimed without an independently closed parent mode.

## Recursion

The main agent's control of a roster and optionally nested worker loops defines the assessed team-control recursion. Cross-task conditional claim is a narrow S2 mechanism; stronger workspace-conflict repair and audit claims are not imported.

## Variety and escalation

Tool failures, rejected task claims and worker states return to the main model for further action. A bounded iteration budget and approvals prevent unbounded operations but do not imply autonomous S4/S5.

## Evidence gaps

No live model benchmark was performed. S2 claim/ownership arbitration is concrete but not proof of merge/write conflict repair. S3 is structurally available through parent roster/task tools; its effectiveness in sustained multi-worker deployments is unmeasured. Handoff review flag defaults off and claim checking lacks whole-current S3* audit closure. Retrospective skill evolution lacks future external adaptation authority.

## Assessment summary

**Proposed included**, source-first vector `S1=A / S2=C / S3=A / S3*=— / S4=— / S5=—`. S2 is limited to conflict attenuation in task ownership; S3 is evidenced by model-selected team-wide current-control actions. The result must pass the Skills structural oracle, Index validation and the separate canonical admission lifecycle before becoming an included corpus row.

---
harness_id: liumengxuan04-minicode
project_name: MiniCode
repository: https://github.com/LiuMengxuan04/MiniCode
review_ref: 55dca55e13b7f34364893f3190914406be860b70
reviewed_at: 2026-10-13
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

# MiniCode

## Review boundary

- System in focus: the installable first-party terminal coding agent `mini-code` at its frozen git revision, its model/tool loop, privileged root coding actor and subordinate read-only investigative workers.
- Purpose and identity: autonomously inspect and modify a developer's source tree through model-selected tools under user approvals and task/session feedback.
- Relevant environment: a local Git checkout and filesystem, shell commands, model API, human goal, permissions, optional MCP/skills and web access.
- Standard-distribution boundary: the shipped CLI/TUI, repository-own tool registry, root model/action loop, file/shell permission and review gates, local session/context mechanisms, plus the supported opt-in in-memory read-only SubAgentManager.
- Credited operating / distribution surfaces: [README.md](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/README.md); [ARCHITECTURE.md](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/ARCHITECTURE.md); [agent-loop.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/agent-loop.ts); [index.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/index.ts); [tool.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/tool.ts); [index.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/tools/index.ts); [sub-agents.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/tools/sub-agents.ts); [manager.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/agents/manager.ts); [worker-prompt.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/agents/worker-prompt.ts); [permissions.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/permissions.ts); [file-review.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/file-review.ts); [session.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/session.ts); [memory.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/memory.ts); [plan.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/tools/plan.ts); [goal.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/tools/goal.ts); [web-search.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/tools/web-search.ts); [auto-compact.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/compact/auto-compact.ts).
- Adjacent first-party surfaces excluded from ownership: tests and package development/CI, architecture-roadmap items that are explicitly not yet built, hypothetical future nested or persistent swarm modes, user-authored MCP servers and skills, and external model/provider governance.
- First-party operating / deployment modes considered: interactive coding root with task-specific permission prompts; session resume/fork and auto-compaction; up to three read-only research subagents created by the root; optional configured model and MCP/skill integrations.
- Recursion level: one root coding session and its scoped read-only sub-agent research tasks, not the maintainer's project organization or separate tool providers.
- Reviewed revision: `55dca55e13b7f34364893f3190914406be860b70`.
- Observation date: 2026-10-13.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

[ARCHITECTURE.md](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/ARCHITECTURE.md) explicitly identifies `model → tool → model` as the product's main execution loop. [agent-loop.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/agent-loop.ts) calls an active model with registered tool schemas, executes chosen file/shell/search/skill tools and returns their outcomes to the next model step; [tool.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/tool.ts) and [index.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/tools/index.ts) own validation and dispatch, and [permissions.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/permissions.ts)/[file-review.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/file-review.ts) bound high-risk edits. [session.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/session.ts) persists append-only session events and resumable context; [memory.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/memory.ts) loads layered project instructions, not independently evolving organization-wide policy. Goals and plans in [plan.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/tools/plan.ts)/[goal.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/tools/goal.ts) concern current-user task criteria and progress, not metasystem authority by themselves.

The shipped subagent boundary is particularly explicit. [sub-agents.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/tools/sub-agents.ts) exports root-only `spawn_agent`, `list_agents`, `wait_agent`, and `close_agent`; [manager.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/agents/manager.ts) maintains up to three running subagents. [worker-prompt.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/agents/worker-prompt.ts) directs every child to **read/search/research only**, excluding edits, terminal execution, user interaction and further subagents; the root remains the only first-party coding modifier. Their reports feed the root's task decisions. [ARCHITECTURE.md](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/ARCHITECTURE.md) explicitly marks persistent agent definitions, nested workers, task-swarm orchestration and remote sessions as future/not yet built, so no future planned behavior is credited now.

## Operational model

The root model makes task-aware choices of tools and file edits after seeing actual observations. Permission and diff approval are operator-owned authorization, while deterministic tooling implements checked side effects. Optional read-only workers perform limited information-gathering S1 tasks and return reports. Their concurrency cap, status list and cancellation do not establish a wider multi-coding-worker operational portfolio; there is no shipped path where two independently code-writing S1s are coordinated over shared changes.

## S1 — Operations

- State: A
- Function: perform uncertain local developer coding work by choosing inspections, edits, commands, follow-up repairs and final response.
- Disturbance / variety regulated: unknown repository structure and behavior, tool errors, incomplete modifications, shell/test feedback, and changing task-local context.
- Decisive decision or feedback right: root model selects the next tool/coding action in response to actual returned tool results and goal/plan observations.
- Decision owner: root coding agent/model, not static tool registry, permissions or local session store.
- Supporting / enforcement mechanisms: CLI/TUI presentation, tool schemas, permission checks, edit review, context compaction and append-only sessions.
- Closure path: model turn → selected read/search/edit/shell operation or denied permission → actual result → model continuation/repair/final.
- Boundary reachability: standard CLI directly instantiates the first-party model/tool loop and built-in mutating coding tools; no external developer composition is required.
- Why this is / is not agent-owned: removing model discretion leaves action primitives and safety gates but no adaptive code-edit choice after observations.
- Evidence: [README.md](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/README.md); [ARCHITECTURE.md](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/ARCHITECTURE.md); [agent-loop.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/agent-loop.ts); [tool.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/tool.ts); [index.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/tools/index.ts); [permissions.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/permissions.ts); [file-review.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/file-review.ts)
- Basis: explicit and structural
- Confidence: high for source-wired loop, no credentialed live model task executed
- Caveats: human owner explicitly approves risky actions; child research reports support but do not replace the root coding owner.


## S2 — Coordination

- State: —
- Function: no shipped regulation of a specific interference between multiple independently operating coding S1 units.
- Disturbance / variety regulated: possible inter-worker conflicts are not materially presented in the read-only child architecture.
- Decisive decision or feedback right: no inter-S1 conflict-response discretion or return channel is established at the declared recursion.
- Decision owner: none evidenced for S2; root alone owns code writes, while children investigate independent read-only questions.
- Supporting / enforcement mechanisms: three-worker concurrency cap, in-memory status, wait and cancel APIs.
- Closure path: a child research report returns to root task choice, not to a dedicated cross-worker interference attenuation/return loop.
- Why this is / is not agent-owned: task decomposition, multiple read-only investigations and bounded concurrent model calls cannot create a file-write collision among distinct first-party coding cells at this scope.
- Evidence: [ARCHITECTURE.md](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/ARCHITECTURE.md); [sub-agents.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/tools/sub-agents.ts); [manager.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/agents/manager.ts); [worker-prompt.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/agents/worker-prompt.ts); [agent-loop.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/agent-loop.ts)
- Basis: explicit implementation boundary plus structural inspection
- Confidence: high for supplied standard-distribution read-only worker path
- Caveats: external/custom workers could introduce real conflicting operational units but are excluded.

### Absence scope

- Surfaces inspected: in-memory SubAgentManager, root and child tool registries, architecture and worker prompt
- Plausible first-party paths checked: shared resource conflicts, mutually destructive edits, explicit interference feedback/attenuation and changed child operations
- Why no material first-party path remains: all shipped children are research/read-only workers while the root exclusively edits; no material S2-specific collision-control loop is provided.


## S3 — Inside-and-now control

- State: —
- Function: no whole-current multi-S1 operational management of resources/priorities/commitments is established.
- Disturbance / variety regulated: individual task limits, read-only child investigation statuses and completion of a user goal.
- Decisive decision or feedback right: root selects its own subtasks and may close a research worker, but no separate whole-system current-control decision is evidenced.
- Decision owner: root for coding delegation; human for user task and permission settings; deterministic manager for the fixed cap.
- Supporting / enforcement mechanisms: agent roster, wait, abort, plan/Todo, goal criteria, per-turn step limits.
- Closure path: child completion informs root's next coding turn, but no live organization-wide reprioritization or constraint return across independent S1 operations.
- Why this is / is not agent-owned: a class named SubAgentManager and root tool scheduling are not proof of a whole-current metasystem; all edits stay with one root coding unit.
- Evidence: [ARCHITECTURE.md](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/ARCHITECTURE.md); [manager.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/agents/manager.ts); [sub-agents.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/tools/sub-agents.ts); [plan.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/tools/plan.ts); [goal.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/tools/goal.ts); [agent-loop.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/agent-loop.ts)
- Basis: explicit and structural
- Confidence: medium-high
- Caveats: local task lifecycle is bounded and useful; no autonomous S3 claim follows.

### Absence scope

- Surfaces inspected: root/child execution, capped worker manager, goal and plan tooling, user approval and persistence
- Plausible first-party paths checked: whole-current visibility across autonomous coding units, shared resource/priority bargaining and parent-governed current-control loop
- Why no material first-party path remains: only root coding work plus read-only research subagents and fixed operational constraints are shipped; no S3 decision authority and returned multi-unit control is established.


## S3* — Complementary audit

- State: —
- Function: no shipped independently commissioned complementary audit with findings returned to a distinct current-control owner.
- Disturbance / variety regulated: potential incorrect implementing-agent claims that would warrant direct independent challenge.
- Decisive decision or feedback right: no first-party independently assigned audit judgment and corrective governance return is evidenced.
- Decision owner: root task model for ordinary review and repair, developer for edit approvals; generic read-only child can investigate any task but has no dedicated auditor authority.
- Supporting / enforcement mechanisms: file-review diff approval, root verification commands, generic investigation/report path, tests as adjacent development infrastructure.
- Closure path: read-only investigation report or diff-approval feedback may influence the same root task, but no distinct S3* audit finding/disposition pipeline to managerial control exists.
- Why this is / is not agent-owned: an instruction to return findings on a user-assigned investigation is not an independent complementary audit contract; ordinary self-verification is not S3*.
- Evidence: [worker-prompt.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/agents/worker-prompt.ts); [manager.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/agents/manager.ts); [sub-agents.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/tools/sub-agents.ts); [file-review.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/file-review.ts); [ARCHITECTURE.md](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/ARCHITECTURE.md); [agent-loop.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/agent-loop.ts)
- Basis: structural
- Confidence: medium-high within shipped features
- Caveats: a root could manually request a code review using the generic child, but an uninstantiated optional use does not establish first-party S3* closure.

### Absence scope

- Surfaces inspected: general read-only subagent prompt and tool list, root edit-review and normal testing paths
- Plausible first-party paths checked: separate auditor role, direct raw-artifact sampling, reviewer authority, independence from producer status and explicit returned corrective current-control disposition
- Why no material first-party path remains: available mechanisms are standard task research and human approval rather than an audit-specific owned/reconciled loop.


## S4 — Outside-and-then intelligence

- State: —
- Function: no continuously available externally and prospectively oriented capability-adaptation decision loop.
- Disturbance / variety regulated: changing model availability, tools and documentation, as opposed to coding task facts.
- Decisive decision or feedback right: no agent or first-party parent selects future system adaptations based on environmental prognosis and returns them to current capability.
- Decision owner: user installs/configures skills/models; agent chooses context and resources for current tasks only.
- Supporting / enforcement mechanisms: layered memory, online search/fetch, skill manager, context compaction and goal tracking.
- Closure path: new information informs the current coding goal or is persisted as user instructions; no prospective alternative/decision/return to organizational capability.
- Why this is / is not agent-owned: project context and goal updates do not constitute VSM S4 future adaptation.
- Evidence: [ARCHITECTURE.md](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/ARCHITECTURE.md); [memory.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/memory.ts); [web-search.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/tools/web-search.ts); [goal.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/tools/goal.ts); [session.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/session.ts)
- Basis: structural
- Confidence: medium-high
- Caveats: developer roadmap lists future features but is adjacent and not shipped.

### Absence scope

- Surfaces inspected: memory loading, context management, web search, plan/goal, roadmap, model and skill configuration
- Plausible first-party paths checked: future environmental sensing, agent-produced adaptation alternatives, approved parent/autonomous adoption and return into later operating capability
- Why no material first-party path remains: implemented tools serve immediate tasks and human-configured knowledge; future organizational adaptation is not a reachable first-party execution path.


## S5 — Policy and identity

- State: —
- Function: no ultimate-purpose identity-policy arbitration and binding return path is established.
- Disturbance / variety regulated: constitutional identity conflicts beyond ordinary tool safety/approval.
- Decisive decision or feedback right: human sets tasks and safety policy; no runtime S5 policy judgment owner.
- Decision owner: user/parent outside session for purpose, permission and accepted changes.
- Supporting / enforcement mechanisms: allow/deny lists, edit review, shell confirmation, project instruction memory and bounded child tools.
- Closure path: human may approve a command or edit, affecting that one operation, but no identity-level proposal → authority → decision → subsequent governance change loop.
- Why this is / is not agent-owned: static guardrails and user task approval differ categorically from S5 identity governance.
- Evidence: [permissions.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/permissions.ts); [file-review.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/file-review.ts); [worker-prompt.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/agents/worker-prompt.ts); [ARCHITECTURE.md](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/ARCHITECTURE.md); [memory.ts](https://github.com/LiuMengxuan04/MiniCode/blob/55dca55e13b7f34364893f3190914406be860b70/src/memory.ts)
- Basis: structural
- Confidence: medium-high
- Caveats: OSS maintainer governance and changes to system purpose are external to installed session.

### Absence scope

- Surfaces inspected: permissions, diff review, system/child prompts, local rules, repository contribution docs
- Plausible first-party paths checked: identity or ultimate-policy dispute reaching an in-boundary/parent authority and subsequent binding policy return
- Why no material first-party path remains: supplied permissions decide ordinary tool effects, not organizational identity; parent closure loop is not shipped.

## Recursion

Read-only child agents are separate investigative S1 task cells with isolated model histories and restricted tools, but not complete recursively viable organizations. The only code-modifying operational owner is the root; the user's broader software team and maintainer development system lie outside this assessment boundary.

## Variety and escalation

Root model decisions absorb repository/tool uncertainty, while permission gates attenuate risky side effects and may consult the human. Child research adds information capacity, but the three-child limit and cancellation are execution controls, not automatically inter-S1 coordination or S3 current control. Errors and session/compaction checkpoints preserve task-local continuity.

## Evidence gaps

Static primary-code assessment at frozen commit. No live provider account was exercised. A first-party role-specific independent audit or multi-coding-worker coordinator in a later revision would require separate new-ref review; the documented planned nested/task-swarm system does not count here. `—` is bounded to this shipped first-party distribution and does not assert future impossibility.

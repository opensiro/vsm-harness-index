---
harness_id: reflex
project_name: Reflex
repository: https://github.com/reflex-agent/reflex-agent
review_ref: f3b3dd7b438c8333e5731a29023eca81239c7d19
reviewed_at: 2026-09-22
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
assessment_changed_at: 2026-09-22
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Reflex

## Review boundary

- **System in focus:** the first-party Reflex local-first personal-agent control layer at pinned revision `f3b3dd7b438c8333e5731a29023eca81239c7d19`: topic/orchestrator protocol, task/worktree dispatch, workflow scheduler, permissions, project dashboard, persistent Markdown/FTS state, utilities/host API and notification surfaces.
- **Purpose and identity:** organize persistent personal/project work around model-driven topics and specialist agents while retaining local state, explicit permissions, scheduled workflows and user-visible current-control surfaces.
- **Relevant environment:** user project repositories and files, local host processes, Claude Code/Codex/Ollama/model providers, Git, Telegram/web UI, external MCP servers and other services reached through generated utilities or agent tools.
- **Standard-distribution boundary:** Reflex-owned server, prompts/protocol, topic/task/workflow stores, worktree and permission machinery, dashboard, utilities and scheduler. Claude Code and Codex are separate subprocess agent implementations; their internal reasoning, tool policy and organizational functions are not credited to Reflex merely because Reflex launches them.
- **Credited operating / distribution surfaces:** the default Reflex chat/orchestrator protocol; topic `/goal` continuation; task dispatch with first-party worktree isolation; root dashboard and approval surfaces; durable scheduler/workflows; built-in system tasks; utility host API and audit log where they materially support a mapped function.
- **Adjacent first-party surfaces excluded from ownership:** roadmap/north-star planning documents are not treated as released runtime behavior; generic event logs, FTS indexing, memory rollups, AI dashboard suggestions and prompt/configuration editors are not promoted to metasystem ownership without the required organizational loop.
- **First-party modes considered:** interactive web/Telegram conversation; delegated specialist execution; task-board code dispatch; scheduled workflows; user-supervised approval/intervention.
- **Recursion level:** one Reflex Space/project organization, with concurrent topic/task agent executions treated as candidate S1 operating units where evidence establishes distinct work.
- **Reviewed revision:** `f3b3dd7b438c8333e5731a29023eca81239c7d19`.
- **Observation date:** 2026-09-22.
- **Generated/current Profile / Methodology:** `0.2.3` / `0.3.5`.

## Repository architecture

Reflex keeps durable topics, task records, project memory and workflow definitions under its own local state boundary. Its chat prompt defines an orchestrator role that may dispatch specialist sub-agents and is reinvoked with their results. Code tasks are bound to per-task Git worktrees before the selected agent subprocess starts. A background scheduler walks registered Spaces and runs due workflows and system tasks. A project dashboard aggregates active goals/running agents and pending approvals, while interactive responses allow the user to permit or deny requested operations and topic controls can stop or abandon ongoing work.

Claude Code and Codex remain implementation substrates/child agent processes. This assessment credits Reflex only where Reflex itself establishes the organizational relation, decision surface and return path around those actors.

## Primary evidence

- [`lib/reflex/prompts/defaults.ts`](https://github.com/reflex-agent/reflex-agent/blob/f3b3dd7b438c8333e5731a29023eca81239c7d19/lib/reflex/prompts/defaults.ts) — Reflex-owned orchestration/dispatch protocol, specialist roles and reinvocation after delegated results.
- [`lib/server/agents/headless.ts`](https://github.com/reflex-agent/reflex-agent/blob/f3b3dd7b438c8333e5731a29023eca81239c7d19/lib/server/agents/headless.ts) — first-party ephemeral agent execution path used by workflows/utilities.
- [`lib/server/tasks/dispatch.ts`](https://github.com/reflex-agent/reflex-agent/blob/f3b3dd7b438c8333e5731a29023eca81239c7d19/lib/server/tasks/dispatch.ts) — task-to-agent dispatch, worktree binding and task-state closure.
- [`lib/server/tasks/worktree.ts`](https://github.com/reflex-agent/reflex-agent/blob/f3b3dd7b438c8333e5731a29023eca81239c7d19/lib/server/tasks/worktree.ts) — explicit file-collision disturbance and per-task worktree/branch isolation.
- [`lib/server/dashboard-actions.ts`](https://github.com/reflex-agent/reflex-agent/blob/f3b3dd7b438c8333e5731a29023eca81239c7d19/lib/server/dashboard-actions.ts) — project-wide aggregation of active goals, running agents, pending approvals, recent knowledge and suggestions.
- [`app/roots/[id]/_components/dashboard-active-goals.tsx`](https://github.com/reflex-agent/reflex-agent/blob/f3b3dd7b438c8333e5731a29023eca81239c7d19/app/roots/%5Bid%5D/_components/dashboard-active-goals.tsx) — user-facing current commitments/running-work view.
- [`app/roots/[id]/_components/dashboard-pending-approvals.tsx`](https://github.com/reflex-agent/reflex-agent/blob/f3b3dd7b438c8333e5731a29023eca81239c7d19/app/roots/%5Bid%5D/_components/dashboard-pending-approvals.tsx) — cross-topic aggregation of permission/question/MCP decisions awaiting the user.
- [`lib/server/topic-actions.ts`](https://github.com/reflex-agent/reflex-agent/blob/f3b3dd7b438c8333e5731a29023eca81239c7d19/lib/server/topic-actions.ts) — start, stop/delete and goal-abandonment actions that return user intervention into live operation.
- [`lib/server/agents/manager.ts`](https://github.com/reflex-agent/reflex-agent/blob/f3b3dd7b438c8333e5731a29023eca81239c7d19/lib/server/agents/manager.ts) and [`app/api/agents/[agentId]/respond/route.ts`](https://github.com/reflex-agent/reflex-agent/blob/f3b3dd7b438c8333e5731a29023eca81239c7d19/app/api/agents/%5BagentId%5D/respond/route.ts) — live permission decisions and their return to the waiting agent process.
- [`lib/server/workflows/scheduler.ts`](https://github.com/reflex-agent/reflex-agent/blob/f3b3dd7b438c8333e5731a29023eca81239c7d19/lib/server/workflows/scheduler.ts) — durable per-Space workflow scheduling and built-in system-task execution.
- [`lib/server/workflows/system-tasks.ts`](https://github.com/reflex-agent/reflex-agent/blob/f3b3dd7b438c8333e5731a29023eca81239c7d19/lib/server/workflows/system-tasks.ts) — weekly memory rollup and session indexing; used here mainly to bound S4 claims.
- [`lib/server/utilities/audit.ts`](https://github.com/reflex-agent/reflex-agent/blob/f3b3dd7b438c8333e5731a29023eca81239c7d19/lib/server/utilities/audit.ts) — host-API call tracing; used to distinguish observability from S3* independence.

## Operational model

A user creates or resumes a persistent topic or task. Reflex starts a configured model/harness actor under a Reflex-owned prompt/protocol. The orchestrator may answer directly or issue one or more specialist dispatch markers; Reflex runs those child turns and re-invokes the orchestrator with their results. For code tasks, Reflex first allocates a separate Git worktree and runs the task agent inside it, preventing concurrent task actors from mutating the same checkout. Persistent goals can auto-continue until a Reflex quick-model check reports completion or a bounded iteration limit/intervention stops the loop.

Across a Space, Reflex exposes the current set of goals/running agents and decisions waiting on the user. The user can stop/abandon work and allow or deny requested capabilities; those decisions are delivered back into the waiting runtime. Scheduled workflows can launch further operational agent turns without an interactive user request.

## S1 — Operations

- **State:** `A`.
- **Function:** model-driven execution of user/project work through persistent Reflex topics, delegated specialist turns, tasks and scheduled/headless runs.
- **Disturbance / variety regulated:** open-ended user requests, project/file state, tool results, specialist findings, task progress, permissions and workflow-triggered work.
- **Decisive decision or feedback right:** within a running Reflex topic, the configured model actor chooses how to pursue the requested outcome, including whether and how to delegate specialist work, what result to synthesize and which Reflex action markers to emit.
- **Decision owner:** autonomous model-driven operating actor running under Reflex's first-party orchestrator protocol.
- **Supporting / enforcement mechanisms:** persistent topics/events, specialist dispatch protocol, task records, bounded `/goal` continuation, worktree cwd binding, host tools, permissions and headless execution.
- **Closure path:** model decision → Reflex action/dispatch/tool execution → changed project/task/environment state or child-agent result → observation/reinvocation → subsequent model decision/output.
- **Boundary reachability:** the default interactive topic path is directly user-reachable; scheduled workflows and task dispatch also reach the same first-party orchestrator runtime.
- **Ownership rationale:** the underlying Claude Code/Codex/model implementation is external, but Reflex supplies the organizational operating protocol and closes the execution/result loop around the actor. No internal Claude/Codex metasystem behavior is imported into this classification.
- **Basis / confidence:** explicit + structural; high.

## S2 — Coordination

- **State:** `C`.
- **Function:** attenuate interference between concurrent code-task S1 units that would otherwise mutate the same repository checkout/files.
- **Distinct S1 units:** separate task-bound model/agent executions can run against the same project repository.
- **Specific interference:** `tasks/worktree.ts` explicitly states that each code task receives its own checkout so concurrent task work does not collide on files; shared checkout mutation would create cross-task interference.
- **Coordination relation:** before a code task starts, Reflex creates a unique `task/<slug>` branch and worktree and binds the dispatched agent's cwd to that isolated checkout. Later merge is a separate controlled operation.
- **Feedback into subsequent S1 behavior:** the task agent receives the isolated worktree path and prompt instruction to commit there rather than touching main; its subsequent file operations therefore occur in a separate coordination lane.
- **Decisive coordination right:** the shipped host policy deterministically selects isolation for qualifying code tasks. It does not establish an autonomous first-party coordinator that can reason over competing task units and choose/adjust coordination policy across them.
- **Decision owner:** first-party Reflex constructor/enforcement surface; autonomous coordination ownership remains uncomposed.
- **Supporting / enforcement mechanisms:** unique worktree/branch allocation, collision checks, worktree-bound task dispatch and explicit later merge path.
- **Boundary reachability:** standard task dispatch reaches this path automatically for code tasks in Git repositories.
- **Ownership rationale:** unlike generic routing, this is a concrete S2 disturbance with a first-party attenuation relation and closed effect on later S1 behavior. It remains `C`, not `A`, because Reflex supplies the coordination primitive/policy but not an autonomous coordinator owning discretionary S2 decisions.
- **Basis / confidence:** explicit + structural; high.

## S3 — Inside-and-now control

- **State:** `P`.
- **Function:** whole-Space current supervision and intervention over ongoing commitments, running agent work and blocked permission decisions.
- **Whole-system current view:** the root dashboard aggregates active persistent goals, running agents without goals and pending permission/question/MCP interactions across every topic in the Space; dashboard actions also assemble recent knowledge and project suggestions.
- **Current-control scope:** the user can enter the originating topic, stop/delete a running topic, abandon a persistent goal, answer agent questions and allow/deny requested operations; these decisions alter or terminate subsequent live execution. Task/worktree merge remains an explicit controlled operation rather than an automatic child-agent right.
- **Disturbance / variety regulated:** simultaneous current commitments, runaway/stale work, blocked agent turns, requested privileges and operational intervention needs.
- **Decisive decision or feedback right:** current-control interventions that cross the Space remain with the user/owner; Reflex aggregates state, exposes the decision points and enforces the returned choice.
- **Decision owner:** legitimate parent user/owner.
- **Supporting / enforcement mechanisms:** root dashboard aggregation, active-goal/running-agent views, pending-approval aggregation, `agentManager.stopTopic`, goal clearing, permission response bridge and task merge controls.
- **Closure path:** Reflex surfaces whole-Space current state / blocked decision → user selects stop/abandon/allow/deny/other intervention → Reflex manager/store applies it → the waiting or running operational path changes accordingly.
- **Boundary reachability:** these controls are first-party web/Telegram/runtime surfaces in the normal distribution, not developer-only internals.
- **Ownership rationale:** Reflex does not show an autonomous supervisor with authority to reprioritize or intervene across the Space. The parent user owns that current-control authority, so the established S3 mode is `P`.
- **Basis / confidence:** explicit + structural; medium-high.

## S3* — Complementary audit

- **State:** `—`.
- **Rationale:** Reflex records detailed host-API audit entries and exposes operational events/status, but the audit log is emitted by the same execution path it records. It does not establish a sufficiently independent complementary channel that tests ordinary operational claims against a separate source of reality, makes an audit judgment and returns findings into S3 control.
- **Boundary reachability:** audit and event surfaces are reachable, but they provide observability rather than the required independent audit function.
- **Basis / confidence:** explicit absence after source review; high.

### Absence scope

Reviewed utility audit generation/reader, dashboard status aggregation, task observation, agent event logs and the documented runtime/permission paths. No first-party complementary auditor with distinct access and corrective return was found at the pinned revision.

## S4 — Outside-and-then intelligence

- **State:** `—`.
- **Rationale:** Reflex has durable workflows, generated utilities, searchable memory, weekly memory rollup and an AI "what's next" suggestion surface. At the pinned revision these do not establish the full S4 loop: deliberate sensing of external/future-relevant distinctions, formation of adaptation options, an adaptation decision, and return into present capability/current control so future operating repertoire changes.
- **Boundary reachability:** scheduler/workflow and suggestion surfaces are first-party and reachable, but the shipped examples primarily execute configured work or summarize current/past internal state. The dashboard suggestion model is on-demand and proposes current project actions rather than owning prospective capability adaptation.
- **Basis / confidence:** structural absence after source review; medium-high.

### Absence scope

Reviewed workflow scheduler/runner/system tasks, background runtime, AI suggestions, memory rollup, utility host/update surfaces and task/orchestrator paths. Generated utilities may extend capability when a user or current operating agent asks for one, but current-task extension alone is not evidence of S4 environmental intelligence.

## S5 — Policy and identity

- **State:** `—`.
- **Rationale:** Reflex exposes model assignments, prompt templates, permissions, workflow definitions and project settings, but these are operational configuration/constraints. No first-party path was found that identifies a system-identity or ultimate-policy question, routes it to an actor with explicit ultimate-policy authority, and closes the returned decision into the organization's identity at this recursion.
- **Boundary reachability:** settings and prompt surfaces are reachable but do not by themselves establish S5 ownership.
- **Basis / confidence:** structural absence after source review; high.

### Absence scope

Reviewed default prompts, settings/model assignment surfaces, permission decisions, workflow/task controls and project dashboard paths. The assessment does not infer S5 merely because the user can edit prompts or authorize tools.

## Recursion

A Reflex Space/project is the declared system boundary. Topics and task-bound executions are operating units within that boundary when they perform distinct project work. Claude Code/Codex subprocesses are external agent implementations recruited into those operating paths, not automatically recursive viable systems whose internal S-functions transfer to Reflex. Separate Spaces, external MCP servers and generated utilities would require their own boundary-specific evidence before being treated as recursive viable systems.

## Variety and escalation

Reflex attenuates operational variety through persistent topics/tasks, isolated code-task worktrees, bounded goal continuation, workflow schedules and permission gates. It amplifies operational repertoire through delegated specialist roles and utility/workflow execution. Requests exceeding granted authority escalate to explicit user permission/question surfaces; whole-Space current intervention likewise returns to the parent user, supporting `S3=P` without implying S5.

## Evidence gaps

- No evidence was found that an autonomous Reflex actor owns whole-Space reprioritization/current-control rights; S3 therefore remains parent-governed.
- The S2 constructor classification is limited to the evidenced concurrent code-task file-collision path; generic multi-agent dispatch is not independently counted as S2.
- Utility generation and scheduled workflows may support richer adaptation in particular user-authored deployments, but such downstream compositions are outside the standalone pinned-repository assessment.
- External Claude Code/Codex implementation details were intentionally excluded from Reflex ownership.

## Admission conclusion

Standalone vector at the pinned revision: `A C P — — —`.

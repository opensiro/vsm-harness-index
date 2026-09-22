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

- System in focus: the first-party Reflex local-first personal-agent control layer at pinned revision `f3b3dd7b438c8333e5731a29023eca81239c7d19`, including topic/orchestrator protocol, task/worktree dispatch, workflow scheduler, permissions, project dashboard, persistent local state, utilities/host API and notification surfaces.
- Purpose and identity: organize persistent personal/project work around model-driven topics and specialist agents while retaining local state, explicit permissions, scheduled workflows and user-visible current-control surfaces.
- Relevant environment: user project repositories and files, local host processes, Claude Code/Codex/Ollama/model providers, Git, Telegram/web UI, external MCP servers and services reached through utilities or agent tools.
- Standard-distribution boundary: Reflex-owned server, prompts/protocol, topic/task/workflow stores, worktree and permission machinery, dashboard, utilities and scheduler. Claude Code and Codex are separate subprocess agent implementations; their internal reasoning, tool policy and organizational functions are not credited to Reflex merely because Reflex launches them.
- Credited operating / distribution surfaces: `lib/reflex/prompts/defaults.ts`; `lib/server/agents/headless.ts`; `lib/server/agents/manager.ts`; `lib/server/tasks/dispatch.ts`; `lib/server/tasks/worktree.ts`; `lib/server/dashboard-actions.ts`; root dashboard active-goal/pending-approval components; `lib/server/topic-actions.ts`; permission response bridge/API; workflow scheduler/system tasks; utility host/audit surfaces where they materially support a mapped function.
- Adjacent first-party surfaces excluded from ownership: roadmap/north-star planning documents; generic event logs and FTS indexing; memory rollups and on-demand AI dashboard suggestions except as inspected negative evidence for S4; prompt/configuration editors except as inspected negative evidence for S5; repository CI/tests except as corroborating implementation evidence.
- First-party operating / deployment modes considered: interactive web/Telegram conversation; delegated specialist execution; task-board code dispatch; scheduled workflows/headless runs; user-supervised approval and intervention.
- Recursion level: one Reflex Space/project organization, with concurrent topic/task agent executions treated as candidate S1 operating units where they perform distinct project work.
- Reviewed revision: `f3b3dd7b438c8333e5731a29023eca81239c7d19`.
- Observation date: 2026-09-22.
- Generated Profile version: `0.2.3`.
- Generated Methodology version: `0.3.5`.
- Current Profile version: `0.2.3`.
- Current Methodology version: `0.3.5`.

## Repository architecture

Reflex keeps durable topics, task records, project memory and workflow definitions under its own local state boundary. Its first-party chat prompt defines an orchestrator role that may dispatch specialist sub-agents and is reinvoked with their results. Code tasks are bound to per-task Git worktrees before the selected agent subprocess starts. A background scheduler walks registered Spaces and runs due workflows/system tasks. The project dashboard aggregates active goals, running agents and pending approvals, while interactive responses let the user permit or deny requested operations and topic controls can stop or abandon ongoing work.

Claude Code and Codex remain implementation substrates/child agent processes. This assessment credits Reflex only where Reflex itself establishes the organizational relation, decision surface and return path around those actors.

## Operational model

A user creates or resumes a persistent topic or task. Reflex starts a configured model/harness actor under a Reflex-owned prompt/protocol. The orchestrator may answer directly or emit one or more specialist dispatch markers; Reflex runs the child turns and reinvokes the orchestrator with their results. For code tasks, Reflex first allocates a separate Git worktree and runs the task agent inside it, preventing concurrent task actors from mutating the same checkout. Persistent goals can auto-continue until a quick-model check reports completion or a bounded iteration/intervention stops the loop.

Across a Space, Reflex exposes current goals/running agents and decisions waiting on the user. The user can stop/abandon work and allow or deny requested capabilities; those decisions are returned to the waiting runtime. Scheduled workflows can launch further operational agent turns without an interactive user request.

## Primary evidence

- [`lib/reflex/prompts/defaults.ts`](https://github.com/reflex-agent/reflex-agent/blob/f3b3dd7b438c8333e5731a29023eca81239c7d19/lib/reflex/prompts/defaults.ts) — Reflex-owned orchestration/dispatch protocol, specialist roles and reinvocation after delegated results.
- [`lib/server/agents/headless.ts`](https://github.com/reflex-agent/reflex-agent/blob/f3b3dd7b438c8333e5731a29023eca81239c7d19/lib/server/agents/headless.ts) — first-party ephemeral agent execution path used by workflows/utilities.
- [`lib/server/tasks/dispatch.ts`](https://github.com/reflex-agent/reflex-agent/blob/f3b3dd7b438c8333e5731a29023eca81239c7d19/lib/server/tasks/dispatch.ts) — task-to-agent dispatch, worktree binding and task-state closure.
- [`lib/server/tasks/worktree.ts`](https://github.com/reflex-agent/reflex-agent/blob/f3b3dd7b438c8333e5731a29023eca81239c7d19/lib/server/tasks/worktree.ts) — explicit file-collision disturbance and per-task worktree/branch isolation.
- [`lib/server/dashboard-actions.ts`](https://github.com/reflex-agent/reflex-agent/blob/f3b3dd7b438c8333e5731a29023eca81239c7d19/lib/server/dashboard-actions.ts) — project-wide aggregation of active goals, running agents, pending approvals, recent knowledge and suggestions.
- [`app/roots/[id]/_components/dashboard-active-goals.tsx`](https://github.com/reflex-agent/reflex-agent/blob/f3b3dd7b438c8333e5731a29023eca81239c7d19/app/roots/%5Bid%5D/_components/dashboard-active-goals.tsx) — user-facing current commitments/running-work view.
- [`app/roots/[id]/_components/dashboard-pending-approvals.tsx`](https://github.com/reflex-agent/reflex-agent/blob/f3b3dd7b438c8333e5731a29023eca81239c7d19/app/roots/%5Bid%5D/_components/dashboard-pending-approvals.tsx) — cross-topic permission/question/MCP decisions awaiting the user.
- [`lib/server/topic-actions.ts`](https://github.com/reflex-agent/reflex-agent/blob/f3b3dd7b438c8333e5731a29023eca81239c7d19/lib/server/topic-actions.ts) — topic start, stop/delete and goal-abandonment controls.
- [`lib/server/agents/manager.ts`](https://github.com/reflex-agent/reflex-agent/blob/f3b3dd7b438c8333e5731a29023eca81239c7d19/lib/server/agents/manager.ts) and [`app/api/agents/[agentId]/respond/route.ts`](https://github.com/reflex-agent/reflex-agent/blob/f3b3dd7b438c8333e5731a29023eca81239c7d19/app/api/agents/%5BagentId%5D/respond/route.ts) — live permission decisions and return to waiting agent execution.
- [`lib/server/workflows/scheduler.ts`](https://github.com/reflex-agent/reflex-agent/blob/f3b3dd7b438c8333e5731a29023eca81239c7d19/lib/server/workflows/scheduler.ts) — durable per-Space workflow scheduling and system-task execution.
- [`lib/server/workflows/system-tasks.ts`](https://github.com/reflex-agent/reflex-agent/blob/f3b3dd7b438c8333e5731a29023eca81239c7d19/lib/server/workflows/system-tasks.ts) — weekly memory rollup and session indexing, inspected for S4.
- [`lib/server/utilities/audit.ts`](https://github.com/reflex-agent/reflex-agent/blob/f3b3dd7b438c8333e5731a29023eca81239c7d19/lib/server/utilities/audit.ts) — same-path host-API call tracing, inspected for S3*.

## S1 — Operations

- State: A
- Function: model-driven execution of user/project work through persistent Reflex topics, delegated specialist turns, tasks and scheduled/headless runs.
- Disturbance / variety regulated: open-ended user requests, project/file state, tool results, specialist findings, task progress, permissions and workflow-triggered work.
- Decisive decision or feedback right: choose how to pursue the requested outcome within the Reflex topic, including whether/how to delegate specialist work, what returned evidence to synthesize and which first-party action markers to emit.
- Decision owner: autonomous model-driven operating actor running under Reflex's first-party orchestrator protocol.
- Supporting / enforcement mechanisms: persistent topics/events, specialist dispatch protocol, task records, bounded `/goal` continuation, worktree cwd binding, host tools, permissions and headless execution.
- Closure path: model decision → Reflex action/dispatch/tool execution → changed project/task/environment state or child-agent result → observation/reinvocation → subsequent model decision/output.
- Boundary reachability: default interactive topics directly reach the Reflex orchestrator turn; task dispatch and scheduled/headless workflows also reach the same first-party operating path.
- Why this is / is not agent-owned: once an operating turn starts, the model actor has bounded discretion over decomposition/delegation/action and consumes returned results; Reflex supplies and closes that organizational protocol. Claude Code/Codex may execute the model/tool substrate, but no internal metasystem semantics from those external subprocesses are imported.
- Evidence: `lib/reflex/prompts/defaults.ts`; `lib/server/agents/headless.ts`; `lib/server/tasks/dispatch.ts`; topic/goal manager path.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the positive claim is Reflex's first-party operating organization around the model actor, not a claim that Claude Code/Codex internals belong to Reflex.

## S2 — Coordination

- State: C
- Function: attenuate interference between concurrent code-task S1 units that would otherwise mutate the same repository checkout/files.
- Disturbance / variety regulated: concurrent agent tasks operating on one repository can collide through shared file mutations, branch/checkout state and commits.
- Decisive decision or feedback right: choose a disturbance-specific coordination arrangement that separates concurrent code-task mutation lanes before task execution begins.
- Decision owner: Reflex supplies and deterministically enforces the worktree isolation constructor path; no autonomous first-party coordinator owns discretionary S2 policy across competing units.
- Supporting / enforcement mechanisms: unique `task/<slug>` branch/worktree allocation, destination/branch collision checks, worktree-bound task cwd and explicit later merge path.
- Closure path: code task selected → Reflex creates isolated worktree/branch → dispatched task agent is instructed and launched inside that checkout → subsequent file operations/commits occur outside main/shared checkout → later controlled merge reconciles output.
- Why this is / is not agent-owned: the coordination function and closure are first-party, but the decisive isolation policy is deterministic host enforcement rather than an autonomous coordinator that observes competing units and chooses/adjusts coordination policy. This supports `C`, not `A`.
- Evidence: `lib/server/tasks/worktree.ts`; `lib/server/tasks/dispatch.ts`.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: generic multi-agent dispatch, dependency fields and shared task state are not separately counted as S2.
- Distinct S1 units: separate task-bound model/agent executions can concurrently perform code work against the same project repository.
- Inter-S1 disturbance: `tasks/worktree.ts` explicitly states that each code task runs in its own checkout so tasks do not collide on files; a shared checkout would expose one task to another task's mutations/branch state.
- Attenuating coordination relation: Reflex allocates a unique worktree and branch per code task before starting the task agent, thereby separating mutation lanes.
- Feedback into subsequent S1 behaviour: `dispatchTask` binds the agent cwd to the isolated worktree and prompts it to commit there, so later S1 file operations are changed by the coordination decision.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the evidence names a concrete cross-S1 file-collision disturbance and a first-party isolation response whose purpose is to prevent that disturbance, rather than merely routing or delegating work.
- Boundary reachability: standard task dispatch automatically reaches the worktree-isolation path for code tasks in Git repositories.

## S3 — Inside-and-now control

- State: P
- Function: whole-Space current supervision and intervention over ongoing commitments, running agent work and blocked permission decisions.
- Disturbance / variety regulated: simultaneous current commitments, runaway/stale work, blocked agent turns, requested privileges and operational intervention needs across a project Space.
- Decisive decision or feedback right: decide whether current goals/work continue, are stopped/abandoned, and whether requested permissions are allowed or denied.
- Decision owner: legitimate parent user/owner operating the first-party Reflex control surfaces.
- Supporting / enforcement mechanisms: root dashboard aggregation, active-goal/running-agent views, pending-approval aggregation, agent-manager stop path, goal clearing, permission response bridge and explicit task/worktree merge controls.
- Closure path: Reflex surfaces whole-Space current work or a blocked decision → user selects stop/abandon/allow/deny or enters the relevant work item for intervention → Reflex manager/store applies the decision → waiting/running S1 operation changes or terminates.
- Why this is / is not agent-owned: Reflex supplies the whole-Space view and enforces returned interventions, but no autonomous supervisor is established with equivalent authority to reprioritize/stop/authorize work across the Space. The parent user owns the decisive S3 right.
- Evidence: `lib/server/dashboard-actions.ts`; `app/roots/[id]/_components/dashboard-active-goals.tsx`; `app/roots/[id]/_components/dashboard-pending-approvals.tsx`; `lib/server/topic-actions.ts`; `lib/server/agents/manager.ts`; `app/api/agents/[agentId]/respond/route.ts`.
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: local topic decisions and ordinary orchestrator delegation remain S1 activity; they are not promoted to S3 by the `manager` or `dispatcher` names.
- Whole-system current view: the root dashboard aggregates active persistent goals, currently running agents without goals and pending permission/question/MCP interactions across every topic of the Space, giving the parent a cross-operating-unit current view.
- Current-control decision scope: stop/delete running topics, abandon persistent goals, answer blocked questions, allow/deny requested operations and retain explicit control over merging task work into the main repository state.
- Boundary reachability: these are ordinary first-party dashboard/chat/runtime surfaces in the standard distribution, and permission decisions are returned through the live manager to waiting agent execution.

## S3* — Complementary audit

- State: —
- Function: no qualifying complementary independent audit function is established at the declared Reflex Space boundary.
- Disturbance / variety regulated: the review looked for operational claims or conditions that are independently checked through a distinct evidence path rather than merely logged by the same runtime.
- Decisive decision or feedback right: no first-party independent auditor was found that judges discrepancies and returns them into S3 current control.
- Decision owner: none established for qualifying S3*.
- Supporting / enforcement mechanisms: utility audit JSONL, agent event logs, task observation/status and dashboard aggregation provide observability but not the required independent audit relation.
- Closure path: host/API calls can be logged and later viewed, but no distinct ordinary-path claim → complementary reality check → audit judgment → corrective current-control feedback loop is established.
- Why this is / is not agent-owned: the utility audit is emitted by the same host execution path it records; neither it nor event/status presentation establishes an independently judging audit actor.
- Evidence: `lib/server/utilities/audit.ts`; `app/audit/page.tsx`; `lib/server/tasks/observe.ts`; dashboard/event surfaces.
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: auditability/logging is useful evidence infrastructure but is not equivalent to S3* organizational ownership.

### Absence scope

- Surfaces inspected: utility audit writer/reader and audit page, task observation, dashboard status aggregation, agent event logs, runtime/permission paths.
- Plausible first-party paths checked: host-API start/end traces, error/result records, task/topic status, pending-interaction aggregation and user-visible audit inspection.
- Why no material first-party path remains: reviewed paths observe or record the same execution system but do not independently test operational claims against a separate source of reality, make an audit judgment and return findings into current control.

## S4 — Outside-and-then intelligence

- State: —
- Function: no complete first-party outside-and-then environmental intelligence/adaptation loop is established at the pinned revision.
- Disturbance / variety regulated: the review looked for external/future-relevant change that is deliberately sensed, converted into adaptation options, decided upon and returned into current capability/operation.
- Decisive decision or feedback right: no first-party actor is established with a closed right to choose prospective capability adaptation from external/future distinctions and install that choice into subsequent operating repertoire.
- Decision owner: none established for qualifying S4.
- Supporting / enforcement mechanisms: workflow scheduler, headless agent execution, generated utilities, searchable memory, weekly memory rollup and on-demand dashboard AI suggestions can support operation/adaptation but do not establish the required S4 closure themselves.
- Closure path: configured workflows execute and memory/suggestions summarize internal/past/current state, but no evidenced external/future sensing → adaptation option → decision → present capability change → later S1/S3 use loop is closed by the standard distribution.
- Why this is / is not agent-owned: model suggestions and utility generation may be model-driven, but at the pinned revision their evidenced triggers concern current user/project needs and require composition/user action; they do not establish an agent-owned prospective environmental-intelligence loop.
- Evidence: `lib/server/workflows/scheduler.ts`; `lib/server/workflows/system-tasks.ts`; `lib/server/ai-suggestions.ts`; utility generation/update/host surfaces inspected in the pinned tree.
- Basis: structural absence.
- Confidence: medium-high.
- Caveats: downstream user-authored workflows could create an S4 loop, but each such specialization is a separate evidence/boundary question and is not inherited by the standalone repository.

### Absence scope

- Surfaces inspected: workflow scheduler/runner/system tasks, background runtime, AI suggestions, memory rollup/search, utility host/update surfaces and task/orchestrator paths.
- Plausible first-party paths checked: periodic workflow execution, cross-Space memory rollup, on-demand "what's next" suggestions, agent-generated utilities and reusable local state.
- Why no material first-party path remains: these mechanisms execute configured/current work or summarize internal/past state; none establishes the full prospective external sensing, adaptation-decision and returned capability-change loop required for S4.

## S5 — Policy and identity

- State: —
- Function: no qualifying ultimate-policy or system-identity closure is established for the Reflex Space organization.
- Disturbance / variety regulated: the review looked for questions about the Space's ultimate purpose/identity/policy that are distinguished from ordinary operating configuration and permission choices.
- Decisive decision or feedback right: no first-party path identifies such an identity/policy issue, routes it to an actor with explicit ultimate authority and closes the returned decision into subsequent organizational identity.
- Decision owner: none established for qualifying S5.
- Supporting / enforcement mechanisms: prompt templates, model assignments, permission settings, workflow definitions and project settings constrain operation but remain configuration/support surfaces.
- Closure path: users can edit prompts/settings and approve tools, but no evidenced identity issue → ultimate-policy judgment → durable identity update → later organizational behavior loop is established.
- Why this is / is not agent-owned: no autonomous or parent-governed S5 actor/path is established; ordinary owner configuration is not upgraded to S5 merely because it affects behavior.
- Evidence: `lib/reflex/prompts/defaults.ts`; settings/model assignment surfaces; permission response path; workflow/task controls; project dashboard surfaces.
- Basis: structural absence.
- Confidence: high.
- Caveats: a downstream Space may embed identity policy in user-authored prompts/workflows, but that downstream specialization is outside this standalone repository assessment.

### Absence scope

- Surfaces inspected: default prompt/protocol, prompt/settings/model assignment surfaces, permission decisions, workflow/task controls and project dashboard paths.
- Plausible first-party paths checked: editable system prompts, model/harness assignments, always/once permission grants, project controls and scheduled workflow definitions.
- Why no material first-party path remains: reviewed surfaces configure or authorize operation but do not establish a distinct ultimate-policy/identity issue, legitimate S5 authority and returned identity closure at the declared recursion.

## Recursion

A Reflex Space/project is the declared system boundary. Topics and task-bound executions are operating units within that boundary when they perform distinct project work. Claude Code/Codex subprocesses are external agent implementations recruited into those operating paths, not automatically recursive viable systems whose internal S-functions transfer to Reflex. Separate Spaces, external MCP servers and generated utilities require their own boundary-specific evidence before being treated as viable recursive systems.

## Variety and escalation

Reflex attenuates operational variety through persistent topics/tasks, isolated code-task worktrees, bounded goal continuation, workflow schedules and permission gates. It amplifies operational repertoire through delegated specialist roles and utility/workflow execution. Requests exceeding granted authority escalate to explicit user permission/question surfaces; whole-Space current intervention likewise returns to the parent user, supporting `S3=P` without implying S5.

## Evidence gaps

- No autonomous Reflex actor was found with whole-Space reprioritization/current-control rights; S3 therefore remains parent-governed.
- The S2 constructor classification is limited to the evidenced concurrent code-task file-collision path; generic multi-agent dispatch is not independently counted as S2.
- Utility generation and scheduled workflows may support richer adaptation in user-authored deployments, but such downstream compositions are outside this standalone pinned-repository assessment.
- External Claude Code/Codex implementation details were intentionally excluded from Reflex ownership.

## Admission conclusion

Standalone vector at the pinned revision: `A C P — — —`.

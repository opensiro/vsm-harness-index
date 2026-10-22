---
harness_id: chord
project_name: Chord
repository: https://github.com/keakon/chord
review_ref: 2319ec34a2963f57e2f041ff82b1a6272435ee70
reviewed_at: 2026-10-22
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Chord

## Review boundary

- System in focus: the first-party Chord Go terminal/headless coding harness at the frozen revision, not a hosted model, an externally coordinated team, or the Chord development organization.
- Purpose and identity: implement and investigate user coding requests through a model-directed tool loop, project state, sessions, optional roles and delegated coding work.
- Relevant environment: the user's repository and shell, model/provider APIs, local filesystem, model tool results, user permissions, and optional project/global agent configuration.
- Standard-distribution boundary: released `cmd/chord` entrypoints, `internal/agent`, `internal/tools`, `internal/config`, local session/recovery, `internal/worktree`, and documented opt-in role configuration.
- Credited operating / distribution surfaces: default `builder` model/tool loop; optional user-configured SubAgent roles via first-party `delegate`, overlapping write-scope detection, model-facing conflict hint, targeted `notify`/`cancel` and worktree support. The latter is a constructor mode, not enabled standard-builder autonomy.
- Adjacent first-party surfaces excluded from ownership: repository CI, tests, performance benchmark, docs-site build, custom user-written agent prompts/hooks, external MCP services, model/provider internals, and the maintainer's release/governance actions.
- First-party operating / deployment modes considered: interactive TUI, headless, default `builder`/`planner` roles, user-enabled subagent definitions and permission overrides, optional long-task loop, model fallback, project memory and worktrees.
- Recursion level: one locally operated coding session with possible delegated coding S1 units; not the Open Source project as a governing organization or separate terminal sessions run by an external team.
- Reviewed revision: [`keakon/chord@2319ec34a2963f57e2f041ff82b1a6272435ee70`](https://github.com/keakon/chord/tree/2319ec34a2963f57e2f041ff82b1a6272435ee70), frozen in Index intake #200.
- Observation date: 2026-10-22; source-only inspection, no provider-backed agent execution.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

Chord's MainAgent assembles LLM requests with conversation, project state and available tool declarations. It accepts model-selected tool calls, executes them through a permission-aware pipeline, commits tool results to the conversation, and starts subsequent requests. A terminal UI and headless interface expose the same agent runtime. Sessions, context compaction, background jobs, optional cross-session project memory and provider/model fallback preserve or recover coding work.

The built-in `builder` and `planner` are **main-mode** roles; `builder` explicitly denies `delegate` and `handoff` by default. No built-in SubAgent role is installed. A user can configure `mode: subagent` roles and override relevant permission rules. In that opt-in mode `delegate` creates independently running model/tool workers, declares expected write scopes, and returns asynchronous durable handles. The first-party task registry detects concrete overlapping write scopes between active writer tasks and annotates the newly started handle with `scope_conflict`, another task ID and `serialize_or_worktree` advice. The parent can issue a targeted `notify` correction, cancel a task or move work to distinct worktrees. Crucially, these scopes are **advisory**: they do not enforce write isolation and the second writer is not automatically serialized.

The runtime also implements limits for concurrent agent slots and LLM requests, leases, stall warnings and resumed task mailboxes. These are mechanisms for safe task processing. The analyzed source does not show a separate, established whole-current resource/commitment governance function, independent complementary management audit, external-and-future adaptive capability loop, or ultimate-policy decision owner with returned identity-level closure.

Primary evidence: [main model/tool handler](https://github.com/keakon/chord/blob/2319ec34a2963f57e2f041ff82b1a6272435ee70/internal/agent/main_handlers_llm.go), [tool-result loop](https://github.com/keakon/chord/blob/2319ec34a2963f57e2f041ff82b1a6272435ee70/internal/agent/main_handlers_tools.go), [built-in role definitions](https://github.com/keakon/chord/blob/2319ec34a2963f57e2f041ff82b1a6272435ee70/internal/config/agent.go#L394-L485), [role opt-in](https://github.com/keakon/chord/blob/2319ec34a2963f57e2f041ff82b1a6272435ee70/docs/configuration.md#L1159-L1214), [overlap signal](https://github.com/keakon/chord/blob/2319ec34a2963f57e2f041ff82b1a6272435ee70/internal/agent/main_subagent.go#L260-L279).

## Operational model

Default Chord has a model-owned coding S1: read/inspect/edit/shell decisions are selected in response to the live task and observed tool outputs, with human tool permission constraints. In the opt-in distributed construction, each delegated worker also runs its own model/tool decisions on a task, while the MainAgent owns task selection and sees delivered result/status messages. Collision-specific writer coordination has a supplied detection and response interface but requires the operator/developer to install compatible roles and authorize delegation. Developer configuration supplies the agents and permissions; the installed runtime provides the conflict-specific feedback primitive, not a proven default autonomous S2 loop.

## S1 — Operations

- State: A
- Function: Solve a coding request by autonomous, feedback-conditioned selection of project/tool actions and edits.
- Disturbance / variety regulated: Unfamiliar code, changing user requirements, errors from tools or providers, and incomplete implementation/test outcomes.
- Decisive decision or feedback right: The model chooses the next file, shell or other tool action and revises work after receiving execution output.
- Decision owner: the first-party MainAgent's selected model; optional configured subagents also own their task-local choices.
- Supporting / enforcement mechanisms: tool executor, permissions, provider adapter, context reduction, session persistence, shell jobs and user approval gates.
- Closure path: user goal → model tool call → permission and tool execution → recorded output or denial → next model request/coding decision.
- Boundary reachability: the default built-in `builder` role uses the MainAgent model/tool loop without requiring a custom subagent or development-only actor.
- Why this is / is not agent-owned: coding tool selection and feedback response are discretionary model actions, while user policy restricts permitted side effects.
- Evidence: [model response classifies executable tool calls](https://github.com/keakon/chord/blob/2319ec34a2963f57e2f041ff82b1a6272435ee70/internal/agent/main_handlers_llm.go#L223-L273), [permission-aware tool dispatch](https://github.com/keakon/chord/blob/2319ec34a2963f57e2f041ff82b1a6272435ee70/internal/agent/main_tool_exec.go#L58-L112), [tool result enters context](https://github.com/keakon/chord/blob/2319ec34a2963f57e2f041ff82b1a6272435ee70/internal/agent/main_handlers_tools.go#L482-L588), [default builder](https://github.com/keakon/chord/blob/2319ec34a2963f57e2f041ff82b1a6272435ee70/internal/config/agent.go#L459-L485).
- Basis: structural.
- Confidence: high for reachable model/tool loop, not a claim of measured task success.
- Caveats: no live model/provider task was run; permission denials can prevent individual actions.

## S2 — Coordination

- State: C
- Function: Dampen concurrent coding-writer interference by detecting overlap between distinct delegated S1 work scopes and exposing a corrective coordination path to the task owner.
- Disturbance / variety regulated: two concurrently active writer subagents proposing modifications to the same file/path/module and potentially overwriting one another's work.
- Distinct S1 units: independently model-running delegated writer tasks under one MainAgent, available only after suitable subagent roles and delegation permissions are configured.
- Inter-S1 disturbance: overlap of nonterminal writers' declared `expected_write_scope` paths, checked against current sibling task records rather than conjectured from generic messaging.
- Attenuating coordination relation: registry computes a specific write-scope conflict and returns `scope_conflict`, `suggested_task_id` and `serialize_or_worktree` advice to the delegating agent; targeted `notify` and `cancel` are first-party response controls.
- Feedback into subsequent S1 behaviour: a composed owner may notify the named worker to defer/re-scope a conflicting edit, cancel a redundant worker or separate worktrees, changing the affected worker's subsequent execution. This path is supported but no default automatic response or successful conflict-settlement trace is claimed.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: an explicit structural *write collision* among separate writer tasks selects the conflict-specific message and corrective target, not merely the existence of `delegate` or a mailbox.
- Decisive decision or feedback right: select a collision-specific response to the flagged overlap; the runtime produces evidence/advice while a configured owner agent must choose and send the correction.
- Decision owner: constructor path for a future configured model owner; default builder denies `delegate`, so the autonomous response is not installed as a default operating closure.
- Supporting / enforcement mechanisms: scope normalization/overlap matching, task registry, durable handles, targeted notification/cancellation, separate git worktree capability and role permission rules.
- Closure path: competing writer scope declarations → exact overlap signal in started task handle → owner selects `notify`/cancel/separation → affected S1 receives a different instruction or ceases writing. This requires an opt-in role and owner policy composition.
- Boundary reachability: the S2-specific overlap computation and corrective tools ship inside the Chord binary and are exposed by documented custom `mode: subagent` roles; their availability requires explicit configuration, making this `C` rather than an automatic `A` in the standard builder mode.
- Why this is / is not agent-owned: the standard runtime does not choose or enforce the resolution; in a composed mode a model can own that choice. Collision reporting alone is not counted as agent-owned S2.
- Evidence: [write-scope contract and handle](https://github.com/keakon/chord/blob/2319ec34a2963f57e2f041ff82b1a6272435ee70/internal/tools/task.go#L17-L115), [path overlap detection](https://github.com/keakon/chord/blob/2319ec34a2963f57e2f041ff82b1a6272435ee70/internal/agent/task_registry.go#L375-L415), [explicit conflict advice](https://github.com/keakon/chord/blob/2319ec34a2963f57e2f041ff82b1a6272435ee70/internal/agent/main_subagent.go#L260-L279), [advisory-only decision](https://github.com/keakon/chord/blob/2319ec34a2963f57e2f041ff82b1a6272435ee70/internal/agent/main_subagent.go#L984-L1050), [notification](https://github.com/keakon/chord/blob/2319ec34a2963f57e2f041ff82b1a6272435ee70/internal/tools/notify.go#L17-L102), [default opt-in restriction](https://github.com/keakon/chord/blob/2319ec34a2963f57e2f041ff82b1a6272435ee70/docs/configuration.md#L1159-L1214).
- Basis: structural.
- Confidence: medium for the S2-specific constructor; high that it is non-default and advisory.
- Caveats: scopes are declarations, not confinement; two writers still launch on an overlap, and model-mediated correction was not dynamically exercised. If the constructor threshold requires a fully installed autonomous response rather than a first-party function-specific response interface, the S2 grade should be revisited rather than silently promoted to `A`.

## S3 — Inside-and-now control

- State: —
- Function: Regulate current shared resources, commitments, accountability and cross-unit priorities on behalf of the whole coding organization.
- Disturbance / variety regulated: concurrent worker slots, LLM rate limits, stalled tasks, budgets and changing code-task commitments.
- Decisive decision or feedback right: none established for an S3-specific current-control function. The model can delegate/retry/cancel individual tasks, while configuration-defined runtime caps and leases enforce preselected limits.
- Decision owner: default S1 owner and human-configured resource policy; no distinct demonstrated S3 whole-current decision right.
- Supporting / enforcement mechanisms: `resourceGovernor`, per-provider/model concurrency counters, stall/coordination snapshots, task progress views and cancellation.
- Closure path: task/slot status → deterministic admission, queue or refusal; owner may revise a coding plan. No evidenced cross-unit current-resource bargaining or discretionary system-wide intervention beyond ordinary task orchestration.
- Why this is / is not agent-owned: observing several tasks and enforcing configured caps does not transfer control of those caps or a whole-current priority decision to a dedicated autonomous S3 owner.
- Evidence: [resource policy and runtime slots](https://github.com/keakon/chord/blob/2319ec34a2963f57e2f041ff82b1a6272435ee70/internal/agent/resource_governor.go#L18-L186), [task-state overlay](https://github.com/keakon/chord/blob/2319ec34a2963f57e2f041ff82b1a6272435ee70/internal/agent/coordination_snapshot.go#L95-L237), [delegation prompt](https://github.com/keakon/chord/blob/2319ec34a2963f57e2f041ff82b1a6272435ee70/internal/agent/prompt_coordination.go#L18-L82).
- Basis: structural.
- Confidence: medium-high for bounded absence.
- Caveats: a user-composed multiagent organization may add real S3 rights; it is not automatically part of this harness.

### Absence scope

- Surfaces inspected: resource governor, task registry, coordination overlays, delegation instructions, terminal task controls, headless and loop modes.
- Plausible first-party paths checked: shared budget/priority negotiation, stalled-task interventions, concurrent model-call admission, operator controls and adaptive whole-current commitment reallocation.
- Why no material first-party path remains: fixed developer/operator limits, task statuses and task-local owner corrections do not embody a separately established whole-current resource/commitment decision and returned regulation.

## S3* — Complementary audit

- State: —
- Function: Challenge an S3 management claim through complementary, sufficiently independent operational evidence and return findings to current control.
- Disturbance / variety regulated: inaccurate task completion or code-review claims, file changes not captured by summaries and misleading current status.
- Decisive decision or feedback right: none shown for an audit of whole-current S3 management. A custom reviewer role, diagnostic hooks and task reports can inspect code but are not packaged as independent S3 audit adjudicators.
- Decision owner: coding model/user for local quality checks; no separate complementary-audit judgment owner.
- Supporting / enforcement mechanisms: child task summaries, file-change evidence, tool trace, hooks, LSP and user-configured reviewer prompts.
- Closure path: optional code inspection or verification → feedback to coding work; no S3 operating claim → independently governed direct-evidence audit → S3 corrective return.
- Why this is / is not agent-owned: a reviewer label or ordinary task QA does not establish independent managerial challenge or corrective authority.
- Evidence: [optional user-defined roles](https://github.com/keakon/chord/blob/2319ec34a2963f57e2f041ff82b1a6272435ee70/docs/customization.md#L25-L42), [built-in main roles](https://github.com/keakon/chord/blob/2319ec34a2963f57e2f041ff82b1a6272435ee70/internal/config/agent.go#L394-L485), [task reporting fields](https://github.com/keakon/chord/blob/2319ec34a2963f57e2f041ff82b1a6272435ee70/internal/agent/coordination_snapshot.go#L125-L220).
- Basis: structural.
- Confidence: medium-high.
- Caveats: optional independent external auditing remains possible but was not evidenced as an installed first-party operating mode.

### Absence scope

- Surfaces inspected: shipped role roster, custom reviewer configuration, subagent reporting, coordination overlays, hooks, LSP, tests and tool feedback.
- Plausible first-party paths checked: independent raw-evidence challenge to S3 decisions, reviewer-specific audit authority, independent replay and an S3 corrective-return mechanism.
- Why no material first-party path remains: no qualifying S3 management claim and no first-party, independently governed complementary audit mode and return path are established.

## S4 — Outside-and-then intelligence

- State: —
- Function: Sense relevant external/future changes, form adaptation options and return them to current organizational capability.
- Disturbance / variety regulated: model-provider reliability, changing tools/user preferences and prospective project conditions.
- Decisive decision or feedback right: no supported external-prospective capability adaptation decision. Model fallback responds to current provider error; memory learns historical session preferences; model-selected web research is task-local.
- Decision owner: human selects provider/roles/skills and project policies; model chooses coding-task tools, not a standing external-future strategy.
- Supporting / enforcement mechanisms: provider fallback, optional project memory extraction, model pools, skills, web tools, session compaction and hooks.
- Closure path: provider failure → configured fallback / session transcript → next coding step, or remembered project fact → future prompt context; neither is a first-party outside-and-then strategy/options return to S3.
- Why this is / is not agent-owned: immediate reliability response and historic-context retention are not prospective adaptation authority.
- Evidence: [project memory contract](https://github.com/keakon/chord/blob/2319ec34a2963f57e2f041ff82b1a6272435ee70/docs/project-memory.md#L1-L55), [provider fallback and context documentation](https://github.com/keakon/chord/blob/2319ec34a2963f57e2f041ff82b1a6272435ee70/README.md#L24-L32), [model pool configuration](https://github.com/keakon/chord/blob/2319ec34a2963f57e2f041ff82b1a6272435ee70/docs/configuration.md).
- Basis: structural.
- Confidence: medium-high.
- Caveats: a user can direct research about future changes, but this does not install a recurring S4 decision/feedback function.

### Absence scope

- Surfaces inspected: provider fallback, model pools, memory capture/retention, custom roles, skill loading, web fetch, hooks and loop mode.
- Plausible first-party paths checked: future-environment sensing, independent option generation, durable capability adoption and S3/S4 conversation.
- Why no material first-party path remains: mechanisms improve present-session operation and preserve preferences, without a shipped externally prospective adaptation choice and returned change in system capability.

## S5 — Policy and identity

- State: —
- Function: Legitimately settle ultimate identity, ethos and policy for the assessed running coding organization and govern later operation.
- Disturbance / variety regulated: user-versus-agent authority, risky commands, untrusted content and proposed permission changes.
- Decisive decision or feedback right: operator owns accepted goals and permission rules; the runtime asks/allows/denies tool use but no identity-level dispute reaches an established parent decision route and returns as supreme policy.
- Decision owner: human operator for instructions and access; permission engine for deterministic enforcement, not autonomous S5 organizational authority.
- Supporting / enforcement mechanisms: allow/ask/deny rules, project/global agent configuration, user confirmation, role prompts, YOLO toggle and hooks.
- Closure path: user-selected policy → configured tool gate → permitted or denied coding action, not an identity-level matter → legitimate parent adjudication → new binding operating policy.
- Why this is / is not agent-owned: the coding model does not own supreme values; routine operator permissions are not a parent S5 loop.
- Evidence: [permission mechanics](https://github.com/keakon/chord/blob/2319ec34a2963f57e2f041ff82b1a6272435ee70/docs/permissions-and-safety.md#L11-L85), [default role gates](https://github.com/keakon/chord/blob/2319ec34a2963f57e2f041ff82b1a6272435ee70/internal/config/agent.go#L459-L485), [permission execution split](https://github.com/keakon/chord/blob/2319ec34a2963f57e2f041ff82b1a6272435ee70/internal/agent/main_tool_exec.go#L58-L112).
- Basis: structural.
- Confidence: medium-high.
- Caveats: external project governance and maintainer release policy are adjacent and cannot be borrowed as runtime S5.

### Absence scope

- Surfaces inspected: rule files, role permissions, confirmation, workflow mode switch, instructions, session state and contribution governance boundary.
- Plausible first-party paths checked: owner/parent ultimate-purpose decision, policy conflict adjudication, authoritative policy return, runtime identity change and enforced subsequent operation.
- Why no material first-party path remains: the checked paths constrain ordinary coding execution but do not create a first-party identity-level discretionary decision-and-return function.

## Distributed OSS parent arrangement

The repository's maintainers and contributors govern the software project, but their release, issue and CI decisions are not installed as S3/S4/S5 rights within the local coding harness. Independent operators' custom roles or sessions similarly do not become a shared project-recursion organization by repository co-location.

## Self-hosted and non-human modes

Chord can run against user-selected model providers in a local terminal or headless client. The supported default mode leaves delegation unavailable. Users can add models, agent roles, permission policies and worktree usage; the S2-specific overlap constructor is credited only at that opt-in operating boundary and no `A(P)` / `C(P)` / `P` parent-governed S3–S5 mode is inferred from ordinary confirmation controls.

## Recursion

Configured SubAgents have separate model/tool choices and task handles, but nested delegation and owner tree persistence alone do not prove each subordinate contains a recursively viable metasystem. The assessed recursion remains one coding session and its possible operational coding cells.

## Variety and escalation

Tool feedback, subagent task results, stall alerts, and advisory write-scope collision hints expose task-related variety. The specific S2 constructor preserves both the conflicting task identity and relevant path declaration; generic progress alerts, resource caps and user confirmation do not by themselves establish algedonic signalling or higher S-functions. Requests beyond an agent's permissions reach the human operator without reclassifying every approval as S5.

## Evidence gaps

- Frozen-source inspection only; no LLM-agent work, provider-backed test, real concurrent writer collision or end-to-end opt-in conflict correction was executed.
- Chord's Go test suite could not be run in this environment because Go is not installed. The repository's source and tests describe conflict flags, but they do not attest model-selected settlements.
- S2 is a deliberately bounded `C` candidate, not a default autonomous `A`; further semantic review could require a narrower constructor interpretation.
- User-authored role/hook configurations and external supervisory organizations can create additional modes, but their decisions were not counted as shipped first-party closure.

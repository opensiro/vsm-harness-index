---
harness_id: velloc-runtime
project_name: Velloc Runtime
repository: https://github.com/VellocLabs/velloc-runtime
review_ref: 28bccb9a03b696efc1890c4b12cb1366646d975c
reviewed_at: 2026-11-02
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

# Velloc Runtime

## Review boundary

- System in focus: A host-granted Velloc coding runtime installation and its supported first-party agent/team/skill modes.
- Purpose and identity: Stateful TypeScript model/tool coding runtime with permissions, sessions, subagents, long-lived teams and optional bundled workflows.
- Relevant environment: User programming requests, repository changes, model providers, filesystem/terminal results, teammate reports, task-board state and security restrictions.
- Standard-distribution boundary: First-party runtime served inside the Velloc host, including bundled default/optional stock skills, supported team feature gate and first-party worker/session protocols; third-party plugin and host internals excluded.
- Credited operating / distribution surfaces: `src/engine`, `toolkit`, `agents`, `team`, `skillLibrary/builtin`, `memory`, `browser` session workers and permission layers.
- Adjacent first-party surfaces excluded from ownership: Plugin-authored external skills and remote model service internals, developer unit/e2e tests, release packaging and vendor corporate governance.
- First-party operating / deployment modes considered: Normal coding session, background subagent/worktree mode, explicitly activated `agent-teams` skill, bundled `simplify`, `batch`, `safe-team`, and optional scheduled/memory maintenance.
- Recursion level: One configured coding task/team with a lead and child sessions; host OS and other unrelated app sessions are outside this task-level recursion.
- Reviewed revision: `28bccb9a03b696efc1890c4b12cb1366646d975c`.
- Observation date: 2026-11-02.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

One shared runtime manager owns a session registry and a separate worker/engine per session. `turnLoop`/interpreter separate pure step transitions from host-granted model calls, effects and tool execution. The native `Agent` route spawns isolated specialist or forked runs; the gated first-party `agent-teams` mode provides persistent teammates, per-team mailboxes, a durable owner/dependency-aware task board and model-visible task/message tools. Bundled stock skills are installed by `installStockSkills()` and exposed through supported invocation modes: `batch` isolates writers in git worktrees, `simplify` dispatches three read-only perspectives to fresh agents and brings findings back to the author, and `safe-team` separates untrusted implementation from a trusted lead's acceptance/security review. These are conditional supported modes, not unconditional behavior of every new chat.

## Operational model

The runtime's model actor chooses task actions. In team/stock-skill modes the lead model allocates and revises shared work, applies isolation to prevent cross-worker write interference, evaluates teammate progress and integrates evidence. A separate review mode compares the code diff against multiple independent reviewer perspectives and returns findings to the author for correction. Static host permissions, provider-trust settings and operator configuration constrain these workflows; routine memory extraction alone is not strategic S4, nor does the installation establish ultimate S5 authority.

## S1 — Operations

- State: A
- Function: Execute coding/user tasks by selecting tools, editing artifacts and reacting to tool, model and delegated results.
- Disturbance / variety regulated: Changing source state, task ambiguity, model/tool errors, missing context, time and token budgets.
- Decisive decision or feedback right: Choose action/tool, agent delegation, implementation revision or final result.
- Decision owner: Active session model; child or teammate models own their bounded delegated task actions.
- Supporting / enforcement mechanisms: Turn reducer/interpreter, tool contracts, permission gates, model drivers, session ledger, contexts and host capabilities.
- Closure path: Conversation and repository context → model request → tool/subagent decision → executed effect and observation → next turn or output.
- Boundary reachability: The host loads the first-party runtime, whose session worker invokes the bundled engine; named built-in Explore, Plan and general-purpose agent routes are compiled into the shipped tool catalog.
- Why this is / is not agent-owned: Model-generated coding and tool decisions respond to execution feedback; the deterministic engine only transports and enforces permissions.
- Evidence: [runtime overview](https://github.com/VellocLabs/velloc-runtime/blob/28bccb9a03b696efc1890c4b12cb1366646d975c/README.md), [turn engine](https://github.com/VellocLabs/velloc-runtime/blob/28bccb9a03b696efc1890c4b12cb1366646d975c/src/engine/turnLoop.ts), [built-in agents](https://github.com/VellocLabs/velloc-runtime/blob/28bccb9a03b696efc1890c4b12cb1366646d975c/src/agents/builtInAgents.ts), [tool registry](https://github.com/VellocLabs/velloc-runtime/blob/28bccb9a03b696efc1890c4b12cb1366646d975c/src/toolkit/toolRegistry.ts).
- Basis: structural.
- Confidence: high.
- Caveats: Frozen source inspection only; no live host/model session was executed by this assessment.

## S2 — Coordination

- State: A
- Function: Attenuate collisions and incompatible sequencing between concurrently working code agents.
- Disturbance / variety regulated: Multiple workers changing overlapping files or acting before prerequisites complete, stale tasks and ambiguous ownership.
- Decisive decision or feedback right: Split nonoverlapping scopes, assign/claim dependency-unblocked tasks, isolate writable worktrees and return conflicts for revised allocation.
- Decision owner: Team lead model following first-party `agent-teams`/`batch` protocols, with teammates updating board ownership and completion.
- Supporting / enforcement mechanisms: `TaskCreate`/`TaskUpdate`/`TaskList`, `SendMessage`, task `blocks`/`blockedBy`, long-lived teammates, worktree isolation and per-member locks/IDs.
- Closure path: Lead defines slices/dependencies → owner claims eligible work → agents execute in allocated locations → board/reports expose blocked/completed or overlapping work → lead updates assignment or integration plan.
- Boundary reachability: The shipped `agent-teams` hosted skill unlocks team tools, while the bundled `/batch` skill is registered by the default stock-skill installer for compatible sessions; neither requires a third-party coordinator.
- Why this is / is not agent-owned: The lead and members select scope and assignments using live shared task state. The registry stores decisions but does not autonomously decide them.
- Distinct S1 units: Lead and separately running teammate/Agent worker models, each executing independent assigned code work in its own session/worktree.
- Inter-S1 disturbance: Concurrent writers can collide in the same source tree; a teammate may take work blocked by another; unowned or stale tasks create duplicated work.
- Attenuating coordination relation: Shared owner/dependency board plus scoped worktree assignment and lead instruction to avoid overlapping slices; one worker claims eligible unblocked tasks, others take a different unit.
- Feedback into subsequent S1 behaviour: Task completion, ownership and blockers are returned through TaskList and mailbox reports, allowing the lead/teammates to claim the next unblocked job or revise work assignments.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: It actively regulates conflicting edit scope and work eligibility between multiple independently acting S1 units, using ownership and isolated write locations with returned task-status feedback.
- Evidence: [agent teams instruction and gate](https://github.com/VellocLabs/velloc-runtime/blob/28bccb9a03b696efc1890c4b12cb1366646d975c/src/toolkit/builtin/team/agentTeamsSkill.ts), [team board state](https://github.com/VellocLabs/velloc-runtime/blob/28bccb9a03b696efc1890c4b12cb1366646d975c/src/team/TeamRegistry.ts), [model-facing task tools](https://github.com/VellocLabs/velloc-runtime/blob/28bccb9a03b696efc1890c4b12cb1366646d975c/src/toolkit/builtin/teamTools.ts), [worktree-based batch](https://github.com/VellocLabs/velloc-runtime/blob/28bccb9a03b696efc1890c4b12cb1366646d975c/src/skillLibrary/builtin/batchSkill.ts).
- Basis: structural and explicit.
- Confidence: medium.
- Caveats: S2 is credited to user-activated team/stock-skill modes; no implicit inter-session management across every Velloc chat is asserted.

## S3 — Inside-and-now control

- State: A
- Function: Regulate current multi-worker commitment, execution progress and integration against the common coding goal.
- Disturbance / variety regulated: Worker failure, unowned or blocked tasks, results that fail validation, privilege exposure and integration readiness.
- Decisive decision or feedback right: Lead chooses next assignments, requests fixes, halts unsafe work and accepts/integrates results based on task-board and current artifact evidence.
- Decision owner: Team lead model in bundled team/batch/safe-team modes, distinct from delegated implementation models.
- Supporting / enforcement mechanisms: Team roster, mutable task board, automatic final-report/message turns, `Shutdown`, host tool permission gates, stable candidate snapshots and lead-owned validation.
- Closure path: Team's live task/output state → lead assesses current readiness/security → changes assignments, requests corrections or stops the worker → updated work state returns for acceptance.
- Boundary reachability: `agent-teams` exposes tools for lead and worker progress updates; bundled `/safe-team` instructs a trusted lead to review a frozen candidate and route actual validation failures back to teammates.
- Why this is / is not agent-owned: The whole-task lead exercises discretionary management on a multi-worker whole rather than merely following a fixed per-tool policy.
- Whole-system current view: The lead reads the team's complete task list, owners/dependencies, teammate status and current candidate artifacts/validation output.
- Current-control decision scope: The lead can adjust assignments/priorities, request fresh fixes, stop unsafe writers, hold integration and authorize acceptance of the reviewed result for the current team task.
- Evidence: [team skill](https://github.com/VellocLabs/velloc-runtime/blob/28bccb9a03b696efc1890c4b12cb1366646d975c/src/toolkit/builtin/team/agentTeamsSkill.ts), [task/teammate tools](https://github.com/VellocLabs/velloc-runtime/blob/28bccb9a03b696efc1890c4b12cb1366646d975c/src/toolkit/builtin/teamTools.ts), [safe-team current management](https://github.com/VellocLabs/velloc-runtime/blob/28bccb9a03b696efc1890c4b12cb1366646d975c/src/skillLibrary/builtin/safeTeam.ts), [teammate reporting](https://github.com/VellocLabs/velloc-runtime/blob/28bccb9a03b696efc1890c4b12cb1366646d975c/src/team/teammateBrief.ts).
- Basis: structural and explicit.
- Confidence: medium.
- Caveats: This is conditional team-level S3, not evidence of central capacity management across all installed users/sessions or proof of real-world success.

## S3* — Complementary audit

- State: A
- Function: Independently examine a code change for actual defects and return findings for author repair.
- Disturbance / variety regulated: Developer self-confirmation, missed reuse/design/performance defects and unsafe changes from untrusted workers.
- Decisive decision or feedback right: Fresh reviewer agents report specific file/line faults; the author/lead triages and fixes or rejects them based on observed code.
- Decision owner: Three separately spawned review-model actors in bundled `simplify` mode; in `safe-team` a trusted lead retains independent snapshot/security acceptance rights.
- Supporting / enforcement mechanisms: Captured `git diff`, independent reviewer briefs for reuse/design/performance, read-only reviewer roles, source-level findings, corrections and stable-snapshot inspection.
- Closure path: Author's changed diff → separately briefed reviewer agents inspect raw code/neighbours → file/line findings → author merges/deduplicates and edits fixes → resulting artifact is returned to normal task validation.
- Boundary reachability: `installStockSkills` registers `simplify` by default for compatible agent/code sessions with the native `Agent` tool; team-only `safe-team` is another shipped optional complementary path.
- Why this is / is not agent-owned: Review models independently examine the current diff and issue discretionary findings, not merely restate the author's report or run deterministic tests.
- Claim being audited: Change quality and safety against the task and existing project code.
- Ordinary reporting path: The implementing model's changes and own summary.
- Complementary access path: Fresh reviewers read raw git diff and surrounding repository implementation, with distinct review briefs.
- Independence boundary: Separate spawned reviewer model sessions/roles from author execution; same underlying provider may be used; no independent institutional auditor claimed.
- Who acts on findings: Original author model fixes findings, drops unsupported ones with reasons, and validates the result; trusted lead approves or halts untrusted code acceptance in safe-team mode.
- Evidence: [bundled simplify review loop](https://github.com/VellocLabs/velloc-runtime/blob/28bccb9a03b696efc1890c4b12cb1366646d975c/src/skillLibrary/builtin/simplifySkill.ts), [stock skill wiring](https://github.com/VellocLabs/velloc-runtime/blob/28bccb9a03b696efc1890c4b12cb1366646d975c/src/skillLibrary/builtin/catalog.ts), [safe-team independent check](https://github.com/VellocLabs/velloc-runtime/blob/28bccb9a03b696efc1890c4b12cb1366646d975c/src/skillLibrary/builtin/safeTeam.ts), [native agent dispatch](https://github.com/VellocLabs/velloc-runtime/blob/28bccb9a03b696efc1890c4b12cb1366646d975c/src/toolkit/builtin/subagentLaunch.ts).
- Basis: explicit and structural.
- Confidence: medium.
- Caveats: User-invoked or model-invoked skill mode, not mandatory audit of every change; review accuracy or an enforced second audit round is not asserted.

## S4 — Outside-and-then intelligence

- State: —
- Function: No organization-level outside/future intelligence and capability adaptation loop demonstrated.
- Disturbance / variety regulated: Evolving external technology and future organizational fitness demands.
- Decisive decision or feedback right: No separately established prospective option authority; user or developer installs plugins and selects models.
- Decision owner: No qualifying S4 agent identified.
- Supporting / enforcement mechanisms: Scheduled routines, cross-session memory extraction/consolidation, model profile switching, extension/plugin marketplaces and developer-facing updating tools.
- Closure path: Memory can be recalled and routines scheduled; no clearly owned external-future sensing → strategic option → implemented capability-change loop is returned to the task system.
- Why this is / is not agent-owned: Reorganizing prior session notes and user-configured provider changes support continuity and current tasks, not prospective environment-driven adaptation on their own.
- Evidence: [memory consolidation](https://github.com/VellocLabs/velloc-runtime/blob/28bccb9a03b696efc1890c4b12cb1366646d975c/src/memory/consolidate/consolidationRunner.ts), [routine scheduler](https://github.com/VellocLabs/velloc-runtime/blob/28bccb9a03b696efc1890c4b12cb1366646d975c/src/routines/RoutineScheduler.ts), [runtime overview](https://github.com/VellocLabs/velloc-runtime/blob/28bccb9a03b696efc1890c4b12cb1366646d975c/README.md).
- Basis: structural.
- Confidence: medium.
- Caveats: A user-written task could ask an agent to research future plans, but that is not a separately shipped governance mode.

### Absence scope

- Surfaces inspected: Cross-session memory extraction/consolidation, routine triggering, plugin/model settings and stock-skill catalog.
- Plausible first-party paths checked: Automatic memory hygiene, recurring agents, provider switches, plugin catalog updates and read-only planning agent.
- Why no material first-party path remains: Neither prospective external sensing nor selected future capability revision is tied to a first-party organization-level adaptation closure.

## S5 — Policy and identity

- State: —
- Function: No ultimate identity/legitimacy dispute arbitration and governing return established.
- Disturbance / variety regulated: Conflicting ultimate goals, authority claims and definition of permissible system identity.
- Decisive decision or feedback right: No governing S5 final decision process observed within the runtime boundary.
- Decision owner: Operator/host chooses capabilities, model trust and permissions; team lead controls task security, not ultimate constitutional authority.
- Supporting / enforcement mechanisms: Host-granted versioned capabilities, permission modes, protected paths, managed-over-user mod tiers and provider trust settings.
- Closure path: Static operator policy is enforced by permission checks; no identity dispute is escalated to final authority and returned as a redefined governing policy.
- Why this is / is not agent-owned: `safe-team` is security/current-work supervision; an app-level permission envelope and developer governance are not an operational S5 function by mere presence.
- Evidence: [runtime capability boundary](https://github.com/VellocLabs/velloc-runtime/blob/28bccb9a03b696efc1890c4b12cb1366646d975c/README.md), [safe-team](https://github.com/VellocLabs/velloc-runtime/blob/28bccb9a03b696efc1890c4b12cb1366646d975c/src/skillLibrary/builtin/safeTeam.ts), [team provider trust](https://github.com/VellocLabs/velloc-runtime/blob/28bccb9a03b696efc1890c4b12cb1366646d975c/src/team/providerCatalog.ts).
- Basis: structural.
- Confidence: medium.
- Caveats: No parent organizational constitution or owner-level ultimate-policy decision should be inferred from default safety settings.

### Absence scope

- Surfaces inspected: Capability host boundary, permission/tool layers, managed/user mod precedence, team trust rules and stock-skill governance wording.
- Plausible first-party paths checked: Human approvals, plan mode, provider trust declarations, trusted lead review and static policy hook precedence.
- Why no material first-party path remains: These authorize concrete tools/workflows, not ultimate identity adjudication through a distinct legitimate S5 decider and return channel.

## Distributed OSS parent arrangement

The runtime is distributed as a component loaded by the Velloc host. Corporate maintainers, external providers and host OS controls are outside the task-level VSM parent. Managed mod priority is a runtime rule, not an autonomous S5 board.

## Self-hosted and non-human modes

Multiple model driver backends and a URL-loaded runtime do not donate their providers' internal decisions. Long-lived headless routines instantiate ordinary task actors; they do not make the manager S4 automatically.

## Recursion

Activated team mode has lead/teammate operational recursion with task board S2 and lead S3. Optional fresh reviewer workflows supply complementary S3* at the same task-team level. The host process manager and passive UI subscriptions are not independently autonomous VSM owners.

## Variety and escalation

Permissions can deny unsafe tools, while task results and mailbox reports are routed to the lead for corrective allocation. In safe-team mode, untrusted agents cannot authorize privilege escalation and the trusted lead reviews a stable snapshot before acceptance. Human provider/model selection remains external authority, not automatic S5.

## Evidence gaps

The assessment establishes source and shipped-invocation reachability, not observed multi-agent performance, review correctness or live integration with the Windows host. Optional features require appropriate session type and explicit activation; no third-party plugin is assumed installed.

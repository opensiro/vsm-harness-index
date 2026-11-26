---
harness_id: orca-stablyai
project_name: Orca
repository: https://github.com/stablyai/orca
review_ref: 4ea5e5a090f97563008d5ebb85ce3ccdf5561d71
reviewed_at: 2026-11-25
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
assessment_changed_at: 2026-11-25
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: P
---

# Orca

## Review boundary

- System in focus: Orca's supported desktop/CLI and host runtime organizing workers, Run coordinators and configured bot-managed work fleets.
- Purpose and identity: Supervise autonomous coding and review work and return outcomes to the operator.
- Relevant environment: Local and supported paired hosts, worktrees and SSH workspaces; external providers and connectors.
- Standard-distribution boundary: Shipped CLI/runtime, experimental supervised orchestration and configured bots with built-in templates.
- Credited operating / distribution surfaces: Worker launch, orchestration skill, task/dispatch/mail/gates, bot preamble, review template and editable standing instructions.
- Adjacent first-party surfaces excluded from ownership: Contributor/release governance, external CI, unmerged PRs, OpenSiro Roadmaps and unrelated provider-native organizational features.
- First-party operating / deployment modes considered: Normal isolated sessions, supervised orchestration, paired hosts, bot-managed fleets, optional review bots, automations and owner-governed bot role.
- Recursion level: A supported Run or bot-managed work organization, with its workers as S1.
- Reviewed revision: 4ea5e5a090f97563008d5ebb85ce3ccdf5561d71
- Observation date: 2026-11-25
- Generated Profile version: unknown (legacy origin omitted)
- Generated Methodology version: unknown (legacy origin omitted)
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8 (Index active; released 0.3.9 S1 clarification separately consulted).

## Repository architecture

[README.md](https://github.com/stablyai/orca/blob/4ea5e5a090f97563008d5ebb85ce3ccdf5561d71/README.md) describes worktrees, native chat/terminal, bots and remote workers. [orchestration.mdx](https://github.com/stablyai/orca/blob/4ea5e5a090f97563008d5ebb85ce3ccdf5561d71/docs/site/content/docs/cli/orchestration.mdx) defines Run as a namespace/inbox, Tasks and supervised Dispatches. [task-store.ts](https://github.com/stablyai/orca/blob/4ea5e5a090f97563008d5ebb85ce3ccdf5561d71/src/main/runtime/orchestration/db/tasks/task-store.ts) persists tasks and dependencies; [attempt-task-settlement.ts](https://github.com/stablyai/orca/blob/4ea5e5a090f97563008d5ebb85ce3ccdf5561d71/src/main/runtime/orchestration/db/dispatch-context/attempt-task-settlement.ts) completes tasks and promotes dependents on success. [bot-preamble.ts](https://github.com/stablyai/orca/blob/4ea5e5a090f97563008d5ebb85ce3ccdf5561d71/src/main/bots/bot-preamble.ts) provides bot work/worker ownership and PR follow-up rules; [bot-template-create.ts](https://github.com/stablyai/orca/blob/4ea5e5a090f97563008d5ebb85ce3ccdf5561d71/src/main/bots/bot-template-create.ts) packages retained skills, schedules and proposed event triggers. Provider inference is external; runtime enforces permissions and persists transitions; operators retain authorized external actions. Contributor governance is outside the assessed runtime.

## Operational model

Separate coding agents select actions and revise from results. A coordinator manages Run tasks and workers; a bot can manage multiple commitments. The operator configures goals, permissions and optional independent review. Deterministic infrastructure enforces decisions, not autonomous judgment. Individual permission approval is not alone S3 or S5.

## S1 — Operations

- State: A
- Function: Produce software changes and investigations.
- Disturbance / variety regulated: Repository state, failed tools/tests and implementation alternatives.
- Decisive decision or feedback right: Select and revise coding actions.
- Decision owner: Supported coding agent.
- Supporting / enforcement mechanisms: Native chat/terminal, worktrees, dispatch and permissions.
- Closure path: Act, observe, revise, report task outcome.
- Boundary reachability: Shipped worker-start and ordinary session modes invoke autonomous coding loops.
- Why this is / is not agent-owned: Coding agent chooses actions, not the launcher.
- Evidence: [README.md](https://github.com/stablyai/orca/blob/4ea5e5a090f97563008d5ebb85ce3ccdf5561d71/README.md); [native-chat.mdx](https://github.com/stablyai/orca/blob/4ea5e5a090f97563008d5ebb85ce3ccdf5561d71/docs/site/content/docs/agents/native-chat.mdx); [orchestration.mdx](https://github.com/stablyai/orca/blob/4ea5e5a090f97563008d5ebb85ce3ccdf5561d71/docs/site/content/docs/cli/orchestration.mdx).
- Basis: explicit
- Confidence: high
- Caveats: No live provider run.

## S2 — Coordination

- State: A
- Function: Attenuate duplicate work and overlapping edits between workers.
- Disturbance / variety regulated: Interference over files and work ownership.
- Distinct S1 units: Separately dispatched coding agents.
- Inter-S1 disturbance: Two workers can edit overlapping files or start the same work.
- Attenuating coordination relation: Guide requires separate workspaces for overlapping edits; bot rules require checking existing work and routing follow-ups to its worker rather than starting another.
- Feedback into subsequent S1 behaviour: Worktree/worker census and returned dispatch results inform next placement/follow-up.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: Directly addresses interference over files/work ownership.
- Decisive decision or feedback right: Judge overlap, choose separate workspace or reuse existing worker.
- Decision owner: Coordinator/bot agent.
- Supporting / enforcement mechanisms: Isolation, run-scoped IDs, worker follow-up.
- Closure path: Inspect work, select isolated placement or existing worker, receive report and adapt subsequent allocation.
- Boundary reachability: Bundled coordinator guide and bot preamble in shipped modes; ordinary manual isolation is the narrower historical C path.
- Why this is / is not agent-owned: Removing agent judgment leaves isolation but removes discretionary overlap and allocation judgment.
- Evidence: [coordinator-loop.md](https://github.com/stablyai/orca/blob/4ea5e5a090f97563008d5ebb85ce3ccdf5561d71/skill-guides/orchestration/references/coordinator-loop.md); [bot-preamble.ts](https://github.com/stablyai/orca/blob/4ea5e5a090f97563008d5ebb85ce3ccdf5561d71/src/main/bots/bot-preamble.ts); [worktrees.mdx](https://github.com/stablyai/orca/blob/4ea5e5a090f97563008d5ebb85ce3ccdf5561d71/docs/site/content/docs/model/worktrees.mdx); [orchestration.mdx](https://github.com/stablyai/orca/blob/4ea5e5a090f97563008d5ebb85ce3ccdf5561d71/docs/site/content/docs/cli/orchestration.mdx).
- Basis: structural
- Confidence: medium
- Caveats: No guarantee of conflict-free merges; no live trace.

## S3 — Inside-and-now control

- State: A
- Function: Regulate current commitments and exceptions across managed Run/bot work.
- Disturbance / variety regulated: Blocked tasks, failed workers, competing work and unresolved review/check outcomes.
- Whole-system current view: Run tasks, workers, inbox and gates; bot items/work records and PR evidence.
- Current-control decision scope: Choose next task, retry/stop, route follow-up, resolve permitted gates or escalate; choose item status and bounded PR repair.
- Decisive decision or feedback right: Select and apply current intervention within authorized scope.
- Decision owner: Coordinator/bot agent under operator goals and permissions.
- Supporting / enforcement mechanisms: Durable tasks, dispatches, inbox wakeups, gates, item state and PR watch.
- Closure path: Worker report wakes coordinator; it chooses next action and observes returned state. Bot PR-wait recipe reads checks/reviews, routes bounded fixes and re-watches after push.
- Boundary reachability: Shipped experimental orchestration enabled explicitly; guide drives coordinator loop; bot session instructions deliver rules and item mode is enabled.
- Why this is / is not agent-owned: Removing agent judgment leaves lifecycle enforcement, not discretionary commitment/intervention choices. Escalated individual parent decisions do not establish a distinct whole-fleet parent mode.
- Evidence: [orchestration.mdx](https://github.com/stablyai/orca/blob/4ea5e5a090f97563008d5ebb85ce3ccdf5561d71/docs/site/content/docs/cli/orchestration.mdx); [coordinator-loop.md](https://github.com/stablyai/orca/blob/4ea5e5a090f97563008d5ebb85ce3ccdf5561d71/skill-guides/orchestration/references/coordinator-loop.md); [bot-preamble.ts](https://github.com/stablyai/orca/blob/4ea5e5a090f97563008d5ebb85ce3ccdf5561d71/src/main/bots/bot-preamble.ts); [bot-session-instructions.ts](https://github.com/stablyai/orca/blob/4ea5e5a090f97563008d5ebb85ce3ccdf5561d71/src/main/bots/bot-session-instructions.ts); [bot-items-ui.ts](https://github.com/stablyai/orca/blob/4ea5e5a090f97563008d5ebb85ce3ccdf5561d71/src/shared/bot-items-ui.ts); [attempt-task-settlement.ts](https://github.com/stablyai/orca/blob/4ea5e5a090f97563008d5ebb85ce3ccdf5561d71/src/main/runtime/orchestration/db/dispatch-context/attempt-task-settlement.ts); [pr-watch-service.ts](https://github.com/stablyai/orca/blob/4ea5e5a090f97563008d5ebb85ce3ccdf5561d71/src/main/github/pr-watch/pr-watch-service.ts).
- Basis: structural
- Confidence: high
- Caveats: A does not establish exact-head merge/release/adoption obligation. Worker success settles Task; ready-to-merge/closed is not adoption. The historical Roadmap targeted a narrower constructor.

## S3* — Complementary audit

- State: C
- Function: Complementary direct review independent of producer report.
- Disturbance / variety regulated: Worker reports success despite defects or missing tests.
- Claim being audited: Work artifact is safe and ready for acceptance.
- Ordinary reporting path: Producing worker reports outcome via dispatch/mail.
- Complementary access path: Built-in PR-review bot and checklist inspect complete diff, code/callers/tests and return file/line findings and readiness judgment; orchestration skill supports another agent reviewing and reporting back.
- Independence boundary: Compose distinct reviewer bot/worker inspecting the artifact, not just producer report; connect corrective authority for the same organization.
- Who acts on findings: Current-control owner/coordinator routes remediation or withholds acceptance; item rules link review workers and record results.
- Decisive decision or feedback right: Judge direct evidence and return findings.
- Decision owner: Configured reviewer agent; separation and corrective path require composition.
- Supporting / enforcement mechanisms: Review template, checklist, connector, delegation, item/report path.
- Closure path: Reviewer inspects artifact and returns findings to coordinator/operator for correction/acceptance.
- Boundary reachability: Template creation installs retained review skill and offers event/connector; shipped skill supports distinct reviewer workers and returns reports.
- Why this is / is not agent-owned: Audit-specific constructor exists; default producer path does not establish independent corrective closure without composition.
- Evidence: [coding.ts](https://github.com/stablyai/orca/blob/4ea5e5a090f97563008d5ebb85ce3ccdf5561d71/src/shared/bots/bot-template-catalog/coding.ts); [pr-review-checklist.ts](https://github.com/stablyai/orca/blob/4ea5e5a090f97563008d5ebb85ce3ccdf5561d71/src/main/bots/bot-template-skills/pr-review-checklist.ts); [bot-template-create.ts](https://github.com/stablyai/orca/blob/4ea5e5a090f97563008d5ebb85ce3ccdf5561d71/src/main/bots/bot-template-create.ts); [SKILL.md](https://github.com/stablyai/orca/blob/4ea5e5a090f97563008d5ebb85ce3ccdf5561d71/skills/orchestration/SKILL.md); [bot-preamble.ts](https://github.com/stablyai/orca/blob/4ea5e5a090f97563008d5ebb85ce3ccdf5561d71/src/main/bots/bot-preamble.ts).
- Basis: structural
- Confidence: medium
- Caveats: No live review-and-repair trace; ordinary human diff review and CI alone are not S3*.

## S4 — Outside-and-then intelligence

- State: —
- Function: Prospective adaptation of the managed agent organization's capability to outside change.
- Disturbance / variety regulated: External developments requiring future capability change.
- Decisive decision or feedback right: No supplied function-specific prospective capability decision/return loop established.
- Decision owner: Not established.
- Supporting / enforcement mechanisms: Automations, connectors, look-around, templates, model settings and memory.
- Closure path: Current-work suggestions and user project tasks, not an established prospective harness adaptation loop.
- Why this is / is not agent-owned: User software planning/triage is not itself adaptation of the managing harness.
- Evidence: [bot-look-around-prompt.ts](https://github.com/stablyai/orca/blob/4ea5e5a090f97563008d5ebb85ce3ccdf5561d71/src/main/bots/bot-look-around-prompt.ts); [bot-look-around-policy.ts](https://github.com/stablyai/orca/blob/4ea5e5a090f97563008d5ebb85ce3ccdf5561d71/src/main/bots/bot-look-around-policy.ts); [bot-look-around-runner.ts](https://github.com/stablyai/orca/blob/4ea5e5a090f97563008d5ebb85ce3ccdf5561d71/src/main/bots/bot-look-around-runner.ts); [automations.mdx](https://github.com/stablyai/orca/blob/4ea5e5a090f97563008d5ebb85ce3ccdf5561d71/docs/site/content/docs/cli/automations.mdx); [coding.ts](https://github.com/stablyai/orca/blob/4ea5e5a090f97563008d5ebb85ce3ccdf5561d71/src/shared/bots/bot-template-catalog/coding.ts); [planning.ts](https://github.com/stablyai/orca/blob/4ea5e5a090f97563008d5ebb85ce3ccdf5561d71/src/shared/bots/bot-template-catalog/planning.ts); [releases.ts](https://github.com/stablyai/orca/blob/4ea5e5a090f97563008d5ebb85ce3ccdf5561d71/src/shared/bots/bot-template-catalog/releases.ts); [native-chat.mdx](https://github.com/stablyai/orca/blob/4ea5e5a090f97563008d5ebb85ce3ccdf5561d71/docs/site/content/docs/agents/native-chat.mdx).
- Basis: structural
- Confidence: medium
- Caveats: Bounded to supplied modes, not every user-authored automation or wider development organization.

### Absence scope

- Surfaces inspected: Automations, look-around read-only prompt/policy/runner, model selection, bot PR follow-up and planning/release/dependency templates, parent identity/permissions.
- Plausible first-party paths checked: Look-around examines external sources for current obligations; dependency-updates adapts user software as operational tasks; planning/release templates concern projects, model/effort settings configure present operation.
- Why no material first-party path remains: Supplied modes handle current work or user-project outcomes, not an agent-organization-specific prospective judgment and return into future capability. Generic prompting does not establish this path; parent configuration alone is insufficient.

## S5 — Policy and identity

- State: P
- Function: Maintain purpose and legitimate identity of bot-managed work.
- Disturbance / variety regulated: Mission or standing-constraint changes and tensions with requested work.
- Identity / ultimate-policy issue: Who the bot is, what it is for, what it must never do.
- Ultimate authority in each claimed mode: Parent owner defines/revises reviewed seed and SOUL.md; bot drafts from owner's input.
- Decisive decision or feedback right: Choose or revise standing purpose and role constraints.
- Decision owner: Parent human/operator.
- Supporting / enforcement mechanisms: Editable SOUL.md, reviewed seed, preamble, turn-context update/fingerprint; team feature flags are not independently credited.
- Return-to-operation path: SOUL.md read at launch; changed standing instructions detected and delivered to subsequent turns.
- Closure path: Parent specifies purpose/constraints; persisted text read into later context, directs subsequent work/delegation.
- Boundary reachability: Built-in template creation uses owner-reviewed seed; UI edits SOUL.md; runtime instructions and turn context consume it in configured bots.
- Why this is / is not agent-owned: Parent owns ultimate role; bot can draft under that authority. No autonomous S5 mode established.
- Evidence: [bot-soul.ts](https://github.com/stablyai/orca/blob/4ea5e5a090f97563008d5ebb85ce3ccdf5561d71/src/shared/bot-soul.ts); [BotSoulEditor.tsx](https://github.com/stablyai/orca/blob/4ea5e5a090f97563008d5ebb85ce3ccdf5561d71/src/renderer/src/components/settings/bots/BotSoulEditor.tsx); [bot-template-create.ts](https://github.com/stablyai/orca/blob/4ea5e5a090f97563008d5ebb85ce3ccdf5561d71/src/main/bots/bot-template-create.ts); [bot-preamble.ts](https://github.com/stablyai/orca/blob/4ea5e5a090f97563008d5ebb85ce3ccdf5561d71/src/main/bots/bot-preamble.ts); [bot-session-instructions.ts](https://github.com/stablyai/orca/blob/4ea5e5a090f97563008d5ebb85ce3ccdf5561d71/src/main/bots/bot-session-instructions.ts); [bot-turn-context.ts](https://github.com/stablyai/orca/blob/4ea5e5a090f97563008d5ebb85ce3ccdf5561d71/src/main/bots/bot-turn-context.ts); [bot-turn-memory-update.ts](https://github.com/stablyai/orca/blob/4ea5e5a090f97563008d5ebb85ce3ccdf5561d71/src/main/bots/bot-turn-memory-update.ts).
- Basis: structural
- Confidence: medium
- Caveats: Instruction delivery does not prove universal compliance; individual merge approval is not S5. Scope is bot-managed organization, not company governance.

## Recursion

Supported Run and bot-managed fleets have worker S1 units; coordinators can delegate to workers and nested Runs. Positive witnesses belong to supported modes at that recursion, not provider or maintainer organizations.

## Variety and escalation

Isolation and identity checks attenuate interference; coordinator chooses interventions and receives feedback. Parent receives permission and item questions with return to work. PR waits enable bounded repair rather than automatic merge authority.

## Evidence gaps

Source-based new-ref review requested in Index #3467. No provider-backed integration run, independent secondary assessment or exhaustive census. Previous accepted source c33a446190bdfa21286a373e097c50a2b3e0a4d4 and contract 0.2.2/0.3.1 remain in Git history; origin metadata was absent and is not backfilled. Source pinned, not moving HEAD. Optional provider/remote parity, independent review-and-repair and SOUL delivery across resumed sessions merit empirical tests. General S3=A does not prove the exact-head merge/release/adoption obligation in the historical Roadmap; reconcile it after Index acceptance.

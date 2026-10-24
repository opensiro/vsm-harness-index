---
harness_id: multica
project_name: Multica
repository: https://github.com/multica-ai/multica
review_ref: 8c4f4328f6e3baff08394b309034463b5db9d7af
reviewed_at: 2026-10-03
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-03
status: excluded-no-agentic-vsm
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Multica

## Review boundary

- System in focus: the first-party Multica workspace/control plane at frozen revision 8c4f4328f6e3baff08394b309034463b5db9d7af, including issue/workspace/run state, backend queueing, daemon/runtime dispatch, per-run workspaces and credentials, squads, Autopilots, retry/timeout handling, execution logs and review/status control surfaces.
- Purpose and identity: coordinate human and AI work around persistent issues and runs, dispatch configured work to coding-agent runtimes, preserve provenance and progress, and return agent results to a shared reviewable workspace.
- Relevant environment: human workspace members, repositories and Git hosts, external coding-agent CLIs and their model providers, connected runtime machines, chat/webhook integrations and external CI/PR systems.
- Standard-distribution boundary: Multica web/desktop/mobile clients, Go backend, PostgreSQL state, CLI, daemon, queue/dispatch/retry machinery, squad/autopilot orchestration, worktree/run preparation and workspace APIs are inside. Claude Code, Codex, Cursor Agent, GitHub Copilot CLI, OpenCode, OpenClaw, Kimi and the other supported coding-agent CLIs and their model/reasoning loops remain external.
- Credited operating / distribution surfaces: README.md; CLI_AND_DAEMON.md; apps/docs/content/docs/agents.mdx; tasks.mdx; triggering-agents.mdx; squads.mdx; autopilots.mdx; issues.mdx; chat.mdx; security-model.mdx; server/internal/daemon/; server/internal/handler/squad_briefing.go; server/internal/service/ and server/cmd/server/ Autopilot/squad control paths.
- Adjacent first-party surfaces excluded from ownership: contributor-only AGENTS.md and repository development instructions; CI/release workflows; tests/examples and benchmark/smoke fixtures; frontend presentation code where it only renders server state; maintainer governance and repository release processes.
- First-party operating / deployment modes considered: self-hosted server plus daemon; hosted workspace plus user-controlled daemon; direct issue assignment; comments and direct chat; squad delegation; scheduled/webhook/manual Autopilots; retries/recovery and review/status workflows.
- Recursion level: one Multica workspace/control organization around one or more externally executed coding-agent identities. The external coding-agent processes are environmental operational actors, not Multica-owned reasoning loops.
- Reviewed revision: 8c4f4328f6e3baff08394b309034463b5db9d7af.
- Observation date: 2026-10-03.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

Multica is a persistent work/control plane backed by a Go server and PostgreSQL, with web, desktop, mobile and CLI clients. A local agent daemon detects installed coding-agent CLIs, registers runtime capabilities, claims queued runs, prepares a per-run working directory and environment, and spawns the configured external coding tool. The repository explicitly states that Multica does not ship a model and that the supported coding-agent tools must already be installed and authenticated.

Issues provide durable goals, status, discussion and run history. A run records a single execution. Triggering an agent creates a run; a runtime claims it; the runtime invokes the configured AI coding tool. Automatic retry logic handles selected infrastructure failures. Execution logs expose tool activity and errors, while issue status and review surfaces keep the result connected to the original work item.

Squads add a first-party coordination protocol around external agents. A squad-assigned issue wakes a leader agent; Multica injects a system-managed operating protocol and roster; the leader decides which member should work, delegates by mention, records an evaluation and stops. Later comments can wake the leader again. The decisive routing judgment is therefore performed by the external coding-agent process acting as leader, while Multica supplies the protocol, state, triggering and deterministic routing/enforcement substrate.

Autopilots store a runbook, assignee and schedule/webhook/manual triggers. A trigger creates an issue or a direct run and then dispatches the assignee through the same external-agent execution path. They automate initiation, not the open-ended task reasoning itself.

Counterfactual owner test: remove every supported external coding-agent CLI/model loop while retaining the Multica server, database, daemon, issue/run state, squad protocol, Autopilots, retries, logs and review gates. The remaining first-party system can create, queue, schedule, route, retry, stop and record work records, but it cannot interpret an open-ended issue, choose substantive repository/tool actions, inspect their semantic results and autonomously choose the next task action. First-party autonomous S1 therefore does not close at this frozen boundary.

Primary evidence:

- [README.md](https://github.com/multica-ai/multica/blob/8c4f4328f6e3baff08394b309034463b5db9d7af/README.md) — Multica says it drives already-installed agent CLIs, does not ship a model, and shows the daemon spawning those external tools.
- [apps/docs/content/docs/agents.mdx](https://github.com/multica-ai/multica/blob/8c4f4328f6e3baff08394b309034463b5db9d7af/apps/docs/content/docs/agents.mdx) — a Multica agent is an identity/configuration that drives an AI coding tool through a bound runtime rather than a continuously running first-party reasoning process.
- [apps/docs/content/docs/tasks.mdx](https://github.com/multica-ai/multica/blob/8c4f4328f6e3baff08394b309034463b5db9d7af/apps/docs/content/docs/tasks.mdx) — run execution is explicitly runtime claim followed by invocation of the configured AI coding tool; retries distinguish platform faults from errors returned by the external agent.
- [apps/docs/content/docs/squads.mdx](https://github.com/multica-ai/multica/blob/8c4f4328f6e3baff08394b309034463b5db9d7af/apps/docs/content/docs/squads.mdx) and [server/internal/handler/squad_briefing.go](https://github.com/multica-ai/multica/blob/8c4f4328f6e3baff08394b309034463b5db9d7af/server/internal/handler/squad_briefing.go) — Multica supplies the squad protocol and re-trigger mechanics, while the leader agent reads the issue and decides whom to delegate to.
- [apps/docs/content/docs/autopilots.mdx](https://github.com/multica-ai/multica/blob/8c4f4328f6e3baff08394b309034463b5db9d7af/apps/docs/content/docs/autopilots.mdx) — Autopilots schedule or event-trigger runs assigned to an agent or squad.
- [apps/docs/content/docs/security-model.mdx](https://github.com/multica-ai/multica/blob/8c4f4328f6e3baff08394b309034463b5db9d7af/apps/docs/content/docs/security-model.mdx) — the daemon spawns Codex, Claude Code or another AI coding tool as a child process and does not claim to own that tool's sandbox/reasoning boundary.

## Operational model

A user, comment, chat message, schedule or webhook creates work in Multica. The backend records a run and routes it to a bound runtime. The daemon prepares execution state and invokes an external coding-agent CLI. That external process performs the open-ended task reasoning and tool/action loop. Multica streams and persists resulting activity, applies deterministic lifecycle/retry rules, and exposes human review and status controls.

In squad mode, the same execution model is used for a leader agent whose prompt receives first-party coordination instructions. The leader's model chooses delegation and later re-evaluates progress; Multica routes the resulting mentions and re-triggers. This is a substantive coordination harness around external agents, but it does not move the decisive cognitive owner of the operational or coordinating decisions into Multica itself.

Because the autonomous-harness admission boundary requires a first-party autonomous S1, the mechanisms below are assessed as control/coordination/audit/adaptation candidates but are not published as positive autonomy states for this excluded frozen revision.

## S1 — Operations

- State: —
- Function: no first-party autonomous environment-facing open-ended operational loop is established inside Multica.
- Disturbance / variety regulated: Multica regulates task arrival, runtime availability, execution lifecycle, workspace isolation, retries and review state around coding work, but the semantic variety of the coding task is handled by an external coding-agent CLI/model loop.
- Decisive decision or feedback right: interpret the issue/chat/runbook, choose the next substantive repository/tool action, observe its result and choose what follows.
- Decision owner: the configured external coding-agent CLI/model process.
- Supporting / enforcement mechanisms: issue/run state, daemon, runtime binding, per-run workspace/environment preparation, run-scoped tokens, queue/claim logic, timeout/retry handling, transcript streaming and status APIs.
- Closure path: Multica trigger and context → external coding-agent process → external tool/repository actions and observations → external next-action decision → Multica result/progress persistence.
- Boundary reachability: the Multica daemon and dispatch machinery are shipped, but ordinary execution explicitly requires and spawns an installed external coding-agent tool; the decisive open-ended loop is therefore outside the credited boundary.
- Why this is / is not agent-owned: a Multica “agent” is a reusable identity/configuration bound to an external runtime/tool. Removing the external tool leaves task-control machinery but no first-party actor that can carry the open-ended task trajectory.
- Evidence: [README.md](https://github.com/multica-ai/multica/blob/8c4f4328f6e3baff08394b309034463b5db9d7af/README.md); [apps/docs/content/docs/agents.mdx](https://github.com/multica-ai/multica/blob/8c4f4328f6e3baff08394b309034463b5db9d7af/apps/docs/content/docs/agents.mdx); [apps/docs/content/docs/tasks.mdx](https://github.com/multica-ai/multica/blob/8c4f4328f6e3baff08394b309034463b5db9d7af/apps/docs/content/docs/tasks.mdx); [apps/docs/content/docs/security-model.mdx](https://github.com/multica-ai/multica/blob/8c4f4328f6e3baff08394b309034463b5db9d7af/apps/docs/content/docs/security-model.mdx).
- Basis: explicit + structural negative review.
- Confidence: high.
- Caveats: Multica owns substantial execution infrastructure and can constrain or interrupt runs; those support rights do not transfer the external tool's semantic action-selection ownership into Multica.

### Absence scope

- Surfaces inspected: README/architecture; daemon and runtime documentation/code; agent/run/chat/issue docs; task queue, retries/timeouts, workdir/environment preparation, runtime profiles, permissions and status flows; squad and Autopilot paths.
- Plausible first-party paths checked: daemon as operational agent; issue-status automation as S1; Autopilot as autonomous operation; squad leader protocol as first-party cognition; Build-with-AI/config generation; retry/recovery as task reasoning.
- Why no material first-party path remains: each path either deterministically controls lifecycle/configuration or invokes an external coding-agent process for the open-ended decision/action/observation loop.

## S2 — Coordination

- State: —
- Function: Multica supplies a strong coordination substrate, especially squads, but no positive first-party autonomous S2 ownership state is retained after S1 admission fails.
- Disturbance / variety regulated: squads address uncertainty over which specialized worker should take the next step and prevent uncontrolled duplicate/self-triggering runs.
- Distinct S1 units: configured agent identities may represent distinct external coding-agent workers, but their operational S1 loops are external to Multica.
- Inter-S1 disturbance: competing/ambiguous ownership, duplicate triggers and sequencing of specialized external workers are structurally addressed by the squad protocol and dedup rules.
- Attenuating coordination relation: Multica wakes one leader, injects roster/protocol constraints, turns delegation mentions into member runs, suppresses specified re-trigger loops and later wakes the leader on relevant updates.
- Feedback into subsequent S1 behaviour: leader comments and mentions cause Multica to enqueue subsequent external-agent runs; member updates can wake the leader again.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the squad protocol explicitly exists to choose among specialized members and close repeated delegation/re-evaluation cycles, not merely transport messages. However, the decisive choice of member and next step belongs to the external leader agent.
- Decisive decision or feedback right: judge which member should take the next step and whether to delegate, escalate or close the coordination loop.
- Decision owner: the external coding-agent process instantiated as the squad leader; first-party Multica owns protocol injection and deterministic trigger routing.
- Supporting / enforcement mechanisms: squad roster/instructions, mention parser, trigger/dedup rules, activity records, parent-status permission boundary and run queue.
- Closure path: issue/update → Multica wakes external leader → external leader chooses delegation → Multica routes mention/run → external member acts → update wakes leader.
- Boundary reachability: squad machinery is shipped and directly wired into runs, but its discretionary coordinator is an external coding-agent runtime.
- Why this is / is not agent-owned: Multica constructs and enforces the coordination channel while borrowing the decisive coordination judgment from an external agent. With no first-party S1 population, this is not published as a positive autonomous-harness state.
- Evidence: [apps/docs/content/docs/squads.mdx](https://github.com/multica-ai/multica/blob/8c4f4328f6e3baff08394b309034463b5db9d7af/apps/docs/content/docs/squads.mdx); [server/internal/handler/squad_briefing.go](https://github.com/multica-ai/multica/blob/8c4f4328f6e3baff08394b309034463b5db9d7af/server/internal/handler/squad_briefing.go).
- Basis: explicit + structural negative publication review.
- Confidence: high.
- Caveats: this does not deny that Multica is practically useful as an S2-like coordination layer around external agents; the negative publication state follows the autonomous-harness system boundary.

### Absence scope

- Surfaces inspected: squad composition, leader protocol, roster/mentions, leader re-trigger rules, activity recording, deduplication, issue assignment and agent access controls.
- Plausible first-party paths checked: deterministic mention routing as S2 owner; squad protocol as constructor/autonomous S2; leader status authority; multi-agent shared workspace state.
- Why no material first-party path remains: the S2-specific discretionary routing judgment is made by an external leader agent, while the supposed S1 units are themselves externally executed; first-party code provides deterministic transport/enforcement rather than an autonomous internal S2 owner.

## S3 — Inside-and-now control

- State: —
- Function: no first-party autonomous whole-system current-control owner over a Multica-owned S1 organization is established.
- Disturbance / variety regulated: queue state, runtime health, concurrency, retries, issue status, run cancellation and review gates regulate current work execution.
- Whole-system current view: the workspace, issue board, runtime state and execution log provide broad current visibility, but the observed operational units are externally executed agents.
- Current-control decision scope: deterministic rules can claim/queue/retry/stop runs and recover status; external agents explicitly write work status as they progress; humans or integrations usually confirm done/review outcomes.
- Decisive decision or feedback right: discretionary current allocation/prioritization/intervention across an internal operational population is not owned by a first-party autonomous Multica actor.
- Decision owner: split among external agent runs, human workspace members and deterministic platform rules, depending on the action.
- Supporting / enforcement mechanisms: board/status state, queue/claim state, runtime heartbeats, retry/timeout logic, concurrency controls, stop controls, execution logs and review surfaces.
- Closure path: platform state and failures can deterministically alter queue/status/retry behavior, while semantic current-control choices return through external agents or humans rather than a first-party autonomous controller.
- Boundary reachability: all support machinery is shipped, but no internal S1 organization and autonomous S3 decision owner are reachable without external worker/human decision makers.
- Why this is / is not agent-owned: enforcement and visibility are substantial but do not themselves own the whole-system discretionary current-control judgment required for S3.
- Evidence: [apps/docs/content/docs/tasks.mdx](https://github.com/multica-ai/multica/blob/8c4f4328f6e3baff08394b309034463b5db9d7af/apps/docs/content/docs/tasks.mdx); [apps/docs/content/docs/issues.mdx](https://github.com/multica-ai/multica/blob/8c4f4328f6e3baff08394b309034463b5db9d7af/apps/docs/content/docs/issues.mdx); [README.md](https://github.com/multica-ai/multica/blob/8c4f4328f6e3baff08394b309034463b5db9d7af/README.md).
- Basis: explicit + structural negative review.
- Confidence: high.
- Caveats: operator review and squad-leader status management can close useful supervisory loops in a larger human+agent organization, but they do not establish a first-party autonomous Multica S3 owner at this boundary.

### Absence scope

- Surfaces inspected: board/issue lifecycle, task queue, retries/timeouts, runtime health, cancellation, review/status behavior, squad status ownership and execution-log surfaces.
- Plausible first-party paths checked: scheduler/queue as S3; retry controller as S3; squad leader as S3; human review gate as parent S3; runtime health/recovery as S3.
- Why no material first-party path remains: deterministic lifecycle mechanisms enforce preset rules, and discretionary semantic control belongs to external agents or humans over externally executed operations.

## S3* — Complementary audit

- State: —
- Function: no materially independent first-party complementary audit judgment with corrective return is established.
- Disturbance / variety regulated: execution logs, transcripts, status history and review gates expose what external agents did and let humans inspect outcomes.
- Claim being audited: whether the external agent's work is correct/acceptable and whether the issue goal has actually been met.
- Ordinary reporting path: external coding-agent output, comments, tool transcript and run completion records.
- Complementary access path: Multica records runtime/tool events and repository-linked work state, but the inspected surfaces do not show a separate first-party autonomous auditor independently judging task correctness.
- Independence boundary: logging/storage is structurally separate from the external agent, but independent access without independent judgment is insufficient for S3*.
- Who acts on findings: humans may review, retry, add requirements or approve delivery; external agents may be triggered again.
- Decisive decision or feedback right: accept/reject/challenge the semantic result using independent evidence.
- Decision owner: no first-party autonomous Multica audit actor is established; ordinary review authority is human/external.
- Supporting / enforcement mechanisms: execution log, streamed transcript, run history, issue comments/status and PR/review integrations.
- Closure path: logs/results → human or external review → optional retry/new run; no first-party independent audit judgment closes autonomously.
- Boundary reachability: logs and review surfaces are shipped, but they do not include a qualifying autonomous independent audit decision path.
- Why this is / is not agent-owned: observability and a human review gate are not by themselves S3*; the required complementary judgment remains outside the first-party autonomous boundary.
- Evidence: [README.md](https://github.com/multica-ai/multica/blob/8c4f4328f6e3baff08394b309034463b5db9d7af/README.md); [apps/docs/content/docs/tasks.mdx](https://github.com/multica-ai/multica/blob/8c4f4328f6e3baff08394b309034463b5db9d7af/apps/docs/content/docs/tasks.mdx); [apps/docs/content/docs/issues.mdx](https://github.com/multica-ai/multica/blob/8c4f4328f6e3baff08394b309034463b5db9d7af/apps/docs/content/docs/issues.mdx).
- Basis: explicit + structural negative review.
- Confidence: high.
- Caveats: users can compose a separate reviewer agent through Multica, but that reviewer would again be an external coding-agent runtime and is not evidence of a first-party Multica auditor.

### Absence scope

- Surfaces inspected: execution logs/transcripts, issue/run history, review gates, retry controls, squad evaluation records and PR/status integration behavior.
- Plausible first-party paths checked: transcript as complementary audit; review gate as S3*; squad leader re-evaluation; retry classification; separate external reviewer-agent composition.
- Why no material first-party path remains: the platform independently records evidence but does not itself make an independent semantic audit judgment and return corrective action through an autonomous first-party path.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party autonomous prospective environment-facing adaptation loop is established.
- Disturbance / variety regulated: schedules, webhooks, runtime/provider availability and reusable skills let operators react to changing work and external events.
- External distinction: Autopilot webhooks/schedules and connected integrations can bring external events into the workspace.
- Future / prospective distinction: runbooks, skills, runtime profiles and workspace settings can encode future behavior, but they are configured by users/maintainers rather than autonomously selected from environmental intelligence.
- Adaptation option generated: no first-party autonomous mechanism is established that models external change and chooses a capability adaptation.
- Path back into current capability / S3: user/maintainer edits to agents, skills, runbooks, profiles or access settings affect later runs; automatic retries restore an existing execution path rather than adapt organizational capability.
- Decisive decision or feedback right: choose a prospective change to present capability in response to environment-facing intelligence.
- Decision owner: users/maintainers or external agent/model workflows, not an autonomous first-party Multica S4 actor.
- Supporting / enforcement mechanisms: Autopilots, webhook filters, skills, runtime profiles, model/tool configuration, persistent history and update/recovery machinery.
- Closure path: external event can trigger current work, but no first-party sense → model future → choose adaptation → reinject capability loop is established.
- Boundary reachability: scheduling and configuration surfaces are shipped; autonomous adaptation ownership is not.
- Why this is / is not agent-owned: event-triggering, persistence and retry are current execution mechanisms; they do not supply prospective adaptation judgment.
- Evidence: [apps/docs/content/docs/autopilots.mdx](https://github.com/multica-ai/multica/blob/8c4f4328f6e3baff08394b309034463b5db9d7af/apps/docs/content/docs/autopilots.mdx); [apps/docs/content/docs/agents.mdx](https://github.com/multica-ai/multica/blob/8c4f4328f6e3baff08394b309034463b5db9d7af/apps/docs/content/docs/agents.mdx); [apps/docs/content/docs/tasks.mdx](https://github.com/multica-ai/multica/blob/8c4f4328f6e3baff08394b309034463b5db9d7af/apps/docs/content/docs/tasks.mdx).
- Basis: explicit + structural negative review.
- Confidence: high.
- Caveats: an external agent can be asked to recommend changes through Multica, but its reasoning remains outside the credited first-party boundary and adoption still requires a separate authority path.

### Absence scope

- Surfaces inspected: Autopilot schedule/webhook/runbook flows, agent/skill/runtime configuration, model/provider switching, retry/recovery, persistent issue/run history and external integrations.
- Plausible first-party paths checked: Autopilot as S4; skills as learned adaptation; retry/self-recovery; runtime re-probing/updating; Build-with-AI configuration; webhook reaction.
- Why no material first-party path remains: these paths trigger work, restore existing capability or apply externally/user-selected configuration; none autonomously chooses and reinjects a prospective capability adaptation.

## S5 — Policy and identity

- State: —
- Function: no first-party autonomous runtime identity/ultimate-policy resolution loop is established for Multica.
- Disturbance / variety regulated: workspace roles, per-agent Access, runtime profiles, run-scoped tokens, instructions, review expectations and security configuration constrain who can run which agents and what execution context they receive.
- Identity / ultimate-policy issue: the inspected configuration expresses operator-selected permissions and work rules, not an autonomous Multica process resolving identity or ultimate-policy tensions at runtime.
- Ultimate authority in each claimed mode: workspace owners/admins, agent owners and ordinary users hold the documented policy/configuration rights; external agents act within those granted constraints.
- Return-to-operation path: human-selected permissions, instructions, runbooks and runtime settings are enforced on later runs.
- Decisive decision or feedback right: resolve an identity/ultimate-policy question for the organization and authoritatively return that decision to operation.
- Decision owner: human/operator governance for the reviewed paths; no qualifying autonomous first-party S5 owner is established.
- Supporting / enforcement mechanisms: workspace roles, agent Access, squad permissions, run-scoped credentials, configuration, security model and review status conventions.
- Closure path: human configuration → deterministic enforcement → later external-agent run; this is policy administration rather than a first-party autonomous S5 loop.
- Boundary reachability: policy enforcement is shipped, but identity/ultimate-policy decision ownership remains human/operator controlled.
- Why this is / is not agent-owned: strong permissions and identity tokens enforce prior decisions; they do not make the runtime the owner of ultimate policy.
- Evidence: [apps/docs/content/docs/agents.mdx](https://github.com/multica-ai/multica/blob/8c4f4328f6e3baff08394b309034463b5db9d7af/apps/docs/content/docs/agents.mdx); [apps/docs/content/docs/security-model.mdx](https://github.com/multica-ai/multica/blob/8c4f4328f6e3baff08394b309034463b5db9d7af/apps/docs/content/docs/security-model.mdx); [apps/docs/content/docs/squads.mdx](https://github.com/multica-ai/multica/blob/8c4f4328f6e3baff08394b309034463b5db9d7af/apps/docs/content/docs/squads.mdx).
- Basis: explicit + structural negative review.
- Confidence: high.
- Caveats: human ownership of permissions and review is important governance, but Methodology 0.3.6 does not equate ordinary static policy/configuration with positive S5.

### Absence scope

- Surfaces inspected: workspace roles, agent ownership/Access, instructions, squad permissions, run-scoped identity/tokens, runtime configuration, security model, review/status conventions and self-hosted/operator modes.
- Plausible first-party paths checked: RBAC as S5; agent identity as S5; run token authority; human review as parent S5; squad protocol as identity policy; security configuration.
- Why no material first-party path remains: inspected mechanisms encode and enforce operator-selected permissions/policy without a runtime identity/ultimate-policy tension-and-resolution loop owned by Multica.

## Recursion

Multica is assessed at the workspace/control-plane recursion. Its first-party server, daemon and clients coordinate many configured agent identities, but the open-ended reasoning loops behind those identities live in external coding-agent tools. Squads create a higher-order coordination structure over those workers without converting the workers or leader cognition into first-party Multica S1 units.

## Variety and escalation

Multica attenuates operational variety through persistent issues, run queues, runtime binding, per-run workspaces, concurrency controls, retries/timeouts, deduplication, status rules, squad protocols, Autopilot triggers, access controls and human review. It escalates blockers through comments/inbox/review flows and can preserve full execution history. These are substantial organizational-control capabilities, but the autonomous-harness inclusion gate is not met because the substantive open-ended operational loop remains external.

## Evidence gaps

- The assessment is intentionally frozen at 8c4f4328f6e3baff08394b309034463b5db9d7af; later Multica changes are outside this review.
- External coding-agent CLIs differ in their own agent loops, multi-agent features, review mechanisms and model providers. None of those external capabilities are imported.
- Hosted-service internals not represented by the frozen public repository are not used for positive ownership claims.
- Multica can compose multiple external agents into sophisticated organizations; this exclusion is about first-party autonomous-harness ownership under the active Index contract, not practical usefulness or orchestration breadth.

## Assessment summary

At frozen revision 8c4f4328f6e3baff08394b309034463b5db9d7af, Multica is a substantial first-party workspace, lifecycle, dispatch and coordination control plane around external coding-agent runtimes. It owns queues, state, schedules, squad protocols, retries, logs and review surfaces, but its own documentation and runtime architecture place the open-ended objective → decision → action → observation → next-decision loop in Claude Code, Codex and other external tools. Under Profile 0.2.4 / Methodology 0.3.6, first-party autonomous S1 therefore does not close, so the proposed terminal disposition is excluded-no-agentic-vsm for this frozen revision.

**Vector:** — · — · — · — · — · —

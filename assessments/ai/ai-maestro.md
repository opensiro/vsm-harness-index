---
harness_id: ai-maestro
project_name: AI Maestro
repository: https://github.com/23blocks-OS/ai-maestro
review_ref: 6c8a5927d66637855c2a31d1b54f92abc9b9e165
reviewed_at: 2026-10-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# AI Maestro

## Review boundary

- System in focus: one self-hosted AI Maestro distributed multi-agent workspace spanning actual CLI agent sessions on local/remote hosts, AMP communication, task/meeting/project dashboard and an operator directing the team.
- Purpose and identity: make multiple persistent, separately owned AI work cells manageable through communication, tasks and human operations control without copying context between terminals.
- Relevant environment: independent agent source repositories, changing tool outputs, cross-machine host availability, message delivery, project dependencies, owner requests and human approval needs.
- Standard distribution: dashboard/server, runtime bridge to external agent CLI programs, hosted/headless agents, AMP transport, agent tasks, teams, meetings and operator chat/approval controls. Bundled optional Claude plugin is a separate Git submodule not present in this shallow checkout.
- Credited operating / distribution surfaces: supported external model CLI workers under first-party session/runtime integration; operator's whole-team live status, task assignment and message/approval controls.
- Adjacent first-party surfaces excluded from ownership: README scripted multi-agent demo, example organization screens, maintainers' own companies, optional separate plugin submodule content not inspected, installer marketing and external model internals.
- First-party operating modes considered: tmux/remote CLI sessions, multi-host AMP messaging, direct agent-owned repositories, task boards with dependency status, human team view/assignment and chat; no presumption that a named project-manager agent is itself a packaged central regulator.
- Recursion level: individual model-backed working agents are S1 cells; assembled multi-host team/dashboard is the evaluated parent boundary with an actual supported operator decision surface.
- Reviewed revision: 23blocks-OS/ai-maestro@6c8a5927d66637855c2a31d1b54f92abc9b9e165 exact first-party checkout, MIT LICENSE. Uninitialized optional plugin submodule is not borrowed as positive evidence.
- Observation date: 2026-10-29, Profile 0.2.4 / released Methodology 0.3.7.

## Repository architecture

The installed dashboard discovers and presents model-driven CLI agents, locally or across peer hosts. Agents can receive messages, run in their own repositories, and use per-agent/team/project task boards with owners, dependency links, status, due dates and waiting states. The backend records a completed dependency and returns newly unblocked task IDs; this is task bookkeeping, not proof of an autonomous cross-worker collision resolver. Meetings broadcast messages and report per-agent delivered, deferred and failed results across hosts; the content and reconciliation judgment remain with agents/operators. Sources: https://github.com/23blocks-OS/ai-maestro/blob/6c8a5927d66637855c2a31d1b54f92abc9b9e165/README.md, https://github.com/23blocks-OS/ai-maestro/blob/6c8a5927d66637855c2a31d1b54f92abc9b9e165/services/agent-tasks-service.ts, https://github.com/23blocks-OS/ai-maestro/blob/6c8a5927d66637855c2a31d1b54f92abc9b9e165/lib/task-registry.ts, https://github.com/23blocks-OS/ai-maestro/blob/6c8a5927d66637855c2a31d1b54f92abc9b9e165/services/meeting-broadcast-service.ts, https://github.com/23blocks-OS/ai-maestro/blob/6c8a5927d66637855c2a31d1b54f92abc9b9e165/services/agents-messaging-service.ts.

The human operator has a genuine project/team-wide present-state surface: status, open/waiting/blocked cards, agents across hosts, priority and review; they may choose assignments, update status, send instructions and answer live permission requests. This is current human parent control through AI Maestro, not a model-backed autonomous S3. The organization feature itself explicitly says that org labels are displayed, not enforced; neither organizational tags nor a name called CEO prove ultimate-policy S5. Code graph and nightly memory collect prior context rather than constructing externally prospective options with a two-way S3/S4 loop. Sources: https://github.com/23blocks-OS/ai-maestro/blob/6c8a5927d66637855c2a31d1b54f92abc9b9e165/lib/organization.ts, https://github.com/23blocks-OS/ai-maestro/blob/6c8a5927d66637855c2a31d1b54f92abc9b9e165/services/agent-tasks-service.ts, https://github.com/23blocks-OS/ai-maestro/blob/6c8a5927d66637855c2a31d1b54f92abc9b9e165/services/agents-chat-service.ts, https://github.com/23blocks-OS/ai-maestro/blob/6c8a5927d66637855c2a31d1b54f92abc9b9e165/services/orgs-service.ts.

## Operational model

Model-backed CLI workers perform actual coding/research tasks with external host capabilities; AI Maestro stores identity, tasks, live state and message channels. Human team lead observes whole current commitments and can intervene through task assignment, chat, meeting and approvals. AMP message delivery alone does not guarantee conflict resolution, and simple task blockers are visible metadata rather than evidence that an agent or deterministic runtime reconciles incompatible independently produced work. No independent audit model, future-capability adaptation governor or ultimate-policy adjudicator was established in the credited runtime boundary.

## S1 — Operations

- State: A
- Function: execute independently scoped project tasks and produce model-chosen code, research or operational output.
- Disturbance / variety regulated: source changes, requirements, test failures and external messages for an agent's owned repository/process.
- Decisive decision or feedback right: the active external CLI model decides what tools to use and how to revise its work.
- Decision owner: attached Claude Code/Codex/other supported CLI model agent; AI Maestro supplies runtime access, message and context transport.
- Supporting / enforcement mechanisms: tmux/remote session management, per-agent clone, tasks, AMP, memory and tool approvals.
- Closure path: operator/task brief → model agent session acts in own working directory → changed artifact/test result → agent reports via message/task board.
- Why this is / is not agent-owned: the dashboard can display/send work but does not generate the actual task-specific code decisions without its model agent.
- Evidence: https://github.com/23blocks-OS/ai-maestro/blob/6c8a5927d66637855c2a31d1b54f92abc9b9e165/README.md; https://github.com/23blocks-OS/ai-maestro/blob/6c8a5927d66637855c2a31d1b54f92abc9b9e165/lib/agent-runtime.ts; https://github.com/23blocks-OS/ai-maestro/blob/6c8a5927d66637855c2a31d1b54f92abc9b9e165/services/agents-core-service.ts; https://github.com/23blocks-OS/ai-maestro/blob/6c8a5927d66637855c2a31d1b54f92abc9b9e165/services/agents-chat-service.ts
- Basis: shipped CLI integration and task communication path; no live external LLM E2E.
- Confidence: high for supported S1 actor boundary, unmeasured outcomes.
- Caveats: some supported terminal programs have fewer chat/control integrations; no third-party provider internals are credited.
- Boundary reachability: standard deployed agent session on local tmux or supported remote host.

## S2 — Coordination

- State: —
- Function: no qualifying first-party inter-S1 incompatible work arbitration or repair path was established.
- Disturbance / variety regulated: two independent agents may change the same API or repository branch incompatibly.
- Decisive decision or feedback right: humans/agents choose how to respond to AMP messages; the service only delivers messages and tracks task blockers.
- Decision owner: no deployed S2 controller with a specific conflict-detection/settlement right demonstrated; agents retain local task choices.
- Supporting / enforcement mechanisms: per-agent clone/branch isolation, signed AMP transport, meeting delivery statuses, blockedBy graph and waiting cards.
- Closure path: agents see messages/blocked status and may respond; no shipped concrete incompatible-artifact detection and corrective return to each S1 was verified.
- Why this is / is not agent-owned: AMP, org/task links and Git clone separation transport or prevent some overlap but do not prove actual cross-S1 correction judgment.
- Evidence: https://github.com/23blocks-OS/ai-maestro/blob/6c8a5927d66637855c2a31d1b54f92abc9b9e165/services/agents-messaging-service.ts; https://github.com/23blocks-OS/ai-maestro/blob/6c8a5927d66637855c2a31d1b54f92abc9b9e165/services/meeting-broadcast-service.ts; https://github.com/23blocks-OS/ai-maestro/blob/6c8a5927d66637855c2a31d1b54f92abc9b9e165/lib/task-registry.ts; https://github.com/23blocks-OS/ai-maestro/blob/6c8a5927d66637855c2a31d1b54f92abc9b9e165/docs/CONCEPTS.md
- Basis: bounded negative across message, task dependency and Git ownership surfaces.
- Confidence: medium; human or agent teams may build effective coordination practices outside this tested first-party circuit.
- Caveats: dependency completion computes newly unblocked IDs but does not itself merge incompatible code, enforce dependent execution or negotiate changed interfaces.

### Absence scope

- Surfaces inspected: AMP send/receive, meeting broadcast, per-agent clones, agent/team/project task dependencies and blockers
- Plausible first-party paths checked: agent request/response, waiting-on-agent, completion unblocks, independent clone plus Git PR integration
- Why no material first-party path remains: all inspected shipped mechanisms carry messages or dependency state, with no specified conflicting S1 outputs, adjudicated correction and returned behavior change.

## S3 — Inside-and-now control

- State: P
- Function: let a parent human regulate present distributed team work, current priorities, assignments and blocked commitments.
- Disturbance / variety regulated: many agents across hosts, blocked or overdue tasks, limited operator attention, delivery failures and work waiting for approval.
- Decisive decision or feedback right: operator chooses which agent owns a card, current priority/status, instructions, meeting scope and approval response from team-wide present state.
- Decision owner: parent human operator acting through installed dashboard and chat, not a default AI Maestro management model.
- Supporting / enforcement mechanisms: host/agent status aggregation, Matrix/Attention board, task API, chat-to-terminal delivery, team meeting and receipt/status records.
- Closure path: team-wide active/blocked/waiting view → human assignment or intervention → persisted task update or message/approval delivery → agent receives new current commitment.
- Why this is / is not agent-owned: UI and API do not choose priorities or reconcile across team autonomously; present controlling judgment remains with user (P).
- Evidence: https://github.com/23blocks-OS/ai-maestro/blob/6c8a5927d66637855c2a31d1b54f92abc9b9e165/lib/organization.ts; https://github.com/23blocks-OS/ai-maestro/blob/6c8a5927d66637855c2a31d1b54f92abc9b9e165/services/agent-tasks-service.ts; https://github.com/23blocks-OS/ai-maestro/blob/6c8a5927d66637855c2a31d1b54f92abc9b9e165/services/agents-chat-service.ts; https://github.com/23blocks-OS/ai-maestro/blob/6c8a5927d66637855c2a31d1b54f92abc9b9e165/services/meeting-broadcast-service.ts
- Basis: supported parent-assisted operating mode with real whole-team view and task/message write paths.
- Confidence: medium-high for available human-controlled current-team closure; individual user's actual meeting choices are not observed.
- Caveats: no automatic model S3 is claimed; unattended API usage alone and task board visuals alone do not prove the human actually exercises every S3 judgment.
- Whole-system current view: Matrix/Attention aggregates open, waiting, review and blocked cards across agents and hosts; organization view groups active work and assignments.
- Current-control decision scope: assign/change task owner, choose present priority and current commitments, send corrective instruction or answer a pending agent approval.
- Boundary reachability: normal self-hosted dashboard and integrated task/chat API directly expose operator write actions to working agent sessions.

## S3* — Complementary audit

- State: —
- Function: no first-party sufficiently independent alternative audit of work outcomes and return to control was established.
- Disturbance / variety regulated: a worker could falsely report completion or produce a regression unobserved by routine status.
- Decisive decision or feedback right: operator may review a card/commit trace, but no separately invoked independent challenger is mandated or shown.
- Decision owner: no specific S3* judge for actual work evidence within assessed code.
- Supporting / enforcement mechanisms: review column, commit trace, agent chat history, docs/code graph and activity status.
- Closure path: visible trace can lead a human to inspect manually, without a packaged complementary auditor diagnosis and correction route.
- Why this is / is not agent-owned: passive trace, status and ordinary review labels do not choose adverse fault findings.
- Evidence: https://github.com/23blocks-OS/ai-maestro/blob/6c8a5927d66637855c2a31d1b54f92abc9b9e165/README.md; https://github.com/23blocks-OS/ai-maestro/blob/6c8a5927d66637855c2a31d1b54f92abc9b9e165/services/commit-trace-service.ts; https://github.com/23blocks-OS/ai-maestro/blob/6c8a5927d66637855c2a31d1b54f92abc9b9e165/services/agent-tasks-service.ts
- Basis: bounded negative across review statuses, session tracing and docs/code index.
- Confidence: medium; an external agent role could provide audit when explicitly installed elsewhere.
- Caveats: a screenshot of a code-reviewer agent is not proof of its executable independent audit or return loop.

### Absence scope

- Surfaces inspected: review tasks, commit trace, session transcripts, code graph, documentation and team meeting
- Plausible first-party paths checked: review status, named reviewer, agent messages, history replay and trace visualization
- Why no material first-party path remains: none shows a distinct reviewer accessing actual evidence independently and returning a binding adverse finding to current control.

## S4 — Outside-and-then intelligence

- State: —
- Function: no prospective environmental options process was wired back into the operator's present team capabilities.
- Disturbance / variety regulated: future customers, infrastructure changes, agent models and emerging threats may require adaptation.
- Decisive decision or feedback right: local memory and scheduled agent tasks collect/contextualize history; no S4 options owner is shown.
- Decision owner: human leadership for future strategy, if supplied outside this app.
- Supporting / enforcement mechanisms: long-term memory, entity graph, agent schedules, code graph and reusable notes.
- Closure path: learned retrospective context reaches later prompts, but no external prospective option/choice → S3 capability change loop is evidenced.
- Why this is / is not agent-owned: memory consolidation and nightly summaries are retrospective operational support, not outside-and-then policy intelligence.
- Evidence: https://github.com/23blocks-OS/ai-maestro/blob/6c8a5927d66637855c2a31d1b54f92abc9b9e165/lib/memory/consolidate.ts; https://github.com/23blocks-OS/ai-maestro/blob/6c8a5927d66637855c2a31d1b54f92abc9b9e165/services/agents-schedule-service.ts; https://github.com/23blocks-OS/ai-maestro/blob/6c8a5927d66637855c2a31d1b54f92abc9b9e165/README.md
- Basis: bounded negative on memory, schedules, organization and information surfaces.
- Confidence: medium-high at published runtime boundary.
- Caveats: an operator can program a strategic research agent; that external configuration is not first-party S4 provenance.

### Absence scope

- Surfaces inspected: nightly memory, schedules, graph, host changes, teams and organization records
- Plausible first-party paths checked: future scheduled tasks, learned entity relations, external AMP federation and remote host deployment
- Why no material first-party path remains: these extend current tasks/knowledge or connectivity without prospective environment modeling, options and return to S3.

## S5 — Policy and identity

- State: —
- Function: no identity-level ultimate policy court or balance of current and future organizational identity is implemented.
- Disturbance / variety regulated: company labels, agent roles, secret permissions, approval and conflicting objectives.
- Decisive decision or feedback right: operator can label organizations and approve individual secrets/actions; there is no identity-level dispute resolution path.
- Decision owner: human company authority external to installed model worker ensemble; no evidenced packaged S5 issue closure.
- Supporting / enforcement mechanisms: org tags and names, agent roles, permission/secret UI, messages and dashboard.
- Closure path: task approval or org rename affects local work/display, but no ultimate policy ruling is returned to a sustained S3/S4 decision relation.
- Why this is / is not agent-owned: an organization record is explicitly shown, not enforced; a role label or approval does not constitute S5.
- Evidence: https://github.com/23blocks-OS/ai-maestro/blob/6c8a5927d66637855c2a31d1b54f92abc9b9e165/lib/organization.ts; https://github.com/23blocks-OS/ai-maestro/blob/6c8a5927d66637855c2a31d1b54f92abc9b9e165/services/orgs-service.ts; https://github.com/23blocks-OS/ai-maestro/blob/6c8a5927d66637855c2a31d1b54f92abc9b9e165/services/agents-chat-service.ts
- Basis: bounded negative review of org, identity, role, permission and approval surfaces.
- Confidence: high that labels alone are not governance; external human policy remains outside boundary.
- Caveats: actual human-run companies may have real S5, but they are not inherited by this software product.

### Absence scope

- Surfaces inspected: organization records/tags, identity display, human secret requests, approval cards, team/operator chat
- Plausible first-party paths checked: default organization, company descriptions, CEO/project-manager tags, task authorization and multi-host ownership
- Why no material first-party path remains: no first-party identity-level issue to legitimate ultimate authority and returned policy decision, only labels and operational controls.

## Distributed OSS parent arrangement

The open-source contributors and vendor organization own the product's publication, not the policy of an installed customer's team. A supported human operator can supply parent S3 for present work (P), but no S5 policy authority is imported from the repository maintainers.

## Self-hosted and non-human modes

Dashboard-free headless hosts still run model-backed S1 agents and messaging, but may lack the active human S3 view. The positive parent S3 claim applies when a real operator uses the first-party dashboard/API as their current-team control channel. No autonomous S3 or S5 is inferred from agent naming.

## Recursion

One agent has persistent identity, repository and workload but not necessarily all metasystemic functions; a tag or separate clone does not prove a complete viable recursion. Multi-host team is parent boundary and human operator is its current S3 mode; transport/meeting services are not separate S2 actors.

## Variety and escalation

Per-agent messages and board statuses expose distributed work; dependency records show what waits on what. Human operator prioritizes and intervenes through tasks/chat; delivery receipts and approval cards return responses to live agents. Exceptional needs are visible, but nothing automatically assigns S3* audit, S4 strategy or S5 ultimate policy.

## Evidence gaps

- No provider-agent E2E run; first-party shipped source and README establish reachable agent and operator paths, not measured performance.
- The optional plugin git submodule was not initialized in this source review; no claims borrow missing skill instruction code.
- S3=P is a supported human-in-the-loop present control mode, not an autonomous AI management grade and not an assertion that every deployment has an active parent.
- AMP messages, blockedBy status, Git clones and meeting delivery cannot alone prove S2 conflict negotiation and source-level repair.
- Review-board labels and code graph are not complementary S3* inspection, and memory/organization labels do not establish S4/S5.

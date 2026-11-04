---
harness_id: orco
project_name: Orco
repository: https://github.com/CJVigil/Orco
review_ref: 148f21d5a4dcf4f833e87d9fa38d3a1bfbe9df59
reviewed_at: 2026-11-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-11-04
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: C(P)
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: P
---

# Orco

## Review boundary

- System in focus: The first-party self-hosted Orco server, its connected coding-agent bridge, MCP collaboration tools, persisted project/ticket state, agent review, lock, policy and human portfolio controls.
- Purpose and identity: Let people and multiple connected coding agents carry out project work with shared tasks, reviewable handoffs, resource coordination and explicit human governance.
- Relevant environment: Local or hosted model providers, developers' actual workspaces, other connected agents, concurrent writes, project commitments, budget/CI/approval signals and external software changes.
- Standard-distribution boundary: Orco 0.2.0 Node/TypeScript server, built-in MCP/API/UI and optional first-party bridge that launches local Codex/Claude/other configured model runners. An actual configured model provider is a declared execution dependency; Orco owns the bridge and collaboration controls, not model internals.
- Credited operating / distribution surfaces: [bridge](https://github.com/CJVigil/Orco/blob/148f21d5a4dcf4f833e87d9fa38d3a1bfbe9df59/src/bridge/bridge.ts), [agent MCP tools](https://github.com/CJVigil/Orco/blob/148f21d5a4dcf4f833e87d9fa38d3a1bfbe9df59/src/mcp.ts), [locks](https://github.com/CJVigil/Orco/blob/148f21d5a4dcf4f833e87d9fa38d3a1bfbe9df59/src/locks.ts), [reviews](https://github.com/CJVigil/Orco/blob/148f21d5a4dcf4f833e87d9fa38d3a1bfbe9df59/src/reviews.ts), [portfolio](https://github.com/CJVigil/Orco/blob/148f21d5a4dcf4f833e87d9fa38d3a1bfbe9df59/src/portfolio.ts), [policies](https://github.com/CJVigil/Orco/blob/148f21d5a4dcf4f833e87d9fa38d3a1bfbe9df59/src/policies.ts), [installed agent skill](https://github.com/CJVigil/Orco/blob/148f21d5a4dcf4f833e87d9fa38d3a1bfbe9df59/integrations/claude-code/skills/orco/SKILL.md).
- Adjacent first-party surfaces excluded from ownership: Repository maintainer and GitHub CI/release procedures, package unit tests, examples, operator-specific prompt conventions not installed by Orco, arbitrary external agents without the bridge/MCP connection, upstream model providers and external CI judgment.
- First-party operating / deployment modes considered: Human-led Orco project with one or many connected agent bridges, agent-to-agent task requests and review requests, MCP clients using the bundled Orco skill, optional operator-constructed model supervisor over project tools, and human org/project admin with portfolio and policy rights.
- Recursion level: One Orco-managed organization/project work system containing multiple distinct connected model-bearing operational agents. S3 constructor mode is project-wide; the parent mode is a human project/org administrator. This is not a claim that independently hosted Orco instances form one coordinated VSM.
- Reviewed revision: 148f21d5a4dcf4f833e87d9fa38d3a1bfbe9df59.
- Observation date: 2026-11-04.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The TypeScript server persists participant identities, projects, rooms, tickets, agent tasks, approvals, schedules, review records, shared locks, budgets and hierarchical policies. A connected-agent bridge claims assigned tasks, launches the selected model CLI in its workspace, injects task context and policy instructions, handles interrupted runs, receives tool results and reports completion. MCP exposes ordinary project work as well as locks, reviews, plans, task changes and tickets to connected model agents. A separate first-party integration skill prescribes accepting jobs, obtaining shared locks, waiting or choosing other work when locked, escalating unsafe actions and reporting completion. An optional model reviewer gets its own assigned review task, can reject work with corrective notes and can trigger a restarted implementation task. Human project/org controllers see cross-project health, commitments, milestones, approvals, CI and spend, and can alter live control and enduring organizational policy. [Quickstart](https://github.com/CJVigil/Orco/blob/148f21d5a4dcf4f833e87d9fa38d3a1bfbe9df59/docs/quickstart.md), [bridge](https://github.com/CJVigil/Orco/blob/148f21d5a4dcf4f833e87d9fa38d3a1bfbe9df59/src/bridge/bridge.ts), [reviews](https://github.com/CJVigil/Orco/blob/148f21d5a4dcf4f833e87d9fa38d3a1bfbe9df59/src/reviews.ts), [tickets](https://github.com/CJVigil/Orco/blob/148f21d5a4dcf4f833e87d9fa38d3a1bfbe9df59/src/tickets.ts).

## Operational model

Connected coding agents perform work in actual workspaces (S1); two or more agents can contend for the same named project resource, and model-directed retry/wait/reprioritization after a lock conflict attenuates interference (S2). The shipped portfolio lets human management close project-wide current control; an agent-controlled supervisory path can be constructed from first-party plan/ticket tools, but no preinstalled autonomous portfolio manager is supplied (S3=C(P)). A distinct agent reviewer may independently inspect work and return changes_requested, restarting the original agent's ticket work (S3*=A, optional). Prospective roadmap/status and follow-up queues are not by themselves an outside-and-then capability adaptation loop (S4=—). Human org/project admins hold and revise binding organizational operating policy that returns to the next bridge task and admission decision (S5=P).

## S1 — Operations

- State: A
- Function: Perform substantive software/project tasks through configured model-bearing connected agents.
- Disturbance / variety regulated: Different user requirements, source code state, failing tool results, changed ticket context and incomplete information.
- Decisive decision or feedback right: Choose investigations, tool invocations, file modifications, responses, task completion and when to ask for input.
- Decision owner: Connected model agent using the launched CLI and MCP tools; the human initiating work owns the original request, not the agent's operational choices.
- Supporting / enforcement mechanisms: Task claim leases, connected bridge, model CLI adapter, prompt/context builder, local workspace, MCP task state and policy/budget gates.
- Closure path: User/other agent requests work → bridge claims task and launches model → model reads context/uses tools and adjusts work to observed results → update_task done/blocked/failed updates shared state.
- Boundary reachability: The shipped orco connect bridge actually starts configured local models from assigned tasks; the default bridge prompt and installed Claude-code skill prescribe this task-to-action lifecycle, rather than relying on the maintainer's development agents.
- Why this is / is not agent-owned: Deterministic orchestration delivers requests and enforces limits; the model chooses substantive work under those limits.
- Evidence: [bridge default/runner](https://github.com/CJVigil/Orco/blob/148f21d5a4dcf4f833e87d9fa38d3a1bfbe9df59/src/bridge/bridge.ts), [model adapter](https://github.com/CJVigil/Orco/blob/148f21d5a4dcf4f833e87d9fa38d3a1bfbe9df59/src/bridge/model.ts), [task API](https://github.com/CJVigil/Orco/blob/148f21d5a4dcf4f833e87d9fa38d3a1bfbe9df59/src/tasks.ts).
- Basis: explicit + structural
- Confidence: high for wired agent decision path; medium for behavior of the external model runtime.
- Caveats: No live external model credentials or end-to-end provider sessions were exercised in this review.

## S2 — Coordination

- State: A
- Function: Prevent parallel connected operational agents from modifying an incompatible shared resource at the same time, with feedback for changed agent behavior.
- Disturbance / variety regulated: Two simultaneously working agents both attempt to use the same branch, deployment target, migration or another named shared project resource.
- Decisive decision or feedback right: On resource conflict, choose wait, release/retry later or pick another task; decide when the shared resource can be relinquished.
- Decision owner: The involved model-bearing task agents in the shipped bridge prompt / integration skill. Deterministic lock service owns exclusion and fencing, not the discretionary response to denied access.
- Supporting / enforcement mechanisms: Project-scoped named lock holder, TTL, monotonically advanced fence, conflict response identifying holder and expiry, blocking wait helper and explicit acquire/release MCP tools.
- Closure path: Agent A obtains named lock → agent B sees conflict identifying holder/expiry → shipped model guidance makes B wait or change work rather than collide → lock expiry/release and subsequent acquire permit resumed work.
- Boundary reachability: The bridge's bundled DEFAULT_PROMPT explicitly requires acquire_lock/release_lock before touching shared resources; the distributed Claude-code Orco skill explicitly specifies waiting or picking different work after a conflict. Both are provided for ordinary supported agent connections.
- Distinct S1 units: Separate connected coding agents with independent task assignments and local model processes.
- Inter-S1 disturbance: Simultaneous work on a single branch, deployment target or migration.
- Attenuating coordination relation: Mutual-exclusion leases plus a returned lock-conflict signal that the model uses to alter its next activity.
- Feedback into subsequent S1 behaviour: The denied model changes task/order or waits until the holder releases, so following tool actions use a nonconflicting shared resource.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The named resource collision is concrete inter-agent interference; first-party lock acquisition, conflict disclosure and instructed behavioral change close a specific attenuation cycle.
- Why this is / is not agent-owned: Lock arithmetic and fencing are runtime enforcement, whereas agents choose the amended work schedule after feedback.
- Evidence: [locks](https://github.com/CJVigil/Orco/blob/148f21d5a4dcf4f833e87d9fa38d3a1bfbe9df59/src/locks.ts), [bridge prompt](https://github.com/CJVigil/Orco/blob/148f21d5a4dcf4f833e87d9fa38d3a1bfbe9df59/src/bridge/bridge.ts), [installed Orco skill](https://github.com/CJVigil/Orco/blob/148f21d5a4dcf4f833e87d9fa38d3a1bfbe9df59/integrations/claude-code/skills/orco/SKILL.md).
- Basis: explicit + structural
- Confidence: medium-high for standard connected agents and actual conflict return.
- Caveats: Lock discipline is advisory for code execution outside Orco; a noncompliant agent can bypass these project-scoped locks.

## S3 — Inside-and-now control

- State: C(P)
- Function: View current work commitments and failures across managed agents/projects and change live allocation, task priorities and intervention decisions.
- Disturbance / variety regulated: Stalled agent tasks, blocked tickets, overlapping priorities, waiting approvals, CI failure, overspend and missed current commitments.
- Decisive decision or feedback right: Decide which current work to reprioritize, pause, assign, unblock or escalate in light of portfolio/project state.
- Decision owner: Base constructor mode: a separately configured model supervisor asked by the operator to use the shipped project_plan, list_tickets and update_ticket tools (C); no such supervisor is installed by default. Parent mode: authenticated human org/project administrator viewing portfolio health and changing tickets/pauses/budgets (P).
- Supporting / enforcement mechanisms: Server-generated project plan and ticket summaries, cross-project health/roadmap/CI/approval/budget aggregation, ticket mutation API, scoped pause/budget control and audit events.
- Closure path: Base: constructed model supervisory session reads whole project open work and plan → decides reassignment/priority update → first-party ticket edits change connected agents' subsequent commitments. Parent: portfolio displays blocked/stalled/over-budget agents and tasks → admin decides assignment/priority/pause → persisted controls/tickets alter later bridge task starts and available work.
- Boundary reachability: First-party MCP ships the necessary project-wide read/update tools for a constructor-configured agent mode, while the first-party Orco human UI and controls route expose portfolio current state and authorized admin changes in normal self-hosted deployment; neither requires maintainer CI or a private service.
- Whole-system current view: For the base constructor, the accessible plan, tickets and dependencies of the selected Orco project (not a complete cross-instance view); for the parent, Portfolio.overview aggregates all visible projects' tickets, stalled agents, approvals, CI, budgets and milestone risk.
- Current-control decision scope: Assigning/updating task commitments, priority and workflow status, pausing selected agents/projects or all agents, and modifying operational budget limits in response to present problems.
- Why this is / is not agent-owned: The runtime computes health and enforces controls but does not select a supervisory response. An operator must construct an agent manager to own that discretionary S3 right; the shipped human-admin mode closes it without an autonomous manager.
- Evidence: [portfolio](https://github.com/CJVigil/Orco/blob/148f21d5a4dcf4f833e87d9fa38d3a1bfbe9df59/src/portfolio.ts), [MCP project/ticket actions](https://github.com/CJVigil/Orco/blob/148f21d5a4dcf4f833e87d9fa38d3a1bfbe9df59/src/mcp.ts), [tickets](https://github.com/CJVigil/Orco/blob/148f21d5a4dcf4f833e87d9fa38d3a1bfbe9df59/src/tickets.ts), [runtime controls](https://github.com/CJVigil/Orco/blob/148f21d5a4dcf4f833e87d9fa38d3a1bfbe9df59/src/controls.ts).
- Basis: structural + explicit
- Confidence: medium for constructor eligibility, high for human-admin closure.
- Caveats: C does not assert a first-party always-on autonomous supervisor. The portfolio view itself is informational until a legitimate admin/model decision changes work.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | Operator-constructed MCP-connected model supervisor | Model is tasked to inspect current project plan, ticket statuses and blockers | Model-chosen update_ticket / assignment / priority changes ensuing agent work | [MCP](https://github.com/CJVigil/Orco/blob/148f21d5a4dcf4f833e87d9fa38d3a1bfbe9df59/src/mcp.ts), [tickets](https://github.com/CJVigil/Orco/blob/148f21d5a4dcf4f833e87d9fa38d3a1bfbe9df59/src/tickets.ts) |
| Parent (`P`) | Human org/project administrator | Current portfolio flags stalled tasks, blockers, CI failure, spend or delayed approvals | Admin changes tickets, agent/project pauses or budgets; bridge reads new constraints | [portfolio](https://github.com/CJVigil/Orco/blob/148f21d5a4dcf4f833e87d9fa38d3a1bfbe9df59/src/portfolio.ts), [controls](https://github.com/CJVigil/Orco/blob/148f21d5a4dcf4f833e87d9fa38d3a1bfbe9df59/src/controls.ts) |

## S3* — Complementary audit

- State: A
- Function: A distinct connected review agent independently evaluates another agent's concrete work and returns corrective findings.
- Disturbance / variety regulated: A coding agent may declare a ticket complete despite defects or missing acceptance requirements.
- Decisive decision or feedback right: Review the actual ticket/workspace and choose approved or changes_requested with an explanatory note.
- Decision owner: A separately addressed model-bearing reviewer, not the original task agent. Human reviewers are also supported, but not used to upgrade agent ownership.
- Supporting / enforcement mechanisms: Requester != reviewer identity check, separate reviewer task and bridge wake, review status persistence, ticket review/rework transition and task restart.
- Closure path: Task agent requests review of ticket → separate reviewer agent receives a new explicit task to inspect the work and submit verdict → changes_requested writes review note, moves ticket to rework and starts original agent's work again; an agent approval records assessment while final done remains gated to a person.
- Boundary reachability: Reviews.request creates a real task for a named agent reviewer through first-party Tasks.create, which the shipped connected bridge executes; Reviews.submit directly implements rework and restart.
- Claim being audited: Work correctness and acceptance for a particular Orco task/ticket.
- Ordinary reporting path: Worker submits update_task done or ticket progress in its own thread.
- Complementary access path: A different agent's model run has a separate task identity, can read the project ticket/context and inspect actual workspace through its own configured coding CLI.
- Independence boundary: Reviewer cannot be the requester; it holds a different Orco participant identity and process. Institutional independence, different model provider and read-only file permissions are not guaranteed.
- Who acts on findings: The review subsystem moves the ticket to rework and starts the assigned coding agent again with the review note attached.
- Why this is / is not agent-owned: A reviewing LLM exercises the verdict; deterministic review/ticket machinery transmits the judgment and restarts work.
- Evidence: [reviews request, verdict and restart](https://github.com/CJVigil/Orco/blob/148f21d5a4dcf4f833e87d9fa38d3a1bfbe9df59/src/reviews.ts), [bridge](https://github.com/CJVigil/Orco/blob/148f21d5a4dcf4f833e87d9fa38d3a1bfbe9df59/src/bridge/bridge.ts), [ticket review path](https://github.com/CJVigil/Orco/blob/148f21d5a4dcf4f833e87d9fa38d3a1bfbe9df59/src/tickets.ts).
- Basis: explicit + structural
- Confidence: medium-high for optional first-party reviewer mode.
- Caveats: Review is not mandatory for every task. A separate agent identity alone does not prove critical rigor or provider independence; review quality is unmeasured here.

## S4 — Outside-and-then intelligence

- State: —
- Function: No shipped closed cycle that senses external/prospective change, selects adaptation to future capability and returns that selection to current operational repertoire.
- Disturbance / variety regulated: Future milestone risk, new follow-up work noticed during tasks and recurring job demand are recorded, but these are not independently established as future environment intelligence.
- Decisive decision or feedback right: Judge external/future environmental alternatives and adopt a changed capability or operating repertoire; not established.
- Decision owner: Humans manage milestones, accept follow-up suggestions and approve schedules; ordinary connected agents can propose work and schedules but do not hold a shipped adaptation mandate.
- Supporting / enforcement mechanisms: Portfolio cross-project roadmap, dated milestones, agent suggestions with optional owner-authorized ticket filing, scheduled recurring tasks and human approvals.
- Closure path: Agent can suggest a follow-up → owner accepts into backlog (or an allowed automatic ticket is filed), and scheduled tasks can later run; no documented installed step converts future outside-environment analysis into a selected capability adaptation that returns to operations.
- Why this is / is not agent-owned: Backlog intake, forecast risk labels and repeat execution do not alone imply outside-and-then strategy or a governed capability change.
- Evidence: [suggestions](https://github.com/CJVigil/Orco/blob/148f21d5a4dcf4f833e87d9fa38d3a1bfbe9df59/src/suggestions.ts), [schedules](https://github.com/CJVigil/Orco/blob/148f21d5a4dcf4f833e87d9fa38d3a1bfbe9df59/src/schedules.ts), [portfolio roadmap](https://github.com/CJVigil/Orco/blob/148f21d5a4dcf4f833e87d9fa38d3a1bfbe9df59/src/portfolio.ts), [MCP milestone operations](https://github.com/CJVigil/Orco/blob/148f21d5a4dcf4f833e87d9fa38d3a1bfbe9df59/src/mcp.ts).
- Basis: explicit + structural
- Confidence: medium, bounded to the shipped first-party standard distribution.
- Caveats: A human organization using Orco can implement strategic analysis externally; no universal claim against that larger system.

### Absence scope

- Surfaces inspected: Portfolio roadmap/risk forecasting, milestones and project plans, agent follow-up suggestions/filing, recurring schedules and their owner approval, task/bridge prompts, MCP project actions and stored policy controls.
- Plausible first-party paths checked: Risk flags leading to milestone changes, follow-up suggestions returning as new tickets, agent-proposed recurring work, operator-written future plans, and human budget/priority adjustments.
- Why no material first-party path remains: These paths manage an internal roadmap, request/backlog intake or future repetition of already configured tasks. None contains an installed external-environment intelligence/adaptation decision that changes future organizational capabilities and returns it to present operational regulation.

## S5 — Policy and identity

- State: P
- Function: Legitimate human parent authority establishes organization-wide and project-specific enduring operating identity/rules and returns binding decisions to subsequent agent work.
- Disturbance / variety regulated: Conflicting agent freedoms, project-local exceptions, unsafe spending/deploy authority and mismatch between organizational mandate and project execution.
- Decisive decision or feedback right: Define or revise authoritative organizational/project rules, required approvals, allowed operational agents and persistent task-budget policy; subordinate projects may tighten but may not relax org constraints.
- Decision owner: Authenticated human organization administrator or project administrator; first-party Policies.set refuses agents and applies scope checks.
- Supporting / enforcement mechanisms: Persisted org/project policy, mergePolicy inheritance/tightening, agent bridge prompt policy lines, new-task admission and budget validation, audit trail and controls event.
- Closure path: Admin receives governance need and sets org/project policy → it is persisted and scoped into the effective project mandate → new task creation rejects forbidden agents/excess budgets; later bridge prompts include binding rules and approval requirements → subsequent agent operation reflects the decision.
- Boundary reachability: The first-party self-hosted server exposes Policies.set to authenticated administrators and directly calls effective policy at task admission and rulesFor in connected-agent contexts. This path is shipped, not an assumed external user-written AGENTS.md.
- Identity / ultimate-policy issue: Which agents and actions the ongoing project/organization authorizes, which approvals remain nondelegable and what spending or time rights every new agent task receives.
- Ultimate authority in each claimed mode: In the one credited parent mode, org administrator sets binding server-wide rules and project administrator sets only narrower local rules; the policy setter rejects model agents outright.
- Return-to-operation path: Stored administrator decision is combined into effective policy; new-task admission enforces the eligible agents and budget caps, and subsequent connected-agent task context receives policy rules and approval requirements.
- Why this is / is not agent-owned: Only a legitimate human admin has authority to change the continuing constitution; agents execute within its returned constraints. Discretionary governance remains at the parent recursion.
- Evidence: [policies](https://github.com/CJVigil/Orco/blob/148f21d5a4dcf4f833e87d9fa38d3a1bfbe9df59/src/policies.ts), [bridge context and rules](https://github.com/CJVigil/Orco/blob/148f21d5a4dcf4f833e87d9fa38d3a1bfbe9df59/src/bridge/bridge.ts), [task admission](https://github.com/CJVigil/Orco/blob/148f21d5a4dcf4f833e87d9fa38d3a1bfbe9df59/src/tasks.ts).
- Basis: explicit + structural
- Confidence: high for hierarchy/admission/prompt return; lower for compliance with textual rules by an external model.
- Caveats: Plain-language policy obedience depends on provider behavior; allowed agent lists and budget caps have stronger deterministic enforcement.

## Distributed OSS parent arrangement

The GitHub repository, maintainers and release CI are excluded from the runtime organization. The credited parent is the actual authenticated Orco org/project administrator in a deployed server. Neither a repository maintainer nor the human who originally wrote a coding task is silently promoted to S3/S4/S5 for every agent run.

## Self-hosted and non-human modes

Orco is self-hostable and supports multiple local/hosted connected models. Agent-to-agent task requests, lock response and agent review use autonomous operational units. Human admins retain policy and normal portfolio control. A constructor can arrange project-wide model-supervised S3 by giving an MCP-connected agent that mandate, but the distribution does not install such an autonomous org manager by default.

## Recursion

The declared system is the Orco-managed project/organization and its distinct connected agents. Ticket-level task decomposition and a reviewer task are relationships inside that boundary, not proof of a further viable recursive organization. The org policy authority is hierarchically above project-specific rules, while individual bridge sessions remain subordinate to task consent.

## Variety and escalation

Multiple connected models/workspaces and per-project task controls amplify operational variety. Named resource locks attenuate concurrent collision; separate reviewer verdicts return corrective variety into subsequent tasks. Task queues, approvals, stalled-task alerts and portfolio health bring current exceptions to human administrators. Enduring org/project policy and new-task admission close the parent-governed S5 return. Roadmap risk indicators lack an evidenced future capability-adaptation closure.

## Evidence gaps

- This is a source-pinned assessment; no external model/API credentials were used to run live bridge, lock-contention and reviewer experiments. Deterministic repository validation does not substitute for provider outcome testing.
- Reviewer identity is distinct from requester, but there is no enforced different model provider, external auditor or read-only workspace; S3* represents the optional structurally shipped independent model-task review path, not independent institutional certification.
- S3=C is conditional on an explicitly constructed MCP-connected supervisory agent with whole-project context. The review does not assert a preinstalled automatic organization manager.
- The bounded S4 absence does not preclude custom externally instructed strategy or downstream autonomous add-ons.

## Assessment result

Included as an agentic harness: substantive work is model-owned through shipped connected bridges and tools. Pinned vector: S1=A, S2=A, S3=C(P), S3*=A, S4=—, S5=P.

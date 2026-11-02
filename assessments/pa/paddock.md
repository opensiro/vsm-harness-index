---
harness_id: paddock
project_name: Paddock
repository: https://github.com/vakovalskii/paddock
review_ref: 96e9b43cd194012599b0608faeb9cd2befa9fee1
reviewed_at: 2026-11-02
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Paddock

## Review boundary

- System in focus: the shipped self-hosted Paddock web cockpit, its per-user Codex app-server harness container, and the optional first-party `paddock-agents` tool installed into that harness; not an imagined future multi-harness fleet.
- Purpose and identity: give each authenticated user isolated browser control of several persistent autonomous coding-agent sessions, with tool invocation, streamed results, and optional communication among that user's sessions.
- Relevant environment: user workspaces and task requests, code/tool observations, other simultaneously active chats, model/account providers, approvals, network connectivity, proxy health and container deployment.
- Standard-distribution boundary: `docker-compose.yml`, `codex/` harness image and entrypoint, the `web/` UI/WS relay and tool-install route, `web/tools/agents/` transport, and documented self-hosted container-per-user mode. Codex itself is an upstream model/tool agent engine, installed as a runtime dependency.
- Credited operating / distribution surfaces: `codex/Dockerfile`, `codex/entrypoint.sh`, `web/server.ts`, `web/lib/codex-client.ts`, `web/lib/tools.ts`, `web/tools/agents/{SKILL.md,paddock-agents.mjs}`, `web/components/pane.tsx`, `docker-compose.yml` and authenticated deployed sessions.
- Adjacent first-party surfaces excluded from ownership: repository contributor/maintainer workflows, `CLAUDE.md` development instructions, operator's ad hoc dogfood agent, CI/browser tests, `web/supervisor.sh` build deployment checks, screenshot fixtures, and explicitly unimplemented roadmap items. The external Codex app-server/LLM owns its lower-level model/tool planning.
- First-party operating / deployment modes considered: deployed per-user Codex app-server behind authenticated web WS proxy; one to four simultaneous chat panes; agent-messaging tool when enabled; optional standalone tmux transport; administrator configuration and self-deploy workflow. No live provider account, production VPS or browser E2E was exercised in this review.
- Recursion level: a Paddock user/workspace installation hosting concurrent coding-agent sessions as S1 cells; isolated installations for other users and Codex's internal subagent machinery are distinct/lower boundaries.
- Reviewed revision: `vakovalskii/paddock@96e9b43cd194012599b0608faeb9cd2befa9fee1` (GitHub repository ID 1437982846), frozen by candidate intake #2578 and controller #2579.
- Observation date: 2026-11-02.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The [README](https://github.com/vakovalskii/paddock/blob/96e9b43cd194012599b0608faeb9cd2befa9fee1/README.md) expressly calls Paddock an infrastructure/web cockpit, not a separately authored agent engine. Its [architecture](https://github.com/vakovalskii/paddock/blob/96e9b43cd194012599b0608faeb9cd2befa9fee1/docs/reference/architecture.md) and [harness service contract](https://github.com/vakovalskii/paddock/blob/96e9b43cd194012599b0608faeb9cd2befa9fee1/docs/services/harness/README.md) give every user an isolated Codex app-server container, persistent home/workspace volumes, no direct internet, and a token-authenticated WebSocket through a shared browser UI. The [Codex bridge](https://github.com/vakovalskii/paddock/blob/96e9b43cd194012599b0608faeb9cd2befa9fee1/web/lib/codex-client.ts) relays thread/turn/item/approval/usage calls and notifications, while the [tools installer](https://github.com/vakovalskii/paddock/blob/96e9b43cd194012599b0608faeb9cd2befa9fee1/web/lib/tools.ts) writes optional CLI-and-skill tools to the agent's harness home. The [agents CLI](https://github.com/vakovalskii/paddock/blob/96e9b43cd194012599b0608faeb9cd2befa9fee1/web/tools/agents/paddock-agents.mjs) lists, reads, sends, waits for and replies to other Codex chats or tmux panes, routing to `turn/steer`, `turn/start`, or terminal paste. It prevents messaging oneself, plain shells and approval prompts and caps chained messages at five hops. These are transport/safety constraints, not a collective task arbiter. The [architecture roadmap](https://github.com/vakovalskii/paddock/blob/96e9b43cd194012599b0608faeb9cd2befa9fee1/docs/plans/roadmap.md) separately identifies autonomous queues, dispatches, worktrees, decision gates and multi-node fleet as future work. The repository has an [agent exchange browser test](https://github.com/vakovalskii/paddock/blob/96e9b43cd194012599b0608faeb9cd2befa9fee1/tests/agents.mjs) and [tmux simulated test](https://github.com/vakovalskii/paddock/blob/96e9b43cd194012599b0608faeb9cd2befa9fee1/tests/agents-tmux.mjs), neither of which tests conflict-regulation ownership.

## Operational model

Each running model-driven Codex session interprets a user goal, chooses coding/tool steps and observes responses. Paddock authenticates users, isolates persistence and networking, mediates approvals, renders events and optional agent-to-agent requests. A user may independently run several chats or ask one to solicit an answer/review from another; no shipped first-party planner supervises the whole set of commitments. Separate users have distinct containers; the common egress bridge is infrastructure, not an inter-user VSM metasystem.

## S1 — Operations

- State: A
- Function: perform substantive autonomous coding/tool work within persistent per-user project sessions using the installed Codex harness.
- Disturbance / variety regulated: varied natural-language coding goals, changing workspace files, shell/tool outputs, model observations, interruptions and approvals.
- Decisive decision or feedback right: select the next model/tool operation and continue or revise a coding task from feedback within one agent session.
- Decision owner: the model-driven Codex agent, composed into the supported first-party per-user harness mode; users assign tasks and approve privileged acts.
- Supporting / enforcement mechanisms: authenticated WS proxy, per-user Docker container/volumes, pane thread selectors, status bar, tools installer, approval relay and proxy chain.
- Closure path: authenticated browser `turn/start` → web relay → Codex app-server's model/tool session → streamed item/approval/result messages → session history and user follow-up.
- Boundary reachability: `codex/entrypoint.sh` launches Codex app-server for the installed image; `web/lib/codex-client.ts` and the documented pane UI call its live protocol. These are supported deployment components, not test fixtures.
- Why this is / is not agent-owned: without the imported model/tool agent, Paddock provides a secure UI and transport but cannot independently choose task-relevant coding actions.
- Evidence: [README](https://github.com/vakovalskii/paddock/blob/96e9b43cd194012599b0608faeb9cd2befa9fee1/README.md), [Codex entrypoint](https://github.com/vakovalskii/paddock/blob/96e9b43cd194012599b0608faeb9cd2befa9fee1/codex/entrypoint.sh), [Codex WS bridge](https://github.com/vakovalskii/paddock/blob/96e9b43cd194012599b0608faeb9cd2befa9fee1/web/lib/codex-client.ts).
- Basis: structural
- Confidence: high
- Caveats: agent planning is upstream Codex, not Paddock-authored; no paid-provider/live browser execution in this assessment.

## S2 — Coordination

- State: —
- Function: no shipped conflict-specific regulation among distinct operational sessions with subsequent cross-cell feedback is demonstrated.
- Disturbance / variety regulated: potential conflicting edits, duplicated work, inconsistent answers and concurrent agents acting in one workspace; all are plausible but not attenuated by a demonstrated S2 loop.
- Decisive decision or feedback right: select a resolution of actual inter-agent interference, then change at least one cell's subsequent behavior; no first-party coordination owner/constructor is established.
- Decision owner: individual asking and receiving agents choose message content/actions, or the human organizes tasks. The CLI only transports messages and returns replies.
- Supporting / enforcement mechanisms: `paddock-agents list/read/send/reply`, `--wait`, busy-turn steering, tmux paste, hop ceiling, approval-prompt refusal, per-user isolation and four-pane layout.
- Closure path: one agent can ask another and receive an answer, but no documented conflict detector, arbitration rule, decision right or regulatory feedback path handles interference between their active goals.
- Why this is / is not agent-owned: ordinary delegation, review request, message delivery and visibility do not themselves satisfy the required inter-S1 conflict/oscillation attenuation condition.
- Evidence: [agent tool instructions](https://github.com/vakovalskii/paddock/blob/96e9b43cd194012599b0608faeb9cd2befa9fee1/web/tools/agents/SKILL.md), [transport source](https://github.com/vakovalskii/paddock/blob/96e9b43cd194012599b0608faeb9cd2befa9fee1/web/tools/agents/paddock-agents.mjs), [agents browser test](https://github.com/vakovalskii/paddock/blob/96e9b43cd194012599b0608faeb9cd2befa9fee1/tests/agents.mjs), [future dispatch plan](https://github.com/vakovalskii/paddock/blob/96e9b43cd194012599b0608faeb9cd2befa9fee1/docs/plans/roadmap.md).
- Basis: structural
- Confidence: medium
- Caveats: a user could manually devise a conflict protocol using messages, but that configuration is not first-party shipped as a functionally closed standard mode.

### Absence scope

- Surfaces inspected: `paddock-agents` source and skill, browser/tmux agent messaging tests, chat pane/protocol architecture, workspace/isolation design and roadmap.
- Plausible first-party paths checked: cross-pane messages, shared folder edits, `--wait` review handoff, hop guard, preventing paste into approval prompts, future queue/worktree/dispatch features.
- Why no material first-party path remains: shipped behavior implements communication and safety but not a specific conflict-sensitive coordination judgment with feedback into subsequent S1 commitments; prospective queue/worktree arbitration is marked unimplemented.

## S3 — Inside-and-now control

- State: —
- Function: no demonstrated first-party whole-user operational-control loop that decides shared priorities, commitments or resource trades across working agents.
- Disturbance / variety regulated: simultaneous busy/idle/approval states, per-user CPU/memory limits, workspace contention, network availability and token budgets.
- Decisive decision or feedback right: dynamic portfolio intervention/reallocation based on a whole-system current assessment is not shown; static limits and user task/stop choices are not that right.
- Decision owner: user/admin chooses tasks and configures container limits; proxy and app-server enforce policies. No autonomous current-control owner or qualifying parent S3 return is wired.
- Supporting / enforcement mechanisms: status bar and pane state, Docker limits, egress health feed, manual stop/approve, chat archive and account settings.
- Closure path: state is displayed to the user and individual turns may stop/resume; there is no surfaced current-control assessment → legitimate whole-user decision → changed allocation/commitment loop.
- Why this is / is not agent-owned: eliminating any putative supervisor agent leaves UI statuses and static resource gates intact; no such supervisor makes cross-session discretionary control choices.
- Evidence: [architecture](https://github.com/vakovalskii/paddock/blob/96e9b43cd194012599b0608faeb9cd2befa9fee1/docs/reference/architecture.md), [UI/capabilities](https://github.com/vakovalskii/paddock/blob/96e9b43cd194012599b0608faeb9cd2befa9fee1/README.md), [roadmap](https://github.com/vakovalskii/paddock/blob/96e9b43cd194012599b0608faeb9cd2befa9fee1/docs/plans/roadmap.md).
- Basis: structural
- Confidence: medium
- Caveats: an operator can exercise external management discretion, but source does not show a distinct in-boundary feedback-closed first-party parent mode.

### Absence scope

- Surfaces inspected: resource/container documents, UI status and action feeds, agent communication, deployment and roadmap.
- Plausible first-party paths checked: four-pane overview, per-user quotas, status/usage graphs, admin setup, messaging, turn stop and agent-based UI self-deployment.
- Why no material first-party path remains: observation and local task control do not demonstrate a whole-current commitment/resource authority loop; queue/dispatch, fleet allocation and decision gates remain roadmap items.

## S3* — Complementary audit

- State: —
- Function: no first-party independent complementary reality check with corrective authority over operational claims is closed in the deployed user/agent mode.
- Disturbance / variety regulated: false agent result claims, mistaken edits, tool output omissions and deployment regressions.
- Decisive decision or feedback right: an independent audit owner determining contradictory evidence and forcing corrective operations is not supplied.
- Decision owner: ordinary worker agent or a second agent selected by the user may review by request; that is ad hoc task delegation, not enforced independent audit judgment/return.
- Supporting / enforcement mechanisms: agent message/read tool, action logs and diffs, per-turn usage, security restrictions, browser tests and admin deployment rollback.
- Closure path: logs and optional review replies reach their users/askers; no independent audit verdict constrains acceptance and loops back into an autonomous task with first-party authority.
- Why this is / is not agent-owned: no audit-specific separation, contradictory evidence path or mandatory correction is present; E2E tests audit project development, not standard user-agent outputs.
- Evidence: [agent tool](https://github.com/vakovalskii/paddock/blob/96e9b43cd194012599b0608faeb9cd2befa9fee1/web/tools/agents/SKILL.md), [tests](https://github.com/vakovalskii/paddock/blob/96e9b43cd194012599b0608faeb9cd2befa9fee1/tests/agents.mjs), [architecture](https://github.com/vakovalskii/paddock/blob/96e9b43cd194012599b0608faeb9cd2befa9fee1/docs/reference/architecture.md).
- Basis: structural
- Confidence: medium
- Caveats: a user may recruit a separate reviewer agent, which does not by itself establish the first-party complementary-audit function.

### Absence scope

- Surfaces inspected: agent messaging CLI/skill, pane result rendering, action feed, live deployment supervisor descriptions and shipped tests.
- Plausible first-party paths checked: review request/response, independent chat, per-turn tool history, destructive-command approval, automatic web build rollback and E2E regression tests.
- Why no material first-party path remains: these are request-directed work, audit-adjacent evidence capture or contributor/deployment checks; no operationally enforced independent audit finding and corrective return is shipped.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party external/prospective adaptation process with authoritative choice and returned new present capability is demonstrated for the multi-chat organization.
- Disturbance / variety regulated: changing model providers, new harness integrations, proxy quality, feature demand and future hosting capacity.
- Decisive decision or feedback right: choosing changes to the present operating model from environmental/future analysis is not performed by a designated S4 agent/parent loop.
- Decision owner: maintainer/admin edits and deploys infrastructure; users select models/tools, and external agents can perform ordinary requested coding tasks.
- Supporting / enforcement mechanisms: provider picker, network health probes, tool refresh/install, supervisor build switch/rollback and documented future adapters/fleet.
- Closure path: a user or developer can update a tool/build, but source does not wire external future sensing → adaptation evaluation → decision → present systemic capability change as a closed first-party mode.
- Why this is / is not agent-owned: model selection and agent-assisted UI edits are operational/development work; these lack an independently established S4 option-judgment owner.
- Evidence: [roadmap](https://github.com/vakovalskii/paddock/blob/96e9b43cd194012599b0608faeb9cd2befa9fee1/docs/plans/roadmap.md), [tools installation](https://github.com/vakovalskii/paddock/blob/96e9b43cd194012599b0608faeb9cd2befa9fee1/web/lib/tools.ts), [architecture](https://github.com/vakovalskii/paddock/blob/96e9b43cd194012599b0608faeb9cd2befa9fee1/docs/reference/architecture.md).
- Basis: structural
- Confidence: medium
- Caveats: human-led OSS strategic development exists above the reviewed runtime boundary; unshipped fleet and adapter goals cannot be credited.

### Absence scope

- Surfaces inspected: first-party architecture, deployment path, tool registry, model/provider selectors, network feed, roadmap and harness protocol.
- Plausible first-party paths checked: optional model/tool changes, admin self-deploy, proxy failover, prospective multi-harness protocol and planned fleet migration.
- Why no material first-party path remains: the shipped paths administer or safeguard capability chosen elsewhere; no prospective outside-and-then option-selection loop returns an evidenced S4 decision into whole-installation control.

## S5 — Policy and identity

- State: —
- Function: no first-party identity/ultimate-policy deliberation with legitimate authority and operational return is established within the agent organization.
- Disturbance / variety regulated: login policy, 2FA, user isolation, model access, approval settings, tool privileges and administrator permissions.
- Decisive decision or feedback right: arbitration of the organization's identity or ultimate commitments and a binding governance return is not implemented as a function-specific process.
- Decision owner: human administrators choose static login/configuration policy; authentication and privilege code enforce it, not an autonomous or returned parent S5 judgment loop.
- Supporting / enforcement mechanisms: password/TOTP gate, capability token, per-user isolation, execution policy rules and approval prompts.
- Closure path: configured access controls affect operations, but no identity-level signal → qualified governing authority → deliberative policy choice → corrective operational return is shown.
- Why this is / is not agent-owned: remove agents and the static access-control machinery remains; no agent decides what the whole organization is for or what ultimate rule should prevail.
- Evidence: [architecture](https://github.com/vakovalskii/paddock/blob/96e9b43cd194012599b0608faeb9cd2befa9fee1/docs/reference/architecture.md), [harness service docs](https://github.com/vakovalskii/paddock/blob/96e9b43cd194012599b0608faeb9cd2befa9fee1/docs/services/harness/README.md), [README](https://github.com/vakovalskii/paddock/blob/96e9b43cd194012599b0608faeb9cd2befa9fee1/README.md).
- Basis: structural
- Confidence: medium
- Caveats: owner/admin policy and public repository maintainer governance are not automatically an assessed first-party S5 parent loop.

### Absence scope

- Surfaces inspected: security/authentication docs, access/token code architecture, execution approval, user/admin configuration, deployment supervisor and roadmap.
- Plausible first-party paths checked: account creation, 2FA, admin permission, hard execpolicy, stop/approve prompts, user isolation and maintainer policy.
- Why no material first-party path remains: security policy is configured and enforced, but no in-boundary ultimate-policy issue is considered by an authority and returned through an evidenced identity-level decision loop.

## Distributed OSS parent arrangement

Independently self-hosting users and public repository contributors are not a single operational metasystem. The instance administrator controls service accounts and deployment; the GitHub maintainer controls code governance. Neither surface is automatically a first-party S3/S4/S5 parent feedback mode at the declared per-user multi-session recursion.

## Self-hosted and non-human modes

The documented self-hosted Docker mode is the primary mode. Its model-driven coding runs are real S1 operations, while app-server internals remain upstream. Optional agent messaging is agent-initiated but task-generic; the product does not ship a non-human conflict supervisor, auditor or policy governor. tmux transport can expose external local agent panes but does not enlarge the deployed Paddock organization's first-party decision rights.

## Recursion

One user operates several coding-agent sessions and may have Codex subagents inside one session. Multiple panes/containers and subagent nesting alone are not evidence of separately viable recursively closed systems; distinct user installations have distinct operational authority.

## Variety and escalation

Authentication, isolated volumes, adapter calls, persistent thread histories, approval relay, optional message transport and proxy health attenuate task/hosting variety. A status/approval card is a regular operational signal, not proof of a distinct algedonic metasystem escalation channel.

## Evidence gaps

The Codex model/tool planner is an imported runtime dependency and not audited here as Paddock-authored logic. The optional first-party agent messaging path was source- and test-inspected, but no live logged-in multi-chat/provider E2E was executed. The repository tests include browser-driven examples but are not equivalent to reproduced live runtime behavior. No supported first-party conflict-resolving S2 workflow or S3–S5 closure can be inferred from the future roadmap.

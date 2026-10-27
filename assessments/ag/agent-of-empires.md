---
harness_id: agent-of-empires
project_name: Agent of Empires
repository: https://github.com/agent-of-empires/agent-of-empires
review_ref: 81d4672a846798d0a9b02183d9dce83ea6bf6917
reviewed_at: 2026-10-27
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

# Agent of Empires

## Review boundary

- System in focus: one local Agent of Empires (AoE) session-management installation with its single-user Daemon, TUI/CLI/Web clients and supported managed coding-agent sessions, including tmux and structured ACP execution, optional git worktrees and sandboxing.
- Purpose and identity: run several AI coding-agent sessions persistently, let a human/operator or external dispatcher create and monitor them, and separate their execution environments where configured.
- Relevant environment: human task prompts, repository and git state, external installed Claude/Codex/Gemini/OpenCode/Kimi/other agent CLIs and their model/tool providers, tmux/process failures, session state, approvals, API callers and optional container/worktree runtimes.
- Standard-distribution boundary: published AoE binary/Daemon and the supported operating mode in which AoE launches and maintains external autonomous coding-agent processes. Their opaque model/tool internals are external substrate; their active coding work is S1 within the intentionally assembled managed-session runtime. No private agent metasystem is imported as AoE's S2–S5.
- Credited operating / distribution surfaces: agent command registry; Daemon session creation/spawn and status handling; tmux and ACP worker sessions; CLI/TUI/Web/API lifecycle; optional worktree creation and working-directory binding; storage, approvals and status callbacks.
- Adjacent first-party surfaces excluded from ownership: the separate CityHall multi-user organization and its governance/audit, contributor and maintainer workflows, marketing/website, installer/CI/test/release tools, optional community skills/plugins and external orchestration software using the AoE API. Shipped opt-in worktrees count as a supported mode, not as a mandatory default.
- First-party operating / deployment modes considered: plain persistent tmux coding-agent sessions; structured ACP sessions; one or several simultaneous sessions; optional branch/worktree or multi-repository workspace separation; sandbox execution; TUI/CLI/Web and external HTTP callers; restart/resume and status callbacks.
- Recursion level: one AoE-managed local set of coding sessions/workspaces, where each hosted autonomous coding-agent session performs its own task as an S1 unit. The Daemon and clients are common harness machinery, not a separate agent making coding decisions.
- Reviewed revision: `81d4672a846798d0a9b02183d9dce83ea6bf6917`.
- Observation date: 2026-10-27.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

AoE launches a configured coding-agent executable inside a persistent tmux session or a structured ACP worker. Its agent registry, session builder, Daemon and ACP supervisor select/resolve executable commands, create or resume session records, attach a working directory and expose terminal/structured status to TUI, web and CLI clients. The hosted agent, not AoE's session controller, selects coding actions and responds to the repository and tool feedback. The session manager can observe Running/Waiting/Idle/Error, transport prompts, restart processes and preserve conversation bindings, but it does not thereby own the agent's task policy.

For parallel sessions, the optional first-party worktree mode creates a distinct branch/checkout per configured task and starts the corresponding agent inside that path. This structurally attenuates collisions over a shared mutable checkout; AoE also serializes simultaneous API send requests for the *same* session to avoid interleaved keystrokes. The latter is one-session input safety, not by itself S2 among distinct S1 units. Callback events let an **external** dispatcher react to status; the dispatcher is not built into the AoE-owned whole-system control loop.

Pinned primary evidence: [README](https://github.com/agent-of-empires/agent-of-empires/blob/81d4672a846798d0a9b02183d9dce83ea6bf6917/README.md), [agent registry](https://github.com/agent-of-empires/agent-of-empires/blob/81d4672a846798d0a9b02183d9dce83ea6bf6917/src/agents.rs), [session plan and provisioning](https://github.com/agent-of-empires/agent-of-empires/blob/81d4672a846798d0a9b02183d9dce83ea6bf6917/src/session/builder.rs), [tmux launch](https://github.com/agent-of-empires/agent-of-empires/blob/81d4672a846798d0a9b02183d9dce83ea6bf6917/src/session/instance/start.rs), [structured spawn](https://github.com/agent-of-empires/agent-of-empires/blob/81d4672a846798d0a9b02183d9dce83ea6bf6917/src/server/session_spawn.rs), [API reference](https://github.com/agent-of-empires/agent-of-empires/blob/81d4672a846798d0a9b02183d9dce83ea6bf6917/docs/api.md).

## Operational model

An operator or API caller creates a session and chooses a configured coding-agent tool, target repository, task and optional worktree. AoE provisions the environment and starts the executable or ACP worker. The agent then autonomously interprets its coding task and uses its own tool/model loop, while AoE transports later messages and reports activity and output. Several such sessions can run concurrently with separate worktrees. A human or external dispatcher may inspect, reprompt, stop or restart sessions, but the shipped Daemon does not interpret the portfolio and autonomously rebalance commitments.

## S1 — Operations

- State: A
- Function: supported managed coding-agent sessions perform task-local coding and tool work on the designated repository/environment.
- Disturbance / variety regulated: heterogeneous code requests, changing files, tool/test feedback, missing context, model responses and task-specific failures.
- Decisive decision or feedback right: the hosted autonomous coding agent decides what coding/tool action to take next based on its prompt and subsequent feedback, and when to continue or finish.
- Decision owner: the supported external coding-agent process acting as the S1 operational unit inside AoE's standard assembled session mode; AoE does not own its internal model or tool policy.
- Supporting / enforcement mechanisms: AoE agent registry, command/profile resolution, tmux/ACP launch, daemon persistence, prompt forwarding, session IDs, environment/worktree/sandbox bindings and status detection.
- Closure path: caller creates/prompts an AoE session → AoE launches the chosen autonomous coding agent in the intended working directory → agent executes task-selected code/tool operations and observes results → agent continues/revises/finishes → AoE captures status/output.
- Boundary reachability: the README quick start explicitly starts `aoe add --cmd claude`; the shipped session builder and tmux/ACP launch paths instantiate configured external agent commands rather than merely describing a hypothetical integration.
- Why this is / is not agent-owned: removing the hosted coding-agent executable while leaving the Daemon, tmux and status UI leaves a session manager but no actor that autonomously chooses coding actions. Only this S1 actor is credited; its undisclosed private metasystem is not.
- Evidence: [quick start](https://github.com/agent-of-empires/agent-of-empires/blob/81d4672a846798d0a9b02183d9dce83ea6bf6917/docs/quick-start.md), [registry](https://github.com/agent-of-empires/agent-of-empires/blob/81d4672a846798d0a9b02183d9dce83ea6bf6917/src/agents.rs), [launch](https://github.com/agent-of-empires/agent-of-empires/blob/81d4672a846798d0a9b02183d9dce83ea6bf6917/src/session/instance/start.rs), [ACP supervisor resolution](https://github.com/agent-of-empires/agent-of-empires/blob/81d4672a846798d0a9b02183d9dce83ea6bf6917/src/acp/supervisor/agents.rs).
- Basis: structural and documented.
- Confidence: high for reachability and actor ownership.
- Caveats: no live provider-backed coding-agent task was executed; external agent performance and internals were not audited.

## S2 — Coordination

- State: C
- Function: optional managed worktree isolation attenuates shared-checkout interference among separately executing S1 coding sessions of one repository/workspace.
- Distinct S1 units: two or more AoE-managed coding-agent sessions separately operating on tasks that reference the same source repository.
- Inter-S1 disturbance: without separation, concurrent writes, index operations and branch checkout changes in the same mutable git working tree can contaminate or overwrite another agent's work.
- Attenuating coordination relation: the first-party session plan creates a branch and independent git worktree before the corresponding agent is started there; multi-repo workspace provisioning applies the same separation for its constituent repositories.
- Feedback into subsequent S1 behaviour: the session's resolved project path/worktree becomes the launched agent's working directory, so later coding actions occur against its separate checkout; failed or conflicting provisioning is reported/refused rather than silently sharing an unintended target.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the witness is the concrete collision class of simultaneously mutating one checkout and the first-party workspace isolation that directly prevents it, not session listing, generic APIs or sequential commands.
- Disturbance / variety regulated: parallel git/file modifications and workspace-state collisions across operational sessions.
- Decisive decision or feedback right: choose/provision distinct branch/worktree paths for the configured sessions, preventing direct cross-agent checkout interference.
- Decision owner: operator/constructor configuration and deterministic AoE worktree provisioning. AoE supplies a first-party S2-specific coordination path, but no autonomous agent owns the decision to choose/revise this response across sessions, hence `C`.
- Supporting / enforcement mechanisms: `InstancePlan::provision`, `GitWorktree::create_worktree_tracked`, unique worktree directories, recorded branch/worktree ownership and cleanup/reconciliation guards.
- Closure path: two concurrent sessions target the repository → opt-in branch/worktree construction separates their mutable checkout paths → each S1 agent is launched within its assigned worktree → work proceeds without competing for the same git index/working directory.
- Boundary reachability: `aoe add -w ... -b`, the TUI worktree checkbox and the Web wizard are supported user-facing modes; the builder invokes the git worktree implementation on the actual session-creation path.
- Why this is / is not agent-owned: isolation is selected by the caller and executed deterministically, not negotiated or adaptively revised by one of the coding agents. The per-session API send mutex only prevents keystroke interleaving and is not this inter-S1 witness.
- Evidence: [worktree guide](https://github.com/agent-of-empires/agent-of-empires/blob/81d4672a846798d0a9b02183d9dce83ea6bf6917/docs/guides/worktrees.md), [session builder](https://github.com/agent-of-empires/agent-of-empires/blob/81d4672a846798d0a9b02183d9dce83ea6bf6917/src/session/builder.rs), [git worktree create](https://github.com/agent-of-empires/agent-of-empires/blob/81d4672a846798d0a9b02183d9dce83ea6bf6917/src/git/worktree/create.rs), [API send isolation](https://github.com/agent-of-empires/agent-of-empires/blob/81d4672a846798d0a9b02183d9dce83ea6bf6917/docs/api.md).
- Basis: structural.
- Confidence: high for optional worktree-mode isolation, not for global task coordination.
- Caveats: worktree mode is not mandatory by default; separate checkouts do not solve logical merge conflicts or task dependency negotiation.

## S3 — Inside-and-now control

- State: —
- Function: no first-party whole-multi-session controller with a current operational picture and decisive adaptive regulation of shared commitments/resources was established.
- Disturbance / variety regulated: competing session priorities, failed/idle agents, capacity limits and unfinished tasks can require whole-workspace current intervention.
- Decisive decision or feedback right: callers choose tool/profile, start/stop/restart/send commands and inspect the status board; the Daemon enforces lifecycle reservations and transports status rather than deciding portfolio-wide priority or resource bargains.
- Decision owner: individual human/API caller for task/session choices, deterministic Daemon for lifecycle enforcement; no established S3 agent or S3-specific autonomous constructor/closed parent mode at the declared recursion.
- Supporting / enforcement mechanisms: session list/status, Daemon store, callback webhooks, lifecycle generations, ACP supervisor, process restart/idle tracking, UI/API controls.
- Closure path: a status event can reach a human or an **external** dispatcher for a new session command; no packaged internal controller interprets all current S1 commitments and returns adaptive whole-system allocation.
- Whole-system current view: AoE displays status of multiple sessions to a human/API caller; this observability is not itself the decisive current-control right.
- Current-control decision scope: fixed lifecycle/permission guards and caller-selected per-session commands; no shipped whole-session resource/commitment balancing decision.
- Why this is / is not agent-owned: an ACP process supervisor chooses execution plumbing and retries a process but does not decide what all coding sessions should work on. Human dashboard operation alone does not establish the required first-party parent-governed S3 loop.
- Evidence: [API](https://github.com/agent-of-empires/agent-of-empires/blob/81d4672a846798d0a9b02183d9dce83ea6bf6917/docs/api.md), [session spawn](https://github.com/agent-of-empires/agent-of-empires/blob/81d4672a846798d0a9b02183d9dce83ea6bf6917/src/server/session_spawn.rs), [status update](https://github.com/agent-of-empires/agent-of-empires/blob/81d4672a846798d0a9b02183d9dce83ea6bf6917/src/session/instance/status_update.rs), [ACP registry resolution](https://github.com/agent-of-empires/agent-of-empires/blob/81d4672a846798d0a9b02183d9dce83ea6bf6917/src/acp/supervisor/agents.rs).
- Basis: structural bounded absence.
- Confidence: medium-high.
- Caveats: a third-party orchestration service could implement S3 through AoE's APIs, but such a service is not the assessed first-party standard-distribution controller.

### Absence scope

- Surfaces inspected: Daemon session spawn/store, status detection, ACP worker supervisor, lifecycle and API command paths, TUI/Web controls, callback fields, configuration and repository operating docs.
- Plausible first-party paths checked: all-session status/dashboard, callback on Waiting/Idle/Error, same-session send serialization, process restart, profile/tool selection, shared session queue and external API orchestration.
- Why no material first-party path remains: each path observes/executes specific sessions or provides an integration hook for an outside dispatcher. None supplies an internally owned whole-system current resource/commitment decision and a return path; generic human commands are insufficient for a qualified S3 parent mode.

## S3* — Complementary audit

- State: —
- Function: no first-party, sufficiently independent audit of coding-agent claims with a returned corrective judgment was established in the supported AoE runtime.
- Disturbance / variety regulated: inaccurate agent completion claims, hidden tool errors or mismatches between terminal statements and actual repository changes.
- Decisive decision or feedback right: a human may inspect diffs, terminal history and structured events, but no separate first-party auditor owns a complementary truth judgment and changes subsequent agent operation.
- Decision owner: none established for the Methodology's positive S3* publication states.
- Supporting / enforcement mechanisms: diff view, status hooks, terminal capture, ACP transcripts, logs and optional human/client reprompting.
- Closure path: a user can manually inspect and send follow-up work, but no independent audit finding automatically or through a first-party specific constructor enters corrective operational control.
- Why this is / is not agent-owned: routine observability, permission dialogs, and a hosted agent's private testing/review cannot be re-labelled as AoE's independent complementary audit.
- Evidence: [diff guide](https://github.com/agent-of-empires/agent-of-empires/blob/81d4672a846798d0a9b02183d9dce83ea6bf6917/docs/guides/diff-view.md), [API diff endpoint](https://github.com/agent-of-empires/agent-of-empires/blob/81d4672a846798d0a9b02183d9dce83ea6bf6917/src/server/api/sessions/diff.rs), [status hooks](https://github.com/agent-of-empires/agent-of-empires/blob/81d4672a846798d0a9b02183d9dce83ea6bf6917/src/status_hooks.rs), [background sub-agent transcript tailer](https://github.com/agent-of-empires/agent-of-empires/blob/81d4672a846798d0a9b02183d9dce83ea6bf6917/src/acp/background_agent.rs).
- Basis: structural bounded absence.
- Confidence: medium-high.
- Caveats: a configured external coding agent or CityHall may have separate review/audit mechanisms; their independence/closure is not AoE-owned evidence at this boundary.

### Absence scope

- Surfaces inspected: diff and terminal/structured views, ACP events, background transcript observation, hooks, API status/diff, approvals and adjacent CityHall architectural note.
- Plausible first-party paths checked: raw git diff inspection, tool/session logs, permission review, model/agent self-check, background-agent progress tracking, third-party plugin reviewers and CityHall human audit.
- Why no material first-party path remains: the shipped reviewed mechanisms display/transport operational data or gate ordinary actions; no AoE-owned complementary independent audit judgment and corrective-return relation is supplied.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party prospective external-environment intelligence loop generating adaptations that return to change AoE's future operating capability.
- Disturbance / variety regulated: changes in agent CLI providers, tool availability, repository requirements, policies and possible future session-workflow needs.
- Decisive decision or feedback right: users choose existing tools/profiles/plugins/skills and maintainers publish software updates; no shipped agent or S4-specific constructor studies external change and changes the system's repertoire on that basis.
- Decision owner: caller for configuration; maintainers in the separate development lifecycle, not an in-runtime S4 authority.
- Supporting / enforcement mechanisms: agent registry, profile/skills management, plugin API, update tooling and persisted configuration.
- Closure path: existing configuration can be changed by a caller, but no in-boundary external/future sensing → adaptation option → return to current S3/capability path was found.
- Why this is / is not agent-owned: coding agents' task-local planning and tool selection are S1, not AoE-wide future adaptation; plugins are generic extension points, not an S4 decision loop.
- Evidence: [agent registry](https://github.com/agent-of-empires/agent-of-empires/blob/81d4672a846798d0a9b02183d9dce83ea6bf6917/src/agents.rs), [plugin docs](https://github.com/agent-of-empires/agent-of-empires/blob/81d4672a846798d0a9b02183d9dce83ea6bf6917/docs/plugins.md), [configuration](https://github.com/agent-of-empires/agent-of-empires/blob/81d4672a846798d0a9b02183d9dce83ea6bf6917/docs/guides/configuration.md).
- Basis: structural bounded absence.
- Confidence: medium-high.
- Caveats: downstream users can build an adaptation layer around AoE's API; that possible extension is outside the pinned standard distribution.

### Absence scope

- Surfaces inspected: agent/ACP registries, profile and skills settings, plugins, external dispatcher callbacks, session history, update and development routes.
- Plausible first-party paths checked: automatic tool discovery, profile selection, persistence/learning from sessions, plugin callbacks, external future research and maintainer updates.
- Why no material first-party path remains: inspected paths select pre-existing capabilities, report current status or support developer changes; none implements an externally prospective choice of adaptation that returns into AoE current capability.

## S5 — Policy and identity

- State: —
- Function: no identity/ultimate-policy issue and legitimate decisive return into subsequent AoE operation was established in the shipped local session-management boundary.
- Disturbance / variety regulated: trust, tool permissions, user access, sandbox exposure and profile-level constraints can affect safe operation but are generally ordinary per-action or configuration decisions.
- Decisive decision or feedback right: local operator grants/denies hooks and access or changes configuration; Daemon authorization enforces selected roles/tokens and safe session mutations, not an identity-level constitutional decision path.
- Decision owner: operator/developer for configuration and immediate approvals; no separately closed first-party ultimate-policy function evidenced.
- Supporting / enforcement mechanisms: token/passphrase, local socket peer authorization, read-only API mode, hook trust review, elevated writes and sandbox settings.
- Closure path: operational allow/deny decisions change specific session actions, but no identity/ultimate-policy dispute reaches legitimate parent authority and returns as binding system-level future policy.
- Why this is / is not agent-owned: permission enforcement is not policy ownership; a user's final say over launching or modifying one agent is not automatically S5. CityHall's separate identity/RBAC service belongs to a different system.
- Evidence: [API authorization](https://github.com/agent-of-empires/agent-of-empires/blob/81d4672a846798d0a9b02183d9dce83ea6bf6917/docs/api.md), [CityHall boundary ADR](https://github.com/agent-of-empires/agent-of-empires/blob/81d4672a846798d0a9b02183d9dce83ea6bf6917/docs/adr/0002-single-user-daemon-multi-user-in-cityhall.md), [session trust and creation](https://github.com/agent-of-empires/agent-of-empires/blob/81d4672a846798d0a9b02183d9dce83ea6bf6917/src/server/session_spawn.rs).
- Basis: structural bounded absence.
- Confidence: medium.
- Caveats: this is not a claim that users or maintainers lack legitimate real-world policy authority; only a bounded AoE runtime S5 closure is unproven.

### Absence scope

- Surfaces inspected: API authentication/read-only mode, user approval/trust, profile/sandbox controls, one-human Daemon ADR, CityHall boundary and session mutation rules.
- Plausible first-party paths checked: principal/role checks, passphrase elevation, hook/MCP trust, user session approvals, CityHall SSO/RBAC and project maintainer governance.
- Why no material first-party path remains: these are access/operation constraints or adjacent organizational governance. No in-boundary identity/ultimate-policy matter with a legitimate parent decision and returned durable governing policy path was established.

## Recursion

Each external coding-agent product can have internal recursive teams, tools and policies. AoE hosts their processes as operational S1 units but does not inherit their private metasystems. The local multi-session AoE system has bounded S2 worktree coordination, not a demonstrated complete higher-recursion viable organization.

## Variety and escalation

AoE amplifies operational capacity by persisting many task-local agents and exposing terminal/ACP clients. It attenuates a concrete portion of parallel code-edit variety with optional independent worktrees and protects one-session API input from keystroke races. Status categorization and callbacks inform a human or outside dispatcher; exception handling and retry remain session-specific rather than an automatic algedonic path to an S3/S4/S5 decision owner. The distinction between configured isolation, observed status and organizational discretion remains explicit.

## Evidence gaps

- No live Claude/Codex/other provider-backed task was run; conclusions concern pinned first-party source and documented reachable architecture, not coding success rates.
- The S2 witness is intentionally limited to configured worktree collision avoidance; plain shared-checkout sessions lack that protection, and independent worktrees do not resolve semantic merge conflicts.
- A third-party dispatcher could use callbacks and the HTTP API to regulate a portfolio, audit outputs or adapt future workflows. The assessed standard AoE distribution does not establish that external controller's actual ownership and closure.
- CityHall operates at a separate multi-user recursion and is not imported to upgrade the single-user Daemon's S3*/S5. Routine terminal/diff views and status events are insufficient evidence of independent audit or whole-system adaptive control.

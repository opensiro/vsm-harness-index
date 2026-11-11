---
harness_id: milletcode
project_name: MilletCode
repository: https://github.com/milletcode/milletcode
review_ref: 2278a648381e3279bb1f29ed54cf48ad19c44d66
reviewed_at: 2026-11-11
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: P
autonomy_s5: —
---

# MilletCode

## Review boundary

- System in focus: configured self-hosted MilletCode Rust API/WebSocket runtime, Svelte console, local/SSH Claude Code session adapters, persistent state, approval and skill-distribution mechanisms.
- Purpose and identity: let an operator dispatch and supervise multiple independent model-coding sessions across projects and local/remote hosts through one browser workbench.
- Relevant environment: repository/project files, external Claude Code CLI reasoning/tools, user messages and approvals, local/SSH hosts, project directories, installed skills and outside skill archives.
- Credited operating / distribution surfaces: `backend/src/agents/session_manager.rs`, `backend/src/agents/adapters/claude.rs`, `backend/src/api/sessions.rs`, `backend/src/api/skills.rs`, `backend/src/runtime/skills/`, `backend/src/projects/`, `frontend-svelte/src/routes/`, persistent stores and REST/WebSocket transport.
- Adjacent first-party surfaces excluded from ownership: external Claude Code model policy and internal reasoning, unfinished disabled adapters (Codex by default), SmartCode alpha/DeepSeek development claims, vendor skill content, host Git/SSH, project maintainers and this repository's own release CI.
- First-party operating/deployment modes: enabled Claude Code local or SSH sessions, persisted session management and human approval UI, optional operator-requested official or third-party skill installation; no asserted first-party autonomous multi-agent supervisor.
- Recursion level: one MilletCode deployment serving projects/sessions, with its autonomous CLI-backed coding sessions as separate S1 operations.
- Reviewed revision: `2278a648381e3279bb1f29ed54cf48ad19c44d66`, source-static (2026-11-11). No live Claude session, remote SSH host or third-party skill download executed.
- Generated Profile/Methodology: 0.2.4 / 0.3.8; active Profile/Methodology: 0.2.4 / 0.3.8.

## Repository architecture

The Rust backend discovers configured local/SSH projects, starts/resumes external Claude Code CLI processes via the first-party adapter, parses stream-json messages, persists multiple sessions and routes prompt/approval/status events over WebSocket and REST. The Svelte browser console provides a whole-deployment view and lets a human start/stop/resume or approve sessions. A separate skills service lists official skill options, validates configured archives, allows human-requested install/uninstall, and can fan out prompted third-party installation to existing agents with after-install verification. See [README](https://github.com/milletcode/milletcode/blob/2278a648381e3279bb1f29ed54cf48ad19c44d66/README.md), [session manager](https://github.com/milletcode/milletcode/blob/2278a648381e3279bb1f29ed54cf48ad19c44d66/backend/src/agents/session_manager.rs) and [skill API](https://github.com/milletcode/milletcode/blob/2278a648381e3279bb1f29ed54cf48ad19c44d66/backend/src/api/skills.rs).

## Operational model

- The external model decides individual coding steps after MilletCode launches an agent session and delivers tools/output; transport, persistence and approvals constrain that execution.
- The operator owns whole-deployment prioritization, resource allocation and intervention from a multi-project/session UI. A deterministic session registry and idle alert do not choose priorities on their own.
- For S4, the human may judge externally supplied skill options and ask the platform to install them into current agent nodes. This is a narrow parent-governed capability-adaptation path, not autonomous market forecasting.

## S1 — Operations

- State: A
- Function: carry out model-directed coding/dialog tasks in configured project workspaces.
- Disturbance / variety regulated: changing prompts, code/tool observations, permissions, session context and test results.
- Decisive decision or feedback right: the Claude Code model chooses next edits, tools and responses during a live session; users may approve/deny restricted actions.
- Decision owner: first-party-launched Claude Code agent process in an enabled instance, whose model reasoning is external but whose session/approval/feedback organization is shipped by MilletCode.
- Supporting / enforcement mechanisms: `ClaudeAdapter` process launcher, `SessionManager`, JSONL event parser, approval response handling, SSH/local runtime and WebSocket streaming.
- Closure path: browser/API prompt → launched Claude CLI with project context → model/tool work → streamed event or approval → user/CLI response → continued model step or completed session.
- Boundary reachability: Claude adapter is enabled by default and `SessionManager::create_session` resolves its configured local or SSH executable; no custom third-party framework implementation is needed beyond installing Claude Code.
- Why this is / is not agent-owned: model selects content/steps and handles tool feedback; backend only starts, meters, routes and persists the session.
- Evidence: [Claude adapter launch/events](https://github.com/milletcode/milletcode/blob/2278a648381e3279bb1f29ed54cf48ad19c44d66/backend/src/agents/adapters/claude.rs), [session management](https://github.com/milletcode/milletcode/blob/2278a648381e3279bb1f29ed54cf48ad19c44d66/backend/src/agents/session_manager.rs), [session API](https://github.com/milletcode/milletcode/blob/2278a648381e3279bb1f29ed54cf48ad19c44d66/backend/src/api/sessions.rs).
- Basis: structural shipped CLI agent mode.
- Confidence: high for adapter-agent reachability, not for quality of model execution.
- Caveats: no model-provider credentials or live end-to-end workflow tested; HTTP agent adapters are immature/disabled and not needed for the S1 claim.

## S2 — Coordination

- State: —
- Function: no evidenced first-party discretionary regulation of interfering decisions among distinct running coding agents.
- Disturbance / variety regulated: two agents could touch the same source files or make incompatible changes, but no inter-agent collision resolution loop is shipped.
- Decisive decision or feedback right: per-session duplicate-key overwrite/resume and resource handling decide session identity, not cross-agent work-claim arbitration.
- Decision owner: absent for an S2-specific corrective choice; operators manually coordinate tasks outside this provided relation.
- Supporting / enforcement mechanisms: composite session keys, status registry, SSH pooling, approval queue, task-specific stop/resume and notifications.
- Closure path: no first-party scope conflict event → coordination verdict → changed instructions to two distinct S1 agents demonstrated.
- Why this is / is not agent-owned: session identity deduplication and transport routing prevent duplicate sessions but do not attenuate conflicting independent tasks across agents.
- Evidence: [session manager](https://github.com/milletcode/milletcode/blob/2278a648381e3279bb1f29ed54cf48ad19c44d66/backend/src/agents/session_manager.rs), [session API](https://github.com/milletcode/milletcode/blob/2278a648381e3279bb1f29ed54cf48ad19c44d66/backend/src/api/sessions.rs), [multi-agent feature description](https://github.com/milletcode/milletcode/blob/2278a648381e3279bb1f29ed54cf48ad19c44d66/README.md).
- Basis: bounded no-path within included session/agent/transport and project surfaces.
- Confidence: medium-high.
- Caveats: an operator or external Claude agent could independently coordinate work; that is not the first-party default S2 loop.

### Absence scope

- Surfaces inspected: adapter registry, `SessionManager`, composite session routing, WebSocket and UI approval controls, project discovery and shared configuration.
- Plausible first-party paths checked: session key collision/resume, concurrent session lists, idle notifications, shared project folder access, approval queues.
- Why no material first-party path remains: each is a session-local status/identity/permission path; no specific inter-S1 work conflict is detected, mediated and returned to participating agents.

## S3 — Inside-and-now control

- State: P
- Function: oversee and intervene in currently active sessions and project commitments across the operator's MilletCode installation.
- Disturbance / variety regulated: stuck/idle agents, unexpected approvals, errored sessions and competing current project work.
- Decisive decision or feedback right: human operator can select projects/sessions, issue work messages, stop/resume instances, resolve pending approvals and change active execution configuration.
- Decision owner: authenticated local/hosted human console operator; no model is shown prioritizing all sessions from a whole-deployment view.
- Supporting / enforcement mechanisms: dashboard and sessions routes, persistent session store, `SessionManager`, status APIs, pending-control registry, idle alerts and project discovery.
- Whole-system current view: `/api/sessions` and projects console enumerate running/idle/stopped sessions across projects and agents, with current status and approval prompts.
- Current-control decision scope: operator allocates attention and instructions, intervenes in stuck sessions and changes which active coding threads continue.
- Closure path: aggregated session/project state → operator selects intervention/priority → REST action (message/approve/stop/restore) → changed agent process and subsequent dashboard state.
- Boundary reachability: installed browser dashboard and REST session controls are first-party supported modes, not maintainer-only developer infrastructure.
- Why this is / is not agent-owned: whole-session decisions require human selection; automatic status updates and Lark notifications only report/enforce.
- Evidence: [sessions API](https://github.com/milletcode/milletcode/blob/2278a648381e3279bb1f29ed54cf48ad19c44d66/backend/src/api/sessions.rs), [session manager](https://github.com/milletcode/milletcode/blob/2278a648381e3279bb1f29ed54cf48ad19c44d66/backend/src/agents/session_manager.rs), [console](https://github.com/milletcode/milletcode/blob/2278a648381e3279bb1f29ed54cf48ad19c44d66/frontend-svelte/src/routes/DashboardRoute.svelte).
- Basis: direct parent-operated current-control path.
- Confidence: medium-high for parent supervision; actual scheduling effectiveness untested.
- Caveats: current S3 belongs to the deployed operator, not an autonomous model supervisor; a session's approval prompt alone would not prove S3 without the whole view.

## S3* — Complementary audit

- State: —
- Function: no independent first-party review of coding-agent operational claims with separate evidence access and a corrective verdict demonstrated.
- Disturbance / variety regulated: coding errors/false completion reports remain possible; installation validation and permission checks address different narrower hazards.
- Decisive decision or feedback right: no shipped independent code-audit actor/constructor returns a judgment that changes worker behavior.
- Decision owner: human may inspect artifacts externally, but that reviewer is not a first-party complementary path in this installed system.
- Supporting / enforcement mechanisms: session history, Git/file browser, per-action approvals and skill after-install checks.
- Closure path: user can view output and decide manually; an independent audit → findings → corrective agent control loop is not supplied.
- Why this is / is not agent-owned: approval prompts are permission decisions, and existence checks for installed skills do not review agent code/work independently.
- Evidence: [sessions UI/API](https://github.com/milletcode/milletcode/blob/2278a648381e3279bb1f29ed54cf48ad19c44d66/backend/src/api/sessions.rs), [skills verification](https://github.com/milletcode/milletcode/blob/2278a648381e3279bb1f29ed54cf48ad19c44d66/backend/src/api/skills.rs), [README](https://github.com/milletcode/milletcode/blob/2278a648381e3279bb1f29ed54cf48ad19c44d66/README.md).
- Basis: bounded absence of independent S3* audit boundary.
- Confidence: medium-high for standard distribution.
- Caveats: external CI or a separately hired model reviewer could be attached, but is not credited without a first-party integration.

### Absence scope

- Surfaces inspected: coding adapters, session history/approval, skill install verification, Git/file views and end-user routes.
- Plausible first-party paths checked: agent permission approval, session event log, skills verification and third-party app/repo checks.
- Why no material first-party path remains: no separate audit owner with complementary code/operational evidence and findings returned into corrective session control.

## S4 — Outside-and-then intelligence

- State: P
- Function: select external skill packages as future coding-agent capability options and deploy the chosen adaptation across configured agent nodes.
- Disturbance / variety regulated: new external skill capabilities and changing local agent requirements beyond a current user prompt.
- Decisive decision or feedback right: a human operator evaluates the available official/third-party skill option and requests install/uninstall; no autonomous model has blanket authority to define future capabilities.
- Decision owner: human console operator who chooses a skill and, for official packages, provides/configures the trusted download source; model-run third-party installers execute that request within bounds.
- Supporting / enforcement mechanisms: official skill manifest, skills marketplace UI, API install queues, configured archive source/password, per-node plan, verification after install, persistent status.
- External distinction: skill packages originate outside the currently installed agent session and may introduce capabilities it previously lacked, unlike session state, logs or immediate code output.
- Future / prospective distinction: the operator selects a reusable capability for subsequent sessions rather than merely answering an ongoing coding turn.
- Adaptation option generated: displayed available skill packages plus manually supplied third-party skill requests; choice remains human and the catalog is not independent strategic research.
- Path back into current capability / S3: operator skill selection → official/third-party install API → per-agent/node skill directory update and verification → sessions using newly available installed skills.
- Closure path: offered outside skill option → parent selection/approval → installation/verification → changed agent skill availability → later coding operations.
- Boundary reachability: first-party `skills.rs` routes and Skills UI are shipped; official install requires an explicitly configured source, while third-party install requires an operator-provided request.
- Why this is / is not agent-owned: software/agents may execute installation, but the prospective option and authorization are owned by the operator, so parent `P` rather than `A`.
- Evidence: [skills API and install verification](https://github.com/milletcode/milletcode/blob/2278a648381e3279bb1f29ed54cf48ad19c44d66/backend/src/api/skills.rs), [skill market UI](https://github.com/milletcode/milletcode/blob/2278a648381e3279bb1f29ed54cf48ad19c44d66/frontend-svelte/src/routes/SkillsRoute.svelte), [README feature description](https://github.com/milletcode/milletcode/blob/2278a648381e3279bb1f29ed54cf48ad19c44d66/README.md).
- Basis: first-party parent-governed capability acquisition path, narrow S4.
- Confidence: medium; live source availability and installed-skill usefulness not tested.
- Caveats: not general environmental foresight, adaptive product strategy or autonomous skill selection; no claim official downloads work without configured URL/password.

## S5 — Policy and identity

- State: —
- Function: no evidenced first-party path where the installed deployment's ultimate mission/identity is authoritatively selected and returned into operations.
- Disturbance / variety regulated: credential/auth and agent allowlists constrain execution, but do not settle the ultimate purpose of the deployment.
- Decisive decision or feedback right: operator can configure access, default model, approvals and skills, but no specific ultimate-identity decision circuit is shown.
- Decision owner: legitimate human owner retains general authority outside the runtime; operational permissions should not be mislabeled a closed S5 function.
- Supporting / enforcement mechanisms: `config.toml`, `auth.mode`, agents/instances, approval controls, SSH credentials and skill installation policy.
- Closure path: settings change execution permissions and capacity, not an explicit identity-level mission/organizational purpose selection and return.
- Why this is / is not agent-owned: no model owns policy identity, and human password/approval controls alone do not establish parent S5 by the function-first threshold.
- Evidence: [configuration](https://github.com/milletcode/milletcode/blob/2278a648381e3279bb1f29ed54cf48ad19c44d66/backend/src/config.rs), [README configuration](https://github.com/milletcode/milletcode/blob/2278a648381e3279bb1f29ed54cf48ad19c44d66/README.md), [approval API](https://github.com/milletcode/milletcode/blob/2278a648381e3279bb1f29ed54cf48ad19c44d66/backend/src/api/pending.rs).
- Basis: bounded no-path at installed boundary.
- Confidence: medium; an operator's outside organizational identity is not denied.
- Caveats: selecting a new skill as future capability is S4 P here, not itself S5 identity authority.

### Absence scope

- Surfaces inspected: configuration/auth, agent instance policy, approvals, skill market and project/session UI.
- Plausible first-party paths checked: admin setting edits, provider/skills choice, agent approval and session termination.
- Why no material first-party path remains: each is task/current-capability/permission selection, not a named ultimate project identity/policy dispute resolved by a first-party return circuit.

## Distributed OSS parent arrangement

The assessed parent is the installed console operator, not the upstream company's maintainers or contributors. The AGPL license and trademark policy of the upstream repository are not evidence of an installed multi-maintainer S5 loop.

## Self-hosted and non-human modes

MilletCode self-hosts operations and models may run autonomously inside individual sessions, but the multi-project dashboard and skill-acquisition selection are human-governed. This assessment does not generalize to unsupported disabled agents or unconfigured official skill servers.

## Recursion

Different coding sessions are S1 cells only when doing distinct work; grouping them on a dashboard does not by itself form inter-agent S2. The console operator controls the installed portfolio at S3 P.

## Variety and escalation

Per-agent configuration, approval queues, session persistence, SSH vs local runtime choice, agent status, idle alerts, source URL/password and post-install verification attenuate variation. None proves reviewer independence or ultimate identity governance.

## Evidence gaps

- Source-static only; live Claude CLI, SSH, auth security, skill installation and dashboard decision quality were not exercised.
- Skill-market S4 is narrow future capability acquisition; external skill utility and provenance trust require deployment-specific verification.
- Multi-session visibility and stop/approve actions do not prove autonomously agent-owned S2/S3.

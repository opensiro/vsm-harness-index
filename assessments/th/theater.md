---
harness_id: theater
project_name: Theater
repository: https://github.com/mana-byte/theater
review_ref: 405d8b914e588e91befba6f8a82eb56ff563fd6e
reviewed_at: 2026-11-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Theater

## Review boundary

- System in focus: installed Theater local daemon, agent-facing MCP orchestration tools, terminal/provider runtime, bundled first-party delegate/pair skills and opt-in packaged hierarchy/Beads play, with live Claude/Codex/Pi/opencode/Vibe sessions.
- Purpose and identity: let coding agents manage, communicate, monitor and coordinate other real coding-agent CLI sessions while the human operator has a unified local Régie/control view.
- Relevant environment: coding tasks, repository branches/worktrees and diffs, runtime prompts, tool outputs, agent availability, terminal process identities and human instructions.
- Standard-distribution boundary: Python Theater daemon, MCP/client tools, bundled `theater-delegate` and `pair` play; the first-party optional `theater-plus` deployment with built-in Beads hierarchy plugin/play is separately identified. Agent CLIs remain external execution dependencies, not independent imported metasystems.
- Credited operating / distribution surfaces: `theater/mcp/`, `theater/skills/builtin/`, `theater/skills/plays.py`, `theater/mcp_plugins/builtin/beads/`, `README.md`, `docs/architecture.md` and the shipped Régie control client.
- Adjacent first-party surfaces excluded from ownership: repository's developer CI, tests and documentation-only aspirational examples; CLI provider-native policies, independent model internals, unrelated project code and separately authored user skills are not borrowed as Theater's S3–S5.
- First-party operating / deployment modes considered: base Theater daemon with agent clients, delegate/pair play, opt-in Theater-plus with Beads hierarchy play, human Régie current oversight, remote/provider-control modes and disabled-plugin configurations.
- Recursion level: one Theater local multi-agent work organization with a master/agents hierarchy; nested teams may delegate but do not automatically contain all six VSM functions.
- Reviewed revision: `405d8b914e588e91befba6f8a82eb56ff563fd6e`.
- Observation date: 2026-11-04.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Theater's daemon owns persistent participant identity, route verification, lifecycle, job and transcript/event projection; MCP servers expose typed spawn/send/await/inspect/control calls to connected agent CLIs. Régie shows live agent trees, terminals and trajectories to a human. The `theater-delegate` skill can start a separate reviewer-master and builder in one scoped worktree; the reviewer independently examines exact commits and iterates fixes. In the optional packaged `hierarchy` play, the master chooses parallel streams by path/interface dependency, routes workers and independent reviewers, then integrates exact reviewed SHAs. The Beads plugin supplies role-scoped shared boards, not the discretionary thinking behind tasks.

Sources: [README](https://github.com/mana-byte/theater/blob/405d8b914e588e91befba6f8a82eb56ff563fd6e/README.md), [architecture](https://github.com/mana-byte/theater/blob/405d8b914e588e91befba6f8a82eb56ff563fd6e/docs/architecture.md), [delegate skill](https://github.com/mana-byte/theater/blob/405d8b914e588e91befba6f8a82eb56ff563fd6e/theater/skills/builtin/theater-delegate/SKILL.md), [pair reviewer](https://github.com/mana-byte/theater/blob/405d8b914e588e91befba6f8a82eb56ff563fd6e/theater/skills/builtin/pair/reviewer/SKILL.md), [hierarchy master](https://github.com/mana-byte/theater/blob/405d8b914e588e91befba6f8a82eb56ff563fd6e/theater/mcp_plugins/builtin/beads/skills/hierarchy/master/SKILL.md).

## Operational model

Theater's base daemon is a transport and state authority, not an LLM decision-maker. Explicitly attached model-backed CLI sessions perform project actions through their native tools, pass results through durable Theater handles, and can spawn workers. Packaged pair/hierarchy plays assign different decision owners to implementation, coordinating master, and independent reviewer; status and job handles enforce correspondence rather than creating cognition. Human Régie can view, send, interrupt and decide user-scoped approvals.

## S1 — Operations

- State: A
- Function: connected model-backed CLI agents perform variable coding/research/testing tasks and return artifacts/results in Theater job sessions.
- Disturbance / variety regulated: changing code states, user specifications, tool outcomes, test failures and revised task briefs.
- Decisive decision or feedback right: each active worker chooses concrete coding actions, tools/tests and corrective edits within its authorized scope.
- Decision owner: spawned or attached Claude/Codex/Pi/opencode/Vibe agent session, not Theater daemon transport.
- Supporting / enforcement mechanisms: verified terminal/provider route, MCP spawn/send/await operations, transcript tracking and optional worktree provisioning.
- Closure path: agent gets task/brief, acts in its own harness, reports done or blocked, and receives further corrections via Theater send/follow-up.
- Boundary reachability: installed Theater explicitly supports these five CLI harnesses and exposes agent-facing spawn/await tools; attached autonomous agents are a first-party operating mode, not an unspecified API consumer.
- Why this is / is not agent-owned: attached model/tool sessions own work decisions; Theater's deterministic process and identity service only makes them addressable and observable.
- Evidence: [README operating modes](https://github.com/mana-byte/theater/blob/405d8b914e588e91befba6f8a82eb56ff563fd6e/README.md), [delegation toolset](https://github.com/mana-byte/theater/blob/405d8b914e588e91befba6f8a82eb56ff563fd6e/theater/mcp/toolsets/delegation.py), [worker play card](https://github.com/mana-byte/theater/blob/405d8b914e588e91befba6f8a82eb56ff563fd6e/theater/mcp_plugins/builtin/beads/skills/hierarchy/worker/SKILL.md).
- Basis: structural.
- Confidence: high.
- Caveats: source review, not a live multi-provider run; an idle process/terminal alone is not an operational S1 unit.

## S2 — Coordination

- State: A
- Function: the hierarchy master dynamically separates concurrent S1 coding streams by path ownership, live interface dependencies and shared integration constraints.
- Disturbance / variety regulated: parallel agents can edit overlapping files or consume interfaces changed by another stream; merge order and shared hot files create conflicts.
- Decisive decision or feedback right: master selects light/heavy execution, assigns exclusive owned paths, keeps shared hot files at integration, sequences consumers after producers, and rejects/repairs unauthorized diff overlap.
- Decision owner: model-backed hierarchy master using the packaged opt-in `hierarchy/master` protocol; deterministic worktree/plugin gates support rather than replace it.
- Supporting / enforcement mechanisms: stream-base SHAs, worktree isolation, dependency contracts, exact file ownership audit, Beads board and role-scoped agent messaging.
- Closure path: after detecting dependency/overlap, master reallocates paths or sequences work, sends bounded tasks, audits completed stream diffs against ownership, then integrates reviewed SHAs in dependency order; failed conflicts return for repair.
- Boundary reachability: Theater ships the hierarchy skill and Beads plugin as its own packaged `theater-plus` option; base daemon by itself is only C-level transport and no default autonomous S2 actor is claimed for unconfigured sessions.
- Why this is / is not agent-owned: the optional installed hierarchy master makes situational shared-resource and inter-S1 dependency decisions; registry route checks and worktree naming are deterministic supports.
- Distinct S1 units: independent workers/leads in separately launched model sessions/worktrees on a common integration project.
- Inter-S1 disturbance: worker B consumes a function worker A changes, or two streams touch one shared registry/hot file.
- Attenuating coordination relation: master-enforced path contracts, producer-before-consumer ordering, exclusive integration ownership and exact-SHA merge sequence.
- Feedback into subsequent S1 behaviour: findings/failed path audits are sent to the owning worker for correction; dependent tasks wait for accepted producer commits.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the master explicitly evaluates cross-worker resource/interface collisions and changes parallel work assignment/merge topology to prevent them.
- Evidence: [hierarchy master track/build/integrate](https://github.com/mana-byte/theater/blob/405d8b914e588e91befba6f8a82eb56ff563fd6e/theater/mcp_plugins/builtin/beads/skills/hierarchy/master/SKILL.md), [play contract](https://github.com/mana-byte/theater/blob/405d8b914e588e91befba6f8a82eb56ff563fd6e/theater/mcp_plugins/builtin/beads/skills/hierarchy/PLAY.toml), [Beads plugin](https://github.com/mana-byte/theater/blob/405d8b914e588e91befba6f8a82eb56ff563fd6e/docs/mcp-server-plugins.md).
- Basis: structural.
- Confidence: medium.
- Caveats: opt-in Beads/hierarchy deployment and model compliance required; base Theater without that play does not autonomously coordinate path ownership.

## S3 — Inside-and-now control

- State: A(P)
- Function: master agent supervises current task commitments, acceptance criteria, multi-worker results and final integration; the human operator can override task priorities/approval in a separate legitimate mode.
- Disturbance / variety regulated: blocked workers, unreviewed commits, drifting acceptance criteria, failing merged suites and open user decisions.
- Decisive decision or feedback right: master chooses work allocation, requests corrections, freezes exact reviewed heads and integrates approved streams; human Régie/brief decision can accept/refuse scope, publication or task continuation.
- Decision owner: connected hierarchy master agent in the optional packaged play; parent human user via Régie/interactive instructions and explicit authorization for external merge/push.
- Supporting / enforcement mechanisms: participant tree, await handles and structured results, role/position permissions, Beads progress board, integration worktree, human messaging/interruption.
- Closure path: master polls/awaits the job handles, checks actual SHAs and tests, revises/reviews current work, merges exact accepted heads, reports AC closure to user; parent can send new scope/decisions or stop work, with authorization returned to master.
- Boundary reachability: hierarchy master is a shipped first-party play in optional Theater-plus; Régie and MCP controls are shipped operational interfaces, not an inferred human board.
- Why this is / is not agent-owned: model-backed master makes current-control choices while deterministic daemon enforces identity/routing; parent authority remains human for material scope, publication and shutdown outside given permissions.
- Whole-system current view: live agent tree, job result handles, master-scoped shared task board, integration branch status, unit acceptance criteria and review outcomes.
- Current-control decision scope: current task decomposition, simultaneous work budget, integration order, review gating, remediation and final closure.
- Evidence: [hierarchy master](https://github.com/mana-byte/theater/blob/405d8b914e588e91befba6f8a82eb56ff563fd6e/theater/mcp_plugins/builtin/beads/skills/hierarchy/master/SKILL.md), [Régie operator interface](https://github.com/mana-byte/theater/blob/405d8b914e588e91befba6f8a82eb56ff563fd6e/README.md), [MCP management controls](https://github.com/mana-byte/theater/blob/405d8b914e588e91befba6f8a82eb56ff563fd6e/theater/mcp/toolsets/participants.py).
- Basis: structural.
- Confidence: medium-high.
- Caveats: base daemon's tree/dashboard alone is not autonomous S3; optional master mode and legitimate owner intervention are distinct paths.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Hierarchy master agent | worker done/blocked, failed review or integration suite | reorganize work, send corrections, re-review and integrate accepted exact SHA | [master card](https://github.com/mana-byte/theater/blob/405d8b914e588e91befba6f8a82eb56ff563fd6e/theater/mcp_plugins/builtin/beads/skills/hierarchy/master/SKILL.md) |
| Parent (`P`) | Human user via Régie/brief | missing approval, changed scope, publication/retirement request | operator sends decision or withholds authorization, master follows it or escalates | [Régie controls](https://github.com/mana-byte/theater/blob/405d8b914e588e91befba6f8a82eb56ff563fd6e/README.md), [delegate card](https://github.com/mana-byte/theater/blob/405d8b914e588e91befba6f8a82eb56ff563fd6e/theater/skills/builtin/theater-delegate/SKILL.md) |

## S3* — Complementary audit

- State: A
- Function: independent reviewer agent inspects builder's actual commit/diff/tests and returns located evidence-based findings for correction before acceptance.
- Disturbance / variety regulated: a builder reports completion despite incorrect code, missing checks or unacceptable deviations from the brief.
- Decisive decision or feedback right: reviewer reads the raw git diff and reruns checks, issues approve/changes_request tied to exact SHA and refuses agreement while substantiated blockers remain.
- Decision owner: separate model-backed reviewer in shipped pair play or hierarchy review role, distinct from builder and denied write ownership.
- Supporting / enforcement mechanisms: separate role/model requirement, read-only reviewer worktree, exact-head artifact binding, structured review reports, corrective `send` and re-review.
- Closure path: reviewer independently reads `git diff base..HEAD`, observes tests, sends located findings to builder, verifies revised SHA after correction and approves only exact unchanged head; master gates integration.
- Boundary reachability: `theater-delegate` installs and invokes the built-in pair reviewer play directly; optional hierarchy also mandates independent per-stream and final reviewers.
- Why this is / is not agent-owned: an independent active agent inspects source artifacts rather than trusting completion text; its judgments have an actionable return loop to the worker/master.
- Claim being audited: builder's delivered implementation and compliance with acceptance criteria at named commit.
- Ordinary reporting path: builder's `done` and structured result.
- Complementary access path: reviewer reads raw source/diff and runs acceptance checks in the separate reviewer role; receipt/commit validation is independent of builder's report.
- Independence boundary: reviewer cannot edit, uses a different model from builder under pair protocol, is not a dual-role writer; human approval does not substitute for audit.
- Who acts on findings: same builder repairs or rebuts; reviewer re-checks, and coordinating master rejects unreviewed integration.
- Evidence: [pair reviewer](https://github.com/mana-byte/theater/blob/405d8b914e588e91befba6f8a82eb56ff563fd6e/theater/skills/builtin/pair/reviewer/SKILL.md), [delegate launcher](https://github.com/mana-byte/theater/blob/405d8b914e588e91befba6f8a82eb56ff563fd6e/theater/skills/builtin/theater-delegate/SKILL.md), [hierarchy review](https://github.com/mana-byte/theater/blob/405d8b914e588e91befba6f8a82eb56ff563fd6e/theater/mcp_plugins/builtin/beads/skills/hierarchy/master/SKILL.md).
- Basis: structural.
- Confidence: high.
- Caveats: audit succeeds only with correct model/provider availability and role compliance; this review did not behaviorally execute a pair.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party prospective environment sensing, future option generation and committed adaptation return loop is packaged.
- Disturbance / variety regulated: agent market, model capability and future task landscape may change, but supported controls are current task/model selection and activity observation.
- Decisive decision or feedback right: no separate intelligence actor is required to observe external change and choose future capability shifts for the organization.
- Decision owner: human may change configs; master can conduct optional research when asked, neither is a standing installed S4 decision owner.
- Supporting / enforcement mechanisms: model discovery, logs/trajectories, cost view and user-defined skills.
- Closure path: provider/model choice affects future spawns but is not a packaged outside-environment-evidence -> prospective options -> S3-adaptation loop.
- Why this is / is not agent-owned: live observability and model lists show present status/options; future-oriented learning is generic capability the user must request and compose.
- Evidence: [architecture](https://github.com/mana-byte/theater/blob/405d8b914e588e91befba6f8a82eb56ff563fd6e/docs/architecture.md), [README model/discovery controls](https://github.com/mana-byte/theater/blob/405d8b914e588e91befba6f8a82eb56ff563fd6e/README.md).
- Basis: structural.
- Confidence: medium.
- Caveats: a separately authored prospective skill could use Theater tools without becoming a function of the standard distribution.

### Absence scope

- Surfaces inspected: daemon architecture, MCP tools, first-party skills/plays, Beads plugin, UI, configuration and model discovery.
- Plausible first-party paths checked: model catalog, trajectory/cost analytics, task-board backlog, debates and optional externally configured skills.
- Why no material first-party path remains: none explicitly binds outside/future evidence to capability adaptation options and returned present-control decisions as a distinct standing S4 function.

## S5 — Policy and identity

- State: —
- Function: role/position policies, identities and operator authorizations exist but no first-party whole-organization ultimate-policy deliberation/return loop is shown.
- Disturbance / variety regulated: delegation rights, user consent, play membership and sensitive termination risk are controlled as task/session authorization rather than an institutional identity-policy tension.
- Decisive decision or feedback right: no first-party pathway takes a cross-system identity/ethos issue through legitimate ultimate authority and returns binding organization-level policy to work.
- Decision owner: user can choose permission and play configuration; daemon enforces role constraints, not a separate S5 policy judge.
- Supporting / enforcement mechanisms: play membership and position assignment, retirement rights, job approvals, operator choices and provider trust boundaries.
- Closure path: a specific human permission changes what one operation may do; no S5 issue -> legitimate deciding forum -> returned policy instrument is packaged.
- Why this is / is not agent-owned: organizational hierarchy and named master do not prove ultimate policy authority; safe controls and membership constraints are lower-level operation governance.
- Evidence: [play position contract](https://github.com/mana-byte/theater/blob/405d8b914e588e91befba6f8a82eb56ff563fd6e/theater/skills/plays.py), [hierarchy play](https://github.com/mana-byte/theater/blob/405d8b914e588e91befba6f8a82eb56ff563fd6e/theater/mcp_plugins/builtin/beads/skills/hierarchy/PLAY.toml), [architecture](https://github.com/mana-byte/theater/blob/405d8b914e588e91befba6f8a82eb56ff563fd6e/docs/architecture.md).
- Basis: structural.
- Confidence: medium-high.
- Caveats: a specific externally configured organization could implement S5 over this substrate, not evidenced here.

### Absence scope

- Surfaces inspected: daemon identity, play membership and authority, user approvals, hierarchy task board, shared config and control UI.
- Plausible first-party paths checked: master/member roles, human supervisor, operator consent, budget rails and project skill definitions.
- Why no material first-party path remains: these constrain who may spawn/send/retire or perform tasks, but no specific ultimate-identity dispute, authorized policy decision and operation-return process is present.

## Distributed OSS parent arrangement

The upstream maintainer/CI is not the installed Theater team's parent. Human Régie/task-owner intervention is credited only as current-control parent S3, without imputing an S5 policy role.

## Self-hosted and non-human modes

Theater state and sessions are local; agent harnesses retain their native accounts, permissions and model reasoning. The base daemon with no model sessions is coordination infrastructure, not an autonomous organization. Optional Beads/hierarchy requires the packaged theater-plus runtime and must not be treated as default for every install.

## Recursion

Nested master/lead/member and pair plays can reproduce delegation, coordination and audit at subtrees; no complete separate S1–S5 loops for each recursive nested unit are established.

## Variety and escalation

Live status, verified routes and shared boards attenuate operational variety; agents and cross-model reviewers amplify relevant responses. Blocked workers and substantive questions escalate through send/await to manager or human, with precise return handles. Neither role hierarchy nor UI telemetry alone constitutes independent audit or future policy.

## Evidence gaps

- Structural source-verified assessment at pinned SHA, not a live 20-agent behavioral study.
- S2 and agent-owned S3 rely on an explicit optional built-in hierarchy play (theater-plus/Beads); base non-play wiring alone is not credited those autonomous functions.
- S3* is strongest in the independent pair reviewer path, but optional invocation is required and results depend on real agent compliance.

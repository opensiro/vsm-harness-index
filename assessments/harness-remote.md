---
harness_id: harness-remote
project_name: Harness Remote
repository: https://github.com/giuliastro/harness-remote
review_ref: ee9d315c7a3329ab6ef5588d1565210167d47a9d
reviewed_at: 2026-10-10
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# Harness Remote

## Review boundary

- System in focus: one Harness Remote-managed local or paired multi-machine coding workspace, including shipped Machine gateway/agent adapters, native Session discovery and control, task-run/worktree construction, project identification, handoff linkage and operator web/desktop/Android views.
- Purpose and identity: operate, remotely observe, steer, resume and continue existing coding-agent work across machines and supported CLI runtimes without copying or replacing their authoritative native sessions.
- Relevant environment: repositories on the target machines, installed/authenticated Codex CLI, Claude Code, OpenCode, Oh My Pi, PI runtimes, operator, machine network/VPN, filesystem/Git, host credentials and model/tool feedback owned by those native agent processes.
- Standard-distribution boundary: shipped Node.js bridge/daemon, Task Run and native Session gateway, packaged agent adapters plus web/desktop/Android clients. External native coding-agent processes perform work as deliberately assembled operational actors; their internal model/tool/permission/session semantics remain external rather than credited as first-party higher VSM functions.
- Credited operating / distribution surfaces: normal Machine launcher and routes, ACP/OpenCode adapters, Task Run with first-party Git worktree preparation, Task context/handoff, Session claim/operation ledger, native-session home, remote observation/control.
- Adjacent first-party surfaces excluded from ownership: upstream proprietary/third-party model internals; the original harness's prompt policies, reasoning, tool execution, memory and compaction; repository CI/test scaffolding and documented experimental features not actually wired into the installed gateway.
- First-party operating / deployment modes considered: desktop app starting local Machine runtime; standalone Node gateway; paired remote machine; native-session control and supported TaskDesk Task Run with optional first-party worktree; cross-agent / cross-machine continuation.
- Recursion level: one operator-governed multi-machine workspace; individual supported native coding-agent sessions executing actual tasks are the S1 cells. Other users' independent deployments and OSS maintainers are separate systems.
- Reviewed revision: `ee9d315c7a3329ab6ef5588d1565210167d47a9d`.
- Observation date: 2026-10-10.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

The README expressly distinguishes Harness Remote from a coding agent: supported agent CLIs remain owners of native Sessions and their transcripts, tool execution, permission mechanisms, context and model behavior. The first-party Machine gateway detects available runtimes, brokers native session APIs (ACP or OpenCode), discovers projects/models, forwards user prompts/stop/approval interactions, and exposes attention/diagnostic state to an operator through local desktop and remote web/mobile interfaces.

For the separate TaskDesk/Task Run path, `TaskRunController` accepts a task and a target agent, records an accepted run identity before launching the native Session and passes a selected workspace path to the agent launcher. `WorktreeManager.prepare` creates a deterministic **unique per-task Git branch/worktree** under the daemon state directory; it refuses reuse/conflicting paths and preserves unmerged/dirty work upon cleanup. Task-run context can include bounded file changes from the worktree. This is a first-party *constructor isolation mode*, not a claim that every pre-existing external native Session is isolated or that any agent autonomously chooses worktree topology.

Other first-party bridge features include real native Session claims, operation idempotency, session and project identity checks, cross-agent lineage, machine pairing and handoff. They aid safety/continuation but do not on their own constitute S2/S3/S3*/S4/S5.

Primary sources: [README.md](https://github.com/giuliastro/harness-remote/blob/ee9d315c7a3329ab6ef5588d1565210167d47a9d/README.md); [launcher.js](https://github.com/giuliastro/harness-remote/blob/ee9d315c7a3329ab6ef5588d1565210167d47a9d/bridge/src/launcher.js); [machine-daemon.js](https://github.com/giuliastro/harness-remote/blob/ee9d315c7a3329ab6ef5588d1565210167d47a9d/bridge/src/machine-daemon.js); [agent-router.js](https://github.com/giuliastro/harness-remote/blob/ee9d315c7a3329ab6ef5588d1565210167d47a9d/bridge/src/agent-router.js); [acp-service.js](https://github.com/giuliastro/harness-remote/blob/ee9d315c7a3329ab6ef5588d1565210167d47a9d/bridge/src/acp-service.js); [opencode-host.js](https://github.com/giuliastro/harness-remote/blob/ee9d315c7a3329ab6ef5588d1565210167d47a9d/bridge/src/opencode-host.js); [task-run-controller.js](https://github.com/giuliastro/harness-remote/blob/ee9d315c7a3329ab6ef5588d1565210167d47a9d/bridge/src/task-run-controller.js); [worktree-manager.js](https://github.com/giuliastro/harness-remote/blob/ee9d315c7a3329ab6ef5588d1565210167d47a9d/bridge/src/worktree-manager.js); [task-launch-server.js](https://github.com/giuliastro/harness-remote/blob/ee9d315c7a3329ab6ef5588d1565210167d47a9d/bridge/src/task-launch-server.js); [native-session-home-base.tsx](https://github.com/giuliastro/harness-remote/blob/ee9d315c7a3329ab6ef5588d1565210167d47a9d/web/src/components/native-session-home-base.tsx); [standalone-universal-workspace.tsx](https://github.com/giuliastro/harness-remote/blob/ee9d315c7a3329ab6ef5588d1565210167d47a9d/web/src/components/standalone-universal-workspace.tsx).

## Operational model

One or more autonomous coding agents run on the user's machines as normal native CLI Sessions. Harness Remote can launch native Task Runs or re-adopt existing sessions and routes prompts and returned events to the operator. The **operational reasoning owner** remains each individual coding agent, but each supported CLI session is an expressly assembled runtime component under the Harness Remote gateway. Removing those models leaves only a remote session controller. The narrow positive coordination mechanism is TaskDesk's optional per-task worktree isolation for concurrently operating S1s; no additional higher autonomy is presumed from displaying multiple Sessions or moving a task across agents.

## S1 — Operations

- State: A
- Function: perform real coding tasks in the project's filesystem/repository through supported autonomous coding-agent Sessions controlled and re-entered from a first-party remote workspace.
- Disturbance / variety regulated: changing coding instructions, native tool/compile/test results and repo changes that require each agent to choose further work.
- Decisive decision or feedback right: the configured Codex/Claude/OpenCode/OMP/PI agent chooses task-local analysis, code/tool actions and follow-up responses.
- Decision owner: the supported native coding-agent actor running on the target machine; its private internal logic is third-party substrate, not a Harness Remote feature.
- Supporting / enforcement mechanisms: Machine launcher/registry, ACP/OpenCode native adapters, TaskRunController, Session event transport, remote prompt/stop/approval UX and continuity metadata.
- Closure path: operator selects target project/Session or Task Run → Harness Remote resolves the installed native agent and forwards work → the agent independently executes code/tool loop in its project environment → native result/feedback is returned through gateway/session state → subsequent task-local actions follow.
- Boundary reachability: `npx harness-remote` gateway and desktop runtime are standard supported installed paths; agent discovery, session creation/attachment and prompts are executable features, not test-only examples.
- Why this is / is not agent-owned: remove the native coding-agent process and remote bridge cannot autonomously choose code changes; the assembled product deliberately delegates S1 to those operational actors without inheriting their proprietary planner, reviewer, control or identity subsystems.
- Evidence: [README.md](https://github.com/giuliastro/harness-remote/blob/ee9d315c7a3329ab6ef5588d1565210167d47a9d/README.md); [launcher.js](https://github.com/giuliastro/harness-remote/blob/ee9d315c7a3329ab6ef5588d1565210167d47a9d/bridge/src/launcher.js); [machine-daemon.js](https://github.com/giuliastro/harness-remote/blob/ee9d315c7a3329ab6ef5588d1565210167d47a9d/bridge/src/machine-daemon.js); [agent-router.js](https://github.com/giuliastro/harness-remote/blob/ee9d315c7a3329ab6ef5588d1565210167d47a9d/bridge/src/agent-router.js); [task-run-controller.js](https://github.com/giuliastro/harness-remote/blob/ee9d315c7a3329ab6ef5588d1565210167d47a9d/bridge/src/task-run-controller.js); [task-launcher.js](https://github.com/giuliastro/harness-remote/blob/ee9d315c7a3329ab6ef5588d1565210167d47a9d/bridge/src/task-launcher.js).
- Basis: explicit + structural.
- Confidence: high for supported runtime composition.
- Caveats: Harness Remote is explicitly **not** another coding agent and supplies no independent substitute for the external model/tool loop; providers/CLI authentication are prerequisites for real operation.

## S2 — Coordination

- State: C
- Function: attenuate file/index/branch interference among parallel TaskDesk agent S1 work cells by placing separate coding tasks in their own managed Git worktrees.
- Disturbance / variety regulated: simultaneous autonomous coding agents modifying the same project's mutable working tree, index or branch state can trample each other's uncommitted changes and invalidate task-local assumptions.
- Decisive decision or feedback right: create/select a distinct isolated worktree for a task before an agent run and deny destructive reuse or cleanup of an unsafe worktree.
- Decision owner: developer/operator-selected TaskDesk constructor mode; first-party deterministic WorktreeManager enforces task-specific isolation, without a packaged autonomous S2 planner dynamically deciding/negotiating the coordination policy.
- Supporting / enforcement mechanisms: task-id-derived worktree directory/branch, `git worktree add -B`, per-task stored workspace path, run launch against the selected path, dirty/unmerged-aware cleanup checks.
- Closure path: two TaskDesk tasks target one Git project → each optionally prepares a distinct managed worktree → launched agents receive their respective worktree paths → subsequent file/commit writes affect separate mutable checkouts; attempted unsafe cleanup is refused, preserving changes for later human integration.
- Boundary reachability: `WorktreeManager` is imported/used by `TaskRunController` and exposed through shipped task/worktree gateway routes; the task launch path accepts the recorded `task.workspace.path`, not an inert sample.
- Why this is / is not agent-owned: no first-party model negotiates isolation; the application implements a specific deterministic inter-S1 conflict-attenuation construction and thus this is C rather than A.
- Distinct S1 units: two separately launched autonomous coding-agent Task Runs (same original Git repository, distinct task identity/managed worktree and native Session).
- Inter-S1 disturbance: concurrently writing the same checkout's files/index/branch would cause cross-task collisions and loss of each task's independent working assumptions.
- Attenuating coordination relation: unique task-key path + branch created by Git worktree before launch, with per-task CWD passed to native agent session creation.
- Feedback into subsequent S1 behaviour: the agent's file/tool operations occur in its distinct worktree environment, while any worktree setup failure blocks the affected run; neither S1 mutates the other's live checkout as a consequence of this construction.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: code specifically prevents an identified concurrent *mutable repository workspace collision*, not simply grouping sessions by machine/project or recording lineage.
- Evidence: [worktree-manager.js](https://github.com/giuliastro/harness-remote/blob/ee9d315c7a3329ab6ef5588d1565210167d47a9d/bridge/src/worktree-manager.js); [task-run-controller.js](https://github.com/giuliastro/harness-remote/blob/ee9d315c7a3329ab6ef5588d1565210167d47a9d/bridge/src/task-run-controller.js); [task-launch-server.js](https://github.com/giuliastro/harness-remote/blob/ee9d315c7a3329ab6ef5588d1565210167d47a9d/bridge/src/task-launch-server.js); [task-launcher.js](https://github.com/giuliastro/harness-remote/blob/ee9d315c7a3329ab6ef5588d1565210167d47a9d/bridge/src/task-launcher.js).
- Basis: structural + explicit.
- Confidence: medium-high for TaskDesk managed-worktree mode.
- Caveats: isolation is **optional** and applies to prepared TaskDesk tasks, not existing native sessions, automatic merges, shared external resources or every cross-machine continuation. No claim of S2 agent discretion or general-purpose conflict resolution.

## S3 — Inside-and-now control

- State: ?
- Function: system-wide current work allocation, resource/priority/commitment regulation and intervention; positive S3 closure not yet established at the declared multi-machine workspace boundary.
- Disturbance / variety regulated: stalled/blocked sessions, incompatible concurrent work and unresponsive provider/harness runtimes are observable but the organization-wide current decision right is unproven.
- Decisive decision or feedback right: an operator can start, stop and continue particular sessions/tasks or switch target agents; a first-party whole-system decision/return authority over the **aggregate** current commitments was not reconstructed.
- Decision owner: session-level human choices plus deterministic gateway controls; any whole-system agent/parent S3 owner remains unresolved.
- Supporting / enforcement mechanisms: Machines→Projects→Sessions rail, attention inbox, TaskDesk run state, native session stop/continue, health reconciliation and adapter constraints.
- Closure path: individual remote session steering returns to that session, but no sufficiently evidenced global view → reprioritize/reallocate shared resources/accountability → return to multiple S1s as a coordinated current-control loop.
- Boundary reachability: native session dashboard and Task Runs are shipped; being controllable does not by itself prove whole-current regulation.
- Why this is / is not agent-owned: neither state aggregation nor deterministic retries/claims chooses a whole-workspace current objective or commitment; an external agent's internal manager is not donated.
- Whole-system current view: UI can display configured Machines, Projects, native Sessions and attention; whether that view supports function-level whole-current management rather than a session directory is unresolved.
- Current-control decision scope: current evidence supports individual session and task intervention; multi-agent resource bargaining, priorities or global work commitments were not established.
- Evidence: [native-session-home-base.tsx](https://github.com/giuliastro/harness-remote/blob/ee9d315c7a3329ab6ef5588d1565210167d47a9d/web/src/components/native-session-home-base.tsx); [standalone-universal-workspace.tsx](https://github.com/giuliastro/harness-remote/blob/ee9d315c7a3329ab6ef5588d1565210167d47a9d/web/src/components/standalone-universal-workspace.tsx); [task-run-controller.js](https://github.com/giuliastro/harness-remote/blob/ee9d315c7a3329ab6ef5588d1565210167d47a9d/bridge/src/task-run-controller.js); [machine-daemon.js](https://github.com/giuliastro/harness-remote/blob/ee9d315c7a3329ab6ef5588d1565210167d47a9d/bridge/src/machine-daemon.js); [native-session-attention-live.ts](https://github.com/giuliastro/harness-remote/blob/ee9d315c7a3329ab6ef5588d1565210167d47a9d/web/src/native-session-attention-live.ts).
- Basis: structural + unresolved.
- Confidence: medium in the insufficiency finding.
- Caveats: do not infer S3=P from a remote Stop button, user choosing another model or a catalog of sessions. Parent-mode closure would need function-specific whole-workspace decisions and effects on later S1 work.

## S3* — Complementary audit

- State: ?
- Function: independently check agent output against an alternative operational evidence route and return a corrective decision.
- Disturbance / variety regulated: agent self-reports that do not reflect real files, tests or operational results.
- Decisive decision or feedback right: not established; native Session review/diagnostics and project outcome reads are visibility mechanisms, not proven independent audit decision owners.
- Decision owner: unresolved.
- Supporting / enforcement mechanisms: native review evidence UI, transcript/cache reconciliation, project diagnostics and task outcome.
- Closure path: UI may present native evidence separately from the conversation, but no demonstrated independent reviewer verdict + corrective return to operating S1s was reconstructed.
- Boundary reachability: inspection surfaces exist in shipped web/bridge, but no positive S3* ownership is inferred.
- Why this is / is not agent-owned: outsourced coding-agent verification cannot be inherited and read-only diagnostics alone do not constitute independent challenges.
- Claim being audited: reported successful task completion/code change.
- Ordinary reporting path: native Session transcript/status and task-run record.
- Complementary access path: project outcome and native review evidence UI; genuine judgment independence remains uncertain.
- Independence boundary: a separate first-party challenger with outcome revision rights was not established.
- Who acts on findings: operator can intervene but an audited, function-specific return is unproven.
- Evidence: [native-session-review-evidence.ts](https://github.com/giuliastro/harness-remote/blob/ee9d315c7a3329ab6ef5588d1565210167d47a9d/web/src/native-session-review-evidence.ts); [project-identity.js](https://github.com/giuliastro/harness-remote/blob/ee9d315c7a3329ab6ef5588d1565210167d47a9d/bridge/src/project-identity.js); [task-context.js](https://github.com/giuliastro/harness-remote/blob/ee9d315c7a3329ab6ef5588d1565210167d47a9d/bridge/src/task-context.js); [README.md](https://github.com/giuliastro/harness-remote/blob/ee9d315c7a3329ab6ef5588d1565210167d47a9d/README.md).
- Basis: structural + unknown.
- Confidence: medium in insufficiency.
- Caveats: do not classify normal reconciliation as complementary audit.

## S4 — Outside-and-then intelligence

- State: ?
- Function: prospectively sense environmental changes and decide adaptations of the workspace's future operational capabilities.
- Disturbance / variety regulated: changing models/providers/projects and future coding needs.
- Decisive decision or feedback right: no established first-party prospective environmental option-generation/selection right.
- Decision owner: unresolved; operator/third-party native agent may choose future approaches but this is not demonstrated as Harness Remote's S4.
- Supporting / enforcement mechanisms: cross-agent and cross-machine continuation context, capability discovery, persistent lineage, model catalog and task outcome history.
- Closure path: handoff can transfer bounded *retrospective* objective/decision/unresolved task information into a new native Session, but no outside-and-then adaptive option → current-capability change loop is established.
- Boundary reachability: handoff and lineage are real first-party paths; this is not sufficient for S4.
- Why this is / is not agent-owned: passing context to a different coding agent is not by itself an autonomous future adaptation right.
- External distinction: external provider/model capabilities can be discovered but no prospective appraisal loop evidenced.
- Future / prospective distinction: continuation following existing work is mostly current/retrospective rather than strategic horizon sensing.
- Adaptation option generated: no function-specific prospective adaptation decision established.
- Path back into current capability / S3: no evidenced S4 return.
- Evidence: [cross-machine-handoff-server.js](https://github.com/giuliastro/harness-remote/blob/ee9d315c7a3329ab6ef5588d1565210167d47a9d/bridge/src/cross-machine-handoff-server.js); [cross-machine-target-runtime.js](https://github.com/giuliastro/harness-remote/blob/ee9d315c7a3329ab6ef5588d1565210167d47a9d/bridge/src/cross-machine-target-runtime.js); [session-link-store.js](https://github.com/giuliastro/harness-remote/blob/ee9d315c7a3329ab6ef5588d1565210167d47a9d/bridge/src/session-link-store.js); [task-context.js](https://github.com/giuliastro/harness-remote/blob/ee9d315c7a3329ab6ef5588d1565210167d47a9d/bridge/src/task-context.js); [README.md](https://github.com/giuliastro/harness-remote/blob/ee9d315c7a3329ab6ef5588d1565210167d47a9d/README.md).
- Basis: structural + unresolved.
- Confidence: medium in insufficient evidence.
- Caveats: another supported configuration may contain prospective adaptation; this review does not establish absence.

## S5 — Policy and identity

- State: ?
- Function: legitimate ultimate-policy and identity closure for the cross-machine operating workspace.
- Disturbance / variety regulated: conflicts about the purpose, governing authority or boundary of agent work.
- Decisive decision or feedback right: local owner selects machine credentials/root, target project, pairing and control capabilities; none alone is an identity-level ultimate-policy decision loop.
- Decision owner: human operator owns configuration/access, but function-specific S5 closure at the declared recursion is unresolved.
- Supporting / enforcement mechanisms: pairing token, allowed CORS origins, project identity checks, task/session authorization, gateway credential and local root boundary.
- Closure path: security/config choices affect permissible requests and handoff destination, but no issue concerning ultimate group purpose → authoritative judgment → returned identity policy was reconstructed.
- Boundary reachability: security and pairing are shipped, not sufficient to claim S5.
- Why this is / is not agent-owned: machine identity/credential checks and static policy do not grant an agent ultimate organizational authority.
- Identity / ultimate-policy issue: unverified.
- Ultimate authority in each claimed mode: no positive S5 mode claimed.
- Return-to-operation path: access decisions are enforced, but not shown to settle ultimate workspace policy.
- Evidence: [pairing-server.js](https://github.com/giuliastro/harness-remote/blob/ee9d315c7a3329ab6ef5588d1565210167d47a9d/bridge/src/pairing-server.js); [project-identity.js](https://github.com/giuliastro/harness-remote/blob/ee9d315c7a3329ab6ef5588d1565210167d47a9d/bridge/src/project-identity.js); [agent-router.js](https://github.com/giuliastro/harness-remote/blob/ee9d315c7a3329ab6ef5588d1565210167d47a9d/bridge/src/agent-router.js); [REFERENCE.md](https://github.com/giuliastro/harness-remote/blob/ee9d315c7a3329ab6ef5588d1565210167d47a9d/REFERENCE.md).
- Basis: structural + unresolved.
- Confidence: medium in insufficient evidence.
- Caveats: do not treat identity-token issuance, root path or project matching as VSM S5 identity-governance closure.

## Distributed OSS parent arrangement

The independent public maintainers of Harness Remote are not a runtime parent for every installed user workspace. Local/operator selection of machines and sessions is not evidence of a project-wide metasystem. TaskDesk worktrees remain local operating infrastructure, not OSS process governance.

## Self-hosted and non-human modes

A local Machine gateway and native coding agents can operate with the UI connected only intermittently. Native model/tool autonomy belongs to the assembled supported worker actors; all metadata and control routes remain first-party. A local human operating an individual session does not thereby provide a whole-system S3 parent, nor does a cross-machine pairing approval establish S5.

## Recursion

One configured machine/project/session federation is the focal operating workspace. Individual native coding Sessions are S1 work cells, and TaskDesk task-specific managed worktrees serve as interference-isolating environments. Other independent machines not paired to this federation, external providers and the OSS development organization are outside this declared recursion.

## Variety and escalation

Individual coding agents handle coding variety; deterministic worktrees attenuate task-local concurrent file conflicts; session claims and operation ledgers restrict duplicate control requests; client UI and health reconciliation surface attention to humans; handoff context preserves continuity but does not independently decide priorities/adaptation/policy.

## Evidence gaps

- Verify actual concurrent TaskDesk managed-worktree operating traces to reproduce S2=C isolation and confirm the specific launch path; do not extrapolate to pre-existing native sessions.
- Establish or refute a first-party *whole-workspace* current control loop before replacing S3=?, especially at multi-machine recursion.
- Inspect whether any evidence-review workflow independently challenges claims and returns correction (S3*), whether capability discovery ever supports prospective adaptation (S4), and whether an actual ultimate-policy issue closes (S5).
- No live connected-model coding run or remote machine pair/claim was executed; this is a pinned-source assessment of first-party shipped mechanisms.

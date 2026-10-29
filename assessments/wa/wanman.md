---
harness_id: wanman
project_name: wanman
repository: https://github.com/chekusu/wanman
review_ref: d3a8138de6c21981a4f1449a7b3f201e724c55c9
reviewed_at: 2026-10-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# wanman

## Review boundary

- System in focus: One locally running wanman Agent Matrix supervising a configured project, including its CEO, worker and optional specialist agent processes, shared task/initiative/capsule stores, messages and isolated workspaces.
- Purpose and identity: Continue a user-given software/project mission by distributing bounded work among model-using agents, monitoring current commitments and retaining local coordination state.
- Relevant environment: repo issues and roadmap changes, overlapping code edits, agent/process failures, subprocess tool observations, external events, CI and operator intervention.
- Standard-distribution boundary: OSS `@wanman/cli`, core and runtime packages, local takeover/run modes, JSON-RPC supervisor, bundled role instructions and SQLite stores; Claude Code or Codex subprocesses are configured execution dependencies.
- Credited operating / distribution surfaces: `packages/runtime/src` Supervisor/AgentProcess/TaskPool/ChangeCapsulePool/Relay and adapters; `packages/cli/src/takeover-project.ts`, takeover coordination and local execution; packaged cross-validation instructions.
- Adjacent first-party surfaces excluded from ownership: hosted wanman.ai services, optional db9 external brain service and global search, demos, tests, author development tools and arbitrary user-authored agent configurations; these do not automatically extend local OSS decision rights.
- First-party operating / deployment modes considered: `wanman takeover` generated project-aware CEO/CTO/dev/devops/feedback/marketing role set (specialists enabled only where source signals are sufficient); local `wanman run`, direct matrix config with continuous/on-demand agents, scoped tasks and change capsules, relay and external event/cron activation.
- Recursion level: a single supervised project-level agent matrix; its independently executing workers are S1 units, but a job/subprocess is not by itself a full lower-recursion viable organization.
- Reviewed revision: `d3a8138de6c21981a4f1449a7b3f201e724c55c9`.
- Observation date: 2026-10-29.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

wanman's local CLI talks to a Node.js JSON-RPC supervisor. The supervisor persists inter-agent messages, context, agent-owned tasks, initiatives, change capsules, hypotheses and artifacts, and launches per-role Claude/Codex subprocesses in isolated git worktrees and homes. A relay delivers steer messages with interruption priority; event subscriptions and cron can wake on-demand roles. A project takeover generates bundled CEO, CTO, dev, devops, feedback and marketing instructions from repository signals. The CEO's task board and change-capsule workflow forms a configurable model-owned current-control path; `TaskPool.checkConflict` rejects overlapping active path scopes, and `ChangeCapsulePool` rejects conflicting active change bundles. The feedback role can mine current issues/docs for potential backlog changes, but that alone does not demonstrate a future-environment options channel or constitutional S5. The bundled post-task cross-validation is performed by the same CEO, not an independent complementary auditor.

Primary frozen sources:

- [README: local modes and supervisor entry](https://github.com/chekusu/wanman/blob/d3a8138de6c21981a4f1449a7b3f201e724c55c9/README.md)
- [Architecture: subprocesses, messaging, worktrees and SQLite](https://github.com/chekusu/wanman/blob/d3a8138de6c21981a4f1449a7b3f201e724c55c9/docs/architecture.md)
- [Supervisor: current task admission, assignment and shared feedback](https://github.com/chekusu/wanman/blob/d3a8138de6c21981a4f1449a7b3f201e724c55c9/packages/runtime/src/supervisor.ts)
- [TaskPool: scope-overlap checks and dependencies](https://github.com/chekusu/wanman/blob/d3a8138de6c21981a4f1449a7b3f201e724c55c9/packages/runtime/src/task-pool.ts)
- [ChangeCapsulePool: high/weak overlap classification](https://github.com/chekusu/wanman/blob/d3a8138de6c21981a4f1449a7b3f201e724c55c9/packages/runtime/src/change-capsule-pool.ts)
- [Takeover role templates, eligibility and agent instructions](https://github.com/chekusu/wanman/blob/d3a8138de6c21981a4f1449a7b3f201e724c55c9/packages/cli/src/takeover-project.ts)
- [Takeover mission initiation and CEO steer](https://github.com/chekusu/wanman/blob/d3a8138de6c21981a4f1449a7b3f201e724c55c9/packages/cli/src/takeover-coordination.ts)
- [Cross-validation skill: CEO performs consistency review](https://github.com/chekusu/wanman/blob/d3a8138de6c21981a4f1449a7b3f201e724c55c9/packages/core/skills/cross-validation/SKILL.md)
- [Implementation-option engine](https://github.com/chekusu/wanman/blob/d3a8138de6c21981a4f1449a7b3f201e724c55c9/packages/runtime/src/exploration-engine.ts)
- [Human safety gate](https://github.com/chekusu/wanman/blob/d3a8138de6c21981a4f1449a7b3f201e724c55c9/packages/runtime/src/safety-gate.ts)

## Operational model

An operator selects a project, external CLI model runtime and high-level mission. The takeover generator constructs role prompts and a local supervisor; the CEO repeatedly reads shared tasks and source signals, decomposes work, assigns named worker agents and requests scoped capsules. An assigned worker receives a durable notification and runs in its isolated worktree, using model-selected tools; results and changed shared state feed the CEO's next cycle. Two overlapping active task scopes cannot both be admitted through the standard `task.create` RPC, and capsule creation rejects high-conflict simultaneous planned edits. This is substantive but bounded coordination, not a proof of globally race-free git collaboration. The packaged feedback/marketing roles provide present backlog/documentation observations, while ultimate project goals and permissions remain with the external operator.

## S1 — Operations

- State: A
- Function: implement delegated software/project tasks using model-selected code, CLI, research and documentation actions with tool-result feedback.
- Disturbance / variety regulated: heterogeneous scoped tasks, changing repo state, test failures, tool observations, local process interruption and external CLI environment variation.
- Decisive decision or feedback right: a worker or specialist model chooses how to perform its assigned work and which next tool operation follows an observed result.
- Decision owner: configured Claude Code/Codex model-backed dev, devops, feedback, marketing or other enabled agent process, not the JSON-RPC messaging wrapper.
- Supporting / enforcement mechanisms: AgentProcess run loop, runtime adapters, supervisor relay, per-agent worktrees/homes, task notifications and durable stores.
- Closure path: assigned goal/task → worker model/tool invocation → file/artifact/event result → subsequent model turn or run completion → shared task/result updates.
- Boundary reachability: documented `wanman takeover` and `wanman run` local entrypoints start first-party supervisor with real child CLI adapters; agent subprocesses are not merely illustrative external examples.
- Why this is / is not agent-owned: model workers choose substantive task solutions; deterministic startup, persistence and CLI routing implement rather than replace that choice.
- Evidence: README local run/takeover contract; docs/architecture.md sections 2, 3, 7–8; supervisor.ts; takeover-project.ts role prompts.
- Basis: structural exact-ref model/observation/action wiring; not inferred from a role label alone.
- Confidence: high for the shipped execution path, not for performance in live unbounded tasks.
- Caveats: external Claude/Codex credentials and executables are required; no live model execution was conducted.

## S2 — Coordination

- State: C
- Function: attenuate concurrent worker interference on overlapping project file scopes and conflicting change-capsule paths.
- Disturbance / variety regulated: separately operating dev agents attempting simultaneous commitments on the same path or high-conflict hot area, causing lost edits and merge collisions.
- Decisive decision or feedback right: reject new overlapping active task scopes and high-conflict capsule plans before a second competing work commitment is accepted.
- Decision owner: constructor-authored TaskPool/ChangeCapsulePool overlap rules, enforced by supervisor RPC admission; not a model-negotiated conflict adjudication.
- Supporting / enforcement mechanisms: path/prefix matching against nonterminal tasks, high-conflict capsule classification, task assignment notification, declared task dependencies and isolated worktrees.
- Closure path: proposed task/capsule scope → query active peer scopes → overlap classification → reject with explicit conflicting IDs or accept/assign → subsequent workers receive only admitted scoped work.
- Boundary reachability: overlap check occurs in shipped supervisor `TASK_CREATE`/capsule RPC paths used by local takeover; it is not a separate uncalled helper or merely recommended etiquette.
- Why this is / is not agent-owned: fixed collision rules enforce bounded eligibility; the CEO/worker models can select scopes but cannot override an RPC conflict response through ordinary creation.
- Distinct S1 units: separate agent subprocesses/roles operating in per-agent worktrees and receiving assigned project tasks.
- Inter-S1 disturbance: competing proposed task/capsule edits to the same path or protected hot file can undermine each other's results.
- Attenuating coordination relation: active-scope exclusion and high-conflict capsule rejection at shared project admission, with weaker conflicts surfaced as warnings.
- Feedback into subsequent S1 behaviour: rejected proposal returns a concrete conflict error to the submitting model, which must re-scope, defer or select different work; accepted assignment notifies its assignee.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: it detects a specific collision *between distinct worker scopes* and changes whether conflicting work is authorized, beyond carrying messages between agents.
- Evidence: task-pool.ts `scopesOverlap`/`checkConflict`; supervisor.ts `TASK_CREATE` and `CAPSULE_CREATE` branches; change-capsule-pool.ts; takeover-project.ts capsule instructions.
- Basis: first-party deterministic enforcement, bound to declared paths and admitted active records.
- Confidence: high for the collision gate; medium for coverage of all real git conflicts.
- Caveats: empty/inaccurate declared scopes, concurrent admission races or out-of-band editing can evade these checks; no global merge-safety guarantee is credited.

## S3 — Inside-and-now control

- State: A
- Function: supervise current multi-agent project work, prioritize and revise the active task and initiative portfolio, assign owners and request rework.
- Disturbance / variety regulated: idle workers, unresolved tasks, missed dependencies, changing present backlog, stale initiatives and active quality/PR blockers.
- Decisive decision or feedback right: a configured CEO model chooses near-term initiatives, task subdivision, priority, worker assignment and corrective follow-up from a shared current work view.
- Decision owner: packaged model-backed `ceo` role in the documented takeover mode; supervisor stores and routes its decisions and optional CTO reviews particular PRs.
- Supporting / enforcement mechanisms: InitiativeBoard, TaskPool with statuses and dependencies, shared artifacts/context, health/agent reports, priority steer/follow-up, takeover mission seed/agent instructions.
- Closure path: CEO reads project docs/tasks/worker results → creates/revises initiatives and bounded assignments → supervisor enforces and notifies S1 agents → completion and exception messages return to CEO for next-cycle decisions.
- Boundary reachability: takeover-project.ts installs a continuously active CEO with explicit `wanman initiative/task/capsule` workflow, while takeover-coordination.ts addresses it with mission/repair messages through the actual supervisor.
- Why this is / is not agent-owned: the CEO's model makes discretionary current-management judgments; SQLite stores and deterministic eligibility checks only implement portions of the work plan.
- Whole-system current view: current project agent list, initiative/task/capsule commitments and assigned outcomes accessible through the single matrix supervisor, not all of a customer's unrelated organizations.
- Current-control decision scope: active project decomposition, worker allocation and current correction within externally configured permissions and user mission; ultimate policy authority is not inferred.
- Evidence: takeover-project.ts CEO instructions and role config; takeover-coordination.ts mission dispatch; supervisor.ts task, initiative, capsule and agent RPC; docs/architecture.md shared stores.
- Basis: a packaged operational configuration with concrete observation, decision and task return paths.
- Confidence: medium-high for reachable first-party mode, not verified unattended performance.
- Caveats: bare custom matrices without the CEO role may have no comparable S3; project/operator remains the policy source.

## S3* — Complementary audit

- State: —
- Function: independent challenge of normal management/agent claims with a complementary observation path to current control.
- Disturbance / variety regulated: faulty self-report, concealed code regressions, inaccurate PR/test claims and inconsistent inter-agent evidence.
- Decisive decision or feedback right: a separate auditor tests operational facts and sends a correction demand to S3 independent of ordinary task-report owners.
- Decision owner: no first-party separately independent audit owner is established; the CEO itself performs packaged post-completion consistency checks, and CTO is in the ordinary current-work quality flow.
- Supporting / enforcement mechanisms: `cross-validation` skill, CTO PR review/coverage gate, work logs, scoped capsules and artifact metadata.
- Closure path: routine CEO/CTO review may create corrective tasks but is part of the same project's current operating management, without a distinct complementary audit challenge channel.
- Why this is / is not agent-owned: a model can check outputs, but the separately independent audit access/authority required for S3* is not evidenced by another prompt title or a recorded test outcome.
- Evidence: packages/core/skills/cross-validation/SKILL.md; takeover-project.ts CTO/CEO instructions; docs/architecture.md logs and capsule stores.
- Basis: independence/return-path comparison at the chosen project recursion.
- Confidence: medium-high for reviewed standard local modes.
- Caveats: a deployer could add an independent auditor, but no such custom augmentation is credited.

### Absence scope

- Surfaces inspected: cross-validation skill, CTO review instructions, capsule review fields, runtime event/log and task completion paths.
- Plausible first-party paths checked: CTO as S3*, CEO consistency checks as S3*, worktree isolation or logs as independent observation, reviewer metadata as audit authority.
- Why no material first-party path remains: all examined review actions are normal current-management/quality mechanisms or passive records; none establishes independent complementary inspection with a distinct challenge to project-level S3.

## S4 — Outside-and-then intelligence

- State: —
- Function: examine prospective external ecosystem changes and feed strategic adaptation options into present project capability decisions.
- Disturbance / variety regulated: future market, user and technology shifts that would make current project priorities/architecture unviable.
- Decisive decision or feedback right: commission/evaluate future-environment alternatives and propose a capability change for decision by current management.
- Decision owner: no bundled first-party project-level S4 owner established; the feedback role scans present issue/docs/backlog signals and the CEO extends the current roadmap.
- Supporting / enforcement mechanisms: feedback/marketing roles, issue and README scanning, hypothesis/initiative records and an implementation-option ExplorationEngine module.
- Closure path: feedback scans existing repo signals and suggests backlog tasks; implementation-option engine addresses a supplied implementation goal, not a materially wired external-future environmental interpretation/return channel.
- Why this is / is not agent-owned: a model's present backlog discovery or solution-option search does not itself entail a separate outside-and-then intelligence function.
- Evidence: takeover-project.ts feedback/marketing and CEO instructions; takeover-mission.ts seeds; exploration-engine.ts and workflow-orchestrator.ts.
- Basis: inspected configured role missions and absence of a credited prospective project S3–S4 closure.
- Confidence: medium; a suitable user-created agent matrix may add this, beyond the credited package configuration.
- Caveats: the project may support prospective research tasks in principle; assessed ownership requires a concrete standard-mode function rather than prompt potential.

### Absence scope

- Surfaces inspected: takeover feedback/marketing role instructions, mission seeds, hypotheses/initiatives RPCs and implementation-option/evaluation modules.
- Plausible first-party paths checked: issue mining as S4, roadmap re-scan as future-environment modeling, hypothesis board as strategic intelligence, uninvoked Explorer as a material S4 organization.
- Why no material first-party path remains: present documentation/backlog alignment and task implementation alternatives are not a distinct outside-and-then model; no standard-mode prospective environmental findings are returned as organizational capability adaptations to S3.

## S5 — Policy and identity

- State: —
- Function: legitimate settlement of ultimate project identity and policy disputes and authoritative return of the decision to the rest of the matrix.
- Disturbance / variety regulated: conflicting foundational goals, forbidden actions, mission legitimacy or unresolved current-versus-future organizational policy tension.
- Decisive decision or feedback right: an accepted constitutional authority decides whether and how to redefine the project mandate, not merely whether one task is approved.
- Decision owner: external human/project owner sets mission, runtime credentials, allowed operations and action approvals; the local named CEO is a current-work planner, not self-authorized ultimate policy authority.
- Supporting / enforcement mechanisms: supplied mission and AGENT.md, static safety-gate approvals, role permissions, external operator commands and mission-seed update.
- Closure path: human can change mission/config or approve a restricted action, which influences later runs, but no first-party identity-dispute detection/adjudication/return loop is wired for the declared project.
- Why this is / is not agent-owned: the label `CEO`, task priorities, action approvals and external user configuration do not establish a legitimate S5 arbitration mandate.
- Evidence: takeover-project.ts mission construction/CEO scope, safety-gate.ts human approvals, README operator/runtime configuration.
- Basis: mapped policy ownership and compared ordinary execution permission with identity-level closure.
- Confidence: medium-high for standard local operation.
- Caveats: the human operator may be part of a larger viable S5 outside wanman; this is not an evidenced integrated parent `P` feedback closure.

### Absence scope

- Surfaces inspected: generated mission, role prompts, CEO and CTO duties, safety gate, approvals and operator configuration.
- Plausible first-party paths checked: CEO title as S5, mission regeneration as constitutional choice, human operation approval as parent S5, static policy gate as ultimate identity mechanism.
- Why no material first-party path remains: ordinary roadmap priorities, external settings and task-level permissions do not constitute a materially routed ultimate policy dispute with authoritative organization-level closure.

## Recursion

Each independently spawned worker has its own S1 model/tool loop and workspace. The CEO's supervisor spans the declared project matrix, but worktrees, agent names and nested task IDs alone do not establish full lower-recursion viable systems. Optional external services and hosted wanman.ai are outside this local OSS boundary.

## Variety and escalation

Agent adapters absorb open-ended task variety; relay priorities and persistence turn messages or external events into new work. Task/capsule path gates attenuate bounded multi-agent edit conflict, and the model CEO can change current assignments based on task and artifact results. Human approval and escalations constrain specific risky actions; neither the approval gate nor the same-CEO consistency check is promoted to S5 or S3* respectively. Present repo/issue observation is credited to task planning, not prospective S4.

## Evidence gaps

- Exact-frozen-source analysis; no paid external model execution, multi-agent live project run, real branch merge conflict trial or operator decision was performed.
- Task scopes must be declared accurately: overlap checks cannot prove universal conflict-freedom, and the check-then-create ordering is not asserted to be an atomic race-proof reservation.
- CEO current-control grade is mode-specific (`wanman takeover` with suitable roles enabled), not a property of all arbitrary JSON agent matrices.
- Hosted wanman.ai feature claims, db9 external brain services, global search and arbitrary user-authored prompts were not counted as the local OSS system's own S4/S5 authority.

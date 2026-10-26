---
harness_id: dtadpole-heddle
project_name: Heddle
repository: https://github.com/dtadpole/heddle
review_ref: 6ae7e8dd80931c69946b3f1d75d523c77a99252d
reviewed_at: 2026-10-26
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Heddle

## Review boundary

- System in focus: one installed Heddle TypeScript/Cordis agent-harness instance and its optional, first-party Agent Teams operating mode; not the organization developing Heddle.
- Purpose and identity: run model-directed tasks against local workspaces through registered tools, durable sessions, and optional cooperating teammates.
- Relevant environment: local workspaces and files, the interactive operator, configured LLM endpoints, tool results, competing teammate work, and runtime permissions.
- Standard-distribution boundary: shipped source and documented `heddle` CLI/Web UI at frozen `6ae7e8dd80931c69946b3f1d75d523c77a99252d`; a configured model endpoint is an execution prerequisite, not an independently credited outside controller.
- Credited operating / distribution surfaces: `src/agent/loop.ts`, `src/boot.ts`, `src/cli.ts`, `src/plugins/{team,subagent-tool,goal-driver,tools}.ts`, `src/team/{service,state,tool,policy}.ts`, model/context/session/goal/tool/sandbox/approval services and root `heddle.patch.yml`. Team mode is included in that first-party profile but can be removed by another profile.
- Adjacent first-party surfaces excluded from ownership: `_verifiers_/`, `_tools_/`, `_context_/` DSH mechanism studies, `ULTIMATE_GOAL.md` and contributor `AGENTS.md`, CI/build/unit tests, development check runs and any higher-level external operator organization. These can corroborate code behaviour but are not automatically the installed product's regulator or independent auditor.
- First-party operating / deployment modes considered: single model/tool turn; goal-driven multi-round continuation; bounded subagent delegation; opt-in Agent Teams with live Lead, teammates and shared task board; operator permission and profile configuration; localhost Web UI.
- Recursion level: one local Heddle installation, with agent sessions as operational units. Individual child sessions do not thereby establish complete viable sub-organizations.
- Reviewed revision: `6ae7e8dd80931c69946b3f1d75d523c77a99252d`.
- Observation date: 2026-10-26.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Heddle's [README](https://github.com/dtadpole/heddle/blob/6ae7e8dd80931c69946b3f1d75d523c77a99252d/README.md) declares a configured Cordis plugin tree, model streaming, append-only session log, context budget/compaction, registered tools, workspace confinement, and localhost token-protected Web UI. [`boot`](https://github.com/dtadpole/heddle/blob/6ae7e8dd80931c69946b3f1d75d523c77a99252d/src/boot.ts) composes and loads the plugin tree. [`runTurn`](https://github.com/dtadpole/heddle/blob/6ae7e8dd80931c69946b3f1d75d523c77a99252d/src/agent/loop.ts) asks a configured model for the next response, executes selected tools, records results or refusals, then re-enters the model with updated context until it finishes or reaches a limit. Provider and tool selection are configured rather than owned by an external coding-agent executable.

The [first-party profile](https://github.com/dtadpole/heddle/blob/6ae7e8dd80931c69946b3f1d75d523c77a99252d/heddle.patch.yml) wires model, sessions, sandbox, approvals, goals, subagent delegation and an optional Team service with its nine model-facing tools. The [subagent implementation](https://github.com/dtadpole/heddle/blob/6ae7e8dd80931c69946b3f1d75d523c77a99252d/src/agent/subagent.ts) runs a child in a separate session, inherits the parent's permission mode, and returns the child's final text. Agent Teams add durable teammate sessions, messages, task revisions, claims, dependencies and Lead-only interventions. The [goal driver](https://github.com/dtadpole/heddle/blob/6ae7e8dd80931c69946b3f1d75d523c77a99252d/src/goal/driver.ts) reconciles an already-selected objective over subsequent turns; it does not independently research future external environments.

Permission approval, sandbox effects and task revision checks are deterministic enforcement. The operator sets profiles, tool access and ordinary approvals. The verifier runner, project goal ledger and DSH comparison materials evaluate or guide *development of Heddle*, rather than constituting an independent production audit, strategic regulator or runtime ultimate-policy body.

## Operational model

The primary S1 outcome is a model-selected investigation or file/tool action followed by a response persisted in its session. In Team mode, the Lead and spawned teammates each run independent model turns in distinct sessions against a shared workspace; each can decide how to work on a claimed task. The Lead has model-facing tools for observing all team members/tasks and for assigning, revising or stopping current work. Task revision conflicts and dependency/readiness checks give concrete inter-S1 collision evidence. The model's decisions are distinct from deterministic CAS refusal, file sandbox enforcement, approval handling and event transport.

## S1 — Operations

- State: A
- Function: produce requested workspace/task results through an iterative model/tool process.
- Disturbance / variety regulated: unknown files, tool observations, permission refusals, new user input and model/context limitations.
- Decisive decision or feedback right: select the next tool, arguments, follow-up investigation or final answer in light of returned observations.
- Decision owner: the model-driven root/teammate agent running `runTurn`; the operator supplies its objective and permitted environment.
- Supporting / enforcement mechanisms: Cordis loader, model adapter, context preparation/compaction, tool registry, sandbox, approvals, round limit and append-only session log.
- Closure path: agent tool choice → tool output/refusal persisted in session → context prepared for the next model round → revised agent choice or completed result.
- Boundary reachability: normal `heddle` CLI/Web modes use `runTurn`; the optional Team plugin also calls the same loop for teammate turns. No outside coding-agent CLI is needed for the witness.
- Why this is / is not agent-owned: without the model's ongoing decisions, deterministic transport and tool handling cannot choose the task-specific next action.
- Evidence: [loop](https://github.com/dtadpole/heddle/blob/6ae7e8dd80931c69946b3f1d75d523c77a99252d/src/agent/loop.ts), [Team plugin](https://github.com/dtadpole/heddle/blob/6ae7e8dd80931c69946b3f1d75d523c77a99252d/src/plugins/team.ts), [profile](https://github.com/dtadpole/heddle/blob/6ae7e8dd80931c69946b3f1d75d523c77a99252d/heddle.patch.yml).
- Basis: structural.
- Confidence: high.
- Caveats: source evidence establishes an executable decision/action path, not model task quality or reliability; no live provider run was made.

## S2 — Coordination

- State: A
- Function: attenuate work-claim and ordering conflicts between distinct teammate S1 units on one team board.
- Distinct S1 units: Lead and autonomous teammate turns, or two independently running teammates whose work shares the team task board and filesystem.
- Inter-S1 disturbance: competing claims of one pending task, a stale task update after another teammate's change, or an attempt to start work before a dependent task is complete. Concurrent write-scope overlap is also surfaced as a warning, not a hard filesystem lock.
- Attenuating coordination relation: version-checked `claim`/update, owner enforcement, dependency readiness, task views with scope-overlap warnings and direct teammate messaging. Agents can choose available work or revise task dependencies/claims after reading the resulting state.
- Feedback into subsequent S1 behaviour: stale or occupied claims are refused with explicit error codes; the agent receives those tool results, can re-read the board and select a different claim or coordinate with another member before acting.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: compare-and-set revisions and ownership/readiness constraints explicitly address collisions among competing task actors; the returned conflict state changes which task work can begin. The mailbox alone would not suffice.
- Disturbance / variety regulated: conflicting claims, out-of-date plans, blocked dependencies and overlapping teammate work.
- Decisive decision or feedback right: select/revise task ownership and dependency handling in response to live conflict signals.
- Decision owner: Team-mode agents acting through the model-facing task tools; fixed CAS and access checks only enforce their attempts. The Lead also has the supervisory reassign right separately considered under S3.
- Supporting / enforcement mechanisms: durable `team/task` event fold, revision comparison, ownership/lead checks, dependency DAG validation, `TEAM_TASK_STALE`/`TEAM_TASK_BLOCKED` refusals and notification/mail transport.
- Closure path: multiple teammates read shared work → agent proposes claim/plan → service accepts or refuses based on current conflict/dependency state → result enters agent's next model round → agent adjusts work selection or message/claim; accepted updates become the next shared task state.
- Boundary reachability: the shipped `team` plugin registers task tools in `heddle.patch.yml` and wires them to the actual team session log; no developer-only verifier or external coordinator is borrowed.
- Why this is / is not agent-owned: agents retain choice over which eligible tasks to claim, which conflicts to resolve by messaging and how to revise dependencies; removing their choices leaves only fixed admission guards, not a complete discretionary coordination response. This is a supported optional mode, not a claim that every single-agent run has S2.
- Evidence: [task state and CAS](https://github.com/dtadpole/heddle/blob/6ae7e8dd80931c69946b3f1d75d523c77a99252d/src/team/state.ts), [model-facing task tools](https://github.com/dtadpole/heddle/blob/6ae7e8dd80931c69946b3f1d75d523c77a99252d/src/team/tool.ts), [Team service](https://github.com/dtadpole/heddle/blob/6ae7e8dd80931c69946b3f1d75d523c77a99252d/src/team/service.ts), [policy note](https://github.com/dtadpole/heddle/blob/6ae7e8dd80931c69946b3f1d75d523c77a99252d/src/team/policy.ts).
- Basis: structural.
- Confidence: medium-high.
- Caveats: write scopes are advisory; source supplies the decision and feedback channel, not an observed conflict-resolution quality result. An operator may direct a team, but no S2 parent notation is used.

## S3 — Inside-and-now control

- State: A
- Function: maintain whole-team current commitments and intervene across multiple ongoing task cells.
- Whole-system current view: model-facing `list_agents` and `team_task_list` expose all members, their live/durable states, task readiness, owners, revisions and dependency blockers.
- Current-control decision scope: the Lead can create and revise shared tasks/dependencies, reassign a teammate's claimed work, reopen work, stop an active teammate turn and send corrective instructions; ordinary teammates cannot reassign someone else's owned task.
- Disturbance / variety regulated: an overloaded, blocked, stale or misassigned current team whose shared commitments cannot be resolved within one task cell.
- Decisive decision or feedback right: choose a whole-team assignment/priority/intervention based on the current board and member statuses, including interruption or reallocation.
- Decision owner: the model-driven Team Lead in the first-party Team mode. Lead-only role checks and cancellation machinery enforce its chosen action; they do not choose the intervention.
- Supporting / enforcement mechanisms: full team state fold, task ownership and revision gates, `requireLead`, turn registry and abort signal, serialized message delivery.
- Closure path: Lead obtains team-wide status → decides to reassign/reopen/stop/message → Team service updates authoritative task/member operation or aborts a turn → affected teammate receives changed work/steered instruction and subsequent operation follows it.
- Boundary reachability: first-party Team plugin registers `list_agents`, `team_task_list`, `team_task_update`, `send_message` and `interrupt_agent`, with Lead authority and live `turns` support wired in the supplied profile. It does not depend on private contributor orchestration.
- Why this is / is not agent-owned: the Lead must select which live commitments to change; the runtime merely rejects illegal states and carries the selected change. A team-less profile has no S3 claim from this mechanism.
- Evidence: [Team service](https://github.com/dtadpole/heddle/blob/6ae7e8dd80931c69946b3f1d75d523c77a99252d/src/team/service.ts), [task intervention rules](https://github.com/dtadpole/heddle/blob/6ae7e8dd80931c69946b3f1d75d523c77a99252d/src/team/state.ts), [Team tools](https://github.com/dtadpole/heddle/blob/6ae7e8dd80931c69946b3f1d75d523c77a99252d/src/team/tool.ts), [profile](https://github.com/dtadpole/heddle/blob/6ae7e8dd80931c69946b3f1d75d523c77a99252d/heddle.patch.yml).
- Basis: structural.
- Confidence: medium-high.
- Caveats: no claim of effective real-world team governance or independent current-performance metrics; hard limits and goal-round continuation alone would not establish S3. Operator instructions over ordinary tasks do not separately prove an S3 parent mode.

## S3* — Complementary audit

- State: —
- Function: no material first-party complementary independent audit-return path established for the installed team/product at this boundary.
- Disturbance / variety regulated: a teammate's potentially incorrect completion report or misleading task status.
- Decisive decision or feedback right: an independently controlled judgment against direct operational evidence and subsequent corrective feedback is not a shipped Team-mode control loop.
- Decision owner: the development-side verifier owners govern the separate project-checking process; runtime Lead/teammates can inspect and review but do not instantiate an independently governed complementary auditor by default.
- Supporting / enforcement mechanisms: session/event logs, task status, developer `_verifiers_`, offline unit tests and review collection scripts.
- Closure path: team task completion/status may inform routine Lead decisions; no separately controlled audit-of-reporting decision and return into Team control is established.
- Why this is / is not agent-owned: a verifier for Heddle's own implementation and ordinary self-reported task completion are not independent inspections of teammates' operating reality at this recursion.
- Evidence: [Team service](https://github.com/dtadpole/heddle/blob/6ae7e8dd80931c69946b3f1d75d523c77a99252d/src/team/service.ts), [verifier boundary](https://github.com/dtadpole/heddle/blob/6ae7e8dd80931c69946b3f1d75d523c77a99252d/ULTIMATE_GOAL.md), [review collection](https://github.com/dtadpole/heddle/blob/6ae7e8dd80931c69946b3f1d75d523c77a99252d/_tools_/review-collect/INDEX.md).
- Basis: structural, bounded negative.
- Confidence: medium.
- Caveats: a user can independently instruct a teammate to inspect raw artifacts, but general tool expressiveness does not establish the function-specific independence and returned control in the shipped operating mode.

### Absence scope

- Surfaces inspected: team tools/state/service/policy, agent loop, session event logs, verifier and review-collection entry points, root profile and product README.
- Plausible first-party paths checked: Lead inspection of task status, teammate reviews via ordinary prompts, read-only tool access, `_verifiers_` and review collection.
- Why no material first-party path remains: none wires a complementary, sufficiently independent direct-evidence audit judgment into team control; the concrete verifier surface judges development artifacts rather than the operating S1 claims. Possible custom composition is outside the evidenced standard mode.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material prospective external-environment sensing, option development and return into installed team capability.
- Disturbance / variety regulated: future model/tool/environment changes rather than current task context or failure recovery.
- Decisive decision or feedback right: choose adaptation of the installation's future capability based on externally derived options; no such shipped decision path is identified.
- Decision owner: operator/developer can update plugins and profiles outside the running organizational loop.
- Supporting / enforcement mechanisms: persistent session/context, context compaction, goal continuation, endpoint selection and dynamic Cordis plugin loading.
- Closure path: goals continue present work and context summaries feed the next task round; neither supplies prospective external intelligence with adopted strategic adaptation.
- Why this is / is not agent-owned: context and goal maintenance are within-task operations; plugin extensibility is not itself an adaptation regulator.
- Evidence: [goal driver](https://github.com/dtadpole/heddle/blob/6ae7e8dd80931c69946b3f1d75d523c77a99252d/src/goal/driver.ts), [context composition](https://github.com/dtadpole/heddle/blob/6ae7e8dd80931c69946b3f1d75d523c77a99252d/src/context/service.ts), [boot/configuration](https://github.com/dtadpole/heddle/blob/6ae7e8dd80931c69946b3f1d75d523c77a99252d/src/boot.ts).
- Basis: structural, bounded negative.
- Confidence: medium-high.
- Caveats: custom plugins or an operator's separate adaptation program would require a new declared boundary and evidence.

### Absence scope

- Surfaces inspected: goals and driver, context/compaction, model routing, plugin/profile configuration, team commands, README and development goals.
- Plausible first-party paths checked: goal-driven self-continuation, memory/context adaptation, model/endpoint selection, optional plugins and future roadmaps.
- Why no material first-party path remains: available feedback concerns current sessions or static extension; no shipped externally prospective investigation-to-option-to-operational-capability return path is established.

## S5 — Policy and identity

- State: —
- Function: no material installed-instance identity or ultimate-policy resolution loop is established.
- Disturbance / variety regulated: potential identity-level tensions about purpose or ultimate permissible operation, distinct from an ordinary tool authorization.
- Decisive decision or feedback right: legitimate ultimate-policy judgment with an authoritative return to subsequent operation; not supplied by Heddle's approval dialogs.
- Decision owner: operator selects standing permissions and profiles; project maintainer owns the separate product-development goal, not a shipped identity-level governance loop.
- Supporting / enforcement mechanisms: `allow`/`deny`/`ask` tool permissions, per-call approval, sandbox modes, configuration file and team-role rules.
- Closure path: human approval or denial returns to one tool call; it does not carry an identity/ultimate-policy issue to a legitimate parent and return a durable policy resolution.
- Why this is / is not agent-owned: the model cannot revise ultimate identity through a first-party policy-authority path; operator's ordinary edit/approval is not automatically S5=P.
- Evidence: [approval service](https://github.com/dtadpole/heddle/blob/6ae7e8dd80931c69946b3f1d75d523c77a99252d/src/approvals/service.ts), [sandbox policy](https://github.com/dtadpole/heddle/blob/6ae7e8dd80931c69946b3f1d75d523c77a99252d/src/sandbox/policy.ts), [development goal](https://github.com/dtadpole/heddle/blob/6ae7e8dd80931c69946b3f1d75d523c77a99252d/ULTIMATE_GOAL.md).
- Basis: structural, bounded negative.
- Confidence: high.
- Caveats: an operator's real organization can have S5 outside this local installed harness.

### Absence scope

- Surfaces inspected: approvals, sandbox, config/profile, team role and policy, goal service, public project goal/verification documentation.
- Plausible first-party paths checked: ask-mode approvals, static permissions, team leader role, persistent goal and owner's development-completion decision.
- Why no material first-party path remains: all first-party runtime returns govern tool/task operations or developer-maintained configuration; the project-completion owner is in a separate development recursion. No shipped identity-level parent request/decision/return loop remains.

## Distributed OSS parent arrangement

Heddle is an installable, local, operator-configured OSS harness. Public maintainer work and project verification do not establish parent S3/S4/S5 closure for each user's installed team. The runtime Team Lead is an agent role for present team control, not by itself the project's ultimate parent authority.

## Self-hosted and non-human modes

The root profile includes optional teams; another named profile may omit them. Single-agent sessions remain S1 without claiming team-specific S2/S3. Local human approvals do not turn normal tool gates into S3/S4/S5 parent notation. No special non-human ultimate-governance mode is documented.

## Recursion

Distinct durable teammate sessions can be S1 operating cells, but their creation, nested turns, independent logs and inherited permissions do not establish full recursively viable organizations for each child.

## Variety and escalation

The model-tool observation cycle absorbs local task variety. CAS task claims and dependency checks attenuate concurrent team collisions; Lead-only reassignment/interruption enables higher-level current intervention. Role/permission/sandbox guards constrain allowed actions without selecting organizational policy. Model errors, task status and team messages can reach another turn, but are not by themselves algedonic governance channels.

## Evidence gaps

No live LLM/provider, Browser or coding-agent quality/performance test was performed. Model-backed decisions and team cooperation are source-grounded operating capabilities, not measured effectiveness claims. Cross-process concurrency/atomicity of the event journal and the quality of agents' conflict handling were not experimentally evaluated; this does not change the source-level existence of CAS/refusal paths. An alternative profile or deployment that omits Team mode should be assessed at its own narrower boundary.

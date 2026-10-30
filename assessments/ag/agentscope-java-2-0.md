---
harness_id: agentscope-java-2-0
project_name: AgentScope Java 2.0
repository: https://github.com/agentscope-ai/agentscope-java
review_ref: 3d1b998d7c1c0aa6d9697a85b59c205a4c7c2a0f
reviewed_at: 2026-10-30
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

# AgentScope Java 2.0

## Review boundary

- System in focus: the packaged Java `ReActAgent` / `HarnessAgent` runtime, including opt-in first-party team mode, not the hosted AgentScope Service as a second autonomous organization.
- Purpose and identity: configure and run long-lived model-backed agents with tool use, memory, workspaces, subagents and optionally coordinated team execution.
- Relevant environment: tasks, model/provider output, tool observations, team task ownership and dependencies, failures, persisted sessions and permission confirmations.
- Standard-distribution boundary: `agentscope-core`, `agentscope-harness` shipped Java libraries; configured builder paths for subagents and teams, using first-party `TeamClient`, `TeamsMiddleware` and `TeamTool`.
- Credited operating / distribution surfaces: [`ReActAgent.java`](https://github.com/agentscope-ai/agentscope-java/blob/3d1b998d7c1c0aa6d9697a85b59c205a4c7c2a0f/agentscope-core/src/main/java/io/agentscope/core/ReActAgent.java), [`HarnessAgent.java`](https://github.com/agentscope-ai/agentscope-java/blob/3d1b998d7c1c0aa6d9697a85b59c205a4c7c2a0f/agentscope-harness/src/main/java/io/agentscope/harness/agent/HarnessAgent.java), [`TeamsMiddleware.java`](https://github.com/agentscope-ai/agentscope-java/blob/3d1b998d7c1c0aa6d9697a85b59c205a4c7c2a0f/agentscope-harness/src/main/java/io/agentscope/harness/agent/middleware/TeamsMiddleware.java), [`TeamTool.java`](https://github.com/agentscope-ai/agentscope-java/blob/3d1b998d7c1c0aa6d9697a85b59c205a4c7c2a0f/agentscope-harness/src/main/java/io/agentscope/harness/agent/tool/TeamTool.java), [`LocalTeamClient.java`](https://github.com/agentscope-ai/agentscope-java/blob/3d1b998d7c1c0aa6d9697a85b59c205a4c7c2a0f/agentscope-harness/src/main/java/io/agentscope/harness/agent/team/LocalTeamClient.java).
- Adjacent first-party surfaces excluded from ownership: documentation/demo programs, test and benchmark harnesses, contributor/CI/release systems and hosted control-plane/service administrative decisions; external model backends, remote MCP servers and end-user application code are not credited as agents in this Java runtime.
- First-party operating / deployment modes considered: single ReAct/HarnessAgent mode; opt-in subagents; builder-configured first-party `teamsModeClient`/`teamsModeContext` mode with team lead and workers; self-hosted local/shared/sandbox state and permission modes.
- Recursion level: one team of operational agent cells when team mode is configured; not the entire independent open-source contributor organization.
- Reviewed revision: `3d1b998d7c1c0aa6d9697a85b59c205a4c7c2a0f`.
- Observation date: 2026-10-30.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

`HarnessAgent` builds on the model–reason–act loop of `ReActAgent`; it supplies workspace, persistence, memory/compaction, sandbox/filesystem, skill and permission middleware, optional local/remote subagents and opt-in team mode. `HarnessAgent.Builder` actually wires `TeamsMiddleware` and its model-facing `TeamTool` when a team client/context are configured; this is not an example-only interface. Team tools include task create/assign/claim/unclaim/complete/fail, messaging, teammate lifecycle, plan approval/rejection and team completion, with role clipping. `LocalTeamClient` persists the shared board and uses versioned compare-and-swap and `blockedBy` checks to reject conflicting claims. At every team lead turn `TeamsMiddleware` renders the entire board with owners, results, outstanding commitments and completion conditions; worker notifications return after claims, failures and completions. Separately, `SkillManageTool` can draft skills and `SkillCuratorMiddleware` runs periodic hygiene with configurable promotion gates. Hosted service consoles, examples, tests and deployment administrators are adjacent and must not donate decision ownership.

## Operational model

The model owns task decomposition, tool selection and, in the supported team mode, lead decisions about which work belongs to whom. Versioned board writes and wakeup delivery enforce/transport those decisions. The S2 and S3 findings below are specific to **configured team mode**, not claims that a single standalone ReActAgent already has an internal multisystem metasystem. Permission, sandbox and skill-governance controls are operator/runtime concerns unless their own organizational right and closure can be proved.

## S1 — Operations

- State: A
- Function: model-directed reasoning and tool action for supplied tasks, including delegated independent subtasks in team mode.
- Disturbance / variety regulated: heterogeneous inputs, tool results/failures, context size, state recovery and diverse task subtasks.
- Decisive decision or feedback right: agent chooses reasoning, next tool or teammate task action on feedback.
- Decision owner: model-backed ReAct/HarnessAgent and configured team worker/lead agent roles.
- Supporting / enforcement mechanisms: `Toolkit`, model/permission middleware, `AgentStateStore`, workspace/sandbox, tool transport and invocation limits.
- Closure path: prompt/state → model choice → tool call → tool result/event → subsequent model decision or task completion.
- Boundary reachability: `ReActAgent` is the packaged core and `HarnessAgent.Builder` creates it with installed middleware and model/tool registries.
- Why this is / is not agent-owned: model makes semantic operational selections, while Java classes enforce schema/permission and handle state/transport.
- Evidence: [`ReActAgent.java`](https://github.com/agentscope-ai/agentscope-java/blob/3d1b998d7c1c0aa6d9697a85b59c205a4c7c2a0f/agentscope-core/src/main/java/io/agentscope/core/ReActAgent.java), [`HarnessAgent.java`](https://github.com/agentscope-ai/agentscope-java/blob/3d1b998d7c1c0aa6d9697a85b59c205a4c7c2a0f/agentscope-harness/src/main/java/io/agentscope/harness/agent/HarnessAgent.java), [`architecture.md`](https://github.com/agentscope-ai/agentscope-java/blob/3d1b998d7c1c0aa6d9697a85b59c205a4c7c2a0f/docs/v2/en/docs/harness/architecture.md).
- Basis: structural.
- Confidence: high for documented installed call path.
- Caveats: hosted models, tools, data and application goals are caller-provided.

## S2 — Coordination

- State: A
- Function: mitigate competing work claims and contradictory or dependent teammate progress within one active team.
- Disturbance / variety regulated: multiple operational members may claim the same task, act before predecessors finish or report incompatible conclusions.
- Distinct S1 units: multiple team-worker/lead model-backed `HarnessAgent` instances identified by team+member and operating on independent tasks.
- Inter-S1 disturbance: competing task ownership and `blockedBy` dependencies; team lead prompt also requires resolution of disagreements among teammate results.
- Attenuating coordination relation: a shared versioned task board implements exclusive compare-and-swap claims/assignments and dependency blocking; model lead sees team reports and can resolve disagreements/reassign work.
- Feedback into subsequent S1 behaviour: conflicts return as tool errors; successful assignment or completion wakes the affected member and injects the task/result into its next reasoning turn.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: unlike a generic mailbox or task fan-out, task-ownership CAS and dependency checks prevent structurally specified competing operations and the team lead is explicitly prompted to reconcile conflicting teammate conclusions.
- Decisive decision or feedback right: choose task allocation/reassignment or reconcile disagreements; prevent double claims and notify the next legitimate worker.
- Decision owner: lead/worker model agents for allocation and response to feedback; `LocalTeamClient` deterministically rejects invalid claims.
- Supporting / enforcement mechanisms: `TeamClient`, CAS store, task owner/blockedBy fields, `TeamTool`, `TeamsMiddleware` wakeups/inbox.
- Closure path: attempted claim/assignment → conflict/dependency check → changed board or denial → model/worker wakes, selects eligible work or lead reallocates it.
- Boundary reachability: `HarnessAgent.Builder` registers `TeamsMiddleware` and `TeamTool` when `teamsModeClient/context` are supplied; `TeamsMiddleware` feeds board and reconciliation instructions to live model reasoning, not only tests.
- Why this is / is not agent-owned: the semantics of allocation/reconciliation belong to team agent choices; CAS is a necessary integrity enforcer but not the owner of team task discretion.
- Evidence: [`LocalTeamClient.java`](https://github.com/agentscope-ai/agentscope-java/blob/3d1b998d7c1c0aa6d9697a85b59c205a4c7c2a0f/agentscope-harness/src/main/java/io/agentscope/harness/agent/team/LocalTeamClient.java), [`TeamTask.java`](https://github.com/agentscope-ai/agentscope-java/blob/3d1b998d7c1c0aa6d9697a85b59c205a4c7c2a0f/agentscope-harness/src/main/java/io/agentscope/harness/agent/team/TeamTask.java), [`TeamsMiddleware.java`](https://github.com/agentscope-ai/agentscope-java/blob/3d1b998d7c1c0aa6d9697a85b59c205a4c7c2a0f/agentscope-harness/src/main/java/io/agentscope/harness/agent/middleware/TeamsMiddleware.java), [`TeamTool.java`](https://github.com/agentscope-ai/agentscope-java/blob/3d1b998d7c1c0aa6d9697a85b59c205a4c7c2a0f/agentscope-harness/src/main/java/io/agentscope/harness/agent/tool/TeamTool.java).
- Basis: structural.
- Confidence: medium-high, conditional on team mode and genuine multiple members.
- Caveats: the CAS subpath is deterministic; A relies on the wired model lead/worker feedback decisions in actual team operation, not CAS in isolation.

## S3 — Inside-and-now control

- State: A
- Function: control present team-wide commitments, task ownership and completion across multiple active workers.
- Disturbance / variety regulated: a lead losing track of allocated work, failed tasks, idle team members and incomplete team commitments.
- Whole-system current view: `TeamsMiddleware.renderBoardDigest` supplies the team lead with every task, state, owner, settled result, and the set of tasks it still owns; refreshed at each turn.
- Current-control decision scope: lead model may create/assign/reassign tasks, spawn/shutdown members, reject/approve plans and complete a team only when the board is settled; worker actions are role-clipped.
- Decisive decision or feedback right: model lead interprets board and member feedback, decides which current work to assign, rescue or close.
- Decision owner: lead model-backed agent in configured team mode, not the deterministic board or external user.
- Supporting / enforcement mechanisms: role-scoped `TeamTool`, board persistence, wakeups, CAS and terminal-state checks.
- Closure path: whole-board digest/member failure notice → lead decides intervention → `TeamTool` updates assignment/team/membership → changed worker tasks and later digest.
- Boundary reachability: source builder wires team middleware and tools into the actual model call, and live `onReasoning` injects refreshed whole-team board into the lead's system message.
- Why this is / is not agent-owned: model is instructed and equipped to reason over entire board and select interventions; runtime enforces ownership and delivery but has no equivalent semantic resource/commitment judgment without the lead.
- Evidence: [`TeamsMiddleware.java`](https://github.com/agentscope-ai/agentscope-java/blob/3d1b998d7c1c0aa6d9697a85b59c205a4c7c2a0f/agentscope-harness/src/main/java/io/agentscope/harness/agent/middleware/TeamsMiddleware.java) (`renderBoardDigest`, `renderTeamSection`), [`TeamTool.java`](https://github.com/agentscope-ai/agentscope-java/blob/3d1b998d7c1c0aa6d9697a85b59c205a4c7c2a0f/agentscope-harness/src/main/java/io/agentscope/harness/agent/tool/TeamTool.java), [`HarnessAgent.java`](https://github.com/agentscope-ai/agentscope-java/blob/3d1b998d7c1c0aa6d9697a85b59c205a4c7c2a0f/agentscope-harness/src/main/java/io/agentscope/harness/agent/HarnessAgent.java) (team mode wiring).
- Basis: structural.
- Confidence: medium-high for wired conditional mode.
- Caveats: team governance is scoped to one run/team, not all externally deployed AgentScope users or cloud admin service.

## S3* — Complementary audit

- State: —
- Function: no separate sufficiently independent inspection of ordinary team reports is established by the inspected runtime.
- Disturbance / variety regulated: team worker errors, tool violations and misleading reports can be observed but only via ordinary logs, tests, task results and permission checks.
- Decisive decision or feedback right: model lead receives worker reports through the same team task board; no separate independent operational-reality access/judgment/return exists in the standard team runtime.
- Decision owner: regular team lead and configured verification hooks; not an independent audit unit.
- Supporting / enforcement mechanisms: `AgentTraceMiddleware`, permission system, tests, task state and logs.
- Closure path: results and tool denials reach ordinary operating agents; no independent audit findings flow to team-wide corrective authority.
- Why this is / is not agent-owned: a reviewer subagent can be configured, but the generic declaration and agent trace alone cannot establish an independent complementary access path.
- Evidence: [`TeamsMiddleware.java`](https://github.com/agentscope-ai/agentscope-java/blob/3d1b998d7c1c0aa6d9697a85b59c205a4c7c2a0f/agentscope-harness/src/main/java/io/agentscope/harness/agent/middleware/TeamsMiddleware.java), [`AgentTraceMiddleware.java`](https://github.com/agentscope-ai/agentscope-java/blob/3d1b998d7c1c0aa6d9697a85b59c205a4c7c2a0f/agentscope-harness/src/main/java/io/agentscope/harness/agent/middleware/AgentTraceMiddleware.java), [`subagent.md`](https://github.com/agentscope-ai/agentscope-java/blob/3d1b998d7c1c0aa6d9697a85b59c205a4c7c2a0f/docs/v2/en/docs/harness/subagent.md).
- Basis: structural.
- Confidence: medium.
- Caveats: independently built application-specific auditors remain possible outside the credited mode.

### Absence scope

- Surfaces inspected: ReAct/HarnessAgent construction, team board/results, trace middleware, documented subagent reviewer configuration, permission and runtime tests.
- Plausible first-party paths checked: worker review role, team lead result collation, permission checks, persistent traces and test failure routes.
- Why no material first-party path remains: each is ordinary delegation, production reporting, enforcement or development QA; no separately independent audit judgment of operational reality returns into current control.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party externally oriented prospective option-development loop linked to adaptation of present team capability is established.
- Disturbance / variety regulated: new user requests and accumulated skill usage change task execution and skill hygiene, not a modeled future environment or strategic response.
- Decisive decision or feedback right: optional agent may propose/edit skills; optional human/local gate promotes them; periodic curator archives stale skills and optionally dry-runs merges.
- Decision owner: agent for task-local skill drafting, operator for promotion, deterministic curator schedule for hygiene; none demonstrably owns S4 prospective adaptation.
- Supporting / enforcement mechanisms: `SkillManageTool`, promotion filters/gates, `SkillCuratorMiddleware`, memory maintenance and usage counters.
- Closure path: approved skills can affect later agent capabilities, but the required outside/future distinction and prospective strategic alternatives/feedback are not evidenced.
- Why this is / is not agent-owned: self-learning and durable skill changes are not sufficient for outside-and-then S4; human approval is not automatically S4 parent authority.
- Evidence: [`skill.md`](https://github.com/agentscope-ai/agentscope-java/blob/3d1b998d7c1c0aa6d9697a85b59c205a4c7c2a0f/docs/v2/en/docs/harness/skill.md), [`SkillCuratorMiddleware.java`](https://github.com/agentscope-ai/agentscope-java/blob/3d1b998d7c1c0aa6d9697a85b59c205a4c7c2a0f/agentscope-harness/src/main/java/io/agentscope/harness/agent/middleware/SkillCuratorMiddleware.java).
- Basis: structural.
- Confidence: medium.
- Caveats: caller-specific future intelligence built via middleware is outside the library's default function.

### Absence scope

- Surfaces inspected: documented optional skill learning/review, long-term memory, curator and team workflow, builder settings.
- Plausible first-party paths checked: skill proposals, approval filters/canaries, periodic maintenance, persistent memory and dynamic team task creation.
- Why no material first-party path remains: the source supplies operational improvement and catalog hygiene, not a loop from external future change through developed adaptation options and strategic selection to current capability.

## S5 — Policy and identity

- State: —
- Function: no installed ultimate-policy/identity deliberation-and-return for the assessed agent/team.
- Disturbance / variety regulated: permissions, team role scope, plan-mode approval and workspace policies limit current work but do not arbitrate mission or ultimate values.
- Decisive decision or feedback right: developer/operator sets tool permissions and team roles; the model receives role clipping and task/plan verdicts, not authority over identity-level policy.
- Decision owner: user/configuration and application administrators outside a first-party constitutional return path.
- Supporting / enforcement mechanisms: permission middleware, `TeamTool` roles, plan approval, skill promotion gates.
- Closure path: tool consent or plan verdict affects task execution, but there is no first-party identity question → legitimate authority → policy ratification → subsequent operation circuit.
- Why this is / is not agent-owned: an agent's role or prompt cannot itself prove ultimate-policy authority; human task approvals do not become S5 parent governance.
- Evidence: [`TeamTool.java`](https://github.com/agentscope-ai/agentscope-java/blob/3d1b998d7c1c0aa6d9697a85b59c205a4c7c2a0f/agentscope-harness/src/main/java/io/agentscope/harness/agent/tool/TeamTool.java), [`permission-system.md`](https://github.com/agentscope-ai/agentscope-java/blob/3d1b998d7c1c0aa6d9697a85b59c205a4c7c2a0f/docs/v2/en/docs/building-blocks/permission-system.md), [`skill.md`](https://github.com/agentscope-ai/agentscope-java/blob/3d1b998d7c1c0aa6d9697a85b59c205a4c7c2a0f/docs/v2/en/docs/harness/skill.md).
- Basis: structural.
- Confidence: medium.
- Caveats: a higher-level installed application may build governance; not credited to this standard Java harness.

### Absence scope

- Surfaces inspected: team roles/tools, permission system, plan mode, skill promotion, service/host documentation and builder integration.
- Plausible first-party paths checked: local permission confirmation, team lead role, worker plan approval, skill promotion and operator config changes.
- Why no material first-party path remains: reviewed controls affect tool/task/capability permissions, but none establishes the ultimate-policy dispute, legitimate adjudicator and return that governs identity across later operations.

## Distributed OSS parent arrangement

Contributors develop the library, while independent self-hosted adopters configure team runs. The repository's contributor and release workflows are not a legitimate parent metasystem wired into an individual runtime's S3/S4/S5 functions. No organization-level parent modifier is claimed.

## Self-hosted and non-human modes

Configured local/shared/sandbox runners can act with model-backed team lead and worker roles; team mode is opt-in, not inherent in a bare ReActAgent. Human operator prompts and promotion gates remain separate from the model-owned S2/S3 team decisions claimed here. External hosting does not automatically change their ownership to first-party parent modes.

## Recursion

Team members and delegated child agents are operational cells under one team recursion; their nested process/session topology does not independently establish fully viable S3/S4/S5 at each child level.

## Variety and escalation

CAS ownership, `blockedBy` dependencies, wakeups and lead arbitration attenuate task contention. Whole-board digest and completion notifications let the model lead regulate current commitments. Sandbox/permission errors are operational signals; an independent audit channel or algedonic identity escalation is not established by event delivery alone.

## Evidence gaps

- Code/documentation-only structural assessment: no live provider/team simulation, quality benchmark or external service deployment was run.
- S2 and S3 positive states are conditional on the shipped builder-configured team mode and active model lead; ordinary standalone ReActAgent does not inherit them.
- Review of the separately hosted AgentScope Service control plane did not establish additional positive ownership for the declared reusable library/system-in-focus; independent service assessment would need a different boundary.

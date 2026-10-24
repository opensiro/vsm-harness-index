---
harness_id: blade-code
project_name: Blade Code
repository: https://github.com/echoVic/blade-code
review_ref: 30f868411df4f7da095aadb7a2a8ca3310315613
reviewed_at: 2026-10-06
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-06
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Blade Code

## Review boundary

- System in focus: the first-party Blade Code runtime at frozen revision 30f868411df4f7da095aadb7a2a8ca3310315613, including its coding-agent loop, built-in tools, first-party subagents and Agent Teams, shared task graph, managed worktrees, independent verification gate, sessions/context, permissions, goal execution, auto-memory, CLI/Web/Headless/ACP surfaces and provider/MCP adapters.
- Purpose and identity: perform software-engineering and automation work through a model-backed coding agent that can work directly, delegate to bounded agents, create durable multi-agent teams, coordinate dependent workstreams and require independent verification before accepting non-trivial implementation work.
- Relevant environment: user goals and steering, repository/workspace state, tool/test/browser/desktop evidence, teammate state/messages, shared task graph state, worktree changes, provider/model responses, persisted sessions/memory and external MCP services.
- Standard-distribution boundary: shipped Blade Code runtime and repository-owned tools/team/subagent/control code. External model providers, MCP servers, browser/OS services and the user repository are dependencies and cannot donate organizational functions.
- Credited operating / distribution surfaces: packages/cli/src/agent, agent/subagents, agent/teams, tools/builtin/task, tools/builtin/team, tools/builtin/worktree, tools/execution, goals, context, memory, services and supported CLI/Web/Headless/ACP runtime paths.
- Adjacent first-party surfaces excluded from ownership: repository CI, docs/plans, bundled third-party-style prompt collections and development evidence except where they corroborate an executable runtime path.
- First-party operating / deployment modes considered: ordinary coding turns; background/foreground Task subagents; Agent Teams with durable task graphs and peer messaging; managed worktree isolation for write-capable teammates; goal execution; mandatory independent verification on qualifying modifications; supported persistent sessions/memory and provider configurations.
- Recursion level: one Blade Code coding organization. The lead coding agent and first-party task/team workers that own bounded implementation outcomes are S1 units at this level.
- Reviewed revision: 30f868411df4f7da095aadb7a2a8ca3310315613.
- Observation date: 2026-10-06.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

Blade Code's main Agent owns the model/tool coding loop. First-party Task delegation can create bounded foreground or background subagent sessions; write-capable subagents can use managed worktree isolation. Agent Teams add a durable team runtime with persistent member sessions, role-specific contexts, a shared dependency graph, atomic task claiming, automatic unblocking, durable direct/broadcast messages and managed worktrees for write-capable members.

The TeamCreate tool is model-callable by the lead agent and accepts role-specific members plus a task DAG with dependency and assignment decisions. TeamStatus returns live member and graph state. SendMessage can deliver a durable steering message into a running teammate turn. TeamDelete can terminate the running team. The lead therefore has both a whole-current view and substantive current-control actions over active commitments.

Blade Code also contains a first-party independent verification gate. After sufficiently broad or high-risk modifications, the main loop requires a fresh built-in verification subagent with read-only tools and an authoritative scope. The verifier must gather direct tool-backed repository/test evidence and emit PASS/FAIL/PARTIAL; only a fresh PASS for the current mutation revision allows completion.

Auto-memory persists selected project facts, conventions, lessons and debugging notes and injects them into later sessions. This is useful learning/persistence, but the reviewed runtime does not establish a distinct outside-and-then option-development function that models future external conditions and returns adaptation options into S3.

## S1 — Operations

- State: A
- Function: autonomously perform software-engineering and automation work through model-selected repository/tool actions.
- Disturbance / variety regulated: unfamiliar code, implementation choices, tool/test/browser failures, model/provider variation, context pressure and bounded delegated work.
- Decisive decision or feedback right: choose substantive coding/tool actions, interpret returned evidence, decide when to delegate or create a team and decide when the assigned operational objective is complete.
- Decision owner: the active model-backed Blade Code agent and, for delegated bounded work, first-party subagent/team-member agents.
- Supporting / enforcement mechanisms: tool registry/executor, permissions, context/session runtime, provider adapters, task admission, goal state, worktrees and cancellation.
- Closure path: user/parent goal → agent chooses direct or delegated coding action → first-party runtime executes → tool/subagent/team evidence returns → agent revises work → completion is accepted when runtime completion gates permit it.
- Boundary reachability: ordinary CLI/Web/Headless/ACP runtime uses the same first-party Agent/tool machinery; Task and Team tools are shipped model-callable surfaces.
- Why this is / is not agent-owned: deterministic code executes and constrains actions, but the model chooses open-ended implementation, investigation, delegation and completion decisions.
- Evidence: [packages/cli/src/agent/Agent.ts](https://github.com/echoVic/blade-code/blob/30f868411df4f7da095aadb7a2a8ca3310315613/packages/cli/src/agent/Agent.ts); [packages/cli/src/tools/builtin/task/task.ts](https://github.com/echoVic/blade-code/blob/30f868411df4f7da095aadb7a2a8ca3310315613/packages/cli/src/tools/builtin/task/task.ts); [README.md](https://github.com/echoVic/blade-code/blob/30f868411df4f7da095aadb7a2a8ca3310315613/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: permissions and scheduling can delay/block actions without becoming the owner of the engineering decision itself.

## S2 — Coordination

- State: A
- Function: attenuate interference among concurrent operational teammates by assigning dependencies/ownership and isolating write-capable workstreams while coordinating peer progress.
- Disturbance / variety regulated: duplicate task claiming, dependency-order violations, concurrent workers editing overlapping workspace state, and peer work that must be synchronized before downstream tasks proceed.
- Decisive decision or feedback right: choose the team members, task partition, dependency graph, initial assignments and whether work benefits from parallel specialization/peer review; use peer messages to adjust coordination as execution unfolds.
- Decision owner: the model-backed team lead through TeamCreate/SendMessage, with deterministic task-graph/worktree mechanisms enforcing the selected relation.
- Supporting / enforcement mechanisms: TeamTaskGraph, atomic claim, automatic unblock, durable peer mailbox, managed worktree isolation for write-capable members and worktree lifecycle/merge machinery.
- Closure path: lead identifies separable/interdependent work → creates roles/tasks/dependencies → teammates claim only unblocked work and write-capable members default to isolated worktrees → completion/unblocking/messages update peer execution → downstream units proceed under the adjusted coordination state.
- Boundary reachability: TeamCreate, TeamTaskClaim, SendMessage and managed teammate worktrees are shipped first-party runtime tools, not documentation-only concepts.
- Why this is / is not agent-owned: the runtime enforces claims, dependencies and isolation, but the lead agent chooses the substantive organizational partition and dependency structure.
- Distinct S1 units: persistent model-backed teammates/subagents that own bounded implementation or review outcomes.
- Inter-S1 disturbance: concurrent workers can duplicate work, violate ordering, or collide through shared writes; managed worktrees and dependency/claim rules exist specifically to reduce those interactions.
- Attenuating coordination relation: lead-selected DAG/assignment plus atomic task claiming, automatic dependency unblocking, durable peer messaging and worktree isolation for writers.
- Feedback into subsequent S1 behaviour: completed tasks unblock dependent work; peer messages enter running teammate turns; task ownership/claim state changes which unit may work next; isolated results are later integrated rather than concurrently overwriting the same checkout.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the mechanisms regulate concrete interaction among simultaneously viable operational workers rather than merely transporting a delegated prompt.
- Evidence: [packages/cli/src/tools/builtin/team/teamTools.ts](https://github.com/echoVic/blade-code/blob/30f868411df4f7da095aadb7a2a8ca3310315613/packages/cli/src/tools/builtin/team/teamTools.ts); [packages/cli/src/agent/teams/TeamTaskGraph.ts](https://github.com/echoVic/blade-code/blob/30f868411df4f7da095aadb7a2a8ca3310315613/packages/cli/src/agent/teams/TeamTaskGraph.ts); [packages/cli/src/agent/subagents/SubagentWorktreeLifecycle.ts](https://github.com/echoVic/blade-code/blob/30f868411df4f7da095aadb7a2a8ca3310315613/packages/cli/src/agent/subagents/SubagentWorktreeLifecycle.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: atomic claiming and worktree mechanics are deterministic support; autonomy is credited to the lead's model-owned organizational decisions.

## S3 — Inside-and-now control

- State: A
- Function: maintain a live whole-team view and regulate current operational commitments while the multi-agent organization is running.
- Disturbance / variety regulated: stalled or unwanted teammates, changed current priorities, task/member status changes, blocked downstream work and a team that should be stopped after synthesis or failure.
- Decisive decision or feedback right: inspect the live team/member/task graph, steer a running teammate with a direct message, broadcast a changed instruction, and terminate running teammates by deleting the current team.
- Decision owner: the model-backed team lead through TeamStatus, SendMessage and TeamDelete.
- Supporting / enforcement mechanisms: AgentSessionStore-backed live member state, durable task graph, TeamMailbox, running-turn message delivery and team/member cancellation.
- Closure path: lead inspects TeamStatus/current graph → detects a current execution need → sends targeted/broadcast steering or terminates the team → running teammate/session state changes → later TeamStatus/results reflect the intervention and the lead proceeds accordingly.
- Boundary reachability: TeamStatus/SendMessage/TeamDelete are shipped model-callable first-party tools available to the team lead.
- Why this is / is not agent-owned: live state storage and cancellation transport are deterministic, but the lead model interprets whole-current state and decides the substantive intervention.
- Whole-system current view: TeamStatus returns live member state from AgentSessionStore together with durable task-graph state for the owned team.
- Current-control decision scope: current peer steering, task/role supervision through the shared graph, and cancellation of running team commitments when work should stop.
- Evidence: [packages/cli/src/tools/builtin/team/teamTools.ts](https://github.com/echoVic/blade-code/blob/30f868411df4f7da095aadb7a2a8ca3310315613/packages/cli/src/tools/builtin/team/teamTools.ts); [packages/cli/src/agent/teams/TeamRuntime.ts](https://github.com/echoVic/blade-code/blob/30f868411df4f7da095aadb7a2a8ca3310315613/packages/cli/src/agent/teams/TeamRuntime.ts); [packages/cli/src/agent/teams/TeamMailbox.ts](https://github.com/echoVic/blade-code/blob/30f868411df4f7da095aadb7a2a8ca3310315613/packages/cli/src/agent/teams/TeamMailbox.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: generic stop/cancel would not be enough alone; the positive claim rests on the combined live whole-team status surface plus targeted running-turn steering and commitment termination.

## S3* — Complementary audit

- State: A
- Function: independently challenge qualifying implementation work with a fresh read-only verifier whose evidence can block completion.
- Disturbance / variety regulated: incorrect implementation claims, failing tests/types/lint, medium/high-risk defects, race/security issues and author self-verification bias.
- Decisive decision or feedback right: independently execute allowed verification commands, inspect the authoritative changed-file scope and emit structured PASS/FAIL/PARTIAL findings.
- Decision owner: the separately instantiated built-in verification agent.
- Supporting / enforcement mechanisms: fresh subagent context, read-only tool restrictions, authoritative verification prompt, mutation-revision tracking, bounded retry gate and deterministic completion policy.
- Closure path: main agent changes qualifying implementation → runtime requires fresh verification Task → independent verifier gathers direct project/tool evidence and emits verdict → FAIL/PARTIAL forces repair/re-verification; only fresh PASS for current mutation revision permits completion.
- Boundary reachability: independentVerification is wired into the shipped main loop and explicitly requires the built-in verification subagent for qualifying changes.
- Why this is / is not agent-owned: the verifier model owns the audit judgment from its own evidence path; deterministic runtime code enforces freshness and blocks completion when the verdict is insufficient.
- Claim being audited: the main coding agent's claim that the current non-trivial implementation is correct and ready to finish.
- Ordinary reporting path: the author agent's normal tool results, implementation narrative and self-checks.
- Complementary access path: a separate read-only verifier runs project checks and reads changed files directly under an authoritative scope.
- Independence boundary: fresh model-backed subagent, no write tools, no nested subagents, tool-evidence-only instructions and no reliance on the author's claimed test outcome.
- Who acts on findings: the main agent must repair reported failures and invoke a new verification run; the runtime completion gate prevents success until the required PASS is fresh.
- Evidence: [packages/cli/src/agent/loop/independentVerification.ts](https://github.com/echoVic/blade-code/blob/30f868411df4f7da095aadb7a2a8ca3310315613/packages/cli/src/agent/loop/independentVerification.ts); [packages/cli/src/agent/subagents/verification.md](https://github.com/echoVic/blade-code/blob/30f868411df4f7da095aadb7a2a8ca3310315613/packages/cli/src/agent/subagents/verification.md); [packages/cli/src/agent/subagents/builtinVerificationAgent.ts](https://github.com/echoVic/blade-code/blob/30f868411df4f7da095aadb7a2a8ca3310315613/packages/cli/src/agent/subagents/builtinVerificationAgent.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: generic code-review skills are not used for this claim; the positive S3* path is the enforced built-in verifier.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party external-and-prospective adaptation loop is established.
- Disturbance / variety regulated: no qualifying future/external condition is placed under a function that develops adaptation options and returns them into current S3 capability.
- Decisive decision or feedback right: none established for S4.
- Decision owner: none established.
- Supporting / enforcement mechanisms: auto-memory, compaction-time consolidation, provider health/recovery, web/browser tools, goals, schedules and plugin/skill configuration can affect later work but do not by themselves close S4.
- Closure path: not applicable.
- Boundary reachability: no positive S4 path claimed.
- Why this is / is not agent-owned: memory consolidation extracts preferences/conventions/lessons/debugging notes and injects retained project knowledge into later sessions; that is persistence/learning context rather than an evidenced outside-and-then option-development conversation with current S3.
- Evidence: [packages/cli/src/memory/AutoMemoryManager.ts](https://github.com/echoVic/blade-code/blob/30f868411df4f7da095aadb7a2a8ca3310315613/packages/cli/src/memory/AutoMemoryManager.ts); [packages/cli/src/memory/MemoryConsolidation.ts](https://github.com/echoVic/blade-code/blob/30f868411df4f7da095aadb7a2a8ca3310315613/packages/cli/src/memory/MemoryConsolidation.ts); [packages/cli/src/goals/executionFrontier.ts](https://github.com/echoVic/blade-code/blob/30f868411df4f7da095aadb7a2a8ca3310315613/packages/cli/src/goals/executionFrontier.ts).
- Basis: structural absence review.
- Confidence: high.
- Caveats: the runtime has substantial persistence and external tooling, but these do not satisfy the Methodology 0.3.6 external-and-prospective option loop without an adaptation owner.

### Absence scope

- Surfaces inspected: auto-memory write/load/consolidation, goal execution, scheduling, provider recovery, web/browser tools, plugins/skills, session recap/compaction and team/subagent mechanisms.
- Plausible first-party paths checked: future environment scan, autonomous strategy/capability reconfiguration, learned policy update, option generation from external change and explicit S4→S3 return.
- Why no material first-party path remains: observed mechanisms preserve/reuse context, execute scheduled/current work or react to current failures rather than create prospective organizational options from outside/future distinctions.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy governance loop is established.
- Disturbance / variety regulated: no identity-level or ultimate-policy conflict is routed to a distinct authoritative S5 owner.
- Decisive decision or feedback right: none established for S5.
- Decision owner: none established.
- Supporting / enforcement mechanisms: permission modes, workspace trust, system prompts, tool policy, plugin/MCP security and configuration constrain execution but do not create identity-governance closure.
- Closure path: not applicable.
- Boundary reachability: no positive S5 path claimed.
- Why this is / is not agent-owned: Blade Code agents operate within developer/user-authored constraints and do not have authority to redefine the system's ultimate identity or governing principles.
- Evidence: [packages/cli/src/config/PermissionChecker.ts](https://github.com/echoVic/blade-code/blob/30f868411df4f7da095aadb7a2a8ca3310315613/packages/cli/src/config/PermissionChecker.ts); [packages/cli/src/security/WorkspaceTrustService.ts](https://github.com/echoVic/blade-code/blob/30f868411df4f7da095aadb7a2a8ca3310315613/packages/cli/src/security/WorkspaceTrustService.ts); [packages/cli/src/prompts/sections.ts](https://github.com/echoVic/blade-code/blob/30f868411df4f7da095aadb7a2a8ca3310315613/packages/cli/src/prompts/sections.ts).
- Basis: structural absence review.
- Confidence: high.
- Caveats: operator permissions and configuration are legitimate constraints, not identity/ultimate-policy governance.

### Absence scope

- Surfaces inspected: permission modes, workspace trust, system prompts, tool policy, plugin/MCP security, model/provider settings, team lifecycle and durable memory.
- Plausible first-party paths checked: autonomous constitutional revision, parent identity authority, agent-written runtime policy and authoritative S3/S4 policy arbitration.
- Why no material first-party path remains: all located policy mechanisms constrain ordinary execution or configure capabilities; none closes an identity-level governance loop.

## Distributed OSS parent arrangement

The assessed organization is the running Blade Code coding organization, not the GitHub maintainer project. Repository governance, CI and release workflows are not imported as runtime S3/S4/S5 owners.

## Self-hosted and non-human modes

Blade Code supports local/cloud providers and CLI/Web/Headless/ACP operation. S1/S2/S3/S3* claims rely on first-party model/runtime paths and do not require a human controller.

## Recursion

At the declared boundary the lead agent and active implementation/review teammates are operational S1 units. The lead owns S2 coordination and S3 current control over Agent Teams. The built-in verification subagent is a complementary S3* actor rather than a peer implementation owner for the claim it audits.

## Variety and escalation

Ordinary coding variety remains in S1. Cross-worker dependencies/write interference are attenuated by team task graphs and managed worktrees under S2. Live teammate/task changes are regulated by the lead under S3. Qualifying implementation claims escalate to a fresh independent verifier under S3*. Memory, provider recovery and configuration do not create S4/S5.

## Evidence gaps

No ? state is required. The frozen runtime exposes the relevant team, task, worktree, live-status/steering and independent-verification paths directly; the inspected memory/policy surfaces are sufficient for the bounded negative S4/S5 conclusions.

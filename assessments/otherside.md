---
harness_id: otherside
project_name: Otherside
repository: https://github.com/daanielcruz/otherside-cli
review_ref: 202aa86c9d182c63f8ba9c0facf2718618de02eb
reviewed_at: 2026-10-06
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-06
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Otherside

## Review boundary

- System in focus: the first-party Otherside coding runtime at frozen revision 202aa86c9d182c63f8ba9c0facf2718618de02eb, including its main model/tool loop, Agent/Task control tools, background and nested subagents, optional git-worktree isolation, deterministic workflows, goal/session/checkpoint state, first-party Verifier agent, provider routing, MCP/plugin/skill integration and interactive/print execution surfaces.
- Purpose and identity: complete software-engineering goals through one coordinating coding agent that can directly edit/test, decompose work into autonomous subagents, run independent work in parallel, supervise current delegated commitments, independently verify non-trivial implementation, and persist/resume sessions.
- Relevant environment: user goals and approvals, repository/worktree contents, tool/process/test results, provider/model availability and quotas, active task/agent state, background completion/failure, MCP/plugin services, persisted sessions/checkpoints and project memory.
- Standard-distribution boundary: shipped Otherside binary/runtime plus repository-owned harness prompts, tools, agent definitions, task/background/workflow/worktree/session machinery and provider adapters. External model endpoints, MCP servers, plugins/skills supplied from outside, mobile/backend services and the user's project remain environment/dependencies and cannot donate organizational ownership.
- Credited operating / distribution surfaces: src/engine queue/background/subagents/workflows/session/providers, src/harness/tools, src/harness/agents, supported TUI/print execution, /goal, /parallel, /fork, /workflows, /tasks, /rewind and related first-party controls.
- Adjacent first-party surfaces excluded from ownership: repository CI/release infrastructure, development tests as ownership by themselves, hosted website/mobile product governance, and externally supplied plugins/MCP servers.
- First-party operating / deployment modes considered: ordinary interactive and one-shot coding; foreground/background/nested agents; concurrent agents; optional worktree isolation; deterministic workflows; goal-driven execution; fresh Verifier agent; multiprovider routing; persistent/resumable sessions.
- Recursion level: one Otherside coding organization for a user objective. The main coding/coordinating model and spawned coding subagents are S1 units when each owns a bounded engineering outcome; the parent model can organize and control that set.
- Reviewed revision: 202aa86c9d182c63f8ba9c0facf2718618de02eb.
- Observation date: 2026-10-06.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

Otherside ships a first-party coding-agent harness with native repository/shell/search/edit tools, multiple provider adapters and session persistence. The Agent tool launches fresh or forked autonomous agents, supports foreground/background execution and explicitly supports launching multiple independent agents concurrently. Write-capable work can optionally be isolated into a dedicated git worktree whose lifecycle, baseline, branch, lease and fail-closed cleanup are managed by first-party runtime code.

The parent runtime also exposes a structured task registry. TaskList returns the whole current task set with status, owner and dependency state. TaskUpdate can change task owner/status/details and add blocks/blockedBy relationships. SendMessage can steer a live agent or resume a completed durable agent with preserved context, while TaskStop aborts a specific running background agent/task. These surfaces provide more than passive status: they allow the coordinating model to alter current commitments and dependency/ownership structure based on live outcomes.

Otherside additionally ships a specialized Verifier agent. It is intended for non-trivial implementation before completion, is read/execute oriented, receives the original task plus changed files/approach, independently scans the parent's claims/tool outputs, directly runs build/tests/linters and adversarial probes, and returns a parsed PASS/FAIL/PARTIAL verdict with evidence. The parent receives that separate agent result and can repair, re-run or withhold completion.

## Operational model

The main model-backed coding agent owns open-ended engineering choices and may delegate bounded S1 work. For independent parallel write work, the same model can choose separate worktree isolation; first-party runtime creates a separate branch/worktree, copies the relevant dirty overlay, holds a run-lifetime lease and refuses unsafe cleanup when the isolated tree has diverged or is still live.

Current organization is observable through the task/background registries and completion notifications. The parent model can modify ownership/dependencies, steer one live child with SendMessage, resume durable workers and stop a selected task. Therefore S2 and S3 are not inferred merely from the presence of subagents: they are tied to explicit decision rights plus first-party enforcement and return paths.

Provider/quota routing, durable sessions, /dream memory, rewind/checkpoints, goal persistence and compaction improve continuity and current execution. They do not by themselves establish a separate outside-and-then adaptation owner or an identity/ultimate-policy governor.

## S1 — Operations

- State: A
- Function: autonomously perform software-engineering work through model-selected investigation, edit, shell, test, web/MCP and delegated coding actions.
- Disturbance / variety regulated: unfamiliar code, implementation choices, test/build/runtime failures, provider/model variability, context pressure, user constraints, tool errors and bounded delegated work.
- Decisive decision or feedback right: choose substantive engineering actions, interpret evidence, decide repairs, choose when/how to delegate and decide when the assigned operational objective is complete.
- Decision owner: the active model-backed main Otherside agent and spawned model-backed coding subagents for their bounded tasks.
- Supporting / enforcement mechanisms: native coding tools, permission modes, provider adapters, session/context handling, background tasks, Agent tool, workflows, MCP/plugins/skills and optional worktree isolation.
- Closure path: user/parent goal → coding agent chooses direct tools or delegated work → first-party runtime executes → tool/subagent evidence returns → agent revises/validates work until completion or an explicit boundary stops it.
- Boundary reachability: the shipped interactive and print modes instantiate the same first-party harness; Agent/workflow tools are normal supported runtime surfaces.
- Why this is / is not agent-owned: deterministic code constrains execution, but the model decides the open-ended implementation/investigation actions and interprets the results.
- Evidence: [README.md](https://github.com/daanielcruz/otherside-cli/blob/202aa86c9d182c63f8ba9c0facf2718618de02eb/README.md); [src/harness/tools/Agent/tool.json](https://github.com/daanielcruz/otherside-cli/blob/202aa86c9d182c63f8ba9c0facf2718618de02eb/src/harness/tools/Agent/tool.json); [src/engine/background/subagents/fork/loop.ts](https://github.com/daanielcruz/otherside-cli/blob/202aa86c9d182c63f8ba9c0facf2718618de02eb/src/engine/background/subagents/fork/loop.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: provider/model selection can be automatic or user-constrained, but provider choice is support for the operational loop rather than ownership of the engineering decision.

## S2 — Coordination

- State: A
- Function: attenuate interference among distinct concurrent coding S1 units by choosing dependency/ownership relations and isolated workspaces when parallel write work could collide.
- Disturbance / variety regulated: duplicate/overlapping delegated work, dependency-order violations, concurrent writes against one checkout, stale/unsafe isolated worktree cleanup and integration ambiguity.
- Decisive decision or feedback right: decide which workstreams may run concurrently, assign task owners/dependencies, avoid duplicate overlapping agents and choose worktree isolation for write-capable subagents whose edits must be separated.
- Decision owner: the model-backed parent/coordinating agent using Agent, TaskList/TaskUpdate and related first-party tools.
- Supporting / enforcement mechanisms: task blockedBy/blocks/owner state; foreground/background Agent dispatch; git worktree creation on per-agent branches; worktree locks, baselines and run-lifetime leases; fail-closed cleanup; returned branch/path/result for parent integration.
- Closure path: parent decomposes current goal → observes/creates task dependencies and ownership → launches independent S1 units, selecting worktree isolation where needed → isolated agents execute → completion/diff/result state returns to the parent → parent adjusts dependencies/integration or follow-up work.
- Boundary reachability: Agent exposes parallel dispatch plus \`isolation: "worktree"\`; TaskCreate/TaskUpdate/List are shipped harness tools; worktree creation/lease/removal are wired first-party runtime modules.
- Why this is / is not agent-owned: git/worktree/task-store code enforces isolation and dependency state, but the parent model owns the discretionary decision about partition, ownership, parallelism, dependencies and whether isolation is appropriate.
- Distinct S1 units: the main coding agent plus one or more autonomous fresh/fork coding agents, including concurrent background agents.
- Inter-S1 disturbance: concurrently write-capable agents can duplicate effort, violate dependency order or edit overlapping repository state; an isolated worker may also leave valuable changes that unsafe cleanup must not erase.
- Attenuating coordination relation: parent-selected task dependencies/owners plus optional separate git worktrees and first-party worktree lease/baseline guards prevent direct workspace collision and preserve changed isolated work for later parent integration.
- Feedback into subsequent S1 behaviour: blockedBy prevents premature task selection; completion and task status expose newly available work; background results/worktree branches return to the parent, which can integrate, redirect or create follow-up tasks rather than letting peers overwrite each other.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the positive claim is not "there are agents"; it is the explicit peer-work interference relation and model-selected dependency/isolation structure that changes whether and where those S1 units may operate.
- Evidence: [src/harness/tools/Agent/tool.json](https://github.com/daanielcruz/otherside-cli/blob/202aa86c9d182c63f8ba9c0facf2718618de02eb/src/harness/tools/Agent/tool.json); [src/harness/tools/TaskList/tool.json](https://github.com/daanielcruz/otherside-cli/blob/202aa86c9d182c63f8ba9c0facf2718618de02eb/src/harness/tools/TaskList/tool.json); [src/harness/tools/TaskUpdate/tool.json](https://github.com/daanielcruz/otherside-cli/blob/202aa86c9d182c63f8ba9c0facf2718618de02eb/src/harness/tools/TaskUpdate/tool.json); [src/engine/background/subagents/worktree-creation.ts](https://github.com/daanielcruz/otherside-cli/blob/202aa86c9d182c63f8ba9c0facf2718618de02eb/src/engine/background/subagents/worktree-creation.ts); [src/engine/background/subagents/worktree-lease.ts](https://github.com/daanielcruz/otherside-cli/blob/202aa86c9d182c63f8ba9c0facf2718618de02eb/src/engine/background/subagents/worktree-lease.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: not every Agent dispatch uses a worktree. The claim is limited to the shipped parent-owned coordination mode where concurrent operational work is explicitly structured and isolation is selected when needed.

## S3 — Inside-and-now control

- State: A
- Function: provide whole-organization current control over active tasks/agents by observing commitments and changing ownership, dependency, direction or continuation while the run is in progress.
- Disturbance / variety regulated: blocked or failed work, changed requirements, misdirected live agents, duplicated ownership, tasks that should stop, newly unblocked work and durable agents that should resume with new direction.
- Decisive decision or feedback right: inspect all current tasks, reassign owner/status/dependencies, steer a selected live agent, resume it with preserved context/routing when appropriate, or stop a specific active background agent/task.
- Decision owner: the model-backed parent/coordinating Otherside agent; a human may also intervene through TUI task/agent controls, but human control is not needed for the A claim.
- Supporting / enforcement mechanisms: TaskList/TaskGet/TaskUpdate, SendMessage, TaskStop, background task registry/controllers, live steer queues, durable fork lifecycle/resume state and completion notifications.
- Closure path: parent observes whole current task/agent state → decides a current-control intervention → first-party tool changes owner/dependencies/status, queues a steer/resume or aborts the selected task → runtime applies that intervention → updated task/agent outcomes return into subsequent parent decisions.
- Boundary reachability: Task tools and SendMessage/TaskStop are shipped harness capabilities available to the coding organization; live fork lifecycle explicitly consumes queued steers and exposes task state.
- Why this is / is not agent-owned: registries/controllers provide state and enforcement, but the parent model makes the substantive judgment about which commitment to redirect, reassign, block, resume or terminate.
- Whole-system current view: TaskList exposes the current task set with status, owner and blockedBy; background task/agent notifications and IDs expose running delegated commitments to the parent.
- Current-control decision scope: task ownership and dependency changes, status transitions, selected live-agent steering, durable resume, route switch on resume subject to policy, and targeted TaskStop cancellation.
- Evidence: [src/harness/tools/TaskList/tool.json](https://github.com/daanielcruz/otherside-cli/blob/202aa86c9d182c63f8ba9c0facf2718618de02eb/src/harness/tools/TaskList/tool.json); [src/harness/tools/TaskUpdate/tool.json](https://github.com/daanielcruz/otherside-cli/blob/202aa86c9d182c63f8ba9c0facf2718618de02eb/src/harness/tools/TaskUpdate/tool.json); [src/harness/tools/SendMessage/tool.json](https://github.com/daanielcruz/otherside-cli/blob/202aa86c9d182c63f8ba9c0facf2718618de02eb/src/harness/tools/SendMessage/tool.json); [src/harness/tools/TaskStop/tool.json](https://github.com/daanielcruz/otherside-cli/blob/202aa86c9d182c63f8ba9c0facf2718618de02eb/src/harness/tools/TaskStop/tool.json); [src/engine/background/subagents/fork/steering.ts](https://github.com/daanielcruz/otherside-cli/blob/202aa86c9d182c63f8ba9c0facf2718618de02eb/src/engine/background/subagents/fork/steering.ts); [src/engine/background/subagents/lifecycle.ts](https://github.com/daanielcruz/otherside-cli/blob/202aa86c9d182c63f8ba9c0facf2718618de02eb/src/engine/background/subagents/lifecycle.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: generic Ctrl+C or emergency cancellation alone would not justify S3. The claim rests on the task-wide current view plus selective model-owned ownership/dependency/steer/resume/stop rights.

## S3* — Complementary audit

- State: A
- Function: independently challenge non-trivial implementation work with a fresh verification specialist that directly executes checks and returns a terminal evidence-based verdict.
- Disturbance / variety regulated: false completion claims, circular/mocked tests, build/type/lint failures, regressions and adversarial edge cases missed by the authoring agent.
- Decisive decision or feedback right: independently inspect actual repository changes, run build/tests/linters/direct runtime probes and issue VERDICT: PASS, FAIL or PARTIAL under explicit evidence rules.
- Decision owner: the separate model-backed Verifier agent.
- Supporting / enforcement mechanisms: dedicated first-party agent definition, fresh Agent invocation, read/execute-oriented toolset, explicit no-project-mutation rule, required command/output evidence and adversarial probes.
- Closure path: parent performs non-trivial implementation → launches Verifier with original task, changed files and approach → Verifier independently reads/runs repository evidence and returns PASS/FAIL/PARTIAL → parent receives findings and can repair/re-run or withhold final completion.
- Boundary reachability: Verifier is a bundled agent definition and Agent tool documentation explicitly presents independent verifier/code-reviewer use; its definition says to invoke after non-trivial implementation before reporting completion.
- Why this is / is not agent-owned: the reviewer model itself interprets direct evidence and decides the audit verdict; deterministic tool restrictions and verdict format only enforce the audit boundary.
- Claim being audited: the implementation/author-agent claim that the current change satisfies the original user task and is ready to report complete.
- Ordinary reporting path: the authoring agent's own tool results, summary and tests run during implementation.
- Complementary access path: the Verifier starts as a separate agent, scans the parent's current-turn claims but independently reads the repository and runs build/tests/linters/runtime/adversarial probes using its own tools.
- Independence boundary: fresh specialized model context, no write authority over the project, direct evidence acquisition and an explicit adversarial mandate not to trust the author's self-report.
- Who acts on findings: the parent coding agent receives the verifier result and decides repair/reverification or whether final completion can be reported.
- Evidence: [src/harness/agents/verifier/AGENT.md](https://github.com/daanielcruz/otherside-cli/blob/202aa86c9d182c63f8ba9c0facf2718618de02eb/src/harness/agents/verifier/AGENT.md); [src/harness/tools/Agent/tool.json](https://github.com/daanielcruz/otherside-cli/blob/202aa86c9d182c63f8ba9c0facf2718618de02eb/src/harness/tools/Agent/tool.json).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: generic "trust but verify" text would not be enough by itself; the claim is anchored in the distinct bundled Verifier actor with direct evidence tools and a parsed terminal verdict.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party external-and-prospective adaptation loop is established.
- Disturbance / variety regulated: no qualifying external/future condition is owned by a function that develops adaptation options and returns them into present organizational capability.
- Decisive decision or feedback right: none established for S4.
- Decision owner: none established.
- Supporting / enforcement mechanisms: /dream project memory, session persistence/rewind, goal persistence across compaction, provider/quota/cooldown routing, web/MCP access, plugin/skill loading and durable subagent resume can affect later work but do not by themselves close S4.
- Closure path: not applicable.
- Boundary reachability: no positive S4 path claimed.
- Why this is / is not agent-owned: provider fallback reacts to current availability; memory/checkpoints preserve state; web/MCP gather current evidence. None establishes a separate outside-and-then option-development owner that feeds prospective adaptations into S3/current capability.
- Evidence: [README.md](https://github.com/daanielcruz/otherside-cli/blob/202aa86c9d182c63f8ba9c0facf2718618de02eb/README.md); [src/commands/handlers/goal.ts](https://github.com/daanielcruz/otherside-cli/blob/202aa86c9d182c63f8ba9c0facf2718618de02eb/src/commands/handlers/goal.ts); [src/engine/providers/registry.ts](https://github.com/daanielcruz/otherside-cli/blob/202aa86c9d182c63f8ba9c0facf2718618de02eb/src/engine/providers/registry.ts).
- Basis: structural absence review.
- Confidence: high.
- Caveats: a user or agent can research future-oriented topics with ordinary tools, but ad hoc research inside S1 is not a standard S4 organizational loop.

### Absence scope

- Surfaces inspected: project memory, persisted/resumable sessions, goals/compaction, provider routing and quota/cooldown state, web/MCP/plugin/skill surfaces, workflows and durable subagent lifecycle.
- Plausible first-party paths checked: autonomous capability/model/tool reconfiguration from environmental trends, learned strategy/policy updates, future scenario/options generation and a return channel into current organizational design.
- Why no material first-party path remains: identified mechanisms preserve context, route current execution or expose optional capabilities; no distinct prospective adaptation owner/decision/return loop was found.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy governance loop is established.
- Disturbance / variety regulated: no identity-level or ultimate-policy conflict is routed to an authoritative S5 owner and returned as governing organizational policy.
- Decisive decision or feedback right: none established for S5.
- Decision owner: none established.
- Supporting / enforcement mechanisms: permission modes, tier ceilings/chain-of-command, provider/model settings, plugin/MCP trust controls, system/agent prompts and user approvals constrain ordinary operation but do not create identity-policy closure.
- Closure path: not applicable.
- Boundary reachability: no positive S5 path claimed.
- Why this is / is not agent-owned: the coding/coordinating agents operate within developer/user-authored policy and have no authority to redefine Otherside's identity or ultimate operating principles.
- Evidence: [README.md](https://github.com/daanielcruz/otherside-cli/blob/202aa86c9d182c63f8ba9c0facf2718618de02eb/README.md); [src/harness/tools/Agent/tool.json](https://github.com/daanielcruz/otherside-cli/blob/202aa86c9d182c63f8ba9c0facf2718618de02eb/src/harness/tools/Agent/tool.json); [src/engine/queue/runtime/permission-resolution.ts](https://github.com/daanielcruz/otherside-cli/blob/202aa86c9d182c63f8ba9c0facf2718618de02eb/src/engine/queue/runtime/permission-resolution.ts).
- Basis: structural absence review.
- Confidence: high.
- Caveats: chain-of-command/tier ceilings govern delegation scope, not organizational identity or ultimate policy.

### Absence scope

- Surfaces inspected: permission system, agent tier/route ceilings, model/provider configuration, plugin/MCP trust, system/agent prompts, session controls and goal/checkpoint state.
- Plausible first-party paths checked: autonomous constitution revision, identity conflict escalation, agent-authored ultimate policy, authoritative policy adjudication and return into operating rules.
- Why no material first-party path remains: the observed surfaces are execution policy/configuration constraints or delegated authority ceilings, not an S5 identity-governance conversation.

## Distributed OSS parent arrangement

The assessed organization is the running Otherside coding organization, not the GitHub maintainer project. Repository governance, CI/release ownership and hosted-product management are not imported as runtime S3/S4/S5 functions.

## Self-hosted and non-human modes

Otherside can run against hosted or self-hosted models and in interactive or one-shot modes. S1/S2/S3/S3* claims depend on first-party harness and agent/runtime paths rather than a particular provider or human controller.

## Recursion

The viable-unit candidate is the main coding/coordinating agent plus instantiated operational subagents. Coding agents are S1 units; the parent model owns S2 and S3 decisions over task/agent structure; a separate Verifier supplies S3*. Worktree/task registries and provider adapters are supporting mechanisms rather than additional viable systems.

## Variety and escalation

Local engineering variety remains in each S1. Cross-agent work/dependency and workspace-collision variety is attenuated through parent-selected task structure and optional worktree isolation (S2). Live task/agent state reaches the parent for reassign/steer/resume/stop decisions (S3). Non-trivial implementation claims can pass through the fresh Verifier evidence path (S3*). Persistence, routing and permissions support these loops without establishing S4/S5.

## Evidence gaps

No ? state is required. The frozen distribution exposes explicit Agent/Task/worktree/steering/stop/verifier paths and broad persistence/routing/policy surfaces sufficient for the positive S1-S3* claims and bounded negative S4/S5 conclusions.

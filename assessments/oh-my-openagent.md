---
harness_id: oh-my-openagent
project_name: oh-my-openagent
repository: https://github.com/code-yeongyu/oh-my-openagent
review_ref: 879a8b791e511edee68bada80187e0febb9b1aac
reviewed_at: 2026-09-17
profile_version: 0.2.2
assessment_procedure_version: 0.3.1
assessment_changed_at: 2026-09-17
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# oh-my-openagent

## Review boundary
Pinned OmO distribution at its OpenCode/team-mode boundary: built-in orchestrating agents, Team Mode lifecycle, team-core registry/mailbox/tasklist/worktree primitives, and the model-facing team-mode skill. Generic host capabilities are credited only where OmO supplies the organizational path and closes it through its own built-in agents.

Reviewed revision: `879a8b791e511edee68bada80187e0febb9b1aac`. Contract: Profile `0.2.2`, Methodology `0.3.1`.

## Primary evidence
- [`packages/omo-opencode/src/AGENTS.md`](https://github.com/code-yeongyu/oh-my-openagent/blob/879a8b791e511edee68bada80187e0febb9b1aac/packages/omo-opencode/src/AGENTS.md) — main OpenCode adapter, built-in agents, team/background/task runtime and lifecycle hooks.
- [`packages/omo-opencode/src/agents/AGENTS.md`](https://github.com/code-yeongyu/oh-my-openagent/blob/879a8b791e511edee68bada80187e0febb9b1aac/packages/omo-opencode/src/agents/AGENTS.md) — first-party agent factories including the main orchestrating agent.
- [`packages/omo-opencode/src/features/team-mode/AGENTS.md`](https://github.com/code-yeongyu/oh-my-openagent/blob/879a8b791e511edee68bada80187e0febb9b1aac/packages/omo-opencode/src/features/team-mode/AGENTS.md) — lead/member lifecycle, dedicated worktrees, dependency tasklist, mailbox, atomic claims and failure/orphan handling.
- [`packages/team-core/AGENTS.md`](https://github.com/code-yeongyu/oh-my-openagent/blob/879a8b791e511edee68bada80187e0febb9b1aac/packages/team-core/AGENTS.md) — team registry, task ownership/dependencies, worktree and mailbox primitives.
- [`packages/skills-loader-core/src/features/builtin-skills/skills/team-mode.ts`](https://github.com/code-yeongyu/oh-my-openagent/blob/879a8b791e511edee68bada80187e0febb9b1aac/packages/skills-loader-core/src/features/builtin-skills/skills/team-mode.ts) — model-facing lead/member operating procedure: create/assign/claim tasks, monitor status, resolve blockers, reassign work, shut down and synthesize.

## S1 — Operations
`A`. Team members are built-in autonomous agents that claim assigned or available work and execute it in their own worktrees. Their model/tool loops produce the operational outcomes of the team. Confidence: high.

## S2 — Coordination
`A`. Team Mode closes a concrete coordination loop among distinct S1s: atomic task claims prevent duplicate ownership, dependency gates suppress premature work, isolated member worktrees attenuate concurrent file interference, and the lead/member agents autonomously react to blockers and task availability. This is more than a mailbox or delegation graph because the mechanisms change later worker behavior in response to shared interference state. Confidence: high.

## S3 — Inside-and-now control
`A`. The Team Lead has a whole-team view of tasks, messages and member status and is instructed to assign/reassign work, resolve blockers, manage member lifecycle, monitor progress and own project-level completion before synthesis. Those current-control decisions are made by a first-party autonomous lead agent. Confidence: high.

## S3* — Complementary audit
`—`. Specialist/reviewer-shaped agents exist, but the reviewed Team Mode evidence does not establish a materially independent audit channel with distinct access and corrective closure over the operating team. Confidence: medium-high.

## S4 — Outside-and-then intelligence
`—`. Research/delegation specialists gather information for current work; no distinct outside-looking prospective organizational adaptation loop was established. Confidence: high.

## S5 — Policy and identity
`—`. User prompts, agent definitions and team instructions provide operating goals and role constraints, not an ultimate organizational identity/policy tension-and-resolution loop. Confidence: high.

## Recursion, variety, and escalation
Lead/member hierarchy, selectable specialist agents and parallel worktrees amplify execution variety. Atomic claims, dependencies, blocker handling and lead reassignment attenuate it; member failures and orphan states escalate into the lead/lifecycle path.

## Admission conclusion
Canonical vector: `A A A — — —`.

The earlier incomplete review stopped at the host-boundary question. The pinned Team Mode implementation resolves it: OmO supplies first-party autonomous lead/member agents plus the coordination and whole-team regulation paths they operate.
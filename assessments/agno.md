---
harness_id: agno
project_name: Agno
repository: https://github.com/agno-agi/agno
review_ref: 44219f8532e2fe6ce936850455f4b9a2567e4194
reviewed_at: 2026-09-15
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Agno

## Review boundary
Agno at the pinned revision, including first-party `Agent`, `Team` and `TeamMode.tasks` behavior. AgentOS hosting/RBAC/observability is supporting infrastructure unless the autonomous team leader itself owns the relevant organizational decision right.

## Repository architecture
Agents perform model/tool work as S1 units. Teams support route, coordinate, broadcast and autonomous tasks modes. In `TeamMode.tasks`, the leader receives model-callable task-management tools over a persistent shared `TaskList`: it can create uniquely named tasks, assign members, encode dependencies, inspect current statuses/results/notes, execute individual or parallel work, retry/reassign/change plans and mark the overall goal complete. Dependency logic blocks premature work and propagates failed dependencies to avoid deadlock.

## Primary evidence
- `libs/agno/agno/team/mode.py`: `tasks` is explicitly autonomous task-based execution in which the leader decomposes a goal into a shared task list, delegates and loops until complete.
- `libs/agno/agno/team/task.py`: persistent shared task model with status, assignee, dependencies, results, notes, availability queries, blocked-state management and failed-dependency propagation.
- `libs/agno/agno/team/_task_tools.py`: model-callable `create_task`, `update_task_status`, `list_tasks`, `add_task_note`, `execute_task` and `mark_all_complete`; member results update shared task state and failures/HITL alter subsequent execution.
- `libs/agno/agno/team/_messages.py`: task-mode instructions require the leader to read the board/results, avoid duplicate tasks, run independent work in parallel, and on failure retry, reassign or change the plan before continuing.
- `cookbook/03_teams/01_quickstart/task_mode.py`: first-party example instructs the autonomous leader to create dependencies, assign appropriate members, track completion, surface blockers and consolidate the result.

## Operational model
Member agents are S1 units. The team leader is an agent-owned metasystem actor: it sees the shared board representing current operational commitments and uses model-selected task-management tools to regulate assignment, dependencies, retries, reassignment and completion across members.

## S1 — Operations
`A`: member agents autonomously execute bounded model/tool work and return results. Confidence: high.

## S2 — Coordination
`A`: `TeamMode.tasks` provides an out-of-box agent-owned mutual-adjustment loop over a shared task board. The leader assigns ownership, prevents duplicate tasks, encodes dependencies, observes member outcomes and can retry/reassign/change the plan; dependency state prevents conflicting/premature execution. This goes beyond one-shot delegation. Confidence: high.

## S3 — Inside-and-now control
`A`: the same leader has a current whole-team view of tasks, assignees, dependency/blocked state, results and failures, plus authority to create/reprioritize through dependencies, assign/reassign members, execute work, update status and decide overall completion. That is a concrete agent-owned current-control loop over shared operational commitments. Confidence: high.

## S3* — Complementary audit
`—`: Agno lets applications compose reviewer/critic members, but the standard team runtime does not supply a distinct sufficiently independent audit channel with alternative operational access and required corrective closure. Confidence: high.

## S4 — Outside-and-then intelligence
`—`: memory, knowledge, reasoning and learning capabilities can improve team operation but do not by themselves instantiate a distinct external-and-prospective intelligence function coupled against S3. Confidence: high.

## S5 — Policy and identity
`—`: team role, instructions, permissions, approvals and identity are application/parent configured. The tasks leader regulates execution but is not given ultimate agent-owned policy/identity authority or an S3–S4 closure role. Confidence: high.

## Recursion, variety, escalation
Nested teams are technically possible, but recursion requires each nested system to demonstrate its own viable metasystem. Task dependencies, assignment and fail-closed blocking attenuate operational variety; autonomous leader replanning/reassignment amplifies corrective variety.
---
harness_id: hermes-agent
project_name: Hermes Agent
repository: https://github.com/NousResearch/hermes-agent
review_ref: 16bddc88dd325c5eef27c2cc71bbb14c16b870aa
reviewed_at: 2026-09-17
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
last_checked_ref: 16bddc88dd325c5eef27c2cc71bbb14c16b870aa
last_checked_at: 2026-09-17
assessment_changed_at: 2026-09-17
last_reassessment_round: R2
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: C(P)
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# Hermes Agent

## Review boundary
Hermes Agent at the pinned revision as the persistent agent runtime plus first-party multi-profile Bot Mode and Kanban organization. The system-in-focus includes autonomous profile processes, their shared room/board coordination, configured orchestrator surfaces, review paths, and the human CLI/dashboard parent-control mode. Deterministic dispatch, locking, persistence and status transitions are treated as support/enforcement unless an agent or parent owns the underlying organizational decision.

## Repository architecture
Hermes now supports both persistent personal-agent work and explicit multi-agent organization. Bot Mode gives separate persistent bot sessions one ordered room log with bounded turns, pass/handoff semantics and room-wide stop/hold controls. Kanban gives independent full-process profiles durable tasks, dependencies, comments, atomic claims, retry/recovery and review state. By default, an auxiliary LLM decomposer can turn a triage item into a graph, choose specialist assignees and dependency edges, and leave the root with an orchestrator profile for later completion judgment. Profiles that explicitly enable the broader `kanban` toolset gain board-routing primitives; humans and scripts operate the same board through CLI/dashboard. Kanban Swarm can additionally place a dedicated verifier between parallel workers and final synthesis.

## Primary evidence
- `apps/desktop/src/plugins/hermes-bots/group-rounds.ts` and `group-round-prompt.ts`: distinct persistent room members are serially coordinated; each agent may pass when it has no new contribution or mention a teammate to hand work off/pull it in, while the room runtime enforces bounded rounds, holds and stops.
- `hermes_cli/kanban_decompose.py`: the default decomposer asks an LLM to choose a 2–6 task graph, specialist assignees and actual dependency edges; the graph is atomically installed, and the root remains owned by the orchestrator profile so it can judge completion and add work after children finish.
- `tools/kanban_tools.py` and Kanban documentation: dispatcher workers are task-scoped, while explicitly configured orchestrator profiles receive the broader board-routing surface such as listing work and routing/unblocking tasks. Humans use CLI/dashboard over the same `kanban_db`, giving a separate whole-board intervention path whose decisions feed the dispatcher and later worker behavior.
- `hermes_cli/kanban_swarm.py` and the review lifecycle: parallel worker outputs can be gated by a separately assigned verifier before synthesis; reviewer `request_changes` returns the same task to its original implementer with concrete corrective feedback.
- Background memory/skill review remains an internal learning path from completed experience; the new organizational surfaces do not establish an external-and-prospective S4 loop or ultimate-policy S5 closure.

## Operational model
Multiple autonomous Hermes profiles can operate as distinct S1 units. Bot Mode regulates conversational participation and handoffs. Kanban profiles consume and mutate durable shared work state; agentic decomposition/routing decisions become enforced dependencies and assignments, and completed/blocked/review outcomes return into subsequent dispatch. A configured orchestrator profile can be given broader board-routing authority, while a human can instead exercise current whole-board control through the CLI/dashboard. Optional review/verifier paths challenge worker results before downstream acceptance.

## S1 — Operations
`A`: persistent Hermes profiles autonomously use tools, execute conversational/scheduled/board work and maintain operational state. Kanban workers are independent full processes with distinct profile identities and bounded task ownership. Confidence: high.

## S2 — Coordination
`A`: current first-party modes establish distinct S1 units, concrete disturbances and closed coordination responses. Bot Mode agents autonomously choose to pass or hand work to named peers while the room runtime bounds repeated turns. In Kanban, the default LLM decomposer chooses assignees and dependency edges that change which workers may run, while shared claims/dependencies/recovery suppress duplicate execution, invalid ordering and retry thrashing. The model/profile owns meaningful coordination discretion; deterministic room/dispatcher machinery transports and enforces those decisions. Confidence: high.

## S3 — Inside-and-now control
`C(P)`: Hermes exposes a dedicated autonomous current-control construction path, but does not supply one universally active autonomous S3 owner. An explicitly configured orchestrator profile can receive board-wide discovery/routing primitives, create/link/unblock work and act separately from implementation workers; the decomposed root also returns to its orchestrator for completion judgment and further commitments. Developer/operator configuration still selects that profile and grants the broader `kanban` surface, so the autonomous path is Constructor-level rather than out-of-box `A`.

A distinct parent mode is first-party and closed: the human CLI/dashboard sees the shared board and can create/assign/link/unblock or change current task state; those decisions enter the same database and dispatcher that governs later worker execution. This is whole-system current-control over active commitments rather than a generic approval/kill hook, so the published state is `C(P)`. Confidence: high.

## S3* — Complementary audit
`C`: Hermes supplies a first-party complementary-review construction path. `kanban_request_review` can transfer a completed implementation into a distinct review run, and a reviewer can `request_changes`, closing the review and routing the task back to the original implementer. Kanban Swarm separately gates synthesis on a verifier that reads every worker handoff/blackboard update and may pass only when evidence is sufficient. However, reviewer/verifier identity and independence are selected by configuration/topology rather than guaranteed by a single standard autonomous auditor, so the correct state is Constructor. Confidence: high.

## S4 — Outside-and-then intelligence
`—`: memory/skill background review, routines and self-improvement can alter later behavior, but they learn from current/internal experience or schedule work. No distinct externally and prospectively oriented intelligence function was established that develops future adaptation options in a two-way S3–S4 loop. Confidence: high.

## S5 — Policy and identity
`—`: profiles, prompts, permissions, tools and orchestration settings are user/developer authored. Human control over ordinary board commitments is S3-level parent regulation, not evidence of identity- or ultimate-policy-level closure. Confidence: high.

## Recursion, variety, escalation
Named profiles and durable board tasks materially increase organizational variety, but a profile/task is not automatically a recursively viable subsystem. Kanban dependencies, blocking, review, retries, orchestrator intervention and human board control provide explicit escalation paths while preserving local worker scope. The reviewed revision therefore moves Hermes from a single-S1 characterization to a multi-S1 organization with autonomous S2, configurable/parent-assisted S3 and composable S3*.
---
harness_id: qwen-code
project_name: Qwen Code
repository: https://github.com/QwenLM/qwen-code
review_ref: 3ac6fe65e81c84897c02d22abd3dc91d1e567d5f
reviewed_at: 2026-09-17
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
last_checked_ref: 3ac6fe65e81c84897c02d22abd3dc91d1e567d5f
last_checked_at: 2026-09-17
assessment_changed_at: 2026-09-17
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Qwen Code

## Review boundary
Qwen Code at the pinned current `main` revision, including the primary coding agent, TeamManager/team tools, shared task state, teammate messaging/backpressure, teammate lifecycle and the standard approval modes. Team vocabulary is not treated as VSM evidence by itself; the positive S2/S3 states come from concrete disturbance-regulation and current-control rights.

## Repository architecture
Qwen Code can instantiate a first-party agent team under `TeamManager`. Distinct teammate agents have mailboxes and shared task state. TeamManager serializes team state, routes messages with priority, detects idle members, performs automatic task claiming and applies bounded backpressure to a teammate's pending-message queue. A model-driven team leader can create/assign team work and has a structurally leader-only `request_shutdown` tool whose effect ends another agent's participation and releases task ownership.

The same sensitive team-control tools are integrated with Qwen Code's permission system. In autonomous approval modes the agent's intervention proceeds under first-party policy/classifier control; in the interactive/default approval mode an `ask` decision is surfaced to the parent user, whose allow/deny response gates execution. That is a separate parent-governed closure of the same current-control path, not S5.

## Primary evidence
- [`packages/core/src/agents/team/TeamManager.ts`](https://github.com/QwenLM/qwen-code/blob/3ac6fe65e81c84897c02d22abd3dc91d1e567d5f/packages/core/src/agents/team/TeamManager.ts): owns team state/lifecycle, priority message routing, idle detection, task claiming and bounded per-agent message backpressure; the cap explicitly prevents a looping/hallucinating teammate from flooding a busy teammate.
- [`packages/core/src/tools/request-shutdown.ts`](https://github.com/QwenLM/qwen-code/blob/3ac6fe65e81c84897c02d22abd3dc91d1e567d5f/packages/core/src/tools/request-shutdown.ts): leader-only current-control action; a shutdown ends teammate participation, releases task ownership and excludes the pending member from automatic assignment.
- [`packages/core/src/tools/agent/agent.ts`](https://github.com/QwenLM/qwen-code/blob/3ac6fe65e81c84897c02d22abd3dc91d1e567d5f/packages/core/src/tools/agent/agent.ts): model-facing agent/team creation path; the agent tool uses an `ask` permission default rather than transferring organizational ownership to the permission runtime.
- [`docs/users/features/approval-mode.md`](https://github.com/QwenLM/qwen-code/blob/3ac6fe65e81c84897c02d22abd3dc91d1e567d5f/docs/users/features/approval-mode.md): first-party approval modes distinguish interactive confirmation from more autonomous execution modes.

## Operational model
A leader and multiple teammate agents perform S1 work. Shared task ownership and message channels let peers/leader adjust work; TeamManager enforces atomicity, queue bounds and lifecycle. The leader can change current team membership/commitments, with an optional parent-confirmed mode for those interventions.

## S1 — Operations
`A`: coding agents autonomously perform tool-using work inside their assigned scope. Confidence: high.

## S2 — Coordination
`A`: multiple S1 teammates share task ownership and messages. Atomic claiming prevents duplicate task ownership, priority delivery changes subsequent teammate behavior, and bounded pending-message queues attenuate a concrete flood/interference mode. Agents choose task/message actions while TeamManager provides deterministic enforcement and feedback. Confidence: high.

## S3 — Inside-and-now control
`A(P)`: the team leader is an autonomous current-control actor over the team. It can create/direct teammates and invoke a leader-only shutdown that removes a teammate from participation and releases its task commitment; TeamManager supplies the whole-team state/lifecycle substrate and closes the intervention. Separately, Qwen Code's interactive approval mode can require the parent user to allow/deny these `ask`-classified team-control actions before execution, establishing a distinct parent-governed S3 mode. Confidence: high.

## S3* — Complementary audit
`—`: no distinct complementary audit actor/path with materially different access to operational reality and findings returned into current control was established. Confidence: high.

## S4 — Outside-and-then intelligence
`—`: no separate outside-and-future adaptation loop was established. Confidence: high.

## S5 — Policy and identity
`—`: approval modes and team-action permissions govern operational interventions. They do not establish a first-party identity/ultimate-policy question and legitimate ultimate-authority loop, so the previous generic `S5=P` interpretation is removed. Confidence: high.

## Recursion, variety, escalation
Team members increase operational variety. Shared tasks, priority messaging and queue backpressure attenuate coordination variety; leader lifecycle control attenuates current organizational variety. Interactive permission mode provides a parent escalation path for sensitive S3 actions without turning ordinary approval into S5.

## Admission conclusion
Canonical vector at the pinned revision: `A A A(P) — — —`. The proposal's S2 remains supported, S3 is upgraded from constructor to autonomous-plus-parent because the leader actor/authority/closure is first-party, and generic approval is removed from S5.
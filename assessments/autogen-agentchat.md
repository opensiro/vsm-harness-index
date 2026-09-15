---
harness_id: autogen-agentchat
project_name: Microsoft AutoGen AgentChat
repository: https://github.com/microsoft/autogen
review_ref: 027ecf0a379bcc1d09956d46d12d44a3ad9cee14
reviewed_at: 2026-09-15
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Microsoft AutoGen AgentChat

## Review boundary
AutoGen AgentChat at the pinned revision. Microsoft Agent Framework is its successor and is assessed separately.

## Repository architecture
AutoGen supplies autonomous tool-using agents plus AgentChat group-chat/team patterns over a message/event runtime. `MagenticOneOrchestrator` adds a persistent whole-team task/facts/plan ledger and progress/stall feedback around those workers.

## Primary evidence
- `python/packages/autogen-agentchat/src/autogen_agentchat/teams/_group_chat/_selector_group_chat.py`: participant filtering, selection and repeated-speaker policy coordinate team turns.
- `python/packages/autogen-agentchat/src/autogen_agentchat/teams/_group_chat/_magentic_one/_magentic_one_orchestrator.py`: keeps the team task, facts, plan, round/stall state and repeatedly assesses request satisfaction, progress and loops; it chooses the next speaker and resets/replans the team when stalls cross the configured threshold.
- `python/packages/autogen-agentchat/tests/test_magentic_one_group_chat.py`: the stall test exercises two no-progress/in-loop assessments followed by regenerated facts/plan and continued execution; save/load tests preserve task, facts, plan, rounds and stalls.

## Operational model
Individual assistants are S1 units. Team protocols regulate which participant may act next. Magentic-One additionally observes the whole current team, retains its commitments and progress state, detects loss of progress, and can replace the current plan/reset participants before work continues.

## S1 — Operations
`A`: stateful agents choose tools/actions and incorporate returned results. Confidence: high.

## S2 — Coordination
`A`: team selection plus Magentic-One's explicit loop/stall detection and controlled transfer of the next action right suppress uncontrolled repetition/interference among multiple S1 participants. This is more than mere delegation. Confidence: high.

## S3 — Inside-and-now control
`A`: `MagenticOneOrchestrator` owns a whole-team current facts/plan/progress ledger and has authority to assess progress, choose commitments, reset participants and regenerate the plan when the team stalls. That closes a superior inside-now regulation loop over the S1 team. Confidence: high.

## S3* — Complementary audit
`—`: the progress ledger is part of the same operational S3 regulator that directs the team. It is not a distinct complementary audit channel with separate reviewing independence.

## S4 — Outside-and-then intelligence
`—`: replanning after current-task stalls is inside-now adaptation. No distinct external/prospective intelligence function shaping future organizational posture is established.

## S5 — Policy and identity
`—`: participant set, instructions, termination rules and ultimate authority remain application/parent-owned.

## Recursion, variety, escalation
Teams and nested tools are compositional structures; recursive viability requires local metasystemic closure beyond the single Magentic-One team boundary.
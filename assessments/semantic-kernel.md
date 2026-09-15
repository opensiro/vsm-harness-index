---
harness_id: semantic-kernel
project_name: Semantic Kernel
repository: https://github.com/microsoft/semantic-kernel
review_ref: ca40aa7226531d28a721d0ca0e451d0aaf86dafc
reviewed_at: 2026-09-15
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# Semantic Kernel

## Review boundary
Semantic Kernel at the pinned revision. Microsoft Agent Framework is its successor but remains a separate repository/system. The previous stored SHA was not resolvable upstream; this deep review explicitly repins the assessment to the current reproducible `main` HEAD shown above.

## Repository architecture
Semantic Kernel ships multiple orchestration types, including concurrent, sequential, handoff and group-chat orchestration. The Python group-chat runtime contains a dedicated `GroupChatManager` abstraction plus manager actor that regulates the conversation among autonomous agent actors.

## Primary evidence
- `python/semantic_kernel/agents/orchestration/group_chat.py`: `GroupChatManager` is explicitly responsible for managing group-chat flow.
- The manager has function-specific decision points `select_next_agent()`, `should_terminate()`, `should_request_user_input()` and `filter_results()` over shared `ChatHistory` and participant descriptions.
- `RoundRobinGroupChatManager` is a supplied concrete manager implementation; application code can also subclass the manager to provide model/policy-driven selection.
- `python/samples/getting_started_with_agents/multi_agent_orchestration/step3b_group_chat_with_chat_completion_manager.py` shows first-party composition of a chat-completion-based manager implementing next-agent selection and result filtering.

## Operational model
Participant agents are S1 units. The manager is a distinct first-party organizational primitive whose explicit job is regulating which participant may act next, when the group stops, when user input is requested and what result is returned.

## S1 — Operations
`A`: agents own bounded model/tool decisions and produce task outcomes. Confidence: high.

## S2 — Coordination
`C`: `GroupChatManager` exposes a function-specific coordination decision path over multiple autonomous participants: next-speaker selection, termination and shared-history feedback. However, the actual autonomous manager policy/authority is application-composed, and the default round-robin manager is deterministic. This satisfies the composable S2 threshold but not out-of-box agent-owned `A`. Confidence: high.

## S3 — Inside-and-now control
`?`: the manager controls conversational turn flow, but this pass did not establish whole-system resource/commitment regulation with S3 authority beyond the group-chat coordination domain.

## S3* — Complementary audit
`?`: `filter_results()` is output selection, not by itself an independent audit path with separate reality access and corrective authority.

## S4 — Outside-and-then intelligence
`?`: planning/plugins/environment access do not by themselves establish a distinct prospective adaptation function coupled to S3.

## S5 — Policy and identity
`?`: agent instructions and manager/application policy remain parent-supplied; no runtime ultimate-policy closure was established.

## Recursion, variety, escalation
Group-chat participant composition is not automatically recursive viability.

## Deep-review result
`S2` resolves from `?` to `C` based on a concrete first-party coordination abstraction and decision path. Other metasystem functions remain unresolved.
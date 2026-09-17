---
harness_id: codex
project_name: Codex
repository: https://github.com/openai/codex
review_ref: b974893c90048d147207ae9004489c02f3116426
reviewed_at: 2026-09-17
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
last_checked_ref: b974893c90048d147207ae9004489c02f3116426
last_checked_at: 2026-09-17
assessment_changed_at: 2026-09-17
last_reassessment_round: R2
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: C
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# Codex

## Review boundary
Deep reassessment of the pinned autonomous coding runtime, MultiAgent V2 team-control surface, proactive delegation mode and Guardian automatic approval reviewer. Organizational functions are established from decision rights rather than from agent, manager, review or policy vocabulary alone.

## Repository architecture
Codex is an autonomous coding harness with sandboxed tool execution, first-party multi-agent collaboration and a separate approval-review subsystem. MultiAgent V2 lets a root agent spawn a tree of capable workers, inspect all live agents in that root tree, send messages and follow-up tasks, wait on mailbox/status updates, and interrupt or close workers and descendants. The V2 feature is stable but disabled by default, so this is a supplied constructor path rather than the ordinary out-of-box mode.

Separately, approval requests can be routed to `auto_review` instead of the default user reviewer. AutoReview runs a distinct Guardian review session over a captured proposed action and host constraints, may gather additional read-only context, and returns a structured allow/deny decision into the execution path.

## Primary evidence
- [`codex-rs/prompts/src/model_messages/multi_agent.rs`](https://github.com/openai/codex/blob/b974893c90048d147207ae9004489c02f3116426/codex-rs/prompts/src/model_messages/multi_agent.rs): defines root/subagent team roles and proactive autonomous delegation guidance.
- [`codex-rs/core/src/tools/handlers/multi_agents_spec.rs`](https://github.com/openai/codex/blob/b974893c90048d147207ae9004489c02f3116426/codex-rs/core/src/tools/handlers/multi_agents_spec.rs): exposes root-tree visibility and the spawn/message/follow-up/wait/interrupt/close control surface.
- [`codex-rs/features/src/lib.rs`](https://github.com/openai/codex/blob/b974893c90048d147207ae9004489c02f3116426/codex-rs/features/src/lib.rs): classifies `multi_agent_v2` as stable while leaving it disabled by default.
- [`codex-rs/protocol/src/config_types.rs`](https://github.com/openai/codex/blob/b974893c90048d147207ae9004489c02f3116426/codex-rs/protocol/src/config_types.rs): `ApprovalsReviewer` defaults to `user`; `auto_review` invokes a prompted subagent to gather context and apply a risk-based approval decision.
- [`codex-rs/ext/guardian-reviewer/src/routing.rs`](https://github.com/openai/codex/blob/b974893c90048d147207ae9004489c02f3116426/codex-rs/ext/guardian-reviewer/src/routing.rs) and [`assessment.rs`](https://github.com/openai/codex/blob/b974893c90048d147207ae9004489c02f3116426/codex-rs/ext/guardian-reviewer/src/assessment.rs): close the independent review path with captured-action validation and structured allow/deny outcomes.

## Operational model
A coding S1 iterates over repository state and tools. In the optional MultiAgent V2 mode, a root agent can build and currently regulate a live worker tree while workers perform delegated operational tasks. In the optional AutoReview path, a distinct Guardian session challenges a proposed privileged/risky action before the action is allowed to proceed.

## S1 — Operations
`A`: the coding agent autonomously selects actions/tools and reacts to execution feedback. Confidence: high.

## S2 — Coordination
`—`: proactive spawning and direct agent messaging improve collaboration, but the reviewed first-party responsibility remains task delegation/communication. No dedicated agent-owned mechanism was established whose organizational function is to regulate recurring interference, oscillation or shared constraints among peer S1 units. The function-first boundary therefore still rejects delegation or messaging alone as S2.

## S3 — Inside-and-now control
`C`: MultiAgent V2 supplies a first-party constructor path for current regulation of the whole active worker tree. The root can enumerate all live agents, assign follow-up commitments, observe completion/status, interrupt work, and close agents/descendants to release bounded concurrency. Those are whole-tree current-control rights beyond merely receiving one child result. The feature is stable but `default_enabled: false`, so Codex supplies the organizational path without making it the ordinary autonomous default.

## S3* — Complementary audit
`C`: AutoReview supplies a distinct first-party Guardian reviewer that receives the proposed action separately from the operating agent, can perform read-only evidence gathering, and returns an allow/deny decision that gates execution. This establishes a complementary challenge path with corrective blocking authority. Reviewer selection is configurable and defaults to the user rather than to AutoReview, so the supplied autonomous audit path is constructor-level rather than default `A`.

## S4 — Outside-and-then intelligence
`—`: repository exploration, planning, model selection and multi-agent delegation serve current coding work. No distinct prospective environment-intelligence function with a strategic adaptation closure path was established.

## S5 — Policy and identity
`—`: sandbox policy, permissions, approval reviewer selection and Guardian policy constrain operational actions but remain configured outside the agent organization. They do not establish harness-owned ultimate identity or policy authority.

## Recursion, variety, escalation
Codex now exposes substantially richer recursive team control than the accepted assessment: capable agents can form nested worker trees, while a root can regulate the live tree and Guardian can independently challenge selected actions. These are classified as S3 and S3* constructor paths respectively; generic delegation and messaging still do not establish S2.
---
harness_id: crush
project_name: Crush
repository: https://github.com/charmbracelet/crush
review_ref: 102f75616d0bbc25377c6b12a2b320fbd3b242a2
reviewed_at: 2026-09-15
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Crush

## Review boundary
Deep review of the pinned core agent/session runtime. Internal naming such as `orchestration`, queues and subagent mode is evaluated at the functional boundary of one coding-agent runtime rather than treated as evidence of a multi-S1 metasystem.

## Repository architecture
Crush implements a session-based terminal coding agent that coordinates model calls, tool execution, messages, session state, token management, queuing and automatic summarization. The core `sessionAgent` also carries an `isSubAgent` mode, but the reviewed runtime remains one operational agent abstraction with session-local dispatch/state machinery rather than a separate organizational control layer.

## Primary evidence
- `internal/agent/agent.go`: describes the package as the core orchestration layer for session-based AI agent functionality and coordinates conversations, tool execution, sessions, messages, summarization, queues and token management.
- `sessionAgent` owns tools, prompts, session/message services, request queues/cancellation and an `isSubAgent` flag inside the same operational runtime.
- Per-session mutex/queue/cancel handling serializes runtime requests; it is session execution infrastructure, not regulation among autonomous organizational S1s.

## Operational model
A session agent receives prompts, invokes the model, executes tools and maintains conversation/session state while runtime machinery queues or cancels concurrent requests and summarizes context as needed.

## S1 — Operations
`A`: the coding agent autonomously chooses tools/actions and iterates from repository/tool feedback. Confidence: high.

## S2 — Coordination
`—`: session queues, dispatch serialization and subagent mode operate inside the runtime abstraction; no separate mechanism was found for regulating interference among multiple autonomous S1 units.

## S3 — Inside-and-now control
`—`: request/session lifecycle management is infrastructure for an S1, not whole-system current authority over shared organizational resources/capacity/commitments.

## S3* — Complementary audit
`—`: review-shaped prompts and normal checks remain inside operational work; no independent complementary audit channel was established.

## S4 — Outside-and-then intelligence
`—`: summarization/context management and task reasoning support current execution, not prospective environmental intelligence and organizational adaptation.

## S5 — Policy and identity
`—`: prompts, models, tools and runtime policy are externally configured.

## Recursion, variety, escalation
Crush exposes a capable operational runtime and subagent-capable mode, but no reviewed S2–S5 organizational function is closed.
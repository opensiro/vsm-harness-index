---
harness_id: oh-my-pi
project_name: oh-my-pi
repository: https://github.com/can1357/oh-my-pi
review_ref: 165cede8400d833382177a4dfd2901271c9f0a2c
reviewed_at: 2026-09-15
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# oh-my-pi

## Review boundary
Oh My Pi at the pinned revision as a coding-agent harness including first-class subagents, peer communication and the separate advisor-model role.

## Repository architecture
OMP supplies IDE/LSP/debugger/code-execution tools, first-class subagents in isolated worktrees, typed result return, peer communication, an Agent Hub, and an optional advisor subsystem that reviews primary-agent updates using separate agent/tool state.

## Primary evidence
- `README.md`: isolated subagent fan-out, peer coordination, Agent Hub and advisor capability.
- `docs/advisor-watchdog.md`: each advisor is a full agent with its own `Agent` instance and distinct `ToolSession`; it receives primary transcript deltas, can independently inspect the workspace with read/grep/glob (or explicitly granted tools), and injects advice back into the primary transcript.
- `docs/advisor-watchdog.md`: `concern` and `blocker` severities can interrupt/steer live work or trigger a follow-up turn, while advisor messages are filtered from subsequent advisor input to avoid self-review.

## Operational model
Coding/subagents are S1. Worktree isolation deterministically prevents some collisions; peer communication exposes an agent-level coordination path. The advisor is a distinct observer with separate runtime/tool context and an explicit corrective channel into the operating agent.

## S1 — Operations
`A`: coding agents autonomously use the rich tool/IDE surface to produce outcomes. Confidence: high.

## S2 — Coordination
`C`: first-party peer communication plus isolated subagent workspaces expose a concrete coordination path among operational agents, but a general mutual-adjustment protocol/authority still depends on the composed task/constraints. Confidence: medium-high.

## S3 — Inside-and-now control
`—`: Agent Hub and parent/subagent controls expose execution management but do not give an autonomous actor whole-system resource, priority and accountability authority in the S3 sense.

## S3* — Complementary audit
`A`: a separate advisor agent with its own agent/tool session independently reviews primary transcript updates, can inspect workspace reality, and feeds `concern`/`blocker` findings back through a steering path that can alter subsequent primary-agent operation. Confidence: high.

## S4 — Outside-and-then intelligence
`—`: no reviewed mechanism models relevant external future change and develops adaptation options coupled to present operations; planning/search alone do not qualify.

## S5 — Policy and identity
`—`: rules, permissions, prompts and ultimate task authority remain parent/user authored rather than agent-owned policy closure.

## Recursion, variety, escalation
Subagents are operational workers. Peer messaging and advisor feedback add metasystemic paths without proving recursive viability of child agents.
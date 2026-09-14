---
harness_id: oh-my-pi
project_name: oh-my-pi
repository: https://github.com/can1357/oh-my-pi
review_ref: 165cede8400d833382177a4dfd2901271c9f0a2c
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: ?
autonomy_s3_star: A
autonomy_s4: ?
autonomy_s5: ?
---

# oh-my-pi

## Review boundary
Oh My Pi at the pinned revision as a coding-agent harness including first-class subagents, peer communication and the separate advisor-model role.

## Repository architecture
OMP supplies IDE/LSP/debugger/code-execution tools, first-class subagents in isolated worktrees, typed result return, peer IRC messaging, an Agent Hub, and an advisor model that observes every main-agent turn from its own model/context and can inject notes, concerns or hard blockers.

## Primary evidence
- `README.md`: isolated subagent fan-out, peer IRC coordination example, Agent Hub; dedicated advisor on a separate model/context observing every turn and injecting corrective feedback/blockers.

## Operational model
Coding/subagents are S1. Worktree isolation deterministically prevents some collisions; peer messaging exposes an agent-level coordination path. The advisor is a distinct observer with separate context/model and a direct corrective channel into the operating agent.

## S1 — Operations
`A`: coding agents autonomously use the rich tool/IDE surface to produce outcomes. Confidence: high.

## S2 — Coordination
`C`: first-party peer messaging plus isolated subagent workspaces expose a concrete coordination path among operational agents, but a general mutual-adjustment protocol/authority still depends on the composed task/constraints. Confidence: medium-high.

## S3 — Inside-and-now control
`?`: Agent Hub and parent control do not prove autonomous whole-system resource/accountability authority.

## S3* — Complementary audit
`A`: the advisor is a separate agent/model with its own context, observes the main agent's turns independently, can raise concerns/hard blockers, and feeds them directly back so the operating agent course-corrects. This is complementary audit beyond ordinary logging/QA. Confidence: high.

## S4 — Outside-and-then intelligence
`?`: no distinct external/prospective adaptation role coupled to S3 is verified.

## S5 — Policy and identity
`?`: rules/permissions remain parent-authored.

## Recursion, variety, escalation
Subagents are operational workers. Peer messaging and advisor feedback add metasystemic paths without proving recursive viability of child agents.
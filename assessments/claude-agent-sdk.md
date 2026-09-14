---
harness_id: claude-agent-sdk
project_name: Claude Agent SDK
repository: https://github.com/anthropics/claude-agent-sdk-python
review_ref: 37a52c9fb3f0271de017911914b0d42efea6267e
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# Claude Agent SDK

## Review boundary
Claude Agent SDK Python at the pinned revision, wrapping the bundled Claude Code CLI and its tool/permission/hook behavior.

## Repository architecture
The SDK exposes interactive Claude Code agent sessions, Read/Write/Edit/Bash tools, custom MCP tools, permissions and Python hooks. It is primarily an SDK surface over one Claude Code operational agent.

## Primary evidence
- `README.md`: bundled Claude Code CLI; `query`/`ClaudeSDKClient`; tools, permissions, custom MCP tools and hooks.

## Operational model
A Claude Code-backed session is S1. Hooks/permissions constrain the loop; tools are operational capabilities.

## S1 — Operations
`A`: Claude autonomously chooses available tools/actions within a session. Confidence: high.

## S2 — Coordination
`—`: no first-party multi-S1 anti-oscillation relation is established by the reviewed SDK evidence.

## S3 — Inside-and-now control
`?`: permissions/hooks are runtime constraints, not autonomous whole-system regulation.

## S3* — Complementary audit
`?`: hooks can inspect/validate events but sufficient independent audit role/feedback closure is not supplied out of the box.

## S4 — Outside-and-then intelligence
`?`: no prospective environment/adaptation function verified.

## S5 — Policy and identity
`?`: system prompts and permission policy are parent-defined.

## Recursion, variety, escalation
Custom tools/MCP amplify one S1's variety; no recursion is established.
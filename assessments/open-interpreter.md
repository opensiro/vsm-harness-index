---
harness_id: open-interpreter
project_name: Open Interpreter
repository: https://github.com/openinterpreter/openinterpreter
review_ref: f110a7a85f43efc343f936f5bc504e01eb262550
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# Open Interpreter

## Review boundary
Open Interpreter at the pinned revision, focusing on the coding-agent runtime/harness emulation layer rather than provider organizations or external MCP servers.

## Repository architecture
The Rust-based coding agent is a Codex fork focused on harness behavior for low-cost models. It runs commands in native sandboxes, supports harness switching, MCP/ACP, skills, hooks, permissions and shared AGENTS.md instructions.

## Primary evidence
- `README.md`: coding agent; Codex-derived harness loop; command execution, sandboxing, skills/hooks/permissions, MCP/ACP and harness switching.

## Operational model
The coding agent is S1. Harness variants, sandbox and permissions shape its local action loop rather than forming separate viable operational units.

## S1 — Operations
`A`: the agent executes coding actions/tools and reacts to workspace results. Confidence: high.

## S2 — Coordination
`—`: no material multi-S1 anti-oscillation function established at this boundary.

## S3 — Inside-and-now control
`?`: sandbox/permission controls are constraints, not autonomous whole-system regulation.

## S3* — Complementary audit
`?`: QA skill/testing is routine operational validation and does not by itself prove independent audit.

## S4 — Outside-and-then intelligence
`?`: tool/browser use does not establish a prospective adaptation function.

## S5 — Policy and identity
`?`: AGENTS.md, permissions and harness configuration remain parent-authored constraints.

## Recursion, variety, escalation
Harness switching changes one S1's operating policy/mechanics; it does not create recursive viable systems.
---
harness_id: continue
project_name: Continue
repository: https://github.com/continuedev/continue
review_ref: 5522c6f44ca0ac3528b37244818fbfa39b5af470
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# Continue

## Review boundary
Continue at the pinned revision as the coding-agent implementation delivered through CLI/VS Code/JetBrains surfaces.

## Repository architecture
The repository identifies Continue as a coding agent with CLI and IDE integrations. The surfaces expose one coding operation against workspace context; UI/plugin packaging is not a separate organizational layer.

## Primary evidence
- `README.md`: Continue as an open-source coding agent across CLI, VS Code and JetBrains; repository/module boundaries.

## Operational model
The coding agent is S1. IDE/CLI adapters provide environment and interaction channels.

## S1 — Operations
`A`: the coding agent performs bounded workspace-oriented coding work. Confidence: medium-high.

## S2 — Coordination
`—`: no material first-party multi-S1 anti-oscillation path is established at this boundary.

## S3 — Inside-and-now control
`?`: no autonomous whole-system regulator verified.

## S3* — Complementary audit
`?`: no independent complementary audit path verified.

## S4 — Outside-and-then intelligence
`?`: workspace context does not establish future/environment adaptation.

## S5 — Policy and identity
`?`: configuration/instructions remain parent-owned.

## Recursion, variety, escalation
Multiple client surfaces wrap the same operational agent and do not constitute recursion.
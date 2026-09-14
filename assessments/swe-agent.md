---
harness_id: swe-agent
project_name: SWE-agent
repository: https://github.com/SWE-agent/SWE-agent
review_ref: 3ea751c087f32b16e039a2233dd6eefecef325d5
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# SWE-agent

## Review boundary
SWE-agent at the pinned revision as a configurable autonomous software-engineering agent. SWE-bench and mini-SWE-agent are separate projects.

## Repository architecture
SWE-agent gives a language model an agent-computer interface and tool access for repository issues/custom tasks, leaving substantial action choice to the model under a YAML configuration.

## Primary evidence
- `README.md`: autonomous tool use on real repositories; maximal LM agency; configurable research-oriented harness; explicit project boundaries.

## Operational model
One coding agent is S1; its ACI/tools and configuration constrain its operational loop.

## S1 — Operations
`A`: the model autonomously chooses repository/tool actions and iterates toward task completion. Confidence: high.

## S2 — Coordination
`—`: no first-party multi-S1 coordination function established.

## S3 — Inside-and-now control
`?`: execution controls are not a whole-system autonomous regulator.

## S3* — Complementary audit
`?`: benchmark/test use is not evidence of independent runtime audit.

## S4 — Outside-and-then intelligence
`?`: repository feedback serves the current task rather than future adaptation.

## S5 — Policy and identity
`?`: YAML/instructions remain parent-authored.

## Recursion, variety, escalation
The ACI amplifies one operational agent; no recursive viable subsystem is established.
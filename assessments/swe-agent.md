---
harness_id: swe-agent
project_name: SWE-agent
repository: https://github.com/SWE-agent/SWE-agent
review_ref: 3ea751c087f32b16e039a2233dd6eefecef325d5
reviewed_at: 2026-09-15
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# SWE-agent

## Review boundary
SWE-agent at the pinned revision as a configurable autonomous software-engineering agent. SWE-bench and mini-SWE-agent are separate projects.

## Repository architecture
SWE-agent gives a language model an agent-computer interface and tool access for repository issues/custom tasks, leaving substantial action choice to the model under YAML configuration. Retry wrappers can run alternative attempts, but each attempt remains one coding agent run.

## Primary evidence
- `sweagent/agent/agents.py`: the agent run owns one trajectory, tool/action loop, finalization and run hooks.
- `config/benchmarks/250212_sweagent_heavy_sbl.yaml`: retry configuration composes repeated agent attempts rather than a standing multi-S1 organization.
- Pinned demonstration/test trajectories show the same agent reading execution feedback, fixing edits and submitting the result.

## Operational model
One coding agent is S1. ACI checks, syntax feedback, retries, hooks, trajectories and benchmark evaluation surround that operation rather than create autonomous metasystem roles.

## S1 — Operations
`A`: the model autonomously chooses repository/tool actions and iterates toward task completion. Confidence: high.

## S2 — Coordination
`—`: no first-party multi-S1 mutual-adjustment function is established.

## S3 — Inside-and-now control
`—`: retry/configuration/run controls do not regulate current commitments or resources across multiple S1 units.

## S3* — Complementary audit
`—`: benchmark evaluation, lint/test feedback and trajectory hooks are normal execution/evaluation support, not a distinct autonomous audit channel with corrective authority.

## S4 — Outside-and-then intelligence
`—`: repository and test feedback serve the current software task rather than a prospective environmental adaptation loop.

## S5 — Policy and identity
`—`: YAML configuration, prompts, tool policy and budgets remain parent authored.

## Recursion, variety, escalation
The ACI amplifies one operational agent; no recursive viable subsystem is established.
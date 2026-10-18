---
harness_id: swe-agent
project_name: SWE-agent
repository: https://github.com/SWE-agent/SWE-agent
review_ref: 3ea751c087f32b16e039a2233dd6eefecef325d5
reviewed_at: 2026-09-15
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
last_checked_ref: 3ea751c087f32b16e039a2233dd6eefecef325d5
last_checked_at: 2026-09-17
assessment_changed_at: 2026-09-15
last_reassessment_round: R2
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# SWE-agent

## Review boundary
SWE-agent at the pinned revision as a configurable autonomous software-engineering agent, including its first-party retry/reviewer wrappers. SWE-bench and mini-SWE-agent are separate projects.

## Repository architecture
SWE-agent gives a language model an agent-computer interface and tool access for repository issues/custom tasks, leaving substantial action choice to the model under YAML configuration. Its optional `RetryAgent` can run multiple operational attempts and place a distinct reviewer/chooser loop above them.

## Primary evidence
- `sweagent/agent/agents.py`: a normal agent run owns one trajectory/tool-action loop, while `RetryAgent` composes multiple attempts under `ScoreRetryLoop` or `ChooserRetryLoop` and can trigger another attempt based on review outcome.
- `sweagent/agent/reviewer.py`: first-party reviewer models score completed attempts or compare candidate trajectories/proposals, returning review decisions used by the retry wrapper.
- `config/benchmarks/250212_sweagent_heavy_sbl.yaml`: reviewer/retry behavior is explicitly selectable configuration rather than mandatory for every standard run.
- Pinned demonstration/test trajectories show the operational agent itself reading execution feedback, fixing edits and submitting results; that ordinary self-checking remains S1 rather than S3*.

## Operational model
One coding agent is S1. Lint/test feedback and trajectory hooks remain inside its operation. The optional retry wrapper is different: a distinct reviewer/chooser assesses completed operational attempts and can reject them by causing further work or select among alternatives.

## S1 — Operations
`A`: the model autonomously chooses repository/tool actions and iterates toward task completion. Confidence: high.

## S2 — Coordination
`—`: repeated candidate runs do not establish mutual adjustment among simultaneously autonomous S1 units.

## S3 — Inside-and-now control
`—`: retry orchestration does not maintain a current organization-wide commitment/resource regulator.

## S3* — Complementary audit
`C`: first-party `ScoreRetryLoop`/`ChooserRetryLoop` reviewer paths separately assess operational attempts and their verdict can force another attempt or select a better candidate. This supplies a composable complementary audit path, but it is optional rather than the default closed agent run.

## S4 — Outside-and-then intelligence
`—`: repository and test feedback serve the current software task rather than a prospective environmental adaptation loop.

## S5 — Policy and identity
`—`: YAML configuration, prompts, reviewer choice, tool policy and budgets remain parent authored.

## Recursion, variety, escalation
Retry/reviewer composition adds an assurance layer around one operational task but does not establish recursive viable-system closure.
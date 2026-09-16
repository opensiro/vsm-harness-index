---
harness_id: gemini-cli
project_name: Gemini CLI
repository: https://github.com/google-gemini/gemini-cli
review_ref: 6a466a7e2fe2b1255752c1e74f69b31f0216084d
reviewed_at: 2026-09-16
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: P
---

# Gemini CLI

## Review boundary
Pinned first-party terminal/coding agent including scheduler policy/confirmation, local sub-agent executor and agent registry.

## Repository architecture
Gemini CLI supplies a first-party agent, local sub-agent execution/registry and scheduler/confirmation mechanisms that bound and coordinate runtime work.

## Primary evidence
- Pinned deep review established scheduler policy/confirmation, local sub-agent executor, agent registry and approval mode at `review_ref`.

## Operational model
The main/sub-agents perform autonomous operations while runtime scheduling and confirmation primitives provide constructor-owned coordination/current regulation; approval remains parent-owned.

## S1 — Operations
`A`: the coding agent autonomously chooses tools/actions. Confidence: high.

## S2 — Coordination
`C`: scheduler/sub-agent runtime provides composable coordination across agent work. Confidence: medium-high.

## S3 — Inside-and-now control
`C`: scheduler policy and confirmation machinery regulate current execution. Confidence: medium-high.

## S3* — Complementary audit
`—`: no independent complementary audit channel was established. Confidence: high.

## S4 — Outside-and-then intelligence
`—`: no prospective organizational adaptation function was established. Confidence: high.

## S5 — Policy and identity
`P`: approval mode/confirmation preserve parent authority. Confidence: high.

## Recursion, variety, escalation
Sub-agents amplify operational variety; scheduler/confirmation attenuate execution risk and provide escalation to the parent.

## Deep-review conclusion
Signature at the pinned revision: `A C C — — P`. The later pinned review establishes more metasystem closure than the earlier subagent-only assessment.
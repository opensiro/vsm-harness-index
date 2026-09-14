---
harness_id: mirothinker
project_name: MiroThinker
repository: https://github.com/MiroMindAI/MiroThinker
review_ref: 1c4253f6774bf40314271a827304b842100e054c
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: —
autonomy_s5: ?
---

# MiroThinker

## Review boundary
MiroThinker at the pinned revision as a deep-research/search agent and its open research harness, not the model-training organization.

## Repository architecture
MiroThinker performs long-horizon research with hundreds of tool/environment interactions, external information acquisition and stepwise trajectory refinement. Training/post-training improves the agent family across releases.

## Primary evidence
- `README.md`: deep research agent, long-chain tasks, high tool-call budgets, interactive agent-environment scaling, benchmark/evaluation and training descriptions.

## Operational model
The research agent is one S1 interacting extensively with the web/tool environment. Training infrastructure is outside the runtime organizational loop being assessed.

## S1 — Operations
`A`: the agent autonomously searches/tools/reasons toward research outcomes. Confidence: high.

## S2 — Coordination
`—`: no multi-S1 coordination function established.

## S3 — Inside-and-now control
`?`: no autonomous whole-system regulator verified.

## S3* — Complementary audit
`?`: step-verifiable research/evaluation does not establish independent runtime audit.

## S4 — Outside-and-then intelligence
`—`: environment feedback refines the current trajectory and offline/post-training improves future policies, but no distinct S4 function generates strategic adaptation options and couples them to S3. Training ≠ S4.

## S5 — Policy and identity
`?`: research objective/policy remains parent-supplied.

## Recursion, variety, escalation
Interactive scaling amplifies one S1's environmental variety; no recursion is established.
---
harness_id: stagehand
project_name: Stagehand
repository: https://github.com/browserbase/stagehand
review_ref: b771930d2b4d858e5bd9670203c66260b385a8fa
reviewed_at: 2026-09-15
status: included
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
last_checked_ref: d55f30ba0402b0b6932aa6b1ab7eca32c33c34be
last_checked_at: 2026-09-17
assessment_changed_at: 2026-09-15
last_reassessment_round: R2
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Stagehand

## Review boundary
Stagehand at the pinned revision as the browser-agent SDK and execution environment, not Browserbase as an organization. Repository-local benchmark/evaluation machinery is treated as an evaluation membrane unless it participates in the product harness's organizational closure.

## Repository architecture
Stagehand exposes agent-optimized browser observation/action/extraction, self-healing primitives, context reduction and autonomous goal execution through `agent().execute()`. At the R2 checked ref it also ships the `browse` CLI for external AI agents and a substantial `packages/evals` framework. The CLI exposes browser capabilities to a caller; the eval framework runs Stagehand and several external harnesses under a separate verifier/evidence pipeline.

## Primary evidence
- `packages/docs/v3/references/agent.mdx`: `AgentInstance.execute()` remains a current documented path for one autonomous browser agent with a high-level instruction, bounded steps, browser page, tool set, callbacks and cancellation.
- `packages/cli/README.md`: `browse` is explicitly a CLI for "any agent" to drive a browser; its persistent daemon/session machinery supplies browser state and tools rather than an autonomous organizational actor.
- `packages/evals/framework/benchHarness.ts`: the eval registry treats `stagehand` as one harness alongside Claude Code, Codex, Mastra, Pi and others; its verifier carrier is never initialized and never drives a browser, and the verifier selects its own model independently of the harness model.
- `packages/evals/framework/verifierAdapter.ts` and `packages/evals/docs/verifier-gates.md`: the verifier grades captured trajectories, applies deterministic evidence gates and persists review artifacts for benchmark outcomes.

## Operational model
A browser agent executing a goal is S1. Self-healing, callbacks, context reduction, action modes and execution limits all support or constrain that same operation. The new CLI is an access/tool surface for an external agent. The repository-local verifier is a benchmark/evaluation environment around product and external harness runs, not a product-runtime metasystem function at this system boundary.

## S1 — Operations
`A`: a standard browser agent autonomously chooses browser actions toward a goal. The current V3 reference still exposes `AgentInstance.execute()` with iterative browser-tool execution. Confidence: high.

## S2 — Coordination
`—`: no material first-party path regulates recurring interference or oscillation among multiple autonomous S1 units. Multiple CLI sessions and benchmark harness rows are independent execution/evaluation instances, not S2. Confidence: high.

## S3 — Inside-and-now control
`—`: max-step, abort, callback and execution controls regulate one S1 runtime rather than current commitments/resources across an organization. The eval runner controls benchmark execution from outside the product harness and does not establish product-runtime S3. Confidence: high.

## S3* — Complementary audit
`—`: the new verifier has genuine complementary-audit behavior for the **evaluation environment**: it independently grades captured trajectories, gates judge verdicts with evidence and records findings. But `benchHarness.ts` makes the boundary explicit: the verifier is a separate carrier/model and the eval framework compares multiple harnesses. Its findings determine benchmark result state, not corrective closure inside the live Stagehand browser-agent organization. Counting it as Stagehand product S3* would collapse the evaluation membrane into the system-in-focus. Confidence: high.

## S4 — Outside-and-then intelligence
`—`: self-healing reacts to changed pages during the current browser task; CLI skills and benchmark datasets improve access/evaluation capability but do not establish a distinct product-runtime prospective environment-to-S3 adaptation function. Confidence: high.

## S5 — Policy and identity
`—`: system prompts, tools, models, modes, execution policy and benchmark criteria remain parent/developer/evaluator configured. No first-party runtime closes ultimate policy or identity authority for the browser-agent organization. Confidence: high.

## Recursion, variety, escalation
Browser context, self-healing and the new CLI amplify operational variety. The eval/verifier stack is an external evaluation/growth membrane over Stagehand and other harnesses rather than a recursive viable subsystem of the Stagehand product harness.

## R2 result
Checked through `d55f30ba0402b0b6932aa6b1ab7eca32c33c34be`. The 16-commit delta materially expands CLI and evaluation infrastructure but does not change the assessed organizational vector: `A — — — — —`. Outcome: `no-material-change`; accepted `review_ref` remains unchanged.
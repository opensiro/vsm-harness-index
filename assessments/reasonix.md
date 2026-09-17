---
harness_id: reasonix
project_name: Reasonix
repository: https://github.com/esengine/DeepSeek-Reasonix
review_ref: ce278545461225dfd4c77840ad2a756bfb2095b9
reviewed_at: 2026-09-17
profile_version: 0.2.2
assessment_procedure_version: 0.3.1
assessment_changed_at: 2026-09-17
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Reasonix

## Review boundary
Pinned shared Reasonix coding-agent engine, including autonomous tool execution, planner/subagent profiles, workspace isolation, write-path claims, permissions/checkpoints and extension/tool surfaces. Terminal/desktop/browser/editor clients are presentation surfaces around the same engine.

Reviewed revision: `ce278545461225dfd4c77840ad2a756bfb2095b9`. Contract: Profile `0.2.2`, Methodology `0.3.1`.

## Primary evidence
- [`README.md`](https://github.com/esengine/DeepSeek-Reasonix/blob/ce278545461225dfd4c77840ad2a756bfb2095b9/README.md) — autonomous long-running coding-agent engine, plan mode, permissions, sandbox, checkpoints, MCP and client surfaces.
- [`docs/SUBAGENT_PROFILES.md`](https://github.com/esengine/DeepSeek-Reasonix/blob/ce278545461225dfd4c77840ad2a756bfb2095b9/docs/SUBAGENT_PROFILES.md) — isolated child agents, task/fleet execution and write-path claim semantics.
- [`docs/TOOL_CONTRACT.md`](https://github.com/esengine/DeepSeek-Reasonix/blob/ce278545461225dfd4c77840ad2a756bfb2095b9/docs/TOOL_CONTRACT.md) — task/fleet tool boundary and execution contracts.

## S1 — Operations
`A`. Reasonix owns an autonomous coding-agent loop that plans and executes tool actions against the workspace. Confidence: high.

## S2 — Coordination
`C`. Concurrent subagents use explicit write-path claims: disjoint claims can run concurrently, overlapping/omitted claims serialize, and whole-workspace or broader tool access escalates the claim. This directly attenuates concurrent workspace mutation collisions. The mechanism is runtime/constructor-owned rather than an autonomous S2 actor. Confidence: high.

## S3 — Inside-and-now control
`—`. Planner/executor composition, checkpoints and permission machinery structure current execution but do not establish a distinct first-party whole-system regulator owning shared organizational priorities/resources/commitments. Confidence: high.

## S3* — Complementary audit
`—`. Review/security labels and ordinary verification surfaces do not establish a materially independent audit actor with distinct evidence access and corrective closure. Confidence: high.

## S4 — Outside-and-then intelligence
`—`. No separate outside-looking prospective capability-adaptation loop was established. Confidence: high.

## S5 — Policy and identity
`—`. Permissions and workspace policy constrain actions but do not close organizational identity or ultimate-policy tension. Confidence: high.

## Recursion, variety, and escalation
Subagent profiles and fleet execution amplify operational variety; write claims serialize conflicting workspace access. Permission/checkpoint surfaces provide execution safety and recovery without establishing higher VSM closure.

## Admission conclusion
Canonical vector: `A C — — — —`.
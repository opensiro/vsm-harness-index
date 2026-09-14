---
harness_id: pi
project_name: Pi
repository: https://github.com/earendil-works/pi
review_ref: 71dca871bc80b6bc97be37f0ca3189399d651fff
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# Pi

## Review boundary
Pi agent harness at the pinned revision, focusing on `pi-agent-core`/coding-agent behavior. Chord and external pi-chat are distinct packages/systems unless directly participating in the agent loop.

## Repository architecture
Pi provides a self-extensible coding-agent CLI and core runtime with tool calling/state management, multi-provider models and external sandbox/container patterns. Telemetry and application-composition packages support the surrounding stack.

## Primary evidence
- `README.md`: agent runtime/tool/state packages, coding agent, permissions/containerization boundary and telemetry/application-composition package map.

## Operational model
The Pi coding agent is S1. Supporting Chord/telemetry/sandbox mechanisms do not establish separate autonomous metasystem functions.

## S1 — Operations
`A`: the coding agent owns bounded tool/action decisions. Confidence: high.

## S2 — Coordination
`—`: no material standard multi-S1 anti-oscillation relation is established.

## S3 — Inside-and-now control
`?`: runtime/state control is not autonomous whole-system regulation.

## S3* — Complementary audit
`?`: telemetry/conformance tests are engineering support, not runtime complementary audit.

## S4 — Outside-and-then intelligence
`?`: no prospective adaptation function verified.

## S5 — Policy and identity
`?`: security boundaries are externally configured; Pi explicitly relies on process/user permissions by default.

## Recursion, variety, escalation
Provider/tools/sandbox options amplify one S1; no recursion is established.
---
harness_id: browser-use
project_name: Browser Use
repository: https://github.com/browser-use/browser-use
review_ref: 50f205533fe10ba35b553d2a3689c77b87bd5d0a
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# Browser Use

## Review boundary
Browser Use at the pinned revision as the open-source browser-agent library, excluding hosted cloud organizational behavior.

## Repository architecture
A standard `Agent` receives a browser task/model and autonomously navigates, observes and acts until it produces a final result. Browser/cloud infrastructure supplies the environment.

## Primary evidence
- `README.md`: open-source Browser Use agent; explicit `Agent(... task=...)` followed by `agent.run()`; autonomous browser task examples.

## Operational model
One browser agent is S1. Browser infrastructure and retries support that operation.

## S1 — Operations
`A`: the agent autonomously selects browser actions toward the supplied task. Confidence: high.

## S2 — Coordination
`—`: no multi-S1 coordination function established.

## S3 — Inside-and-now control
`?`: run/browser management is not an autonomous whole-system regulator.

## S3* — Complementary audit
`?`: benchmark/recording infrastructure is not independent audit.

## S4 — Outside-and-then intelligence
`?`: browser observation is current-task sensing rather than prospective adaptation.

## S5 — Policy and identity
`?`: task/data policy remains parent supplied.

## Recursion, variety, escalation
Browser access amplifies one S1's environmental variety; no recursion is established.
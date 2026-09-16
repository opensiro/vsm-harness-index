---
harness_id: eigent
project_name: Eigent
repository: https://github.com/eigent-ai/eigent
review_ref: 6c49956b2aa878c08bee5edcf8a1eb63122c2cd9
reviewed_at: 2026-09-16
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: P
---

# Eigent

## Review boundary
The system-in-focus is Eigent's deployed multi-agent Workforce runtime: CAMEL-backed workers plus Eigent's decomposition, assignment, dependency, recovery, run-control, permission and human-interaction extensions. The human user is outside the autonomous organization and acts as parent authority.

## Repository architecture
`Workforce` extends CAMEL with coordinator/task agents, autonomous task decomposition, worker assignment, dependency-aware execution, task analysis, retry/replan failure handling and shared task channels. Eigent additionally inserts a permission-policy gate before tool dispatch; protected actions suspend execution until matching human approval is verified.

## Primary evidence
- [`backend/app/utils/workforce.py`](https://github.com/eigent-ai/eigent/blob/6c49956b2aa878c08bee5edcf8a1eb63122c2cd9/backend/app/utils/workforce.py#L115-L225): coordinator/task agents, workers, limits and autonomous retry/replan strategies.
- [`backend/app/utils/workforce.py`](https://github.com/eigent-ai/eigent/blob/6c49956b2aa878c08bee5edcf8a1eb63122c2cd9/backend/app/utils/workforce.py#L250-L400): autonomous task decomposition and dependency updates.
- [`backend/app/utils/workforce.py`](https://github.com/eigent-ai/eigent/blob/6c49956b2aa878c08bee5edcf8a1eb63122c2cd9/backend/app/utils/workforce.py#L520-L720): assignee selection, dependency checks and work publication.
- [`backend/app/permission_policy/runtime.py`](https://github.com/eigent-ai/eigent/blob/6c49956b2aa878c08bee5edcf8a1eb63122c2cd9/backend/app/permission_policy/runtime.py#L35-L205): executable deny/suspend/human-approval gate with action-digest verification.

## Operational model
A user supplies top-level purpose. Task/coordinator cognition decomposes it into an interdependent graph, chooses workers and dispatches ready work. Workers execute S1 tasks; Workforce state/failure analysis regulate execution including retry/replan. Protected tool actions pass through deterministic permission policy and may return authority to the human parent.

## S1 — Operations
`A`: worker agents receive subtasks and execute them through the Workforce task channel. Proof: [worker assignment/execution](https://github.com/eigent-ai/eigent/blob/6c49956b2aa878c08bee5edcf8a1eb63122c2cd9/backend/app/utils/workforce.py#L520-L720). Confidence: high.

## S2 — Coordination
`A`: task cognition generates dependencies and autonomous assignment carries/enforces them before work is released. Proof: [dependency construction](https://github.com/eigent-ai/eigent/blob/6c49956b2aa878c08bee5edcf8a1eb63122c2cd9/backend/app/utils/workforce.py#L250-L400), [dependency-aware release](https://github.com/eigent-ai/eigent/blob/6c49956b2aa878c08bee5edcf8a1eb63122c2cd9/backend/app/utils/workforce.py#L520-L720). Confidence: high.

## S3 — Inside-and-now control
`A`: coordinator/task agents allocate work, analyze outcomes and invoke autonomous retry/replan recovery. Proof: [failure analysis/recovery](https://github.com/eigent-ai/eigent/blob/6c49956b2aa878c08bee5edcf8a1eb63122c2cd9/backend/app/utils/workforce.py#L115-L245), [worker allocation](https://github.com/eigent-ai/eigent/blob/6c49956b2aa878c08bee5edcf8a1eb63122c2cd9/backend/app/utils/workforce.py#L520-L650). Confidence: high.

## S3* — Complementary audit
`—`: task analysis is part of ordinary Workforce S3 recovery rather than a structurally independent complementary audit channel. Proof: [task-analysis path](https://github.com/eigent-ai/eigent/blob/6c49956b2aa878c08bee5edcf8a1eb63122c2cd9/backend/app/utils/workforce.py#L180-L245). Confidence: high.

## S4 — Outside-and-then intelligence
`—`: decomposition/retry/replan operate on current tasks; no distinct prospective environment-facing adaptation process is closed. Proof: [current-task decomposition](https://github.com/eigent-ai/eigent/blob/6c49956b2aa878c08bee5edcf8a1eb63122c2cd9/backend/app/utils/workforce.py#L250-L400). Confidence: medium-high.

## S5 — Policy and identity
`P`: protected actions can create a durable approval request, suspend execution and require trusted human approval for the exact action before dispatch. Proof: [approval suspension](https://github.com/eigent-ai/eigent/blob/6c49956b2aa878c08bee5edcf8a1eb63122c2cd9/backend/app/permission_policy/runtime.py#L35-L155), [approval verification](https://github.com/eigent-ai/eigent/blob/6c49956b2aa878c08bee5edcf8a1eb63122c2cd9/backend/app/permission_policy/runtime.py#L155-L205). Confidence: high.

## Recursion, variety, escalation
Task decomposition/dependencies attenuate problem variety; worker pools distribute it; retry/replan absorbs recoverable failures. Protected actions cross a stronger boundary and escalate to the human parent. Agent hierarchy alone is not treated as recursive VSM closure.

## Deep-review conclusion
Signature at the pinned revision: `A A A — — P`. Eigent gives model-driven Workforce cognition executable ownership of decomposition, dependencies, worker allocation and failure replanning while retaining consequential policy authority with the parent.
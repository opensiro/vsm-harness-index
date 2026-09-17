---
harness_id: aionui
project_name: AionUi
repository: https://github.com/iOfficeAI/AionUi
review_ref: 6744099b279b991c17e31c243f0920477bd31cb6
reviewed_at: 2026-09-17
profile_version: 0.2.2
assessment_procedure_version: 0.3.1
assessment_changed_at: 2026-09-17
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# AionUi

## Review boundary
Pinned AionUi built-in agent and Team Mode runtime, including autonomous leader/teammate execution, Team MCP, persistent task/mailbox/run/slot state, dependency/ownership tracking and permission handling. Human approval is credited only where it establishes the relevant VSM function rather than ordinary execution permission.

Reviewed revision: `6744099b279b991c17e31c243f0920477bd31cb6`. Contract: Profile `0.2.2`, Methodology `0.3.1`.

## Primary evidence
- [`readme.md`](https://github.com/iOfficeAI/AionUi/blob/6744099b279b991c17e31c243f0920477bd31cb6/readme.md) — built-in autonomous agent plus Team Mode in which a Leader decomposes work, delegates to parallel Teammates, tracks progress and aggregates results.
- [`packages/desktop/src/common/types/team/teamTypes.ts`](https://github.com/iOfficeAI/AionUi/blob/6744099b279b991c17e31c243f0920477bd31cb6/packages/desktop/src/common/types/team/teamTypes.ts) — leader/teammate roles, per-slot queued/running/paused/blocked state, whole-run slot state, mailbox, and task ownership/dependency graph (`owner`, `blocked_by`, `blocks`).
- [`packages/desktop/src/common/adapter/ipcBridge.ts`](https://github.com/iOfficeAI/AionUi/blob/6744099b279b991c17e31c243f0920477bd31cb6/packages/desktop/src/common/adapter/ipcBridge.ts) — first-party Team control surface routed to the AionCore runtime.

## S1 — Operations
`A`. AionUi ships a built-in autonomous agent engine and Team Mode runs autonomous Leader/Teammate agents through supported backends. These agents perform the operational file/tool/task work rather than merely exposing constructor slots. Confidence: high.

## S2 — Coordination
`A`. Team Mode closes a concrete coordination loop across distinct S1s: tasks carry owners and explicit dependency/blocker relations; teammates execute in parallel; and the autonomous Leader decomposes and assigns work while the runtime exposes blocked/queued/running state that changes subsequent team behavior. This regulates duplicate, premature and mutually dependent work rather than merely transporting messages. Confidence: high.

## S3 — Inside-and-now control
`A`. The autonomous Leader has a whole-team current view and authority to assign, track and aggregate teammate work, while Team Mode exposes whole-run/per-slot state and dynamic member control. That establishes first-party agent-owned regulation over current team commitments and progress. Confidence: high.

## S3* — Complementary audit
`—`. Per-agent approvals, status and ordinary result aggregation are part of the normal execution/control path; no materially independent complementary audit channel with distinct evidence access and corrective closure was established. Confidence: high.

## S4 — Outside-and-then intelligence
`—`. External search/tools may support current tasks, but no distinct outside-looking prospective organizational adaptation loop was established. Confidence: high.

## S5 — Policy and identity
`—`. Human permission dialogs and deployment policy constrain actions, but routine execution approval is not an organizational identity or ultimate-policy tension-and-resolution loop. The historical `P` therefore does not survive the function-first S5 test. Confidence: high.

## Recursion, variety, and escalation
Parallel teammates, heterogeneous backends and dynamic scaling amplify operational variety. Task ownership/dependencies and Leader regulation attenuate coordination/current-control variety; per-agent permission and failure states provide operational escalation without establishing S5.

## Admission conclusion
Canonical vector: `A A A — — —`.

Same-ref correction of historical `A C C — — P`: the supplied Leader closes S2/S3 autonomously, while human permissions are ordinary parent execution control rather than S5 identity governance.
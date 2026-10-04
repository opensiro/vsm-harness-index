---
harness_id: wtsup-code
project_name: wtsup-code
repository: https://github.com/Shrit1401/wtsup-code
review_ref: abff97e3a6bce94cb7fc115d95f13e60acf650e1
reviewed_at: 2026-10-05
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-05
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# wtsup-code

## Review boundary

- System in focus: the first-party local harness at frozen revision `abff97e3a6bce94cb7fc115d95f13e60acf650e1`: browser-mediated Meta AI transport, prompt/tool protocol, parser/recovery, project-confined coding tools, approval handling and task loop.
- Purpose and identity: turn a consumer Meta AI WhatsApp conversation into a local coding agent by owning the tool protocol and execution feedback loop.
- Relevant environment: user task, project files/commands, Meta AI replies, browser/WhatsApp state, malformed protocol output, tool failures and approvals.
- Standard-distribution boundary: `src/harness.js`, `src/tools.js`, `src/waweb.js` and CLI/UI are inside. WhatsApp Web, Meta AI/model cognition, Playwright/Chromium and user approval are dependencies/parent inputs.
- Credited operating / distribution surfaces: interactive and one-shot CLI, persistent browser chat session, read/write/replace/ls/bash tools, malformed-response recovery and approval/`--yolo` modes.
- Adjacent first-party surfaces excluded from ownership: repository-development tests/CI and external Meta/WhatsApp behavior beyond the harness protocol.
- First-party operating / deployment modes considered: interactive task session and one-shot task execution.
- Recursion level: one coding task/session is the focal S1.
- Reviewed revision: `abff97e3a6bce94cb7fc115d95f13e60acf650e1`.
- Observation date: 2026-10-05.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

`createSession().run()` teaches Meta AI a JSON action protocol, parses each returned action, checks mutation preconditions, executes local tools and returns real output to the same conversation. Existing-file mutations require complete prior reads; dangerous shell/file actions are parent-confirmed unless `--yolo` is selected. Parser repair and bounded retries handle malformed consumer-chat output without inventing success.

Primary evidence:

- [README.md](https://github.com/Shrit1401/wtsup-code/blob/abff97e3a6bce94cb7fc115d95f13e60acf650e1/README.md)
- [harness loop](https://github.com/Shrit1401/wtsup-code/blob/abff97e3a6bce94cb7fc115d95f13e60acf650e1/src/harness.js)
- [tools](https://github.com/Shrit1401/wtsup-code/blob/abff97e3a6bce94cb7fc115d95f13e60acf650e1/src/tools.js)
- [WhatsApp transport](https://github.com/Shrit1401/wtsup-code/blob/abff97e3a6bce94cb7fc115d95f13e60acf650e1/src/waweb.js)

## Operational model

The external model chooses one or more coding actions; wtsup-code validates and executes them inside the selected project and returns results for the next model decision. The local harness, rather than Meta AI, owns tool availability, project containment, read-before-write enforcement, approvals, protocol recovery and termination bounds.

## S1 — Operations

- State: A
- Function: execute an open-ended coding task through iterative model-selected local actions and observed tool results.
- Disturbance / variety regulated: repository state, tool output/failure, malformed model protocol, browser transport changes and approval denials.
- Decisive decision or feedback right: select the next coding/tool action and revise work from real results.
- Decision owner: the model-backed coding actor instantiated by the first-party harness protocol.
- Supporting / enforcement mechanisms: JSON parser/repair, project-boundary checks, read-before-write state, confirmations, max turns and WhatsApp transport.
- Closure path: task → model action → harness validation/tool execution → output returned to model → next action/done.
- Boundary reachability: standard interactive and one-shot CLI modes instantiate this loop.
- Why this is / is not agent-owned: removing model-selected action choice leaves only transport and fixed tool enforcement.
- Evidence: `src/harness.js`; `src/tools.js`; README.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: model reasoning is provided by Meta AI, but the concrete tool feedback organization is first-party.

## S2 — Coordination

- State: —
- Function: no coordination among distinct same-recursion operational S1 units is established.
- Disturbance / variety regulated: one task uses one conversation/loop; tool batches remain actions of that same S1.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: single-session sequencing and single browser-profile exclusion.
- Closure path: no peer-S1 interference/attenuation/feedback loop exists.
- Why this is / is not agent-owned: serialization prevents concurrent session use but does not coordinate peer operations.
- Evidence: README; harness and WhatsApp transport.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: none material.

### Absence scope

- Surfaces inspected: task loop, batch execution, browser profile/session, tool executor and CLI modes.
- Plausible first-party paths checked: tool batch as multiple S1s; browser exclusivity as coordination; repeated tasks as peer operations.
- Why no material first-party path remains: all are one focal coding loop or support serialization.

## S3 — Inside-and-now control

- State: —
- Function: no whole-system current-control function is established.
- Disturbance / variety regulated: approvals, max turns and tool failures constrain one task.
- Decisive decision or feedback right: no portfolio-wide priority/resource/current-performance intervention right.
- Decision owner: not established.
- Supporting / enforcement mechanisms: confirmation gate, max-turn bound, protocol retries and batch stop-on-failure.
- Closure path: mechanisms constrain individual S1 execution only.
- Why this is / is not agent-owned: fixed guards and parent approvals are enforcement, not S3 management.
- Evidence: `src/harness.js`; `src/tools.js`.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: none material.

### Absence scope

- Surfaces inspected: approvals, task state, turn limits, batch failure and browser lifecycle.
- Plausible first-party paths checked: approval as S3; max turns as S3; task status as current control.
- Why no material first-party path remains: no whole-system S1 portfolio exists or is managed.

## S3* — Complementary audit

- State: —
- Function: no sufficiently independent complementary audit path is established.
- Disturbance / variety regulated: read-before-write and tool-result validation are ordinary S1 correctness controls.
- Decisive decision or feedback right: no independent reviewer verdict with corrective return.
- Decision owner: not established.
- Supporting / enforcement mechanisms: parser validation, project containment, read-before-write rule and tests outside runtime.
- Closure path: checks feed the same coding loop rather than an independent audit relation.
- Why this is / is not agent-owned: deterministic preconditions are not a separate auditor.
- Evidence: harness/tools; README.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: repository tests are adjacent development evidence.
- Claim being audited: no distinct producer claim.
- Ordinary reporting path: model/tool conversation.
- Complementary access path: none.
- Independence boundary: none at runtime.
- Who acts on findings: same S1 or parent user.

### Absence scope

- Surfaces inspected: parser recovery, mutation preconditions, tool failure handling and development tests.
- Plausible first-party paths checked: read-before-write as audit; tests as audit; parser validation as audit.
- Why no material first-party path remains: none supplies independent organizational challenge plus corrective return.

## S4 — Intelligence / adaptation

- State: —
- Function: no prospective external/future adaptation loop is established.
- Disturbance / variety regulated: chat context persists within a session and protocol repair reacts to malformed output.
- Decisive decision or feedback right: no durable capability adaptation decision.
- Decision owner: not established.
- Supporting / enforcement mechanisms: in-session context and bounded parser repair.
- Closure path: current-task recovery does not create future-facing adaptation.
- Why this is / is not agent-owned: the system learns no durable strategy/capability from external future evidence.
- Evidence: README; harness.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: none material.

### Absence scope

- Surfaces inspected: session persistence, parser recovery, configuration and development process.
- Plausible first-party paths checked: chat memory as S4; protocol recovery as adaptation.
- Why no material first-party path remains: both concern current-session operation.

## S5 — Policy and identity

- State: —
- Function: no identity/ultimate-policy closure is established.
- Disturbance / variety regulated: fixed safety rules and user approvals constrain actions.
- Decisive decision or feedback right: parent approval chooses specific risky effects, not system identity/policy.
- Decision owner: not established at S5 level.
- Supporting / enforcement mechanisms: project confinement, confirmations, `--yolo` and fixed system preamble.
- Closure path: standing constraints and action approvals apply directly without an identity-policy decision loop.
- Why this is / is not agent-owned: the agent does not own ultimate policy.
- Evidence: README; harness/tools.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: none material.

### Absence scope

- Surfaces inspected: safety model, approval path, system preamble and configuration.
- Plausible first-party paths checked: confirmations as S5; system prompt as policy; `--yolo` as identity mode.
- Why no material first-party path remains: these are operating constraints/modes, not S5 closure.

## Recursion

One coding session is the focal operational unit; tools and browser transport are support mechanisms.

## Variety and escalation

The harness attenuates malformed protocol, unsafe paths, unread-file mutation, failures and destructive actions. Risky actions escalate to the parent user unless `--yolo` is explicitly selected.

## Evidence gaps

No `?` state is required; the small frozen implementation provides direct evidence for the complete negative scopes.

## Assessment summary

wtsup-code closes autonomous S1 through a first-party model/tool protocol around Meta AI and local coding tools. Its safety, parsing and approval machinery constrain that one operation but do not establish S2, S3, independent S3*, prospective S4 or identity-level S5.

**Vector:** A · — · — · — · — · —

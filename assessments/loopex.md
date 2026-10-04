---
harness_id: loopex
project_name: Loopex
repository: https://github.com/lexlapax/loopex
review_ref: 3f81b04828901a6fb05b29e8b6bed211eed2d376
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

# Loopex

## Review boundary

- System in focus: Loopex's shipped OTP-native coding harness/runtime at frozen revision `3f81b04828901a6fb05b29e8b6bed211eed2d376`: durable model/tool sessions, journal/recovery, local executor, CLI/app-server/daemon protocols, governed context admission and host-policy boundary.
- Purpose and identity: run durable coding-agent sessions whose model receives real tool results while Loopex owns truthful effect execution, recovery and session continuity.
- Relevant environment: user/host prompt, repository workspace, model replies, tool outputs, crashes/restarts, context limits, executor state, daemon clients and host policy decisions.
- Standard-distribution boundary: first-party Loopex runtime, CLI, daemon, reference provider/executor/client components are inside. External model provider, OS boundary and embedding host governance remain dependencies/parent actors; repository-development CI/review is adjacent and excluded from runtime ownership.
- Credited operating / distribution surfaces: terminal coding sessions; durable session/runtime; local executor; app-server and daemon protocols; resume/replay; host-policy callbacks; governed project/skill context.
- Adjacent first-party surfaces excluded from ownership: repository milestone/CI/release organization, roadmap/future distributed capabilities, and any host application that embeds Loopex but is not itself part of the shipped focal runtime.
- First-party operating / deployment modes considered: direct CLI, app-server/reference-client, daemon-backed session, embedded runtime with host-supplied policy.
- Recursion level: one durable coding session is the focal S1 operation. Multiple clients, tool workers and executor processes are support machinery unless they independently satisfy VSM operational-unit criteria.
- Reviewed revision: `3f81b04828901a6fb05b29e8b6bed211eed2d376`.
- Observation date: 2026-10-05.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Loopex implements a provider-neutral multi-turn coding loop around durable OTP sessions. The session coordinator is the serial writer of model/effect truth: it stages model requests, commits attempt intent before dispatch, records model replies, resolves tool calls through host policy, commits effect intent, and feeds durable tool receipts back into the conversation. The local executor runs bounded coding effects against a workspace lease and records receipts; recovery replays committed journal truth rather than guessing whether an ambiguous effect succeeded.

The daemon keeps sessions alive beyond client attachment and uses controller leases so one client drives a session while other clients observe or explicitly take over. Those client/controller rules preserve session ownership and continuity. They do not create several peer coding S1s that mutually coordinate. Loopex also states the design boundary directly: “mechanism in Loopex, governance in the host.”

Primary evidence:

- [README.md](https://github.com/lexlapax/loopex/blob/3f81b04828901a6fb05b29e8b6bed211eed2d376/README.md)
- [agent loop and tools](https://github.com/lexlapax/loopex/blob/3f81b04828901a6fb05b29e8b6bed211eed2d376/docs/developer/agent-loop-and-tools.md)
- [daemon guide](https://github.com/lexlapax/loopex/blob/3f81b04828901a6fb05b29e8b6bed211eed2d376/docs/operator/daemon.md)
- [session coordinator](https://github.com/lexlapax/loopex/blob/3f81b04828901a6fb05b29e8b6bed211eed2d376/apps/loopex/lib/loopex/runtime/session_coordinator.ex)
- [local executor](https://github.com/lexlapax/loopex/blob/3f81b04828901a6fb05b29e8b6bed211eed2d376/apps/loopex_executor_local/lib/executor.ex)
- [workspace lease](https://github.com/lexlapax/loopex/blob/3f81b04828901a6fb05b29e8b6bed211eed2d376/apps/loopex_executor_local/lib/workspace_lease.ex)

## Operational model

A model-backed session receives a coding objective and admitted context, selects tools, and gets concrete executor receipts/results back into subsequent turns. Durable intent-before-effect and fact-before-publication ordering lets a successor process recover the operation without converting uncertainty into a false success. Host policy can allow, deny or ask about a tool call; that policy constrains S1 but remains host-owned rather than becoming Loopex-owned metasystem authority.

## S1 — Operations

- State: A
- Function: perform coding work through a durable model/tool feedback loop.
- Disturbance / variety regulated: repository state, model responses, tool failures, crash/restart ambiguity, context pressure, deadlines and host-policy results.
- Decisive decision or feedback right: choose the next coding/tool action and revise work from returned evidence until task completion.
- Decision owner: the model-backed Loopex coding actor operating through the session coordinator.
- Supporting / enforcement mechanisms: journal, session coordinator, context admission, local executor, workspace lease/fencing, receipts, provider boundary, bounds and daemon transport.
- Closure path: objective/context → model action/tool call → policy/admission → executed effect and durable receipt → tool result enters conversation → model chooses the next action.
- Boundary reachability: the shipped CLI/app-server/embedded runtime instantiates this loop directly at the frozen revision.
- Why this is / is not agent-owned: removing the model actor leaves durable transport/enforcement but removes open-ended coding decisions.
- Evidence: README; agent-loop documentation; session coordinator; executor.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: provider inference is external, but the agent/tool organizational loop is first-party.

## S2 — Coordination

- State: —
- Function: no material same-recursion coordination function among distinct operational S1 units was established.
- Disturbance / variety regulated: client leases, serialized session ownership and executor root/workspace claims prevent ambiguous control/effect ownership, but regulate support machinery around individual sessions rather than peer coding S1s.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: one serial owner per session, controller lease/takeover, workspace leases, fencing tokens, executor serialization and durable receipts.
- Closure path: no peer-S1 interference → coordination response → changed peer behavior loop was established.
- Why this is / is not agent-owned: locks/leases deterministically constrain transport/effects and do not select mutual adjustment between autonomous operational units.
- Evidence: README; daemon guide; workspace lease; executor.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: future remote-worker/fleet possibilities and multiple client attachments are not current S2 evidence.

### Absence scope

- Surfaces inspected: daemon/controller lease, runtime/session ownership, executor/workspace claims, concurrent clients, coding loop and documented future distribution.
- Plausible first-party paths checked: controller takeover as S2; executor serialization as S2; multiple sessions as peer S1s; remote “brains and hands”.
- Why no material first-party path remains: mechanisms maintain authority/effect truth for sessions/jobs; no inter-S1 operational conflict is detected, attenuated and returned to peer behavior.

## S3 — Inside-and-now control

- State: —
- Function: no whole-system current-control function over a portfolio of operational S1 units was established.
- Disturbance / variety regulated: daemon/session status, stop/drain, deadlines, resource/context bounds and recovery regulate individual sessions/runtime integrity.
- Decisive decision or feedback right: no whole-current priority/resource/accountability intervention right is implemented by Loopex itself.
- Decision owner: not established.
- Supporting / enforcement mechanisms: daemon session index, lifecycle commands, runtime bounds, quiesce/drain, telemetry, host-policy callbacks.
- Closure path: mechanisms can observe/stop/recover sessions, but no first-party whole-system managerial decision loop is closed.
- Why this is / is not agent-owned: lifecycle control and host-owned policy remain support/parent mechanisms rather than S3 decision ownership.
- Evidence: README; daemon/runtime docs.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: an embedding host may build S3 over Loopex, but “governance in the host” places it outside this boundary.

### Absence scope

- Surfaces inspected: daemon-wide session ownership, status/list/stop/drain, controller leases, telemetry, bounds and host policy.
- Plausible first-party paths checked: daemon as manager; controller lease as current control; runtime bounds as resource bargaining; observability as S3.
- Why no material first-party path remains: surfaces enforce session/run integrity and expose state without deciding whole-system priorities or interventions.

## S3* — Complementary audit

- State: —
- Function: no closed complementary audit relation over runtime operational claims was established.
- Disturbance / variety regulated: receipts, reconciliation and verification establish truthful execution state; they are ordinary execution/recovery evidence rather than independent organizational audit.
- Decisive decision or feedback right: not established at S3* level.
- Decision owner: not established.
- Supporting / enforcement mechanisms: executor receipts, journal replay, reconciliation, diagnostics/telemetry and repository-development verification.
- Closure path: runtime evidence returns into ordinary S1 recovery; repository independent review is adjacent development governance.
- Why this is / is not agent-owned: proof/reconciliation validates effects but does not create a sufficiently independent auditor with corrective authority.
- Evidence: README; executor/session ordering; verification documentation.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: hosts may compose independent auditing around the runtime.
- Claim being audited: no distinct first-party runtime producer claim/auditor relation established.
- Ordinary reporting path: session journal/events/receipts.
- Complementary access path: none distinct from ordinary runtime evidence at the assessed boundary.
- Independence boundary: repository CI/review is excluded as adjacent development organization.
- Who acts on findings: ordinary session/runtime recovery or external host/operator.

### Absence scope

- Surfaces inspected: receipts, reconciliation, event/trace planes, tests/release checks, independent development review.
- Plausible first-party paths checked: receipts as S3*; reconciliation as S3*; telemetry as S3*; repository independent review as runtime audit.
- Why no material first-party path remains: runtime checks are in-band execution truth/recovery, while independent development review is outside deployed Loopex.

## S4 — Intelligence / adaptation

- State: —
- Function: no externally and prospectively oriented adaptation loop was established.
- Disturbance / variety regulated: context admission and live-extension machinery can accept host-supplied project/skill/code changes while sessions persist.
- Decisive decision or feedback right: no first-party path senses external/future change, develops adaptation options and selects one into present capability.
- Decision owner: not established.
- Supporting / enforcement mechanisms: project/skill context admission, extension generations, migration/rollback machinery, roadmap/development process.
- Closure path: host-supplied changes can be admitted/rolled back, but Loopex does not own the prospective adaptation decision.
- Why this is / is not agent-owned: admission/rollback enforce externally chosen changes rather than choose strategy.
- Evidence: README; context-admission documentation; vision/roadmap distinction.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: repository development evolution is adjacent and excluded.

### Absence scope

- Surfaces inspected: context/resource admission, skill admission, live extension claims, roadmap, runtime migration/rollback.
- Plausible first-party paths checked: live code evolution as S4; skills/project instructions as adaptation; roadmap as S4.
- Why no material first-party path remains: no deployed environmental/prospective sensing-and-option loop is wired to current capability.

## S5 — Policy and identity

- State: —
- Function: no first-party identity/ultimate-policy closure was established.
- Disturbance / variety regulated: host policy may permit/refuse/ask on tool calls and controls trusted context admission.
- Decisive decision or feedback right: ordinary action permission belongs to the host/operator; no identity-level decision path closes inside Loopex.
- Decision owner: not established at S5 level.
- Supporting / enforcement mechanisms: Policy boundary, context-admission decisions, provenance classes and fixed runtime invariants.
- Closure path: host decisions constrain later effects, but no identity/ultimate-policy issue → legitimate authority decision → returned governance path is established.
- Why this is / is not agent-owned: Loopex explicitly separates mechanism from host governance.
- Evidence: README; host policy and context-admission surfaces.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: a larger host can own S5 without transferring it to Loopex.

### Absence scope

- Surfaces inspected: host-policy callbacks, context trust/admission, runtime invariants, daemon authority and project governance docs.
- Plausible first-party paths checked: allow/refuse/ask policy as S5; trusted context admission as S5; architectural invariants as identity policy.
- Why no material first-party path remains: these are action/context constraints and developer design rules, not runtime identity/ultimate-policy closure.

## Recursion

A durable coding session is the focal S1. Tool workers, provider companion processes, daemon clients and executor processes are supporting actors; nesting/supervision does not establish recursive viability.

## Variety and escalation

Loopex absorbs task/effect variety with journal truth, replay, bounded context, receipts, fencing, reconciliation and host-policy questions. Governance variety is intentionally escalated to the host; this evidences the boundary rather than an internal higher VSM function.

## Evidence gaps

No `?` state is required. Frozen implementation/documentation directly establishes S1 and bounds the negative findings for S2–S5.

## Assessment summary

Loopex closes autonomous S1 through an OTP-native durable model/tool session. Leases, fencing, receipts, reconciliation, daemon lifecycle and governed context protect execution truth/composability, but governance is left to the host; no first-party S2, whole-current S3, complementary S3*, prospective S4 or identity-level S5 closure is established.

**Vector:** A · — · — · — · — · —

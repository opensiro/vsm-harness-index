---
harness_id: grinta
project_name: Grinta
repository: https://github.com/josephsenior/Grinta-Coding-Agent
review_ref: 98112110dc30e983f22982a9891aadd18fdfb189
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

# Grinta

## Review boundary

- System in focus: Grinta's first-party local coding-agent runtime at frozen revision `98112110dc30e983f22982a9891aadd18fdfb189`: session orchestrator, model/tool loop, execution middleware, read-only delegate workers, recovery/stuck/circuit-breaker machinery, durable events and checkpoints.
- Purpose and identity: autonomously plan, edit, execute, debug and validate software tasks while keeping execution/control state local.
- Relevant environment: user task, repository/workspace, tool observations, tests/diagnostics, provider errors, context/budget pressure, durable session state and parent confirmation.
- Standard-distribution boundary: Grinta runtime, CLI/TUI, orchestration/execution/durability layers and shipped delegate workers are inside. Model providers, MCP servers, OS/container boundary and parent user are dependencies/actors. Repository-development CI and benchmark verifier are adjacent.
- Credited operating / distribution surfaces: Agent mode and non-interactive execution, local tools, task tracking, recovery/retry/stuck handling, checkpoints/restore, advisory completion validation and bounded read-only delegation.
- Adjacent first-party surfaces excluded from ownership: development/release process, external benchmark verifier and provider-owned cognition.
- First-party operating / deployment modes considered: interactive Agent mode and non-interactive/headless execution; conservative/balanced/full confirmation modes alter approvals, not VSM function identity.
- Recursion level: one Grinta coding session/task is the focal S1; read-only delegated investigations are subordinate workers within that operation rather than independently viable same-recursion S1 units.
- Reviewed revision: `98112110dc30e983f22982a9891aadd18fdfb189`.
- Observation date: 2026-10-05.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Grinta's `SessionOrchestrator` drives a model-backed action loop through safety, cost/context, rollback, diagnostics and tool-result middleware. Recovery services handle retries, circuit breaking, stuck detection and pending-action failure. Durable events/checkpoints support resume and rollback.

The `delegate_task` tool can fan out bounded read-only investigations and return their conclusions to the parent agent. Those workers cannot edit the workspace or recursively delegate, and the parent remains the operation that applies changes. Parallel action scheduling also handles execution concurrency/resource conflicts inside one model turn.

The optional completion validator is explicitly advisory: a failed verdict emits a warning but does not block transition to `FINISHED`. Therefore it is not a decisive complementary-audit closure.

Primary evidence:

- [README.md](https://github.com/josephsenior/Grinta-Coding-Agent/blob/98112110dc30e983f22982a9891aadd18fdfb189/README.md)
- [architecture](https://github.com/josephsenior/Grinta-Coding-Agent/blob/98112110dc30e983f22982a9891aadd18fdfb189/docs/ARCHITECTURE.md)
- [reliability](https://github.com/josephsenior/Grinta-Coding-Agent/blob/98112110dc30e983f22982a9891aadd18fdfb189/docs/RELIABILITY.md)
- [session orchestrator](https://github.com/josephsenior/Grinta-Coding-Agent/blob/98112110dc30e983f22982a9891aadd18fdfb189/backend/orchestration/session_orchestrator.py)
- [delegate task](https://github.com/josephsenior/Grinta-Coding-Agent/blob/98112110dc30e983f22982a9891aadd18fdfb189/backend/engine/tools/delegate_task.py)
- [completion validator](https://github.com/josephsenior/Grinta-Coding-Agent/blob/98112110dc30e983f22982a9891aadd18fdfb189/backend/orchestration/services/task_validation_service.py)
- [parallel scheduler](https://github.com/josephsenior/Grinta-Coding-Agent/blob/98112110dc30e983f22982a9891aadd18fdfb189/backend/orchestration/action_scheduler.py)

## Operational model

The focal agent repeatedly plans/acts, executes through local tools, receives observations and repairs/continues until it produces a final response. Reliability controls shape that same loop. Read-only delegates provide bounded investigation evidence to the parent; completion-quality validation can warn the same transcript but cannot veto completion.

## S1 — Operations

- State: A
- Function: perform end-to-end repository coding work through a model/tool feedback loop.
- Disturbance / variety regulated: repository complexity, failing tests/commands, provider failures, context pressure, repeated/stuck actions, crashes and parent confirmation requirements.
- Decisive decision or feedback right: choose investigative/edit/execution actions, revise from observations, recover and decide when the coding task is complete.
- Decision owner: the model-backed Grinta agent inside the session orchestrator.
- Supporting / enforcement mechanisms: middleware pipeline, local execution, task tracking, retries/circuit breakers, checkpoints, event ledger, context/budget controls and delegate workers.
- Closure path: task/state → model action → policy/execution → observation/evidence → next model decision/recovery → final response.
- Boundary reachability: normal Agent/headless modes directly instantiate the loop.
- Why this is / is not agent-owned: without the model actor, middleware and recovery machinery enforce/transport actions but do not choose open-ended coding work.
- Evidence: README; SessionOrchestrator; architecture/reliability docs.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: some risky actions remain parent-confirmed depending on configured autonomy level.

## S2 — Coordination

- State: —
- Function: no material coordination among distinct same-recursion viable S1 units was established.
- Disturbance / variety regulated: delegate workers investigate separate questions; the action scheduler prevents unsafe concurrent resource use.
- Decisive decision or feedback right: no peer-S1 mutual-adjustment right is established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: parent delegation, worker limits/timeouts, parallel batch conflict detection and pending-action tracking.
- Closure path: subordinate worker findings return to the parent S1; resource-conflict scheduling regulates tool actions, not interference among independent operational units.
- Why this is / is not agent-owned: delegated workers are read-only, one level deep, non-recursive, and cannot close the product's coding operation independently.
- Evidence: `delegate_task.py`; `action_scheduler.py`; SessionOrchestrator.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: worker plurality alone does not satisfy S2.

### Absence scope

- Surfaces inspected: delegate_task, parallel action scheduler, pending-action lifecycle, session orchestration and documented Agent modes.
- Plausible first-party paths checked: parallel delegates as peer S1s; resource-conflict scheduling as S2; concurrent tool actions as S1 plurality.
- Why no material first-party path remains: these are subordinate investigation/tool-execution mechanisms under one focal Grinta operation, with no distinct viable peer operations whose conflicts are mutually regulated.

## S3 — Inside-and-now control

- State: —
- Function: no whole-system current-control function over multiple viable S1 operations was established.
- Disturbance / variety regulated: budgets, iteration limits, retries, stuck detection, pending actions and current-task lifecycle.
- Decisive decision or feedback right: no whole-current portfolio priority/resource/accountability intervention exists.
- Decision owner: not established.
- Supporting / enforcement mechanisms: SessionOrchestrator, autonomy/safety services, circuit breaker, rate governor, task tracker and lifecycle state machine.
- Closure path: controls constrain/recover one focal S1 execution rather than manage a population of S1 operations.
- Why this is / is not agent-owned: orchestration is current-loop control machinery, not a distinct whole-system managerial function.
- Evidence: architecture; SessionOrchestrator; reliability.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: user approval is parent authority for specific effects, not S3.

### Absence scope

- Surfaces inspected: orchestration services, lifecycle states, budgets, rate governor, autonomy controls, task tracking, delegation and parallel execution.
- Plausible first-party paths checked: SessionOrchestrator as S3; budget/rate controls as resource management; task tracker as whole-current view.
- Why no material first-party path remains: all inspected paths are internal controls for a single coding operation rather than current-control decisions across viable S1 units.

## S3* — Complementary audit

- State: —
- Function: no decisive independent complementary audit closure was established.
- Disturbance / variety regulated: task validation, auto-check, diagnostics and grounding gates can surface correctness evidence during the coding loop.
- Decisive decision or feedback right: the optional LLM completion validator cannot veto `FINISHED`; its negative verdict is warning-only.
- Decision owner: not established at S3* level.
- Supporting / enforcement mechanisms: TaskValidationService, Test/Diff/File validators, AutoCheck, diagnostics, grounding read/check after failure.
- Closure path: validation evidence feeds the same S1 or emits an advisory warning; no independent audit verdict owns corrective return and re-verification.
- Why this is / is not agent-owned: the implementation explicitly preserves the agent's final-response decision instead of granting validator closure authority.
- Evidence: `task_validation_service.py`; architecture; reliability.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: external benchmark verifiers are outside the first-party runtime boundary.
- Claim being audited: coding-task completion/correctness.
- Ordinary reporting path: agent event stream and final response.
- Complementary access path: optional validator/tests/diagnostics read task/state/workspace evidence.
- Independence boundary: validator may use a separate judgment path, but it has no decisive corrective authority.
- Who acts on findings: the same operational transcript/agent or parent user; negative completion-validator findings are warning-only.

### Absence scope

- Surfaces inspected: TaskValidationService, validator wiring, AutoCheck/diagnostics, grounding gates, benchmark adapter/verifier boundary.
- Plausible first-party paths checked: LLM completion validator as S3*; test/diagnostic middleware as audit; external benchmark verifier as audit.
- Why no material first-party path remains: first-party validator is advisory/in-band and external benchmark authority is outside the system-in-focus.

## S4 — Intelligence / adaptation

- State: —
- Function: no externally and prospectively oriented adaptation loop was established.
- Disturbance / variety regulated: session memory/context, checkpoints, recovery and provider/model selection support current/future runs operationally.
- Decisive decision or feedback right: no first-party mechanism senses environmental futures, develops strategic options and selects capability adaptation.
- Decision owner: not established.
- Supporting / enforcement mechanisms: durable event history, compaction/memory, checkpoints, configurable providers/models and recovery.
- Closure path: retained history/configuration changes affect operation but do not close an outside-and-then adaptation relation.
- Why this is / is not agent-owned: learning/recovery from current failures remains S1 support unless prospective environment/capability adaptation is established.
- Evidence: README; reliability; architecture.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: repository roadmap/development is adjacent.

### Absence scope

- Surfaces inspected: memory/context, checkpoints, provider/model configuration, recovery, evidence/case studies and roadmap.
- Plausible first-party paths checked: durable history as learning; failure recovery as adaptation; model switching as strategy adaptation.
- Why no material first-party path remains: inspected mechanisms handle current-task execution/reuse rather than prospective external adaptation.

## S5 — Policy and identity

- State: —
- Function: no identity/ultimate-policy closure was established.
- Disturbance / variety regulated: autonomy levels, safety policy, workspace boundaries and parent confirmations constrain actions.
- Decisive decision or feedback right: no qualifying identity-level matter is decided by an ultimate first-party authority and returned to operations.
- Decision owner: not established at S5 level.
- Supporting / enforcement mechanisms: AutonomyController, SafetyValidator, confirmation service, execution profiles and configuration.
- Closure path: standing rules/configuration and per-action approvals directly constrain S1.
- Why this is / is not agent-owned: full autonomy removes prompts but does not give the agent authority over Grinta's identity or ultimate policy.
- Evidence: README; AutonomyService; architecture/reliability.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: parent user retains configurable approval rights.

### Absence scope

- Surfaces inspected: autonomy modes, safety middleware, confirmation service, configuration/execution profiles and user authority.
- Plausible first-party paths checked: autonomy level as S5; safety rules as ultimate policy; confirmations as governance.
- Why no material first-party path remains: these are operational constraints/approvals, not an identity-policy proposal/decision/return loop.

## Recursion

The focal viable operation is one coding task/session. Read-only delegated workers are subordinate investigation actors, and parallel tool actions are mechanisms inside that operation.

## Variety and escalation

Grinta absorbs failures through retries, circuit breakers, stuck detection, grounding, durable events/checkpoints and model-visible recovery prompts. Risky actions may escalate to the parent user according to autonomy mode.

## Evidence gaps

No `?` state is required. The frozen implementation is broad and explicit enough to establish S1 and complete the negative scopes.

## Assessment summary

Grinta closes autonomous S1 with a durable recovery-oriented coding loop. Its worker delegation, parallel scheduling, completion validation and safety/control services remain subordinate/in-band mechanisms for that operation: they do not establish same-recursion S2, whole-current S3, decisive independent S3*, prospective S4 or identity-level S5.

**Vector:** A · — · — · — · — · —

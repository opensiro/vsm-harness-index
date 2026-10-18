---
harness_id: openclaw-dotnet
project_name: OpenClaw.NET
repository: https://github.com/clawdotnet/openclaw.net
review_ref: a5d1b7ee689967baf4097c5bf8b578f00e2da87e
reviewed_at: 2026-09-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-30
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# OpenClaw.NET

## Review boundary

- System in focus: the shipped OpenClaw.NET self-hosted agent runtime and gateway at frozen revision `a5d1b7ee689967baf4097c5bf8b578f00e2da87e`, including its model-backed agent loop, first-party tools, sessions/memory, delegation, gateway runtime services, Plan-Execute-Verify path, runtime pulse and review-first learning surfaces when reachable from supported deployment modes.
- Purpose and identity: run a self-hosted assistant/agent over configured model providers, tools, memory, channels and APIs, with optional delegated sub-agents and durable runtime/governance support.
- Relevant environment: operator requests; configured model providers; local files and processes; enabled tools and external services; channel/API messages; session/memory state; delegated child-agent work; runtime failures; configured security, approval and execution constraints.
- Standard-distribution boundary: first-party OpenClaw.NET runtime, Gateway/CLI/Companion surfaces and first-party tool/runtime services are inside. External model-provider internals, external services reached by tools, third-party plugins, MCP servers and channel-provider internals remain dependencies and are not credited with OpenClaw.NET organizational functions.
- Credited operating / distribution surfaces: `README.md`; `src/OpenClaw.Agent/AgentRuntime.cs`; `src/OpenClaw.Agent/Tools/DelegateTool.cs`; `src/OpenClaw.Core/Sessions/SessionManager.cs`; `src/OpenClaw.Gateway/SharedHarnessStateService.cs`; `src/OpenClaw.Gateway/PlanExecuteVerifyService.cs`; `src/OpenClaw.Agent/AuditLogHook.cs`; `docs/PULSE.md`; `docs/LEARNING.md`.
- Adjacent first-party surfaces excluded from ownership: repository-development governance and contributor review; tests/CI/release machinery; documentation-only proposals; sample-only durable-agent review workflows; maintainer review checklists; other example/evaluation surfaces not wired into the supported runtime mode.
- First-party operating / deployment modes considered: local/self-hosted Gateway; Companion/browser/CLI/API access; configured model-backed agent runtime; optional `delegate_agent`; optional Plan-Execute-Verify; Runtime Pulse; review-first Learning Proposals; ordinary operator approval surfaces.
- Recursion level: one deployed OpenClaw.NET runtime as the system in focus. A model-backed agent session is the primary S1 operational unit. Delegated child sessions are inspected as additional candidate S1 units, but their existence alone is not treated as S2/S3 or recursive viability.
- Reviewed revision: `a5d1b7ee689967baf4097c5bf8b578f00e2da87e`.
- Observation date: 2026-09-30.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

OpenClaw.NET ships a provider-agnostic model-backed `AgentRuntime` whose ordinary turn loop builds context from session/memory state, calls the configured model, executes first-party or configured tools, feeds tool results back to the model and continues until completion or a runtime limit. The shipped Gateway/CLI/Companion expose that loop as a self-hosted assistant/agent runtime rather than as a library-only construction kit.

The runtime also has explicit multi-agent delegation. `DelegateTool` lets the current model-backed agent select a named profile and task, constructs a restricted tool set, starts another `AgentRuntime` in a persisted child session, returns the child response to the parent and stores delegation metadata/tool-use summaries. This establishes additional agentic work units, but the Profile explicitly requires more than delegation or plurality to establish S2 or S3.

Several first-party control and evidence surfaces are substantial but remain narrower than positive VSM mappings at this frozen ref. `SessionManager` serializes admission/persistence for a session and bounds concurrent sessions. `SharedHarnessStateService` can represent participants/actions and detect write/write, versioned read/write, assumption and verifier-obligation conflicts. Its detected conflicts carry `warn`/`escalate` policies and recommendations, but the inspected implementation persists and exposes those findings; no standard first-party closure was found that applies a coordination result back to the affected S1 work units. `PlanExecuteVerifyService` creates contracts/evidence and runs deterministic tool-outcome, approval, contract, security and regression checks around configured tool execution. `AuditLogHook` records tool invocation/completion but explicitly always permits execution.

Runtime Pulse is a scheduled agent turn for checking lightweight runtime context and surfacing operator-visible alerts or reviewable suggestions. Learning Proposals turn repeated operator behaviour into pending profile/skill/automation/harness suggestions, but durable changes remain operator-review-first. These mechanisms were inspected for S3/S4/S5 closure; at the reviewed boundary they do not establish a whole-system current regulator, an externally prospective adaptation loop returning through S3, or identity/ultimate-policy closure.

Primary evidence:

- [`README.md`](https://github.com/clawdotnet/openclaw.net/blob/a5d1b7ee689967baf4097c5bf8b578f00e2da87e/README.md)
- [`src/OpenClaw.Agent/AgentRuntime.cs`](https://github.com/clawdotnet/openclaw.net/blob/a5d1b7ee689967baf4097c5bf8b578f00e2da87e/src/OpenClaw.Agent/AgentRuntime.cs)
- [`src/OpenClaw.Agent/Tools/DelegateTool.cs`](https://github.com/clawdotnet/openclaw.net/blob/a5d1b7ee689967baf4097c5bf8b578f00e2da87e/src/OpenClaw.Agent/Tools/DelegateTool.cs)
- [`src/OpenClaw.Core/Sessions/SessionManager.cs`](https://github.com/clawdotnet/openclaw.net/blob/a5d1b7ee689967baf4097c5bf8b578f00e2da87e/src/OpenClaw.Core/Sessions/SessionManager.cs)
- [`src/OpenClaw.Gateway/SharedHarnessStateService.cs`](https://github.com/clawdotnet/openclaw.net/blob/a5d1b7ee689967baf4097c5bf8b578f00e2da87e/src/OpenClaw.Gateway/SharedHarnessStateService.cs)
- [`src/OpenClaw.Gateway/PlanExecuteVerifyService.cs`](https://github.com/clawdotnet/openclaw.net/blob/a5d1b7ee689967baf4097c5bf8b578f00e2da87e/src/OpenClaw.Gateway/PlanExecuteVerifyService.cs)
- [`src/OpenClaw.Agent/AuditLogHook.cs`](https://github.com/clawdotnet/openclaw.net/blob/a5d1b7ee689967baf4097c5bf8b578f00e2da87e/src/OpenClaw.Agent/AuditLogHook.cs)
- [`docs/PULSE.md`](https://github.com/clawdotnet/openclaw.net/blob/a5d1b7ee689967baf4097c5bf8b578f00e2da87e/docs/PULSE.md)
- [`docs/LEARNING.md`](https://github.com/clawdotnet/openclaw.net/blob/a5d1b7ee689967baf4097c5bf8b578f00e2da87e/docs/LEARNING.md)

## Operational model

A standard OpenClaw.NET deployment binds one or more sessions to a configured model provider and a first-party tool registry. On each turn the model observes prompt/session/memory context, chooses whether and how to use available tools, receives observations and revises its next action. Tool approvals, budgets, circuit breakers, session persistence and optional PEV constrain or verify that work but do not own its open-ended task decisions.

With delegation enabled, an S1 agent may create a child agent session with a selected profile/task/tool subset. The parent receives the child's result and can continue its own turn. This is genuine agentic task delegation, but no material first-party mechanism was found that both regulates a specific interference among distinct S1 units and closes that coordination result into later S1 behaviour. Likewise, no actor was found with the whole-system current view plus resource/commitment authority required for S3.

## S1 — Operations

- State: A
- Function: perform open-ended user-directed work through model reasoning, tool selection/execution and iterative use of returned observations.
- Disturbance / variety regulated: changing user requests, session and memory context, tool outputs/failures, local/external resource state exposed through enabled tools, and intermediate evidence encountered while completing a task.
- Decisive decision or feedback right: choose the next task-specific response or tool action and revise subsequent action from returned tool/model context.
- Decision owner: the configured model-backed OpenClaw.NET agent session.
- Supporting / enforcement mechanisms: `AgentRuntime`; session history and memory; tool registry/executor; retries/circuit breaker; token/runtime limits; approval policy; checkpoints; optional goals/background continuation; Gateway/CLI/Companion transport.
- Closure path: operator/message objective + current context → model selects response/tool call → first-party executor runs the call → observation returns to the same model-backed turn loop → the agent revises its next action or completes the task.
- Boundary reachability: `README.md` documents the self-hosted Gateway/Companion/CLI path with configured hosted or local models, and `AgentRuntime` directly implements the shipped model/tool feedback loop; no user-authored orchestration layer is required for this operational path.
- Why this is / is not agent-owned: removing model decision-making while keeping sessions, queues, memory, approval and tool plumbing removes the open-ended task choice. The model-backed session therefore owns the S1 operational discretion even though deterministic runtime machinery executes and constrains its choices.
- Evidence: [`README.md`](https://github.com/clawdotnet/openclaw.net/blob/a5d1b7ee689967baf4097c5bf8b578f00e2da87e/README.md); [`AgentRuntime.cs`](https://github.com/clawdotnet/openclaw.net/blob/a5d1b7ee689967baf4097c5bf8b578f00e2da87e/src/OpenClaw.Agent/AgentRuntime.cs); [`DelegateTool.cs`](https://github.com/clawdotnet/openclaw.net/blob/a5d1b7ee689967baf4097c5bf8b578f00e2da87e/src/OpenClaw.Agent/Tools/DelegateTool.cs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: a spawned/delegated child is not automatically a recursively viable system; this assessment credits the concrete model-backed operational loop, not every helper process or tool call.

## S2 — Coordination

- State: —
- Function: no closed S2 function established at the declared boundary.
- Disturbance / variety regulated: candidate inter-S1 conflicts include concurrent writes, versioned read/write dependencies and contradictory assumptions represented in shared harness state.
- Decisive decision or feedback right: no material first-party right was found that takes a detected inter-S1 conflict and closes a coordination response into subsequent behaviour of the affected S1 units.
- Decision owner: not established.
- Supporting / enforcement mechanisms: `SessionManager` locks/admission; `SharedHarnessStateService` conflict detection; delegation depth/tool subsets; ordinary tool-call ordering and runtime concurrency controls.
- Closure path: not established for inter-S1 coordination. Shared harness conflict detection persists `warn`/`escalate` recommendations, but no standard consumer was found that applies them as a mutual-adjustment or isolation decision to the implicated agent work units.
- Why this is / is not agent-owned: the repository contains real collision representations, but detection, generic locking and delegation do not satisfy the Profile without a feedback path that changes later S1 behaviour.
- Evidence: [`SharedHarnessStateService.cs`](https://github.com/clawdotnet/openclaw.net/blob/a5d1b7ee689967baf4097c5bf8b578f00e2da87e/src/OpenClaw.Gateway/SharedHarnessStateService.cs); [`SessionManager.cs`](https://github.com/clawdotnet/openclaw.net/blob/a5d1b7ee689967baf4097c5bf8b578f00e2da87e/src/OpenClaw.Core/Sessions/SessionManager.cs); [`DelegateTool.cs`](https://github.com/clawdotnet/openclaw.net/blob/a5d1b7ee689967baf4097c5bf8b578f00e2da87e/src/OpenClaw.Agent/Tools/DelegateTool.cs).
- Basis: structural negative finding.
- Confidence: medium-high.
- Caveats: `SharedHarnessStateService` is close to an S2 construction surface. A later or separately wired mode that consumes its conflicts to serialize, reassign, isolate or renegotiate affected agent actions could change the result.

### Absence scope

- Surfaces inspected: agent runtime/tool loop, delegated child sessions, session locking/admission, shared harness participants/actions/conflicts, PEV/runtime governance and standard Gateway deployment documentation.
- Plausible first-party paths checked: write/write and read/write conflict detection; assumption conflicts; verifier-obligation escalation; per-session locks; delegation depth/profile/tool constraints; tool execution sequencing.
- Why no material first-party path remains: inspected S2-like mechanisms either protect one session/runtime data structure, decompose work, or produce conflict records/recommendations without a returned coordination decision that changes the affected S1 units.

## S3 — Inside-and-now control

- State: —
- Function: no whole-system inside-and-now regulator established at the declared recursion.
- Disturbance / variety regulated: candidate current-control disturbances include session capacity, runtime/tool risk, contract budgets, failed operations, active goals, delegated children and pending runtime/learning alerts.
- Decisive decision or feedback right: no actor was found with both a whole-system current view and discretionary authority over the runtime's operational population, shared resources, commitments or priorities.
- Decision owner: not established.
- Supporting / enforcement mechanisms: session admission limits/locks; token/runtime budgets; tool governance/approval; PEV trigger/verification policy; goals/background continuation; Runtime Pulse; operator admin surfaces.
- Closure path: deterministic limits and per-action approval/verification can stop or constrain local execution, but they do not constitute a whole-system resource/commitment decision loop.
- Why this is / is not agent-owned: the primary agent can delegate a task and later consume a child result, but the Profile explicitly excludes worker selection/delegation/result aggregation by itself. Runtime Pulse observes selected status and surfaces alerts, but no whole-system current-control authority was found behind it.
- Evidence: [`AgentRuntime.cs`](https://github.com/clawdotnet/openclaw.net/blob/a5d1b7ee689967baf4097c5bf8b578f00e2da87e/src/OpenClaw.Agent/AgentRuntime.cs); [`SessionManager.cs`](https://github.com/clawdotnet/openclaw.net/blob/a5d1b7ee689967baf4097c5bf8b578f00e2da87e/src/OpenClaw.Core/Sessions/SessionManager.cs); [`PlanExecuteVerifyService.cs`](https://github.com/clawdotnet/openclaw.net/blob/a5d1b7ee689967baf4097c5bf8b578f00e2da87e/src/OpenClaw.Gateway/PlanExecuteVerifyService.cs); [`docs/PULSE.md`](https://github.com/clawdotnet/openclaw.net/blob/a5d1b7ee689967baf4097c5bf8b578f00e2da87e/docs/PULSE.md).
- Basis: structural negative finding.
- Confidence: medium-high.
- Caveats: OpenClaw.NET has rich current-state/governance primitives. A mode that unifies these under a regulator with a whole-system view and actual resource/commitment decision rights could qualify in a later review.

### Absence scope

- Surfaces inspected: Gateway/session control, agent goal/background logic, delegation, shared harness state, PEV, tool approval/governance, Runtime Pulse and operator/admin runtime surfaces.
- Plausible first-party paths checked: max-concurrent-session admission, per-session locking, contract and token budgets, PEV escalation/approval, goal continuation, pulse alerts, delegated-child summaries and shared harness participants/actions.
- Why no material first-party path remains: each inspected path is local enforcement, observability, task delegation or operator tooling; none establishes a current whole-system regulator with authority to bargain/revise shared resources, commitments or priorities and close that choice back into operations.

## S3* — Complementary audit

- State: —
- Function: no sufficiently independent complementary operational audit loop established in the standard deployed boundary.
- Disturbance / variety regulated: candidate audit targets include tool-action correctness, approval/contract compliance, security posture, regression obligations and runtime claims.
- Decisive decision or feedback right: no complementary auditor was found whose materially different access to operational reality can challenge ordinary S1/S3 reporting and feed an independent finding into subsequent control.
- Decision owner: not established.
- Supporting / enforcement mechanisms: `PlanExecuteVerifyService` verifiers; evidence bundles; governance ledger; `AuditLogHook`; ordinary approvals; sample-only durable review workflows.
- Closure path: PEV verification is a configured routine stage around the same tool execution path and its deterministic checks can pass/warn/fail that action. `AuditLogHook` only logs and always permits execution. These are valuable assurance surfaces but do not establish the complementary, sufficiently independent access required by S3*.
- Why this is / is not agent-owned: no independent audit actor owns a separate operational-reality access path in the inspected standard mode.
- Evidence: [`PlanExecuteVerifyService.cs`](https://github.com/clawdotnet/openclaw.net/blob/a5d1b7ee689967baf4097c5bf8b578f00e2da87e/src/OpenClaw.Gateway/PlanExecuteVerifyService.cs); [`AuditLogHook.cs`](https://github.com/clawdotnet/openclaw.net/blob/a5d1b7ee689967baf4097c5bf8b578f00e2da87e/src/OpenClaw.Agent/AuditLogHook.cs); [`README.md`](https://github.com/clawdotnet/openclaw.net/blob/a5d1b7ee689967baf4097c5bf8b578f00e2da87e/README.md).
- Basis: structural negative finding.
- Confidence: high.
- Caveats: repository samples demonstrate review-oriented construction patterns, but sample/example membership cannot supply ownership or closure to the assessed deployment boundary under Profile 0.2.4.

### Absence scope

- Surfaces inspected: PEV verifier chain, evidence/governance support, audit logging, tool approval, README review/observability path, review-first learning and durable-agent review sample surfaces.
- Plausible first-party paths checked: outcome/security/regression verification, approval evidence, audit hook, human review and sample reviewer roles.
- Why no material first-party path remains: standard-path verification is routine/in-path and audit logging is observational; the materially more independent reviewer topology found in sample/example material is adjacent to, not operationally wired into, the credited distribution boundary.

## S4 — Outside-and-then intelligence

- State: —
- Function: no externally and prospectively oriented adaptation loop established.
- Disturbance / variety regulated: candidate adaptation signals include repeated operator behaviour, runtime alerts/failures, changing tool/provider state and proposed harness changes.
- Decisive decision or feedback right: no first-party actor was found that models external/future distinctions, develops adaptation options and returns them through current control into changed operational capability.
- Decision owner: not established.
- Supporting / enforcement mechanisms: Learning Proposals; Runtime Pulse; memory/profile/skill mechanisms; automation suggestions; `harness_change` proposals; provider/tool integrations.
- Closure path: Learning Proposals can retain evidence and propose reviewable profile/skill/automation/harness changes, but they are primarily learning from repeated current/operator behaviour and require operator review. Runtime Pulse surfaces current maintenance signals. Neither establishes the Profile-required outside-and-then conversation with an S3 current-control function.
- Why this is / is not agent-owned: model-backed pulse/agent turns may notice conditions and suggest actions, but internal planning, learning, memory and event reaction are explicitly insufficient without an external/prospective model plus return-to-current-capability closure.
- Evidence: [`docs/LEARNING.md`](https://github.com/clawdotnet/openclaw.net/blob/a5d1b7ee689967baf4097c5bf8b578f00e2da87e/docs/LEARNING.md); [`docs/PULSE.md`](https://github.com/clawdotnet/openclaw.net/blob/a5d1b7ee689967baf4097c5bf8b578f00e2da87e/docs/PULSE.md); [`README.md`](https://github.com/clawdotnet/openclaw.net/blob/a5d1b7ee689967baf4097c5bf8b578f00e2da87e/README.md).
- Basis: structural negative finding.
- Confidence: high.
- Caveats: the review-first learning substrate could support a future S4-specific construction, but no such complete loop is credited at this ref.

### Absence scope

- Surfaces inspected: Learning Proposals, Runtime Pulse, goals, memory/profile/skills, automation suggestions, harness-change proposals and provider/tool integration surfaces.
- Plausible first-party paths checked: repeated-behaviour learning; heartbeat/runtime awareness; reviewable durable-change proposals; skill/profile adaptation; external tool/provider sensing.
- Why no material first-party path remains: the inspected mechanisms are internal/current learning, alerting, operator suggestion or generic external I/O; no path establishes both external/future distinctions and a closed adaptation conversation with present operational control.

## S5 — Policy and identity

- State: —
- Function: no runtime identity/ultimate-policy closure established at the declared recursion.
- Disturbance / variety regulated: candidate policy matters include tool risk, approvals, contract constraints, credentials/security, durable learning proposals and suggested harness changes.
- Decisive decision or feedback right: no first-party path was found for an identity- or ultimate-policy-level issue to reach legitimate ultimate authority and return as an authoritative policy decision governing subsequent operation.
- Decision owner: not established.
- Supporting / enforcement mechanisms: static configuration; approval policy; tool governance; PEV risk rules; operator acceptance/rejection of learning proposals; security restrictions.
- Closure path: ordinary tool approval and proposal review can permit/reject concrete actions or durable suggestions, but no identity-level issue/authority/return loop is shown.
- Why this is / is not agent-owned: system prompts, policies, constraints and approvals bound operational behaviour without becoming S5. Operator review of a skill/profile/automation/harness proposal is not by itself evidence of ultimate identity/policy closure.
- Evidence: [`docs/LEARNING.md`](https://github.com/clawdotnet/openclaw.net/blob/a5d1b7ee689967baf4097c5bf8b578f00e2da87e/docs/LEARNING.md); [`PlanExecuteVerifyService.cs`](https://github.com/clawdotnet/openclaw.net/blob/a5d1b7ee689967baf4097c5bf8b578f00e2da87e/src/OpenClaw.Gateway/PlanExecuteVerifyService.cs); [`README.md`](https://github.com/clawdotnet/openclaw.net/blob/a5d1b7ee689967baf4097c5bf8b578f00e2da87e/README.md).
- Basis: structural negative finding.
- Confidence: high.
- Caveats: this is a runtime-boundary finding, not a statement that the OSS project lacks human governance.

### Absence scope

- Surfaces inspected: operator approvals, tool governance/risk controls, PEV governance ledger, Learning Proposals including `harness_change`, runtime/security configuration and repository governance material as an adjacent surface.
- Plausible first-party paths checked: action approval, durable proposal approval, policy/configuration enforcement, security posture and project governance.
- Why no material first-party path remains: inspected decisions are ordinary operational/configuration/change controls, while repository governance is an adjacent project-development system; no credited path closes an identity/ultimate-policy issue back into the deployed runtime.

## Distributed OSS parent arrangement

OpenClaw.NET is an OSS project with documented maintainers and contribution governance, but that development organization is not automatically part of one deployed runtime. No organization-level parent mode is inferred from repository governance. Supported local operator approvals are credited only as operational constraints/review surfaces and do not independently satisfy S3/S4/S5 parent-mode closure.

## Self-hosted and non-human modes

The primary assessed mode is self-hosted and can be operated through Gateway/Companion/CLI/API surfaces. Human approval can be configured for tools and durable learning changes, but the inspected supported modes do not establish function-specific parent loops for S3, S4 or S5. Absence of parent notation therefore reflects the function/closure evidence, not absence of an operator.

## Recursion

`delegate_agent` constructs persisted child sessions with focused profiles and tool subsets, and those child sessions execute the same model-backed agent loop. This proves agentic decomposition and local operational autonomy, but not recursive viability: the child does not thereby acquire its own complete metasystem, durable identity/environment relation or independent S2–S5 closure. The assessment therefore stays at the deployed runtime recursion and uses delegation only as evidence of additional candidate S1 units.

## Variety and escalation

OpenClaw.NET attenuates substantial runtime variety through tool presets, approval rules, token/runtime budgets, session limits, delegation depth, PEV triggers, checkpoints and conservative review-first durable changes. It amplifies capability through configurable tools, skills, channels, model providers, memory and delegation. Exceptional conditions can become warnings, failed PEV checks, runtime events, pulse alerts or operator-visible proposals. Those channels are useful control infrastructure, but the assessment does not promote them to S2/S3/S3*/S4/S5 without the function-specific decision owner and closure required by Profile 0.2.4.

## Evidence gaps

- `SharedHarnessStateService` contains unusually explicit multi-participant conflict models, but no standard frozen-ref consumer was found that turns a detected conflict into a closed coordination action over affected S1 units. A future assessment should re-check this first.
- PEV contains real verification and regression concepts, but the inspected default path is routine tool-path verification rather than complementary independent operational access. If a standard deployment later wires an independent reviewer/evidence source into PEV, S3* should be reconsidered.
- Learning Proposals and Runtime Pulse provide adaptation-oriented primitives, but the frozen ref does not show the external/prospective distinctions plus S3 return loop needed for S4.
- Repository governance and sample review workflows were deliberately excluded from runtime ownership under the boundary-provenance rule.
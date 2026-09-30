---
harness_id: sandbase-harness
project_name: SandBase Harness
repository: https://github.com/sandbaseai/sandbase-harness
review_ref: f4534553352bc22baf226367ab987a611cc30eca
reviewed_at: 2026-09-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-30
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# SandBase Harness

## Review boundary

- System in focus: the shipped SandBase Harness local-first managed-agent runtime at frozen revision `f4534553352bc22baf226367ab987a611cc30eca`, including model-backed sessions, the built-in strategy loop, sandbox/MCP tools, declarative delegation, session/event persistence, optional context memory, scheduling, tool approvals, runtime observability and first-party outcome-evaluation APIs where reachable from the supported distribution.
- Purpose and identity: provide a self-hosted runtime/control-plane layer for persistent AI-agent sessions with sandboxed execution, tools, skills, memory, credentials, audit/replay, scheduling and optional delegated child-agent work.
- Relevant environment: user/API messages; configured model providers; sandbox files/processes; MCP services; persisted session/event state; configured skills and memory; delegated child-agent results; tool-confirmation decisions; scheduler time; runtime failures and operator/API administration.
- Standard-distribution boundary: first-party runtime code under `src/core/`, public `/v1` API/SDK/Console, built-in strategy/session machinery, first-party sandbox adapters, built-in/MCP/delegation tools, scheduling/outcome services and shipped local-first configuration are inside. External model-provider internals, MCP-server internals, Kubernetes/Docker infrastructure semantics, third-party clients, externally authored skills and repository-development governance remain dependencies or adjacent systems unless the frozen first-party runtime itself owns the decisive function.
- Credited operating / distribution surfaces: `README.md`; `docs/spec/requirements.md`; `docs/spec/design.md`; `src/core/session/executor.ts`; `src/strategy/default-strategy.ts`; `src/core/session/session-manager.ts`; `src/core/session/tool-resolver.ts`; `src/core/session/delegation-service.ts`; `src/core/orchestrator/agent-orchestrator.ts`; `src/core/session/context-builder.ts`; `src/core/operations/scheduler.ts`; `src/core/operations/outcome-evaluator.ts`; `src/core/runtime/server-assembly.ts`; and first-party `/v1` routes for sessions, operations, agents, skills and runtime status.
- Adjacent first-party surfaces excluded from ownership: repository CI/release/contributor governance; test-evidence fixtures; documentation-only future adapters; external directory/review/promotional material; operator-authored agent/skill configuration as an autonomous decision source; and any evaluator or administrative API that is not wired back into live operational control.
- First-party operating / deployment modes considered: the documented local-first `/v1` runtime and Console/SDK clients; local-process sandbox; per-session Docker sandbox; Kubernetes `kubectl exec/cp` backend; self-hosted worker-queue backend; built-in model loop; declarative delegated agents; configured tool-approval mode; optional SQLite context memory; scheduled deployments; and the standard outcome-evaluation endpoint.
- Recursion level: one deployed SandBase Harness workspace/runtime is the system in focus. A model-backed session is the primary S1 operational unit. A delegated child is an additional model-backed S1 candidate but is not treated as a recursively viable system merely because it has its own ephemeral sub-session/sandbox.
- Reviewed revision: `f4534553352bc22baf226367ab987a611cc30eca`.
- Observation date: 2026-09-30.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

SandBase Harness explicitly positions itself as a local-first runtime layer around model agents rather than as a visual workflow DSL. Its `SessionManager` owns session lifecycle and persisted event state, while `DefaultSessionExecutor` resolves the selected agent/model, provisions or reuses the session sandbox, builds context from event history plus configured skills/memory, resolves sandbox/MCP/delegation tools, and invokes an `AgentStrategy`. The built-in strategy uses a bounded model/tool loop: the model chooses tool calls, first-party runtime machinery executes them, records results, and returns those observations into subsequent model steps.

The runtime also exposes declarative multi-agent delegation. An agent definition may name permitted delegation targets or enable a general sub-agent; the model receives delegation tools and decides at runtime whether to invoke them. Delegation validates depth/target/cycle constraints, creates an ephemeral child sub-session with its own sandbox and agent configuration, runs the child through the same model-backed strategy, returns the child's text result to the parent and cleans up the child sandbox. This is genuine delegated S1 work, but no first-party mechanism was found that closes a specific inter-S1 conflict/oscillation into changed later behaviour of two or more operating units.

Several substantial control/evaluation surfaces remain non-positive under the Profile's function thresholds. Per-session queues serialize turns and lifecycle APIs can list/stop sessions; runtime metrics aggregate status/usage; scheduled deployments create sessions when operator-authored cron schedules become due. These mechanisms enforce or expose current state but no autonomous whole-system regulator was found that uses the global view to reprioritize, reassign or bargain over shared commitments. Outcome evaluation can score a completed/persisted session transcript using deterministic or model-assisted evaluators and persists the result in `session_outcomes`, but no standard consumer feeds that finding back into the running session/current-control path. Optional SQLite memory retrieves prior user-message content into later context, while agents and skills are changed through operator/API configuration rather than an autonomous outside-and-then adaptation loop.

Primary evidence:

- [`README.md`](https://github.com/sandbaseai/sandbase-harness/blob/f4534553352bc22baf226367ab987a611cc30eca/README.md)
- [`docs/spec/requirements.md`](https://github.com/sandbaseai/sandbase-harness/blob/f4534553352bc22baf226367ab987a611cc30eca/docs/spec/requirements.md)
- [`src/core/session/executor.ts`](https://github.com/sandbaseai/sandbase-harness/blob/f4534553352bc22baf226367ab987a611cc30eca/src/core/session/executor.ts)
- [`src/strategy/default-strategy.ts`](https://github.com/sandbaseai/sandbase-harness/blob/f4534553352bc22baf226367ab987a611cc30eca/src/strategy/default-strategy.ts)
- [`src/core/session/delegation-service.ts`](https://github.com/sandbaseai/sandbase-harness/blob/f4534553352bc22baf226367ab987a611cc30eca/src/core/session/delegation-service.ts)
- [`src/core/session/session-manager.ts`](https://github.com/sandbaseai/sandbase-harness/blob/f4534553352bc22baf226367ab987a611cc30eca/src/core/session/session-manager.ts)
- [`src/core/operations/outcome-evaluator.ts`](https://github.com/sandbaseai/sandbase-harness/blob/f4534553352bc22baf226367ab987a611cc30eca/src/core/operations/outcome-evaluator.ts)
- [`src/api/routes/operations.ts`](https://github.com/sandbaseai/sandbase-harness/blob/f4534553352bc22baf226367ab987a611cc30eca/src/api/routes/operations.ts)

## Operational model

A normal session is created for an operator-selected agent and environment. A user/API event enters that session's serialized execution chain. The executor resolves the agent and model, provisions the session sandbox, reconstructs model context from persisted events plus configured skills/memory, exposes allowed sandbox/MCP/delegation tools and invokes the selected strategy. In the built-in strategy the model iterates over observations and tool results until it completes, hits a step limit, fails or pauses for a required tool confirmation.

When delegation is configured, the parent model may invoke a generated delegation tool. The child receives a separate model-backed execution with its own sandbox and selected agent definition and returns a textual result to the parent. SandBase therefore supplies multiple operational units, but their standard relationship is task handoff/result return. Per-session isolation, serialization, depth/cycle checks and worker claims are enforcement or safety mechanisms rather than evidence of a closed inter-S1 coordination or whole-system management function.

## S1 — Operations

- State: A
- Function: perform open-ended user-directed work through model reasoning, tool selection/execution, delegated child work and iterative observation feedback.
- Disturbance / variety regulated: changing user/API objectives, event/session history, sandbox state, tool and MCP results/failures, delegated child results, configured skills/memory and approval outcomes for gated tool calls.
- Decisive decision or feedback right: choose the next task-specific response, sandbox/MCP tool action or permitted delegation and revise subsequent action from returned observations within the session objective.
- Decision owner: the configured model-backed SandBase agent session; delegated child sessions own their bounded child task decisions while active.
- Supporting / enforcement mechanisms: `DefaultSessionExecutor`; `DefaultStrategy`; model registry; event log; per-session execution chain; sandbox lifecycle; built-in/MCP/delegation tool resolution; max-step and retry limits; optional tool confirmations; context compaction; configured skills and memory.
- Closure path: user/API objective + reconstructed session context → model chooses response/tool/delegation → first-party runtime executes the selected action → tool/delegation observation is persisted/returned to the model loop → the same agent revises its next action until completion or a bounded stop condition.
- Boundary reachability: README and requirements document the self-hosted `/v1` runtime, session/message API and built-in agent execution path; `DefaultSessionExecutor` and `DefaultStrategy` directly implement this standard model/tool feedback loop with first-party built-in tools and optional delegation, so no user-authored orchestration layer is required.
- Why this is / is not agent-owned: if the model-backed agent is removed while queues, sandboxes, event storage, permission checks and lifecycle machinery remain, those components still enforce preselected constraints but no longer choose what task-specific evidence/action to pursue. The material S1 discretion is therefore agent-owned.
- Evidence: [`README.md`](https://github.com/sandbaseai/sandbase-harness/blob/f4534553352bc22baf226367ab987a611cc30eca/README.md); [`requirements.md`](https://github.com/sandbaseai/sandbase-harness/blob/f4534553352bc22baf226367ab987a611cc30eca/docs/spec/requirements.md); [`executor.ts`](https://github.com/sandbaseai/sandbase-harness/blob/f4534553352bc22baf226367ab987a611cc30eca/src/core/session/executor.ts); [`default-strategy.ts`](https://github.com/sandbaseai/sandbase-harness/blob/f4534553352bc22baf226367ab987a611cc30eca/src/strategy/default-strategy.ts); [`delegation-service.ts`](https://github.com/sandbaseai/sandbase-harness/blob/f4534553352bc22baf226367ab987a611cc30eca/src/core/session/delegation-service.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: stronger isolation depends on the selected sandbox backend, but backend strength does not change ownership of the model-backed operational loop.

## S2 — Coordination

- State: —
- Function: no material inter-S1 coordination function established at the declared runtime recursion.
- Disturbance / variety regulated: candidate disturbances include delegated-parent/child interaction, concurrent top-level sessions, shared runtime capacity, delegation cycles and worker-queue contention.
- Decisive decision or feedback right: no first-party path was found that observes a specific interference/conflict/oscillation among distinct agentic S1 units, chooses an attenuation response and returns that coordination result into their subsequent behaviour.
- Decision owner: not established.
- Supporting / enforcement mechanisms: synchronous delegation/result return; per-session sandbox isolation; per-session turn serialization; delegation depth/target/cycle validation; worker-queue claiming; session lifecycle state.
- Closure path: not established for inter-S1 coordination. Parent-child delegation returns a task result, while isolation/serialization/cycle checks prevent or constrain unsafe execution structurally; none of these paths reconstructs an S2-specific conflict → coordination decision → changed later S1 behaviour loop.
- Why this is / is not agent-owned: multiple sessions and delegated agents establish plurality, but Methodology 0.3.6 does not treat handoff, queues, shared runtime state or static graph validation as S2 without a specific interference witness and returned attenuation path.
- Evidence: [`agent-orchestrator.ts`](https://github.com/sandbaseai/sandbase-harness/blob/f4534553352bc22baf226367ab987a611cc30eca/src/core/orchestrator/agent-orchestrator.ts); [`delegation-service.ts`](https://github.com/sandbaseai/sandbase-harness/blob/f4534553352bc22baf226367ab987a611cc30eca/src/core/session/delegation-service.ts); [`session-manager.ts`](https://github.com/sandbaseai/sandbase-harness/blob/f4534553352bc22baf226367ab987a611cc30eca/src/core/session/session-manager.ts); [`requirements.md`](https://github.com/sandbaseai/sandbase-harness/blob/f4534553352bc22baf226367ab987a611cc30eca/docs/spec/requirements.md).
- Basis: structural negative finding.
- Confidence: high.
- Caveats: a future shared-resource/conflict-arbitration mode could change this result if it closes a concrete inter-S1 disturbance back into later agent behaviour.

### Absence scope

- Surfaces inspected: declarative delegation/orchestrator; child-session execution; session lifecycle/queues; sandbox ownership/isolation; self-hosted worker queue; scheduling; public runtime APIs and multi-agent requirements.
- Plausible first-party paths checked: parent/child result exchange; delegation cycle/depth checks; concurrent top-level sessions; session execution serialization; shared runtime/worker capacity; sandbox/file ownership and lifecycle.
- Why no material first-party path remains: the reviewed mechanisms isolate, serialize, validate or hand off work, but none supplies an S2-specific decision/feedback relation for a concrete conflict or oscillation among distinct S1 units.

## S3 — Inside-and-now control

- State: —
- Function: no whole-system inside-and-now regulator established at the declared workspace/runtime recursion.
- Disturbance / variety regulated: candidate current-control disturbances include running/failed/paused sessions, resource/backend capacity, schedules, usage, stalled executions and operator-visible runtime status.
- Decisive decision or feedback right: no autonomous actor was found with both a current whole-runtime view and discretionary authority to reprioritize, reassign or bargain over shared operational commitments/resources on behalf of the whole.
- Decision owner: not established.
- Supporting / enforcement mechanisms: `SessionManager.list/stop/shutdown/reconcileOrphans`; per-session execution chains; runtime `/metrics/summary`; scheduler; sandbox/worker capacity controls; API/Console administration.
- Closure path: deterministic lifecycle operations and operator API calls can inspect or stop individual sessions, and scheduled definitions can create sessions when due, but no first-party current-control loop converts the aggregate state into an autonomous whole-system allocation/intervention decision that closes back into operations.
- Why this is / is not agent-owned: the primary agent can delegate a bounded child task, but delegation/result collection is not a whole-system current-control right. The runtime can enforce stop/queue/schedule rules, but those are machinery around developer/operator-selected constraints rather than an autonomous S3 decision owner.
- Evidence: [`session-manager.ts`](https://github.com/sandbaseai/sandbase-harness/blob/f4534553352bc22baf226367ab987a611cc30eca/src/core/session/session-manager.ts); [`scheduler.ts`](https://github.com/sandbaseai/sandbase-harness/blob/f4534553352bc22baf226367ab987a611cc30eca/src/core/operations/scheduler.ts); [`runtime.ts`](https://github.com/sandbaseai/sandbase-harness/blob/f4534553352bc22baf226367ab987a611cc30eca/src/api/routes/runtime.ts); [`README.md`](https://github.com/sandbaseai/sandbase-harness/blob/f4534553352bc22baf226367ab987a611cc30eca/README.md).
- Basis: structural negative finding.
- Confidence: high.
- Caveats: the control-plane APIs and aggregate metrics could support a future S3 construction, but generic observability/intervention primitives do not receive `C` without an established function-specific current-control path.

### Absence scope

- Surfaces inspected: session manager/listing/stopping/recovery; runtime metrics; scheduler; sandbox lifecycle; worker queue; public API/Console administration; parent-agent delegation.
- Plausible first-party paths checked: cross-session status aggregation; stop/abort; orphan recovery; scheduled session creation; shared resource/back-end limits; delegated-child control; operator/runtime administration.
- Why no material first-party path remains: all inspected paths are local lifecycle enforcement, scheduled execution, observability or operator controls; none establishes a whole-system current regulator with a discretionary resource/commitment decision and returned operational closure.

## S3* — Complementary audit

- State: —
- Function: no sufficiently independent complementary operational audit loop established in the standard runtime boundary.
- Disturbance / variety regulated: candidate audit targets include task/outcome correctness, transcript criteria, tool decisions, runtime failures and persisted event/audit trails.
- Decisive decision or feedback right: no first-party complementary actor/path was found whose independent observation of operational reality produces an audit judgment that is returned into subsequent current control or S1 behaviour.
- Decision owner: not established.
- Supporting / enforcement mechanisms: persisted event log/audit/replay; deterministic and model-assisted outcome evaluator; `/sessions/:id/outcomes/evaluate`; tool confirmation; runtime status/metrics.
- Closure path: outcome evaluation reads a persisted session transcript, computes a score/status/summary and inserts the result into `session_outcomes`; the inspected standard runtime has no consumer that turns that result into retry, correction, reassignment, session control or changed future S1 action. Tool confirmations are in-path operational approvals rather than complementary audit.
- Why this is / is not agent-owned: the optional model-assisted evaluator can own an evaluation judgment, but it observes the ordinary transcript through an explicit post-hoc API call and its finding terminates in stored/API-visible outcome state. Without complementary access plus corrective return, a routine evaluation surface is not S3*.
- Evidence: [`outcome-evaluator.ts`](https://github.com/sandbaseai/sandbase-harness/blob/f4534553352bc22baf226367ab987a611cc30eca/src/core/operations/outcome-evaluator.ts); [`operations.ts`](https://github.com/sandbaseai/sandbase-harness/blob/f4534553352bc22baf226367ab987a611cc30eca/src/api/routes/operations.ts); [`server-assembly.ts`](https://github.com/sandbaseai/sandbase-harness/blob/f4534553352bc22baf226367ab987a611cc30eca/src/core/runtime/server-assembly.ts); [`tool-resolver.ts`](https://github.com/sandbaseai/sandbase-harness/blob/f4534553352bc22baf226367ab987a611cc30eca/src/core/session/tool-resolver.ts).
- Basis: structural negative finding.
- Confidence: high.
- Caveats: outcome evaluation is a material assurance primitive and is wired into the public runtime, but the frozen ref does not close it as complementary operational audit.

### Absence scope

- Surfaces inspected: outcome evaluator and server wiring; outcome routes/storage; event log/audit/replay; strategy hooks; executor configuration; tool-confirmation flow; runtime metrics.
- Plausible first-party paths checked: model-assisted transcript evaluation; deterministic outcome scoring; post-hoc outcome storage; generic `afterStep`/`onComplete` strategy hooks; approval decisions; event replay/observability.
- Why no material first-party path remains: the standard executor does not wire strategy completion hooks to the outcome evaluator, stored outcomes have no runtime feedback consumer, and approval/audit-log paths do not provide an independent complementary view with corrective return.

## S4 — Outside-and-then intelligence

- State: —
- Function: no externally and prospectively oriented adaptation loop established at the declared runtime recursion.
- Disturbance / variety regulated: candidate adaptation signals include prior user/session history, external tool results, outcome scores, runtime failures, skill availability, configured model/sandbox/memory backends and scheduled work.
- Decisive decision or feedback right: no first-party agent was found that turns external/future distinctions into a durable change of agent organization, skills, model/tool policy or runtime capability and returns that adaptation through present control.
- Decision owner: not established.
- Supporting / enforcement mechanisms: optional SQLite context memory; session history/compaction; uploaded skill packages; versioned agent definitions; Settings V2 adapter selection; outcome evaluation; scheduler; external MCP/tool access.
- Closure path: context memory stores/retrieves prior user-message content into later prompts, while skills, agent definitions and runtime adapters are created/selected through operator/API configuration. No standard first-party loop converts sensed external/future change or evaluation evidence into an autonomously selected persistent capability adaptation.
- Why this is / is not agent-owned: remembering earlier user text, researching the current task, scheduling configured jobs and loading operator-authored skills are not an outside-and-then adaptation function by themselves. The ordinary agent tool set exposes sandbox/MCP/delegation actions, not first-party self-administration of agents/skills/settings.
- Evidence: [`context-builder.ts`](https://github.com/sandbaseai/sandbase-harness/blob/f4534553352bc22baf226367ab987a611cc30eca/src/core/session/context-builder.ts); [`memory-provider.ts`](https://github.com/sandbaseai/sandbase-harness/blob/f4534553352bc22baf226367ab987a611cc30eca/src/core/memory/memory-provider.ts); [`skills.ts`](https://github.com/sandbaseai/sandbase-harness/blob/f4534553352bc22baf226367ab987a611cc30eca/src/api/routes/skills.ts); [`agents.ts`](https://github.com/sandbaseai/sandbase-harness/blob/f4534553352bc22baf226367ab987a611cc30eca/src/api/routes/agents.ts); [`tool-resolver.ts`](https://github.com/sandbaseai/sandbase-harness/blob/f4534553352bc22baf226367ab987a611cc30eca/src/core/session/tool-resolver.ts).
- Basis: structural negative finding.
- Confidence: high.
- Caveats: SandBase exposes strong persistence/configuration primitives from which an adaptation system could be composed, but Methodology `C` requires an already-established function-specific path rather than generic CRUD/extension points.

### Absence scope

- Surfaces inspected: context memory extraction/injection; event history/compaction; skills upload/delete/reference path; agent create/version/update/archive path; Settings V2; scheduler; outcome evaluation; standard tool resolver and external MCP access.
- Plausible first-party paths checked: cross-session memory; self-modification via skills/agent definitions; evaluator-driven learning; scheduled adaptation; backend/model/tool changes; external research feeding durable runtime changes.
- Why no material first-party path remains: persistence and configuration changes are either current-task context or operator/developer-authored resources, and no first-party autonomous adaptation owner closes external/prospective evidence into changed present capability.

## S5 — Policy and identity

- State: —
- Function: no runtime identity/ultimate-policy closure established for the deployed SandBase workspace.
- Disturbance / variety regulated: candidate policy matters include agent/system prompts, tool permissions and approvals, credential/access constraints, sandbox policy, settings/backend choices, agent versions and skill selection.
- Decisive decision or feedback right: no first-party path was found for an identity- or ultimate-policy-level issue to reach legitimate ultimate authority and return as authoritative policy governing subsequent operation.
- Decision owner: not established.
- Supporting / enforcement mechanisms: operator-authored agent definitions; versioned agent CRUD; tool permission policies and `always_ask`; API keys; Settings V2; sandbox boundaries; skill configuration; audit logs.
- Closure path: these mechanisms configure or approve concrete operational capability, but no identity/ultimate-policy matter is recognized, escalated to a legitimate S5 authority, decided and returned into the runtime as such.
- Why this is / is not agent-owned: technical resource identity, system prompts, access controls and human tool approvals bound operation without creating S5. An operator may edit agent/settings/skills, but generic configuration authority is not a parent-governed S5 loop absent an evidenced identity-level issue and return path.
- Evidence: [`README.md`](https://github.com/sandbaseai/sandbase-harness/blob/f4534553352bc22baf226367ab987a611cc30eca/README.md); [`agents.ts`](https://github.com/sandbaseai/sandbase-harness/blob/f4534553352bc22baf226367ab987a611cc30eca/src/api/routes/agents.ts); [`tool-resolver.ts`](https://github.com/sandbaseai/sandbase-harness/blob/f4534553352bc22baf226367ab987a611cc30eca/src/core/session/tool-resolver.ts); [`docs/spec/settings-v2.md`](https://github.com/sandbaseai/sandbase-harness/blob/f4534553352bc22baf226367ab987a611cc30eca/docs/spec/settings-v2.md).
- Basis: structural negative finding.
- Confidence: high.
- Caveats: this is a runtime-recursion finding, not a statement about human governance of the SandBase OSS project.

### Absence scope

- Surfaces inspected: agent definitions/versioning; tool permission/confirmation flow; API authentication; settings/backend configuration; skills; sandbox policies; runtime audit; repository governance as an adjacent development system.
- Plausible first-party paths checked: operator approval; configuration revision/audit; agent identity/version changes; runtime access policy; skill/model/backend selection; repository maintainership.
- Why no material first-party path remains: inspected decisions are operational/configuration/development controls, while repository governance is outside one deployed runtime; no credited path closes an identity/ultimate-policy issue through S5 authority and back into runtime operation.

## Distributed OSS parent arrangement

SandBase Harness is open source and exposes local operator administration, but repository maintainers and external community review are not automatically part of a deployed workspace. Operator API/Console actions are credited only where they materially constrain individual runtime actions or configuration. No S3/S4/S5 parent mode is inferred from generic human ability to stop sessions, approve tools, edit agents/skills/settings or maintain the repository.

## Self-hosted and non-human modes

The primary distribution is explicitly local-first/self-hosted and can run model-backed sessions through API, SDK, Console and multiple sandbox backends. Individual tools can be configured for human confirmation; this creates a per-action approval path that returns a tool result to the same S1 session, but it does not by itself establish parent-mode S3/S4/S5. The positive S1 loop is available without a higher-recursion human owner for every decision.

## Recursion

Delegated children run model-backed work in separate ephemeral sub-sessions and sandboxes and return results to their parent. This establishes additional operational units but not recursive viability: the child does not thereby own its own S2–S5 metasystem, durable identity/environment relation or higher-level governance. The assessment therefore remains at one SandBase runtime/workspace recursion.

## Variety and escalation

SandBase attenuates operational variety with per-session sandboxes, serialized turn chains, bounded model steps, retries, permission policies, delegation depth/cycle constraints, session lifecycle states, worker claims and optional human confirmation. It amplifies capability through configurable models, MCP, built-in tools, skills, memory, sandbox backends and delegation. Exceptional events can become structured failures, `requires_action` confirmations, stopped/reconciled sessions, metrics or outcome records. Those are meaningful runtime-control primitives, but at the frozen ref they do not close S2, S3, S3*, S4 or S5 under the function-specific thresholds above.

## Evidence gaps

- Declarative delegation creates genuine additional agentic work units, but no shared-resource/evidence disagreement arbitration path was found between them. Reassess S2 if a standard multi-agent mode later closes a concrete inter-S1 conflict into changed subsequent behaviour.
- Model-assisted outcome evaluation is first-party and runtime-wired, but its output is post-hoc persisted/API-visible state rather than corrective feedback. Reassess S3* if outcome/audit findings become independently sourced and are returned into live current control.
- Aggregate runtime metrics and stop/list/recovery APIs expose substantial control-plane information, but no autonomous whole-system regulator consumes it at this ref. Reassess S3 if such a regulator becomes standard-distribution reachable.
- Context memory, skill/agent CRUD and Settings V2 were explicitly checked for S4/S5; they remain persistence/configuration surfaces rather than autonomous adaptation or identity-policy closure.

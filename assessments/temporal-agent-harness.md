---
harness_id: temporal-agent-harness
project_name: Temporal Agent Harness
repository: https://github.com/temporal-community/temporal-agent-harness
review_ref: d54bef90153a5201aff680cfa36b921bea7cc2e4
reviewed_at: 2026-09-23
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-23
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: C(P)
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Temporal Agent Harness

## Review boundary

- System in focus: one first-party Temporal Agent Harness installation at pinned revision `d54bef90153a5201aff680cfa36b921bea7cc2e4`, including the harness agent workflow/runtime, durable tool execution, subagent composition, workflow-side approval/callback gates, packaged session manager, FastAPI control surface, merged/replayable event streams and packaged Svelte UI.
- Purpose and identity: provide durable autonomous agent workflows whose model/tool turns, subagents, human approvals and client callbacks survive worker/process failure and can be resumed, inspected and controlled through Temporal-backed first-party product surfaces.
- Relevant environment: human/operator; application clients; project/task inputs; model providers; tools and client-side callback capabilities; Temporal service/workers; external data/services reached through tools; operating/runtime failures.
- Standard-distribution boundary: `temporal_agent_harness` package runtime, agent protocol, agent workflow runner, subagent toolset/activities, session-manager workflow, packaged web API and packaged UI. External model providers, Temporal service internals, application-specific agent code and third-party tools do not donate their organizational functions.
- Credited operating / distribution surfaces: `README.md`; `temporal_agent_harness/harness/agent.py`; `temporal_agent_harness/harness/agent_workflow.py`; `temporal_agent_harness/harness/agent_client.py`; `temporal_agent_harness/harness/subagent_toolset.py`; `temporal_agent_harness/harness/subagent_activities.py`; `temporal_agent_harness/web/session_manager.py`; `temporal_agent_harness/web/app.py`; `ui/README.md`; `ui/docs/api.md`.
- Adjacent first-party surfaces excluded from ownership: repository CI/release/contributor workflows; tests and examples except as corroboration; current/default-branch documentation absent from the frozen revision; application-specific concrete agent policies; provider SDK internals; Temporal server scheduling/replay internals beyond the harness-visible durable execution contract.
- First-party operating / deployment modes considered: top-level autonomous agent workflow; durable tool calls; subagent composition via `subagent_toolset`; interactive packaged web/UI sessions; human tool approval; client callback tools; session create/close/control; event replay/attach after disconnect or failure.
- Recursion level: the harness installation/session-manager organization is the system-in-focus. Managed autonomous agent workflows are installation-level S1 units. A parent agent and its child subagents may form a nested lower-recursion organization, but delegation alone is not promoted to installation-level S2.
- Reviewed revision: `d54bef90153a5201aff680cfa36b921bea7cc2e4`.
- Observation date: 2026-09-23.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

The first-party runtime is a Temporal workflow-side agent harness. Agent authors expose typed accepted messages and model-callable tools; `AgentWorkflowRunner` manages turns, tool lifecycle, approvals, callbacks and durable state. Model/tool outcomes are returned to the autonomous agent loop while Temporal supplies replay/retry/recovery mechanics. A failure or disconnect therefore does not create a second organizational decision owner; durability transports the same admitted work across runtime failures.

Multi-agent composition is explicit but subordinate to the parent's task-local tool loop. `subagent_toolset()` generates start/send/stop tools for a statically selected child workflow and `SubagentActivities` durably drives one child turn, deduplicating retries and returning the selected child's reply. This establishes real multiple-agent execution, but the reviewed frozen boundary does not establish a sibling-generated coordination disturbance and S2-specific feedback relation merely from delegation, parallel child handles, stream isolation or Temporal delivery semantics.

The packaged web product adds a separate installation-level control plane. `SessionManagerWorkflow` tracks browser-visible child agent sessions, while `/api/sessions` returns all managed/discovered sessions with execution state. Per-session status exposes current turn, queued messages, approvals and live approval policy. The same first-party API can create and gracefully close sessions, submit messages and resolve pending approvals/callbacks. The packaged Svelte UI is a client of this API. The session manager itself does not autonomously decide which current intervention to perform; it executes caller-selected control operations.

## S1 — Operations

- State: A
- Function: perform open-ended user/application work through autonomous model/tool turns inside durable Temporal-managed agent workflows.
- Disturbance / variety regulated: task uncertainty, model responses, tool/environment outcomes, callback results, runtime interruption, tool failure and iterative task-local feedback.
- Decisive decision or feedback right: choose substantive reasoning/model continuation and tool calls needed to pursue the admitted objective in response to returned model/tool/environment feedback.
- Decision owner: the autonomous model/agent actor executing through the first-party agent workflow/tool loop.
- Supporting / enforcement mechanisms: Temporal workflow durability/replay/retry, typed message dispatch, tool schemas, activity-backed execution, callback transport, approval gates, event publication, timeout/error handling and state persistence.
- Closure path: message/objective is admitted → harness invokes the configured autonomous model with permitted tools/context → model selects substantive action/tool call → harness executes or gates the tool and returns the result/error → model continues until the turn/result closes → state/events remain durable and subsequent work can resume from the persisted workflow.
- Boundary reachability: `README.md` documents the harness as a standard production path for durable agent workflows; `agent.py` and `agent_workflow.py` implement the first-party workflow/tool contract, while the packaged session manager/API starts and addresses these agent workflows directly.
- Why this is / is not agent-owned: Temporal and harness code enforce replay, approvals, typing and lifecycle but do not choose the task solution. Removing the autonomous model actor leaves durable orchestration machinery without the substantive operational decision loop.
- Evidence: [`README.md`](https://github.com/temporal-community/temporal-agent-harness/blob/d54bef90153a5201aff680cfa36b921bea7cc2e4/README.md); [`temporal_agent_harness/harness/agent.py`](https://github.com/temporal-community/temporal-agent-harness/blob/d54bef90153a5201aff680cfa36b921bea7cc2e4/temporal_agent_harness/harness/agent.py); [`temporal_agent_harness/harness/agent_workflow.py`](https://github.com/temporal-community/temporal-agent-harness/blob/d54bef90153a5201aff680cfa36b921bea7cc2e4/temporal_agent_harness/harness/agent_workflow.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: external model/provider internals are not credited as first-party harness functions; `A` credits the autonomous operational actor reached through the shipped first-party workflow boundary.

## S2 — Coordination

- State: —
- Function: no installation-level S2 mutual-adjustment function is established among sibling S1 agent workflows.
- Disturbance / variety regulated: the harness supports multiple sessions, child workflows, concurrent/joined messages and durable subagent calls, but the reviewed standard distribution does not identify an interaction-generated sibling-S1 conflict/oscillation together with an S2-specific attenuation relation and returned behavioral adjustment.
- Decisive decision or feedback right: not established for S2.
- Decision owner: not established.
- Supporting / enforcement mechanisms: subagent start/send/stop tools, child-workflow handles, retry/idempotency keys, stream isolation, `MidTurn.ENQUEUE/REJECT/ACCEPT`, activity heartbeats and message/turn attribution regulate delivery/lifecycle correctness rather than a demonstrated inter-S1 disturbance.
- Closure path: not applicable for the negative finding.
- Boundary reachability: no qualifying installation-level S2 path was found in the frozen first-party runtime, session manager, API or packaged UI.
- Why this is / is not agent-owned: no S2 function is established to classify. Parent-to-child delegation and Temporal sequencing are not evidence that sibling operational units mutually adjust to an interaction-created disturbance.
- Evidence: [`temporal_agent_harness/harness/subagent_toolset.py`](https://github.com/temporal-community/temporal-agent-harness/blob/d54bef90153a5201aff680cfa36b921bea7cc2e4/temporal_agent_harness/harness/subagent_toolset.py); [`temporal_agent_harness/harness/subagent_activities.py`](https://github.com/temporal-community/temporal-agent-harness/blob/d54bef90153a5201aff680cfa36b921bea7cc2e4/temporal_agent_harness/harness/subagent_activities.py); [`ui/docs/api.md`](https://github.com/temporal-community/temporal-agent-harness/blob/d54bef90153a5201aff680cfa36b921bea7cc2e4/ui/docs/api.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: `MidTurn` can serialize/reject/join messages inside one agent workflow and subagent tooling can run several children in parallel; neither alone establishes the Profile's sibling-S1 coordination witness.

### Absence scope

- Surfaces inspected: subagent tool generation; child-turn activity and retry semantics; message disposition (`enqueue`, `reject`, `accept`); merged streams; session manager; packaged API/UI; approval and callback gates.
- Plausible first-party paths checked: parent/subagent delegation, multiple parallel child handles, mid-turn contention, stream merge ordering, workflow retry/idempotency, session-manager child workflow tracking.
- Why no material first-party path remains: these paths admit, route, isolate, serialize or durably deliver work, but no reviewed path ties them to a specific interaction-generated disturbance among sibling S1 units plus an S2-specific feedback relation that changes subsequent sibling behavior.

## S3 — Inside-and-now control

- State: C(P)
- Function: provide a whole-current control surface over the harness installation's managed agent sessions so active work can be inspected, admitted, stopped and constrained through current approvals/callbacks.
- Disturbance / variety regulated: sessions can be running/closed/unavailable, workers may be ready or absent, turns may be active or queued, tool calls can wait for approval, callback tools can wait for client results, and current sessions may need to be started or stopped.
- Decisive decision or feedback right: choose which session to create or close and how to resolve current pending tool/callback gates so subsequent active operation changes.
- Decision owner: constructor mode — the first-party session-manager/API exposes function-specific whole-current state and mutations for a downstream autonomous manager, but none is packaged. Parent mode — the human/operator using the packaged UI/API owns session creation/closure and approval decisions.
- Supporting / enforcement mechanisms: `SessionManagerWorkflow`, Temporal child-workflow lifecycle, `/api/sessions`, live workflow execution state, per-session `AgentStatus`, worker readiness, close signal, tool-approval update, callback-result update and event stream.
- Closure path: whole installation session list/current status is exposed → controller/operator identifies a current intervention → first-party create/close/approval/callback operation is issued → session manager/agent workflow applies it → subsequent session/tool execution changes and refreshed status/events expose the result.
- Boundary reachability: `ui/README.md` identifies the shared Svelte frontend as the packaged harness UI over the FastAPI API; `web/session_manager.py` and `web/app.py` implement the manager, list/status, create/close and approval/callback operations in the standard distribution.
- Why this is / is not agent-owned: the session manager is a durable parent workflow but does not make autonomous supervisory judgments; it tracks sessions and executes requested operations. A downstream autonomous supervisor can be composed over the API, while the shipped human-facing UI closes a parent-governed mode.
- Evidence: [`temporal_agent_harness/web/session_manager.py`](https://github.com/temporal-community/temporal-agent-harness/blob/d54bef90153a5201aff680cfa36b921bea7cc2e4/temporal_agent_harness/web/session_manager.py); [`temporal_agent_harness/web/app.py`](https://github.com/temporal-community/temporal-agent-harness/blob/d54bef90153a5201aff680cfa36b921bea7cc2e4/temporal_agent_harness/web/app.py); [`ui/docs/api.md`](https://github.com/temporal-community/temporal-agent-harness/blob/d54bef90153a5201aff680cfa36b921bea7cc2e4/ui/docs/api.md); [`ui/README.md`](https://github.com/temporal-community/temporal-agent-harness/blob/d54bef90153a5201aff680cfa36b921bea7cc2e4/ui/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: Temporal replay/retry, queueing, message ordering and approval enforcement are supporting mechanisms, not autonomous S3 decision owners.
- Whole-system current view: `GET /api/sessions` returns all sessions tracked by the manager plus discovered running sessions with execution state; agent/worker readiness and per-session `AgentStatus` expose current turn, queued work, pending approvals/callbacks and live approval policy.
- Current-control decision scope: create a managed agent session, gracefully close an active session, submit current work/messages, resolve pending tool approvals (including remember-for-session policy change), and provide pending callback results that unblock current execution.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | downstream autonomous manager must be composed | installation session/status/readiness state indicates a current-control intervention | manager reads first-party list/status surfaces and invokes create/close/approval/callback/message operations; authoritative workflows change and refreshed status/events expose the result | `temporal_agent_harness/web/session_manager.py`; `temporal_agent_harness/web/app.py`; `ui/docs/api.md` |
| Parent (`P`) | human/operator | packaged UI exposes sessions/current state or a pending approval requiring intervention | operator creates/closes a session or approves/denies a gated tool through the shipped UI/API; the workflow applies the decision and subsequent current operation changes | `ui/README.md`; `ui/docs/api.md`; `temporal_agent_harness/web/app.py` |

## S3* — Complementary audit

- State: —
- Function: no materially independent complementary audit loop over operational agent claims/results is established in the reviewed standard distribution.
- Disturbance / variety regulated: replayable events, observable agent state, typed outputs and human tool approvals expose execution evidence and constrain risky actions, but they do not independently challenge a producer's completion/reality claim and return a finding into bounded corrective rework.
- Decisive decision or feedback right: not established for complementary audit.
- Decision owner: not established.
- Supporting / enforcement mechanisms: merged/replayable event streams, message/tool attribution, workflow history, status queries, approval gates, callback-result validation and output typing provide evidence/control but not an independent audit judgment.
- Closure path: not applicable for the negative finding.
- Boundary reachability: no first-party frozen runtime path was found that assigns a distinct reviewer/auditor to an operational result and routes its finding back to the producer for correction before acceptance.
- Why this is / is not agent-owned: observability and replay preserve what happened; human approval decides whether a prospective tool action may proceed. Neither is the Profile's complementary audit function.
- Evidence: [`temporal_agent_harness/harness/agent_client.py`](https://github.com/temporal-community/temporal-agent-harness/blob/d54bef90153a5201aff680cfa36b921bea7cc2e4/temporal_agent_harness/harness/agent_client.py); [`temporal_agent_harness/harness/agent_workflow.py`](https://github.com/temporal-community/temporal-agent-harness/blob/d54bef90153a5201aff680cfa36b921bea7cc2e4/temporal_agent_harness/harness/agent_workflow.py); [`ui/docs/api.md`](https://github.com/temporal-community/temporal-agent-harness/blob/d54bef90153a5201aff680cfa36b921bea7cc2e4/ui/docs/api.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: a developer can build a reviewer as another agent/subagent, but generic ability to compose one does not establish a first-party S3* constructor path without an audit-specific relation.

### Absence scope

- Surfaces inspected: event/replay APIs; agent status; tool approvals; callback validation; subagent composition; Code Mode; session manager; packaged UI/API; frozen design docs for observable/per-message state.
- Plausible first-party paths checked: replay/time-travel observability, human tool approval, typed callback validation, subagent delegation, stream merge and application-defined reviewer composition.
- Why no material first-party path remains: all inspected paths preserve evidence, constrain prospective actions or provide generic composition. None supplies the required independent audit judgment plus corrective return against ordinary operational reporting.

## S4 — Outside-and-then adaptation

- State: —
- Function: no installation-level outside-and-then adaptation loop is established in the reviewed standard distribution.
- Disturbance / variety regulated: model/tool/provider/environment changes can affect agent work, but the harness does not itself sense such future-relevant distinctions, generate organizational adaptation options and close a decision back into present capability/current control.
- Decisive decision or feedback right: not established for S4.
- Decision owner: not established.
- Supporting / enforcement mechanisms: agent registry, typed tool/interface discovery, Code Mode, provider abstractions, runtime state, event history and developer-configured policies expose capability/configuration but do not constitute a first-party adaptive organizational loop.
- Closure path: not applicable for the negative finding.
- Boundary reachability: no qualifying standard-distribution adaptation path was found at the frozen revision.
- Why this is / is not agent-owned: an operational model can reason about a task or write orchestration code, but task-local reasoning does not become S4 unless a first-party outside/future adaptation loop changes organizational capability/control.
- Evidence: [`README.md`](https://github.com/temporal-community/temporal-agent-harness/blob/d54bef90153a5201aff680cfa36b921bea7cc2e4/README.md); [`temporal_agent_harness/harness/subagent_toolset.py`](https://github.com/temporal-community/temporal-agent-harness/blob/d54bef90153a5201aff680cfa36b921bea7cc2e4/temporal_agent_harness/harness/subagent_toolset.py); [`ui/docs/api.md`](https://github.com/temporal-community/temporal-agent-harness/blob/d54bef90153a5201aff680cfa36b921bea7cc2e4/ui/docs/api.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: extensibility and dynamic agent/tool composition can support downstream adaptation designs; Methodology `C` still requires a function-specific S4 path rather than general framework expressiveness.

### Absence scope

- Surfaces inspected: agent registry/interface discovery; Code Mode; model/provider abstractions; session/runtime state; event history; subagent composition; tool/callback policies; packaged UI/API.
- Plausible first-party paths checked: dynamic tool use, Code Mode orchestration, provider selection, runtime replay/history, developer registry changes and application-defined agent composition.
- Why no material first-party path remains: none of these paths reconstructs external/future sensing → adaptation option generation → decisive adaptation feedback → changed present capability/S3 as a first-party organizational function.

## S5 — Identity / ultimate policy

- State: —
- Function: no identity/ultimate-policy closure path is established for the harness installation.
- Disturbance / variety regulated: approval policy, subagent tool policy, registry contents, message handlers and workflow configuration constrain ordinary operation but do not resolve organizational identity or constitutional/ultimate-policy disputes.
- Decisive decision or feedback right: not established for S5.
- Decision owner: not established.
- Supporting / enforcement mechanisms: `ToolApprovalPolicy`, human approve/deny/remember actions, `SubagentToolPolicy`, registry configuration, workflow close and typed agent interfaces are operational policy/control mechanisms.
- Closure path: not applicable for the negative finding.
- Boundary reachability: no first-party standard mode was found that raises an identity/ultimate-policy matter to an authoritative owner and returns that decision as the constitutional constraint for subsequent operation.
- Why this is / is not agent-owned: generic human approval is explicitly lower-level operational authority; it does not become S5 merely because the human has final say over a tool call or session.
- Evidence: [`temporal_agent_harness/harness/agent.py`](https://github.com/temporal-community/temporal-agent-harness/blob/d54bef90153a5201aff680cfa36b921bea7cc2e4/temporal_agent_harness/harness/agent.py); [`temporal_agent_harness/harness/subagent_toolset.py`](https://github.com/temporal-community/temporal-agent-harness/blob/d54bef90153a5201aff680cfa36b921bea7cc2e4/temporal_agent_harness/harness/subagent_toolset.py); [`ui/docs/api.md`](https://github.com/temporal-community/temporal-agent-harness/blob/d54bef90153a5201aff680cfa36b921bea7cc2e4/ui/docs/api.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: safe-by-default approval policy is a strong operational governance feature, but function mapping precedes authority classification and no S5 function is established.

### Absence scope

- Surfaces inspected: human tool approval/remember policy; subagent access policy; agent registry; workflow close/control; message interfaces; Code Mode; packaged UI/API.
- Plausible first-party paths checked: human approval, mutable per-session allow-list, subagent authority narrowing, agent registry choices, workflow/session termination and developer configuration.
- Why no material first-party path remains: these paths govern tool/session execution and composition. None is an identity/ultimate-policy issue with a dedicated ultimate-authority and return-to-operation loop.

## Summary

| Function | State | Decisive owner / path |
| --- | --- | --- |
| S1 | A | autonomous model/agent owns task-local reasoning/tool choice through the durable first-party agent workflow |
| S2 | — | no sibling-S1 disturbance/attenuation/feedback witness established |
| S3 | C(P) | first-party installation session-control constructor surface + closed human packaged-UI mode |
| S3* | — | replay/observability/approvals do not establish independent corrective audit |
| S4 | — | no outside/future adaptation loop established |
| S5 | — | tool/session policy does not establish identity/ultimate-policy closure |

Assessment signature: **`A — C(P) — — —`**.

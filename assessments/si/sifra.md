---
harness_id: sifra
project_name: SIFRA
repository: https://github.com/atharva1407-sys/SIFRA-Agent-Orchestration-Multi-Agent-Runtime
review_ref: 6856b054ba67e4dc4ef499a46732eeed80b5ac68
reviewed_at: 2026-10-20
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# SIFRA

## Review boundary

- System in focus: Shipped TypeScript SIFRA support-agent app: single-agent triage-to-billing loop and alternative supervised customer-escalation mode, not the organization of a real call center.
- Purpose and identity: Handle one customer support work request using task-contingent model and local tools; support durability, optional parallel read-only investigation and human approval of sensitive tool calls.
- Relevant environment: Node/TypeScript Express/WS frontend, configured Vercel AI SDK/OpenAI-compatible model, Postgres/DBOS workflow history, user sending a task/approval. Model provider and persistence library are external execution dependencies.
- Standard-distribution boundary: `server/index.ts`, `sifra/{runtime,supervisor,investigators,agents,tools,model,memory,db,bus,sandbox}.ts`, shared event types and normal WebSocket/HTTP invocation; both `submit_task` modes count. Mock local charges, replies and refund handlers are *not* external billing/email execution.
- Credited operating / distribution surfaces: [server/index.ts](https://github.com/atharva1407-sys/SIFRA-Agent-Orchestration-Multi-Agent-Runtime/blob/6856b054ba67e4dc4ef499a46732eeed80b5ac68/server/index.ts); [sifra/runtime.ts](https://github.com/atharva1407-sys/SIFRA-Agent-Orchestration-Multi-Agent-Runtime/blob/6856b054ba67e4dc4ef499a46732eeed80b5ac68/sifra/runtime.ts); [sifra/supervisor.ts](https://github.com/atharva1407-sys/SIFRA-Agent-Orchestration-Multi-Agent-Runtime/blob/6856b054ba67e4dc4ef499a46732eeed80b5ac68/sifra/supervisor.ts); [sifra/investigators.ts](https://github.com/atharva1407-sys/SIFRA-Agent-Orchestration-Multi-Agent-Runtime/blob/6856b054ba67e4dc4ef499a46732eeed80b5ac68/sifra/investigators.ts); [sifra/agents.ts](https://github.com/atharva1407-sys/SIFRA-Agent-Orchestration-Multi-Agent-Runtime/blob/6856b054ba67e4dc4ef499a46732eeed80b5ac68/sifra/agents.ts); [sifra/tools.ts](https://github.com/atharva1407-sys/SIFRA-Agent-Orchestration-Multi-Agent-Runtime/blob/6856b054ba67e4dc4ef499a46732eeed80b5ac68/sifra/tools.ts); [sifra/memory.ts](https://github.com/atharva1407-sys/SIFRA-Agent-Orchestration-Multi-Agent-Runtime/blob/6856b054ba67e4dc4ef499a46732eeed80b5ac68/sifra/memory.ts); [sifra/db.ts](https://github.com/atharva1407-sys/SIFRA-Agent-Orchestration-Multi-Agent-Runtime/blob/6856b054ba67e4dc4ef499a46732eeed80b5ac68/sifra/db.ts); [sifra/bus.ts](https://github.com/atharva1407-sys/SIFRA-Agent-Orchestration-Multi-Agent-Runtime/blob/6856b054ba67e4dc4ef499a46732eeed80b5ac68/sifra/bus.ts); [sifra/sandbox.ts](https://github.com/atharva1407-sys/SIFRA-Agent-Orchestration-Multi-Agent-Runtime/blob/6856b054ba67e4dc4ef499a46732eeed80b5ac68/sifra/sandbox.ts).
- Adjacent first-party surfaces excluded from ownership: Course lessons, `CLAUDE.md`, OpenSpec drafts, README architecture illustrations, separate runtime SDK internals, UI styling and unrun demo scripts. Generic DBOS/AI SDK internals and externally owned actual customer/finance systems are not transferred to the SIFRA organization.
- First-party operating / deployment modes considered: Interactive model-driven triage with allowed tools and optional billing handoff; `supervised` parallel investigator planning/fan-out/fan-in/synthesis, persistent workflow resume, user refund approval, task stop/cancel and UI event replay. No real customer payments/mail or live paid model executed during evidence review.
- Recursion level: One customer-support workstream/case service, with multiple agent roles inside a bounded request; not a constellation of independently viable continuing customer-support businesses.
- Reviewed revision: `atharva1407-sys/SIFRA-Agent-Orchestration-Multi-Agent-Runtime@6856b054ba67e4dc4ef499a46732eeed80b5ac68` on `main`; exact source Git tree `293059dc6e454f57a25d7e45c61ad39903818a27`; public nonfork, nonarchived GitHub ID 1332269075, repository creation 2026-08-12.
- Observation date: 2026-10-20.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

SIFRA ships two *reachable* first-party modes in the WebSocket server. The normal path dispatches to `DBOS.registerWorkflow(agentWorkflow)`: `streamText` emits model turns, the local harness collects tool calls, intercepts `handoff`, executes selected first-party tool handlers inside DBOS steps, returns structured tool results into later turns, and awaits a human decision for `issueRefund`. The alternative `supervised` path invokes `DBOS.registerWorkflow(supervisorWorkflow)`: a model emits a typed case plan, independent context-window investigators use SDK `generateText` with callable read-only tools, DBOS settles branches in parallel, and a separate model synthesizes one customer reply. First-party `bus`, `db` and server replay expose events; Postgres/DBOS support crash recovery. [server/index.ts](https://github.com/atharva1407-sys/SIFRA-Agent-Orchestration-Multi-Agent-Runtime/blob/6856b054ba67e4dc4ef499a46732eeed80b5ac68/server/index.ts); [sifra/runtime.ts](https://github.com/atharva1407-sys/SIFRA-Agent-Orchestration-Multi-Agent-Runtime/blob/6856b054ba67e4dc4ef499a46732eeed80b5ac68/sifra/runtime.ts); [sifra/supervisor.ts](https://github.com/atharva1407-sys/SIFRA-Agent-Orchestration-Multi-Agent-Runtime/blob/6856b054ba67e4dc4ef499a46732eeed80b5ac68/sifra/supervisor.ts); [sifra/investigators.ts](https://github.com/atharva1407-sys/SIFRA-Agent-Orchestration-Multi-Agent-Runtime/blob/6856b054ba67e4dc4ef499a46732eeed80b5ac68/sifra/investigators.ts).

Critical evidence limitation: [sifra/tools.ts](https://github.com/atharva1407-sys/SIFRA-Agent-Orchestration-Multi-Agent-Runtime/blob/6856b054ba67e4dc4ef499a46732eeed80b5ac68/sifra/tools.ts) implements `sendReply` and `issueRefund` as canned JSON success results, with no customer messaging or money transfer. `getCharges` and KB access return hardcoded demonstration entries. Runtime documentation saying that a refund *really* moves money does not override observed source. The positive S1 is **model-directed demonstration support work**, not verified autonomous production financial operations.

## Operational model

Operationally SIFRA is one task-owning support-agent system. A model selects task-specific tools, role handoffs, or multi-investigator case decomposition. DBOS enforces persistence and fixed control flow. A human approves or rejects a particular sensitive tool invocation. No first-party distinct continuing S1 businesses or standing multi-unit constitutional/current/strategic management boundary is implemented. Independent contexts and approval/guarding count as evidence of their actual local functions only, not automatic VSM metasystem ownership.

## S1 — Operations

- State: A
- Function: Single deployed support-task agent runtime and supervisor case work: model selects support tools/specialist handoff and answers a customer request from observations; in supervised mode model creates a plan for concurrent bounded read-only investigators and synthesizes a case answer.
- Disturbance / variety regulated: Unexpected customer queries, duplicate charge records, incomplete knowledge-base hits, tool failures, specialist handoffs, model-context growth, and unavailable approval for a sensitive step.
- Decisive decision or feedback right: In interactive agent mode, the model's generated tool calls determine current work and the handoff to the billing specialist; the runtime runs local handlers and returns tool-result messages to the model. In supervised mode, a model-generated plan selects relevant billing/technical/sales investigators, each model selects first-party read tools, and a synthesis model decides the response. The user alone approves `issueRefund` requests.
- Decision owner: Configured model-backed first-party support agents plus supervisor planning/synthesis model own task-contingent action judgment; DBOS controls deterministic checkpoint/replay and step sequencing; external human owns refund approval. The `runTool` refund/sendReply handlers only return mock success objects using canned datasets, despite README/prompt wording about real money/mail.
- Supporting / enforcement mechanisms: Registered DBOS agentWorkflow and supervisorWorkflow; Vercel AI SDK streamText/generateObject/generateText; fixed local tool registry, event bus and Postgres/DBOS persistence; triage/billing prompt/tool maps, limited execution budget, tool result message, approval recv and WebSocket entry.
- Closure path: WebSocket submit_task → selected DBOS workflow → model turn or supervisor plan → first-party tool/investigator runs → observed results/DBOS records → next model turn or synthesis; sensitive refund call awaits external /api/approve before local mock handler returns; final event/response recorded and sent to UI.
- Boundary reachability: Shipped server/index.ts dispatches submit_task to the real registered workflows; runtime.ts imports actual first-party model, prompts and tool runner. Supervisor directly calls generateObject, runInvestigator and generateText, with a DBOS recovery-aware execution path.
- Why this is / is not agent-owned: Removing configured model inference eliminates case-dependent tool choice, handoff, subtask plan and synthesis; deterministic DBOS orchestration alone cannot replace those decisions. Canned tool side effects limit what the S1 outcome demonstrates, not whether model/tool work is first-party configured.
- Evidence: [server/index.ts](https://github.com/atharva1407-sys/SIFRA-Agent-Orchestration-Multi-Agent-Runtime/blob/6856b054ba67e4dc4ef499a46732eeed80b5ac68/server/index.ts); [sifra/runtime.ts](https://github.com/atharva1407-sys/SIFRA-Agent-Orchestration-Multi-Agent-Runtime/blob/6856b054ba67e4dc4ef499a46732eeed80b5ac68/sifra/runtime.ts); [sifra/supervisor.ts](https://github.com/atharva1407-sys/SIFRA-Agent-Orchestration-Multi-Agent-Runtime/blob/6856b054ba67e4dc4ef499a46732eeed80b5ac68/sifra/supervisor.ts); [sifra/investigators.ts](https://github.com/atharva1407-sys/SIFRA-Agent-Orchestration-Multi-Agent-Runtime/blob/6856b054ba67e4dc4ef499a46732eeed80b5ac68/sifra/investigators.ts); [sifra/agents.ts](https://github.com/atharva1407-sys/SIFRA-Agent-Orchestration-Multi-Agent-Runtime/blob/6856b054ba67e4dc4ef499a46732eeed80b5ac68/sifra/agents.ts); [sifra/tools.ts](https://github.com/atharva1407-sys/SIFRA-Agent-Orchestration-Multi-Agent-Runtime/blob/6856b054ba67e4dc4ef499a46732eeed80b5ac68/sifra/tools.ts); [sifra/model.ts](https://github.com/atharva1407-sys/SIFRA-Agent-Orchestration-Multi-Agent-Runtime/blob/6856b054ba67e4dc4ef499a46732eeed80b5ac68/sifra/model.ts)
- Basis: structural: first-party reachable runtime with model/tool/feedback loops
- Confidence: High for source-level agentic S1; no live provider test performed.
- Caveats: Provider+database are required for live normal operation. Canned charges/KB and mock sendReply/issueRefund cannot establish actual external customer-message/refund effects, production quality, or third-party billing rights.

## S2 — Coordination

- State: —
- Function: No independent coordination among multiple continuing viable S1 operational departments is established in the packaged customer-support demonstration.
- Disturbance / variety regulated: Billing, technical and sales investigator findings can conflict, fail or overlap while supporting a single customer escalation.
- Decisive decision or feedback right: The supervisor creates a parallel case plan, collects successes/failures and synthesizes one customer reply; `handoff` transfers the same conversation to another specialist. These paths do not mediate reciprocal real disturbances between separately viable ongoing S1 departments.
- Decision owner: A task-specific support supervisor model and deterministic Promise.allSettled/DBOS fan-in rather than an S2 organizational regulator.
- Supporting / enforcement mechanisms: Supervisor PlanSchema, investigator modes, parallel dispatch with failures captured, triage-to-billing handoff and shared event log.
- Closure path: One customer case → parallel bounded investigations or a single handoff → collected results → same customer-case answer. No multi-S1 interdepartmental oscillation report → negotiated balancing constraints → returned commitments to distinct continuing S1 businesses.
- Why this is / is not agent-owned: Specialists have named prompts and read-only tools but no independent enduring purpose, business output obligations or disturbance negotiation scope. Task routing and response synthesis do not become S2 merely because asynchronous branches exist.
- Evidence: [sifra/supervisor.ts](https://github.com/atharva1407-sys/SIFRA-Agent-Orchestration-Multi-Agent-Runtime/blob/6856b054ba67e4dc4ef499a46732eeed80b5ac68/sifra/supervisor.ts); [sifra/investigators.ts](https://github.com/atharva1407-sys/SIFRA-Agent-Orchestration-Multi-Agent-Runtime/blob/6856b054ba67e4dc4ef499a46732eeed80b5ac68/sifra/investigators.ts); [sifra/agents.ts](https://github.com/atharva1407-sys/SIFRA-Agent-Orchestration-Multi-Agent-Runtime/blob/6856b054ba67e4dc4ef499a46732eeed80b5ac68/sifra/agents.ts); [sifra/runtime.ts](https://github.com/atharva1407-sys/SIFRA-Agent-Orchestration-Multi-Agent-Runtime/blob/6856b054ba67e4dc4ef499a46732eeed80b5ac68/sifra/runtime.ts)
- Basis: bounded negative from the configured standard distribution
- Confidence: High at single customer-support-service recursion.
- Caveats: Multiple outside support departments could use the framework but are not delivered here as independent operating S1s.

### Absence scope

- Surfaces inspected: Supervisor full plan/parallel-fan-in/synthesis, investigator roster, triage/billing handoff, event DB and normal server entry.
- Plausible first-party paths checked: Checked whether the three investigation specialties are separately viable continuing S1 units, whether actual ongoing mutual interference is regulated, and whether specific returned operational commitments stabilize those units.
- Why no material first-party path remains: Both paths manage one finite customer escalation and its answer; no in-boundary independent multi-department mutual-regulation authority, reciprocal feedback or enduring S1-unit relationship remains.

## S3 — Inside-and-now control

- State: —
- Function: No current whole-system managerial function deciding resources, accountability, commitments or binding intervention across enduring viable S1 units.
- Disturbance / variety regulated: A customer case has several subtasks, one sub-agent can fail, durable workflow may restart, sensitive actions need approval.
- Decisive decision or feedback right: The model support lead chooses a decomposition for one case and writes a customer answer; DBOS retries/recovery and operator stop/approve perform task-local control. No agent or human is wired as legitimate organization-wide manager with a current multi-unit view, binding resource commitments and return.
- Decision owner: Task-level model planner and external user for action approval; deterministic runtime for DBOS step tracking; no distinct in-scope S3 or accepted parent mode.
- Supporting / enforcement mechanisms: Supervisor structured plan, fan-in, fail events, DBOS workflow, /api/stop, /api/approve, event telemetry.
- Closure path: Single escalation request → subtask plan/dispatch/reply and possible user approval → end of case. No continuing group-level operations report → S3 resource allocation, accountability intervention → changed ongoing unit commitments.
- Why this is / is not agent-owned: A function named `supervisor` is not itself VSM S3. DBOS recovery and a human approving one refund lack managerial multi-unit scope and a standing current-policy mandate.
- Evidence: [sifra/supervisor.ts](https://github.com/atharva1407-sys/SIFRA-Agent-Orchestration-Multi-Agent-Runtime/blob/6856b054ba67e4dc4ef499a46732eeed80b5ac68/sifra/supervisor.ts); [server/index.ts](https://github.com/atharva1407-sys/SIFRA-Agent-Orchestration-Multi-Agent-Runtime/blob/6856b054ba67e4dc4ef499a46732eeed80b5ac68/server/index.ts); [sifra/runtime.ts](https://github.com/atharva1407-sys/SIFRA-Agent-Orchestration-Multi-Agent-Runtime/blob/6856b054ba67e4dc4ef499a46732eeed80b5ac68/sifra/runtime.ts); [sifra/bus.ts](https://github.com/atharva1407-sys/SIFRA-Agent-Orchestration-Multi-Agent-Runtime/blob/6856b054ba67e4dc4ef499a46732eeed80b5ac68/sifra/bus.ts)
- Basis: bounded negative after testing model and parent paths
- Confidence: High.
- Caveats: A deployed institution can use SIFRA as an operational tool; the institution's management decisions are not encoded in this first-party repository.

### Absence scope

- Surfaces inspected: Source of supervisor, server stop/approval handlers, DBOS workflow execution, investigator failures, UI task dispatch and configuration.
- Plausible first-party paths checked: Tested plausible model S3 in supervisor plan, potential human S3 in /api/approve and global stop, and DBOS operational health/step coordination as distinct from discretionary whole-current management.
- Why no material first-party path remains: All recorded decisions are on one incoming support case or its safeguards and do not bind several independently viable operating units; no current multi-unit executive authority and return path is packaged.

## S3* — Complementary audit

- State: —
- Function: No complementary independent verification of ordinary S3 managerial claims against separately accessible field reality, followed by corrections to S3.
- Disturbance / variety regulated: An investigator may fail, a tool claim can be wrong, mock data may be stale, operator may disapprove a refund.
- Decisive decision or feedback right: The supervisor receives investigator findings and failure receipts via Promise.allSettled and composes a response; these observations concern task-level outputs. Event inspection/DBOS logs track execution, not S3 management report accuracy.
- Decision owner: Task orchestration model and deterministic event/status store rather than an independently mandated organizational audit actor.
- Supporting / enforcement mechanisms: Investigator records, failure events, DBOS persistence, event bus/WebSocket inspector and observed customer-support data.
- Closure path: Subagent result or failure → supervisor model/failure emission → customer answer; no ordinary S3 management narrative → independent field sampling → corrective binding report back to S3.
- Why this is / is not agent-owned: Separate investigator context and durable run evidence are not a complementary S3 audit when the reported object and recipient are one S1 support task, not S3 management accounts.
- Evidence: [sifra/supervisor.ts](https://github.com/atharva1407-sys/SIFRA-Agent-Orchestration-Multi-Agent-Runtime/blob/6856b054ba67e4dc4ef499a46732eeed80b5ac68/sifra/supervisor.ts); [sifra/investigators.ts](https://github.com/atharva1407-sys/SIFRA-Agent-Orchestration-Multi-Agent-Runtime/blob/6856b054ba67e4dc4ef499a46732eeed80b5ac68/sifra/investigators.ts); [sifra/bus.ts](https://github.com/atharva1407-sys/SIFRA-Agent-Orchestration-Multi-Agent-Runtime/blob/6856b054ba67e4dc4ef499a46732eeed80b5ac68/sifra/bus.ts); [sifra/db.ts](https://github.com/atharva1407-sys/SIFRA-Agent-Orchestration-Multi-Agent-Runtime/blob/6856b054ba67e4dc4ef499a46732eeed80b5ac68/sifra/db.ts); [server/index.ts](https://github.com/atharva1407-sys/SIFRA-Agent-Orchestration-Multi-Agent-Runtime/blob/6856b054ba67e4dc4ef499a46732eeed80b5ac68/server/index.ts)
- Basis: bounded negative despite separate investigator channels
- Confidence: High.
- Caveats: The raw event log could support an external auditor, but no function-specific S3 audit role/authority is first-party wired.

### Absence scope

- Surfaces inspected: Parallel investigator and failure receipts, supervisor synthesis, DBOS/event history and frontend inspection route.
- Plausible first-party paths checked: Checked whether audit-like direct investigator evidence tests normal S3 managerial reports, whether there is an independent S3* charter, and whether its findings reach a manager able to correct multi-unit current control.
- Why no material first-party path remains: Observations feed the same support-case output rather than challenging a standing manager's whole-system account; no distinct S3* reality-audit decision and return path is shipped.

## S4 — Outside-and-then intelligence

- State: —
- Function: No standing outside-and-then strategic sensing that proposes and accepts durable organizational capability adaptations.
- Disturbance / variety regulated: New customer issue types, an unknown KB query, evolving support tools and future operational requirements.
- Decisive decision or feedback right: Support model dynamically plans only the immediate escalation. Context summarization saves tokens, and known KB cases inform a current answer; there is no model-owned or parent-governed future strategy acceptance and integration into continuing service capability.
- Decision owner: Present-task model and static developer tools/KB; no ongoing prospective intelligence owner or returned accepted adaptation decision.
- Supporting / enforcement mechanisms: Supervisor current-case plan, investigator KB read, memory summarization, canned knowledge, fixed prompt/tool registry.
- Closure path: Current question → KB/charges lookup or case decomposition → present response. No external environment discovery → alternative long-range capability strategy → authoritative acceptance → changes to ongoing runtime policies/capabilities.
- Why this is / is not agent-owned: Adapting a reply to the customer or reducing context size is not future-oriented organizational capability renewal.
- Evidence: [sifra/supervisor.ts](https://github.com/atharva1407-sys/SIFRA-Agent-Orchestration-Multi-Agent-Runtime/blob/6856b054ba67e4dc4ef499a46732eeed80b5ac68/sifra/supervisor.ts); [sifra/investigators.ts](https://github.com/atharva1407-sys/SIFRA-Agent-Orchestration-Multi-Agent-Runtime/blob/6856b054ba67e4dc4ef499a46732eeed80b5ac68/sifra/investigators.ts); [sifra/memory.ts](https://github.com/atharva1407-sys/SIFRA-Agent-Orchestration-Multi-Agent-Runtime/blob/6856b054ba67e4dc4ef499a46732eeed80b5ac68/sifra/memory.ts); [sifra/tools.ts](https://github.com/atharva1407-sys/SIFRA-Agent-Orchestration-Multi-Agent-Runtime/blob/6856b054ba67e4dc4ef499a46732eeed80b5ac68/sifra/tools.ts); [sifra/agents.ts](https://github.com/atharva1407-sys/SIFRA-Agent-Orchestration-Multi-Agent-Runtime/blob/6856b054ba67e4dc4ef499a46732eeed80b5ac68/sifra/agents.ts)
- Basis: bounded negative
- Confidence: High.
- Caveats: Lesson documents discuss extensible harness topics but are not executable first-party organizational S4 ownership.

### Absence scope

- Surfaces inspected: Supervisor plan and case synthesis, agents/investigators, read-only KB, context compaction, source-shipped fixed registry.
- Plausible first-party paths checked: Checked self-initiated future scanning, strategy options, autonomous or legitimate parent acceptance and durable return-to-S3/current capability.
- Why no material first-party path remains: Shipped choices are responses to present customer requests; no first-party strategic/environmental change adoption path exists.

## S5 — Policy and identity

- State: —
- Function: No first-party ultimate constitutional identity/purpose decision loop for the support organization.
- Disturbance / variety regulated: Privilege of refund action, tool access for specialists, unsafe code execution, stop and approval instructions.
- Decisive decision or feedback right: Developer hardcodes tool grants, workflows and human approval for `issueRefund`; HTTP /api/approve delivers one boolean to an awaiting workflow. No actor adjudicates ultimate service identity conflicts or commits binding overarching organizational policy with a return loop.
- Decision owner: External app developer/operator writes configuration and approves a specific action; DBOS/runtime enforce permission, not an organizational S5 owner.
- Supporting / enforcement mechanisms: Fixed triage/billing tool grants, NEEDS_APPROVAL, approval receive/send, sandbox, max steps and stop/cancel endpoints.
- Closure path: Local model selects sensitive call → DBOS waits for human boolean → mock tool executes/rejects; no ultimate identity-policy issue → legitimate authoritative S5 deliberation → binding change of ongoing organization.
- Why this is / is not agent-owned: One human click on a refund is a safety approval on an operational action, not the constitutional policy of a viable organization. Hardcoded role permissions are enforcement, not ultimate identity judgment.
- Evidence: [sifra/runtime.ts](https://github.com/atharva1407-sys/SIFRA-Agent-Orchestration-Multi-Agent-Runtime/blob/6856b054ba67e4dc4ef499a46732eeed80b5ac68/sifra/runtime.ts); [sifra/agents.ts](https://github.com/atharva1407-sys/SIFRA-Agent-Orchestration-Multi-Agent-Runtime/blob/6856b054ba67e4dc4ef499a46732eeed80b5ac68/sifra/agents.ts); [server/index.ts](https://github.com/atharva1407-sys/SIFRA-Agent-Orchestration-Multi-Agent-Runtime/blob/6856b054ba67e4dc4ef499a46732eeed80b5ac68/server/index.ts); [sifra/tools.ts](https://github.com/atharva1407-sys/SIFRA-Agent-Orchestration-Multi-Agent-Runtime/blob/6856b054ba67e4dc4ef499a46732eeed80b5ac68/sifra/tools.ts); [sifra/sandbox.ts](https://github.com/atharva1407-sys/SIFRA-Agent-Orchestration-Multi-Agent-Runtime/blob/6856b054ba67e4dc4ef499a46732eeed80b5ac68/sifra/sandbox.ts)
- Basis: bounded negative after parent-mode review
- Confidence: High.
- Caveats: The support-organization owner could establish such a system externally; first-party shipped implementation does not demonstrate it.

### Absence scope

- Surfaces inspected: Privilege gating in runtime.ts, human approval endpoint, role tool set, sandbox, DBOS cancellation, prompts and static support scope.
- Plausible first-party paths checked: Checked whether any route carries identity/ultimate policy decisions to legitimate owner authority and returns adopted policy to continuing organizational control.
- Why no material first-party path remains: Only a specific sensitive tool approval and developer-established constraints exist; no first-party organization-identity issue channel, binding ultimate policy authority or constitutional return loop.

## Distributed OSS parent arrangement

The public OSS contributors and the support-demo users are not evidenced as a unified higher organizational recursion with delegated current-control or constitutional authority. They may provide source changes or per-tool approval, neither of which supplies a first-party S3/S4/S5 decision-and-return loop for independently viable units.

## Self-hosted and non-human modes

Both the single-agent and supervised pathways run locally with configurable external model/database services. DBOS durability and model API substitution do not by themselves supply a new S2–S5 owner. The human approval route constrains one sensitive S1 action; it is not parent policy governance.

## Recursion

Single continuing *type* of support service, executed as bounded cases. The triage/billing roles and billing/technical/sales investigators are functional job roles within that service, not independently viable S1 businesses. This boundary prevents mistaking a model-planned case decomposition for inter-business coordination or a supervisor executive.

## Variety and escalation

Customer demands, changing case facts, tool failures and missing human approval are local operational disturbances. The model reacts using tools and response synthesis; DBOS catches/replays work; aborted/failed states and approval waiting are visible via the bus. These are operational error/approval paths, not evidence of a distinct algedonic constitutional channel or strategic S4 acceptance mechanism.

## Evidence gaps

Source-pinned first-party runtime review only. No live hosted model run, production DB deployment, long-running recovery exercise or external email/charge/refund effect executed. Typecheck/build, if tested, will be recorded separately and will not be presented as model-performance evidence. Existing mock tool handlers establish how agent tool selection/feedback is wired, not production financial authority. No concrete unresolved first-party S2–S5 closure paths were found after checking the strongest supervisor, investigator, approval and event paths. Hypothetical future integrations do not require `?`.

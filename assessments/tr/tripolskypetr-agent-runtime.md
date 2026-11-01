---
harness_id: tripolskypetr-agent-runtime
project_name: Agent Runtime
repository: https://github.com/tripolskypetr/agent-runtime
review_ref: b7150aacb08333a75c7a53510007dc11df2e2446
reviewed_at: 2026-11-01
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Agent Runtime

## Review boundary

- System in focus: the concrete REST agent service, at the service/request-agent recursion.
- Purpose and identity: transform supplied conversations/files into schema-conforming objects or text using local workspace tools.
- Relevant environment: callers, uploaded files/images, shell environment, Ollama endpoints and malformed model responses.
- Standard-distribution boundary: TypeScript server and its configured pi Agent composition; container/self-hosted object and text endpoints.
- Credited operating / distribution surfaces: src/agent/runInference.ts, queue.ts, workspace.ts, tools, route/server wiring, config and prompt templates.
- Adjacent first-party surfaces excluded from ownership: SDK clients, demo/smoke/schema tests, publishing machinery and admin presentation; upstream pi/Ollama internals remain dependencies.
- First-party operating / deployment modes considered: object and text inference via the server, default or caller-selected model/instructions; no hypothetical external coordinator.
- Recursion level: service with independent inference work cells sharing one transient workspace.
- Reviewed revision: b7150aacb08333a75c7a53510007dc11df2e2446.
- Observation date: 2026-11-01.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

[src/agent/runInference.ts](https://github.com/tripolskypetr/agent-runtime/blob/b7150aacb08333a75c7a53510007dc11df2e2446/src/agent/runInference.ts) instantiates pi Agent with a first-party Ollama streaming adapter, request-specific model/prompt, bash/read/image tools and optional provide_answer. The service materializes files, runs the actor, feeds tool/schema errors back, bounds attempts/turns/time, persists transcript and output attachments to SQLite, then clears the workspace. [src/agent/queue.ts](https://github.com/tripolskypetr/agent-runtime/blob/b7150aacb08333a75c7a53510007dc11df2e2446/src/agent/queue.ts) serializes request work cells because all use the same directory. [src/agent/workspace.ts](https://github.com/tripolskypetr/agent-runtime/blob/b7150aacb08333a75c7a53510007dc11df2e2446/src/agent/workspace.ts) resolves paths and snapshots outputs. [src/agent/systemPrompt.ts](https://github.com/tripolskypetr/agent-runtime/blob/b7150aacb08333a75c7a53510007dc11df2e2446/src/agent/systemPrompt.ts) reloads developer templates; [src/config.ts](https://github.com/tripolskypetr/agent-runtime/blob/b7150aacb08333a75c7a53510007dc11df2e2446/src/config.ts) fixes execution limits. There is no delegate/auditor/adaptation actor in this composition. Operators supply configuration and callers supply tasks. Root MIT licensing does not establish organizational governance. Tests and admin history support inspection, not a separate decisive owner.

## Operational model

Each inference Agent decides how to inspect inputs, invoke tools and formulate a deliverable. The selected SDK supplies execution machinery but this repository wires the concrete runnable product and tool-feedback loop. Request instances are separate operational cells; the serial queue protects their shared destructive workspace lifecycle. Developer-authored limits and retry rules remain enforcement, with no autonomous service-wide resource bargaining.

## S1 — Operations

- State: A
- Function: produce the requested structured/text answer and generated files.
- Disturbance / variety regulated: variable input files, tool observations, schema violations and incomplete model replies.
- Decisive decision or feedback right: choose tools/arguments and revise the task response after observations.
- Decision owner: the instantiated model-backed Agent.
- Supporting / enforcement mechanisms: pi loop, Ollama transport, tool implementations, schema validator, time/turn limits, SQLite and workspace lifecycle.
- Closure path: tool results and invalid-answer feedback return to the same conversation until the agent supplies an accepted result or the run fails.
- Boundary reachability: runInference constructs and prompts the Agent in the public inference/text route; no donor platform-wide role is assumed.
- Why this is / is not agent-owned: removing the model actor leaves storage and guards but no discretionary task transformation.
- Evidence: [src/agent/runInference.ts](https://github.com/tripolskypetr/agent-runtime/blob/b7150aacb08333a75c7a53510007dc11df2e2446/src/agent/runInference.ts); [src/agent/tools/provideAnswer.tool.ts](https://github.com/tripolskypetr/agent-runtime/blob/b7150aacb08333a75c7a53510007dc11df2e2446/src/agent/tools/provideAnswer.tool.ts); [src/agent/ollama.ts](https://github.com/tripolskypetr/agent-runtime/blob/b7150aacb08333a75c7a53510007dc11df2e2446/src/agent/ollama.ts).
- Basis: structural
- Confidence: high
- Caveats: source-supported availability, not a measured quality or reliability claim; no live model run.

## S2 — Coordination

- State: C
- Function: prevent independent request-agent cells from destroying or mixing one another's workspace.
- Disturbance / variety regulated: one inference resets the shared directory before/after work; overlap would erase another inference's inputs/outputs.
- Decisive decision or feedback right: select the non-overlapping admission order into the shared workspace.
- Decision owner: developer-composed deterministic SerialQueue; an autonomous coordination actor is not supplied.
- Supporting / enforcement mechanisms: promise-tail serialization, pending/running state and finally release.
- Closure path: the queued request invokes runInference only after its predecessor settles; failure is caught so subsequent requests can proceed.
- Boundary reachability: the service's concrete shared-workspace inference path uses this request queue; C credits the supplied interference-specific constructor path, not agent discretion.
- Why this is / is not agent-owned: the model cannot revise the ordering policy; the first-party queue exposes the specific coordination path but autonomous choice would require composition.
- Distinct S1 units: independent model-backed inference request work cells with separate inputs and deliverables.
- Inter-S1 disturbance: destructive reset and output collection on the same filesystem directory.
- Attenuating coordination relation: exclusive sequential ownership of the workspace for the entire inference lifecycle.
- Feedback into subsequent S1 behaviour: completion/failure of the predecessor releases the next cell to initialize and operate.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: queue.ts explicitly ties serialization to a shared workspace; runInference's reset/collect/final-reset makes the concrete destructive interference reconstructable.
- Evidence: [src/agent/queue.ts](https://github.com/tripolskypetr/agent-runtime/blob/b7150aacb08333a75c7a53510007dc11df2e2446/src/agent/queue.ts); [src/agent/runInference.ts](https://github.com/tripolskypetr/agent-runtime/blob/b7150aacb08333a75c7a53510007dc11df2e2446/src/agent/runInference.ts); [src/server.ts](https://github.com/tripolskypetr/agent-runtime/blob/b7150aacb08333a75c7a53510007dc11df2e2446/src/server.ts); [src/agent/workspace.ts](https://github.com/tripolskypetr/agent-runtime/blob/b7150aacb08333a75c7a53510007dc11df2e2446/src/agent/workspace.ts).
- Basis: structural
- Confidence: medium
- Caveats: C is a constructor topology, not a claim that FIFO runtime enforcement owns autonomous coordination; no request-level planning is promoted to S3.

## S3 — Inside-and-now control

- State: —
- Function: The run's fixed MAX_TURNS, timeout and MAX_ATTEMPTS plus queue depth do not supply whole-service discretionary resource/commitment control.
- Disturbance / variety regulated: the corresponding service-wide organizational variety is not closed by the reviewed mechanisms.
- Decisive decision or feedback right: no material function-specific right established.
- Decision owner: none established for this function at the declared boundary.
- Supporting / enforcement mechanisms: turn/attempt/time bounds, service queue and admin history
- Closure path: no qualifying organizational closure; ordinary task feedback remains S1.
- Why this is / is not agent-owned: no agent-owned or eligible parent-governed functional loop was found after checking the plausible shipped paths.
- Evidence: [src/agent/runInference.ts](https://github.com/tripolskypetr/agent-runtime/blob/b7150aacb08333a75c7a53510007dc11df2e2446/src/agent/runInference.ts); [src/agent/systemPrompt.ts](https://github.com/tripolskypetr/agent-runtime/blob/b7150aacb08333a75c7a53510007dc11df2e2446/src/agent/systemPrompt.ts); [src/config.ts](https://github.com/tripolskypetr/agent-runtime/blob/b7150aacb08333a75c7a53510007dc11df2e2446/src/config.ts); [src/routes/admin.route.ts](https://github.com/tripolskypetr/agent-runtime/blob/b7150aacb08333a75c7a53510007dc11df2e2446/src/routes/admin.route.ts); [README.md](https://github.com/tripolskypetr/agent-runtime/blob/b7150aacb08333a75c7a53510007dc11df2e2446/README.md).
- Basis: structural
- Confidence: medium-high
- Caveats: bounded standard-distribution absence, not impossibility of custom extension.

### Absence scope

- Surfaces inspected: turn/attempt/time bounds, service queue and admin history
- Plausible first-party paths checked: a whole-system controller choosing/revising resources or a parent current-control transaction
- Why no material first-party path remains: static per-run enforcement and observational history expose no function-specific discretionary whole-service control/return path.

## S3* — Complementary audit

- State: —
- Function: Schema acceptance, logged transcripts and demo tests are routine production validation and observability, not an independent challenge to operational claims.
- Disturbance / variety regulated: the corresponding service-wide organizational variety is not closed by the reviewed mechanisms.
- Decisive decision or feedback right: no material function-specific right established.
- Decision owner: none established for this function at the declared boundary.
- Supporting / enforcement mechanisms: provideAnswer schema validation, runInference transcript persistence, admin routes and demo/schema checks
- Closure path: no qualifying organizational closure; ordinary task feedback remains S1.
- Why this is / is not agent-owned: no agent-owned or eligible parent-governed functional loop was found after checking the plausible shipped paths.
- Evidence: [src/agent/runInference.ts](https://github.com/tripolskypetr/agent-runtime/blob/b7150aacb08333a75c7a53510007dc11df2e2446/src/agent/runInference.ts); [src/agent/systemPrompt.ts](https://github.com/tripolskypetr/agent-runtime/blob/b7150aacb08333a75c7a53510007dc11df2e2446/src/agent/systemPrompt.ts); [src/config.ts](https://github.com/tripolskypetr/agent-runtime/blob/b7150aacb08333a75c7a53510007dc11df2e2446/src/config.ts); [src/routes/admin.route.ts](https://github.com/tripolskypetr/agent-runtime/blob/b7150aacb08333a75c7a53510007dc11df2e2446/src/routes/admin.route.ts); [README.md](https://github.com/tripolskypetr/agent-runtime/blob/b7150aacb08333a75c7a53510007dc11df2e2446/README.md).
- Basis: structural
- Confidence: medium-high
- Caveats: bounded standard-distribution absence, not impossibility of custom extension.

### Absence scope

- Surfaces inspected: provideAnswer schema validation, runInference transcript persistence, admin routes and demo/schema checks
- Plausible first-party paths checked: an independently controlled raw-artifact challenge whose findings enter corrective control
- Why no material first-party path remains: the inspected composition supplies production checks and passive history without an independent audit actor/authority/feedback route.

## S4 — Outside-and-then intelligence

- State: —
- Function: File/image inspection solves the current request; prompt-template reload and model selection do not form prospective capability adaptation.
- Disturbance / variety regulated: the corresponding service-wide organizational variety is not closed by the reviewed mechanisms.
- Decisive decision or feedback right: no material function-specific right established.
- Decision owner: none established for this function at the declared boundary.
- Supporting / enforcement mechanisms: model/config selection, templates, request instructions, history and SDK/demo surfaces
- Closure path: no qualifying organizational closure; ordinary task feedback remains S1.
- Why this is / is not agent-owned: no agent-owned or eligible parent-governed functional loop was found after checking the plausible shipped paths.
- Evidence: [src/agent/runInference.ts](https://github.com/tripolskypetr/agent-runtime/blob/b7150aacb08333a75c7a53510007dc11df2e2446/src/agent/runInference.ts); [src/agent/systemPrompt.ts](https://github.com/tripolskypetr/agent-runtime/blob/b7150aacb08333a75c7a53510007dc11df2e2446/src/agent/systemPrompt.ts); [src/config.ts](https://github.com/tripolskypetr/agent-runtime/blob/b7150aacb08333a75c7a53510007dc11df2e2446/src/config.ts); [src/routes/admin.route.ts](https://github.com/tripolskypetr/agent-runtime/blob/b7150aacb08333a75c7a53510007dc11df2e2446/src/routes/admin.route.ts); [README.md](https://github.com/tripolskypetr/agent-runtime/blob/b7150aacb08333a75c7a53510007dc11df2e2446/README.md).
- Basis: structural
- Confidence: medium-high
- Caveats: bounded standard-distribution absence, not impossibility of custom extension.

### Absence scope

- Surfaces inspected: model/config selection, templates, request instructions, history and SDK/demo surfaces
- Plausible first-party paths checked: external/future sensing producing adaptation options that return into current service capability, including parent-assisted modes
- Why no material first-party path remains: configuration is externally authored; no shipped option-generation and returned capability decision loop is wired.

## S5 — Policy and identity

- State: —
- Function: Prompts and configuration define constraints but no identity/ultimate-policy issue is routed to legitimate authority and returned.
- Disturbance / variety regulated: the corresponding service-wide organizational variety is not closed by the reviewed mechanisms.
- Decisive decision or feedback right: no material function-specific right established.
- Decision owner: none established for this function at the declared boundary.
- Supporting / enforcement mechanisms: system prompt templates/reload, config, request instructions, server/admin routes, README and license
- Closure path: no qualifying organizational closure; ordinary task feedback remains S1.
- Why this is / is not agent-owned: no agent-owned or eligible parent-governed functional loop was found after checking the plausible shipped paths.
- Evidence: [src/agent/runInference.ts](https://github.com/tripolskypetr/agent-runtime/blob/b7150aacb08333a75c7a53510007dc11df2e2446/src/agent/runInference.ts); [src/agent/systemPrompt.ts](https://github.com/tripolskypetr/agent-runtime/blob/b7150aacb08333a75c7a53510007dc11df2e2446/src/agent/systemPrompt.ts); [src/config.ts](https://github.com/tripolskypetr/agent-runtime/blob/b7150aacb08333a75c7a53510007dc11df2e2446/src/config.ts); [src/routes/admin.route.ts](https://github.com/tripolskypetr/agent-runtime/blob/b7150aacb08333a75c7a53510007dc11df2e2446/src/routes/admin.route.ts); [README.md](https://github.com/tripolskypetr/agent-runtime/blob/b7150aacb08333a75c7a53510007dc11df2e2446/README.md).
- Basis: structural
- Confidence: medium-high
- Caveats: bounded standard-distribution absence, not impossibility of custom extension.

### Absence scope

- Surfaces inspected: system prompt templates/reload, config, request instructions, server/admin routes, README and license
- Plausible first-party paths checked: runtime identity dispute, policy amendment authority and authoritative return to operation in autonomous or parent mode
- Why no material first-party path remains: caller instructions/template edits are ordinary external configuration; no supplied identity-level deliberation and authoritative closure path remains.

## Recursion

Separate request cells and dependency nesting do not establish recursively viable metasystems.

## Variety and escalation

Schema/tool observations preserve local task variety. Attempt/turn/time exhaustion returns an error to the caller. These error/status channels do not themselves establish algedonic authority or S3/S5.

## Evidence gaps

No live model execution, provider internals or performance claim is assessed. S2=C is limited to the explicitly wired shared-workspace request coordination constructor. No concrete unexamined shipped metasystem path was identified in the inspected service composition.

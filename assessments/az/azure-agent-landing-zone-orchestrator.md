---
harness_id: azure-agent-landing-zone-orchestrator
project_name: Azure Agent Landing Zone Orchestrator
repository: https://github.com/Azure/agent-app-orchestrator
review_ref: 72909db145ca41b954e18261d89e50318bed592a
reviewed_at: 2026-11-18
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Azure Agent Landing Zone Orchestrator

## Review boundary

- System in focus: One first-party Azure Agent Landing Zone Orchestrator native app deployment, conversational agent and optional `agent-lz-research-review` workflow with configured Microsoft Agent Framework and Azure Foundry services. The entire Azure platform or Agent Framework is outside this assessed system.
- Purpose and identity: Supply an authenticated, configurable, hosted/containerized conversational and research-answer service, with optional sources/tools and an explicit human approval gate before publishing the research result.
- Relevant environment: Incoming authenticated caller topics/messages, Azure Foundry models, managed retrieval/MCP tools, human reviewer decisions, configuration revisions, identity claims and deployment infrastructure.
- Standard-distribution boundary: First-party Python app, concrete Agent/Workflow/Executor factories, configuration and tool composition, native hosted/durable adapters, API service and workflow contracts. Third-party `agent_framework`, cloud inference, Azure identity/hosting and source data remain dependencies, not automatically first-party owners of additional VSM functions.
- Credited operating / distribution surfaces: [README.md](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/README.md), [src/native/agent.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/native/agent.py), [src/native/workflow.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/native/workflow.py), [src/native/config.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/native/config.py), [src/native/hosted.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/native/hosted.py), [src/native/durable.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/native/durable.py), [src/native/tools.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/native/tools.py), [src/native/knowledge.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/native/knowledge.py), [src/api/hosted_entrypoint.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/api/hosted_entrypoint.py) in supported authenticated deployment modes.
- Adjacent first-party surfaces excluded from ownership: Development-only Copilot agents under `.github/agents`, CI/security workflows, sample datasets and golden tests, release instructions, frontend monitoring/configuration dashboards and target infrastructure templates insofar as they do not decide functions at the agent/workflow runtime boundary.
- First-party operating / deployment modes considered: `agent-lz-conversation` model-backed agent; workflow mode with one or up to ten declared research producer occurrences, sequentially executed in fixed ordinal order; `human-review` interactive/durable request_info gate; Hosted or containerized runtime with authenticated caller and optional retrieval/MCP integrations.
- Recursion level: One deployed response/research workflow with model-backed research agent(s) and an external human reviewer; distinct declared research producers are not presumed to form an independently governed viable organization.
- Reviewed revision: `72909db145ca41b954e18261d89e50318bed592a` (frozen canonical upstream public `main`).
- Observation date: 2026-11-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The native layer constructs a Microsoft Agent Framework `Agent` with Foundry model, prompt, optional knowledge toolbox, composed MCP/tools, runtime configuration and identity-aware middleware. In conversation mode the agent responds directly to the caller. In research-review mode `Research.draft` takes an authenticated topic, captures a functional config snapshot, invokes one model agent or sequentially declared producers and projects/merges their textual/presentation outputs. A `HumanReview` executor sends the resulting draft through the Agent Framework `request_info` response boundary and accepts or rejects it; a `Complete` executor yields a final record with revision. First-party code validates configuration, tool/source payloads and trusted caller partitions, while durable/external cloud execution comes from the Agent Framework/runtime and Azure hosting. Sources: [src/native/agent.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/native/agent.py), [src/native/workflow.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/native/workflow.py), [src/native/presentation.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/native/presentation.py), [src/native/config.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/native/config.py), [src/native/durable.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/native/durable.py), [src/native/hosted.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/native/hosted.py), [src/main.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/main.py).

## Operational model

An external caller requests conversational help or asks for a research answer. The authored first-party agent definition delegates model inference to its configured provider, selects and invokes supported tools and returns an answer. In research-review mode the first-party workflow sequences the research producer(s), serializes a validated `ReviewRequest`, waits for a human review response and returns approved/rejected output with the captured functional revision. Presentation consolidation and identity configuration are important safety/integration mechanisms, but cannot be reclassified as inter-agent S2 regulation, S3 current-control or S5 policy ownership merely because their objects are named `supervise`/`config`.


## S1 — Operations
- State: A
- Function: Use a model-backed agent and optional knowledge/MCP tools to answer authenticated questions or draft research results.
- Disturbance / variety regulated: Variable user topics, source availability, dynamic model/tool results and retrieved knowledge.
- Decisive decision or feedback right: Agent chooses responses and tool invocations to accomplish conversational or research task from current inputs.
- Decision owner: Configured model-backed native Agent instance, through first-party shipped `create_agent` definition and research/hosted entry points.
- Supporting / enforcement mechanisms: FoundryChatClient, agent middleware, resource cleanup, tool composition, configuration snapshot, output schema/presentation validation and workflow durable adapter.
- Closure path: The agent runs with caller topic, consumes tool/retrieval responses, returns a draft or direct conversational messages; research mode subsequently delivers draft to a human outcome gate.
- Boundary reachability: `create_agent` constructs a real `agent_framework.Agent` with prompt/tools; `Research.draft` explicitly invokes `agent.run(start.topic)`; supported hosted/container entrypoints instantiate these agents.
- Why this is / is not agent-owned: The model-backed agent selects task-specific content/action; Python and cloud services support execution without becoming separate VSM policy managers.
- Evidence: [src/native/agent.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/native/agent.py), [src/native/workflow.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/native/workflow.py), [src/native/hosted.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/native/hosted.py), [src/native/knowledge.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/native/knowledge.py), [src/native/tools.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/native/tools.py)
- Basis: direct first-party runtime source with concrete agent.run calls
- Confidence: high for reachable configured mode
- Caveats: No live Foundry deployment or external model calls executed during this source-only review; retrieval and tool privileges depend on external services.


## S2 — Coordination
- State: —
- Function: No evidence of first-party attenuation of actual cross-agent conflict/oscillation among separate S1 operating units.
- Disturbance / variety regulated: If research producer agents competed over shared tasks or tool resources, a distinct inter-S1 coordination loop would be necessary.
- Decisive decision or feedback right: No first-party agent-specific conflict/remedy choice or returned corrective act across multiple independent research producers found.
- Decision owner: None at the assessed boundary; declared producer ordinals, sequential runs and display merges are deterministic orchestration, not a conflict-controlling authority.
- Supporting / enforcement mechanisms: Sequential `ResearchProducer` order validation, `merge_presentations` and schema guards, WorkflowBuilder routing.
- Closure path: Messages proceed from research → human-review → complete; no inter-S1 disturbance is judged, attenuated and fed back into later agent work.
- Why this is / is not agent-owned: Serializing source producers and combining presentation outputs cannot serve as positive S2 without a specific operational conflict and corrective feedback.
- Evidence: [src/native/workflow.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/native/workflow.py), [src/native/presentation.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/native/presentation.py), [src/native/contracts.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/native/contracts.py), [src/native/agent.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/native/agent.py)
- Basis: bounded first-party workflow and presentation source
- Confidence: medium-high for declared modes
- Caveats: A downstream application could add coordination through the Agent Framework, but that is outside the pinned first-party app.

### Absence scope

- Surfaces inspected: [src/native/workflow.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/native/workflow.py), [src/native/presentation.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/native/presentation.py), [src/native/contracts.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/native/contracts.py), [src/native/config.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/native/config.py)
- Plausible first-party paths checked: Multiple declared producer workflow occurrences, uniqueness/ordinal checks, sequential agent execution, source presentation merging and graph edges.
- Why no material first-party path remains: These inspected paths validate order/presentation and hand off output; no first-party cross-agent interference, attenuating intervention or return into subsequent distinct S1 operation is supplied.


## S3 — Inside-and-now control
- State: —
- Function: No first-party whole-system inside-and-now authority over the shared commitments of a fleet of S1 units is established.
- Disturbance / variety regulated: Whole-team current resource allocation, competing service capacity, workload priorities or supervisory intervention.
- Decisive decision or feedback right: Human reviewer approves/rejects one research draft, but does not operate a whole-team control view or reassignment/commitment management loop.
- Decision owner: No qualifying S3 owner within installed workflow; deterministic framework state and human output gate do not acquire S3 ownership.
- Supporting / enforcement mechanisms: FunctionalSnapshot, native runtime auth/config validation, durable requests, status outputs and monitoring telemetry.
- Closure path: The single-draft approval response yields a result; no current whole-fleet view → legitimate resource/commitment intervention → changed S1 behavior path was found.
- Why this is / is not agent-owned: Approval of one produced answer is an output gate, not supervisory current-management; runtime scheduler/configuration is enforcement.
- Evidence: [src/native/workflow.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/native/workflow.py), [src/native/config.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/native/config.py), [src/native/durable.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/native/durable.py), [src/telemetry/audit.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/telemetry/audit.py), [src/orchestration/orchestrator.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/orchestration/orchestrator.py)
- Basis: bounded inspected runtime/control surfaces
- Confidence: medium-high
- Caveats: Azure platform tenancy and enterprise governance are external higher-system facilities, not credited to this app.

### Absence scope

- Surfaces inspected: [src/native/workflow.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/native/workflow.py), [src/native/config.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/native/config.py), [src/native/durable.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/native/durable.py), [src/native/hosted.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/native/hosted.py), [src/telemetry/audit.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/telemetry/audit.py)
- Plausible first-party paths checked: Research→human-review graph, mutable deployment configuration, functional revision snapshots, hosted/durable state and instrumentation.
- Why no material first-party path remains: No sourced whole-system current view and discretionary cross-operational commitment/resource control with return into subsequent S1 execution exists in these first-party operating modes.


## S3* — Complementary audit
- State: —
- Function: No independently sourced complementary operational audit with distinct access and corrective closure is established.
- Disturbance / variety regulated: Misleading completion claims, hidden source/data defects and deviations from actual task reality.
- Decisive decision or feedback right: The human review executor accepts a typed yes/no decision about an existing draft; it neither gathers independent evidence nor audits task reality through a second path.
- Decision owner: No qualifying independent S3* auditor; telemetry/audit event recording is ordinary provenance and does not judge operational truth.
- Supporting / enforcement mechanisms: HumanReview request_info, source/presentation validators, audit-event schemas and diagnostic telemetry.
- Closure path: Review may approve or reject the output, but there is no complementary source-of-reality investigation and distinct corrective return to operations.
- Why this is / is not agent-owned: The word 'review' and structured telemetry/audit naming do not prove sufficiently independent auditor judgment; they are ordinary output/record operations.
- Evidence: [src/native/workflow.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/native/workflow.py), [src/native/presentation.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/native/presentation.py), [src/telemetry/audit.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/telemetry/audit.py), [src/telemetry/audit_contract.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/telemetry/audit_contract.py)
- Basis: bounded first-party audited/source surfaces
- Confidence: medium-high
- Caveats: A reviewer could conduct private checks outside the application, but no first-party access to that evidence/closure is supplied.

### Absence scope

- Surfaces inspected: [src/native/workflow.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/native/workflow.py), [src/native/presentation.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/native/presentation.py), [src/telemetry/audit.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/telemetry/audit.py), [src/telemetry/audit_contract.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/telemetry/audit_contract.py)
- Plausible first-party paths checked: Human review response and review request, telemetry/audit schemas, presentation/source-data validation and development-only test datasets.
- Why no material first-party path remains: These paths expose the produced draft or log the same run; no independent direct-evidence audit judgment plus corrective organizational feedback is wired into a shipped runtime.


## S4 — Outside-and-then intelligence
- State: —
- Function: No first-party environmental foresight/prospective change of future organizational capability established.
- Disturbance / variety regulated: Longer-horizon environmental/tool/provider change requiring a redesigned capability, not simply responding to a new question.
- Decisive decision or feedback right: No agent/human prospective adaptation decision and enacted capability change exists; retrieval yields per-request answer context.
- Decision owner: None at this boundary; external Azure configuration/provider operators are outside the first-party S4 closure.
- Supporting / enforcement mechanisms: RAG/KB retrieval, optional MCP tools, runtime configuration snapshots and presentation selection.
- Closure path: Configuration revision is captured for one run and does not itself show external forecast → capability option → adoption into future operational mode.
- Why this is / is not agent-owned: Reading fresh knowledge for the current answer is S1 environment interaction, not outside-and-then strategic adaptation.
- Evidence: [src/native/knowledge.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/native/knowledge.py), [src/native/config.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/native/config.py), [src/native/tools.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/native/tools.py), [src/native/workflow.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/native/workflow.py)
- Basis: bounded source evidence
- Confidence: medium-high
- Caveats: Not a universal impossibility claim; a separate deployment operator could implement a strategic loop externally.

### Absence scope

- Surfaces inspected: [src/native/knowledge.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/native/knowledge.py), [src/native/tools.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/native/tools.py), [src/native/config.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/native/config.py), [src/native/workflow.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/native/workflow.py)
- Plausible first-party paths checked: External retrieval, optional MCP connection, mutable configuration views, functional revision snapshot and research response approval.
- Why no material first-party path remains: No first-party external/prospective decision proposes and adopts an enduring revised service capability; observed external data is used for answering the current request.


## S5 — Policy and identity
- State: —
- Function: No first-party identity/ultimate-policy decision-and-return loop for the organization established.
- Disturbance / variety regulated: Mission/constitutional authority changes, organizational identity and ultimate priorities over the agent service.
- Decisive decision or feedback right: Static authentication and permission modes require trusted principals, but no runtime governing authority changes organizational purpose or identity.
- Decision owner: None established; cloud identity and tenant-level platform governance are separate upstream owners.
- Supporting / enforcement mechanisms: Service vs user delegation authentication, caller partitions, prompt/tool guardrails, configuration schema and audit event validation.
- Closure path: Identity admission checks affect per-call tool access; no legitimate ultimate-policy decision returns to redefine future agent organizational rules.
- Why this is / is not agent-owned: Authentication/authorization is not by itself an S5 constitution; a human approve/reject on one research draft is not a policy identity change.
- Evidence: [src/native/agent.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/native/agent.py), [src/native/config.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/native/config.py), [src/native/workflow.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/native/workflow.py), [src/native/tools.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/native/tools.py), [src/telemetry/audit.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/telemetry/audit.py)
- Basis: bounded first-party code and operational contracts
- Confidence: medium-high
- Caveats: Cloud platform and enterprise organizational S5 are outside the reviewed first-party application.

### Absence scope

- Surfaces inspected: [src/native/agent.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/native/agent.py), [src/native/config.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/native/config.py), [src/native/workflow.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/native/workflow.py), [src/native/tools.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/native/tools.py), [src/telemetry/audit.py](https://github.com/Azure/agent-app-orchestrator/blob/72909db145ca41b954e18261d89e50318bed592a/src/telemetry/audit.py)
- Plausible first-party paths checked: User/service identity checks, hosted storage partition, policy/configuration validation, human answer approval and audit event schemas.
- Why no material first-party path remains: These mechanisms establish call safety/identity of a caller and static configuration, not a first-party governing decision over the agent organization's ultimate identity and returned policy revision.

## Recursion

Research mode may declare up to ten sequential producer occurrences and one human reviewer, but the project does not thereby instantiate an independently coordinated team with S2/S3/S5 at the declared recursion. Azure tenancy, external Microsoft Agent Framework and the deploying company are separate systems, not part of this first-party assessment.

## Variety and escalation

The application handles per-request prompts and retrieval/tool variability; identity/mode validation fail closed for invalid caller/config, and research output waits for approved/rejected human response. These are meaningful S1 service protections, not evidence of six-function viable organizational governance.

## Evidence gaps

- No Foundry model invocation, hosted tenant or durable user-review session run; evidence comes from immutable source, workflow contracts and supported modes.
- Review executor does not independently inspect code/data source reality at this boundary; a human reviewer may gather private evidence outside the app, which is not credited.
- The optional multiple research producers run in declared sequential order; source merging/projection and static config are not counted as cross-agent S2, prospective S4 or identity S5. Future features/deployments could change scope, but frozen `review_ref` does not.
- No independent second semantic reviewer/Audit for this OpenSiro assessment.

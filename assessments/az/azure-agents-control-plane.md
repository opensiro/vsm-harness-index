---
harness_id: azure-agents-control-plane
project_name: Azure Agents Control Plane
repository: https://github.com/microsoft/azure-agents-control-plane
review_ref: 91e8ef1e4711e87395dd1d0733c8204e6058265b
reviewed_at: 2026-10-31
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Azure Agents Control Plane

## Review boundary

- System in focus: the deployable first-party MCP/Next Best Action agent application and its explicitly wired governance/approval/learning interfaces, not the whole Azure or Microsoft 365 tenancy.
- Purpose and identity: run healthcare quality-management agent requests and expose governed tools through a deployable Azure-hosted service.
- Relevant environment: authenticated user requests, Foundry model endpoint, MCP callers, Azure/Fabric data services and human deployment approvers.
- Standard-distribution boundary: pinned Python default MCP runtime (`src/next_best_action_agent.py`), optional TypeScript runtime, AKS/APIM deployment, approval callback, and first-party operational APIs/tools; external Agent Framework, Foundry, Learning SDK, Entra, Logic Apps and Fabric internals are dependencies.
- Credited operating / distribution surfaces: `/agent/chat` and streaming API, model-backed intent/plan and MCP tool handlers, feedback/history tools and configured approval workflow. Their actual calls and returns, not Azure service labels, anchor the assessment.
- Adjacent first-party surfaces excluded from ownership: SpecKit authoring/constitution, agent-onboarding scripts, developer Copilot assistance, infrastructure CI, benchmark/evaluation tests, external tenant owners/approvers and SDK example code. These do not become active autonomous metasystem owners.
- First-party operating / deployment modes considered: Python default deployment with configured Foundry; TypeScript alternative; MCP-only client use; optional Learning SDK capture/training; operator/Teams approval mode.
- Recursion level: one deployed service's user-request/agent/tool execution, not a fleet of independent Azure customer agents or Microsoft tenant governance.
- Reviewed revision: `microsoft/azure-agents-control-plane@91e8ef1e4711e87395dd1d0733c8204e6058265b`; intake #2473/controller #2474 row 1; original #188 row 6.
- Observation date: 2026-10-31.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The [README](https://github.com/microsoft/azure-agents-control-plane/blob/91e8ef1e4711e87395dd1d0733c8204e6058265b/README.md) and [architecture](https://github.com/microsoft/azure-agents-control-plane/blob/91e8ef1e4711e87395dd1d0733c8204e6058265b/docs/AGENTS_ARCHITECTURE.md) distinguish the deployed MCP application from external user/agent clients and Azure resources. [Python runtime](https://github.com/microsoft/azure-agents-control-plane/blob/91e8ef1e4711e87395dd1d0733c8204e6058265b/src/next_best_action_agent.py) instantiates `AzureAIAgentClient` when configured, serves `/agent/chat` and `/agent/chat/stream` with returned model output, and supplies first-party Foundry-backed `analyze_intent`/`generate_plan` and many MCP tools. It handles memory, Fabric read/write paths and approval checkpoints; the actual model/tool decision machinery of the external SDK/provider is not independently reclassified as first-party control.

[Approval engine binding](https://github.com/microsoft/azure-agents-control-plane/blob/91e8ef1e4711e87395dd1d0733c8204e6058265b/src/next_best_action_agent.py#L1091-L1164) makes deployment-like requests return `approval_pending` until verified human approval; it explicitly does not execute deployments. [Learning helpers](https://github.com/microsoft/azure-agents-control-plane/blob/91e8ef1e4711e87395dd1d0733c8204e6058265b/src/next_best_action_agent.py#L1916-L2019) expose episode/reward/policy/training tools using a separate Learning SDK. The deployed agent request path still selects the fixed configured Foundry deployment via `get_model_deployment`; no runtime `policy.choose()` was found in shipped `src/` beyond documentation examples. [Agent identity onboarding](https://github.com/microsoft/azure-agents-control-plane/blob/91e8ef1e4711e87395dd1d0733c8204e6058265b/docs/AGENTS_AGENT365_ONBOARDING.md) requires external tenant owners, consent and verified credentials. No live Azure/provider/E2E execution was conducted.

## Operational model

The supported application runs a model-owned current request/turn with tool and contextual data feedback. Azure APIM/AKS/credential plumbing is enforcement/transport. Approval routes pause narrow high-risk actions for an external human; learning APIs expose separately invoked evaluation/training, but do not show that the resulting policy affects this application's future action selection. There is no evidenced independent S1 fleet or autonomous whole-system decision owner at this recursion.

## S1 — Operations

- State: A
- Function: Answer user requests and perform selected task/tool actions in the deployed agent application.
- Disturbance / variety regulated: Variable natural-language requests, tool results, retrieved facts and unavailable service responses.
- Decisive decision or feedback right: Model-driven selection of answer/plan and subsequent interactions through the configured application.
- Decision owner: Deployed Foundry-backed agent in the first-party `create_mcp_agent` and `/agent/chat` composition; Foundry/Agent Framework internals remain external execution dependencies.
- Supporting / enforcement mechanisms: FastAPI route, MCP tool dispatcher, identity credentials, memory adapters and APIM/AKS.
- Closure path: User/history → configured agent run or Foundry plan generation → returned text/tool output → client and subsequent request context.
- Boundary reachability: The documented Python `azd up` path deploys this service; startup initializes `mcp_ai_agent`, and `/agent/chat` calls `.run(messages)` when a Foundry endpoint is configured. Optional TypeScript and uninstalled third-party agents are not needed for this witness.
- Why this is / is not agent-owned: A configured model selects response content, rather than a fixed policy/route table; the first-party application supplies a real executable request/return composition. This does not credit Azure's internal agent organization.
- Evidence: [runtime client and chat endpoint](https://github.com/microsoft/azure-agents-control-plane/blob/91e8ef1e4711e87395dd1d0733c8204e6058265b/src/next_best_action_agent.py#L2449-L2470), [startup and run](https://github.com/microsoft/azure-agents-control-plane/blob/91e8ef1e4711e87395dd1d0733c8204e6058265b/src/next_best_action_agent.py#L5210-L5352), [model-backed planning](https://github.com/microsoft/azure-agents-control-plane/blob/91e8ef1e4711e87395dd1d0733c8204e6058265b/src/next_best_action_agent.py#L395-L522), [deployment](https://github.com/microsoft/azure-agents-control-plane/blob/91e8ef1e4711e87395dd1d0733c8204e6058265b/README.md#L56-L107)
- Basis: structural
- Confidence: medium
- Caveats: External Foundry credentials/model and SDK are required; source shows reachability, not a verified live deployment or provider-run result.

## S2 — Coordination

- State: —
- Function: No separate first-party inter-S1 conflict-attenuation function established at the one-service recursion.
- Disturbance / variety regulated: Possible multiple-agent contention, tool/request concurrency and conflicting approvals.
- Decisive decision or feedback right: A conflict-specific feedback decision between distinct autonomous operational units.
- Decision owner: No first-party S2 owner identified; external agent clients and platform provisioning may coordinate outside this boundary.
- Supporting / enforcement mechanisms: APIM routing, AKS replicas, memory/session IDs and optional multi-agent/specification labels.
- Closure path: Requests are served/routed; no evidenced agent-to-agent interference repair feedback into their next S1 decisions.
- Why this is / is not agent-owned: Replica load distribution and generic multi-agent option do not document a concrete inter-unit oscillation and adjustment relation.
- Evidence: [README governance and runtime](https://github.com/microsoft/azure-agents-control-plane/blob/91e8ef1e4711e87395dd1d0733c8204e6058265b/README.md), [architecture](https://github.com/microsoft/azure-agents-control-plane/blob/91e8ef1e4711e87395dd1d0733c8204e6058265b/docs/AGENTS_ARCHITECTURE.md), [runtime](https://github.com/microsoft/azure-agents-control-plane/blob/91e8ef1e4711e87395dd1d0733c8204e6058265b/src/next_best_action_agent.py)
- Basis: structural
- Confidence: medium
- Caveats: No full tenant-level fleet orchestration claim.

### Absence scope

- Surfaces inspected: README governance modes, architecture, app routes, MCP/tool dispatch and session/approval flows.
- Plausible first-party paths checked: Parallel request routing, specified multi-agent mode, shared memory, approval contention and coordination through clients.
- Why no material first-party path remains: They show services and communication/permissions, not a shipped conflict-sensitive relation among distinct S1 agents with returned behavioural correction.

## S3 — Inside-and-now control

- State: —
- Function: No first-party whole-current agent organization management established above the one request-serving agent.
- Disturbance / variety regulated: Budgets, current commitments, competing priorities and safe continuation.
- Decisive decision or feedback right: Authoritative reallocation/constraint judgment over ongoing S1 work with returned correction.
- Decision owner: Tenant operator specifies deployment resources and policies; agent handles current request, not a fleet control mandate.
- Supporting / enforcement mechanisms: APIM policies, workload identity, monitoring, approval checkpoint, AKS scaling and observability.
- Closure path: Security or approval checks allow/block narrow actions, but no source-backed whole-system current decision alters a roster of operational S1 commitments.
- Why this is / is not agent-owned: Enterprise control-plane branding is infrastructure/governance support; approval for a deployment recommendation is not evidence of S3-wide supervision.
- Evidence: [architecture](https://github.com/microsoft/azure-agents-control-plane/blob/91e8ef1e4711e87395dd1d0733c8204e6058265b/docs/AGENTS_ARCHITECTURE.md), [approval binding](https://github.com/microsoft/azure-agents-control-plane/blob/91e8ef1e4711e87395dd1d0733c8204e6058265b/src/next_best_action_agent.py#L1091-L1164)
- Basis: structural
- Confidence: medium
- Caveats: Azure tenant-level human management excluded as another system boundary.

### Absence scope

- Surfaces inspected: APIM/AKS and agent deployment design, tool dispatcher, approval engine and observability surfaces.
- Plausible first-party paths checked: Runtime control over many S1 instances, budget/priority arbitration, approval and agent registry/identity flows.
- Why no material first-party path remains: No owned whole-current commitments decision and feedback loop is wired into the deployed agent operating boundary; deterministic/tenant controls do not substitute.

## S3* — Complementary audit

- State: —
- Function: No separate complementary operational audit organization established.
- Disturbance / variety regulated: Misleading operational claims or unauthorized tool/action output.
- Decisive decision or feedback right: Independent reality-access audit verdict returned for correction.
- Decision owner: External evaluators, CI and humans may judge, but no separate first-party audit agent/owner is wired to regulate current operation.
- Supporting / enforcement mechanisms: Evaluation API/test harnesses, telemetry, Defender/Purview integrations and approval verification.
- Closure path: Diagnostics and evaluation records can be inspected; no independent audit finding is automatically returned into current agent correction.
- Why this is / is not agent-owned: The presence of Evaluation SDK metrics, CI and approval records does not itself establish complementary audit independence or feedback closure.
- Evidence: [evaluation documentation](https://github.com/microsoft/azure-agents-control-plane/blob/91e8ef1e4711e87395dd1d0733c8204e6058265b/docs/AGENTS_EVALUATIONS.md), [learning/evaluation helpers](https://github.com/microsoft/azure-agents-control-plane/blob/91e8ef1e4711e87395dd1d0733c8204e6058265b/src/next_best_action_agent.py#L1740-L1915)
- Basis: structural
- Confidence: medium
- Caveats: This is a product-boundary assessment, not an assertion that Azure lacks auditing services.

### Absence scope

- Surfaces inspected: Agent evaluation docs, learning metrics/reward tools, approval/audit handlers, monitoring and CI layout.
- Plausible first-party paths checked: Judge/eval results, independent source access, approval verification and active corrective return.
- Why no material first-party path remains: The shipped evaluation and policy utilities are callable and record results, but no materially independent operational observer is shown closing an S3* correction path over active S1.

## S4 — Outside-and-then intelligence

- State: —
- Function: A separate externally prospective agent-capability adaptation loop is not materially closed in the shipped app.
- Disturbance / variety regulated: Future task/tool/provider changes and recurring failures.
- Decisive decision or feedback right: Select new capabilities/policies using prospective evidence and return the choice to current action selection.
- Decision owner: Developer/operator chooses model/prompt and manually invokes opt-in Learning SDK policy functions; no live S4 owner established.
- Supporting / enforcement mechanisms: Episode capture, reward tools, `SoftmaxPolicy`, offline REINFORCE training, memory and task similarity retrieval.
- Closure path: Learned snapshots can be stored and read; the actual deployed request path continues to call the fixed configured Foundry deployment and has no first-party `policy.choose()` use in `src/` to alter next actions.
- Why this is / is not agent-owned: SDK ability and a conceptual learn loop are not sufficient without a returned operational adaptation. This does not deny that a developer could construct S4 from these pieces.
- Evidence: [learning design/example](https://github.com/microsoft/azure-agents-control-plane/blob/91e8ef1e4711e87395dd1d0733c8204e6058265b/docs/AGENTS_AGENT_LEARNING_DESIGN.md), [runtime model choice](https://github.com/microsoft/azure-agents-control-plane/blob/91e8ef1e4711e87395dd1d0733c8204e6058265b/src/next_best_action_agent.py#L230-L266), [training code](https://github.com/microsoft/azure-agents-control-plane/blob/91e8ef1e4711e87395dd1d0733c8204e6058265b/src/next_best_action_agent.py#L1916-L1999)
- Basis: structural
- Confidence: medium
- Caveats: Source-only negative for the assessed mode; deployment-specific custom action-selection wiring could change it, but is not shipped here.

### Absence scope

- Surfaces inspected: Runtime learning imports/setup, policy read/train/score/tools, task-memory functions, relevant tests and design docs.
- Plausible first-party paths checked: Policy choose/use in live agent, reward-driven training and prospective capability return.
- Why no material first-party path remains: The policy is stored/trained on an optional explicit path but never selected to change agent action in the deployed runtime; only docs demonstrate `policy.choose()`.

## S5 — Policy and identity

- State: —
- Function: No first-party identity/ultimate-policy adjudication and return over the agent organization.
- Disturbance / variety regulated: Legitimate agent identity, sponsor authority, strategic purpose and final policy conflicts.
- Decisive decision or feedback right: Settle an ultimate identity/organizational policy matter and bind subsequent operation.
- Decision owner: External tenant owner/admin and developer supply registration, consent, credentials and SpecKit constitution; no first-party S5 decision loop established.
- Supporting / enforcement mechanisms: Entra Agent ID registration, owner/sponsor checks, RBAC, API gateway, approval workflows and SpecKit files.
- Closure path: Authorized identity/credential registration controls access, but no separate ultimate-policy issue/decision/return relation is implemented at this one-service recursion.
- Why this is / is not agent-owned: Credential ownership and action-level approval are real constraints, not by themselves S5 organizational identity closure.
- Evidence: [onboarding](https://github.com/microsoft/azure-agents-control-plane/blob/91e8ef1e4711e87395dd1d0733c8204e6058265b/docs/AGENTS_AGENT365_ONBOARDING.md), [README governance model](https://github.com/microsoft/azure-agents-control-plane/blob/91e8ef1e4711e87395dd1d0733c8204e6058265b/README.md#L31-L54)
- Basis: structural
- Confidence: medium
- Caveats: A customer's higher-recursion tenant governance is not assessed.

### Absence scope

- Surfaces inspected: Agent identity and onboarding, SpecKit governance, approval flow and runtime policy/credential paths.
- Plausible first-party paths checked: Sponsor/owner registration, high-risk approvals, constitution updates and policy return.
- Why no material first-party path remains: These configure/enforce one application and delegate consent externally; no function-specific ultimate-policy conflict and authoritative S5 return is observed.

## Distributed OSS parent arrangement

Contributor/tenant owners are distinct from the deployed application. Their CI, SpecKit and identity administration do not automatically form a parent S5 or alternative S3/S4 mode for this one service.

## Recursion

The request-serving agent is the operational cell; its configured tool/APIM/Azure dependencies are not separate S1 units under an evidenced agent metasystem. A broader enterprise agent fleet could be assessed under a different declared boundary.

## Variety and escalation

Natural-language requests and data/tool failures are absorbed by the model/return path. High-risk deployment recommendations return approval-pending to a human and tenant access can fail closed. Neither path is asserted as a complete S3/S5 parent loop.

## Evidence gaps

No live provider/tenant test was run, and the operational use of optional learning, actual multi-agent deployment and tenant organizational decisions are not attested. The states above are evidence-bounded conclusions for the shipped default application, not performance or security guarantees.

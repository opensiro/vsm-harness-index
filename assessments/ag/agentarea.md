---
harness_id: agentarea
project_name: AgentArea
repository: https://github.com/agentarea/agentarea
review_ref: 6e610c4ffffdf6b6ba8e45cba27b3ba577e8476c
reviewed_at: 2026-10-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: C(P)
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: P
---

# AgentArea

## Review boundary

- System in focus: one self-hosted AgentArea workspace with its agent task cells, Temporal worker, backend services, platform governance policies and legitimate workspace operator.
- Purpose and identity: execute durable model-directed agent tasks and controlled tool/delegation flows within a workspace-scoped, governed multi-agent infrastructure.
- Relevant environment: workspace users and teams, model providers, MCP servers, remote tools, agent/agent permissions, budgets, external events and infrastructure failures.
- Standard-distribution boundary: released Docker Compose API/worker/Web UI and first-party Python `agentarea-platform` libraries, execution workflow and workspace-scoped toolsets; not the developer's own tenant organization or arbitrary third-party agents.
- Credited operating / distribution surfaces: `agentarea-platform/libs/execution/agentarea_execution/workflows/agent_execution_workflow.py`, agent execution activities, `agentarea-platform/apps/api/agentarea_api/tools/`, governance policy resolver and API routes, workspace services, Temporal orchestration and their shipped Docker/worker wiring.
- Adjacent first-party surfaces excluded from ownership: `docs/` architecture examples and aspirational network topologies, `tests/` and E2E fixture agents, standalone CLI, OSS maintainer CI and contributor governance, and external Ory/LiteLLM/Temporal service behavior not shown by the first-party integration.
- First-party operating / deployment modes considered: model-backed task workflow with MCP/tools, optional agent delegation/child workflows, human approval, workspace policy control from operator API and optional privileged platform-toolset composition.
- Recursion level: one workspace's agent task operating organization, with each independently executable model-backed task or delegated child as an S1 work cell. The separate hosting platform and external service provider are supporting context.
- Reviewed revision: `agentarea/agentarea@6e610c4ffffdf6b6ba8e45cba27b3ba577e8476c` (frozen row 3/5 in Index batch #2393).
- Observation date: 2026-10-30.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

All source links use the [immutable reviewed revision](https://github.com/agentarea/agentarea/tree/6e610c4ffffdf6b6ba8e45cba27b3ba577e8476c). This is source inspection, not a live provider-backed end-to-end evaluation.

## Repository architecture

The [README](https://github.com/agentarea/agentarea/blob/6e610c4ffffdf6b6ba8e45cba27b3ba577e8476c/README.md) describes a self-hosted API/worker/web stack, Temporal durability, workspace isolation, model inference through LiteLLM, MCP tools, task events, authorization and governance. The [agent execution workflow](https://github.com/agentarea/agentarea/blob/6e610c4ffffdf6b6ba8e45cba27b3ba577e8476c/agentarea-platform/libs/execution/agentarea_execution/workflows/agent_execution_workflow.py) implements a real work loop: resolve effective policy/budgets, call the LLM activity, process tool decisions, execute tool and delegation activities, and continue until completion, pause or budget/iteration bounds. Child delegation workflows may run concurrently. The model makes task/tool choices; Temporal and limits enforce selected operating conditions.

Governance has persistent [workspace policy services](https://github.com/agentarea/agentarea/blob/6e610c4ffffdf6b6ba8e45cba27b3ba577e8476c/agentarea-platform/libs/governance/agentarea_governance/application/service.py) and an [effective-policy resolver](https://github.com/agentarea/agentarea/blob/6e610c4ffffdf6b6ba8e45cba27b3ba577e8476c/agentarea-platform/libs/governance/agentarea_governance/domain/policies.py). The execution workflow enforces the captured policy: `decide_tool_action` can allow, deny or trigger an authorized human escalation before tool execution; budget limits and policy revisions constrain subsequent work. The [platform tool registry](https://github.com/agentarea/agentarea/blob/6e610c4ffffdf6b6ba8e45cba27b3ba577e8476c/agentarea-platform/apps/api/agentarea_api/tools/__init__.py) exposes workspace-scoped agent, run, governance-policy, network, inbox and audit capabilities to authorized agent/MCP users. These are tool affordances, not autonomous metasystem decisions by name.

## Operational model

An authorized initiator creates a task for a configured agent in a workspace. Temporal runs a durable agent workflow, which sends messages to a model, chooses and performs permitted tools, may delegate to other registered agents and records task events. The tool policy gate may require a human decision; the response is inserted into subsequent model operation. Workspace operators set effective governance policy and budgets which the workflow snapshots and enforces, including a controlled re-resolution route for budget continuation. Privileged policy tools are first-party constructors for an agent that is explicitly authorized to inspect/change workspace-wide rules; such an agent's governing behavior and authority must still be composed.

The repository also ships architectural diagrams and docs promising agentic networks. They are not independently credited as S2 solely because there are agent-to-agent messages, isolation or parallel delegation. Model/task feedback should not be confused with independent audit or future-oriented S4.

## S1 — Operations

- State: A
- Function: configured model agent carries out a task with independent choice of reasoning, completion and permitted tool actions.
- Disturbance / variety regulated: new instructions, tool outputs, external APIs, model feedback, errors, budget limits, user follow-up.
- Decisive decision or feedback right: choose subsequent task step, issue tool calls, delegate where allowed and decide to complete.
- Decision owner: model-backed agent acting inside the first-party workflow; Temporal controls state transitions but does not select the model's task judgment.
- Supporting / enforcement mechanisms: Temporal durable workflow, model activity, policy gate, MCP tool execution, budget tracker and task/event database.
- Closure path: workspace task → model response → tool/delegation results appended to context → next model turn / completion event to user.
- Boundary reachability: the shipped `AgentExecutionWorkflow.run` and its tool/LLM loop are used by the first-party worker, not merely defined in a test fixture.
- Why this is / is not agent-owned: the autonomous actor chooses task actions within the configured bounds, whereas deterministic ceilings and workflow persistence only constrain that autonomy.
- Evidence: [execution workflow](https://github.com/agentarea/agentarea/blob/6e610c4ffffdf6b6ba8e45cba27b3ba577e8476c/agentarea-platform/libs/execution/agentarea_execution/workflows/agent_execution_workflow.py), [Temporal runner](https://github.com/agentarea/agentarea/blob/6e610c4ffffdf6b6ba8e45cba27b3ba577e8476c/agentarea-platform/libs/execution/agentarea_execution/runners/temporal_runner.py), [README runtime](https://github.com/agentarea/agentarea/blob/6e610c4ffffdf6b6ba8e45cba27b3ba577e8476c/README.md).
- Basis: shipped first-party execution path, not marketing text alone.
- Confidence: high for configured model-backed tasks.
- Caveats: model inference and MCP servers are external and must be installed/configured; no live work was invoked during assessment.

## S2 — Coordination

- State: —
- Function: no first-party S2 regulation path sufficiently evidenced for specific interference among distinct S1 task cells at the declared workspace recursion.
- Disturbance / variety regulated: concurrent delegated agents could duplicate work, contend for an external resource or diverge, but a potential conflict is not evidence of an attenuating S2 loop.
- Decisive decision or feedback right: no specific cross-S1 oscillation/commitment arbitration decision and returned correction established in the reviewed standard execution path.
- Decision owner: not established.
- Supporting / enforcement mechanisms: parallel child workflow fan-out, inbox, agent discovery, workspace scoping, role permissions and network topology; these transport or constrain interactions without proving S2 on their own.
- Closure path: task delegations and result collection exist; no demonstrated conflict-specific adjustment returned to two competing S1 cells.
- Why this is / is not agent-owned: an agent can choose which worker to delegate to, but decomposition, shared communication and access control alone do not constitute S2-specific stabilization.
- Evidence: [concurrent delegated calls in workflow](https://github.com/agentarea/agentarea/blob/6e610c4ffffdf6b6ba8e45cba27b3ba577e8476c/agentarea-platform/libs/execution/agentarea_execution/workflows/agent_execution_workflow.py), [read-only topology tool](https://github.com/agentarea/agentarea/blob/6e610c4ffffdf6b6ba8e45cba27b3ba577e8476c/agentarea-platform/apps/api/agentarea_api/tools/network_toolset.py), [agentic networks docs](https://github.com/agentarea/agentarea/blob/6e610c4ffffdf6b6ba8e45cba27b3ba577e8476c/docs/agentic-networks.md).
- Basis: Methodology-specific negative calibration, not a claim that multi-agent use is impossible.
- Confidence: moderate.
- Caveats: deployment-specific worker conventions may regulate collisions, but are not established by the shipped paths reviewed.

### Absence scope

- Surfaces inspected: agent Temporal execution/child delegation, agent tools, inbox and network tools, governance permissions, docs and relevant e2e tests.
- Plausible first-party paths checked: parent/child result collection, shared workspace authorization, topology/network policy, task scheduling, inbox handoffs and distinct worker arbitration.
- Why no material first-party path remains: source shows orchestration, authorization and communication, but not a distinct conflict-specific inter-S1 feedback decision that attenuates an identified oscillation or resource collision and changes both or subsequent units; the docs' example network topology does not supply such a verified runtime loop.

## S3 — Inside-and-now control

- State: C(P)
- Function: workspace-wide current regulation of permitted agent execution, shared tool rights, task budgets and resource commitments.
- Disturbance / variety regulated: excessive model/tool spend, unauthorized actions and incompatible active run permissions across the workspace.
- Whole-system current view: the workspace-scoped policy registry, policy rule listing, effective resolution for agents/tasks and live task status/budget counters.
- Current-control decision scope: set/revise workspace policy rules, permitted tools, run budget and escalation requirements that constrain multiple S1 tasks.
- Decisive decision or feedback right: choose policy rules and current resource allowances; authorize/reject sensitive work and changes.
- Decision owner: in the standard parent mode, an authorized workspace human/operator; in the constructor mode, a separately composed and granted agent could choose mutations through the shipped privileged `PoliciesToolset`, but the reviewed distribution does not ship a completed autonomous management policy.
- Supporting / enforcement mechanisms: governance API, effective-policy resolver, `assert_enforceable`, `decide_tool_action`, task snapshot, budget tracker, REST/MCP authorization and Temporal continuation machinery.
- Closure path: parent changes rules → policy is persisted/resolved into the next task or authorized policy revision → gate denies/approves requests or budget enforces the new rule. The constructor surface lists and writes rules via the same service, but needs externally composed agent decision and appropriate authority.
- Boundary reachability: the first-party `get_platform_tools()` registers `PoliciesToolset`, and its privileged `create/update` calls the live workspace governance service; the run workflow consumes enforceable policies. Parent API is likewise a shipped operating route.
- Why this is / is not agent-owned: the only complete current-control governance mode observed is parent-owned; the shipped S3-specific toolset is a reachable constructor that can be given to an agent, not itself agent discretion. Therefore C(P), not A(P).
- Evidence: [policies toolset](https://github.com/agentarea/agentarea/blob/6e610c4ffffdf6b6ba8e45cba27b3ba577e8476c/agentarea-platform/apps/api/agentarea_api/tools/policies_toolset.py), [platform tool registration](https://github.com/agentarea/agentarea/blob/6e610c4ffffdf6b6ba8e45cba27b3ba577e8476c/agentarea-platform/apps/api/agentarea_api/tools/__init__.py), [governance policy API](https://github.com/agentarea/agentarea/blob/6e610c4ffffdf6b6ba8e45cba27b3ba577e8476c/agentarea-platform/apps/api/agentarea_api/api/v1/policies.py), [workflow policy gate and revisions](https://github.com/agentarea/agentarea/blob/6e610c4ffffdf6b6ba8e45cba27b3ba577e8476c/agentarea-platform/libs/execution/agentarea_execution/workflows/agent_execution_workflow.py).
- Basis: two distinct reachable ownership modes with actual policy application.
- Confidence: moderate; optional privileged agent toolsets require explicit authority.
- Caveats: a single-task budget tracker alone is not whole-workspace S3; the cross-task policy registry/rule resolution is the relevant whole-system control scope.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | Developer-composed, authorized future agent/controller; none autonomously shipped as whole-workspace policy owner | Agent receives registered privileged governance-policy tool and must be configured to select rule revisions | First-party policy-toolset writes workspace rules; effective-policy resolver affects later tasks; autonomous judgment/authority not prewired | `tools/policies_toolset.py`, `tools/__init__.py`, `governance/application/service.py` |
| Parent (`P`) | Authenticated workspace operator/administrator | Current resource/access/approval requirements change | REST policy writes → effective task policy → budget/tool-approval enforcement or authorized continuation | `api/v1/policies.py`, `workflows/agent_execution_workflow.py` |

## S3* — Complementary audit

- State: —
- Function: no independent complementary probe of an agent's routine execution reports is established as an organizational audit path.
- Disturbance / variety regulated: model-tool reports might omit actual outcomes; complementary evidence would require independent access and return.
- Decisive decision or feedback right: no separate audit authority with a corrective verdict loop identified.
- Decision owner: none established.
- Supporting / enforcement mechanisms: task events, audit logs, `AuditToolset`, policy observer and artifact validation of own outputs; these are compliance/ordinary operational checks unless independently controlled.
- Closure path: no evidence of an independent auditor inspecting reality outside the ordinary workflow and returning findings to workspace control.
- Why this is / is not agent-owned: a tool named audit and recorded execution events are not a separate autonomous audit judge.
- Evidence: [audit toolset registration](https://github.com/agentarea/agentarea/blob/6e610c4ffffdf6b6ba8e45cba27b3ba577e8476c/agentarea-platform/apps/api/agentarea_api/tools/__init__.py), [audit observer](https://github.com/agentarea/agentarea/blob/6e610c4ffffdf6b6ba8e45cba27b3ba577e8476c/agentarea-platform/libs/governance/agentarea_governance/interceptors/observers/audit_observer.py), [artifact validation](https://github.com/agentarea/agentarea/blob/6e610c4ffffdf6b6ba8e45cba27b3ba577e8476c/agentarea-platform/libs/execution/agentarea_execution/activities/artifact_validation.py).
- Basis: absence in reviewed deployed operating boundary.
- Confidence: moderate.
- Caveats: external evaluators or project-specific independent audit agents can be built with the platform; not credited without a wired first-party mode.

### Absence scope

- Surfaces inspected: governance observers, audit toolset/API, task events, artifact-validation activity, primary workflow, tests and examples.
- Plausible first-party paths checked: raw external-state reconciliation, separate agent auditor with independent evidence access, sampled replay and auditor verdict fed back to workspace S3.
- Why no material first-party path remains: built-in audit trail observes the same operational event stream and output checks occur in the normal workflow; no separately independent evaluator and return-to-control procedure is part of the standard deployed workspace runtime.

## S4 — Outside-and-then intelligence

- State: —
- Function: no standard workspace-level externally prospective intelligence and adaptation-option loop established.
- Disturbance / variety regulated: provider/model capability changes, new security threats, user requirements and future tool opportunities are environmental variety.
- Decisive decision or feedback right: no first-party loop selecting and returning future-oriented capability adaptation to workspace policy/current control.
- Decision owner: none established for the scoped S4 function.
- Supporting / enforcement mechanisms: registry/provider discovery, model/tool catalogs, event triggers and user-supplied research-agent tasks.
- Closure path: new registry/provider data may be browsed or synced, but is not a model of alternative future adaptation options returned to S3.
- Why this is / is not agent-owned: a research agent pursuing a user task is S1, not automatically the workspace's strategic intelligence.
- Evidence: [registry service](https://github.com/agentarea/agentarea/tree/6e610c4ffffdf6b6ba8e45cba27b3ba577e8476c/agentarea-platform/libs/registry), [provider model discovery](https://github.com/agentarea/agentarea/tree/6e610c4ffffdf6b6ba8e45cba27b3ba577e8476c/agentarea-platform/libs/llm/agentarea_llm/application), [README](https://github.com/agentarea/agentarea/blob/6e610c4ffffdf6b6ba8e45cba27b3ba577e8476c/README.md).
- Basis: negative-state scoped to shipped workspace runtime rather than user-installed future planners.
- Confidence: moderate.
- Caveats: the repository contains roadmaps and examples of prospective work, excluded as adjacent development/governance.

### Absence scope

- Surfaces inspected: runtime execution loop, model/provider registry, triggers, agent and governance tools, operator integration, first-party docs/tests.
- Plausible first-party paths checked: external capability sensing, prospective distinction-to-options model, decision ownership over adaptation, and returned change to current workspace capability.
- Why no material first-party path remains: catalogs and schedules expose current sources/actions but do not furnish a standard autonomous or parent-governed option-generation/selection S4 conversation with operational S3.

## S5 — Policy and identity

- State: P
- Function: parent ownership of workspace identity, legitimate actor permissions and ultimate governance policy for allowed agent activity.
- Disturbance / variety regulated: conflicting user/agent claims to authority, workspace risk posture, policy boundaries and rules governing future tasks.
- Identity / ultimate-policy issue: who belongs to the workspace and can change its governing baseline, and which categories of agent tool/work are legitimate.
- Ultimate authority in each claimed mode: workspace administrator/human/legitimate parent through workspace and governance-policy APIs, with a first-party authorization graph. A privileged tool's existence is not proof that an agent owns ultimate workspace identity.
- Return-to-operation path: parent establishes/updates baseline rules and membership → persistent workspace-scoped governance service/authorization → effective policy snapshot and tool/approval gate regulate subsequent tasks and tools.
- Decisive decision or feedback right: ultimate workspace operating/identity/risk boundary decisions, distinct from approving one routine tool call.
- Decision owner: authorized parent workspace authority; model agents act within, not above, the policy they are given.
- Supporting / enforcement mechanisms: workspace baseline seeding, permission graph, governance policy resolver, effective task policy, human approval and identity context.
- Closure path: workspace policy decision → saved enforceable rules → new or revised task policy → subsequent tool/action allowed, denied, or escalated under that authority.
- Boundary reachability: the first-party workspace creation API seeds a policy baseline; the same workspace rule service and workflow policy consumer operate in the shipped API/worker mode.
- Why this is / is not agent-owned: runtime restrictions and prompts are supports. Parent governance is credited only because authenticated change and later-task enforcement close a concrete workspace identity/authority loop.
- Evidence: [workspace creation route](https://github.com/agentarea/agentarea/blob/6e610c4ffffdf6b6ba8e45cba27b3ba577e8476c/agentarea-platform/apps/api/agentarea_api/api/v1/workspaces.py), [governance policy API](https://github.com/agentarea/agentarea/blob/6e610c4ffffdf6b6ba8e45cba27b3ba577e8476c/agentarea-platform/apps/api/agentarea_api/api/v1/policies.py), [policy resolver](https://github.com/agentarea/agentarea/blob/6e610c4ffffdf6b6ba8e45cba27b3ba577e8476c/agentarea-platform/libs/governance/agentarea_governance/domain/policies.py), [workflow gate](https://github.com/agentarea/agentarea/blob/6e610c4ffffdf6b6ba8e45cba27b3ba577e8476c/agentarea-platform/libs/execution/agentarea_execution/workflows/agent_execution_workflow.py).
- Basis: parent authority, workspace identity policy and durable return.
- Confidence: moderate.
- Caveats: per-tool approval alone belongs to current operational control; it is not used as standalone S5 evidence.

## Distributed OSS parent arrangement

AgentArea is self-hosted. Upstream contributors do not automatically govern a tenant workspace or own its policy; each workspace's legitimate owner supplies any parent-controlled S3/S5 decision. Agent cooperation in one workspace does not demonstrate project-wide policy rights for remote OSS contributors.

## Self-hosted and non-human modes

The packaged API/worker/Compose mode supports parent-managed workspace policies and optional privileged workspace toolsets, not an automatic autonomous governance board. An entirely non-human installation could grant an agent current-control policy rights; that requires compositional policy/authority and is recorded as `C` rather than pretending the standard distribution already runs it. It does not independently close S4 or S5.

## Recursion

Agent child workflows may be S1 subunits; spawning a child does not prove an autonomous viable recursion. The workspace boundary contains current resource governance and an externally legitimate policy authority. No inference is made that individual agents or the hosting SaaS provider own all higher organizational functions.

## Variety and escalation

The LLM absorbs local task variety while Temporal persists a long-running trajectory. Workspace policy attenuates dangerous resource/tool variety; escalation waits for an authorized parent and feeds the verdict into the next agent turn. That human feedback is current control unless it changes the governing workspace identity/policy. The boundary has no independently wired complementary auditor or prospective S4 adaptation return.

## Evidence gaps

- Reviewed first-party frozen code and documentation only; no provider-backed live execution and no claim about configured third-party models or tenant installations.
- The documentation sketches inter-agent network permissions; source checked did not establish a specific S2 conflict→attenuation→return loop among distinct task S1 units. An actually implemented project-specific arbiter would require a new source-bound review.
- `C(P)` concerns specific reachable governance-policy constructors and a distinct parent mode; it is not a claim that ordinary autonomous agents are deployed with permission to rewrite workspace policies.
- Observability and ordinary artifact validation are not independent S3* audits; registry changes are not by themselves S4 intelligence.
- No independence or ecosystem autonomy grade is inferred from GitHub CI or this assessment.

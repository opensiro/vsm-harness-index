---
harness_id: knowwork
project_name: KnowWork
repository: https://github.com/knowflow-ai/KnowWork
review_ref: 83c763e4fe2d63cd59e0344268afa94321d35585
reviewed_at: 2026-10-24
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# KnowWork

## Review boundary

- System in focus: The standard, self-hosted enterprise KnowWork installation that assembles a DeepSeek Harness (DSH) model/tool agent, presents it to workspace users, and constrains multiple concurrent user sessions through first-party business-server, runtime-host, and session-sandbox machinery.
- Purpose and identity: Deliver enterprise user tasks involving documents, knowledge, skills, business tools and configured model endpoints while respecting the workspace's accounts, permissions and execution boundaries.
- Relevant environment: Employee tasks, separate users/workspaces, knowledge sources, third-party model endpoints, uploaded files, enabled business tools, skills and the Docker host shared by concurrently executing user sessions.
- Standard-distribution boundary: The documented web → FastAPI business service → Node runtime-host (official DeepSeek Harness SDK plus shipped KnowWork profile/plugins) → separate Docker session containers. Installed DSH packages provide the general agent loop; this assessment credits **KnowWork's shipped composition and extension into an operational agent**, not ownership of DSH's upstream loop implementation or the external LLM service.
- Credited operating / distribution surfaces: [runtime profile bundles](https://github.com/knowflow-ai/KnowWork/blob/83c763e4fe2d63cd59e0344268afa94321d35585/runtime-host/profile/package.json#L1-L13), [first-party host plugin composition](https://github.com/knowflow-ai/KnowWork/blob/83c763e4fe2d63cd59e0344268afa94321d35585/runtime-host/plugins/host-bundle/cordis.patch.yml#L1-L114), [agent session open and model turns](https://github.com/knowflow-ai/KnowWork/blob/83c763e4fe2d63cd59e0344268afa94321d35585/runtime-host/plugins/dsh-host/src/http-host.mjs#L143-L260), [Docker session ownership and collision rejection](https://github.com/knowflow-ai/KnowWork/blob/83c763e4fe2d63cd59e0344268afa94321d35585/server/src/knowwork_server/sandbox/containers.py#L37-L202), [workflow agent-step integration](https://github.com/knowflow-ai/KnowWork/blob/83c763e4fe2d63cd59e0344268afa94321d35585/server/src/knowwork_server/workflows/agent.py#L72-L170).
- Adjacent first-party surfaces excluded from ownership: Official `@deepseek-ai/dsh` model/tool/agent/subagent loop implementation, external inference providers, user-authored skill definitions and workflow plans, web UI demos, standalone test mocks, deployment/upgrade preflight, administrative use outside the runtime, and source authors' claims about achieved business outcomes. The business service's RBAC or monitoring is not itself an agent decision owner.
- First-party operating / deployment modes considered: Default full agent chat on a configured model endpoint; quick-answer mode; child subagents with inherited permission policy; user-defined deterministic workflow steps that invoke agent sessions; sandbox-enabled Docker deployment, plus `--no-sandbox` option (in which sandbox-only guarantees are unavailable). Dynamic policy/skill grants and developer upgrades are inspected but not assumed to create metasystem cognition.
- Recursion level: A KnowWork enterprise deployment composed of independently running user-session S1s, not the independent DeepSeek project, the enterprise itself, or a future organization using KnowWork.
- Reviewed revision: `83c763e4fe2d63cd59e0344268afa94321d35585`, frozen in [intake #2000](https://github.com/opensiro/vsm-harness-index/issues/2000) and [serial batch #2001](https://github.com/opensiro/vsm-harness-index/issues/2001).
- Observation date: 2026-10-24.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The Python business service owns identity, grants, model/tool credentials, workspace-scoped tool calls, per-user conversations, workflow execution, trace projections, audit records and Docker sandbox management. A Node runtime host installs the official `@deepseek-ai/dsh-sdk-minimal` profile and KnowWork's own plugin bundle; the bundle disables local filesystem/shell and the upstream SDK's stdio server, adds an HTTP session adapter, remote filesystem/subprocess calls, model gateway, skill/tool bridge, session policy, subagent-policy inheritance and completion gates. `ctx.agents.create`/`resume` and `agent.followup`/`steer` are calls into the *installed DSH runtime*, not a separately written KnowWork language-model loop. [Profile](https://github.com/knowflow-ai/KnowWork/blob/83c763e4fe2d63cd59e0344268afa94321d35585/runtime-host/profile/package.json), [plugin graph](https://github.com/knowflow-ai/KnowWork/blob/83c763e4fe2d63cd59e0344268afa94321d35585/runtime-host/plugins/host-bundle/cordis.patch.yml), [adapter](https://github.com/knowflow-ai/KnowWork/blob/83c763e4fe2d63cd59e0344268afa94321d35585/runtime-host/plugins/dsh-host/src/http-host.mjs#L190-L260).

Each sandbox-enabled conversation's commands and file actions are sent through KnowWork's business service to a Docker container named and labeled by `(workspace_id, session_id)`. Container creation refuses a pre-existing name whose labels do not match, and accesses are routed by this same key. The official DSH subagent implementation is configured and child sessions inherit root restrictions and approval routing. The separate workflow engine follows a frozen, author-supplied ordered step plan and can call a bounded DSH agent step; its scheduling, schemas, retry limits and approval steps are deterministic. [Sandbox key/manager](https://github.com/knowflow-ai/KnowWork/blob/83c763e4fe2d63cd59e0344268afa94321d35585/server/src/knowwork_server/sandbox/containers.py#L37-L202), [child policy](https://github.com/knowflow-ai/KnowWork/blob/83c763e4fe2d63cd59e0344268afa94321d35585/runtime-host/plugins/dsh-host/src/subagent-policy.mjs#L1-L57), [workflow engine](https://github.com/knowflow-ai/KnowWork/blob/83c763e4fe2d63cd59e0344268afa94321d35585/server/src/knowwork_server/workflows/engine.py#L1-L218).

## Operational model

An operator configures a model and grants tools. A user starts a session; KnowWork instantiates an operational DSH-backed agent, constrains its usable tools, forwards model requests through its gateway and sends every command/file action into the matching session sandbox. Within those constraints the installed model-backed agent selects tools, reads the resulting observations and continues work; the operational S1 is the *composed deployed actor*. Multiple S1 sessions can execute concurrently; first-party namespace and container ownership controls suppress their collision and cross-tenant file/workspace interference. No first-party agent or operator-facing procedure was found that governs the whole population's present commitments, independently audits management claims, models prospective environmental capability changes or settles deployment-level ultimate identity policy as VSM functions.

## S1 — Operations

- State: A
- Function: Complete workspace users' open-ended information, document and tool tasks within an enterprise-controlled environment.
- Disturbance / variety regulated: Ambiguous user requests, unfamiliar document content, unavailable files/tools, tool errors, and the need to select subsequent actions from previous observations.
- Decisive decision or feedback right: The configured model-backed DSH agent decides the next task-specific tool invocation, follow-up and stopping behaviour; KnowWork's first-party runtime host constructs the real session and installs its usable tools, prompt, gateway and observation transport.
- Decision owner: The installed composite DSH model-backed actor for task decisions; upstream DSH supplies the general agent loop, while KnowWork supplies the first-party deployed composition and enterprise execution world. Neither the external inference provider nor KnowWork's deterministic permission service alone owns the task decisions.
- Supporting / enforcement mechanisms: Shipped DSH profile and plugins, `ctx.agents` adapter, model gateway, session state, remote shell/filesystem, business tool bridge, task/turn events, policy deny rules, user approval and Docker sandboxes.
- Closure path: User turn → KnowWork runtime invokes active DSH agent → model chooses tool or response → KnowWork-owned tool bridge/sandbox returns actual result → DSH history/loop presents that observation to the model → subsequent model action or completion. A workflow agent step likewise feeds its returned answer through schema checking and optional constrained retry.
- Boundary reachability: `runtime-host/profile/package.json` loads both official DSH SDK and first-party host bundle; the shipped HTTP host opens sessions and calls `followup`/`steer` on real agent objects; the README's standard self-hosted setup exposes these paths to users.
- Why this is / is not agent-owned: The next open-ended task/tool choice is model-directed, not a fixed program or an administrator's prescribed step; attribution is expressly limited to the *composed first-party deployment*, not claimed as a separately authored DSH model loop.
- Evidence: [standard product boundary](https://github.com/knowflow-ai/KnowWork/blob/83c763e4fe2d63cd59e0344268afa94321d35585/README_en.md#L96-L180); [profile bundles](https://github.com/knowflow-ai/KnowWork/blob/83c763e4fe2d63cd59e0344268afa94321d35585/runtime-host/profile/package.json#L1-L13); [session creation and action delivery](https://github.com/knowflow-ai/KnowWork/blob/83c763e4fe2d63cd59e0344268afa94321d35585/runtime-host/plugins/dsh-host/src/http-host.mjs#L193-L260); [first-party tool backend replacement](https://github.com/knowflow-ai/KnowWork/blob/83c763e4fe2d63cd59e0344268afa94321d35585/runtime-host/plugins/host-bundle/cordis.patch.yml#L15-L90).
- Basis: Shipped first-party integration code, DSH package/profile manifests and source-level agent-session feedback wiring, not live model execution or business-outcome evaluation.
- Confidence: High that a configurable autonomous actor is actually installed; medium on precise outcome behaviour of the upstream DSH package, which is external to this frozen source.
- Caveats: First-party ownership means a deployable composite S1; it must not be misreported as an independently implemented or self-trained agent core. The model endpoint is external or operator-supplied, and no live LLM was invoked.

## S2 — Coordination

- State: C
- Function: Attenuate concrete cross-session workspace/file-state interference among distinct simultaneously running operational S1s in the sandbox-enabled standard deployment.
- Disturbance / variety regulated: Distinct user-session agents could otherwise alias a working directory, collide on a container name, manipulate each other's files or allow one tenant's lifecycle request to seize another session's sandbox.
- Distinct S1 units: Independently instantiated DSH-backed user sessions with individual session IDs, conversation states, task loops and tool-execution contexts.
- Inter-S1 disturbance: Shared Docker host and business service serve multiple agents, whose shell/filesystem actions require isolation to avoid destructive concurrent interference and unauthorized cross-session access.
- Attenuating coordination relation: A deterministic `SandboxKey(workspace_id, session_id)` hashes each identity into a unique container name and ownership label, and `ContainerManager` refuses an existing name whose labels do not match. Every remote filesystem/subprocess invocation addresses the corresponding session's container and workspace.
- Feedback into subsequent S1 behaviour: Container lookup routes further tool actions back to the original isolated execution world; non-matching label/name collisions are refused instead of silently connecting to another S1's files. An agent therefore observes and continues within its own workspace, or receives a conflict/failure rather than taking over a sibling's state.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The concrete relation is isolation against **interference of concurrently operating S1 file/tool actions**—not merely passing messages or ordering a single workflow. It is narrower than arbitration over shared project deliverables, agent negotiation or whole-deployment resource prioritization.
- Decisive decision or feedback right: Determine which sandbox state belongs to each live S1, and reject cross-identity adoption while preserving successive tool calls' same-session continuity.
- Decision owner: KnowWork's deterministic sandbox constructor/manager; there is no agent-owned S2 coordination discretion or supported S2 parent mode.
- Supporting / enforcement mechanisms: Per-(workspace, session) key/hash, Docker labels, per-key locks, busy handles, session-scoped remote tools and namespace check before container adoption.
- Closure path: Two concurrent session requests → distinct scoped sandbox keys → separate containers and tool paths; same key resumes its own container, while a label mismatch refuses adoption → each S1's subsequent work observes its own results.
- Boundary reachability: The default documented deployment enables per-session Docker sandboxes and the runtime-host profile substitutes KnowWork remote fs/subprocess; `DockerSessionSandbox` obtains each command's container via the same key. `--no-sandbox` does **not** receive this S2 credit.
- Why this is / is not agent-owned: The cross-S1 relation materially limits interaction and routes subsequent behaviour, but it is a fixed constructor and namespace guard—not an autonomous agent scheduling or resolving resource conflicts.
- Evidence: [container key and labels](https://github.com/knowflow-ai/KnowWork/blob/83c763e4fe2d63cd59e0344268afa94321d35585/server/src/knowwork_server/sandbox/containers.py#L37-L95); [scoped acquisition and collision rejection](https://github.com/knowflow-ai/KnowWork/blob/83c763e4fe2d63cd59e0344268afa94321d35585/server/src/knowwork_server/sandbox/containers.py#L117-L202); [tool invocation through scoped key](https://github.com/knowflow-ai/KnowWork/blob/83c763e4fe2d63cd59e0344268afa94321d35585/server/src/knowwork_server/sandbox/docker_sandbox.py#L126-L175); [documented sandbox default and opt-out](https://github.com/knowflow-ai/KnowWork/blob/83c763e4fe2d63cd59e0344268afa94321d35585/README_en.md#L96-L126).
- Basis: Direct first-party implemented identity/ownership guards and standard configuration; no cross-tenant Docker isolation claim was verified with a live container.
- Confidence: High for implemented namespace and label checks; operational Docker guarantees were not penetration-tested.
- Caveats: Does not credit tenant permissions as S2 judgment; does not imply cross-agent negotiation, S3 management, or security proof against container/daemon compromise. The README explicitly warns that mounting Docker socket on the server has host-root implications.

## S3 — Inside-and-now control

- State: —
- Function: No first-party whole-current managerial decision over the concurrent S1 portfolio is established; individual session/user/workflow control remains local or externally chosen.
- Disturbance / variety regulated: System-wide priority disputes, work reassignment, shared resource trade-offs and intervention across S1s are not substantively regulated by a decision-owning S3 shown in this release.
- Decisive decision or feedback right: Not established. The workflow engine follows the author's frozen step order and fails/pauses/resumes deterministically; workspace administrators and users approve or cancel their own operations without a whole-deployment management loop.
- Decision owner: None established at the chosen recursion; task decisions belong to individual DSH S1s and higher-level priorities to external users/admins.
- Supporting / enforcement mechanisms: Sequential workflow state machine, heartbeat/lease, per-user conversation queue, subagent parent events, session limits, audit records and manual cancel/approval.
- Closure path: Local retry/approval/status paths return to their respective session or author-defined workflow, but no source path shows an accountable whole-portfolio view selecting and returning changed commitments among multiple S1s.
- Why this is / is not agent-owned: Deterministic workflow progression is not autonomous whole-system management, and per-session DSH child delegation is inside an operational S1 task rather than a metasystem for the enterprise deployment.
- Evidence: [workflow state engine and frozen plan](https://github.com/knowflow-ai/KnowWork/blob/83c763e4fe2d63cd59e0344268afa94321d35585/server/src/knowwork_server/workflows/engine.py#L1-L218); [agent step stays scoped to a run](https://github.com/knowflow-ai/KnowWork/blob/83c763e4fe2d63cd59e0344268afa94321d35585/server/src/knowwork_server/workflows/agent.py#L72-L170); [host lifecycle](https://github.com/knowflow-ai/KnowWork/blob/83c763e4fe2d63cd59e0344268afa94321d35585/runtime-host/plugins/dsh-host/src/http-host.mjs#L180-L287).
- Basis: Negative finding bounded by shipped runtime and management surfaces.
- Confidence: Medium-high.
- Caveats: This does not deny that a deploying enterprise may have its own managers; such management is outside the assessed KnowWork runtime.

### Absence scope

- Surfaces inspected: Workflow engine/agent steps, business-server session control, DSH host lifecycle, tool and subagent policy, published system overview.
- Plausible first-party paths checked: Workflow-level next-step driver, subagent delegation/parent conversations, per-session approvals/cancellations, Docker resource regulation, and admin controls.
- Why no material first-party path remains: None of those routes observes the enterprise deployment's competing S1 commitments and exercises a first-party whole-current steering/reallocation decision; they enforce a fixed plan, local policy or individual user's task choice.

## S3* — Complementary audit

- State: —
- Function: No established complementary, sufficiently independent audit that challenges a metasystem claim via an alternative observation route and feeds that finding into whole-current control.
- Disturbance / variety regulated: False completion/quality claims and misleading aggregate state could motivate S3* audit, but routine event logging, user-visible replay and completion checking do not establish that distinct audit function.
- Decisive decision or feedback right: Not established at S3* level. A required-tool gate can detect missing successful tool calls and steer/reject completion; it checks a predetermined task constraint in the ordinary turn path rather than independently auditing whole-system reality.
- Decision owner: The gate is a fixed KnowWork plugin; audit trail viewers and ordinary end-user approvals do not become independent metasystem auditors merely through human observation.
- Supporting / enforcement mechanisms: Agent/tool event sinks, searchable run history, audit logs, replay views, deterministic schema checker and success-tool completion gate.
- Closure path: Missing required tool → plugin sends steering text or marks a turn failed, which is local QA. No independent audit observation of S3/S1 aggregate performance → S3 decision → changed cross-unit regulation is evidenced.
- Why this is / is not agent-owned: Tool-success events are recorded outside the model but the gate is a mandatory production completion rule, not a separately commissioned independent auditor of operational claims.
- Evidence: [completion gate](https://github.com/knowflow-ai/KnowWork/blob/83c763e4fe2d63cd59e0344268afa94321d35585/runtime-host/plugins/dsh-host/src/skill-gate.mjs#L1-L96); [replay/audit surface](https://github.com/knowflow-ai/KnowWork/blob/83c763e4fe2d63cd59e0344268afa94321d35585/README_en.md#L54-L83); [workflow JSON schema](https://github.com/knowflow-ai/KnowWork/blob/83c763e4fe2d63cd59e0344268afa94321d35585/server/src/knowwork_server/workflows/agent.py#L35-L130).
- Basis: Negative assessment of independent observation and decision-return boundary, not a claim that logs/gates are useless.
- Confidence: Medium-high.
- Caveats: A deployment could add a separate human audit process, but such an external process is not established as a first-party supported S3* function here.

### Absence scope

- Surfaces inspected: Audit/event source modules, runtime event forwarding, replay documentation, skill-gate code, approval flow and workflow-schema validations.
- Plausible first-party paths checked: Tool receipt checks, admin audit logs, conversation replay, completion-tool nudges, and schema validation of workflow agent responses.
- Why no material first-party path remains: These are ordinary execution receipts or local quality/permission gates; no alternate independent review of a metasystem's account of S1 activity is operationally coupled to subsequent deployment-wide control.

## S4 — Outside-and-then intelligence

- State: —
- Function: No first-party prospective environmental sensing → adaptation-option selection → installed future capability feedback loop is established.
- Disturbance / variety regulated: Changes to employee needs, external models, tool ecosystems and compliance obligations can be accommodated through administrator changes, but no S4-specific system models those changes and closes a capability adaptation decision.
- Decisive decision or feedback right: Not established. Users/admins install/publish skills, configure models and tools, or manually upgrade DSH; no shipped owner evaluates external future conditions and adopts a strategy based on that evaluation.
- Decision owner: External human administrators/developers control configuration and releases, without a first-party closed parent-mode prospective adaptation procedure.
- Supporting / enforcement mechanisms: Skill catalogue, version publication, model gateway configuration, dynamic grants, DSH upgrade preflight and dependency pins.
- Closure path: Manual config can change later S1 affordances, but source does not tie it to an external-prospect intelligence path and accountable adoption feedback to current control.
- Why this is / is not agent-owned: Flexible tooling, uploaded skills and runtime upgrades provide adaptation *mechanisms* but not the required outside-and-then decision function.
- Evidence: [skills and versioning](https://github.com/knowflow-ai/KnowWork/blob/83c763e4fe2d63cd59e0344268afa94321d35585/README_en.md#L68-L97); [DSH upgrade policy](https://github.com/knowflow-ai/KnowWork/blob/83c763e4fe2d63cd59e0344268afa94321d35585/README_en.md#L161-L190); [skill provider/host graph](https://github.com/knowflow-ai/KnowWork/blob/83c763e4fe2d63cd59e0344268afa94321d35585/runtime-host/plugins/host-bundle/cordis.patch.yml#L175-L201).
- Basis: Bounded negative finding for shipped standard operational flow.
- Confidence: Medium-high.
- Caveats: Admin-driven tool adoption in a real enterprise could be part of that enterprise's S4; KnowWork alone does not own its external sensing or future strategy.

### Absence scope

- Surfaces inspected: Profile bundles, README architecture, model/skill configuration, skill publish operations, DSH upgrade preflight and workflow engine.
- Plausible first-party paths checked: Tool/skill publication, model-provider switching, policy grants, quick-answer routing and developer dependency-upgrade checks.
- Why no material first-party path remains: These are user/admin-configured affordances, local task modes or maintenance compatibility tests, with no evidence-backed sensing of future relevant change, comparative option development and selection into ongoing S1 capability.

## S5 — Identity and ultimate policy

- State: —
- Function: No first-party ultimate organizational identity/ethos decision path closes conflicts between current operations and future change at the assessed KnowWork deployment recursion.
- Disturbance / variety regulated: Scope-of-business, enduring purpose and tension between S3/S4 would require an ultimate authority; the shipped permission system handles access and task safety but does not make those identity-level decisions.
- Decisive decision or feedback right: Not established. Workspace admins grant/revoke access and users approve high-risk calls; these rights concern operational authorization, not identity or ultimate policy of the whole viable organization.
- Decision owner: Enterprise principals have external ultimate authority; KnowWork's own policy engine only enforces the configured grants and does not decide the organization's final identity.
- Supporting / enforcement mechanisms: Casbin deny-by-default permission checks, organization hierarchy, access grants, session approval and auditing.
- Closure path: Admin-granted resource permissions return to future sessions through deterministic enforcement, but no identity/ultimate-policy issue escalation to legitimate authority and policy settlement back into S3/S4 exists within the assessed distribution.
- Why this is / is not agent-owned: The name “policy engine” describes access enforcement; neither RBAC nor final approval of a user tool action is S5 by itself.
- Evidence: [Casbin enforcement](https://github.com/knowflow-ai/KnowWork/blob/83c763e4fe2d63cd59e0344268afa94321d35585/server/src/knowwork_server/access/engine.py#L1-L193); [enterprise permissions description](https://github.com/knowflow-ai/KnowWork/blob/83c763e4fe2d63cd59e0344268afa94321d35585/README_en.md#L34-L61); [admin grants](https://github.com/knowflow-ai/KnowWork/blob/83c763e4fe2d63cd59e0344268afa94321d35585/README_en.md#L190-L225).
- Basis: Bounded negative source review of authority level and return path.
- Confidence: High for distinction between first-party resource enforcement and ultimate identity authority; no claim about external enterprise governance.
- Caveats: Enterprise management could supply S5 at a higher recursion if assessed together with its governance, but that is not KnowWork's first-party standard distribution.

### Absence scope

- Surfaces inspected: Account/organization/role/grant service and Casbin engine, tool approval broker, system architecture, workflow administrative surfaces and DSH host configuration.
- Plausible first-party paths checked: Department hierarchy, policies for models/skills/tools, human approval and administrator brand/system-name configuration.
- Why no material first-party path remains: The code encodes resource authorization and operator choices, with no first-party identity-conflict agenda, authoritative final settlement or S3/S4 policy feedback loop; organizational policy authority is external.

## Summary and evidence gaps

| Function | S1 | S2 | S3 | S3* | S4 | S5 |
| --- | --- | --- | --- | --- | --- | --- |
| State | A | C | — | — | — | — |

The relevant distinction from a standalone upstream DSH agent is a deployable enterprise **composed S1** plus bounded deterministic **S2 session-sandbox collision attenuation**. RBAC, approvals, audit logs, skill management and workflows are meaningful product features without automatically establishing S3/S3*/S4/S5 governance. The primary unresolved *operational effectiveness* questions are Docker/provider behavior under real workload and users' business outcomes; these have not been converted into `?` ownership symbols because the inspected code sufficiently bounds the claimed functions.

Validation boundary: Static inspection of the exact frozen source and package/profile wiring. No live LLM, provider, browser, Docker agent or assistant loop was launched, and no comparative agent performance was measured. The standalone assessment is proposed for review, not yet an admitted canonical classification.

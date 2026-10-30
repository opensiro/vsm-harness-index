---
harness_id: openshift-agent-control-plane
project_name: OpenShift Agent Control Plane
repository: https://github.com/openshift-online/agent-control-plane
review_ref: 9d7246cb467b3e4d4060bff760b6256f6a368a50
reviewed_at: 2026-10-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: P
---

# OpenShift Agent Control Plane

## Review boundary

- System in focus: one deployed ACP platform comprising tenant projects, configured agents and independently executing sandbox sessions, its API server, first-party reconciliation, scheduler, runner and parent administration.
- Purpose and identity: securely host project-scoped autonomous AI-agent sessions, marshal project inputs and credentials, and operate a managed multi-tenant agent fleet.
- Relevant environment: project teams, external Git repositories and issue trackers, external model providers, Kubernetes/OpenShell, identity providers, schedules and resource isolation requirements.
- Standard-distribution boundary: shipped Go API services and control-plane reconcilers, Python agent runners and bridge adapters, the first-party UI/CLI/MCP surfaces and declarative project/agent/schedule configuration. Deployment requires external Kubernetes/OpenShell, identity and model services; these are dependencies, not credited autonomous owners.
- Credited operating / distribution surfaces: `components/ambient-api-server/plugins/{agents,sessions,scheduledSessions,projects,policies}`, `components/ambient-control-plane/internal/reconciler/`, `components/runners/ambient-runner/`, `components/ambient-mcp/tools/`, shipped manifests and documented operator flows.
- Adjacent first-party surfaces excluded from ownership: `examples/vteam-catalog/` (illustrative teams, not guaranteed deployed organizational decisions), `tests/`, docs/spec plans, GitHub CI, contributor governance and the user's own external model/Kubernetes organizations. Their presence does not automatically close platform S2/S3*/S4/S5.
- First-party operating / deployment modes considered: on-demand and scheduled session starts; Claude bridge and alternative runner bridges; project-owner/operator changes via API/CLI/UI/GitOps; optional first-party MCP server. The scheduler's `skip`/`allow` overlap modes are distinguished.
- Recursion level: the ACP tenant-project operating organization whose S1 cells are independently executing sandbox sessions; an individual model/agent loop is one lower-level S1 cell. Cross-tenant ACP infrastructure is a supporting higher-level platform, not a single shared autonomous agent.
- Reviewed revision: `openshift-online/agent-control-plane@9d7246cb467b3e4d4060bff760b6256f6a368a50` (frozen batch #2393 row 2; repository source checked out exactly at that SHA).
- Observation date: 2026-10-30.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

Evidence links below all refer to this [immutable reviewed tree](https://github.com/openshift-online/agent-control-plane/tree/9d7246cb467b3e4d4060bff760b6256f6a368a50). Source execution was not performed: this is a first-party code/configuration assessment, not a live provider-backed E2E.

## Repository architecture

The [README](https://github.com/openshift-online/agent-control-plane/blob/9d7246cb467b3e4d4060bff760b6256f6a368a50/README.md) identifies projects as isolated tenants, agents as project-bound configurations, sessions as separate agent runs, OpenShell sandboxes, credentials, a Go API server, Go control plane, Python runner, MCP tools and scheduled sessions. The API stores domain objects, the control plane turns session state into sandbox runs and assembles initial prompts, and the runner routes AG-UI requests to bridge-specific model agents. This is a real deployed runtime architecture, not only a framework sketch.

The [run endpoint](https://github.com/openshift-online/agent-control-plane/blob/9d7246cb467b3e4d4060bff760b6256f6a368a50/components/runners/ambient-runner/ambient_runner/endpoints/run.py) passes the run to the selected bridge, streams model/tool events and reports errors. The [Claude bridge](https://github.com/openshift-online/agent-control-plane/blob/9d7246cb467b3e4d4060bff760b6256f6a368a50/components/runners/ambient-runner/ambient_runner/bridges/claude/bridge.py) creates/resumes a worker, executes the agent query, streams events, and handles interrupts/halting. The model provider owns generation inside S1; ACP owns the surrounding session boundary.

The [schedule service](https://github.com/openshift-online/agent-control-plane/blob/9d7246cb467b3e4d4060bff760b6256f6a368a50/components/ambient-api-server/plugins/scheduledSessions/service.go) checks the schedule creator's RBAC, skips a new run if a prior run for the *same schedule* remains active under `overlap_policy=skip`, and creates a new session otherwise. The [application reconciler](https://github.com/openshift-online/agent-control-plane/blob/9d7246cb467b3e4d4060bff760b6256f6a368a50/components/ambient-control-plane/internal/reconciler/application_reconciler.go) applies operator-selected Git declarations into platform state. Neither deterministic code path supplies an autonomous strategic/regulatory judgment by itself.

## Operational model

An authorized user or scheduler selects a configured agent and creates a session. The platform provisions an isolated execution environment and assembles the project-level prompt, agent-specific prompt, unread inbox and session input; the actual agent decides which permitted tool/model actions to perform. The event stream and session state return to the project. Operators choose project policy, agent configuration, credentials, schedules and GitOps desired state; reconcilers enforce those choices. First-party optional MCP tools allow an agent to manipulate permitted platform resources, but do not themselves establish an autonomous whole-project governance loop in the default mode.

The [initial prompt composition](https://github.com/openshift-online/agent-control-plane/blob/9d7246cb467b3e4d4060bff760b6256f6a368a50/components/ambient-control-plane/internal/reconciler/kube_reconciler.go) in `assembleInitialPrompt` shows return to later work from project `Prompt`, agent `Prompt`, unread inbox and the particular session prompt. The [agent MCP tools](https://github.com/openshift-online/agent-control-plane/blob/9d7246cb467b3e4d4060bff760b6256f6a368a50/components/ambient-mcp/tools/agents.go) expose bounded list/get/create/update/annotation operations through authenticated platform APIs; tool availability and authority remain deployment-dependent.

## S1 — Operations

- State: A
- Function: independently executing agent session cells produce project outcomes against their respective task environments.
- Disturbance / variety regulated: changing task content, external systems, tool results, model outputs, conversation continuation and human messages.
- Decisive decision or feedback right: decide the next response and authorized tool use within an active session.
- Decision owner: the selected autonomous model agent through the runner bridge, not the deterministic API or reconciler.
- Supporting / enforcement mechanisms: Python runner, AG-UI stream, model bridge, isolated OpenShell sandbox, credentials, API event store and session lifecycle.
- Closure path: session inputs and assembled prompt → bridge worker query/tool actions → event results and optional subsequent turns, with persisted session context.
- Boundary reachability: first-party run endpoint calls `bridge.run`, Claude bridge calls live session worker `query`, and the platform deploys this runner in provisioned sandboxes; external provider service supplies model inference, not a separately credited ACP management function.
- Why this is / is not agent-owned: the AI worker exercises local task/tool discretion; sessions are not merely metadata records.
- Evidence: [run endpoint](https://github.com/openshift-online/agent-control-plane/blob/9d7246cb467b3e4d4060bff760b6256f6a368a50/components/runners/ambient-runner/ambient_runner/endpoints/run.py), [Claude bridge](https://github.com/openshift-online/agent-control-plane/blob/9d7246cb467b3e4d4060bff760b6256f6a368a50/components/runners/ambient-runner/ambient_runner/bridges/claude/bridge.py), [runner architecture](https://github.com/openshift-online/agent-control-plane/blob/9d7246cb467b3e4d4060bff760b6256f6a368a50/components/runners/ambient-runner/README.md).
- Basis: first-party source inspection at pinned ref.
- Confidence: high for a supported provider-configured mode.
- Caveats: ACP cannot execute agents without an external model provider and infrastructure; local judgement belongs to the deployed model-backed worker, not the platform's Go controller.

## S2 — Coordination

- State: C
- Function: attenuate a concrete overlap collision between independently triggered session-run S1 cells from the same schedule.
- Disturbance / variety regulated: a recurring trigger arrives while a prior instance is still active, risking overlapping work against the same agent/task/external resource.
- Distinct S1 units: the still-running sandbox session and the separately triggered would-be session instance, each a distinct run cell even though they share an agent definition. These are not claimed to be two different configured agents.
- Inter-S1 disturbance: duplicate live execution of a recurring job before the earlier instance completes.
- Attenuating coordination relation: schedule-level `overlap_policy=skip` queries `ActiveByScheduledSessionID` and declines the overlapping session creation; `allow` explicitly disables the attenuation.
- Feedback into subsequent S1 behaviour: skip returns without creating the competing session; after the active session exits, a subsequent scheduled trigger can create the next run.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the tested relation is a concrete conflict between successive operational run instances, not just a queue. It is only schedule-local; there is no asserted project-wide inter-agent allocation or negotiation.
- Decisive decision or feedback right: select overlap policy and resolve the detected conflict by suppressing a run.
- Decision owner: first-party deterministic schedule-service primitive enforces a policy chosen by the schedule owner; the autonomous agents do not autonomously choose/revise the S2 policy. This is classified as constructor-level C, not A.
- Supporting / enforcement mechanisms: active-session lookup, scheduler triggers, session creation API and schedule settings.
- Closure path: authorized schedule owner selects `skip` → scheduler checks active run → suppresses overlapping run; later triggers apply the same choice.
- Boundary reachability: the shipped `createSessionFromSchedule` is invoked for actual scheduler triggers and checks both RBAC and overlap before creating a session.
- Why this is / is not agent-owned: S2-specific attenuation is operational, but the agent owns neither overlap response policy nor the scheduler.
- Evidence: [scheduled session service](https://github.com/openshift-online/agent-control-plane/blob/9d7246cb467b3e4d4060bff760b6256f6a368a50/components/ambient-api-server/plugins/scheduledSessions/service.go), [overlap tests](https://github.com/openshift-online/agent-control-plane/blob/9d7246cb467b3e4d4060bff760b6256f6a368a50/components/ambient-api-server/plugins/scheduledSessions/scheduler_test.go), [schedule model](https://github.com/openshift-online/agent-control-plane/blob/9d7246cb467b3e4d4060bff760b6256f6a368a50/components/ambient-api-server/plugins/scheduledSessions/model.go).
- Basis: structural collision/attenuation/return test, not multi-agent-message inference.
- Confidence: moderate; narrow to overlapping independent session instances of one schedule.
- Caveats: if an assessment boundary requires distinct *configured agents* rather than distinct independently executing S1 runs, this is not evidence for that broader S2; project inbox, prompts and multi-agent examples are not independently promoted to S2.

## S3 — Inside-and-now control

- State: P
- Function: parent-owned current control of the tenant project agent fleet and current operational commitments.
- Disturbance / variety regulated: which agents, permissions, schedules, providers and deployments are allowed to consume project resources and execute work at this time.
- Whole-system current view: project-scoped agent/session/schedule records, operator API and UI, current application sync/health state.
- Current-control decision scope: choose/create/update agent definitions, suspend/resume schedules, configure project resources and submit GitOps desired state.
- Decisive decision or feedback right: change fleet configuration and active schedule commitments for the project.
- Decision owner: authorized project owner/platform operator in the parent-controlled mode; Go reconcilers and API authorization execute decisions, not choose the organizational priority.
- Supporting / enforcement mechanisms: agent/schedule/project services, RBAC evaluator, GitOps application reconciler, Kubernetes/OpenShell provisioner and operator CLI/UI.
- Closure path: authorized operator updates project/agent/schedule or Git declaration → API persists/reconciler applies desired state → later session creation and execution adopt changed configuration or are denied/skipped.
- Boundary reachability: the first-party API and reconciliation code are deployed control paths, with `suspend/resume`, RBAC and application reconciliation implemented. This is not merely a docs proposal.
- Why this is / is not agent-owned: available MCP API mutations can be composed into an autonomous control policy, but source evidence does not establish a first-party agent holding the project-wide current-control right and closing such a policy in the standard mode. Therefore P, not A(P) or C(P).
- Evidence: [schedule service](https://github.com/openshift-online/agent-control-plane/blob/9d7246cb467b3e4d4060bff760b6256f6a368a50/components/ambient-api-server/plugins/scheduledSessions/service.go), [application reconciler](https://github.com/openshift-online/agent-control-plane/blob/9d7246cb467b3e4d4060bff760b6256f6a368a50/components/ambient-control-plane/internal/reconciler/application_reconciler.go), [agent API/MCP](https://github.com/openshift-online/agent-control-plane/blob/9d7246cb467b3e4d4060bff760b6256f6a368a50/components/ambient-mcp/tools/agents.go), [README platform model](https://github.com/openshift-online/agent-control-plane/blob/9d7246cb467b3e4d4060bff760b6256f6a368a50/README.md).
- Basis: specific parent current-control decision and return path.
- Confidence: moderate-high for P, no autonomous S3 ownership inferred.
- Caveats: deterministic enforcement is not the S3 decision owner; a simple delegation API or single-session interruption is insufficient alone.

## S3* — Complementary audit

- State: —
- Function: no materially independent supplementary audit of operational reality established in the reviewed deployed project mode.
- Disturbance / variety regulated: unverifiable or misleading routine agent/session reports would require distinct raw evidence access.
- Decisive decision or feedback right: no shipped separate complementary audit verdict and feedback path found.
- Decision owner: not established.
- Supporting / enforcement mechanisms: session events, tool-call logs, MLflow tracing and API status are useful observability, not independent verification.
- Closure path: no independent audit-to-current-control return identified.
- Why this is / is not agent-owned: model evaluation or external auditors are not automatically shipped members of a given tenant project.
- Evidence: [README observability](https://github.com/openshift-online/agent-control-plane/blob/9d7246cb467b3e4d4060bff760b6256f6a368a50/README.md), [runner tracing](https://github.com/openshift-online/agent-control-plane/blob/9d7246cb467b3e4d4060bff760b6256f6a368a50/components/runners/ambient-runner/ambient_runner/middleware/tracing.py), [session event service](https://github.com/openshift-online/agent-control-plane/blob/9d7246cb467b3e4d4060bff760b6256f6a368a50/components/ambient-api-server/plugins/sessions/event_service.go).
- Basis: negative-state scoped to standard runtime.
- Confidence: moderate.
- Caveats: first-party example PR reviewers/test suites do not close a complementary audit for arbitrary tenant operations.

### Absence scope

- Surfaces inspected: control-plane reconciliation, runner execution/tracing, API session events, example reviewers, docs on observability, unit/e2e tests.
- Plausible first-party paths checked: independent raw-artifact sampling, separate auditor authority, model-output challenge feedback and direct audit-to-operator control.
- Why no material first-party path remains: standard deployed platform records the session's own events and exposes them to users, without a separately wired, sufficiently independent reviewer that can challenge those reports and feed an audit verdict into subsequent project regulation; optional example users may build one externally.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party project-level environmental forecasting/options-generation loop that returns into current capability is established.
- Disturbance / variety regulated: external changes in requirements, APIs, model capabilities and security threats could demand future adaptation; these inputs are supplied through project operators or individual S1 prompts.
- Decisive decision or feedback right: no shipped autonomous or parent-closed prospectively modeling/adapting project capability function beyond manual configuration is identified.
- Decision owner: none established for S4 in scope.
- Supporting / enforcement mechanisms: GitOps sync applies already-chosen declarations; agent scheduling and prompts drive current work.
- Closure path: no external-prospective option→S3 capability-change feedback loop; configuration sync alone is present-time control.
- Why this is / is not agent-owned: an agent can research as its S1 task, but research output is not automatically an S4 loop for its hosting project organization.
- Evidence: [application reconciler](https://github.com/openshift-online/agent-control-plane/blob/9d7246cb467b3e4d4060bff760b6256f6a368a50/components/ambient-control-plane/internal/reconciler/application_reconciler.go), [README GitOps](https://github.com/openshift-online/agent-control-plane/blob/9d7246cb467b3e4d4060bff760b6256f6a368a50/README.md), [example vTeam](https://github.com/openshift-online/agent-control-plane/tree/9d7246cb467b3e4d4060bff760b6256f6a368a50/examples/vteam-catalog).
- Basis: negative-state scoped to supported project runtime.
- Confidence: moderate.
- Caveats: future-oriented examples and repository roadmaps are adjacent intentions, not automatically deployed organizational capability adaptation.

### Absence scope

- Surfaces inspected: first-party control plane, runner bridges, GitOps application sync, project/agent/schedule APIs, shipped examples, docs/specs and tests.
- Plausible first-party paths checked: model/tool environment scanning, prospective option generation, project-level adaptation decision, and option return to fleet capabilities/constraints.
- Why no material first-party path remains: reconciler applies a human-selected desired-state repository but does not discover or choose future adaptation options; no standard project-level autonomous or parent-governed prospective S4 cycle is wired into operations.

## S5 — Policy and identity

- State: P
- Function: parent-established tenant/project identity, operating instructions and ultimate access-policy boundaries.
- Disturbance / variety regulated: project identity and normative instructions, permitted actor access, sandbox policy and legitimate policy changes that must bind later agent runs.
- Identity / ultimate-policy issue: what project a team is operating, which instructions and credentials it authorizes, who may execute or change agents and schedules.
- Ultimate authority in each claimed mode: authenticated project/platform operator and administrators through RBAC, project/agent configuration and policy APIs; no demonstrated independent AI agent with authority to rewrite the project's ultimate identity.
- Return-to-operation path: authorized parent changes project prompt, agent/policy settings or RBAC → API persists them → `assembleInitialPrompt` injects project instruction into subsequent sessions and access/authorization code applies configuration to later operations.
- Decisive decision or feedback right: define and revise the project-level operating/identity boundary, rather than simply approving one output.
- Decision owner: legitimate human/institutional parent authority in the deployed platform mode.
- Supporting / enforcement mechanisms: projects and policy services, role bindings and RBAC, sandbox policy enforcement, prompt assembly and GitOps.
- Closure path: parent project decision → first-party API/GitOps persistence → next run receives governing prompt and sandbox/credential permissions.
- Boundary reachability: the deployed project configuration is looked up directly by the Kubernetes session reconciler during actual initial prompt assembly; policies and role bindings are shipped API resources, not repository governance documents.
- Why this is / is not agent-owned: the model agent can obey or act within these policy limits but is not the ultimate policy authority; P specifically records parent closure, not a static prompt mislabeled as autonomous S5.
- Evidence: [project model](https://github.com/openshift-online/agent-control-plane/blob/9d7246cb467b3e4d4060bff760b6256f6a368a50/components/ambient-api-server/plugins/projects/model.go), [policies service](https://github.com/openshift-online/agent-control-plane/blob/9d7246cb467b3e4d4060bff760b6256f6a368a50/components/ambient-api-server/plugins/policies/service.go), [prompt assembly](https://github.com/openshift-online/agent-control-plane/blob/9d7246cb467b3e4d4060bff760b6256f6a368a50/components/ambient-control-plane/internal/reconciler/kube_reconciler.go), [RBAC schedule check](https://github.com/openshift-online/agent-control-plane/blob/9d7246cb467b3e4d4060bff760b6256f6a368a50/components/ambient-api-server/plugins/scheduledSessions/service.go).
- Basis: parent issue/decision/return path, bounded to tenant identity and policy.
- Confidence: moderate.
- Caveats: ordinary pause/approval of a task is S3, not S5; parent S5 rests on stable project identity/instructions and legitimate resource authority that govern later runs.

## Distributed OSS parent arrangement

This is a multi-tenant deployment product. Independent upstream OSS contributors and example vTeams do not jointly constitute the tenant project's parent authority; the applicable parent is each deployment's authenticated project/platform operator. Nothing in this classification imports the maintainer GitHub organization, example swarms or Red Hat as a default agentic S3/S5 owner for an arbitrary user deployment.

## Self-hosted and non-human modes

Self-hosted Kind/OpenShift deployment supports operator-led project governance, schedules and policies. The analysis does not infer an autonomous S3/S4/S5 organization from a single-agent run or a declarative YAML file. An optional MCP server grants task/tool access subject to deployment authorization; a developer might construct richer agent-owned management, but no such project-wide closed decision policy is established as the standard default.

## Recursion

Each running agent session can itself sustain a locally agentic loop, while the parent project owns project-wide schedules, resources and policy. Multiple isolated tenant projects are independent organizational boundaries; cross-tenant identity isolation does not automatically become coordination among a single project's S1 units. No claim is made that nesting sessions or agent definitions establishes all six functions at every recursion.

## Variety and escalation

Agent task variety is absorbed locally by the model and tool stack. Platform constraints attenuate credential/network variety and scheduling overlap. User or administrator changes resolve current fleet scheduling, policy and identity decisions, and the next run receives their effects. Streaming telemetry makes evidence visible but does not independently audit itself. There is no demonstrated packaged S4 prospective loop or independent S3* verdict returned to regulation.

## Evidence gaps

- No first-party end-to-end runtime execution was performed; model/provider availability, actual tenant policy and external system access vary by deployment.
- S2 witness is narrow to two independently triggered run cells of one schedule, not coordination among arbitrary different configured agents or across tenants.
- Optional MCP-enabled agent management may support a richer constructor mode, but the inspected first-party standard path does not prove autonomous whole-project S3 policy discretion.
- A configured tenant may install independent auditors or strategic planners. Such third-party choices are not evidence of first-party default S3*/S4 closure.
- The Profile's `P` notation here denotes legitimate deployed parent ownership, not a blanket grade of ACP organizational autonomy or an independent S3* evaluation.

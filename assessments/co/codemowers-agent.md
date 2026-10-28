---
harness_id: codemowers-agent
project_name: Codemowers Agent
repository: https://github.com/codemowers/agent
review_ref: d056e1414b3e2e6f0f2c387bdab2c540bd26730d
reviewed_at: 2026-10-28
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Codemowers Agent

## Review boundary

- System in focus: one deployed Codemowers Agent privilege domain and its persistent Task workers, operator/dashboard and event intake.
- Purpose and identity: perform durable coding/operational work in Kubernetes from objectives and authenticated events.
- Relevant environment: Git forges, source/workspaces, Kubernetes, mail/events, model services and authorized human operators.
- Standard-distribution boundary: repository-built worker image with pinned coding CLIs, task-worker adapter, Go operator/API, Task/Agent CRDs and dashboard.
- Credited operating / distribution surfaces: src/task-worker.js, turn queue, runner/package.json, operator task reconciliation, Agent MCP and authenticated dashboard API.
- Adjacent first-party surfaces excluded from ownership: CI/tests, maintainer governance, optional feed-crawler development and platform-administration examples; external CLI/platform internals are dependencies, not borrowed metasystem owners.
- First-party operating / deployment modes considered: Claude/Codex/OpenCode workers; event-created and manually declared Tasks, persistent suspend/resume, human dashboard steering and Agent-scoped MCP.
- Recursion level: one deployed Agent Task fleet, not the Codemowers organization or the whole cluster.
- Reviewed revision: `d056e1414b3e2e6f0f2c387bdab2c540bd26730d`.
- Observation date: 2026-10-28.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The operator reconciles Agent/Task resources into worker Pods and PVCs; the runner image explicitly includes supported coding CLIs. The worker seeds task/workspace instructions, builds the CLI/MCP invocation, resumes native sessions, publishes progress/results and processes durable queued steering. Agent MCP is bound to the current Pod/Task/Agent by TokenReview and exposes own-task reporting plus same-Agent list/get/create/complete. Canonical resource keys reuse existing Tasks; normalized events reject ambiguous key ownership, coalesce duplicate activities and wake the owning Task. Human dashboard users see current fleet/tasks, progress, activity and metrics, then steer, stop or suspend/resume authorized Tasks. Namespace administrators retain Agent/credential/resource policy. Runtime lifecycle and cluster admission enforce those decisions.

## Operational model

Tasks are durable operational cells with independent workspaces, objectives and model-directed coding sessions. This is a concrete first-party composition of coding engines, not merely a list of compatible external products: the worker image pins them, seeds instructions, dispatches work and returns results. Task-key deduplication is a specific coordination constructor. Current fleet supervision is supported through an authenticated parent view and intervention path. Agent MCP lifecycle tools do not establish a shipped autonomous fleet regulator by themselves.

## S1 — Operations

- State: A
- Function: deliver code/operational outcomes through persistent Task sessions
- Disturbance / variety regulated: unknown code, tool/build failures, external updates and interrupted work
- Decisive decision or feedback right: choose task actions, respond to results and continue from steering/session state
- Decision owner: model actor in the repository-composed pinned coding CLI worker
- Supporting / enforcement mechanisms: worker image/adapter, PVC, CLI tool loop, MCP, event queue and Kubernetes confinement
- Closure path: objective/event → seeded worker/model actions → files/tools/results → published progress and resumed next turn
- Why this is / is not agent-owned: the worker adapter supplies reachability and persistence while the model owns substantive task choices
- Boundary reachability: runner/package.json pins all three supported engines and task-worker.js invokes/resumes them with first-party task instructions and Agent MCP
- Evidence: [runner/package.json](https://github.com/codemowers/agent/blob/d056e1414b3e2e6f0f2c387bdab2c540bd26730d/runner/package.json), [src/task-worker.js](https://github.com/codemowers/agent/blob/d056e1414b3e2e6f0f2c387bdab2c540bd26730d/src/task-worker.js), [src/turn-queue.js](https://github.com/codemowers/agent/blob/d056e1414b3e2e6f0f2c387bdab2c540bd26730d/src/turn-queue.js), [operator/internal/controller/agent_controller.go](https://github.com/codemowers/agent/blob/d056e1414b3e2e6f0f2c387bdab2c540bd26730d/operator/internal/controller/agent_controller.go).
- Basis: structural.
- Confidence: medium-high for bounded source inspection.
- Caveats: source-based ownership mapping; no live model/provider run or effectiveness claim.

## S2 — Coordination

- State: C
- Function: attenuate duplicate Task commitments for one external resource
- Disturbance / variety regulated: two workers/intake paths creating parallel work for the same issue/resource and repeated webhook/mail activity
- Decisive decision or feedback right: recognize existing same-Agent work and select a canonical routing key instead of creating duplicate commitments
- Decision owner: first-party deduplication constructor; agent coordination policy and cross-Task reconciliation remain to be composed
- Supporting / enforcement mechanisms: Agent-scoped list/get, canonical URI identity, deterministic Task name, create collision checks and event coalescing
- Closure path: existing task/key → reuse receipt or conflict/fallback → later work/events routed to one owned Task
- Why this is / is not agent-owned: runtime equality checks enforce identity; they do not own a discretionary coordination response
- Boundary reachability: worker Agent MCP explicitly instructs list_tasks to find existing work/avoid duplicates and create_task to supply a canonical key; operator implements reuse/collision checks
- Distinct S1 units: independent Task workers operating on related issue/resource objectives
- Inter-S1 disturbance: duplicate commitments and parallel effects when separate Tasks claim the same resource
- Attenuating coordination relation: canonical-key reuse with scoped ownership checks and duplicate/ambiguous event handling
- Feedback into subsequent S1 behaviour: create returns existing=true/name so a caller can reuse work; subsequent events wake the owned task rather than a duplicate
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the key/reuse contract explicitly targets duplicate work across cells; a queue or event router alone would not qualify
- Evidence: [operator/internal/api/agent_mcp.go](https://github.com/codemowers/agent/blob/d056e1414b3e2e6f0f2c387bdab2c540bd26730d/operator/internal/api/agent_mcp.go), [operator/api/v1alpha1/keys.go](https://github.com/codemowers/agent/blob/d056e1414b3e2e6f0f2c387bdab2c540bd26730d/operator/api/v1alpha1/keys.go), [operator/internal/controller/normalized_event.go](https://github.com/codemowers/agent/blob/d056e1414b3e2e6f0f2c387bdab2c540bd26730d/operator/internal/controller/normalized_event.go), [operator/internal/controller/consumer.go](https://github.com/codemowers/agent/blob/d056e1414b3e2e6f0f2c387bdab2c540bd26730d/operator/internal/controller/consumer.go).
- Basis: structural.
- Confidence: medium-high for bounded source inspection.
- Caveats: source-based ownership mapping; no live model/provider run or effectiveness claim.

## S3 — Inside-and-now control

- State: P
- Function: parent-governed regulation of current Task-fleet commitments
- Disturbance / variety regulated: undesired continued execution, stale priorities, resource use and capability exposure across current Tasks
- Decisive decision or feedback right: inspect current fleet and decide which commitments run, pause, resume, receive steering or lose an MCP capability
- Decision owner: legitimate authenticated human operator for permitted Agent Tasks; namespace admin for resource envelope
- Supporting / enforcement mechanisms: OIDC/RBAC-filtered fleet/task views, steering queue, stop/suspend API, Task reconciliation and Pod lifecycle
- Closure path: fleet/task state → parent current-control judgment → authenticated steering/suspend/resume/MCP change → worker/queue/Pod state changes → refreshed current view
- Why this is / is not agent-owned: human owns current priorities/intervention; Go reconciliation enforces the choice and is not autonomous S3
- Boundary reachability: shipped dashboard/API exposes the view and interventions; reconciler applies Task.spec.Suspend and worker steering in the same deployed fleet
- Whole-system current view: listAgents/listTasks expose the authorized Agent domain’s tasks, phases, current activity, progress, resource settings and turn metrics
- Current-control decision scope: which current Task commitments run or pause and which tools remain available, within the human’s Agent RBAC envelope
- Evidence: [operator/internal/api/handler.go](https://github.com/codemowers/agent/blob/d056e1414b3e2e6f0f2c387bdab2c540bd26730d/operator/internal/api/handler.go), [operator/internal/api/public/index.html](https://github.com/codemowers/agent/blob/d056e1414b3e2e6f0f2c387bdab2c540bd26730d/operator/internal/api/public/index.html), [operator/internal/controller/agent_controller.go](https://github.com/codemowers/agent/blob/d056e1414b3e2e6f0f2c387bdab2c540bd26730d/operator/internal/controller/agent_controller.go), [docs/security-model.md](https://github.com/codemowers/agent/blob/d056e1414b3e2e6f0f2c387bdab2c540bd26730d/docs/security-model.md).
- Basis: structural.
- Confidence: medium-high for bounded source inspection.
- Caveats: source-based ownership mapping; no live model/provider run or effectiveness claim.

## S3* — Complementary audit

- State: —
- Function: no complementary independent audit path established
- Disturbance / variety regulated: routine worker status and execution claims
- Decisive decision or feedback right: publish/inspect task reports, probe MCP availability and validate authenticated observations
- Decision owner: worker reporting, deterministic validators and human operational viewer; no supplied independent auditor
- Supporting / enforcement mechanisms: streamed results, metrics, probes and status records
- Closure path: ordinary reporting/probe results update current task state
- Why this is / is not agent-owned: availability checks and result parsing do not establish independent corrective audit judgment
- Evidence: [src/task-worker.js](https://github.com/codemowers/agent/blob/d056e1414b3e2e6f0f2c387bdab2c540bd26730d/src/task-worker.js), [operator/internal/api/agent_mcp.go](https://github.com/codemowers/agent/blob/d056e1414b3e2e6f0f2c387bdab2c540bd26730d/operator/internal/api/agent_mcp.go), [operator/internal/api/handler.go](https://github.com/codemowers/agent/blob/d056e1414b3e2e6f0f2c387bdab2c540bd26730d/operator/internal/api/handler.go).
- Basis: structural.
- Confidence: medium-high for bounded source inspection.
- Caveats: source-based ownership mapping; no live model/provider run or effectiveness claim.

### Absence scope

- Surfaces inspected: worker report/probe, dashboard, status validation, CLI dispatch and tests/CI separation
- Plausible first-party paths checked: MCP connectivity probes, streamed tool events, model outputs, raw workspace inspection and human review
- Why no material first-party path remains: shipped paths report production or connection health; no materially independent complementary claim challenge and returned corrective audit is wired; human code review and external CLI internals are not borrowed

## S4 — Outside-and-then intelligence

- State: —
- Function: no external prospective capability-adaptation loop established
- Disturbance / variety regulated: incoming issues/mail/alerts/feed events and current task failures
- Decisive decision or feedback right: react to an event or configure current model/instructions
- Decision owner: operational agent and human administrators; no supplied S4 decision owner
- Supporting / enforcement mechanisms: authenticated receivers, feed crawler, TaskPolicy, durable sessions and model configuration
- Closure path: events wake current work; no prospective capability option-generation/return cycle
- Why this is / is not agent-owned: environmental event intake is not by itself outside-and-then intelligence
- Evidence: [operator/internal/controller/normalized_event.go](https://github.com/codemowers/agent/blob/d056e1414b3e2e6f0f2c387bdab2c540bd26730d/operator/internal/controller/normalized_event.go), [operator/api/v1alpha1/task_policy.go](https://github.com/codemowers/agent/blob/d056e1414b3e2e6f0f2c387bdab2c540bd26730d/operator/api/v1alpha1/task_policy.go), [operator/api/v1alpha1/types.go](https://github.com/codemowers/agent/blob/d056e1414b3e2e6f0f2c387bdab2c540bd26730d/operator/api/v1alpha1/types.go), [README.md](https://github.com/codemowers/agent/blob/d056e1414b3e2e6f0f2c387bdab2c540bd26730d/README.md).
- Basis: structural.
- Confidence: medium-high for bounded source inspection.
- Caveats: source-based ownership mapping; no live model/provider run or effectiveness claim.

### Absence scope

- Surfaces inspected: event/feed intake, task policies, worker context, model/Agent configuration and documented roadmap
- Plausible first-party paths checked: feed-based work creation, resumed context, policy/model changes and operator planning
- Why no material first-party path remains: these route current work or install configuration; neither an autonomous nor first-party parent loop develops future-environment adaptation options and returns them into present capability

## S5 — Policy and identity

- State: —
- Function: no identity/ultimate-policy issue-resolution loop established
- Disturbance / variety regulated: credential scope, role instructions and platform trust boundaries
- Decisive decision or feedback right: namespace humans define Agent role, credentials and pod envelope
- Decision owner: namespace/cluster administrators; model workers cannot mutate Agent resources
- Supporting / enforcement mechanisms: Agent CRD, RBAC, credential projection, admission and injected instructions
- Closure path: configured role/limits reach a worker; no function-specific identity dispute/referral and authoritative return loop is supplied
- Why this is / is not agent-owned: configuration authority and human merge ownership alone do not establish S5
- Evidence: [operator/api/v1alpha1/types.go](https://github.com/codemowers/agent/blob/d056e1414b3e2e6f0f2c387bdab2c540bd26730d/operator/api/v1alpha1/types.go), [docs/security-model.md](https://github.com/codemowers/agent/blob/d056e1414b3e2e6f0f2c387bdab2c540bd26730d/docs/security-model.md), [src/task-worker.js](https://github.com/codemowers/agent/blob/d056e1414b3e2e6f0f2c387bdab2c540bd26730d/src/task-worker.js), [AGENTS.md](https://github.com/codemowers/agent/blob/d056e1414b3e2e6f0f2c387bdab2c540bd26730d/AGENTS.md).
- Basis: structural.
- Confidence: medium-high for bounded source inspection.
- Caveats: source-based ownership mapping; no live model/provider run or effectiveness claim.

### Absence scope

- Surfaces inspected: Agent instructions/specification, namespace trust model, worker privilege boundaries, steering and maintainer scope
- Plausible first-party paths checked: human role/policy edits, scoped credentials, final human merge and generic operator intervention
- Why no material first-party path remains: these define/enforce an envelope but do not supply an in-boundary identity/ultimate-policy question → legitimate parent decision → returned governance closure; ordinary S3 steering is kept separate

## Distributed OSS parent arrangement

Repository maintainers and external PR reviewers are adjacent. The positive S3 parent is the deployed fleet’s authenticated operator, not the source project’s contributor governance. Local task review does not establish project-wide S5.

## Self-hosted and non-human modes

The supported self-hosted Kubernetes mode explicitly keeps namespace administrators human and Agent specs outside worker mutation. Parent S3 uses authorized fleet visibility and intervention; no autonomous S3/S5 owner is inferred from a Kubernetes operator name.

## Recursion

Tasks contribute durable operations to one Agent domain. Native CLI subagents or independent Pods do not establish complete recursive viable units.

## Variety and escalation

Authenticated events and queued steering carry operational variety. Key deduplication/coalescing attenuate duplicate work; scoped credentials/RBAC/confinement bound action. Credit exhaustion can suspend a task and request restoration; that error alone is not an algedonic or policy function.

## Evidence gaps

No Kubernetes deployment, live coding/model call, external message or infrastructure mutation was performed. Thirteen selected deterministic Node tests passed (turn queue, identity, MCP authentication, Kubernetes environment and child signals). Go is unavailable on the inspection host, so the operator suite was not run. Static supported-path evidence supplies the mapping, not an asserted production-effectiveness trace.

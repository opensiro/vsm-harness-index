---
harness_id: openclaw-enterprise
project_name: OpenClaw Enterprise
repository: https://github.com/openclaw/openclaw-enterprise
review_ref: b601b1c6061b356620117979506109c54eea8730
reviewed_at: 2026-10-06
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-06
status: excluded-no-agentic-vsm
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# OpenClaw Enterprise

## Review boundary

- System in focus: the first-party OpenClaw Enterprise / OpenClaw Control Plane (OCC) at frozen revision b601b1c6061b356620117979506109c54eea8730, including Agent and AgentRevision lifecycle, Configuration and Secret handling, IAM authorization, durable work queues, controller reconciliation, Compute/Sandbox/Configuration Driver integration, console/CLI surfaces, operational metrics and audit recording.
- Purpose and identity: provide a vendor-neutral control plane that configures, authorizes, deploys, reconciles, observes and removes Agent workloads.
- Relevant environment: operators and API clients, Namespaces, Configurations, Secrets, selected Drivers and infrastructure, deployed Agent gateways, OpenClaw or Codex Harness runtimes, model providers, runtime readiness/failure evidence and audit/metrics consumers.
- Standard-distribution boundary: OCC API, worker, resource lifecycle, persistence/work queue, IAM, audit, Drivers, deployment admission and routing are inside. The semantic Agent turn loop that receives messages, calls a model, chooses tool actions and executes tools belongs to the selected OpenClaw or Codex Harness runtime and is not credited to OCC merely because OCC deploys or configures it.
- Credited operating / distribution surfaces: README.md; docs/guides/concepts.md; docs/reference/harness-execution.md; docs/reference/controller.md; docs/flows/controller-worker.md; docs/reference/agents.md; packages/occ; packages/iam; packages/audit; apps/controller; bundled Driver integration and CLI/console management surfaces.
- Adjacent first-party surfaces excluded from ownership: upstream OpenClaw and Codex runtime cognition/agent-loop implementations; model providers; external infrastructure and Sandbox implementations; repository CI/release/contributor tooling; examples/tests that demonstrate a Harness but do not move the semantic loop into OCC.
- First-party operating / deployment modes considered: local Kubernetes and production Kubernetes Agent deployment, embedded OpenClaw, dedicated Codex, controller API plus independent worker reconciliation, operator console/CLI, Agent stop/delete/redeploy, IAM/Secret/configuration management, observability and diagnostics.
- Recursion level: one OCC installation governing deployed Agent resources. Deployed Agent/Harness runtimes are governed operational systems at the data-plane boundary; their semantic task loops are not inherited as OCC-owned S1.
- Reviewed revision: b601b1c6061b356620117979506109c54eea8730.
- Observation date: 2026-10-06.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

The repository explicitly separates control and data planes. OCC configures and manages Agent deployments: its API authenticates and authorizes resource changes, persists immutable AgentRevision state, and queues durable lifecycle work. A separate controller worker claims that work, rechecks current authorization, invokes the selected Compute path, observes readiness or failure, activates the admitted revision and persists terminal or retry state.

The data plane is described separately. Each deployed Agent has a gateway and a Harness. The Harness executes Agent turns and tools; supported paths use embedded OpenClaw or dedicated Codex. packages/occ/src/configured-harness.ts resolves and validates which supported runtime is selected from model/configuration policy, while controller provisioning and reconciliation arrange credentials, infrastructure, readiness and activation around that runtime. Those mechanisms select and govern a semantic actor; they do not implement its open-ended objective → model/tool decision → observation → revised action loop.

Counterfactual owner test: remove the OpenClaw/Codex Harness runtime and model-backed turn loop while leaving OCC resource state, IAM, work queue, controller worker, Drivers, audit and console intact. OCC can still validate configuration, authorize requests, persist desired state, enqueue/reconcile lifecycle work, expose diagnostics and record audit evidence, but it cannot interpret an open-ended user task, choose semantic tool actions or complete that task. The decisive S1 task loop therefore remains outside the assessed OCC boundary.

Primary evidence:

- https://github.com/openclaw/openclaw-enterprise/blob/b601b1c6061b356620117979506109c54eea8730/README.md
- https://github.com/openclaw/openclaw-enterprise/blob/b601b1c6061b356620117979506109c54eea8730/docs/guides/concepts.md
- https://github.com/openclaw/openclaw-enterprise/blob/b601b1c6061b356620117979506109c54eea8730/docs/reference/harness-execution.md
- https://github.com/openclaw/openclaw-enterprise/blob/b601b1c6061b356620117979506109c54eea8730/docs/reference/controller.md
- https://github.com/openclaw/openclaw-enterprise/blob/b601b1c6061b356620117979506109c54eea8730/docs/flows/controller-worker.md
- https://github.com/openclaw/openclaw-enterprise/blob/b601b1c6061b356620117979506109c54eea8730/packages/occ/src/configured-harness.ts
- https://github.com/openclaw/openclaw-enterprise/blob/b601b1c6061b356620117979506109c54eea8730/packages/occ/src/agent-provisioning.ts

## Operational model

An authenticated caller creates or updates Agent-related resources and requests deployment. OCC authorizes the exact resources, freezes an AgentRevision and queues durable work. The worker claims the operation, reloads current state and authorization, calls selected infrastructure Drivers, prepares the gateway/Harness workload, observes bounded readiness/model-probe evidence, activates the revision and records results. Once active, client messages are processed by the Agent data plane: the selected OpenClaw/Codex Harness calls the model and runs tools. OCC can later expose logs/status, write selected workspace files, stop/delete the Agent or admit a new revision, but it does not own the deployed Harness's semantic reasoning loop.

## S1 — Operations

- State: —
- Function: no first-party OCC autonomous operational unit is established for the semantic agent work that OpenClaw Enterprise manages.
- Disturbance / variety regulated: OCC regulates deployment/resource/configuration/authorization/infrastructure variety; open-ended task, conversation and tool-choice variety is absorbed by the selected external model-backed Harness runtime.
- Decisive decision or feedback right: interpret an open-ended task and observations, choose semantic model/tool actions, revise those choices from results and decide task completion.
- Decision owner: the deployed OpenClaw or Codex Harness/model-backed agent runtime, not OCC.
- Supporting / enforcement mechanisms: Agent/AgentRevision resources, Configuration validation, IAM, Secrets, durable work queue, controller worker, Compute/Sandbox/Configuration Drivers, readiness probes, routing and lifecycle APIs.
- Closure path: caller admits/deploys Agent → OCC provisions and activates selected Harness → gateway/Harness receives a message → Harness/model chooses and executes semantic actions → response/tool evidence remains in the data plane; OCC governs lifecycle around it.
- Boundary reachability: no positive OCC S1 path claimed; the semantic actor is reachable only as a separately selected/deployed Harness runtime whose cognition is outside the credited OCC ownership boundary.
- Why this is / is not agent-owned: OCC makes deterministic/configured lifecycle and authorization decisions. Removing the selected Harness/model loop removes the open-ended agent operation while leaving OCC control-plane behavior materially intact.
- Evidence: https://github.com/openclaw/openclaw-enterprise/blob/b601b1c6061b356620117979506109c54eea8730/docs/guides/concepts.md; https://github.com/openclaw/openclaw-enterprise/blob/b601b1c6061b356620117979506109c54eea8730/docs/reference/harness-execution.md; https://github.com/openclaw/openclaw-enterprise/blob/b601b1c6061b356620117979506109c54eea8730/packages/occ/src/configured-harness.ts.
- Basis: explicit + structural negative review.
- Confidence: high.
- Caveats: OCE deliberately provides supported deployment paths for Agent runtimes, including embedded OpenClaw. Deployment ownership and runtime selection do not transfer the runtime's semantic decision right to OCC.

### Absence scope

- Surfaces inspected: root architecture/code-layout documentation; control/data-plane concepts; Harness execution contract; Agent lifecycle and provisioning; controller worker/reconciliation; packages/occ runtime selection/provisioning; IAM/audit/Driver boundaries; first-Agent and production deployment guides.
- Plausible first-party paths checked: embedded OpenClaw path; dedicated Codex path; model startup probes; workspace-file access; plugin selection; controller worker; Agent provisioning helpers; console/CLI Agent operations.
- Why no material first-party path remains: inspected OCC code and documentation configure, admit, provision, authorize, observe or operate the selected Harness, while the Harness itself owns model calls and tool execution. No OCC-native semantic task loop remains after external/runtime cognition is excluded.

## S2 — Coordination

- State: —
- Function: no qualifying first-party inter-S1 coordination function is established at the assessed OCC recursion.
- Disturbance / variety regulated: work-queue contention, Namespace/Agent lifecycle concurrency, deployment ordering and resource ownership are regulated, but these are control-plane consistency concerns rather than interference among distinct first-party autonomous S1 units.
- Decisive decision or feedback right: choose and return a coordination response to a specific interference among distinct same-recursion operational S1 units.
- Decision owner: none established because first-party OCC S1 units are not established.
- Supporting / enforcement mechanisms: PostgreSQL work claims, leases, FOR UPDATE SKIP LOCKED behavior, per-Agent/Namespace exclusion, immutable revisions, driver reconciliation and activation ordering.
- Closure path: deterministic work-queue rules prevent conflicting lifecycle claims and retry/defer operations; no first-party autonomous S1 behavior is adjusted by a separate interference-specific coordination actor.
- Boundary reachability: no positive S2 path claimed.
- Why this is / is not agent-owned: queue serialization and lifecycle fencing are real coordination mechanisms at the software-resource level, but Methodology 0.3.6 requires the S2 witness to start from distinct qualifying S1 operational units and a concrete inter-S1 disturbance.
- Evidence: https://github.com/openclaw/openclaw-enterprise/blob/b601b1c6061b356620117979506109c54eea8730/docs/flows/controller-worker.md; https://github.com/openclaw/openclaw-enterprise/blob/b601b1c6061b356620117979506109c54eea8730/docs/reference/controller.md.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: a larger organization containing several deployed Agents may need genuine S2. Their agentic S1 ownership belongs to the deployed runtimes and cannot be borrowed into OCC's standalone assessment.

### Absence scope

- Surfaces inspected: controller work queue/claim model, Agent/Namespace lifecycle, activation/replacement rules, current Driver reconciliation and supported multi-Agent resource model.
- Plausible first-party paths checked: concurrent deployment exclusion, queue leases, AgentRevision activation ordering, Namespace isolation and multi-Agent inventory.
- Why no material first-party path remains: these paths serialize or protect control-plane state. They do not establish distinct first-party autonomous S1 units plus an interference → attenuation → feedback witness.

## S3 — Inside-and-now control

- State: —
- Function: OCC provides strong current control and enforcement over deployed resources, but no first-party autonomous S3 decision owner is established inside the assessed autonomous-harness publication boundary.
- Disturbance / variety regulated: current desired/runtime state, deployment failures, authorization changes, stale claims, readiness, retries, Agent stop/delete requests and infrastructure availability.
- Decisive decision or feedback right: make discretionary whole-system current choices over shared commitments, priorities, resources or intervention on behalf of an autonomous organization.
- Decision owner: operator/API caller/configuration for substantive choices; deterministic OCC authorization, queue and reconciliation code enforces the admitted choice and current policy.
- Supporting / enforcement mechanisms: whole-installation API/resource views, controller worker, IAM reauthorization, retry/defer/fail-closed logic, stop/delete/deploy lifecycle, diagnostics and metrics.
- Closure path: caller/configuration selects desired current action → OCC authorizes and persists it → worker rechecks current authority and reconciles → workload/current state changes. No autonomous OCC actor owns the substantive whole-system current discretion.
- Boundary reachability: no positive autonomous S3 path claimed.
- Why this is / is not agent-owned: the worker has hard enforcement power but follows deterministic lifecycle and admitted desired state. Removing any external model/Harness cognition does not remove the worker's same deterministic reconciliation behavior.
- Evidence: https://github.com/openclaw/openclaw-enterprise/blob/b601b1c6061b356620117979506109c54eea8730/docs/reference/controller.md; https://github.com/openclaw/openclaw-enterprise/blob/b601b1c6061b356620117979506109c54eea8730/docs/flows/controller-worker.md; https://github.com/openclaw/openclaw-enterprise/blob/b601b1c6061b356620117979506109c54eea8730/docs/reference/agents.md.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: OCE is intentionally a strong control plane. Methodology 0.3.6 separates enforcement from organizational decision ownership and does not publish a deterministic/operator-owned control plane as autonomous S3 when the first-party S1 admission boundary already fails.

### Absence scope

- Surfaces inspected: installation/Agent current-state APIs, deployment/stop/delete, controller worker current authorization checks, work retry/defer/failure, diagnostics, metrics, console and CLI.
- Plausible first-party paths checked: resource inventory, selective intervention, deployment replacement, runtime health response, actor revocation, retry/failure handling and Agent lifecycle reconciliation.
- Why no material first-party path remains: OCC closes deterministic or operator-requested current-control effects, but no first-party autonomous actor owns the whole-system discretionary current-control right.

## S3* — Complementary audit

- State: —
- Function: audit events, diagnostics, metrics and persisted worker results provide complementary evidence, but no independent first-party autonomous audit judgment with corrective return is established.
- Disturbance / variety regulated: authorization/accountability records, deployment failure evidence, request/reconciliation outcomes, runtime diagnostics and observability data.
- Decisive decision or feedback right: independently challenge an operational claim from a complementary access path and return a judgment that changes current operation.
- Decision owner: deterministic logging/diagnostic machinery records bounded facts; interpretation/remediation remains with operators or external systems.
- Supporting / enforcement mechanisms: packages/audit, admission audit events, worker structured events, diagnostics endpoint, metrics, runtime logs and sanitized evidence.
- Closure path: OCC records/exposes evidence → operator or external monitoring may interpret it → any corrective deploy/stop/policy action is separately requested; no autonomous first-party audit-judgment loop closes the path.
- Boundary reachability: no positive S3* path claimed.
- Why this is / is not agent-owned: independent process separation of API and worker and durable audit records improve evidence quality, but process independence is not equivalent to an independent semantic audit judgment.
- Evidence: https://github.com/openclaw/openclaw-enterprise/blob/b601b1c6061b356620117979506109c54eea8730/docs/reference/controller.md; https://github.com/openclaw/openclaw-enterprise/blob/b601b1c6061b356620117979506109c54eea8730/packages/audit/src/index.ts; https://github.com/openclaw/openclaw-enterprise/blob/b601b1c6061b356620117979506109c54eea8730/docs/reference/agents.md.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: external monitoring or a human operator can use OCC evidence to perform audit, but that parent/external auditor is not a first-party autonomous S3* owner in this repository boundary.

### Absence scope

- Surfaces inspected: audit package, request/admission audit paths, controller worker logs, metrics, Agent deployment status/diagnostics and runtime log surfaces.
- Plausible first-party paths checked: audit event verification, separate worker observations, runtime diagnostics, failure-cause recording and metrics-triggered remediation.
- Why no material first-party path remains: inspected paths collect, sanitize and expose evidence or deterministic checks; no independent semantic auditor forms a judgment and returns it into current control automatically.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party external-and-prospective adaptation loop is established.
- Disturbance / variety regulated: changing infrastructure/runtime availability, provider/model configuration, Harness versions, Driver selections and future deployment choices can be represented, but adaptation judgment is operator/developer-owned.
- Decisive decision or feedback right: sense an external/future distinction, generate adaptation options, choose among them and return the choice into current capability.
- Decision owner: operator/developer/maintainer through Configuration, startup YAML, deployment selection and software updates.
- Supporting / enforcement mechanisms: immutable AgentRevision snapshots, Configurations, model/Harness resolver, Driver selection, diagnostics, deployment retries and plugin/runtime policy validation.
- Closure path: external change is observed by humans/integrations → configuration/software/deployment choice is changed → a new revision or installation configuration is admitted → OCC enforces it. No autonomous OCC intelligence function owns the adaptation judgment.
- Boundary reachability: no positive S4 path claimed.
- Why this is / is not agent-owned: runtime selection and future redeployment are configurable capabilities, not an agent-owned prospective option-generation and adaptation loop.
- Evidence: https://github.com/openclaw/openclaw-enterprise/blob/b601b1c6061b356620117979506109c54eea8730/docs/reference/harness-execution.md; https://github.com/openclaw/openclaw-enterprise/blob/b601b1c6061b356620117979506109c54eea8730/packages/occ/src/configured-harness.ts; https://github.com/openclaw/openclaw-enterprise/blob/b601b1c6061b356620117979506109c54eea8730/docs/reference/agents.md.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: OCC can preserve and apply new configurations robustly. Persistence/configurability and reacting to current failures do not satisfy the Methodology's outside-and-then adaptation witness.

### Absence scope

- Surfaces inspected: configuration/revision model, Driver and Harness selection, model/provider policy, diagnostics, retry/redeploy behavior, plugin selection, operator guidance and deployment flows.
- Plausible first-party paths checked: automatic model/Harness switching, autonomous Driver selection, future-capability planning, learned policy/configuration changes and diagnostics-driven self-adaptation.
- Why no material first-party path remains: changes to capability are explicitly admitted/configured by operators or developers; no first-party autonomous external/prospective judgment loop selects and returns an adaptation.

## S5 — Policy and identity

- State: —
- Function: OCC supplies IAM, Restrictions, roles, configuration validation and Agent identity primitives, but no first-party autonomous identity/ultimate-policy governance loop is established.
- Disturbance / variety regulated: who may mutate resources, which exact resources are accessible, which Harness/runtime/configuration is admitted, and which credentials or infrastructure bindings are permitted.
- Decisive decision or feedback right: authoritatively decide the organization's identity or ultimate policy and return that decision so subsequent operation is governed by it.
- Decision owner: installation/operator/administrator and developer-authored trusted configuration; OCC deterministically checks and enforces those choices.
- Supporting / enforcement mechanisms: packages/iam, Roles, AccessBindings, Restrictions, stable Agent service principals, trusted startup YAML, exact-resource authorization, Configuration/Harness validation and fail-closed admission.
- Closure path: parent/operator authors or changes policy/configuration → OCC validates/persists/enforces it → subsequent requests and deployments are constrained. No autonomous OCC actor owns the ultimate-policy choice.
- Boundary reachability: no positive autonomous S5 path claimed.
- Why this is / is not agent-owned: policy enforcement is strong, but the decisive policy/identity authority remains external human/developer configuration. An Agent service principal is an identity object, not an autonomous S5 governor.
- Evidence: https://github.com/openclaw/openclaw-enterprise/blob/b601b1c6061b356620117979506109c54eea8730/docs/guides/topics/iam.md; https://github.com/openclaw/openclaw-enterprise/blob/b601b1c6061b356620117979506109c54eea8730/packages/iam/src/index.ts; https://github.com/openclaw/openclaw-enterprise/blob/b601b1c6061b356620117979506109c54eea8730/docs/reference/controller.md.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: a parent-governed S5 loop can exist in a deployed organization using OCC, but the autonomous-harness publication boundary fails at S1 and this standalone OCC review does not import operator governance as autonomous S5.

### Absence scope

- Surfaces inspected: IAM roles/bindings/restrictions, Agent service principals, startup configuration, Harness/model selection policy, resource authorization, Configuration validation, deployment admission and operator administration surfaces.
- Plausible first-party paths checked: Agent self-policy revision, autonomous identity governance, autonomous Role/Restriction changes, self-selected ultimate runtime policy and policy findings returned as authoritative governance.
- Why no material first-party path remains: all ultimate policy/identity decisions identified are administrator/developer-authored and deterministically enforced; no first-party autonomous authority owns them.

## Distributed OSS parent arrangement

The assessed organization is a running OCE/OCC installation, not the GitHub maintainer project. Repository contribution and release governance are adjacent development surfaces and are not imported as runtime S3/S4/S5 ownership.

## Self-hosted and non-human modes

OCE is self-hostable and can deploy autonomous OpenClaw or Codex Agents. Those Agents may themselves qualify as autonomous harnesses when assessed at their own runtime boundary. This assessment intentionally does not inherit their cognition into the OCC control plane merely because OCC provisions, authenticates or observes them.

## Recursion

OCC is a management/control layer around Agent resources. At a broader deployment recursion, autonomous Agents may be operational units under OCC-mediated governance. At the repository-relative OCC boundary required by this review, however, those data-plane agent loops are separate governed systems rather than first-party OCC S1.

## Variety and escalation

OCC absorbs substantial infrastructure, lifecycle, authorization, tenancy, configuration, credential and failure variety through deterministic APIs, durable state, work claims, Drivers and fail-closed checks. Exceptional runtime failures are surfaced through bounded status/diagnostic/log evidence for operator action. These mechanisms are operationally important but do not substitute for the missing first-party autonomous S1 semantic loop.

## Evidence gaps

No ? state is required. The frozen repository directly documents the control/data-plane split, identifies the Harness as the component that calls models and runs tools, and exposes the OCC resource/admission/reconciliation source required to support the boundary-relative negative findings. Proposed terminal disposition: excluded-no-agentic-vsm.

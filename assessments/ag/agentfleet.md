---
harness_id: agentfleet
project_name: AgentFleet
repository: https://github.com/narkco-kang/agent-fleet
review_ref: f2fd46afbebdc1df520dec7f5862edd1e0047e23
reviewed_at: 2026-11-03
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-11-03
status: excluded-no-agentic-vsm
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# AgentFleet

**Canonical disposition:** `excluded-no-agentic-vsm`. This is a first-party autonomous S1 eligibility finding, not a denial of AgentFleet's substantial cross-device task lifecycle, routing, failover, memory ledger, or ability to execute *externally installed* coding agents.

## Review boundary

- System in focus: AgentFleet's self-hosted coordinator, device daemons/adapters, team/swarm/loop scheduling, modelgateway and shared evidence ledger; not Claude/Codex/Grok/other separately installed agent cognition.
- Purpose and identity: Deploy and coordinate existing local agent platforms across devices, route tasks to healthy targets, preserve shared memory/evidence and expose activity to operators.
- Relevant environment: Device reachability, installed external CLI agents, configured provider models, submitted prompts, per-agent capacity, task status, failure events and human deployment approvals.
- Standard-distribution boundary: Backend dashboard/coordinator + device daemon dispatches tasks to external CLI adapters. Gateway routes a single `chat/completions` request to a selected model/provider or configured fallback. Preconfigured expert teams and loops produce deterministic routing/dispatch plans, not an internal model deciding and revising its next tool action.
- Credited operating / distribution surfaces: [README.md](https://github.com/narkco-kang/agent-fleet/blob/f2fd46afbebdc1df520dec7f5862edd1e0047e23/README.md), [scheduler.ts](https://github.com/narkco-kang/agent-fleet/blob/f2fd46afbebdc1df520dec7f5862edd1e0047e23/backend/src/services/scheduler.ts), [taskRunner.ts](https://github.com/narkco-kang/agent-fleet/blob/f2fd46afbebdc1df520dec7f5862edd1e0047e23/backend/src/services/taskRunner.ts), [device message handler](https://github.com/narkco-kang/agent-fleet/blob/f2fd46afbebdc1df520dec7f5862edd1e0047e23/device-agent/src/messageHandler.ts), [CLI adapter](https://github.com/narkco-kang/agent-fleet/blob/f2fd46afbebdc1df520dec7f5862edd1e0047e23/device-agent/src/adapters/cliRunner.ts), [modelgateway OpenAI handler](https://github.com/narkco-kang/agent-fleet/blob/f2fd46afbebdc1df520dec7f5862edd1e0047e23/modelgateway/src/openai.ts), [swarmRouter.ts](https://github.com/narkco-kang/agent-fleet/blob/f2fd46afbebdc1df520dec7f5862edd1e0047e23/backend/src/services/swarm/swarmRouter.ts).
- Adjacent first-party surfaces excluded from ownership: Marketing-style dashboard demo simulation, performance benchmark fixtures, research/PRD files, prospective WeChat personal connector, external CLI model/tool loops and operator-provided role/skill/persona definitions.
- First-party operating / deployment modes considered: Local device task dispatch with confirmed stable Grok adapter and platform-specific unverified/scaffold adapters; direct gateway completion and model fallback; team/swarm routing; deterministic loop scheduler; memory-ledger sync; human-authorized deployment and assets.
- Recursion level: One cross-device task scheduler and relay over externally owned AI workers, not a proven first-party agentic operational recursion.
- Reviewed revision: `f2fd46afbebdc1df520dec7f5862edd1e0047e23`.
- Observation date: 2026-11-03.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The backend stores task states, uses online device/agent registry and capacity to pick a target, claims a slot and sends a task envelope to a device. Its CLI adapter spawns a separately installed agent program and streams stdout/status; the external program chooses coding actions. Alternatively, gateway tasks send a single user message to modelgateway, which proxies `chat/completions` to a provider and returns its text without interpreting tool calls or running a model/tool loop. Swarm role selection applies manual/preferred/capability tiers; team and loop services map operator-defined roles and step templates to dispatch instructions. The shared memory ledger is hash-linked evidence storage, with no first-party model-operated prospective strategy owner. [scheduler.ts](https://github.com/narkco-kang/agent-fleet/blob/f2fd46afbebdc1df520dec7f5862edd1e0047e23/backend/src/services/scheduler.ts), [device message handler](https://github.com/narkco-kang/agent-fleet/blob/f2fd46afbebdc1df520dec7f5862edd1e0047e23/device-agent/src/messageHandler.ts), [CLI adapter](https://github.com/narkco-kang/agent-fleet/blob/f2fd46afbebdc1df520dec7f5862edd1e0047e23/device-agent/src/adapters/cliRunner.ts), [gateway](https://github.com/narkco-kang/agent-fleet/blob/f2fd46afbebdc1df520dec7f5862edd1e0047e23/modelgateway/src/openai.ts), [loop scheduler](https://github.com/narkco-kang/agent-fleet/blob/f2fd46afbebdc1df520dec7f5862edd1e0047e23/backend/src/services/loop/loopScheduler.ts).

Counterfactual owner test: remove installed Claude/Codex/Grok/etc agents from devices, retaining the coordinator, team/loop scheduler, provider proxy and DB. The remaining backend can accept tasks, compute routes, enqueue steps, make one prompt-response model request and report device/model failure; it cannot choose a sequence of coding tools after inspecting results, repair source changes or adaptively close open-ended engineering work. With external CLI agents restored, those agents—not AgentFleet—own the actual model/tool feedback decisions. `README.md` explicitly says it coordinates agents already installed and does not build them. This is a functional integration and governance wrapper, not an independently owned agentic S1 harness.

## Operational model

Human/API creates a prompt/role/target → dispatcher chooses an available external agent or gateway model → device daemon launches external CLI (or gateway forwards one model completion) → task events/usage are stored → mechanical failover/requeue or terminal result. Human controls team definitions, deployment/asset approvals, installed agents and model configuration. The substantive adaptive engineering work, when present, is owned by the external coding agent. [README.md](https://github.com/narkco-kang/agent-fleet/blob/f2fd46afbebdc1df520dec7f5862edd1e0047e23/README.md), [scheduler.ts](https://github.com/narkco-kang/agent-fleet/blob/f2fd46afbebdc1df520dec7f5862edd1e0047e23/backend/src/services/scheduler.ts).

## S1 — Operations

- State: —
- Function: Adaptive autonomous software task execution would select tools/actions, inspect actual results and decide next engineering steps to closure.
- Disturbance / variety regulated: Device/model availability, prompt delivery and failure are handled; semantic coding surprises are left to separately installed CLI agents.
- Decisive decision or feedback right: Choose substantive next tool actions on changing repository/tool evidence; not first-party AgentFleet-owned.
- Decision owner: External Claude/Codex/Grok and other coding-agent binaries. The gateway provider returns one answer, while AgentFleet chooses only where/how to deliver the prompt.
- Supporting / enforcement mechanisms: Task scheduler, device adapter `runCli`, modelgateway `chatCompletions`, capacity claims, messages, streams and memory ledger.
- Closure path: Task → deterministic target selection → external CLI executes its own loop and emits result (or one gateway model response) → AgentFleet stores outcome; AgentFleet never owns adaptive in-task code/tool choices.
- Why this is / is not agent-owned: A real external coding agent may act autonomously, but the surrounding AgentFleet process only supervises its lifecycle or passes through one inference response; neither transfers first-party operational semantic discretion.
- Evidence: [README.md, responsibility matrix](https://github.com/narkco-kang/agent-fleet/blob/f2fd46afbebdc1df520dec7f5862edd1e0047e23/README.md), [device adapter](https://github.com/narkco-kang/agent-fleet/blob/f2fd46afbebdc1df520dec7f5862edd1e0047e23/device-agent/src/adapters/cliRunner.ts), [scheduler gateway](https://github.com/narkco-kang/agent-fleet/blob/f2fd46afbebdc1df520dec7f5862edd1e0047e23/backend/src/services/scheduler.ts), [modelgateway OpenAI handler](https://github.com/narkco-kang/agent-fleet/blob/f2fd46afbebdc1df520dec7f5862edd1e0047e23/modelgateway/src/openai.ts).
- Basis: explicit + structural negative.
- Confidence: high for reviewed standard paths.
- Caveats: The stable Grok CLI path can run a genuine agent externally. Other advertised direct adapters have differing verification/scaffold status, which further bounds—not reverses—first-party attribution.

### Absence scope

- Surfaces inspected: README runtime responsibility matrix, scheduler and gateway execution, device task handler, direct CLI adapter and loop/teams service.
- Plausible first-party paths checked: Grok stable adapter, Claude/Codex text/stream adapters, gateway role completion, swarm expert personas, loop templates and provider failover.
- Why no material first-party path remains: None implements a first-party model/tool decision-feedback operational worker; each invokes somebody else's loop or makes one provider request and reports it.

## S2 — Coordination

- State: —
- Function: No first-party agent-owned inter-S1 interference attenuation and adaptive mutual adjustment is evidenced.
- Disturbance / variety regulated: Agent capacity claims, device saturation, offline workers and team target collisions are handled through deterministic routing/requeue.
- Decisive decision or feedback right: Interpret actual inter-worker interference and direct changed reciprocal worker behaviours; absent.
- Decision owner: User-configured team routes, `SwarmRouter` preference tiers and scheduler rules; external agent processes receive their prompts without a first-party conflict negotiation protocol.
- Supporting / enforcement mechanisms: `max_concurrency` claims, online-device filtering, team binding, manual/preferred/capability fallback and task queue.
- Closure path: Target exhausted/offline → scheduler selects another device or leaves task queued; no model-operated peer conflict interpretation/feedback to multiple S1 agent commitments.
- Why this is / is not agent-owned: Load balancing and deterministic binding attenuate capacity conflicts as infrastructure but do not establish agent-owned S2 between first-party autonomous S1 units.
- Evidence: [swarmRouter.ts](https://github.com/narkco-kang/agent-fleet/blob/f2fd46afbebdc1df520dec7f5862edd1e0047e23/backend/src/services/swarm/swarmRouter.ts), [scheduler.ts](https://github.com/narkco-kang/agent-fleet/blob/f2fd46afbebdc1df520dec7f5862edd1e0047e23/backend/src/services/scheduler.ts), [teamService.ts](https://github.com/narkco-kang/agent-fleet/blob/f2fd46afbebdc1df520dec7f5862edd1e0047e23/backend/src/services/teams/teamService.ts).
- Basis: structural.
- Confidence: high.
- Caveats: A downstream team may define its own model-based negotiation protocol on top, which is outside this shipped boundary.

### Absence scope

- Surfaces inspected: Swarm candidate resolution, role/team routing, agent claims, task scheduling, device failover and loop dependencies.
- Plausible first-party paths checked: Parallel specialist teams, per-device team bindings, model fallback, saturated-worker alternatives and shared memory sync.
- Why no material first-party path remains: These paths select targets or move tasks mechanically, without an agent-specific collision/feedback/changed-peer-commitment relation and without first-party agentic S1 cells.

## S3 — Inside-and-now control

- State: —
- Function: No model/parent-owned whole-system present resource/commitment decision loop over first-party operational agents is established.
- Disturbance / variety regulated: Capacity pressure, device failure, queued tasks, token budgets and offline routes.
- Decisive decision or feedback right: Judge whole-system priorities and reallocate operating commitments from an integrated current view; absent as a discretionary first-party agent decision.
- Decision owner: Operators configure teams/roles/limits and confirm actions; scheduler applies deterministic target scoring, task-state transitions and failure fallbacks.
- Supporting / enforcement mechanisms: Backend task registry, workload counters, roleRouter, loop scheduler, device heartbeat and usage ledger.
- Closure path: Device status/task state → deterministic queue selection/requeue → task dispatched or failed; no agent-owned whole-system priority/constraint amendment returned to an autonomous S1 organization.
- Why this is / is not agent-owned: The dashboard is a genuine whole-fleet view, but a view plus rules-based scheduling is not an agent choosing current organizational strategy/commitments.
- Evidence: [scheduler.ts](https://github.com/narkco-kang/agent-fleet/blob/f2fd46afbebdc1df520dec7f5862edd1e0047e23/backend/src/services/scheduler.ts), [roleRouter.ts](https://github.com/narkco-kang/agent-fleet/blob/f2fd46afbebdc1df520dec7f5862edd1e0047e23/backend/src/services/routing/roleRouter.ts), [loopScheduler.ts](https://github.com/narkco-kang/agent-fleet/blob/f2fd46afbebdc1df520dec7f5862edd1e0047e23/backend/src/services/loop/loopScheduler.ts).
- Basis: structural.
- Confidence: high for evaluated current-control paths.
- Caveats: Human configuration and confirmation are local operations approvals, not sufficient evidence of a separate parent S3 over first-party agentic work.

### Absence scope

- Surfaces inspected: Dashboard/current task model, scheduler, loop states, gateway health, role/team bindings, human action guard and usage ledger.
- Plausible first-party paths checked: Swarm capacity decisions, priority reassignments, model failover, cross-device recovery and expert-team loops.
- Why no material first-party path remains: All decisions are computed by fixed availability/capacity/step rules or made by operators setting task inputs; no autonomous or function-specific parent whole-system control feedback is established.

## S3* — Complementary audit

- State: —
- Function: No independent substantive audit of first-party S1 work reports returning correction to organizational control is evidenced.
- Disturbance / variety regulated: Lost tasks, stale devices and tampered ledger entries are detected by protocol/cryptographic checks.
- Decisive decision or feedback right: Independently challenge an agent's claimed task success against operational reality and return accountable corrections; absent.
- Decision owner: Process exit/status event, ledger hash/signature checks and operator dashboard; no distinct model-bearing reviewer is mandated to assess the actual work.
- Supporting / enforcement mechanisms: Event stream, task result records, hash-linked memory ledger, Merkle tree, signatures and benchmarks.
- Closure path: Transport/memory failures trigger rejected blocks or requeue; task completion follows external CLI exit status or gateway answer without an independent first-party correctness audit.
- Why this is / is not agent-owned: Tamper-evident logs and task telemetry are complementary evidence facilities, not an autonomous claim-versus-reality auditor with corrective authority.
- Evidence: [taskRunner.ts](https://github.com/narkco-kang/agent-fleet/blob/f2fd46afbebdc1df520dec7f5862edd1e0047e23/backend/src/services/taskRunner.ts), [CLI adapter](https://github.com/narkco-kang/agent-fleet/blob/f2fd46afbebdc1df520dec7f5862edd1e0047e23/device-agent/src/adapters/cliRunner.ts), [README.md](https://github.com/narkco-kang/agent-fleet/blob/f2fd46afbebdc1df520dec7f5862edd1e0047e23/README.md).
- Basis: structural.
- Confidence: medium-high.
- Caveats: A human/externally composed model team can audit stored evidence, but that is not AgentFleet's claimed first-party S3*.

### Absence scope

- Surfaces inspected: Task telemetry/final status, device failover, memory ledger checks, benchmark and team routing paths.
- Plausible first-party paths checked: Tamper-resistant logs, task result status, free-source probes and memory insights.
- Why no material first-party path remains: These secure/measure delivery and outcomes without a distinct task success audit judgment and return-to-correction right.

## S4 — Outside-and-then intelligence

- State: —
- Function: No autonomous or legitimate parent-governed prospective external-environment-to-capability adaptation closure at a first-party agentic harness boundary is shown.
- Disturbance / variety regulated: Provider failure, missing devices and history distribution are present availability/knowledge problems.
- Decisive decision or feedback right: Evaluate future operating alternatives and authorize durable capability/strategy changes based on environmental prospects; absent.
- Decision owner: Operators install agents, configure providers/models, assign teams and approve assets; auto-failover follows fixed configured options.
- Supporting / enforcement mechanisms: Provider availability probes, source ratings, deploy scripts, memory insights, model selection/fallback and asset distribution.
- Closure path: Provider fails → next configured provider or local fallback; memory events → indexes/insights. No internally owned prospective options → evaluation → authorized change to future operating capability is shown.
- Why this is / is not agent-owned: Changing a current failed provider is operational recovery, and an operator uploading future skills is a management interface, not evidenced first-party S4 adaptation.
- Evidence: [README.md](https://github.com/narkco-kang/agent-fleet/blob/f2fd46afbebdc1df520dec7f5862edd1e0047e23/README.md), [scheduler.ts](https://github.com/narkco-kang/agent-fleet/blob/f2fd46afbebdc1df520dec7f5862edd1e0047e23/backend/src/services/scheduler.ts), [assetService.ts](https://github.com/narkco-kang/agent-fleet/blob/f2fd46afbebdc1df520dec7f5862edd1e0047e23/backend/src/services/assets/assetService.ts).
- Basis: structural.
- Confidence: medium-high.
- Caveats: The repository offers useful human-led fleet evolution; no source-based prospective model adaptation authority is credited.

### Absence scope

- Surfaces inspected: Provider health/failover, deployment and asset APIs, memory insights, modelgateway and expert-role templates.
- Plausible first-party paths checked: Learned failure lessons, automatic model selection, fleet expansion/deployment and future roadmap assets.
- Why no material first-party path remains: All shown returns are fixed current routing or operator-initiated configuration, not an agent/parent-owned prospective adaptation at this boundary.

## S5 — Policy and identity

- State: —
- Function: No first-party autonomous organization-level ultimate-purpose/policy adjudication with authoritative return is evidenced.
- Disturbance / variety regulated: Device credentials, deployment safety, task permissions and token accounting are operational policies, not identity disputes.
- Decisive decision or feedback right: Legitimately redefine organization identity and binding policy in response to contested ultimate constraints; not supplied.
- Decision owner: Human operator sets roles, models, deployment authority and action approvals; code enforces static authentication and action guard.
- Supporting / enforcement mechanisms: Token pairing, explicit confirmation of install/uninstall/assets/loops, provider credential store and transport controls.
- Closure path: Human confirms a sensitive action → safe API dispatch; no purpose challenge → legitimate ultimate authority → binding policy decision → changed first-party autonomous operations.
- Why this is / is not agent-owned: Security controls and user confirmation are not a constitutional decision right over a self-governing agent organization.
- Evidence: [README.md, safety boundary](https://github.com/narkco-kang/agent-fleet/blob/f2fd46afbebdc1df520dec7f5862edd1e0047e23/README.md), [actionGuard.ts](https://github.com/narkco-kang/agent-fleet/blob/f2fd46afbebdc1df520dec7f5862edd1e0047e23/backend/src/services/actionGuard.ts), [modelgateway server](https://github.com/narkco-kang/agent-fleet/blob/f2fd46afbebdc1df520dec7f5862edd1e0047e23/modelgateway/src/server.ts).
- Basis: structural.
- Confidence: high within the reviewed standard distribution.
- Caveats: An external enterprise organization may govern an AgentFleet deployment; no such S5 is first-party evidenced here.

### Absence scope

- Surfaces inspected: Device registration/security, action confirmation, role/team configuration, policy/capacity guards and memory trust.
- Plausible first-party paths checked: Team identity/purpose fields, model approval, deploy/uninstall permissions, asset policy and cross-device trust key rotation.
- Why no material first-party path remains: These do not constitute an accountable identity/ultimate-policy dispute decision and return to autonomous first-party S1 operations.

## Distributed OSS parent arrangement

Open-source users host their own coordinator and independent external agent executables. Their humans may legitimately govern work, but a local dashboard/confirmation interface is not evidence of a shared higher-recursion S5 parent for a first-party AgentFleet agent organization.

## Self-hosted and non-human modes

Backend, device daemons, modelgateway and ledger may be self-hosted. Running meaningful software agents still requires preinstalled externally governed CLI software; a gateway-only configuration returns one chat answer per task. Neither mode supplies a first-party self-governing agentic S1 loop.

## Recursion

Devices, team tags and role/persona labels are routing units within a coordinator; the external coding agents own operational cognition, so their separate viable recursions cannot be imputed to AgentFleet.

## Variety and escalation

The platform absorbs device/provider availability variety by deterministic queue, claim, failover and replay machinery, with human confirmation for sensitive changes. When meaningful task-solving feedback occurs, the external agent processes it; the platform receives a terminal status. No higher agentic VSM loop is evidenced.

## Evidence gaps

- No live multi-device or paid coding-agent execution was run here; published benchmarks and CLI verification matrix were interpreted as source evidence, not independent measurement.
- Most advertised local adapters are marked scaffold or unverified in the repository's own capability matrix. Only the documented stable direct path is credited as available, and its cognition remains external.
- Optional future model-managed teams built by downstream operators could change the organizational boundary, but are not first-party shipped decision/closure evidence at this ref.

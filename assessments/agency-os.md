---
harness_id: agency-os
project_name: Agency-OS
repository: https://github.com/swarm-ai-research/agency-os
review_ref: 010d216b10cb6f504de27312de0112dc7782e4ee
reviewed_at: 2026-10-10
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# Agency-OS

## Review boundary

- System in focus: one Agency-OS running package-defined organization, API/CLI task-submission service, background worker fleet, persisted task ledger and instantiated model-driven BusinessAgents, with bidding/worker claims and configured governance.
- Purpose and identity: receive and execute customer tasks through provider-backed business agent work units while preventing duplicate executions, controlling budgets/permissions, and exposing task results.
- Relevant environment: customer requests, Python package agent specs, model providers, filesystem/tools, SQL database, tenants, money/token budgets, task failures and concurrent worker processes.
- Standard-distribution boundary: installed Python `agency_os` package, bundled package manifests and runtime `Organization`, factory, `BusinessAgent`, API/task worker, SQL task persistence; upstream SWARM LLM dependency and model providers used by actual execution. Benchmarks, autonomous harness-generation/dogfood features and unbound review examples do not contribute positive owner paths.
- Credited operating / distribution surfaces: `agency_os/{service/api/routers/tasks.py,worker.py,storage.py,agents/business_agent.py,agents/agent_factory.py,orchestration/organization.py}`; normal `agency-os run --task` and API with running TaskWorker.
- Adjacent first-party surfaces excluded from ownership: benchmark pipeline and evaluation protocols, experimental `autoharness`, optional QA feedback helpers not wired to task execution, developer tests/CI, external SWARM implementation internals and cloud model intelligence beyond the submitted task.
- First-party operating / deployment modes considered: installed package agent factory with provider model connection; API queued worker mode with multiple TaskWorkers; CLI task execution; governance preset with bid allocation and human approval for individual high-impact tasks.
- Recursion level: one running customer organization and task fleet; tenant operator, vendor org, test/benchmark agents and downstream separate organizations are different recursion.
- Reviewed revision: `010d216b10cb6f504de27312de0112dc7782e4ee`.
- Observation date: 2026-10-10.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

Agency-OS uses YAML package specs and an `AgentFactory` to instantiate BusinessAgents extending a SWARM LLM agent adapter; each retains role prompt, configured model, permissions, economic/reputation state and task-local `_call_llm_sync` capability. The runtime organization evaluates deterministic bids, elects a task owner, and in synchronous CLI mode may directly execute it. The API persists a task as `assigned` and a separate `TaskWorker` polls pending tasks. Before running an agent it invokes `Database.claim_task` with an atomic conditional SQL update from `assigned` to `executing`; one successful claimant performs `agent.execute_task` and records result, while other worker processes skip it. No undocumented agent collaboration is required to witness that first-party coordination seam.

Governance presets, permission denies, trust/circuit-breaker scoring, optional workflow/QA helper and telemetry surround the operating path. Per-task bidder choice and work queue concurrency do not by themselves establish whole-current S3. A `WorkflowEngine` with a supplied approval count and optional `FeedbackLoop` data class cannot be treated as a live independent S3* adjudicator without wiring to a reviewer and returned corrective execution. Historical trust weight and provider fallback are not automatically S4 prospective sensing, and YAML governance does not automatically settle S5 identity.

Sources: [README.md](https://github.com/swarm-ai-research/agency-os/blob/010d216b10cb6f504de27312de0112dc7782e4ee/README.md); [business_agent.py](https://github.com/swarm-ai-research/agency-os/blob/010d216b10cb6f504de27312de0112dc7782e4ee/agency_os/agents/business_agent.py); [agent_factory.py](https://github.com/swarm-ai-research/agency-os/blob/010d216b10cb6f504de27312de0112dc7782e4ee/agency_os/agents/agent_factory.py); [organization.py](https://github.com/swarm-ai-research/agency-os/blob/010d216b10cb6f504de27312de0112dc7782e4ee/agency_os/orchestration/organization.py); [tasks.py](https://github.com/swarm-ai-research/agency-os/blob/010d216b10cb6f504de27312de0112dc7782e4ee/agency_os/service/api/routers/tasks.py); [worker.py](https://github.com/swarm-ai-research/agency-os/blob/010d216b10cb6f504de27312de0112dc7782e4ee/agency_os/worker.py); [storage.py](https://github.com/swarm-ai-research/agency-os/blob/010d216b10cb6f504de27312de0112dc7782e4ee/agency_os/storage.py); [task_router.py](https://github.com/swarm-ai-research/agency-os/blob/010d216b10cb6f504de27312de0112dc7782e4ee/agency_os/orchestration/task_router.py).

## Operational model

Configured provider-backed BusinessAgents are the operational S1 cells. The first-party Python service allocates requests, a scalable worker consumes/executes them, and each model actor generates output under a package-specific prompt/permissions. In multi-worker deployments shared SQL task status prevents two worker processes from executing the same job. This is a narrow S2 constructor path distinct from the sealed-bid route (which allocates one new task and is not automatically a cross-S1 conflict). Current-control and independent-audit claims remain uncertain at the chosen recursion.

## S1 — Operations

- State: A
- Function: perform assigned business/coding analysis tasks through first-party instantiated model-driven BusinessAgent work cells and a model-call/response feedback path.
- Disturbance / variety regulated: user requests, changing task contexts, model outputs, tool authorization constraints and execution failures.
- Decisive decision or feedback right: configured LLM agent chooses substantive task response using its composed spec/system prompt and task context.
- Decision owner: BusinessAgent model actor instantiated by Agency-OS's factory in a running organization, with SWARM `LLMAgent` substrate bundled as a dependency; remote model inference remains external.
- Supporting / enforcement mechanisms: package manifests, agent spec parser, provider config, tenant-auth task queue, TaskWorker, local model invocation, cost/metering and outcome recording.
- Closure path: user/CLI/API submits task → organization allocates it to a BusinessAgent → persisted task claimed by worker → `agent.execute_task` passes sanitized task/context to `_call_llm_sync` → LLM response recorded as task result/trajectory and returned through client polling, permitting further work.
- Boundary reachability: `TaskWorker._execute_task` calls `BusinessAgent.execute_task` from a worker consumption loop, and CLI offers direct `org.submit_task(... execute=True)`; this is installed runtime, not only benchmarks.
- Why this is / is not agent-owned: without a hosted completion model, factory, queue and gates cannot produce discretionary task content, while deleting deterministic bid score calculations does not remove the model-owned task decision.
- Evidence: [business_agent.py](https://github.com/swarm-ai-research/agency-os/blob/010d216b10cb6f504de27312de0112dc7782e4ee/agency_os/agents/business_agent.py); [agent_factory.py](https://github.com/swarm-ai-research/agency-os/blob/010d216b10cb6f504de27312de0112dc7782e4ee/agency_os/agents/agent_factory.py); [worker.py](https://github.com/swarm-ai-research/agency-os/blob/010d216b10cb6f504de27312de0112dc7782e4ee/agency_os/worker.py); [tasks.py](https://github.com/swarm-ai-research/agency-os/blob/010d216b10cb6f504de27312de0112dc7782e4ee/agency_os/service/api/routers/tasks.py); [organization.py](https://github.com/swarm-ai-research/agency-os/blob/010d216b10cb6f504de27312de0112dc7782e4ee/agency_os/orchestration/organization.py); [cli.py](https://github.com/swarm-ai-research/agency-os/blob/010d216b10cb6f504de27312de0112dc7782e4ee/agency_os/service/cli.py)
- Basis: structural + explicit.
- Confidence: high in configured provider-backed mode.
- Caveats: the default BusinessAgent implementation is a bounded model-generated response path; code-writing/tool execution or autonomous coding substeps are not presumed from agent identity or unrelated benchmark examples. Provider/SWARM runtime dependencies are explicit.

## S2 — Coordination

- State: C
- Function: attenuate competing worker execution of one assigned shared task when multiple queue consumers concurrently observe an available task.
- Disturbance / variety regulated: two independently running TaskWorker processes can poll the same `assigned` task and both attempt an agent model execution, causing duplicated paid work and inconsistent task status/result recording.
- Decisive decision or feedback right: only one concurrent consumer may transition the task from `assigned` to `executing`; a loser must not execute this task.
- Decision owner: first-party SQLAlchemy database conditional-update transaction, not an agent negotiating or a language model deciding task ownership.
- Supporting / enforcement mechanisms: tenant/org task ledger, atomic `UPDATE tasks SET status=executing WHERE task_id=? AND status=assigned`, rowcount result, main worker polling loop and status transition.
- Closure path: two TaskWorker participants read the same pending task → both attempt `claim_task` → DB commits a single successful transition → loser receives `False` and skips execution → only admitted work cell calls the assigned BusinessAgent; later task result is persisted.
- Boundary reachability: both `storage.Database.claim_task` and `TaskWorker.run` are shipped runtime paths; API persists `assigned` tasks for workers. Scaling worker processes is explicitly supported.
- Why this is / is not agent-owned: the duplicate-execution collision is resolved by an atomic conditional gate, with no discretionary model choice of which runner receives a contested task.
- Distinct S1 units: two separate TaskWorker consumers, each able to instantiate/operate a BusinessAgent for the same organization, as concurrent execution work cells.
- Inter-S1 disturbance: duplicate processing of the same shared task would consume tokens/budget twice and race updates to task results, disrupting legitimate execution.
- Attenuating coordination relation: SQL conditional `status=assigned` compare-and-set permits exactly one transition to `executing`; only successful claimant proceeds to `_execute_task`.
- Feedback into subsequent S1 behaviour: the failed `claim_task` boolean prevents the unsuccessful consumer from entering model execution, so execution occurs once and the loser can poll other tasks.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the mechanism addresses an identified **cross-worker duplicate execution collision**, not selection of the best bidder, task ordering or message passing.
- Evidence: [storage.py](https://github.com/swarm-ai-research/agency-os/blob/010d216b10cb6f504de27312de0112dc7782e4ee/agency_os/storage.py); [worker.py](https://github.com/swarm-ai-research/agency-os/blob/010d216b10cb6f504de27312de0112dc7782e4ee/agency_os/worker.py); [tasks.py](https://github.com/swarm-ai-research/agency-os/blob/010d216b10cb6f504de27312de0112dc7782e4ee/agency_os/service/api/routers/tasks.py); [organization.py](https://github.com/swarm-ai-research/agency-os/blob/010d216b10cb6f504de27312de0112dc7782e4ee/agency_os/orchestration/organization.py)
- Basis: structural + explicit.
- Confidence: medium-high for concurrent worker mode.
- Caveats: this is narrowly queue-consumer S2; bid auctions are static one-task allocation and not inherently S2. It does not prove distributed file-write conflict resolution, autonomous S2 negotiation, or globally balanced worker fairness.

## S3 — Inside-and-now control

- State: ?
- Function: whole-current regulation of organization workload, active commitments and resource priorities rather than local per-task assignment and budget checking.
- Disturbance / variety regulated: uneven workloads, failed/frozen business agents and conflicts between active projects.
- Decisive decision or feedback right: per-task highest-bid selection and circuit-breaker gating are real but do not establish an owner deciding global current priorities/resource reallocations across the operating organization.
- Decision owner: configurable package/organization owner and deterministic bid sort / freeze-threshold code; no distinct whole-current S3 agent/controller established.
- Supporting / enforcement mechanisms: roster, task history, bid score, wallet and trust, model-call runtime, governance controls and owner APIs.
- Closure path: task arrives → algorithm picks one eligible agent → result recorded, but no demonstrated whole-current multi-task visibility → regulation decision → changed commitments across S1 units.
- Boundary reachability: auction and governance are first-party operational paths but fail the function-specific aggregate current-control criterion on current evidence.
- Why this is / is not agent-owned: a model executing one task or deterministic ranking individual bid scores does not own current management of the whole organization's portfolio.
- Whole-system current view: live agent roster and per-task history are stored, but no bound whole-current priority/commitment decision loop is evidenced.
- Current-control decision scope: winner selection for isolated tasks and failure gating, not global allocation governance.
- Evidence: [organization.py](https://github.com/swarm-ai-research/agency-os/blob/010d216b10cb6f504de27312de0112dc7782e4ee/agency_os/orchestration/organization.py); [task_router.py](https://github.com/swarm-ai-research/agency-os/blob/010d216b10cb6f504de27312de0112dc7782e4ee/agency_os/orchestration/task_router.py); [business_agent.py](https://github.com/swarm-ai-research/agency-os/blob/010d216b10cb6f504de27312de0112dc7782e4ee/agency_os/agents/business_agent.py); [worker.py](https://github.com/swarm-ai-research/agency-os/blob/010d216b10cb6f504de27312de0112dc7782e4ee/agency_os/worker.py); [governance.py](https://github.com/swarm-ai-research/agency-os/blob/010d216b10cb6f504de27312de0112dc7782e4ee/agency_os/service/api/routers/governance.py)
- Basis: structural + unresolved.
- Confidence: medium in incomplete mapping.
- Caveats: do not infer S3=A from the organization label or S3=P from any individual manager approval header.

## S3* — Complementary audit

- State: ?
- Function: challenge normal agent work claims through independent evidence access and return corrections.
- Disturbance / variety regulated: an agent reporting an output that fails requested tests or violates constraints.
- Decisive decision or feedback right: the optional review-workflow engine accepts caller-supplied evidence and approval counts; no guaranteed independently appointed reviewer with direct evidence and consequent correction loop is demonstrated in the shipped task-worker path.
- Decision owner: unknown; optional QA feedback can be passed into a helper but that helper is not automatically installed as an independent auditor.
- Supporting / enforcement mechanisms: `WorkflowEngine` minimum evidence/approval gates, `FeedbackLoop` helper, trajectory capture, trust/circuit breakers and audit event records.
- Closure path: a caller may set supplied approvals and evidence, and QA helper can output `rework`; no proven separate reviewer acquires raw evidence and returns a corrective instruction to the original executing agent through first-party live task worker.
- Boundary reachability: quality-gate helper and QA feedback class ship, but first-party runtime review execution and authority separation are not bound to the standard task pathway.
- Why this is / is not agent-owned: static evidence count and approval threshold do not constitute independent substantive audit judgment; benchmark auditors cannot be borrowed as deployed product audit actors.
- Claim being audited: the winning model agent completed an assigned task correctly.
- Ordinary reporting path: BusinessAgent result, task status and trajectory.
- Complementary access path: possible QA reviewer inspecting implementation/source outside worker claim, not shown as mandatory enacted workflow.
- Independence boundary: no independently instantiated reviewer plus direct artifact access established for this assessed operating mode.
- Who acts on findings: hypothetical coordinator or human; demonstrated feedback-to-original-worker closure absent.
- Evidence: [workflow_engine.py](https://github.com/swarm-ai-research/agency-os/blob/010d216b10cb6f504de27312de0112dc7782e4ee/agency_os/orchestration/workflow_engine.py); [feedback_loops.py](https://github.com/swarm-ai-research/agency-os/blob/010d216b10cb6f504de27312de0112dc7782e4ee/agency_os/orchestration/feedback_loops.py); [worker.py](https://github.com/swarm-ai-research/agency-os/blob/010d216b10cb6f504de27312de0112dc7782e4ee/agency_os/worker.py); [trajectory.py](https://github.com/swarm-ai-research/agency-os/blob/010d216b10cb6f504de27312de0112dc7782e4ee/agency_os/observability/trajectory.py); [pipeline.py](https://github.com/swarm-ai-research/agency-os/blob/010d216b10cb6f504de27312de0112dc7782e4ee/agency_os/benchmarks/pipeline.py)
- Basis: structural + unresolved.
- Confidence: medium in insufficient evidence.
- Caveats: S3* unknown, not absent; review/gate architecture is not enough for positive ownership.

## S4 — Outside-and-then intelligence

- State: ?
- Function: prospectively sense changes in the organization environment and develop future capability adaptation options.
- Disturbance / variety regulated: changing customer objectives and model/provider conditions.
- Decisive decision or feedback right: no first-party prospective environmental option-generation/selection/returned adaptation right established.
- Decision owner: unresolved.
- Supporting / enforcement mechanisms: trust/reputation scores, historical task success and failure, cost-aware task bids, memory decay and optional planning components.
- Closure path: task outcomes alter agent reputation and later bid scoring, but that is performance feedback for reactive per-task selection, not an independently evidenced outside-and-then prospecting/adaptation function.
- Boundary reachability: reputation and task selection are live; that is insufficient for S4.
- Why this is / is not agent-owned: static trust rules affecting future bids do not show a model/legitimate parent choosing new future organization capabilities.
- External distinction: no specific outside horizon monitoring path established.
- Future / prospective distinction: past outcome statistics influence subsequent route quality but are not necessarily prospective intelligence.
- Adaptation option generated: unverified.
- Path back into current capability / S3: no separate S4 adaptation decision and change authority.
- Evidence: [organization.py](https://github.com/swarm-ai-research/agency-os/blob/010d216b10cb6f504de27312de0112dc7782e4ee/agency_os/orchestration/organization.py); [business_agent.py](https://github.com/swarm-ai-research/agency-os/blob/010d216b10cb6f504de27312de0112dc7782e4ee/agency_os/agents/business_agent.py); [trust.py](https://github.com/swarm-ai-research/agency-os/blob/010d216b10cb6f504de27312de0112dc7782e4ee/agency_os/governance/trust.py); [executor.py](https://github.com/swarm-ai-research/agency-os/blob/010d216b10cb6f504de27312de0112dc7782e4ee/agency_os/planning/executor.py); [decay.py](https://github.com/swarm-ai-research/agency-os/blob/010d216b10cb6f504de27312de0112dc7782e4ee/agency_os/memory/decay.py)
- Basis: structural + unresolved.
- Confidence: medium in insufficiency.
- Caveats: this does not deny that a suitably configured research organization could have S4 at another recursion.

## S5 — Policy and identity

- State: ?
- Function: ultimate purpose and legitimate policy identity of the whole organization when fundamental authority conflicts arise.
- Disturbance / variety regulated: changes to organizational mission and legitimate authority rather than per-task tool access.
- Decisive decision or feedback right: human defines agent roles, wallets, governance preset, charters, tool denies and high-impact approval; no distinct ultimate-policy-level dispute and authoritative return is reconstructed.
- Decision owner: configuring operator/tenant for ordinary policy, no proven S5 identity decision owner.
- Supporting / enforcement mechanisms: package YAML, governance preset, permission checker, budget and circuit-breaker policy, task approval headers and API auth.
- Closure path: configuration and manager approval affect task admission, but do not show identity/purpose change proposal → legitimate parent decision → returned governance for future operations.
- Boundary reachability: governance parameters are shipped, but not automatically S5.
- Why this is / is not agent-owned: budget/permissions enforcement and labels such as governance are not the constitutive policy decision itself.
- Identity / ultimate-policy issue: no concrete policy identity conflict with closure found.
- Ultimate authority in each claimed mode: no positive S5 autonomous or parent mode claimed.
- Return-to-operation path: per-task permission choices returned; no identity-level closure evidenced.
- Evidence: [README.md](https://github.com/swarm-ai-research/agency-os/blob/010d216b10cb6f504de27312de0112dc7782e4ee/README.md); [schema.py](https://github.com/swarm-ai-research/agency-os/blob/010d216b10cb6f504de27312de0112dc7782e4ee/agency_os/packages/schema.py); [presets.py](https://github.com/swarm-ai-research/agency-os/blob/010d216b10cb6f504de27312de0112dc7782e4ee/agency_os/governance/presets.py); [tasks.py](https://github.com/swarm-ai-research/agency-os/blob/010d216b10cb6f504de27312de0112dc7782e4ee/agency_os/service/api/routers/tasks.py); [governance.py](https://github.com/swarm-ai-research/agency-os/blob/010d216b10cb6f504de27312de0112dc7782e4ee/agency_os/service/api/routers/governance.py)
- Basis: structural + unresolved.
- Confidence: medium in insufficient evidence.
- Caveats: human approval of a high-impact task is a local permission gate, not a demonstrated identity-level S5 process.

## Distributed OSS parent arrangement

The open-source project maintainer team and SWARM library authors are not the runtime owner of each deployed customer organization. Package configuration is supplied by tenant/operator; this does not establish autonomous S5 or whole-current S3.

## Self-hosted and non-human modes

Task workers run without the UI actively connected, consuming persistent assigned jobs under tenant constraints; the actual task response requires a provider-backed model. If the runtime operates without concurrent workers, the cross-worker conflict seam is available as constructor but no S2 collision occurs in that simple deployment. Human manager approval is an admission condition on some requests, not proof of a full parent S3/S5 mode.

## Recursion

One package-defined running organization is the focus. Individual BusinessAgent jobs are S1 work units, worker processes are execution carriers of those agents, and their shared SQL queue regulates a concrete duplicate-job disturbance. Separate customer tenants, SaaS enterprise governance and SWARM package maintainers are outside this recursion.

## Variety and escalation

Models absorb task-level input and response variety; deterministic per-task bidding and SQL exclusive claim distribute work without double processing; wallets/permissions/circuit breakers limit unsafe execution. Logs and optional QA libraries support potential later auditing but do not prove an enacted independent S3* reviewer. Error/approval escalation is recorded separately from higher functions.

## Evidence gaps

- Live provider-backed API TaskWorker execution and two-process claim race were not run during this pinned-source review; replicate to confirm concurrent exactly-once task execution and budget accounting.
- Investigate whether deployed whole-org current resource balancing exists beyond one-task auctions before upgrading S3.
- Separate review quality gates from independently bound auditor tool access and corrective return before S3* promotion.
- Prospective environmental adaptation and ultimate-policy identity closure were not established; do not import benchmarks/autoharness agents as product owners.

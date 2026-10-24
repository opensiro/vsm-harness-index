---
harness_id: afc-runtime
project_name: AFC Runtime (woafc-runtime)
repository: https://github.com/philngt/afc-runtime
review_ref: 204647311304ca0f40334a27ac3a152700144a4f
reviewed_at: 2026-10-20
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: C
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# AFC Runtime (woafc-runtime)

## Review boundary

- System in focus: Public `philngt/afc-runtime` generic file-queue runtime, domain-neutral DAG compiler and headless runtime-adapter/supervisor for agent-runner tasks; standalone first-party Python runtime library plus optional independently packaged Telegram assistant transport. Assess **the runtime constructor**, not an unprovided product-specific workflow instance or its model.
- Purpose and identity: Safely transport, claim, run, checkpoint and finish task envelopes through externally configured agent runtimes, with queue.v2 receipt binding, deterministic promotion/finalisation and synthetic tests. It is not itself an end-to-end autonomous business/content agent.
- Relevant environment: An externally supplied thin workflow instance with `runtime/workspace.json`, `runtime/roles.json`, `runtime/fleet.json`, runtime descriptor, domain/pipeline data, handlers, contracts, model credentials, independent tools, task files and optional Telegram host gateway. Operational success beyond synthetic tests needs an actual configured instance and agent runner.
- Standard-distribution boundary: `wo_runtime/core/pipeline.py`, `queue/commands.py`, `worker.py`, `orchestrator/core.py`, `runtime/{supervisor,resolve,start,fleet_plan}.py`, reusable queue contract schema and CLI. For the optional Telegram package only shipped transport/allowlist and explicit host factory interface are credited; external host authorization/approval/runtime policy remains excluded.
- Credited operating / distribution surfaces: [`README.md`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/README.md); [`docs/CORE.md`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/docs/CORE.md); [`docs/QUEUE.md`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/docs/QUEUE.md); [`docs/PRIMITIVES.md`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/docs/PRIMITIVES.md); [`wo_runtime/core/pipeline.py`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/wo_runtime/core/pipeline.py); [`wo_runtime/runtime/supervisor.py`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/wo_runtime/runtime/supervisor.py); [`wo_runtime/runtime/fleet_plan.py`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/wo_runtime/runtime/fleet_plan.py); [`wo_runtime/runtime/start.py`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/wo_runtime/runtime/start.py); [`wo_runtime/runtime/resolve.py`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/wo_runtime/runtime/resolve.py); [`wo_runtime/queue/commands.py`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/wo_runtime/queue/commands.py); [`wo_runtime/orchestrator/core.py`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/wo_runtime/orchestrator/core.py); [`wo_runtime/worker.py`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/wo_runtime/worker.py); [`plugins/telegram-assistant/README.md`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/plugins/telegram-assistant/README.md).
- Adjacent first-party surfaces excluded from ownership: `wo_runtime/testing.py` synthetic selftest; CI/GitLab release checks; developer `AGENTS.md`, workflows and copy-paste authoring prompt; example prompts for product videos; plugin test fixtures and package build; externally owned thin-instance `src/` product handler and provider configuration. These may corroborate intended constructor interfaces but do **not** supply an autonomous actor or governing institutional mandate to the pinned runtime.
- First-party operating / deployment modes considered: `wo-runtime core plan` request compiler, queue claim/terminal with receipt fencing, generic headless supervisor with selected runtime descriptor and role watches, optional interactive agent start/Stop-hook integration, deterministic orchestrator tick/daemon, bounded retry/recovery, opt-in Telegram plugin using an explicit host gateway, synthetic selftest. No substantive default model/runtime descriptor, product workflow, external backend or live agent is included in this repo.
- Recursion level: A configured instance's request/task production workflow; runtime package is a first-party *constructor of a possible autonomous S1 workstream*, whereas domain/agent decisions remain to be composed by the instance.
- Reviewed revision: `philngt/afc-runtime@204647311304ca0f40334a27ac3a152700144a4f`; immutable Git tree `28383aa1e3dfca0f659057dc0bb66e2b165cd992`; GitHub repository ID `1297966484`; public, nonfork, nonarchived, Apache-2.0, originally created 2026-07-12T04:02:42Z.
- Observation date: 2026-10-20.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

`wo_runtime` explicitly separates runtime-owned queue primitives and receipt validation from instance-owned product domain and policy. `core/pipeline.py` compiles a request into a queue task DAG using data from a supplied workspace's domain and pipeline profiles, assigning dependencies, stage fan-out, input aliases and contract references. `queue/commands.py` owns atomic exact-task claim with lease/attempt/fencing metadata and terminal success/failure/requeue; `worker.py` checks environment receipt identity and provides bound terminal operations. The queue cannot autonomously select a substantive answer. [`README.md`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/README.md); [`docs/CORE.md`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/docs/CORE.md); [`docs/QUEUE.md`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/docs/QUEUE.md); [`wo_runtime/core/pipeline.py`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/wo_runtime/core/pipeline.py); [`wo_runtime/queue/commands.py`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/wo_runtime/queue/commands.py); [`wo_runtime/worker.py`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/wo_runtime/worker.py).

`runtime/supervisor.py` can watch configured role queues and launch multiple headless child processes from runtime descriptors with limits and role/task claim receipts. Interactive launch is supported in separate `start.py` mode. `orchestrator/core.py` performs reconcile, watchdog, failed-dependency recovery, promotion and finalisation passes, allowing host callbacks at named hook points. These are first-party executable task-control and S1 constructor mechanisms, but autonomous reasoning, provider keys, model choice and product semantics must come from **an instance that is not bundled here**. A deterministic queue/orchestrator must not be credited as the autonomous actor. [`wo_runtime/runtime/supervisor.py`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/wo_runtime/runtime/supervisor.py); [`wo_runtime/runtime/start.py`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/wo_runtime/runtime/start.py); [`wo_runtime/runtime/resolve.py`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/wo_runtime/runtime/resolve.py); [`wo_runtime/orchestrator/core.py`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/wo_runtime/orchestrator/core.py); [`wo_runtime/runtime/fleet_plan.py`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/wo_runtime/runtime/fleet_plan.py).

The separate `plugins/telegram-assistant` package is disabled until an instance starts it explicitly with a named gateway factory; its own documentation says the host owns approval, authorization, SQLite truth, prompts and backends. It is not an alternate shipped human-governed S5 or autonomous model agent. The source ships synthetic queue and plugin unit tests; they validate code-level paths, not real task performance. [`plugins/telegram-assistant/README.md`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/plugins/telegram-assistant/README.md); [`wo_runtime/testing.py`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/wo_runtime/testing.py); [`wo_runtime/runtime/selftest.py`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/wo_runtime/runtime/selftest.py).

## Operational model

A host creates a thin workflow instance with real agent runtime descriptors and product handlers. The first-party runtime compiles request context and enforces exact-claim leases; an external selected autonomous agent can then interpret the task, choose actions and report a result. The generic orchestrator's subsequent decisions depend on predetermined queue rules or host callbacks. Since the source contains a specific composable external-agent call path but *no included autonomous decision actor*, the appropriate positive publication state is S1 **C** (constructor), not S1 A or exclusion. All higher VSM functions were tested for separate ownership, not inferred from infrastructure names.

## S1 — Operations

- State: C
- Function: **Constructor** for an agent-executed task-to-result workstream: the first-party queue safely introduces a real externally configured headless agent runtime to an assigned task and preserves its returned result, but does not supply the model or task-specific autonomous decision policy.
- Disturbance / variety regulated: Task and workspace input variability, dependencies/fan-out, provider/runner errors, unreliable partial writes, duplicate workers, stale claims, timeouts, and failures under restart.
- Decisive decision or feedback right: The *prospective* autonomous worker invoked through an instance-provided descriptor can choose what work to do within the prompt and call tools, then submit a task result through a bound receipt. At the pinned first-party repo, the runtime itself chooses only when to claim, launch, retry, requeue or finalise a task according to predefined policies; the discretionary model/executor and its substantive task strategy are not packaged here.
- Decision owner: Constructor surface: first-party generic supervisor/queue/worker adapter; missing decisive autonomous actor: an externally supplied instance runtime descriptor and its headless model agent/handler. The external instance owns product/domain policy, model identity, prompts and actual task completion decisions.
- Supporting / enforcement mechanisms: Core request→pipeline DAG compiler, queue.v2 claims/leases/heartbeat/fencing, Supervisor.run role watch/headless descriptor invocation, BoundClaim.from_environment binding, RuntimeTerminal.complete/fail, generic orchestrator promotion/finalisation, hooks and optional wrappers.
- Closure path: Configured external workflow instance request → compile instance-defined DAG → staged queue task → first-party supervisor atomically claims exact task and launches instance-selected headless model runtime with bounded context and task receipt → externally composed agent decides actions/produces result → worker terminal commits result against current lease → deterministic orchestrator releases dependent task/finalises. This is **a specific first-party S1 construction seam**, but independent autonomous task policy is not closed inside this repository.
- Why this is / is not agent-owned: The repo intentionally stays runtime-neutral and has no default model, task handler, provider keys, domain policy or end-to-end business workflow instance. Its supervisor, queue and launcher alone cannot select next semantic actions; configure an external model agent and prompt in a thin instance to close the autonomous S1 decision loop.
- Evidence: [`README.md`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/README.md); [`wo_runtime/runtime/supervisor.py`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/wo_runtime/runtime/supervisor.py); [`wo_runtime/runtime/fleet_plan.py`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/wo_runtime/runtime/fleet_plan.py); [`wo_runtime/runtime/start.py`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/wo_runtime/runtime/start.py); [`wo_runtime/runtime/resolve.py`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/wo_runtime/runtime/resolve.py); [`wo_runtime/queue/commands.py`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/wo_runtime/queue/commands.py); [`wo_runtime/worker.py`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/wo_runtime/worker.py); [`wo_runtime/core/pipeline.py`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/wo_runtime/core/pipeline.py); [`wo_runtime/orchestrator/core.py`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/wo_runtime/orchestrator/core.py); [`docs/PRIMITIVES.md`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/docs/PRIMITIVES.md); [`docs/WORKFLOW-AUTHORING.md`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/docs/WORKFLOW-AUTHORING.md).
- Basis: Explicit first-party actor-construction path; no external model decision rights are imported into the pinned repo.
- Confidence: High for `C` rather than `A` on the declared distribution boundary.
- Caveats: The published artifact is a generic assembly dependency; `selftest` verifies synthetic queue mechanics but does not execute a real model or independently verify productive behavior. Product-specific endpoints supplied by consumers may be autonomous in a different assessed boundary.
- Boundary reachability: The first-party supported `wo-runtime runtime supervisor`, `runtime start`, queue claim and `RuntimeTerminal` entry points are all shipped and documented for instances: a task's claim is bound to an executable child-runtime invocation and fenced terminal receipt. The *model/agent that decides task content* must still be composed from the external instance, which is exactly why the state is C.

## S2 — Coordination

- State: —
- Function: No actual S2-specific relation attenuating disturbances between separately viable, mutually affecting autonomous S1 operating units; only deterministic queue/dependency mechanics for parts of a single configured product workstream.
- Disturbance / variety regulated: Distinct roles may share claimable queues, dependency slots or worker replicas; stale leases and workload contention cause duplicate/late results.
- Decisive decision or feedback right: Atomic claim/fencing, queue ordering, capacity caps and DAG promotion protect integrity and schedule tasks according to host policy. No first-party agent monitors/negotiates cross-unit conflict or changes reciprocal operating behavior among independent viable S1 departments.
- Decision owner: Queue file locks and supervisor/host-provided role mappings; not an independent coordination decision owner.
- Supporting / enforcement mechanisms: Role watches, queue.v2 lock/claim/requeue, fixed concurrency caps, fan-out/depends_on edges, strict dependency-result resolution.
- Closure path: One task result → released dependencies and another worker claim; load/race conflict → deterministic lease winner/rejection. This is work sequencing/data safety, not inter-S1 mutual-disturbance control.
- Why this is / is not agent-owned: Role labels and replica counts denote interchangeable worker services for sub-tasks; even parallel roles do not by themselves prove viability as autonomous continuing organizations. No coordination policy or returned change to separate S1 departmental commitments is shipped.
- Evidence: [`docs/QUEUE.md`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/docs/QUEUE.md); [`wo_runtime/runtime/supervisor.py`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/wo_runtime/runtime/supervisor.py); [`wo_runtime/queue/commands.py`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/wo_runtime/queue/commands.py); [`wo_runtime/orchestrator/core.py`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/wo_runtime/orchestrator/core.py); [`wo_runtime/core/pipeline.py`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/wo_runtime/core/pipeline.py); [`docs/CORE.md`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/docs/CORE.md).
- Basis: Bounded negative at the runtime-neutral, per-workflow instance-construction recursion.
- Confidence: High.
- Caveats: Two real business departments could be connected by a bespoke instance; their mutual-regulation authority is absent from this runtime package.

### Absence scope

- Surfaces inspected: First-party pipeline compiler, queue.v2 state transitions and locks, role/fleet watches, multi-replica supervisor and output dependency matching.
- Plausible first-party paths checked: Checked worker-role distinctions, queue backpressure, lease conflicts, task DAG fan-out, independent terminal outputs and instance hooks as candidate S2 relationships.
- Why no material first-party path remains: All inspected controls are generic sequencing, work admission and integrity support inside a single supplied workflow. No distinct continuing viable S1 units nor separate inter-unit variety damping judgment/feedback into their subsequent commitments is shipped.

## S3 — Inside-and-now control

- State: —
- Function: No independently owned current management of a whole set of separately viable S1 operating departments through discretionary priorities, commitments or resource allocation.
- Disturbance / variety regulated: Queued and blocked tasks, crashed workers, lease expiration, budget exhaustion, stuck supervisor passes, dependency failures, false terminal states.
- Decisive decision or feedback right: Supervisor enforces configured replica limits, hard claim lease and subprocess timeouts; Orchestrator passes reconcile/timeout, promotion, failed dependencies and finalisation. These are transparent deterministic operational controls; optional host hooks supply actual domain decisions. The external instance must compose any current management.
- Decision owner: Deterministic Python orchestrator/supervisor under config selected by host, with optional host hook callback; not a standing autonomous or parent-governed S3 decision owner.
- Supporting / enforcement mechanisms: Role/fleet launch plan, selftest, watchdog and finalisation, typed task and result validation, queue receipt fencing, hook calls before/after tick or finalisation.
- Closure path: Task status changes → process restart/retry, requeue, promotion/failure or terminal finalisation following static rules. No whole multi-viable-S1 current management account → substantive discretionary priority/resource commitment → returned S3 decision to separate units.
- Why this is / is not agent-owned: Having fleet totals and automatically recovering tasks is execution governance, not a task-owning, independent metasystem. An instance-defined `after_final_success` hook does not close missing S3 by itself; author/operator governance is outside the source-bound runtime.
- Evidence: [`wo_runtime/runtime/supervisor.py`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/wo_runtime/runtime/supervisor.py); [`wo_runtime/orchestrator/core.py`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/wo_runtime/orchestrator/core.py); [`wo_runtime/runtime/fleet_plan.py`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/wo_runtime/runtime/fleet_plan.py); [`docs/PRIMITIVES.md`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/docs/PRIMITIVES.md); [`README.md`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/README.md); [`docs/CORE.md`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/docs/CORE.md).
- Basis: Specific S3 candidates considered: watchdog, budget, scheduler, fleet config and host recovery hooks; function-specific ownership absent.
- Confidence: High.
- Caveats: Deployed tenants might have parent managers; no first-party top-level S3 mandate and return loop exists in this library's released distribution.

### Absence scope

- Surfaces inspected: Supervisor concurrency, role/fleet configuration, child deadlines, queue watchdog, orchestrator promotion/failed-dependency/finalisation, recovery hooks and runtime CLI.
- Plausible first-party paths checked: Whole-fleet view and static lease/budget enforcement as potential current executive; external host `before_tick` / `after_final_success` as possible supervisor/parent-managed decisions.
- Why no material first-party path remains: Generic engine observes execution states but cannot itself judge and reallocate obligations/resources across independently viable operating businesses. Instance hook contracts delegate policy to absent external owner; no first-party autonomous or closed parent-governed S3 decision loop.

## S3* — Complementary audit

- State: —
- Function: No independent complementary reality-audit channel that challenges an S3 manager's normal reports and returns a corrective finding to that manager.
- Disturbance / variety regulated: Stale task receipts, duplicated worker claims, schema-invalid output, missing dependency results, forged status or wrong delivery receipt.
- Decisive decision or feedback right: Receipt fencing and output schema validation are independent of some untrusted worker claims; synthetic audits/tests check them, but there is no distinct S3 current-control reporting path to audit or independent site-inspection judgment returned to S3.
- Decision owner: Deterministic verifier and file-queue gate or host-provided instance validator; no S3* auditor with separate evidence access or S3 finding recipient.
- Supporting / enforcement mechanisms: queue.v2 claim lease IDs, attempt guards, bound worker receipts, validation schemas, finalization hooks and audit/event files.
- Closure path: Worker result → same queue terminal acceptance/fail closed; audit/event lines → optional host observation. No S3 manager claim → independent reality route → organizational discrepancy judgment → S3 corrective resource/priority change.
- Why this is / is not agent-owned: Data integrity checks can be separate from an individual worker's assertion and remain valuable; they do not amount to a complementary organizational truth auditor with systemic management return.
- Evidence: [`docs/QUEUE.md`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/docs/QUEUE.md); [`wo_runtime/queue/commands.py`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/wo_runtime/queue/commands.py); [`wo_runtime/worker.py`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/wo_runtime/worker.py); [`wo_runtime/orchestrator/core.py`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/wo_runtime/orchestrator/core.py); [`wo_runtime/core/validation.py`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/wo_runtime/core/validation.py); [`docs/PRIMITIVES.md`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/docs/PRIMITIVES.md).
- Basis: Bounded negative after checking independent receipt verification, result schema validation, event logging and watchdog.
- Confidence: High.
- Caveats: An instance may build an independent QA or forensic audit node, but the first-party runtime does not assign it S3* mandate.

### Absence scope

- Surfaces inspected: Claim fencing, schema validation, lock receipt bindings, terminal idempotency, audit/event files and generic orchestrator watchdog.
- Plausible first-party paths checked: Direct task evidence and mismatch detection as a candidate separate audit route, and whether a managerial report and corrective S3 decision owner exist.
- Why no material first-party path remains: These checks validate single task acceptance against a stable queue contract. No audited organizational S3 ordinary-report path, complementary direct field check over separate viable operations, independence mandate or returned S3 corrective decision is supplied.

## S4 — Outside-and-then intelligence

- State: —
- Function: No autonomous or supported parent-governed outside-and-then strategic intelligence generating and adopting longer-term capability adaptations.
- Disturbance / variety regulated: External client requirements and channels may change; worker timeouts, repeated task errors and quotas generate tactical need for recovery.
- Decisive decision or feedback right: Static instance-defined pipeline profiles choose stage paths and fan-out; supervisor quota backoff and workflow authoring instructions describe future workflow creation by host/developer. Runtime does not independently observe external trends, formulate strategic options, accept a future change or update subsequent current capability.
- Decision owner: Externally configured workflow instance or human developer, not an embedded strategic actor; deterministic retry/backoff state.
- Supporting / enforcement mechanisms: Pipeline compiler, profile defaults and routing by request fields, quota-state backoff, runtime launcher descriptors, authoring documentation and plugin packaging.
- Closure path: Configured input → existing pipeline/task DAG; runtime error → short-term retry/requeue/backoff; developer may separately revise instance config. There is no independent future intelligence → adaptation-option selection → binding returned update to organizational capability or S3.
- Why this is / is not agent-owned: Selection among predeclared branches and recovery from failures are current-execution reactions, not autonomous future-planning/strategic learning. An instruction for a developer to author a new workflow is not an implemented S4 decision/return.
- Evidence: [`wo_runtime/core/pipeline.py`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/wo_runtime/core/pipeline.py); [`wo_runtime/runtime/supervisor.py`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/wo_runtime/runtime/supervisor.py); [`docs/WORKFLOW-AUTHORING.md`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/docs/WORKFLOW-AUTHORING.md); [`docs/CORE.md`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/docs/CORE.md); [`README.md`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/README.md); [`plugins/telegram-assistant/README.md`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/plugins/telegram-assistant/README.md).
- Basis: Bounded no material S4 actor/constructor on examined shipped code and supported plugin/instance boundaries.
- Confidence: High.
- Caveats: Future thin workflow instances can add learning/strategy; those would belong to that deployment's assessment.

### Absence scope

- Surfaces inspected: Request pipeline stage selection, runtime descriptors and fleet settings, quota retries/backoff, recovery, workflow authoring docs and optional Telegram integration.
- Plausible first-party paths checked: Potential future capability adjustment through instance config updates, workflow-generation instruction templates or learning from quota failures.
- Why no material first-party path remains: The runtime neither generates strategic environmental distinctions nor autonomously commits an accepted changed policy/capability; source-bounded dynamic paths only choose previously configured stages or recover existing tasks.

## S5 — Policy and identity

- State: —
- Function: No first-party constitutional policy/identity decision owner for a continuing organization, internally or through a closed parent mandate.
- Disturbance / variety regulated: Unsafe path traversal, unauthorized Telegram ingress, duplicate terminal acceptance, secrets disclosure and prohibited manually dispatched tasks.
- Decisive decision or feedback right: Schema/path/claim checks enforce predetermined rules; optional Telegram assistant is off by default and its actual authorization, approvals, SQLite truth, prompts and model backends are explicitly supplied by a host workspace gateway factory.
- Decision owner: Host/instance developer supplies policy and credentials; transport/runtime enforces them mechanically rather than establishing a legitimate parent S5 decision about mission and identity.
- Supporting / enforcement mechanisms: Queue contract guardrails, role/fleet descriptors, per-plugin exact allowlist, no imported plugin at runtime core, manualOnly denial, terminal claims.
- Closure path: Host configuration → local permitted/denied request or task; if enabled, named Telegram host adapter → message/authorization. No purpose/identity issue → recognized ultimate authority judgment → returned constitutional decision changing current S1–S4 operation.
- Why this is / is not agent-owned: Administrative guardrails and local human approval belong to task security and workflow configuration, not S5; the first-party package declares its own lack of ownership over user/account policy.
- Evidence: [`plugins/telegram-assistant/README.md`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/plugins/telegram-assistant/README.md); [`docs/QUEUE.md`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/docs/QUEUE.md); [`wo_runtime/core/validation.py`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/wo_runtime/core/validation.py); [`wo_runtime/runtime/supervisor.py`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/wo_runtime/runtime/supervisor.py); [`README.md`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/README.md); [`docs/PRIMITIVES.md`](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/docs/PRIMITIVES.md).
- Basis: Negative claim bounded to published optional and core first-party capabilities, considering parent-assisted possibilities.
- Confidence: High.
- Caveats: An external workflow instance or organization may have actual governing policy; no shipped legitimate parent authority and returned systemic decision has been shown.

### Absence scope

- Surfaces inspected: Core queue contract path/security checks, manualOnly rule, host role/fleet config, opt-in Telegram allowlist and named gateway factory.
- Plausible first-party paths checked: Developer-specified access controls and human approval as candidate parent governance or ultimate-policy enforcement.
- Why no material first-party path remains: First-party only enforces specific security/transport rules. Identity and legitimate ultimate policy belong explicitly to an unprovided external host; no S5 decision, recognized parent mandate and returned organizational policy closure is packaged.


## Recursion

This runtime is intentionally not the workflow *instance* and not an autonomous provider. It exposes a specific constructor path for an independent model-guided S1 workstream after a host supplies agent runtime, credentials, prompts, workflow and outputs. Queue worker classes and stage roles are not independently viable businesses; task-level deterministic control is not S3 at a larger management recursion. Human institutional policies or downstream deployment could establish functions in their own assessed boundary, but cannot be silently imported here.

## Variety and escalation

Stale task claims, bad dependency inputs, lost worker subprocesses, lease deadlines and duplicated completion are handled by path safety, locks, fencing, watchdog, quarantine, requeue and configured retry. An external agent, if composed, would react to semantic task variety through its own tools/model and return fenced output. The generic runtime does not provide algedonic S3/S5 governance merely because some task has status `failed` or an error event. Hard queue safety boundaries remain explicit and are not a security review of user-provided agent code.

## Evidence gaps

- Reviewed exact public SHA and shipping first-party code. The repository intentionally omits the thin product workflow instances, model provider, agent prompts and business acceptance criteria; these omissions are substantive for the **C** vs **A** boundary.
- `python3 -m compileall -q wo_runtime` **PASS**, `python3 bin/wo-runtime selftest --synthetic-workspace` **PASS**, optional Telegram `PYTHONPATH=src python3 -m unittest discover -s tests -q` **11/11 PASS** at the frozen source. All are synthetic or unit checks, **not evidence that a live model autonomously completed a real task**.
- No live external model or tenant instance was launched and no first-party function-specific higher management/strategic/policy mandate was found. This does not assert that users cannot construct those functions downstream.

---
harness_id: deepseek-super-agent
project_name: DeepSeek Super Agent
repository: https://github.com/LofiSu/deepseek-super-agent
review_ref: a1985c06b2c1520f14b54817e22f73542f9e2d7d
reviewed_at: 2026-11-04
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
autonomy_s5: —
---

# DeepSeek Super Agent

## Review boundary

- System in focus: the installable `ds-agent` TypeScript runtime and its first-party Main Agent / Executor ticket organization, not DeepSeek's prototype or any connected organization.
- Purpose and identity: process inbound events into scoped, model-directed agent work and deliver bounded replies or task outcomes through channels.
- Relevant environment: local filesystem/sandbox, human operators, model providers, configured channels (CLI, Feishu, GitHub-style), asynchronous jobs and shared worker capacity.
- Standard-distribution boundary: shipped `src/runtime.ts`, Engine, Harness, Ingress, Store, channel adapters and CLI/daemon modes at the frozen revision; optional configured services credited only where actually wired. External model APIs provide reasoning but their unrelated organization is excluded.
- Credited operating / distribution surfaces: [Runtime assembly](https://github.com/LofiSu/deepseek-super-agent/blob/a1985c06b2c1520f14b54817e22f73542f9e2d7d/src/runtime.ts#L343-L626), [Harness loop](https://github.com/LofiSu/deepseek-super-agent/blob/a1985c06b2c1520f14b54817e22f73542f9e2d7d/src/harness/loop.ts#L88-L175), [Engine](https://github.com/LofiSu/deepseek-super-agent/blob/a1985c06b2c1520f14b54817e22f73542f9e2d7d/src/core/engine.ts), [CLI](https://github.com/LofiSu/deepseek-super-agent/blob/a1985c06b2c1520f14b54817e22f73542f9e2d7d/src/cli/main.ts), [module wiring note](https://github.com/LofiSu/deepseek-super-agent/blob/a1985c06b2c1520f14b54817e22f73542f9e2d7d/docs/MODULES.md).
- Adjacent first-party surfaces excluded from ownership: `test/`, CLI demo/bakeoff, benchmarking metrics, the `PLAN.md` future roadmap and unmounted remote-mesh network listeners; the cited DeepSeek reference article/prototype and external channel/model providers do not donate decisions.
- First-party operating / deployment modes considered: local CLI `chat`/`serve` and channel loops with a live model; configured Main/Executor sessions; operator `panel`/`pause`/`intervene`/`resume`; keyless MockModel and offline demos considered only as evidence/limitations, not proof of autonomous live outcomes.
- Recursion level: installed local runtime spanning several Tickets/Executor operational cells; spawned team members are decomposition unless separate viability is evidenced.
- Reviewed revision: `a1985c06b2c1520f14b54817e22f73542f9e2d7d`.
- Observation date: 2026-11-04.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Ingress filters and records Triggers. The Engine groups them by Thread, applies a deterministic Gate and defers uncertain admission to a model-backed Main Agent before creating a Mandate/Ticket/Assignment. Router sessions are sequence points; separate Executor Sessions run an asynchronous model/tool loop, with job completions returning as further prompts. SQLite persists tickets, assignments, subscriptions, session journals and outbox entries; the in-process Harness capacity queue and mesh placement regulate concurrent work. A daemon ticks a deterministic Watchdog. Operator CLI commands can pause, supply guidance and resume tickets. Runtime data and model-provided judgments must be distinguished from the fixed Go/TypeScript mechanisms and operator authority. External model endpoints, Feishu/GitHub servers, `bwrap`/`sandbox-exec` and unmounted cross-host transports remain environment/dependencies. [README architecture](https://github.com/LofiSu/deepseek-super-agent/blob/a1985c06b2c1520f14b54817e22f73542f9e2d7d/README.md#L141-L223); [module implementation limits](https://github.com/LofiSu/deepseek-super-agent/blob/a1985c06b2c1520f14b54817e22f73542f9e2d7d/docs/MODULES.md#L29-L94).

## Operational model

Each live Ticket's Executor produces the environment-facing outcome: tool activity and a report within a Mandate. The Main Agent can accept/ignore/stop uncertain input and sequence work, but is not shown a whole-system current-control view merely by being called Main. Distinct Executor tickets share finite worker capacity and a durable event store. Operators can inspect a system-wide execution panel and intervene in ongoing work. The deterministic Gate, worker placement, sandbox and watchdog enforce constraints without inheriting the choices of the model or operator. [Assessment entrypoint](https://github.com/LofiSu/deepseek-super-agent/blob/a1985c06b2c1520f14b54817e22f73542f9e2d7d/src/core/assessment.ts#L29-L105); [panel](https://github.com/LofiSu/deepseek-super-agent/blob/a1985c06b2c1520f14b54817e22f73542f9e2d7d/src/core/panel.ts#L27-L76).

## S1 — Operations

- State: A
- Function: Executor Session performs assigned user/environment work through a model-directed tool loop.
- Disturbance / variety regulated: task contents, model/tool observations, errors and asynchronous job completions in each Ticket's local work environment.
- Decisive decision or feedback right: select tool calls, interpret results and produce/continue the task report within the accepted Mandate.
- Decision owner: the configured model-backed Executor agent in live-model mode.
- Supporting / enforcement mechanisms: session journal, role-restricted tool registry, SQLite state, environment/sandbox and async job callbacks.
- Closure path: Executor's model/tool turns receive outputs and completion prompts, issue subsequent calls or report results into the Engine; the Ticket state and outbox preserve the outcome.
- Boundary reachability: `Runtime.create` assembles Harness, Engine, role models and tools; live CLI/channel execution launches Executor sessions on accepted Tickets. Keyless MockModel is not counted as a live provider outcome.
- Why this is / is not agent-owned: the Executor model chooses actions; deterministic tool execution and sandbox limits do not choose the task response.
- Evidence: [Harness launch and Worker sequencing](https://github.com/LofiSu/deepseek-super-agent/blob/a1985c06b2c1520f14b54817e22f73542f9e2d7d/src/harness/loop.ts#L91-L145), [model/tool turn](https://github.com/LofiSu/deepseek-super-agent/blob/a1985c06b2c1520f14b54817e22f73542f9e2d7d/src/harness/loop.ts#L650-L800), [worker tools](https://github.com/LofiSu/deepseek-super-agent/blob/a1985c06b2c1520f14b54817e22f73542f9e2d7d/src/harness/tools.ts), [runtime evaluation and launch](https://github.com/LofiSu/deepseek-super-agent/blob/a1985c06b2c1520f14b54817e22f73542f9e2d7d/src/runtime.ts#L860-L887).
- Basis: structural.
- Confidence: high for source wiring; provider-backed effectiveness not measured.
- Caveats: `serve` without a live provider defers assessments; remote execution placement remains an optional, separately mounted boundary.

## S2 — Coordination

- State: C
- Function: prevent inter-Executor overcommit and unstable competition for limited shared worker-node capacity.
- Disturbance / variety regulated: several Tickets can demand the same bounded mesh slots while each independently pursues work.
- Decisive decision or feedback right: assign one ticket to an eligible least-loaded node or defer it until capacity returns; an agent-owned negotiation of these shared allocations is not provided.
- Decision owner: built-in deterministic mesh/scheduler mechanisms under operator-configured capacity; an autonomous S2 decision owner would require composition.
- Supporting / enforcement mechanisms: per-ticket placement accounting, bounded FIFO and queue rejection, terminal release hooks.
- Closure path: a full node causes the Executor launch to park; when the prior Assignment ends and releases a slot, the Harness re-reads the Ticket and starts the queued Executor, changing later S1 behavior.
- Boundary reachability: runtime wires `WorkerMeshRegistry.pickNode/release` into Harness `startOrQueue` and `pumpQueue`; this is in the normal local process even though remote mesh network dispatch is not mounted.
- Why this is / is not agent-owned: the inter-S1 anti-overcommit relation is real, but node choice/FIFO are rule-driven, not model-owned coordination discretion.
- Distinct S1 units: two or more independently running Executor Sessions attached to different live Tickets.
- Inter-S1 disturbance: simultaneous demand for bounded worker-node slots would overcommit the shared execution resource.
- Attenuating coordination relation: per-ticket capacity reservation, least-loaded selection, FIFO wait, and release-driven retry.
- Feedback into subsequent S1 behaviour: a parked Ticket only runs after capacity is freed and its current live/paused state is rechecked.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the capacity conflict arises **between operational Executors**, and the reservation/queue specifically prevents competing concurrent launches; generic Router sequencing or Thread subscriptions alone are not credited.
- Evidence: [mesh registry](https://github.com/LofiSu/deepseek-super-agent/blob/a1985c06b2c1520f14b54817e22f73542f9e2d7d/src/harness/mesh.ts#L1-L90), [start/queue/pump](https://github.com/LofiSu/deepseek-super-agent/blob/a1985c06b2c1520f14b54817e22f73542f9e2d7d/src/harness/loop.ts#L147-L320), [runtime release](https://github.com/LofiSu/deepseek-super-agent/blob/a1985c06b2c1520f14b54817e22f73542f9e2d7d/src/runtime.ts#L431-L502), [module limitation](https://github.com/LofiSu/deepseek-super-agent/blob/a1985c06b2c1520f14b54817e22f73542f9e2d7d/docs/MODULES.md#L29-L75).
- Basis: structural.
- Confidence: medium; S2-specific structural conflict/closure is explicit, but discretionary inter-unit negotiation is not shipped.
- Caveats: this does not turn the deterministic node picker into autonomous S2; the `C` state describes its function-specific first-party path, not general message or queue availability.

## S3 — Inside-and-now control

- State: P
- Function: an installed human/operator oversight mode for current work commitments across Tickets.
- Disturbance / variety regulated: blocked/paused/overlong Tickets, conflicting current commitments and operator-directed corrections during active work.
- Decisive decision or feedback right: inspect active ticket/mandate/report state, then choose a ticket to pause, correct or resume on behalf of the local installed operation.
- Decision owner: the legitimate operator of the local runtime, not the deterministic CLI or Main Agent.
- Supporting / enforcement mechanisms: `executionView` panel over all Tickets, persisted collaboration flags, CLI commands, runtime hooks and per-step pause guards.
- Closure path: operator review of the whole current panel → `pause`/`intervene`/`resume` command → durable guidance/hold flag → Executor's next turn observes guidance or stops until resumed.
- Boundary reachability: `ds-agent panel`, `pause`, `intervene` and `resume` are shipped local CLI paths; `Runtime.resume` invokes `Harness.resume` when the Ticket is live.
- Why this is / is not agent-owned: the model may decide its own local actions and an admission decision, but the whole-current supervisory intervention is selected by the operator; the CLI merely records/enforces it.
- Whole-system current view: `executionView` derives all visible Tickets with mandate, state, last report, session, subscriptions and delivery counts from Store facts.
- Current-control decision scope: operator holds/corrects/resumes ongoing work in light of the all-Ticket panel; this is a supported supervisory **mode**, not a claim that every run is human-reviewed.
- Evidence: [panel materialization](https://github.com/LofiSu/deepseek-super-agent/blob/a1985c06b2c1520f14b54817e22f73542f9e2d7d/src/core/panel.ts#L27-L77), [CLI interventions](https://github.com/LofiSu/deepseek-super-agent/blob/a1985c06b2c1520f14b54817e22f73542f9e2d7d/src/cli/main.ts#L570-L630), [runtime return path](https://github.com/LofiSu/deepseek-super-agent/blob/a1985c06b2c1520f14b54817e22f73542f9e2d7d/src/runtime.ts#L899-L937), [Harness pause guards](https://github.com/LofiSu/deepseek-super-agent/blob/a1985c06b2c1520f14b54817e22f73542f9e2d7d/src/harness/loop.ts#L624-L668).
- Basis: structural.
- Confidence: medium; source exhibits reachable operator closure, but no cross-organization management is inferred.
- Caveats: the model-based Main Agent's trigger admission does not by itself prove S3; per-ticket CLI correction without the whole-current panel would not suffice. Only this bounded local parent mode is credited.

## S3* — Complementary audit

- State: —
- Function: no sufficiently independent complementary audit of Executor claims established in the shipped mode.
- Disturbance / variety regulated: potential divergence between reported completion/progress and operational reality; the available checks primarily see the internal Ticket/Job state.
- Decisive decision or feedback right: no audit-specific independent evidence judgment with return into current control identified.
- Decision owner: not established.
- Supporting / enforcement mechanisms: deterministic Watchdog heartbeat/failed-job/marker checks, health and metrics, development tests and demo probes.
- Closure path: Watchdog nudges/fails jobs on its internal signals; this is an ordinary control path, not independent audit of the claimed result.
- Why this is / is not agent-owned: a separately named Watchdog role and external-to-Executor timer do not create complementary access to operational artifacts by themselves.
- Evidence: [Watchdog signals/actions](https://github.com/LofiSu/deepseek-super-agent/blob/a1985c06b2c1520f14b54817e22f73542f9e2d7d/src/watchdog/watchdog.ts#L13-L178), [module notes](https://github.com/LofiSu/deepseek-super-agent/blob/a1985c06b2c1520f14b54817e22f73542f9e2d7d/docs/MODULES.md#L288-L294).
- Basis: structural.
- Confidence: medium-high for the declared installed boundary.
- Caveats: downstream users may compose independent audit outside this first-party distribution.

### Absence scope

- Surfaces inspected: Watchdog, role tools, persisted reports, health/metrics, bundled tests and demo/benchmark separation.
- Plausible first-party paths checked: watchdog's stale/job/drift detection and feedback; model watchdog commands; normal report and evaluation/demo data; optional channel outcomes.
- Why no material first-party path remains: checks read internal heartbeat/report/job markers or development fixtures, not a sufficiently independent complementary observation that challenges claimed operational results with corrective return in the standard distribution.

## S4 — Outside-and-then intelligence

- State: —
- Function: no shipped external-and-prospective capability adaptation closure established at the installed organization boundary.
- Disturbance / variety regulated: changes in future environment, provider or task demands could call for capability change, but current primitives handle ticket intake and memory reuse.
- Decisive decision or feedback right: no first-party model/operator capability-revision option/decision loop tied to future environmental distinctions is established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: persistent long-term recall, trigger filters/shards, speculative assignments, metrics/bakeoff and the roadmap.
- Closure path: recall changes context for later operational work; it does not select and install future capability options as an S4 loop.
- Why this is / is not agent-owned: trigger responses, worker plans and durable memory remain current operational learning/support, not future-oriented organizational adaptation.
- Evidence: [long-term memory](https://github.com/LofiSu/deepseek-super-agent/blob/a1985c06b2c1520f14b54817e22f73542f9e2d7d/src/memory/long-term.ts), [speculative gate](https://github.com/LofiSu/deepseek-super-agent/blob/a1985c06b2c1520f14b54817e22f73542f9e2d7d/src/speculate/gate.ts), [module limitations](https://github.com/LofiSu/deepseek-super-agent/blob/a1985c06b2c1520f14b54817e22f73542f9e2d7d/docs/MODULES.md#L173-L229).
- Basis: structural.
- Confidence: medium.
- Caveats: a product operator could separately revise code or models; no first-party prospective S4 decision-and-return path was demonstrated.

### Absence scope

- Surfaces inspected: Ingress, long-term memory, prospective plans, speculative assignments, role tools, tests and module roadmap.
- Plausible first-party paths checked: recall from finished tickets, dynamic shard routing, model role selection, speculative execution/deliver gate, metrics-driven experiments.
- Why no material first-party path remains: the shipped transitions route or remember current tasks; benchmark/roadmap activity is adjacent and does not feed a selected external/future adaptation option back into current installed capability.

## S5 — Policy and identity

- State: —
- Function: no operational identity/ultimate-policy arbitration and return loop established at the declared runtime recursion.
- Disturbance / variety regulated: authorization, admissibility and task scope are constrained, but potential identity-level policy conflicts are not routed to a legitimate ultimate authority with a returned decision.
- Decisive decision or feedback right: no first-party ultimate-policy revision/settlement path; the policy gate and mandate construction apply existing task rules.
- Decision owner: not established for S5. Developers/operator configure policies outside the run; ordinary human intervention is S3/task scope, not identity-level governance.
- Supporting / enforcement mechanisms: deterministic Gate, version-labelled Mandate, ingress allowlists and per-task human pause/guidance.
- Closure path: Gate decisions accept, defer, ignore or stop tasks; no identity/ultimate-policy matter → parent decision → changed operative policy path is wired.
- Why this is / is not agent-owned: model `accept`/`ignore` is admission discretion and an ordinary authorization matter; static versioned policy text is not an S5 owner.
- Evidence: [policy gate](https://github.com/LofiSu/deepseek-super-agent/blob/a1985c06b2c1520f14b54817e22f73542f9e2d7d/src/core/policy.ts), [assessment](https://github.com/LofiSu/deepseek-super-agent/blob/a1985c06b2c1520f14b54817e22f73542f9e2d7d/src/core/assessment.ts#L29-L105), [known policy limitation](https://github.com/LofiSu/deepseek-super-agent/blob/a1985c06b2c1520f14b54817e22f73542f9e2d7d/docs/DOMAIN_ALIGNMENT.md#L100-L109).
- Basis: structural.
- Confidence: medium-high for bounded runtime policy path.
- Caveats: the GitHub maintainer's general development governance is an adjacent recursion and not an installed S5 parent mode.

### Absence scope

- Surfaces inspected: Policy Gate, Main Agent assessment, mandate state, CLI intervention, external channel admission, policy docs and contributor/product boundary.
- Plausible first-party paths checked: `Policy.version`/rules, operator approvals, intake scope revisions, runtime config and human intervention commands.
- Why no material first-party path remains: these apply static policy or resolve current task-level matters; the shipped distribution lacks a function-specific identity/ultimate-policy escalation, authoritative settlement and return into subsequent policy-governed operation.

## Distributed OSS parent arrangement

The public maintainers and contributors are outside the deployed local agent/ticket organization. Their PRs, releases and design decisions are not treated as first-party S3/S4/S5 parent governance for an installed run. The S3 `P` finding is limited to the *local operator* supervising the installed runtime via shipped CLI controls and current-state panel.

## Self-hosted and non-human modes

Self-hosted live-model and MockModel modes differ: keyless `serve` can keep deferred work pending, which is not evidence of autonomous live completions. Local operator interventions are separately supported; no alternative autonomous S3 or parent-governed S4/S5 closure is inferred from optional provider choice or static policy files.

## Recursion

Each Executor Ticket is a bounded operational cell with its own Session and task environment. Team-member jobs and router shards do not establish complete recursive viable systems solely through spawning, role naming, or separate persistence.

## Variety and escalation

Filtering/Thread grouping attenuate incoming event variety; session tools and model reasoning amplify each Executor's response repertoire. Shared mesh capacity is attenuated through reservation/FIFO, and Watchdog/current-state intervention provides exception routes. Human guidance returns to live work, but this is neither independent audit nor identity-level policy closure. Local sandbox/network restrictions and missing true cross-host transport bound what outcomes are reachable.

## Evidence gaps

- Source tracing and documented unit/demo modes were inspected; no live paid model, Feishu/GitHub network delivery, remote mesh, or sandboxed upstream end-to-end run was performed for this assessment.
- The degree to which model-mediated Main Agent decisions could exercise whole-system current control in custom deployments is unresolved; no extra autonomous S3 mode is credited without a shipped whole-current discretion/return witness.
- The optional future multi-host/semantic memory paths in roadmap or adapters are not credited as shipped S4/S5 functions.

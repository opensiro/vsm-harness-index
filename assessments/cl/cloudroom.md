---
harness_id: cloudroom
project_name: Cloudroom
repository: https://github.com/davidondrej/cloudroom
review_ref: 112f097c8a38c771d233270047f541761a81530a
reviewed_at: 2026-11-10
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Cloudroom

**Proposed disposition:** `excluded-no-agentic-vsm` at the first-party Cloudroom Core/GUI control-plane boundary. This is not a claim that Cloudroom cannot host autonomous coding agents: it deliberately hosts external agent CLIs and provides substantial, durable execution infrastructure. Their autonomous judgment remains owned by those native harnesses.

## Review boundary

- System in focus: Cloudroom's first-party Rust Core, desktop GUI, authenticated HTTP API, native CLI adapters, child-session delivery, workspace sandboxing, recording, recovery and teleport controls.
- Purpose and identity: keep otherwise independent coding-agent CLI sessions alive, isolated, observable and portable across cloud/local environments without replacing their underlying reasoning engines.
- Relevant environment: Codex, Claude Code, Pi, OpenCode and other externally implemented CLIs and their model providers, machine/disk availability, OS process isolation, Git checkouts, cloud host/API and human desktop operator.
- Standard-distribution boundary: Core `Manager` receives authenticated request IDs, launches/configures a selected native harness in a sandbox, records native events and queues/relays prompts, controls its process lifecycle and recovery. The native harness owns its model→tool→observation loop, tools, inference, retries and compaction; it is not implemented by Cloudroom Core.
- Credited operating / distribution surfaces: [README](https://github.com/davidondrej/cloudroom/blob/112f097c8a38c771d233270047f541761a81530a/README.md), [explicit harness ownership contract](https://github.com/davidondrej/cloudroom/blob/112f097c8a38c771d233270047f541761a81530a/core/docs/harnesses.md), [session manager](https://github.com/davidondrej/cloudroom/blob/112f097c8a38c771d233270047f541761a81530a/core/src/session/mod.rs), [child sessions](https://github.com/davidondrej/cloudroom/blob/112f097c8a38c771d233270047f541761a81530a/core/src/session/children.rs), [API](https://github.com/davidondrej/cloudroom/blob/112f097c8a38c771d233270047f541761a81530a/core/docs/api.md), [lifecycle/replay](https://github.com/davidondrej/cloudroom/blob/112f097c8a38c771d233270047f541761a81530a/core/docs/session-lifecycle.md), [storage guard](https://github.com/davidondrej/cloudroom/blob/112f097c8a38c771d233270047f541761a81530a/core/src/session/guard.rs).
- Adjacent first-party surfaces excluded from ownership: contributor AGENTS instructions, bundled skill text delivered to external agents, GUI marketing/demo, CI/tests/fixture agents, hosted website organization and external model/CLI implementations; their reasoning or repository governance is not donated to Core.
- First-party operating / deployment modes considered: self-hosted Rust service, hosted per-thread sandbox and GUI, configured native adapters, local/cloud teleport, child session spawning and relay, background jobs, queued prompts, scheduled automation, dashboard, recover/sleep/stop and disk-safety guard.
- Recursion level: one Cloudroom control-plane instance managing one or more externally implemented coding-agent sessions. Parent/child session records do not alone establish first-party autonomous metasystem ownership.
- Reviewed revision: `112f097c8a38c771d233270047f541761a81530a` (Index intake #3035).
- Observation date: 2026-11-10.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The [README](https://github.com/davidondrej/cloudroom/blob/112f097c8a38c771d233270047f541761a81530a/README.md) explicitly says Cloudroom runs coding agents as their own CLIs in isolated branches/sandboxes, with Core providing process, queue, history and recovery. The [native harness contract](https://github.com/davidondrej/cloudroom/blob/112f097c8a38c771d233270047f541761a81530a/core/docs/harnesses.md) assigns inference, agent loop, tools, retries and compaction to each native agent. Core's [API](https://github.com/davidondrej/cloudroom/blob/112f097c8a38c771d233270047f541761a81530a/core/docs/api.md) accepts start/prompt/interrupt/steer/stop/reorder/recover/teleport commands with durable receipts, then dispatches them to selected native harnesses. Parent/child thread relations, replies, notices and relays are functional, but their substantive planning comes from the attached external agent's decision to spawn, tell or stop. The [session lifecycle](https://github.com/davidondrej/cloudroom/blob/112f097c8a38c771d233270047f541761a81530a/core/docs/session-lifecycle.md) is robust against crash/retry uncertainty, including fsynced queues, native resume and fail-closed storage. These are real operational capabilities; their enforcement does not turn Core into an autonomous coding-agent decision loop.

Counterfactual owner test: remove Codex, Claude Code, Pi and other native agent CLIs while keeping Cloudroom's Core, GUI, API, sandbox, scheduler, child-thread transport, skills and history store. Core can still validate requests, manage sessions, protect storage, transport text and present dashboards, but cannot itself understand an open-ended coding objective, autonomously choose file/tool actions from observations and continue toward the task goal. That decisive S1 right sits in the external harness.

## Operational model

- Actual outcome: a durable, observable and recoverable remote/native coding-agent execution environment; its coding outcome is produced by the launched native agent.
- S1 units in deployment: native CLI sessions, including optional children spawned by external agents, each with its own model/tool loop. They are integrated *as external decision owners* rather than authored by Cloudroom Core.
- Ownership split: Cloudroom selects and enforces infrastructure lifecycle, queue ordering by API request, resource guard and data persistence; external CLIs decide semantic operations; operator selects agents/credentials/sandboxes and sends commands.

## S1 — Operations

- State: —
- Function: an autonomously deciding, feedback-driven repository task unit is not first-party-owned at this Core boundary.
- Disturbance / variety regulated: Core handles process crashes, session startup, queue/lifecycle uncertainty and storage conditions; external native agents handle code/task distinctions and tool observations.
- Decisive decision or feedback right: interpret a software-engineering goal, select next file/tool operation, judge observations and revise the plan; owned by separately installed native CLI harness.
- Decision owner: Codex/Claude/Pi/OpenCode/etc. runtime chosen by configuration or API; Cloudroom's `Manager` has no independent model-driven semantic execution actor.
- Supporting / enforcement mechanisms: runtime adapters, authenticated request receipts, sandbox/container separation, session journal, child relays and teleport.
- Closure path: user or parent-agent prompt → Core receipt/dispatch → native CLI model/tool loop → native observation and next action → Core event/history transport. The task's adaptive action decision closes *inside the external CLI*, not Core.
- Boundary reachability: Core's adapter is runnable in supported deployments, but the [harnesses contract](https://github.com/davidondrej/cloudroom/blob/112f097c8a38c771d233270047f541761a81530a/core/docs/harnesses.md) requires separately configured native CLI and login; no Core-owned equivalent agent loop is shipped.
- Why this is / is not agent-owned: isolating and dispatching an autonomous external process does not transfer its internal semantic decision right to the process manager.
- Evidence: [README ownership split](https://github.com/davidondrej/cloudroom/blob/112f097c8a38c771d233270047f541761a81530a/README.md), [harness adapters](https://github.com/davidondrej/cloudroom/blob/112f097c8a38c771d233270047f541761a81530a/core/docs/harnesses.md), [Core API](https://github.com/davidondrej/cloudroom/blob/112f097c8a38c771d233270047f541761a81530a/core/docs/api.md), [session manager](https://github.com/davidondrej/cloudroom/blob/112f097c8a38c771d233270047f541761a81530a/core/src/session/mod.rs).
- Basis: explicit architectural ownership and static structural inspection.
- Confidence: high for first-party Core/native-harness boundary.
- Caveats: Cloudroom deployments *do* execute real autonomous agents, but they are external engines and are assessed separately if their own first-party harnesses enter Index.

### Absence scope

- Surfaces inspected: README, adapter contracts, native provider configuration, Core session start/child/relay, API, queued prompts, lifecycle/recovery and bundled skill entry.
- Plausible first-party paths checked: native child agent integration, bundled skills, scheduled prompt delivery, multi-session transport, CLI command guard, hosted sandbox image and GUI automation.
- Why no material first-party path remains: every semantic model/tool feedback loop requires an externally authored native agent runtime; Core has no substituting model/tool-step chooser.

## S2 — Coordination

- State: —
- Function: no first-party autonomous S2-specific adaptive regulation of inter-S1 interference is established.
- Disturbance / variety regulated: multiple native sessions can share directories, queue messages and child/parent reports, with potential resource/disk contention.
- Decisive decision or feedback right: an external parent agent may decide to spawn or message children; Core transports and persists requests and applies fixed filesystem/process rules, without discretionary coordination of conflicting agent commitments.
- Decision owner: external parent native agent/user; Core's child ledger, route, outbox and worker queues are deterministic.
- Supporting / enforcement mechanisms: [child-session adapter](https://github.com/davidondrej/cloudroom/blob/112f097c8a38c771d233270047f541761a81530a/core/src/session/children.rs), `relay`, persistent prompt/receipt queue, per-process sandbox and startup semaphore.
- Closure path: `room-cli thread spawn` or API child request creates another native session; child result is returned to parent as a notice/response. This is delegated work/result transport, not an evidenced S2-specific resolution of a concrete inter-S1 conflict with subsequent adjusted operations.
- Why this is / is not agent-owned: messages, child status and serial queues can support an externally built coordinator; they do not themselves show first-party material conflict attenuation owned by an autonomous S2 actor.
- Evidence: [child start and result](https://github.com/davidondrej/cloudroom/blob/112f097c8a38c771d233270047f541761a81530a/core/src/session/children.rs), [API child/relay/reorder contract](https://github.com/davidondrej/cloudroom/blob/112f097c8a38c771d233270047f541761a81530a/core/docs/api.md), [session lifecycle](https://github.com/davidondrej/cloudroom/blob/112f097c8a38c771d233270047f541761a81530a/core/docs/session-lifecycle.md).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: a third-party parent agent may deliberately coordinate its children at another assessed boundary; not a Core-owned mode.

### Absence scope

- Surfaces inspected: child-session creation, local and cross-sandbox relay, queued prompts, process startup concurrency, disk guards and shared workspace isolation.
- Plausible first-party paths checked: parent notices, child reply forwarding, tell/stop/archive, receipt queues, worker admission and per-thread sandboxing.
- Why no material first-party path remains: no identified Core-owned inter-S1 conflict judgment/feedback relation, only routing, isolation and deterministic capacity constraints.

## S3 — Inside-and-now control

- State: —
- Function: no whole-system discretionary current-control decision loop owned by Cloudroom or a qualifying parent mode is demonstrated.
- Disturbance / variety regulated: lost sessions, running/queued jobs, memory/disk pressure, startup races and failed native handshakes are observed and enforced under rules.
- Decisive decision or feedback right: no agent chooses current priorities/commitments across the whole portfolio from a comprehensive live supervisory view; operator API actions target selected sessions or request queues.
- Decision owner: human user sends selected commands; Core manages deterministic recovery/safety thresholds; external native agents decide their own work.
- Supporting / enforcement mechanisms: `/v1/dashboard` aggregated read-only summary, session state machine, request receipts, startup semaphore, idle sleep, disk guard that pauses/stops work under configured thresholds.
- Closure path: resource sample or session status → Core fixed safety/recovery rule or UI state → state change/failed receipt; not a new discretionary choice that reallocates system-wide work.
- Why this is / is not agent-owned: even globally enforced storage pause is a prewritten safety predicate; it does not endow Core with adaptive whole-current planning. Dashboard is explicitly read-only; local user stop/resume is not automatically S3=P.
- Evidence: [dashboard read-only semantics](https://github.com/davidondrej/cloudroom/blob/112f097c8a38c771d233270047f541761a81530a/core/docs/dashboard.md), [storage guard](https://github.com/davidondrej/cloudroom/blob/112f097c8a38c771d233270047f541761a81530a/core/src/session/guard.rs), [session recovery](https://github.com/davidondrej/cloudroom/blob/112f097c8a38c771d233270047f541761a81530a/core/docs/session-lifecycle.md).
- Basis: structural.
- Confidence: medium-high for Core; GUI human supervision not behaviorally tested.
- Caveats: safety and crash recovery are sophisticated and useful, but ownership requirements are stricter than runtime robustness.

### Absence scope

- Surfaces inspected: aggregated dashboard, session API, lifecycle, storage guard, startup capacity control and human GUI controls.
- Plausible first-party paths checked: dashboard counts, session states, queue reorder, global disk pause, per-session stop/resume and child status reports.
- Why no material first-party path remains: observed actions are read-only summaries, deterministic enforcement or isolated operator actions, not an evidenced owner-mediated whole-system current-control portfolio loop.

## S3* — Complementary audit

- State: —
- Function: no first-party independent complementary assessment of agent output claims and returned corrective judgment is established.
- Disturbance / variety regulated: process errors, uncertain receipts, invalid checkpoints, external task correctness and tool failure are tracked as lifecycle facts, not audited operational claims.
- Decisive decision or feedback right: Core validates protocol integrity and records native events; agent output quality/review remains in external harnesses, users and optional skills.
- Decision owner: deterministic receipt/checkpoint validators and human/external auditors, not a first-party complementary auditor.
- Supporting / enforcement mechanisms: native event journal, startup/exit assertions, receipt status, history replay, dashboard, and optional external review skills.
- Closure path: rejected checkpoint or uncertain native request changes session readiness/receipt; there is no independent operational artifact inspection reporting a claim-relative finding into later agent control.
- Why this is / is not agent-owned: source integrity/transport verification is not a separate audit of the coding agent's substantive claimed work; user reviews and external CLI skills are not Core-owned audit judgment.
- Evidence: [session lifecycle/replay](https://github.com/davidondrej/cloudroom/blob/112f097c8a38c771d233270047f541761a81530a/core/docs/session-lifecycle.md), [API history](https://github.com/davidondrej/cloudroom/blob/112f097c8a38c771d233270047f541761a81530a/core/docs/api.md), [native adapter separation](https://github.com/davidondrej/cloudroom/blob/112f097c8a38c771d233270047f541761a81530a/core/docs/harnesses.md).
- Basis: structural.
- Confidence: medium-high.
- Caveats: optional external coding-agent reviewer skill could add a different audit scope in a configured deployment.

### Absence scope

- Surfaces inspected: native session event recording, receipt and checkpoint validation, API event readback, GUI dashboard, native skills/adapters.
- Plausible first-party paths checked: process-health verification, reconciliation after crash, persisted tool results, user diff review and external agent review skills.
- Why no material first-party path remains: no complementary evidence path plus independent judgment about operational claims returned to the originating agent as corrective governance.

## S4 — Outside-and-then intelligence

- State: —
- Function: no prospectively sensing and selecting durable future agent-organization adaptation path owned by Core is established.
- Disturbance / variety regulated: host availability, new native harness versions and network conditions affect service deployment, but installed Core tracks primarily immediate runtime readiness.
- Decisive decision or feedback right: user/developer chooses software upgrades, native harness providers and configuration; Core does not generate and select strategic capability changes.
- Decision owner: human/developer external to runtime organization; deterministic updater/config and scheduled transports are support.
- Supporting / enforcement mechanisms: harness discovery/catalogs, setup/update scripts, session recording, skills sync, telemetry and cloud/local transfer.
- Closure path: service discovers configured harnesses and serves selected capability lists; updates and chosen future policies come from outside the managed runtime rather than a first-party prospective agent loop.
- Why this is / is not agent-owned: synchronizing skills, adding adapters and executing scheduled prompts are not themselves an autonomous outside-and-then intelligence/option/selection return cycle.
- Evidence: [README scope](https://github.com/davidondrej/cloudroom/blob/112f097c8a38c771d233270047f541761a81530a/README.md), [adapter setup](https://github.com/davidondrej/cloudroom/blob/112f097c8a38c771d233270047f541761a81530a/core/docs/harnesses.md), [API capabilities](https://github.com/davidondrej/cloudroom/blob/112f097c8a38c771d233270047f541761a81530a/core/docs/api.md).
- Basis: structural.
- Confidence: medium-high.
- Caveats: future human OSS improvements to Cloudroom do not automatically become runtime S4=P.

### Absence scope

- Surfaces inspected: adapter discovery, installed native skills, setup/update paths, dashboard metrics, telemetry, local/cloud sync and automations.
- Plausible first-party paths checked: new-model catalogs, skill syncing, version updates, scheduled agent requests, workload metrics and teleport modes.
- Why no material first-party path remains: these expose configuration and operational data without a first-party owner generating/screening future adaptation options and feeding a selected change into current capability.

## S5 — Policy and identity

- State: —
- Function: no first-party ultimate-policy/identity issue decision and legitimate return path at the Cloudroom runtime recursion is established.
- Disturbance / variety regulated: authorization, sandbox boundaries, native agent trust and storage safety are fixed deployment policy, not self-governed constitutional issues.
- Decisive decision or feedback right: operator chooses trusted users, app configuration and agent access; no policy-level issue reaches an identified S5 parent, then returns as binding changed organizational identity.
- Decision owner: developer/operator sets service authentication, Linux isolation, credential storage and native-agent trust constraints.
- Supporting / enforcement mechanisms: bearer token, local bind address, separate Linux user, protected file permissions, command guard and no-approval native CLI setting.
- Closure path: API request authenticates or fails and trusted native harness executes within selected sandbox; this is security enforcement, not an ultimate-policy deliberation/decision loop.
- Why this is / is not agent-owned: ACLs, trusted-user rules and instruction files constrain operation; none demonstrates identity-level authority with an explicit escalation and return.
- Evidence: [README security](https://github.com/davidondrej/cloudroom/blob/112f097c8a38c771d233270047f541761a81530a/README.md), [API authentication](https://github.com/davidondrej/cloudroom/blob/112f097c8a38c771d233270047f541761a81530a/core/docs/api.md), [adapter account separation](https://github.com/davidondrej/cloudroom/blob/112f097c8a38c771d233270047f541761a81530a/core/docs/harnesses.md).
- Basis: structural.
- Confidence: medium-high.
- Caveats: public GitHub maintainer governance is a separate organization and cannot be imported as runtime S5=P.

### Absence scope

- Surfaces inspected: service auth, sandbox/security docs, adapter/provider configuration, command guard, user settings, skills and runtime identity.
- Plausible first-party paths checked: authentication/trust, native CLI approvals, configuration updates, role-like child sessions and contributor policies.
- Why no material first-party path remains: local safety authorization never becomes a function-specific ultimate identity-policy matter with legitimate owner and binding return.

## Recursion

Cloudroom sessions are instances of externally sourced autonomous harnesses, not Core-authored viable child organizations. Core may couple them through parent/child notices and cross-sandbox relay, and native agents may form higher-level teams under their own decision rights. The present assessment stops at the first-party Core control-plane boundary: process containment, transport and recording are not assigned the native agents' S1–S5 discretionary ownership.

## Variety and escalation

Core attenuates infrastructure variety through journaled exactly-once request identity, safe retry statuses, startup/recovery queues, session sleep/close and disk warnings/pauses. Absent/failed native runtimes stop rather than implicitly switching decisions. A model-based plan, inter-agent conflict policy or ultimate escalation must be provided by the attached agent/user or a separately governed external control plane; Core's error/refusal paths are observable but do not close those functions.

## Evidence gaps

- Source-first assessment only: no self-hosted/cloud deployment, native authenticated agent run, live teleport, user GUI experiment or process-failure simulation was performed.
- A cloud image can bundle preinstalled third-party CLIs; bundling binaries does not change their first-party decision ownership. Additional private service orchestration is outside this public source boundary.
- The negative states concern this repository's shipped Core/GUI ownership. They do not deny that a separate autonomous agent could *use* Cloudroom tools to build an S1/S2/S3 organization at its own boundary.

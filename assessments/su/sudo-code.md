---
harness_id: sudo-code
project_name: Sudo Code
repository: https://github.com/sudoprivacy/sudocode
review_ref: dad7da543b53db4a4946156c9d60187a088539c2
reviewed_at: 2026-10-06
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-06
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Sudo Code

## Review boundary

- System in focus: the first-party Sudo Code coding runtime at frozen revision dad7da543b53db4a4946156c9d60187a088539c2, including the model/tool coding loop, built-in coding tools, permissions/sandbox/session state, task/subagent execution, experimental coordinator mode, verification worker preset, memory/session surfaces and ACP/headless operation.
- Purpose and identity: a Rust-native coding-agent unit that can operate directly as one coding agent or, in the shipped coordinator mode, act as a model-owned coordinator over multiple fresh worker agents.
- Relevant environment: user goals, repository state and tests, tool/process outcomes, worker status/results, provider/model responses, file-overlap risk among write workers, permissions/sandbox constraints, persisted sessions/memory and ACP/MCP integrations.
- Standard-distribution boundary: the Sudo Code binary and repository-owned runtime/tools/prompts. Sudowork, Hydra, Nexus infrastructure, external model providers, MCP servers and other external agents remain dependencies/adjacent systems and cannot donate hidden organizational functions.
- Credited operating / distribution surfaces: rust/crates/runtime, rust/crates/tools, rusty-sudocode-cli, engine-acp and shipped prompt/config paths, including opt-in coordinator mode and built-in subagent presets.
- Adjacent first-party surfaces excluded from ownership: Sudowork/Hydra fleet UI/orchestration, repository CI/release governance and roadmap-only capabilities not wired into the frozen runtime.
- First-party operating / deployment modes considered: ordinary standalone coding; interactive/headless/ACP; task/subagent execution; opt-in coordinator mode via first-party settings/environment flag; built-in Verification worker mode.
- Recursion level: one Sudo Code coding organization. In coordinator mode the coordinator and spawned coding workers are distinct operational units at this recursion.
- Reviewed revision: dad7da543b53db4a4946156c9d60187a088539c2.
- Observation date: 2026-10-06.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

Sudo Code's base runtime is a first-party model/tool coding loop with repository read/write/edit/bash/search tooling, permissions, sandboxing, sessions, provider adapters and ACP/headless surfaces. The runtime also ships model-callable subagents with fresh contexts and specialized tool pools.

Coordinator mode is a shipped experimental configuration, not an external fleet manager. When enabled, it prepends a coordinator system prompt and hard-gates the coordinator away from write-side tools. The coordinator instead receives agent_spawn, send, pid_status, pid_output, pid_kill and related worker-control tools. It is explicitly instructed to divide complex work across research, implementation and verification workers, synthesize their findings, run independent verification and recover from failed or misdirected workers. Worker completion/failure/killed state returns as structured task-notification messages.

The same coordinator prompt contains a concrete interference policy: read-only research may run freely in parallel, while write-heavy work is serialized per overlapping file set. The coordinator chooses the work partition and concurrency relationship. Runtime process/status/notification mechanisms enforce and expose the resulting worker state.

## Operational model

The ordinary model-backed agent owns open-ended coding actions. In coordinator mode a separate model role owns the current worker portfolio: it decides what to delegate, which workers may run concurrently, when a worker should be killed or redirected, how failures are retried, and when a separate Verification worker should challenge completed implementation.

Deterministic process management, task notifications and permission gates support those choices but do not replace the coordinator's substantive decisions. Memory and session persistence can carry facts between turns, but no separate external-and-prospective adaptation owner was established.

## S1 — Operations

- State: A
- Function: autonomously perform software-engineering work through model-selected repository, shell, test and edit actions.
- Disturbance / variety regulated: unfamiliar code, implementation choices, tool/process failures, test results, provider/model variability, context pressure and bounded delegated coding tasks.
- Decisive decision or feedback right: choose substantive coding/tool actions, interpret returned evidence and decide whether the assigned implementation objective is complete.
- Decision owner: the active model-backed Sudo Code coding agent or spawned coding worker.
- Supporting / enforcement mechanisms: built-in tools, permissions/sandbox, provider adapters, sessions, compaction, ACP/headless transport and runtime cancellation.
- Closure path: user/coordinator goal → coding model chooses actions → runtime executes tools → evidence returns to the same worker → worker revises or completes the task.
- Boundary reachability: ordinary CLI/headless/ACP operation and spawned general-purpose workers instantiate the same first-party coding machinery.
- Why this is / is not agent-owned: removing the model leaves execution/permission machinery but no open-ended engineering choice.
- Evidence: [README.md](https://github.com/sudoprivacy/sudocode/blob/dad7da543b53db4a4946156c9d60187a088539c2/README.md); [rust/crates/runtime/src/conversation.rs](https://github.com/sudoprivacy/sudocode/blob/dad7da543b53db4a4946156c9d60187a088539c2/rust/crates/runtime/src/conversation.rs); [rust/crates/runtime/src/agent_types.rs](https://github.com/sudoprivacy/sudocode/blob/dad7da543b53db4a4946156c9d60187a088539c2/rust/crates/runtime/src/agent_types.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: external provider/model services execute inference but do not own the coding decision rights credited here.

## S2 — Coordination

- State: A
- Function: attenuate interference among concurrent worker S1 units by deciding which work may run in parallel and which write-heavy commitments must be serialized by overlapping file scope.
- Disturbance / variety regulated: concurrent write workers modifying the same file area and thereby producing conflicting or destructive changes.
- Decisive decision or feedback right: choose worker decomposition, file/task scopes and whether write work is parallelized or serialized.
- Decision owner: the model-backed coordinator in coordinator mode.
- Supporting / enforcement mechanisms: agent_spawn task framing, worker status/results, process isolation, one-at-a-time write-heavy policy per file set and runtime task-notification/control tools.
- Closure path: coordinator decomposes current work → identifies independent versus overlapping write scopes → launches compatible workers concurrently and serializes overlapping write work → worker results/failures return → coordinator changes the next worker assignment/integration decision.
- Boundary reachability: coordinator mode is enabled through first-party configuration/environment flags and exposes the first-party worker-control tool set.
- Why this is / is not agent-owned: the runtime executes worker processes, but the coordinator model decides the organizational partition and interaction policy for the current work.
- Distinct S1 units: fresh coding workers spawned through agent_spawn, each owning a bounded operational software-engineering outcome.
- Inter-S1 disturbance: two write-heavy workers operating on the same file set can conflict or overwrite one another's work.
- Attenuating coordination relation: the coordinator prompt explicitly requires write-heavy work to run one at a time per set of files while allowing independent/read-only work to run concurrently.
- Feedback into subsequent S1 behaviour: worker completion/failure/task-notification evidence returns to the coordinator, which determines the next worker scope, retry or serialization decision before subsequent work proceeds.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the positive claim rests on a concrete peer-write interference mode and a model-owned relation that changes concurrency based on overlapping operational scope, not on worker plurality or message transport alone.
- Evidence: [rust/crates/runtime/src/coordinator_mode.rs](https://github.com/sudoprivacy/sudocode/blob/dad7da543b53db4a4946156c9d60187a088539c2/rust/crates/runtime/src/coordinator_mode.rs); [rust/crates/tools/src/lib.rs](https://github.com/sudoprivacy/sudocode/blob/dad7da543b53db4a4946156c9d60187a088539c2/rust/crates/tools/src/lib.rs).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: the standalone branch-lock collision helper is not used as the owner of this claim; S2 rests on the reachable coordinator's scope/concurrency decisions and returned worker outcomes.

## S3 — Inside-and-now control

- State: A
- Function: regulate the current multi-worker portfolio by allocating work, observing worker state/results and changing active commitments.
- Disturbance / variety regulated: worker failure, incorrect direction, changed user requirements, unfinished parallel work, verification need and current workload allocation.
- Decisive decision or feedback right: spawn workers, choose their tasks, inspect all current worker states/results, send follow-up instructions, kill a misdirected worker, retry failed work with a changed scope and decide when to proceed to verification/integration.
- Decision owner: the model-backed coordinator.
- Supporting / enforcement mechanisms: pid_status, pid_output, send, pid_kill, agent_spawn, task notifications and coordinator write-tool gate.
- Closure path: coordinator launches worker set → receives current task notifications/status/output → interprets failures/progress/user changes → sends, kills, retries or launches replacement/verification workers → subsequent current work changes under that decision.
- Boundary reachability: opt-in coordinator mode is first-party and executable via settings/environment configuration.
- Why this is / is not agent-owned: deterministic tools expose/enforce state transitions; the coordinator model owns the substantive current allocation/intervention decision.
- Whole-system current view: pid_status can list the spawned agents while task notifications and pid_output expose terminal/current outcomes to the coordinator alongside the parent goal.
- Current-control decision scope: worker commitments, concurrency, reassignment/retry, selective termination, follow-up direction and transition from implementation to verification.
- Evidence: [rust/crates/runtime/src/coordinator_mode.rs](https://github.com/sudoprivacy/sudocode/blob/dad7da543b53db4a4946156c9d60187a088539c2/rust/crates/runtime/src/coordinator_mode.rs); [rust/crates/tools/src/lib.rs](https://github.com/sudoprivacy/sudocode/blob/dad7da543b53db4a4946156c9d60187a088539c2/rust/crates/tools/src/lib.rs); [rust/crates/runtime/src/conversation.rs](https://github.com/sudoprivacy/sudocode/blob/dad7da543b53db4a4946156c9d60187a088539c2/rust/crates/runtime/src/conversation.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: coordinator mode is opt-in; the positive state describes a supported first-party operating mode, not every default standalone session.

## S3* — Complementary audit

- State: A
- Function: independently verify implementation work using a separate fresh Verification worker with direct repository/test access.
- Disturbance / variety regulated: incorrect implementation claims, missing tests, edge-case failures and author-worker self-report errors.
- Decisive decision or feedback right: run independent tests/checks and return a verification result that the coordinator uses before treating implementation as proven.
- Decision owner: the separate model-backed Verification worker.
- Supporting / enforcement mechanisms: dedicated Verification agent type, fresh child context, bash/read/search tool pool, verification-streak nudge and coordinator verification phase.
- Closure path: implementation worker reports completion → coordinator spawns a Verification worker → verifier independently reads/runs checks over the repository → result returns as task notification/output → coordinator decides whether to accept, repair or retry.
- Boundary reachability: Verification is a shipped built-in agent type and coordinator mode explicitly assigns the Verification phase to workers.
- Why this is / is not agent-owned: a distinct model instance makes the audit judgment from its own repository/test evidence; the same author worker is not merely self-checking.
- Claim being audited: the implementation worker's claim that its code change is correct and satisfies the requested behavior.
- Ordinary reporting path: the implementation worker's own completion text/task notification.
- Complementary access path: the Verification worker has fresh context plus bash/read/glob/grep and related direct evidence tools.
- Independence boundary: fresh spawned worker, separate model turn/context and specialized non-write verification tool pool.
- Who acts on findings: the coordinator receives the verifier result and owns the next accept/repair/retry decision.
- Evidence: [rust/crates/runtime/src/agent_types.rs](https://github.com/sudoprivacy/sudocode/blob/dad7da543b53db4a4946156c9d60187a088539c2/rust/crates/runtime/src/agent_types.rs); [rust/crates/runtime/src/coordinator_mode.rs](https://github.com/sudoprivacy/sudocode/blob/dad7da543b53db4a4946156c9d60187a088539c2/rust/crates/runtime/src/coordinator_mode.rs); [rust/crates/runtime/src/verification_watcher.rs](https://github.com/sudoprivacy/sudocode/blob/dad7da543b53db4a4946156c9d60187a088539c2/rust/crates/runtime/src/verification_watcher.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: deterministic verification nudges are supporting triggers only; S3* ownership is credited to the separate Verification model worker.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party external-and-prospective adaptation loop is established.
- Disturbance / variety regulated: no outside/future condition is shown producing organizational adaptation options that return into current capability under a dedicated owner.
- Decisive decision or feedback right: none established for S4.
- Decision owner: none established.
- Supporting / enforcement mechanisms: persisted memory, sessions, model/provider configuration, web tools, skills and roadmap/design material can influence later work but do not themselves close S4.
- Closure path: not applicable.
- Boundary reachability: no positive S4 path claimed.
- Why this is / is not agent-owned: current memory/provider code stores or retrieves context/configuration, and the MemoryProvider prefetch interface at the frozen ref is not itself a complete autonomous prospective adaptation conversation.
- Evidence: [rust/crates/runtime/src/memory/mod.rs](https://github.com/sudoprivacy/sudocode/blob/dad7da543b53db4a4946156c9d60187a088539c2/rust/crates/runtime/src/memory/mod.rs); [rust/crates/runtime/src/memory/provider.rs](https://github.com/sudoprivacy/sudocode/blob/dad7da543b53db4a4946156c9d60187a088539c2/rust/crates/runtime/src/memory/provider.rs); [README.md](https://github.com/sudoprivacy/sudocode/blob/dad7da543b53db4a4946156c9d60187a088539c2/README.md).
- Basis: structural absence review.
- Confidence: high.
- Caveats: future roadmap architecture is not imported into the frozen runtime assessment.

### Absence scope

- Surfaces inspected: memory provider/storage, sessions, provider/model configuration, web/skill surfaces, coordinator recovery, roadmap/design material and runtime experiments.
- Plausible first-party paths checked: autonomous environment scanning, durable learned-strategy updates, self-reconfiguration and future-oriented option generation returned to S3.
- Why no material first-party path remains: observed mechanisms are current-task evidence, persistence/configuration or roadmap intent rather than a closed outside-and-then adaptation loop.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy governance loop is established.
- Disturbance / variety regulated: no identity-level policy conflict is routed to an authoritative runtime owner and returned as governing policy.
- Decisive decision or feedback right: none established for S5.
- Decision owner: none established.
- Supporting / enforcement mechanisms: permissions, sandbox, coordinator tool gate, configuration, system prompts and trust policy constrain execution but do not create identity governance.
- Closure path: not applicable.
- Boundary reachability: no positive S5 path claimed.
- Why this is / is not agent-owned: coding/coordinator agents operate inside developer/user-authored rules and cannot authoritatively redefine Sudo Code's identity or ultimate policy.
- Evidence: [README.md](https://github.com/sudoprivacy/sudocode/blob/dad7da543b53db4a4946156c9d60187a088539c2/README.md); [rust/crates/runtime/src/permissions.rs](https://github.com/sudoprivacy/sudocode/blob/dad7da543b53db4a4946156c9d60187a088539c2/rust/crates/runtime/src/permissions.rs); [rust/crates/runtime/src/coordinator_mode.rs](https://github.com/sudoprivacy/sudocode/blob/dad7da543b53db4a4946156c9d60187a088539c2/rust/crates/runtime/src/coordinator_mode.rs).
- Basis: structural absence review.
- Confidence: high.
- Caveats: README design principles and operator configuration are externally authored constraints, not a runtime S5 loop.

### Absence scope

- Surfaces inspected: system/coordinator prompts, permissions, sandbox/trust policy, configuration, design principles, experiments and operator controls.
- Plausible first-party paths checked: autonomous constitutional revision, parent identity governance, runtime policy-authoring actor and authoritative return-to-operation path.
- Why no material first-party path remains: identified mechanisms enforce or describe operating policy but do not close identity/ultimate-policy governance.

## Distributed OSS parent arrangement

The assessed organization is the running Sudo Code session, including its optional coordinator-mode worker organization, not the wider Sudo Privacy project or Sudowork/Hydra fleet. Repository maintainer governance is not imported as runtime parent ownership.

## Self-hosted and non-human modes

Sudo Code supports local/headless/ACP operation and multiple providers. The positive S2/S3/S3* claims are first-party model/runtime modes and do not depend on a human dashboard or proprietary provider.

## Recursion

In ordinary mode the session contains one coding S1 plus optional task subagents. In coordinator mode the coordinator plus spawned coding workers form the viable unit: workers are S1, the coordinator owns S2 and S3 over them, and a separate Verification worker supplies S3*.

## Variety and escalation

Ordinary coding variety remains in S1. Cross-worker overlap is attenuated by coordinator-chosen concurrency/scope under S2. Current worker failures, direction and allocation escalate to the coordinator under S3. Implementation claims can escalate to a fresh Verification worker under S3*. Persistence and static policy remain supporting mechanisms rather than S4/S5.

## Evidence gaps

No ? state is required. Frozen first-party source establishes the coordinator tool gate, worker lifecycle, task-notification return path and Verification preset, while the reviewed memory/policy surfaces are broad enough for the bounded negative S4/S5 conclusions.

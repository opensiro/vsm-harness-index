---
harness_id: inkpi
project_name: InkPi
repository: https://github.com/MeiSiristhebest/inkpi
review_ref: 4d231366a1c7b08d1d5ade7fd7c105d4a49557c4
reviewed_at: 2026-11-02
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# InkPi

## Review boundary

- System in focus: InkPi first-party core and supported CLI/daemon model-task composition, with published storage/workflow primitives examined for optional paths.
- Purpose and identity: Modular model/tool task execution with durable sessions, context and host extension points.
- Relevant environment: users, workspaces, model services, tools and the operational disturbances described below.
- Standard-distribution boundary: The current packages/agent-core and packages/server executable composition, model adapters, protocol, session backends and storage APIs.
- Credited operating / distribution surfaces: Agent/AgentLoopRunner, TaskRouter and TaskModelHandler, explicit daemon wiring and shipped tools/context/session mechanisms.
- Adjacent first-party surfaces excluded from ownership: Architecture-remediation/contributor SOPs, tests/benchmarks, CI/release ratchets, unconfigured host callbacks and external provider-owned agents.
- First-party operating / deployment modes considered: CLI/daemon tasks and embedded Agent with explicit model/tools; optional generic workflows, storage and host adapters inspected without assuming an unwired agent organization.
- Recursion level: one deployed harness/composition and its work sessions; repository maintainers and external hosts are outside this operational recursion.
- Reviewed revision: `4d231366a1c7b08d1d5ade7fd7c105d4a49557c4`.
- Observation date: 2026-11-02.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7 (active Index pair; current Skills main calibration also consulted).

## Repository architecture

InkPi separates domain core, AI adapters, daemon transports, session backends, storage and terminal/client surfaces. Agent drives context preparation, model streaming, tool dispatch and continuation. The daemon registers runtime.model/runtime.batch handlers and persists task admission/execution/checkpoint state. Skills, discovery, context providers, proposals and generic workflow gates are extensibility surfaces. Writer leases/fencing live in a separate storage primitive; their collision purpose does not prove an autonomous operational coordination mode. Maintainer architecture and verification work remains adjacent.

## Operational model

The S1 is the first-party model/tool task actor. Multiple tasks, role registries and generic workflows expose composition choices; task/resource lifecycle and deterministic collision enforcement are kept separate from organizational decision ownership. Positive and parent modes were tested before the bounded negatives below. No generic API receives C merely because it could support a future metasystem.

## S1 — Operations

- State: A
- Function: Execute user/model tasks with iterative tool action and observation.
- Disturbance / variety regulated: Task uncertainty, failed tools, context overflow, interruptions and provider errors.
- Decisive decision or feedback right: Choose subsequent tools/actions and completion using model output and returned results.
- Decision owner: The configured model actor driven by first-party Agent/TaskModelHandler loops.
- Supporting / enforcement mechanisms: AgentLoopRunner context/stream/dispatch/finalization stages, journals, model adapters, tool registry and daemon RPC.
- Closure path: Prepared context → model response → tool dispatch/result → finalized continuation; steering and follow-ups are consumed at turn boundaries.
- Why this is / is not agent-owned: The first-party loop supplies goal-directed iteration without importing an external coding-agent runtime; model APIs supply inference rather than a separate harness.
- Evidence: [packages/agent-core/src/agent.ts](https://github.com/MeiSiristhebest/inkpi/blob/4d231366a1c7b08d1d5ade7fd7c105d4a49557c4/packages/agent-core/src/agent.ts); [packages/agent-core/src/turn/agent-loop-runner.ts](https://github.com/MeiSiristhebest/inkpi/blob/4d231366a1c7b08d1d5ade7fd7c105d4a49557c4/packages/agent-core/src/turn/agent-loop-runner.ts); [packages/agent-core/src/turn/tool-dispatcher.ts](https://github.com/MeiSiristhebest/inkpi/blob/4d231366a1c7b08d1d5ade7fd7c105d4a49557c4/packages/agent-core/src/turn/tool-dispatcher.ts); [packages/server/src/task-model-handler.ts](https://github.com/MeiSiristhebest/inkpi/blob/4d231366a1c7b08d1d5ade7fd7c105d4a49557c4/packages/server/src/task-model-handler.ts); [packages/server/src/daemon.ts](https://github.com/MeiSiristhebest/inkpi/blob/4d231366a1c7b08d1d5ade7fd7c105d4a49557c4/packages/server/src/daemon.ts).
- Basis: structural.
- Confidence: high.
- Caveats: Source-level assessment; no live model/provider execution is claimed.
- Boundary reachability: InkPiDaemon registers the first-party model task handler, while Agent is a public executable core class with explicit model/tools; CLI/daemon and embedding modes reach these paths.

## S2 — Coordination

- State: —
- Function: No material first-party S2 loop is shipped in the assessed daemon/core composition.
- Disturbance / variety regulated: The function-specific candidate disturbances in the inspected paths below.
- Decisive decision or feedback right: No shipped function-specific organizational decisive right established.
- Decision owner: No autonomous or eligible parent owner established for this function.
- Supporting / enforcement mechanisms: Task scheduling/deduplication, child spawning, generic role stages, document writer leases and fencing. The storage mutation queue explicitly targets multi-agent write collisions, and returns lock/lost-lease failures to its caller.
- Closure path: The inspected mechanisms do not close this organizational function in the supported composition.
- Why this is / is not agent-owned: The collision-specific storage primitive is not wired to distinct operational S1 agents in the inspected supported daemon/core composition (production references remain inside storage; callers must supply holder/mutation code). Generic task sequencing/capacity enforcement does not supply the missing inter-S1 adjustment relation. A library lock alone is not credited as S2=C.
- Evidence: [packages/agent-core/src/tasks/task-router.ts](https://github.com/MeiSiristhebest/inkpi/blob/4d231366a1c7b08d1d5ade7fd7c105d4a49557c4/packages/agent-core/src/tasks/task-router.ts); [packages/agent-core/src/lifecycle/scheduler.ts](https://github.com/MeiSiristhebest/inkpi/blob/4d231366a1c7b08d1d5ade7fd7c105d4a49557c4/packages/agent-core/src/lifecycle/scheduler.ts); [packages/agent-core/src/pipeline/roles.ts](https://github.com/MeiSiristhebest/inkpi/blob/4d231366a1c7b08d1d5ade7fd7c105d4a49557c4/packages/agent-core/src/pipeline/roles.ts); [packages/storage/src/mutation-queue.ts](https://github.com/MeiSiristhebest/inkpi/blob/4d231366a1c7b08d1d5ade7fd7c105d4a49557c4/packages/storage/src/mutation-queue.ts); [packages/storage/src/leases.ts](https://github.com/MeiSiristhebest/inkpi/blob/4d231366a1c7b08d1d5ade7fd7c105d4a49557c4/packages/storage/src/leases.ts); [packages/server/src/daemon.ts](https://github.com/MeiSiristhebest/inkpi/blob/4d231366a1c7b08d1d5ade7fd7c105d4a49557c4/packages/server/src/daemon.ts).
- Basis: structural.
- Confidence: high.
- Caveats: Source-level assessment; no live model/provider execution is claimed.

### Absence scope

- Surfaces inspected: packages/agent-core/src/tasks/task-router.ts, packages/agent-core/src/lifecycle/scheduler.ts, packages/agent-core/src/pipeline/roles.ts, packages/storage/src/mutation-queue.ts, packages/storage/src/leases.ts, packages/server/src/daemon.ts and the declared runtime/distribution wiring.
- Plausible first-party paths checked: Task scheduling/deduplication, child spawning, generic role stages, document writer leases and fencing. The storage mutation queue explicitly targets multi-agent write collisions, and returns lock/lost-lease failures to its caller.
- Why no material first-party path remains: The collision-specific storage primitive is not wired to distinct operational S1 agents in the inspected supported daemon/core composition (production references remain inside storage; callers must supply holder/mutation code). Generic task sequencing/capacity enforcement does not supply the missing inter-S1 adjustment relation. A library lock alone is not credited as S2=C.

## S3 — Inside-and-now control

- State: —
- Function: No material whole-system current-control decision loop is supplied.
- Disturbance / variety regulated: The function-specific candidate disturbances in the inspected paths below.
- Decisive decision or feedback right: No shipped function-specific organizational decisive right established.
- Decision owner: No autonomous or eligible parent owner established for this function.
- Supporting / enforcement mechanisms: Task submit/status/execution/cancel/steer/resume/fork RPCs, priority/concurrency options, retry/checkpoint persistence and model-route health.
- Closure path: The inspected mechanisms do not close this organizational function in the supported composition.
- Why this is / is not agent-owned: These close per-task lifecycle and deterministic scheduling. No supported agent or parent regulator receives a whole-operation resource/commitment case and owns a returned system-wide allocation/intervention choice. Caller-selected executionPolicy and optional host callbacks do not themselves establish S3 or a function-specific autonomous S3 constructor.
- Evidence: [packages/agent-core/src/tasks/task-router.ts](https://github.com/MeiSiristhebest/inkpi/blob/4d231366a1c7b08d1d5ade7fd7c105d4a49557c4/packages/agent-core/src/tasks/task-router.ts); [packages/agent-core/src/lifecycle/scheduler.ts](https://github.com/MeiSiristhebest/inkpi/blob/4d231366a1c7b08d1d5ade7fd7c105d4a49557c4/packages/agent-core/src/lifecycle/scheduler.ts); [packages/server/src/daemon.ts](https://github.com/MeiSiristhebest/inkpi/blob/4d231366a1c7b08d1d5ade7fd7c105d4a49557c4/packages/server/src/daemon.ts); [packages/server/src/task-model-handler.ts](https://github.com/MeiSiristhebest/inkpi/blob/4d231366a1c7b08d1d5ade7fd7c105d4a49557c4/packages/server/src/task-model-handler.ts); [packages/agent-core/src/pipeline/workflow-executor.ts](https://github.com/MeiSiristhebest/inkpi/blob/4d231366a1c7b08d1d5ade7fd7c105d4a49557c4/packages/agent-core/src/pipeline/workflow-executor.ts).
- Basis: structural.
- Confidence: high.
- Caveats: Source-level assessment; no live model/provider execution is claimed.

### Absence scope

- Surfaces inspected: packages/agent-core/src/tasks/task-router.ts, packages/agent-core/src/lifecycle/scheduler.ts, packages/server/src/daemon.ts, packages/server/src/task-model-handler.ts, packages/agent-core/src/pipeline/workflow-executor.ts and the declared runtime/distribution wiring.
- Plausible first-party paths checked: Task submit/status/execution/cancel/steer/resume/fork RPCs, priority/concurrency options, retry/checkpoint persistence and model-route health.
- Why no material first-party path remains: These close per-task lifecycle and deterministic scheduling. No supported agent or parent regulator receives a whole-operation resource/commitment case and owns a returned system-wide allocation/intervention choice. Caller-selected executionPolicy and optional host callbacks do not themselves establish S3 or a function-specific autonomous S3 constructor.

## S3* — Complementary audit

- State: —
- Function: No complementary independent operational-audit function is supplied.
- Disturbance / variety regulated: The function-specific candidate disturbances in the inspected paths below.
- Decisive decision or feedback right: No shipped function-specific organizational decisive right established.
- Decision owner: No autonomous or eligible parent owner established for this function.
- Supporting / enforcement mechanisms: Generic workflow quality rules/qualityGateHandler, role invocation, trace/observation exports and execution snapshots.
- Closure path: The inspected mechanisms do not close this organizational function in the supported composition.
- Why this is / is not agent-owned: Quality gating is an ordinary configured production stage; the generic strategy stores outputs and calls user-composed handlers without a distinct complementary access/independent audit owner and corrective return. Repository tests and architecture ratchets audit software development, which is outside the operational boundary.
- Evidence: [packages/agent-core/src/pipeline/workflow-executor.ts](https://github.com/MeiSiristhebest/inkpi/blob/4d231366a1c7b08d1d5ade7fd7c105d4a49557c4/packages/agent-core/src/pipeline/workflow-executor.ts); [packages/agent-core/src/pipeline/workflow-strategy.ts](https://github.com/MeiSiristhebest/inkpi/blob/4d231366a1c7b08d1d5ade7fd7c105d4a49557c4/packages/agent-core/src/pipeline/workflow-strategy.ts); [packages/agent-core/src/pipeline/role-invoker.ts](https://github.com/MeiSiristhebest/inkpi/blob/4d231366a1c7b08d1d5ade7fd7c105d4a49557c4/packages/agent-core/src/pipeline/role-invoker.ts); [packages/agent-core/src/telemetry/task-observability.ts](https://github.com/MeiSiristhebest/inkpi/blob/4d231366a1c7b08d1d5ade7fd7c105d4a49557c4/packages/agent-core/src/telemetry/task-observability.ts); [packages/server/src/observation-sink.ts](https://github.com/MeiSiristhebest/inkpi/blob/4d231366a1c7b08d1d5ade7fd7c105d4a49557c4/packages/server/src/observation-sink.ts).
- Basis: structural.
- Confidence: high.
- Caveats: Source-level assessment; no live model/provider execution is claimed.

### Absence scope

- Surfaces inspected: packages/agent-core/src/pipeline/workflow-executor.ts, packages/agent-core/src/pipeline/workflow-strategy.ts, packages/agent-core/src/pipeline/role-invoker.ts, packages/agent-core/src/telemetry/task-observability.ts, packages/server/src/observation-sink.ts and the declared runtime/distribution wiring.
- Plausible first-party paths checked: Generic workflow quality rules/qualityGateHandler, role invocation, trace/observation exports and execution snapshots.
- Why no material first-party path remains: Quality gating is an ordinary configured production stage; the generic strategy stores outputs and calls user-composed handlers without a distinct complementary access/independent audit owner and corrective return. Repository tests and architecture ratchets audit software development, which is outside the operational boundary.

## S4 — Outside-and-then intelligence

- State: —
- Function: No external-and-prospective adaptation loop is supplied.
- Disturbance / variety regulated: The function-specific candidate disturbances in the inspected paths below.
- Decisive decision or feedback right: No shipped function-specific organizational decisive right established.
- Decision owner: No autonomous or eligible parent owner established for this function.
- Supporting / enforcement mechanisms: What-if branches, JIT retrieval, compaction, skill loading, model capability routing and domain-neutral proposal/rebase/commit APIs.
- Closure path: The inspected mechanisms do not close this organizational function in the supported composition.
- Why this is / is not agent-owned: These support current task context, route selection and hypothetical domain artifacts. No supplied supported actor develops future environmental adaptation options and closes their selection into present harness capability. A domain-neutral proposal API is not an S4-specific constructor, and development roadmaps are adjacent.
- Evidence: [packages/agent-core/src/branch-what-if.ts](https://github.com/MeiSiristhebest/inkpi/blob/4d231366a1c7b08d1d5ade7fd7c105d4a49557c4/packages/agent-core/src/branch-what-if.ts); [packages/agent-core/src/compaction/compaction.ts](https://github.com/MeiSiristhebest/inkpi/blob/4d231366a1c7b08d1d5ade7fd7c105d4a49557c4/packages/agent-core/src/compaction/compaction.ts); [packages/server/src/jit-context-provider.ts](https://github.com/MeiSiristhebest/inkpi/blob/4d231366a1c7b08d1d5ade7fd7c105d4a49557c4/packages/server/src/jit-context-provider.ts); [packages/server/src/model-capability-router.ts](https://github.com/MeiSiristhebest/inkpi/blob/4d231366a1c7b08d1d5ade7fd7c105d4a49557c4/packages/server/src/model-capability-router.ts); [packages/agent-core/src/skills/skills.ts](https://github.com/MeiSiristhebest/inkpi/blob/4d231366a1c7b08d1d5ade7fd7c105d4a49557c4/packages/agent-core/src/skills/skills.ts); [packages/agent-core/src/proposals/domain-proposal-ledger.ts](https://github.com/MeiSiristhebest/inkpi/blob/4d231366a1c7b08d1d5ade7fd7c105d4a49557c4/packages/agent-core/src/proposals/domain-proposal-ledger.ts).
- Basis: structural.
- Confidence: high.
- Caveats: Source-level assessment; no live model/provider execution is claimed.

### Absence scope

- Surfaces inspected: packages/agent-core/src/branch-what-if.ts, packages/agent-core/src/compaction/compaction.ts, packages/server/src/jit-context-provider.ts, packages/server/src/model-capability-router.ts, packages/agent-core/src/skills/skills.ts, packages/agent-core/src/proposals/domain-proposal-ledger.ts and the declared runtime/distribution wiring.
- Plausible first-party paths checked: What-if branches, JIT retrieval, compaction, skill loading, model capability routing and domain-neutral proposal/rebase/commit APIs.
- Why no material first-party path remains: These support current task context, route selection and hypothetical domain artifacts. No supplied supported actor develops future environmental adaptation options and closes their selection into present harness capability. A domain-neutral proposal API is not an S4-specific constructor, and development roadmaps are adjacent.

## S5 — Policy and identity

- State: —
- Function: No identity/ultimate-policy closure is supplied.
- Disturbance / variety regulated: The function-specific candidate disturbances in the inspected paths below.
- Decisive decision or feedback right: No shipped function-specific organizational decisive right established.
- Decision owner: No autonomous or eligible parent owner established for this function.
- Supporting / enforcement mechanisms: Proposal acceptance/rejection, project instructions, credential grants, sandbox boundaries and dynamically registered workflow roles.
- Closure path: The inspected mechanisms do not close this organizational function in the supported composition.
- Why this is / is not agent-owned: Proposal state and tool authority are generic operational/configuration mechanisms. They do not identify an ultimate-policy dispute or legitimate identity-level arbitration/return path at the harness recursion. User callbacks cannot supply that missing function by name alone.
- Evidence: [packages/agent-core/src/proposals/domain-proposal-ledger.ts](https://github.com/MeiSiristhebest/inkpi/blob/4d231366a1c7b08d1d5ade7fd7c105d4a49557c4/packages/agent-core/src/proposals/domain-proposal-ledger.ts); [packages/agent-core/src/sandbox/sandbox.ts](https://github.com/MeiSiristhebest/inkpi/blob/4d231366a1c7b08d1d5ade7fd7c105d4a49557c4/packages/agent-core/src/sandbox/sandbox.ts); [packages/agent-core/src/instructions/instruction-registry.ts](https://github.com/MeiSiristhebest/inkpi/blob/4d231366a1c7b08d1d5ade7fd7c105d4a49557c4/packages/agent-core/src/instructions/instruction-registry.ts); [packages/server/src/project-instructions.ts](https://github.com/MeiSiristhebest/inkpi/blob/4d231366a1c7b08d1d5ade7fd7c105d4a49557c4/packages/server/src/project-instructions.ts); [packages/server/src/runtime-credential-broker.ts](https://github.com/MeiSiristhebest/inkpi/blob/4d231366a1c7b08d1d5ade7fd7c105d4a49557c4/packages/server/src/runtime-credential-broker.ts).
- Basis: structural.
- Confidence: high.
- Caveats: Source-level assessment; no live model/provider execution is claimed.

### Absence scope

- Surfaces inspected: packages/agent-core/src/proposals/domain-proposal-ledger.ts, packages/agent-core/src/sandbox/sandbox.ts, packages/agent-core/src/instructions/instruction-registry.ts, packages/server/src/project-instructions.ts, packages/server/src/runtime-credential-broker.ts and the declared runtime/distribution wiring.
- Plausible first-party paths checked: Proposal acceptance/rejection, project instructions, credential grants, sandbox boundaries and dynamically registered workflow roles.
- Why no material first-party path remains: Proposal state and tool authority are generic operational/configuration mechanisms. They do not identify an ultimate-policy dispute or legitimate identity-level arbitration/return path at the harness recursion. User callbacks cannot supply that missing function by name alone.

## Distributed OSS parent arrangement

Public maintainers own development and release governance. Their repository process is adjacent to the installed harness; contributor plurality does not establish operational parent S3/S4/S5 at this recursion. No additional closed parent-governed function is established by ordinary configuration or approvals.

## Self-hosted and non-human modes

CLI/daemon tasks and embedded Agent with explicit model/tools; optional generic workflows, storage and host adapters inspected without assuming an unwired agent organization. Model choice, permission settings and deployment administration alone do not establish ultimate-policy governance. Unimplemented extensions do not receive constructor credit.

## Recursion

Subagents are task decomposition; no recursively viable suborganization is established.

## Variety and escalation

Tool/model failures, permission limits and context exhaustion return as observations, refusals, pauses or terminal results. These channels support local recovery; they are not additional VSM functions or automatic algedonic evidence.

## Evidence gaps

No live provider or product E2E run was performed. Conclusions concern reachable source-level ownership at the exact frozen revision, not performance, deployment reliability or benchmark quality. Bounded absence claims cover the stated supported distribution, not arbitrary future extensions.

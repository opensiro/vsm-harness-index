---
harness_id: kuafu
project_name: Kuafu
repository: https://github.com/DoSomeForFun/kuafu
review_ref: 0628a879bb2ca24be9142ef32c49ab7aab8520bf
reviewed_at: 2026-10-27
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Kuafu

## Review boundary

- System in focus: The first-party Kuafu TypeScript source-build Kernel, Store and Action distribution built by tsup, with a real configured LLMProvider.chat and optional action/perception/hooks. The unbuilt stub default and incomplete checked-in dist are explicitly not claimed functional model-backed modes.
- Purpose and identity: Embed a channel-neutral autonomous task/tool loop with persisted context.
- Relevant environment: Host task store/files/shell, injected model provider, tool failures and caller-supplied runtime events/context.
- Standard-distribution boundary: The first-party Kuafu TypeScript source-build Kernel, Store and Action distribution built by tsup, with a real configured LLMProvider.chat and optional action/perception/hooks. The unbuilt stub default and incomplete checked-in dist are explicitly not claimed functional model-backed modes.
- Credited operating / distribution surfaces: src Kernel constructor/run and FSM handlers, Action tools, Perception/skills, Store and typed runtime hooks, all reachable through standard tsup build entrypoints. Injecting a provider is normal runtime configuration, not a bespoke organizational supervisor.
- Adjacent first-party surfaces excluded from ownership: README BridgeMemoryProvider/Memox/CompositeMemoryProvider and replay examples are not borrowed as shipped actors when absent from the inspected source/export surface. Tests and examples corroborate intent but are not model runs. Checked-in dist references absent chunk files and is not a verified executable build.
- First-party operating / deployment modes considered: Supported local self-hosted runtime and operator-supervised configuration; no custom external composition is credited.
- Recursion level: One runtime/project deployment; nested task agents are not presumed recursively viable.
- Reviewed revision: 0628a879bb2ca24be9142ef32c49ab7aab8520bf
- Observation date: 2026-10-27
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

The source Kernel creates a task-scoped context and runs PERCEIVING/THINKING/DECIDING/ACTING/REFLECTING until DONE/FAILED or turn bound. THINKING calls the injected LLMProvider.chat with history and tool schemas; returned tool calls invoke Action and results are persisted and fed to the next model turn. Store provides SQLite task branches, messages, lessons and vector retrieval. Perception routes file-based skills and recalls lessons/context. Before/after hooks can capture, silence or rewrite a task's input/output; telemetry/progress sinks report events. The constructor reads llmProvider and otherwise installs StubLLMProvider, so the README's llm function example does not match this source. Standard tsup configuration builds the exported Kernel/Action/Store entrypoints; the repository's checked-in dist alone is incomplete.

## Operational model

One configured Kernel run is the operational agent unit. The model chooses contextual tools and final answer; deterministic FSM/turn limits enforce its loop. Concurrent tool calls within one turn are actions of that unit, not separate autonomous S1 units. No shipped team regulator, independent audit owner or prospective capability/ultimate-policy organization is supplied.

## S1 — Operations

- State: A
- Function: Autonomous task response and tool operation
- Disturbance / variety regulated: Uncertain task context and tool outcomes
- Decisive decision or feedback right: Choose tool calls or final answer through configured LLMProvider.chat
- Decision owner: Injected model-backed agent in the source-build Kernel mode
- Supporting / enforcement mechanisms: KernelFSM, Action.invokeTool, Store history, perception and maxTurns
- Closure path: ACTING results pass through REFLECTING into Store, then THINKING reads history and continues until model completion or deterministic bound
- Why this is / is not agent-owned: Injected model-backed agent in the source-build Kernel mode; Default is a stub; A applies only to the explicit real-provider source-build mode. No successful native build or model task is claimed.
- Evidence: [src/kernel/index.ts](https://github.com/DoSomeForFun/kuafu/blob/0628a879bb2ca24be9142ef32c49ab7aab8520bf/src/kernel/index.ts); [src/kernel/handlers.ts](https://github.com/DoSomeForFun/kuafu/blob/0628a879bb2ca24be9142ef32c49ab7aab8520bf/src/kernel/handlers.ts); [src/kernel/fsm.ts](https://github.com/DoSomeForFun/kuafu/blob/0628a879bb2ca24be9142ef32c49ab7aab8520bf/src/kernel/fsm.ts); [src/kernel/types.ts](https://github.com/DoSomeForFun/kuafu/blob/0628a879bb2ca24be9142ef32c49ab7aab8520bf/src/kernel/types.ts) LLMProvider; [tsup.config.ts](https://github.com/DoSomeForFun/kuafu/blob/0628a879bb2ca24be9142ef32c49ab7aab8520bf/tsup.config.ts)
- Basis: structural
- Confidence: high
- Caveats: Default is a stub; A applies only to the explicit real-provider source-build mode. No successful native build or model task is claimed.
- Boundary reachability: src Kernel constructor/run and FSM handlers, Action tools, Perception/skills, Store and typed runtime hooks, all reachable through standard tsup build entrypoints. Injecting a provider is normal runtime configuration, not a bespoke organizational supervisor. The cited decision path is shipped in this mode and returns through KernelFSM, Action.invokeTool, Store history, perception and maxTurns.

## S2 — Coordination

- State: —
- Function: No first-party inter-S1 coordination path
- Disturbance / variety regulated: Potential interference between distinct autonomous operational units
- Decisive decision or feedback right: No shipped conflict-sensitive coordination decision/feedback path established
- Decision owner: None established
- Supporting / enforcement mechanisms: Task/session IDs, SQLite message branches, runtime scopes and parallel action calls
- Closure path: The kernel regulates one run; parallel tool Promise.all is action execution, and shared storage/scopes do not assign or reconcile competing agents
- Why this is / is not agent-owned: None established; A caller could create multiple Kernels, but no S2-specific first-party actor or conflict protocol is supplied.
- Evidence: [src/kernel/handlers.ts](https://github.com/DoSomeForFun/kuafu/blob/0628a879bb2ca24be9142ef32c49ab7aab8520bf/src/kernel/handlers.ts) ACTING; [src/kernel/index.ts](https://github.com/DoSomeForFun/kuafu/blob/0628a879bb2ca24be9142ef32c49ab7aab8520bf/src/kernel/index.ts); [src/store.ts](https://github.com/DoSomeForFun/kuafu/blob/0628a879bb2ca24be9142ef32c49ab7aab8520bf/src/store.ts); [src/runtime.ts](https://github.com/DoSomeForFun/kuafu/blob/0628a879bb2ca24be9142ef32c49ab7aab8520bf/src/runtime.ts)
- Basis: structural
- Confidence: medium
- Caveats: A caller could create multiple Kernels, but no S2-specific first-party actor or conflict protocol is supplied.

### Absence scope

- Surfaces inspected: [src/kernel/handlers.ts](https://github.com/DoSomeForFun/kuafu/blob/0628a879bb2ca24be9142ef32c49ab7aab8520bf/src/kernel/handlers.ts) ACTING; [src/kernel/index.ts](https://github.com/DoSomeForFun/kuafu/blob/0628a879bb2ca24be9142ef32c49ab7aab8520bf/src/kernel/index.ts); [src/store.ts](https://github.com/DoSomeForFun/kuafu/blob/0628a879bb2ca24be9142ef32c49ab7aab8520bf/src/store.ts); [src/runtime.ts](https://github.com/DoSomeForFun/kuafu/blob/0628a879bb2ca24be9142ef32c49ab7aab8520bf/src/runtime.ts); runtime entry, roles/tools, supported configuration and operating documentation within the declared boundary.
- Plausible first-party paths checked: Task/session IDs, SQLite message branches, runtime scopes and parallel action calls; autonomous and operator-governed alternatives were checked for no first-party inter-s1 coordination path.
- Why no material first-party path remains: The kernel regulates one run; parallel tool Promise.all is action execution, and shared storage/scopes do not assign or reconcile competing agents A caller could create multiple Kernels, but no S2-specific first-party actor or conflict protocol is supplied. This is a bounded shipped-distribution conclusion, not impossibility of an extension.

## S3 — Inside-and-now control

- State: —
- Function: No whole-system current-control function
- Disturbance / variety regulated: Shared resources/commitments across operational units
- Decisive decision or feedback right: No whole-system current view plus discretionary regulation scope established
- Decision owner: None established
- Supporting / enforcement mechanisms: maxTurns, progress/outcome hooks, Decision stop checks, task status persistence
- Closure path: Deterministic bounds terminate a run and hooks intercept it; no supplied agent or parent reallocates whole-system commitments/resources from a global current view
- Why this is / is not agent-owned: None established; Stopping a loop or configuring hooks alone is enforcement/extensibility, not S3 ownership or an S3 constructor.
- Evidence: [src/kernel/fsm.ts](https://github.com/DoSomeForFun/kuafu/blob/0628a879bb2ca24be9142ef32c49ab7aab8520bf/src/kernel/fsm.ts); [src/kernel/index.ts](https://github.com/DoSomeForFun/kuafu/blob/0628a879bb2ca24be9142ef32c49ab7aab8520bf/src/kernel/index.ts); [src/decision.ts](https://github.com/DoSomeForFun/kuafu/blob/0628a879bb2ca24be9142ef32c49ab7aab8520bf/src/decision.ts); [src/runtime.ts](https://github.com/DoSomeForFun/kuafu/blob/0628a879bb2ca24be9142ef32c49ab7aab8520bf/src/runtime.ts)
- Basis: structural
- Confidence: medium
- Caveats: Stopping a loop or configuring hooks alone is enforcement/extensibility, not S3 ownership or an S3 constructor.

### Absence scope

- Surfaces inspected: [src/kernel/fsm.ts](https://github.com/DoSomeForFun/kuafu/blob/0628a879bb2ca24be9142ef32c49ab7aab8520bf/src/kernel/fsm.ts); [src/kernel/index.ts](https://github.com/DoSomeForFun/kuafu/blob/0628a879bb2ca24be9142ef32c49ab7aab8520bf/src/kernel/index.ts); [src/decision.ts](https://github.com/DoSomeForFun/kuafu/blob/0628a879bb2ca24be9142ef32c49ab7aab8520bf/src/decision.ts); [src/runtime.ts](https://github.com/DoSomeForFun/kuafu/blob/0628a879bb2ca24be9142ef32c49ab7aab8520bf/src/runtime.ts); runtime entry, roles/tools, supported configuration and operating documentation within the declared boundary.
- Plausible first-party paths checked: maxTurns, progress/outcome hooks, Decision stop checks, task status persistence; autonomous and operator-governed alternatives were checked for no whole-system current-control function.
- Why no material first-party path remains: Deterministic bounds terminate a run and hooks intercept it; no supplied agent or parent reallocates whole-system commitments/resources from a global current view Stopping a loop or configuring hooks alone is enforcement/extensibility, not S3 ownership or an S3 constructor. This is a bounded shipped-distribution conclusion, not impossibility of an extension.

## S3* — Complementary audit

- State: —
- Function: No independent complementary audit loop
- Disturbance / variety regulated: Reliability of model response and tool-result claims
- Decisive decision or feedback right: No independent audit judgment/access/returned corrective control supplied
- Decision owner: None established
- Supporting / enforcement mechanisms: Telemetry, stored tool results, Decision.semanticCheck and README trace/replay examples
- Closure path: semanticCheck only checks non-empty response in source; logs and replay recipes have no separately owned audit judgment/return loop
- Why this is / is not agent-owned: None established; Verifiable Tape terminology and ordinary test cases do not establish independent operational S3*.
- Evidence: [src/decision.ts](https://github.com/DoSomeForFun/kuafu/blob/0628a879bb2ca24be9142ef32c49ab7aab8520bf/src/decision.ts); [src/telemetry.ts](https://github.com/DoSomeForFun/kuafu/blob/0628a879bb2ca24be9142ef32c49ab7aab8520bf/src/telemetry.ts); [src/kernel/handlers.ts](https://github.com/DoSomeForFun/kuafu/blob/0628a879bb2ca24be9142ef32c49ab7aab8520bf/src/kernel/handlers.ts); [README.md](https://github.com/DoSomeForFun/kuafu/blob/0628a879bb2ca24be9142ef32c49ab7aab8520bf/README.md) trace/replay
- Basis: structural
- Confidence: medium
- Caveats: Verifiable Tape terminology and ordinary test cases do not establish independent operational S3*.

### Absence scope

- Surfaces inspected: [src/decision.ts](https://github.com/DoSomeForFun/kuafu/blob/0628a879bb2ca24be9142ef32c49ab7aab8520bf/src/decision.ts); [src/telemetry.ts](https://github.com/DoSomeForFun/kuafu/blob/0628a879bb2ca24be9142ef32c49ab7aab8520bf/src/telemetry.ts); [src/kernel/handlers.ts](https://github.com/DoSomeForFun/kuafu/blob/0628a879bb2ca24be9142ef32c49ab7aab8520bf/src/kernel/handlers.ts); [README.md](https://github.com/DoSomeForFun/kuafu/blob/0628a879bb2ca24be9142ef32c49ab7aab8520bf/README.md) trace/replay; runtime entry, roles/tools, supported configuration and operating documentation within the declared boundary.
- Plausible first-party paths checked: Telemetry, stored tool results, Decision.semanticCheck and README trace/replay examples; autonomous and operator-governed alternatives were checked for no independent complementary audit loop.
- Why no material first-party path remains: semanticCheck only checks non-empty response in source; logs and replay recipes have no separately owned audit judgment/return loop Verifiable Tape terminology and ordinary test cases do not establish independent operational S3*. This is a bounded shipped-distribution conclusion, not impossibility of an extension.

## S4 — Outside-and-then intelligence

- State: —
- Function: No external-and-prospective adaptation function
- Disturbance / variety regulated: Future-relevant environmental/capability changes
- Decisive decision or feedback right: No supplied sensing/options-to-current-capability adaptation judgment established
- Decision owner: None established
- Supporting / enforcement mechanisms: Perception, lesson retrieval, skill discovery/cache refresh, semantic recall and REFLECTING
- Closure path: Perception recalls task context; REFLECTING persists tool results; skill matching selects existing files. No external/future options are developed and returned as capability changes
- Why this is / is not agent-owned: None established; Learning/lessons/memory labels and generic custom hooks do not supply an S4-specific constructor or parent adaptation loop.
- Evidence: [src/perception.ts](https://github.com/DoSomeForFun/kuafu/blob/0628a879bb2ca24be9142ef32c49ab7aab8520bf/src/perception.ts); [src/skills.ts](https://github.com/DoSomeForFun/kuafu/blob/0628a879bb2ca24be9142ef32c49ab7aab8520bf/src/skills.ts); [src/kernel/handlers.ts](https://github.com/DoSomeForFun/kuafu/blob/0628a879bb2ca24be9142ef32c49ab7aab8520bf/src/kernel/handlers.ts); [src/store.ts](https://github.com/DoSomeForFun/kuafu/blob/0628a879bb2ca24be9142ef32c49ab7aab8520bf/src/store.ts)
- Basis: structural
- Confidence: medium
- Caveats: Learning/lessons/memory labels and generic custom hooks do not supply an S4-specific constructor or parent adaptation loop.

### Absence scope

- Surfaces inspected: [src/perception.ts](https://github.com/DoSomeForFun/kuafu/blob/0628a879bb2ca24be9142ef32c49ab7aab8520bf/src/perception.ts); [src/skills.ts](https://github.com/DoSomeForFun/kuafu/blob/0628a879bb2ca24be9142ef32c49ab7aab8520bf/src/skills.ts); [src/kernel/handlers.ts](https://github.com/DoSomeForFun/kuafu/blob/0628a879bb2ca24be9142ef32c49ab7aab8520bf/src/kernel/handlers.ts); [src/store.ts](https://github.com/DoSomeForFun/kuafu/blob/0628a879bb2ca24be9142ef32c49ab7aab8520bf/src/store.ts); runtime entry, roles/tools, supported configuration and operating documentation within the declared boundary.
- Plausible first-party paths checked: Perception, lesson retrieval, skill discovery/cache refresh, semantic recall and REFLECTING; autonomous and operator-governed alternatives were checked for no external-and-prospective adaptation function.
- Why no material first-party path remains: Perception recalls task context; REFLECTING persists tool results; skill matching selects existing files. No external/future options are developed and returned as capability changes Learning/lessons/memory labels and generic custom hooks do not supply an S4-specific constructor or parent adaptation loop. This is a bounded shipped-distribution conclusion, not impossibility of an extension.

## S5 — Policy and identity

- State: —
- Function: No identity/ultimate-policy closure
- Disturbance / variety regulated: Task-system purpose or ultimate policy in dispute
- Decisive decision or feedback right: No legitimate authority issue/decision/return protocol established
- Decision owner: Caller configuration alone; no qualifying S5 owner
- Supporting / enforcement mechanisms: Before/after hook decisions, routing environment, optional SOUL text/cache, tool configuration
- Closure path: Hooks allow/capture/silence/rewrite individual runs; routing and persona configuration constrain execution without adjudicating ultimate identity/policy
- Why this is / is not agent-owned: Caller configuration alone; no qualifying S5 owner; A generic hook or human caller is not a parent S5 mode merely because it can change execution.
- Evidence: [src/runtime.ts](https://github.com/DoSomeForFun/kuafu/blob/0628a879bb2ca24be9142ef32c49ab7aab8520bf/src/runtime.ts); [src/kernel/index.ts](https://github.com/DoSomeForFun/kuafu/blob/0628a879bb2ca24be9142ef32c49ab7aab8520bf/src/kernel/index.ts); [src/perception.ts](https://github.com/DoSomeForFun/kuafu/blob/0628a879bb2ca24be9142ef32c49ab7aab8520bf/src/perception.ts); [src/routing-config.ts](https://github.com/DoSomeForFun/kuafu/blob/0628a879bb2ca24be9142ef32c49ab7aab8520bf/src/routing-config.ts)
- Basis: structural
- Confidence: medium
- Caveats: A generic hook or human caller is not a parent S5 mode merely because it can change execution.

### Absence scope

- Surfaces inspected: [src/runtime.ts](https://github.com/DoSomeForFun/kuafu/blob/0628a879bb2ca24be9142ef32c49ab7aab8520bf/src/runtime.ts); [src/kernel/index.ts](https://github.com/DoSomeForFun/kuafu/blob/0628a879bb2ca24be9142ef32c49ab7aab8520bf/src/kernel/index.ts); [src/perception.ts](https://github.com/DoSomeForFun/kuafu/blob/0628a879bb2ca24be9142ef32c49ab7aab8520bf/src/perception.ts); [src/routing-config.ts](https://github.com/DoSomeForFun/kuafu/blob/0628a879bb2ca24be9142ef32c49ab7aab8520bf/src/routing-config.ts); runtime entry, roles/tools, supported configuration and operating documentation within the declared boundary.
- Plausible first-party paths checked: Before/after hook decisions, routing environment, optional SOUL text/cache, tool configuration; autonomous and operator-governed alternatives were checked for no identity/ultimate-policy closure.
- Why no material first-party path remains: Hooks allow/capture/silence/rewrite individual runs; routing and persona configuration constrain execution without adjudicating ultimate identity/policy A generic hook or human caller is not a parent S5 mode merely because it can change execution. This is a bounded shipped-distribution conclusion, not impossibility of an extension.

## Distributed OSS parent arrangement

Public contributors and maintainers are outside this deployed-runtime recursion. Local operator decisions do not imply project-wide or organization-wide parent governance.

## Self-hosted and non-human modes

Self-hosted operation is the assessed mode; parent notation is used only for the explicitly established function-specific loop, if any. No intentionally non-human governing organization is supplied.

## Recursion

Agents, tasks and sessions may be nested, but this does not establish independent viable systems with their own complete metasystem.

## Variety and escalation

Host task store/files/shell, injected model provider, tool failures and caller-supplied runtime events/context. One configured Kernel run is the operational agent unit. The model chooses contextual tools and final answer; deterministic FSM/turn limits enforce its loop. Concurrent tool calls within one turn are actions of that unit, not separate autonomous S1 units. No shipped team regulator, independent audit owner or prospective capability/ultimate-policy organization is supplied.

## Evidence gaps

Source/static assessment only; inspection host lacks Node/npm, so npm build/test/typecheck and provider execution were not run. Important distribution/API limitations: checked-in dist/index.js imports missing chunk files; constructor consumes llmProvider rather than README llm; dts generation is disabled although package declarations name .d.ts files; README's named bridge/composite memory and traceSink/replay features are not assumed implemented here. A records the explicit standard source-build real-provider path, not an out-of-box installation/performance guarantee. No independent semantic review.

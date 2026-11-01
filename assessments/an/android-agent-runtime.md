---
harness_id: android-agent-runtime
project_name: Android Agent Runtime
repository: https://github.com/NoHarry/android-agent-runtime
review_ref: 57267123cf43ed832f50f65de89023adf84578db
reviewed_at: 2026-11-01
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Android Agent Runtime

## Review boundary

- System in focus: the embeddable first-party JVM/Android agent runtime, including documented optional Android Use integration.
- Purpose and identity: run model-directed tool/workspace tasks inside a host process with durable sessions.
- Relevant environment: host applications, model/provider endpoints, mounted virtual filesystems, MCP servers and optional shared Android screen.
- Standard-distribution boundary: published runtime/core modules configured through AgentRuntimeBuilder or AndroidAgentRuntime; optional first-party tools only where installed.
- Credited operating / distribution surfaces: native model/tool loop and builders; session/confirmation/retention support; Android Use provider and process-wide screen lease in its supported optional mode.
- Adjacent first-party surfaces excluded from ownership: sample apps and fake providers are wiring illustrations; tools/bench/a2a test infrastructure, probes and contributor workflows are not autonomous runtime owners; remote agents/providers are external.
- First-party operating / deployment modes considered: JVM and Android embeddings with model/tools/workspace configured; optional Subagents launcher, Android Use accessibility module and host-controlled confirmation.
- Recursion level: runtime and its independently operating session agents; subagent creation alone is not recursive viability.
- Reviewed revision: 57267123cf43ed832f50f65de89023adf84578db.
- Observation date: 2026-11-01.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The builder compiles model/tool/plugin declarations into DefaultAgentRuntime. NativeToolLoop initializes request/history/context, calls NativeRoundRunner, executes tools through NativeToolUseController, and feeds results or confirmation/user-input continuations back into subsequent rounds. Virtual filesystems bound workspace access; session stores/event logs support persistence and replay. SessionRunScheduler provides per-session ownership tokens and cross-session fair execution permits; provider limits and loop budgets constrain resource use. Subagents exposes model-facing spawn/wait/cancel, but the host supplies its launcher/report delivery. PolicyEngine evaluates host-authored tool rules. Optional AndroidUseToolProvider executes accessibility observations/actions under one process-wide screen lease. DreamRecords contains candidate/scaffold memory workers rather than a prospective intelligence actor. Probes are explicitly observe-only and completion obligations are production checks.

## Operational model

The model actor owns task/tool choices in the configured native loop. The host selects permissions, budgets, mounts and integrations. The optional screen module exposes a concrete inter-session interference-regulation constructor: one screen cannot safely receive competing action streams. No autonomous whole-runtime resource manager, independent corrective auditor, prospective capability-adaptation actor or ultimate-policy adjudicator is wired by these configuration APIs.

## S1 — Operations

- State: A
- Function: carry user tasks through discretionary model/tool observation cycles to a result.
- Disturbance / variety regulated: workspace content, tool errors, retrieved information and user continuation.
- Decisive decision or feedback right: select tools and arguments, interpret observations and revise/finish the task.
- Decision owner: the configured ModelClient-backed actor inside the native loop.
- Supporting / enforcement mechanisms: round runner/tool controller, VFS, budgets, hooks, history, confirmation store and provider adapters.
- Closure path: model-selected calls produce tool messages consumed by later native rounds; explicit finish and unresolved obligations determine task termination.
- Why this is / is not agent-owned: without the model actor deterministic hooks/storage cannot choose the operational transformation.
- Evidence: [agent-runtime/src/main/kotlin/cc/noharry/agent/runtime/AgentRuntimeBuilder.kt](https://github.com/NoHarry/android-agent-runtime/blob/57267123cf43ed832f50f65de89023adf84578db/agent-runtime/src/main/kotlin/cc/noharry/agent/runtime/AgentRuntimeBuilder.kt); [agent-runtime/src/main/kotlin/cc/noharry/agent/runtime/DefaultAgentRuntime.kt](https://github.com/NoHarry/android-agent-runtime/blob/57267123cf43ed832f50f65de89023adf84578db/agent-runtime/src/main/kotlin/cc/noharry/agent/runtime/DefaultAgentRuntime.kt); [agent-runtime/src/main/kotlin/cc/noharry/agent/runtime/run/NativeLoopFactory.kt](https://github.com/NoHarry/android-agent-runtime/blob/57267123cf43ed832f50f65de89023adf84578db/agent-runtime/src/main/kotlin/cc/noharry/agent/runtime/run/NativeLoopFactory.kt); [agent-kernel-core/src/main/kotlin/cc/noharry/agent/kernel/core/loop/NativeToolLoop.kt](https://github.com/NoHarry/android-agent-runtime/blob/57267123cf43ed832f50f65de89023adf84578db/agent-kernel-core/src/main/kotlin/cc/noharry/agent/kernel/core/loop/NativeToolLoop.kt); [agent-kernel-core/src/main/kotlin/cc/noharry/agent/kernel/core/loop/NativeRoundRunner.kt](https://github.com/NoHarry/android-agent-runtime/blob/57267123cf43ed832f50f65de89023adf84578db/agent-kernel-core/src/main/kotlin/cc/noharry/agent/kernel/core/loop/NativeRoundRunner.kt)
- Basis: structural
- Confidence: high
- Caveats: Bounded source assessment of the supported distribution; no live model or performance claim.
- Boundary reachability: AgentRuntimeBuilder.build wires the supplied model into DefaultAgentRuntime/NativeLoopFactory; supported Android builder wraps that path.

## S2 — Coordination

- State: C
- Function: attenuate destructive concurrent interaction between independent session agents acting on one physical screen.
- Disturbance / variety regulated: different conversations/A2A callers can issue screen observations/gestures against changing UI state.
- Decisive decision or feedback right: grant and retain exclusive current-screen actor access, reject competing sessions and release after idle expiry.
- Decision owner: first-party developer-composed AndroidUseLease rule; autonomous coordination policy/authority would need composition.
- Supporting / enforcement mechanisms: process-wide lease, monotonic timing, session/run IDs, DEVICE_BUSY tool result and lease touch after action.
- Closure path: AndroidUseToolProvider.callTool acquires the lease before observe/action; a competing session receives DEVICE_BUSY in its own tool feedback and must change its subsequent task behavior.
- Why this is / is not agent-owned: the agent can respond to contention but does not own the fixed lease arbitration rule; C credits the S2-specific constructor, not deterministic enforcement as autonomy.
- Evidence: [agent-android-use/src/main/kotlin/cc/noharry/agent/androiduse/AndroidUseLease.kt](https://github.com/NoHarry/android-agent-runtime/blob/57267123cf43ed832f50f65de89023adf84578db/agent-android-use/src/main/kotlin/cc/noharry/agent/androiduse/AndroidUseLease.kt); [agent-android-use/src/main/kotlin/cc/noharry/agent/androiduse/AndroidUseToolProvider.kt](https://github.com/NoHarry/android-agent-runtime/blob/57267123cf43ed832f50f65de89023adf84578db/agent-android-use/src/main/kotlin/cc/noharry/agent/androiduse/AndroidUseToolProvider.kt); [README.md](https://github.com/NoHarry/android-agent-runtime/blob/57267123cf43ed832f50f65de89023adf84578db/README.md)
- Basis: structural
- Confidence: medium-high
- Caveats: Bounded source assessment of the supported distribution; no live model or performance claim.
- Distinct S1 units: model-directed session/conversation or A2A-caller agents with independent tasks sharing a device screen.
- Inter-S1 disturbance: one actor's gestures alter the UI context observed/acted on by another actor.
- Attenuating coordination relation: one process-wide screen holder, same-session continuation takeover and cross-session idle lease.
- Feedback into subsequent S1 behaviour: DEVICE_BUSY is returned instead of executing competing actions, allowing the model/tool loop to defer or choose another action.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the lease explicitly exists for one-actor-per-screen interference, and is enforced immediately at the first-party screen observation/action boundary.
- Boundary reachability: supported optional Android Use provider installs into the same runtime tool path; its public constructor uses the process-wide lease. This is not credited to the core when the module is absent.

## S3 — Inside-and-now control

- State: —
- Function: No function-specific whole-runtime discretionary resource/commitment control actor is supplied.
- Disturbance / variety regulated: model/tool capacity, queue length, same-session ownership and child duration.
- Decisive decision or feedback right: No qualifying function-specific decisive right established.
- Decision owner: No owner established for this function at the declared boundary.
- Supporting / enforcement mechanisms: SessionRunScheduler, provider concurrency, loop budgets, subagent watchdogs and cancellation.
- Closure path: No qualifying organizational return path; ordinary task feedback is separate.
- Why this is / is not agent-owned: The examined paths do not supply the agent-owned or eligible parent-governed function.
- Evidence: [agent-kernel-core/src/main/kotlin/cc/noharry/agent/kernel/core/state/SessionRunScheduler.kt](https://github.com/NoHarry/android-agent-runtime/blob/57267123cf43ed832f50f65de89023adf84578db/agent-kernel-core/src/main/kotlin/cc/noharry/agent/kernel/core/state/SessionRunScheduler.kt); [agent-runtime/src/main/kotlin/cc/noharry/agent/runtime/AgentRuntimeBuilder.kt](https://github.com/NoHarry/android-agent-runtime/blob/57267123cf43ed832f50f65de89023adf84578db/agent-runtime/src/main/kotlin/cc/noharry/agent/runtime/AgentRuntimeBuilder.kt); [agent-runtime/src/main/kotlin/cc/noharry/agent/runtime/Subagents.kt](https://github.com/NoHarry/android-agent-runtime/blob/57267123cf43ed832f50f65de89023adf84578db/agent-runtime/src/main/kotlin/cc/noharry/agent/runtime/Subagents.kt); [agent-kernel-core/src/main/kotlin/cc/noharry/agent/kernel/core/loop/LoopBudgetConfig.kt](https://github.com/NoHarry/android-agent-runtime/blob/57267123cf43ed832f50f65de89023adf84578db/agent-kernel-core/src/main/kotlin/cc/noharry/agent/kernel/core/loop/LoopBudgetConfig.kt)
- Basis: structural
- Confidence: medium-high
- Caveats: Bounded source assessment of the supported distribution; no live model or performance claim.

### Absence scope

- Surfaces inspected: session admission/scheduling, builder resource limits, provider/tool limiting and child watchdog/report APIs.
- Plausible first-party paths checked: whole-current view with discretionary reprioritization/resource bargaining, child status supervision and host confirmation/current-control return.
- Why no material first-party path remains: fixed fair scheduling, configured caps and child lifecycle transport enforce host choices; generic status/cancel/launcher APIs do not intentionally expose a whole-system S3 decision path.

## S3* — Complementary audit

- State: —
- Function: No independent complementary challenge and returned corrective judgment is supplied.
- Disturbance / variety regulated: unreliable completion claims and incomplete tool obligations.
- Decisive decision or feedback right: No qualifying function-specific decisive right established.
- Decision owner: No owner established for this function at the declared boundary.
- Supporting / enforcement mechanisms: completion ledger/gate, event logs, probes, trace redaction and generic hooks/observers.
- Closure path: No qualifying organizational return path; ordinary task feedback is separate.
- Why this is / is not agent-owned: The examined paths do not supply the agent-owned or eligible parent-governed function.
- Evidence: [agent-kernel-core/src/main/kotlin/cc/noharry/agent/kernel/core/loop/RuntimeCompletionGate.kt](https://github.com/NoHarry/android-agent-runtime/blob/57267123cf43ed832f50f65de89023adf84578db/agent-kernel-core/src/main/kotlin/cc/noharry/agent/kernel/core/loop/RuntimeCompletionGate.kt); [agent-kernel-core/src/main/kotlin/cc/noharry/agent/kernel/core/loop/RuntimeObligationLedger.kt](https://github.com/NoHarry/android-agent-runtime/blob/57267123cf43ed832f50f65de89023adf84578db/agent-kernel-core/src/main/kotlin/cc/noharry/agent/kernel/core/loop/RuntimeObligationLedger.kt); [agent-runtime/src/main/kotlin/cc/noharry/agent/runtime/probe/ProbeBus.kt](https://github.com/NoHarry/android-agent-runtime/blob/57267123cf43ed832f50f65de89023adf84578db/agent-runtime/src/main/kotlin/cc/noharry/agent/runtime/probe/ProbeBus.kt); [agent-runtime/src/main/kotlin/cc/noharry/agent/runtime/dream/DreamRecords.kt](https://github.com/NoHarry/android-agent-runtime/blob/57267123cf43ed832f50f65de89023adf84578db/agent-runtime/src/main/kotlin/cc/noharry/agent/runtime/dream/DreamRecords.kt)
- Basis: structural
- Confidence: medium-high
- Caveats: Bounded source assessment of the supported distribution; no live model or performance claim.

### Absence scope

- Surfaces inspected: completion acceptance, obligation tracking, probe/event/trace support, observers, Dream scaffold and sample/test boundaries.
- Plausible first-party paths checked: independent artifact inspection versus producer self-report, first-party audit judgment and returned correction.
- Why no material first-party path remains: completion gates check production obligations, probes are observe-only, and generic observer/hooks require a custom audit actor and authority; the shipped Dream paths do not supply that complementary challenge.

## S4 — Outside-and-then intelligence

- State: —
- Function: No supplied external-and-prospective capability-adaptation loop is established.
- Disturbance / variety regulated: context growth, memory retrieval and provider/tool availability are current execution concerns.
- Decisive decision or feedback right: No qualifying function-specific decisive right established.
- Decision owner: No owner established for this function at the declared boundary.
- Supporting / enforcement mechanisms: skills registry, memory candidate extraction/retrieval, Dream workers and context compaction.
- Closure path: No qualifying organizational return path; ordinary task feedback is separate.
- Why this is / is not agent-owned: The examined paths do not supply the agent-owned or eligible parent-governed function.
- Evidence: [agent-runtime/src/main/kotlin/cc/noharry/agent/runtime/dream/DreamRecords.kt](https://github.com/NoHarry/android-agent-runtime/blob/57267123cf43ed832f50f65de89023adf84578db/agent-runtime/src/main/kotlin/cc/noharry/agent/runtime/dream/DreamRecords.kt); [agent-kernel-core/src/main/kotlin/cc/noharry/agent/kernel/core/memory/MemoryCandidateExtractor.kt](https://github.com/NoHarry/android-agent-runtime/blob/57267123cf43ed832f50f65de89023adf84578db/agent-kernel-core/src/main/kotlin/cc/noharry/agent/kernel/core/memory/MemoryCandidateExtractor.kt); [agent-kernel-core/src/main/kotlin/cc/noharry/agent/kernel/core/memory/RuntimeMemoryPolicy.kt](https://github.com/NoHarry/android-agent-runtime/blob/57267123cf43ed832f50f65de89023adf84578db/agent-kernel-core/src/main/kotlin/cc/noharry/agent/kernel/core/memory/RuntimeMemoryPolicy.kt); [agent-runtime/src/main/kotlin/cc/noharry/agent/runtime/SkillRegistry.kt](https://github.com/NoHarry/android-agent-runtime/blob/57267123cf43ed832f50f65de89023adf84578db/agent-runtime/src/main/kotlin/cc/noharry/agent/runtime/SkillRegistry.kt); [agent-runtime/src/main/kotlin/cc/noharry/agent/runtime/AgentRuntimeBuilder.kt](https://github.com/NoHarry/android-agent-runtime/blob/57267123cf43ed832f50f65de89023adf84578db/agent-runtime/src/main/kotlin/cc/noharry/agent/runtime/AgentRuntimeBuilder.kt)
- Basis: structural
- Confidence: medium-high
- Caveats: Bounded source assessment of the supported distribution; no live model or performance claim.

### Absence scope

- Surfaces inspected: Dream candidate/scaffold workers, memory/index paths, skill loading, compaction and provider/plugin configuration.
- Plausible first-party paths checked: future environment distinctions generating capability alternatives and returned adoption, including a legitimate parent adaptation mode.
- Why no material first-party path remains: memory maintenance, task-time discovery and configurable integrations supply no prospective option-generation/adoption loop; a no-op/index-rebuild scaffold does not establish S4.

## S5 — Policy and identity

- State: —
- Function: No identity/ultimate-policy issue-decision-return loop is supplied.
- Disturbance / variety regulated: ordinary tool permissions and host profile/configuration.
- Decisive decision or feedback right: No qualifying function-specific decisive right established.
- Decision owner: No owner established for this function at the declared boundary.
- Supporting / enforcement mechanisms: PolicyEngine, compiled immutable AgentProfile, confirmations and host-provided hooks.
- Closure path: No qualifying organizational return path; ordinary task feedback is separate.
- Why this is / is not agent-owned: The examined paths do not supply the agent-owned or eligible parent-governed function.
- Evidence: [agent-runtime/src/main/kotlin/cc/noharry/agent/policy/PolicyEngine.kt](https://github.com/NoHarry/android-agent-runtime/blob/57267123cf43ed832f50f65de89023adf84578db/agent-runtime/src/main/kotlin/cc/noharry/agent/policy/PolicyEngine.kt); [agent-runtime/src/main/kotlin/cc/noharry/agent/runtime/AgentRuntimeBuilder.kt](https://github.com/NoHarry/android-agent-runtime/blob/57267123cf43ed832f50f65de89023adf84578db/agent-runtime/src/main/kotlin/cc/noharry/agent/runtime/AgentRuntimeBuilder.kt); [agent-kernel-core/src/main/kotlin/cc/noharry/agent/kernel/core/plugin/ProfileCompiler.kt](https://github.com/NoHarry/android-agent-runtime/blob/57267123cf43ed832f50f65de89023adf84578db/agent-kernel-core/src/main/kotlin/cc/noharry/agent/kernel/core/plugin/ProfileCompiler.kt); [agent-kernel-core/src/main/kotlin/cc/noharry/agent/kernel/core/state/PendingToolUseController.kt](https://github.com/NoHarry/android-agent-runtime/blob/57267123cf43ed832f50f65de89023adf84578db/agent-kernel-core/src/main/kotlin/cc/noharry/agent/kernel/core/state/PendingToolUseController.kt); [README.md](https://github.com/NoHarry/android-agent-runtime/blob/57267123cf43ed832f50f65de89023adf84578db/README.md)
- Basis: structural
- Confidence: medium-high
- Caveats: Bounded source assessment of the supported distribution; no live model or performance claim.

### Absence scope

- Surfaces inspected: policy evaluation, profile compilation, confirmation resume, host hooks and operator/embedding documentation.
- Plausible first-party paths checked: ultimate authority deciding an identity-level dispute and returning binding policy into subsequent operation.
- Why no material first-party path remains: profiles and rules are authored configuration; approval resumes an ordinary tool action and generic hooks do not establish a first-party identity-level governance transaction.

## Recursion

Host, runtime, session and child nesting are explicit implementation boundaries, not evidence that each contains a viable metasystem.

## Variety and escalation

Tool results, busy-screen responses, confirmations and user-input resumptions return local variety to the responsible task actor/host. Scheduler generation tokens prevent stale releases. These are operational channels, not by themselves an algedonic path or higher-function decision.

## Evidence gaps

No Android device/provider or LLM-agent E2E run. S2=C is restricted to the optional first-party screen-sharing path. Host-supplied launcher/observers and remote A2A agents are not credited as shipped autonomous metasystem owners. No specific unresolved in-boundary positive path was identified after inspecting the listed runtime and optional integration surfaces.

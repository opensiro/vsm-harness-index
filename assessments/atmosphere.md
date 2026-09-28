---
harness_id: atmosphere
project_name: Atmosphere
repository: https://github.com/Atmosphere/atmosphere
review_ref: 5eaac40919357742ac0d67c59840d0b6eb909d53
reviewed_at: 2026-09-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-29
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# Atmosphere

## Review boundary

- System in focus: the first-party Atmosphere AI/deep-agent runtime and coordinator/fleet stack at frozen revision `5eaac40919357742ac0d67c59840d0b6eb909d53`, including the built-in agent runtime/model-tool loop, harness preset, first-party tools, memory/planning/filesystem surfaces, coordinator/fleet orchestration, governance interception, result-evaluation/refinement machinery, sandbox and protocol/channel serving.
- Purpose and identity: provide a JVM agent/application runtime in which first-party `@Agent`, `@Coordinator` and opted-in `@AiEndpoint` surfaces can run model-driven tool loops with memory, planning, bounded files, delegation and governance, while supporting multi-agent fleet composition.
- Relevant environment: users/operators, external model providers and models, remote A2A agents, MCP servers/tools, application-defined business tools, Spring/Quarkus/servlet containers and external stores/services.
- Standard-distribution boundary: first-party runtime loops, harness preset, built-in tools, fleet/coordinator machinery, governance/evaluation seams and shipped adapters are inside. External model/provider internals, remote agents, operator-authored application policy content, application-specific business tools and unrelated deployment infrastructure remain environment.
- Credited operating / distribution surfaces: `modules/ai`, `modules/coordinator`, the default deep-agent harness described in `docs/deep-agent.md`, first-party governance machinery, sandbox/tool execution, memory/planning/filesystem primitives and supported protocol/channel bridges.
- Adjacent first-party surfaces excluded from ownership: repository CI/tests, release/maintainer activity, samples used only as demonstrations, documentation publishing, benchmark/development workflows and contributor governance. Tests corroborate shipped paths but do not themselves own VSM functions.
- First-party operating / deployment modes considered: built-in `AgentRuntime`; default `@Agent` and `@Coordinator` `Harness.ALL`; coordinator fleet with model-callable `delegate_task` / `task`; policy-intercepted fleet dispatch; evaluator-driven `refineUntil`; supported Spring/Quarkus/plain-servlet modes.
- Recursion level: one deployed Atmosphere agent application / coordinator fleet. Individual autonomous `@Agent`/spawned subagent instances are S1 operational units relative to the fleet. Repository-development governance is a separate recursion and is not borrowed.
- Reviewed revision: `5eaac40919357742ac0d67c59840d0b6eb909d53`.
- Observation date: 2026-09-29.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Atmosphere ships a real first-party autonomous agent loop rather than only wrappers around external agent frameworks. `BuiltInAgentRuntime` advertises `TOOL_CALLING`; `OpenAiCompatibleClient` repeatedly submits model-visible tool schemas, receives model tool calls, executes them through the first-party approval/tool-execution helper, appends tool results to the conversation and re-enters the model until a terminal response or bound is reached. The external model supplies discretionary reasoning, while Atmosphere owns the runtime loop, tool exposure/execution, returned observations, budgets/approval wiring and continuation semantics.

The deep-agent harness is standard-distribution behavior. `docs/deep-agent.md` states that `@Agent` and `@Coordinator` are batteries-included by default with `Harness.ALL`, adding memory, cache, delegation, planning and bounded filesystem primitives. For coordinators, `CoordinatorProcessor` creates a first-party model runtime, resolves the declared fleet, registers model-callable delegation/subagent tools and injects the finished `AgentFleet` into the same prompt/runtime surface.

The strongest metasystem constructor evidence is narrow and function-specific. For S2, `GovernanceFleetInterceptor` explicitly treats cross-agent goal hijacking as an agent-to-agent coordination risk and can deny or transform the actual outbound payload before the target S1 receives it; `CoordinatorProcessor` installs that governance wrapper on the default delegation path when policies are present. The coordination policy itself is developer/operator supplied or deterministic, so autonomous S2 ownership is not closed.

For S3*, `AgentFleet.refineUntil` supplies a dedicated result-evaluation feedback loop: worker output is evaluated, failed evaluator reasons are injected under `_refine_feedback`, and the worker is re-dispatched until pass or a bounded terminal condition. `ResultEvaluator` is explicitly composable and the standard service registration supplies `SanityCheckEvaluator`. The default evaluator only inspects the reported result and is not sufficiently independent for complementary-audit ownership. The first-party verification/feedback constructor can, however, be supplied a materially independent evaluator without reimplementing the corrective return loop, supporting `C` rather than `A`.

Primary evidence:

- [`docs/deep-agent.md`](https://github.com/Atmosphere/atmosphere/blob/5eaac40919357742ac0d67c59840d0b6eb909d53/docs/deep-agent.md) — default harness reachability and built-in memory/delegation/planning/filesystem surfaces.
- [`modules/ai/src/main/java/org/atmosphere/ai/llm/BuiltInAgentRuntime.java`](https://github.com/Atmosphere/atmosphere/blob/5eaac40919357742ac0d67c59840d0b6eb909d53/modules/ai/src/main/java/org/atmosphere/ai/llm/BuiltInAgentRuntime.java) — first-party built-in runtime and tool-calling capability.
- [`modules/ai/src/main/java/org/atmosphere/ai/llm/OpenAiCompatibleClient.java`](https://github.com/Atmosphere/atmosphere/blob/5eaac40919357742ac0d67c59840d0b6eb909d53/modules/ai/src/main/java/org/atmosphere/ai/llm/OpenAiCompatibleClient.java) — iterative model/tool/result continuation loop.
- [`modules/coordinator/README.md`](https://github.com/Atmosphere/atmosphere/blob/5eaac40919357742ac0d67c59840d0b6eb909d53/modules/coordinator/README.md) — coordinator/fleet, model-callable delegation, isolated spawned subagents, journaling and evaluation surfaces.
- [`modules/coordinator/src/main/java/org/atmosphere/coordinator/fleet/GovernanceFleetInterceptor.java`](https://github.com/Atmosphere/atmosphere/blob/5eaac40919357742ac0d67c59840d0b6eb909d53/modules/coordinator/src/main/java/org/atmosphere/coordinator/fleet/GovernanceFleetInterceptor.java) — cross-agent goal-hijack regulation through deny/transform.
- [`modules/coordinator/src/main/java/org/atmosphere/coordinator/processor/CoordinatorProcessor.java`](https://github.com/Atmosphere/atmosphere/blob/5eaac40919357742ac0d67c59840d0b6eb909d53/modules/coordinator/src/main/java/org/atmosphere/coordinator/processor/CoordinatorProcessor.java) — standard coordinator runtime/fleet/governance/delegation wiring.
- [`modules/coordinator/src/main/java/org/atmosphere/coordinator/fleet/AgentFleet.java`](https://github.com/Atmosphere/atmosphere/blob/5eaac40919357742ac0d67c59840d0b6eb909d53/modules/coordinator/src/main/java/org/atmosphere/coordinator/fleet/AgentFleet.java) — evaluator-driven bounded `refineUntil` return loop and fleet health/execution surfaces.
- [`modules/coordinator/src/main/java/org/atmosphere/coordinator/evaluation/SanityCheckEvaluator.java`](https://github.com/Atmosphere/atmosphere/blob/5eaac40919357742ac0d67c59840d0b6eb909d53/modules/coordinator/src/main/java/org/atmosphere/coordinator/evaluation/SanityCheckEvaluator.java) — default deterministic result evaluator.
- [`docs/governance-policy-plane.md`](https://github.com/Atmosphere/atmosphere/blob/5eaac40919357742ac0d67c59840d0b6eb909d53/docs/governance-policy-plane.md) — operator-authored policy enforcement and audit identity, used as a boundary witness rather than S5 credit.

## Operational model

A standard Atmosphere `@Agent`/`@Coordinator` can receive a user/application goal, call a model through the first-party runtime, receive model-selected tool calls, execute allowed tools and return their observations for another model turn. The harness can persist conversation/long-term memory, expose planning and bounded file tools, and for coordinators expose delegation to declared or ephemeral agents. This supplies autonomous operational discretion while deterministic code retains safety, budgets, transport and execution enforcement.

At the fleet level, autonomous S1 units may be composed under one coordinator. Atmosphere provides several mechanisms around them — routing, fan-out, pipeline, voting, retries, circuit breakers, journaling, health and evaluation. Those names are not mapped mechanically. Only the cross-agent governance path is credited as S2 because it is tied to a concrete inter-S1 goal-hijacking disturbance; only `refineUntil`/`ResultEvaluator` is credited as S3* because it is a dedicated judgment/feedback constructor. No whole-system current-control owner, prospective adaptation loop or identity/ultimate-policy closure was established.

## S1 — Operations

- State: A
- Function: execute open-ended agent work through a model-driven decision/action/observation loop with first-party tool execution and continuation.
- Disturbance / variety regulated: user/application goals, conversation state, tool results/errors, external service/file state reached through tools, model uncertainty and bounded runtime constraints.
- Decisive decision or feedback right: choose the next substantive response/tool action from the current context and returned observations.
- Decision owner: the autonomous model-driven agent actor running inside Atmosphere's first-party `AgentRuntime` loop.
- Supporting / enforcement mechanisms: `BuiltInAgentRuntime`, `OpenAiCompatibleClient`, tool registry/execution helper, approvals, budgets, conversation/long-term memory, planning/filesystem tools, sandbox and protocol/channel transport.
- Closure path: goal/context → model turn → model-selected tool call or answer → Atmosphere validates/executes allowed tool → tool result enters conversation → next model turn revises/continues → final response or bounded stop.
- Why this is / is not agent-owned: deterministic host code exposes/enforces actions but does not choose the substantive next tool/action. Removing the model-driven actor leaves a capable runtime without the task-level discretionary loop.
- Evidence: [`BuiltInAgentRuntime.java`](https://github.com/Atmosphere/atmosphere/blob/5eaac40919357742ac0d67c59840d0b6eb909d53/modules/ai/src/main/java/org/atmosphere/ai/llm/BuiltInAgentRuntime.java); [`OpenAiCompatibleClient.java`](https://github.com/Atmosphere/atmosphere/blob/5eaac40919357742ac0d67c59840d0b6eb909d53/modules/ai/src/main/java/org/atmosphere/ai/llm/OpenAiCompatibleClient.java); [`docs/deep-agent.md`](https://github.com/Atmosphere/atmosphere/blob/5eaac40919357742ac0d67c59840d0b6eb909d53/docs/deep-agent.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: provider/model internals are environment; credit rests on Atmosphere's first-party loop and standard harness reachability, not on importing provider-side organizational functions.

## S2 — Coordination

- State: C
- Function: attenuate a concrete cross-agent interference mode — goal/scope hijacking on an outbound fleet dispatch — before the target S1 acts on the conflicting request.
- Disturbance / variety regulated: one S1/coordinator can dispatch a task whose requested skill/payload violates the target/fleet's installed scope/governance policy, allowing one agent's goal to hijack another operational unit.
- Decisive decision or feedback right: determine whether the inter-agent call proceeds, is denied, or has its message-bearing arguments transformed before delivery.
- Decision owner: constructor/configuration path. First-party `GovernanceFleetInterceptor` owns the S2-specific enforcement/return seam, but the substantive policy decision is supplied by installed `GovernancePolicy` implementations/operator/developer configuration rather than autonomously revised by a coordinator agent.
- Supporting / enforcement mechanisms: coordinator/fleet topology, default DELEGATION preset, `GovernanceFleetInterceptor`, policy chain, journaling, target `AgentProxy` and tool dispatch.
- Closure path: autonomous source S1 selects delegation → outbound `AgentCall` enters governance interceptor → policy admits/denies/transforms → deny suppresses target execution or transform changes the exact payload → target S1's subsequent behavior is changed before work proceeds; journal can record the denied/changed edge.
- Why this is / is not agent-owned: the repository explicitly identifies goal hijacking at the agent-to-agent edge and ships a disturbance-specific attenuation/feedback path, satisfying the S2 constructor threshold. The policy owner is not a packaged autonomous S2 actor, so the state is `C`, not `A`.
- Evidence: [`GovernanceFleetInterceptor.java`](https://github.com/Atmosphere/atmosphere/blob/5eaac40919357742ac0d67c59840d0b6eb909d53/modules/coordinator/src/main/java/org/atmosphere/coordinator/fleet/GovernanceFleetInterceptor.java); [`CoordinatorProcessor.java`](https://github.com/Atmosphere/atmosphere/blob/5eaac40919357742ac0d67c59840d0b6eb909d53/modules/coordinator/src/main/java/org/atmosphere/coordinator/processor/CoordinatorProcessor.java); [`modules/coordinator/README.md`](https://github.com/Atmosphere/atmosphere/blob/5eaac40919357742ac0d67c59840d0b6eb909d53/modules/coordinator/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: fan-out, pipelines, routing, voting and delegation are not independently credited as S2; the positive mapping rests specifically on the documented inter-agent goal-hijack/scope-conflict path.

## S3 — Inside-and-now control

- State: —
- Function: no first-party whole-system current-control decision loop was established at the declared fleet recursion.
- Disturbance / variety regulated: fleet availability, retries, circuit state, parallel execution, per-agent turn/depth limits and cancellations are visible/enforceable, but the reviewed paths do not establish organization-wide bargaining or intervention over current commitments/priorities/resources by exception.
- Decisive decision or feedback right: choose or revise whole-fleet current allocations, commitments, priorities, constraints or interventions from a whole-system current view.
- Decision owner: not established. Application/coordinator code or an operator can invoke execution/routing/cancellation primitives; deterministic limits/circuit breakers enforce configured rules.
- Supporting / enforcement mechanisms: `AgentFleet.health()`, `available()`, `parallelCancellable()`, `AgentLimits`, retry/circuit-breaker machinery, routing, coordinator fleet topology and activity/journal state.
- Closure path: individual calls can be routed, bounded, retried, cancelled or observed, but no standard path was found in which a whole-system current view feeds a legitimate S3 judgment that revises shared fleet commitments and returns as subsequent current-control state.
- Why this is / is not agent-owned: Profile 0.2.4 explicitly excludes worker selection, delegation, result merging and static enforcement from S3 by themselves. Atmosphere supplies strong control machinery but not the missing whole-system discretionary organ.
- Evidence: [`AgentFleet.java`](https://github.com/Atmosphere/atmosphere/blob/5eaac40919357742ac0d67c59840d0b6eb909d53/modules/coordinator/src/main/java/org/atmosphere/coordinator/fleet/AgentFleet.java); [`modules/coordinator/README.md`](https://github.com/Atmosphere/atmosphere/blob/5eaac40919357742ac0d67c59840d0b6eb909d53/modules/coordinator/README.md); [`CoordinatorProcessor.java`](https://github.com/Atmosphere/atmosphere/blob/5eaac40919357742ac0d67c59840d0b6eb909d53/modules/coordinator/src/main/java/org/atmosphere/coordinator/processor/CoordinatorProcessor.java).
- Basis: structural negative search.
- Confidence: medium-high.
- Caveats: an application can compose an autonomous fleet manager using these surfaces; generic composition capacity is not enough for `C` without a first-party S3-specific decision/feedback path.

### Absence scope

- Surfaces inspected: coordinator/fleet APIs, fleet health/activity/journal, routing/voting/pipeline/fan-out, cancellable executions, retries/circuit breakers, agent limits, delegation/subagent spawning, governance interception and admin/runtime-truth surfaces.
- Plausible first-party paths checked: `@Coordinator` by role/name; `health()` as whole-system view; routing/delegation as allocation; limits/circuit breakers as resource control; cancellation handles as intervention; coordinator journal as accountability.
- Why no material first-party path remains: these surfaces provide visibility, task routing or deterministic enforcement, but no standard autonomous/constructor S3 organ is specialized to a whole-fleet current resource/commitment decision with returned organizational closure.

## S3* — Complementary audit

- State: C
- Function: provide a dedicated result-judgment and corrective-feedback path that can be supplied a suitably independent evaluator before a worker result is accepted as final.
- Disturbance / variety regulated: a worker result may be low-quality or fail deployment-defined acceptance despite ordinary worker self-report, requiring a distinct judgment and another operational attempt.
- Decisive decision or feedback right: judge the worker result against evaluation evidence/rubric, emit pass/fail plus reasons, and on failure feed those reasons into a new worker attempt.
- Decision owner: constructor path. Atmosphere supplies the evaluator contract and closed bounded return/retry machinery, but the standard registered `SanityCheckEvaluator` only inspects result text/metadata and does not establish materially independent complementary access. A deployment must compose an evaluator whose evidence/independence fits the audited claim.
- Supporting / enforcement mechanisms: `ResultEvaluator`, `Evaluation`, ServiceLoader discovery, `AgentFleet.evaluate()`, bounded `refineUntil`, `_refine_feedback`, turn budgets and optional coordinator journaling.
- Closure path: worker result → registered evaluator(s) judge → any failure reasons are aggregated → first-party `refineUntil` injects them into the next worker call → worker retries → passing result or bounded best result becomes terminal.
- Why this is / is not agent-owned: the path is purpose-built for verification judgment plus corrective return rather than generic callbacks. However, default sanity/LLM helpers do not establish sufficiently independent autonomous audit ownership; independence and decisive auditor composition remain downstream, so publication is `C` rather than `A`.
- Evidence: [`AgentFleet.java`](https://github.com/Atmosphere/atmosphere/blob/5eaac40919357742ac0d67c59840d0b6eb909d53/modules/coordinator/src/main/java/org/atmosphere/coordinator/fleet/AgentFleet.java); [`SanityCheckEvaluator.java`](https://github.com/Atmosphere/atmosphere/blob/5eaac40919357742ac0d67c59840d0b6eb909d53/modules/coordinator/src/main/java/org/atmosphere/coordinator/evaluation/SanityCheckEvaluator.java); [`LlmResultEvaluator.java`](https://github.com/Atmosphere/atmosphere/blob/5eaac40919357742ac0d67c59840d0b6eb909d53/modules/coordinator/src/main/java/org/atmosphere/coordinator/evaluation/LlmResultEvaluator.java); [`modules/coordinator/README.md`](https://github.com/Atmosphere/atmosphere/blob/5eaac40919357742ac0d67c59840d0b6eb909d53/modules/coordinator/README.md).
- Basis: structural.
- Confidence: medium-high.
- Caveats: the default ServiceLoader evaluator is `SanityCheckEvaluator`; that helper alone is not claimed as materially independent audit. The `C` credit rests on the dedicated evaluator + feedback/retry constructor that lets an independent evaluator own the missing audit judgment without reimplementing closure.
- Claim being audited: whether a worker agent's result is acceptable under the deployment's evaluation criterion before the result is allowed to terminate the refinement process.
- Ordinary reporting path: worker `AgentResult` returned from the fleet call.
- Complementary access path: deployment-supplied `ResultEvaluator` invoked after worker completion; it can use evidence appropriate to the claim and returns a separate `Evaluation` verdict/reason.
- Independence boundary: first-party default sanity/LLM helpers are insufficient for strong independence; a qualifying deployment must supply a materially independent evaluator through the dedicated SPI.
- Who acts on findings: `refineUntil` deterministically feeds failing reasons back to the worker and controls retry/terminal selection; the evaluator owns the audit judgment in a composed positive realization.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party outside-and-future sensing → adaptation-option → present-capability return loop was established.
- Disturbance / variety regulated: Atmosphere persists conversation/long-term memory, compacts history, routes providers and can enforce policy preferences, but those paths regulate current context/reliability rather than model an external future and install an adaptation.
- Decisive decision or feedback right: interpret external/future change, develop options and select an adaptation that alters present capability.
- Decision owner: not established for S4; application developers/operators define skills, policies, tools, models and harness configuration.
- Supporting / enforcement mechanisms: long-term memory, compaction, planning, coordination journal, governance `Prefer`, provider routing/health, skills/workspace configuration and persistent state.
- Closure path: observations/history may affect later context and operator/developer changes may alter capability, but no shipped S4-specific loop develops prospective adaptation options and returns a selected capability change into standard operation.
- Why this is / is not agent-owned: memory, planning, policy preference and generic learning-like state are explicitly insufficient for S4 without external/prospective option development and return.
- Evidence: [`docs/deep-agent.md`](https://github.com/Atmosphere/atmosphere/blob/5eaac40919357742ac0d67c59840d0b6eb909d53/docs/deep-agent.md); [`docs/governance-policy-plane.md`](https://github.com/Atmosphere/atmosphere/blob/5eaac40919357742ac0d67c59840d0b6eb909d53/docs/governance-policy-plane.md); [`modules/ai/README.md`](https://github.com/Atmosphere/atmosphere/blob/5eaac40919357742ac0d67c59840d0b6eb909d53/modules/ai/README.md).
- Basis: structural negative search.
- Confidence: medium-high.
- Caveats: applications built on Atmosphere can implement prospective adaptation; this assessment does not infer that function from general tools/memory extensibility.

### Absence scope

- Surfaces inspected: long-term memory and compaction, planning/filesystem harness, governance policy plane, preference decisions, provider routing/health, coordinator journal/fork/evaluation, skills/workspace configuration and runtime state.
- Plausible first-party paths checked: long-term memory as learning; planning as S4; provider health/routing as environmental intelligence; governance `Prefer` as adaptation; coordination forks/evaluation as future-option exploration.
- Why no material first-party path remains: inspected paths alter current context, constrain current action, explore task-local alternatives or expose generic extension points; none closes an external-and-prospective capability-adaptation loop.

## S5 — Policy and identity

- State: —
- Function: no first-party identity/ultimate-policy deliberation and closure path was established for the Atmosphere agent organization.
- Disturbance / variety regulated: governance YAML/Rego/Cedar/ACS, scope policies, permissions, approval strategies, budgets and guardrails constrain agent behavior and can admit/deny/transform turns or fleet dispatches.
- Decisive decision or feedback right: resolve an identity/ultimate-policy matter at the chosen recursion and return that authoritative decision as governing policy for subsequent operation.
- Decision owner: not established. Operators/developers author policy artifacts/configuration; runtime machinery parses/enforces them.
- Supporting / enforcement mechanisms: `GovernancePolicy`, policy parsers/registry/rings, admission gates, scope policies, audit sinks, tool approvals/permissions and fleet governance interception.
- Closure path: configured policy → first-party enforcement on requests/tool/fleet edges → subsequent work is constrained. The missing step is an identity-level matter reaching a legitimate ultimate authority whose substantive judgment revises governing policy and returns to operation.
- Why this is / is not agent-owned: a policy plane, policy identity, static policy files and approval gates are constraints/enforcement, not S5 by themselves under Profile 0.2.4.
- Evidence: [`docs/governance-policy-plane.md`](https://github.com/Atmosphere/atmosphere/blob/5eaac40919357742ac0d67c59840d0b6eb909d53/docs/governance-policy-plane.md); [`GovernanceFleetInterceptor.java`](https://github.com/Atmosphere/atmosphere/blob/5eaac40919357742ac0d67c59840d0b6eb909d53/modules/coordinator/src/main/java/org/atmosphere/coordinator/fleet/GovernanceFleetInterceptor.java); [`docs/deep-agent.md`](https://github.com/Atmosphere/atmosphere/blob/5eaac40919357742ac0d67c59840d0b6eb909d53/docs/deep-agent.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: an embedding institution can legitimately own S5 over an Atmosphere deployment, but ordinary policy authoring/approval is not enough to publish `P` without an evidenced identity/ultimate-policy issue-and-return loop.

### Absence scope

- Surfaces inspected: governance policy plane, policy identity/version/audit, scope policies, tool approvals, permissions, budgets, workspace/skill/system-prompt configuration, harness kill switch and coordinator governance.
- Plausible first-party paths checked: operator-authored policy as parent S5; system/skill prompts as identity; governance admin/check endpoint as S5 authority; tool approval as ultimate decision; kill switch as identity closure.
- Why no material first-party path remains: these surfaces define/enforce lower-level constraints and permissions; no genuine identity/constitutional matter → legitimate ultimate authority judgment → returned governing-policy loop was found.

## Recursion, variety, and escalation

Atmosphere can create fleets and isolated ephemeral subagents, but spawning/delegation alone is not VSM recursion. The assessed recursion is the deployed fleet/application: model-driven agents are operational S1 units, while fleet governance/evaluation machinery regulates selected interactions around them.

Operational variety is amplified by tools, remote agents, parallel fan-out, dynamic subagents and multiple providers. It is attenuated by scope/governance interception, recursion/worker budgets, timeouts, circuit breakers, approvals, sandboxing and bounded refinement. These enforcement mechanisms are credited only where a function-specific witness exists; otherwise they remain support rather than inferred S3/S4/S5 ownership.

## Terminal outcome

Proposed canonical vector: `S1=A / S2=C / S3=— / S3*=C / S4=— / S5=—`.

Atmosphere qualifies as an included autonomous harness because the frozen standard distribution closes a first-party model/tool/observation S1 loop. Its strongest metasystem paths are constructor-level: cross-agent governance supplies a disturbance-specific S2 path for goal/scope hijacking, and evaluator-driven bounded refinement supplies an S3* verification/feedback constructor. Coordinator naming, fleet routing, policy enforcement, memory and planning are not promoted to S3/S4/S5 without their missing organizational decision loops.

## Evidence boundaries / caveats

- Pinned to `5eaac40919357742ac0d67c59840d0b6eb909d53`; later upstream changes, including later governance/learning additions, are not imported.
- External model/provider internals do not contribute provider-side VSM functions; Atmosphere receives S1 credit for its own standard first-party agent loop and action/observation closure.
- S2 credit is not based on plurality, delegation, fan-out, pipelines, routing or voting alone; it is based on the explicitly documented agent-to-agent goal-hijack governance path.
- S3* credit is constructor-only. Default sanity/LLM evaluators do not independently establish complementary audit ownership; a qualifying evaluator must be composed into the supplied evaluation/feedback closure.
- Policies, guardrails, HITL approvals, budgets and kill switches are not promoted to S5 merely because they can block consequential work.

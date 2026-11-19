---
harness_id: llmcore
project_name: llmcore
repository: https://github.com/araray/llmcore
review_ref: 1bd7540267a0a6cc26a069bf6211ea4824f20321
reviewed_at: 2026-11-19
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# llmcore

## Review boundary

- System in focus: The installed llmcore Python library with its first-party enhanced single-agent execution mode.
- Purpose and identity: Perform tool-using tasks through provider-neutral cognitive cycles, memory and optional sandbox execution.
- Relevant environment: User goals, tool results, provider failures, workspace/sandbox resources, approval decisions and stored context.
- Standard-distribution boundary: LLMCore.create() → create_enhanced_agent_manager() → EnhancedAgentManager.run(SINGLE), plus documented legacy and optional HITL/sandbox modes. Routing, model-card and runtime APIs are inspected without treating every library subsystem as an autonomous organization.
- Credited operating / distribution surfaces: API factory, enhanced manager, SingleAgentMode, cognitive phases, tool/activity binding, sandbox integration, circuit breaker, memory/persona and approval interfaces.
- Adjacent first-party surfaces excluded from ownership: Repository CI/tests and examples corroborate interfaces but do not supply runtime owners. Remote providers, host applications, injected tools, external memory backends and model-card generation infrastructure cannot donate organizational closure.
- First-party operating / deployment modes considered: Embedded async Python enhanced SINGLE, supported deprecated LEGACY, configured sandbox and HITL. MULTI is exposed as an enum but raises NotImplementedError in manager.run().
- Recursion level: One deployed harness instance; nested execution is not presumed recursively viable.
- Reviewed revision: 1bd7540267a0a6cc26a069bf6211ea4824f20321
- Observation date: 2026-11-19
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

The public API constructs shared provider/memory/storage managers and binds a grimoire-backed prompt/tool catalog into EnhancedAgentManager. SINGLE dispatches to SingleAgentMode and an eight-phase cognitive cycle. The model proposes actions, validation and optional approval constrain execution, activity/tool output is observed, reflection updates the next step, and budgets/convergence bound the loop. Sessions and memory preserve context. Separate provider routing, model-card, generative media and remote-GPU APIs are library services. The Darwin arbiter compares generated candidate contents; it is not credited as a complementary operational auditor.

## Operational model

One goal-directed model/tool cycle is the evidenced S1 unit. Runtime validation, circuit breaking, routing and storage support it. Naming a manager, cognitive phase, persona or provider pool does not establish a whole-system metasystem. Host-composed organizations are outside this library-instance assessment.

## S1 — Operations

- State: A
- Function: Transform user goals into tool actions and a final task result.
- Disturbance / variety regulated: Unknown task state, tool failures and incomplete progress.
- Decisive decision or feedback right: Choose the next action, revise plans from observations, and finish the task.
- Decision owner: The configured model actor within the first-party cognitive cycle.
- Supporting / enforcement mechanisms: Provider/tool managers, grimoire prompts, sandbox execution, sessions, validation and iteration/cost bounds.
- Closure path: run_iteration applies action results and reflection to agent state; run_until_complete repeats until completion or a bound.
- Why this is / is not agent-owned: Removing model choices leaves managers and budgets without a discretionary task solution.
- Evidence: [README.md](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/README.md); [src/llmcore/api.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/api.py); [src/llmcore/agents/manager.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/agents/manager.py); [src/llmcore/agents/single_agent.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/agents/single_agent.py); [src/llmcore/agents/cognitive/phases/cycle.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/agents/cognitive/phases/cycle.py); [src/llmcore/agents/cognitive/phases/act.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/agents/cognitive/phases/act.py)
- Basis: structural
- Confidence: high
- Caveats: Bounded source inspection at the exact revision; no provider-backed runtime experiment or independent secondary semantic review was performed.
- Boundary reachability: The supported public factory passes initialized managers and grimoire to EnhancedAgentManager; run(SINGLE) directly invokes the packaged SingleAgentMode.

## S2 — Coordination

- State: —
- Function: No shipped inter-S1 interference-regulation path at this boundary.
- Disturbance / variety regulated: Potential conflicts among multiple autonomous work units.
- Decisive decision or feedback right: No function-specific decisive organizational right is established in the inspected supported modes.
- Decision owner: No qualifying owner for this function; narrower runtime/developer/operator decisions remain with their actual actors.
- Supporting / enforcement mechanisms: SINGLE/LEGACY dispatch, MULTI enum, sequential phases and generic tool/state interfaces.
- Closure path: No function-specific returned decision changing subsequent regulation is established.
- Why this is / is not agent-owned: MULTI explicitly raises NotImplementedError; phases and candidate alternatives are not distinct interacting operational S1 units.
- Evidence: [README.md](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/README.md); [src/llmcore/api.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/api.py); [src/llmcore/agents/manager.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/agents/manager.py); [src/llmcore/agents/darwin/arbiter.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/agents/darwin/arbiter.py)
- Basis: structural
- Confidence: medium
- Caveats: Bounded source inspection at the exact revision; no provider-backed runtime experiment or independent secondary semantic review was performed.

### Absence scope

- Surfaces inspected: [README.md](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/README.md); [src/llmcore/api.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/api.py); [src/llmcore/agents/manager.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/agents/manager.py); [src/llmcore/agents/darwin/arbiter.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/agents/darwin/arbiter.py); supported-mode documentation and relevant configuration/test wiring.
- Plausible first-party paths checked: MULTI branch, persona switching, phase ordering and Darwin candidate generation.
- Why no material first-party path remains: The inspected manager ships no multi-unit conflict/attenuation/feedback relation; generic host composition is not S2-specific.

## S3 — Inside-and-now control

- State: —
- Function: No established whole-current organizational controller.
- Disturbance / variety regulated: Shared commitments/resources on behalf of the whole.
- Decisive decision or feedback right: No function-specific decisive organizational right is established in the inspected supported modes.
- Decision owner: No qualifying owner for this function; narrower runtime/developer/operator decisions remain with their actual actors.
- Supporting / enforcement mechanisms: Circuit-breaker thresholds, request-level model routing, sandbox limits and remote-runtime spend confirmation.
- Closure path: No function-specific returned decision changing subsequent regulation is established.
- Why this is / is not agent-owned: These mechanisms enforce configured bounds or serve a request; the single-task manager does not own portfolio resource bargaining or current commitments.
- Evidence: [README.md](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/README.md); [src/llmcore/api.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/api.py); [src/llmcore/agents/manager.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/agents/manager.py); [src/llmcore/agents/resilience/circuit_breaker.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/agents/resilience/circuit_breaker.py); [src/llmcore/agents/routing/model_router.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/agents/routing/model_router.py); [src/llmcore/runtimes/manager.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/runtimes/manager.py)
- Basis: structural
- Confidence: medium
- Caveats: Bounded source inspection at the exact revision; no provider-backed runtime experiment or independent secondary semantic review was performed.

### Absence scope

- Surfaces inspected: [README.md](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/README.md); [src/llmcore/api.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/api.py); [src/llmcore/agents/manager.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/agents/manager.py); [src/llmcore/agents/resilience/circuit_breaker.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/agents/resilience/circuit_breaker.py); [src/llmcore/agents/routing/model_router.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/agents/routing/model_router.py); [src/llmcore/runtimes/manager.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/runtimes/manager.py); supported-mode documentation and relevant configuration/test wiring.
- Plausible first-party paths checked: Agent manager, circuit-breaker intervention, provider/model router and GPU runtime manager, including operator confirmation.
- Why no material first-party path remains: Their decisions are task/request/service provisioning or preset enforcement, without a shipped whole-agent-operations current view and regulatory return.

## S3* — Complementary audit

- State: —
- Function: No complementary operational audit path established.
- Disturbance / variety regulated: Mismatch between an operational success claim and independently accessible reality.
- Decisive decision or feedback right: No function-specific decisive organizational right is established in the inspected supported modes.
- Decision owner: No qualifying owner for this function; narrower runtime/developer/operator decisions remain with their actual actors.
- Supporting / enforcement mechanisms: Reflection, candidate arbiter, HITL audit log and execution replay.
- Closure path: No function-specific returned decision changing subsequent regulation is established.
- Why this is / is not agent-owned: The arbiter evaluates supplied candidate content, reflection belongs to the producing cycle, and logs/replay expose records without installing an independent evidence-selecting audit return.
- Evidence: [README.md](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/README.md); [src/llmcore/api.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/api.py); [src/llmcore/agents/manager.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/agents/manager.py); [src/llmcore/agents/darwin/arbiter.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/agents/darwin/arbiter.py); [src/llmcore/agents/cognitive/phases/reflect.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/agents/cognitive/phases/reflect.py); [src/llmcore/agents/observability/replay.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/agents/observability/replay.py); [src/llmcore/agents/hitl/manager.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/agents/hitl/manager.py)
- Basis: structural
- Confidence: medium
- Caveats: Bounded source inspection at the exact revision; no provider-backed runtime experiment or independent secondary semantic review was performed.

### Absence scope

- Surfaces inspected: [README.md](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/README.md); [src/llmcore/api.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/api.py); [src/llmcore/agents/manager.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/agents/manager.py); [src/llmcore/agents/darwin/arbiter.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/agents/darwin/arbiter.py); [src/llmcore/agents/cognitive/phases/reflect.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/agents/cognitive/phases/reflect.py); [src/llmcore/agents/observability/replay.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/agents/observability/replay.py); [src/llmcore/agents/hitl/manager.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/agents/hitl/manager.py); supported-mode documentation and relevant configuration/test wiring.
- Plausible first-party paths checked: Darwin arbiter evaluation inputs, reflection phase, replay and HITL audit records.
- Why no material first-party path remains: These supply routine QA, candidate selection or observability; no supported alternative-primary-evidence auditor/controller loop is supplied.

## S4 — Outside-and-then intelligence

- State: —
- Function: No externally and prospectively closed capability adaptation loop established.
- Disturbance / variety regulated: Changing external capabilities and possible future operating conditions.
- Decisive decision or feedback right: No function-specific decisive organizational right is established in the inspected supported modes.
- Decision owner: No qualifying owner for this function; narrower runtime/developer/operator decisions remain with their actual actors.
- Supporting / enforcement mechanisms: Failure memories, reflection guidance, memory consolidation, model routing/cards and GPU provisioning APIs.
- Closure path: No function-specific returned decision changing subsequent regulation is established.
- Why this is / is not agent-owned: Reflection and learned guidance improve current-task handling; model/service selection and manually refreshed metadata do not themselves develop future adaptation options with a return into current control.
- Evidence: [README.md](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/README.md); [src/llmcore/api.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/api.py); [src/llmcore/agents/manager.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/agents/manager.py); [src/llmcore/agents/learning/reflection_bridge.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/agents/learning/reflection_bridge.py); [src/llmcore/agents/learning/failure_memory.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/agents/learning/failure_memory.py); [src/llmcore/agents/routing/model_router.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/agents/routing/model_router.py); [src/llmcore/runtimes/manager.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/runtimes/manager.py)
- Basis: structural
- Confidence: medium
- Caveats: Bounded source inspection at the exact revision; no provider-backed runtime experiment or independent secondary semantic review was performed.

### Absence scope

- Surfaces inspected: [README.md](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/README.md); [src/llmcore/api.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/api.py); [src/llmcore/agents/manager.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/agents/manager.py); [src/llmcore/agents/learning/reflection_bridge.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/agents/learning/reflection_bridge.py); [src/llmcore/agents/learning/failure_memory.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/agents/learning/failure_memory.py); [src/llmcore/agents/routing/model_router.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/agents/routing/model_router.py); [src/llmcore/runtimes/manager.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/runtimes/manager.py); supported-mode documentation and relevant configuration/test wiring.
- Plausible first-party paths checked: ReflectionBridge, consolidation, failure learning, model router and remote-runtime provisioning.
- Why no material first-party path remains: No supported loop connects prospective environmental distinctions to discretionary reusable capability adaptation; operator/API extensibility alone cannot fill it.

## S5 — Policy and identity

- State: —
- Function: No identity/ultimate-policy issue and returned-authority loop established.
- Disturbance / variety regulated: Disputes over identity or ultimate policy.
- Decisive decision or feedback right: No function-specific decisive organizational right is established in the inspected supported modes.
- Decision owner: No qualifying owner for this function; narrower runtime/developer/operator decisions remain with their actual actors.
- Supporting / enforcement mechanisms: Grimoire prompt/persona configuration, HITL scopes and sandbox security policies.
- Closure path: No function-specific returned decision changing subsequent regulation is established.
- Why this is / is not agent-owned: Ordinary action authorization and configurable persona constraints govern tool use without an identity-level escalation/decision/return procedure.
- Evidence: [README.md](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/README.md); [src/llmcore/api.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/api.py); [src/llmcore/agents/manager.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/agents/manager.py); [src/llmcore/agents/persona/manager.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/agents/persona/manager.py); [src/llmcore/agents/hitl/manager.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/agents/hitl/manager.py); [src/llmcore/agents/grimoire_tool_catalog.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/agents/grimoire_tool_catalog.py)
- Basis: structural
- Confidence: medium
- Caveats: Bounded source inspection at the exact revision; no provider-backed runtime experiment or independent secondary semantic review was performed.

### Absence scope

- Surfaces inspected: [README.md](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/README.md); [src/llmcore/api.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/api.py); [src/llmcore/agents/manager.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/agents/manager.py); [src/llmcore/agents/persona/manager.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/agents/persona/manager.py); [src/llmcore/agents/hitl/manager.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/agents/hitl/manager.py); [src/llmcore/agents/grimoire_tool_catalog.py](https://github.com/araray/llmcore/blob/1bd7540267a0a6cc26a069bf6211ea4824f20321/src/llmcore/agents/grimoire_tool_catalog.py); supported-mode documentation and relevant configuration/test wiring.
- Plausible first-party paths checked: Prompt/tool catalog binding, persona management, HITL approval callbacks and policy enforcement.
- Why no material first-party path remains: Supported approval paths decide actions/scopes; neither static prompts nor host configuration establish runtime ultimate-policy closure.

## Distributed OSS parent arrangement

Repository maintenance and contributor approvals are outside the deployed product recursion. Multiple contributors do not establish organization-level parent governance in the assessed harness.

## Self-hosted and non-human modes

Self-hosting and provider choice are supported. Operator configuration or ordinary tool approval alone does not establish a parent-governed S3/S4/S5 mode.

## Recursion

No claim of recursively complete VSM units is made. Execution phases, provider instances and nested calls do not establish recursive viability.

## Variety and escalation

Tool/environment feedback is transduced into cognitive state; approval pauses and circuit breakers bound local activity. Resource limits, failure memories and persona constraints retain narrower roles. No exceptional authority channel or S3–S4–S5 homeostat is inferred.

## Evidence gaps

Source tracing, not a live model/sandbox execution or independent secondary audit. The broad provider/media catalog is not individually exercised. The assessment resolves the supported enhanced/legacy agent boundary and inspects plausible metasystem surfaces; future MULTI implementation or host-authored controllers may change it.

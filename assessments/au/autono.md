---
harness_id: autono
project_name: Autono
repository: https://github.com/vortezwohl/Autono
review_ref: ebc66d3d9cd5c2a802af8b531af67a1b70c56a63
reviewed_at: 2026-10-27
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

# Autono

## Review boundary

- System in focus: The first-party Autono Python agent runtime, synchronous Agent and asynchronous MCP-backed McpAgent, including nested agentic abilities.
- Purpose and identity: Complete a supplied request through adaptive model-selected abilities with memory and bounded abandonment support.
- Relevant environment: Developer-supplied functions, MCP tools, model responses, local results/errors and optional nested task agents.
- Standard-distribution boundary: Exported autono package and its documented standard Agent/McpAgent modes at the frozen source. Developer-created tools supply task-specific environment access, while the loop is shipped first-party.
- Credited operating / distribution surfaces: [autono/__init__.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/autono/__init__.py); [autono/brain/agent.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/autono/brain/agent.py); [autono/brain/mcp_agent.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/autono/brain/mcp_agent.py); [autono/prompt/next_move_prompt.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/autono/prompt/next_move_prompt.py); [autono/prompt/executor_prompt.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/autono/prompt/executor_prompt.py); [autono/ability/agentic_ability.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/autono/ability/agentic_ability.py)
- Adjacent first-party surfaces excluded from ownership: demo/ illustrates packaged constructors but its live browser/MCP servers and particular calculator/write-file roles are not a deployed organization credited by default. README benchmark numbers, external experiment repository and paper are not independent operational audit or capability evidence for this assessment.
- First-party operating / deployment modes considered: Synchronous function abilities, MCP async tools, nested @agentic delegation with memory transfer, configurable personality/penalty and optional before/after hooks. No bespoke supervisor, auditor or governance implementation is assumed.
- Recursion level: One request-solving agent/call tree at application-runtime recursion.
- Reviewed revision: `ebc66d3d9cd5c2a802af8b531af67a1b70c56a63`
- Observation date: 2026-10-27
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

BaseAgent registers abilities, resolves a request, builds self-introduction and can generate a plan. Agent.just_do_it estimates step count and repeatedly invokes NextMovePrompt over request, available abilities and action memory. The chosen ability/arguments execute through ExecutorPrompt; the result is summarized and memorized before the next decision. AgenticAbility relays request and a copy of prior memory to another Agent and returns its response. McpAgent follows an asynchronous variant using discovered MCP tools. Before/AfterActionTaken hooks can replace next-action or result messages but are generic callbacks. A developer-set probability/penalty/personality controls stochastic abandonment after excess steps; the model still owns task-specific choice. Final introspection summarizes task progress from the same history, then runtime state is reset. No persistent whole-team scheduler, separate audit authority or policy-return service is shipped.

## Operational model

One or more instantiated agents choose task actions using their granted abilities. A caller can synchronously delegate to another agent as an ability and use its result in later action selection. Developers choose the ability set, model and termination parameters; the runtime enforces/executes those choices rather than inheriting organizational control rights.

## S1 — Operations

- State: A
- Function: Produce request-solving outcomes through first-party model/ability feedback iteration.
- Disturbance / variety regulated: Changing intermediate results, incomplete requests, unavailable capabilities and task-specific action arguments.
- Decisive decision or feedback right: Choose the next available ability/arguments or task-complete/failure response using current request/history.
- Decision owner: The model-backed Agent or McpAgent.
- Supporting / enforcement mechanisms: Ability registration, JSON/format parsing, ExecutorPrompt tool invocation, action memory, MCP transport and stochastic termination enforcement.
- Closure path: NextMovePrompt selects action → execute callable/MCP tool → summarize and memorize returned result → next choice; terminal choice/abandonment returns AllDoneMessage.
- Why this is / is not agent-owned: Removing the model preserves tools and enforcement but removes task-specific action selection. The developer supplies task abilities without needing to implement the autonomous loop.
- Evidence: [autono/__init__.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/autono/__init__.py); [autono/brain/agent.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/autono/brain/agent.py); [autono/brain/mcp_agent.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/autono/brain/mcp_agent.py); [autono/prompt/next_move_prompt.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/autono/prompt/next_move_prompt.py); [autono/prompt/executor_prompt.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/autono/prompt/executor_prompt.py); [README.md](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/README.md)
- Basis: structural
- Confidence: high within the declared source boundary
- Caveats: A is structural runtime ownership, not a claim of robust task performance or guaranteed completion; constructor/introduction/model calls were not executed here.
- Boundary reachability: Autono exports Agent/McpAgent and first-party ability/delegation constructors; README's instantiate→assign→just_do_it path directly enters the shipped loop.

## S2 — Coordination

- State: —
- Function: No specific inter-S1 conflict-regulation path established beyond delegation and memory transfer.
- Disturbance / variety regulated: A call tree may contain multiple task agents; historical progress can inform later steps.
- Decisive decision or feedback right: No qualifying first-party decisive right established for this function.
- Decision owner: No qualifying owner at the declared boundary.
- Supporting / enforcement mechanisms: The cited runtime and documentation are supporting surfaces, not decision owners.
- Closure path: No function-specific returned closure at this boundary.
- Why this is / is not agent-owned: Nested ability calls, copied memory, chronological progress reasoning and division of labour do not identify a concrete interaction conflict plus a coordination discretion/return path.
- Evidence: [autono/ability/agentic_ability.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/autono/ability/agentic_ability.py); [autono/ability/mcp_agentic_ability.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/autono/ability/mcp_agentic_ability.py); [autono/brain/memory_augment.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/autono/brain/memory_augment.py); [autono/prompt/next_move_prompt.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/autono/prompt/next_move_prompt.py); [demo/multi_agent.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/demo/multi_agent.py)
- Basis: structural
- Confidence: high within the declared source boundary
- Caveats: Static source evidence; no live model/provider run or empirical viability claim.

### Absence scope

- Surfaces inspected: [autono/ability/agentic_ability.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/autono/ability/agentic_ability.py); [autono/ability/mcp_agentic_ability.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/autono/ability/mcp_agentic_ability.py); [autono/brain/memory_augment.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/autono/brain/memory_augment.py); [autono/prompt/next_move_prompt.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/autono/prompt/next_move_prompt.py); [demo/multi_agent.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/demo/multi_agent.py)
- Plausible first-party paths checked: Nested-agent request/history relay, copy-on-access memory, synchronous return, example specialist agents and next-move progress reasoning.
- Why no material first-party path remains: The package supplies task delegation and generic shared context, with no material reservation/conflict/oscillation-specific relation or agent-owned conflict adjustment. Hypothetically composing one from hooks is not S2=C.

## S3 — Inside-and-now control

- State: —
- Function: No whole-current organizational control loop in the shipped runtime.
- Disturbance / variety regulated: Excess steps and unsuitable abilities can waste a task's effort.
- Decisive decision or feedback right: No qualifying first-party decisive right established for this function.
- Decision owner: No qualifying owner at the declared boundary.
- Supporting / enforcement mechanisms: The cited runtime and documentation are supporting surfaces, not decision owners.
- Closure path: No function-specific returned closure at this boundary.
- Why this is / is not agent-owned: Probabilistic stopping, expected-step estimation, personality and grant/deprive APIs constrain local execution; they do not assign a whole-system resource/commitment decision owner.
- Evidence: [autono/brain/agent.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/autono/brain/agent.py); [autono/brain/base_agent.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/autono/brain/base_agent.py); [autono/brain/mcp_agent.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/autono/brain/mcp_agent.py); [autono/brain/hook/before_action_taken.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/autono/brain/hook/before_action_taken.py); [README.md](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/README.md)
- Basis: structural
- Confidence: high within the declared source boundary
- Caveats: Static source evidence; no live model/provider run or empirical viability claim.

### Absence scope

- Surfaces inspected: [autono/brain/agent.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/autono/brain/agent.py); [autono/brain/base_agent.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/autono/brain/base_agent.py); [autono/brain/mcp_agent.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/autono/brain/mcp_agent.py); [autono/brain/hook/before_action_taken.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/autono/brain/hook/before_action_taken.py); [README.md](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/README.md)
- Plausible first-party paths checked: estimate_step/stop/penalize/set_penalty/change_personality, tool grants/removals, child delegation and hook intervention including parent callbacks.
- Why no material first-party path remains: Termination sampling enforces developer settings and delegation serves the current task. Generic callbacks expose no first-party whole-team view, supervisory decision and returned control. Operator configuration alone is not S3=P.

## S3* — Complementary audit

- State: —
- Function: No complementary independent audit of agent success claims.
- Disturbance / variety regulated: The model's own summaries may omit or misread operational facts.
- Decisive decision or feedback right: No qualifying first-party decisive right established for this function.
- Decision owner: No qualifying owner at the declared boundary.
- Supporting / enforcement mechanisms: The cited runtime and documentation are supporting surfaces, not decision owners.
- Closure path: No function-specific returned closure at this boundary.
- Why this is / is not agent-owned: Executor summaries and final introspection use the acting model/history; observability hooks are developer callbacks, not an independent audit-specific access/judgment/control path.
- Evidence: [autono/prompt/executor_prompt.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/autono/prompt/executor_prompt.py); [autono/prompt/introspection_prompt.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/autono/prompt/introspection_prompt.py); [autono/brain/hook/base_hook.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/autono/brain/hook/base_hook.py); [autono/brain/hook/after_action_taken.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/autono/brain/hook/after_action_taken.py); [demo/multi_agent.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/demo/multi_agent.py); [README.md](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/README.md)
- Basis: structural
- Confidence: high within the declared source boundary
- Caveats: Static source evidence; no live model/provider run or empirical viability claim.

### Absence scope

- Surfaces inspected: [autono/prompt/executor_prompt.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/autono/prompt/executor_prompt.py); [autono/prompt/introspection_prompt.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/autono/prompt/introspection_prompt.py); [autono/brain/hook/base_hook.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/autono/brain/hook/base_hook.py); [autono/brain/hook/after_action_taken.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/autono/brain/hook/after_action_taken.py); [demo/multi_agent.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/demo/multi_agent.py); [README.md](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/README.md)
- Plausible first-party paths checked: Action/result hooks, introspection, raw returned action fields, demo printing and external benchmark links.
- Why no material first-party path remains: No shipped complementary auditor, separately controlled raw-evidence check or returned corrective authority is wired. Logging/benchmarks and extensible hook signatures cannot supply the missing function by themselves.

## S4 — Outside-and-then intelligence

- State: —
- Function: No external-and-prospective capability adaptation loop.
- Disturbance / variety regulated: Requests and external tool results vary; model/tool selection may be customized.
- Decisive decision or feedback right: No qualifying first-party decisive right established for this function.
- Decision owner: No qualifying owner at the declared boundary.
- Supporting / enforcement mechanisms: The cited runtime and documentation are supporting surfaces, not decision owners.
- Closure path: No function-specific returned closure at this boundary.
- Why this is / is not agent-owned: Dynamic next actions, planning, memory transfer and self-introduction solve the current request. They do not develop future-environment options and couple them to present capability regulation.
- Evidence: [autono/prompt/scheduler_prompt.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/autono/prompt/scheduler_prompt.py); [autono/prompt/next_move_prompt.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/autono/prompt/next_move_prompt.py); [autono/brain/memory_augment.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/autono/brain/memory_augment.py); [autono/brain/base_agent.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/autono/brain/base_agent.py); [README.md](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/README.md)
- Basis: structural
- Confidence: high within the declared source boundary
- Caveats: Static source evidence; no live model/provider run or empirical viability claim.

### Absence scope

- Surfaces inspected: [autono/prompt/scheduler_prompt.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/autono/prompt/scheduler_prompt.py); [autono/prompt/next_move_prompt.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/autono/prompt/next_move_prompt.py); [autono/brain/memory_augment.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/autono/brain/memory_augment.py); [autono/brain/base_agent.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/autono/brain/base_agent.py); [README.md](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/README.md)
- Plausible first-party paths checked: Task planning, capability introspection, MCP discovery, model factories, personality changes and history relay.
- Why no material first-party path remains: The standard package has no prospective option-development/selection loop with a current-control return; developer extension and adaptive local action choice do not establish A/C/P for S4.

## S5 — Policy and identity

- State: —
- Function: No identity/ultimate-policy decision-and-return path.
- Disturbance / variety regulated: Agent names, abilities, personalities and hook rules bound operation.
- Decisive decision or feedback right: No qualifying first-party decisive right established for this function.
- Decision owner: No qualifying owner at the declared boundary.
- Supporting / enforcement mechanisms: The cited runtime and documentation are supporting surfaces, not decision owners.
- Closure path: No function-specific returned closure at this boundary.
- Why this is / is not agent-owned: Generated self-introduction describes the assigned ability set; it does not decide legitimate system identity or resolve ultimate policy.
- Evidence: [autono/brain/base_agent.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/autono/brain/base_agent.py); [autono/prompt/self_introduce.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/autono/prompt/self_introduce.py); [autono/enum/Personality.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/autono/enum/Personality.py); [autono/brain/hook/base_hook.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/autono/brain/hook/base_hook.py); [README.md](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/README.md)
- Basis: structural
- Confidence: high within the declared source boundary
- Caveats: Static source evidence; no live model/provider run or empirical viability claim.

### Absence scope

- Surfaces inspected: [autono/brain/base_agent.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/autono/brain/base_agent.py); [autono/prompt/self_introduce.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/autono/prompt/self_introduce.py); [autono/enum/Personality.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/autono/enum/Personality.py); [autono/brain/hook/base_hook.py](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/autono/brain/hook/base_hook.py); [README.md](https://github.com/vortezwohl/Autono/blob/ebc66d3d9cd5c2a802af8b531af67a1b70c56a63/README.md)
- Plausible first-party paths checked: Self-introduction, names, developer ability grant/deprive, personalities, user requests and generic before/after intervention.
- Why no material first-party path remains: No identity-policy issue reaches legitimate ultimate authority and returns as a binding decision governing later operation. A configurable personality, prompt or callback is not that closure.

## Distributed OSS parent arrangement

Developers/operators configure model, abilities and hooks locally. Neither those controls nor multiple OSS contributors establish a function-specific project-wide or local returned parent S3/S4/S5 mode.

## Self-hosted and non-human modes

Agent and MCP deployments can be self-hosted and nested, but custom audit/governance hooks remain composition outside the shipped function boundary. No non-human viable organization is inferred from multiple agents.

## Recursion

Nested agentic abilities preserve request/history and return results; they demonstrate delegation, not a complete recursive viable system with its own metasystem.

## Variety and escalation

Formatted-response retries can raise TooDumbException; excess-step stochastic stopping returns an introspective result. These are bounded local error/termination paths, not automatically algedonic channels or S3 control.

## Evidence gaps

Static frozen-source inspection only. Python compileall passed for the package; no packaged native test suite was found. Provider/MCP dependencies and live model/browser demos were not executed. Public README performance claims were not independently reproduced or borrowed into the vector. No guarantee of successful termination, task quality or whole-system viability is claimed. GPL-3.0 LICENSE is present.

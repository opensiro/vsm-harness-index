---
harness_id: grapes
project_name: grapes
repository: https://github.com/im6ix/grapes
review_ref: ce0c56414827fb10d395a2f2d4176e8da2a29b49
reviewed_at: 2026-11-01
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

# grapes

## Review boundary

- System in focus: the shipped grapes Python plugin runtime and its bundled interactive tool-using Chat agent.
- Purpose and identity: compose reversible plugins and answer user requests by autonomous model/tool iteration.
- Relevant environment: user prompts, registered tools, plugin/service availability, provider errors and local JSONL session storage.
- Standard-distribution boundary: main.py and importable grapes runtime with bundled Llm/model adapter, calculator and file-search plugins; external provider and adopter-written plugins remain dependencies or adjacent compositions.
- Credited operating / distribution surfaces: main.py, grapes/agent, Context, Harness, Registry/Fiber/Reflect, events and bundled tools.
- Adjacent first-party surfaces excluded from ownership: tests and documentation examples are corroboration; repository CI/contributor work is outside the running agent boundary.
- First-party operating / deployment modes considered: bundled interactive chat with session new/resume; library composition through Context.mount; no shipped multi-agent or parent-governed organizational mode found.
- Recursion level: one deployed harness instance; child execution is not presumed recursively viable.
- Reviewed revision: `ce0c56414827fb10d395a2f2d4176e8da2a29b49`.
- Observation date: 2026-11-01.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7 (Index active release; Skills main 0.3.8 inspected but not silently activated).

## Repository architecture

main.py mounts the calculator, Llm service and API model adapter, then creates a durable Chat. run_agent repeatedly calls the model with available tool schemas, dispatches the chosen tool, appends results/errors and returns a final answer within a step cap. Context tracks reversible effects; Registry creates a Fiber per mounted plugin. Provider-ticket changes unload/reload dependent fibers, with one transition at a time and teardown against the committed dependency snapshot. Reflect is service-provider selection, not model reflection. Chat appends new messages to JSONL sessions. Generic plugin lifecycle, dependency reactivity and event subscription are not by themselves VSM metasystem functions.

## Operational model

One autonomous conversational/tool work cell is established. Its model chooses actions; Context executes them and appends observations. Plugin fibers provide services/tools, not independently purposeful S1 units. No separate organization of autonomous operational units is supplied by the bundled setup.

## S1 — Operations

- State: A
- Function: tool-assisted user-request transformation.
- Disturbance / variety regulated: varying user questions and tool failures.
- Decisive decision or feedback right: select tool name/arguments or final answer, and revise the next step after returned observation.
- Decision owner: the model-backed Chat agent.
- Supporting / enforcement mechanisms: run_agent, Context.call_tool and schema registry, provider adapter and session append.
- Closure path: tool/error messages re-enter the next model completion; answer and messages persist through Chat.
- Boundary reachability: main.py mounts bundled runtime/model/tool plugins and calls Chat.ask, which directly invokes the first-party run_agent loop.
- Why this is / is not agent-owned: without model discretion, the runtime exposes tools but does not choose the request transformation.
- Evidence: [main.py](https://github.com/im6ix/grapes/blob/ce0c56414827fb10d395a2f2d4176e8da2a29b49/main.py); [grapes/agent/chat.py](https://github.com/im6ix/grapes/blob/ce0c56414827fb10d395a2f2d4176e8da2a29b49/grapes/agent/chat.py); [grapes/agent/loop.py](https://github.com/im6ix/grapes/blob/ce0c56414827fb10d395a2f2d4176e8da2a29b49/grapes/agent/loop.py); [grapes/context.py](https://github.com/im6ix/grapes/blob/ce0c56414827fb10d395a2f2d4176e8da2a29b49/grapes/context.py).
- Basis: structural.
- Confidence: high.
- Caveats: small experimental runtime; no outcome-quality or provider-availability claim.

## S2 — Coordination

- State: —
- Function: no evidenced inter-S1 coordination loop.
- Disturbance / variety regulated: the function-specific disturbance described below is not regulated by a shipped organizational loop.
- Decisive decision or feedback right: no function-specific decisive organizational right established.
- Decision owner: not established; runtime mechanisms retain their narrower implementation role.
- Supporting / enforcement mechanisms: the inspected task, lifecycle or configuration mechanisms below.
- Closure path: no function-specific returned decision into subsequent regulation established.
- Why this is / is not agent-owned: Fibers are plugin/service lifecycles, not distinct autonomous operational cells with a concrete inter-S1 disturbance. Provider-ticket consistency prevents implementation re-entry; it is not first-party inter-S1 regulation.
- Evidence: [grapes/harness.py](https://github.com/im6ix/grapes/blob/ce0c56414827fb10d395a2f2d4176e8da2a29b49/grapes/harness.py); [grapes/registry.py](https://github.com/im6ix/grapes/blob/ce0c56414827fb10d395a2f2d4176e8da2a29b49/grapes/registry.py); [grapes/fiber.py](https://github.com/im6ix/grapes/blob/ce0c56414827fb10d395a2f2d4176e8da2a29b49/grapes/fiber.py); [grapes/reflect.py](https://github.com/im6ix/grapes/blob/ce0c56414827fb10d395a2f2d4176e8da2a29b49/grapes/reflect.py); [main.py](https://github.com/im6ix/grapes/blob/ce0c56414827fb10d395a2f2d4176e8da2a29b49/main.py).
- Basis: structural.
- Confidence: medium.
- Caveats: Bounded to the pinned supported distribution; hypothetical downstream extensions are not assessed.

### Absence scope

- Surfaces inspected: [grapes/harness.py](https://github.com/im6ix/grapes/blob/ce0c56414827fb10d395a2f2d4176e8da2a29b49/grapes/harness.py); [grapes/registry.py](https://github.com/im6ix/grapes/blob/ce0c56414827fb10d395a2f2d4176e8da2a29b49/grapes/registry.py); [grapes/fiber.py](https://github.com/im6ix/grapes/blob/ce0c56414827fb10d395a2f2d4176e8da2a29b49/grapes/fiber.py); [grapes/reflect.py](https://github.com/im6ix/grapes/blob/ce0c56414827fb10d395a2f2d4176e8da2a29b49/grapes/reflect.py); [main.py](https://github.com/im6ix/grapes/blob/ce0c56414827fb10d395a2f2d4176e8da2a29b49/main.py); main.py, grapes/agent, Context, Harness, Registry/Fiber/Reflect, events and bundled tools..
- Plausible first-party paths checked: plugin load/unload serialization, provider replacement/re-entrancy guards and generic events were tested as possible S2 paths.
- Why no material first-party path remains: Fibers are plugin/service lifecycles, not distinct autonomous operational cells with a concrete inter-S1 disturbance. Provider-ticket consistency prevents implementation re-entry; it is not first-party inter-S1 regulation.

## S3 — Inside-and-now control

- State: —
- Function: no whole-current organizational control loop.
- Disturbance / variety regulated: the function-specific disturbance described below is not regulated by a shipped organizational loop.
- Decisive decision or feedback right: no function-specific decisive organizational right established.
- Decision owner: not established; runtime mechanisms retain their narrower implementation role.
- Supporting / enforcement mechanisms: the inspected task, lifecycle or configuration mechanisms below.
- Closure path: no function-specific returned decision into subsequent regulation established.
- Why this is / is not agent-owned: The step cap and lifecycle wait enforce task/runtime bounds. No whole-system current view with substantive resource/commitment judgment and returned control over operations is supplied.
- Evidence: [grapes/agent/loop.py](https://github.com/im6ix/grapes/blob/ce0c56414827fb10d395a2f2d4176e8da2a29b49/grapes/agent/loop.py); [grapes/harness.py](https://github.com/im6ix/grapes/blob/ce0c56414827fb10d395a2f2d4176e8da2a29b49/grapes/harness.py); [grapes/registry.py](https://github.com/im6ix/grapes/blob/ce0c56414827fb10d395a2f2d4176e8da2a29b49/grapes/registry.py); [main.py](https://github.com/im6ix/grapes/blob/ce0c56414827fb10d395a2f2d4176e8da2a29b49/main.py).
- Basis: structural.
- Confidence: medium.
- Caveats: Bounded to the pinned supported distribution; hypothetical downstream extensions are not assessed.

### Absence scope

- Surfaces inspected: [grapes/agent/loop.py](https://github.com/im6ix/grapes/blob/ce0c56414827fb10d395a2f2d4176e8da2a29b49/grapes/agent/loop.py); [grapes/harness.py](https://github.com/im6ix/grapes/blob/ce0c56414827fb10d395a2f2d4176e8da2a29b49/grapes/harness.py); [grapes/registry.py](https://github.com/im6ix/grapes/blob/ce0c56414827fb10d395a2f2d4176e8da2a29b49/grapes/registry.py); [main.py](https://github.com/im6ix/grapes/blob/ce0c56414827fb10d395a2f2d4176e8da2a29b49/main.py); main.py, grapes/agent, Context, Harness, Registry/Fiber/Reflect, events and bundled tools..
- Plausible first-party paths checked: step bound, wait_until_idle, mount/dispose, model adapter selection and human session commands, including possible parent-mode controls.
- Why no material first-party path remains: The step cap and lifecycle wait enforce task/runtime bounds. No whole-system current view with substantive resource/commitment judgment and returned control over operations is supplied.

## S3* — Complementary audit

- State: —
- Function: no complementary independent audit path.
- Disturbance / variety regulated: the function-specific disturbance described below is not regulated by a shipped organizational loop.
- Decisive decision or feedback right: no function-specific decisive organizational right established.
- Decision owner: not established; runtime mechanisms retain their narrower implementation role.
- Supporting / enforcement mechanisms: the inspected task, lifecycle or configuration mechanisms below.
- Closure path: no function-specific returned decision into subsequent regulation established.
- Why this is / is not agent-owned: These are ordinary task observations, persistence and developer tests. No separate auditor obtains complementary raw reality and returns challenge findings into operational control.
- Evidence: [grapes/agent/loop.py](https://github.com/im6ix/grapes/blob/ce0c56414827fb10d395a2f2d4176e8da2a29b49/grapes/agent/loop.py); [grapes/agent/chat.py](https://github.com/im6ix/grapes/blob/ce0c56414827fb10d395a2f2d4176e8da2a29b49/grapes/agent/chat.py); [grapes/logger.py](https://github.com/im6ix/grapes/blob/ce0c56414827fb10d395a2f2d4176e8da2a29b49/grapes/logger.py); [grapes/agent/session.py](https://github.com/im6ix/grapes/blob/ce0c56414827fb10d395a2f2d4176e8da2a29b49/grapes/agent/session.py); [README.md](https://github.com/im6ix/grapes/blob/ce0c56414827fb10d395a2f2d4176e8da2a29b49/README.md).
- Basis: structural.
- Confidence: medium.
- Caveats: Bounded to the pinned supported distribution; hypothetical downstream extensions are not assessed.

### Absence scope

- Surfaces inspected: [grapes/agent/loop.py](https://github.com/im6ix/grapes/blob/ce0c56414827fb10d395a2f2d4176e8da2a29b49/grapes/agent/loop.py); [grapes/agent/chat.py](https://github.com/im6ix/grapes/blob/ce0c56414827fb10d395a2f2d4176e8da2a29b49/grapes/agent/chat.py); [grapes/logger.py](https://github.com/im6ix/grapes/blob/ce0c56414827fb10d395a2f2d4176e8da2a29b49/grapes/logger.py); [grapes/agent/session.py](https://github.com/im6ix/grapes/blob/ce0c56414827fb10d395a2f2d4176e8da2a29b49/grapes/agent/session.py); [README.md](https://github.com/im6ix/grapes/blob/ce0c56414827fb10d395a2f2d4176e8da2a29b49/README.md); main.py, grapes/agent, Context, Harness, Registry/Fiber/Reflect, events and bundled tools..
- Plausible first-party paths checked: tool exceptions, logs, persisted transcripts, ordinary test suite and bundled plugin surfaces.
- Why no material first-party path remains: These are ordinary task observations, persistence and developer tests. No separate auditor obtains complementary raw reality and returns challenge findings into operational control.

## S4 — Outside-and-then intelligence

- State: —
- Function: no externally prospective capability-adaptation closure.
- Disturbance / variety regulated: the function-specific disturbance described below is not regulated by a shipped organizational loop.
- Decisive decision or feedback right: no function-specific decisive organizational right established.
- Decision owner: not established; runtime mechanisms retain their narrower implementation role.
- Supporting / enforcement mechanisms: the inspected task, lifecycle or configuration mechanisms below.
- Closure path: no function-specific returned decision into subsequent regulation established.
- Why this is / is not agent-owned: Provider replacement reacts to currently mounted services; it does not sense a future environment, develop adaptation options and return a decisive capability change. Persistence and generic mounting remain implementation mechanisms.
- Evidence: [grapes/reflect.py](https://github.com/im6ix/grapes/blob/ce0c56414827fb10d395a2f2d4176e8da2a29b49/grapes/reflect.py); [grapes/fiber.py](https://github.com/im6ix/grapes/blob/ce0c56414827fb10d395a2f2d4176e8da2a29b49/grapes/fiber.py); [grapes/agent/model.py](https://github.com/im6ix/grapes/blob/ce0c56414827fb10d395a2f2d4176e8da2a29b49/grapes/agent/model.py); [grapes/agent/session.py](https://github.com/im6ix/grapes/blob/ce0c56414827fb10d395a2f2d4176e8da2a29b49/grapes/agent/session.py); [main.py](https://github.com/im6ix/grapes/blob/ce0c56414827fb10d395a2f2d4176e8da2a29b49/main.py).
- Basis: structural.
- Confidence: medium.
- Caveats: Bounded to the pinned supported distribution; hypothetical downstream extensions are not assessed.

### Absence scope

- Surfaces inspected: [grapes/reflect.py](https://github.com/im6ix/grapes/blob/ce0c56414827fb10d395a2f2d4176e8da2a29b49/grapes/reflect.py); [grapes/fiber.py](https://github.com/im6ix/grapes/blob/ce0c56414827fb10d395a2f2d4176e8da2a29b49/grapes/fiber.py); [grapes/agent/model.py](https://github.com/im6ix/grapes/blob/ce0c56414827fb10d395a2f2d4176e8da2a29b49/grapes/agent/model.py); [grapes/agent/session.py](https://github.com/im6ix/grapes/blob/ce0c56414827fb10d395a2f2d4176e8da2a29b49/grapes/agent/session.py); [main.py](https://github.com/im6ix/grapes/blob/ce0c56414827fb10d395a2f2d4176e8da2a29b49/main.py); main.py, grapes/agent, Context, Harness, Registry/Fiber/Reflect, events and bundled tools..
- Plausible first-party paths checked: reactive provider changes, dependency remounting, persistent chat and operator/library plugin installation; positive and parent adaptation modes considered.
- Why no material first-party path remains: Provider replacement reacts to currently mounted services; it does not sense a future environment, develop adaptation options and return a decisive capability change. Persistence and generic mounting remain implementation mechanisms.

## S5 — Policy and identity

- State: —
- Function: no ultimate-policy/identity decision-return loop.
- Disturbance / variety regulated: the function-specific disturbance described below is not regulated by a shipped organizational loop.
- Decisive decision or feedback right: no function-specific decisive organizational right established.
- Decision owner: not established; runtime mechanisms retain their narrower implementation role.
- Supporting / enforcement mechanisms: the inspected task, lifecycle or configuration mechanisms below.
- Closure path: no function-specific returned decision into subsequent regulation established.
- Why this is / is not agent-owned: Operator parameters and ordinary user requests define task conditions. No identity-level issue, legitimate ultimate decision authority and authoritative return into runtime policy are wired.
- Evidence: [main.py](https://github.com/im6ix/grapes/blob/ce0c56414827fb10d395a2f2d4176e8da2a29b49/main.py); [grapes/context.py](https://github.com/im6ix/grapes/blob/ce0c56414827fb10d395a2f2d4176e8da2a29b49/grapes/context.py); [grapes/agent/loop.py](https://github.com/im6ix/grapes/blob/ce0c56414827fb10d395a2f2d4176e8da2a29b49/grapes/agent/loop.py); [grapes/agent/model.py](https://github.com/im6ix/grapes/blob/ce0c56414827fb10d395a2f2d4176e8da2a29b49/grapes/agent/model.py); [README.md](https://github.com/im6ix/grapes/blob/ce0c56414827fb10d395a2f2d4176e8da2a29b49/README.md).
- Basis: structural.
- Confidence: medium.
- Caveats: Bounded to the pinned supported distribution; hypothetical downstream extensions are not assessed.

### Absence scope

- Surfaces inspected: [main.py](https://github.com/im6ix/grapes/blob/ce0c56414827fb10d395a2f2d4176e8da2a29b49/main.py); [grapes/context.py](https://github.com/im6ix/grapes/blob/ce0c56414827fb10d395a2f2d4176e8da2a29b49/grapes/context.py); [grapes/agent/loop.py](https://github.com/im6ix/grapes/blob/ce0c56414827fb10d395a2f2d4176e8da2a29b49/grapes/agent/loop.py); [grapes/agent/model.py](https://github.com/im6ix/grapes/blob/ce0c56414827fb10d395a2f2d4176e8da2a29b49/grapes/agent/model.py); [README.md](https://github.com/im6ix/grapes/blob/ce0c56414827fb10d395a2f2d4176e8da2a29b49/README.md); main.py, grapes/agent, Context, Harness, Registry/Fiber/Reflect, events and bundled tools..
- Plausible first-party paths checked: user prompts, model defaults, max_steps and plugin configuration plus session reset/resume and maintainer governance.
- Why no material first-party path remains: Operator parameters and ordinary user requests define task conditions. No identity-level issue, legitimate ultimate decision authority and authoritative return into runtime policy are wired.

## Distributed OSS parent arrangement

MIT licensing and contributor/maintainer activity establish distribution provenance, not project-level S3/S4/S5 parent closure. This assessment concerns the deployed product boundary; no organization-level parent mode is inferred from local maintainer decisions.

## Self-hosted and non-human modes

Local chat operators choose credentials/plugins and sessions. None of these controls establishes a function-specific S3/S4/S5 parent loop. Adopter-authored plugins could expand the system but are outside the frozen shipped boundary.

## Recursion

Nested execution and delegated tasks do not establish recursive viable systems; no child full metasystem is claimed.

## Variety and escalation

Tool schemas transduce tool capability into model choices; errors enter the same action loop. Dependency tickets and reversible effects preserve local implementation consistency. A too-many-steps exception stops the task without establishing a higher organizational escalation channel.

## Evidence gaps

Source-first only; no real provider agent run. Native pytest was attempted but unavailable (No module named pytest); no upstream test pass is claimed. The package has no runtime dependencies and its small runtime/entrypoint/lifecycle paths were inspected. No unresolved concrete shipped metasystem path identified; negative claims are boundary-relative.

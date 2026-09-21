---
harness_id: dexto
project_name: Dexto
repository: https://github.com/truffle-ai/dexto
review_ref: ac56fbfcd8e7a682fc0e96c690e5b6362980181d
reviewed_at: 2026-09-21
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Dexto

## Review boundary

- System in focus: the shipped Dexto agent harness at one installed/runtime boundary, including `DextoAgent`, the first-party turn executor, sessions/state/tools/memory/permissions, `@dexto/agent-management` runtime primitives and the shipped sub-agent machinery.
- Purpose and identity: turn configured LLMs into stateful, tool-using agents and provide reusable runtime/orchestration surfaces for single-agent and multi-agent applications.
- Relevant environment: users and host applications, local/cloud model providers, workspaces/filesystems, MCP/tool services, external APIs, and operator approval input.
- Standard-distribution boundary: repository-shipped CLI/Web/server/MCP/SDK modes plus exported first-party `@dexto/core` and `@dexto/agent-management` runtime surfaces at the frozen revision.
- Credited operating / distribution surfaces: `DextoAgent`, `ChatSession`, `TurnExecutor`, tool/approval/memory services, `AgentRuntime`, `AgentSpawnerRuntime`, bundled coding-agent configuration and creator/lifecycle tool factories.
- Adjacent first-party surfaces excluded from ownership: repository CI/tests, changelog/release machinery, contributor/development instructions, examples that are not wired into the supported runtime, documentation-generation surfaces, and benchmark/evaluation material.
- First-party operating / deployment modes considered: local/self-hosted CLI and Web UI, server/API and MCP-server modes, embedded SDK use, shipped coding-agent mode, and programmatic multi-agent composition through `@dexto/agent-management`.
- Recursion level: one Dexto harness/agent installation; spawned `DextoAgent` instances are treated as candidate subordinate S1 units only where first-party runtime evidence establishes distinct operational loops.
- Reviewed revision: `ac56fbfcd8e7a682fc0e96c690e5b6362980181d`.
- Observation date: 2026-09-21.
- Generated Profile version: 0.2.3.
- Generated Methodology version: 0.3.5.
- Current Profile version: 0.2.3.
- Current Methodology version: 0.3.5.

## Repository architecture

Dexto describes itself as an open agent harness and ships a production-ready coding agent together with CLI, Web UI, server, MCP-server and embeddable SDK modes. The primary runtime is `DextoAgent`, which owns session, state, tool, memory, MCP, workspace, event and approval services. Each `ChatSession` creates a first-party LLM service and runs a `TurnExecutor` that deliberately takes control back after each single model step, executes tool calls, processes queued steer/follow-up input, handles compaction and decides whether the turn continues.

The standard coding-agent configuration wires filesystem/process/planning/todo tools and an `agent-spawner` provider. `AgentSpawnerRuntime` can create ephemeral first-party child `DextoAgent` instances, apply concurrency and iteration caps, forward child approval requests to the parent approval system, emit progress and clean children up after completion. Separately, exported `AgentRuntime` is a general-purpose lifecycle manager for multiple Dexto agents with spawn, task execution, status/list/stats and stop/stop-all surfaces.

Dexto also ships persistent memory CRUD, creator tools that can create/update skills, generic hooks, telemetry/logging and human approval machinery. These are inspected below by function rather than promoted from feature names.

## Operational model

The primary S1 is a running Dexto model/tool loop acting on user or host goals. The model supplies substantive choices such as tool selection and tool arguments; first-party runtime code controls the turn boundary, executes/validates tools, persists context and feeds observations back to the model. Spawned Dexto sub-agents can form distinct operational units because they instantiate their own `DextoAgent` loops with separate sessions/configuration and return results through first-party parent/child machinery.

The multi-agent package also exposes constructor-level organizational primitives. Its deterministic concurrency bounds and parent/child runtime establish a concrete coordination path, while `AgentRuntime` exposes a whole-pool current view plus lifecycle intervention. No default autonomous metasystem actor was found that owns those S2/S3 decisions across the whole pool, so those functions are classified as constructor paths rather than autonomous closure.

## S1 — Operations

- State: A
- Function: perform substantive user-directed work through a model-driven plan/action/tool/observation loop.
- Disturbance / variety regulated: ambiguous goals, changing conversation context, tool/service observations, tool failures, queued user steering, context pressure and provider responses.
- Decisive decision or feedback right: choose substantive next actions/tool calls and revise subsequent action from returned observations inside configured authority.
- Decision owner: the running Dexto model agent.
- Supporting / enforcement mechanisms: `DextoAgent`, `ChatSession`, first-party `TurnExecutor`, context/session persistence, `ToolManager`, approvals, queued steer/follow-up input, compaction, provider adapters and runtime state.
- Closure path: user/host goal and current context → model step → selected tool/action → first-party execution/result → observation added to context → next model step or final result.
- Boundary reachability: the shipped Dexto modes call `DextoAgent`/`ChatSession`, whose first-party `TurnExecutor` replaces the provider SDK's internal multi-step loop and explicitly controls one model step, tool execution and the next-step decision; no downstream harness implementation is required.
- Why this is / is not agent-owned: runtime code validates, transports and enforces the loop, but removing the model actor removes the discretionary choice of substantive tool/action and adaptation to the returned observation.
- Evidence: [`README.md`](https://github.com/truffle-ai/dexto/blob/ac56fbfcd8e7a682fc0e96c690e5b6362980181d/README.md), [`packages/core/src/agent/DextoAgent.ts`](https://github.com/truffle-ai/dexto/blob/ac56fbfcd8e7a682fc0e96c690e5b6362980181d/packages/core/src/agent/DextoAgent.ts), [`packages/core/src/session/chat-session.ts`](https://github.com/truffle-ai/dexto/blob/ac56fbfcd8e7a682fc0e96c690e5b6362980181d/packages/core/src/session/chat-session.ts), [`packages/core/src/llm/executor/turn-executor.ts`](https://github.com/truffle-ai/dexto/blob/ac56fbfcd8e7a682fc0e96c690e5b6362980181d/packages/core/src/llm/executor/turn-executor.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: provider inference is execution substrate; it is not imported as organizational ownership.

## S2 — Coordination

- State: C
- Function: bound destructive interference among concurrently runnable child-agent S1 units sharing one parent/runtime capacity envelope.
- Disturbance / variety regulated: excessive simultaneous sub-agent activity consuming finite parent/runtime capacity, producing unbounded parallel exploration or runaway subordinate execution.
- Decisive decision or feedback right: determine the permitted concurrent-child envelope and therefore whether another child can enter the active set.
- Decision owner: constructor/configuration owner; first-party runtime deterministically enforces the selected bound.
- Supporting / enforcement mechanisms: `maxConcurrentAgents`, global `maxAgents`, per-parent grouping, `canSpawn()`, subordinate iteration caps, task timeouts and synchronous cleanup.
- Closure path: active child count reaches the configured envelope → another spawn is rejected/withheld → existing child completes/stops and is removed → capacity becomes available → later child execution can proceed.
- Boundary reachability: the shipped coding agent includes `agent-spawner`; the provider's schema and `AgentSpawnerRuntime` implement the per-parent bound, and exported `AgentRuntime` supplies the underlying first-party agent pool. The coordination primitive is therefore available in supported distribution without a downstream scheduler implementation.
- Why this is / is not agent-owned: the standard model agent may choose when to invoke `spawn_agent`, but it does not choose or revise the concurrency policy in response to inter-agent disturbance; deterministic runtime enforces a constructor-selected limit.
- Evidence: [`README.md`](https://github.com/truffle-ai/dexto/blob/ac56fbfcd8e7a682fc0e96c690e5b6362980181d/README.md), [`agents/coding-agent/coding-agent.yml`](https://github.com/truffle-ai/dexto/blob/ac56fbfcd8e7a682fc0e96c690e5b6362980181d/agents/coding-agent/coding-agent.yml), [`packages/agent-management/src/tool-factories/agent-spawner/schemas.ts`](https://github.com/truffle-ai/dexto/blob/ac56fbfcd8e7a682fc0e96c690e5b6362980181d/packages/agent-management/src/tool-factories/agent-spawner/schemas.ts), [`packages/agent-management/src/tool-factories/agent-spawner/runtime.ts`](https://github.com/truffle-ai/dexto/blob/ac56fbfcd8e7a682fc0e96c690e5b6362980181d/packages/agent-management/src/tool-factories/agent-spawner/runtime.ts), [`packages/agent-management/src/runtime/AgentRuntime.ts`](https://github.com/truffle-ai/dexto/blob/ac56fbfcd8e7a682fc0e96c690e5b6362980181d/packages/agent-management/src/runtime/AgentRuntime.ts).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: generic delegation is not the witness; the credited S2 path is the explicit bounded shared-capacity relation across concurrently runnable subordinate S1 units. The standard distribution does not establish an autonomous actor that owns or revises this coordination decision.
- Distinct S1 units: separately instantiated spawned `DextoAgent` child loops executing independent delegated tasks.
- Inter-S1 disturbance: simultaneous child loops can exceed the configured safe/capacity envelope for one parent/runtime and create uncontrolled parallel subordinate activity.
- Attenuating coordination relation: `maxConcurrentAgents` / `maxAgents` plus runtime admission checks cap the active child set; subordinate iteration/time limits further bound the disturbance.
- Feedback into subsequent S1 behaviour: an attempted child does not enter execution when the cap is reached; completion/cleanup changes pool state so a later spawn can enter the active set.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the positive claim is tied to a concrete cross-unit concurrency disturbance and a first-party capacity attenuation path, not to the fact that tasks are delegated or messages/results are routed.

## S3 — Inside-and-now control

- State: C
- Function: expose current whole-pool visibility and lifecycle intervention over multiple Dexto operational agents for a higher-level controller.
- Disturbance / variety regulated: changing active-agent population, running/error/stopped states, current task commitments and agents that need to be stopped or removed.
- Decisive decision or feedback right: choose which agents to spawn, continue or stop based on the current pool/agent state.
- Decision owner: not supplied autonomously by the constructor surface; a downstream controller/operator must exercise the exposed right.
- Supporting / enforcement mechanisms: `AgentPool`, status transitions, grouping/filtering, `spawnAgent`, `getAgent`, `listAgents`, `getStats`, `stopAgent` and `stopAll`.
- Closure path: current pool/status view → downstream supervisory decision → spawn/stop intervention → first-party lifecycle machinery changes the active pool → updated list/stats/status is available for the next decision.
- Boundary reachability: `AgentRuntime` is exported as a first-party general-purpose multi-agent lifecycle manager and intentionally exposes pool visibility plus intervention methods; it is usable by supported applications without implementing the lifecycle substrate from scratch.
- Why this is / is not agent-owned: the first-party runtime supplies the S3-specific view and intervention path but no standard autonomous supervisor was found that observes the whole pool and owns the discretionary portfolio/resource decision. Deterministic status transitions and limits are enforcement, not autonomous S3 ownership.
- Evidence: [`packages/agent-management/src/runtime/AgentRuntime.ts`](https://github.com/truffle-ai/dexto/blob/ac56fbfcd8e7a682fc0e96c690e5b6362980181d/packages/agent-management/src/runtime/AgentRuntime.ts), [`packages/agent-management/src/runtime/index.ts`](https://github.com/truffle-ai/dexto/blob/ac56fbfcd8e7a682fc0e96c690e5b6362980181d/packages/agent-management/src/runtime/index.ts), [`packages/agent-management/src/runtime/schemas.ts`](https://github.com/truffle-ai/dexto/blob/ac56fbfcd8e7a682fc0e96c690e5b6362980181d/packages/agent-management/src/runtime/schemas.ts).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: the shipped coding agent's synchronous `spawn_agent` delegation is not itself credited as autonomous S3 because it lacks a whole-current-pool supervisory loop. The `C` claim rests on the exported `AgentRuntime` constructor surface.
- Whole-system current view: `listAgents()` can return the managed pool filtered by group/status/ephemeral state and `getStats()` summarizes the runtime population by status.
- Current-control decision scope: create a new managed operational unit or stop one/all currently managed units, changing current commitments and resource occupancy.

## S3* — Complementary audit

- State: —
- Function: no material first-party path establishes a sufficiently independent complementary auditor that challenges ordinary operational claims and closes findings back into corrective S1/S3 action.
- Disturbance / variety regulated: not established as S3* at the reviewed runtime boundary.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: hooks can inspect/modify/cancel extension-point payloads, telemetry/logging records runtime activity, approval policy gates tools, and sub-agent progress reports ordinary subordinate execution.
- Closure path: not applicable.
- Why this is / is not agent-owned: the inspected mechanisms observe, gate or transport the normal production path; no independent complementary operational-reality judgment owner was found.
- Evidence: [`packages/core/src/hooks/manager.ts`](https://github.com/truffle-ai/dexto/blob/ac56fbfcd8e7a682fc0e96c690e5b6362980181d/packages/core/src/hooks/manager.ts), [`packages/core/src/hooks/types.ts`](https://github.com/truffle-ai/dexto/blob/ac56fbfcd8e7a682fc0e96c690e5b6362980181d/packages/core/src/hooks/types.ts), [`packages/core/src/telemetry/README.md`](https://github.com/truffle-ai/dexto/blob/ac56fbfcd8e7a682fc0e96c690e5b6362980181d/packages/core/src/telemetry/README.md), [`packages/agent-management/src/tool-factories/agent-spawner/runtime.ts`](https://github.com/truffle-ai/dexto/blob/ac56fbfcd8e7a682fc0e96c690e5b6362980181d/packages/agent-management/src/tool-factories/agent-spawner/runtime.ts).
- Basis: structural absence review.
- Confidence: medium-high.
- Caveats: downstream applications can install hooks/evaluators, but generic extension capability is outside the positive constructor threshold unless the S3* function itself is supplied.

### Absence scope

- Surfaces inspected: core hook manager/types, telemetry/logging, tool approval/gating, runtime error/retry paths, sub-agent progress/status reporting and first-party tests/docs around those mechanisms.
- Plausible first-party paths checked: hooks as complementary inspection; telemetry/logs as audit; approval as audit judgment; sub-agent progress monitoring as independent audit; ordinary retry/error handling as corrective audit.
- Why no material first-party path remains: these paths remain part of ordinary execution, observation or enforcement and do not establish materially independent complementary access plus a distinct audit judgment returned into corrective control.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party path establishes an external-and-prospective adaptation loop that develops future-oriented options and closes them back into current capability.
- Disturbance / variety regulated: not established as S4 at the reviewed boundary.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: persistent memory CRUD, skill creation/update tools, dynamic skill loading, web/search/tool access, configurable model/tool switching and ordinary current-task planning.
- Closure path: not applicable.
- Why this is / is not agent-owned: a model can write memories or create/update a skill when those tools are available, but the standard evidence reviewed does not supply the missing external/prospective distinction and adaptation-judgment loop; persistence/self-modification alone is not S4.
- Evidence: [`packages/tools-lifecycle/src/memory-tools.ts`](https://github.com/truffle-ai/dexto/blob/ac56fbfcd8e7a682fc0e96c690e5b6362980181d/packages/tools-lifecycle/src/memory-tools.ts), [`packages/agent-management/src/tool-factories/creator-tools/factory.ts`](https://github.com/truffle-ai/dexto/blob/ac56fbfcd8e7a682fc0e96c690e5b6362980181d/packages/agent-management/src/tool-factories/creator-tools/factory.ts), [`.agents/skills/create-skill/SKILL.md`](https://github.com/truffle-ai/dexto/blob/ac56fbfcd8e7a682fc0e96c690e5b6362980181d/.agents/skills/create-skill/SKILL.md), [`docs/docs/architecture/skills.md`](https://github.com/truffle-ai/dexto/blob/ac56fbfcd8e7a682fc0e96c690e5b6362980181d/docs/docs/architecture/skills.md).
- Basis: structural absence review.
- Confidence: medium-high.
- Caveats: creator tools are strong capability-mutation primitives and could support an S4 design, but Methodology does not award `C` from generic self-modification primitives when the S4 function itself is not established.

### Absence scope

- Surfaces inspected: persistent memory manager/tools, local skills discovery, skill creator/update/refresh flow, coding-agent prompts/configuration, web/search capability, model/tool switching, session history/search and repository docs for skills.
- Plausible first-party paths checked: memory as learning/S4; skill creation as self-improvement/S4; web search as environmental sensing; model switching as adaptation; current planning as prospective intelligence.
- Why no material first-party path remains: the reviewed standard distribution exposes storage, sensing and capability-mutation mechanisms but no shipped loop that distinguishes future/external change, develops an adaptation option from it and returns that option into present capability as S4 rather than ordinary current-task action.

## S5 — Policy and identity

- State: —
- Function: no material first-party runtime path establishes identity/ultimate-policy adjudication at the chosen Dexto harness recursion.
- Disturbance / variety regulated: not established as S5.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: system prompts, YAML configuration, permission modes/tool policies, human tool approvals, agent registry/configuration, safety hooks and operator setup.
- Closure path: not applicable.
- Why this is / is not agent-owned: these surfaces define or enforce operating constraints and authorize current actions, but no identity/constitutional-policy issue → legitimate ultimate authority → authoritative decision → returned governing-policy loop was established.
- Evidence: [`README.md`](https://github.com/truffle-ai/dexto/blob/ac56fbfcd8e7a682fc0e96c690e5b6362980181d/README.md), [`agents/coding-agent/coding-agent.yml`](https://github.com/truffle-ai/dexto/blob/ac56fbfcd8e7a682fc0e96c690e5b6362980181d/agents/coding-agent/coding-agent.yml), [`packages/core/src/agent/DextoAgent.ts`](https://github.com/truffle-ai/dexto/blob/ac56fbfcd8e7a682fc0e96c690e5b6362980181d/packages/core/src/agent/DextoAgent.ts), [`packages/core/src/hooks/types.ts`](https://github.com/truffle-ai/dexto/blob/ac56fbfcd8e7a682fc0e96c690e5b6362980181d/packages/core/src/hooks/types.ts).
- Basis: structural absence review.
- Confidence: medium-high.
- Caveats: an operator can change configuration and approve risky tool actions, but generic operator authority/action approval is not automatically S5=P.

### Absence scope

- Surfaces inspected: system prompts, agent YAML/runtime configuration, permissions/tool policies, approval flow, hooks, agent registry/manager, operator setup and human-in-the-loop documentation.
- Plausible first-party paths checked: system prompt as S5; human tool approval as S5=P; permission configuration as policy closure; agent configuration/registry as identity governance; hook cancellation as ultimate policy.
- Why no material first-party path remains: all inspected paths configure, constrain or authorize operational behavior; none reconstructs an identity/ultimate-policy dispute resolved by legitimate ultimate authority and returned as governing policy at this recursion.

## Distributed OSS parent arrangement

Repository maintainers and contributors can change Dexto code/configuration, but public project governance is outside the running-harness boundary. No organization-level `(P)` state is inferred from ordinary maintainership, PR review or release authority. A downstream operator can supervise one deployment, but only function-specific runtime closure would justify parent-mode notation.

## Self-hosted and non-human modes

Dexto explicitly supports local/self-hosted execution and local models. The S1 loop remains first-party regardless of whether inference is local or remote. Operator approval and configuration modes materially constrain current actions but do not by themselves establish parent-governed S3/S4/S5. Programmatic multi-agent use exposes constructor-level S2/S3 primitives without requiring a human parent.

## Recursion

A spawned child created by `AgentSpawnerRuntime` instantiates another `DextoAgent` with its own session and model/tool loop, so it can serve as a distinct subordinate operational unit. The assessment does not claim full recursive viability for every child merely from spawning; only the operational S1 distinction and parent/child coordination/control primitives are credited.

## Variety and escalation

Dexto absorbs operational variety through model/tool iteration, queued user steering, permissions/approvals, context management, provider/tool selection, sub-agent delegation and deterministic runtime limits. Child approval requests can flow into the parent's approval system, and operator approval can gate risky current actions. These escalation paths remain operational unless the escalated matter is shown to close a higher VSM function.

## Evidence gaps

- No autonomous S2 actor was found that owns/revises the coordination response; the positive S2 claim is constructor-owned deterministic bounded concurrency.
- No standard autonomous whole-pool supervisor was found over exported `AgentRuntime`; therefore S3 remains `C`, not `A`.
- Hooks, telemetry, logs and progress reporting did not establish an independent complementary S3* auditor.
- Persistent memory and creator tools are real mutation surfaces but no first-party external-and-prospective S4 loop was established.
- No identity/ultimate-policy S5 closure was established; ordinary prompts, permissions and human tool approvals are intentionally not promoted to S5.

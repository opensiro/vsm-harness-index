---
harness_id: continual-harness
project_name: Continual Harness
repository: https://github.com/sethkarten/continual-harness
review_ref: bbab97ad73e460b7cd7c08527d10ced30cc03fbe
reviewed_at: 2026-09-24
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-24
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: A
autonomy_s5: —
---

# Continual Harness

## Review boundary

- System in focus: one first-party Continual Harness run at pinned revision `bbab97ad73e460b7cd7c08527d10ced30cc03fbe`, using the repository's `continualharness` PokeAgent scaffold together with its game-facing runtime, run/trajectory persistence, persistent memory/skill/subagent stores, and supported `HarnessEvolver` path enabled through `--enable-prompt-optimization`.
- Purpose and identity: operate autonomously in the Pokémon environment while preserving and autonomously revising reusable harness capability — prompt, skills, custom subagents and memory — from accumulated trajectory evidence so later operation can change without resetting the run.
- Relevant environment: Pokémon Red/Emerald emulator/game state; MCP-style game/action endpoints; operator-selected starting state/objectives; model-provider APIs used by the operational agent and Refiner; persisted run trajectories/checkpoints; prior-run artifacts when the explicit bootstrap mode is selected.
- Standard-distribution boundary: repository-shipped `run.py`; `PokeAgent`; scaffold-specific tool registry and Continual Harness prompts; game/server adapters; run-data/trajectory persistence; memory, skill and subagent stores; `HarnessEvolver`/`PromptOptimizer`; and the documented `continualharness + --enable-prompt-optimization` operating mode. External Gemini/OpenAI/OpenRouter/Anthropic/provider internals and the Pokémon emulator/game itself remain environmental dependencies.
- Credited operating / distribution surfaces: `README.md`; `run.py`; `agents/PokeAgent.py`; `agents/tools/registry.py`; `agents/utils/harness_evolver.py`; `agents/utils/prompt_optimizer.py`; `agents/prompts/pokeagent-directives/continual-harness/SYSTEM_PROMPT.md`; `utils/stores/base_store.py`; repository-shipped run scripts and architecture notes that corroborate reachability.
- Adjacent first-party surfaces excluded from ownership: paper/result tables and benchmark comparisons; repository-development CI/release work; built-in expert subagents that the `continualharness` scaffold explicitly excludes; other scaffolds such as `pokeagent`, `simple`, `simplest`, `autonomous_cli` and `vision_only` except where they clarify boundary contrasts; arbitrary downstream custom subagents that may be created at runtime; functions internal to external model providers.
- First-party operating / deployment modes considered: the README-documented Continual Harness invocation with `--scaffold continualharness --enable-prompt-optimization`; autonomous agent operation through the model/tool loop; scheduled harness evolution after trajectory warmup; agent-triggered `evolve_harness`; persistent skill/memory/subagent CRUD; and the explicit prior-run bootstrap option only as a supporting persistence mode.
- Recursion level: one continually adapting PokeAgent run is the system-in-focus. The PokeAgent model/tool loop is S1. Custom subagents are bounded task helpers created/used inside that operation and are not treated as independently viable recursive S1 units merely because they have separate prompts or execution loops. The HarnessEvolver is assessed as a metasystem adaptation actor over the same operational organization.
- Reviewed revision: `bbab97ad73e460b7cd7c08527d10ced30cc03fbe`.
- Observation date: 2026-09-24.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Continual Harness ships a concrete autonomous PokeAgent rather than only an optimizer around an external agent. `run.py` exposes the `continualharness` scaffold and passes the selected model/backend and `--enable-prompt-optimization` flag into `PokeAgent`. The README documents that combination as the Continual Harness run. `PokeAgent.run_step()` calls the configured model with the current state/context and first-party tool declarations, executes model-selected function calls, publishes the returned tool result into runtime/history/trajectory state, and continues on later turns. This closes the first-party S1 operation loop; the game server and model provider are dependencies rather than organizational decision owners.

The `continualharness` scaffold deliberately differs from the expert PokeAgent surface. `agents/tools/registry.py` marks it as a no-builtins scaffold: it retains generic memory/skill/code/custom-subagent primitives and `replan_objectives`, but excludes the repository's built-in expert subagent tools. It uniquely exposes `evolve_harness`, whose contract asks the operational agent to trigger an evolution pass when it notices an underperforming skill/subagent rather than waiting for the scheduled cycle. This prevents neighboring verifier/reflection subagents from being silently imported into the assessed scaffold.

When the documented evolution mode is enabled, `PokeAgent` constructs `HarnessEvolver` with the active model actor and run-data manager. Evolution is not merely an offline post-processing script. During ordinary operation, after trajectory logging, `PokeAgent` checks `HarnessEvolver.should_evolve(...)` and automatically invokes `HarnessEvolver.evolve(...)`; the same evolution path can also be invoked on demand through the model-selected `evolve_harness` tool.

`HarnessEvolver` consumes recent trajectories and performs separate prompt, subagent, skill and memory evolution passes. Its model-driven adaptation actor sees the current registries plus recent behavior/failure evidence and chooses concrete create/update/retire/replace actions. The affected stores are persistent JSON stores, while prompt optimization exposes the current evolved prompt back to `PokeAgent`. Later S1 turns therefore operate with changed durable capability. The standard runtime also injects an evolution summary back into the operational context so the PokeAgent knows what changed.

This adaptation architecture is kept separate from current-control and audit semantics. `replan_objectives`, local custom subagents and action-history machinery help the same S1 pursue the present game objective; they do not establish a distinct whole-organization S3 manager. Likewise, the repository contains a built-in `subagent_verify` implementation in the wider PokeAgent codebase, but `subagent_verify` is explicitly listed among `BUILTIN_SUBAGENT_TOOL_NAMES`, and the `continualharness` scaffold excludes those built-ins. Generic capability to create a downstream custom subagent is not treated as a first-party S3* construction path without evidence that the standard organization assigns it a complementary-audit function.

Published benchmark/paper performance is not used to establish any VSM state in this assessment. The assessment maps the frozen repository's organizational function and ownership only.

## Operational model

A documented Continual Harness run starts the game/server environment, creates `PokeAgent` with the `continualharness` scaffold, initializes run persistence and enables harness evolution. On each operational turn, the PokeAgent receives current state/context, the model selects substantive actions/tools, first-party runtime executes them, and the returned state/result becomes context for later decisions.

In parallel with that continuing operation, the adaptation loop accumulates trajectory evidence. After warmup, an adaptive schedule triggers the HarnessEvolver automatically; the S1 model can also request an immediate pass through `evolve_harness`. The Refiner interprets recent behavior and chooses persistent changes to prompt, custom subagents, skills and memory. Those mutations are stored/reloaded and affect subsequent operational turns. This is an outside-and-then adaptation loop over durable capability, not merely transient context accumulation.

## S1 — Operations

- State: A
- Function: pursue the current game objective through an autonomous model/tool loop that observes game state, chooses actions and supporting tools, receives results and continues until the run objective/budget ends.
- Disturbance / variety regulated: changing game state, navigation/battle/menu uncertainty, tool success/failure, current objectives, accumulated memories/skills, model uncertainty, action outcomes and environment transitions.
- Decisive decision or feedback right: choose the next substantive operational action/tool invocation from current state and history and use returned observations to decide what follows.
- Decision owner: the model-driven first-party `PokeAgent` orchestrator instantiated by the `continualharness` scaffold.
- Supporting / enforcement mechanisms: `run.py`; VLM backend wrapper; scaffold-filtered tool declarations; MCP/game adapter; function-call execution; runtime/history publication; trajectory logging; action queue/state reads; step/context limits and persistence.
- Closure path: game/current objective/context → PokeAgent model call → model-selected game/tool/custom-subagent action → first-party execution/game result → result/history/trajectory publication → next PokeAgent turn.
- Boundary reachability: `run.py` directly lists `continualharness` as a supported scaffold and constructs `PokeAgent`; the README supplies a normal command-line invocation for this mode. No adjacent external agent harness is needed to supply the goal-directed decision loop.
- Why this is / is not agent-owned: deterministic server/tool machinery transports and constrains actions, but the substantive next-action decision belongs to the model-driven PokeAgent. Removing that actor while retaining persistence, MCP endpoints and stores leaves no autonomous objective-pursuit loop.
- Evidence: [`README.md`](https://github.com/sethkarten/continual-harness/blob/bbab97ad73e460b7cd7c08527d10ced30cc03fbe/README.md); [`run.py`](https://github.com/sethkarten/continual-harness/blob/bbab97ad73e460b7cd7c08527d10ced30cc03fbe/run.py); [`agents/PokeAgent.py`](https://github.com/sethkarten/continual-harness/blob/bbab97ad73e460b7cd7c08527d10ced30cc03fbe/agents/PokeAgent.py); [`agents/tools/registry.py`](https://github.com/sethkarten/continual-harness/blob/bbab97ad73e460b7cd7c08527d10ced30cc03fbe/agents/tools/registry.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: model-provider inference is external, but the operational loop, state assembly, tool contract, execution and returned-feedback path are first-party. Other repository scaffolds are not needed for the positive S1 claim.

## S2 — Coordination

- State: —
- Function: no material first-party S2 relation is established at the declared Continual Harness recursion.
- Disturbance / variety regulated: the scaffold can create/use multiple custom subagents and route bounded work to them, but the reviewed first-party organization does not establish distinct viable sibling S1 units whose interaction generates a concrete conflict, oscillation or interference condition requiring attenuation.
- Decisive decision or feedback right: not established for S2.
- Decision owner: not established.
- Supporting / enforcement mechanisms: custom-subagent registry, subagent execution, `return_to_orchestrator`, objective replanning, shared memory/skill stores and ordinary result handoff.
- Closure path: helper/subagent results can be returned to the PokeAgent and inform the same S1's next action. No separate disturbance-specific coordination loop among sibling viable units is established.
- Boundary reachability: the generic helper/subagent primitives are reachable, but their evidenced function is decomposition/support for one PokeAgent operation rather than S2.
- Why this is / is not agent-owned: agent plurality, delegation, shared registries and result handoff do not establish S2 without the required inter-S1 disturbance and attenuation relation.
- Evidence: [`agents/tools/registry.py`](https://github.com/sethkarten/continual-harness/blob/bbab97ad73e460b7cd7c08527d10ced30cc03fbe/agents/tools/registry.py); [`agents/PokeAgent.py`](https://github.com/sethkarten/continual-harness/blob/bbab97ad73e460b7cd7c08527d10ced30cc03fbe/agents/PokeAgent.py); [`agents/utils/harness_evolver.py`](https://github.com/sethkarten/continual-harness/blob/bbab97ad73e460b7cd7c08527d10ced30cc03fbe/agents/utils/harness_evolver.py).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: a later evolved custom-subagent organization could instantiate a real S2 relation, but that emergent/downstream organization would require its own functional evidence rather than being inferred from the generic registry.
- Distinct S1 units checked: PokeAgent plus custom/bounded subagent execution paths.
- Inter-S1 disturbance checked: no standard first-party conflict/oscillation/contention witness between independent viable units was found.
- Why generic communication/routing/delegation is insufficient: the helper result returns to one orchestrator's current task; that is task decomposition, not a demonstrated mutual-regulation loop.

### Absence scope

- Surfaces inspected: scaffold tool registry, custom-subagent CRUD/execution, local subagent machinery, objective replanning, shared memory/skill stores, HarnessEvolver-created subagents and run architecture.
- Plausible first-party paths checked: multiple subagents as S2; `return_to_orchestrator` as coordination; shared stores as coordination; objective replanning as inter-unit coordination.
- Why no material first-party path remains: none of these paths reconstructs the required sibling-S1 disturbance → attenuation → feedback relation at the declared recursion.

## S3 — Inside-and-now control

- State: —
- Function: no distinct whole-system inside-and-now management function is established at the reviewed run boundary.
- Disturbance / variety regulated: PokeAgent can replan current objectives, inspect state, delegate bounded work and manage its own reusable tools; those are local S1 decisions/support mechanisms rather than a separate current-control right over multiple operational units.
- Decisive decision or feedback right: no first-party actor is shown receiving a whole-current-organization view and deciding resource/priority/commitment/intervention allocation among independently viable S1 operations.
- Decision owner: not established for S3.
- Supporting / enforcement mechanisms: `replan_objectives`, current game/run state, objective completion, step/runtime state, action queue handling, subagent registry and run-data persistence.
- Closure path: current-state information returns to the same PokeAgent operation and changes its local plan/actions. No distinct whole-system present-management loop closes.
- Boundary reachability: the current-task controls are normal runtime surfaces; their negative classification is functional rather than due to absence or unreachability.
- Why this is / is not agent-owned: the PokeAgent owns S1 task pursuit. Replanning the same operational task or invoking helpers does not create a separate S3 merely because the orchestrator has a broad local context.
- Evidence: [`agents/PokeAgent.py`](https://github.com/sethkarten/continual-harness/blob/bbab97ad73e460b7cd7c08527d10ced30cc03fbe/agents/PokeAgent.py); [`agents/tools/registry.py`](https://github.com/sethkarten/continual-harness/blob/bbab97ad73e460b7cd7c08527d10ced30cc03fbe/agents/tools/registry.py); [`run.py`](https://github.com/sethkarten/continual-harness/blob/bbab97ad73e460b7cd7c08527d10ced30cc03fbe/run.py).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: HarnessEvolver makes organizational changes for future operation and is therefore considered under S4, not relabeled as S3 because it runs during the same long episode.

### Absence scope

- Surfaces inspected: PokeAgent runtime, objective planning/replanning, action execution, subagent execution, run/server state, scheduled evolution and persistence.
- Plausible first-party paths checked: PokeAgent as whole-system manager; objective planner as manager; action queue/server lifecycle as S3; HarnessEvolver as current manager.
- Why no material first-party path remains: all reviewed present-time controls either belong to one S1's operational loop, are deterministic infrastructure, or are prospective capability adaptation mapped to S4.

## S3* — Complementary audit

- State: —
- Function: no material first-party complementary-audit path is established for the `continualharness` operating mode.
- Disturbance / variety regulated: not established as a distinct independent challenge to S1 claims/results with corrective return.
- Decisive decision or feedback right: not established for S3*.
- Decision owner: not established.
- Supporting / enforcement mechanisms: trajectory logging, run-state snapshots, HarnessEvolver analysis and the repository-wide local subagent implementations are evidence/diagnostic surfaces but do not establish the required complementary-audit organization for this scaffold.
- Closure path: recent trajectories are consumed by the S4 Refiner to decide future capability changes. That is adaptation evidence flow, not a separate auditor judging an S1 claim and returning a corrective discrepancy into current control.
- Boundary reachability: importantly, the wider repository's built-in `subagent_verify` is **not** reachable in the assessed scaffold. `subagent_verify` is part of `BUILTIN_SUBAGENT_TOOL_NAMES`; `continualharness` is a `NO_BUILTINS_SCAFFOLDS` member and filters those tools out.
- Why this is / is not agent-owned: a verifier implementation existing elsewhere in the repository cannot donate S3* to a mode that deliberately excludes it. Generic ability to create a custom subagent also does not establish an S3*-specific constructor without evidence assigning that subagent independent complementary-audit responsibility and corrective closure.
- Evidence: [`agents/tools/registry.py`](https://github.com/sethkarten/continual-harness/blob/bbab97ad73e460b7cd7c08527d10ced30cc03fbe/agents/tools/registry.py); [`agents/subagents/utils/registry.py`](https://github.com/sethkarten/continual-harness/blob/bbab97ad73e460b7cd7c08527d10ced30cc03fbe/agents/subagents/utils/registry.py); [`agents/PokeAgent.py`](https://github.com/sethkarten/continual-harness/blob/bbab97ad73e460b7cd7c08527d10ced30cc03fbe/agents/PokeAgent.py); [`agents/utils/harness_evolver.py`](https://github.com/sethkarten/continual-harness/blob/bbab97ad73e460b7cd7c08527d10ced30cc03fbe/agents/utils/harness_evolver.py).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: other PokeAgent scaffolds may expose built-in verification helpers; they are distinct deployment modes and are excluded from this Continual Harness boundary.

### Absence scope

- Surfaces inspected: scaffold-filtered tool registry, built-in subagent registry, `subagent_verify` implementation, custom-subagent construction path, trajectory logging, HarnessEvolver analysis and run state.
- Plausible first-party paths checked: built-in verifier as S3*; Refiner trajectory analysis as audit; custom-subagent construction as S3* constructor; deterministic run/game evidence as audit.
- Why no material first-party path remains: the explicit verifier is filtered out of this scaffold, Refiner evidence is consumed for S4 adaptation, and generic extensibility does not itself establish the function-specific audit right.

## S4 — Outside-and-then adaptation

- State: A
- Function: interpret accumulated operational evidence and autonomously change the durable harness repertoire — prompt, custom subagents, skills and memory — so later S1 operation uses a revised capability organization.
- Disturbance / variety regulated: recurring operational failures, ineffective or missing skills/subagents, repeated disposable code patterns, stale/incorrect reusable knowledge, prompt weaknesses and other distinctions visible across recent trajectories rather than only the immediately current action.
- Decisive decision or feedback right: choose what durable harness capability should be created, updated, retired or rewritten in response to longitudinal trajectory evidence.
- Decision owner: the model-driven first-party `HarnessEvolver`/composed `PromptOptimizer` in the supported Continual Harness evolution mode; the PokeAgent may additionally decide to invoke the same autonomous adaptation pass early through `evolve_harness`.
- Supporting / enforcement mechanisms: trajectory/run-data persistence; adaptive evolution schedule; prompt optimizer; persistent memory/skill/subagent stores; scaffold-specific evolution prompt; tool-failure extraction; CRUD/storage helpers; evolution log; reload/use of current evolved prompt and stores; evolution-summary injection.
- Closure path: S1 produces and persists trajectory/action/tool evidence → after warmup the first-party schedule triggers HarnessEvolver, or the PokeAgent requests `evolve_harness` → Refiner model analyzes recent evidence and chooses prompt/subagent/skill/memory changes → first-party stores/optimizer persist those changes → later S1 turns load/use the changed prompt and registries → new operational evidence accumulates for subsequent adaptation.
- Boundary reachability: `run.py` exposes the necessary flag and scaffold; the README documents the exact `--scaffold continualharness --enable-prompt-optimization` mode; repository test/run scripts exercise the same mode. Once selected, the runtime itself closes scheduled evolution automatically and exposes on-demand evolution to the operational actor.
- Why this is / is not agent-owned: the flag selects an operating mode but does not decide individual adaptations. Within that supported mode, the model-driven Refiner interprets evidence and chooses substantive mutations; deterministic scheduling/storage merely invokes and applies that judgment. Therefore the adaptation right is autonomous rather than constructor-only.
- Evidence: [`README.md`](https://github.com/sethkarten/continual-harness/blob/bbab97ad73e460b7cd7c08527d10ced30cc03fbe/README.md); [`run.py`](https://github.com/sethkarten/continual-harness/blob/bbab97ad73e460b7cd7c08527d10ced30cc03fbe/run.py); [`agents/PokeAgent.py`](https://github.com/sethkarten/continual-harness/blob/bbab97ad73e460b7cd7c08527d10ced30cc03fbe/agents/PokeAgent.py); [`agents/utils/harness_evolver.py`](https://github.com/sethkarten/continual-harness/blob/bbab97ad73e460b7cd7c08527d10ced30cc03fbe/agents/utils/harness_evolver.py); [`utils/stores/base_store.py`](https://github.com/sethkarten/continual-harness/blob/bbab97ad73e460b7cd7c08527d10ced30cc03fbe/utils/stores/base_store.py); [`agents/prompts/pokeagent-directives/continual-harness/SYSTEM_PROMPT.md`](https://github.com/sethkarten/continual-harness/blob/bbab97ad73e460b7cd7c08527d10ced30cc03fbe/agents/prompts/pokeagent-directives/continual-harness/SYSTEM_PROMPT.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: full harness evolution is not enabled by the scaffold name alone; the documented `--enable-prompt-optimization` mode must be selected. This is treated as a supported deployment/operating mode, not as downstream code construction. Benchmark/paper improvement numbers are not used to establish ownership.
- External / future-facing signal: longitudinal trajectory/tool-failure evidence accumulated over many operational steps, including repeated weaknesses and missing/underperforming reusable capabilities.
- Adaptation option generation: the Refiner model proposes concrete prompt rewrites and subagent/skill/memory create/update/retire actions from that evidence.
- Return into operation: the selected changes are persisted in the prompt/stores and consumed by subsequent PokeAgent turns in the same continuing run.

## S5 — Policy / identity

- State: —
- Function: no material first-party identity/ultimate-policy closure is established at the assessed run boundary.
- Disturbance / variety regulated: scaffold/model/game/objective selection, evolution enablement, fixed system instructions and tool constraints define or constrain the run, but no runtime actor recognizes an identity-level policy issue, refers it to legitimate ultimate authority and returns a binding identity/policy decision into the organization.
- Decisive decision or feedback right: not established for S5.
- Decision owner: not established.
- Supporting / enforcement mechanisms: CLI configuration, fixed scaffold-specific system prompt, tool availability, model/backend selection, objective configuration, bootstrap choice and deterministic safety/runtime constraints.
- Closure path: configuration is supplied before/during startup and lower-level mechanisms obey it; no S5 issue → legitimate authority → policy adjudication/revision → returned governing identity loop is evidenced.
- Boundary reachability: the configuration/prompt surfaces are reachable, but they are lower-level operating constraints rather than S5 closure.
- Why this is / is not agent-owned: the HarnessEvolver can change selected operational capability layers, but the fixed organizational identity/ultimate-policy layer is not itself placed under a legitimate runtime policy authority. Evolution therefore remains S4 rather than silently becoming S5.
- Evidence: [`run.py`](https://github.com/sethkarten/continual-harness/blob/bbab97ad73e460b7cd7c08527d10ced30cc03fbe/run.py); [`agents/prompts/pokeagent-directives/continual-harness/SYSTEM_PROMPT.md`](https://github.com/sethkarten/continual-harness/blob/bbab97ad73e460b7cd7c08527d10ced30cc03fbe/agents/prompts/pokeagent-directives/continual-harness/SYSTEM_PROMPT.md); [`agents/PokeAgent.py`](https://github.com/sethkarten/continual-harness/blob/bbab97ad73e460b7cd7c08527d10ced30cc03fbe/agents/PokeAgent.py); [`agents/utils/harness_evolver.py`](https://github.com/sethkarten/continual-harness/blob/bbab97ad73e460b7cd7c08527d10ced30cc03fbe/agents/utils/harness_evolver.py).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: operator choice to enable evolution or choose a scaffold is configuration/admission of a deployment mode, not evidence of parent-governed S5.

### Absence scope

- Surfaces inspected: CLI/scaffold configuration, fixed system prompt, evolution boundaries, model/backend/objective selection, persistence/bootstrap, tool registry and HarnessEvolver mutation repertoire.
- Plausible first-party paths checked: system prompt as S5; operator flag as parent authority; bootstrap as identity choice; HarnessEvolver as policy authority; tool constraints as policy.
- Why no material first-party path remains: the reviewed paths configure or adapt lower-level operation but do not implement legitimate ultimate-policy adjudication and returned identity closure.

## Summary

| Function | State | Decision owner | Evidence basis | Confidence |
| --- | --- | --- | --- | --- |
| S1 | A | model-driven `PokeAgent` in the `continualharness` scaffold | explicit + structural | high |
| S2 | — | not established | explicit + structural negative search | high |
| S3 | — | not established | explicit + structural negative search | high |
| S3* | — | not established; built-in verifier excluded from this scaffold | explicit + structural negative search | high |
| S4 | A | model-driven first-party `HarnessEvolver` / `PromptOptimizer` | explicit + structural | high |
| S5 | — | not established | explicit + structural negative search | high |

Standalone signature:

```text
S1=A / S2=— / S3=— / S3*=— / S4=A / S5=—
```

The defining organizational feature is not simply that Continual Harness stores memory or contains a component named Refiner. In the documented evolution mode, it closes a genuine prospective adaptation loop: operational trajectories become evidence for an autonomous Refiner, which chooses persistent changes to the harness and returns them into later operation. Conversely, built-in verification machinery from neighboring scaffolds is deliberately excluded rather than borrowed into S3*, and generic subagent/delegation facilities are not treated as S2/S3 without their required organizational functions.

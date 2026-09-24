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
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: A
autonomy_s5: —
---

# Continual Harness

## Review boundary

- System in focus: one first-party Continual Harness organization at pinned revision `bbab97ad73e460b7cd7c08527d10ced30cc03fbe`, specifically the in-repository `PokeAgent` operating loop running with scaffold `continualharness`, the game/environment runtime it acts through, persistent prompt/subagent/skill/memory stores, run-data/trajectory state, and the standard `HarnessEvolver` path enabled by `--enable-prompt-optimization`.
- Purpose and identity: operate a long-running foundation agent against an environment while allowing the same installed organization to adapt its durable harness in place from accumulated operational evidence, without resetting the ongoing episode between adaptations.
- Relevant environment: Pokémon Red/Emerald game state and emulator/runtime feedback, screenshots and structured map/state, objectives and tool outcomes, model-provider inference, persistent run data, and historical trajectories used by the Refiner.
- Standard-distribution boundary: the repository's Python agent/runtime, scaffold/tool registry, persistent stores, trajectory/run-data machinery and HarnessEvolver are inside. Model-provider APIs, emulator/game assets and external CLI harnesses exposed elsewhere in the repository are dependencies or alternate modes and do not donate VSM functions to this review boundary.
- Credited operating / distribution surfaces: `run.py`; `agents/PokeAgent.py`; `agents/tools/registry.py`; `agents/utils/harness_evolver.py`; `agents/utils/prompt_optimizer.py`; `utils/stores/{memory,skills,subagents}.py`; `System-Design/architecture/harness_evolver.md`; the first-party `continualharness` scaffold documented in `README.md`.
- Adjacent first-party surfaces excluded from ownership: the hand-engineered `pokeagent` scaffold, external Claude Code/Gemini CLI/Codex/Hermes MCP modes, repository-development tests/CI, benchmark-paper result tables, and built-in verifier/reflection subagents that the `continualharness` scaffold explicitly excludes from its normal tool surface.
- First-party operating / deployment modes considered: in-repo `PokeAgent` with `--scaffold continualharness --enable-prompt-optimization`, including reset-free in-episode evolution; bootstrap-from-prior-run is corroborating persistence evidence but is not required for the autonomous S4 claim.
- Recursion level: one continuing Continual Harness agent organization operating one environment episode. Local/custom subagents created inside the harness are subordinate operating mechanisms and are not presumed to be separate viable recursive organizations merely because they are separately configured.
- Reviewed revision: `bbab97ad73e460b7cd7c08527d10ced30cc03fbe`.
- Observation date: 2026-09-24.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Continual Harness ships a concrete environment-facing agent and a distinct adaptation path inside the same first-party runtime. `PokeAgent` owns the ordinary model/tool loop: it maintains conversation/run state, assembles the scaffold-specific system prompt and tool declarations, calls the configured model, executes first-party/local or server-backed tools, records trajectories and carries observations into later agent turns.

When the standard `continualharness` mode is launched with prompt optimization enabled, `PokeAgent` constructs a `HarnessEvolver`. The evolver reads recent trajectory evidence on an adaptive schedule and performs four model-driven adaptation passes over the installed harness: prompt, subagents, skills and memory. The resulting persistent state is used by the continuing PokeAgent organization on subsequent steps of the same episode. First-party documentation explicitly describes this as reset-free mid-episode refinement and supports later bootstrapping from a prior evolved harness.

The functional separation is therefore S1 = continuing environment-facing agent operation, and S4 = a separate evidence-to-persistent-adaptation loop that diagnoses accumulated operating evidence and changes future operating capability before S1 continues.

The repository also contains richer PokeAgent modes with built-in `subagent_verify`, reflection and planning helpers. Those surfaces are not imported into this assessment. `continualharness` is one of the scaffolds for which `run.py` sets `EXCLUDE_BUILTIN_SUBAGENTS=1`, and the tool registry filters built-in subagent tools when that exclusion is active.

## Primary evidence

- [`README.md`](https://github.com/sethkarten/continual-harness/blob/bbab97ad73e460b7cd7c08527d10ced30cc03fbe/README.md) — reference scaffold, reset-free harness evolution, persistent adaptation surfaces and launch flags.
- [`agents/PokeAgent.py`](https://github.com/sethkarten/continual-harness/blob/bbab97ad73e460b7cd7c08527d10ced30cc03fbe/agents/PokeAgent.py) — operational loop, scaffold selection, HarnessEvolver construction and runtime evolution trigger/return path.
- [`agents/utils/harness_evolver.py`](https://github.com/sethkarten/continual-harness/blob/bbab97ad73e460b7cd7c08527d10ced30cc03fbe/agents/utils/harness_evolver.py) — evolution schedule, trajectory sensing, model-driven prompt/subagent/skill/memory mutation and evolution logging.
- [`agents/tools/registry.py`](https://github.com/sethkarten/continual-harness/blob/bbab97ad73e460b7cd7c08527d10ced30cc03fbe/agents/tools/registry.py) — scaffold-specific tool surface and built-in-subagent exclusion.
- [`run.py`](https://github.com/sethkarten/continual-harness/blob/bbab97ad73e460b7cd7c08527d10ced30cc03fbe/run.py) — normal launch wiring, optimization flag propagation and `EXCLUDE_BUILTIN_SUBAGENTS` boundary.
- [`System-Design/architecture/harness_evolver.md`](https://github.com/sethkarten/continual-harness/blob/bbab97ad73e460b7cd7c08527d10ced30cc03fbe/System-Design/architecture/harness_evolver.md) — post-step `should_evolve → evolve → _inject_evolution_summary` closure.

## Operational model

A standard Continual Harness run starts the environment/runtime and an in-repository PokeAgent configured with the `continualharness` scaffold. On each operating turn the model receives current context and the admitted first-party tool surface, selects an action, receives tool/environment feedback, and continues.

After enough operational steps, HarnessEvolver inspects a recent trajectory window. Its model-driven Refiner diagnoses patterns and chooses persistent changes to one or more of prompt, subagent registry, skill library and memory. Those stores are subsequently consumed by PokeAgent, and the evolution result is injected into the continuing orchestrator context. The episode is not reset.

## S1 — Operations

- State: A
- Function: pursue the environment objective through a continuing model-driven PokeAgent loop that observes current state, chooses first-party tools/actions, receives their results and continues until the episode/run terminates.
- Disturbance / variety regulated: changing game state, screenshots/map/state observations, objective progress, tool/action outcomes, local failures, context pressure and open-ended next-action choice.
- Decisive decision or feedback right: choose the next substantive environment/tool action from current operating context and returned observations.
- Decision owner: the model-driven PokeAgent actor assembled and driven by the first-party runtime.
- Supporting / enforcement mechanisms: server/MCP adapter, scaffold-specific tool registry, conversation/run state, trajectory logging, persistent stores, context handling and execution bounds.
- Closure path: environment/context → PokeAgent model turn → model-selected action/tool → first-party execution/environment feedback → updated context → next model turn.
- Boundary reachability: `run.py` directly launches the in-repository agent path; `continualharness` is a documented first-party scaffold.
- Why this is / is not agent-owned: model-provider inference is environmental, but the first-party runtime defines the operating loop, context/tool surface and return path while the model-driven actor owns substantive next-action choice.
- Evidence: [`README.md`](https://github.com/sethkarten/continual-harness/blob/bbab97ad73e460b7cd7c08527d10ced30cc03fbe/README.md); [`agents/PokeAgent.py`](https://github.com/sethkarten/continual-harness/blob/bbab97ad73e460b7cd7c08527d10ced30cc03fbe/agents/PokeAgent.py); [`run.py`](https://github.com/sethkarten/continual-harness/blob/bbab97ad73e460b7cd7c08527d10ced30cc03fbe/run.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: external model-provider or alternate external-CLI organization is not imported into this S1 claim.

## S2 — Coordination

- State: —
- Function: no material first-party disturbance-specific coordination loop among distinct viable S1 units is established at the declared boundary.
- Disturbance / variety regulated: local/custom subagents, tool calls and harness components may interact during one operating task, but no sibling-unit oscillation, contention or incompatible-assumption disturbance is detected and attenuated by a distinct relation.
- Decisive decision or feedback right: no S2-specific conflict/attenuation decision right is established.
- Decision owner: not established for S2.
- Supporting / enforcement mechanisms: subagent/tool registry, sequential operating loop, objective progression, custom subagent execution and persistence.
- Closure path: operational delegation/tool use returns results to the orchestrator; no separate inter-S1 disturbance → attenuation → feedback closure is established.
- Boundary reachability: subordinate subagent mechanisms are reachable, but plurality/topology is not treated as S2 by itself.
- Why this is / is not agent-owned: delegation and component interaction do not prove a coordination function without the required disturbance-specific relation.
- Evidence: [`agents/PokeAgent.py`](https://github.com/sethkarten/continual-harness/blob/bbab97ad73e460b7cd7c08527d10ced30cc03fbe/agents/PokeAgent.py); [`agents/tools/registry.py`](https://github.com/sethkarten/continual-harness/blob/bbab97ad73e460b7cd7c08527d10ced30cc03fbe/agents/tools/registry.py).
- Basis: structural negative search.
- Confidence: high.
- Caveats: a generated/custom subagent organization could create a downstream S2 relation, but it would require separate evidence.
- Distinct S1 units checked: main PokeAgent and subordinate/custom subagent executions reachable in the standard scaffold.
- Inter-S1 disturbance checked: task handoff/tool use and shared trajectory context do not establish mutual operational interference.
- Why generic communication/routing/delegation is insufficient: the main operating actor initiates subordinate work and receives a result; no independent coordination loop resolves a disturbance between viable units.

### Absence scope

- Surfaces inspected: scaffold/tool registry, PokeAgent subagent execution, objective progression, HarnessEvolver-created subagent state and runtime architecture docs.
- Plausible first-party paths checked: subagent plurality as S2; custom subagent handoff as S2; adaptation across multiple harness components as S2.
- Why no material first-party path remains: identified paths are composition, subordinate execution or adaptation rather than disturbance-specific inter-S1 coordination.

## S3 — Inside-and-now control

- State: —
- Function: no distinct first-party current-management function with a whole-organization present view and intervention authority is established.
- Disturbance / variety regulated: step scheduling, objective state, local replanning, context compaction and evolution timing constrain individual operation but do not constitute whole-system resource/commitment/current-priority management.
- Decisive decision or feedback right: no actor is established that receives a present whole-organization view and reallocates resources, priorities, commitments or accountability among operating units.
- Decision owner: not established for S3.
- Supporting / enforcement mechanisms: deterministic run lifecycle, adaptive evolution schedule, objective state and local operating/tool limits.
- Closure path: these mechanisms constrain or advance one current run; no distinct present-management judgment → cross-operation intervention → returned feedback loop closes.
- Boundary reachability: mechanisms are first-party and reachable, but classified by function rather than by names such as planner/orchestrator.
- Why this is / is not agent-owned: local operational planning and S4 adaptation do not automatically create S3 current control.
- Evidence: [`agents/PokeAgent.py`](https://github.com/sethkarten/continual-harness/blob/bbab97ad73e460b7cd7c08527d10ced30cc03fbe/agents/PokeAgent.py); [`agents/utils/harness_evolver.py`](https://github.com/sethkarten/continual-harness/blob/bbab97ad73e460b7cd7c08527d10ced30cc03fbe/agents/utils/harness_evolver.py).
- Basis: structural negative search.
- Confidence: high.
- Caveats: richer alternate PokeAgent modes expose planning helpers, but the selected `continualharness` boundary excludes built-in subagents and still does not establish installation-level S3 ownership.

### Absence scope

- Surfaces inspected: current objective/step handling, local subagent/planner surfaces, evolution scheduling, run state and scaffold configuration.
- Plausible first-party paths checked: PokeAgent orchestration as S3; objective replanning as S3; adaptive evolution scheduler as S3.
- Why no material first-party path remains: inspected paths regulate one continuing operation or future capability rather than managing the present organization as a whole.

## S3* — Complementary audit

- State: —
- Function: no material independent complementary audit/challenge function with corrective closure is established in the reviewed `continualharness` mode.
- Disturbance / variety regulated: trajectories, tool failures and current outcomes are inspected by the Refiner, but that evidence feeds S4 adaptation rather than a distinct current complementary-audit function.
- Decisive decision or feedback right: no separate audit actor with independent discrepancy judgment and corrective return is reachable in the selected scaffold.
- Decision owner: not established for S3*.
- Supporting / enforcement mechanisms: trajectory/run logs, evolution analysis and verifier/reflection subagents present in richer repository modes.
- Closure path: Refiner observations return as persistent future-capability changes under S4. `subagent_verify` is explicitly excluded from `continualharness` and cannot supply current audit closure here.
- Boundary reachability: `run.py` sets `EXCLUDE_BUILTIN_SUBAGENTS=1` for `continualharness`; the registry omits built-in subagent tools including `subagent_verify` under that setting.
- Why this is / is not agent-owned: repository-wide existence of verifier code is insufficient when it is outside the selected standard path.
- Evidence: [`run.py`](https://github.com/sethkarten/continual-harness/blob/bbab97ad73e460b7cd7c08527d10ced30cc03fbe/run.py); [`agents/tools/registry.py`](https://github.com/sethkarten/continual-harness/blob/bbab97ad73e460b7cd7c08527d10ced30cc03fbe/agents/tools/registry.py); [`agents/PokeAgent.py`](https://github.com/sethkarten/continual-harness/blob/bbab97ad73e460b7cd7c08527d10ced30cc03fbe/agents/PokeAgent.py).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: a downstream or alternate scaffold that enables a materially independent verifier is a different operating boundary and would require its own evidence; no such verifier is credited to the frozen Continual Harness mode.

### Absence scope

- Surfaces inspected: built-in verifier implementation, scaffold exclusion wiring, trajectory/evolution analysis and standard `continualharness` tool surface.
- Plausible first-party paths checked: `subagent_verify` as S3*; HarnessEvolver failure analysis as S3*; logs/metrics as S3*.
- Why no material first-party path remains: verifier is not reachable in the reviewed scaffold, while Refiner/log evidence belongs to adaptation/observability rather than current independent challenge-and-correction.

## S4 — Outside-and-then intelligence

- State: A
- Function: use accumulated operating evidence to autonomously choose persistent changes to the installed agent harness so subsequent S1 operation has changed future capability.
- Disturbance / variety regulated: recurring navigation/tool failures, stalled objectives, ineffective subagents/skills, prompt shortcomings, memory gaps/staleness and other patterns across recent trajectories.
- Decisive decision or feedback right: decide which prompt, subagent, skill and memory mechanisms should be created, changed or retired in response to accumulated evidence.
- Decision owner: the model-driven first-party HarnessEvolver/Refiner invoked automatically by the continuing runtime.
- Supporting / enforcement mechanisms: adaptive evolution schedule; recent-trajectory extraction; separate prompt/subagent/skill/memory evolution passes; persistent first-party stores; evolution log; bootstrap/load surfaces.
- Closure path: S1 trajectories/failures → scheduled HarnessEvolver → Refiner interpretation and chosen durable mutations → persistent prompt/subagent/skill/memory state → continuing PokeAgent consumes changed state on later steps without episode reset.
- Boundary reachability: `--scaffold continualharness --enable-prompt-optimization` is documented and wired as the reference Continual Harness mode; `PokeAgent` constructs and invokes `HarnessEvolver` directly.
- Why this is / is not agent-owned: deterministic scheduling decides when to inspect; the substantive adaptation choice is made by the model-driven Refiner and applied without requiring a human adaptation decision each cycle.
- External distinction: S4 evidence is drawn from the operating environment and accumulated trajectory/tool-result failures produced by S1 interaction, not merely from static repository configuration or an internal search objective detached from ongoing operation.
- Future / prospective distinction: the Refiner does not merely repair the just-completed action; it converts patterns across prior operation into durable changes intended to improve later steps of the same episode and, optionally, later bootstrapped runs.
- Adaptation option generated: the Refiner autonomously proposes and implements concrete prompt rewrites plus create/update/retire operations over subagents, skills and memory based on the observed trajectory window.
- Path back into current capability / S3: chosen mutations are written to first-party persistent harness stores and prompt state; the same continuing PokeAgent reloads/consumes those changed capability surfaces on subsequent S1 steps, while the evolution summary is returned into its continuing context. This is an S4→S1 capability return, not a claim of separate S3 ownership.
- Evidence: [`README.md`](https://github.com/sethkarten/continual-harness/blob/bbab97ad73e460b7cd7c08527d10ced30cc03fbe/README.md); [`agents/utils/harness_evolver.py`](https://github.com/sethkarten/continual-harness/blob/bbab97ad73e460b7cd7c08527d10ced30cc03fbe/agents/utils/harness_evolver.py); [`agents/PokeAgent.py`](https://github.com/sethkarten/continual-harness/blob/bbab97ad73e460b7cd7c08527d10ced30cc03fbe/agents/PokeAgent.py); [`System-Design/architecture/harness_evolver.md`](https://github.com/sethkarten/continual-harness/blob/bbab97ad73e460b7cd7c08527d10ced30cc03fbe/System-Design/architecture/harness_evolver.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: this S4 claim is specific to the concrete continuing organization. A separate meta-search system may have harness search/evolution as its S1 instead, as the Index records for Meta-Harness.

## S5 — Policy and identity

- State: —
- Function: no material identity/ultimate-policy authority loop is established for the running Continual Harness organization.
- Disturbance / variety regulated: scaffold selection, game/objective setup, model/backend choice, optimization enablement and fixed safety/tool constraints bound lower-level operation/adaptation.
- Decisive decision or feedback right: no actor is shown adjudicating an identity/ultimate-policy issue and returning a newly decided policy that changes the legitimate organizational constitution.
- Decision owner: not established for S5.
- Supporting / enforcement mechanisms: CLI/configuration, scaffold/tool registry, fixed prompt constraints, operator-selected model/backend and optimization flags.
- Closure path: operators/configuration establish lower-level constraints before or around operation; no runtime identity/policy issue → legitimate authority → returned constitutional policy closure is established.
- Boundary reachability: configuration and policy-like constraints are first-party and reachable, but remain lower-level setup/enforcement surfaces.
- Why this is / is not agent-owned: harness self-modification is bounded adaptation of operational capability, not evidence that the Refiner owns ultimate identity or policy defining what organization it may become.
- Evidence: [`README.md`](https://github.com/sethkarten/continual-harness/blob/bbab97ad73e460b7cd7c08527d10ced30cc03fbe/README.md); [`run.py`](https://github.com/sethkarten/continual-harness/blob/bbab97ad73e460b7cd7c08527d10ced30cc03fbe/run.py); [`agents/tools/registry.py`](https://github.com/sethkarten/continual-harness/blob/bbab97ad73e460b7cd7c08527d10ced30cc03fbe/agents/tools/registry.py).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: the Refiner can change prompts/skills/memory/subagents, but those delegated adaptation rights remain inside operator-selected scaffold/tool/safety boundaries and do not establish legitimate ultimate-policy authority.

### Absence scope

- Surfaces inspected: CLI/scaffold configuration, fixed tool/safety boundaries, prompt/bootstrap state and HarnessEvolver mutation scope.
- Plausible first-party paths checked: scaffold config as S5; model/backend selection as S5; self-modification/evolved prompt as S5.
- Why no material first-party path remains: these surfaces configure or adapt lower-level capability; none establishes ultimate organizational identity/policy adjudication and return.

## Recursion, autonomy, and evidence boundary

The reviewed organization is the concrete continuing Continual Harness runtime, not the repository maintainer organization and not every alternate scaffold bundled in the repository. Its environment-facing PokeAgent closes S1, while the separately purposed Refiner closes autonomous S4 by returning persistent future-capability changes into later operation.

The assessment intentionally does not infer S2 from subagent plurality, S3 from orchestration/objective planning, S3* from verifier code that the selected scaffold excludes, or S5 from the fact that S4 can rewrite prompts/skills/memory. Published benchmark gains and cross-method comparisons are excluded from ownership classification and belong, if admitted, only to the separate non-normative capability experiment.

## Admission conclusion

Proposed standalone vector:

`S1=A / S2=— / S3=— / S3*=— / S4=A / S5=—`.

This file remains `status: proposed`; canonical admission is a separate transaction.
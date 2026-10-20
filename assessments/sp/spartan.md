---
harness_id: spartan
project_name: Spartan
repository: https://github.com/CorticalComputer/Spartan
review_ref: 8f7b36a2326c0157a82040f8e04b474f4899c3da
reviewed_at: 2026-10-20
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: A
autonomy_s5: A
---

# Spartan

## Review boundary

- System in focus: Spartan's one persistent, independently model-driven local entity and its shipped Python cognitive loop, memory, tools, self-initiative, future GrandStrategy and Charter identity amendment. Optional multi-entity scripts and human dashboard were reviewed as modes, not automatically credited as a separate corporate metasystem.
- Purpose and identity: Persistent autonomous self-chosen tasks, long-horizon goals, first-person identity policy and machine-level actions across model-backend and process restarts.
- Relevant environment: Local host machine that README explicitly says is not sandboxed; configured external model provider, human machine operator, optional local MLX/llama.cpp, Soul on-disk archive, tools for console and files, GUI/headless mode, FileWatcher alerts, optional semantic memory/peer radio.
- Standard-distribution boundary: spartan.py cognitive_loop and TOOL_MAP; genesis_core.py role/policy/strategy prompts; spartan_config.yaml; local persistence, self-alerts, Memory/Soul and optional radio/drone/watchdog. First-party provider adapters suffice to link to a concrete running model when configured; no private past deployment receipts are borrowed.
- Credited operating / distribution surfaces: [source](https://github.com/CorticalComputer/Spartan/blob/8f7b36a2326c0157a82040f8e04b474f4899c3da/spartan.py); [source](https://github.com/CorticalComputer/Spartan/blob/8f7b36a2326c0157a82040f8e04b474f4899c3da/genesis_core.py); [source](https://github.com/CorticalComputer/Spartan/blob/8f7b36a2326c0157a82040f8e04b474f4899c3da/spartan_config.yaml); [source](https://github.com/CorticalComputer/Spartan/blob/8f7b36a2326c0157a82040f8e04b474f4899c3da/ltm.py); [source](https://github.com/CorticalComputer/Spartan/blob/8f7b36a2326c0157a82040f8e04b474f4899c3da/Tools/SpartanRadio.py); [source](https://github.com/CorticalComputer/Spartan/blob/8f7b36a2326c0157a82040f8e04b474f4899c3da/Tools/spawn_drone.py); [source](https://github.com/CorticalComputer/Spartan/blob/8f7b36a2326c0157a82040f8e04b474f4899c3da/Tools/terminate_drone.py); [source](https://github.com/CorticalComputer/Spartan/blob/8f7b36a2326c0157a82040f8e04b474f4899c3da/SpartanLink.py); [source](https://github.com/CorticalComputer/Spartan/blob/8f7b36a2326c0157a82040f8e04b474f4899c3da/spartan_watchdog.sh).
- Adjacent first-party surfaces excluded from ownership: README's past fleet/identity-performance claims, figures, logos, external paid provider internals, user's home system/operator, development work and human GUI decision authority; optional radio transport cannot on its own prove viable S2/S3 management.
- First-party operating / deployment modes considered: configured Claude/Gemini/OpenAI/Grok/MLX/llama.cpp providers, GUI and --headless entity loops, user/peer FileWatcher alerts, take_initiative, self-alert token cycles, persistent Soul and CMO/LTM, backend hot swap, optional mindfulness self-check, radio drones, human SpartanLink and watchdog.
- Recursion level: One continuing self-directing entity. Independent spawned Spartans may be separate S1s but no collective organizational higher recursion is assumed.
- Reviewed revision: CorticalComputer/Spartan@8f7b36a2326c0157a82040f8e04b474f4899c3da, Git tree b8fecce521fdd5959277fb236cb72cf5b109641b, GitHub repository ID 1294239187, Apache-2.0, created 2026-07-08T21:03:46Z, public, nonfork, nonarchived.
- Observation date: 2026-10-20.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

spartan.py repeatedly receives incoming collaborator and peer events, runs token-driven self-alerts or take_initiative prompts, constructs Genesis+Soul and volatile Layer-4 context, calls a concrete configured LLM provider, parses action JSON and dispatches tools, then stores observations for the next cycle. This source shows discretionary agent action ownership rather than a prescribed task sequence. [source](https://github.com/CorticalComputer/Spartan/blob/8f7b36a2326c0157a82040f8e04b474f4899c3da/spartan.py); [source](https://github.com/CorticalComputer/Spartan/blob/8f7b36a2326c0157a82040f8e04b474f4899c3da/spartan_config.yaml).

Persistence has explicitly differentiated planes: immutable developer Genesis Core, durable Charter of Self loaded *fully* into the system message, Grand Strategy with future horizons, Working Memory for current task, and episodic/LTM history. The model can choose update_grand_strategy so its next cycle reads a changed future objective; it can choose add_charter_entry and, after Sleep Cycle staging flush, future prompts read the new identity/constitutional principle. These are separate actual feedback paths for S4 and bounded self-S5. [source](https://github.com/CorticalComputer/Spartan/blob/8f7b36a2326c0157a82040f8e04b474f4899c3da/spartan.py); [source](https://github.com/CorticalComputer/Spartan/blob/8f7b36a2326c0157a82040f8e04b474f4899c3da/genesis_core.py); [source](https://github.com/CorticalComputer/Spartan/blob/8f7b36a2326c0157a82040f8e04b474f4899c3da/ltm.py).

Optional SpartanRadio links independently configured entities by alert files and whitelists; spawn/terminate scripts create or remove entity processes; SpartanLink is a human fleet panel; watchdog controls process restart/rollback. Their existence is not evidence of a separate S2 inter-unit conflict regulator, S3 whole-resource manager or independent S3* audit. [source](https://github.com/CorticalComputer/Spartan/blob/8f7b36a2326c0157a82040f8e04b474f4899c3da/Tools/SpartanRadio.py); [source](https://github.com/CorticalComputer/Spartan/blob/8f7b36a2326c0157a82040f8e04b474f4899c3da/Tools/spawn_drone.py); [source](https://github.com/CorticalComputer/Spartan/blob/8f7b36a2326c0157a82040f8e04b474f4899c3da/Tools/terminate_drone.py); [source](https://github.com/CorticalComputer/Spartan/blob/8f7b36a2326c0157a82040f8e04b474f4899c3da/SpartanLink.py); [source](https://github.com/CorticalComputer/Spartan/blob/8f7b36a2326c0157a82040f8e04b474f4899c3da/spartan_watchdog.sh).

## Operational model

The model-backed entity owns current tool decisions (S1), future Grand Strategy choices returned into current work (S4) and self-authoring its own constitutional Charter amendments returned into future cognitive contexts (S5) subject to fixed developer Genesis and physical host constraints. No human approval is needed for a local model-selected update; however this says nothing about external legal authority, personhood or society-wide governance.

## S1 — Operations

- State: A
- Function: Persistent autonomous local entity operating loop: select model-authored task actions, change files/console/memory and continue from returned tool observations without a new human prompt.
- Disturbance / variety regulated: Novel machine contents, external user or peer observations, tool errors, incomplete objectives, backend failures and bounded context history.
- Decisive decision or feedback right: Concrete configured LLM model chooses JSON action_type/arguments every cognitive cycle; first-party dispatch_actions calls execute_console, view, write_file, block_replace, update_working_memory and other handlers; observations feed next provider call. Initiative can invoke new cognition without user input.
- Decision owner: Configured model-backed Spartan entity owns agent task decisions. Deterministic Python dispatcher executes tool choices; human controls host/config/credentials but not each action.
- Supporting / enforcement mechanisms: ResilientProvider, continuous cognitive_loop, convert_history_to_messages, TOOL_MAP, dispatch_actions, persistent session, FileWatcher and self-alerts.
- Closure path: External observation or autonomous initiative → provider action objects → dispatch tools → action and result recorded to conversation history/state → subsequent prompt reincludes observations → new agent decision; process can persist/recover.
- Boundary reachability: The normal GUI and headless shipped paths both connect supported real providers to cognitive_loop and TOOL_MAP and expose proactive take_initiative; the model can act on actual new tool outputs and not only a static mock plan.
- Why this is / is not agent-owned: Counterfactually deleting the model removes task-contingent choice while leaving the Python dispatcher and watchdog; discretionary action is agent-owned.
- Evidence: [source](https://github.com/CorticalComputer/Spartan/blob/8f7b36a2326c0157a82040f8e04b474f4899c3da/spartan.py); [source](https://github.com/CorticalComputer/Spartan/blob/8f7b36a2326c0157a82040f8e04b474f4899c3da/genesis_core.py); [source](https://github.com/CorticalComputer/Spartan/blob/8f7b36a2326c0157a82040f8e04b474f4899c3da/spartan_config.yaml); [source](https://github.com/CorticalComputer/Spartan/blob/8f7b36a2326c0157a82040f8e04b474f4899c3da/README.md)
- Basis: First-party explicit code and supported runtime modes; no empirical provider invocation in this assessment.
- Confidence: High for S1 decision closure at one agent recursion.
- Caveats: Unsandboxed shell/filesystem access is deliberately unsafe; no reliability, security or deployment-performance claim.


## S2 — Coordination

- State: —
- Function: No evidenced inter-S1 conflict-damping relation among continuing viable autonomous entities; peer links transport messages but do not regulate collective variety.
- Disturbance / variety regulated: Spawned Spartan entities may send alerts, have competing objectives, overload contacts or fail independently.
- Decisive decision or feedback right: SpartanRadio whitelist and FileWatcher deliver alert messages; SpartanLink shows status to a human. No autonomously authoritative interentity commitment balancing or conflict resolution is defined.
- Decision owner: Individual entity models, deterministic inbox code, human SpartanLink operator; none assigned S2 mutual-regulation decision.
- Supporting / enforcement mechanisms: Radio file alerts, allowed sender list, rate limiting, spawn/terminate scripts and Link roster.
- Closure path: Message → target inbox/context → target entity discretionary actions; no inter-unit disturbance diagnosis → balancing S2 decision → corrected mutual operations.
- Boundary reachability: Agents may be independently viable, but their communication is not shown to attenuate clashes or oscillations across their goals.
- Why this is / is not agent-owned: All shipped routes are reachable as optional peer modes, but none closes S2.
- Evidence: [source](https://github.com/CorticalComputer/Spartan/blob/8f7b36a2326c0157a82040f8e04b474f4899c3da/Tools/SpartanRadio.py); [source](https://github.com/CorticalComputer/Spartan/blob/8f7b36a2326c0157a82040f8e04b474f4899c3da/Tools/spawn_drone.py); [source](https://github.com/CorticalComputer/Spartan/blob/8f7b36a2326c0157a82040f8e04b474f4899c3da/Tools/terminate_drone.py); [source](https://github.com/CorticalComputer/Spartan/blob/8f7b36a2326c0157a82040f8e04b474f4899c3da/SpartanLink.py); [source](https://github.com/CorticalComputer/Spartan/blob/8f7b36a2326c0157a82040f8e04b474f4899c3da/spartan.py)
- Basis: Bounded negative from direct first-party messaging/fleet review.
- Confidence: Medium-high.
- Caveats: Private real-world fleets are not credited as source evidence.

### Absence scope

- Surfaces inspected: SpartanRadio, FileWatcher, spawn/terminate drone, optional SpartanLink and multi-entity README instructions.
- Plausible first-party paths checked: Checked peer exchange, sender allowlists, fleet UI and autonomous spawning as candidate interentity coordination loops.
- Why no material first-party path remains: First-party only transports messages and manages process access; no interference-specific coordination owner, moderation judgment or returned changes to several independently viable entities' commitments.


## S3 — Inside-and-now control

- State: —
- Function: No separate whole-current discretionary manager of several autonomous entities' resources, priorities, commitments and accountability.
- Disturbance / variety regulated: Child process failure, resource/budget shortage, changes to single entity's task focus and competing peer demands.
- Decisive decision or feedback right: An entity edits its own Working Memory and Grand Strategy and can spawn or terminate drones. Deterministic watchdog restarts or rolls back crashes; this is not a binding, organization-wide manager with a whole portfolio view.
- Decision owner: Single entity controls its own work, watchdog/launch scripts enforce host lifecycle; collaborator may operate Link but does not receive a supported standing S3 parent mandate.
- Supporting / enforcement mechanisms: WM/GS, spawn_drone, terminate_drone, SpartanLink status UI, resilience/watchdog.
- Closure path: Per-entity observation → local task update; local crash → restart/rollback. No whole-system current-state report → accountable allocation decision → return changing different viable S1 units.
- Boundary reachability: Single-agent goal management is not an independently authorized current management layer; optional drone creation does not automatically grant their resource/priority authority.
- Why this is / is not agent-owned: Optional scripts and peer interfaces were inspected; none provides a separately functioning S3 executive.
- Evidence: [source](https://github.com/CorticalComputer/Spartan/blob/8f7b36a2326c0157a82040f8e04b474f4899c3da/spartan.py); [source](https://github.com/CorticalComputer/Spartan/blob/8f7b36a2326c0157a82040f8e04b474f4899c3da/Tools/spawn_drone.py); [source](https://github.com/CorticalComputer/Spartan/blob/8f7b36a2326c0157a82040f8e04b474f4899c3da/Tools/terminate_drone.py); [source](https://github.com/CorticalComputer/Spartan/blob/8f7b36a2326c0157a82040f8e04b474f4899c3da/SpartanLink.py); [source](https://github.com/CorticalComputer/Spartan/blob/8f7b36a2326c0157a82040f8e04b474f4899c3da/spartan_watchdog.sh)
- Basis: Bounded negative after checking strongest fleet and human-parent paths.
- Confidence: Medium-high.
- Caveats: A separately governed deployment could supply such an owner beyond the pinned distribution.

### Absence scope

- Surfaces inspected: Local GS/WM, drones, CLI, watchdog, provider fallback, SpartanLink and peer communications.
- Plausible first-party paths checked: Checked whole-fleet view, child lifecycle control and human collaboration as S3 or parent-governed current executive.
- Why no material first-party path remains: No independent whole-current managerial reporting view and discretionary resource/commitment decisions returned to separate viable S1s; all observed functions stay agent-local or deterministic process lifecycle.


## S3* — Complementary audit

- State: —
- Function: No independent complementary audit of S3 ordinary management claims with distinct direct-reality access and returned corrective S3 decision.
- Disturbance / variety regulated: Hallucinated model assertions, incorrect tools, bad persistence, crashed process, mistaken peer status.
- Decisive decision or feedback right: Mindfulness second-pass critiques the same model's draft. Watchdog verifies process health. Neither is an independent reality auditor over an S3 manager.
- Decision owner: Same Spartan model and deterministic lifecycle monitors, not separately mandated auditor.
- Supporting / enforcement mechanisms: Optional two-pass mindfulness, history observations, LTM, watchdog and human UI.
- Closure path: Model draft → same model correction → next own task answer, or watchdog crash → restart. No S3 report → independent field finding → S3 correction.
- Boundary reachability: Self-critique does not satisfy independence and task observation does not establish organizational management audit.
- Why this is / is not agent-owned: Mindfulness and peer status are first-party but do not implement the audit relationship.
- Evidence: [source](https://github.com/CorticalComputer/Spartan/blob/8f7b36a2326c0157a82040f8e04b474f4899c3da/spartan.py); [source](https://github.com/CorticalComputer/Spartan/blob/8f7b36a2326c0157a82040f8e04b474f4899c3da/genesis_core.py); [source](https://github.com/CorticalComputer/Spartan/blob/8f7b36a2326c0157a82040f8e04b474f4899c3da/spartan_watchdog.sh); [source](https://github.com/CorticalComputer/Spartan/blob/8f7b36a2326c0157a82040f8e04b474f4899c3da/SpartanLink.py)
- Basis: Bounded negative after checking all available audit-like surfaces.
- Confidence: High.
- Caveats: Do not deny value of task checking or infer an external reviewer without source.

### Absence scope

- Surfaces inspected: Mindfulness optional self-review, tool results, peer alerts, LTM and watchdog.
- Plausible first-party paths checked: Checked complementary reality-access independent from normal management report and who receives findings.
- Why no material first-party path remains: No identifiable independent S3 management report to challenge, external audit owner, or corrective return to S3; self-review and crash recovery are within task/process boundary.


## S4 — Outside-and-then intelligence

- State: A
- Function: Outside-and-then future intelligence over the entity's prospective objectives and operating capability.
- Disturbance / variety regulated: New external file/peer/tool information, changing research goals, memories/ideas about opportunities and threats, future provider or tool limits.
- Decisive decision or feedback right: Agent model may on its own examine observations, choose time-horizon GrandStrategy objectives, issue update_grand_strategy, then use the changed plan to guide WorkingMemory and new tools. Agent can also switch backend or edit scripts for capability adjustment.
- Decision owner: Persistent autonomous entity owns future-goal judgment; developer Genesis provides framing and runtime carries out writes.
- Supporting / enforcement mechanisms: Continuous initiative scan, first-party file/console observation, long-term semantic recall, horizon-labeled Genesis strategy contract, GS update tool, L4 prompt assembly.
- Closure path: Outside input/recall → model selects prospective strategic revision → update_grand_strategy persists state → next assemble_layer_4 presents revised GS → model reworks current WM and actions.
- Boundary reachability: The current normal cognitive loop actually uses model-selected GS edits and then rebuilds next-cycle context with that GS; no external human must accept the entity's future objective.
- Why this is / is not agent-owned: The actor chooses what future goal to pursue; fixed state writer is merely a mechanism, and the returned goal can affect subsequent action.
- Evidence: [source](https://github.com/CorticalComputer/Spartan/blob/8f7b36a2326c0157a82040f8e04b474f4899c3da/spartan.py); [source](https://github.com/CorticalComputer/Spartan/blob/8f7b36a2326c0157a82040f8e04b474f4899c3da/genesis_core.py); [source](https://github.com/CorticalComputer/Spartan/blob/8f7b36a2326c0157a82040f8e04b474f4899c3da/ltm.py); [source](https://github.com/CorticalComputer/Spartan/blob/8f7b36a2326c0157a82040f8e04b474f4899c3da/spartan_config.yaml)
- Basis: Source-backed prospective option and returned operating feedback at the single-entity recursion.
- Confidence: Medium-high.
- Caveats: Unmeasured plan quality; not a claim of company-level foresight or effective market intelligence.
- External distinction: FileWatcher, tools and LTM expose changing host/peer/external observations, while initiative mode can prompt scanning for actionable objectives.
- Future / prospective distinction: Genesis explicitly distinguishes weeks/months/years/decades horizons and separates Grand Strategy from immediate Working Memory.
- Adaptation option generated: Agent-selected update_grand_strategy may introduce or replace future-oriented objectives, and other supported tools can switch backend or change technical files.
- Path back into current capability / S3: Updated GrandStrategy is reinserted into Layer 4 every next cognitive step and drives current WM/tool work. No independent S3 is claimed; the feedback returns directly to current S1.


## S5 — Policy and identity

- State: A
- Function: Single-entity foundational identity and ultimate internal policy: self-authored Charter of Self directs the entity's purpose, constraints and subsequent strategy.
- Disturbance / variety regulated: New substantial experiences or identity conflicts after continuous operation/backend changes can challenge standing self-principles.
- Decisive decision or feedback right: Agent model can choose add_charter_entry with a selected MANDATE, CONSTRAINT, PRINCIPLE, DIRECTIVE or other charter entry and rationale; first-party code stages then flushes it to Soul/CharterOfSelf.md, which is fully included in later system prompts.
- Decision owner: At this local entity recursion, the agent owns self-charter amendment decisions within developer's fixed Genesis Core/host envelope. Human host has physical sovereignty but no separately closed first-party parent-S5 decision loop is credited.
- Supporting / enforcement mechanisms: add_charter_entry in TOOL_MAP, staged knowledge buffer, Sleep Cycle flush, Charter file unlimited load into assemble_system_prompt, Genesis identity→strategy→tactics hierarchy.
- Closure path: Self-deliberated policy issue → model-authored charter amendment → staged and flushed to disk → complete Charter reappears in future system prompt → subsequent strategic and operative decisions use self-authored constitutional rules.
- Boundary reachability: Charter edit is a supported real agent action path, not documentation alone, and the stored entry returns as an authoritative identity layer in a future normal provider call.
- Why this is / is not agent-owned: Agent selects and authors enduring policy rather than merely executing a human configured toggle; fixed Genesis and host control bound this sovereignty to its own agent recursion.
- Evidence: [source](https://github.com/CorticalComputer/Spartan/blob/8f7b36a2326c0157a82040f8e04b474f4899c3da/spartan.py); [source](https://github.com/CorticalComputer/Spartan/blob/8f7b36a2326c0157a82040f8e04b474f4899c3da/genesis_core.py); [source](https://github.com/CorticalComputer/Spartan/blob/8f7b36a2326c0157a82040f8e04b474f4899c3da/README.md)
- Basis: Explicit local identity ownership and return path, not a metaphysical/organizational-personhood claim.
- Confidence: Medium-high.
- Caveats: Genesis is developer-defined and immutable by normal prompt contract; amendments are additive and need successful flush, and host can ultimately stop/edit the system.
- Identity / ultimate-policy issue: Whether a new durable principle, mandate, constraint or directive should change the single entity's own enduring purpose, rights, obligations or identity.
- Ultimate authority in each claimed mode: In autonomous entity mode the model authors its own Charter amendments. This is not legal sovereignty or authority over host machine and no parent S5 is claimed.
- Return-to-operation path: add_charter_entry → staging buffer → Sleep Cycle flush → Soul/CharterOfSelf.md → full Charter loaded on next system prompt → identity-guided GS/WM/current tool choices.



## Recursion

This entity closes S1, S4 and self-authored S5 at its own recursion. It does not establish a corporate S5 for a whole multi-agent organization. Peer file links and drone tools do not imply current management and need separately credible S2/S3/S3* evidence. A self-maintained future Grand Strategy is not the same as managerial allocation among multiple independently viable S1 units.

## Variety and escalation

New host/user/peer/tool inputs and prior memories can change current tool actions; long-term signals can change GS goals, and rare identity-level dilemmas can change Charter principles. Backend failover, memory condensation, process watchdog and token self-alert mechanisms support continuity without inheriting function ownership. No special corporate algedonic signal/parent-control claim is made.

## Evidence gaps

- All source claims are bounded to the pinned Git commit and shipped first-party model action/persistence/prompt assembly paths. Self-described historical machine operation in README is not independently verified.
- The review deliberately did **not run** the autonomous unsandboxed Spartan agent, which can access local console, modify code and spawn processes. Python compileall PASS establishes source syntax only, not model decision quality.
- S4 and S5 grades rely on documented model-selected state changes with reconstructable future prompt return. They do not claim effective foresight, actual constitutional wisdom, corporate sovereignty or nonhuman personhood.
- Fixed developer Genesis text and human host rights constrain this entity's S5 authority; durable Charter amendment requires successful Sleep Cycle flush. Those limitations are not elided.

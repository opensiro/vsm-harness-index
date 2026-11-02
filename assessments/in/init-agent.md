---
harness_id: init-agent
project_name: INIT-Agent
repository: https://github.com/nagisanzenin/INIT-Agent
review_ref: 1b8b407d2716739a4cfaff6a1751c2f968425edb
reviewed_at: 2026-11-02
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: P
autonomy_s3_star: ?
autonomy_s4: A
autonomy_s5: P
---

# INIT-Agent

## Review boundary

- System in focus: One installed INIT coding agent, comprising its mutable agent zone, kernel and separately protected Root supervisor.
- Purpose and identity: Execute coding tasks while allowing agent-authored changes to its own prompts, tools and compiled core under a protected owner charter.
- Relevant environment: Local workspaces, user requests, model providers, tests, budgets, process health and evolving task/tool needs.
- Standard-distribution boundary: First-party `init-agent` and `init-root` installed runtime and documented gated/free self-extension paths; no external agent providers' internal organizations.
- Credited operating / distribution surfaces: `seed/src/loop`, `seed/src/tools`, `kernel`, Root process/charter/owner channel, self-edit/promote gates and sealed checks available in the installed system.
- Adjacent first-party surfaces excluded from ownership: Development fixtures, prerecorded experiments, benchmark orchestration, release CI, repository maintainers and synthetic demonstrations; their results corroborate but do not supply runtime decision owners.
- First-party operating / deployment modes considered: Normal coding loop; agent-authored gate/promote/evolve path; owner status/charter/panic/rollback channel; gated and free monitoring modes.
- Recursion level: One deployed agent-and-Root operating system. Separate spawned processes and optional bounded delegate are not automatically viable child organizations.
- Reviewed revision: `1b8b407d2716739a4cfaff6a1751c2f968425edb`.
- Observation date: 2026-11-02.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The Rust `seed` body owns model requests, iterative tool use, observations and task context. The kernel supervises body startup and checks agent-authored source changes before hot-swapping the body. `init-root` is outside the modifiable agent zone: it brokers launches, keys, charter access constraints, lineage, sealed test tasks, recovery snapshots and owner commands. The agent may change its body and extensions, but cannot edit the Root or read sealed evaluation data. The documented release/fixture/qualification trees are evidence and development machinery, not additional deployed VSM actors.

## Operational model

The model actor performs coding work through tool-observation cycles and may propose durable changes to its own capabilities. Root and kernel enforce a separate owner-selected safety boundary; human owner operations can return current recovery and ultimate charter decisions. The separate Root's automated sealed regression check is a substantive candidate complementary audit path, but its deterministic verdict is not itself evidence that an autonomous audit actor owns the discretionary S3* judgment.

## S1 — Operations

- State: A
- Function: Convert coding requests into tool-mediated work, revise actions after observed outcomes and return results.
- Disturbance / variety regulated: Changing code/task state, model results, tool failures, user steering and interrupted sessions.
- Decisive decision or feedback right: Select subsequent code/tool actions and responses from the model's observations.
- Decision owner: Mutable agent-body model in the normal supported session.
- Supporting / enforcement mechanisms: Model I/O types, tool dispatcher, context/log, kernel process lifecycle, Root sandbox and egress proxy.
- Closure path: Input/context → model-selected tool call → dispatched tool result in the conversation → next model decision.
- Boundary reachability: The installed `init-agent` launches the shipped body loop through the kernel; tool use is not borrowed from the provider's internal agent service.
- Why this is / is not agent-owned: The first-party model chooses substantive tool use and adjusts after feedback; Root only constrains execution and supplies transport.
- Evidence: [seed loop](https://github.com/nagisanzenin/INIT-Agent/blob/1b8b407d2716739a4cfaff6a1751c2f968425edb/seed/src/loop/mod.rs), [model tool-call types](https://github.com/nagisanzenin/INIT-Agent/blob/1b8b407d2716739a4cfaff6a1751c2f968425edb/seed/src/model.rs), [tool dispatcher](https://github.com/nagisanzenin/INIT-Agent/blob/1b8b407d2716739a4cfaff6a1751c2f968425edb/seed/src/tools/mod.rs), [body boot](https://github.com/nagisanzenin/INIT-Agent/blob/1b8b407d2716739a4cfaff6a1751c2f968425edb/seed/src/main.rs).
- Basis: structural.
- Confidence: high.
- Caveats: Source inspection only; no paid provider or installed-session E2E execution was performed.

## S2 — Coordination

- State: —
- Function: No separately evidenced first-party inter-S1 interference attenuation loop at this chosen recursion.
- Disturbance / variety regulated: Potential interference among multiple independent S1 operations.
- Decisive decision or feedback right: No function-specific inter-S1 conflict-resolution right established.
- Decision owner: None evidenced for S2 in the normal distribution.
- Supporting / enforcement mechanisms: Bounded delegation, serial body turn execution, process/sandbox separation and ordinary result return.
- Closure path: Delegation and result reporting support S1 task decomposition, without an evidenced S2-specific coordination correction.
- Why this is / is not agent-owned: Multiple processes and a delegate tool do not independently demonstrate an interference/oscillation witness and subsequent coordination feedback.
- Evidence: [delegate implementation](https://github.com/nagisanzenin/INIT-Agent/blob/1b8b407d2716739a4cfaff6a1751c2f968425edb/seed/src/loop/delegate.rs), [delegate tool](https://github.com/nagisanzenin/INIT-Agent/blob/1b8b407d2716739a4cfaff6a1751c2f968425edb/seed/src/tools/delegate.rs), [system architecture](https://github.com/nagisanzenin/INIT-Agent/blob/1b8b407d2716739a4cfaff6a1751c2f968425edb/README.md).
- Basis: structural.
- Confidence: medium.
- Caveats: This does not assert that a custom future fleet cannot implement S2.

### Absence scope

- Surfaces inspected: Shipped body loop/delegate, Root/kernel responsibilities and README operating modes.
- Plausible first-party paths checked: Nested delegate, process separation, task result return and Root supervision.
- Why no material first-party path remains: These are single-task delegation, isolation or current control; no shipped inter-S1 interference detector, attenuating coordination decision and returned coordination effect were identified at the deployed boundary.

## S3 — Inside-and-now control

- State: P
- Function: Parent-controlled current recovery and runtime constraint changes over the one live agent-and-Root system.
- Disturbance / variety regulated: Unsafe operation, health regressions, continued erroneous work, spend/exposure concerns and failed self-changes.
- Decisive decision or feedback right: Inspect system status and select owner panic/stop/recovery/rollback rather than simply accept the current run.
- Decision owner: Legitimate human operator via the Root's owner channel; Root executes the returned choice.
- Supporting / enforcement mechanisms: Root status snapshot, owner socket/CLI, signed lineage, sandbox, watchdog and snapshot restore.
- Closure path: Root current status and warnings → owner chooses `panic`, `stop`, `resume` or rollback → Root changes currently permitted execution/recovered tuple.
- Boundary reachability: `init-root status`, `attach`, `panic`, `resume` and Root recovery are supported installed owner commands, not contributor CI or a suggested external management plugin.
- Why this is / is not agent-owned: The parent selects consequential whole-system intervention; deterministic Root enforcement and autonomous threshold rollback alone are not credited as agent-owned S3 discretion.
- Whole-system current view: Root publishes live slot/mode/level/charter, process state, spend, snapshots and fault/lineage status for the deployed system.
- Current-control decision scope: Stop or resume current work and restore/restrict the active body state and access envelope.
- Evidence: [Root owner CLI](https://github.com/nagisanzenin/INIT-Agent/blob/1b8b407d2716739a4cfaff6a1751c2f968425edb/root/crates/init-root/src/cli.rs), [Root contract](https://github.com/nagisanzenin/INIT-Agent/blob/1b8b407d2716739a4cfaff6a1751c2f968425edb/docs/root/root.md), [README controls](https://github.com/nagisanzenin/INIT-Agent/blob/1b8b407d2716739a4cfaff6a1751c2f968425edb/README.md).
- Basis: structural.
- Confidence: medium.
- Caveats: Parent path is local owner control, not an autonomous multi-agent S3 or organizational governance of repository contributors.

## S3* — Complementary audit

- State: ?
- Function: A Root-sealed, agent-inaccessible regression check of evolved bodies is present; its ownership as the Methodology's discretionary complementary S3* audit remains unresolved.
- Disturbance / variety regulated: Self-reported successful mutation concealing functional regression or benchmark gaming.
- Decisive decision or feedback right: Challenge the current body with unseen tasks and return regression/rollback decisions.
- Decision owner: Sealed deterministic Root evaluator executes tests and thresholds; no separately evidenced autonomous discretionary audit judge is identified.
- Supporting / enforcement mechanisms: Root-only sealed task store, canaries, paired comparisons, noise floors, signed audit records and rollback mechanism.
- Closure path: Sealed task results → deterministic regression verdict → rollback/demotion or accepted audited pointer, affecting subsequent body operation.
- Why this is / is not agent-owned: Complementary first-party access and correction exist, but the recorded judge is deterministic enforcement. Further bounded analysis is needed to decide whether the established function's published ownership is `C`, `—` or unresolved under Methodology 0.3.7.
- Evidence: [Root sealed evaluation contract](https://github.com/nagisanzenin/INIT-Agent/blob/1b8b407d2716739a4cfaff6a1751c2f968425edb/docs/root/sealed-eval.md), [Root module wiring](https://github.com/nagisanzenin/INIT-Agent/blob/1b8b407d2716739a4cfaff6a1751c2f968425edb/root/crates/init-root/src/main.rs), [promotion gate contract](https://github.com/nagisanzenin/INIT-Agent/blob/1b8b407d2716739a4cfaff6a1751c2f968425edb/docs/kernel/gate.md).
- Basis: explicit and structural.
- Confidence: low for ownership, high for shipped sealed infrastructure.
- Caveats: This is not an independent reviewer run or proof of successful model performance.

## S4 — Outside-and-then intelligence

- State: A
- Function: Propose and deploy changes to the agent's future operating capabilities from observed task/tool limitations.
- Disturbance / variety regulated: Changing requirements, repeated tool failures, inefficiencies and capability mismatch with prospective work.
- Decisive decision or feedback right: The model chooses edits to its own prompt, extension/tool set or compiled body and requests their promotion.
- Decision owner: Agent model authors the adaptation option; Root/kernel safety and performance gates may reject it without owning option generation.
- Supporting / enforcement mechanisms: Editable body/extension worktree, `initctl promote`, G0–G4 tests, staged process hot-swap, lineage and safety rollback.
- Closure path: Observed limitations → agent-authored source/extension change → promotion/gates → accepted live body/tool capability used on later turns; rejected change returns evidence for another attempt.
- Boundary reachability: Self-edit is a documented native agent capability; released kernel/Root perform the promotion and can preserve conversation state through a core swap.
- Why this is / is not agent-owned: The source modification and future option are model-selected; a fixed compiler/test/holdout guard has veto power but does not independently choose the proposed enhancement.
- External distinction: Performance and tool demands of tasks/environment relative to present agent capabilities.
- Future / prospective distinction: Revised future tool/core behavior, not merely saving a current conversation.
- Adaptation option generated: New/modified skills, tools and Rust body code.
- Path back into current capability / S3: Accepted promotion changes the running body; Root can roll it back based on current outcome.
- Evidence: [README self-evolution workflow](https://github.com/nagisanzenin/INIT-Agent/blob/1b8b407d2716739a4cfaff6a1751c2f968425edb/README.md), [agent evolution contract](https://github.com/nagisanzenin/INIT-Agent/blob/1b8b407d2716739a4cfaff6a1751c2f968425edb/docs/evolution.md), [kernel gate contract](https://github.com/nagisanzenin/INIT-Agent/blob/1b8b407d2716739a4cfaff6a1751c2f968425edb/docs/kernel/gate.md), [extension authoring](https://github.com/nagisanzenin/INIT-Agent/blob/1b8b407d2716739a4cfaff6a1751c2f968425edb/docs/ext/authoring.md).
- Basis: explicit and structural.
- Confidence: medium.
- Caveats: Shipped self-edit closure is not a claim of measured net capability gain; the README explicitly notes that persistent benefit is not yet demonstrated.

## S5 — Policy and identity

- State: P
- Function: Keep ultimate authority over the agent's identity and non-editable safety/extension charter outside the self-modifying actor.
- Disturbance / variety regulated: Agent efforts to redefine its own authority, protected access and evolution permissions.
- Decisive decision or feedback right: Select and explicitly apply the Root charter defining the owner's non-negotiable authority envelope.
- Decision owner: Human owner; the independent Root validates, signs and enforces the choice.
- Supporting / enforcement mechanisms: Owner-only `charter.toml`, charter checks/digest, active charter state, Root sandbox/permission rules and separation from the agent zone.
- Closure path: Owner changes charter and invokes `charter check --apply` → Root validates/activates it → the next runtime decisions are constrained by the new authoritative charter.
- Boundary reachability: The installed Root CLI exposes owner-only charter check/apply while the mutable agent is sandboxed away from Root home.
- Why this is / is not agent-owned: The self-modifying agent does not control the protected charter or Root. Runtime permission requests alone were not counted; the evidenced claim is the explicit higher-level charter authority and return to operation.
- Identity / ultimate-policy issue: Whether and under which hard non-editable constraints the agent may alter itself, gain access or survive a regression.
- Ultimate authority in each claimed mode: Human owner only; Root records/enforces the decision.
- Return-to-operation path: Active charter affects subsequent agent-zone sandbox and promotion operations.
- Evidence: [Root charter implementation](https://github.com/nagisanzenin/INIT-Agent/blob/1b8b407d2716739a4cfaff6a1751c2f968425edb/root/crates/init-root/src/charter.rs), [owner apply CLI](https://github.com/nagisanzenin/INIT-Agent/blob/1b8b407d2716739a4cfaff6a1751c2f968425edb/root/crates/init-root/src/cli.rs), [Root architecture](https://github.com/nagisanzenin/INIT-Agent/blob/1b8b407d2716739a4cfaff6a1751c2f968425edb/docs/root/root.md).
- Basis: explicit and structural.
- Confidence: medium.
- Caveats: Does not infer project-level S5 governance from the existence of maintainers, contributors or release approvals.

## Distributed OSS parent arrangement

The assessed parent is the local installed owner, not a repository-wide maintainer collective. Public development/release governance does not automatically supply per-deployment S3/S5 ownership.

## Self-hosted and non-human modes

The owner can choose gated/free mutation policies and current access modes; none grant the agent authority over the immutable Root. No unsupported autonomous S5 mode is inferred. Provider model selection is a dependency, not an external VSM actor that donates functions.

## Recursion

Root/kernel/body are distinct responsibility layers within one agent operating system. A bounded delegate does not have evidenced independent environment plus full metasystem; no second viable recursion is asserted.

## Variety and escalation

The Root mediates external API/key/OS risk, can reject evolution, and returns safe fallback or owner attention. Watchdog alerts are not independently counted as an algedonic VSM function or as agent-owned current-control judgment.

## Evidence gaps

The specific residual question for S3* is whether a sealed deterministic, independent-instrumentation regression evaluator with integrated rollback counts as a first-party audit-specific constructor (`C`) or only support/enforcement without autonomous audit ownership; a fresh source-first semantic adjudication of that boundary is needed. No live paid provider run, native installation or benchmark result was reproduced. All claims are bounded to the exact pinned source and documented shipped modes.

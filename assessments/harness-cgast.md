---
harness_id: harness-cgast
project_name: Harness
repository: https://github.com/cgast/harness
review_ref: b3a9edde79f332f86189da742c5313f25f210b79
reviewed_at: 2026-09-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-30
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Harness

## Review boundary

- System in focus: one first-party Harness deployment at pinned revision `b3a9edde79f332f86189da742c5313f25f210b79`, including the core model/tool loop, state, tools, persistence, plugin/event surfaces, optional shipped memory and human-feedback plugins, and the supported CLI/server/desktop host modes.
- Purpose and identity: turn user tasks into model-selected, tool-mediated outcomes through a provider-neutral agent runtime with persistent state and plugin-extensible control surfaces.
- Relevant environment: users/operators, configured LLM providers, host filesystem/process/network resources, plugin-supplied capabilities, persisted sessions/memory, and tool-mediated external systems.
- Standard-distribution boundary: shipped runtime and bundled first-party plugins reachable through ordinary CLI/server/desktop operation. Repository-development CI, security review documents, examples, and the unimplemented heartbeat plan are adjacent and do not supply runtime ownership.
- Credited operating / distribution surfaces: `packages/core` loop/state/prompt/tool/event/persistence surfaces; shipped CLI/server/desktop hosts; bundled plugins when enabled through the documented plugin configuration.
- Adjacent first-party surfaces excluded from ownership: `.github` build/release workflows, `SECURITY_ASSESSMENT.md`, contributor/development machinery, examples, and `.claude/plan.md` heartbeat design because the frozen tree contains the design plan rather than an implemented heartbeat operating path.
- First-party operating / deployment modes considered: CLI task execution, HTTP/server execution, desktop execution, plugin-enabled runs, persistent memory mode, and human-feedback/review mode.
- Recursion level: one Harness deployment. One active model/tool task loop is the established S1 operational unit; multiple sessions or host invocations do not by themselves establish multiple mutually coordinating S1 units.
- Reviewed revision: `b3a9edde79f332f86189da742c5313f25f210b79`.
- Observation date: 2026-09-30.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Harness is a TypeScript monorepo centered on `packages/core`. The core loop assembles a system prompt from the selected soul, active skills, state and tools; calls a configured model provider; accepts streamed text/tool calls; executes requested tools; writes tool results back into conversation state; and repeats until the model produces a final response or a deterministic termination condition fires. CLI, server and Electron desktop surfaces host this same runtime.

An event bus exposes modifiable hooks around agent start, prompt assembly, LLM requests and tool requests/results. Plugins can add tools/providers and may block or transform selected actions. Persistence stores sessions and memory. The bundled memory plugin exposes `memory_store`/`memory_recall` and injects stored user facts into later prompts. The feedback manager can pause one active agent state while a human supplies confirmation, choice, text, artifact review or structured feedback.

These are substantial harness mechanisms, but the assessment separates them from higher VSM functions. The frozen runtime does not establish a second distinct operational S1 whose interference with the first is attenuated by an S2 loop. Current status, iteration limits, timeouts, plugin aborts and local human approvals regulate one task loop rather than supplying a separate whole-deployment S3 regulator. Events, telemetry, persisted transcripts and repository security review do not form an independent complementary S3* path. Cross-session memory changes later context, but the Profile explicitly requires more than event ingestion or memory update for S4: no external-and-prospective adaptation-option loop returning into current capability was found. Finally, soul YAML contains personality, values and boundaries, but a static/selectable system prompt or policy file is not itself S5; no runtime identity/ultimate-policy issue → legitimate parent decision → returned authoritative policy loop is established.

Primary evidence:

- [`README.md`](https://github.com/cgast/harness/blob/b3a9edde79f332f86189da742c5313f25f210b79/README.md) — standard runtime architecture, host modes, state/persistence/plugins, souls and documented loop.
- [`packages/core/src/engine/loop.ts`](https://github.com/cgast/harness/blob/b3a9edde79f332f86189da742c5313f25f210b79/packages/core/src/engine/loop.ts) — model/tool/observation feedback loop, deterministic termination, state changes and plugin interception.
- [`packages/core/src/engine/prompt-assembler.ts`](https://github.com/cgast/harness/blob/b3a9edde79f332f86189da742c5313f25f210b79/packages/core/src/engine/prompt-assembler.ts) — soul/skills/history/tools assembly and modifiable prompt hook.
- [`packages/core/src/feedback/manager.ts`](https://github.com/cgast/harness/blob/b3a9edde79f332f86189da742c5313f25f210b79/packages/core/src/feedback/manager.ts) — per-run human feedback pause/return path inspected for possible parent S3/S5 evidence.
- [`plugins/memory/src/index.ts`](https://github.com/cgast/harness/blob/b3a9edde79f332f86189da742c5313f25f210b79/plugins/memory/src/index.ts) — model-addressable persistent facts and later prompt injection inspected for S4.
- [`packages/core/src/soul/loader.ts`](https://github.com/cgast/harness/blob/b3a9edde79f332f86189da742c5313f25f210b79/packages/core/src/soul/loader.ts) — static/selectable soul identity document loading inspected for S5.
- [`.claude/plan.md`](https://github.com/cgast/harness/blob/b3a9edde79f332f86189da742c5313f25f210b79/.claude/plan.md) — heartbeat is an implementation plan at the frozen ref and is excluded from operating evidence.

## Operational model

A user task becomes one model-governed operational loop. The model chooses whether to answer or call a tool; returned tool evidence enters state and changes the next model turn. Deterministic runtime limits, plugins, timeouts, workspace/sandbox restrictions and optional human feedback constrain this loop. Persistence and memory carry selected information across sessions, while a selected soul supplies static identity/context constraints. No qualifying metasystemic function above S1 is closed at the assessed deployment boundary.

## S1 — Operations

- State: A
- Function: transform a user objective into an answer or tool-mediated environmental result through repeated model decision, tool execution and observation feedback.
- Disturbance / variety regulated: task ambiguity, changing conversation state, model uncertainty, tool availability/results/failures, filesystem/network state, plugin constraints and user-provided evidence.
- Decisive decision or feedback right: choose the substantive next response or tool action and revise subsequent behavior from returned tool results and accumulated messages.
- Decision owner: the active LLM actor inside the Harness loop.
- Supporting / enforcement mechanisms: prompt assembler, provider adapter, tool registry/executor, `AgentState`, event hooks, iteration/token configuration, timeouts, persistence and optional sandbox/feedback plugins.
- Closure path: user task and current state → prompt assembled → model selects text or tool call → runtime applies permitted tool action → result/error returns as a tool message → updated state enters the next model turn → model chooses the next substantive action or final answer.
- Boundary reachability: this is the standard first-party loop used by the documented CLI/server/desktop modes and requires no downstream harness composition beyond a configured model/provider.
- Why this is / is not agent-owned: removing the model while retaining runtime enforcement removes the discretionary next-action/tool choice; the runtime can constrain or execute decisions but does not substitute the same task judgment.
- Evidence: [`README.md`](https://github.com/cgast/harness/blob/b3a9edde79f332f86189da742c5313f25f210b79/README.md); [`packages/core/src/engine/loop.ts`](https://github.com/cgast/harness/blob/b3a9edde79f332f86189da742c5313f25f210b79/packages/core/src/engine/loop.ts).
- Basis: explicit + structural
- Confidence: high
- Caveats: model inference may be external, but the repository supplies the first-party reason/action/tool/result feedback organization and applies model choices through its runtime.

## S2 — Coordination

- State: —
- Function: no material first-party inter-S1 coordination function is established at the assessed deployment recursion.
- Disturbance / variety regulated: no concrete interference or oscillation between at least two credited S1 units is established.
- Decisive decision or feedback right: not established.
- Decision owner: none established for S2.
- Supporting / enforcement mechanisms: event bus, plugin hooks, persistence, host/session boundaries and task invocation can sequence or isolate work but do not establish S2.
- Closure path: not applicable; no reviewed path closes distinct S1 units → specific inter-S1 disturbance → attenuation relation → changed subsequent S1 behavior.
- Distinct S1 units: one active model/tool task loop is established; separate sessions/invocations are not shown as mutually coupled operational units in one higher-recursion organization.
- Inter-S1 disturbance: none materially evidenced in the standard frozen runtime.
- Attenuating coordination relation: none established for an inter-S1 disturbance.
- Feedback into subsequent S1 behaviour: none established from an S2-specific relation.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the event bus and shared persistence are generic runtime mechanisms; there is no concrete multi-S1 disturbance-and-attenuation witness.
- Why this is / is not agent-owned: no S2 function is established, so ownership classification does not proceed.
- Evidence: [`README.md`](https://github.com/cgast/harness/blob/b3a9edde79f332f86189da742c5313f25f210b79/README.md); [`packages/core/src/engine/loop.ts`](https://github.com/cgast/harness/blob/b3a9edde79f332f86189da742c5313f25f210b79/packages/core/src/engine/loop.ts).
- Basis: structural absence review
- Confidence: high
- Caveats: plugins or a wider downstream deployment could compose several Harness agents, but that would require separate evidence at that wider boundary.

### Absence scope

- Surfaces inspected: core agent loop, event bus/plugin architecture, persistence, CLI/server/desktop host modes, memory/feedback plugins and frozen heartbeat planning artifact.
- Plausible first-party paths checked: concurrent sessions, plugin-mediated events, shared persistence, periodic-session design and host-level task invocation.
- Why no material first-party path remains: no implemented standard path supplies at least two distinct coupled S1 units together with a concrete interference mode, an S2-specific attenuating relation and returned coordination feedback.

## S3 — Inside-and-now control

- State: —
- Function: no separate whole-system current-control function is established above the single task loop.
- Disturbance / variety regulated: current task state, iteration limits, tool timeouts, plugin aborts and human approvals are regulated locally, not through a whole-deployment current-control loop.
- Decisive decision or feedback right: no whole-system decision over current resources, commitments, priorities, constraints or cross-operation intervention is established.
- Decision owner: none established for S3.
- Supporting / enforcement mechanisms: `AgentState`, max-iteration/model/token configuration, tool timeout, event hooks, server/desktop controls and FeedbackManager pause/resume.
- Closure path: not applicable; reviewed controls constrain or intervene in one active operation rather than close whole-system current evidence → S3 judgment → changed deployment-wide operation.
- Boundary reachability: runtime controls are reachable, but the S3 organizational function itself is not established.
- Whole-system current view: no supported aggregate view over multiple current S1 commitments/resources was found.
- Current-control decision scope: local run constraints, tool approvals and interrupts only; no coherent whole-system resource/priority/commitment decision right is established.
- Why this is / is not agent-owned: deterministic runtime constraints and local human feedback do not establish S3 ownership without the S3 function.
- Evidence: [`packages/core/src/engine/loop.ts`](https://github.com/cgast/harness/blob/b3a9edde79f332f86189da742c5313f25f210b79/packages/core/src/engine/loop.ts); [`packages/core/src/feedback/manager.ts`](https://github.com/cgast/harness/blob/b3a9edde79f332f86189da742c5313f25f210b79/packages/core/src/feedback/manager.ts); [`README.md`](https://github.com/cgast/harness/blob/b3a9edde79f332f86189da742c5313f25f210b79/README.md).
- Basis: structural absence review
- Confidence: high
- Caveats: ordinary human approval of a tool/action is explicitly narrower than parent S3 current-control closure.

### Absence scope

- Surfaces inspected: run state/status, runtime limits, event bus, plugin abort/modify hooks, human-feedback manager, CLI/server/desktop hosting and persistence.
- Plausible first-party paths checked: operator intervention, task abort, human review, plugin policy, iteration/resource limits and multiple host sessions.
- Why no material first-party path remains: all established paths are local run regulation or deterministic enforcement; no whole-system current operational picture plus decision-and-return authority over the deployment's S1 commitments is supplied.

## S3* — Complementary audit

- State: —
- Function: no independent complementary audit of ordinary operational claims is established in the runtime boundary.
- Disturbance / variety regulated: events/logs and human review expose ordinary run information, but no materially independent alternative-access audit path closes into control.
- Decisive decision or feedback right: not established.
- Decision owner: none established for S3*.
- Supporting / enforcement mechanisms: fully observable event stream, telemetry hooks, persistence, feedback review and repository `SECURITY_ASSESSMENT.md`.
- Closure path: not applicable; no runtime chain establishes ordinary claim → independent complementary evidence → audit judgment → finding returned into subsequent current control.
- Boundary reachability: telemetry/feedback are reachable but remain ordinary observation/intervention surfaces; repository security review is adjacent development evidence.
- Claim being audited: none with a qualifying independent runtime audit path.
- Ordinary reporting path: normal event/state/tool/model records.
- Complementary access path: none established.
- Independence boundary: not established for a runtime auditor separate from the ordinary production path.
- Who acts on findings: no qualifying finding-return loop is established.
- Why this is / is not agent-owned: no S3* function is established.
- Evidence: [`README.md`](https://github.com/cgast/harness/blob/b3a9edde79f332f86189da742c5313f25f210b79/README.md); [`packages/core/src/feedback/manager.ts`](https://github.com/cgast/harness/blob/b3a9edde79f332f86189da742c5313f25f210b79/packages/core/src/feedback/manager.ts).
- Basis: structural absence review
- Confidence: high
- Caveats: observability or a human artifact review can support auditing in a composed system, but neither alone supplies the required complementary independence and control return at this boundary.

### Absence scope

- Surfaces inspected: event/telemetry architecture, persistence, human artifact review, plugin hooks, repository security assessment and host modes.
- Plausible first-party paths checked: telemetry-derived checking, human review, persisted session inspection and development security review.
- Why no material first-party path remains: runtime evidence is ordinary-path observation/review, while the repository security assessment belongs to development governance rather than a shipped complementary audit loop.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material external-and-prospective adaptation loop is established.
- Disturbance / variety regulated: persistent user facts and changing tool/model environment can affect later behavior, but no future-oriented adaptation option is generated and returned into present capability as S4 closure.
- Decisive decision or feedback right: not established for prospective capability adaptation.
- Decision owner: none established for S4.
- Supporting / enforcement mechanisms: memory store/recall, persistence, skills/plugins, provider selection and the frozen heartbeat design plan.
- Closure path: not applicable; memory capture → later prompt context is persistence/context reuse, not an established external/future distinction → adaptation option → present-capability change loop.
- Boundary reachability: memory and configuration paths are reachable; heartbeat adaptation is not because only its implementation plan exists at the frozen revision.
- External distinction: user facts and external tool/model results are observable.
- Future / prospective distinction: no distinct future-oriented environmental model/judgment is established.
- Adaptation option generated: none established beyond stored context/configuration.
- Path back into current capability / S3: memory can re-enter later prompts, but without a prospective adaptation judgment this does not satisfy S4.
- Why this is / is not agent-owned: the model may choose to store a fact, but generic memory update alone is explicitly insufficient for S4 under Profile 0.2.4.
- Evidence: [`plugins/memory/src/index.ts`](https://github.com/cgast/harness/blob/b3a9edde79f332f86189da742c5313f25f210b79/plugins/memory/src/index.ts); [`README.md`](https://github.com/cgast/harness/blob/b3a9edde79f332f86189da742c5313f25f210b79/README.md); [`.claude/plan.md`](https://github.com/cgast/harness/blob/b3a9edde79f332f86189da742c5313f25f210b79/.claude/plan.md).
- Basis: explicit + structural absence review
- Confidence: high
- Caveats: an implemented future heartbeat/self-adaptation subsystem could change this mapping; the frozen revision contains only its plan.

### Absence scope

- Surfaces inspected: memory plugin, persistent session/memory stores, skills, plugins, provider/config selection, heartbeat plan and ordinary model/tool loop.
- Plausible first-party paths checked: model-selected memory storage, cross-session prompt injection, plugin/skill configuration and planned proactive heartbeat sessions.
- Why no material first-party path remains: implemented mechanisms preserve/reuse context or configure current capability, while the only explicit prospective periodic subsystem is not implemented at the frozen ref; no closed prospective adaptation-option loop remains.

## S5 — Policy and identity

- State: —
- Function: no material runtime identity/ultimate-policy closure is established.
- Disturbance / variety regulated: soul files contain values, boundaries, character and context, and plugins can enforce local action policy, but no identity-level issue is adjudicated through an ultimate-authority loop.
- Decisive decision or feedback right: no runtime path for identity/ultimate-policy judgment is established.
- Decision owner: none established for S5 at this boundary.
- Supporting / enforcement mechanisms: selectable soul YAML, soul loader/injector, prompt assembly, configuration and local approval/policy plugins.
- Closure path: not applicable; loading a prewritten soul into future prompts is static policy enforcement, not identity/policy issue → legitimate ultimate authority → authoritative decision → returned governance.
- Boundary reachability: soul selection and injection are reachable, but the required S5 decision path is absent.
- Identity / ultimate-policy issue: none shown reaching an authority for adjudication during supported operation.
- Ultimate authority in each claimed mode: no positive mode claimed.
- Return-to-operation path: static soul contents return to prompts, but no new identity/ultimate-policy decision is generated through a qualifying authority path.
- Why this is / is not agent-owned: a system prompt, policy file or safety boundary does not by itself own S5; the frozen runtime does not establish autonomous or parent-governed ultimate-policy closure.
- Evidence: [`packages/core/src/soul/loader.ts`](https://github.com/cgast/harness/blob/b3a9edde79f332f86189da742c5313f25f210b79/packages/core/src/soul/loader.ts); [`packages/core/src/engine/prompt-assembler.ts`](https://github.com/cgast/harness/blob/b3a9edde79f332f86189da742c5313f25f210b79/packages/core/src/engine/prompt-assembler.ts); [`README.md`](https://github.com/cgast/harness/blob/b3a9edde79f332f86189da742c5313f25f210b79/README.md).
- Basis: explicit + structural absence review
- Confidence: high
- Caveats: a wider parent organization can edit soul/configuration files between runs, but generic configuration authority is not enough for Methodology parent S5 without a reconstructable identity/ultimate-policy decision-and-return loop.

### Absence scope

- Surfaces inspected: soul schema/loader/injection, documented boundaries/ethics/character/context layers, configuration, plugin policy hooks and human-feedback paths.
- Plausible first-party paths checked: operator soul selection/editing, static safety boundaries, plugin-based approval and prompt modification.
- Why no material first-party path remains: all reviewed identity/policy material is preconfigured or locally enforced; no first-party operating mode supplies a qualifying ultimate-policy issue, legitimate authority decision and returned authoritative closure.

## Distributed OSS parent arrangement

Repository maintainers and contributors govern the software project, but that development organization is outside the shipped Harness deployment boundary. No organization-level parent VSM mode is inferred from OSS contribution or release authority.

## Self-hosted and non-human modes

Harness is self-hosted and exposes operator configuration plus local human feedback. These paths were inspected for S3/S4/S5 parent modes. Human confirmation/review is local to an operational action and soul/configuration files are static inputs; neither establishes the corresponding complete parent loop under Methodology 0.3.6.

## Recursion

The established viable operational unit is one model/tool agent loop. Plugins, tools and individual tool calls are supporting mechanisms rather than separate viable S1 units. Independent Harness sessions can be analyzed as S1 cells only in a wider organization that actually couples them; such a composed deployment is not present at the pinned standard boundary.

## Variety and escalation

The model absorbs task-level semantic variety while tools expand response capacity. Runtime limits, timeouts, workspace/sandbox constraints and plugin hooks attenuate unsafe or excessive execution variety. Human-feedback adapters can escalate individual choices to a person, but the frozen runtime does not establish metasystemic S3/S4/S5 ownership from those local escalations.

## Evidence gaps

No positive higher-system evidence remains unresolved enough to require `?`: the frozen standard boundary is sufficiently broad to support the recorded absence findings. The most important future reassessment triggers would be implementation of the planned heartbeat/proactive subsystem, a first-party multi-agent operating mode with conflict attenuation, a whole-deployment supervisory control plane, or an explicit identity-policy escalation/closure surface.

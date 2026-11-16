---
harness_id: sol-pi
project_name: SoL-Pi
repository: https://github.com/NVlabs/SoL-Pi
review_ref: 219568034fa54ed121ede80961655e33dfb9d0e3
reviewed_at: 2026-11-16
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# SoL-Pi

## Review boundary

- System in focus: The first-party SoL-Pi Pi-extension package as installed by its documented public extension entry point, not the upstream Pi coding agent, training/research pipeline, Claude Code/Codex example hosts or NVIDIA's developer organization.
- Purpose and identity: Reduce token/turn cost and preserve evidence for tasks being executed by an independently supplied Pi agent runtime.
- Relevant environment: Pi tool results, agent session/context events, model-provider requests delegated to the host, local session archives and configured user/project trust.
- Standard-distribution boundary: Shipped `src/sol-pi/index.ts` feature registration, all four optional extension implementations, default configuration and documented Pi-hosted installation; include documented all-enabled mode as well as default-disabled mode.
- Credited operating / distribution surfaces: Action Fusion tool wrappers, ObservationPack context transform and exact recall, Evidence-Preserving Reducer separate summarizer with checked quotations, Online Context Compact deterministic decision, Pi event subscriptions and host compaction API calls.
- Adjacent first-party surfaces excluded from ownership: External Pi agent model/tool loop and control plane, third-party host API implementations, paper's offline auto-research and benchmark experiment cycles, examples executed in Claude Code/Codex, project maintainer/contributor governance and CI.
- First-party operating / deployment modes considered: Default (four mechanisms opt-in and disabled); explicit user opt-in for any/all four; Pi codemode support; local or in-memory session archival; separately selected remote reducer provider/model.
- Recursion level: The independently installed extension's own decision boundary, an attached support component of one host Pi run. No standalone first-party organizational S1 agent is shipped.
- Reviewed revision: `219568034fa54ed121ede80961655e33dfb9d0e3`.
- Observation date: 2026-11-16.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

SoL-Pi is published as a Pi extension, not a fork or vendor of Pi. Its only package entry point registers feature hooks under Pi's public `ExtensionAPI` after `session_start` and a trusted-config lookup. The user-facing README says that every mechanism is opt-in and disabled by default and that Pi owns the main model, authentication and provider. With explicit flags, action fusion executes a follow-up validation command in one tool call, ObservationPack replaces old model-visible observations with archival handles, a separate provider call can reduce a diagnostic log into a checked receipt, and Online Context Compact evaluates a cost/window condition before requesting Pi native compaction and continuation. These changes are valuable *support mechanics* of an external working agent, but they do not ship a first-party open-ended agent owning an environment-facing task action loop. [`src/sol-pi/index.ts`](https://github.com/NVlabs/SoL-Pi/blob/219568034fa54ed121ede80961655e33dfb9d0e3/src/sol-pi/index.ts#L14-L50), [`src/sol-pi/extensions/action-fusion/index.ts`](https://github.com/NVlabs/SoL-Pi/blob/219568034fa54ed121ede80961655e33dfb9d0e3/src/sol-pi/extensions/action-fusion/index.ts#L85-L165), [`src/sol-pi/extensions/observation-pack/index.ts`](https://github.com/NVlabs/SoL-Pi/blob/219568034fa54ed121ede80961655e33dfb9d0e3/src/sol-pi/extensions/observation-pack/index.ts#L58-L161), [`src/sol-pi/extensions/evidence-preserving-reducer/index.ts`](https://github.com/NVlabs/SoL-Pi/blob/219568034fa54ed121ede80961655e33dfb9d0e3/src/sol-pi/extensions/evidence-preserving-reducer/index.ts#L68-L219), [`src/sol-pi/extensions/online-context-compact/extension.ts`](https://github.com/NVlabs/SoL-Pi/blob/219568034fa54ed121ede80961655e33dfb9d0e3/src/sol-pi/extensions/online-context-compact/extension.ts#L294-L391).

## Operational model

Host Pi supplies the agent session, messages, task goal, model selection, tool invocation decision and task-result ownership. SoL-Pi's handlers receive selected context/turn/tool events and take bounded, configured transformations. The opt-in reducer calls a separate model for one diagnostic receipt, but that model does not own the user's task, decide to invoke environment-facing operations, or independently run subsequent user task turns. The opt-in compaction logic computes whether to ask the host to compact; the host then continues its own run. This distinction separates an agentic upstream dependency from the extension's first-party scope.

## S1 — Operations

- State: —
- Function: No independent first-party autonomous operational agent executing an open-ended task against its environment is implemented by this extension.
- Disturbance / variety regulated: Host Pi handles arbitrary coding tasks; the extension handles token/turn inefficiency and bounded diagnostic observation volume.
- Decisive decision or feedback right: Selecting environment-facing task actions from changing observations belongs to the independent Pi agent, while the extension only transforms selected calls/context.
- Decision owner: External Pi/model for user-task S1; deterministic first-party handlers for cost/archival transformations. The optional reducer model can only summarize one eligible log.
- Supporting / enforcement mechanisms: Event hooks, follow-up bash chaining, archived observation tokens, receipt validation, compaction economics and Pi's continuation call.
- Closure path: Source observations and feature flags trigger deterministic transformations and host API requests; none constitutes a first-party autonomous task-decision loop with iterative goals and tools.
- Boundary reachability: The documented Pi extension entry point calls `registerConfiguredFeatures` only after `session_start`; it imports host Pi interfaces and does not define or instantiate Pi's agent runtime.
- Why this is / is not agent-owned: A reducer model can supply a narrow summary, not the decisive task action policy; removing upstream Pi leaves callbacks without any agent capable of working on a user's task.
- Evidence: [`src/sol-pi/index.ts`](https://github.com/NVlabs/SoL-Pi/blob/219568034fa54ed121ede80961655e33dfb9d0e3/src/sol-pi/index.ts#L14-L50); [`src/sol-pi/extensions/evidence-preserving-reducer/index.ts`](https://github.com/NVlabs/SoL-Pi/blob/219568034fa54ed121ede80961655e33dfb9d0e3/src/sol-pi/extensions/evidence-preserving-reducer/index.ts#L68-L192); [`src/sol-pi/extensions/observation-pack/index.ts`](https://github.com/NVlabs/SoL-Pi/blob/219568034fa54ed121ede80961655e33dfb9d0e3/src/sol-pi/extensions/observation-pack/index.ts#L144-L188); [`src/sol-pi/extensions/online-context-compact/extension.ts`](https://github.com/NVlabs/SoL-Pi/blob/219568034fa54ed121ede80961655e33dfb9d0e3/src/sol-pi/extensions/online-context-compact/extension.ts#L391-L469); [`README.md`](https://github.com/NVlabs/SoL-Pi/blob/219568034fa54ed121ede80961655e33dfb9d0e3/README.md).
- Basis: explicit public packaging and structural code ownership.
- Confidence: High for the bounded first-party absence, including all-enabled configuration.
- Caveats: Pi itself may qualify as an agentic harness and should be independently assessed under its own repository; this is not a claim about Pi or a future integrated fork.

### Absence scope

- Surfaces inspected: Package entry point and peer-dependency packaging; feature registry/config; action-fusion, observation, reducer, compaction handlers, model-call adapter, first-party tests and documented installation.
- Plausible first-party paths checked: Reducer provider call (bounded diagnostic summarization), `pi.registerTool` for exact observation recall, fused edit/write tool wrapper, `pi.on("turn_end")` compaction selection and `pi.on("agent_settled")` host continuation.
- Why no material first-party path remains: None of these supported paths creates an autonomous task agent with its own goal-to-tool-to-environment-to-next-goal operational loop. Every normal user task and tool-action decision remains with the separately installed Pi host.

## S2 — Coordination

- State: —
- Function: No first-party inter-S1 interference-attenuation decision is evidenced at the extension boundary.
- Disturbance / variety regulated: One host task can generate many observations and commands, but distinct first-party operational S1 units in coordination conflict are not present.
- Decisive decision or feedback right: Resolve a specific clash, oscillation or incompatible commitment among independent operational agents; no such first-party right exists.
- Decision owner: None established.
- Supporting / enforcement mechanisms: Observation identities, archive session directories, fused tool command sequence and compaction event state.
- Closure path: Transformations route results back to the same host Pi task without arbitration between independent first-party S1 activities.
- Why this is / is not agent-owned: Exact archival handles, callback serialization and a queued follow-up command are not evidence of inter-S1 coordination.
- Evidence: [`src/sol-pi/extensions/action-fusion/index.ts`](https://github.com/NVlabs/SoL-Pi/blob/219568034fa54ed121ede80961655e33dfb9d0e3/src/sol-pi/extensions/action-fusion/index.ts#L85-L165); [`src/sol-pi/extensions/observation-pack/index.ts`](https://github.com/NVlabs/SoL-Pi/blob/219568034fa54ed121ede80961655e33dfb9d0e3/src/sol-pi/extensions/observation-pack/index.ts#L58-L175); [`src/sol-pi/index.ts`](https://github.com/NVlabs/SoL-Pi/blob/219568034fa54ed121ede80961655e33dfb9d0e3/src/sol-pi/index.ts#L14-L50).
- Basis: structural.
- Confidence: High for declared extension-only scope.
- Caveats: Host Pi or another independently configured multi-agent application could regulate shared work; that is not owned by SoL-Pi.

### Absence scope

- Surfaces inspected: All registered feature surfaces, callback entry point, observation archive, fused tool handler, reducer and compaction hooks.
- Plausible first-party paths checked: Repeated results/handle deduplication, chained edit→validate, plan-step progress, independent reducer model and host continuation.
- Why no material first-party path remains: None exposes two first-party S1 agents or their interference as a source decision and none returns an arbitration outcome to changed peer commitments; the mechanisms compress or sequence a single externally owned run.

## S3 — Inside-and-now control

- State: —
- Function: No first-party whole-organization current-commitment controller is established.
- Disturbance / variety regulated: Window pressure and token cost can make one Pi task inefficient.
- Decisive decision or feedback right: Revision of whole-system current priorities, resource commitments and accountability based on a whole-system operational view is absent.
- Decision owner: Host/operator owns the task plan and model action policy; deterministic `decideCompaction` owns an individual context-optimization threshold, not organizational S3.
- Supporting / enforcement mechanisms: Estimated remaining requests and compaction economics, plan-step state, session usage, native Pi compact call.
- Closure path: On a completed plan boundary, numerical checks may request host compaction, which returns a shorter context to the same Pi task.
- Why this is / is not agent-owned: A model-led task is not supervised here; an efficiency threshold neither reallocates a fleet's commitments nor revises a shared current organizational plan.
- Evidence: [`src/sol-pi/extensions/online-context-compact/economics.ts`](https://github.com/NVlabs/SoL-Pi/blob/219568034fa54ed121ede80961655e33dfb9d0e3/src/sol-pi/extensions/online-context-compact/economics.ts#L129-L220); [`src/sol-pi/extensions/online-context-compact/extension.ts`](https://github.com/NVlabs/SoL-Pi/blob/219568034fa54ed121ede80961655e33dfb9d0e3/src/sol-pi/extensions/online-context-compact/extension.ts#L294-L379); [`src/sol-pi/extensions/online-context-compact/extension.ts`](https://github.com/NVlabs/SoL-Pi/blob/219568034fa54ed121ede80961655e33dfb9d0e3/src/sol-pi/extensions/online-context-compact/extension.ts#L391-L469).
- Basis: structural.
- Confidence: High for described compiled package mode.
- Caveats: A host application could interpret these metrics as S3 inputs, but the reported extension does not own such decisions.

### Absence scope

- Surfaces inspected: Online Context Compact plan/context event handlers, compaction decision and state; feature registry; basic CLI/host integration.
- Plausible first-party paths checked: Plan progress and next-handoff boundaries, compaction economics, corrective context messages and session selection.
- Why no material first-party path remains: Compaction can optimize one working memory and resume one task; it does not own a current whole-system view, a cross-S1 resource/priority decision or a returned S3-level corrective intervention.

## S3* — Complementary audit

- State: —
- Function: No independent audit of actual operational results and corrective return to organizational current control is established.
- Disturbance / variety regulated: Diagnostic-log summarizers may omit or corrupt evidence, but the extension verifies quote fidelity rather than auditing operational truth.
- Decisive decision or feedback right: A complementary auditor would compare independent operational evidence against an operating claim and feed its finding into supervisory control; this package makes no such organizational audit decision.
- Decision owner: None qualified. Optional reducer model selects candidate citations, while local validator checks hash, exact quotes and failure-signal fidelity.
- Supporting / enforcement mechanisms: Archived raw source, model-produced receipt, exact-quote validation, failure fallback to unchanged source, observation recall.
- Closure path: Receipt validation accepts or rejects a compressed observation in the same Pi context; it does not independently inspect real work artifacts or send an audit verdict to an S3 controller.
- Why this is / is not agent-owned: A separate reducer model and exact-evidence check give integrity protection to a tool result, not independent auditor authority over agent operations.
- Evidence: [`src/sol-pi/extensions/evidence-preserving-reducer/index.ts`](https://github.com/NVlabs/SoL-Pi/blob/219568034fa54ed121ede80961655e33dfb9d0e3/src/sol-pi/extensions/evidence-preserving-reducer/index.ts#L68-L192); [`src/sol-pi/extensions/evidence-preserving-reducer/receipt.ts`](https://github.com/NVlabs/SoL-Pi/blob/219568034fa54ed121ede80961655e33dfb9d0e3/src/sol-pi/extensions/evidence-preserving-reducer/receipt.ts#L79-L143); [`src/sol-pi/extensions/observation-pack/index.ts`](https://github.com/NVlabs/SoL-Pi/blob/219568034fa54ed121ede80961655e33dfb9d0e3/src/sol-pi/extensions/observation-pack/index.ts#L144-L189).
- Basis: structural.
- Confidence: Moderate to high within the shipped callback boundary.
- Caveats: The receipt is a useful integrity check and should not be misdescribed as meaningless; the missing property is independent organizational audit closure, not quote validity.

### Absence scope

- Surfaces inspected: Evidence-Preserving Reducer provider/receipt validation and archive, ObservationPack original bytes and recall, post-compaction state, optional error feedback.
- Plausible first-party paths checked: Separate model reduction of command log, hash/quote verification and restoration of raw log on invalid receipt, plan recovery and context correction.
- Why no material first-party path remains: The returned check evaluates the fidelity of a summary to its source, not the truth of the underlying completed task or independent operational conditions, and no result reaches an organizational supervisory authority.

## S4 — Outside-and-then intelligence

- State: —
- Function: No installed prospective environment-sensing, options and adoption loop changes future organizational capability.
- Disturbance / variety regulated: Future cost of long context or different tool/model environments might motivate adapting the runtime.
- Decisive decision or feedback right: Generate and adopt longer-term adaptation options from outside-and-then evidence and return them to current S3 capacity.
- Decision owner: None at first-party runtime; humans authored efficiency techniques offline for this release, while numerical runtime compaction is current-session housekeeping.
- Supporting / enforcement mechanisms: Learned/researched efficiency mechanisms baked into source code, context request horizon estimation, compaction option and provider compatibility configuration.
- Closure path: Compaction can shorten one current session but does not learn a new harness policy/tool/capability from environmental developments and adopt it for future sessions.
- Why this is / is not agent-owned: The paper's auto-research discovery is an external historical research process, not an installed future-intelligence agent in SoL-Pi.
- Evidence: [`src/sol-pi/extensions/online-context-compact/economics.ts`](https://github.com/NVlabs/SoL-Pi/blob/219568034fa54ed121ede80961655e33dfb9d0e3/src/sol-pi/extensions/online-context-compact/economics.ts#L77-L128); [`src/sol-pi/extensions/online-context-compact/economics.ts`](https://github.com/NVlabs/SoL-Pi/blob/219568034fa54ed121ede80961655e33dfb9d0e3/src/sol-pi/extensions/online-context-compact/economics.ts#L129-L220); [`src/sol-pi/extensions/online-context-compact/extension.ts`](https://github.com/NVlabs/SoL-Pi/blob/219568034fa54ed121ede80961655e33dfb9d0e3/src/sol-pi/extensions/online-context-compact/extension.ts#L391-L469); [`src/sol-pi/index.ts`](https://github.com/NVlabs/SoL-Pi/blob/219568034fa54ed121ede80961655e33dfb9d0e3/src/sol-pi/index.ts#L14-L50).
- Basis: structural.
- Confidence: High for the pinned standard distribution.
- Caveats: Efficiency improvement and operational optimization are real; this assessment is only about VSM ownership/closure.

### Absence scope

- Surfaces inspected: Package README/paper boundary statement, runtime feature flags, economics, plan state, online compaction, reducer model and archives.
- Plausible first-party paths checked: Cost forecasts, plan-driven compaction, rule changes through user config, offline auto-research claims and reducer inference.
- Why no material first-party path remains: No first-party installed mechanism continuously senses a future environment, evaluates strategic alternatives and adopts a durable change to organization capability/S3; the user can manually enable fixed components.

## S5 — Policy and identity

- State: —
- Function: No first-party governing identity/ultimate purpose institution is implemented for the external agent organization.
- Disturbance / variety regulated: Which installed extensions/models/providers are trusted and entitled to change task behavior is decided by Pi/user authority.
- Decisive decision or feedback right: Legitimate identity, ultimate-purpose or authority-setting decision returned to operation is absent inside SoL-Pi.
- Decision owner: Pi host and user/project config determine installed permissions and trust; SoL-Pi reads config and enforces local feature flags.
- Supporting / enforcement mechanisms: Trust-aware config file priority, default-disabled features, opt-in reducer provider/model choice, local storage controls.
- Closure path: Host-supplied trust/config enables or disables handlers, but no independent first-party S5 institution decides overarching identity or authorizations on the system's behalf.
- Why this is / is not agent-owned: A fixed configuration gate is a support mechanism, not a model-based or legitimate parent-governed identity-policy decision.
- Evidence: [`src/sol-pi/index.ts`](https://github.com/NVlabs/SoL-Pi/blob/219568034fa54ed121ede80961655e33dfb9d0e3/src/sol-pi/index.ts#L14-L50); [`src/sol-pi/extensions/evidence-preserving-reducer/index.ts`](https://github.com/NVlabs/SoL-Pi/blob/219568034fa54ed121ede80961655e33dfb9d0e3/src/sol-pi/extensions/evidence-preserving-reducer/index.ts#L202-L219); [`docs/configuration.md`](https://github.com/NVlabs/SoL-Pi/blob/219568034fa54ed121ede80961655e33dfb9d0e3/docs/configuration.md).
- Basis: structural.
- Confidence: High for the extension-only published scope.
- Caveats: Host Pi governance is an external agent's organization and is not credited here.

### Absence scope

- Surfaces inspected: Configuration loading and trust state, extension registration, provider model routing, archive storage.
- Plausible first-party paths checked: Project/user opt-in policy, reducer provider, built-in feature flags, changes to hook behavior and session compaction.
- Why no material first-party path remains: These are host-selected extension behaviors, not a first-party legitimate ultimate-policy decision process with returned organizational identity authority.

## Distributed OSS parent arrangement

The upstream README's research releases, maintainers, benchmarking statements and collaboration are about the source project, not a first-party deployed operational agent organization. Do not borrow the developer institution as a P-mode to make an extension's runtime viable.

## Self-hosted and non-human modes

The documented Pi-hosted extension can be loaded with all four features enabled, including a remotely hosted separate reducer model. It still cannot run a user task without an independent Pi agent; the extra model only reduces eligible logs. The default with no flags is even less agentic, but the exclusion conclusion is based on both available modes rather than merely disabled defaults.

## Recursion

One installed SoL-Pi extension is a subordinate support layer inside Pi's agent loop. It is not an independently viable multi-agent recursive level; the paper's research agents and user's host Pi agent are external and not imported.

## Variety and escalation

Diagnostic-log observations can be compressed subject to source hash/quotation checks; a bad receipt triggers a fallback to raw output. Context pressure can trigger host compaction after a plan boundary. Neither pipeline supplies first-party open-ended S1 task action ownership or independent metasystem control. [`src/sol-pi/extensions/evidence-preserving-reducer/index.ts`](https://github.com/NVlabs/SoL-Pi/blob/219568034fa54ed121ede80961655e33dfb9d0e3/src/sol-pi/extensions/evidence-preserving-reducer/index.ts#L149-L192), [`src/sol-pi/extensions/online-context-compact/extension.ts`](https://github.com/NVlabs/SoL-Pi/blob/219568034fa54ed121ede80961655e33dfb9d0e3/src/sol-pi/extensions/online-context-compact/extension.ts#L294-L379).

## Exclusion decision

**Proposed canonical outcome: `excluded-no-agentic-vsm`.** SoL-Pi is valuable efficiency infrastructure for an actual autonomous agent host, but the packaged extension alone does not own a first-party autonomous operational S1 decision loop. Keep it as a documented excluded candidate rather than promoting Pi's capabilities to a different repository. No positive S1–S5/S3* autonomy states are asserted.

## Evidence gaps

- This review is a fixed source and documented-reachability assessment; it did not execute a Pi provider or an agent task.
- If SoL-Pi later ships a first-party autonomous task loop or an independently legitimate organizational S3/S4/S5 mode, reassess that updated source revision separately. Inference from the original research paper's offline experimental agents is not source evidence of deployed extension behavior.
- Optional model-based log reduction and first-party exact-fidelity validation were inspected and correctly bounded; they are not counted as open-ended agentic task execution or S3* independent operational audit.

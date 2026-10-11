---
harness_id: self-improving-agent
project_name: self-improving-agent
repository: https://github.com/xmaks82/self-improving-agent
review_ref: fd59417b91292b48711410a91d2cbf3eaeb0c060
reviewed_at: 2026-10-11
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: ?
autonomy_s4: A
autonomy_s5: —
---

# self-improving-agent

## Review boundary

- System in focus: shipped Python CLI coding harness with model-based MainAgent, first-party tool loop, bundling of task subagents, feedback-triggered prompt-improvement agents, optional automated verification, per-version metrics and rollback.
- Purpose and identity: solve user coding tasks and self-adjust future assistant response capabilities when credible user feedback identifies deficiencies.
- Relevant environment: local project/repo, shell and code, user approval, provider model endpoint, task outcomes, observed user feedback, persisted prompts/logs.
- Standard-distribution boundary: `src/agent/main.py` launched CLI and reachable `MainAgent.process`, `AgentPipeline`, AnalyzerAgent, VersionerAgent, prompts, feedback, task subagents and user-invoked verification modes.
- Credited operating / distribution surfaces: [src/agent/main.py](https://github.com/xmaks82/self-improving-agent/blob/fd59417b91292b48711410a91d2cbf3eaeb0c060/src/agent/main.py), [src/agent/agents/main_agent.py](https://github.com/xmaks82/self-improving-agent/blob/fd59417b91292b48711410a91d2cbf3eaeb0c060/src/agent/agents/main_agent.py#L40-L535), [src/agent/agents/pipeline.py](https://github.com/xmaks82/self-improving-agent/blob/fd59417b91292b48711410a91d2cbf3eaeb0c060/src/agent/agents/pipeline.py#L37-L191), [src/agent/agents/verification.py](https://github.com/xmaks82/self-improving-agent/blob/fd59417b91292b48711410a91d2cbf3eaeb0c060/src/agent/agents/verification.py#L53-L117), [src/agent/agents/analyzer.py](https://github.com/xmaks82/self-improving-agent/blob/fd59417b91292b48711410a91d2cbf3eaeb0c060/src/agent/agents/analyzer.py#L164-L279), [src/agent/agents/versioner.py](https://github.com/xmaks82/self-improving-agent/blob/fd59417b91292b48711410a91d2cbf3eaeb0c060/src/agent/agents/versioner.py#L137-L435), [src/agent/core/orchestrator.py](https://github.com/xmaks82/self-improving-agent/blob/fd59417b91292b48711410a91d2cbf3eaeb0c060/src/agent/core/orchestrator.py#L34-L212), [src/agent/storage/prompts.py](https://github.com/xmaks82/self-improving-agent/blob/fd59417b91292b48711410a91d2cbf3eaeb0c060/src/agent/storage/prompts.py#L14-L255).
- Adjacent first-party surfaces excluded from ownership: developer [tests/test_agentic_loop.py](https://github.com/xmaks82/self-improving-agent/blob/fd59417b91292b48711410a91d2cbf3eaeb0c060/tests/test_agentic_loop.py) and [.github/workflows/ci.yml](https://github.com/xmaks82/self-improving-agent/blob/fd59417b91292b48711410a91d2cbf3eaeb0c060/.github/workflows/ci.yml), changelog/roadmap as plans rather than executable runtime, Docker/package maintenance and external inference provider work.
- First-party operating / deployment modes considered: standard interactive CLI; model/tool iteration; delegated task subagents; automatic post-edit verifier (when enabled/wired); confidence-gated auto-improvement and prompt rollback.
- Recursion level: one user-operated coding agent and its bounded task/improvement organization, not contributor collective or external model provider.
- Reviewed revision: `fd59417b91292b48711410a91d2cbf3eaeb0c060`.
- Observation date: 2026-10-11.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

`MainAgent.process` loads current prompt, streams a bounded model/tool decision loop, records tool results and session state; the provider remains external but tool-loop organization is first-party. General-purpose `AgentOrchestrator` selects/delegates tasks and can invoke parallel subagents; the mailbox is a support channel, not by its name S2. The main agent uses a `FeedbackDetector` on user inputs, can launch one background improvement at a time, and invokes model-driven Analyzer/Versioner through `ImprovementOrchestrator`. `PromptManager` validates and activates new prompt versions and keeps performance-feedback rollback metadata. [src/agent/agents/main_agent.py](https://github.com/xmaks82/self-improving-agent/blob/fd59417b91292b48711410a91d2cbf3eaeb0c060/src/agent/agents/main_agent.py#L219-L519); [src/agent/core/orchestrator.py](https://github.com/xmaks82/self-improving-agent/blob/fd59417b91292b48711410a91d2cbf3eaeb0c060/src/agent/core/orchestrator.py#L59-L209); [src/agent/storage/prompts.py](https://github.com/xmaks82/self-improving-agent/blob/fd59417b91292b48711410a91d2cbf3eaeb0c060/src/agent/storage/prompts.py#L76-L235).

`AgentPipeline` wires a separate adversarial `VerificationAgent` following 3+ source edits, offering raw-file/build/test access where model tool calling exists. Its verdict is reported to the user. Its S3* independence and actual corrective-loop closure are unresolved; merely naming the feature automatic verification is not enough to claim S3*. [src/agent/agents/pipeline.py](https://github.com/xmaks82/self-improving-agent/blob/fd59417b91292b48711410a91d2cbf3eaeb0c060/src/agent/agents/pipeline.py#L91-L126); [src/agent/agents/verification.py](https://github.com/xmaks82/self-improving-agent/blob/fd59417b91292b48711410a91d2cbf3eaeb0c060/src/agent/agents/verification.py#L1-L117).

## Operational model

Primary S1 is a coding session responding to user tasks. Bounded helper S1 calls may review, research or modify code. The feedback/improvement metasystem reacts to externally originating user quality signals by proposing and activating a new prompt for future tasks; separate specialized model agents make the adaptation choices. A tool-enabled verifier can probe artifacts after source modifications, but its report feeds the CLI after the task output without a proven closed audit/fixback mandate. A human governs task and approvals; static validation/rollback constraints do not thereby enact S5.

## S1 — Operations

- State: A
- Function: First-party coding loop selecting tools and iterating against source, shell, tests and user requests.
- Disturbance / variety regulated: Uncertain tasks, code state, tool results, shell failures and model context.
- Decisive decision or feedback right: Choose source/tool operations and next coding actions using model observations.
- Decision owner: MainAgent model-backed task actor; optional subagents decide scoped tasks.
- Supporting / enforcement mechanisms: Client adapters, tool registry, iteration cap, approval, context and guard.
- Closure path: tool result → conversation context → next model decision and tool action.
- Boundary reachability: CLI constructs MainAgent and bundled tool registry, executes first-party process tool loop; no external coding agent is required.
- Why this is / is not agent-owned: A deterministic registry cannot choose the next coding operation without model action selection.
- Evidence: [src/agent/agents/main_agent.py](https://github.com/xmaks82/self-improving-agent/blob/fd59417b91292b48711410a91d2cbf3eaeb0c060/src/agent/agents/main_agent.py#L219-L391), [src/agent/agents/_tool_loop.py](https://github.com/xmaks82/self-improving-agent/blob/fd59417b91292b48711410a91d2cbf3eaeb0c060/src/agent/agents/_tool_loop.py), [src/agent/agents/orchestrator.py](https://github.com/xmaks82/self-improving-agent/blob/fd59417b91292b48711410a91d2cbf3eaeb0c060/src/agent/agents/orchestrator.py#L53-L129)
- Basis: structural
- Confidence: high
- Caveats: Model endpoint is an external reasoning provider, not a borrowed harness.
- Boundary reachability: CLI constructs MainAgent and bundled tool registry, executes first-party process tool loop; no external coding agent is required.

## S2 — Coordination

- State: —
- Function: No fully evidenced first-party inter-S1 oscillation-reduction cycle at a specific operational recursion.
- Disturbance / variety regulated: Competing child tasks, concurrent improvement runs potentially racing to version prompts.
- Decisive decision or feedback right: Deterministic background-task guard skips a second improvement run while the first executes; subagent orchestrator gathers task outputs.
- Decision owner: Runtime guard enforces same-workflow exclusion; agent decides tasks, but no coordination policy between distinct independent coding S1 operating units was evidenced.
- Supporting / enforcement mechanisms: `_improvement_task` guard, async gather and generic mailbox.
- Closure path: A duplicate improvement request is reported as skipped; this avoids a version race in one meta-workflow, but does not establish distinct S1 operational-unit feedback stabilization.
- Why this is / is not agent-owned: A guarded single shared critical section in the same improvement pipeline and parallel task decomposition are not by themselves evidence of S2 among separate operating S1s.
- Evidence: [src/agent/agents/main_agent.py](https://github.com/xmaks82/self-improving-agent/blob/fd59417b91292b48711410a91d2cbf3eaeb0c060/src/agent/agents/main_agent.py#L448-L458), [src/agent/agents/orchestrator.py](https://github.com/xmaks82/self-improving-agent/blob/fd59417b91292b48711410a91d2cbf3eaeb0c060/src/agent/agents/orchestrator.py#L87-L167), [src/agent/core/mailbox.py](https://github.com/xmaks82/self-improving-agent/blob/fd59417b91292b48711410a91d2cbf3eaeb0c060/src/agent/core/mailbox.py)
- Basis: structural
- Confidence: medium
- Caveats: The simultaneous version-creation race is real; the missing element for positive S2 is distinct operating S1 units and a return that coordinates *their* subsequent action, rather than guarding a single improvement version store.

### Absence scope

- Surfaces inspected: main tool loop, pipeline, agent orchestrator, subagent delegation and mailbox, concurrent improvement-cycle guard.
- Plausible first-party paths checked: async parallel child execution, feedback cycle lock, shared prompt-version store and inter-agent message transport.
- Why no material first-party path remains: No specifically evidenced inter-S1 collision attenuation with feedback altering independently operating S1 units; guard serializes one meta-workflow's self-update versioning.

## S3 — Inside-and-now control

- State: —
- Function: No current whole-organization discretionary resource/priority supervisory loop evidenced.
- Disturbance / variety regulated: Operation errors, context pressure, budget, agent/model configuration and version quality.
- Decisive decision or feedback right: The main agent chooses task steps; deterministic limits, approvals and rollback enforce configured thresholds; not a system-wide commitment intervention authority.
- Decision owner: Root task agent for coding, user/configuration for limits, deterministic evaluator for thresholds.
- Supporting / enforcement mechanisms: CostTracker, approval/undo, log manager and conversation compactor.
- Closure path: Local operation gating and prompt rollback affect future requests, but not demonstrated whole-system S3 bargaining/accountability.
- Why this is / is not agent-owned: A named orchestrator sequences tasks and agents; it does not demonstrate independent S3 current whole-system control.
- Evidence: [src/agent/agents/orchestrator.py](https://github.com/xmaks82/self-improving-agent/blob/fd59417b91292b48711410a91d2cbf3eaeb0c060/src/agent/agents/orchestrator.py#L53-L170), [src/agent/agents/main_agent.py](https://github.com/xmaks82/self-improving-agent/blob/fd59417b91292b48711410a91d2cbf3eaeb0c060/src/agent/agents/main_agent.py#L405-L458), [src/agent/core/orchestrator.py](https://github.com/xmaks82/self-improving-agent/blob/fd59417b91292b48711410a91d2cbf3eaeb0c060/src/agent/core/orchestrator.py#L59-L209)
- Basis: structural
- Confidence: medium-high
- Caveats: Feedback-driven prompt change is assessed separately as S4.

### Absence scope

- Surfaces inspected: main agent processing, subagent orchestrator, improvement manager, cost tracking, approvals and session state.
- Plausible first-party paths checked: manager labels, agent selection and runtime limits, feedback-gated prompt rollback and verification result.
- Why no material first-party path remains: No separate discretionary whole-current operational view/decision authority making returned shared commitments or resource allocation decisions was established.

## S3* — Complementary audit

- State: ?
- Function: An automatic adversarial verifier provides a plausible complementary raw-artifact access path, but audit independence and returned corrective control remain unresolved at this source boundary.
- Disturbance / variety regulated: Potential false claims that code modifications work despite unseen build/test failures.
- Decisive decision or feedback right: VerificationAgent may independently read files and run build/tests after three edits; a PASS/FAIL/PARTIAL report is given to the user.
- Decision owner: A separate verifier persona/model call may judge raw evidence, but it shares the producer tool registry/client and has no evidenced independent mandate or authority to require a subsequent correction.
- Supporting / enforcement mechanisms: AgentPipeline.maybe_verify edit counter and call, tool-enabled bounded verifier, VERDICT extraction.
- Closure path: Verification report appears in main response; there is no deterministic failure → producer correction → rerun closure; whether operator supervision closes an audit finding in shipped operation cannot be determined.
- Why this is / is not agent-owned: Unlike generic reviewer names, a separately prompted adversarial agent with first-party direct tests has plausible material S3* access. However the independence and consequential feedback threshold cannot be settled from static source alone.
- Evidence: [src/agent/agents/pipeline.py](https://github.com/xmaks82/self-improving-agent/blob/fd59417b91292b48711410a91d2cbf3eaeb0c060/src/agent/agents/pipeline.py#L91-L126), [src/agent/agents/verification.py](https://github.com/xmaks82/self-improving-agent/blob/fd59417b91292b48711410a91d2cbf3eaeb0c060/src/agent/agents/verification.py#L1-L117), [src/agent/agents/main_agent.py](https://github.com/xmaks82/self-improving-agent/blob/fd59417b91292b48711410a91d2cbf3eaeb0c060/src/agent/agents/main_agent.py#L423-L433)
- Basis: structural / unknown
- Confidence: medium for reachable audit-like access; low for audit closure.
- Caveats: The verifier can fall back to text-only model if tools unsupported, and a failed verifier exception returns None.

## S4 — Outside-and-then intelligence

- State: A
- Function: Use external user quality feedback and recent interaction histories to form forward-looking improvements to the system prompt, activate a new version and retrospectively rollback failures.
- External distinction: Explicit negative or corrective user feedback is new environmental evidence about response fitness outside the harness output channel.
- Future / prospective distinction: Analyzer hypothesizes how revised prompt rules would improve later, not just the current, user sessions.
- Adaptation option generated: Versioner proposes a validated new active prompt version with targeted model-authored changes.
- Path back into current capability / S3: PromptManager switches current.yaml and MainAgent loads that active prompt on the next turn; version feedback can revert failures. This returns the option into operating capability without asserting S3 ownership.
- Disturbance / variety regulated: User dissatisfaction, recurring response-quality failures, environmental performance changes across future sessions.
- Decisive decision or feedback right: AnalyzerAgent proposes hypotheses and confidence; VersionerAgent selects prompt modifications, validates and creates a new active prompt version.
- Decision owner: First-party separately model-driven AnalyzerAgent and VersionerAgent. Human feedback triggers the review; deterministic threshold prevents low-confidence changes without owning adaptation judgment.
- Supporting / enforcement mechanisms: FeedbackDetector, ImprovementOrchestrator, PromptManager, response logs and version-level metric/rollback checks.
- Closure path: negative/confident feedback → analyzer prospective hypotheses → versioner prompt rewrite → PromptManager.create_version switches current.yaml → MainAgent.get_system_prompt uses latest version next turn; feedback metrics may rollback.
- Boundary reachability: MainAgent.process wires feedback detection and starts ImprovementOrchestrator in a bounded background task. Prompts live in packaged storage and are loaded afresh for next request; no developer-only CI is required.
- Why this is / is not agent-owned: Without the analyzer/versioner models the same novel option generation and targeted change would not be made by threshold/metadata storage alone.
- Evidence: [src/agent/agents/main_agent.py](https://github.com/xmaks82/self-improving-agent/blob/fd59417b91292b48711410a91d2cbf3eaeb0c060/src/agent/agents/main_agent.py#L219-L246), [src/agent/agents/main_agent.py](https://github.com/xmaks82/self-improving-agent/blob/fd59417b91292b48711410a91d2cbf3eaeb0c060/src/agent/agents/main_agent.py#L434-L503), [src/agent/core/orchestrator.py](https://github.com/xmaks82/self-improving-agent/blob/fd59417b91292b48711410a91d2cbf3eaeb0c060/src/agent/core/orchestrator.py#L59-L188), [src/agent/agents/analyzer.py](https://github.com/xmaks82/self-improving-agent/blob/fd59417b91292b48711410a91d2cbf3eaeb0c060/src/agent/agents/analyzer.py#L181-L279), [src/agent/agents/versioner.py](https://github.com/xmaks82/self-improving-agent/blob/fd59417b91292b48711410a91d2cbf3eaeb0c060/src/agent/agents/versioner.py#L153-L271), [src/agent/agents/versioner.py](https://github.com/xmaks82/self-improving-agent/blob/fd59417b91292b48711410a91d2cbf3eaeb0c060/src/agent/agents/versioner.py#L366-L435), [src/agent/storage/prompts.py](https://github.com/xmaks82/self-improving-agent/blob/fd59417b91292b48711410a91d2cbf3eaeb0c060/src/agent/storage/prompts.py#L76-L159)
- Basis: structural
- Confidence: medium-high for wired prospective capability adaptation; not proven effective empirically.
- Caveats: This is feedback-driven future *response* capability, not automatic model-weight optimization or benchmark superiority.
- Boundary reachability: MainAgent.process wires feedback detection and starts ImprovementOrchestrator in a bounded background task. Prompts live in packaged storage and are loaded afresh for next request; no developer-only CI is required.

## S5 — Policy and identity

- State: —
- Function: No explicit ultimate policy/identity issue cycle routed to legitimate higher authority with binding returned system-level decision.
- Disturbance / variety regulated: Risky commands, prompt drift, unwanted self-rewrite and user permissions.
- Decisive decision or feedback right: Developer-set protected meta-agent list, prompt validation rules and operator approvals constrain the system. Their enforcement is not S5 identity adjudication.
- Decision owner: Static constructor and human task/operator for local permissions, not a legitimate autonomous S5 ultimate-policy authority.
- Supporting / enforcement mechanisms: VersionerAgent.PROTECTED_AGENTS, prompt validation, tool security, approval and rollback.
- Closure path: Invalid proposed prompt is rejected and task controls enforced; no S5-level issue → authority → policy decision → governed subsequent operation.
- Why this is / is not agent-owned: Constraints guarding adaptive S4 from self-poisoning are not an autonomous identity or policy-making loop.
- Evidence: [src/agent/agents/versioner.py](https://github.com/xmaks82/self-improving-agent/blob/fd59417b91292b48711410a91d2cbf3eaeb0c060/src/agent/agents/versioner.py#L126-L137), [src/agent/agents/versioner.py](https://github.com/xmaks82/self-improving-agent/blob/fd59417b91292b48711410a91d2cbf3eaeb0c060/src/agent/agents/versioner.py#L340-L388), [src/agent/storage/prompts.py](https://github.com/xmaks82/self-improving-agent/blob/fd59417b91292b48711410a91d2cbf3eaeb0c060/src/agent/storage/prompts.py#L114-L159), [src/agent/approval/confirmator.py](https://github.com/xmaks82/self-improving-agent/blob/fd59417b91292b48711410a91d2cbf3eaeb0c060/src/agent/approval/confirmator.py)
- Basis: structural
- Confidence: medium-high
- Caveats: The repository's maintainer governance and human product identity belong to a broader recursion.

### Absence scope

- Surfaces inspected: prompt version safeguards, feedback/rollback governance, approval/security policies, agent configuration and CLI.
- Plausible first-party paths checked: meta-agent protection, prompt policy changes, safety confirmation and prospective prompt adaptation.
- Why no material first-party path remains: Prompts can change at S4 capability level, but no separately evidenced ultimate-policy authority closes identity disputes and returns decisions into operation.

## Recursion

The main agent delegates bounded task subagents and maintains a distinct Analyzer/Versioner improvement pipeline. Separate tasks and messages do not prove that child subagents are recursively viable higher-level organizations: local identity and metasystem autonomy remain restricted. [src/agent/agents/orchestrator.py](https://github.com/xmaks82/self-improving-agent/blob/fd59417b91292b48711410a91d2cbf3eaeb0c060/src/agent/agents/orchestrator.py#L53-L169).

## Variety and escalation

Tool results absorb local code/shell disturbances within S1. Confidence-gated negative feedback is an S4 prospective capability-improvement trigger; prompt-version tracking and rollback attenuate adaptation risk, not an asserted identity-policy decision. Post-edit adversarial verification can reveal otherwise hidden test failures, but its control consequence requires evidence beyond the mere returned report. [src/agent/agents/main_agent.py](https://github.com/xmaks82/self-improving-agent/blob/fd59417b91292b48711410a91d2cbf3eaeb0c060/src/agent/agents/main_agent.py#L405-L519).

## Evidence gaps

- Methodology 0.3.7 `S3*=?`: shipped auto verifier's raw-artifact independence and user-visible FAIL/PARTIAL are real; the lack of a reliably closed correction mandate and shared client/registry means source alone cannot establish a positive complementary audit right or bounded absence, so neither A nor — is asserted.
- S2 negative explicitly examines the same-workflow improvement lock; it avoids prompt version races but does not clearly coordinate separate S1 units.
- S4 positive is limited to externally triggered, model-authored prompt-version changes for future sessions, not demonstrated outcome efficacy, model-weight training or benchmark transfer.

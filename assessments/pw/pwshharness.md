---
harness_id: pwshharness
project_name: PwshHarness
repository: https://github.com/josh-j/pwsh-harness
review_ref: e56e989bbd68d1e6a1138c3755d6c76266700a78
reviewed_at: 2026-10-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# PwshHarness

## Review boundary

- System in focus: the shipped PowerShell terminal agent and built-in extension host at one workspace/session recursion.
- Purpose and identity: carry out user-selected coding and PowerShell tasks with tools, direct result feedback and bounded execution.
- Relevant environment: workspace files, shell commands, a configured OpenAI-compatible model endpoint and the interactive operator.
- Standard-distribution boundary: portable/installed PwshHarness module, Engine and TUI plus built-in agent, provider, retrieval, PowerShell, run-policy and self-extend extensions.
- Credited operating / distribution surfaces: Start/Invoke-PwshHarness activation, Engine AgentLoop, agent tools and optional report_finding fresh read-only subagent.
- Adjacent first-party surfaces excluded from ownership: packaging/install scripts, reference extension samples, bundled example scripts and contributor-facing development machinery; examples corroborate constructor usage but do not supply cognitive owners.
- First-party operating / deployment modes considered: interactive Auto (default), Approve, proposal-only noninteractive calls, mock provider, optional extension generation and findings checker. S1 credit uses the configured real-model agent; mock/proposal-only mode is not its witness.
- Recursion level: workspace harness with one active parent run and serial read-only delegates; background shell processes are tools.
- Reviewed revision: `e56e989bbd68d1e6a1138c3755d6c76266700a78`.
- Observation date: 2026-10-29.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

[Modules/PwshHarness.Engine/Private/AgentLoop.ps1](https://github.com/josh-j/pwsh-harness/blob/e56e989bbd68d1e6a1138c3755d6c76266700a78/src/PwshHarness/Modules/PwshHarness.Engine/Private/AgentLoop.ps1) owns the model/tool/result exchange, streaming retry, run budget and resumable state. [Modules/PwshHarness.Engine/Private/AgentAuthority.ps1](https://github.com/josh-j/pwsh-harness/blob/e56e989bbd68d1e6a1138c3755d6c76266700a78/src/PwshHarness/Modules/PwshHarness.Engine/Private/AgentAuthority.ps1) binds Auto authority to a live user/frontend activation, session epoch and physical workspace; restored config cannot grant Auto. Agent extensions supply reads/edits, background commands, bounded read-only delegation, plans and defect finding. [Extensions/agent/AgentWork.ps1](https://github.com/josh-j/pwsh-harness/blob/e56e989bbd68d1e6a1138c3755d6c76266700a78/src/PwshHarness/Extensions/agent/AgentWork.ps1) records observed reads/command results and sends a reported defect to a fresh refutation context. [Extensions/agent/AgentTools.ps1](https://github.com/josh-j/pwsh-harness/blob/e56e989bbd68d1e6a1138c3755d6c76266700a78/src/PwshHarness/Extensions/agent/AgentTools.ps1) registers these tools and a completion policy that compares the answer with checked findings and execution evidence. Retrieval, semantic checks and generated-test verification support task work. Lessons save bounded command-invocation observations for later prompts. [Extensions/self-extend/Commands.ps1](https://github.com/josh-j/pwsh-harness/blob/e56e989bbd68d1e6a1138c3755d6c76266700a78/src/PwshHarness/Extensions/self-extend/Commands.ps1) generates/stages extensions from a user description; source-bound approval, static checks and child dry-load precede live install.

## Operational model

The parent model owns local task actions and serial child investigation. Runtime gates enforce authority, budgets and trustworthy result attribution. In the optional report_finding path, a separately initialized read-only model challenges a concrete parent's source claim; its result returns to the parent and completion control. This is a bounded complementary audit of a finding, not a claim of an independent security organization.

## S1 — Operations

- State: A
- Function: Model-owned workspace operations.
- Disturbance / variety regulated: Changing task requirements, file content, tool failures and shell feedback.
- Decisive decision or feedback right: Select tool/arguments and revise subsequent actions or final answer.
- Decision owner: Configured model-backed parent agent.
- Supporting / enforcement mechanisms: Provider adapter, tool registry, session lease, exact-action Approve or activated Auto, budget and logging enforcement.
- Closure path: Tool result enters the model exchange; the next model request decides continuation; final answer and session records retain outcome.
- Boundary reachability: Start-PwshHarness enables shipped agent mode; native tools and continuation are installed by the bundled agent extension.
- Why this is / is not agent-owned: Without the model the dispatcher and policies retain limits but do not choose task-specific edits and repairs.
- Evidence: [Modules/PwshHarness.Engine/Private/AgentLoop.ps1](https://github.com/josh-j/pwsh-harness/blob/e56e989bbd68d1e6a1138c3755d6c76266700a78/src/PwshHarness/Modules/PwshHarness.Engine/Private/AgentLoop.ps1); [Extensions/agent/AgentTools.ps1](https://github.com/josh-j/pwsh-harness/blob/e56e989bbd68d1e6a1138c3755d6c76266700a78/src/PwshHarness/Extensions/agent/AgentTools.ps1); [Modules/PwshHarness.Engine/Private/AgentAuthority.ps1](https://github.com/josh-j/pwsh-harness/blob/e56e989bbd68d1e6a1138c3755d6c76266700a78/src/PwshHarness/Modules/PwshHarness.Engine/Private/AgentAuthority.ps1)
- Basis: structural
- Confidence: high for code wiring
- Caveats: PowerShell 7.6/provider execution was not tested.

## S2 — Coordination

- State: —
- Function: Inter-S1 interference regulation is not established.
- Disturbance / variety regulated: Read-only subagents run one at a time; shell background tasks are subprocess tools. Plans, ordered calls and session exclusivity do not demonstrate distinct operational work cells mutually adjusting a concrete conflict.
- Decisive decision or feedback right: No qualifying function-specific decision/return path identified.
- Decision owner: No credited metasystem owner; developer/operator configuration and agent task decisions remain separate.
- Supporting / enforcement mechanisms: Session leases, run policies, budget enforcement, logs and ordinary approvals.
- Closure path: No qualifying function-specific closure.
- Why this is / is not agent-owned: Read-only subagents run one at a time; shell background tasks are subprocess tools. Plans, ordered calls and session exclusivity do not demonstrate distinct operational work cells mutually adjusting a concrete conflict.
- Evidence: [Extensions/agent/AgentWork.ps1](https://github.com/josh-j/pwsh-harness/blob/e56e989bbd68d1e6a1138c3755d6c76266700a78/src/PwshHarness/Extensions/agent/AgentWork.ps1); [Modules/PwshHarness.Engine/Private/AgentLoop.ps1](https://github.com/josh-j/pwsh-harness/blob/e56e989bbd68d1e6a1138c3755d6c76266700a78/src/PwshHarness/Modules/PwshHarness.Engine/Private/AgentLoop.ps1); [Extensions/agent/AgentTasks.ps1](https://github.com/josh-j/pwsh-harness/blob/e56e989bbd68d1e6a1138c3755d6c76266700a78/src/PwshHarness/Extensions/agent/AgentTasks.ps1)
- Basis: structural
- Confidence: high for the inspected supported distribution
- Caveats: Custom extension organizations and unobserved deployments are outside the boundary.

### Absence scope

- Surfaces inspected: Engine loop/authority/run policy; agent tool, work, task and lesson extensions; self-extend staging/approval/install; PowerShell verification; prompts, profiles, README and CONFIGURATION.
- Plausible first-party paths checked: serial delegation, background commands, plan state, extension registration collisions and session lease exclusivity
- Why no material first-party path remains: The supplied constraints regulate a single run's execution/registry, with no inter-S1 disturbance-specific response and feedback relation.

## S3 — Inside-and-now control

- State: —
- Function: Whole-harness current control is not established.
- Disturbance / variety regulated: Token/cost/time reservations, retry fallback and user steering regulate one task under supplied limits; a model does not acquire whole-system resource/commitment authority from those gates.
- Decisive decision or feedback right: No qualifying function-specific decision/return path identified.
- Decision owner: No credited metasystem owner; developer/operator configuration and agent task decisions remain separate.
- Supporting / enforcement mechanisms: Session leases, run policies, budget enforcement, logs and ordinary approvals.
- Closure path: No qualifying function-specific closure.
- Why this is / is not agent-owned: Token/cost/time reservations, retry fallback and user steering regulate one task under supplied limits; a model does not acquire whole-system resource/commitment authority from those gates.
- Evidence: [Modules/PwshHarness.Engine/Private/AgentAuthority.ps1](https://github.com/josh-j/pwsh-harness/blob/e56e989bbd68d1e6a1138c3755d6c76266700a78/src/PwshHarness/Modules/PwshHarness.Engine/Private/AgentAuthority.ps1); [Modules/PwshHarness.Engine/Private/AgentLoop.ps1](https://github.com/josh-j/pwsh-harness/blob/e56e989bbd68d1e6a1138c3755d6c76266700a78/src/PwshHarness/Modules/PwshHarness.Engine/Private/AgentLoop.ps1); [Modules/PwshHarness.Engine/Private/Budget.ps1](https://github.com/josh-j/pwsh-harness/blob/e56e989bbd68d1e6a1138c3755d6c76266700a78/src/PwshHarness/Modules/PwshHarness.Engine/Private/Budget.ps1)
- Basis: structural
- Confidence: high for the inspected supported distribution
- Caveats: Custom extension organizations and unobserved deployments are outside the boundary.

### Absence scope

- Surfaces inspected: Engine loop/authority/run policy; agent tool, work, task and lesson extensions; self-extend staging/approval/install; PowerShell verification; prompts, profiles, README and CONFIGURATION.
- Plausible first-party paths checked: snapshot/steering, shared parent-child limits, kill/status tools and user configuration
- Why no material first-party path remains: No shipped whole-harness current-view-to-discretionary-control loop is supplied; generic operator adjustment of a session is not a separately established parent S3 mode.

## S3* — Complementary audit

- State: A
- Function: Complementary challenge of a reported source defect before publication.
- Disturbance / variety regulated: A parent model can mistake a guard/caller/library premise and publish a false or unsupported finding.
- Decisive decision or feedback right: Judge whether the concrete claimed defect is supported, refuted, reproduced or unresolved after direct source/counterevidence inspection.
- Decision owner: Fresh read-only checker model invoked by report_finding; runtime parses/records the judgment.
- Supporting / enforcement mechanisms: Bounded readonly schemas, fresh provider exchange, exact file/line/trigger/consequence, observed-command provenance and completion policy.
- Closure path: Invoke-AgentFindingCheck returns verdict/premise/counterevidence to the parent; Get-AgentFindingReview rejects citing refuted findings and requests checked/qualified reporting in a further step.
- Boundary reachability: Bundled AgentTools installs work schemas and completion-review; AgentPresentation dispatches report_finding to Invoke-AgentFindingCheck; Engine Delegate creates the separate read-only exchange.
- Why this is / is not agent-owned: The model tests the disputed premise using callers/tests/guards, while deterministic parsing and answer reminders only enforce its evidence labels. Generic logs and routine parser/Pester checks are not credited.
- Evidence: [Extensions/agent/AgentWork.ps1](https://github.com/josh-j/pwsh-harness/blob/e56e989bbd68d1e6a1138c3755d6c76266700a78/src/PwshHarness/Extensions/agent/AgentWork.ps1); [Modules/PwshHarness.Engine/Private/AgentLoop.ps1](https://github.com/josh-j/pwsh-harness/blob/e56e989bbd68d1e6a1138c3755d6c76266700a78/src/PwshHarness/Modules/PwshHarness.Engine/Private/AgentLoop.ps1); [Extensions/agent/AgentTools.ps1](https://github.com/josh-j/pwsh-harness/blob/e56e989bbd68d1e6a1138c3755d6c76266700a78/src/PwshHarness/Extensions/agent/AgentTools.ps1); [Extensions/agent/AgentPresentation.ps1](https://github.com/josh-j/pwsh-harness/blob/e56e989bbd68d1e6a1138c3755d6c76266700a78/src/PwshHarness/Extensions/agent/AgentPresentation.ps1)
- Basis: structural
- Confidence: medium-high for this bounded audit mode
- Caveats: Parent selects the claim and both actors may share provider/model. Independence is fresh reasoning with separate direct source access, not institutional independence; no live witness or universal claim coverage.
- Claim being audited: Parent's reported defect at File/Line with Trigger/Consequence and optional executed reproduction.
- Ordinary reporting path: Parent's own source interpretation and draft final finding.
- Complementary access path: Fresh checker reads cited code, callers, guards and tests through independently selected readonly tools and searches for refutation.
- Independence boundary: New base messages and separate provider cache/replay, readonly actor, no nested delegates; it receives the claim rather than the parent's full reasoning transcript.
- Who acts on findings: Parent model revises/qualifies its finding; completion-review returns contradictions into subsequent operation when a step/time budget remains.

## S4 — Outside-and-then intelligence

- State: —
- Function: External/prospective capability adaptation is not established.
- Disturbance / variety regulated: Lessons summarize past workspace command success; /extend implements a directly requested extension. Neither path supplies environmental/future modelling that develops and selects an adaptation option.
- Decisive decision or feedback right: No qualifying function-specific decision/return path identified.
- Decision owner: No credited metasystem owner; developer/operator configuration and agent task decisions remain separate.
- Supporting / enforcement mechanisms: Session leases, run policies, budget enforcement, logs and ordinary approvals.
- Closure path: No qualifying function-specific closure.
- Why this is / is not agent-owned: Lessons summarize past workspace command success; /extend implements a directly requested extension. Neither path supplies environmental/future modelling that develops and selects an adaptation option.
- Evidence: [Extensions/agent/AgentLessons.ps1](https://github.com/josh-j/pwsh-harness/blob/e56e989bbd68d1e6a1138c3755d6c76266700a78/src/PwshHarness/Extensions/agent/AgentLessons.ps1); [Extensions/self-extend/Commands.ps1](https://github.com/josh-j/pwsh-harness/blob/e56e989bbd68d1e6a1138c3755d6c76266700a78/src/PwshHarness/Extensions/self-extend/Commands.ps1); [Extensions/self-extend/Authoring.ps1](https://github.com/josh-j/pwsh-harness/blob/e56e989bbd68d1e6a1138c3755d6c76266700a78/src/PwshHarness/Extensions/self-extend/Authoring.ps1)
- Basis: structural
- Confidence: high for the inspected supported distribution
- Caveats: Custom extension organizations and unobserved deployments are outside the boundary.

### Absence scope

- Surfaces inspected: Engine loop/authority/run policy; agent tool, work, task and lesson extensions; self-extend staging/approval/install; PowerShell verification; prompts, profiles, README and CONFIGURATION.
- Plausible first-party paths checked: lesson collection/reinjection, retrieval, model fallback, /extend generation and source-approved live installation
- Why no material first-party path remains: Capability installation is real, but its input is an ordinary description-driven authoring task; no shipped outside-and-then intelligence or parent-owned prospective adaptation conversation closes S4.

## S5 — Policy and identity

- State: —
- Function: Identity/ultimate-policy closure is not established.
- Disturbance / variety regulated: Live Auto activation, source-bound extension approval and risk capability labels constrain ordinary task/extension execution without addressing system identity or balancing S3/S4.
- Decisive decision or feedback right: No qualifying function-specific decision/return path identified.
- Decision owner: No credited metasystem owner; developer/operator configuration and agent task decisions remain separate.
- Supporting / enforcement mechanisms: Session leases, run policies, budget enforcement, logs and ordinary approvals.
- Closure path: No qualifying function-specific closure.
- Why this is / is not agent-owned: Live Auto activation, source-bound extension approval and risk capability labels constrain ordinary task/extension execution without addressing system identity or balancing S3/S4.
- Evidence: [Modules/PwshHarness.Engine/Private/AgentAuthority.ps1](https://github.com/josh-j/pwsh-harness/blob/e56e989bbd68d1e6a1138c3755d6c76266700a78/src/PwshHarness/Modules/PwshHarness.Engine/Private/AgentAuthority.ps1); [Extensions/self-extend/Approval.ps1](https://github.com/josh-j/pwsh-harness/blob/e56e989bbd68d1e6a1138c3755d6c76266700a78/src/PwshHarness/Extensions/self-extend/Approval.ps1); [Extensions/self-extend/Commands.ps1](https://github.com/josh-j/pwsh-harness/blob/e56e989bbd68d1e6a1138c3755d6c76266700a78/src/PwshHarness/Extensions/self-extend/Commands.ps1)
- Basis: structural
- Confidence: high for the inspected supported distribution
- Caveats: Custom extension organizations and unobserved deployments are outside the boundary.

### Absence scope

- Surfaces inspected: Engine loop/authority/run policy; agent tool, work, task and lesson extensions; self-extend staging/approval/install; PowerShell verification; prompts, profiles, README and CONFIGURATION.
- Plausible first-party paths checked: Auto/Approve selection, revoke-on-context-change, run policy, prompt and extension capability approvals
- Why no material first-party path remains: No identity/ultimate-policy issue is escalated to a legitimate parent and returned as authoritative governing policy; ordinary consent/configuration is insufficient.

## Distributed OSS parent arrangement

Contributor/packaging activity is outside the installed runtime. Local operator authority is not organization-wide parent governance.

## Self-hosted and non-human modes

Auto and Approve preserve different operation authorization; self-extend always requires explicit source approval. These are not separately proven S3/S4/S5 parent modes.

## Recursion

Readonly delegates have bounded subtasks, no autonomous metasystem and no recursive viability claim. Background commands do not add S1 units.

## Variety and escalation

Authority epochs, confinement, bounded retries, failure reports and live steering retain task feedback. Logging failures stop action; that fail-closed behavior alone is not an algedonic channel.

## Evidence gaps

Static source inspection only. PowerShell 7.6 and Pester are unavailable, so native execution/tests were not run. No provider/LLM or generated extension was executed. Complementary audit credit is limited to the actually wired optional finding checker; no claim about audit effectiveness, product quality or all reported findings is made.

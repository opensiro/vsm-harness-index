---
harness_id: meldwork
project_name: Meldwork
repository: https://github.com/Ryder-Sun/Meldwork
review_ref: 4c522c0997035af8b931e5420f48b3edc3177a05
reviewed_at: 2026-10-27
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Meldwork

## Review boundary

- System in focus: one supported Meldwork V4 Auto Discussion group conversation and its configured agent participants in the local Electron desktop product, not all unrelated conversations or the development organization.
- Purpose and identity: obtain a negotiated multi-agent solution, execute owned contributions, independently verify the final artifact, and deliver a group result to a human user.
- Relevant environment: user task, local desktop files and knowledge sources, configured external agent CLI/model providers, permissions, runtime failures and operator gates.
- Standard-distribution boundary: the installed desktop main process, V4 collaboration and workspace runner, supported agent connectors, persistence, review evidence and Human Gate. Model cognition runs in configured external providers, not an in-repository model.
- Credited operating / distribution surfaces: `desktop/src/collaboration/orchestration-v4-records.cjs`, `desktop/src/workspace/local-workspace-auto-runner-v4-*.cjs`, `desktop/src/runs/`, provider/connector integration and the local UI's shipped V4 flow.
- Adjacent first-party surfaces excluded from ownership: V1–V3 modes, marketing site, tests and mock providers, repository contributors, release/CI, optional Cloud/Channel connector operation without a V4 group, and conversations outside the group assessed.
- First-party operating / deployment modes considered: packaged local desktop, direct one-to-one agent chat, group conversations, V4 proposal/challenge/negotiated work/synthesis/verification, user permission/budget gates and local persistence. No hosted tenant service or autonomous scheduler is presumed.
- Recursion level: one group discussion whose S1 units are configured participant agent invocations; one chat message or renderer component is not a separate viable recursion.
- Reviewed revision: `4c522c0997035af8b931e5420f48b3edc3177a05`.
- Observation date: 2026-10-27.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Meldwork is a locally installed Electron/Vue desktop application. Its main process is the trusted control boundary, while a limited preload bridge exposes functions to the renderer. Configured external agent providers supply contextual decisions and tool output; the main process handles session invocation, durable records, per-run quotas, failure classification, permission gates and conversation-scoped single-writer enforcement. V4 records bind proposal/challenge receipts to immutable context and a plan hash, then issue dependency-aware work assignments to negotiated owners. A designated finalizer synthesizes artifacts; distinct agents verify directly supplied artifacts, digests and evidence, and an acceptance gate requires supporting findings. A human may resolve unknown writable outcomes or permission/budget decisions. The user documentation explicitly notes conversations do not wait for one another, so cross-conversation file collision control is not credited here.

Primary sources: [architecture](https://github.com/Ryder-Sun/Meldwork/blob/4c522c0997035af8b931e5420f48b3edc3177a05/architecture.md), [V4 coordination record rules](https://github.com/Ryder-Sun/Meldwork/blob/4c522c0997035af8b931e5420f48b3edc3177a05/desktop/src/collaboration/orchestration-v4-records.cjs), and [V4 runner](https://github.com/Ryder-Sun/Meldwork/blob/4c522c0997035af8b931e5420f48b3edc3177a05/desktop/src/workspace/local-workspace-auto-runner-v4-discussion.cjs).

## Operational model

External provider-backed participant agents produce proposals, challenges, work and review judgments. Meldwork's shipped orchestrator controls when each distinct role is invoked and validates typed receipts; it does not itself own the LLM's substantive action or verdict. An accepted group result requires agreement over the same coordination-plan hash and later separate verification of actual synthesis content. The normal budget/watchdog and human approval mechanisms enforce conditions, but do not demonstrate a discretionary autonomous whole-group S3 function. The observed evidence is source-based; no live model/provider execution was performed.

## S1 — Operations

- State: A
- Function: produce agent-owned task proposals, implementation/analysis artifacts and final synthesis through configured provider-backed participant sessions.
- Disturbance / variety regulated: different task requirements, peer objections, tool feedback, partial work and failing provider invocations.
- Decisive decision or feedback right: propose a solution, revise a challenge response, choose the substantive content of an owned work artifact and synthesize task evidence.
- Decision owner: configured external model-backed participant agents, reached through first-party desktop connector and V4 runner; not the Electron scheduler.
- Supporting / enforcement mechanisms: provider invocation, persistent snapshot/receipt records, context packs, assigned roles, artifact storage and Human Gate.
- Closure path: the participant receives context/peer challenge, returns a decision/artifact receipt, and the V4 discussion runner uses that receipt to advance or require another agent turn.
- Boundary reachability: these invocations form the documented supported V4 Auto Discussion path in the installed desktop, not a mock, test or plugin-only example.
- Why this is / is not agent-owned: task-specific proposals and artifacts require the configured agents' contextual judgments; deterministic records and queues alone cannot determine their contents.
- Evidence: [V4 runner proposal/challenge/work](https://github.com/Ryder-Sun/Meldwork/blob/4c522c0997035af8b931e5420f48b3edc3177a05/desktop/src/workspace/local-workspace-auto-runner-v4-discussion.cjs#L600-L753), [architecture modes and provider boundary](https://github.com/Ryder-Sun/Meldwork/blob/4c522c0997035af8b931e5420f48b3edc3177a05/architecture.md).
- Basis: explicit and structural.
- Confidence: medium-high.
- Caveats: external providers are optional and need user configuration; no outcome or provider quality is claimed.

## S2 — Coordination

- State: A
- Function: negotiate compatible cross-agent responsibilities before work to reduce ownership conflicts and conflicting plans inside one group.
- Disturbance / variety regulated: multiple agents may propose incompatible task partitions, duplicate responsibilities, or disagree on the finalizer and dependencies.
- Decisive decision or feedback right: individually challenge, support or contradict a common plan; collectively admit a single unanimous normalized coordination-plan hash before work starts.
- Decision owner: distinct configured proposal/challenge agents; first-party plan validation is deterministic enforcement of their consensus.
- Supporting / enforcement mechanisms: challenge bindings, signed/linked receipts, target-kind membership, common plan hash, assignments, dependency-aware work scheduling and a designated finalizer.
- Closure path: each agent receives competing candidate plans and challenges them; unanimous support receipts select the same plan hash; the runner turns agreed assignments into later agent work and repeats challenge when there is no agreement.
- Boundary reachability: the V4 Auto Discussion group flow invokes proposal then challenge as normal operating phases and blocks work until a valid coordination plan exists.
- Why this is / is not agent-owned: participant agents own distinct approval/contradiction judgments; code verifies the agreement and changes work allocation but does not choose the substantive partition for them.
- Distinct S1 units: agent kinds bound to separate participant slots and challenge receipts.
- Inter-S1 disturbance: conflicting planned responsibility/ownership over the shared group task, not merely a transport or message-order concern.
- Attenuating coordination relation: unanimous plan support plus allocated owner, dependency and finalizer identities suppress incompatible concurrent work and duplicates within the group.
- Feedback into subsequent S1 behaviour: accepted responsibilities select subsequent work prompts and the finalizer; disagreement invokes another challenge round.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: independent agent review and a shared plan hash determine who may do what before any work is admitted, actively handling competing plans.
- Evidence: [coordination unanimity](https://github.com/Ryder-Sun/Meldwork/blob/4c522c0997035af8b931e5420f48b3edc3177a05/desktop/src/collaboration/orchestration-v4-records.cjs#L600-L668), [challenge to work transition](https://github.com/Ryder-Sun/Meldwork/blob/4c522c0997035af8b931e5420f48b3edc3177a05/desktop/src/workspace/local-workspace-auto-runner-v4-discussion.cjs#L619-L753).
- Basis: explicit and structural.
- Confidence: high.
- Caveats: the controller can still permit separate conversations to collide on disk; S2 here is limited to the declared V4 group and is not global file-lock arbitration.

## S3 — Inside-and-now control

- State: —
- Function: no separately owned whole-group discretionary current-control judgment was established beyond agent-work coordination and deterministic enforcement.
- Disturbance / variety regulated: budget exhaustion, failed/late invocations, stalled agents and writable-state ambiguity.
- Decisive decision or feedback right: no autonomous or parent-governed whole-system balancing/commitment choice separate from single-group workflow enforcement established.
- Decision owner: none established at this function; operator controls budgets/permissions and scheduler enforces preselected limits.
- Supporting / enforcement mechanisms: per-run budgets, invocation watchdog, stop/cancel handling, one conversation-scoped writer and Human Gates for unknown write outcomes.
- Closure path: quota checks or user gates stop/retry individual runs; these do not evidence a distinct manager evaluating and reallocating the group's overall current commitments.
- Why this is / is not agent-owned: a runner that orders dependencies and consumes receipts is S2/workflow infrastructure, and a human granting permission is not by itself S3.
- Evidence: [architecture scheduling/Human Gate](https://github.com/Ryder-Sun/Meldwork/blob/4c522c0997035af8b931e5420f48b3edc3177a05/architecture.md#L20-L24), [V4 phase runner](https://github.com/Ryder-Sun/Meldwork/blob/4c522c0997035af8b931e5420f48b3edc3177a05/desktop/src/workspace/local-workspace-auto-runner-v4-discussion.cjs).
- Basis: structural.
- Confidence: medium.
- Caveats: a human can pause or reject operations, but no established separately owned whole-group S3 parent decision loop was evidenced.

### Absence scope

- Surfaces inspected: local desktop trust boundary, per-agent/run scheduler, Human Gate, V4 control and phase transitions, work and completion logic.
- Plausible first-party paths checked: budget admission, writer leases, failure retry, cancellation, user gate and group-run task/finalizer control.
- Why no material first-party path remains: these surfaces bound or sequence one operation/conversation but do not demonstrate whole-group discretionary present-state tradeoff ownership distinct from S1/S2.

## S3* — Complementary audit

- State: A
- Function: independently challenge the synthesized result using primary artifact content and binding evidence instead of trusting the producing finalizer's completion claim.
- Disturbance / variety regulated: a finalizer's purported output may be unsupported by stored artifact content, lack evidence or conflict with independent reviewer findings.
- Decisive decision or feedback right: a non-writer agent can issue independently attributed review findings and a `support` or adverse verdict that affects acceptance.
- Decision owner: independently invoked configured verification agents, explicitly excluding the synthesis writer; deterministic acceptance only checks their returned evidence and verdicts.
- Supporting / enforcement mechanisms: reviewer binding filtered away from writer, immutable artifact ID/hash, direct stored artifact context, attributed finding records and acceptance guard.
- Closure path: the verifier receives the stored synthesis artifact and its digest, records a finding bound to the exact content/run, and a non-support/open finding blocks acceptance and drives another V4 round.
- Boundary reachability: V4 uses this non-writer verification path as a first-party production phase in its normal group execution; it does not require test harnesses or manually invented reviewer roles.
- Why this is / is not agent-owned: a distinct model-backed agent controls the substantive verification finding; content/hash verification by the runner ensures accountability but is not the audit judgment.
- Ordinary reporting path: synthesis-finalizer receipt and typed task/artifact claims.
- Complementary access path: another agent reads the stored final artifact and evidence independently of the writer, rather than only repeating its summary or self-reported status.
- Independence and returned control: writer-kind exclusion, distinct reviewer attribution, artifact-linked adversarial findings and acceptance veto create an independent corrective return to the V4 controller.
- Evidence: [non-writer verifier selection](https://github.com/Ryder-Sun/Meldwork/blob/4c522c0997035af8b931e5420f48b3edc3177a05/desktop/src/workspace/local-workspace-auto-runner-v4-synthesis.cjs#L28-L52), [content-based findings and acceptance](https://github.com/Ryder-Sun/Meldwork/blob/4c522c0997035af8b931e5420f48b3edc3177a05/desktop/src/workspace/local-workspace-auto-runner-v4-outcomes.cjs#L275-L351), [artifact context to verifier](https://github.com/Ryder-Sun/Meldwork/blob/4c522c0997035af8b931e5420f48b3edc3177a05/desktop/src/workspace/local-workspace-auto-runner-v4-delivery.cjs#L200-L341), [acceptance guard](https://github.com/Ryder-Sun/Meldwork/blob/4c522c0997035af8b931e5420f48b3edc3177a05/desktop/src/workspace/local-workspace-auto-runner-v4-outcomes.cjs#L575-L630).
- Basis: structural and explicit.
- Confidence: medium.
- Caveats: although verification is a normal V4 phase, its distinct source-of-truth access and owner separate it from a mere repeated checklist. Evidence establishes an independent complementary audit **path**, not that external provider judgments are reliably correct or statistically independent.

## S4 — Outside-and-then intelligence

- State: —
- Function: no durable forward-looking adaptation to a changing external environment established in the supported group runtime.
- Disturbance / variety regulated: evolution of provider capabilities, task domain and future operating conditions, if an adaptation function existed.
- Decisive decision or feedback right: no separate agent-owned or parent-closed environmental scan, option selection and implementation loop found.
- Decision owner: none established.
- Supporting / enforcement mechanisms: configurable providers/connectors, skills, knowledge sources, V4 task proposals and failure policy.
- Closure path: changes to a present task's plan or provider retry can affect current execution, but do not feed a future-facing strategy back into the group identity or operating capabilities.
- Why this is / is not agent-owned: proposal/challenge rounds solve the given task, not long-horizon adaptation of the system itself.
- Evidence: [architecture/deployment boundary](https://github.com/Ryder-Sun/Meldwork/blob/4c522c0997035af8b931e5420f48b3edc3177a05/architecture.md), [V4 discussion phases](https://github.com/Ryder-Sun/Meldwork/blob/4c522c0997035af8b931e5420f48b3edc3177a05/desktop/src/workspace/local-workspace-auto-runner-v4-discussion.cjs).
- Basis: structural.
- Confidence: medium.
- Caveats: future-oriented prompts can be entered by a user, but are not a shipped standing S4 loop for the harness.

### Absence scope

- Surfaces inspected: V4 planning/work/review, connectors, knowledge-source configuration, scheduler and local persistence.
- Plausible first-party paths checked: iterative discussion, retries after provider failure, model changes by the user, optional Cloud/Channel connectors.
- Why no material first-party path remains: these are current-task loops or user configuration; no distinct ongoing external-environment intelligence and implemented adaptation was located.

## S5 — Policy and identity

- State: —
- Function: no closed ultimate-purpose/identity dispute and legitimate parent decision loop in a V4 group.
- Disturbance / variety regulated: fundamental conflicts about a group's charter or non-negotiable identity, rather than task solution disagreement.
- Decisive decision or feedback right: no such legitimate identity-level decision right established inside the shipped desktop runtime.
- Decision owner: none established for S5 at this recursion.
- Supporting / enforcement mechanisms: permissions, credentials, Human Gates, trusted Electron IPC and human task goals.
- Closure path: an operator's allowed/denied tool request or a group's accepted task plan changes operational execution but is not ultimate organizational policy adjudication.
- Why this is / is not agent-owned: participant consensus is over a task responsibility graph; the product owner and human user's task instructions do not establish a separate S5 identity function within the deployed group.
- Evidence: [architecture and permission boundary](https://github.com/Ryder-Sun/Meldwork/blob/4c522c0997035af8b931e5420f48b3edc3177a05/architecture.md), [V4 agreed plan schema](https://github.com/Ryder-Sun/Meldwork/blob/4c522c0997035af8b931e5420f48b3edc3177a05/desktop/src/collaboration/orchestration-v4-records.cjs).
- Basis: structural.
- Confidence: medium.
- Caveats: developer governance and the user's own policy authority are adjacent actors, not auto-credited as a runtime S5 loop.

### Absence scope

- Surfaces inspected: Human Gates, task/role bindings, plan consensus, user trust/permission controls, connector configuration and desktop architecture.
- Plausible first-party paths checked: unanimous task plans, permission denial, explicit human intervention, user/provider configuration and contributor policy.
- Why no material first-party path remains: the decisions govern current task progress, runtime safety and external project maintenance, not an escalated existential policy matter with an identified legitimate S5 closure.

## Distributed OSS parent arrangement

The public repository's maintainers govern code and releases, but their contribution policy does not govern the identity of a particular deployed V4 conversation. Its users provide the task charter and can authorize execution at the Human Gate; that does not import developer or user identity governance as a proved group S5.

## Self-hosted and non-human modes

Meldwork runs locally with optional configured connectors. Multiple external model agents can negotiate and verify without a human message for each phase, while human budget/permission/writable-recovery gates remain possible. Autonomy claims require these configured providers and apply to the V4 group path only.

## Recursion

The V4 group contains individual agent sessions. They have local task decisions, but the repository evidence does not warrant a claim that every session is an independent complete viable organization. Separate group conversations have distinct writer controls and are not assessed as one coordinated viable aggregate.

## Variety and escalation

Negotiated responsibility graphs attenuate conflict among contributors before work, and direct artifact review provides a complementary corrective signal. A failed challenge revisits coordination; an adverse independent review prevents acceptance. Runtime failures and unknown writable outcomes move to retry/stop/Human Gate, not automatically to a distinct S3, S4 or S5 authority.

## Evidence gaps

- S3*: agent independence is established by role exclusion and content-bound review records, but the code cannot establish genuine statistical independence or audit accuracy for an externally configured provider; no live evaluation was performed.
- S2 is scoped strictly to a group; the architecture acknowledges separate conversations do not coordinate file writes with each other.
- No current-state whole-group S3 or future adaptation loop was credited merely from deterministic phase/limit machinery.
- Optional providers and connectors were inspected structurally at a pinned source revision; a live authenticated desktop run was outside the review scope.

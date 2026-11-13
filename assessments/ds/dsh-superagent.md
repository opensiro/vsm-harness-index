---
harness_id: dsh-superagent
project_name: dsh-superagent
repository: https://github.com/deepseek-ai/dsh-superagent-prototype
review_ref: 8c32a9dc5d72c033816c6a8110b37f40cf94fba4
reviewed_at: 2026-11-13
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: P
---

# dsh-superagent

## Review boundary

- System in focus: One installed dsh-superagent bundle serving one configured GitHub repository.
- Purpose and identity: Turn authorized repository requests and eligible observations into bounded implementation work and deliver its outcome.
- Relevant environment: GitHub issues, pull requests, and check feedback, optional Feishu messages, a DeepSeek Harness host and inference provider, and a deployment operator.
- Standard-distribution boundary: The bundle manifest and runtime, its GitHub and optional Feishu adapters, orchestrator and worker role instructions and tools, ticket store, worker executor and management panel. The external DeepSeek Harness host supplies session execution and tool services.
- Credited operating / distribution surfaces: The bundle-wired main and worker sessions, trigger evaluation and routing, worker hand-back and reporting, operator load and ticket views, versioned policy settings and enforcement.
- Adjacent first-party surfaces excluded from ownership: Development and test fixtures and maintenance of the upstream bundle. External GitHub reviewers, checks and hosted inference supply inputs or execution services at the deployment boundary.
- First-party operating / deployment modes considered: Explicit requests in off, observe and auto modes, inferred decisions in observe and auto, optional Feishu source, and supervised management through the operator panel. Inferred observation in observe mode records a prospective ticket decision without launching a worker.
- Recursion level: The one-repository deployment, with per-ticket worker cells below it and the human deployment operator as parent.
- Reviewed revision: `8c32a9dc5d72c033816c6a8110b37f40cf94fba4`.
- Observation date: 2026-11-13.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

Source adapters normalize events into triggers. The engine preserves source positions, thread subscriptions, evaluations, decisions and ticket assignments. A main DSH session receives candidate and ticket context. The bundle binds its own role instructions and tools to that session and to persistent per-ticket DSH worker sessions. A worker receives its mandate and input in its own workspace, can operate within the mandate, and returns structured reports. An operator panel exposes deployment health, ticket state, settings and intervention actions. This review credits the role and feedback wiring supplied by the bundle. The host and its model provide the underlying agent services. [docs/001-domain.md](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/docs/001-domain.md#L25-L43), [src/app/runtime.ts](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/src/app/runtime.ts#L113-L168), [src/app/sessions.ts](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/src/app/sessions.ts#L137-L155), [docs/003-execution.md](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/docs/003-execution.md#L23-L61), [src/app/views/overview.ts](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/src/app/views/overview.ts#L38-L79).

## Operational model

The repeating operational outcome is a bounded repository change or disposition of the authorized ticket. Distinct worker sessions can serve multiple tickets concurrently against the same repository, including tickets that follow the same source thread. The main session assesses and routes new demand, while workers choose implementation and judge their own scope. The deployment operator manages current load and the standing mandate. The source participant who asks for work and the maintainer who reviews a resulting PR have narrower rights. [docs/001-domain.md](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/docs/001-domain.md#L43-L58), [docs/002-authorization.md](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/docs/002-authorization.md#L18-L42), [docs/003-execution.md](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/docs/003-execution.md#L55-L61).

## S1 — Operations

- State: A
- Function: Complete a bounded repository work item through the worker's investigation, implementation and disposition.
- Disturbance / variety regulated: Heterogeneous change requests, repository conditions, incoming feedback and task blockers.
- Decisive decision or feedback right: Choose how to investigate and implement the accepted change, whether new inputs fit the mandate, and what outcome the ticket can report.
- Decision owner: The bundle-wired ticket worker session. The main session controls acceptance and routing, and the operator or repository maintainer retains external authorization and review rights.
- Supporting / enforcement mechanisms: Per-ticket workspaces and persistent DSH sessions, ticket mandates, tool bindings and structured report schemas.
- Closure path: Acceptance creates the ticket and mandate, the executor launches the worker session, and the worker's report updates the assignment and determines whether work continues, awaits input or ends. A bound PR can keep the ticket open through review and closure.
- Boundary reachability: The standard runtime wires worker tools and prompts into the session that the ticket executor launches.
- Why this is / is not agent-owned: Removing the worker's judgment leaves launch and state handling but removes implementation choices and the resulting work.
- Evidence: [src/core/evals.ts](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/src/core/evals.ts#L306-L316), [src/app/runtime.ts](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/src/app/runtime.ts#L119-L132), [src/app/tools/executor.ts](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/src/app/tools/executor.ts#L66-L105), [src/core/assignments.ts](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/src/core/assignments.ts#L99-L134), [prompts/worker.md](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/prompts/worker.md#L1-L10).
- Basis: structural
- Confidence: high
- Caveats: The result is scoped to authorized work. Inferred candidates only dispatch automatically in auto mode. Hosted DSH model behavior and maintainer acceptance are external.

## S2 — Coordination

- State: A
- Function: Resolve ambiguous or overlapping ownership of follow-up work among ticket workers sharing a source thread.
- Disturbance / variety regulated: A follow-up can reach several tickets with different mandates. A misplaced or duplicate assignment can make multiple workers act on the same request or leave it with the wrong worker.
- Decisive decision or feedback right: Each affected worker judges whether to retain or hand back the follow-up. When ownership is released, the main session judges whether to attach it elsewhere, create distinct work or ignore it.
- Decision owner: The shipped ticket worker roles and main orchestrator role, at their respective points in the hand-back loop.
- Supporting / enforcement mechanisms: Recorded trigger disposition and subscriptions, refusal of premature rerouting, requeue only after other ticket owners release the message, and an idempotent accept by trigger.
- Closure path: A worker returns out-of-scope work with a reason. When no ticket still owns it, the next candidate carries the reasons and the main session can reroute. Attach supplies input to the selected ticket; accept creates a separate ticket.
- Boundary reachability: Worker hand-back and main routing tools are registered by the runtime for active ticket and main sessions.
- Why this is / is not agent-owned: The runtime enforces the hand-back conditions. It does not choose whether a concrete follow-up fits a ticket's mandate or which ticket should receive released work.
- Distinct S1 units: Concurrent ticket workers with independent mandates and persistent sessions in the same deployment.
- Inter-S1 disturbance: Shared source threads can carry separate pieces of work and reach several ticket workers, with scope overlap or mistaken assignment of a new follow-up.
- Attenuating coordination relation: Workers judge ownership and release misrouted input, and the main role can attach the released input to a better-fitting ticket using current ticket summaries.
- Feedback into subsequent S1 behaviour: The return reason becomes candidate context. The subsequent routing result changes which worker receives an actionable input and under which mandate it acts.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The return is tied to an identified ownership conflict across live units. The runtime blocks a second assignment while a ticket still owns the follow-up.
- Evidence: [docs/001-domain.md](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/docs/001-domain.md#L45-L58), [docs/002-authorization.md](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/docs/002-authorization.md#L18-L42), [src/core/evals.ts](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/src/core/evals.ts#L183-L191), [src/core/engine.ts](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/src/core/engine.ts#L100-L125), [prompts/dispatch.md](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/prompts/dispatch.md#L31-L51).
- Basis: structural
- Confidence: medium
- Caveats: This witness concerns scoped input ownership. It does not establish general file-conflict detection or contention-aware scheduling across arbitrary worktrees.

## S3 — Inside-and-now control

- State: P
- Function: Regulate current deployment load and active commitments through operator decisions about concurrency, pause/resume and intervention on open tickets.
- Disturbance / variety regulated: Queue pressure, stalled tickets, execution capacity and delivery problems across the deployment.
- Decisive decision or feedback right: Change the operating capacity or suspend/resume the deployment and intervene in live commitments from its current view.
- Decision owner: Deployment operator. The main session can request a missing ticket report and routes individual work, while the executor enforces configured capacity.
- Supporting / enforcement mechanisms: Overview health and ticket projections, revisioned settings, worker-slot accounting, ticket stop/retry commands and the processing pass.
- Closure path: The operator reads active load and commitments, saves an executor setting or pauses/resumes processing, or stops/retries a ticket. The runtime uses the changed setting for subsequent work, or terminates/replaces the assignment.
- Boundary reachability: The shipped panel reads overview and calls management routes on the same runtime and store that govern dispatch.
- Why this is / is not agent-owned: The main role's local accountability action asks an idle worker for a report. Retry and control settings require explicit human direction. The supported autonomous role has no evidenced independent deployment-wide resource or intervention decision loop.
- Whole-system current view: The deployment overview combines open tickets, work awaiting a person, executor load, configured capacity and active operational problems.
- Current-control decision scope: Global dispatch capacity and processing state, with operator intervention in individual commitments from that whole view.
- Evidence: [src/app/views/overview.ts](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/src/app/views/overview.ts#L38-L79), [src/app/http.ts](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/src/app/http.ts#L157-L204), [src/app/settings.ts](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/src/app/settings.ts#L176-L213), [src/app/tools/main.ts](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/src/app/tools/main.ts#L161-L174), [src/app/tools/main.ts](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/src/app/tools/main.ts#L249-L264), [docs/003-execution.md](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/docs/003-execution.md#L55-L61).
- Basis: structural
- Confidence: medium
- Caveats: Pause governs new evaluation, dispatch and delivery. It is distinct from stopping already-running work.

## S3* — Complementary audit

- State: —
- Function: Complementary examination of operational claims through a separately scoped evidence and judgment path.
- Disturbance / variety regulated: A worker's ordinary report may omit or mischaracterize the implementation result.
- Decisive decision or feedback right: No bundled independent actor was found that examines the actual work and returns an audit judgment to deployment control.
- Decision owner: No first-party audit owner established in this deployment.
- Supporting / enforcement mechanisms: Ticket and decision histories, model admission records, external PR review and check ingestion, and ordinary worker reports.
- Closure path: External review/check feedback returns to the ticket worker. The main role consumes summaries and can request an ordinary missing report.
- Why this is / is not agent-owned: The admission judgment concerns prospective requests. PR reviewers are external actors. The worker's own report and its assessment of review feedback are operational reporting.
- Evidence: [prompts/dispatch.md](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/prompts/dispatch.md#L44-L58), [src/app/tools/main.ts](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/src/app/tools/main.ts#L167-L174), [src/sources/github-trigger.ts](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/src/sources/github-trigger.ts#L48-L76), [src/app/tools/executor.ts](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/src/app/tools/executor.ts#L75-L105), [docs/003-execution.md](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/docs/003-execution.md#L82-L108).
- Basis: structural
- Confidence: medium
- Caveats: External CI or reviewer evidence can affect implementation. The deployment supplies no independent audit owner or a separately configured first-party audit role.

### Absence scope

- Surfaces inspected: Runtime role/tool registration, orchestrator and worker prompts, worker reporting, the operator view, GitHub trigger integration and PR lifecycle.
- Plausible first-party paths checked: Main role reads and status requests, nested worker sessions, evaluation records and PR review/check callbacks.
- Why no material first-party path remains: The main role is directed away from independent technical investigation, nested workers inherit the ticket worker's permissions and context boundary, and external observations return through the ordinary worker path without a separately assigned first-party audit judgment.

## S4 — Outside-and-then intelligence

- State: —
- Function: Develop and return an adaptation option for the future capability of the deployment.
- Disturbance / variety regulated: Changes in the deployment's environment that may call for a new capability or operating arrangement.
- Decisive decision or feedback right: No bundled loop was found that develops capability adaptation options from an external/prospective distinction and returns a decision to deployment control.
- Decision owner: No first-party adaptation owner established at this recursion.
- Supporting / enforcement mechanisms: Source observation and replay, observe mode, model and source settings, and versioned operator prompt configuration.
- Closure path: Observations become ticket decisions, including prospective accepts in observe mode. An operator can enable auto or edit settings and prompts using the management surface.
- Why this is / is not agent-owned: The main role assesses whether a concrete request fits current rules. The observe-to-auto recommendation is an operator deployment calibration step, with prospective ticket records rather than generated alternatives for changing deployment capability.
- Evidence: [docs/002-authorization.md](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/docs/002-authorization.md#L91-L105), [src/policy.ts](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/src/policy.ts#L40-L64), [src/app/tools/main.ts](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/src/app/tools/main.ts#L249-L277), [src/app/prompts.ts](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/src/app/prompts.ts#L135-L174), [SETUP.md](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/SETUP.md#L56-L72).
- Basis: structural
- Confidence: medium
- Caveats: The operator can use external analysis to change configuration. The boundary is the deployment's shipped operational loop.

### Absence scope

- Surfaces inspected: Candidate assessment and policy outcomes, source-to-trigger integration, observe/auto deployment guidance, management tools and prompt versioning.
- Plausible first-party paths checked: Proactive request assessment, observe-to-auto calibration, configurable sources/models, and policy/prompt revisions.
- Why no material first-party path remains: The runtime processes present requests against the existing mandate. The shipped management path persists operator choices but does not connect environmental sensing to generation and selection of future capability alternatives.

## S5 — Policy and identity

- State: P
- Function: Establish and revise the standing mandate for which repository demand the deployment may take up.
- Disturbance / variety regulated: Conflicting or changing expectations about who may authorize work, which classes of changes are in scope, and whether inferred work may be undertaken.
- Decisive decision or feedback right: Choose the deployment-wide admission policy, allowed authorities, rule scope and mode.
- Decision owner: The deployment operator, acting directly through the panel or by explicit configuration instruction.
- Supporting / enforcement mechanisms: Policy and mode schema, settings revision, computed policy version, admission checks, affected-ticket notifications and later mandate revalidation.
- Closure path: The operator changes the standing mandate after examining decision records or deployment needs. The saved version changes subsequent evaluation, queues stale evaluations anew, and sends relevant changes to affected active tickets. The executor revalidates ended work before resuming under its mandate.
- Boundary reachability: The standard deployment exposes policy settings and decision records. Both the panel and explicit-request tool save through the runtime settings service read by evaluation.
- Why this is / is not agent-owned: The main role applies the standing policy. Its settings tool is scoped to explicit human configuration requests, and assessed source content does not authorize a change in policy.
- Identity / ultimate-policy issue: The deployment's enduring authorization envelope for proactive repository work, beyond any individual ticket approval.
- Ultimate authority in each claimed mode: The deployment operator sets the policy, including in auto mode.
- Return-to-operation path: Versioned settings feed the next admission decisions and revalidation; relevant changes are delivered to affected live workers.
- Evidence: [docs/002-authorization.md](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/docs/002-authorization.md#L91-L141), [src/app/tools/main.ts](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/src/app/tools/main.ts#L249-L264), [src/app/settings.ts](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/src/app/settings.ts#L176-L195), [src/core/engine.ts](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/src/core/engine.ts#L252-L257).
- Basis: structural
- Confidence: medium
- Caveats: A policy change does not immediately revoke all active mandates. Its effects depend on scope, notifications and the next decision or revalidation path.

## Distributed OSS parent arrangement

The assessed operator is the parent of one deployment. Upstream maintainership of the bundle, source repository contribution governance and external review decisions belong to other boundaries.

## Self-hosted and non-human modes

Self-hosted operation supports the human deployment operator and autonomous ticket execution. The operating modes alter inferred admission, without transferring deployment-level policy authority to the agent.

## Recursion

The deployment supervises ticket workers. A ticket worker can use host-provided subagents within its mandate. The latter are nested work helpers, with no separate deployment-level decision rights credited here.

## Variety and escalation

Admission and scope judgments attenuate diverse incoming demand. Worker hand-back, blocked or failed reports, operator attention and manual stops provide distinct feedback channels. The evidence supports scoped escalation, without a separately established deployment-level algedonic mechanism.

## Evidence gaps

The assessment uses pinned source, prompts and documented supported modes. It did not run a live DSH or GitHub/Feishu deployment. The S2 evidence is scoped to ambiguous shared-thread ownership, and the absence judgments are scoped to first-party paths at this revision.

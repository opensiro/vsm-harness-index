---
harness_id: openoutbound
project_name: OpenOutbound
repository: https://github.com/xyluxx/openoutbound
review_ref: bc158cac6548ab54699442d159cc2130570b9a78
reviewed_at: 2026-11-14
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C(P)
autonomy_s3_star: C
autonomy_s4: C(P)
autonomy_s5: P
---

# OpenOutbound

## Review boundary

- System in focus: One self-hosted OpenOutbound workspace, including the first-party outbound execution engine, embedded LLM brain decisions, campaign and inbox jobs, safety/approval mechanisms, workspace operating-state views, strategy change proposals and supplied Agent Skill/MCP construction path. Do not credit external agent hosts as installed internal autonomous managers.
- Purpose and identity: Conduct bounded outbound sales/customer communications for the workspace owner's defined commercial goals, with controlled campaign execution, prospective adjustments, consent and risk limits.
- Relevant environment: Prospects and replies, companies and campaigns, sending provider outcomes, market signals, mailboxes, channel limits, CRM state, human owner policy and model/provider availability.
- Standard-distribution boundary: Shipped TypeScript engine and modules, built-in AI brain invocation, CLI/REST/MCP operations and supported Agent Skill as explicit construction surface. An arbitrary outside Claude/Codex/ChatGPT MCP agent is not silently first-party installed autonomous ownership.
- Credited operating / distribution surfaces: src/brain/service.ts, src/modules/inbox/classify.ts and actions.ts, src/modules/campaigns/enrollment.ts and control.ts, src/modules/reports/attention/build.ts, src/modules/strategy/proposals.ts and review.ts, src/modules/email/reconcile-job.ts and unknown-operations.ts; shipped skills/openoutbound/SKILL.md with operator control entry.
- Adjacent first-party surfaces excluded from ownership: Tests and sandbox simulator as operational actors, docs-only aspirational roles, third-party model/provider systems, arbitrary user-authored agents and unrelated workspace/instance administration outside the chosen workspace recursion.
- First-party operating / deployment modes considered: Engine background operation with configured built-in model and campaigns; external-agent composition over explicitly shipped MCP/Agent Skill interface; separate workspace operator-governed control/strategy/policy mode; optional automatic agent change application only when configured with permitted scopes.
- Recursion level: One workspace comprising campaigns and interactions as operational work, with whole-workspace operating state, intervention and strategy identity owned or composed according to the mode. Multi-workspace agency-level management is excluded.
- Reviewed revision: bc158cac6548ab54699442d159cc2130570b9a78.
- Observation date: 2026-11-14.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

OpenOutbound is a self-hosted TypeScript outbound engine with durable jobs, campaign scheduling, message drafting, LLM reply classification, lead/relationship records, delivery reconciliation, compliance/suppression and workspace-specific approvals. MCP, REST and CLI doors expose one operation registry and a safety gate, including explicit agent-facing operating/strategy and review tools. Internal AI brain calls produce bounded semantic decisions such as reply category; deterministic action code executes the selected consequences within rules. A separately supplied Agent Skill instructs a compatible *external* agent to operate the engine, monitor whole-workspace state, propose strategy changes and return to work. Those external agent decisions must not be presented as an installed agent-owned S3/S4 system. Parent operators can directly control current workspace commitments, set strategy and approve or edit proposals. Strategy outcomes are reviewed after a configured delay using before/after campaign metrics.

Evidence: [architecture](https://github.com/xyluxx/openoutbound/blob/bc158cac6548ab54699442d159cc2130570b9a78/docs/architecture.md), [how it works](https://github.com/xyluxx/openoutbound/blob/bc158cac6548ab54699442d159cc2130570b9a78/docs/concepts/how-it-works.md), [Agent Skill](https://github.com/xyluxx/openoutbound/blob/bc158cac6548ab54699442d159cc2130570b9a78/skills/openoutbound/SKILL.md), [strategy lifecycle](https://github.com/xyluxx/openoutbound/blob/bc158cac6548ab54699442d159cc2130570b9a78/docs/concepts/strategy.md).

## Operational model

Each campaign manages outreach sequences for enrolled prospects. The embedded LLM brain classifies replies and can thereby trigger different downstream operational handling inside a registered first-party job; this bounded semantic decision/action loop is credited to S1. Multiple campaigns can interfere by contacting the same person/company; specialized enrollment checks attenuate that collision, while external agents may compose the discretionary inter-campaign response. An operating-state/attention view and strategy proposals expose specialized whole-workspace current and prospective control, but their decisive discretionary actor is external agent or parent operator depending on the mode. The business owner retains ultimate purpose and standing communication constraints.

## S1 — Operations

- State: A
- Function: Run AI-mediated outbound/contact-response work in an active workspace, with semantic decisions affecting subsequent operational behavior.
- Disturbance / variety regulated: Prospect replies vary by intent and content, including negative, unsubscribe, legal, interested, referral and automated responses, requiring different contact outcomes.
- Decisive decision or feedback right: The embedded model classifies an inbound response and returns structured semantic facts/category; the first-party action matrix executes the corresponding enrollment, suppression, follow-up or escalation changes.
- Decision owner: First-party configured LLM brain task for the meaning/category decision; engine implements fixed authorized consequences rather than pretending to own this semantic discretion.
- Supporting / enforcement mechanisms: Scheduled inbox classification job, brain routing and schema checks, stored reply facts, action matrix, campaign state, source records and safety gate.
- Closure path: A classified reply is persisted and applied to contact/campaign state; subsequent sequence steps are stopped, paused, continued or escalated according to semantic feedback and workspace rules.
- Boundary reachability: Standard engine ships and schedules inbox classification with a configured brain; this operation is inside its first-party runtime and requires no custom external MCP agent.
- Why this is / is not agent-owned: Removing the LLM classification choice leaves deterministic prechecks and delivery machinery but not the supported context-sensitive reply understanding that changes operating decisions.
- Evidence: [classify.ts#L163-L309](https://github.com/xyluxx/openoutbound/blob/bc158cac6548ab54699442d159cc2130570b9a78/src/modules/inbox/classify.ts#L163-L309), [actions.ts#L119-L286](https://github.com/xyluxx/openoutbound/blob/bc158cac6548ab54699442d159cc2130570b9a78/src/modules/inbox/actions.ts#L119-L286), [brain/service.ts](https://github.com/xyluxx/openoutbound/blob/bc158cac6548ab54699442d159cc2130570b9a78/src/brain/service.ts), [how it works](https://github.com/xyluxx/openoutbound/blob/bc158cac6548ab54699442d159cc2130570b9a78/docs/concepts/how-it-works.md).
- Basis: structural
- Confidence: medium
- Caveats: Narrow built-in autonomy is not equivalent to an autonomous general-purpose SDR agent or strategy decision maker. Source-only review did not execute model/provider calls; final inclusion still requires explicit assessment of whether the bounded agentic execution meets Index eligibility.

## S2 — Coordination

- State: C
- Function: Attenuate interference between multiple operational campaign units sharing contacts, channels and company relationships.
- Disturbance / variety regulated: Separate campaigns can enroll the same person or reach too many people at one company, producing duplicate/conflicting communication and subsequent relationship disruption.
- Decisive decision or feedback right: A first-party S2-specific feedback/construction path detects conflicts and exposes rejected/affected enrollments; an operator/developer must compose the autonomous agent that chooses which campaign to prioritize and how to reallocate future work.
- Decision owner: Deterministic engine enforces compliance and stops collisions; decisive inter-campaign discretionary coordination remains with a composed external agent, not a bundled autonomous S2 agent.
- Supporting / enforcement mechanisms: one_active_campaign_per_person, active-in-other-campaign checks, company contact cap, rest days, suppression records and stop/pause services.
- Closure path: Enrollment rejects conflicting targets and reports skip reasons; subsequent campaign planning can avoid conflicted prospects, and reply-triggered stop/pause changes active enrollments across relevant campaigns.
- Boundary reachability: Explicit first-party campaign enrollment, contact control and MCP/Agent Skill interfaces are shipped; developer composes agent coordination around these specialized collision results.
- Why this is / is not agent-owned: The engine reliably enforces fixed conflict rules, but it does not itself make an autonomous strategic choice between campaigns; the grade is constructor C, not A.
- Distinct S1 units: Concurrent campaigns with separate goals, enrollments, sequencer steps, sender schedules and prospect operations within the workspace.
- Inter-S1 disturbance: Duplicate or inconsistent contact work for the same person/company, with contact capacity and response conflict.
- Attenuating coordination relation: Cross-campaign enrollment restrictions and common relationship stop/pause actions, with a first-party interface exposing conflicts to the composing actor.
- Feedback into subsequent S1 behaviour: Conflicted enrollments are skipped, and replies can stop or pause unsent cross-campaign actions; external composed agent can select alternative campaign assignments.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The code checks concrete cross-campaign contention for a person/company and changes enrollment behavior, not merely routing a message to a worker.
- Evidence: [enrollment.ts#L50-L183](https://github.com/xyluxx/openoutbound/blob/bc158cac6548ab54699442d159cc2130570b9a78/src/modules/campaigns/enrollment.ts#L50-L183), [control.ts#L116-L181](https://github.com/xyluxx/openoutbound/blob/bc158cac6548ab54699442d159cc2130570b9a78/src/modules/campaigns/control.ts#L116-L181), [actions.ts#L237-L286](https://github.com/xyluxx/openoutbound/blob/bc158cac6548ab54699442d159cc2130570b9a78/src/modules/inbox/actions.ts#L237-L286).
- Basis: structural
- Confidence: medium
- Caveats: The S1-unit boundary treats campaigns as distinct operational units of the workspace, not self-standing VSM organizations. The agent that chooses discretionary campaign reconciliation must be composed.

## S3 — Inside-and-now control

- State: C(P)
- Function: Regulate present whole-workspace commitments, active campaign problems, sending capacity, approvals and intervention.
- Disturbance / variety regulated: Simultaneous campaigns, outreach quota pressure, high-severity problems, mailbox failures and pending replies can threaten whole-workspace coherence.
- Decisive decision or feedback right: Choose whether and how to pause/resume, revise current campaign commitments or redirect work based on whole-workspace operating state.
- Decision owner: Constructor mode delegates choice to developer-composed external MCP agent; separate parent mode is closed by legitimate workspace owner/operator with the required scopes.
- Supporting / enforcement mechanisms: get_operating_state, attention queue, campaign controls, runtime safety gate, budgets, owner approvals and status bookkeeping.
- Closure path: Agent/operator sees cross-campaign status and problems, selects authorized workspace/campaign operations, and those changes govern subsequent jobs/sends.
- Boundary reachability: First-party status, attention and campaign/workspace control operations plus shipped Agent Skill supply the S3-specific constructor; owner may act directly through shipped CLI/REST/MCP.
- Why this is / is not agent-owned: Attention prioritization is mostly deterministic and external agent runtime is not bundled; no internal autonomous S3 owner is inferred. Operator has an evidenced alternative parent decision and return path.
- Whole-system current view: Workspace-level operating state covers active campaigns, sending/capacity, replies, approvals, problems, budgets and sender condition.
- Current-control decision scope: Pause or revise active campaigns/workspace, adjust authorized current settings and resolve urgent operational problems on the whole workspace.
- Evidence: [Agent Skill#L18-L63](https://github.com/xyluxx/openoutbound/blob/bc158cac6548ab54699442d159cc2130570b9a78/skills/openoutbound/SKILL.md#L18-L63), [attention/build.ts#L13-L140](https://github.com/xyluxx/openoutbound/blob/bc158cac6548ab54699442d159cc2130570b9a78/src/modules/reports/attention/build.ts#L13-L140), [safety-and-approvals.md#L58-L130](https://github.com/xyluxx/openoutbound/blob/bc158cac6548ab54699442d159cc2130570b9a78/docs/concepts/safety-and-approvals.md#L58-L130).
- Basis: structural
- Confidence: medium
- Caveats: A single message approval or fixed budget enforcement does not establish S3; the claim depends on whole-workspace status and actual intervention operations in two different operating modes.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | Developer-composed external agent, not embedded engine | Read first-party whole-workspace operating/attention state | Chooses a workspace intervention via specialized MCP tools affecting later jobs/campaigns | [Agent Skill](https://github.com/xyluxx/openoutbound/blob/bc158cac6548ab54699442d159cc2130570b9a78/skills/openoutbound/SKILL.md), [attention queue](https://github.com/xyluxx/openoutbound/blob/bc158cac6548ab54699442d159cc2130570b9a78/src/modules/reports/attention/build.ts) |
| Parent (`P`) | Authorized human workspace operator | Operating problems, pending approvals or manual current-plan review | CLI/REST controls change active workspace/campaign and downstream execution | [safety-and-approvals](https://github.com/xyluxx/openoutbound/blob/bc158cac6548ab54699442d159cc2130570b9a78/docs/concepts/safety-and-approvals.md), [campaign control](https://github.com/xyluxx/openoutbound/blob/bc158cac6548ab54699442d159cc2130570b9a78/src/modules/campaigns/control.ts) |

## S3* — Complementary audit

- State: C
- Function: Complement ordinary sending records with alternative direct verification of whether an uncertain outbound message actually left the mailbox.
- Disturbance / variety regulated: A timeout or interrupted job cannot tell from its own execution record whether a message reached the provider, risking duplicate sends or false assertions of delivery.
- Decisive decision or feedback right: First-party specialized reconciliation inspects the Sent folder by Message-ID; the remaining ambiguous outcome is exposed as a specific resolve_unknown corrective decision for an operator or developer-composed audit agent.
- Decision owner: Deterministic reconciliation owns fixed evidence checks and safe retries; an autonomous independent auditor is not shipped to own ambiguous discretionary judgment. A composed external actor can use first-party corrective endpoint.
- Supporting / enforcement mechanisms: IMAP Sent-folder evidence, message id, unknown/reconcile states, resend guards, capped retries, send_unknown problems and specialized resolve_unknown operation.
- Closure path: Confirmed Sent evidence changes status to sent; qualified absence allows one conditional resend; unresolved ambiguity creates a problem and first-party resolution that changes subsequent campaign steps.
- Boundary reachability: Shipped email.reconcile_sends job runs in the engine; messages.resolve_unknown is a first-party operation exposed through the same registry to a composed agent.
- Why this is / is not agent-owned: The alternative evidence path is first-party, but the engine's default reconciliation is deterministic and any independent agent decision must be composed; therefore C rather than A.
- Claim being audited: Whether an attempted outbound message was actually sent despite an indeterminate original execution response.
- Ordinary reporting path: Sending job status, provider response and original message ledger.
- Complementary access path: Search of the real mailbox Sent folder for the message identity, plus bounded reconciliation observations.
- Independence boundary: Mailbox Sent folder is an alternative external operational artifact distinct from original job success/failure reporting; no audit of all customer outreach correctness is claimed.
- Who acts on findings: Engine reconciliation closes confirmed outcomes or raises an unknown problem; the operator/composed agent can perform the specialized resolution for continued execution.
- Evidence: [reconcile-job.ts#L1-L14](https://github.com/xyluxx/openoutbound/blob/bc158cac6548ab54699442d159cc2130570b9a78/src/modules/email/reconcile-job.ts#L1-L14), [reconcile-job.ts#L267-L425](https://github.com/xyluxx/openoutbound/blob/bc158cac6548ab54699442d159cc2130570b9a78/src/modules/email/reconcile-job.ts#L267-L425), [unknown-operations.ts#L67-L175](https://github.com/xyluxx/openoutbound/blob/bc158cac6548ab54699442d159cc2130570b9a78/src/modules/email/unknown-operations.ts#L67-L175).
- Basis: structural
- Confidence: medium-low
- Caveats: This is delivery-evidence reconciliation, not an independent model judgment over campaign quality. A later reviewer may reasonably place routine reconciliation inside S1 recovery rather than complementary organizational audit; that is a source-relative semantic dispute, not proof of autonomous A.

## S4 — Outside-and-then intelligence

- State: C(P)
- Function: Translate changing prospect/market response and campaign outcomes into prospective adjustments of outreach capability.
- Disturbance / variety regulated: Changing prospect preferences, weak conversion, emerging market signals and changing channel performance undermine future effectiveness of current offers, ICPs and campaigns.
- Decisive decision or feedback right: Evaluate and choose proposed changes to ICP, offer, campaign, settings or automation, with an evidence reason and expected outcome.
- Decision owner: In base constructor mode, a developer-composed agent chooses option and requests application through manage_strategy; in separate parent mode the workspace owner approves/edits/rejects and can later undo the decision.
- Supporting / enforcement mechanisms: Signal monitors, conversion reports, strategy page, proposed operation allowlist, approval router, change log, after-days review and before/after outcome metrics.
- Closure path: Proposed option is approved or applied in its authorized mode, changing live workspace operating capability; later review stores better/worse/unclear outcomes that inform subsequent strategy decisions.
- Boundary reachability: Shipped Agent Skill and manage_strategy proposal operation expose a function-specific construction path; the owner also has built-in proposal approval and strategy operations in the normal self-hosted workspace.
- Why this is / is not agent-owned: An external agent can propose and act only when composed with credentials and scope. Fixed post-change verdict evaluation is not itself an autonomous S4 strategic decision; parent owner mode is distinct.
- External distinction: Prospect responses, demand signals and observed campaign conversion changes.
- Future / prospective distinction: Expected improvements in future customer acquisition and conversion rather than only processing one current reply.
- Adaptation option generated: ICP/offer/campaign/automation or workspace-setting change with reason, evidence, expected outcome and review period.
- Path back into current capability / S3: Approved/applied proposal changes future campaign execution and is recorded on the workspace strategy page; subsequent evaluation returns into the next operating review.
- Evidence: [strategy.md#L92-L176](https://github.com/xyluxx/openoutbound/blob/bc158cac6548ab54699442d159cc2130570b9a78/docs/concepts/strategy.md#L92-L176), [proposals.ts#L315-L460](https://github.com/xyluxx/openoutbound/blob/bc158cac6548ab54699442d159cc2130570b9a78/src/modules/strategy/proposals.ts#L315-L460), [review.ts#L319-L437](https://github.com/xyluxx/openoutbound/blob/bc158cac6548ab54699442d159cc2130570b9a78/src/modules/strategy/review.ts#L319-L437).
- Basis: structural
- Confidence: medium
- Caveats: Agent_changes:auto is an explicitly configured mode, not universal default. There is no claim of an autonomous in-engine S4 actor; operational feedback and parent governance are distinct from the model's routine email writing.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | Developer-composed external agent | Evaluate signals/strategy outcomes, propose adaptation through first-party operation | Authorized propose/apply path changes campaign capabilities; later outcome is reviewed | [Agent Skill](https://github.com/xyluxx/openoutbound/blob/bc158cac6548ab54699442d159cc2130570b9a78/skills/openoutbound/SKILL.md), [proposals](https://github.com/xyluxx/openoutbound/blob/bc158cac6548ab54699442d159cc2130570b9a78/src/modules/strategy/proposals.ts) |
| Parent (`P`) | Legitimate workspace owner/operator | Evidence-backed proposal and current performance review | Owner approves/edits/rejects, application changes future operations and reviewed outcomes return | [strategy lifecycle](https://github.com/xyluxx/openoutbound/blob/bc158cac6548ab54699442d159cc2130570b9a78/docs/concepts/strategy.md), [review](https://github.com/xyluxx/openoutbound/blob/bc158cac6548ab54699442d159cc2130570b9a78/src/modules/strategy/review.ts) |

## S5 — Policy and identity

- State: P
- Function: Preserve the client's legitimate ultimate outreach purpose, identity and standing policy constraints amid changing operating and strategic options.
- Disturbance / variety regulated: Agent-generated tactics may conflict with business goals, acceptable claims, compliance, brand/voice identity or the owner's constitutive outreach mandate.
- Decisive decision or feedback right: The authorized workspace owner sets/revises goals, qualified-meeting identity, nonnegotiable communication notes and workspace policy, and approves identity-level strategy change when necessary.
- Decision owner: Parent human/organization that owns the workspace; no autonomous ultimate authority is installed in the engine.
- Supporting / enforcement mechanisms: Strategy page, owner settings, agent_notes, offer/voice/never-say rules, precedence hierarchy, change proposals, approvals, safety gate and persistent change log.
- Closure path: Owner-authoritative settings/strategy change returns through the strategy page and safety gate into future agent sessions, campaign plans and message execution.
- Boundary reachability: Shipped workspace settings and strategy operations let the authorized owner set standing mission and identity, and the Agent Skill requires this state be read first by later sessions.
- Why this is / is not agent-owned: The engine enforces current owner-set policy; it neither chooses the ultimate business identity nor has a supported internal mode for legitimate self-revision.
- Identity / ultimate-policy issue: Whether the workspace may change its defined business outreach goals and standing acceptable-customer-communication constraints.
- Ultimate authority in each claimed mode: Parent workspace owner/institution, not an agent and not the service's repository maintainers.
- Return-to-operation path: Owner-authoritative strategy/workspace settings → persistent workspace strategy page → later agent's first read and execution-gated campaign behavior.
- Evidence: [strategy.md#L7-L42](https://github.com/xyluxx/openoutbound/blob/bc158cac6548ab54699442d159cc2130570b9a78/docs/concepts/strategy.md#L7-L42), [strategy.md#L92-L130](https://github.com/xyluxx/openoutbound/blob/bc158cac6548ab54699442d159cc2130570b9a78/docs/concepts/strategy.md#L92-L130), [Agent Skill#L18-L22](https://github.com/xyluxx/openoutbound/blob/bc158cac6548ab54699442d159cc2130570b9a78/skills/openoutbound/SKILL.md#L18-L22), [safety-and-approvals.md](https://github.com/xyluxx/openoutbound/blob/bc158cac6548ab54699442d159cc2130570b9a78/docs/concepts/safety-and-approvals.md).
- Basis: structural
- Confidence: medium
- Caveats: This is the client workspace business identity and enduring communication policy, not governance of the upstream OpenOutbound project. Ordinary send approvals or a single launch authorization are not credited as S5.

## Distributed OSS parent arrangement

Upstream maintainers, contributors and repository CI are outside the chosen self-hosted workspace boundary. The parent is the actual workspace owner who governs that client environment, not a hypothetical distributed upstream contributor council.

## Self-hosted and non-human modes

The shipped engine operates with configured LLM brains and can be driven by either local humans or developer-composed external agents. The latter supports specialized C constructors for whole-workspace control and prospective change without promoting an external host to in-engine autonomy. Human operating modes are evidenced by first-party direct controls and closures, yielding C(P) for S3/S4 and P for S5. No general autonomous S5 is claimed.

## Recursion

The assessed unit is one workspace with several campaign operations, a cross-campaign relationship layer, workspace current controls, strategy and legitimate business owner. Multiple workspaces in an agency deployment form another recursion and are excluded here.

## Variety and escalation

Contact/response disturbances enter the inbox classifier and lead state, inter-campaign collisions are prevented, high-severity campaign problems enter the attention queue, unknown sends reach independent Sent-folder evidence or human resolution, prospective changes enter proposal review. A problem status alone does not establish metasystem control; decisional and feedback rights determine each function.

## Evidence gaps

- Eligibility is borderline: the first-party engine contains model-owned reply classification/action feedback but an autonomous general SDR strategy agent is ordinarily external. Canonical inclusion should explicitly accept this narrower S1 boundary rather than silently borrow the MCP client.
- S2=C relies on campaigns as distinct operational units and a S2-specific conflict/response constructor. The deterministic no-double-enroll gate alone is not an autonomous coordinator.
- S3*=C has a narrowly scoped delivery-uncertainty audit path. Its placement against ordinary S1 delivery recovery merits semantic review; never claim broad model-owned audit.
- Parent S5 rests on the owner setting enduring commercial mission and communication identity, not on an ordinary per-message approval.
- No live send, external provider call or real-world deliverability assessment was performed. License at the pinned repository is Apache-2.0.

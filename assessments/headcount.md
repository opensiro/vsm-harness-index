---
harness_id: headcount
project_name: Headcount
repository: https://github.com/cbrock84/headcount
review_ref: 9cbf34005e3e8a980a6af9b55eb226bd926a62b3
reviewed_at: 2026-09-18
generated_profile_version: 0.2.2
generated_assessment_procedure_version: 0.3.4
profile_version: 0.2.2
assessment_procedure_version: 0.3.4
assessment_changed_at: 2026-09-18
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: A
autonomy_s5: A
---

# Headcount

## Review boundary

- System in focus: Headcount's first-party agent organization as instantiated in its supported Claude Code / ChatGPT skill-and-agent mode at pinned revision `9cbf34005e3e8a980a6af9b55eb226bd926a62b3`, including department agent charters, executive/strategy/reviewer skills and the documented orchestrator/subagent organization pattern.
- Purpose and identity: provide a company-shaped autonomous agent organization whose functional specialists produce work, coordinate bounded parallel work, regulate cross-functional tradeoffs, independently audit risky work, model future/external strategy and maintain organizational direction.
- Relevant environment: the user's business/project context, target repository/work artifacts, customers/markets/competitors, legal/security constraints, human owner and supported model host.
- Standard-distribution boundary: Headcount's shipped skills, department agent charters, organization/use-case contracts and agent-hierarchy/parallel-delivery methods. Claude Code/ChatGPT supply the model execution host but are not credited with unrelated organizational functions.
- First-party modes considered: direct skill invocation, delegated department subagents, cross-department situation workflows, producer/auditor hierarchy and executive/strategy decision paths.
- Recursion level: one Headcount organization. Departments are functionally distinct units but are not automatically credited as complete viable recursions.
- Reviewed revision: `9cbf34005e3e8a980a6af9b55eb226bd926a62b3`.
- Observation date: 2026-09-18.
- Generated/current Profile / Methodology: `0.2.2` / `0.3.4`.

## Repository architecture

Headcount packages a company-shaped organization as independently installable department plugins and agent charters. Department agents can be delegated bounded work with exclusive write surfaces. Cross-functional use cases deliberately compose several departments in sequence and preserve reviewer-class stop authority. The executive layer separates present cross-functional allocation/arbitration from long-horizon strategy; the strategy role develops external/future options and hands them into executive/finance allocation. A dedicated agent-hierarchy method pairs producers with independent read-only auditors and machine-checks exclusive ownership boundaries.

## Primary evidence

- [`README.md`](https://github.com/cbrock84/headcount/blob/9cbf34005e3e8a980a6af9b55eb226bd926a62b3/README.md) — agent-organization boundary, independently installable departments and delegated department subagents.
- [`docs/USE-CASES.md`](https://github.com/cbrock84/headcount/blob/9cbf34005e3e8a980a6af9b55eb226bd926a62b3/docs/USE-CASES.md) — multi-function situations, reviewer-class stop authority and organizational return behavior.
- [`plugins/executive/skills/chief-executive/SKILL.md`](https://github.com/cbrock84/headcount/blob/9cbf34005e3e8a980a6af9b55eb226bd926a62b3/plugins/executive/skills/chief-executive/SKILL.md) — cross-functional allocation/arbitration, direction, strategy-of-record and final internal decision authority.
- [`plugins/corporate-strategy/skills/chief-strategy-officer/SKILL.md`](https://github.com/cbrock84/headcount/blob/9cbf34005e3e8a980a6af9b55eb226bd926a62b3/plugins/corporate-strategy/skills/chief-strategy-officer/SKILL.md) — markets/competitors, multi-year horizon, scenarios/early-warning indicators and return into CEO/CFO resource decisions.
- [`plugins/technology/skills/parallel-agent-delivery/SKILL.md`](https://github.com/cbrock84/headcount/blob/9cbf34005e3e8a980a6af9b55eb226bd926a62b3/plugins/technology/skills/parallel-agent-delivery/SKILL.md) — concrete overlapping-write disturbance and parallel/sequential coordination rule.
- [`plugins/executive/skills/agent-hierarchy/SKILL.md`](https://github.com/cbrock84/headcount/blob/9cbf34005e3e8a980a6af9b55eb226bd926a62b3/plugins/executive/skills/agent-hierarchy/SKILL.md) — exclusive write-surface organization, autonomous/proposes/escalates authority, independent read-only auditors and CI guard.
- [`plugins/security/skills/security-architecture-review/SKILL.md`](https://github.com/cbrock84/headcount/blob/9cbf34005e3e8a980a6af9b55eb226bd926a62b3/plugins/security/skills/security-architecture-review/SKILL.md) — raw-artifact security review, blocking findings and corrective return contract.

## S1 — Operations

- State: A
- Function: department specialist agents perform the organization's primary transformations by producing analyses, plans, reviews, implementations and other domain outcomes.
- Disturbance / variety regulated: domain-specific uncertainty across finance, product, technology, security, legal, operations, revenue, people and other local environments.
- Decisive decision or feedback right: choose the domain reasoning/action needed to produce the requested bounded outcome within the department charter.
- Decision owner: the model-driven department specialist/subagent executing the first-party Headcount skill/charter.
- Supporting / enforcement mechanisms: department plugins, skill auto-loading, `.claude/agents/` charters, exclusive write surfaces and host model/tool execution.
- Closure path: the specialist produces the domain artifact/decision/review under its return contract and returns it into the invoking organization/orchestrator or directly into the target work surface.
- Why this is / is not agent-owned: the decisive domain judgment is made by the autonomous specialist actor; Headcount's Markdown/charter machinery defines remit and constraints but does not substitute a deterministic answer.
- Evidence: `README.md` documents department agents and delegation; `docs/USE-CASES.md` shows departments engaging to produce concrete business/project outcomes.
- Basis: explicit + structural
- Confidence: high
- Caveats: the execution host is external software; the credited S1 ownership is the autonomous department actor instantiated through Headcount's first-party standard-distribution contract.

## S2 — Coordination

- State: A
- Function: regulate interference among multiple operational agents when work can be parallelized safely and serialize it when dependencies or shared write surfaces would make parallel work destructive.
- Disturbance / variety regulated: two agents editing the same file, sequential dependencies, incompatible parallel work and merge/lost-update conflicts between otherwise autonomous producers.
- Decisive decision or feedback right: decide whether the current work can be split, define exclusive agent surfaces/briefs and choose parallel versus sequential execution/integration.
- Decision owner: the autonomous main/orchestrator agent applying Headcount's parallel-delivery / hierarchy method.
- Supporting / enforcement mechanisms: exclusive write-surface map, agent charters, structured returns, read-only reviewer class and `agent-guard` CI checks.
- Closure path: the orchestrator partitions only disjoint independent work for parallel dispatch; unsafe work remains sequential; returned results are reviewed/reconciled before merge and later work observes the integrated state.
- Why this is / is not agent-owned: the CI guard mechanically verifies the selected partition, but the agent decides the decomposition and whether parallelism is valid from the actual work dependencies and surfaces.
- Evidence: `parallel-agent-delivery` explicitly identifies same-file concurrent writes as merge-conflict/lost-update failures and instructs the agent to run sequentially unless disjointness/dependency/verification conditions hold; `agent-hierarchy` makes exclusive surfaces a first-party organizational contract.
- Basis: explicit + structural
- Confidence: high
- Caveats: generic cross-department sequencing is not the positive witness; the mapping rests on the explicit inter-agent write/dependency interference path.
- Distinct S1 units: two or more department/builder agents operating on separately assigned work surfaces or domain outcomes.
- Inter-S1 disturbance: overlapping writes can create merge conflicts or silent lost updates, while sequential dependencies can make premature parallel execution invalid.
- Attenuating coordination relation: the orchestrator proves disjoint write surfaces and dependency independence before dispatch, otherwise keeps work sequential; the hierarchy map/guard prevents conflicting ownership.
- Feedback into subsequent S1 behaviour: the chosen partition determines which agents run, their allowed surfaces and when dependent work may begin; failed disjointness/guard checks prevent the conflicting execution/merge.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: Headcount names a concrete destructive interaction between S1s and provides an agent-owned coordination decision plus enforceable surface boundaries specifically to attenuate it.

## S3 — Inside-and-now control

- State: A
- Function: regulate current organization-wide priorities, capital/attention allocation, cross-functional commitments and conflicts on behalf of the whole.
- Disturbance / variety regulated: specialist-local optimization, mutually incompatible department recommendations, excessive simultaneous priorities and current resource/attention conflicts that cannot be settled within one function.
- Decisive decision or feedback right: choose which cross-functional consideration wins, what is not pursued, where capital/attention goes and which current priority becomes binding.
- Decision owner: the autonomous Chief Executive agent role.
- Supporting / enforcement mechanisms: cross-department return contracts, priority stack, strategy/decision artifacts, escalation conventions and orchestrator delegation.
- Closure path: functional specialists return their positions; the Chief Executive makes the cross-functional choice and issues explicit handoffs/priority/allocation decisions that govern subsequent department work.
- Why this is / is not agent-owned: the Chief Executive skill explicitly states that one agent, rather than the orchestrator or specialist, owns the call when specialists disagree; deterministic routing is not being credited as S3.
- Evidence: `chief-executive/SKILL.md` assigns capital/attention allocation, cross-functional arbitration and final say on tradeoffs to the agent and requires concrete handoffs in the return contract; `docs/USE-CASES.md` routes multi-function situations to executive closure where needed.
- Basis: explicit + structural
- Confidence: high
- Caveats: owner-reserved matters can still be deferred to the human; no separate parent S3 mode is published because the pinned evidence does not reconstruct a distinct standard current-control parent loop with the specificity required for `A(P)`.
- Whole-system current view: the Chief Executive receives cross-functional analyses, constraints, costs, risks and competing current priorities from the relevant departments.
- Current-control decision scope: current priority stack, capital/attention allocation, cross-functional tradeoffs, present-quarter conflicts and handoffs across functions.

## S3* — Complementary audit

- State: A
- Function: independently challenge producer/department claims through reviewer-class agents that inspect the underlying artifact and can block progression.
- Disturbance / variety regulated: optimistic producer self-report, unsafe design/implementation, legal/security facts hidden by ordinary functional summaries and self-review bias.
- Decisive decision or feedback right: independently judge the producer's artifact/finding and issue a blocking or pass/corrective review outcome.
- Decision owner: autonomous reviewer-class agent, such as security/legal reviewer or the independent read-only auditor defined by the agent-hierarchy method.
- Supporting / enforcement mechanisms: permanent read-only reviewer class, producer/auditor separation, exclusive surfaces, CI guard and reviewer return contracts.
- Closure path: the reviewer inspects the actual artifact/evidence, returns findings and blocking status, and the organization must correct/escalate before the affected work proceeds; the reviewed department cannot silently overrule its reviewer-class constraint.
- Why this is / is not agent-owned: the reviewer agent owns the audit judgment; read-only/CI separation enforces independence but does not manufacture the finding.
- Evidence: `agent-hierarchy/SKILL.md` requires that producer and auditor are never the same agent and makes reviewers permanently read-only; `docs/USE-CASES.md` states reviewer-class security/legal findings are not overrulable by the department under review; `security-architecture-review` instructs the reviewer to read what is actually being built and return blocking findings/fixes.
- Basis: explicit + structural
- Confidence: high
- Caveats: ordinary tests are not counted; the positive mapping is the structurally separated reviewer path with complementary artifact access and corrective authority.
- Claim being audited: that a producer's design/change/functional recommendation is safe, legally/technically acceptable or ready to proceed.
- Ordinary reporting path: the producing department/builder returns its own artifact and summary through its normal engagement/return contract.
- Complementary access path: a separate reviewer reads the actual design/change/artifact and applicable evidence/standards rather than relying on the producer's self-assessment.
- Independence boundary: reviewer-class agents are read-only/separate from builders, and Headcount explicitly prohibits producer=self-auditor; reviewer-class departments report outside the function being reviewed.
- Who acts on findings: the orchestrator/Chief Executive and responsible producer consume the blocking finding, correction and escalation path before further commitment.

## S4 — Outside-and-then intelligence

- State: A
- Function: model external/future conditions, develop strategic adaptation options and return them into present resource/capability decisions.
- Disturbance / variety regulated: changing markets, competitors, partnerships, acquisition opportunities, uncertain multi-year conditions and early signs that strategic assumptions may be becoming false.
- Decisive decision or feedback right: choose the strategic interpretation/options/recommendation and the indicators that should trigger revision of the plan.
- Decision owner: the autonomous Chief Strategy Officer agent role.
- Supporting / enforcement mechanisms: scenario framing, competitive analysis, assumptions/early-warning indicators, portfolio analysis, strategy artifacts and CEO/CFO handoff.
- Closure path: the CSO develops options/recommendation from external/future evidence and hands the conclusion to the Chief Executive/Finance; the strategy is not considered finished until resourcing artifacts such as hiring/roadmap/incentives move, closing the S4→S3 conversation.
- Why this is / is not agent-owned: the model-driven CSO owns the prospective strategic judgment; the CEO retains present allocation/final strategy-of-record authority, which is the required S4/S3 relationship rather than evidence against S4 autonomy.
- Evidence: `chief-strategy-officer/SKILL.md` assigns markets, partnerships, acquisitions, multi-year planning, scenarios and early-warning indicators to the role; it explicitly instructs the CSO to hand conclusions to CEO/CFO and tests whether resourcing artifacts actually changed.
- Basis: explicit + structural
- Confidence: high
- Caveats: generic planning/backlog work is not credited; the positive witness is the explicit external and multi-year strategic role with a return into present allocation.
- External distinction: market/segment choice, competitor investment/pricing behavior, strategic partnerships, acquisitions/divestitures and other changes outside current internal execution.
- Future / prospective distinction: multi-year horizon, scenarios, early-warning indicators and falsifiable assumptions about what could change the strategy.
- Adaptation option generated: where to play, build/buy/partner/exit choices, portfolio funding recommendations and strategic tradeoffs.
- Path back into current capability / S3: recommendation goes to Chief Executive/Finance and is only operationally finished when headcount/roadmap/incentive/resource artifacts move.

## S5 — Policy and identity

- State: A
- Function: maintain organizational direction, identity and ultimate internal policy closure when cross-functional present/future tensions require a legitimate final organizational decision.
- Disturbance / variety regulated: ambiguity about what the organization is for, what it will not do, which strategy is authoritative and which cross-functional tradeoff should define the organization rather than one department.
- Decisive decision or feedback right: set organizational direction, decide what will not be pursued, own the strategy of record and close final internal cross-functional policy choices.
- Decision owner: the autonomous Chief Executive agent role.
- Supporting / enforcement mechanisms: strategy of record, priority stack, explicit executive authority/remit, department escalation paths and six-part return/handoff contract.
- Closure path: unresolved cross-functional or strategic matters reach the Chief Executive; the agent makes the direction/policy decision and returns explicit priority/handoff consequences that govern later department work.
- Why this is / is not agent-owned: `chief-executive/SKILL.md` explicitly gives the role ownership of direction and final internal cross-functional calls rather than merely displaying a static policy prompt; human-owner-reserved decisions remain a caveat and are not silently promoted to a parent mode without a separately evidenced closure protocol.
- Evidence: the Chief Executive remit includes “what the organization is for, and what it will not do,” owns the strategy of record/priority stack/final tradeoffs and is the escalation endpoint for organizational decisions; the CSO explicitly leaves final strategy approval/ownership with this role.
- Basis: explicit + structural
- Confidence: medium-high
- Caveats: the skill states that genuinely owner-reserved decisions should be identified rather than decided for the human. The reviewed standard distribution does not specify a sufficiently explicit separate parent S5 trigger/return protocol to publish `A(P)`, so only the agent-owned internal S5 closure is encoded.
- Identity / ultimate-policy issue: organizational purpose/direction, authoritative strategy and final policy-level cross-functional choice.
- Ultimate authority in each claimed mode: Chief Executive agent for the claimed autonomous internal mode.
- Return-to-operation path: the Chief Executive's strategy/priority/tradeoff decision produces explicit handoffs and changes the direction/allocation under which departments subsequently operate.

## Recursion

Departments have durable remits, agent charters and local environments, but this assessment does not infer a complete recursive viable system for every department. The six-function mapping is for the assembled Headcount organization at the chosen recursion.

## Variety and escalation

Department specialization distributes local variety. Exclusive write-surface coordination prevents destructive parallelism; reviewer-class functions add independent challenge; the Chief Executive absorbs only cross-functional/current and identity-level variety that specialists cannot settle; the CSO carries external/future variety into that executive conversation.

## Evidence gaps

The largest uncertainty is deployment closure: Headcount is predominantly a skill/agent-organization package whose execution depends on a supported host, not a standalone daemon. The states therefore describe the first-party supported organizational mode when those shipped charters/skills are instantiated by the host; no unrelated host functions are inherited.

## Admission conclusion

Canonical vector: `A A A A A A`.

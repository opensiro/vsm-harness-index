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
assessment_changed_at: 2026-09-19
last_checked_ref: 9cbf34005e3e8a980a6af9b55eb226bd926a62b3
last_checked_at: 2026-09-19
last_reassessment_round: R3
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: C
autonomy_s4: A
autonomy_s5: A
---

# Headcount

## Review boundary

- System in focus: Headcount's first-party user-facing agent organization at pinned revision `9cbf34005e3e8a980a6af9b55eb226bd926a62b3`, as exposed through independently installable department plugins, shipped skills and documented host-instantiated operating patterns. Repository-development agents used to maintain Headcount itself are not automatically part of this system boundary.
- Purpose and identity: provide a company-shaped autonomous agent organization whose functional specialists produce work, coordinate bounded parallel work, regulate cross-functional tradeoffs, expose complementary review, model future/external strategy and maintain organizational direction.
- Relevant environment: the user's business/project context, target repository/work artifacts, customers/markets/competitors, legal/security constraints, human owner and supported model host.
- Standard-distribution boundary: Headcount's independently installable department plugins, shipped skills/manifests, documented user workflows and first-party organizational methods such as `parallel-agent-delivery` and `agent-hierarchy`. Root repository-development surfaces such as `.claude/agents/*` and `docs/AGENT-SURFACES.md` are treated as evidence of how Headcount's maintainers instantiate the method, but they are not credited as installed user-facing actors unless the assessed operating mode separately packages or wires them.
- First-party modes considered: direct skill invocation, host-instantiated department specialists, skill-driven delegated work, cross-department situation workflows, constructor-based producer/auditor composition, and executive/strategy decision paths.
- Recursion level: one Headcount organization. Departments are functionally distinct units but are not automatically credited as complete viable recursions.
- Reviewed revision: `9cbf34005e3e8a980a6af9b55eb226bd926a62b3`.
- Observation date: 2026-09-18.
- Generated/current Profile / Methodology: `0.2.2` / `0.3.4`.

## Repository architecture

Headcount packages a company-shaped organization as independently installable department plugins containing specialist skills. The documented user path lets the host instantiate relevant specialists and can apply shipped organizational methods for bounded delegation and parallel work. Cross-functional use cases deliberately compose several departments in sequence and preserve reviewer-class stop semantics. The executive layer separates present cross-functional allocation/arbitration from long-horizon strategy; the strategy role develops external/future options and hands them into executive/finance allocation.

Headcount also dogfoods a richer repository-development organization under root `.claude/agents/*` and `docs/AGENT-SURFACES.md`, including permanently read-only reviewer agents. That development organization is strong evidence that the supplied organizational method is concrete, but it is a distinct operating boundary from an independently installed department plugin and therefore cannot by itself establish autonomous ownership in the assessed user-facing distribution.

## Primary evidence

- [`README.md`](https://github.com/cbrock84/headcount/blob/9cbf34005e3e8a980a6af9b55eb226bd926a62b3/README.md) — agent-organization boundary, independently installable departments and documented delegation.
- [`docs/GETTING-STARTED.md`](https://github.com/cbrock84/headcount/blob/9cbf34005e3e8a980a6af9b55eb226bd926a62b3/docs/GETTING-STARTED.md) — installed-plugin user boundary, direct skill use, delegated department pattern and reviewer-class behavior.
- [`docs/USE-CASES.md`](https://github.com/cbrock84/headcount/blob/9cbf34005e3e8a980a6af9b55eb226bd926a62b3/docs/USE-CASES.md) — multi-function situations, reviewer-class stop authority and organizational return behavior.
- [`plugins/executive/skills/chief-executive/SKILL.md`](https://github.com/cbrock84/headcount/blob/9cbf34005e3e8a980a6af9b55eb226bd926a62b3/plugins/executive/skills/chief-executive/SKILL.md) — cross-functional allocation/arbitration, direction, strategy-of-record and final internal decision authority.
- [`plugins/corporate-strategy/skills/chief-strategy-officer/SKILL.md`](https://github.com/cbrock84/headcount/blob/9cbf34005e3e8a980a6af9b55eb226bd926a62b3/plugins/corporate-strategy/skills/chief-strategy-officer/SKILL.md) — markets/competitors, multi-year horizon, scenarios/early-warning indicators and return into CEO/CFO resource decisions.
- [`plugins/technology/skills/parallel-agent-delivery/SKILL.md`](https://github.com/cbrock84/headcount/blob/9cbf34005e3e8a980a6af9b55eb226bd926a62b3/plugins/technology/skills/parallel-agent-delivery/SKILL.md) — concrete overlapping-write disturbance and parallel/sequential coordination rule.
- [`plugins/executive/skills/agent-hierarchy/SKILL.md`](https://github.com/cbrock84/headcount/blob/9cbf34005e3e8a980a6af9b55eb226bd926a62b3/plugins/executive/skills/agent-hierarchy/SKILL.md) — explicit producer/auditor separation, read-only reviewers, authority states and guard construction method.
- [`plugins/security/skills/security-architecture-review/SKILL.md`](https://github.com/cbrock84/headcount/blob/9cbf34005e3e8a980a6af9b55eb226bd926a62b3/plugins/security/skills/security-architecture-review/SKILL.md) — raw-artifact security review, blocking findings and corrective return contract.
- [`plugins/security/.claude-plugin/plugin.json`](https://github.com/cbrock84/headcount/blob/9cbf34005e3e8a980a6af9b55eb226bd926a62b3/plugins/security/.claude-plugin/plugin.json) — independently installed security plugin boundary.
- [`docs/AGENT-SURFACES.md`](https://github.com/cbrock84/headcount/blob/9cbf34005e3e8a980a6af9b55eb226bd926a62b3/docs/AGENT-SURFACES.md) and [`.claude/agents/security-review.md`](https://github.com/cbrock84/headcount/blob/9cbf34005e3e8a980a6af9b55eb226bd926a62b3/.claude/agents/security-review.md) — concrete repository-development instantiation of the reviewer method; used as boundary evidence, not as an installed user-facing reviewer actor.

## S1 — Operations

- State: A
- Function: department specialist agents perform the organization's primary transformations by producing analyses, plans, reviews, implementations and other domain outcomes.
- Disturbance / variety regulated: domain-specific uncertainty across finance, product, technology, security, legal, operations, revenue, people and other local environments.
- Decisive decision or feedback right: choose the domain reasoning/action needed to produce the requested bounded outcome within the department skill/remit.
- Decision owner: the model-driven department specialist instantiated through the first-party Headcount plugin/skill path.
- Supporting / enforcement mechanisms: independently installable department plugins, skill auto-loading/invocation and host model/tool execution.
- Closure path: the specialist produces the domain artifact/decision/review under its return contract and returns it into the invoking organization/orchestrator or directly into the target work surface.
- Why this is / is not agent-owned: the decisive domain judgment is made by the autonomous specialist actor; Headcount's skill machinery defines remit and constraints but does not substitute a deterministic answer.
- Evidence: `README.md` and `docs/GETTING-STARTED.md` document installed department specialists and direct skill engagement; `docs/USE-CASES.md` shows departments producing concrete business/project outcomes.
- Basis: explicit + structural
- Confidence: high
- Caveats: the execution host is external software; the credited S1 ownership is the autonomous specialist actor instantiated through Headcount's first-party standard-distribution contract, not the root repository-development agent roster.

## S2 — Coordination

- State: A
- Function: regulate interference among multiple operational agents when work can be parallelized safely and serialize it when dependencies or shared write surfaces would make parallel work destructive.
- Disturbance / variety regulated: two agents editing the same file, sequential dependencies, incompatible parallel work and merge/lost-update conflicts between otherwise autonomous producers.
- Decisive decision or feedback right: decide whether the current work can be split, define exclusive agent surfaces/briefs and choose parallel versus sequential execution/integration.
- Decision owner: the autonomous main/orchestrator agent applying Headcount's shipped `parallel-agent-delivery` method.
- Supporting / enforcement mechanisms: the first-party disjoint-surface/dependency rules, structured returns and optional `agent-hierarchy` guard pattern when the user composes a persistent roster.
- Closure path: the orchestrator partitions only disjoint independent work for parallel dispatch; unsafe work remains sequential; returned results are reviewed/reconciled before integration and later work observes the integrated state.
- Why this is / is not agent-owned: the agent decides decomposition and whether parallelism is valid from actual work dependencies/surfaces; deterministic guard machinery, when adopted, only verifies the selected partition.
- Evidence: `parallel-agent-delivery` explicitly identifies same-file concurrent writes as merge-conflict/lost-update failures and instructs the agent to run sequentially unless disjointness/dependency/verification conditions hold; `agent-hierarchy` supplies a persistent form of the same surface discipline.
- Basis: explicit + structural
- Confidence: high
- Caveats: generic cross-department sequencing and the maintainer's root surface map are not the positive witness; the mapping rests on the shipped agent-owned inter-agent write/dependency coordination method.
- Distinct S1 units: two or more department/builder agents operating on separately assigned work surfaces or domain outcomes.
- Inter-S1 disturbance: overlapping writes can create merge conflicts or silent lost updates, while sequential dependencies can make premature parallel execution invalid.
- Attenuating coordination relation: the orchestrator establishes disjoint write surfaces and dependency independence before dispatch, otherwise keeps work sequential.
- Feedback into subsequent S1 behaviour: the chosen partition determines which agents run, their allowed surfaces and when dependent work may begin; failed coordination conditions prevent conflicting parallel execution.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: Headcount names a concrete destructive interaction between S1s and supplies an agent-owned coordination decision specifically to attenuate it.

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

- State: C
- Function: independently challenge producer/department claims through a separate reviewer that inspects the underlying artifact/evidence and can return blocking or corrective findings.
- Disturbance / variety regulated: optimistic producer self-report, unsafe design/implementation, legal/security facts hidden by ordinary functional summaries and self-review bias.
- Decisive decision or feedback right: independently judge the producer's artifact/finding and issue a blocking or pass/corrective review outcome.
- Decision owner: constructor path. Headcount supplies the review method and independence contract, but the assessed installed-plugin boundary does not itself wire a distinct autonomous reviewer actor that owns this judgment.
- Supporting / enforcement mechanisms: reviewer-class skill semantics, `agent-hierarchy` producer/auditor separation, read-only reviewer requirements, blocking-findings return contracts and optional guard machinery when a user instantiates the hierarchy.
- Closure path: when composed, a separate reviewer inspects the actual artifact/evidence, returns findings and blocking status, and the orchestrator/Chief Executive plus responsible producer consume the result before further commitment. The first-party method defines this loop, but the independent reviewer identity/wiring must still be instantiated in the target organization.
- Why this is / is not agent-owned: `agent-hierarchy` specifically exposes the organizational audit primitive and requires producer and auditor to be different, while `security-architecture-review` defines the complementary raw-artifact judgment and blocking return. However, at the pinned independently installed plugin boundary, the security plugin ships the skill rather than a separately wired reviewer agent. The root `.claude/agents/security-review.md` is a concrete autonomous implementation for maintaining Headcount's own repository, which is a different system-in-focus and cannot be borrowed to upgrade the user-facing path to `A`.
- Evidence: `agent-hierarchy/SKILL.md` requires producer/auditor separation and read-only reviewers; `docs/GETTING-STARTED.md` and `docs/USE-CASES.md` describe reviewer-class blocking semantics; `security-architecture-review/SKILL.md` requires reading the actual artifact and returning blocking findings/fixes; `plugins/security/.claude-plugin/plugin.json` defines the installed security-plugin boundary; root `docs/AGENT-SURFACES.md` / `.claude/agents/security-review.md` demonstrate a separate repository-development instantiation rather than packaged plugin wiring.
- Basis: explicit + structural
- Confidence: high
- Caveats: the repository proves that Headcount's own maintainers instantiate the reviewer pattern autonomously, but same-repository dogfood does not establish that the actor is present in the assessed standard distribution. A future supported distribution that packages/wires the independent reviewer could justify `A` without changing the S3* functional mapping.
- Claim being audited: that a producer's design/change/functional recommendation is safe, legally/technically acceptable or ready to proceed.
- Ordinary reporting path: the producing department/specialist returns its own artifact and summary through its normal engagement/return contract.
- Complementary access path: the supplied review skills/method require a separate reviewer to inspect the actual design/change/artifact and applicable evidence rather than relying on the producer's self-assessment.
- Independence boundary: independence is an explicit first-party construction rule, but the distinct reviewer actor must be instantiated by the host/user organization at the assessed distribution boundary.
- Who acts on findings: the orchestrator/Chief Executive and responsible producer consume the blocking finding, correction and escalation path once the reviewer lane has been composed.

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
- Confidence: medium
- Caveats: the skill states that genuinely owner-reserved decisions should be identified rather than decided for the human. The reviewed standard distribution does not specify a sufficiently explicit separate parent S5 trigger/return protocol to publish `A(P)`, so only the evidenced agent-owned internal S5 closure is encoded.
- Identity / ultimate-policy issue: organizational purpose/direction, authoritative strategy and final policy-level cross-functional choice.
- Ultimate authority in each claimed mode: Chief Executive agent for the claimed autonomous internal mode.
- Return-to-operation path: the Chief Executive's strategy/priority/tradeoff decision produces explicit handoffs and changes the direction/allocation under which departments subsequently operate.

## Recursion

Departments have durable remits and local environments, but this assessment does not infer a complete recursive viable system for every department. The six-function mapping is for the assembled Headcount organization at the chosen recursion.

## Variety and escalation

Department specialization distributes local variety. The shipped coordination method attenuates destructive parallelism; reviewer-class methods expose a complementary challenge path that requires independent actor composition; the Chief Executive absorbs cross-functional/current and identity-level variety that specialists cannot settle; the CSO carries external/future variety into that executive conversation.

## Evidence gaps

The largest uncertainty is distribution closure. Headcount is predominantly a skill/organization package whose execution depends on a supported host, not a standalone daemon. In particular, the pinned repository contains a strong autonomous repository-development reviewer organization under root `.claude/agents/*`, but the independently installed department plugins do not at this revision demonstrate that the same reviewer actor is packaged/wired into the user-facing organization. The classification therefore keeps S3* at constructor level rather than borrowing a development-only actor across the system boundary.

## Admission conclusion

Canonical vector: `A A A C A A`.

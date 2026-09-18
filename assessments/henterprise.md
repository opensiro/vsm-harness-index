---
harness_id: henterprise
project_name: Henterprise
repository: https://github.com/humbertobellor/henterprise
review_ref: 0bd56397676462e216f92b5b7800919a3597a99a
reviewed_at: 2026-09-19
generated_profile_version: 0.2.2
generated_assessment_procedure_version: 0.3.4
profile_version: 0.2.2
assessment_procedure_version: 0.3.4
assessment_changed_at: 2026-09-19
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C
autonomy_s3_star: C
autonomy_s4: C
autonomy_s5: C
---

# Henterprise

## Review boundary

- System in focus: Henterprise's first-party organizational layer for Hermes Agent at pinned revision `0bd56397676462e216f92b5b7800919a3597a99a`, including its 16 departmental skill trees, staged `SOUL.md` personas, executive/escalation relationships, reviewer-class departments, and bundled organizational methods.
- Purpose and identity: provide a virtual agentic enterprise organization in which Hermes agents can perform specialized departmental work and use explicit paths for coordination, current control, independent review, strategic adaptation, and ultimate organizational direction.
- Relevant environment: user/business requests, projects, markets, regulation, technology, risk, delivery capacity, organizational commitments, and the Hermes Agent runtime that executes the supplied profiles and skills.
- Standard-distribution boundary: first-party Henterprise repository contents and documented Hermes installation modes. Hermes itself is an external execution host and is not credited with Henterprise-specific metasystem functions merely because it loads these skills.
- First-party operating / deployment modes considered: one Hermes profile with the complete Henterprise skill tree; one Hermes profile per department using the supplied departmental `SOUL.md`; and separate reviewer-class Security and Legal & Risk profiles.
- Recursion level: one installed Henterprise virtual organization. Departmental profiles are candidate operational units, but departmental hierarchy alone does not establish recursive viability.
- Reviewed revision: `0bd56397676462e216f92b5b7800919a3597a99a`.
- Observation date: 2026-09-19.
- Generated Profile version: `0.2.2`.
- Generated Methodology version: `0.3.4`.
- Current Profile version: `0.2.2`.
- Current Methodology version: `0.3.4`.

## Repository architecture

Henterprise is an organizational skill/persona layer rather than a standalone agent runtime. The repository contains 16 departments, 143 Hermes skills, staged `SOUL.md` files for departmental profiles, a migration report, and a validator for the Hermes skill contract.

The top-level README documents two important deployment arrangements. A single Hermes profile may see the whole skill tree, with the Executive persona as the natural organization-wide soul. Alternatively, each department may run as its own Hermes profile. The latter is explicitly important for Security and Legal & Risk, which are reviewer-class departments intended to remain separate from producing profiles.

The repository also assigns specific decision rights. The Chief Executive owns direction and cross-functional arbitration; the COO owns execution/process boundaries; the PMO owns portfolio intake/capacity and resource contention; Corporate Strategy owns long-horizon options and scenario work; Security and Legal & Risk independently review producing departments.

These mappings are not taken from role names. The positive findings below depend on the concrete disturbances, decision rights, independence rules, and return paths documented in the relevant skills.

Primary evidence:

- [`README.md`](https://github.com/humbertobellor/henterprise/blob/0bd56397676462e216f92b5b7800919a3597a99a/README.md) — 16-department boundary, one-profile and per-department modes, reviewer-class deployment guidance.
- [`OUTPUT.md`](https://github.com/humbertobellor/henterprise/blob/0bd56397676462e216f92b5b7800919a3597a99a/OUTPUT.md) — migration boundary, staged souls, reviewer-class preservation, and Hermes-specific packaging.
- [`executive/SOUL.md`](https://github.com/humbertobellor/henterprise/blob/0bd56397676462e216f92b5b7800919a3597a99a/executive/SOUL.md) and [`executive/chief-executive/SKILL.md`](https://github.com/humbertobellor/henterprise/blob/0bd56397676462e216f92b5b7800919a3597a99a/executive/chief-executive/SKILL.md) — direction, capital/attention allocation, cross-functional arbitration and endpoint escalation.
- [`pmo/dependency-and-risk-management/SKILL.md`](https://github.com/humbertobellor/henterprise/blob/0bd56397676462e216f92b5b7800919a3597a99a/pmo/dependency-and-risk-management/SKILL.md) — cross-team commitments, two-way dependency tracking and escalation.
- [`pmo/head-of-pmo/SKILL.md`](https://github.com/humbertobellor/henterprise/blob/0bd56397676462e216f92b5b7800919a3597a99a/pmo/head-of-pmo/SKILL.md) and [`pmo/portfolio-governance/SKILL.md`](https://github.com/humbertobellor/henterprise/blob/0bd56397676462e216f92b5b7800919a3597a99a/pmo/portfolio-governance/SKILL.md) — portfolio capacity, gates, current commitments and resource contention.
- [`security/chief-information-security-officer/SKILL.md`](https://github.com/humbertobellor/henterprise/blob/0bd56397676462e216f92b5b7800919a3597a99a/security/chief-information-security-officer/SKILL.md) and [`legal-risk/SOUL.md`](https://github.com/humbertobellor/henterprise/blob/0bd56397676462e216f92b5b7800919a3597a99a/legal-risk/SOUL.md) — independent reviewer-class authority and escalation.
- [`corporate-strategy/chief-strategy-officer/SKILL.md`](https://github.com/humbertobellor/henterprise/blob/0bd56397676462e216f92b5b7800919a3597a99a/corporate-strategy/chief-strategy-officer/SKILL.md) and [`corporate-strategy/scenario-planning/SKILL.md`](https://github.com/humbertobellor/henterprise/blob/0bd56397676462e216f92b5b7800919a3597a99a/corporate-strategy/scenario-planning/SKILL.md) — outside/future strategy and adaptation options.
- [`executive/agent-hierarchy/SKILL.md`](https://github.com/humbertobellor/henterprise/blob/0bd56397676462e216f92b5b7800919a3597a99a/executive/agent-hierarchy/SKILL.md) — explicit builder/reviewer separation, authority categories, write-surface conflict control and a portable organization-construction method.

## Operational model

Hermes supplies the underlying autonomous model/tool loop. Henterprise supplies the organizational specialization, decision procedures, escalation relationships, reviewer independence, and role-specific constraints used by that loop.

Departmental profile agents can directly produce domain-specific judgments and work products. In the per-department mode, the repository also exposes explicit cross-profile organizational relationships. However, Henterprise does not ship a durable shared control plane that automatically transports every handoff, stores portfolio or strategy state, routes artifacts to reviewer profiles, monitors indicators, or applies returned decisions across all profiles.

The assessment therefore distinguishes autonomous local operation from higher-level constructor paths. S2-S5 are positive because the repository supplies function-specific decision/feedback surfaces, not because generic Hermes extensibility could be programmed into those functions. They remain `C` because the cross-profile actor/transport/state/closure needed for autonomous whole-organization execution still has to be composed by the operator or surrounding runtime.

## S1 — Operations

- State: `A`.
- Function: departmental Hermes agents directly produce domain-specific enterprise outcomes using the supplied skills and personas.
- Disturbance / variety regulated: task-specific business requests, domain evidence, constraints, trade-offs, and tool/environment observations within each department's remit.
- Decisive decision or feedback right: choose the substantive domain reasoning, recommendation, analysis, or action needed to produce the requested bounded outcome.
- Decision owner: the Hermes agent actor running the relevant Henterprise profile/skill.
- Supporting / enforcement mechanisms: Hermes skill discovery and execution, departmental `SOUL.md`, skill procedures, related-skill references, and verification sections.
- Closure path: request enters the agent loop; Henterprise selects/bounds the departmental capability; the agent produces and returns the domain outcome to the user or invoking work context.
- Why this is / is not agent-owned: the substantive domain judgment remains model-driven and discretionary within the supplied remit; Henterprise's Markdown contracts shape that discretion but do not deterministically produce the answer.
- Evidence: top-level README and departmental souls, including `technology/SOUL.md` and `executive/SOUL.md`.
- Basis: `explicit` and `structural`.
- Confidence: high.
- Caveats: Henterprise depends on Hermes Agent for the underlying autonomous execution loop and is therefore assessed as an organizational harness layer over that execution host.

## S2 — Coordination

- State: `C`.
- Function: regulate cross-unit dependencies and handoff failures so separately responsible operational units do not proceed on incompatible or unaccepted commitments.
- Disturbance / variety regulated: unowned dependencies, one-sided assumptions about what another team owes, cross-functional handoff failures, and resulting delivery interference.
- Distinct S1 units: separate departmental Hermes profiles, including producing units such as Product, Technology, Operations, Finance, Marketing, and other departments.
- Inter-S1 disturbance: one unit can depend on another without the owning unit having accepted the commitment; teams can track what they are owed while failing to track what they owe, producing structurally inconsistent plans and late handoffs.
- Attenuating coordination relation: the dependency method requires what is needed, from whom, by when, and an explicit owning-team commitment represented on that team's plan; dependencies are tracked in both directions and escalated when they exceed local authority or approach their decision date.
- Feedback into subsequent S1 behaviour: the coordination result is intended to become a dated commitment on the owning unit's plan or an escalation that changes the plan before the dependency fails.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the path addresses a concrete inter-unit instability — mutually inconsistent dependency commitments — rather than merely moving messages or assigning work.
- Decisive decision or feedback right: accept/revise the cross-unit commitment and determine when the unresolved dependency must escalate.
- Decision owner: a designated PMO/operations agent in the supplied organizational design, but the repository does not autonomously transport and persist those commitments across separate Hermes profiles.
- Supporting / enforcement mechanisms: department boundaries, explicit dependency fields, escalation instructions, and related-skill routing.
- Closure path: Henterprise defines the S2-specific commitment/feedback path, but the actual cross-profile message/state transport and continuing shared commitment ledger require composition.
- Why this is / is not agent-owned: the intended coordinator is agentic, but Henterprise does not itself close the organizational loop in the documented multi-profile mode; this therefore meets the constructor rather than autonomous threshold.
- Evidence: `pmo/dependency-and-risk-management/SKILL.md`; `operations/chief-operating-officer/SKILL.md` for cross-functional handoff responsibility.
- Basis: `explicit` and `structural`.
- Confidence: high.
- Caveats: the positive mapping does not rely on ordinary delegation or skill cross-references; it relies on the explicit dependency/handoff disturbance and its coordination procedure.

## S3 — Inside-and-now control

- State: `C`.
- Function: regulate current organization-wide commitments, portfolio capacity, priorities, and intervention on behalf of the whole.
- Disturbance / variety regulated: portfolio overcommitment, excessive work in progress, competing initiatives, resource contention, recurring execution failures, and cross-functional priority conflicts.
- Whole-system current view: the PMO is explicitly tasked with making organization-wide delivery capacity visible; the Chief Executive receives cross-functional considerations and owns allocation of capital and attention.
- Current-control decision scope: decide which work proceeds, draw the line at actual capacity, stop/pause/redirect work at stage gates, resolve resource contention, and arbitrate present cross-functional trade-offs.
- Decisive decision or feedback right: select which current commitments the organization carries and which are displaced, stopped, or redirected.
- Decision owner: the designated PMO/COO/Chief Executive agent according to the concrete current-control issue.
- Supporting / enforcement mechanisms: stage-gate procedures, capacity measurement, portfolio records, operating cadence, owned artifacts and escalation conventions.
- Closure path: Henterprise specifies that gates can stop, pause, or redirect work and that each approval should displace another commitment when capacity is fixed; applying those decisions across separately running departmental profiles still requires a composed shared state/transport layer.
- Why this is / is not agent-owned: the S3-specific decision rights and agent roles are explicit, but durable whole-system execution of their decisions is not closed by Henterprise alone; the standard distribution therefore exposes a constructor path.
- Evidence: `pmo/head-of-pmo/SKILL.md`, `pmo/portfolio-governance/SKILL.md`, `operations/chief-operating-officer/SKILL.md`, and `executive/chief-executive/SKILL.md`.
- Basis: `explicit`.
- Confidence: high.
- Caveats: resource contention at portfolio level is S3 evidence here; S2 above is established separately through cross-unit dependency/handoff regulation.

## S3* — Complementary audit

- State: `C`.
- Function: independently challenge security, legal, compliance, and other producer claims through reviewer-class units with authority the producing department cannot silently overrule.
- Disturbance / variety regulated: producer self-review bias, unsafe designs or commitments, risk being downgraded to fit delivery authority, and compliance findings being closed by the same unit that created them.
- Claim being audited: whether a produced design, commitment, contract term, security posture, compliance state, or accepted risk is actually acceptable.
- Ordinary reporting path: the producing department creates the artifact/decision and would otherwise report its own readiness or risk assessment.
- Complementary access path: separate Security and Legal & Risk reviewer-class profiles are intended to inspect what other departments build or commit to and return findings outside the producing department's ordinary authority path.
- Independence boundary: blocking findings are not overrulable by the department under review; Security is explicitly separated from Technology, and Legal & Risk states that a producing department cannot approve its own contract terms, accept its own above-threshold risk, or close its own compliance finding.
- Who acts on findings: the reviewer agent owns the finding; unresolved acceptance escalates to the Chief Executive, which may accept risk on the record.
- Decisive decision or feedback right: issue the independent finding/block and determine whether the matter can proceed locally or requires top-level risk acceptance.
- Decision owner: the intended independent reviewer agent.
- Supporting / enforcement mechanisms: separate profile/SOUL installation, organizational reporting separation, non-overrule rules, explicit blocking semantics, and named risk-acceptance records.
- Closure path: finding → block or escalation → Chief Executive risk acceptance or correction → affected work may proceed under the returned decision. The repository defines that path but does not itself route artifacts/findings and enforce the block across separately running Hermes profiles.
- Why this is / is not agent-owned: the reviewer judgment is designed to be agent-owned, but the standard distribution leaves the inter-profile audit invocation and enforcement closure to composition; the result is `C`, not `A`.
- Evidence: `security/chief-information-security-officer/SKILL.md`, `legal-risk/SOUL.md`, and top-level README guidance to run reviewer-class departments as separate profiles.
- Basis: `explicit` and `structural`.
- Confidence: high.
- Caveats: the one-profile-for-everything mode weakens the independence boundary; the constructor claim rests on the explicitly documented separate-profile reviewer mode.

## S4 — Outside-and-then intelligence

- State: `C`.
- Function: model external and prospective conditions, develop adaptation options, and return them toward present organizational capability and allocation decisions.
- Disturbance / variety regulated: changing markets, competitors, regulation, technology, partnerships, acquisition opportunities, uncertain multi-year conditions, and falsified strategic assumptions.
- External distinction: markets, segments, competitors, regulation, technology shifts, strategic partnerships, acquisitions/divestitures, and other conditions outside current internal execution.
- Future / prospective distinction: multi-year horizon, scenario quadrants, load-bearing uncertainties, early-warning indicators, and assumptions whose falsification should change the strategy.
- Adaptation option generated: robust moves, contingent moves, real options, market/business entry or exit choices, build/buy/partner choices, and portfolio recommendations.
- Path back into current capability / S3: the strategy role hands recommendations to the Chief Executive and Finance; scenario planning names actions to take now and indicators that should trigger revisiting the plan. Henterprise does not itself monitor those indicators or propagate the resulting strategy revision through persistent organization-wide state.
- Decisive decision or feedback right: develop/revise strategic options and recommend changes when environmental assumptions or future scenarios alter the viable choice set.
- Decision owner: the intended Corporate Strategy agent.
- Supporting / enforcement mechanisms: scenario templates, assumption lists, indicator ownership/review cadence, related-skill routing, and executive/finance escalation.
- Closure path: outside/future distinction → strategic option/recommendation → executive/finance handoff → intended change to present allocation/capability; the last cross-profile return remains composition-dependent.
- Why this is / is not agent-owned: Henterprise supplies an S4-specific agent role and adaptation procedure, but no autonomous monitoring/return loop that closes the organizational adaptation cycle across profiles.
- Evidence: `corporate-strategy/chief-strategy-officer/SKILL.md` and `corporate-strategy/scenario-planning/SKILL.md`.
- Basis: `explicit`.
- Confidence: high.
- Caveats: ordinary task planning is not counted as S4; the positive path depends on explicit external/future strategy and scenario work.

## S5 — Policy and identity

- State: `C`.
- Function: establish organizational direction, identity boundaries, and ultimate arbitration where lower-level functions cannot settle a question.
- Disturbance / variety regulated: disagreement over what the organization is for, what it will not do, which strategy is authoritative, and cross-functional conflicts that require an organization-level rather than departmental choice.
- Identity / ultimate-policy issue: organizational purpose/direction, explicit exclusions, strategy of record, priority stack, and final policy-level cross-functional trade-offs.
- Ultimate authority in each claimed mode: the supplied Chief Executive agent role is designated as the internal escalation endpoint and owner of direction for the constructor path.
- Return-to-operation path: executive decisions are required to end with concrete handoffs/owners/dates and are intended to govern subsequent departmental priorities and work; Henterprise does not persist or automatically apply that policy state across separately running profiles.
- Decisive decision or feedback right: set direction and resolve ultimate internal policy conflicts no subordinate executive can settle.
- Decision owner: the intended Chief Executive agent.
- Supporting / enforcement mechanisms: Executive `SOUL.md`, `chief-executive` skill, subordinate escalation rules, strategy/priority artifacts, and return-contract conventions.
- Closure path: identity/policy conflict → Chief Executive decision → explicit handoff/priority consequences → intended subsequent departmental operation. The final return across the multi-profile organization remains composition-dependent.
- Why this is / is not agent-owned: Henterprise supplies a function-specific autonomous role and decision surface, but not a complete first-party organizational runtime that closes the returned policy across all departmental profiles; the state is therefore `C`.
- Evidence: `executive/SOUL.md`, `executive/chief-executive/SKILL.md`, and `corporate-strategy/chief-strategy-officer/SKILL.md` for final strategy ownership.
- Basis: `explicit`.
- Confidence: high.
- Caveats: the Executive persona says genuinely owner-reserved matters should be returned to the owner, but the repository does not define a sufficiently specific identity/ultimate-policy parent trigger and returned decision loop to publish `P` or `C(P)`. Generic human installation, invocation, or override is not enough.

## Distributed OSS parent arrangement

Henterprise is public OSS, but repository maintainer/contributor governance is not used to infer a parent-governed S3/S4/S5 mode for the installed virtual organization. The system-in-focus is the Henterprise/Hermes organization at runtime, not the GitHub project that maintains the skill files.

No organization-level `(P)` path is published merely because a human installs profiles, chooses a `SOUL.md`, edits a skill, or can ignore an agent recommendation.

## Self-hosted and non-human modes

Henterprise is designed for locally configured Hermes profiles and therefore naturally supports operator-controlled deployment. Operator presence by itself does not establish `(P)`. No function-specific parent-governed loop meeting Methodology 0.3.4 was established for S3, S4, or S5 at the declared runtime boundary.

## Recursion

Henterprise has substantial hierarchy but does not establish VSM recursion by hierarchy alone. Departments have distinct personas, remits, owned artifacts, specialist skills and escalation paths, but the reviewed evidence does not show each department independently closing the operational and metasystemic functions needed to count as a recursively viable subsystem.

The bundled `agent-hierarchy` method can construct orchestrator/builder/reviewer arrangements with authority maps and producer/auditor separation. That is a constructor capability; it is not evidence that Henterprise's own departments are already complete recursive viable systems.

## Variety and escalation

Henterprise attenuates organizational variety primarily through specialization and explicit authority boundaries:

```text
business/user disturbance
        ↓
department / skill selection
        ↓
local agent discretion
        ↓
cross-unit dependency, current-control issue, review finding,
future adaptation question, or identity/policy conflict
        ↓
function-specific constructor path
        ↓
Chief Executive escalation where lower authority is insufficient
```

Notable mechanisms include narrow departmental ownership, artifacts of record, dated dependency commitments, PMO capacity/gating, independent reviewer classes, long-horizon strategy/scenario methods, and Chief Executive escalation.

The main missing capability is not organizational semantics but runtime closure. The repository describes who should decide and how signals should move more completely than it implements durable cross-profile transport, shared state, automatic invocation, monitoring, and enforcement.

## Evidence gaps

The principal unresolved implementation boundary is Hermes itself and the wiring between separately installed departmental profiles. No Henterprise-local execution trace was found demonstrating a complete cross-profile cycle such as:

```text
Technology output
→ Security independent review
→ blocking finding
→ Chief Executive risk acceptance
→ decision returned to Technology
→ changed subsequent operation
```

Likewise, no Henterprise-local persistent organizational state was established for dependency commitments, portfolio capacity, strategy of record, accepted-risk records, early-warning indicators, or executive decisions. These gaps do not erase the highly specific constructor paths, but they prevent upgrading S2-S5 from `C` to `A` at the reviewed repository boundary.

## Admission conclusion

Canonical standalone vector at the reviewed revision:

```text
A C C C C C
```

Henterprise qualifies for inclusion as an autonomous-agent organizational harness. Its distinguishing property is that the higher VSM functions are not inferred from generic messaging, graph structure, role names, or framework extensibility. The repository contains explicit function-specific organizational procedures for cross-unit coordination, portfolio/current control, independent reviewer audit, external/future adaptation, and ultimate direction/policy.

At the same time, Henterprise remains constructor-heavy: it supplies organizational decision surfaces much more completely than it supplies the runtime channels/state needed to close them across separately running Hermes profiles. This is why the resulting vector is `A C C C C C`, rather than either a role-name-driven all-`A` classification or an overly strict `A — — — — —`.

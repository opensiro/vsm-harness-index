---
harness_id: agent-starter-kit
project_name: Agent Starter Kit
repository: https://github.com/ntorga/agent-starter-kit
review_ref: 851e942ad94f98819cfe550da99c033444c10397
reviewed_at: 2026-10-27
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# Agent Starter Kit

## Review boundary

- System in focus: The installed .agents framework's full Maestro/persona orchestration mode in a documented supported coding-agent host.
- Purpose and identity: Deliver software work through specialized personas with scoped dispatch, reviewed epics and persistent session context.
- Relevant environment: User requirements, project code/files, external/native model CLIs, conflicting edits, provider failures and changing implementation facts.
- Standard-distribution boundary: First-party ENTRYPOINT→Maestro→boot/dispatch/plan/review skills and registered personas; the external host provides model/tools, while this framework supplies the installed operational roles. Freeze actual source rather than following later auto-updates.
- Credited operating / distribution surfaces: [ENTRYPOINT.md](https://github.com/ntorga/agent-starter-kit/blob/851e942ad94f98819cfe550da99c033444c10397/ENTRYPOINT.md); [personas/maestro.md](https://github.com/ntorga/agent-starter-kit/blob/851e942ad94f98819cfe550da99c033444c10397/personas/maestro.md); [personas/coder.md](https://github.com/ntorga/agent-starter-kit/blob/851e942ad94f98819cfe550da99c033444c10397/personas/coder.md); [skills/dispatch/SKILL.md](https://github.com/ntorga/agent-starter-kit/blob/851e942ad94f98819cfe550da99c033444c10397/skills/dispatch/SKILL.md); [skills/plan-management/SKILL.md](https://github.com/ntorga/agent-starter-kit/blob/851e942ad94f98819cfe550da99c033444c10397/skills/plan-management/SKILL.md); [skills/review-loop/SKILL.md](https://github.com/ntorga/agent-starter-kit/blob/851e942ad94f98819cfe550da99c033444c10397/skills/review-loop/SKILL.md)
- Adjacent first-party surfaces excluded from ownership: README demo screenshots, asset test fixtures and development CHANGELOG are not executing organization actors. Third-party native host personas are explicitly not substituted for registered framework personas. Test success does not establish semantic ownership.
- First-party operating / deployment modes considered: Full orchestration via ENTRYPOINT, default quick work, native same-provider dispatch and cross-provider CLI dispatch, optional OpenCode bindings, human plan/escalation return. Assess the documented full mode; not an invented custom assembly.
- Recursion level: One installed local software team/feature, not the public maintainer organization.
- Reviewed revision: `851e942ad94f98819cfe550da99c033444c10397`
- Observation date: 2026-10-27
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

Maestro boots a file-based team, loads rules/memory, routes work to registered Architect/Coder/Reviewer/Contextualizer personas and uses native or CLI model dispatch. Persona prompts, scoped rules, skill references, acceptance criteria and limited extra context form a defined dispatch envelope. Plans persist design decisions, implementation epics and review status. File-overlap and concurrency limits constrain parallel dispatch. Model tiers can be upgraded for difficulty and a failing/low-quality external result can be redispatched natively. Human decisions over settled plan contradictions return via re-grounding. Ordinary reviewers perform incremental and final branch acceptance; Maestro's review-loop also exposes a specific raw-code spot-check of reviewer truth/completeness. Its broad persona red line against direct scanning conflicts with that instruction, so autonomous ownership of the complementary spot-check is not assumed.

## Operational model

Coder and other outcome-producing personas absorb task-specific variety through the supported host's model/tool loop and return structured handoffs. Maestro owns coordination and present-team intervention. Host subagent/CLI APIs are transport; registered first-party identity and procedures determine the decision roles. The user's settled intent limits current commitments, with explicit escalation/return for changes.

## S1 — Operations

- State: A
- Function: Produce scoped software implementation, design, context and review outcomes.
- Disturbance / variety regulated: Unknown code details, task failure, architecture facts and acceptance criteria.
- Decisive decision or feedback right: Choose local implementation/investigation steps, execute native host tools, verify and return a handoff.
- Decision owner: Registered model-backed framework personas, including Coder.
- Supporting / enforcement mechanisms: Supported host inference/tools, dispatch envelope, plan/todo/memory files and native/CLI transport.
- Closure path: Maestro dispatches a persona identity plus bounded task → persona performs/validates work → structured handoff → correction or delivery.
- Why this is / is not agent-owned: The first-party persona specifies the autonomous action/feedback procedure; host machinery executes it. Coder chooses how to satisfy the brief while yielding scope/commit authority.
- Evidence: [README.md](https://github.com/ntorga/agent-starter-kit/blob/851e942ad94f98819cfe550da99c033444c10397/README.md); [ENTRYPOINT.md](https://github.com/ntorga/agent-starter-kit/blob/851e942ad94f98819cfe550da99c033444c10397/ENTRYPOINT.md); [personas/maestro.md](https://github.com/ntorga/agent-starter-kit/blob/851e942ad94f98819cfe550da99c033444c10397/personas/maestro.md); [skills/dispatch/SKILL.md](https://github.com/ntorga/agent-starter-kit/blob/851e942ad94f98819cfe550da99c033444c10397/skills/dispatch/SKILL.md); [personas/coder.md](https://github.com/ntorga/agent-starter-kit/blob/851e942ad94f98819cfe550da99c033444c10397/personas/coder.md)
- Basis: structural
- Confidence: high within the declared source boundary
- Caveats: Static source evidence; no live model/provider run or empirical viability claim.
- Boundary reachability: README installation and ENTRYPOINT boot wire the registered personas to explicit native and CLI dispatch instructions. No bespoke persona workflow is required after installation.

## S2 — Coordination

- State: A
- Function: Attenuate concrete shared-file interference among parallel coding personas.
- Disturbance / variety regulated: Concurrent dispatches with overlapping file scopes can overwrite/conflict; too many concurrent jobs exceed the prescribed team concurrency.
- Decisive decision or feedback right: Compare scopes, choose non-overlapping parallel groups and serialize unavoidable overlaps.
- Decision owner: Maestro agent.
- Supporting / enforcement mechanisms: Dispatch envelopes, plan parallelizable-group annotations and host task/CLI execution.
- Closure path: Scope declarations and plan/handoffs inform Maestro grouping; serialized or narrowed dispatch changes which persona can write which files next.
- Why this is / is not agent-owned: The agent chooses the grouping from actual scopes; the static limit and transport are supporting constraints, not ownership.
- Evidence: [skills/dispatch/SKILL.md](https://github.com/ntorga/agent-starter-kit/blob/851e942ad94f98819cfe550da99c033444c10397/skills/dispatch/SKILL.md); [skills/plan-management/SKILL.md](https://github.com/ntorga/agent-starter-kit/blob/851e942ad94f98819cfe550da99c033444c10397/skills/plan-management/SKILL.md); [personas/maestro.md](https://github.com/ntorga/agent-starter-kit/blob/851e942ad94f98819cfe550da99c033444c10397/personas/maestro.md)
- Basis: structural
- Confidence: high within the declared source boundary
- Caveats: Instruction-level scope regulation; no universal filesystem lock/compliance guarantee.
- Boundary reachability: Maestro is required to load dispatch and plan-management; dispatch guardrails explicitly forbid overlap and cap simultaneous subagents at three.
- Distinct S1 units: Two or more dispatched coders/personas performing independently scoped outcomes.
- Inter-S1 disturbance: Overlapping parallel file writes and excessive concurrent dispatch load.
- Attenuating coordination relation: Do not overlap file scopes; serialize when unavoidable; at most three parallel subagents.
- Feedback into subsequent S1 behaviour: Plans/handoffs identify current/next scopes; subsequent dispatches are regrouped, sequenced or narrowed.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The shipped rule directly addresses file-write collisions between units; dispatch is only its carrier.

## S3 — Inside-and-now control

- State: A(P)
- Function: Regulate the installed team's current model resources, delivery commitments and exceptional intervention.
- Disturbance / variety regulated: Low-confidence/low-quality provider output, task difficulty and new facts contradicting the agreed feature plan.
- Decisive decision or feedback right: Base: choose/upgrade model tier, switch failed provider and redispatch/correct current work. Parent: decide changes to settled feature scope/commitments after escalation.
- Decision owner: Base: Maestro. Parent: user who owns the project's agreed requirements and scope.
- Supporting / enforcement mechanisms: Provider/model registry, scoped dispatch, persistent plan/session state, Architect grounding and review gates.
- Closure path: Base: handoff/review evidence → agent resource/provider/intervention choice → new dispatch. Parent: contradictory fact or changed scope → Maestro presents issue → user resolves → revised/re-grounded plan is reviewed → later Coder epic uses the returned decision.
- Why this is / is not agent-owned: Model/resource and corrective commitment judgments are agent-owned in the base mode; settled-scope revision remains with the legitimate local user in the parent mode. Host CLI invocation and saved plans enforce/transport those choices.
- Evidence: [personas/maestro.md](https://github.com/ntorga/agent-starter-kit/blob/851e942ad94f98819cfe550da99c033444c10397/personas/maestro.md); [skills/dispatch/SKILL.md](https://github.com/ntorga/agent-starter-kit/blob/851e942ad94f98819cfe550da99c033444c10397/skills/dispatch/SKILL.md); [skills/plan-management/SKILL.md](https://github.com/ntorga/agent-starter-kit/blob/851e942ad94f98819cfe550da99c033444c10397/skills/plan-management/SKILL.md); [skills/architect-impl-grounding/SKILL.md](https://github.com/ntorga/agent-starter-kit/blob/851e942ad94f98819cfe550da99c033444c10397/skills/architect-impl-grounding/SKILL.md); [skills/agent-memory/SKILL.md](https://github.com/ntorga/agent-starter-kit/blob/851e942ad94f98819cfe550da99c033444c10397/skills/agent-memory/SKILL.md)
- Basis: structural
- Confidence: high within the declared source boundary
- Caveats: Parent control is at the local feature/team recursion; ordinary git commit approval alone is not its S3 witness.
- Boundary reachability: Maestro dispatch escalation, dispatch tier/fallback rules and plan-management grounding/revision are mandatory parts of full orchestration; both modes are first-party.
- Whole-system current view: Maestro receives persona handoffs, epic progress, review verdicts and current plan/session state across the installed team.
- Current-control decision scope: Current provider/tier resources, replacement/corrective dispatch and user-reserved changes to the feature's settled commitments.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Maestro agent | Difficult work, failed/low-quality/low-confidence dispatch | Select tier/provider/fallback or corrective redispatch; subsequent persona operates under changed assignment | [dispatch](https://github.com/ntorga/agent-starter-kit/blob/851e942ad94f98819cfe550da99c033444c10397/skills/dispatch/SKILL.md), [Maestro](https://github.com/ntorga/agent-starter-kit/blob/851e942ad94f98819cfe550da99c033444c10397/personas/maestro.md) |
| Parent (`P`) | Local project user | New fact contradicts settled plan or scope/sequence/acceptance changes | User resolves escalation; plan is revised, re-grounded/reviewed and used for later epic | [plan-management](https://github.com/ntorga/agent-starter-kit/blob/851e942ad94f98819cfe550da99c033444c10397/skills/plan-management/SKILL.md), [grounding](https://github.com/ntorga/agent-starter-kit/blob/851e942ad94f98819cfe550da99c033444c10397/skills/architect-impl-grounding/SKILL.md) |

## S3* — Complementary audit

- State: C
- Function: Complement reviewer truth/completeness reports with direct sampled operational evidence.
- Disturbance / variety regulated: Reviewers can hallucinate blockers or falsely report no findings while missing risky changes.
- Decisive decision or feedback right: Inspect raw code to confirm reported findings and sample omitted error/auth/data-mutation/I/O paths, then correct reviewer assumptions, provider or framework instructions.
- Decision owner: The review-loop assigns this audit-like judgment to Maestro, but autonomous authority is not fully established because Maestro's broad red line forbids direct scanning/hands-on work.
- Supporting / enforcement mechanisms: Reviewer handoffs, changed-file list and direct code access through the host; verdict/redispatch state.
- Closure path: The supplied procedure confirms/discards claims, samples missing findings and feeds diagnosed context/design/model limitations into changed briefs/framework/provider and redispatch; authority conflict must be resolved to claim autonomous closure.
- Why this is / is not agent-owned: A specific complementary judgment/feedback path is supplied, but composition must reconcile the designated actor's conflicting authority before A can be credited. Ordinary per-epic/final QA is not itself the positive witness.
- Evidence: [skills/review-loop/SKILL.md](https://github.com/ntorga/agent-starter-kit/blob/851e942ad94f98819cfe550da99c033444c10397/skills/review-loop/SKILL.md); [personas/maestro.md](https://github.com/ntorga/agent-starter-kit/blob/851e942ad94f98819cfe550da99c033444c10397/personas/maestro.md); [personas/reviewer.md](https://github.com/ntorga/agent-starter-kit/blob/851e942ad94f98819cfe550da99c033444c10397/personas/reviewer.md); [skills/dispatch/SKILL.md](https://github.com/ntorga/agent-starter-kit/blob/851e942ad94f98819cfe550da99c033444c10397/skills/dispatch/SKILL.md)
- Basis: structural
- Confidence: medium; function-specific constructor established, autonomous authority unresolved
- Caveats: The positive is the separate checking of reviewers' claims, not mandatory QA merely renamed as audit. No independent review was executed in this assessment.
- Boundary reachability: Maestro explicitly invokes skills/review-loop/SKILL.md; step 5 exposes the function-specific raw evidence and returned control procedure in the shipped full mode. This is a concrete constructor, not arbitrary reviewer extensibility.
- Claim being audited: Reviewer blocker validity and completeness, including suspiciously clean verdicts on complex changes.
- Ordinary reporting path: Reviewer pass/partial-pass/fail handoff from routine code/plan reviews.
- Complementary access path: Maestro spot-checks claims against actual code, then samples the first three high-risk paths for missing findings.
- Independence boundary: Different role from Coder and reporting Reviewer; direct raw code can challenge their reports. Designated Maestro authority conflicts with its no-scanning red line, so fully closed autonomous independence/ownership is not asserted.
- Who acts on findings: Maestro is specified to discard false positives and alter context/instructions/provider or redispatch; a composed authority resolution is still needed.

## S4 — Outside-and-then intelligence

- State: —
- Function: No external-and-prospective adaptation loop for this installed team.
- Disturbance / variety regulated: Provider changes, reviewer errors and accumulated observations may motivate improvement.
- Decisive decision or feedback right: No qualifying first-party decisive right established for this function.
- Decision owner: No qualifying owner at the declared boundary.
- Supporting / enforcement mechanisms: The cited runtime and documentation are supporting surfaces, not decision owners.
- Closure path: No function-specific returned closure at this boundary.
- Why this is / is not agent-owned: Switching a failing current provider, repairing ambiguous briefs, storing lessons or pulling an updated framework addresses present execution/internal history; no prospective external-option loop is established.
- Evidence: [skills/boot/SKILL.md](https://github.com/ntorga/agent-starter-kit/blob/851e942ad94f98819cfe550da99c033444c10397/skills/boot/SKILL.md); [skills/agent-memory/SKILL.md](https://github.com/ntorga/agent-starter-kit/blob/851e942ad94f98819cfe550da99c033444c10397/skills/agent-memory/SKILL.md); [skills/review-loop/SKILL.md](https://github.com/ntorga/agent-starter-kit/blob/851e942ad94f98819cfe550da99c033444c10397/skills/review-loop/SKILL.md); [skills/plan-management/SKILL.md](https://github.com/ntorga/agent-starter-kit/blob/851e942ad94f98819cfe550da99c033444c10397/skills/plan-management/SKILL.md); [personas/maestro.md](https://github.com/ntorga/agent-starter-kit/blob/851e942ad94f98819cfe550da99c033444c10397/personas/maestro.md)
- Basis: structural
- Confidence: high within the declared source boundary
- Caveats: Static source evidence; no live model/provider run or empirical viability claim.

### Absence scope

- Surfaces inspected: [skills/boot/SKILL.md](https://github.com/ntorga/agent-starter-kit/blob/851e942ad94f98819cfe550da99c033444c10397/skills/boot/SKILL.md); [skills/agent-memory/SKILL.md](https://github.com/ntorga/agent-starter-kit/blob/851e942ad94f98819cfe550da99c033444c10397/skills/agent-memory/SKILL.md); [skills/review-loop/SKILL.md](https://github.com/ntorga/agent-starter-kit/blob/851e942ad94f98819cfe550da99c033444c10397/skills/review-loop/SKILL.md); [skills/plan-management/SKILL.md](https://github.com/ntorga/agent-starter-kit/blob/851e942ad94f98819cfe550da99c033444c10397/skills/plan-management/SKILL.md); [personas/maestro.md](https://github.com/ntorga/agent-starter-kit/blob/851e942ad94f98819cfe550da99c033444c10397/personas/maestro.md)
- Plausible first-party paths checked: Framework auto-update, provider/model routing, review-cause repair, long-term Observations and plan refresh.
- Why no material first-party path remains: The shipped paths do not develop future-environment adaptation options and return selected options to current capability through a coupled S3 conversation. A user can customize the framework, but that alone does not establish a parent S4 mode.

## S5 — Policy and identity

- State: —
- Function: No identity/ultimate-policy issue and authoritative return loop.
- Disturbance / variety regulated: User intent, safety/commit rules and plan contradictions limit local work.
- Decisive decision or feedback right: No qualifying first-party decisive right established for this function.
- Decision owner: No qualifying owner at the declared boundary.
- Supporting / enforcement mechanisms: The cited runtime and documentation are supporting surfaces, not decision owners.
- Closure path: No function-specific returned closure at this boundary.
- Why this is / is not agent-owned: Plan scope, acceptance and provider choices are current control; static red lines, risk confirmations and memory preferences are not ultimate-identity closure.
- Evidence: [personas/maestro.md](https://github.com/ntorga/agent-starter-kit/blob/851e942ad94f98819cfe550da99c033444c10397/personas/maestro.md); [skills/agent-decision/SKILL.md](https://github.com/ntorga/agent-starter-kit/blob/851e942ad94f98819cfe550da99c033444c10397/skills/agent-decision/SKILL.md); [skills/agent-memory/SKILL.md](https://github.com/ntorga/agent-starter-kit/blob/851e942ad94f98819cfe550da99c033444c10397/skills/agent-memory/SKILL.md); [skills/plan-management/SKILL.md](https://github.com/ntorga/agent-starter-kit/blob/851e942ad94f98819cfe550da99c033444c10397/skills/plan-management/SKILL.md); [rules/README.md](https://github.com/ntorga/agent-starter-kit/blob/851e942ad94f98819cfe550da99c033444c10397/rules/README.md)
- Basis: structural
- Confidence: high within the declared source boundary
- Caveats: Static source evidence; no live model/provider run or empirical viability claim.

### Absence scope

- Surfaces inspected: [personas/maestro.md](https://github.com/ntorga/agent-starter-kit/blob/851e942ad94f98819cfe550da99c033444c10397/personas/maestro.md); [skills/agent-decision/SKILL.md](https://github.com/ntorga/agent-starter-kit/blob/851e942ad94f98819cfe550da99c033444c10397/skills/agent-decision/SKILL.md); [skills/agent-memory/SKILL.md](https://github.com/ntorga/agent-starter-kit/blob/851e942ad94f98819cfe550da99c033444c10397/skills/agent-memory/SKILL.md); [skills/plan-management/SKILL.md](https://github.com/ntorga/agent-starter-kit/blob/851e942ad94f98819cfe550da99c033444c10397/skills/plan-management/SKILL.md); [rules/README.md](https://github.com/ntorga/agent-starter-kit/blob/851e942ad94f98819cfe550da99c033444c10397/rules/README.md)
- Plausible first-party paths checked: Maestro yield rules, user contradiction/escalation, commit authorization, persistent preferences and role/rules configuration.
- Why no material first-party path remains: No explicit identity/ultimate-policy issue is routed to legitimate final authority with a function-specific returned decision. Current feature changes and ordinary safety approvals do not become S5.

## Distributed OSS parent arrangement

The local user has the explicitly returned current-plan S3 mode. Independent installations and public contributors do not thereby establish one organization-wide parent arrangement. No S4/S5 parent mode is inferred.

## Self-hosted and non-human modes

Same-provider native and cross-provider CLI modes are first-party supported; optional OpenCode config can be skipped when dependencies are absent. These mechanisms do not inherit decision rights. Framework auto-pull was not run as an installed live agent; frozen ref is preserved.

## Recursion

Personas have bounded outcomes and local decision repertoire, but a full recursive viable metasystem for each persona is not established by nesting or dispatch.

## Variety and escalation

Loop-recovery diagnoses repeated failures and oscillation, pivots once, then returns a bounded handoff. Maestro distinguishes local corrections from user-reserved scope changes. This is reconstructable escalation, not automatically an algedonic or identity-level function.

## Evidence gaps

Source-only; no live provider/subagent execution. The S3* constructor has a concrete unresolved Maestro authority conflict (mandatory spot-check versus broad no-scanning red line); do not upgrade it to A without resolving that boundary. Native OpenCode config tests ran 4 passed/10 failed with yq unavailable; they are not claimed green. Native context-scan tests passed 11/11. Bash syntax checks pass. No external host or maintainer authority is borrowed; MIT LICENSE is present.

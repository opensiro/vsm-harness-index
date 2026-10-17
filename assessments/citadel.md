---
harness_id: citadel
project_name: Citadel
repository: https://github.com/SethGammon/Citadel
review_ref: 38f3a4e7fa13cd48cfbedde872778b847af6c842
reviewed_at: 2026-10-17
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: ?
autonomy_s4: A
autonomy_s5: —
---

# Citadel

## Review boundary

- System in focus: shipped project-local Citadel plugin at frozen source revision `38f3a4e7fa13cd48cfbedde872778b847af6c842`, including its `/do`, opt-in `/archon`/`/fleet` and `/evolve` modes, first-party skill/agent instructions, scope claims and executable helper scripts, not the external model runtime.
- Purpose and identity: provide a repeatable project-local operating/control layer for coding agents; route requests, coordinate multi-session deliverables and parallel work, preserve state/evidence and optionally improve reusable skills.
- Relevant environment: user and project Git state, tests/runtime artifacts, external provider-backed Claude Code/Codex agent, tool permissions, repository conventions, developer goals and prospective scored skill quality.
- Standard-distribution boundary: pinned first-party plugins under `.claude-plugin`/`.codex-plugin`, bundled `skills/`, `agents/`, `core/` and `scripts/` actually referenced by documented routes; explicit user invocation and configured external coding model are required. Official `v1.4.3` tag points to a **later** commit than the frozen review ref and may not donate later-only behavior.
- Credited operating / distribution surfaces: `skills/do/SKILL.md`, `skills/archon/SKILL.md`, `skills/fleet/SKILL.md`, `core/coordination/claims.js`, current project Git and campaign state, included read-only reviewer/phase-validator, opt-in `skills/evolve/SKILL.md` plus scored improvement workflow.
- Adjacent first-party surfaces excluded from ownership: docs promotional diagrams, development-only `.planning` and benchmarks/trials for Citadel itself, provider-internal cognition or vendor worktree APIs, newer official tag source after pinned SHA, unrelated optional experimental operation-control variants not wired to the declared `/do` distribution.
- First-party operating / deployment modes considered: `/do` agent instruction routing; explicitly invoked `/archon` model-directed current multiphase campaign with model-backed delegates; `/fleet` opt-in parallel non-overlapping worktree waves with coordination claims; distinct opt-in `/evolve` multi-cycle prospective skill adaptation using an approved rubric; separately selected `/review`/read-only reviewer paths. No claim that all modes are always active.
- Recursion level: one installed Citadel-managed project operation/campaign with operational coding-agent roles and a model-led campaign orchestrator; a maintainer organization or the operator's wider enterprise is outside the boundary.
- Reviewed revision: 38f3a4e7fa13cd48cfbedde872778b847af6c842.
- Observation date: 2026-10-17.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Citadel is a project-local coding-agent plugin rather than an AI inference model. A first-party `/do` skill classifies exact commands and routes nontrivial work into the bundled `/archon`, `/fleet` and more focused skill modes. In `/archon`, a provider-backed agent operating first-party instructions reads current campaign, claims scoped work, chooses phase decomposition and delegates actual repository implementation/test operations to additional model-backed agents; phase and review evidence return to the campaign record. The underlying Claude Code/Codex execution remains environmental and does not donate unrelated organizational functions ([README.md](https://github.com/SethGammon/Citadel/blob/38f3a4e7fa13cd48cfbedde872778b847af6c842/README.md); [skills/do/SKILL.md](https://github.com/SethGammon/Citadel/blob/38f3a4e7fa13cd48cfbedde872778b847af6c842/skills/do/SKILL.md); [skills/archon/SKILL.md](https://github.com/SethGammon/Citadel/blob/38f3a4e7fa13cd48cfbedde872778b847af6c842/skills/archon/SKILL.md); [skills/fleet/SKILL.md](https://github.com/SethGammon/Citadel/blob/38f3a4e7fa13cd48cfbedde872778b847af6c842/skills/fleet/SKILL.md); [core/skills/routing.js](https://github.com/SethGammon/Citadel/blob/38f3a4e7fa13cd48cfbedde872778b847af6c842/core/skills/routing.js)).

`core/coordination/claims.js` explicitly compares writable path scopes and refuses an overlapping claim. Parallel `/fleet` and `/archon` instructions read scope claims and use isolated worktrees to attenuate sibling write interference. The claim implementation is **not** a cross-process atomic transaction (lookup-before-write can race); it is credited only as a bounded conflict-aware S2 constructor rather than a universal safe merge gate ([core/coordination/claims.js](https://github.com/SethGammon/Citadel/blob/38f3a4e7fa13cd48cfbedde872778b847af6c842/core/coordination/claims.js); [core/coordination/instances.js](https://github.com/SethGammon/Citadel/blob/38f3a4e7fa13cd48cfbedde872778b847af6c842/core/coordination/instances.js); [skills/archon/SKILL.md](https://github.com/SethGammon/Citadel/blob/38f3a4e7fa13cd48cfbedde872778b847af6c842/skills/archon/SKILL.md); [skills/fleet/SKILL.md](https://github.com/SethGammon/Citadel/blob/38f3a4e7fa13cd48cfbedde872778b847af6c842/skills/fleet/SKILL.md)).

First-party `/archon` names a separate Phase Validator reviewing a worker HANDOFF, and separately checks executable end conditions/evidence. The former specifically checks HANDOFF claims, while the latter is largely acceptance verification, not automatically an independent complementary reality audit. `agents/arch-reviewer.md` and `/review` are read-only and can inspect direct source, but their invocation and a distinct audit-to-rework closure in the shipped ordinary campaign are not sufficiently established to award S3* ([skills/archon/SKILL.md](https://github.com/SethGammon/Citadel/blob/38f3a4e7fa13cd48cfbedde872778b847af6c842/skills/archon/SKILL.md); [agents/arch-reviewer.md](https://github.com/SethGammon/Citadel/blob/38f3a4e7fa13cd48cfbedde872778b847af6c842/agents/arch-reviewer.md); [skills/review/SKILL.md](https://github.com/SethGammon/Citadel/blob/38f3a4e7fa13cd48cfbedde872778b847af6c842/skills/review/SKILL.md); [core/verification/profiles.js](https://github.com/SethGammon/Citadel/blob/38f3a4e7fa13cd48cfbedde872778b847af6c842/core/verification/profiles.js)).

The separate opt-in `/evolve` director creates prospective quality hypotheses from score/research/environment feedback, scouts evidence, runs model-backed changes in isolated worktrees, verifies improvements against a rubric, integrates nonregressing changes into `SKILL.md` and distributes transferable patterns to other future skills. Its model owns iterative hypotheses/prioritization and choice of skill changes within a previously operator-approved evaluation rubric; exceptional level-up of rubric itself returns to the user. The adaptation of skills is distinct from mere replaying memory or rerunning present-task tests ([skills/evolve/SKILL.md](https://github.com/SethGammon/Citadel/blob/38f3a4e7fa13cd48cfbedde872778b847af6c842/skills/evolve/SKILL.md); [skills/learn/SKILL.md](https://github.com/SethGammon/Citadel/blob/38f3a4e7fa13cd48cfbedde872778b847af6c842/skills/learn/SKILL.md); [skills/do/SKILL.md](https://github.com/SethGammon/Citadel/blob/38f3a4e7fa13cd48cfbedde872778b847af6c842/skills/do/SKILL.md)).

## Operational model

An operator installs the pinned-supported Citadel plugin in an agent-hosted Git repository. Simple work is routed to a first-party skill and performed by a configured coding model; larger work explicitly activates `/archon` or `/fleet`, which select operational tasks/agents, set scopes and verify source/test artifacts as phases complete. When `/evolve` is explicitly requested with an approved target rubric, a model-led improvement director uses comparative feedback about existing skills to generate, test and apply options for future capability. These are source-backed *modes*, not witnessed live multicycle successes.

## S1 — Operations

- State: A
- Function: execute coding, research, review or test tasks in the target repository through first-party scoped agent roles and skills.
- Disturbance / variety regulated: variable user requirements, actual repository state, tool errors and test results.
- Decisive decision or feedback right: the configured coding model chooses and revises substantive code/research/tool steps to fulfill each bounded task.
- Decision owner: provider-backed agent operating bundled Citadel skills/prompts; provider internal inference and generic vendor tools are external.
- Supporting / enforcement mechanisms: /do routing, installed skill definitions, delegate assignments, Git worktree/checkpoint state, evidence and callbacks.
- Closure path: user outcome → route to model-backed specialist or delegate → tool/source/test work → returned result and observed evidence → correction and delivery.
- Boundary reachability: the declared pinned `/do` and `/archon` instructions are shipped plugin skills; model executor is separately installed.
- Why this is / is not agent-owned: without the model, scripts can route/validate but do not solve arbitrary engineering work.
- Evidence: [skills/do/SKILL.md](https://github.com/SethGammon/Citadel/blob/38f3a4e7fa13cd48cfbedde872778b847af6c842/skills/do/SKILL.md); [skills/archon/SKILL.md](https://github.com/SethGammon/Citadel/blob/38f3a4e7fa13cd48cfbedde872778b847af6c842/skills/archon/SKILL.md); [skills/fleet/SKILL.md](https://github.com/SethGammon/Citadel/blob/38f3a4e7fa13cd48cfbedde872778b847af6c842/skills/fleet/SKILL.md); [skills/review/SKILL.md](https://github.com/SethGammon/Citadel/blob/38f3a4e7fa13cd48cfbedde872778b847af6c842/skills/review/SKILL.md)
- Basis: direct installed skill invocation and source code
- Confidence: medium-high for supported mode, no external model run witnessed
- Caveats: not every plugin installation has a currently running autonomous delegate.

## S2 — Coordination

- State: C
- Function: attenuate concurrent inter-agent interference by detecting overlapping writable scopes and holding a competing work claim.
- Disturbance / variety regulated: simultaneous operational agents editing the same module/worktree or conflicting merge ownership.
- Decisive decision or feedback right: allow a first-party scope claim only when `findOverlap` returns no existing colliding writable scope, otherwise throw `SCOPE_OVERLAP`.
- Decision owner: first-party deterministic coordination constructor; assignment choices still belong to model orchestrator.
- Supporting / enforcement mechanisms: claim registry, prefix-overlap checks, read-only exemptions, task/worktree isolation and workflow claim/release instructions.
- Closure path: agents choose bounded scopes → claimScope compares active write owners → overlap aborts competing claim/feedback → orchestrator must re-scope/serialize work; release restores opportunity.
- Boundary reachability: core claims module is source-reachable via project-local coordination tooling and shipped /archon/fleet steps rather than merely in a document.
- Why this is / is not agent-owned: conflict resolution is a deterministic constructor, not independently model-owned S2, and no global lock guarantee follows.
- Evidence: [core/coordination/claims.js](https://github.com/SethGammon/Citadel/blob/38f3a4e7fa13cd48cfbedde872778b847af6c842/core/coordination/claims.js); [core/coordination/instances.js](https://github.com/SethGammon/Citadel/blob/38f3a4e7fa13cd48cfbedde872778b847af6c842/core/coordination/instances.js); [skills/archon/SKILL.md](https://github.com/SethGammon/Citadel/blob/38f3a4e7fa13cd48cfbedde872778b847af6c842/skills/archon/SKILL.md); [skills/fleet/SKILL.md](https://github.com/SethGammon/Citadel/blob/38f3a4e7fa13cd48cfbedde872778b847af6c842/skills/fleet/SKILL.md)
- Basis: source-structural explicit collision mechanism
- Confidence: medium, with non-atomic cross-process race caveat
- Caveats: the lookup/write sequence has a TOCTOU race; this is bounded mitigation not complete exclusion.
- Distinct S1 units: two or more concurrent model-backed fleet/campaign delegates with declared writable project paths.
- Inter-S1 disturbance: competing work on overlapping source paths can overwrite or invalidate sibling changes.
- Attenuating coordination relation: scope-overlap comparison and refusal before writing the new ownership claim; optional isolated worktrees.
- Feedback into subsequent S1 behaviour: on SCOPE_OVERLAP, competing work is held/re-scoped instead of legitimately continuing under the claimed scope.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: checks a material competing-write relation between operational agents and returns a refusal rather than just recording messages or tasks.

## S3 — Inside-and-now control

- State: A
- Function: current allocation, accountability, intervention and recovery across the scoped Citadel campaign's operational tasks and delegates.
- Disturbance / variety regulated: stalled phases, failed verifications, scope collisions, cost/resource constraints and changing evidence about current delivery.
- Decisive decision or feedback right: model Archon decides campaign phase order, delegate assignments, direction corrections, retries and escalation based on whole-campaign ledger and evidence.
- Decision owner: model-backed Archon current controller; deterministic scripts/checkpoints/evidence tests are enforcement or support.
- Supporting / enforcement mechanisms: campaign/feature/decision logs, context handoff, scope-claims, phase validator returns, command/checkpoint/human gates.
- Closure path: campaign state and active phase results → Archon model chooses intervention/redelegate/hold/advance → updates campaign and delegate action → subsequent verifier/status feedback.
- Boundary reachability: explicit supported /archon skills instruct complete campaign read, phase choice, delegation, corrective and completion decisions, not just scheduling.
- Why this is / is not agent-owned: if the Archon model is conceptually removed, the state/gates cannot select revised goals, allocate priorities or choose rework among alternatives.
- Evidence: [skills/archon/SKILL.md](https://github.com/SethGammon/Citadel/blob/38f3a4e7fa13cd48cfbedde872778b847af6c842/skills/archon/SKILL.md); [skills/do/SKILL.md](https://github.com/SethGammon/Citadel/blob/38f3a4e7fa13cd48cfbedde872778b847af6c842/skills/do/SKILL.md); [core/coordination/claims.js](https://github.com/SethGammon/Citadel/blob/38f3a4e7fa13cd48cfbedde872778b847af6c842/core/coordination/claims.js); [agents/phase-validator.md](https://github.com/SethGammon/Citadel/blob/38f3a4e7fa13cd48cfbedde872778b847af6c842/agents/phase-validator.md)
- Basis: first-party model-led shipped campaign mode
- Confidence: medium-high for source-described model authority
- Caveats: no separate parent-governed S3 mode credited merely because user can approve a blocking step.
- Whole-system current view: active campaign, phase end conditions, feature/decision ledger, delegation/claim context, blockers and verification evidence.
- Current-control decision scope: choose work owners/phase resources, rework, interruption, corrections, failure escalation and delivery closure.

## S3* — Complementary audit

- State: ?
- Function: complementary independently judged audit of operational producer claims using direct reality evidence rather than re-parsing ordinary handoffs.
- Disturbance / variety regulated: producer HANDOFF claims may be inconsistent with changed code or actual behavior.
- Decisive decision or feedback right: distinct direct-artifact reviewer could return findings to compel new producer work, but entire function-specific independently owned path is not proven.
- Decision owner: unresolved: phase-validator checks handoff claims, read-only arch-reviewer can examine files and /review independently reads diff; their binding integration into campaign rework is not established.
- Supporting / enforcement mechanisms: dedicated reviewer persona, five-pass review skill, phase-end evidence runner and phase validator.
- Closure path: plausible independent reviewer real file/diff inspection → finding → Archon action/rework; inspected default requirement instead validates HANDOFF plus ordinary test gates.
- Boundary reachability: all reviewer artifacts and /archon are packaged at exact source, yet distinct reviewer invocation and audit-specific correction path are not proven in a supported completed mode.
- Why this is / is not agent-owned: read-only role designation or test gate is insufficient to declare a separate audit authority.
- Evidence: [agents/arch-reviewer.md](https://github.com/SethGammon/Citadel/blob/38f3a4e7fa13cd48cfbedde872778b847af6c842/agents/arch-reviewer.md); [skills/review/SKILL.md](https://github.com/SethGammon/Citadel/blob/38f3a4e7fa13cd48cfbedde872778b847af6c842/skills/review/SKILL.md); [skills/archon/SKILL.md](https://github.com/SethGammon/Citadel/blob/38f3a4e7fa13cd48cfbedde872778b847af6c842/skills/archon/SKILL.md); [core/verification/profiles.js](https://github.com/SethGammon/Citadel/blob/38f3a4e7fa13cd48cfbedde872778b847af6c842/core/verification/profiles.js)
- Basis: plausible in-boundary pathway without decisive independent closure
- Confidence: medium confidence in explicit uncertainty
- Caveats: do not infer mandatory external reviewer, S3* autonomy, or independent quality from phase validator alone.
- Claim being audited: a phase's implementation and evidence really meet architectural, code/test and requested constraints.
- Ordinary reporting path: delegate HANDOFF/phase completion and verification status to Archon.
- Complementary access path: separate read-only reviewer can inspect actual source and changes; not proven tied to every qualifying phase.
- Independence boundary: dedicated read-only reviewer is distinct as a persona but first-party review-to-rework call path cannot yet be established.
- Who acts on findings: Archon can re-delegate remediation in general, but whether findings from a distinct audit alter phase advancement is unproven.

## S4 — Outside-and-then intelligence

- State: A
- Function: explicit prospective adaptation of skill capabilities to future task/environment requirements using measured feedback and model-led exploration.
- Disturbance / variety regulated: new/failing performance criteria, changed repository constraints, skill drift, unfamiliar target scores and recurring usability shortcomings.
- Decisive decision or feedback right: in opt-in /evolve mode, model director generates hypotheses/options, chooses improvement attack axes, applies tested nonregressing skill edits and cross-pollinates confirmed patterns.
- Decision owner: configured model director running shipped /evolve skill; operator sets target and approved rubric, exceptional rubric 'level-up' returns to parent but no distinct closed parent S4 mode claimed.
- Supporting / enforcement mechanisms: scoring/rubrics, scouting agents, isolated worktree experiments, belief model, evidence logs, verification oracle, commit/reload-skills and /learn pattern compilation.
- Closure path: observed external/task scores → prospective hypothesis → independent scout → model selects future skill edit → tested modification/commit → reload or future session uses changed skill, with repeated reassessment.
- Boundary reachability: shipped /evolve is user-invocable and explicitly names Phase 5 modification + Phase 6 evidence compilation + Phase 7 cross-skill application; requires approved rubric and configured provider.
- Why this is / is not agent-owned: model autonomously selects and applies evidence-backed future skill changes within its declared constraints; a static wiki or generator alone would not do this.
- Evidence: [skills/evolve/SKILL.md](https://github.com/SethGammon/Citadel/blob/38f3a4e7fa13cd48cfbedde872778b847af6c842/skills/evolve/SKILL.md); [skills/learn/SKILL.md](https://github.com/SethGammon/Citadel/blob/38f3a4e7fa13cd48cfbedde872778b847af6c842/skills/learn/SKILL.md); [skills/do/SKILL.md](https://github.com/SethGammon/Citadel/blob/38f3a4e7fa13cd48cfbedde872778b847af6c842/skills/do/SKILL.md)
- Basis: explicit skill-defined source-reachable prospective action loop
- Confidence: medium; no witnessed trials or measured improvement
- Caveats: this is **conditional opt-in** skill adaptation rather than default project control or automatically evolving the external model; rubric choice remains human prior policy.
- External distinction: skill/target quality feedback from tasks and evaluation inputs plus actual test/regression results, not simply next action on current task.
- Future / prospective distinction: updates stored skill behavior for future independent tasks and sibling skills, with pattern library cross-pollination.
- Adaptation option generated: hypothesis-driven skill patch, verified axis change or transferable pattern from observed scores.
- Path back into current capability / S3: verified edits to SKILL.md are committed and reloaded where supported or applied in the next model session, changing future task routing/behavior.

## S5 — Identity and ultimate policy

- State: —
- Function: no distinct ultimate organizational ethos/identity settlement path proven for the local project Citadel campaign.
- Disturbance / variety regulated: fundamental project/fleet identity and normative tensions between current operations and adaptation.
- Decisive decision or feedback right: legitimate ultimate policy right and normative return to mission operations would be required; no separate material path identified.
- Decision owner: human user chooses installation, project policy and approves risk/level-up; the model is not ultimate identity authority.
- Supporting / enforcement mechanisms: project-local configuration, hook permissions, risk governance, rubrics and controlled user decisions.
- Closure path: permissions, checkpoints and human approval govern task/skill changes but do not constitute independent first-party whole-system ultimate-policy closure.
- Boundary reachability: inspected /do/archon/evolve policy, project configuration, risk/manual gates and role prompts at pinned ref; no external organization borrowed.
- Why this is / is not agent-owned: ordinary approval of risky actions and metric rubric edits is not S5, and no first-party S5 autonomous loop found.
- Evidence: [skills/archon/SKILL.md](https://github.com/SethGammon/Citadel/blob/38f3a4e7fa13cd48cfbedde872778b847af6c842/skills/archon/SKILL.md); [skills/evolve/SKILL.md](https://github.com/SethGammon/Citadel/blob/38f3a4e7fa13cd48cfbedde872778b847af6c842/skills/evolve/SKILL.md); [core/config/identity.js](https://github.com/SethGammon/Citadel/blob/38f3a4e7fa13cd48cfbedde872778b847af6c842/core/config/identity.js); [skills/do/SKILL.md](https://github.com/SethGammon/Citadel/blob/38f3a4e7fa13cd48cfbedde872778b847af6c842/skills/do/SKILL.md); [docs/OPERATION_CONTROL.md](https://github.com/SethGammon/Citadel/blob/38f3a4e7fa13cd48cfbedde872778b847af6c842/docs/OPERATION_CONTROL.md)
- Basis: bounded negative at local project operation boundary
- Confidence: medium-high within inspected supported distribution
- Caveats: does not deny that the operator's institution has legitimate S5 outside Citadel.

### Absence scope

- Surfaces inspected: role/project identity config, user installation/configuration decisions, project-local guard/hook policies, current-control campaign and skill evolution/budget approvals.
- Plausible first-party paths checked: parent manual approval, project mission selection, rubric level-up, safety policy evolution, final identity/ethos settlement.
- Why no material first-party path remains: paths set operational constraints or authorize adaptive skill choices, but do not close a distinct ultimate-policy conflict/authority/return loop for the assessed local campaign.

## Evidence gaps

- Assessment sources are pinned to `38f3a4e7fa13cd48cfbedde872778b847af6c842`, not the **later** v1.4.3 tagged object or production deployment. README's advertised newer tag does not authorize copying later code into this frozen review.
- Positive functions are conditional installed skill/model operating paths, not witnessed live Claude/Codex tool calls or efficacy comparisons.
- Scope claims detect obvious write overlap but are not atomic compare-and-claim across processes; S2=C represents bounded conflict attenuation only.
- S3=A depends on opted-in multi-phase /archon with model owner, not mere deterministic CLI dispatch or user approval.
- S3*=? preserves unresolved separation of a genuine independent audit from a Phase Validator checking a HANDOFF or ordinary test acceptance.
- S4=A is opt-in /evolve's future skill editing with verified loop and current/future reload; no claim of autonomous internal model training or an experiment success rate.
- S5=— is limited to this one user's project-level harness recursion, not to a broader deploying organization or Citadel OSS governance.

## Conclusion

**Proposed general assessment, not canonical.** In separately supported explicit first-party modes: `S1=A / S2=C / S3=A / S3*=? / S4=A / S5=—`. Model-backed coding/delegate operation is S1; scope claims bound one actual inter-S1 interference as S2=C; the model Archon controls whole present multi-phase work (S3=A); complementary independent audit is unresolved; user-invoked /evolve applies verified future skill capability improvements with model judgment (S4=A); ordinary approvals and project identity do not prove S5. Modes are not claimed simultaneous or empirically witnessed.

---
harness_id: cocoplus
project_name: CocoPlus
repository: https://github.com/Snowflake-Labs/cocoplus
review_ref: b252a8e7e09da6ca3178000d1fb5f48783dffc13
reviewed_at: 2026-09-18
generated_profile_version: 0.2.2
generated_assessment_procedure_version: 0.3.4
profile_version: 0.2.2
assessment_procedure_version: 0.3.4
assessment_changed_at: 2026-09-18
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: A
autonomy_s4: C
autonomy_s5: —
---

# CocoPlus

## Review boundary

- System in focus: CocoPlus's first-party agentic operating layer over Snowflake Coco at pinned revision `b252a8e7e09da6ca3178000d1fb5f48783dffc13`, including CocoPilot/CocoForge/CocoFlow/CocoFleet, personas, lifecycle state, governance hooks, critics, evidence/proposal gates, retrospective/hygiene paths and explicit developer gates.
- Purpose and identity: structure autonomous data-engineering work into coordinated specialist workflows with current-control, independent quality challenge, governed escalation and controlled adaptation of recurring harness rules.
- Relevant environment: Snowflake/data-engineering project artifacts, external model capability changes, repository/flow state, tests/evidence, developer/operator decisions and Snowflake Coco as the underlying host.
- Standard-distribution boundary: CocoPlus skills/personas/templates/hooks/state/contracts. Snowflake Coco and provider models execute actors/tools but are not credited with organizational functions that CocoPlus does not specify.
- First-party modes considered: CocoForge expert-team loop, CocoFlow parallel/dependency execution, CocoFleet producer/critic runs, Leviathan long-running autonomy, developer human gates/steering and hygiene/model-upgrade analysis.
- Recursion level: one CocoPlus project/run organization. Specialist personas are S1 work units for the assembled organization; technical phase nesting is not automatically VSM recursion.
- Reviewed revision: `b252a8e7e09da6ca3178000d1fb5f48783dffc13`.
- Observation date: 2026-09-18.
- Generated/current Profile / Methodology: `0.2.2` / `0.3.4`.

## Repository architecture

CocoPlus extends Snowflake Coco with project lifecycle, specialist personas, persistent run state, safety/policy hooks and several organizational modes. CocoForge runs a Team Lead, specialists, a Quality Critic and Learning Curator across iterative milestone gates. CocoFlow/CocoHarvest choose safe parallelism from dependencies and isolate concurrent producer work. CocoFleet separates producers from read-only critics and can require PASS signoff. Developer gates, stop/steer controls and dispute resolution provide an explicit parent current-control mode. A model-upgrade hygiene path evaluates whether standing harness/governance rules remain load-bearing after external model capability changes and proposes adaptations without silently applying destructive rule changes.

## Primary evidence

- [`README.md`](https://github.com/Snowflake-Labs/cocoplus/blob/b252a8e7e09da6ca3178000d1fb5f48783dffc13/README.md) — Agentic Operating System boundary, specialist/fleet workflows, autonomous modes, governance, evidence/proposal gates and retrospectives/hygiene.
- [`docs/features.html`](https://github.com/Snowflake-Labs/cocoplus/blob/b252a8e7e09da6ca3178000d1fb5f48783dffc13/docs/features.html) — dependency-aware parallelism, isolated worktrees, adaptive stage parallelism, stall/recovery/escalation and run-state regulation.
- [`.cortex/skills/cocoforge/forge.skill.md`](https://github.com/Snowflake-Labs/cocoplus/blob/b252a8e7e09da6ca3178000d1fb5f48783dffc13/.cortex/skills/cocoforge/forge.skill.md) — Team Lead/Specialist/Quality Critic/Learning Curator topology, budget/team/history state, milestone gates and dispute escalation.
- [`templates/AGENTS.md.template`](https://github.com/Snowflake-Labs/cocoplus/blob/b252a8e7e09da6ca3178000d1fb5f48783dffc13/templates/AGENTS.md.template) — critic independence, developer stop/steer/human gates, run-policy immutability, fleet producer/critic separation and retrospective/hygiene requirements.
- [`.cortex/skills/cocohygiene/hygiene.skill.md`](https://github.com/Snowflake-Labs/cocoplus/blob/b252a8e7e09da6ca3178000d1fb5f48783dffc13/.cortex/skills/cocohygiene/hygiene.skill.md) — model-upgrade governance/harness audit and evidence-backed adaptation recommendations.
- [`.cortex/hooks/pre-tool-use.js`](https://github.com/Snowflake-Labs/cocoplus/blob/b252a8e7e09da6ca3178000d1fb5f48783dffc13/.cortex/hooks/pre-tool-use.js) — deterministic policy/hazard/evidence enforcement supporting but not owning organizational decisions.

## S1 — Operations

- State: A
- Function: specialist/persona agents autonomously perform the data-engineering/project transformations defined by the active CocoPlus goal/flow.
- Disturbance / variety regulated: requirements, code/data artifacts, tool/Snowflake results, tests, implementation uncertainty and bounded project-state changes within each specialist remit.
- Decisive decision or feedback right: choose local implementation/analysis/tool actions needed to complete the assigned stage/iteration outcome.
- Decision owner: model-driven CocoPlus specialist/producer agent.
- Supporting / enforcement mechanisms: personas, Snowflake Coco host, phase/stage contracts, model-tier floors, isolated worktrees, artifacts and tool/policy hooks.
- Closure path: specialists produce artifacts/evidence in their bounded stage; outputs are persisted and passed to later stage/review/current-control paths, affecting subsequent project work.
- Why this is / is not agent-owned: deterministic gates/hook policy restrict actions but do not choose the specialist's substantive solution; the model-driven actor owns local operational judgment.
- Evidence: `README.md` and CocoForge/CocoFlow documentation describe specialist agents executing build/test/review/project stages and autonomous long-running modes.
- Basis: explicit + structural
- Confidence: high
- Caveats: Snowflake Coco/model providers are external execution hosts; only CocoPlus-specified organizational decision paths are credited.

## S2 — Coordination

- State: A
- Function: regulate dependencies and destructive concurrent interference among specialist/producer S1 units while preserving useful parallelism.
- Disturbance / variety regulated: dependency-invalid stage starts, concurrent producers touching overlapping file scopes, incomplete work contaminating another agent's context and oscillation between parallelism levels after failures.
- Decisive decision or feedback right: decide which approved-plan work can run simultaneously versus must wait, and adapt stage parallelism from current dependency/failure conditions.
- Decision owner: model-driven CocoHarvest/Team Lead coordination actor operating under the first-party flow contract.
- Supporting / enforcement mechanisms: dependency graph/gates, isolated worktrees, disjoint producer `file_scope`, checkpoint artifacts, concurrency/retry budgets and deterministic dispatch guards.
- Closure path: the coordination decision changes which stages/producers dispatch, which wait, and the scope they receive; dependency/checkpoint failures and disjoint-scope enforcement prevent unsafe execution until the coordination condition changes.
- Why this is / is not agent-owned: dependency/worktree mechanisms enforce safe boundaries, while the agentic harvest/lead path chooses the useful parallelization/coordination response within them.
- Evidence: `docs/features.html` calls CocoHarvest the intelligence behind parallelism and describes dependency-aware waits/isolated worktrees/adaptive stage parallelism; `AGENTS.md.template` requires concurrent producer scopes to remain disjoint.
- Basis: explicit + structural
- Confidence: high
- Caveats: plain phase sequencing is not credited; the positive witness is the concrete dependency/write-contamination disturbance with an agent-owned parallelism decision.
- Distinct S1 units: two or more specialist/persona/producer agents executing separate CocoFlow/CocoForge/CocoFleet work.
- Inter-S1 disturbance: overlapping writes or dependency-invalid parallel stages can contaminate shared state, create conflicting outputs or cause downstream work to start from incomplete prerequisites.
- Attenuating coordination relation: CocoHarvest/Team Lead chooses parallel versus waiting/dependency order; disjoint file scopes, isolated worktrees and checkpoint gates enforce that chosen separation.
- Feedback into subsequent S1 behaviour: only admitted stages/producers dispatch, blocked dependencies remain waiting, and failure/regression signals can narrow parallelism before later execution.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the mechanism is explicitly tied to preventing cross-agent contamination and dependency conflict, not merely assigning or ordering tasks.

## S3 — Inside-and-now control

- State: A(P)
- Function: regulate current whole-run commitments, specialist dispatch, iteration/milestone progression, budgets, recovery and live intervention.
- Disturbance / variety regulated: failing iterations, budget pressure, stalled stages, specialist output disagreement, quality-gate failure, current run-policy constraints and exceptions requiring developer intervention.
- Decisive decision or feedback right: autonomous mode — choose iteration plan/dispatch/synthesis/next milestone response and current recovery within hard bounds; parent mode — clear human-gated stages, steer/stop/resume or resolve a dispute when current-control authority is deliberately reserved to the developer.
- Decision owner: autonomous mode — model-driven Team Lead/run coordinator; parent mode — developer/operator.
- Supporting / enforcement mechanisms: `forge-state.json` goal/iteration/phase/budget/team/history, milestone gates, run-policy snapshots, stall detection, retry budgets, AGENT_STOP/STEER, human-gate files and deterministic pre-tool policy hooks.
- Closure path: autonomous lead decisions change specialist assignments, iteration state and next-stage progression; parent decisions clear/retain gates, resolve disputes or stop/steer the run, and the persisted state/policy governs subsequent agents.
- Why this is / is not agent-owned: Team Lead owns current orchestration within the established run boundary; hard hooks enforce constraints, while explicitly documented human gates/dispute/steering paths preserve a separate parent-owned mode rather than being attributed to the runtime.
- Evidence: `forge.skill.md` assigns plan/dispatch/synthesis/milestone-gate decisions to Team Lead and persists whole-run state; `AGENTS.md.template` supplies AGENT_STOP/STEER, non-bypassable human gates and run-policy boundaries; `docs/features.html` supplies recovery/escalation/adaptive stage control.
- Basis: explicit + structural
- Confidence: high
- Caveats: static policy enforcement by hooks is not credited as S3 ownership; the mapping depends on Team Lead discretion and explicit returned parent decisions.
- Whole-system current view: current forge goal, iteration, phase, budget status, team, history, stage dependencies, evidence/critic status and run-policy snapshot.
- Current-control decision scope: iteration plan, specialist dispatch, synthesis, milestone progression, current recovery/parallelism and developer-gated intervention.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Model-driven Team Lead / run coordinator | Ordinary current iteration, dispatch, recovery or milestone decision inside active hard bounds | Lead updates iteration/stage/dispatch/milestone state; specialists proceed under the new current plan | `.cortex/skills/cocoforge/forge.skill.md`, `docs/features.html` |
| Parent (`P`) | Developer/operator | Human-gated stage, explicit stop/steer, refinement dispute or decision deliberately outside autonomous authority | Developer clears/retains gate, resolves dispute or steers/stops; state/policy is persisted and subsequent run behavior changes | `templates/AGENTS.md.template`, `.cortex/skills/cocoforge/forge.skill.md` |

## S3* — Complementary audit

- State: A
- Function: independently challenge specialist/producer quality claims before milestone/signoff using a structurally separated critic path.
- Disturbance / variety regulated: producer self-approval, rationalization, hidden quality regressions and acceptance of evidence that does not meet stated criteria.
- Decisive decision or feedback right: issue PASS/REJECT quality judgment from the independent evidence presented to the critic and gate progression accordingly.
- Decision owner: model-driven Quality Critic / read-only fleet critic.
- Supporting / enforcement mechanisms: critic read-only role, lack of specialist reasoning traces, default-REJECT stance, producer/critic separation, required PASS signoff and milestone/refinement gates.
- Closure path: critic verdict enters the milestone/flow state; rejection prevents acceptance/progression and drives another fix iteration/dispute, while PASS permits the governed continuation.
- Why this is / is not agent-owned: the critic agent owns the quality judgment; read-only/separation/gating mechanisms preserve independence and enforce its consequences but do not produce the judgment.
- Evidence: `AGENTS.md.template` states that the Quality Critic receives iteration outputs but not specialist reasoning traces, starts from REJECT and cannot be overruled by Team Lead; fleet mode separates producers from read-only critics and can require PASS; `forge.skill.md` places critic verdict in each milestone gate.
- Basis: explicit + structural
- Confidence: high
- Caveats: routine tests/evidence gates are not the S3* witness; the mapping is specifically the independent critic path with complementary output-level access and non-overridable feedback.
- Claim being audited: that specialist/producer iteration output meets the stated goal/quality/evidence criteria and is safe to accept for progression.
- Ordinary reporting path: specialist/producer returns its output/artifacts into the Team Lead/flow iteration.
- Complementary access path: separate Quality Critic/read-only critic receives iteration outputs/evidence without the specialist reasoning trace and evaluates them under its own criteria/default-REJECT stance.
- Independence boundary: critic is separated from producer, read-only in fleet mode, lacks producer reasoning traces and cannot be overruled by Team Lead.
- Who acts on findings: Team Lead/flow milestone control consumes PASS/REJECT; rejection forces another iteration, withheld signoff or dispute escalation before progression.

## S4 — Outside-and-then intelligence

- State: C
- Function: inspect externally changed model capability after an upgrade, determine how that changes the value of existing governance/harness rules and develop evidence-backed adaptation options for future operation.
- Disturbance / variety regulated: a newer model may make standing rules/checks newly redundant, advisory or still necessary, creating risk of stale harness constraints or unsafe premature deletion.
- Decisive decision or feedback right: judge which recurring rule/check should remain load-bearing, degrade to advisory or be proposed as obsolete after model-capability change.
- Decision owner: constructor path — CocoPlus supplies the S4-specific model-upgrade hygiene analysis, but the standard path does not autonomously close destructive rule changes; developer composition/authority is still required for returned adaptation.
- Supporting / enforcement mechanisms: `$hygiene --model-upgrade`, evidence collection across sessions/committed artifacts, retrospective/benchmark recommendations and prohibition on silent deletion.
- Closure path: hygiene produces evidence-backed keep/advisory/obsolete recommendations intended to change recurring hooks/skills/standing context, but destructive adaptation is proposed rather than automatically applied; downstream developer action must complete the return into present capability.
- Why this is / is not agent-owned: an agent can perform the prospective analysis, yet CocoPlus intentionally withholds autonomous closure over the recurring harness rules; this is therefore a supplied S4 constructor path rather than `A`.
- Evidence: `cocohygiene/hygiene.skill.md` explicitly defines a model-upgrade audit of governance rules/harness checks and classifies their future status while requiring evidence and proposing rather than silently applying deletions; `AGENTS.md.template` directs retrospective/hygiene/model benchmarking before changing recurring rules.
- Basis: explicit + structural
- Confidence: medium-high
- Caveats: generic retrospectives/learning are not credited as S4. The positive mapping is narrowly the external model-upgrade path; `C` reflects incomplete first-party adaptation closure.
- External distinction: the capability/behavior of the upgraded external model relative to the assumptions under which current CocoPlus rules were created.
- Future / prospective distinction: whether recurring governance/harness checks will remain necessary, become merely advisory or become obsolete for subsequent sessions/runs.
- Adaptation option generated: retain the rule, downgrade its standing, replace/adjust it or propose removal when evidence shows it is obsolete.
- Path back into current capability / S3: the recommendation targets recurring hooks/skills/standing context used by current runs, but developer action is still needed to apply the proposed structural change; this incomplete closure is why the state is `C`.

## S5 — Policy and identity

- State: —
- Function: no distinct runtime identity/ultimate-policy function is established at the reviewed project/run recursion beyond developer-authored policies, covenants and safety boundaries.
- Disturbance / variety regulated: autonomy covenants, hard stops, run policies, safety rules and human approvals constrain operation, but the evidence does not show a legitimate S5 identity/ultimate-policy conversation with closure separate from those constraints/current-control gates.
- Decisive decision or feedback right: no material first-party S5 decision right is established.
- Decision owner: none established for a qualifying S5 function.
- Supporting / enforcement mechanisms: covenant acceptance, run-policy snapshots, hard safety gates, human gates, policy engine, steering restrictions and persistent project configuration.
- Closure path: these controls constrain subsequent operation, but no identity/ultimate-policy issue → legitimate S5 judgment → returned organizational policy loop is established at the chosen recursion.
- Why this is / is not agent-owned: neither a static covenant/policy nor human approval over ordinary current work is sufficient to establish S5; no autonomous or parent S5 closure is inferred from enforcement.
- Evidence: `README.md`, `AGENTS.md.template`, `forge.skill.md` and `pre-tool-use.js` were inspected for ultimate-policy/identity authority; the evidenced functions are current governance, safety and developer control.
- Basis: structural
- Confidence: high
- Caveats: a wider organization operating CocoPlus can supply its own S5 outside this repository-relative project/run boundary.

### Absence scope

- Surfaces inspected: project lifecycle/persona docs, CocoForge/Leviathan activation, run policies, covenant/hard-stop rules, human gates, steering/stop controls, safety/policy hooks and persistent configuration/state.
- Plausible first-party paths checked: Leviathan covenant acceptance, developer human gates, run-policy snapshots, safety policy engine, steering rules, project identity/configuration and dispute escalation.
- Why no material first-party path remains: these surfaces authorize or constrain current execution and safety; none establishes a separate identity/ultimate-policy function with legitimate ultimate authority and a returned S5 closure at the assessed project/run recursion.

## Recursion

Specialists/personas can be dynamically composed and flows can nest phases/runs, but no child is automatically credited as a complete viable recursion. The assessment maps the assembled project/run organization.

## Variety and escalation

CocoPlus distributes operational variety across specialists, attenuates destructive parallelism through dependency/worktree/file-scope controls, uses Team Lead current regulation and independent critics for quality challenge, and escalates stalled/disputed/human-gated current decisions to the developer. Model-upgrade hygiene supplies a future-facing constructor path for adapting recurring harness controls.

## Evidence gaps

The main classification boundary is S4: model-upgrade hygiene clearly performs external/prospective analysis and develops options, but the first-party evidence intentionally stops short of automatic destructive adaptation, so `C` is used rather than `A` or `P`. No S5 state is inferred from strong governance alone.

## Admission conclusion

Canonical vector: `A A A(P) A C —`.

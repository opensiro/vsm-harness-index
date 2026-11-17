---
harness_id: frenzymath-archon
project_name: Archon
repository: https://github.com/frenzymath/Archon
review_ref: 3fe2618870808d8c20912ab8b5aff80af275a1de
reviewed_at: 2026-11-18
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Archon

## Review boundary

- System in focus: One initialized Archon Lean formalization project and its normal plan/prove/review loop, including optional parallel lanes, read-only audits and operator steering.
- Purpose and identity: Formalize supplied mathematics faithfully, close proof gaps and leave reproducible Lean and blueprint artifacts.
- Environment: Lean and Mathlib, source literature, evolving project dependency graph, parallel proof candidates, user guidance and peer project references.
- Standard-distribution boundary: Archon CLI, project state, shipped role prompts, Python phase and lane machinery, inner Git, subagent dispatch and operator UI. Lean, provider models and tools remain dependencies.
- Credited operating / distribution surfaces: Model-owned planner/prover/reviewer roles, proof worktrees and promotion, isolated auditors, discussion hints and checked per-iteration objectives.
- Adjacent first-party surfaces excluded from ownership: Cross-project scope view at a different recursion, Archon Horizon, development and release checks, external references and external mathematical authority.
- First-party operating / deployment modes considered: Standard single-lane loop, supported multi-lane execution, optional shipped read-only audits, operator project discussion with consented input to the loop.
- Recursion level: One project as a whole. Provers and proof lanes are operational units within it. Several independent projects and their coordinated scope have a separate boundary.
- Reviewed revision: `3fe2618870808d8c20912ab8b5aff80af275a1de`.
- Observation date: 2026-11-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The loop reads project state and assigns proof objectives, launches prover sessions, collects and reconciles artifacts, records standard review and re-enters planning. Optional lanes use inner-Git worktrees for simultaneous proof attempts. Enabled audit subagents use separate read-only access and report back. [Shipped formalization loop](https://github.com/frenzymath/Archon/blob/3fe2618870808d8c20912ab8b5aff80af275a1de/README.md#L267-L291) · [Planner launch and hint consumption](https://github.com/frenzymath/Archon/blob/3fe2618870808d8c20912ab8b5aff80af275a1de/src/archon/commands/loop/phases/plan.py#L246-L319) · [Multilane execution path](https://github.com/frenzymath/Archon/blob/3fe2618870808d8c20912ab8b5aff80af275a1de/src/archon/commands/loop/phases/prover.py#L102-L135) · [Merge results returned to the project](https://github.com/frenzymath/Archon/blob/3fe2618870808d8c20912ab8b5aff80af275a1de/src/archon/commands/loop/lane_round/writeback.py#L176-L241) · [Auxiliary audit dispatch and feedback](https://github.com/frenzymath/Archon/blob/3fe2618870808d8c20912ab8b5aff80af275a1de/src/archon/.archon-src/prompts/review.md#L177-L217)

## Operational model

The plan agent is responsible for project-wide current commitments. Provers exercise Lean implementation discretion and the merge model reconciles eligible outputs. The mathematician can steer work at the same recursion using the discussion-to-hints path. [Planner state, discretion and objectives](https://github.com/frenzymath/Archon/blob/3fe2618870808d8c20912ab8b5aff80af275a1de/src/archon/.archon-src/prompts/plan.md#L9-L57) · [Decisive merge actor and fallback](https://github.com/frenzymath/Archon/blob/3fe2618870808d8c20912ab8b5aff80af275a1de/src/archon/multilane/merge_agent.py#L126-L177) · [Operator current-state steering](https://github.com/frenzymath/Archon/blob/3fe2618870808d8c20912ab8b5aff80af275a1de/src/archon/commands/discuss.py#L319-L339)

## S1 — Operations

- State: A
- Function: Produce and revise Lean proofs and the corresponding mathematical project artifacts.
- Disturbance / variety regulated: Open proof holes, failed elaboration, wrong intermediate statements and changing dependencies.
- Decisive decision or feedback right: Generate or revise proof terms and tactics in the assigned target in response to Lean feedback.
- Decision owner: Model-backed prover agents. Planning specifies mathematical scope and Lean checks eligibility of a produced artifact.
- Supporting / enforcement mechanisms: Role prompts, Lean feedback, project dependency data, worker mode and protected files.
- Closure path: The proof attempt and its result return into the project's artifact, journal and later planning/repair.
- Why this is / is not agent-owned: The actual model worker selects proof and tool actions within the shipped proving phase.
- Evidence: [Shipped formalization loop](https://github.com/frenzymath/Archon/blob/3fe2618870808d8c20912ab8b5aff80af275a1de/README.md#L267-L291) · [Prover phase](https://github.com/frenzymath/Archon/blob/3fe2618870808d8c20912ab8b5aff80af275a1de/src/archon/commands/loop/phases/prover.py#L23-L79) · [Multilane execution path](https://github.com/frenzymath/Archon/blob/3fe2618870808d8c20912ab8b5aff80af275a1de/src/archon/commands/loop/phases/prover.py#L102-L135)
- Basis: Explicit and structural.
- Confidence: High.
- Caveats: A validated proof is specific to its Lean statement. The workflow also inspects correspondence to the intended mathematics.
- Boundary reachability: The standard CLI runs a real prover phase from the planner's assigned Lean objectives and supports model-backed serial or multi-lane proving.

## S2 — Coordination

- State: A
- Function: Dampen conflict between independently operating provers producing competing changes to the same Lean declarations.
- Disturbance / variety regulated: Two lanes can write overlapping implementations for the same target file and cannot both be directly written back to the shared project.
- Decisive decision or feedback right: Select a consistent proof per declaration when more than one eligible lane produces a candidate.
- Decision owner: The shipped per-file merge agent. The allocator and writeback functions supply and enforce the scope.
- Supporting / enforcement mechanisms: Worktree isolation, eligible-result grouping, model merge role and inner Git commit.
- Closure path: The merge agent chooses and writes a consistent file. The normal writeback commits it and later loop work uses the resulting main project state.
- Why this is / is not agent-owned: Isolation attenuates concurrent edits and the shipped model actor resolves conflicting candidate changes. The single-success path uses deterministic copying.
- Evidence: [Parallel lanes and operator mode](https://github.com/frenzymath/Archon/blob/3fe2618870808d8c20912ab8b5aff80af275a1de/README.md#L309-L328) · [Multilane execution path](https://github.com/frenzymath/Archon/blob/3fe2618870808d8c20912ab8b5aff80af275a1de/src/archon/commands/loop/phases/prover.py#L102-L135) · [Isolated lane worktrees](https://github.com/frenzymath/Archon/blob/3fe2618870808d8c20912ab8b5aff80af275a1de/src/archon/multilane/worktree.py#L40-L71) · [Merge results returned to the project](https://github.com/frenzymath/Archon/blob/3fe2618870808d8c20912ab8b5aff80af275a1de/src/archon/commands/loop/lane_round/writeback.py#L176-L241) · [Decisive merge actor and fallback](https://github.com/frenzymath/Archon/blob/3fe2618870808d8c20912ab8b5aff80af275a1de/src/archon/multilane/merge_agent.py#L126-L177)
- Basis: Explicit and structural.
- Confidence: High.
- Caveats: Applies to a multi-lane run with multiple eligible versions. A failed merge agent falls back to the first candidate.
- Boundary reachability: The packaged multi-lane execution selects eligible candidates and invokes the supplied merge actor when several versions of one file qualify.
- Distinct S1 units: Parallel proof lanes with separately executing model agents and independent worktrees.
- Inter-S1 disturbance: Competing proofs or declaration edits would overwrite each other in a common tree.
- Attenuating coordination relation: Separate workspaces, filter candidate files, then have a model-backed merge actor reconcile the alternatives.
- Feedback into subsequent S1 behaviour: The selected proofs replace the shared project file for subsequent compilation and planning rather than exposing simultaneous candidate branches as the same authoritative source.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The path explicitly handles conflicting model products for the same mutable project declarations.

## S3 — Inside-and-now control

- State: A(P)
- Function: Regulate the whole project's current prover commitments and provide a distinct parent-owned steering path.
- Disturbance / variety regulated: Blocked routes, finite prover effort, project-wide dependencies and evidence that the current approach should change.
- Decisive decision or feedback right: Choose which whole-project route and objectives to pursue, reallocate the next proving iteration or complete the project. In assisted operation the mathematician chooses a returned project-wide steering instruction.
- Decision owner: Plan agent in its normal autonomous mode. Mathematician as parent for explicit steering through project discussion and hints.
- Supporting / enforcement mechanisms: Project status, Lean dependency frontier, attempt and review records, protected boundaries, PROGRESS and user hints.
- Closure path: Planner reads all current work and review evidence, rewrites current objectives and dispatch uses them. In assisted mode the parent's approved steering returns through USER_HINTS, which is consumed and applied by the next planner.
- Why this is / is not agent-owned: The planner explicitly owns decisions among alternative current routes. The separate mode supplies real parent judgment and a first-party path back into the same live project loop.
- Evidence: [Planner state, discretion and objectives](https://github.com/frenzymath/Archon/blob/3fe2618870808d8c20912ab8b5aff80af275a1de/src/archon/.archon-src/prompts/plan.md#L9-L57) · [Proof strategy and corrective return](https://github.com/frenzymath/Archon/blob/3fe2618870808d8c20912ab8b5aff80af275a1de/src/archon/.archon-src/prompts/plan.md#L201-L225) · [Planner launch and hint consumption](https://github.com/frenzymath/Archon/blob/3fe2618870808d8c20912ab8b5aff80af275a1de/src/archon/commands/loop/phases/plan.py#L246-L319) · [Project completion constraint](https://github.com/frenzymath/Archon/blob/3fe2618870808d8c20912ab8b5aff80af275a1de/src/archon/commands/loop/phases/plan.py#L321-L339) · [Prover phase](https://github.com/frenzymath/Archon/blob/3fe2618870808d8c20912ab8b5aff80af275a1de/src/archon/commands/loop/phases/prover.py#L23-L79) · [Operator current-state steering](https://github.com/frenzymath/Archon/blob/3fe2618870808d8c20912ab8b5aff80af275a1de/src/archon/commands/discuss.py#L319-L339)
- Basis: Explicit and structural.
- Confidence: High.
- Caveats: Parent guidance is scoped and interpreted by the planner. It does not take over each proof or override protected requirements.
- Boundary reachability: Plan phase consumes session-derived review/attempt evidence and user hints as part of ordinary execution. The project discussion command has a supplied, consented path for recording project-wide steerage.
- Whole-system current view: Project dependency frontier, all pending and completed objectives, recent prover attempts, review recommendations, protected scope and blockers.
- Current-control decision scope: Commit or redirect project-wide prover work among candidate proof routes and current objectives. The parent path applies user-chosen guidance to how the next iteration allocates work.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Project plan agent | Project state or review evidence invalidates current proof commitments | Rewrites current objectives and dispatch consumes them | [Planner state, discretion and objectives](https://github.com/frenzymath/Archon/blob/3fe2618870808d8c20912ab8b5aff80af275a1de/src/archon/.archon-src/prompts/plan.md#L9-L57) · [Proof strategy and corrective return](https://github.com/frenzymath/Archon/blob/3fe2618870808d8c20912ab8b5aff80af275a1de/src/archon/.archon-src/prompts/plan.md#L201-L225) · [Prover phase](https://github.com/frenzymath/Archon/blob/3fe2618870808d8c20912ab8b5aff80af275a1de/src/archon/commands/loop/phases/prover.py#L23-L79) |
| Parent (`P`) | Mathematician | Whole-project status requires human steering of the current approach | User approves guidance to the plan and the next iteration consumes it | [Operator current-state steering](https://github.com/frenzymath/Archon/blob/3fe2618870808d8c20912ab8b5aff80af275a1de/src/archon/commands/discuss.py#L319-L339) · [Planner launch and hint consumption](https://github.com/frenzymath/Archon/blob/3fe2618870808d8c20912ab8b5aff80af275a1de/src/archon/commands/loop/phases/plan.py#L246-L319) |

## S3* — Complementary audit

- State: A
- Function: Check the adequacy of prover progress and planning claims through separately scoped artifact and source inspection.
- Disturbance / variety regulated: Provers may report a successful result that uses a weakened definition or invalid assumption. A strategy may claim a route is supported without grounding it in the original mathematics.
- Decisive decision or feedback right: Independently flag suspect definitions or unsupported strategy claims using an evidence channel separate from routine reports.
- Decision owner: A fresh read-only Lean auditor or strategy auditor in the enabled subagent mode. Planner and reviewer decide corrective action.
- Supporting / enforcement mechanisms: Selector and dispatch catalog, separate scoped instructions, raw source and Lean reads, reports and recommendations.
- Closure path: Lean auditor results inform review recommendations returned to the planner, with severe findings offered as refactor directives. The strategy auditor's raw reference findings can change STRATEGY and next-round objectives.
- Why this is / is not agent-owned: Separate read-only model agents make their own finding judgments. Their evidence access and prompt are distinct from the responsible prover's activity and self-report.
- Evidence: [Raw Lean audit and restricted context](https://github.com/frenzymath/Archon/blob/3fe2618870808d8c20912ab8b5aff80af275a1de/src/archon/.archon-src/subagents/lean-auditor.md#L1-L45) · [Independent raw-reference challenge](https://github.com/frenzymath/Archon/blob/3fe2618870808d8c20912ab8b5aff80af275a1de/src/archon/.archon-src/subagents/strategy-auditor.md#L1-L31) · [Auxiliary audit dispatch and feedback](https://github.com/frenzymath/Archon/blob/3fe2618870808d8c20912ab8b5aff80af275a1de/src/archon/.archon-src/prompts/review.md#L177-L217) · [Planner state, discretion and objectives](https://github.com/frenzymath/Archon/blob/3fe2618870808d8c20912ab8b5aff80af275a1de/src/archon/.archon-src/prompts/plan.md#L9-L57) · [Ordinary review and reporting path](https://github.com/frenzymath/Archon/blob/3fe2618870808d8c20912ab8b5aff80af275a1de/src/archon/commands/loop/phases/review.py#L27-L81)
- Basis: Explicit procedural and structural.
- Confidence: High.
- Caveats: Optional supported mode. Complementarity is tied to the supplied raw-artefact or raw-reference judgment, beyond the routine summary and Lean build. The Lean auditor's implicit strategy blinding is scoped to its directive.
- Boundary reachability: The review and plan prompts expose enabled read-only catalog auditors, wait for reports and route the resulting findings into the next planner decision.
- Claim being audited: The current proof increment or route supports the claimed mathematical progress and does not hide a weakened definition, unresolved assumptions or a source mismatch.
- Ordinary reporting path: Prover attempts and task results, build/sorry counts, ordinary proof journal and iteration summaries.
- Complementary access path: A separate Lean auditor reads project Lean files with minimal strategy context. A separate strategy auditor reads primary PDFs or TeX against the planned route.
- Independence boundary: Fresh, read-only sessions with scoped directives. The Lean auditor can write its report but cannot edit the proof or set its own evidence verdict in the planner's main state.
- Who acts on findings: Review agent inserts actionable findings into recommendations and the next planner selects an objective change or a structural refactor. Strategy-auditor findings return directly to the planner's current commitments.

## S4 — Outside-and-then intelligence

- State: —
- Function: Model external future change and adopt an adaptation option for the assessed project's own ongoing capability.
- Disturbance / variety regulated: New sources or peer proofs can create useful options for the current formalization.
- Decisive decision or feedback right: No supplied prospective capability decision for this project boundary was established.
- Decision owner: Planner selects current proof strategy and objectives. User owns any separately approved tooling/configuration change.
- Supporting / enforcement mechanisms: Reference search, longer-horizon proof strategy, peer inbox, read-only scope roadmap and operator editing.
- Closure path: Peer findings, sources and alternative mathematical routes support today's project backlog. Capability changes in installed skills are separately authored.
- Why this is / is not agent-owned: The scope advisor models dependencies among current projects and proposes extractions. Its declared scope and authority form an adjacent recursion, while the project loop consumes evidence for the supplied formalization.
- Evidence: [Proof strategy and corrective return](https://github.com/frenzymath/Archon/blob/3fe2618870808d8c20912ab8b5aff80af275a1de/src/archon/.archon-src/prompts/plan.md#L201-L225) · [Cross-project roadmap and operator proposals](https://github.com/frenzymath/Archon/blob/3fe2618870808d8c20912ab8b5aff80af275a1de/src/archon/commands/scope/discuss.py#L31-L87) · [Peer inbox input](https://github.com/frenzymath/Archon/blob/3fe2618870808d8c20912ab8b5aff80af275a1de/src/archon/prompts.py#L1294-L1325) · [Manual skills adaptation](https://github.com/frenzymath/Archon/blob/3fe2618870808d8c20912ab8b5aff80af275a1de/README.md#L330-L342)
- Basis: Bounded structural absence.
- Confidence: Medium.
- Caveats: A wider cross-project system or an explicitly configured external capability-adaptation role needs its own analysis.

### Absence scope

- Surfaces inspected: Project planner with literature search and persisted strategy, peer inbox, scope advisor and documented tool/skill changes.
- Plausible first-party paths checked: Prospective environmental scenarios, experimentally chosen changes to future proving resources, and applied feedback into project capability.
- Why no material first-party path remains: The primary paths resolve current mathematical targets or expose current cross-project dependencies. The shipped project loop has no demonstrated route from prospective external modeling to a governing capability decision.

## S5 — Policy and identity

- State: —
- Function: Close an identity or ultimate-policy dispute and apply the authoritative result to subsequent operation.
- Disturbance / variety regulated: Changing a protected declaration or fundamental mathematical assumption can conflict with current project instructions.
- Decisive decision or feedback right: No supplied identity-level decision protocol was established at the assessed recursion.
- Decision owner: Mathematician supplies the problem and protected constraints. Planner chooses routes within them.
- Supporting / enforcement mechanisms: Protected declarations, supplied guardrails, user notices and project discussion/steering.
- Closure path: A protected-signature blocker can reach the mathematician, and operational guidance returns to the next planner. The supplied route regulates existing project commitments.
- Why this is / is not agent-owned: The observed human rights govern scope and constraints. No mechanism is shown that adjudicates the project's ultimate purpose or policy in a distinct supported loop.
- Evidence: [Authority and protected objectives](https://github.com/frenzymath/Archon/blob/3fe2618870808d8c20912ab8b5aff80af275a1de/src/archon/.archon-src/prompts/plan.md#L40-L71) · [Parallel lanes and operator mode](https://github.com/frenzymath/Archon/blob/3fe2618870808d8c20912ab8b5aff80af275a1de/README.md#L309-L328) · [Operator current-state steering](https://github.com/frenzymath/Archon/blob/3fe2618870808d8c20912ab8b5aff80af275a1de/src/archon/commands/discuss.py#L319-L339) · [Project completion constraint](https://github.com/frenzymath/Archon/blob/3fe2618870808d8c20912ab8b5aff80af275a1de/src/archon/commands/loop/phases/plan.py#L321-L339)
- Basis: Bounded structural absence.
- Confidence: Medium.
- Caveats: A user can edit the local policy and prompts outside the assessed loop. Evidence here concerns current steering and source-fixed mathematical scope.

### Absence scope

- Surfaces inspected: Protection declaration rules, user-only blocker surface, discussion and persistent hints, completion and author modes.
- Plausible first-party paths checked: Escalation for changing a foundational statement, approval/return of a protected constraint and governing rule changes.
- Why no material first-party path remains: The reviewed paths return problem-specific instructions or begin from user-authored policy. They supply no separate ultimate-purpose or identity adjudication path.

## Distributed OSS parent arrangement

Upstream Archon maintainers own tool development. The local mathematician owns formalization scope and supported assisted project steering.

## Self-hosted and non-human modes

A locally configured project can run autonomously from its blueprint and provider setup. Human hints and explicit discussion choices support a distinct parent-assisted control path.

## Recursion

A prover lane is one operational unit. The assessed project integrates its lanes and proof goals. Multi-project scope advice is a distinct higher view.

## Variety and escalation

A stalled route or contradictory evidence can redirect proof commitments. Serious read-only audit findings enter the next planner decision. User-only blockers use the notices and discussion path. [Proof strategy and corrective return](https://github.com/frenzymath/Archon/blob/3fe2618870808d8c20912ab8b5aff80af275a1de/src/archon/.archon-src/prompts/plan.md#L201-L225) · [Auxiliary audit dispatch and feedback](https://github.com/frenzymath/Archon/blob/3fe2618870808d8c20912ab8b5aff80af275a1de/src/archon/.archon-src/prompts/review.md#L177-L217) · [Operator current-state steering](https://github.com/frenzymath/Archon/blob/3fe2618870808d8c20912ab8b5aff80af275a1de/src/archon/commands/discuss.py#L319-L339)

## Evidence gaps

Reviewed pinned sources and supplied agent instructions. No Lean builds or provider sessions were executed. Multi-lane and optional auditor states are conditional on the supported modes being enabled.

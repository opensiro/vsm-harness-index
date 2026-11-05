---
harness_id: quickmaths
project_name: QuickMaths
repository: https://github.com/genproof/QuickMaths
review_ref: c2dbb59e13b3cce451b86e600345361b34e8c5ba
reviewed_at: 2026-11-05
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: C(P)
autonomy_s3_star: C
autonomy_s4: P
autonomy_s5: —
---

# QuickMaths

## Review boundary

- System in focus: One deployed QuickMaths proving campaign: its first-party lineage/lane work cells, fleet regulation and documented experiment-manager operating mode.
- Purpose and identity: Produce Lean proofs and verified submission packages for a pinned problem campaign.
- Relevant environment: Problem statements and published mathematics, external Claude Code/model accounts, Linux hosts/quotas, reusable formalization libraries and organizers verification/resource requirements.
- Standard-distribution boundary: Installed leh CLI, packaged runtime, deployable fleet/controller/briefs/operator tools and the documented supervised experiment-manager procedure. External Claude Code internals, Lean kernels and benchmark organizers are dependencies.
- Credited operating / distribution surfaces: Actual job/agent_runner/controller/feeder wiring, ARCHITECT/LANE/REARCHITECT briefs, fleet coordinator/operator APIs, map and bank tools, and experiment-manager method linked from deployment docs.
- Adjacent first-party surfaces excluded from ownership: Repository CI, tests, historical AUDIT report, external leaderboard claims and unshipped campaign transcripts. The shipped official verification integration is runtime support; upstream evaluator ownership is not imported.
- First-party operating / deployment modes considered: Single round/lineage, multi-lane program, multi-host fleet, scheduled deterministic coordinator, and human/supervised-agent experiment manager. The manager level is explicitly not automated.
- Recursion level: Campaign organization with proof lineage/lane operational cells. Programs/rounds are work groupings; no independently viable lower recursion is assumed.
- Reviewed revision: `c2dbb59e13b3cce451b86e600345361b34e8c5ba`.
- Observation date: 2026-11-05.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The leh package deploys deterministic fleet control around model proving rounds. Jobs prepare pinned workspaces and role briefs; a first-party supervisor launches external Claude Code in a bounded sandbox; ./lean supplies controlled compile/search feedback. Feeder/controller persist lineages, proof-lane contracts, claims and official verification receipts. The fleet coordinator gathers state and applies policy-selected transfers, de-duplication and hedges. A separately operated experiment manager performs current intervention, complementary progress audits and approved capability adaptation; this level explicitly does not run automatically. [`docs/ARCHITECTURE.md`](https://github.com/genproof/QuickMaths/blob/c2dbb59e13b3cce451b86e600345361b34e8c5ba/docs/ARCHITECTURE.md); [`docs/OPERATIONS.md`](https://github.com/genproof/QuickMaths/blob/c2dbb59e13b3cce451b86e600345361b34e8c5ba/docs/OPERATIONS.md); [`docs/METHOD.md`](https://github.com/genproof/QuickMaths/blob/c2dbb59e13b3cce451b86e600345361b34e8c5ba/docs/METHOD.md)

## Operational model

Proof lineages and parallel contracted lanes directly produce the mathematical transformation. ARCHITECT also owns concrete inter-lane interface corrections, while fleet-wide current policy and manager-level judgment are separated from deterministic enforcement. The documented manager is part of the supported campaign operating mode; external evaluator/model internals and repository development are not evidence donors.

## S1 — Operations

- State: A
- Function: Transform a mathematical problem or contracted proof lane into proof artifacts through successive agent choices and compiler observations.
- Disturbance / variety regulated: Open proof holes, library availability, compiler errors, failed tactics, quota limits and continued work.
- Decisive decision or feedback right: Choose mathematical steps, edits, searches and next proof tactics within the supplied problem/lane contract.
- Decision owner: Model-driven proving agent in the concrete first-party prepared job/role composition.
- Supporting / enforcement mechanisms: Pinned external Claude Code executes model rounds; first-party agent_runner, Landlock boundary, ./lean broker, snapshots, role briefs, budgets and continuation sustain them.
- Closure path: Prepared job/brief launches the pinned CLI with workspace tools; ./lean returns build/search/inspect observations; later edits/rounds consume those observations and retained notes/artifacts. Official verification alone controls final acceptance.
- Boundary reachability: controller prepares and starts the packaged runtime; feeder attaches actual role briefs to assignments. This credits the shipped proving composition, without borrowing unrelated Claude Code functions.
- Why this is / is not agent-owned: Removing the model-driven prover leaves supervision and compilation but no choice of proof construction or repair.
- Evidence: [`fleet/server/controller.py`](https://github.com/genproof/QuickMaths/blob/c2dbb59e13b3cce451b86e600345361b34e8c5ba/fleet/server/controller.py); [`runtime/leaneval/jobs.py`](https://github.com/genproof/QuickMaths/blob/c2dbb59e13b3cce451b86e600345361b34e8c5ba/runtime/leaneval/jobs.py); [`runtime/leaneval/agent_runner.py`](https://github.com/genproof/QuickMaths/blob/c2dbb59e13b3cce451b86e600345361b34e8c5ba/runtime/leaneval/agent_runner.py); [`runtime/leaneval/worker.py`](https://github.com/genproof/QuickMaths/blob/c2dbb59e13b3cce451b86e600345361b34e8c5ba/runtime/leaneval/worker.py); [`fleet/server/briefs/COMMON.md`](https://github.com/genproof/QuickMaths/blob/c2dbb59e13b3cce451b86e600345361b34e8c5ba/fleet/server/briefs/COMMON.md)
- Basis: structural
- Confidence: high
- Caveats: No model, host fleet, Lean workbench or benchmark score was executed/verified in this assessment.

## S2 — Coordination

- State: A
- Function: Regulate conflicting interfaces and duplicate shared machinery among concurrent proof-lane S1 cells.
- Disturbance / variety regulated: A consumer needs a stronger producer statement, a lane refutes a shared assumption, or consumers independently re-derive incompatible shared machinery.
- Decisive decision or feedback right: Architect grants/refuses interface requests, revises producing/consuming contracts and preserves only still-valid finished lanes.
- Decision owner: The model-driven ARCHITECT/REARCHITECT agent at the lane-program coordination boundary.
- Supporting / enforcement mechanisms: Lane write confinement, InterfaceRequests/refutation extraction, validated reductions/sanity statements, bounded rearchitecture, merged overlays and redispatch enforce and transport the chosen response. Fleet de-duplication is an additional deterministic path, not the agent owner.
- Closure path: LANE writes a concrete request/refutation; feeder collects it and supplies findings to a later architect; architect chooses corrected statements; validated architecture becomes the new base and subsequent lane assignments use those contracts.
- Boundary reachability: feeder update_program/program_assignment wire the shipped role briefs and findings into actual model rounds, then replace active lane state after validation. This is a supported operating path, not contributor dogfood.
- Why this is / is not agent-owned: Deterministic code can detect/reforward a mismatch, but cannot choose the corrected mathematical interface or grant/refuse the request without the architect.
- Distinct S1 units: Concurrent producer and consumer LANE proof work cells, each with a separate proof outcome and directory.
- Inter-S1 disturbance: Consumer requirements exceed producer contracts or a refuted interface invalidates dependent lanes; concrete request/refutation fields and source tests expose this collision.
- Attenuating coordination relation: Shared interface contracts, one shared-tool producer, request-to-architect revision and invalidation of dependent completed claims.
- Feedback into subsequent S1 behaviour: Corrected architecture replaces lane statements and subsequent dispatched/restarted work uses the new base; invalid consumers cannot remain done.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The return changes a specific producer–consumer interface conflict rather than merely assigning tasks or transporting results.
- Evidence: [`fleet/server/briefs/roles/ARCHITECT.md`](https://github.com/genproof/QuickMaths/blob/c2dbb59e13b3cce451b86e600345361b34e8c5ba/fleet/server/briefs/roles/ARCHITECT.md); [`fleet/server/briefs/roles/LANE.md`](https://github.com/genproof/QuickMaths/blob/c2dbb59e13b3cce451b86e600345361b34e8c5ba/fleet/server/briefs/roles/LANE.md); [`fleet/server/briefs/roles/REARCHITECT.md`](https://github.com/genproof/QuickMaths/blob/c2dbb59e13b3cce451b86e600345361b34e8c5ba/fleet/server/briefs/roles/REARCHITECT.md); [`fleet/server/feeder.py`](https://github.com/genproof/QuickMaths/blob/c2dbb59e13b3cce451b86e600345361b34e8c5ba/fleet/server/feeder.py); [`fleet/tests/test_feeder.py`](https://github.com/genproof/QuickMaths/blob/c2dbb59e13b3cce451b86e600345361b34e8c5ba/fleet/tests/test_feeder.py)
- Basis: structural
- Confidence: high
- Caveats: Rearchitecture is bounded and may wait for running lanes to end; it does not prove every fleet conflict is handled autonomously.

## S3 — Inside-and-now control

- State: C(P)
- Function: Regulate current campaign commitments, placement, continuation, competing routes and scarce account/runner resources.
- Disturbance / variety regulated: Quota-exhausted work alongside idle usable accounts, duplicated programs, stalled lineages and unsuitable placements.
- Decisive decision or feedback right: Select/revise fleet policies and current interventions: hold/release, stop, hand off, split, hedge or rearchitect on behalf of the campaign.
- Decision owner: Base C: a developer must compose the discretionary autonomous campaign controller over the specific current-view/plan/inbox/operator interfaces. Parent P: the legitimate campaign experiment manager/operator owns those choices.
- Supporting / enforcement mechanisms: Deterministic coordinator.plan/execute, feeder scheduling, inbox outcomes, locks, controlled STOP and quota gates enforce selected constraints; their fixed rules are not autonomous organizational judgment.
- Closure path: Gathered fleet status and lane/claim evidence inform manager decisions; --apply/inbox and operator commands change holds, claims, seeds or program architecture; feeder readback and later assignments enact the decision.
- Boundary reachability: Deployment docs explicitly expose fleet status, coordinator apply and leh op to the experiment manager. Unlike a generic kill switch, these are campaign-specific current-control interfaces. No automatically running agent manager is shipped.
- Why this is / is not agent-owned: With the manager removed, configured rules still enforce preselected policy but do not independently revise campaign priorities. A possible supervised agent session does not establish autonomous ownership of the reserved manager decisions.
- Whole-system current view: Coordinator gathers hosts, accounts, live lineages, passes, targets, programs and prior directive outcomes; manager reads campaign status plus residual/quota information.
- Current-control decision scope: Cross-host resource/commitment intervention and campaign/program continuation/route decisions, rather than just one proof tool call.
- Evidence: [`fleet/local/coordinator.py`](https://github.com/genproof/QuickMaths/blob/c2dbb59e13b3cce451b86e600345361b34e8c5ba/fleet/local/coordinator.py); [`fleet/server/feeder.py`](https://github.com/genproof/QuickMaths/blob/c2dbb59e13b3cce451b86e600345361b34e8c5ba/fleet/server/feeder.py); [`fleet/docs/COORDINATOR-POLICY.md`](https://github.com/genproof/QuickMaths/blob/c2dbb59e13b3cce451b86e600345361b34e8c5ba/fleet/docs/COORDINATOR-POLICY.md); [`fleet/operator/README.md`](https://github.com/genproof/QuickMaths/blob/c2dbb59e13b3cce451b86e600345361b34e8c5ba/fleet/operator/README.md); [`docs/EXPERIMENT_MANAGER.md`](https://github.com/genproof/QuickMaths/blob/c2dbb59e13b3cce451b86e600345361b34e8c5ba/docs/EXPERIMENT_MANAGER.md)
- Basis: structural with explicit documented parent procedure
- Confidence: high for P and specific construction surfaces; no A claim
- Caveats: C does not grade deterministic scheduling as agent-owned. Parent authority is local to the operated campaign, not the OSS contributor organization.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | Autonomous chooser/authority still requires composition over campaign-specific current-control interfaces | Live fleet/commitment disturbance | plan/inbox/apply and operator mutations are supplied; autonomous policy discretion is not | [`fleet/local/coordinator.py`](https://github.com/genproof/QuickMaths/blob/c2dbb59e13b3cce451b86e600345361b34e8c5ba/fleet/local/coordinator.py); [`fleet/server/feeder.py`](https://github.com/genproof/QuickMaths/blob/c2dbb59e13b3cce451b86e600345361b34e8c5ba/fleet/server/feeder.py) |
| Parent (`P`) | Campaign experiment manager/operator | Quota, nonconvergence or competing work visible in fleet status | Manager selects intervention; operator/inbox mutates campaign state; feeder applies/readbacks and later work changes | [`docs/EXPERIMENT_MANAGER.md`](https://github.com/genproof/QuickMaths/blob/c2dbb59e13b3cce451b86e600345361b34e8c5ba/docs/EXPERIMENT_MANAGER.md); [`fleet/operator/README.md`](https://github.com/genproof/QuickMaths/blob/c2dbb59e13b3cce451b86e600345361b34e8c5ba/fleet/operator/README.md) |


## S3* — Complementary audit

- State: C
- Function: Complement ordinary progress claims with direct proof-graph/statement inspection of a nonconverging program.
- Disturbance / variety regulated: Self-reported RESIDUALS estimates can shrink through renaming while actual holes remain; false/vacuous lane assumptions can invalidate apparent progress.
- Decisive decision or feedback right: Judge mismatch between agent progress claims and direct Lean declaration/statement reality, then require corrective intervention.
- Decision owner: A separately composed experiment-manager auditor; the first-party audit-specific procedure and evidence/control path are supplied, but autonomous auditor execution/authority is not automatically wired.
- Supporting / enforcement mechanisms: leh map builds the merged tree and extracts actual reached/sorry-dependent declarations/refutations; operator tools expose artifacts/notes and rearchitect/stop updates. Lean execution and JSON summaries are evidence machinery, not the audit-judgment owner.
- Closure path: METHOD §9 requires periodic map-versus-RESIDUALS comparison; the manager stop-and-audit procedure inspects statement truth/source strength and routes findings into rearchitecture/hedges or corrected program briefs through leh op. The direct map is advisory until that actor acts.
- Boundary reachability: The installed leh map and deployed operator tools are linked by the supported manager method. It is an intentionally exposed campaign-audit construction, distinct from repository AUDIT.md or mandatory official acceptance.
- Why this is / is not agent-owned: The map exposes materially different facts, but does not itself decide or implement the audit judgment; the supervised manager/agent setup remains to be composed for autonomous closure.
- Claim being audited: Reported progress/completion and validity/usefulness of lane statements.
- Ordinary reporting path: NOTES RESIDUALS/HANDOFF, lane done state and feeder convergence summaries.
- Complementary access path: Build the merged proof tree, walk actual Lean declaration reachability/sorry/refutation dependencies, inspect published proof and concrete statement counterexamples.
- Independence boundary: Manager does not prove the lanes; direct graph/statement access is outside self-reported estimates. Official verifier alone is not treated as S3*.
- Who acts on findings: Experiment manager selects corrective stop/rearchitecture/hedge; operator tools return findings to architect and subsequent lane rounds.
- Evidence: [`docs/METHOD.md`](https://github.com/genproof/QuickMaths/blob/c2dbb59e13b3cce451b86e600345361b34e8c5ba/docs/METHOD.md); [`docs/EXPERIMENT_MANAGER.md`](https://github.com/genproof/QuickMaths/blob/c2dbb59e13b3cce451b86e600345361b34e8c5ba/docs/EXPERIMENT_MANAGER.md); [`src/harness/map/build.py`](https://github.com/genproof/QuickMaths/blob/c2dbb59e13b3cce451b86e600345361b34e8c5ba/src/harness/map/build.py); [`src/harness/map/summary.py`](https://github.com/genproof/QuickMaths/blob/c2dbb59e13b3cce451b86e600345361b34e8c5ba/src/harness/map/summary.py); [`fleet/operator/rearchitect.py`](https://github.com/genproof/QuickMaths/blob/c2dbb59e13b3cce451b86e600345361b34e8c5ba/fleet/operator/rearchitect.py)
- Basis: structural
- Confidence: medium-high
- Caveats: No autonomous always-on auditor is claimed, and this assessment did not run Lean graph extraction. Human-owned audit is not published as P in this Methodology.

## S4 — Outside-and-then intelligence

- State: P
- Function: Develop the campaign capability repertoire from external mathematical/library opportunities under experiment-manager direction.
- Disturbance / variety regulated: Upcoming proof ingredients absent from current workbench versus existing licensed formalizations, changed/problematic benchmark statements and future evaluation feasibility.
- Decisive decision or feedback right: Choose external reusable sources or revised methods to bring into the proving capability, with human acceptance and rollout.
- Decision owner: The legitimate campaign experiment manager; documentation explicitly says a person decides/applies adaptation. A supervised operator agent can assist without establishing autonomous adaptation authority.
- Supporting / enforcement mechanisms: Manager literature/web recon and evolve reports support option development; bank add pins/license-checks sources, deploy distributes accepted briefs/policies, and worker search exposes admitted bank entries.
- Closure path: Manager compares current convergence/capability gaps with published sources and future campaign needs, chooses reuse/admission or method change, adds pinned formalizations to the durable workbench bank or commits/redeploys approved changes; later architects/lanes search/use them and report reuse. Subsequent reports compare effects.
- Boundary reachability: METHOD §§6,8,10 and manager instructions explicitly connect external recon to the bank/briefs; bank.py and worker.py implement the returned capability change. Evolve alone, being retrospective internal analysis, would not establish S4.
- Why this is / is not agent-owned: Model proof search and deterministic proposal reports cannot independently approve/admit campaign adaptation; the documented manager remains the decisive parent.
- External distinction: Relevant published mathematics/formalizations, benchmark issue information and organizer resource envelope beyond the current proof workspace.
- Future / prospective distinction: Whether forthcoming campaign/lane work should reuse new ingredients or change method rather than repeat unsupported construction; durable bank admission changes the repertoire of later rounds.
- Adaptation option generated: Acquire a licensed pinned formalization as a reusable tool source, revise role briefs/gates, or retain the current capability after comparison.
- Path back into current capability / S3: Manager bank admission makes new sources searchable by the running runtime; accepted policy/brief changes are tested/deployed and used by later fleet assignments.
- Evidence: [`docs/METHOD.md`](https://github.com/genproof/QuickMaths/blob/c2dbb59e13b3cce451b86e600345361b34e8c5ba/docs/METHOD.md); [`docs/EXPERIMENT_MANAGER.md`](https://github.com/genproof/QuickMaths/blob/c2dbb59e13b3cce451b86e600345361b34e8c5ba/docs/EXPERIMENT_MANAGER.md); [`docs/EVOLVE.md`](https://github.com/genproof/QuickMaths/blob/c2dbb59e13b3cce451b86e600345361b34e8c5ba/docs/EVOLVE.md); [`runtime/tools/bank.py`](https://github.com/genproof/QuickMaths/blob/c2dbb59e13b3cce451b86e600345361b34e8c5ba/runtime/tools/bank.py); [`runtime/leaneval/worker.py`](https://github.com/genproof/QuickMaths/blob/c2dbb59e13b3cce451b86e600345361b34e8c5ba/runtime/leaneval/worker.py); [`fleet/server/briefs/roles/ARCHITECT.md`](https://github.com/genproof/QuickMaths/blob/c2dbb59e13b3cce451b86e600345361b34e8c5ba/fleet/server/briefs/roles/ARCHITECT.md)
- Basis: explicit documented operating procedure plus structural return path
- Confidence: medium-high
- Caveats: A search for a present proof ingredient alone is S1; credit is limited to the documented manager capability-acquisition/rollout loop. No campaign transcript, measured adaptation benefit or autonomous Director is claimed.

## S5 — Policy and identity

- State: —
- Function: Standing safety/source/acceptance rules and a person deciding submission/publication constrain the campaign; no runtime identity/ultimate-policy issue process with legitimate authoritative return is supplied. Experiment-manager current control and approved method updates do not automatically become S5.
- Disturbance / variety regulated: No distinct function-specific regulation established at this boundary.
- Decisive decision or feedback right: None supplied for this organizational function.
- Decision owner: No first-party function owner established.
- Supporting / enforcement mechanisms: Static source/credential/acceptance constraints, profile.toml licensing rules, reviewed evolution commits and publish/trust decisions; none establishes a distinct identity-policy deliberation/escalation loop.
- Closure path: No function-specific returned regulation; the operational mechanisms remain as described.
- Why this is / is not agent-owned: The reviewed mechanisms do not establish the function before ownership classification.
- Evidence: [`docs/EXPERIMENT_MANAGER.md`](https://github.com/genproof/QuickMaths/blob/c2dbb59e13b3cce451b86e600345361b34e8c5ba/docs/EXPERIMENT_MANAGER.md); [`docs/EVOLVE.md`](https://github.com/genproof/QuickMaths/blob/c2dbb59e13b3cce451b86e600345361b34e8c5ba/docs/EVOLVE.md); [`docs/CONFIGURATION.md`](https://github.com/genproof/QuickMaths/blob/c2dbb59e13b3cce451b86e600345361b34e8c5ba/docs/CONFIGURATION.md); [`runtime/leaneval/resources/profile.toml`](https://github.com/genproof/QuickMaths/blob/c2dbb59e13b3cce451b86e600345361b34e8c5ba/runtime/leaneval/resources/profile.toml); [`fleet/local/publish.py`](https://github.com/genproof/QuickMaths/blob/c2dbb59e13b3cce451b86e600345361b34e8c5ba/fleet/local/publish.py)
- Basis: structural
- Confidence: high within the declared boundary
- Caveats: Bounded absence in the reviewed distribution, not impossibility of future composition.

### Absence scope

- Surfaces inspected: README, complete operating/method/manager/configuration docs, role briefs, CLI, fleet policy/operator and evolution/bank paths.
- Plausible first-party paths checked: Static source/credential/acceptance constraints, profile.toml licensing rules, reviewed evolution commits and publish/trust decisions; none establishes a distinct identity-policy deliberation/escalation loop.
- Why no material first-party path remains: Standing safety/source/acceptance rules and a person deciding submission/publication constrain the campaign; no runtime identity/ultimate-policy issue process with legitimate authoritative return is supplied. Experiment-manager current control and approved method updates do not automatically become S5.

## Recursion

A lead/lane/program hierarchy is visible, but lane spawning, role names and nested proof decomposition do not demonstrate independently viable recursive organizations.

## Variety and escalation

Proof agents absorb tactic/compiler variety locally. Contracts and write confinement attenuate cross-lane interference; exact requests/refutations amplify concrete conflicts to the architect. Quota/directive/hold readbacks expose fleet disturbances to the manager. Credential alerts have a specified operator response, without implying a new S-function.

## Evidence gaps

Offline source witnesses passed: 22 coordinator, 100 feeder and 9 operator unittest cases (131 total), using temporary fake host/program layouts. These exercise routing, interface/refutation handling and returned state, not model judgment, real SSH/fleet operation or Lean acceptance. No 30GB workbench, token, private campaign repository, external publication or leaderboard verification was accessed. P/C claims describe supported wiring/procedure, not measured campaign success.

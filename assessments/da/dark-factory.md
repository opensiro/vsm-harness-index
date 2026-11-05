---
harness_id: dark-factory
project_name: Dark factory
repository: https://github.com/ruslantrachuk/dark-factory
review_ref: a56142f7e79efdfa9aa8acee7596974b4efea174
reviewed_at: 2026-11-05
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: A
autonomy_s4: P
autonomy_s5: P
---

# Dark factory

## Review boundary

- System in focus: the installed first-party software-delivery factory for a project: declared agent roles/workflows plus opt-in queue/fleet and module-management paths.
- Purpose and identity: deliver requested, reviewed project changes while reserving acceptance and the factory's delegation policy to the project owner.
- Relevant environment: customer/project requirements, repository reality, concurrent branches, a growing contributor/client/production environment, model host, subscription limits and code-host services.
- Standard-distribution boundary: installed dark-factory plugin, its executable Workflow compositions, agents/skills, hooks and selected shipped project modules; a working Claude Code Workflow host, beads, GitHub and declared project tests are dependencies.
- Credited operating / distribution surfaces: feature-auto/core/lite workflows and builder/reviewer roles; standard hooks; provisioned-project queue triage; level and add module commands in supported operator mode. Optional paths are credited only with their stated prerequisites.
- Adjacent first-party surfaces excluded from ownership: repository-development openspec work, test/dryrun fake agents, release CI for the plugin itself, analytics examples and unequipped placeholder deployments. Third-party host internals donate no uninspected function.
- First-party operating / deployment modes considered: attended session and unattended feature pipeline (session and parallel-wave variants), optional Linux provisioned project with queue review, and operator-selected module/fence changes. Seatbelt-only installation alone does not establish the stronger configured paths.
- Recursion level: one configured project's delivery organization, not every external app it delivers, the Claude service or the author's entire private fleet.
- Reviewed revision: `a56142f7e79efdfa9aa8acee7596974b4efea174`.
- Observation date: 2026-11-05.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The MIT repository packages an installable plugin. `plugins/dark-factory/workflows/README.md` and the feature-pipeline manifest wire named workflows to the host Workflow tool. `feature-auto.js` prepares a worktree, obtains a plan and invokes the core/lite builder composition. `feature-core.js` implements graph waves, pairwise file disjointness, a single integration writer, fresh read-only reviewer calls and a fix return. Builder/reviewer definitions carry explicit roles and preloaded stage skills; source-defined prompts/schemas and returned workflow state make this a concrete delivery composition rather than a bare wrapper around an external worker.

`hooks/hooks.json` activates guard, quota and level hooks in opted-in projects. `scripts/fleet.py` provisions optional local sessions/timers; `scripts/triage.py` gathers whole-project commitments, obtains a read-only proposal and returns the owner's selection through concrete bd close/defer operations. `scripts/level.py` reports environmental/structural signals and validates a bounded human prompt grant for governance-fence changes. The add skill plus `add-module.sh` installs and configures shipped capabilities with tests/status checks. Production monitoring, vulnerability remediation and telemetry were inspected as shipped optional paths; customer-product repair is not confused with adaptation of the delivery factory.

## Operational model

Builder cells turn scoped requirements into committed, tested changes. In pipeline mode several builders operate on disjoint files; one integrator serializes their accumulated branch. Reviewer roles inspect raw code in a separate context. The human owns current commitment retirement in queue review, selection of structural capability changes and the ultimate delegation/review fence. Fixed budgets, parsers, queues and hooks support those decisions. This assessment does not attribute native Claude Code functions to the plugin merely because it invokes that host.

## S1 — Operations

- State: A
- Function: deliver project changes and bounded correction.
- Disturbance / variety regulated: underspecified implementation details, code/test failures and returned findings.
- Decisive decision or feedback right: choose implementation, tests and bounded fixes within the approved request.
- Decision owner: first-party builder role instantiated by the installed delivery workflow.
- Supporting / enforcement mechanisms: external host/model, source-defined role and skills, scoped worktree/tools, schemas, tests, commit and task-state scripts.
- Closure path: owned builder prompt → edits/tests/result → integration and review → fix agent or explicit incomplete result → committed branch.
- Boundary reachability: feature command and feature-pipeline manifest invoke shipped named workflows and builder role; no private author runtime is required.
- Why this is / is not agent-owned: workflow scaffolding alone cannot implement arbitrary requirements; the configured builder exercises local coding discretion.
- Evidence: [plugins/dark-factory/workflows/feature-auto.js](https://github.com/ruslantrachuk/dark-factory/blob/a56142f7e79efdfa9aa8acee7596974b4efea174/plugins/dark-factory/workflows/feature-auto.js); [plugins/dark-factory/workflows/feature-core.js](https://github.com/ruslantrachuk/dark-factory/blob/a56142f7e79efdfa9aa8acee7596974b4efea174/plugins/dark-factory/workflows/feature-core.js); [plugins/dark-factory/agents/builder.md](https://github.com/ruslantrachuk/dark-factory/blob/a56142f7e79efdfa9aa8acee7596974b4efea174/plugins/dark-factory/agents/builder.md); [plugins/dark-factory/templates/feature-pipeline/MANIFEST.md](https://github.com/ruslantrachuk/dark-factory/blob/a56142f7e79efdfa9aa8acee7596974b4efea174/plugins/dark-factory/templates/feature-pipeline/MANIFEST.md).
- Basis: structural.
- Confidence: high for source wiring; not an empirical outcome claim.
- Caveats: Requires the documented host/toolchain and project setup; seatbelt-only mode has no such complete delivery loop.

## S2 — Coordination

- State: C
- Function: attenuate concurrent builder edits and conflicts with unmerged work.
- Distinct S1 units: separate feature/subtask builder cells in parallel-wave mode.
- Inter-S1 disturbance: two cells write the same planned code file or concurrently commit the shared working tree.
- Attenuating coordination relation: pairwiseDisjoint forces overlapping waves to run sequentially; disjoint workers do not commit, and a single integrator commits the wave. feature-auto also returns overlaps in-flight branch before build.
- Feedback into subsequent S1 behaviour: overlap changes execution from parallel to serial, or stops a feature until the branch is merged/restarted; each later wave observes integrated predecessor state.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the dispatch decision explicitly tests the actual shared-file collision surface and constrains subsequent writes/commits.
- Disturbance / variety regulated: concrete cross-builder file/commit interference.
- Decisive decision or feedback right: select the prescribed safe wave/stop response to intersecting file scopes.
- Decision owner: developer-authored collision rule and configured override; the overlap agent gathers intersections rather than owning discretionary organizational settlement.
- Supporting / enforcement mechanisms: task graph, file sets, sequential/parallel executor, worktree and integrator role.
- Closure path: planned file intersection → serialize/stop → constrained later builder operation.
- Boundary reachability: the installed feature-core pipeline mode intentionally exposes this function-specific path; session mode is a single writer.
- Why this is / is not agent-owned: the fixed rule is not autonomous coordination discretion; a function-specific path exists, but autonomous coordination authority must still be composed.
- Evidence: [plugins/dark-factory/workflows/feature-core.js](https://github.com/ruslantrachuk/dark-factory/blob/a56142f7e79efdfa9aa8acee7596974b4efea174/plugins/dark-factory/workflows/feature-core.js); [plugins/dark-factory/workflows/feature-auto.js](https://github.com/ruslantrachuk/dark-factory/blob/a56142f7e79efdfa9aa8acee7596974b4efea174/plugins/dark-factory/workflows/feature-auto.js); [plugins/dark-factory/workflows/README.md](https://github.com/ruslantrachuk/dark-factory/blob/a56142f7e79efdfa9aa8acee7596974b4efea174/plugins/dark-factory/workflows/README.md).
- Basis: structural.
- Confidence: high for source wiring; not an empirical outcome claim.
- Caveats: C is limited to evidenced file/commit interference, not semantic coordination or generic task sequencing.

## S3 — Inside-and-now control

- State: P
- Function: regulate the project's current outstanding commitments on behalf of the whole.
- Whole-system current view: triage facts/report account for open and in-progress tasks, stale work, main-branch completion evidence, queue limit and fresh tasks excluded from detailed review.
- Current-control decision scope: retire obsolete/completed/unsupported commitments or defer work; retain exceptions selected by the project owner.
- Disturbance / variety regulated: unbounded accumulated task commitments and stale work competing with present delivery.
- Decisive decision or feedback right: choose which proposed close/defer actions become authoritative.
- Decision owner: legitimate local project owner answering the Remote Control queue-review session.
- Supporting / enforcement mechanisms: timer/fleet, read-only product-owner model proposal, numbered report/TTL, choose parser and bd CLI.
- Closure path: project queue facts → proposal/report to owner → yes/except/number selection → triage.py apply executes only selected close/defer decisions → later queue-driven work changes.
- Boundary reachability: fleet provisions the first-party triage path for a project with bd; the same shipped script opens the owner-visible session and implements apply.
- Why this is / is not agent-owned: the model recommends; no commitment is closed without the owner's returned answer. Static agent/credit caps are enforcement, not an additional A S3 mode.
- Evidence: [plugins/dark-factory/scripts/triage.py](https://github.com/ruslantrachuk/dark-factory/blob/a56142f7e79efdfa9aa8acee7596974b4efea174/plugins/dark-factory/scripts/triage.py); [plugins/dark-factory/scripts/fleet.py](https://github.com/ruslantrachuk/dark-factory/blob/a56142f7e79efdfa9aa8acee7596974b4efea174/plugins/dark-factory/scripts/fleet.py).
- Basis: structural.
- Confidence: high for source wiring; not an empirical outcome claim.
- Caveats: Only the configured local project queue is covered; no claim of autonomous whole-fleet management or cryptographic human authentication.

## S3* — Complementary audit

- State: A
- Function: challenge builder claims of a correct, appropriately tested implementation through complementary source inspection.
- Claim being audited: the builder's completed/tested branch respects requirements, project invariants and test-layer contracts.
- Ordinary reporting path: builder result and green scoped/full gates.
- Complementary access path: fresh reviewer reads the actual branch diff, neighboring source and standards through test/invariant/simplify lenses.
- Independence boundary: separately instantiated read-only reviewer role, separate context, no authority to alter its target or decide merge; it can report defects despite builder/gate success.
- Who acts on findings: a separate fix builder verifies/rejects scoped findings with reasons, edits and reruns gates; unresolved critical findings prevent a clean result.
- Disturbance / variety regulated: self-reporting blind spots, omitted tests, invariant breaches and false clean claims.
- Decisive decision or feedback right: judge evidence-backed findings against raw source and the stated contract.
- Decision owner: fresh first-party reviewer agent; fix/triage authority is separately owned.
- Supporting / enforcement mechanisms: role tools/prompt, finding schemas, severity filtering and workflow outcome gate.
- Closure path: raw diff inspection → structured findings → bounded fix or justified rejection → tests/commit and blockersRemaining/error result.
- Boundary reachability: feature-core invokes shipped reviewer role after build, and passes findings into its shipped Fix stage; the manifest packages this into the supported feature command.
- Why this is / is not agent-owned: the independent audit judgment is model-owned; schema parsing and gates only transport/enforce it.
- Evidence: [plugins/dark-factory/workflows/feature-core.js](https://github.com/ruslantrachuk/dark-factory/blob/a56142f7e79efdfa9aa8acee7596974b4efea174/plugins/dark-factory/workflows/feature-core.js); [plugins/dark-factory/agents/reviewer.md](https://github.com/ruslantrachuk/dark-factory/blob/a56142f7e79efdfa9aa8acee7596974b4efea174/plugins/dark-factory/agents/reviewer.md); [plugins/dark-factory/templates/base/docs/review-contract.md](https://github.com/ruslantrachuk/dark-factory/blob/a56142f7e79efdfa9aa8acee7596974b4efea174/plugins/dark-factory/templates/base/docs/review-contract.md); [plugins/dark-factory/workflows/README.md](https://github.com/ruslantrachuk/dark-factory/blob/a56142f7e79efdfa9aa8acee7596974b4efea174/plugins/dark-factory/workflows/README.md).
- Basis: structural.
- Confidence: high for source wiring; not an empirical outcome claim.
- Caveats: Independence is contextual and role-based, not separate infrastructure or empirical proof of defect detection.

## S4 — Outside-and-then intelligence

- State: P
- Function: adapt the delivery factory's available organizational capability as its project environment changes.
- External distinction: level inspection detects deployment/production configuration and growth to multiple human contributors; module manifests distinguish client production and monitoring requirements.
- Future / prospective distinction: those signals motivate future unattended operation, client support/monitoring or a changed team-control arrangement, rather than another requested product fix.
- Adaptation option generated: level report proposes the next structural step and its consequences; shipped add/provision paths identify concrete capability modules and their prerequisites.
- Path back into current capability / S3: owner invokes the selected add/provision skill; file installation, seam adaptation, tests and status checks make the new module available to subsequent project operation.
- Disturbance / variety regulated: a factory outgrowing its supported operating arrangement as production/client/team demands change.
- Decisive decision or feedback right: select whether and how the proposed structural capability is adopted.
- Decision owner: project owner; the level/add skills explicitly reserve the selection and structural step to that owner.
- Supporting / enforcement mechanisms: level.py signals/report/hint, module manifest, installer, project checks and fleet provisioning.
- Closure path: environmental evidence → report/options to owner → explicit chosen structural command → shipped module installation/configuration/test/status → changed current factory capability.
- Boundary reachability: level SessionStart hint and explicitly invoked level/add commands ship with the plugin; installer copies real modules, not future roadmap placeholders.
- Why this is / is not agent-owned: the parent chooses adaptation; neither deterministic hints nor a model implementing the chosen installation owns the adoption decision.
- Evidence: [plugins/dark-factory/scripts/level.py](https://github.com/ruslantrachuk/dark-factory/blob/a56142f7e79efdfa9aa8acee7596974b4efea174/plugins/dark-factory/scripts/level.py); [plugins/dark-factory/skills/level/SKILL.md](https://github.com/ruslantrachuk/dark-factory/blob/a56142f7e79efdfa9aa8acee7596974b4efea174/plugins/dark-factory/skills/level/SKILL.md); [plugins/dark-factory/skills/add/SKILL.md](https://github.com/ruslantrachuk/dark-factory/blob/a56142f7e79efdfa9aa8acee7596974b4efea174/plugins/dark-factory/skills/add/SKILL.md); [plugins/dark-factory/scripts/add-module.sh](https://github.com/ruslantrachuk/dark-factory/blob/a56142f7e79efdfa9aa8acee7596974b4efea174/plugins/dark-factory/scripts/add-module.sh); [plugins/dark-factory/hooks/hooks.json](https://github.com/ruslantrachuk/dark-factory/blob/a56142f7e79efdfa9aa8acee7596974b4efea174/plugins/dark-factory/hooks/hooks.json).
- Basis: structural.
- Confidence: medium, bounded to the documented operator-led installation/return path.
- Caveats: No autonomous S4 or empirical adaptation outcome is claimed. Vulnerability repair of a customer product and ordinary feature planning remain S1, not the credited S4 witness.

## S5 — Policy and identity

- State: P
- Function: close changes to the delivery factory's ultimate delegation/review policy.
- Identity / ultimate-policy issue: whether the project permits solo/standard/team delivery authority, including mandatory human approval and whether agents may weaken governing fences.
- Ultimate authority in each claimed mode: the local project owner using the explicitly human-invoked level command; no agent-owned alternative is supplied.
- Return-to-operation path: UserPromptSubmit records an exact project/target-bound expiring one-use grant; level.py applies the authorized fence change; guard reads the stricter working/main fence so weakening binds only after integration.
- Disturbance / variety regulated: tension between delivery freedom/unattended work and the project's reserved governance constraints.
- Decisive decision or feedback right: authorize a change to the standing governance fence, rather than approve an individual operational command.
- Decision owner: legitimate project owner; unattended/model-launched attempts cannot create the first-party prompt grant.
- Supporting / enforcement mechanisms: level skill, prompt hook, grant store/TTL, atomic fence update, protected merge path and PreToolUse guard.
- Closure path: policy-change proposal → owner explicitly names target and confirms → exact grant consumed → effective fence changed → later delivery/merge actions governed by returned policy.
- Boundary reachability: level and guard are installed plugin hooks; the explicit level skill is disabled for model invocation and is the documented policy-change route.
- Why this is / is not agent-owned: human authority decides the standing policy. A hook denial, ordinary release acceptance or permission dialog alone is not this S5 witness.
- Evidence: [plugins/dark-factory/skills/level/SKILL.md](https://github.com/ruslantrachuk/dark-factory/blob/a56142f7e79efdfa9aa8acee7596974b4efea174/plugins/dark-factory/skills/level/SKILL.md); [plugins/dark-factory/scripts/level.py](https://github.com/ruslantrachuk/dark-factory/blob/a56142f7e79efdfa9aa8acee7596974b4efea174/plugins/dark-factory/scripts/level.py); [plugins/dark-factory/scripts/guard.py](https://github.com/ruslantrachuk/dark-factory/blob/a56142f7e79efdfa9aa8acee7596974b4efea174/plugins/dark-factory/scripts/guard.py); [plugins/dark-factory/hooks/hooks.json](https://github.com/ruslantrachuk/dark-factory/blob/a56142f7e79efdfa9aa8acee7596974b4efea174/plugins/dark-factory/hooks/hooks.json).
- Basis: structural.
- Confidence: medium-high for the implemented parent policy route.
- Caveats: This is local configured-project ultimate policy, not authority over the host/provider or the OSS organization. Hooks are explicitly not a complete security sandbox.

## Distributed OSS parent arrangement

The assessed parent is the configured project's operator. Public contributors and the author's private factory are not treated as a shared ultimate authority.

## Self-hosted and non-human modes

Parent S3 requires provisioned queue review; S4/S5 require the explicit operator paths. Plain Workflow session/pipeline modes supply builder and reviewer autonomy. No composite A(P)/C(P) state is inferred because no autonomous S3/S4/S5 base is established.

## Recursion

A workflow calling another workflow and spawning builders is decomposition, not proof of recursive viable systems. The external product and host remain separate boundaries.

## Variety and escalation

File collisions, findings, quota, stale work and changed deployment conditions reach different owners. Incomplete error/overlap states are returned with evidence; they are not automatically algedonic signals. Out-of-scope product changes remain reserved to the owner.

## Evidence gaps

Source-backed supported-mode assessment, not a live customer deployment. Model/host/bd/GitHub/toolchain prerequisites were not installed or exercised against paid providers. Stub dryruns can check branch mechanics but cannot establish model judgment, real human response or operational efficacy.


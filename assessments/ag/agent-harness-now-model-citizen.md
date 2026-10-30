---
harness_id: agent-harness-now-model-citizen
project_name: Agent Harness (now Model Citizen)
repository: https://github.com/JakeSelby/model-citizen
review_ref: af9693b97480c7b801c57c43863b116f4116808c
reviewed_at: 2026-10-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: C
autonomy_s4: P
autonomy_s5: —
---

# Agent Harness (now Model Citizen)

## Review boundary

- System in focus: the pinned Agent Harness installed role/workflow/policy organization and constrained worker runner hosted by compatible Claude Code/Codex clients.
- Purpose and identity: apply shared user-aligned procedures and bounded roles to research, planning, implementation and review, with common policy projections.
- Relevant environment: user issues/plans, repositories/worktrees/artifacts, native client/model services, provider model-catalog changes and concurrent task cells.
- Standard-distribution boundary: primitives role/workflow/skill authority; bin/harness; lib/harness_core; policy/hooks and native adapters/projections. The current repository is renamed Model Citizen, but the pinned project calls itself Agent Harness.
- Credited operating / distribution surfaces: shipped operational role/workflow instructions, workers.py with actual adapter launch/result handling, lifecycle policies, worktree helper and model-tier inspection/configuration path.
- Adjacent first-party surfaces excluded from ownership: this repository's own AGENTS.md development/release organization, BMad authored product-planning outputs, compatibility test fixtures and future hosted-agent plans. Native host internal functions, external frameworks/viewers and model internals are not donated.
- First-party operating / deployment modes considered: installed shared Claude/Codex projections; constrained read-only/planner role workers; build/review workflows; worktree-per-agent isolation; native hook controls; operator tier checking/remapping. No global install/sync/trust or native agent execution performed in this assessment.
- Recursion level: one installed user work organization with bounded research/build/review cells. Repository-maintenance governance is a separate recursion.
- Reviewed revision: `JakeSelby/model-citizen@af9693b97480c7b801c57c43863b116f4116808c`, frozen intake #2412 / controller #2413.
- Observation date: 2026-10-30.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

[README.md](https://github.com/JakeSelby/model-citizen/blob/af9693b97480c7b801c57c43863b116f4116808c/README.md) separates shared primitives/policy from native clients. [lib/harness_core/workers.py](https://github.com/JakeSelby/model-citizen/blob/af9693b97480c7b801c57c43863b116f4116808c/lib/harness_core/workers.py) resolves committed role/stance contracts, launches an isolated native process through a specific adapter, validates its result and atomically publishes bounded planner artifacts. Native engines provide inference/tool execution; the first-party role contracts and return protocol supply the credited work organization. [primitives/workflows/build.md](https://github.com/JakeSelby/model-citizen/blob/af9693b97480c7b801c57c43863b116f4116808c/primitives/workflows/build.md) binds a builder to an issue/worktree and requires the caller's own verification before publication. [primitives/workflows/review.md](https://github.com/JakeSelby/model-citizen/blob/af9693b97480c7b801c57c43863b116f4116808c/primitives/workflows/review.md) separates fresh scope and quality reviews of raw diffs. [lib/harness_core/lifecycle.py](https://github.com/JakeSelby/model-citizen/blob/af9693b97480c7b801c57c43863b116f4116808c/lib/harness_core/lifecycle.py) projects deterministic hook decisions, not universal agent ownership. Model-tier checking compares current bindings with provider cache entries and exposes missing/superseded/rank conflicts.

## Operational model

The supported installed composition contains first-party instructed task actors and concrete launch/return paths; it is more than a prompt dump or generic CLI proxy. S1=A is limited to that composition, not a bare config generator, and does not import arbitrary native-host functions. Worktree policy/helper provides specific coordination support. Optional independent raw-artifact review provides an audit constructor path, without claiming automatically closed audit control for every task. The installation operator retains the documented model-lineup adaptation choice.

## S1 — Operations

- State: A
- Function: produce bounded research/planning/implementation results through first-party shared operational roles/workflows.
- Disturbance / variety regulated: unfamiliar project source, issue requirements, intermediate implementation failures and missing evidence.
- Decisive decision or feedback right: choose task-local investigation/implementation actions and synthesize the required report or plan within the role contract.
- Decision owner: the model-driven actor running the supplied gatherer/planner/builder contract; the caller retains publication/approval decisions.
- Supporting / enforcement mechanisms: native model/tool engine, explicit role/stance instruction assembly, isolated worker configuration, result parsing/size limits, plan validator and artifact publication.
- Closure path: bounded brief/source inputs → native actor under first-party role instructions → returned result/report → caller verification or validated new plan artifact; ordinary build fixes follow gate feedback.
- Boundary reachability: workers.run assembles committed role contracts and adapter command, executes it and consumes the result; installed build/research/plan workflows and documented harness role run expose these modes. No custom downstream role/controller is required.
- Why this is / is not agent-owned: the native host supplies generic execution; the packaged role actor still chooses semantic task actions/results. Removing that actor leaves no investigation or implementation result.
- Evidence: [lib/harness_core/workers.py](https://github.com/JakeSelby/model-citizen/blob/af9693b97480c7b801c57c43863b116f4116808c/lib/harness_core/workers.py); [adapters/claude-code/worker.py](https://github.com/JakeSelby/model-citizen/blob/af9693b97480c7b801c57c43863b116f4116808c/adapters/claude-code/worker.py); [adapters/codex/worker.py](https://github.com/JakeSelby/model-citizen/blob/af9693b97480c7b801c57c43863b116f4116808c/adapters/codex/worker.py); [primitives/roles/builder.md](https://github.com/JakeSelby/model-citizen/blob/af9693b97480c7b801c57c43863b116f4116808c/primitives/roles/builder.md); [docs/role-workers.md](https://github.com/JakeSelby/model-citizen/blob/af9693b97480c7b801c57c43863b116f4116808c/docs/role-workers.md)
- Basis: structural
- Confidence: medium
- Caveats: native qualification is explicitly unqualified at this pin. This is a conditional supported-client structural path, not verified cross-version confinement, actual model execution or certification.

## S2 — Coordination

- State: C
- Function: attenuate concurrent task-cell edits to a shared checkout and resulting lost/overlapping changes.
- Distinct S1 units: separate builder/implementation task cells working on different issues in the same repository.
- Inter-S1 disturbance: simultaneous edits to one working tree/shared generated or append-only files can overwrite or conflict with sibling changes.
- Attenuating coordination relation: worktree-per-agent policy plus dedicated-root worktree create/audit/remove helper; scoped builder briefs, single-threaded writes and explicit warnings for shared documents/generated files.
- Feedback into subsequent S1 behaviour: builders return worktree/branch/commit and deviations; callers verify/land through repository workflow, while later worktrees fetch the accepted base. Audit/removal rejects dirty or unreferenced state rather than silently discarding it.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the skill explicitly identifies shared-checkout races and binds implementation cells to separate branches/worktrees; this is disturbance-specific isolation and integration support.
- Disturbance / variety regulated: cross-cell workspace mutation and merge interference.
- Decisive decision or feedback right: assign isolated workspaces and reconcile task changes into accepted base without losing sibling work.
- Decision owner: the supplied policy/helper specifies isolation; caller/agent must compose the actual concurrent assignment and reconciliation discipline.
- Supporting / enforcement mechanisms: git worktree commands, repository markers, path checks and dirty-state refusal.
- Closure path: separate worktree allocation → bounded builder edits/report → caller gate/PR integration → future work starts from fetched accepted main.
- Boundary reachability: builder role invokes bundled worktree-per-agent instructions and bin/harness cmd_worktree implements the primitive in the normal installed distribution.
- Why this is / is not agent-owned: A is not inferred from running git commands; the complete autonomous cross-cell reconciliation owner is not established by these fixed primitives alone.
- Evidence: [primitives/skills/worktree-per-agent/SKILL.md](https://github.com/JakeSelby/model-citizen/blob/af9693b97480c7b801c57c43863b116f4116808c/primitives/skills/worktree-per-agent/SKILL.md); [primitives/roles/builder.md](https://github.com/JakeSelby/model-citizen/blob/af9693b97480c7b801c57c43863b116f4116808c/primitives/roles/builder.md); [bin/harness](https://github.com/JakeSelby/model-citizen/blob/af9693b97480c7b801c57c43863b116f4116808c/bin/harness); [tests/test_worktree.py](https://github.com/JakeSelby/model-citizen/blob/af9693b97480c7b801c57c43863b116f4116808c/tests/test_worktree.py)
- Basis: structural
- Confidence: medium
- Caveats: shared append-only/generated files still need explicit integration discipline; isolation is not proof of conflict-free delivery.

## S3 — Inside-and-now control

- State: —
- Function: No additional whole-system inside-and-now regulator established.
- Disturbance / variety regulated: Parent task delegation, caller gate rerun, usage feeds, cost/fan-out posture, stop gates and ordinary human permissions were checked.
- Decisive decision or feedback right: no qualifying function-specific loop established.
- Decision owner: users select preferences; task actors retain bounded operational decisions.
- Supporting / enforcement mechanisms: primitives/workflows/build.md, primitives/rules/delegation.md, primitives/stances/cost/balanced.md, docs/runtime-controls.md
- Closure path: The build caller verifies one issue's production result; fixed cost/effort/fan-out preferences and usage reports constrain tasks. They do not by themselves expose a discretionary whole-organization resource/priority/intervention loop or a complete distinct parent mode. Do not promote task assignment or deterministic enforcement into S3.
- Why this is / is not agent-owned: instructions, monitoring and enforcement do not inherit a missing organizational decision.
- Evidence: [primitives/workflows/build.md](https://github.com/JakeSelby/model-citizen/blob/af9693b97480c7b801c57c43863b116f4116808c/primitives/workflows/build.md); [primitives/rules/delegation.md](https://github.com/JakeSelby/model-citizen/blob/af9693b97480c7b801c57c43863b116f4116808c/primitives/rules/delegation.md); [primitives/stances/cost/balanced.md](https://github.com/JakeSelby/model-citizen/blob/af9693b97480c7b801c57c43863b116f4116808c/primitives/stances/cost/balanced.md); [docs/runtime-controls.md](https://github.com/JakeSelby/model-citizen/blob/af9693b97480c7b801c57c43863b116f4116808c/docs/runtime-controls.md)
- Basis: structural
- Confidence: medium
- Caveats: source-relative supported-mode finding, not a claim of universal impossibility.

### Absence scope

- Surfaces inspected: primitives/workflows/build.md, primitives/rules/delegation.md, primitives/stances/cost/balanced.md, docs/runtime-controls.md, README/runtime-controls/role-worker documentation and relevant unit tests.
- Plausible first-party paths checked: Parent task delegation, caller gate rerun, usage feeds, cost/fan-out posture, stop gates and ordinary human permissions were checked.
- Why no material first-party path remains: The build caller verifies one issue's production result; fixed cost/effort/fan-out preferences and usage reports constrain tasks. They do not by themselves expose a discretionary whole-organization resource/priority/intervention loop or a complete distinct parent mode. Do not promote task assignment or deterministic enforcement into S3.

## S3* — Complementary audit

- State: C
- Function: provide complementary fresh-context challenge of operational scope/correctness claims using direct artifacts.
- Claim being audited: a branch/implementation satisfies its requested scope and its reports/verification claims are justified.
- Ordinary reporting path: builder returns commit, changed files, gate tail, deviations and claimed checks to its caller.
- Complementary access path: separate spec-reviewer and reviewer read the raw diff, specification and changed source directly; the caller rechecks findings against code.
- Independence boundary: contexts that did not perform the implementation; separate scope pass before quality pass; read-only constrained-role worker path is supplied. Native confinement remains subject to actual client qualification.
- Who acts on findings: the invoking caller/user selects corrective control and may route findings into build; that full integration must still be composed.
- Disturbance / variety regulated: self-reported completeness, hidden scope changes and incorrect evidence/verification claims.
- Decisive decision or feedback right: make an independent evidence-backed finding that can challenge the ordinary builder report.
- Decision owner: supplied reviewer roles expose the audit judgment path; consumer must compose verified runtime independence and consequential return/control for a concrete deployment.
- Supporting / enforcement mechanisms: fresh role context, explicit diff/spec inputs, isolated read-only worker adapters and findings-only result shape.
- Closure path: review artifacts → independent findings → caller code recheck → actionable scope/quality report; corrective build/acceptance policy remains with the consumer. No automatic A closure is claimed.
- Boundary reachability: review is a bundled callable workflow referencing packaged reviewer contracts; constrained role launches route through workers.py rather than an undocumented future auditor plugin.
- Why this is / is not agent-owned: the audit-specific primitive is established beyond a component name, but complete independent corrective organization is not guaranteed merely by generating a role file or passing unit tests.
- Evidence: [primitives/workflows/review.md](https://github.com/JakeSelby/model-citizen/blob/af9693b97480c7b801c57c43863b116f4116808c/primitives/workflows/review.md); [primitives/roles/reviewer.md](https://github.com/JakeSelby/model-citizen/blob/af9693b97480c7b801c57c43863b116f4116808c/primitives/roles/reviewer.md); [primitives/roles/spec-reviewer.md](https://github.com/JakeSelby/model-citizen/blob/af9693b97480c7b801c57c43863b116f4116808c/primitives/roles/spec-reviewer.md); [lib/harness_core/workers.py](https://github.com/JakeSelby/model-citizen/blob/af9693b97480c7b801c57c43863b116f4116808c/lib/harness_core/workers.py); [docs/role-workers.md](https://github.com/JakeSelby/model-citizen/blob/af9693b97480c7b801c57c43863b116f4116808c/docs/role-workers.md)
- Basis: structural
- Confidence: medium
- Caveats: ordinary design-loop scoring, stop-gate tests and mandatory QA are not separately credited as S3*. C rests on the distinct raw-diff/spec challenge path and its explicit independence/return surface, not the word reviewer.

## S4 — Outside-and-then intelligence

- State: P
- Function: adapt the installed role-to-model capability mapping as the external provider lineup changes.
- External distinction: provider model catalog entries identify disappeared models, named upgrade successors and priority ordering relative to current classes.
- Future / prospective distinction: a still-resolving versioned model can already be superseded; continued future work on old/wrong class mappings would silently retain obsolete capability assumptions.
- Adaptation option generated: reported successor/removal/rank conflicts expose concrete replacement/remapping choices for the operator's role classes.
- Path back into current capability / S3: operator compares findings with current role/class bindings, edits documented tiers or role_bindings, then syncs definitions or launches constrained workers; resolver consumes the returned mapping and workers record selected model/effort.
- Disturbance / variety regulated: changing model availability/capability and stale class assumptions.
- Decisive decision or feedback right: select a replacement class-to-model mapping and authorize its use across roles.
- Decision owner: the legitimate local installation user/operator; checker reports options/problems and does not autonomously choose a new model.
- Supporting / enforcement mechanisms: harness tiers check, tier_findings, native provider cache, validated user overrides, sync projection and worker resolution.
- Closure path: external catalog → check against current mapping → parent chooses remapping → role resolution/projection uses it for subsequent operations → checker/worker posture records permit checking the resulting mapping.
- Boundary reachability: cmd_tiers and catalog.tier_findings are implemented; docs/role-workers explicitly describes user tier/role_bindings remapping when the lineup turns over, and workers.resolution consumes those same values.
- Why this is / is not agent-owned: parent keeps the adaptation judgment; automatic lookup/validation is support. No autonomous A or independent C base mode is asserted.
- Evidence: [bin/harness](https://github.com/JakeSelby/model-citizen/blob/af9693b97480c7b801c57c43863b116f4116808c/bin/harness); [lib/harness_core/catalog.py](https://github.com/JakeSelby/model-citizen/blob/af9693b97480c7b801c57c43863b116f4116808c/lib/harness_core/catalog.py); [lib/harness_core/workers.py](https://github.com/JakeSelby/model-citizen/blob/af9693b97480c7b801c57c43863b116f4116808c/lib/harness_core/workers.py); [docs/role-workers.md](https://github.com/JakeSelby/model-citizen/blob/af9693b97480c7b801c57c43863b116f4116808c/docs/role-workers.md); [tests/test_primitive_catalog.py](https://github.com/JakeSelby/model-citizen/blob/af9693b97480c7b801c57c43863b116f4116808c/tests/test_primitive_catalog.py)
- Basis: structural
- Confidence: medium
- Caveats: bounded model-lineup adaptation mode only; offline cache freshness, comparative model quality and actual upgraded native execution were not measured. Generic memory, instructions or self-authoring are not the S4 witness.

## S5 — Policy and identity

- State: —
- Function: No runtime identity/ultimate-policy closure established.
- Disturbance / variety regulated: User preference/stance authoring, permission confirmation, licensing posture, shared primitive authority and upstream maintainer governance were checked.
- Decisive decision or feedback right: no qualifying function-specific loop established.
- Decision owner: users select preferences; task actors retain bounded operational decisions.
- Supporting / enforcement mechanisms: primitives/skills/harness-authoring/SKILL.md, lib/harness_core/lifecycle.py, docs/preferences.md, README.md
- Closure path: Authoring changes instructions/settings under explicit user requests and repository process; hooks enforce selected policies. No identity-level unresolved matter has a supplied ultimate-authority deliberation and returned runtime governance loop. Preference switching and ordinary approvals are not automatically S5.
- Why this is / is not agent-owned: instructions, monitoring and enforcement do not inherit a missing organizational decision.
- Evidence: [primitives/skills/harness-authoring/SKILL.md](https://github.com/JakeSelby/model-citizen/blob/af9693b97480c7b801c57c43863b116f4116808c/primitives/skills/harness-authoring/SKILL.md); [lib/harness_core/lifecycle.py](https://github.com/JakeSelby/model-citizen/blob/af9693b97480c7b801c57c43863b116f4116808c/lib/harness_core/lifecycle.py); [docs/preferences.md](https://github.com/JakeSelby/model-citizen/blob/af9693b97480c7b801c57c43863b116f4116808c/docs/preferences.md); [README.md](https://github.com/JakeSelby/model-citizen/blob/af9693b97480c7b801c57c43863b116f4116808c/README.md)
- Basis: structural
- Confidence: medium
- Caveats: source-relative supported-mode finding, not a claim of universal impossibility.

### Absence scope

- Surfaces inspected: primitives/skills/harness-authoring/SKILL.md, lib/harness_core/lifecycle.py, docs/preferences.md, README.md, README/runtime-controls/role-worker documentation and relevant unit tests.
- Plausible first-party paths checked: User preference/stance authoring, permission confirmation, licensing posture, shared primitive authority and upstream maintainer governance were checked.
- Why no material first-party path remains: Authoring changes instructions/settings under explicit user requests and repository process; hooks enforce selected policies. No identity-level unresolved matter has a supplied ultimate-authority deliberation and returned runtime governance loop. Preference switching and ordinary approvals are not automatically S5.

## Distributed OSS parent arrangement

S4=P is local installation-user authority over model-capability adaptation, not upstream project governance. The source repository's own AGENTS/release/BMad organization was inspected as adjacent evidence and is not borrowed into user installations.

## Self-hosted and non-human modes

Shared installed projections and isolated worker commands are first-party supported compositions on external native clients. Missing/unqualified native behavior is disclosed; no host-internal S-functions or undeployed hosted-agent roadmap is credited.

## Recursion

Role/workflow nesting establishes bounded task cells and a caller/worker relationship, not complete recursively viable organizations.

## Variety and escalation

Brief scope, read-only/artifact authority, bounded result size, timeout, gate feedback and orphan-status detection regulate local variety. Pending actions return to the caller; ordinary errors/reports are not automatically algedonic channels.

## Evidence gaps

Pinned source and documented modes reviewed. Native deterministic suite: 1,151 tests PASS in 104.724s; lint 0 findings; generated projection check PASS. Tests use fake/mocked native workers and do not establish actual CLI/model execution or native qualification. No global configuration install/sync/trust, external agent E2E or model/provider calls were executed. Positive claims remain bounded structural mappings, with S3* explicitly constructor-level.

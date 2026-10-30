---
harness_id: multi-agents-control-plane
project_name: Multi-Agents Control Plane
repository: https://github.com/QiQi14/multi-agents-control-plane
review_ref: 4483c54037ed04c8b5f7f2ac65aca7604d6c58e8
reviewed_at: 2026-10-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: C
autonomy_s2: —
autonomy_s3: P
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: P
---

# Multi-Agents Control Plane

## Review boundary

- System in focus: the installed `.ai/` task-contract control plane in one software repository, its configured external AI coding-tool adapters, task state/receipt workflow and legitimate project maintainer.
- Purpose and identity: constrain and coordinate model-assisted software work through project-specific contracts, source-bound implementation evidence, separate read-only QA and human merge decisions.
- Relevant environment: repository state/diffs, implementation requirements, coding agents launched externally, verification commands, risk tiers, maintainers and changing tool availability.
- Standard-distribution boundary: stdlib-Python `ai` CLI, `scripts/ai_plane/` tasks/prompts/routing/auto_dispatch, task-evidence schema, verification/risk-gating, generated adapters and first-party installer. No resident model runtime or agent service ships.
- Credited operating / distribution surfaces: `scripts/ai_plane/{tasks,prompts,auto_dispatch,route,task_evidence,sync}.py`, `scripts/verify_contract.py`, `scripts/ai_cli.py`, installed task/adapter manifests and first-party `install.py`.
- Adjacent first-party surfaces excluded from ownership: repo's own contributor/CI workflow, `scripts/tests/`, static HTML reader, documentation images, illustrative sample task, Rust extension when not explicitly enabled, external Codex/Claude/Gemini execution internals and any user's private agent workers.
- First-party operating / deployment modes considered: default manual prompt handoff, opt-in configured `--auto` exec/deeplink dispatch, explicit reviewer prompt/QA receipt, owner risk gate and local repository sync. Automatic dispatch requires a user-provided tool descriptor and remains disabled by default.
- Recursion level: a project-level software-work orchestration cell whose candidate S1s are external model coding tasks constructed/connected by this first-party control plane; no assumption that the installed wrapper itself is a model agent.
- Reviewed revision: `QiQi14/multi-agents-control-plane@4483c54037ed04c8b5f7f2ac65aca7604d6c58e8` (batch #2393, row 4).
- Observation date: 2026-10-30.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

The source is pinned to the [immutable reviewed tree](https://github.com/QiQi14/multi-agents-control-plane/tree/4483c54037ed04c8b5f7f2ac65aca7604d6c58e8). No external model session was run during this assessment.

## Repository architecture

The [README](https://github.com/QiQi14/multi-agents-control-plane/blob/4483c54037ed04c8b5f7f2ac65aca7604d6c58e8/README.md) states that the product installs a stdlib Python task-state plane and generated agent adapters, not a model service. The [dispatch command](https://github.com/QiQi14/multi-agents-control-plane/blob/4483c54037ed04c8b5f7f2ac65aca7604d6c58e8/scripts/ai_plane/prompts.py) creates tool-specific prompt files; if explicitly configured and invoked with `--auto`, [auto dispatch](https://github.com/QiQi14/multi-agents-control-plane/blob/4483c54037ed04c8b5f7f2ac65aca7604d6c58e8/scripts/ai_plane/auto_dispatch.py) launches a selected external executable or deeplink. Otherwise the human takes the prompt to a separate coding agent. The first-party wrapper supplies a *specific constructor path* to an agentic operational unit but the actual model worker/tool execution belongs to the composed external tool. It must not be credited as already auto-running in default mode.

Task contracts and [role prompts](https://github.com/QiQi14/multi-agents-control-plane/blob/4483c54037ed04c8b5f7f2ac65aca7604d6c58e8/scripts/ai_plane/prompts.py) separate strategist/planner/executor/reviewer roles. The [QA receipt schema](https://github.com/QiQi14/multi-agents-control-plane/blob/4483c54037ed04c8b5f7f2ac65aca7604d6c58e8/scripts/ai_plane/task_evidence.py) preserves actor, revision, decision, gates and evidence references, while the [merge gate](https://github.com/QiQi14/multi-agents-control-plane/blob/4483c54037ed04c8b5f7f2ac65aca7604d6c58e8/scripts/ai_plane/tasks.py) requires an accepting QA decision and, at high risk, explicit owner approval. It prints that the gate passed but does **not** itself merge to Git; project maintainer/CI owns the external repository merge. A receipt's claimed reviewer identity is not itself proof a genuinely independent reviewer was executed.

## Operational model

An owner defines a task including scope, forbidden paths, risk and tool assignments. `ai dispatch` composes the executor prompt with task contract and required evidence. Either the parent hands it off manually or the opt-in launcher starts a configured external agent tool. The external coding agent then makes code changes and writes its executor receipt. A separate `ai review` prompt asks a different read-only actor to inspect the task and exact revision/diff and write a QA receipt. Versioned evidence is checked; `ai merge` checks acceptance/closeout and high-risk approval but leaves the actual Git merge outside the wrapper. `ai sync` propagates owner-maintained `.ai/` policy into tool-specific instructions for later executions.

The decisive rights must be separated: the external model owns local code choices if it was actually launched; deterministic CLI owns parsing/validation; the parent owns task assignment, risk acceptance and ultimate project policy. Documentation claims about cross-family reviewer checks are bounded by what local source demonstrably enforces; no autonomous independent auditor is presumed from labels.

## S1 — Operations

- State: C
- Function: a contract-bounded AI coding task is an operational cell when connected to an actual external coding agent.
- Disturbance / variety regulated: implementation details, changing repository code, failing tests, scope requirements and tool feedback.
- Decisive decision or feedback right: choose which code and tests to create/change within the authorized task area, and return an implementation result.
- Decision owner: configured external model coding agent in the composed run; no first-party model execution loop in this repository.
- Supporting / enforcement mechanisms: generated executor prompt and adapter, tool-assignment taxonomy, opt-in subprocess/deeplink launcher, task contract and receipt schema.
- Closure path: owner task contract → `ai dispatch` prompt → external agent tool executes under composed authority → changed repository files and executor receipt → later QA and project decision.
- Boundary reachability: first-party `cmd_dispatch` builds a concrete per-tool prompt, and opt-in `perform_auto_dispatch` can launch a declared executable or deeplink. Default settings do not launch; developer/owner must compose an actual model tool and delegation authority.
- Why this is / is not agent-owned: the installed control plane has no autonomous model task loop; first-party S1-specific adapter construction is real, but ownership only closes through an external agent/tool configuration, hence C rather than A.
- Evidence: [dispatch/render code](https://github.com/QiQi14/multi-agents-control-plane/blob/4483c54037ed04c8b5f7f2ac65aca7604d6c58e8/scripts/ai_plane/prompts.py), [auto dispatch](https://github.com/QiQi14/multi-agents-control-plane/blob/4483c54037ed04c8b5f7f2ac65aca7604d6c58e8/scripts/ai_plane/auto_dispatch.py), [CLI commands](https://github.com/QiQi14/multi-agents-control-plane/blob/4483c54037ed04c8b5f7f2ac65aca7604d6c58e8/scripts/ai_cli.py).
- Basis: bounded S1 constructor, not autonomous default runtime.
- Confidence: high for constructor status; no live external-agent evidence.
- Caveats: task-state commands and static docs alone are not an autonomous agent. Installation, configured external tool and project intent are necessary for a real S1 unit.

## S2 — Coordination

- State: —
- Function: no demonstrated S2-specific cross-agent oscillation/interference attenuation and returned closure among distinct S1 coding cells.
- Disturbance / variety regulated: competing external coding agents may write the same file, duplicate a task or race on verification, but generic workflow sequencing is insufficient.
- Decisive decision or feedback right: no first-party policy responding to a specific inter-S1 collision across simultaneously active tasks is established.
- Decision owner: not established as S2.
- Supporting / enforcement mechanisms: task state graph, declared dependencies/scopes, isolated project worktrees, generated prompts, verification lock and role/risk routing.
- Closure path: scope validation and verification serialization act on an individual task/verification run; no evidenced feedback from a conflict between two operational units that adjusts their subsequent behavior.
- Why this is / is not agent-owned: splitting tasks, assigning models, writing separate worktrees and serializing a verifier are not by themselves S2-specific regulation.
- Evidence: [task state and routing](https://github.com/QiQi14/multi-agents-control-plane/blob/4483c54037ed04c8b5f7f2ac65aca7604d6c58e8/scripts/ai_plane/tasks.py), [scope verification](https://github.com/QiQi14/multi-agents-control-plane/blob/4483c54037ed04c8b5f7f2ac65aca7604d6c58e8/scripts/verify_contract.py), [verification lock doctor](https://github.com/QiQi14/multi-agents-control-plane/blob/4483c54037ed04c8b5f7f2ac65aca7604d6c58e8/scripts/ai_plane/doctor.py).
- Basis: negative state under specific S2 witness threshold.
- Confidence: moderate.
- Caveats: external agent tools and project processes may negotiate file conflicts; these are not shipped operational closures of this wrapper.

### Absence scope

- Surfaces inspected: task state machine, task-graph dependencies, scope verifier, worktree installation, dispatch/review prompts, routing, verification lock and tests.
- Plausible first-party paths checked: simultaneous task scope collision detection, live active-agent contention resolution, reallocation after conflict and feedback into two running S1 coding units.
- Why no material first-party path remains: the shipped mechanism prepares tasks and verifies one diff, but does not establish a conflict-specific coordination response that closes across distinct live S1 units; parent scheduling and external agent coordination remain outside its operating loop.

## S3 — Inside-and-now control

- State: P
- Function: whole-project parent control of current task scope, model assignment, risk gate and merge readiness.
- Disturbance / variety regulated: active task priorities, unauthorized diff expansion, incompatible risk/evidence decisions and execution-resource allocation.
- Whole-system current view: repository `.ai/tasks` states, current task assignments, dependency graph, accepted or rejected QA receipts and evidence/verification status.
- Current-control decision scope: parent sets task contracts, allowed scopes, assigned tool/reviewer, risk and explicit approval for high-risk merge.
- Decisive decision or feedback right: choose what may execute and what may proceed to repository merge under current constraints.
- Decision owner: legitimate project maintainer/operator in standard mode, with CLI validators enforcing fixed selected constraints; no first-party agent exercises whole-project S3 current control autonomously.
- Supporting / enforcement mechanisms: `cmd_task_show`, task routing taxonomy, scope verification, QA/closeout gates, immutable receipts and risk rules.
- Closure path: parent defines task/risk/assignments → handoff prompt and verifier use the contract → QA acceptance plus owner `--approved` where required → parent executes normal Git merge or returns revision to executor.
- Boundary reachability: installed CLI reads persisted task contracts and QA receipts, gates merge readiness and generates executable handoff prompts; a human is needed to make the actual authority choice/merge.
- Why this is / is not agent-owned: deterministic tool recommendation and checkers do not own the chosen priority/risk/merge decision; parent explicitly retains it.
- Evidence: [task merge gate](https://github.com/QiQi14/multi-agents-control-plane/blob/4483c54037ed04c8b5f7f2ac65aca7604d6c58e8/scripts/ai_plane/tasks.py), [routing and conflict reporting](https://github.com/QiQi14/multi-agents-control-plane/blob/4483c54037ed04c8b5f7f2ac65aca7604d6c58e8/scripts/ai_plane/route.py), [verification contract](https://github.com/QiQi14/multi-agents-control-plane/blob/4483c54037ed04c8b5f7f2ac65aca7604d6c58e8/scripts/verify_contract.py).
- Basis: real parent decision right and return to bounded execution.
- Confidence: high for parent-owned mode.
- Caveats: a task manager or human final click alone does not prove S3; the whole-project contract/priority/risk surface and returned gate are the credited path.

## S3* — Complementary audit

- State: C
- Function: construct a separate read-only reviewer path to challenge executor claims against actual repository diff, task acceptance and supporting evidence.
- Disturbance / variety regulated: executor may claim completion without source/test evidence, mutate forbidden files or omit regressions.
- Claim being audited: executor's assertion that its bounded implementation satisfies task contract and acceptance tests.
- Ordinary reporting path: executor receipt and implementation summary.
- Complementary access path: reviewer prompt explicitly requests the *exact diff/revision*, contract and separate read-only inspection, then typed QA decision and evidence references.
- Independence boundary: reviewer role has no implementation authority and is a distinct configured tool identity; for high risk routing can recommend cross-model-family independence, but an actual independent reviewer is external/manual and not verified merely by a receipt string.
- Who acts on findings: human owner and subsequent executor; `ai merge` refuses non-accepting QA receipts and `task-closeout`/evidence violations.
- Decisive decision or feedback right: independently judge accept/revise/reject against source evidence, not merely replay the executor's routine status.
- Decision owner: separate externally executed reviewer, to be composed and verified by the project owner; first-party CLI does not autonomously render the audit verdict.
- Supporting / enforcement mechanisms: `ai review` prompt, `receipt.qa.yaml` schema, revision/diff fingerprint, model family metadata, `ai merge` QA gate and immutable-round policy.
- Closure path: separate reviewer reads diff → writes QA receipt → owner/gate accepts or routes `revise`/`reject` to next executor attempt; actual reviewer execution must be supplied.
- Boundary reachability: the CLI ships `cmd_review` and versioned QA schema/merge gate for installed projects; this is an S3*-specific constructor, not only an example or README assertion.
- Why this is / is not agent-owned: independent reviewer agent could own the audit judgment after composition, but no out-of-box autonomous reviewer execution or guaranteed separation is proved; classify C, not A.
- Evidence: [review prompt generation](https://github.com/QiQi14/multi-agents-control-plane/blob/4483c54037ed04c8b5f7f2ac65aca7604d6c58e8/scripts/ai_plane/prompts.py), [versioned QA schema](https://github.com/QiQi14/multi-agents-control-plane/blob/4483c54037ed04c8b5f7f2ac65aca7604d6c58e8/scripts/ai_plane/task_evidence.py), [merge gate](https://github.com/QiQi14/multi-agents-control-plane/blob/4483c54037ed04c8b5f7f2ac65aca7604d6c58e8/scripts/ai_plane/tasks.py), [cross-family routing](https://github.com/QiQi14/multi-agents-control-plane/blob/4483c54037ed04c8b5f7f2ac65aca7604d6c58e8/scripts/ai_plane/route.py).
- Basis: source-bound distinct audit constructor and return, not generic unit tests.
- Confidence: moderate-high for C.
- Caveats: QA receipt parsing cannot independently attest that a claimed reviewer or model family truly ran; human owner must execute and verify the separate actor.

## S4 — Outside-and-then intelligence

- State: —
- Function: no materially closed prospective external environment modeling and adaptation feedback path at the chosen installed project boundary.
- Disturbance / variety regulated: changes to model tools, dependencies, organizational requirements and future technical options could demand adaptation.
- Decisive decision or feedback right: no standard deployed autonomous/parent-closed mechanism to turn environmental sensing into prospective capability options and S3 changes.
- Decision owner: not established for S4.
- Supporting / enforcement mechanisms: named strategist role, tool availability detection, task complexity routing, project intelligence source indexing and developer-maintained extensions.
- Closure path: none for external-and-prospective intelligence; current tool routing and documentation indexing do not form S4.
- Why this is / is not agent-owned: a strategist prompt without an executed external prospective model and returned capability decision is not an S4 function.
- Evidence: [routing code](https://github.com/QiQi14/multi-agents-control-plane/blob/4483c54037ed04c8b5f7f2ac65aca7604d6c58e8/scripts/ai_plane/route.py), [project intelligence](https://github.com/QiQi14/multi-agents-control-plane/tree/4483c54037ed04c8b5f7f2ac65aca7604d6c58e8/scripts/ai_plane/knowledge_projection), [README strategist role](https://github.com/QiQi14/multi-agents-control-plane/blob/4483c54037ed04c8b5f7f2ac65aca7604d6c58e8/README.md).
- Basis: scoped negative conclusion; no universal impossibility assertion.
- Confidence: moderate.
- Caveats: a project's external strategist agent may implement S4 after composition, but the reviewed first-party plane only prepares instructions.

### Absence scope

- Surfaces inspected: strategist/plan prompts, routing, tool detection, code indexing, task graph, CLI and extensions/verification.
- Plausible first-party paths checked: future external opportunity/threat sense, prospective option generation and returned project-level changes to current capabilities.
- Why no material first-party path remains: source indexes current project state and chooses current executor/tool profiles, but does not ship a closed environmental futures→options→S3 capability regulation loop.

## S5 — Policy and identity

- State: P
- Function: project owner preserves ultimate work-policy identity through canonical `.ai/` configuration, immutable task contracts and generated agent instructions.
- Disturbance / variety regulated: incompatible goals, scope expansion, tool policy changes and threats to project identity or risk tolerance.
- Identity / ultimate-policy issue: which canonical project rules and task authority limits all future AI contributors must respect, and who may legitimately amend those rules.
- Ultimate authority in each claimed mode: legitimate repository/project maintainer; deterministic `.ai` policy registry and generated adapters transmit that choice but have no independent ultimate-policy discretion.
- Return-to-operation path: parent changes canonical `.ai/` project policy/skills/config → `ai sync` creates guarded adapters/manifests → future external agent prompts use those instructions and contract gates constrain subsequent work.
- Decisive decision or feedback right: define/revise ultimate project operating policy, not just approve an implementation diff.
- Decision owner: human/project parent with repository modification/merge authority.
- Supporting / enforcement mechanisms: `.ai/config.yaml`, canonical skills/rules registry, generated adapter synchronization, hash manifest, task contract and risk gate.
- Closure path: legitimate parent policy update → canonical registry → deterministic rendering → next agent handoff and verification; parent still owns actual project Git changes.
- Boundary reachability: the installed `ai sync` and prompt assembly consume canonical `.ai` sources for supported external tool adapters, not merely docs or CI.
- Why this is / is not agent-owned: a static policy file alone would not prove S5; here an operational parent edit/propagation path exists, while no agent owns the ultimate identity decision.
- Evidence: [adapter sync](https://github.com/QiQi14/multi-agents-control-plane/blob/4483c54037ed04c8b5f7f2ac65aca7604d6c58e8/scripts/ai_plane/sync.py), [config loader](https://github.com/QiQi14/multi-agents-control-plane/blob/4483c54037ed04c8b5f7f2ac65aca7604d6c58e8/scripts/ai_plane/config.py), [prompt construction](https://github.com/QiQi14/multi-agents-control-plane/blob/4483c54037ed04c8b5f7f2ac65aca7604d6c58e8/scripts/ai_plane/prompts.py), [README authority](https://github.com/QiQi14/multi-agents-control-plane/blob/4483c54037ed04c8b5f7f2ac65aca7604d6c58e8/README.md).
- Basis: bounded parent policy-to-next-run return.
- Confidence: moderate.
- Caveats: normal high-risk merge approval is S3 current control, not the sole basis for S5.

## Distributed OSS parent arrangement

The public repository distributes an installable tool. Its upstream maintainers do not thereby control every downstream project installing it; only the installing project's actual authorized owner supplies S3/S5 parent closure. Independent external agents using their own private sessions are not counted as a shared upstream multi-agent organization.

## Self-hosted and non-human modes

No daemon/provider backed autonomous executor is bundled. An operator can use manual handoff or opt into a configured external executable/deeplink; this keeps S1 constructor-level in the general distribution. Separate QA is also an active constructor path but requires an actually independent external reviewer. An entirely agent-governed project may be composed using these tools, but it is not shipped as an autonomous S3/S4/S5 mode.

## Recursion

Task contracts are not automatically viable subsystems; an external executor may hold local autonomy after launch, while project-level scope/risk/identity decisions are parent-owned. Separately named strategist/planner/reviewer roles express intended authority isolation but do not by themselves demonstrate independent nested viable organizations.

## Variety and escalation

Task scope and evidence gates attenuate implementation and proof variety before an owner merges changes. High-risk issues escalate to human approval; QA verdicts return to next implementation attempts. The state and receipt store supports reproducible review, but model execution and independent judgment are performed by composed external tool actors, not the deterministic CLI itself.

## Evidence gaps

- No autonomous model worker is packaged; manually dispatched prompts are not evidence that a model executed or owned the task.
- The `--auto` path executes a user-provided descriptor; no preconfigured default launch or provider-backed live run is credited.
- Review prompts and QA receipts support a complementary audit constructor; they do not independently prove a different model family, actor isolation or actual source-first review occurred.
- No demonstrated cross-task S2 conflict dampening beyond generic scope/dependencies/verification locks; no S4 environmental futures loop.
- A parent-maintained `.ai/` policy and generated adapter return were observed; this is not an autonomous S5 claim or a human-approval-means-S5 shortcut.

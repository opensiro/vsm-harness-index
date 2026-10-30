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
status: excluded-no-agentic-vsm
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Multi-Agents Control Plane

**Canonical disposition:** `excluded-no-agentic-vsm` for frozen Index batch #2393, row 4. The standalone proposal documented a first-party **constructor** for externally run agents (`S1=C`) and read-only review prompts (`S3*=C`), but the Index inclusion gate requires a first-party **autonomous operational S1 (`S1=A`)**. The canonical no-agentic-VSM vector does not deny the utility of this deterministic control plane; it excludes external coding tools, human review and their unverified autonomy from the system's own decision owners. No model/provider-backed execution was performed.

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

- State: —
- Function: a contract-bounded AI coding task is an operational cell when connected to an actual external coding agent.
- Disturbance / variety regulated: implementation details, changing repository code, failing tests, scope requirements and tool feedback.
- Decisive decision or feedback right: choose which code and tests to create/change within the authorized task area, and return an implementation result.
- Decision owner: configured external model coding agent in the composed run; no first-party model execution loop in this repository.
- Supporting / enforcement mechanisms: generated executor prompt and adapter, tool-assignment taxonomy, opt-in subprocess/deeplink launcher, task contract and receipt schema.
- Closure path: owner task contract → `ai dispatch` prompt → optionally configured **external** agent tool runs → changed product files/executor receipt → QA and parent decision. The first-party code does not execute an autonomous decision loop itself.
- Boundary reachability: no positive first-party autonomous state claimed. `cmd_dispatch` builds a prompt and opt-in `perform_auto_dispatch` launches an externally supplied tool, which is excluded as an independent operational decision owner.
- Why this is / is not agent-owned: installed control plane has no model-controlled task-turn/tool-result loop. Constructor support, including optional external-tool launch, does not by itself satisfy the canonical included `S1=A` threshold.
- Evidence: [dispatch/render code](https://github.com/QiQi14/multi-agents-control-plane/blob/4483c54037ed04c8b5f7f2ac65aca7604d6c58e8/scripts/ai_plane/prompts.py), [auto dispatch](https://github.com/QiQi14/multi-agents-control-plane/blob/4483c54037ed04c8b5f7f2ac65aca7604d6c58e8/scripts/ai_plane/auto_dispatch.py), [CLI commands](https://github.com/QiQi14/multi-agents-control-plane/blob/4483c54037ed04c8b5f7f2ac65aca7604d6c58e8/scripts/ai_cli.py).
- Basis: source-bound absence of an autonomous first-party S1; constructor potential was described in the integrated proposal #2400.
- Confidence: high for constructor status; no live external-agent evidence.
- Caveats: task-state commands and static docs alone are not an autonomous agent. Installation, configured external tool and project intent are necessary for a real S1 unit.

### Absence scope

- Surfaces inspected: stdlib CLI, `cmd_dispatch`, auto-launch/deeplink, adapter generation, external-tool descriptors, task events and integration/unit tests.
- Plausible first-party paths checked: manual dispatch, configured auto-exec, generated executor prompts and QA receipts, CLI task transitions, and external coding-host integrations.
- Why no material first-party path remains: the only model-agent decision loop belongs to an external Codex/Claude/Gemini-like executable or its human operator; first-party Python code creates artifacts or invokes that tool and never owns autonomous task/tool decisions. At this defined boundary there is no S1=A capable of admission.

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

- State: —
- Function: parent task/risk choices and merge-readiness checks exist, but no whole-system S3 regulation of **first-party autonomous S1 operations** closes at the included-harness boundary.
- Disturbance / variety regulated: active task priorities, unauthorized diff expansion, incompatible risk/evidence decisions and execution-resource allocation.
- Whole-system current view: the local inventory of *externally delegated* tasks, assignments, dependency graph and receipts is a useful control record, not evidence of an internally operating autonomous agent fleet.
- Current-control decision scope: human parent sets task scopes and merge approvals for its external repository work.
- Decisive decision or feedback right: choose what may execute and what may proceed to repository merge under current constraints.
- Decision owner: external project maintainer, not an agentic owner within a qualifying first-party VSM organization.
- Supporting / enforcement mechanisms: `cmd_task_show`, task routing taxonomy, scope verification, QA/closeout gates, immutable receipts and risk rules.
- Closure path: operator decisions and deterministic gates condition external agents and external Git merge, but no first-party autonomous S1 receives an internally owned project-wide current-control decision.
- Boundary reachability: no positive first-party S3 state claimed; installed CLI gates external work and reports merge readiness without owning the coding operations.
- Why this is / is not agent-owned: deterministic routing and QA parsing are not a project-wide agent S3 decision; the owner remains external.
- Evidence: [task merge gate](https://github.com/QiQi14/multi-agents-control-plane/blob/4483c54037ed04c8b5f7f2ac65aca7604d6c58e8/scripts/ai_plane/tasks.py), [routing and conflict reporting](https://github.com/QiQi14/multi-agents-control-plane/blob/4483c54037ed04c8b5f7f2ac65aca7604d6c58e8/scripts/ai_plane/route.py), [verification contract](https://github.com/QiQi14/multi-agents-control-plane/blob/4483c54037ed04c8b5f7f2ac65aca7604d6c58e8/scripts/verify_contract.py).
- Basis: external parent management is described but not promoted to S3 publication for an excluded no-S1 boundary.
- Confidence: high for parent-owned mode.
- Caveats: an integrating project can obtain human-owned current management over external agents, but that does not change the first-party S1 absence finding.

### Absence scope

- Surfaces inspected: task inventory, routing/assignment rules, contract parser, scope checker, QA gate and merge command.
- Plausible first-party paths checked: autonomous agent-manager interventions over current operational work, budget/commitment arbitration and returned changes to internal S1 cells.
- Why no material first-party path remains: current-control decisions are supplied by external owner; code merely applies preselected task/risk settings to externally executed agents, with no qualifying first-party autonomous operations to govern.

## S3* — Complementary audit

- State: —
- Function: construct a separate read-only reviewer path to challenge executor claims against actual repository diff, task acceptance and supporting evidence.
- Disturbance / variety regulated: executor may claim completion without source/test evidence, mutate forbidden files or omit regressions.
- Claim being audited: executor's assertion that its bounded implementation satisfies task contract and acceptance tests.
- Ordinary reporting path: executor receipt and implementation summary.
- Complementary access path: reviewer prompt explicitly requests the *exact diff/revision*, contract and separate read-only inspection, then typed QA decision and evidence references.
- Independence boundary: reviewer role has no implementation authority and is a distinct configured tool identity; for high risk routing can recommend cross-model-family independence, but an actual independent reviewer is external/manual and not verified merely by a receipt string.
- Who acts on findings: human owner and subsequent executor; `ai merge` refuses non-accepting QA receipts and `task-closeout`/evidence violations.
- Decisive decision or feedback right: an external reviewer could judge accept/revise/reject; no first-party independent reviewer is instantiated.
- Decision owner: separate external reviewer/human if the owner actually invokes one; no first-party autonomous audit owner.
- Supporting / enforcement mechanisms: `ai review` prompt, `receipt.qa.yaml` schema, revision/diff fingerprint, model family metadata, `ai merge` QA gate and immutable-round policy.
- Closure path: if an external reviewer supplies an actual verdict, the CLI can consume its QA receipt; without that external reviewer the schema and gate cannot inspect and judge artifacts independently.
- Boundary reachability: no positive first-party audit state claimed. `cmd_review` writes a prompt and QA schema; actual independent source access/judgment remains outside the shipped boundary.
- Why this is / is not agent-owned: independent reviewer agent could own judgment after user composition, but receipt labels and read-only prompts do not establish that reviewer as a first-party autonomous auditor.
- Evidence: [review prompt generation](https://github.com/QiQi14/multi-agents-control-plane/blob/4483c54037ed04c8b5f7f2ac65aca7604d6c58e8/scripts/ai_plane/prompts.py), [versioned QA schema](https://github.com/QiQi14/multi-agents-control-plane/blob/4483c54037ed04c8b5f7f2ac65aca7604d6c58e8/scripts/ai_plane/task_evidence.py), [merge gate](https://github.com/QiQi14/multi-agents-control-plane/blob/4483c54037ed04c8b5f7f2ac65aca7604d6c58e8/scripts/ai_plane/tasks.py), [cross-family routing](https://github.com/QiQi14/multi-agents-control-plane/blob/4483c54037ed04c8b5f7f2ac65aca7604d6c58e8/scripts/ai_plane/route.py).
- Basis: evidence of an audit *constructor* but absence of first-party independent audit decision closure.
- Confidence: high for external-review dependence.
- Caveats: QA receipt parsing cannot independently attest that a claimed reviewer or model family truly ran; human owner must execute and verify the separate actor.

### Absence scope

- Surfaces inspected: reviewer prompt builder, immutable QA receipt schema, merge gate, cross-family recommendation and tests.
- Plausible first-party paths checked: automatic model reviewer launch, independent access to checked diff, reviewer judgment and closed audit verdict returned to operations.
- Why no material first-party path remains: standard `ai review` generates a handoff file but does not execute a reviewer; a supplied receipt is not proof of independently observed reality, and the required judge/return remains composed outside the first-party runtime.

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

- State: —
- Function: deterministic project policy/instruction propagation exists, but no first-party organizational identity/ultimate-policy decision loop for an internally autonomous operating system is established.
- Disturbance / variety regulated: incompatible goals, scope expansion, tool policy changes and threats to project identity or risk tolerance.
- Identity / ultimate-policy issue: which canonical project rules and task authority limits all future AI contributors must respect, and who may legitimately amend those rules.
- Ultimate authority in each claimed mode: external repository/project maintainer; no S5 positive first-party mode is claimed in this excluded boundary.
- Return-to-operation path: parent changes canonical `.ai/` policy/config → `ai sync` renders instructions for external agent tools. This is a useful outward policy-support mechanism, not internally closed S5 over first-party autonomous operations.
- Decisive decision or feedback right: define/revise ultimate project operating policy, not just approve an implementation diff.
- Decision owner: external human/project parent.
- Supporting / enforcement mechanisms: `.ai/config.yaml`, canonical skills/rules registry, generated adapter synchronization, hash manifest, task contract and risk gate.
- Closure path: parent change reaches deterministic adapter files, then requires an external agent/parent workflow to exercise and close the governing decision.
- Boundary reachability: no positive first-party S5 state claimed; canonical `.ai/` rules reach external tools only through rendered instructions.
- Why this is / is not agent-owned: no internally autonomous agent owns ultimate identity and the parent policy loop is external to the no-S1 control-plane boundary.
- Evidence: [adapter sync](https://github.com/QiQi14/multi-agents-control-plane/blob/4483c54037ed04c8b5f7f2ac65aca7604d6c58e8/scripts/ai_plane/sync.py), [config loader](https://github.com/QiQi14/multi-agents-control-plane/blob/4483c54037ed04c8b5f7f2ac65aca7604d6c58e8/scripts/ai_plane/config.py), [prompt construction](https://github.com/QiQi14/multi-agents-control-plane/blob/4483c54037ed04c8b5f7f2ac65aca7604d6c58e8/scripts/ai_plane/prompts.py), [README authority](https://github.com/QiQi14/multi-agents-control-plane/blob/4483c54037ed04c8b5f7f2ac65aca7604d6c58e8/README.md).
- Basis: bounded parent instruction propagation without qualifying first-party agentic closure.
- Confidence: moderate.
- Caveats: normal high-risk merge approval is S3 current control, not the sole basis for S5.

### Absence scope

- Surfaces inspected: canonical configuration, policy registry, `ai sync`, generated adapters, task contracts and merge-risk controls.
- Plausible first-party paths checked: ultimate policy proposal/decision owner, legitimate return of changed purpose to an internally executing S1 organization and closure after S3/S4 tension.
- Why no material first-party path remains: the CLI renders owner-written instructions for externally executed agents but does not host an autonomous operating organization whose identity-level decisions close inside this first-party system; task risk approval is routine external control.

## Distributed OSS parent arrangement

The public repository distributes an installable tool. Its upstream maintainers do not thereby control every downstream project installing it; only the installing project's actual authorized owner supplies S3/S5 parent closure. Independent external agents using their own private sessions are not counted as a shared upstream multi-agent organization.

## Self-hosted and non-human modes

No daemon/provider-backed autonomous executor is bundled. An operator can use manual handoff or opt into a configured external executable/deeplink; neither alone establishes first-party S1=A. Separate QA is an audit construction affordance, not a deployed independent reviewer. An entirely agent-governed project could be composed externally using these tools, but is not shipped as a complete first-party agentic operating mode.

## Recursion

Task contracts are not automatically viable subsystems; an external executor may hold local autonomy after launch, while project-level scope/risk/identity decisions are parent-owned. Separately named strategist/planner/reviewer roles express intended authority isolation but do not by themselves demonstrate independent nested viable organizations.

## Variety and escalation

Task scope and evidence gates attenuate implementation and proof variety before an owner merges changes. High-risk issues escalate to human approval; QA verdicts return to next implementation attempts. The state and receipt store supports reproducible review, but model execution and independent judgment are performed by composed external tool actors, not the deterministic CLI itself.

## Evidence gaps

- No autonomous model worker is packaged; manually dispatched prompts are not evidence that a model executed or owned the task.
- The `--auto` path executes a user-provided descriptor; no preconfigured default launch or provider-backed live run is credited.
- Review prompts and QA receipts support a complementary audit constructor; they do not independently prove a different model family, actor isolation or actual source-first review occurred.
- No demonstrated cross-task S2 conflict dampening beyond generic scope/dependencies/verification locks; no S4 environmental futures loop.
- Parent-maintained `.ai/` policy and generated adapter return were observed; these do not substitute for an autonomous first-party S1 or close S5 over such a unit.
- Canonical exclusion has all six `—` by the active Index admission boundary. The proposed vector C/—/P/C/—/P remains available in PR #2400 as analysis of constructor and external parent affordances, not as an included autonomy profile.

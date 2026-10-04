---
harness_id: forja
project_name: Forja
repository: https://github.com/lex0c/forja
review_ref: db34341cfacbca3a50029530d2e95a3ae3e5072e
reviewed_at: 2026-10-05
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-05
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# Forja

## Review boundary

- System in focus: Forja's first-party terminal coding harness at frozen revision `db34341cfacbca3a50029530d2e95a3ae3e5072e`, including its model/tool loop, playbook subagents, worktree isolation, verification/audit surfaces, cross-session memory and operator policy.
- Purpose and identity: autonomously perform repository coding/investigation work while making effects observable, reversible and bounded by explicit permissions, budgets and audit records.
- Relevant environment: user goal, repository/filesystem and Git state, provider/model outputs, tool results, subagent branches/worktrees, tests, memory corpus and operator permission/governance decisions.
- Standard-distribution boundary: installed Forja CLI/runtime, builtin tools/playbooks, subagent runtime, worktree manager, verify gate, memory governance and operator surfaces are inside. Model/provider services, host OS and external Git hosting are dependencies. Repository-development CI/evals are adjacent and excluded.
- Credited operating / distribution surfaces: interactive, one-shot and headless coding loops; autonomous mode; builtin and project/user playbooks; sync/async subagents; definition-selected worktree isolation; builtin read-only code-review playbook; shipped memory-verification/governance surfaces.
- Adjacent first-party surfaces excluded from ownership: Forja repository contribution CI/evals, maintainer merge decisions, unshipped roadmap/backlog mechanisms and benchmark-only evidence.
- First-party operating / deployment modes considered: supervised and autonomous terminal modes, headless/NDJSON mode, subagent playbooks, worktree-isolated mutating children and model-routed review playbooks.
- Recursion level: a top-level coding run and substantial child playbook runs are operational S1 cells; coordination/audit claims are evaluated only where first-party relations regulate those cells or independently challenge their claims.
- Reviewed revision: `db34341cfacbca3a50029530d2e95a3ae3e5072e`.
- Observation date: 2026-10-05.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Forja supplies a model-driven step loop with structured tools, permissions, checkpoints, budgets and context management. Playbooks can run as isolated child model loops through `task_sync` or `task_async`; mutating playbooks may declare `isolation: worktree`, causing the harness to create a dedicated Git worktree/branch and return preservation metadata to the parent.

Forja also ships a builtin `code-review` playbook whose tools are read-only and whose prompt explicitly defines it as a merge gatekeeper reporting blockers without fixing. The normal model routing guidance says review requests should be delegated to this isolated playbook rather than performed inline. The product additionally contains memory-verification/governance machinery, but the narrower code-review constructor is sufficient for the S3* finding below.

## Operational model

The primary model chooses tools and subagents, receives concrete tool/subagent results and iterates until it settles. In autonomous mode, ordinary development-loop confirmations are auto-approved while protected effects remain gated. Child agents have distinct conversations/runtime state and may execute concurrently; when configured for worktree isolation, their writes cannot land directly in the parent's working tree.

## S1 — Operations

- State: A
- Function: perform repository coding, investigation and development tasks through a model/tool feedback loop.
- Disturbance / variety regulated: heterogeneous codebases, incomplete context, tool/test failures, provider responses, permission outcomes, budget limits and user goals.
- Decisive decision or feedback right: choose what to inspect or change next, which tool/subagent to invoke, how to respond to returned evidence and when the requested task is complete.
- Decision owner: the active model-backed Forja actor.
- Supporting / enforcement mechanisms: tool registry, permission engine, checkpoints, sandbox, budgets, audit log, context/compaction, provider adapters and subagent runtime.
- Closure path: goal/context → model action/tool/subagent choice → observed result → result re-enters context → model revises the work until terminal answer or bounded stop.
- Boundary reachability: interactive, one-shot, headless and supported autonomous modes all instantiate the first-party loop directly.
- Why this is / is not agent-owned: removing the model leaves enforcement and persistence but removes open-ended coding/tool decisions.
- Evidence: README; `docs/spec/ORCHESTRATION.md`; harness/tool runtime.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: provider inference is external infrastructure, not organizational ownership.

## S2 — Coordination

- State: C
- Function: attenuate mutable-workspace interference among distinct delegated coding S1 cells by binding mutating child runs to isolated Git worktrees.
- Disturbance / variety regulated: concurrent or overlapping child coding runs against one repository could observe/overwrite one another's in-progress file changes or blur ownership of change sets.
- Decisive decision or feedback right: choose the worktree-isolation relation for a mutating playbook so its subsequent file actions occur on a dedicated branch/root rather than the parent's live checkout.
- Decision owner: constructor-level developer/operator definition; the runtime deterministically enforces `isolation: worktree`, while no shipped autonomous coordinator owns the isolation policy itself.
- Supporting / enforcement mechanisms: playbook isolation field, subagent validator, worktree creation/validation, unique child branch, per-child cwd, dirty-worktree preservation and returned worktree metadata.
- Closure path: playbook declares worktree isolation → parent model dispatches the child → Forja creates a dedicated worktree/branch → child reads/writes there → cleanup preserves dirty output for parent inspection or removes a clean branch → parent receives the child result/worktree metadata for subsequent action.
- Boundary reachability: `isolation: worktree` is a shipped playbook field; the ordinary model-facing task dispatcher and subagent runtime execute it without custom external glue.
- Distinct S1 units: top-level and child playbook runs have separate model conversations/runtime state, and multiple async child runs can execute concurrently.
- Inter-S1 disturbance: mutating child runs sharing one checkout would create write/read interference and ambiguous ownership of concurrent change sets.
- Attenuating coordination relation: Forja gives each worktree-isolated mutating child a dedicated Git worktree and branch, preventing its writes from leaking into the parent's live tree or another child tree.
- Feedback into subsequent S1 behaviour: the child actually runs with the isolated worktree as cwd, so later reads/writes are constrained to that state; its final result exposes preserved branch/path metadata back to the parent for follow-up rather than silently merging changes.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the credited mechanism is specifically tied to attenuation of concurrent filesystem/write interference; task messaging, async handles and shared budgets are not independently credited.
- Why this is / is not agent-owned: removing the parent model does not remove the definition-selected isolation rule; autonomous discretion is not what selects the coordination policy, so this is `C`, not `A`.
- Evidence: `src/subagents/worktree.ts`; `src/subagents/runtime.ts`; `src/subagents/validate.ts`; `src/tools/builtin/task.ts`; `docs/spec/ORCHESTRATION.md`.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: isolation prevents destructive interference but does not itself merge competing child changes; integration remains a later parent/operator decision.

## S3 — Inside-and-now control

- State: —
- Function: no distinct whole-system current-control function over a standing portfolio of operational units was established.
- Disturbance / variety regulated: shared cost caps, concurrency limits, child handles, cancellation and DAG scheduling bound one focal run and its delegated work.
- Decisive decision or feedback right: no separate whole-system priority/resource/accountability intervention right beyond task decomposition and run-local budget enforcement was established.
- Decision owner: not established at S3 level.
- Supporting / enforcement mechanisms: async handles, shared cost accounting, cap watchdog, max concurrent subagents, DAG failure policies and cancellation.
- Closure path: mechanisms constrain one run's delegation/execution but do not close a distinct current-management loop over an organizational portfolio.
- Why this is / is not agent-owned: model delegation is S1 task decomposition; deterministic budget/concurrency enforcement does not create S3 ownership.
- Evidence: `docs/spec/ORCHESTRATION.md`; `src/harness/subagent-dispatcher.ts`.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: custom higher-level compositions could use these primitives differently.

### Absence scope

- Surfaces inspected: sync/async subagents, DAG execution, child status/cancel paths, shared budgets, cost watchdog and orchestration documentation.
- Plausible first-party paths checked: parent model as S3 supervisor; async handle registry as current view; budget/cap watchdog as resource control; DAG scheduler as S3.
- Why no material first-party path remains: each path is scoped to execution/decomposition of the current focal task and lacks a separate whole-system current-control function at the assessed recursion.

## S3* — Complementary audit

- State: C
- Function: challenge a proposed code change with a distinct read-only reviewer path that inspects the actual diff/repository context and returns structured blocking findings.
- Disturbance / variety regulated: a coding actor may miss regressions, security flaws, contract breaks or dangerous untested paths in its own changed code.
- Decisive decision or feedback right: inspect the proposed diff independently and emit a structured merge-oriented report with blockers, nits, questions, explicit not-reviewed areas and a ship/rework summary.
- Decision owner: constructor path. Forja supplies the separate autonomous reviewer actor and restricted audit surface, but standard runtime does not automatically bind every producer completion to mandatory repair/re-review closure; caller/operator orchestration remains decisive for acting on the report.
- Supporting / enforcement mechanisms: protected builtin `code-review` playbook, read-only tool whitelist, isolated child context, structured output schema, playbook routing guidance and subagent runtime.
- Closure path: changed code/branch exists → review request is routed to the builtin read-only reviewer → reviewer directly reads diff/context and returns structured findings → parent/user can route blockers into correction and a later review; mandatory corrective re-review is not automatically closed by the standard path.
- Boundary reachability: `forja init` installs builtin playbooks and first-party routing guidance explicitly maps diff/PR/branch review requests to `code-review`; no external reviewer product is needed.
- Claim being audited: that the proposed code change is fit to ship/merge without material regression or security/contract blockers.
- Ordinary reporting path: the coding actor's own final answer/change set and normal tool history.
- Complementary access path: a separate read-only reviewer model gets Git/diff plus direct repository reads/searches and must ground findings in file/line evidence.
- Independence boundary: reviewer tools cannot mutate the code and its prompt/context are distinct from the producer's ordinary coding turn; however the standard product leaves report acceptance/correction orchestration to the caller/operator.
- Who acts on findings: parent agent or human/operator must apply corrections and request subsequent review.
- Why this is / is not agent-owned: the independent audit actor exists first-party, but the complete audit-to-correction-to-re-review loop is not mandatory/closed autonomously; the function-specific constructor therefore publishes as `C`.
- Evidence: `src/cli/init-playbooks/code-review.md`; `src/cli/playbook-prompt.ts`; subagent runtime/dispatcher.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the separate default-on memory verifiers provide additional complementary evidence paths, but are not needed to strengthen this narrower code-change S3* classification.

## S4 — Outside-and-then intelligence

- State: —
- Function: no externally and prospectively oriented adaptation loop was established.
- Disturbance / variety regulated: memory, retrieval, browser use, skills and current-task research can preserve or fetch context for present work.
- Decisive decision or feedback right: no first-party loop was established that senses future/external change, develops adaptation options and returns a selected option into current capability/S3.
- Decision owner: not established.
- Supporting / enforcement mechanisms: memory corpus, proactive recall, browser/retrieval tools, skill/playbook catalog and provider configuration.
- Closure path: contextual evidence changes current task behavior, not a distinct outside-and-then adaptation cycle.
- Why this is / is not agent-owned: learning/recall/research inside current work is not S4 by itself.
- Evidence: README; `docs/MEMORY.md`; tool/playbook docs.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: roadmap/evals are adjacent development surfaces and excluded.

### Absence scope

- Surfaces inspected: memory lifecycle/governance, proactive recall, browser/retrieval, skills, provider model catalog and development adaptation docs.
- Plausible first-party paths checked: memory verification as S4; proactive recall as adaptation; browser research as S4; model switching as adaptation.
- Why no material first-party path remains: inspected loops validate/retrieve present knowledge or configure execution, without a closed external/prospective option-generation relation.

## S5 — Policy and identity

- State: —
- Function: no qualifying identity/ultimate-policy closure was established.
- Disturbance / variety regulated: enterprise/user/project permissions, trust attestation, supervised/autonomous mode, memory-governance approvals and protected effects constrain operation.
- Decisive decision or feedback right: no identity/ultimate-policy issue is routed through a first-party legitimate authority and returned as a system-identity decision.
- Decision owner: not established at S5 level.
- Supporting / enforcement mechanisms: layered permissions, trust gate, policy locks, operator confirmations, memory governance proposals and static runtime safety rules.
- Closure path: operator decisions constrain specific effects or memory-state changes, but no identity/ultimate-policy issue/authority/return loop is established.
- Why this is / is not agent-owned: permission and memory-governance controls are operational governance, not evidence of S5 identity closure.
- Evidence: README; permission/security docs; `docs/MEMORY.md`; `src/memory/governance.ts`.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: operator authority is real but remains below the Profile's S5 identity/ultimate-policy threshold.

### Absence scope

- Surfaces inspected: layered permission policy, trust boundary, autonomous/supervised mode, operator confirmations, memory governance and project bootstrap configuration.
- Plausible first-party paths checked: enterprise policy as S5; trust attestation as S5; memory governance as S5; protected-effect approval as S5.
- Why no material first-party path remains: each inspected mechanism governs actions/context/memory rather than identity or ultimate policy of the harness/system.

## Recursion

Top-level and substantial playbook child loops can be treated as operational cells for the narrow S2 constructor finding. Nested subagents remain bounded children; worktree/IPC nesting does not by itself establish full recursive viability.

## Variety and escalation

Forja absorbs operational variety through model/tool iteration, subagent specialization, isolated worktrees, permissions, checkpoints, budgets, verification and memory. Protected effects and governance proposals escalate to the operator; audit findings can likewise be returned to a parent/human for correction.

## Evidence gaps

No `?` state is required. The frozen source provides explicit evidence for S1, worktree-specific S2 constructor coordination and the read-only code-review S3* constructor, with sufficient boundary coverage for negative S3/S4/S5 findings.

## Assessment summary

Forja closes autonomous S1 through its model/tool coding loop, supplies constructor S2 through definition-selected worktree isolation for mutating child agents, and supplies constructor S3* through a distinct read-only code-review playbook. Run-local orchestration does not establish whole-system S3, while memory/retrieval and layered policy do not close prospective S4 or identity-level S5.

**Vector:** A · C · — · C · — · —

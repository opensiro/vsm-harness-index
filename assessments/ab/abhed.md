---
harness_id: abhed
project_name: Abhed
repository: https://github.com/zybuu-ai/abhed
review_ref: 151b8ddceee7ae232e526b3c237356151dde780e
reviewed_at: 2026-09-26
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-26
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Abhed

## Review boundary

- System in focus: one first-party Abhed Community Edition agent-harness deployment at pinned revision `151b8ddceee7ae232e526b3c237356151dde780e`, including the ordinary event-sourced model/tool loop, native tools, context/offload/compaction, first-party `task` / `tasks` subagent paths, role profiles, git-worktree isolation, permissions/policy, durable session record/replay, HawkEYE session inspection and standard CLI/headless/server surfaces where implemented in this repository.
- Purpose and identity: execute open-ended technical work through a model-driven local/on-prem agent while keeping actions policy-bounded, replayable and optionally decomposable into bounded fresh-context subagents that can investigate, test, review or perform parallel work.
- Relevant environment: user/operator requests, repository/filesystem/process state, configured model provider, optional web/retrieval/MCP dependencies, git state, policy/approval decisions and persisted session records.
- Standard-distribution boundary: Apache-2.0 Community Edition code and documented first-party runtime paths at the frozen revision. Proprietary Team/Enterprise features named in the README, repository-development eval/benchmark/red-team activity, CI and arbitrary downstream extensions are adjacent unless Community Edition production wiring directly invokes them.
- Credited operating / distribution surfaces: normal CLI and headless agent loop; first-party tool registry; `task` and concurrent `tasks`; fresh-context explore/test/review/general profiles; optional git-worktree isolation; shared hierarchical subagent limits; policy/approval path; durable event store/replay/fork/recall; HawkEYE inspection reachable from CLI/server/session commands.
- Adjacent first-party surfaces excluded from ownership: `abhed eval`, benchmark corpora/results, adversarial suites and repository-development security validation as organizational audit of the assessed runtime; proprietary scheduled-run/admin/audit-export features explicitly excluded from this repository; roadmap/design claims not corroborated by frozen production code; arbitrary extension/MCP behavior not supplied by Abhed itself.
- First-party operating / deployment modes considered: interactive CLI, headless CLI, ordinary server/API sessions where backed by the same runtime, single-agent execution, one delegated subagent, concurrent `tasks` fan-out with shared workspace or `worktree` isolation, role-scoped review/explore/test children, replay/inspection paths and configured permission modes.
- Recursion level: one Abhed session/deployment centered on the primary model-driven agent. The primary loop and each spawned child loop are S1 operational units when executing work. The assessment asks whether first-party relations among those credited operations close S2/S3/S3* rather than inferring metasystemic functions from plurality alone.
- Reviewed revision: `151b8ddceee7ae232e526b3c237356151dde780e`.
- Observation date: 2026-09-26.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Abhed's Community Edition contains a genuine event-sourced model/tool loop. `Loop.Run` repeatedly assembles the model request, obtains model output, executes selected tools under policy, records outcomes and returns tool/environment evidence into later turns until a terminal condition. The normal CLI wires this loop to native tools, optional retrieval/web/MCP surfaces, persistence and approvals. The active model therefore owns the substantive next-action judgment while deterministic runtime machinery enforces limits and permissions.

The same normal runtime registers both `task` and `tasks`. A subagent gets a fresh system prompt and conversation, a role-scoped tool registry, its own session record and a bounded return summary. The `tasks` tool runs several such loops concurrently. Its source identifies a concrete interference problem: writing children in one checkout can overwrite one another and make authorship/survival of changes ambiguous. The model-callable tool therefore exposes `isolation: "worktree"`; when selected, each child is placed in a distinct git worktree/branch and the parent receives per-branch change/merge information after completion. Tests verify isolation prevents one child's writes from appearing in another child's worktree or the main tree.

That establishes an S2 relation rather than merely concurrency. The parent model chooses whether the actual task needs isolated worktrees, while first-party runtime enforces separate workspaces. The coordination decision changes the environments in which child S1s operate and returns merge/branch facts to the parent for subsequent integration decisions.

The multi-agent surface does not, however, establish S3 current control. A single `task` call waits for its child. `tasks` creates the batch, waits for all children with `wg.Wait()`, and only then assembles outcomes. The standard model-callable surface reviewed here has no live child-tree list/status/message/interrupt/close loop comparable to a whole-system current-control console. Hierarchical token/subagent/concurrency limits are operator-configured deterministic enforcement, not themselves a discretionary S3 owner.

Abhed does expose a materially complementary review path. The built-in `review` profile has a fresh context, direct read/search access to the workspace and no write/bash tools; its explicit job is to find correctness bugs and return file:line findings plus concrete failure scenarios. `task`/`tasks` expose that profile in the standard model-callable subagent surface, and the parent receives the independent child's bounded conclusion for subsequent fixing/testing/delegation. This is credited as S3* because the review child forms its judgment from operational artifacts directly rather than merely relaying an implementer's self-report. HawkEYE is useful corroborating inspection infrastructure but is not the basis of S3*: it is a deterministic pure function of the same event record and does not itself close corrective action.

No qualifying S4 or S5 loop was found. Web/retrieval/skills/model selection increase task capability but do not close an outside-and-then organizational adaptation loop. System prompts, managed config, deny/ask/allow policy and human approvals constrain operational action, but no standard path elevates an identity/ultimate-policy issue to legitimate ultimate authority and returns that resolution as an S5 policy decision.

Primary evidence:

- [`internal/agent/loop.go`](https://github.com/zybuu-ai/abhed/blob/151b8ddceee7ae232e526b3c237356151dde780e/internal/agent/loop.go) — production model/tool feedback loop, termination, budget enforcement and steering.
- [`app/main.go`](https://github.com/zybuu-ai/abhed/blob/151b8ddceee7ae232e526b3c237356151dde780e/app/main.go) — normal CLI/headless wiring that registers `task` and `tasks`, role profiles, policy, persistence and runtime dependencies.
- [`internal/agent/subagent.go`](https://github.com/zybuu-ai/abhed/blob/151b8ddceee7ae232e526b3c237356151dde780e/internal/agent/subagent.go) — fresh-context child loops, role-scoped tools, bounded summaries, workspaces and hierarchical limits.
- [`internal/agent/parallel.go`](https://github.com/zybuu-ai/abhed/blob/151b8ddceee7ae232e526b3c237356151dde780e/internal/agent/parallel.go) — concurrent multi-subagent execution, explicit shared-checkout overwrite disturbance, model-selected worktree isolation and branch/merge feedback.
- [`internal/agent/parallel_test.go`](https://github.com/zybuu-ai/abhed/blob/151b8ddceee7ae232e526b3c237356151dde780e/internal/agent/parallel_test.go) — verifies parallel execution bounds and that isolated writing children cannot touch one another or the main worktree.
- [`internal/agent/prompt.go`](https://github.com/zybuu-ai/abhed/blob/151b8ddceee7ae232e526b3c237356151dde780e/internal/agent/prompt.go) — built-in explore/test/review profiles; review is direct, read-only correctness inspection with concrete failure reporting.
- [`internal/agent/subagent_test.go`](https://github.com/zybuu-ai/abhed/blob/151b8ddceee7ae232e526b3c237356151dde780e/internal/agent/subagent_test.go) — verifies fresh delegated execution, bounded summary return, role tool narrowing and budget/count limits.
- [`docs/guide/04-permissions.md`](https://github.com/zybuu-ai/abhed/blob/151b8ddceee7ae232e526b3c237356151dde780e/docs/guide/04-permissions.md) — action-policy/approval semantics inspected for S5 and kept distinct from identity/ultimate-policy closure.
- [`docs/guide/15-hawkeye.md`](https://github.com/zybuu-ai/abhed/blob/151b8ddceee7ae232e526b3c237356151dde780e/docs/guide/15-hawkeye.md) — deterministic session-record inspection, explicitly a pure function of the record; inspected as supporting audit evidence rather than treated as S3* ownership.
- [`README.md`](https://github.com/zybuu-ai/abhed/blob/151b8ddceee7ae232e526b3c237356151dde780e/README.md) and [`docs/architecture/02-system-architecture.md`](https://github.com/zybuu-ai/abhed/blob/151b8ddceee7ae232e526b3c237356151dde780e/docs/architecture/02-system-architecture.md) — supported product boundary and architecture, used where corroborated by source.

## Operational model

A primary Abhed agent receives an objective, chooses tool-mediated actions, observes results and continues from changed evidence. It can delegate bounded work to independent fresh-context child loops. For parallel writing work it can ask the first-party `tasks` tool to isolate children into separate worktrees, then use the returned summaries and branch facts for subsequent integration. It can also delegate a read-only `review` child that independently inspects repository reality and returns corrective findings. Runtime policy, limits, storage and sandboxing enforce the operating envelope but do not substitute for the agent-owned judgments credited to S1/S2/S3*.

## S1 — Operations

- State: A
- Function: transform an open-ended technical objective into repository/environment outcomes through repeated model-selected actions, tool execution and evidence feedback.
- Disturbance / variety regulated: changing user requirements, repository/filesystem/process state, tool results/errors, model/provider responses, policy outcomes, context pressure and child-agent results.
- Decisive decision or feedback right: choose the next substantive response/tool action and revise later behavior from observed tool/environment evidence.
- Decision owner: the active Abhed model agent in the primary or delegated child loop.
- Supporting / enforcement mechanisms: `Loop`, tool registry, policy/approver, session workspace, event recorder/store, context offload/compaction, sandbox, provider adapter, budgets and presentation/server surfaces.
- Closure path: objective enters the session → model selects an action/tool call → Abhed policy/runtime executes or refuses it → result/denial is recorded and returned to the conversation → later model turn observes changed evidence and chooses the next action → task/environment state changes.
- Boundary reachability: `app/main.go` wires the standard interactive/headless Community Edition session directly to `Loop` and its tool surface; spawned subagents instantiate the same first-party loop with bounded role-specific configuration.
- Why this is / is not agent-owned: deterministic code executes, constrains and records already-selected actions, but removing the model eliminates the substantive next-action choice and adaptive interpretation of returned evidence.
- Evidence: [`internal/agent/loop.go`](https://github.com/zybuu-ai/abhed/blob/151b8ddceee7ae232e526b3c237356151dde780e/internal/agent/loop.go); [`app/main.go`](https://github.com/zybuu-ai/abhed/blob/151b8ddceee7ae232e526b3c237356151dde780e/app/main.go); [`internal/agent/subagent.go`](https://github.com/zybuu-ai/abhed/blob/151b8ddceee7ae232e526b3c237356151dde780e/internal/agent/subagent.go).
- Basis: explicit + structural
- Confidence: high
- Caveats: external inference is a dependency, but Abhed supplies the first-party feedback loop that repeatedly invokes it and applies its decisions to the operating environment.

## S2 — Coordination

- State: A
- Function: attenuate destructive write interference between distinct concurrently executing child agents by separating editing work into isolated git worktrees/branches when parallel writes would collide.
- Disturbance / variety regulated: two or more writing subagents operating in one checkout can overwrite one another, obscure which changes survived and make concurrent implementation state inconsistent.
- Decisive decision or feedback right: decide whether a concrete parallel batch requires `worktree` isolation rather than a shared workspace and supply the task decomposition/roles executed under that coordination choice.
- Decision owner: the primary Abhed model agent calling the standard `tasks` tool.
- Supporting / enforcement mechanisms: `Tasks` schema/description, git worktree creation, per-child `SubagentRequest.Workspace`, child session scoping, branch naming, concurrency semaphore and returned per-worktree diff/merge instructions.
- Closure path: primary agent identifies independent parallel work with write risk → selects `tasks` with `isolation: "worktree"` → runtime creates one branch/worktree per child and binds each child S1 to its own workspace → children operate without cross-writing → `tasks` returns every child summary plus branch/change/merge facts → parent uses that coordinated result for subsequent integration or further work.
- Boundary reachability: `app/main.go` registers `agent.Tasks` in the normal Community Edition tool registry and supplies the standard `SubagentFactory`; isolation is a documented model-callable argument rather than a test-only helper.
- Distinct S1 units: two or more fresh-context child `Loop` instances spawned concurrently by one `tasks` call, each capable of model/tool operation on a bounded delegated outcome.
- Inter-S1 disturbance: parallel writing children sharing one checkout can overwrite one another's changes so the parent cannot reliably tell whose change survived.
- Attenuating coordination relation: model-selected worktree isolation gives every child a separate git branch/checkout and filesystem scope, preventing one child from modifying another child's current work or the main tree.
- Feedback into subsequent S1 behaviour: workspace binding changes each child S1's operational environment before it acts; after completion the parent receives per-branch status/change/merge information and can choose how subsequent integration work proceeds.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the positive mapping rests on an explicit inter-S1 write-collision disturbance and a first-party isolation relation built specifically to attenuate it; concurrency limits and subagent delegation alone are not credited.
- Why this is / is not agent-owned: Abhed deterministically enforces the requested isolation, but the parent model owns the task-specific judgment that concurrent writing work needs isolation and invokes the coordinating mode. Removing that judgment leaves the mechanism but not the actual coordination decision for the current task.
- Evidence: [`internal/agent/parallel.go`](https://github.com/zybuu-ai/abhed/blob/151b8ddceee7ae232e526b3c237356151dde780e/internal/agent/parallel.go); [`internal/agent/parallel_test.go`](https://github.com/zybuu-ai/abhed/blob/151b8ddceee7ae232e526b3c237356151dde780e/internal/agent/parallel_test.go); [`app/main.go`](https://github.com/zybuu-ai/abhed/blob/151b8ddceee7ae232e526b3c237356151dde780e/app/main.go); [`internal/agent/subagent.go`](https://github.com/zybuu-ai/abhed/blob/151b8ddceee7ae232e526b3c237356151dde780e/internal/agent/subagent.go).
- Basis: explicit + structural
- Confidence: high
- Caveats: `isolation: "none"` deliberately permits shared-workspace operation. S2=A credits the standard agent-owned coordination path when parallel writes require isolation; it does not claim every concurrent batch is automatically coordinated.

## S3 — Inside-and-now control

- State: —
- Function: no material first-party whole-system inside-and-now current-control loop is established over the temporary Abhed multi-agent organization.
- Disturbance / variety regulated: Abhed bounds spend, spawn count and concurrency and the parent chooses initial delegation, but no standard model-callable path manages changing live child commitments from a whole-system current view.
- Decisive decision or feedback right: not established for ongoing cross-child current control.
- Decision owner: none established for S3 at this boundary.
- Supporting / enforcement mechanisms: parent-created task batch, per-child `max_turns`, hierarchical token/subagent limits, `MaxParallel`, context cancellation and final aggregated task outcomes constrain execution but do not themselves establish S3.
- Closure path: not applicable; the parent launches delegated work and receives results after child completion, but no reviewed path closes live whole-system status → discretionary intervention/reallocation → renewed whole-system feedback while children are active.
- Whole-system current view: not established. `task` blocks on one child; `tasks` launches the requested batch and waits for all goroutines before assembling the returned outcome report.
- Current-control decision scope: the parent can choose initial tasks, roles, turn caps and isolation, but the standard tool surface exposes no child `list`/progress/steer/interrupt/close/reassign controls over the running batch.
- Why this is / is not agent-owned: without an established S3 function, ownership classification does not proceed. Initial decomposition and deterministic limit enforcement remain S1/S2 support rather than a whole-system current regulator.
- Evidence: [`internal/agent/subagent.go`](https://github.com/zybuu-ai/abhed/blob/151b8ddceee7ae232e526b3c237356151dde780e/internal/agent/subagent.go); [`internal/agent/parallel.go`](https://github.com/zybuu-ai/abhed/blob/151b8ddceee7ae232e526b3c237356151dde780e/internal/agent/parallel.go); [`config/config.go`](https://github.com/zybuu-ai/abhed/blob/151b8ddceee7ae232e526b3c237356151dde780e/config/config.go); [`app/main.go`](https://github.com/zybuu-ai/abhed/blob/151b8ddceee7ae232e526b3c237356151dde780e/app/main.go).
- Basis: explicit + structural absence review
- Confidence: high
- Caveats: the architecture document calls the primary actor an orchestrator and describes plan/budget ownership, but Methodology `0.3.6` requires the actual current-control function; naming, initial delegation and configured resource caps are insufficient.

### Absence scope

- Surfaces inspected: single and parallel subagent APIs, role profiles, hierarchical budget/spawn/concurrency limits, main-loop steering, session records and normal CLI/headless wiring.
- Plausible first-party paths checked: parent supervision of running subagents, live child-tree inspection, per-child steering/interruption/reassignment, resource/capacity control and recovery from partial child failure.
- Why no material first-party path remains: the reviewed standard child tools expose launch-and-return semantics rather than a live whole-system control surface; resource caps are deterministic enforcement and aggregated outcomes arrive after the batch wait.

## S3* — Complementary audit

- State: A
- Function: independently inspect current repository reality for correctness defects through a fresh-context read-only reviewer child and return evidence-backed findings for corrective action.
- Disturbance / variety regulated: implementation defects or inaccurate/incomplete conclusions that the implementing primary/child agent's normal execution and self-report may fail to expose.
- Decisive decision or feedback right: form a correctness judgment from direct read/search access to the workspace and identify concrete bugs/failure scenarios independently of the implementer's transcript or summary.
- Decision owner: the model running the built-in `review` subagent profile.
- Supporting / enforcement mechanisms: fresh subagent context, `review` profile instruction, read-only `read`/`glob`/`grep` subset, independent child `Loop`, bounded summary return and parent model continuation.
- Closure path: implementation/current repository state exists → parent invokes a `review` child through `task` or `tasks` → reviewer independently reads/searches repository artifacts and forms correctness findings → bounded findings return to the parent as a tool result → parent can revise code, test, delegate or otherwise change subsequent operation from those findings.
- Boundary reachability: `review` is a built-in first-party profile exposed through the normal `task` / `tasks` tool schemas, and those tools are registered in the ordinary Community Edition CLI/headless runtime.
- Claim being audited: that the current implementation/repository state produced or accepted by ordinary agent operation is correct enough to proceed without a concrete correctness defect.
- Ordinary reporting path: an implementing agent/subagent returns its own assistant summary and normal tool/session record to the parent/runtime.
- Complementary access path: a separate `review` child starts with a fresh context and directly inspects current workspace files through read/search tools rather than consuming only the implementing worker's summary.
- Independence boundary: the reviewer receives none of the parent's conversational turns, has an explicit non-fixing review role and a read-only tool subset; its correctness judgment is produced by a distinct child model loop over repository evidence.
- Who acts on findings: the primary Abhed model agent receives the reviewer summary as a normal tool result and owns subsequent corrective tool use, testing or further delegation within the same session.
- Why this is / is not agent-owned: Abhed supplies the separate review channel and tool restrictions, but the substantive bug judgment is made by the reviewer model from direct evidence. Removing reviewer-agent judgment leaves read/search primitives but no equivalent correctness findings.
- Evidence: [`internal/agent/prompt.go`](https://github.com/zybuu-ai/abhed/blob/151b8ddceee7ae232e526b3c237356151dde780e/internal/agent/prompt.go); [`internal/agent/subagent.go`](https://github.com/zybuu-ai/abhed/blob/151b8ddceee7ae232e526b3c237356151dde780e/internal/agent/subagent.go); [`app/main.go`](https://github.com/zybuu-ai/abhed/blob/151b8ddceee7ae232e526b3c237356151dde780e/app/main.go); [`docs/guide/15-hawkeye.md`](https://github.com/zybuu-ai/abhed/blob/151b8ddceee7ae232e526b3c237356151dde780e/docs/guide/15-hawkeye.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: HawkEYE and repository eval/red-team infrastructure are not the decisive S3* owner. The positive claim is the standard fresh-context direct-workspace reviewer path; arbitrary use of a generic subagent as a reviewer would not have been sufficient without this built-in role/access boundary.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party outside-and-then organizational adaptation loop is established at the assessed session/deployment recursion.
- Disturbance / variety regulated: Abhed can retrieve current information, search the web, use skills, switch models and retain session/history state, but these capabilities are not shown owning prospective adaptation of the harness organization.
- Decisive decision or feedback right: not established for adopting an organizational capability/policy change from external/future distinctions.
- Decision owner: none established for S4 at this boundary.
- Supporting / enforcement mechanisms: web search, RAG/retrieval, skills, provider/model selection, project memory, session replay/fork/recall, compaction and repository-development eval/benchmark material.
- Closure path: not applicable; reviewed paths acquire information or change task execution/configuration but do not close external/future sensing → adaptation option → adopted change to current organizational capability/S3.
- Why this is / is not agent-owned: the model may autonomously research information for an S1 task, but no separate S4 organizational adaptation function is established, so task research is not reclassified as S4.
- Evidence: [`internal/agent/prompt.go`](https://github.com/zybuu-ai/abhed/blob/151b8ddceee7ae232e526b3c237356151dde780e/internal/agent/prompt.go); [`app/main.go`](https://github.com/zybuu-ai/abhed/blob/151b8ddceee7ae232e526b3c237356151dde780e/app/main.go); [`README.md`](https://github.com/zybuu-ai/abhed/blob/151b8ddceee7ae232e526b3c237356151dde780e/README.md).
- Basis: explicit + structural absence review
- Confidence: high
- Caveats: repository research/evaluation informed Abhed's development, but development-process learning is adjacent to the frozen runtime unless a first-party operational return loop is established.

### Absence scope

- Surfaces inspected: web search, retrieval/indexing, skills, model/provider switching, ABHED.md/project memory, event replay/fork/recall, context compaction and evaluation/benchmark documentation.
- Plausible first-party paths checked: autonomous current-information research, retained session knowledge, model switching, capability extension and repository-development evaluation.
- Why no material first-party path remains: these surfaces provide task knowledge, persistence or configured capability, but no reviewed standard path senses an external/prospective organizational distinction and returns a selected adaptation into the present harness organization.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy decision loop is established at the assessed session/deployment recursion.
- Disturbance / variety regulated: system prompt, project/org memory, permission modes, deny/ask/allow rules, managed config and approval gates constrain operational behavior but are not shown resolving identity/ultimate-policy issues.
- Decisive decision or feedback right: not established for an identity-level policy issue.
- Decision owner: none established for S5 within the Community Edition runtime.
- Supporting / enforcement mechanisms: layered system prompt/memory, managed configuration precedence, ordered policy engine, absolute deny, destructive-action confirmation, human approver and workspace/additional-directory boundaries.
- Closure path: not applicable; no reviewed path detects an identity/ultimate-policy issue, escalates it to legitimate ultimate authority and returns an authoritative resolution that governs subsequent operation.
- Why this is / is not agent-owned: agents act within operator/org-configured constraints and can receive ordinary action approvals/denials, but neither static policy nor generic approval confers ultimate policy authority on the model or operator as an S5 loop.
- Evidence: [`docs/guide/04-permissions.md`](https://github.com/zybuu-ai/abhed/blob/151b8ddceee7ae232e526b3c237356151dde780e/docs/guide/04-permissions.md); [`config/config.go`](https://github.com/zybuu-ai/abhed/blob/151b8ddceee7ae232e526b3c237356151dde780e/config/config.go); [`internal/agent/prompt.go`](https://github.com/zybuu-ai/abhed/blob/151b8ddceee7ae232e526b3c237356151dde780e/internal/agent/prompt.go); [`app/main.go`](https://github.com/zybuu-ai/abhed/blob/151b8ddceee7ae232e526b3c237356151dde780e/app/main.go).
- Basis: explicit + structural absence review
- Confidence: high
- Caveats: managed org policy can be stronger than local configuration and interactive approval can return reasons to the model, but Methodology `0.3.6` does not treat constraint precedence or ordinary action authorization as S5 without identity/ultimate-policy closure.

### Absence scope

- Surfaces inspected: system prompt and ABHED.md layers, managed config precedence, permission modes/rules, extension vetoes, destructive-action confirmation, human approval and workspace authorization.
- Plausible first-party paths checked: local/operator override, managed-organization policy, approval denial/reason feedback and runtime configuration changes.
- Why no material first-party path remains: these mechanisms specify or enforce operational constraints; no standard Community Edition path turns an identity/ultimate-policy issue into an ultimate-authority decision with return-to-operation closure.

## Distributed OSS parent arrangement

Abhed is open source, but repository maintainer/contributor governance was not used to infer runtime parent ownership. The assessed system is one Community Edition operating deployment/session. Project development, release governance, benchmark research and proprietary edition administration remain adjacent unless frozen first-party runtime evidence closes them back into the assessed organization.

## Self-hosted and non-human modes

Abhed is explicitly designed for local/on-prem and air-gapped operation and supports headless execution. Interactive approvals can gate actions, while headless runs refuse calls that still require consent unless policy already authorizes them. Those action-level human/configuration controls do not create parent-mode notation for S3/S4/S5 without the corresponding organizational function.

## Recursion

The focal recursion is one Abhed session/deployment. The primary model/tool loop is an S1 operation, and each fresh-context delegated child is another bounded S1 when spawned. Concurrent children can create real S1 plurality. At that plurality, first-party worktree isolation closes S2 for write-interference attenuation and the built-in direct-workspace reviewer path closes S3*. No live whole-tree current-control relation sufficient for S3 is established.

## Variety and escalation

Abhed attenuates operational variety through policy/approval rules, workspace and sandbox boundaries, turn/token/subagent/concurrency limits, context offload/compaction, role-scoped tools, git-worktree isolation and durable event recording. Tool denials return reasons so the active S1 can adapt; interactive users can steer the primary loop at turn boundaries; reviewer findings return to the primary agent for corrective action. These mechanisms are credited only where they close the mapped function rather than being treated as metasystemic merely because they constrain execution.

## Evidence gaps

- No fresh runtime trace was executed inside this assessment environment; positive claims rely on the frozen first-party source, tests and production wiring.
- S2=A depends on the standard `worktree` isolation path for concurrent writing children; shared-workspace parallelism alone would not establish the credited attenuation.
- S3 remains absent because launch/budget/concurrency enforcement and final fan-in do not provide a live whole-system child view plus discretionary intervention rights.
- S3*=A credits the built-in fresh-context read-only `review` profile with direct workspace access and return to the parent; HawkEYE/eval/red-team surfaces are not used as substitutes for that independent judgment.
- S4 remains absent despite research/retrieval/model-selection capabilities because no operational outside-and-then adaptation closure was established.
- S5 remains absent despite strong policy/managed-config/approval machinery because operational constraint enforcement is not identity/ultimate-policy closure.

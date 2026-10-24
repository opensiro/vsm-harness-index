---
harness_id: sanook-cli
project_name: Sanook CLI
repository: https://github.com/Sir-chawakorn/sanook-cli
review_ref: c7bbede1823b68f4c48959dc34d864a5404762c8
reviewed_at: 2026-10-23
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-23
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: A
autonomy_s5: —
---

# Sanook CLI

## Review boundary

- System in focus: one installed, locally operated Sanook CLI model-driven coding assistant, including its first-party child-agent tools, local gateway/scheduler, memory and skills.
- Purpose and identity: perform interactive or headless software and general assistant tasks using tools, independently executing bounded child tasks, optional isolated concurrent edits and reusable local operating procedures.
- Relevant environment: user tasks, changing project files/Git state, tool execution and errors, overlapping child writes, model-provider output, recurring future tasks and operator approvals.
- Standard-distribution boundary: pinned TypeScript/Node CLI v0.5.13 with the supported REPL/headless/gateway invocation paths, local config, skill store, task registry and Git worktree helper. A provider and network access are necessary for actual model inference; external models are not first-party governors.
- Credited operating / distribution surfaces: `src/bin.ts`, `src/loop.ts`, `src/tools/index.ts`, `src/tools/task.ts`, `src/orchestrate.ts`, `src/worktree.ts`, `src/tools/skill.ts`, `src/skills.ts`, `src/auto-maintain.ts`, `src/approval.ts`, `src/ui/app.tsx`, `src/gateway/` and local persistence helpers.
- Adjacent first-party surfaces excluded from ownership: test mocks/fixtures, CI, release and contributor workflows, repository documentation, source maintainer decisions and evaluation/doctor commands when not running as a controlling agent in the installed harness. External provider, hosted services, MCP servers and user organizations are not donated owners.
- First-party operating / deployment modes considered: model-selected local tools and child tasks; parallel child agents with optional `isolate=true` worktree separation and sequential patch apply; parent-model background task roster/abort; attended TUI task inspection; `create_skill` and later skill discovery; user `ask` versus supported automatic permissions; gateway/scheduled jobs and automatic memory maintenance.
- Recursion level: one Sanook process/session with its own model-backed primary and child operational units, not the upstream project's maintainer organization or several independent installs.
- Reviewed revision: `c7bbede1823b68f4c48959dc34d864a5404762c8` (batch #1011 frozen row 6).
- License screen: repository root `LICENSE` grants Apache-2.0.
- Observation date: 2026-10-23.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

`runAgent` builds the session system prompt from local memory, persisted skills, Git/repository context and optional second-brain retrieval, executes provider-backed `streamText` with registered tools and returns results for further model decisions. `task`, `task_parallel` and background `task_spawn` start separate `runAgent` instances with bounded recursion, budgets, tool subsets and per-child async contexts. `task_parallel(isolate=true)` gives concurrently writing children private Git worktrees, captures their resulting diffs, then applies each patch to the parent sequentially; conflicts are reported, not silently dropped or intelligently reconciled. Background jobs are retained in a session-scoped `TaskRegistry`, exposed to the parent model through `task_status`, `task_collect` and `task_cancel`; the TUI also exposes a read-only tasks hub.

The primary model can decide that a completed multi-step procedure will recur and call `create_skill` to write a reusable global Markdown runbook. Later `runAgent` turns load its metadata in the system prompt and can retrieve its complete procedure through `skill`, providing a bounded longitudinal capability-adaptation path. The separate automatic memory/vault consolidation and relevant-fact recall supply context but are not independently promoted to S4 ownership. Gateway scheduling serves user-selected future tasks; permission gates and user persona/config do not establish ultimate policy. Native tests exercise tool and workflow mechanics without real model requests.

Frozen primary evidence: [model loop](https://github.com/Sir-chawakorn/sanook-cli/blob/c7bbede1823b68f4c48959dc34d864a5404762c8/src/loop.ts), [task tools](https://github.com/Sir-chawakorn/sanook-cli/blob/c7bbede1823b68f4c48959dc34d864a5404762c8/src/tools/task.ts), [worktree lifecycle](https://github.com/Sir-chawakorn/sanook-cli/blob/c7bbede1823b68f4c48959dc34d864a5404762c8/src/worktree.ts), [skill creation](https://github.com/Sir-chawakorn/sanook-cli/blob/c7bbede1823b68f4c48959dc34d864a5404762c8/src/tools/skill.ts), [skill reuse](https://github.com/Sir-chawakorn/sanook-cli/blob/c7bbede1823b68f4c48959dc34d864a5404762c8/src/skills.ts), [task registry](https://github.com/Sir-chawakorn/sanook-cli/blob/c7bbede1823b68f4c48959dc34d864a5404762c8/src/orchestrate.ts).

## Operational model

The primary model owns task-local tool and delegation selections; child models each carry out their own bounded operational work (`S1=A`). When independent writers might collide, the primary model can select worktree isolation; first-party machinery regulates cross-child file interference and returns merge/conflict reports for a new parent decision (`S2=A`, narrowly limited to the optional isolated-batch path). The parent model may inspect every active background child and selectively cancel a current commitment (`S3=A`). The TUI list lacks a corresponding human selective-stop path, so it does not add `(P)`. A separate independent operational auditor or identity-level governor was not found (`S3*=—`, `S5=—`). Agent-authored persisted skills chosen for anticipated reuse and automatically exposed to later turns establish a bounded future capability loop (`S4=A`); automatic memory consolidation alone is not the witness.

## S1 — Operations

- State: A
- Function: handle user coding and assistant requests by selecting and executing tools, examining failures and iterating; optionally delegate independently executed subtasks.
- Disturbance / variety regulated: varying user goals, source/test feedback, command failures, retrieved context, tool permission outcomes and provider-generated uncertainty.
- Decisive decision or feedback right: the primary and child models select tool calls and subsequent operations from messages/results; the runtime executes and reports those calls.
- Decision owner: configured model-backed `runAgent` instance, with child `runAgent` loops as separately deciding S1 units.
- Supporting / enforcement mechanisms: `streamText` provider adapter, tool schemas, budgets, permissions, context assembly, local files/Git/web tools and child context isolation.
- Closure path: task/context → model tool choice → tool result or refusal → next model turn / delegated child / completion.
- Boundary reachability: CLI/headless/gateway handlers call `runAgent`; exposed task tools import and call the same loop for each child, in the installed product.
- Why this is / is not agent-owned: the model selects substantive task execution and repairs, whereas the TS runtime and policy gates only transport/enforce the chosen steps.
- Evidence: [loop](https://github.com/Sir-chawakorn/sanook-cli/blob/c7bbede1823b68f4c48959dc34d864a5404762c8/src/loop.ts), [CLI](https://github.com/Sir-chawakorn/sanook-cli/blob/c7bbede1823b68f4c48959dc34d864a5404762c8/src/bin.ts), [task](https://github.com/Sir-chawakorn/sanook-cli/blob/c7bbede1823b68f4c48959dc34d864a5404762c8/src/tools/task.ts), [mock loop test](https://github.com/Sir-chawakorn/sanook-cli/blob/c7bbede1823b68f4c48959dc34d864a5404762c8/src/integration.test.ts).
- Basis: frozen source, static call wiring and native mock tests; no live inference.
- Confidence: high in executable agent constructor, not in model effectiveness.
- Caveats: real providers, external services and interactive quality were not tested; the selected integration suite had environment-sensitive failures.

## S2 — Coordination

- State: A
- Function: prevent independent concurrently writing child S1 units from corrupting the same project working tree, and return integration collisions to a coordinating parent.
- Disturbance / variety regulated: overlapping edits and incompatible file changes produced by parallel model-backed children.
- Decisive decision or feedback right: the primary model can choose `task_parallel` with `isolate=true` for a particular set of writers; after separate execution, first-party patch application reports whether each result was integrated, so the parent can change the next task/repair.
- Decision owner: the primary model for whether and how to isolate the delegated batch and subsequent response to reported conflicts; deterministic worktree logic for enforcement and sequential merge order.
- Supporting / enforcement mechanisms: private Git worktrees, child-local `cwd`/async contexts, diff capture, `git apply --check --3way`, sequential apply and failure reporting.
- Closure path: model classifies potentially overlapping parallel work → selects isolated batch → separate children operate on private trees → diffs applied in a fixed order → merge/conflict notes return as parent-model tool output → later operational decisions can change.
- Boundary reachability: `taskParallelTool` directly calls `runIsolated` when the model chooses `isolate`; `runIsolated` invokes `runInWorktrees`, and the registered parent agent can consume its merged outcome.
- Why this is / is not agent-owned: the discretionary choice to use isolation and what to do with collisions belongs to the model, not to a fixed supervisor. This supports bounded A for the explicitly isolated batch, not universal automatic coordination; the patch merge itself is deterministic and semantic conflict resolution is not proven.
- Evidence: [parallel and isolation tool](https://github.com/Sir-chawakorn/sanook-cli/blob/c7bbede1823b68f4c48959dc34d864a5404762c8/src/tools/task.ts), [worktree](https://github.com/Sir-chawakorn/sanook-cli/blob/c7bbede1823b68f4c48959dc34d864a5404762c8/src/worktree.ts), [offline tests](https://github.com/Sir-chawakorn/sanook-cli/blob/c7bbede1823b68f4c48959dc34d864a5404762c8/src/worktree.test.ts).
- Basis: executable first-party interference guard and tests with injected fake child work.
- Confidence: medium-high for the optional interference-specific path; no live model choice measured.
- Caveats: the default non-isolated parallel path leaves writers sharing a workspace; `isolate` must be selected, and patch conflicts are reported for later resolution rather than autonomously semantically merged.
- Distinct S1 units: two or more independent model-backed child `runAgent` loops with writable toolsets and separate contexts.
- Inter-S1 disturbance: concurrent writes to overlapping source paths and contradictory proposed edits of the shared project.
- Attenuating coordination relation: model-selected `isolate=true` creates a separate Git worktree for each writer, then serially checks/applies returned diffs.
- Feedback into subsequent S1 behaviour: each isolated task returns success/failure and patch conflict notes, allowing the primary model to choose follow-up work after the batch.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: dedicated code isolates an actual multi-writer conflict class and explicitly checks integration collisions, changing the shared filesystem's interference topology.

## S3 — Inside-and-now control

- State: A
- Function: maintain a whole-session picture of currently running background child commitments and selectively stop work that is no longer justified.
- Disturbance / variety regulated: unnecessary, prolonged or mistaken active child commitments consuming bounded task slots and attention.
- Decisive decision or feedback right: the parent model obtains the entire `TaskRegistry` via `task_status`, selects a running child id and calls `task_cancel` when current commitments should change.
- Decision owner: parent model for selection/intervention; registry `AbortController` for termination enforcement.
- Supporting / enforcement mechanisms: process-scoped registry with states, start/end timestamps, `task_spawn`, `task_collect`, `task_status`, `task_cancel`, shared budgets and abort signals.
- Closure path: current child roster → parent judgment → targeted `task_cancel` → child abort/status update → subsequent model status/collection and reprioritized work.
- Boundary reachability: all four tools are in the registered parent `tools` map, and `TaskRegistry` survives successive tool calls within one ordinary session; model-facing instructions advertise these control actions.
- Why this is / is not agent-owned: choosing which of all current child commitments to stop is a discretionary parent-model decision; a fixed concurrency ceiling or abort API by itself would not establish S3.
- Evidence: [task status/cancel](https://github.com/Sir-chawakorn/sanook-cli/blob/c7bbede1823b68f4c48959dc34d864a5404762c8/src/tools/task.ts), [registry](https://github.com/Sir-chawakorn/sanook-cli/blob/c7bbede1823b68f4c48959dc34d864a5404762c8/src/orchestrate.ts), [native task tests](https://github.com/Sir-chawakorn/sanook-cli/blob/c7bbede1823b68f4c48959dc34d864a5404762c8/src/tools/task.test.ts).
- Basis: tool and registry wiring, selected offline tests.
- Confidence: medium-high for the narrow session roster/intervention circuit.
- Caveats: no demonstrated model optimization of priorities or resources beyond selective background-task cancellation; TUI tasks overlay lists and inspects but has no direct selective-stop operation, so parent mode is not claimed.
- Whole-system current view: `task_status` lists every retained background job in the local session with id, state, duration and description.
- Current-control decision scope: the parent model can terminate a selected currently running child via `task_cancel` and reconsider subsequent commitments; it does not govern external agents or separate installations.

## S3* — Complementary audit

- State: —
- Function: no materially complementary, independently deciding audit of the coding organization was established in the supported first-party session.
- Disturbance / variety regulated: undetected errors could remain after ordinary tests, child reports and memory retrieval.
- Decisive decision or feedback right: no distinct auditor is first-party wired to acquire independent evidence, judge an operational claim and return an audit finding to a corrective control path.
- Decision owner: the same primary agent can request ordinary child research/review, and the user can inspect reports; neither constitutes a shipped complementary audit body.
- Supporting / enforcement mechanisms: generic `task`/`task_parallel`, code tests, memory health `brain-doctor`/`brain-eval` and TUI status information.
- Closure path: task and test outputs re-enter ordinary S1 processing; no separate first-party independent audit→finding→control return is defined.
- Why this is / is not agent-owned: generic fresh child delegation does not supply an explicitly distinct audit judgment, access policy or substantive independence, and deterministic memory metrics are not an agent-owned complement to operational control.
- Evidence: [task delegation](https://github.com/Sir-chawakorn/sanook-cli/blob/c7bbede1823b68f4c48959dc34d864a5404762c8/src/tools/task.ts), [brain evaluation](https://github.com/Sir-chawakorn/sanook-cli/blob/c7bbede1823b68f4c48959dc34d864a5404762c8/src/brain-eval.ts), [CLI](https://github.com/Sir-chawakorn/sanook-cli/blob/c7bbede1823b68f4c48959dc34d864a5404762c8/src/bin.ts).
- Basis: first-party child tools and native diagnostic routes inspected.
- Confidence: medium-high within the supported local boundary.
- Caveats: an operator could manually prompt a separate subagent for review; that external composition is not claimed as shipped S3*.

### Absence scope

- Surfaces inspected: task and parallel subagent constructors, tool role limits, brain doctor/eval commands, test integration and TUI background-job views.
- Plausible first-party paths checked: separately prompted `task` as reviewer, deterministic memory evaluation as auditor and ordinary compiler/test output as independent evidence.
- Why no material first-party path remains: no audit-specific independent access/judgment/return circuit is shipped; these paths are generic delegation, diagnostics or operational feedback.

## S4 — Outside-and-then intelligence

- State: A
- Function: alter the future repertoire of the locally installed agent by generalizing successful recurring procedures into reusable skills.
- Disturbance / variety regulated: future recurring task types and the cost/error risk of reconstructing a multi-step procedure from scratch every time.
- Decisive decision or feedback right: the primary model decides after a successful multi-step task whether the procedure is likely to recur, invents a general runbook and chooses to call `create_skill`; the operator permission gate may approve/deny persistence in `ask` mode.
- Decision owner: primary model in the first-party supported automatic-write mode for prospective skill selection/content; deterministic store for saving and making it available on later tasks.
- Supporting / enforcement mechanisms: model system instruction about reusable successful work, `create_skill` schema, slug-validated global skill files, `loadSkills`, `find_skills` and `skill` retrieval into new session prompt context.
- Closure path: observed completed work plus inferred future repetition → model generalizes/chooses a new capability → `saveSkill` persists it → later `runAgent` loads its description and can follow the body → subsequent operating repertoire changes.
- Boundary reachability: the primary `runAgent` registers `create_skill`, instruction explicitly requests prospective reusable skill creation and the supported `--yes`/automatic permission mode permits persistence; new sessions invoke `loadSkills` and expose saved skills to their models.
- Why this is / is not agent-owned: the prospective choice of what future capability is worth installing and its procedural content belongs to the model; fixed skill loading, saved memory and cache are infrastructure rather than the adaptation decision itself.
- Evidence: [agent future-use instruction](https://github.com/Sir-chawakorn/sanook-cli/blob/c7bbede1823b68f4c48959dc34d864a5404762c8/src/loop.ts), [skill creation](https://github.com/Sir-chawakorn/sanook-cli/blob/c7bbede1823b68f4c48959dc34d864a5404762c8/src/tools/skill.ts), [skill store/reload](https://github.com/Sir-chawakorn/sanook-cli/blob/c7bbede1823b68f4c48959dc34d864a5404762c8/src/skills.ts), [offline roundtrip](https://github.com/Sir-chawakorn/sanook-cli/blob/c7bbede1823b68f4c48959dc34d864a5404762c8/src/integration.test.ts).
- Basis: explicit longitudinal future-use instruction, model-selectable durable capability writer and deterministic roundtrip tests.
- Confidence: medium for bounded capability adaptation; no live-model autonomous learning outcome was measured.
- Caveats: prospective signal is inferred expected task recurrence rather than a broad external market/environment scan; the default `ask` permission mode may require an operator approval, and no skill-quality improvement was empirically demonstrated.
- External distinction: a user/project-originated task and its execution outcomes reveal a repeatable work pattern beyond the agent's built-in procedure repertoire.
- Future / prospective distinction: the primary model judges after a successful multi-step execution that the same type of procedure is likely to recur in later tasks.
- Adaptation option generated: the model decides whether to codify an additional skill and chooses its name, applicable conditions and procedural body.
- Path back into current capability / S3: `saveSkill` installs the global capability; later `loadSkills` advertises it to subsequent `runAgent` sessions and `skill` retrieves its steps for future S1 execution.

## S5 — Policy and identity

- State: —
- Function: no governing identity or ultimate-policy institution with its own issue/decision/return loop is established for a local Sanook installation.
- Disturbance / variety regulated: changing purpose, legitimacy and fundamental organizational tradeoffs are outside the shipped current-task/permission circuits.
- Decisive decision or feedback right: no first-party S5 body arbitrates ultimate purpose or identity and binds subsequent lower-system choices; the user chooses tactical permission/configuration.
- Decision owner: operator for per-tool approval and model/config settings, upstream maintainers for product direction outside the declared boundary.
- Supporting / enforcement mechanisms: `ask`/`auto` tool gating, trust scope, personality and goals configuration, environment secrets and gateway access boundaries.
- Closure path: approvals and configuration affect immediate tool execution; no complete identity-policy question → ultimate legitimate decision → returned governing constraint is present.
- Why this is / is not agent-owned: permission enforcement and persona injection do not constitute an organization-level ultimate-policy authority.
- Evidence: [approval gate](https://github.com/Sir-chawakorn/sanook-cli/blob/c7bbede1823b68f4c48959dc34d864a5404762c8/src/approval.ts), [CLI config](https://github.com/Sir-chawakorn/sanook-cli/blob/c7bbede1823b68f4c48959dc34d864a5404762c8/src/bin.ts), [agent prompt](https://github.com/Sir-chawakorn/sanook-cli/blob/c7bbede1823b68f4c48959dc34d864a5404762c8/src/loop.ts).
- Basis: inspected policy, configuration, identity hints and installed operating paths.
- Confidence: medium-high for the local session boundary.
- Caveats: legitimate human oversight exists but is principally tactical tool approval, not proven S5 parent governance.

### Absence scope

- Surfaces inspected: permission/trust logic, user persona/config and remembered goals, gateway/scheduler, local operating tools and maintainer/project docs.
- Plausible first-party paths checked: `ask` mode as parent S5, personality/goal injection as durable identity, self-generated skills as constitutional policy and repository maintainers as installed governance.
- Why no material first-party path remains: these are operator preferences, action gating, prospective task procedures or adjacent upstream decisions; none closes an ultimate-policy authority/return circuit for the assessed local organization.

## Distributed OSS parent arrangement

Public contributors and maintainers govern the upstream source project, but their GitHub/CI decisions are not a first-party current-control, adaptation or identity owner of an independent locally installed Sanook coding organization.

## Self-hosted and non-human modes

The parent model owns local task selection, isolated-writer coordination, selected background cancellation and future runbook creation in the supported automatic-permission mode. An attended operator can approve or deny mutating calls in `ask` mode and inspect the tasks hub, but task inspection has no direct operator cancellation action and approval is a tactical gate, so no parent S3/S4/S5 mode is inferred from it.

## Recursion

The primary session and separate model-backed subagents are distinct S1 cells inside a single Sanook process. The bounded `TaskRegistry` and worktrees provide internal S2/S3 circuits, not governance of external providers, other installations or the upstream OSS developer community.

## Variety and escalation

Tool results feed S1 retry. Worktree isolation changes concurrent-writer collision exposure but does not ensure all patches integrate. Current-task cancellation can selectively remove a background commitment. Durable skills may change future procedure selection; user approval or unresolved Git conflicts remain explicit limitations rather than independent S5 or S3* bodies.

## Evidence gaps

- Frozen revision `c7bbede`: `npm run typecheck` **PASS**. Focused `src/worktree.test.ts`, `src/tools/task.test.ts`, `src/skills.test.ts` and `src/auto-maintain.test.ts` **79/79 PASS**, all native/mock/script-only, no live model or external provider execution.
- `npm ci --ignore-scripts --no-audit --no-fund` was blocked by the upstream package-lock/manifest mismatch (missing optional `node-pty@1.1.0` and `node-addon-api@7.1.1`). A lockfile-preserving fallback `npm install --package-lock=false --ignore-scripts --no-save` installed dependencies without editing the frozen repository.
- Broader selected four-file suite (`worktree`, `task`, `integration`, `approval`) yielded **57 passed, 3 failed, 4 skipped**. Failures were in integration fixtures checking a synthetic Windows `Path`, mocked loop file-write probe and project-trust hook condition; they are not represented as a fully passing suite. The isolated worktree/task/skill/auto-maintain suite passed.
- Positive S2 uses a model-selectable optional isolated-writer path, not an unconditional guard. The model's real selection quality, race conditions under live providers and semantic conflict resolution are unmeasured.
- Positive S3 is bounded to a whole-session background roster and selective cancellation, not an organization-wide resource governor. The UI's tasks hub does not expose parent-owned cancel.
- Positive S4 rests on structurally wired model-authored reusable procedures and the future skill discovery loop. No live LLM self-improvement outcome or measured before/after capability gain is asserted.

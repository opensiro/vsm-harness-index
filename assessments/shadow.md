---
harness_id: shadow
project_name: Shadow
repository: https://github.com/ishaan1013/shadow
review_ref: 96e7b187951d66740dcd7d0bf3d5f94f5d09ed41
reviewed_at: 2026-10-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-04
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Shadow

## Review boundary

- System in focus: the first-party Shadow background coding-agent product in `ishaan1013/shadow` at frozen revision `96e7b187951d66740dcd7d0bf3d5f94f5d09ed41`, including the server-side model/tool loop, task/workspace lifecycle, file/terminal/search tools, repository memory, Git commit/PR delivery and local/remote execution modes.
- Purpose and identity: perform software-engineering work against a selected GitHub repository inside a task-scoped workspace, persist task/repository context, and deliver code changes through Shadow-managed branches/commits/PRs.
- Relevant environment: user task and follow-ups, repository/filesystem/Git state, terminal and search output, model-provider responses, task status, repository memories, optional semantic index/wiki state, and GitHub delivery state.
- Standard-distribution boundary: Shadow's server agent loop, task initialization, local/remote workspace execution, built-in tools, memory service, task status and Git/PR delivery are inside. External model providers, GitHub itself, Kubernetes/Kata/QEMU substrate and target-project governance are dependencies/environment.
- Credited operating / distribution surfaces: `README.md`; `apps/server/src/agent/chat.ts`; `apps/server/src/agent/llm/streaming/stream-processor.ts`; `apps/server/src/agent/tools/index.ts`; `apps/server/src/services/memory-service.ts`; task-initialization surfaces under `apps/server/src/initialization/`; execution/workspace abstractions; and first-party Git/PR services.
- Adjacent first-party surfaces excluded from ownership: repository-development CI, maintainer governance, frontend rendering by itself, passive telemetry, generated Shadow Wiki/indexing unless it enters a function-specific decision loop, and infrastructure isolation without a same-recursion coordination relation.
- First-party operating / deployment modes considered: local execution; remote Kata/QEMU-isolated task execution; background coding tasks; persistent task follow-ups; model/tool coding loop; repository memories; semantic search when available; automatic commit/push and optional PR creation.
- Recursion level: one Shadow coding task/session organization. The model-backed coding actor is the focal S1. Independent Shadow tasks/workspaces are not presumed to be production S1 units of one higher-level organization merely because the platform can host many tasks.
- Reviewed revision: `96e7b187951d66740dcd7d0bf3d5f94f5d09ed41`.
- Observation date: 2026-10-04.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Shadow ships a real first-party coding loop rather than only a launcher. `StreamProcessor` invokes the selected model with the current conversation, first-party tools and a `MAX_STEPS` bound of 100. AI SDK tool execution feeds tool results back into the same multi-step stream, while `ChatService` persists messages, tracks task state and commits resulting workspace changes.

The tool surface includes file reads/edits/deletes, grep/file/semantic search, terminal execution, TODO management and repository-scoped memory operations. Remote mode executes tasks in isolated Kata/QEMU workspaces; local mode executes directly in a prepared workspace. Task initialization creates or restores that environment, while later follow-ups can reactivate an inactive task and continue work.

Repository memories are persistent across tasks for the same user/repository. The model can add/list/remove memories, and `MemoryService` can automatically format stored memories into later system prompts. This materially extends cross-task context, but persistence and model-authored notes alone do not establish a prospective S4 intelligence/adaptation function.

After an agent response, Shadow can detect changes, generate a commit message, commit and push the task branch, and optionally create/update a draft pull request. Those delivery mechanisms close the operational software-engineering path but do not create a distinct complementary reviewer or whole-system manager.

Primary evidence:

- [`README.md`](https://github.com/ishaan1013/shadow/blob/96e7b187951d66740dcd7d0bf3d5f94f5d09ed41/README.md)
- [`apps/server/src/agent/llm/streaming/stream-processor.ts`](https://github.com/ishaan1013/shadow/blob/96e7b187951d66740dcd7d0bf3d5f94f5d09ed41/apps/server/src/agent/llm/streaming/stream-processor.ts)
- [`apps/server/src/agent/chat.ts`](https://github.com/ishaan1013/shadow/blob/96e7b187951d66740dcd7d0bf3d5f94f5d09ed41/apps/server/src/agent/chat.ts)
- [`apps/server/src/agent/tools/index.ts`](https://github.com/ishaan1013/shadow/blob/96e7b187951d66740dcd7d0bf3d5f94f5d09ed41/apps/server/src/agent/tools/index.ts)
- [`apps/server/src/services/memory-service.ts`](https://github.com/ishaan1013/shadow/blob/96e7b187951d66740dcd7d0bf3d5f94f5d09ed41/apps/server/src/services/memory-service.ts)
- [`apps/server/src/github/pull-requests.ts`](https://github.com/ishaan1013/shadow/blob/96e7b187951d66740dcd7d0bf3d5f94f5d09ed41/apps/server/src/github/pull-requests.ts)

## Operational model

A Shadow task is initialized against a repository/branch and receives an isolated or local workspace. The main model sees the current conversation/system context and tool schemas. It selects file/search/terminal/TODO/memory actions; Shadow executes them, returns results into the same AI SDK multi-step run, and repeats until model completion, cancellation/error or the step bound.

The resulting workspace is tracked as a task-scoped branch. Shadow may automatically commit/push modifications and create or update a draft pull request. Task messages, status and repository memories remain available for later follow-ups.

## S1 — Operations

- State: A
- Function: perform environment-facing software-engineering work in a task-scoped repository workspace and deliver resulting changes.
- Disturbance / variety regulated: heterogeneous user requests, repository structure, file/Git state, tool/terminal/search output, provider responses, implementation failures, context/history and changing task evidence.
- Decisive decision or feedback right: choose which files/evidence to inspect, what terminal/search/edit action to execute, how to revise work from tool results, what TODO/memory action to take and when to stop responding.
- Decision owner: the model-backed Shadow coding agent in the first-party `streamText` multi-step loop.
- Supporting / enforcement mechanisms: first-party tool schemas/executors; task/workspace initialization; local/remote execution abstraction; TODOs; repository memory; semantic search; task status; checkpoints/history; Git commit/push and PR delivery.
- Closure path: task + workspace/session context → model chooses a tool/action → Shadow executes it → result is returned inside the same multi-step model stream → model chooses subsequent action or completes → Shadow persists/delivers resulting workspace changes.
- Boundary reachability: normal Shadow task execution directly wires the model to built-in coding tools with `maxSteps: 100`; no downstream orchestration code is required.
- Why this is / is not agent-owned: removing the model-backed actor leaves workspace/tool/storage/delivery machinery but removes the open-ended coding judgment that selects and sequences work.
- Evidence: [`stream-processor.ts`](https://github.com/ishaan1013/shadow/blob/96e7b187951d66740dcd7d0bf3d5f94f5d09ed41/apps/server/src/agent/llm/streaming/stream-processor.ts); [`tools/index.ts`](https://github.com/ishaan1013/shadow/blob/96e7b187951d66740dcd7d0bf3d5f94f5d09ed41/apps/server/src/agent/tools/index.ts); [`chat.ts`](https://github.com/ishaan1013/shadow/blob/96e7b187951d66740dcd7d0bf3d5f94f5d09ed41/apps/server/src/agent/chat.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: model inference is provider-backed; Shadow is credited for the first-party agent/tool/feedback organization and execution boundary.

## S2 — Coordination

- State: —
- Function: no material same-recursion inter-S1 coordination function was established.
- Disturbance / variety regulated: not established at S2 level. Shadow isolates task workspaces, but reviewed evidence does not establish distinct production S1 units inside one task organization whose mutual interference is specifically attenuated by a first-party coordination relation.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: per-task workspaces/branches; Kata/QEMU isolation; task initialization/status; queued task actions.
- Closure path: not applicable; no distinct-S1 interference → coordination response → changed subsequent S1 behavior loop was found.
- Why this is / is not agent-owned: workspace isolation is primarily task/environment containment. Independent hosted tasks are not promoted into one organization without evidence of a shared same-recursion operational objective and interference relation.
- Evidence: [`README.md`](https://github.com/ishaan1013/shadow/blob/96e7b187951d66740dcd7d0bf3d5f94f5d09ed41/README.md); [`chat.ts`](https://github.com/ishaan1013/shadow/blob/96e7b187951d66740dcd7d0bf3d5f94f5d09ed41/apps/server/src/agent/chat.ts).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: a larger deployment could coordinate multiple Shadow tasks externally; that organization is outside this task-level assessment.

### Absence scope

- Surfaces inspected: task/workspace isolation; branches; local/remote execution; queued actions; initialization; task status; background services; agent/tool loop.
- Plausible first-party paths checked: multiple simultaneous tasks; isolated VMs; queued messages/stacked task actions; branch separation; shared repository context.
- Why no material first-party path remains: the located mechanisms isolate/manage independent task executions but do not reconstruct a concrete same-recursion inter-S1 interference condition with a coordination decision and feedback relation.

## S3 — Inside-and-now control

- State: —
- Function: no distinct whole-organization current-control function was established.
- Disturbance / variety regulated: task status, initialization state, active streams, queued actions, cleanup, workspace availability and background services are tracked, but these are lifecycle/runtime controls around the focal task rather than whole-system operational management.
- Decisive decision or feedback right: not established at S3 level.
- Decision owner: not established.
- Supporting / enforcement mechanisms: task statuses; active stream/cancel/queue maps; initialization engine; cleanup scheduling; background service manager; TODO state; Git/PR state.
- Closure path: not applicable; no whole-system current view plus substantive organization-wide resource/priority/commitment intervention loop was reconstructed.
- Why this is / is not agent-owned: the model owns coding decisions inside S1; task lifecycle state and scheduling are deterministic/operator-driven mechanisms.
- Evidence: [`chat.ts`](https://github.com/ishaan1013/shadow/blob/96e7b187951d66740dcd7d0bf3d5f94f5d09ed41/apps/server/src/agent/chat.ts); [`README.md`](https://github.com/ishaan1013/shadow/blob/96e7b187951d66740dcd7d0bf3d5f94f5d09ed41/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: real-time task tracking is operationally useful but does not by itself satisfy the stronger S3 closure.

### Absence scope

- Surfaces inspected: task status/progress; queued actions; active streams; initialization/reinitialization; TODO management; background wiki/indexing; auto-commit/PR lifecycle.
- Plausible first-party paths checked: server orchestrator as manager; task-status dashboard; TODO state as whole-current view; stacked/queued tasks; automatic PR delivery.
- Why no material first-party path remains: these surfaces track or sequence one task's lifecycle or independent task executions; no distinct whole-organization current-control actor/decision loop was found.

## S3* — Complementary audit

- State: —
- Function: no material first-party complementary audit actor/path distinct from the producing S1 was established.
- Disturbance / variety regulated: ordinary tool errors, command results and generated PR metadata can expose problems, but no separate reviewer independently audits the producing agent's correctness/completion claim.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: command/tool validation; Git diff/commit generation; PR snapshot creation; task status; ordinary model self-observation.
- Closure path: not applicable; no producing-S1 claim → complementary independent evidence path → audit verdict → corrective return loop was found.
- Why this is / is not agent-owned: command/security validation is deterministic enforcement and PR generation summarizes/delivers changes; neither is a separate autonomous complementary auditor.
- Evidence: [`chat.ts`](https://github.com/ishaan1013/shadow/blob/96e7b187951d66740dcd7d0bf3d5f94f5d09ed41/apps/server/src/agent/chat.ts); [`pull-requests.ts`](https://github.com/ishaan1013/shadow/blob/96e7b187951d66740dcd7d0bf3d5f94f5d09ed41/apps/server/src/github/pull-requests.ts).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: a user can review the draft PR externally; that external review is not a first-party autonomous S3* path.

### Absence scope

- Surfaces inspected: tool-result validation; command security; task completion/status; commit generation; PR generation/snapshots; background wiki/indexing; memory.
- Plausible first-party paths checked: automatic tests as reviewer; PR generation as review; separate model validation; background code understanding/indexing; frontend diff/status surfaces.
- Why no material first-party path remains: no distinct model/auditor is wired to independently inspect the producer's result and return a semantic verdict into the active coding loop.

## S4 — Intelligence / adaptation

- State: —
- Function: no material outside-and-future intelligence/adaptation loop was established.
- Disturbance / variety regulated: repository-specific knowledge can persist across tasks through memories, and semantic/wiki context can improve later operation, but no explicit prospective environmental-modeling and adaptation-selection function was reconstructed.
- Decisive decision or feedback right: not established at S4 level.
- Decision owner: not established.
- Supporting / enforcement mechanisms: `add_memory`, `list_memories`, `remove_memory`; automatic memory injection into later prompts; Shadow Wiki; optional semantic indexing; persisted task history.
- Closure path: not applicable; no external/future distinction → adaptation-option generation → autonomous selection → persistent organizational capability/strategy change → later operation loop was found.
- Why this is / is not agent-owned: the coding agent may decide to save useful facts, and those facts are later reused, but remembering operational knowledge is not itself the stronger prospective adaptation function.
- Evidence: [`tools/index.ts`](https://github.com/ishaan1013/shadow/blob/96e7b187951d66740dcd7d0bf3d5f94f5d09ed41/apps/server/src/agent/tools/index.ts); [`memory-service.ts`](https://github.com/ishaan1013/shadow/blob/96e7b187951d66740dcd7d0bf3d5f94f5d09ed41/apps/server/src/services/memory-service.ts); [`README.md`](https://github.com/ishaan1013/shadow/blob/96e7b187951d66740dcd7d0bf3d5f94f5d09ed41/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: persistence is substantial; the negative classification is specifically about S4's prospective adaptation closure, not about whether Shadow learns/reuses repository facts colloquially.

### Absence scope

- Surfaces inspected: repository memories; automatic prompt injection; Shadow Wiki; semantic indexing/search; task history; model/provider configuration; initialization.
- Plausible first-party paths checked: model-authored memories as learning; wiki/index generation as environment model; cross-task memory reuse; autonomous configuration/capability changes.
- Why no material first-party path remains: located paths preserve/retrieve current or historical repository knowledge, but do not establish an autonomous outside/future adaptation decision that persistently changes organizational strategy/capability.

## S5 — Policy and identity

- State: —
- Function: no material identity/ultimate-policy decision loop was established.
- Disturbance / variety regulated: custom rules, command security, workspace boundaries, user settings, model/provider choice and auto-PR settings constrain operation, but they are task/runtime policy rather than identity-level governance.
- Decisive decision or feedback right: not established for a genuine identity/ultimate-policy issue.
- Decision owner: user/deployment/project configuration for relevant constraints; deterministic Shadow mechanisms enforce those selections.
- Supporting / enforcement mechanisms: custom rules; command validation; workspace path protection; user settings; model selection; local/remote mode; auto-PR option.
- Closure path: not applicable at S5 level; no identity/policy conflict → legitimate ultimate authority → authoritative decision → returned organizational operation loop was established.
- Why this is / is not agent-owned: the coding model does not own Shadow's ultimate policy/identity boundary, and enforcement of configured restrictions is not itself S5.
- Evidence: [`README.md`](https://github.com/ishaan1013/shadow/blob/96e7b187951d66740dcd7d0bf3d5f94f5d09ed41/README.md); [`chat.ts`](https://github.com/ishaan1013/shadow/blob/96e7b187951d66740dcd7d0bf3d5f94f5d09ed41/apps/server/src/agent/chat.ts).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: a broader organization may govern Shadow through external policy; that parent is not imported without a function-specific closed loop.

### Absence scope

- Surfaces inspected: custom code-generation rules; command security; workspace containment; user settings; model/provider selection; auto-PR controls; deployment mode.
- Plausible first-party paths checked: user settings as parent policy; custom rules as identity; command-security vetoes; deployment configuration; PR policy.
- Why no material first-party path remains: these are configured operating constraints and deterministic enforcement, not a first-party identity/ultimate-policy adjudication function.

## Distributed OSS parent arrangement

The public repository's maintainer/contributor process is outside the deployed task-level Shadow organization. GitHub PR delivery can expose work to external human governance, but the external review/governance path is not credited as a first-party S3*/S5 owner.

## Self-hosted and non-human modes

Shadow can execute locally or in remote isolated environments and can continue background coding with automated commit/push/PR delivery. The main coding loop remains autonomous S1. Environment isolation, lifecycle automation and unattended delivery do not promote the absent metasystem functions.

## Recursion

The focal recursion is one Shadow coding task. A task has one primary model/tool coding actor. Multiple independently hosted tasks/workspaces are treated as separate organizations unless first-party evidence reconstructs a higher-level coordination/control organization among them.

## Variety and escalation

Shadow attenuates operational variety through sandbox/workspace isolation, command validation, task status, retries/tool feedback, TODOs, persistent context, checkpoints/history, semantic search and delivery automation. These mechanisms strengthen S1 robustness but do not independently establish S2/S3/S3*/S4/S5.

## Evidence gaps

No `?` state is required at the frozen revision. Primary exact-ref implementation establishes the S1 model/tool closure and provides sufficient surface coverage to bound the most plausible stronger claims: workspace isolation, task orchestration, PR delivery, persistent memory and configured policy.

## Assessment summary

Shadow closes autonomous S1 through its first-party bounded model/tool coding loop with task-scoped workspace execution and Git delivery. The reviewed standard distribution does not establish same-recursion S2, whole-system S3, complementary autonomous S3*, prospective S4, or identity-level S5. Persistent repository memory is credited as a strong S1 context mechanism rather than promoted to S4 without a future-oriented adaptation loop.

**Vector:** A · — · — · — · — · —

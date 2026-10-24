---
harness_id: cluxmate
project_name: CluxMate
repository: https://github.com/r1c7/CluxMate
review_ref: c3d5d84bbb6149ebdd2bd0ec7a8fa7817a984192
reviewed_at: 2026-10-23
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: A
autonomy_s4: A
autonomy_s5: P
---

# CluxMate

## Review boundary

- System in focus: one installed/self-hosted CluxMate coding-agent workspace and its parent agent, delegated child agents, current session and durable local context; not the upstream project-maintainer organization.
- Purpose and identity: answer software-engineering requests by inspecting code, choosing edits/tool calls, delegating bounded sub-tasks, testing and reporting results.
- Relevant environment: a user-selected project directory, Python agent core, external configured OpenAI-compatible model endpoint, files/shell/LSP/web/MCP tools and an optional Electron desktop shell.
- Standard-distribution boundary: shipped Python CLI/REPL/Textual TUI/Electron bridge with the same `AgentLoop`, `AgentBuilder`, built-in child types, model prompts, native memory/permission/scheduler mechanisms.
- Credited operating / distribution surfaces: `cluxmate/core/agent.py`, `builder.py`, `subagents.py`, `subagent_scheduler.py`, `completion_audit.py`, `permissions.py`, `memory.py`, `retrieval_memory.py`, `session_log.py`, `checkpoints.py`, `tools/task.py`, `tools/update_memory.py`, the shipped Jinja prompts and CLI/TUI/desktop controls.
- Adjacent first-party surfaces excluded from ownership: project contributor commits/issues; source repository `AGENTS.md` governing contributors; Python/Electron unit and integration tests, screenshots and release scripts. Tests corroborate mechanisms but do not operate a deployed agent; third-party LLM provider is a dependency, not an independently evidenced OpenSiro organizational actor.
- First-party operating / deployment modes considered: model-driven coding and delegation; read-only `plan`, supervised `default`, `acceptEdits`, explicitly unsandboxed `yolo`; local parent-controlled UI/CLI; optional enabled retrieval memory and custom agent types.
- Recursion level: local agent-assisted software-delivery workspace/session; the delegated S1 children are operations within this recursion, not automatically independently viable organizations.
- Reviewed revision: `r1c7/CluxMate@c3d5d84bbb6149ebdd2bd0ec7a8fa7817a984192` (frozen by Index #1884).
- Observation date: 2026-10-23.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The Python `AgentLoop` repeatedly obtains model decisions, mediates risk-tiered tool approvals, dispatches tools and captures results in an event-sourced session log. `AgentBuilder` loads project/user context and registers parent-only memory, task tracking and user-question tools. The same core is exposed via terminal clients and the desktop JSON-RPC bridge. Built-in `general-purpose`, `explore` and `reviewer` child types have explicit tool restrictions, independent child turns and logs. The scheduler bounds parallel child execution to four (maximum two writers), normalizes write-path claims, serializes overlapping scopes and avoids nested-slot deadlock. Completed changes are checked by a separate evidence-oriented spec reviewer when dispatched by the parent model. The host also performs narrower advisory completion-claim reconciliation; its logs do not in themselves prove task correctness. User decisions on mode, persistent permissions, trust, sandbox grants and long-term instructions constrain subsequent operation.

Primary anchors: [README](https://github.com/r1c7/CluxMate/blob/c3d5d84bbb6149ebdd2bd0ec7a8fa7817a984192/README.md), [agent loop](https://github.com/r1c7/CluxMate/blob/c3d5d84bbb6149ebdd2bd0ec7a8fa7817a984192/cluxmate/core/agent.py), [builder](https://github.com/r1c7/CluxMate/blob/c3d5d84bbb6149ebdd2bd0ec7a8fa7817a984192/cluxmate/core/builder.py), [scheduler](https://github.com/r1c7/CluxMate/blob/c3d5d84bbb6149ebdd2bd0ec7a8fa7817a984192/cluxmate/core/subagent_scheduler.py), [subagents](https://github.com/r1c7/CluxMate/blob/c3d5d84bbb6149ebdd2bd0ec7a8fa7817a984192/cluxmate/core/subagents.py).

## Operational model

The user supplies an engineering objective and constraints. The parent model owns selection of implementation steps, tool usage, child task partition, declared write scopes and disposition of independent review findings; host enforcement carries those choices and reports denial/child status back. Child model agents exercise operational discretion over assigned scoped work. The parent human can select task/mode, inspect current agent/tree/todo/diffs, intervene or stop, control durable memory and policy, and use session-scoped checkpoints. A reviewer has its own fresh evidence-gathering path to the workspace, but the default model/provider and parent-selected review task remain correlated with ordinary operation. This review credits model autonomy in the configured supported mode, not actual LLM performance measured by an experiment.

## S1 — Operations

- State: A
- Function: execute coding, inspection, file modification and verification requests; delegated children independently pursue bounded subtasks.
- Disturbance / variety regulated: changing codebase requirements, missing context, tool errors, differing file structure and failed checks.
- Decisive decision or feedback right: select an action/tool, evaluate the result, change the next action and decide when to complete within the task boundary.
- Decision owner: model-driven parent `AgentLoop`, and model child loops over delegated work.
- Supporting / enforcement mechanisms: tool bridge, sandbox/fences, permissions, LSP, shell, checkpoint snapshotting and event log.
- Closure path: user task → model decision → approved tool/child action → result/log and diagnostics → next model decision or completion.
- Boundary reachability: `AgentBuilder` registers task/file/shell/LSP tools for the default live agent and `TaskTool` constructs executable children; CLI/TUI/desktop all run this core.
- Why this is / is not agent-owned: the model selects the concrete work, tool call and response to feedback; the user chooses the objective and risk ceiling and the host enforces safety.
- Evidence: [agent loop](https://github.com/r1c7/CluxMate/blob/c3d5d84bbb6149ebdd2bd0ec7a8fa7817a984192/cluxmate/core/agent.py), [builder tool registration](https://github.com/r1c7/CluxMate/blob/c3d5d84bbb6149ebdd2bd0ec7a8fa7817a984192/cluxmate/core/builder.py), [task execution](https://github.com/r1c7/CluxMate/blob/c3d5d84bbb6149ebdd2bd0ec7a8fa7817a984192/cluxmate/tools/task.py).
- Basis: source-level standard-distribution closure, not a live agent run.
- Confidence: high on mechanism/ownership; runtime effectiveness unmeasured.
- Caveats: no model/provider-quality benchmark run; dangerous work can require human approval.

## S2 — Coordination

- State: A
- Function: coordinate distinct delegated coding S1 units so simultaneous work does not race on the same workspace paths or exhaust shared execution slots.
- Disturbance / variety regulated: child write/write conflict, uncontrolled fan-out, a nested child waiting for its parent's saturated slot.
- Decisive decision or feedback right: model parent chooses task partition and the `write_paths` claims on each `task` call; when a child cannot be admitted or reports completion the parent receives its outcome and can replan. The deterministic scheduler enforces the selected partition and structural overlap rules.
- Decision owner: model parent for discretionary partition and coordination; `SubagentScheduler` for fixed admission enforcement.
- Supporting / enforcement mechanisms: `MAX_CONCURRENT=4`, `MAX_WRITERS=2`, path canonicalization, overlap detection, writer serialization, nested fail-fast and ticket release.
- Closure path: parent allocates tasks/scopes → scheduler compares active claims → executes disjoint children, queues conflicting top-level writers or refuses blocked nested spawns → completed/blocked child status returns in the parent `task` result → parent changes downstream assignment.
- Boundary reachability: shipped parent `TaskTool` exposes `write_paths` and calls `SubagentScheduler.acquire` before child construction; the scheduler releases slots under `finally`.
- Why this is / is not agent-owned: the model selects work boundaries, coordinating scope and subsequent plan; the host's fixed cap and serialization alone would warrant only a coordination constructor, not model ownership. Positive `A` is bounded to parent-mediated child partition, not an independent dynamic negotiation protocol among all children.
- Distinct S1 units: two or more delegated `general-purpose` writer children, with optional `explore` and reviewer children.
- Inter-S1 disturbance: concurrent writes to equal, ancestor or descendant workspace paths and competition for shared execution capacity.
- Attenuating coordination relation: declared claim scopes, overlap admission gate, deferred incompatible writers and limited model-available parallel slots.
- Feedback into subsequent S1 behaviour: scheduler denial/queuing affects what can execute now, and structured child status/failed nested spawn returns to the model parent for a changed assignment or continuation.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: it explicitly detects and attenuates inter-child write conflicts, with a model-selected scope boundary, rather than merely offering a mailbox, task list or child-spawn primitive.
- Evidence: [scheduler](https://github.com/r1c7/CluxMate/blob/c3d5d84bbb6149ebdd2bd0ec7a8fa7817a984192/cluxmate/core/subagent_scheduler.py), [task write claims / feedback](https://github.com/r1c7/CluxMate/blob/c3d5d84bbb6149ebdd2bd0ec7a8fa7817a984192/cluxmate/tools/task.py), [scheduler tests](https://github.com/r1c7/CluxMate/blob/c3d5d84bbb6149ebdd2bd0ec7a8fa7817a984192/tests/core/test_subagent_scheduler.py).
- Basis: explicit end-to-end runtime wiring plus host tests; no LLM test.
- Confidence: medium-high; coordination discretion is model-mediated, fixed admission decisions remain runtime-owned.
- Caveats: omitted paths conservatively claim the whole workspace; uncontrolled parent direct writes are not proven serializable against children; guarantees are about declared child claims and scheduling, not universal data-race freedom.

## S3 — Inside-and-now control

- State: A(P)
- Function: integrate concurrent work, set current task commitments and resource/priority trade-offs, act on child/audit evidence, and steer execution of the session whole.
- Disturbance / variety regulated: task fragmentation, incomplete/false successes, bounded child budgets, current permission constraints, competing work priorities and execution failures.
- Decisive decision or feedback right: model parent decomposes and allocates ongoing work and accepts/corrects child work; alternatively the supervising user steers current commitments, mode and recovery after observing workspace/session status.
- Decision owner: agent parent in autonomous delegated mode; human operator in the supported attended session mode.
- Supporting / enforcement mechanisms: root-only todo, child tree/turn logs, child-status normalization, tool approval, session checkpoint/rewind, desktop agent inspector and session controls.
- Closure path: current task and child reports/diffs → parent model's priority/correct/retry/review decision → additional tool and child actions; in attended mode user observes current task/session state → changes priorities/mode, interrupts or restores → next session operation follows that decision.
- Boundary reachability: shipped root `AgentLoop`, `TaskTool`, parent-only `TodoTool` and UI/JSON-RPC current-session controls; operator intervention exists at the same workspace/session recursion.
- Why this is / is not agent-owned: the model decides the whole-task mix and reacts to returned children rather than the scheduler deciding organizational commitments; the user has a separate supported whole-session intervention route, not merely one write approval.
- Whole-system current view: root task/todo, child execution tree and per-child status/log, current workspace diff, mode and checkpoint timeline in the local client.
- Current-control decision scope: decompose and retask children, prioritize repair/review/completion, request further work, abort/rewind/restrict an ongoing session.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | root model agent | task, returned child status, tool or review findings | retask, continue, repair, review or finish via agent loop | [parent prompt](https://github.com/r1c7/CluxMate/blob/c3d5d84bbb6149ebdd2bd0ec7a8fa7817a984192/cluxmate/templates/system_prompt.j2), [task](https://github.com/r1c7/CluxMate/blob/c3d5d84bbb6149ebdd2bd0ec7a8fa7817a984192/cluxmate/tools/task.py) |
| Parent (`P`) | local session owner | observed whole-session plan/tree/diff/progress or problem | task correction, mode switch, interruption or scoped rewind governs later operation | [desktop inspector](https://github.com/r1c7/CluxMate/blob/c3d5d84bbb6149ebdd2bd0ec7a8fa7817a984192/desktop/src/renderer/components/AgentInspector.tsx), [JSON-RPC control](https://github.com/r1c7/CluxMate/blob/c3d5d84bbb6149ebdd2bd0ec7a8fa7817a984192/cluxmate/core/jsonrpc_server.py), [checkpoint manager](https://github.com/r1c7/CluxMate/blob/c3d5d84bbb6149ebdd2bd0ec7a8fa7817a984192/cluxmate/core/checkpoints.py) |

- Evidence: [builder parent tool gating](https://github.com/r1c7/CluxMate/blob/c3d5d84bbb6149ebdd2bd0ec7a8fa7817a984192/cluxmate/core/builder.py), [task result status](https://github.com/r1c7/CluxMate/blob/c3d5d84bbb6149ebdd2bd0ec7a8fa7817a984192/cluxmate/tools/task.py), [agent inspector](https://github.com/r1c7/CluxMate/blob/c3d5d84bbb6149ebdd2bd0ec7a8fa7817a984192/desktop/src/renderer/components/AgentInspector.tsx).
- Basis: model current-control instructions and live-control surfaces are shipped; parent mode bounded to local operator, not upstream maintainers.
- Confidence: medium-high.
- Caveats: user authority is not an autonomous current-control actor in this mode; generic approval alone was not used as proof of `(P)`.

## S3* — Complementary audit

- State: A
- Function: separately inspect the gap between claimed requirement completion and directly observable code/test reality; return discrepancies for current-control correction.
- Disturbance / variety regulated: implementer self-report bias, omitted requirements, unsupported green statuses and regressions invisible in the ordinary child summary.
- Decisive decision or feedback right: a distinct model `reviewer` judges each requirement claim on source/test evidence and returns `pass`/`fail`/`unverifiable`; the parent model can demand correction and a bounded scoped re-review.
- Decision owner: first-party spawned reviewer model for independent audit judgment; parent model S3 receives findings and changes work priorities.
- Supporting / enforcement mechanisms: built-in reviewer profile has no edit tools; separate child session and prompt, raw read/grep/LSP/bash checks, no implementer-summary input, path-claim serialization, normalized machine-readable child status, narrower host claim-audit reminder.
- Closure path: implementation artifact and original requirement → distinct reviewer inspects raw tree, executes allowed deterministic check → per-claim findings returned by `task` → root model fixes failures → optional single scoped re-review before completion.
- Boundary reachability: `reviewer` is a built-in standard type and the root system prompt explicitly dispatches it after nontrivial implementation work, with original requirements and diff; child builder builds its own restricted loop.
- Why this is / is not agent-owned: reviewer model owns actual discrepancy judgment, distinct from implementer's self-report; scheduler and advisory completion audit only support the independent path. Parent controls review triggering, so it is not mandatory for every run.
- Claim being audited: whether nontrivial delivered code satisfies each requested requirement and whether a child's reported success is backed by evidence.
- Ordinary reporting path: implementer child → completion narrative/status → parent model and task/turn events.
- Complementary access path: reviewer gets requirement plus file/diff reference, reads actual workspace and can run verification commands; excludes implementer narrative.
- Independence boundary: separate child context, restricted toolset and actual code/test evidence bypass implementer summary; same configured provider/model family, reviewer dispatch owner and mutable workspace remain possible correlated failure points.
- Who acts on findings: model parent S3 fixes/retasks and invokes at most one targeted re-review; a human may inspect the report in attended mode.
- Evidence: [reviewer registry and evidentiary contract](https://github.com/r1c7/CluxMate/blob/c3d5d84bbb6149ebdd2bd0ec7a8fa7817a984192/cluxmate/core/subagents.py), [root review gate instructions](https://github.com/r1c7/CluxMate/blob/c3d5d84bbb6149ebdd2bd0ec7a8fa7817a984192/cluxmate/templates/system_prompt.j2), [child status reconciliation](https://github.com/r1c7/CluxMate/blob/c3d5d84bbb6149ebdd2bd0ec7a8fa7817a984192/cluxmate/tools/task.py), [review gate tests](https://github.com/r1c7/CluxMate/blob/c3d5d84bbb6149ebdd2bd0ec7a8fa7817a984192/tests/core/test_builder_subagent_types.py).
- Basis: specific independent auditor actor, direct operational evidence and explicit corrective return path in standard prompts, not CI alone.
- Confidence: medium-high on shipped path, medium on real-world independence.
- Caveats: text/prompt obligations are not host-enforced audit coverage; a reviewer with bash can technically alter files subject to instruction/permissions; no experiment measures capture resistance or verdict accuracy.

## S4 — Outside-and-then intelligence

- State: A
- Function: take durable lessons about changing project/environment constraints and use them to adapt future coding behavior across sessions.
- Disturbance / variety regulated: rediscovery of non-obvious conventions, previously encountered build/test gotchas, and lost project-specific experience as future tasks differ.
- Decisive decision or feedback right: the root model is explicitly instructed to decide when a non-obvious, reusable learning merits writing to durable memory and what guidance should persist; the next turn's injected memory changes its available response policy/context.
- Decision owner: root model agent selecting and recording prospective lessons; host stores and reinjects them.
- Supporting / enforcement mechanisms: `update_memory` writes project/global `AGENTS.md`, always-injected future project memory; optional opt-in `remember`/`forget` plus lexical recall of stable facts.
- Closure path: emerging project requirement/tool failure/environment observation → model determines reusable future distinction and formulates memory entry → durable project/global `AGENTS.md` or optional fact store → later request reinjects or recalls the lesson → model adjusts approach.
- Boundary reachability: root `AgentBuilder` includes `UpdateMemoryTool` in regular non-plan modes; root system prompt explicitly calls for proactive learned context; memory manager reads on subsequent requests. Retrieval memory is optional and not needed for the base loop.
- Why this is / is not agent-owned: model chooses to distill and persist the adaptation signal; this is bounded knowledge/capability adaptation, not a claim of autonomous architecture redevelopment, systematic outside-market surveillance or policy authorship. A user can also edit memory, but a separate human-owned strategic S4 cycle is not established merely from editable instructions.
- External distinction: new, non-obvious repo/environment conventions, build/test behavior and constraints experienced while carrying out coding tasks.
- Future / prospective distinction: whether those lessons will recur and ought to change subsequent sessions, versus transient details to discard.
- Adaptation option generated: model-authored durable memory instruction/fact, with potential later correction or removal.
- Path back into current capability / S3: `MemoryManager.render` and `builder.injections_for_turn` inject the revised future-session memory for current model task planning and execution.
- Evidence: [proactive learning prompt](https://github.com/r1c7/CluxMate/blob/c3d5d84bbb6149ebdd2bd0ec7a8fa7817a984192/cluxmate/templates/system_prompt.j2), [update-memory tool](https://github.com/r1c7/CluxMate/blob/c3d5d84bbb6149ebdd2bd0ec7a8fa7817a984192/cluxmate/tools/update_memory.py), [memory readback](https://github.com/r1c7/CluxMate/blob/c3d5d84bbb6149ebdd2bd0ec7a8fa7817a984192/cluxmate/core/memory.py), [root tool registration](https://github.com/r1c7/CluxMate/blob/c3d5d84bbb6149ebdd2bd0ec7a8fa7817a984192/cluxmate/core/builder.py), [optional retrieval memory](https://github.com/r1c7/CluxMate/blob/c3d5d84bbb6149ebdd2bd0ec7a8fa7817a984192/cluxmate/core/retrieval_memory.py).
- Basis: standard root-prompt instruction plus write→persist→future-injection code path; no real model learning uplift measured.
- Confidence: medium; prospective memory closure established, strategic breadth explicitly narrow.
- Caveats: the agent need not record every useful lesson; disabled retrieval memory does not undermine always-injected `AGENTS.md`; user review/approval can be required for writes depending on mode; memory may be stale or truncated.

## S5 — Policy and identity

- State: P
- Function: retain the workspace assistant's ultimate operational identity, trusted project boundary, allowed capabilities and risk-policy envelope under legitimate operator control.
- Disturbance / variety regulated: request for unsafe tooling, untrusted project-provided instructions, escalation of dangerous shell code and drift of persistent authorization policy.
- Decisive decision or feedback right: user determines authorized project trust, persistent safe/dangerous allowlists, sandbox grants, model configuration and allowed operating mode; critical/escalated calls retain human gating even when routine activity is autonomous.
- Decision owner: local human/operator for the durable identity and ultimate-policy boundary; not the agent, provider or repository maintainer.
- Supporting / enforcement mechanisms: `PermissionPolicy` and `TrustStore` persistence, `WriteFence`, OS sandbox and SSRF/egress rules, scoped user approvals and mode switch.
- Closure path: identity/authority question (trusted workspace, permitted risk tier, escalation/egress/sandbox ceiling) → operator approves/denies/configures → trust/permissions/config stored in protected user/project locations → effective toolset and next execution governed by selected policy.
- Boundary reachability: supported user-global and per-project policy/config files, live prompt cards, CLI trust commands and desktop settings; model cannot simply write protected `.cluxmate` authority configuration through normal file tools.
- Why this is / is not agent-owned: agent chooses task actions *inside* the operator's policy, but does not own the legitimate decision to change that ultimate envelope.
- Identity / ultimate-policy issue: whom the agent may act for, which workspace it may trust and which risks remain forbidden or require explicit authority.
- Ultimate authority in each claimed mode: human project/session owner; no autonomous first-party S5 policy-substitution mode established.
- Return-to-operation path: persisted per-project/global decision is reloaded/consulted on later requests, changing available tools, approvals and enforcement.
- Evidence: [permission mode and persisted policy](https://github.com/r1c7/CluxMate/blob/c3d5d84bbb6149ebdd2bd0ec7a8fa7817a984192/cluxmate/core/permissions.py), [trust registry](https://github.com/r1c7/CluxMate/blob/c3d5d84bbb6149ebdd2bd0ec7a8fa7817a984192/cluxmate/core/trust.py), [README security](https://github.com/r1c7/CluxMate/blob/c3d5d84bbb6149ebdd2bd0ec7a8fa7817a984192/README.md), [builder sandbox enforcement](https://github.com/r1c7/CluxMate/blob/c3d5d84bbb6149ebdd2bd0ec7a8fa7817a984192/cluxmate/core/builder.py).
- Basis: explicit first-party durable user authority and enforcement return loop.
- Confidence: high.
- Caveats: `yolo` opt-out weakens the sandbox by intentional operator choice; this does not transfer ultimate authority to the model.

## Distributed OSS parent arrangement

The repository is publicly developed, but one self-hosted workspace agent is the credited recursion. Contributor/maintainer decisions are not assumed to have access to private local session logs or write authority over individual user's policy. Parent `S3=A(P)` and `S5=P` designate the *local* operator route; no claim is made that the project-level OSS maintainer collective controls or audits all deployments.

## Self-hosted and non-human modes

The user may run the Python CLI/TUI/REPL without desktop and can select supervised modes with persistent policy. In headless configured model mode, S1/S2/S3/S3*/S4 closures are agent-mediated, while the initial objective and legitimate top-level policy remain operator-owned. A parent-only control plane is reachable in shipped local UI/CLI but cannot be projected onto a non-human upstream organization. Tools are not exercised against a live model in this assessment.

## Recursion

`general-purpose` / `explore` / `reviewer` are bounded delegated subagents with per-child logs, budgets, tool sets and maximum depth four. A reviewer is complementary audit inside the same local unit, not an entirely independent viable company, and write-path isolation is coordination of task-scoped operations rather than proof of independently self-maintaining S1 organizations.

## Variety and escalation

Tool results, diagnostics and audit findings amplify relevant error distinctions to the model; fixed write claims and resource caps attenuate race/fan-out variety; project modes/permissions block or escalate risk to a legitimate human; persisted memory can carry a subset of experienced environment variety forward. The product does not prove perfect isolation of simultaneous writes by the parent or perfect independent audit: those remain explicit operational bounds.

## Evidence gaps

- No authorized live LLM/provider, end-to-end agent quality or benchmark tests performed; source and supplied native unit tests are *mechanism evidence*, not behavioral success measurements.
- Reviewer is a distinct prompted child with direct evidence access but not a separately attested evaluator; independence may be limited by provider choice, scheduler/tool policies and parent-controlled triggering.
- The active S4 learning path is narrow prospective cross-session memory, not autonomously measured capability optimization or outside-market forecasting.
- Deterministic scheduling tests demonstrate child overlap behavior; they do not establish an absolute safety guarantee for unregistered parent writes or external tools.

---
harness_id: aperant
project_name: Aperant
repository: https://github.com/AndyMik90/Aperant
review_ref: 20250db069a849ab001ac6ab9e3e9779886ab9e2
reviewed_at: 2026-10-31
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-31
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Aperant

## Review boundary

- System in focus: the shipped 2.x Aperant / Auto-Claude Electron desktop app and its first-party TypeScript agent/worker, task, worktree, QA, merger, memory and roadmap implementations at the frozen revision.
- Purpose and identity: user-directed autonomous software planning, implementation, validation and integration for git projects, with concurrent task lanes supervised from a desktop interface.
- Relevant environment: selected user repositories, git branches/worktrees, model providers/Claude Code dependencies, tests, development services, user approval, desktop operating system and optional integrations.
- Standard-distribution boundary: the public 2.x desktop app/source, not the separately developed, unreviewable 3.0 rewrite. The README explicitly states that the 2.x app is in maintenance mode and the 3.0 work is in a separate repository.
- Credited operating surfaces: desktop task start/stop/review, worker-backed phase sessions, task-default isolated worktrees, model-directed coding/QA, optional post-task merge, local memory and user-invoked feature roadmap.
- Adjacent surfaces excluded from ownership: upstream model inference quality, provider account authorization, user repositories' release pipelines, externally installed MCP/Claude Code agents and the unreleased 3.0 code. A test-only parallel-executor helper without a production callsite is not credited as a deployed coordination loop.
- First-party modes considered: normal default worktree-backed task execution, user-selected no-worktree/fallback mode, desktop operator stop/review, separate QA review/fixer sessions, optional merge and roadmap.
- Recursion level: one desktop workspace/project and its multiple task/spec agent runs, not the development company or every independent organization using Aperant.
- Reviewed revision: 20250db069a849ab001ac6ab9e3e9779886ab9e2.
- Observation date: 2026-10-31.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Aperant's main process AgentManager creates a task-specific worktree by default, constructs a serializable session with a build-orchestrator agent type and launches a worker process; failed worktree creation explicitly falls back to the shared project root. The BuildOrchestrator moves from spec/planning to coder subtask sessions, then a distinct QA reviewer and, on failure, a QA fixer followed by re-review. The first-party AI session/agent code supplies tool registries and model-tool observation loops. Separate desktop IPC handles task start, stop, review and merge. MergeOrchestrator checks conflict patterns and can call a model-powered resolver, but merging is a user-facing post-task integration path, not evidence of a persistent agent-bargained intertask resource policy. Roadmap and memory services generate project artefacts/notes; neither makes the harness's ultimate mandate mutable. No provider-backed E2E run was attempted in this source-only review.

## Operational model

Each coding/QA worker is a bounded operational cell executing a user-specified development task against project files and test observations. The app constructor supplies phase routing, max steps, worktree isolation, progress and resource limits. Model actors choose concrete inspections, edits, implementation and repair proposals; operator-selected tasks and desktop controls set higher-level task acceptance. The model QA reviewer is distinct from the producer and can test/inspect the actual project, report defects and send them into a new fixer iteration. Concurrent builds are buffered primarily through preselected disjoint worktrees; post hoc merge reduces integration conflicts, but its AI text resolution is not credited as a standing whole-current coordination negotiation.

## S1 — Operations

- State: A
- Function: autonomously perform a bounded engineering task by planning, editing, running available tools and reacting to actual build/test/review feedback.
- Disturbance / variety regulated: unfamiliar codebase, missing dependency details, failed subtasks, build failures and QA findings.
- Decisive decision or feedback right: a model-driven session selects code/tool actions and revised attempts within the selected project and configured permissions.
- Decision owner: model-backed planner/coder and QA fixer sessions launched by Aperant's first-party worker/orchestration path; user specifies the task and model provider remains external.
- Supporting / enforcement mechanisms: prompt/config roles, tool registry, session step bounds, task-state persistence and worktree paths.
- Closure path: user task/spec → planner output → coder model/tool loop → observed file/tool/test result → correction, remaining subtasks and final QA return.
- Boundary reachability: AgentManager's task-execution path constructs the build-orchestrator worker and worktree with supported defaults; BuildOrchestrator calls real phase-specific sessions.
- Why this is / is not agent-owned: code and tool choices adapt to feedback from the model; deterministic phase transitions and limits alone would not supply that discretion.
- Evidence: [AgentManager active worktree-to-worker path](https://github.com/AndyMik90/Aperant/blob/20250db069a849ab001ac6ab9e3e9779886ab9e2/apps/desktop/src/main/agent/agent-manager.ts#L456-L548), [BuildOrchestrator lifecycle](https://github.com/AndyMik90/Aperant/blob/20250db069a849ab001ac6ab9e3e9779886ab9e2/apps/desktop/src/main/ai/orchestration/build-orchestrator.ts#L229-L289), [coder session invocation](https://github.com/AndyMik90/Aperant/blob/20250db069a849ab001ac6ab9e3e9779886ab9e2/apps/desktop/src/main/ai/orchestration/build-orchestrator.ts#L423-L487), [first-party agent worker](https://github.com/AndyMik90/Aperant/blob/20250db069a849ab001ac6ab9e3e9779886ab9e2/apps/desktop/src/main/ai/agent/worker.ts).
- Basis: structural.
- Confidence: high for code path, medium for installation-specific runtime.
- Caveats: model credentials and actual external provider behavior were not exercised; shipped 2.x is reviewed, not the unmerged 3.0 rewrite.

## S2 — Coordination

- State: C
- Function: mechanically dampen shared-file interference among independently executing coding task cells by giving them separate branches/worktrees and a bounded later integration path.
- Disturbance / variety regulated: two live task workers writing incompatible paths in the same user repository, followed by textual/semantic merge conflicts at integration.
- Decisive decision or feedback right: first-party constructor selects a per-task git worktree/branch by default before starting the worker; merge tools detect conflicts and can request AI text resolution after a user initiates integration.
- Decision owner: constructor-owned static worktree policy (C), not an autonomous S2 manager deciding live task ownership or negotiated revised commitments; the model resolver selects a merge text only on the post hoc path.
- Supporting / enforcement mechanisms: unique spec branch/worktree mapping, git branch isolation, conflict detector, merge report and optional AI resolver.
- Closure path: concurrent task launches → distinct project filesystem views → local independent edits without overwrite → explicit integration/conflict detection → accepted/rejected merge result.
- Boundary reachability: worktrees are enabled by default in the actual AgentManager call path, and the merge IPC wires MergeOrchestrator and resolver. The no-worktree option and nonfatal worktree creation failure bypass this guarantee.
- Why this is / is not agent-owned: the decisive prevention is a preset technical partition, not a model-selected inter-agent arbitration; an AI-generated conflict patch after the task does not establish a live S2 policy owner.
- Evidence: [actual default task isolation and fallback](https://github.com/AndyMik90/Aperant/blob/20250db069a849ab001ac6ab9e3e9779886ab9e2/apps/desktop/src/main/agent/agent-manager.ts#L472-L500), [worktree manager](https://github.com/AndyMik90/Aperant/blob/20250db069a849ab001ac6ab9e3e9779886ab9e2/apps/desktop/src/main/ai/worktree/worktree-manager.ts#L72-L205), [merge IPC connection](https://github.com/AndyMik90/Aperant/blob/20250db069a849ab001ac6ab9e3e9779886ab9e2/apps/desktop/src/main/ipc-handlers/task/worktree-handlers.ts#L2029-L2087), [model text resolver](https://github.com/AndyMik90/Aperant/blob/20250db069a849ab001ac6ab9e3e9779886ab9e2/apps/desktop/src/main/ai/runners/merge-resolver.ts#L52-L117).
- Basis: structural.
- Confidence: medium-high.
- Caveats: the isolated mode is a selectable default, not a hard invariant; a failed worktree can revert to shared-root execution, and no model-mediated prospective conflict negotiation was demonstrated.

## S3 — Inside-and-now control

- State: P
- Function: let a human desktop operator see ongoing task/agent status, stop or review current work and decide task continuation across a project workspace.
- Disturbance / variety regulated: stuck, misdirected, unsafe or unwanted concurrent task execution and acceptance decisions.
- Decisive decision or feedback right: the operator chooses which task to start/stop and approves/rejects a review result using IPC connected to active worker lifecycle and task-state manager.
- Decision owner: parent/operator (P); App/AgentManager provides a shared current status/command surface but no autonomous whole-portfolio executive deciding priorities and allocations.
- Supporting / enforcement mechanisms: Kanban task board and multiple agent terminals, process registry, task-state transitions and stop/restart tracking.
- Closure path: active task state appears in desktop → operator inspects portfolio/task → stop or review command → worker termination or status/acceptance transition → refreshed UI.
- Boundary reachability: README documents the active desktop task/terminal modes; TASK_STOP and TASK_REVIEW handlers call the live AgentManager/task-state paths.
- Why this is / is not agent-owned: UI and preset concurrency bounds do not make a model the owner of whole-current resource/priority control; the consequential selection remains human.
- Evidence: [supported desktop task controls](https://github.com/AndyMik90/Aperant/blob/20250db069a849ab001ac6ab9e3e9779886ab9e2/README.md), [stop and review IPC](https://github.com/AndyMik90/Aperant/blob/20250db069a849ab001ac6ab9e3e9779886ab9e2/apps/desktop/src/main/ipc-handlers/task/execution-handlers.ts#L364-L411), [worker lifecycle](https://github.com/AndyMik90/Aperant/blob/20250db069a849ab001ac6ab9e3e9779886ab9e2/apps/desktop/src/main/ai/agent/executor.ts#L34-L85).
- Basis: structural.
- Confidence: medium.
- Caveats: no independent runtime UI exercise; the right is scoped to the app's tasks and does not imply a whole business enterprise controller.

## S3* — Complementary audit

- State: A
- Function: independently challenge the coder's completion claim against direct code, changed-file and test/visual evidence before considering the task done.
- Disturbance / variety regulated: a coder may have skipped acceptance criteria, introduced a regression or reported passing work without sufficient testing.
- Decisive decision or feedback right: separate model-driven QA reviewer runs inspections/tests and writes a pass/fail report; a fail invokes a different fixer session and a fresh reviewer.
- Decision owner: model-backed QA reviewer distinct from the coder, with BuildOrchestrator interpreting the QA result and launching correction; the fixed loop bound is constructor policy.
- Supporting / enforcement mechanisms: explicit QA reviewer prompt, raw git diff/source reads, test and UI checks, qa_report status, reviewer/fixer phase separation and report reset.
- Closure path: coder finishes → QA reviewer separately inspects repository/diff and tests → failed report → QA fixer repairs → previous report cleared → new reviewer pass or bounded failure.
- Boundary reachability: BuildOrchestrator calls qa_reviewer and qa_fixer in the production task lifecycle; prompt demands actual direct inspection rather than relying on coder prose.
- Why this is / is not agent-owned: the independent QA model decides evidentiary defects; a deterministic CI gate, status parser or coder self-check alone would not receive S3* credit.
- Claim being audited: implementation satisfies spec acceptance criteria and can be signed off.
- Ordinary reporting path: the coder's subtask status/summary and implementation-plan progress.
- Complementary access path: a new QA session with tools to inspect git diffs, source, unit/integration/E2E tests and rendered behavior when relevant.
- Independence boundary: roles and session calls are separated; same overall app/provider may be used, so independence is contextual/role-based rather than an external audit organization.
- Who acts on findings: the separately launched QA fixer performs repair and returns work for another QA review; operator may later accept the task.
- Evidence: [QA reviewer/fixer bounded correction loop](https://github.com/AndyMik90/Aperant/blob/20250db069a849ab001ac6ab9e3e9779886ab9e2/apps/desktop/src/main/ai/orchestration/build-orchestrator.ts#L490-L580), [reviewer's direct-evidence protocol](https://github.com/AndyMik90/Aperant/blob/20250db069a849ab001ac6ab9e3e9779886ab9e2/apps/desktop/prompts/qa_reviewer.md), [distinct agent configuration](https://github.com/AndyMik90/Aperant/blob/20250db069a849ab001ac6ab9e3e9779886ab9e2/apps/desktop/src/main/ai/config/agent-configs.ts#L261-L312).
- Basis: structural.
- Confidence: medium-high.
- Caveats: source-backed closure path, not proof of an observed provider-backed successful QA run; review quality and UI tool availability remain environment-dependent.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party closed loop was demonstrated that revises the harness's future organizational capabilities in response to external strategic change.
- Disturbance / variety regulated: available memory observations, prospective feature ideas and competitor context might support future project decisions but do not establish a harness-level adaptation return.
- Decisive decision or feedback right: no source-backed owner of external/future viability adaptation and accepted persistent organizational capability change.
- Decision owner: the user chooses roadmaps and future tasks; model sessions can propose project features, while the passive memory observer classifies own-task tool/retry signals.
- Supporting / enforcement mechanisms: memory candidate capture/trust gates, optional co-access synthesis (marked placeholder), roadmap discovery and feature-generation files.
- Closure path: roadmap.json or memory candidates can be persisted and later consumed; this is project work/planning and episodic memory, not a demonstrated external change → selected future operating policy/capability → adoption loop of Aperant itself.
- Why this is / is not agent-owned: feature priority proposals and internal task reflections are not by themselves an S4 system-level adaptation function, even when generated by an LLM.
- External distinction: optional competitor context for a user project's roadmap is not evidence of continuous environmental intelligence governing the harness.
- Future / prospective distinction: the roadmap is prospective for project features, but no first-party acceptance/implementation of a changed harness operating architecture is linked by this path.
- Evidence: [roadmap generated as project JSON](https://github.com/AndyMik90/Aperant/blob/20250db069a849ab001ac6ab9e3e9779886ab9e2/apps/desktop/src/main/ai/runners/roadmap.ts#L209-L355), [memory observer candidates and gate](https://github.com/AndyMik90/Aperant/blob/20250db069a849ab001ac6ab9e3e9779886ab9e2/apps/desktop/src/main/ai/memory/observer/memory-observer.ts#L94-L126), [deferred synthesis path](https://github.com/AndyMik90/Aperant/blob/20250db069a849ab001ac6ab9e3e9779886ab9e2/apps/desktop/src/main/ai/memory/observer/memory-observer.ts#L316-L327), [roadmap feature prompt](https://github.com/AndyMik90/Aperant/blob/20250db069a849ab001ac6ab9e3e9779886ab9e2/apps/desktop/prompts/roadmap_features.md).
- Basis: structural.
- Confidence: medium.
- Caveats: a user could adopt generated feature plans outside the runtime, but this is not credited as a shipped S4 closure.

### Absence scope

- Surfaces inspected: memory observer/promotion, roadmap runner and feature prompts, competitor-analysis persistence and task orchestration.
- Plausible first-party paths checked: error learning, co-access synthesis, optional competitor research, human-roadmap review and persisting future tasks.
- Why no material first-party path remains: none shows a separately owned strategic adaptation decision that changes the harness's prospective operating capability in response to an outside variety signal.

## S5 — Policy and identity

- State: —
- Function: no first-party runtime authority closes the ultimate identity, legitimate organizational purpose and constitutional policy return of a multi-agent system.
- Disturbance / variety regulated: security permissions, task approvals and provider config constrain execution but do not constitute identity-level governance.
- Decisive decision or feedback right: none established; project owner and external product governance retain final authority.
- Decision owner: user chooses projects, task requests, permissions and acceptance; fixed safeguards apply without an identity-level deliberator.
- Supporting / enforcement mechanisms: command validators, OS/path containment, OAuth/provider selection, task approval and status controls.
- Closure path: authorization gates restrict tasks; no first-party reasoned ultimate-policy amendment and return into subordinate decision rights.
- Why this is / is not agent-owned: local allowlists and prompts are procedural bounds, not the authority to resolve legitimate purpose and identity.
- Evidence: [security profile and validator](https://github.com/AndyMik90/Aperant/blob/20250db069a849ab001ac6ab9e3e9779886ab9e2/apps/desktop/src/main/ai/security/security-profile.ts), [bash validator](https://github.com/AndyMik90/Aperant/blob/20250db069a849ab001ac6ab9e3e9779886ab9e2/apps/desktop/src/main/ai/security/bash-validator.ts), [operator review](https://github.com/AndyMik90/Aperant/blob/20250db069a849ab001ac6ab9e3e9779886ab9e2/apps/desktop/src/main/ipc-handlers/task/execution-handlers.ts#L392-L411).
- Basis: structural.
- Confidence: high within reviewed boundary.
- Caveats: upstream product governance is outside the harness runtime.

### Absence scope

- Surfaces inspected: user controls, task-state permissions, security policies, model/provider configuration, roadmap and project-level prompts.
- Plausible first-party paths checked: safety constraints, approval mode, project goal setting, memory promotion and product roadmap.
- Why no material first-party path remains: none authorizes a runtime constitutional owner to decide and promulgate ultimate organizational identity or legitimate policy.

## Recursion

The desktop workspace is the focus. Each model-backed task build (and its coder/reviewer/fixer phases) is an S1 operational cell. Worktree isolation is a constructor-level cross-cell buffer; the human desktop operator supplies current oversight. A QA reviewer is the complementary challenge path of the task, not automatically a higher S3 executive. User projects and future generated feature implementations are operational environments/outputs, not recursive S4/S5 organizations of Aperant.

## Variety and escalation

- Model-selected tool actions and retry respond to task-level source/test variety.
- Default separate worktrees prevent competing tasks from overwriting one shared checkout, but optional bypass/fallback can forfeit that protection.
- The QA model can contest the coder's account from direct code/tests, returning failures through a separate fixing session.
- A desktop operator can stop/review a running task; this parent mode is not attributed as agent-owned fleet regulation.
- When model credentials, worktree creation, tool access or tests fail, the run can stop/fall back/report rather than silently proving success; user permission boundaries are not bypassed.
- The reviewed public 2.x distribution is in maintenance, while the 3.0 rebuild is outside this source boundary.

## Evidence gaps

- Source-first structural assessment only: no external model credentials, desktop installer, full Electron UI, multi-provider task run or independent QA model execution exercised.
- Public code demonstrates the default worktree and reviewer loop, but not collision frequency, runtime outcomes or measured review independence.
- No active production caller was found for the isolated parallel-executor helper; it is not used to infer a separate scheduling agent.
- Provider authorization and all third-party model/tool internals are excluded from first-party ownership.
- Revisit only if a newer frozen public revision or actual platform/semantic review supplies contrary primary evidence.

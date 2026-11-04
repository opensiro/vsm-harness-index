---
harness_id: tkcode
project_name: TKCode
repository: https://github.com/AtomUICommunity/TKCode
review_ref: 620235e49fa0d7a1c7d80136a00414d9a398a102
reviewed_at: 2026-11-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# TKCode

## Review boundary

- System in focus: The shipped TKCode local coding-agent session and its supported first-party ACP coordinated-subagent mode, treated as a single human-initiated software-change engagement.
- Purpose and identity: Investigate, plan, execute and verify changes in a local workspace through model-directed coding tools, with optional parent coordinator and specialized workers.
- Relevant environment: Source files, test results, command failures, uncertain user requirements, task dependencies, overlapping file edits, provider and tool failures, and operator permissions.
- Standard-distribution boundary: .NET desktop application, first-party AgentHost, built-in model/tool loop, session role instructions, task tools and first-party subagent coordinator. External Codex/Claude/third-party ACP processes are not credited.
- Credited operating / distribution surfaces: [README](https://github.com/AtomUICommunity/TKCode/blob/620235e49fa0d7a1c7d80136a00414d9a398a102/README.md), [Agent loop](https://github.com/AtomUICommunity/TKCode/blob/620235e49fa0d7a1c7d80136a00414d9a398a102/src/TKCode.Agent/Agent.cs), [SessionRole ACP](https://github.com/AtomUICommunity/TKCode/blob/620235e49fa0d7a1c7d80136a00414d9a398a102/src/TKCode.Agent.Coding/Assets/SessionRole.cs), [AgentCoordinator](https://github.com/AtomUICommunity/TKCode/blob/620235e49fa0d7a1c7d80136a00414d9a398a102/src/TKCode.AgentHost/AgentCoordinator.cs), [session options](https://github.com/AtomUICommunity/TKCode/blob/620235e49fa0d7a1c7d80136a00414d9a398a102/src/TKCode.AgentHost/SessionOptions.cs), [task tools](https://github.com/AtomUICommunity/TKCode/blob/620235e49fa0d7a1c7d80136a00414d9a398a102/src/TKCode.Agent.Coding/Tools/Tasks/TaskTools.cs).
- Adjacent first-party surfaces excluded from ownership: Documentation/design proposals, CI, tests and development governance. Third-party external agent runtimes, remote model services and MCP servers do not donate ownership.
- First-party operating / deployment modes considered: Default Agent, Plan and ACP role; built-in general-purpose, explore and plan subagents; foreground/background workers; permission modes; local sessions and user approvals.
- Recursion level: One user coding engagement as system; independently executing worker agents are S1 units under an optional ACP parent at the engagement recursion.
- Reviewed revision: 620235e49fa0d7a1c7d80136a00414d9a398a102 (GitHub repository ID 1422076028).
- Observation date: 2026-11-04.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

AgentHost constructs built-in coding sessions with role-filtered tool sets. An Agent drives model responses and executes matching tools; task lists, workspace and background-task state persist within an engagement. The shipped ACP role makes one coordinator responsible for architecture, task decomposition, file ownership, dispatch and integration. AgentCoordinator starts actual isolated built-in agent sessions for delegated coding work, returns status/reports and can deliver later follow-up messages. A subagent inherits shared workspace/task list and its parent permission gate, but owns its own model loop and tool use. Default Agent mode runs coding tools directly. Plan mode requires operator approval before execution. [Agent session](https://github.com/AtomUICommunity/TKCode/blob/620235e49fa0d7a1c7d80136a00414d9a398a102/src/TKCode.Agent.Coding/AgentSession.cs), [role logic](https://github.com/AtomUICommunity/TKCode/blob/620235e49fa0d7a1c7d80136a00414d9a398a102/src/TKCode.Agent.Coding/Assets/SessionRole.cs), [coordinator](https://github.com/AtomUICommunity/TKCode/blob/620235e49fa0d7a1c7d80136a00414d9a398a102/src/TKCode.AgentHost/AgentCoordinator.cs).

## Operational model

In the built-in solo path the LLM chooses which coding tools to invoke and adjusts from results. In the ACP mode the coordinator model owns the current engagement plan, identifies independent file ownership domains, launches worker agents, reads their reports and delegates repairs or verification. Host task records and tool permission checks enable and constrain those decisions. ACP is a role a user can select, not evidence that every default session uses multi-agent coordination.

## S1 — Operations

- State: A
- Function: Execute source investigation, edits, commands and verification in response to a bounded delegated coding assignment.
- Disturbance / variety regulated: Unexpected source structure, execution errors, incomplete specifications and changing worktree feedback.
- Decisive decision or feedback right: Built-in model selects tools, edits and next actions after seeing execution results.
- Decision owner: Built-in Agent loop for default session and general-purpose worker loops in ACP.
- Supporting / enforcement mechanisms: Tool registry, workspace roots, file-state checks, JSONL session storage, permissions and model APIs.
- Closure path: Agent calls tool; tool executes and returns feedback; model chooses its next coding action until it reports completion.
- Boundary reachability: AgentHost creates built-in sessions and AgentCoordinator creates separate executable general-purpose subagent sessions; both run Agent.
- Why this is / is not agent-owned: Tool and action selection are runtime model decisions, not a fixed script.
- Evidence: [model/tool loop](https://github.com/AtomUICommunity/TKCode/blob/620235e49fa0d7a1c7d80136a00414d9a398a102/src/TKCode.Agent/Agent.cs), [AgentCoordinator.SpawnAsync](https://github.com/AtomUICommunity/TKCode/blob/620235e49fa0d7a1c7d80136a00414d9a398a102/src/TKCode.AgentHost/AgentCoordinator.cs), [AgentTool.ExecuteAsync](https://github.com/AtomUICommunity/TKCode/blob/620235e49fa0d7a1c7d80136a00414d9a398a102/src/TKCode.Agent.Coding/Tools/Agents/AgentTools.cs).
- Basis: structural.
- Confidence: high.
- Caveats: Upstream first-party source reviewed, without running the .NET desktop UI or external model.

## S2 — Coordination

- State: A
- Function: Attenuate interference among coding workers operating on a shared codebase and interdependent change tasks.
- Disturbance / variety regulated: Concurrent edits to the same file and inconsistent dependent work across independently executing subagents.
- Decisive decision or feedback right: ACP coordinator model decides whether tasks can run simultaneously based on non-overlapping file ownership, or must be sequential; can send corrective messages on conflict.
- Decision owner: Parent model in first-party ACP role.
- Supporting / enforcement mechanisms: Shared workspace and task registry, subagent names, spawn/report/message tools; per-session file mutation queues alone are insufficient cross-agent arbitration.
- Closure path: Parent selects file-scoped assignments and parallel/sequential dispatch; receives agent reports; on conflict or gaps sends follow-up and changes subsequent worker tasks.
- Boundary reachability: SessionRole.Acp is a selectable built-in role; SessionOptions.Apply installs the role and AgentTool/AgentCoordinator support actual first-party worker execution.
- Why this is / is not agent-owned: File-overlap judgments and conflict resolution are instructions to a coordinating model; not merely mechanical shared task state.
- Distinct S1 units: Separately instantiated general-purpose worker model loops, each editing its assigned source files.
- Inter-S1 disturbance: Overlapping file mutations and dependent modifications that can invalidate another worker result.
- Attenuating coordination relation: ACP instructs parent to serialize overlap and parallelize independent file ownership, plus resolve post-report conflicts.
- Feedback into subsequent S1 behaviour: Worker completion reports and post-hoc send_message cause parent to revise subagent tasks or execution sequence.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The explicit file-overlap interference rule and corrective feedback restrict concurrent worker actions for coherence, rather than merely distributing work.
- Evidence: [ACP role steps 3–7](https://github.com/AtomUICommunity/TKCode/blob/620235e49fa0d7a1c7d80136a00414d9a398a102/src/TKCode.Agent.Coding/Assets/SessionRole.cs), [AgentTool concurrency and messaging](https://github.com/AtomUICommunity/TKCode/blob/620235e49fa0d7a1c7d80136a00414d9a398a102/src/TKCode.Agent.Coding/Tools/Agents/AgentTools.cs), [Coordinator reports and notifications](https://github.com/AtomUICommunity/TKCode/blob/620235e49fa0d7a1c7d80136a00414d9a398a102/src/TKCode.AgentHost/AgentCoordinator.cs).
- Basis: structural.
- Confidence: medium-high.
- Caveats: Source proves the model-facing ACP protocol and wired tools, not that every run successfully detects every overlapping write.

## S3 — Inside-and-now control

- State: A
- Function: Manage the engagement's current task commitments, work assignment, integration and corrective interventions across executing workers.
- Disturbance / variety regulated: Incomplete delegation, blocked dependencies, failed implementation, inconsistent outcomes and integration gaps.
- Decisive decision or feedback right: ACP coordinator designs current architecture, creates tasks, assigns files/workers, updates task commitments, reviews reports and dispatches corrective and final verification work.
- Decision owner: First-party ACP coordinator model, with human user resolving scope-changing choices and approving tool calls as needed.
- Supporting / enforcement mechanisms: Shared TaskList, task_create/task_update/task_list, AgentCoordinator, worker reports and inherited permission gates.
- Closure path: Parent sets engagement task plan and owners, receives worker outcomes, revises tasks/assignments, orders corrections and final verification before reporting completion.
- Boundary reachability: Built-in ACP role restricts coordinator tools, shared tasks are wired via AgentHost, and workers inherit parent task list in AgentCoordinator.SpawnAsync.
- Why this is / is not agent-owned: The model makes task prioritization and corrective resource/commitment decisions across the worker system rather than mechanically enforcing a budget or timeout.
- Whole-system current view: Parent ACP model's task list, assigned file boundaries, architecture plan and returned agent reports.
- Current-control decision scope: Task decomposition, agent assignment, dependency/parallel sequencing, rework and final integration assurance.
- Evidence: [ACP controlling instructions](https://github.com/AtomUICommunity/TKCode/blob/620235e49fa0d7a1c7d80136a00414d9a398a102/src/TKCode.Agent.Coding/Assets/SessionRole.cs), [task management API](https://github.com/AtomUICommunity/TKCode/blob/620235e49fa0d7a1c7d80136a00414d9a398a102/src/TKCode.Agent.Coding/Tools/Tasks/TaskTools.cs), [shared work/task registration](https://github.com/AtomUICommunity/TKCode/blob/620235e49fa0d7a1c7d80136a00414d9a398a102/src/TKCode.AgentHost/AgentCoordinator.cs).
- Basis: structural.
- Confidence: medium-high.
- Caveats: S3 is established for the optional ACP coding engagement, not for a project-wide institution or ordinary one-agent session.

## S3* — Complementary audit

- State: —
- Function: No separately owned complementary audit channel challenges the parent engagement management independently.
- Disturbance / variety regulated: Defects or omissions in worker outputs can trigger routine verification, but independence is not established.
- Decisive decision or feedback right: The same coordinator may ask a subagent to run tests/review; no independent auditor owns a privileged S3*-to-S3 challenge right.
- Decision owner: ACP parent delegates verification and evaluates worker reports.
- Supporting / enforcement mechanisms: ACP step 7 verification delegation, test/command tools, AgentTool reports and task records.
- Closure path: Verification reports return through the ordinary delegated-task channel into the same parent, not an independent complementary audit channel.
- Why this is / is not agent-owned: A verification subagent is a worker appointed and scoped by the same plan owner; this is normal S3 quality checking unless separate access/independent challenge and corrective accountability are shown.
- Evidence: [ACP review/verification instructions](https://github.com/AtomUICommunity/TKCode/blob/620235e49fa0d7a1c7d80136a00414d9a398a102/src/TKCode.Agent.Coding/Assets/SessionRole.cs), [subagent report delivery](https://github.com/AtomUICommunity/TKCode/blob/620235e49fa0d7a1c7d80136a00414d9a398a102/src/TKCode.AgentHost/AgentCoordinator.cs), [task tools](https://github.com/AtomUICommunity/TKCode/blob/620235e49fa0d7a1c7d80136a00414d9a398a102/src/TKCode.Agent.Coding/Tools/Tasks/TaskTools.cs).
- Basis: structural.
- Confidence: medium-high.
- Caveats: A human could arrange independent review outside the shown standard runtime; not credited here.

### Absence scope

- Surfaces inspected: ACP role instruction, first-party subagent lifecycle, task updates, plan review and test delegation.
- Plausible first-party paths checked: Verification subagents, read-only explore/plan roles, external agent reviews and host permission prompts.
- Why no material first-party path remains: These are under the same coordinator or operator and lack a reconstructable complementary independent audit judgment returned to S3.

## S4 — Outside-and-then intelligence

- State: —
- Function: No demonstrated prospective environmental/capability adaptation beyond executing the current coding assignment.
- Disturbance / variety regulated: Unforeseen code and user requirements trigger local planning and replanning, not harness-wide future adaptation.
- Decisive decision or feedback right: ACP model plans the present implementation and handles source contingencies; it does not own an external-future capability strategy.
- Decision owner: Agent/ACP parent for current work; developer/operator for future TKCode capability changes.
- Supporting / enforcement mechanisms: Plan role, ask_user, task creation, model/runtime selection and user-configured roles.
- Closure path: Task plans feed current implementation, not an external-capability proposal into a distinct S3 management decision.
- Why this is / is not agent-owned: A code implementation plan or selectable model is not an organizational future/environment intelligence right.
- Evidence: [Plan/ACP role](https://github.com/AtomUICommunity/TKCode/blob/620235e49fa0d7a1c7d80136a00414d9a398a102/src/TKCode.Agent.Coding/Assets/SessionRole.cs), [session roles/options](https://github.com/AtomUICommunity/TKCode/blob/620235e49fa0d7a1c7d80136a00414d9a398a102/src/TKCode.AgentHost/SessionOptions.cs), [README](https://github.com/AtomUICommunity/TKCode/blob/620235e49fa0d7a1c7d80136a00414d9a398a102/README.md).
- Basis: structural.
- Confidence: medium-high.
- Caveats: Real product roadmapping is outside the scoped runtime.

### Absence scope

- Surfaces inspected: Agent/Plan/ACP roles, session options, design references, task and worker management.
- Plausible first-party paths checked: Planning mode, broad codebase exploration, model/provider switching and custom roles.
- Why no material first-party path remains: No separate future environmental sensing, prospective system adaptation choice and return into present capabilities are traced.

## S5 — Policy and identity

- State: —
- Function: No autonomous or function-specific parent runtime identity/ultimate-policy governance is established.
- Disturbance / variety regulated: User instructions, security permissions and safety rules affect tool execution.
- Decisive decision or feedback right: Human approves or refuses individual actions; built-in modes and permissions enforce preset limits, not legitimate policy-level adjudication.
- Decision owner: User/maintainers for identity and policies; code restricts tool scope.
- Supporting / enforcement mechanisms: Ask/autoApprove/fullAccess, Plan approvals, role filters, prompt limits and workspace permission checks.
- Closure path: Tool approval gates an individual action or plan; no identity-level conflict moves through ultimate authority and returns as revised governing policy.
- Why this is / is not agent-owned: Operator approval and static permission modes do not establish an S5 policy decision/feedback organization at engagement recursion.
- Evidence: [session permission modes](https://github.com/AtomUICommunity/TKCode/blob/620235e49fa0d7a1c7d80136a00414d9a398a102/src/TKCode.AgentHost/SessionOptions.cs), [session approval bridge](https://github.com/AtomUICommunity/TKCode/blob/620235e49fa0d7a1c7d80136a00414d9a398a102/src/TKCode.AgentHost/SessionManager.cs), [role filters](https://github.com/AtomUICommunity/TKCode/blob/620235e49fa0d7a1c7d80136a00414d9a398a102/src/TKCode.Agent.Coding/Assets/SessionRole.cs).
- Basis: structural.
- Confidence: high.
- Caveats: Corporate or repository governance should not be inferred from runtime UI controls.

### Absence scope

- Surfaces inspected: Role resolution and permissions, user/plan approvals, system prompts and session options.
- Plausible first-party paths checked: ACP user choices, task approvals, project instructions and tool enforcement.
- Why no material first-party path remains: There is no explicit ultimate-policy issue, legitimate deciding authority, policy verdict and changed subsequent operation at this recursion.

## Distributed OSS parent arrangement

The software supports a per-engagement local ACP parent with shared worker state, not a demonstrated cross-contributor OSS project control plane. The separate repository maintainers and external models are not imported into these S2/S3 credits.

## Self-hosted and non-human modes

Built-in self-hosted Agent and optional ACP share the same first-party implementation. ACP supports model-owned S2/S3 current coordination; Plan and operator permissions are valid supervised modes but not a complete separate parent S4/S5 governance return.

## Recursion

In ACP, subagents are operational S1 cells within one coding engagement; the ACP parent coordinates and manages their present tasks. The default solo agent has only the S1 loop. A desktop host can have multiple sessions without establishing a common governing recursion among them.

## Variety and escalation

File overlap is anticipated before dispatch; downstream worker progress and failure reports provide corrective feedback. Scope-changing decisions escalate to the user, and low-level permission checks can stop tools. Neither escalation is by itself S5 policy arbitration.

## Evidence gaps

This is a structural source assessment, without a live desktop/model integration run, actual concurrent-file conflict reproduction or independent review-channel exercise. ACP model prompts specify coordination policy but do not guarantee every model execution follows it.

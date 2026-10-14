---
harness_id: deepcode
project_name: DeepCode
repository: https://github.com/HKUDS/DeepCode
review_ref: 2b223c13fd36a574157751e3812c1cdebd8921c6
reviewed_at: 2026-10-12
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# DeepCode

## Review boundary
- System in focus: frozen first-party HKUDS DeepCode code-editing agent and native subagent team inside its shared CLI/Desktop/Web agent runtime, including its model/tool loop and parent-team orchestration.
- Purpose and identity: carry out software engineering goals, inspect and change source files, validate work and delegate independent bounded tasks to coding subagents.
- Relevant environment: user repository and Git worktrees, model outputs, tools/shell tests, runtime observations, native child tasks, persisted sessions and current user approvals.
- Standard-distribution boundary: shipped shared DeepCode Python agent runtime and its native `spawn_agent` / `wait_agent` / `send_message` tools. External Codex/Claude Code CLI backend agents, upstream models, user-created external MCP servers, developer CI and demo-only workflows excluded ([README.md](https://github.com/HKUDS/DeepCode/blob/2b223c13fd36a574157751e3812c1cdebd8921c6/README.md); [core/harness/agents/control.py](https://github.com/HKUDS/DeepCode/blob/2b223c13fd36a574157751e3812c1cdebd8921c6/core/harness/agents/control.py)).
- Credited operating / distribution surfaces: [core/agent_runtime/runner.py](https://github.com/HKUDS/DeepCode/blob/2b223c13fd36a574157751e3812c1cdebd8921c6/core/agent_runtime/runner.py); [core/harness/agents/control.py](https://github.com/HKUDS/DeepCode/blob/2b223c13fd36a574157751e3812c1cdebd8921c6/core/harness/agents/control.py); [core/harness/tools/spawn_agent.py](https://github.com/HKUDS/DeepCode/blob/2b223c13fd36a574157751e3812c1cdebd8921c6/core/harness/tools/spawn_agent.py); [core/team/worktree.py](https://github.com/HKUDS/DeepCode/blob/2b223c13fd36a574157751e3812c1cdebd8921c6/core/team/worktree.py); [core/agent_runtime/runtime.py](https://github.com/HKUDS/DeepCode/blob/2b223c13fd36a574157751e3812c1cdebd8921c6/core/agent_runtime/runtime.py); [core/application/worktree_service.py](https://github.com/HKUDS/DeepCode/blob/2b223c13fd36a574157751e3812c1cdebd8921c6/core/application/worktree_service.py); [core/application/test_service.py](https://github.com/HKUDS/DeepCode/blob/2b223c13fd36a574157751e3812c1cdebd8921c6/core/application/test_service.py); [core/loop/autodream.py](https://github.com/HKUDS/DeepCode/blob/2b223c13fd36a574157751e3812c1cdebd8921c6/core/loop/autodream.py).
- Adjacent first-party surfaces excluded from ownership: third-party model/CLI native agent plans and policies, CI/test fixture organization, uninstalled custom plugins or workflow definitions, unspecific hosted services and user-controlled future repository governance.
- First-party operating / deployment modes considered: user code goal with streaming model/tool cycle; opt-in/available native background subagents; default worktree isolation, child merge and failure feedback; task-status and live-message controls; project/session automation, direct tests and autonomous memory consolidation.
- Recursion level: one DeepCode root coding-agent session with its separately running native coding worker team; not every user thread, the GitHub project's organization or external CLI providers.
- Reviewed revision: `2b223c13fd36a574157751e3812c1cdebd8921c6`.
- Observation date: 2026-10-12.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture
The first-party AgentRunner streams model outputs into a tool execution pipeline and loops with tool results. A model-facing `SpawnAgentTool` creates non-blocking child sessions, each with separate native runtime and its own prompt/tool context, subject to bounded concurrency and parent-scoped control. `WaitAgentTool`, `ListAgentsTool`, `InterruptAgentTool` and `SendMessageTool` give the model parent status/feedback and a way to revise active child work. [core/agent_runtime/runner.py](https://github.com/HKUDS/DeepCode/blob/2b223c13fd36a574157751e3812c1cdebd8921c6/core/agent_runtime/runner.py#L458-L645); [core/harness/agents/control.py](https://github.com/HKUDS/DeepCode/blob/2b223c13fd36a574157751e3812c1cdebd8921c6/core/harness/agents/control.py#L278-L395); [core/harness/tools/spawn_agent.py](https://github.com/HKUDS/DeepCode/blob/2b223c13fd36a574157751e3812c1cdebd8921c6/core/harness/tools/spawn_agent.py).
Native worker tasks use isolated Git worktrees by default, then first-party merge logic attempts to integrate work back into the base. Git's 3-way merge explicitly detects overlapping-line conflict; on conflict the merge is aborted and conflicting filenames are returned to the parent, rather than silently overwriting results. A base-Git lock prevents concurrent merges from racing. That is a concrete inter-S1 interference attenuator tied to the write hazard, distinct from generic queueing. [core/team/worktree.py](https://github.com/HKUDS/DeepCode/blob/2b223c13fd36a574157751e3812c1cdebd8921c6/core/team/worktree.py#L1-L18); [core/team/worktree.py](https://github.com/HKUDS/DeepCode/blob/2b223c13fd36a574157751e3812c1cdebd8921c6/core/team/worktree.py#L141-L220); [core/harness/agents/control.py](https://github.com/HKUDS/DeepCode/blob/2b223c13fd36a574157751e3812c1cdebd8921c6/core/harness/agents/control.py#L445-L547).
A first-party test command service and goal tools exist alongside model-loop verification helpers and an `autodream` memory consolidation pass. These do not in themselves establish an independent audit judgment, a prospective outside-and-then capability-adaptation owner, or ultimate organizational policy governance. [core/application/test_service.py](https://github.com/HKUDS/DeepCode/blob/2b223c13fd36a574157751e3812c1cdebd8921c6/core/application/test_service.py); [core/harness/tools/goal.py](https://github.com/HKUDS/DeepCode/blob/2b223c13fd36a574157751e3812c1cdebd8921c6/core/harness/tools/goal.py); [core/loop/autodream.py](https://github.com/HKUDS/DeepCode/blob/2b223c13fd36a574157751e3812c1cdebd8921c6/core/loop/autodream.py).

## Operational model
The root model chooses local coding actions and may delegate work to multiple native model-driven workers. First-party `AgentControl` records and limits their active status, injects parent messages, returns results and mediates git worktree merges. Child workloads are actual independently executing S1 operations; root model/host jointly provide scoped current-team control. Not every plugin, model provider or separate workspace thread is credited to this single team.

## S1 — Operations
- State: A
- Function: Model-directed coding and tool action in the root and separately runnable native child sessions.
- Disturbance / variety regulated: Uncertain software tasks, changing file/test state, provider and tool errors, unknown repository details.
- Decisive decision or feedback right: Choose coding/tool actions and adapt to results in first-party model turn loop; workers independently act on assigned coding objectives.
- Decision owner: DeepCode-configured model-driven AgentRunner for root and native worker instances.
- Supporting / enforcement mechanisms: First-party provider request adapter, ToolRegistry, AgentRunner, session context and native child runner.
- Closure path: Goal/task prompt → model/tool calls → observed file/tool result → subsequent model work, completion or repair.
- Boundary reachability: The package's user-facing CLI/Web/Desktop host binds the same native model/tool runner; children are real separately launched AgentSessions rather than simulated example classes ([README.md](https://github.com/HKUDS/DeepCode/blob/2b223c13fd36a574157751e3812c1cdebd8921c6/README.md#L534-L555); [core/agent_runtime/runner.py](https://github.com/HKUDS/DeepCode/blob/2b223c13fd36a574157751e3812c1cdebd8921c6/core/agent_runtime/runner.py#L458-L645); [core/harness/agents/control.py](https://github.com/HKUDS/DeepCode/blob/2b223c13fd36a574157751e3812c1cdebd8921c6/core/harness/agents/control.py#L562-L640)).
- Why this is / is not agent-owned: Model requests drive concrete task-specific operations; deterministic tool admission and loops only constrain acts.
- Evidence: [core/agent_runtime/runner.py](https://github.com/HKUDS/DeepCode/blob/2b223c13fd36a574157751e3812c1cdebd8921c6/core/agent_runtime/runner.py); [core/harness/tools/spawn_agent.py](https://github.com/HKUDS/DeepCode/blob/2b223c13fd36a574157751e3812c1cdebd8921c6/core/harness/tools/spawn_agent.py); [core/harness/agents/control.py](https://github.com/HKUDS/DeepCode/blob/2b223c13fd36a574157751e3812c1cdebd8921c6/core/harness/agents/control.py).
- Basis: structural
- Confidence: high
- Caveats: No provider-backed end-to-end coding benchmark was executed; conclusion is source-relative.

## S2 — Coordination
- State: C
- Function: Attenuate and expose collisions between independently editing child-agent workspaces when returned results are integrated.
- Distinct S1 units: Concurrent native model-driven subagents created by `spawn_agent` with independent prompts, tools, workspaces and result channels.
- Inter-S1 disturbance: Parallel edits can modify overlapping paths/hunks, risking silent overwrite or Git merge conflicts.
- Attenuating coordination relation: Per-worker Git worktree isolation (the native default) prevents concurrent writes into one shared checkout; serialized 3-way merges detect content collisions, abort unsafe integration and return concrete conflict filenames.
- Feedback into subsequent S1 behaviour: Merge success/conflict is included in the parent-visible result text; parent model can revise tasks, inspect conflicts or reroute subsequent child work.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The code directly targets **multiple code-writing worker collisions** with isolation/merge-conflict treatment, not just message delivery or capacity limits.
- Disturbance / variety regulated: Overlapping file write claims and incompatible child-produced patches.
- Decisive decision or feedback right: Admit per-worker worktree and reject unsafe merge based on conflict; parent can choose further remediation.
- Decision owner: Deterministic first-party WorktreeManager and serialized git merge path (`C`), not a separate autonomous conflict-arbitrating model.
- Supporting / enforcement mechanisms: WorktreeManager, base `_git_lock`, 3-way `git merge`, per-child result mailbox and worktree cleanup.
- Closure path: Independent worker changes → isolated staging → serialized conflict-checking merge → collision rejection or safe application → error/result to parent for next agent task choices.
- Boundary reachability: The shipped native subagent path activates the worktree manager with `isolate=True` by default and returns merged result through the live parent inbox ([core/harness/agents/control.py](https://github.com/HKUDS/DeepCode/blob/2b223c13fd36a574157751e3812c1cdebd8921c6/core/harness/agents/control.py#L445-L547); [core/team/worktree.py](https://github.com/HKUDS/DeepCode/blob/2b223c13fd36a574157751e3812c1cdebd8921c6/core/team/worktree.py#L174-L219)).
- Why this is / is not agent-owned: The content-aware merge gate is deterministic policy; it materially coordinates workers without its own agentic policy autonomy.
- Evidence: [core/harness/agents/control.py](https://github.com/HKUDS/DeepCode/blob/2b223c13fd36a574157751e3812c1cdebd8921c6/core/harness/agents/control.py#L1-L20); [core/harness/agents/control.py](https://github.com/HKUDS/DeepCode/blob/2b223c13fd36a574157751e3812c1cdebd8921c6/core/harness/agents/control.py#L445-L547); [core/team/worktree.py](https://github.com/HKUDS/DeepCode/blob/2b223c13fd36a574157751e3812c1cdebd8921c6/core/team/worktree.py#L141-L219).
- Basis: explicit
- Confidence: high
- Caveats: Only for native worktree mode; `isolate=False` and external CLI tools do not automatically receive this guarantee.

## S3 — Inside-and-now control
- State: A
- Function: Model-led parent makes and revises current coding-team commitments across active child operating agents.
- Disturbance / variety regulated: Pending/running child subtasks, failure/interrupts, completion and changed requirements in the root goal.
- Decisive decision or feedback right: Choose what tasks to delegate, inspect child roster/results, wait for completions, interrupt and steer a live worker with revised intent.
- Decision owner: DeepCode root model-driven agent through first-party child-management tools; registry is enforcement rather than the decision owner.
- Supporting / enforcement mechanisms: AgentControl roster, active-count capacity, child task inbox, wait/list/send/interrupt tools, root goal/turn state.
- Whole-system current view: Parent sees bounded root-team child status and returned results; not all multi-tenant projects or external model organizations.
- Current-control decision scope: Allocate/suspend/revise work commitments of multiple running child agents and integrate their outcomes.
- Closure path: Worker report/merge result → parent model perceives progress/conflict → changes child assignment, sends correction/interruption or resumes root work.
- Boundary reachability: `spawn_agent`, `list_agents`, `wait_agent`, `interrupt_agent` and `send_message` are actual model-facing shipped tools using the same AgentControl, not passive dashboard labels ([core/harness/tools/spawn_agent.py](https://github.com/HKUDS/DeepCode/blob/2b223c13fd36a574157751e3812c1cdebd8921c6/core/harness/tools/spawn_agent.py); [core/harness/agents/control.py](https://github.com/HKUDS/DeepCode/blob/2b223c13fd36a574157751e3812c1cdebd8921c6/core/harness/agents/control.py#L190-L255)).
- Why this is / is not agent-owned: Consequential team commitment choices are model-generated while the deterministic coordinator only executes them.
- Evidence: [core/harness/tools/spawn_agent.py](https://github.com/HKUDS/DeepCode/blob/2b223c13fd36a574157751e3812c1cdebd8921c6/core/harness/tools/spawn_agent.py); [core/harness/agents/control.py](https://github.com/HKUDS/DeepCode/blob/2b223c13fd36a574157751e3812c1cdebd8921c6/core/harness/agents/control.py); [core/harness/tools/goal.py](https://github.com/HKUDS/DeepCode/blob/2b223c13fd36a574157751e3812c1cdebd8921c6/core/harness/tools/goal.py).
- Basis: explicit
- Confidence: medium
- Caveats: Team-level current-control only; no organization-wide portfolio governance claimed.

## S3* — Complementary audit
- State: ?
- Function: Verification/test services expose actual code outcomes, but material separation from the producing agent's routine task-check-and-repair path remains unestablished.
- Disturbance / variety regulated: Incorrect code completion claims, failing test/build outcomes and missing task artifacts.
- Decisive decision or feedback right: Agent/user may run tests and respond to verifier feedback, but no separately controlled complementary auditor obligation or sample selection proved.
- Decision owner: Main AgentRunner/user in normal execution; independent audit owner unresolved.
- Supporting / enforcement mechanisms: TestService, tool invocation and goal verification, persisted test/turn artifacts.
- Claim being audited: That new code meets task requirements.
- Ordinary reporting path: Agent reports code changes and goal completion, including own test/build results.
- Complementary access path: First-party TestService can independently execute test commands against code artifacts, but this is also a normal step in the coding task.
- Independence boundary: Materially distinct artifact observation exists, yet first-party independently controlled complementary sampling/judgment is not established.
- Who acts on findings: Main coding agent/user may perform repair, but no distinct auditor-to-parent corrective loop is guaranteed.
- Closure path: Code artifact → test command/result → agent task continuation or display; remains ambiguous ordinary S1 verification versus S3*.
- Why this is / is not agent-owned: Routine code tests and verifier prompts do not qualify without separate sufficiently independent operational-audit authority.
- Evidence: [core/application/test_service.py](https://github.com/HKUDS/DeepCode/blob/2b223c13fd36a574157751e3812c1cdebd8921c6/core/application/test_service.py); [core/agent_runtime/runner.py](https://github.com/HKUDS/DeepCode/blob/2b223c13fd36a574157751e3812c1cdebd8921c6/core/agent_runtime/runner.py); [core/harness/tools/goal.py](https://github.com/HKUDS/DeepCode/blob/2b223c13fd36a574157751e3812c1cdebd8921c6/core/harness/tools/goal.py).
- Basis: unknown
- Confidence: low
- Caveats: Inspect first-party reviewer roles/goal-completion evidence and operational artifact sampling before moving to bounded negative or positive.

## S4 — Outside-and-then intelligence
- State: ?
- Function: Automation, skills and `autodream` memory consolidation may alter future agent context, but no proven external, prospective option-to-capability adaptation closure.
- Disturbance / variety regulated: Changing technology/project environment, repeated mistakes and future capability needs.
- Decisive decision or feedback right: Unknown whether first-party agent can select future organizational redesign instead of merely recalling memory or rerunning tasks.
- Decision owner: Unresolved across user/workflow authors, model task agent and background memory consolidator.
- Supporting / enforcement mechanisms: Skills and presets, automation scheduler, persistent session memory, autodream pass.
- External distinction: Tool/web facts and task history are accessible, but explicit scanning of external future opportunities and threats has not been tied to organizational adaptation.
- Future / prospective distinction: Consolidated memory changes future prompts; not necessarily outside-and-then intelligence.
- Adaptation option generated: No verified future capability-changing alternative and organizational choice owner.
- Path back into current capability / S3: Memory/instructions can shape new sessions; capability redesign or a returned future plan is unresolved.
- Closure path: Prior task events → memory consolidation → later context, incomplete prospective adaptation/feedback closure.
- Why this is / is not agent-owned: Long-term memory and scheduled tasks alone are not S4.
- Evidence: [core/loop/autodream.py](https://github.com/HKUDS/DeepCode/blob/2b223c13fd36a574157751e3812c1cdebd8921c6/core/loop/autodream.py); [core/application/automation_scheduler.py](https://github.com/HKUDS/DeepCode/blob/2b223c13fd36a574157751e3812c1cdebd8921c6/core/application/automation_scheduler.py); [core/harness/tools/goal.py](https://github.com/HKUDS/DeepCode/blob/2b223c13fd36a574157751e3812c1cdebd8921c6/core/harness/tools/goal.py); [core/harness/agents/control.py](https://github.com/HKUDS/DeepCode/blob/2b223c13fd36a574157751e3812c1cdebd8921c6/core/harness/agents/control.py).
- Basis: unknown
- Confidence: low
- Caveats: Investigate active external-scan and authorized plan adoption before reclassifying S4.

## S5 — Policy and identity
- State: ?
- Function: App-level trust, permissions, execution security policy and profile configuration constrain agent behavior but ultimate organizational identity/policy feedback at the assessed team recursion remains uncertain.
- Disturbance / variety regulated: Unauthorized tool changes, unsafe workspace modifications, role capabilities and user trust.
- Decisive decision or feedback right: Operator/app grants permissions and chooses profiles; no source-grounded ultimate purpose and identity-policy decision owner reconstructed.
- Decision owner: Operator and deterministic permission/security engine; qualified ultimate parent S5 not proven.
- Supporting / enforcement mechanisms: ExecutionSecurityPolicy, approval service, tool allowlists, project trust and session profile.
- Identity / ultimate-policy issue: Which purpose, limits and authority the DeepCode team follows across ongoing operations.
- Ultimate authority in each claimed mode: User/developer governs static settings; not a proved adaptive ultimate-policy parent mode.
- Return-to-operation path: Permissions and trust checks alter allowed tool actions, lacking an organizational purpose challenge and return loop.
- Closure path: Approval/policy → execution allow/deny; organizational policy evolution/return unresolved.
- Why this is / is not agent-owned: Enforced permissions are not ultimate governance decisions by themselves.
- Evidence: [core/application/execution_security_policy.py](https://github.com/HKUDS/DeepCode/blob/2b223c13fd36a574157751e3812c1cdebd8921c6/core/application/execution_security_policy.py); [core/application/approval_service.py](https://github.com/HKUDS/DeepCode/blob/2b223c13fd36a574157751e3812c1cdebd8921c6/core/application/approval_service.py); [core/application/agent_adapter.py](https://github.com/HKUDS/DeepCode/blob/2b223c13fd36a574157751e3812c1cdebd8921c6/core/application/agent_adapter.py).
- Basis: unknown
- Confidence: low
- Caveats: A future source-specific owner/policy-change closure may resolve the uncertainty; no S5 state is inferred from product policy labels.

## Recursion
One model-driven coding run is an operating S1 unit. Native independent child coding runs add separately operating S1 units; their worktree-safe integration supports structural S2 in bounded parallel mode. The root model can adjust current child assignments and conflicts (S3=A) in the declared task-team recursion; providers and external coding CLIs are not included as first-party organizational owners.

## Variety and escalation
The agent loop regulates model/tool task disturbances. Git worktree merge conflicts protect parallel changes and report interference to the parent. Child mailbox/status provides current-control observations, while testing/verification, memory and permission checks are not automatically independent audit, prospective adaptation or identity-policy.

## Evidence gaps
Source-first static review of one immutable upstream SHA; no live model-backed work. Distinct verification/audit ownership (S3*), future-intelligence capability adaptation (S4) and ultimate-policy/identity feedback (S5) remain open with stated plausible first-party paths; unknown is not a universal negative.

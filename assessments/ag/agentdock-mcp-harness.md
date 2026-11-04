---
harness_id: agentdock-mcp-harness
project_name: AgentDock MCP Harness
repository: https://github.com/gabyic/agentdock-mcp-harness
review_ref: d5f06ba7c712be032ff7788175cb04d322bead7b
reviewed_at: 2026-11-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# AgentDock MCP Harness

## Review boundary

- System in focus: the installed AgentDock MCP execution service *with its explicitly supported external chat-model MCP client*, carrying out one remote software-engineering task and its durable guided-development workflow.
- Purpose and identity: let a ChatGPT/Claude/other MCP-capable chat reasoning agent inspect, edit, test, commit and complete code work on a Linux server with persistent worktree/task/evidence state, without a second server-side model.
- Relevant environment: user Git repositories, remote Linux commands and files, tool-call results, resumable tasks, process crashes/disconnects, approval/policy settings, workflow phase and outstanding product decisions.
- Standard-distribution boundary: first-party MCP tool registration, task/plan/workflow/skill/approval/process/git services, installable user-local Linux service and documented chat-model invocation. The external chat model provides the explicitly integrated autonomous decision actor; its unrelated capabilities, hidden prompts, account plans or unspecified subagent tools are not credited.
- Credited operating / distribution surfaces: [README architecture and user flow](https://github.com/gabyic/agentdock-mcp-harness/blob/d5f06ba7c712be032ff7788175cb04d322bead7b/README.md), [MCP server tool contract](https://github.com/gabyic/agentdock-mcp-harness/blob/d5f06ba7c712be032ff7788175cb04d322bead7b/src/server.js), [durable tasks](https://github.com/gabyic/agentdock-mcp-harness/blob/d5f06ba7c712be032ff7788175cb04d322bead7b/src/task-service.js), [workflow service](https://github.com/gabyic/agentdock-mcp-harness/blob/d5f06ba7c712be032ff7788175cb04d322bead7b/src/workflow-service.js), and [guided-development protocol](https://github.com/gabyic/agentdock-mcp-harness/blob/d5f06ba7c712be032ff7788175cb04d322bead7b/docs/guided-development.md).
- Adjacent first-party surfaces excluded from ownership: developer release/CI scripts, roadmap documents, private chat-vendor agent internals, uninstalled third-party Matt Pocock skills (including their review subagents), deployment's TLS/OAuth proxy, and human project-owner decisions.
- First-party operating / deployment modes considered: live connected chat-model MCP task session; resumed existing Task/Workflow across disconnects; optional installed Git skill resources and Auto Matt routing where configured; deterministic Plan runner with explicit reasoning/human barriers; user approval/policy modes. No server-side autonomous LLM or model scheduler is claimed.
- Recursion level: one integrated chat-agent remote coding task with durable project-specific workflow, not the chat platform's entire organization.
- Reviewed revision: `gabyic/agentdock-mcp-harness@d5f06ba7c712be032ff7788175cb04d322bead7b` (MIT).
- Observation date: 2026-11-04.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

AgentDock is a user-installed Node MCP server that exposes structured tools for workspace Tasks, isolated Git worktrees, file search/write, processes/test output, commits, approvals, plan execution, skills and durable guided workflows. Its architecture expressly keeps reasoning and tool selection in the connected chat model, not the server. The server implements deterministic policy and idempotency, durable records, task/plan lifecycles, crash/reconnect reconciliation and audit. A first-party `skill.invoke` boundary supplies installed instructions to the chat model, with optional `auto` routing; `workflow.guide` supplies persisted phase/open-decision context and recommendations but explicitly never executes a skill. The model makes the content and next-action decisions and invokes MCP operations. [README](https://github.com/gabyic/agentdock-mcp-harness/blob/d5f06ba7c712be032ff7788175cb04d322bead7b/README.md), [Guided Development](https://github.com/gabyic/agentdock-mcp-harness/blob/d5f06ba7c712be032ff7788175cb04d322bead7b/docs/guided-development.md), [workflow code](https://github.com/gabyic/agentdock-mcp-harness/blob/d5f06ba7c712be032ff7788175cb04d322bead7b/src/workflow-service.js).

## Operational model

When a user asks the connected chat agent to fix code, it may create a worktree-backed Task, read and edit project files through AgentDock, run tests, inspect results, iterate and finish with a commit/evidence. In guided development, the same chat agent must interpret current work, choose the next suitable installed skill and explicitly advance permitted workflow boundaries; a persistent phase machine prevents skipping outstanding human/product decisions. This is a *composed first-party integration mode*, not a claim that AgentDock itself runs an autonomous LLM on the server. Without a connected autonomous chat client, only the deterministic MCP service remains and no autonomous S1 runs.

## S1 — Operations

- State: A
- Function: complete user-requested remote code investigation, editing, test and commit work via the explicitly supported chat agent/MCP service combination.
- Disturbance / variety regulated: changing code/task conditions, failing tests, external command output and bugs requiring choices that cannot be predetermined by a tool schema.
- Decisive decision or feedback right: the connected chat model interprets files and test feedback, chooses which edit or command to perform, decides whether to retry, and invokes task completion with evidence.
- Decision owner: the external MCP-capable chat *agent in the documented AgentDock operating mode*; first-party AgentDock tools execute and persist its selected actions without a server-side second model.
- Supporting / enforcement mechanisms: `task.create`, file/read/patch tools, `process.start`, Git worktree/commit, approval/policy gates, persisted Task state and audit trail.
- Closure path: user coding objective → chat agent inspects remote repository through MCP → agent chooses source edits/tests → AgentDock executes and returns actual results → same agent revises or completes the Task.
- Boundary reachability: README documents live ChatGPT Web end-to-end acceptance and ships an installable MCP endpoint with executable file/process/git/task tools for that exact use; the external chat model is a required explicitly supported runtime component, not an unrelated adjacent coding product credited by assumption.
- Why this is / is not agent-owned: the server's process/tool implementations are deterministic and cannot decide the meaning of a failing test or appropriate fix; the integrated chat agent makes that discretionary operational choice.
- Evidence: [README execution loop and boundary](https://github.com/gabyic/agentdock-mcp-harness/blob/d5f06ba7c712be032ff7788175cb04d322bead7b/README.md), [registered MCP tools](https://github.com/gabyic/agentdock-mcp-harness/blob/d5f06ba7c712be032ff7788175cb04d322bead7b/src/server.js), [task worktree state](https://github.com/gabyic/agentdock-mcp-harness/blob/d5f06ba7c712be032ff7788175cb04d322bead7b/src/task-service.js).
- Basis: explicit and structural.
- Confidence: medium.
- Caveats: this positive claim depends on the first-party documented *composite* chat-agent mode. AgentDock's server in isolation has no reasoning agent, nor does the package guarantee any specific ChatGPT/Claude subscription quota.

## S2 — Coordination

- State: —
- Function: no separately established coordination decision/feedback loop among distinct simultaneously operating S1 agents.
- Disturbance / variety regulated: multiple tasks may touch the same Git source and processes may have competing leases, but the implementation separates worktree state and reconciles ownership deterministically.
- Decisive decision or feedback right: no specific autonomous inter-agent coordination right found; worktree allocation and owner leases enforce fixed rules.
- Decision owner: Git/worktree, task/lease and process reconciliation machinery; ordinary chat-agent task planning and phase changes belong to S3, not S2.
- Supporting / enforcement mechanisms: isolated Git worktrees per write-capable Task, persistent task IDs, process execution-owner leases, idempotency keys and task reconciliation.
- Closure path: separate task worktrees and lease checks prevent cross-write contamination or false resumption; no distinct coordination judgment is returned to change another S1 agent's behavior.
- Why this is / is not agent-owned: concurrency-safe storage and isolation protect operations, but the shipped mode does not provide a first-party multi-agent cross-S1 regulator.
- Evidence: [README worktree and crash handling](https://github.com/gabyic/agentdock-mcp-harness/blob/d5f06ba7c712be032ff7788175cb04d322bead7b/README.md), [task service](https://github.com/gabyic/agentdock-mcp-harness/blob/d5f06ba7c712be032ff7788175cb04d322bead7b/src/task-service.js), [process reconciliation](https://github.com/gabyic/agentdock-mcp-harness/blob/d5f06ba7c712be032ff7788175cb04d322bead7b/src/task-reconcile-service.js).
- Basis: structural.
- Confidence: medium.
- Caveats: one connected chat client may use external subagent features, but such unbundled features are not AgentDock-owned S2 evidence.

### Absence scope

- Surfaces inspected: MCP registration, task/worktree management, leases/reconciliation, guided workflow and plan driver.
- Plausible first-party paths checked: concurrent tasks, process lease recovery, Git worktree isolation, workflow phase dependencies and optional installed external skills.
- Why no material first-party path remains: all established interactions involve deterministic state separation or sequential work of the same chat agent; no shipped distinct-S1 corrective coordination decision and returned feedback loop is established.

## S3 — Inside-and-now control

- State: A
- Function: control current whole coding-workflow commitments, route the active software project through explicit phases, and decide whether to continue, correct, or finish the task.
- Disturbance / variety regulated: vague user goals, unresolved product decisions, unfinished implementation, failed verification and interrupted sessions can cause inappropriate transitions or premature completion.
- Decisive decision or feedback right: the integrated chat agent classifies the work, chooses the next step/skill from current Task and workflow status, records open decisions, proposes or revises bounded work plans, and invokes permitted transitions after substantive acceptance. The server refuses invalid transitions and protects human decision boundaries.
- Decision owner: the connected chat agent for task-specific current work choice; user retains original requirements and necessary product/approval decisions, while the finite-state engine only enforces allowed transitions.
- Supporting / enforcement mechanisms: `workflow.start/status/guide/update/advance`, durable state, recommended skills, `plan` steps and explicit reasoning/human barriers, Task completion contracts and approval records.
- Closure path: persisted whole-task goal/phase and unresolved decisions → chat agent interprets current project condition and chooses next commitment → AgentDock records phase/plan/task action → the next work iteration uses the updated state or stops at an unresolved human boundary.
- Boundary reachability: the shipped MCP server exposes these workflow and Plan endpoints and documents their normal use by a chat agent responding to 'continue this project'; no server-side planner is presumed.
- Why this is / is not agent-owned: the server can suggest a skill and reject an illegal phase jump, but the agent makes the contextual choice about the phase's actual completion, suitable task actions and evidence needed for acceptance.
- Whole-system current view: one repository's durable project goal, phase, open decisions, artifact paths, recommended next skill, task/worktree status and recent tool outputs.
- Current-control decision scope: current project phase, task commitments, action order, next required evidence and final task completion within this user-authorized software job.
- Evidence: [workflow guidance and explicit transitions](https://github.com/gabyic/agentdock-mcp-harness/blob/d5f06ba7c712be032ff7788175cb04d322bead7b/docs/guided-development.md), [workflow implementation](https://github.com/gabyic/agentdock-mcp-harness/blob/d5f06ba7c712be032ff7788175cb04d322bead7b/src/workflow-service.js), [plan barriers](https://github.com/gabyic/agentdock-mcp-harness/blob/d5f06ba7c712be032ff7788175cb04d322bead7b/src/plan-service.js).
- Basis: explicit and structural.
- Confidence: medium.
- Caveats: there is a single integrated chat reasoning actor; this is a task/workflow S3 role, not a claim that the AgentDock server independently manages multiple agent workers. Generic human approval is insufficient to add `(P)` at this boundary.

## S3* — Complementary audit

- State: —
- Function: no first-party independent audit of the chat agent's whole-task control and claims using complementary operational access.
- Disturbance / variety regulated: a wrong edit or premature completion could pass the same agent's review; some evidence is independently recorded but audit judgment is not delegated to an independent actor by the core distribution.
- Decisive decision or feedback right: no shipped separate auditor with an independent model judgment and corrective return to S3 is wired; test exit codes, process logs and user audit records are factual checks.
- Decision owner: same chat agent and optional human reviewer; any Standards/Spec multi-pass review is instruction from separately installed upstream skills, not a bundled independent audit mode.
- Supporting / enforcement mechanisms: structured event audit, Git diffs, test completion evidence, `workflow` review phase and third-party `code-review` skill compatibility.
- Closure path: operational records → original model/user inspection; no first-party independent complementary-audit verdict cycle is established.
- Why this is / is not agent-owned: deterministic verification and two sequential passes in one context do not by themselves create an independent S3* actor.
- Evidence: [audit and checks](https://github.com/gabyic/agentdock-mcp-harness/blob/d5f06ba7c712be032ff7788175cb04d322bead7b/README.md), [upstream skill dependency and missing host subagents](https://github.com/gabyic/agentdock-mcp-harness/blob/d5f06ba7c712be032ff7788175cb04d322bead7b/docs/guided-development.md), [audit service](https://github.com/gabyic/agentdock-mcp-harness/blob/d5f06ba7c712be032ff7788175cb04d322bead7b/src/audit-service.js).
- Basis: explicit and structural.
- Confidence: high.
- Caveats: a connected host might independently supply specialized reviewers, but they are not guaranteed or first-party packaged here.

### Absence scope

- Surfaces inspected: audit service, process/test evidence, README review loop, guided workflow review phase, `skill.invoke` and Auto Matt routing.
- Plausible first-party paths checked: task completion evidence, Standards/Spec review, independent subagent support, user approval and raw Git diff audit.
- Why no material first-party path remains: installed upstream skills are optional/unmodified; documentation explicitly says AgentDock creates no second model or subagent runtime, and its own audit is stored evidence without independent audit judgment.

## S4 — Outside-and-then intelligence

- State: —
- Function: no evidenced prospective sensing/adaptation of the AgentDock work-cell's future operating capability.
- Disturbance / variety regulated: future task environments or installed skills may change, but the service's guidance and skill updates are operator-initiated tools rather than an S4 intelligence loop.
- Decisive decision or feedback right: none beyond user-authorized current software planning and explicit installed skill updates.
- Decision owner: user for installing/updating skill sources and software releases; external chat agent chooses present coding tasks and workflow steps.
- Supporting / enforcement mechanisms: Git-backed skill install/update, persistent workflow phases, memory of artifacts and status, repository plans.
- Closure path: no first-party outside/then sensing → future adaptation option → capability adoption/feedback loop established for this task cell.
- Why this is / is not agent-owned: planning future *product code* is an S1/S3 coding job, not automatically proactive adaptation of the harness's own capabilities.
- Evidence: [skill/update and workflow scope](https://github.com/gabyic/agentdock-mcp-harness/blob/d5f06ba7c712be032ff7788175cb04d322bead7b/docs/guided-development.md), [managed upgrade explicitly not automatic](https://github.com/gabyic/agentdock-mcp-harness/blob/d5f06ba7c712be032ff7788175cb04d322bead7b/docs/lifecycle.md).
- Basis: structural.
- Confidence: medium.
- Caveats: an installed third-party skill could teach a chat model an adaptation process; that unpinned external logic is not bundled as AgentDock S4.

### Absence scope

- Surfaces inspected: persistent workflows, `skill.install/update/invoke`, release lifecycle, plan driver and readme architecture.
- Plausible first-party paths checked: future project planning, guide recommendations, user-selected skill refresh, provider changes and automatic software upgrade.
- Why no material first-party path remains: these paths are current-work guidance or explicit human-controlled changes without a documented first-party prospective environmental intelligence/adoption loop.

## S5 — Policy and identity

- State: —
- Function: no in-boundary identity/ultimate-policy adjudication path for the AgentDock task system.
- Disturbance / variety regulated: host safety, approvals, task scopes and human product decisions are important constraints but do not constitute identity-level organizational tension.
- Decisive decision or feedback right: no autonomous or legitimate in-boundary parent S5 loop identified; the human sets policy rules and approves/denies sensitive individual actions.
- Decision owner: user/OS administration outside the coding task; deterministic policy service evaluates configured allow/ask/deny rules.
- Supporting / enforcement mechanisms: approval requests, per-task scopes, secret-redacted audit, host/workspace policy, plan human barrier.
- Closure path: configured policy → evaluation and human action approval → tool execution/denial; no identity-level issue escalated to ultimate authority and returned as a governing policy decision.
- Why this is / is not agent-owned: permission grants and a `HUMAN_BARRIER` are operational authorization, not S5 purpose/identity adjudication.
- Evidence: [policy implementation](https://github.com/gabyic/agentdock-mcp-harness/blob/d5f06ba7c712be032ff7788175cb04d322bead7b/src/policy-service.js), [approval service](https://github.com/gabyic/agentdock-mcp-harness/blob/d5f06ba7c712be032ff7788175cb04d322bead7b/src/approval-service.js), [Plan barriers](https://github.com/gabyic/agentdock-mcp-harness/blob/d5f06ba7c712be032ff7788175cb04d322bead7b/src/plan-service.js).
- Basis: structural.
- Confidence: medium.
- Caveats: the host organization may have its own policies, but they are not an assessed AgentDock task-cell S5 loop.

### Absence scope

- Surfaces inspected: MCP policy/approval, plan human barriers, project skill trust model and managed service lifecycle.
- Plausible first-party paths checked: operator approval, task stop/escalation, immutable config, product decisions and upstream project governance.
- Why no material first-party path remains: first-party runtime enforces tool authorization and preserves unresolved human decisions but supplies no specific identity/ultimate-policy adjudication and return-to-operation path at the task recursion.

## Distributed OSS parent arrangement

The OSS maintainer publishes the execution service while independent users connect their own chat agents and choose projects, permissions, skills and installed versions. These independent user task cells do not share a public global governance state. Repository development governance and client-provider policies are not imported as first-party task S5.

## Self-hosted and non-human modes

AgentDock runs on a self-hosted Linux system, but the model's reasoning remains in the user's chat session. Work may continue after reconnect via durable Task/Workflow state; the service cannot continue autonomous reasoning with no connected agent. Operator interaction at reasoning/human barriers is acknowledged without claiming a separate complete S3 `(P)` mode.

## Recursion

One chat agent can operate several durable Tasks and workflow phases; isolated Git worktrees are task boundaries, not automatically separate autonomous S1 organizations. Third-party skills and host-provided subagents are adjacent capabilities unless explicitly configured and evidenced at their own boundary.

## Variety and escalation

Deterministic policy gates can ask the human, deny or allow actions; workflows refuse transitions while open decisions remain and Plans pause at reasoning/human barriers. Process-owner leases detect crashed execution owners, and task audit/commit evidence supports resumption and inspection. These mechanisms support the agent's work but neither independently reason nor supply an S3* audit or S5 adjudication.

## Evidence gaps

- Live remote acceptance is claimed in first-party documentation; this assessment did not run a user's private chat-client integration, so effectiveness and host-provider behavior are not independently verified.
- The boundary explicitly includes a *configured* external chat agent because the product ships no model runtime. An MCP server with no connected reasoning agent has deterministic functions only; the `A` claims apply solely to the first-party documented composite operating mode.
- Optional installed Matt Pocock skill corpus and its independent subagent review procedures are not pinned or bundled as first-party AgentDock mechanisms; no S3* is inferred from them.

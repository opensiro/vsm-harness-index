---
harness_id: androidharness
project_name: AndroidHarness
repository: https://github.com/Sanuu7/AndroidHarness
review_ref: 341bc6252364d298b18bd9f1ab6592e3a67fe514
reviewed_at: 2026-11-10
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# AndroidHarness

## Review boundary

- System in focus: the first-party native Android AI coding-agent and chat harness, with its model-driven Code session, optional task subagents, project/workspace tools and session runtime. The user-controlled Android app is the distribution boundary; Android OS, third-party MCP servers and remote model providers are outside.
- Purpose and identity: inspect and modify real coding projects from a phone using model-selected file, shell, Git, browser and delegated agent tools, with a separate read-only Chat mode.
- Relevant environment: phone filesystem and project workspaces, model endpoints or on-device models, terminal access, Android UI/operator approvals, provider/network failures and optional remote GitHub resources.
- Standard-distribution boundary: Android application → Code/Chat mode → `RunManager.startRun` → `AgentEngine` model/tool loop → registered tools, workspace routing and permission enforcement. Optional first-party background/foreground task delegates are within scope.
- Credited operating / distribution surfaces: [README](https://github.com/Sanuu7/AndroidHarness/blob/341bc6252364d298b18bd9f1ab6592e3a67fe514/README.md), [run manager](https://github.com/Sanuu7/AndroidHarness/blob/341bc6252364d298b18bd9f1ab6592e3a67fe514/app/src/main/java/com/androidharness/app/agent/RunManager.kt), [agent engine](https://github.com/Sanuu7/AndroidHarness/blob/341bc6252364d298b18bd9f1ab6592e3a67fe514/app/src/main/java/com/androidharness/app/agent/AgentEngine.kt), [task tool](https://github.com/Sanuu7/AndroidHarness/blob/341bc6252364d298b18bd9f1ab6592e3a67fe514/app/src/main/java/com/androidharness/app/tools/SubagentTools.kt), [subagent runs](https://github.com/Sanuu7/AndroidHarness/blob/341bc6252364d298b18bd9f1ab6592e3a67fe514/app/src/main/java/com/androidharness/app/agent/SubagentRuns.kt), [subagent control](https://github.com/Sanuu7/AndroidHarness/blob/341bc6252364d298b18bd9f1ab6592e3a67fe514/app/src/main/java/com/androidharness/app/tools/SubagentControlTools.kt).
- Adjacent first-party surfaces excluded from ownership: Android operating-system process scheduler, model vendor policy, Google Play release process, external GitHub repository governance, user project CI and optional third-party plugins/MCP servers. These are not first-party VSM function owners merely because the harness can invoke them.
- First-party modes considered: Code and Chat, plan/act modes, multiple workspaces and chats, foreground/background task delegates, configured named agent roles, scheduled automations, saved task resume and user permission/approval controls.
- Recursion level: Code session and its task delegates as operational units within the installed app. A child context window is not automatically a new viable metasystem.
- Reviewed revision: `341bc6252364d298b18bd9f1ab6592e3a67fe514`, pinned by Index intake #3035.
- Observation date: 2026-11-10.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The [README](https://github.com/Sanuu7/AndroidHarness/blob/341bc6252364d298b18bd9f1ab6592e3a67fe514/README.md) documents an installable Kotlin Android app with agentic Code mode and read-only Chat mode. `RunManager` creates and resumes session jobs in an application coroutine scope, stores live per-session state and current task controls, binds the workspace, and delegates model/tool execution to `AgentEngine`. The [engine](https://github.com/Sanuu7/AndroidHarness/blob/341bc6252364d298b18bd9f1ab6592e3a67fe514/app/src/main/java/com/androidharness/app/agent/AgentEngine.kt) loops through model responses and tool results, routes tools to workspaces, and checks permission mode and per-agent tool restrictions before executing action tools. It intercepts `task` calls and runs delegates with independent model context; delegates return their results to the calling agent, or report asynchronous status through `SubagentRuns` and `subagent_*` control tools. The app also offers scheduled automation, diff/undo and verification display, but these are not assumed to be autonomous higher-system management by their labels.

## Operational model

- Actual outcome: an edited or investigated coding workspace with explanations and tool observations returned through an app chat; read-only research answers in Chat mode.
- S1 units: model-driven Code session and optional model-driven delegated task loops. The same app may run several sessions, and child delegates can be read-only or (with settings and permission gates) action-capable.
- Ownership split: the model selects file/tool actions and decides whether to delegate. Application code owns deterministic execution, permissions, saved job state, concurrency limits and workspace safety checks. The human configures models, permissions, workspaces and approvals.

## S1 — Operations

- State: A
- Function: model-guided task execution transforms a coding workspace and observations into edits, tests and answers.
- Disturbance / variety regulated: unknown project state, command and tool failures, test outcomes, changing file content and evolving user objectives.
- Decisive decision or feedback right: the model chooses successive action/tool calls and the final result after receiving concrete tool observations; it may elect to delegate a bounded subtask.
- Decision owner: Code session's model-backed `AgentEngine`, with delegated model actor for a `task` subloop.
- Supporting / enforcement mechanisms: `RunManager`, workspace tool routing, tool registry, permission modes, task budgets, saved resume, optional shell backends and `SubagentRuns`.
- Closure path: user instruction → selected model turn and tool call → permission/workspace routing → actual tool result → model's next decision or delegated result → final answer/change.
- Boundary reachability: `RunManager.startRun` starts a shipped app job; `AgentEngine.performWithPermission` executes registered tools and intercepts the active `task` tool; the [task schema](https://github.com/Sanuu7/AndroidHarness/blob/341bc6252364d298b18bd9f1ab6592e3a67fe514/app/src/main/java/com/androidharness/app/tools/SubagentTools.kt) and [engine dispatch](https://github.com/Sanuu7/AndroidHarness/blob/341bc6252364d298b18bd9f1ab6592e3a67fe514/app/src/main/java/com/androidharness/app/agent/AgentEngine.kt) confirm that delegation is functional, not merely advertised.
- Why this is / is not agent-owned: removing model discretion leaves a tool runner, workspace guards and schedules, but not adaptive coding decisions; the agent selects meaningful operations in response to evidence.
- Evidence: [README Code/Chat features](https://github.com/Sanuu7/AndroidHarness/blob/341bc6252364d298b18bd9f1ab6592e3a67fe514/README.md), [session run lifecycle](https://github.com/Sanuu7/AndroidHarness/blob/341bc6252364d298b18bd9f1ab6592e3a67fe514/app/src/main/java/com/androidharness/app/agent/RunManager.kt), [model/tool and subagent execution](https://github.com/Sanuu7/AndroidHarness/blob/341bc6252364d298b18bd9f1ab6592e3a67fe514/app/src/main/java/com/androidharness/app/agent/AgentEngine.kt).
- Basis: structural.
- Confidence: high for shipped model-choice/tool-feedback path; runtime success on a physical Android device was not tested.
- Caveats: cloud providers, runtime permissions and installed shell environments condition what tools actually succeed.

## S2 — Coordination

- State: —
- Function: no autonomous first-party S2-specific inter-S1 interference regulation and returned adjustment loop is established.
- Disturbance / variety regulated: simultaneous sessions or child agents could interfere via overlapping workspace edits, while resource pressure may arise from concurrent delegates.
- Decisive decision or feedback right: no observed autonomous coordinator resolving a specific cross-S1 conflict and issuing adaptive subsequent-task constraints; model delegates its own tasks, and guard code rejects selected collisions by fixed rules.
- Decision owner: per-session model for delegation; developer-authored `workspaceGuard`, `workspaceBusy`, and fixed subagent semaphore for safety/execution.
- Supporting / enforcement mechanisms: `RunManager.withIdleWorkspace`, `withIdleStorage`, `workspaceBusy`, and `SubagentRuns` semaphore (default parallelism 2); child `task` results and `subagent_status`/`stop`.
- Closure path: workspace conflict checks block publishing, deletion, reassignment and message replacement; task results return to their caller. No distinct agentic conflict assessment and coordination correction returned across competing S1 tasks was found.
- Why this is / is not agent-owned: workspace-busy checks enforce fixed predicates and semaphore queues; ordinary task splitting and status reporting do not by themselves establish a second, coordination-specific autonomous decision owner.
- Evidence: [workspace guard and busy detection](https://github.com/Sanuu7/AndroidHarness/blob/341bc6252364d298b18bd9f1ab6592e3a67fe514/app/src/main/java/com/androidharness/app/agent/RunManager.kt), [subagent semaphore and state](https://github.com/Sanuu7/AndroidHarness/blob/341bc6252364d298b18bd9f1ab6592e3a67fe514/app/src/main/java/com/androidharness/app/agent/SubagentRuns.kt), [delegation contract](https://github.com/Sanuu7/AndroidHarness/blob/341bc6252364d298b18bd9f1ab6592e3a67fe514/app/src/main/java/com/androidharness/app/tools/SubagentTools.kt).
- Basis: structural.
- Confidence: medium-high for the inspected source-distributed modes.
- Caveats: deterministic file-safety exclusion is real and valuable; the negative state does not deny its existence or rule out higher-function plugins.

### Absence scope

- Surfaces inspected: session lifecycle and workspace guards, delegation/child status, concurrency semaphore and read-only/background execution policies.
- Plausible first-party paths checked: concurrent chats, worker slots, `workspaceBusy`, agent-chosen parallel tasks, `subagent_status`/`stop`, mutation/publish exclusion.
- Why no material first-party path remains: these paths enforce configured bounds, serialize a subset of unsafe mutations, or return delegated findings to the same parent S1; no separately owned S2-specific adaptive feedback across competing S1 commitments is sourced.

## S3 — Inside-and-now control

- State: —
- Function: no full-system discretionary current-control owner over the app's simultaneous operational commitments is established.
- Disturbance / variety regulated: interrupted runs, over-budget steps, pending approvals, long-running delegates and concurrent session jobs are handled through status, recovery and fixed controls.
- Decisive decision or feedback right: a user may stop/approve local work and an agent may steer its own task; no evidenced system-wide selection/reallocation of active commitments based on an aggregate supervisory view.
- Decision owner: per-chat models and the human user for local actions; application code executes lifecycle rules, restarts, limits and state persistence.
- Supporting / enforcement mechanisms: `RunManager.LiveRunState`, `TaskControlStore`, task queue, background job states, completion/stop controls and budget checks.
- Closure path: session events update local status/controls, and user/model may continue a session; this does not reconstruct a separate current S3 authority over all S1 commitments.
- Why this is / is not agent-owned: execution of budgets and cancellations is not discretionary whole-current management. Local human approval of a command does not by itself establish S3=P.
- Evidence: [RunManager state and start/stop lifecycle](https://github.com/Sanuu7/AndroidHarness/blob/341bc6252364d298b18bd9f1ab6592e3a67fe514/app/src/main/java/com/androidharness/app/agent/RunManager.kt), [task control](https://github.com/Sanuu7/AndroidHarness/blob/341bc6252364d298b18bd9f1ab6592e3a67fe514/app/src/main/java/com/androidharness/app/agent/TaskControl.kt), [subagent control tools](https://github.com/Sanuu7/AndroidHarness/blob/341bc6252364d298b18bd9f1ab6592e3a67fe514/app/src/main/java/com/androidharness/app/tools/SubagentControlTools.kt).
- Basis: structural.
- Confidence: medium; no live multi-session supervision exercise was run.
- Caveats: the operator retains substantial local control, but a generic operator interface is not sufficient to publish an S3 parent mode.

### Absence scope

- Surfaces inspected: run start, per-session state, task controls, subagent reports, UI-advertised monitoring and resume/automation modes.
- Plausible first-party paths checked: session status monitoring, local approval/stop, queued prompts, background delegation and workspace storage gates.
- Why no material first-party path remains: no sourced whole-current portfolio decision with authority over multiple S1 commitments and a returned operational adjustment; local controls and fixed policies remain at their respective boundaries.

## S3* — Complementary audit

- State: —
- Function: no claim-relative independent operational-artifact audit and corrective control path is established as a separate first-party function.
- Disturbance / variety regulated: coding defects and unverified edits may be surfaced by test runs, diff review and verification cards, without a distinct autonomous auditor.
- Decisive decision or feedback right: model or user chooses ordinary tests/review; `VerificationEvidence` classifies previously reported command exits and marks checks stale after changes, not independent artifact judgment.
- Decision owner: originating Code agent/user for test and review decisions; verification status extraction is deterministic.
- Supporting / enforcement mechanisms: `VerificationEvidence.collect`, diff and undo UI, `/review` request and external user-project tests.
- Closure path: tool command results and UI verification cards return to originating session/user; no separate auditor obtains complementary direct evidence and issues corrective findings controlling subsequent work.
- Why this is / is not agent-owned: parsing tool results and ordinary self-review do not establish a separate independent audit authority; optional role/subagent can be asked to review but generic child prompting is not evidence of first-party complementary audit closure.
- Evidence: [verification evidence parser](https://github.com/Sanuu7/AndroidHarness/blob/341bc6252364d298b18bd9f1ab6592e3a67fe514/app/src/main/java/com/androidharness/app/agent/VerificationEvidence.kt), [README verification/diff/review features](https://github.com/Sanuu7/AndroidHarness/blob/341bc6252364d298b18bd9f1ab6592e3a67fe514/README.md), [subagent tool contract](https://github.com/Sanuu7/AndroidHarness/blob/341bc6252364d298b18bd9f1ab6592e3a67fe514/app/src/main/java/com/androidharness/app/tools/SubagentTools.kt).
- Basis: structural.
- Confidence: medium-high for inspected verification/review paths.
- Caveats: a specifically configured external review plugin could add an audit path outside this first-party default.

### Absence scope

- Surfaces inspected: verification parser, self-review command, tool return messages, generic task delegates and status UI claims.
- Plausible first-party paths checked: build/test status collection, stale-result invalidation, diff review, user approval and child reviewer prompts.
- Why no material first-party path remains: none provides a separately owned complementary evidence-access/judgment/returned-correction loop for operational claims.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party prospective environmental sensing, option development and selected durable future-capability adaptation loop is established.
- Disturbance / variety regulated: changing dependencies, external documentation and user demands are task-level inputs; they do not automatically drive systematic future harness adaptation.
- Decisive decision or feedback right: no source-wired prospective owner choosing improvements to the harness operating capability based on external intelligence.
- Decision owner: Code model for in-task research; user/developer for installing extensions, choosing model/providers and app updates.
- Supporting / enforcement mechanisms: web/research tools, plugin/skills managers, model selection, persistent memory, scheduled prompts and automations.
- Closure path: research observations can affect the immediate session and installed options can be set by users; no evidenced outside-and-then adaptation proposal → authoritative selection → durable changed organizational capability loop.
- Why this is / is not agent-owned: configurable plugins and scheduled recurring prompts are valuable extensibility/operations, not by themselves S4 prospective intelligence.
- Evidence: [README model, plugin and automation features](https://github.com/Sanuu7/AndroidHarness/blob/341bc6252364d298b18bd9f1ab6592e3a67fe514/README.md), [run manager](https://github.com/Sanuu7/AndroidHarness/blob/341bc6252364d298b18bd9f1ab6592e3a67fe514/app/src/main/java/com/androidharness/app/agent/RunManager.kt), [automation manager](https://github.com/Sanuu7/AndroidHarness/blob/341bc6252364d298b18bd9f1ab6592e3a67fe514/app/src/main/java/com/androidharness/app/automation/AutomationManager.kt).
- Basis: structural.
- Confidence: medium; first-party user extension workflows were not executed.
- Caveats: external developers can improve the app between versions, which is not sufficient evidence of in-boundary S4 parent mode.

### Absence scope

- Surfaces inspected: README/feature modes, model/provider settings, scheduled automation manager, tool and subagent execution, context memory.
- Plausible first-party paths checked: scheduled research prompts, plugin installation, web research, auto-resume, user configuration and external GitHub project access.
- Why no material first-party path remains: no identified prospective function owns sensing→option→adaptation feedback into ongoing harness capabilities rather than immediate task solving or human software maintenance.

## S5 — Policy and identity

- State: —
- Function: no first-party identity/ultimate-policy decision and authoritative return path at the installed-harness recursion is established.
- Disturbance / variety regulated: unsafe commands, tool permissions, project scopes and user approval requests are operational policy enforcement or local authorizations, not an evidenced ultimate-policy dispute.
- Decisive decision or feedback right: user grants tool permissions and changes settings; no constitutional purpose/identity issue is routed to a legitimate ultimate-policy authority and returned as binding organizational policy.
- Decision owner: developer-written app policy and human operator configuration; model cannot independently elevate permission authority.
- Supporting / enforcement mechanisms: `PermissionMode`, tool restrictions, workspace routing, plan mode, user approval, saved grants and model/provider settings.
- Closure path: tool action request → fixed enforcement or user approval → permitted/denied tool call; no identity-level escalation → authoritative judgment → revised governing identity path.
- Why this is / is not agent-owned: permission gates and explicit user consent are not themselves S5=P; they manage local operational actions without showing ultimate-policy decision content or its return.
- Evidence: [permission/workspace routing in AgentEngine](https://github.com/Sanuu7/AndroidHarness/blob/341bc6252364d298b18bd9f1ab6592e3a67fe514/app/src/main/java/com/androidharness/app/agent/AgentEngine.kt), [workspace assignment and grant startup in RunManager](https://github.com/Sanuu7/AndroidHarness/blob/341bc6252364d298b18bd9f1ab6592e3a67fe514/app/src/main/java/com/androidharness/app/agent/RunManager.kt), [README safety model](https://github.com/Sanuu7/AndroidHarness/blob/341bc6252364d298b18bd9f1ab6592e3a67fe514/README.md).
- Basis: structural.
- Confidence: medium-high at this specific boundary.
- Caveats: governance of the open-source app itself is outside the installed-agent system assessed here.

### Absence scope

- Surfaces inspected: permissions, workspace tool routing, task agent policies, user settings, app distribution and README safety explanation.
- Plausible first-party paths checked: plan approval, tool grants, privileged shell consent, profile configuration, user settings changes and runtime refusals.
- Why no material first-party path remains: paths authorize/refuse operational actions but do not reconstruct an ultimate-policy issue reaching a parent or autonomous S5 owner with an authoritative policy-level return.

## Recursion

Code sessions and delegates have bounded autonomous task decisions; background delegates retain status and own model context, but cannot spawn further subagents and are typically read-only. Several sessions may be active, yet this is not sufficient to infer a nested self-governing metasystem. `workspaceGuard` connects process operations at a safety-enforcement level and does not constitute independent agent-owned coordination or whole-current control.

## Variety and escalation

Tool results return task-level disturbances directly to the Code model. Permission-denied actions, unavailable runtime providers, workspace collisions and interrupted tasks either produce an error, require local user action or follow fixed resume/retry rules. The app tracks persistent state and verification cards, but higher-order policy conflicts and organizational adaptation have no separately evidenced governance escalation/return channel.

## Evidence gaps

- Source-first review of the pinned repository only; no physical Android installation, model-backed exercise, live background concurrency, provider failure or external GitHub write was performed.
- UI and documented optional modes were correlated with source wiring for the principal agent/delegate/guard paths; some user-enabled plugin and automation configurations could change the concrete deployment and are not treated as present by default.
- S2 and S3 are bounded negatives despite genuine safety guards and job status; they require decision/feedback ownership and control scope beyond concurrency, local task management or deterministic protections.

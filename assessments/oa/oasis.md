---
harness_id: oasis
project_name: OASIS
repository: https://github.com/FAHTHIZ/oasis
review_ref: b03a4207c6969a71d570cedf4db2651245b4a822
reviewed_at: 2026-11-03
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# OASIS

## Review boundary

- System in focus: First-party OASIS coding-agent runtime, including its supported optional multi-agent shared-task and specialist-review modes, not its development/evaluation organization.
- Purpose and identity: Let a chosen model implement coding tasks through controlled tools and verifiable outcomes; optionally coordinate independent workers without silently merging their changes.
- Relevant environment: User-specified repository/workspace, file/shell/Git tools, model providers, browser/CLI frontends, possible peer workers and actual tests/diffs.
- Standard-distribution boundary: Node `src/agent.mjs` model/tool loop with CLI/browser/SDK interfaces, built-in subagents, session-local shared task board, team/dispatch tools, separate read-only specialist reviews and runtime safety/verification gates.
- Credited operating / distribution surfaces: [agent.mjs](https://github.com/FAHTHIZ/oasis/blob/b03a4207c6969a71d570cedf4db2651245b4a822/src/agent.mjs), [shared-tasks.mjs](https://github.com/FAHTHIZ/oasis/blob/b03a4207c6969a71d570cedf4db2651245b4a822/src/shared-tasks.mjs), [agent-tasks.mjs](https://github.com/FAHTHIZ/oasis/blob/b03a4207c6969a71d570cedf4db2651245b4a822/src/agent-tasks.mjs), [subagents.mjs](https://github.com/FAHTHIZ/oasis/blob/b03a4207c6969a71d570cedf4db2651245b4a822/src/subagents.mjs), [architecture](https://github.com/FAHTHIZ/oasis/blob/b03a4207c6969a71d570cedf4db2651245b4a822/docs/ARCHITECTURE.md).
- Adjacent first-party surfaces excluded from ownership: Development benchmark/evaluator and CI, GitHub Action executing a separate checkout, external model-provider adaptation, plugin marketplace and maintainer roadmap are not co-opted as runtime metasystem. Optional imported hooks/plugins remain developer- or user-configured actors until reached in a first-party mode.
- First-party operating / deployment modes considered: One local CLI/web/SDK coding agent; task subagents and named teams; shared dependency-aware board and `dispatch_ready_tasks`; optional built-in `code-review`, `security-review`, and `run_specialist_review` agent modes.
- Recursion level: One user task/project session with its distinct active worker agents as S1 units and its parent OASIS model session as coordinator/current-control actor. No continuous cloud portfolio is inferred.
- Reviewed revision: `b03a4207c6969a71d570cedf4db2651245b4a822`.
- Observation date: 2026-11-03.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

`runAgentTurnRaw` drives a bounded model→tool calls→guarded executor→observation loop, with provider compatibility, tool-call repair, permissions and completion verification. `runSubagent` creates separate worker contexts, and `shared-tasks.mjs` implements task IDs, dependencies and exclusive expiring claims; `dispatchReadyTasks` launches eligible workers in separate Git worktrees, returns agent IDs, and optionally chains further ready work while this same parent session lives. Team messages and reports return to the parent. Two first-party review paths exist: distinct built-in read-only `code-review`/`security-review` subagents, and bounded separate `run_specialist_review` sessions explicitly forbidden from editing/running shell or fetching URLs. Test-tamper and completion gates are deterministic, not mistaken for independent audit actors. [architecture](https://github.com/FAHTHIZ/oasis/blob/b03a4207c6969a71d570cedf4db2651245b4a822/docs/ARCHITECTURE.md#agent-coordination-and-longer-work), [agent.mjs](https://github.com/FAHTHIZ/oasis/blob/b03a4207c6969a71d570cedf4db2651245b4a822/src/agent.mjs#L4347).

## Operational model

A single parent agent can perform its own code task; in the explicit shared-task mode, model agents own different deliverables. The main model can create/revise the task board, select dispatch and responses to conflicts, and review the returned reports. Runtime leases, dependencies and isolated worktrees enforce these choices without becoming autonomous decision owners by themselves. Review agents separately inspect source/diffs and return findings for the parent to judge and act on; their mere availability does not force every task to receive an audit.

## S1 — Operations

- State: A
- Function: Local autonomous coding task execution with tool observations and completion feedback.
- Disturbance / variety regulated: Codebase uncertainty, tool errors, unexpected test failures, model tool-output malformation and incomplete edits.
- Decisive decision or feedback right: Model selects and revises file/search/shell/Git/tool operations from task observations; may request child agents.
- Decision owner: Chosen parent or task-specific model agent, not the provider endpoint or deterministic safety layer.
- Supporting / enforcement mechanisms: `runAgentTurnRaw` step loop, `executeTool` dispatcher, permissions, tool-call repair, session history, file checkpoints and verification state.
- Closure path: Model tool-call→runtime authorization/execution→tool result→subsequent model turn, with final response checked against actual diff/test evidence.
- Boundary reachability: Normal shipped OASIS CLI/web/SDK session and task-subagent APIs, not an evaluation-only mock.
- Why this is / is not agent-owned: Host safety gates constrain and verify, but cannot choose the task-sensitive next action without the model.
- Evidence: [agent.mjs#L4633](https://github.com/FAHTHIZ/oasis/blob/b03a4207c6969a71d570cedf4db2651245b4a822/src/agent.mjs#L4633), [agent.mjs#L5019](https://github.com/FAHTHIZ/oasis/blob/b03a4207c6969a71d570cedf4db2651245b4a822/src/agent.mjs#L5019), [tools.mjs](https://github.com/FAHTHIZ/oasis/blob/b03a4207c6969a71d570cedf4db2651245b4a822/src/tools.mjs).
- Basis: structural
- Confidence: high for pinned first-party loop wiring, not independent quality/effectiveness.
- Caveats: No paid/local model run was performed; model availability and permissions vary by deployment.

## S2 — Coordination

- State: A
- Distinct S1 units: Multiple model workers launched through `task`/background dispatch, with separate context and optional isolated worktrees.
- Inter-S1 disturbance: Two workers attempting to claim/change the same shared task, duplicate work after an expired claim, and downstream work starting before a prerequisite is complete.
- Attenuating coordination relation: Shared task leases/dependency checks plus a model-accessible `task_list`, `task_claim`, `task_release`, `task_update`, `team_send_message` and conditional dispatcher. Parent/model and workers can select alternative ready work or explicitly release/reassign after observing a conflict.
- Feedback into subsequent S1 behaviour: Claim rejection names current claimant/expiry, successful release/expiry opens a task for reassignment, and prerequisite status changes readiness for subsequent dispatch; agent receives these tool results before its next choice.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: Exclusive ownership and dependency constraints are designed to attenuate concrete conflicting work, not just order generic messages; conflict feedback alters which worker can perform which task next.
- Function: Inter-worker mutual-exclusion, dependency and conflict-adjustment regulation at task-board recursion.
- Disturbance / variety regulated: Duplicate edits/claims, incompatible simultaneous work and premature dependent launches.
- Decisive decision or feedback right: Select and adjust shared-task ownership/dependencies and reassign after claim refusal or worker failure.
- Decision owner: Model agents exercising first-party board and team tools, including parent with explicit force-release authority; runtime owns only atomic lease enforcement and safe dispatch limits.
- Supporting / enforcement mechanisms: Session-local board with lease TTL, dependency DAG, agent registry/status/events, per-worker worktrees and dispatch waves.
- Closure path: Collision/expired claim or failed worker→board tool status and event to agent→new claim, release, reassignment or changed dependency→next eligible worker execution.
- Boundary reachability: Shipped default `task_*` and `dispatch_ready_tasks` tools are exposed to live parent/worker sessions, not developer-only examples.
- Why this is / is not agent-owned: The code enforces accepted decisions, while autonomous agents choose task selection, claim/release and response to returned contention information; simply auto-serializing alone is not credited.
- Evidence: [shared-tasks.mjs#L232](https://github.com/FAHTHIZ/oasis/blob/b03a4207c6969a71d570cedf4db2651245b4a822/src/shared-tasks.mjs#L232), [agent.mjs#L3552](https://github.com/FAHTHIZ/oasis/blob/b03a4207c6969a71d570cedf4db2651245b4a822/src/agent.mjs#L3552), [agent-tasks.mjs](https://github.com/FAHTHIZ/oasis/blob/b03a4207c6969a71d570cedf4db2651245b4a822/src/agent-tasks.mjs).
- Basis: structural
- Confidence: medium-high for the supported multi-agent mode; no reproduced competing-work test in this review.
- Caveats: A session that never launches peers has no active S2 relation; leases are session-local and reset on process restoration. A failed automatic dispatch pauses; agent discretion to adjust is available but not guaranteed to be effective.

## S3 — Inside-and-now control

- State: A
- Whole-system current view: Parent model can inspect the full shared task board, claims, dependencies and all worker reports/status/events within its session, including worktree changes awaiting integration.
- Current-control decision scope: Create/prioritize task commitments, change dependencies/owners, choose dispatch parallelism, pause or resume waves, intervene in failures and judge whether to integrate worker branches.
- Function: Current whole-session commitments and resource allocation across delegated code work.
- Disturbance / variety regulated: Blocked dependencies, worker failure, depleted agent slots, pending unintegrated changes and unfinished work.
- Decisive decision or feedback right: The main model changes current task definitions/owners, manages waves and adjusts continuation from observed worker evidence.
- Decision owner: Main OASIS model agent, subject to operator approval for unsafe tool/merge operations; runtime only enforces preselected guardrails.
- Supporting / enforcement mechanisms: `task_list/update`, `agent_status/events`, dispatch limit and pause logic, Git worktrees and explicit review/integration workflow.
- Closure path: Workers finish/fail→agent event/board read→main model updates commitments or dispatches/reviews next wave→new worker state or a blocked escalation.
- Boundary reachability: First-party `task_*`, `agent_*` and dispatch tools are available in an ordinary multi-agent OASIS session.
- Why this is / is not agent-owned: The dispatcher computes feasible slots but does not decide task priorities, exception response or integration; those are model/current-control choices.
- Evidence: [agent.mjs#L549](https://github.com/FAHTHIZ/oasis/blob/b03a4207c6969a71d570cedf4db2651245b4a822/src/agent.mjs#L549), [agent.mjs#L3431](https://github.com/FAHTHIZ/oasis/blob/b03a4207c6969a71d570cedf4db2651245b4a822/src/agent.mjs#L3431), [agent.mjs#L3552](https://github.com/FAHTHIZ/oasis/blob/b03a4207c6969a71d570cedf4db2651245b4a822/src/agent.mjs#L3552).
- Basis: structural
- Confidence: medium; supported current-control topology, not measured resilience of a real swarm.
- Caveats: No sustained service across process restart; external manual worktree integration is required. Human intervention rights at tool gates do not alone qualify a separate S3 parent mode.

## S3* — Complementary audit

- State: A
- Claim being audited: Parent or implementation worker's claim that a code change is correct or free of relevant security regressions.
- Ordinary reporting path: Implementing model returns its own final prose, tool transcript, diff and verification state to parent/main session.
- Complementary access path: Distinct read-only `code-review` / `security-review` model session or bounded `run_specialist_review` directly reads actual repository files and Git evidence with independent tool context, then returns finding details.
- Independence boundary: Specialist has a separate session, no inherited working conversation as authority, read-only tool allowlist and explicit prohibition on edits, shell/network and MCP; distinct built-in read-only reviewers can be invoked through `task`. This is procedural separation, not institutional isolation or a mandatory third-party audit.
- Who acts on findings: Parent/main agent receives reviewer result in the normal tool response, inspects reported paths and applies or delegates corrections, followed by available tests/verification.
- Function: Independent challenge of work claims from actual source/diff evidence, with returned corrective action potential.
- Disturbance / variety regulated: Plausible but incorrect implementation summaries, untested edge cases and security regressions.
- Decisive decision or feedback right: Separate specialist model judges inspected code and reports bounded actionable findings; main session owns remediation decisions.
- Decision owner: Read-only review model owns independent audit judgment, distinct from production agent; parent owns current-control correction.
- Supporting / enforcement mechanisms: `runSpecialistReview`, specialist roles, bounded review budgets, reviewer read-only tool filter and ordinary verification gate.
- Closure path: Main invokes review→separate model reads actual files/diff→returns concrete findings→main re-evaluates and revises code or task→checks again.
- Boundary reachability: Built-in specialist-review tool and `code-review`/`security-review` subagents available without custom extensions, in normal coding sessions.
- Why this is / is not agent-owned: The specialist—not the implementer or its deterministic verifier—chooses what to challenge and whether evidence supports a defect.
- Evidence: [agent.mjs#L2982](https://github.com/FAHTHIZ/oasis/blob/b03a4207c6969a71d570cedf4db2651245b4a822/src/agent.mjs#L2982), [agent.mjs#L4211](https://github.com/FAHTHIZ/oasis/blob/b03a4207c6969a71d570cedf4db2651245b4a822/src/agent.mjs#L4211), [subagents.mjs](https://github.com/FAHTHIZ/oasis/blob/b03a4207c6969a71d570cedf4db2651245b4a822/src/subagents.mjs).
- Basis: structural
- Confidence: medium for reachable complementary path; not a measured audit-success rate.
- Caveats: Review is optional, and some tool/approval modes may narrow its usefulness. Deterministic auto-test and LSP checks are excluded from S3* credit by themselves.

## S4 — Outside-and-then intelligence

- State: —
- Function: Prospective external/environmental sensing and governing self-adaptation of the OASIS session capability.
- Disturbance / variety regulated: Evolving APIs, model catalogs and ecosystem plugins.
- Decisive decision or feedback right: No evidenced first-party external future assessment→adaptation option→committed capability update loop under an autonomous S4 actor.
- Decision owner: Operator/developer selects model, extension updates and imported skills; task-agent searches are for the current user deliverable.
- Supporting / enforcement mechanisms: Model discovery/router, web search, update command, plugin catalog, imported skill review, session memory and workflow scripts.
- Closure path: Configuration/skills change by operator action or a current task's explicit command; there is no distinct prospective environmental function returning to whole-session S3 capability.
- Why this is / is not agent-owned: Availability of web tools, plugin import and a roadmap does not establish self-directed future adaptation of the harness.
- Evidence: [architecture](https://github.com/FAHTHIZ/oasis/blob/b03a4207c6969a71d570cedf4db2651245b4a822/docs/ARCHITECTURE.md#extension-and-plugin-ecosystem), [update.mjs](https://github.com/FAHTHIZ/oasis/blob/b03a4207c6969a71d570cedf4db2651245b4a822/src/update.mjs), [extensions.mjs](https://github.com/FAHTHIZ/oasis/blob/b03a4207c6969a71d570cedf4db2651245b4a822/src/extensions.mjs).
- Basis: structural
- Confidence: medium-high for bounded standard modes examined.
- Caveats: A custom workflow may research future changes, but that composition is not a shipped autonomous S4 owner.

### Absence scope

- Surfaces inspected: Model routing/discovery, marketplace/plugin import, skill loading, memory, workflow, updates and runtime monitor.
- Plausible first-party paths checked: External web queries, plugin/version updates, model fallback, user skill adoption, project improvement plans and later-session notes.
- Why no material first-party path remains: None was found to close an independent prospective environment→option→selection→new present capability return, rather than current-task execution or human-maintained configuration.

## S5 — Policy and identity

- State: —
- Function: Ultimate identity/policy conflict resolution for the OASIS agent system itself.
- Disturbance / variety regulated: Competing goals and exceptional decisions over core system identity, not ordinary tool safety.
- Decisive decision or feedback right: No first-party identity-level legitimacy mandate and binding returned policy decision.
- Decision owner: User/developer authors permissions, model/tool settings, static policy text and task instructions; model cannot redefine ultimate authority through the workflow.
- Supporting / enforcement mechanisms: Permission policy, plan/approval gates, trust boundaries, security patterns and protected paths.
- Closure path: Approval or rejection returns to individual tool/task execution; no identity dispute reaches a legitimized ultimate authority and returns to govern subsequent system purpose.
- Why this is / is not agent-owned: Even stringent deterministic safety checks regulate risky acts, not the identity or ultimate policy of a viable system.
- Evidence: [permissions.mjs](https://github.com/FAHTHIZ/oasis/blob/b03a4207c6969a71d570cedf4db2651245b4a822/src/permissions.mjs), [agent.mjs](https://github.com/FAHTHIZ/oasis/blob/b03a4207c6969a71d570cedf4db2651245b4a822/src/agent.mjs), [architecture](https://github.com/FAHTHIZ/oasis/blob/b03a4207c6969a71d570cedf4db2651245b4a822/docs/ARCHITECTURE.md#security-and-trust-boundaries).
- Basis: structural
- Confidence: medium-high.
- Caveats: Human project governance outside the runtime is not asserted absent.

### Absence scope

- Surfaces inspected: User policy settings, permission callbacks, plan/approval modes, team/project configuration and system instruction surfaces.
- Plausible first-party paths checked: User tool approval, security veto, authorization to merge worktrees, team shutdown, model selection and update workflows.
- Why no material first-party path remains: These constrain current execution or modify configuration but do not route/close an identity or ultimate-policy dispute through a legitimate authority.

## Recursion

Each subagent can itself run a coding S1 loop. The shared board, team and main session provide a session-local metasystem; background registries and checkpoints do not imply persistence of a higher-level organization beyond process restart.

## Variety and escalation

Exclusive claims, dependency gates and isolated worktrees attenuate duplicate edits; worker failure pauses automatic dispatch and returns a visible event for main-agent decision. Tests, test-tamper and human approval are ordinary safety/verification evidence unless an independent review path is separately invoked. Completion gating blocks unsupported success assertions but cannot guarantee correctness.

## Evidence gaps

This is source-structural review of an Apache-2.0 public commit. No live provider, sustained multi-agent run, independent audit efficacy measurement or actual Git branch integration was exercised. S2/S3/S3* positive states describe available explicitly invoked modes, not always-on governance in a singleton chat.

## Verdict

**Include.** Shipped OASIS contains an autonomous coding S1, model-accessible specific inter-worker claim/dependency coordination, parent-model current task regulation and separately instantiated read-only audit judgment with findings returned for correction. Operator-controlled external updates and conventional safety configuration do not establish S4 or S5.

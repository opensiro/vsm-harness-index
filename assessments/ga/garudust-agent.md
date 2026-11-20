---
harness_id: garudust-agent
project_name: Garudust Agent
repository: https://github.com/garudust-org/garudust-agent
review_ref: 905e7797fc1f71782c88e3af0ff7dfb7b9aca61a
reviewed_at: 2026-11-20
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Garudust Agent

## Review boundary

- System in focus: A running personal Garudust agent with optional model-delegated sub-agent tasks, supplied in one Rust desktop, terminal or daemon deployment; not upstream Garudust OSS development, chat-platform company or externally hosted provider.
- Purpose and identity: Perform human-directed tool-mediated tasks while remembering task context, optionally delegating independent portions and reusing local skills under operator-defined permissions and identity files.
- Relevant environment: Human requests, workspace and web/tool outputs, provider errors, failed subagents, local memory and installed skills, chat-platform messages, sandbox/approval boundaries.
- Standard-distribution boundary: Native Rust crates `garudust-agent`, `garudust-tools`, `garudust-memory`, `garudust-core`, terminal/server and desktop adapters; external LLMs, custom hub skills, provider APIs and user edits to `SOUL.md` do not establish first-party governance by themselves.
- Credited operating / distribution surfaces: Native model/tool loop, `DelegateTask`/`DelegateTasks` child-run contracts, GoalStore and memory loader, model-visible scheduling, limited conflict-key serialization of concurrent calls, CLI/daemon/desktop frontends.
- Adjacent first-party surfaces excluded from ownership: Upstream `.github` CI and Claude PR review, offline tests, community skills or hosted MCP servers, platform-side RBAC, operator-maintained persona/policy files.
- First-party operating modes considered: Interactive terminal, embedded desktop and autonomous headless server; optional subagents share `Agent` runner under owner-supplied toolset; no independently run subagent proof or system-of-systems organization assessment.
- Recursion level: Human-scoped task agent/its optional child work, not Garudust's software maintainer ecosystem.
- Reviewed revision: `905e7797fc1f71782c88e3af0ff7dfb7b9aca61a`.
- Observation date: 2026-11-20.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The Rust `Agent` receives a provider transport, tool registry, local memory store and budget/config, then sends messages and model-visible schemas to the provider, executes selected calls and feeds observations back. CLI, native desktop and headless server use the same first-party loop. A `delegate_task` or `delegate_tasks` call re-enters the Agent runner for independent subgoals; multi-delegation limits concurrency, sorts outcomes by task index and returns both successes and explicit failed blocks to the model parent. Separate run history and GoalStore allow current commitments to be reloaded across turns. The general tool engine serializes calls only when first-party tool `parallelism_key` matches, avoiding collisions **within simultaneous tool calls**; no equivalent shared inter-child workspace arbitration or cross-agent review protocol is sourced.

The system prompt loads operator-managed `SOUL.md`, `AGENTS.md`, profile, memory and skills. Built-in model calls may propose new skills based on experience. A model can create cron jobs in an active runtime, but `cron_create` explicitly says these jobs are not persisted across restart unless declared by a human in config. An identity file is not itself an S5 feedback contract.

Evidence: [agent loop](https://github.com/garudust-org/garudust-agent/blob/905e7797fc1f71782c88e3af0ff7dfb7b9aca61a/crates/garudust-agent/src/agent.rs), [delegation](https://github.com/garudust-org/garudust-agent/blob/905e7797fc1f71782c88e3af0ff7dfb7b9aca61a/crates/garudust-tools/src/toolsets/delegate.rs), [tool concurrency contract](https://github.com/garudust-org/garudust-agent/blob/905e7797fc1f71782c88e3af0ff7dfb7b9aca61a/crates/garudust-core/src/tool.rs), [goal state](https://github.com/garudust-org/garudust-agent/blob/905e7797fc1f71782c88e3af0ff7dfb7b9aca61a/crates/garudust-memory/src/goal_store.rs), [prompt assembly](https://github.com/garudust-org/garudust-agent/blob/905e7797fc1f71782c88e3af0ff7dfb7b9aca61a/crates/garudust-agent/src/prompt_builder.rs).

## Operational model

Operator configures the provider, workspace/sandbox, available tools, permissions and persona. Model chooses ordinary tool operations and can decompose a task into independent subagent instructions. Each child produces a bounded result or an explicit failure; model parent can revise its work plan, retry a failed part or integrate completed work. This supplies task-local current control, but no public first-party contract for cross-child interference resolution beyond the premise that delegated tasks should be independent. External content stays data in prompt guidance; compliance not runtime tested.

## S1 — Operations

- State: A
- Function: Perform human-scoped tool-bearing tasks and deliver answers or artifacts.
- Disturbance / variety regulated: Unpredictable user, workspace, web and tool outcomes, provider feedback and execution errors.
- Decisive decision or feedback right: Select/revise tool calls, use returned results, continue or complete.
- Decision owner: Principal model-driven `Agent` and model-driven child instances for delegated tasks.
- Supporting / enforcement mechanisms: Provider transport, typed `ToolRegistry`, iteration budget, guarded execution groups, local memory and prompt builder.
- Closure path: Current task -> LLM/tool decision -> guarded tool call -> tool result -> LLM chooses another call, delegation, or answer.
- Boundary reachability: `Agent::run` drives public terminal, server and desktop paths; `DelegateTask` calls `SubAgentRunner::run_task` in the same shipped crate.
- Why this is / is not agent-owned: Model owns substantive task actions; provider backend and registry execute/guard them.
- Evidence: [Agent implementation](https://github.com/garudust-org/garudust-agent/blob/905e7797fc1f71782c88e3af0ff7dfb7b9aca61a/crates/garudust-agent/src/agent.rs), [Tool trait](https://github.com/garudust-org/garudust-agent/blob/905e7797fc1f71782c88e3af0ff7dfb7b9aca61a/crates/garudust-core/src/tool.rs), [README operational modes](https://github.com/garudust-org/garudust-agent/blob/905e7797fc1f71782c88e3af0ff7dfb7b9aca61a/README.md).
- Basis: structural
- Confidence: high
- Caveats: No live model or host execution performed for the assessment.

## S2 — Coordination

- State: —
- Function: No qualifying inter-S1 adaptive coordination was evidenced despite optional parallel child execution.
- Disturbance / variety regulated: Multiple child agents could choose incompatible edits or outputs on a shared workspace.
- Decisive decision or feedback right: Parent instructs children to take independent tasks; fixed fan-out limit, result ordering and intra-call conflict serialization do not themselves resolve cross-child conflicts, and no separate cross-child coordinator was found.
- Decision owner: No qualifying function-specific first-party coordination owner; the parent may reconcile outcomes as a normal whole-task S3 step.
- Supporting / enforcement mechanisms: `DelegateTasks` concurrency cap, child output indexing and failure marking; `parallelism_key` serializes **same-agent tool calls** with conflicting keys.
- Closure path: Independent delegated tasks are launched -> results returned in order -> parent can retry/accept; no evidenced separate shared inter-child interference regulation returns a coordinated joint operating rule.
- Boundary reachability: Delegate tools are shipped, but none of the code examined proves shared child workspace lock/scoped-write arbitration, team task claims, or inter-child feedback logic.
- Why this is / is not agent-owned: Generic parallelism and parent-level post-hoc integration do not make S2; a key conflict guard regulates concurrent tool invocations, not autonomous child relations.
- Distinct S1 units: Model-operated child runs that may execute at once.
- Inter-S1 disturbance: Potential overlapping shared workspace mutation or incompatible outputs.
- Attenuating coordination relation: Not established as a distinct inter-S1 coordination mechanism; only request that tasks be independent and fixed concurrency cap.
- Feedback into subsequent S1 behaviour: Failed child outputs return to parent for whole-task replan (S3), not a verified inter-child coordination channel.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: No source showed that additional S2-specific intervention; absence is intentional, not a claim that the system cannot ever be configured to coordinate.
- Evidence: [delegation](https://github.com/garudust-org/garudust-agent/blob/905e7797fc1f71782c88e3af0ff7dfb7b9aca61a/crates/garudust-tools/src/toolsets/delegate.rs), [concurrency key trait](https://github.com/garudust-org/garudust-agent/blob/905e7797fc1f71782c88e3af0ff7dfb7b9aca61a/crates/garudust-core/src/tool.rs), [agent grouped dispatch](https://github.com/garudust-org/garudust-agent/blob/905e7797fc1f71782c88e3af0ff7dfb7b9aca61a/crates/garudust-agent/src/agent.rs).
- Basis: structural
- Confidence: medium
- Caveats: A custom skill or external orchestrator might implement S2, but it is outside the shipped first-party boundary.

### Absence scope

- Surfaces inspected: Native agent loop, delegate wrappers and child-run interface, tool dispatch/conflict guard, goal/session storage and runtime tool registry.
- Plausible first-party paths checked: Parallel subagent fan-out, subtask output merge/partial failures, same-key tool-call serialization and independent session state.
- Why no material first-party path remains: Neither per-child shared-resource scope/lock nor inter-child arbitration/feedback surfaced; all checked mechanisms are worker invocation, intra-agent tool serialization, or parent task-level integration.

## S3 — Inside-and-now control

- State: A
- Function: Regulate a whole present task's plan, subgoal division, unsuccessful work and final acceptance across optional parallel subagents.
- Disturbance / variety regulated: Uncompleted parts, failed delegated tasks, budget pressure, inconsistent outputs and user goal continuation.
- Decisive decision or feedback right: Parent model decomposes current goal, chooses independent subtasks, consumes indexed failures/successes and chooses retry/integration/answer within the bounded task.
- Decision owner: Parent `Agent` model; not `DelegateTasks` cap or persistence code.
- Supporting / enforcement mechanisms: GoalStore per conversation, iteration budget, delegation tool results, memory and status messages in model history.
- Closure path: Current goal and work -> model chooses delegated task set -> returned partial outcomes and failures are visible -> parent adjusts plan or verifies deliverable -> follow-up S1 calls or final answer.
- Boundary reachability: Public `delegate_tasks` tool and native `Agent::run` loop; behavior explicitly documented in tool description and output shaping.
- Why this is / is not agent-owned: The model chooses current subtask scope and response; the Rust budget, child ordering and session persistence merely support its discretion.
- Whole-system current view: Goal + model history with child statuses/outputs for one user's bounded task.
- Current-control decision scope: Continue/retry/accept present task subtasks, not governance of multiple independently owned deployments.
- Evidence: [delegate tasks API](https://github.com/garudust-org/garudust-agent/blob/905e7797fc1f71782c88e3af0ff7dfb7b9aca61a/crates/garudust-tools/src/toolsets/delegate.rs), [Agent runner](https://github.com/garudust-org/garudust-agent/blob/905e7797fc1f71782c88e3af0ff7dfb7b9aca61a/crates/garudust-agent/src/agent.rs), [GoalStore](https://github.com/garudust-org/garudust-agent/blob/905e7797fc1f71782c88e3af0ff7dfb7b9aca61a/crates/garudust-memory/src/goal_store.rs).
- Basis: explicit and structural
- Confidence: medium
- Caveats: Current-control scope is single task with optional child calls; no durable organization-wide project board is shown.

## S3* — Complementary audit

- State: —
- Function: No shipped, distinct complementary evidence-challenge audit path was established for running customer task outputs.
- Disturbance / variety regulated: Model-written work can be confidently wrong without a separately sourced falsification channel.
- Decisive decision or feedback right: Generic child delegation can be prompted to review output, but no first-party reviewer role/trigger, raw-source independent access agreement and receipt-to-parent feedback path is supplied as a standard construction.
- Decision owner: Application/user might designate an independent reviewer; no qualifying shipped auditor owner observed.
- Supporting / enforcement mechanisms: General child tools, regular tool/response messages, development PR review CI and tests.
- Closure path: Ordinary tool return is not an independent audit. Repository Claude PR review inspects Garudust source contributions, not each end-user run.
- Why this is / is not agent-owned: A possible custom reviewer prompt is external composition, and generic self-critique or a failed tool is not S3*.
- Claim being audited: Customer-task deliverable correctness.
- Ordinary reporting path: Principal model reports its work and child completions.
- Complementary access path: No first-party separately tasked challenger with raw-evidence and returned verdict established.
- Independence boundary: Not demonstrated.
- Who acts on findings: User or custom orchestrator if added; none guaranteed.
- Evidence: [general child delegation](https://github.com/garudust-org/garudust-agent/blob/905e7797fc1f71782c88e3af0ff7dfb7b9aca61a/crates/garudust-tools/src/toolsets/delegate.rs), [agent loop](https://github.com/garudust-org/garudust-agent/blob/905e7797fc1f71782c88e3af0ff7dfb7b9aca61a/crates/garudust-agent/src/agent.rs), [repository PR-review CI excluded](https://github.com/garudust-org/garudust-agent/blob/905e7797fc1f71782c88e3af0ff7dfb7b9aca61a/.github/workflows/claude-pr-review.yml).
- Basis: structural
- Confidence: medium
- Caveats: No claim that users cannot build S3* from custom skills; only the pinned shipped default was evaluated.

### Absence scope

- Surfaces inspected: Native loop, subagent tools, prompt instructions, bundled tools/skills and repository review automation.
- Plausible first-party paths checked: Generic `delegate_task` as a reviewer, automated development PR review, response retries, tests and memory corrections.
- Why no material first-party path remains: No first-party independent reviewer contract or raw-evidence-to-finding-to-rework path for the assessed task was sourced.

## S4 — Outside-and-then intelligence

- State: —
- Function: No sourced future-oriented external variety sensing -> capability option selection -> present governance return loop.
- Disturbance / variety regulated: Future market, tool, model and environmental change beyond the current user request.
- Decisive decision or feedback right: The model can search the web, learn preferences and create reusable skills from completed work, but the shipped process is reactive to current tasks/experience.
- Decision owner: No distinct first-party prospective intelligence owner; human can install tools and skills.
- Supporting / enforcement mechanisms: `web_search`, `skill_view`/local skills, memory, scheduled task creation, user install commands.
- Closure path: Tool results or local lessons support current/future tool use, but without a demonstrable *external-and-then* prospective strategy feedback loop.
- Why this is / is not agent-owned: Saving a learned skill, extracting a preference and running cron jobs are not by themselves S4.
- Evidence: [skill loader](https://github.com/garudust-org/garudust-agent/blob/905e7797fc1f71782c88e3af0ff7dfb7b9aca61a/crates/garudust-tools/src/toolsets/skills.rs), [prompt instructions](https://github.com/garudust-org/garudust-agent/blob/905e7797fc1f71782c88e3af0ff7dfb7b9aca61a/crates/garudust-agent/src/prompt_builder.rs), [cron tools](https://github.com/garudust-org/garudust-agent/blob/905e7797fc1f71782c88e3af0ff7dfb7b9aca61a/crates/garudust-tools/src/toolsets/cron.rs), [README](https://github.com/garudust-org/garudust-agent/blob/905e7797fc1f71782c88e3af0ff7dfb7b9aca61a/README.md).
- Basis: structural
- Confidence: medium
- Caveats: User-authored recurring environmental analysis might qualify at a different sourced project boundary.

### Absence scope

- Surfaces inspected: Web/tool and skill entry points, memory, active goal and cron scheduler, model selection and provider transport.
- Plausible first-party paths checked: Reactive skill crystallization, web lookup, prompt memory, scheduling, model fallback and manual hub installation.
- Why no material first-party path remains: Sourced future-directed external signals did not flow into an autonomous capability plan and a governed operational adaptation owner; operator-configured cron alone is not enough.

## S5 — Policy and identity

- State: —
- Function: No first-party ongoing legitimate ultimate-identity/purpose conflict resolution and returned policy commitment found in the assessed personal-task agent.
- Disturbance / variety regulated: Contradictory foundational purposes, user persona requirements and authority conflicts.
- Decisive decision or feedback right: Human owner can edit `SOUL.md`, profile, config and tool-approval modes; these are external inputs or tactical tool permissions, not an evidenced S5 governance decision loop.
- Decision owner: Legitimate user/operator outside the runtime. No first-party S5-specific closing controller established.
- Supporting / enforcement mechanisms: System prompt from static agent identity + operator `SOUL.md`, user profile and `AGENTS.md`, host CLI config.
- Closure path: Operator-provided identity text is injected at run start; no source proves a first-party identity-issue -> deliberate human acceptance/rejection -> enduring policy update pathway analogous to a governed mandate.
- Why this is / is not agent-owned: Prompt rules and generic destructive-action approval constrain S1 without permitting the agent to own or settle its ultimate purpose.
- Identity / ultimate-policy issue: Durable foundational persona/mission, beyond episodic answer or user preference memory.
- Ultimate authority in each claimed mode: No positive first-party S5 mode asserted; user owns static configuration.
- Return-to-operation path: Static `SOUL.md` and `AGENTS.md` load into prompt but are not a complete S5 governance mechanism.
- Evidence: [prompt builder](https://github.com/garudust-org/garudust-agent/blob/905e7797fc1f71782c88e3af0ff7dfb7b9aca61a/crates/garudust-agent/src/prompt_builder.rs), [configuration](https://github.com/garudust-org/garudust-agent/blob/905e7797fc1f71782c88e3af0ff7dfb7b9aca61a/crates/garudust-core/src/config.rs), [approval policies](https://github.com/garudust-org/garudust-agent/blob/905e7797fc1f71782c88e3af0ff7dfb7b9aca61a/crates/garudust-agent/src/approver.rs).
- Basis: structural
- Confidence: medium
- Caveats: An owner can build a higher-level policy process in an application, but none is inferred from static files.

### Absence scope

- Surfaces inspected: Operator persona and policy files, system prompt, memory, approval, task goals, CLI/server mode and platform RBAC.
- Plausible first-party paths checked: SOUL identity loading, persistent user preference, destructive-action confirmation, and administrator configuration.
- Why no material first-party path remains: No distinctive ongoing ultimate-policy issue/decision/return process beyond setup and individual tool gate.

## Distributed OSS parent arrangement

Upstream Garudust maintainers review code and releases in GitHub, but the code-project PR gate is a different system than a personal deployed task agent. No parent-governed runtime S5 is imported from repository CI or OSS governance.

## Self-hosted and non-human modes

The default app supports a human owner and potentially unattended headless runs. These modes retain configured prompts and permissions, but do not by themselves grant S2/S3*/S4/S5 decision rights. Active `cron_create` explicitly lacks restart durability; durable schedules require separate config.

## Recursion

Subagent instances use their own run budgets but inherit the parent tool set and human-specified purpose. Their spawning neither implies a complete lower VSM recursion nor agent-owned future/ultimate policy.

## Variety and escalation

Untrusted search responses are tagged, child failures are marked and re-enter model context, and same-key tool calls are serialized. The parent can retry or consolidate current task outcomes. Subagent auto-approvals and default direct host terminal sandbox are safety scope concerns, not evidence of S2, S3* or S5; runtime behavior was not exercised.

## Evidence gaps

- Static source inspection only. No live Rust binary/provider run, actual cross-agent collision test, independent review or interactive human approval executed.
- S2 negative is specifically about interference among model-operated child units; same-agent tool serialization is acknowledged but not treated as an independent agent coordinator.
- S3 model-level whole-task control is inferred from delegation and results, not demonstrated for organization-scale scheduling.
- S3* absence concerns a standard review constructor, not impossibility to prompt a custom reviewing child.
- S4 and S5 negative judgments are bounded to first-party shipped mechanisms in the pinned revision.

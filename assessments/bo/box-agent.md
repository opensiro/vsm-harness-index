---
harness_id: box-agent
project_name: Box Agent
repository: https://github.com/Raccoon-Office/Box-Agent
review_ref: 060edcd2b551a05cd3c68b2c861f97b67a63a653
reviewed_at: 2026-11-20
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: P
---

# Box Agent

## Review boundary

- System in focus: One configured Box Agent user task/session, including its first-party agent loop, optional parallel subagent cells, delivered Skills and local persistence; not the Box Agent development project.
- Purpose and identity: Complete human-scoped general-purpose tasks by choosing model-driven tool calls, managing delegated subtasks and returning evidence-backed deliverables within host-declared permissions.
- Relevant environment: User goals and changing instructions, workspace files and artifacts, external tool and web outputs, concurrent child file activity, model services, host permissions and user identity preferences.
- Standard-distribution boundary: Released CLI/ACP/SDK `AgentSession` and `AgentLoopKernel`, built-in tool engine, first-party subagent handoff, goal/plan/todo state, configured bundled Skills, and the user-managed core-memory path. Provider APIs, host UI internals, user-installed third-party plugins, local developer workflows and repository PR review infrastructure remain distinct.
- Credited operating / distribution surfaces: `box_agent/agent.py`, `kernel/loop.py`, session/tool engine, optional shipped `sub_agent` plus scoped writes, goal/plan/todo tools, optional bundled `ppt-fast` content-review role, local memory user decision path.
- Adjacent first-party surfaces excluded from ownership: `general_review/` and `docs/PR_REVIEW_STANDARD.md` review the Box Agent code repository and are **not** a shipped independent auditor of every customer task; repository unit tests/CI, developer dogfood, removed workflow-owner state machines, third-party model provider, host UI, arbitrary installed skills and package examples are excluded.
- First-party operating / deployment modes considered: Interactive CLI, ACP managed session, direct Agent/SDK, optional concurrent `sub_agent` with disjoint path scopes, user-enabled bundled document Skills, local core-memory promotion/host decision. No live hosted model or actual peer execution performed.
- Recursion level: User task/session with one principal model-driven operational agent and optional delegated child work cells; children do not inherit complete viable-system identity by being spawned.
- Reviewed revision: `060edcd2b551a05cd3c68b2c861f97b67a63a653`.
- Observation date: 2026-11-20.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The public `Agent` facade drives the same `AgentLoopKernel` through CLI and ACP `AgentSession` adapters, keeping step state, LLM/tool choices and tool-result feedback inside the managed run. A static composition boundary constructs per-session and per-run service bundles; configuration and permissions are host/operator owned. Tools perform read/write, search, code execution and evidence collection under per-call guardrails. `SessionLog` is the durable source of messages, tool outcomes and Goal/Plan/Todo state; legacy workflow-owner/checkpoint machines are not active. Optional `sub_agent` creates independent model conversations with limited tools and budgets, isolated Python kernels, scoped file-write capabilities and explicit handoff/checkpoint receipts. The parent remains responsible for task selection, shared conflict resolution, verifying worker output and composing the final result. Bundled Skills may add domain-specific structured verification; repository-development review jobs are a separate system.

Primary architecture: [architecture](https://github.com/Raccoon-Office/Box-Agent/blob/060edcd2b551a05cd3c68b2c861f97b67a63a653/docs/ARCHITECTURE.md), [managed sessions](https://github.com/Raccoon-Office/Box-Agent/blob/060edcd2b551a05cd3c68b2c861f97b67a63a653/docs/AGENT_SESSION.md), [ownership](https://github.com/Raccoon-Office/Box-Agent/blob/060edcd2b551a05cd3c68b2c861f97b67a63a653/docs/WORKFLOW_OWNERSHIP.md), [kernel](https://github.com/Raccoon-Office/Box-Agent/blob/060edcd2b551a05cd3c68b2c861f97b67a63a653/box_agent/kernel/loop.py).

## Operational model

One user supplies the task/constraints. The principal agent chooses calls to first-party tools, uses feedback to revise its steps, and may delegate separable parts to child agents. Explicit child write scopes and resource permissions isolate competing edits, with the principal agent receiving child outputs/handoffs and retaining final integration authority. Goal autopilot can continue an active goal under bounded continuation/stall policy, but the policy controller is a counter, not a discretionary manager. Changes to core user memory require a distinct user-owned acceptance and then alter future injected context; ordinary tool approvals are not treated as S5.

## S1 — Operations

- State: A
- Function: Perform the user-requested investigation, artifact work, execution and tool-mediated actions.
- Disturbance / variety regulated: Unpredictable user inputs, file contents, external search/tool responses, model errors and changing task evidence.
- Decisive decision or feedback right: Select and revise the concrete action/tool call and answer after interpreting observed results.
- Decision owner: Principal model-driven Agent; a delegated child model independently chooses in-scope steps for its assigned outcome.
- Supporting / enforcement mechanisms: Stable kernel event loop, tool engine, permissions, bounded steps, SessionLog, configured provider clients.
- Closure path: Model selects tool -> guarded tool executes -> tool result returns to its message history -> model chooses the next step or final output.
- Boundary reachability: Shared CLI/ACP `AgentSession.run_events` invokes the released kernel and model/tool pipeline, not a development-only script.
- Why this is / is not agent-owned: Model selects substantive task actions; deterministic gateway and provider SDK only convey/enforce them.
- Evidence: [agent facade](https://github.com/Raccoon-Office/Box-Agent/blob/060edcd2b551a05cd3c68b2c861f97b67a63a653/box_agent/agent.py), [kernel/tool pipeline](https://github.com/Raccoon-Office/Box-Agent/blob/060edcd2b551a05cd3c68b2c861f97b67a63a653/box_agent/kernel/loop.py), [session architecture](https://github.com/Raccoon-Office/Box-Agent/blob/060edcd2b551a05cd3c68b2c861f97b67a63a653/docs/AGENT_SESSION.md).
- Basis: structural
- Confidence: high
- Caveats: No external provider run is claimed; outcome quality depends on a configured model and permissions.

## S2 — Coordination

- State: A
- Function: Prevent conflicting parallel child work from corrupting a shared workspace while retaining several model-operated task cells.
- Disturbance / variety regulated: Independent child agents can write the same file, overwrite sibling results, or return incompatible partial work.
- Decisive decision or feedback right: Principal agent chooses disjoint child output scopes, resolves returned incompatible work and decides what to reassign or integrate.
- Decision owner: Principal agent for the discretionary cross-child resolution; first-party scoped-write wrapper enforces declared path boundaries.
- Supporting / enforcement mechanisms: Child tool capability intersection, exact `write_scope` guards, disjoint parallel outputs, separate child state/isolated Python kernels and parent handoff.
- Closure path: Parent assigns non-overlapping scopes -> children work autonomously -> scoped write guard rejects unauthorized collisions -> child completion/handoff reaches parent -> parent verifies/adjusts integration and later delegation.
- Boundary reachability: `sub_agent` is a first-party optional tool in the ordinary Agent runtime and direct model-visible delegation API.
- Why this is / is not agent-owned: The policy wrapper has no choice about reconciling conflicting semantically valid child outputs; that choice remains with the parent agent.
- Distinct S1 units: Concurrent child agents doing independent user-task subunits, each with its own agent conversation and local tools.
- Inter-S1 disturbance: Concurrent write overlap on the shared artifact workspace, plus incompatible sibling outputs.
- Attenuating coordination relation: Parent-designated distinct file-write scopes and bounded child handoffs, with a single parent integrator.
- Feedback into subsequent S1 behaviour: Parent inspects child results and failed/rejected write outcomes, then scopes follow-up work or adopts one verified result.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: It explicitly regulates the documented concurrent **same-file write collision** using per-child disjoint scopes, then routes conflict resolution to the parent, not just generic messaging or scheduling.
- Evidence: [delegation contract](https://github.com/Raccoon-Office/Box-Agent/blob/060edcd2b551a05cd3c68b2c861f97b67a63a653/docs/SUB_AGENT_DELEGATION.md), [capability resolver](https://github.com/Raccoon-Office/Box-Agent/blob/060edcd2b551a05cd3c68b2c861f97b67a63a653/box_agent/tools/sub_agent_capabilities.py), [child handoff](https://github.com/Raccoon-Office/Box-Agent/blob/060edcd2b551a05cd3c68b2c861f97b67a63a653/box_agent/tools/sub_agent_handoff.py), [subagent execution](https://github.com/Raccoon-Office/Box-Agent/blob/060edcd2b551a05cd3c68b2c861f97b67a63a653/box_agent/tools/sub_agent_tool.py).
- Basis: explicit and structural
- Confidence: medium
- Caveats: Applies only when optional parallel writable children are used; runtime does not autonomously select disjoint paths or resolve source conflicts without the parent model.

## S3 — Inside-and-now control

- State: A
- Function: Regulate the current whole user task's commitments, progress, constrained delegation and continuation after setbacks.
- Disturbance / variety regulated: Multiple competing deliverable steps, stalled work, exhausted delegated budgets, partial worker handoffs and unverified claimed completion.
- Decisive decision or feedback right: Parent agent chooses which work remains, whether to delegate or resume it, which returned result is verified enough to integrate, and whether to replan within the current goal.
- Decision owner: Principal model-driven agent for task-level current-control decisions; human/operator config selects hard limits.
- Supporting / enforcement mechanisms: Goal/Plan/Todo state, SessionLog, run/child call ledgers, guardrail timeouts, child checkpoints, host-visible progress.
- Closure path: Agent reads current task progress plus child handoffs and artifacts -> reallocates/scopes the next work or verifies/finalizes -> updated plan/workspace and next tool calls change present task operations.
- Boundary reachability: Shipped goal/plan/todo model-visible tools and `sub_agent` return verified handoff statuses to the main Agent loop in CLI/ACP.
- Why this is / is not agent-owned: Goal autopilot counters and quota enforcement do not choose the next subtask or accept a contested worker outcome; the parent model does.
- Whole-system current view: The session-level goal, plan, todo and returned child statuses/receipts expose the current set of commitments for one task (not a company-wide fleet).
- Current-control decision scope: Parent decides active task order, delegated scope, continuation/retry and whether to accept/rework an output within owner-selected budgets.
- Evidence: [goal continuation](https://github.com/Raccoon-Office/Box-Agent/blob/060edcd2b551a05cd3c68b2c861f97b67a63a653/box_agent/agent.py), [goal bounds](https://github.com/Raccoon-Office/Box-Agent/blob/060edcd2b551a05cd3c68b2c861f97b67a63a653/box_agent/goal_runtime.py), [todo view](https://github.com/Raccoon-Office/Box-Agent/blob/060edcd2b551a05cd3c68b2c861f97b67a63a653/box_agent/tools/todo_tool.py), [plan state](https://github.com/Raccoon-Office/Box-Agent/blob/060edcd2b551a05cd3c68b2c861f97b67a63a653/box_agent/tools/plan_tool.py), [delegation contract](https://github.com/Raccoon-Office/Box-Agent/blob/060edcd2b551a05cd3c68b2c861f97b67a63a653/docs/SUB_AGENT_DELEGATION.md).
- Basis: structural
- Confidence: medium
- Caveats: A task-local view is not enterprise-wide resource governance. Budget stop/cancellation by itself would not establish S3; this state rests on the parent model's current cross-work commitments and feedback.

## S3* — Complementary audit

- State: C
- Function: Construct an evidence-based, separately tasked review of a model-produced presentation's central factual/content claims, beyond the author's ordinary success report.
- Disturbance / variety regulated: Draft page narratives may silently overstate or distort facts even while routine format/schema validation succeeds.
- Decisive decision or feedback right: Independently tasked content reviewer compares current copy with source passages and returns support/mismatch/unresolved verdicts; parent agent revises the artifact from those findings.
- Decision owner: Review model in a separately invoked native `sub_agent` role when configured; main agent owns acceptance and repair.
- Supporting / enforcement mechanisms: Bundled `ppt-fast` source-review procedure, delegated isolated child context, factual source pointers, outline checker, scripted review receipts.
- Closure path: Main agent prepares current source and outline -> separate reviewer reads raw evidence and copy -> structured findings return -> main agent revises copy or marks explicit gaps and revalidates deliverable.
- Boundary reachability: `box_agent/skills/document-skills/pptx/SKILL.md` and its content-review-role source are shipped first-party task Skills for an opt-in PPT workflow, while native `sub_agent` is shipped in Box Agent; the independent model invocation must be composed for the particular run.
- Why this is / is not agent-owned: Content support/mismatch judgment is made by a distinct model reviewer, not by schema validation or the original author's own claims.
- Claim being audited: Model author's presentation claim accuracy, scope, factual support and content framing.
- Ordinary reporting path: Main author writes validated outline, draft deck and source facts.
- Complementary access path: Reviewer directly reads raw/canonical evidence and current draft copy, may use bounded contrary-source lookups, and challenges content assertions independently.
- Independence boundary: First-party role-specific instruction plus separate child context, *not* guaranteed blind review or distinct provider. This is a conditional constructor, not observed independent execution.
- Who acts on findings: Main agent owns edits/rechecks, while user controls delivery and acceptance.
- Evidence: [bundled PPT Skill](https://github.com/Raccoon-Office/Box-Agent/blob/060edcd2b551a05cd3c68b2c861f97b67a63a653/box_agent/skills/document-skills/pptx/SKILL.md), [independent reviewer contract](https://github.com/Raccoon-Office/Box-Agent/blob/060edcd2b551a05cd3c68b2c861f97b67a63a653/box_agent/skills/document-skills/pptx/references/content-review-role.md), [subagent isolation](https://github.com/Raccoon-Office/Box-Agent/blob/060edcd2b551a05cd3c68b2c861f97b67a63a653/docs/SUB_AGENT_DELEGATION.md).
- Basis: explicit
- Confidence: medium
- Caveats: `C` applies only to a supported optional domain mode with correctly invoked independent reviewer; no actual completed audit was observed. The repository's unrelated `general_review/` PR review standard does not receive credit.

## S4 — Outside-and-then intelligence

- State: —
- Function: No first-party supported loop was established that develops prospective capability adaptation from external/future distinctions and returns it to present task governance.
- Disturbance / variety regulated: Changing external tools, providers, threat landscapes, and future user needs could demand sustained adaptation.
- Decisive decision or feedback right: Model can research and suggest changes for the current task; host/user config and installed Skills determine longer-term capability changes, without a demonstrated first-party future-oriented adapter.
- Decision owner: No qualifying ongoing S4 owner at the assessed task/session boundary.
- Supporting / enforcement mechanisms: Web tools, long-term memory, local skill discovery/install, goal planner and host configuration are available but not themselves an S4 intelligence loop.
- Closure path: Current-task search, memory and explicit host installation do not source-prove a future-directed environmental option-selection loop returning to sustained current capabilities.
- Why this is / is not agent-owned: A task plan or memory fact is not externally prospective adaptation.
- Evidence: [workflow ownership](https://github.com/Raccoon-Office/Box-Agent/blob/060edcd2b551a05cd3c68b2c861f97b67a63a653/docs/WORKFLOW_OWNERSHIP.md), [goal runtime](https://github.com/Raccoon-Office/Box-Agent/blob/060edcd2b551a05cd3c68b2c861f97b67a63a653/box_agent/goal_runtime.py), [memory proposals](https://github.com/Raccoon-Office/Box-Agent/blob/060edcd2b551a05cd3c68b2c861f97b67a63a653/docs/MEMORY_PROPOSAL_PROTOCOL.md), [user choices](https://github.com/Raccoon-Office/Box-Agent/blob/060edcd2b551a05cd3c68b2c861f97b67a63a653/docs/USER_DECISION_PROTOCOL.md).
- Basis: structural
- Confidence: medium
- Caveats: User-configured specialized research/agent Skills could construct S4, but arbitrary custom extensions are outside the declared standard operating boundary.

### Absence scope

- Surfaces inspected: Model/tool loop, goals, plan/todo, web/tool and memory entry points, skill lifecycle, configuration/host path and bundled presentation reviewer.
- Plausible first-party paths checked: Web/research and skill installation, automatic memory promotion, scheduled task drafting, and goal-autopilot continuation.
- Why no material first-party path remains: Inspected paths address current task data, user memory or explicit host approvals; none in the shipped general operating boundary establishes a governed external-and-future signal -> adaptation option -> present-capability return loop. The schedule tool only emits a host draft without confirmation that any automation was saved.

## S5 — Policy and identity

- State: P
- Function: Permit the legitimate human to decide what durable user-profile/preference information becomes a high-authority core identity context for subsequent sessions.
- Disturbance / variety regulated: Automatically learned or inferred personal preferences might be promoted into always-injected context incorrectly, altering long-lived user/agent alignment.
- Decisive decision or feedback right: Human decides whether a proposed user/profile/preference item is pinned, skipped or permanently rejected as core memory.
- Decision owner: User (parent authority at this personal-agent recursion); local memory manager and ACP host transport the decision.
- Supporting / enforcement mechanisms: Thresholded v2 experience candidates, host Pull/Apply protocol, user-visible three-way decision, deduplication and `MEMORY.md` loader.
- Closure path: Agent identifies candidate -> host presents candidate -> human gives `pin`/`skip`/`reject` -> Apply writes/retains core memory -> future sessions inject updated `MEMORY.md` as high-authority persistent personal context. Generic task permission prompts are not credited.
- Boundary reachability: First-party ACP memory-proposal Pull/Apply and built-in memory manager are documented as supported; a configured local core-memory mode and real human decision are required.
- Why this is / is not agent-owned: The model cannot authoritatively elevate a candidate into core identity on its own through the promotion path; user owns the decision and memory backend applies it.
- Identity / ultimate-policy issue: Durable user profile/preference commitments that affect ongoing personal-agent behavior, not a one-off file edit or ordinary task approval.
- Ultimate authority in each claimed mode: Human user only; no independent first-party agent-owned S5 mode established.
- Return-to-operation path: `MEMORY.md` after `pin` is read into subsequent session's system context; `reject` permanently suppresses future proposal.
- Evidence: [core-memory proposal protocol](https://github.com/Raccoon-Office/Box-Agent/blob/060edcd2b551a05cd3c68b2c861f97b67a63a653/docs/MEMORY_PROPOSAL_PROTOCOL.md), [memory tools](https://github.com/Raccoon-Office/Box-Agent/blob/060edcd2b551a05cd3c68b2c861f97b67a63a653/box_agent/tools/memory_tool.py), [agent session](https://github.com/Raccoon-Office/Box-Agent/blob/060edcd2b551a05cd3c68b2c861f97b67a63a653/docs/AGENT_SESSION.md).
- Basis: explicit
- Confidence: medium
- Caveats: This narrowly credits *identity-context* governance in the documented enabled memory mode, not maintainer code governance or generic permissions. If the documented protocol is not reachable in the current standard ACP distribution, downgrade to `?` after targeted packaging/entry-point verification.

## Distributed OSS parent arrangement

Repository maintainers own project/code development policy, but their PR gate is not the assessed personal-task runtime. S5 parent mode is local to a configured user's own task agent and durable memory; no organization-wide policy identity authority is inferred from multiple contributors.

## Self-hosted and non-human modes

Self-hosted CLI and ACP permit distinct operator controls. Host-supplied task permissions and budgets constrain execution but do not by themselves create additional parent-governed S3/S4 modes. No supported non-human whole-organization recursion is claimed.

## Recursion

The model-driven principal agent and child cells can display local autonomy and distinct outputs. Child spawning alone does not establish a self-sufficient recursively viable system, and child authority remains inside parent-scoped tools, budgets and permissions.

## Variety and escalation

User instructions, file/test evidence and external tool feedback flow into model decisions. Child concurrency amplifies available operational variety but also risks clashing writes; disjoint scopes attenuate this. Timeouts, no-progress limits, permission requests and handoffs can escalate unmanageable variety to principal agent or human. An exceptional notification by itself is not a distinct VSM function.

## Evidence gaps

- Static source/contract inspection only; no live LLM/provider/host deployment was executed and no real independent reviewer verdict was observed.
- S3 current-control remains task-local; do not generalize to organizational fleet management.
- S3* reviewer is a shipped optional construction mode, not a blanket always-on audit guarantee.
- S5 P depends on the documented local-core-memory/ACP supported mode being wired when enabled. The user-authority closure is evidenced in the protocol, but no interactive acceptance was run during review.

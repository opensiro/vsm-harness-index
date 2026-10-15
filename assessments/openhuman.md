---
harness_id: openhuman
project_name: OpenHuman
repository: https://github.com/tinyhumansai/openhuman
review_ref: eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d
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

# OpenHuman

## Review boundary
- System in focus: the frozen first-party OpenHuman Rust agent host and orchestrator, running a local model/tool operational agent, subordinate worker agents and the shipped team/parallel-task controls.
- Purpose and identity: perform conversational and automated user tasks through model-directed tool use, while coordinating attached task workers and returning their outcomes to a project-level parent.
- Relevant environment: local workspace, user messages and external events, provider API responses, managed or BYOK inference, tools, evolving files, memory, task lifecycle and local user approval.
- Standard-distribution boundary: first-party `openhuman-core`, CLI/embedding/app wiring and OpenHuman-owned adapters/policy around declared `tinyagents` graph dependencies. The external upstream `tinyagents`, `tinyflows` and third-party services' internal choices do not count as OpenHuman-authored metasystem ownership ([Cargo.toml](https://github.com/tinyhumansai/openhuman/blob/eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d/Cargo.toml); [gitbooks/developing/architecture/agent-harness.md](https://github.com/tinyhumansai/openhuman/blob/eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d/gitbooks/developing/architecture/agent-harness.md)).
- Credited operating / distribution surfaces: [crates/openhuman-core/src/agent/tinyagents/turn_runner.rs](https://github.com/tinyhumansai/openhuman/blob/eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d/crates/openhuman-core/src/agent/tinyagents/turn_runner.rs); [crates/openhuman-core/src/agent/tinyagents/turn_runner_inner.rs](https://github.com/tinyhumansai/openhuman/blob/eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d/crates/openhuman-core/src/agent/tinyagents/turn_runner_inner.rs); [crates/openhuman-core/src/agent/orchestration/tools/spawn_parallel_agents.rs](https://github.com/tinyhumansai/openhuman/blob/eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d/crates/openhuman-core/src/agent/orchestration/tools/spawn_parallel_agents.rs); [crates/openhuman-core/src/agent/orchestration/spawn_parallel_graph/staging.rs](https://github.com/tinyhumansai/openhuman/blob/eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d/crates/openhuman-core/src/agent/orchestration/spawn_parallel_graph/staging.rs); [crates/openhuman-core/src/agent/orchestration/running_subagents/registry.rs](https://github.com/tinyhumansai/openhuman/blob/eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d/crates/openhuman-core/src/agent/orchestration/running_subagents/registry.rs); [crates/openhuman-core/src/agent/orchestration/tools/steer_subagent.rs](https://github.com/tinyhumansai/openhuman/blob/eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d/crates/openhuman-core/src/agent/orchestration/tools/steer_subagent.rs); [crates/openhuman-core/src/agent/orchestration/agent_teams/runtime.rs](https://github.com/tinyhumansai/openhuman/blob/eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d/crates/openhuman-core/src/agent/orchestration/agent_teams/runtime.rs).
- Adjacent first-party surfaces excluded from ownership: tests/e2e fixtures, stale historical architecture passages describing removed in-tree loop, publication/marketing claims not wired in executable code, standalone upstream tinyagents/tinyflows projects, provider-host native internals and user-created independent organizations.
- First-party operating / deployment modes considered: normal host-managed agent turn; opt-in `spawn_parallel_agents` with shared-workspace file claims and optional isolated worktrees; first-party subagent task supervision and steering; agent-teams and durable status projection; user plan-approval mode; post-turn memory/learning.
- Recursion level: an OpenHuman-owned parent conversation/team coordinating its subordinate independent task runs. Not the external provider company or all user-connected apps.
- Reviewed revision: `eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d`.
- Observation date: 2026-10-12.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture
Current first-party host entrypoints route live agent turns through a `tinyagents` harness dependency; model-proposed tool calls are bound to OpenHuman's tool registry, parent execution context and product policy. The maintained architecture text explicitly warns that an older hand-built `run_turn_engine` was removed and must not be credited. Instead the actual Rust agent/tinyagents adapter calls the provider-backed loop, while the OpenHuman host supplies isolation, tooling, source-identity and persisted session integration. [gitbooks/developing/architecture/agent-harness.md](https://github.com/tinyhumansai/openhuman/blob/eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d/gitbooks/developing/architecture/agent-harness.md); [crates/openhuman-core/src/agent/tinyagents/turn_runner.rs](https://github.com/tinyhumansai/openhuman/blob/eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d/crates/openhuman-core/src/agent/tinyagents/turn_runner.rs); [crates/openhuman-core/src/agent/tinyagents/turn_runner_inner.rs](https://github.com/tinyhumansai/openhuman/blob/eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d/crates/openhuman-core/src/agent/tinyagents/turn_runner_inner.rs).
For multi-agent execution, `spawn_parallel_agents` takes distinct tasks, an allowed-agent definition and an explicit live parent. OpenHuman validates which workers can write the shared workspace, checks file-path ownership claims and invokes one contention-aware dispatch plan; overlapping claims are rejected with an isolation/disjoint-path repair hint while non-colliding tasks may run in parallel. This is a concrete first-party conflict attenuation relation even though the generic workspace arbitration primitive is reused from the dependent harness library. [crates/openhuman-core/src/agent/orchestration/tools/spawn_parallel_agents.rs](https://github.com/tinyhumansai/openhuman/blob/eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d/crates/openhuman-core/src/agent/orchestration/tools/spawn_parallel_agents.rs#L129-L223); [crates/openhuman-core/src/agent/orchestration/spawn_parallel_graph/staging.rs](https://github.com/tinyhumansai/openhuman/blob/eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d/crates/openhuman-core/src/agent/orchestration/spawn_parallel_graph/staging.rs#L175-L225); [crates/openhuman-core/src/agent/orchestration/spawn_parallel_graph/staging.rs](https://github.com/tinyhumansai/openhuman/blob/eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d/crates/openhuman-core/src/agent/orchestration/spawn_parallel_graph/staging.rs#L350-L454).
The parent can obtain child/task lifecycle reports and send mid-flight steering instructions; a task registry enforces the parent session owner. The command center presents durable status and human actions separately. [crates/openhuman-core/src/agent/orchestration/running_subagents/registry.rs](https://github.com/tinyhumansai/openhuman/blob/eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d/crates/openhuman-core/src/agent/orchestration/running_subagents/registry.rs#L1-L20); [crates/openhuman-core/src/agent/orchestration/tools/steer_subagent.rs](https://github.com/tinyhumansai/openhuman/blob/eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d/crates/openhuman-core/src/agent/orchestration/tools/steer_subagent.rs#L111-L210); [crates/openhuman-core/src/agent/orchestration/command_center/ops.rs](https://github.com/tinyhumansai/openhuman/blob/eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d/crates/openhuman-core/src/agent/orchestration/command_center/ops.rs).

## Operational model
One user request starts a model-led tool cycle. As operating work becomes decomposed into independent parallel/async units, the active OpenHuman parent can allocate, monitor, steer, cancel and reassign child work while host execution policies enforce the allowed actions. Separate external providers supply LLM inference, but first-party parent-team task authority and file-interference gates are exercised through shipped OpenHuman tools. Automated checks and human approvals remain distinct from evidence of an independent organizational audit or ultimate policy owner.

## S1 — Operations
- State: A
- Function: Model-directed first-party agent turns and executable subordinate task agents perform user work through tool/environment actions and observation feedback.
- Disturbance / variety regulated: Dynamic user tasks, changing workspace, provider/tool errors, remote-page/tool results, context limitations and child-work outcomes.
- Decisive decision or feedback right: Choose task-specific tools/actions in the active hosted agent turn, and initiate further work based on results.
- Decision owner: The OpenHuman-configured model-driven agent in its first-party host mode; the dependent generic harness executes the loop without owning the product-specific delegated task choice.
- Supporting / enforcement mechanisms: OpenHuman core session host, tools, model routing, policies, token/iteration stop hooks, storage and TinyAgents loop substrate.
- Closure path: User/event goal → hosted model/tool-turn proposal → allowed tool action → observed result → next model decision, completion or revised attempt.
- Boundary reachability: OpenHuman documents an actual installed app/CLI/embedded host route and wires the running turn through first-party tinyagents adapters, not an example/test-only graph ([gitbooks/developing/architecture/agent-harness.md](https://github.com/tinyhumansai/openhuman/blob/eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d/gitbooks/developing/architecture/agent-harness.md); [crates/openhuman-core/src/agent/tinyagents/turn_runner.rs](https://github.com/tinyhumansai/openhuman/blob/eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d/crates/openhuman-core/src/agent/tinyagents/turn_runner.rs)).
- Why this is / is not agent-owned: The executed action choices are agent/model-directed; neither budget guards nor the graph runner's deterministic control transfer constitutes a substitute decision owner.
- Evidence: [crates/openhuman-core/src/agent/tinyagents/turn_runner.rs](https://github.com/tinyhumansai/openhuman/blob/eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d/crates/openhuman-core/src/agent/tinyagents/turn_runner.rs); [crates/openhuman-core/src/agent/tinyagents/turn_runner_inner.rs](https://github.com/tinyhumansai/openhuman/blob/eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d/crates/openhuman-core/src/agent/tinyagents/turn_runner_inner.rs); [crates/openhuman-core/src/agent/orchestration/tools/spawn_subagent.rs](https://github.com/tinyhumansai/openhuman/blob/eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d/crates/openhuman-core/src/agent/orchestration/tools/spawn_subagent.rs); [gitbooks/developing/architecture/agent-harness.md](https://github.com/tinyhumansai/openhuman/blob/eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d/gitbooks/developing/architecture/agent-harness.md).
- Basis: structural
- Confidence: high
- Caveats: Source evidence establishes mode/reachability, not model competence; no live provider-backed trajectory was executed.

## S2 — Coordination
- State: C
- Function: Regulate concrete shared-workspace file-write conflicts among separately active delegated subagents.
- Distinct S1 units: A parent schedules multiple independent subagent tasks via `spawn_parallel_agents`, each bound to an allowed agent definition, task ID, tools and workspace rights ([crates/openhuman-core/src/agent/orchestration/tools/spawn_parallel_agents.rs](https://github.com/tinyhumansai/openhuman/blob/eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d/crates/openhuman-core/src/agent/orchestration/tools/spawn_parallel_agents.rs#L129-L223)).
- Inter-S1 disturbance: Two write-capable parallel workers editing the same workspace paths can overwrite or race against one another; the worktree module records prior stale assumptions/silent clobber hazards ([crates/openhuman-core/src/agent/orchestration/worktree.rs](https://github.com/tinyhumansai/openhuman/blob/eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d/crates/openhuman-core/src/agent/orchestration/worktree.rs#L1-L20)).
- Attenuating coordination relation: OpenHuman assembles per-task shared-workspace write claims, rejects unscoped write access, identifies overlapping path claims, supplies isolation/disjoint-path remedy and restricts dispatch to compatible parallel or safe serial plans ([crates/openhuman-core/src/agent/orchestration/spawn_parallel_graph/staging.rs](https://github.com/tinyhumansai/openhuman/blob/eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d/crates/openhuman-core/src/agent/orchestration/spawn_parallel_graph/staging.rs#L175-L225); [crates/openhuman-core/src/agent/orchestration/spawn_parallel_graph/staging.rs](https://github.com/tinyhumansai/openhuman/blob/eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d/crates/openhuman-core/src/agent/orchestration/spawn_parallel_graph/staging.rs#L350-L454)).
- Feedback into subsequent S1 behaviour: Conflicting worker requests are returned as rejection/actionable correction to the calling model, while allowed workers run isolated or serialized; the parent receives outcomes for subsequent work ([crates/openhuman-core/src/agent/orchestration/spawn_parallel_graph/staging.rs](https://github.com/tinyhumansai/openhuman/blob/eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d/crates/openhuman-core/src/agent/orchestration/spawn_parallel_graph/staging.rs#L400-L454)).
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The explicit relation is between independently editing subagents under the same root and is triggered by their actual file ownership overlap, not just a task queue or message bus.
- Disturbance / variety regulated: Parallel task write interference, invalid ownership boundaries, overlapping paths, unsafe shared mutations.
- Decisive decision or feedback right: Grant parallel execution, serialize, refuse or demand isolation based on path overlap.
- Decision owner: OpenHuman-owned staging and policy adapter invoking a deterministic first-party-controlled contention planner (`C`), not a model-led metacoordinator.
- Supporting / enforcement mechanisms: `WorkspaceClaim`, shared-write preview, isolation flags, subagent allowlists, dispatcher and Git worktrees.
- Closure path: Competing per-worker claims → first-party request validation plus claim planning → admitted/rejected or serial/parallel changed execution → result/rejection to parent and adjusted next child work.
- Boundary reachability: `spawn_parallel_agents` is a registered runtime tool and routes to the same staging/dispatch code; it is not a dormant library class ([crates/openhuman-core/src/agent/orchestration/tools/spawn_parallel_agents.rs](https://github.com/tinyhumansai/openhuman/blob/eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d/crates/openhuman-core/src/agent/orchestration/tools/spawn_parallel_agents.rs#L81-L123); [crates/openhuman-core/src/agent/orchestration/spawn_parallel_graph/staging.rs](https://github.com/tinyhumansai/openhuman/blob/eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d/crates/openhuman-core/src/agent/orchestration/spawn_parallel_graph/staging.rs)).
- Why this is / is not agent-owned: Conflict attenuation is actually operational, but its decisive per-claim grant is a deterministic program, not autonomous agent coordination authority.
- Evidence: [crates/openhuman-core/src/agent/orchestration/worktree.rs](https://github.com/tinyhumansai/openhuman/blob/eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d/crates/openhuman-core/src/agent/orchestration/worktree.rs); [crates/openhuman-core/src/agent/orchestration/spawn_parallel_graph/staging.rs](https://github.com/tinyhumansai/openhuman/blob/eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d/crates/openhuman-core/src/agent/orchestration/spawn_parallel_graph/staging.rs); [crates/openhuman-core/src/agent/orchestration/tools/spawn_parallel_agents.rs](https://github.com/tinyhumansai/openhuman/blob/eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d/crates/openhuman-core/src/agent/orchestration/tools/spawn_parallel_agents.rs).
- Basis: structural
- Confidence: high
- Caveats: Scope is explicit first-party parallel-agent mode with claim/isolation policy; not a universal concurrency guarantee for all OpenHuman workspaces or the external dependency's generic scheduler.

## S3 — Inside-and-now control
- State: A
- Function: Model-driven parent agent regulates current commitments and intervention over its running subagent team.
- Disturbance / variety regulated: Active child tasks, stuck or failed work, unexpected results, required mid-flight correction and cancellation.
- Decisive decision or feedback right: Based on child rosters and returned results, parent can delegate additional work, steer a running child, collect, wait or close work.
- Decision owner: OpenHuman's hosted model-driven parent agent; the status registry and command-center buttons merely implement/access those decisions.
- Supporting / enforcement mechanisms: Task registry, owner-scoped steering queue, list/wait tools, task ledger, cancellation tokens and parent-context gates.
- Whole-system current view: The parent has a roster of its live subordinate tasks, run status and returned outcomes in its bounded team recursion, rather than full organizational control of every unrelated user session.
- Current-control decision scope: Allocation, priority/intent revision, cancellation and recovery of the parent team's active work.
- Closure path: Child status/outcome → parent observes via list/wait/return → chooses steering/new assignment/cancellation → child receives new instruction or next run is changed.
- Boundary reachability: Shipped parent-context runtime registers subagent control tools; `steer_subagent` enforces parent ownership and inserts a live message consumed mid-flight by the child's turn ([crates/openhuman-core/src/agent/orchestration/tools/steer_subagent.rs](https://github.com/tinyhumansai/openhuman/blob/eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d/crates/openhuman-core/src/agent/orchestration/tools/steer_subagent.rs#L111-L210); [crates/openhuman-core/src/agent/orchestration/running_subagents/registry.rs](https://github.com/tinyhumansai/openhuman/blob/eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d/crates/openhuman-core/src/agent/orchestration/running_subagents/registry.rs#L1-L20)).
- Why this is / is not agent-owned: Resource/commitment decisions are contingent model/parent-directed task commands over distinct workers, not inference from a passive status dashboard or timer.
- Evidence: [crates/openhuman-core/src/agent/orchestration/tools/list_subagents.rs](https://github.com/tinyhumansai/openhuman/blob/eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d/crates/openhuman-core/src/agent/orchestration/tools/list_subagents.rs); [crates/openhuman-core/src/agent/orchestration/tools/steer_subagent.rs](https://github.com/tinyhumansai/openhuman/blob/eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d/crates/openhuman-core/src/agent/orchestration/tools/steer_subagent.rs); [crates/openhuman-core/src/agent/orchestration/running_subagents/registry.rs](https://github.com/tinyhumansai/openhuman/blob/eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d/crates/openhuman-core/src/agent/orchestration/running_subagents/registry.rs); [crates/openhuman-core/src/agent/orchestration/agent_teams/runtime.rs](https://github.com/tinyhumansai/openhuman/blob/eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d/crates/openhuman-core/src/agent/orchestration/agent_teams/runtime.rs).
- Basis: structural
- Confidence: medium
- Caveats: Explicitly a parent-subagent team recursion, not an enterprise-wide S3 owner; separate human command-center operator mode is not credited as `P` without its full function-specific parent loop.

## S3* — Complementary audit
- State: ?
- Function: Delegation includes a model `review` stage, but the shipped path has not established material independence and operational-artifact sampling distinct from the ordinary producing stage.
- Disturbance / variety regulated: Defective subagent completion claims, unsafe or incomplete task results and quality gaps.
- Decisive decision or feedback right: A review-stage output can request revision, but separate audit function/owner is unproven from the reviewed source.
- Decision owner: Delegation stage worker; may be a distinct stage but not proven to be an independently sampling auditor.
- Supporting / enforcement mechanisms: Delegation `plan → execute ⇄ review → finalize` graph, review_approves output, revision budget, run checkpoints.
- Claim being audited: Whether an execution-stage result fulfills its assigned task.
- Ordinary reporting path: Producing subagent returns its text/work result to the delegation graph.
- Complementary access path: A distinct review-stage model call receives the prior textual result/task, but no guaranteed independently obtained operational-artifact evidence path is established.
- Independence boundary: Not established; distinct stage alone does not prove independent observational access.
- Who acts on findings: Delegation controller can repeat execute using reviewer feedback, yet full audit-specific independence remains unproven.
- Closure path: Review text → approve/revise → subsequent execute; does not yet meet the complete independent audit threshold.
- Why this is / is not agent-owned: A generic review prompt or retry stage is not inherently S3* even when used after code production.
- Evidence: [crates/openhuman-core/src/agent/orchestration/delegation.rs](https://github.com/tinyhumansai/openhuman/blob/eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d/crates/openhuman-core/src/agent/orchestration/delegation.rs#L175-L257); [crates/openhuman-core/src/agent/plan_review/mod.rs](https://github.com/tinyhumansai/openhuman/blob/eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d/crates/openhuman-core/src/agent/plan_review/mod.rs); [crates/openhuman-core/src/agent/orchestration/workflow_runs/engine.rs](https://github.com/tinyhumansai/openhuman/blob/eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d/crates/openhuman-core/src/agent/orchestration/workflow_runs/engine.rs).
- Basis: unknown
- Confidence: low
- Caveats: Search other shipped review/inspection and parent corrective paths before a positive or bounded `—` conclusion; the architecture document also mentions a now-removed delegation adapter, so exact live reachability must be checked.

## S4 — Outside-and-then intelligence
- State: ?
- Function: Memory ingestion, autonomous learning and scheduled workflow construction may support future capability adaptation, but a source-grounded external/prospective choice and returned capability-change closure is not yet established.
- Disturbance / variety regulated: Changing documents/tasks/integrations and future user requirements.
- Decisive decision or feedback right: Undetermined whether a first-party agent or parent actually selects and integrates an external future adaptation option beyond immediate task improvement.
- Decision owner: Unresolved among learning/memory agent, workflow author, operator and settings.
- Supporting / enforcement mechanisms: Persistent memory agents, goal state, scheduled sources, task post-turn hooks and workflow builder.
- External distinction: Automated ingestion can observe external connected-source changes, but external observation by itself is not S4.
- Future / prospective distinction: Retained memory and scheduled workflows affect future runs; prospective reasoning/authority to adapt organizational capability has not been traced.
- Adaptation option generated: Not established in the required external/longer-horizon organizational sense.
- Path back into current capability / S3: New memory can appear in later prompts, but this alone does not prove the complete S4 closure.
- Closure path: Ingestion → retained context → later agent prompt; possible broader adaptation remains unresolved.
- Why this is / is not agent-owned: Historical memory and scheduling are not automatically outside-and-then intelligence.
- Evidence: [crates/openhuman-core/src/memory/agent/README.md](https://github.com/tinyhumansai/openhuman/blob/eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d/crates/openhuman-core/src/memory/agent/README.md); [crates/openhuman-core/src/agent/learning](https://github.com/tinyhumansai/openhuman/blob/eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d/crates/openhuman-core/src/agent/learning/README.md); [crates/openhuman-core/src/flows/agents](https://github.com/tinyhumansai/openhuman/blob/eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d/crates/openhuman-core/src/flows/agents/mod.rs); [gitbooks/features/workflows.md](https://github.com/tinyhumansai/openhuman/blob/eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d/gitbooks/features/workflows.md).
- Basis: unknown
- Confidence: low
- Caveats: Review actual active learning agent and workflow builder paths before resolving S4.

## S5 — Policy and identity
- State: ?
- Function: Live autonomy/tool safety policies and human approval operate, but no full identity/ultimate-policy organizational decision and returned governing feedback loop has been established at parent-team recursion.
- Disturbance / variety regulated: Tool permissions, sandbox and egress restrictions, access level, user security approvals.
- Decisive decision or feedback right: User can approve/deny actions and configure tools; whether that amounts to ultimate organizational policy authority remains unresolved.
- Decision owner: Human operator and deterministic core enforcement; neither by itself demonstrates a canonical S5 parent mode.
- Supporting / enforcement mechanisms: First-party security policies, approval gates, parent subagent allowlists and plan-review human interruption.
- Identity / ultimate-policy issue: Allowed identity/policy for a local agent team and permitted external actions.
- Ultimate authority in each claimed mode: Unresolved, no positive autonomous or parent mode credited.
- Return-to-operation path: Tool permission/approval changes can alter individual execution; an ultimate-policy decision returning to govern continued organization is not proven.
- Closure path: User permission/action guard → authorize or deny action; insufficient to establish S5.
- Why this is / is not agent-owned: Generic sandbox/policy flags are enforcement, not independent ultimate-policy judgment.
- Evidence: [crates/openhuman-core/src/security/approval](https://github.com/tinyhumansai/openhuman/blob/eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d/crates/openhuman-core/src/security/approval/mod.rs); [crates/openhuman-core/src/agent/plan_review/mod.rs](https://github.com/tinyhumansai/openhuman/blob/eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d/crates/openhuman-core/src/agent/plan_review/mod.rs); [crates/openhuman-core/src/agent/orchestration/spawn_parallel_graph/staging.rs](https://github.com/tinyhumansai/openhuman/blob/eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d/crates/openhuman-core/src/agent/orchestration/spawn_parallel_graph/staging.rs).
- Basis: unknown
- Confidence: low
- Caveats: Examine actual parent-governance identity/policy return path before upgrading to `P` or deriving bounded absence.

## Recursion
One conversation/tool-loop and its subagent instances are operating S1 units. The parent conversation acts as a current-control higher recursion for the explicitly spawned task-team mode. The OS user and external provider/tool systems are separate; independent TinyAgents library primitives are not credited as OpenHuman-specific organizational ownership without a shipped OpenHuman decision/closure integration.

## Variety and escalation
Dynamic task execution uses model/tool feedback; shared workspace claims attenuate collision; subagent status and steering form parent-team current-control feedback. Workflow approvals and task stop rules are constraints, not proof of S5 or complementary audit. Persistence and memory reuse do not automatically supply S4.

## Evidence gaps
Static primary-source inspection of one frozen checkout; no provider-backed agent run. OpenHuman's maintained documentation contains historical references to removed code, which were not counted as working operational evidence. S3* complementary source sampling, S4 prospective adaptation and S5 identity/ultimate-policy closure remain explicitly unknown. Revisit those first-party paths under a separate evidence update rather than claiming a negative from partial coverage.

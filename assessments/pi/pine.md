---
harness_id: pine
project_name: PINE
repository: https://github.com/pmndre/pine
review_ref: c9dbfd129a8574459e37cfa834662b0fa8ca8a1b
reviewed_at: 2026-11-18
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: P
---

# PINE

## Review boundary

- System in focus: One installed PINE daemon and its configured agents, shared policy files, event sources and owner-facing control surface.
- Purpose and identity: Sustain multiple tool-using agents that execute operator tasks and react to subscribed external events while retaining distinct sessions, tools and workspaces.
- Relevant environment: User messages, files, websites, local programs/devices, scheduled events, external MCP/model services, owner policy and competing requests for shared compute and repositories.
- Standard-distribution boundary: Bundled Node runtime, pi model-backed sessions, tools, event router, source adapters, local owner API/CLI/TUI, and optional first-party delegate/subagent and worktree modes. Models, model providers and individual user-written source modules are external.
- Credited operating / distribution surfaces: Shipped agent execution, source subscriptions, delegation, isolated worktrees with merge/conflict handling, owner activity/status and current-control endpoints, and shared owner/global instruction updates.
- Adjacent first-party surfaces excluded from ownership: This repository's own release CI, development and tests, reference demonstrations and owner-added agent/source implementations not wired into standard deployment.
- First-party operating / deployment modes considered: Linux/macOS daemon in operator-authenticated mode; default main and configured secondary agents; optional concurrent subagents/delegates in Git worktrees; owner control API and shared instruction files.
- Recursion level: One PINE installation as a multi-agent operational organization; individual agent sessions are operational units, not automatically separately viable recursions.
- Reviewed revision: `c9dbfd129a8574459e37cfa834662b0fa8ca8a1b`.
- Observation date: 2026-11-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

PINE runs model-backed agent sessions with memory, tool dispatch, durable tasks and a central event bus. A source subscription can wake a conversation on a filesystem, time, message or external event; the router retains event trust and delivers subsequent input. The main agent can create configured subsidiary agents, while a `delegate` tool hands them independent tasks; `subagent` runs bounded, parallel, fresh-context work. Isolated Git worktrees hold each concurrent code job on a branch. The control API exposes agents, tasks, status, approvals and settings to the local owner, who can cancel tasks and set global operating parameters. Tool security and sandbox gates are enforced by the runtime; the owner grants critical rights.

## Operational model

Each model-driven conversation acts on local state and external tool results to produce user-requested work or responses to events. In worktree mode two separately executing agents/subagents may modify the same source repository without directly overwriting one another. The initiating agent chooses whether and how to delegate and isolate work, then receives branch summaries and decides how to integrate changes. The owner retains current control over the multi-agent installation and decides durable cross-agent instructions; runtime settings and approval mechanisms implement these decisions.

## S1 — Operations

- State: A
- Function: Carry out event-triggered and requested tasks using model-directed tools and independent agent sessions.
- Disturbance / variety regulated: Distinct user objectives, changing external events, file state, model responses and tool results.
- Decisive decision or feedback right: Select tools, edits, responses and further tasks from current context.
- Decision owner: Installed model-backed agent session, within owner-set access and model constraints.
- Supporting / enforcement mechanisms: Task persistence, pi session runtime, source subscriptions, task queue, sandbox and tool gates.
- Closure path: Model/tool feedback changes the next action; resulting files, emitted messages and task state persist into future interactions.
- Boundary reachability: Standard `pine init` includes main agent and model session runtime; source events and operator prompts are both wired to the same task submit/execute path.
- Why this is / is not agent-owned: The model makes task-level choices; PINE's deterministic event transport and permissions do not choose the task's substantive outcome.
- Evidence: [installed runtime](https://github.com/pmndre/pine/blob/c9dbfd129a8574459e37cfa834662b0fa8ca8a1b/docs/references/operations.md#L16-L35), [task submission and model dispatch](https://github.com/pmndre/pine/blob/c9dbfd129a8574459e37cfa834662b0fa8ca8a1b/src/agents.ts#L688-L750), [run and session loop](https://github.com/pmndre/pine/blob/c9dbfd129a8574459e37cfa834662b0fa8ca8a1b/src/agents.ts#L1853-L1883), [source-to-agent event path](https://github.com/pmndre/pine/blob/c9dbfd129a8574459e37cfa834662b0fa8ca8a1b/src/router.ts#L101-L139).
- Basis: structural
- Confidence: high
- Caveats: Requires an actually configured reachable model. No live model task was executed during this source-based review.

## S2 — Coordination

- State: A
- Function: Attenuate concurrent operational agents' conflicting edits to the same Git repository.
- Disturbance / variety regulated: Simultaneous independent code edits can overwrite each other or conflict when brought back to the common branch.
- Decisive decision or feedback right: Initiating agent selects isolated worktree mode for delegated/subagent tasks and then decides how to merge, retry or resolve conflicting branches after receiving results.
- Decision owner: Initiating model-backed coding agent in a supported owner-trusted session; runtime only executes Git safety rules.
- Supporting / enforcement mechanisms: Independent `pine/*` branches, worktree allocation, merge-tree checks, no-overwrite merge gates and conflict details returned to the initiating actor.
- Closure path: Each child writes to a separate checkout; its returned branch information informs the initiator's subsequent integration. Merge conflicts identify overlapping files and require resolution before advancing the base.
- Boundary reachability: `delegate` and `subagent` both expose `worktree: true` in the standard tools and return branch/merge instructions; the owner control API also offers conflict-aware merge operations.
- Why this is / is not agent-owned: The lead can decide whether to isolate, how to integrate and how to revise an overlapping assignment; fixed Git commands merely implement/refuse that decision.
- Distinct S1 units: Two agent/subagent tasks with separate model sessions, outputs and worktree branches, working on a shared project.
- Inter-S1 disturbance: Concurrent writes to one checkout and divergent edits to the same file during integration.
- Attenuating coordination relation: Runtime-enforced independent worktrees and explicit agent-selected merge/integration policy, with a conflict refusal rather than hidden overwrite.
- Feedback into subsequent S1 behaviour: Branch return prompts the parent to merge or reassign work; rejected merge names overlapping files and blocks adoption until a revised child operation.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The shipped worktree/merge subsystem explicitly addresses a concrete inter-worker write collision, including overlap detection and correction feedback.
- Evidence: [delegation worktree option and child return](https://github.com/pmndre/pine/blob/c9dbfd129a8574459e37cfa834662b0fa8ca8a1b/src/tools.ts#L115-L157), [parallel subagents](https://github.com/pmndre/pine/blob/c9dbfd129a8574459e37cfa834662b0fa8ca8a1b/src/tools.ts#L193-L230), [collision intent and isolation](https://github.com/pmndre/pine/blob/c9dbfd129a8574459e37cfa834662b0fa8ca8a1b/src/worktrees.ts#L7-L15), [merge conflict refusal](https://github.com/pmndre/pine/blob/c9dbfd129a8574459e37cfa834662b0fa8ca8a1b/src/worktrees.ts#L289-L323), [owner merge conflict return](https://github.com/pmndre/pine/blob/c9dbfd129a8574459e37cfa834662b0fa8ca8a1b/src/http.ts#L393-L405).
- Basis: structural
- Confidence: medium
- Caveats: Isolation is optional and only source-proven; coordination of arbitrary separate non-code agents is not established. The base merge is not guaranteed to succeed; successful conflict resolution is actor-dependent.

## S3 — Inside-and-now control

- State: P
- Function: Parent/operator current-control oversight of active agents and competing runtime capacity.
- Disturbance / variety regulated: Multiple sessions and workers compete for execution slots and may continue a task that the owner no longer wants.
- Decisive decision or feedback right: View installation-wide tasks, intervene with task cancellation, set agent execution mode and choose global concurrent-run capacity.
- Decision owner: Authenticated installation owner through the bundled API/CLI/TUI.
- Supporting / enforcement mechanisms: Global status and task listing, task cancellation, persisted model/mode limits and concurrency limiter.
- Closure path: A canceled task stops/aborts subsequent execution; owner-selected per-agent mode affects later tool authorization; changed concurrency capacity governs scheduling after restart where documented.
- Boundary reachability: The standard HTTP control API exposes `/status`, `/tasks`, `/agents`, `/tasks/<id>/cancel`, agent mode updates and global `limits.maxConcurrentRuns` configuration.
- Why this is / is not agent-owned: The whole-installation intervention right belongs to the local owner, not the model or deterministic limiter; model-managed delegation is task-local.
- Whole-system current view: The standard `/status`, `/tasks` and `/agents` endpoints expose work across agents rather than only one child's task status.
- Current-control decision scope: Cancel a particular run, change an agent's operating mode, or choose available parallel execution slots.
- Evidence: [global listing](https://github.com/pmndre/pine/blob/c9dbfd129a8574459e37cfa834662b0fa8ca8a1b/src/http.ts#L105-L115), [task stop and agent mode](https://github.com/pmndre/pine/blob/c9dbfd129a8574459e37cfa834662b0fa8ca8a1b/src/http.ts#L255-L270), [cancellation endpoint](https://github.com/pmndre/pine/blob/c9dbfd129a8574459e37cfa834662b0fa8ca8a1b/src/http.ts#L408-L414), [global concurrency parameter](https://github.com/pmndre/pine/blob/c9dbfd129a8574459e37cfa834662b0fa8ca8a1b/src/admin.ts#L519-L536), [runtime scheduling](https://github.com/pmndre/pine/blob/c9dbfd129a8574459e37cfa834662b0fa8ca8a1b/src/agents.ts#L1839-L1865).
- Basis: structural
- Confidence: medium
- Caveats: `maxConcurrentRuns` is a saved-next-start setting, not immediate preemption; no autonomous whole-installation S3 decision is credited. Simple human approvals for individual tool actions are not counted as S3.

## S3* — Complementary audit

- State: —
- Function: A sufficiently independent corrective audit of operational claims, beyond routine checks, was not established in the shipped installation.
- Disturbance / variety regulated: A working agent may incorrectly report completion of a goal or of a delegated task.
- Decisive decision or feedback right: The goal-mode judge issues `MET/CONTINUE/BLOCKED` from the *agent's answer*, not an independent review of changed files or external effects.
- Decision owner: Goal status continuation belongs to judge/runtime; it does not own an independent evidence-based complementary audit.
- Supporting / enforcement mechanisms: Goal judge prompt, runtime status, optional parallel tasks and owner review.
- Closure path: A judge verdict can cause another goal round, but its information source is the producer's own report. No independent raw-evidence audit decision/return loop was identified.
- Why this is / is not agent-owned: A second model call on the producer's answer is not an independent access path to operational reality; a user-created reviewer is not automatically present in the standard distribution.
- Evidence: [judge's exact input](https://github.com/pmndre/pine/blob/c9dbfd129a8574459e37cfa834662b0fa8ca8a1b/src/goals.ts#L45-L93), [judge and continuation](https://github.com/pmndre/pine/blob/c9dbfd129a8574459e37cfa834662b0fa8ca8a1b/src/goals.ts#L296-L310), [generic subagent, not an audit](https://github.com/pmndre/pine/blob/c9dbfd129a8574459e37cfa834662b0fa8ca8a1b/src/tools.ts#L193-L230).
- Basis: structural
- Confidence: medium
- Caveats: An owner can compose a separate reviewer, but this is not first-party installed S3* closure in the declared boundary.

### Absence scope

- Surfaces inspected: Goals/judge logic, owner status API, subagent/delegation tools, installed agent/source documentation and worktree integration.
- Plausible first-party paths checked: Goal judge as independent verifier; ad hoc delegated reviewers; Git conflict checking and manual owner inspection.
- Why no material first-party path remains: The shipped judge observes only the producer's answer and ordinary merge safeguards observe code conflicts, while an independent complementary audit actor with distinct evidence access and returned control is not installed.

## S4 — Outside-and-then intelligence

- State: —
- Function: No shipped prospective environmental-intelligence-to-capability-adaptation loop was established for the PINE installation itself.
- Disturbance / variety regulated: New external event types, model availability and future demands may motivate changing what agents can do.
- Decisive decision or feedback right: Owners can ask the main agent to install sources, routes or agents; no first-party S4 decision loop was found that turns external future-relevant distinctions into options and subsequently changes current capability.
- Decision owner: Owner controls explicit changes to topology and configuration; individual agents respond to subscribed events in their current jobs.
- Supporting / enforcement mechanisms: General-purpose source subscriptions, model/manual lookups, routed events, agent creation and administrator tools.
- Closure path: A source event can wake an agent and an owner-requested configuration change can affect later operations, but the inspected standard flow does not link those steps into a prospective adaptation judgment.
- Why this is / is not agent-owned: Environmental reaction and ordinary runtime self-configuration are not by themselves a demonstrated future-oriented intelligence function.
- Evidence: [source subscription lifecycle](https://github.com/pmndre/pine/blob/c9dbfd129a8574459e37cfa834662b0fa8ca8a1b/src/sources.ts#L16-L31), [router event handling](https://github.com/pmndre/pine/blob/c9dbfd129a8574459e37cfa834662b0fa8ca8a1b/src/router.ts#L79-L143), [agent construction needs owner request/approval](https://github.com/pmndre/pine/blob/c9dbfd129a8574459e37cfa834662b0fa8ca8a1b/src/tools.ts#L1024-L1056), [goal loop is owner-objective continuation](https://github.com/pmndre/pine/blob/c9dbfd129a8574459e37cfa834662b0fa8ca8a1b/src/goals.ts#L1-L44).
- Basis: structural
- Confidence: medium
- Caveats: An operator can build an S4-specific workflow from the primitives; that hypothetical composition is not a shipped positive function.

### Absence scope

- Surfaces inspected: Agent admin, runtime, event router/sources, scheduled and goal-mode execution, model/settings controls and first-party setup documentation.
- Plausible first-party paths checked: Reactive event intake as external sensing; agent/source construction as adaptation; goal continuation as long-horizon planning; owner change of model or agent roles.
- Why no material first-party path remains: These paths wake agents for present tasks or implement explicit operator configuration; none supplies a standard function-specific prospective option-to-current-capability return loop.

## S5 — Policy and identity

- State: P
- Function: Set and revise installation-wide normative identity/behavior rules that govern all agents.
- Disturbance / variety regulated: Divergent agent-specific behaviors and revised owner requirements for the whole installed organization.
- Decisive decision or feedback right: Decide what collective rules, traits and behavioral obligations should hold for every installed agent.
- Decision owner: The installation owner, acting as legitimate parent through explicit instructions or authenticated global-instruction control.
- Supporting / enforcement mechanisms: Shared `AGENTS.md` read into every agent's prompt, exclusive main-agent edit tooling and authenticated owner shared-file API.
- Closure path: Owner supplies an installation-wide policy decision; the main agent/owner writes the global rule file; subsequently agents read that file on their next message, changing their governed behavior.
- Boundary reachability: The installed default main agent is explicitly charged with maintaining shared rules; all agents load shared instruction files and the owner API can edit them without creating a custom plugin.
- Why this is / is not agent-owned: The main agent transcribes/implements owner-decided normative rules, but cannot legitimately substitute its own ultimate policy for the owner's.
- Identity / ultimate-policy issue: Which binding behavioral rules and common agent identity/ethos should apply across all agent cells, not whether to approve a particular tool call.
- Ultimate authority in each claimed mode: Authenticated owner only; no independent autonomous S5 closure claimed.
- Return-to-operation path: Authenticated owner/main-agent shared-file update → saved global `AGENTS.md` → next-session prompt update for every agent → subsequent behavior under revised collective rules.
- Evidence: [global rules and owner write rights](https://github.com/pmndre/pine/blob/c9dbfd129a8574459e37cfa834662b0fa8ca8a1b/docs/references/agents.md#L73-L114), [global instruction incorporation](https://github.com/pmndre/pine/blob/c9dbfd129a8574459e37cfa834662b0fa8ca8a1b/docs/references/agents.md#L121-L137), [authenticated shared-file update](https://github.com/pmndre/pine/blob/c9dbfd129a8574459e37cfa834662b0fa8ca8a1b/src/owner.ts#L340-L350), [main agent's delegated role](https://github.com/pmndre/pine/blob/c9dbfd129a8574459e37cfa834662b0fa8ca8a1b/src/agents.ts#L88-L116).
- Basis: structural
- Confidence: medium
- Caveats: A simple per-tool permission is not S5. Credit is strictly to owner-decided *collective normative policy* changes; no automated S3–S4 strategic settlement or autonomous policy-maker is demonstrated.

## Distributed OSS parent arrangement

The owner of an installed PINE runtime governs its own agents; maintainers of the public PINE repository are not a parent S3/S5 actor of that installation. Repository contributor CI and release practices are outside the operating boundary.

## Self-hosted and non-human modes

A local owner may have one or several agents; S2 applies to the supported concurrent code-worktree mode, not all one-agent deployments. The owner mode for S3 and S5 is installed and distinguishable from agent task discretion. Operator choices and service configuration do not turn the runtime limiter or rule file into independent autonomous governance.

## Recursion

Agents have durable purposes, workspaces and task environments but nesting alone does not establish complete VSM recursion. The chosen installation-level recursion allows several task-performing cells without assuming each is a complete viable system.

## Variety and escalation

Source trust flags and sandbox/approval gates attenuate unsafe external inputs; worktree separation attenuates editing collisions. Agents can request owner intervention when their autonomy is exceeded. Owner goal interruption and request timeouts restrict uncontrolled continuation.

## Evidence gaps

This is a source-based review of the frozen public tree; no installed model, external provider, runtime execution trace or independent S3* audit was run. Positive S2 depends on opt-in worktree behavior; positive S5 concerns explicit installation-wide normative decisions and does not imply an autonomous strategic governance function.

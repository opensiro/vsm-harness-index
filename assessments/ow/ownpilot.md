---
harness_id: ownpilot
project_name: OwnPilot
repository: https://github.com/ownpilot/OwnPilot
review_ref: eb4c27f29d4d12778621a83e49cd673cd8b62239
reviewed_at: 2026-10-24
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# OwnPilot

## Review boundary

- System in focus: OwnPilot's supported self-hosted autonomous Claw parent/child mission mode, with the shipped crew/Soul facilities assessed as adjacent compatible operating surfaces. A plain chat assistant and separately controlled coding-agent CLI are not automatically credited as a multi-agent organization.
- Purpose and identity: Execute a user's bounded or continuing personal/software mission with tool-using autonomous agents, optionally spawning children, enforcing isolation and returning state/outcomes to a parent.
- Relevant environment: Changing user mission conditions, tool/CLI errors, overlapping agent workspaces, parallel agents competing for a shared crew task, provider failures, self-modification risk and cost/permission constraints.
- Standard-distribution boundary: First-party Node/TypeScript gateway/core/UI/CLI, provider adapters, Claw model/tool cycle, ClawManager, `claw_spawn_subclaw`/list/stop tools, per-child sandbox policy, database-backed crew task queue, Soul heartbeat and operator-issued autonomy policy. External model providers supply inference; their own fleet/governance is excluded.
- Credited operating / distribution surfaces: [self-hosted modes](https://github.com/ownpilot/OwnPilot/blob/eb4c27f29d4d12778621a83e49cd673cd8b62239/README.md#L1-L126), [Claw tool-driven parent/child spawning and mandatory child isolation](https://github.com/ownpilot/OwnPilot/blob/eb4c27f29d4d12778621a83e49cd673cd8b62239/packages/gateway/src/tools/claw/delegation-executors.ts#L1-L135), [Claw child state/stop feedback](https://github.com/ownpilot/OwnPilot/blob/eb4c27f29d4d12778621a83e49cd673cd8b62239/packages/gateway/src/tools/claw/delegation-executors.ts#L138-L202), [crew task claim concurrency](https://github.com/ownpilot/OwnPilot/blob/eb4c27f29d4d12778621a83e49cd673cd8b62239/packages/gateway/src/db/repositories/crew/tasks.ts#L120-L157), [Claw runner/manager](https://github.com/ownpilot/OwnPilot/blob/eb4c27f29d4d12778621a83e49cd673cd8b62239/packages/gateway/src/services/claw/runner.ts).
- Adjacent first-party surfaces excluded from ownership: Project CI, codebase audits, benchmark/test fixtures, open-source maintainer/release choices, doc future-work proposals and research-like recommendations. Coding agents launched as independent external CLIs are not credited as their vendors' whole autonomous organizations; a user-defined crew with no operating agent policy is not treated as autonomous S3/S3*.
- First-party operating / deployment modes considered: Self-hosted chat, background Soul heartbeats, four Claw modes (single-shot/continuous/interval/event), subclaw hierarchy with inherited safeguards and Docker isolation; team/crew message, review-request and atomic task-claim facilities; manual/supervised vs higher-autonomy operator policies.
- Recursion level: A parent Claw's delegated work across child Claw S1 units in one user's installed instance. Crew queue is credited only where the same locally owned S1 units compete for crew work; the unrelated user's full provider and external enterprise organization are outside the boundary.
- Reviewed revision: `eb4c27f29d4d12778621a83e49cd673cd8b62239`, frozen in [#2012](https://github.com/opensiro/vsm-harness-index/issues/2012) / [#2013](https://github.com/opensiro/vsm-harness-index/issues/2013).
- Observation date: 2026-10-24.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

OwnPilot has several distinct agent concepts: reactive Personal Assistant, scheduled Soul, mission-cyclic Claw and external coding agent. The gateway runs a model/tool loop, while ClawManager records state and enforces cycles, limits, timeouts and per-call permissions. Crucially, the actual `claw_spawn_subclaw` tool runs **inside the parent Claw context**, creates a separately tracked child with inherited provider/permission configuration, forces a child Docker sandbox, and either awaits a single-shot result or launches a continuing child. The parent can query real child state and stop a selected child. These are first-party shipped paths into an operating model decision, unlike mere agent-name metadata. [agent-mode comparison](https://github.com/ownpilot/OwnPilot/blob/eb4c27f29d4d12778621a83e49cd673cd8b62239/docs/AGENT_ECOSYSTEM.md#L25-L56), [model-backed Claw runner](https://github.com/ownpilot/OwnPilot/blob/eb4c27f29d4d12778621a83e49cd673cd8b62239/packages/gateway/src/services/claw/runner.ts#L365-L405), [delegation tool](https://github.com/ownpilot/OwnPilot/blob/eb4c27f29d4d12778621a83e49cd673cd8b62239/packages/gateway/src/tools/claw/delegation-executors.ts#L18-L135).

The complementary crew system exposes agent-owned task delegation, shared knowledge and review-request messages. The actual database `claimHighestPriority` uses `SELECT … FOR UPDATE SKIP LOCKED` to prevent multiple live workers claiming the same pending task. However `request_review` constructs an ordinary feedback message to a selected peer; no first-party requirement proves a separately independent evaluator's access, authoritative judgment and mandatory return-to-control path. Model-generated reusable skills after completed runs are retrospective skill distillation, not by themselves prospective outside-and-then governance. [crew operations](https://github.com/ownpilot/OwnPilot/blob/eb4c27f29d4d12778621a83e49cd673cd8b62239/packages/gateway/src/tools/crew-tools.ts#L1-L35), [queue](https://github.com/ownpilot/OwnPilot/blob/eb4c27f29d4d12778621a83e49cd673cd8b62239/packages/gateway/src/db/repositories/crew/tasks.ts#L121-L165), [review request](https://github.com/ownpilot/OwnPilot/blob/eb4c27f29d4d12778621a83e49cd673cd8b62239/packages/gateway/src/tools/crew-tools.ts#L608-L675), [skill learning](https://github.com/ownpilot/OwnPilot/blob/eb4c27f29d4d12778621a83e49cd673cd8b62239/packages/gateway/src/services/claw/skill-distiller.ts#L1-L27).

## Operational model

The user configures a mission, model/provider, tools, allowed actions, autonomy policy and execution limits. A Claw's LLM then chooses tool calls from changing observations across its cycle. The same acting Claw may decompose the current mission into child missions, spawn isolated subclaws, inspect their statuses/results and take subsequent steps or stop a child. Separately configured Soul agents in a crew can use the atomic pending-task queue and message each other, but fixed work ordering and coordination messages do not automatically create a central autonomous S3. User autonomy/security policy is a mandate; the presence of an operator does not itself supply a legitimate identity-level S5 return path. [README mode claims](https://github.com/ownpilot/OwnPilot/blob/eb4c27f29d4d12778621a83e49cd673cd8b62239/README.md#L100-L149), [children](https://github.com/ownpilot/OwnPilot/blob/eb4c27f29d4d12778621a83e49cd673cd8b62239/packages/gateway/src/tools/claw/delegation-executors.ts#L18-L202).

## S1 — Operations

- State: A
- Function: Use tools to achieve a bounded mission or continue a configured monitoring/action mission across cycles.
- Disturbance / variety regulated: New data, changing webpages/files, tool failures, provider outputs, user messages and incomplete task results.
- Decisive decision or feedback right: The Claw model chooses tools, further observations, scripts and completion/retry/reflection in response to actual tool results.
- Decision owner: The configured first-party Claw model/tool actor in its supported runtime, using an external inference provider but the packaged Claw execution and feedback integration.
- Supporting / enforcement mechanisms: Tool catalog, runner, cycle manager, `.claw/` directives, persistent context, tool-result history, time/cost limits and sandbox permissions.
- Closure path: Mission → model-chosen tool action → observed tool result → updated session memory/next model choice → report or further cycle.
- Boundary reachability: Claw creation and its model/tool runner are part of the installed first-party gateway, not a user-authored hypothetical plugin or stand-alone coding-agent vendor.
- Why this is / is not agent-owned: The runtime schedules and enforces configured bounds but cannot replace the model's mission-specific action decisions.
- Evidence: [Claw modes and tool list](https://github.com/ownpilot/OwnPilot/blob/eb4c27f29d4d12778621a83e49cd673cd8b62239/README.md#L111-L147), [Claw runner](https://github.com/ownpilot/OwnPilot/blob/eb4c27f29d4d12778621a83e49cd673cd8b62239/packages/gateway/src/services/claw/runner.ts), [subclaw task result](https://github.com/ownpilot/OwnPilot/blob/eb4c27f29d4d12778621a83e49cd673cd8b62239/packages/gateway/src/tools/claw/delegation-executors.ts#L94-L133).
- Basis: Shipped model-directed agent operation with an actual tool/observation loop.
- Confidence: High for source wiring, not measured mission success.
- Caveats: No live agent/model-provider execution or autonomous effectiveness study is claimed.

## S2 — Coordination

- State: C
- Function: Prevent concurrent subordinate operational cells from corrupting one another's workspace or claiming the same pending crew task.
- Disturbance / variety regulated: Parent/child file-state contamination and two active worker agents racing to own one queue task.
- Decisive decision or feedback right: First-party subclaw spawning **forces child Docker isolation**, preventing child writes to its parent's workspace; atomic crew claim returns exactly one owner and makes other competing agents reselect another task. Policy/queue constraints are configured/enforced by code, not chosen by an S2 manager agent.
- Decision owner: The user/parent config supplies the boundary and task source, while first-party S2-specific isolation and claim gates enforce anti-interference; autonomous organizational coordination discretion beyond those paths is not established.
- Supporting / enforcement mechanisms: Child-created `docker` sandbox, inherited policy, task queue `SKIP LOCKED`, `claimed_by` ownership, typed result/claim status and sibling messaging tools.
- Closure path: Multiple active S1 units contend for shared filesystem or pending work → forced sandbox/transaction isolates outcomes → another agent receives an unsuccessful claim or separate workspace and must use its own next operational action.
- Boundary reachability: Child isolation is *mandatory* in the packaged Claw spawn tool and queue claiming is an exported first-party crew execution tool, both reachable in supported modes without writing anti-contention logic.
- Why this is / is not agent-owned: The S2 function is concretely anti-interference, not generic routing; `C` records intentionally exposed first-party mechanism without autonomous ownership of an S2-specific discretionary coordination choice.
- Distinct S1 units: Parent Claw and its independently executing child Claws, or two separately configured Soul crew workers.
- Inter-S1 disturbance: A child contaminates shared parent mission state through file writes; two workers concurrently claim the same piece of pending crew work.
- Attenuating coordination relation: Forced subclaw Docker sandbox independent from parent's workspace plus a single-winner crew claim transaction.
- Feedback into subsequent S1 behaviour: Conflicting task claims return no task to the losing agent and the parent can inspect child state; isolated child actions cannot overwrite the parent workspace.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The implementation explicitly documents prevention of **parent-workspace corruption**, and a lock-enforced no-double-claim invariant directly regulates cross-agent competition, unlike task order or messages alone.
- Evidence: [mandatory isolation purpose and code](https://github.com/ownpilot/OwnPilot/blob/eb4c27f29d4d12778621a83e49cd673cd8b62239/packages/gateway/src/tools/claw/delegation-executors.ts#L56-L83), [atomic task claim](https://github.com/ownpilot/OwnPilot/blob/eb4c27f29d4d12778621a83e49cd673cd8b62239/packages/gateway/src/db/repositories/crew/tasks.ts#L128-L161), [exposed claim tool](https://github.com/ownpilot/OwnPilot/blob/eb4c27f29d4d12778621a83e49cd673cd8b62239/packages/gateway/src/tools/crew-tools.ts#L99-L122).
- Basis: Narrow first-party mechanism specifically resolves structurally evidenced inter-agent interference, but deterministic gates do not give autonomous S2 discretion.
- Confidence: Medium-high; isolated and queue modes have different deployment preconditions.
- Caveats: Docker availability matters for subclaws; do not infer broad conflict-free team programming from this bounded witness.

## S3 — Inside-and-now control

- State: A
- Function: Decide current resource/commitment allocation among child agents executing one parent Claw's active mission.
- Disturbance / variety regulated: Changing subtask requirements, unfinished children, failed tool runs, wasted effort or no longer relevant subordinate work.
- Decisive decision or feedback right: The parent model-backed Claw chooses whether/which child missions to create, which mission configuration to pass, inspects child live status and results, and chooses when to stop or redirect its current child work.
- Decision owner: The active parent Claw agent, not a queue, fixed cron heartbeat or mere user CRUD dashboard.
- Supporting / enforcement mechanisms: Spawn/list/stop executors, actual ClawManager, `parentClawId`, inherited tool permissions, child state/results, durable session context and tool-observation feedback.
- Closure path: Parent mission and currently running child status/results → model decisions to spawn additional specialized work, stop a child or proceed itself → first-party manager changes subordinate execution → resulting status returns to parent on next tool observation.
- Boundary reachability: The active runner includes parent-to-child tools, and their handlers require the authentic Claw execution context and instantiate/start/manage children; this is not a user-created coordinator in another repo.
- Why this is / is not agent-owned: Deciding which concurrent work to commit to a child, and changing it after status feedback, is current multi-unit control. Permission and depth guards enforce constraints but are not the owner of the parent's portfolio choice.
- Whole-system current view: The current parent Claw mission, its own plan/history and live states of all `getChildClaws(parentId)` children, with result/status from completed child calls.
- Current-control decision scope: Composition, addition, stop/replacement and outcome integration of the **same parent mission's** children; no claim of control over every independent Soul/crew in the OwnPilot installation.
- Evidence: [parent tool interface](https://github.com/ownpilot/OwnPilot/blob/eb4c27f29d4d12778621a83e49cd673cd8b62239/packages/gateway/src/tools/claw/definitions.ts#L90-L127), [create/start and outcome feedback](https://github.com/ownpilot/OwnPilot/blob/eb4c27f29d4d12778621a83e49cd673cd8b62239/packages/gateway/src/tools/claw/delegation-executors.ts#L18-L135), [complete child inventory and stop](https://github.com/ownpilot/OwnPilot/blob/eb4c27f29d4d12778621a83e49cd673cd8b62239/packages/gateway/src/tools/claw/delegation-executors.ts#L137-L202).
- Basis: Standard agent-owned current allocation across its subordinate S1 missions; parent discretion is separate from deterministic scheduler/policy.
- Confidence: Medium-high for code path, no measurement of model ability to choose useful interventions.
- Caveats: Optional subclaw spawning is not automatically exercised by every Claw run. No `(P)` inferred from merely managing cards or user permission toggles.

## S3* — Complementary audit

- State: —
- Function: No sufficiently independent complementary auditor with a closed finding → parent-current-control return is supplied by the standard parent/child Claw hierarchy.
- Disturbance / variety regulated: Parent/child claims may be wrong and tools may fail, but ordinary progress metrics, logs and optional peer requests do not by themselves establish an independent auditor.
- Decisive decision or feedback right: No guaranteed independently judging agent with contradictory authority and separate access in the credited Claw mode. `request_review` sends a message to a user-selected peer, not an autonomous trusted veto.
- Decision owner: The acting Claw itself, optional user-configured peer, or human reader of metrics; no identified first-party S3* holder with independent closure.
- Supporting / enforcement mechanisms: `claw_history`, deterministic run reliability metrics, generic crew `request_review`, activity/audit logs and tool-call security guard.
- Closure path: Ordinary logs/feedback can inform next work, but there is no default independent claim checking and returned corrective decision into parent allocation from a distinct auditor.
- Why this is / is not agent-owned: A review message or a self-run reliability score does not independently audit organizational reporting.
- Evidence: [review request is peer message](https://github.com/ownpilot/OwnPilot/blob/eb4c27f29d4d12778621a83e49cd673cd8b62239/packages/gateway/src/tools/crew-tools.ts#L608-L675), [deterministic run evaluation](https://github.com/ownpilot/OwnPilot/blob/eb4c27f29d4d12778621a83e49cd673cd8b62239/packages/gateway/src/services/claw/run-eval.ts#L1-L28).
- Basis: Bounded negative first-party Claw recursion, without borrowing user-configured independent reviewers.
- Confidence: Medium.
- Caveats: Some crews can include a reviewer-role agent; their actual independence and feedback closure must be assessed in a separately pinned configuration.

### Absence scope

- Surfaces inspected: Claw spawn/child monitoring, crew review-request tool, task/result submission, run-eval, audit history and policy gateway.
- Plausible first-party paths checked: Generic `request_review`, model self-reflection, tool-call success statistics, independent coding-agent commands and logged tool actions.
- Why no material first-party path remains: These are optional messaging, ordinary operator observability or self-report. The installed hierarchical mode does not require a distinct contrary auditor with evidence access and binding return to current parent control.

## S4 — Outside-and-then intelligence

- State: —
- Function: No demonstrated first-party closed process links externally sensed prospective changes to adoption of new future organizational capabilities for the parent/child mission system.
- Disturbance / variety regulated: Changing external AI tools, markets and user environments could require future capabilities; current mission adaptation and learned task recipes only handle known-run history.
- Decisive decision or feedback right: No distinct whole-system prospective adaptation owner/return established; users choose extensions, models, identity settings and future missions.
- Decision owner: First-party Claw agent may refine its current plan and auto-distill a prior completed task into a skill, but this is not shown to own outside-and-then strategic adaptation.
- Supporting / enforcement mechanisms: Claw reflection, learned skill distillation and lookup, dynamic tool catalog, extensible service and provider discovery.
- Closure path: Past task trajectory → model-produced reusable skill → extension installation → future retrieval is operational learning; missing external/future distinction and intentional prospective options/choice for parent capability.
- Why this is / is not agent-owned: Replaying skill learned from one's own task is not equivalent to sensing future environmental challenges and directing sustained capability adaptation.
- Evidence: [skill distiller](https://github.com/ownpilot/OwnPilot/blob/eb4c27f29d4d12778621a83e49cd673cd8b62239/packages/gateway/src/services/claw/skill-distiller.ts#L1-L28), [distiller actual installation](https://github.com/ownpilot/OwnPilot/blob/eb4c27f29d4d12778621a83e49cd673cd8b62239/packages/gateway/src/services/claw/skill-distiller.ts#L151-L187), [autonomy modes](https://github.com/ownpilot/OwnPilot/blob/eb4c27f29d4d12778621a83e49cd673cd8b62239/docs/AUTONOMOUS_AGENTS.md#L17-L52).
- Basis: Bounded absence of external/prospective organizational adaptation closure.
- Confidence: Medium.
- Caveats: Specific self-configured market-research Soul roles could sense the outside, but a feed-to-adoption path is not established at this reviewed hierarchy.

### Absence scope

- Surfaces inspected: Claw reflection, skill distiller, Soul evolution fields, user extension installation, agent creator and adaptive scheduling.
- Plausible first-party paths checked: Learned reusable skills after successful runs, automated tool discovery, self-modification toggles, research Soul templates and changing provider routing.
- Why no material first-party path remains: The examined mechanisms use local operational outcomes or operator configuration; none demonstrates an outside/future intelligence judgment producing adopted strategic capability adjustments at the assessed multi-unit recursion.

## S5 — Policy and identity

- State: —
- Function: No established first-party settlement of ultimate organizational identity or governing-policy disputes into the parent/child multi-agent operation.
- Disturbance / variety regulated: Risks around self-modification, destructive actions, forbidden tools, overspending and mission scope require constraints but are predominantly ordinary operating policy, not ultimate identity-level governance.
- Decisive decision or feedback right: Operator configures autonomy policies and tool permissions; no identified first-party identity/policy dispute → legitimate ultimate authority → returned binding decision path.
- Decision owner: User for initial identity, mission and safeguards; deterministic permission gate for action allow/deny; the model cannot independently rewrite ultimate mandate under a proven S5 authority mode.
- Supporting / enforcement mechanisms: Autonomy policies, budget limits, immutable Soul core traits and delegated permission gates, optional user approvals, file scopes and allowSubclaws.
- Closure path: A forbidden tool is denied or ordinary permission requested, but the system does not turn an ultimate charter/policy disagreement into a resolved organizational rule applied prospectively.
- Why this is / is not agent-owned: Hard permissions and user-defined identity fields, absent a conflict/legitimacy path, do not constitute S5 merely by being configurable.
- Evidence: [tool permissions](https://github.com/ownpilot/OwnPilot/blob/eb4c27f29d4d12778621a83e49cd673cd8b62239/packages/gateway/src/services/permission/gate.ts#L242-L327), [core Soul identity/evolution config](https://github.com/ownpilot/OwnPilot/blob/eb4c27f29d4d12778621a83e49cd673cd8b62239/docs/AUTONOMOUS_AGENTS.md#L32-L153).
- Basis: Bounded absence of identity/ultimate-policy return loop.
- Confidence: Medium-high.
- Caveats: A local operator legitimately defines the assistant's identity; Methodology S5=P requires a stronger complete governance loop than simple configuration or per-action approval.

### Absence scope

- Surfaces inspected: Soul identity, core/mutable traits, agent creation, approval queue, execution permission gate, parent subclaw inheritance and operator settings.
- Plausible first-party paths checked: `allowSelfModify`, `allowSubclaws`, mission config changes, human approvals, budgets and cross-user message restrictions.
- Why no material first-party path remains: Each is a static/operator action policy or task permission path. None supports a documented ultimate identity dispute, legitimate adjudication, and authoritative governance return across subsequent multi-unit operations.

## Distributed OSS parent arrangement

OwnPilot is self-hosted by independent users; the repository's maintainers and outside model vendors are not the legitimate parent governor of a given active instance. Enterprise or operator oversight could exist independently, but code review, releases and personal model settings are not imported to assert S3/S4/S5 parent modes at the selected hierarchy.

## Self-hosted and non-human modes

Built-in Claw cycles and subclaw tools can run self-hosted with configured external model/local provider. The positive states are conditioned on an actually configured agent runtime and, for S2 child isolation, working Docker. Human-created crew templates and Soul configurations are optional organization patterns; they do not silently create independent audit or policy governance. The parent Claw's current-control decisions remain model-owned within operator-set permissions.

## Recursion

The parent Claw's children are S1 operational cells; first-party mechanisms constrain cross-cell workspace and claim interference; the parent Claw owns current child allocation. An ordinary peer reviewer and a tool-call log are not recursively established as S3*; future-facing templates and policy fields do not establish S4/S5.

## Variety and escalation

Task/tool uncertainty stays with the Claw S1, contested resource access gets forced workspace/queue isolation, and child portfolio questions return to the parent Claw S3. Per-action permission violations escalate to operator approval/denial as ordinary operation. No independent audit or prospective capability/ultimate identity governance closure is claimed.

## Evidence gaps

- No live model, provider, Claw or crew-run effectiveness tests. Source and deterministic test files demonstrate shipped interfaces and guards, not decision quality.
- S2 positive is limited to mandatory child isolation and the crew's competing-task claim transaction; it does not imply comprehensive prevention of file conflicts among arbitrary unrelated workspaces.
- The exact cross-product composition of Soul crew workers versus nested Claws may vary by user configuration. The S3 decision witness specifically belongs to one parent Claw with child missions, not a globally autonomous operator over all OwnPilot features.
- Separate human/model peer review can be configured, but no first-party mandatory complementary auditor or standing binding return-to-control mechanism is established in the reviewed mode.

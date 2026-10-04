---
harness_id: dodo
project_name: Dodo
repository: https://github.com/jonnyparris/dodo
review_ref: 156d60ca2f743ad4177b0ed781e61ecbd1af508f
reviewed_at: 2026-10-05
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-05
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Dodo

## Review boundary

- System in focus: Dodo's first-party Cloudflare-hosted coding-agent service at frozen revision `156d60ca2f743ad4177b0ed781e61ecbd1af508f`, including CodingAgent sessions, task/facet execution, goal-driven continuation, scheduling, task board and shipped autopilot supervisor/worker mode.
- Purpose and identity: provide autonomous repository coding sessions that can be dispatched manually, in parallel, on schedules or under goals, with a first-party self-diagnose supervisor mode for current service failures.
- Relevant environment: user goals/prompts, cloned repositories and workspaces, model/tool results, task/session state, Cloudflare Worker logs, failed/stalled sessions, scheduled jobs, existing autopilot workers and external Git/GitHub delivery.
- Standard-distribution boundary: Worker, Durable Objects, UserControl/SharedIndex/CodingAgent, first-party agentic loop, facets, task board, scheduling, memory/skills/browser tools, MCP and autopilot surfaces are inside. LLM gateways, GitHub/GitLab, ntfy and Cloudflare platform services are dependencies. Human PR review/merge and repository-development CI are external/parent governance and do not donate runtime S3*.
- Credited operating / distribution surfaces: ordinary coding sessions, goal-driven sessions, scheduled sessions, parallel batch dispatch, facet subagents, and the documented installable scheduled autopilot supervisor with worker dispatch.
- Adjacent first-party surfaces excluded from ownership: repository-development checks and maintainer review except where the shipped runtime explicitly invokes them as external delivery; roadmap/future features not present at the frozen ref.
- First-party operating / deployment modes considered: web/UI sessions; MCP; cron/scheduled prompts; goal-driven sessions; task-board batch dispatch; configured facet mode; installed autopilot supervisor.
- Recursion level: ordinary coding sessions and autopilot worker sessions are S1 operations at their respective supported service mode; the autopilot supervisor is evaluated as a metasystemic controller over current maintenance-worker activity and live failure signals.
- Reviewed revision: `156d60ca2f743ad4177b0ed781e61ecbd1af508f`.
- Observation date: 2026-10-05.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Dodo runs its own model/tool coding loop in per-session Durable Objects with isolated workspaces, Git, browser and code-execution tools. Sessions can continue autonomously under goals, be scheduled, be dispatched from a task board, and spawn bounded explore/task facets. Parallel facets may use scratch workspaces whose writes remain isolated until the parent explicitly applies selected paths.

The shipped autopilot mode adds a distinct current-control loop. A scheduled supervisor session reads a cross-section of recent Worker exceptions, client-side errors and stalled scheduled sessions; reads prior autopilot-worker state; decides whether a concrete non-duplicate issue merits investigation; and dispatches up to three fresh goal-driven worker sessions. Workers investigate, test and open draft PRs. Later supervisor runs observe worker status and suppress duplicate/in-flight or repeated-failure dispatches. This is a first-party agent-owned current regulation loop even though human review remains required before a code change is merged.

Primary evidence:

- [README.md](https://github.com/jonnyparris/dodo/blob/156d60ca2f743ad4177b0ed781e61ecbd1af508f/README.md)
- [session goals](https://github.com/jonnyparris/dodo/blob/156d60ca2f743ad4177b0ed781e61ecbd1af508f/docs/session-goals.md)
- [facets](https://github.com/jonnyparris/dodo/blob/156d60ca2f743ad4177b0ed781e61ecbd1af508f/docs/facets.md)
- [autopilot supervisor/worker prompts](https://github.com/jonnyparris/dodo/blob/156d60ca2f743ad4177b0ed781e61ecbd1af508f/src/autopilot.ts)
- [autopilot MCP tools](https://github.com/jonnyparris/dodo/blob/156d60ca2f743ad4177b0ed781e61ecbd1af508f/src/mcp.ts)
- [autopilot/task routes](https://github.com/jonnyparris/dodo/blob/156d60ca2f743ad4177b0ed781e61ecbd1af508f/src/index.ts)

## Operational model

A Dodo coding session receives a task/goal, selects tools, observes real repository/browser/execution results and iterates until it finishes, blocks, needs input or exhausts its budget. Goal-driven sessions auto-continue without a human nudge. The task board and scheduler can create several such operations.

In autopilot mode, a scheduled supervisor is itself a model-backed decision actor. It uses installation-wide failure evidence and worker-state evidence to allocate current investigative work, prevent duplicate investigations and escalate repeated stuck patterns. That is distinct from ordinary coding S1.

## S1 — Operations

- State: A
- Function: carry out repository-oriented coding, investigation and delivery work through first-party model/tool sessions.
- Disturbance / variety regulated: heterogeneous codebases, tool outcomes, browser/repository evidence, task goals, context pressure, repeated tool loops, test failures, scheduled execution and human-input blockers.
- Decisive decision or feedback right: choose the next tool/action, interpret results, continue across turns under a goal, and decide when the requested operational outcome is done/blocked/needs input.
- Decision owner: the model-backed CodingAgent or goal-driven autopilot worker.
- Supporting / enforcement mechanisms: Durable Object session, workspace isolation, Git/browser/code tools, doom-loop guard, token budget, compaction, scheduler, goal state and `set_goal_status`.
- Closure path: task/goal + context → model selects action → tool/environment returns evidence → model revises work → goal/session terminal or continued turn.
- Boundary reachability: ordinary UI/MCP sessions and goal-driven/scheduled modes are shipped first-party paths at the pinned revision.
- Why this is / is not agent-owned: removing the model actor leaves storage/scheduling/guardrails but removes open-ended coding and investigation decisions.
- Evidence: README; `docs/session-goals.md`; CodingAgent/agentic runtime.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: Git hosting and model inference are dependencies, not decision owners.

## S2 — Coordination

- State: —
- Function: no qualifying same-recursion peer-S1 disturbance/coordination loop was established.
- Disturbance / variety regulated: batch-dispatched sessions have separate workspaces; facets can run concurrently and task facets can use scratch prefixes; supervisor deduplication allocates work from above.
- Decisive decision or feedback right: no distinct S2 mutual-adjustment decision among peer operational units is established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: per-session workspace isolation, scratch workspaces, task/facet naming, batch-dispatch caps and supervisor duplicate suppression.
- Closure path: isolation prevents state collision, but no concrete peer disturbance is sensed and resolved through a coordination relation that changes both/peer S1 behavior.
- Why this is / is not agent-owned: the strongest concurrency mechanisms are partitioning/delegation or S3 allocation, not a separate S2 decision right.
- Evidence: README task-board/facet sections; `docs/facets.md`; task dispatch routes.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: if a future first-party flow explicitly reconciles competing session changes against one shared delivery surface, this finding could change.

### Absence scope

- Surfaces inspected: batch task dispatch, parallel facets, scratch/apply flow, session workspaces, task board and autopilot worker deduplication.
- Plausible first-party paths checked: workspace isolation as S2; scratch merge as S2; task-board parallelism as S2; supervisor duplicate suppression as S2.
- Why no material first-party path remains: parallel units are isolated or centrally allocated; no distinct same-recursion conflict/oscillation → coordination response → peer behavior closure is evidenced.

## S3 — Inside-and-now control

- State: A
- Function: regulate current Dodo maintenance activity in the shipped autopilot mode by deciding which live/recent failures merit investigation and allocating bounded worker sessions.
- Disturbance / variety regulated: Worker exceptions, client-error groups, stalled scheduled sessions, duplicate/in-flight investigations, repeated failure patterns and bounded worker capacity.
- Decisive decision or feedback right: decide whether there is a concrete actionable issue, which issue(s) to investigate now, whether an issue is already covered, and whether to dispatch up to three worker sessions or pause/escalate a repeated pattern.
- Decision owner: the model-backed scheduled autopilot supervisor session.
- Supporting / enforcement mechanisms: `list_failed_sessions`, `list_autopilot_workers`, `dispatch_autopilot_worker`, cron scheduling, worker goal state, max-three rule and ntfy notification.
- Closure path: cross-section failure evidence + prior worker state → supervisor judgment → new goal-driven worker dispatch or no-dispatch/pause → workers update status/open draft PRs → later supervisor run reads worker/failure state and adjusts subsequent dispatch.
- Boundary reachability: README documents installation of the scheduled supervisor; `src/index.ts` exposes the supervisor schedule; `src/mcp.ts` ships the exact control tools; `src/autopilot.ts` supplies the model-owned decision procedure.
- Why this is / is not agent-owned: removing the supervisor model while leaving logs, cron and dispatch endpoints intact removes the judgment that selects actionable issues, deduplicates them semantically and chooses current worker allocation.
- Evidence: README Autopilot; `src/autopilot.ts`; `src/mcp.ts`; supervisor routes.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: human review/merge remains downstream authority over code admission; S3 credit is for autonomous current investigation allocation/control, not autonomous deployment.

## S3* — Complementary audit

- State: —
- Function: no qualifying independent audit loop over an S1 claim was established inside the deployed Dodo boundary.
- Disturbance / variety regulated: workers run focused tests and open draft PRs, and humans review those PRs; ordinary coding sessions may perform PR-review tasks.
- Decisive decision or feedback right: no first-party independent auditor owns a complementary verdict over another Dodo producer and closes correction/re-review.
- Decision owner: not established.
- Supporting / enforcement mechanisms: tests, Git diffs/PRs, human review requirement, optional review prompts.
- Closure path: worker findings reach a draft PR/human; the human/repository-development path is external parent governance rather than first-party S3*.
- Why this is / is not agent-owned: an operational agent can perform “review” as its assigned S1 task, but no distinct autonomous auditor relationship is wired into standard runtime delivery.
- Evidence: README Autopilot; `docs/session-goals.md`; repository review statements.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: human review is real assurance but cannot be published as S3* under this boundary.

- Claim being audited: no first-party producer/auditor pair with mandatory corrective closure established.
- Ordinary reporting path: session result, tests, Git branch/draft PR.
- Complementary access path: external human/repository review.
- Independence boundary: maintainer/CI review is adjacent to the deployed service.
- Who acts on findings: human maintainer or ordinary coding session.

### Absence scope

- Surfaces inspected: tests, draft PR delivery, PR-review goal examples, autopilot workers, facets and human-review rule.
- Plausible first-party paths checked: tests as S3*; PR-review tasks as S3*; human draft-PR review as S3*; explore facet as reviewer.
- Why no material first-party path remains: tests are ordinary S1 feedback, review is optional operational work, and the mandatory independent acceptance authority is external.

## S4 — Intelligence / adaptation

- State: —
- Function: no externally and prospectively oriented adaptation loop was established.
- Disturbance / variety regulated: browser research, persistent memory and autopilot log investigation help current tasks/current failures.
- Decisive decision or feedback right: no first-party path models future/external change, develops adaptation options and returns a selected option into present whole-system capability.
- Decision owner: not established at S4 level.
- Supporting / enforcement mechanisms: browser/CDP tools, memory, skills, model routing and current-failure autopilot.
- Closure path: external/current evidence can shape the active coding task, but no prospective strategic adaptation loop is shown.
- Why this is / is not agent-owned: current-task web research and current-error repair are not the Profile's outside-and-then function.
- Evidence: README Browser/Memory/Autopilot sections.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: self-repair can change future code after human merge, but its trigger/judgment is current failure remediation rather than external/prospective intelligence.

### Absence scope

- Surfaces inspected: browser research, memory, skills, model selection, self-diagnose supervisor.
- Plausible first-party paths checked: browsing as S4; memory as S4; autopilot self-improvement as S4.
- Why no material first-party path remains: all inspected paths center on the present task or present operational failures.

## S5 — Policy and identity

- State: —
- Function: no identity/ultimate-policy closure was established.
- Disturbance / variety regulated: admin allowlists, sharing permissions, secrets, model config, goal rules and autopilot hard rules constrain operation.
- Decisive decision or feedback right: no identity-level issue is routed to legitimate ultimate authority and returned as durable system-governing policy through a first-party closure loop.
- Decision owner: not established at S5 level.
- Supporting / enforcement mechanisms: SharedIndex/UserControl permissions, admin guards, configuration, static prompts and tool permissions.
- Closure path: constraints apply directly to operations, but no S5 issue/authority/return cycle is evidenced.
- Why this is / is not agent-owned: security/permission settings and hard-coded supervisor rules bound autonomy without constituting identity governance.
- Evidence: README architecture/security sections; MCP/admin surfaces.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: deployment owners retain ultimate authority outside Dodo.

### Absence scope

- Surfaces inspected: SharedIndex/UserControl permissions, admin controls, configuration, skills/memory policy and autopilot hard rules.
- Plausible first-party paths checked: admin role as S5; permissions as S5; autopilot rules as identity policy.
- Why no material first-party path remains: these are operational access/safety constraints, not identity/ultimate-policy closure.

## Recursion

Ordinary Dodo coding sessions are autonomous operational units. In the optional autopilot mode, goal-driven maintenance workers form an operational set supervised by the scheduled autopilot model. Facets remain subordinate bounded helpers and are not credited as recursive viable systems.

## Variety and escalation

Dodo absorbs variety through model/tool iteration, goal continuation, scheduling, isolation, compaction, loop guards and worker fan-out. Current service-health variety can escalate into the autopilot supervisor; ambiguous or repeated patterns can escalate to a human notification, while code merge remains human-controlled.

## Evidence gaps

No `?` state is required. The frozen source explicitly documents both the ordinary operational loop and the shipped autopilot supervisor path.

## Assessment summary

Dodo closes autonomous S1 through first-party durable coding sessions and autonomous S3 in its shipped scheduled autopilot mode, where a model-backed supervisor consumes cross-service failure evidence and worker state to decide current investigation allocation. Parallel sessions/facets remain isolation/delegation rather than S2, tests/human PR review do not establish first-party S3*, and browser/memory/security surfaces do not close S4 or S5.

**Vector:** A · — · A · — · — · —

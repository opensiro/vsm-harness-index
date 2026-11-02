---
harness_id: recurse
project_name: Recurse
repository: https://github.com/ebetica/recurse
review_ref: 6e4d231e299a14f19fe6eee9d9f7f43781780c2a
reviewed_at: 2026-11-02
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Recurse

## Review boundary

- System in focus: the shipped self-hosted Recurse web/Pi Durable coding-agent organization: a parent model-led conversation and its locally spawned, independently operating child agents, using optional managed Git worktrees and the native tree-control CLI.
- Purpose and identity: carry out long-horizon coding and repository work with durable tool-using agents, background processes and monitors, delegable independent work, a visible tree, and reviewable results.
- Relevant environment: mutable source repositories, concurrent editing, process completion, changing tool/test output, model/provider failures, overlapping child work, operator intervention, and uncertainty about completed subtasks.
- Standard-distribution boundary: supported Bun `recurse` server and web app, Pi Durable conversations and tools, shipped `subagent.ts`/`worktree.ts`, model-backed parent and children, and built-in safety extension. Providers, Git, the OS/container, and remote CI platforms supply external services, not autonomous first-party owners.
- Credited operating / distribution surfaces: `docs/{guide,examples}.md`, `src/agents/{README.md,agent_tree.ts,supervisor/,runtime/,durable/}`, `src/agents/runtime/prompts.ts`, `tools/{subagent.ts,worktree.ts}`, and `src/extensions/core/safety/`.
- Adjacent first-party surfaces excluded from ownership: Recurse's own contributor `docs/agents/` PR-review governance, development tests/fixtures and CI, manually authored application-specific skills, sample graphs not installed as an active workflow, third-party provider governance, and external Git hosting merge policy.
- First-party operating / deployment modes considered: ordinary single root agent, supported parent/child parallel execution with named worktrees and tree digest, operator takeover/interrupt, scriptable but not preinstalled agent graphs, model safety review, and optional external-event monitors. The positive S2/S3 findings concern the documented multi-agent operation, not every single-agent run.
- Recursion level: one local coding-delivery tree with multiple task-owning child S1 work cells and a coordinating parent; a single model session or separately hosted backend is not automatically another full organization.
- Reviewed revision: `ebetica/recurse@6e4d231e299a14f19fe6eee9d9f7f43781780c2a`, GitHub repository ID 1435307881, frozen intake #2578 / serial controller #2579.
- Observation date: 2026-11-02.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The [guide](https://github.com/ebetica/recurse/blob/6e4d231e299a14f19fe6eee9d9f7f43781780c2a/docs/guide.md) describes each conversation as an agent with its own model, working directory and history. `AgentNode` owns one agent's messages and local controls, a [`DurableHost`](https://github.com/ebetica/recurse/blob/6e4d231e299a14f19fe6eee9d9f7f43781780c2a/src/agents/durable/README.md) runs the model/tool turns, and the [`Supervisor`](https://github.com/ebetica/recurse/blob/6e4d231e299a14f19fe6eee9d9f7f43781780c2a/src/agents/README.md) owns the tree/lifecycle. Child agents receive distinct tasks and run independently, including after the browser closes. Tool results, agent messages, background-shell completions and child final reports return to the appropriate model turn.

For parallel editing, the documented supported `subagent create --worktree` interface creates an agent-held checkout; [`tools/worktree.ts`](https://github.com/ebetica/recurse/blob/6e4d231e299a14f19fe6eee9d9f7f43781780c2a/tools/worktree.ts) manages checkout creation, holder claims and deferred safe retirement. [The guide's worktree workflow](https://github.com/ebetica/recurse/blob/6e4d231e299a14f19fe6eee9d9f7f43781780c2a/docs/guide.md) explicitly addresses concurrent agents editing the same files, recommends isolated child checkouts and hands branch/PR integration to the parent or operator. [`subagent.ts`](https://github.com/ebetica/recurse/blob/6e4d231e299a14f19fe6eee9d9f7f43781780c2a/tools/subagent.ts) also exposes send/interrupt, wait, move, removal and selective effort for active children. The [`runtime prompt tree digest`](https://github.com/ebetica/recurse/blob/6e4d231e299a14f19fe6eee9d9f7f43781780c2a/src/agents/runtime/prompts.ts) exposes child status, queue and descendant count to the parent at request boundaries.

Model [safety review](https://github.com/ebetica/recurse/blob/6e4d231e299a14f19fe6eee9d9f7f43781780c2a/src/extensions/core/safety/README.md) separately reviews planned `bash`/`write`/`edit` calls against operator intent and static risk policy; it excludes tool-result content and does not inspect the actual produced artifact. Shipped [example graphs](https://github.com/ebetica/recurse/blob/6e4d231e299a14f19fe6eee9d9f7f43781780c2a/docs/examples.md) describe how users may script a planner/implementers/reviewer chain, but the reviewer script is a recipe, not a running standard-distribution audit process.

## Operational model

An operator points Recurse at a repository and asks the root agent for an outcome. It can run tools, continue on background notifications, inspect current child status and progress, create independent child task owners with separate worktrees, and act on their results. Child agents independently decide how to implement their tasks; their reports and branches inform the parent. The agent can change allocation, interrupt/redirect a running child or spawn a correction. Normal safety review limits some planned tool actions but does not independently check post-execution success.

## S1 — Operations

- State: A
- Function: produce code/repository outcomes through independently model-directed persistent work on a task, including observation, edits, tests, terminal commands and iteration.
- Disturbance / variety regulated: changing code state, command/test failures, incomplete context, long-running commands and interruptions/restarts.
- Decisive decision or feedback right: each agent chooses its subsequent tools, edits, tests, recovery, further child tasks or final result from observed feedback.
- Decision owner: the Pi Durable model actor in each root/child conversation, subject to external operator authorization and safety-tool constraints.
- Supporting / enforcement mechanisms: per-agent `AgentNode`, Durable Harness, background shell/wait/monitor, persisted messages, working-directory state and safety checks.
- Closure path: operator/parent task → model-selected tools/edits → shell/file/agent observations and completion wakes → subsequent model decision and result report; durable work can resume across browser disconnection and restart.
- Boundary reachability: normal `recurse /path` starts a real agent; documented `subagent create` starts more independent model agents from CLI without a special development fixture.
- Why this is / is not agent-owned: model turns choose task-level actions and responses; deterministic process supervision only transports results and gates execution.
- Evidence: [quickstart and purpose](https://github.com/ebetica/recurse/blob/6e4d231e299a14f19fe6eee9d9f7f43781780c2a/README.md), [runtime guide](https://github.com/ebetica/recurse/blob/6e4d231e299a14f19fe6eee9d9f7f43781780c2a/docs/guide.md), [Durable turns](https://github.com/ebetica/recurse/blob/6e4d231e299a14f19fe6eee9d9f7f43781780c2a/src/agents/durable/README.md).
- Basis: structural
- Confidence: high
- Caveats: no live provider-authenticated long-horizon turn was executed for this assessment; source and bundled documentation establish the operating path.

## S2 — Coordination

- State: A
- Distinct S1 units: two or more independently running implementer child agents with separate model turns, local tasks and repository-editing decisions, under one parent tree.
- Inter-S1 disturbance: simultaneous implementation in one checkout can overwrite, interleave or destabilize another child's in-progress file changes; the official guide explicitly motivates separate worktrees to prevent this shared-write interference.
- Attenuating coordination relation: the parent model assigns separate named managed Git worktrees during `subagent create --worktree`, so concurrent implementers operate against isolated working files and branches; parent/worker exchange and eventual review/merge reconcile outcomes rather than expose the same working tree to competing writers.
- Feedback into subsequent S1 behaviour: the chosen worktree path becomes the spawned child's effective working directory for its later tool calls; its branch or PR comes back as an integration artifact, and the parent can message/reassign a child or defer/alter a merge when work overlaps.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the intervention targets a named code-edit collision between distinct S1 producers; it changes their actual workspace topology and future write targets. Messaging alone, ordinary task splitting or generic queueing is not credited.
- Function: damp parallel implementation interference by deciding and maintaining task-specific checkout separation and integrating branch-level results.
- Disturbance / variety regulated: concurrent editing races and inadvertent shared-workspace corruption; downstream logical Git merge conflicts remain possible.
- Decisive decision or feedback right: choose which child receives a fresh checkout and task/branch, and adjust work allocation or subsequent merge handling after reports.
- Decision owner: parent model-led agent when operating the documented parallel-worktree mode; deterministic Git/worktree holder machinery implements the isolation decision.
- Supporting / enforcement mechanisms: `subagent.ts --worktree`, `worktree.ts` named checkouts and holder claims, per-agent cwd, Git branches, child messages/final reports.
- Closure path: parent recognizes parallel edits → assigns separate worktrees → each child modifies its own checkout → branch/PR or feedback returns → parent selects review, integration, clarification or further task allocation; future child work remains separated.
- Boundary reachability: the shipped CLI and runtime support worktree-bearing spawns; the first-party guide explicitly recommends and illustrates this normal multi-agent delivery pattern, not an unimplemented suggestion.
- Why this is / is not agent-owned: the parent model elects when/how to separate work and which tasks/branches to assign; static worktree creation, holder bookkeeping and Git merge mechanics are enforcement, not autonomous coordinators.
- Evidence: [worktrees, multiagent and collision purpose](https://github.com/ebetica/recurse/blob/6e4d231e299a14f19fe6eee9d9f7f43781780c2a/docs/guide.md), [child creation interface](https://github.com/ebetica/recurse/blob/6e4d231e299a14f19fe6eee9d9f7f43781780c2a/tools/subagent.ts), [managed checkouts and claims](https://github.com/ebetica/recurse/blob/6e4d231e299a14f19fe6eee9d9f7f43781780c2a/tools/worktree.ts), [example agent graph](https://github.com/ebetica/recurse/blob/6e4d231e299a14f19fe6eee9d9f7f43781780c2a/docs/examples.md).
- Basis: structural
- Confidence: medium
- Caveats: there is no automatic semantic merge-conflict arbitrator; S2 here is model-selected preventive checkout isolation and returned branch handling, not guaranteed conflict-free integration. One-agent or shared-cwd use does not exercise it.

## S3 — Inside-and-now control

- State: A
- Whole-system current view: the parent's model-request snapshot lists its child/descendant status and queued inputs, while native `subagent` reads/waits/messages expose individual work and results; the supervisor maintains authoritative live membership and lifecycle status.
- Current-control decision scope: the parent can choose/constrain concurrent commitments and effort on creation, interrupt or redirect active children, reassign with `move`, retire stale work cells and integrate or rework their output as the joint goal demands.
- Function: govern a coding tree's ongoing resource/commitment allocation and exceptional intervention while independent implementers own their local tasks.
- Disturbance / variety regulated: stalled agents, poor distribution of effort, late user requirements, active conflicts or incomplete child tasks and divergent branch outcomes.
- Decisive decision or feedback right: choose whether to launch, interrupt, redirect, reparent or retire child work and whether its returned work satisfies the whole task.
- Decision owner: model-backed parent agent in the supported multiagent tree; operator may intervene or take over, but operator interaction is not assumed to constitute an independent whole-team S3 parent mode.
- Supporting / enforcement mechanisms: live `Supervisor`/tree projection, agent digest, `subagent.ts` create/send/interrupt/wait/move/rm, Durable report holds and completion delivery, fixed resource/process limits.
- Closure path: status/child output/monitor/user steer → parent sees current tree information → parent selects task or resource intervention → supervisor/CLI changes relevant child agent and sends new input → changed work and updated status return to parent.
- Boundary reachability: the agent prompt includes a live tree digest; the shipped CLI supports the control operations under normal local execution, and child reports reach the parent automatically.
- Why this is / is not agent-owned: the parent model decides interventions and current tradeoffs; the supervisor enforces ownership/fencing and routes commands but is not itself a discretionary S3 agent. Merely having a class named `Supervisor` is insufficient.
- Evidence: [parent model tree digest](https://github.com/ebetica/recurse/blob/6e4d231e299a14f19fe6eee9d9f7f43781780c2a/src/agents/runtime/prompts.ts), [CLI control surface](https://github.com/ebetica/recurse/blob/6e4d231e299a14f19fe6eee9d9f7f43781780c2a/tools/subagent.ts), [tree ownership and interventions](https://github.com/ebetica/recurse/blob/6e4d231e299a14f19fe6eee9d9f7f43781780c2a/src/agents/README.md), [child report closure](https://github.com/ebetica/recurse/blob/6e4d231e299a14f19fe6eee9d9f7f43781780c2a/src/agents/durable/README.md).
- Basis: structural
- Confidence: medium
- Caveats: Recurse supplies general parent control primitives, not an always-on optimized project manager; the positive owner exists in the documented model-led multiagent mode and depends on the parent choosing current-control interventions, not on mechanical delegation alone.

## S3* — Complementary audit

- State: —
- Function: no first-party standard operating audit process is evidenced that independently inspects completed operational results and returns findings to current control.
- Disturbance / variety regulated: optimistic code-completion claims, faulty edits or unsafe commands could require independent checking.
- Decisive decision or feedback right: inspect raw delivered artifacts outside ordinary child reporting and issue a complementary verdict with corrective return; no installed closed path established.
- Decision owner: `pi-safety` uses a separate model to grant/deny *proposed* actions; an optional reviewer child can be authored by a user, but there is no default complementary outcome auditor.
- Supporting / enforcement mechanisms: separate model safety reviewer, action transcript, built-in denial gate, recipe for a review-agent graph, source tests and developer review rules.
- Closure path: safety's pre-execution `DENY` returns a reason and can change the next actor proposal; this regulates permissions, not independent observation of the action's real outcome. User-authored review scripts may create further loops but are not established here as an active standard process.
- Why this is / is not agent-owned: the second model genuinely judges proposed tool authorization, but its evidence deliberately excludes tool outputs, edited file content and post-execution result; its separate model identity does not make it complementary operational audit.
- Evidence: [review evidence boundary and fail-open behavior](https://github.com/ebetica/recurse/blob/6e4d231e299a14f19fe6eee9d9f7f43781780c2a/src/extensions/core/safety/README.md), [user-composed reviewer example](https://github.com/ebetica/recurse/blob/6e4d231e299a14f19fe6eee9d9f7f43781780c2a/docs/examples.md), [agent report path](https://github.com/ebetica/recurse/blob/6e4d231e299a14f19fe6eee9d9f7f43781780c2a/src/agents/durable/README.md).
- Basis: structural
- Confidence: medium
- Caveats: a local user could explicitly build a reviewer that reads branch diffs or tests; that would require assessment of its concrete installed closure, not promotion of general scriptability.

### Absence scope

- Surfaces inspected: separate safety-review model/inputs, child reports, read-only side conversations, sample reviewer graph, contributor QA instructions and source tests.
- Plausible first-party paths checked: safety pre-action veto, independent generated review agent, user-authored PR pipeline, operator prompt inspection, CI/test results and `return_to_main` side conversation.
- Why no material first-party path remains: the installed always-on reviewer is pre-action permission review with no distinct operational-result evidence; remaining alternatives are manual or illustrative compositions rather than a wired post-result independent audit loop.

## S4 — Outside-and-then intelligence

- State: —
- Function: no distinct prospective environment-model and capability adaptation loop is established beyond ordinary coding tasks and event-driven continuation.
- Disturbance / variety regulated: changing provider/tool ecosystems, CI trends, new project requirements and future architectural possibilities.
- Decisive decision or feedback right: choose a new whole-harness capability based on external/future distinctions and carry it back into live operation; not evidenced.
- Decision owner: agents can investigate and change repository code when tasked, while users/developers configure tools and skills; no autonomous organization-level S4 owner is shipped.
- Supporting / enforcement mechanisms: background monitors, memory, MCP configuration, skills, models and task-local planning.
- Closure path: a CI/deployment monitor can wake an agent for immediate handling, but a signal-to-task reaction is not itself prospective option formation and a capability-adaptation return to S3.
- Why this is / is not agent-owned: planning future code steps is S1 task choice; Recurse's extensibility offers means to construct S4 but no first-party defined future/environment adaptation decision loop.
- Evidence: [monitor and goals examples](https://github.com/ebetica/recurse/blob/6e4d231e299a14f19fe6eee9d9f7f43781780c2a/docs/examples.md), [extensibility principles](https://github.com/ebetica/recurse/blob/6e4d231e299a14f19fe6eee9d9f7f43781780c2a/README.md), [runtime guide](https://github.com/ebetica/recurse/blob/6e4d231e299a14f19fe6eee9d9f7f43781780c2a/docs/guide.md).
- Basis: structural
- Confidence: medium
- Caveats: general-purpose agents can be assigned external research or self-improvement tasks, but unbounded possibilities do not define a positive native S4 arrangement.

### Absence scope

- Surfaces inspected: monitor contracts, example skills, memory, provider/model settings, remote servers and background shell continuation.
- Plausible first-party paths checked: CI watchers, cron loops, goal reminder, user-authored agent graphs, skill/MCP configuration and persistent memory.
- Why no material first-party path remains: these capture events or customize immediate tasks but do not independently establish externally oriented prospective option judgment with an authorized return into current capability management.

## S5 — Policy and identity

- State: —
- Function: no distinct runtime identity/ultimate-policy adjudicator is established for the multiagent coding organization.
- Disturbance / variety regulated: risky commands, operator intent conflicts, policy exceptions, agent takeovers and security-mode choices.
- Decisive decision or feedback right: settle a whole-organization identity or ultimate-policy tension and return a binding new rule; no closed function-specific path shown.
- Decision owner: operator/developer owns Recurse permissions and safety instructions; model safety reviewer applies predefined action policy, and child/parent agents follow ordinary delegated task authority.
- Supporting / enforcement mechanisms: user task prompts, first-party `pi-safety` and custom additive policy rules, operator-only takeover, tool denial circuit breaker and user consent for exact actions.
- Closure path: model reviewer may return `DENY` and request a safer action or explicit authorization; that decides an individual command under existing policy, not a new identity-governing rule for the organization.
- Why this is / is not agent-owned: a model can reason about dangerous operations, but ultimate authority to change policy is not delegated to a live S5 body with a policy-level issue/escalation and operational return.
- Evidence: [safety review limits](https://github.com/ebetica/recurse/blob/6e4d231e299a14f19fe6eee9d9f7f43781780c2a/src/extensions/core/safety/README.md), [operator takeover](https://github.com/ebetica/recurse/blob/6e4d231e299a14f19fe6eee9d9f7f43781780c2a/docs/guide.md), [takeover state/authority](https://github.com/ebetica/recurse/blob/6e4d231e299a14f19fe6eee9d9f7f43781780c2a/src/agents/README.md).
- Basis: structural
- Confidence: medium
- Caveats: self-hosted operator remains a legitimate ultimate authority in practice; ordinary task approvals and safety policy configuration are insufficient by themselves to publish S5=P.

### Absence scope

- Surfaces inspected: built-in safety policy and operator override, takeover authority, project prompt, model efforts, config options and user-to-agent control.
- Plausible first-party paths checked: three-denial gate, protected safety-instruction editing, operator interruption, accepted user-request exception and global system prompt.
- Why no material first-party path remains: these enforce existing restrictions or let an operator direct a task; none shows a distinct identity/policy question reaching legitimate final authority and returning a revised system-wide identity rule.

## Distributed OSS parent arrangement

Recurse's repository maintainers and project contributor review process are not the runtime coding tree's metasystem. A self-hosted operator can observe, interrupt and take over an agent, but this does not convert every operator instruction into S5 or create an externally visible project-governance hierarchy. Remote provider models and CI services remain external dependencies.

## Self-hosted and non-human modes

The standard local mode supports one or many autonomous model conversations. With parallel child agents and managed worktrees, the parent model chooses isolation and current-work interventions (S2/S3); with one root, only the S1 loop may be exercised. The operator can take over a child, which then stops reporting to its old parent; that changes reporting and control ownership rather than constituting a permanent alternative parent-governed S3 mode. User-authored agent graphs might add audit/adaptation functions, but are not silently credited to the shipped distribution.

## Recursion

Each persistent child is an S1 operation with its own environment and decision loop. A child can spawn descendants, which reproduces the tree at another potential work-management scope; the existence of nested processes alone does not prove an independently closed viable metasystem at every depth. The published vector is for the documented local parent-and-workers delivery recursion.

## Variety and escalation

Worktree separation dampens shared-edit interference; status digest, result messages, interruption and task redirection let a model parent intervene when a local worker cannot absorb variety. Safety `DENY` messages and shell/monitor wakeups feed back into a specific agent's next proposal; they are not by themselves independent result audit, prospective adaptation or ultimate-policy escalation. Logical merge conflicts, missed work and unsafe outputs can still escape without a user-composed reviewer.

## Evidence gaps

Assessment is from the exact frozen source/documentation; no live Bun/provider conversation, parallel Git-edit collision test or end-to-end supervisor session was executed. The S2 and S3 positives are conditional on the documented agent-led multiagent/worktree mode, not default behavior in every deployment. Reviewer examples and project contributor review rules were excluded from operating S3* ownership because they require separately composed/triggered workflows rather than a native complementary evidence-return path.

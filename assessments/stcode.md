---
harness_id: stcode
project_name: stcode
repository: https://github.com/Ming-doan/stcode
review_ref: c8ea59204776d6ed1a4bbe395872f32027833905
reviewed_at: 2026-10-12
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# stcode

## Review boundary

- System in focus: shipped Python stcode Agent/Harness coding loop, daemon, supervisor, bounded `task` children and optional container team mode backed by a shared volume; reviewed as a repository-relative distribution, not the contributor organization.
- Purpose and identity: execute developer-specified code tasks with model-chosen tools, persistence and interactive steering; expose optionally deployed independent role agents with filesystem message passing.
- Relevant environment: daemon-owned local workspace/git branches, model provider and configured API credentials, team shared volume, role prompts and chat approvals, optional MCP/skills.
- Standard-distribution boundary: `stcode/core/agent`, `stcode/core/harness`, `stcode/core/daemon`, `stcode/core/team` and packaged CLI/config profiles. Team modes require explicit `[team] enabled` / `STCODE_TEAM=1`, role and shared volume; subagents are distinct from team peers.
- Credited operating / distribution surfaces: [README](https://github.com/Ming-doan/stcode/blob/c8ea59204776d6ed1a4bbe395872f32027833905/README.md); [Agent loop](https://github.com/Ming-doan/stcode/blob/c8ea59204776d6ed1a4bbe395872f32027833905/stcode/core/agent/agent.py); [task child executor](https://github.com/Ming-doan/stcode/blob/c8ea59204776d6ed1a4bbe395872f32027833905/stcode/core/agent/task.py); [trajectory supervisor](https://github.com/Ming-doan/stcode/blob/c8ea59204776d6ed1a4bbe395872f32027833905/stcode/core/agent/supervisor.py); [Mailbox](https://github.com/Ming-doan/stcode/blob/c8ea59204776d6ed1a4bbe395872f32027833905/stcode/core/team/mailbox.py); [send_message](https://github.com/Ming-doan/stcode/blob/c8ea59204776d6ed1a4bbe395872f32027833905/stcode/core/team/tools.py); [daemon session runner](https://github.com/Ming-doan/stcode/blob/c8ea59204776d6ed1a4bbe395872f32027833905/stcode/core/daemon/runner.py); [tools and harness](https://github.com/Ming-doan/stcode/blob/c8ea59204776d6ed1a4bbe395872f32027833905/stcode/core/harness/harness.py); [team mode contract](https://github.com/Ming-doan/stcode/blob/c8ea59204776d6ed1a4bbe395872f32027833905/docs/architecture/team.md); [agent loop design](https://github.com/Ming-doan/stcode/blob/c8ea59204776d6ed1a4bbe395872f32027833905/docs/architecture/agent-loop.md); [supervisor mode](https://github.com/Ming-doan/stcode/blob/c8ea59204776d6ed1a4bbe395872f32027833905/docs/architecture/supervisor.md); [team mode workflow](https://github.com/Ming-doan/stcode/blob/c8ea59204776d6ed1a4bbe395872f32027833905/docs/teams/workflow.md).
- Adjacent first-party surfaces excluded from ownership: developer/release CI, documentation's unevaluated team benchmarking exercise, human project maintainers, user-defined arbitrary team wiring beyond shipped commands/config and separate external Git hosting governance.
- First-party operating / deployment modes considered: normal single daemon-owned coding session; nested bounded task subprocess/child Agent; optional multi-container role agents each with own checkout and shared inbox; human/direct role dispatch and manual Git merge via devops convention; default low-cost trajectory supervisor.
- Recursion level: single autonomous coding-agent session for S1; optional independent role sessions at multi-container team recursion, for which current organizational coordination/supervision/audit requires separately established runtime decision loops.
- Reviewed revision: `c8ea59204776d6ed1a4bbe395872f32027833905`.
- Observation date: 2026-10-12.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

[Agent._turn_body](https://github.com/Ming-doan/stcode/blob/c8ea59204776d6ed1a4bbe395872f32027833905/stcode/core/agent/agent.py) invokes a provider model, executes selected local tool calls (possibly concurrently), gathers tool results before the next model request, handles incoming user/team messages at legal tool boundaries and stops when the model stops calling tools. [Harness](https://github.com/Ming-doan/stcode/blob/c8ea59204776d6ed1a4bbe395872f32027833905/stcode/core/harness/harness.py) enforces tool capability/approval semantics; [SessionRunner](https://github.com/Ming-doan/stcode/blob/c8ea59204776d6ed1a4bbe395872f32027833905/stcode/core/daemon/runner.py) owns execution, session persistence, watcher forwarding and approvals independently of TUI clients. [task](https://github.com/Ming-doan/stcode/blob/c8ea59204776d6ed1a4bbe395872f32027833905/stcode/core/agent/task.py) launches a separate bounded Agent/Harness child with its own transcript, one level of recursion and narrowed tool/write scopes. A child returns its final answer or a failure, not a mandatory independent audit.

The first-party [Mailbox](https://github.com/Ming-doan/stcode/blob/c8ea59204776d6ed1a4bbe395872f32027833905/stcode/core/team/mailbox.py) writes atomic JSON envelopes with references in a shared `/team/inbox/<role>/` directory. [send_message](https://github.com/Ming-doan/stcode/blob/c8ea59204776d6ed1a4bbe395872f32027833905/stcode/core/team/tools.py) enables exchange among configured peer roles. [team design](https://github.com/Ming-doan/stcode/blob/c8ea59204776d6ed1a4bbe395872f32027833905/docs/architecture/team.md) expressly specifies **no lead agent, no scheduler and no coordinator**; humans dispatch across BA/development roles. Each role maintains its own checkout/branch and a designated merging role convention. Shared docs rely on per-file ownership prompts; no native lock/CRDT/semantic arbitration was found for inter-worker interference. Team mode is off by default.

[Supervisor](https://github.com/Ming-doan/stcode/blob/c8ea59204776d6ed1a4bbe395872f32027833905/stcode/core/agent/supervisor.py) uses heuristics for repeated same tool arguments, high failure rate, repeated file writes, or many reads without writes in the **same executing session's transcript**. On a trigger, a cheaper model may return a nudge, appended back to that agent's ordinary conversation. This is present-task loop correction, not independent sampled operational reality or meta-system S3* by name alone.

## Operational model

The acting model selects coding tool actions and interprets results, so primary autonomous operations are established. Multiple separately executing role agents may exchange messages/refs and commit to separate branches, but shipped messages and Git handoffs lack a first-party inter-S1 disturbance-specific feedback arbitrator. Human movement across role containers and a convention of a final merger do not establish whole-current dynamic resource regulation in a standard agent-owned or parent-governed S3 mode. The low-cost supervisor acts only on the same local transcript rather than independently collecting artifact evidence. Project configuration/permissions and runtime model routing remain operator control rather than S4/S5 organizational authority.

## S1 — Operations

- State: A
- Function: Autonomously execute developer coding tasks through model-directed tool calls and source/test feedback.
- Disturbance / variety regulated: Unknown source content, editing/test/shell failures, tool availability, interrupts and incoming developer/team changes.
- Decisive decision or feedback right: A provider-backed Agent chooses its own file/shell/tool action from real previous results and determines whether to continue or finish a turn.
- Decision owner: The active root model or independently instantiated child/role Agent, not the daemon or tool executor.
- Supporting / enforcement mechanisms: Harness approvals, tool schemas/handlers, daemon-owned sessions, bounded max_turns, context/records and message delivery at safe tool boundaries.
- Closure path: Developer request → model selects tool(s) → Harness invokes real tools → returns full results → model selects correction, further actions or final response.
- Boundary reachability: Native installed stcode CLI/TUI/daemon instantiates Agent.create; role sessions/children can also use the same first-party Agent loop.
- Why this is / is not agent-owned: The model selects the organizationally relevant coding action; deterministic daemon, security, tracing and transport merely execute/enforce it.
- Evidence: [_turn_body / _run_tools](https://github.com/Ming-doan/stcode/blob/c8ea59204776d6ed1a4bbe395872f32027833905/stcode/core/agent/agent.py); [turn contract](https://github.com/Ming-doan/stcode/blob/c8ea59204776d6ed1a4bbe395872f32027833905/docs/architecture/agent-loop.md); [Harness](https://github.com/Ming-doan/stcode/blob/c8ea59204776d6ed1a4bbe395872f32027833905/stcode/core/harness/harness.py).
- Basis: explicit and structural
- Confidence: high for reachable coding loop; no live external-provider success claim
- Caveats: A permission gate or max-turn termination can prevent an action; this does not create a higher VSM owner.

## S2 — Coordination

- State: —
- Function: No first-party disturbance-specific coordination loop reducing actual conflict/oscillation between distinct operating role S1 units is established.
- Disturbance / variety regulated: Parallel role agents can diverge on API contracts, change incompatible files or block one another before final Git integration.
- Decisive decision or feedback right: The human dispatches work by role; send_message transports messages. Git's generic branch/merge mechanism can reveal merge conflicts, but product supplies no S2-specific dispute decision/return loop governing peer behavior.
- Decision owner: Human role operator or peer models for their local tasks; no explicit S2 coordination right.
- Supporting / enforcement mechanisms: Filesystem mailbox, write-then-rename delivery, references instead of pasted bodies, one merge-owner convention and separate checkouts.
- Closure path: Role message → recipient inbox/next Agent turn; Git branches merge according to operator action. No actual/structural conflict witness → first-party attenuation decision → returned revised commitments to affected S1 workers.
- Boundary reachability: Messaging is reachable only in enabled multi-container role mode; the protocol has no coordination controller and remains a transport.
- Why this is / is not agent-owned: Communication content and separate branches are not themselves a specific coordination decision over a known inter-S1 disturbance.
- Evidence: [no coordinator/no locks role design](https://github.com/Ming-doan/stcode/blob/c8ea59204776d6ed1a4bbe395872f32027833905/docs/architecture/team.md); [mailbox](https://github.com/Ming-doan/stcode/blob/c8ea59204776d6ed1a4bbe395872f32027833905/stcode/core/team/mailbox.py); [send_message](https://github.com/Ming-doan/stcode/blob/c8ea59204776d6ed1a4bbe395872f32027833905/stcode/core/team/tools.py); [Git merge convention](https://github.com/Ming-doan/stcode/blob/c8ea59204776d6ed1a4bbe395872f32027833905/docs/teams/workflow.md).
- Basis: explicit negative design and structural
- Confidence: high at frozen shipped boundary
- Caveats: Custom user agent instructions could compose coordination, but that is not standard first-party S2.

### Absence scope

- Surfaces inspected: Core team Mailbox and send_message, role/checkout configuration, Git merge convention, nested task delegation.
- Plausible first-party paths checked: Specific inter-S1 file/API conflict handling, lock/reservation/adjudication or escalation rule with correction delivered into later role operation.
- Why no material first-party path remains: Explicit team design states no scheduler/coordinator and no shared-knowledge locking/CRDT. Other paths merely deliver messages or isolate branches; no conflict-specific first-party closure.

## S3 — Inside-and-now control

- State: —
- Function: No standard whole-team current-control loop allocating resources/priorities and returning its decisions to multiple operational S1s is evidenced.
- Disturbance / variety regulated: Multiple role agents require whole-project accountability and reconciliation when work diverges; the shipped runtime deliberately leaves dispatch and integration to humans.
- Decisive decision or feedback right: No built-in central model manager chooses task priorities across role agents. A user manually enters different role containers; a devops role convention merges branches but does not establish a standard whole-system managerial controller.
- Decision owner: Individual role models and external human task assigner; neither is a proven first-party whole-current manager in this boundary.
- Supporting / enforcement mechanisms: Daemon per-role sessions, bare Git origin and one merge-owner convention, local transcript supervisor and per-agent tool approvals.
- Closure path: Per-role local task/report and Git branch → human/role integration. No native whole-current team view → authoritative resource/commitment decision → returned correction to operating roles.
- Boundary reachability: The deployed multiple-role mode has inboxes and isolated agents, not a first-party management board/controller with decisive rights; this negative is scoped to the shipped deployment contract.
- Why this is / is not agent-owned: Routine local loop nudges, provider-turn limits and role-based task delegation do not provide a whole-recursion current-control decision owner.
- Evidence: [human-led dispatch](https://github.com/Ming-doan/stcode/blob/c8ea59204776d6ed1a4bbe395872f32027833905/docs/architecture/team.md); [team integration](https://github.com/Ming-doan/stcode/blob/c8ea59204776d6ed1a4bbe395872f32027833905/docs/teams/workflow.md); [single-agent nudge](https://github.com/Ming-doan/stcode/blob/c8ea59204776d6ed1a4bbe395872f32027833905/stcode/core/agent/supervisor.py); [per-session ownership](https://github.com/Ming-doan/stcode/blob/c8ea59204776d6ed1a4bbe395872f32027833905/stcode/core/daemon/runner.py).
- Basis: explicit and structural
- Confidence: medium-high
- Caveats: A parent institution could create an S3 management process around stcode, but no complete first-party parent-mode return path was shown.

### Absence scope

- Surfaces inspected: Team design and roles, daemon status, role prompts, git integration, supervisor and nested task.
- Plausible first-party paths checked: Whole-system present commitments/resources visibility, agent or legitimate parent manager making decisions over multiple S1s and an operative return path.
- Why no material first-party path remains: The package deliberately supplies separate role sessions plus human coordination conventions, not an integrated whole-current management/feedback loop.

## S3* — Complementary audit

- State: —
- Function: No complementary audit path with sufficiently independent operational evidence, audit judgment and return into meta-control is established.
- Disturbance / variety regulated: An agent can loop, fail tools or claim completion without evidence; shipped supervisor helps diagnose loop symptoms from normal records.
- Decisive decision or feedback right: Low-cost supervisor may issue a nudge based exclusively on the acting agent's same transcript; no independent file/artifact replay or source-sampling review is required.
- Decision owner: Deterministic heuristic plus low-difficulty model judging transcript stagnation, acting within the unit's own execution feedback; no independent audit authority.
- Supporting / enforcement mechanisms: Supervisor.smell/check, session records, lightweight model inference and user-message nudge; optional generic task child.
- Closure path: Same agent transcript → heuristic trigger → optional small-model nudge → same agent continues local task. This is ordinary S1 execution correction, not complementary access → independent audit → S3 governance closure.
- Boundary reachability: Supervisor is enabled by default for root Agent and omitted for subagents, but its data source is still solely the acting Agent's routine records.
- Why this is / is not agent-owned: A second model instance or class named Supervisor does not make its input sufficiently independent for S3*; a nudge is not operational-source inspection.
- Evidence: [Supervisor.smell/check/diagnose](https://github.com/Ming-doan/stcode/blob/c8ea59204776d6ed1a4bbe395872f32027833905/stcode/core/agent/supervisor.py); [_supervise](https://github.com/Ming-doan/stcode/blob/c8ea59204776d6ed1a4bbe395872f32027833905/stcode/core/agent/agent.py); [same-session trajectory contract](https://github.com/Ming-doan/stcode/blob/c8ea59204776d6ed1a4bbe395872f32027833905/docs/architecture/supervisor.md); [generic child](https://github.com/Ming-doan/stcode/blob/c8ea59204776d6ed1a4bbe395872f32027833905/stcode/core/agent/task.py).
- Basis: explicit and structural
- Confidence: high for absence of independent artifact access in first-party supervisor
- Caveats: External reviewer agents can be configured separately; no standard S3*-specific independent reality-access contract is implied.

### Absence scope

- Surfaces inspected: Supervisor model, same transcript, task child, tracing, developer tests and role checkout convention.
- Plausible first-party paths checked: Independent source-file/artifact sampling, audit judgment over routine claims and feedback to current whole-team manager.
- Why no material first-party path remains: Primary supervisor only reads ordinary production transcript; separately executing task children are generic work delegates, not required source-first audit actors.

## S4 — Outside-and-then intelligence

- State: —
- Function: No autonomous external-and-prospective intelligence function with return into present organizational capability is established.
- Disturbance / variety regulated: Provider ecosystems, future project architecture, dependencies and user objectives may evolve; implementation does not operate an independent future-environment intelligence process.
- Decisive decision or feedback right: Human selects model/config and team roles; current coding agents choose immediate implementation tactics. No prospective organization-level adaptation owner.
- Decision owner: Operator for provider and role configuration, coding model for local plans.
- Supporting / enforcement mechanisms: Gateway routing, model difficulty tiers, skills/MCP plugin loading, system prompts, per-session context.
- Closure path: New config/prompt or task → local active Agent operation. Missing sensed external/future distinction, assessed strategic option and adoption returned to current S3.
- Boundary reachability: Inspected default and enabled role/tool modes; no standard adaptation loop beyond responding to human objectives.
- Why this is / is not agent-owned: Current project planning, model choice, source lookup and compaction do not equal prospective S4.
- Evidence: [provider gateway](https://github.com/Ming-doan/stcode/blob/c8ea59204776d6ed1a4bbe395872f32027833905/stcode/core/providers/gateway.py); [harness config](https://github.com/Ming-doan/stcode/blob/c8ea59204776d6ed1a4bbe395872f32027833905/docs/architecture/harness.md); [team roles](https://github.com/Ming-doan/stcode/blob/c8ea59204776d6ed1a4bbe395872f32027833905/docs/architecture/team.md).
- Basis: structural
- Confidence: medium-high
- Caveats: A user could assign forward-looking research to an agent, but that single S1 user job does not establish a standing first-party S4-to-S3 loop.

### Absence scope

- Surfaces inspected: Provider gateway, role agent profiles, MCP/skills, context tools, project docs.
- Plausible first-party paths checked: External future sensing/option generation and a returned organization-level adaptation choice changing present capability.
- Why no material first-party path remains: No specified and wired outside-and-then intelligence loop; available features support a current task or operator-controlled configuration.

## S5 — Policy and identity

- State: —
- Function: No operational ultimate identity/purpose-policy arbitration right with a binding whole-team feedback closure is supplied.
- Disturbance / variety regulated: Role identity text, autonomy restrictions and approval decisions bound execution, not organization-wide constitutional coherence.
- Decisive decision or feedback right: Human/operator sets approval mode, team enrollment/role, max_clients and config. No actor settles an S3–S4 organization identity conflict.
- Decision owner: External operator chooses process settings; runtime enforces tool permissions/role validity.
- Supporting / enforcement mechanisms: Daemon guard_autonomy, session approvals, role config, tool scope caps and team enable/disable flags.
- Closure path: Local operator config/approval → affected role/session tool behavior; absent ultimate-policy question/legitimate S5 arbiter/returned binding identity decision.
- Boundary reachability: Role config and approvals are first-party settings but not first-party S5 function.
- Why this is / is not agent-owned: Safety and operational instruction hierarchy are not evidence of ultimate organizational policy ownership.
- Evidence: [autonomy guard](https://github.com/Ming-doan/stcode/blob/c8ea59204776d6ed1a4bbe395872f32027833905/stcode/core/daemon/autonomy.py); [configs](https://github.com/Ming-doan/stcode/blob/c8ea59204776d6ed1a4bbe395872f32027833905/stcode/core/configs.py); [role config](https://github.com/Ming-doan/stcode/blob/c8ea59204776d6ed1a4bbe395872f32027833905/docs/architecture/team.md).
- Basis: structural
- Confidence: high for reviewed boundary
- Caveats: An independent deploying organization may supply constitutional policy but is not part of shipped standard runtime.

### Absence scope

- Surfaces inspected: Role prompt/config, runtime guard, approval callbacks, human deployment operations and repo policy documents.
- Plausible first-party paths checked: Constitutive identity-level decision path and legitimate authority returning into whole-system future/current balance.
- Why no material first-party path remains: Shipped controls are task, permission and deployment settings; no identity-policy adjudication or S3–S4 balance closure.
## Recursion

Default agent loop is autonomous coding S1. In enabled team mode each independently running role/container can be an operational S1 at a higher collaboration recursion, and `task` children form bounded within-role work, but the system does not automatically acquire S2 or S3 by having peers and inboxes. The local stagnation supervisor watches one S1's normal transcript only. A true org-level metasystem would require the missing coordination/current-control/evidence closure described above.

## Variety and escalation

Tool errors and verifier feedback return through the ordinary agent loop. A supervisor nudge corrects an individual agent's repeated actions, not an independent audit. Team mailbox notifications are atomic and deliver referential messages to another role, but delivery is not an inter-S1 conflict decision. User interruptions and permission denials are local execution controls. No standalone algedonic channel is inferred from daemon events or statuses without a receiving authority and return decision.

## Evidence gaps

- Frozen first-party code/doc source inspection; no paid live-provider run or multi-container operational benchmark performed.
- Team design explicitly says no lead agent, scheduler, coordinator, locking or CRDT; custom deployment governance may change this but is outside the reviewed standard boundary.
- A reviewer task can be instructed externally; the shipped low-cost Supervisor itself does not inspect independently sourced operational artifacts, so S3* is not promoted from its name or use of a second model.
- Documentation includes an evaluation set for team mode described as not yet executed; no performance or validation claim is inferred from it.

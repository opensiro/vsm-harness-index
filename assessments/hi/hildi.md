---
harness_id: hildi
project_name: Hildi
repository: https://github.com/one-king-studio/hildi
review_ref: d5fb376ab918e02facdbdcc0fbf00dabb3f6a806
reviewed_at: 2026-11-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# Hildi

## Review boundary

- System in focus: Hildi's supported Free Pascal coding-agent installation, including its headless socket runtime, TUI client, local workspace/session store, shared peer-task board and supervised child-agent processes.
- Purpose and identity: Execute model-selected coding/file/shell tasks with scoped approval, shared-workspace conflict avoidance, recoverable session history and bounded delegated subtask execution.
- Relevant environment: Local workspace and competing model sessions, users, provider API, MCP processes, SQLite, running tool calls, child agent processes and TUI supervision.
- Standard-distribution boundary: The wired hildi-agent headless runtime plus sibling hildi TUI and supported tools/SQLite store, in single-session, independent same-workspace peer and delegated child modes.
- Credited operating / distribution surfaces: [agent loop](https://github.com/one-king-studio/hildi/blob/d5fb376ab918e02facdbdcc0fbf00dabb3f6a806/src/HildiAgent.pas), [harness session](https://github.com/one-king-studio/hildi/blob/d5fb376ab918e02facdbdcc0fbf00dabb3f6a806/src/HildiHarnessSession.pas), [coordination protocol](https://github.com/one-king-studio/hildi/blob/d5fb376ab918e02facdbdcc0fbf00dabb3f6a806/src/HildiCoordination.pas), [task claims](https://github.com/one-king-studio/hildi/blob/d5fb376ab918e02facdbdcc0fbf00dabb3f6a806/src/HildiTasksStore.pas), [runtime subagent supervisor](https://github.com/one-king-studio/hildi/blob/d5fb376ab918e02facdbdcc0fbf00dabb3f6a806/src/HildiSubagentSupervisor.pas), [subagent observer](https://github.com/one-king-studio/hildi/blob/d5fb376ab918e02facdbdcc0fbf00dabb3f6a806/src/HildiHarnessSubagentSpy.pas) and [TUI intervention](https://github.com/one-king-studio/hildi/blob/d5fb376ab918e02facdbdcc0fbf00dabb3f6a806/src/HildiHarnessApp.pas).
- Adjacent first-party surfaces excluded from ownership: Spec-first development documents, development AGENTS.md, test doubles, test suite, compiler/dependency packaging, CI, contributor and release workflows. They corroborate reachable runtime paths without governing live agents.
- First-party operating / deployment modes considered: One TUI+headless agent, independently started peer sessions in the same workspace, optional child delegation/message/abort/release, operator spy/abort/promote, gated shell/file tools, persistent shared tasks/board, MCP/skills and offline local store.
- Recursion level: The workspace's cooperating model-owned sessions and, separately, a parent session's child task portfolio; child nesting is a lower S1 division, not proof of another viable metasystem.
- Reviewed revision: d5fb376ab918e02facdbdcc0fbf00dabb3f6a806.
- Observation date: 2026-11-04.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

HildiAgent drives a model/tool feedback loop with a bounded iteration limit; the headless runtime runs a local session socket and a TUI connects in a drive or observe role. The loop and SDK expose shell commands and file tools under approval, an SQLite transcript and history, workspace change logs, skills, MCP clients and task/board tools. Independent live sessions sharing one workspace are detected from a runtime-presence table; a per-turn coordination prompt distinguishes peers from spawned children and changes when peers arrive/leave. The shared task list uses an atomic SQL claim and reports the other claimant plus claim age on conflict; board posts/supersession retain coordination decisions. A parent may asynchronously spawn, message, abort or release bounded child session processes. Their results arrive as ambient notifications which can wake the parent model. A TUI operator can observe a child's raw stored transcript plus live stream through a separate observe-only socket, and can abort, release or promote the child, detaching it and posting a takeover notice into the parent's board. This operator mode supplements, but does not continuously replace, model control. [README](https://github.com/one-king-studio/hildi/blob/d5fb376ab918e02facdbdcc0fbf00dabb3f6a806/README.md), [features index](https://github.com/one-king-studio/hildi/blob/d5fb376ab918e02facdbdcc0fbf00dabb3f6a806/docs/features/FEATURES.md), [runtime](https://github.com/one-king-studio/hildi/blob/d5fb376ab918e02facdbdcc0fbf00dabb3f6a806/src/HildiSessionRuntime.pas).

## Operational model

The primary model-owned session selects actual coding actions. Separately launched peer sessions are distinct S1 units, and child sessions do self-contained model task work for a parent. A coordination rule tells peers to claim before changing, and the atomic claim implements an explicit conflict/refusal outcome returned to a model; the agents decide whether to take different work, wait or revise. The parent agent controls current child commitments using delegation and returned results. In a different supported first-party mode the human operator sees the child roster/live details and intervenes through the TUI, with an operationally returned status/board notice. Those two S3 modes are documented independently. Direct child observation enables a complementary audit construction path but does not ship an autonomous independent reviewer with a prescribed audit judgment.

## S1 — Operations

- State: A
- Function: Model-led coding and file/system task execution through observed tool feedback.
- Disturbance / variety regulated: User instructions, unknown file state, command errors, provider tool-call responses and subtask results.
- Decisive decision or feedback right: Select tools/arguments, decide edits and shell commands, consult source, request child work and revise steps based on returned observations.
- Decision owner: The model in each supported session/child agent loop.
- Supporting / enforcement mechanisms: TAgentLoop, OpenAI-compatible model transport, approval gate, command classification, SQLite session store, socket runtime and bounded tools.
- Closure path: User/ambient context → LLM tool selection → execution under approval → tool result returned in conversation → subsequent model turn or final answer; child completions may wake the parent for another turn.
- Boundary reachability: The shipped hildi-agent runtime constructs THarnessSession with TAgentLoop and tool registry; the TUI drives the same socket session and child processes run the same agent mechanism.
- Why this is / is not agent-owned: Deterministic approval/security and session persistence remain without a model, but they cannot choose which code changes solve the current task.
- Evidence: [HildiAgent](https://github.com/one-king-studio/hildi/blob/d5fb376ab918e02facdbdcc0fbf00dabb3f6a806/src/HildiAgent.pas), [HildiHarnessSession tool wiring](https://github.com/one-king-studio/hildi/blob/d5fb376ab918e02facdbdcc0fbf00dabb3f6a806/src/HildiHarnessSession.pas), [HildiSessionRuntime](https://github.com/one-king-studio/hildi/blob/d5fb376ab918e02facdbdcc0fbf00dabb3f6a806/src/HildiSessionRuntime.pas).
- Basis: explicit + structural.
- Confidence: high in wired agent/tool loop; provider efficacy not exercised.
- Caveats: Headless model inference requires a configured external provider; source-level claims are not live model task benchmarks.

## S2 — Coordination

- State: A
- Function: Suppress duplicate work and stale-state oscillation among independent model-operated sessions in the same workspace.
- Disturbance / variety regulated: Two peers simultaneously starting the same task, overwriting one another's workspace changes or acting on stale task/board state.
- Distinct S1 units: Separate independently started live agent sessions detected via session_runtimes, explicitly distinguished from parent-owned spawned child sessions.
- Inter-S1 disturbance: Competing peers race to claim an open card; without the guarded claim both could work it and issue conflicting changes. Protocol also identifies path ownership/commit cadence as conflict risks.
- Attenuating coordination relation: Shared board decisions plus task_claim's atomic compare-and-swap, holder/age refusal and mandatory claim-before-change rule; peer mode is selected from actual live runtime presence rather than a static multi-agent flag.
- Feedback into subsequent S1 behaviour: Losing claim returns holder/status and how long held to the requesting model; board notices and mode-transition ambient messages prompt a fresh board_read, revised claim/task choice or peer protocol.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: Conflict arises between distinct independent S1 agents; a first-party prevention gate identifies its winner/loser, and the model-directed protocol uses that feedback to adjust later operations. Spawned children are deliberately treated as delegation, not peer negotiation.
- Decisive decision or feedback right: Choose a different card, defer modifications, negotiate path ownership/commit protocol and record a new shared decision when contention or changing peer presence is observed.
- Decision owner: Each model-driven peer agent, with deterministic SQLite CAS as enforcement, not as discretionary coordinator.
- Supporting / enforcement mechanisms: HildiCoordination live-peer query and prompt, TSqliteTaskStore.Claim, TTaskTool.ClaimCard, board_post/read, task update and stale-source warnings.
- Closure path: Contending work intentions → atomic claim/board visibility → successful claim or explicit holder refusal → returned tool/ambient feedback → agent revises own next task and writes a shared coordination decision when needed.
- Boundary reachability: A stored workspace session wires TTaskTool and TBoardTools directly into the model registry; DetectCoordinationMode and NoticeBoard run in the supported per-turn session path with peer joining/leaving messages.
- Why this is / is not agent-owned: The CAS cannot decide which alternative task, path ownership or coordination protocol to adopt after conflict; the model session owns that discretion.
- Evidence: [HildiCoordination](https://github.com/one-king-studio/hildi/blob/d5fb376ab918e02facdbdcc0fbf00dabb3f6a806/src/HildiCoordination.pas), [ClaimCard](https://github.com/one-king-studio/hildi/blob/d5fb376ab918e02facdbdcc0fbf00dabb3f6a806/src/HildiTasksTools.pas), [atomic Claim](https://github.com/one-king-studio/hildi/blob/d5fb376ab918e02facdbdcc0fbf00dabb3f6a806/src/HildiTasksStore.pas), [NoticeBoard and tool registration](https://github.com/one-king-studio/hildi/blob/d5fb376ab918e02facdbdcc0fbf00dabb3f6a806/src/HildiHarnessSession.pas).
- Basis: explicit + structural.
- Confidence: high for peer-level claim contention; not evidence of an always-successful multi-agent planning consensus.
- Caveats: Claim-before-change is an instruction, not a forced path-level reservation for every write; external tools may bypass it.

## S3 — Inside-and-now control

- State: A(P)
- Function: Maintain and intervene in current child-agent commitments in a parent-session work portfolio.
- Disturbance / variety regulated: Active child availability, asynchronous failures, task ownership changes, approval stalls and urgent operator takeover during live work.
- Whole-system current view: The model obtains child status/slot acknowledgments and ambient terminal results, while the human operator's sidebar/spy shows the full current child roster and direct child transcript/live stream in the same parent composition.
- Current-control decision scope: Model chooses delegate/message/abort/release actions, task scope, child follow-ups and parent next work; human chooses abort/release/promote of a specific child with live roster context.
- Decisive decision or feedback right: In the base mode, the parent model allocates/reallocates work and responds to child outcomes; in the supervised mode, the operator decides whether a live child remains under the parent's current control.
- Decision owner: Base A mode — parent model; parent P mode — legitimate operator acting through the TUI for that task composition. SubagentSupervisor only enforces capacities, socket commands, event relay and lineage.
- Supporting / enforcement mechanisms: Child process supervisor, max/depth caps, message/abort/release command handlers, parent prompt queue, child roster, observer socket, status board and session lineage detachment.
- Closure path: Base: delegation → independent child run → result/aborted/gone event → ambient parent wake → model changes next commitments. Parent mode: operator inspects roster/live child → aborts/releases/promotes → runtime command changes child operation/lineage, and takeover coordination notice reaches the former parent.
- Boundary reachability: HildiSessionRuntime creates TSubagentSupervisor and registers the model-callable child tools; TUI ShowSpy, OnSpyAction and AnnounceTakeover are shipped with the sibling client and address the live parent/child session.
- Why this is / is not agent-owned: The base choice of which task to delegate or revise is model discretionary; the optional human takeover is an independently evidenced alternative decisive owner. Registry limits and event loops enforce but do not select either owner's intervention.
- Evidence: [subagent tools and service](https://github.com/one-king-studio/hildi/blob/d5fb376ab918e02facdbdcc0fbf00dabb3f6a806/src/HildiSubagent.pas), [supervisor](https://github.com/one-king-studio/hildi/blob/d5fb376ab918e02facdbdcc0fbf00dabb3f6a806/src/HildiSubagentSupervisor.pas), [runtime ambient return](https://github.com/one-king-studio/hildi/blob/d5fb376ab918e02facdbdcc0fbf00dabb3f6a806/src/HildiSessionRuntime.pas), [TUI takeover path](https://github.com/one-king-studio/hildi/blob/d5fb376ab918e02facdbdcc0fbf00dabb3f6a806/src/HildiHarnessApp.pas).
- Basis: explicit + structural.
- Confidence: high for delegated current-control and observed parent mode, bounded to one composition.
- Caveats: This is not a whole-organization manager of all unrelated peer sessions. The P mode is optional and its board notification is best-effort; loss of the notification can weaken parent awareness although lineage detachment still changes what the parent can command.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Parent model | Decide to delegate, revise, message or stop child work | Supervisor returns result/diagnostic into parent ambient turn; model changes next commitments | [Subagent tool and runtime](https://github.com/one-king-studio/hildi/blob/d5fb376ab918e02facdbdcc0fbf00dabb3f6a806/src/HildiSessionRuntime.pas) |
| Parent (`P`) | Human TUI operator | Live child roster/spy reveals need to intervene | TUI abort/release/promote changes live child/lineage and records a takeover notice for parent | [OnSpyAction and AnnounceTakeover](https://github.com/one-king-studio/hildi/blob/d5fb376ab918e02facdbdcc0fbf00dabb3f6a806/src/HildiHarnessApp.pas) |

## S3* — Complementary audit

- State: C
- Function: Supply an independent-from-summary observation path into a delegated child's actual conversation/tool operations for potential corrective audit by an operator or composed reviewer.
- Disturbance / variety regulated: Parent receives only a summarized child result, which may hide failed tool actions or unexpectedly broad work; a distinct observer can inspect recorded tool/action reality.
- Claim being audited: Whether a child actually performed the stated actions and whether its work should continue under parent authority.
- Ordinary reporting path: TSubagentSupervisor sends summarized completion/status as an ambient result to the parent model.
- Complementary access path: Separate observe-only TSessionClient socket to the child's runtime plus a stored per-child transcript tail, showing raw tool, error, assistant and live event stream.
- Independence boundary: The observer is not the child's own summary and does not gain a drive role; it reads first-party child runtime/store evidence directly. It is not independent of the physical host's persistence or evidence integrity, and does not itself make an audit verdict.
- Who acts on findings: In the shipped UI a human can inspect and abort/promote/release a child, with takeover notice and detachment; a composed independent audit judgment/mandate remains required for autonomous S3* ownership.
- Decisive decision or feedback right: Compare direct child execution evidence with reported status and decide whether/how to return corrective intervention; the specific observation/intervention seam exists, but no dedicated independent autonomous reviewer is wired.
- Decision owner: Potential human auditor/constructor consumer; no shipped agent-owned S3* judgment. The TUI supplies direct access and intervention construction points, not an automatic auditor.
- Supporting / enforcement mechanisms: Read-only session observer, historical message tail, live stream renderer, child status, abort/release/promote controls and board takeover status.
- Closure path: Parent result claim → optional direct child spy and transcript examination → operator may intervene via runtime command and parent board notice; an autonomous audit actor and systematic checking policy would require composition.
- Boundary reachability: Sidebar/ShowSpy and TSubagentSpy.Open are shipped UI paths; OnSpyAction calls the supported runtime command and AnnounceTakeover publishes a corrective status for the former parent.
- Why this is / is not agent-owned: A second direct observer and corrective control surfaces are not just the ordinary result summary, but no first-party model auditor decides independent findings; accordingly the scoped S3*-specific constructor is C, not A.
- Evidence: [HildiHarnessSubagentSpy](https://github.com/one-king-studio/hildi/blob/d5fb376ab918e02facdbdcc0fbf00dabb3f6a806/src/HildiHarnessSubagentSpy.pas), [TUI ShowSpy / OnSpyAction](https://github.com/one-king-studio/hildi/blob/d5fb376ab918e02facdbdcc0fbf00dabb3f6a806/src/HildiHarnessApp.pas), [runtime ordinary child reporting](https://github.com/one-king-studio/hildi/blob/d5fb376ab918e02facdbdcc0fbf00dabb3f6a806/src/HildiSessionRuntime.pas).
- Basis: explicit + structural.
- Confidence: medium; the claim is deliberately limited to complementary observation and possible corrective return, not guaranteed independent audit.
- Caveats: The user's decision may be ordinary supervision rather than a formal audit; an observed and acted-on discrepancy is not demonstrated by a live trace in this review.

## S4 — Outside-and-then intelligence

- State: —
- Function: No separately closed process that evaluates external future possibilities and adapts the workspace organization or operating capability.
- Disturbance / variety regulated: Changing providers, project context and tool availability may require new skills or working strategy, but the installed agent mostly responds within the current task.
- Decisive decision or feedback right: Judge external prospective capability needs and return a strategic adaptation into present operation; no such closed first-party decision owner is installed.
- Decision owner: User/developer selects skills, MCP providers and runtime upgrades; a model chooses on-demand current tools, board entries and task plans.
- Supporting / enforcement mechanisms: MCP tool reconciliation, dynamic prompt assembly, skill loading, checkpoint/handoff, workspace board, goals and current task queue.
- Closure path: Tools/skills can change with configuration and context checkpoints can carry a recent summary; none supplies a future-oriented outside assessment and authoritative capability-adaptation decision returned to S3.
- Why this is / is not agent-owned: A static skill or saved plan may shape next work, but neither is a prospective adaptation regulator with continuing responsibility.
- Evidence: [turn assembly](https://github.com/one-king-studio/hildi/blob/d5fb376ab918e02facdbdcc0fbf00dabb3f6a806/src/HildiHarnessSession.pas), [skills](https://github.com/one-king-studio/hildi/blob/d5fb376ab918e02facdbdcc0fbf00dabb3f6a806/src/HildiSkills.pas), [MCP provider](https://github.com/one-king-studio/hildi/blob/d5fb376ab918e02facdbdcc0fbf00dabb3f6a806/src/HildiMCPProvider.pas), [feature statuses](https://github.com/one-king-studio/hildi/blob/d5fb376ab918e02facdbdcc0fbf00dabb3f6a806/docs/features/FEATURES.md).
- Basis: structural.
- Confidence: medium-high for bounded shipped modes.
- Caveats: An external agent might use Hildi to maintain/evolve a project, but such an additional organization's strategic loop is not Hildi's standard runtime.

### Absence scope

- Surfaces inspected: Runtime loop, MCP lifecycle, skills, transcript checkpoint, task/board protocol, features statuses and main distribution entry points.
- Plausible first-party paths checked: Dynamic tool registration, goal/plan carryover, context handoff, peer protocol decisions and user-provided skill evolution.
- Why no material first-party path remains: These support task recovery, current configuration and peer work; none links outside-future analysis to an owned capability-change decision and returned present operation.

## S5 — Policy and identity

- State: —
- Function: No complete runtime constitutional-identity or ultimate-policy adjudication and return loop at the assessed agent organization level.
- Disturbance / variety regulated: Risky shell actions, approval scopes, task-card moderation and peer protocol changes remain local work/coordination decisions rather than identity-level constitutional conflicts.
- Decisive decision or feedback right: Authoritatively resolve a conflict about organizational identity or ultimate purpose, then return a binding policy decision to all affected ongoing operation; not present.
- Decision owner: Operator grants tool permissions and moderates shared records; model agents negotiate path/task protocols; maintainers decide repository policy outside the shipped runtime.
- Supporting / enforcement mechanisms: Command effect classification and approval, shared board moderation, operator task reassignment and peer coordination prompt.
- Closure path: User approval allows/denies tools and peer board decisions guide later tasks, but no identity-level matter → legitimate ultimate-policy authority → binding return to the live organization is established.
- Why this is / is not agent-owned: Claim ownership, operator takeover and shared protocol negotiation affect present work allocation (S2/S3), not the durable ultimate purpose or identity of the system.
- Evidence: [approval](https://github.com/one-king-studio/hildi/blob/d5fb376ab918e02facdbdcc0fbf00dabb3f6a806/src/HildiApproval.pas), [board tools](https://github.com/one-king-studio/hildi/blob/d5fb376ab918e02facdbdcc0fbf00dabb3f6a806/src/HildiBoardTools.pas), [task moderation](https://github.com/one-king-studio/hildi/blob/d5fb376ab918e02facdbdcc0fbf00dabb3f6a806/src/HildiTasksTools.pas), [coordination protocol](https://github.com/one-king-studio/hildi/blob/d5fb376ab918e02facdbdcc0fbf00dabb3f6a806/src/HildiCoordination.pas).
- Basis: structural.
- Confidence: medium-high for bounded absence.
- Caveats: The public project's actual maintainer identity/governance decisions are adjacent, not a governing organ reached through the live harness.

### Absence scope

- Surfaces inspected: Human approval TUI/runner, board/task policy and moderation, peer coordination prompt, child lineage/ownership, plugin/security config and contribution docs.
- Plausible first-party paths checked: Owner takeover, peer protocol decisions, task reassignment, persisted board decisions and shell approval grants.
- Why no material first-party path remains: None escalates an identity/ultimate-policy dilemma to a legitimate parent authority and returns a durable policy resolution to subsequent operation across the assessed organization.

## Distributed OSS parent arrangement

Hildi's own development repository documents human/agent contributions and specific release/testing rules. They are outside the shipped agent organization. The supported human-operated TUI is credited only for its live S3 parent mode and optional S3* observation/intervention seam, not as an automatic project-wide S5 organ.

## Self-hosted and non-human modes

One agent with SQLite can use the board as a journal; multiple separately launched peer agents activate S2 coordination through the same model tools. A model parent delegates, receives ambient child results and changes commitments autonomously (S3 A). A TUI operator may instead inspect and interrupt/promote a child with returned coordination notice (S3 P). No assumption of permanently attached human oversight is made.

## Recursion

Spawned children own bounded task execution contexts but do not inherit a full independent S2–S5 metasystem. Independent peer sessions sharing the same workspace are distinct task-owning S1 units for S2, while their joint organization has no evidenced single global S3. Positive S3 is limited to a parent and its child portfolio, including its supervised mode.

## Variety and escalation

Provider-selected tools, shell/file verbs, MCP, skills and multiple sessions amplify operational response variety. Approval gates, command effect classification, SQLite atomic claims, per-workspace board, child-depth/capacity limits, context checkpoint and cancel controls attenuate failure/conflict. Ambient messages notify parent of child completion/failure; the event channel alone does not prove higher-level algedonic governance.

## Evidence gaps

- Free Pascal 3.3.1 and required C-link toolchain are unavailable in this reviewer environment; no source build or upstream make check was executed. Source claims are limited to pinned code paths and shipped documentation.
- No live provider, SQLite race experiment or interactive operator spy session was executed; autonomy classification is an architectural/behavioral interpretation of reachable first-party code and its bundled tests.
- The S3* constructor finding does not establish a default independent auditor or systematic live audit verdict; it relies on the separate observer and operator corrective path. Same-runtime transcript provenance limits independence.
- Parent S3 operator takeover notice is best-effort; parent awareness can lag even though child detachment and the runtime command change authority.

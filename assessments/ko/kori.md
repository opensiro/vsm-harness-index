---
harness_id: kori
project_name: Kori
repository: https://github.com/FacileStudio/kori
review_ref: 960e7cb242a64f271afefbe194cf10926db00eca
reviewed_at: 2026-10-21
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Kori

**Proposed, not canonical:** the frozen [intake #860](https://github.com/opensiro/vsm-harness-index/issues/860) row 4 and [assessment batch #1842](https://github.com/opensiro/vsm-harness-index/issues/1842) support an included, first-party *assembled coding-agent product* with the proposed vector **S1=A / S2=— / S3=— / S3*=— / S4=— / S5=—**. The underlying Nacelle SDK is a separately owned dependency; this assessment credits only mechanisms wired into the shipped Kori executable and does not claim Kori authored Nacelle's agent-loop implementation.

## Review boundary

- System in focus: Kori's executable terminal/headless coding assistant and its owned configuration of provider, tool, model, TUI, session handling, optional parallel workers, approvals, project context, task-plan tooling, diagnostic checks and optional scheduled/remote runs.
- Purpose and identity: Deliver a user-directed, model-guided coding session with observable intermediate tool results and optional parallel research/exploration under a local operator's configured environment.
- Relevant environment: Local code repository, file and command tools, external model endpoints, user's terminal/IDE, optional remote targets, project-provided skills/hooks and MCP services, external Nacelle Go SDK.
- Standard-distribution boundary: The first-party Go binary assembled by `cmd/rune`-independent Kori-specific `cmd` and `internal/agent`/TUI modules, built with Nacelle v0.28.2. An explicit CLI/headless/IDE/remote/cron mode may contribute only through an actually shipped first-party path. At this pinned ref the module still declares github.com/FacileStudio/kori. GitHub presently redirects the frozen FacileStudio/kori repository identity to FacileStudio/bulle; the original frozen commit is available there. This is a repository **rename**, not a new source or repinning.
- Credited operating / distribution surfaces: `main.go`, `cmd/root.go`, `internal/agent/agent.go`, `internal/agent/runflags.go`, `internal/agent/headless.go`, `internal/agent/delegate.go`, `internal/agent/tools_main.go`, `internal/tui/run.go`, `internal/tui/parallel_detached.go`, `internal/agent/policy.go`, user-facing `README.md` and `docs/parallel-agents.md` where corroborated by wired source.
- Adjacent first-party surfaces excluded from ownership: design/proposed plans, repo CI/release machinery, SDK's internal uninstantiated features, independently installed model/tool/MCP behavior, developer coding/dogfood actions, build and benchmark scripts, and arbitrary end-user hooks. In particular, `docs/plan-matrix-chat.md` is not taken as deployment proof merely because a plan exists.
- First-party operating / deployment modes considered: local TUI, shipped headless invocation, opt-in terminal command and model-callable background delegation, task/diagnostic modes, configured cron/IDE integrations. Claimed S1 only requires the standard bundled coding-agent mode.
- Recursion level: The installed Kori coding-work application; concurrent delegated model tasks are work cells inside one user's session, not independently viable organizations by default.
- Reviewed revision: [FacileStudio/kori@960e7cb242a64f271afefbe194cf10926db00eca](https://github.com/FacileStudio/bulle/tree/960e7cb242a64f271afefbe194cf10926db00eca)
- Observation date: 2026-10-21
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

At the frozen revision [Kori's first-party build function](https://github.com/FacileStudio/bulle/blob/960e7cb242a64f271afefbe194cf10926db00eca/internal/agent/agent.go) selects a provider, assembles task/diagnostic/delegation tools, enforces chosen approval settings and constructs a `nacelle.Config` and `nacelle.New` agent. Nacelle handles the generic model/tool iteration; Kori owns the concrete installed coding interface, configuration, relevant tools and tool-event/feedback path. [Headless mode](https://github.com/FacileStudio/bulle/blob/960e7cb242a64f271afefbe194cf10926db00eca/internal/agent/headless.go) is wired separately; [TUI run](https://github.com/FacileStudio/bulle/blob/960e7cb242a64f271afefbe194cf10926db00eca/internal/tui/run.go) presents/receives execution events and interruptions.

[Parallel delegate wiring](https://github.com/FacileStudio/bulle/blob/960e7cb242a64f271afefbe194cf10926db00eca/internal/agent/delegate.go) registers an opt-in model-callable Nacelle parallel tool with `Detach: true`; [TUI detached fan-out](https://github.com/FacileStudio/bulle/blob/960e7cb242a64f271afefbe194cf10926db00eca/internal/tui/parallel_detached.go) starts subprocess-like nested agent tasks through Nacelle and routes results by batch/index back into displayed state. It can re-engage a main agent to synthesize results, but its channels and shared UI accounting are not automatically independent S1 coordination. [Diagnostic gate](https://github.com/FacileStudio/bulle/blob/960e7cb242a64f271afefbe194cf10926db00eca/internal/diagnostics/gate.go) runs configurable checks after editing; [policy constructor](https://github.com/FacileStudio/bulle/blob/960e7cb242a64f271afefbe194cf10926db00eca/internal/agent/policy.go) configures compaction. [Cron log](https://github.com/FacileStudio/bulle/blob/960e7cb242a64f271afefbe194cf10926db00eca/internal/agent/cronlog.go) records scheduled run outcomes; no whole-fleet decision is inherited from run telemetry.

The shipped [architecture document](https://github.com/FacileStudio/bulle/blob/960e7cb242a64f271afefbe194cf10926db00eca/README.md) explicitly describes Kori as Nacelle's first executable consumer and describes optional permissions and delegation; that ownership distinction is consistent with the build code. The frozen source was inspected; no Go runtime tests were executed on the available host, which lacks a Go compiler. Installed dependency functionality is credited only where its Kori-facing assembly/return is demonstrated.

## Operational model

In a standard session a human chooses a coding objective and supported operating mode; Kori resolves provider/settings, assembles the registered first-party coding tools and Nacelle-backed model loop, relays requests and tool results and offers interruption/approval. The model session chooses the next tool call from available tool definitions and observes responses. In the optional detached path, child tasks receive their own model-agent configuration and their results are identified and returned to the main TUI/agent. Parallelism and resource limits are configured; no automatic whole-system executive ownership or independent policy body is implied.

## S1 — Operations

- State: A
- Function: Perform open-ended, model-directed coding/investigation tasks through a first-party installed coding agent using file, shell (where enabled), web, MCP and project-context tools.
- Disturbance / variety regulated: Open-ended task requirements, evolving repository state, tool errors, tests, diagnosis and changing user instructions.
- Decisive decision or feedback right: The running model-agent chooses next tool actions, observes their outcomes and revises execution until an answer or stop condition; operator may gate individual effects.
- Decision owner: Model-directed Kori-assembled Nacelle `Agent` operating through shipped supported Kori tool and user-session paths; Nacelle owns generic loop implementation, not Kori's local configured task identity.
- Supporting / enforcement mechanisms: First-party `assemble` tool wiring, provider selection, Nacelle model/tool API, TUI/headless dispatcher, permissions, sessions, task tool, compaction, optional diagnostics and user hooks.
- Closure path: User coding request → Kori provider/tool/approval composition → Nacelle-backed agent proposes tool action → Kori-visible tool output/event → model observes output and acts or returns answer → Kori records/presents result.
- Boundary reachability: The shipped [builder](https://github.com/FacileStudio/bulle/blob/960e7cb242a64f271afefbe194cf10926db00eca/internal/agent/agent.go) executes `nacelle.New(cfg)`, while [TUI runner](https://github.com/FacileStudio/bulle/blob/960e7cb242a64f271afefbe194cf10926db00eca/internal/tui/run.go) and [headless runner](https://github.com/FacileStudio/bulle/blob/960e7cb242a64f271afefbe194cf10926db00eca/internal/agent/headless.go) expose the actual session. This is a product-wired agent path, not merely SDK example code.
- Why this is / is not agent-owned: With the configured model decision process removed, the Kori UI and registered tools do not choose open-ended source modifications or follow-up exploration. Kori has a working agent session through an external SDK, but the agent's task-semantic decisions occur in that instantiated first-party configuration.
- Evidence: [builder](https://github.com/FacileStudio/bulle/blob/960e7cb242a64f271afefbe194cf10926db00eca/internal/agent/agent.go); [TUI](https://github.com/FacileStudio/bulle/blob/960e7cb242a64f271afefbe194cf10926db00eca/internal/tui/run.go); [CLI](https://github.com/FacileStudio/bulle/blob/960e7cb242a64f271afefbe194cf10926db00eca/cmd/root.go); [README](https://github.com/FacileStudio/bulle/blob/960e7cb242a64f271afefbe194cf10926db00eca/README.md).
- Basis: explicit and structural
- Confidence: high for shipped executable assembly; no live model/provider effectiveness inferred
- Caveats: Nacelle is a genuine loop dependency; this assessment does not claim Kori independently implements the underlying generic engine. Shell availability and approvals depend on configuration.

## S2 — Coordination

- State: —
- Function: No first-party path was established that specifically attenuates actual or structurally demonstrated interference/oscillation **between distinct S1 coding work cells**, beyond generic asynchronous delegation/result routing.
- Disturbance / variety regulated: Concurrent child-agent work and possible collision on shared editor state, files, approvals and agent messaging.
- Decisive decision or feedback right: A qualifying S2 would detect/prevent an inter-S1 interference relation and return its resolution to affected sibling cells. Kori code principally launches *independent* subtasks and reassembles their outputs; it does not own a shown cross-child conflict or deconfliction judgment.
- Decision owner: No distinct first-party S2 owner identified. Nacelle owns the delegated agents' concurrency bounds; Kori's TUI controls detached output/display and the parent's subsequent synthesis.
- Supporting / enforcement mechanisms: `withParallelAgents`, concurrent Nacelle `DelegateParallel`, per-batch/index result channel, UI serialized update loop, user-message queue, optional cancellation and display spend accounting.
- Closure path: Child results return to the parent display or synthesis, but that is generic result aggregation. A supported sibling-contention→attenuation→changed competing S1 execution path was not established.
- Boundary reachability: No positive S2 claimed. The opt-in first-party [delegation tool](https://github.com/FacileStudio/bulle/blob/960e7cb242a64f271afefbe194cf10926db00eca/internal/agent/delegate.go) and [TUI result handler](https://github.com/FacileStudio/bulle/blob/960e7cb242a64f271afefbe194cf10926db00eca/internal/tui/parallel_result.go) are accessible, but coordinate reports and UI state, not an evidenced shared work conflict.
- Why this is / is not agent-owned: Scheduling independent jobs and rendering asynchronous messages are not function-specific S2 evidence without a concrete inter-S1 disturbance. User messages queued during a busy parent turn are a parent-input ordering concern, not interference between two autonomous task agents.
- Evidence: [parallel assembly](https://github.com/FacileStudio/bulle/blob/960e7cb242a64f271afefbe194cf10926db00eca/internal/agent/delegate.go); [fan-out](https://github.com/FacileStudio/bulle/blob/960e7cb242a64f271afefbe194cf10926db00eca/internal/tui/parallel_detached.go); [result handler](https://github.com/FacileStudio/bulle/blob/960e7cb242a64f271afefbe194cf10926db00eca/internal/tui/parallel_result.go); [delivery test](https://github.com/FacileStudio/bulle/blob/960e7cb242a64f271afefbe194cf10926db00eca/internal/tui/deliver_test.go).
- Basis: structural bounded negative
- Confidence: moderate
- Caveats: The SDK or externally configured worktree controllers may contain conflict controls, but they cannot be transferred into Kori without an evidenced shipped Kori operating path at this pinned boundary.

### Absence scope

- Surfaces inspected: Kori's first-party parallel delegate tool, detached launcher, shared update-loop/result handler, parent prompt queue/test and first-party description of parallel agents.
- Plausible first-party paths checked: Shared-file/worktree collision handling, exclusive child tool-approval arbitration, contention resolution between independently editing agents, restart/feedback changing competing children's subsequent execution.
- Why no material first-party path remains: The shipped first-party paths expose independent tasks and tagged result/synthesis, not a specific inter-S1 collision and attenuating feedback. Explicit parallel-implementation documentation notes no distributed file locks or agent worktrees in this TUI layer.

## S3 — Inside-and-now control

- State: —
- Function: No independently established whole-Kori current-control manager over multiple S1 units' collective resources, priorities, commitments or corrective tradeoffs.
- Disturbance / variety regulated: Multiple unfinished subtasks, diagnostic failures, scheduled sessions, tool approvals and resource expenditure.
- Decisive decision or feedback right: Choose current cross-work priorities or allocation based on a whole-organization situation view and return the choice into constituent S1 work.
- Decision owner: No demonstrated global executive agent or legitimate parent-regulated whole-system S3. Operators steer individual runs and configure caps; Kori presents updates and task-level controls.
- Supporting / enforcement mechanisms: TUI multiagent display, task plan, max-iterations, parallel concurrency caps, cron records, diagnostic gates, interrupt/cancel and operator session settings.
- Closure path: Session-local plan and task progress update the current task, not a sourced whole-current organizational resource/commitment decision feeding multiple independent S1 cells.
- Boundary reachability: No positive path credited; configured [parallel assembly](https://github.com/FacileStudio/bulle/blob/960e7cb242a64f271afefbe194cf10926db00eca/internal/agent/delegate.go) and [cron run records](https://github.com/FacileStudio/bulle/blob/960e7cb242a64f271afefbe194cf10926db00eca/internal/agent/cronlog.go) are included in inspected scope.
- Why this is / is not agent-owned: Model task planning, human steering and deterministic guards do not create a whole-system managerial owner.
- Evidence: [task-run assembly](https://github.com/FacileStudio/bulle/blob/960e7cb242a64f271afefbe194cf10926db00eca/internal/agent/agent.go); [parallel implementation](https://github.com/FacileStudio/bulle/blob/960e7cb242a64f271afefbe194cf10926db00eca/internal/tui/parallel_detached.go); [cron log](https://github.com/FacileStudio/bulle/blob/960e7cb242a64f271afefbe194cf10926db00eca/internal/agent/cronlog.go); [README](https://github.com/FacileStudio/bulle/blob/960e7cb242a64f271afefbe194cf10926db00eca/README.md).
- Basis: structural
- Confidence: moderate
- Caveats: Users may embed Kori sessions in higher-level organizations; those are not first-party installed current-control loops.

### Absence scope

- Surfaces inspected: Builder, session/TUI, task plan, optional parallel tool, schedule log and local intervention surfaces.
- Plausible first-party paths checked: Cross-agent performance/resource dashboard to decision owner to reprioritization, optional parent S3 mode, runtime cross-session arbitration of shared commitments.
- Why no material first-party path remains: The inspected operating paths own per-task execution and deterministic caps but do not source a whole-system managerial intervention loop returned to multiple S1 units.

## S3* — Complementary audit

- State: —
- Function: No sufficiently independent complement of normal S1/management reporting with a distinct audit finding and corrective whole-system return.
- Disturbance / variety regulated: False claims of coding success, failing tool/test runs and misleading session outcomes.
- Decisive decision or feedback right: Compare ordinary reporting with independent direct evidence and return corrective finding to current management.
- Decision owner: No distinct independent complementary auditor established in the shipped Kori installation. User-specified tests and optional diagnostics run in ordinary task workflow.
- Supporting / enforcement mechanisms: Post-edit diagnostic gate, source/tool results, session transcript, configurable hook trust, project tests and IDE event surfaces.
- Closure path: Diagnostic checks can produce findings or refuse an edit in the task, but a separate independent audit mandate/access and corrective management return is not evidenced.
- Boundary reachability: No positive audit path; configured diagnostics are a shipped per-edit gate rather than whole-organization independent S3* audit.
- Why this is / is not agent-owned: A deterministic post-edit check, a reviewer skill that users could install or a distinct background worker does not by itself give independent complementary audit authority.
- Evidence: [diagnostic gate](https://github.com/FacileStudio/bulle/blob/960e7cb242a64f271afefbe194cf10926db00eca/internal/diagnostics/gate.go); [builder](https://github.com/FacileStudio/bulle/blob/960e7cb242a64f271afefbe194cf10926db00eca/internal/agent/agent.go); [parallel result](https://github.com/FacileStudio/bulle/blob/960e7cb242a64f271afefbe194cf10926db00eca/internal/tui/parallel_result.go).
- Basis: structural bounded negative
- Confidence: moderate
- Caveats: Routine verification is visible; independence and correction of an S3 manager are not.

### Absence scope

- Surfaces inspected: Optional diagnostic hooks/gates, TUI model/tool events, parallel helper feedback and test references.
- Plausible first-party paths checked: A separate auditor inspecting real files independently of ordinary agent claims, corrective findings delivered into a distinct whole-current manager and returned changes to operation.
- Why no material first-party path remains: The checked path is per-edit deterministic QA and child-result synthesis; no independent complementary audit-to-S3 closure is installed.

## S4 — Outside-and-then intelligence

- State: —
- Function: No evidence of a shipped prospective outside-environment intelligence/adaptation loop that selects future capability changes and returns them into current Kori operation.
- Disturbance / variety regulated: Evolving tool/model availability, recurring incidents, newly required tasks and future operating constraints.
- Decisive decision or feedback right: Select a forward-looking adaptation option on new environmental evidence, approve/adopt it and alter future installed agent capability or organization.
- Decision owner: Human chooses provider/settings/tools and may write plugins/skills. Runtime compaction and diagnostic checks act on existing conversation/tool state rather than a future-directed capability adaptation choice.
- Supporting / enforcement mechanisms: Config, provider resolver, skill discovery, short-term context compaction, optional external compaction judge and cron scheduling/logging.
- Closure path: Kori reacts to present task results and user configuration. No first-party prospective selection→adoption→later capability modification closure or parent-governed S4 mode is established.
- Boundary reachability: No positive path; shipped [compaction policy](https://github.com/FacileStudio/bulle/blob/960e7cb242a64f271afefbe194cf10926db00eca/internal/agent/policy.go) and [scheduled-run state](https://github.com/FacileStudio/bulle/blob/960e7cb242a64f271afefbe194cf10926db00eca/internal/agent/cronlog.go) do not demonstrate S4.
- Why this is / is not agent-owned: Saving context and selecting provider under user configuration solve execution context, not future organizational intelligence.
- Evidence: [policy](https://github.com/FacileStudio/bulle/blob/960e7cb242a64f271afefbe194cf10926db00eca/internal/agent/policy.go); [settings](https://github.com/FacileStudio/bulle/blob/960e7cb242a64f271afefbe194cf10926db00eca/internal/agent/agent.go); [cron](https://github.com/FacileStudio/bulle/blob/960e7cb242a64f271afefbe194cf10926db00eca/internal/agent/cronlog.go).
- Basis: structural
- Confidence: moderate
- Caveats: No broad impossibility claim about future plugins or SDK capabilities.

### Absence scope

- Surfaces inspected: Model/provider settings, hooks/skills config, compaction and opt-in external judge, schedule logs, task execution, developer roadmap as adjacent.
- Plausible first-party paths checked: First-party outside-and-then signal collection, prospective modification proposal, legitimate adoption and return into subsequent installed runtime.
- Why no material first-party path remains: The observed mechanisms preserve context or configure a static run; no supported first-party adaptation loop of this function is wired.

## S5 — Policy and identity

- State: —
- Function: No first-party runtime identity/ultimate-policy governance body with a decisive policy revision right and return to Kori agent operations.
- Disturbance / variety regulated: Conflicts between agent activity, user goals and long-lived ultimate operating rules.
- Decisive decision or feedback right: Decide which ultimate policy/identity may govern Kori's organization and return its adopted outcome into future agent work.
- Decision owner: User/developer configures model, source root, approval policy, tools and skills; no first-party agent or separately constituted legitimate parent S5 owner/path is established.
- Supporting / enforcement mechanisms: Tool approvals, hook trust, environment/path restrictions, settings parsing, CLI flags and task-system prompts.
- Closure path: Operator config changes what a session may do; no explicit function-specific ultimate-policy decision and approved return-to-operation loop is installed.
- Boundary reachability: No positive function claim; session-local approvals and settings exist but are not a first-party S5 decision owner.
- Why this is / is not agent-owned: Security checks and user approvals enforce tool-use constraints; an installed coding assistant does not automatically decide its own organizational identity or host ultimate purpose.
- Evidence: [README](https://github.com/FacileStudio/bulle/blob/960e7cb242a64f271afefbe194cf10926db00eca/README.md); [builder](https://github.com/FacileStudio/bulle/blob/960e7cb242a64f271afefbe194cf10926db00eca/internal/agent/agent.go); [tool approvals](https://github.com/FacileStudio/bulle/blob/960e7cb242a64f271afefbe194cf10926db00eca/internal/agent/delegate.go).
- Basis: structural
- Confidence: moderate
- Caveats: End-user authority over one local task is not parent-mode VSM S5.

### Absence scope

- Surfaces inspected: Session/provider policy settings, permissions, hook trust, local/project modes, custom workflow and adjacent contributor governance.
- Plausible first-party paths checked: Legitimate identity-policy deliberation and approval by autonomous/parent function, accepted policy revision, and resulting operational enforcement beyond one tool authorization.
- Why no material first-party path remains: The shipped product has configured behavior constraints but not a distinct S5 policy decision/return structure.

## Distributed OSS parent arrangement

Kori's public repository, external Nacelle maintainer and users' own configured SDK/tool roles are not a documented distributed ultimate authority operating inside the shipped local coding runtime. The same source may be wrapped by organizations, but their separate VSM functions do not transfer into this assessment.

## Self-hosted and non-human modes

The local assistant can perform multi-step model-selected S1 actions in an operator's environment without requiring step-by-step task selection. Operator chooses initial task, credentials and permissions. Non-human S2/S3/S3*/S4/S5 ownership is not inferred from parallel agents, scheduling or generic SDK capabilities.

## Recursion

Subagents are lower-level coding work cells whose task outcomes feed the local parent session; nesting and a display showing many sessions are not automatically viable recursive organizations.

## Variety and escalation

Open-ended coding/task variety is handled through model/tool feedback. Errors and approvals can return to the user or task agent, but the evidence does not establish a separate organizational algedonic channel, executive current-control recursion or future strategic adaptation owner.

## Evidence gaps

- S2: Kori shows substantial parallel delegation and result collection but no concrete first-party collision attenuation across independent agent workspaces/commitments. A future **same-ref** finding of sibling resource/approval collision with returned resolution could revise the bounded `—`.
- SDK boundary: Nacelle v0.28.2 owns generic model/tool/delegation engines; the demonstrated Kori product assembly is enough for S1, but SDK-internal hypothetical functions are not donated to the assessed repository.
- Provenance: Kori's frozen original GitHub path now redirects to FacileStudio/bulle. Original catalog repository identity and immutable SHA are intentionally retained at proposal stage; verify canonical GitHub ID and redirects before admission.
- Verification: source inspection only; Go compiler absent on dev-alpha host, so **no** Kori Go test or live model execution is claimed. Index structural validation and GitHub CI are separate gates.

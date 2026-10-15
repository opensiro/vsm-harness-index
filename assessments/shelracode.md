---
harness_id: shelracode
project_name: ShelraCode
repository: https://github.com/Shelra/ShelraCode
review_ref: 45f87d1f7f71d5f6bba07405167893fa74d7c2a4
reviewed_at: 2026-10-12
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# ShelraCode

## Review boundary

- System in focus: installed ShelraCode TypeScript terminal/headless coding agent, its first-party model/tool runtime, autonomous objective kernel, optional isolated verification/sub-agent modes, durable session/memory/decision ledger and background scheduler.
- Purpose and identity: fulfill developer coding objectives using real file/shell/browser activity, staged acceptance and bounded verification/repair; optionally commission a separate verifier that inspects built/running artifacts.
- Relevant environment: user repository and build/tests, provider API and context, CLI/TUI/daemon schedules, project instructions and human-approved decisions, Shuru sandbox and browser when available, external documentation researched for a current coding task.
- Standard-distribution boundary: `src/agent`, `src/autonomy`, `src/verify`, `src/exec`, `src/daemon`, `src/tools` and core packaged CLI entrypoints. Installed self-contained code and enabled explicitly supported subagent/verification modes count; user-authored agents or independently deployed services are not imputed.
- Credited operating / distribution surfaces: [supported coding, autonomy and verify modes](https://github.com/Shelra/ShelraCode/blob/45f87d1f7f71d5f6bba07405167893fa74d7c2a4/README.md); [Agent and child runner](https://github.com/Shelra/ShelraCode/blob/45f87d1f7f71d5f6bba07405167893fa74d7c2a4/src/agent/agent.ts); [interactive task kernel](https://github.com/Shelra/ShelraCode/blob/45f87d1f7f71d5f6bba07405167893fa74d7c2a4/src/agent/kernel.ts); [autonomous composition root](https://github.com/Shelra/ShelraCode/blob/45f87d1f7f71d5f6bba07405167893fa74d7c2a4/src/autonomy/runtime.ts); [plan/act/verify/repair loop](https://github.com/Shelra/ShelraCode/blob/45f87d1f7f71d5f6bba07405167893fa74d7c2a4/src/autonomy/kernel.ts); [verify and UI auditor child briefs](https://github.com/Shelra/ShelraCode/blob/45f87d1f7f71d5f6bba07405167893fa74d7c2a4/src/agent/prompts.ts); [shipped verify child wiring](https://github.com/Shelra/ShelraCode/blob/45f87d1f7f71d5f6bba07405167893fa74d7c2a4/src/verify/orchestrator.ts); [verification recipe and evidence](https://github.com/Shelra/ShelraCode/blob/45f87d1f7f71d5f6bba07405167893fa74d7c2a4/src/verify/entrypoint.ts); [host evidence recognition](https://github.com/Shelra/ShelraCode/blob/45f87d1f7f71d5f6bba07405167893fa74d7c2a4/src/agent/verification-evidence.ts); [background delegation boundary](https://github.com/Shelra/ShelraCode/blob/45f87d1f7f71d5f6bba07405167893fa74d7c2a4/src/agent/delegations.ts); [scheduler](https://github.com/Shelra/ShelraCode/blob/45f87d1f7f71d5f6bba07405167893fa74d7c2a4/src/daemon/scheduler.ts); [reflection](https://github.com/Shelra/ShelraCode/blob/45f87d1f7f71d5f6bba07405167893fa74d7c2a4/src/memory/reflection.ts); [decisions ledger](https://github.com/Shelra/ShelraCode/blob/45f87d1f7f71d5f6bba07405167893fa74d7c2a4/src/ledger/store.ts).
- Adjacent first-party surfaces excluded from ownership: `.agents/skills/impeccable/` or other bundled third-party skill prompts not integrated as separate default control actors, `bench/`, `research/`, `docs/AUDIT-2026-09-23.md`, website/front-end and package release CI; these do not create an operating organizational owner. External `agent-desktop` and Shuru run as dependencies and are credited only through first-party invocation and feedback.
- First-party operating / deployment modes considered: normal interactive/headless coding; autonomous objective `--autonomous` with sequential task plan and repair; opt-in `/verify`/CLI `--verify` with dedicated verification model and isolated sandbox/browser feedback where platform permits; optional `ui-verify` reviewer subagent; foreground task and bounded read-only asynchronous delegate; recurring headless schedules; human-approval decision ledger and project memory.
- Recursion level: primary coding session is an operational S1; temporary task and verify children are separately executing task-level actors under the root. Scheduling independent prompts and retaining a task plan do not automatically make one continuously controlled worker organization.
- Reviewed revision: `45f87d1f7f71d5f6bba07405167893fa74d7c2a4`.
- Observation date: 2026-10-12.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

[Agent](https://github.com/Shelra/ShelraCode/blob/45f87d1f7f71d5f6bba07405167893fa74d7c2a4/src/agent/agent.ts) owns interactive model/tool turns and code editing, records real execution outcomes and host verification evidence, and returns failures into later coding decisions. The native [AutonomyKernel](https://github.com/Shelra/ShelraCode/blob/45f87d1f7f71d5f6bba07405167893fa74d7c2a4/src/autonomy/kernel.ts) independently exposes objective specification, an ordered task plan, file/shell changes, concrete acceptance checks, multiple bounded repair attempts, repeat-failure recognition and an honest blocked outcome. [runObjective](https://github.com/Shelra/ShelraCode/blob/45f87d1f7f71d5f6bba07405167893fa74d7c2a4/src/autonomy/runtime.ts) binds this to real subprocess/file/browser/HTTP tools and optional external research for the *current* objective. The host also marks tasks unverified when last-code real checks are missing or fail. This is substantial S1 task closure, not automatically system-wide S3 control.

[runTaskRequest](https://github.com/Shelra/ShelraCode/blob/45f87d1f7f71d5f6bba07405167893fa74d7c2a4/src/agent/agent.ts) spawns a child with its own messages, model/runtime and tool set for `explore`, `plan`, `general`, `verify`, `ui-verify` and other supported roles. For the explicit [runVerifyOrchestration](https://github.com/Shelra/ShelraCode/blob/45f87d1f7f71d5f6bba07405167893fa74d7c2a4/src/verify/orchestrator.ts) path, an independent `verify-detect` child inspects repository configuration, a `verify` child executes an independently prepared build/test/boot/browser recipe against the actual workspace within a separate Shuru environment, and results return to the root Agent and its kernel. [buildVerifyTaskPrompt](https://github.com/Shelra/ShelraCode/blob/45f87d1f7f71d5f6bba07405167893fa74d7c2a4/src/verify/entrypoint.ts) demands real build/run/browser interactions, screenshots and video rather than an untested model assertion. The built-in [ui-verify](https://github.com/Shelra/ShelraCode/blob/45f87d1f7f71d5f6bba07405167893fa74d7c2a4/src/agent/prompts.ts) child is separately instructed to audit rendered workspace against an explicit visual specification over several independent inspect/report passes. These explicit operating modes are platform/capability-gated, not assumed to run in every coding turn.

[DelegationManager](https://github.com/Shelra/ShelraCode/blob/45f87d1f7f71d5f6bba07405167893fa74d7c2a4/src/agent/delegations.ts) can start read-only background `explore` children and return written findings. The [SchedulerDaemon](https://github.com/Shelra/ShelraCode/blob/45f87d1f7f71d5f6bba07405167893fa74d7c2a4/src/daemon/scheduler.ts) launches time-triggered headless prompts, whereas [memory reflection](https://github.com/Shelra/ShelraCode/blob/45f87d1f7f71d5f6bba07405167893fa74d7c2a4/src/memory/reflection.ts) condenses previous local coding episodes into guarded suggestions. Human-approved project decisions in [decision ledger](https://github.com/Shelra/ShelraCode/blob/45f87d1f7f71d5f6bba07405167893fa74d7c2a4/src/ledger/store.ts) can add future enforcement checks to coding jobs. None of these by its name alone proves independent team coordination, whole-current managerial resource ownership, externally prospective adaptation, or ultimate organizational identity arbitration.

## Operational model

A model can autonomously pursue a coding objective through changed code and observed verification feedback. Child tool calls may improve one task; generic agent delegation and regular tests are not conflated with S2/S3 coordination or S3*. In explicit independently executed verify/UI-verify mode a distinct review model has a direct observational source (build, boot, test, browser/screenshot and source files) rather than relying solely on the producer's completion narrative; the parent consumes the report and can block/revise current work. Human approval of durable architectural decisions remains local authorization and test gating, not proof of constitutional S5 at the declared harness recursion.

## S1 — Operations

- State: A
- Function: Autonomously carry out uncertain coding changes with actual tool, test and environment feedback.
- Disturbance / variety regulated: Unknown code structure, failing tests/builds, incomplete requirements, changing local tool results, user edits and runtime failures.
- Decisive decision or feedback right: Root model selects coding tool/repair actions and re-evaluates observed tool/criterion evidence; in autonomous objective mode a model proposes plans and repairs subject to real host acceptance gates.
- Decision owner: First-party model-driven Agent and objective runtime; the fixed kernel and independent tools constrain completion but do not themselves decide the appropriate code change.
- Supporting / enforcement mechanisms: Tool registry, typed shell/file actions, host verification oracle, attempt cap, task acceptance criteria, source/memory context and session persistence.
- Closure path: User objective → model selects read/edit/test operation → host actually executes → environment result/acceptance witness returns → model repairs or reports verified/blocked outcome.
- Boundary reachability: Shipped interactive/headless command and `--autonomous` invoke installed Agent or AutonomyKernel with native tool execution and verification/repair controls.
- Why this is / is not agent-owned: Execution receipts cannot invent task-specific code decisions or repair strategies without the model; the model exercises the decisive operational discretion.
- Evidence: [Agent loop](https://github.com/Shelra/ShelraCode/blob/45f87d1f7f71d5f6bba07405167893fa74d7c2a4/src/agent/agent.ts); [runObjective](https://github.com/Shelra/ShelraCode/blob/45f87d1f7f71d5f6bba07405167893fa74d7c2a4/src/autonomy/runtime.ts); [autonomous repair loop](https://github.com/Shelra/ShelraCode/blob/45f87d1f7f71d5f6bba07405167893fa74d7c2a4/src/autonomy/kernel.ts); [first-party verification closure tests](https://github.com/Shelra/ShelraCode/blob/45f87d1f7f71d5f6bba07405167893fa74d7c2a4/src/agent/completion-gate.test.ts).
- Basis: explicit and structural
- Confidence: high for runtime design and gated feedback; this review does not reproduce a remote-model end-to-end run
- Caveats: Local model and platform availability matter; bounded retries can end with honest failure.

## S2 — Coordination

- State: —
- Function: No shipped function-specific mechanism attenuating observed conflict or oscillation among distinct operating S1 workers and returning corrected behavior to both was found.
- Disturbance / variety regulated: Simultaneous children could select overlapping files/tasks; concurrency and background scheduling create potential contention but not by themselves a coordinated feedback loop.
- Decisive decision or feedback right: Root model chooses child scopes; tools restrict background explore to read-only and kernel sequences objective tasks. No native inter-S1 conflict witness/arbitration decision is evidenced in supported modes.
- Decision owner: Root coding model for its own task; fixed sandbox and child nesting limits for execution safety.
- Supporting / enforcement mechanisms: Child role restrictions, detached explore process, optional skills and static/ordered planning, cancellation and job state.
- Closure path: Child calls execute and return reports to parent; no concrete two-worker conflict detection → coordination intervention → changed constraints returned to the affected S1 peers.
- Why this is / is not agent-owned: Read-only delegates, a queue of sequential tasks, execution restriction or a scheduler does not alone regulate actual S1-to-S1 interference.
- Evidence: [read-only background child manager](https://github.com/Shelra/ShelraCode/blob/45f87d1f7f71d5f6bba07405167893fa74d7c2a4/src/agent/delegations.ts); [child mode selection](https://github.com/Shelra/ShelraCode/blob/45f87d1f7f71d5f6bba07405167893fa74d7c2a4/src/agent/agent.ts); [sequential plan](https://github.com/Shelra/ShelraCode/blob/45f87d1f7f71d5f6bba07405167893fa74d7c2a4/src/autonomy/kernel.ts); [headless task scheduling](https://github.com/Shelra/ShelraCode/blob/45f87d1f7f71d5f6bba07405167893fa74d7c2a4/src/daemon/scheduler.ts).
- Basis: structural
- Confidence: medium-high in shipped modes
- Caveats: A custom user orchestration layer could implement coordination but lies outside the reviewed standard distribution.

### Absence scope

- Surfaces inspected: Child/subagent role enforcement, background jobs, sequential objective steps, daemon scheduler, project task plan.
- Plausible first-party paths checked: Distinct simultaneously operating S1 units, concrete witnessed interference, interference-specific decision, returned change to their subsequent work.
- Why no material first-party path remains: Reviewed standard controls prevent or limit work by design and return ordinary child reports; none is a first-party conflict-specific inter-S1 corrective circuit.

## S3 — Inside-and-now control

- State: —
- Function: No distinct whole-current managerial authority over a sustained plurality of operating S1s was demonstrated.
- Disturbance / variety regulated: Multiple project tasks, process/agent execution budgets and scheduled runs could require current organizational resource/priority arbitration; shipped code mainly organizes a single coder's objective or individual prompts.
- Decisive decision or feedback right: The coding model selects current steps, retries and delegates one bounded task; deterministic kernel controls time/budget and completion. There is no attributed manager deciding collective commitments across a continuously operating S1 portfolio.
- Decision owner: Single current-task root Agent, human operator for CLI/schedule/approvals, deterministic objective kernel for step gating; none owns a proved full-team current control loop.
- Supporting / enforcement mechanisms: AutonomyKernel task plan, project decision checks, daemon schedules, task/delegate tool, budget counters and persistent objectives index.
- Closure path: Task status/verification → coding agent changes next step. Missing whole-system worker/commitment observation → managerial allocation/intervention → feedback into multiple operating units.
- Why this is / is not agent-owned: A long plan, a task queue, stop/retry logic and a generic orchestrator named kernel still operate the single user's coding objective.
- Evidence: [objective kernel](https://github.com/Shelra/ShelraCode/blob/45f87d1f7f71d5f6bba07405167893fa74d7c2a4/src/autonomy/kernel.ts); [task phases](https://github.com/Shelra/ShelraCode/blob/45f87d1f7f71d5f6bba07405167893fa74d7c2a4/src/agent/kernel.ts); [recurring prompt scheduler](https://github.com/Shelra/ShelraCode/blob/45f87d1f7f71d5f6bba07405167893fa74d7c2a4/src/daemon/scheduler.ts); [independent child job](https://github.com/Shelra/ShelraCode/blob/45f87d1f7f71d5f6bba07405167893fa74d7c2a4/src/agent/delegations.ts).
- Basis: structural
- Confidence: medium-high; no first-party team-control operating contract found
- Caveats: Human can manage several separate requests, but this is not a shipped parent-controlled organizational S3 mode with an evidenced whole-team decision return.

### Absence scope

- Surfaces inspected: Autonomous multi-step objective, scheduled background prompts, progress index, generic child delegation, user approvals.
- Plausible first-party paths checked: Live whole-system resource/workforce view, distinct S3 current decision right and authoritative intervention returned across subordinate operational units.
- Why no material first-party path remains: Only per-objective progress and independent scheduling/dispatch without a live multi-S1 controller are wired as standard.

## S3* — Complementary audit

- State: A
- Function: In the explicit built-in verify and UI-verifier modes, independently inspect primary project/running-application artifacts and return a challenging evidentiary judgment to the coding controller.
- Disturbance / variety regulated: The implementing coder may mistakenly claim builds, tests or UI interactions worked without actually executing them, or may miss errors in rendered runtime behavior.
- Decisive decision or feedback right: A separate child model selects repository/build/test/boot/browser and UI observation actions, observes their actual outputs, then reports failures/evidence. The parent can prevent acceptance or revise work based on this returned verdict.
- Decision owner: Distinct provider-backed `verify` or `ui-verify` Agent in supported opt-in verification mode; deterministic host can apply sandbox/recipe and reject unsupported executions but does not choose the observed verdict.
- Supporting / enforcement mechanisms: runVerifyOrchestration, verify-detect recipe, Shuru sandbox, built-in screenshot/browser/command tools, child-context isolation, returned ToolResult and kernel verification/failed status.
- Closure path: Root code/reported success → dedicated child independently reads/executes a real project build/test/boot/browser or examines rendered UI → evidence-bearing pass/fail/artifact report → parent Agent/kernel records verification and can block completion or choose repairs.
- Boundary reachability: Shipped `/verify`/`--verify` path creates real separate `verify` child through `runVerifyOrchestration` and `runTaskRequest`; `ui-verify` has its own built-in model prompt and inspection tools. Both are supported distribution modes, gated by required Shuru/browser platform where applicable.
- Why this is / is not agent-owned: The independently executing reviewer model collects and interprets real source/runtime observations; passive test status or producer self-report alone is not the positive evidence.
- Claim being audited: The implementing coding agent's claim that the requested change works and, for UI verification, that the rendered workspace meets the visual expectation.
- Ordinary reporting path: Main Agent's own tool transcript, completion statements, acceptance criteria and host verification recognizer.
- Complementary access path: Separate verify Agent directly executes installation/build/tests/boot and browser smoke interactions in sandbox; UI-verifier examines rendered state and screenshot/source evidence instead of only summary text.
- Independence boundary: Fresh child messages/context and sandboxed/isolated tool execution with its own reviewer brief; this is a first-party operationally separate evidence path, not a cryptographically blinded review.
- Who acts on findings: Parent coding agent/kernel receives the ToolResult, records failure/verification status and may issue further code repair, or reports that verification did not succeed.
- Evidence: [prepare and run independent verify](https://github.com/Shelra/ShelraCode/blob/45f87d1f7f71d5f6bba07405167893fa74d7c2a4/src/verify/orchestrator.ts); [verified source/build/boot/browser requirements](https://github.com/Shelra/ShelraCode/blob/45f87d1f7f71d5f6bba07405167893fa74d7c2a4/src/verify/entrypoint.ts); [child creation and root verify feedback](https://github.com/Shelra/ShelraCode/blob/45f87d1f7f71d5f6bba07405167893fa74d7c2a4/src/agent/agent.ts); [separate built-in reviewer prompts](https://github.com/Shelra/ShelraCode/blob/45f87d1f7f71d5f6bba07405167893fa74d7c2a4/src/agent/prompts.ts); [/verify and --verify mode](https://github.com/Shelra/ShelraCode/blob/45f87d1f7f71d5f6bba07405167893fa74d7c2a4/README.md).
- Basis: explicit and structural
- Confidence: medium-high for optional reality-sampling mode; source-level reachability is clear, but execution cannot be inferred when Shuru is unsupported
- Caveats: Verify is opt-in and platform-gated; ordinary same-model requirement audit within Agent completion gate is not credited as independent S3*. No claim of a guaranteed correct or producer-blind reviewer verdict.

## S4 — Outside-and-then intelligence

- State: —
- Function: No first-party continuing outside-and-future intelligence process choosing organizational adaptation options with returned change in whole-current capability is evidenced.
- Disturbance / variety regulated: External packages/APIs and future project requirements can evolve, but normal web research is recruited to the present coding task, while memory reflection derives from past local execution.
- Decisive decision or feedback right: Agent chooses current-task research and writes changes; memory reflection model may propose local facts/skills, with deterministic promotion/human involvement. No distinct future-environment option selector owns a strategic adoption decision.
- Decision owner: Active coding S1 for present work; human for manual skill promotion/config; no S4 organizational controller.
- Supporting / enforcement mechanisms: Web search/open, project episodic memory, gated reflection, skills compiler and local decision ledger.
- Closure path: Current request/previous code outcomes → present project research or local reusable note → future prompt/tool context. Missing prospectively sensed external change, alternative capability appraisal and explicit S4→S3 adoption feedback.
- Why this is / is not agent-owned: Learning from local historical tool outcomes and maintaining skills improve S1 and do not, by themselves, model a changing outside-and-then environment.
- Evidence: [experience reflection](https://github.com/Shelra/ShelraCode/blob/45f87d1f7f71d5f6bba07405167893fa74d7c2a4/src/memory/reflection.ts); [memory consolidation](https://github.com/Shelra/ShelraCode/blob/45f87d1f7f71d5f6bba07405167893fa74d7c2a4/src/memory/consolidate.ts); [research for current task](https://github.com/Shelra/ShelraCode/blob/45f87d1f7f71d5f6bba07405167893fa74d7c2a4/src/autonomy/runtime.ts); [web evidence](https://github.com/Shelra/ShelraCode/blob/45f87d1f7f71d5f6bba07405167893fa74d7c2a4/src/research/web.ts).
- Basis: structural
- Confidence: medium-high in shipped modes
- Caveats: A separately commissioned future research task or manually updated toolset could be part of an external S4 system, not evidenced here.

### Absence scope

- Surfaces inspected: External web research, memory consolidation/skill promotion, tool/provider routing, autonomous objective planner, project decisions.
- Plausible first-party paths checked: Continuing environmental horizon sensing, modeled future options, adoption decision and return to whole-current organizational capability.
- Why no material first-party path remains: These paths update ordinary coding context or present-task action; they do not carry a dedicated external-prospective adaptation decision and S3 feedback relation.

## S5 — Policy and identity

- State: —
- Function: No ultimate identity-purpose policy arbiter balancing whole-current and future-facing organizational demands at the declared harness recursion is demonstrated.
- Disturbance / variety regulated: Human-approved project ADRs, safety approval and secrets restrictions constrain implementation, but do not necessarily govern the autonomous coding organization's constitutional identity.
- Decisive decision or feedback right: Human approves/rejects local architectural decisions and controls permissions; running agent checks globs/commands to prevent incompatible project edits. This is protected work policy, not shown as a legitimate S5 organization-level purpose arbitration.
- Decision owner: External human project owner for decisions; deterministic ledger/check tools enforce them in future coding tasks.
- Supporting / enforcement mechanisms: Persistent decisions ledger, approve/supersede lifecycle, glob-scoped checks, user credential policies and command sandbox.
- Closure path: Operator-approved project technical decision → ledger check guards the next code edit/acceptance; absent distinct organizational S3/S4 policy conflict and supreme identity arbiter with binding return into whole-system policy.
- Why this is / is not agent-owned: Human approval makes a binding project design constraint but not automatically VSM S5 constitutional control. No running Agent owns ultimate purpose.
- Evidence: [project decision persistence](https://github.com/Shelra/ShelraCode/blob/45f87d1f7f71d5f6bba07405167893fa74d7c2a4/src/ledger/store.ts); [decision checking](https://github.com/Shelra/ShelraCode/blob/45f87d1f7f71d5f6bba07405167893fa74d7c2a4/src/ledger/judge.ts); [operator approve/supersede path](https://github.com/Shelra/ShelraCode/blob/45f87d1f7f71d5f6bba07405167893fa74d7c2a4/README.md); [decision gate](https://github.com/Shelra/ShelraCode/blob/45f87d1f7f71d5f6bba07405167893fa74d7c2a4/src/agent/agent.ts).
- Basis: explicit and structural
- Confidence: medium-high
- Caveats: Institutional software governance may define S5 externally; no operational link to a first-party S3–S4 metasystem is shown.

### Absence scope

- Surfaces inspected: Human decision approvals, scoped architecture checks, product identity text, provider policy, sandbox permissions.
- Plausible first-party paths checked: Ultimate organizational purpose/identity tension, legitimate deciding authority and returned whole-system policy balance across current and future.
- Why no material first-party path remains: Only project-level design constraints and tool permissions are closed; no independent organization-identity adjudication is established.
## Recursion

Default interactive and autonomous objective mode constitute a single viable coding S1 with bounded task children. Generic subagents, long task plans and scheduled independent jobs do not automatically form a coordinated/current-controlled organization at a higher recursion. In explicitly invoked verify/UI-verify mode a fresh child Agent is an evidentiary reviewer of the original coder's real output; its independent artifact/behavior access, not its class name, supports the bounded S3* mapping.

## Variety and escalation

Tool failures and test/build evidence return to the main coding model; bounded retries can trigger blocked/fail-closed terminal states instead of fabricated success. For optional verify mode, real sandbox/build/browser failures are interpreted by a separate review actor and returned to the host Agent/kernel to affect current code acceptance and repair. An unverified status label, a scheduled job or a project ADR alone is not an algedonic or higher-VSM function without the corresponding decision authority.

## Evidence gaps

- Assessed at the original immutable Git SHA using code and shipped operating documentation; no paid-model/live Shuru macOS validation trace has been reproduced by this reviewer.
- S3*=A is **only** credited to the expressly supported independent `verify`/`ui-verify` source-inspection mode, not the ordinary single-model verification round or automatic after-every-task audit. Its accessibility depends on Shuru/platform and mode enablement.
- The `reviewPassed` kernel flag by itself is not independent review evidence. The positive path is the actual separate Agent with source/build/browser access and return into the parent.
- No S2, S3, S4 or S5 is inferred from naming an orchestrator/ledger, background schedules, generic tool hooks or optional third-party skills.

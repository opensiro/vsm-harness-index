---
harness_id: ai-coding-agents-orchestrator
project_name: AI Coding Agents Orchestrator
repository: https://github.com/Open-Makers/ai-coding-agents-orchestrator
review_ref: 1c1185c6f323bf3475c3847e38245276852ebc5e
reviewed_at: 2026-10-25
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# AI Coding Agents Orchestrator

## Review boundary

- System in focus: One installed first-party Open-Makers coding-project orchestrator run, with a PM agent, Coder, QA, UX reviewer and Security reviewer, source-reading reviewers, bounded task-plan and remediation loops, local workspace and human artifact gates. It is **not** the Open-Makers contributor organization or the Claude/Codex/LM Studio/external runner vendor's internal agent architecture.
- Purpose and identity: Negotiate a requested software change, plan its sub-tasks, implement and test it, independently challenge defects and organize bounded rework until a deliverable can be returned.
- Relevant environment: User requirements/approval, real repository files/build output/tests, runtime errors, QA/security findings, incomplete dependencies, memory/review context and provider availability.
- Standard-distribution boundary: Shipped `cmd/orchestrator` construction, `internal/orchestrator/TaskRunner`, distinct Go first-party roles in `internal/agent`, actual local source-read/context and tool/test invocation, installed provider runners, `beads` optional state, workspace artifacts and TUI approval gates. Provider weights and external CLI agent internals remain external; Go code itself assembles model-backed role decisions and enforces their return paths.
- Credited operating / distribution surfaces: [standard agent construction](https://github.com/Open-Makers/ai-coding-agents-orchestrator/blob/1c1185c6f323bf3475c3847e38245276852ebc5e/cmd/orchestrator/main.go#L430-L483), [task-runner lifecycle](https://github.com/Open-Makers/ai-coding-agents-orchestrator/blob/1c1185c6f323bf3475c3847e38245276852ebc5e/internal/orchestrator/task_runner.go#L185-L485), [PM review arbitration](https://github.com/Open-Makers/ai-coding-agents-orchestrator/blob/1c1185c6f323bf3475c3847e38245276852ebc5e/internal/agent/pm.go#L508-L605), [QA source/test verification](https://github.com/Open-Makers/ai-coding-agents-orchestrator/blob/1c1185c6f323bf3475c3847e38245276852ebc5e/internal/agent/qa.go#L103-L285), [Security independent source review](https://github.com/Open-Makers/ai-coding-agents-orchestrator/blob/1c1185c6f323bf3475c3847e38245276852ebc5e/internal/agent/security.go#L15-L115), [independent raw source reader](https://github.com/Open-Makers/ai-coding-agents-orchestrator/blob/1c1185c6f323bf3475c3847e38245276852ebc5e/internal/agent/source_context.go#L34-L143).
- Adjacent first-party surfaces excluded from ownership: Repository CI/test fixtures, developer issues/contributions, optional telemetry shadow measurement, documentation/screenshots, benchmark samples and any externally run agent/tool chain not invoked by this standard TaskRunner. Go unit tests are validation of source-path existence, not themselves observed live LLM quality.
- Supported modes considered: Normal negotiated green/brown/fix task pipelines, optional R&D/PoC path, persisted/restartable work, optional beads execution with in-order fallback, configured model runners, independent QA/UX/security review, bounded PM arbitration, human artifact approval and bounded QA test-verification escalation. Positive S3/S3* claims apply to the integrated implementation/review modes, **not** the reduced R&D path.
- Recursion: One coding project/task's continuing implementation/review run with multiple operational roles; not a multi-project company or each spawned model vendor's own recursion.
- Frozen review: `Open-Makers/ai-coding-agents-orchestrator@1c1185c6f323bf3475c3847e38245276852ebc5e`, recorded in [discovery #2036](https://github.com/opensiro/vsm-harness-index/issues/2036) / serial [batch #2037](https://github.com/opensiro/vsm-harness-index/issues/2037). Observed 2026-10-25; Profile 0.2.4 / Methodology 0.3.7.

## Repository architecture

`main.go` installs distinct PM, Coder, QA, UX and Security agents with configured model-backed runners. `TaskRunner` negotiates a task with a human, asks PM to split it into sub-tasks, routes tests/implementation/build through QA and Coder, and then sends *source files* separately to QA, UX and Security. PM receives their feedback, decides pass versus blocking fixes, creates new sub-task beads and repeats execution/review within fixed iteration limits. This is an installed decision-return chain, not merely a list of named agents. [role wiring](https://github.com/Open-Makers/ai-coding-agents-orchestrator/blob/1c1185c6f323bf3475c3847e38245276852ebc5e/cmd/orchestrator/main.go#L436-L482); [review → PM → new tasks loop](https://github.com/Open-Makers/ai-coding-agents-orchestrator/blob/1c1185c6f323bf3475c3847e38245276852ebc5e/internal/orchestrator/task_runner.go#L433-L501).

The execution phase generates QA tests and later coder implementation over a shared worktree; a project-wide build/test loop tries coder repairs and, after repeated failure, asks QA to inspect actual test/source files and decide if tests are wrong or the coder must continue fixing. The correctness dispute is a specific QA↔Coder work-product incompatibility. `qualityReview` meanwhile assembles fresh code context from the filesystem independently of the Coder's own result message; raw code and test output are evaluated by dedicated reviewer roles, with a corrective return through PM. [test/coder conflict resolution](https://github.com/Open-Makers/ai-coding-agents-orchestrator/blob/1c1185c6f323bf3475c3847e38245276852ebc5e/internal/orchestrator/task_runner.go#L1091-L1175); [quality review roles](https://github.com/Open-Makers/ai-coding-agents-orchestrator/blob/1c1185c6f323bf3475c3847e38245276852ebc5e/internal/orchestrator/task_runner.go#L1179-L1270).

## Operational model

Distinct S1 units produce project negotiation/plans, test artifacts, source modifications and review reports using their own model-backed Go agent implementations. The Coder executes implementation and fixes; QA produces tests and separate review; PM negotiates/decomposes and makes current corrective prioritization decisions; Security and UX independently inspect current sources. Runtime code handles artifact gates, caps and status transitions. The human grants task/spec/plan permission; ordinary approvals do not govern ultimate organizational identity by themselves.

## S1 — Operations

- State: A
- Function: Interpret a coding task, produce/test/edit source files and deliver model-mediated QA/implementation results within the active project.
- Disturbance / variety regulated: User goals, repository structure, compiler/test diagnostics, code changes, alternative implementation paths and failures under active work.
- Decisive decision or feedback right: Model-backed Coder decides concrete implementation/fix content from specifications and current source/test observations; QA chooses test content; PM develops an actionable decomposition. Actual code/test outputs feed later work.
- Decision owner: The first-party configured and invoked Go model-backed agents and their separate `runner.LLMRunner`s, assembled by standard main and TaskRunner. External model inference/vendor process logic is a dependency, not assigned independent organizational governance.
- Supporting / enforcement mechanisms: Local workspace/artifact stores, test executor, context source collection, role-specific prompts, optional beads dependency claims, budgets, bounded retries, event bus, source writes and human task gates.
- Closure path: User task → PM negotiation/approved spec → model-produced sub-tasks → QA-generated tests / Coder source work and build results → model-driven fixes → audited deliverable/status.
- Boundary reachability: `cmd/orchestrator/main.go` instantiates all roles; `TaskRunner.run` directly calls `executeBeads` and `implementBead`, which route to real model-backed role agents and workspace mutation; no custom downstream operator needs to implement the actor loop for normal use.
- Why this is / is not agent-owned: Without model role decisions the program can copy artifacts, enforce test bounds and sequence phases but cannot interpret arbitrary coding goals or choose implementation actions. This is first-party assembled autonomous S1, not evidence of first-party model weights.
- Evidence: [standard role setup](https://github.com/Open-Makers/ai-coding-agents-orchestrator/blob/1c1185c6f323bf3475c3847e38245276852ebc5e/cmd/orchestrator/main.go#L436-L481); [subtask execution and actual code fixes](https://github.com/Open-Makers/ai-coding-agents-orchestrator/blob/1c1185c6f323bf3475c3847e38245276852ebc5e/internal/orchestrator/task_runner.go#L870-L1175); [first-party role-specific QA inference](https://github.com/Open-Makers/ai-coding-agents-orchestrator/blob/1c1185c6f323bf3475c3847e38245276852ebc5e/internal/agent/qa.go#L220-L264).
- Basis: Standard first-party model/role/workspace feedback paths; no live model-effectiveness test.
- Confidence: High for program structure, no empirical success claim.
- Caveats: Model/provider is external; the unsupported absence of a provider prevents a live session but not a shipped standard model-backed mode.

## S2 — Coordination

- State: A
- Function: Resolve a concrete inter-S1 incompatibility between QA-authored tests and Coder-authored source, preventing unproductive coder-fix versus test-requirement oscillation in the active project.
- Disturbance / variety regulated: The coder may repeatedly fail QA-generated tests either because code is wrong or because test assumptions are incorrect; retrying only the coder can cause persistent interference between independent work products.
- Distinct S1 units: `QAAgent` creates actual test files, and `CoderAgent` produces implementation/fixes; both are separately instantiated role actors and output into the same project.
- Inter-S1 disturbance: `globalBuildFix` observes repeated build/test failure and escalates to QA to discriminate incorrect tests from deficient code. The origin is concrete incompatible code/test artifacts, not mere parallel invocation.
- Attenuating coordination relation: `QAAgent.VerifyTests` reopens production-source/test files via `safefile.ReadFile`, judges test correctness, and either returns `TestsOK` (force coder to retry its side) or emits updated test files (repair the QA side). The harness merges changed paths and resumes coder fixes.
- Feedback into subsequent S1 behaviour: `UpdatedFiles` are written to the worktree and merged into the files passed to the next Coder fix; a `TestsOK` response records that QA's tests should stand and Coder work must continue. Retry/QA-verification caps prevent endless cycling.
- Decisive decision or feedback right: A separate model-backed QA role owns the distinction between valid and faulty tests, specifically at the cross-unit conflict boundary. Deterministic counters/escalation trigger and file merge enforce that judgment.
- Decision owner: Autonomous first-party `QAAgent` configured by standard main; no external human must personally judge each test-versus-code conflict in the normal path.
- Supporting / enforcement mechanisms: `defaultMaxCoderAttempts`, `maxQAVerifyRounds`, test reports, separate QA role prompt, source file reader and updated-file parser/writer.
- Closure path: QA tests + coder implementation → actual failed build/test loop → QA model reads both sides and chooses retain/fix tests → changed files / judgment return to coder → renewed build/test execution.
- Boundary reachability: Standard `globalBuildFix` is invoked after the implementation of all sub-tasks; it calls installed QA agent's `VerifyTests` after bounded failed attempts. This is not a generic queue or hypothetical coordination extension.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The logic explicitly recognizes a disagreement between separate S1-produced artifacts, invokes a function-specific adjudication to identify which side is wrong and feeds the outcome back into their subsequent work. The fixed number of attempts is mere enforcement, not the S2 ownership proof.
- Why this is / is not agent-owned: Remove the QA model judgment and only retries/fail counts remain; the code no longer decides whether to rewrite tests or require implementation correction. This narrow S2 right is model-owned (`A`), not inferred from the orchestrator name.
- Evidence: [QA TDD, Coder and escalation](https://github.com/Open-Makers/ai-coding-agents-orchestrator/blob/1c1185c6f323bf3475c3847e38245276852ebc5e/internal/orchestrator/task_runner.go#L1039-L1175); [independent QA source and test verdict](https://github.com/Open-Makers/ai-coding-agents-orchestrator/blob/1c1185c6f323bf3475c3847e38245276852ebc5e/internal/agent/qa.go#L103-L192).
- Basis: Concrete first-party inter-S1 artifact conflict + autonomous resolution + operational return.
- Confidence: Medium-high for installed path; no claim QA's judgment is factually correct.
- Caveats: QA authored the tests it evaluates, so this narrow coordination decision is **not** itself the independent S3* audit witness. Other cross-agent resource contention and infinite loop avoidance are not inferred from it.

## S3 — Inside-and-now control

- State: A
- Function: Govern the currently approved project implementation as a whole by judging multi-reviewer feedback, deciding actionable commitments and directing new corrective sub-tasks to the active work cells.
- Disturbance / variety regulated: Aggregate QA, UX and Security defects threaten the deliverable after ordinary coder completion; individual workers cannot decide which whole-project issues are blocking versus deferrable.
- Whole-system current view: `TaskRunner` retains approved spec, task plan/sub-task beads, implementation status, current source files and QA/UX/Security review feedback. The PM arbitration call receives all three reviewer channels in one input and can distinguish current blockers from nice-to-haves.
- Current-control decision scope: PM model decides pass versus real fixes, `NiceToHave` deferral and new remediation `SubTasks`/review scope; `TaskRunner` replaces the next iteration's active tasks with these sub-tasks, creates new beads and reruns implement+review.
- Decisive decision or feedback right: A model-backed PM `ArbitrateAll` deliberates the current global review state and selects the next project-wide commitments; the Go loop limits iteration count and applies task allocations but does not choose which findings warrant fixes.
- Decision owner: First-party configured autonomous PM role, invoked in normal green/brown/fix implementation+review pipelines. Human approves initial scope/spec/plan but does not own each automated PM remediation choice in that mode.
- Supporting / enforcement mechanisms: Shared task/artifact store, beads and dependency tracking, QA/UX/security reports, fix-round counter, `maxArbitrateIterations`/`maxFixIterations`, event/status and branch/file outcome recording.
- Closure path: Complete work across sub-tasks → code-reality review by QA/UX/Security → PM verdict → fresh sub-tasks/beads → Coder/QA perform remediations → new whole-project review until pass/cap.
- Boundary reachability: `implementAndReview` is called by the shipped `run` for standard green/brown/fix pipelines. Its `pm.ArbitrateAll` result is directly consumed to rewrite the task list for the next execution loop. Reduced R&D mode is explicitly excluded from this claim.
- Why this is / is not agent-owned: If PM is removed, `TaskRunner` takes a permissive "accepting review as pass" fallback; no autonomous whole-project prioritization remains. Model PM owns the substantive current-control judgment, not the deterministic iterator.
- Evidence: [run modes and user gates](https://github.com/Open-Makers/ai-coding-agents-orchestrator/blob/1c1185c6f323bf3475c3847e38245276852ebc5e/internal/orchestrator/task_runner.go#L320-L452); [PM remediation feedback loop](https://github.com/Open-Makers/ai-coding-agents-orchestrator/blob/1c1185c6f323bf3475c3847e38245276852ebc5e/internal/orchestrator/task_runner.go#L455-L525); [autonomous PM arbitration call/parser](https://github.com/Open-Makers/ai-coding-agents-orchestrator/blob/1c1185c6f323bf3475c3847e38245276852ebc5e/internal/agent/pm.go#L508-L606).
- Basis: Positive installed current-plan/review → discretionary new commitments → execution return.
- Confidence: Medium-high for structural model-owned intervention, no runtime effectiveness assertion.
- Caveats: Whole-system is the one active coding-project/task recursion, not all projects of the OSS maintainer organization. Human approval of task scope is an operational gate, not a separate evidenced S3 parent-owned mode.

## S3* — Complementary audit

- State: A
- Function: Supply complementary raw-code reality to challenge normal Coder-produced outputs and return actionable independent defects to the current PM control loop.
- Disturbance / variety regulated: Coder might report completion or pass its internal checks while source contains correctness, security or UX defects that routine coder reporting does not reveal.
- Claim being audited: Coder's claim that implemented project files and a passing ordinary build/test phase are sufficiently correct and safe for acceptance.
- Ordinary reporting path: Coder returns implementation files/build outcome through its first-party role and normal TaskRunner status; the project may otherwise be marked implemented after a build loop.
- Complementary access path: Independently instantiated Security/QA/UX reviewer roles receive actual *filesystem-read* project source context assembled by `buildCompactSourceContext`, plus test-result artifacts. This is different access from accepting the Coder's completion text. Source context is bounded/truncated; if no source is available, a fallback to raw Coder output weakens independence and is **not** the positive basis.
- Decisive decision or feedback right: Dedicated model-backed Security and QA review agents inspect the code and judge `Approved` versus concrete `MustFix`; Security does not implement the Coder change in this path. QA may also generate tests elsewhere, but Security's separate source-reading role anchors the independent code-audit claim.
- Decision owner: Separate first-party model-backed reviewer role(s), with dedicated prompts and source read permissions; audit judgments remain autonomous while Go transport and parsing are deterministic.
- Closure path: Actual files → independent role review → reviewer `MustFix`/unparsed concern → `qualityReview` channels → PM `ArbitrateAll` → accepted blocking issues become new remediation sub-tasks → coder changes real files and subsequent reviewers recheck.
- Who acts on findings: The separately modeled PM agent decides which reviewer defects become blocking new sub-tasks, while Coder implements fixes and reviewers subsequently revisit the changed sources.
- Supporting / enforcement mechanisms: `safefile.ReadFile`, import/caller context expansion, source/test artifacts, separate role agents and logs, fixed iteration caps and parse-to-feedback mapping.
- Independence boundary: Security is created separately from Coder and reads code anew from workspace paths. This is independent **with respect to ordinary Coder-produced success claims**, though it shares project/operator configuration and model provider infrastructure. It is not a statistically independent outcome study.
- Boundary reachability: Standard `main.go` creates Security and QA roles independently from Coder; normal `qualityReview` after implementation invokes those agents with actual project file paths and routes their returned results to PM arbitration.
- Why this is / is not agent-owned: Remove separate reviewer cognition and only source ingestion and deterministic status remain. The auditor's qualitative distinction among must-fix and acceptable code is model-owned, while PM separately owns corrective prioritization, preserving roles.
- Evidence: [default separate agents](https://github.com/Open-Makers/ai-coding-agents-orchestrator/blob/1c1185c6f323bf3475c3847e38245276852ebc5e/cmd/orchestrator/main.go#L454-L481); [independent source reader](https://github.com/Open-Makers/ai-coding-agents-orchestrator/blob/1c1185c6f323bf3475c3847e38245276852ebc5e/internal/agent/source_context.go#L34-L143); [Security raw source versus coder-output fallback](https://github.com/Open-Makers/ai-coding-agents-orchestrator/blob/1c1185c6f323bf3475c3847e38245276852ebc5e/internal/agent/security.go#L54-L110); [audit-to-PM corrective return](https://github.com/Open-Makers/ai-coding-agents-orchestrator/blob/1c1185c6f323bf3475c3847e38245276852ebc5e/internal/orchestrator/task_runner.go#L455-L520).
- Basis: Source-first alternative evidence + dedicated autonomous independent reviewer + distinct S3 return.
- Confidence: Medium. Actual raw-source availability and result correctness were not measured; independence is structural and claim-relative.
- Caveats: QA test-author reviewing its own tests is not counted as independently auditing itself; the positive witness is Security and distinct reviewer raw-code inspection of Coder-produced material. Mandatory QA in the ordinary production chain would not alone establish S3*: the dedicated source-read and PM corrective return are decisive here.

## S4 — Outside-and-then intelligence

- State: —
- Function: No standing environment/future scanning → adaptation-option judgment → return into currently deployed organizational capability is established.
- Disturbance / variety regulated: Evolving dependency vulnerabilities, new coding models, project needs and future tool capabilities could require adaptation, but inspected loops address a currently approved task or update ordinary memory.
- Decisive decision or feedback right: PM R&D path can explore user-specified PoCs and memory persists lessons; no autonomous role is shown deciding the orchestrator's prospective capability policy based on external future-relevant distinctions and returning it to S3 as an adaptation decision.
- Decision owner: User for selecting model/configuration and proposing future projects, PM/Coder for the present R&D or implementation task.
- Supporting / enforcement mechanisms: `CollectMemory`, finalise-memory hooks, model config/provider fallback, project-context collection and R&D PoC loops.
- Closure path: Memory can inform next user task and PM may produce a PoC, but no ongoing future-environment model selects a new capability program and installs it in present operating policy.
- Why this is / is not agent-owned: Project-specific innovation, memory storage and re-running task-review do not independently constitute S4 external-prospective strategy.
- Evidence: [project context and recalled memory](https://github.com/Open-Makers/ai-coding-agents-orchestrator/blob/1c1185c6f323bf3475c3847e38245276852ebc5e/internal/orchestrator/task_runner.go#L251-L325); [R&D task PoC loop](https://github.com/Open-Makers/ai-coding-agents-orchestrator/blob/1c1185c6f323bf3475c3847e38245276852ebc5e/internal/orchestrator/task_runner.go#L599-L692); [task completion/memory](https://github.com/Open-Makers/ai-coding-agents-orchestrator/blob/1c1185c6f323bf3475c3847e38245276852ebc5e/internal/orchestrator/task_runner.go#L420-L444).
- Basis: Bounded negative.
- Confidence: Medium-high.
- Caveats: A user could explicitly order future-oriented research, but this is a bounded S1 project goal until an operating capability-adaptation loop is shown.

### Absence scope

- Surfaces inspected: R&D/PoC mode, project context collection, memory recall/finalization, PM planning, runner selection, reviews and fix iterations.
- Plausible first-party paths checked: Past-run lessons in prompts, provider capability changes, novel project research and successive quality-remediation rounds.
- Why no material first-party path remains: Observed information either enriches present task execution or records prior context; no separately owned externally prospective adaptation decision enters current S3 capability governance.

## S5 — Policy and identity

- State: —
- Function: No distinct first-party ultimate organizational identity/policy dispute, legitimate final authority and binding operational return.
- Disturbance / variety regulated: Safety concerns, task scope and human preferences constrain what code can be written, but routine task acceptance is not a constitutional choice for the system's identity.
- Decisive decision or feedback right: Human gates approve/reject task specifications, research and implementation plans; PM R&D can propose ending, and Security may flag must-fix. These are project authorization/content decisions, not an established ultimate identity-policy authority loop.
- Decision owner: Human user sets project scope and authorizes work; PM acts within delegated task scope. No S5 owner/path at chosen installed project recursion is identified.
- Supporting / enforcement mechanisms: `gateCh`, `regenerateCh`, artifact approvals, security review findings, configured role instructions, model-provider permissions and audit reports.
- Closure path: Approval releases task execution or re-planning within the same user task; source does not show identity-level disputes being escalated, decided and converted into durable governing policy for later organizational operation.
- Why this is / is not agent-owned: TaskSpec and human approval are not ultimate policy governance by name, and security must-fix is a current operational safety issue unless it changes final organizational identity rules.
- Evidence: [task spec negotiation/approval](https://github.com/Open-Makers/ai-coding-agents-orchestrator/blob/1c1185c6f323bf3475c3847e38245276852ebc5e/internal/orchestrator/task_runner.go#L315-L373); [human plan approval](https://github.com/Open-Makers/ai-coding-agents-orchestrator/blob/1c1185c6f323bf3475c3847e38245276852ebc5e/internal/orchestrator/task_runner.go#L690-L748); [run gates](https://github.com/Open-Makers/ai-coding-agents-orchestrator/blob/1c1185c6f323bf3475c3847e38245276852ebc5e/internal/orchestrator/task_runner.go#L155-L181).
- Basis: Bounded negative.
- Confidence: Medium-high.
- Caveats: User governance over a broader software organization can be legitimate, but this project/task's approval gate has not been shown to adjudicate ultimate identity disputes.

### Absence scope

- Surfaces inspected: TaskSpec negotiations, human plan/research gates, Security/QA findings, PM remediation loop, R&D approval and configuration/permission paths.
- Plausible first-party paths checked: User mandate changes, formal task scope acceptance, security block escalation, model role policies and human option to reject a plan.
- Why no material first-party path remains: Every first-party gate inspected changes a bounded task plan or code acceptance; no ultimate purpose/identity question reaches authority and returns a binding identity-policy revision to future project operations.

## Distributed OSS parent arrangement

Open-Makers contributors, repository CI and maintainer issues do not own the running project instance's PM remediation or audit rights by mere co-location. Separate users can configure agents and approve task plans independently. These local human permissions are bounded to operating projects unless a higher-recursion shared governance return is actually evidenced.

## Self-hosted and non-human modes

After a human approves the task and plan, the normal green/brown/fix path can autonomously execute multiple S1 units, settle a narrow QA/Coder work-product conflict, perform PM remediation and independently review raw source. The human still owns task authorization; `S3=A` is not labeled `A(P)` merely because a human can stop or reject an initial spec. A reduced R&D mode omits several claimed loops and is explicitly not the positive witness.

## Recursion

The project task contains multiple role work cells under a PM and an alternate source-reading review path. No independent viable S2–S5 structure is inferred inside each role, nor is one orchestrator run evidence that Open-Makers' entire development organization has that topology. Positive functions concern one installed coding-task control loop.

## Variety and escalation

Source files/tests, error returns and user feedback supply variety. QA/Coder test conflict escalates after bounded retries to a specifically authorized QA decision; QA/UX/Security independently inspect the current result and send distinct must-fix inputs to PM; PM issues fresh current commitments to the agent work cells. Fail/retry caps attenuate uncontrolled cycling. Neither ordinary scope approval nor memory storage demonstrates S5 or outside-future S4.

## Evidence gaps

- No live LLM/model-provider/Browser/coding-agent quality experiment occurred. The classification concerns pinned first-party reachable source and substantive decision paths; it does not certify that generated code is secure, correct or high quality.
- `S2=A` is narrow: after failed code/test reconciliation, QA itself may have authored the tests; this is cross-unit coordination, not independent audit of QA's own output.
- `S3*=A` uses a distinct source-reading Security/QA reviewer over Coder's actual files with findings returned to PM. If no files are available and reviewers fall back to Coder raw output, the complementary evidence claim does not hold for that particular run. Structural independence is relative to the Coder and bounded by shared provider/project infrastructure.
- `S3=A` belongs to PM's actual accepted-defect → new-subtasks remediation decision in the full integration pipeline, not merely a PM title, initial decomposition or static iteration cap.
- Human approvals are operational task/plan gates; an identity-level S5 parent mode is not inferred. External software-project governance and model-provider architectures remain out of boundary.

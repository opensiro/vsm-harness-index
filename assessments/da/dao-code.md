---
harness_id: dao-code
project_name: Dao Code
repository: https://github.com/tigicion/dao-code
review_ref: 2b50e82c3de751c071e1610b39b3c95956853498
reviewed_at: 2026-10-31
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-31
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: A
autonomy_s5: —
---

# Dao Code

## Review boundary

- System in focus: the shipped Dao Code / dao terminal coding agent TypeScript runtime with its model/tool loop, first-party subagent dispatcher and task manager, git-worktree isolation, built-in verifier, interactive memory reflector, future-session memory injection and configured permission/identity layer.
- Purpose and identity: complete software-engineering assignments in a terminal through a model-controlled tool loop, with optional concurrent child work, live corrections, adversarial verification and reuse of learned project/user practices.
- Relevant environment: local user workspace/git, DeepSeek or configured model provider, shell/tests/browser/MCP tools, user task and feedback, project/user memory files, user/managed permission settings.
- Standard-distribution boundary: installed npm/binary/CLI runtime in normal interactive mode, with optional goal, background agents and isolated subagent settings. One-shot/headless/evaluation modes are distinguished: interactive memory reflection is not credited to those modes.
- Credited operating / distribution surfaces: src/index.ts wiring of model tools, agent tool with parallel tasks and model-selected isolation, background task registry and messaging, model-visible TaskList/TaskStop/TaskSend, bundled verify subagent, interactive unifiedReflect feedback-to-memory persistence and next-session memory injection.
- Adjacent first-party surfaces excluded from ownership: external model/server and arbitrary MCP tools, repository benchmark claims, bundled marketing screenshots, upstream user projects' policies and external managed policy; optional reflection Challenger is disabled by default unless --reflect-challenger and its same-prefix advisory is not credited as the independent S3* audit.
- First-party modes considered: interactive coding with standard permissions and memory, optional parallel/background/isolate agent dispatch, model-owned current task supervision, nontrivial-change verify subagent, future interactive memory recurrence, headless/one-shot without memory reflection.
- Recursion level: one dao CLI session with parent and subagent work cells over the same user project; continuity across interactive sessions for S4, not the entire commercial provider or all accounts.
- Reviewed revision: 2b50e82c3de751c071e1610b39b3c95956853498.
- Observation date: 2026-10-31.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The native streamChat loop executes model-requested tools under first-party approval gates and appends actual result/error observations, including task notification injection and cancel/continue. The agent tool supports independent subagent contexts, tasks[] concurrent fanout, background status, and an isolate/worktree option. Tool instructions explicitly forbid parallel writes to the same files and give the parent a model-visible choice of whether tasks are independent or need serialized execution and isolation. An in-session TaskManager records the population and exposes TaskList, TaskGet/TaskOutput, TaskSend and TaskStop; a child can report upward with MessageParent and a parent can redirect it on a tool boundary. The bundled verify agent has a distinct adversarial source/test mandate and read-only project permissions; it can run tests and report failures, and normal model-facing instructions call for it on nontrivial changes before declaring done. Interactive unified reflection mines user corrections into procedural/feedback rules, deduplicates/upserts them to durable memory, while startup validates them against live code and injects surviving guidance into the next stable prefix. The optional --reflect-challenger advisory is not the same as the verifier and is normally off. Fixed security hierarchy and owner/enterprise policy overlays constrain tools but do not define a deliberative S5 constitutional authority. No provider run or benchmark success was independently reproduced here.

## Operational model

A model-directed parent chooses edits and tool calls for its own current coding task and may spin out separate viable child coding or verification units. S2 credit is for model-owned selection of disjoint parallel work versus serial dependency, including selected isolated worktrees, in response to possible file interference; the low-level worktree mechanism itself is a constructor-owned backstop. S3 credit is narrower than a business-wide fleet: within the parent mission, a model can list, get results from, redirect/resume or stop the active population, with progress/aborts returned to its main context. S3* is the distinct built-in verify Task reading real artifacts and running adversarial tests—not in-band VerifyDone, same-prefix reflection or ordinary producer self-check. S4 is a separate cross-session prospective user-correction-to-reusable-rule path: user feedback is external to the current task hypothesis, the reflector selects a prevention rule and future sessions consume validated guidance. These are supported modes, not claims about every default prompt's actual utilization rate.

## S1 — Operations

- State: A
- Function: autonomously inspect, edit, test and correct a user's software project through a model/tool/result loop.
- Disturbance / variety regulated: unfamiliar code, compile/test failure, unexpected command output, loss of context, blocked edits and changed user requests.
- Decisive decision or feedback right: model selects code operations, tool arguments, next inspections, delegated subtasks and corrective attempts from observed responses.
- Decision owner: model-backed dao parent or child agent; first-party loop dispatches and returns observations, while external model provider implements inference.
- Supporting / enforcement mechanisms: tools registry, approval gate, streaming API, session checkpoints, compaction, todo, shell processes and project instructions.
- Closure path: user task and source context → model tool call → guarded execution → actual tool/test output → model repairs or concludes → changed project artifact/report.
- Boundary reachability: the published dao CLI registers model-facing tools and runs the native turn loop; no external agent E2E or benchmark acceptance is needed to infer this first-party composition.
- Why this is / is not agent-owned: model decisions change next code/tool action in response to feedback; deterministic limits and permission gates do not supply that discretion.
- Evidence: [main model/tool loop](https://github.com/tigicion/dao-code/blob/2b50e82c3de751c071e1610b39b3c95956853498/src/agent/loop.ts), [CLI runTurn wiring](https://github.com/tigicion/dao-code/blob/2b50e82c3de751c071e1610b39b3c95956853498/src/index.ts#L1443-L1475), [first-party tools and loop description](https://github.com/tigicion/dao-code/blob/2b50e82c3de751c071e1610b39b3c95956853498/README.md).
- Basis: structural.
- Confidence: high for source path, medium for production inference quality.
- Caveats: source/CLI architecture inspected at fixed ref; no external DeepSeek key, registered MCP provider or benchmark run was exercised.

## S2 — Coordination

- State: A
- Function: attenuate worktree/file-write interference among independent model-driven subagents by model-selected parallel versus serial assignments and explicit isolated branch partitioning.
- Disturbance / variety regulated: two independently executing code-edit children might change the same project files or consume each other's partial uncommitted work.
- Distinct S1 units: separate model/tool/result child agent runs that can inspect/edit code or tests and progress concurrently under tasks[] or background mode.
- Inter-S1 disturbance: competing writes/read-after-write assumptions to one shared git working tree create overwritten changes, invalid dependencies and ambiguous integration.
- Attenuating coordination relation: parent model is instructed to parallelize only mutually independent tasks and decide when to use isolate/worktree to separate changes; chosen dispatch arguments create distinct git worktrees before child execution.
- Feedback into subsequent S1 behaviour: each child receives the selected isolated worktree as its effective project location; results and branch/change notices return to parent for subsequent review/integration or revised sequential dispatch.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: this explicitly prevents a concrete collision between separately viable source-changing S1s, with the model selecting nonoverlap versus serial order and actual workspace partitioning, not merely handing messages to specialists.
- Decisive decision or feedback right: model chooses which subjobs can safely coexist and which need isolated workspaces or serial ordering, then issues the actual task and isolation arguments.
- Decision owner: parent model in first-party agent tool protocol (A); worktree creation and MAX_PARALLEL cap are constructor-owned support, not the agent decision.
- Supporting / enforcement mechanisms: tasks[] concurrency limiter, model-facing conflict rule, isolate/git-worktree creation, separate child contexts, task results and explicit later review.
- Closure path: parent identifies subjobs and overlap risk → chooses disjoint parallel tasks or sequential dependencies plus isolate → distinct child runs on selected paths → independent changes and completion feedback → parent adjusts next delegation/integration.
- Boundary reachability: agentTool is a registered executable tool, not a README-only promise; it binds selected isolation to createWorktree and passes the resulting worktreePath to runAgent.
- Why this is / is not agent-owned: the parent decides actual partition/scheduling from the task context, while the platform creates and enforces the filesystem isolation. No claim of automatic static conflict detection on every invocation.
- Evidence: [model-facing parallel and same-file exclusion contract](https://github.com/tigicion/dao-code/blob/2b50e82c3de751c071e1610b39b3c95956853498/src/tools/agent.ts#L64-L82), [active isolation and child creation](https://github.com/tigicion/dao-code/blob/2b50e82c3de751c071e1610b39b3c95956853498/src/tools/agent.ts#L190-L275), [parallel task execution](https://github.com/tigicion/dao-code/blob/2b50e82c3de751c071e1610b39b3c95956853498/src/tools/agent.ts#L408-L436), [worktree support](https://github.com/tigicion/dao-code/blob/2b50e82c3de751c071e1610b39b3c95956853498/src/agent/worktree.ts).
- Basis: structural.
- Confidence: medium.
- Caveats: isolation is optional and task overlap is inferred by a model from descriptions, not guaranteed by a scheduler; unisolated parallel edits can still collide. This A is a supported explicit model-owner path, not all-mode automatic coverage.

## S3 — Inside-and-now control

- State: A
- Function: regulate the parent mission's whole current population of running, completed and failed background/foreground child jobs.
- Disturbance / variety regulated: child drift, stalled or unnecessary background work, resource/token consumption, changed task constraints and incomplete results in flight.
- Whole-system current view: TaskManager maintains the registry; model-facing TaskList can show all running/finished jobs, TaskGet/TaskOutput exposes task progress/details, and completion/message notifications return to parent turn context.
- Current-control decision scope: parent model can decide to inspect progress, send mid-course instructions, resume a finished subagent, stop a divergent one or launch replacement work; task state is revised in the current runtime.
- Decisive decision or feedback right: choose task population interventions on live child evidence, rather than only receiving a fixed aggregate report.
- Decision owner: model-driven parent receiving these tools; TaskManager stores and executes decisions but cannot autonomously decide priorities.
- Supporting / enforcement mechanisms: task registry, AbortController, TaskSend pending-message queue, notification injection, TaskStop, TaskList and on-demand TaskOutput.
- Closure path: child task progress/message/error → main context/TaskList → parent model chooses stop/steer/resume/reassign → targeted child receives message or abort → updated state/result returns to main model.
- Boundary reachability: agent tool registers async/foreground tasks in shared TaskManager and main runTurn drains notifications; TaskStop and TaskSend use the same manager.
- Why this is / is not agent-owned: the model, not a timeout or UI operator alone, chooses whether specific live jobs should continue, be redirected or stopped. This is parent-mission S3 only, not multi-user organizational governance.
- Evidence: [task registry, messaging, current snapshot](https://github.com/tigicion/dao-code/blob/2b50e82c3de751c071e1610b39b3c95956853498/src/agent/tasks.ts), [model-visible TaskList](https://github.com/tigicion/dao-code/blob/2b50e82c3de751c071e1610b39b3c95956853498/src/tools/task_list.ts#L16-L45), [real TaskStop abort](https://github.com/tigicion/dao-code/blob/2b50e82c3de751c071e1610b39b3c95956853498/src/tools/task_stop.ts#L6-L33), [mid-course TaskSend/resume](https://github.com/tigicion/dao-code/blob/2b50e82c3de751c071e1610b39b3c95956853498/src/tools/task_send.ts#L5-L50), [main notification return](https://github.com/tigicion/dao-code/blob/2b50e82c3de751c071e1610b39b3c95956853498/src/index.ts#L1443-L1469).
- Basis: structural.
- Confidence: medium-high.
- Caveats: current whole is the parent session's task fleet. Tool descriptions can encourage but do not guarantee a particular model will use supervision at every point.

## S3* — Complementary audit

- State: A
- Function: challenge a producer's completion account using a distinct adversarial, read-only project verifier that runs source-specific tests and seeks counterexamples.
- Disturbance / variety regulated: implementing agent can claim success from its own mocks/happy-path tests or summary while real app/API/CLI/public contract still fails.
- Decisive decision or feedback right: separate verify subagent chooses adversarial cases, directly runs tests/server/browser/CLI checks and returns pass/fail/partial findings for producer rework.
- Decision owner: model-backed built-in verify agent with its own role/context/tool restrictions; parent chooses dispatch/repairs. A status parser or fixed VerifyDone command is not the auditing owner.
- Supporting / enforcement mechanisms: verify agent definition, disallowed edit/write tools, read/execute investigation, risk-specific probes, task return/notification, model-facing nontrivial-change verification guidance.
- Closure path: producer changes and claim → parent dispatches verify Task → verifier independently reads project/spec and exercises tests/behavior → findings and commands → parent fixes or rechecks → no unverified completion claim.
- Boundary reachability: verify is bundled into the active agent definition list and callable by agent agent_type=verify; the bundled verification skill and tool-facing instructions request it for nontrivial changes. It is a supported optional verification mode, not mandatory on every trivial edit.
- Why this is / is not agent-owned: verifier chooses tests/edge cases based on direct evidence, not merely accepting the producer's narrative. Ordinary in-band VerifyDone and same-prefix reflection are excluded.
- Claim being audited: reported code change meets its actual intended behavior and does not create material regressions.
- Ordinary reporting path: parent/producer tool summary, test claims, todo or VerifyDone result.
- Complementary access path: fresh read-only verifier context with source/spec/README, actual test commands, server/browser/API probes and observed stdout/behavior.
- Independence boundary: distinct model-backed subagent and tool restriction relative to implementing agent, but potentially same external model provider and parent task; no organizationally external audit independence claimed.
- Who acts on findings: parent/coding agent repairs or qualifies results after receiving verifier return; verifier does not write project files itself.
- Evidence: [built-in adversarial verify definition](https://github.com/tigicion/dao-code/blob/2b50e82c3de751c071e1610b39b3c95956853498/src/agent/bundled_agents.ts#L108-L185), [verify skill dispatch guidance](https://github.com/tigicion/dao-code/blob/2b50e82c3de751c071e1610b39b3c95956853498/src/skills/bundled.ts#L80-L100), [agent role dispatch and permission](https://github.com/tigicion/dao-code/blob/2b50e82c3de751c071e1610b39b3c95956853498/src/tools/agent.ts#L190-L274), [model-facing subagent evidence skepticism](https://github.com/tigicion/dao-code/blob/2b50e82c3de751c071e1610b39b3c95956853498/src/tools/agent.ts#L119-L141).
- Basis: structural.
- Confidence: medium.
- Caveats: optional dispatch and external provider availability; no actual test run of the independent model verifier was observed in this assessment.

## S4 — Outside-and-then intelligence

- State: A
- Function: adapt later coding sessions' operating guidance to recurring user corrections, preferences and observed failed techniques.
- Disturbance / variety regulated: outside user negative feedback about current approach or missing acceptance criteria that would otherwise recur across future tasks.
- Decisive decision or feedback right: model-backed interactive reflector recognizes a correction, proposes a reusable why/how prevention rule, selects memory type/confidence/merge target and causes persistent upsert; startup validation governs whether future sessions receive it.
- Decision owner: model-driven unified reflector as a distinct model invocation in the first-party interactive runtime, with deterministic salience/trust/secret filters and memory store as supporting constructors.
- Supporting / enforcement mechanisms: correction-specific prompt, feedback why/how criterion, scope routing, mergeInto/upsert persistence, code-based memory validation and stable session prompt injection.
- Closure path: user corrects a mistaken approach/DoD → reflector extracts prospective rule with why/how → durable user/project memory upsert or revision → next interactive session filters against live code → accepted guidance injected into model context → subsequent engineering behavior can change.
- Boundary reachability: src/index.ts calls maybeReflect during normal interactive turns (unless --no-memory/one-shot), runs unifiedReflect, persists accepted memory and loads/validates/uses memory at next startup. Challenger drift review is a separately opt-in feature and not required for S4 credit.
- Why this is / is not agent-owned: model decides which user reaction is a durable future rule and its specific meaning; validation/GC/filing alone do not create that semantic adaptation.
- External distinction: human user correction or a demand for stronger acceptance checks is an external expectation signal, not merely model self-talk or log summarization.
- Future / prospective distinction: the extracted why/how rule is intended to guide later unrelated sessions and prevent recurrence, rather than fix only the present code line.
- Adaptation option generated: reusable feedback/procedural memory advising changed future checks or mode of work, with confidence and source.
- Path back into current capability / S3: validated memory becomes a fixed next-session model prefix and memory_read retrieval source, changing the operating discretion of the next coding/S3 parent; no separate organization-wide S5 right is implied.
- Evidence: [model-authored user correction and future rule prompt](https://github.com/tigicion/dao-code/blob/2b50e82c3de751c071e1610b39b3c95956853498/src/agent/unified_reflect.ts#L18-L68), [actual interactive reflection persistence and correction](https://github.com/tigicion/dao-code/blob/2b50e82c3de751c071e1610b39b3c95956853498/src/index.ts#L1491-L1548), [future-session code validation and prompt injection](https://github.com/tigicion/dao-code/blob/2b50e82c3de751c071e1610b39b3c95956853498/src/index.ts#L640-L696), [memory store](https://github.com/tigicion/dao-code/blob/2b50e82c3de751c071e1610b39b3c95956853498/src/memory/store.ts).
- Basis: structural.
- Confidence: medium-high.
- Caveats: contingent on normal interactive memory being enabled and the model extracting a substantive rule; one-shot/--no-memory/benchmark paths skip the loop. No measured longitudinal adaptation was tested.

## S5 — Policy and identity

- State: —
- Function: no first-party autonomous legitimacy/identity policy forum governs the system's ultimate purpose.
- Disturbance / variety regulated: sensitive paths, dangerous commands, project permission modes and skill instruction conflicts are constrained by a predetermined rule hierarchy.
- Decisive decision or feedback right: the user or managed enterprise setting chooses access/identity constraints; the model can propose tool calls but cannot constitutionally amend ultimate policy.
- Decision owner: configured owner/enterprise policy and fixed permission interpreter, not a model-led S5 constitutional decision process.
- Supporting / enforcement mechanisms: allow/ask/deny, managed policy precedence, sandbox/secret scanning, constitution-style prompt priorities, permission modes and human confirmations.
- Closure path: selected user/managed rules → tool request → permission gate/ask/deny → operational outcome; no autonomous ultimate-purpose deliberation → policy amendment → returned binding authority.
- Why this is / is not agent-owned: a priority ordering in the system prompt and layered permission enforcement do not constitute a function that legitimately revises organizational identity.
- Evidence: [permission hierarchy](https://github.com/tigicion/dao-code/blob/2b50e82c3de751c071e1610b39b3c95956853498/README.md), [permissions engine](https://github.com/tigicion/dao-code/blob/2b50e82c3de751c071e1610b39b3c95956853498/src/permissions/engine.ts), [settings and managed policy](https://github.com/tigicion/dao-code/blob/2b50e82c3de751c071e1610b39b3c95956853498/src/permissions/settings.ts).
- Basis: structural.
- Confidence: high within inspected boundary.
- Caveats: external owner institutions, DeepSeek provider policy and the governance of user repositories are excluded.

### Absence scope

- Surfaces inspected: constitution-style prompt ordering, permissions engine/settings, managed-policy precedence, model modes, skills and user feedback memory.
- Plausible first-party paths checked: permission changes, enterprise policy, self-improvement memory, skill adaptation and account profiles.
- Why no material first-party path remains: these enforce or remember subordinate practices, not a first-party ultimate legitimacy/identity decision with durable policy ratification.

## Recursion

The parent dao session is the focal operational whole. It owns model-directed S1 actions and optional independent child coding cells. S2 selects parallel disjoint work and worktree isolation; S3 supervises the current child population; S3* challenges a producer from direct independent source/behavior evidence. S4 reaches forward across interactive sessions through user-feedback rules. These functions compose at the CLI mission/project recursion only; static owner/enterprise permission constraints remain externally set, not S5.

## Variety and escalation

- Work may be split into independent parallel child tasks when the model judges them nonoverlapping; explicit isolate/worktree is available for concurrent writes, while no automated universal conflict detector is claimed.
- Background children can send messages to parent, and parent can inspect, redirect, resume or abort active work; an abort does not automatically undo prior file edits.
- Nontrivial changes can be reviewed by a distinct restricted verify agent, whereas a local VerifyDone command, in-band self-check or same-prefix Challenger is not enough for complementary audit credit.
- Interactive memory can promote external corrections to next-session guidance with model judgment and deterministic validation, whereas one-shot/evaluation sessions intentionally omit the adaptation loop.
- Layered permissions, managed policy and human approvals can block unsafe tool actions; no user/enterprise gate is bypassed by the assessment.
- No external model E2E, benchmark or live tool/provider integration was run here.

## Evidence gaps

- Revision-pinned first-party source review; no DeepSeek credentials, user workspace changes, independent verify model execution or real multi-agent edit collision was exercised.
- The optional isolation mode and parallel task scope selection rely on a model obeying tool instructions. S2=A is a reachable decision path, not blanket collision freedom.
- Verify agent is a supported optional role for nontrivial changes; built-in same-prefix reflection is normally disabled and was not used as S3* evidence.
- Cross-session S4 needs interactive mode and meaningful user corrections; source shows its storage/injection path but not measured future behavior.
- Bundled tests and eval artifacts were inspected for structure, not re-run with installed node dependencies or provider test harness; no quantitative benchmark/pricing claim was independently accepted.
- External provider/MCP and user policy rights are outside the assessed first-party closure.

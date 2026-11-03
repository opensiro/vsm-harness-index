---
harness_id: colony
project_name: colony
repository: https://github.com/yusa-imit/colony
review_ref: b1a7679ac299bf4be2e278cfb25616fac52b3365
reviewed_at: 2026-11-03
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-11-03
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# colony

## Review boundary

- System in focus: The first-party Rust Colony runtime, agent-work protocol, shared task board/chat, Git hub, worker lifecycle and optional whole-branch verification; not generic Claude Code capabilities outside Colony's operating protocol.
- Purpose and identity: Coordinate several autonomous Claude Code worker processes toward one operator-specified software goal without a central task-assigning manager.
- Relevant environment: Repository code, overlapping edits, tasks/dependencies, peer claims and failures, shared branch, developer-specified goal, tests and usage limits.
- Standard-distribution boundary: `colony` binary starts workers with a common goal and first-party protocol, implements board/claim/propose/reopen tools and a serializable hub; number of workers and a verification command are operator-configured.
- Credited operating / distribution surfaces: [prompts.rs](https://github.com/yusa-imit/colony/blob/b1a7679ac299bf4be2e278cfb25616fac52b3365/src/prompts.rs), [mcp.rs](https://github.com/yusa-imit/colony/blob/b1a7679ac299bf4be2e278cfb25616fac52b3365/src/mcp.rs), [board.rs](https://github.com/yusa-imit/colony/blob/b1a7679ac299bf4be2e278cfb25616fac52b3365/src/board.rs), [hub.rs](https://github.com/yusa-imit/colony/blob/b1a7679ac299bf4be2e278cfb25616fac52b3365/src/hub.rs), [supervisor.rs](https://github.com/yusa-imit/colony/blob/b1a7679ac299bf4be2e278cfb25616fac52b3365/src/supervisor.rs), [inbox.rs](https://github.com/yusa-imit/colony/blob/b1a7679ac299bf4be2e278cfb25616fac52b3365/src/inbox.rs).
- Adjacent first-party surfaces excluded from ownership: Underlying external Claude Code's general tool intelligence, human-set goal/budget/deadline, Git's mechanical conflict checks, deterministic atomic claims, verify command/test suite and human evaluation of final work.
- First-party operating modes considered: Several model-bearing workers, shared board with no director, inter-worker chat/notes, local clone and hub, usage-limited supervisor; optional `--verify` command.
- Recursion level: One colony of operational worker units, with distributed current coordination and whole-goal closure; not each spawned shell command as an additional viable recursion.
- Reviewed revision: `b1a7679ac299bf4be2e278cfb25616fac52b3365`.
- Observation date: 2026-11-03.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Colony starts external Claude Code workers in separate clones, but supplies the distinctive first-party system protocol and shared MCP task tools. All workers see a board and one goal, with no central manager assigning work. A worker chooses and claims tasks, proposes missing subtasks, decides how to implement them, checks and rebases before pushing, shares observations and may reopen broken peer work. The board enforces exclusivity; the hub enforces non-force-push integration; the supervisor enforces budgets and concurrency, but explicitly does not decide who works on what. [prompts.rs#L38-L101](https://github.com/yusa-imit/colony/blob/b1a7679ac299bf4be2e278cfb25616fac52b3365/src/prompts.rs#L38-L101), [mcp.rs#L188-L282](https://github.com/yusa-imit/colony/blob/b1a7679ac299bf4be2e278cfb25616fac52b3365/src/mcp.rs#L188-L282), [supervisor.rs#L1-L14](https://github.com/yusa-imit/colony/blob/b1a7679ac299bf4be2e278cfb25616fac52b3365/src/supervisor.rs#L1-L14).

## Operational model

Peer agents independently select task and code actions while sharing a goal. The board exposes entire live work status and returns feedback on contested claims, blocked dependencies and completed tasks. Peer messages and rebase/reopen loops alter subsequent peer behavior. A worker may propose a current workplan or declare the collective goal complete only after current board obligations close and, when configured, a whole-branch verification passes. The optional peer-reopen pathway can challenge another worker's completion, but it does not mandate a separate reviewer nor truly independent external evidence.

## S1 — Operations

- State: A
- Function: Adaptively produce software changes and work artifacts for a claimed task.
- Disturbance / variety regulated: Unspecified implementation steps, code reality, failing checks, rebases and local task obstacles.
- Decisive decision or feedback right: Choose implementation, tool sequence, code fixes, testing and completion or release of the current claimed task.
- Decision owner: Individual model-bearing worker operating inside Colony's task protocol.
- Supporting / enforcement mechanisms: Claude Code CLI process, isolated clone, turn prompt, MCP tools, tests, Git hub, budget gate.
- Closure path: Current task/goal → worker reads code → chooses changes → checks observed result → repairs or pushes verified work → records task completion.
- Boundary reachability: Colony launches real workers with first-party prompt and task tools on its standard command path; model/service availability is external.
- Why this is / is not agent-owned: Model workers choose real next actions and interpret test feedback; the deterministic board does not write code or select solutions.
- Evidence: [prompts.rs#L38-L80](https://github.com/yusa-imit/colony/blob/b1a7679ac299bf4be2e278cfb25616fac52b3365/src/prompts.rs#L38-L80), [worker.rs](https://github.com/yusa-imit/colony/blob/b1a7679ac299bf4be2e278cfb25616fac52b3365/src/worker.rs), [hub.rs](https://github.com/yusa-imit/colony/blob/b1a7679ac299bf4be2e278cfb25616fac52b3365/src/hub.rs).
- Basis: explicit + structural.
- Confidence: high for operating ownership; no external provider-backed execution in this review.
- Caveats: The coding cognition is supplied by an installed external Claude Code worker; Colony owns the protocol/orchestration that directs it, not the model internals.

## S2 — Coordination

- State: A
- Distinct S1 units: Separate code-writing Claude Code worker processes, each owning a different claimed task and isolated clone.
- Inter-S1 disturbance: Competing task claims, duplicate work, conflicting changes to shared files and unmet task dependencies.
- Attenuating coordination relation: Workers observe atomic claim feedback and peer messages, change their commitments, reserve dependency-blocked work, negotiate overlap and integrate only after a non-force Git rebase.
- Feedback into subsequent S1 behaviour: A refused claim makes the worker choose another item; a peer mention or rejected push leads to coordination, rebase and retesting before completing its own task.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The first-party protocol connects a named inter-worker collision to its observed refusal or conflict, then instructs the model worker to change its plan and return a non-conflicting commitment. The mechanical lock alone would not suffice.
- Function: Attenuate interference between parallel workers changing the same goal/repository and return conflict signals to those workers.
- Disturbance / variety regulated: Competing claims, duplicate task proposals, overlapping edits, unmet dependencies and stale peer assumptions can destabilize otherwise productive S1 workers.
- Decisive decision or feedback right: Re-select work after a rejected claim, renegotiate task boundaries via peer chat, revise after conflicting Git changes, or reserve/release an interdependent task.
- Decision owner: Peer model workers interpret the conflicting board/chat/Git feedback; board and hub provide non-discretionary exclusivity constraints.
- Supporting / enforcement mechanisms: Atomic claim/rejection, duplicate proposal filter, dependency reservation, shared chat/notes, mid-turn inbox and non-force-push shared branch.
- Closure path: Worker A claims/changes a task → worker B sees refused claim, chat mention or changed hub → B selects another task, coordinates boundaries or rebases → new board/branch state is visible to both.
- Boundary reachability: Multiple workers and board tools are the normal Colony runtime, not an external application constructing its own regulator.
- Why this is / is not agent-owned: Locks and rebases alone are automatic S2 support; positive attribution is limited to model-owned choice to replan, coordinate and repair after those feedback signals.
- Evidence: [prompts.rs#L46-L75](https://github.com/yusa-imit/colony/blob/b1a7679ac299bf4be2e278cfb25616fac52b3365/src/prompts.rs#L46-L75), [board.rs#L391-L562](https://github.com/yusa-imit/colony/blob/b1a7679ac299bf4be2e278cfb25616fac52b3365/src/board.rs#L391-L562), [inbox.rs](https://github.com/yusa-imit/colony/blob/b1a7679ac299bf4be2e278cfb25616fac52b3365/src/inbox.rs), [hub.rs](https://github.com/yusa-imit/colony/blob/b1a7679ac299bf4be2e278cfb25616fac52b3365/src/hub.rs).
- Basis: explicit + structural.
- Confidence: medium-high; the code establishes the regulation loop, not conflict-recovery success rates.
- Caveats: When only one worker is started, cross-worker S2 is dormant; low-level locking itself is not counted as agent autonomy.

## S3 — Inside-and-now control

- State: A
- Whole-system current view: Every worker reads the shared board with all open/claimed/done tasks and the common goal, rather than merely its own tool log.
- Current-control decision scope: Any worker can propose missing goal work, amend present task dependencies and commitments, reopen failed completion, or close the whole goal after all current tasks finish and configured checks pass.
- Function: Distribute current whole-goal task commitments and regulate unresolved work across the shared colony.
- Disturbance / variety regulated: Missing goal subtasks, blocked critical paths, stale completed work, all-done-but-goal-incomplete conditions and changed availability.
- Decisive decision or feedback right: From a whole-board current view, propose a 5–15-task plan, add missing work, pick/reassign one's commitment, reopen a flawed completed task, and finally declare goal completion.
- Decision owner: Distributed model workers; one agent initially takes the planning task but any worker may amend the plan or exercise whole-goal closure. No separate central director exists.
- Supporting / enforcement mechanisms: `board_view`, shared goal, task dependencies/status, board wakeups, one-planning-task bootstrap, `goal_complete` eligibility and optional cached verifier.
- Closure path: Goal/current board → worker identifies missing or blocked work → proposes/reopens and changes commitments → colleagues see the revised board and act → terminal whole-goal verification/closure.
- Boundary reachability: The shipped standard protocol initializes the planning task and gives every worker whole-board tools and goal-completion rights.
- Why this is / is not agent-owned: The status checks are deterministic, but agents decide priorities, propose new current work and judge missing completeness; S3 is distributed rather than embodied by a manager process.
- Evidence: [prompts.rs#L46-L63](https://github.com/yusa-imit/colony/blob/b1a7679ac299bf4be2e278cfb25616fac52b3365/src/prompts.rs#L46-L63), [prompts.rs#L89-L99](https://github.com/yusa-imit/colony/blob/b1a7679ac299bf4be2e278cfb25616fac52b3365/src/prompts.rs#L89-L99), [mcp.rs#L188-L204](https://github.com/yusa-imit/colony/blob/b1a7679ac299bf4be2e278cfb25616fac52b3365/src/mcp.rs#L188-L204), [board.rs#L852-L890](https://github.com/yusa-imit/colony/blob/b1a7679ac299bf4be2e278cfb25616fac52b3365/src/board.rs#L852-L890).
- Basis: explicit + structural.
- Confidence: medium; no measured claim of effective governance across arbitrary worker counts.
- Caveats: No separately privileged S3 agent; the same workers own S1 and distributed S3 choices. Operator-goal changes and budgets remain external.

## S3* — Complementary audit

- State: C
- Claim being audited: A peer's done task or final shared-branch state meets its acceptance criteria and the colony goal.
- Ordinary reporting path: Task owner writes `task_complete` summary with a merged commit; status appears on the board.
- Complementary access path: Another worker can inspect the actual shared branch and task details, execute checks, then call `task_reopen` with a reason; configured `verify` independently executes an operator-specified test command against the current hub commit.
- Independence boundary: Source access and separate peer model process are available but independent reviewer assignment is optional and not enforced; automated `verify` is a check, not a separate agent judgment.
- Who acts on findings: Reopened task becomes claimable and workers are signaled; a failed `verify` refuses `goal_complete`, announces the failure and requires branch repair.
- Function: Conditional peer challenge of task completion and reality check of the merged goal state.
- Disturbance / variety regulated: Misleading done summaries, broken peer changes and unverified whole-goal completion.
- Decisive decision or feedback right: A peer can reject a completion with evidence; optional verifier can block a false goal-complete declaration.
- Decision owner: A distinct worker when it undertakes peer inspection; test-command outcome and close-goal gate are deterministic.
- Supporting / enforcement mechanisms: `task_reopen`, source/branch access, task logs, peer notifications, `verify` commit cache and closure refusal.
- Closure path: Owner's done claim → separate worker inspects actual artifact → reasoned reopen → peer correction/new claim → fresh completion; optional test failure triggers the same operational repair path.
- Boundary reachability: Peer-reopen tool and prompt are standard; a different reviewer agent and configured verify command are possible but not required on every completion, warranting C rather than A.
- Why this is / is not agent-owned: The peer can make a substantive source-grounded audit decision; generic testing/board messages are not themselves independent S3* agency.
- Evidence: [prompts.rs#L89-L99](https://github.com/yusa-imit/colony/blob/b1a7679ac299bf4be2e278cfb25616fac52b3365/src/prompts.rs#L89-L99), [board.rs#L692-L719](https://github.com/yusa-imit/colony/blob/b1a7679ac299bf4be2e278cfb25616fac52b3365/src/board.rs#L692-L719), [mcp.rs#L269-L285](https://github.com/yusa-imit/colony/blob/b1a7679ac299bf4be2e278cfb25616fac52b3365/src/mcp.rs#L269-L285), [mcp.rs#L420-L445](https://github.com/yusa-imit/colony/blob/b1a7679ac299bf4be2e278cfb25616fac52b3365/src/mcp.rs#L420-L445).
- Basis: explicit + structural.
- Confidence: medium for conditional peer pathway; independent-review coverage not established.
- Caveats: `task_reopen` can be used by the original worker; no source code mandates a distinct auditor. A test failure and its deterministic gate do not prove auditor independence.

## S4 — Outside-and-then intelligence

- State: —
- Function: No evidenced distinct prospective external scanning and organization-level capability adaptation.
- Disturbance / variety regulated: Current goal implementation, API usage and peer failures, not an evolving future external environment.
- Decisive decision or feedback right: Choose and propagate forward-looking capability/strategy shifts in response to environmental futures; absent.
- Decision owner: Operator sets goals, worker count, tools and usage limits; workers can revise within-goal plans only.
- Supporting / enforcement mechanisms: Plan task T1, peer notes, repeated sessions, usage-limit throttling and dynamic current tasks.
- Closure path: Within-goal task replanning returns to present operations; no prospective option evaluation leading to durable new capability and authorized integration.
- Why this is / is not agent-owned: Choosing tomorrow's step of an already fixed software goal is current execution, not S4 environmental adaptation.
- Evidence: [prompts.rs#L38-L102](https://github.com/yusa-imit/colony/blob/b1a7679ac299bf4be2e278cfb25616fac52b3365/src/prompts.rs#L38-L102), [supervisor.rs#L1-L14](https://github.com/yusa-imit/colony/blob/b1a7679ac299bf4be2e278cfb25616fac52b3365/src/supervisor.rs#L1-L14).
- Basis: structural.
- Confidence: high for reviewed first-party modes.
- Caveats: A user may assign a future-oriented project goal; task subject matter does not establish a distinct harness S4.

### Absence scope

- Surfaces inspected: Prompt protocol, planning task, notes/chat, supervisor/config, worker and repo integration paths.
- Plausible first-party paths checked: Long-running goal, peer-discovered tasks, rate-limit adaptation, retained notes and end-to-end completion checks.
- Why no material first-party path remains: All closed loops are bounded by the operator's present goal; no durable future environment-to-capability adaptation decision is evidenced.

## S5 — Policy and identity

- State: —
- Function: No harness-owned identity/ultimate-policy governance that can legitimately redefine the binding goal and return a constitutional decision.
- Disturbance / variety regulated: User-configured budget, deadlines, permissions and Git restrictions are operational bounds, not identity disputes.
- Decisive decision or feedback right: Resolve binding-purpose/policy conflicts with authorized parent return; absent.
- Decision owner: Operator supplies goal and budget, Rust supervisor enforces stops, and workers choose within those bounds.
- Supporting / enforcement mechanisms: Goal text, usage caps, task/branch gates, deterministic verifier and human external CLI configuration.
- Closure path: Worker goal-complete stops the job and budget stop cancels workers; neither authorizes a change of organizational identity.
- Why this is / is not agent-owned: A worker's finishing declaration is current objective closure (S3), not binding S5 purpose adjudication.
- Evidence: [supervisor.rs](https://github.com/yusa-imit/colony/blob/b1a7679ac299bf4be2e278cfb25616fac52b3365/src/supervisor.rs), [mcp.rs#L420-L445](https://github.com/yusa-imit/colony/blob/b1a7679ac299bf4be2e278cfb25616fac52b3365/src/mcp.rs#L420-L445), [prompts.rs#L38-L46](https://github.com/yusa-imit/colony/blob/b1a7679ac299bf4be2e278cfb25616fac52b3365/src/prompts.rs#L38-L46).
- Basis: structural.
- Confidence: high.
- Caveats: Operator authorization can govern the colony from outside the reviewed first-party system; no internal legitimate parent role is claimed.

### Absence scope

- Surfaces inspected: Goal prompt and CLI configuration, complete-goal transition, budget/limit supervisor, task restrictions and test verification.
- Plausible first-party paths checked: Self-proposed new work, rewriting task plans, deadline stop, supervisor policy, worker closure of the goal.
- Why no material first-party path remains: Each is present-goal decision or static enforcement; none handles a contested organizational identity question with an accountable higher authority and returned binding policy.

## Distributed OSS parent arrangement

Human operator sets the original binding goal and runtime constraints; peers can alter the task board but do not acquire an owner-authorized parent mandate to change that goal or external publication policy.

## Self-hosted and non-human modes

The Rust coordinator and Git hub can be locally run, while model-bearing Claude Code workers require an external installed runtime and its model access. Distributed S2/S3 rely on actual multiple workers and readable shared board state, not on a centralized LLM manager.

## Recursion

Workers are S1 units coordinated in the colony's one operational recursion. A separate clone, additional process or worker turn is not proof of a full new viable metasystem.

## Variety and escalation

Task proposal, claim reservation and peer negotiation absorb concurrent code-change variety. Board reopens and verifier failure may send corrective signals to operations. Supervisor rate-limit concurrency changes are mechanical reliability controls, not a discretionary policy escalation loop.

## Evidence gaps

- No provider-backed multi-worker run or quantitative conflict-recovery/peer-audit effectiveness was executed at the pinned revision.
- A distinct peer inspection is possible but not required, making S3* conditional even with the shipped `task_reopen` tool.
- Actual Claude Code internals are outside the credited first-party boundary; Colony's own prompt, tools and coordination flow are the basis of attribution.

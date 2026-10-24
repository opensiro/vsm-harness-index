---
harness_id: alisio
project_name: Alisio
repository: https://github.com/GustavoGutierrez/alisio
review_ref: 4a3c9c21b9e005f7bf8ebcd256bee5de60dc2e48
reviewed_at: 2026-10-23
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-23
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Alisio

## Review boundary

- System in focus: first-party Alisio terminal coding-agent application at `GustavoGutierrez/alisio@4a3c9c21b9e005f7bf8ebcd256bee5de60dc2e48`, including its default-enabled subagent plugin within one parent coding session.
- Purpose and identity: complete user-requested repository development work by selecting model-backed tools, observing outcomes and, when useful, delegating independently executing coding or exploration subtasks.
- Relevant environment: project repository, shell and git state, model/provider responses, per-project configuration, tool permissions, multiple working child sessions, contention from concurrent writes and user decisions.
- Standard-distribution boundary: shipped CLI and built-in plugins, core model/tool/session runtime, documented foreground/background subagents, interactive and headless modes.
- Credited operating / distribution surfaces: `packages/cli/src/builtin.ts`, `packages/core/src/core/runner.ts`, `packages/core/src/sessions/children.ts`, `packages/plugin-subagents/src/`, `packages/plugin-memory/src/` and documented built-in operating modes.
- Adjacent first-party surfaces excluded from ownership: repository maintenance/CI/release, Vitest fixtures and mock providers, examples of user-authored agent definitions, external provider companies, developer's personal scripts and external git hosting governance.
- First-party operating / deployment modes considered: interactive TUI and noninteractive agent use, built-in `general`/`explore`/`plan` children, foreground/background delegation, default ask/serial write safety, optional git-worktree isolation and supplied main-agent/child definitions.
- Recursion level: one user-requested coding session and its subordinate working child sessions, not the OSS maintainer organization.
- Reviewed revision: `4a3c9c21b9e005f7bf8ebcd256bee5de60dc2e48` (immutable frozen batch #996 row 5).
- License screen: frozen root `LICENSE` contains MIT; GitHub repository metadata independently reports `MIT`.
- Observation date: 2026-10-23.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.7`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.7`.

## Repository architecture

The CLI assembles a model provider, tools, session store, permission layer and plugins. `AgentRunner` exposes tool descriptions to the model, executes selected calls with permission checks, stores tool output and resumes the model's own decision loop; consecutive read-only or explicitly concurrent tool calls may run in bounded batches. A default-enabled `subagents` plugin contributes `task`, `task_status`, `task_wait` and `send_message`. The primary model can start several separately model-backed child conversations, choose their instructions/roles/model, inspect returned states, and revise instructions. Built-in `general`, `explore` and `plan` are shipped; children have narrowed permissions and delegated-capability limits.

`SubagentManager` specifically addresses shared-workspace write collisions: concurrent writing children trigger an interactive choice among separate git worktrees, serial writes and explicitly risky shared writing. Headless `ask` falls back to serial execution. A semaphore or per-child worktree operationalizes the selected response, child results and diffstat return to the parent, and optional human `/agents merge` or discard commands govern worktree integration. Separate default-enabled memory uses SQLite FTS5 and session compaction; it does not itself investigate and redesign future product capability.

Frozen primary sources: [`CLI built-ins`](https://github.com/GustavoGutierrez/alisio/blob/4a3c9c21b9e005f7bf8ebcd256bee5de60dc2e48/packages/cli/src/builtin.ts), [`model runner`](https://github.com/GustavoGutierrez/alisio/blob/4a3c9c21b9e005f7bf8ebcd256bee5de60dc2e48/packages/core/src/core/runner.ts), [`subagent plugin`](https://github.com/GustavoGutierrez/alisio/blob/4a3c9c21b9e005f7bf8ebcd256bee5de60dc2e48/packages/plugin-subagents/src/index.ts), [`manager`](https://github.com/GustavoGutierrez/alisio/blob/4a3c9c21b9e005f7bf8ebcd256bee5de60dc2e48/packages/plugin-subagents/src/manager.ts), [`write configuration`](https://github.com/GustavoGutierrez/alisio/blob/4a3c9c21b9e005f7bf8ebcd256bee5de60dc2e48/packages/plugin-subagents/src/config.ts), [`built-in agent definitions`](https://github.com/GustavoGutierrez/alisio/blob/4a3c9c21b9e005f7bf8ebcd256bee5de60dc2e48/packages/plugin-subagents/src/definitions.ts), [`shipped user documentation`](https://github.com/GustavoGutierrez/alisio/blob/4a3c9c21b9e005f7bf8ebcd256bee5de60dc2e48/docs/subagents.md).

## Operational model

An autonomous primary coding agent owns the decisions over file/shell tools and task decomposition; child sessions independently decide how to accomplish bounded subtasks. At the parent boundary their possible concurrent writes create a first-party S2 interference class. The primary agent chooses when and which children operate, with instructions and follow-up messages shaping their work; the runtime enforces a distinct write-collision guard, while the operator chooses the safety mode when a terminal is interactive. Neither ordinary delegation, the queue/status panel, nor configured concurrency caps by themselves establish whole-system S3 current-control decisions; no independently wired S3* operational audit, prospective S4 redesign or S5 identity closure is evidenced.

## S1 — Operations

- State: A
- Function: execute user-requested coding operations in the repository, including independent bounded child tasks.
- Disturbance / variety regulated: unfamiliar code, errors, shell results, changing task requirements, permissions, provider output and child-task results.
- Decisive decision or feedback right: model-backed primary and child actors select tools/arguments and adapt subsequent actions to tool output and instructions.
- Decision owner: primary Alisio model agent and distinct subordinate model sessions in supported delegation mode.
- Supporting / enforcement mechanisms: provider/session bindings, tool registry, permissions, active-agent selection, child session creation, depth/turn limits and tool-result persistence.
- Closure path: model decides tool or child task → runtime executes or denies → tool output/child result enters that actor's or parent's conversation → agent selects further work.
- Boundary reachability: CLI ships the core runner and enables the `subagents` plugin by default; its built-in general/explore/plan definitions instantiate separate child model sessions via registered tools.
- Why this is / is not agent-owned: the model chooses work and responds to results; runner and permissions execute/constrain but do not preselect individual code edits.
- Evidence: [`runner.ts`](https://github.com/GustavoGutierrez/alisio/blob/4a3c9c21b9e005f7bf8ebcd256bee5de60dc2e48/packages/core/src/core/runner.ts), [`index.ts`](https://github.com/GustavoGutierrez/alisio/blob/4a3c9c21b9e005f7bf8ebcd256bee5de60dc2e48/packages/plugin-subagents/src/index.ts), [`manager.ts`](https://github.com/GustavoGutierrez/alisio/blob/4a3c9c21b9e005f7bf8ebcd256bee5de60dc2e48/packages/plugin-subagents/src/manager.ts).
- Basis: structural source and first-party operating documentation; native deterministic subagent tests.
- Confidence: high for supported operating path.
- Caveats: no connected live LLM was run; native tests corroborate constructor and control behavior, not model quality.

## S2 — Coordination

- State: A
- Function: dampen interference among independently deciding child coding S1s working under one primary agent.
- Disturbance / variety regulated: concurrent write-capable children may overwrite one another's changes or generate conflicting repository modifications.
- Distinct S1 units: two or more child model sessions with separate conversations and scoped tool rights, scheduled through the built-in `task` tool.
- Inter-S1 disturbance: `startTask` explicitly detects at least two overlapping write-capable children and activates a collision-specific mitigation path; read-only work does not require writer isolation.
- Attenuating coordination relation: the primary model selects child roles, bounds instructions and work decomposition and can adjust running children via `send_message`; the built-in manager then serializes writers or uses isolated git worktrees under the configured/operator-chosen policy.
- Feedback into subsequent S1 behaviour: assigned child instructions and write boundaries govern the work they undertake; queued/finished results and worktree diffstats return to the parent agent, which can revise later delegation or message a child. Worktree changes require explicit integration before affecting the shared tree.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the separate mitigation is triggered by an implemented *concurrent write collision* class, and changes the execution location/ordering of precisely those S1s; it is not a generic task queue or chat transport alone.
- Decisive decision or feedback right: the parent model decides which independent child work to run and its task-specific coordination boundaries, and can revise a child after result feedback; an interactive human separately chooses worktree/serial/shared collision policy when prompted.
- Decision owner: model-backed primary actor for task-specific coordination; interactive operator for the write-safety policy choice; deterministic `SubagentManager` for enforcement only.
- Supporting / enforcement mechanisms: 40 ms overlapping-writer detection, config `parallelWrites`, terminal selector, serial mutex, git-worktree setup, child results/diffstat, `task_status` and `send_message`.
- Closure path: primary selects concurrent child roles/prompts → manager detects write contention and enforces selected isolation/serialization → child S1s work within resulting constraints → their results and branch changes return → primary revises future coordinated delegation.
- Boundary reachability: default-enabled plugin registers the agent-owned `task`/`send_message` tools and ships built-in independently executing children plus a write-specific first-party safeguard. Headless runs use serial writes without requiring interactive selection.
- Why this is / is not agent-owned: removal of the primary actor leaves only enforcement of already selected collision policies, not task-specific decisions about which child work should coexist or how results should alter subsequent child instructions. The operator's independent choice of safety mode is not falsely attributed to the model.
- Evidence: [`manager.ts`](https://github.com/GustavoGutierrez/alisio/blob/4a3c9c21b9e005f7bf8ebcd256bee5de60dc2e48/packages/plugin-subagents/src/manager.ts), [`index.ts`](https://github.com/GustavoGutierrez/alisio/blob/4a3c9c21b9e005f7bf8ebcd256bee5de60dc2e48/packages/plugin-subagents/src/index.ts), [`docs/subagents.md`](https://github.com/GustavoGutierrez/alisio/blob/4a3c9c21b9e005f7bf8ebcd256bee5de60dc2e48/docs/subagents.md), [`tests/subagents.test.ts`](https://github.com/GustavoGutierrez/alisio/blob/4a3c9c21b9e005f7bf8ebcd256bee5de60dc2e48/tests/subagents.test.ts).
- Basis: explicit interference guard plus structural independent child-agent decision/feedback path.
- Confidence: medium-high: S2 is bounded to one primary agent's cooperating child set, not a globally autonomous distributed coordinator.
- Caveats: the default interactive write-safety mode is chosen by the human rather than the model; agent autonomy lies in task-specific child coordination and feedback, with code enforcing write isolation.

## S3 — Inside-and-now control

- State: —
- Function: no separate whole-current system resource/commitment-control authority evidenced beyond parent task delegation.
- Disturbance / variety regulated: child task capacity, deadlines and token limits exist, but the shipped scheduling layer enforces configured caps instead of making a whole-system discretionary commitment decision.
- Decisive decision or feedback right: parent can launch/retry/message individual tasks; static runtime admits, queues, bounds or cancels sessions.
- Decision owner: no evidenced owner of whole-current resource bargaining, organizational priority negotiation or cross-unit accountability at the assessed recursion.
- Supporting / enforcement mechanisms: per-parent/global concurrency caps, queue, session tree, token budgets, TUI cancel/merge commands and `task_status`.
- Closure path: child work/reports reach parent and optional operator commands alter individual child execution; a separate whole-system resource/priority decision-return path is not established.
- Why this is / is not agent-owned: choosing an agent for a subtask and observing its progress is ordinary decomposition; structural limits do not give their enforcer discretion over present organization-wide commitments.
- Evidence: [`manager.ts`](https://github.com/GustavoGutierrez/alisio/blob/4a3c9c21b9e005f7bf8ebcd256bee5de60dc2e48/packages/plugin-subagents/src/manager.ts), [`config.ts`](https://github.com/GustavoGutierrez/alisio/blob/4a3c9c21b9e005f7bf8ebcd256bee5de60dc2e48/packages/plugin-subagents/src/config.ts), [`docs/subagents.md`](https://github.com/GustavoGutierrez/alisio/blob/4a3c9c21b9e005f7bf8ebcd256bee5de60dc2e48/docs/subagents.md).
- Basis: bounded first-party implementation inspection.
- Confidence: medium-high.
- Caveats: a custom primary prompt or outside orchestrator could exercise broader control, but it is not supplied by this standard runtime.

### Absence scope

- Surfaces inspected: parent/child tools, manager tree/status/queue, write policy, budgets, sessions and operator commands.
- Plausible first-party paths checked: `task_status` and `send_message` as whole-current management, concurrency caps as allocation, TUI cancel/merge as S3 and primary task division as commitment bargaining.
- Why no material first-party path remains: these are individual child task operations or enforcement of fixed limits; the shipped boundary does not establish a distinct agent-owned or parent-governed whole-current organizational decision over shared commitments and priorities.

## S3* — Complementary audit

- State: —
- Function: no independent operational-reality audit loop is wired to corrective control in the default product.
- Disturbance / variety regulated: code errors can be tested or reviewed, but no complementary evidence-based challenge of normal child reports is installed.
- Decisive decision or feedback right: a generic user-authored `reviewer` may read a diff, and output of ordinary tests returns to the producing agent; neither supplies first-party independent audit ownership.
- Decision owner: no built-in S3* audit actor established.
- Supporting / enforcement mechanisms: child role definition loader, read-only permissions, Git tools, testing and result wrappers warning that child reports are not authoritative.
- Closure path: ordinary tool/child results return to the primary operational path; no separately wired reviewer observation → audit judgment → corrective whole-control return.
- Why this is / is not agent-owned: a sample reviewer definition demonstrates composability but is not standard shipped audit closure or independent sampling of operational artifacts.
- Evidence: [`definitions.ts`](https://github.com/GustavoGutierrez/alisio/blob/4a3c9c21b9e005f7bf8ebcd256bee5de60dc2e48/packages/plugin-subagents/src/definitions.ts), [`manager.ts`](https://github.com/GustavoGutierrez/alisio/blob/4a3c9c21b9e005f7bf8ebcd256bee5de60dc2e48/packages/plugin-subagents/src/manager.ts), [`docs/subagents.md`](https://github.com/GustavoGutierrez/alisio/blob/4a3c9c21b9e005f7bf8ebcd256bee5de60dc2e48/docs/subagents.md).
- Basis: inspection of default agent catalog, delegation, returned results and optional reviewer example.
- Confidence: medium-high.
- Caveats: downstream users can configure reviewers, but the assessed standard mode does not prescribe independent audit inputs, authority and returned corrective action.

### Absence scope

- Surfaces inspected: shipped agent definitions, plugin registry, task results and notifications, terminal review commands and repository tests.
- Plausible first-party paths checked: built-in read-only `explore` as auditor, untrusted-result wrapper as independent verification, optional sample reviewer as a closed audit mode and test output as alternative evidence.
- Why no material first-party path remains: none is a first-party purpose-built complementary reviewer with a sufficiently independent operational-artifact judgment and a returned corrective governance loop.

## S4 — Outside-and-then intelligence

- State: —
- Function: no installed external/future-oriented capability adaptation loop is established.
- Disturbance / variety regulated: repeated session findings and environment information may be recorded, but prospective product redesign is not automatically selected or returned into the active harness.
- Decisive decision or feedback right: the active model can plan its current task, while user/config controls memory/provider/agents; neither decides an S4 future capability change from environmental scanning.
- Decision owner: no prospective organizational adaptation authority identified.
- Supporting / enforcement mechanisms: `@alisio/plugin-memory` SQLite search and compaction, provider switches, skills, customizable agents, model planning.
- Closure path: stored notes and retrieved context inform later coding requests; no environment horizon → adaptation options → selected durable capability change → current-control return is wired.
- Why this is / is not agent-owned: generic memory and user-configured plugins facilitate S1 decisions, but do not establish an S4-specific option-selection/implementation owner.
- Evidence: [`plugin-memory/src/index.ts`](https://github.com/GustavoGutierrez/alisio/blob/4a3c9c21b9e005f7bf8ebcd256bee5de60dc2e48/packages/plugin-memory/src/index.ts), [`plugin-memory/src/store.ts`](https://github.com/GustavoGutierrez/alisio/blob/4a3c9c21b9e005f7bf8ebcd256bee5de60dc2e48/packages/plugin-memory/src/store.ts), [`builtin.ts`](https://github.com/GustavoGutierrez/alisio/blob/4a3c9c21b9e005f7bf8ebcd256bee5de60dc2e48/packages/cli/src/builtin.ts).
- Basis: bounded memory/config/provider and runtime inspection.
- Confidence: medium-high.
- Caveats: a user's coding task may build future-facing software, but that is still S1 delivery without the organizational S4 loop.

### Absence scope

- Surfaces inspected: memory plugin and storage, skill/plugin loading, agent definitions, model/provider routing and core context compaction.
- Plausible first-party paths checked: stored long-term notes as environmental intelligence, main-agent `plan` mode as S4, user-authored agent evolution and model selection as prospect-driven adaptation.
- Why no material first-party path remains: these mechanisms retain/retrieve context or let a user change configuration; no shipped future-oriented environmental distinction is coupled to a decided, returned organizational capability adaptation.

## S5 — Policy and identity

- State: —
- Function: no legitimate ultimate identity/policy adjudication with return to the coding organization is established.
- Disturbance / variety regulated: untrusted shell/files and unsafe parallel edits trigger permissions/coordination choices, not institutional purpose conflicts between current and future viability.
- Decisive decision or feedback right: operator grants or refuses tool requests and chooses write-isolation posture; fixed config narrows sessions.
- Decision owner: operator owns local permissions but no function-specific ultimate organizational S5 decision circuit is installed.
- Supporting / enforcement mechanisms: trust settings, tool permission checks, child inheritance, bounded task scopes and interactive selection.
- Closure path: action approval/denial alters one operation; no identity-level issue reaches a legitimate parent who decides ultimate policy and returns that decision as a governing rule to subsequent organization-wide operation.
- Why this is / is not agent-owned: a permission gate, project config or human merge command does not create ultimate identity/ethos authority.
- Evidence: [`runner.ts`](https://github.com/GustavoGutierrez/alisio/blob/4a3c9c21b9e005f7bf8ebcd256bee5de60dc2e48/packages/core/src/core/runner.ts), [`manager.ts`](https://github.com/GustavoGutierrez/alisio/blob/4a3c9c21b9e005f7bf8ebcd256bee5de60dc2e48/packages/plugin-subagents/src/manager.ts), [`docs/subagents.md`](https://github.com/GustavoGutierrez/alisio/blob/4a3c9c21b9e005f7bf8ebcd256bee5de60dc2e48/docs/subagents.md).
- Basis: reviewed supported permissions, configuration and operator paths.
- Confidence: medium-high.
- Caveats: product maintainers govern releases at an adjacent recursion, not the assessed running session.

### Absence scope

- Surfaces inspected: project trust, child permission narrowing, tool approval, builtin configurations, worktree user decisions, OSS maintainer boundary.
- Plausible first-party paths checked: parent user as S5 through per-tool approval; model/system instructions as policy; write-mode selection as identity control; release maintainers as operating S5.
- Why no material first-party path remains: the available decisions concern per-operation safety or workflow settings, with no evidenced ultimate-policy question, legitimate S5 resolution and returned governing closure.

## Distributed OSS parent arrangement

The project is publicly maintained, but the local CLI does not expose the contributor organization's collective decisions as a current operating S3/S4/S5 control channel. The optional operator choices regulate task safety only; they are not organization-level parent-mode evidence.

## Self-hosted and non-human modes

The shipped agent can use user-chosen model endpoints and supports headless execution. Its builtin child sessions and collision guard remain reachable; headless write policy deterministically serializes concurrent writers rather than inventing a human decision. No separate legitimate S3/S4/S5 parent loop is supplied by model/provider configuration.

## Recursion

Parent and child sessions are distinct operational decision units in one coding assignment. Their nested depth is limited, but task nesting by itself does not prove full nested VSM viability. The assessed S2 is specific to sibling child contention, not a claim that each subagent is a full autonomous enterprise.

## Variety and escalation

Tool errors, approvals, subagent status/result notifications and overlapping-writer detection are transduced into parent decisions or deterministic safety constraints. Live task-tree/status helps the actor notice work state. Neither the queue nor a failed/cancelled task alone evidences an exceptional algedonic S3/S4/S5 decision path.

## Evidence gaps

- Native `pnpm typecheck` passes, and isolated `pnpm exec vitest run tests/subagents.test.ts` passes 19/19 without a live LLM. The full frozen-source suite, run after installing Bun and with a normal color-capable terminal, passes 815/819: three `tests/skills-manager-application.test.ts` cases fail with `Unknown built-in plugin: extra-provider`, and one `tests/tui-rich-render.test.ts` case expects Unicode tree glyphs but receives ASCII fallback. These are disclosed rather than mislabeled as a full green run; none is in the isolated tested subagent group. No test establishes successful model decisions, real-world inter-agent effectiveness or audit independence.
- The deterministic suite verifies writer-isolation constructs and result delivery, while the S2 ownership assignment is a source-based analysis of discretionary primary-model tool access, not an experiment using multiple connected LLMs.
- A user-supplied reviewer or external orchestration can create additional functions, but those cannot be credited to the standard-distribution boundary without first-party wiring and closure evidence.

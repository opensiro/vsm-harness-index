---
harness_id: cox
project_name: cox
repository: https://github.com/listepo/cox
review_ref: d4eb49f1f283f95d233785c452e3be8ea28cb5eb
reviewed_at: 2026-10-24
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-24
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# cox

## Review boundary

- System in focus: cox's first-party Rust coding-agent runtime, including the main model/tool Session, bundled concurrent child `agent` tool, task registry/relay, tool/runtime permissions, optional worktree isolation and standard CLI/headless/ACP/MCP surfaces.
- Purpose and identity: carry out coding and repository tasks with streamed model decisions and real tool feedback; delegate investigations or bounded shell work while preserving workspace permissions, cost accountability and local operator control.
- Relevant environment: changing source trees, collisions among concurrent model-backed worker edits, tool errors, user interruptions, provider availability, shared spend capacity, background task progress and external research requested by coding tasks.
- Standard-distribution boundary: pinned `listepo/cox` Rust workspace and bundled core, tools, CLI/editor/MCP adapters, documented supported modes and configured first-party subagent presets. Custom user-authored `.cox/agents`, `.claude/agents`, plugins, external Cursor agents and development/benchmark organizations do not supply additional uninstantiated autonomous owners.
- Credited operating / distribution surfaces: main model/tool turn loop, bundled `agent` tool with `explore`/`shell` independent sessions, optional foreground/background children, task messages and resumption, explicit worktree isolation, shared child concurrency cap and budget slices, permission engine, session/task output and TUI status.
- Adjacent first-party surfaces excluded from ownership: evals/ scripted-provider test harness and token benchmarks, developer `plan.md`/`research.md` and design review commentary, docs/ website build/CI, example plugins including external-agent driver and user-added reviewer definitions not invoked in a shipped review pathway.
- First-party operating / deployment modes considered: terminal UI, headless/stream-json, ACP/MCP adapters to the same core, bundled child `explore` and `shell` agent tools, optional `background` tasks, optional child `isolation: worktree`, addressed `send_message`, operator approval and memory-extraction settings.
- Recursion level: one current cox session organization with a main model manager and multiple bounded, separately model-driven child operating cells. Child sessions have their own immediate work, contexts and budgets but are not shown to carry a full independent S3–S5 viable-system metasystem.
- Reviewed revision: `d4eb49f1f283f95d233785c452e3be8ea28cb5eb` (batch #1013 row 8), observed 2026-10-24.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

cox is a Rust workspace exposing one `Submission` → `cox-core::Session` → `Event` model/tool state machine to native TUI, command-line one-shot, ACP and MCP surfaces. The model chooses read/search/write/bash/tool calls, permission/budget controls admit them, and real results enter later model requests. The core installs a first-party `agent` tool on main sessions: independently model-driven child sessions receive a delegated task, a restricted tool set, selected tier and own slice of the parent's money budget. `explore` is read-only; `shell` can invoke bash/web tools. Foreground tasks return bounded results; background tasks run concurrently and report named task identifiers and results.

Distinct from one-shot delegation, the pinned code maintains a parent-owned registry of running and finished children and names. Parent and children can send direct follow-up instructions to a task; a running child queues the message behind its current turn, a finished child resumes with prior history and bounded new slot. The protocol limits causal message hops and received-message counts, preventing runaway sibling ping-pong; the parent alone routes child-to-child messages. The main model can also deliberately select `isolation: worktree` per delegated job: cox builds an isolated Git checkout/branch with a separate writable root, and reports its location to the parent when finished. This prevents concurrent coding workers from silently overwriting the parent's checkout. The cap on concurrently running children is enforced by an atomic reservation independent of the model's choice of which tasks to start.

The TUI shows running/finished task state and agent activity; task completion and message receipts reach main session history. The parent model therefore can use whole-current task information to revise children’s instructions and allocate new subtasks/budgets, while the deterministic runtime owns slot reservation and scheduling. Ordinary tests/evals and model-assisted end-of-session memory extraction are adjacent or current-history aids, not independently instantiated S3* audit/S4 strategy. Source: [README](https://github.com/listepo/cox/blob/d4eb49f1f283f95d233785c452e3be8ea28cb5eb/README.md), [how it works](https://github.com/listepo/cox/blob/d4eb49f1f283f95d233785c452e3be8ea28cb5eb/docs/how-it-works.md), [Session](https://github.com/listepo/cox/blob/d4eb49f1f283f95d233785c452e3be8ea28cb5eb/crates/cox-core/src/session.rs), [subagents](https://github.com/listepo/cox/blob/d4eb49f1f283f95d233785c452e3be8ea28cb5eb/crates/cox-core/src/subagent.rs), [tasks](https://github.com/listepo/cox/blob/d4eb49f1f283f95d233785c452e3be8ea28cb5eb/crates/cox-core/src/tasks.rs).

## Operational model

The primary coding model can work directly or authorize real delegated child sessions with separate model/tool turn sequences. Subagent calls are concurrently dispatched; each child is an S1 operating contributor, not just a tool-thread. The parent sees assignment/start/completion, returns instructions via `send_message` and can choose worktree isolation for editing work that would interfere with other cells. Atomic shared limits and message queues support the organizational decisions but do not themselves own the model's choice. No live LLM agents, model providers or Browser quality tests were executed; evidence is frozen source and deterministic Index validation.

## S1 — Operations

- State: A
- Function: respond autonomously to changing code and shell/web evidence while producing user-requested project outcomes.
- Disturbance / variety regulated: missing information, source changes, test failures, conflicting implementation constraints, task-specific uncertainty and tool errors.
- Decisive decision or feedback right: choose tools, file changes, investigative steps, new child tasks and follow-up actions based on actual observations.
- Decision owner: main model-backed Session; delegated `explore`/`shell` child Sessions separately own bounded model/tool decisions for assigned contributions.
- Supporting / enforcement mechanisms: protocol Event stream, provider adapters, tool traits, sandbox, permission engine, context archiving and budget/failure gates.
- Closure path: user/parent task → model request → model tool decision → first-party execution → tool result/feedback → further model task action or answer.
- Boundary reachability: main sessions install the agent tool, built-in workspace tools and provider-neutral loop; children create separate Sessions and run real model requests as shipped behavior.
- Why this is / is not agent-owned: the model selects and revises substantive operations; deterministic event and permission machinery cannot decide the code changes.
- Evidence: [turn engine](https://github.com/listepo/cox/blob/d4eb49f1f283f95d233785c452e3be8ea28cb5eb/crates/cox-core/src/turn.rs), [session construction](https://github.com/listepo/cox/blob/d4eb49f1f283f95d233785c452e3be8ea28cb5eb/crates/cox-core/src/session.rs), [child dispatch](https://github.com/listepo/cox/blob/d4eb49f1f283f95d233785c452e3be8ea28cb5eb/crates/cox-core/src/subagent.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: no live effectiveness measurement; bundled default child presets are narrower than user-defined agents.

## S2 — Coordination

- State: A
- Function: attenuate inter-worker source mutation clashes through an explicitly selected separate writable worktree for each independently acting child S1.
- Disturbance / variety regulated: parallel shell/coding workers sharing a mutable checkout can overwrite or invalidate each other's workspace effects; parent-to-child directions also must not corrupt the child's running turn.
- Distinct S1 units: the main coding Session and separately model-driven `agent` child sessions; multiple children can run concurrently with their own delegated tasks, histories and tool actions.
- Inter-S1 disturbance: concurrent writable `shell`/custom worker operations can change common project files and invalidate another's assumptions or overwrite the main agent's edits.
- Attenuating coordination relation: the parent model can choose `agent(isolation: "worktree")` per worker to separate mutation domains and stop shared checkout effects. Parent-to-child follow-ups are queued to turn boundaries. The implemented sibling relay has causal-hop and reception limits but built-in child presets do not expose `send_message` to children; no default child-to-child messaging topology is claimed.
- Feedback into subsequent S1 behaviour: isolated child executes in its own Git worktree; completion names the branch for parent integration, and messages become the addressee's next model turn (including resumed completed children), so later actions can adjust based on the coordination decision.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: model-selected isolation addresses the specific shared-checkout interference of concurrently acting child workers; message delivery is supporting current-task feedback, not credited as independent S2 merely because messages can be routed.
- Decisive decision or feedback right: select whether each agent task requires isolated mutation space and what conflict-resolution instruction to send a particular running/finished child.
- Decision owner: parent model for optional isolation and task-specific follow-up decisions; fixed protocol queue/cap behavior belongs to the developer/runtime, not to the model.
- Supporting / enforcement mechanisms: Git worktree creation/owner locks, deterministic task registry and relay, message delivery caps for optional custom-agent modes, atomic child slot reservations.
- Closure path: parallel task planning/concurrent effect risk → parent chooses isolation and/or directed follow-up → runtime creates isolated branch/queues one child turn → child adapts actions on its actual workspace/instructions → returned branch/response informs subsequent parent/worker decisions.
- Boundary reachability: `agent` is installed into standard Sessions; its advertised `isolation` input calls the shipped worktree interface configured by CLI, while core `send_message`/task registry supports parent and child messaging in the normal loop.
- Why this is / is not agent-owned: the parent model explicitly selects a function-specific effect-domain option and message contents for live worker conflict management; deterministic locks and flood caps merely enforce selected and fixed constraints.
- Evidence: [AgentTool options and dispatch](https://github.com/listepo/cox/blob/d4eb49f1f283f95d233785c452e3be8ea28cb5eb/crates/cox-core/src/subagent.rs), [task relay/guards](https://github.com/listepo/cox/blob/d4eb49f1f283f95d233785c452e3be8ea28cb5eb/crates/cox-core/src/tasks.rs), [worktree implementation](https://github.com/listepo/cox/blob/d4eb49f1f283f95d233785c452e3be8ea28cb5eb/crates/cox-tools/src/git.rs), [normal-session worktree wiring](https://github.com/listepo/cox/blob/d4eb49f1f283f95d233785c452e3be8ea28cb5eb/crates/cox/src/session.rs).
- Basis: explicit + structural.
- Confidence: medium.
- Caveats: worktree isolation is opt-in, not default; no proof that agents always choose it or merge correctly. Built-in `explore`/`shell` child presets do not grant sibling `send_message`, so optional custom-agent relay capabilities are not evidence for this S2 state.

## S3 — Inside-and-now control

- State: A
- Function: govern the active team of independently progressing worker commitments under a shared parent task and budget by allocating bounded jobs and redirecting ongoing assignments.
- Disturbance / variety regulated: oversubscribed child budgets/capacity, stalled or no-longer-useful subtasks, changing parent priorities, delayed responses and an active portfolio whose work must still support one goal.
- Whole-system current view: parent tracks child IDs/names and running/finished state via the task registry and receives TaskCreated/TaskCompleted, usage/result notices and child-to-parent messages; the TUI `/tasks` and `/agents` views expose the active set to its operator.
- Current-control decision scope: the parent model chooses which children to create, the tasks/presets, relative spend slices and isolation and can direct running or finished child sessions with new instructions; fixed concurrency and permission rules enforce bounds.
- Decisive decision or feedback right: select/revise concurrent child commitments in light of existing job responses, cost and new overarching task requirements.
- Decision owner: the main cox model, as current manager of its spawned S1 worker team. Operator can steer and approve specific operations, but no separate parent-governed S3 portfolio mode is claimed.
- Supporting / enforcement mechanisms: child task registry, shared budget accounting, atomic `max_concurrent_subagents` reservations, per-child cost slices, background task notices, `send_message` relay and user-visible task status.
- Closure path: whole-team known task IDs/progress and changing objective → parent model allocates bounded jobs or sends revised task direction → runtime spawns, resumes or queues the targeted child → child does new work and returns cost/results to the parent.
- Boundary reachability: `AgentTool` is registered in main sessions, task ownership and message delivery are wired through ordinary runtime, and child progress is returned to the same main model context; no user-script manager or development-only orchestration is borrowed.
- Why this is / is not agent-owned: selecting and revising commitments across independently model-backed children requires parent model judgment; slot guards and cost accounting cannot choose which job matters next.
- Evidence: [Session agent registration and task identity](https://github.com/listepo/cox/blob/d4eb49f1f283f95d233785c452e3be8ea28cb5eb/crates/cox-core/src/session.rs), [AgentTool budget/child creation](https://github.com/listepo/cox/blob/d4eb49f1f283f95d233785c452e3be8ea28cb5eb/crates/cox-core/src/subagent.rs), [task status and parent feedback](https://github.com/listepo/cox/blob/d4eb49f1f283f95d233785c452e3be8ea28cb5eb/crates/cox-core/src/tasks.rs), [UI current task view](https://github.com/listepo/cox/blob/d4eb49f1f283f95d233785c452e3be8ea28cb5eb/crates/cox-tui/src/tasks.rs).
- Basis: structural.
- Confidence: medium.
- Caveats: this is a bounded **current child-team** view, not cross-repository enterprise governance; no empirical demonstration of quality or optimal budget reallocation is claimed. Generic decomposition alone would not suffice without the active feedback/resumption/revision path.

## S3* — Complementary audit

- State: —
- Function: no shipped independently controlled review judgment using complementary direct operational evidence and binding corrective feedback is instantiated.
- Disturbance / variety regulated: routine test failures, build output, tool permission issues and correctness claims can be checked by the same operational agent; that alone is not distinct audit.
- Claim being audited: whether coded changes meet requested quality/correctness beyond the coding actor's own report.
- Ordinary reporting path: shell/test tool results and child output/rollout summaries return to parent coding context.
- Complementary access path: read-only `explore` child may inspect files, but is a generic delegable investigator; tests and sample named `reviewer` presets are not shipped with a required independent reviewer judgment and corrective return.
- Independence boundary: a separately instantiated evidence-bearing review agent with authority to challenge operational claims is not wired by default; optional user-authored agent definitions cannot be assumed to exist.
- Who acts on findings: parent model/operator reacts to tool or child findings as normal coding decisions, not mandatory or independent S3* control.
- Decisive decision or feedback right: no distinct audit judgment owner established, although any authorized coding/test process may report diagnostics.
- Decision owner: operational model and configured tools, not a separate first-party audit actor.
- Supporting / enforcement mechanisms: shell/test tools, archived outputs, evals/ and user-configurable child presets.
- Closure path: tool/test report → coding model action exists; independent audit probe → separate judgment → returned S3 correction is not instantiated.
- Why this is / is not agent-owned: agent-directed code review can be composed by users, but shipped generic exploration and same-task test outcomes do not confer independent complementary audit ownership.
- Evidence: [presets and dynamic definitions](https://github.com/listepo/cox/blob/d4eb49f1f283f95d233785c452e3be8ea28cb5eb/crates/cox-core/src/subagent.rs), [tool-output workflow](https://github.com/listepo/cox/blob/d4eb49f1f283f95d233785c452e3be8ea28cb5eb/docs/how-it-works.md), [eval harness](https://github.com/listepo/cox/blob/d4eb49f1f283f95d233785c452e3be8ea28cb5eb/evals/src/cox_evals/harness.py).
- Basis: structural bounded absence review.
- Confidence: medium-high.
- Caveats: an operator could explicitly create a reviewer subagent, but that would be a different composed operating mode needing its own evidence.

### Absence scope

- Surfaces inspected: bundled `explore`/`shell` presets, child creation and tests, task results, external-agent/plugin examples, eval scripts and core hooks.
- Plausible first-party paths checked: read-only child as S3* reviewer, ordinary automated tests as independent audit, model/plugin judge helpers and evaluation fixtures as an operational auditor.
- Why no material first-party path remains: none wires a separate evidence-facing audit judgment into routine or optional product control; available checks are generic task work or adjacent development evaluations.

## S4 — Outside-and-then intelligence

- State: —
- Function: no shipped autonomous externally and prospectively oriented capability-option search and adoption return to present organizational operation.
- Disturbance / variety regulated: current task web context, provider/model suitability and accumulated session facts are handled for immediate execution or remembered context.
- Decisive decision or feedback right: no distinct decision over future harness capabilities based on horizon scanning and tested alternatives.
- Decision owner: operator/developers choose available models, plugins, future roadmap work and package settings; the current model selects task actions.
- Supporting / enforcement mechanisms: tier router, model metadata, optional plugin advice, web_fetch, end-of-session memory extraction and config changes.
- Closure path: current task information → tool/tier/model decisions and retained facts exists; future environmental model → adaptation option → adopted current capability is not instantiated.
- Why this is / is not agent-owned: budget-aware tier selection and extracted task facts are not prospectively changing the organization's capability or policy.
- Evidence: [model route advice](https://github.com/listepo/cox/blob/d4eb49f1f283f95d233785c452e3be8ea28cb5eb/crates/cox-core/src/advise.rs), [memory extraction](https://github.com/listepo/cox/blob/d4eb49f1f283f95d233785c452e3be8ea28cb5eb/crates/cox-core/src/memory_extract.rs), [project README](https://github.com/listepo/cox/blob/d4eb49f1f283f95d233785c452e3be8ea28cb5eb/README.md).
- Basis: structural bounded absence review.
- Confidence: medium-high.
- Caveats: development plans and external advisory plugins could produce strategy elsewhere, but are outside the reviewed shipped decision closure.

### Absence scope

- Surfaces inspected: model routing/decide advice, plugin mechanisms, web tools, session memory extraction and durable state, config and the repository's development research/roadmap.
- Plausible first-party paths checked: memory extraction as strategy, cheaper model routing as organizational adaptation, external-agent/plugin availability as horizon sensing and maintainer roadmap as in-product S4.
- Why no material first-party path remains: these represent cost optimization, context retention or external human design; no S4 option-development and operational-capability adoption loop is connected in the standard distribution.

## S5 — Policy and identity

- State: —
- Function: no runtime institution owns final identity/ultimate-policy decisions and returns them into later operation at cox's assessed session recursion.
- Disturbance / variety regulated: risky tool calls, spending limits and access to secret/out-of-workspace paths are handled by fixed policies and operator approvals, not a durable ethos/identity deliberation loop.
- Identity / ultimate-policy issue: system role and mission are configured by shipped prompts and user task; no in-product authority resolves a dispute about the harness's ultimate purpose.
- Ultimate authority in each claimed mode: no positive S5 mode; user/developer sets permissions, model tiers, configuration and source behavior.
- Return-to-operation path: permission denial/approval changes concrete tool execution; identity-level question → legitimate ultimate parent decision → binding return is not established.
- Decisive decision or feedback right: granular tool-approval and configuration decisions, not ultimate policy/identity adjudication.
- Decision owner: operator for per-tool authorization and developer for product defaults; neither closes a first-party identity-level parent loop.
- Supporting / enforcement mechanisms: `cox_permission` engine, sandbox, redaction and plugin capability restrictions.
- Closure path: tool risk classification → allow/ask/deny → tool outcome; no identifiable S5 identity controversy and authoritative return.
- Why this is / is not agent-owned: the agent executes under fixed/user policies, while legitimate identity decisions are not delegated or procedurally fed back at this recursion.
- Evidence: [permission workflow](https://github.com/listepo/cox/blob/d4eb49f1f283f95d233785c452e3be8ea28cb5eb/docs/how-it-works.md), [runtime tool safety](https://github.com/listepo/cox/blob/d4eb49f1f283f95d233785c452e3be8ea28cb5eb/crates/cox-core/src/turn.rs), [configuration](https://github.com/listepo/cox/blob/d4eb49f1f283f95d233785c452e3be8ea28cb5eb/docs/config.md).
- Basis: structural bounded absence review.
- Confidence: high.
- Caveats: upstream OSS governance and commercial licensing are different organizations/recursion levels and are excluded.

### Absence scope

- Surfaces inspected: prompt and configuration, permission engine/approvals, model tiers, plugins, working-directory protection, maintainer governance and licensing files.
- Plausible first-party paths checked: operator tool approval as parent S5, plugin policy decision as constitutional authority, model router as purpose changer and maintainer policies as runtime S5.
- Why no material first-party path remains: each controls an operational call, config or development process; no supported ultimate identity/policy adjudication-and-return path is wired into the coding Session.

## Distributed OSS parent arrangement

Project maintainers and separate cox installations do not share a bundled runtime parent-governance process. The model-run organization is the declared parent plus bounded child Sessions, not the upstream GitHub contributor organization or commercial licensing regime.

## Self-hosted and non-human modes

All shipped local surfaces use the same core; the main model may own current child-team management while users retain tool authorization. Worktree isolation is opt-in and model-selectable; a client or plugin may extend the arrangement but does not automatically become a parent S3/S4/S5 owner.

## Recursion

Each child has its own task, environment, model/tool decisions, bounded budget and named session, but lacks an independently demonstrated full metasystem and ultimate purpose. A nested child Session is therefore a distinct S1 operating cell of the current task team, not proof of a separate recursively viable organization.

## Variety and escalation

Parallel subagents and plugin/provider/tool choice amplify coding response variety; optional worktree isolation attenuates shared-source collision. The task relay is turn-bounded, and its anti-oscillation caps apply if an eligible custom child has messaging access. The parent model sees individual job feedback and can revise active commitments, while permission/budget machines enforce constraints. Runtime errors, budget denial and approval requests escalate to the human; none automatically establishes S3*, S4 or S5.

## Evidence gaps

- S2=A relies on the supported optional model-selected `isolation: worktree` and addressed agent-to-agent revision path, not on the mere existence of a message bus or static concurrency limit. Empirical contention reduction and model selection frequency were not measured.
- S3=A is bounded to the current child-team operating level, with task registry/status, cost and follow-up authority; it does not claim a company/portfolio management layer or uninterrupted real-time model dashboard.
- Named `reviewer` examples in protocol unit tests and user-created custom agents do not instantiate an independent first-party auditor in the standard distribution.
- Design documents may describe superseded plans; active Rust source at the frozen SHA controls the assessment. No external LLM or live provider/Browser quality test was run.

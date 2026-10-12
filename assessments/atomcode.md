---
harness_id: atomcode
project_name: AtomCode
repository: https://github.com/karlorz/atomcode
review_ref: 152b2cc132dda9b177c3a030e21cfacd95494ea3
reviewed_at: 2026-10-12
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# AtomCode

## Review boundary

- System in focus: AtomCode's shipped Rust coding agent distributed through the terminal/headless/ACP and related first-party session entry points, composed of the `atomcode-coding` assembly, the model-driven agent/kernel loop, first-party tools, and an optionally callable in-session `code_review` child reviewer.
- Purpose and identity: a local coding assistant that autonomously reads/changes repository files, executes commands and tests, pursues bounded goals, reviews current changes via a separate read-only reviewer when invoked, and persists sessions for continuation.
- Relevant environment: Git workspace, shell/filesystem, configured LLM API/provider, structured model function calls, tool authorization and path policies, optional local TUI/browser/daemon clients, per-turn memory and saved sessions.
- Standard-distribution boundary: the released first-party `crates/atomcode-coding`, `atomcode-kernel`, `atomcode-core`, `atomcode-capabilities`, `atomcode-review`, `atomcode-cli` and associated shipped runtime modes. External providers, upstream AtomGit services, third-party MCP tools, arbitrary user-defined skills and development benchmark runners remain dependencies or adjacent actors rather than credited owners.
- Credited operating / distribution surfaces: Rust coding-agent composition, `AgentLoop`, `TurnRunner`, first-party file/shell/code tools, goal and post-edit check paths, the `ReviewTool` subagent wiring, read-only review assembler/persona/report finding tool, local session and permissions.
- Adjacent first-party surfaces excluded from ownership: repository CI/release, benchmark/evaluation harnesses, benchmark-only review runs, contributor governance and README claims without matching shipped wiring; the separately packaged **shipped and wired** `atomcode-review` child *is included* because `atomcode-coding/src/parts.rs` explicitly mounts it in the standard runtime.
- First-party operating / deployment modes considered: normal interactive/headless coding, plan/build mode, user-invoked goal/loop continuation, optional background task sessions, a first-party callable `code_review` tool (enabled by default in `PrepareOptions`), and user review command surfaces where present; standard provider/session and local permission policies.
- Recursion level: one coding session is the focal operational system. The read-only reviewer is a separately instantiated complementary child at a lower recursion, not another independently running S1 development team. Any per-file subagents remain bounded local subordinate units.
- Reviewed revision: 152b2cc132dda9b177c3a030e21cfacd95494ea3.
- Observation date: 2026-10-12.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

AtomCode's Rust kernel hosts a model/tool feedback loop. `atomcode-coding` prepares coding capabilities and composes a provider-backed agent. The tool registry includes source/file edit, shell, search, code-symbol and web tools, subject to approval and working-directory safety. The model selects actions, receives tool results and advances the session; code verification may be prompted after writes, and goal evaluation can extend one coding task beyond a normal stopping turn. Those are ordinary S1 regulation and deterministic support; they do not automatically establish S3.

A parallel per-file subagent pool exists in `atomcode-core/src/agent/parallel_edit.rs`. Its bounded execution, tool filters, independent child contexts, retry/timeout budgets and ordered results are useful for decomposing coding operations. Source review did not identify a first-party concrete cross-subagent conflicting-file integration/arbitration path feeding back into each operating child; a scheduler/JoinSet is not itself S2. Similarly, background sessions and goal modes do not supply a whole-current model-governed resource/commitment controller over a population of independent S1 units merely by name.

Most importantly, standard `atomcode-coding/src/parts.rs` sets `PrepareOptions.review=true` by default and registers `ReviewTool` as the model-callable `code_review` tool. That tool computes the current Git diff in the actual live workdir (or staged/base), annotates changed lines and risk rules, creates a **fresh independent reviewer Agent** with a different read-only persona and direct read/grep/AST/code-graph access to surrounding files. The reviewer cannot write files, execute shell commands or inherit the implementing agent's mutable tool set; path-confinement blocks reads outside the review root. Its `report_finding` tool accumulates structured defect findings, which are restricted to changed files, sorted and returned to the implementing parent tool loop. The parent can then decide corrections and repeat operation. A shared model provider does not imply shared review conversation or implementation authority. This concrete optional first-party mode meets complementary audit rather than same-agent verification.

Key primary-source evidence:
- [Coding session/prepare defaults and review mounting](https://github.com/karlorz/atomcode/blob/152b2cc132dda9b177c3a030e21cfacd95494ea3/crates/atomcode-coding/src/parts.rs)
- [Coding kernel and tool-driven agent loop](https://github.com/karlorz/atomcode/blob/152b2cc132dda9b177c3a030e21cfacd95494ea3/crates/atomcode-kernel/src/agent.rs)
- [AgentLoop source and ordinary task verification](https://github.com/karlorz/atomcode/blob/152b2cc132dda9b177c3a030e21cfacd95494ea3/crates/atomcode-core/src/agent/mod.rs)
- [Normal post-edit verification path](https://github.com/karlorz/atomcode/blob/152b2cc132dda9b177c3a030e21cfacd95494ea3/crates/atomcode-core/src/agent/verify.rs)
- [Per-file parallel child tasks and deterministic pool](https://github.com/karlorz/atomcode/blob/152b2cc132dda9b177c3a030e21cfacd95494ea3/crates/atomcode-core/src/agent/parallel_edit.rs)
- [Background task facilities](https://github.com/karlorz/atomcode/blob/152b2cc132dda9b177c3a030e21cfacd95494ea3/crates/atomcode-core/src/agent/background.rs)
- [Goal continuation evaluator](https://github.com/karlorz/atomcode/blob/152b2cc132dda9b177c3a030e21cfacd95494ea3/crates/atomcode-core/src/agent/goal_evaluator.rs)
- [ReviewTool: live Git diff, independent child and feedback](https://github.com/karlorz/atomcode/blob/152b2cc132dda9b177c3a030e21cfacd95494ea3/crates/atomcode-review/src/review_tool.rs)
- [Fresh read-only reviewer assembly and mounted tools](https://github.com/karlorz/atomcode/blob/152b2cc132dda9b177c3a030e21cfacd95494ea3/crates/atomcode-review/src/assemble.rs)
- [Reviewer-only source path confinement](https://github.com/karlorz/atomcode/blob/152b2cc132dda9b177c3a030e21cfacd95494ea3/crates/atomcode-review/src/confine.rs)
- [Independent reviewer persona](https://github.com/karlorz/atomcode/blob/152b2cc132dda9b177c3a030e21cfacd95494ea3/crates/atomcode-review/src/persona.rs)
- [Normal coding tools, sessions and safety overview](https://github.com/karlorz/atomcode/blob/152b2cc132dda9b177c3a030e21cfacd95494ea3/README.md)

## Operational model

The main coding model operates through a first-party Rust tool loop. Work units may be delegated to file-scoped children or continued in a goal mode, but no separately closed whole-current supervising organization is presumed. A code review is a different operation: the host explicitly invokes a distinct read-only reviewing model agent over actual source/diff evidence, receives attributable structured findings and can correct implementation. Both the reviewer and implementer may use the same API provider/model family, but their conversations, tool scopes, permissible actions and judgment purposes are independent in the shipped path.

## S1 — Operations

- State: A
- Function: perform and verify software changes through the model/tool/feedback loop.
- Disturbance / variety regulated: user requests, repository contents, compiler/test failures, tool results, budget/goal conditions, provider output and permissions.
- Decisive decision or feedback right: choose the next coding tool/action, revise a patch based on feedback, invoke review, and decide task completion.
- Decision owner: main model-backed coding agent (and bounded child coding models for delegated file tasks).
- Supporting / enforcement mechanisms: kernel `Agent` and `TurnRunner`, coding tool registry, permissions, turn budgets, session, goal evaluator, post-edit verification, notifications.
- Closure path: prompt → model-chosen code/tool action → first-party tool execution → returned observation → further model reasoning/action or final response.
- Boundary reachability: the standard coding-agent assembly builds this loop and registers first-party tools for interactive/headless use.
- Why this is / is not agent-owned: the runtime enforces scope, timeouts and dispatch, but the model retains the task-specific code operation choices.
- Evidence: [kernel agent](https://github.com/karlorz/atomcode/blob/152b2cc132dda9b177c3a030e21cfacd95494ea3/crates/atomcode-kernel/src/agent.rs), [coding assembly](https://github.com/karlorz/atomcode/blob/152b2cc132dda9b177c3a030e21cfacd95494ea3/crates/atomcode-coding/src/parts.rs), [core loop](https://github.com/karlorz/atomcode/blob/152b2cc132dda9b177c3a030e21cfacd95494ea3/crates/atomcode-core/src/agent/mod.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: external model/provider availability is a dependency rather than a credited system owner.

## S2 — Coordination

- State: —
- Function: no bounded first-party inter-S1 interference-specific coordination/feedback loop is evidenced.
- Disturbance / variety regulated: parallel child edits could conflict over a shared repository, but deterministic per-file task partition, queueing and concurrency caps do not show incompatible-change detection/attenuation with returned child correction.
- Decisive decision or feedback right: no distinct S2-specific arbitration right established.
- Decision owner: not established for S2.
- Supporting / enforcement mechanisms: `SubAgentPool` concurrent `JoinSet`, per-file `SubAgentTask`, timeout/retry limits, child tool filtering, progress/result events.
- Closure path: task results return to the main coding model, but no specific inter-S1 conflicting-operation attenuation/return relationship was reconstructed.
- Boundary reachability: no positive S2 path claimed.
- Why this is / is not agent-owned: selecting one file per child reduces a possible overlap by design, but this is decomposition/serialization; it is not a demonstrated organizational S2 controller that senses interaction disturbances and changes subsequent S1 work.
- Evidence: [parallel_edit.rs](https://github.com/karlorz/atomcode/blob/152b2cc132dda9b177c3a030e21cfacd95494ea3/crates/atomcode-core/src/agent/parallel_edit.rs), [background.rs](https://github.com/karlorz/atomcode/blob/152b2cc132dda9b177c3a030e21cfacd95494ea3/crates/atomcode-core/src/agent/background.rs).
- Basis: structural.
- Confidence: medium-high.
- Caveats: does not mean agents can never be assembled into an S2-capable multi-team configuration; no unsupported cross-agent owner imported here.

### Absence scope

- Surfaces inspected: subagent pool task/data structures and result/error events, child work scopes, background mode and task/goal continuation paths.
- Plausible first-party paths checked: per-file parallel fanout, concurrency/timeout limits, child tool availability, response aggregation and head-agent follow-up.
- Why no material first-party path remains: no wired first-party conflict-detect/arbiter/return mechanism specific to disturbances BETWEEN independently operating S1 children was verified.

## S3 — Inside-and-now control

- State: —
- Function: no distinct current whole-system manager owning resource/commitment discretion across a live set of S1 units was reconstructed from the shipped modes.
- Disturbance / variety regulated: goal progress, turn caps and individual background sessions are tracked, but this is operation-level control.
- Decisive decision or feedback right: no separate whole-current portfolio/priority/commitment decision over multiple S1 units.
- Decision owner: not established for S3.
- Supporting / enforcement mechanisms: goal-evaluation continuation, turn-level progress/budget guard, per-file subagent pool, background task session control, CLI/TUI status.
- Closure path: current coding work may continue or stop based on model feedback and deterministic budgets, without a separate S3 current supervisory return.
- Boundary reachability: no positive S3 path claimed.
- Why this is / is not agent-owned: goal-mode agents and deterministic background schedulers act on bounded coding tasks; they do not automatically own overall current organizational commitments.
- Evidence: [goal evaluator](https://github.com/karlorz/atomcode/blob/152b2cc132dda9b177c3a030e21cfacd95494ea3/crates/atomcode-core/src/agent/goal_evaluator.rs), [goal lifecycle](https://github.com/karlorz/atomcode/blob/152b2cc132dda9b177c3a030e21cfacd95494ea3/crates/atomcode-core/src/agent/goal.rs), [subagent pool](https://github.com/karlorz/atomcode/blob/152b2cc132dda9b177c3a030e21cfacd95494ea3/crates/atomcode-core/src/agent/parallel_edit.rs), [background agent](https://github.com/karlorz/atomcode/blob/152b2cc132dda9b177c3a030e21cfacd95494ea3/crates/atomcode-core/src/agent/background.rs).
- Basis: structural.
- Confidence: medium-high.
- Caveats: the model has real choice within individual tasks; that is credited S1, not general whole-current management.

### Absence scope

- Surfaces inspected: goal evaluator/controller, background agent, parallel task pool, current CLI/daemon status and agent loop.
- Plausible first-party paths checked: long-running goals, background sessions, parallel subagent result aggregation and budget enforcement.
- Why no material first-party path remains: no first-party model manager with entire currently active S1 commitment view, substantive managerial right and returned intervention to the subordinate active set was demonstrated.

## S3* — Complementary audit

- State: A
- Function: in the separately callable shipped `code_review` mode, independently inspect actual changed source and Git diff, judge implementation defects, and return structured findings for coding-agent correction.
- Disturbance / variety regulated: divergence between an implementer's reported success and defects in actual changed code, APIs, correctness/security/reliability implications.
- Decisive decision or feedback right: independently decide/report defect findings from a direct evidence path, not merely relay implementing agent's own tool outcomes.
- Decision owner: distinct read-only reviewer `Agent` with a dedicated persona, message context and tool set; the implementing main model owns follow-up corrective code operations.
- Supporting / enforcement mechanisms: first-party ReviewTool, live `git diff`, diff line annotations and impact/risk plan, review-only registry, path confinement, structured `report_finding` sink, change-scope filter and findings sorting, provider reuse.
- Closure path: parent/host model invokes `code_review` → tool obtains Git diff from LIVE workspace → separate reviewer inspects surrounding source, reports findings → tool returns structured evidence to host model → host can revise code and re-run checks/review.
- Boundary reachability: shipped `PrepareOptions::default().review=true`, `parts.rs` registers `ReviewTool` in coding agent tool registry, fills its shared provider on assembly; the `code_review` tool then instantiates a fresh restricted read-only reviewer with direct repository access. No custom extension or benchmark-only setup is needed.
- Why this is / is not agent-owned: the separate reviewer model determines actual defect judgments, while Git diff retrieval, access confinement and rendering are deterministic supports; a common provider does not share agent history or mutable authority.
- Claim being audited: actual worktree/staged/base code changes relative to the implementation task, not only the main agent's self-report.
- Ordinary reporting path: main coding-agent messages, tool results, tests and same-agent post-edit verification.
- Complementary access path: independent reviewer starts from live Git diff, directly reads/greps/inspects source via its restricted tool registry, and writes structured `report_finding` judgments.
- Independence boundary: fresh read-only reviewer agent with own persona/messages and no write/edit/bash tools, path-confined to repo; possible shared LLM provider/model family is a dependency and not a common decision context.
- Who acts on findings: invoking primary coding model receives prioritized results and may modify code or request more tests; review tool itself remains read-only.
- Evidence: [ReviewTool](https://github.com/karlorz/atomcode/blob/152b2cc132dda9b177c3a030e21cfacd95494ea3/crates/atomcode-review/src/review_tool.rs), [read-only child build](https://github.com/karlorz/atomcode/blob/152b2cc132dda9b177c3a030e21cfacd95494ea3/crates/atomcode-review/src/assemble.rs), [coding mount](https://github.com/karlorz/atomcode/blob/152b2cc132dda9b177c3a030e21cfacd95494ea3/crates/atomcode-coding/src/parts.rs), [path guard](https://github.com/karlorz/atomcode/blob/152b2cc132dda9b177c3a030e21cfacd95494ea3/crates/atomcode-review/src/confine.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: available as a separately triggered tool; not necessarily executed on every coding turn. The source confirms independence of reviewer context/tool authority, not that every reviewer verdict is correct. Ordinary same-agent verification by `verify.rs` is expressly excluded as the positive audit witness.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party prospective external environment-intelligence loop culminating in adaptation of the organization's future capability was established.
- Disturbance / variety regulated: current requests, provider/tool outcomes and stored past session information are available, but no distinct outside-and-then intelligence function is shown.
- Decisive decision or feedback right: no future organizational capability adaptation owner proven.
- Decision owner: none established for S4.
- Supporting / enforcement mechanisms: persistent sessions, memory/context, web tools, code graphs, goal mode, skills, provider/model selection.
- Closure path: current task information may inform subsequent tasks, but an external future signal → adaptation option → model/parent-owned capability change → returned altered operation was not established.
- Boundary reachability: no positive S4 path claimed.
- Why this is / is not agent-owned: agentic browsing and persistent context can support immediate coding operations; their existence does not establish strategic external intelligence ownership.
- Evidence: [coding assembly](https://github.com/karlorz/atomcode/blob/152b2cc132dda9b177c3a030e21cfacd95494ea3/crates/atomcode-coding/src/parts.rs), [goal evaluator](https://github.com/karlorz/atomcode/blob/152b2cc132dda9b177c3a030e21cfacd95494ea3/crates/atomcode-core/src/agent/goal_evaluator.rs), [README feature boundary](https://github.com/karlorz/atomcode/blob/152b2cc132dda9b177c3a030e21cfacd95494ea3/README.md).
- Basis: structural.
- Confidence: medium.
- Caveats: possible user-defined future extensions not bundled/wired in the reviewed mode cannot be credited.

### Absence scope

- Surfaces inspected: operating tool registry, session/memory/skills providers, web/search capabilities, goal-mode continuation and source code review specialization.
- Plausible first-party paths checked: web research for tasks, project context persistence, model selection and long-running goals.
- Why no material first-party path remains: reviewed live paths inform or check present coding work rather than convert future environmental distinctions into changed organizational capability.

## S5 — Policy and identity

- State: —
- Function: no constitutional identity/purpose reconciliation loop with an ultimate first-party decision owner and authoritative return was established.
- Disturbance / variety regulated: tool risk, task objectives and provider configuration are enforcement and operational constraints, not a whole-system identity or ultimate purpose matter.
- Decisive decision or feedback right: none for organization-level ultimate policy/identity in the declared boundary.
- Decision owner: none established for S5; user authorization does not automatically create an S5 parent mode.
- Supporting / enforcement mechanisms: system prompt, tool permission policies, sensitive path checks, approval screens, provider settings, remote access/session controls.
- Closure path: a user may allow or deny an edit or switch a model, but there is no declared identity-policy matter → legitimate ultimate authority → binding returned policy/identity decision loop.
- Boundary reachability: no positive S5 path claimed.
- Why this is / is not agent-owned: removing the model leaves fixed permissions, not a model-owned ultimate organizational charter.
- Evidence: [coding assembly](https://github.com/karlorz/atomcode/blob/152b2cc132dda9b177c3a030e21cfacd95494ea3/crates/atomcode-coding/src/parts.rs), [README safety/modes](https://github.com/karlorz/atomcode/blob/152b2cc132dda9b177c3a030e21cfacd95494ea3/README.md).
- Basis: structural.
- Confidence: medium-high.
- Caveats: upstream human product/OSS governance is an adjacent actor unless a supported runtime loop binds it as an S5 parent decision right.

### Absence scope

- Surfaces inspected: coding instructions, approval middleware, runtime configuration, model/provider choice, goal mode, CLI remote/sessions, review permissions.
- Plausible first-party paths checked: owner/user permission changes, role switches, goal selection, static config and security protections.
- Why no material first-party path remains: all inspected paths regulate individual tasks/tools or set fixed constraints, not ultimate purpose/identity via authoritative returned S5 decisions.

## Recursion

One model-led AtomCode coding session and its bounded child coding/review paths form the assessed system. The review child supplies an S3* complementary channel at that local recursion, not an independent model-coordinated S2 worker. Separate sessions, users, external providers and OSS maintainers are not presumed a single AtomCode supervisory organization.

## Variety and escalation

Model/tool feedback and optional goal continuation absorb code/task variety. Permission exception decisions reach a human, but do not establish a constitutional purpose loop. Syntax/test verification is internal S1 support; the independent `code_review` child can return a distinct evidence-backed fault signal to the main coding agent. Background/parallel tasks have deterministic caps and statuses, without a separately established S2 inter-worker disturbance controller or S3 whole-current management function. No independent algedonic architecture is inferred from the existence of error reports.

## Evidence gaps

- Review is explicitly available by default in the shipped coding assembly but optional per request/agent tool call. There is no claim of unconditional review on every submission or a different model provider requirement.
- Per-file parallel subagent execution lacks a demonstrated first-party cross-worker conflict detection/coordination return path. If later evidence shows shipped integration arbitration at the frozen revision, reassess S2 under the same ref rather than inferring it from task count.
- Goal/background modes were not shown to own whole-current resource commitments across independently active operating units. Re-examine only with source-specific evidence, not status names.
- No live provider invocation was performed. This is a frozen primary-source organizational assessment, not an execution-quality benchmark, independent human review or validation of reviewer accuracy.

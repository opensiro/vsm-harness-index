---
harness_id: learn-claude-code-rs
project_name: learn-claude-code-rs
repository: https://github.com/wulawulu/learn-claude-code-rs
review_ref: 2981fc1b6ec3c45843d89412292b6b15505665e3
reviewed_at: 2026-10-26
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

# learn-claude-code-rs

## Review boundary

- System in focus: The first-party integrated `sfull` coding-agent runtime invoked by the repository's documented `cargo run -p sfull` route, including its synchronous fresh-context subagent tool.
- Purpose and identity: Carry out user-requested coding work through model-selected tools while demonstrating a modular Rust agent harness.
- Relevant environment: Project filesystem and shell, provider responses, tool errors, user permissions, context size, persistent task/memory data and optional MCP servers.
- Standard-distribution boundary: `sfull` binary/library, built-in tools and managers, dynamic/static prompt construction, provider SDK transport and configured MCP clients at the frozen revision. Educational purpose does not prevent an actual runnable loop from qualifying.
- Credited operating / distribution surfaces: [documented integrated mode and limits](https://github.com/wulawulu/learn-claude-code-rs/blob/2981fc1b6ec3c45843d89412292b6b15505665e3/sfull/sfull.en.md), [binary startup](https://github.com/wulawulu/learn-claude-code-rs/blob/2981fc1b6ec3c45843d89412292b6b15505665e3/sfull/src/main.rs), [Agent loop](https://github.com/wulawulu/learn-claude-code-rs/blob/2981fc1b6ec3c45843d89412292b6b15505665e3/sfull/src/lib.rs), [registered tools](https://github.com/wulawulu/learn-claude-code-rs/blob/2981fc1b6ec3c45843d89412292b6b15505665e3/sfull/src/tool/mod.rs).
- Adjacent first-party surfaces excluded from ownership: Independently runnable tutorial chapters `s01`–`s21`, the agent-builder teaching skill, repository maintenance/CI and tests. In particular, `s17` worker loops and `s21` evaluator are not wired into `sfull` merely because they share a Cargo workspace; no ownership is borrowed from them. This assessment does not claim to grade every alternate chapter mode.
- First-party operating / deployment modes considered: Integrated interactive runtime in Default or Auto permission mode; Plan mode is read-only. Built-in `task` subagents share domain context/filesystem but have their own fresh model conversation and small toolset. Team record/message tools and worktree tools are considered exactly as implemented, not as a hypothetical complete worker fleet.
- Recursion level: One integrated coding session and subordinate task calls; not the tutorial's development organization or all chapters combined.
- Reviewed revision: `2981fc1b6ec3c45843d89412292b6b15505665e3`.
- Observation date: 2026-10-26.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The repository is a progressive tutorial with independent Cargo crates and one documented integrated runtime. `sfull/main.rs` creates a configured Anthropic-compatible client, permission manager, skill registry, `.claude` stores, domain managers, optional MCP router and an `Agent`. A user query enters context and calls `agent_loop`.

The first-party loop sends history plus native/MCP tool schemas to the provider, handles transport/context/truncation recovery, executes model-returned tool calls, appends their actual results and continues until a non-tool response. Shell/read/write/edit tools act on the project. Runtime permission checks and hooks precede/observe actions; model-assisted context compaction and durable memory support continued work. The SDK transports model inference; it is not an external prebuilt coding-agent loop.

The `task` tool creates another first-party Agent with fresh conversation, a coding-subagent prompt and bash/read/write/edit tools, awaits its loop, then returns a summary. In contrast, `spawn_teammate` writes a named idle teammate record; send/broadcast/plan_approval/shutdown functions append inbox records. These team tools do not start an autonomous teammate worker or consume a plan/shutdown decision. Worktree tools create/list/status/run named Git worktrees, without merge/rebase integration. Cron tools create/delete/list stored schedule records; the integrated source does not supply a due-task execution loop. These limits are material to the mapping, rather than merely missing marketing documentation.

## Operational model

The root and an explicitly invoked coding subagent can choose real project observations/actions from tool feedback. Their output is source changes, investigation or verification, not just task metadata. Stored teammate names, dependency fields and schedules are supporting domain data; they are not independently executing S1s by themselves. The user sets goals/permissions; the model owns ordinary task action selection. No positive parent mode is inferred from Default/Auto/Plan labels.

## S1 — Operations

- State: A
- Function: Perform coding/investigation outcomes through a continuing observation–decision–tool-action loop.
- Disturbance / variety regulated: Unknown files, implementation alternatives, tool failures, denied actions and incomplete context.
- Decisive decision or feedback right: Select read/edit/shell/delegation actions, interpret their actual result, revise subsequent work and decide when to return.
- Decision owner: Model-backed first-party Agent; subagents own their assigned local coding decisions.
- Supporting / enforcement mechanisms: Provider SDK, tool router/context, permission manager, hooks, persistence, compaction and retry logic.
- Closure path: User query → Agent request with tools → model-selected action → native/MCP execution → tool_result appended to history → next model decision; task calls return their actual child result to the root.
- Boundary reachability: The documented sfull command constructs these tools and calls agent_loop directly. `task` constructs another Agent and awaits that same loop, rather than invoking a separate external coding CLI.
- Why this is / is not agent-owned: The Rust router can enforce or execute actions, but removing model decisions leaves no substantive coding/action choice. User permissions bound the operation rather than select each ordinary step.
- Evidence: [startup](https://github.com/wulawulu/learn-claude-code-rs/blob/2981fc1b6ec3c45843d89412292b6b15505665e3/sfull/src/main.rs#L26), [request/action/result continuation](https://github.com/wulawulu/learn-claude-code-rs/blob/2981fc1b6ec3c45843d89412292b6b15505665e3/sfull/src/lib.rs#L115), [first-party subagent](https://github.com/wulawulu/learn-claude-code-rs/blob/2981fc1b6ec3c45843d89412292b6b15505665e3/sfull/src/tool/subagent.rs).
- Basis: structural.
- Confidence: High for source wiring; live effectiveness unmeasured.
- Caveats: Requires a compatible configured provider and working tool permissions; source inspection does not establish performance.

## S2 — Coordination

- State: —
- Function: No material inter-S1 conflict-attenuation and returned adjustment loop in the integrated mode.
- Disturbance / variety regulated: Candidate paths are conflicting task ownership, shared files and dependency ordering.
- Decisive decision or feedback right: Task owner/dependency fields and isolated worktrees do not supply a conflict-specific resolution protocol.
- Decision owner: Root chooses task actions; predefined managers update records and enforce local data consistency.
- Supporting / enforcement mechanisms: Shared mutexes, blocked_by/blocks metadata, teammate inboxes and named worktree isolation.
- Closure path: Synchronous child summaries return, but teammate inbox creation does not feed an executing teammate; worktree results are not reconciled into an inter-worker settlement.
- Why this is / is not agent-owned: Generic delegation/storage and a theoretical user-written coordination protocol do not meet the S2-specific constructor test.
- Evidence: [task metadata/updates](https://github.com/wulawulu/learn-claude-code-rs/blob/2981fc1b6ec3c45843d89412292b6b15505665e3/sfull/src/task.rs), [team record-only implementation](https://github.com/wulawulu/learn-claude-code-rs/blob/2981fc1b6ec3c45843d89412292b6b15505665e3/sfull/src/team.rs#L54), [worktree operations](https://github.com/wulawulu/learn-claude-code-rs/blob/2981fc1b6ec3c45843d89412292b6b15505665e3/sfull/src/worktree.rs).
- Basis: structural.
- Confidence: High within sfull.
- Caveats: Other independently runnable chapters are distinct boundaries; no broader claim about them is made.

### Absence scope

- Surfaces inspected: sfull startup/loop, task manager/tool, teammate manager/protocol tools, synchronous child implementation and worktree manager.
- Plausible first-party paths checked: Duplicate ownership/dependency adjustment, team messages and plan approval, child coordination and isolated worktree return.
- Why no material first-party path remains: Team tools persist records without a worker consumer, task metadata does not resolve a specified inter-S1 interference, and worktree tools do not merge/reconcile. The integrated distribution supplies no differentiated conflict-specific behavioral feedback loop.

## S3 — Inside-and-now control

- State: —
- Function: No whole-current organizational regulation established beyond local coding-task planning/delegation.
- Disturbance / variety regulated: Candidate paths are present task commitments, team plans and shutdown/resource control.
- Decisive decision or feedback right: The root can edit task state and call a coding child; plan_approval/shutdown tools only store a typed message, without a governing control consumer.
- Decision owner: Model for current task operation; user/developer for permission/recovery settings. No distinct S3 or parent S3 loop established.
- Supporting / enforcement mechanisms: Task lists, team status records, protocol inboxes, context limits, retries and permission checks.
- Closure path: Tool results inform current coding work; no first-party whole-current allocation/accountability or intervention decision returns into a governed worker fleet.
- Why this is / is not agent-owned: The names manager, team, plan and shutdown do not turn a local tool loop or record API into whole-system present-control ownership.
- Evidence: [protocol message functions](https://github.com/wulawulu/learn-claude-code-rs/blob/2981fc1b6ec3c45843d89412292b6b15505665e3/sfull/src/tool/team.rs#L74), [record persistence](https://github.com/wulawulu/learn-claude-code-rs/blob/2981fc1b6ec3c45843d89412292b6b15505665e3/sfull/src/team.rs#L114), [operational prompt](https://github.com/wulawulu/learn-claude-code-rs/blob/2981fc1b6ec3c45843d89412292b6b15505665e3/sfull/src/lib.rs#L450).
- Basis: structural.
- Confidence: High within the integrated mode.
- Caveats: A developer could compose a manager; a generic toolset is not a supplied S3-specific constructor.

### Absence scope

- Surfaces inspected: Agent/root prompt, team/task managers and protocol consumers, tool registration and documented integrated limits.
- Plausible first-party paths checked: Global task list, plan approval, shutdown request/response, child return and permission escalation.
- Why no material first-party path remains: The review finds local task decisions and record/message APIs, without an established whole-current regulatory scope and operative decision/return path. Generic user approval is not a function-specific parent mode.

## S3* — Complementary audit

- State: —
- Function: No differentiated independent complementary operational audit arrangement in sfull.
- Disturbance / variety regulated: Incorrect output can be checked by the producing coding agent or a generically delegated coding child.
- Decisive decision or feedback right: No supplied claim-relative audit role/independence contract or corrective-control return is assigned.
- Decision owner: Producing agent and user in ordinary task completion; developer for arbitrary hook composition.
- Supporting / enforcement mechanisms: File/shell inspection, hook callbacks, tool-result history and generic child context separation.
- Closure path: Tool errors/hooks feed normal production; a user-defined audit is additional composition, not the shipped path.
- Why this is / is not agent-owned: Fresh context alone does not supply audit independence. The registered child is a coding agent with write tools, and the standalone s21 evaluator is not integrated here.
- Evidence: [coding child role/toolset](https://github.com/wulawulu/learn-claude-code-rs/blob/2981fc1b6ec3c45843d89412292b6b15505665e3/sfull/src/tool/subagent.rs), [generic hook interface](https://github.com/wulawulu/learn-claude-code-rs/blob/2981fc1b6ec3c45843d89412292b6b15505665e3/sfull/src/hook.rs), [integration and chapter boundaries](https://github.com/wulawulu/learn-claude-code-rs/blob/2981fc1b6ec3c45843d89412292b6b15505665e3/README.md).
- Basis: structural.
- Confidence: High for the bounded integration claim.
- Caveats: No claim that tests or an externally composed reviewer lack practical value.

### Absence scope

- Surfaces inspected: Native/subagent toolsets, child prompt, hook registration and execution, integrated documentation and Cargo membership.
- Plausible first-party paths checked: Coding child as auditor, pre/post hooks, shell checks, stored transcripts and separate evaluator chapter.
- Why no material first-party path remains: The integrated hooks/child expose generic production/extensibility, without a differentiated independent audit judgment and corrective control; adjacent evaluation code is not wired into the assessed mode.

## S4 — Outside-and-then intelligence

- State: —
- Function: No established externally prospective capability-adaptation loop in the integrated coding session.
- Disturbance / variety regulated: Context growth, user corrections, remembered project facts and stored future task descriptions.
- Decisive decision or feedback right: The agent chooses task actions and memories; no actor owns prospective environmental options and a return to present capability.
- Decision owner: Coding agent for local memory/task work; user for purpose/model settings.
- Supporting / enforcement mechanisms: Memory types, prompt loading, skills, context compaction and cron record CRUD.
- Closure path: Memory is re-presented to future prompts and schedules are stored. Neither establishes a prospective adaptation/current-control conversation.
- Why this is / is not agent-owned: Local learning/continuity is not S4, and a persisted cron string does not establish an autonomous strategic worker.
- Evidence: [memory guidance](https://github.com/wulawulu/learn-claude-code-rs/blob/2981fc1b6ec3c45843d89412292b6b15505665e3/sfull/src/memory.rs#L11), [cron storage only](https://github.com/wulawulu/learn-claude-code-rs/blob/2981fc1b6ec3c45843d89412292b6b15505665e3/sfull/src/cron.rs), [prompt/compaction](https://github.com/wulawulu/learn-claude-code-rs/blob/2981fc1b6ec3c45843d89412292b6b15505665e3/sfull/src/lib.rs).
- Basis: structural.
- Confidence: High within sfull.
- Caveats: A coding task may investigate the future; that task content alone does not establish the organizational function.

### Absence scope

- Surfaces inspected: Memory and skills, dynamic prompt, compaction, cron manager and tool registration, documented startup flow.
- Plausible first-party paths checked: User feedback memory, reference discovery, cron-triggered future work and skill-driven capability change.
- Why no material first-party path remains: These preserve/augment current task context or store schedules, without a supplied external/future distinction → adaptation-option owner → changed current-capability loop or complete parent adaptation mode.

## S5 — Policy and identity

- State: —
- Function: No runtime identity/ultimate-policy arbitration and governing return.
- Disturbance / variety regulated: Tool risk, user denials and static coding constraints.
- Decisive decision or feedback right: Human chooses permission mode/action approvals; prompt/configuration supplies operational constraints.
- Decision owner: User/developer for execution policy; not an established S5 owner at the session recursion.
- Supporting / enforcement mechanisms: Default/Plan/Auto modes, Allow/Deny/Ask, prompt constraints, hooks and CLAUDE.md loading.
- Closure path: Approval allows a tool; denial returns to the coding agent. No identity-level matter and returned governing settlement is supplied.
- Why this is / is not agent-owned: Permission and plan-approval labels do not create ultimate-policy closure; plan_approval itself merely appends a message.
- Evidence: [permission mode and check/ask](https://github.com/wulawulu/learn-claude-code-rs/blob/2981fc1b6ec3c45843d89412292b6b15505665e3/sfull/src/permission.rs), [tool approval return](https://github.com/wulawulu/learn-claude-code-rs/blob/2981fc1b6ec3c45843d89412292b6b15505665e3/sfull/src/lib.rs#L207), [static/dynamic prompt](https://github.com/wulawulu/learn-claude-code-rs/blob/2981fc1b6ec3c45843d89412292b6b15505665e3/sfull/src/prompt.rs).
- Basis: structural.
- Confidence: High for the function distinction.
- Caveats: A real user's higher-level organization may have S5 outside this runtime.

### Absence scope

- Surfaces inspected: Permission manager/modes, user approval return, prompt builder/template, loaded project instructions and team protocol functions.
- Plausible first-party paths checked: Plan mode, repeated denials, user approval, static policy/CLAUDE.md and plan_approval messages.
- Why no material first-party path remains: Every supplied decision concerns task execution, stored instruction or protocol data; there is no identity/ultimate-policy referral, legitimate deciding authority and governing return at the declared recursion.

## Distributed OSS parent arrangement

Tutorial maintainers and user-authored project instructions are not a demonstrated organization-level parent loop for this coding runtime. No parent states are inferred from contributor governance.

## Self-hosted and non-human modes

The operator configures an Anthropic-compatible endpoint and permission mode. Default/Auto can support local autonomous coding; Plan is read-only. No alternate autonomous metasystem or function-specific parent mode is established by endpoint choice or unattended tool permission.

## Recursion

The first-party `task` child has meaningful coding discretion and a result channel, but no separate metasystem is shown. A Cargo chapter sequence, task dependency graph or teammate name list is not VSM recursion.

## Variety and escalation

Model-selected actions absorb local source variety; permission denials, transport backoff, compaction and tool errors delimit continuation. Generic stored plan/shutdown messages have no integrated autonomous consumer. Background shell completion is operational feedback, not a separate organizational controller.

## Evidence gaps

Static pinned-source assessment; no live LLM/provider/agent-quality run. Cargo/Rust is unavailable in this environment, so upstream compilation/tests were not executed. The sfull team/cron/worktree limits are source-backed boundaries rather than claimed successful operations. Alternate chapter deployments are explicitly outside this mode-specific assessment and must be separately reconstructed before their capabilities can change its conclusions. Pinned Methodology and Index validators check structure/provenance, not effectiveness.

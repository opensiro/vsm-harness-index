---
harness_id: llm
project_name: llm
repository: https://github.com/imjiaoyuan/llm
review_ref: fa532244bc543a02850151a692feca74b15f713c
reviewed_at: 2026-10-05
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-05
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# llm

## Review boundary

- System in focus: the first-party `imjiaoyuan/llm` terminal coding-agent runtime at frozen revision `fa532244bc543a02850151a692feca74b15f713c`, including its model/tool loop, built-in coding tools, approvals/blacklist enforcement, interactive and JSON entry surfaces, persisted sessions, compaction/recovery, skill/package/extension discovery and project prompt context.
- Purpose and identity: execute coding tasks in a terminal by letting a model inspect, edit and run a project through first-party tools, with resumable conversation state and optional user-installed extensions/skills.
- Relevant environment: user requests and steering, repository/filesystem state, shell/build/test results, model/provider responses, approvals/blacklist policy, project instructions, installed skills/extensions/packages and persisted session history.
- Standard-distribution boundary: the Rust runtime under `src/agent`, built-in tools, CLI/session surfaces and first-party discovery/install mechanisms are inside. External model providers, user/community packages, MCP servers and a supervising editor/CI/agent using `--json` are dependencies/parents and cannot donate VSM functions. Files under `examples/` are reference implementations and do not become active runtime paths unless separately installed/configured.
- Credited operating / distribution surfaces: ordinary interactive and one-shot coding runs, `--json` form of the same run, built-in tools, approvals, session persistence/resume/fork/export, compaction/recovery, project-context loading, skills/packages/extensions mounted through supported discovery.
- Adjacent first-party surfaces excluded from ownership: repository-development CI/tests, installer/update mechanism, example subagent/reviewer extensions and example agent definitions unless explicitly mounted, and any external supervisor driving JSON output.
- First-party operating / deployment modes considered: interactive terminal session, one-shot task, JSON event mode, resumed/forked sessions and the same runtime with user/project skills or extensions loaded.
- Recursion level: one active model/tool coding run is the focal S1 unit. Built-in tools, plan state, extensions, prompt templates and persisted messages are subordinate mechanisms; optional example child agents are not part of the default first-party operating path.
- Reviewed revision: `fa532244bc543a02850151a692feca74b15f713c`.
- Observation date: 2026-10-05.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

The frozen runtime implements a direct model/tool coding loop. The model receives the system/project/skill prompt plus session history, chooses built-in tools such as read/write/edit/bash/search/webfetch/update_plan, receives concrete tool results and continues until it stops calling tools or the run is interrupted/bounded. Mid-run user steering is injected at tool-round boundaries.

Sessions persist each completed round so crash recovery loses only the in-flight round. Resume/fork/export, context compaction, oversized-result pruning and stream recovery preserve the same operational conversation. Approvals and hard/blacklist command refusal constrain individual tool calls.

Skills and packages are discovered from first-party user/project paths and can be selected into prompts. Extensions can add tools/commands/hooks, but their behavior is supplied by user-installed code. The repository ships example subagent and reviewer definitions, including a parallel/chain child-agent extension, yet those examples are not mounted by the standard runtime automatically and therefore do not establish higher-system ownership for the assessed distribution.

## Operational model

A user task enters `run_agent`. On each round the model sees the current prompt/history and available tools, chooses actions, receives tool results/errors, and can revise subsequent work. The same conversation can persist across tasks or resume from disk. Approval callbacks can allow, allow-for-session or deny gated operations, while hard refusals and blacklist rules enforce safety boundaries.

## S1 — Operations

- State: A
- Function: autonomously perform coding work by selecting and revising repository inspection, edits, writes, command execution and search actions from current evidence.
- Disturbance / variety regulated: unfamiliar codebases, incomplete task requirements, changing file state, command/build/test failures, provider/context errors, oversized results, interrupted streams and user steering.
- Decisive decision or feedback right: choose the next coding/tool action, interpret returned evidence and errors, revise the plan/action sequence, and stop when the model judges the task complete.
- Decision owner: the active model-backed `llm` coding agent.
- Supporting / enforcement mechanisms: `run_agent`, built-in tool registry, `update_plan`, session persistence, compaction/recovery, steering queue, approvals/blacklist, project prompt context and skill discovery.
- Closure path: user/project/session context → model chooses tool/action → tool/runtime returns result/error → evidence enters later model round → subsequent coding behaviour changes until completion, interruption or bounded failure.
- Boundary reachability: ordinary `llm "task"` and interactive `llm` directly instantiate this first-party model/tool loop without requiring an example extension or external orchestrator.
- Why this is / is not agent-owned: removing the model leaves tools, persistence, approvals and rendering but removes the open-ended choice that converts repository evidence into coding actions.
- Evidence: README; `src/agent/mod.rs`; `src/agent/repl.rs`; `src/agent/session.rs`; `src/agent/tools/`; `src/agent/system_prompt.rs`.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: provider inference is external, but the product concretely owns the coding-loop composition and tool feedback path.

## S2 — Coordination

- State: —
- Function: no distinct inter-S1 coordination function is established in the standard runtime.
- Disturbance / variety regulated: one focal coding run may invoke several tools, load extensions or be driven by an external supervisor, but the default product does not expose distinct peer S1 units with a specific mutual interference relation.
- Decisive decision or feedback right: no S2-specific decision over conflict, oscillation or mutual adjustment among distinct S1 units was found.
- Decision owner: not established at S2 level.
- Supporting / enforcement mechanisms: sequential tool rounds, approval gating, steering queue, session state and optional extension loading.
- Closure path: these mechanisms serialize or constrain one run; no coordination result is fed back into distinct peer operational units.
- Why this is / is not agent-owned: sequencing and one-agent planning are S1 mechanisms, not S2.
- Evidence: `src/agent/mod.rs`; `src/agent/session.rs`; `src/agent/ext/`; README.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: `examples/extensions/subagent.py` can construct child-agent batches/chains after installation, but that optional example is not an automatically active standard path and, by itself, parallel delegation still would not prove an inter-S1 attenuation witness.

### Absence scope

- Surfaces inspected: core agent loop, built-in tools, session runtime, extension host, JSON mode, approvals, skills/packages and shipped subagent example.
- Plausible first-party paths checked: tool parallelism as peer operations; steering as coordination; JSON supervisor as S2; optional child agents as S2; session forks as peer S1 units.
- Why no material first-party path remains: standard operation has one coding decision actor, external supervisors are outside the boundary, and optional examples do not supply a first-party always-available coordination closure among distinct S1 units.

## S3 — Inside-and-now control

- State: —
- Function: no distinct whole-system current-control function is established beyond local control of one coding run/session.
- Disturbance / variety regulated: approvals, interruption, compaction thresholds, session state, tool restrictions and model selection constrain the current run.
- Decisive decision or feedback right: no separate owner has a whole-system current view plus authority over a portfolio of shared operations, priorities, resources or commitments.
- Decision owner: not established at S3 level.
- Supporting / enforcement mechanisms: session status, interrupt/steering, approvals, tool allowlists, compaction/recovery, model selection and persisted thread state.
- Closure path: these controls alter the same focal coding loop and its local session, not a metasystemic current-management loop.
- Why this is / is not agent-owned: the coding model manages its own task as S1 while users/runtime enforce local controls; neither constitutes distinct whole-system S3.
- Evidence: README; `src/agent/mod.rs`; `src/agent/repl.rs`; `src/agent/session.rs`; `src/agent/approval.rs`.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: `--json` is explicitly usable by an editor, CI lane or another agent, but that supervising process is external and cannot donate S3 to this harness.

### Absence scope

- Surfaces inspected: interactive/JSON entry modes, session lists/resume/fork, approvals, plan tool, compaction/recovery, provider/model controls, extension events and external-supervisor documentation.
- Plausible first-party paths checked: `update_plan` as S3; session browser as whole-system view; JSON event stream as supervisory control; approval callbacks as S3 parent authority; model switching as resource control.
- Why no material first-party path remains: each first-party mechanism is scoped to one run/conversation or exposes data to an external parent; no separate internal whole-current decision owner closes the required S3 path.

## S3* — Complementary audit

- State: —
- Function: no sufficiently independent complementary audit path is established in the standard runtime.
- Disturbance / variety regulated: bash/tests, tool errors, user steering and optional hooks can reveal defects during coding, but they are ordinary producer feedback.
- Decisive decision or feedback right: no separate first-party reviewer in the default runtime owns an independent claim-checking judgment and returns findings through a distinct current-control path.
- Decision owner: not established at S3* level.
- Supporting / enforcement mechanisms: shell/test execution, tool results, extension hooks and optional reviewer example.
- Closure path: default verification evidence returns directly to the same coding actor or user; no separate complementary audit loop is automatically instantiated.
- Why this is / is not agent-owned: self-testing inside the coding loop is not sufficiently independent; the shipped reviewer definition is an example requiring separate composition.
- Evidence: README; `src/agent/tools/bash.rs`; `src/agent/ext/`; `examples/agents/reviewer.md`; `examples/extensions/subagent.py`.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: a user can install the first-party example subagent extension and explicitly run the read-only reviewer, but the frozen standard distribution does not wire that reviewer into an ordinary producer→audit→control closure.

### Absence scope

- Surfaces inspected: built-in bash/tool feedback, extensions/hooks, JSON output, example reviewer definition, example subagent chain/batch support and repository tests.
- Plausible first-party paths checked: running tests as S3*; hooks as auditor; reviewer example as complementary audit; external CI supervisor as S3*.
- Why no material first-party path remains: core checks are in-band, example reviewer composition is optional/unmounted, and external CI/supervisors lie outside the harness boundary.

## S4 — Outside-and-then intelligence

- State: —
- Function: no distinct outside-and-then adaptation loop is established.
- Disturbance / variety regulated: project instructions, skills, packages, extensions, model/provider settings and persisted session context can change what future runs know or can do.
- Decisive decision or feedback right: no first-party process senses external/future change, develops adaptation options for the harness and autonomously returns a selected capability change into later operation.
- Decision owner: not established at S4 level.
- Supporting / enforcement mechanisms: AGENTS/CLAUDE project context, skill discovery, package install/refresh, extension loading, session persistence and configurable providers/models.
- Closure path: operator-authored or installed capabilities are loaded into later prompts/tools; the runtime does not itself close a prospective environmental adaptation cycle.
- Why this is / is not agent-owned: the system prompt documents how an agent could write an extension or skill, but that is ordinary current-task extensibility, not a distinct process that senses future environmental change and chooses an adaptation option.
- Evidence: README; `src/agent/skills.rs`; `src/agent/system_prompt.rs`; `src/agent/ext/`; package/install paths.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: user/project packages can materially expand future capability, but installation/configuration alone is not S4.

### Absence scope

- Surfaces inspected: project-context discovery, skills, package install/refresh, extension discovery/reload, session persistence, model/provider settings and self-extension guidance in the system prompt.
- Plausible first-party paths checked: persisted sessions as learning; skills as S4; package refresh as adaptation; model-authored extension/skill creation as self-improvement; provider switching as environmental adaptation.
- Why no material first-party path remains: these surfaces retain or install capabilities but do not implement a separate external/prospective distinction → option generation → selected adaptation → return-to-current-capability loop.

## S5 — Policy and identity

- State: —
- Function: no identity- or ultimate-policy-level closure is established.
- Disturbance / variety regulated: hard command refusals, blacklist rules, per-tool allow/deny/prompt settings, approval responses and system/project prompt hierarchy constrain ordinary operation.
- Decisive decision or feedback right: no identity/ultimate-policy issue is routed to a legitimate ultimate authority and returned as a durable governing system decision.
- Decision owner: not established at S5 level.
- Supporting / enforcement mechanisms: hardcoded refusal set, user/project blacklist, tool approval config, system prompt/project instructions and model/provider settings.
- Closure path: safety/configuration decisions constrain current tool execution or future local configuration but do not close an identity-level policy matter for the viable system.
- Why this is / is not agent-owned: static/reflexive safety constraints and user approvals are operational policy enforcement, not S5.
- Evidence: README; `src/agent/approval.rs`; `src/agent/blacklist.rs`; `src/agent/settings.rs`; `src/agent/system_prompt.rs`.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: users and maintainers retain real authority over installed packages/configuration, but adjacent operator/development governance is not first-party S5 closure.

### Absence scope

- Surfaces inspected: hard refusals, blacklist, approval modes, tool settings, system/project prompt hierarchy, package trust guidance, model/provider configuration and repository governance.
- Plausible first-party paths checked: immutable refusal rules as S5; blacklist as policy; approval prompts as S5; project AGENTS instructions as constitution; maintainer/user authority as ultimate policy.
- Why no material first-party path remains: inspected mechanisms regulate ordinary execution or external configuration and do not implement identity/ultimate-policy issue → legitimate authority → authoritative decision → return-to-operation closure.

## Recursion

The default runtime exposes one coding-agent operation. Session forks remain conversations, tools/extensions are subordinate capabilities, and the shipped subagent/reviewer examples require separate installation/composition before they can create additional operational units.

## Variety and escalation

The agent absorbs coding variety through iterative tools, planning, project instructions, skills, compaction and stream recovery. Hard or blacklisted commands can be refused or escalated to a user approval callback; interruptions and steering change the same S1 loop rather than establishing a separate metasystem.

## Evidence gaps

No `?` state is required. The frozen runtime and documentation expose the core loop, session/approval/extension/skill boundaries and example-only multi-agent surfaces sufficiently to establish S1 and support negative S2/S3/S3*/S4/S5 conclusions.

## Assessment summary

llm closes autonomous S1 through its first-party model/tool coding loop with persisted sessions and direct coding tools. Standard-distribution coordination, whole-current control, complementary audit, prospective adaptation and identity-policy closure are not established; optional examples and external supervisors are excluded from donating those functions.

**Vector:** A · — · — · — · — · —

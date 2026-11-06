---
harness_id: picocode
project_name: PicoCode
repository: https://github.com/shijizhi/picocode
review_ref: c016d4ff9a84c6584f4c09706b05a364b2a5b5dd
reviewed_at: 2026-11-07
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

# PicoCode

## Review boundary

- System in focus: the first-party Rust terminal coding-agent workbench, its shipped `AgentCore`, OpenAI-compatible model adapter, `ToolRuntime` and workspace edit/command effects, event/session store and user-facing TUI.
- Purpose and identity: answer a user's programming requests by exploring project files, applying source edits and executing commands with model-selected successive actions.
- Relevant environment: code workspace, search/read findings, command failures and tests, editing conflicts, human command policy, model service availability, user task changes and finite context.
- Standard-distribution boundary: `src/main.rs` → `src/lib.rs` → `src/terminal.rs` instantiates `AgentCore` from `src/agent_core.rs`, `src/ai/*`, `src/tool.rs` and `src/workspace.rs`. This is a standalone Rust binary; underlying hosted OpenAI-compatible model service supplies inference rather than a borrowed agent harness.
- Credited operating / distribution surfaces: `src/agent_core.rs`, `src/terminal.rs`, `src/ai/{mod,openai}.rs`, `src/tool.rs`, `src/workspace.rs`, `src/{event,session,instruction,app}.rs`.
- Adjacent first-party surfaces excluded from ownership: design roadmap and aspirational architecture under `design/`, session export/share, interactive TUI diff/confirmation views, manually forked session tree, provider/model picker and install/release scripts. They are support or human operations, not autonomous meta-management.
- First-party modes considered: native model/tool loop, workspace read/search/edit, preview/apply/rewind with checkpoints, command run and repair loop, user sessions/fork/compact, skill/capability discovery and project configuration.
- Recursion level: one live model-governed coding turn / workspace goal; multiple saved or forked histories are not demonstrated to be coordinated autonomous operating units.
- Reviewed source: `shijizhi/picocode@c016d4ff9a84c6584f4c09706b05a364b2a5b5dd` (stable GitHub repository ID `1239352257`); Profile 0.2.4 and Methodology 0.3.7.

## Repository architecture

The shipped terminal path in `src/terminal.rs` builds an `AgentCore`, which calls the configured model through `AiClient`, parses first-party native or text tool calls, dispatches one operation to `ToolRuntime`, captures the real `ToolResult` and inserts it into subsequent model context. Tool implementations read/search the workspace, preview and apply single or batch file edits, record reversible checkpoints and execute commands. On failed `run_command`, the core adds a repair instruction to the **same** acting model and asks it to investigate, edit and rerun. Each turn is bounded by model/tool limits.

The terminal's `thread::spawn` is asynchronous UI execution of one submitted agent turn, not creation of a separate child agent with its own role/decision right. The session tree forks historical event streams on user request; its branches are not a managed multi-agent collaboration system. Atomic batch edits, per-file base hashes and conflict detection protect the integrity of a **single** operation, not a negotiated coordination protocol among distinct S1 writers.

Frozen source anchors:

- [Product scope and session capabilities](https://github.com/shijizhi/picocode/blob/c016d4ff9a84c6584f4c09706b05a364b2a5b5dd/README.md)
- [AgentCore model/tool/retry loop](https://github.com/shijizhi/picocode/blob/c016d4ff9a84c6584f4c09706b05a364b2a5b5dd/src/agent_core.rs)
- [Terminal wiring to native AgentCore](https://github.com/shijizhi/picocode/blob/c016d4ff9a84c6584f4c09706b05a364b2a5b5dd/src/terminal.rs)
- [Provider adapter](https://github.com/shijizhi/picocode/blob/c016d4ff9a84c6584f4c09706b05a364b2a5b5dd/src/ai/openai.rs) and [AI client](https://github.com/shijizhi/picocode/blob/c016d4ff9a84c6584f4c09706b05a364b2a5b5dd/src/ai/mod.rs)
- [Tool registration, execution and command policy](https://github.com/shijizhi/picocode/blob/c016d4ff9a84c6584f4c09706b05a364b2a5b5dd/src/tool.rs)
- [Workspace editing, hashes and batch rollback](https://github.com/shijizhi/picocode/blob/c016d4ff9a84c6584f4c09706b05a364b2a5b5dd/src/workspace.rs)
- [Session persistence, fork](https://github.com/shijizhi/picocode/blob/c016d4ff9a84c6584f4c09706b05a364b2a5b5dd/src/session.rs), [TUI state](https://github.com/shijizhi/picocode/blob/c016d4ff9a84c6584f4c09706b05a364b2a5b5dd/src/app.rs), [instruction/config](https://github.com/shijizhi/picocode/blob/c016d4ff9a84c6584f4c09706b05a364b2a5b5dd/src/instruction.rs)

## Operational model

The user supplies a project and objective; the configured LLM selects its successive native search/read/edit/command tools, receives observations and either repairs a problem or responds. Deterministic workspace and command safeguards can veto effects and return errors; UI state and session events persist, but no first-party autonomous manager, strategy actor or reviewer is constructed around the operative model.

## S1 — Operations

- State: A
- Function: direct coding investigation, workspace editing and command/test effects in pursuit of a user-specified programming goal.
- Disturbance / variety regulated: repository uncertainty, missing symbols/files, build/test failure, changed file contents, insufficient context, provider errors and operator effects policy.
- Decisive decision or feedback right: the model selects which real tool and parameters to use next; after results, it can choose to modify files, retry a command, investigate or finalize.
- Decision owner: the first-party `AgentCore` model/tool loop, with semantic action selection delegated to the configured LLM.
- Supporting / enforcement mechanisms: `AiClient`, `TOOL_PROTOCOL`, native tool schema, `ToolRuntime`, `Workspace`, reversible editing, hashed previews, `run_command`, event context and limits.
- Closure path: user request → LLM tool choice → workspace tool effect/denial → observed result/event → model's next choice or final response; failed command triggers an explicit same-model repair context.
- Boundary reachability: `terminal::process_submission` constructs `AgentCore` in the shipped binary; `run_prompt_turn` repeatedly invokes `ai.complete` and `tools.execute`.
- Why this is / is not agent-owned: without model-directed action selection, the remaining terminal and deterministic tools cannot autonomously decide how to carry out the coding task.
- Evidence: [wired terminal](https://github.com/shijizhi/picocode/blob/c016d4ff9a84c6584f4c09706b05a364b2a5b5dd/src/terminal.rs), [core](https://github.com/shijizhi/picocode/blob/c016d4ff9a84c6584f4c09706b05a364b2a5b5dd/src/agent_core.rs), [tools](https://github.com/shijizhi/picocode/blob/c016d4ff9a84c6584f4c09706b05a364b2a5b5dd/src/tool.rs).
- Basis: explicit + structural, corroborated by first-party fake-provider loop tests.
- Confidence: high.
- Caveats: fake-provider unit tests verify control flow, not actual inference-backed task success; Rust toolchain unavailable for execution here.

## S2 — Coordination

- State: —
- Function: no independent first-party coordination of interfering operational S1 units is evidenced.
- Disturbance / variety regulated: edit checkpoint mismatch, duplicate target in one batch and overlapping human task contexts are local integrity hazards, not demonstrated competition among separately deciding S1 workers.
- Distinct S1 units: one `AgentCore` works per model turn. Session forks are user-selected saved histories, not a wired collaborating cohort.
- Inter-S1 disturbance: no shared multi-agent workspace commitment or first-party concurrent autonomous writer collision is specified.
- Attenuating coordination relation: `expected_hash` and atomic batch rollback guard individual file writes; they do not allocate or reconcile independently owned work from multiple S1 agents.
- Feedback into subsequent S1 behaviour: the same agent sees its own tool errors, not a coordination verdict balancing different S1 actors.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: `thread::spawn` keeps the UI responsive and edit hashes detect stale reads; neither establishes separate competing decision owners or returned inter-unit arbitration.
- Decisive decision or feedback right: no independent first-party cross-S1 interference decision.
- Decision owner: none evidenced; hardcoded workspace checks and operator session navigation are S1 support.
- Supporting / enforcement mechanisms: base hashes, checkpoint journal, batch rollback, manual session forks.
- Closure path: local edit clash → one tool error → same agent's next operation, not an inter-agent settlement.
- Why this is / is not agent-owned: no multi-worker ownership exists at the frozen operating boundary.
- Evidence: [workspace conflict checks](https://github.com/shijizhi/picocode/blob/c016d4ff9a84c6584f4c09706b05a364b2a5b5dd/src/workspace.rs), [terminal dispatch](https://github.com/shijizhi/picocode/blob/c016d4ff9a84c6584f4c09706b05a364b2a5b5dd/src/terminal.rs), [fork API](https://github.com/shijizhi/picocode/blob/c016d4ff9a84c6584f4c09706b05a364b2a5b5dd/src/session.rs).
- Basis: structural absence review.
- Confidence: high.
- Caveats: the product may be run in independent terminal processes, but the source does not establish an owned cooperative group of those instances.

### Absence scope

- Surfaces inspected: AgentCore, background terminal worker, tool/file conflict logic, session forks/history, command handling and event queues.
- Plausible first-party paths checked: autonomous child worker creation, cross-agent file reservation, competing commitments, conflict detection and settlement return.
- Why no material first-party path remains: wired agent action selection is a single model context, and integrity checks operate on a single local edit/batch.

## S3 — Inside-and-now control

- State: —
- Function: no first-party whole-current supervisor allocates resources, priorities and exceptions among a portfolio of S1 operations.
- Disturbance / variety regulated: tool/model step limits, command timeout, TUI pending queues, session switching and compaction bound an active turn or human interaction.
- Decisive decision or feedback right: no separate current-control actor chooses priorities or reassigns multiple operational commitments; limits and queue processing are fixed.
- Decision owner: model for one task, user for session/model choices, source code for static limits.
- Supporting / enforcement mechanisms: `AgentConfig`, runtime status, event queues, timeouts and session state.
- Closure path: agent's error/time limit returns to its own turn or to user; no whole-current management feedback into distinct operational units.
- Why this is / is not agent-owned: a deterministic runtime loop with limits and a TUI progress display does not itself constitute organizational S3.
- Evidence: [model/tool budgets](https://github.com/shijizhi/picocode/blob/c016d4ff9a84c6584f4c09706b05a364b2a5b5dd/src/agent_core.rs), [TUI dispatch](https://github.com/shijizhi/picocode/blob/c016d4ff9a84c6584f4c09706b05a364b2a5b5dd/src/terminal.rs).
- Basis: structural absence review.
- Confidence: high.
- Caveats: interactive human control is outside the assessed first-party model/meta-organization.

### Absence scope

- Surfaces inspected: step-limit enforcement, command timeout, session picker, terminal event lifecycle, project configuration.
- Plausible first-party paths checked: whole-current multi-operation status, binding allocation, escalation ownership and returned changed commitments.
- Why no material first-party path remains: runtime controls only regulate an individual agent call or interactive application, with no managing S3 decision right evidenced.

## S3* — Complementary audit

- State: —
- Function: no complementary independently grounded evaluator challenges the S1 completion claim and returns binding corrective findings to its controller.
- Disturbance / variety regulated: failed shell commands force investigation and retry, while preview/diff/checkpoint guards flag direct edit errors. These are immediate S1 tool observations.
- Decisive decision or feedback right: no separate read-only model, deterministic post-hoc cross-checker of completion claims or independent raw-source reviewer is wired.
- Decision owner: same acting model for whether a repair succeeded; user may read TUI logs and diff preview.
- Supporting / enforcement mechanisms: `repair_context`, `run_command` status/stderr, edit preview and session event logs.
- Claim being audited: a possible claim that the coding change is done or passes its tests.
- Ordinary reporting path: model observes its own command/tool results, updates context and writes a final answer.
- Complementary access path: human-visible diff and command output, but no separate first-party contradicting audit actor or report-to-controller route.
- Independence boundary: forced repair after a failed command occurs **inside the producer's single model turn**, not independently of its operational evidence flow.
- Who acts on findings: the original model reacts to the same tool result; human can intervene externally.
- Closure path: command failure → error → same-model repair instruction, not separate verifier judgement and corrective veto.
- Why this is / is not agent-owned: mandatory repeat after a direct failed action is operational error handling, not independent audit of a prior reported success.
- Evidence: [repair loop and context](https://github.com/shijizhi/picocode/blob/c016d4ff9a84c6584f4c09706b05a364b2a5b5dd/src/agent_core.rs), [command result reporting](https://github.com/shijizhi/picocode/blob/c016d4ff9a84c6584f4c09706b05a364b2a5b5dd/src/tool.rs).
- Basis: structural absence review.
- Confidence: high.
- Caveats: tests run by the acting model can be useful correctness evidence, but independence has not been established.

### Absence scope

- Surfaces inspected: model completion and repair flow, command/test tool result, workspace diff and edit journal, TUI events.
- Plausible first-party paths checked: raw-source independent reinspection, separate verifier verdict, contradicted success reporting and binding audit-to-repair return.
- Why no material first-party path remains: only first-party operational feedback from the producing agent and optional human inspection are wired.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party prospective sensing/scenario/option evaluation selects and returns future adaptation of the agent organization.
- Disturbance / variety regulated: varying provider/model availability, user-installed skills and evolving codebases influence current task execution or user configuration.
- Decisive decision or feedback right: user manually selects model/skills or updates binary; model's immediate source discovery solves the present task, not the future of the system.
- Decision owner: human for software/model/configuration; operating model for task-bound investigation.
- Supporting / enforcement mechanisms: model switcher, skill/capability discovery, session compression, instruction loader and versioning scripts.
- Closure path: user loads capability/model or agent reads current code → immediate tool context; no prospective environmental intelligence-to-adaptation verdict is returned.
- Why this is / is not agent-owned: loading an existing skill, compaction and choosing providers are not strategic option evaluation with a future-world model.
- Evidence: [features](https://github.com/shijizhi/picocode/blob/c016d4ff9a84c6584f4c09706b05a364b2a5b5dd/README.md), [capability handling](https://github.com/shijizhi/picocode/blob/c016d4ff9a84c6584f4c09706b05a364b2a5b5dd/src/capability.rs), [models](https://github.com/shijizhi/picocode/blob/c016d4ff9a84c6584f4c09706b05a364b2a5b5dd/src/model_picker.rs).
- Basis: structural absence review.
- Confidence: high.
- Caveats: the design document mentions possible future architecture; aspirational text cannot establish a shipped closed loop.

### Absence scope

- Surfaces inspected: capability and instruction loading, model/provider config, session compaction, source roadmap and release scripts.
- Plausible first-party paths checked: outside trend sensing, scenario generation, evaluated future options, authorization and returned new operating architecture.
- Why no material first-party path remains: current capabilities are loaded by user choice; no source-grounded autonomous adaptation owner and feedback were found.

## S5 — Policy and identity

- State: —
- Function: no distinct first-party ultimate legitimacy/organizational identity policy path resolves mission conflicts and returns ratified direction.
- Disturbance / variety regulated: risky commands, workspace escape and model/provider settings are tool-effect limitations, not contested identity.
- Decisive decision or feedback right: no ratified mission/policy revision is issued by a legitimate top-level organizational authority inside the harness.
- Decision owner: human supplies goal and configuration; deterministic command policy restricts effects; model chooses task operations.
- Supporting / enforcement mechanisms: project `CommandApproval`, instruction loader, command risk checks and workspace fences.
- Closure path: command is allowed/denied by static policy → tool outcome to same S1; no ultimate policy deliberation, ratification or persistent charter update.
- Why this is / is not agent-owned: risk gating and user consent per command do not supply an S5 identity-dispute resolution role.
- Evidence: [config/approval](https://github.com/shijizhi/picocode/blob/c016d4ff9a84c6584f4c09706b05a364b2a5b5dd/src/instruction.rs), [command gate](https://github.com/shijizhi/picocode/blob/c016d4ff9a84c6584f4c09706b05a364b2a5b5dd/src/tool.rs).
- Basis: structural absence review.
- Confidence: high.
- Caveats: external institutional policies governing a human user are not first-party harness S5.

### Absence scope

- Surfaces inspected: project instructions/command policy, agent protocol, user prompt entry, workspace restrictions and session settings.
- Plausible first-party paths checked: ultimate identity dispute, authorized policy authority, ratification and durable binding direction into future coding tasks.
- Why no material first-party path remains: all evidenced decisions are operational commands, configuration and pre-existing static safety constraints.

## Recursion

The first-party unit is one coding-agent/model-tool loop. Saved and forked TUI sessions do not imply inter-agent production commitments or recursive management. Provider abstraction is a model API boundary, not an imported meta-harness.

## Variety and escalation

The operating model reacts to file, search and command errors; the runtime enforces finite steps, edit hashes, rollback and command policy. Command failure routes back to the same model to repair. Human can change sessions/models or inspect output; no separate first-party S2 conflict settlement, S3 current portfolio controller, S3* independent auditor, S4 prospective strategy or S5 identity-ratification loop is evidenced.

## Evidence gaps

The frozen commit and GitHub repository identity were checked; first-party runtime entrypoints, agent/tool loop, conflict logic, sessions and model adapter inspected directly. `cargo` was unavailable in this environment, so the Rust upstream suite and inference-backed TUI end-to-end session were **not** executed. Native fake-provider unit test source corroborates the intended loop but is not presented as a test PASS. Design goals and claimed macOS usability do not establish additional agent ownership.

## Assessment summary

PicoCode is a substantive self-contained Rust coding agent (**S1=A**), including real file and command feedback and an explicitly forced repair loop after command failures. Manual session forks, atomic edit batches and per-command policy are useful local features, but the frozen first-party implementation has no verified cross-agent coordination, whole-current manager, independent audit, prospective adaptive strategy or legitimate ultimate-policy closure (**S2/S3/S3*/S4/S5=—**).

Proposed vector: **`A · — · — · — · — · —`**.

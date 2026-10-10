---
harness_id: bbarit-oss
project_name: bbarit-oss
repository: https://github.com/bbarit/bbarit-agent-oss
review_ref: 2cb8b723f2787aa587ef063d366b7cb408ead4aa
reviewed_at: 2026-10-10
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: ?
autonomy_s4: —
autonomy_s5: —
---

# bbarit-oss

## Review boundary

- System in focus: current public Rust bbarit-agent-oss executable as a terminal coding agent, with its own commands.rs agent loop, tools.rs dispatcher, self-process subagents and native --orchestrate/agent_team, session persistence, project memory and wiki.
- Purpose and identity: provider-agnostic autonomous coding and context-aware project assistance, optionally delegating independent tasks to native concurrent child processes.
- Relevant environment: local repository/filesystem, subprocess shells, provider API result, user authorization, independent child process results, previous sessions and project files.
- Standard-distribution boundary: owned first-party Rust application and bundled personas; vendor/semble is an embedded semantic search dependency, external Pi/qwen-code are conceptual lineage rather than first-party decision owners.
- Credited operating / distribution surfaces: src/commands.rs, src/tools.rs, src/orchestrator.rs, src/llm.rs, src/session.rs, src/memory.rs, src/wiki.rs, CLI/TUI modes.
- Adjacent first-party surfaces excluded from ownership: BBARIT Terminal desktop app, third-party Pi agent design, qwen-code memory implementation lineage, vendor/semble independent code, remote MCP servers, GitHub CI/maintainers, eval artifacts and persona text absent supporting execution wiring.
- First-party operating / deployment modes considered: normal coding TUI/--print; native autoapproved/trusted subagent team on shared cwd with ≤4 concurrency; read-only plan/persona mode; memory auto-extract/recall; bundled reviewer persona as potential scoped audit path.
- Recursion level: one agentic coding session and its optional directly spawned worker processes as lower-level task operating units; no ownership transitivity from predecessor systems.
- Reviewed revision: 2cb8b723f2787aa587ef063d366b7cb408ead4aa.
- Observation date: 2026-10-10.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

The executable is an independent Rust coding-agent runtime rather than a wrapper of Pi. First-party commands.rs runs its own multi-turn model/tool loop. The model chooses native read/write/patch/shell/search tools, trusted_tool dispatch applies project trust and plan/persona guards, and returned tool results feed subsequent model turns. The loop includes read-before-edit and one verification nudge if changed code was not checked, auto-continuation bounds, failure-repeat guards, session state and provider adapters.

Native orchestrator.rs forks copies of the current executable with separate child sessions and bounded contexts; agent_team launches up to four children concurrently for model-given independent prompts, in the **same cwd**, then collects and labels final reports. There is no automatic Git worktree isolation, cross-worker file conflict arbitration or model-driven reallocation after failure in that stock path. Auto-memory extracts prior session decisions to durable notes and a project wiki stores repository knowledge. Optional MCP, LSP, skills, review personas and extension interop are tool/context surfaces rather than new organizational functions by declaration.

Potential S3* audit is deliberately unresolved: first-party child process can run a bundled code-reviewer persona and return an independent context summary. However, the shipped operating contract does not require a separate source-native code review over changed files or close a mandatory report/correction path, and the reviewer persona lacks an explicit read-only mode declaration. This does not suffice to classify A, yet a negative would exceed the narrow evidence.

Frozen sources: [src/commands.rs](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/src/commands.rs); [src/orchestrator.rs](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/src/orchestrator.rs); [src/tools.rs](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/src/tools.rs); [src/memory.rs](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/src/memory.rs); [ARCHITECTURE.md](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/ARCHITECTURE.md); [PROVENANCE.md](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/PROVENANCE.md).

## Operational model

The main coding model chooses tools and optionally divides work into child processes. Rust enforces trust and execution/loop limits. Child results are returned as summaries to the original model, not to a separate autonomous multi-unit resource regulator. Historical memory may improve continuity without an outside-and-then strategic change process.

## S1 — Operations

- State: A
- Function: Code edit, read, search, shell execution and feedback on current task state.
- Disturbance / variety regulated: Unexpected source code, command failures, generated edits and user needs.
- Decisive decision or feedback right: Select subsequent tool calls and respond to observed tool outcomes.
- Decision owner: Rust run_agent_loop driven by the selected coding model.
- Supporting / enforcement mechanisms: Native provider completion, tool registry, read-before-edit, anchored edits, turn limits, verification and session JSONL.
- Closure path: User request plus code context -> model chooses read/edit/bash -> owned handler performs operation -> tool result re-enters same conversation -> the agent chooses new action or completion.
- Boundary reachability: Shipped --print/TUI calls commands::run_agent_loop and first-party execute_trusted_tool_call, rather than wrapping an external Pi executable.
- Why this is / is not agent-owned: Main coding model makes operational decisions; Rust code transports/guards them and does not import upstream Pi ownership.
- Evidence: [src/commands.rs](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/src/commands.rs); [src/tools.rs](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/src/tools.rs); [src/llm.rs](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/src/llm.rs); [src/lib.rs](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/src/lib.rs); [ARCHITECTURE.md](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/ARCHITECTURE.md).
- Basis: structural + explicit.
- Confidence: high.
- Caveats: Providers remain external inference dependencies. Risky tools require trusted project or explicit approvals..


## S2 — Coordination

- State: —
- Function: No first-party closed inter-S1 interference attenuation loop established for parallel code-writing child processes.
- Disturbance / variety regulated: Separate children writing same project directory could collide or oscillate, but there is no assigned conflict detection or attenuation decision path among them.
- Decisive decision or feedback right: None demonstrated beyond single child dispatch, a fixed four-parallel cap and ordered collection of summaries.
- Decision owner: No S2 coordinating decision owner established.
- Supporting / enforcement mechanisms: Child re-execution, 4-way parallel launch, shared cwd, optional persona and trust gate, one-level nesting cap.
- Closure path: Agent chooses task prompts, children run on shared directory, return outcome paragraphs; the parent can read them but no specific inter-child conflict adjustment/control is wired.
- Why this is / is not agent-owned: Parallelism, generic task decomposition, result collection and per-child caps are not by themselves S2. Read-before-write fingerprint protection is per-agent file safety and not evidenced as cross-worker regulator.
- Evidence: [src/orchestrator.rs](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/src/orchestrator.rs); [src/commands.rs](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/src/commands.rs); [src/tools.rs](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/src/tools.rs); [src/hashline.rs](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/src/hashline.rs).
- Basis: structural + explicit.
- Confidence: medium-high.
- Caveats: An orchestrator prompt may ask for disjoint work, but no first-party enforceable partition or conflict feedback is shown..

### Absence scope

- Surfaces inspected: Native orchestrator and subprocess runs, tool and file guards, task/persona schema, shared directory and concurrency rules.
- Plausible first-party paths checked: Parallel fanout, current working directory, separate sessions, maximum concurrent count, per-file read-before-write fingerprints and patch conflict tokens.
- Why no material first-party path remains: No observed first-party regulator detects interfering different S1 workers and returns a functional coordination change to later child behavior; concurrent children operate in same cwd, and summary aggregation alone cannot establish a whole interference loop.


## S3 — Inside-and-now control

- State: —
- Function: No distinct ongoing whole-current operations manager with rights over multiple worker commitments.
- Disturbance / variety regulated: Live child failures, competing task commitments, resource allocation and work priority could require project-wide intervention.
- Decisive decision or feedback right: No function-specific whole-current decision established; the code launches a bounded batch and orders reports.
- Decision owner: No S3 metasystem owner in the reviewed CLI runtime.
- Supporting / enforcement mechanisms: Cancellation, thread joins, tool budgets, todo lists and summary format.
- Closure path: Subagent summaries return to the parent agent but the fixed orchestrator has no independent source-wired whole-current decision and corrective reassignment of active S1 units.
- Why this is / is not agent-owned: The model may delegate and synthesize, while Go/Rust (here Rust) orchestration mechanics constrain work; neither supplies the separate management closure automatically.
- Evidence: [src/orchestrator.rs](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/src/orchestrator.rs); [src/commands.rs](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/src/commands.rs); [src/tools.rs](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/src/tools.rs).
- Basis: structural + explicit.
- Confidence: medium-high.
- Caveats: The assessment does not deny that an end-user could script higher-order coordination externally..

### Absence scope

- Surfaces inspected: Rust top-level agent loop, orchestrator team/child spawn, todo and cost handling, cancel mechanics.
- Plausible first-party paths checked: Subtask reports, CLI --orchestrate, child role selection, cost/turn limits, ongoing progress cues.
- Why no material first-party path remains: No first-party role reads live whole-fleet commitments then makes and feeds a resource/priority/reassignment decision to operating units. Execution uses fixed batch-and-report mechanics.


## S3* — Complementary audit

- State: ?
- Function: Reviewer persona can be delegated to an isolated child agent, but an independently sufficient audit judgment-plus-corrective operating feedback path is unresolved.
- Disturbance / variety regulated: Code correctness and completeness errors might escape the parent coder's own claimed completion.
- Decisive decision or feedback right: The main agent can ask a code-reviewer persona subagent to inspect a task, but the source does not show a standard required source-native diff audit coupled to systematic correction of its findings.
- Decision owner: Potential separate reviewer model and ordinary parent coder; ownership of distinct audit closure not proven.
- Supporting / enforcement mechanisms: Child executable process with independent session, reviewer persona brief, inherited project directory and read-only mode support if requested.
- Closure path: Optional specialist report returns to parent model; a user/model may choose corrections, but there is no demonstrated first-party standardized audit input and corrective return contract for coding changes.
- Why this is / is not agent-owned: A specialist persona or generic child task tool is not sufficient to prove independent complementary audit; evidence is too incomplete to publish either positive A/C or a defensible absence.
- Evidence: [src/orchestrator.rs](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/src/orchestrator.rs); [src/tools.rs](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/src/tools.rs); [src/commands.rs](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/src/commands.rs); [src/personas.rs](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/src/personas.rs); [personas/engineering/code-reviewer.md](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/personas/engineering/code-reviewer.md).
- Basis: structural + explicit.
- Confidence: medium for candidate; unresolved for S3* ownership.
- Caveats: The code-reviewer persona in the pinned bundle does not itself declare read-only mode. The child process can mutate with inherited trusted approval; isolation of model context is not a complete audit independence guarantee..


## S4 — Outside-and-then intelligence

- State: —
- Function: No prospective external intelligence/capability adaptation organization established.
- Disturbance / variety regulated: Future environmental shifts and alternative capabilities are not actively monitored/selected through a dedicated model-owned organizational feedback loop.
- Decisive decision or feedback right: None evidenced for S4; memory stores and recalls historically inferred facts.
- Decision owner: No S4 agent or legitimate parent decision owner established.
- Supporting / enforcement mechanisms: Automatic background memory extraction, project wiki, cached semantic search, skill/persona config, model selection.
- Closure path: Prior session facts are extracted and can enter later turns, but no future-facing environmental distinction -> adaptive option judgment -> modification of system repertoire is wired.
- Why this is / is not agent-owned: Persistence, wiki, role libraries, imported skills and provider switching are ordinary context/tool support, not S4 by label.
- Evidence: [src/memory.rs](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/src/memory.rs); [src/wiki.rs](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/src/wiki.rs); [src/resources.rs](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/src/resources.rs); [src/commands.rs](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/src/commands.rs).
- Basis: structural + explicit.
- Confidence: medium-high.
- Caveats: External persona libraries and opt-in tool interop do not donate organizational adaptation..

### Absence scope

- Surfaces inspected: Memory auto-extraction/recall, project wiki, semantic search, resource/persona selection and provider settings.
- Plausible first-party paths checked: Background data distillation, new project wiki, tool extensions, provider model switches, skills and user commands.
- Why no material first-party path remains: No first-party prospective environment-scanning process develops options, decides an autonomous capability-change strategy and closes that to present S1 operations.


## S5 — Policy and identity

- State: —
- Function: No ultimate-policy/identity governance adjudication and returned binding decision.
- Disturbance / variety regulated: Individual tool trust or read-only approval is a task-level authorization, not organization-wide identity tension.
- Decisive decision or feedback right: No ultimate governing choice; human or configured trust permissions allow/deny discrete execution.
- Decision owner: Operator/configured gates constrain actions without an S5 owner.
- Supporting / enforcement mechanisms: Trust gate, plan mode, persona restrictions, nesting cap, upstream provenance docs, session configuration.
- Closure path: Tool approval changes whether a call runs; it does not resolve identity/constitutional issues and govern downstream organizational policy.
- Why this is / is not agent-owned: Inherited Pi design claims, static personas and trusted-project control do not constitute S5.
- Evidence: [src/trust.rs](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/src/trust.rs); [src/commands.rs](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/src/commands.rs); [src/personas.rs](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/src/personas.rs); [PROVENANCE.md](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/PROVENANCE.md).
- Basis: structural + explicit.
- Confidence: medium-high.
- Caveats: There may be human governance of the developer organization, excluded from installed coding agent recursion..

### Absence scope

- Surfaces inspected: Project trust, plan mode, persona governance, CLI setup, standard help, developer provenance.
- Plausible first-party paths checked: Human permissions, model/provider choice, persona identity prompts, CLI flags, project wiki editing.
- Why no material first-party path remains: No owned ultimate-policy decision right with authoritative actor and policy-to-subsequent-operation return path appears at the installed coding-harness recursion.


## Distributed OSS parent arrangement

The public Rust repository and maintainer process do not provide the installed user's coding session with parent-governed S3/S4/S5 authority. Pi and qwen-code design references are excluded from ownership and all states are reconstructed from owned Rust code at the frozen SHA.

## Self-hosted and non-human modes

User-run/local/cloud models can operate the same Rust loop; automatic tool choice remains within the project trust boundary. Native subprocess team members inherit the same working directory and auto-approval mode after a trust gate. Their concurrency changes operating variety but is not proof of S2 coordination.

## Recursion

Individual --print child processes have distinct context/model tool loops and can produce task results. The developer's fixed capped batch-and-collect launcher does not automatically establish complete VSM recursion or a separate metasystem governing conflict, adaptive project resources or policy.

## Variety and escalation

Native tool errors, repeated command failures and unverified changes can produce same-agent corrective nudges. A user may reject risky calls or cancel whole team work; planned permission changes affect tool rights, not ultimate-policy governance. Results from children return to parent but inter-child conflict attenuation is not evidenced.

## Evidence gaps

- Real concurrent subagents have shared cwd and can edit; inter-agent coordination must not be inferred from the word orchestrator.
- A bundled reviewer persona may support an independently composed audit but the first-party correction/audit contract is not proved here; S3* remains ? rather than a positive or absence.
- Historical memory/auto-wiki and opt-in external tools cannot establish prospective S4 governance by themselves.
- The structural review does not claim benchmark quality or tested multi-agent code correctness.

---
harness_id: smallcode
project_name: SmallCode
repository: https://github.com/Doorman11991/smallcode
review_ref: 624970cce81657fd2751ee7f11ba85f35f2bb5c3
reviewed_at: 2026-10-31
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

# SmallCode

## Review boundary

- System in focus: the installed SmallCode terminal coding harness at the pinned revision.
- Purpose and identity: complete software tasks with local small language models.
- Relevant environment: a user's working repository, shell/test tools, local or configured remote model endpoints and optional MCP servers.
- Standard-distribution boundary: npm/checkout CLI, classic/TUI and API/ACP surfaces backed by the shipped agent loop.
- Credited operating / distribution surfaces: `bin/smallcode.js`, executor/tools, session/context/plan state, local memory, model routing and optional reviewer.
- Adjacent first-party surfaces excluded from ownership: benchmark scoring, build/release CI and repository contributor activity; role/team files and an uncalled parallel executor are not credited as active multi-unit organization.
- First-party operating / deployment modes considered: local default model, opt-in escalation/reviewer, classic/TUI, headless task and configured provider modes.
- Recursion level: one SmallCode coding session, not the developer organization or the model provider.
- Reviewed revision: `624970cce81657fd2751ee7f11ba85f35f2bb5c3`.
- Observation date: 2026-10-31.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The Node CLI owns a model-to-tool loop, parses/reconstructs tool calls, executes file/shell operations and returns observations to conversation history. Context eviction, plan tracking, validation/fix prompts, snapshots, JSON/SQLite memory and model escalation support the coding actor. The agent chooses operations while deterministic guards enforce limits and protect editing. The optional reviewer makes a separate model request but receives task text, filenames and the assistant's response summary, rather than independently reading changed artifacts. Its result is injected as a follow-up note.

The dependency graph recognizes shared-file plan steps and computes batches; the CLI stores/displays those batches. The separate parallel executor exports mini-loops, but the reviewed CLI does not invoke it. This distinction prevents importing an unwired multi-worker mode into the installed session. Model endpoints and budget-aware-mcp are dependencies rather than separate credited regulators. The pinned LICENSE grants MIT terms.

## Operational model

The coding actor owns task-local choices: inspect source, select tools, edit, respond to errors and continue toward a result. The user selects the task/configuration and may intervene. Tool scoring, context limits and validation are support; none alone establishes a metasystem function. Removing the model actor leaves no equivalent discretionary coding decision.

## S1 — Operations

- State: A
- Function: produce a software change or informed answer in the working repository.
- Disturbance / variety regulated: unknown code, tool failures, invalid edits and incomplete task information.
- Decisive decision or feedback right: choose the next inspection/action and revise the implementation from returned observations.
- Decision owner: the model-driven SmallCode coding actor.
- Supporting / enforcement mechanisms: tool-call parsing, executor, context/plan state, validation and retry limits.
- Closure path: model response → tool execution → tool observations/validation errors → next model decision and file changes.
- Boundary reachability: the packaged CLI invokes `runAgentLoop`; the model/tool loop and validation feedback are active in normal task execution.
- Why this is / is not agent-owned: the model chooses concrete work; the runtime transports and constrains those choices.
- Evidence: [CLI loop and feedback](https://github.com/Doorman11991/smallcode/blob/624970cce81657fd2751ee7f11ba85f35f2bb5c3/bin/smallcode.js), [executor](https://github.com/Doorman11991/smallcode/blob/624970cce81657fd2751ee7f11ba85f35f2bb5c3/bin/executor.js), [architecture](https://github.com/Doorman11991/smallcode/blob/624970cce81657fd2751ee7f11ba85f35f2bb5c3/ARCHITECTURE.md).
- Basis: structural.
- Confidence: high.
- Caveats: source assessment; no live model performance claim.

## S2 — Coordination

- State: —
- Function: no closed inter-S1 coordination relation is supplied in the assessed installed session.
- Disturbance / variety regulated: same-file parallel edits are recognized by the dependency graph, but no active parallel-worker path closes their regulation here.
- Decisive decision or feedback right: no in-boundary autonomous coordination owner established.
- Decision owner: not established; dependency extraction and batching are deterministic.
- Supporting / enforcement mechanisms: plan graph and dormant parallel-executor exports.
- Closure path: batch structure is stored/displayed, not dispatched to parallel units by the reviewed CLI.
- Why this is / is not agent-owned: plan sequencing and exported mini-loops do not establish a reachable coordinating actor.
- Evidence: [dependency graph](https://github.com/Doorman11991/smallcode/blob/624970cce81657fd2751ee7f11ba85f35f2bb5c3/src/session/dependency_graph.js), [parallel executor](https://github.com/Doorman11991/smallcode/blob/624970cce81657fd2751ee7f11ba85f35f2bb5c3/src/session/parallel_executor.js), [CLI graph call sites](https://github.com/Doorman11991/smallcode/blob/624970cce81657fd2751ee7f11ba85f35f2bb5c3/bin/smallcode.js).
- Basis: structural.
- Confidence: medium-high.
- Caveats: the exported executor could support future composition; that is not the assessed shipped orchestration.

### Absence scope

- Surfaces inspected: CLI plan capture and graph call sites, parallel executor, session modules, architecture, agent/team definitions.
- Plausible first-party paths checked: shared-file dependency batches, isolated per-step loops, role/team configuration and result merging.
- Why no material first-party path remains: the actual CLI only records the batches; no call wires the parallel executor and S2-specific agent discretion into this session. Labels/configuration do not close that missing path.

## S3 — Inside-and-now control

- State: —
- Function: no separate whole-system current-control loop established.
- Disturbance / variety regulated: local model failure, validation errors and context exhaustion remain coding-session operational variety.
- Decisive decision or feedback right: fixed limits and fallback thresholds do not demonstrate resource/commitment bargaining on behalf of a multi-unit whole.
- Decision owner: developer/operator selects configuration; coding actor chooses local repair.
- Supporting / enforcement mechanisms: governor, token monitor, early-stop, hard-fail checks and escalation.
- Closure path: failures return to the coding loop; no distinct whole-system current-control decision is reconstructed.
- Why this is / is not agent-owned: autonomous task repair is S1; budget enforcement alone is not S3.
- Evidence: [governor](https://github.com/Doorman11991/smallcode/blob/624970cce81657fd2751ee7f11ba85f35f2bb5c3/bin/governor.js), [budget policy](https://github.com/Doorman11991/smallcode/blob/624970cce81657fd2751ee7f11ba85f35f2bb5c3/src/compiled/features/policy.js), [escalation](https://github.com/Doorman11991/smallcode/blob/624970cce81657fd2751ee7f11ba85f35f2bb5c3/bin/escalation.js).
- Basis: structural.
- Confidence: medium-high.
- Caveats: no S3 parent mode is inferred from changing a setting.

### Absence scope

- Surfaces inspected: governor, policy budgets, CLI validation/decomposition/escalation, configuration and live settings.
- Plausible first-party paths checked: failure-driven model changes, hard-fail stop, token budget enforcement and user settings.
- Why no material first-party path remains: these paths regulate one task or enforce preselected limits without a whole-system discretionary control/returned parent-control relation.

## S3* — Complementary audit

- State: —
- Function: no materially independent access to operational reality established beyond production checks.
- Disturbance / variety regulated: potentially incorrect generated code and completion claims.
- Decisive decision or feedback right: the optional reviewer critiques the writer's summary rather than independently inspecting artifacts.
- Decision owner: optional reviewer model owns textual critique; it does not acquire an independent audit access path.
- Supporting / enforcement mechanisms: ordinary compile/run validation, semantic self-critique and asynchronous history injection.
- Closure path: errors/critique enter conversation history; that supplies corrective feedback without establishing complementary audit.
- Why this is / is not agent-owned: a second model call is not sufficient independence for the operational code claim.
- Evidence: [reviewer input construction](https://github.com/Doorman11991/smallcode/blob/624970cce81657fd2751ee7f11ba85f35f2bb5c3/src/model/reviewer.js), [validation and reviewer call sites](https://github.com/Doorman11991/smallcode/blob/624970cce81657fd2751ee7f11ba85f35f2bb5c3/bin/smallcode.js), [verifier](https://github.com/Doorman11991/smallcode/blob/624970cce81657fd2751ee7f11ba85f35f2bb5c3/bin/governor.js).
- Basis: structural.
- Confidence: high.
- Caveats: a different endpoint is configurable, but does not change the supplied evidence from summary to raw artifact.

### Absence scope

- Surfaces inspected: reviewer implementation and CLI invocation/await/injection, edit validation and benchmark/evaluation separation.
- Plausible first-party paths checked: opt-in reviewer endpoint/model, semantic edit check, syntax/execution checks and final-response guard.
- Why no material first-party path remains: the reviewer only sees bounded task/response text and filenames; ordinary checks belong to the producer's regular path. No shipped complementary direct-evidence audit owner/return is established.

## S4 — Outside-and-then intelligence

- State: —
- Function: no outside-and-then capability adaptation loop established.
- Disturbance / variety regulated: repeated internal failures and relevant previous task knowledge.
- Decisive decision or feedback right: memory retrieval and failure thresholds do not develop prospective environmental adaptation options.
- Decision owner: coding actor performs task work; routing/memory code applies fixed selection and capture rules.
- Supporting / enforcement mechanisms: trace-derived evidence memory, adaptive routing, escalation and context retrieval.
- Closure path: prior outcomes can inform later tasks; no evidenced prospective option-development and capability-control conversation.
- Why this is / is not agent-owned: persistence and reactive model fallback do not establish S4.
- Evidence: [evidence memory](https://github.com/Doorman11991/smallcode/blob/624970cce81657fd2751ee7f11ba85f35f2bb5c3/src/memory/evidence.js), [adaptive router](https://github.com/Doorman11991/smallcode/blob/624970cce81657fd2751ee7f11ba85f35f2bb5c3/src/model/adaptive_router.js), [architecture](https://github.com/Doorman11991/smallcode/blob/624970cce81657fd2751ee7f11ba85f35f2bb5c3/ARCHITECTURE.md).
- Basis: structural.
- Confidence: medium-high.
- Caveats: future custom agents or user-selected research tasks are not credited.

### Absence scope

- Surfaces inspected: task planning, memory capture/retrieval/hygiene, model fallback/routing, architecture and configuration.
- Plausible first-party paths checked: reusable task evidence, tool success scores, planner and model escalation.
- Why no material first-party path remains: the shipped paths improve current task execution from internal outcomes; they do not close external/future distinctions → adaptation options → present capability. No separate parent adaptation loop is supplied.

## S5 — Policy and identity

- State: —
- Function: no runtime identity/ultimate-policy adjudication loop established.
- Disturbance / variety regulated: fixed task constraints, permissions and configured provider limits.
- Decisive decision or feedback right: configuration and user task commands do not constitute an identity-level proposal/decision/return path.
- Decision owner: operator/developer supplies constraints; no qualifying S5 owner is reconstructed.
- Supporting / enforcement mechanisms: prompts, configuration, budget and permission guards.
- Closure path: operational commands/configuration affect execution; no ultimate-policy escalation/returned decision is established.
- Why this is / is not agent-owned: static boundaries and ordinary human intervention do not imply S5.
- Evidence: [configuration](https://github.com/Doorman11991/smallcode/blob/624970cce81657fd2751ee7f11ba85f35f2bb5c3/bin/config.js), [commands](https://github.com/Doorman11991/smallcode/blob/624970cce81657fd2751ee7f11ba85f35f2bb5c3/bin/commands.js), [CLI prompts/guards](https://github.com/Doorman11991/smallcode/blob/624970cce81657fd2751ee7f11ba85f35f2bb5c3/bin/smallcode.js).
- Basis: structural.
- Confidence: medium-high.
- Caveats: repository maintainers' authority is outside the installed-session recursion.

### Absence scope

- Surfaces inspected: CLI/task input, settings/configuration, commands, prompts, budget policy and security/architecture documentation.
- Plausible first-party paths checked: operator configuration, task approvals/commands and hard constraints.
- Why no material first-party path remains: no shipped identity/ultimate-policy matter reaches legitimate parent authority and returns through an explicit policy-decision path; only ordinary operational configuration is evidenced.

## Distributed OSS parent arrangement

MIT distribution and multiple contributors do not establish parent governance of a user's installed session. Contributor/CI authority is adjacent to this boundary; no organization-level parent modifier is inferred.

## Self-hosted and non-human modes

Local model use and configured external providers preserve the same owner distinction. Optional reviewer/escalation changes support, not demonstrated S3/S4/S5 ownership.

## Recursion

Named specialist agents, plan steps and the exported parallel mini-loop do not prove nested viable systems.

## Variety and escalation

Context compaction, validation/fix feedback, decomposition, snapshots and opt-in stronger-model fallback absorb coding disturbances. Exhausted limits and user intervention remain visible operational exits.

## Evidence gaps

No live model run or performance claim. The dormant parallel-execution module is not treated as a supported active organization; a future revision wiring it requires new-ref review. This assessment is bounded to the pinned distribution.

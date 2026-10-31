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
autonomy_s3_star: C
autonomy_s4: P
autonomy_s5: —
---

# SmallCode

## Review boundary

- System in focus: the installed SmallCode terminal coding harness at the pinned revision.
- Purpose and identity: complete software tasks with local small language models.
- Relevant environment: a user's working repository, shell/test tools, local or configured remote model endpoints and optional MCP servers.
- Standard-distribution boundary: npm/checkout CLI, classic/TUI and API/ACP surfaces backed by the shipped agent loop.
- Credited operating / distribution surfaces: `bin/smallcode.js`, executor/tools, session/context/plan state, local memory, model routing and optional reviewer.
- Adjacent first-party surfaces excluded from ownership: benchmark scoring, build/release CI and repository contributor activity; the uncalled parallel executor is not credited as active multi-unit organization. Shipped /agent and /team command paths are considered separately.
- First-party operating / deployment modes considered: local default model, opt-in escalation/reviewer, classic/TUI, headless task, configured provider, /agent, /team and operator-promoted /evolve modes.
- Recursion level: one SmallCode coding session, not the developer organization or the model provider.
- Reviewed revision: `624970cce81657fd2751ee7f11ba85f35f2bb5c3`.
- Observation date: 2026-10-31.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The Node CLI owns a model-to-tool loop, parses/reconstructs tool calls, executes file/shell operations and returns observations to conversation history. Context eviction, plan tracking, validation/fix prompts, snapshots, JSON/SQLite memory and model escalation support the coding actor. The agent chooses operations while deterministic guards enforce limits and protect editing. The optional reviewer makes a separate model request but receives task text, filenames and the assistant's response summary, rather than independently reading changed artifacts. Its result is injected as a follow-up note. Separately, /agent and /team invoke bounded tool-using specialist conversations; the review team is a sequential critic/red-team/QA pipeline. /evolve detects repeated user requests and retries in saved traces, asks a model for a reusable skill draft and requires operator promotion before future-session activation.

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

- Surfaces inspected: CLI plan capture and graph call sites, parallel executor, session modules, architecture, agent/team definitions and the sequential team runner.
- Plausible first-party paths checked: shared-file dependency batches, isolated per-step loops, role/team configuration and result merging.
- Why no material first-party path remains: the actual CLI only records the batches; no call wires the parallel executor and S2-specific agent discretion into this session. The reachable /team runner passes one agent's output to the next without a specific inter-unit interference-regulation relation; sequential specialization alone is not S2.

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

- State: C
- Function: complementary challenge of a coding actor's implementation/completion claims using independently inspected code and checks.
- Disturbance / variety regulated: producer summaries can omit defects or unverified requirements.
- Decisive decision or feedback right: the critic decides OKAY/REJECT from its own source inspection; the caller must compose the corrective return to the producer.
- Decision owner: the separately invoked critic actor owns audit judgment; the operator/developer owns invocation and subsequent corrective integration.
- Supporting / enforcement mechanisms: isolated AgentRunner context, narrowed read/search/bash/test tools, bounded steps and command output.
- Closure path: /agent critic or /team review → isolated inspection → finding/verdict returned to the caller; automatic re-entry into the production coding actor is not wired, hence C rather than A.
- Boundary reachability: bin/commands.js invokes AgentRunner/runTeam using shipped agent/team definitions. This is an optional CLI mode, not repository-development dogfood.
- Why this is / is not agent-owned: the audit-specific constructor supplies a real independent tool-using judgment path, while corrective ownership/closure still needs composition.
- Claim being audited: implementation satisfies the requirements and is ready to ship.
- Ordinary reporting path: coding actor response and routine post-edit validation.
- Complementary access path: critic reads the spec and changed files and runs checks; red-team can separately inspect attack surfaces.
- Independence boundary: AgentRunner starts a new bounded conversation without parent history and permits raw artifact access. Different model tiers are optional; independence rests on evidence access and separate judgment.
- Who acts on findings: caller/operator must return findings for repair; team pipeline alone prints the final result.
- Evidence: [critic](https://github.com/Doorman11991/smallcode/blob/624970cce81657fd2751ee7f11ba85f35f2bb5c3/agents/critic.md), [isolated runner](https://github.com/Doorman11991/smallcode/blob/624970cce81657fd2751ee7f11ba85f35f2bb5c3/src/plugins/agent_runner.js), [command wiring](https://github.com/Doorman11991/smallcode/blob/624970cce81657fd2751ee7f11ba85f35f2bb5c3/bin/commands.js), [team runner](https://github.com/Doorman11991/smallcode/blob/624970cce81657fd2751ee7f11ba85f35f2bb5c3/src/plugins/team_runner.js).
- Basis: structural.
- Confidence: medium-high.
- Caveats: the asynchronous summary-only reviewer is insufficient by itself and is not the credited path. Merely running the sequential review team does not prove autonomous corrective audit closure.

## S4 — Outside-and-then intelligence

- State: P
- Function: adapt reusable coding capability to recurring unmet user demand beyond a single task.
- Disturbance / variety regulated: repeated requests that lack a corresponding skill and recurrent tool friction in prior sessions.
- Decisive decision or feedback right: select whether a proposed reusable skill should become active in future sessions.
- Decision owner: the legitimate local operator; the model generates an option, but /evolve promote is an explicit operator decision.
- Supporting / enforcement mechanisms: trace storage, friction extraction, model proposal, proposal validation, draft storage, promotion and skill loading.
- Closure path: /evolve examines saved demand/friction → model proposes one reusable skill → operator reviews and /evolve promote activates it for subsequent sessions → the skill can govern later task execution.
- Boundary reachability: /evolve and /evolve promote are registered shipped CLI commands; promoted drafts enter the normal SkillManager skill directory.
- Why this is / is not agent-owned: option generation is model-assisted, but the decisive adaptation right remains parent-owned. No autonomous A/C base is claimed from a human-required promotion path.
- External distinction: repeated user requests not covered by existing skill keywords distinguish unmet demand in the harness's local user/task environment.
- Future / prospective distinction: the proposed skill is reusable guidance for later similar work, rather than a patch only to the current task.
- Adaptation option generated: one named, validated skill proposal with trigger, keywords, body and rationale.
- Path back into current capability / S3: operator promotion moves the draft into active skills; ordinary skill selection/injection then affects later operation. No separate autonomous S3 is inferred.
- Evidence: [command proposal/promotion](https://github.com/Doorman11991/smallcode/blob/624970cce81657fd2751ee7f11ba85f35f2bb5c3/bin/commands.js), [demand/friction extraction](https://github.com/Doorman11991/smallcode/blob/624970cce81657fd2751ee7f11ba85f35f2bb5c3/src/plugins/friction_analyzer.js), [skills activation](https://github.com/Doorman11991/smallcode/blob/624970cce81657fd2751ee7f11ba85f35f2bb5c3/src/plugins/skills.js), [proposal machinery](https://github.com/Doorman11991/smallcode/blob/624970cce81657fd2751ee7f11ba85f35f2bb5c3/src/plugins/evolver.js).
- Basis: structural.
- Confidence: medium.
- Caveats: only the demand-driven reusable-skill path is credited; generic evidence memory, task planning and reactive model routing do not independently establish S4. No claim of measured adaptation benefit.

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

MIT distribution and multiple contributors do not establish parent governance of a user's installed session. Contributor/CI authority is adjacent to this boundary. The S4 parent finding is local to the operator's installed harness, not the upstream OSS organization.

## Self-hosted and non-human modes

Local model use and configured external providers preserve the same owner distinction. The supported /agent audit constructor and /evolve operator adaptation path are distinguished from ordinary reviewer/escalation support. No autonomous S3/S5 mode is inferred.

## Recursion

Named specialist agents, plan steps and the exported parallel mini-loop do not prove nested viable systems.

## Variety and escalation

Context compaction, validation/fix feedback, decomposition, snapshots and opt-in stronger-model fallback absorb coding disturbances. Exhausted limits and user intervention remain visible operational exits.

## Evidence gaps

No live model run or performance claim. The dormant parallel-execution module is not treated as a supported active organization; a future revision wiring it requires new-ref review. This assessment is bounded to the pinned distribution.

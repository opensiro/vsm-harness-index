---
harness_id: rocinante
project_name: Rocinante
repository: https://github.com/djynnius/rocinante
review_ref: 86aa7369bc775c583d46f8c3bb286c76d0401220
reviewed_at: 2026-10-11
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: C
autonomy_s4: C
autonomy_s5: —
---

# Rocinante

## Review boundary

- System in focus: shipped Rocinante Rust terminal coding agent including model/tool loop, CLI wiring, nested task agents, parallel execution scheduling, optional trusted-check verification, and learned global rules.
- Purpose and identity: solve requested code/research tasks in a local workspace using chosen first-party tools and delegating to configurable subagent profiles.
- Relevant environment: user, local worktree and developer tooling, Ollama or hosted inference endpoints, file system and test commands, user corrections and recurring behavioral preferences.
- Standard-distribution boundary: `rocinante-cli` setup with first-party `Agent`, `TaskTool`, `Verifier`, `Lessons`, tool registry, local model gates and config. The optional configured `check_command` is run by first-party code but its content is selected by the operator; untrusted user scripts are not counted as first-party auditors.
- Credited operating / distribution surfaces: [crates/rocinante-core/src/agent/agent.rs](https://github.com/djynnius/rocinante/blob/86aa7369bc775c583d46f8c3bb286c76d0401220/crates/rocinante-core/src/agent/agent.rs), [crates/rocinante-core/src/agent/subagent.rs](https://github.com/djynnius/rocinante/blob/86aa7369bc775c583d46f8c3bb286c76d0401220/crates/rocinante-core/src/agent/subagent.rs), [crates/rocinante-cli/src/setup.rs](https://github.com/djynnius/rocinante/blob/86aa7369bc775c583d46f8c3bb286c76d0401220/crates/rocinante-cli/src/setup.rs), [crates/rocinante-core/src/verifier.rs](https://github.com/djynnius/rocinante/blob/86aa7369bc775c583d46f8c3bb286c76d0401220/crates/rocinante-core/src/verifier.rs), [crates/rocinante-core/src/lessons.rs](https://github.com/djynnius/rocinante/blob/86aa7369bc775c583d46f8c3bb286c76d0401220/crates/rocinante-core/src/lessons.rs), [crates/rocinante-core/src/prompt/mod.rs](https://github.com/djynnius/rocinante/blob/86aa7369bc775c583d46f8c3bb286c76d0401220/crates/rocinante-core/src/prompt/mod.rs), [crates/rocinante-core/src/config/schema.rs](https://github.com/djynnius/rocinante/blob/86aa7369bc775c583d46f8c3bb286c76d0401220/crates/rocinante-core/src/config/schema.rs).
- Adjacent first-party surfaces excluded from ownership: [.github/workflows/ci.yml](https://github.com/djynnius/rocinante/blob/86aa7369bc775c583d46f8c3bb286c76d0401220/.github/workflows/ci.yml), [CHANGELOG.md](https://github.com/djynnius/rocinante/blob/86aa7369bc775c583d46f8c3bb286c76d0401220/CHANGELOG.md), packaged skills as reusable task instructions, package update command and external model internals.
- First-party operating / deployment modes considered: terminal REPL/TUI; enabled-by-default configurable `[verification]` with automatic and manual `/verify` modes, trusted project check command optionally configured; `[learning]` if enabled; serial/parallel scoped subagents; ordinary in-session LSP/MCP and recurring task commands.
- Recursion level: one operator-directed terminal coding session with bounded independently acting S1 children and first-party feedback/support mechanisms.
- Reviewed revision: `86aa7369bc775c583d46f8c3bb286c76d0401220`.
- Observation date: 2026-10-11.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

`Agent.submit` appends user request, iterates model/tool selection, dispatches read-only and spawned tasks concurrently while executing file-mutating commands in order, and returns tool results to subsequent model decisions. A configurable `task` tool instantiates separate constrained model-driven subagents; executable paths may perform code search, edits and shell commands. The `TaskTool` holds a shared `write_gate` for write-capable concurrent children, while a second global gate serializes different-model local Ollama child work to avoid VRAM thrashing. [crates/rocinante-core/src/agent/agent.rs](https://github.com/djynnius/rocinante/blob/86aa7369bc775c583d46f8c3bb286c76d0401220/crates/rocinante-core/src/agent/agent.rs); [crates/rocinante-core/src/agent/subagent.rs](https://github.com/djynnius/rocinante/blob/86aa7369bc775c583d46f8c3bb286c76d0401220/crates/rocinante-core/src/agent/subagent.rs).

The auto verifier is not merely a reviewer label: `Agent.submit` calls `iterate_verification` before TurnFinished for substantial tool work; a dedicated checker model compares the original ask/work/final report, and the optional trusted `check_command` provides a direct environment/test signal. Negative findings become a corrective input followed by another agent run, up to a configured bound. The checker fails open on model timeout/error; its positive claim is limited to constructor ownership and to configurations where independent command evidence is available. [crates/rocinante-core/src/verifier.rs](https://github.com/djynnius/rocinante/blob/86aa7369bc775c583d46f8c3bb286c76d0401220/crates/rocinante-core/src/verifier.rs); [crates/rocinante-core/src/agent/agent.rs](https://github.com/djynnius/rocinante/blob/86aa7369bc775c583d46f8c3bb286c76d0401220/crates/rocinante-core/src/agent/agent.rs).

The optional learning mode uses a separate model request over user-correction transcripts to extract durable cross-project preference/rule changes into `LESSONS.md`; subsequent CLI setups inject them into the active system prompt. This creates a future-facing adaptation constructor, but the operator selects cadence and enablement, so it is not credited as agent-owned prospective strategic intelligence. [crates/rocinante-core/src/lessons.rs](https://github.com/djynnius/rocinante/blob/86aa7369bc775c583d46f8c3bb286c76d0401220/crates/rocinante-core/src/lessons.rs); [crates/rocinante-cli/src/setup.rs](https://github.com/djynnius/rocinante/blob/86aa7369bc775c583d46f8c3bb286c76d0401220/crates/rocinante-cli/src/setup.rs); [crates/rocinante-core/src/prompt/mod.rs](https://github.com/djynnius/rocinante/blob/86aa7369bc775c583d46f8c3bb286c76d0401220/crates/rocinante-core/src/prompt/mod.rs).

## Operational model

Root actor selects coding actions and subagent goals. Independent task children can act in parallel, but shared write operations and contested local model memory are serialized by deterministic gates. A verifier samples the completed coding claim and optional real check results, then re-enters the operating loop with specific remediation when gaps occur. External user correction may be distilled into durable rules for subsequent sessions. None of these alone confers a legitimate whole-system S3 manager or ultimate S5 policy authority.

## S1 — Operations

- State: A
- Function: first-party goal-directed coding, source inspection, shell operations and bounded delegated task execution.
- Disturbance / variety regulated: changing source, errors, test results, local tools and task intent.
- Decisive decision or feedback right: choose next model/tool operation using returned observations; task subagents choose scoped actions.
- Decision owner: model-driven root `Agent`, or a bounded child for its own delegated S1 work.
- Supporting / enforcement mechanisms: tool registry, permission engine, LSP/MCP providers, context compaction, output-repair and cancellation.
- Closure path: tool use → first-party execution → result appended → model selects next tool/response.
- Boundary reachability: `rocinante-cli` setup wires the model, tools and agent for the shipped terminal modes.
- Why this is / is not agent-owned: model actors make discretionary task-specific decisions; kernel dispatch alone cannot choose the work.
- Evidence: [crates/rocinante-core/src/agent/agent.rs](https://github.com/djynnius/rocinante/blob/86aa7369bc775c583d46f8c3bb286c76d0401220/crates/rocinante-core/src/agent/agent.rs); [crates/rocinante-cli/src/setup.rs](https://github.com/djynnius/rocinante/blob/86aa7369bc775c583d46f8c3bb286c76d0401220/crates/rocinante-cli/src/setup.rs); [crates/rocinante-core/src/tools/registry.rs](https://github.com/djynnius/rocinante/blob/86aa7369bc775c583d46f8c3bb286c76d0401220/crates/rocinante-core/src/tools/registry.rs).
- Basis: structural.
- Confidence: high.
- Caveats: no behavioral benchmark is inferred from static source.

## S2 — Coordination

- State: C
- Function: attenuate explicit conflicts between concurrent independent coding S1 children, particularly competing mutations of one shared git worktree and local model VRAM contention.
- Distinct S1 units: `TaskTool` children instantiate independent `Agent` loops with their own prompts/model profiles and bounded task objectives.
- Inter-S1 disturbance: two spawned write-capable child agents may edit or shell-mutate the same workspace; different large local Ollama child model sessions may thrash constrained GPU memory.
- Attenuating coordination relation: `TaskTool::run` holds a shared `write_gate` mutex across any write-capable child task, while allowing read-only children to execute in parallel; `LocalModelGate` serializes different-model local children for the duration of their run.
- Feedback into subsequent S1 behaviour: contenders await gate release, then proceed with a nonoverlapping editing/model-compute window; their results and progress return via the task tool/event channel to the parent for further task work.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: named concrete child-child worktree write collision and local-model residency interference are prevented by mutex admission boundaries for distinct model-driven S1 children; this is not merely moving tasks or messages.
- Disturbance / variety regulated: concurrent child write and VRAM-resource contention.
- Decisive decision or feedback right: choose execution admission order for conflicting child work based on scoped child profile/capabilities and resource locality.
- Decision owner: deterministic runtime mutex gates, not an autonomous mediator model; therefore constructor class C.
- Supporting / enforcement mechanisms: per-TaskTool shared mutexes, resolved model selection, concurrent tool dispatcher, child task/event channel.
- Closure path: competing tasks → write/model resource classification → await exclusive gate → child execution → release and subsequent child run/result.
- Boundary reachability: shipped `rocinante-cli` registers `TaskTool`; concurrency and gating work when relevant child profiles are configured.
- Why this is / is not agent-owned: the model can ask for delegation but the mutex conflict response does not depend on a model judging resource tradeoffs.
- Evidence: [crates/rocinante-core/src/agent/subagent.rs](https://github.com/djynnius/rocinante/blob/86aa7369bc775c583d46f8c3bb286c76d0401220/crates/rocinante-core/src/agent/subagent.rs); [crates/rocinante-core/src/agent/agent.rs](https://github.com/djynnius/rocinante/blob/86aa7369bc775c583d46f8c3bb286c76d0401220/crates/rocinante-core/src/agent/agent.rs); [crates/rocinante-cli/src/setup.rs](https://github.com/djynnius/rocinante/blob/86aa7369bc775c583d46f8c3bb286c76d0401220/crates/rocinante-cli/src/setup.rs).
- Basis: structural.
- Confidence: high for gate existence, medium for measured effectiveness.
- Caveats: serialization avoids concurrent mutation but does not eliminate semantic edit conflicts after the fact; no autonomous S2=A claim.

## S3 — Inside-and-now control

- State: —
- Function: no separately owned whole-current supervisor over shared current operating commitments and resources.
- Disturbance / variety regulated: permissions, budget, progress, cancellation, verifier failures and memory windows.
- Decisive decision or feedback right: root coding model chooses task steps and human/operator sets configuration; deterministic guards and verifier retry limit act on local task closure.
- Decision owner: root S1 actor for work, constructor for gates; no evidenced higher current-control arbiter.
- Supporting / enforcement mechanisms: execution mode, status and model configuration, permission router, S2 mutexes, verifier, context compactor and memory.
- Closure path: local tool/child control or verifier correction returns to task; no separately managed whole-session multiunit commitment reallocation feedback.
- Why this is / is not agent-owned: mixing S2 serialization, S3* correctness verification and task-agent planning does not create whole-current management by aggregation.
- Evidence: [crates/rocinante-core/src/agent/agent.rs](https://github.com/djynnius/rocinante/blob/86aa7369bc775c583d46f8c3bb286c76d0401220/crates/rocinante-core/src/agent/agent.rs); [crates/rocinante-core/src/config/schema.rs](https://github.com/djynnius/rocinante/blob/86aa7369bc775c583d46f8c3bb286c76d0401220/crates/rocinante-core/src/config/schema.rs); [crates/rocinante-core/src/permissions/engine.rs](https://github.com/djynnius/rocinante/blob/86aa7369bc775c583d46f8c3bb286c76d0401220/crates/rocinante-core/src/permissions/engine.rs).
- Basis: structural.
- Confidence: medium-high.
- Caveats: operator might supervise multiple sessions externally.

### Absence scope

- Surfaces inspected: CLI setup/modes, root Agent task loop and child hierarchy, budget/permission routing, verifier, LSP/MCP support, local S2 mutexes.
- Plausible first-party paths checked: child progress/status, model selection, VRAM coordination, S3* remediation retry, task cancellation and background memory.
- Why no material first-party path remains: no distinct whole-current owner with shared operating view, authoritative inter-unit priority/resource decision and returned supervisory closure is established.

## S3* — Complementary audit

- State: C
- Claim being audited: a producing coding turn has satisfied the original user request and its claimed file/test changes work as reported.
- Ordinary reporting path: root coding model's final_text and own tool-action work_summary, which alone could contain mistaken success assertions.
- Complementary access path: a separately invoked Verifier model compares original ask/work summary/output and, in the configured check-command mode, first-party code runs a trusted build/test command directly against the real workspace, overriding positive text-only judgments on failure.
- Independence boundary: verifier is a distinct invocation and independent direct test source in the optional check-command mode, but shares a first-party runtime/provider configuration and can fail open if the model/checker is unavailable; no external independent auditor is claimed.
- Who acts on findings: Agent::iterate_verification issues the findings as a corrective_prompt into the producing Agent, reruns its coding loop and calls Verifier::check again up to max_iterations, then emits a residual-failure report.
- Function: source-independent-in-principle configured checker/test corroboration of the task's claimed completion with consequential corrective return.
- Disturbance / variety regulated: erroneous coding completion claims, missed compilation/test failures and unfulfilled user requirements.
- Decisive decision or feedback right: after actual tool work, dedicated verifier model judges the user's original ask vs result/work summary; when configured, a direct trusted check command runs against real workspace and **overrides** model optimism on failure.
- Decision owner: first-party verifier constructor, operated by its own model invocation plus deterministic direct test-command override. It is distinct from producing run but not an organizationally independent human auditor.
- Supporting / enforcement mechanisms: automatic `Verifier::check`, configured trusted test/build command, bounded max_iterations, verifier events and corrective prompts.
- Closure path: completed work → independent checker/test evidence → concrete findings → `corrective_prompt` to root → root rerun → checker rerun (or bounded residual failure).
- Boundary reachability: `setup.rs` wires verifier when enabled; `verification.enabled/auto` default true; `check_command` optional and must be trusted/configured. Positive C is bounded to that optional evidence-bearing configuration.
- Why this is / is not agent-owned: checker is not an independently authorized audit organization with independent source collection by default; constructor runs tests and feeds findings, hence C, not A. On model timeout checker fails open and cannot be credited as universal audit assurance.
- Evidence: [crates/rocinante-core/src/agent/agent.rs](https://github.com/djynnius/rocinante/blob/86aa7369bc775c583d46f8c3bb286c76d0401220/crates/rocinante-core/src/agent/agent.rs); [crates/rocinante-core/src/verifier.rs](https://github.com/djynnius/rocinante/blob/86aa7369bc775c583d46f8c3bb286c76d0401220/crates/rocinante-core/src/verifier.rs); [crates/rocinante-cli/src/setup.rs](https://github.com/djynnius/rocinante/blob/86aa7369bc775c583d46f8c3bb286c76d0401220/crates/rocinante-cli/src/setup.rs); [crates/rocinante-core/src/config/schema.rs](https://github.com/djynnius/rocinante/blob/86aa7369bc775c583d46f8c3bb286c76d0401220/crates/rocinante-core/src/config/schema.rs).
- Basis: structural.
- Confidence: medium for constructor audit closure with a trusted check command, low for universal correctness guarantees.
- Caveats: model-only path sees self-reported work summary and has permissive OK bias; absent trusted independent check evidence would not justify S3* closure. This is a shipped opt-in constructor, not a universal deployment-mode guarantee.

## S4 — Outside-and-then intelligence

- State: C
- External distinction: observed *user*-originated corrections/repeated complaints reflect preference and behavioral variety originating beyond the coding agent's own report, not its static task memory.
- Future / prospective distinction: Lessons capture requests rules for how this user wants the agent to behave across future projects/sessions; a separate model extracts only generalizable do/don't changes, rather than planning today's tool actions.
- Path back into current capability / S3: the model-curated LESSONS.md is loaded by the shipped CLI setup and injected into the active future system prompt, changing operational behavior under user governance; this is constructor-based adaptation and does not prove S3 ownership.
- Function: encode external user corrections into durable cross-session future operating-behavior rules and activate those rules as future session context.
- External / future distinction: actual user corrections and repeated complaints about response behavior are external environment signals about future preferences, not current repository content. Learned rules explicitly target all subsequent projects/sessions.
- Adaptation option generated: separate low-temperature model job conservatively extracts reusable global rules/preferences from interaction transcript and merges into `LESSONS.md`.
- Path back into current capability: first-party CLI setup loads the learned file and prepends globally binding rules to later agent system prompts, changing their subsequent task behavior; the current running model's task decisions are distinct from a durable configuration constructor.
- Disturbance / variety regulated: changes in recurring user preferences, repeated corrected behavior and cross-project process assumptions.
- Decisive decision or feedback right: retain/adapt a general rule from a source-constrained transcript, using model extraction gated by deterministic update cadence and sanitization.
- Decision owner: automatically dispatched model-driven `Lessons` capture constructor rather than autonomous S4 strategic planning authority; C is bounded to enabled `[learning]` config and later CLI prompt loading.
- Supporting / enforcement mechanisms: `Lessons::note_turn`, background capture, `LESSONS.md` atomic storage and `prompt::lessons_section`.
- Closure path: user correction → model-curated lesson → durable global file → subsequent CLI injected prompt → changed future operational rules.
- Boundary reachability: `setup.rs` registers this component when `learning.enabled`; no external CI or maintainer commit required.
- Why this is / is not agent-owned: output synthesis is model-backed but the adaptation *policy* is a fixed signal-filter/store/inject pipeline rather than independently directed prospective intelligence; no A promotion.
- Evidence: [crates/rocinante-core/src/lessons.rs](https://github.com/djynnius/rocinante/blob/86aa7369bc775c583d46f8c3bb286c76d0401220/crates/rocinante-core/src/lessons.rs); [crates/rocinante-core/src/prompt/mod.rs](https://github.com/djynnius/rocinante/blob/86aa7369bc775c583d46f8c3bb286c76d0401220/crates/rocinante-core/src/prompt/mod.rs); [crates/rocinante-cli/src/setup.rs](https://github.com/djynnius/rocinante/blob/86aa7369bc775c583d46f8c3bb286c76d0401220/crates/rocinante-cli/src/setup.rs); [crates/rocinante-core/src/agent/agent.rs](https://github.com/djynnius/rocinante/blob/86aa7369bc775c583d46f8c3bb286c76d0401220/crates/rocinante-core/src/agent/agent.rs).
- Basis: structural.
- Confidence: medium; positive C does not imply robust strategic environmental scanning.
- Caveats: conservative memory/rules learning can overlap S1 context retention. No S4 claim is made for mere compaction/BRAINBOX summary without the specific cross-session user-correction rule adaptation.

## S5 — Policy and identity

- State: —
- Function: no ultimate policy/identity deliberation and legitimate authority with binding returned decision at one terminal agent recursion.
- Disturbance / variety regulated: risky tool access, trust changes, child capabilities and user-wide preferences.
- Decisive decision or feedback right: operator approves tools and sets child profiles; automated lessons may adjust preferences but do not arbitrate ultimate organizational identity.
- Decision owner: external user/operator for top-level policy, deterministic permission engine for enforcement; no separate S5 owner.
- Supporting / enforcement mechanisms: user trust config, permission prompts, subagent tool allowlists and LESSONS preference injection.
- Closure path: permissions enforce individual tool boundaries; no identity-level issue → legitimate ultimate authority → policy return.
- Why this is / is not agent-owned: learned user instructions and static security policies are not an S5 governance channel simply because they influence behavior.
- Evidence: [crates/rocinante-core/src/config/trust.rs](https://github.com/djynnius/rocinante/blob/86aa7369bc775c583d46f8c3bb286c76d0401220/crates/rocinante-core/src/config/trust.rs); [crates/rocinante-core/src/permissions/engine.rs](https://github.com/djynnius/rocinante/blob/86aa7369bc775c583d46f8c3bb286c76d0401220/crates/rocinante-core/src/permissions/engine.rs); [crates/rocinante-core/src/prompt/mod.rs](https://github.com/djynnius/rocinante/blob/86aa7369bc775c583d46f8c3bb286c76d0401220/crates/rocinante-core/src/prompt/mod.rs).
- Basis: structural.
- Confidence: medium-high.
- Caveats: developer/OSS project governance belongs to a different recursion.

### Absence scope

- Surfaces inspected: permission/trust/configuration, user preferences, model/child routing and learning/verification setup.
- Plausible first-party paths checked: user policy overrides, global learned behavior rules, trusted test commands, child tool permissions and release self-update command.
- Why no material first-party path remains: no self-owned legitimate ultimate identity/policy dispute and binding authority feedback is wired into the operating organization.

## Recursion

Configured child agents own bounded separate model/tool decisions, but their goals/roles and rights come from the parent `TaskTool`, and they return results to it; nested capacity is not recursively viable S3/S4/S5 by assumption. [crates/rocinante-core/src/agent/subagent.rs](https://github.com/djynnius/rocinante/blob/86aa7369bc775c583d46f8c3bb286c76d0401220/crates/rocinante-core/src/agent/subagent.rs).

## Variety and escalation

Parallel write conflict is attenuated by mutex serialization; verifier failures generate an operational corrective turn and eventually a bounded residual-failure report. User preference corrections may affect later sessions through separate durable learned rules. Errors in verifier inference fail open and therefore no reliability guarantee is claimed.

## Evidence gaps

- Frozen source-only, without observed production transcripts, independent tester-run or measured benchmark performance.
- C for S3* explicitly relies on enabled trusted check-command verification and a source-wired returned corrective loop; the default model-only self-report checker is weaker and can fail open.
- C for S4 explicitly relies on enabled learned global-rule cross-session adaptation; normal historical memory and simple context compaction do not establish S4 by themselves.

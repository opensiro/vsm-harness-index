---
harness_id: multi-agent-orchestrator-rs
project_name: multi-agent-orchestrator-rs
repository: https://github.com/formiat/multi-agent-orchestrator-rs
review_ref: ea6c114a40c005256d125984b3d77cc758bdc8fe
reviewed_at: 2026-10-20
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

# multi-agent-orchestrator-rs

## Review boundary

- System in focus: The first-party Rust two-agent coding-task orchestration system, `orchestrate` and companion `orchestrate-batch`, at one work-cell recursion. It integrates user-selected preexisting executor and independent reviewer AI-provider sessions.
- Purpose and identity: Deliver a given plan, investigation or implementation with independent review, revision loop, stopping rules and reproducible workspace reporting. Batch mode processes a human-supplied ordered file queue.
- Environment: Task request, target clean Git worktree, repository artifacts/commits/tests, authenticated Claude/OpenCode/Codex provider CLIs and sessions, optional Notion/GitLab/remote target access under user-selected policies, operator and subprocess environment.
- Standard-distribution boundary: Supported Rust binary/CLI invocation with explicitly bound distinct preexisting provider sessions; source-owned prompt templates and adapters; live target workspace via the tool; optional batch. Provider engine internals and the user's wider development organization are outside first-party software ownership, while called agent actors remain part of the configured *integration mode* being assessed.
- Credited operating / distribution surfaces: [src/main.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/main.rs); [src/orchestrator/mod.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/orchestrator/mod.rs); [src/fsm.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/fsm.rs); [src/orchestrator/phases/decision.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/orchestrator/phases/decision.rs); [src/orchestrator/phases/dispatch.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/orchestrator/phases/dispatch.rs); [src/orchestrator/phases/output.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/orchestrator/phases/output.rs); [src/orchestrator/monitor.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/orchestrator/monitor.rs); [src/workflow/executor.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/workflow/executor.rs); [src/workflow/reviewer.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/workflow/reviewer.rs); [src/providers/mod.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/providers/mod.rs); [src/sessions.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/sessions.rs); [src/yaml_check.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/yaml_check.rs); [src/transport.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/transport.rs); [crates/orchestrate-batch/src/lib.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/crates/orchestrate-batch/src/lib.rs); [crates/orchestrate-batch/src/queue.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/crates/orchestrate-batch/src/queue.rs).
- Adjacent first-party surfaces excluded from ownership: Project `CLAUDE.md`/`AGENTS.md` contributor instructions, Rust tests and test fixtures, build/Makefile, standalone Notion/GitLab protocol prose as external system governance, and a target repository's own organization. These can corroborate supported modes but do not supply VSM functions to this coding-workflow system.
- First-party operating / deployment modes considered: `investigate`, `plan`, `implement` direct workflows; Claude/OpenCode/Codex agent CLI provider pair with separately bound pre-existing sessions; independent reviewer loop and user-selected remote network/Notion constraints; optional numeric sequential batch plan→implement or implement-only; cancel/timeout/invalid protocol; no host-created provider sessions.
- Recursion level: One bounded coding-task operation (human request → agent executor → reviewer → revised result) and its repeatable sequential batch wrapper, not a multi-department self-managing software company.
- Reviewed revision: `formiat/multi-agent-orchestrator-rs@ea6c114a40c005256d125984b3d77cc758bdc8fe`, exact Git source tree `05fdae593edec697a04ef8536a2e61147046eea7`; public `main` nonfork/nonarchived, GitHub repo ID 1234061728, created `2026-05-09T17:43:59Z`.
- Observation date: 2026-10-20.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

The `orchestrate` executable is **deterministic Rust control around configured model-driven external provider sessions**. `src/cli.rs` requires a workspace, named executor/reviewer sessions and provider choices; preflight ensures relevant Git/policy/session invariants. `src/orchestrator/mod.rs` implements the RunState machine and context; phases dispatch provider-specific subprocesses, wait/inspect transport files and execution-state facts, parse and verify a reviewer YAML object, enforce mechanical quality/failure/termination limits, and pass semantic revision feedback to the executor. `src/workflow/executor.rs` and `src/workflow/reviewer.rs` embed operational prompts: the former produces task artifact or code and responds to feedback, while the latter checks changed files and actual workspace sources instead of trusting the executor. `src/orchestrator/phases/decision.rs` owns deterministic accept/revise/blocked branch selection from the reviewer's returned decision. `orchestrate-batch` opens ordered numeric tasks and runs plan/implementation phases sequentially, with a separate implement-only mode. [src/cli.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/cli.rs); [src/orchestrator/mod.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/orchestrator/mod.rs); [src/orchestrator/phases/dispatch.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/orchestrator/phases/dispatch.rs); [src/workflow/executor.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/workflow/executor.rs); [src/workflow/reviewer.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/workflow/reviewer.rs); [src/orchestrator/phases/decision.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/orchestrator/phases/decision.rs); [crates/orchestrate-batch/src/lib.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/crates/orchestrate-batch/src/lib.rs).

There is no first-party hosted model inference or independently managed provider-session creation. Agent autonomy is attributed to the **configured two-agent workflow mode reached through shipped templates and CLI adapters**, not falsely to Rust FSM code. Inference, provider authentication and actual task performance depend on external sessions; the source demonstrates a runnable integration contract, not empirical provider performance.

## Operational model

The work cell directly enacts one task. Executor owns task-specific reasoning and production, independent reviewer owns deliverable-quality judgment and corrective feedback, while deterministic Rust orchestrator enforces a bounded review/retry protocol and the human supplies permissible operating parameters. Reviewer independence is substantive at S1 quality-control scope; this does not establish S3* without evidence of auditing S3 managerial reports. A batch contains serial tasks rather than continuing separately viable S1 businesses. No persistent organizational management, policy adaptation or identity governance can be inferred from process state labels.

## S1 — Operations

- State: A
- Function: Per-request planning, investigation or implementation of software tasks, producing investigation/plan documents or local code changes with feedback-directed repair.
- Disturbance / variety regulated: Variable repository behavior, complex task requirements, defects, missing artifacts, regressions, rejected reviewer checks and uncertain provider session continuity.
- Decisive decision or feedback right: A configured external-provider executor agent reasons about the specific task, inspects the workspace and edits/commits or writes the required artifact; a separately bound reviewer agent independently examines actual changes, chooses an evidence-backed YAML accept/revise/blocked/disagreement decision and sends concrete improvement feedback. The first-party Rust gate only interprets structured decisions and deterministic conditions, and retries the executor on revise.
- Decision owner: The task-dependent choices and corrections are owned by the two configured AI agent sessions (Claude/OpenCode/Codex) under first-party prompt templates and provider dispatch in this distributed execution mode. The Rust orchestrator is the deterministic harness controller; the human supplies the prompt, target repo, model/provider options, session identities and network policies. These external provider tools are indispensable executors, not a first-party in-process model implementation.
- Supporting / enforcement mechanisms: Source-owned workflow templates, CLI input and session lock/binding, transport files and fingerprints, provider subprocess adapters, FSM monitor, reviewer YAML schema and quality gate, Git checks, retry cap, batch task-file queue.
- Closure path: CLI workspace/prompt and preexisting sessions → first-party context preparation + executor prompt → provider-session executor makes and reports task changes → first-party monitor/transport → independent reviewer-session checks code/files/tests → parsed review decision → Rust quality gate closes success or dispatches feedback into a later executor round. Batch mode repeats per queued task, not autonomously planning a new organization.
- Boundary reachability: Main binary invokes first-party orchestrator; current orchestrator phases dispatch the two supported provider sessions with owned templates and transport; accept/revise flow in quality gate terminates or re-enters executor dispatch. Batch binary invokes the same orchestration workflow for each task file.
- Why this is / is not agent-owned: Removing the configured agent sessions eliminates the discretionary investigation/coding and semantic review; Rust cannot invent equivalent task-specific plans, code or critique. Conversely removing the Rust FSM leaves uncoordinated provider sessions without shipped restart/review-contract/gate behavior. Agent discretion is first-party *integrated* at the supported runtime boundary, not Rust inference.
- Evidence: [README.md](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/README.md); [src/main.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/main.rs); [src/orchestrator/mod.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/orchestrator/mod.rs); [src/workflow/executor.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/workflow/executor.rs); [src/workflow/reviewer.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/workflow/reviewer.rs); [src/orchestrator/phases/dispatch.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/orchestrator/phases/dispatch.rs); [src/orchestrator/phases/output.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/orchestrator/phases/output.rs); [src/orchestrator/phases/decision.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/orchestrator/phases/decision.rs); [crates/orchestrate-batch/src/lib.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/crates/orchestrate-batch/src/lib.rs); [src/providers/mod.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/providers/mod.rs); [src/yaml_check.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/yaml_check.rs)
- Basis: explicit and structural — executable prompt/dispatch/review/feedback chain
- Confidence: High for source-wired agentic S1; provider session runtime effects not live-tested.
- Caveats: Requires two separate existing authenticated provider sessions, CLI binaries and an appropriate clean Git worktree. No provider inference or real target modifications were performed; the repo's documented behavior and first-party integration code, not measured output quality, ground this result.

## S2 — Coordination

- State: —
- Function: No sustained coordination function shown that attenuates *actual inter-S1 oscillation or mutual disturbance* among multiple independently viable operational units.
- Disturbance / variety regulated: An executor may miss a requirement and reviewer may request revisions; batches contain several sequential software tasks.
- Decisive decision or feedback right: Reviewer feedback governs acceptance/revision for the same coding task, not mutual operating interference between separate viable S1 departments. Sequential batch runner selects the next numbered task after completion but does not maintain interdependent S1 mutual constraints.
- Decision owner: Reviewer session owns a task-local judgment; Rust quality gate routes retry and the queue determines sequence. No distinct S2 variety-attenuating owner between viable units.
- Supporting / enforcement mechanisms: Role separation and transport protocol, review YAML accept/revise contract, fixed FSM, sequential batch task processing, per-session locks.
- Closure path: Executor work → reviewer feedback → same executor's corrective next round → terminal result; not S1-A disturbance → S2 negotiation/coordination → modified concurrent S1-B and S1-A behavior.
- Why this is / is not agent-owned: Executor and reviewer are asymmetric production and quality-control roles in one work cell. Review is not coordination of two ongoing independently viable systems. Multiple queue entries are tasks rather than independently operating environmental departments.
- Evidence: [src/workflow/reviewer.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/workflow/reviewer.rs); [src/workflow/executor.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/workflow/executor.rs); [src/orchestrator/phases/decision.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/orchestrator/phases/decision.rs); [crates/orchestrate-batch/src/lib.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/crates/orchestrate-batch/src/lib.rs); [crates/orchestrate-batch/src/queue.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/crates/orchestrate-batch/src/queue.rs); [src/orchestrator/mod.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/orchestrator/mod.rs)
- Basis: bounded negative with positive task-coordination hypothesis checked
- Confidence: High at bounded coding-workflow recursion.
- Caveats: Teams running several instances could externally coordinate across products, but no shipped cross-instance organizational S2/feedback loop is assessed.

### Absence scope

- Surfaces inspected: CLI direct agent workflow, phase dispatcher/gate, reviewer and executor prompts, batch task loop and locks.
- Plausible first-party paths checked: Checked agent-to-agent review as S2, independent viability and recurring external environment of executor/reviewer, and batch sequencing as possible coordination of multiple S1s.
- Why no material first-party path remains: Both agent roles contribute to one bounded task outcome; the batch runner serializes tasks rather than regulating their inter-unit reciprocal interference, and no S2 owner/feedback relation among autonomous continuing S1s is shipped.

## S3 — Inside-and-now management

- State: —
- Function: No separately justified whole-system present management of continuing viable operational units and binding cross-unit resources/commitments.
- Disturbance / variety regulated: Provider hangs, malformed YAML, dirty worktree, regressions, policy violations and failed task deliveries.
- Decisive decision or feedback right: Rust decides state transitions/retries, scoring thresholds, termination, no-progress caps, and error reporting from a fixed configuration. Reviewer decides if one task is acceptable. Human selects CLI constraints before running; no actor evaluates and directs whole-current multi-unit production/resource/accountability trade-offs.
- Decision owner: Task reviewer agent for bounded product gate, deterministic Rust FSM for mechanical retry/failure and user for input policies. None is shown exercising the organizational S3 management right.
- Supporting / enforcement mechanisms: FSM run states, monitoring/probe diagnostics, reviewer schema/quality score, session locks, workspace clean preflight, provider options and network policy.
- Closure path: One task/reviewer output → deterministic gate/retry/failure → same task executor or terminal JSON; no plural operational-unit management returns with allocations or policy reconciliations.
- Why this is / is not agent-owned: A quality gate over one deliverable is not whole-current S3 merely because it blocks acceptance. Network policies and retry thresholds originate outside the agent, and code enforces rather than autonomously decides organization-wide management.
- Evidence: [src/orchestrator/mod.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/orchestrator/mod.rs); [src/orchestrator/phases/decision.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/orchestrator/phases/decision.rs); [src/fsm.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/fsm.rs); [src/state.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/state.rs); [src/orchestrator/phases/preflight.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/orchestrator/phases/preflight.rs); [src/cli.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/cli.rs); [src/orchestrator/monitor.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/orchestrator/monitor.rs); [crates/orchestrate-batch/src/lib.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/crates/orchestrate-batch/src/lib.rs)
- Basis: bounded negative after model, deterministic and human paths
- Confidence: High.
- Caveats: An operator could use the tool inside a multi-team organization, but that parent's present resource-management authority is not wired as an assessed first-party mode.

### Absence scope

- Surfaces inspected: First-party orchestrator context/run-state/gate, provider monitor, task batch loop, configuration and user-policy inputs.
- Plausible first-party paths checked: Checked whether reviewer acceptance is S3 managerial audit/intervention, whether Rust quality gate owns discretionary current commitments, whether a batch controls independent S1 businesses, and any returned parent governance.
- Why no material first-party path remains: Everything is bounded to one executor/reviewer task or sequential queue progress; no continuing cross-operational-unit resource/accountability decisions and binding corrective-management return are shipped.

## S3* — Complementary audit

- State: —
- Function: No distinct complementary investigation of an S3 management view or its executive claims against unfiltered operational reality with corrective return.
- Disturbance / variety regulated: Executor self-report may misstate implementation quality, omit changed files, hide regressions or violate policies.
- Decisive decision or feedback right: The separately bound reviewer is explicitly required to inspect workspace artifacts, code, diffs and risks independently and issue revise/accept/block decisions. This is strong *task-level* quality verification, but it samples executor output, not claims in a distinct organizational S3 present-management account.
- Decision owner: Independent reviewer agent owns a real S1 quality-review decision. The deterministic gate applies it to the same work item; no S3* mandate/recipient at the current whole-system management recursion.
- Supporting / enforcement mechanisms: Reviewer prompts with no-trust requirement, workspace/commit checks, YAML structured findings, review repair and procedural error gates.
- Closure path: Executor artifact and claims → independent reviewer evidence → YAML judgment → executor correction / terminal; not S3 management self-report → independently sampled unit reality → corrective report into continuing S3 controls.
- Why this is / is not agent-owned: Do not discard a real independent reviewer: its audit-like behavior is positive evidence for robust S1 control. Its measured object, decision scope, and corrective recipient remain task delivery, not S3 managerial communications or an independent S3* audit function.
- Evidence: [src/workflow/reviewer.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/workflow/reviewer.rs); [src/workflow/executor.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/workflow/executor.rs); [src/yaml_check.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/yaml_check.rs); [src/orchestrator/phases/output.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/orchestrator/phases/output.rs); [src/orchestrator/phases/decision.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/orchestrator/phases/decision.rs); [src/orchestrator/mod.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/orchestrator/mod.rs)
- Basis: explicit source evidence of task verification, negative S3* function adjudication
- Confidence: High with fixed recursion and current management assessment.
- Caveats: One could change the boundary or introduce a manager whose reports are audited; no such parent pathway exists as shipped code.

### Absence scope

- Surfaces inspected: Whole reviewer prompt, code/diff/requirements verification contract, emitted YAML fields, FSM review-result handling and report projection.
- Plausible first-party paths checked: Tested strongest plausible S3* path: reviewer checks primary workspace evidence independently and returns corrective feedback; specifically traced whether its target is a distinct S3 management account and whether the feedback closes S3 organizational correction.
- Why no material first-party path remains: The target is the executor's one task outcome, and revise returns to that same executor. No first-party ongoing S3 managerial account, complementary-management sampling mandate or corrective return to S3 exists.

## S4 — Outside-and-then intelligence

- State: —
- Function: No continuing future-environment intelligence with accepted strategic change to the organization’s capability or policies.
- Disturbance / variety regulated: Unknown technical constraints may emerge in investigations; provider models may vary, external Git/Notion/remote systems may change.
- Decisive decision or feedback right: An executor can research and create an investigation or implementation plan **for the current user-supplied task**. Model override, provider selection, network policy and prompt/workflow type are operator inputs; neither S4 agent nor parent accepts a strategy governing future work of the whole system.
- Decision owner: Configured executor model for immediate task analysis and user/developer for CLI/provider policy; no standing outward/future strategy owner.
- Supporting / enforcement mechanisms: Investigate and plan workflow types, provider CLI adapters, project profiles, Notion/remote access protocols, task wrappers and current workspace discovery.
- Closure path: Current request → case investigation/PLAN.md → reviewer quality feedback → file artifact/implementation. No outside trends → future strategic options → legitimate acceptance → changed future ongoing organizational operating capability.
- Why this is / is not agent-owned: The words 'plan', 'investigate', and 'research' can denote future thinking about a software change but refer to scoped S1 user work, not the viable organization's environmental strategy and accepted renewal.
- Evidence: [src/workflow/executor.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/workflow/executor.rs); [src/workflow/reviewer.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/workflow/reviewer.rs); [src/cli.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/cli.rs); [crates/orchestrate-batch/src/lib.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/crates/orchestrate-batch/src/lib.rs); [src/orchestrator/phases/preflight.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/orchestrator/phases/preflight.rs); [README.md](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/README.md)
- Basis: bounded negative with task research positive hypothesis evaluated
- Confidence: High.
- Caveats: Outputs may inform human strategic decisions externally; no first-party S4 acceptance/return is provided.

### Absence scope

- Surfaces inspected: All three direct workflow types, batch plan/implementation loop, provider model/config options and project profiles.
- Plausible first-party paths checked: Checked whether investigation/PLAN.md becomes standing environment sensing and organizational strategic decision, plus model/parent acceptance of future capability-policy changes.
- Why no material first-party path remains: All forecasts and planning are deliverables of a user-defined current software task; no persistent outside/then opportunity-control, strategy acceptance or return changing the harness organization is shipped.

## S5 — Policy and identity

- State: —
- Function: No ultimate organizational identity/purpose-policy determination or legitimate parent adjudication/return loop.
- Disturbance / variety regulated: Conflicting user requirements, provider selection, remote network safety, quality thresholds, blocked/irreconcilable reviewer outcomes.
- Decisive decision or feedback right: External operator sets workflow, providers, sessions and remote network policy. Static Rust/embedded prompts enforce no-forbidden remote actions, reviewer acceptance rules, hard-block stopping and manual next-action reporting; no actor decides the organization's enduring constitutional purposes and returns revised identity policy into execution.
- Decision owner: External human/developer for configuration/policy input; deterministic runtime enforces it and reviewer rejects violations. No first-party S5 agent or legitimate parent identity-policy role.
- Supporting / enforcement mechanisms: CLI flags, remote-network policy enum, baked-in reviewer instructions and quality thresholds, session locks, safety gates and terminal error reporting.
- Closure path: Operator-provided constraints → task-level enforcement/stop or reviewer verdict → terminal report for operator; no ultimate identity issue → valid top authority resolves enduring purpose → adopted constitutional policy changes subsequent system operation.
- Why this is / is not agent-owned: A strong deterministic permission check, a quality standard, a disagreement outcome and an external operator do not by themselves form S5; they lack the ultimate-policy object/authority/closure.
- Evidence: [src/cli.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/cli.rs); [src/workflow/reviewer.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/workflow/reviewer.rs); [src/workflow/executor.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/workflow/executor.rs); [src/orchestrator/phases/decision.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/orchestrator/phases/decision.rs); [src/orchestrator/mod.rs](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/src/orchestrator/mod.rs); [README.md](https://github.com/formiat/multi-agent-orchestrator-rs/blob/ea6c114a40c005256d125984b3d77cc758bdc8fe/README.md)
- Basis: bounded negative after parent-mode investigation
- Confidence: High.
- Caveats: The user can govern their own external organization, but it is not a first-party parent-governed constitutional mode of this released orchestrator.

### Absence scope

- Surfaces inspected: CLI/network/Notion policies, baked-in prompt constraints, quality/stop gates, human input/output route and batch automation.
- Plausible first-party paths checked: Checked S5-like safety policy, reviewer poisoned/blocked/irreconcilable outcome, operator authority and feedback from reported required next action.
- Why no material first-party path remains: They configure or constrain a single coding task and return terminal state; no binding ultimate identity/purpose-policy adjudication by a legitimate S5 owner and a subsequent governance change loop is provided.

## Distributed OSS parent arrangement

No parent viable organization or manager is supplied as a first-party active runtime. The CLI user supplies the target, provider policy, session names and prompt and may cancel/restart outside the system; these are configuration and task ownership, not evidenced S3/S4/S5 parent cycles. Provider accounts may have their own restrictions, but their internal policies belong to external systems.

## Self-hosted and non-human modes

The compiled binaries operate within a user-controlled workspace, invoking preexisting provider CLI sessions. The executor/reviewer may be the same model provider or different providers, but bindings must resolve to **distinct** provider-session identities. No autonomous self-provision of those external sessions, inter-instance global control or S5 parent delegation is demonstrated. Batch automation changes repetition and phase sequencing, not the assessed organizational recursion.

## Recursion

One coding/research/implementation work cell with QA in its own feedback path. Distinct role assignments, separate session state and independent verification are *within* an operation and do not convert executor and reviewer into two enduring independently viable S1 departments. Sequential numeric batch tasks do not imply separate viable S1 systems.

## Variety and escalation

Provider hangs, errors, invalid YAML, poisoned sessions, permission failures, cancellation, reviews requiring changes and no-progress limits enter the fixed RunState classification/monitor path and may trigger retry, stop, feedback or an operator-facing terminal reason. Those runtime status channels and reviewer quality controls handle immediate work, not a demonstrated organizational algedonic path or future-identity steering.

## Evidence gaps

Evidence is code/document review of frozen first-party Rust distribution and supported external-provider integration. No real provider sessions supplied, no agent inference executed, no target-workspace mutation performed, and no actual quality/completion benchmark measured. Compiler/toolchain availability should be reported separately from this semantic assessment. No concrete unresolved shipped parent-governed S3/S4/S5 return path, S3 manager-account audit pathway, or ongoing cross-S1 S2 coordination pathway was left open by the inspected implementation.

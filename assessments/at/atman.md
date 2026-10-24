---
harness_id: atman
project_name: Atman
repository: https://github.com/W-Mai/atman
review_ref: 56933fc40e38ccb5575cbfdda341d86a449643ac
reviewed_at: 2026-10-16
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Atman

## Review boundary

- System in focus: the first-party Atman Rust `.at` flow interpreter and its **shipped managed agent** and subagent templates, at frozen `56933fc40e38ccb5575cbfdda341d86a449643ac`; installed CLI/TUI/daemon executing native flow source and child runtimes.
- Purpose and identity: run model-directed coding tasks as explicit, reproducible DSL flows with typed tool and event traces, distinct task delegates, optional worktree isolation and bounded completion checking.
- Relevant environment: local repository/worktree, parent user task, selected model providers, primary/child flow sessions, event/task registry, current active-flow inventory, result transcript and tool feedback.
- Standard-distribution boundary: built-in `agent.at`/ `subagent.at` and associated prompt templates from `crates/atman-runtime/src/templates.rs`, first-party `atman-runtime` tool dispatch and `atman-cli`, flow registry, child workspace service, final-disposition classification, native tools and user-approval surfaces. External model providers, custom flow packages or maintained OSS project governance are excluded.
- Credited operating / distribution surfaces: shipped `atman init` managed agent template and supporting CLI/TUI route, `llm.call` with file/shell/git tool dispatch and results, available first-party `flow.instances/spawn/status/output/kill` control tools, built-in `verify_loop` child role, model-based final-answer classification, and **optional** `flow.spawn(workspace:"auto"/"retain")` managed per-child worktree isolation. The worktree feature is not assumed enabled by default.
- Adjacent first-party surfaces excluded from ownership: externally authored `.at` flows, independent project CI, external coding-agent harnesses, published metrics, uncontrolled Git roots, provider/model reasoning quality and standalone example tests not used by a shipped flow.
- First-party operating / deployment modes considered: regular `atman init` managed coding flow and direct CLI agent; first-party spawned subagent flows; explicitly selected verify role and managed worktree child mode; separate final-answer classifier (shipped managed flow). No live model provider executions or actual conflict trials were run.
- Recursion level: one parent Atman coding organization with model-directed primary whole-flow controller and child first-party coder/research/verify flows. Positive S2/S3/S3* are tied to their specific available managed modes and evidence; the DSL interpreter in isolation is not itself an autonomous organization.
- Reviewed revision: `56933fc40e38ccb5575cbfdda341d86a449643ac` (Index frozen candidate #379).
- Observation date: 2026-10-16.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The packaged `.at` DSL interpreter executes explicit typed flows with `llm.call`, native tool dispatch, loops/branches and child subflows. The first-party **managed agent** supplied in `templates.rs` configures a model with code tools and separate child-flow management, reads recent confessions, continues on concrete tool outputs, and challenges candidate final responses through a distinct `llm.classify` call against current user objective and recent transcript ([crates/atman-runtime/src/templates.rs](https://github.com/W-Mai/atman/blob/56933fc40e38ccb5575cbfdda341d86a449643ac/crates/atman-runtime/src/templates.rs), [crates/atman-runtime/src/tools/llm_call.rs](https://github.com/W-Mai/atman/blob/56933fc40e38ccb5575cbfdda341d86a449643ac/crates/atman-runtime/src/tools/llm_call.rs), [crates/atman-runtime/src/executor.rs](https://github.com/W-Mai/atman/blob/56933fc40e38ccb5575cbfdda341d86a449643ac/crates/atman-runtime/src/executor.rs), [examples/agent.at](https://github.com/W-Mai/atman/blob/56933fc40e38ccb5575cbfdda341d86a449643ac/examples/agent.at)). Although the DSL makes orchestration deterministic at the interpreter level, the hosted model decides specific coding tools, edits and delegated task goals within that programmed loop, and first-party executor returns observations for further model decisions (S1).

Child `flow.spawn` is protected by a **single-use** token produced by `flow.instances` after a session-scoped live inventory; outdated tokens fail when inventory changes. The shipped managed system prompt instructs the model to observe existing work, reuse or kill redundant child flows and spawn specifically scoped research/implement/verify/review jobs. In this mode the primary model sees multiple S1 units and can choose which current subordinate commitments survive, begin, or change, applying decisions through `flow.spawn/status/output/kill/interject` and feeding results into later model rounds; this is separate whole-current S3 and not merely a generic subprocess loader ([crates/atman-runtime/src/tools/flow_list.rs](https://github.com/W-Mai/atman/blob/56933fc40e38ccb5575cbfdda341d86a449643ac/crates/atman-runtime/src/tools/flow_list.rs), [crates/atman-runtime/src/templates.rs](https://github.com/W-Mai/atman/blob/56933fc40e38ccb5575cbfdda341d86a449643ac/crates/atman-runtime/src/templates.rs), [crates/atman-runtime/src/task_registry.rs](https://github.com/W-Mai/atman/blob/56933fc40e38ccb5575cbfdda341d86a449643ac/crates/atman-runtime/src/task_registry.rs), [crates/atman-runtime/src/tools/agent_ctrl.rs](https://github.com/W-Mai/atman/blob/56933fc40e38ccb5575cbfdda341d86a449643ac/crates/atman-runtime/src/tools/agent_ctrl.rs)).

For parallel child tasks, `flow.spawn` optionally allocates a first-party Git worktree with `workspace: "auto"` or `"retain"`. `FlowWorkspaceService.allocate` derives an independent repository-bound execution root and binds child file/shell/Git tools to that workspace; cleanup preserves dirty work, and parent workdir is not rewritten. This attenuates concrete concurrent child-file collision in a *supported configured mode*. The default `workspace:"none"` does not provide the S2 isolation benefit ([crates/atman-runtime/src/flow_workspace.rs](https://github.com/W-Mai/atman/blob/56933fc40e38ccb5575cbfdda341d86a449643ac/crates/atman-runtime/src/flow_workspace.rs), [crates/atman-runtime/src/git_workspace.rs](https://github.com/W-Mai/atman/blob/56933fc40e38ccb5575cbfdda341d86a449643ac/crates/atman-runtime/src/git_workspace.rs), [README.md](https://github.com/W-Mai/atman/blob/56933fc40e38ccb5575cbfdda341d86a449643ac/README.md)).

For complementary checking, the managed primary agent's **second model** uses `llm.classify` to challenge a candidate's completion from the original request, result and readback of recent transcript; a `continue_action/continue_work` finding forces re-entry rather than terminal success. This validates *claim-to-request progress*, not independent test correctness by itself. Separately the first-party shipped `subagent.at` role `verify` has its own independent model call, read-only source and test tools, and dedicated role prompt: it can independently inspect/build/test results from the workspace and report back as a specialized child. The parent flow can then apply its findings to further implementation. Positive S3* is strictly bounded to these source-proven completion and explicitly invoked verify paths, not a blanket guarantee that all completed code passed automated code review ([crates/atman-runtime/src/templates.rs](https://github.com/W-Mai/atman/blob/56933fc40e38ccb5575cbfdda341d86a449643ac/crates/atman-runtime/src/templates.rs), [crates/atman-runtime/src/tools/final_answer.rs](https://github.com/W-Mai/atman/blob/56933fc40e38ccb5575cbfdda341d86a449643ac/crates/atman-runtime/src/tools/final_answer.rs), [crates/atman-runtime/src/tools/llm_classify.rs](https://github.com/W-Mai/atman/blob/56933fc40e38ccb5575cbfdda341d86a449643ac/crates/atman-runtime/src/tools/llm_classify.rs), [crates/atman-runtime/src/tools/agent_ctrl.rs](https://github.com/W-Mai/atman/blob/56933fc40e38ccb5575cbfdda341d86a449643ac/crates/atman-runtime/src/tools/agent_ctrl.rs)).

The `memory.confess` and project-rules/store features carry task errors and durable hints across flows. They do not alone create a first-party environment/future sensing→capability option→changed runtime ability S4. Static DSL `contract.scope`, bound user confirmation for specific spec revisions, and tool capability sandbox protect authorization and scope but do not constitute an ultimate-identity S5 decision organ.

## Operational model

The user launches Atman's managed flow on a coding request. The primary model chooses task-specific local tools and can delegate work to separate first-party child models, reviewing the live inventory first. If the user or configured flow requests managed worktrees, child work runs in isolated Git roots; task results return to parent after completion. The primary model can decide to cancel or redirect child commitments based on runtime status and output; the managed completion classifier challenges premature final responses, and optional dedicated verify child agents inspect evidence and give findings for correction. These are installed native paths, not empirical claims about model correctness on a particular repo.

## S1 — Operations

- State: A
- Function: model-directed code work within programmed `.at` agent flow, with tool/result feedback.
- Disturbance / variety regulated: unknown files, failures in shell/test/edit commands, incomplete tasks and differing child work outcomes.
- Decisive decision or feedback right: choose native tools and code edits or next model goal in response to prior tool results, within typed flow permissions.
- Decision owner: first-party managed Atman model-directed coding actor operating through `llm.call` and `dispatch_all`; the `.at` script defines bounds rather than individual tool choices.
- Supporting / enforcement mechanisms: managed `AGENT_AT`, flow executor, `llm.call`, tool dispatch, session messages, native Git/fs/shell tools.
- Closure path: user task→`llm.call`→model-selected tools→`dispatch_all` executes→`session.push` feedback→subsequent model/tool choice or finished response.
- Boundary reachability: `atman init` installs native managed flow; CLI/TUI default route and `atman run` can execute it.
- Why this is / is not agent-owned: the model chooses concrete coding operations and adapts to observed tool results; full .at control-flow ownership is deterministic but does not eliminate adaptive S1.
- Evidence: [crates/atman-runtime/src/templates.rs](https://github.com/W-Mai/atman/blob/56933fc40e38ccb5575cbfdda341d86a449643ac/crates/atman-runtime/src/templates.rs), [crates/atman-runtime/src/executor.rs](https://github.com/W-Mai/atman/blob/56933fc40e38ccb5575cbfdda341d86a449643ac/crates/atman-runtime/src/executor.rs), [crates/atman-runtime/src/tools/llm_call.rs](https://github.com/W-Mai/atman/blob/56933fc40e38ccb5575cbfdda341d86a449643ac/crates/atman-runtime/src/tools/llm_call.rs), [README.md](https://github.com/W-Mai/atman/blob/56933fc40e38ccb5575cbfdda341d86a449643ac/README.md).
- Basis: first-party supported native model loop and tool feedback.
- Confidence: high for source-reachable operating path, no live task outcome test.
- Caveats: CLI/DSL custom flows without model-choice tools can be deterministic rather than S1=A; current assessment is for shipped managed agent mode.

## S2 — Coordination

- State: C
- Function: construct isolation that attenuates concrete shared-file write interference among separate coding child S1 actors.
- Disturbance / variety regulated: independent child flows writing overlapping files in the same parent checkout.
- Decisive decision or feedback right: allocate different Git worktrees for each child when `workspace:auto/retain` is requested, rejecting mismatched repository bindings and preserving separate result paths.
- Decision owner: first-party deterministic workspace constructor (`C`) under operator/parent requested workspace policy.
- Supporting / enforcement mechanisms: managed worktree service, per-child workspace id/lease, repository-root and owner validation, propagated child execution cwd and lifecycle finalization.
- Closure path: parallel child spawn with workspace policy→`FlowWorkspaceService.allocate` creates child-specific Git worktree→child fs/bash/git tools use isolated working directory→distinct result files and lifecycle return avoid concurrent writes to parent's checkout.
- Boundary reachability: native `flow.spawn` accepts workspace `auto`/`retain` in installed runtime, default `none` remains non-isolated.
- Why this is / is not agent-owned: deterministic first-party isolation changes the contested writable work domain, but model arbitration of semantic patch conflicts is not demonstrated.
- Distinct S1 units: separate first-party `subagent.at` implementer or other child coding flows spawned from a parent session.
- Inter-S1 disturbance: concurrent editing of identical files or commands in the same repository checkout by multiple independent children.
- Attenuating coordination relation: unique managed per-child worktrees and guarded workspace ownership isolate each writable Git checkout.
- Feedback into subsequent S1 behaviour: accepted children execute in distinct roots; invalid bindings fail instead of permitting conflicting edits to parent root; child outputs return with workspace scope.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: explicit per-child writable workspace isolation attenuates *inter-worker resource contention*, not just sequencing or status transport.
- Evidence: [crates/atman-runtime/src/flow_workspace.rs](https://github.com/W-Mai/atman/blob/56933fc40e38ccb5575cbfdda341d86a449643ac/crates/atman-runtime/src/flow_workspace.rs), [crates/atman-runtime/src/git_workspace.rs](https://github.com/W-Mai/atman/blob/56933fc40e38ccb5575cbfdda341d86a449643ac/crates/atman-runtime/src/git_workspace.rs), [README.md](https://github.com/W-Mai/atman/blob/56933fc40e38ccb5575cbfdda341d86a449643ac/README.md).
- Basis: supported optional first-party collision attenuator.
- Confidence: high for static worktree allocation, no concurrent live trial.
- Caveats: worktree policy is opt-in; it does not resolve merge conflicts across resulting patches.

## S3 — Inside-and-now control

- State: A
- Function: model-owned whole-current management of ongoing child coding and verification flows in managed agent mode.
- Disturbance / variety regulated: duplicate tasks, stalled or irrelevant child work, tasks needing reassignment, overall progress and running/background child status.
- Decisive decision or feedback right: inspect whole visible session's child population and decide which to spawn, reuse, kill, steer/interject or await, changing real execution commitments.
- Decision owner: first-party managed primary model invoking `flow.instances/status/output/spawn/kill/interject` as separate child-control tools; registry owns safe execution of its decisions.
- Supporting / enforcement mechanisms: session-scoped `FlowInstances` live inventory and one-use spawn token, model tool choices, native child registry, lifecycle/status and output, async watchers.
- Closure path: current worker inventory and task outputs→primary model interprets whole group→kills duplicate work, spawns new work with token or redirects active child→tool execution mutates live child state→updated inventory/results feed back to parent.
- Boundary reachability: `templates.rs` ships a managed agent with these exact exposed and recommended tools; first-party `flow.instances` and control actions are available when group exists, not hypothetical user-authored software.
- Why this is / is not agent-owned: model makes conditional whole-team current decisions from a live group view; unlike a fixed DSL stage list this changes commitments to address current work state. The same model can do S1 code work, but the child portfolio decision right is a differentiated metasystem function in the supported delegation mode.
- Whole-system current view: session-scope inventory of all visible spawned child handles, goal, status, model, run id, output and watchers, plus parent goal and prior task results.
- Current-control decision scope: choose child assignment and active/cancelled commitments, reuse current work, redirect or terminate a worker rather than merely issue own file actions.
- Evidence: [crates/atman-runtime/src/templates.rs](https://github.com/W-Mai/atman/blob/56933fc40e38ccb5575cbfdda341d86a449643ac/crates/atman-runtime/src/templates.rs), [crates/atman-runtime/src/tools/flow_list.rs](https://github.com/W-Mai/atman/blob/56933fc40e38ccb5575cbfdda341d86a449643ac/crates/atman-runtime/src/tools/flow_list.rs), [crates/atman-runtime/src/tools/agent_ctrl.rs](https://github.com/W-Mai/atman/blob/56933fc40e38ccb5575cbfdda341d86a449643ac/crates/atman-runtime/src/tools/agent_ctrl.rs), [crates/atman-runtime/src/task_registry.rs](https://github.com/W-Mai/atman/blob/56933fc40e38ccb5575cbfdda341d86a449643ac/crates/atman-runtime/src/task_registry.rs).
- Basis: built-in autonomous primary supervisor over subordinate first-party flows.
- Confidence: medium-high for supported path, dynamic decisions not live witnessed.
- Caveats: without spawned children, the ordinary agent loop does not expose a whole-team portfolio to regulate.

## S3* — Complementary audit

- State: A
- Function: challenge candidate completion using a distinct model-backed disposition judge and, in explicit verification mode, an independently tasked read/test child whose findings can drive correction.
- Disturbance / variety regulated: premature `final.answer`, candidate summaries omitting required work, unsupported completion claims and untested code modifications.
- Decisive decision or feedback right: judge completion relative to original request and recent transcript, trigger `continue_action`/`continue_work` instead of returning; in verify-child mode separately select file/read/test evidence actions and report independent findings.
- Decision owner: first-party separate `llm.classify` model invocation at managed agent handback, and optional first-party verify-role model actor on distinct child flow; parent receives findings for corrective coding.
- Supporting / enforcement mechanisms: `AGENT_AT` managed final-answer disposition schema, recent-turn evidence, answer origin, injected continuation directives, first-party `SUBAGENT_AT` verify_loop with restricted tools and separate session.
- Closure path: producer candidate final response→separate `llm.classify` checks request/transcript and emits disposition→negative continuation gate appends correction to live parent agent; optional verify child reads/tests repo directly→findings returned via flow output→parent implementation/decision.
- Boundary reachability: installed `atman init` managed agent **automatically** calls disposition judge for no-tool final candidates; dedicated verify-role subagent is shipped and model-callable but optional.
- Why this is / is not agent-owned: a distinct model invocation/child role, not the producer's self-claim, chooses whether reported work is sufficient; the first-party flow enforces re-entry. It does not automatically verify all code with a test suite.
- Claim being audited: user-request completion for a proposed final answer; optionally correctness of implementation as observed by dedicated verify child.
- Ordinary reporting path: producer model response with `final.answer`, tool transcript and running child work.
- Complementary access path: classifier gets independent `memory.recent_turns` evidence and original request, separate from candidate text; optional verify child can read source/Git diff and run tests in its own model/tool loop.
- Independence boundary: completion classifier is a separate model call with a role-specific category contract, not a producer statement; verify role is a separate first-party child run with read/test rights. Neither implies externally attested reviewer independence.
- Who acts on findings: managed flow directly blocks premature exit by injecting a continuation directive, and parent agent consumes child verification findings and may repair work before a later answer.
- Evidence: [crates/atman-runtime/src/templates.rs](https://github.com/W-Mai/atman/blob/56933fc40e38ccb5575cbfdda341d86a449643ac/crates/atman-runtime/src/templates.rs), [crates/atman-runtime/src/tools/llm_classify.rs](https://github.com/W-Mai/atman/blob/56933fc40e38ccb5575cbfdda341d86a449643ac/crates/atman-runtime/src/tools/llm_classify.rs), [crates/atman-runtime/src/tools/final_answer.rs](https://github.com/W-Mai/atman/blob/56933fc40e38ccb5575cbfdda341d86a449643ac/crates/atman-runtime/src/tools/final_answer.rs), [crates/atman-runtime/src/tools/agent_ctrl.rs](https://github.com/W-Mai/atman/blob/56933fc40e38ccb5575cbfdda341d86a449643ac/crates/atman-runtime/src/tools/agent_ctrl.rs).
- Basis: source-confirmed separate model judgment and binding narrow completion return; optional read/test evidence mode.
- Confidence: medium-high for configured first-party pathways.
- Caveats: classifier's evidence is a recent transcript excerpt, not an independent workspace check; stronger code-claim audit depends on explicitly spawning verify role. Absence of an observed live model decision is not hidden.

## S4 — Outside-and-then intelligence

- State: —
- Function: no separate external/future intelligence actor selecting and rolling out durable new capabilities from environmental evidence.
- Disturbance / variety regulated: task failures, stored confessions, rule changes and changing context are addressed through ordinary memory and coding control.
- Decisive decision or feedback right: detect outside/future change and decide a prospective installed capability adaptation with binding return into new operations; not established.
- Decision owner: developer/operator can edit .at flows or memory manually; no first-party prospective strategy-selection organ demonstrated.
- Supporting / enforcement mechanisms: `memory.confess`, rules, history, project goals, flow authoring and tool availability.
- Closure path: durable confessions inject corrective hints into current/future coding, but do not autonomously choose new tools/flows or govern future systemic capacity under a distinct owner.
- Why this is / is not agent-owned: remembering errors and allowing DSL editing are useful but not a genuine outside-and-then option→implementation cycle.
- Evidence: [crates/atman-runtime/src/memory/confession.rs](https://github.com/W-Mai/atman/blob/56933fc40e38ccb5575cbfdda341d86a449643ac/crates/atman-runtime/src/memory/confession.rs), [crates/atman-runtime/src/templates.rs](https://github.com/W-Mai/atman/blob/56933fc40e38ccb5575cbfdda341d86a449643ac/crates/atman-runtime/src/templates.rs), [crates/atman-runtime/src/flow_registry.rs](https://github.com/W-Mai/atman/blob/56933fc40e38ccb5575cbfdda341d86a449643ac/crates/atman-runtime/src/flow_registry.rs).
- Basis: bounded negative first-party source inspection.
- Confidence: medium.
- Caveats: user can construct S4 using external flow programs, which are not the credited standard distribution.

### Absence scope

- Surfaces inspected: built-in memory confessions, project rule loading, agent/subagent templates, flow registry and extension/configuration tools.
- Plausible first-party paths checked: long-lived project memory, rule fetch, history retrieval, configurable flows and model routes.
- Why no material first-party path remains: no first-party dedicated environmental hypothesis and future capability selection/adoption loop is evidenced beyond current work and user-supplied configuration.

## S5 — Identity and ultimate policy

- State: —
- Function: no ultimate identity/purpose interpretation organ with independent legitimate authority beyond user-defined task and runtime security policy.
- Disturbance / variety regulated: untrusted flows, unsupported permissions, scope changes and spec design uncertainty.
- Decisive decision or feedback right: adjudicate governing system identity and ultimate organizational purpose with binding decisions for S3/S4; not established.
- Decision owner: legitimate user authorizes specific spec designs, sandbox capabilities and commands; DSL enforces these bounds but does not independently decide organizational constitutional policy.
- Supporting / enforcement mechanisms: static flow `contract.scope` checking, capability sandbox, human `form.ask` with revision-bound approval receipts, TUI permissions and role prompts.
- Closure path: spec confirmation grants/denies exact design, tool permission allows or denies a call; neither establishes a rightful ultimate identity owner governing system ends.
- Why this is / is not agent-owned: narrow task approvals and exact-revision authorization are operating governance, not distinct S5 identity/purpose self-rule.
- Evidence: [crates/atman-runtime/src/approval.rs](https://github.com/W-Mai/atman/blob/56933fc40e38ccb5575cbfdda341d86a449643ac/crates/atman-runtime/src/approval.rs), [crates/atman-runtime/src/permission.rs](https://github.com/W-Mai/atman/blob/56933fc40e38ccb5575cbfdda341d86a449643ac/crates/atman-runtime/src/permission.rs), [crates/atman-runtime/src/templates.rs](https://github.com/W-Mai/atman/blob/56933fc40e38ccb5575cbfdda341d86a449643ac/crates/atman-runtime/src/templates.rs).
- Basis: bounded negative.
- Confidence: medium-high.
- Caveats: an adopting organization can supply external S5 policy and custom flows, outside this published harness's recursion.

### Absence scope

- Surfaces inspected: DSL flow contract, scoped tool permissions, approval receipts and spec workflow, managed model instruction roles.
- Plausible first-party paths checked: revision-bound design approval, prompt/role definitions, package trust and user permissions.
- Why no material first-party path remains: observed controls decide narrow workflow rights without an identifiable separate ultimate organizational identity decision organ and return to the work system.

## Evidence gaps

- No provider-backed model run, actual parallel worktree interference trial, or independent verification transcript was executed for this pinned source review. Attributions concern shipped decision paths, not empirical task performance.
- The DSL interpreter is deterministic but the **managed agent** model chooses tool/worker actions; a purely static external .at program can lack S1/S3 agent ownership.
- S2 constructor isolation is optional; unisolated default child workers may still edit overlapping files. A single-use spawn token safeguards admission/staleness but does not itself prove S2.
- S3 whole-current claim concerns managed subagent portfolio, not every one-agent task; S3* basic classifier detects unsupported completion from transcript, while explicit verify-role source/test access is stronger but separately invoked.
- No user-created code, external provider, downstream hosted company authorization or developer repository governance is imported into credited S4/S5.

## Conclusion

Atman's shipped managed-agent runtime closes autonomous coding S1=A, opt-in worktree separation of child write domains S2=C, model-owned whole-current child portfolio control S3=A, and a separate model-backed completion feedback gate plus explicit read/test verify child S3*=A. Confession/memory and DSL configuration are not an owned outside-and-then S4, nor do exact spec/tool approvals create legitimate identity-level S5. Source-first proposed vector: **A / C / A / A / — / —**, mode-scoped and frozen.

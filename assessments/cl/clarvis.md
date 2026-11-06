---
harness_id: clarvis
project_name: Clarvis
repository: https://github.com/getclarvis/clarvis
review_ref: 17a550a7fff59752a1917c3c88dbe9a2aef09bdf
reviewed_at: 2026-11-07
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Clarvis

## Review boundary

- System in focus: first-party local Clarvis coding agent running in its workspace with the built-in `marshall` Lead, executable subagents, and supported `admiral`/workflow-mode leaders through the same kernel/loop. Both interactive TUI and headless CLI are in scope; project-external plugin/MCP providers do not donate organizational functions.
- Purpose and identity: investigate and modify user-selected source files through model-selected code/shell tools, optionally decompose complex work into separately operating leaders, prevent known shared-file interference in scheduled batches, and verify consequences before reporting.
- Relevant environment: repository source, commands/tests, changing errors, user input and approvals, shared workspace writes by parallel leaders, external inference providers and configurable safety/trust boundaries.
- Standard-distribution boundary: `packages/code` CLI → `packages/kernel` file-backed service → `packages/loop` engine and first-party `tools`, `supervision`, `workflows`, `plan` and `memory` capabilities; built-in `marshall`/`admiral` profiles and `audit`/`implement`/`research` workflow definitions. The monorepo packages are one shipped product composition, not independent institutions.
- Credited operating / distribution surfaces: `packages/code/src/run-host.ts`, `packages/kernel/src/{file-kernel,kernel}.ts`, `packages/loop/src/runtime/{execute-run,subagents}.ts`, `packages/workflows/src/{schedule,work-items,run-round,dispatch}.ts`, `packages/workflows/src/builtin-workflows/implement.ts`, `packages/kernel/src/config/builtin-agents/{marshall,admiral}.ts`, and model-selected first-party file/shell tools.
- Adjacent first-party surfaces excluded from ownership: repository CI/release/notarization, development test harness, site/documentation, externally supplied MCP servers and plugins, third-party LLM inference, extension-author scripts, and standalone memory-indexing viewed without prospective environmental adaptation.
- First-party operating modes considered: default `marshall` lead with direct tools and optional subagents; `admiral` workflow leader hierarchy and structured `run_work_items`/`run_round`/`run_workflow`; built-in `implement` with separate review/verification. These workflow paths are supported but not automatically invoked by every simple `marshall` turn.
- Recursion level: one installed workspace coding-agent organization. Workflows can spawn separate full leader runs and subordinate subagents, but the product explicitly bounds the runtime tree and does not establish separate top-level organizations by nesting alone.
- Reviewed source: `getclarvis/clarvis@17a550a7fff59752a1917c3c88dbe9a2aef09bdf` (GitHub repository ID `1346200536`); pinned source from Index #938; active Profile `0.2.4`, Methodology `0.3.7`, reviewed 2026-11-07.

## Repository architecture

`@clarvis/code` uses the local kernel, which composes the first-party `@clarvis/loop` execution engine and tools into run dependencies. The built-in `marshall` model chooses tool calls, edits code, tests and can spawn independent focused subagents. Under the supported `admiral` profile, `run_leader` starts full isolated worker runs whose progress, tool evidence and status are exposed through the run-scoped supervision registry; the model can inspect, steer or stop its own active leaders and has explicit finalization limits while children remain unresolved.

The workflow capability can turn model-produced `work_items` into dependency-ordered **conflict-free waves**. Its code compares declared read/write paths (including directory overlap, Windows/macOS case folding and unknown-scope writers) and prevents a writer/reader or writer/writer pair from executing in the same wave. This is a real S2 anti-interference mechanism, but **not** a write sandbox: correctness depends on worker declarations and file effects respecting scope. The Manager may inspect the entire leader roster, evidence, exhausted budgets, latest checkpoint and proposed next round, then use revision-bound `workflow_decide` to authorize or stop subsequent work.

The built-in `implement` workflow uses separate `coder` leader runs for changes, then an isolated read-only `explorer` leader to inspect **actual diffs and files**, rerun checks and report problems; additional independent read-only leaders try to refute consequential findings. The same package also includes read-only `audit`/`research` variants. This is a complementary path relative to a producer's ordinary implementation report rather than a label-only verifier. Session memory/indexing and future reuse of learned notes are assessed but not credited as S4 absent an externally/prospectively governed option-and-return loop.

Frozen primary sources:

- [Installed product entry and supported modes](https://github.com/getclarvis/clarvis/blob/17a550a7fff59752a1917c3c88dbe9a2aef09bdf/README.md)
- [Code host](https://github.com/getclarvis/clarvis/blob/17a550a7fff59752a1917c3c88dbe9a2aef09bdf/packages/code/src/run-host.ts), [file kernel](https://github.com/getclarvis/clarvis/blob/17a550a7fff59752a1917c3c88dbe9a2aef09bdf/packages/kernel/src/file-kernel.ts), [loop execution](https://github.com/getclarvis/clarvis/blob/17a550a7fff59752a1917c3c88dbe9a2aef09bdf/packages/loop/src/runtime/execute-run.ts)
- [Built-in working Lead](https://github.com/getclarvis/clarvis/blob/17a550a7fff59752a1917c3c88dbe9a2aef09bdf/packages/kernel/src/config/builtin-agents/marshall.ts) and [workflow Admiral](https://github.com/getclarvis/clarvis/blob/17a550a7fff59752a1917c3c88dbe9a2aef09bdf/packages/kernel/src/config/builtin-agents/admiral.ts)
- [Run-scoped supervision/steer](https://github.com/getclarvis/clarvis/blob/17a550a7fff59752a1917c3c88dbe9a2aef09bdf/packages/supervision/src/registry.ts), [lead tools](https://github.com/getclarvis/clarvis/blob/17a550a7fff59752a1917c3c88dbe9a2aef09bdf/packages/loop/src/runtime/subagents/lead-tools.ts)
- [Conflict-specific wave scheduler](https://github.com/getclarvis/clarvis/blob/17a550a7fff59752a1917c3c88dbe9a2aef09bdf/packages/workflows/src/schedule.ts), [runtime work-item dispatch](https://github.com/getclarvis/clarvis/blob/17a550a7fff59752a1917c3c88dbe9a2aef09bdf/packages/workflows/src/work-items.ts), [manager checkpoints](https://github.com/getclarvis/clarvis/blob/17a550a7fff59752a1917c3c88dbe9a2aef09bdf/packages/workflows/src/run-round.ts)
- [Implementation code-review and adversarial verification](https://github.com/getclarvis/clarvis/blob/17a550a7fff59752a1917c3c88dbe9a2aef09bdf/packages/workflows/src/builtin-workflows/implement.ts), [audit workflow](https://github.com/getclarvis/clarvis/blob/17a550a7fff59752a1917c3c88dbe9a2aef09bdf/packages/workflows/src/builtin-workflows/audit.ts)
- [Memory indexing and future recall](https://github.com/getclarvis/clarvis/blob/17a550a7fff59752a1917c3c88dbe9a2aef09bdf/packages/memory/README.md)

## Operational model

The user supplies a task, a provider and workspace trust/action approval. A working model chooses real source/tool actions. In workflow mode, separate leader runs operate with private contexts, shared workspace effects and a common manager-visible supervised state. A deterministic file-scope scheduler attenuates one concrete cross-leader interference risk, while a model Admiral chooses how current resources/rounds should be used after observing evidence and failures. Supported `implement` then reads actual changed artifacts through a separate reviewer and verifier set. Command approval, kernel policy, model settings and persisted memory are not treated as ultimate identity authority.

## S1 — Operations

- State: A
- Function: solve user coding requests through model-chosen workspace investigation, edits, shell/testing operations and feedback.
- Disturbance / variety regulated: unknown project code, cross-file dependencies, broken builds, test failures, incomplete returned work, user clarification and model context limits.
- Decisive decision or feedback right: `marshall`/`coder` model selects tools, target files, edit content, follow-up investigation and final response; independent leaders can complete their own bounded implementation/research tasks.
- Decision owner: executing model-guided agent(s) through the first-party loop; deterministic kernel owns tool grants, effect fencing, session persistence and provider transport.
- Supporting / enforcement mechanisms: `@clarvis/loop` run engine, first-party source/shell tools, workspace trust, scoped grants, plan/task and memory capabilities, model turn/result channels.
- Closure path: user task → model-selected read/edit/run → permitted workspace effect → actual tool output/exit status → next model choice or a bounded returned result.
- Boundary reachability: default installed `clarvis` starts the `marshall` profile with coding tool grants; the kernel constructs loop dependencies; headless and interactive surfaces use the same runtime.
- Why this is / is not agent-owned: only the model-driven execution loop can decide task-specific source transformations and subsequent repairs; fixed command guards do not author the code solution.
- Evidence: [default Lead](https://github.com/getclarvis/clarvis/blob/17a550a7fff59752a1917c3c88dbe9a2aef09bdf/packages/kernel/src/config/builtin-agents/marshall.ts), [loop](https://github.com/getclarvis/clarvis/blob/17a550a7fff59752a1917c3c88dbe9a2aef09bdf/packages/loop/src/runtime/execute-run.ts), [tools](https://github.com/getclarvis/clarvis/blob/17a550a7fff59752a1917c3c88dbe9a2aef09bdf/packages/tools/src/tools/registry.ts), [CLI](https://github.com/getclarvis/clarvis/blob/17a550a7fff59752a1917c3c88dbe9a2aef09bdf/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: provider-backed autonomous run success was not independently measured.

## S2 — Coordination

- State: C
- Function: prevent destructive interference and inconsistent reads among distinct leader coding runs sharing a real workspace, by delaying conflicting scheduled work to later waves.
- Disturbance / variety regulated: overlapping file mutations, concurrent read while another leader writes, directory-scoped overlap, undeclared broad writes and inter-leader dependency failure.
- Distinct S1 units: each `run_leader` creates a separately operating run with its own model context, bounded goal, output/evidence and workspace tool effects; `run_work_items` and workflow rounds may run multiple such leaders.
- Inter-S1 disturbance: two leaders modifying the same file can clobber one another; a reader and writer of the same path can produce a torn or inconsistent observation.
- Attenuating coordination relation: `scheduleWorkItems` normalizes paths and partitions model-declared work into topological layers and waves with no writer/writer or reader/writer file overlap; unscoped mutations run alone; dispatch waits for prior waves and blocks dependents when predecessors fail.
- Feedback into subsequent S1 behaviour: only nonconflicting leaders are spawned in the current wave; conflicting leaders remain queued for subsequent waves and failures block dependent tasks, changing when/if they run and what settled workspace state they observe. Manager receives wave progress and can intervene.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the separation rule is specifically triggered by an evidenced shared-file collision mode; dependency ordering alone would not justify S2, but the actual read/write conflict predicate does.
- Decisive decision or feedback right: model describes tasks and file scopes; a first-party deterministic scheduler chooses conflict-safe concurrent placement and imposes the dispatch barrier.
- Decision owner: constructor-coded S2 enforcement/feedback, not an autonomous agent arbitrating conflict. Neither the `admiral` prompt's safety advice nor generic `agent_list` supervision proves S2 ownership.
- Supporting / enforcement mechanisms: `schedule.ts` conflict predicate, derived topological wave packing, `work-items.ts` admission, `dispatch.ts` semaphore/wave transitions, supervision handles and status/errors.
- Closure path: model-submitted work items → file overlap/reader-writer conflict detection → safe wave sequencing → completed/blocked leader results → changed subsequent leader start and manager-visible status.
- Boundary reachability: `run_work_items` and workflow-round build/dispatch paths actually call the production schedule and dispatcher. The operator must select a workflow/batch; this is not a universal lock on every independent `run_leader` tool call.
- Why this is / is not agent-owned: removing the model does not remove the wave conflict predicate, while changing model output can bypass it by falsely declaring files; there is meaningful first-party coordination construction but no agent-owned comprehensive concurrency arbitration.
- Evidence: [scheduler](https://github.com/getclarvis/clarvis/blob/17a550a7fff59752a1917c3c88dbe9a2aef09bdf/packages/workflows/src/schedule.ts), [batch launch](https://github.com/getclarvis/clarvis/blob/17a550a7fff59752a1917c3c88dbe9a2aef09bdf/packages/workflows/src/work-items.ts), [workflow rounds](https://github.com/getclarvis/clarvis/blob/17a550a7fff59752a1917c3c88dbe9a2aef09bdf/packages/workflows/src/run-round.ts), [wave regression tests](https://github.com/getclarvis/clarvis/blob/17a550a7fff59752a1917c3c88dbe9a2aef09bdf/packages/workflows/tests/unit/schedule.test.ts).
- Basis: explicit + structural.
- Confidence: high for a narrow constructor S2, not global write isolation.
- Caveats: leader-generated file lists can be incomplete or dishonest, and ad-hoc parallel `run_leader` calls are not guaranteed to pass through this file-overlap wave scheduler.

## S3 — Inside-and-now control

- State: A
- Function: allocate current work, attention and leader commitments and decide whether verified progress warrants another expensive round or exception intervention for the overall user goal.
- Disturbance / variety regulated: stalled leaders, failed subgoals, concurrency/token saturation, premature task finalization, unverified findings, incomplete coverage and redundant continuation after low-yield rounds.
- Whole-system current view: Admiral receives a shared supervision registry of all its current leaders (status, activity, budget/tokens, errors and returned evidence), the workflow's complete round state and discovered work items; `workflow_status` exposes exact active checkpoint, proposed next round, revision and leader-capacity limits.
- Current-control decision scope: model Admiral chooses which leaders to launch with scoped goals, which to stop or steer after observing activity, which result needs a fresh independent verification round, and `workflow_decide(continue|stop)` for the next explicitly authorized round. Runtime enforces finite total leader ceiling, one active sequence and CAS revision, but does not make the semantic current-priority judgment.
- Decisive decision or feedback right: active LLM-backed Lead/Admiral selects operational commitments and exception interventions on current observed whole-run state; parent/hardcoded limits only bound these choices.
- Decision owner: `admiral` model in supported workflow profile; default `marshall` also supervises its own spawned agents but does not by its label alone justify this broader workflow-level S3.
- Supporting / enforcement mechanisms: `agent_list`/`agent_poll`/`agent_steer`/`agent_stop`/`await_agents`, run-scoped supervision registry, work-item/wave ledger, `workflow_status`, revision-bound `workflow_decide`, finalize gate and budget monitor.
- Closure path: current portfolio of leader evidence + exception/budget state → Lead model chooses reallocation/steer/stop/next round → kernel dispatch/CAS gate → changed live commitments and new results → another global checkpoint or terminal synthesis.
- Boundary reachability: `admiral` is a shipped builtin agent profile with `workflow` grant; first-party `run_round`, `run_work_items` and supervisor tools are exposed in its loop, and `workflow_decide` explicitly changes subsequent execution.
- Why this is / is not agent-owned: the model must judge which failing/unverified goal deserves a leader, steer and another round; the semaphore, registry and CAS check enforce capacity/correctness but do not decide whether continued work is worthwhile.
- Evidence: [admiral profile and supervisory instructions](https://github.com/getclarvis/clarvis/blob/17a550a7fff59752a1917c3c88dbe9a2aef09bdf/packages/kernel/src/config/builtin-agents/admiral.ts), [runtime checkpoint tool](https://github.com/getclarvis/clarvis/blob/17a550a7fff59752a1917c3c88dbe9a2aef09bdf/packages/workflows/src/run-round.ts), [supervision registry](https://github.com/getclarvis/clarvis/blob/17a550a7fff59752a1917c3c88dbe9a2aef09bdf/packages/supervision/src/registry.ts).
- Basis: explicit + structural.
- Confidence: high for the supported workflow current-control mode; no cross-workspace organization-wide S3 is claimed.
- Caveats: workflow profiles and artifact definitions may be operator-overridden; S3 is tied to the actual first-party supported `admiral` mode, not every serial task or the mere existence of planning data.

## S3* — Complementary audit

- State: A
- Function: independently inspect and challenge coding producers' actual changes against real source and tests and return a bounded review/verifier verdict to the supervising workflow.
- Disturbance / variety regulated: self-serving or mistaken builder completion reports, untested code changes, missing caller updates, hallucinated test outcomes, reviewer false positives and unobserved coverage gaps.
- Claim being audited: `implement` workflow's coder leaders claim that specific workspace edits are complete, correct and checked; reviewer claims about defects are themselves subjected to separate refutation.
- Ordinary reporting path: coder leaders' `build.findings`, self-run checks, returned result schema and routine run transcripts/ledger.
- Complementary access path: later `review` round starts a distinct, read-only `explorer` leader with its own context and instructions to read the actual diff/files, rerun checks and cite exact source. Its load-bearing findings are given to **different** `verify` leaders that independently attempt to falsify them in source, using explicit `confirmed`/`refuted`/`inconclusive` verdicts.
- Independence boundary: full isolated leader contexts and read-only review/verification roles have independent raw-artifact/command access beyond the producer's self-report; verifier fanout and threshold preserve failed/inconclusive replicas. All are first-party model workloads on an operator-chosen provider, not external institutionally independent auditors.
- Who acts on findings: `admiral` is obliged to collect rounds, review verified evidence and decide whether to continue, stop, report unresolved defects or launch corrective work. Built-in `implement` synthesis includes surviving review defects as work outstanding rather than silently accepting them.
- Decisive decision or feedback right: read-only Reviewer/Verifier models choose substantive source-grounded diagnostics and counterexamples, while the deterministic threshold aggregates their structured evidence; Lead decides subsequent control.
- Decision owner: distinct reviewer and verifier model-led work units in the explicitly selected first-party `implement` workflow; not the production coder or the deterministic parser alone.
- Supporting / enforcement mechanisms: typed round result schema, review→verify selectors, source-reading tools, separate leader contexts, threshold aggregation including failed replicas and stepwise Manager checkpoints.
- Closure path: implementation result → separate raw diff/file inspection and rerun checks → adversarial source verification of consequential findings → structured surviving/refuted findings → Admiral's next current-control action/synthesis.
- Boundary reachability: bundled `IMPLEMENT_WORKFLOW` is registered by first-party workflows capability; `run_workflow` can execute it after supported operator review and delivers distinct leader rounds via production `run-round.ts`.
- Why this is / is not agent-owned: fresh source inspection, selecting counterexamples and explanatory diagnostic judgments are model-run decisions in an isolated reviewer context; raw artifacts and a majority threshold alone would not close the complementary function.
- Evidence: [builtin implement path](https://github.com/getclarvis/clarvis/blob/17a550a7fff59752a1917c3c88dbe9a2aef09bdf/packages/workflows/src/builtin-workflows/implement.ts), [round runtime](https://github.com/getclarvis/clarvis/blob/17a550a7fff59752a1917c3c88dbe9a2aef09bdf/packages/workflows/src/run-round.ts), [independent run leader](https://github.com/getclarvis/clarvis/blob/17a550a7fff59752a1917c3c88dbe9a2aef09bdf/packages/workflows/src/run-leader.ts), [model reviewer profile](https://github.com/getclarvis/clarvis/blob/17a550a7fff59752a1917c3c88dbe9a2aef09bdf/packages/kernel/src/config/builtin-agents/explorer.ts).
- Basis: explicit + structural.
- Confidence: medium-high for code-artifact review; no external assurance claim.
- Caveats: selecting `implement` or another staged review mode matters: default `marshall` task completion does not necessarily run this independent verification chain. The separate `audit` workflow targets user-chosen subjects and is not alone treated as internal auditing of the coding S1.

## S4 — Outside-and-then intelligence

- State: —
- Function: no qualifying separate external-and-prospective adaptation-option loop with returned current capability change at the declared Clarvis server/workspace level was established.
- Disturbance / variety regulated: the product tracks new user tasks, prior fixes, context pressure and indexed repository knowledge; these affect present or later task execution, but the inspected loop does not generate and return a governed future-capability option.
- Decisive decision or feedback right: no first-party strategic future/environment change-selection right; the model can write memory notes and an operator can install plugins/skills, but these are not a bounded S4 adaptation authority path.
- Decision owner: user and model for their current objectives and local memory authoring; external contributors for evolving the product itself, which is outside the shipped runtime boundary.
- Supporting / enforcement mechanisms: `@clarvis/memory` post-run model indexer/wiki, model catalog/configuration, tool discovery, static update notices and user-managed extension/workflow files.
- Closure path: observed run → memory indexing/retrieval → later context enrichment; no distinct external-future assessment, option selection, S3 negotiation and controlled capability revision was evidenced.
- Why this is / is not agent-owned: learning/retrieval and task planning can help later work but do not by themselves establish S4's outside-and-then intelligence function or future-relevant option/return process.
- Evidence: [memory indexing/retrieval](https://github.com/getclarvis/clarvis/blob/17a550a7fff59752a1917c3c88dbe9a2aef09bdf/packages/memory/README.md), [kernel runtime composition](https://github.com/getclarvis/clarvis/blob/17a550a7fff59752a1917c3c88dbe9a2aef09bdf/packages/kernel/src/file-kernel.ts), [user-facing options/update boundary](https://github.com/getclarvis/clarvis/blob/17a550a7fff59752a1917c3c88dbe9a2aef09bdf/README.md).
- Basis: structural absence review.
- Confidence: medium-high.
- Caveats: operator-maintained future strategy or independent product engineering may exist, but neither is a shipped autonomously closed runtime S4.

### Absence scope

- Surfaces inspected: memory tools/indexer, role planner, workflow rounds/scheduler, model configuration, extension profiles, updater controls and product docs.
- Plausible first-party paths checked: detecting environmental trajectories rather than only present errors, developing prospective alternate capabilities, ratifying one against current operations and returning it to the active agent tool/policy repertoire.
- Why no material first-party path remains: historical memory, dynamic current scheduling and manually supplied extensions lack an evidenced external-and-prospective choice-and-return pipeline under this runtime's ownership.

## S5 — Policy and identity

- State: —
- Function: no distinct identity/ultimate policy debate, legitimate parent ratification and binding returned governance of the whole Clarvis organization is established.
- Disturbance / variety regulated: host command permissions, workspace trust, sandbox bounds, role grants and task approvals control operational effects under a given purpose, not a dispute about the organization's ultimate identity.
- Decisive decision or feedback right: no first-party mechanism exposes an ultimate mission/ethos conflict and authorizes final resolution binding both present operation and future adaptation.
- Decision owner: workspace owner and operator authorize tools/models/extensions and individual workflow launches, but do not exercise a demonstrably distinct S5 identity-closure contract through the shipped runtime.
- Supporting / enforcement mechanisms: agent profile priority text, permission and trust prompts, tool capability grants, plan approval/revision, kernel policies, immutable context admission and user configuration.
- Closure path: a tool, plan or workflow requests authorization → operator/runtime allows or refuses a scoped effect; no identity-level issue → charter authority → durable returned decision path exists.
- Why this is / is not agent-owned: static safety priority and the term `policy` do not create an autonomous ultimate-policy decision right; the user having final say over commands is not equivalent to a parent S5 mode.
- Evidence: [builtin lead scope](https://github.com/getclarvis/clarvis/blob/17a550a7fff59752a1917c3c88dbe9a2aef09bdf/packages/kernel/src/config/builtin-agents/marshall.ts), [kernel policy](https://github.com/getclarvis/clarvis/blob/17a550a7fff59752a1917c3c88dbe9a2aef09bdf/packages/kernel/src/policy.ts), [security boundary](https://github.com/getclarvis/clarvis/blob/17a550a7fff59752a1917c3c88dbe9a2aef09bdf/README.md).
- Basis: structural absence review.
- Confidence: medium-high.
- Caveats: the user's external professional/project governance is not imported into the self-hosted coding-agent boundary.

### Absence scope

- Surfaces inspected: agent profile and safety ordering, local kernel policy/workspace trust, plan gating, workflow admission, model/extension selection and persisted configuration.
- Plausible first-party paths checked: dispute over purpose/identity, legitimate ultimate-policy owner, ratified charter change, returned binding governance across subsequent operations.
- Why no material first-party path remains: all reachable decision paths regulate task selection, effects, safety or operational resources without an ultimate-policy issue/ratification loop.

## Recursion

The workspace-level model/tool agent performs coding S1. The optional Admiral workflow owns present control of isolated *leader* working units within its run, not an external management hierarchy. Conflict-aware waves attenuate simultaneous file operations at that same recursion; independently staffed reviewer/verifier leaders check earlier builder claims through a complementary path. Subagent and leader nesting alone does not prove recursion or full VSM completeness. External enterprise/project policy, provider internals and Clarvis maintainers' own OSS development are not admitted into the assessed runtime.

## Variety and escalation

Model-guided coding creates local operational variety to fit a user goal. Workspace trust/permission rules constrain effects. Under an explicit workflow, model-declared file scopes drive a constructor-owned anti-collision schedule, while Supervisor/Admiral role can steer/stop live leaders, authorize additional verification and own an evidence-bounded finish decision. Built-in `implement` challenges builder claims from an independent raw-source/test path and can mark findings outstanding. Operator-provided memory and future extension updates remain uncredited as S4 absent a prospective environmental option loop; there is no evidenced S5 charter authority path.

## Evidence gaps

Frozen revision matched GitHub and local checkout. Reviewed first-party monorepo boundaries, concrete engine/kernel/workflow wiring, source for collision scheduler, supervisor role/context and built-in implementation audit. Documentation/TypeScript regression fixtures corroborate source, not a live external coding task. The required contributor Bun `1.4.0` runtime was **not available** in this environment; upstream Bun suites, full portable distribution smoke and live model-backed workflow were **not run**. Deterministic Index-level validation must be checked separately. The conflict scheduler relies on truthful declared file scopes; unscheduled raw concurrent leaders may still collide. S3* independence is role/context/artifact-level, not external organizational independence.

## Assessment summary

Clarvis's model/tool coding loop owns operational work (**S1=A**). Its supported structured workflow scheduler supplies narrow, deterministic shared-file conflict attenuation among separately operating leaders (**S2=C**), while the LLM-backed Admiral chooses current leader interventions and round commitments from the whole active workflow (**S3=A**). The bundled `implement` workflow gives separate read-only reviewer and adversarial verifier leaders direct evidence access and consequential findings returned for present control (**S3*=A**). Persistent learning/memory and operator policy/approval mechanisms do not by themselves close external-and-future S4 or ultimate-policy S5 (**—**, **—**). This is a frozen-source organizational mapping, not a quality or safety grade.

Proposed vector: **`A · C · A · A · — · —`**.

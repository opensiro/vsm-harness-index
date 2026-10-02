---
harness_id: carbon
project_name: Carbon
repository: https://github.com/thecarbonlayer/carbon
review_ref: 8fafacd56f10a6eeb6f3b095fa6af3dfb5681aaf
reviewed_at: 2026-10-02
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-02
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# Carbon

## Review boundary

- System in focus: the first-party Carbon coding-agent harness at frozen revision `8fafacd56f10a6eeb6f3b095fa6af3dfb5681aaf`, including the mature `Agent` model/tool loop, coding tools and workspace, policy/approval gate, sandbox, durable sessions and memory, context management, orchestration helpers, subagent/delegation tools, verification primitives, observability and the versioned editable configuration surface shipped in this repository.
- Purpose and identity: teach and provide a reusable from-scratch coding-agent harness whose first-party runtime lets a model inspect a repository, use coding/system tools, modify code under policy, delegate bounded research, preserve state, run tests and return a result through REPL, print-mode and TUI/library surfaces.
- Relevant environment: human/operator task input; project repository/workspace and `AGENTS.md`; model provider endpoints; local/Docker execution substrate; prior Carbon sessions; optional consumer tools/extensions; tests and shell results; external consumers that embed Carbon.
- Standard-distribution boundary: the frozen repository's `harness/`, `model/`, `carbon/`, `ui/` and normal CLI/library surfaces are inside. Model/provider services, Docker/host internals and consumer-owned domain logic remain dependencies. The separate public `refinery` evaluation/self-improvement consumer and Carbon's separate `self-improvement` branch are not imported into this frozen default-branch assessment.
- Credited operating / distribution surfaces: `README.md`; `carbon/__init__.py`; `harness/agent.py`; `harness/tools.py`; `harness/workspace.py`; `harness/sandbox.py`; `harness/policy.py`; `harness/memory.py`; `harness/orchestrator.py`; `harness/subagents.py`; `harness/verification.py`; `harness/harness_config.py`; `harness/session_env.py`.
- Adjacent first-party surfaces excluded from ownership: repository CI/release/contributor governance; `tasks/` acceptance tooling and `tests/` as runtime owners (used only to corroborate shipped behavior); dev-roadmap prose as an owner; the opt-in example `extensions/audit_log.py`; external consumer/evaluation/editor repositories including `refinery`; the non-frozen `self-improvement` branch; chapter-history tags except as documentation of current primitives.
- First-party operating / deployment modes considered: interactive REPL; one-shot print mode; TUI; direct `Agent`/Carbon library use; default mature coding toolbelt with delegate/fan-out tools; optional `Orchestrator`; persisted-session/memory operation; default verification gate when a project declares a test command.
- Recursion level: one Carbon coding session is the primary system-in-focus. Fresh delegated subagents are bounded subordinate operational workers within that session; they are not silently promoted into a higher-recursion viable organization merely because fan-out can run several workers concurrently.
- Reviewed revision: `8fafacd56f10a6eeb6f3b095fa6af3dfb5681aaf`.
- Observation date: 2026-10-02.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Carbon's mature runtime is a model-driven coding loop. `Agent` assembles the system/project context, calls an OpenAI-compatible provider, exposes first-party tools, executes selected tool calls through a policy and workspace/sandbox boundary, appends results to the model history and continues until the model finishes or a bounded runtime condition stops the turn. REPL, print mode and TUI use the shared mature coding-tool builder, which includes repository exploration, file mutation, sandboxed bash, episodic search and bounded delegation/fan-out.

The harness has durable JSONL sessions, cross-session keyword retrieval, trace persistence, context compaction and checkpoint/scratch machinery. These mechanisms preserve/recover operational context; they do not by themselves model external futures or generate organizational adaptation options.

Delegation creates a fresh full `Agent` for a self-contained subtask. The mature coding toolbelt intentionally gives delegated workers a read-only view of the parent's workspace by default, because a worker runs under its own policy and otherwise could mutate without reaching the parent's approval gate. `fan_out` can run independent subtasks concurrently and returns ordered labeled answers to the parent. This is bounded task decomposition and vertical permission containment. The frozen evidence does not identify a sibling-worker conflict/oscillation and a feedback relation that coordinates those workers with one another, so it is not credited as S2.

`Orchestrator` asks a planner model for two-to-four steps, executes them sequentially through one worker Agent, allows a caller approval callback to skip a step and retries a failed step. This is useful workflow sequencing but does not create a whole-system current view or current-control authority over a population of S1 units.

Carbon exposes two verification-related paths. The normal mature `Agent` gate watches whether a code-changing turn produced a real passing run of the project's declared test command after the last mutation; if not, it pushes corrective text back to the same operational model and eventually marks the result unverified. Separately, the shipped production module `harness/verification.py` provides a verification constructor: `run_python(code, check)` executes candidate code plus a caller-supplied assertion in a fresh scrubbed process and only reports success after a per-run random nonce is emitted after the assertion. The helper supplies materially different execution evidence from the model's narrative claim, but the independent assertion/audit authority and its composition into a consequential control loop remain caller-owned. That supports constructor S3*, not autonomous audit ownership.

Carbon also exposes a carefully bounded editable configuration surface and `surface_manifest()`, including named strategy menus, locked fields and immutable invariants. The repository documentation is unusually explicit about its boundary: ADR 0002 states that a consumer's propose-and-validate/release workflow must not migrate into Carbon, and the generalization audit identifies `refinery` as the external measurement/self-improving editor that drives and edits Carbon from outside it. Therefore the editable surface is an adaptation target/mechanism for another system, not evidence that the frozen Carbon runtime itself closes S4.

Primary evidence:

- [`README.md`](https://github.com/thecarbonlayer/carbon/blob/8fafacd56f10a6eeb6f3b095fa6af3dfb5681aaf/README.md)
- [`harness/agent.py`](https://github.com/thecarbonlayer/carbon/blob/8fafacd56f10a6eeb6f3b095fa6af3dfb5681aaf/harness/agent.py)
- [`harness/subagents.py`](https://github.com/thecarbonlayer/carbon/blob/8fafacd56f10a6eeb6f3b095fa6af3dfb5681aaf/harness/subagents.py)
- [`harness/orchestrator.py`](https://github.com/thecarbonlayer/carbon/blob/8fafacd56f10a6eeb6f3b095fa6af3dfb5681aaf/harness/orchestrator.py)
- [`harness/verification.py`](https://github.com/thecarbonlayer/carbon/blob/8fafacd56f10a6eeb6f3b095fa6af3dfb5681aaf/harness/verification.py)
- [`harness/harness_config.py`](https://github.com/thecarbonlayer/carbon/blob/8fafacd56f10a6eeb6f3b095fa6af3dfb5681aaf/harness/harness_config.py)
- [`dev-notes/adr/0002-mechanism-in-gemma-domain-in-the-consumer.md`](https://github.com/thecarbonlayer/carbon/blob/8fafacd56f10a6eeb6f3b095fa6af3dfb5681aaf/dev-notes/adr/0002-mechanism-in-gemma-domain-in-the-consumer.md)
- [`dev-notes/generalization-audit.md`](https://github.com/thecarbonlayer/carbon/blob/8fafacd56f10a6eeb6f3b095fa6af3dfb5681aaf/dev-notes/generalization-audit.md)

## Operational model

A normal Carbon session receives the user's coding objective and project context, then the model repeatedly chooses among first-party read/search/write/edit/patch/bash/memory/delegation tools. Tool results and policy refusals return into later model turns. The agent therefore owns the open-ended operational choice of what to inspect, modify, execute or delegate while deterministic machinery confines the workspace, gates mutations, manages context and records results.

The parent model may delegate or fan out independent read-only research to fresh workers. Workers return bounded answers; the parent retains mutation authority and integrates those answers into its own subsequent S1 decisions. The standard path deliberately avoids treating concurrent workers as a self-coordinating organization.

When verification is relevant, the ordinary model can be challenged by execution evidence rather than its completion text. The integrated gate uses a declared project test command and returns missing/failing-verification feedback to the same S1. The standalone verification helper goes further as a constructor: a caller supplies an assertion that executes with candidate code in a separate scrubbed process, returning an independent pass/fail evidence object for downstream composition.

## S1 — Operations

- State: A
- Function: perform a coding task through an autonomous model-driven loop that inspects project state, chooses tools, edits files, executes commands, retrieves prior context, delegates bounded research and reacts to returned evidence.
- Disturbance / variety regulated: ambiguous task requirements, repository/file state, code and test failures, tool errors, provider faults, context pressure, prior-session information, approval denials and subagent findings.
- Decisive decision or feedback right: choose the substantive next task action—what evidence to inspect, which tool/subtask to invoke, which change to make and how to react to tool/test/delegation feedback.
- Decision owner: the autonomous model actor driven by Carbon's first-party `Agent` loop.
- Supporting / enforcement mechanisms: tool registry; workspace confinement; approval/permission policy; sandbox; retry/compaction limits; session persistence; episodic retrieval; verification gate; delegate/fan-out transport; tracer and result objects.
- Closure path: user task/context → model call → model selects tool/action/delegation → first-party runtime executes or refuses it → result/subagent finding/test evidence returns to model history → model selects a subsequent action → loop reaches a completion result or bounded stop.
- Boundary reachability: README-supported REPL, print mode, TUI and direct library use all expose the mature first-party `Agent` execution boundary rather than requiring a downstream application to write the operational model/tool loop.
- Why this is / is not agent-owned: removing the model leaves tools, policy, storage, sandbox and deterministic gates but no open-ended coding decisions; the model's task-specific choices are therefore decisive S1 ownership rather than mere enforcement.
- Evidence: [`README.md`](https://github.com/thecarbonlayer/carbon/blob/8fafacd56f10a6eeb6f3b095fa6af3dfb5681aaf/README.md); [`harness/agent.py`](https://github.com/thecarbonlayer/carbon/blob/8fafacd56f10a6eeb6f3b095fa6af3dfb5681aaf/harness/agent.py); [`harness/tools.py`](https://github.com/thecarbonlayer/carbon/blob/8fafacd56f10a6eeb6f3b095fa6af3dfb5681aaf/harness/tools.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: provider inference is external; deterministic policies/limits support and constrain S1 without acquiring ownership of the substantive coding decisions.

## S2 — Coordination

- State: —
- Function: no material first-party mutual-adjustment function among distinct sibling S1 units is established at the reviewed recursion.
- Disturbance / variety regulated: Carbon can create several fresh subagents and run independent subtasks in parallel, but the reviewed path does not establish a concrete interaction-generated conflict/oscillation among those workers together with a relation that feeds a coordination result back into their subsequent behavior.
- Decisive decision or feedback right: not established for an S2-specific relation.
- Decision owner: not established.
- Supporting / enforcement mechanisms: read-only default worker policy; isolated agent contexts; shared parent session scratch; ordered fan-out result collection; parent-owned mutation; thread-pool concurrency.
- Closure path: not applicable for the negative finding. Workers execute assigned independent subtasks and return answers to the parent; there is no evidenced sibling mutual-adjustment loop.
- Why this is / is not agent-owned: the parent model may decide to delegate and later integrate answers, but delegation/task decomposition is an S1 operating technique here. The read-only worker policy prevents bypass of the parent's approval boundary rather than deciding an inter-S1 coordination response.
- Evidence: [`harness/subagents.py`](https://github.com/thecarbonlayer/carbon/blob/8fafacd56f10a6eeb6f3b095fa6af3dfb5681aaf/harness/subagents.py); [`harness/agent.py`](https://github.com/thecarbonlayer/carbon/blob/8fafacd56f10a6eeb6f3b095fa6af3dfb5681aaf/harness/agent.py); [`tests/test_delegation_boundaries.py`](https://github.com/thecarbonlayer/carbon/blob/8fafacd56f10a6eeb6f3b095fa6af3dfb5681aaf/tests/test_delegation_boundaries.py); [`tests/episodes/test_ch11.py`](https://github.com/thecarbonlayer/carbon/blob/8fafacd56f10a6eeb6f3b095fa6af3dfb5681aaf/tests/episodes/test_ch11.py).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: a downstream composition could assign overlapping mutable work and add collision handling, but that is not a first-party S2 path in this frozen distribution.

### Absence scope

- Surfaces inspected: mature delegate/fan-out tool wiring; `run_subagent`; worker policies; thread-pool fan-out; shared scratch routing; delegation-boundary tests; orchestration planner; parent result integration.
- Plausible first-party paths checked: parallel worker write conflicts; shared-workspace contention; shared-scratch collision; negotiated task ownership; worker-to-worker messaging; collision detection; merge arbitration; scheduler/turn-taking among sibling agents.
- Why no material first-party path remains: shipped fan-out is explicitly for independent subtasks, workers are read-only by default, results are returned to the parent, and tests establish permission/scratch isolation rather than an inter-worker disturbance plus corrective feedback into sibling behavior.

## S3 — Inside-and-now control

- State: —
- Function: no distinct whole-system current-control function is established above Carbon's single coding-session S1.
- Disturbance / variety regulated: the runtime bounds one session through policy, tool-step limits, verification, retries and optional planned steps, but it does not maintain a whole-system current view and choose allocations/priorities/commitments among multiple S1 operations.
- Decisive decision or feedback right: not established. `Orchestrator` plans a task and executes steps sequentially through one worker; the mature parent agent delegates bounded subtasks but no first-party metasystem owns organization-wide current resource or commitment tradeoffs.
- Decision owner: not established.
- Supporting / enforcement mechanisms: `Orchestrator` plan sequencing; caller step approval; per-step retry; Agent limits/deadline; policy gate; worker read-only constraints; verification; tracing.
- Closure path: not applicable for the negative finding; observed controls either structure one S1 task or enforce caller-selected constraints rather than regulate a whole operational population.
- Why this is / is not agent-owned: planner/model choices in `Orchestrator` decompose a parent task and the normal model owns S1 task execution. No separate S3 decision right survives the Profile's whole-system current-view test.
- Evidence: [`harness/orchestrator.py`](https://github.com/thecarbonlayer/carbon/blob/8fafacd56f10a6eeb6f3b095fa6af3dfb5681aaf/harness/orchestrator.py); [`harness/agent.py`](https://github.com/thecarbonlayer/carbon/blob/8fafacd56f10a6eeb6f3b095fa6af3dfb5681aaf/harness/agent.py); [`tests/episodes/test_ch10.py`](https://github.com/thecarbonlayer/carbon/blob/8fafacd56f10a6eeb6f3b095fa6af3dfb5681aaf/tests/episodes/test_ch10.py).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: a downstream workflow or external self-improvement organization can own higher-recursion current control, but that authority is not inherited by Carbon.

### Absence scope

- Surfaces inspected: `Orchestrator`; parent Agent; delegate/fan-out; policy/approval gate; max-step/deadline/retry controls; checkpoints/session state; observability.
- Plausible first-party paths checked: multi-S1 current-state aggregation; shared resource allocator; commitment/priority bargaining; exception supervisor; cross-worker performance intervention; organization-level admission/concurrency control.
- Why no material first-party path remains: planning and retry operate on one task/worker sequence, delegation is subordinate S1 execution, and hard limits enforce preselected constraints without a whole-system current-control decision owner.

## S3* — Complementary audit

- State: C
- Function: expose a first-party verification path that can challenge a model-produced candidate against execution evidence distinct from the model's ordinary completion claim.
- Disturbance / variety regulated: an operational coding model may claim a change is complete even though candidate code fails a required assertion/test, a claimed test run is stale relative to the last mutation, or a forged/short-circuited receipt would otherwise appear successful.
- Decisive decision or feedback right: the shipped `harness.verification.run_python(code, check)` primitive executes candidate code plus a caller-supplied assertion in a fresh scrubbed process and returns a structured pass/fail result only when a random post-check nonce is observed; the surrounding composition still supplies the independent assertion/audit authority and decides consequential acceptance.
- Decision owner: constructor path. Carbon supplies the complementary execution/evidence primitive and deterministic result judgment, but no independent autonomous auditor owns the substantive audit criterion in the standard distribution.
- Supporting / enforcement mechanisms: temporary isolated work directory; scrubbed environment; per-run random nonce; subprocess exit status/output; the mature Agent's separate observed-test-receipt gate; mutation ordering and verification-attempt cap.
- Closure path: candidate code/claim → constructor invokes fresh-process assertion verification → complementary pass/fail evidence is returned → a composed caller can accept/reject/repair; in Carbon's normal coding loop, the analogous observed-test gate already demonstrates a first-party return pattern by pushing missing/failing-verification feedback into a subsequent model turn.
- Boundary reachability: `harness/verification.py` is a shipped production harness module explicitly documented in README's primitive map as verification that runs candidate code against an assertion and returns proof rather than trust. It does not depend on repository CI/test execution to exist, while the mature Agent's built-in test gate corroborates the intended control relation.
- Why this is / is not agent-owned: removing the operational model leaves the fresh-process verifier able to judge supplied candidate/assertion evidence; removing the caller-supplied criterion leaves no substantive audit claim to judge. Carbon therefore supplies a function-specific constructor, not an autonomous S3* owner.
- Evidence: [`harness/verification.py`](https://github.com/thecarbonlayer/carbon/blob/8fafacd56f10a6eeb6f3b095fa6af3dfb5681aaf/harness/verification.py); [`harness/agent.py`](https://github.com/thecarbonlayer/carbon/blob/8fafacd56f10a6eeb6f3b095fa6af3dfb5681aaf/harness/agent.py); [`README.md`](https://github.com/thecarbonlayer/carbon/blob/8fafacd56f10a6eeb6f3b095fa6af3dfb5681aaf/README.md); [`tests/episodes/test_ch12.py`](https://github.com/thecarbonlayer/carbon/blob/8fafacd56f10a6eeb6f3b095fa6af3dfb5681aaf/tests/episodes/test_ch12.py).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: the default Agent gate is a routine in-band QA path and is not by itself credited as S3*. The positive `C` rests on the separately shipped fresh-process assertion verifier as a constructor; a downstream system must supply sufficiently independent criteria and consequential closure.
- Claim being audited: that model-produced candidate code satisfies an externally supplied executable assertion/verification condition rather than merely being described as correct by the operational model.
- Ordinary reporting path: model final response plus normal tool transcript and ordinary coding-session result.
- Complementary access path: execute candidate code and the supplied assertion in a separate scrubbed process and require process success plus an unpredictable nonce emitted only after the assertion completes.
- Independence boundary: execution/evidence collection is separated from the model's narrative claim and cannot be satisfied by merely claiming success; however, the audit criterion itself is caller supplied and Carbon does not package a distinct autonomous auditor or protected domain oracle.
- Who acts on findings: a composed consumer decides consequential acceptance/repair from `VerificationResult`; the built-in test-receipt gate separately demonstrates that Carbon can return verification failure/missing evidence to the operational model for another turn.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party outside-and-then adaptation loop is closed inside the frozen Carbon distribution.
- Disturbance / variety regulated: Carbon can recall prior sessions and exposes configurable strategy choices, but it does not itself sense external/future change, evaluate alternatives through an independent improvement environment and select/promote an adaptation back into current capability.
- Decisive decision or feedback right: not established inside Carbon. The repository deliberately leaves proposal/evaluation/release policy to external consumers such as `refinery`.
- Decision owner: not established within the assessed boundary.
- Supporting / enforcement mechanisms: durable session memory/search; editable `harness_config.json`; `config_schema()`; `surface_manifest()`; bounded strategy registries; config versioning; locked fields and immutable invariants.
- Closure path: not applicable for the negative finding. Carbon can consume a changed configuration after restart, but the sensing → prospective option generation/evaluation → adaptation decision path that chooses such a change lives outside the frozen runtime.
- Why this is / is not agent-owned: the operational model may search old sessions and adapt a current task, but that is S1. The editable surface is intentionally an actuator/contract for an external improver rather than an internal agent-owned adaptation decision.
- Evidence: [`harness/harness_config.py`](https://github.com/thecarbonlayer/carbon/blob/8fafacd56f10a6eeb6f3b095fa6af3dfb5681aaf/harness/harness_config.py); [`harness/memory.py`](https://github.com/thecarbonlayer/carbon/blob/8fafacd56f10a6eeb6f3b095fa6af3dfb5681aaf/harness/memory.py); [`dev-notes/adr/0002-mechanism-in-gemma-domain-in-the-consumer.md`](https://github.com/thecarbonlayer/carbon/blob/8fafacd56f10a6eeb6f3b095fa6af3dfb5681aaf/dev-notes/adr/0002-mechanism-in-gemma-domain-in-the-consumer.md); [`dev-notes/generalization-audit.md`](https://github.com/thecarbonlayer/carbon/blob/8fafacd56f10a6eeb6f3b095fa6af3dfb5681aaf/dev-notes/generalization-audit.md); [`AGENTS.md`](https://github.com/thecarbonlayer/carbon/blob/8fafacd56f10a6eeb6f3b095fa6af3dfb5681aaf/AGENTS.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: Carbon is intentionally designed to be edited by `refinery`; an assessment of the composed Carbon+Refinery organization could produce a different S4 result, but that external consumer is outside this repository assessment.

### Absence scope

- Surfaces inspected: durable session/memory retrieval; editable config/schema/manifest; strategy registries; immutable invariants; README self-improvement description; ADR 0002; generalization audit; branch contract; orchestrator/planner.
- Plausible first-party paths checked: autonomous configuration proposal; external-environment sensing; held-in/held-out evaluation; option comparison; promotion/release authority; self-edit selection; durable adaptation feedback into the running harness.
- Why no material first-party path remains: primary repository authority explicitly places the editor's propose-and-validate loop, evaluation integrity rules and release workflow in the consumer; the public `refinery` drives and edits Carbon from outside it. Carbon ships the configurable mechanism/actuator but not the S4 decision loop.

## S5 — Identity / ultimate policy

- State: —
- Function: no material first-party identity/ultimate-policy closure loop is established at the selected Carbon runtime recursion.
- Disturbance / variety regulated: approval rules, read-only policy, editable fields, locked fields and immutable verification/config invariants constrain behavior, but they are predefined mechanisms/constraints rather than a runtime process that decides Carbon's identity or ultimate policy.
- Decisive decision or feedback right: not established. A human/consumer chooses policies/configuration outside the runtime; Carbon enforces those choices and rejects invalid/forbidden behavior.
- Decision owner: ultimate policy remains with developer/operator/consumer authority outside the assessed runtime; no first-party parent-governed identity issue/decision/return loop is packaged.
- Supporting / enforcement mechanisms: `Policy` allow/deny/read-only/approval rules; `harness_config.json`; `surface_manifest()`; non-editable fields; immutable invariants; approval callbacks; fail-closed tool decisions.
- Closure path: not applicable; supplied policy/configuration affects later execution, but no identity/ultimate-policy issue is raised to legitimate authority, decided there and returned through a first-party governance path.
- Why this is / is not agent-owned: removing the coding model leaves materially identical policy/configuration enforcement. Conversely, operator/developer control of those files/callbacks is generic external configuration, not an evidenced S5 parent loop under Methodology 0.3.6.
- Evidence: [`harness/policy.py`](https://github.com/thecarbonlayer/carbon/blob/8fafacd56f10a6eeb6f3b095fa6af3dfb5681aaf/harness/policy.py); [`harness/harness_config.py`](https://github.com/thecarbonlayer/carbon/blob/8fafacd56f10a6eeb6f3b095fa6af3dfb5681aaf/harness/harness_config.py); [`README.md`](https://github.com/thecarbonlayer/carbon/blob/8fafacd56f10a6eeb6f3b095fa6af3dfb5681aaf/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: repository maintainers and external consumers obviously exercise real governance, but that higher-recursion OSS/product governance is not silently inherited as runtime S5.

### Absence scope

- Surfaces inspected: permission `Policy`; approval callbacks; config loader/schema/manifest; immutable invariants; system prompt; extension loading controls; branch/governance documentation; self-improvement boundary.
- Plausible first-party paths checked: identity-level proposal/escalation; ultimate-policy deliberation; legitimate parent decision and return; autonomous constitution revision; runtime conflict between present operation and future adaptation; policy exception governance.
- Why no material first-party path remains: all located policy surfaces are static/preselected constraints or external configuration, while repository/product governance is adjacent to the runtime and supplies no first-party operational identity/ultimate-policy closure path.

## Recursion, variety, escalation, and evidence gaps

- Recursion: delegated workers are bounded subtask agents under one parent session. The frozen distribution does not establish them as independently viable recursive organizations with their own complete metasystems.
- Variety attenuation/amplification: context compaction/truncation, tool exposure policies, read-only worker belts and strategy menus attenuate presented/action variety; tools, memory retrieval and delegated research amplify operational response capacity. These mechanisms are classified by the functions they actually close rather than by the generic variety language.
- Escalation: mutation approval and verification pushback are local operational exception paths. No evidence promotes them to S3/S5 solely because a human or gate can stop work.
- Evidence gaps: no material gap forces `?` at the reviewed boundary. The strongest adjacent uncertainty—the external `refinery` self-improvement organization—is explicitly outside the frozen Carbon distribution by repository authority.

## Assessment summary

Carbon closes autonomous S1 through its mature first-party coding model/tool loop. Rich orchestration and subagent machinery remains bounded delegation without a demonstrated inter-S1 disturbance/coordination loop, so S2 is absent; task planning, approval and local limits do not form whole-system S3. Carbon does expose a genuine S3* constructor: a separately shipped fresh-process assertion verifier can challenge model-produced candidate code using execution evidence, but the independent audit criterion and consequential authority still require downstream composition. Durable memory and the editable strategy surface do not establish S4 because Carbon explicitly keeps the propose/evaluate/release self-improvement loop in the external `refinery` consumer. Policies, approval gates and immutable config rules constrain execution without providing S5 identity/ultimate-policy closure.

Proposed vector: **`A · — · — · C · — · —`**.

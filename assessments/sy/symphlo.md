---
harness_id: symphlo
project_name: Symphlo
repository: https://github.com/huisezhiyin/symphlo
review_ref: 47c4975f1689c18334ad99252a0eb575e05c7958
reviewed_at: 2026-10-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Symphlo

## Review boundary

- System in focus: one durable task/Flow and its agent work nodes in the shipped Local Alpha runtime.
- Purpose and identity: produce an accepted deliverable through explicit bounded agent turns, persisted context, evaluation and recoverable handoffs.
- Relevant environment: task inputs, user-installed agent executables, local workspace, capability processes, failed or rejected outputs and the local operator.
- Standard-distribution boundary: installable Python/desktop Local Alpha with first-party Codex and OpenCode presets, saved linear Flows and supported console/API recovery. The deterministic demo is a separate non-agent mode.
- Credited operating / distribution surfaces: src/symphlo runtime, executors, workspace, store, capability/evaluation adapters and shipped local console.
- Adjacent first-party surfaces excluded from ownership: development QwenWork evaluations, fake-agent test fixtures, fictional deterministic writing/session demo, CI, project vision and contributor instructions; separate Clerklet/Personal Assistant clients do not donate owners.
- First-party operating / deployment modes considered: Codex/OpenCode agent-backed Flow, user-configured command/session capability, local operator control and deterministic demo. Inclusion rests on the real preset route, not the fixture.
- Recursion level: one complete durable task over bounded production work cells; no autonomous workspace portfolio or recursive viable agent organization inferred.
- Reviewed revision: 47c4975f1689c18334ad99252a0eb575e05c7958.
- Observation date: 2026-10-30.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The Python runtime validates an immutable linear Flow, admits effect scope and executes its nodes in order. Each executor receives accepted context, instruction, cancellation and optional session identity. Real presets invoke a user-installed Codex CLI or managed OpenCode process; model choices inside the bounded writing/research/editing turn are opaque to the outer runtime. Outputs become durable context, events and artifacts. The zero-credential sample instead runs deterministic fixtures and is not evidence of agent autonomy. Session groups preserve conversation identity where supported. SQLite-backed evidence, executor fingerprints, exact Flow hashes, evaluation rejection and same-Flow forks support reproducibility and recovery. The operator can inspect the entire task, cancel active work and select a repair boundary while retaining accepted preceding work. Agent execution is not bundled with a provider account and does not prove quality.

Evidence: [README.md](https://github.com/huisezhiyin/symphlo/blob/47c4975f1689c18334ad99252a0eb575e05c7958/README.md#L62-L99), [src/symphlo/executors.py](https://github.com/huisezhiyin/symphlo/blob/47c4975f1689c18334ad99252a0eb575e05c7958/src/symphlo/executors.py#L311-L488), [src/symphlo/runtime.py](https://github.com/huisezhiyin/symphlo/blob/47c4975f1689c18334ad99252a0eb575e05c7958/src/symphlo/runtime.py#L94-L174), [src/symphlo/runtime.py](https://github.com/huisezhiyin/symphlo/blob/47c4975f1689c18334ad99252a0eb575e05c7958/src/symphlo/runtime.py#L176-L310), [src/symphlo/workspace.py](https://github.com/huisezhiyin/symphlo/blob/47c4975f1689c18334ad99252a0eb575e05c7958/src/symphlo/workspace.py#L958-L1005).

## Operational model

Agent-backed drafting, reviewing and revision nodes produce the task's substantive output. The runtime chooses sequence from the authored Flow; the model decides the content/interpretation of each bounded task and consumes preceding results. Flow authors select structure, effects and executor bindings. At the task recursion, an operator can regulate the whole work commitment through evidence-informed cancellation and selective rerun. This parent current-control path is distinguished from a model-owned orchestrator. A deterministic-only Flow would not satisfy agentic S1.

## S1 — Operations

- State: A
- Function: transform accepted task context into substantive research, drafts, editorial judgments and revised deliverables.
- Disturbance / variety regulated: varying user inputs, content ambiguity, preceding draft defects and required principles.
- Decisive decision or feedback right: choose the substantive output and revisions within the bounded node instruction.
- Decision owner: model-backed Codex/OpenCode participant reached through the first-party preset; not the deterministic writing fixture.
- Supporting / enforcement mechanisms: immutable Flow, subprocess/HTTP adapter, timeouts, effect authorization, accepted-result parsing, store and context links.
- Closure path: executor output is persisted, supplied to the next node and ultimately published as the task artifact; a revision receives the accepted review.
- Boundary reachability: the console compiler calls agent_preset_executor for a non-deterministic preset; CommandAgentExecutor builds the bounded prompt and actually invokes the selected CLI. No custom agent wiring is required for these presets.
- Why this is / is not agent-owned: the runtime fixes who/when and validates output shape; it cannot produce the same discretionary writing/revision choices without the agent.
- Evidence: [src/symphlo/workspace.py](https://github.com/huisezhiyin/symphlo/blob/47c4975f1689c18334ad99252a0eb575e05c7958/src/symphlo/workspace.py#L981-L993), [src/symphlo/executors.py](https://github.com/huisezhiyin/symphlo/blob/47c4975f1689c18334ad99252a0eb575e05c7958/src/symphlo/executors.py#L350-L443), [src/symphlo/executors.py](https://github.com/huisezhiyin/symphlo/blob/47c4975f1689c18334ad99252a0eb575e05c7958/src/symphlo/executors.py#L459-L576), [src/symphlo/runtime.py](https://github.com/huisezhiyin/symphlo/blob/47c4975f1689c18334ad99252a0eb575e05c7958/src/symphlo/runtime.py#L227-L310).
- Basis: structural.
- Confidence: high for supported source path.
- Caveats: installing/authenticating the external preset is required; no live provider run or content-quality claim is made. Generic external clients are not independently credited.

## S2 — Coordination

- State: —
- Function: sought specific attenuation of interference among distinct operational units.
- Disturbance / variety regulated: potential clobbering between concurrent work cells, rather than ordinary ordered input handoff.
- Decisive decision or feedback right: no shipped agent/constructor arbitration of such an inter-unit disturbance is established.
- Decision owner: authored linear order and deterministic workspace run lock; no S2 owner credited.
- Supporting / enforcement mechanisms: node input_from, accepted context, session groups and one-active-Run guard.
- Closure path: sequential results feed later nodes, but this alone does not constitute a specific inter-S1 coordination loop.
- Why this is / is not agent-owned: no model selects a conflict response across simultaneously autonomous production lanes in this boundary.
- Evidence: [src/symphlo/runtime.py](https://github.com/huisezhiyin/symphlo/blob/47c4975f1689c18334ad99252a0eb575e05c7958/src/symphlo/runtime.py#L185-L238), [src/symphlo/workspace.py](https://github.com/huisezhiyin/symphlo/blob/47c4975f1689c18334ad99252a0eb575e05c7958/src/symphlo/workspace.py#L541-L561), [src/symphlo/workspace.py](https://github.com/huisezhiyin/symphlo/blob/47c4975f1689c18334ad99252a0eb575e05c7958/src/symphlo/workspace.py#L684-L712), [src/symphlo/contracts.py](https://github.com/huisezhiyin/symphlo/blob/47c4975f1689c18334ad99252a0eb575e05c7958/src/symphlo/contracts.py#L47-L69).
- Basis: structural bounded negative.
- Confidence: high.
- Caveats: generic dependency/session primitives could support a future coordinator but do not establish S2=C.

### Absence scope

- Surfaces inspected: Flow contracts, sequential runtime execution, workspace active-run guard, session topology, executor dispatch and cancellation tests.
- Plausible first-party paths checked: accepted-context handoff, single-run lock, shared session reuse and evaluation repair. These serialize or validate one Flow rather than resolve a concrete conflict among distinct S1 units.
- Why no material first-party path remains: the shipped linear task boundary has no specific inter-unit interference/response witness; generic sequencing and preventing a second entire Run do not supply a function-specific S2 constructor.

## S3 — Inside-and-now control

- State: P
- Function: regulate the whole current task commitment after failed/rejected work, preserving valid work while choosing what must be repeated or stopped.
- Disturbance / variety regulated: a rejected intermediate result threatens downstream publication, or current execution should be interrupted and recovered from a selected boundary.
- Decisive decision or feedback right: decide whether to continue the task through a child Run and which node/prefix to retain or repeat; cancel active whole-task execution when warranted.
- Decision owner: legitimate local workspace operator using the shipped Runs/console recovery interface.
- Supporting / enforcement mechanisms: run/node/evidence projections, rejection events, cancellation token, exact Flow/executor checks, ForkSeed and persisted prefix reuse.
- Closure path: operator inspects task-wide node/evidence state, selects from_node_id, and fork_console_run admits a new execution that reuses the chosen accepted prefix and reruns remaining production. Cancellation reaches the active process token. Runtime enforcement does not select the operator's repair commitment.
- Boundary reachability: shipped workspace and console/API expose evidence, cancellation and same-Flow fork without an external custom controller.
- Why this is / is not agent-owned: no built-in agent decides the whole-task intervention/reuse boundary; the parent owns that discretion. This is broader than a generic kill button because evidence-informed selective recovery changes the allocation of remaining task work.
- Whole-system current view: complete Run status, all node states, events, accepted context and artifacts for this task.
- Current-control decision scope: abandon current execution or recommit selected failed/downstream nodes while preserving accepted upstream work, at the declared task recursion.
- Evidence: [README.md](https://github.com/huisezhiyin/symphlo/blob/47c4975f1689c18334ad99252a0eb575e05c7958/README.md#L324-L345), [src/symphlo/workspace.py](https://github.com/huisezhiyin/symphlo/blob/47c4975f1689c18334ad99252a0eb575e05c7958/src/symphlo/workspace.py#L453-L561), [src/symphlo/workspace.py](https://github.com/huisezhiyin/symphlo/blob/47c4975f1689c18334ad99252a0eb575e05c7958/src/symphlo/workspace.py#L728-L751), [src/symphlo/runtime.py](https://github.com/huisezhiyin/symphlo/blob/47c4975f1689c18334ad99252a0eb575e05c7958/src/symphlo/runtime.py#L70-L92).
- Basis: structural and explicit operator recovery.
- Confidence: medium.
- Caveats: exact same-Flow forks require a terminal parent and cannot change executor or cross session-group boundaries. This is not autonomous priority/resource bargaining, workspace-wide portfolio management or unrestricted Flow redesign.

## S3* — Complementary audit

- State: —
- Function: sought complementary independently governed access capable of challenging ordinary operational claims.
- Disturbance / variety regulated: misleading success/content claims from production.
- Decisive decision or feedback right: no distinct first-party independent audit owner/path beyond routine flow evaluation is established.
- Decision owner: ordinary configured reviewer/evaluator or operator; no S3* owner credited.
- Supporting / enforcement mechanisms: read-only evaluation capability, pass/fail parsing, publication gate, stored evidence and cross-run comparison.
- Closure path: failed routine evaluation stops downstream nodes and offers repair; that is ordinary production acceptance, not by itself complementary audit.
- Why this is / is not agent-owned: separating a review node or making it read-only does not establish an independently governed alternative channel to operational reality.
- Evidence: [src/symphlo/runtime.py](https://github.com/huisezhiyin/symphlo/blob/47c4975f1689c18334ad99252a0eb575e05c7958/src/symphlo/runtime.py#L239-L296), [README.md](https://github.com/huisezhiyin/symphlo/blob/47c4975f1689c18334ad99252a0eb575e05c7958/README.md#L324-L345), [src/symphlo/maintenance.py](https://github.com/huisezhiyin/symphlo/blob/47c4975f1689c18334ad99252a0eb575e05c7958/src/symphlo/maintenance.py#L21-L72).
- Basis: structural bounded negative.
- Confidence: medium-high.
- Caveats: an operator could compose an independent auditor using capabilities, but general executor extensibility does not establish a shipped S3*-specific construction path.

### Absence scope

- Surfaces inspected: evaluation task contract and gate, capability executors, stored evidence, run comparison/stability reports, demo review and tests.
- Plausible first-party paths checked: separate review-draft node, read-only evaluator, cross-run comparison and manual recovery; each uses ordinary accepted task results/reporting without a complementary audit regime.
- Why no material first-party path remains: no first-party audit selection, independent access/authority and returned audit judgment are wired beyond routine quality gates; development evaluations belong to an adjacent system.

## S4 — Outside-and-then intelligence

- State: —
- Function: sought an external/prospective adaptation loop returning options to current capability.
- Disturbance / variety regulated: future inadequacy of a Flow or executor in a changed environment.
- Decisive decision or feedback right: no shipped external sensing/options/adoption loop is established.
- Decision owner: human can author flows/capabilities; this alone does not close S4 parent governance.
- Supporting / enforcement mechanisms: run comparison, stability projections, saved capabilities and editable Flow definitions.
- Closure path: same-Flow recovery repeats work; it does not itself develop externally informed future capability options.
- Why this is / is not agent-owned: internal task research or editorial planning is the operational transformation, and retrospective comparison is not prospective intelligence.
- Evidence: [src/symphlo/maintenance.py](https://github.com/huisezhiyin/symphlo/blob/47c4975f1689c18334ad99252a0eb575e05c7958/src/symphlo/maintenance.py#L21-L72), [src/symphlo/maintenance.py](https://github.com/huisezhiyin/symphlo/blob/47c4975f1689c18334ad99252a0eb575e05c7958/src/symphlo/maintenance.py#L265-L299), [src/symphlo/workspace.py](https://github.com/huisezhiyin/symphlo/blob/47c4975f1689c18334ad99252a0eb575e05c7958/src/symphlo/workspace.py#L453-L481), [README.md](https://github.com/huisezhiyin/symphlo/blob/47c4975f1689c18334ad99252a0eb575e05c7958/README.md#L324-L339).
- Basis: structural bounded negative.
- Confidence: medium-high.
- Caveats: development vision/benchmark reports cannot supply runtime S4 for a user's task.

### Absence scope

- Surfaces inspected: maintenance reports, capability discovery, Flow authoring, fork constraints, production research node and README supported/future boundaries.
- Plausible first-party paths checked: stability-triggered redesign, capability replacement, same-Flow fork, model research nodes and companion recommendations. No supported externally prospective options-to-adoption loop is specified.
- Why no material first-party path remains: reporting informs a user but supplies no function-specific external/future feedback contract; hypothetical new flows and adjacent development studies do not close this task's S4.

## S5 — Policy and identity

- State: —
- Function: sought runtime identity/ultimate-policy resolution at the task recursion.
- Disturbance / variety regulated: possible tension between task purpose, present delivery and a future adaptation option.
- Decisive decision or feedback right: no first-party identity-level escalation/authoritative-return path is established.
- Decision owner: operator sets task/Flow inputs and approves effects; no S5 mode inferred from those ordinary rights.
- Supporting / enforcement mechanisms: immutable Flow hash, declared effects, approval challenge and input constraints.
- Closure path: effect authorization permits a particular execution scope, not an identity-level decision returned after S3/S4 tension.
- Why this is / is not agent-owned: neither static contracts nor an ordinary run approval owns ultimate organizational policy.
- Evidence: [src/symphlo/runtime.py](https://github.com/huisezhiyin/symphlo/blob/47c4975f1689c18334ad99252a0eb575e05c7958/src/symphlo/runtime.py#L94-L138), [src/symphlo/contracts.py](https://github.com/huisezhiyin/symphlo/blob/47c4975f1689c18334ad99252a0eb575e05c7958/src/symphlo/contracts.py#L47-L69), [README.md](https://github.com/huisezhiyin/symphlo/blob/47c4975f1689c18334ad99252a0eb575e05c7958/README.md#L379-L414).
- Basis: structural bounded negative.
- Confidence: high.
- Caveats: project-maintainer governance and independent clients' authority are outside the assessed task boundary.

### Absence scope

- Surfaces inspected: task/Flow authoring, effect authorization, immutable admission, cancellation/fork controls, local console/API and contributor surfaces.
- Plausible first-party paths checked: approval challenge, task goal edit, cancellation, client-confirmed plan and Flow replacement; these are setup or operational permissions without identity-level escalation and return.
- Why no material first-party path remains: the supported task runtime regulates a previously authored contract, with no ultimate-policy dispute resolution loop. Human authorship alone does not establish P.

## Recursion

Nodes are bounded work units, not proven recursively viable systems. External agent internals and separate clients are not assessed as Symphlo-owned metasystem functions. Parent current control is local to the one task, not the OSS development organization.

## Variety and escalation

Bounded instructions and accepted context attenuate accumulated session state; model discretion handles content variety. Errors, rejection and cancellation retain evidence and stop publication. Operator recovery preserves accepted prefixes. These status/events do not independently establish an algedonic channel or additional S-function.

## Evidence gaps

Source-first, frozen-revision review; no live provider/agent E2E was executed. Deterministic native tests: runtime 7/7, agent presets 4/4, evaluation gate 2/2 and cancellation 1/1 passed using fixtures/mocks. These verify contracts, not provider cognition or production quality. Parent S3 is limited to the evidenced local task-wide recovery route; no portfolio autonomy or additional parent functions are inferred.

---
harness_id: codeagent
project_name: CodeAgent
repository: https://github.com/WSH-4380/CodeAgent
review_ref: 0ca84f16e5c4c09675d9d91be334a203bb672bb2
reviewed_at: 2026-10-02
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-02
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# CodeAgent

## Review boundary

- System in focus: the first-party `WSH-4380/CodeAgent` local C++ coding-agent runtime at frozen revision `0ca84f16e5c4c09675d9d91be334a203bb672bb2`, including its model/tool loop, strict action protocol, sandboxed filesystem tools, task-progress state, bounded in-run history/chunk memory, read-budget breaker, annotation-plan merge/fidelity path, final-artifact verification and workspace trace logging.
- Purpose and identity: execute one natural-language coding or annotation task inside a user-selected workspace by repeatedly asking a configured model for the next structured action, executing bounded local tools, returning results to the same model actor and refusing unsupported completion claims.
- Relevant environment: the selected workspace and its files, the user task, DeepSeek Chat Completions/model inference, local filesystem state, prompt files loaded by the binary, network/API availability and the host operating system/runtime.
- Standard-distribution boundary: `main.cpp`, `tools.cpp`, `tools.h`, `systemprompt.txt`, `skill.txt` and the built binary/runtime behavior they implement are inside. DeepSeek/model inference, libcurl/nlohmann internals, CMake/build tooling, the host operating system and the target workspace/project's own governance remain dependencies/environment rather than CodeAgent organizational owners.
- Credited operating / distribution surfaces: `README_EN.md`; `README.md`; `main.cpp`; `tools.cpp`; `tools.h`; `systemprompt.txt`; `skill.txt` at the frozen revision.
- Adjacent first-party surfaces excluded from ownership: contributor/release governance, roadmap-only P0/P1/P2 items, build configuration, logs as evidence rather than decision actors, and capabilities explicitly listed as not implemented such as multi-agent, RAG, MCP, streaming and plan → execute → reflect subtask planning.
- First-party operating / deployment modes considered: normal `general` task mode and `annotation` mode through the shipped `myagent.exe <workspace> <task>` entry point, including read/search/write/create tools, read-budget enforcement, final-artifact existence verification and program-side annotation merge/fidelity checking.
- Recursion level: one CodeAgent task/run. The single model-backed agent loop is the operating S1. No standard multi-agent/team recursion is shipped at the frozen revision.
- Reviewed revision: `0ca84f16e5c4c09675d9d91be334a203bb672bb2`.
- Observation date: 2026-10-02.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

CodeAgent is intentionally a small single-agent runtime. The CLI receives a workspace and task, loads the first-party system/skill prompts, initializes task-progress state and a workspace log, then enters a bounded synchronous loop. Each turn rebuilds model context from the task, current `TaskProgress`, bounded conversation history and recent code chunks, calls DeepSeek Chat Completions directly, validates the returned strict JSON action and either dispatches a local tool, processes an annotation plan or evaluates a final response. Tool output and deterministic rejection messages are added to the same conversation so the model can revise the next action.

The first-party tool layer exposes only local list/read/read-range/write/append/create/search operations and constrains paths to the selected workspace. `TaskProgress` records the current mode, recent reads/writes and compact code excerpts. In general mode, repeated or excessive reading flips a deterministic `readBudgetExceeded`/`write` state that is fed back into later turns, discouraging endless read-only behavior. This is regulation of one task-performing S1, not coordination among distinct S1 units or whole-organization S3 management.

Completion checks are likewise task-local. A `final` action with `check_exists=true` must declare artifacts and CodeAgent verifies those paths before allowing termination; missing artifacts produce feedback and another turn. Annotation mode instead requires a structured annotation plan, merges comments programmatically into the original source and checks source fidelity. These mechanisms challenge a proposed task result deterministically inside the ordinary execution path, but no materially independent auditor actor/access path is created.

The runtime is explicitly documented as single-threaded, synchronous and stateless across runs, with no multi-agent system. Conversation history and chunk memory are bounded current-run context aids, while `log.txt` is reset for each run. The roadmap mentions richer planning/reflection and other extensions as not implemented, so they are not credited.

Primary evidence:

- [`README_EN.md`](https://github.com/WSH-4380/CodeAgent/blob/0ca84f16e5c4c09675d9d91be334a203bb672bb2/README_EN.md)
- [`main.cpp`](https://github.com/WSH-4380/CodeAgent/blob/0ca84f16e5c4c09675d9d91be334a203bb672bb2/main.cpp)
- [`tools.cpp`](https://github.com/WSH-4380/CodeAgent/blob/0ca84f16e5c4c09675d9d91be334a203bb672bb2/tools.cpp)
- [`tools.h`](https://github.com/WSH-4380/CodeAgent/blob/0ca84f16e5c4c09675d9d91be334a203bb672bb2/tools.h)
- [`systemprompt.txt`](https://github.com/WSH-4380/CodeAgent/blob/0ca84f16e5c4c09675d9d91be334a203bb672bb2/systemprompt.txt)

## Operational model

A normal run places one model-backed actor inside a first-party ReAct-like feedback loop. The actor chooses from the allowed local actions using the current task/workspace context. CodeAgent validates the protocol, dispatches the selected tool inside the workspace boundary, updates `TaskProgress`, compresses and records relevant results, then places that evidence back into the next model request. The actor continues until it produces an admissible final result or the deterministic turn/retry guards terminate the run.

Read-budget, artifact-existence and annotation-fidelity checks alter subsequent behavior by returning ordinary task feedback to that same actor. They materially improve reliability but do not introduce another operating unit, a whole-system controller, a complementary independent audit channel, prospective organizational adaptation or ultimate-policy ownership.

## S1 — Operations

- State: A
- Function: perform environment-facing code understanding/editing or annotation work for the user-selected workspace by choosing local tool actions, observing their results and iterating toward a task result.
- Disturbance / variety regulated: heterogeneous repository/file contents, incomplete task information, search/read results, filesystem/tool failures, model uncertainty, missing claimed artifacts and source-fidelity constraints encountered during the current coding task.
- Decisive decision or feedback right: choose the next structured `tool`, `annotation_plan` or admissible `final` action, including which workspace evidence to inspect or mutate, and revise that choice after returned tool/verification feedback.
- Decision owner: the model-backed agent actor reached through CodeAgent's shipped synchronous loop and first-party action protocol.
- Supporting / enforcement mechanisms: strict JSON action validation; seven workspace-scoped tools; `TaskProgress`; bounded conversation/chunk context; read-budget breaker; turn/retry limits; artifact-existence checks; annotation-plan merge/fidelity verification; workspace trace logging.
- Closure path: CLI task/workspace → first-party context assembly → direct model call → model chooses structured action → CodeAgent validates and executes/checks the action → tool/verification result updates task state/history → the same model actor receives the changed evidence and chooses the next action or a verified final response.
- Boundary reachability: the shipped executable directly enters this model/tool loop from `myagent.exe <workspace> <task>`; no application-authored orchestration layer is required to create the autonomous operating actor.
- Why this is / is not agent-owned: removing the model-backed actor leaves deterministic parsing, sandboxing, counters and verification logic but no component that chooses open-ended task-specific reads, edits, annotations or completion strategy.
- Evidence: [`README_EN.md`](https://github.com/WSH-4380/CodeAgent/blob/0ca84f16e5c4c09675d9d91be334a203bb672bb2/README_EN.md); [`main.cpp`](https://github.com/WSH-4380/CodeAgent/blob/0ca84f16e5c4c09675d9d91be334a203bb672bb2/main.cpp); [`systemprompt.txt`](https://github.com/WSH-4380/CodeAgent/blob/0ca84f16e5c4c09675d9d91be334a203bb672bb2/systemprompt.txt); [`tools.cpp`](https://github.com/WSH-4380/CodeAgent/blob/0ca84f16e5c4c09675d9d91be334a203bb672bb2/tools.cpp).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: model inference is an external dependency. The assessment credits CodeAgent for the standard first-party role/protocol/tool loop that operationally closes S1, not for provider internals.

## S2 — Coordination

- State: —
- Function: no material first-party coordination loop among distinct simultaneously active CodeAgent S1 units is implemented.
- Disturbance / variety regulated: not established at S2 level.
- Decisive decision or feedback right: not established. The frozen distribution documents one synchronous single-threaded agent loop and explicitly states that multi-agent support is absent.
- Decision owner: not established.
- Supporting / enforcement mechanisms: workspace sandboxing, sequential action dispatch, read-budget counters and task history regulate one S1; they are not inter-S1 interference attenuation.
- Closure path: not applicable; no distinct-S1 disturbance → attenuation relation → changed subsequent S1 behavior path exists in the standard distribution.
- Why this is / is not agent-owned: there is no first-party population of concurrent operating agents from which an S2 owner or constructor relation could be derived.
- Evidence: [`README_EN.md`](https://github.com/WSH-4380/CodeAgent/blob/0ca84f16e5c4c09675d9d91be334a203bb672bb2/README_EN.md); [`main.cpp`](https://github.com/WSH-4380/CodeAgent/blob/0ca84f16e5c4c09675d9d91be334a203bb672bb2/main.cpp).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: filesystem containment can reduce interference with unrelated external processes, but that is not a coordination function among first-party S1 units.

### Absence scope

- Surfaces inspected: documented architecture and limitations; main synchronous turn loop; task-progress/read-budget state; local tool dispatch; workspace sandbox; annotation path; roadmap.
- Plausible first-party paths checked: parallel/multi-agent execution; shared-work arbitration; concurrent tool execution; task queues; worker pools; separate coordinating processes; annotation/general mode interaction.
- Why no material first-party path remains: the repository explicitly defines the runtime as single-threaded and synchronous, says multi-agent is not implemented, and contains no second first-party operating loop or inter-S1 feedback relation at the frozen ref.

## S3 — Inside-and-now control

- State: —
- Function: no material first-party whole-organization current-regulation function exists above the single task-performing S1.
- Disturbance / variety regulated: not established at S3 level.
- Decisive decision or feedback right: not established. `TaskProgress`, read-budget forcing, retries, turn limits and completion checks constrain the current task loop but do not manage a wider population of S1 commitments, resources or priorities.
- Decision owner: not established.
- Supporting / enforcement mechanisms: task mode detection; `TaskProgress`; read/write counters; max-turn/retry guards; action validation; sandbox and completion verification.
- Closure path: not applicable; observed control returns to the same operating S1 and never forms a separate whole-current organizational management cycle.
- Why this is / is not agent-owned: the model can decide its own next task action, while deterministic guards can force/reject local behavior. Neither becomes a higher-recursion manager with a whole-system current view and substantive reallocation/commitment authority.
- Evidence: [`README_EN.md`](https://github.com/WSH-4380/CodeAgent/blob/0ca84f16e5c4c09675d9d91be334a203bb672bb2/README_EN.md); [`main.cpp`](https://github.com/WSH-4380/CodeAgent/blob/0ca84f16e5c4c09675d9d91be334a203bb672bb2/main.cpp).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: this absence distinguishes task-loop regulation from the stronger S3 organizational-control function.

### Absence scope

- Surfaces inspected: `TaskProgress`; general/annotation mode selection; read-budget breaker; retry/turn limits; final-artifact validation; action protocol; tool/sandbox state; trace logging.
- Plausible first-party paths checked: current progress monitoring; forced transition from read to write; retry escalation; whole-workspace artifact checking; mode-specific control; operator/runtime state.
- Why no material first-party path remains: every located control mechanism either constrains the one S1's current task or mechanically enforces preselected limits. No separate whole-system state projection or managerial decision scope exists.

## S3* — Complementary audit

- State: —
- Function: no materially independent complementary audit/challenge path with its own access boundary and corrective return is implemented.
- Disturbance / variety regulated: not established at S3* level.
- Decisive decision or feedback right: not established. Artifact-existence and annotation-fidelity checks deterministically validate task claims in the ordinary execution path; they do not constitute an independent auditor that forms a judgment from complementary access.
- Decision owner: not established.
- Supporting / enforcement mechanisms: strict action parsing; declared-artifact existence checks; program-side annotation merge; byte/source fidelity verification; workspace log.
- Closure path: not applicable at S3*. A failed deterministic check returns feedback to the same S1 loop, with no separate audit actor/channel and no independent audit verdict feeding a higher control function.
- Why this is / is not agent-owned: the checks can reject an S1 completion claim, but they evaluate fixed predicates using the same runtime state rather than exercising complementary audit discretion or independent evidence access.
- Evidence: [`README_EN.md`](https://github.com/WSH-4380/CodeAgent/blob/0ca84f16e5c4c09675d9d91be334a203bb672bb2/README_EN.md); [`main.cpp`](https://github.com/WSH-4380/CodeAgent/blob/0ca84f16e5c4c09675d9d91be334a203bb672bb2/main.cpp); [`systemprompt.txt`](https://github.com/WSH-4380/CodeAgent/blob/0ca84f16e5c4c09675d9d91be334a203bb672bb2/systemprompt.txt).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: strong deterministic verification is credited as S1 support/enforcement, not promoted to S3* without material complementary independence.

### Absence scope

- Surfaces inspected: final-result artifact verification; annotation-plan merge/fidelity checker; strict JSON/action validation; workspace trace; retry path; task history and tool results.
- Plausible first-party paths checked: independent verifier agent; secondary model/reviewer; separate audit data path; post-run challenge; mutation review; deterministic anti-hallucination checks.
- Why no material first-party path remains: all located verification executes inside the ordinary single-agent control path over the same workspace/state and returns fixed-predicate failures directly to that S1; no independent challenge role/access path remains.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material outside-and-then organizational intelligence/adaptation loop is implemented.
- Disturbance / variety regulated: not established at S4 level.
- Decisive decision or feedback right: not established. CodeAgent can inspect current workspace evidence and retain bounded current-run history/chunks, but it does not scan an external future environment, form adaptation options and change durable organizational capability/strategy.
- Decision owner: not established.
- Supporting / enforcement mechanisms: fixed-window conversation history; recent chunk memory; task-progress notes; current workspace search/read tools; model reasoning within the current task.
- Closure path: not applicable; no prospective distinction → adaptation-option formation → capability/strategy change → return-to-present organization path exists.
- Why this is / is not agent-owned: immediate task replanning from new tool evidence is S1 adaptation. The documented state is stateless across runs, `log.txt` is reset each run, and roadmap-only plan → execute → reflect work is explicitly not implemented.
- Evidence: [`README_EN.md`](https://github.com/WSH-4380/CodeAgent/blob/0ca84f16e5c4c09675d9d91be334a203bb672bb2/README_EN.md); [`main.cpp`](https://github.com/WSH-4380/CodeAgent/blob/0ca84f16e5c4c09675d9d91be334a203bb672bb2/main.cpp).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: bounded memory inside one task improves context continuity but does not satisfy S4's prospective organizational adaptation threshold.

### Absence scope

- Surfaces inspected: history window; chunk memory; task-progress notes; current workspace search; model/context assembly; task modes; logging; documented roadmap and limitations.
- Plausible first-party paths checked: persistent learning across runs; external trend/environment scan; strategic option generation; self-modification; model/tool reconfiguration; reflective planning; durable capability promotion.
- Why no material first-party path remains: located memory is current-run context, the runtime is documented as stateless, and prospective/reflection capabilities appear only in the not-implemented roadmap rather than a shipped feedback loop.

## S5 — Identity / ultimate policy

- State: —
- Function: no material first-party ultimate identity/policy closure is implemented.
- Disturbance / variety regulated: not established at S5 level.
- Decisive decision or feedback right: not established. Workspace boundaries, allowed tools, action schemas, task mode, model endpoint and turn/retry limits are hard-coded or operator/runtime supplied constraints rather than an autonomously owned decision about organizational identity or ultimate policy.
- Decision owner: not established inside CodeAgent; ultimate task/policy boundaries remain user/developer/configuration owned.
- Supporting / enforcement mechanisms: `systemprompt.txt`; `skill.txt`; fixed tool allowlist; workspace sandbox; general/annotation protocol; hard-coded model/endpoint; deterministic limits.
- Closure path: not applicable; CodeAgent enforces its supplied operating contract but does not itself decide or reconcile what its ultimate purpose/identity/policy should be and return that decision to operations.
- Why this is / is not agent-owned: the model actor operates within the supplied system prompt/protocol and can choose task actions, but it cannot authoritatively redefine the ultimate operating boundary, allowed capability set or organizational purpose.
- Evidence: [`systemprompt.txt`](https://github.com/WSH-4380/CodeAgent/blob/0ca84f16e5c4c09675d9d91be334a203bb672bb2/systemprompt.txt); [`README_EN.md`](https://github.com/WSH-4380/CodeAgent/blob/0ca84f16e5c4c09675d9d91be334a203bb672bb2/README_EN.md); [`main.cpp`](https://github.com/WSH-4380/CodeAgent/blob/0ca84f16e5c4c09675d9d91be334a203bb672bb2/main.cpp).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: policy enforcement and sandboxing are substantial safety mechanisms but do not transfer ultimate-policy ownership to an S5 actor.

### Absence scope

- Surfaces inspected: system/skill prompts; tool allowlist; workspace containment; task-mode detection; action protocol; model/endpoint configuration; retry/turn limits; final/annotation completion rules.
- Plausible first-party paths checked: model-led mode/policy revision; dynamic tool authorization; self-authored system policy; identity-goal reconciliation; autonomous provider/model selection; persistent constitutional state.
- Why no material first-party path remains: the authoritative operating constraints are fixed in code/prompts or supplied by the user/developer, and no first-party actor owns a runtime ultimate-policy/identity decision loop.

## Assessment summary

CodeAgent closes one clear autonomous S1 through its shipped model/tool feedback loop. Its deterministic read-budget, sandbox, artifact-existence and annotation-fidelity mechanisms improve the reliability of that S1 but do not establish additional VSM functions. The frozen distribution is explicitly single-threaded, synchronous and without multi-agent support, so no S2 or whole-system S3 path exists; verification lacks complementary independence for S3*; bounded current-run memory and task adaptation do not establish prospective S4; and hard-coded/operator-supplied policy remains outside autonomous S5 ownership.

Proposed vector: **`A · — · — · — · — · —`**.

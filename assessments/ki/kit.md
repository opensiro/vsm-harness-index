---
harness_id: kit
project_name: Kit
repository: https://github.com/speakeasy-api/kit
review_ref: 3fd1fd5fda269569ceba0c2dd884c988d31f53d0
reviewed_at: 2026-10-16
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Kit

## Review boundary

- System in focus: Kit's first-party installed Rust coding-agent runtime at frozen `3fd1fd5fda269569ceba0c2dd884c988d31f53d0`; one local/remote-protocol coding session with optional model-directed Runlet Compose calls and internal subagent sessions.
- Purpose and identity: provide model-directed repository work through one compositional executable tool, session persistence and optional delegated child work.
- Relevant environment: shell/file system, selected model provider, active project root, Runlet program evaluations, direct and ACP child sessions, TUI and durable transcript storage.
- Standard-distribution boundary: first-party `kit` Rust binary, native runtime and tool registry, Compose Runlet integration, file/shell/edit tools, built-in `acp.kit` child harness, first-party session management and ACP/A2A/TUI clients. Runlet and AgentKit libraries are explicit protocol/engine dependencies, not independent external code-agent ownership.
- Credited operating / distribution surfaces: shipped `Runtime.run_persistent_inner` and `Agent::builder` with the first-party Compose tool source, modeled `compose` program/tool-result cycle, internal Kit subagents with generation-aware continuation/forking, append-only durable session snapshots and local file tools.
- Adjacent first-party surfaces excluded from ownership: external Claude/Codex/Cursor ACP child runtimes and their model/tool loops, optional downloaded plugins/skills/MCP servers, benchmarks, project CI and release process, model weights or hosted Speakeasy AI Control Plane. External TypeSafe Jev scoring tool is a callable option, not a mandatory reviewer/org gate by itself.
- First-party operating / deployment modes considered: ordinary TUI, `kit prompt`, ACP and A2A routes to Kit's local runtime; optional `acp.kit` child work, persistent/forkable child sessions, concurrent Compose programs. No live model inference or audited child behavior was executed in this source-first review.
- Recursion level: one Kit-managed local coding session and its optional first-party child session operations; no other vendor's agent or controlling external organization is imported into the assessed system.
- Reviewed revision: `3fd1fd5fda269569ceba0c2dd884c988d31f53d0`, pinned from Index intake #379.
- Observation date: 2026-10-16.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Kit implements a first-party coding runtime in `src/runtime.rs`. `run_persistent_inner` opens durable sessions, creates a selected model adapter and first-party tools/Compose source, builds an `agentkit-loop` engine `Agent`, calls `start`, and drives it with `drive_with_tasks`. The imported AgentKit core supplies the generic loop machinery; Kit owns the deployed tool registry, user-facing session lifecycle, Compose orchestration and source-specific work rights ([src/runtime.rs](https://github.com/speakeasy-api/kit/blob/3fd1fd5fda269569ceba0c2dd884c988d31f53d0/src/runtime.rs), [Cargo.toml](https://github.com/speakeasy-api/kit/blob/3fd1fd5fda269569ceba0c2dd884c988d31f53d0/Cargo.toml)). `compose` runs a small Runlet program written by the model and can issue shell/read/edit, independent calls and explicit dependency/retry constructs. The Runlet package is an execution substrate, not evidence of a separately owned systems 2–5 controller ([README.md](https://github.com/speakeasy-api/kit/blob/3fd1fd5fda269569ceba0c2dd884c988d31f53d0/README.md), [src/tools/shell.rs](https://github.com/speakeasy-api/kit/blob/3fd1fd5fda269569ceba0c2dd884c988d31f53d0/src/tools/shell.rs), [src/tools/edit.rs](https://github.com/speakeasy-api/kit/blob/3fd1fd5fda269569ceba0c2dd884c988d31f53d0/src/tools/edit.rs)).

Kit's native subagent registry supports create, continue, fork and close with a per-child monotonic generation/handle check. `prompt` serializes access to one child state, rejects stale continuations and marks its lifecycle before executing; `fork` similarly protects the source session state ([src/tools/subagent.rs](https://github.com/speakeasy-api/kit/blob/3fd1fd5fda269569ceba0c2dd884c988d31f53d0/src/tools/subagent.rs), [src/tools/subagent/recovery.rs](https://github.com/speakeasy-api/kit/blob/3fd1fd5fda269569ceba0c2dd884c988d31f53d0/src/tools/subagent/recovery.rs), [src/session/children.rs](https://github.com/speakeasy-api/kit/blob/3fd1fd5fda269569ceba0c2dd884c988d31f53d0/src/session/children.rs)). These are real first-party safeguards against concurrent writes to **one child session state**, but they do not establish a qualified inter-S1 organizational S2 relation between independently competing coding divisions. Kit can also launch Claude/Codex/Cursor via ACP, but those child coding capabilities are explicitly external and receive no attribution as Kit-owned operating units in this assessment.

An optional first-party `eval` tool submits user/model-provided independent questions to an external TypeSafe service; responses are tool results, not an installed separately assigned auditor that automatically verifies code changes and binds disposition into current/repair control. Session persistence/compaction and user-selected model/provider changes improve continuity, not a demonstrated outside/future capability selection loop.

## Operational model

A user supplies a coding request. Kit opens/recovers a durable session, prompts a provider via an AgentKit engine with Kit's Compose-only tool registry and executes the model's Runlet program; file/shell/edit/subagent results are returned to the model for next coding decisions. The program may fan out independent calls, explicitly order dependencies, retry failures, or continue/fork a Kit child with a generation-checked handle. External ACP children retain their own ownership. No independently staffed present whole-work governance, reviewer findings-to-correction gate or future strategic intelligence lifecycle is evidenced in the credited first-party mode.

## S1 — Operations

- State: A
- Function: autonomously carry out coding tasks with model-selected Compose programs and observation-driven follow-up.
- Disturbance / variety regulated: repo discovery, edited files, tests, command failures, subprocess outputs and varying subtask context.
- Decisive decision or feedback right: select Runlet `compose` program, branches, tool operations, edits and subsequent steps according to observed results.
- Decision owner: model-directed installed Kit coding actor; imported AgentKit loop library supplies a generic executor while Kit supplies the shipped local Compose programming/tool/session runtime.
- Supporting / enforcement mechanisms: `Runtime.run_persistent_inner`, `Agent::builder` with Compose source, shell/read/edit tools, tool-run observations, durable session and user-selected model.
- Closure path: user task→Kit-created model session→model emits Compose program→Runlet and first-party local tools execute→returned output reaches model→next program or final answer.
- Boundary reachability: shipped TUI, prompt, ACP and A2A modes all use Kit's session/runtime and local tool registry.
- Why this is / is not agent-owned: adaptive next task operations are chosen by the model rather than fixed orchestration; source-specific program tool registry and observed feedback are integrated into an installed product.
- Evidence: [src/runtime.rs](https://github.com/speakeasy-api/kit/blob/3fd1fd5fda269569ceba0c2dd884c988d31f53d0/src/runtime.rs), [src/tools/mod.rs](https://github.com/speakeasy-api/kit/blob/3fd1fd5fda269569ceba0c2dd884c988d31f53d0/src/tools/mod.rs), [src/tools/shell.rs](https://github.com/speakeasy-api/kit/blob/3fd1fd5fda269569ceba0c2dd884c988d31f53d0/src/tools/shell.rs), [src/tools/edit.rs](https://github.com/speakeasy-api/kit/blob/3fd1fd5fda269569ceba0c2dd884c988d31f53d0/src/tools/edit.rs), [README.md](https://github.com/speakeasy-api/kit/blob/3fd1fd5fda269569ceba0c2dd884c988d31f53d0/README.md).
- Basis: source-backed installed agent/tool feedback, dependency-labeled.
- Confidence: high for first-party wired path; task performance not tested.
- Caveats: imported `agentkit-loop` implements generic model loop, and external ACP agent behaviors are excluded.

## S2 — Coordination

- State: —
- Function: no distinct first-party interference-specific feedback loop between separate first-party operational S1 divisions.
- Disturbance / variety regulated: parallel Compose operations could touch overlapping files; two requests to the same reusable child can race its session generation.
- Decisive decision or feedback right: separate S1 units mutually rescope, serialize conflicting work or receive a conflict-specific correction from a coordinator; not established.
- Decision owner: Compose ordering is model-authored execution programming; child registry enforces one child session's handle/generation validity; neither constitutes a distinct S2 work division coordinator.
- Supporting / enforcement mechanisms: parallel Runlet calls, `after` dependency edges, per-child mutex, monotonically checked session generations, stale-handle refusal and resource limits.
- Closure path: stale child-generation request fails rather than corrupting that one session; no observed cross-worker interference detector/relation returns to alter distinct operational S1 commitments.
- Why this is / is not agent-owned: generic concurrency control in one child object's lifecycle, explicit programming dependencies and task fan-out are insufficient for autonomous or constructor S2 over distinct S1 divisions.
- Evidence: [src/tools/subagent.rs](https://github.com/speakeasy-api/kit/blob/3fd1fd5fda269569ceba0c2dd884c988d31f53d0/src/tools/subagent.rs), [src/runtime.rs](https://github.com/speakeasy-api/kit/blob/3fd1fd5fda269569ceba0c2dd884c988d31f53d0/src/runtime.rs), [README.md](https://github.com/speakeasy-api/kit/blob/3fd1fd5fda269569ceba0c2dd884c988d31f53d0/README.md), [src/session/children.rs](https://github.com/speakeasy-api/kit/blob/3fd1fd5fda269569ceba0c2dd884c988d31f53d0/src/session/children.rs).
- Basis: bounded negative with explicitly considered generation lock.
- Confidence: moderate.
- Caveats: external user-written concurrent programs could construct coordination, and independently imported ACP agents may have their own controllers, but neither is credited to Kit's shipped organizational boundary.

### Absence scope

- Surfaces inspected: Runlet Compose, native/ACP child registry, fork/continue generation guards, session persistence and local tools.
- Plausible first-party paths checked: parallel Compose data dependencies, stale child continuation, child spawn and reuse, resource and concurrency caps.
- Why no material first-party path remains: controls protect individual execution state or deterministic dependencies, not identified conflict between distinct first-party S1 units with returned inter-S1 behavior correction.

## S3 — Inside-and-now control

- State: —
- Function: no distinct whole-system current control decision owner separate from the coding agent's task loop.
- Disturbance / variety regulated: step budget, model failure, user interruption, child depth/capacity, pending background jobs and resume state are ordinary execution disturbances.
- Decisive decision or feedback right: select whole-current organization of multiple S1 units and enforce modified operational commitments from an independent current controller; not found.
- Decision owner: user controls one session, model authors Compose programs, runtime limits/retries sessions and child concurrency; no separate privileged whole-current judgment/feedback organ.
- Supporting / enforcement mechanisms: persistent transcript and locks, cancellation, child generation/caps, TUI controls and request budgets.
- Closure path: local run cancellation or child stale-handle rejection changes a task; no whole-current multi-unit supervisory regulation, state inspection and returned new system-wide commitments.
- Why this is / is not agent-owned: Kit does not claim full organization of all connected third-party ACP agents; child task delegation, scripting and deterministic safety gates are not a distinct S3 current-control actor.
- Evidence: [src/runtime.rs](https://github.com/speakeasy-api/kit/blob/3fd1fd5fda269569ceba0c2dd884c988d31f53d0/src/runtime.rs), [src/tools/subagent.rs](https://github.com/speakeasy-api/kit/blob/3fd1fd5fda269569ceba0c2dd884c988d31f53d0/src/tools/subagent.rs), [src/session.rs](https://github.com/speakeasy-api/kit/blob/3fd1fd5fda269569ceba0c2dd884c988d31f53d0/src/session.rs), [src/request_budget.rs](https://github.com/speakeasy-api/kit/blob/3fd1fd5fda269569ceba0c2dd884c988d31f53d0/src/request_budget.rs).
- Basis: bounded negative.
- Confidence: moderate.
- Caveats: an external operator could organize many Kit instances, but that is outside this single-session assessment.

### Absence scope

- Surfaces inspected: prompt driver, Compose registry, live child tasks, session state/cancellation, request budget and TUI/ACP lifecycle.
- Plausible first-party paths checked: whole-session model allocation, multi-child orchestration, retries, generation safety, interactive controls and provider account management.
- Why no material first-party path remains: no distinct whole-current owner with superior operational choice, evidence of system-wide policy tradeoff and returned changed commitments.

## S3* — Complementary audit

- State: —
- Function: no independently assigned first-party claim-audit owner or binding findings-to-repair loop in the installed local coding session.
- Disturbance / variety regulated: false code-correctness/completion claims; ordinary model may run tests, and optional `eval` questions may inspect a state.
- Decisive decision or feedback right: independent review of producer code/claims with auditable findings and subsequent controller/repair disposition; no qualifying path shown.
- Decision owner: model using ordinary shell, externally supplied Jev `eval` questions when enabled, or externally configured ACP reviewer; none is a first-party dedicated complementary auditor for the selected task.
- Supporting / enforcement mechanisms: Compose test calls, external `EvalTool`, child prompt output schema and session history.
- Closure path: any `eval`/child result returns as a normal model tool observation with no claim-specific mandatory review gate or guaranteed accountable correction path.
- Why this is / is not agent-owned: a user/model-callable evaluator and general child role prompt are not an automatically assigned evidence-taking complementary audit owner.
- Evidence: [src/tools/eval.rs](https://github.com/speakeasy-api/kit/blob/3fd1fd5fda269569ceba0c2dd884c988d31f53d0/src/tools/eval.rs), [src/runtime.rs](https://github.com/speakeasy-api/kit/blob/3fd1fd5fda269569ceba0c2dd884c988d31f53d0/src/runtime.rs), [src/tools/subagent.rs](https://github.com/speakeasy-api/kit/blob/3fd1fd5fda269569ceba0c2dd884c988d31f53d0/src/tools/subagent.rs).
- Basis: bounded negative.
- Confidence: medium-high for the default first-party session.
- Caveats: external evaluation can still be useful to the user, but not automatically equivalent to first-party independent S3* ownership.

### Absence scope

- Surfaces inspected: optional `eval`, native tool results, child schema/fork, runtime conclusion and model session.
- Plausible first-party paths checked: tests as tools, external Jev model responses, child-harness review prompts and status transcript.
- Why no material first-party path remains: no installed differentiated audit workflow with claim-relative independent evidence access, negative verdict gate and binding accountable remedy path.

## S4 — Outside-and-then intelligence

- State: —
- Function: no separately owned external/prospective capability adaptation to future tasks.
- Disturbance / variety regulated: long context, changing model preferences and persistent task history are handled by compaction/config, not a distinct future-environment intelligence remit.
- Decisive decision or feedback right: analyze outside/long-term change, select new capabilities and return them to future operation in an owned feedback cycle; absent.
- Decision owner: operator changes provider/model/config/plugins; installed coding agent has no source-proven strategic future capability owner.
- Supporting / enforcement mechanisms: durable JSONL transcript, compaction, plugin load, model selection and Kit binary update.
- Closure path: resuming/replaying current session or installing third-party plugin does not itself establish prospective adaptation strategy with selected return to S1/S3.
- Why this is / is not agent-owned: saving memory and allowing extension installation are capability primitives, not an observed first-party external-intelligence organization.
- Evidence: [src/compaction.rs](https://github.com/speakeasy-api/kit/blob/3fd1fd5fda269569ceba0c2dd884c988d31f53d0/src/compaction.rs), [src/plugins.rs](https://github.com/speakeasy-api/kit/blob/3fd1fd5fda269569ceba0c2dd884c988d31f53d0/src/plugins.rs), [src/update.rs](https://github.com/speakeasy-api/kit/blob/3fd1fd5fda269569ceba0c2dd884c988d31f53d0/src/update.rs), [src/session.rs](https://github.com/speakeasy-api/kit/blob/3fd1fd5fda269569ceba0c2dd884c988d31f53d0/src/session.rs).
- Basis: bounded negative.
- Confidence: moderate.
- Caveats: user-created higher-level workflows could adapt Kit externally, not assessed here.

### Absence scope

- Surfaces inspected: compaction, native session resume, model switching, plugin catalog, binary update and user-configurable tools.
- Plausible first-party paths checked: context compress/resume, forked subagent exploratory branches, imported plugins, automatic library update.
- Why no material first-party path remains: no dedicated outside/future option appraisal and runtime-adopted capability modification owned by the installed harness.

## S5 — Identity and ultimate policy

- State: —
- Function: no distinct rightful organizational identity/ultimate-policy controller at this coding-session recursion.
- Disturbance / variety regulated: user/provider security requirements, tool scopes and child headless permission prompts.
- Decisive decision or feedback right: legitimate ultimate system-purpose policy adjudication with authoritative return into system operation; not proven.
- Decision owner: external user/configured security container owns task and permissions. Kit explicitly states it is **not a security boundary** and does not ship a permissions framework.
- Supporting / enforcement mechanisms: root directory choice, subagent limits, headless permission refusal and external sandbox.
- Closure path: a headless child permission prompt is rejected/failed, or environment provides a sandbox, but no whole-identity S5 decision/return.
- Why this is / is not agent-owned: rejecting risky child permissions, external environment policy and user model selection are ordinary operating constraints, not S5 legitimacy/identity authority.
- Evidence: [README.md](https://github.com/speakeasy-api/kit/blob/3fd1fd5fda269569ceba0c2dd884c988d31f53d0/README.md), [src/tools/subagent.rs](https://github.com/speakeasy-api/kit/blob/3fd1fd5fda269569ceba0c2dd884c988d31f53d0/src/tools/subagent.rs), [src/runtime.rs](https://github.com/speakeasy-api/kit/blob/3fd1fd5fda269569ceba0c2dd884c988d31f53d0/src/runtime.rs).
- Basis: bounded negative.
- Confidence: high that no distinct first-party S5 is described at this boundary.
- Caveats: an adopting external organization may govern the binary and tools as its own S5; no such parent rights are invented here.

### Absence scope

- Surfaces inspected: security/trust README, native permission handling, runtime config, child model/provider route and external plugins.
- Plausible first-party paths checked: child headless prompts, `--root` working-dir constraints, user-authored sandbox and credential configuration.
- Why no material first-party path remains: no first-party appointed ultimate-purpose policymaker or authoritative identity interpretation and return to S3/S4.

## Evidence gaps

- No model-backed live coding task, actual child generation race trial or independent audit evaluation occurred during this assessment. Verdicts are source-bound rather than measured success probabilities.
- Imported `AgentKit` and Runlet perform substantial generic engine/execution work. Kit's credited ownership concerns the shipped integrated coding system and first-party Compose/session/tool interfaces, not authorship of dependency internals.
- The generation-check concurrency guard is a real safety property, but insufficient to infer cross-S1 S2 without separate operational units and conflict-specific closure.
- External ACP harnesses and optional Jev evaluation remain excluded from first-party role/function ownership.

## Conclusion

Kit's installed model-to-Compose-to-observation loop supports autonomous S1 coding work, even though the generic engine is a pinned imported dependency. The native child-generation guard and Compose parallelism do not establish distinct inter-S1 coordination S2; no separate whole-current S3 owner, independent S3* audit path, prospective S4 or legitimate S5 policy controller is demonstrated at the credited local runtime boundary. Proposed vector: **A / — / — / — / — / —**, source-first and frozen.

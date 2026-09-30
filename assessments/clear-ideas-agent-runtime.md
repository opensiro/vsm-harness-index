---
harness_id: clear-ideas-agent-runtime
project_name: Clear Ideas Agent Runtime
repository: https://github.com/clearideas/agent-runtime
review_ref: 6abb6fa1ae2455dfe3eb86414b617e1fa84a47b1
reviewed_at: 2026-09-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-30
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Clear Ideas Agent Runtime

## Review boundary

- System in focus: one execution of the shipped Clear Ideas Agent Runtime at frozen revision `6abb6fa1ae2455dfe3eb86414b617e1fa84a47b1`, including the portable agent/run manifest, first-party core execution engine, prompt/loop/standard step executors, checkpoint/run-state machinery, execution adapters and included runtime/store/model/tool/sandbox interfaces where they are wired into normal operation.
- Purpose and identity: execute a host-defined portable agent contract reproducibly across local or remote infrastructure while allowing model-backed prompt work, bounded tools/sub-runs, dependency-safe parallelism, durable suspension/resume, budgets and host-controlled authorization.
- Relevant environment: run inputs and manifest variables; provider/model responses; tool and connection results; child/sub-run outputs; approval responses; token consumption; cancellation; adapter failures; checkpoint/run-store state; remote-worker availability; sandbox/webhook outcomes.
- Standard-distribution boundary: first-party manifests/contracts, core runtime, execution-plan builder, prompt/loop/standard executors, included local/SQLite stores, execution engines, model adapter, sandbox/runtime packages and their normal host ports are inside where shipped. External model/provider internals, MCP endpoints, host business-policy logic, host secrets/credentials, application-specific adapters and external remote infrastructure remain dependencies unless an included first-party adapter itself owns the credited decision.
- Credited operating / distribution surfaces: `README.md`; `docs/{concepts,manifests,persistence-and-recovery,production}.md`; `packages/core/src/{agent-runtime,execution-plan}.ts`; `packages/step-prompt/src/index.ts`; `packages/step-loop/src/index.ts`; `packages/step-standard/src/index.ts`; first-party execution, runtime, store, model and sandbox packages where they support the normal run lifecycle.
- Adjacent first-party surfaces excluded from ownership: repository `GOVERNANCE.md`, `SECURITY_REVIEW.md`, CI/release tooling, contributor checks/tests and package-validation scripts; documentation-site analytics; runnable examples as independent systems; example-only evaluator loops; host applications that embed the runtime; external provider/tool/connection implementations.
- First-party operating / deployment modes considered: in-process/local execution; child-process execution; remote worker execution through the shipped protocol; sequential runs; dependency-safe parallel prompt waves; tool/loop/webhook/approval/code/sub-run steps; checkpointed suspension and fresh-process resume.
- Recursion level: one runtime run is the assessed system. Model-backed prompt branches and model-backed sub-runs can serve as S1 operational units when they produce substantive task outcomes. The deterministic runtime is the current coordination/control metasystem for that run. Host/operator authority over adapters, credentials or one approval action is not silently promoted to S5 at this recursion.
- Reviewed revision: `6abb6fa1ae2455dfe3eb86414b617e1fa84a47b1`.
- Observation date: 2026-09-30.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Clear Ideas Agent Runtime is a provider-neutral TypeScript runtime built around versioned agent manifests and invocation-specific run manifests. A manifest declares variables, model references, steps, limits and metadata; the host resolves provider/connection/infrastructure adapters and starts a run. The core runtime resolves dependencies, executes registered step executors, maintains durable run state and transcript, emits ordered events and checkpoints committed progress.

The runtime deliberately separates substantive model work from deterministic orchestration. Prompt steps can call a model and tools, while the core chooses execution waves from declared data dependencies, preserves effectful/stateful work ordering, limits parallelism, validates parallel state patches and commits each parallel wave atomically in manifest order. Checkpoint attempts fence stale writers after resume, and cumulative model-token budgets can suspend a run before later continuation under a raised limit.

There is no evidenced built-in cross-run learning or identity-governance subsystem at this frozen revision. Persistence preserves run state and recovery; manifests/configuration define externally supplied contracts; telemetry observes execution. Those capabilities are not treated as S4 or S5 without an evidence-to-adaptation or ultimate-policy closure loop.

Primary evidence:

- [`README.md`](https://github.com/clearideas/agent-runtime/blob/6abb6fa1ae2455dfe3eb86414b617e1fa84a47b1/README.md)
- [`docs/concepts.md`](https://github.com/clearideas/agent-runtime/blob/6abb6fa1ae2455dfe3eb86414b617e1fa84a47b1/docs/concepts.md)
- [`docs/manifests.md`](https://github.com/clearideas/agent-runtime/blob/6abb6fa1ae2455dfe3eb86414b617e1fa84a47b1/docs/manifests.md)
- [`packages/core/src/agent-runtime.ts`](https://github.com/clearideas/agent-runtime/blob/6abb6fa1ae2455dfe3eb86414b617e1fa84a47b1/packages/core/src/agent-runtime.ts)
- [`packages/core/src/execution-plan.ts`](https://github.com/clearideas/agent-runtime/blob/6abb6fa1ae2455dfe3eb86414b617e1fa84a47b1/packages/core/src/execution-plan.ts)

## Operational model

A host submits a resolved agent or run manifest plus invocation variables and optional scheduling/budget controls. The first-party runtime validates inputs, resolves an execution plan and invokes step executors. Prompt steps use a model adapter for substantive generation and may use authorized tools. In parallel mode, only eligible tool-free prompt branches can share an execution wave; a consumer of another branch's output waits for its producer, and stateful/effectful work remains ordered. The core validates each parallel outcome's state patch, atomically commits the wave in manifest order, then exposes committed state to later work.

The runtime checkpoints before execution and after committed steps or waves. Suspension, cancellation and failure are represented in the run lifecycle. Resume verifies the manifest fingerprint, increments the attempt and fences writes from older attempts. Token usage is cumulative across attempts; exhausting a declared model-token budget suspends prompt execution, after which a later resume may provide a higher limit.

## S1 — Operations

- State: A
- Function: perform substantive model-backed task work for prompt steps or model-backed child runs and return task-specific generated output into the run state/transcript.
- Disturbance / variety regulated: changing prompt/input content, current committed variables, model responses, tool observations, structured-output requirements, intermediate transcript and task-specific content constraints.
- Decisive decision or feedback right: choose the substantive generated response and, where a prompt loop uses tools, choose model-directed tool calls and subsequent content from returned observations.
- Decision owner: model-backed prompt execution reached through the first-party `ModelAdapter`/prompt executor path.
- Supporting / enforcement mechanisms: manifest-defined prompt/system messages; model profile resolution; prompt-step executor; tool adapter; transcript; structured-output handling; token budget; checkpointed step state.
- Closure path: declared task/input + committed runtime context → prompt executor calls model-backed actor → actor generates content/tool decisions → tool/model observations return into the prompt execution → final model-backed result becomes the step output/transcript and feeds later run work.
- Boundary reachability: prompt is a built-in shipped step type and the primary public runtime path directly wires model adapters into step execution; an external orchestrator does not have to invent the model-work loop.
- Why this is / is not agent-owned: removing the model-backed actor while retaining manifests, schedulers, stores and step-lifecycle machinery leaves deterministic execution infrastructure but removes the substantive task-specific language/reasoning decision. S1 is therefore agent-owned.
- Evidence: [`README.md`](https://github.com/clearideas/agent-runtime/blob/6abb6fa1ae2455dfe3eb86414b617e1fa84a47b1/README.md); [`docs/concepts.md`](https://github.com/clearideas/agent-runtime/blob/6abb6fa1ae2455dfe3eb86414b617e1fa84a47b1/docs/concepts.md); [`packages/step-prompt/src/index.ts`](https://github.com/clearideas/agent-runtime/blob/6abb6fa1ae2455dfe3eb86414b617e1fa84a47b1/packages/step-prompt/src/index.ts); [`packages/core/src/agent-runtime.ts`](https://github.com/clearideas/agent-runtime/blob/6abb6fa1ae2455dfe3eb86414b617e1fa84a47b1/packages/core/src/agent-runtime.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: model-provider infrastructure remains externally supplied/host-selected. Credit is for the model actor reached through the shipped prompt operating loop, not for provider internals.

## S2 — Coordination

- State: C
- Function: attenuate interference among concurrently executing model-backed prompt branches so their shared run state remains deterministic and downstream S1 work consumes a coherent committed result.
- Distinct S1 units: two or more eligible model-backed prompt branches scheduled concurrently in one dependency-safe execution wave.
- Inter-S1 disturbance: branches can depend on another branch's declared output or target the same declared state key, and arbitrary concurrent state patches could race or make shared run state order-dependent; effectful/tool/stateful work would add side-effect interference if admitted to the same wave.
- Attenuating coordination relation: `buildExecutionWaves` excludes effectful/stateful/non-plain prompt steps from parallel waves, flushes a wave when a prompt reads or writes a variable produced by another current-wave step, and caps concurrency; after execution, `assertParallelWaveStatePatches` rejects a parallel outcome that mutates state outside its declared `outputVariable`; the runtime then commits the wave atomically in manifest order.
- Feedback into subsequent S1 behaviour: later dependent prompt branches receive only the ordered committed state/results after the producer wave completes; consumers are therefore delayed until the dependency has been resolved and see the coordinated output rather than a racing intermediate state.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the credited mechanism targets a specific interference created by multiple concurrent S1 prompt branches sharing one run-state namespace. It prevents conflicting/dependent writes from co-executing, limits what each concurrent branch may mutate and returns a deterministic committed state to later S1s. Credit does not come from the mere existence of a graph or queue.
- Disturbance / variety regulated: same-output-variable contention, read-after-write dependencies, arbitrary shared-state mutation from parallel branches and effectful/stateful work that would be unsafe to interleave.
- Decisive decision or feedback right: decide which prompt branches may safely co-execute, which must wait, whether a parallel state patch is admissible and the deterministic order in which wave results become authoritative run state.
- Decision owner: deterministic first-party core runtime.
- Supporting / enforcement mechanisms: dependency inspection; execution-wave builder; host/manifest concurrency ceilings; parallel state-patch validation; atomic wave checkpoint/commit; manifest-order state/result application.
- Closure path: candidate concurrent S1 prompt branches → dependency/effect/state checks construct a safe wave → branches execute → state patches are validated → wave commits atomically in manifest order → later S1s consume the resulting authoritative state, with dependent/conflicting branches having been held outside the unsafe wave.
- Boundary reachability: dependency-safe parallel scheduling and ordered wave commits are shipped core runtime behavior exposed by the normal run manifest; no consumer-authored coordination algorithm is required.
- Why this is / is not agent-owned: the model actors produce branch content but do not decide the interference policy. The core deterministically constructs waves, rejects unsafe patches and orders commits. S2 is therefore first-party constructor/runtime-owned `C`.
- Evidence: [`README.md`](https://github.com/clearideas/agent-runtime/blob/6abb6fa1ae2455dfe3eb86414b617e1fa84a47b1/README.md); [`docs/manifests.md`](https://github.com/clearideas/agent-runtime/blob/6abb6fa1ae2455dfe3eb86414b617e1fa84a47b1/docs/manifests.md); [`docs/concepts.md`](https://github.com/clearideas/agent-runtime/blob/6abb6fa1ae2455dfe3eb86414b617e1fa84a47b1/docs/concepts.md); [`packages/core/src/execution-plan.ts`](https://github.com/clearideas/agent-runtime/blob/6abb6fa1ae2455dfe3eb86414b617e1fa84a47b1/packages/core/src/execution-plan.ts); [`packages/core/src/agent-runtime.ts`](https://github.com/clearideas/agent-runtime/blob/6abb6fa1ae2455dfe3eb86414b617e1fa84a47b1/packages/core/src/agent-runtime.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: ordinary sequential manifest order is not itself the S2 witness. Credit is bounded to the shipped parallel-wave mode where several S1 prompt branches actually run concurrently and the runtime attenuates their evidenced shared-state interference.

## S3 — Inside-and-now control

- State: C
- Function: maintain current whole-run control over execution eligibility, dependency progress, resource ceilings, authoritative state, suspension/resume ownership and cancellation/failure lifecycle.
- Whole-system current view: the runtime has the active manifest and execution cursor, committed variables/results/transcript/artifacts, current attempt/checkpoint, declared execution mode/concurrency, cumulative token budget state, active step/wave and cancellation/suspension condition.
- Current-control decision scope: build and advance execution waves; admit step/wave commits; enforce token ceilings; suspend when a prompt exhausts the current budget; checkpoint resumable state; validate resume against the manifest fingerprint; increment attempt ownership and fence stale attempts; handle cancellation/failure; maintain ordered state across local or remote execution.
- Disturbance / variety regulated: unresolved dependencies, concurrent execution pressure, stale writers after takeover/resume, process interruption, cancellation, token-budget exhaustion, step failure, manifest drift between checkpoint and resume, and current run-state consistency.
- Decisive decision or feedback right: determine what current work may execute/commit next, which attempt owns the run, whether the run must suspend/fail/cancel, and what committed checkpoint is authoritative for continuation.
- Decision owner: deterministic first-party core/runtime lifecycle logic.
- Supporting / enforcement mechanisms: execution-wave builder; run-store attempts; manifest hashing; checkpoints; lifecycle state; `RunSuspendedError`; cumulative token budget; abort signals; local/child/remote execution engines; stale-attempt fencing.
- Closure path: current whole-run state + dependency/resource/lifecycle evidence → deterministic runtime selects executable wave/admission/lifecycle action → S1/step work executes → usage/result/error/checkpoint evidence returns → runtime commits, suspends, cancels, fails or advances the current run, changing what may happen next.
- Boundary reachability: these current-control paths are wired directly into the shipped `AgentRuntime` and included execution contracts for ordinary local/remote use; they are not development-only operators.
- Why this is / is not agent-owned: removing the model actor while keeping the core still leaves the same dependency, commit, attempt, checkpoint, budget and lifecycle decisions. The material S3 current-control discretion is encoded by deterministic first-party runtime rules, therefore `C` rather than `A`.
- Evidence: [`packages/core/src/agent-runtime.ts`](https://github.com/clearideas/agent-runtime/blob/6abb6fa1ae2455dfe3eb86414b617e1fa84a47b1/packages/core/src/agent-runtime.ts); [`packages/core/src/execution-plan.ts`](https://github.com/clearideas/agent-runtime/blob/6abb6fa1ae2455dfe3eb86414b617e1fa84a47b1/packages/core/src/execution-plan.ts); [`docs/concepts.md`](https://github.com/clearideas/agent-runtime/blob/6abb6fa1ae2455dfe3eb86414b617e1fa84a47b1/docs/concepts.md); [`docs/persistence-and-recovery.md`](https://github.com/clearideas/agent-runtime/blob/6abb6fa1ae2455dfe3eb86414b617e1fa84a47b1/docs/persistence-and-recovery.md); [`packages/step-prompt/src/index.ts`](https://github.com/clearideas/agent-runtime/blob/6abb6fa1ae2455dfe3eb86414b617e1fa84a47b1/packages/step-prompt/src/index.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: a dependency graph or checkpoint alone is not counted as S3. Credit rests on the integrated whole-run lifecycle loop that combines current work admission, authoritative run state, resource limits, suspension/resume ownership and failure/cancellation control.

## S3* — Complementary audit

- State: —
- Function: no material first-party complementary audit path over the live Agent Runtime run was established at the assessed recursion.
- Disturbance / variety regulated: not established beyond ordinary execution validation, checkpoint integrity, observability/telemetry and task-local evaluator patterns.
- Decisive decision or feedback right: no separate sufficiently independent operational-audit judgment over claimed run reality was found.
- Decision owner: not established.
- Supporting / enforcement mechanisms: ordered events, event sinks, OpenTelemetry, manifest/checkpoint validation and example evaluator loops provide observation or ordinary workflow checks but not a complementary whole-run audit channel.
- Closure path: no shipped independent observation/reconstruction path was found that samples operational reality separately from the normal run/control path and returns findings into S3 current control.
- Why this is / is not agent-owned: not applicable because the function itself is not established at this boundary.
- Evidence: [`docs/events-and-streaming.md`](https://github.com/clearideas/agent-runtime/blob/6abb6fa1ae2455dfe3eb86414b617e1fa84a47b1/docs/events-and-streaming.md); [`packages/core/src/agent-runtime.ts`](https://github.com/clearideas/agent-runtime/blob/6abb6fa1ae2455dfe3eb86414b617e1fa84a47b1/packages/core/src/agent-runtime.ts); [`examples/manifests/evaluator-loop.agent.yaml`](https://github.com/clearideas/agent-runtime/blob/6abb6fa1ae2455dfe3eb86414b617e1fa84a47b1/examples/manifests/evaluator-loop.agent.yaml); [`SECURITY_REVIEW.md`](https://github.com/clearideas/agent-runtime/blob/6abb6fa1ae2455dfe3eb86414b617e1fa84a47b1/SECURITY_REVIEW.md).
- Basis: explicit + structural negative review.
- Confidence: high.
- Caveats: strong observability does not by itself establish S3*. The runtime even treats event sinks as observational by default rather than allowing them to invalidate a commit.

### Absence scope

- Surfaces inspected: root README/documentation; core run lifecycle, execution-plan and state paths; event/streaming and OpenTelemetry surfaces; checkpoint/hash/attempt recovery paths; prompt/loop/standard executors; evaluator-loop and interactive examples; repository security review, tests and validation tooling as adjacent evidence.
- Plausible first-party paths checked: event sinks as an alternate observation channel; OpenTelemetry as independent operational evidence; checkpoint verification as replay/audit; evaluator-loop as a separate checker; security review/tests as an audit actor; remote worker protocol as an alternate operational observer.
- Why no material first-party path remains: event/telemetry surfaces observe the same ordinary runtime path and are explicitly observational by default, checkpoint/hash checks protect ordinary run-state integrity, evaluator-loop is a user-composed/example S1 workflow, and repository security/tests are development surfaces. None establishes an independent complementary audit channel whose findings close back into live run S3.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party prospective adaptation loop was established that converts prior environment/outcome evidence into changed future Agent Runtime capability or control policy.
- Disturbance / variety regulated: not established beyond persistence/recovery of the current run and bounded retries/loops inside an already-declared manifest.
- Decisive decision or feedback right: no adaptation judgment over future runtime capability was found.
- Decision owner: not established.
- Supporting / enforcement mechanisms: checkpoints, run stores, transcripts, retries, loops and resume preserve/re-enter current work but do not themselves infer or apply future capability changes.
- Closure path: no observed-evidence → adaptation decision → durable changed future capability → later current-control use path was established.
- Why this is / is not agent-owned: not applicable because the S4 function itself is not established at this boundary.
- Evidence: [`docs/concepts.md`](https://github.com/clearideas/agent-runtime/blob/6abb6fa1ae2455dfe3eb86414b617e1fa84a47b1/docs/concepts.md); [`docs/persistence-and-recovery.md`](https://github.com/clearideas/agent-runtime/blob/6abb6fa1ae2455dfe3eb86414b617e1fa84a47b1/docs/persistence-and-recovery.md); [`packages/core/src/agent-runtime.ts`](https://github.com/clearideas/agent-runtime/blob/6abb6fa1ae2455dfe3eb86414b617e1fa84a47b1/packages/core/src/agent-runtime.ts); [`packages/step-loop/src/index.ts`](https://github.com/clearideas/agent-runtime/blob/6abb6fa1ae2455dfe3eb86414b617e1fa84a47b1/packages/step-loop/src/index.ts).
- Basis: explicit + structural negative review.
- Confidence: high.
- Caveats: durable history, fresh-process resume and retries are intentionally not counted as S4 without prospective adaptation.

### Absence scope

- Surfaces inspected: run/checkpoint stores; transcript/event persistence; prompt/loop executors; runtime configuration/model profiles; adapters; resume/retry/budget recovery; manifests/examples and repository tree searches for learning/reflection/adaptation surfaces.
- Plausible first-party paths checked: checkpoint history as learned state; persisted transcript as future memory; loop goal/evaluator patterns as self-improvement; retry diagnostics as adaptation evidence; model/runtime configuration changes as an internal strategy-update loop.
- Why no material first-party path remains: persisted state is scoped to run recovery/continuation, loop/retry behavior is part of the current declared workflow, and configuration/manifests are externally authored inputs. No first-party mechanism was found that interprets operating evidence into a durable change of later runtime capability or S3 policy.

## S5 — Policy and identity

- State: —
- Function: no closed first-party runtime path was established for deciding or reaffirming ultimate agent/run identity or policy and returning that decision into operation.
- Disturbance / variety regulated: not established beyond externally supplied manifest/configuration, host authorization, connection/tool boundaries and local human approval steps.
- Decisive decision or feedback right: no runtime ultimate-policy/identity decision right was found.
- Decision owner: not established.
- Supporting / enforcement mechanisms: manifests, model/runtime configuration, host-owned credentials/connections, approval adapters, sandbox/network policy and production tenant ceilings constrain operation but are not themselves a closed S5 governance loop.
- Closure path: no first-party identity/policy issue → legitimate ultimate authority → authoritative policy/identity decision → returned operation path was established at this frozen revision.
- Why this is / is not agent-owned: neither an autonomous S5 owner nor a complete first-party parent S5 mode was established.
- Evidence: [`README.md`](https://github.com/clearideas/agent-runtime/blob/6abb6fa1ae2455dfe3eb86414b617e1fa84a47b1/README.md); [`docs/concepts.md`](https://github.com/clearideas/agent-runtime/blob/6abb6fa1ae2455dfe3eb86414b617e1fa84a47b1/docs/concepts.md); [`docs/production.md`](https://github.com/clearideas/agent-runtime/blob/6abb6fa1ae2455dfe3eb86414b617e1fa84a47b1/docs/production.md); [`packages/step-standard/README.md`](https://github.com/clearideas/agent-runtime/blob/6abb6fa1ae2455dfe3eb86414b617e1fa84a47b1/packages/step-standard/README.md); [`GOVERNANCE.md`](https://github.com/clearideas/agent-runtime/blob/6abb6fa1ae2455dfe3eb86414b617e1fa84a47b1/GOVERNANCE.md).
- Basis: explicit + structural negative review.
- Confidence: high.
- Caveats: an approval step can legitimately gate one action, and a host can define strong policy, but neither establishes S5 unless the assessed first-party system closes the ultimate identity/policy decision and returns it into operation.

### Absence scope

- Surfaces inspected: agent/run manifests and runtime configuration; host credential/connection/tool authorization; approval steps/adapters; token/tenant ceilings; sandbox/network policy; production guidance; repository governance as adjacent evidence.
- Plausible first-party paths checked: manifest authorship as identity authority; host authorization as parent S5; human approval steps as policy decisions; tenant/budget policy as ultimate policy; OSS project governance as runtime parent governance.
- Why no material first-party path remains: manifests/configuration are external declarations consumed by the runtime, approval steps resolve bounded workflow actions, and host/tenant/security policies enforce lower-level permissions/constraints. Repository governance governs development rather than a deployed run. No standard first-party mode closes an ultimate identity/policy decision at the assessed recursion.

## Distributed OSS parent arrangement

Repository maintainers govern development and releases of Agent Runtime, but that public OSS governance is outside one deployed run's recursion and is not imported as runtime S5. Host applications retain control of models, credentials, tools, persistence, compute, sandboxes and telemetry; those host boundaries are recorded as environment/parent constraints rather than credited as a first-party S5 loop without a shipped identity-governance contract.

## Self-hosted and non-human modes

The same manifest/run contract can execute in-process, in a child process or through a remote worker, and ordinary prompt execution plus deterministic S2/S3 control can proceed without continuous human supervision. A manifest may contain an explicit approval step, but that bounded workflow mode does not change the base ownership classification of S3 or create S5.

## Recursion

At the assessed recursion, one Agent Runtime run is the system. Model-backed prompt branches are operational S1s; in parallel mode several independent branches may coexist in one wave. The deterministic core supplies S2-specific interference attenuation and S3 whole-run current control. Sub-runs create nested operational systems with isolated state and only configured outputs returning to the parent; their existence is not used to inflate the parent recursion's S4/S5.

## Variety and escalation

The runtime attenuates current variety with manifest validation, dependency-safe waves, ordered/atomic commits, state-patch restrictions, bounded concurrency, authorization adapters, token budgets, checkpoint hashes, attempt fencing, cancellation and sandbox/network constraints. It amplifies operational capacity through model-backed prompts, tools, sub-runs, loops and local/remote execution adapters. Current exceptions are suspended, failed, retried or returned through host/approval boundaries; no built-in prospective adaptation or identity-governance escalation loop was established.

## Evidence gaps

- S2 is not inferred from graph scheduling alone. Credit rests on actual concurrent model-backed prompt S1s plus dependency exclusion, parallel-state restrictions and authoritative ordered wave commits.
- S3 is deterministic runtime control, not agent-owned orchestration: the manifest and core decide the current execution/lifecycle structure while models own substantive prompt work.
- S3* remains negative because telemetry/events/checkpoints do not provide a sufficiently independent complementary audit channel over the operating run.
- S4 remains negative because stores/checkpoints/transcripts preserve work but do not adapt future capability from observed evidence.
- S5 remains negative because manifests, approvals and host authorization are declarations/gates rather than a first-party ultimate identity/policy decision loop.

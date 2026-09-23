---
harness_id: nac
project_name: nac
repository: https://github.com/arcee-ai/nac
review_ref: fd75f2a000fd794a3a5c2184437d3a5e6c2a0437
reviewed_at: 2026-09-23
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-23
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# nac

## Review boundary

- System in focus: one nac runtime at pinned revision `fd75f2a000fd794a3a5c2184437d3a5e6c2a0437`, including the first-party central orchestrator, worker threads, workset/task decomposition, thread dispatch/re-dispatch/fork tools, structured episodes and the standard completion/verification protocol.
- Purpose and identity: execute long-running multi-step agent work by decomposing it across autonomous worker threads, synchronizing their discoveries and dependencies, synthesizing results and independently verifying material work before completion.
- Relevant environment: user objectives, repositories/files/tools reached by workers, model providers, MCP/tool results and external task evidence.
- Standard-distribution boundary: nac-owned Rust runtime, orchestrator prompt/runtime, thread tools, worker histories, episodes and workset state. Model-provider internals, external MCP servers/tools and repository CI are environmental systems and do not donate organizational functions.
- Credited operating / distribution surfaces: `README.md`; `crates/nac-core/src/agent/prompts/nac_orchestrator.md`; `crates/nac-core/src/tools/orchestrator.rs`; `crates/nac-core/src/tools/thread/mod.rs`; first-party workset/episode/thread state reached by those runtime paths.
- Adjacent first-party surfaces excluded from ownership: repository CI/release/contributor governance, tests and examples used only to validate nac itself, and provider/model internals not owned by nac.
- First-party operating / deployment modes considered: standard nac orchestrator execution with autonomous worker-thread dispatch, retained episodes, explicit re-dispatch/fork and fresh verification before completion.
- Recursion level: the nac run is the system-in-focus. Autonomous worker threads are sibling S1 operational units; the central orchestrator is the metasystem actor for their coordination/current control. A fresh verification thread is a complementary audit actor at the same run boundary.
- Reviewed revision: `fd75f2a000fd794a3a5c2184437d3a5e6c2a0437`.
- Observation date: 2026-09-23.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

nac ships a central autonomous orchestrator plus autonomous worker threads. The orchestrator owns decomposition, thread dispatch, current work-tree steering, cross-thread synchronization and final synthesis. Each dispatched worker receives its own agent/history context and produces a retained episode. The first-party thread tool can re-dispatch an existing worker with source-thread episodes and extra context or fork work into a fresh worker.

The standard orchestrator instructions make cross-thread synchronization an explicit organizational responsibility: discoveries, blockers and changed assumptions relevant to another active thread are to be re-dispatched rather than left in isolated histories. Before material completion the orchestrator is also instructed to launch a fresh verification thread when verification is appropriate. This separates production from complementary challenge while preserving an autonomous corrective-return path through subsequent re-dispatch.

## S1 — Operations

- State: A
- Function: perform bounded task work inside autonomous worker threads and return concrete findings, edits or other task results to the run.
- Disturbance / variety regulated: task uncertainty, repository/environment state, tool/model feedback and local implementation/research decisions within each delegated scope.
- Decisive decision or feedback right: choose the task-local reasoning, tool use and actions needed to satisfy a worker thread's assigned objective.
- Decision owner: the autonomous worker-thread model actor created by the first-party thread runtime.
- Supporting / enforcement mechanisms: thread histories, task prompt/context construction, tools, structured episodes, workset identity and runtime lifecycle.
- Closure path: orchestrator dispatches a scoped task → nac creates a worker with its own history and tools → worker autonomously executes → final result is retained as an episode → orchestrator consumes it and subsequent work can use it.
- Boundary reachability: the standard orchestrator directly exposes thread dispatch/fork/re-dispatch tools and `thread/mod.rs` instantiates the worker actor in the normal runtime path.
- Why this is / is not agent-owned: the runtime transports context and lifecycle, while substantive task-local decisions are made by the worker model actor.
- Evidence: [`README.md`](https://github.com/arcee-ai/nac/blob/fd75f2a000fd794a3a5c2184437d3a5e6c2a0437/README.md); [`crates/nac-core/src/tools/thread/mod.rs`](https://github.com/arcee-ai/nac/blob/fd75f2a000fd794a3a5c2184437d3a5e6c2a0437/crates/nac-core/src/tools/thread/mod.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: provider/model internals are not credited beyond the reachable autonomous worker role.

## S2 — Coordination

- State: A
- Function: attenuate inconsistent or stale assumptions among concurrent sibling worker threads by explicitly propagating relevant discoveries and dependency changes into subsequent sibling behavior.
- Disturbance / variety regulated: concurrently active threads can proceed from incompatible assumptions, miss another thread's blocker/discovery or continue work whose dependency context has materially changed.
- Decisive decision or feedback right: decide which discovery/blocker/changed assumption must be propagated to which active sibling and re-dispatch that target with the relevant source-thread evidence.
- Decision owner: the autonomous central orchestrator agent.
- Supporting / enforcement mechanisms: retained episodes, thread list/read state, dependency-aware scopes, `Redispatch`, `Fork`, source-thread episode injection and isolated thread histories.
- Closure path: sibling thread produces a material discovery → orchestrator recognizes relevance/interference → target sibling is re-dispatched with source-thread episodes/context → target worker resumes under the updated information → later output returns to the orchestrator.
- Boundary reachability: cross-thread bridge/re-dispatch behavior is required by the shipped orchestrator prompt and implemented by the standard thread tool.
- Why this is / is not agent-owned: the thread tool transports selected context, but the organizational discretion about relevance, target and timing belongs to the orchestrator agent.
- Evidence: [`crates/nac-core/src/agent/prompts/nac_orchestrator.md`](https://github.com/arcee-ai/nac/blob/fd75f2a000fd794a3a5c2184437d3a5e6c2a0437/crates/nac-core/src/agent/prompts/nac_orchestrator.md); [`crates/nac-core/src/tools/thread/mod.rs`](https://github.com/arcee-ai/nac/blob/fd75f2a000fd794a3a5c2184437d3a5e6c2a0437/crates/nac-core/src/tools/thread/mod.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: generic delegation is not the basis; the positive finding depends on the explicit inter-thread disturbance and feedback relation.
- Distinct S1 units: independently running worker threads with separate histories and assigned scopes.
- Inter-S1 disturbance: a worker's discovery, blocker or changed assumption can invalidate or interfere with another active worker's continuing scope or assumptions.
- Attenuating coordination relation: the orchestrator acts as a communication bridge and explicitly re-dispatches the affected target thread with source-thread episodes and additional context.
- Feedback into subsequent S1 behaviour: re-dispatch changes the target worker's next context and therefore its subsequent task behavior before its next retained result.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the relation exists specifically to regulate interaction-generated inconsistency among sibling operational threads, not merely to transmit tasks or store shared data.

## S3 — Inside-and-now control

- State: A
- Function: maintain and regulate the current whole-run work organization by decomposing the objective, inspecting current thread/work state, assigning scopes, steering active work and synthesizing completion.
- Disturbance / variety regulated: incomplete coverage, duplicated or mis-scoped work, dependency changes, blocked threads, competing implementation paths and current uncertainty about what remains to be done.
- Decisive decision or feedback right: choose the current work decomposition and dependency structure, dispatch/re-dispatch/fork workers, select among competing implementation paths and decide when current work is sufficiently integrated to enter verification/completion.
- Decision owner: the autonomous central orchestrator agent.
- Supporting / enforcement mechanisms: thread list/read tools, workset/task state, episodes, dispatch/fork/re-dispatch primitives and runtime concurrency instrumentation.
- Closure path: orchestrator observes current work/thread outputs → makes an allocation/steering/synthesis decision → first-party tools mutate active worker assignments/context → workers continue under the new current-control decision → resulting episodes update the orchestrator's current view.
- Boundary reachability: the central orchestrator and its control tools are the normal runtime entry path, not a development-only surface.
- Why this is / is not agent-owned: deterministic tools create and transport thread state, but the whole-run current-control discretion is exercised by the orchestrator model actor.
- Evidence: [`crates/nac-core/src/agent/prompts/nac_orchestrator.md`](https://github.com/arcee-ai/nac/blob/fd75f2a000fd794a3a5c2184437d3a5e6c2a0437/crates/nac-core/src/agent/prompts/nac_orchestrator.md); [`crates/nac-core/src/tools/orchestrator.rs`](https://github.com/arcee-ai/nac/blob/fd75f2a000fd794a3a5c2184437d3a5e6c2a0437/crates/nac-core/src/tools/orchestrator.rs); [`crates/nac-core/src/tools/thread/mod.rs`](https://github.com/arcee-ai/nac/blob/fd75f2a000fd794a3a5c2184437d3a5e6c2a0437/crates/nac-core/src/tools/thread/mod.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the S3 finding is run-scoped; it does not claim installation-wide control over unrelated nac runs.
- Whole-system current view: the orchestrator can list/read active threads, their retained episodes and the current work/dependency structure for the run.
- Current-control decision scope: task decomposition, scope/dependency assignment, dispatch, re-dispatch, fork, selection among competing implementations, synthesis and transition toward completion.

## S3* — Complementary audit

- State: A
- Function: challenge material completion through a fresh worker context before the orchestrator accepts the run as done, and return audit findings into corrective operational work when needed.
- Disturbance / variety regulated: an implementation or synthesized result may appear complete while containing defects, missed requirements, incorrect assumptions or unverified claims.
- Decisive decision or feedback right: independently inspect the produced work in a fresh verification thread and return findings that determine whether correction/re-dispatch is required before completion.
- Decision owner: the autonomous model actor in the fresh verification thread; the orchestrator autonomously routes resulting findings into correction.
- Supporting / enforcement mechanisms: fresh thread creation, separate history, verifier task context, retained episodes and source-thread re-dispatch.
- Closure path: producer thread reports result → orchestrator launches fresh verification thread → verifier independently inspects the artifact/claim and returns an episode → orchestrator acts on findings by re-dispatching corrective work or accepts the verified result → completion proceeds only after that loop.
- Boundary reachability: the shipped orchestrator prompt explicitly requires a fresh verification thread before declaring completion when verification is appropriate, and the normal thread runtime creates that independent actor.
- Why this is / is not agent-owned: verification judgment is made by a fresh model actor rather than by a deterministic build gate or the producing thread itself.
- Evidence: [`crates/nac-core/src/agent/prompts/nac_orchestrator.md`](https://github.com/arcee-ai/nac/blob/fd75f2a000fd794a3a5c2184437d3a5e6c2a0437/crates/nac-core/src/agent/prompts/nac_orchestrator.md); [`crates/nac-core/src/tools/thread/mod.rs`](https://github.com/arcee-ai/nac/blob/fd75f2a000fd794a3a5c2184437d3a5e6c2a0437/crates/nac-core/src/tools/thread/mod.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the audit is bounded to verification-appropriate material work; this does not imply every trivial response launches a verifier.
- Claim being audited: the producer/synthesis claim that the material implementation or task result is ready for completion.
- Ordinary reporting path: the producing worker returns its result as a retained completion episode to the orchestrator.
- Complementary access path: a fresh verification thread receives an independent task/context and can inspect the actual artifact/evidence rather than merely trust the producer's report.
- Independence boundary: the verifier is a fresh autonomous thread with its own actor/history rather than the producing thread's continuation.
- Who acts on findings: the central orchestrator consumes the verifier episode and can re-dispatch the producer or another worker with the finding before completion.

## S4 — Outside-and-then adaptation

- State: —
- Function: no run-level outside-and-future adaptation function is established in the reviewed standard distribution.
- Disturbance / variety regulated: episodes, worksets and skills preserve/use current or historical task knowledge, but the inspected runtime does not establish a separate loop that senses future-relevant external change, develops an organizational adaptation option and returns that option into present capability/current control.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: durable episodes, retained findings, skills/tools and workset state can support later work but do not by themselves establish S4.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: no qualifying S4 function is established, so no ownership state is assigned.
- Evidence: [`README.md`](https://github.com/arcee-ai/nac/blob/fd75f2a000fd794a3a5c2184437d3a5e6c2a0437/README.md); [`crates/nac-core/src/agent/prompts/nac_orchestrator.md`](https://github.com/arcee-ai/nac/blob/fd75f2a000fd794a3a5c2184437d3a5e6c2a0437/crates/nac-core/src/agent/prompts/nac_orchestrator.md).
- Basis: explicit + structural negative search.
- Confidence: medium-high.
- Caveats: memory and research inside a task are not automatically S4.

### Absence scope

- Surfaces inspected: orchestrator prompt/runtime, thread lifecycle, episodes, worksets, skills/tools and completion/verification protocol.
- Plausible first-party paths checked: retained historical episodes, reusable skills/tools, research threads and cross-thread synthesis.
- Why no material first-party path remains: these mechanisms improve present task execution or preserve knowledge, but no reviewed path closes external prospective sensing → adaptation-option generation → returned capability/current-control change at the assessed run boundary.

## S5 — Identity / ultimate policy

- State: —
- Function: no identity/ultimate-policy closure is established for the nac run.
- Disturbance / variety regulated: prompts, workset constraints and user objectives shape operational behavior but do not constitute an explicit dispute/decision over organizational identity or ultimate policy.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: system/orchestrator prompts, task scopes, tool permissions and runtime configuration constrain operation without creating an S5 organization.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: no qualifying S5 function is established.
- Evidence: [`README.md`](https://github.com/arcee-ai/nac/blob/fd75f2a000fd794a3a5c2184437d3a5e6c2a0437/README.md); [`crates/nac-core/src/agent/prompts/nac_orchestrator.md`](https://github.com/arcee-ai/nac/blob/fd75f2a000fd794a3a5c2184437d3a5e6c2a0437/crates/nac-core/src/agent/prompts/nac_orchestrator.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: task-final authority and prompt hierarchy are not promoted to identity/ultimate-policy governance.

### Absence scope

- Surfaces inspected: orchestrator/worker prompts, workset/task constraints, thread tools, runtime configuration and completion protocol.
- Plausible first-party paths checked: orchestrator final synthesis authority, task admission, prompt hierarchy and tool/workset constraints.
- Why no material first-party path remains: all inspected decisions remain task-operational or metasystem-current-control decisions; none is an identity/ultimate-policy issue with authoritative closure back into the organization.

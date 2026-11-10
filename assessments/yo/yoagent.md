---
harness_id: yoagent
project_name: yoagent
repository: https://github.com/yologdev/yoagent
review_ref: f1495e7f5746445a269ec6a9d14fa8ac346b359d
reviewed_at: 2026-11-10
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# yoagent

## Review boundary

- System in focus: The installed Rust `yoagent` loop library in a host-configured task run, including its optional first-party `SubAgentTool` delegation tree, standard filesystem tools, shared state and extension hooks. The companion yoyo/yobuild applications are separate systems.
- Purpose and identity: Provide a reusable model/tool loop that can stream, retry, gate, delegate and record work without imposing an application-specific task graph or agent organization.
- Relevant environment: User requests, provider responses, files and shell effects, tool errors, cancellation, token budgets, provider/context limits and concurrent subagent file accesses.
- Standard-distribution boundary: Public Rust crate `Agent` / `agent_loop` with configured provider and `AgentTool`s; optional `SubAgentTool` actually executes nested child loops in the same process, and first-party `ReadFileTool`, `WriteFileTool` and `EditFileTool` share a resolved-file lock across those loops.
- Credited operating / distribution surfaces: [core loop](https://github.com/yologdev/yoagent/blob/f1495e7f5746445a269ec6a9d14fa8ac346b359d/src/agent_loop.rs), [child loop tool](https://github.com/yologdev/yoagent/blob/f1495e7f5746445a269ec6a9d14fa8ac346b359d/src/sub_agent.rs), [process-wide file interference guard](https://github.com/yologdev/yoagent/blob/f1495e7f5746445a269ec6a9d14fa8ac346b359d/src/tools/file.rs), [extension contract](https://github.com/yologdev/yoagent/blob/f1495e7f5746445a269ec6a9d14fa8ac346b359d/src/extension.rs), [shared state](https://github.com/yologdev/yoagent/blob/f1495e7f5746445a269ec6a9d14fa8ac346b359d/src/shared_state.rs).
- Adjacent first-party surfaces excluded from ownership: `examples/` CLI, code review, extension verifier and evolution demonstrations; `integrations/` companion plugin/Worker crates; separate [yoyo-evolve](https://github.com/yologdev/yoyo-evolve) and `yobuild` agents; `docs/evals/`, tests, CI and project maintainer governance. Examples support API reachability but cannot donate application-specific metasystems to the installed loop.
- First-party operating / deployment modes considered: Single model/tool loop, configured nested `SubAgentTool` children, concurrent/batched/sequential tool strategies, default filesystem tools, scoped shared state, optional tree extensions and budgets, native and wasm-compatible library use. S2=C is limited to same-process file-tool combinations; an all-agent general coordination mode is not claimed.
- Recursion level: A task agent and optional child agent loops under one host-configured delegation tree. Child loops have distinct model/tool decisions as operational S1s; parallel tool calls within one loop are merely that S1's actions.
- Reviewed revision: `yologdev/yoagent@f1495e7f5746445a269ec6a9d14fa8ac346b359d` (pinned checkout).
- Observation date: 2026-11-10; static code/docs inspection without paid-provider execution.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

`agent_loop()` is the streaming model/tool feedback engine; the `Agent` wrapper retains sessions and queues. Tools execute sequentially, in batches or concurrently according to configuration. `SubAgentTool.execute()` constructs a fresh child `AgentContext`, calls `agent_loop_with_stats()`, forwards events/cancellation and returns child output and spending to the parent; the model may choose further work after receiving the result. Optional `SharedState` supplies a capacity-bounded key/value store but no semantic conflict adjudicator. [`agent_loop.rs`](https://github.com/yologdev/yoagent/blob/f1495e7f5746445a269ec6a9d14fa8ac346b359d/src/agent_loop.rs), [`sub_agent.rs`](https://github.com/yologdev/yoagent/blob/f1495e7f5746445a269ec6a9d14fa8ac346b359d/src/sub_agent.rs), [`shared_state.rs`](https://github.com/yologdev/yoagent/blob/f1495e7f5746445a269ec6a9d14fa8ac346b359d/src/shared_state.rs).

`hold_file()` uses a process-global keyed mutex for each normalized path across `read_file`, `write_file` and `edit_file`, explicitly covering concurrent subagents and preventing interleaved edits/lost updates. A cancelled waiter does not act; after lock release the next call proceeds and returns result to its originating loop. It is not an OS cross-process lock or a semantic negotiation of competing goals. Default file tools also include a per-agent `ReadLog` guard against overwriting files after only partial reads; it is not shared as an inter-agent intent registry. [`file.rs`](https://github.com/yologdev/yoagent/blob/f1495e7f5746445a269ec6a9d14fa8ac346b359d/src/tools/file.rs).

## Operational model

Within one run the model owns task/tool choices. In a configured tree, each child model has its own operational loop while the parent chooses delegation prompts and receives outcomes. First-party file-level sequencing constrains interference at one concrete shared surface, but no source-supported whole-organization commitment scheduler, independent audit unit, future adaptation governance or ultimate constitutional authority is inferred from general hooks and extension points.

## S1 — Operations

- State: A
- Function: Complete a user/parent task through model-directed iterative tool execution and responses, including configured child tasks.
- Disturbance / variety regulated: Evolving task instructions, tool effects/errors, provider responses, time/cost bounds, cancellation and context growth.
- Decisive decision or feedback right: Select tool/child delegation, arguments, next step and final answer based on returned observations.
- Decision owner: Model actor in each `agent_loop`; application supplies provider, permissions and exposed tools.
- Supporting / enforcement mechanisms: Streaming `agent_loop_with_stats`, execution strategies, tool gate, retries, continuation/stop decisions, context management, session wrapper and actual `SubAgentTool` recursion.
- Closure path: Prompt → model tool decisions → first-party tool execution or child loop → result/status/cost feedback → updated model turn → answer or bounded stop.
- Boundary reachability: The public `Agent` and free `agent_loop` are installed entry points; `SubAgentTool` implements the tool trait and invokes a separate child loop, not just an example stub.
- Why this is / is not agent-owned: Model choices drive operational action and delegation; the Rust runtime enforces tool/limit mechanics but does not pick the substantive next task itself.
- Evidence: [core loop](https://github.com/yologdev/yoagent/blob/f1495e7f5746445a269ec6a9d14fa8ac346b359d/src/agent_loop.rs), [subagent execute implementation](https://github.com/yologdev/yoagent/blob/f1495e7f5746445a269ec6a9d14fa8ac346b359d/src/sub_agent.rs), [README quickstart](https://github.com/yologdev/yoagent/blob/f1495e7f5746445a269ec6a9d14fa8ac346b359d/README.md).
- Basis: First-party implemented model/tool/child feedback loops.
- Confidence: High for supported source-level path.
- Caveats: Agent and child tool sets/providers must be configured, and no actual task-success benchmark is implied.

## S2 — Coordination

- State: C
- Function: Attenuate concrete same-file write/read/edit interference between distinct S1 child loops operating in one Rust process.
- Disturbance / variety regulated: Two concurrent child agents editing the same file, lost-update races and reads observing incomplete writes; not unrelated conceptual disagreement or cross-process coordination.
- Decisive decision or feedback right: Determine which competing file call can execute now and which must wait, thereby preserving serialized read/write/edit effects.
- Decision owner: First-party `hold_file` resolved-path mutex constructor; lock-order decision is deterministic, not model-owned S2 A, and requires host composition of multiple S1 loops with the supplied file tools.
- Supporting / enforcement mechanisms: Process-wide lock map keyed by path, each file operation acquiring/releasing the guard, cancellation rejection, `SubAgentTool` child concurrency, tool results returned to each actor.
- Closure path: Two child S1s request the same file → first-party keyed guard suspends one while the other finishes → waiting call executes or is cancelled → both receive their respective tool outcomes and continue their model loops.
- Boundary reachability: `SubAgentTool.execute()` runs real separate child loops, while the shipped `ReadFileTool`/`WriteFileTool`/`EditFileTool` call the same static `hold_file()`; composition of these installed parts is an explicit supported operating mode.
- Why this is / is not agent-owned: The specific file collision is dampened by runtime-enforced serialization; an agent does not autonomously judge competing intentions or allocate file rights, so constructor `C` rather than `A`.
- Distinct S1 units: Two `SubAgentTool` child runs with their own model/tool decisions inside the same process.
- Inter-S1 disturbance: Interleaved writes/edit read-modify-write and partial reads on the same resolved file.
- Attenuating coordination relation: A shared per-file mutex acquired by all three built-in filesystem tools and held for the full operation.
- Feedback into subsequent S1 behaviour: Each child sees its delayed operation's actual returned file result or cancellation/error, then proceeds or revises its subsequent model turn.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The lock's explicit reason and scope is preventing conflicting **distinct child agents** from corrupting the same operating artifact; generic `SharedState` and tool-batch scheduling alone would not meet this test.
- Evidence: [`file.rs` `hold_file` and tool use](https://github.com/yologdev/yoagent/blob/f1495e7f5746445a269ec6a9d14fa8ac346b359d/src/tools/file.rs), [real child runs](https://github.com/yologdev/yoagent/blob/f1495e7f5746445a269ec6a9d14fa8ac346b359d/src/sub_agent.rs), [tool execution strategies](https://github.com/yologdev/yoagent/blob/f1495e7f5746445a269ec6a9d14fa8ac346b359d/src/agent_loop.rs).
- Basis: Structural supported multi-child constructor for a narrow file-conflict S2 relation.
- Confidence: Medium-high for source-level path and scope; no live multi-provider concurrency test in this review.
- Caveats: Only same-process calls through these tools and normalized paths are coordinated; external processes, shell writes, arbitrary tools and semantic edit conflicts are not covered.

## S3 — Inside-and-now control

- State: —
- Function: Would decide current whole-task commitments, resource allocation or corrective interventions across several operational S1 agents.
- Disturbance / variety regulated: Competing child priorities, shared staffing/capacity, aggregate task outcomes and live organizational deviations.
- Decisive decision or feedback right: No standing first-party whole-portfolio current-control actor/reallocation cycle beyond model-chosen delegation of an individual task.
- Decision owner: Caller defines child/tool configuration, execution limits and optional budget extensions; parent model can assign tasks but has no supplied whole-organization commitments view.
- Supporting / enforcement mechanisms: Parent receives child tool output/usage, nested cancellation, depth/turn caps, optional tree-wide `Budget` and extension hooks.
- Closure path: A child result returns to the parent model, but ordinary delegation and a deterministic budget stop are not a system-wide current resource/commitment decision that is returned to distinct units.
- Why this is / is not agent-owned: Root-model delegation may be S1 task decomposition; the library does not supply a current-control function that manages a multi-agent portfolio or parent-governed bargaining.
- Evidence: [`sub_agent.rs` child return and limits](https://github.com/yologdev/yoagent/blob/f1495e7f5746445a269ec6a9d14fa8ac346b359d/src/sub_agent.rs), [`extension.rs` Budget](https://github.com/yologdev/yoagent/blob/f1495e7f5746445a269ec6a9d14fa8ac346b359d/src/extension.rs), [README design boundary](https://github.com/yologdev/yoagent/blob/f1495e7f5746445a269ec6a9d14fa8ac346b359d/README.md).
- Basis: Bounded absence at general crate recursion.
- Confidence: Medium-high; configured host could supply an S3 owner externally.
- Caveats: Parent tool-use can resemble supervision, but without durable whole-current commitments it is not automatically S3.

### Absence scope

- Surfaces inspected: Child task creation/return, parent event forwarding, shared state, tool execution strategies, extension/Budget and documented design boundary.
- Plausible first-party paths checked: Shared current portfolio, dynamic multi-child resource/priority choices, distinct S3 discretionary owner, parent decision feedback and revised operational commitments.
- Why no material first-party path remains: The crate implements bounded delegation and deterministic limits, not a supplied whole-organization current-control decision/closure path.

## S3* — Complementary audit

- State: —
- Function: Would challenge ordinary operational success claims against complementary reality evidence and send findings back to control.
- Disturbance / variety regulated: Missed execution failure, false model claims and unobserved artifact defects.
- Decisive decision or feedback right: No built-in independent claim-relative artifact audit and returned verdict in the core installed crate.
- Decision owner: Producing loop logs/events; a host can write its own `RunHooks::on_stop` verifier, but no such substantive first-party auditor is installed by default.
- Supporting / enforcement mechanisms: `RunHooks`, `StopContext`, `StopDecision::Continue/Fail`, optional GASP semantic event recording and example verifier.
- Closure path: The hook supports returning a host-written stop judgment into the loop, but the crate does not itself obtain complementary artifact evidence or make an audit verdict; logging alone does not close S3*.
- Why this is / is not agent-owned: Generic hook/recording machinery is not an independent inspector; the sample verifier's specific policy is adjacent example code.
- Evidence: [`extension.rs` stop hook contract](https://github.com/yologdev/yoagent/blob/f1495e7f5746445a269ec6a9d14fa8ac346b359d/src/extension.rs), [`agent_loop.rs` stop feedback](https://github.com/yologdev/yoagent/blob/f1495e7f5746445a269ec6a9d14fa8ac346b359d/src/agent_loop.rs), [README examples boundary](https://github.com/yologdev/yoagent/blob/f1495e7f5746445a269ec6a9d14fa8ac346b359d/README.md).
- Basis: Bounded absence of an installed specific auditor, notwithstanding a genuine return hook.
- Confidence: Medium-high.
- Caveats: A separate host-installed verifier could substantiate S3* for that host's assessed boundary; no claim of universal impossibility.

### Absence scope

- Surfaces inspected: Core loop event and stop path, `RunHooks`, example verifier/audit, GASP recording and subagent report propagation.
- Plausible first-party paths checked: Audit-specific independent evidence access, artifact verdict, distinct authority and returned correction beyond ordinary producing logs.
- Why no material first-party path remains: Shipped generic verifier scaffolding leaves substantive complementary observation/judgment to host-authored code, while packaged event logs share producer provenance.

## S4 — Outside-and-then intelligence

- State: —
- Function: Would proactively assess external/future conditions and return selected durable capability changes to current operations.
- Disturbance / variety regulated: Changing user needs, capabilities, tools, threats and opportunities outside the present task.
- Decisive decision or feedback right: No installed future-option generation/adaptation judgment or durable capability-update authority.
- Decision owner: Host developers supply extensions, providers and tools; model actions and skill lookups serve current user instructions.
- Supporting / enforcement mechanisms: Extension/tool-source refresh, skill loading, session tree, provider switching, optional decision-model tool gate and companion self-evolving agents outside the crate.
- Closure path: Dynamic tool sources are refreshed on generation changes, but no first-party prospective environmental diagnosis → selected adaptation → durable future capability return is established.
- Why this is / is not agent-owned: Fresh capability discovery and response to current tasks are not an ongoing future-strategy function without a separate adaptation decision.
- Evidence: [`tool_source.rs`](https://github.com/yologdev/yoagent/blob/f1495e7f5746445a269ec6a9d14fa8ac346b359d/src/tool_source.rs), [`agent_loop.rs`](https://github.com/yologdev/yoagent/blob/f1495e7f5746445a269ec6a9d14fa8ac346b359d/src/agent_loop.rs), [README explicit loop-not-agent framing](https://github.com/yologdev/yoagent/blob/f1495e7f5746445a269ec6a9d14fa8ac346b359d/README.md).
- Basis: Bounded absence.
- Confidence: Medium-high.
- Caveats: Separate `yoyo-evolve` uses this library for self-modification; its S4 would belong to that different assessed system.

### Absence scope

- Surfaces inspected: Tool-source refresh, extensions, skills, context/session, model options, decision model, companion integrations and examples.
- Plausible first-party paths checked: Outside/future scanning, prospective alternatives, decision on future operating capacity, durable implementation and return to present S1/S3.
- Why no material first-party path remains: Runtime reconfiguration points are real but prospective selection and durable capability governance are host/application responsibilities.

## S5 — Policy and identity

- State: —
- Function: Would resolve legitimate ultimate identity/policy questions, issue an authoritative decision and return it into subsequent operation.
- Disturbance / variety regulated: Conflicts over mission, legitimate ultimate constraints and who may change operating identity, not individual tool-call safety alone.
- Decisive decision or feedback right: No first-party legitimate ultimate-policy deliberation/adjudication owner at the installed crate boundary.
- Decision owner: Host configures prompts, tools and `tree_extensions`; deterministic guard hooks enforce host-supplied rules over a run/delegation tree.
- Supporting / enforcement mechanisms: Tree-inherited tool/input policies, required extension fail-closed behavior, budgets, allowed paths, depth limits and cancellation.
- Closure path: A host-installed policy can deny a tool and affect child continuation, but the crate does not handle identity dispute → legitimate constitutional decision → authoritative new rule → future operating closure.
- Why this is / is not agent-owned: Tree policy enforcement is useful runtime constraint, not evidence that either model or legitimate parent adjudicates ultimate identity inside the packaged system.
- Evidence: [`extension.rs` tree hooks](https://github.com/yologdev/yoagent/blob/f1495e7f5746445a269ec6a9d14fa8ac346b359d/src/extension.rs), [`sub_agent.rs` inherited extensions](https://github.com/yologdev/yoagent/blob/f1495e7f5746445a269ec6a9d14fa8ac346b359d/src/sub_agent.rs), [README host-gate contract](https://github.com/yologdev/yoagent/blob/f1495e7f5746445a269ec6a9d14fa8ac346b359d/README.md).
- Basis: Bounded absence.
- Confidence: High for packaged crate, not for user-built applications.
- Caveats: Parent organizations may legitimately own policy over installed agents; their own ultimate-policy workflow is external.

### Absence scope

- Surfaces inspected: Tree extensions, input/tool gates, stop behavior, agent configuration, shared state, system prompt, model and host APIs.
- Plausible first-party paths checked: Identity controversy, ultimate-policy ownership, parent authority deliberation, constitutive update and durable return-to-operation.
- Why no material first-party path remains: The crate supplies enforceable host-given constraints without a packaged constitutional adjudication/return mechanism.

## Distributed OSS parent arrangement

Maintainers and release contributors govern the Rust crate, not each installed agent or independent deployment. No project-wide parent identity/current-control mandate is returned into consumers by the package. Optional host-created delegation trees may be governed locally by their own applications, but are not an OpenSiro-style common organization by implication.

## Self-hosted and non-human modes

Native, WebAssembly and local-provider runs expose the same source-wired S1 model loop. Configured same-process subagents using standard file tools can obtain the narrow S2=C interference guard; remote workers, separately deployed processes, shell edits and arbitrary plugins do not inherit that protection. User-authored tree extensions enforce local host policy but do not independently establish S3/S4/S5.

## Recursion

The root and delegated child loops are separate task-executing S1s when configured. The file lock is a shared lower-level S2 constructor for their conflicting file operations. A host application could add further organizational levels and audit/strategy/policy owners; that higher recursion is not imported from sibling projects or examples.

## Variety and escalation

Model/tool observations close ordinary task variety; cancellation, limit and retry paths contain runtime disturbances. Per-file locks dampen a specific inter-agent concurrency disturbance, and children return output/usage to their invoking parent. Other cross-agent conflicts, allocation escalation, independent outcome audit and future/ultimate authority must be supplied by the host.

## Evidence gaps

- Static inspection at the frozen revision; no live provider-backed multi-agent run or concurrency benchmark. The S2=C claim is based on the explicit shared `hold_file` path and concrete same-process child-loop construction.
- Tool adapters not using the bundled file helpers and external processes fall outside the lock's scope.
- Companion applications, custom extensions and first-party examples may instantiate higher-recursion functions, but their workflows are not part of the installed general library boundary.

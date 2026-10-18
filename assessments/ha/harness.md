---
harness_id: harness
project_name: Harness
repository: https://github.com/sausheong/harness
review_ref: 1e5b6599bbc68519e83d156150d70f793653ca7d
reviewed_at: 2026-09-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-29
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: C
autonomy_s5: —
---

# Harness

## Review boundary

- System in focus: the first-party reusable Go agent runtime at frozen revision `1e5b6599bbc68519e83d156150d70f793653ca7d`, including the model/tool loop, tool executor and permissions, session/compaction machinery, subagent factory and `task` tool, runtime budgets and execution boundaries, steering seam, memory/skills providers, and the `runtime.Review` self-improvement constructor.
- Purpose and identity: provide a library substrate for long-running tool-using agents whose host application composes a `Runtime`, model provider, tools, session and optional memory/skills/subagent facilities, then drives autonomous work through `Runtime.Run` / `RunTurn`.
- Relevant environment: host applications and their operators, external LLM providers/models, caller-authored agent specs/system prompts, MCP servers, external tools/services, workspaces/filesystems and caller-selected persistence backends.
- Standard-distribution boundary: first-party Go packages that implement runtime/model invocation, tool execution and permissioning, session persistence/compaction, budgets, steering, subagents, memory/skills integration, review and execution backends are inside. Caller applications, external model/provider internals, caller-defined organizational control planes and provider-side agent functions remain environment.
- Credited operating / distribution surfaces: `runtime`, `session`, `tool`, `budget`, compaction/token machinery, bundled provider/execution adapters, the first-party subagent/task surface, memory/skills provider interfaces and `runtime.Review` constructor.
- Adjacent first-party surfaces excluded from ownership: repository CI/tests, release/maintainer activity, documentation publishing and examples as operating actors. The shipped self-improving example corroborates that the `Review` constructor is usable end-to-end but does not itself become a resident owner in every library deployment.
- First-party operating / deployment modes considered: ordinary `Runtime.Run` / `RunTurn`; optional registered subagents through the LLM-callable `task` tool; persistent-session mode with writer leases; optional steering; optional memory/skills providers; caller-wired end-of-run review using `LifecycleHooks.OnStop` + `runtime.Review`.
- Recursion level: one Harness-composed agent application. A top-level Runtime is an S1 operational unit; an explicitly spawned subagent Runtime can be another S1 unit when the host configures it. The library itself does not define a higher crew/organization control plane.
- Reviewed revision: `1e5b6599bbc68519e83d156150d70f793653ca7d`.
- Observation date: 2026-09-29.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Harness supplies an actual first-party think-act loop rather than only a provider wrapper. `Runtime.RunTurn` assembles session history, exposed tools, permissions and system context, calls the configured LLM provider, accepts model-selected tool calls, dispatches them through the first-party tool executor, appends results to session state and returns `continue` so the enclosing run can feed those observations into another model turn. `Runtime.Run` adds the streaming/concurrent-tool path, budgets, compaction and lifecycle behavior. The external model owns substantive next-action choice while Harness owns execution, observation return, persistence and bounded continuation.

The library also exposes nested autonomous work. `MakeSubagentFactory` constructs a fresh child Runtime with its own tools, prompt and session; `TaskTool` is model-callable and returns the child agent's final output to the parent as a normal tool result. Depth caps, per-runtime locking, tool-concurrency partitioning and persistent-session writer leases bound execution, but those deterministic mechanisms are not promoted to S2/S3 merely because they serialize or limit work.

The strongest metasystemic constructor is `runtime.Review`. It creates a distinct one-shot reviewer Runtime over a snapshot of a completed parent conversation and gives that reviewer intentionally restricted memory/skill tools. `ReviewPromptDefault` asks the reviewer to identify durable user preferences, project facts and reusable workflows specifically because they may matter in future sessions. Reviewer writes go to the shared stores used by the parent. `BuildRuntime` injects the skill index into model context, and the runtime refreshes self-authored skills before later model requests. The first-party path therefore converts external/user interaction into future-facing adaptation options and returns those options into present capability. It remains constructor-owned because applications must opt in and wire the review trigger/tools; the library does not automatically run this adaptation organ for every Runtime.

Primary evidence:

- [`runtime/runturn.go`](https://github.com/sausheong/harness/blob/1e5b6599bbc68519e83d156150d70f793653ca7d/runtime/runturn.go) — durable model/tool/result turn and continuation semantics.
- [`runtime/runtime.go`](https://github.com/sausheong/harness/blob/1e5b6599bbc68519e83d156150d70f793653ca7d/runtime/runtime.go) — full streaming agent loop, first-party execution boundaries and self-authored skill refresh before later model requests.
- [`runtime/subagent.go`](https://github.com/sausheong/harness/blob/1e5b6599bbc68519e83d156150d70f793653ca7d/runtime/subagent.go) — fresh child Runtime construction, separate child session and parent event/result return.
- [`tool/task.go`](https://github.com/sausheong/harness/blob/1e5b6599bbc68519e83d156150d70f793653ca7d/tool/task.go) — model-callable subagent delegation and explicit non-concurrency-safe task surface.
- [`session/lease.go`](https://github.com/sausheong/harness/blob/1e5b6599bbc68519e83d156150d70f793653ca7d/session/lease.go) — exclusive persistent-session writer lease.
- [`runtime/STEERING.md`](https://github.com/sausheong/harness/blob/1e5b6599bbc68519e83d156150d70f793653ca7d/runtime/STEERING.md) — caller-supplied correction boundary and its explicit host responsibilities.
- [`runtime/review.go`](https://github.com/sausheong/harness/blob/1e5b6599bbc68519e83d156150d70f793653ca7d/runtime/review.go) — first-party reviewer Runtime, shared memory/skills writes and explicit caller wiring.
- [`runtime/review_prompts.go`](https://github.com/sausheong/harness/blob/1e5b6599bbc68519e83d156150d70f793653ca7d/runtime/review_prompts.go) — future-session preferences/facts/reusable-workflow adaptation objective.
- [`runtime/builder.go`](https://github.com/sausheong/harness/blob/1e5b6599bbc68519e83d156150d70f793653ca7d/runtime/builder.go) — memory/skills injection and dynamic skill-index rebuild support.
- [`runtime/skills_refresh.go`](https://github.com/sausheong/harness/blob/1e5b6599bbc68519e83d156150d70f793653ca7d/runtime/skills_refresh.go) — refresh of self-authored skills into later system context.
- [`examples/self-improving-agent/main.go`](https://github.com/sausheong/harness/blob/1e5b6599bbc68519e83d156150d70f793653ca7d/examples/self-improving-agent/main.go) — shipped end-to-end construction demonstrating OnStop review into durable memory/skills.

## Operational model

A host creates a Runtime with an agent spec, provider, tool registry and session. The model sees the current session and allowed tool schemas, chooses a response or tool calls, and Harness executes allowed calls and returns the resulting observations to the next model turn. Optional budgets, compaction and permissions constrain the loop without taking over task-level discretion. A model may invoke a configured `task` tool to run a separate child Runtime, whose final response returns as an observation to the parent.

Harness is intentionally library-shaped rather than a crew/control-plane product. The host composes higher-level organization. This matters for S2 and S3: locks, serialization, recursion caps, steering and budgets are real runtime controls, but no first-party higher-level agent organ is supplied that arbitrates a concrete inter-S1 disturbance or continuously regulates whole-organization commitments. Separately, the optional Review constructor is explicitly future-facing and can modify shared skills used by later runs, which is why S4 receives constructor credit while the other metasystem functions remain unestablished.

## S1 — Operations

- State: A
- Function: perform open-ended agent work through a model-driven decision/action/observation loop with first-party tool execution and continuation.
- Disturbance / variety regulated: user/host goals, evolving session state, tool/service/file observations, model uncertainty, tool errors, provider responses, context pressure and runtime budget constraints.
- Decisive decision or feedback right: choose the next substantive answer or tool action in light of current context and returned tool observations.
- Decision owner: the autonomous model-driven agent actor running inside Harness's first-party Runtime.
- Supporting / enforcement mechanisms: `Runtime.Run` / `RunTurn`, provider abstraction, tool registry/executor, permission checker, session persistence, compaction, budgets, result spilling, fallback model and lifecycle hooks.
- Closure path: host/user goal → model turn → model-selected tool call or answer → Harness validates/executes the allowed tool → tool result is appended to session → later model turn sees the observation and revises/continues → terminal answer or bounded stop.
- Boundary reachability: `Runtime.Run` and `RunTurn` are the core shipped library API and require no repository-development actor; a host only supplies the external provider/tools/session expected by the library contract.
- Why this is / is not agent-owned: deterministic runtime code transports, bounds and executes actions, but it does not choose the substantive next task action. Removing the model actor leaves execution machinery without the open-ended operational decision loop.
- Evidence: [`runtime/runturn.go`](https://github.com/sausheong/harness/blob/1e5b6599bbc68519e83d156150d70f793653ca7d/runtime/runturn.go); [`runtime/runtime.go`](https://github.com/sausheong/harness/blob/1e5b6599bbc68519e83d156150d70f793653ca7d/runtime/runtime.go); [`runtime/builder.go`](https://github.com/sausheong/harness/blob/1e5b6599bbc68519e83d156150d70f793653ca7d/runtime/builder.go).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the model/provider itself is environment. S1 credit rests on Harness owning the first-party action/execution/observation continuation path around that model.

## S2 — Coordination

- State: —
- Function: no first-party coordination function was established that attenuates a specific interference/oscillation between distinct S1 units at the declared recursion.
- Disturbance / variety regulated: Harness can create parent and child Runtime units, but the reviewed standard distribution does not identify a concrete inter-unit conflict and a function-specific coordination judgment/feedback path for resolving it.
- Decisive decision or feedback right: not established for S2.
- Decision owner: not established.
- Supporting / enforcement mechanisms: `task` delegation, separate child sessions, recursion depth caps, tool-call concurrency classification, per-Runtime `runMu`, persistent-session writer leases and shared event forwarding.
- Closure path: delegation returns child output to the parent, and locks/serialization protect runtime data structures, but no qualifying inter-S1 disturbance → coordination response → changed later S1 behavior loop was established.
- Why this is / is not agent-owned: delegation and transport are not S2 by themselves. The strongest collision-like mechanisms are deterministic safety primitives: the `task` tool is marked non-concurrency-safe because parallel child-event forwarding is untested, while persistent writer leases protect one session from concurrent writers rather than coordinating the distinct parent/child S1 units that normally use separate sessions.
- Evidence: [`tool/task.go`](https://github.com/sausheong/harness/blob/1e5b6599bbc68519e83d156150d70f793653ca7d/tool/task.go); [`runtime/subagent.go`](https://github.com/sausheong/harness/blob/1e5b6599bbc68519e83d156150d70f793653ca7d/runtime/subagent.go); [`session/lease.go`](https://github.com/sausheong/harness/blob/1e5b6599bbc68519e83d156150d70f793653ca7d/session/lease.go).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: a caller application could construct multi-agent collision regulation around these primitives; generic programmability is not enough for `C`.

### Absence scope

- Surfaces inspected: subagent factory/runner, `task` tool, tool partitioning/concurrency, Runtime lock, parent event forwarding, persistent-session writer leases, budgets, steering and session persistence.
- Plausible first-party paths checked: subagent serialization as anti-interference; writer leases as shared-state collision regulation; concurrency caps/partitioning as cross-unit coordination; parent-child result return as coordination.
- Why no material first-party path remains: the child Runtime normally has a fresh session, writer leases regulate same-session writers rather than distinct S1 interaction, and task/concurrency mechanisms serialize or transport work without an evidenced inter-S1 disturbance-specific discretionary/feedback relation.

## S3 — Inside-and-now control

- State: —
- Function: no first-party whole-system current-control organ was established at the declared application recursion.
- Disturbance / variety regulated: Harness bounds individual Runtime work through turn/token/time/tool concurrency, permissions, steering and cancellation, but these do not form a whole-system view and decision loop over multiple current commitments/resources.
- Decisive decision or feedback right: choose or revise current organization-wide allocations, commitments, priorities, constraints or interventions from a whole-system view.
- Decision owner: not established. Host/application code chooses configuration and may supply steering; deterministic Harness code enforces those choices at the Runtime boundary.
- Supporting / enforcement mechanisms: budgets, max turns/depth/tool concurrency, permissions, session locking, runtime cancellation, lifecycle hooks and optional steering source.
- Closure path: configured limits and user corrections can change or stop one Runtime trajectory, but no standard whole-system current view → S3 judgment → organization-wide current-operation change path was found.
- Why this is / is not agent-owned: hard enforcement does not imply ownership. The `WithSteering` contract explicitly leaves queue ownership, pending/delivered state and reconciliation to the host and inserts corrections into one run at execution boundaries; it is not a fleet/whole-system management organ.
- Evidence: [`runtime/STEERING.md`](https://github.com/sausheong/harness/blob/1e5b6599bbc68519e83d156150d70f793653ca7d/runtime/STEERING.md); [`runtime/runtime.go`](https://github.com/sausheong/harness/blob/1e5b6599bbc68519e83d156150d70f793653ca7d/runtime/runtime.go); [`runtime/partition.go`](https://github.com/sausheong/harness/blob/1e5b6599bbc68519e83d156150d70f793653ca7d/runtime/partition.go).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: a host can build a manager above the library, but that external composition is outside the reviewed standard-distribution boundary.

### Absence scope

- Surfaces inspected: budgets, permissions, runtime locks, steering, subagent depth and tool-concurrency limits, lifecycle hooks, cancellation/session facilities and caller-facing configuration.
- Plausible first-party paths checked: steering as parent current control; budgets/concurrency as resource management; subagent parent relation as supervision; lifecycle hooks as current-control intervention.
- Why no material first-party path remains: every inspected path is local Runtime enforcement, correction or extension plumbing; none supplies the required whole-system current view and organization-level resource/commitment judgment.

## S3* — Complementary audit

- State: —
- Function: no materially independent complementary-audit path over an operational claim was established.
- Disturbance / variety regulated: ordinary model/tool results may be wrong or incomplete, but the standard runtime does not independently inspect operational reality and return an audit judgment to current control.
- Decisive decision or feedback right: not established for S3*.
- Decision owner: not established.
- Supporting / enforcement mechanisms: traces, session history, hooks, errors, tool results, compaction state and the separate `runtime.Review` reviewer Runtime.
- Closure path: ordinary tool observations return to S1 and Review can write future memory/skills, but neither forms a claim → materially complementary evidence → independent audit verdict → corrective current-control loop.
- Why this is / is not agent-owned: `runtime.Review` is a distinct model pass, but its supplied prompts ask what should be remembered for future sessions rather than checking a producer's operational claim against independent evidence. It is credited under S4 instead of being relabeled as audit.
- Evidence: [`runtime/review.go`](https://github.com/sausheong/harness/blob/1e5b6599bbc68519e83d156150d70f793653ca7d/runtime/review.go); [`runtime/review_prompts.go`](https://github.com/sausheong/harness/blob/1e5b6599bbc68519e83d156150d70f793653ca7d/runtime/review_prompts.go); [`runtime/runtime.go`](https://github.com/sausheong/harness/blob/1e5b6599bbc68519e83d156150d70f793653ca7d/runtime/runtime.go).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: a caller can provide a domain-specific `ReviewSpec.Prompt` and tools, but generic custom prompting is not a first-party S3*-specific constructor.

### Absence scope

- Surfaces inspected: `runtime.Review`, review prompts, traces/events, session history, lifecycle hooks, tool-result feedback, compaction and tests/examples as corroboration only.
- Plausible first-party paths checked: Review as independent critic; tool results as ground truth; traces/session logs as audit; lifecycle hooks as verifier seam.
- Why no material first-party path remains: no shipped path identifies an operational claim, obtains materially different access to reality, produces an audit judgment and returns that finding into corrective current control. Review's first-party semantic purpose is future memory/skill curation.

## S4 — Outside-and-then intelligence

- State: C
- Function: convert evidence from completed user/environment interactions into durable future-facing memory or reusable skills that can alter later agent capability.
- Disturbance / variety regulated: user preferences, project constraints and useful workflows discovered during operation can change or accumulate, making a fixed future agent context/capability progressively less fitted to later sessions.
- Decisive decision or feedback right: judge which completed-interaction distinctions are durable/reusable enough to save and choose whether to create/update future-facing memory or procedural skill content.
- Decision owner: constructor path. When invoked, the dedicated reviewer model owns the content-selection/adaptation judgment; however the host application must explicitly install the OnStop trigger, shared stores and review toolset, so Harness does not supply a resident autonomous S4 organ by default.
- Supporting / enforcement mechanisms: `runtime.Review`, snapshot reviewer Runtime, `ReviewPromptDefault` / `ReviewPromptVerbose`, memory and skill tools/stores, origin tagging, `RuntimeDeps.Skills`, `BuildRuntime` skill-index construction and `refreshSkills` before later model requests.
- Closure path: completed user/agent interaction → separately invoked reviewer reads the finished conversation → reviewer identifies a durable preference/project fact/reusable workflow → shared memory/skill write → later Runtime request refreshes the self-authored skill index / exposes load tools → subsequent operational model context and available procedural knowledge can change.
- Boundary reachability: `runtime.Review` and the standard future-session prompts are shipped Runtime APIs with documented `LifecycleHooks.OnStop` wiring; the same repository ships memory/skill providers and an end-to-end example. The function-specific constructor is therefore product-reachable even though applications must opt in and compose it.
- Why this is / is not agent-owned: once composed, the reviewer model makes the substantive prospective selection rather than a fixed parser. The missing piece is standard autonomous installation/trigger ownership, so Methodology `0.3.6` publishes constructor `C`, not `A`.
- Evidence: [`runtime/review.go`](https://github.com/sausheong/harness/blob/1e5b6599bbc68519e83d156150d70f793653ca7d/runtime/review.go); [`runtime/review_prompts.go`](https://github.com/sausheong/harness/blob/1e5b6599bbc68519e83d156150d70f793653ca7d/runtime/review_prompts.go); [`runtime/builder.go`](https://github.com/sausheong/harness/blob/1e5b6599bbc68519e83d156150d70f793653ca7d/runtime/builder.go); [`runtime/skills_refresh.go`](https://github.com/sausheong/harness/blob/1e5b6599bbc68519e83d156150d70f793653ca7d/runtime/skills_refresh.go); [`examples/self-improving-agent/main.go`](https://github.com/sausheong/harness/blob/1e5b6599bbc68519e83d156150d70f793653ca7d/examples/self-improving-agent/main.go).
- Basis: explicit + structural.
- Confidence: high.
- External distinction: the standard reviewer prompt explicitly extracts changing user preferences and project facts from a completed interaction, treating user/project evidence outside the Runtime's fixed prior capability as distinctions worth carrying forward.
- Future / prospective distinction: the prompt filters for information “worth remembering for future sessions” and reusable workflows/techniques rather than merely summarizing the completed task.
- Adaptation option generated: reviewer-selected durable memory entries and named procedural skills representing future behavior/context/capability changes.
- Path back into current capability / S3: reviewer writes into the parent's shared stores; `BuildRuntime` exposes memory/skills and embeds skill indices, while `Runtime.Run` refreshes self-authored skills before subsequent model requests, so later S1 operation can use the adaptation.
- Caveats: memory alone would not establish S4. Credit rests on the explicit future-relevance judgment plus reusable-skill generation and a first-party return path into later model context. The opt-in caller wiring prevents `A`.

## S5 — Policy and identity

- State: —
- Function: no first-party identity/ultimate-policy closure was established at the declared application recursion.
- Disturbance / variety regulated: agent specs, system prompts, permissions, budgets and memory files constrain operation, but the reviewed distribution does not define a genuine identity/constitutional issue and an authoritative decision loop that returns to govern the organization.
- Decisive decision or feedback right: not established for S5.
- Decision owner: caller/operator configuration supplies prompts, permissions and policy-like constraints; no qualifying S5 authority path is packaged by Harness.
- Supporting / enforcement mechanisms: `AgentSpec.SystemPrompt`, `MemoryFiles`, permission checker, budgets, steering and caller-selected runtime configuration.
- Closure path: configuration can alter later operation, but no identity/ultimate-policy issue → legitimate authority judgment → returned governing-policy closure is established.
- Why this is / is not agent-owned: prompts and permission gates are constraints, not S5 by themselves. `runtime.Review` writes memory/skills and does not receive an ultimate-policy mandate or authority to redefine the application's identity.
- Evidence: [`runtime/builder.go`](https://github.com/sausheong/harness/blob/1e5b6599bbc68519e83d156150d70f793653ca7d/runtime/builder.go); [`runtime/review.go`](https://github.com/sausheong/harness/blob/1e5b6599bbc68519e83d156150d70f793653ca7d/runtime/review.go); [`runtime/STEERING.md`](https://github.com/sausheong/harness/blob/1e5b6599bbc68519e83d156150d70f793653ca7d/runtime/STEERING.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: a host application may establish its own parent governance around Harness; that would require assessment at the host application's recursion rather than attribution to this library.

### Absence scope

- Surfaces inspected: agent/system prompt construction, memory files, permissions, budgets, steering, lifecycle hooks, review/memory/skills adaptation and caller configuration surfaces.
- Plausible first-party paths checked: system prompt as identity; permissions/budgets as ultimate policy; steering as parent authority; review as self-authored identity evolution; memory files as durable constitution.
- Why no material first-party path remains: inspected artifacts constrain or adapt lower-level operation but do not expose a first-party identity/ultimate-policy issue, legitimate authority decision and return-to-operation closure at the reviewed recursion.

## Recursion

Harness supports recursive task decomposition mechanically: a top-level model can invoke `task`, which constructs a fresh child Runtime with its own prompt, tools and session, and child output returns to the parent. This proves nested autonomous S1 work, not recursive viability by itself. The library does not supply a complete child metasystem or a higher crew-level organization whose S2–S5 functions can be inherited by name.

## Variety and escalation

Harness attenuates operational variety with permissions, turn/token/time limits, tool-concurrency classification, session leases, compaction, cancellation and steering boundaries. It amplifies action variety with arbitrary tools, MCP/provider adapters and opt-in subagents. Tool errors and child results return to the model as ordinary S1 feedback. Parent steering and host configuration remain external/local control rather than automatically becoming S3/S5. The Review constructor is the one function-specific future-facing escalation path credited above: it can convert completed interaction evidence into reusable skill/memory adaptations for later operation.

## Evidence gaps

- No first-party organization/crew layer was found that supplies a whole-system S3 view/authority above individual Runtime instances.
- No concrete inter-S1 collision/oscillation witness tied to the normal parent/subagent topology was found; session writer leases and task serialization are therefore retained as safety mechanisms rather than promoted to S2.
- No shipped independent operational verifier/auditor with a claim/evidence/corrective loop was found. `runtime.Review` is semantically a future-session curation primitive.
- The S4 constructor is explicit and end-to-end, but applications must opt in through lifecycle wiring and shared stores; this is the decisive reason for `C` rather than `A`.
- External provider/model internals and caller-built control planes are intentionally not imported into the vector.
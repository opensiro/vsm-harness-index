---
harness_id: yao-agents
project_name: Yao Agents
repository: https://github.com/YaoApp/yao
review_ref: a289dd55abe357941506e2114fb8c5ec21b99149
reviewed_at: 2026-09-24
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-24
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Yao Agents

## Review boundary

- System in focus: the first-party Yao Agents runtime at pinned revision `a289dd55abe357941506e2114fb8c5ec21b99149`, including assistant execution, LLM/tool/search/memory integration, first-party agent-to-agent calls, task execution/scheduling/quota state, workspaces/sandbox integration and standard runtime hooks.
- Purpose and identity: run self-hosted AI assistants and task agents that can converse, use tools/search/memory, operate in workspaces, call other agents and execute recurring tasks across a Yao deployment.
- Relevant environment: users and teams, external LLM provider endpoints, MCP servers/tools, web/knowledge/database sources, workspace/filesystem/computer nodes, configured credentials and application-specific hook code.
- Standard-distribution boundary: repository-owned `agent/assistant`, `agent/context`, `agent/caller`, `agent/task`, `agent/decision`, memory/search/MCP integration and shipped runtime/configuration surfaces are inside. External model providers, MCP servers and application-authored agent packages/hooks remain environmental or constructor inputs.
- Credited operating / distribution surfaces: top-level `README.md`; `agent/README.md`; `agent/assistant/agent.go`; `agent/caller/orchestrator.go`; `agent/docs/context-api.md`; `agent/task/run.go`; `agent/task/quota.go`; `agent/task/schedule.go`; `agent/task/enrich_result.go`; shipped assistant/task runtime paths.
- Adjacent first-party surfaces excluded from ownership: `agent/eval` CLI/testing framework, repository tests, CI, unit/integration fixtures and development-only evaluation flows. These may corroborate behavior but do not donate runtime S3* or other metasystem ownership to ordinary deployed agents.
- First-party operating / deployment modes considered: normal assistant chat/task execution through Yao's first-party LLM connector path; MCP/search/memory tool use; first-party A2A calls from agent hooks; parallel A2A `All`/`Any`/`Race`; task daemon execution; team quota/priority queue; configured recurring/daemon schedules. Optional external DeepSeek Harness or other adjacent runtimes are not needed for the credited S1 path.
- Recursion level: one Yao runtime/deployment containing one or more configured assistants/task agents. Individual assistant loops are S1 units. First-party A2A isolation can supply an S2 constructor path; team task quota/priority machinery can supply an S3 constructor path. Application-specific higher-level organizations composed with Yao require their own evidence.
- Reviewed revision: `a289dd55abe357941506e2114fb8c5ec21b99149`.
- Observation date: 2026-09-24.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Yao ships a first-party agent runtime rather than only an adapter around another harness. An `Assistant.Stream` call resolves the configured LLM connector, loads conversation/runtime context, performs search when enabled, calls the model, executes returned MCP tool calls, returns tool results to the model, retries/corrects failed tool calls and continues the tool loop. Create/Next hooks can alter context or delegate, while memory, trace, MCP, search, direct LLM and A2A capabilities are exposed through the runtime context.

The A2A layer resolves another configured Yao agent and calls that agent's own `Stream` path. Its `Orchestrator` supplies `All`, `Any` and `Race` parallel patterns. For parallel calls the runtime deliberately forks the parent context because concurrent agents would otherwise race on shared `Stack`, `Logger` and related mutable context state. This gives Yao a concrete anti-interference coordination surface rather than mere messaging.

Task execution adds a durable control layer around assistants. `Run` registers a daemon execution, applies a per-team execution quota, queues excess work, starts the selected assistant, persists run state and supports cancellation. `QuotaManager` maintains per-team running counts, limits and a priority queue; release of a slot deterministically admits the next queued task. `ScheduleEngine` reloads configured schedules, resets orphaned run states after restart and starts recurring task runs with backoff.

After a task run, `enrichTaskResult` makes a separate light-model call to derive task metadata including status, summary, outputs, priority and a reusable instruction. That instruction is persisted and may be used by later scheduled runs. This is useful longitudinal task maintenance, but at the reviewed boundary it abstracts the just-completed internal task conversation into another instruction; it does not model an external future, develop competing adaptation options and couple them back to a whole-system current-control function.

The same repository also contains a substantial `agent/eval` framework with simulator agents, agent-driven assertions, stability runs and CI integration. It is an explicit evaluation/testing surface invoked by `yao agent eval`, not part of the ordinary deployed assistant/task runtime. Under the Profile's boundary-provenance rule it therefore does not supply runtime S3* merely because it is first-party and co-located.

## Operational model

The primary operational unit is a configured Yao assistant/task agent. It receives a user/task objective, chooses model/tool/search actions, observes returned results and continues until the runtime ends the turn/task. Yao owns this loop in first-party code even though model inference and external tools may be supplied by providers.

When multiple Yao agents are invoked in parallel, the runtime exposes a specific constructor for coordination: isolated forked contexts plus explicit completion semantics prevent shared mutable execution state from colliding. The runtime provides the disturbance-specific mechanism and feedback structure, while application/hook authors still decide when and how autonomous agents should use that coordination relation.

For current whole-system control, the task subsystem exposes a per-team view of running versus queued work, a hard concurrent-execution limit and a priority decision path that determines which queued task receives the next released execution slot. This is a concrete shared-resource/current-priority control surface, but the standard distribution does not supply an autonomous manager that owns the priority/limit judgment. The caller/operator/application provides priority/configuration and the deterministic runtime enforces it.

## S1 — Operations

- State: A
- Function: execute assistant/task objectives through an autonomous model/tool/search/memory loop that directly produces user-facing or workspace outcomes.
- Disturbance / variety regulated: ambiguous user/task requests, changing conversation state, tool availability and tool results, search findings, MCP failures, model output, workspace state and task-local errors.
- Decisive decision or feedback right: choose the next substantive model/tool/search action in service of the current objective and revise that choice after observing returned results or failures.
- Decision owner: the configured autonomous assistant/model actor running through first-party `Assistant.Stream` and its tool loop.
- Supporting / enforcement mechanisms: LLM connector resolution, history/context construction, MCP execution, search, memory, hooks, sandbox/workspace APIs, retry construction, task daemon lifecycle and output streaming.
- Closure path: objective/messages plus current state → first-party assistant invokes the configured model → model chooses response/tool action → Yao executes tool/search operations → results/errors return into the assistant/model loop → subsequent action/output changes until completion or delegation.
- Boundary reachability: the first-party assistant path is the standard Yao agent runtime described in `agent/README.md` and implemented by `agent/assistant/agent.go`; external DeepSeek Harness integration is optional and is not required for this model/tool closure.
- Why this is / is not agent-owned: deterministic Yao code transports context, executes calls and handles retries, but the substantive next-action choice is made by the autonomous model actor. Removing that actor leaves transport/execution machinery without the goal-directed operational decision loop.
- Evidence: [`agent/README.md`](https://github.com/YaoApp/yao/blob/a289dd55abe357941506e2114fb8c5ec21b99149/agent/README.md); [`agent/assistant/agent.go`](https://github.com/YaoApp/yao/blob/a289dd55abe357941506e2114fb8c5ec21b99149/agent/assistant/agent.go); [`agent/docs/context-api.md`](https://github.com/YaoApp/yao/blob/a289dd55abe357941506e2114fb8c5ec21b99149/agent/docs/context-api.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the model provider is an external dependency and application hooks can constrain or redirect the loop; neither changes the fact that the shipped Yao runtime closes ordinary autonomous operation around the model actor.

## S2 — Coordination

- State: C
- Function: attenuate concrete shared-context race/interference when several first-party Yao agent S1 calls execute concurrently.
- Disturbance / variety regulated: concurrent A2A agent calls would otherwise modify shared mutable parent context state such as `Stack` and `Logger`, creating race conditions and cross-call interference.
- Decisive decision or feedback right: select a coordination pattern (`All`, `Any`, `Race`) and place each participating agent call in an isolated forked context so concurrent local activity cannot corrupt the shared parent execution state.
- Decision owner: constructor path only. Yao owns the S2-specific isolation and completion primitives, while the application/hook developer must compose the autonomous actor or policy that decides when those coordination patterns govern interacting agents.
- Supporting / enforcement mechanisms: context `Fork()`, per-call goroutines/channels, `All`/`Any`/`Race` completion semantics, panic isolation and result collection.
- Closure path: an application/hook requests concurrent calls to distinct Yao agents → `Orchestrator` forks context per S1 call and applies the selected concurrency relation → each agent executes against isolated mutable state → coordinated completion/results return to the caller and subsequent work consumes those results without shared-context races.
- Boundary reachability: `ctx.agent.All`, `Any` and `Race` are documented first-party Context APIs and call configured Yao agents through the ordinary `agent.Stream` runtime; the anti-race fork is implemented directly in `agent/caller/orchestrator.go`.
- Why this is / is not agent-owned: the S2 function is materially implemented, but the standard runtime does not supply an autonomous coordination actor that owns the choice among these relations for a live multi-agent organization. That missing owner/closure composition is why the publication state is `C`, not `A`.
- Evidence: [`agent/caller/orchestrator.go`](https://github.com/YaoApp/yao/blob/a289dd55abe357941506e2114fb8c5ec21b99149/agent/caller/orchestrator.go); [`agent/docs/context-api.md`](https://github.com/YaoApp/yao/blob/a289dd55abe357941506e2114fb8c5ec21b99149/agent/docs/context-api.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: generic A2A delegation is not credited. The positive mapping is limited to the explicit shared-state race and the first-party isolation/completion path that regulates it.
- Distinct S1 units: two or more configured Yao assistants invoked through A2A; each call resolves a separate agent and enters that agent's `Stream` loop.
- Inter-S1 disturbance: parallel calls can race while mutating shared parent-context state; the source explicitly says forked contexts are used to avoid race conditions on shared `Stack`, `Logger`, and related state.
- Attenuating coordination relation: each parallel S1 receives an isolated forked context, while `All`/`Any`/`Race` define how concurrent results are admitted back to the parent caller.
- Feedback into subsequent S1 behaviour: the coordinated result set/first success/first completion returns to the calling hook/agent workflow and determines what continuation can consume, while isolation prevents one concurrent S1 from corrupting another's working state.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the credited mechanism exists specifically to suppress an evidenced concurrency race between simultaneously executing S1 calls; A2A messaging and delegation alone are not used as the positive witness.

## S3 — Inside-and-now control

- State: C
- Function: regulate current shared execution capacity and priority across a team's concurrently runnable task-agent operations.
- Disturbance / variety regulated: more runnable task executions than the team's allowed concurrent capacity, plus contention over which queued commitment receives the next available execution slot.
- Decisive decision or feedback right: determine current team execution capacity and relative queue priority, thereby deciding which commitment may run now and which waits when capacity is exhausted.
- Decision owner: constructor path only. The first-party API/runtime exposes the team-wide resource/priority decision path, but priority/configuration is supplied by caller/operator/application rather than an autonomous Yao manager that owns whole-system current-control discretion.
- Supporting / enforcement mechanisms: `QuotaManager.running`, per-team limits, atomic `TryAcquire`, priority heap, `Enqueue`, `Release`, `SetPriority`, queue status, daemon run registration and cancellation.
- Closure path: task run requests reach the team quota boundary → available slots are admitted; excess commitments enter the per-team priority queue → a released slot selects the highest-priority queued commitment and signals its daemon → that task changes from queued to running and executes its assistant loop.
- Boundary reachability: `Run` uses the global team quota in the shipped task runtime on every task execution; queue priority is an explicit `RunReq`/WS command field and queued-task priority can be changed through the first-party task API.
- Why this is / is not agent-owned: Yao has actual current authority over shared execution slots and commitments, not merely observability, but the organizational choice of limits/priorities is not autonomously owned in the standard distribution. Deterministic quota/heap enforcement does not upgrade the state to `A`.
- Evidence: [`agent/task/run.go`](https://github.com/YaoApp/yao/blob/a289dd55abe357941506e2114fb8c5ec21b99149/agent/task/run.go); [`agent/task/quota.go`](https://github.com/YaoApp/yao/blob/a289dd55abe357941506e2114fb8c5ec21b99149/agent/task/quota.go); [`agent/task/types.go`](https://github.com/YaoApp/yao/blob/a289dd55abe357941506e2114fb8c5ec21b99149/agent/task/types.go).
- Basis: structural.
- Confidence: medium-high.
- Caveats: this is a constructor classification, not a claim that a queue or scheduler is itself S3. The positive function is the explicit team-level capacity/priority control path; an autonomous owner of the decisive priority/resource judgment still must be composed.
- Whole-system current view: `QuotaManager` maintains, per team, the concurrent execution limit, current running count and queued commitments, and exposes `GetStatus` as `Limit/Running/Queued`.
- Current-control decision scope: execution-slot admission and ordering of queued task commitments under a team-wide capacity constraint.

## S3* — Complementary audit

- State: —
- Function: no materially independent complementary audit path is wired into the ordinary deployed agent/task runtime.
- Disturbance / variety regulated: Yao has tracing, task result enrichment and a rich evaluation framework, but ordinary execution does not route operational claims through a separate independent reviewer that can challenge them and close corrective feedback into subsequent runtime control.
- Decisive decision or feedback right: not established for S3* in the credited deployment boundary.
- Decision owner: not established.
- Supporting / enforcement mechanisms: trace nodes/logging, task summaries/result enrichment, `agent/eval` simulator/assertion/reporting tools and tests.
- Closure path: no standard runtime complementary-audit closure established.
- Why this is / is not agent-owned: `agent/eval` can run independent tests and agent-driven assertions, but it is an explicit developer/evaluation CLI surface rather than a credited actor in normal assistant/task operation. Runtime enrichment summarizes its own just-completed task conversation and is not independent audit access.
- Evidence: [`agent/eval/README.md`](https://github.com/YaoApp/yao/blob/a289dd55abe357941506e2114fb8c5ec21b99149/agent/eval/README.md); [`agent/task/enrich_result.go`](https://github.com/YaoApp/yao/blob/a289dd55abe357941506e2114fb8c5ec21b99149/agent/task/enrich_result.go); [`agent/docs/context-api.md`](https://github.com/YaoApp/yao/blob/a289dd55abe357941506e2114fb8c5ec21b99149/agent/docs/context-api.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: an application can use the eval framework or another Yao agent as an auditor, but that creates a separately composed operating boundary and does not make ordinary runtime S3* positive.

### Absence scope

- Surfaces inspected: assistant/tool loop, tracing, task daemon/result enrichment, A2A runtime, `agent/eval` documentation and evaluator/test surfaces.
- Plausible first-party paths checked: trace as audit, result enrichment as reviewer, agent-driven assertions, simulator/checkpoints, test reporter agents and A2A reviewer composition.
- Why no material first-party path remains: the ordinary runtime checks are same-path operational/support functions, while the independently configurable evaluator is a separate developer/CI evaluation surface with no standard return-to-operation corrective loop in the assessed deployment mode.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party external-and-prospective adaptation loop is established at the Yao runtime/deployment boundary.
- Disturbance / variety regulated: assistants can search external sources and persistent task metadata can change across runs, but these mechanisms remain task execution/context support rather than a metasystem that models future environmental change and develops organizational adaptation options.
- Decisive decision or feedback right: no runtime owner is shown deciding future capability changes from an external/prospective model.
- Decision owner: not established.
- Supporting / enforcement mechanisms: web/KB/DB search, persistent memory, task history, task-result enrichment, reusable scheduled instructions, model/connector configuration and eval outputs.
- Closure path: no S4 closure established. Search findings normally feed the current S1 task; post-run enrichment abstracts the current conversation into a reusable instruction that later repeats the task, but it does not generate future organizational adaptation options through an S3–S4 conversation.
- Why this is / is not agent-owned: model-driven learning/memory/instruction rewriting is not enough under the Profile unless it is externally and prospectively oriented and changes current organizational capability through the required closure.
- Evidence: [`agent/docs/context-api.md`](https://github.com/YaoApp/yao/blob/a289dd55abe357941506e2114fb8c5ec21b99149/agent/docs/context-api.md); [`agent/task/enrich_result.go`](https://github.com/YaoApp/yao/blob/a289dd55abe357941506e2114fb8c5ec21b99149/agent/task/enrich_result.go); [`agent/task/enrich_result_prompt.yml`](https://github.com/YaoApp/yao/blob/a289dd55abe357941506e2114fb8c5ec21b99149/agent/task/enrich_result_prompt.yml); [`agent/task/schedule.go`](https://github.com/YaoApp/yao/blob/a289dd55abe357941506e2114fb8c5ec21b99149/agent/task/schedule.go).
- Basis: structural negative search.
- Confidence: high.
- Caveats: the reusable instruction is a meaningful longitudinal feedback mechanism, but it is scoped to repeating/maintaining the same task and lacks the Profile's external/prospective option-development witness.

### Absence scope

- Surfaces inspected: search APIs, memory namespaces, task scheduling, result enrichment/instruction persistence, decision connector, eval framework, agent hooks and configuration paths.
- Plausible first-party paths checked: search as environmental sensing; memory as learning; result-enrichment instruction as self-improvement; recurring schedules as future orientation; eval reports as adaptation input.
- Why no material first-party path remains: no reviewed standard runtime path combines external/future-relevant distinctions, development of adaptation options and a return into present whole-system capability/S3. The observed loops are current-task operation, task repetition or adjacent evaluation.

## S5 — Policy and identity

- State: —
- Function: no first-party runtime identity/ultimate-policy deliberation and closure path is established at the Yao deployment recursion.
- Disturbance / variety regulated: configured prompts, assistant packages, team/user authorization, connector choices, workspace settings, schedules and permissions constrain what agents may do, but those constraints originate from users/developers/operators.
- Decisive decision or feedback right: choose or revise the deployment's durable mission, identity or ultimate policy when current operational needs and future adaptation conflict.
- Decision owner: external user/team/operator/developer; no first-party S5 actor or closed parent-governed identity path is established in the reviewed runtime evidence.
- Supporting / enforcement mechanisms: `package.yao`, prompts, authorization context, agent configuration, team scoping, connector selection, workspace/sandbox configuration and runtime hooks.
- Closure path: configuration can govern later execution after an external actor edits it, but no runtime identity/policy issue → legitimate ultimate authority → authoritative decision → returned operation loop was established.
- Why this is / is not agent-owned: policy/configuration text and ordinary user/operator control constrain operation without themselves constituting S5 ownership.
- Evidence: [`agent/README.md`](https://github.com/YaoApp/yao/blob/a289dd55abe357941506e2114fb8c5ec21b99149/agent/README.md); [`agent/docs/context-api.md`](https://github.com/YaoApp/yao/blob/a289dd55abe357941506e2114fb8c5ec21b99149/agent/docs/context-api.md); [`agent/assistant/agent.go`](https://github.com/YaoApp/yao/blob/a289dd55abe357941506e2114fb8c5ec21b99149/agent/assistant/agent.go).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: a self-hosted parent organization can author and deploy identity-level policy around Yao, but ordinary configuration ownership is not enough to publish `P` without a function-specific runtime closure.

### Absence scope

- Surfaces inspected: assistant/package configuration, prompts, auth/team context, task/workspace configuration, hooks, model connector selection, scheduling and runtime stop/cancel paths.
- Plausible first-party paths checked: system prompt as policy; authorization as S5; team ownership as parent governance; decision connector as policy actor; operator configuration and stop/cancel as ultimate authority.
- Why no material first-party path remains: these surfaces express or enforce externally supplied constraints and ordinary operational control. No identity-level matter is surfaced to a legitimate ultimate authority and returned through a first-party S5 closure path.

## Recursion, variety, and escalation

Yao supports nested A2A calls and many configured assistants, but nesting alone does not establish recursive viable systems. A child assistant has local operational autonomy, yet evidence for its own S2–S5 closure depends on the application assembled around it.

The runtime attenuates variety through context isolation, quotas, priorities, timeouts, cancellation, schedules and authorization; it amplifies operational variety through MCP/search/memory/sandbox/A2A capabilities. Task status, queue state and failures are observable, but ordinary status/queue surfaces are not treated as separate algedonic functions.

## Evidence gaps

- No positive S3* is inferred from the co-located eval framework because ordinary deployed runtime wiring into a corrective audit loop was not established.
- No S4 is inferred from the task-enrichment instruction loop because the reviewed evidence does not establish external/prospective option development coupled back into present whole-system capability.
- No parent-mode notation is published from generic self-hosted operator control alone.

## Proposed terminal outcome

`included` with standalone state vector:

```text
S1=A / S2=C / S3=C / S3*=— / S4=— / S5=—
```

Yao is included because its first-party standard runtime closes an autonomous model/tool operational loop. Its higher-level organizational strengths are constructor paths: concrete multi-agent anti-race coordination and team-wide current execution-capacity/priority control are shipped, while autonomous metasystem owners must still be composed by the application.

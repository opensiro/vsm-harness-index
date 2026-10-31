---
harness_id: reinloop
project_name: reinloop
repository: https://github.com/aantenore/reinloop
review_ref: 358b8f677fc279155808c9e4bb8fe3cf443c00ab
reviewed_at: 2026-10-31
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# reinloop

## Review boundary

- System in focus: The standalone reinloop runtime and its documented first-party agent/team constructor APIs.
- Purpose and identity: Run user-defined agents/teams with durable model/tool execution and explicit configuration.
- Relevant environment: User workspaces, configured inference endpoints, MCP/tool services and the human caller.
- Standard-distribution boundary: Packaged src-based runtime, built-in patterns/architect, CLI/HTTP/MCP interfaces and supported declarative composition. External agent-layers implementations are excluded.
- Credited operating / distribution surfaces: src/loop.ts, patterns/team/subagent composition, config/runtime, workspace tools, policy/store adapters and the public interfaces.
- Adjacent first-party surfaces excluded from ownership: Examples provide constructor wiring evidence only; test/fixtures, benchmarks, live scripts, development CI and external Pi/agent-layers packages do not supply installed autonomous owners.
- First-party operating / deployment modes considered: Standalone CLI run/chat/create, programmatic agent/team, HTTP and MCP; configured evaluator mode is a constructor, not an installed default reviewer.
- Recursion level: One configured project/runtime and its operational members; nesting does not prove viable recursion.
- Reviewed revision: `358b8f677fc279155808c9e4bb8fe3cf443c00ab`.
- Observation date: 2026-10-31.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

A dependency-free TypeScript event loop folds run state over append-only events, executes policy-gated tools, budgets and compacts context, calls providers and persists checkpoints. A team has linked member runs and aggregate usage. Built-in chain/parallel/router/evaluator/orchestrator patterns construct dataflow or delegation; custom patterns/plugins remain caller supplied. The evaluator keeps a generator session, invokes a separate schema-constrained judge, and feeds rejected output back for revision. Architect writes/validates agent files inside a restricted directory. Identity, guardrail, knowledge, telemetry and evaluation interfaces are explicit; external implementations are not imported as first-party behavior. See [architecture][R4], [patterns][R2] and [runtime][R3].

## Operational model

Each configured model-backed member owns its local task/tool choices. Deterministic patterns, logs, budget limits and approval transport support those choices. The public evaluator role exposes a reconstructable review-and-return constructor, but a caller must provide its reviewer/evidence boundary. Other pattern names do not establish organizational functions by themselves.

## S1 — Operations

- State: A
- Function: Agents execute user work through model-selected tools; the built-in architect also constructs agent/team definitions.
- Disturbance / variety regulated: Task-specific file, shell, web, memory, delegated-work and provider outcomes.
- Decisive decision or feedback right: Select tools/delegates and interpret their returned observations until a final or structured answer.
- Decision owner: The configured model-backed agent.
- Supporting / enforcement mechanisms: First-party event loop, budget/permission enforcement, crash-safe stores, compaction and provider transports.
- Closure path: generate → tool calls → policy/approval/execute → persisted results → subsequent model turn or output.
- Boundary reachability: CLI/config/runtime and the public agent/run API construct the model-backed loop; teams invoke the same first-party member runner. No new loop code is required.
- Why this is / is not agent-owned: Removing the agent leaves recording and limits but no discretionary operational action selection.
- Evidence: [Loop][R1], [composition][R2], [runtime][R3], [architecture][R4].
- Basis: structural.
- Confidence: high.
- Caveats: Mock providers and conformance tests do not evidence autonomy; real provider access was not exercised.


## S2 — Coordination

- State: —
- Function: No supplied inter-S1 interference regulation is established.
- Disturbance / variety regulated: Distinct team members can run concurrently, but the pinned patterns do not identify a concrete cross-unit collision/oscillation they regulate.
- Decisive decision or feedback right: Chain/parallel/router/orchestrator choose execution order or assignees without a conflict-response decision path.
- Decision owner: Pattern authors configure topology and concurrency; lead agents delegate tasks.
- Supporting / enforcement mechanisms: Bounded concurrency, labelled outputs, failure aggregation, isolated child context and linked event logs.
- Closure path: Results reach an aggregator or parent; no specific inter-S1 disturbance-to-attenuation feedback is supplied.
- Why this is / is not agent-owned: Coordination requires more than choosing a worker, limiting parallelism or forwarding events.
- Evidence: [Patterns][R2], [team API][R5], [subagents][R6], [pattern documentation][R7].
- Basis: structural.
- Confidence: high.
- Caveats: A custom conflict-regulating pattern is possible but is caller-created.

### Absence scope

- Surfaces inspected: README.md, docs/architecture.md, docs/patterns.md, docs/layers/eval.md, src/loop.ts, src/patterns.ts, src/team.ts, src/subagent.ts, src/policy.ts, src/serve.ts, src/architect.ts, src/router.ts, configuration/registry code and test/patterns.test.ts
- Plausible first-party paths checked: Checked all five built-in patterns, the limited worker scheduler, member failure handling, nested teams, child budgets and shared stores for reservations, conflict arbitration or anti-oscillation feedback.
- Why no material first-party path remains: The shipped relations are decomposition, routing, sequencing, aggregation and quality iteration; none is tied to a concrete inter-S1 interference relation.


## S3 — Inside-and-now control

- State: —
- Function: No whole-system current-regulation decision path is supplied.
- Disturbance / variety regulated: Per-run budget, cancellation, member failures, policy denials and accumulated usage.
- Decisive decision or feedback right: No shipped regulator revises common commitments/resources using a whole-team current view.
- Decision owner: Caller/developer sets budgets and policies; runtime enforces them. The orchestrator receives delegated answers, not shared-resource intervention powers.
- Supporting / enforcement mechanisms: Aggregated team usage/cost, parentRunId, RunHandle.abort, HTTP run listing and approval callbacks.
- Closure path: Budgets stop member runs, failures propagate and operators can inspect logs; these are not a whole-system decision-and-return loop.
- Why this is / is not agent-owned: Enforcement and observability do not establish S3 ownership. No function-specific autonomous constructor or legitimate parent current-control mode is evidenced.
- Evidence: [Team state][R5], [loop][R1], [policy][R8], [HTTP surfaces][R9], [orchestrator pattern][R2].
- Basis: structural.
- Confidence: high.
- Caveats: The public hooks can support a separately implemented regulator.

### Absence scope

- Surfaces inspected: README.md, docs/architecture.md, docs/patterns.md, docs/layers/eval.md, src/loop.ts, src/patterns.ts, src/team.ts, src/subagent.ts, src/policy.ts, src/serve.ts, src/architect.ts, src/router.ts, configuration/registry code and test/patterns.test.ts
- Plausible first-party paths checked: Inspected whole-team usage aggregation, orchestrator delegates, member failure reporting, budget termination, serve operator access and abort/approval APIs.
- Why no material first-party path remains: The standard distribution exposes operational control primitives but does not supply whole-system regulatory judgment, shared commitment revision or a qualifying parent-control closure.


## S3* — Complementary audit

- State: C
- Function: The configurable evaluator pattern exposes a complementary code/artifact review path with corrective return.
- Disturbance / variety regulated: A generator's claimed completion may conceal defects in the changed workspace.
- Decisive decision or feedback right: A separately configured evaluator can inspect primary files, reject the candidate and return actionable defects that force another generator round.
- Decision owner: Constructor: the caller must bind an evaluator actor, evidence tools and independence constraints to the shipped evaluator role; verdict judgment belongs to that reviewer, not JSON parsing.
- Supporting / enforcement mechanisms: Fresh member context, retained evaluator tools, enforced pass/feedback schema, bounded revision rounds and generator-session continuation.
- Closure path: Generator candidate → separate evaluator run → pass/feedback verdict → generator revision with feedback, or stopped after maxRounds.
- Boundary reachability: The exported evaluator pattern copies the caller's evaluator Agent, retaining its independently selected tools, and invokes it via ctx.call. The documented read-only reviewer/ship composition shows the first-party constructor wiring. The example actor is not installed by default and is not credited as autonomous product ownership.
- Why this is / is not agent-owned: The code supplies an audit-specific judge/verdict/rework path; an application must still compose direct evidence access and independence. This supports C rather than A. A bare text-quality judge without complementary access would remain routine QA.
- Evidence: [Evaluator build and revision][R2], [member contexts][R5], [documented patterns][R7], [read-only reviewer reference][R10], [ship binding][R11], [evaluation boundary][R12].
- Basis: structural.
- Confidence: medium.
- Caveats: The external agent-layers evaluator implementations/runners are outside this boundary. No default installed reviewer or live audit success is claimed.

- Claim being audited: The producing agent's candidate/code change satisfies the requested task.
- Ordinary reporting path: The generator's completed output and own tool history.
- Complementary access path: A caller-bound reviewer with read/grep/glob can inspect actual workspace files rather than accept the completion narrative.
- Independence boundary: Separate evaluator Agent/context, separately selected tools/instructions; material independence remains a constructor obligation.
- Who acts on findings: The pattern returns negative feedback into the generator's continuing session and refuses unconditional completion.


## S4 — Outside-and-then intelligence

- State: —
- Function: No external-and-prospective adaptation closure is supplied.
- Disturbance / variety regulated: External research results, model alternatives and new agent designs can be processed as ordinary tasks.
- Decisive decision or feedback right: No supported regulator turns future-relevant distinctions into adaptation options and negotiated current-capability changes.
- Decision owner: Users request designs/configuration changes; agents perform the requested current task.
- Supporting / enforcement mechanisms: Architect writes/validates agent files; model router selects providers; memory, web/signal and integration hooks broaden S1 inputs.
- Closure path: Design files can be loaded later, but no first-party prospective sensing → adaptation judgment → current-capability conversation is wired.
- Why this is / is not agent-owned: Capability construction, request-level model routing, research tools and memory alone are not S4.
- Evidence: [Architect][R13], [router][R14], [architecture][R4], [configuration runtime][R3].
- Basis: structural.
- Confidence: high.
- Caveats: A user can author an adaptive organization with custom agents/plugins; it is not supplied by the stock runtime.

### Absence scope

- Surfaces inspected: README.md, docs/architecture.md, docs/patterns.md, docs/layers/eval.md, src/loop.ts, src/patterns.ts, src/team.ts, src/subagent.ts, src/policy.ts, src/serve.ts, src/architect.ts, src/router.ts, configuration/registry code and test/patterns.test.ts
- Plausible first-party paths checked: Inspected architect instructions/design validation, routedModel selection, signals/web integration, memory and configuration loading for external/future distinctions and an operational capability-return path.
- Why no material first-party path remains: The reviewed stock paths provide user-directed construction and task processing; no external/prospective adaptation loop or function-specific parent mode is shipped.


## S5 — Policy and identity

- State: —
- Function: No identity/ultimate-policy adjudication loop is supplied.
- Disturbance / variety regulated: Tool authorization, identities, prompts, guardrails and caller-selected configuration.
- Decisive decision or feedback right: No ultimate-policy issue is raised, decided by legitimate authority and returned as an authoritative governing decision.
- Decision owner: Developer/operator configures instructions and policy; external authorizers supply access decisions.
- Supporting / enforcement mechanisms: Ordered allow/deny/ask rules, optional identity verifier/PDP and workspace gates.
- Closure path: Authorization results govern individual tool calls; they do not close identity or unresolved S3–S4 policy tension.
- Why this is / is not agent-owned: Identity authentication and policy enforcement are not VSM S5 ownership; generic approve callbacks do not establish a parent S5 loop.
- Evidence: [Policy][R8], [HTTP identity boundary][R9], [runtime][R3], [architecture][R4].
- Basis: structural.
- Confidence: high.
- Caveats: External policy/identity adapters are explicitly out-of-repository implementations.

### Absence scope

- Surfaces inspected: README.md, docs/architecture.md, docs/patterns.md, docs/layers/eval.md, src/loop.ts, src/patterns.ts, src/team.ts, src/subagent.ts, src/policy.ts, src/serve.ts, src/architect.ts, src/router.ts, configuration/registry code and test/patterns.test.ts
- Plausible first-party paths checked: Checked identity/verifier/credentials/authorizer contracts, operator tokens, allow/ask/deny callbacks, agent instructions, architect guards and plugin configuration.
- Why no material first-party path remains: No shipped function-specific identity-level judgment/return path remains; constrained operation and configuration authority do not supply it.


## Distributed OSS parent arrangement

Maintainer code changes and independent users' agent files are not a shared project-level parent-governed VSM organization. No organization-level parent S3/S4/S5 return loop is credited.

## Self-hosted and non-human modes

Self-hosted CLI/HTTP/MCP settings and approval callbacks are supported. Operator-wide log visibility is observability; token/configuration access alone does not create function-specific parent control, adaptation or ultimate policy.

## Recursion

Teams may contain teams and delegates have separate run IDs/budgets, but the source does not establish a complete local metasystem for every nested member.

## Variety and escalation

Policies and budgets attenuate tool/resource variety; compaction/offloading reduce context, and external tools expand operational repertoire. Failures become explicit result data. No separate algedonic authority channel is established from event labels alone.

## Evidence gaps

Pinned-source assessment; no paid provider or live autonomous-agent run. Constructor S3* is conditional on a caller binding an independent raw-evidence reviewer; the stock text-only quality judge alone is not sufficient. External agent-layers evaluation and policy implementations were not credited.

[R1]: https://github.com/aantenore/reinloop/blob/358b8f677fc279155808c9e4bb8fe3cf443c00ab/src/loop.ts
[R2]: https://github.com/aantenore/reinloop/blob/358b8f677fc279155808c9e4bb8fe3cf443c00ab/src/patterns.ts
[R3]: https://github.com/aantenore/reinloop/blob/358b8f677fc279155808c9e4bb8fe3cf443c00ab/src/config/runtime.ts
[R4]: https://github.com/aantenore/reinloop/blob/358b8f677fc279155808c9e4bb8fe3cf443c00ab/docs/architecture.md
[R5]: https://github.com/aantenore/reinloop/blob/358b8f677fc279155808c9e4bb8fe3cf443c00ab/src/team.ts
[R6]: https://github.com/aantenore/reinloop/blob/358b8f677fc279155808c9e4bb8fe3cf443c00ab/src/subagent.ts
[R7]: https://github.com/aantenore/reinloop/blob/358b8f677fc279155808c9e4bb8fe3cf443c00ab/docs/patterns.md
[R8]: https://github.com/aantenore/reinloop/blob/358b8f677fc279155808c9e4bb8fe3cf443c00ab/src/policy.ts
[R9]: https://github.com/aantenore/reinloop/blob/358b8f677fc279155808c9e4bb8fe3cf443c00ab/src/serve.ts
[R10]: https://github.com/aantenore/reinloop/blob/358b8f677fc279155808c9e4bb8fe3cf443c00ab/examples/dev-team/agents/reviewer.md
[R11]: https://github.com/aantenore/reinloop/blob/358b8f677fc279155808c9e4bb8fe3cf443c00ab/examples/dev-team/agents/ship.md
[R12]: https://github.com/aantenore/reinloop/blob/358b8f677fc279155808c9e4bb8fe3cf443c00ab/docs/layers/eval.md
[R13]: https://github.com/aantenore/reinloop/blob/358b8f677fc279155808c9e4bb8fe3cf443c00ab/src/architect.ts
[R14]: https://github.com/aantenore/reinloop/blob/358b8f677fc279155808c9e4bb8fe3cf443c00ab/src/router.ts

---
harness_id: ag2
project_name: AG2
repository: https://github.com/ag2ai/ag2
review_ref: 3211bb19832049e7abe1a5742b6d177274bff723
reviewed_at: 2026-09-18
generated_profile_version: 0.2.2
generated_assessment_procedure_version: 0.3.1
profile_version: 0.2.2
assessment_procedure_version: 0.3.1
assessment_changed_at: 2026-09-18
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# AG2

## Review boundary

- System in focus: AG2 v1.0's first-party `Agent` runtime plus the opt-in `ag2.network` Hub/channel machinery at pinned revision `3211bb19832049e7abe1a5742b6d177274bff723`.
- Purpose and identity: provide reusable autonomous agent loops and protocol-driven multi-agent cooperation with tools, persistent context/knowledge, human-input hooks, typed channels, governance enforcement, and durable network state.
- Relevant environment: user/application requests, model providers, tools/APIs, human participants, external stores/transports, and peer agents connected to a configured AG2 Network.
- Standard-distribution boundary: the `ag2` package and first-party documentation/tests at the pinned revision. AG2 Classic (`ag2ai/ag2-classic`), application-specific agents/policies, external model providers, and downstream custom Hub/Arbiter implementations are outside the credited boundary.
- First-party operating / deployment modes considered: standalone `Agent`; optional harness primitives (`assembly`, `knowledge`, `tasks`); local or distributed `Network` Hub with built-in conversation/consulting/discussion/workflow adapters; optional HITL hooks and human network clients.
- Recursion level: one configured AG2 agent organization. Individual autonomous `Agent` instances are candidate S1 units; nested task/subagent calls are not treated as VSM recursion by themselves.
- Reviewed revision: `3211bb19832049e7abe1a5742b6d177274bff723`.
- Observation date: 2026-09-18.
- Generated Profile version: `0.2.2`.
- Generated Methodology version: `0.3.1`.
- Current Profile version: `0.2.2`.
- Current Methodology version: `0.3.1`.

## Primary evidence

- [`README.md`](https://github.com/ag2ai/ag2/blob/3211bb19832049e7abe1a5742b6d177274bff723/README.md) — v1.0 boundary, core `Agent`, tools, HITL, Network and harness primitives; explicitly separates AG2 Classic into another repository.
- [`ag2/agent.py`](https://github.com/ag2ai/ag2/blob/3211bb19832049e7abe1a5742b6d177274bff723/ag2/agent.py) — autonomous model/tool loop, streams, optional knowledge/assembly/task harness features, subtask tooling and per-stream turn serialization.
- [`website/docs/user-guide/network/overview.mdx`](https://github.com/ag2ai/ag2/blob/3211bb19832049e7abe1a5742b6d177274bff723/website/docs/user-guide/network/overview.mdx) — authoritative Hub state, typed adapters, enforceable turn order, governance rules, WAL/audit and distributed deployment.
- [`ag2/network/adapters/discussion.py`](https://github.com/ag2ai/ag2/blob/3211bb19832049e7abe1a5742b6d177274bff723/ag2/network/adapters/discussion.py) — concrete multi-participant round-robin regulation, out-of-turn rejection and expected-turn feedback.
- [`website/docs/user-guide/network/expectations_and_audit.mdx`](https://github.com/ag2ai/ag2/blob/3211bb19832049e7abe1a5742b6d177274bff723/website/docs/user-guide/network/expectations_and_audit.mdx) — expectation evaluators/handlers, ordinary audit log, read-only listeners and the customizable pre-commit `HubArbiter` decision seam.
- [`website/docs/user-guide/network/hub_and_identity.mdx`](https://github.com/ag2ai/ag2/blob/3211bb19832049e7abe1a5742b6d177274bff723/website/docs/user-guide/network/hub_and_identity.mdx) — per-agent rules, authoritative Hub state, observed capability statistics, health snapshots and sweepers.
- [`website/docs/user-guide/context/human_in_the_loop.mdx`](https://github.com/ag2ai/ag2/blob/3211bb19832049e7abe1a5742b6d177274bff723/website/docs/user-guide/context/human_in_the_loop.mdx) — structured human confirmation/information hooks and fail-closed approval behavior.

## Repository architecture

AG2 v1.0 is distinct from AG2 Classic. A first-party `Agent` drives a model/tool loop over a stream: the model chooses tool calls, AG2 executes them, returned observations enter the same run/history, and subsequent model decisions continue the trajectory. Optional harness features add persistent knowledge, assembly/compaction and bounded subtask agents without changing that primary operational ownership.

For multi-agent operation, `ag2.network` adds one authoritative Hub, thin agent clients, durable channel WALs and four built-in channel protocols. `discussion` is explicitly a multi-party turn-taking protocol; `consulting` imposes strict request/reply order; `workflow` follows a developer-supplied transition graph. The Hub also enforces per-agent access/limit rules and adapter expectations. Its audit/listener surfaces observe ordinary Hub state, while a tenant may replace or extend the policy decision seam through `HubArbiter`.

This assessment therefore distinguishes a supplied coordination function from broader framework expressiveness. AG2's built-in discussion protocol provides a concrete S2 disturbance/regulation witness. In contrast, Hub rules, health state, listeners and custom arbiters are useful governance infrastructure but do not themselves establish a first-party autonomous or constructor-owned S3/S3*/S4/S5 organizational loop under the current function-first thresholds.

## Operational model

The S1 units are model-driven `Agent` loops that directly transform requests into tool/model actions and results. A standalone agent may operate independently; a Network can place multiple agents behind one Hub and bind their exchanges to typed channel semantics.

Developer/application configuration chooses agents, prompts, tools, channel types, transition graphs, rules and optional HITL hooks. The runtime executes and enforces those choices. Where an agent itself owns a task-local model/tool decision, ownership is autonomous. Where the runtime supplies a concrete organizational regulation but no autonomous agent owns its decisive coordination discretion, the result is constructor-owned rather than agent-owned.

## S1 — Operations

- State: `A`.
- Function: autonomous agent loops perform the primary task transformation through model decisions and tool actions.
- Disturbance / variety regulated: user/task uncertainty, model outputs, tool/environment feedback, persistent conversational state and task-local exceptions.
- Decisive decision or feedback right: choose the next model/tool action and revise the trajectory from returned observations.
- Decision owner: the model-driven `Agent` actor.
- Supporting / enforcement mechanisms: stream/history, tool execution, middleware, response validation, optional knowledge/assembly, subtask tools and runtime cancellation.
- Closure path: tool/model results are appended to the run/stream and enter later model requests, changing subsequent action.
- Why agent-owned: first-party source defines `Agent` as the agentic unit that runs the model loop and invokes tools; the README describes the model deciding when to call tools.
- Evidence: README and `ag2/agent.py` at the pinned revision.
- Basis: `explicit` and `structural`.
- Confidence: high.
- Caveats: developer configuration constrains prompts/tools/providers, but the operational choice within those bounds remains model-owned.

## S2 — Coordination

- State: `C`.
- Distinct S1 units: two or more autonomous `Agent` instances participating in a Network discussion.
- Specific inter-S1 disturbance: multiple participants share one conversational work channel and can otherwise attempt to speak out of sequence or stall an expected turn, producing conversational collision/oscillation and blocking progress.
- Coordination relation: the first-party `DiscussionAdapter` snapshots participant order, exposes one `expected_next_speaker`, rejects any out-of-turn `EV_TEXT`, rotates the expected speaker after each accepted message, and publishes `turn_within` expectations for delayed turns.
- Disturbance attenuation: deterministic Hub/adapter enforcement serializes the common conversational floor; expectation feedback can warn or hide a participant that fails to take its expected turn.
- Decisive decision or feedback right: the supplied protocol determines which participant may speak next and whether an attempted send is admissible; the developer chooses to compose the agents into this discussion mode rather than an autonomous agent choosing the coordination rule.
- Decision owner: first-party deterministic runtime / developer-composed channel protocol, not an autonomous coordinating agent.
- Supporting / enforcement mechanisms: authoritative Hub state, channel WAL, adapter state folding, validation, expectation sweeper and violation handlers.
- Closure path: accepted turns advance `expected_next_speaker`; rejected out-of-turn sends return a protocol error; expectation violations feed channel warnings/hiding back into later participant behavior.
- Why this is S2-specific rather than generic messaging: the primitive is explicitly a multi-participant turn-taking regulator with an evidenced collision/stall mode and enforced feedback, not merely a mailbox/router/graph edge. The standard distribution supplies the regulation, but autonomous coordination ownership must still be composed, so the publication state is `C`, not `A`.
- Evidence: Network overview and `DiscussionAdapter` implementation.
- Basis: `explicit` and `structural`.
- Confidence: high.
- Caveats: `conversation` free-form messaging and generic `workflow` sequencing are not independently promoted to S2; the positive claim rests on the concrete discussion turn-regulation path.

## S3 — Inside-and-now control

- State: `—`.
- Function finding: the Hub centralizes current network state and enforces rules, but no first-party actor/path was established that combines a whole-system current view with discretionary authority over shared resources, commitments, priorities, accountability or intervention on behalf of the organization as a whole.
- Disturbance / variety regulated: access limits, inbox pressure, delegation depth, channel counts and TTLs are runtime constraints, not by themselves S3 organizational decisions.
- Decisive decision or feedback right: not established for S3. The default `RuleBasedArbiter` applies tenant/developer-selected rules; custom `HubArbiter` subclasses are extension points whose S3 semantics, if any, belong to downstream composition.
- Decision owner: not established.
- Supporting / enforcement mechanisms: Hub `health()`, registry/channel state, `Rule`, `RuleBasedArbiter`, rate/inbox/access checks, TTL/expectation sweepers and HITL hooks.
- Closure path: the runtime can allow/deny individual network actions and auto-close channels, but this closes enforcement decisions selected elsewhere rather than a first-party whole-system current-control loop.
- Why not `C`: a generic/customizable policy gate plus central telemetry does not establish the S3 function before autonomy classification. The developer would need to supply the whole-system regulatory judgment itself, not merely its autonomous owner.
- Evidence: Hub/Identity and Governance/Audit documentation.
- Basis: `structural`.
- Confidence: high.
- Caveats: a downstream application can implement an S3-capable arbiter or manager against these primitives; that composed system requires its own assessment boundary.

## S3* — Complementary audit

- State: `—`.
- Claim being audited: channel/rule/expectation events and operational state are recorded by the Hub audit/listener path.
- Ordinary reporting path: the Hub's own registry, WAL, state transitions and expectation evaluators.
- Complementary access path: none established. The built-in `AuditLog` is itself a Hub listener receiving the same committed transitions, and expectation evaluators inspect the same channel metadata/WAL state.
- Independence boundary: no materially independent operational-evidence path is supplied by default.
- Decisive audit judgment / owner: not established.
- Supporting / enforcement mechanisms: append-only audit log, `HubListener`, expectation evaluators, task observations and custom listener hooks.
- Closure path: expectation violations can warn/close channels, but that is ordinary protocol monitoring/enforcement rather than complementary independent audit.
- Why not `C`: custom listeners/evaluators can be attached, but the standard distribution does not supply an S3*-specific independent evidence/judgment path; generic extension is insufficient.
- Evidence: Governance/Audit documentation.
- Basis: `structural`.
- Confidence: high.
- Caveats: a downstream independent auditor using different evidence could establish S3* in a composed system.

## S4 — Outside-and-then intelligence

- State: `—`.
- External distinction: agents can use tools and external services during current task execution.
- Future/prospective distinction: no distinct first-party environmental/future model was established for organizational adaptation.
- Adaptation option generated: none at the harness-organization capability level.
- Path back into current capability / S3: none established.
- Decision owner: not applicable.
- Supporting mechanisms: persistent knowledge, history compaction/assembly, observed capability statistics, tools, middleware and application-defined workflows.
- Closure path: those mechanisms alter context or record retrospective performance, but no outside-and-then adaptation loop is supplied.
- Evidence: agent harness and Hub/Identity surfaces reviewed at the pin.
- Basis: `structural`.
- Confidence: high.
- Caveats: learning, compaction, retrospective task statistics and current external tool use are not S4 by themselves.

## S5 — Policy and identity

- State: `—`.
- Identity / ultimate-policy issue: no first-party runtime path was established for resolving identity/ultimate-policy tensions for the configured agent organization.
- Ultimate authority: developers/operators select prompts, models, tools, passports, rules, auth adapters, channel manifests and HITL hooks; those configuration choices are not themselves a runtime S5 loop.
- Decisive decision or feedback right: no identity/ultimate-policy issue-to-authority-to-return path was established.
- Supporting / enforcement mechanisms: `Passport`, `Rule`, authentication, access/limit enforcement, system prompts and human approval hooks.
- Return-to-operation path: ordinary HITL approval returns to the current tool trajectory, but the documented cases are task/safety approvals rather than identity-level policy closure.
- Why not `C` or `P`: configurable policy/enforcement surfaces and generic human approval do not establish S5 before ownership is classified.
- Evidence: Hub/Identity and HITL documentation.
- Basis: `structural`.
- Confidence: high.
- Caveats: a downstream organization may place ultimate policy at a human or institutional parent, but AG2 does not establish that function at this reviewed boundary.

## Recursion

AG2 can spawn subtasks/subagents and can host several named agents in a Network. That demonstrates decomposition and multi-agent composition, not recursive viability. The reviewed standard distribution does not establish that each child/team unit carries its own complete metasystem and parent-level channels, so no stronger VSM recursion claim is made.

## Variety and escalation

Operational variety is amplified by tools, middleware, subagents, knowledge and distributed Network participants. Typed channel protocols, round-robin validation, access/inbox/delegation limits, TTLs and expectation handlers attenuate communication and resource-pressure variety. WAL/audit/state surfaces preserve evidence across those transitions.

Escalation is explicit at the operational level through protocol errors, expectation violations, failed turns and optional human-input requests. Those paths improve reliability but are not promoted to S3-S5 unless the corresponding organizational function and ownership loop are independently established.

## Evidence gaps

No unresolved gap requires `?`. The review inspected the strongest first-party candidates for higher functions: Network coordination, Hub governance/arbitration, audit/listeners, observed capability state, harness memory/compaction and HITL. Only the discussion turn-regulation path meets a metasystem function threshold under Profile `0.2.2` / Methodology `0.3.1`.

## Admission conclusion

Canonical vector: `A C — — — —`.

AG2 v1.0 is admitted as an autonomous agent harness/framework. Its standard distribution supplies autonomous S1 and a concrete constructor-owned S2 path for multi-agent conversational turn regulation. Central Hub state, rules/arbitration, audit/observability, learning-like harness features and human approval remain supporting/configurable mechanisms rather than established S3, S3*, S4 or S5 closure.
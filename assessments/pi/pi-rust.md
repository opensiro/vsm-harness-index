---
harness_id: pi-rust
project_name: pi-rust
repository: https://github.com/yannelli/pi-rust
review_ref: 965fdef64353849da37ad7b9e419cdb5fe8bfacd
reviewed_at: 2026-10-27
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# pi-rust

## Review boundary

- System in focus: the distributed pi coding CLI and its first-party pi-agent/session runtime, including library hooks and normal editor transports.
- Purpose and identity: perform coding work through streaming model/tool sessions in Rust.
- Relevant environment: workspace files/commands, model providers, MCP servers, user/editor clients and installed extensions.
- Standard-distribution boundary: pi-coding-agent binary and wired runtime libraries; generic SDK/transport APIs are inspected as construction support, not presumed autonomous organizations.
- Credited operating / distribution surfaces: crates/pi-agent/src/agent_loop.rs and tool_execution.rs; pi-coding-agent session, built-in tool, configuration, interactive/print/RPC/ACP and resource modules.
- Adjacent first-party surfaces excluded from ownership: pi-evals host/model evaluations and documentation-audit agent; test fixtures, release provenance machinery, contributor agents and arbitrary consumer-written extensions/hosts.
- First-party operating / deployment modes considered: interactive, print/JSON, RPC and ACP; persisted/resumed sessions; local or hosted models; SDK loop/hooks as shipped.
- Recursion level: one coding-agent session; multiple hosted sessions and nested tool calls are not presumed recursive operational organizations.
- Reviewed revision: 965fdef64353849da37ad7b9e419cdb5fe8bfacd.
- Observation date: 2026-10-27.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The pi-agent library runs stream → tool execution → returned results until completion, steering/follow-up or cancellation. pi-coding-agent composes session trees, resources, model runtime, MCP/extensions, compaction, tools and transports. Hooks can alter request context and continuation; these are generic lifecycle extension points. Run limits enforce user-selected cost/turn bounds. /review sends a raw-diff review prompt through the same active session. A separate pi-evals documentation-audit harness is development evaluation and does not own installed-product audit.

## Operational model

The session model owns tool/argument/continuation choices. Runtime hooks, tool execution, schemas, trust and cost limits support that local S1. No supplied cross-unit coordination, supervisory resource bargain, independent product audit or prospective adaptation process is inferred from generic extension expressiveness.

## S1 — Operations

- State: A
- Function: transform coding requests into file/tool actions and completed responses.
- Disturbance / variety regulated: task-specific code state, errors, user steering and context limits.
- Decisive decision or feedback right: choose the next tool/action and whether to continue from returned observations.
- Decision owner: the configured session's model-backed agent.
- Supporting / enforcement mechanisms: stream adapter, tool registry/schema validation, before/after hooks, session history, compaction, cancellation and run limits.
- Closure path: run_loop executes model tool calls, appends their results and starts subsequent turns; installed sessions wire request/turn hooks and active tools.
- Boundary reachability: the shipped pi CLI constructs the session and calls pi-agent; users select a provider rather than implementing a new loop.
- Why this is / is not agent-owned: without the model, execution machinery cannot choose task-specific actions or answers.
- Evidence: [shipped modes](https://github.com/yannelli/pi-rust/blob/965fdef64353849da37ad7b9e419cdb5fe8bfacd/README.md#L83-L112); [loop construction](https://github.com/yannelli/pi-rust/blob/965fdef64353849da37ad7b9e419cdb5fe8bfacd/crates/pi-agent/src/agent_loop.rs#L160-L200); [decision/action continuation](https://github.com/yannelli/pi-rust/blob/965fdef64353849da37ad7b9e419cdb5fe8bfacd/crates/pi-agent/src/agent_loop.rs#L202-L290); [tool pipeline](https://github.com/yannelli/pi-rust/blob/965fdef64353849da37ad7b9e419cdb5fe8bfacd/crates/pi-agent/src/tool_execution.rs#L61-L99); [session wiring](https://github.com/yannelli/pi-rust/blob/965fdef64353849da37ad7b9e419cdb5fe8bfacd/crates/pi-coding-agent/src/agent_session/hooks.rs#L1-L78).
- Basis: structural.
- Confidence: high.
- Caveats: Source-relative finding; no empirical model-quality claim.

## S2 — Coordination

- State: —
- Function: no shipped inter-S1 interference-regulation relation at the session boundary established.
- Disturbance / variety regulated: independently acting work cells could collide, but parallel tools are not distinct S1 units.
- Decisive decision or feedback right: no coordination-specific peer-conflict decision/return supplied.
- Decision owner: none established for S2.
- Supporting / enforcement mechanisms: sequential/parallel tool execution, steering/follow-up queues, session/settings locks and transport routing.
- Closure path: tool events and queued messages return within one agent loop; this is ordinary execution sequencing.
- Why this is / is not agent-owned: generic hooks and nested calls do not establish mutual regulation among distinct operational units.
- Evidence: [loop/queues](https://github.com/yannelli/pi-rust/blob/965fdef64353849da37ad7b9e419cdb5fe8bfacd/crates/pi-agent/src/agent_loop.rs#L202-L290); [nested tool boundary](https://github.com/yannelli/pi-rust/blob/965fdef64353849da37ad7b9e419cdb5fe8bfacd/crates/pi-agent/src/nested.rs#L1-L35); [tool batch API](https://github.com/yannelli/pi-rust/blob/965fdef64353849da37ad7b9e419cdb5fe8bfacd/crates/pi-agent/src/tool_execution.rs#L1-L59).
- Basis: structural.
- Confidence: high.
- Caveats: Source-relative finding; no empirical model-quality claim.

### Absence scope

- Surfaces inspected: agent loop, tool execution/nesting, session services, steering queues and installed RPC/ACP modes.
- Plausible first-party paths checked: parallel tool calls, separate sessions, nested tool host, locks and external extensions.
- Why no material first-party path remains: the supplied mechanisms serialize or route local execution/state; no specific conflict among distinct S1 work units and coordination feedback is packaged at this boundary.

## S3 — Inside-and-now control

- State: —
- Function: no separate whole-system current-control process established.
- Disturbance / variety regulated: session cost/context pressure is bounded locally rather than through supervisory bargaining.
- Decisive decision or feedback right: no agent or function-specific parent right to revise cross-unit commitments/resources supplied.
- Decision owner: none established for S3; CLI user selects fixed local limits.
- Supporting / enforcement mechanisms: max-turn/max-cost stop, session stats, cancellation, generic finish_turn/prepare_request hooks.
- Closure path: limits stop local work and hooks permit arbitrary embedding; neither supplies an S3-specific supervisory loop.
- Why this is / is not agent-owned: autonomous coding within limits is S1; a hook able to replace a model is not automatically S3=C.
- Evidence: [run-limit selection and enforcement](https://github.com/yannelli/pi-rust/blob/965fdef64353849da37ad7b9e419cdb5fe8bfacd/crates/pi-coding-agent/src/agent_session/run_limits.rs#L18-L36); [local stop](https://github.com/yannelli/pi-rust/blob/965fdef64353849da37ad7b9e419cdb5fe8bfacd/crates/pi-coding-agent/src/agent_session/run_limits.rs#L110-L165); [generic hook surface](https://github.com/yannelli/pi-rust/blob/965fdef64353849da37ad7b9e419cdb5fe8bfacd/crates/pi-agent/src/agent_loop.rs#L77-L116).
- Basis: structural.
- Confidence: high.
- Caveats: Source-relative finding; no empirical model-quality claim.

### Absence scope

- Surfaces inspected: run limits, session stats/configuration, cancellation, request/turn hooks and editor transports.
- Plausible first-party paths checked: operator cost limits, hook-directed continuation/model replacement and multiple hosted sessions.
- Why no material first-party path remains: only local run enforcement or generic composition is supplied, without a whole-system control view/decision and returned commitment change.

## S3* — Complementary audit

- State: —
- Function: no sufficiently independent complementary audit of installed operational claims established.
- Disturbance / variety regulated: bugs or false completion claims in code changes.
- Decisive decision or feedback right: no audit-specific independent owner and corrective-control return supplied.
- Decision owner: none established for S3*.
- Supporting / enforcement mechanisms: /review raw diff/status prompt, session transcript and separate pi-evals documentation audit.
- Closure path: /review is sent as an ordinary prompt to the same active session; evaluation audits belong to an adjacent host purpose.
- Why this is / is not agent-owned: a model reviewing its own context in a normal prompted task does not supply the required independent complementary channel.
- Evidence: [same-session review implementation](https://github.com/yannelli/pi-rust/blob/965fdef64353849da37ad7b9e419cdb5fe8bfacd/crates/pi-coding-agent/src/interactive/review.rs#L1-L52); [adjacent documentation audit](https://github.com/yannelli/pi-rust/blob/965fdef64353849da37ad7b9e419cdb5fe8bfacd/crates/pi-evals/evals/documentation-audit.eval.rs#L1-L65).
- Basis: structural.
- Confidence: high.
- Caveats: Source-relative finding; no empirical model-quality claim.

### Absence scope

- Surfaces inspected: interactive review/diff command, session prompt routing, raw-artifact tools, hooks and pi-evals audit wiring.
- Plausible first-party paths checked: user-triggered /review with git evidence, extension hooks and the host documentation-audit evaluator.
- Why no material first-party path remains: the installed review uses the same operational model/session, generic hooks supply no independent audit contract, and the developer evaluator is outside the product boundary.

## S4 — Outside-and-then intelligence

- State: —
- Function: no outside-and-future capability-adaptation loop established.
- Disturbance / variety regulated: changing provider/model availability and future coding needs.
- Decisive decision or feedback right: no prospective option-development/adoption feedback owner supplied.
- Decision owner: none established.
- Supporting / enforcement mechanisms: model catalogs, update commands, package/skill installation, context compaction and /init instructions.
- Closure path: catalog refresh changes available models; user selection and ordinary task-derived context do not themselves close prospective adaptation.
- Why this is / is not agent-owned: automatic catalog freshness, software update and current-task planning are not S4.
- Evidence: [catalog/update and selection](https://github.com/yannelli/pi-rust/blob/965fdef64353849da37ad7b9e419cdb5fe8bfacd/README.md#L75-L105); [provider catalog refresh](https://github.com/yannelli/pi-rust/blob/965fdef64353849da37ad7b9e419cdb5fe8bfacd/README.md#L209-L225); [resource services](https://github.com/yannelli/pi-rust/blob/965fdef64353849da37ad7b9e419cdb5fe8bfacd/crates/pi-coding-agent/src/agent_session/services.rs#L40-L95); [turn context preparation](https://github.com/yannelli/pi-rust/blob/965fdef64353849da37ad7b9e419cdb5fe8bfacd/crates/pi-coding-agent/src/agent_session/hooks.rs#L26-L43).
- Basis: structural.
- Confidence: high.
- Caveats: Source-relative finding; no empirical model-quality claim.

### Absence scope

- Surfaces inspected: model registry/update commands, package/resources/skills, /init, compaction and request-model hooks.
- Plausible first-party paths checked: external model discovery, self-update, changing loaded skills and adaptive context projection.
- Why no material first-party path remains: the paths refresh/configure current execution; no supplied future-relevant option generation and two-way return to supervisory capability is wired.

## S5 — Policy and identity

- State: —
- Function: no identity/ultimate-policy dispute and authoritative-return path established.
- Disturbance / variety regulated: system-level purpose or ultimate risk decisions would require distinct authority.
- Decisive decision or feedback right: context prompts, project trust and extension permissions do not establish ultimate-policy settlement.
- Decision owner: none established for S5.
- Supporting / enforcement mechanisms: SYSTEM/APPEND_SYSTEM/AGENTS resources, project trust decisions, tool hooks and user/editor commands.
- Closure path: trusted resources govern subsequent requests as configuration, without a supplied identity issue reaching legitimate ultimate authority and returning as a decision.
- Why this is / is not agent-owned: instructions and ordinary consent are constraints on S1, not S5 by presence.
- Evidence: [configuration surfaces](https://github.com/yannelli/pi-rust/blob/965fdef64353849da37ad7b9e419cdb5fe8bfacd/README.md#L187-L207); [resource trust scope](https://github.com/yannelli/pi-rust/blob/965fdef64353849da37ad7b9e419cdb5fe8bfacd/crates/pi-coding-agent/src/agent_session/services.rs#L40-L85); [prompt builder](https://github.com/yannelli/pi-rust/blob/965fdef64353849da37ad7b9e419cdb5fe8bfacd/crates/pi-coding-agent/src/system_prompt.rs#L137-L170).
- Basis: structural.
- Confidence: high.
- Caveats: Source-relative finding; no empirical model-quality claim.

### Absence scope

- Surfaces inspected: system prompts/resources, startup trust, session user steering, extension loading and project governance boundaries.
- Plausible first-party paths checked: prompt override/reload, project/package approval and ordinary user corrections.
- Why no material first-party path remains: these paths configure or constrain sessions; no function-specific ultimate identity/policy authority and returned settlement is supplied.

## Distributed OSS parent arrangement

Project contributors and release governance are adjacent to the installed harness. No organization-level parent ownership is inferred from contributor identities.

## Self-hosted and non-human modes

The same local model/tool decision loop is available in CLI and editor transports. SDK hooks or installed third-party extensions can add custom behavior, which is not credited as a shipped organizational function. No parent modifier is established.

## Recursion

Nested tool calls record execution lineage, not nested viable systems. Multiple sessions and transport hosts do not imply a built-in coordinating metasystem.

## Variety and escalation

Steering/follow-up and tool error returns preserve operational feedback; transcript trees, compaction and run limits bound local state/cost. Ordinary cancellation or JSON events do not alone establish algedonic/S3 authority.

## Evidence gaps

Static pinned-source assessment only; no live coding-agent/model/evaluation runs. Cargo is unavailable on the inspection host, so Rust tests were not executed or reported PASS. The separate pi-evals audit is explicitly excluded from installed runtime ownership. Profile main is unchanged; current Skills main was inspected, while Index remains pinned to Methodology 0.3.7.

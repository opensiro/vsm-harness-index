---
harness_id: nexo
project_name: nexo
repository: https://github.com/Locotir/nexo
review_ref: a9643683250aeff6050d0b77adfed0fe9392e53c
reviewed_at: 2026-11-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-11-04
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# nexo

## Review boundary

- System in focus: The installable nexo terminal coding assistant, including the first-party model/tool loop, permission gate, optional task subagents, persistent sessions, context curator, and CLI.
- Purpose and identity: Perform repository coding work under user-given goals while retaining an exact recoverable history and presenting selected context to the model.
- Relevant environment: Local source tree and shell, user approvals, provider endpoints, files/tests, model context limits, external web/MCP tools and changing coding tasks.
- Standard-distribution boundary: The shipped Rust `nexo-cli` composition with `nexo-agent`, `nexo-core`, provider and tool crates; optional built-in `explore` and `general` task subagents. An external model endpoint is needed for live inference.
- Credited operating / distribution surfaces: [agent turn](https://github.com/Locotir/nexo/blob/a9643683250aeff6050d0b77adfed0fe9392e53c/nexo/crates/nexo-agent/src/turn.rs), [subagent](https://github.com/Locotir/nexo/blob/a9643683250aeff6050d0b77adfed0fe9392e53c/nexo/crates/nexo-agent/src/subagent.rs), [permissions](https://github.com/Locotir/nexo/blob/a9643683250aeff6050d0b77adfed0fe9392e53c/nexo/crates/nexo-agent/src/permission.rs), [session](https://github.com/Locotir/nexo/blob/a9643683250aeff6050d0b77adfed0fe9392e53c/nexo/crates/nexo-agent/src/session.rs), [context curator](https://github.com/Locotir/nexo/blob/a9643683250aeff6050d0b77adfed0fe9392e53c/nexo/crates/nexo-agent/src/brief.rs).
- Adjacent first-party surfaces excluded from ownership: Benchmark and offline fixture replay, CI, release process, docs' measured examples, developer-maintained prompts/agent profile files; third-party provider and MCP server internals.
- First-party operating / deployment modes considered: Interactive/human-approval mode, headless execution, goal continuation, optional read-only background exploration versus foreground writable subagent, resumed/forked sessions.
- Recursion level: One coding session/goal with agent-selected tool actions; task subagents are bounded workers and do not by their existence prove recursive viability.
- Reviewed revision: `a9643683250aeff6050d0b77adfed0fe9392e53c`.
- Observation date: 2026-11-04.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The CLI composes a first-party `turn::run` session with model client, tool set, permission gate and durable history. `run_turn` repeatedly prepares model requests, streams replies, executes model-selected tool calls, appends outcomes and stops at final answer, budget or cancellation. An optional `task` tool launches nested loops with capped rounds and a returned report. Built-in `explore` is read-only and can work as a background job; file-changing `general` works in foreground and uses the main session's permission decisions. Session resumption, fork/rewind, brief/curator selection, provider fallback and loop/stale guards protect the coding process but do not independently supply higher VSM governance. The user can configure permissions, models and goals; a model service provides inference, not the native orchestration. [README](https://github.com/Locotir/nexo/blob/a9643683250aeff6050d0b77adfed0fe9392e53c/README.md), [turn.rs#L165-L240](https://github.com/Locotir/nexo/blob/a9643683250aeff6050d0b77adfed0fe9392e53c/nexo/crates/nexo-agent/src/turn.rs#L165-L240), [turn.rs#L1221-L1440](https://github.com/Locotir/nexo/blob/a9643683250aeff6050d0b77adfed0fe9392e53c/nexo/crates/nexo-agent/src/turn.rs#L1221-L1440), [subagent.rs#L1-L96](https://github.com/Locotir/nexo/blob/a9643683250aeff6050d0b77adfed0fe9392e53c/nexo/crates/nexo-agent/src/subagent.rs#L1-L96).

## Operational model

One model-driven coding loop interprets a user goal and chooses read/edit/shell/search and optional delegated tasks. Tool results return for the next model decision; the session is the accountable unit. A read-only search child can be another temporary S1 work cell, but bounded task allocation and eventual report aggregation do not alone establish an independently viable level or an inter-unit metasystem. Permissions, budgets and context selection are deterministic constraints around the agent's coding discretion.

## S1 — Operations

- State: A
- Function: Execute coding requests by repeatedly choosing tools, inspecting source/environment feedback, revising edits and returning an answer.
- Disturbance / variety regulated: Unfamiliar repository structure, failed commands/tests, permission denials, context-window pressure and changing task instructions.
- Decisive decision or feedback right: Choose the next coding/tool action or task subagent after inspecting the prior feedback and judge when the task response is complete.
- Decision owner: Model-driven agent in the shipped `run_turn` loop; the human supplies the task and approval boundary, while Rust handles transport and enforcement.
- Supporting / enforcement mechanisms: Tool registry, permission gate, max turns/cost, cancellation, context curator, sessions/checkpoints, loop/stale guards.
- Closure path: User goal → model decision → first-party tool dispatch/permission → result or refusal appended to history → next model decision/final response.
- Boundary reachability: `turn::run` constructs session, client, tools and optional `SubAgent`; `run_turn` is directly used by the supported CLI/headless composition.
- Why this is / is not agent-owned: The substantive tool and code choices are returned by the model; the fixed gates do not select the edits.
- Evidence: [turn.rs#L165-L240](https://github.com/Locotir/nexo/blob/a9643683250aeff6050d0b77adfed0fe9392e53c/nexo/crates/nexo-agent/src/turn.rs#L165-L240), [turn.rs#L1221-L1440](https://github.com/Locotir/nexo/blob/a9643683250aeff6050d0b77adfed0fe9392e53c/nexo/crates/nexo-agent/src/turn.rs#L1221-L1440), [turn.rs#L1830-L1980](https://github.com/Locotir/nexo/blob/a9643683250aeff6050d0b77adfed0fe9392e53c/nexo/crates/nexo-agent/src/turn.rs#L1830-L1980).
- Basis: structural
- Confidence: high for the shipped decision/feedback loop.
- Caveats: No paid-provider execution or benchmark success was independently reproduced in this review.

## S2 — Coordination

- State: —
- Function: No first-party cross-S1 conflict-and-oscillation regulation is established beyond bounded delegation and tool safety.
- Disturbance / variety regulated: Concurrent edits could interfere, but the shipped `task` design runs file-changing children in foreground and confines background children to read-only work.
- Decisive decision or feedback right: Detect an inter-S1 collision and choose a mutual adjustment returned into two operational cells; no such S2-specific decision path is shipped.
- Decision owner: No qualifying S2 actor; deterministic subagent mode restrictions and the parent task selection manage task execution locally.
- Supporting / enforcement mechanisms: Read-only profile, foreground writing, task report, shared host permission gate and session job tracking.
- Closure path: Child task → report → parent coding loop; no evidenced two-unit collision signal and negotiated/adjusted subsequent worker behaviour.
- Why this is / is not agent-owned: Agent delegation and a serial-write safety rule are not the four-part S2 disturbance/attenuation/feedback witness.
- Evidence: [subagent.rs#L1-L96](https://github.com/Locotir/nexo/blob/a9643683250aeff6050d0b77adfed0fe9392e53c/nexo/crates/nexo-agent/src/subagent.rs#L1-L96), [subagent.rs#L174-L233](https://github.com/Locotir/nexo/blob/a9643683250aeff6050d0b77adfed0fe9392e53c/nexo/crates/nexo-agent/src/subagent.rs#L174-L233), [turn.rs#L165-L190](https://github.com/Locotir/nexo/blob/a9643683250aeff6050d0b77adfed0fe9392e53c/nexo/crates/nexo-agent/src/turn.rs#L165-L190).
- Basis: structural
- Confidence: medium-high within the standard distribution.
- Caveats: A user can construct a multi-session development team externally; that is not established by nexo's built-in task tool.

### Absence scope

- Surfaces inspected: Built-in/custom subagent profiles, host permit/spend API, background job rules, main session tool dispatch, task reports and README operational mode.
- Plausible first-party paths checked: Parallel exploration, writable delegation, shared permission decisions and agent task return.
- Why no material first-party path remains: These paths bound or serialize child actions rather than recognize a concrete conflict between distinct S1 cells and feed an S2-specific corrective adjustment to both.

## S3 — Inside-and-now control

- State: —
- Function: No separately established whole-system current control over a portfolio of operational units.
- Disturbance / variety regulated: Overspend, repetitive tool loops and stuck goal continuation inside one session.
- Decisive decision or feedback right: Reallocate shared priorities/resources across distinct S1 units after a whole-current judgment; not supplied.
- Decision owner: User chooses budget/permission limits, model chooses ordinary local work, deterministic runtime enforces stops.
- Supporting / enforcement mechanisms: Session budget, max-turns, day cost, repeat/stale guards, job kill/status and permission modes.
- Closure path: Guard stops or constrains the same coding turn; no whole-system allocation decision returns to multiple operational units.
- Why this is / is not agent-owned: A cap or kill mechanism is enforcement, not an agent-owned S3 resource bargaining decision.
- Evidence: [turn.rs#L1221-L1277](https://github.com/Locotir/nexo/blob/a9643683250aeff6050d0b77adfed0fe9392e53c/nexo/crates/nexo-agent/src/turn.rs#L1221-L1277), [turn.rs#L455-L527](https://github.com/Locotir/nexo/blob/a9643683250aeff6050d0b77adfed0fe9392e53c/nexo/crates/nexo-agent/src/turn.rs#L455-L527).
- Basis: structural
- Confidence: medium-high.
- Caveats: The human user's wider coding organization was outside this session boundary.

### Absence scope

- Surfaces inspected: Budget/limits, turn lifecycle, jobs, user commands, permission policy and subagent host.
- Plausible first-party paths checked: Per-session cost limits, goal continuation, background job cancellation and parent-child task selection.
- Why no material first-party path remains: No whole-current multi-cell operating view and discretionary cross-unit commitment/resource intervention loop is installed.

## S3* — Complementary audit

- State: —
- Function: No sufficiently independent complementary audit of production claims with returned corrective control.
- Disturbance / variety regulated: False coding completion claims or incorrect edits could require evidence outside the ordinary model/tool report.
- Decisive decision or feedback right: Independently sample actual code/task reality, decide a challenge finding and cause control response; no built-in audit-specific right is supplied.
- Decision owner: None established; model-selected `explore` children provide generic task evidence, user may inspect results.
- Supporting / enforcement mechanisms: Read-only subagent, ordinary tests, session/event history, diagnostics and CLI view.
- Closure path: Child search/report returns to the same S1 model; not a separate audit judgment whose finding drives accountable correction.
- Why this is / is not agent-owned: An independent context or routine command/test does not by itself make a complementary S3* control channel.
- Evidence: [subagent.rs#L1-L96](https://github.com/Locotir/nexo/blob/a9643683250aeff6050d0b77adfed0fe9392e53c/nexo/crates/nexo-agent/src/subagent.rs#L1-L96), [turn.rs#L600-L620](https://github.com/Locotir/nexo/blob/a9643683250aeff6050d0b77adfed0fe9392e53c/nexo/crates/nexo-agent/src/turn.rs#L600-L620).
- Basis: structural
- Confidence: medium.
- Caveats: A human could compose a separate reviewer workflow, but generic capability is not a shipped S3* path.

### Absence scope

- Surfaces inspected: Task subagents, tool loop, ordinary tests/diagnostics, session history and release documentation.
- Plausible first-party paths checked: Read-only explore as reviewer, built-in test running, report aggregation, independent user inspection.
- Why no material first-party path remains: No first-party audit trigger, independent adjudicator/claim comparison and finding-to-current-control return is evidenced in the selected mode.

## S4 — Outside-and-then intelligence

- State: —
- Function: No separate prospective environmental sensing and durable adaptation-option loop into future coding capability.
- Disturbance / variety regulated: Model context pressure, stale file reads and changed task information are regulated as present coding context.
- Decisive decision or feedback right: Assess external/future changes and select a persistent change to harness capability, then return that option into present operations; not found.
- Decision owner: Context selection is deterministic; agent makes current coding choices; model/provider configuration changes are user-owned.
- Supporting / enforcement mechanisms: Curator, reusable brief, goal continuation, model/provider configuration and session memory/recall.
- Closure path: Selected history/notes enter the next current request, not an enduring outside-and-then adaptation proposal and current-capability revision.
- Why this is / is not agent-owned: Context engineering and task planning do not establish prospective S4 capability governance.
- Evidence: [brief.rs#L1-L26](https://github.com/Locotir/nexo/blob/a9643683250aeff6050d0b77adfed0fe9392e53c/nexo/crates/nexo-agent/src/brief.rs#L1-L26), [turn.rs#L685-L737](https://github.com/Locotir/nexo/blob/a9643683250aeff6050d0b77adfed0fe9392e53c/nexo/crates/nexo-agent/src/turn.rs#L685-L737), [context.rs](https://github.com/Locotir/nexo/blob/a9643683250aeff6050d0b77adfed0fe9392e53c/nexo/crates/nexo-agent/src/context.rs).
- Basis: structural
- Confidence: medium-high.
- Caveats: A model may write future-facing plans as ordinary user-assigned work; they are not automatically harness-level S4.

### Absence scope

- Surfaces inspected: Context policy/curator, recall, persistent session, goal command and provider configuration.
- Plausible first-party paths checked: Cross-session memory, generated plan, stale-read pruning, model discovery and user settings updates.
- Why no material first-party path remains: No sustained externally prospective evidence-to-adaptation-option decision with a returned update of current harness capability is wired.

## S5 — Policy and identity

- State: —
- Function: No first-party ultimate-policy dispute and authoritative identity-decision return loop at the selected coding session recursion.
- Disturbance / variety regulated: Unsafe tools, untrusted repository agent files and permission escalation during local coding.
- Decisive decision or feedback right: Decide an identity/ultimate-policy matter and return a binding revised policy to future operation; not supplied as a function-specific first-party path.
- Decision owner: User/developer sets policy and explicitly approves individual actions; runtime enforces it without deciding the harness's identity.
- Supporting / enforcement mechanisms: Plan mode, trusted project filters, tool permission gate, prompt directives and persisted allow rules.
- Closure path: User authorizes/refuses an individual tool and next tool action follows that result; no distinct identity-policy appeal → legitimate parent judgment → new binding organizational policy.
- Why this is / is not agent-owned: Permission policy and normal task approvals are not S5 governance by their existence.
- Evidence: [permission.rs#L1-L86](https://github.com/Locotir/nexo/blob/a9643683250aeff6050d0b77adfed0fe9392e53c/nexo/crates/nexo-agent/src/permission.rs#L1-L86), [turn.rs#L165-L190](https://github.com/Locotir/nexo/blob/a9643683250aeff6050d0b77adfed0fe9392e53c/nexo/crates/nexo-agent/src/turn.rs#L165-L190), [subagent.rs#L75-L118](https://github.com/Locotir/nexo/blob/a9643683250aeff6050d0b77adfed0fe9392e53c/nexo/crates/nexo-agent/src/subagent.rs#L75-L118).
- Basis: structural
- Confidence: medium-high.
- Caveats: Maintainer governance of the Rust product is a different recursion; it cannot be imported as runtime S5.

### Absence scope

- Surfaces inspected: Permission modes, plan mode/ask-user, agent profile trust, runtime directives, CLI configuration, project maintenance.
- Plausible first-party paths checked: Tool approval, persisted allow rules, trusted project admission and user-configured rules.
- Why no material first-party path remains: They enforce or amend ordinary tool constraints without an identity/ultimate-policy issue, legitimate parent ruling and returned governance of subsequent operation.

## Distributed OSS parent arrangement

The open-source project maintainers and users may choose different model/permission settings. This is not evidence of an organization-level first-party S3/S4/S5 parent control arrangement for an installed coding session.

## Self-hosted and non-human modes

Local and hosted model providers share the agent/tool loop and permission model. Headless mode changes how approvals are supplied, not whether a separate higher-function parent decision path exists.

## Recursion

The coding session is the S1 operating boundary. Optional child loops have tools, rounds and local tasks but are not shown to have their own durable viable metasystem or legitimate identity.

## Variety and escalation

Tool/model choice amplifies coding options; the permission gate, prompt/context selection and budgets attenuate unsafe or unaffordable action variety. A denial/error returns as local S1 feedback. Goal continuation stops after bounded rounds; no automatic algedonic status or S3/S5 authority is inferred from an error/notice.

## Evidence gaps

- No paid-provider, full-repository live coding evaluation or external effectiveness claim was independently reproduced; source and local tests establish supported architecture.
- Optional project-defined custom subagents can add behaviors outside the standard built-ins, but no such deployment-specific S2/S3*/S4/S5 construction was credited without a shipped function path.

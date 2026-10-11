---
harness_id: atlas-agent
project_name: Atlas Agent
repository: https://github.com/Omerfaruk-aydn/Atlas-Agent
review_ref: 3d0d63e20d9d2221be9a6e6ab4fc0350df5237f5
reviewed_at: 2026-10-11
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Atlas Agent

## Review boundary

- System in focus: packaged Go CLI/service autonomous coding runtime built around a first-party Coordinator/SessionAgent, model/provider/tool resolution, optional model-driven child task agents, optional second-opinion Advisor and deterministic execution limits.
- Purpose and identity: complete user software-engineering tasks on a local workspace through model/tool turns and optionally parallel child exploration, with user control and separate diagnostics of completed work.
- Relevant environment: user tasks; repository, file and shell tools; provider rate limits; available models; human permissions and approvals.
- Standard-distribution boundary: shipped Atlas CLI and model/tools integration in `internal/agent`, `internal/config` and ordinary tool implementations. Optional `advisor`, `orchestrate`, `delegate`, `debate`, and concurrency-capped child modes are included only when constructed by supported first-party config.
- Credited operating / distribution surfaces: [internal/agent/coordinator.go](https://github.com/Omerfaruk-aydn/Atlas-Agent/blob/3d0d63e20d9d2221be9a6e6ab4fc0350df5237f5/internal/agent/coordinator.go), [internal/agent/agent.go](https://github.com/Omerfaruk-aydn/Atlas-Agent/blob/3d0d63e20d9d2221be9a6e6ab4fc0350df5237f5/internal/agent/agent.go), [internal/agent/agent_tool.go](https://github.com/Omerfaruk-aydn/Atlas-Agent/blob/3d0d63e20d9d2221be9a6e6ab4fc0350df5237f5/internal/agent/agent_tool.go), [internal/agent/delegate_tool.go](https://github.com/Omerfaruk-aydn/Atlas-Agent/blob/3d0d63e20d9d2221be9a6e6ab4fc0350df5237f5/internal/agent/delegate_tool.go), [internal/agent/orchestrate_tool.go](https://github.com/Omerfaruk-aydn/Atlas-Agent/blob/3d0d63e20d9d2221be9a6e6ab4fc0350df5237f5/internal/agent/orchestrate_tool.go), [internal/agent/advisor.go](https://github.com/Omerfaruk-aydn/Atlas-Agent/blob/3d0d63e20d9d2221be9a6e6ab4fc0350df5237f5/internal/agent/advisor.go), [internal/agent/subagent_limit.go](https://github.com/Omerfaruk-aydn/Atlas-Agent/blob/3d0d63e20d9d2221be9a6e6ab4fc0350df5237f5/internal/agent/subagent_limit.go).
- Adjacent first-party surfaces excluded from ownership: developer tests and `.github/workflows` CI, future features in docs/config/FUTURE.md, third-party model/provider internal code, and unrelated user-defined organizational workflows/approvers beyond shipped code.
- First-party operating / deployment modes considered: CLI task session, named child agents/fanout with configured rate-limit slots, optional Advisor/elevated read-only second opinion, optional autonomous goal continuation; no borrowed external coding-agent CLI actors.
- Recursion level: one user-owned Atlas coding-agent session with model-driven bounded child operating units; independently complete enterprise hierarchy is not inferred.
- Reviewed revision: `3d0d63e20d9d2221be9a6e6ab4fc0350df5237f5`.
- Observation date: 2026-10-11.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

`Coordinator.Run` selects configured models/tools and builds a `SessionAgent` whose model loop makes coding/tool decisions. The optional agent/delegate/orchestrate/debate tools spawn separate child agents with their own prompts and model sessions, returning results to the root. Multiple children sharing one limited model API can trip concurrent provider rate limiting; the first-party `concurrencyLimiter` can cap simultaneous child sessions when configured, yielding a specific S2 constructor response to their shared provider disturbance. [internal/agent/coordinator.go](https://github.com/Omerfaruk-aydn/Atlas-Agent/blob/3d0d63e20d9d2221be9a6e6ab4fc0350df5237f5/internal/agent/coordinator.go#L267-L409), [internal/agent/orchestrate_tool.go](https://github.com/Omerfaruk-aydn/Atlas-Agent/blob/3d0d63e20d9d2221be9a6e6ab4fc0350df5237f5/internal/agent/orchestrate_tool.go#L55-L146), [internal/agent/subagent_limit.go](https://github.com/Omerfaruk-aydn/Atlas-Agent/blob/3d0d63e20d9d2221be9a6e6ab4fc0350df5237f5/internal/agent/subagent_limit.go#L5-L46).

Optional `advisor` is a separate model-driven post-turn reviewer, equipped with limited read-only tools to inspect raw code. Findings can be queued into the root agent's next prompt or notified to the user. When configured, escalation asks a second reviewer with the same read-only evidence access to deepen the diagnosis. The optional goal judge separately challenges an agent's own completion claim from the goal and session transcript, but lacks a raw-code direct inspection channel and cannot be borrowed as stronger audit evidence. [internal/agent/advisor.go](https://github.com/Omerfaruk-aydn/Atlas-Agent/blob/3d0d63e20d9d2221be9a6e6ab4fc0350df5237f5/internal/agent/advisor.go#L29-L245), [internal/agent/coordinator.go](https://github.com/Omerfaruk-aydn/Atlas-Agent/blob/3d0d63e20d9d2221be9a6e6ab4fc0350df5237f5/internal/agent/coordinator.go#L1330-L1432), [internal/agent/goal.go](https://github.com/Omerfaruk-aydn/Atlas-Agent/blob/3d0d63e20d9d2221be9a6e6ab4fc0350df5237f5/internal/agent/goal.go#L267-L324).

## Operational model

The main agent accepts a task, selects tools, receives feedback, and may distribute bounded work across child model agents. The constructor S2 slot gate allows current child work without a burst of colliding provider requests. At the end of a turn an optional adviser can inspect the outcome separately and return concerns into later work. No separate organizational S3 whole-current manager, future-facing S4 option generator, or S5 identity authority is established at the assessed session boundary.

## S1 — Operations

- State: A
- Function: Model-directed coding operations in the first-party Go session runtime; includes shell/filesystem/source tools, provider/tool feedback and independently model-driven bounded subagent instances.
- Disturbance / variety regulated: Changing user instructions, source/code errors, build/environment changes, provider responses and tool results.
- Decisive decision or feedback right: Main SessionAgent model selects work and tools after observing files, commands and previous responses; bounded subagent model chooses its own scoped actions.
- Decision owner: First-party sessionAgent model loop, or generated model-driven child on delegated work.
- Supporting / enforcement mechanisms: Coordinator model/provider builder, registered toolset, session persistence, cancel and message queue, prompt hooks, budgets and permission gates.
- Closure path: User goal → model Stream/tool selection → tool execution/result → next model step or reply, with persistent messages and bounded recovery.
- Boundary reachability: Shipped Atlas executable uses Coordinator.Run with buildAgent; it constructs SessionAgent and first-party worktree tools. The user need not bring an external coding-agent CLI as the actor.
- Why this is / is not agent-owned: Without first-party model-selected actions the fixed tool registry and turn controls do not decide which code fix satisfies the user.
- Evidence: [internal/agent/coordinator.go](https://github.com/Omerfaruk-aydn/Atlas-Agent/blob/3d0d63e20d9d2221be9a6e6ab4fc0350df5237f5/internal/agent/coordinator.go#L267-L403), [internal/agent/coordinator.go](https://github.com/Omerfaruk-aydn/Atlas-Agent/blob/3d0d63e20d9d2221be9a6e6ab4fc0350df5237f5/internal/agent/coordinator.go#L697-L807), [internal/agent/agent.go](https://github.com/Omerfaruk-aydn/Atlas-Agent/blob/3d0d63e20d9d2221be9a6e6ab4fc0350df5237f5/internal/agent/agent.go#L777-L1029), [internal/agent/agent.go](https://github.com/Omerfaruk-aydn/Atlas-Agent/blob/3d0d63e20d9d2221be9a6e6ab4fc0350df5237f5/internal/agent/agent.go#L1030-L1505)
- Basis: structural
- Confidence: high
- Caveats: No empirical success rate or model reliability is inferred.

## S2 — Coordination

- State: C
- Function: Prevent provider-wide rate-limit interference among parallel model-driven child S1 sessions launched by one task organization.
- Distinct S1 units: Multiple independently executing SessionAgent children with individually selected named task prompts created by the agent/delegate/orchestrate/debate tool paths.
- Inter-S1 disturbance: Simultaneous provider calls from a large fan-out cause shared service throttling (`429` bursts), degrading each child's progress; source explicitly calls out this concrete failure mode.
- Attenuating coordination relation: Configured MaxConcurrentSubAgents creates a channel-semaphore admission gate shared across child runs within the respective delegation tool; waiting children pause instead of starting simultaneous provider use.
- Feedback into subsequent S1 behaviour: A child acquires a slot or cancels while queued; after a previous child releases its slot, admitted child performs its model/tool loop; results are returned to the caller to inform subsequent task decisions.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: This is not merely selecting an agent or forwarding messages: concurrent independently model-driven S1 work would hit a concrete shared-provider overload disturbance; the constructor dynamically gates and releases admission before subsequent child execution.
- Disturbance / variety regulated: Inter-child request concurrency and provider 429 overload within a configured rate-limited environment.
- Decisive decision or feedback right: Admit/wait/cancel child execution based on a concurrency slot, then release the slot after completion; the upper model selects subtask goals but does not adjudicate slot policy.
- Decision owner: Deterministic first-party concurrencyLimiter constructor (`C`) rather than an autonomous S2 decision model.
- Supporting / enforcement mechanisms: Go channel semaphore, tool-level limiter, cancellation token, WaitGroup/join and result multiplexing.
- Closure path: Concurrent child requests → slot classification/admission or wait → provider calls serialized to capacity → release on finish → queued child proceeds, returns result to parent.
- Boundary reachability: `agent`, `orchestrate`, `delegate`, and `debate` tool builders register limiter when `max_concurrent_subagents` is set above zero; this is packaged Atlas code, not an external team orchestrator.
- Why this is / is not agent-owned: Agent decides decomposition, but deterministic runtime alone enforces the response to rate-limit contention.
- Evidence: [internal/agent/subagent_limit.go](https://github.com/Omerfaruk-aydn/Atlas-Agent/blob/3d0d63e20d9d2221be9a6e6ab4fc0350df5237f5/internal/agent/subagent_limit.go#L5-L46), [internal/agent/orchestrate_tool.go](https://github.com/Omerfaruk-aydn/Atlas-Agent/blob/3d0d63e20d9d2221be9a6e6ab4fc0350df5237f5/internal/agent/orchestrate_tool.go#L55-L146), [internal/agent/orchestrate_tool.go](https://github.com/Omerfaruk-aydn/Atlas-Agent/blob/3d0d63e20d9d2221be9a6e6ab4fc0350df5237f5/internal/agent/orchestrate_tool.go#L151-L185), [internal/agent/delegate_tool.go](https://github.com/Omerfaruk-aydn/Atlas-Agent/blob/3d0d63e20d9d2221be9a6e6ab4fc0350df5237f5/internal/agent/delegate_tool.go#L55-L129), [internal/agent/agent_tool.go](https://github.com/Omerfaruk-aydn/Atlas-Agent/blob/3d0d63e20d9d2221be9a6e6ab4fc0350df5237f5/internal/agent/agent_tool.go#L94-L149), [internal/config/config.go](https://github.com/Omerfaruk-aydn/Atlas-Agent/blob/3d0d63e20d9d2221be9a6e6ab4fc0350df5237f5/internal/config/config.go#L583-L589)
- Basis: explicit / structural
- Confidence: high for constructor, medium for measured effect
- Caveats: An unconfigured (zero) cap is unlimited; positive C is explicitly bounded to deployments setting a finite cap. It does not prevent semantic write conflicts between children.

## S3 — Inside-and-now control

- State: —
- Function: No separately owned organization-wide discretionary supervisor responsible for continuously reallocating priorities/resources across operational S1 teams.
- Disturbance / variety regulated: Session cost, tool permissions, user goals, concurrent prompts, retries and current task health.
- Decisive decision or feedback right: The S1 root can plan its work and delegate; Goal mode may automatically start the next turn, while fixed budget and session policy enforce caps; neither supplies a distinct whole-current S3 owner.
- Decision owner: Current coding agent for task choices and Go runtime/operator for task caps, no independent supervisory S3 decision right.
- Supporting / enforcement mechanisms: goalRun budget/verification, per-session dispatch mutex, cost guards, orchestration tool, per-subagent S2 semaphore, advisor diagnostic.
- Closure path: Current goal turns and local enforcement update the same task stream; no distinct whole-current negotiated resource commitment or cross-unit managerial intervention is returned.
- Why this is / is not agent-owned: Goal continuation and current task planning are within S1; provider concurrency protection is S2, while independent turn review is S3*, not by aggregation S3.
- Evidence: [internal/agent/goal.go](https://github.com/Omerfaruk-aydn/Atlas-Agent/blob/3d0d63e20d9d2221be9a6e6ab4fc0350df5237f5/internal/agent/goal.go#L1-L275), [internal/agent/coordinator.go](https://github.com/Omerfaruk-aydn/Atlas-Agent/blob/3d0d63e20d9d2221be9a6e6ab4fc0350df5237f5/internal/agent/coordinator.go#L267-L409), [internal/agent/agent.go](https://github.com/Omerfaruk-aydn/Atlas-Agent/blob/3d0d63e20d9d2221be9a6e6ab4fc0350df5237f5/internal/agent/agent.go#L777-L865), [internal/agent/orchestrate_tool.go](https://github.com/Omerfaruk-aydn/Atlas-Agent/blob/3d0d63e20d9d2221be9a6e6ab4fc0350df5237f5/internal/agent/orchestrate_tool.go#L55-L146)
- Basis: structural
- Confidence: medium-high
- Caveats: Broader deployments coordinating multiple Atlas servers could have an external S3 parent beyond this packaged session boundary.

### Absence scope

- Surfaces inspected: Coordinator, goal mode, task/subagent dispatch, session controls, cost limit, message queue, read-only advisor/escalation.
- Plausible first-party paths checked: Goal auto-continuation, current work planning, root fan-out, concurrency mutex/cap, permission intervention and advisor feedback.
- Why no material first-party path remains: No distinct owner with shared current organization view can make and close supervisory inter-unit resource/priority commitments.

## S3* — Complementary audit

- State: A
- Function: Model-owned separate read-only second opinion on a completed producing agent turn with concrete code inspection and corrective advice to next turn.
- Claim being audited: Producer's final coding response satisfies user request and any source-code outcome it asserts is substantiated.
- Ordinary reporting path: Main coding agent's user-facing final answer and its ordinary tool results; this path may be mistaken or overly confident.
- Complementary access path: Optional configured `advisor` role builds a separate model invocation with only `glob`, `grep`, `ls`, `view` read-only tools; it can inspect actual working tree instead of relying solely on the producer summary.
- Independence boundary: Advisor is a distinct model-driven checking pass, and optional escalate role can independently inspect code for flagged concerns. It shares the same first-party runtime and configured provider ecosystem, so not an externally or organizationally independent reviewer.
- Who acts on findings: Advisor injects `NIT`/`CONCERN`/`BLOCKER` note through `advisorNotes` into the next main prompt; concern/blocker can also notify the user. The next producing Agent decides corrective action, not a hard mandatory merge gate.
- Disturbance / variety regulated: False completion claims and unintended code changes missed by the production turn.
- Decisive decision or feedback right: Second model chooses whether, which files, and how to inspect; judges severity and writes concrete issue for the next coding turn.
- Decision owner: First-party model-driven Advisor, so `A` where advisor is enabled and role resolved; escalation may use another model without changing main owner.
- Supporting / enforcement mechanisms: Role-specific read-only tool list, result truncation, cadence EveryNTurns, timeout, severity parser, session note queue and optional user notification.
- Closure path: Completed turn → advisor raw-source inspection/judgment → stored concern → `injectAdvisorNote` into next root turn → subsequent corrective work or user-visible warning. The pass is advisory/fail-open, so no forced correction guarantee.
- Boundary reachability: `coordinator.buildAgent` constructs advisor only in ordinary non-subagent session when `options.advisor.enabled` and a model role are configured. `sessionAgent.Run` launches it asynchronously after turn; next Run injects note.
- Why this is / is not agent-owned: The audit judgment and decision to invoke raw code tools depend on the advisor model, unlike a static test or heuristic. The runtime only schedules and transports its finding.
- Evidence: [internal/agent/coordinator.go](https://github.com/Omerfaruk-aydn/Atlas-Agent/blob/3d0d63e20d9d2221be9a6e6ab4fc0350df5237f5/internal/agent/coordinator.go#L1320-L1364), [internal/agent/coordinator.go](https://github.com/Omerfaruk-aydn/Atlas-Agent/blob/3d0d63e20d9d2221be9a6e6ab4fc0350df5237f5/internal/agent/coordinator.go#L697-L728), [internal/agent/advisor.go](https://github.com/Omerfaruk-aydn/Atlas-Agent/blob/3d0d63e20d9d2221be9a6e6ab4fc0350df5237f5/internal/agent/advisor.go#L29-L170), [internal/agent/agent.go](https://github.com/Omerfaruk-aydn/Atlas-Agent/blob/3d0d63e20d9d2221be9a6e6ab4fc0350df5237f5/internal/agent/agent.go#L779-L799), [internal/agent/agent.go](https://github.com/Omerfaruk-aydn/Atlas-Agent/blob/3d0d63e20d9d2221be9a6e6ab4fc0350df5237f5/internal/agent/agent.go#L1471-L1490)
- Basis: explicit / structural
- Confidence: high for reachable conditional path; medium for actual audit efficacy
- Caveats: Optional mode may be disabled by default, timed-out, skipped by cadence, or conclude NONE. Advisor report is not mandatory correction enforcement, and the goal judge's transcript-only confirmation is not treated as independent raw-source auditing.

## S4 — Outside-and-then intelligence

- State: —
- Function: No bounded source proof of a future-external environment sensing, strategic option selection and accepted change to organization-wide future capability.
- Disturbance / variety regulated: Provider failures, historical prompts, memory and current goal continuation.
- Decisive decision or feedback right: Goal mode pursues a current user objective; model fallback and memory change execution continuity, not a prospective autonomous future operating policy.
- Decision owner: User/configuration and ordinary task agent for model choices, no first-party prospective adaptation body.
- Supporting / enforcement mechanisms: Memory/factstore, context summary, fallback models, goal progress, templates and docs for future features.
- Closure path: Existing context and provider choices may be applied inside current tasks, but no externally sourced prospective capability option is adopted into governance/operation.
- Why this is / is not agent-owned: Persistence, task resume, failover and alternate models do not imply an S4 intelligence loop.
- Evidence: [internal/agent/goal.go](https://github.com/Omerfaruk-aydn/Atlas-Agent/blob/3d0d63e20d9d2221be9a6e6ab4fc0350df5237f5/internal/agent/goal.go#L1-L180), [internal/agent/memorystore.go](https://github.com/Omerfaruk-aydn/Atlas-Agent/blob/3d0d63e20d9d2221be9a6e6ab4fc0350df5237f5/internal/agent/memorystore.go), [internal/agent/model_fallback.go](https://github.com/Omerfaruk-aydn/Atlas-Agent/blob/3d0d63e20d9d2221be9a6e6ab4fc0350df5237f5/internal/agent/model_fallback.go), [internal/agent/coordinator.go](https://github.com/Omerfaruk-aydn/Atlas-Agent/blob/3d0d63e20d9d2221be9a6e6ab4fc0350df5237f5/internal/agent/coordinator.go#L1236-L1335)
- Basis: structural
- Confidence: medium
- Caveats: The package is feature-rich; review is scoped to evidenced supported adaptive operating paths.

### Absence scope

- Surfaces inspected: Goal/autonomous run, memory, role models, fallback, prompts, tools, sessions, and published future configuration docs.
- Plausible first-party paths checked: User-goal auto-loop, advisor next-turn note, provider failover, persistent memories and long-term strategic config.
- Why no material first-party path remains: These alter the current coding task or retain its context; none independently generates and returns a prospective organizational capability option from future-facing external signals.

## S5 — Policy and identity

- State: —
- Function: No autonomous or first-party parent-governed ultimate-policy/identity issue-deliberation with legitimate authoritative return at this agent recursion.
- Disturbance / variety regulated: Unsafe shell use, cost overrun, tool permissions and user preferences.
- Decisive decision or feedback right: Developer/operator configures permissions/model roles; runtime gates apply them locally; user approves or rejects current actions.
- Decision owner: External user and fixed local policy enforcement, not an S5 governance organ with issue and binding policy decision.
- Supporting / enforcement mechanisms: Permission approvals, budget/session caps, tool access profiles, prompt templates, CLI configuration.
- Closure path: Individual tools are authorized or denied; there is no identity-level dispute → legitimate authority → binding revised policy return.
- Why this is / is not agent-owned: Configured safe execution is not self-governing identity-policy choice.
- Evidence: [internal/agent/coordinator.go](https://github.com/Omerfaruk-aydn/Atlas-Agent/blob/3d0d63e20d9d2221be9a6e6ab4fc0350df5237f5/internal/agent/coordinator.go#L804-L1126), [internal/agent/agent.go](https://github.com/Omerfaruk-aydn/Atlas-Agent/blob/3d0d63e20d9d2221be9a6e6ab4fc0350df5237f5/internal/agent/agent.go#L779-L811), [internal/config/config.go](https://github.com/Omerfaruk-aydn/Atlas-Agent/blob/3d0d63e20d9d2221be9a6e6ab4fc0350df5237f5/internal/config/config.go)
- Basis: structural
- Confidence: medium-high
- Caveats: Maintainer organization and user-agent contract outside this recursion are not credited.

### Absence scope

- Surfaces inspected: Permissions/config, model role registry, goal mode, tool scopes, subagents and memory/config rules.
- Plausible first-party paths checked: Human approvals, goal authority, role hot-reload, policy changes and session-level limits.
- Why no material first-party path remains: No legitimate identity-level decision-maker and consequential ultimate-policy issue return are present in this shipped session.

## Recursion

Named children are separate running model decision loops but remain bounded by the parent request, configured model and tool scopes; the parent receives their results. Each child is not assumed to reproduce independent S3/S4/S5 and policy identity. [internal/agent/orchestrate_tool.go](https://github.com/Omerfaruk-aydn/Atlas-Agent/blob/3d0d63e20d9d2221be9a6e6ab4fc0350df5237f5/internal/agent/orchestrate_tool.go); [internal/agent/agent_tool.go](https://github.com/Omerfaruk-aydn/Atlas-Agent/blob/3d0d63e20d9d2221be9a6e6ab4fc0350df5237f5/internal/agent/agent_tool.go).

## Variety and escalation

Configured S2 rate-limit slots prevent provider-concurrency shocks before starting child work; optional read-only advisor can flag source-check concerns and, at configured severities, escalate and notify, then return notes for the next producer turn. Ordinary session cancellation, fallback, goal continuation and cost guards are separate support mechanisms.

## Evidence gaps

- Positive S2 requires a finite `max_concurrent_subagents` setting; zero/unconfigured is explicitly unlimited.
- Positive S3* requires `advisor.enabled` and a resolvable `advisor` model role. The separate model is independent of the producing turn and has direct read-only source access, but does not ensure a mandatory fix/rerun and can fail open; no Organization S3* reviewer independence is claimed.
- Static source supports capability-mode classification, not observed effectiveness at avoiding provider 429s, catching wrong answers, or improving code quality.

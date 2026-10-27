---
harness_id: ylva
project_name: Ylva
repository: https://github.com/manuel-koch/ylva
review_ref: f1275d3dbb4e055798b53033f483e59d34c978d8
reviewed_at: 2026-10-27
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Ylva

## Review boundary

- System in focus: the shipped Ylva Rust CLI/TUI and its configured root/subagent runtime.
- Purpose and identity: execute model-directed terminal/file/web work with persisted conversations and bounded delegation.
- Relevant environment: user workspaces, provider connections, tools, human approvals and concurrent delegated tasks.
- Standard-distribution boundary: source-installed product runtime and first-party provider/tool/configuration paths; macOS is supported, Linux unverified and Windows unsupported.
- Credited operating / distribution surfaces: src/agent.rs and src/agent/runtime/*; src/agent_factory.rs; src/agent/tools/*; src/http.rs; installed profile, sandbox and persistence modules.
- Adjacent first-party surfaces excluded from ownership: mock providers and tests, maintainer development workflows, CI/release configuration and generic instructions addressed to outside contributor agents.
- First-party operating / deployment modes considered: interactive TUI and headless CLI, configured root and one-level subagents, local/hosted providers and supervised or configured automatic tool approval.
- Recursion level: one user session and its delegated operational agent runs.
- Reviewed revision: f1275d3dbb4e055798b53033f483e59d34c978d8.
- Observation date: 2026-10-27.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

AgentFactory assembles engine, persona, skill catalog, tool registry, sandbox and persisted store into an AgentLoop. The non-blocking loop streams model output, admits tool calls, waits for approval policy, executes tools and returns structured results. A root may spawn configured subagent types; a FIFO/concurrency manager and completion notices provide lifecycle support. Separate root/subagent contexts persist JSONL histories; compaction limits the model view. Provider connections share concurrency and Retry-After cooldown state. Configuration trust hashes protect workspace settings, while SOUL and agent persona text supply instructions. No development evaluator is credited as runtime audit.

## Operational model

Root and child model loops own local action/delegation/result choices; tools, cancellation, budgets and approvals constrain those choices. The special provider retry path attenuates a concrete cross-agent contention problem. Its timing policy is fixed runtime/developer logic, so the coordination-specific path is constructor-level rather than agent-owned A. Root delegation/aggregation alone is not whole-system S3.

## S1 — Operations

- State: A
- Function: perform user-directed file, shell, search and web work through model-selected actions.
- Disturbance / variety regulated: changing task content, tool errors, context pressure and asynchronously completed work.
- Decisive decision or feedback right: select tools, arguments, delegation and continuation from returned observations.
- Decision owner: root or child model-backed agent at its local operational boundary.
- Supporting / enforcement mechanisms: AgentFactory, tool schemas, approval sandbox, iteration/context bounds, store and subagent scheduler.
- Closure path: AgentEvent tool results enter Context and restart model requests; child agent_finish outcomes enter root notices and subsequent synthesis.
- Boundary reachability: normal CLI/TUI construction invokes AgentFactory and AgentLoop; registered product tools are available to configured model engines without custom agent-loop code.
- Why this is / is not agent-owned: removing the model leaves execution gates but no discretionary next-action choice.
- Evidence: [loop/roles](https://github.com/manuel-koch/ylva/blob/f1275d3dbb4e055798b53033f483e59d34c978d8/src/agent.rs#L150-L202); [factory](https://github.com/manuel-koch/ylva/blob/f1275d3dbb4e055798b53033f483e59d34c978d8/src/agent_factory.rs#L34-L65); [tool event return](https://github.com/manuel-koch/ylva/blob/f1275d3dbb4e055798b53033f483e59d34c978d8/src/agent/runtime/events.rs#L210-L275); [child completion](https://github.com/manuel-koch/ylva/blob/f1275d3dbb4e055798b53033f483e59d34c978d8/src/agent/runtime/subagents.rs#L18-L152).
- Basis: structural.
- Confidence: high.
- Caveats: Source-relative finding; no empirical model-quality claim.

## S2 — Coordination

- State: C
- Function: attenuate provider-rate contention and synchronized retry oscillation among concurrent operational loops.
- Disturbance / variety regulated: root/subagent requests sharing one provider trigger 429/503 Retry-After and can retry in lockstep.
- Decisive decision or feedback right: select the shared not-before delay, concurrency allowance and desynchronizing retry response.
- Decision owner: fixed first-party runtime/developer policy; an autonomous coordination-policy owner would require composition.
- Supporting / enforcement mechanisms: shared RetryCooldown deadline, semaphore, cancellation-aware waits, bounded Retry-After retries and jitter.
- Closure path: a rate-limited request extends the shared gate; other requests from the same provider connection wait before their next attempts, and jitter disperses subsequent retries.
- Boundary reachability: provider HTTP paths intentionally share RequestConcurrencyLimiter and its cooldown across the product's concurrent calls. This is a specific anti-contention path, not generic graph expressiveness.
- Distinct S1 units: root and concurrently running subagent loops using the same configured provider connection.
- Inter-S1 disturbance: competition for that provider's rate allowance with coupled retry storms.
- Attenuating coordination relation: shared cooldown plus request concurrency cap and retry jitter.
- Feedback into subsequent S1 behaviour: provider Retry-After changes when all affected operational loops may next request model work.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the shipped implementation explicitly identifies parallel requests retrying in lockstep and shares a corrective deadline; FIFO child scheduling alone is not the witness.
- Why this is / is not agent-owned: no model chooses or revises this coordination policy; A is not established.
- Evidence: [shared gate](https://github.com/manuel-koch/ylva/blob/f1275d3dbb4e055798b53033f483e59d34c978d8/src/http.rs#L58-L110); [limiter](https://github.com/manuel-koch/ylva/blob/f1275d3dbb4e055798b53033f483e59d34c978d8/src/http.rs#L148-L170); [retry enforcement](https://github.com/manuel-koch/ylva/blob/f1275d3dbb4e055798b53033f483e59d34c978d8/src/http.rs#L517-L635); [documented cross-agent retry](https://github.com/manuel-koch/ylva/blob/f1275d3dbb4e055798b53033f483e59d34c978d8/docs/features.md#L487-L503).
- Basis: structural.
- Confidence: medium.
- Caveats: Narrow provider-contention constructor only; not autonomous workspace/file-conflict coordination or S3.

## S3 — Inside-and-now control

- State: —
- Function: no first-party whole-session supervisory regulation beyond local delegation and fixed limits established.
- Disturbance / variety regulated: shared commitments, budgets and priority conflicts would require current-control judgment.
- Decisive decision or feedback right: no cross-unit resource/commitment intervention owner established.
- Decision owner: none established for S3; operator approves individual tools and configures limits.
- Supporting / enforcement mechanisms: FIFO spawn cap, per-type timeout/iteration limits, token/cost views, cancellation and root aggregation.
- Closure path: child completion returns task results, not a separately established supervisory bargain or revised whole-system commitment.
- Why this is / is not agent-owned: a root selecting tasks and receiving outcomes is insufficient to establish S3.
- Evidence: [scheduler-only boundary](https://github.com/manuel-koch/ylva/blob/f1275d3dbb4e055798b53033f483e59d34c978d8/src/agent/subagent_manager.rs#L15-L27); [spawn admission](https://github.com/manuel-koch/ylva/blob/f1275d3dbb4e055798b53033f483e59d34c978d8/src/agent/tool_queue/spawn.rs#L15-L140); [configured limits](https://github.com/manuel-koch/ylva/blob/f1275d3dbb4e055798b53033f483e59d34c978d8/src/config/agent.rs#L20-L89).
- Basis: structural.
- Confidence: high.
- Caveats: Source-relative finding; no empirical model-quality claim.

### Absence scope

- Surfaces inspected: root/subagent factory and scheduler, completion return, type limits, user approvals and TUI/CLI controls.
- Plausible first-party paths checked: root spawn/aggregate, configured concurrency/timeouts, steering and cancellation, cost display and operator intervention.
- Why no material first-party path remains: the paths regulate local task execution or enforce preselected parameters; no supplied whole-system resource/commitment decision loop or qualifying parent-control contract closes S3.

## S3* — Complementary audit

- State: —
- Function: no complementary independently controlled audit channel established.
- Disturbance / variety regulated: incorrect task claims or incomplete subagent results.
- Decisive decision or feedback right: no audit-specific independent judgment/returned corrective-control right supplied.
- Decision owner: none established.
- Supporting / enforcement mechanisms: transcripts, source lists, tools, mock-provider tests and subagent completion statuses.
- Closure path: routine root review/aggregation is the production path; tests remain adjacent.
- Why this is / is not agent-owned: the available child tool does not intentionally instantiate an independent audit role.
- Evidence: [subagent role/tool](https://github.com/manuel-koch/ylva/blob/f1275d3dbb4e055798b53033f483e59d34c978d8/src/agent/tools/spawn_subagent.rs#L15-L69); [completion metadata](https://github.com/manuel-koch/ylva/blob/f1275d3dbb4e055798b53033f483e59d34c978d8/src/agent/subagent_manager.rs#L52-L118); [ordinary completion handling](https://github.com/manuel-koch/ylva/blob/f1275d3dbb4e055798b53033f483e59d34c978d8/src/agent/runtime/subagents.rs#L18-L152).
- Basis: structural.
- Confidence: high.
- Caveats: Source-relative finding; no empirical model-quality claim.

### Absence scope

- Surfaces inspected: tool catalog, agent types/factory, child outcomes and persistence/evaluation documentation.
- Plausible first-party paths checked: delegating a review task, source-bearing agent_finish results, transcript inspection and tests.
- Why no material first-party path remains: generic task delegation/observability does not supply a separately controlled complementary audit with findings returned to supervisory control.

## S4 — Outside-and-then intelligence

- State: —
- Function: no external/prospective capability-adaptation loop established.
- Disturbance / variety regulated: future provider/tool/environment changes.
- Decisive decision or feedback right: no function-specific prospective adaptation option/adoption right supplied.
- Decision owner: none established.
- Supporting / enforcement mechanisms: web search/fetch, model picker/catalog, local skills and context compaction.
- Closure path: results and summaries affect the current task; user model selection affects requests without a supplied external-and-future adaptation process.
- Why this is / is not agent-owned: search and model discovery are capabilities, not S4 by themselves.
- Evidence: [tool capabilities and picker](https://github.com/manuel-koch/ylva/blob/f1275d3dbb4e055798b53033f483e59d34c978d8/docs/features.md#L427-L487); [skill selection](https://github.com/manuel-koch/ylva/blob/f1275d3dbb4e055798b53033f483e59d34c978d8/src/skills/policy.rs#L15-L85); [configured agent capability](https://github.com/manuel-koch/ylva/blob/f1275d3dbb4e055798b53033f483e59d34c978d8/src/config/agent.rs#L20-L89).
- Basis: structural.
- Confidence: high.
- Caveats: Source-relative finding; no empirical model-quality claim.

### Absence scope

- Surfaces inspected: web tools, model discovery/picker, skill catalogs, compaction and profile reload/configuration paths.
- Plausible first-party paths checked: external web sensing, choosing a model, loading skills and adapting context usage.
- Why no material first-party path remains: these support current operation or manual configuration; no packaged future option-development and return to present supervisory capability is wired.

## S5 — Policy and identity

- State: —
- Function: no legitimate ultimate-policy/identity issue and decisive-return process established.
- Disturbance / variety regulated: identity or ultimate risk-policy disputes are not a supplied runtime workstream.
- Decisive decision or feedback right: ordinary configuration/trust/tool-approval choices do not establish ultimate-policy settlement.
- Decision owner: none established for S5.
- Supporting / enforcement mechanisms: SOUL/persona loading, trusted instruction files, workspace content-hash trust and tool approval rules.
- Closure path: approved settings constrain subsequent operation, but no identity-level matter-to-authority-to-return path is supplied.
- Why this is / is not agent-owned: persona text and approval enforcement do not become an agentic or parent S5.
- Evidence: [persona resolution](https://github.com/manuel-koch/ylva/blob/f1275d3dbb4e055798b53033f483e59d34c978d8/src/config/soul.rs#L15-L48); [workspace trust scope](https://github.com/manuel-koch/ylva/blob/f1275d3dbb4e055798b53033f483e59d34c978d8/src/config/workspace_trust.rs#L15-L28); [configuration boundaries](https://github.com/manuel-koch/ylva/blob/f1275d3dbb4e055798b53033f483e59d34c978d8/src/config/agent.rs#L20-L89).
- Basis: structural.
- Confidence: high.
- Caveats: Source-relative finding; no empirical model-quality claim.

### Absence scope

- Surfaces inspected: SOUL/instructions, profile/type configuration, workspace trust, sandbox approval and human clarification.
- Plausible first-party paths checked: trust/retrust after edits, per-tool consent, operator steering and persona replacement.
- Why no material first-party path remains: all are configuration security or ordinary operational interaction; no shipped identity/ultimate-policy escalation and authoritative resolution loop is defined.

## Distributed OSS parent arrangement

Project contributors and release governance are adjacent to the installed harness. No organization-level parent ownership is inferred from contributor identities.

## Self-hosted and non-human modes

Supported macOS source installation and CLI/TUI modes are assessed structurally. Hosted/local providers and manual/automatic approval do not change the mapped decisive ownership. No parent modifier is established.

## Recursion

One-level child loops have local work and outcomes; delegation does not establish recursive viability or a child metasystem.

## Variety and escalation

Tool-result envelopes, bounded batches, context compaction and explicit skipped-call errors preserve corrective distinctions. Provider-wide cooldown/jitter attenuates request contention. Stop and clarify route ordinary operational exceptions.

## Evidence gaps

No live provider/agent-quality runs. Cargo is unavailable on the inspection host, and the project documents Linux as unverified; native Rust tests were not executed or reported PASS. The source-level findings do not claim measured performance. Current Skills main 0.3.8 was inspected; Index selects released 0.3.7, which is preserved rather than silently migrated.

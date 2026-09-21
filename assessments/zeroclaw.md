---
harness_id: zeroclaw
project_name: ZeroClaw
repository: https://github.com/zeroclaw-labs/zeroclaw
review_ref: 757db6c356c61861256a87222e30c7c92e8f166f
reviewed_at: 2026-09-21
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: A
autonomy_s5: —
---

# ZeroClaw

## Review boundary

- System in focus: one first-party ZeroClaw agent-runtime installation at pinned revision `757db6c356c61861256a87222e30c7c92e8f166f`, including the canonical agent loop, configured agents, first-party delegation/subagent runtime, background task control, SOP/runtime policy, persistent skills and the shipped skill-review path.
- Purpose and identity: operate a locally owned personal AI-agent runtime that accepts work through configured channels, executes model/tool turns, can delegate work to configured specialist agents, and can persist selected learned operating knowledge into its skill library.
- Relevant environment: user requests, channel inputs, model/provider responses, tool results and failures, external services, concurrent delegated work, installed skills and operator-configured risk/identity policy.
- Standard-distribution boundary: the shipped ZeroClaw Rust binary and first-party runtime/tool surfaces at the pinned revision. External model providers, MCP servers, user-authored skills, downstream custom agents, repository-development workflows and maintainers are outside organizational ownership.
- Credited operating / distribution surfaces: canonical agent loop and tool execution, configured-agent delegation, background delegate-result/task control, standard security/approval gates, SOP runtime, persistent skill library, and the first-party background skill-review fork.
- Adjacent first-party surfaces excluded from ownership: contribution/release automation, development-only tests/fixtures, repository governance, and security/development audits that do not execute as an independent runtime organizational actor.
- First-party operating / deployment modes considered: interactive/channel agent turns, configured delegation and background delegation, SOP execution, supervised/other shipped risk-policy modes, and opt-in first-party skill improvement.
- Recursion level: one ZeroClaw installation. Distinct configured delegated agents can form subordinate operational S1 units because `delegate` transfers work to a different configured identity/model/tool policy; same-identity `spawn_subagent` is supporting evidence but is not required for the S1-unit claim.
- Reviewed revision: `757db6c356c61861256a87222e30c7c92e8f166f`.
- Observation date: 2026-09-21.
- Generated Profile version: 0.2.3.
- Generated Methodology version: 0.3.5.
- Current Profile version: 0.2.3.
- Current Methodology version: 0.3.5.

## Repository architecture

ZeroClaw ships its own agent runtime rather than only wrapping an external harness. Its README describes one agent loop receiving configured channel inputs and acting through first-party tools under runtime security policy. The runtime crate contains the canonical model/tool loop, dispatcher, approval bridge, control-plane/task state, delegation, skills, SOP execution and observability surfaces.

Delegation is a substantive operational path. `spawn_subagent` runs a bounded child under the same identity, while `delegate` hands work to a different configured agent identity and policy. Delegation supports synchronous execution, parallel fan-out and background tasks; background lifecycle state is persisted in the control-plane database and the caller can inspect, wait for and cancel its delegated tasks.

No S2 state is credited merely from delegation, parallel tool execution, message routing or shared budgets. The reviewed first-party paths establish multiple operational units and current-control relations, but the assessment did not establish a distinct coordination relation that senses a concrete cross-S1 interference condition and attenuates that disturbance back into the participating units. Generic depth limits, policy ceilings and task sequencing are treated as runtime enforcement rather than S2 evidence.

A strong prospective-adaptation path exists in the runtime skill-review subsystem. After a sufficiently tool-active turn, `maybe_run_skill_review` launches a restricted background model fork with the completed conversation/history and explicit failure hints. The fork is given only `skills_list`, `skill_view` and mutating `skill_manage`; human approval is explicitly absent. Its shipped prompt instructs it to detect user corrections, workflow corrections, failed/outdated skills and reusable techniques, then patch, extend or archive the persistent skill library so later sessions start with the learned operating knowledge. `skill_manage` and `SkillImprover` persist those changes atomically with audit metadata.

Audit-named surfaces are not automatically S3*. For example, `SopAuditLogger` stores run starts, step results, suspicious/blocked events and run completion in memory/logs. That is evidence capture and enforcement telemetry, not an independent complementary auditor making a distinct operational-reality claim and closing corrective feedback into S1. The skill-review fork is classified by its prospective adaptation function as S4, not double-counted as S3*.

Human escalation is also not automatically S5. The shipped `escalate_to_human` tool can deliver an operational question to an operator and optionally wait for the reply, while supervised approvals and risk profiles gate current actions. The reviewed evidence did not establish a separate loop for resolving organization identity, ultimate policy or constitutional conflicts and returning an authoritative governing decision to the running organization.

Primary evidence:

- [`README.md`](https://github.com/zeroclaw-labs/zeroclaw/blob/757db6c356c61861256a87222e30c7c92e8f166f/README.md) — shipped agent runtime, canonical agent loop, tools, security policy, SOP and standard deployment modes.
- [`docs/book/src/agents/delegation.md`](https://github.com/zeroclaw-labs/zeroclaw/blob/757db6c356c61861256a87222e30c7c92e8f166f/docs/book/src/agents/delegation.md) — configured-agent delegation, identity/policy ownership, parallel/background execution and task result/cancellation surface.
- [`crates/zeroclaw-runtime/src/tools/delegate.rs`](https://github.com/zeroclaw-labs/zeroclaw/blob/757db6c356c61861256a87222e30c7c92e8f166f/crates/zeroclaw-runtime/src/tools/delegate.rs) — first-party delegate/background task implementation and caller-scoped result-management operations.
- [`crates/zeroclaw-runtime/src/skills/review.rs`](https://github.com/zeroclaw-labs/zeroclaw/blob/757db6c356c61861256a87222e30c7c92e8f166f/crates/zeroclaw-runtime/src/skills/review.rs) — post-turn skill-review fork, history/failure input, restricted mutation tools and explicit no-human-in-the-loop execution.
- [`crates/zeroclaw-runtime/src/skills/review_prompt.md`](https://github.com/zeroclaw-labs/zeroclaw/blob/757db6c356c61861256a87222e30c7c92e8f166f/crates/zeroclaw-runtime/src/skills/review_prompt.md) — operational signals to learn from and instructions to persist class-level skill changes for future sessions.
- [`crates/zeroclaw-runtime/src/skills/improver.rs`](https://github.com/zeroclaw-labs/zeroclaw/blob/757db6c356c61861256a87222e30c7c92e8f166f/crates/zeroclaw-runtime/src/skills/improver.rs) — durable skill mutation, cooldown/audit metadata and extraction of success/failure signals from tool history.
- [`crates/zeroclaw-runtime/src/tools/skill_manage.rs`](https://github.com/zeroclaw-labs/zeroclaw/blob/757db6c356c61861256a87222e30c7c92e8f166f/crates/zeroclaw-runtime/src/tools/skill_manage.rs) — mutation surface for patching, adding support files and archiving installed skills.
- [`crates/zeroclaw-runtime/src/sop/audit.rs`](https://github.com/zeroclaw-labs/zeroclaw/blob/757db6c356c61861256a87222e30c7c92e8f166f/crates/zeroclaw-runtime/src/sop/audit.rs) — audit logging/record retrieval rather than an independent runtime auditor.
- [`crates/zeroclaw-tools/src/escalate.rs`](https://github.com/zeroclaw-labs/zeroclaw/blob/757db6c356c61861256a87222e30c7c92e8f166f/crates/zeroclaw-tools/src/escalate.rs) — real operator escalation/response path used as operational governance evidence, not by itself as S5 closure.

## Operational model

Inbound channel or CLI work enters the ZeroClaw runtime's model/tool loop. The model chooses substantive next actions; first-party policy and approval mechanisms constrain execution, tools return observations, and the loop continues until completion.

For multi-agent work, the caller may delegate to a separately configured agent. That target owns its configured identity, model/provider and bounded tool policy. Background delegation persists lifecycle state and gives the caller control operations for its current delegated-work portfolio, including inspection, waiting and cancellation.

After sufficiently tool-active work, the optional first-party skill-review mechanism can fork a restricted model turn over the completed operational history. It evaluates durable lessons and can directly mutate the installed skill library without a human approval callback. Those changed skills are then available to shape future agent operation.

## S1 — Operations

- State: A
- Function: perform user- or event-directed work through a model-driven tool/observation loop and return operational outcomes.
- Disturbance / variety regulated: ambiguous requests, external/tool results, provider responses, failures, installed capabilities and changing task context.
- Decisive decision or feedback right: choose substantive next actions/tools and revise the plan from returned observations within configured authority.
- Decision owner: the running ZeroClaw model agent; delegated configured agents own their delegated operational work at their recursion level.
- Supporting / enforcement mechanisms: agent loop, tool registry/dispatcher, security policy, approval bridge, provider transport, memory/context handling and tool receipts.
- Closure path: inbound work → model decision → authorized tool/delegation action → returned observation/result → subsequent model decision → terminal response/outcome.
- Boundary reachability: the standard `zeroclaw agent -a <alias>`/channel runtime enters the first-party agent loop shipped in the ZeroClaw binary; no downstream harness is required.
- Why this is / is not agent-owned: deterministic runtime code transports and constrains actions, while the model loop chooses substantive operational actions from current evidence.
- Evidence: [`README.md`](https://github.com/zeroclaw-labs/zeroclaw/blob/757db6c356c61861256a87222e30c7c92e8f166f/README.md), [`crates/zeroclaw-runtime/src/agent/loop_.rs`](https://github.com/zeroclaw-labs/zeroclaw/blob/757db6c356c61861256a87222e30c7c92e8f166f/crates/zeroclaw-runtime/src/agent/loop_.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: external model inference is execution substrate, not an imported organizational owner.

## S2 — Coordination

- State: —
- Function: no material first-party path was established that attenuates a concrete cross-S1 interference condition among distinct operational units.
- Disturbance / variety regulated: not established as S2 at the reviewed system boundary.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: delegation policy, shared action/cost ceilings, depth limits, routing, task sequencing and parallel execution exist, but none is credited without a demonstrated S2-specific disturbance relation.
- Closure path: not applicable.
- Why this is / is not agent-owned: the repository supports communication and work distribution among agents, but delegation/parallelism alone does not prove coordination in the VSM sense.
- Evidence: [`docs/book/src/agents/delegation.md`](https://github.com/zeroclaw-labs/zeroclaw/blob/757db6c356c61861256a87222e30c7c92e8f166f/docs/book/src/agents/delegation.md), [`crates/zeroclaw-runtime/src/tools/delegate.rs`](https://github.com/zeroclaw-labs/zeroclaw/blob/757db6c356c61861256a87222e30c7c92e8f166f/crates/zeroclaw-runtime/src/tools/delegate.rs).
- Basis: structural absence review.
- Confidence: medium-high.
- Caveats: a future reassessment should revisit S2 if first-party evidence explicitly connects a coordination mechanism to shared-resource contention, oscillation or another cross-S1 disturbance.

### Absence scope

- Surfaces inspected: configured-agent delegation, same-identity subagents, parallel fan-out, background task lifecycle, shared policy/budget inheritance, SOP graph/routing and runtime task-control surfaces.
- Plausible paths considered: delegation as coordination, shared budgets as coordination, parallel-execution limits, message routing and SOP sequencing.
- Why no material path remains: reviewed evidence establishes task distribution, permission enforcement and sequencing, but not the required disturbance → attenuation relation between distinct S1 units.

## S3 — Inside-and-now control

- State: A
- Function: regulate the current portfolio of background work delegated by a configured caller agent.
- Disturbance / variety regulated: changing current workload, long-running delegated tasks, completed/failed work and tasks that are no longer needed.
- Decisive decision or feedback right: create background delegated commitments, inspect/list current caller-owned delegated tasks, wait for selected tasks and cancel current work.
- Decision owner: the model-driven caller agent using the built-in `delegate` control surface.
- Supporting / enforcement mechanisms: control-plane database, caller-scoped task/result registry, cancellation tokens, persisted result artifacts and delegation policy.
- Closure path: current delegated-task portfolio → model invokes list/check/await operations → model current-control decision → delegate/cancel/continue action → lifecycle state changes → updated portfolio available to the caller.
- Boundary reachability: `delegate` is a first-party built-in runtime tool for configured agents; background mode returns a `task_id`, and the same tool exposes `check_result`, `list_results`, `cancel_task` and `await_sessions` for caller-owned task rows.
- Why this is / is not agent-owned: persistence/cancellation mechanics are deterministic, while the model caller decides which current commitments to create, inspect, await or cancel.
- Evidence: [`docs/book/src/agents/delegation.md`](https://github.com/zeroclaw-labs/zeroclaw/blob/757db6c356c61861256a87222e30c7c92e8f166f/docs/book/src/agents/delegation.md), [`crates/zeroclaw-runtime/src/tools/delegate.rs`](https://github.com/zeroclaw-labs/zeroclaw/blob/757db6c356c61861256a87222e30c7c92e8f166f/crates/zeroclaw-runtime/src/tools/delegate.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: this is caller-scoped portfolio control, not a claim that one agent globally controls every configured agent/task in the installation.
- Whole-system current view: within the declared caller-owned delegated-work subsystem, `list_results`/`check_result` expose current task lifecycle state; `await_sessions` aggregates multiple task states/results.
- Current-control decision scope: start new delegated work or cancel existing caller-owned background work, changing the current portfolio.

## S3* — Complementary audit

- State: —
- Function: no material first-party runtime path establishes an independent complementary auditor whose distinct findings about operational reality close back into corrective S1 behavior.
- Disturbance / variety regulated: not established as S3* at the reviewed boundary.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: SOP audit logging, security/audit records, observability, task lifecycle/recovery and the skill-review fork exist but serve logging/enforcement/recovery or prospective adaptation rather than a distinct S3* audit function.
- Closure path: not applicable.
- Why this is / is not agent-owned: audit loggers store evidence; deterministic monitors enforce/recover runtime state; the model-driven skill reviewer changes future skills and is therefore classified as S4 rather than complementary current-operation audit.
- Evidence: [`crates/zeroclaw-runtime/src/sop/audit.rs`](https://github.com/zeroclaw-labs/zeroclaw/blob/757db6c356c61861256a87222e30c7c92e8f166f/crates/zeroclaw-runtime/src/sop/audit.rs), [`crates/zeroclaw-runtime/src/skills/review.rs`](https://github.com/zeroclaw-labs/zeroclaw/blob/757db6c356c61861256a87222e30c7c92e8f166f/crates/zeroclaw-runtime/src/skills/review.rs).
- Basis: structural absence review.
- Confidence: medium-high.
- Caveats: security and SOP evidence stores may be useful inputs to an external/parent audit process, but such a distinct closing actor was not established inside the reviewed runtime boundary.

### Absence scope

- Surfaces inspected: SOP audit logger, runtime observability/logging, security/audit surfaces, task lifecycle/recovery surfaces, skill review and approval mechanisms.
- Plausible paths considered: audit logging as S3*, security scanning/enforcement as S3*, skill review as S3*, deterministic recovery as S3*.
- Why no material path remains: none establishes the required independent complementary operational-reality claim plus corrective closure into S1; the strongest model-driven review path is prospective skill adaptation.

## S4 — Outside-and-then adaptation

- State: A
- Function: detect durable lessons from completed operational interaction and modify persistent skills that shape future agent behavior.
- Disturbance / variety regulated: user corrections, workflow corrections, failed/outdated skills, reusable techniques/workarounds and newly learned task-class knowledge.
- Decisive decision or feedback right: decide whether a durable adaptation is warranted and directly patch, extend or archive the installed skill library.
- Decision owner: the first-party background SKILL REVIEW model agent.
- Supporting / enforcement mechanisms: post-turn trigger threshold, failure-signal extraction, restricted review tool registry, skill validation, atomic writes, cooldowns and improvement audit metadata.
- Closure path: completed operational history/tool outcomes → background review fork → model identifies durable adaptation → `skill_manage` mutates persistent skill artifacts → later sessions discover/read changed skills → future operational behavior is altered.
- Boundary reachability: the review subsystem is shipped in `zeroclaw-runtime`; `review.rs` documents the production caller path, and when the first-party `SkillImprovementConfig` is enabled the fork runs with built-in review tools rather than requiring downstream review code.
- Why this is / is not agent-owned: the trigger and write validation are deterministic, but the model review agent decides whether/what durable lesson to encode and can execute the persistent mutation without human approval (`approval: None`).
- Evidence: [`crates/zeroclaw-runtime/src/skills/review.rs`](https://github.com/zeroclaw-labs/zeroclaw/blob/757db6c356c61861256a87222e30c7c92e8f166f/crates/zeroclaw-runtime/src/skills/review.rs), [`crates/zeroclaw-runtime/src/skills/review_prompt.md`](https://github.com/zeroclaw-labs/zeroclaw/blob/757db6c356c61861256a87222e30c7c92e8f166f/crates/zeroclaw-runtime/src/skills/review_prompt.md), [`crates/zeroclaw-runtime/src/tools/skill_manage.rs`](https://github.com/zeroclaw-labs/zeroclaw/blob/757db6c356c61861256a87222e30c7c92e8f166f/crates/zeroclaw-runtime/src/tools/skill_manage.rs), [`crates/zeroclaw-runtime/src/skills/improver.rs`](https://github.com/zeroclaw-labs/zeroclaw/blob/757db6c356c61861256a87222e30c7c92e8f166f/crates/zeroclaw-runtime/src/skills/improver.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the feature is configuration-gated; the `A` state describes the shipped first-party operating mode when skill improvement is enabled, not an assertion that every installation enables it by default.

## S5 — Identity / ultimate policy

- State: —
- Function: no material first-party path establishes organization-level identity/ultimate-policy adjudication closure inside the ZeroClaw runtime.
- Disturbance / variety regulated: not established as S5 at the reviewed boundary.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: configured identities/personality, risk profiles, supervised approvals, security policy and `escalate_to_human` constrain or escalate current operation but are not by themselves S5.
- Closure path: not applicable.
- Why this is / is not agent-owned: the human can answer escalated operational questions and authorize actions, but the reviewed path does not distinguish or resolve organization identity/constitutional-policy questions as an ultimate-policy function.
- Evidence: [`README.md`](https://github.com/zeroclaw-labs/zeroclaw/blob/757db6c356c61861256a87222e30c7c92e8f166f/README.md), [`crates/zeroclaw-tools/src/escalate.rs`](https://github.com/zeroclaw-labs/zeroclaw/blob/757db6c356c61861256a87222e30c7c92e8f166f/crates/zeroclaw-tools/src/escalate.rs), [`crates/zeroclaw-runtime/src/identity.rs`](https://github.com/zeroclaw-labs/zeroclaw/blob/757db6c356c61861256a87222e30c7c92e8f166f/crates/zeroclaw-runtime/src/identity.rs).
- Basis: structural absence review.
- Confidence: medium-high.
- Caveats: downstream deployments may place ZeroClaw under a human or external S5 parent; that parent is outside this standalone repository assessment.

### Absence scope

- Surfaces inspected: configured agent identity/personality, risk/security policy, supervised action approval, human escalation, SOP approval and delegation authority surfaces.
- Plausible paths considered: operator approval as S5, `escalate_to_human` as S5, static identity/personality configuration as S5, risk policy as S5.
- Why no material path remains: these surfaces define/configure constraints or resolve current operational actions; no first-party question → identity/ultimate-policy adjudication → authoritative governing return loop was established.

## Distributed OSS / parent arrangement

ZeroClaw can be embedded under an external human or organizational parent, and its escalation/approval surfaces make that arrangement practical. This standalone assessment does not credit external operators or downstream governance as first-party S5 ownership. Likewise, configured specialist agents are part of the installation only where the first-party runtime directly owns the delegation relation; their downstream authored prompts/skills are not silently credited as repository semantics.

## Self-hosted / non-human modes

The product is explicitly self-hosted and can run with local providers and locally persisted state. S1, S3 and the enabled S4 review mode do not require a remote organizational controller. External model inference may still be selected as a provider, but provider ownership is not treated as ownership of VSM decision rights.

## Recursion

Configured delegated agents provide a first-party recursion mechanism: the parent/caller hands a bounded task to another configured identity that executes its own model/tool loop under its target policy. Delegation depth is bounded by runtime policy. `spawn_subagent` is a same-identity child-run mechanism and is not used as the sole proof of a distinct recursive organization.

## Variety and escalation

Operational variety is absorbed through model/tool iteration, multiple providers/tools, delegation to configured specialists and SOP execution under risk policy. Background delegation expands operational capacity while preserving caller-scoped lifecycle control. Human escalation can return an operator response for difficult current situations. Separately, the skill-review path reduces future variety by turning durable corrections and reusable techniques into persistent operating knowledge.

## Evidence gaps

- No S2 state is credited without stronger evidence of a concrete inter-S1 disturbance and its attenuation relation; generic delegation, shared budgets and parallel execution remain non-qualifying shortcuts.
- No runtime S3* actor was established beyond audit/logging/enforcement/recovery and the separately classified S4 review fork.
- No S5 identity/ultimate-policy closure was established; operational human escalation/approval is intentionally not promoted to S5=P.
- The S4 state depends on the shipped skill-improvement operating mode being enabled; future reassessment should verify if its production reachability/defaults materially change.

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
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: A
autonomy_s5: —
---

# ZeroClaw

## Review boundary

- System in focus: one first-party ZeroClaw agent-runtime installation at pinned revision `757db6c356c61861256a87222e30c7c92e8f166f`, including the canonical agent loop, configured-agent delegation, background task control, SOP/runtime policy, persistent skills and the shipped skill-review path.
- Purpose and identity: operate a locally owned personal AI-agent runtime that accepts work through configured channels, executes model/tool turns, delegates bounded work to configured specialist agents, and can persist learned operating knowledge into its skill library.
- Relevant environment: user requests, channel inputs, model/provider responses, tool results and failures, external services, concurrent delegated work, installed skills and operator-configured risk/identity policy.
- Standard-distribution boundary: the shipped ZeroClaw Rust binary and first-party runtime/tool surfaces at the pinned revision. External model providers, MCP servers, user-authored skills, downstream custom agents, repository-development workflows and maintainers are outside organizational ownership.
- Credited operating / distribution surfaces: canonical agent loop and tool execution, configured-agent delegation, background delegate task control, standard security/approval gates, SOP runtime, persistent skill library, and first-party background skill review.
- Adjacent first-party surfaces excluded from ownership: contribution/release automation, development-only tests/fixtures, repository governance, and development audits that do not execute as a runtime organizational actor.
- First-party operating / deployment modes considered: interactive/channel agent turns, configured delegation and background delegation, SOP execution, supervised/other shipped risk-policy modes, and opt-in first-party skill improvement.
- Recursion level: one ZeroClaw installation. Distinct configured delegated agents can form subordinate S1 units because `delegate` transfers work to a different configured identity/model/tool policy; same-identity `spawn_subagent` is supporting evidence but is not required for the distinct-unit claim.
- Reviewed revision: `757db6c356c61861256a87222e30c7c92e8f166f`.
- Observation date: 2026-09-21.
- Generated Profile version: 0.2.3.
- Generated Methodology version: 0.3.5.
- Current Profile version: 0.2.3.
- Current Methodology version: 0.3.5.

## Repository architecture

ZeroClaw ships its own agent runtime rather than only wrapping an external harness. The shipped binary routes configured channels into a first-party agent loop that calls models and tools under runtime security policy. The runtime also owns configured-agent delegation, task lifecycle state, SOP execution, persistent skills and a model-driven background skill-review fork.

`delegate` hands work to a different configured agent identity and supports synchronous, parallel and background execution. Background lifecycle state is persisted in the control plane, and the caller can inspect, wait for and cancel its own delegated tasks. This establishes inside-and-now portfolio control, but delegation itself is not treated as S2.

For future adaptation, `maybe_run_skill_review` receives completed operational history and failure hints, launches a restricted model fork with `skills_list`, `skill_view` and mutating `skill_manage`, and explicitly supplies no human approval callback. Its shipped prompt instructs the review agent to detect user/workflow corrections, failed or outdated skills and reusable techniques, then persist class-level skill changes for later sessions.

Audit-named runtime surfaces are not automatically S3*. `SopAuditLogger`, for example, records run/step/security events and exposes stored records; it does not establish an independent complementary auditor that makes a distinct claim about operational reality and closes corrective feedback into S1. The model-driven skill reviewer is classified by its prospective adaptation function as S4 rather than double-counted as S3*.

Human escalation is likewise not automatically S5. `escalate_to_human` can ask an operator and optionally wait for a reply, while supervised approvals and risk profiles constrain current actions. The reviewed evidence does not establish identity/ultimate-policy adjudication closure.

Primary evidence:

- [`README.md`](https://github.com/zeroclaw-labs/zeroclaw/blob/757db6c356c61861256a87222e30c7c92e8f166f/README.md) — shipped runtime, agent loop, tools, security policy and SOP surface.
- [`docs/book/src/agents/delegation.md`](https://github.com/zeroclaw-labs/zeroclaw/blob/757db6c356c61861256a87222e30c7c92e8f166f/docs/book/src/agents/delegation.md) — configured-agent identities, parallel/background delegation and task control.
- [`crates/zeroclaw-runtime/src/tools/delegate.rs`](https://github.com/zeroclaw-labs/zeroclaw/blob/757db6c356c61861256a87222e30c7c92e8f166f/crates/zeroclaw-runtime/src/tools/delegate.rs) — first-party delegate/background implementation.
- [`crates/zeroclaw-runtime/src/skills/review.rs`](https://github.com/zeroclaw-labs/zeroclaw/blob/757db6c356c61861256a87222e30c7c92e8f166f/crates/zeroclaw-runtime/src/skills/review.rs) — post-turn review fork and explicit no-human-in-loop execution.
- [`crates/zeroclaw-runtime/src/skills/review_prompt.md`](https://github.com/zeroclaw-labs/zeroclaw/blob/757db6c356c61861256a87222e30c7c92e8f166f/crates/zeroclaw-runtime/src/skills/review_prompt.md) — operational signals and future skill adaptation policy.
- [`crates/zeroclaw-runtime/src/skills/improver.rs`](https://github.com/zeroclaw-labs/zeroclaw/blob/757db6c356c61861256a87222e30c7c92e8f166f/crates/zeroclaw-runtime/src/skills/improver.rs) — durable skill mutation and history-derived success/failure signals.
- [`crates/zeroclaw-runtime/src/tools/skill_manage.rs`](https://github.com/zeroclaw-labs/zeroclaw/blob/757db6c356c61861256a87222e30c7c92e8f166f/crates/zeroclaw-runtime/src/tools/skill_manage.rs) — patch/write/archive mutation surface.
- [`crates/zeroclaw-runtime/src/sop/audit.rs`](https://github.com/zeroclaw-labs/zeroclaw/blob/757db6c356c61861256a87222e30c7c92e8f166f/crates/zeroclaw-runtime/src/sop/audit.rs) — evidence/log storage rather than an independent runtime auditor.
- [`crates/zeroclaw-tools/src/escalate.rs`](https://github.com/zeroclaw-labs/zeroclaw/blob/757db6c356c61861256a87222e30c7c92e8f166f/crates/zeroclaw-tools/src/escalate.rs) — real operator escalation/response path, not by itself S5.

## Operational model

Inbound channel or CLI work enters the first-party model/tool loop. The model chooses substantive actions; policy and approval mechanisms constrain execution; returned observations inform subsequent model decisions. A caller can delegate work to another configured identity and manage its current background delegated-task portfolio. After sufficiently tool-active work, the optional first-party skill-review path can inspect completed history and autonomously persist changes to skills that affect future sessions.

## S1 — Operations

- State: A
- Function: perform user- or event-directed work through a model-driven tool/observation loop and return operational outcomes.
- Disturbance / variety regulated: ambiguous requests, external/tool results, provider responses, failures, installed capabilities and changing task context.
- Decisive decision or feedback right: choose substantive next actions/tools and revise the plan from returned observations within configured authority.
- Decision owner: the running ZeroClaw model agent; delegated configured agents own their delegated work at their recursion level.
- Supporting / enforcement mechanisms: agent loop, tool registry/dispatcher, security policy, approval bridge, provider transport, memory/context handling and tool receipts.
- Closure path: inbound work → model decision → authorized tool/delegation action → observation/result → subsequent model decision → outcome.
- Boundary reachability: the standard `zeroclaw agent -a <alias>`/channel runtime enters the first-party agent loop shipped in the ZeroClaw binary; no downstream harness is required.
- Why this is / is not agent-owned: deterministic runtime code transports and constrains actions, while the model chooses substantive operational actions from current evidence.
- Evidence: [`README.md`](https://github.com/zeroclaw-labs/zeroclaw/blob/757db6c356c61861256a87222e30c7c92e8f166f/README.md), [`crates/zeroclaw-runtime/src/agent/loop_.rs`](https://github.com/zeroclaw-labs/zeroclaw/blob/757db6c356c61861256a87222e30c7c92e8f166f/crates/zeroclaw-runtime/src/agent/loop_.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: external model inference is execution substrate, not an imported organizational owner.

## S2 — Coordination

- State: —
- Function: no material first-party path was established that attenuates a concrete cross-S1 interference condition among distinct operational units.
- Disturbance / variety regulated: not established as S2 at the reviewed boundary.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: delegation policy, shared action/cost ceilings, depth limits, routing, task sequencing and parallel execution exist, but none is credited without a demonstrated S2-specific disturbance relation.
- Closure path: not applicable.
- Why this is / is not agent-owned: the repository supports communication and work distribution among agents, but delegation/parallelism alone does not prove coordination in the VSM sense.
- Evidence: [`docs/book/src/agents/delegation.md`](https://github.com/zeroclaw-labs/zeroclaw/blob/757db6c356c61861256a87222e30c7c92e8f166f/docs/book/src/agents/delegation.md), [`crates/zeroclaw-runtime/src/tools/delegate.rs`](https://github.com/zeroclaw-labs/zeroclaw/blob/757db6c356c61861256a87222e30c7c92e8f166f/crates/zeroclaw-runtime/src/tools/delegate.rs).
- Basis: structural absence review.
- Confidence: medium-high.
- Caveats: reassess if first-party evidence explicitly connects a coordination mechanism to shared-resource contention, oscillation or another cross-S1 disturbance.

### Absence scope

- Surfaces inspected: configured-agent delegation, same-identity subagents, parallel fan-out, background task lifecycle, shared policy/budget inheritance, SOP graph/routing and task-control surfaces.
- Plausible first-party paths checked: delegation as coordination; shared budgets as coordination; parallel-execution limits; message routing; SOP sequencing.
- Why no material first-party path remains: these establish task distribution, enforcement and sequencing, but not a concrete cross-S1 disturbance → attenuation → changed S1-behaviour closure.

## S3 — Inside-and-now control

- State: A
- Function: regulate the current portfolio of background work delegated by a configured caller agent.
- Disturbance / variety regulated: changing workload, long-running delegated tasks, completed/failed work and tasks that are no longer needed.
- Decisive decision or feedback right: create background delegated commitments, inspect/list caller-owned tasks, wait for selected tasks and cancel current work.
- Decision owner: the model-driven caller agent using the built-in `delegate` control surface.
- Supporting / enforcement mechanisms: control-plane database, caller-scoped task/result registry, cancellation tokens and delegation policy.
- Closure path: current delegated-task portfolio → model invokes list/check/await → current-control decision → delegate/cancel/continue → lifecycle state changes → updated portfolio.
- Boundary reachability: `delegate` is a first-party runtime tool; background mode returns `task_id`, and the same surface exposes `check_result`, `list_results`, `cancel_task` and `await_sessions` for caller-owned tasks.
- Why this is / is not agent-owned: persistence/cancellation mechanics are deterministic, while the model caller decides which current commitments to create, inspect, await or cancel.
- Evidence: [`docs/book/src/agents/delegation.md`](https://github.com/zeroclaw-labs/zeroclaw/blob/757db6c356c61861256a87222e30c7c92e8f166f/docs/book/src/agents/delegation.md), [`crates/zeroclaw-runtime/src/tools/delegate.rs`](https://github.com/zeroclaw-labs/zeroclaw/blob/757db6c356c61861256a87222e30c7c92e8f166f/crates/zeroclaw-runtime/src/tools/delegate.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: this is caller-scoped portfolio control, not a claim that one agent controls every configured task in the installation.
- Whole-system current view: within the declared caller-owned delegated-work subsystem, `list_results`/`check_result` expose current lifecycle state and `await_sessions` aggregates multiple tasks.
- Current-control decision scope: start new delegated work or cancel existing caller-owned background work, changing the current portfolio.

## S3* — Complementary audit

- State: —
- Function: no material first-party runtime path establishes an independent complementary auditor whose distinct operational-reality findings close back into corrective S1 behavior.
- Disturbance / variety regulated: not established as S3* at the reviewed boundary.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: SOP audit logging, security/audit records, observability, task recovery and the skill-review fork serve logging/enforcement/recovery or prospective adaptation rather than S3*.
- Closure path: not applicable.
- Why this is / is not agent-owned: audit loggers store evidence; deterministic monitors enforce/recover state; the model-driven skill reviewer changes future skills and is classified as S4.
- Evidence: [`crates/zeroclaw-runtime/src/sop/audit.rs`](https://github.com/zeroclaw-labs/zeroclaw/blob/757db6c356c61861256a87222e30c7c92e8f166f/crates/zeroclaw-runtime/src/sop/audit.rs), [`crates/zeroclaw-runtime/src/skills/review.rs`](https://github.com/zeroclaw-labs/zeroclaw/blob/757db6c356c61861256a87222e30c7c92e8f166f/crates/zeroclaw-runtime/src/skills/review.rs).
- Basis: structural absence review.
- Confidence: medium-high.
- Caveats: evidence stores may feed an external/parent audit process, but no such closing runtime actor was established inside the boundary.

### Absence scope

- Surfaces inspected: SOP audit logger, runtime observability/logging, security/audit surfaces, task lifecycle/recovery, skill review and approval mechanisms.
- Plausible first-party paths checked: audit logging as S3*; security scanning/enforcement as S3*; skill review as S3*; deterministic recovery as S3*.
- Why no material first-party path remains: none establishes an independent complementary operational-reality claim plus corrective closure into S1; the strongest model-driven review path is prospective adaptation.

## S4 — Outside-and-then adaptation

- State: A
- Function: detect durable lessons from completed operational interaction and modify persistent skills that shape future agent behavior.
- Disturbance / variety regulated: user corrections, workflow corrections, failed/outdated skills, reusable techniques/workarounds and newly learned task-class knowledge.
- Decisive decision or feedback right: decide whether a durable adaptation is warranted and directly patch, extend or archive the installed skill library.
- Decision owner: the first-party background SKILL REVIEW model agent.
- Supporting / enforcement mechanisms: post-turn trigger threshold, failure-signal extraction, restricted review tools, skill validation, atomic writes, cooldowns and audit metadata.
- Closure path: completed operational history/tool outcomes → review fork → model identifies durable adaptation → `skill_manage` mutates persistent skills → later sessions consume changed skills → future operation changes.
- Boundary reachability: the review subsystem ships in `zeroclaw-runtime`; `review.rs` identifies the production caller path, and enabling first-party `SkillImprovementConfig` requires no downstream review implementation.
- Why this is / is not agent-owned: trigger/write validation are deterministic, but the model review agent decides whether/what durable lesson to encode and can execute the mutation with `approval: None`.
- Evidence: [`crates/zeroclaw-runtime/src/skills/review.rs`](https://github.com/zeroclaw-labs/zeroclaw/blob/757db6c356c61861256a87222e30c7c92e8f166f/crates/zeroclaw-runtime/src/skills/review.rs), [`crates/zeroclaw-runtime/src/skills/review_prompt.md`](https://github.com/zeroclaw-labs/zeroclaw/blob/757db6c356c61861256a87222e30c7c92e8f166f/crates/zeroclaw-runtime/src/skills/review_prompt.md), [`crates/zeroclaw-runtime/src/tools/skill_manage.rs`](https://github.com/zeroclaw-labs/zeroclaw/blob/757db6c356c61861256a87222e30c7c92e8f166f/crates/zeroclaw-runtime/src/tools/skill_manage.rs), [`crates/zeroclaw-runtime/src/skills/improver.rs`](https://github.com/zeroclaw-labs/zeroclaw/blob/757db6c356c61861256a87222e30c7c92e8f166f/crates/zeroclaw-runtime/src/skills/improver.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: this is a configuration-gated shipped operating mode; `A` does not imply every installation enables it by default.
- External distinction: the review fork evaluates evidence from the just-completed operation and user/environment feedback rather than merely continuing the same immediate task loop.
- Future / prospective distinction: it decides what durable class-level operating knowledge should govern later sessions, not only how to finish the current turn.
- Adaptation option generated: patch an existing skill, add a durable support artifact, create a class-level skill, archive an obsolete skill, or intentionally make no change.
- Path back into current capability / S3: accepted review decisions persist directly into the installed skill library; subsequent normal agent turns discover/read those changed skills, so the adapted capability re-enters operational control without a downstream maintainer step.

## S5 — Identity / ultimate policy

- State: —
- Function: no material first-party path establishes organization-level identity/ultimate-policy adjudication closure inside the runtime.
- Disturbance / variety regulated: not established as S5 at the reviewed boundary.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: configured identity/personality, risk profiles, supervised approvals, security policy and `escalate_to_human` constrain/escalate current operation but are not by themselves S5.
- Closure path: not applicable.
- Why this is / is not agent-owned: a human can answer operational questions and authorize actions, but the reviewed path does not resolve organization identity or constitutional-policy questions as an ultimate-policy function.
- Evidence: [`README.md`](https://github.com/zeroclaw-labs/zeroclaw/blob/757db6c356c61861256a87222e30c7c92e8f166f/README.md), [`crates/zeroclaw-tools/src/escalate.rs`](https://github.com/zeroclaw-labs/zeroclaw/blob/757db6c356c61861256a87222e30c7c92e8f166f/crates/zeroclaw-tools/src/escalate.rs), [`crates/zeroclaw-runtime/src/identity.rs`](https://github.com/zeroclaw-labs/zeroclaw/blob/757db6c356c61861256a87222e30c7c92e8f166f/crates/zeroclaw-runtime/src/identity.rs).
- Basis: structural absence review.
- Confidence: medium-high.
- Caveats: downstream deployments may place ZeroClaw under a human/external S5 parent; that parent is outside this standalone assessment.

### Absence scope

- Surfaces inspected: configured agent identity/personality, risk/security policy, supervised action approval, human escalation, SOP approval and delegation authority.
- Plausible first-party paths checked: operator approval as S5; `escalate_to_human` as S5; static identity/personality configuration as S5; risk policy as S5.
- Why no material first-party path remains: these surfaces define constraints or resolve current operational actions; no question → identity/ultimate-policy adjudication → authoritative governing return loop was established.

## Distributed OSS / parent arrangement

ZeroClaw can run under an external human or organizational parent, and its escalation/approval surfaces support that arrangement. This standalone assessment does not credit external operators or downstream governance as first-party S5 ownership. Configured specialist agents are credited only where the first-party runtime owns the delegation relation; downstream-authored semantics are not silently imported.

## Self-hosted / non-human modes

The product is explicitly self-hosted and can use local providers and local persisted state. S1, S3 and enabled S4 review do not require a remote organizational controller. External model inference may still be selected as substrate without becoming owner of the VSM decision rights.

## Recursion

Configured delegated agents provide a first-party recursion mechanism: the caller hands a bounded task to another configured identity that executes its own model/tool loop under target policy. Delegation depth is bounded by runtime policy. Same-identity `spawn_subagent` is not used as the sole proof of a distinct recursive organization.

## Variety and escalation

Operational variety is absorbed through model/tool iteration, providers/tools, configured-agent delegation and SOP execution under risk policy. Background delegation expands operational capacity while preserving caller-scoped current control. Human escalation can return an operator response for difficult current situations. Separately, the skill-review path reduces future variety by turning durable corrections and reusable techniques into persistent operating knowledge.

## Evidence gaps

- No S2 state is credited without stronger evidence of a concrete inter-S1 disturbance and attenuation relation; generic delegation, shared budgets and parallel execution remain non-qualifying shortcuts.
- No runtime S3* actor was established beyond logging/enforcement/recovery and the separately classified S4 review fork.
- No S5 identity/ultimate-policy closure was established; operational human escalation/approval is intentionally not promoted to S5=P.
- S4 depends on the shipped skill-improvement mode being enabled; reassess if its production reachability or semantics materially change.

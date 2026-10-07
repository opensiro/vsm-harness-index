---
harness_id: pi-rs
project_name: pi-rs
repository: https://github.com/CCherry07/pi-rs
review_ref: efb6925e248ea801448fd09e60623d109852d3c9
reviewed_at: 2026-10-07
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: A
autonomy_s5: —
---

# pi-rs

## Review boundary

- System in focus: the shipped pi-rs Rust terminal coding-agent product at the frozen revision, including its native agent/session/runtime, Coding domain assembly, first-party tools, bundled subagent collaboration plugin, built-in Hermes memory provider, and supported CLI/TUI/print/JSON/RPC/ACP modes.
- Purpose and identity: an independent Rust implementation of a terminal coding agent that executes coding work, delegates to reusable isolated child sessions, controls the live collaboration tree, performs independent review through role-specific children, and can preserve model-selected reusable learning as future skill capability.
- Relevant environment: the selected project/workspace, local filesystem/shell, configured model/provider, trusted project resources, bundled/global skills/plugins, persistent Pi sessions, and user-facing terminal/API clients.
- Standard-distribution boundary: pi-rs first-party Rust product and bundled first-party plugins. Current TypeScript Pi under `legacy/pi` is behavioral/reference lineage only and is not an evidence donor. External model providers, third-party extensions/plugins, MCP servers, package registries, and operating-system permissions are dependencies/environment.
- Credited operating / distribution surfaces: `crates/pi-agent`, `crates/pi-session`, `crates/pi-runtime`, `domains/coding`, first-party production tool plugins, `plugins/features/pi-plugin-subagents`, and the default `plugins/features/pi-plugin-memory-hermes` provider plus supported product entry points that instantiate them.
- Adjacent first-party surfaces excluded from ownership: `legacy/pi` reference implementation, repository CI/release workflows, eval/benchmark crates as evaluation evidence, research notes, desktop-only code not needed for the claimed terminal witness modes, and docs/tests except where they corroborate a shipped runtime path.
- First-party operating / deployment modes considered: standard local coding sessions with bundled collaboration tools; reviewer child profile; default Hermes memory provider with background review enabled; trusted-project skill mode where relevant; CLI/TUI and non-interactive adapters sharing the product runtime.
- Recursion level: one pi-rs coding session as system-in-focus; isolated subagent sessions are subordinate operational units whose coordination/current control belongs to the parent collaboration tree.
- Reviewed revision: `efb6925e248ea801448fd09e60623d109852d3c9`.
- Observation date: 2026-10-07.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

pi-rs implements a provider-neutral Rust agent loop with first-party coding tools, durable Pi v4 session state, input queues, compaction/recovery, multiple terminal/protocol frontends, plugin generations, project trust, and resource loading. Model/tool results are persisted through the session runtime and feed subsequent agent decisions.

The bundled subagents plugin exposes six model-callable collaboration tools: `spawn_agent`, `send_message`, `followup_task`, `wait_agent`, `interrupt_agent`, and `list_agents`. Children execute in reusable isolated sessions. Spawns are asynchronous, bounded by root concurrency/depth/budget, excess launches queue FIFO, normal reports automatically rejoin the parent context, and the parent can inspect the descendant tree, wait on barriers/races, send information, issue follow-up work, or interrupt an active child turn while preserving its session. The shipped parent guidance explicitly notes that children share the working directory/filesystem, requires disjoint write ownership for parallel editors, and tells the parent to re-plan after each result/message.

The built-in `reviewer` profile is a separate child role with only read/grep/find/ls tools, no nested subagents/skills, a dedicated review prompt, and an explicit merge verdict. It inspects source evidence independently and returns the report through the ordinary child-result rejoin path to the parent, which retains final orchestration/acceptance authority.

Hermes is the default memory provider. Its normal memory persistence is supporting state, but the product also ships a separate model-backed background review path. `review_enabled` defaults true; after eligible user turns/final responses, a fresh review can inspect the completed session for durable preferences and reusable verified techniques. The skill-review prompt instructs the review model to patch an existing agent-managed skill, extend an umbrella, add supporting files, or create a new class-level skill only when evidence supports reusable future value. The write guard enforces current-review read-before-write, provenance, pin/ownership/hash boundaries, and project trust. Successful skill changes persist outside the current session's frozen prompt and become reusable capability for later sessions/catalog reloads. Curator adds optional periodic library-wide pruning/consolidation under stricter ownership/scope controls.

Primary evidence:
- [README](https://github.com/CCherry07/pi-rs/blob/efb6925e248ea801448fd09e60623d109852d3c9/README.md)
- [subagent plugin registration and parent guidance](https://github.com/CCherry07/pi-rs/blob/efb6925e248ea801448fd09e60623d109852d3c9/plugins/features/pi-plugin-subagents/src/lib.rs)
- [collaboration tools](https://github.com/CCherry07/pi-rs/blob/efb6925e248ea801448fd09e60623d109852d3c9/plugins/features/pi-plugin-subagents/src/tool.rs)
- [durable collaboration runtime](https://github.com/CCherry07/pi-rs/blob/efb6925e248ea801448fd09e60623d109852d3c9/plugins/features/pi-plugin-subagents/src/runtime.rs)
- [reviewer profile](https://github.com/CCherry07/pi-rs/blob/efb6925e248ea801448fd09e60623d109852d3c9/plugins/features/pi-plugin-subagents/agents/reviewer.md)
- [built-in agent profiles](https://github.com/CCherry07/pi-rs/blob/efb6925e248ea801448fd09e60623d109852d3c9/plugins/features/pi-plugin-subagents/src/profiles.rs)
- [Hermes defaults and skill tool contract](https://github.com/CCherry07/pi-rs/blob/efb6925e248ea801448fd09e60623d109852d3c9/plugins/features/pi-plugin-memory-hermes/src/config.rs)
- [Hermes lifecycle/background review](https://github.com/CCherry07/pi-rs/blob/efb6925e248ea801448fd09e60623d109852d3c9/plugins/features/pi-plugin-memory-hermes/src/lib.rs)
- [skill-review adaptation policy](https://github.com/CCherry07/pi-rs/blob/efb6925e248ea801448fd09e60623d109852d3c9/plugins/features/pi-plugin-memory-hermes/src/prompts/skill_review.md)
- [skill write safeguards](https://github.com/CCherry07/pi-rs/blob/efb6925e248ea801448fd09e60623d109852d3c9/plugins/features/pi-plugin-memory-hermes/src/skill_review.rs)
- [Curator runtime](https://github.com/CCherry07/pi-rs/blob/efb6925e248ea801448fd09e60623d109852d3c9/plugins/features/pi-plugin-memory-hermes/src/curator/runtime.rs)

## Operational model

The root coding agent performs the focal coding task and can create subordinate model-backed child sessions. The collaboration plugin does not merely fan out prompts: it exposes explicit inter-child coordination and parent current-control rights, while deterministic runtime state supplies queues, durable identifiers, recovery, concurrency/depth limits, and cancellation transport.

A normal bounded child report automatically joins the parent's context. The parent therefore remains the organizational owner that partitions work, observes the active tree, handles dependencies/results, decides interventions, and accepts/rejects the combined outcome.

Hermes background review is a distinct adaptation witness. The review agent cannot freely rewrite arbitrary skill state: its decisions are bounded to agent-owned/unpinned/unchanged skills, fresh evidence reads are required, protected/user/external skills remain outside its authority, and writes persist for later reuse rather than mutating the current session's frozen memory prompt.

## S1 — Operations

- State: A
- Function: perform open-ended coding work through model-selected first-party tools and iterative reaction to source/tool/provider results.
- Disturbance / variety regulated: changing code/task requirements, repository state, tool/test failures, provider outputs, user input, and session recovery/continuation conditions.
- Decisive decision or feedback right: select coding actions/tools, interpret results, change approach, delegate bounded work, and decide when the requested operation is complete.
- Decision owner: the root coding agent, with subordinate worker agents owning delegated operational tasks.
- Supporting / enforcement mechanisms: pi-agent loop/tool scheduler, Coding tool plugins, durable session journal/queues, compaction/recovery, project trust/resource generation, provider adapters.
- Closure path: user/task input → model decision → first-party tool action → persisted tool/result evidence → next model decision → further action or terminal response.
- Boundary reachability: Coding product assembly and supported frontends instantiate the same first-party agent/session/tool runtime at the frozen revision.
- Why this is / is not agent-owned: deterministic Rust code executes, persists and constrains actions, but the model chooses task-specific operations and reacts to returned evidence; removing model discretion leaves execution machinery rather than materially the same coding operation.
- Evidence: [README](https://github.com/CCherry07/pi-rs/blob/efb6925e248ea801448fd09e60623d109852d3c9/README.md); [crates/pi-agent](https://github.com/CCherry07/pi-rs/tree/efb6925e248ea801448fd09e60623d109852d3c9/crates/pi-agent); [domains/coding](https://github.com/CCherry07/pi-rs/tree/efb6925e248ea801448fd09e60623d109852d3c9/domains/coding).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: external providers supply inference; project trust and OS permissions bound reachable actions but do not own the open-ended task decision.

## S2 — Coordination

- State: A
- Function: attenuate interference among simultaneously viable child S1 units by assigning disjoint write ownership, separating independent from dependency-constrained work, and reintegrating reports/messages before dependent action.
- Disturbance / variety regulated: shared-filesystem write collisions, dependency races, duplicated/conflicting work, and premature dependent decisions while peer work remains unsettled.
- Decisive decision or feedback right: choose child task/scope, decide which children may run concurrently, message or wait on dependencies, and re-plan after reports/messages.
- Decision owner: the parent/root model-backed agent.
- Supporting / enforcement mechanisms: asynchronous `spawn_agent`, FIFO concurrency queue, stable child ids, durable collaboration messages, automatic report rejoin, `wait_agent` barriers/races, follow-up sessions, root depth/spawn limits.
- Distinct S1 units: model-backed reusable isolated child sessions performing bounded coding/research/review tasks under the parent session.
- Inter-S1 disturbance: child sessions share the current working directory/filesystem, so parallel editors can collide; dependent work can also consume stale/incomplete peer results if advanced concurrently.
- Attenuating coordination relation: shipped parent guidance requires disjoint write ownership for parallel editors, launches only independent children together, uses waits/messages for dependencies, and re-plans from returned results.
- Feedback into subsequent S1 behaviour: bounded child reports/messages rejoin the parent context; wait results and statuses change which child/follow-up/dependent work the parent launches or accepts next.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the collaboration rules explicitly regulate a concrete shared-workspace/dependency interference risk among distinct concurrently viable S1 units and alter whether/how those units may execute.
- Closure path: parent partitions work → independent child S1s run concurrently under disjoint ownership / dependent paths wait → reports/messages/status return → parent re-plans and launches/continues dependent S1 work.
- Boundary reachability: all six collaboration operations are model-callable tools registered by the bundled first-party subagents plugin; parent guidance is injected into eligible root sessions.
- Why this is / is not agent-owned: deterministic concurrency limits/queues/messages enforce transport, while the parent model owns the substantive partition, independence/dependency judgment and response to peer results.
- Evidence: [subagent parent guidance](https://github.com/CCherry07/pi-rs/blob/efb6925e248ea801448fd09e60623d109852d3c9/plugins/features/pi-plugin-subagents/src/lib.rs); [tool.rs](https://github.com/CCherry07/pi-rs/blob/efb6925e248ea801448fd09e60623d109852d3c9/plugins/features/pi-plugin-subagents/src/tool.rs); [runtime.rs](https://github.com/CCherry07/pi-rs/blob/efb6925e248ea801448fd09e60623d109852d3c9/plugins/features/pi-plugin-subagents/src/runtime.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: concurrency capacity/FIFO ordering itself is deterministic support; S2 ownership rests on the parent agent's conflict/dependency decisions.

## S3 — Inside-and-now control

- State: A
- Function: maintain a whole-current collaboration-tree view and regulate active child commitments through observation, messaging, waits, follow-up work and targeted interruption.
- Disturbance / variety regulated: queued/running/settled child work, blocked dependencies, stale plans, child failure, need for new guidance, and active turns that should be stopped/reused.
- Decisive decision or feedback right: inspect the descendant tree, wait on any/all selected children, send guidance, launch follow-up work into an existing child session, interrupt one active child turn, and re-plan the live portfolio of delegated commitments.
- Decision owner: the parent/root model-backed agent.
- Supporting / enforcement mechanisms: `list_agents`, `wait_agent`, `send_message`, `followup_task`, `interrupt_agent`, durable child/session status, root concurrency/depth budgets, recovery/checkpoint machinery.
- Closure path: parent reads current descendant-tree/status/message/result evidence → chooses current intervention (wait/message/follow-up/interrupt/new spawn/re-plan) → runtime applies it → updated state/result/message returns → parent makes the next control decision.
- Boundary reachability: collaboration management tools are first-party and model-callable in the bundled subagent mode; asynchronous child sessions remain addressable by stable ids across turns/follow-ups.
- Why this is / is not agent-owned: runtime state/cancellation transport expose and enforce controls, but the parent model interprets whole-current evidence and chooses the substantive intervention.
- Whole-system current view: `list_agents` returns a read-only snapshot of the caller's descendant agent tree; wait/list results include child lifecycle state and messages/results while the parent also holds its own task/session context.
- Current-control decision scope: launch versus wait, dependency barriers/races, targeted message/guidance, reuse through follow-up turns, targeted interruption, and re-planning of active delegated commitments.
- Evidence: [tool.rs](https://github.com/CCherry07/pi-rs/blob/efb6925e248ea801448fd09e60623d109852d3c9/plugins/features/pi-plugin-subagents/src/tool.rs); [runtime.rs](https://github.com/CCherry07/pi-rs/blob/efb6925e248ea801448fd09e60623d109852d3c9/plugins/features/pi-plugin-subagents/src/runtime.rs); [lib.rs parent guidance](https://github.com/CCherry07/pi-rs/blob/efb6925e248ea801448fd09e60623d109852d3c9/plugins/features/pi-plugin-subagents/src/lib.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: hard concurrency/depth/spawn budgets are enforcement rather than the S3 owner.

## S3* — Complementary audit

- State: A
- Function: independently review coding/diff/plan/PR claims through a dedicated restricted child role and return a merge/acceptance judgment to the parent.
- Disturbance / variety regulated: implementation defects, scope drift, unsupported assumptions, missing edge cases, inconsistency with requirements, and false confidence in the author's own account.
- Decisive decision or feedback right: inspect the named review target with direct repository evidence and emit an evidence-backed `BLOCK`, `OK`, or `OK with notes` judgment.
- Decision owner: the separate model-backed `reviewer` child agent.
- Supporting / enforcement mechanisms: reviewer-specific system prompt, read/grep/find/ls-only toolset, no nested subagents, no inherited skills, isolated child session, automatic bounded-report rejoin to parent.
- Claim being audited: the focal implementation/plan/diff/PR claim that work is correct, appropriately bounded and acceptable.
- Ordinary reporting path: the implementing/root agent's own coding/tool evidence and completion narrative.
- Complementary access path: reviewer directly reads/searches the repository target under its own restricted role and must ground findings in code/tests/docs/requirements rather than trusting the parent's summary.
- Independence boundary: distinct child session/model context, reviewer-specific prompt, no write or shell tools, no nested subagents/skills, and explicit evidence-backed verdict format.
- Who acts on findings: the parent/root agent receives the normal child report, retains final acceptance/orchestration authority, and can launch corrective/follow-up implementation before accepting completion.
- Closure path: parent has implementation/claim → spawns reviewer → reviewer independently inspects direct evidence → verdict/finding automatically rejoins parent context → parent accepts, repairs or launches follow-up work.
- Boundary reachability: `reviewer` is a built-in profile in the bundled subagent plugin and can be selected by the model-callable `spawn_agent` path.
- Why this is / is not agent-owned: the audit judgment comes from a separate constrained model context with direct evidence access; deterministic role/tool restriction and result transport support rather than replace that judgment.
- Evidence: [reviewer.md](https://github.com/CCherry07/pi-rs/blob/efb6925e248ea801448fd09e60623d109852d3c9/plugins/features/pi-plugin-subagents/agents/reviewer.md); [profiles.rs](https://github.com/CCherry07/pi-rs/blob/efb6925e248ea801448fd09e60623d109852d3c9/plugins/features/pi-plugin-subagents/src/profiles.rs); [tool.rs](https://github.com/CCherry07/pi-rs/blob/efb6925e248ea801448fd09e60623d109852d3c9/plugins/features/pi-plugin-subagents/src/tool.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: reviewer use is a supported reachable mode rather than an unconditional gate on every coding turn.

## S4 — Outside-and-then intelligence

- State: A
- Function: convert evidence from completed user/task experience into model-selected reusable future capability and maintain that capability under bounded ownership/provenance rules.
- Disturbance / variety regulated: user preferences/workflow corrections, newly verified techniques, stale or incomplete reusable procedures, overlapping managed skills, and future recurrence of task classes that would otherwise repeat avoidable discovery/error.
- External distinction: the background review examines completed foreground conversation/tool experience and durable user/task signals as evidence distinct from the current session's frozen skill/memory capability state.
- Future / prospective distinction: the skill-review policy explicitly asks what a future session would benefit from, requires class-level reusable procedures rather than one-off task narratives, and rejects unresolved failures as future guidance.
- Adaptation option generated: patch a currently loaded managed skill, extend an existing umbrella, add reusable references/templates/scripts, create a new class-level skill when no umbrella fits, or (under Curator safeguards) consolidate/archive redundant agent-managed skills.
- Decisive decision or feedback right: the background review model chooses whether supported learning warrants no-op, update, creation, or bounded consolidation and selects the content/procedure to persist for future reuse.
- Decision owner: the model-backed Hermes background review / Curator review agent within its bounded managed-skill scope.
- A witness mode: the default Hermes provider has `review_enabled: true`; eligible user sessions periodically mark memory/skill review due, and after a final response the plugin can run a fresh background review with `skill_view`/`skills_list`/`skill_manage` under review-private read-before-write observations. Agent-created managed skills become reusable Pi-native skills after catalog/resource reload.
- Supporting / enforcement mechanisms: review cadence counters, fresh review-run state, ownership/pin/content-hash/provenance checks, current-review read-before-write guard, trusted-project scope, archives/backups, Curator due/idle gate, session/resource reload.
- Closure path: completed user/task experience → fresh background model review distinguishes durable future-relevant learning → model selects/edits/creates bounded agent-managed skill capability → guarded write persists it → later resource/skill catalog reload exposes the adapted procedure to subsequent pi-rs operation.
- Boundary reachability: Hermes is the built-in default memory provider and background review is enabled by default; the code registers the memory/skill tools and triggers review only for user-origin sessions under explicit cadence/final-response gates.
- Why this is / is not agent-owned: persistence and cadence are deterministic support, but the substantive future-relevance judgment, adaptation option and skill content are model-generated. Removing the review model leaves storage/guards but not materially the same adaptation decision.
- Evidence: [config.rs](https://github.com/CCherry07/pi-rs/blob/efb6925e248ea801448fd09e60623d109852d3c9/plugins/features/pi-plugin-memory-hermes/src/config.rs); [lib.rs](https://github.com/CCherry07/pi-rs/blob/efb6925e248ea801448fd09e60623d109852d3c9/plugins/features/pi-plugin-memory-hermes/src/lib.rs); [skill_review.md](https://github.com/CCherry07/pi-rs/blob/efb6925e248ea801448fd09e60623d109852d3c9/plugins/features/pi-plugin-memory-hermes/src/prompts/skill_review.md); [skill_review.rs](https://github.com/CCherry07/pi-rs/blob/efb6925e248ea801448fd09e60623d109852d3c9/plugins/features/pi-plugin-memory-hermes/src/skill_review.rs); [curator/runtime.rs](https://github.com/CCherry07/pi-rs/blob/efb6925e248ea801448fd09e60623d109852d3c9/plugins/features/pi-plugin-memory-hermes/src/curator/runtime.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: ordinary MEMORY.md persistence alone would not establish S4; the positive claim relies on the separate model-backed future-reuse skill adaptation loop. Curator consolidation is optional, but the default-enabled background review already provides the A witness.

## S5 — Policy and identity

- State: —
- Function: no runtime first-party identity/ultimate-policy governance loop is established at the assessed recursion.
- Disturbance / variety regulated: not established as S5.
- Decisive decision or feedback right: no model-backed authority to redefine pi-rs's ultimate identity, purpose, or governing principles is established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: project trust, system prompts, plugin/resource generations, permission/OS boundaries, provider/model settings, pinned/user-owned skill protections.
- Closure path: not applicable.
- Boundary reachability: no positive S5 path claimed.
- Why this is / is not agent-owned: project trust and protected-resource rules are strong governance/enforcement boundaries, but ultimate authority remains with user/developer configuration; the operating agents cannot authoritatively redefine those identity/policy boundaries.
- Evidence: [README project trust and resource sections](https://github.com/CCherry07/pi-rs/blob/efb6925e248ea801448fd09e60623d109852d3c9/README.md); [Hermes skill ownership safeguards](https://github.com/CCherry07/pi-rs/blob/efb6925e248ea801448fd09e60623d109852d3c9/plugins/features/pi-plugin-memory-hermes/src/skill_review.rs).
- Basis: structural.
- Confidence: high.
- Caveats: configurable policy, trust, protected skills and human authority do not become S5 merely because they constrain lower-level agents.

### Absence scope

- Surfaces inspected: system/resource assembly, project trust, plugin generations, subagent roles/collaboration, Hermes memory/skills/Curator, session lifecycle and user/configuration controls.
- Plausible first-party paths checked: root/parent collaboration authority, reviewer/oracle roles, trust decisions, prompt/resource reload, protected skill policy, memory/Curator adaptation, scheduled prompts.
- Why no material first-party path remains: no model-backed first-party path frames an identity/ultimate-policy issue, exercises legitimate ultimate authority, and returns a binding identity/policy decision that governs subsequent operation.

## Distributed OSS parent arrangement

Public repository governance and maintainership are outside the assessed installed/runtime system. No parent-mode S3/S4/S5 state is inferred from GitHub maintainership, package publication, or the upstream/reference Pi relationship.

## Self-hosted and non-human modes

pi-rs is a self-hosted local product. Operator trust/configuration and OS permissions constrain execution. Those human/operator surfaces do not displace the autonomous witness modes above and do not create a parent-owned S5 mode.

## Recursion

The root session plus its collaboration tree is the assessed recursion. Child sessions are bounded operational units with persistent identity and reusable turns, but no claim is made that every child closes a full viable-system metasystem independently. Nested delegation is supported only where a selected profile allows it and is depth-bounded.

## Variety and escalation

Operational variety is absorbed through direct tools, durable queues/recovery, parallel isolated child sessions, explicit inter-agent messaging/waits, live interruption/follow-up, independent reviewer roles, and persisted future-skill adaptation. Algedonic-style failure/blocker signals can return through child results/messages and reviewer verdicts to the parent, which can interrupt, re-plan or launch corrective work.

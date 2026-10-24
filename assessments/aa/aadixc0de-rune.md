---
harness_id: aadixc0de-rune
project_name: Rune
repository: https://github.com/AadiXC0DE/Rune
review_ref: 538f8bdb96c926880628c102fdc2cd8c2d473fb1
reviewed_at: 2026-10-23
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: P
---

# Rune (AadiXC0DE)

## Review boundary

- System in focus: self-hosted Rust coding-agent CLI, one-shot runner, ACP adapter, and publicly exported agent/delegation library at one frozen commit.
- Purpose and identity: user-configured, provider-agnostic assistant for local repository tasks and review.
- Relevant environment: local repository/workspace, user configuration and credentials, model endpoint, shell/filesystem and optional client host.
- Standard-distribution boundary: installed `rune` interactive and command modes, embedded crate interfaces when documented as buildable first-party constructors; no assumed external host implementation.
- Credited operating / distribution surfaces: `crates/rune/src/{main,session,ask,auto_review}.rs`, `crates/rune-agent/src/{turn,subagent,subagent_tool}.rs`, `crates/rune-tools/src/update_plan.rs`, `crates/rune-core/src/config.rs`, `crates/rune-context/src/{instructions,prompt}.rs` and public ACP/SDK entry points.
- Adjacent first-party surfaces excluded from ownership: `AUDIT.md`, `NEXT-PHASE.md`, tests/fixtures, unreached `crates/rune/src/subagent.rs` live-child bridge, maintainer contribution and release workflows, hypothetical host plugins and external model-provider judgement.
- First-party operating / deployment modes considered: native interactive CLI, one-shot `ask` / `review`, ACP client-mediated session, embeddable `rune-agent` constructor with caller-supplied delegate.
- Recursion level: one local coding-agent task/session and optional first-party child-agent construction, not the distributed repository-maintainer organization.
- Reviewed revision: `AadiXC0DE/Rune@538f8bdb96c926880628c102fdc2cd8c2d473fb1`.
- Observation date: 2026-10-23 (UTC+03 date).
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Rune is a Rust agent loop with provider adapters, bounded conversation history, workspace-aware read/write/shell tools, an in-session updateable plan, user/project instruction discovery, permission policy and session logs. The native interactive host registers tools and handles queued mid-turn steering. `rune ask` uses one-shot output; `rune review` supplies pending `git diff` to an ordinary model for defect reporting, without becoming a standing operational auditor. An automatic model reviewer of unresolved shell/tool permissions may clear or hold an individual action; this is a policy decision, not independent examination of management claims.

The library exposes `Subagent`, `Registry`, `Delegate` and authority/feedback contracts, including a per-parent child bound and rejection of duplicate named children. However, the actual native CLI `prepare()` registers `Subagent::unsupported(...)`. A separate source file contains a read-only synchronous child `Bridge`/`Runner`, but `main.rs` does not declare/load that module and the CLI does not register its bridge. ACP/SDK interfaces let a host provide a registry; this assessment does not equate an outside host's custom delegate with shipped default child execution. Source-defined library S2 *construction* is therefore distinguished from native operational S2 autonomy.

Persistent configuration is layered with a restrictive list of project-safe keys; provider, permissions and review model are user/profile-owned. `AGENTS.md` and skills are scoped inputs to later prompts, not evidence of a first-party sensing/adaptation owner. No live provider, LLM agent, benchmark or task-completion test was executed for this assessment.

Primary source anchors: [interactive host](https://github.com/AadiXC0DE/Rune/blob/538f8bdb96c926880628c102fdc2cd8c2d473fb1/crates/rune/src/session.rs), [model loop](https://github.com/AadiXC0DE/Rune/blob/538f8bdb96c926880628c102fdc2cd8c2d473fb1/crates/rune-agent/src/turn.rs), [child constructor](https://github.com/AadiXC0DE/Rune/blob/538f8bdb96c926880628c102fdc2cd8c2d473fb1/crates/rune-agent/src/subagent.rs), [host delegation interface](https://github.com/AadiXC0DE/Rune/blob/538f8bdb96c926880628c102fdc2cd8c2d473fb1/crates/rune-agent/src/subagent_tool.rs), [policy settings](https://github.com/AadiXC0DE/Rune/blob/538f8bdb96c926880628c102fdc2cd8c2d473fb1/crates/rune-core/src/config.rs).

## Operational model

In the standard CLI, the single model-directed coding worker chooses tools, reacts to observations and can revise a whole in-session task plan. The human supplies the task and standing permission/provider policy; the tool host enforces bounds. In a *separate embeddable constructor mode*, a developer can compose several model-driven children with first-party per-parent registration, admission and feedback checks, but must supply a live `Delegate` to run and reconcile them. Merely invoking `subagent` in the standard native CLI fails with `Unsupported` rather than starting another S1 unit. These distinctions limit the S2 and S3 claims.

## S1 — Operations

- State: A
- Function: choose and perform bounded repository investigation, editing, shell/verification actions and response revision for a user's current coding task.
- Disturbance / variety regulated: uncertain repository layout, tool failures, unexpected file contents, user steering and incomplete verification.
- Decisive decision or feedback right: the active model selects tool calls, interprets returned results and chooses the next coding step or completion; the user and fixed policy retain higher authority.
- Decision owner: model actor inside the native interactive session or one-shot task.
- Supporting / enforcement mechanisms: `turn::run_turn`, advertised tool registry, workspace context, result/event recording, budget and policy checks.
- Closure path: user request → model-generated tool call → authorized tool result → history/steering feedback → next model action or final response.
- Boundary reachability: `rune` interactive session directly calls `turn::run_turn` with production registry; this does not depend on the dormant child bridge.
- Why this is / is not agent-owned: the model chooses task-level investigation and correction, whereas deterministic sandbox, limits and permission rules only bound those choices.
- Evidence: [turn execution loop](https://github.com/AadiXC0DE/Rune/blob/538f8bdb96c926880628c102fdc2cd8c2d473fb1/crates/rune-agent/src/turn.rs), [native session](https://github.com/AadiXC0DE/Rune/blob/538f8bdb96c926880628c102fdc2cd8c2d473fb1/crates/rune/src/session.rs).
- Basis: direct in-distribution model/tool action-and-feedback closure.
- Confidence: high for code-path structure, untested task effectiveness.
- Caveats: configured model service required at actual runtime; no live LLM performance measurement.

## S2 — Coordination

- State: C
- Function: construct bounded same-parent coordination/admission among separately identified child S1 workers, avoiding duplicate identity and exhaustion of the available child slots.
- Disturbance / variety regulated: overlapping child identities that make feedback ambiguous, multiple attempted child commitments against the same finite parent budget, and stale commands after a child has ended.
- Decisive decision or feedback right: first-party `Registry::create` rejects duplicate active named children and excess children; feedback channels reject closed/full queues and only drain guidance at step boundaries, returning errors to the caller.
- Decision owner: fixed first-party per-parent admission/feedback rule; a host-composed parent model would have to decide how to respond to rejection. No autonomous S2 owner is shipped in the native CLI.
- Supporting / enforcement mechanisms: `ChildKind::Named`, `Registry`, `Feedback::queue`/`drain`, `Subagent::new(Delegate, Authority)`, authority inheritance and revocation checks.
- Closure path: two potential child S1 commitments contend for the same parent name/slot → the library constructor rejects interference and exposes the failure → composed parent can redirect or wait → later eligible child request can proceed. The host must supply the actual child runner and complete decision loop.
- Boundary reachability: the public `rune-agent` `Registry`/`Subagent` types are first-party constructor exports; live child operation requires host composition, while the standard CLI deliberately registers `Unsupported` and is **not** a positive S2 runtime witness.
- Why this is / is not agent-owned: an S2-specific admission relation exists at the constructor level, but its admission decision is deterministic; no shipped autonomous coordinator controls multiple live children.
- Distinct S1 units: separate prospective registered child sessions under one parent, each with its own task brief and child identity after a host supplies `Delegate`.
- Inter-S1 disturbance: two children with an identical addressable name would compete for the same parent messaging target, or excessive parallel child commitments would exceed the parent's declared capacity.
- Attenuating coordination relation: reject duplicate names, enforce per-parent child ceiling, validate feedback queue validity and return explicit failures.
- Feedback into subsequent S1 behaviour: constructor errors and bounded feedback returns let the parent change the next child request or delay it; queued steering is drained at a child boundary when supplied by a host.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: checks are scoped to competing sibling *agent* identities and their shared per-parent execution budget, not a generic message transport alone.
- Evidence: [child registry and feedback](https://github.com/AadiXC0DE/Rune/blob/538f8bdb96c926880628c102fdc2cd8c2d473fb1/crates/rune-agent/src/subagent.rs), [delegate constructor](https://github.com/AadiXC0DE/Rune/blob/538f8bdb96c926880628c102fdc2cd8c2d473fb1/crates/rune-agent/src/subagent_tool.rs), [native `Unsupported` wiring](https://github.com/AadiXC0DE/Rune/blob/538f8bdb96c926880628c102fdc2cd8c2d473fb1/crates/rune/src/session.rs#L747-L768).
- Basis: function-specific constructor, not delivered autonomous CLI coordination.
- Confidence: moderate; precise structural constructor, no live multi-child host proved.
- Caveats: no workspace conflict resolver, scheduling policy or independent sibling agents in the standard CLI; do not upgrade this state to `A` on the strength of uncompiled `Bridge` source.

## S3 — Inside-and-now control

- State: A
- Function: choose and revise the current local task's overall commitments and completion order, conditional on results, within a single running session.
- Disturbance / variety regulated: changing current task scope, diverging steps, unsuccessful verification, available token/step budget and mid-turn user correction.
- Decisive decision or feedback right: model can replace its entire live task plan (`pending`/`in_progress`/`completed`) and choose whether to inspect, patch, verify, retry or return a bounded partial outcome.
- Decision owner: session-level coding model; user can steer individual decisions but the positive claim does not rely on a separate autonomous child hierarchy.
- Supporting / enforcement mechanisms: `update_plan` whole-snapshot, per-turn history/steering, one-active-step consistency check, visible state events and deterministic limits.
- Closure path: task goal and current plan → model observes operational results or queued guidance → revises overall near-term plan and work priority → calls ensuing tools or returns to user.
- Boundary reachability: `update_plan` is supplied in the native tools inventory and `turn::run_turn` handles resulting plan events in ordinary sessions; no external controller is needed.
- Why this is / is not agent-owned: selecting and revising current work priorities is model discretion; enforcing the maximum number of plan steps or the context budget is not itself S3 ownership.
- Whole-system current view: within the deliberately narrow one-task recursion, the model sees task history, one live plan snapshot and returned tool outcomes, not a fleet-wide multi-agent portfolio.
- Current-control decision scope: order/replace all current task commitments, move a different step to active status, reconsider remaining work on failure and decide completion/reporting of the local coding task.
- Evidence: [bounded plan replacement](https://github.com/AadiXC0DE/Rune/blob/538f8bdb96c926880628c102fdc2cd8c2d473fb1/crates/rune-tools/src/update_plan.rs), [turn history and steering](https://github.com/AadiXC0DE/Rune/blob/538f8bdb96c926880628c102fdc2cd8c2d473fb1/crates/rune-agent/src/turn.rs), [native tool preparation](https://github.com/AadiXC0DE/Rune/blob/538f8bdb96c926880628c102fdc2cd8c2d473fb1/crates/rune/src/session.rs).
- Basis: local-current control over the entire bounded task, not organization-wide resource allocation.
- Confidence: moderate; model option present, actual fidelity not run.
- Caveats: the review finds no active native child portfolio and does not credit speculative parent-wide coordination or an independent parent-mode S3 controller from mere CLI stop/steer.

## S3* — Complementary audit

- State: —
- Function: independently challenge the S3 controller's account of live current-task management using a separate evidentiary route, then return management correction.
- Disturbance / variety regulated: erroneous priority/commitment accounting or uncorrected S3 narrative; no such closed complementary audit is established.
- Decisive decision or feedback right: absent. `rune review` takes a provided pending diff and invokes ordinary `ask`; automatic review decides whether an unresolved tool action is safe, not whether S3 is reporting management reality faithfully.
- Decision owner: no in-boundary complementary S3 audit owner identified.
- Supporting / enforcement mechanisms: diff capture, per-action model review/hold, ordinary user-visible session log.
- Closure path: neither diff feedback nor per-action permission review is an independent S3 claim → direct evidence → corrective control path.
- Why this is / is not agent-owned: a second review model is not S3* simply because it exists; the audited claim and corrective loop are about another function.
- Evidence: [one-shot diff review](https://github.com/AadiXC0DE/Rune/blob/538f8bdb96c926880628c102fdc2cd8c2d473fb1/crates/rune/src/main.rs#L280-L346), [action reviewer](https://github.com/AadiXC0DE/Rune/blob/538f8bdb96c926880628c102fdc2cd8c2d473fb1/crates/rune/src/auto_review.rs), [permission routing](https://github.com/AadiXC0DE/Rune/blob/538f8bdb96c926880628c102fdc2cd8c2d473fb1/crates/rune/src/session.rs#L125-L177).
- Basis: bounded negative at the declared local-task management recursion.
- Confidence: high for two checked reviewer paths.
- Caveats: external ACP clients may independently audit S3, but those client arrangements are not shipped Rune ownership.

### Absence scope

- Surfaces inspected: native review command and diff collector, automatic unresolved-action review, agent turn, current plan/events and ACP client permission hooks.
- Plausible first-party paths checked: second model reviewer, user-invoked `rune review`, session transcript, child read-only reviewer role and ACP permission client.
- Why no material first-party path remains: none reaches an independently sourced assessment of the current S3 controller's commitments and feeds such findings into its control decisions; test-only reviewer roles and dormant child bridge are excluded.

## S4 — Outside-and-then intelligence

- State: —
- Function: learn from outside/future distinctions and decide changes to reusable future task capability.
- Disturbance / variety regulated: new project/tool environments, evolving methods or recurrent skill failures; no first-party prospective adaptation closure found.
- Decisive decision or feedback right: not established; static skills and layered instruction files are loaded, not autonomously revised from external research or operational outcomes.
- Decision owner: no credited S4 owner; human maintainers can edit project/user instructions outside the assessed running harness.
- Supporting / enforcement mechanisms: `AGENTS.md` scope chain, skills catalog, prompt assembly and persisted logs/commands.
- Closure path: prompt/context injection affects a present run; it is not a demonstrated future-option generation and return path.
- Why this is / is not agent-owned: current context search, task re-planning and manually edited files do not alone imply outside-and-then intelligence.
- Evidence: [instructions discovery](https://github.com/AadiXC0DE/Rune/blob/538f8bdb96c926880628c102fdc2cd8c2d473fb1/crates/rune-context/src/instructions.rs), [prompt assembly](https://github.com/AadiXC0DE/Rune/blob/538f8bdb96c926880628c102fdc2cd8c2d473fb1/crates/rune-context/src/prompt.rs), [configuration](https://github.com/AadiXC0DE/Rune/blob/538f8bdb96c926880628c102fdc2cd8c2d473fb1/crates/rune-core/src/config.rs).
- Basis: bounded negative for first-party future adaptation.
- Confidence: moderate-high.
- Caveats: maintainers' `NEXT-PHASE.md` is a roadmap, not an adaptive operating function.

### Absence scope

- Surfaces inspected: project/user instruction loader, context prompt, skills/tools, sessions, repository roadmap and CLI/SDK action routes.
- Plausible first-party paths checked: durable memory/pins, skill reloads, model/provider choice, planning tool, manual config editing and maintainer audit documents.
- Why no material first-party path remains: these carry existing instructions or local task state, but no supported component senses outside/future needs, proposes durable capability alternatives and owns/adopts their return to subsequent tasks.

## S5 — Policy and identity

- State: P
- Function: set the standing owner-approved normative boundary for the local assistant's identity, provider, permissions and allowed repository operations.
- Disturbance / variety regulated: attempts by untrusted repository configuration or a model action to override the user's provider/permission identity, authorization and tool-safety policy.
- Decisive decision or feedback right: user selects profile-owned provider, permission mode, rule settings and secrets; the project `.rune.toml` cannot override these keys; operator CLI/environment overrides remain explicit outside-model controls.
- Decision owner: legitimate local human/host operator (`P`), not the task model or untrusted repository contributor.
- Supporting / enforcement mechanisms: five-layer config resolver with project-safe whitelist, `PermissionMode`, rule/approval routing, runtime tool-call gate and inherited child authority caps.
- Closure path: operator configures durable user policy → project-owned unsafe keys are ignored with diagnostics → running host resolves and enforces effective policy on attempted actions → subsequent work stays under that operator boundary.
- Boundary reachability: the native `rune` entry loads these settings before interactive or `ask` execution and applies permission mode during live tool-call decisions.
- Why this is / is not agent-owned: setting ultimate provider/permission identity belongs to the local operator; model/automatic reviewer judges an individual unresolved action within this standing policy and cannot rewrite its authority.
- Identity / ultimate-policy issue: whose standing safety, provider and authorization configuration may govern later local assistant sessions, including when repository contents disagree.
- Ultimate authority in each claimed mode: user/host operator (`P`) alone; no agent-owned ultimate identity mode established.
- Return-to-operation path: resolved `Settings` selects provider, working mode and permission decision path for later agent tool calls.
- Evidence: [config separation and precedence](https://github.com/AadiXC0DE/Rune/blob/538f8bdb96c926880628c102fdc2cd8c2d473fb1/crates/rune-core/src/config.rs#L1-L15), [project key restriction](https://github.com/AadiXC0DE/Rune/blob/538f8bdb96c926880628c102fdc2cd8c2d473fb1/crates/rune-core/src/config.rs#L660-L692), [native run settings](https://github.com/AadiXC0DE/Rune/blob/538f8bdb96c926880628c102fdc2cd8c2d473fb1/crates/rune/src/main.rs#L110-L175), [policy gate](https://github.com/AadiXC0DE/Rune/blob/538f8bdb96c926880628c102fdc2cd8c2d473fb1/crates/rune/src/session.rs#L125-L177).
- Basis: standing identity/ultimate-policy authority returning to real operation, not a per-call permission prompt alone.
- Confidence: moderate-high.
- Caveats: this is a local installation's policy recursion; neither OSS contributors nor model provider are a single distributed S5 parent for all installations.

## Distributed OSS parent arrangement

GitHub maintainers publish the binary and repository roadmap, but private operator sessions do not report to a centralized organizational S3/S4/S5. The positive S5 claim is confined to the owner of one installation. No inference about contributor governance is drawn from the presence of maintainer notes, PRs, CI or releases.

## Self-hosted and non-human modes

Configured local operator identity remains authoritative in terminal and one-shot modes; the ACP client can additionally review individual permissions, but an ACP consumer is not automatically an independent S3 auditor or organization parent. Headless script operation does not by itself confer agent-owned ultimate identity. The SDK allows host-provided tools and a `Delegate` constructor, but no specific unseen host is counted as a delivered autonomous coordinator.

## Recursion

Primary recursion is the native one-task work organization. The S1 and bounded S3 claims relate to the model's task-wide plan and feedback; the S2 `C` claim relates to first-party *potential child* admission at the library-constructor recursion, not an assertion that the default CLI actually runs a multi-child organization. `S3*` and `S4` remain absent after checking adjacent paths. `S5=P` is operator policy at the parent recursion, not ordinary in-task approvals.

## Variety and escalation

The task model absorbs coding variety by choosing tools, inspecting results and replacing the current plan. Fixed limits and permission rules attenuate failure and authority variety; per-parent child identity and admission constructors attenuate prospective inter-child routing/capacity conflicts. Unauthorized tool actions are denied, held for narrow automatic safety review or surfaced to the human/client. Escalation does not transform the safety reviewer into an S3* audit or create S4 learning.

## Evidence gaps

- No live LLM agent or provider test: autonomy describes source-observable decision rights and closure, not empirically measured success rates.
- The native `Subagent::unsupported` wiring prevents a delivered CLI S2 autonomous claim; the unreferenced read-only bridge cannot supply it. `S2=C` is confined to exported function-specific registration/admission construction, conditional on host composition.
- No independent corrective audit of S3 current-control claims or first-party outside-and-then strategy loop was found in assessed runtime modes.
- The session-level S3 scope is deliberately narrow: one task plan, not simultaneous child agents or an enterprise operations portfolio.
- `AadiXC0DE/Rune` is distinct from another Index project using the short `rune` name; this row uses the owner-qualified canonical id `aadixc0de-rune` and must not overwrite that existing assessment.

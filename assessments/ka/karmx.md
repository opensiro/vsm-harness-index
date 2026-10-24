---
harness_id: karmx
project_name: karmX
repository: https://github.com/KarmSakha/karmx-agent
review_ref: 34a1f940e185db7dbfedba87be8206705e79b89d
reviewed_at: 2026-10-23
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-23
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# karmX

## Review boundary

- System in focus: shipped karmX AI coding harness in `KarmSakha/karmx-agent@34a1f940e185db7dbfedba87be8206705e79b89d`, centered on the Rust CLI agent, its built-in platform extensions and supported opt-in session orchestrator mode.
- Purpose and identity: model-directed repository development using files, shell, model-selected tools and optional browser/context/sidekick capabilities, with accountable local user oversight.
- Relevant environment: local project files, shell processes, running browser/dev-server pages, configured model endpoints, session registry, human permission choices, concurrent delegated coding sessions and evolving conversation context.
- Standard-distribution boundary: shipped Rust `goose` core/CLI (branded karmX), first-party extension registry, included `summon` delegation and opt-in `orchestrator`; documented local CLI modes and desktop interface as related entry points.
- Credited operating / distribution surfaces: `crates/goose/src/agents/agent.rs`, `crates/goose/src/agents/state_machine/`, `crates/goose/src/agents/platform_extensions/`, `crates/goose/src/agents/local_fusion/`, core session/agent manager and `crates/goose-cli/`.
- Adjacent first-party surfaces excluded from ownership: upstream Goose maintainers' distributed OSS governance, repository development CI/evals and fixtures, sample recipes, vendor binaries, release automation, npm packaging, videos and documentation authoring.
- First-party operating / deployment modes considered: standard karmX CLI with model/tool loop and built-in developer/summon/context engine/browser tools; lead/sidekick delegated mode; opt-in registered `orchestrator` extension with independent top-level agent sessions; legacy/default and feature-gated state-machine agent loops.
- Recursion level: local multi-session agent work organization under one model-directed top-level controlling agent when the shipped optional orchestrator is enabled; ordinary one-session operation analyzed separately.
- Reviewed revision: `34a1f940e185db7dbfedba87be8206705e79b89d` (immutable batch #996 row 6).
- License screen: frozen root `LICENSE` is Apache License Version 2.0 and project `NOTICE` exists; GitHub repository metadata identifies `Apache-2.0`. The project openly describes itself as a fork of Apache-2.0 Goose.
- Observation date: 2026-10-23.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.7`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.7`.

## Repository architecture

karmX declares itself a customized fork of Goose. The first-party agent runtime exposes model-backed file/tool execution and returned observations. Its named additions are enabled native platform extensions: a codebase context engine offering retrieval/reranking and editable prompt enhancement, a live browser preview of rendered DOM/console, Chrome CDP computer control, and a `sidekick` tool layered over existing `delegate` machinery with a separately chosen model/provider. `summon` is enabled by default. Its tool description explicitly warns that async subagents share a filesystem and same-file writing conflicts; the primary agent can be prompted to partition paths, but this is not an enforced cross-agent file ownership/reservation protocol.

`local_fusion` contains an extensive prompt template advertising a persistent companion, but at this frozen revision its templating/rendering function is referenced only by local unit tests; the reachable `sidekick` tool actually converts a brief into a delegate call, normally creates a child session and may run it asynchronously. The marketing claim of a single enduring sidekick across multiple calls is therefore not treated as proved by first-party execution wiring. The default-disabled but registered first-party `orchestrator` extension provides a qualitatively different optional mode: the model can list/view session state across active and idle top-level agents, start new distinct sessions, send work into sessions and interrupt busy ones.

Frozen evidence: [`README.md`](https://github.com/KarmSakha/karmx-agent/blob/34a1f940e185db7dbfedba87be8206705e79b89d/README.md), [`KARMX.md`](https://github.com/KarmSakha/karmx-agent/blob/34a1f940e185db7dbfedba87be8206705e79b89d/KARMX.md), [`agent.rs`](https://github.com/KarmSakha/karmx-agent/blob/34a1f940e185db7dbfedba87be8206705e79b89d/crates/goose/src/agents/agent.rs), [`platform registry`](https://github.com/KarmSakha/karmx-agent/blob/34a1f940e185db7dbfedba87be8206705e79b89d/crates/goose/src/agents/platform_extensions/mod.rs), [`summon.rs`](https://github.com/KarmSakha/karmx-agent/blob/34a1f940e185db7dbfedba87be8206705e79b89d/crates/goose/src/agents/platform_extensions/summon.rs), [`local_fusion/mod.rs`](https://github.com/KarmSakha/karmx-agent/blob/34a1f940e185db7dbfedba87be8206705e79b89d/crates/goose/src/agents/local_fusion/mod.rs), [`orchestrator.rs`](https://github.com/KarmSakha/karmx-agent/blob/34a1f940e185db7dbfedba87be8206705e79b89d/crates/goose/src/agents/platform_extensions/orchestrator.rs).

## Operational model

In ordinary local operation one coding agent chooses tools and reacts to returned file, process, browser and context observations (S1=A). Delegation yields separately model-directed child work units, but the default warning to partition files is not a runtime-guaranteed concrete interference-damping relation with verified multi-agent closure (S2=—). The supported opt-in orchestrator changes the operating boundary: an autonomous agent can inspect current whole-session state and decide to create, message or interrupt other independent top-level S1s, closing current control into their operation (S3=A). Simple lead/sidekick division is not itself the S3 proof. The code neither wires a sufficiently independent complementary audit of operational evidence (S3*) nor an external/future capability adaptation loop (S4) nor identity-level policy closure (S5).

## S1 — Operations

- State: A
- Function: autonomously execute repository-development tasks through a provider/model/tool loop, with optional independently deciding subagent and top-level worker sessions.
- Disturbance / variety regulated: project contents, shell errors, tool denials, web UI state, prompt uncertainty, model feedback and asynchronous work results.
- Decisive decision or feedback right: the LLM chooses which tool calls and arguments to issue and how to adapt after returned observations; separate delegate sessions follow their own model loops.
- Decision owner: model-backed main karmX agent and spawned model-backed delegates/top-level sessions in supported modes.
- Supporting / enforcement mechanisms: provider adapter, tool calls, Rust execution, permission modes, shell/browser/context platform extensions, persistent conversations, compaction and `summon` task metadata.
- Closure path: incoming development request → provider chooses tools/sidekick tasks → runtime executes and returns result or denial → model chooses subsequent code changes, checks or user response.
- Boundary reachability: compiled CLI connects its agent/runtime and enabled platform-extension registry; browser/context and `summon` entries are first-party default-enabled, while orchestrator can additionally create top-level S1s in an explicitly enabled mode.
- Why this is / is not agent-owned: the model selects task-specific repository changes and revises them from tool feedback; deterministic execution and permissions only constrain those choices.
- Evidence: [`agent.rs`](https://github.com/KarmSakha/karmx-agent/blob/34a1f940e185db7dbfedba87be8206705e79b89d/crates/goose/src/agents/agent.rs), [`state_machine/ops_toolcalling.rs`](https://github.com/KarmSakha/karmx-agent/blob/34a1f940e185db7dbfedba87be8206705e79b89d/crates/goose/src/agents/state_machine/ops_toolcalling.rs), [`summon.rs`](https://github.com/KarmSakha/karmx-agent/blob/34a1f940e185db7dbfedba87be8206705e79b89d/crates/goose/src/agents/platform_extensions/summon.rs).
- Basis: explicit operating docs and frozen source; no live LLM run.
- Confidence: high for architecture and reachable decision path.
- Caveats: no model correctness or practical coding quality is inferred from source and deterministic tests.

## S2 — Coordination

- State: —
- Function: distinct model-backed delegates can coexist, but no complete first-party interference-specific coordination loop is evidenced for their concurrent repository writes.
- Disturbance / variety regulated: sidekick/delegates sharing files can edit the same path and conflict; the source explicitly warns this can happen.
- Decisive decision or feedback right: the `delegate` tool advises the main model to partition files, but neither tracks actual file ownership nor mediates overlap or returns a collision-specific coordination response.
- Decision owner: parent model may choose task decomposition in normal S1 work; no independently established S2 ownership closure.
- Supporting / enforcement mechanisms: `delegate`/`sidekick`, `load`, asynchronous task handles, separate model contexts and tool-description advice to avoid same-file work.
- Closure path: child summaries return to the parent for task synthesis, but no first-party inter-S1 conflict detection/negotiation/reservation → decision → adapted sibling operation loop is exposed.
- Why this is / is not agent-owned: the advisory sentence can influence a model, but the checked delegate path neither carries resolved per-child file scopes nor traces conflict-specific feedback that changes other child operations. Top-level orchestrator messaging is generic transport absent a particular interference-regulation use.
- Evidence: [`summon.rs`](https://github.com/KarmSakha/karmx-agent/blob/34a1f940e185db7dbfedba87be8206705e79b89d/crates/goose/src/agents/platform_extensions/summon.rs), [`local_fusion/mod.rs`](https://github.com/KarmSakha/karmx-agent/blob/34a1f940e185db7dbfedba87be8206705e79b89d/crates/goose/src/agents/local_fusion/mod.rs), [`orchestrator.rs`](https://github.com/KarmSakha/karmx-agent/blob/34a1f940e185db7dbfedba87be8206705e79b89d/crates/goose/src/agents/platform_extensions/orchestrator.rs).
- Basis: source explicitly describes the collision risk and advisory-only response.
- Confidence: medium-high.
- Caveats: users can voluntarily partition tasks or use separate worktrees, but no sufficient first-party specific closure is evidenced in this frozen implementation.

### Absence scope

- Surfaces inspected: `summon` delegate/sidekick tool schemas and work-mode text, async tasks and load, local fusion prompts and template wiring, optional orchestrator sessions and messages.
- Plausible first-party paths checked: delegate warning to partition files as coordination, lead/sidekick division as S2, async task handles as inter-S1 regulation, generic cross-session messaging as conflict mitigation.
- Why no material first-party path remains: the source acknowledges collision risk and recommends voluntary file partitioning, but the checked operating path supplies no task-scoped ownership negotiation, recorded conflict resolution or S2-specific return that revises sibling behavior. A deterministic lock would be one possible implementation, not a requirement; the missing witness is a concrete closed coordination relation beyond generic delegation instructions.

## S3 — Inside-and-now control

- State: A
- Function: coordinate current commitments and execution capacity over several independently operating top-level agent sessions in an explicitly enabled first-party orchestrator mode.
- Disturbance / variety regulated: disparate session progress, idle/busy workers, current work commitments, agent capacity and interruption/reassignment needs.
- Whole-system current view: `orchestrator.list_sessions` surfaces session types, status, latest updates and message counts, and `view_session` exposes current conversation evidence or a summary; the session manager spans the local current agent cohort.
- Current-control decision scope: top-level orchestrating model chooses which new session to start, what message/assignment to send to an existing session and when to interrupt a busy one.
- Decisive decision or feedback right: the model sees current agent roster/status and decides interventions over active peer work; not merely an automatic concurrency quota.
- Decision owner: model-backed top-level agent in optional orchestrator-enabled mode.
- Supporting / enforcement mechanisms: session manager, registered `orchestrator` tools, agent manager, start/interrupt permission checks, cancellation tokens, provider/session binding and response delivery.
- Closure path: model inspects current roster/conversation → chooses start/message/interrupt tool → runtime creates or changes running sessions → subsequent operations follow new assignment or cancellation → model can reinspect current state.
- Boundary reachability: `platform_extensions/mod.rs` registers `orchestrator` as a first-party extension even though `default_enabled: false` and `hidden: true`; normal platform extension configuration permits the supported opt-in mode. No external custom orchestrator actor or implementation is required.
- Why this is / is not agent-owned: without the model's discretionary choice about which session to affect, the runtime only lists/enforces requested actions; it cannot select current priorities/commitments on its own. The optional path is genuine autonomous current control, unlike default lead/sidekick delegation by itself.
- Evidence: [`orchestrator.rs`](https://github.com/KarmSakha/karmx-agent/blob/34a1f940e185db7dbfedba87be8206705e79b89d/crates/goose/src/agents/platform_extensions/orchestrator.rs), [`platform_extensions/mod.rs`](https://github.com/KarmSakha/karmx-agent/blob/34a1f940e185db7dbfedba87be8206705e79b89d/crates/goose/src/agents/platform_extensions/mod.rs), [`config/extensions.rs`](https://github.com/KarmSakha/karmx-agent/blob/34a1f940e185db7dbfedba87be8206705e79b89d/crates/goose/src/config/extensions.rs).
- Basis: structural, function-specific top-level cross-session control; the frozen Goose-derived first-party constructor is retained by this fork.
- Confidence: high for advertised first-party optional wiring, with opt-in scope explicitly bounded.
- Caveats: ordinary default CLI operation does not automatically activate this mode; S3=A records supported availability, not usage in every local run.

## S3* — Complementary audit

- State: —
- Function: no established independent complementary audit judgment returns into whole-current control.
- Disturbance / variety regulated: errors or inaccurate delegated coding reports can require review, but a separate first-party audit governance path is not wired.
- Decisive decision or feedback right: lead guidance asks to inspect the sidekick's diff, yet the long `SIDEKICK_PROMPT` audit-like template is not consumed by the operating agent; regular tests and browser previews are direct work verification.
- Decision owner: no distinct independent S3* audit actor established.
- Supporting / enforcement mechanisms: file/diff tools, sidekick report contract, model tool results, user review of artifacts and unit/eval scripts.
- Closure path: sidekick results or browser DOM observations return to the producing/lead S1 decision path; no independent complementary sampler → review finding → S3 corrective return.
- Why this is / is not agent-owned: asking the same lead to read its worker's diff is not an evidentially independent complementary audit circuit, and unmounted template text cannot supply ownership.
- Evidence: [`local_fusion/mod.rs`](https://github.com/KarmSakha/karmx-agent/blob/34a1f940e185db7dbfedba87be8206705e79b89d/crates/goose/src/agents/local_fusion/mod.rs), [`summon.rs`](https://github.com/KarmSakha/karmx-agent/blob/34a1f940e185db7dbfedba87be8206705e79b89d/crates/goose/src/agents/platform_extensions/summon.rs), [`orchestrator.rs`](https://github.com/KarmSakha/karmx-agent/blob/34a1f940e185db7dbfedba87be8206705e79b89d/crates/goose/src/agents/platform_extensions/orchestrator.rs).
- Basis: source-level audit-role and reachable-path inspection.
- Confidence: medium-high.
- Caveats: a separately configured auditor could close this function downstream, but cannot be borrowed into the shipped runtime assessment.

### Absence scope

- Surfaces inspected: local fusion prompts and actual call references, runtime sidekick/delegate, orchestrator view commands, browser preview/console and repository tests.
- Plausible first-party paths checked: lead diff review as independent S3*, sidekick self-checks, orchestrator conversation summary as alternative audit, rendered DOM as separate evidence and CI as operational S3*.
- Why no material first-party path remains: these are producing-path observations or tooling, not an independent specialized complementary reviewer with audit judgment and returned corrective control over a claim.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party forward-looking external environmental model driving durable organizational capability redesign is closed.
- Disturbance / variety regulated: changing code state, browsers and user prompts present current-work uncertainties rather than a monitored future strategic environment.
- Decisive decision or feedback right: the model selects retrieval/enhancement/rerank for the present request, while human config chooses providers and extension use; no future-oriented adaptation option receives organizational approval/return.
- Decision owner: no S4-specific prospective choice owner established.
- Supporting / enforcement mechanisms: context engine's workspace retrieval/relevance ranking, prompt enhancer, browser preview DOM/console, Chrome CDP control, predictive context compaction, user-maintained skills and provider configuration.
- Closure path: context/browser observations can revise the current coding turn; they do not form an outside-and-then scan → adaptation option → changed reusable organizational capability → present-control loop.
- Why this is / is not agent-owned: even model-backed prompt enhancement and browser inspection improve present task execution, not necessarily the future operating identity/capabilities of the harness.
- Evidence: [`context_engine/mod.rs`](https://github.com/KarmSakha/karmx-agent/blob/34a1f940e185db7dbfedba87be8206705e79b89d/crates/goose/src/agents/platform_extensions/context_engine/mod.rs), [`browser_preview/mod.rs`](https://github.com/KarmSakha/karmx-agent/blob/34a1f940e185db7dbfedba87be8206705e79b89d/crates/goose/src/agents/platform_extensions/browser_preview/mod.rs), [`computer_control/mod.rs`](https://github.com/KarmSakha/karmx-agent/blob/34a1f940e185db7dbfedba87be8206705e79b89d/crates/goose/src/agents/platform_extensions/computer_control/mod.rs).
- Basis: bounded built-in capabilities/source and documentation.
- Confidence: high for lack of proven prospective capability closure in inspected modes.
- Caveats: an operator can ask the coding agent to build a new capability, but this remains external task assignment rather than an S4-specific organizational adaptive function.

### Absence scope

- Surfaces inspected: context engine, native browser preview, computer control, predictor/compactor, skill/extension sources, existing orchestrator tool controls.
- Plausible first-party paths checked: retrieval as external sensing, prompt enhancement as strategy, rendered browser state as future scanning, knowledge compaction as learning, user-created extensions as adaptation.
- Why no material first-party path remains: none closes a future-oriented environmental distinction into autonomously chosen durable capability redesign and a return to present S3 capacity.

## S5 — Policy and identity

- State: —
- Function: no legitimate ultimate-policy or organizational identity decision path is established in the operating multi-session agent.
- Disturbance / variety regulated: per-tool safety/permissions and session authority matter, but are tactical task constraints rather than identity-level disputes between S3 current control and S4 adaptation.
- Decisive decision or feedback right: model can issue task/tool requests, permission manager and human operator choose whether particular actions are allowed; code enforces session relation bounds.
- Decision owner: no first-party S5 agent or legitimate parent identity-policy owner with returned organizational closure evidenced.
- Supporting / enforcement mechanisms: GooseMode, permission manager, child role limits, working-directory checks, extension configuration, prompts and maintainers' repository governance.
- Closure path: tool approval or denial returns to the requesting coding turn; no ultimate identity/policy issue → legitimate authority decision → durable governing return loop.
- Why this is / is not agent-owned: model-visible permissions and provider configuration do not grant authority over the system's defining purpose or arbitrate S3/S4 tensions.
- Evidence: [`agent.rs`](https://github.com/KarmSakha/karmx-agent/blob/34a1f940e185db7dbfedba87be8206705e79b89d/crates/goose/src/agents/agent.rs), [`summon.rs`](https://github.com/KarmSakha/karmx-agent/blob/34a1f940e185db7dbfedba87be8206705e79b89d/crates/goose/src/agents/platform_extensions/summon.rs), [`orchestrator.rs`](https://github.com/KarmSakha/karmx-agent/blob/34a1f940e185db7dbfedba87be8206705e79b89d/crates/goose/src/agents/platform_extensions/orchestrator.rs).
- Basis: bounded review of identity, permission and session authority paths.
- Confidence: medium-high.
- Caveats: maintainers may make strategic choices for the OSS project, but their external release organization is excluded from this local runtime boundary.

### Absence scope

- Surfaces inspected: runtime system prompts, permission/mode and extension configuration, orchestrator session authorization, local human approval, OSS governance docs.
- Plausible first-party paths checked: permissions as S5, sidekick identity-concealment instruction as organizational identity, operator model selection as parent S5, orchestrator authority and maintainer release governance as ultimate policy.
- Why no material first-party path remains: the identified decisions alter tool/session execution and product maintenance without an organizational identity/ultimate-policy deliberation and returned governing outcome.

## Distributed OSS parent arrangement

karmX identifies an upstream Apache-2.0 codebase and independent fork additions. Neither the fork's public contributors nor original Goose maintainers operate the assessed local multi-session agent at a shared organizational recursion. First-party runtime ownership derives from shipped executable modules and supported optional configuration, not from repository co-location with external governance.

## Self-hosted and non-human modes

Users may select an OpenAI-compatible/self-hosted provider and independent sidekick model. When a user enables the shipped orchestrator extension, a model-backed top-level actor owns S3 decisions over local sessions; in ordinary single-session operation that mode is inactive. Human tool approval constrains execution, but does not establish S3 parent-control or S5 policy identity.

## Recursion

Distinct top-level sessions initiated through orchestrator have their own runtime, repository task environment and model discretion. The orchestrator regulates their present commitments at the local multi-session recursion; an ordinary sidekick is a delegated child and not automatically an independently viable recursive organization. Separate model choices alone do not make a complete viable system.

## Variety and escalation

Tool results, browser observations and child reports flow into present model decisions; orchestrator session status and interruptions can change the current work capacity/commitments. Neither a stalled child nor a scheduled recipe is by itself an algedonic escalation or S4/S5 evidence.

## Evidence gaps

- This is a first-party frozen code assessment, not a live LLM or Chrome/browser effectiveness experiment. Native `cargo test -p goose --lib` filtered suites were executed at the frozen ref after reproducible toolchain bootstrap: `local_fusion` 11/11 PASS, `orchestrator` 11/11 PASS, `browser_preview` 13/13 PASS and `computer_control` 22/22 PASS. The `context_engine` filter passed 28/29, with `enhance::tests::builds_request_with_prompt_appended` failing its `starts_with("Here is an instruction")` assertion. In total 85/86 targeted deterministic tests passed; this test regression is disclosed, and source/tests do not prove agent judgment quality.
- The local-fusion prompt template and marketing use the term persistent sidekick, but the tested reachable `sidekick` wrapper builds ordinary delegate arguments. No persistent cross-call peer identity is credited without runtime evidence.
- S3=A is conditional on the installed opt-in orchestrator mode and matches its explicitly shipped cross-session control path, not a blanket claim that every karmX user runs multiple agents.

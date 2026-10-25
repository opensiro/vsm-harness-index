---
harness_id: kimchi
project_name: Kimchi
repository: https://github.com/getkimchi/kimchi
review_ref: 65dfefb12a177e60942dc8fde87eeabe02d006af
reviewed_at: 2026-10-25
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Kimchi

## Review boundary

- System in focus: One standard, locally installed Kimchi coding-agent CLI session, especially its shipped default multi-model orchestration, first-party subagent extension and operational plan/build/review/fix cycle. Optional Ferment adds a separate project-run lifecycle; its state machines are considered only where reachable as a first-party extension. The system is **not** the getkimchi company, its service-provider fleet or the upstream pi-mono SDK itself.
- Purpose and identity: Receive a software-development request, choose appropriate work phases, delegate bounded source-changing work to subordinate agents, verify the result through a separate reviewer and return a completed result or remaining problems.
- Relevant environment: Human request and scope, local repository/source/tests/lint, model registry, tool failures, worker budgets, different model capabilities, review findings, persistent project state and service outages.
- Standard-distribution boundary: Kimchi's own `src/cli.ts` extension injection, orchestration directives, first-party multi-model defaults, agent personas, agent spawning/steering/return, plan/review/fix files and optional Ferment lifecycle. Upstream pi-mono supplies the generic model/session/tool loop; model weights and backend router outcomes are externally owned and are **not** counted as autonomous Kimchi subsystems. The shipped code composes operational actors and decides their return path.
- Credited operating / distribution surfaces: [CLI extension registration and pi-mono entry](https://github.com/getkimchi/kimchi/blob/65dfefb12a177e60942dc8fde87eeabe02d006af/src/cli.ts#L890-L970), [default multi-model selection](https://github.com/getkimchi/kimchi/blob/65dfefb12a177e60942dc8fde87eeabe02d006af/src/extensions/multi-model.ts#L19-L85), [role defaults](https://github.com/getkimchi/kimchi/blob/65dfefb12a177e60942dc8fde87eeabe02d006af/src/extensions/orchestration/model-roles.ts#L62-L103), [worker manager and agent creation](https://github.com/getkimchi/kimchi/blob/65dfefb12a177e60942dc8fde87eeabe02d006af/src/extensions/agents/manager/agent-manager.ts#L168-L270), [concrete SDK-backed worker sessions](https://github.com/getkimchi/kimchi/blob/65dfefb12a177e60942dc8fde87eeabe02d006af/src/extensions/agents/manager/agent-runner.ts#L540-L585), [workflow and review return directives](https://github.com/getkimchi/kimchi/blob/65dfefb12a177e60942dc8fde87eeabe02d006af/src/extensions/orchestration/orchestration-instructions.ts#L60-L158).
- Scope restriction: This is a pinned source-reachability assessment, not a live run or a performance/security certification. Source prompt instructions are weaker than unbypassable enforcement; optional or human-switched single-model mode narrows the observed configuration. Current source-code defaults are preferred to possibly stale README model names or broad marketing claims.
- Adjacent first-party surfaces excluded from ownership: Installer/login flows, hosted Kimchi metadata and model-serving policy, updater/release scripts, benchmark task packs, contributor AGENTS/issue policy, optional skills fetched from resources, SDK-internal generic model/tool loop, and backend `auto` model selection are not treated as distinct autonomous organizational S-functions. Local Ferment verification gates are credited as support only where they return current-job evidence, not as independent autonomous higher-level intelligence.

## Organizational functions and decision ownership

Operational Builder, Fixer, Explorer and Researcher are model-backed worker sessions assembled by Kimchi's first-party `AgentManager`, with personas, differentiated tools and return records. The top-level model-backed orchestrator owns work-phase and rework priorities for one **current** coding request. A distinct Reviewer runs with separate context and direct source/test access, and returns a recorded finding before further current work. The parent user can change task scope, select modes/models and set policy restrictions, but those interfaces do not themselves decide the ultimate identity of the coding organization.

## S1 — Operations

- State: A
- Function: Produce a code change, tests, analysis or research artifact for a bounded project task using model-directed tools.
- Disturbance / variety regulated: Unfamiliar source, implementation alternatives, failing tests/builds, file content, context limits and differing task requests.
- Decisive decision or feedback right: The Builder chooses the actual implementation and tests, the Fixer chooses repairs from findings, and Explorer/Researcher choose task-relevant observations; their executed tools affect returned artifacts.
- Decision owner: Model-backed first-party Kimchi worker personas invoked by `AgentManager` and independent `createAgentSession` calls. External model inference/SDK generic loop is dependency, not credited as a separate Kimchi governance actor.
- Supporting / enforcement mechanisms: Model-role routing, shared workspace, tool allowlists, worker turns/tokens/time budgets, background concurrency limits, session files, provider runtime and result transport.
- Closure path: Parent task/spec → first-party `Agent` tool → Kimchi manager creates a configured worker session → model chooses read/write/bash actions → source/tests/report or blocked result returns to parent.
- Boundary reachability: Enabled first-party `extensions.agents` and orchestration prompt are included in the regular CLI; multi-model has a hardcoded true global default. The actor path does not require a custom application to instantiate the extension or a separate developer-implemented worker.
- Why this is / is not agent-owned: Removing the worker's model-mediated decisions leaves tool execution, limits and session transport, but no owner that chooses the code to write or the corrections to implement. Do not transfer upstream pi-mono's generic agent internals to Kimchi's organizational classification.
- Evidence: [Builder and Fixer personas](https://github.com/getkimchi/kimchi/blob/65dfefb12a177e60942dc8fde87eeabe02d006af/src/extensions/agents/personas/default-agents.ts#L205-L346); [manager spawn](https://github.com/getkimchi/kimchi/blob/65dfefb12a177e60942dc8fde87eeabe02d006af/src/extensions/agents/manager/agent-manager.ts#L194-L270); [worker session construction](https://github.com/getkimchi/kimchi/blob/65dfefb12a177e60942dc8fde87eeabe02d006af/src/extensions/agents/manager/agent-runner.ts#L545-L565).
- Basis: Positive pinned first-party path.
- Confidence: High for shipped autonomy wiring, not generated artifact quality.
- Caveats: Single-model can run pi-mono directly with no autonomous role decomposition; the standard distribution's default multi-model mode supplies the cited positive S1 path.

## S2 — Coordination

- State: —
- Function: Would attenuate an evidenced interference or oscillation between distinct operational Builder/Fixer/other S1 units without merely commanding task phases.
- Disturbance / variety regulated: Possible concurrent edits to shared files, incompatible worker assumptions, cross-worker dependency conflicts or duplicate remediation; a qualifying first-party disturbance-specific response was not established.
- Decisive decision or feedback right: No demonstrated S2-specific discretionary right distinct from the top-level orchestrator's current work assignment/review acceptance or deterministic Ferment sequence guards.
- Decision owner: Not established for S2 at the reviewed boundary.
- Supporting / enforcement mechanisms: AgentManager's background concurrency cap/queue, GroupJoin, planner-defined chunk order, Ferment's parallel-cohort/FSM gates and prompt instructions not to work on an agent's assigned step concurrently.
- Closure path: No evidenced cross-S1 conflict → specific coordination decision → changed subsequent S1 behavior loop. Review verdict → Fixer is a current quality-control/audit correction path, not proof of autonomous mediation between colliding operational S1 units.
- Boundary reachability: The coordination primitives are shipped and callable; a material S2 conflict mediator is not shown in their active call path.
- Why this is / is not agent-owned: The orchestrator may schedule tasks and interpret reviews, but generic schedule/delegation does not establish the narrower organizational S2 function. Deterministic prevention of illegal simultaneous Ferment steps is support, not discretionary inter-unit conflict ownership.
- Evidence: [concurrency queue](https://github.com/getkimchi/kimchi/blob/65dfefb12a177e60942dc8fde87eeabe02d006af/src/extensions/agents/manager/agent-manager.ts#L160-L266); [Ferment next-action sequencer](https://github.com/getkimchi/kimchi/blob/65dfefb12a177e60942dc8fde87eeabe02d006af/src/ferment/engine.ts#L75-L162); [phase sequencing instructions](https://github.com/getkimchi/kimchi/blob/65dfefb12a177e60942dc8fde87eeabe02d006af/src/extensions/orchestration/orchestration-instructions.ts#L73-L95).
- Basis: Bounded negative, not a claim that multi-agent worker collisions cannot arise.
- Confidence: Medium-high.
- Caveats: A particular deployment may implement S2 via extra custom agents, external git/worktree coordination or operator conduct; those are not credited to this standard first-party boundary without a concrete closure.

### Absence scope

- Surfaces inspected: Multi-model configuration/role assignment, orchestrator phase prompts, manager spawn/queue/group joins, Ferment parallel cohort/failed-step states, review-to-Fixer procedure and worker context/steering.
- Plausible first-party paths checked: Shared workspace edit conflict, overlapping agents, run-order interference, duplicate implementations, reviewer opposition to Builder output, deterministic concurrent-step rejection.
- Why no material first-party path remains: They implement allocation, task sequencing, generic error retry and vertical current-project review/remediation. No source-linked mediation protocol was found that identifies a **specific inter-S1 conflict** and selects a coordination settlement which changes those units' subsequent interaction.

## S3 — Inside-and-now control

- State: A
- Function: Control one current coding-job's global phase selection, budgets/role commitments, correction priority and final completeness after worker and reviewer feedback.
- Disturbance / variety regulated: Simple versus complex requests, failing build chunks, disputed review findings, time/token constraints and incomplete current work.
- Decisive decision or feedback right: The top-level model-backed orchestrator classifies the task, chooses explore/research/plan/build/review phases, allocates work to specified roles/models, decides corrective Fixer calls and stops/reports after bounded verdict cycles.
- Decision owner: Kimchi's current top-level orchestrator model, furnished with Kimchi's operative system-prompt workflow and `Agent` tool; it is not the queue/Ferment FSM itself or a human who selected the initial task.
- Supporting / enforcement mechanisms: First-party phase/guideline prompts, named persona contracts, default roles, timestamps and reports, optional Ferment state, concurrency/token limits, review-verdict files and stop caps.
- Closure path: Current user goal + known workspace/worker state → orchestrator chooses plan and worker responsibilities → Builder/reviewer reports and failures → orchestrator delegates revised Fixer/chunk work or stops with unresolved problems → revised current completion state.
- Boundary reachability: Default multi-model mode injects orchestration/agent extensions into ordinary CLI; a model agent actively selects pipeline and revises present commitments. Ferment additionally supplies project-wide scoped steps/recovery but its deterministic scheduler alone is not counted as owner.
- Why this is / is not agent-owned: Fixed resource caps enforce choices, while the orchestration model decides which parts of current work need reassignment/correction; remove it and only a passive state machine/agent sessions remain.
- Whole-system current view: One installed coding session's user request, files, plan/spec chunks, active/finished subagents, tests and independent review verdict; not the whole getkimchi company or portfolio.
- Current-control decision scope: Current project task phases, which agent/model works which chunk, remediation after findings, bounded retries, completion or transparent halt.
- Evidence: [classification and phase selection](https://github.com/getkimchi/kimchi/blob/65dfefb12a177e60942dc8fde87eeabe02d006af/src/extensions/orchestration/orchestration-instructions.ts#L60-L101); [review remediation/stop policy](https://github.com/getkimchi/kimchi/blob/65dfefb12a177e60942dc8fde87eeabe02d006af/src/extensions/orchestration/orchestration-instructions.ts#L137-L158); [phase role decisions](https://github.com/getkimchi/kimchi/blob/65dfefb12a177e60942dc8fde87eeabe02d006af/src/extensions/orchestration/orchestration-instructions.ts#L290-L389); [Ferment actual step state](https://github.com/getkimchi/kimchi/blob/65dfefb12a177e60942dc8fde87eeabe02d006af/src/ferment/engine.ts#L50-L164).
- Basis: Positive source-evidenced agent-owned current control.
- Confidence: Medium-high; model compliance is not experimentally validated.
- Caveats: Prompt directives can be ignored by a provider model; supported autonomous ownership is structurally reachable, not a measured success rate. Human planning approval remains within a particular operating task, not a proven `(P)` whole-system parent mode.

## S3* — Complementary audit

- State: A
- Function: Obtain a second evidence-reading judgment of the current implementation's source, tests and match to spec, return contradictions to project control without the reviewer making audited source edits.
- Disturbance / variety regulated: Builder self-report errors, latent correctness/security defects, unchecked missing functionality, misleading test success and implementation/spec divergence.
- Decisive decision or feedback right: A separately instantiated Reviewer model examines **actual code**, runs tests/lint, decides `APPROVED` versus `NEEDS_FIXES` with cited problems, and writes a review report; current controller routes its findings to a Fixer.
- Decision owner: The separate Reviewer agent persona and child model session, with a direct read/batch test tool surface independent of the Builder's final summary. The orchestrator subsequently controls fixes; the deterministic parsing of a verdict is not itself independent judgment.
- Supporting / enforcement mechanisms: Read-only-oriented Reviewer persona (read/bash/grep/find/ls plus report write), fresh child context, `.kimchi/docs/review.md`, no direct source edits in the review contract, feedback routing to Fixer, review/fix round caps.
- Closure path: Builder work claims code/test completion → separate Reviewer reads spec and raw source and runs tests/lint → evidence-based findings file → orchestrator reads findings and invokes Fixer → source is corrected or defects are reported to user.
- Boundary reachability: The default coding pipeline directs model-backed review delegation, and the shipped Reviewer has direct source/tool capability. The code permits self-review for *trivial low-risk* changes when the orchestrator is also reviewer; that reduced path is not the independent positive witness.
- Why this is / is not agent-owned: Reviewer chooses the substantive discrepancy judgment from firsthand source/tests, rather than copying Builder output or reporting automatic CI alone. Its duty separation is by fresh agent context and role, not necessarily by distinct model family.
- Claim being audited: Builder's assertions that new code matches spec, tests pass and changes contain no material correctness/security defects.
- Ordinary reporting path: Builder reports artifact paths and its own build/lint/test outcome to orchestrator.
- Complementary access path: Reviewer independently reads changed source and context, can execute checks, and records findings separate from the Builder summary.
- Independence boundary: Distinct child session and Reviewer persona restricted by instructions to source-read/report writing, rather than the Builder's execution context. Shell write prevention is **not** cryptographically enforced merely by prompt; this is behavioral role independence, not a security isolation guarantee.
- Who acts on findings: Top-level orchestrator and separately tasked Fixer, not the reviewer itself.
- Evidence: [Reviewer direct-source contract](https://github.com/getkimchi/kimchi/blob/65dfefb12a177e60942dc8fde87eeabe02d006af/src/extensions/agents/personas/default-agents.ts#L252-L310); [fresh session creation](https://github.com/getkimchi/kimchi/blob/65dfefb12a177e60942dc8fde87eeabe02d006af/src/extensions/agents/manager/agent-runner.ts#L545-L567); [independent review and return to fix](https://github.com/getkimchi/kimchi/blob/65dfefb12a177e60942dc8fde87eeabe02d006af/src/extensions/orchestration/orchestration-instructions.ts#L132-L158); [delegated review conditional](https://github.com/getkimchi/kimchi/blob/65dfefb12a177e60942dc8fde87eeabe02d006af/src/extensions/orchestration/orchestration-instructions.ts#L360-L386).
- Basis: Positive conditional independent source-read audit path in standard multi-model code workflow.
- Confidence: Medium; independence is meaningful for source access but not guaranteed for every trivial task or provider-run behavior.
- Caveats: This does not claim an external institutional auditor, distinct model weights, secure filesystem sandbox or that any sample LLM review actually caught bugs.

## S4 — Outside-and-then intelligence

- State: —
- Function: Would detect outside/future shifts and autonomously revise the coding organization’s future capabilities and resource premises rather than just execute today's task.
- Disturbance / variety regulated: Prospective model ecosystem/library/environment changes and organizational future requirements; no qualifying first-party adaptation loop was established.
- Decisive decision or feedback right: None established for external-prospective capability planning.
- Decision owner: Not established; provider and maintainers change catalogs/models, while Kimchi records selection, memory and project-scope preferences.
- Supporting / enforcement mechanisms: Researcher/web access, memory, `auto` backend routing pick observation, default-model deprecation fallback, local Ferment memories/decisions and skill installation.
- Closure path: Current-job research and saved observations can inform tasks but were not shown to autonomously select a prospective capability strategy and return it to future execution governance.
- Boundary reachability: These are shipped first-party extension paths, yet their positive returns stop at routing, task context or configuration repair.
- Why this is / is not agent-owned: A server-picked concrete model and client-side capability synchronization are not a first-party model agent governing prospective organizational adaptation.
- Evidence: [backend pick observation](https://github.com/getkimchi/kimchi/blob/65dfefb12a177e60942dc8fde87eeabe02d006af/src/extensions/auto-model/index.ts#L230-L272); [dead-model default repair](https://github.com/getkimchi/kimchi/blob/65dfefb12a177e60942dc8fde87eeabe02d006af/src/extensions/auto-model/index.ts#L392-L483); [Ferment scoped memory](https://github.com/getkimchi/kimchi/blob/65dfefb12a177e60942dc8fde87eeabe02d006af/src/ferment/state-machine.ts#L945-L973).
- Basis: Bounded negative.
- Confidence: Medium-high.
- Caveats: Operational task research and provider-side future planning may still exist externally; no ownership transferred into the assessed local harness.

### Absence scope

- Surfaces inspected: Researcher persona, web research instructions, memory storage/capture, model defaults/metadata, backend `auto` pick handling, model fallback/self-heal, Ferment decisions and planning prompts.
- Plausible first-party paths checked: Learned future model selection from outcome feedback, autonomous prospective skill/capability acquisition, environmental scenario tracking, external future risk analysis and returned portfolio changes.
- Why no material first-party path remains: None shows external/future intelligence turning into a chosen change of prospective organizational capability with a binding return into the next active S3 operating configuration; model metadata sync and task memories only support current operation.

## S5 — Policy and identity

- State: —
- Function: Would adjudicate ultimate organizational mission, identity, invariants and conflicting inside/outside priorities with a binding return to operation.
- Disturbance / variety regulated: Foundational identity and policy conflicts; task authorization and model/permissions choices are a narrower variety class.
- Decisive decision or feedback right: No first-party internal or supported parent-mode ultimate identity adjudication and closure evidenced.
- Decision owner: Human user owns local task intents, resources and mode configuration, but that is not a proven S5 responsibility at the organization recursion.
- Supporting / enforcement mechanisms: Intent boundary instructions, tool permissions, project trust, user questionnaire, phase approvals, settings and hard stops.
- Closure path: User constrains or revises a task; no ultimate-policy issue → legitimate authority → binding identity decision → future operating changes loop at the declared organization boundary.
- Boundary reachability: These mechanisms are reachable but constrain local task execution rather than governance of Kimchi's identity/purpose.
- Why this is / is not agent-owned: System-prompt invariants, task approvals and static permission gates do not exercise mission/policy discretion simply because an LLM interprets them.
- Evidence: [task intent boundaries](https://github.com/getkimchi/kimchi/blob/65dfefb12a177e60942dc8fde87eeabe02d006af/src/extensions/orchestration/orchestration-instructions.ts#L73-L91); [user-selected mode](https://github.com/getkimchi/kimchi/blob/65dfefb12a177e60942dc8fde87eeabe02d006af/src/extensions/multi-model.ts#L22-L105); [parent/worker exclusion tools](https://github.com/getkimchi/kimchi/blob/65dfefb12a177e60942dc8fde87eeabe02d006af/src/extensions/agents/manager/agent-runner.ts#L61-L85).
- Basis: Bounded negative.
- Confidence: Medium-high.
- Caveats: Real users or upstream maintainers may exercise S5 organizationally; their separate private governance is outside the reviewed one-session boundary.

### Absence scope

- Surfaces inspected: User approvals, project trust, orchestration intent/stop guidelines, Ferment charter/constraints, multi-model settings and resource/permission policy.
- Plausible first-party paths checked: Mission conflict, local human executive authority, goal-versus-safety tradeoffs, task authorization and automatic redefinition of system identity.
- Why no material first-party path remains: The surfaced gates choose how to perform or authorize a coding task; no evidenced ongoing apex-policy deliberation changes the purpose/identity constraints for subsequent runs.

## Distributed OSS parent arrangement

Separate getkimchi contributors, provider operators, local users and upstream pi-mono maintainers are not a single observable parent control system for one user's Kimchi session. Open-source issue review and CI have no automatic authority over the local runtime's autonomous task controller. No `(P)` S3/S4/S5 mode is inferred from the existence of human contributors or ordinary CLI configuration.

## Self-hosted and non-human modes

The default multi-model mode is selectable and starts enabled according to the pinned first-party setting resolution. Its autonomous orchestrator manages the current work and can call separate operational and auditor agent sessions. Explicit single-model mode disables automatic task classification and delegation; a manually requested subagent remains possible but does not supply the same whole-current S3/S3* witness by itself. Optional Ferment provides an additional structured task/verification/recovery runtime; its state machines do not automatically own the organizational choices they enforce.

## Recursion

The supported positive ownership applies to one current developer job, decomposed into local delegated operations with a higher-level controller and a separated evidence-reading review path. Child agents do not thereby become viable independent organizations with S2–S5; the getkimchi company/remote model infrastructure is not smuggled into the local recursion boundary.

## Variety and escalation

Different code demands and failures are handled by local operational worker reasoning and bounded returns. The controller changes phase/worker assignments in response to reports. Reviewer access to source/test output supplies a complementary challenge to Builder claims and can trigger repair. A reported dead worker or unverified review eventually results in a bounded user-facing stop, not an unbounded self-correcting guarantee. Models, budgets, prompts, locks and permission restrictions support this regulation but are not substitute owners.

## Evidence gaps

- No LLM agent, model-provider, browser, end-to-end coding-quality or adversarial review experiment was run. No claim is made that prompt compliance, code correctness or review reliability has been empirically measured.
- The assignment distinguishes the actual pinned source from mutable current README/default-model names. It does not infer hosted backend intelligence or upstream pi-mono ownership as Kimchi-first-party adaptive S4.
- The S3* positive path is conditional on non-trivial independent review; trivial self-review is a documented exception, and the reviewer role's read-only promise is not a strict filesystem sandbox.

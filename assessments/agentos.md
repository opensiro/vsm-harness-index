---
harness_id: agentos
project_name: AgentOS
repository: https://github.com/framerslab/agentos
review_ref: 1e9921837385b8218774955b699d949c233e52ea
reviewed_at: 2026-09-25
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-25
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: C
autonomy_s3_star: —
autonomy_s4: A
autonomy_s5: P
---

# AgentOS

## Review boundary

- System in focus: one first-party AgentOS runtime/agency organization at pinned revision `1e9921837385b8218774955b699d949c233e52ea`, including the high-level agent/agency runtime, multi-agent strategy compilers, WorkflowEngine current-control surfaces, the full-runtime emergent capability engine, and the SOUL workspace identity loader.
- Purpose and identity: operate model-driven agents and multi-agent teams that can execute user goals, coordinate distinct agent perspectives, regulate whole-runtime commitments through configured controls, extend their executable capability repertoire, and run under durable parent-authored identity and hard-limit definitions.
- Relevant environment: user/operator requests, peer-agent outputs, model-provider responses, tool/API/file results, capability gaps encountered during work, workflow load and aggregate resource usage, and parent-authored identity/policy material in the agent workspace.
- Standard-distribution boundary: the first-party `@framers/agentos` runtime and documented public constructors at the pinned revision. External model providers, external tools/services, channel providers, caller infrastructure, and downstream applications are environmental dependencies and do not donate VSM ownership.
- Credited operating / distribution surfaces: standard model/tool agent execution; `agency()` multi-agent strategies including `debate`; `WorkflowEngine` active-workflow admission/status surfaces and agency-wide resource controls; full-runtime `AgentOS` emergent `forge_tool` path; SOUL workspace loading into structured persona/system context.
- Adjacent first-party surfaces excluded from ownership: repository CI/release workflows; tests and benchmark/evaluation packages as evidence-only unless wired into the operating path; standalone `Evaluator`/LLMJudge library usage not wired into ordinary runtime control; examples as corroboration rather than owners; lightweight `agent()` emergent configuration where the repository explicitly states that `forge_tool` is not activated; generic observability/provenance surfaces where they only report events.
- First-party operating / deployment modes considered: ordinary single-agent model/tool operation; configured multi-agent `agency()` operation; debate-mode mutual adjustment; host-configured workflow/resource-regulation mode; full `AgentOS` runtime with `emergent: true`; SOUL-backed agents whose workspace identity is authored by the parent/operator.
- Recursion level: one AgentOS runtime/agency is the primary system-in-focus. Named roster agents are treated as distinct S1 units only where the evidence establishes separate agent loops contributing different operational perspectives/outcomes inside the same agency; merely spawning or naming a worker is not taken as recursive viability.
- Reviewed revision: `1e9921837385b8218774955b699d949c233e52ea`.
- Observation date: 2026-09-25.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

AgentOS ships both a lightweight high-level agent API and a fuller service runtime. The ordinary operating path gives a model an iterative generation/tool surface and returns tool/environment results into subsequent model decisions. `agency()` places several named agents behind one Agent-compatible interface and compiles one of six first-party orchestration strategies.

The strongest S2 path is not generic routing, graph edges, or shared memory. In the `debate` strategy, multiple agent units intentionally expose conflicting operational positions to one another: each later turn receives the accumulated arguments from peer units and is explicitly required to rebut the strongest opposing claim and add a new point. That changed shared context alters the next S1 response, and a model-driven synthesizer then adjudicates the resulting conflict into one coherent output. The disturbance is therefore structurally evidenced disagreement among distinct S1 contributions, and the attenuation relation closes through autonomous mutual adjustment rather than through mere transport.

Inside-and-now control is more limited. The hierarchical manager chooses delegates and subtasks, but that is task decomposition and is not credited as S3 by itself. Instead, AgentOS exposes first-party whole-runtime control primitives: `WorkflowEngine` tracks the number of active workflows and rejects new commitments when a configured whole-system concurrency ceiling is reached, while agency resource controls evaluate aggregate tokens, duration, agent-call count and cost and can fail runs on configured limits. These are real current-commitment/resource regulation mechanisms, but the decisive limits and response regime are supplied by the host/operator rather than selected by an autonomous S3 actor. They therefore establish a constructor path, not autonomous S3.

The repository contains several reviewers, judges and evaluation surfaces, but no credited S3* path at this boundary. The agency `review-loop` reviewer sees the producer's ordinary draft plus the original task and performs routine in-path QA; it does not obtain materially different access to operational reality. The standalone evaluation framework is not wired as a complementary operating audit with corrective closure. Emergent judges inspect candidate capabilities inside the adaptation pipeline, which is capability-admission QA rather than complementary audit of ordinary S1/S3 claims.

The strongest S4 path is the full-runtime emergent capability engine. With `emergent: true`, an agent that encounters an externally presented task for which its current tool repertoire is insufficient can invoke `forge_tool`, generate or compose a candidate capability, run declared tests, submit it to an LLM judge, and on approval register it for subsequent turns. The first-party tiering path can later promote repeatedly successful capabilities beyond the current session. This is an explicit external capability-gap distinction, development and testing of a prospective adaptation option, and closure back into future operating capability. The lightweight `agent()` helper alone is not credited because the repository explicitly says it accepts emergent configuration without activating the forge path.

S5 remains parent-governed. The SOUL workspace separates identity from ordinary procedures: `SOUL.md` carries personality, values, tone and hard limits, is required for a souled identity, is loaded at boot, and its structured/prose content is injected back into runtime persona/system context. The parent/operator authors that workspace; AgentOS's self-editing memory wiki and bounded personality adaptation do not establish autonomous authority to rewrite the ultimate identity/hard-limit source. Thus the identity decision reaches a legitimate parent and returns into later operation, but no autonomous S5 owner is packaged.

Primary evidence:

- [`README.md`](https://github.com/framerslab/agentos/blob/1e9921837385b8218774955b699d949c233e52ea/README.md) — standard agent/agency surface, multi-agent strategies, runtime tool forging and SOUL identity overview.
- [`src/api/agency.ts`](https://github.com/framerslab/agentos/blob/1e9921837385b8218774955b699d949c233e52ea/src/api/agency.ts) — one-request agency boundary, strategy compilation, aggregate resource controls, validation/retry and HITL wiring.
- [`src/api/runtime/strategies/hierarchical.ts`](https://github.com/framerslab/agentos/blob/1e9921837385b8218774955b699d949c233e52ea/src/api/runtime/strategies/hierarchical.ts) — model-owned delegation decisions and runtime specialist synthesis; used as S1 evidence but not treated as S3 merely because it is called a manager.
- [`src/api/runtime/strategies/debate.ts`](https://github.com/framerslab/agentos/blob/1e9921837385b8218774955b699d949c233e52ea/src/api/runtime/strategies/debate.ts) — explicit inter-agent argumentative conflict, peer-feedback into subsequent rounds and model-driven synthesis.
- [`src/api/runtime/strategies/review-loop.ts`](https://github.com/framerslab/agentos/blob/1e9921837385b8218774955b699d949c233e52ea/src/api/runtime/strategies/review-loop.ts) — routine producer/reviewer QA path considered and rejected as S3* evidence.
- [`src/orchestration/workflows/WorkflowEngine.ts`](https://github.com/framerslab/agentos/blob/1e9921837385b8218774955b699d949c233e52ea/src/orchestration/workflows/WorkflowEngine.ts) — active-workflow count, concurrency admission ceiling, workflow state/progress surfaces and host-set control regime.
- [`docs/architecture/EMERGENT_CAPABILITIES.md`](https://github.com/framerslab/agentos/blob/1e9921837385b8218774955b699d949c233e52ea/docs/architecture/EMERGENT_CAPABILITIES.md) — full-runtime capability-gap → forge/test/judge → session registration → later promotion loop and explicit lightweight-runtime boundary.
- [`src/cognition/emergent/SelfImprovementConfig.ts`](https://github.com/framerslab/agentos/blob/1e9921837385b8218774955b699d949c233e52ea/src/cognition/emergent/SelfImprovementConfig.ts) and [`SelfEvaluateTool.ts`](https://github.com/framerslab/agentos/blob/1e9921837385b8218774955b699d949c233e52ea/src/cognition/emergent/SelfEvaluateTool.ts) — opt-in bounded self-evaluation/parameter adjustment considered but not used alone to establish S4 or S3*.
- [`docs/SOUL_FILES.md`](https://github.com/framerslab/agentos/blob/1e9921837385b8218774955b699d949c233e52ea/docs/SOUL_FILES.md) — parent-authored identity, values and hard limits loaded back into subsequent runtime operation.

## S1 — Operations

- State: A
- Function: execute user/operator objectives through model-driven agent loops that select tools/delegations, consume returned observations and continue toward an operational result.
- Disturbance / variety regulated: request ambiguity, intermediate model/tool results, external API/file/tool evidence, failures, and capability/role differences that change the next useful action.
- Decisive decision or feedback right: choose substantive model responses, tool calls, delegation targets/subtasks and follow-up actions within configured bounds.
- Decision owner: the model-driven AgentOS agent; in hierarchical agency mode the manager model owns the substantive delegation sequence while delegated agents autonomously execute their assigned local work.
- Supporting / enforcement mechanisms: provider adapters, tool execution, bounded step counts, guardrails, schemas, retries, permissions, deterministic strategy plumbing and optional HITL constraints.
- Closure path: request enters AgentOS → model selects response/tool/delegation → first-party runtime executes the selected path → observations/sub-agent outputs return into model context → model chooses subsequent action or completes → result returns to the user/environment.
- Boundary reachability: ordinary `agent`/`agency` operation and hierarchical model-driven delegation are first-party documented runtime paths at the pinned revision.
- Why this is / is not agent-owned: deterministic compilers and execution machinery transport/enforce decisions, but removing the model actor removes the substantive selection of tools, delegated work and response progression; the same decisions are not reproduced by static runtime rules.
- Evidence: [`README.md`](https://github.com/framerslab/agentos/blob/1e9921837385b8218774955b699d949c233e52ea/README.md); [`src/api/runtime/strategies/hierarchical.ts`](https://github.com/framerslab/agentos/blob/1e9921837385b8218774955b699d949c233e52ea/src/api/runtime/strategies/hierarchical.ts).
- Basis: explicit + structural
- Confidence: high
- Caveats: deterministic sequential/graph paths and lightweight helper modes also exist. `A` is based on reachable model-owned operating paths, not on every strategy transition being autonomous.

## S2 — Coordination

- State: A
- Function: attenuate substantive disagreement among distinct agent S1 contributions by making peer positions available for mutual adjustment and converging the resulting conflict into a coherent agency response.
- Disturbance / variety regulated: different operational agents can produce incompatible positions, omit one another's evidence or continue talking past each other, leaving the agency with unresolved contradictory output.
- Decisive decision or feedback right: each debate agent decides how to change its next argument in response to peer claims, and the final synthesizer decides how the competing positions are reconciled into one verdict/output.
- Decision owner: distributed model-driven debate agents plus the model-driven synthesis agent.
- Supporting / enforcement mechanisms: deterministic round sequencing, accumulated transcript construction, per-agent invocation, round caps and final synthesis prompt.
- Closure path: multiple S1 agents produce positions → accumulated peer arguments are injected into later agent turns → agents autonomously rebut/refine in response → changed arguments enter subsequent rounds → synthesizer autonomously resolves the collected conflict into one agency result.
- Boundary reachability: `debate` is a shipped first-party `agency()` strategy; callers select it directly without supplying their own coordination transport or reconciliation implementation.
- Why this is / is not agent-owned: the runtime determines when transcript material is passed, but it does not predetermine how an S1 responds to another S1's claim or which arguments ultimately prevail; those coordination judgments are model-owned.
- Evidence: [`src/api/runtime/strategies/debate.ts`](https://github.com/framerslab/agentos/blob/1e9921837385b8218774955b699d949c233e52ea/src/api/runtime/strategies/debate.ts); [`README.md`](https://github.com/framerslab/agentos/blob/1e9921837385b8218774955b699d949c233e52ea/README.md).
- Basis: explicit + structural
- Confidence: medium-high
- Caveats: generic graph dependencies, sequential routing, shared memory and message buses are not credited as S2. The positive mapping is specifically the debate-mode conflict/mutual-adjustment relation.
- Distinct S1 units: two or more named agency agents with independent model calls/instructions that each produce an operational contribution to the same agency outcome.
- Inter-S1 disturbance: materially conflicting or incomplete positions from different agents can leave the agency's response incoherent or blind to objections; the debate strategy deliberately surfaces this disagreement rather than assuming independent outputs compose safely.
- Attenuating coordination relation: every non-opening debate turn receives the accumulated arguments from prior peer units and is instructed to attack the strongest opposing claim and add a new point; a final model-driven synthesis adjudicates the resulting positions.
- Feedback into subsequent S1 behaviour: peer arguments become input to later S1 model calls, directly changing what those agents consider and how they respond before final synthesis.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the transcript and round scheduler are only supporting channels; credit comes from their explicit use to expose and regulate inter-S1 disagreement through mutual rebuttal and reconciliation.

## S3 — Inside-and-now control

- State: C
- Function: regulate current whole-runtime commitments and aggregate resource exposure through active-workflow admission and agency-level resource limits.
- Disturbance / variety regulated: too many simultaneously active workflows or aggregate agency consumption can exceed configured current capacity/cost/time/call bounds and threaten the ability of the runtime to honor its existing commitments.
- Decisive decision or feedback right: choose/revise whole-runtime concurrency and aggregate resource limits, together with the response policy when those limits are reached.
- Decision owner: no autonomous first-party S3 actor owns those choices. The downstream host/operator supplies the control regime; first-party runtime components measure and enforce it.
- Supporting / enforcement mechanisms: `WorkflowEngine.activeWorkflowCount`, `maxConcurrentWorkflows`, workflow store/progress APIs, agency aggregate usage/call/duration accounting, `checkLimits()` and configured error/warn behavior.
- Closure path: current workflow/agency load is observed → configured whole-system threshold is evaluated → excess new workflow commitment is rejected or a configured agency-limit response is raised → subsequent admitted work is constrained by that regime.
- Boundary reachability: `WorkflowEngine` and agency `controls` are shipped first-party runtime surfaces and are directly configurable by an adopter without replacing the underlying control machinery.
- Why this is / is not agent-owned: the runtime has real whole-system state and enforcement authority, but the organizational choice of concurrency/resource budget and limit-response policy is not made by an autonomous model actor. The function-specific decision path is therefore left for downstream construction, yielding `C`.
- Evidence: [`src/orchestration/workflows/WorkflowEngine.ts`](https://github.com/framerslab/agentos/blob/1e9921837385b8218774955b699d949c233e52ea/src/orchestration/workflows/WorkflowEngine.ts); [`src/api/agency.ts`](https://github.com/framerslab/agentos/blob/1e9921837385b8218774955b699d949c233e52ea/src/api/agency.ts).
- Basis: structural
- Confidence: medium-high
- Caveats: the hierarchical `manager` is not credited as S3 merely because it delegates work. Its documented scope is one-request task accomplishment. Likewise static limits do not become autonomous simply because the runtime enforces them.
- Whole-system current view: active workflow count and workflow/progress state at the full WorkflowEngine level, plus aggregate agency usage, elapsed duration and agent-call counts for the agency-level control surface.
- Current-control decision scope: admission of additional concurrent workflow commitments and aggregate agency resource/limit regime; the decisive policy values remain host-owned.

## S3* — Complementary audit

- State: —
- Function: no material first-party complementary audit path is established for the declared AgentOS operating boundary at the pinned revision.
- Disturbance / variety regulated: not established.
- Decisive decision or feedback right: not established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: `review-loop`, standalone Evaluator/LLMJudge utilities, emergent capability judges, tests, tracing and provenance were inspected but do not close S3* for ordinary operations.
- Closure path: no complementary operating-audit closure established.
- Why this is / is not agent-owned: the review-loop reviewer consumes the producer's ordinary draft plus task and is part of the normal production QA path; standalone evaluator surfaces are not wired into current operational control; emergent judges audit proposed capabilities inside S4 adaptation rather than independently sampling ordinary S1/S3 reality.
- Evidence: [`src/api/runtime/strategies/review-loop.ts`](https://github.com/framerslab/agentos/blob/1e9921837385b8218774955b699d949c233e52ea/src/api/runtime/strategies/review-loop.ts); [`src/safety/evaluation/Evaluator.ts`](https://github.com/framerslab/agentos/blob/1e9921837385b8218774955b699d949c233e52ea/src/safety/evaluation/Evaluator.ts); [`docs/architecture/EMERGENT_CAPABILITIES.md`](https://github.com/framerslab/agentos/blob/1e9921837385b8218774955b699d949c233e52ea/docs/architecture/EMERGENT_CAPABILITIES.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: a downstream application can compose evaluators or external evidence into an audit loop, but that does not donate S3* ownership to this repository-relative assessment.

### Absence scope

- Surfaces inspected: agency review-loop/reviewer path; safety evaluation framework and LLM judge surfaces; emergent creation/reuse/promotion judges; provenance/observability descriptions; tests/examples as corroborating evidence only.
- Plausible first-party paths checked: independent reviewer agent, standalone evaluator, LLM-as-judge, forged-tool judge/promotion panel, tracing/provenance and ordinary validation/retry surfaces.
- Why no material first-party path remains: each inspected path is either routine production QA, adaptation-admission QA, observational infrastructure or a library surface requiring downstream composition; none supplies materially different access to ordinary operational reality plus a first-party corrective return path.

## S4 — Outside-and-then intelligence

- State: A
- Function: detect externally presented capability gaps, develop and test new executable capability options, and return approved adaptations into the agent's future operating repertoire.
- Disturbance / variety regulated: tasks and environmental demands can require a capability absent from the agent's currently registered tools, while candidate generated capabilities may be unsafe, incorrect or unreliable.
- Decisive decision or feedback right: the model agent decides that a capability gap warrants forging and specifies a new capability; model-driven judging participates in deciding whether the candidate is safe/correct enough to enter the repertoire, within deterministic safety/test bounds.
- Decision owner: the model-driven operating agent owns the adaptation proposal; the first-party LLM judge owns the semantic approval judgment for creation/promotion subject to hard runtime constraints.
- Supporting / enforcement mechanisms: `forge_tool`, composable and sandbox builders, declared test cases, schema validation, hardened `node:vm`, EmergentJudge, EmergentToolRegistry, session/agent/shared tiers and deterministic usage/confidence thresholds.
- Closure path: an external task exposes a missing capability → model invokes `forge_tool` and proposes/composes implementation → first-party tests and LLM judge evaluate the option → approved capability is registered at session tier → subsequent turns can invoke it by name → sufficiently proven capabilities can move to a longer-lived agent tier, changing future operating capability.
- Boundary reachability: the repository documents `AgentOS.create({ emergent: true })` as a full-runtime first-party entry point that initializes emergent support and exposes `forge_tool`; the positive claim does not rely on the lightweight `agent()` helper, which explicitly does not activate the path on its own.
- Why this is / is not agent-owned: deterministic sandbox, schemas and thresholds constrain the search space, but they do not decide which missing capability to invent or semantically judge the candidate. Removing the model proposal/judge actors removes those adaptation decisions.
- Evidence: [`docs/architecture/EMERGENT_CAPABILITIES.md`](https://github.com/framerslab/agentos/blob/1e9921837385b8218774955b699d949c233e52ea/docs/architecture/EMERGENT_CAPABILITIES.md); [`src/cognition/emergent/ForgeToolMetaTool.ts`](https://github.com/framerslab/agentos/blob/1e9921837385b8218774955b699d949c233e52ea/src/cognition/emergent/ForgeToolMetaTool.ts); [`src/cognition/emergent/EmergentCapabilityEngine.ts`](https://github.com/framerslab/agentos/blob/1e9921837385b8218774955b699d949c233e52ea/src/cognition/emergent/EmergentCapabilityEngine.ts).
- Basis: explicit + structural
- Confidence: high
- Caveats: emergent capability creation is opt-in rather than default. Opt-in does not negate boundary reachability because the full runtime ships the complete decision/feedback path. Generic memory/self-improvement alone is not used as the S4 witness.
- External distinction: a task/environment presents a required operation for which the current capability catalog has no suitable tool.
- Future / prospective distinction: the runtime does not merely improvise one answer; it creates a named executable capability intended for subsequent turns, tracks reliability and provides a path to longer-lived agent-tier reuse.
- Adaptation option generated: a composed or sandboxed typed tool implementation with schemas and tests, proposed by the model and semantically reviewed before activation.
- Path back into current capability / S3: approved tools enter the first-party EmergentToolRegistry and become callable by name on later turns; promotion can persist a proven capability at agent tier.

## S5 — Policy and identity

- State: P
- Function: establish and preserve agent identity, values, tone and hard behavioral limits through a durable parent-authored SOUL workspace that governs subsequent runtime behavior.
- Disturbance / variety regulated: model/context drift or operational adaptation could otherwise make the agent's enduring identity, values and ultimate behavioral boundaries ambiguous across sessions and changing tasks.
- Decisive decision or feedback right: define or revise the identity-level content of `SOUL.md`, including values and hard limits that bound subsequent operation.
- Decision owner: the legitimate parent/operator who owns the agent workspace; no autonomous first-party actor is given ultimate authority to rewrite the SOUL identity/hard-limit source.
- Supporting / enforcement mechanisms: SOUL workspace convention, YAML-to-`IPersonaDefinition` parsing, `SoulLoader`, system-message injection, structured persona fields and runtime prompt/persona machinery.
- Closure path: identity/policy content is authored or revised by the parent in `SOUL.md` → first-party loader reads it at agent boot → structured identity/hard limits and prose enter runtime persona/system context → subsequent model operation is governed by that parent decision.
- Boundary reachability: SOUL workspaces and `souledAgent()`/`loadSoul` are documented first-party runtime paths, with `SOUL.md` explicitly required for the souled identity mode.
- Why this is / is not agent-owned: AgentOS can autonomously edit its memory wiki and can optionally adapt bounded personality parameters, but those lower-level adaptation paths do not transfer ultimate authority over the durable SOUL identity, values and hard limits away from the parent.
- Evidence: [`docs/SOUL_FILES.md`](https://github.com/framerslab/agentos/blob/1e9921837385b8218774955b699d949c233e52ea/docs/SOUL_FILES.md); [`src/cognition/substrate/personas/SoulLoader.ts`](https://github.com/framerslab/agentos/blob/1e9921837385b8218774955b699d949c233e52ea/src/cognition/substrate/personas/SoulLoader.ts); [`src/cognition/substrate/personas/SOUL.template.md`](https://github.com/framerslab/agentos/blob/1e9921837385b8218774955b699d949c233e52ea/src/cognition/substrate/personas/SOUL.template.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: a generic system prompt alone would not establish S5. Credit is based on the repository's identity-specific SOUL boundary, explicit values/hard-limit semantics and closed load-back path. Bounded runtime personality adaptation is not treated as autonomous ultimate-policy authority.
- Identity / ultimate-policy issue: who the agent is, what values it embodies and which hard behavioral limits remain authoritative across changing tasks/sessions.
- Ultimate authority in each claimed mode: parent-governed mode only — the workspace owner/operator authors the identity source; no autonomous S5 mode is claimed.
- Return-to-operation path: `SOUL.md` is loaded at boot into structured persona fields and the leading system context, which directly governs later agent decisions and responses.

## Summary

AgentOS closes autonomous S1 through its model/tool/delegation loops, autonomous S2 through debate-mode mutual adjustment of conflicting peer-agent positions, and autonomous S4 through full-runtime capability-gap detection and judged runtime tool forging. It exposes constructor-owned whole-system current-control primitives for S3, but routine reviewers/evaluators do not establish an independent S3* path. Durable identity, values and hard limits return through a first-party SOUL workspace whose ultimate authority remains with the parent operator, yielding S5=P.

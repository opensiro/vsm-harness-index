---
harness_id: primusclaw
project_name: PrimusClaw
repository: https://github.com/AMD-AGI/PrimusClaw
review_ref: bbd925a5b12b4ffe425c5ff01f00e9bc93863dfc
reviewed_at: 2026-10-05
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-05
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: C
autonomy_s3_star: —
autonomy_s4: A
autonomy_s5: —
---

# PrimusClaw

## Review boundary

- System in focus: PrimusClaw's first-party Claw harness at frozen revision `bbd925a5b12b4ffe425c5ff01f00e9bc93863dfc`, specifically the shipped API / Brain / Hands composition under `claw/`, its task/DAG scheduler, model/tool agent loop, in-process sub-agents, sandbox/workspace lifecycle, memory/skill services and opt-in skill-evolution mode.
- Purpose and identity: run autonomous coding-agent sessions in isolated per-session workspaces, route model/tool work, schedule current task commitments, and optionally adapt reusable skills from accumulated execution evidence.
- Relevant environment: user prompts and feedback, repository/workspace state, tool and shell outcomes, task/DAG demand, model-provider responses, current fleet capacity, session/event history, persisted skills/memory, SaFE sandbox placement, NATS/PostgreSQL/S3 infrastructure and connected MCP/A2A services.
- Standard-distribution boundary: first-party `claw/packages/api`, `brain`, `hands`, `protocol` and their shipped deployment/configuration surfaces are inside. SaFE, NATS, PostgreSQL, S3-compatible storage, LiteLLM/model providers and the separately licensed bundled `sandbox/` fork are infrastructure/dependencies. Third-party Cursor/Claude/Codex agents cannot donate their internal functions.
- Credited operating / distribution surfaces: normal Claw API→Brain→Hands session execution; Brain model/tool loop and shipped sub-agent task tool; API task/DAG scheduling and fleet-wide admission ceilings; opt-in `CLAW_SKILL_EVOLUTION_ENABLED=true` mode including skill selection, feedback, durable evolution jobs, LLM mutation proposal/verification and active-skill reinjection.
- Adjacent first-party surfaces excluded from ownership: repository-development CI/tests, maintainer/release governance, benchmark/evaluation-only tests, and `claw/docs/agent-team-design.md`, whose own status is draft/pending review and whose team-runtime paths are not present in the frozen tree.
- First-party operating / deployment modes considered: ordinary single-session coding runs, in-process sub-agent delegation, DAG/task execution, configured fleet admission ceilings, and the documented opt-in skill-evolution deployment mode. Draft AgentTeam topology is excluded.
- Recursion level: a coding session/Brain agent loop is an operational S1 unit. DAG task rows may represent several current operational commitments for S3 analysis. Higher-function claims are credited only where shipped runtime paths operate across or adapt those operations.
- Reviewed revision: `bbd925a5b12b4ffe425c5ff01f00e9bc93863dfc`.
- Observation date: 2026-10-05.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Claw is a distributed first-party API / Brain / Hands harness. API persists sessions/events/tasks and publishes work; Brain consumes tasks, runs the model/tool loop, manages sub-agents and sandbox/workspace lifecycle; Hands supplies filesystem/shell/edit tools inside the per-session sandbox. The API task scheduler also observes current DAG/task state and fleet admission usage, promotes dependency-ready work, applies run/sandbox/GPU ceilings, reserves queued work and dispatches accepted rows.

The frozen Brain ships in-process sub-agents with fresh conversations and scoped tool sets, but they share the parent's Hands sandbox/workspace. The draft AgentTeam document describes a future leader/worker team runtime, yet no corresponding shipped team implementation is present at the frozen tree and it is excluded from positive evidence.

A separately shipped opt-in skill-evolution mode records cross-session skill outcomes, detects degraded active skills, retrieves recent successful/problematic trajectories, asks an LLM to propose concrete skill/file mutations, uses a second LLM verifier plus deterministic safety checks as a publication gate, applies accepted mutations transactionally, and makes active/probation skills selectable for later tasks.

## Operational model

For ordinary work, a Brain model actor iterates over LLM responses and first-party/connected tools against an isolated workspace. The `task` tool can create a fresh sub-agent context with a restricted tool profile while retaining the same Hands workspace. API-side task/DAG scheduling is a deterministic current-control plane over queued/running commitments. When skill evolution is enabled, completed runs additionally feed a durable background adaptation loop whose resulting active skill content is selected and injected into subsequent agent prompts.

## S1 — Operations

- State: A
- Function: execute autonomous coding/session work through a model-driven tool feedback loop in a per-session workspace.
- Disturbance / variety regulated: heterogeneous coding goals, repository/filesystem state, command/tool outcomes, model responses, sandbox failures/recovery, context limits, connected MCP/A2A capabilities and user interruptions.
- Decisive decision or feedback right: choose the next reasoning/tool/sub-agent action from current context and returned evidence, revise work after results, and decide when the requested operational outcome is complete.
- Decision owner: the active model-backed Brain agent.
- Supporting / enforcement mechanisms: API session/task dispatch, Brain agent loop, tool router, Hands MCP tools, sandbox/workspace lifecycle, checkpoints, run locks/leases, model routing and deterministic execution/safety gates.
- Closure path: user/task context → Brain agent chooses action/tool/sub-agent → Hands/MCP/runtime returns evidence → evidence returns into the model conversation → subsequent action changes until completion, interruption or bounded failure.
- Boundary reachability: the standard Claw deployment directly instantiates API→Brain→Hands execution; no adjacent development system or third-party coding-agent internals are required for this S1 loop.
- Why this is / is not agent-owned: removing the model actor leaves dispatch, storage, locks and tools but removes the open-ended coding decisions that transform observations into subsequent actions.
- Evidence: README; `claw/packages/brain/src/agent/agent-loop.ts`; `claw/packages/brain/src/agent/sub-agent.ts`; `claw/packages/brain/src/tools/router.ts`; `claw/packages/hands/src/tools/`.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: external model inference and SaFE sandbox placement remain dependencies rather than owners of the coding decisions.

## S2 — Coordination

- State: —
- Function: no distinct first-party S2 relation was established that specifically attenuates an evidenced peer-S1 interference or oscillation.
- Disturbance / variety regulated: shipped in-process sub-agents may run concurrently and share the parent's workspace, while DAG dependencies and queue ordering sequence work; neither path demonstrates peer mutual-adjustment or collision regulation at the assessed recursion.
- Decisive decision or feedback right: no S2-specific decision over a concrete inter-S1 conflict was found.
- Decision owner: not established at S2 level.
- Supporting / enforcement mechanisms: sub-agent tool whitelists/depth limits, shared Hands sandbox, DAG dependency state, queue ordering, task locks and admission ceilings.
- Closure path: delegation and DAG scheduling alter execution order or capacity, but no shipped relation specifically detects/attenuates an inter-S1 disturbance and returns that coordination result into peer behavior.
- Why this is / is not agent-owned: sub-agent delegation, shared state and scheduler sequencing are not S2 without the Profile's specific disturbance/attenuation witness.
- Evidence: `claw/packages/brain/src/agent/sub-agent.ts`; `claw/packages/brain/src/agent/agent-loop.ts`; `claw/packages/api/src/tasks/scheduler.ts`; draft `claw/docs/agent-team-design.md` inspected but excluded.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: the draft AgentTeam design describes future coordination surfaces but is not shipped evidence at this ref.

### Absence scope

- Surfaces inspected: in-process sub-agents, task-tool concurrency, Hands workspace sharing, DAG dependencies, scheduler/admission controls, task locks, A2A surfaces and AgentTeam draft documentation.
- Plausible first-party paths checked: sub-agent parallelism as S2; shared-workspace protection as S2; DAG dependencies as S2; fleet admission ceilings as S2; proposed AgentTeam result/wait flow as S2.
- Why no material first-party path remains: sub-agents share a workspace without a shipped collision-resolution relation, DAG edges are dependency sequencing, fleet admission is classified below as whole-current S3 resource control, and the richer team-coordination design is draft-only.

## S3 — Inside-and-now control

- State: C
- Function: regulate current fleet-wide execution commitments against shared run, sandbox and GPU-node capacity, dependency readiness and task priority.
- Disturbance / variety regulated: several queued/running task or DAG commitments can simultaneously demand limited execution slots, sandboxes and GPU nodes; failed dependencies and dispatch stalls can also leave current work in inconsistent states.
- Decisive decision or feedback right: decide which currently ready/queued rows are admitted/reserved for execution now, which remain deferred, which dependent work is failed, and when DAG roots can settle from peer status.
- Decision owner: constructor/runtime policy. The API scheduler deterministically executes configured priority, dependency and admission-ceiling rules; no autonomous agent owns the fleet-wide admission judgment in the standard path.
- Supporting / enforcement mechanisms: current usage snapshots, run-root accounting, hard/soft admission ceilings, owned admission lock, PostgreSQL row locks/CAS, queued→preparing reservation, dependency promotion/cascade, dispatch timeouts and periodic scheduler ticks.
- Closure path: current occupying/executing usage + ready/queued rows → scheduler applies dependency/priority/capacity policy → accepted rows transition/reserve and dispatch, rejected rows stay queued/waiting → later task status and usage change → next scheduler tick re-evaluates the current portfolio.
- Boundary reachability: `claw/packages/api/src/tasks/scheduler.ts` and its admission machinery are shipped API-runtime paths; deployments can configure the first-party fleet ceilings without writing a new scheduler.
- Why this is / is not agent-owned: the whole-current resource-control function is concrete and closed, but its decisive policy is deterministic/configured rather than autonomously chosen or revised by an agent; therefore the publication state is constructor `C`, not `A`.
- Evidence: `claw/packages/api/src/tasks/scheduler.ts`; `claw/packages/api/src/tasks/admission.ts`; `claw/packages/api/src/config.ts`; task/DAG DB lifecycle.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: zero-valued ceilings disable some capacity dimensions; the positive constructor claim concerns the shipped configured-ceiling mode.

- Whole-system current view: scheduler reads current occupying/executing usage across run roots, sandboxes and GPU nodes together with dependency-ready/queued task rows and their priority/status.
- Current-control decision scope: admit/reserve/defer current tasks under shared ceilings, promote ready dependencies, cascade failed dependency effects, settle DAG roots and dispatch accepted commitments.

## S3* — Complementary audit

- State: —
- Function: no distinct complementary audit path over current S1 operational claims was established.
- Disturbance / variety regulated: repository CI/tests, runtime events, skill-evolution mutation verification and safety checks provide various forms of validation, but none forms a separate shipped S3* path auditing ordinary coding operations.
- Decisive decision or feedback right: no operational auditor with materially different access to S1 reality and a separate audit-to-current-control feedback path was found.
- Decision owner: not established at S3* level.
- Supporting / enforcement mechanisms: event logs/metrics, task settlement checks, evolution mutation verifier, repository tests and safety validators.
- Closure path: runtime checks remain ordinary execution/control feedback; the evolution verifier governs S4 adaptation proposals rather than independently auditing an S1 completion claim.
- Why this is / is not agent-owned: an autonomous verifier exists inside the skill-evolution adaptation path, but function-first mapping places that judgment in S4 capability adaptation, not S3* operational audit.
- Evidence: `claw/packages/api/src/marketplace/skill-service.ts`; `claw/packages/api/src/events/consumer.ts`; task settlement paths; repository tests inspected as adjacent.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: external evaluators or future team reviewer roles could create S3*, but they are not credited here.

### Absence scope

- Surfaces inspected: Brain/Hands runtime results, API event/status paths, task settlement/recovery, skill-evolution verifier, repository CI/tests and draft team/evaluator material.
- Plausible first-party paths checked: event/metrics as S3*; task completion checks as audit; evolution mutation verifier as S3*; repository tests as complementary audit; draft evaluator/team role as S3*.
- Why no material first-party path remains: operational checks are in-band, development tests are adjacent, the shipped verifier audits adaptation mutations rather than operational reality, and the team/evaluator topology is not implemented at the frozen ref.

## S4 — Outside-and-then intelligence

- State: A
- Function: learn from cross-session environmental/task outcomes and autonomously generate, verify and install reusable skill adaptations for future operation.
- Disturbance / variety regulated: an active skill may underperform on changing user tasks or environments, evidenced by failures, high turn counts, repeated errors and contrasting successful/problematic trajectories across recent sessions.
- Decisive decision or feedback right: determine whether observed bad cases justify a capability change, choose concrete skill-description/content/sub-file or new-skill mutations, and accept/reject those mutations through autonomous semantic verification before publication.
- Decision owner: a distributed autonomous LLM path: the evolution LLM proposes evidence-grounded adaptation mutations and a separate verifier LLM can veto unsafe/weak mutations; deterministic validation and DB transaction machinery constrain and apply the surviving decision.
- Supporting / enforcement mechanisms: `shouldEvolveSkill` statistics gate, cross-session good/bad trajectory retrieval, durable evolution-job queue/retries, mutation shape/path/size/safety checks, verifier score threshold, transactional batch application, probation/feedback state and active-skill selection.
- Closure path: completed task outcomes and trajectories accumulate → degraded active skill crosses evolution threshold → LLM analyzes good/bad evidence and proposes future-oriented mutations → verifier/safety gates accept the batch → active skill content/files/version are updated transactionally → later tasks select that active skill → Brain prompt injects the evolved skill → subsequent S1 behavior changes.
- Boundary reachability: the complete path is shipped in `packages/api` and `packages/brain` and is enabled through the documented first-party deployment mode `CLAW_SKILL_EVOLUTION_ENABLED=true`; no custom code or external adaptation service is required.
- Why this is / is not agent-owned: deterministic thresholds and safety gates alone cannot invent the adaptation; removing the LLM adaptation/verification actors leaves evidence storage and enforcement but no semantic choice of capability mutation.
- Evidence: `claw/packages/api/src/events/consumer.ts`; `claw/packages/api/src/marketplace/evolve-worker.ts`; `claw/packages/api/src/marketplace/skill-service.ts`; `claw/packages/api/src/config.ts`; `claw/packages/brain/src/agent/prompt.ts`.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: skill evolution defaults OFF and must be deliberately enabled; `A` describes this documented supported first-party mode, not every deployment.

- External distinction: recent real user/task prompts, tool sequences and execution outcomes distinguish where a selected skill succeeds versus fails or struggles in its operating environment.
- Future / prospective distinction: the evolution prompt explicitly asks what shared bad-case pattern should be changed so future comparable cases succeed without breaking successful behavior.
- Adaptation option generated: autonomous LLM output can revise SKILL.md, description, supporting files, add/delete files, or spawn a new reusable skill, subject to independent semantic/safety validation.
- Path back into current capability / S3: accepted mutations update the active/probation skill store; `selectSkillsForTask` selects those versions for future tasks and Brain `buildPrompt` injects their content/supporting-file hints into subsequent operational runs.

## S5 — Policy and identity

- State: —
- Function: no identity- or ultimate-policy-level closure was established.
- Disturbance / variety regulated: authentication, execution templates/config, feature flags, tool permissions, sandbox/security policy, admission ceilings and operator/admin controls constrain operation.
- Decisive decision or feedback right: no first-party runtime path routes a genuine identity/ultimate-policy issue to a legitimate ultimate authority and returns that decision as governing system identity.
- Decision owner: not established at S5 level.
- Supporting / enforcement mechanisms: auth tokens/roles, environment configuration, feature flags, tool whitelists, sandbox policy, resource ceilings, admin routes and deployment controls.
- Closure path: operators configure or gate concrete runtime capabilities/resources, but those decisions do not constitute an identity-policy issue/authority/return loop at the assessed recursion.
- Why this is / is not agent-owned: security/configuration and operator controls bound the harness but are not evidence of S5.
- Evidence: README; `claw/packages/api/src/config.ts`; Brain sub-agent tool policies; deployment/auth documentation.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: project maintainers have repository governance authority, but development governance is adjacent to the deployed harness boundary.

### Absence scope

- Surfaces inspected: authentication, admin controls, execution/config flags, resource policy, sandbox/security boundaries, skill governance/evolution, operator deployment controls and repository governance.
- Plausible first-party paths checked: execution templates/config as S5; skill verifier/evolution as policy; admin authority as S5; admission ceilings as ultimate policy; maintainer governance as deployed-harness identity.
- Why no material first-party path remains: each runtime path governs capability, resource or adaptation decisions below identity level, while repository governance is an adjacent development organization.

## Distributed OSS parent arrangement

No parent-mode notation is claimed. Maintainer and deployment-operator authority was inspected but does not establish an S3/S4/S5 parent loop beyond the functions already mapped: configured scheduler policy is published as constructor S3, autonomous skill evolution as S4, and no identity-level S5 closure is established.

## Recursion

Ordinary Brain sessions and substantial sub-agent runs can be operational S1 cells, but in-process sub-agents share the parent workspace and do not establish a shipped viable team recursion by themselves. DAG rows contribute current commitments for S3 resource-control analysis. Draft AgentTeam design is excluded until implemented.

## Variety and escalation

Claw absorbs operational variety through the Brain model/tool loop, sandbox recovery, scoped sub-agents, task leases/checkpoints and tool routing. Shared fleet demand is attenuated at the S3 level through deterministic admission/resource policy. With skill evolution enabled, persistent performance variety is elevated into a separate S4 loop that mutates reusable future capability.

## Evidence gaps

No `?` state is required. The frozen tree exposes the operational loop, scheduler/admission machinery and skill-evolution implementation directly. Draft-only AgentTeam material is explicitly excluded rather than used to fill S2/S3*/S5 gaps.

## Assessment summary

PrimusClaw closes autonomous S1 through its shipped Brain/Hands coding loop, supplies constructor S3 through deterministic fleet-wide task/resource admission and closes autonomous S4 in its documented opt-in skill-evolution mode. In-process sub-agents and DAG sequencing do not establish S2, mutation verification belongs to the S4 adaptation path rather than an operational S3* audit, and runtime/deployment governance does not close S5.

**Vector:** A · — · C · — · A · —

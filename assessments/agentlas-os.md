---
harness_id: agentlas-os
project_name: Agentlas OS
repository: https://github.com/agentlas-ai/Agentlas-OS
review_ref: 7032c0b0a660983dcdfdb14cb215d8e93af97d4b
reviewed_at: 2026-09-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-30
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: A(P)
autonomy_s5: P
---

# Agentlas OS

## Review boundary

- System in focus: the shipped Agentlas OS local agent-team operating system at frozen revision `7032c0b0a660983dcdfdb14cb215d8e93af97d4b`, including Workforce task-force construction/execution, Stormbreaker execution fabric, OS-resident PM Soul / Memory Curator / Task Bias roles, host model phases, goal ledger, independent verification, governed memory, and the explicit human authority paths documented by the frozen first-party distribution.
- Purpose and identity: turn user/project goals into governed multi-agent task forces whose work is decomposed, staffed, executed, verified, remembered and adapted under explicit local policy and provenance boundaries.
- Relevant environment: user/project goals; project files and project memory; local/Cloud/Hub candidate inventories; host model/runtime/tool capabilities; specialist worker outputs and artifacts; execution failures; task/goal progress; cost/time budgets; verification evidence; repeated operational experience; user approval for mission/high-impact policy changes.
- Standard-distribution boundary: first-party OS runtime contracts, `agentlas_cloud` execution/workforce/networking code, canonical `system-agents` built-in role bodies and their declared runtime chokepoints, documented local/terminal/Desktop host surfaces, and first-party receipts/journals/state stores are inside where the frozen repository explicitly declares them as shipped/runtime-owned. External model-provider internals, third-party agent packages, Hub/Cloud service internals, user-authored domain packages and repository-development governance are separate unless Agentlas itself owns the decisive organizational function.
- Credited operating / distribution surfaces: `README.md`; `system-agents/MANIFEST.json`; `system-agents/pm-soul.md`; `system-agents/memory-curator.md`; `system-agents/task-bias.md`; `system-agents/orchestrator-protocol.md`; `system-agents/policy-gate.md`; `agentlas_cloud/workforce/contracts.py`; `agentlas_cloud/workforce/selection.py`; `agentlas_cloud/workforce/host_executor.py`; `agentlas_cloud/workforce/goal_ledger.py`; `agentlas_cloud/networking/execution_fabric.py`; `agentlas_cloud/networking/stormbreaker_runner.py`; `agentlas_cloud/evolution_proposals.py`; `agentlas_cloud/memory_hook.py`; `agentlas_cloud/one_workspace.py`.
- Adjacent first-party surfaces excluded from ownership: repository CI/release policy; benchmarks and fixture-only evidence; public Hub ranking/install/usage history; private/provider internals; developer comments that do not correspond to a supported path; package-builder authoring decisions before deployment except where the shipped runtime explicitly preserves them as governing policy.
- First-party operating / deployment modes considered: host-driven Workforce on local/Cloud/Hub source scopes; provider-neutral host adapter execution; Stormbreaker parallel packet execution; nested team manager/worker execution graphs; persistent goal mode; local governed memory/One hooks; OS-resident PM Soul, Memory Curator and Task Bias built-ins; human approval/escalation paths for mission/high-impact decisions.
- Recursion level: one Agentlas-managed project / staffed task force is the system in focus. Specialist model invocations and nested team workers are S1 operational units. PM Soul, task-force control, verification, adaptation and ultimate-policy paths are assessed one level above those operations. A borrowed package is not treated as recursively viable merely because it can itself contain a team.
- Reviewed revision: `7032c0b0a660983dcdfdb14cb215d8e93af97d4b`.
- Observation date: 2026-09-30.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Agentlas separates model judgment from deterministic enforcement. Workforce turns a goal into a typed WorkOrder, federates candidate inventories, lets the host LLM author the exact Selection, pins immutable releases, and executes planner/worker/manager/synthesis/verifier model phases through a provider-neutral adapter. Core validates identities, graph structure, permissions, artifacts and receipts rather than silently choosing a model or package for the host.

Stormbreaker provides execution coordination and assurance. Work packets have explicit artifact dependencies and isolated write scopes, are grouped into dependency-ready parallel groups, and cannot unlock dependents until predecessor packets pass. Cyclic task-force handoffs are rejected before execution with the exact cycle path. A successful executor is still `unverified`; a separately attributable verifier process/model phase must inspect evidence and produce a nonce-bound, digest-checked verification receipt before completion can pass.

Above individual operations, Agentlas ships OS-resident system roles. The PM Soul is declared the project continuity owner and maintains the project-wide source of truth, work ownership, open loops, risks, handoffs and specialist routing. A persistent goal ledger separately enforces whole-goal continuation against current open tasks, stall state and wallclock/cycle/cost budgets. The Task Bias built-in is a second-order governance agent over the project sitemap: it detects undercoverage/staleness/recent-focus bias, changes work-allocation policy in small logged reversible steps and proposes schema changes, while high-impact schema and mission changes escalate to human authority. The Memory Curator owns durable memory admission and conflict-aware promotion, while repeated experience/failure signals also produce explicit growth proposals for future runs.

Primary evidence:

- [`README.md`](https://github.com/agentlas-ai/Agentlas-OS/blob/7032c0b0a660983dcdfdb14cb215d8e93af97d4b/README.md)
- [`system-agents/MANIFEST.json`](https://github.com/agentlas-ai/Agentlas-OS/blob/7032c0b0a660983dcdfdb14cb215d8e93af97d4b/system-agents/MANIFEST.json)
- [`system-agents/pm-soul.md`](https://github.com/agentlas-ai/Agentlas-OS/blob/7032c0b0a660983dcdfdb14cb215d8e93af97d4b/system-agents/pm-soul.md)
- [`system-agents/task-bias.md`](https://github.com/agentlas-ai/Agentlas-OS/blob/7032c0b0a660983dcdfdb14cb215d8e93af97d4b/system-agents/task-bias.md)
- [`agentlas_cloud/workforce/host_executor.py`](https://github.com/agentlas-ai/Agentlas-OS/blob/7032c0b0a660983dcdfdb14cb215d8e93af97d4b/agentlas_cloud/workforce/host_executor.py)
- [`agentlas_cloud/workforce/goal_ledger.py`](https://github.com/agentlas-ai/Agentlas-OS/blob/7032c0b0a660983dcdfdb14cb215d8e93af97d4b/agentlas_cloud/workforce/goal_ledger.py)
- [`agentlas_cloud/networking/execution_fabric.py`](https://github.com/agentlas-ai/Agentlas-OS/blob/7032c0b0a660983dcdfdb14cb215d8e93af97d4b/agentlas_cloud/networking/execution_fabric.py)
- [`agentlas_cloud/networking/stormbreaker_runner.py`](https://github.com/agentlas-ai/Agentlas-OS/blob/7032c0b0a660983dcdfdb14cb215d8e93af97d4b/agentlas_cloud/networking/stormbreaker_runner.py)

## Operational model

A project goal can be decomposed into typed role slots and handoffs. Candidate agents/teams are retrieved from explicit scopes and the host LLM authors the exact staffing selection; Core validates and pins it. At execution time, the host adapter receives separate model phases for orchestration, planning, workers, team managers, synthesis and verification. Worker outputs are materialized as verified handoff artifacts and downstream workers receive predecessor handoffs rather than an unstructured shared transcript.

For Stormbreaker routes, packet dependencies and write scopes define which work may execute concurrently. Dependents remain blocked until prerequisites pass. Execution does not become success from an executor exit alone: separate verification and final gates must pass. Persistent goal mode carries project-level open tasks and budgets across cycles and can stop a stalled or exhausted goal even if a model would otherwise continue.

The PM Soul and Task Bias built-ins operate above individual specialist calls. PM Soul keeps whole-project continuity and ownership current; Task Bias changes allocation policy based on the project sitemap and recent work history. Human authority remains explicit at the top boundary for mission expansion and other declared high-impact changes.

## S1 — Operations

- State: A
- Function: perform goal-directed specialist work through model-owned planning, tool/native execution, worker/team invocations, synthesis and iterative task completion.
- Disturbance / variety regulated: changing user goals, project state, specialist tasks, tool inventory, source availability, predecessor artifacts, runtime/tool failures and observed work results.
- Decisive decision or feedback right: choose task-specific plans/actions/outputs within the selected role and revise later work from verified handoffs and observed execution results.
- Decision owner: host model / selected model-backed worker or team invocation for the active operational role.
- Supporting / enforcement mechanisms: Workforce WorkOrder/Selection contracts; pinned releases; host adapter; tool inventory/bindings; execution graphs; artifact snapshots; Stormbreaker packets; run journals; permission/runtime validation.
- Closure path: project objective/task → model phase chooses the task-specific work → host/native runtime executes and materializes artifacts/results → verified handoffs/observations feed later worker/manager/synthesis phases → the task force continues toward acceptance or a bounded stop condition.
- Boundary reachability: README documents the standard Workforce `search_candidates → validate_selection → prepare_execution` path and external-host execution; `host_executor.py` explicitly classifies orchestrator/planner/worker/manager/synthesis/verifier as model phases in the shipped adapter contract.
- Why this is / is not agent-owned: removing the model phases while retaining Core leaves identities, pins, graph checks and receipts, but removes the material choices about how to solve each specialist task. The operational discretion is therefore agent-owned.
- Evidence: [`README.md`](https://github.com/agentlas-ai/Agentlas-OS/blob/7032c0b0a660983dcdfdb14cb215d8e93af97d4b/README.md); [`host_executor.py`](https://github.com/agentlas-ai/Agentlas-OS/blob/7032c0b0a660983dcdfdb14cb215d8e93af97d4b/agentlas_cloud/workforce/host_executor.py); [`execution_fabric.py`](https://github.com/agentlas-ai/Agentlas-OS/blob/7032c0b0a660983dcdfdb14cb215d8e93af97d4b/agentlas_cloud/networking/execution_fabric.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: Core deliberately owns enforcement/pinning rather than the task-specific model judgment; that separation does not reduce S1 ownership.

## S2 — Coordination

- State: C
- Function: attenuate concrete interference among distinct operational slots by preventing cyclic handoff deadlocks and preventing consumers from running before required producer artifacts have passed.
- Distinct S1 units: producer and consumer specialist/worker slots in one staffed task force; each slot is executed by a separate selected model-backed invocation or nested team member.
- Inter-S1 disturbance: a cyclic handoff graph creates an operational deadlock, while a downstream consumer starting before its producer has a passing artifact creates missing/unverified-input interference.
- Attenuating coordination relation: Core rejects cycle-bearing handoff graphs and Stormbreaker gates each consumer on explicit predecessor `passing` state while isolating packet write scopes.
- Feedback into subsequent S1 behaviour: a rejected cycle forces a new work-order/selection, and a non-passing predecessor prevents the downstream S1 from starting until the predecessor state changes.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the credited relation is tied to an evidenced producer/consumer interference and cyclic deadlock condition, not to the mere existence of edges, queues or delegation.
- Disturbance / variety regulated: cyclic task-force handoffs; dependency inversion; downstream consumption of missing/unverified predecessor outputs; concurrent packets writing into the same generic execution area.
- Decisive decision or feedback right: reject a cyclic work-order/selection; assign packet-specific write scopes; hold a dependent packet until all declared predecessors are passing; block dependent work when a predecessor is not passing.
- Decision owner: deterministic Agentlas Core / Stormbreaker coordination machinery.
- Supporting / enforcement mechanisms: `find_cycle`; WorkOrder/Selection semantic validation; explicit `consumes`/`produces` dependencies; parallel groups; `all_packets_pass_before_dependents_start`; per-packet write scopes; blocked dependency results.
- Closure path: distinct S1 slots declare artifact handoffs → Core detects a cycle or derives predecessor dependencies → cyclic organizations are rejected with the exact path, while valid dependents are held until predecessor status is `passing` → the later S1 start/availability changes accordingly, preventing the identified deadlock or premature-consumption interference.
- Why this is / is not agent-owned: the host model authors the task force, but the decisive attenuation rule is not delegated to a model. Core deterministically detects the cycle/dependency condition and enforces the resulting block/order. This is constructor/runtime-owned coordination, so `C` rather than `A`.
- Boundary reachability: the README documents task split/handoff validation and Stormbreaker as the shipped execution-gating subsystem; the frozen first-party Core implements both cycle rejection and dependency-ready packet execution without requiring user-authored coordination code.
- Evidence: [`contracts.py`](https://github.com/agentlas-ai/Agentlas-OS/blob/7032c0b0a660983dcdfdb14cb215d8e93af97d4b/agentlas_cloud/workforce/contracts.py); [`selection.py`](https://github.com/agentlas-ai/Agentlas-OS/blob/7032c0b0a660983dcdfdb14cb215d8e93af97d4b/agentlas_cloud/workforce/selection.py); [`execution_fabric.py`](https://github.com/agentlas-ai/Agentlas-OS/blob/7032c0b0a660983dcdfdb14cb215d8e93af97d4b/agentlas_cloud/networking/execution_fabric.py); [`stormbreaker_runner.py`](https://github.com/agentlas-ai/Agentlas-OS/blob/7032c0b0a660983dcdfdb14cb215d8e93af97d4b/agentlas_cloud/networking/stormbreaker_runner.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: this credit is not based on generic sequencing, messaging or plurality. The interference witness is the declared producer/consumer handoff graph itself: cyclic handoffs deadlock, and downstream work cannot safely consume a predecessor that has not passed.

## S3 — Inside-and-now control

- State: A
- Function: maintain whole-project current continuity and regulate who owns current work, open loops, risks, handoffs and specialist routing while project execution proceeds.
- Whole-system current view: PM Soul reads the canonical project memory and relevant source/project state and tracks decisions, constraints, owners, risks, pending work and open loops for the whole Agentlas-managed project rather than one worker task.
- Current-control decision scope: choose current ownership/specialist routing, split workstreams, issue handoffs, maintain open-loop state, escalate unresolved decisions and, with deterministic goal-ledger support, continue or block whole-goal execution under current budgets/stall state.
- Disturbance / variety regulated: changing project requests/state; unresolved decisions; ownership ambiguity; open/blocked work; specialist handoff needs; current risks; goal stalls; cycle/cost/wallclock exhaustion.
- Decisive decision or feedback right: frame current work, choose the operational owner/specialist, split workstreams, issue compact handoffs, maintain the project source of truth and current open loops, and decide/escalate what current work proceeds; deterministic goal control can additionally continue/block whole-goal execution under current budgets/stall state.
- Decision owner: OS-resident model-backed PM Soul for project-level current regulation; Agentlas Core goal ledger provides deterministic enforcement/support for continue/block limits.
- Supporting / enforcement mechanisms: PM Soul project memory and routing contract; orchestrator handoff protocol; Workforce staffing/receipts; persistent goal ledger; task/open-loop state; current budget/stall checks.
- Closure path: current project/request + canonical project memory/open loops/risks → PM Soul frames ownership and routes/splits work → specialist S1s execute and return findings/risks/memory proposals → PM Soul updates project state, closes or preserves open loops and chooses the next current owner/action; the goal ledger independently prevents continuation when whole-goal budgets/stall state disallow it.
- Boundary reachability: `system-agents/MANIFEST.json` declares PM Soul as a `runtime-builtin` continuity owner and names its runtime chokepoint; the PM Soul body explicitly owns one project's continuity and specialist routing. README documents Agentlas as the execution OS around these team roles.
- Why this is / is not agent-owned: if PM Soul model judgment is removed, deterministic ledgers can still count tasks/budgets and refuse invalid continuation, but they do not decide the project-level owner, problem framing, handoff content or current workstream routing. The material whole-project S3 judgment is therefore agent-owned.
- Evidence: [`system-agents/MANIFEST.json`](https://github.com/agentlas-ai/Agentlas-OS/blob/7032c0b0a660983dcdfdb14cb215d8e93af97d4b/system-agents/MANIFEST.json); [`pm-soul.md`](https://github.com/agentlas-ai/Agentlas-OS/blob/7032c0b0a660983dcdfdb14cb215d8e93af97d4b/system-agents/pm-soul.md); [`goal_ledger.py`](https://github.com/agentlas-ai/Agentlas-OS/blob/7032c0b0a660983dcdfdb14cb215d8e93af97d4b/agentlas_cloud/workforce/goal_ledger.py); [`orchestrator-protocol.md`](https://github.com/agentlas-ai/Agentlas-OS/blob/7032c0b0a660983dcdfdb14cb215d8e93af97d4b/system-agents/orchestrator-protocol.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: host-LMM WorkOrder creation by itself would only be decomposition. S3 credit instead rests on the OS-resident continuity owner operating over persistent whole-project state and returned specialist results across turns.

## S3* — Complementary audit

- State: A
- Function: independently verify operational outputs/evidence through a separately attributable model-verifier path before success is admitted.
- Disturbance / variety regulated: false completion, invalid or missing evidence, executor-authored self-verification, artifact drift, verifier attribution mismatch and task-force output that fails acceptance.
- Claim being audited: whether a worker/packet/task-force execution actually produced acceptable evidence/artifacts and may truthfully be reported as successful.
- Audited operational claim: that a worker/packet/task-force execution actually produced acceptable evidence/artifacts and may be reported as successful.
- Ordinary control path: orchestrator/planner/worker/manager/synthesis model phases produce work and artifacts; Core materializes handoffs and execution receipts.
- Ordinary reporting path: worker/manager/synthesis phases return their outputs and artifacts through the host adapter and normal execution receipt path before complementary verification.
- Complementary access path: a distinct `verifier` model phase / separately attributable verifier command executes after the worker path, receives verified inputs, and must produce its own verdict/evidence receipt. Stormbreaker deletes any executor-written receipt first, mints a verifier-only nonce, checks verifier identity/command digest, constrains evidence to the packet write scope and verifies artifact SHA-256 values.
- Independence boundary: executor and verifier cannot be the same command in the Stormbreaker path; absence of a verifier remains explicitly `unverified`; host-executor model phases distinguish verifier from synthesis/worker invocations.
- Corrective / return path: verifier failure or missing/invalid evidence blocks the packet/task-force final gate; only a passing independent verification receipt permits `passing`/accepted completion and downstream/final success.
- Closure path: ordinary execution produces a candidate result → the separate verifier inspects the bounded evidence and returns a verdict/receipt → Core validates attribution and evidence → a failed/missing verdict keeps the packet unverified/blocked, while a passed verdict unlocks downstream/final closure.
- Who acts on findings: Agentlas Core/Stormbreaker acts on the verifier finding by blocking or admitting completion; downstream task-force execution therefore changes based on the audit result.
- Decisive decision or feedback right: judge whether produced work passes and therefore whether operational success may close.
- Decision owner: model-backed verifier invocation owns the pass/fail judgment; deterministic Core owns attribution/evidence validation and blocks false closure.
- Supporting / enforcement mechanisms: separate verifier phase; verifier nonce; command digest; evidence SHA-256; write-scope confinement; execution receipt validator; final gate.
- Boundary reachability: README explicitly states planning, work, synthesis and verification run as separate invocations and an independent verifier must pass before anything is called done; both provider-neutral Workforce host execution and Stormbreaker expose this shipped verification boundary.
- Why this is / is not agent-owned: deterministic checks can prove attribution and evidence integrity, but the verifier model phase owns the material evaluation verdict. Removing the verifier judgment leaves completed execution explicitly unverified and unable to pass the final gate.
- Evidence: [`README.md`](https://github.com/agentlas-ai/Agentlas-OS/blob/7032c0b0a660983dcdfdb14cb215d8e93af97d4b/README.md); [`host_executor.py`](https://github.com/agentlas-ai/Agentlas-OS/blob/7032c0b0a660983dcdfdb14cb215d8e93af97d4b/agentlas_cloud/workforce/host_executor.py); [`stormbreaker_runner.py`](https://github.com/agentlas-ai/Agentlas-OS/blob/7032c0b0a660983dcdfdb14cb215d8e93af97d4b/agentlas_cloud/networking/stormbreaker_runner.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: this is not credit for same-path QA naming; the frozen runner explicitly enforces separate attribution and complementary evidence access.

## S4 — Outside-and-then intelligence

- State: A(P)
- Function: detect project undercoverage/staleness/bias and accumulated operational experience, adapt future work-allocation/evidence policy, and escalate high-impact adaptation to human review.
- External distinction: project-sitemap coverage, staleness, risk/dependency state, recent task history, user-reported failures and accumulated operational experience are observed as conditions outside the currently executing specialist task.
- Future / prospective distinction: Task Bias evaluates which project surfaces need future exploration/revalidation and whether domain schema/allocation policy should change for subsequent work rather than only solving the current task.
- Adaptation option generated: tune exploration/recent-focus/dependency/completion-gap weights, create/promote/merge/split sitemap nodes, request revalidation, propose domain-schema fields, and generate future-run growth/guardrail proposals from repeated evidence.
- Path back into current capability / S3: bounded Task Bias decisions update the project sitemap/allocation policy that PM Soul/current routing uses for subsequent work; high-impact proposals return only after parent approval and then govern later project operation.
- Disturbance / variety regulated: uninspected project surfaces; stale validation; repeated recent-focus bias; dependency/risk imbalance; weak evidence density; repeated user failures after validation; domain schema gaps; accumulated experience/repeated failure patterns.
- Decisive decision or feedback right: autonomously tune bounded allocation weights and sitemap state, request revalidation and propose schema changes; propose future guardrail/learning changes from accumulated experience; require human review for high-impact schema changes and mission-level expansion.
- Decision owner: OS-resident model-backed Task Bias governance agent for bounded routine adaptation; human/user parent for declared high-impact or mission-changing adaptations.
- Supporting / enforcement mechanisms: project AI Sitemap; logged reversible allocation-policy weights; Task Bias decision records; Memory Curator / project memory; experience candidate store; evolution-proposal bridge; human review boundary.
- Closure path: project history/sitemap/evidence exposes undercoverage, staleness, bias or repeated failure → Task Bias / evolution machinery forms an allocation-policy, revalidation, schema or growth change → bounded Task Bias changes are logged/reversible and affect subsequent task selection; high-impact schema/mission changes are withheld for user review → accepted policy then governs later work.
- Parent-mode closure: high-impact schema change or project-mission expansion is explicitly recognized as requiring human review/approval; the runtime-builtin governance role escalates rather than deciding it autonomously, and subsequent project operation receives the user's authoritative decision through the host conversation/project state.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | OS-resident Task Bias model-backed governance agent | undercoverage, staleness, recent-focus bias, weak validation evidence or a bounded schema/allocation need | logged/reversible sitemap or allocation-policy change affects subsequent project task selection/revalidation | `system-agents/task-bias.md`; `system-agents/MANIFEST.json` |
| Parent (`P`) | project user/operator | high-impact schema change or mission-level expansion exceeds delegated adaptation authority | governance role escalates; accepted user decision returns through project conversation/state and governs subsequent work | `system-agents/task-bias.md`; `system-agents/pm-soul.md` |
- Boundary reachability: `system-agents/MANIFEST.json` declares Task Bias as a `runtime-builtin` governance role owning the project sitemap; its canonical body states governance starts automatically, allocation weights are tunable/logged/reversible, and high-impact schema changes require human review. The experience/evolution path is also first-party and feeds future-run proposals from repeated evidence.
- Why this is / is not agent-owned: bounded allocation adaptation is materially chosen by a model-backed governance role rather than a fixed scheduler. The parent modifier is separate: the agent is explicitly forbidden from unilateral mission expansion/high-impact schema decisions and must escalate those adaptations to the user.
- Evidence: [`system-agents/MANIFEST.json`](https://github.com/agentlas-ai/Agentlas-OS/blob/7032c0b0a660983dcdfdb14cb215d8e93af97d4b/system-agents/MANIFEST.json); [`task-bias.md`](https://github.com/agentlas-ai/Agentlas-OS/blob/7032c0b0a660983dcdfdb14cb215d8e93af97d4b/system-agents/task-bias.md); [`evolution_proposals.py`](https://github.com/agentlas-ai/Agentlas-OS/blob/7032c0b0a660983dcdfdb14cb215d8e93af97d4b/agentlas_cloud/evolution_proposals.py); [`memory_hook.py`](https://github.com/agentlas-ai/Agentlas-OS/blob/7032c0b0a660983dcdfdb14cb215d8e93af97d4b/agentlas_cloud/memory_hook.py); [`memory-curator.md`](https://github.com/agentlas-ai/Agentlas-OS/blob/7032c0b0a660983dcdfdb14cb215d8e93af97d4b/system-agents/memory-curator.md).
- Basis: explicit + structural.
- Confidence: high for Task Bias allocation adaptation; medium for the separate growth-proposal apply path because this frozen repository exposes proposal generation more clearly than `agentlas evolve` application implementation.
- Caveats: `A(P)` does not rely on the incompletely evidenced growth-proposal apply command. The positive autonomous S4 closure is the runtime-builtin Task Bias policy/sitemap loop; the parent mode is the explicit high-impact/mission review boundary.

## S5 — Policy and identity

- State: P
- Function: preserve ultimate project-mission authority at the human/user parent boundary while lower-level Agentlas roles govern within that mission.
- Identity / ultimate-policy issue: whether the project mission itself may be expanded or changed beyond the delegated scope of the Agentlas governance roles.
- Ultimate authority in each claimed mode: in the claimed parent mode, the project user/operator is the sole decisive authority; Task Bias is explicitly forbidden from expanding mission without explicit user approval.
- Return-to-operation path: the governance role escalates the mission-level question → the user approves/refuses through the host interaction → PM Soul receives the authoritative user input and resumes routing/current control within the resulting mission boundary.
- Disturbance / variety regulated: proposed expansion or change of project mission and other unresolved decisions that exceed delegated role authority.
- Decisive decision or feedback right: approve or refuse mission-level change; delegated governance roles are explicitly prohibited from expanding mission without that approval.
- Decision owner: human/user parent.
- Supporting / enforcement mechanisms: Task Bias mission boundary; PM Soul escalation of unresolved decisions; orchestrator stop-and-escalate rules; Policy Gate declaration that permission widening is a human host decision.
- Closure path: a governance role encounters a mission-level change outside delegated authority → it must escalate to the user rather than silently change mission → the user's response becomes authoritative project input/state → PM Soul/current-control roles continue within the approved mission decision.
- Parent-mode closure: explicit. Task Bias says it cannot expand project mission without explicit user approval and must escalate mission-level changes; PM Soul's output contract surfaces unresolved decisions to the user as questions and treats the user request as an input to subsequent project control.
- Why this is / is not agent-owned: Agentlas intentionally withholds ultimate mission authority from its governance agents. They may frame, recommend and maintain continuity, but the decisive identity/mission choice is reserved to the user; therefore this is `P`, not `A` or `C`.
- Boundary reachability: Task Bias is declared `runtime-builtin` in the frozen system-agent manifest; PM Soul is likewise a runtime-builtin whose normal input includes the user request and whose output contract explicitly escalates unresolved decisions as questions, giving the mission decision a supported return path.
- Evidence: [`task-bias.md`](https://github.com/agentlas-ai/Agentlas-OS/blob/7032c0b0a660983dcdfdb14cb215d8e93af97d4b/system-agents/task-bias.md); [`pm-soul.md`](https://github.com/agentlas-ai/Agentlas-OS/blob/7032c0b0a660983dcdfdb14cb215d8e93af97d4b/system-agents/pm-soul.md); [`orchestrator-protocol.md`](https://github.com/agentlas-ai/Agentlas-OS/blob/7032c0b0a660983dcdfdb14cb215d8e93af97d4b/system-agents/orchestrator-protocol.md); [`policy-gate.md`](https://github.com/agentlas-ai/Agentlas-OS/blob/7032c0b0a660983dcdfdb14cb215d8e93af97d4b/system-agents/policy-gate.md).
- Basis: explicit + structural parent-governance path.
- Confidence: high.
- Caveats: ordinary tool approval or permission configuration is not the basis for S5. Credit rests on the explicit mission-level authority boundary and return through the project's user/PM-Soul control loop.

## Distributed OSS parent arrangement

Repository maintainers and public Hub participants are not counted as the parent of one deployed Agentlas project. The credited parent is the project user/operator only where the shipped runtime explicitly escalates a decision outside delegated authority. Public package popularity, ratings, install history and repository governance are explicitly non-authoritative for runtime staffing and do not receive VSM ownership credit here.

## Self-hosted and non-human modes

Agentlas can operate locally through provider-neutral host adapters and deterministic Core enforcement while model phases own the specialist/manager/verifier judgments. Human involvement is not required for every S1/S2/S3/S3*/S4 decision. It becomes structurally required only at declared parent boundaries such as mission expansion or other explicit high-impact/user-authority decisions.

## Recursion

The assessment uses one Agentlas-managed project/task force as the viable-system recursion. Worker agents and nested team workers are S1 units. PM Soul operates as whole-project S3 at the next level; the independent verifier is complementary S3*; Task Bias is the project-level S4 governance role. Human mission authority is S5 parent mode. Nested worker teams are not recursively promoted to separate viable systems without independent evidence for their own full metasystem.

## Variety and escalation

Agentlas attenuates variety through typed WorkOrders, explicit handoff graphs, candidate eligibility, immutable release pins, permission policies, per-packet write scopes, dependency gates, budgets, run journals, fail-closed receipts and separate verification. It amplifies capacity with federated candidate discovery, host-model staffing, parallel workers, nested teams, MCP/native tools, project memory and OS-resident governance roles. Failure/conflict can become a typed block, independent verification failure, goal stall, revalidation request, memory conflict, or user escalation rather than being silently averaged into success.

## Evidence gaps

- The `agentlas evolve` growth-proposal apply/revert command is referenced by the frozen first-party proposal module, but its implementation was not found in this repository. S4 does not depend on that path because the Task Bias runtime-builtin provides a separate closed adaptation loop.
- PM Soul and Task Bias runtime chokepoints are declared in `system-agents/MANIFEST.json` as OS-resident built-ins; this assessment credits those supported first-party distribution modes, not hypothetical package-local copies.
- S2 is intentionally `C`, not `A`: model-authored task-force design is not itself coordination ownership. The credited interference attenuation is deterministic cycle/dependency enforcement.
- S5 is intentionally parent-only. No autonomous Agentlas role is credited with ultimate authority to redefine the project's mission.

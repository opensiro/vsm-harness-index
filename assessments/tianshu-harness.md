---
harness_id: tianshu-harness
project_name: Tianshu Harness
repository: https://github.com/huiliyi37/Tianshu-harness
review_ref: 6dbf1e0482cf5338b7587d029cbfadc3306b05f5
reviewed_at: 2026-10-13
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Tianshu Harness

## Review boundary

- System in focus: the shipped first-party TypeScript Tianshu coding-agent runtime shared by terminal TUI and desktop app, including its autonomous coding root, supported worker coordinator/team-wave mode, execution/verification gates, and goal judging. Do not import the repository maintainer's benchmark/dev process as runtime organization.
- Purpose and identity: autonomously complete human-specified coding work through live file/tool/model decisions and, where needed, coordinated implementation workers with scoped writes, evidence-gated delivery, and supplementary independent verification.
- Relevant environment: user repository and local shell/Git, external model API(s), project rules, human permissions and optional web/MCP/browser integrations. Those externals provide observations or capabilities but not the first-party organization by themselves.
- Standard-distribution boundary: installable CLI `tianshu` and shipped desktop front end calling common agent core; default tool presets, supported `delegate_task`, `delegate_batch` and `team_orchestrate` modes, coordinator-controlled work orders, goal continuation when the judge/coordinator are wired, first-party runtime hook and evidence systems. Optional advanced profiles can be credited only as explicitly shipped and reachable; no external custom orchestration.
- Credited operating / distribution surfaces: [README.en.md](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/README.en.md); [index.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/index.ts); [loop.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/loop.ts); [coordinator.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/coordinator.ts); [work-queue.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/work-queue.ts); [team-orchestrate.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/tools/team-orchestrate.ts); [plan-executor.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/plan-executor.ts); [task-board.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/task-board.ts); [coordination-policy.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/coordination-policy.ts); [worker-write-gate.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/worker-write-gate.ts); [worker-evidence.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/worker-evidence.ts); [goal-judge.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/goal-judge.ts); [goal-continuation.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/goal-continuation.ts); [loop-factory.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/loop-factory.ts); [verification.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/verification.ts); [model-routing-shadow-controller.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/model-routing-shadow-controller.ts); [domain-drift-detector.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/domain-drift-detector.ts); [retrospect.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/retrospect.ts); [tool-preset.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/tools/tool-preset.ts); [semantic-lock.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/semantic-lock.ts).
- Adjacent first-party surfaces excluded from ownership: documentation's A/B evaluation claims and model-quality tables, source unit tests and development CI, repository contributor governance, optional project-specific skills and custom plugins, prompts/examples with no packaged execution route, nonexecuting shadow telemetry, the separate model-provider's organizational choices, and downstream external integrations.
- First-party operating / deployment modes considered: ordinary autonomous root coding tasks; `team_orchestrate` with wave-based scoped write workers; direct single/batched delegate orders; opt-in distinct reviewer/goal-judge worker contexts; external operator-approved plans; shadow model routing only insofar as it actually affects behavior (it does not in the cited shadow controller).
- Recursion level: one live software engineering engagement comprising root/lead and subordinate code-executing workers under an explicit team mode. Not the package's owner organization, the whole user company or separate unrelated Tianshu deployments.
- Reviewed revision: `6dbf1e0482cf5338b7587d029cbfadc3306b05f5`.
- Observation date: 2026-10-13.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

[README.en.md](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/README.en.md) defines the shipped CLI/desktop common runtime, tool loop, worker delegation, team-wave operation and delivery evidence gates. [loop.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/loop.ts) runs the coding model/tool loop; the coordinator in [coordinator.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/coordinator.ts) accepts work orders from [team-orchestrate.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/tools/team-orchestrate.ts) and [plan-executor.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/plan-executor.ts), creates independently executing workers, controls a global concurrent worker capacity, and returns their status/evidence to the calling model/tool session. [task-board.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/task-board.ts) is explicitly a read-only projection of queue events, not an agentic decision maker. [coordination-policy.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/coordination-policy.ts) differentiates brain/hands/read-only worker permissions.

Cross-worker protection has a concrete implementation. [coordinator.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/coordinator.ts) `checkGlobalFileConflict` checks the declared file scopes of in-flight orders; two readonly scopes may coexist, but a write overlap blocks the second order. `runDelegationWithGlobalGateImpl` rejects unscoped writers, checks/registers claims *after* concurrency admission, returns a `blocked` work result with an explicit conflict and a recommendation to wait or narrow `scope.files`, and removes the claim at settlement. [work-queue.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/work-queue.ts) additionally serializes unsafe overlap inside wave queues. These are deterministic coordination decisions enforced by first-party code, not an autonomous S2 model judgment merely because a model may react later.

[plan-executor.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/plan-executor.ts) and [team-orchestrate.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/tools/team-orchestrate.ts) expose planning/wave execution with live statuses, stop/retry/review gates and current management actions. The model-led root decides the present subtask plan, specializations and delegated assignments; deterministic schedulers and constraint gates preserve execution safety and aggregate evidence. [worker-write-gate.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/worker-write-gate.ts) reruns verification against a worker's actual changed tree, catches false-green, and can request one bounded repair by the same worker; this standard verification gate is not counted as independently reasoning S3*. Instead, [goal-judge.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/goal-judge.ts) constructs a distinct read-only `goal_judge` model worker's direct-test/file-read objective, [loop-factory.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/loop-factory.ts) wires that worker to `Coordinator.delegate`, and [goal-continuation.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/goal-continuation.ts) consumes its verified/rejected/inconclusive verdict with operational consequences. A rejection within the retry budget returns an explicit correction instruction to the implementing agent; unavailability and exhausted retries can accept unverified with telemetry, so do not claim this is an unconditional fail-closed proof gate.

[model-routing-shadow-controller.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/model-routing-shadow-controller.ts) explicitly computes and records model-routing recommendations in *shadow-only* mode, never affecting a model call. [domain-drift-detector.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/domain-drift-detector.ts) is likewise observational domain drift signalling, not automatic adoption of a new domain. Task planning, retrospective memory and repository-dependent adaptations must not be promoted to prospective organizational S4 or ultimate-policy S5 without another decisive operating path.

## Operational model

The coding model uses actual tool observations to continue, edit or stop; in team mode the lead model decomposes and delegates across write-capable workers. Deterministic scope/conflict admission attenuates concrete cross-worker interference, and model-led assignment/replanning manages current delegated commitments using returned statuses/results. Distinct judge-model verification can challenge producer completion claims and return corrections, conditional on an active wired coordinator and enabled goal judging. Operator permissions and governance rules are external constraints, not an autonomous ultimate-identity owner.

## S1 — Operations

- State: A
- Function: execute uncertain repository coding work by deciding files/tools/commands and next actions after observing real outputs.
- Disturbance / variety regulated: unknown source state, inconsistent tool outcomes, failing verification, incomplete edits and changed runtime context.
- Decisive decision or feedback right: root and subordinate working models decide next tool use/code change and whether the coding subtask is done after tool-result feedback.
- Decision owner: operating coding models in root and write-capable delegated S1 workers.
- Supporting / enforcement mechanisms: model/tool loop, command and file tools, worker tool whitelist, permission hooks, context persistence and verification gates.
- Closure path: model selection → tool admission and file/shell execution → observed result/error → further model action/repair/final answer.
- Boundary reachability: first-party packaged CLI/runtime invokes root coding actions and dispatched write-worker model sessions; no third-party workflow must be authored.
- Why this is / is not agent-owned: removing the model's discretionary next-action choice leaves tool dispatch/verification plumbing but no task-specific adaptive coding operation.
- Evidence: [README.en.md](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/README.en.md); [loop.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/loop.ts); [coordinator.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/coordinator.ts); [coordination-policy.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/coordination-policy.ts); [worker-write-gate.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/worker-write-gate.ts)
- Basis: explicit and structural
- Confidence: high for shipped source path, no live credentialed model run
- Caveats: human authorizes risky actions; developer CI and benchmark results do not own this function.

## S2 — Coordination

- State: C
- Function: attenuate inter-S1 file-write interference among concurrently running implementation workers through scope-dependent dispatch admission and returned conflict feedback.
- Disturbance / variety regulated: two independently running write-capable S1 workers attempting to change overlapping files, including across separate waves and single vs batch delegation.
- Decisive decision or feedback right: the deterministic Coordinator global file-claim gate rejects overlapping incoming orders after slot admission; the blocked result and suggested scope fix are returned to the caller.
- Decision owner: first-party deterministic coordination constructor, not a demonstrated agent-owned S2 choice. Root model may change subsequent assignments after returned conflict but deterministic gate enforces the actual conflict relation.
- Supporting / enforcement mechanisms: declared `scope.files`, work-order queue dependency/file checks, current in-flight claims map, concurrency semaphore, separate read-vs-write worker profiles.
- Closure path: existing writer claims files → second writer's overlapping scope detected → second order blocked with conflicting paths and wait/narrow guidance → caller may retry with revised scope once conflict clears; claims removed on settlement.
- Boundary reachability: single delegation, batch and background dispatch use the shipped `runDelegationWithGlobalGateImpl`; it is wired before worker execution, not merely a test utility.
- Why this is / is not agent-owned: without model discretion the deterministic interference guard still rejects overlapping writers and reports the conflict; the model's possible broader rescoping is an S3/S1 scheduling response, not evidence that S2 itself becomes A.
- Evidence: [coordinator.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/coordinator.ts); [work-queue.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/work-queue.ts); [coordination-policy.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/coordination-policy.ts); [team-orchestrate.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/tools/team-orchestrate.ts)
- Basis: explicit executable dispatch code
- Confidence: high within declared file-scope contract; unscoped writers blocked rather than assumed safe
- Caveats: file scope must be declared and truthful, and this does not guarantee detection of semantic collisions between disjoint files.
- Distinct S1 units: separately running write-capable implementation workers executing model/tool tasks under coordinator work orders.
- Inter-S1 disturbance: overlapping write scopes could corrupt or overwrite another worker's changed files.
- Attenuating coordination relation: global scope claim admission rejects unsafe concurrent work and serializes non-read-only conflicts.
- Feedback into subsequent S1 behaviour: blocked worker result with conflict paths and revised scope/wait instruction returned to manager/lead to modify later task dispatch.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the gate compares specific shared write resources between S1 workers and rejects the conflicting action; it is not merely a queue/status list.

## S3 — Inside-and-now control

- State: A
- Function: exercise current management of multiple delegated coding operations through model-selected work breakdown, wave assignments and response to current worker evidence.
- Disturbance / variety regulated: multiple simultaneously running task commitments, dependency and deadline/verification failures, blocked workers and available execution capacity.
- Decisive decision or feedback right: lead model elects how to break down the present user objective, requests worker profiles/scopes and follow-on repairs or new work; wave execution/worker feedback enables dynamic commitments.
- Decision owner: root/lead coding model in supported multi-worker team/plan modes; not TaskBoard read-only projection, deterministic queue or automatic review gates.
- Supporting / enforcement mechanisms: `team_orchestrate` and plan-wave execution, queue state and live work results, dispatch gate, human plan approval where configured, verification/revision feedback.
- Closure path: current multi-worker progress/failure/conflict/verification outcome → lead sees results and chooses updated task(s) or repair scope → coordinator dispatches a changed worker commitment → new status/review feedback.
- Boundary reachability: shipped `team_orchestrate` tool and `delegate_batch`/coordinator paths run through the packaged runtime and are referenced by documented `/team` mode.
- Why this is / is not agent-owned: remove the lead's discretionary plan/task selection and generic wave execution can still run a static plan, but cannot choose new task objectives, worker scopes or repair responses based on the present system view.
- Evidence: [team-orchestrate.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/tools/team-orchestrate.ts); [plan-executor.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/plan-executor.ts); [coordinator.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/coordinator.ts); [task-board.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/task-board.ts); [work-queue.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/work-queue.ts); [loop.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/loop.ts)
- Basis: explicit and structural
- Confidence: medium-high for session/workflow-scoped lead control, not multi-deployment authority
- Caveats: some execution ordering is constructor-owned; operator-approved plans and predefined worker budgets remain human/deterministic controls.
- Whole-system current view: the supported orchestration run aggregates per-wave work orders, worker status/results, verification and affected file scopes.
- Current-control decision scope: select which current engineering subtask is assigned to which worker, when repair/revision is required, and what follow-up committed work to dispatch.

## S3* — Complementary audit

- State: A
- Function: independently challenge implementing-agent completion evidence with a separate read-only test/file-reading goal judge and return a corrective verdict to the running goal-continuation controller.
- Disturbance / variety regulated: a producing coding agent can falsely claim that a goal and individual acceptance criteria have been satisfied despite defects or missing behavior.
- Decisive decision or feedback right: a separately spawned `goal_judge` model directly verifies acceptance criteria with tests/files (optional browser/API where enabled) and classifies verified/rejected/inconclusive; a rejected verdict within retry budget causes the root task to continue and repair.
- Decision owner: separate judge model for complementary verdict, with runtime controller for bounded verdict/retry disposition and implementing model for corrective work.
- Supporting / enforcement mechanisms: goal tracker, coordinator delegate `kind: verify, profile: goal_judge`, read-only-plus-test profile, evidence snapshot and telemetry, bounded retry counter.
- Closure path: implementer emits GOAL ACHIEVED → goal continuation creates independent judge order → judge directly inspects repository/test reality rather than trusting claim → verdict returns to controller → rejection yields explicit next-turn unmet criteria and repair work.
- Boundary reachability: `loop-factory.ts` wires active `goalJudge` configuration and a coordinator reference directly to `goal-continuation.ts`; this is first-party runtime code, not an offline maintainer/CI reviewer.
- Why this is / is not agent-owned: the distinct judge model exercises evidentiary judgment; deterministic verification-only gates and producer self-report cannot supply the same independent verdict. Optional fail-open on judge unavailability is explicitly disclosed.
- Evidence: [goal-judge.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/goal-judge.ts); [goal-continuation.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/goal-continuation.ts); [loop-factory.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/loop-factory.ts); [coordinator.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/coordinator.ts); [worker-evidence.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/worker-evidence.ts); [worker-write-gate.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/worker-write-gate.ts)
- Basis: explicit first-party source
- Confidence: medium-high on reachable positive path; independent context vs implementation task, not a separate organization or universally enforced gate
- Caveats: disabled/missing coordinator, inconclusive verdict or exhausted retries may accept an unverified completion with warning; no blanket fail-closed or S3* organizational audit claim.
- Claim being audited: implementer's assertion that the user's goal and acceptance criteria are genuinely complete.
- Ordinary reporting path: implementer summary, captured evidence/tool output and main-side write verification metadata.
- Complementary access path: separately run read-only goal_judge worker instructed to use real file reads/tests to challenge each criterion, optionally HTTP/browser checks.
- Independence boundary: fresh delegated model worker role/context inspecting actual project state rather than solely consuming producer's successful status.
- Who acts on findings: goal continuation returns specific rejected criteria for further root implementation within bounded review rounds.

## S4 — Outside-and-then intelligence

- State: —
- Function: no evidence-backed shipped agent-owned prospective outside-world capability redesign/adoption loop changes the organization after external sensing.
- Disturbance / variety regulated: changing model/provider capabilities, outside tools and future environmental opportunities.
- Decisive decision or feedback right: no operational prospective adaptation decision owner with an applied capability change and returned control closure established.
- Decision owner: human/configuration for domain and model settings, coding agent for present-work choices; shadow-only routing model produces no applied decision.
- Supporting / enforcement mechanisms: cognitive hooks, model routing shadow telemetry, historical reward summaries, domain drift suggestion, task retrospective/memory and optional external web/tools.
- Closure path: observations and model recommendations are stored or used in present tasks, but the checked model-routing-shadow controller explicitly never changes active model calls and domain drift detector only advises.
- Why this is / is not agent-owned: task-context research, prompt/skill updates and shadow candidate rankings do not prove a future-oriented system adaptation decision with return.
- Evidence: [model-routing-shadow-controller.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/model-routing-shadow-controller.ts); [domain-drift-detector.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/domain-drift-detector.ts); [retrospect.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/retrospect.ts); [README.en.md](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/README.en.md); [loop-factory.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/loop-factory.ts)
- Basis: explicit no-apply code and bounded structural source inspection
- Confidence: medium; broad first-party codebase could later reveal another reachably applied path
- Caveats: tactical model/profile selection per worker should not be mistaken for organizational S4 prospective capability adaptation.

### Absence scope

- Surfaces inspected: model routing shadow controller, model-policy candidate scoring, adaptive task memory, star domain drift suggestions and documented provider modes
- Plausible first-party paths checked: future-focused environmental sensing, agent-owned adoption of newly selected capability, oversight/permission and returned changed organizational operating capability
- Why no material first-party path remains: inspected candidate paths serve current task context or produce nonacting shadow telemetry and human settings; no materially qualifying future-adaptation closure is established in supported runtime.

## S5 — Policy and identity

- State: —
- Function: no ultimate identity/purpose-policy adjudicator and returned governing decision is shipped at this coding-engagement recursion.
- Disturbance / variety regulated: conflicts over durable organizational identity, constitutional policy or mission rather than one dangerous tool/edit.
- Decisive decision or feedback right: no agent or first-party parent decides final mission identity and propagates a binding governing policy change.
- Decision owner: human task owner/project maintainer outside system-in-focus sets purpose and governance; tool permission checks implement localized constraints.
- Supporting / enforcement mechanisms: security gates, worker whitelists, plan approvals, domain prompts, project rule memory and runtime hooks.
- Closure path: human permission returns an allow/deny for an action, or a plan is approved; these do not constitute a constitutional identity conflict and an authoritative identity decision returned to operational units.
- Why this is / is not agent-owned: safety policy engine and governance-like naming or project memory do not have the decisive ultimate policy/identity right.
- Evidence: [README.en.md](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/README.en.md); [coordination-policy.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/coordination-policy.ts); [tool-preset.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/tools/tool-preset.ts); [loop.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/loop.ts); [plan-executor.ts](https://github.com/huiliyi37/Tianshu-harness/blob/6dbf1e0482cf5338b7587d029cbfadc3306b05f5/src/agent/plan-executor.ts)
- Basis: structural
- Confidence: medium-high at stated recursive boundary
- Caveats: the public repository's maintainer practices and user-enterprise governance are separate external systems.

### Absence scope

- Surfaces inspected: tools/security restrictions, plan approvals, memory/role governance cues, documented maintainer policies
- Plausible first-party paths checked: identity-level conflict arbitration, accessible constitutional parent owner and binding decision returned into the operating session
- Why no material first-party path remains: only ordinary task/action policy enforcement and human choices are evidenced; no first-party ultimate identity-decision closure is present.

## Recursion

Independent write-capable worker sessions are subordinate S1 execution units to a model-led task organization in documented team modes; do not infer that each worker contains its own S2–S5 metasystem. The current team-coordinator path is first-party but the external user's company and maintainer's repository project are outside the assessed recursion.

## Variety and escalation

Model-driven coding uses tool-result feedback to meet the immediate objective. Global scoped-write claims attenuate cross-worker interference deterministically. Model-led work decomposition, wave selection and response to failed/blocked child results regulate current team commitments. The goal judge offers a separate complementary direct-evidence check and correction path, although unavailable/inconclusive/exhausted cases may accept unverified. Human permission/plan approval attenuates risk but is not an internal S5.

## Evidence gaps

Pinned-source static assessment, not a credentialed end-to-end live run. The C for S2 reflects deterministic scoped-writer admission, not a claim of autonomously invented coordination. S3 and S3* positives are mode-conditioned and limited to the supported team/goal-judge paths. EFE shadow recommendations do not by themselves change active model routing. Further independent deployment tests could clarify how often the eligible modes actually run; negative S4/S5 apply to bounded shipped first-party operation rather than universal future impossibility.

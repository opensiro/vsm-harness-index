---
harness_id: orkas
project_name: Orkas
repository: https://github.com/Orkas-AI/Orkas
review_ref: bc21869913e30b72f83998d79c030b290d10f140
reviewed_at: 2026-09-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-30
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: A
autonomy_s5: P
---

# Orkas

## Review boundary

- System in focus: one Orkas-managed project/team operating through the shipped local-first desktop runtime at frozen revision `bc21869913e30b72f83998d79c030b290d10f140`, including Commander, named group agents and anonymous workers, core-agent runners, group-chat orchestration state, shared conversation/project workspaces, first-party tools, project context, persistence and background reflection.
- Purpose and identity: turn user-owned project goals and current requests into bounded multi-agent work while preserving the user's standing project rules, routing specialist work, protecting shared execution state and adapting future behavior from observed experience.
- Relevant environment: current user requests; user-authored project goals/rules; project files and workspaces; named specialist agents and their outputs; external web/model/provider results; tool and connector availability; concurrent writes; failures/blockers; user corrections, preferences and domain constraints; accumulated conversation activity.
- Standard-distribution boundary: first-party Orkas desktop/source runtime, bundled Commander and marketplace-agent definitions, group-chat state/bus contracts, core-agent runner/tool surface, project instructions/context, workspace/file conflict handling, cross-session memory and metacognitive reflection are inside where the frozen repository wires them into normal operation. External model-provider internals, web sites, MCP/connector services and third-party tools remain dependencies.
- Credited operating / distribution surfaces: `README.md`; `src/main/prompts/chat_commander.md`; `src/main/prompts/chat_user_intent_rules.md`; `src/main/prompts/chat_project_context_policy.md`; `src/main/features/group_chat/state.ts`; `src/main/util/uniquify-path.ts`; `src/main/model/core-agent/runner.ts`; `src/main/features/projects.ts`; `src/main/features/metacognition.ts`; `src/main/features/reflection-orchestrator.ts`; `src/core-agent/src/evolution/metacognition.ts`; bundled marketplace agent definitions where they are shipped runtime actors.
- Adjacent first-party surfaces excluded from ownership: `eval/model-eval` and repository tests/fixtures; CI/release/development governance; source comments or plans not wired into the frozen runtime; feature-local QA/audit routines that assess one task artifact but do not independently audit the Orkas operating system; stripped/private account/sync service internals; external provider/connector/tool implementations.
- First-party operating / deployment modes considered: local desktop/source operation; Commander-led group chat; project-scoped conversations with user-authored standing instructions; named specialist dispatch/handoff; anonymous bounded workers; parallel nested agent turns; background metacognitive reflection; external-model/provider execution through the first-party runner.
- Recursion level: one Orkas project/team is the system in focus. Commander is the project/team metasystem current-control actor. Named specialist agents, anonymous workers and direct Commander task execution are S1 operational units where they perform user-visible work. The project user/operator is the legitimate parent for identity/ultimate-policy decisions. Agent-private learning is credited to the project recursion only where the shipped `_default`/Commander reflection path changes future metasystem behavior.
- Reviewed revision: `bc21869913e30b72f83998d79c030b290d10f140`.
- Observation date: 2026-09-30.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Orkas is a local-first desktop agent runtime centered on a Commander plus specialist Agents. The Commander receives the current visible conversation, runtime injection and, when work is suspended, a persisted orchestration ledger. It chooses whether to act directly, hand work to one named Agent, dispatch work whose result must return for synthesis, or create a bounded anonymous worker. Named agents receive their own sessions, skills, tools and persistent context; nested work can run in parallel while the top-level conversation remains serialized by the host runtime.

The runtime separates discretionary model decisions from deterministic host enforcement. Group-chat state records the current floor, in-flight actors and suspended larger task. Tool surfaces, project boundaries and permissions are host-enforced. Shared-workspace write tools use a requested-path mutex and unique-name fallback so parallel agent turns do not silently overwrite one another. Project instructions provide durable user-authored standing goals/rules and are injected into every project session under an explicit priority policy where the current user request remains authoritative.

Orkas also ships a background reflection loop. It selects agents with new activity, builds a bounded transcript, asks a model to identify durable competence/strategy/skill updates, persists accepted changes, and injects the resulting metacognition into later eligible turns. For the default/Commander scope this closes an adaptation path back into the team metasystem rather than only into one specialist.

Primary evidence:

- [`README.md`](https://github.com/Orkas-AI/Orkas/blob/bc21869913e30b72f83998d79c030b290d10f140/README.md)
- [`src/main/prompts/chat_commander.md`](https://github.com/Orkas-AI/Orkas/blob/bc21869913e30b72f83998d79c030b290d10f140/src/main/prompts/chat_commander.md)
- [`src/main/features/group_chat/state.ts`](https://github.com/Orkas-AI/Orkas/blob/bc21869913e30b72f83998d79c030b290d10f140/src/main/features/group_chat/state.ts)
- [`src/main/util/uniquify-path.ts`](https://github.com/Orkas-AI/Orkas/blob/bc21869913e30b72f83998d79c030b290d10f140/src/main/util/uniquify-path.ts)
- [`src/main/features/projects.ts`](https://github.com/Orkas-AI/Orkas/blob/bc21869913e30b72f83998d79c030b290d10f140/src/main/features/projects.ts)
- [`src/main/features/reflection-orchestrator.ts`](https://github.com/Orkas-AI/Orkas/blob/bc21869913e30b72f83998d79c030b290d10f140/src/main/features/reflection-orchestrator.ts)
- [`src/main/model/core-agent/runner.ts`](https://github.com/Orkas-AI/Orkas/blob/bc21869913e30b72f83998d79c030b290d10f140/src/main/model/core-agent/runner.ts)

## Operational model

A user request enters a Commander-managed conversation. Commander resolves current intent, separates outcomes and chooses the owner, decomposition, sequencing, verification method and recovery route inside the user's existing authority. It can complete work itself, transfer the floor to a specialist, dispatch a specialist and consume the result, or use an anonymous worker for bounded isolated work. When a larger Commander-owned task blocks on a specialist interaction, Orkas persists an orchestration ledger containing the user goal, owner, handoff and resume instruction so current-control continuity survives the handoff.

Specialist and Commander turns use the first-party runner and tool surfaces to produce concrete outputs. When parallel agent turns share a conversation workspace, host file-write coordination prevents same-path silent overwrite and returns the actual saved path to the losing actor. Project sessions additionally receive user-authored standing instructions and project context. Background reflection later reviews real activity/corrections and can change the competence/strategy/skill state injected into future turns.

## S1 — Operations

- State: A
- Function: perform user-visible project work through model-owned reasoning, specialist execution and tool use, producing answers, files, research, code or other requested outcomes.
- Disturbance / variety regulated: changing user requests, project files/context, external information, tool/provider availability, specialist domain requirements, intermediate results, errors and blockers.
- Decisive decision or feedback right: choose task-specific actions, tool calls, artifact changes and substantive output needed to satisfy the assigned outcome, and revise that work from observed tool/result feedback.
- Decision owner: Commander or the selected model-backed named Agent/worker for the active operational outcome.
- Supporting / enforcement mechanisms: core-agent runner; provider selection; scoped tool surface; conversation/session persistence; workspace/path guards; dispatch/handoff bus; tool-result storage; host permission gates.
- Closure path: user/project outcome → model-backed operational actor selects actions/tools → first-party runner executes and returns observations/artifacts → actor revises or completes the outcome → result returns to the user or Commander for the next operation.
- Boundary reachability: the frozen README documents direct Commander work and named-agent dispatch/handoff as shipped behavior, while the first-party runner builds the model/tool loop for normal group sessions. No external orchestrator must be composed to create the operational decision loop.
- Why this is / is not agent-owned: removing the model-backed Commander/specialist while retaining deterministic runner/session/tool machinery leaves execution primitives but removes the task-specific choices about what work to perform and how to respond to results. The material operational discretion is agent-owned.
- Evidence: [`README.md`](https://github.com/Orkas-AI/Orkas/blob/bc21869913e30b72f83998d79c030b290d10f140/README.md); [`chat_commander.md`](https://github.com/Orkas-AI/Orkas/blob/bc21869913e30b72f83998d79c030b290d10f140/src/main/prompts/chat_commander.md); [`runner.ts`](https://github.com/Orkas-AI/Orkas/blob/bc21869913e30b72f83998d79c030b290d10f140/src/main/model/core-agent/runner.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: external model providers supply inference, but Orkas owns the first-party model/tool/session operating loop and the standard distribution exposes those autonomous operational roles directly.

## S2 — Coordination

- State: C
- Function: attenuate a concrete same-resource interference between distinct parallel S1 agent turns sharing one conversation workspace.
- Distinct S1 units: two or more parallel Commander-dispatched/nested agent turns that can independently write user-visible files into the same conversation workspace.
- Inter-S1 disturbance: concurrent turns can request the same output path, both observe it as free and silently overwrite one another's work if probe and write are not coordinated.
- Attenuating coordination relation: `uniquifyPathForWrite` serializes path decision plus write on a mutex keyed by the requested path; after the first write, the losing writer sees the collision and receives a suffixed path rather than overwriting the winner.
- Feedback into subsequent S1 behaviour: the runtime returns a `<file-renamed>` signal naming the actual saved path and instructs the actor to use that exact path in subsequent reads, references and the user-visible response.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the credited relation exists specifically to regulate an evidenced interference created by parallel S1s contending for the same workspace resource. Credit does not come from group-chat routing, a queue, plurality or the existence of shared state.
- Disturbance / variety regulated: same-path concurrent writes and silent overwrite between independently running agent turns.
- Decisive decision or feedback right: serialize contenders on the requested path, preserve the first writer's artifact, assign a unique path to the conflicting later writer, and return that coordination result to the later S1.
- Decision owner: deterministic first-party Orkas file-write coordination machinery.
- Supporting / enforcement mechanisms: per-path `fileEditLock`; existence probes; suffix generation; write-under-lock; `<file-renamed>` feedback block.
- Closure path: parallel S1s target the same path → mutex serializes probe+write → the first write wins and the later write is renamed → the later S1 receives the actual path and changes subsequent references accordingly, eliminating the silent-overwrite interference.
- Boundary reachability: this path is wired into normal first-party write-style tools (`write_file`, PDF/image output paths) in the shared conversation workspace; it is not an example-only or user-composed extension.
- Why this is / is not agent-owned: no autonomous agent chooses the collision-resolution policy. The host deterministically applies the coordination rule. Under the Methodology publication boundary this is a first-party constructor/runtime-owned S2 path, therefore `C` rather than `A`.
- Evidence: [`src/main/util/uniquify-path.ts`](https://github.com/Orkas-AI/Orkas/blob/bc21869913e30b72f83998d79c030b290d10f140/src/main/util/uniquify-path.ts); [`src/main/model/core-agent/local-tools.ts`](https://github.com/Orkas-AI/Orkas/blob/bc21869913e30b72f83998d79c030b290d10f140/src/main/model/core-agent/local-tools.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: shell-side writes can bypass `write_file` conflict protection, so the S2 claim is bounded to the first-party coordinated write-tool path rather than every possible filesystem mutation.

## S3 — Inside-and-now control

- State: A
- Function: maintain whole-team current control over ownership, decomposition, sequencing, verification and recovery for the user's active project outcome.
- Whole-system current view: Commander receives the visible conversation/current request, runtime injection, project context and the suspended-orchestration ledger when one exists; the ledger preserves the larger user goal, current specialist owner, handoff and resume instruction across an interactive delegation.
- Current-control decision scope: decide outcome ownership, task decomposition, sequencing, verification method and recovery route; diagnose agent-reported blockers; repair recoverable host/workspace blockers; resume the original outcome; decide when work may run in parallel versus when dependent work must wait.
- Disturbance / variety regulated: multiple candidate owners, changing current user intent, dependencies among outcomes, specialist blockers/failures, interrupted handoffs, stale/failed delivered results, and the need to preserve the larger commitment while one interaction blocks.
- Decisive decision or feedback right: choose which actor owns each current outcome and how work is decomposed/sequenced/verified/recovered within the user's existing authority.
- Decision owner: model-backed Commander.
- Supporting / enforcement mechanisms: group-chat bus; server-authoritative floor; `state.json`; in-flight tracking; orchestration ledger; task board; runtime/session persistence; deterministic permission and admission rules.
- Closure path: current whole-goal state + returned specialist/tool evidence → Commander chooses owner/decomposition/sequence/verification/recovery → S1 work runs or is held → result/blocker returns to Commander → Commander repairs, reroutes, resumes or completes the larger outcome and updates subsequent current operation.
- Boundary reachability: Commander is the default shipped orchestrator for group chat. The frozen prompt explicitly assigns these current-control choices to Commander, and `state.ts` persists the larger Commander-owned task across handoff rather than requiring an external supervisor.
- Why this is / is not agent-owned: with the bus/ledger/runtime retained but Commander judgment removed, Orkas can persist and route already-selected state but does not choose the best owner, decomposition, recovery or verification route for the active whole. The decisive S3 discretion is therefore agent-owned.
- Evidence: [`src/main/prompts/chat_commander.md`](https://github.com/Orkas-AI/Orkas/blob/bc21869913e30b72f83998d79c030b290d10f140/src/main/prompts/chat_commander.md); [`src/main/features/group_chat/state.ts`](https://github.com/Orkas-AI/Orkas/blob/bc21869913e30b72f83998d79c030b290d10f140/src/main/features/group_chat/state.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: delegation alone is not the S3 evidence. Credit rests on Commander's whole-goal current decision rights and the returned blocker/result loop, with deterministic state machinery treated only as support/enforcement.

## S3* — Complementary audit

- State: —
- Function: no material first-party complementary audit path was established at the declared Orkas project/team recursion.
- Disturbance / variety regulated: not established beyond task-local verification/QA inside individual operational workflows.
- Decisive decision or feedback right: no separate metasystemic audit judgment over the operating team's claimed reality was found.
- Decision owner: not established.
- Supporting / enforcement mechanisms: Orkas ships several verification/QA mechanisms, including provenance-bound citation checking and feature-local content/office/video checks, but these remain part of the task's ordinary production/validation path.
- Closure path: no first-party complementary audit channel was found that independently samples or reconstructs project/team operations and returns findings into Commander current control.
- Why this is / is not agent-owned: not applicable; the function itself is not established at this boundary.
- Evidence: [`src/main/model/core-agent/research-verify-tool.ts`](https://github.com/Orkas-AI/Orkas/blob/bc21869913e30b72f83998d79c030b290d10f140/src/main/model/core-agent/research-verify-tool.ts); [`resources/builtin/marketplace/agents/78900d8758bc/agent.json`](https://github.com/Orkas-AI/Orkas/blob/bc21869913e30b72f83998d79c030b290d10f140/resources/builtin/marketplace/agents/78900d8758bc/agent.json); [`eval/model-eval`](https://github.com/Orkas-AI/Orkas/tree/bc21869913e30b72f83998d79c030b290d10f140/eval/model-eval).
- Basis: explicit + structural negative review.
- Confidence: medium-high.
- Caveats: the negative state is boundary-relative. A task-local verifier can be strong assurance without being VSM S3* at the project/team recursion.

### Absence scope

- Surfaces inspected: frozen README and root tree; Commander/group-chat orchestration prompt/state; core-agent runner and tool surfaces; bundled specialist workflows; provenance-bound research verification; feature-local audit/QA/search surfaces; background reflection/metacognition; project context/policy; repository `eval/model-eval` and representative tests as adjacent evidence.
- Plausible first-party paths checked: a separate verifier actor over Commander/specialist work; host-side evidence verification; office/video/content audit paths; replay/evaluation surfaces; reflection as a potential retrospective challenger; persisted group-chat state/ledger as a possible audit feed.
- Why no material first-party path remains: the runtime verifiers found are embedded in the ordinary S1 deliverable path and judge local claims/artifacts, reflection adapts future behavior rather than independently auditing current operations, and `eval/model-eval`/tests are development-evaluation surfaces excluded from the shipped ownership boundary. No shipped complementary actor/channel with sufficiently independent access to project/team operational reality and a return path into Commander S3 was found.

## S4 — Outside-and-then intelligence

- State: A
- Function: convert external/user-experience distinctions from prior activity into autonomous changes to future Commander/agent competence, strategies and learned behavior.
- External distinction: user corrections, edits, preferences, domain constraints, repeated success/failure evidence and other activity signals observed in completed conversations are treated as evidence about the environment rather than merely the current task instruction.
- Future / prospective distinction: the reflection loop asks which stable lessons should alter later behavior and explicitly separates durable methods/preferences from transient errors, so the decision concerns future capability rather than only resolving the just-finished turn.
- Adaptation option generated: revise `COMPETENCE.md`, revise `LEARNING_STRATEGIES.md`, and for named Agents create/patch/delete learned skills when durable evidence supports a reusable change; otherwise return `nothing to save`.
- Path back into current capability / S3: persisted metacognition is re-read and injected into later eligible model turns. The empty agent id maps Commander conversations to `_default`, so project/team current control can be changed by this learned state on later Commander turns; named agents likewise receive their own persisted learning.
- Disturbance / variety regulated: recurring user corrections; newly discovered preferences/domain constraints; obsolete self-assessments; repeated strengths/weaknesses; reusable recovery methods; changing operating evidence across conversations.
- Decisive decision or feedback right: judge which observed activity contains a durable lesson, what competence/strategy/skill change should be made, and whether nothing should be saved.
- Decision owner: model-backed reflection run for the relevant Commander/default or named-agent scope.
- Supporting / enforcement mechanisms: dirty-activity gate; cooldown and per-cycle cap; transcript builder; persistence limits/injection scan; metacognition write tool; evolved-skill store; future-turn prompt injection.
- Closure path: completed activity/corrections/signals → background scheduler selects an eligible scope → reflection model reviews transcript/current self-knowledge and chooses an adaptation → host persists the change → next eligible Commander/agent turn receives the changed competence/strategy/skill context and can alter present operation.
- Boundary reachability: reflection is wired as first-party background runtime behavior; `_default` explicitly covers unbound/Commander conversations, and the normal runner injects persisted metacognition into later eligible turns. The project/team S4 claim therefore does not borrow a development-only evaluator or a specialist-only private loop.
- Why this is / is not agent-owned: deterministic scheduling decides when reflection may run and persistence enforces limits, but the material adaptation judgment—what lesson exists and how future behavior should change—is produced by the reflection model. Removing that model leaves scheduling/storage but no prospective adaptation decision.
- Evidence: [`src/main/features/reflection-orchestrator.ts`](https://github.com/Orkas-AI/Orkas/blob/bc21869913e30b72f83998d79c030b290d10f140/src/main/features/reflection-orchestrator.ts); [`src/core-agent/src/evolution/metacognition.ts`](https://github.com/Orkas-AI/Orkas/blob/bc21869913e30b72f83998d79c030b290d10f140/src/core-agent/src/evolution/metacognition.ts); [`src/main/features/metacognition.ts`](https://github.com/Orkas-AI/Orkas/blob/bc21869913e30b72f83998d79c030b290d10f140/src/main/features/metacognition.ts); [`src/main/model/core-agent/runner.ts`](https://github.com/Orkas-AI/Orkas/blob/bc21869913e30b72f83998d79c030b290d10f140/src/main/model/core-agent/runner.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: generic durable memory is not the S4 basis. Credit rests on the explicit evidence-review → model adaptation judgment → durable future-turn reinjection loop, especially the `_default` Commander path at the assessed recursion.

## S5 — Policy and identity

- State: P
- Function: preserve the project's standing goal/rules and ultimate authority to create exceptions or expand/change those rules at the user/operator parent boundary.
- Identity / ultimate-policy issue: what the project is trying to accomplish and which standing rules govern its conversations, including whether the current request creates an exception to those saved project instructions or authorizes changing them.
- Ultimate authority in each claimed mode: the project user/operator is authoritative. `ORKAS.md` is explicitly user-authored standing goal/rules; the current user request has higher priority; saved project instructions/tasks/memory may be changed only with user authorization.
- Return-to-operation path: user authors or authorizes the standing instructions/current exception → Orkas persists the project instructions and injects the policy block plus user-authored content into every project conversation → Commander and named project agents follow that returned policy on subsequent work, with the current request able to override it for the active turn.
- Disturbance / variety regulated: conflicts among current user intent, standing project goals/rules, project status/memory and directive-looking stale context; attempts to widen action/policy beyond the user's authorized target/condition.
- Decisive decision or feedback right: define the project's standing goal/rules, authorize changes to them, and create current-request exceptions or authorize materially different/policy-expanding action.
- Decision owner: human project user/operator parent.
- Supporting / enforcement mechanisms: `ORKAS.md` project-instructions persistence; conflict-priority prompt; compare-and-set model write path; project owner scope; user-intent authority rules; runner injection into every project session.
- Closure path: project-level rule/goal or exception issue arises → legitimate user provides/authorizes the authoritative instruction → first-party project store and runner return it into all relevant project sessions → Commander/specialist operation is subsequently governed by the saved instructions or current higher-priority request.
- Boundary reachability: projects and project instructions are a shipped first-party mode. The frozen project module states that the USER edits the standing goal/rules, the runner injects them into every project session, and model-side replacement is conditional; the project context policy explicitly requires user authorization for stored-context changes.
- Why this is / is not agent-owned: Commander and named project actors can carry out an authorized instruction change through the conditional tool, but they do not own the ultimate policy right. The current user request outranks saved project instructions, and the runtime requires user authorization for changing those standing rules. No autonomous S5 ownership mode was established, so the published state is parent-only `P`.
- Evidence: [`src/main/features/projects.ts`](https://github.com/Orkas-AI/Orkas/blob/bc21869913e30b72f83998d79c030b290d10f140/src/main/features/projects.ts); [`src/main/prompts/chat_project_context_policy.md`](https://github.com/Orkas-AI/Orkas/blob/bc21869913e30b72f83998d79c030b290d10f140/src/main/prompts/chat_project_context_policy.md); [`src/main/prompts/chat_user_intent_rules.md`](https://github.com/Orkas-AI/Orkas/blob/bc21869913e30b72f83998d79c030b290d10f140/src/main/prompts/chat_user_intent_rules.md); [`src/main/model/core-agent/runner.ts`](https://github.com/Orkas-AI/Orkas/blob/bc21869913e30b72f83998d79c030b290d10f140/src/main/model/core-agent/runner.ts).
- Basis: explicit + structural parent-governance path.
- Confidence: high.
- Caveats: ordinary permission prompts, deletion confirmations and tool approvals are not used as S5 evidence. Credit is limited to the user-owned project goal/rule hierarchy and its complete return into subsequent operation.

## Distributed OSS parent arrangement

Public Orkas maintainers/contributors are not treated as the parent of one deployed project/team merely because they control the repository. The credited parent is the local project user/operator whose standing rules and current requests are consumed by the shipped runtime. Repository governance, CI and public development decisions remain outside this deployment recursion.

## Self-hosted and non-human modes

Orkas is local-first and can execute ordinary S1/S2/S3/S4 decisions without continuous human supervision once the user has supplied the task/project boundary. The operator remains structurally authoritative for project identity/ultimate policy. No alternative first-party autonomous S5 mode was established at the frozen revision.

## Recursion

At the assessed recursion, one user-owned Orkas project/team is the system. Named specialist agents, anonymous workers and direct task-performing turns are operational S1s. Shared-workspace conflict handling coordinates those operations. Commander provides whole-team current S3 control. Commander/default reflection provides project-level future adaptation. The user/operator remains the parent S5 authority. A named agent's private skills/memory are lower-recursion capabilities unless their outputs return through the Commander/project loop.

## Variety and escalation

Orkas attenuates operational variety with explicit owner selection, bounded delegation shapes, server-authoritative floor/state, suspended-orchestration ledgers, scoped tool surfaces, permission gates, shared-workspace collision handling and project context precedence. It amplifies capacity through specialist agents, anonymous workers, parallel nested dispatch, web/tools/connectors, cross-session context and learned strategies. Blockers can return to Commander for diagnosis/recovery; materially new authority or policy expansion returns to the user rather than being silently selected.

## Evidence gaps

- S3* is intentionally negative at the project/team recursion. Strong task-local verifiers such as provenance-bound citation checking are ordinary QA for those S1 workflows, not a separately closed complementary audit of Orkas operations as a whole.
- S2 is intentionally `C`, not `A`: the concrete coordination loop is fully first-party but the decisive same-path collision rule is deterministic runtime policy rather than autonomous agent discretion.
- S4 credit is bounded to the shipped reflection path whose saved changes are actually reinjected into future turns; persistence/memory by itself is not counted.
- S5 is intentionally `P`. Model actors may execute an already-authorized project-instruction change, but the user remains the authority over the standing project goal/rules and current exceptions.

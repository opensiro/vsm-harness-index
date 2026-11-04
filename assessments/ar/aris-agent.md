---
harness_id: aris-agent
project_name: aris-agent
repository: https://github.com/tauhb/aris-agent
review_ref: 067695907ffa776afdf42595b08a7587e0c00424
reviewed_at: 2026-11-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: A(P)
autonomy_s5: P
---

# aris-agent

## Review boundary

- System in focus: The installed Aris personal/team-agent product: the version-pinned DeepSeek Harness (DSH) runtime composed with Aris's own Commander, bots, goals, memory, reflection, skills, guard, channels and user interfaces; not DSH as an independently assessed general framework.
- Purpose and identity: Execute user work through one or more configurable personal agents while coordinating team assignments, bounded goals, owner preferences and reusable skills.
- Relevant environment: User instructions, files, tools, external model/provider and CLI responses, other team agents, task dependencies, feedback on earlier responses, budget and permission constraints.
- Standard-distribution boundary: The checked-in Aris bundle adds its plugin rows after the DSH base and web/ACP/headless bundles; its own CLI/setup launches that composition. External model services and optional outside Codex/Claude workers supply cognition/execution but do not donate their unrelated organizational controls.
- Credited operating / distribution surfaces: [bundle wiring](https://github.com/tauhb/aris-agent/blob/067695907ffa776afdf42595b08a7587e0c00424/packages/aris-bundle/cordis.patch.yml), [Commander](https://github.com/tauhb/aris-agent/blob/067695907ffa776afdf42595b08a7587e0c00424/packages/aris-commander/src/index.ts), [dispatch](https://github.com/tauhb/aris-agent/blob/067695907ffa776afdf42595b08a7587e0c00424/packages/aris-commander/src/dispatch.ts), [goal autonomy](https://github.com/tauhb/aris-agent/blob/067695907ffa776afdf42595b08a7587e0c00424/packages/aris-autonomy/src/index.ts), [reflection](https://github.com/tauhb/aris-agent/blob/067695907ffa776afdf42595b08a7587e0c00424/packages/aris-reflect/src/index.ts), [skills](https://github.com/tauhb/aris-agent/blob/067695907ffa776afdf42595b08a7587e0c00424/packages/aris-skills/src/index.ts), [bot identity and API](https://github.com/tauhb/aris-agent/blob/067695907ffa776afdf42595b08a7587e0c00424/packages/aris-bots/src/api.ts), and [guard](https://github.com/tauhb/aris-agent/blob/067695907ffa776afdf42595b08a7587e0c00424/packages/aris-guard/src/index.ts).
- Adjacent first-party surfaces excluded from ownership: UI demos, scripted unit tests, project development/design plans, contributor CI, uninstalled skills/templates, optional standalone external-agent drivers beyond the selected composition and upstream DSH's independent project governance.
- First-party operating / deployment modes considered: Aris web UI, one-shot headless and ACP, one-bot work, Commander/team and project Driver, reflection/learn with owner approval, operator persona and department-policy editing, routine/goal callbacks and hard guard.
- Recursion level: One self-hosted Aris installation and its team of operational bots, with individual task agents as S1 units; a mere subagent process is not another proven full VSM recursion.
- Reviewed revision: `067695907ffa776afdf42595b08a7587e0c00424`.
- Observation date: 2026-11-04.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The product is a TypeScript monorepo of Aris plugins mounted into an explicitly configured DSH agent, team, tool, session and schedule foundation. Its standard Aris bundle actually inserts Commander, bots, memory, providers, reflection, skills, goal autonomy, routines, guard, checkpoints, channel, UI and other integrations into web/ACP/headless modes. DSH's model/tool engine is a runtime dependency; the first-party Aris code adds a model-facing team delegation tool, bot roles, projects and an optional task Driver. Commander prompts the model to choose small direct work, specialist delegation or a whole department, and receives real teammate results. Goal autonomy runs a separate inexpensive model verdict after turns, controls completion/block/wait and injects missing-work notices. Reflection analyzes actual turns, writes high-confidence owner insights into future prompts, and proposes reusable skills/memory for human approval. Guard enforces cost/permission stops without becoming the organizational chooser. [Bundle](https://github.com/tauhb/aris-agent/blob/067695907ffa776afdf42595b08a7587e0c00424/packages/aris-bundle/cordis.patch.yml), [Commander guide](https://github.com/tauhb/aris-agent/blob/067695907ffa776afdf42595b08a7587e0c00424/packages/aris-commander/src/index.ts), [autonomy](https://github.com/tauhb/aris-agent/blob/067695907ffa776afdf42595b08a7587e0c00424/packages/aris-autonomy/src/index.ts), [reflection](https://github.com/tauhb/aris-agent/blob/067695907ffa776afdf42595b08a7587e0c00424/packages/aris-reflect/src/index.ts).

## Operational model

User work enters one model-bearing Aris/DSH session. Its bot chooses tools and may delegate to other named model-bearing bot sessions; those independently process local subtasks. Commander or an authorized department lead selects assignments, reasons and follow-up, while first-party shared task records, dependency-ready checks, role restrictions and busy limits constrain execution. Teammate reports return to the delegator and can change its next choice. Owner-created bot personalities, departments and policies become required runtime prompt context, but vendor model intelligence, external CLIs, operator policy and deterministic caps remain distinct from Aris's own decision ownership.

## S1 — Operations

- State: A
- Function: Perform autonomous user-requested work through model-selected tools and independently acting bot sessions.
- Disturbance / variety regulated: Different user requests, source/tool feedback, missing information, task progress and local failures.
- Decisive decision or feedback right: Choose a substantive tool/response or delegated task action, interpret results and continue/stop within a goal.
- Decision owner: The model-bearing current bot and assigned operational bot, using the installed DSH loop and Aris-defined team/task context.
- Supporting / enforcement mechanisms: DSH model/tool/session engine, Aris prompt and bot roster, guard, goal counters, state stores and bounded scheduling.
- Closure path: User/goal → bot model turn → tool or teammate action → observed result → next turn/action and final response or goal disposition.
- Boundary reachability: Standard Aris composition includes the live model/tool DSH engine, with Aris goal/team integrations across web/headless/ACP modes; delegation is an installed callable tool rather than an unshipped plan.
- Why this is / is not agent-owned: The model chooses task content and actions; the runtime may enforce permissions or persistence but does not make the operational choice.
- Evidence: [bundle wiring](https://github.com/tauhb/aris-agent/blob/067695907ffa776afdf42595b08a7587e0c00424/packages/aris-bundle/cordis.patch.yml), [Commander tool and prompt](https://github.com/tauhb/aris-agent/blob/067695907ffa776afdf42595b08a7587e0c00424/packages/aris-commander/src/index.ts), [dispatch/teammate action](https://github.com/tauhb/aris-agent/blob/067695907ffa776afdf42595b08a7587e0c00424/packages/aris-commander/src/dispatch.ts), [goal continuation and verdict](https://github.com/tauhb/aris-agent/blob/067695907ffa776afdf42595b08a7587e0c00424/packages/aris-autonomy/src/index.ts).
- Basis: explicit + structural.
- Confidence: high for the wired agent/action path; runtime provider execution was not replayed in this review.
- Caveats: Aris does not own the external model or DSH's independent general-purpose agent engine, but its installed product organizes their participation in this task boundary.

## S2 — Coordination

- State: A
- Distinct S1 units: Named concurrently active team bots, each with an independent task/session and potentially overlapping skills or dependencies.
- Inter-S1 disturbance: Duplicate assignments to the same bot, overcommitting the shared busy-bot capacity, dispatching not-ready dependency cards, and two workers attempting incompatible task ownership.
- Attenuating coordination relation: Commander selects a target and action from the roster and observed task state; `dispatch` refuses duplicate names, rejects capacity overflow and dependency-unready cards, records owner/revision and returns explicit refusal feedback. The model must sequence or revise assignments in response.
- Feedback into subsequent S1 behaviour: Rejected or blocked dispatch is reported back in the model tool result; Commander is instructed to wait for dependencies or worker results, then choose another assignment, sequence later work and integrate reports.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: Specific shared-worker overcommitment and dependency collisions are tested before dispatch; refusal is an in-band signal for changed subsequent team commitments, not merely arbitrary message transport.
- Function: Attenuate team-agent assignment/interference and dependency oscillation while keeping work distributed.
- Disturbance / variety regulated: Competition for a limited set of specialist workers and premature dependent-task starts.
- Decisive decision or feedback right: Select an alternative worker, revise assignment ordering, or postpone dependent work upon real conflict feedback.
- Decision owner: Model-driven Commander/authorized lead for task reallocation; deterministic checks enforce task-ready, single-target and max-busy constraints.
- Supporting / enforcement mechanisms: DSH task/member state, `busyBots`, repeated-handle check, task revision and owner update, and the explicit rejection summary.
- Closure path: Competing assignment → guard refuses or task reports not-ready → model receives error → revises dispatch/waits → subsequent worker commitments reflect the new choice.
- Boundary reachability: Both Commander model guidance and concrete `dispatch` tool/board checks ship in the configured Aris bundle, with no separately scripted user glue needed.
- Why this is / is not agent-owned: Hard capacity/duplicate checks do not themselves choose the new work partition; that reallocation remains the model's discretion.
- Evidence: [dispatch interference guards and return](https://github.com/tauhb/aris-agent/blob/067695907ffa776afdf42595b08a7587e0c00424/packages/aris-commander/src/dispatch.ts), [Commander sequencing guidance/tool registration](https://github.com/tauhb/aris-agent/blob/067695907ffa776afdf42595b08a7587e0c00424/packages/aris-commander/src/index.ts), [project board](https://github.com/tauhb/aris-agent/blob/067695907ffa776afdf42595b08a7587e0c00424/packages/aris-projects/src/board.ts).
- Basis: structural + explicit.
- Confidence: medium; first-party paths are present, but no observed multi-bot collision-recovery success rate is claimed.
- Caveats: If only one bot operates, this inter-bot function is dormant. Mechanical rejection is supporting S2 rather than independent agentic ownership.

## S3 — Inside-and-now control

- State: A
- Whole-system current view: Commander has the team roster, work/assignment history, busy count, project tasks and returned worker status; an authorized lead can view its department's present work.
- Current-control decision scope: Decide current task granularity, which specialist/department receives work, staged commitments, shared capacity use, dependency sequencing and integration of worker results.
- Function: Govern current shared team commitments and accountable delegation against the user's whole task.
- Disturbance / variety regulated: Insufficient specialist fit, busy worker capacity, dependencies, incomplete or failed delegated tasks, changing immediate user priorities.
- Decisive decision or feedback right: From the full requested task and team state, choose direct work vs delegation vs department, specialist/commitment allocation and response to returned results.
- Decision owner: Model-bearing Commander or the delegated department-lead session for the relevant current work; human explicitly chooses or overrides its own requests.
- Supporting / enforcement mechanisms: TeamPort and DSH member/task APIs, recorded dispatch, limits and task Driver, budgets, authorization settings.
- Closure path: User goal and live team context → Commander selects whole-task resource commitments → task/member state and bot actions update → returned reports/errors prompt next current allocation or completed answer.
- Boundary reachability: The standard Commander plugin injects its current-control guide and registers `giao_viec`/department delegation; dependency and status hooks are wired into the operational team path.
- Why this is / is not agent-owned: The agent selects which current work and roles to commit, while the task board, concurrency limits and guard merely implement/limit that discretion.
- Evidence: [Commander guidance and live ports](https://github.com/tauhb/aris-agent/blob/067695907ffa776afdf42595b08a7587e0c00424/packages/aris-commander/src/index.ts), [assignment choices and records](https://github.com/tauhb/aris-agent/blob/067695907ffa776afdf42595b08a7587e0c00424/packages/aris-commander/src/dispatch.ts), [projects](https://github.com/tauhb/aris-agent/blob/067695907ffa776afdf42595b08a7587e0c00424/packages/aris-projects/src/index.ts).
- Basis: explicit + structural.
- Confidence: medium-high for available current-control authority; the quality of resource decisions was not empirically benchmarked.
- Caveats: A per-task assignment alone would be insufficient; the whole-team/project state and controlled commitments supply the narrower S3 claim. Operator preferences and hard caps are not transferred to the agent.

## S3* — Complementary audit

- State: —
- Function: No separate sufficiently independent complementary inspection and corrective audit channel is established in the reviewed installed modes.
- Disturbance / variety regulated: Potential false task/goal completion and misleading agent reports, mitigated partly by ordinary goal grading, tests and checkpoints but without an independent audit owner.
- Decisive decision or feedback right: Independently challenge an operational claim using alternative reality evidence and send a corrective finding; no such first-party governed right found.
- Decision owner: The after-turn `aris-autonomy` judge decides goal status from the bot's own answer/tool-name record; deterministic checkpoints/guard do not exercise independent operational audit judgment.
- Supporting / enforcement mechanisms: Model-based completion grader, file snapshots, ordinary skill evaluations and logs.
- Closure path: Goal verdict can block/retry the same task, but its inputs are mainly the producer's ordinary report; a complementary ground-truth-to-control return is not established.
- Why this is / is not agent-owned: A distinct model call for a routine completion verdict is not inherently independent access to reality; checkpoints capture recovery material, not an audit finding owner.
- Evidence: [judge inputs and goal transitions](https://github.com/tauhb/aris-agent/blob/067695907ffa776afdf42595b08a7587e0c00424/packages/aris-autonomy/src/index.ts), [pre-tool file checkpoints](https://github.com/tauhb/aris-agent/blob/067695907ffa776afdf42595b08a7587e0c00424/packages/aris-checkpoints/src/index.ts), [skill evaluation surface](https://github.com/tauhb/aris-agent/blob/067695907ffa776afdf42595b08a7587e0c00424/packages/aris-skills/src/eval.ts).
- Basis: structural.
- Confidence: medium-high within the pinned installed modes.
- Caveats: An operator may configure external review, but no first-party routine auditor with complementary source access and returned corrective scope was demonstrated.

### Absence scope

- Surfaces inspected: Installed bundle, autonomy model verdict, Commander task reports, checkpoint/rollback hooks, skill evaluation and guard/error paths.
- Plausible first-party paths checked: Goal judge as reviewer, independent teammate reviewing another's primary artifacts, checkpoint diff as evidence, automatic skill test, human preview and approval.
- Why no material first-party path remains: The goal judge receives the operational answer/tool summary, checkpoints merely capture files, and generic peer/skill/test utilities lack a shipped independent complementary audit owner and corrective return loop; these can be composed into future review but are not the established S3* relationship.

## S4 — Outside-and-then intelligence

- State: A(P)
- External distinction: Actual user corrections, remember-this requests, repeated failures, tool outcomes and observed individual preferences enter the reflection engine from task encounters; these are environmental feedback beyond mere current-step planning.
- Future / prospective distinction: Retained user insights alter future bot contexts; proposed reusable memories/skills are intended for subsequent tasks, not just finishing the current turn.
- Adaptation option generated: A model review extracts structured preferences and reusable task practice; it may propose a new or updated skill with evaluation examples, while high-confidence owner insights are recorded automatically.
- Path back into current capability / S3: Trusted observations are rendered into later system-prompt context; a human-approved skill becomes active in the catalog and available to later agents.
- Function: Convert observed environmental/use feedback into a changed future operating repertoire for the team.
- Disturbance / variety regulated: Recurring mismatch between user practice and existing agent guidance, newly revealed preferences and tool-failure patterns.
- Decisive decision or feedback right: In the base mode the reflection model selects trusted future-relevant observations that Aris persists/loads; in the parent mode the user approves/rejects skill adaptation before activation.
- Decision owner: Reflection model in the autonomous owner-insight path; owner/user in the reviewed-skill publication path.
- Supporting / enforcement mechanisms: Trigger heuristics, provider selection, daily cost cap, insight confidence store, proposal queue, skill catalog and prompt-context renderer.
- Closure path: User corrections/tool history → reflect model makes future guidance → high-confidence insight automatically enters subsequent prompt; alternatively skill proposal → owner approval → active skills refresh → subsequent task may use the new skill.
- Boundary reachability: Reflection and skills plugins are in the standard bundle, subscribed to actual sessions and wired to context and review/approval API, not test-only self-improvement examples.
- Why this is / is not agent-owned: In base insight mode the model makes the substantive content selection and persistence is automatic; in skill mode the user holds acceptance discretion. Neither the queue nor the scheduler owns that choice.
- Evidence: [reflection triggers and insight feedback](https://github.com/tauhb/aris-agent/blob/067695907ffa776afdf42595b08a7587e0c00424/packages/aris-reflect/src/index.ts), [insight confidence/prompt](https://github.com/tauhb/aris-agent/blob/067695907ffa776afdf42595b08a7587e0c00424/packages/aris-reflect/src/insights.ts), [skill proposal, approval and live refresh](https://github.com/tauhb/aris-agent/blob/067695907ffa776afdf42595b08a7587e0c00424/packages/aris-skills/src/index.ts).
- Basis: explicit + structural.
- Confidence: medium; the mechanism is installed but not behaviorally measured across real future tasks.
- Caveats: These are user- and experience-oriented adaptation modes; routine in-goal progress verdicts alone are not credited as S4. Unapproved skill drafts cannot be credited as active capability.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Reflection model | Observed user corrections/failure/repeated practice | Trusted future-relevant owner insight enters later prompts | [reflect](https://github.com/tauhb/aris-agent/blob/067695907ffa776afdf42595b08a7587e0c00424/packages/aris-reflect/src/index.ts), [insights](https://github.com/tauhb/aris-agent/blob/067695907ffa776afdf42595b08a7587e0c00424/packages/aris-reflect/src/insights.ts) |
| Parent (`P`) | Installation owner/user | New skill/revision proposed from observed use | Approval changes active skill catalog and next agent context | [skills approval](https://github.com/tauhb/aris-agent/blob/067695907ffa776afdf42595b08a7587e0c00424/packages/aris-skills/src/index.ts) |

## S5 — Policy and identity

- State: P
- Identity / ultimate-policy issue: What a named team bot is for, its assigned role/persona and binding department tool policy; an Aris rewrite can propose an updated identity, but does not self-authorize it.
- Ultimate authority in each claimed mode: The self-hosted installation owner, through authenticated bot/department API and human confirmation, rather than the generated persona text or model that drafts it.
- Return-to-operation path: User updates or accepts rewritten SOUL/role/department policy → bot store and version history change → required prompt-context renderer and tool policy read the new binding settings for later sessions/actions.
- Function: Close the purpose, identity and binding rule choices for the owned bot team.
- Disturbance / variety regulated: Conflicting or changing user expectations about agent role, working ethos, and allowed tools relative to actual tasks.
- Decisive decision or feedback right: Accept, replace or restore the bot's identity instructions and binding departmental tool permissions.
- Decision owner: Parent installation owner/user; the optional model-driven rewrite returns only an uncommitted draft.
- Supporting / enforcement mechanisms: `soul-rewrite` draft model, versioned SOUL history, bot/departments store, authenticated API, required persona context, tool permission gate.
- Closure path: Parent identifies desired role/policy update → model may suggest SOUL → user saves it via API → durable bot/department state changes → subsequent bot prompt and tool checks enforce the new identity/constraints.
- Boundary reachability: Bot/departments API, `soul-rewrite`, history/version restore and required persona context are installed core product surfaces, not repository governance or static config examples.
- Why this is / is not agent-owned: Removing the human decision leaves a draft but not an authoritative identity update; prompt injection and tool enforcement merely apply accepted parent choices.
- Evidence: [bot API identity edits and rewrite draft](https://github.com/tauhb/aris-agent/blob/067695907ffa776afdf42595b08a7587e0c00424/packages/aris-bots/src/api.ts), [SOUL revision history](https://github.com/tauhb/aris-agent/blob/067695907ffa776afdf42595b08a7587e0c00424/packages/aris-bots/src/soul.ts), [required persona injection](https://github.com/tauhb/aris-agent/blob/067695907ffa776afdf42595b08a7587e0c00424/packages/aris-bots/src/index.ts), [policy enforcement](https://github.com/tauhb/aris-agent/blob/067695907ffa776afdf42595b08a7587e0c00424/packages/aris-bots/src/policy.ts).
- Basis: explicit + structural.
- Confidence: medium for the per-installation bot-team parent path, not for any broader community/open-source parent governance.
- Caveats: Ordinary approval of a file edit, API credential or spending cap is not itself S5; this mapping is limited to role/SOUL/department-purpose decisions that define who each bot is. No independent autonomous agent-owned ultimate-policy mode is credited.

## Distributed OSS parent arrangement

Multiple contributors to the Aris repository are not a shared agent organization at the assessed recursion. Local bot-team authority belongs to each installation owner. Contributor CI, maintainer actions and project README policies are outside this installed runtime and do not establish an additional parent mode.

## Self-hosted and non-human modes

The bundle can be run locally with web/headless/ACP interfaces. Optional humans select bot/department identity and approve durable skill changes; autonomous bot work, coordination and current resource choices remain separate. The parent modes above are limited to specific identity/adaptation loops with returned live effects.

## Recursion

Individual assigned bots have local sessions, task scopes and environment contact. The installation is the assessed whole; there is no claim that every nested DSH subagent or CLI worker has its own complete independent S1–S5 recursion.

## Variety and escalation

Commander uses task size, skill fit, dependency readiness and busy capacity to attenuate concurrent-work variety. Guard rejects prohibited tools/budget overruns and offers emergency human stop; its hard veto does not confer S3/S5 discretion. Goal judge distinguishes done, blocked, wait and no-progress and returns that feedback into sessions, with bounded scheduling. Skill approval and bot identity editing deliberately return future capability/policy changes to the installation owner's authority.

## Evidence gaps

- No provider-backed E2E execution, external CLI runtime test or measured team-conflict recovery was performed at the pinned ref; source and repository tests underpin the mapping.
- DSH engine/model provider behavior is an external integration boundary. The credited decisions are those reachable in the shipped Aris composition, not the unrelated independent DSH project's metagovernance.
- Skill acceptance is parent-owned; the autonomous reflective S4 claim is limited to the verified high-confidence owner-insight route, not autonomous rewriting of all team skills.

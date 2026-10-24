---
harness_id: herd
project_name: Herd
repository: https://github.com/NickGuAI/Herd
review_ref: fbda6618c7b53524faddbed070e4fbc14970e412
reviewed_at: 2026-10-17
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: —
---

# Herd

## Review boundary

- System in focus: one supported local Herd v0.0.14-beta Node/TypeScript installation, its packaged model-backed commander/worker operating mode, durable quests, worker/session/machine routing and optional installed skills.
- Purpose and identity: durable mission/task management and present control around multiple external coding-agent provider CLIs and operator-controlled machines.
- Relevant environment: human operator, Git repositories, external model/provider runtime, machines, tool/source/test feedback, operator permissions and network channels.
- Standard-distribution boundary: documented Linux Node web server with bundled commander package, supported configured provider/machine and explicitly used quest/worker interfaces; no credit to a provider's undisclosed internal orchestration.
- Credited operating / distribution surfaces: Asina commander model instructions; first-party quest/worker API and launcher; persisted quest ownership; model session and memory bootstrap; optional supplied engineering-review/debrief skills, shared learnings/guardrails and action approvals.
- Adjacent first-party surfaces excluded from ownership: development `.dev` maps/reviews and tests, public mirrors, release CI, unused/paused automation instances, marketing-only diagrams, external provider CLIs and SSH/Tailscale internals, unsupported provider configurations.
- First-party operating / deployment modes considered: explicitly active model-backed bundled Asina/commander with quest/worker dispatch; multiple owned conversations attempting quest claims; optional packaged review or debrief invoked by a model/user, paused marketplace research automations, single-operator approval modes. Not all active by default.
- Recursion level: one installed Herd commander mission with operational workers and commander conversations; broader institutional/company or Herd OSS maintainer governance excluded.
- Reviewed revision: fbda6618c7b53524faddbed070e4fbc14970e412.
- Observation date: 2026-10-17.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The Herd control plane is an installable Node/TypeScript application. Its model-backed commanders receive a first-party scoped prompt listing quest claim/note/done commands, durable-memory discovery and workflow constraints. Bundled Asina is an engineering management role charged with inspecting source, choosing the next issue/worker and verifying actual Git/test artifacts. `POST /:id/workers` validates commander-scoped dispatch authority and routes to Herd's worker session launcher; the underlying model/provider execution is external, while the commander prompt, session identity, trusted provenance and controller APIs are first-party ([README.md](https://github.com/NickGuAI/Herd/blob/fbda6618c7b53524faddbed070e4fbc14970e412/README.md); [apps/herd/modules/commanders/memory/prompt.ts](https://github.com/NickGuAI/Herd/blob/fbda6618c7b53524faddbed070e4fbc14970e412/apps/herd/modules/commanders/memory/prompt.ts); [apps/herd/modules/commanders/packages/bundled/engineering-manager/COMMANDER.md](https://github.com/NickGuAI/Herd/blob/fbda6618c7b53524faddbed070e4fbc14970e412/apps/herd/modules/commanders/packages/bundled/engineering-manager/COMMANDER.md); [apps/herd/modules/commanders/routes/register-workers.ts](https://github.com/NickGuAI/Herd/blob/fbda6618c7b53524faddbed070e4fbc14970e412/apps/herd/modules/commanders/routes/register-workers.ts); [apps/herd/modules/agents/session/commander-worker-dispatch.ts](https://github.com/NickGuAI/Herd/blob/fbda6618c7b53524faddbed070e4fbc14970e412/apps/herd/modules/agents/session/commander-worker-dispatch.ts)).

Herd's quest store serializes `claimNext` and `claim` across conversations, grants pending quest ownership to one conversation and rejects subsequent claimants with an existing holder. The real quest route publishes conflict `409`, giving a narrow inter-operational disturbance/feedback path rather than generic storage or transport ([apps/herd/modules/commanders/quest-store.ts](https://github.com/NickGuAI/Herd/blob/fbda6618c7b53524faddbed070e4fbc14970e412/apps/herd/modules/commanders/quest-store.ts); [apps/herd/modules/commanders/routes/register-quests.ts](https://github.com/NickGuAI/Herd/blob/fbda6618c7b53524faddbed070e4fbc14970e412/apps/herd/modules/commanders/routes/register-quests.ts)).

The bundled `engineering-review` skill demands direct checks of source, plans or PR changes but the reviewed first-party delegation path does not establish an independent reviewer specifically distinct from the producing worker and ordinary commander verification, followed by binding corrective return. Similarly, `debrief` and shared `LEARNINGS.md` can support knowledge transfer, but packaged research automations start `paused` and the pre-kill debrief endpoint explicitly returns `not-supported-yet`. Neither the S3* audit loop nor S4 outside-and-then adaptation loop is established merely by these facilities ([agent-skills/herd-starter/engineering-review/SKILL.md](https://github.com/NickGuAI/Herd/blob/fbda6618c7b53524faddbed070e4fbc14970e412/agent-skills/herd-starter/engineering-review/SKILL.md); [agent-skills/herd-starter/debrief/SKILL.md](https://github.com/NickGuAI/Herd/blob/fbda6618c7b53524faddbed070e4fbc14970e412/agent-skills/herd-starter/debrief/SKILL.md); [apps/herd/modules/commanders/memory/prompt.ts](https://github.com/NickGuAI/Herd/blob/fbda6618c7b53524faddbed070e4fbc14970e412/apps/herd/modules/commanders/memory/prompt.ts); [apps/herd/modules/commanders/packages/bundled/research-intelligence-analyst/automations.manifest.json](https://github.com/NickGuAI/Herd/blob/fbda6618c7b53524faddbed070e4fbc14970e412/apps/herd/modules/commanders/packages/bundled/research-intelligence-analyst/automations.manifest.json); [apps/herd/modules/agents/routes/session-control-routes.ts](https://github.com/NickGuAI/Herd/blob/fbda6618c7b53524faddbed070e4fbc14970e412/apps/herd/modules/agents/routes/session-control-routes.ts)).

## Operational model

A human installs Herd, configures provider access and machines and uses a bundled commander. The model-backed commander reads its current mission/quests and evidence, chooses scoped work and launches worker sessions using Herd's first-party controls. The provider-backed worker carries out source/research/tool actions, returns status and artifacts, then the commander can issue correction, completion or more work. Two active commander conversations claiming the same quest cannot both own it. This is a source-reachable mode, not an observed production/model run.

## S1 — Operations

- State: A
- Function: carry out model-driven coding, investigation, tests or other delegated task operations through role-scoped commander and workers.
- Disturbance / variety regulated: changing source and requirements, test failures, tool feedback and artifact evidence.
- Decisive decision or feedback right: the active model-backed agent selects contextual next substantive source/tool actions and revises them from operational feedback.
- Decision owner: configured model-backed commander/worker running first-party Herd prompts and tasks; external provider inference is an environmental dependency.
- Supporting / enforcement mechanisms: bundled commander persona/skills, API worker creation, machine selection, session persistence, tool/permission plumbing.
- Closure path: operator/quest task → configured session → model-chosen tool/source/test action → result → iterative work/worker artifact → commander/user.
- Boundary reachability: Asina is bundled, quest prompt and worker route are shipped and reachable when a provider and machine are configured.
- Why this is / is not agent-owned: removing the model leaves stateful Node routing without adaptive task execution.
- Evidence: [apps/herd/modules/commanders/packages/bundled/engineering-manager/COMMANDER.md](https://github.com/NickGuAI/Herd/blob/fbda6618c7b53524faddbed070e4fbc14970e412/apps/herd/modules/commanders/packages/bundled/engineering-manager/COMMANDER.md); [apps/herd/modules/commanders/memory/prompt.ts](https://github.com/NickGuAI/Herd/blob/fbda6618c7b53524faddbed070e4fbc14970e412/apps/herd/modules/commanders/memory/prompt.ts); [apps/herd/modules/agents/worker-launch.ts](https://github.com/NickGuAI/Herd/blob/fbda6618c7b53524faddbed070e4fbc14970e412/apps/herd/modules/agents/worker-launch.ts); [apps/herd/modules/agents/session/commander-worker-dispatch.ts](https://github.com/NickGuAI/Herd/blob/fbda6618c7b53524faddbed070e4fbc14970e412/apps/herd/modules/agents/session/commander-worker-dispatch.ts); [agent-skills/herd-starter/legion-implement/SKILL.md](https://github.com/NickGuAI/Herd/blob/fbda6618c7b53524faddbed070e4fbc14970e412/agent-skills/herd-starter/legion-implement/SKILL.md)
- Basis: explicit first-party execution composition
- Confidence: medium-high, supported mode, not witnessed inference
- Caveats: do not import provider-internal cognition beyond the action loop invoked via shipped model session.

## S2 — Coordination

- State: C
- Function: prevent duplicate/conflicting quest ownership by distinct active operational commander conversations.
- Disturbance / variety regulated: two work-taking S1 conversations simultaneously attempt the same task, causing duplicate execution and contradictory completion.
- Decisive decision or feedback right: serialize pending→active claim and reject competing conversation with holder identity.
- Decision owner: first-party deterministic CommanderQuestStore mutation/claim constructor, not autonomous model S2.
- Supporting / enforcement mechanisms: per-store mutation queue, persisted claimedByConversationId, active state and HTTP 409 for existing claim.
- Closure path: multiple model-backed conversations see pending quest → lock acquisition → one claim saved → other gets 409 and holder → only holder may legitimately act as owner.
- Boundary reachability: shipped quest-next/claim API and bundled commander quest prompt, callable in an installed configured fleet.
- Why this is / is not agent-owned: claim rejection is code owned; a model can choose a quest but cannot override the exclusive claim.
- Evidence: [apps/herd/modules/commanders/quest-store.ts](https://github.com/NickGuAI/Herd/blob/fbda6618c7b53524faddbed070e4fbc14970e412/apps/herd/modules/commanders/quest-store.ts); [apps/herd/modules/commanders/routes/register-quests.ts](https://github.com/NickGuAI/Herd/blob/fbda6618c7b53524faddbed070e4fbc14970e412/apps/herd/modules/commanders/routes/register-quests.ts); [apps/herd/modules/commanders/memory/prompt.ts](https://github.com/NickGuAI/Herd/blob/fbda6618c7b53524faddbed070e4fbc14970e412/apps/herd/modules/commanders/memory/prompt.ts)
- Basis: direct implementation and return-path evidence
- Confidence: high for narrow deterministic mechanism
- Caveats: no claim of universal file/worktree collision prevention.
- Distinct S1 units: separate provider-backed commander conversations that may work from one shared commander quest board.
- Inter-S1 disturbance: parallel claims of a common quest would duplicate operational commitments/work.
- Attenuating coordination relation: serialized first-party ownership transition with binding claim-owner check.
- Feedback into subsequent S1 behaviour: losing claimant receives 409/current holder rather than an active claim, and must choose other work.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: enforces an explicit inter-S1 work-conflict resolution, not simple ordering or messaging.

## S3 — Inside-and-now control

- State: A
- Function: control present work of the local commander mission, allocating workers, task commitments and corrective interventions from current feedback.
- Disturbance / variety regulated: blocked quests, failing workers, misallocated attention, incomplete artifacts and current delivery risk.
- Decisive decision or feedback right: choose which quest to claim and which worker/host/task to dispatch, verify outcomes and choose corrective work, stopping or escalation.
- Decision owner: model-backed bundled commander (Asina) as the current controller; backend claim/routing/policy gates are mechanisms, not its discretionary decisions.
- Supporting / enforcement mechanisms: durable quests, workers/sessions, current Command Room context, worker dispatch API, memory, permission policy.
- Closure path: read active mission, pending tasks and worker source feedback → commander model chooses current priority/assignment → first-party quest/worker action → persisted status/artifacts feed its next decision.
- Boundary reachability: bundled role explicitly responsible for orchestrating workers, verifying code and reporting status; system prompt includes usable quest lifecycle; backend worker route acts.
- Why this is / is not agent-owned: without commander model and its sourced operating role, transport/storage alone cannot choose mission-level priorities or corrective work.
- Evidence: [apps/herd/modules/commanders/packages/bundled/engineering-manager/COMMANDER.md](https://github.com/NickGuAI/Herd/blob/fbda6618c7b53524faddbed070e4fbc14970e412/apps/herd/modules/commanders/packages/bundled/engineering-manager/COMMANDER.md); [apps/herd/modules/commanders/memory/prompt.ts](https://github.com/NickGuAI/Herd/blob/fbda6618c7b53524faddbed070e4fbc14970e412/apps/herd/modules/commanders/memory/prompt.ts); [apps/herd/modules/commanders/routes/register-workers.ts](https://github.com/NickGuAI/Herd/blob/fbda6618c7b53524faddbed070e4fbc14970e412/apps/herd/modules/commanders/routes/register-workers.ts); [docs/concepts/command-room.md](https://github.com/NickGuAI/Herd/blob/fbda6618c7b53524faddbed070e4fbc14970e412/docs/concepts/command-room.md); [docs/concepts/workers.md](https://github.com/NickGuAI/Herd/blob/fbda6618c7b53524faddbed070e4fbc14970e412/docs/concepts/workers.md)
- Basis: first-party shipped model/task workflow, no live execution claim
- Confidence: medium for model-ownership and return source path
- Caveats: not a claim that any server without a model is autonomous or that ordinary user action policy approval creates a separate parent S3.
- Whole-system current view: Asina/commanders can inspect current quests and worker status/outputs across their bounded commander mission.
- Current-control decision scope: choose current resource/worker dispatch, task claims/priorities, recovery, rework and escalating blockers.

## S3* — Complementary audit

- State: ?
- Function: independent audit of producer implementation claims with distinct direct operational evidence access and findings returned into subsequent work.
- Disturbance / variety regulated: worker's reported success diverges from real code, tests, repository and safety constraints.
- Decisive decision or feedback right: a separately selected nonproducer reviewer could judge actual diffs and require corrections; this function-specific decisive actor and closure not established.
- Decision owner: unknown: supplied engineering-review skill can run source review; bundled Asina verifies own workers; neither proves separate independent auditor and binding feedback.
- Supporting / enforcement mechanisms: engineering-review skill, Asina verification instructions, source/Git/test access and worker delegation API.
- Closure path: plausible nonproducer review → findings → commanded rework/re-review, but distinct reviewer invocation and corrective-return binding not traced as an executable first-party lane.
- Boundary reachability: packaged skill exists in bundled engineering-manager package, but its invocation in an actually separate audit run remains unresolved.
- Why this is / is not agent-owned: reviewing one's own worker output as ordinary S3 acceptance is not sufficient for S3* independence.
- Evidence: [agent-skills/herd-starter/engineering-review/SKILL.md](https://github.com/NickGuAI/Herd/blob/fbda6618c7b53524faddbed070e4fbc14970e412/agent-skills/herd-starter/engineering-review/SKILL.md); [apps/herd/modules/commanders/packages/bundled/engineering-manager/skills.manifest.json](https://github.com/NickGuAI/Herd/blob/fbda6618c7b53524faddbed070e4fbc14970e412/apps/herd/modules/commanders/packages/bundled/engineering-manager/skills.manifest.json); [apps/herd/modules/commanders/packages/bundled/engineering-manager/COMMANDER.md](https://github.com/NickGuAI/Herd/blob/fbda6618c7b53524faddbed070e4fbc14970e412/apps/herd/modules/commanders/packages/bundled/engineering-manager/COMMANDER.md); [docs/concepts/workers.md](https://github.com/NickGuAI/Herd/blob/fbda6618c7b53524faddbed070e4fbc14970e412/docs/concepts/workers.md)
- Basis: plausible in-boundary skill path with unresolved independent loop
- Confidence: medium for uncertainty; not positive
- Caveats: no universal mandatory independent review inferred; ? rather than ungrounded A/C or global absence.
- Claim being audited: the producing worker's implementation satisfies task, tests and repository constraints.
- Ordinary reporting path: worker task summary/status and produced artifacts return to commander.
- Complementary access path: review skill directs checking actual source/PR/architecture evidence rather than only relying on worker prose.
- Independence boundary: distinct reviewer model ownership not demonstrably established by default or selected completed mode.
- Who acts on findings: commander/user could assign rework, but this corrective path is not shown as a complete review-specific binding loop.

## S4 — Outside-and-then intelligence

- State: ?
- Function: propose future adaptation from changed outside reality and return accepted changes into later commander capability.
- Disturbance / variety regulated: stale operating doctrine, recurring errors, new domain research and changed external project conditions.
- Decisive decision or feedback right: authorize, select and effect a durable forward-looking change in future operating rules/capabilities; decisive authority unresolved.
- Decision owner: not established: optional debrief may propose lessons, a human or agent can edit knowledge, but no closed first-party adaptation judgment and actual adoption path is demonstrated.
- Supporting / enforcement mechanisms: debrief skill, LEARNINGS/DOCTRINES shared knowledge, prompt bootstrap and paused research-distill/backlog automations.
- Closure path: plausible correction/research → debrief candidate → authorized durable lesson update → later session reads it, but the source does not establish the full operational loop; pre-kill debrief explicitly returns not-supported-yet.
- Boundary reachability: all named pieces are shipped but meaningful S4 adaptation depends on unproven selection/writing/return, and preconfigured automations are paused.
- Why this is / is not agent-owned: routine memory persistence or changing docs is not itself an autonomous S4 or parent-governed adaptation decision.
- Evidence: [agent-skills/herd-starter/debrief/SKILL.md](https://github.com/NickGuAI/Herd/blob/fbda6618c7b53524faddbed070e4fbc14970e412/agent-skills/herd-starter/debrief/SKILL.md); [apps/herd/modules/commanders/memory/prompt.ts](https://github.com/NickGuAI/Herd/blob/fbda6618c7b53524faddbed070e4fbc14970e412/apps/herd/modules/commanders/memory/prompt.ts); [apps/herd/runtime/defaults/shared-knowledge/LEARNINGS.md](https://github.com/NickGuAI/Herd/blob/fbda6618c7b53524faddbed070e4fbc14970e412/apps/herd/runtime/defaults/shared-knowledge/LEARNINGS.md); [apps/herd/modules/commanders/packages/bundled/research-intelligence-analyst/automations.manifest.json](https://github.com/NickGuAI/Herd/blob/fbda6618c7b53524faddbed070e4fbc14970e412/apps/herd/modules/commanders/packages/bundled/research-intelligence-analyst/automations.manifest.json); [apps/herd/modules/agents/routes/session-control-routes.ts](https://github.com/NickGuAI/Herd/blob/fbda6618c7b53524faddbed070e4fbc14970e412/apps/herd/modules/agents/routes/session-control-routes.ts)
- Basis: specific plausible in-scope source path with material closure gap
- Confidence: medium for unresolved state
- Caveats: no positive S4 state from labels, debrief template or prospect-only command.
- External distinction: candidate lessons can stem from new user corrections, outside research or changing repositories rather than active turn state.
- Future / prospective distinction: a curated durable rule would change subsequent tasks rather than immediately retry a failed action.
- Adaptation option generated: debrief/research-distill can report recommended lessons or future domain updates.
- Path back into current capability / S3: commander prompt references shared learnings, but effectful rule update and subsequent S3 integration remain materially unverified.

## S5 — Identity and ultimate policy

- State: —
- Function: no distinct first-party whole-fleet ultimate identity/ethos policy settlement and binding normative return established.
- Disturbance / variety regulated: fundamental policy/mission tensions rather than individual tool/action risk.
- Decisive decision or feedback right: a legitimate ultimate-authority judgment on system identity/ethos with governing return would be required, but not identified.
- Decision owner: single operator can edit commander identity/doctrines and approve an action, not thereby shown to close S5.
- Supporting / enforcement mechanisms: org display/identity, static doctrines, policy gate, human approvals, commander prompt configuration.
- Closure path: identity/permission constraints reach operations, but not via a separate S5 dispute → ultimate authority decision → normative governing return loop.
- Boundary reachability: inspected shipped single-operator org/approval/identity/command prompt, not broad institution governance.
- Why this is / is not agent-owned: no model whole-system S5 choice or legitimate independent parent S5 mode established.
- Evidence: [docs/concepts/org.md](https://github.com/NickGuAI/Herd/blob/fbda6618c7b53524faddbed070e4fbc14970e412/docs/concepts/org.md); [docs/concepts/approvals.md](https://github.com/NickGuAI/Herd/blob/fbda6618c7b53524faddbed070e4fbc14970e412/docs/concepts/approvals.md); [apps/herd/modules/policies/action-policy-gate.ts](https://github.com/NickGuAI/Herd/blob/fbda6618c7b53524faddbed070e4fbc14970e412/apps/herd/modules/policies/action-policy-gate.ts); [apps/herd/runtime/defaults/shared-knowledge/DOCTRINES.md](https://github.com/NickGuAI/Herd/blob/fbda6618c7b53524faddbed070e4fbc14970e412/apps/herd/runtime/defaults/shared-knowledge/DOCTRINES.md); [apps/herd/modules/commanders/memory/prompt.ts](https://github.com/NickGuAI/Herd/blob/fbda6618c7b53524faddbed070e4fbc14970e412/apps/herd/modules/commanders/memory/prompt.ts)
- Basis: bounded negative at supported local fleet recursion
- Confidence: medium-high
- Caveats: an external deploying organization may own S5 outside Herd, which is not transferred into this assessment.

### Absence scope

- Surfaces inspected: first-party organization/commander identity and prompts, single-operator approvals, action policy, doctrines, packaged configurable skills.
- Plausible first-party paths checked: changing commander roles/identity, policy approvals, operator authority, shared doctrine updates and long-term adaptation tension.
- Why no material first-party path remains: configuration and operational safety gates do not identify a separate ultimate policy dispute and legitimate settlement with binding first-party return at this local fleet boundary.

## Evidence gaps

- First-party source/packaged supported modes inspected at exact review ref, not live model action traces, production outcome claims or evaluator truth.
- Multiple agent conversations and quest conflicts are a conditional supported operating mode, not proof of actual external simultaneous collisions.
- S2=C applies narrowly to quest owner conflicts, not scheduling alone, file writes or inter-machine network variety.
- S3=A rests on a configured bundled commander model making work decisions with first-party available APIs; plain deterministic server/worker sessions do not supply it.
- S3* remains `?`: separate reviewer skill exists, but the independently owned audit-to-correction loop and mandatory/conditional distinct actor are not demonstrated.
- S4 remains `?`: plausible learning/curation exists but paused automations and a debrief stub do not demonstrate full adaptation closure.
- S5=— is a bounded absence statement about Herd's single-operator first-party mission, not a claim about a deploying institution or maintainer project.

## Conclusion

**Canonical general assessment.** The source-supported qualified mapping is `S1=A / S2=C / S3=A / S3*=? / S4=? / S5=—`. Executing model-backed commanders/workers comprise S1; exclusive active quest claims attenuate duplicate inter-S1 work (S2=C); a configured model commander controls present quest and worker commitments (S3=A). Separate audit and prospective adaptation closure are unresolved at the declared boundary; identity and ordinary approval controls do not establish S5.

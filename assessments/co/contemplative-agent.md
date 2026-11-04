---
harness_id: contemplative-agent
project_name: Contemplative Agent
repository: https://github.com/shimo4228/contemplative-agent
review_ref: 46ab9fc09ce62ce1a73364e055f82fc7b13043c7
reviewed_at: 2026-11-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: P
autonomy_s5: P
---

# Contemplative Agent

## Review boundary

- System in focus: One installed Contemplative Agent social actor together with its supported experience-distillation and human adoption cycle.
- Purpose and identity: Autonomous social participation with a local model and legible, owner-governed evolution of behavioral skills, identity and constitutional principles.
- Relevant environment: Other agents/posts, social interaction contexts, platform responses, local inference and the legitimate owner deciding value changes.
- Standard-distribution boundary: Python run/distill/insight/distill-identity/amend-constitution/adopt-staged commands, shipped prompts, stores and documented scheduled/manual modes.
- Credited operating / distribution surfaces: Moltbook actor and LLM prompting; episode→pattern→skill proposals; identity/constitution proposals; explicit adoption and live prompt consumption.
- Adjacent first-party surfaces excluded from ownership: Weekly developer Claude Code sessions, research instruments, eval judges, mirrors, CI and repository-development governance are outside this social-runtime boundary. Read-only diagnostics corroborate without supplying a corrective audit actor.
- First-party operating / deployment modes considered: Interactive APPROVE, GUARDED/AUTO social sessions, launchd scheduling, direct/staged distillation and interactive/named/batch owner adoption; dialogue/meditation inspected for alternate ownership.
- Recursion level: One social actor and its behavioral harness under its local owner; platform peers and research-program agents are external.
- Reviewed revision: 46ab9fc09ce62ce1a73364e055f82fc7b13043c7
- Observation date: 2026-11-04
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

The Python core separates local-model prompting and durable episode/pattern/skill/value stores from the Moltbook adapter. The adapter owns relevance/content selection, publication, API readback, pacing and outcome recording. Supported CLI commands distill world/action episodes, propose reusable skills or identity/constitutional revisions, stage them and adopt owner-selected items. Live prompt builders consume identity, axioms, skills and rules. Research instruments, weekly developer sessions and eval judges are substantial adjacent surfaces but do not supply owners inside the assessed social actor.

## Operational model

The local model owns S1 social decisions. Two supported owner-governed returns are separately established: outside-interaction-derived future practices into behavioral capability (S4=P), and identity/constitutional proposals into governing principles (S5=P). Model authorship of a proposal does not own the adoption verdict. Pacing and routine verification remain operational support.

## S1 — Operations

- State: A
- Function: Select socially relevant material and produce context-sensitive posts, replies and actions in the environment.
- Disturbance / variety regulated: Changing feed/replies, novelty/relevance, duplicate content, API errors and rate limits.
- Decisive decision or feedback right: Model-backed relevance/content/skill judgments determine the next social response from observations.
- Decision owner: First-party local-model social actor in supported AUTO/GUARDED modes.
- Supporting / enforcement mechanisms: Moltbook client, rate scheduler, deduplication, filters, optional action confirmation and durable episodes.
- Closure path: External feed/replies → model selection/generation → allowed action → outcome/episode records → later cycles and experience input.
- Boundary reachability: The shipped run command invokes MoltbookAgent.run_session and its wired managers/LLM functions; autonomous action modes are explicitly supported.
- Why this is / is not agent-owned: Without model judgments the remaining pacing/filter mechanics cannot choose contextual responses. APPROVE mode retains human outward-action gating alongside the separate autonomous mode.
- Evidence: [src/contemplative_agent/adapters/moltbook/agent.py](https://github.com/shimo4228/contemplative-agent/blob/46ab9fc09ce62ce1a73364e055f82fc7b13043c7/src/contemplative_agent/adapters/moltbook/agent.py); [src/contemplative_agent/adapters/moltbook/llm_functions.py](https://github.com/shimo4228/contemplative-agent/blob/46ab9fc09ce62ce1a73364e055f82fc7b13043c7/src/contemplative_agent/adapters/moltbook/llm_functions.py); [src/contemplative_agent/core/skill_selection.py](https://github.com/shimo4228/contemplative-agent/blob/46ab9fc09ce62ce1a73364e055f82fc7b13043c7/src/contemplative_agent/core/skill_selection.py); [README.md](https://github.com/shimo4228/contemplative-agent/blob/46ab9fc09ce62ce1a73364e055f82fc7b13043c7/README.md)
- Basis: explicit and structural
- Confidence: high
- Caveats: No live platform/model session or published longitudinal adoption count was independently reproduced.

## S2 — Coordination

- State: —
- Function: No material first-party inter-S1 coordination path at the declared supported boundary.
- Disturbance / variety regulated: Multiple action paths/components of one actor, rather than evidenced distinct interacting S1 cells.
- Decisive decision or feedback right: No qualifying function-level decision/feedback right reconstructed after checking supported positive and eligible parent modes.
- Decision owner: No qualifying owner at this function; narrower operational or configuration choices remain as described.
- Supporting / enforcement mechanisms: Post/reply pacing, rate constraints, deduplication, dialogue and staging locks.
- Closure path: No function-specific returned closure is supplied by the checked paths.
- Why this is / is not agent-owned: Action managers are components of one S1. Rate limits, artifact-producer locks and content deduplication stabilize local actions or staging. Dialogue peers exchange content without an evidenced conflict-attenuation relation among operational units. No S2-specific autonomous or constructor path remains at the declared recursion.
- Evidence: [src/contemplative_agent/adapters/moltbook/agent.py](https://github.com/shimo4228/contemplative-agent/blob/46ab9fc09ce62ce1a73364e055f82fc7b13043c7/src/contemplative_agent/adapters/moltbook/agent.py); [src/contemplative_agent/adapters/moltbook/session_context.py](https://github.com/shimo4228/contemplative-agent/blob/46ab9fc09ce62ce1a73364e055f82fc7b13043c7/src/contemplative_agent/adapters/moltbook/session_context.py); [src/contemplative_agent/core/scheduler.py](https://github.com/shimo4228/contemplative-agent/blob/46ab9fc09ce62ce1a73364e055f82fc7b13043c7/src/contemplative_agent/core/scheduler.py); [src/contemplative_agent/cli/staging.py](https://github.com/shimo4228/contemplative-agent/blob/46ab9fc09ce62ce1a73364e055f82fc7b13043c7/src/contemplative_agent/cli/staging.py); [README.md](https://github.com/shimo4228/contemplative-agent/blob/46ab9fc09ce62ce1a73364e055f82fc7b13043c7/README.md)
- Basis: structural bounded absence
- Confidence: medium-high
- Caveats: A custom external organization could add the function; hypothetical extensions are outside this assessment.

### Absence scope

- Surfaces inspected: src/contemplative_agent/adapters/moltbook/agent.py, src/contemplative_agent/adapters/moltbook/session_context.py, src/contemplative_agent/core/scheduler.py, src/contemplative_agent/cli/staging.py, README.md
- Plausible first-party paths checked: Post/reply pacing, rate constraints, deduplication, dialogue and staging locks.
- Why no material first-party path remains: Action managers are components of one S1. Rate limits, artifact-producer locks and content deduplication stabilize local actions or staging. Dialogue peers exchange content without an evidenced conflict-attenuation relation among operational units. No S2-specific autonomous or constructor path remains at the declared recursion.

## S3 — Inside-and-now control

- State: —
- Function: No material first-party whole-system current control path at the declared supported boundary.
- Disturbance / variety regulated: Current action pacing, flags and stop conditions constrain one session operationally.
- Decisive decision or feedback right: No qualifying function-level decision/feedback right reconstructed after checking supported positive and eligible parent modes.
- Decision owner: No qualifying owner at this function; narrower operational or configuration choices remain as described.
- Supporting / enforcement mechanisms: Duration/autonomy flags, fixed rate limits, shutdown/verification stops, following maintenance, scheduling and activity reports.
- Closure path: No function-specific returned closure is supplied by the checked paths.
- Why this is / is not agent-owned: These paths enforce preset limits or individual action permissions, rather than a whole-system commitment/resource bargaining or intervention decision loop. Reports and editable flags alone do not establish parent S3. Behavioral adoption and constitutional decisions are mapped separately below; adjacent research/development control is not borrowed.
- Evidence: [src/contemplative_agent/adapters/moltbook/agent.py](https://github.com/shimo4228/contemplative-agent/blob/46ab9fc09ce62ce1a73364e055f82fc7b13043c7/src/contemplative_agent/adapters/moltbook/agent.py); [src/contemplative_agent/core/scheduler.py](https://github.com/shimo4228/contemplative-agent/blob/46ab9fc09ce62ce1a73364e055f82fc7b13043c7/src/contemplative_agent/core/scheduler.py); [src/contemplative_agent/cli/session_cmds.py](https://github.com/shimo4228/contemplative-agent/blob/46ab9fc09ce62ce1a73364e055f82fc7b13043c7/src/contemplative_agent/cli/session_cmds.py); [src/contemplative_agent/cli/schedule.py](https://github.com/shimo4228/contemplative-agent/blob/46ab9fc09ce62ce1a73364e055f82fc7b13043c7/src/contemplative_agent/cli/schedule.py); [README.md](https://github.com/shimo4228/contemplative-agent/blob/46ab9fc09ce62ce1a73364e055f82fc7b13043c7/README.md)
- Basis: structural bounded absence
- Confidence: medium-high
- Caveats: A custom external organization could add the function; hypothetical extensions are outside this assessment.

### Absence scope

- Surfaces inspected: src/contemplative_agent/adapters/moltbook/agent.py, src/contemplative_agent/core/scheduler.py, src/contemplative_agent/cli/session_cmds.py, src/contemplative_agent/cli/schedule.py, README.md
- Plausible first-party paths checked: Duration/autonomy flags, fixed rate limits, shutdown/verification stops, following maintenance, scheduling and activity reports.
- Why no material first-party path remains: These paths enforce preset limits or individual action permissions, rather than a whole-system commitment/resource bargaining or intervention decision loop. Reports and editable flags alone do not establish parent S3. Behavioral adoption and constitutional decisions are mapped separately below; adjacent research/development control is not borrowed.

## S3* — Complementary audit

- State: —
- Function: No material first-party complementary audit path at the declared supported boundary.
- Disturbance / variety regulated: Actions, drift and learned artifacts can be logged, measured and verified.
- Decisive decision or feedback right: No qualifying function-level decision/feedback right reconstructed after checking supported positive and eligible parent modes.
- Decision owner: No qualifying owner at this function; narrower operational or configuration choices remain as described.
- Supporting / enforcement mechanisms: Posting readback, episode/audit logs, distance/shadow instruments, novelty/duplicate judges and the research/eval boundary.
- Closure path: No function-specific returned closure is supplied by the checked paths.
- Why this is / is not agent-owned: Posting readback is routine S1 verification. Drift/shadow instruments are explicitly read-only and do not supply a separate complementary audit judgment with a corrective return into control. Novelty judges are part of proposal production. Developer/eval agents belong to the adjacent research program.
- Evidence: [src/contemplative_agent/adapters/moltbook/verification.py](https://github.com/shimo4228/contemplative-agent/blob/46ab9fc09ce62ce1a73364e055f82fc7b13043c7/src/contemplative_agent/adapters/moltbook/verification.py); [src/contemplative_agent/core/identity_drift.py](https://github.com/shimo4228/contemplative-agent/blob/46ab9fc09ce62ce1a73364e055f82fc7b13043c7/src/contemplative_agent/core/identity_drift.py); [src/contemplative_agent/core/constitution_shadow.py](https://github.com/shimo4228/contemplative-agent/blob/46ab9fc09ce62ce1a73364e055f82fc7b13043c7/src/contemplative_agent/core/constitution_shadow.py); [src/contemplative_agent/cli/approval.py](https://github.com/shimo4228/contemplative-agent/blob/46ab9fc09ce62ce1a73364e055f82fc7b13043c7/src/contemplative_agent/cli/approval.py); [README.md](https://github.com/shimo4228/contemplative-agent/blob/46ab9fc09ce62ce1a73364e055f82fc7b13043c7/README.md)
- Basis: structural bounded absence
- Confidence: medium-high
- Caveats: A custom external organization could add the function; hypothetical extensions are outside this assessment.

### Absence scope

- Surfaces inspected: src/contemplative_agent/adapters/moltbook/verification.py, src/contemplative_agent/core/identity_drift.py, src/contemplative_agent/core/constitution_shadow.py, src/contemplative_agent/cli/approval.py, README.md
- Plausible first-party paths checked: Posting readback, episode/audit logs, distance/shadow instruments, novelty/duplicate judges and the research/eval boundary.
- Why no material first-party path remains: Posting readback is routine S1 verification. Drift/shadow instruments are explicitly read-only and do not supply a separate complementary audit judgment with a corrective return into control. Novelty judges are part of proposal production. Developer/eval agents belong to the adjacent research program.

## S4 — Outside-and-then intelligence

- State: P
- Function: Develop future behavioral adaptation options from externally situated social experience, with parent adoption into present capability.
- Disturbance / variety regulated: Recurring differences in outside interactions that the current behavioral repertoire does not adequately distinguish.
- Decisive decision or feedback right: Accept/reject newly proposed reusable practices for the live skill repertoire.
- Decision owner: Legitimate local human owner; the local model develops candidate options but does not own their authoritative adoption.
- Supporting / enforcement mechanisms: Episodes/patterns, clusters, novelty and nearest-skill comparison, staging, adoption records and runtime skill/prompt loading.
- Closure path: Social-world episode → grounded patterns → insight generates reusable conditions/actions for future episodes → owner adopts selected candidate → live skills store changes → later prompt/skill selection uses it. Current store skills feed novelty/duplicate comparisons back into option generation.
- Boundary reachability: distill/insight --stage and adopt-staged are shipped commands; the same installation consumes adopted skills during ordinary social operation. The separate weekly research agent is not required for this manual cycle.
- Why this is / is not agent-owned: The witness includes explicit world-grounded input, future reusable practices and actual returned capability change; memory alone is not credited. The owner retains the decisive adaptation choice, so no A or autonomous C base is asserted.
- External distinction: The episode prompt explicitly preserves what other agents/posts presented, the actor response and what the interaction revealed.
- Future / prospective distinction: The insight prompt requires recurring structural triggers reusable across future episodes, removing transient post/user/time identifiers.
- Adaptation option generated: A proposed skill specifying what the actor does in those recurring situations, compared with its existing repertoire.
- Path back into current capability / S3: Owner adoption writes live skills; prompting/selection consumes them in later social decisions. This is bounded behavioral adaptation, not an inferred autonomous resource controller.
- Evidence: [config/prompts/distill_episode.md](https://github.com/shimo4228/contemplative-agent/blob/46ab9fc09ce62ce1a73364e055f82fc7b13043c7/config/prompts/distill_episode.md); [config/prompts/insight_extraction.md](https://github.com/shimo4228/contemplative-agent/blob/46ab9fc09ce62ce1a73364e055f82fc7b13043c7/config/prompts/insight_extraction.md); [src/contemplative_agent/core/insight.py](https://github.com/shimo4228/contemplative-agent/blob/46ab9fc09ce62ce1a73364e055f82fc7b13043c7/src/contemplative_agent/core/insight.py); [src/contemplative_agent/cli/memory_cmds.py](https://github.com/shimo4228/contemplative-agent/blob/46ab9fc09ce62ce1a73364e055f82fc7b13043c7/src/contemplative_agent/cli/memory_cmds.py); [src/contemplative_agent/cli/adopt.py](https://github.com/shimo4228/contemplative-agent/blob/46ab9fc09ce62ce1a73364e055f82fc7b13043c7/src/contemplative_agent/cli/adopt.py); [src/contemplative_agent/core/llm/prompting.py](https://github.com/shimo4228/contemplative-agent/blob/46ab9fc09ce62ce1a73364e055f82fc7b13043c7/src/contemplative_agent/core/llm/prompting.py); [src/contemplative_agent/core/skill_selection.py](https://github.com/shimo4228/contemplative-agent/blob/46ab9fc09ce62ce1a73364e055f82fc7b13043c7/src/contemplative_agent/core/skill_selection.py)
- Basis: explicit and structural parent-governed adaptation
- Confidence: medium
- Caveats: S4 is limited to outside-interaction-derived future behavioral practices; introspection, weights, provider optimization and unobserved strategic research are not credited. Effectiveness or beneficial direction is unproven.

## S5 — Policy and identity

- State: P
- Function: Maintain/revise actor identity and ultimate constitutional principles under legitimate owner authority.
- Disturbance / variety regulated: Experience reveals identity drift/misalignment or proposed changes to ethical principles.
- Decisive decision or feedback right: Authoritatively approve/reject identity revisions and constitutional amendments for the governing value layer.
- Decision owner: Local human owner. Named-file and explicit --yes channels encode gate decisions, not a separately established autonomous ultimate authority.
- Supporting / enforcement mechanisms: Proposal generation, snapshots/lineage, staged sidecars, approval audit, target-specific replacement and prompt reload.
- Closure path: Experience-grounded identity/constitutional proposal → direct/staged owner review → logged authoritative verdict → accepted live identity.md/constitution replacement → subsequent prompts load the adopted self-description/principles.
- Boundary reachability: Proposal, adoption and canonical-target replacement ship in the same installation, and first-party domain/prompt builders consume the resulting live artifacts. This is a function-specific value governance flow rather than mere file editability or task approval.
- Why this is / is not agent-owned: The model proposes, but the owner decides adoption in the supported human-governed cycle. The returned parent verdict changes actual governing prompts.
- Identity / ultimate-policy issue: Who the actor is and which ethical principles govern it, distinguished from operational skills or individual post approval.
- Ultimate authority in each claimed mode: Legitimate owner through direct/staged approval, named adoption or explicitly selected batch acceptance; no autonomous ultimate-policy mode established.
- Return-to-operation path: adopt-staged replaces the intended identity/constitution artifact; later model prompting reads the live governing content.
- Evidence: [src/contemplative_agent/core/constitution.py](https://github.com/shimo4228/contemplative-agent/blob/46ab9fc09ce62ce1a73364e055f82fc7b13043c7/src/contemplative_agent/core/constitution.py); [config/prompts/constitution_amend.md](https://github.com/shimo4228/contemplative-agent/blob/46ab9fc09ce62ce1a73364e055f82fc7b13043c7/config/prompts/constitution_amend.md); [config/prompts/identity_distill.md](https://github.com/shimo4228/contemplative-agent/blob/46ab9fc09ce62ce1a73364e055f82fc7b13043c7/config/prompts/identity_distill.md); [src/contemplative_agent/cli/memory_cmds.py](https://github.com/shimo4228/contemplative-agent/blob/46ab9fc09ce62ce1a73364e055f82fc7b13043c7/src/contemplative_agent/cli/memory_cmds.py); [src/contemplative_agent/cli/approval.py](https://github.com/shimo4228/contemplative-agent/blob/46ab9fc09ce62ce1a73364e055f82fc7b13043c7/src/contemplative_agent/cli/approval.py); [src/contemplative_agent/cli/adopt.py](https://github.com/shimo4228/contemplative-agent/blob/46ab9fc09ce62ce1a73364e055f82fc7b13043c7/src/contemplative_agent/cli/adopt.py); [src/contemplative_agent/core/domain.py](https://github.com/shimo4228/contemplative-agent/blob/46ab9fc09ce62ce1a73364e055f82fc7b13043c7/src/contemplative_agent/core/domain.py); [src/contemplative_agent/core/llm/prompting.py](https://github.com/shimo4228/contemplative-agent/blob/46ab9fc09ce62ce1a73364e055f82fc7b13043c7/src/contemplative_agent/core/llm/prompting.py); [README.md](https://github.com/shimo4228/contemplative-agent/blob/46ab9fc09ce62ce1a73364e055f82fc7b13043c7/README.md)
- Basis: explicit and structural parent-governed policy closure
- Confidence: high
- Caveats: This changes attitudinal/value prompts, not code-enforced network/security permissions. Parent governance does not grant model ultimate authority.

## Distributed OSS parent arrangement

Parent witnesses are local to the legitimate owner of an installed actor. Public maintainers, contributors, social peers and research agents are not combined into organization-level parent authority.

## Self-hosted and non-human modes

Local inference and scheduled AUTO/GUARDED actions coexist with human-governed skill/value adoption. Outward-action autonomy does not transfer adoption or constitutional authority. Dialogue/meditation modes do not establish autonomous ultimate-policy closure.

## Recursion

Content, reply, scheduler and memory managers decompose one actor. Social peers are environment participants and the research/development program is adjacent, rather than recursively viable S1 cells owned by this actor.

## Variety and escalation

World/action episodes retain experience. Selection, filters, pacing, retries and graceful stops handle local disturbances. Behavioral and constitutional proposals use distinct owner adoption channels; rejection leaves a candidate out, while adoption returns the chosen change into later operation. This does not guarantee favorable long-term value evolution.

## Evidence gaps

No Ollama/platform execution, longitudinal adoption count or research-program evaluation was reproduced. S4 is deliberately narrower and less certain than S5: the source witnesses future reusable practices grounded in outside interaction, not infrastructure strategy or introspective memory alone. Negative findings are bounded by the social-runtime and supported value-cycle partition above.

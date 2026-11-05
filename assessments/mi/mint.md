---
harness_id: mint
project_name: mint
repository: https://github.com/ketiyohannes/mint
review_ref: 0f98e1b4a17f9b73aabc6f8789e604d5902d648d
reviewed_at: 2026-11-05
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# mint

## Review boundary

- System in focus: the first-party local tutoring application and its supported model-backed teaching composition, one learner/class operational boundary.
- Purpose and identity: turn learner materials and demonstrated understanding into grounded explanations, practice, checks and durable learning records.
- Relevant environment: learner questions/answers, local and imported source materials, trusted web domains, model services and sandboxed exercise execution.
- Standard-distribution boundary: Electron main services, job prompts/schemas, learning rules, local store, renderer/preload and supported Claude/Codex adapters.
- Credited operating / distribution surfaces: `src/main/services/{chat,setup,intake,sessions,threads,kernel}.ts`, `src/main/jobs/`, `src/main/learning/`, `src/main/agents/` and their wired application entry. The concrete teaching composition supplies the operational outcome; SDK internals are dependencies.
- Adjacent first-party surfaces excluded from ownership: scripted Demo mode, fixtures, tests, screenshots, release CI and development tooling; these can demonstrate wiring but do not supply autonomous decision ownership.
- First-party operating / deployment modes considered: local Claude Agent SDK composition (bundled agent, explicit read/web allowlist), Codex app-server composition (ephemeral read-only turns), and Demo as a non-agentic contrast. No live model run was performed.
- Recursion level: one tutoring product/class cell; not the learner's wider educational institution or the repository's maintainer organization.
- Reviewed revision: `0f98e1b4a17f9b73aabc6f8789e604d5902d648d`.
- Observation date: 2026-11-05.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

[README.md](https://github.com/ketiyohannes/mint/blob/0f98e1b4a17f9b73aabc6f8789e604d5902d648d/README.md) describes the Electron/React local product. The main process owns classes, source imports, curriculum, sessions, anchored side threads, notes and atomic JSON persistence. [src/main/services/chat.ts](https://github.com/ketiyohannes/mint/blob/0f98e1b4a17f9b73aabc6f8789e604d5902d648d/src/main/services/chat.ts) routes intake, chat and lesson/quiz/code/diagram requests. [src/main/services/setup.ts](https://github.com/ketiyohannes/mint/blob/0f98e1b4a17f9b73aabc6f8789e604d5902d648d/src/main/services/setup.ts) calls curriculum proposal/application; [src/main/services/sessions.ts](https://github.com/ketiyohannes/mint/blob/0f98e1b4a17f9b73aabc6f8789e604d5902d648d/src/main/services/sessions.ts) generates briefs/checks, sends learner answers to a model judge, records attempts, and applies deterministic mastery/review rules from [src/main/learning/engine.ts](https://github.com/ketiyohannes/mint/blob/0f98e1b4a17f9b73aabc6f8789e604d5902d648d/src/main/learning/engine.ts). [src/main/services/threads.ts](https://github.com/ketiyohannes/mint/blob/0f98e1b4a17f9b73aabc6f8789e604d5902d648d/src/main/services/threads.ts) constructs grounded tutor requests, streams replies and changes the help rung from learner requests and recorded evidence.

[src/main/jobs/index.ts](https://github.com/ketiyohannes/mint/blob/0f98e1b4a17f9b73aabc6f8789e604d5902d648d/src/main/jobs/index.ts) defines the actual teaching jobs; [src/main/jobs/run.ts](https://github.com/ketiyohannes/mint/blob/0f98e1b4a17f9b73aabc6f8789e604d5902d648d/src/main/jobs/run.ts) validates structured answers and returns validation errors for a bounded retry. [src/main/agents/claude.ts](https://github.com/ketiyohannes/mint/blob/0f98e1b4a17f9b73aabc6f8789e604d5902d648d/src/main/agents/claude.ts) configures SDK tools, class-folder and trusted-domain hooks, model and turn limits; [src/main/agents/codex/runtime.ts](https://github.com/ketiyohannes/mint/blob/0f98e1b4a17f9b73aabc6f8789e604d5902d648d/src/main/agents/codex/runtime.ts) supplies the separate Codex transport. These libraries/CLIs are not treated as donors of unexamined VSM functions. Human actions initiate study, supply goals/sources, ask for more help and accept proposed records. Maintainer release CI and headless Demo tests are outside this operating cell.

## Operational model

The S1 outcome is grounded tutoring and evidence-based learning feedback, not merely a graphical client for external coding agents. Repository-owned jobs decide explanation, curriculum content, misconception judgments and practice artifacts; services apply those outputs to later learner interactions. File/network tools and deterministic schemas constrain the agent. A learner remains responsible for studying and accepting records; that does not remove the model's substantive tutoring discretion. Concurrent chat/lesson calls are facets of this teaching cell, not an evidenced portfolio of autonomous operational organizations.

## S1 — Operations

- State: A
- Function: produce context-sensitive tutoring, exercises and judgments of demonstrated understanding.
- Disturbance / variety regulated: different materials, questions, wrong/partial learner answers and requests for additional help.
- Decisive decision or feedback right: choose grounded explanation/practice content and judge an answer against materials; propose a curriculum or session wrap within the teaching contract.
- Decision owner: model-backed tutor instantiated by the first-party job composition; learner owns goals and acceptance, code owns state transitions and safety limits.
- Supporting / enforcement mechanisms: SDK/app-server transport, folder/domain hooks, schemas and retry, topic-progress rules, JSON store, UI and exercise sandbox.
- Closure path: learner answer → `judgeCheck` → validated verdict/feedback → `submitCheck` stores attempts and updates progress; next session/thread consumes refreshed context. `tutorReply` returns a grounded response into the continuing thread.
- Boundary reachability: shipped ChatService/SessionService invoke the owned jobs through Kernel.runtime; the Claude/Codex adapters provide the configured execution seam. No development agent is borrowed.
- Why this is / is not agent-owned: without the model actor, transport, allowlists and progress rules cannot choose the same explanations or misconception verdicts; Demo is explicitly scripted and is not the credited mode.
- Evidence: [src/main/jobs/index.ts](https://github.com/ketiyohannes/mint/blob/0f98e1b4a17f9b73aabc6f8789e604d5902d648d/src/main/jobs/index.ts); [src/main/services/sessions.ts](https://github.com/ketiyohannes/mint/blob/0f98e1b4a17f9b73aabc6f8789e604d5902d648d/src/main/services/sessions.ts); [src/main/services/threads.ts](https://github.com/ketiyohannes/mint/blob/0f98e1b4a17f9b73aabc6f8789e604d5902d648d/src/main/services/threads.ts); [src/main/agents/claude.ts](https://github.com/ketiyohannes/mint/blob/0f98e1b4a17f9b73aabc6f8789e604d5902d648d/src/main/agents/claude.ts).
- Basis: structural.
- Confidence: high for implemented ownership/wiring; no claim of learning efficacy.
- Caveats: provider access and a real model are required; learner activity drives the sessions and accepted records.

## S2 — Coordination

- State: —
- Function: no material first-party path for interference among independent S1 tutoring units at the declared boundary.
- Disturbance / variety regulated: the candidate distinction is interference among independent S1 tutoring units; observed nearby mechanisms are assessed below.
- Decisive decision or feedback right: no function-specific decisive right with the required closure established.
- Decision owner: no qualifying owner identified for this function; learner/model/developer ownership of ordinary teaching remains as described.
- Supporting / enforcement mechanisms: `src/main/services/setup.ts`, `src/main/services/threads.ts`, `src/main/services/sessions.ts`.
- Closure path: Concurrent class planning, per-class locks and fresh-state merges prevent duplicate jobs or lost updates, but the reviewed cell exposes one tutor through several service facets. No specific inter-S1 mutual-adjustment relation is established by these storage primitives.
- Why this is / is not agent-owned: no positive functional witness is supplied by the inspected alternatives, so agent/constructor/parent ownership is not inferred.
- Evidence: [src/main/services/setup.ts](https://github.com/ketiyohannes/mint/blob/0f98e1b4a17f9b73aabc6f8789e604d5902d648d/src/main/services/setup.ts); [src/main/services/threads.ts](https://github.com/ketiyohannes/mint/blob/0f98e1b4a17f9b73aabc6f8789e604d5902d648d/src/main/services/threads.ts); [src/main/services/sessions.ts](https://github.com/ketiyohannes/mint/blob/0f98e1b4a17f9b73aabc6f8789e604d5902d648d/src/main/services/sessions.ts).
- Basis: structural.
- Confidence: medium-high, bounded to the supplied distribution.
- Caveats: custom integrations or a wider institution could add this function; that possibility is not evidence of a shipped path.

### Absence scope

- Surfaces inspected: `src/main/services/setup.ts`, `src/main/services/threads.ts`, `src/main/services/sessions.ts`, application README, job/runtime composition and the supported learner interactions.
- Plausible first-party paths checked: Concurrent class planning, per-class locks and fresh-state merges prevent duplicate jobs or lost updates, but the reviewed cell exposes one tutor through several service facets. No specific inter-S1 mutual-adjustment relation is established by these storage primitives.
- Why no material first-party path remains: the reviewed alternatives close ordinary teaching or implementation support; none supplies the distinct interference among independent S1 tutoring units relation within this standard distribution.

## S3 — Inside-and-now control

- State: —
- Function: no material first-party path for whole-system resource/commitment control at the declared boundary.
- Disturbance / variety regulated: the candidate distinction is whole-system resource/commitment control; observed nearby mechanisms are assessed below.
- Decisive decision or feedback right: no function-specific decisive right with the required closure established.
- Decision owner: no qualifying owner identified for this function; learner/model/developer ownership of ordinary teaching remains as described.
- Supporting / enforcement mechanisms: `src/main/learning/engine.ts`, `src/main/services/setup.ts`, `src/main/agents/claude.ts`.
- Closure path: Curriculum selection, lesson progress and help-level changes are the primary tutoring transformation. Cancellation, fixed turn limits and a learner selecting a model do not constitute whole-system current resource bargaining or intervention. The inspected supported learner mode supplies no separate function-specific parent S3 loop.
- Why this is / is not agent-owned: no positive functional witness is supplied by the inspected alternatives, so agent/constructor/parent ownership is not inferred.
- Evidence: [src/main/learning/engine.ts](https://github.com/ketiyohannes/mint/blob/0f98e1b4a17f9b73aabc6f8789e604d5902d648d/src/main/learning/engine.ts); [src/main/services/setup.ts](https://github.com/ketiyohannes/mint/blob/0f98e1b4a17f9b73aabc6f8789e604d5902d648d/src/main/services/setup.ts); [src/main/agents/claude.ts](https://github.com/ketiyohannes/mint/blob/0f98e1b4a17f9b73aabc6f8789e604d5902d648d/src/main/agents/claude.ts).
- Basis: structural.
- Confidence: medium-high, bounded to the supplied distribution.
- Caveats: custom integrations or a wider institution could add this function; that possibility is not evidence of a shipped path.

### Absence scope

- Surfaces inspected: `src/main/learning/engine.ts`, `src/main/services/setup.ts`, `src/main/agents/claude.ts`, application README, job/runtime composition and the supported learner interactions.
- Plausible first-party paths checked: Curriculum selection, lesson progress and help-level changes are the primary tutoring transformation. Cancellation, fixed turn limits and a learner selecting a model do not constitute whole-system current resource bargaining or intervention. The inspected supported learner mode supplies no separate function-specific parent S3 loop.
- Why no material first-party path remains: the reviewed alternatives close ordinary teaching or implementation support; none supplies the distinct whole-system resource/commitment control relation within this standard distribution.

## S3* — Complementary audit

- State: —
- Function: no material first-party path for independent challenge to operational tutoring claims at the declared boundary.
- Disturbance / variety regulated: the candidate distinction is independent challenge to operational tutoring claims; observed nearby mechanisms are assessed below.
- Decisive decision or feedback right: no function-specific decisive right with the required closure established.
- Decision owner: no qualifying owner identified for this function; learner/model/developer ownership of ordinary teaching remains as described.
- Supporting / enforcement mechanisms: `src/main/jobs/index.ts`, `src/main/services/sessions.ts`, `src/main/jobs/run.ts`.
- Closure path: The model judges the learner's answer, not a tutor's ordinary claim of successful work. Diagram repair, schema validation and learner-code tests are routine production checks. No independent direct-evidence challenge of the tutoring cell with a returned corrective control path is supplied.
- Why this is / is not agent-owned: no positive functional witness is supplied by the inspected alternatives, so agent/constructor/parent ownership is not inferred.
- Evidence: [src/main/jobs/index.ts](https://github.com/ketiyohannes/mint/blob/0f98e1b4a17f9b73aabc6f8789e604d5902d648d/src/main/jobs/index.ts); [src/main/services/sessions.ts](https://github.com/ketiyohannes/mint/blob/0f98e1b4a17f9b73aabc6f8789e604d5902d648d/src/main/services/sessions.ts); [src/main/jobs/run.ts](https://github.com/ketiyohannes/mint/blob/0f98e1b4a17f9b73aabc6f8789e604d5902d648d/src/main/jobs/run.ts).
- Basis: structural.
- Confidence: medium-high, bounded to the supplied distribution.
- Caveats: custom integrations or a wider institution could add this function; that possibility is not evidence of a shipped path.

### Absence scope

- Surfaces inspected: `src/main/jobs/index.ts`, `src/main/services/sessions.ts`, `src/main/jobs/run.ts`, application README, job/runtime composition and the supported learner interactions.
- Plausible first-party paths checked: The model judges the learner's answer, not a tutor's ordinary claim of successful work. Diagram repair, schema validation and learner-code tests are routine production checks. No independent direct-evidence challenge of the tutoring cell with a returned corrective control path is supplied.
- Why no material first-party path remains: the reviewed alternatives close ordinary teaching or implementation support; none supplies the distinct independent challenge to operational tutoring claims relation within this standard distribution.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party path for external and prospective adaptation of the tutoring system's capability at the declared boundary.
- Disturbance / variety regulated: the candidate distinction is external and prospective adaptation of the tutoring system's capability; observed nearby mechanisms are assessed below.
- Decisive decision or feedback right: no function-specific decisive right with the required closure established.
- Decision owner: no qualifying owner identified for this function; learner/model/developer ownership of ordinary teaching remains as described.
- Supporting / enforcement mechanisms: `src/main/services/setup.ts`, `src/main/jobs/index.ts`, `src/main/learning/engine.ts`.
- Closure path: Source import, web-assisted answers, curriculum re-planning and learner-independence history inform delivery of the current class. They do not develop and return options for changing this harness's future operational capability. No separate supported autonomous or parent adaptation loop is supplied.
- Why this is / is not agent-owned: no positive functional witness is supplied by the inspected alternatives, so agent/constructor/parent ownership is not inferred.
- Evidence: [src/main/services/setup.ts](https://github.com/ketiyohannes/mint/blob/0f98e1b4a17f9b73aabc6f8789e604d5902d648d/src/main/services/setup.ts); [src/main/jobs/index.ts](https://github.com/ketiyohannes/mint/blob/0f98e1b4a17f9b73aabc6f8789e604d5902d648d/src/main/jobs/index.ts); [src/main/learning/engine.ts](https://github.com/ketiyohannes/mint/blob/0f98e1b4a17f9b73aabc6f8789e604d5902d648d/src/main/learning/engine.ts).
- Basis: structural.
- Confidence: medium-high, bounded to the supplied distribution.
- Caveats: custom integrations or a wider institution could add this function; that possibility is not evidence of a shipped path.

### Absence scope

- Surfaces inspected: `src/main/services/setup.ts`, `src/main/jobs/index.ts`, `src/main/learning/engine.ts`, application README, job/runtime composition and the supported learner interactions.
- Plausible first-party paths checked: Source import, web-assisted answers, curriculum re-planning and learner-independence history inform delivery of the current class. They do not develop and return options for changing this harness's future operational capability. No separate supported autonomous or parent adaptation loop is supplied.
- Why no material first-party path remains: the reviewed alternatives close ordinary teaching or implementation support; none supplies the distinct external and prospective adaptation of the tutoring system's capability relation within this standard distribution.

## S5 — Policy and identity

- State: —
- Function: no material first-party path for identity or ultimate-policy tension at the tutoring-cell boundary at the declared boundary.
- Disturbance / variety regulated: the candidate distinction is identity or ultimate-policy tension at the tutoring-cell boundary; observed nearby mechanisms are assessed below.
- Decisive decision or feedback right: no function-specific decisive right with the required closure established.
- Decision owner: no qualifying owner identified for this function; learner/model/developer ownership of ordinary teaching remains as described.
- Supporting / enforcement mechanisms: `src/main/services/setup.ts`, `src/main/services/chat.ts`, `src/main/services/sessions.ts`.
- Closure path: Mission fields, fixed pedagogy, trusted domains and record/source acceptance constrain the teaching task. Changing a class goal or approving a source/record is ordinary operational input. No path frames an unresolved identity/ultimate-policy matter, routes it to a legitimate ultimate authority, and returns that decision to govern the cell.
- Why this is / is not agent-owned: no positive functional witness is supplied by the inspected alternatives, so agent/constructor/parent ownership is not inferred.
- Evidence: [src/main/services/setup.ts](https://github.com/ketiyohannes/mint/blob/0f98e1b4a17f9b73aabc6f8789e604d5902d648d/src/main/services/setup.ts); [src/main/services/chat.ts](https://github.com/ketiyohannes/mint/blob/0f98e1b4a17f9b73aabc6f8789e604d5902d648d/src/main/services/chat.ts); [src/main/services/sessions.ts](https://github.com/ketiyohannes/mint/blob/0f98e1b4a17f9b73aabc6f8789e604d5902d648d/src/main/services/sessions.ts).
- Basis: structural.
- Confidence: medium-high, bounded to the supplied distribution.
- Caveats: custom integrations or a wider institution could add this function; that possibility is not evidence of a shipped path.

### Absence scope

- Surfaces inspected: `src/main/services/setup.ts`, `src/main/services/chat.ts`, `src/main/services/sessions.ts`, application README, job/runtime composition and the supported learner interactions.
- Plausible first-party paths checked: Mission fields, fixed pedagogy, trusted domains and record/source acceptance constrain the teaching task. Changing a class goal or approving a source/record is ordinary operational input. No path frames an unresolved identity/ultimate-policy matter, routes it to a legitimate ultimate authority, and returns that decision to govern the cell.
- Why no material first-party path remains: the reviewed alternatives close ordinary teaching or implementation support; none supplies the distinct identity or ultimate-policy tension at the tutoring-cell boundary relation within this standard distribution.

## Distributed OSS parent arrangement

Public contribution/release ownership is outside the tutoring cell. The learner's local source, goal and record choices do not establish organization-level parent S3/S4/S5.

## Self-hosted and non-human modes

Claude and Codex are supported alternative execution seams, not alternative VSM parent modes. Demo demonstrates UI flow without autonomous reasoning and contributes no A claim.

## Recursion

Classes, sessions and anchored threads partition state; no complete recursive viable suborganization is established.

## Variety and escalation

The help ladder, citation context, input limits, schema retry, trusted domains and cancellation attenuate learner/provider variety. Errors become notices or returned job errors. These are not by themselves algedonic or metasystemic functions.

## Evidence gaps

Static source assessment only; no paid-provider or packaged desktop E2E run. No claim that generated checks are pedagogically valid or that a learner gains measured independence. Boundaries follow the implemented local teaching composition rather than external SDK internals.

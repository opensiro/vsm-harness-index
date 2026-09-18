---
harness_id: clawgui
project_name: ClawGUI
repository: https://github.com/ZJU-REAL/ClawGUI
review_ref: d990d3e3f2390ced708771d9681d3c4f9a6cbef5
reviewed_at: 2026-09-18
generated_profile_version: 0.2.2
generated_assessment_procedure_version: 0.3.1
profile_version: 0.2.2
assessment_procedure_version: 0.3.1
assessment_changed_at: 2026-09-18
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# ClawGUI

## Review boundary

- System in focus: the deployable ClawGUI-Agent / ClawGUI-APP operational harness plus the first-party ClawGUI-Skills runtime at pinned revision `d990d3e3f2390ced708771d9681d3c4f9a6cbef5`.
- Purpose and identity: let a model-driven GUI agent execute real-device tasks and, in the optional evolve mode, reuse/revise procedural skills from operational evidence.
- Relevant environment: Android/HarmonyOS/iOS devices, mobile applications and screens, external model endpoints, user requests and chat/control surfaces.
- Standard-distribution boundary: ClawGUI's own Agent/APP orchestration and Skills implementation. ClawGUI-RL and ClawGUI-Eval are training/evaluation environments rather than part of the operational system-in-focus; upstream OpenClaw/nanobot behaviour is not inherited wholesale.
- First-party operating/deployment modes considered: deployable device agent, on-device brain+phone-agent stack, skill modes `off`, `trace`, `reuse`, and `evolve`.
- Recursion level: one deployed GUI-agent organization. Brain/phone-agent composition is task decomposition unless separately shown to be viable recursion.
- Reviewed revision: `d990d3e3f2390ced708771d9681d3c4f9a6cbef5`.
- Observation date: 2026-09-18.
- Generated/current Profile / Methodology: `0.2.2` / `0.3.1`.

## Repository architecture

ClawGUI-Agent exposes natural-language control over mobile devices and maintains sessions/memory. ClawGUI-APP can run a two-agent stack on one phone: a brain model handles planning/tool orchestration while a phone agent performs screen understanding and actions. The optional ClawGUI-Skills subsystem stores structured procedural packages and can retrieve them into PhoneAgent context.

In `evolve` mode, a failed rollout is sent to an explicitly isolated verifier. The verifier receives a sealed observational view — task instruction, screenshots, action JSON, accessibility/DOM text and final state — while being prohibited from seeing executor reasoning or skill-package contents. It returns an evidence-grounded success/failure diagnosis and behavioral suggestions. A separate skill-revision step must then edit the restricted skill package and PhoneAgent retries when a revision is produced.

## Primary evidence

- [`README.md`](https://github.com/ZJU-REAL/ClawGUI/blob/d990d3e3f2390ced708771d9681d3c4f9a6cbef5/README.md) — deployable Agent/APP boundaries, brain/phone-agent split, memory and self-evolving Skills surface.
- [`clawgui-skills/README.md`](https://github.com/ZJU-REAL/ClawGUI/blob/d990d3e3f2390ced708771d9681d3c4f9a6cbef5/clawgui-skills/README.md) — evolve-mode retrieve/generate/diagnose/revise/retry closure, isolated verifier and restricted revision boundary.
- [`clawgui-skills/clawgui_skills/prompts.py`](https://github.com/ZJU-REAL/ClawGUI/blob/d990d3e3f2390ced708771d9681d3c4f9a6cbef5/clawgui-skills/clawgui_skills/prompts.py) — strict verifier information isolation, evidence-grounded diagnostic schema and mandatory downstream skill-edit protocol.

## Operational model

The main operational unit is the model-driven GUI agent that plans and performs device actions to satisfy a user task. In APP mode the brain and phone agent divide planning/orchestration from screen execution, but this alone does not establish peer coordination or whole-system control. Skill evolution is optional and is treated separately from the normal task loop. Its verifier path is materially distinct from ordinary self-report because it observes sealed execution evidence without access to the executor's reasoning/playbook and can force corrective revision before retry.

## S1 — Operations

- State: `A`.
- Function: execute user-requested GUI/device outcomes through autonomous perception, planning/tool orchestration and screen actions.
- Disturbance / variety regulated: changing UI state, device/application differences, task instructions, failed actions and environmental interruptions.
- Decisive decision or feedback right: model-driven agent actors choose operational plans/actions and adapt to observed device state.
- Decision owner: autonomous brain/GUI-agent actor in the first-party deployment path.
- Supporting / enforcement mechanisms: device adapters, sessions, memory, chat surfaces and skill retrieval/injection.
- Closure path: actions change device state, subsequent screen observations return to the agent and drive later actions until completion/failure.
- Basis / confidence: explicit + structural; high.

## S2 — Coordination

- State: `—`.
- The two-agent brain/phone architecture separates responsibilities and tool execution, but the pinned evidence does not establish a concrete inter-S1 interference/conflict/oscillation plus a mutual-adjustment loop that attenuates it. Orchestration/delegation alone is not S2.
- Confidence: high.

## S3 — Inside-and-now control

- State: `—`.
- The brain orchestrates a task and the runtime manages sessions/device execution, but no distinct first-party actor is evidenced with current whole-organization visibility plus discretionary authority over shared resources, priorities or commitments across multiple operational S1s.
- Confidence: high.

## S3* — Complementary audit

- State: `A`.
- Claim being audited: whether the operating PhoneAgent actually achieved the user's GUI task and, when not, where observable execution first departed from success.
- Ordinary reporting path: executor rollout/actions and its normal task outcome.
- Complementary access path: an explicitly independent verifier receives only sealed external evidence — screenshots, action log, accessibility/DOM data, final state and optional prior assertions — and never sees the executor's reasoning, plans or skill package.
- Independence boundary: the verifier is instructed to judge only observable evidence and cannot modify the executor's playbook itself.
- Decisive judgment / owner: the verifier model independently determines task success, failure type/step, root cause and behavioral corrections.
- Supporting mechanisms: strict JSON schema, evidence packaging and restricted skill-file tools.
- Closure path: failed verification feeds a separate `skill_revise` step that is required to change the skill package; when a revision is produced, PhoneAgent immediately retries using the changed capability.
- Why this is S3*: the path provides materially different access to operational reality, an independent judgment boundary and explicit corrective return rather than routine executor self-checking.
- Basis / confidence: explicit + structural; high.

## S4 — Outside-and-then intelligence

- State: `—`.
- The evolve loop changes future procedural capability, but its trigger and evidence are failures from the system's own current GUI-task execution. It does not establish an external-and-prospective model of changing users, threats, tools or future conditions that develops adaptation options in a two-way S3/S4 conversation.
- Self-improvement alone is therefore not promoted to S4.
- Confidence: high.

## S5 — Policy and identity

- State: `—`.
- User requests, model/configuration choices, skill modes and restricted edit surfaces constrain operation, but no runtime identity/ultimate-policy authority loop is evidenced at this recursion.
- Confidence: high.

## Recursion

The brain and phone agent are compositional actors, not automatically recursive viable systems. RL/evaluation modules are separate lifecycle environments and do not lend their functions to the deployed operational harness.

## Variety and escalation

Skill retrieval attenuates context variety; model/device support amplifies operational repertoire. In evolve mode, failure evidence bypasses executor self-report through the isolated verifier and returns through restricted revision/retry, forming the credited S3* corrective path.

## Evidence gaps

The assessment does not import upstream OpenClaw/nanobot organizational behaviour beyond what ClawGUI's pinned first-party deployment and Skills contracts explicitly expose.

## Admission conclusion

Canonical vector: `A — — A — —`.

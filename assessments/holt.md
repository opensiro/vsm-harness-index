---
harness_id: holt
project_name: Holt
repository: https://github.com/holt-os/holt
review_ref: 3a88451f980678f5dd62d72d9b159c125c48ae05
reviewed_at: 2026-09-22
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
assessment_changed_at: 2026-09-22
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: P
autonomy_s3_star: C
autonomy_s4: A
autonomy_s5: —
---

# Holt

## Review boundary

- System in focus: one trusted first-party Holt workspace installation at pinned revision `3a88451f980678f5dd62d72d9b159c125c48ae05`, including Holt's built-in direct-API REPL/task path, memory/wiki/voice state, routines/schedules, Telegram path, shipped skills and self-hosted operator commands.
- Purpose and identity: provide a local personal-agent OS that performs remembered work, can run configured work unattended, adapts selected future behavior from user evidence, and keeps the user's knowledge and operating controls inspectable on their own machine.
- Relevant environment: the user and their writing/work patterns, workspace files, Telegram messages, scheduled time, model-provider responses, machine/tool availability, memory state, and recurring work the user may choose to automate.
- Standard-distribution boundary: Holt-owned TypeScript runtime, direct provider API adapter, REPL/noninteractive runner, local memory/wiki/voice files, OS-timer integration, built-in skills, Telegram adapter and operator CLI. Claude Code, Codex and Gemini interactive/noninteractive CLI brains are separate external agent runtimes; their internal tools, planning and autonomy are not credited to Holt.
- Credited operating / distribution surfaces: `src/apibrain.ts`; `src/commands/chat.ts`; `src/runner.ts`; `src/routines.ts`; `src/scheduler.ts`; `src/commands/routine.ts`; `src/commands/schedule.ts`; `src/commands/telegram.ts`; `src/voice.ts`; `src/commands/voice.ts`; `src/commands/write.ts`; `src/skills.ts`; `skills/audit/SKILL.md`; `skills/level-up/SKILL.md`; `src/commands/doctor.ts`; `src/memory.ts`; `src/facts.ts`; `src/wiki.ts`; supported operator commands/configuration around those surfaces.
- Adjacent first-party surfaces excluded from ownership: repository CI/release workflows, tests, contributor tooling and documentation examples are corroborating only. Holt's launch/compiler/hook integrations may configure external Claude Code/Codex/Gemini environments, but the external CLI agent's own shell/tool autonomy is not borrowed as Holt ownership.
- First-party operating / deployment modes considered: Holt's built-in REPL with a direct API brain; one-shot `holt run`; named routines; OS-scheduled runs; Telegram-to-`runTask`; voice-profile synthesis and `holt write`; built-in `/skill audit` and `/skill level-up`; local self-hosted operator administration.
- Recursion level: one Holt workspace installation is the system-in-focus. Individual scheduled runs, routines and chat turns are candidate operational units only where they perform distinct outcomes; external CLI agents are not promoted into the Holt organization merely because Holt can launch them.
- Reviewed revision: `3a88451f980678f5dd62d72d9b159c125c48ae05`.
- Observation date: 2026-09-22.
- Generated Profile version: `0.2.3`.
- Generated Methodology version: `0.3.5`.
- Current Profile version: `0.2.3`.
- Current Methodology version: `0.3.5`.

## Repository architecture

Holt has two materially different brain boundaries. Its default interactive launcher can hand the terminal to Claude Code, Codex or Gemini; those products retain their own agentic tool/runtime behavior and stay external to this assessment. Separately, Holt ships a first-party direct-API path. `runApiBrain` talks to supported provider APIs itself, and Holt's own REPL and shared `runTask` runner can select that path without an external coding-agent harness.

Holt owns transcript reconstruction, semantic/keyword recall, persistence and task closure around that direct model call. `runTask` is shared by one-shot work, Telegram and scheduled/routine execution. Routines persist named reusable tasks or skills, while schedules install OS-native launchd/cron/Task Scheduler entries that invoke the same Holt runner later. This establishes a first-party autonomous operating mode even when no external CLI-agent autonomy is credited.

The repository also ships two metasystemically relevant surfaces. First, `/skill audit` is an explicit read-only setup audit procedure: it requires raw Holt state from memory/facts, voice, hook, skills, routines, schedules, doctor and wiki surfaces, grades the installation's Know/Reach/Do/Run rungs, identifies broken state separately from missing state, and returns one next corrective action. The skill is prompt text rather than executable code, so in Holt's first-party direct-API mode the model cannot itself run those local probes; the user must paste evidence or an external tool-capable CLI brain must be composed. Second, Holt's voice subsystem converts real user writing/interview evidence into a model-selected durable `StyleProfile`; later `holt write` calls load that profile into the generation prompt, creating a closed first-party behavioral adaptation loop.

## Operational model

A user message, Telegram message, one-shot task or scheduled routine enters Holt's own runner. Holt recalls relevant memory, adds available-skill context, invokes the configured direct API brain when selected, and on success persists task/result state or routes output to a file/Telegram. Scheduled work therefore can complete without a fresh user turn.

Current installation control remains parent-owned. Holt deliberately keeps trust, brain choice, hooks, skills, routines, schedules, semantic-memory repair and related machine-level decisions exposed to the local operator. The shipped `audit` procedure turns those raw surfaces into one installation-wide health view and a prioritized next intervention; the operator chooses and executes the returned control change.

The same `audit` surface is complementary to ordinary operation but does not reach autonomous S3* closure inside Holt's own direct-API runtime because skills are prompt text and the direct model has no shell/tool channel for the required probes. It is therefore credited as a first-party audit constructor rather than importing the external CLI brain's tool agency.

## S1 — Operations

- State: A
- Function: autonomously turn user, Telegram or scheduled objectives into model-selected content/work outcomes with Holt-owned memory and output closure.
- Disturbance / variety regulated: heterogeneous natural-language tasks, recalled workspace context, model-provider responses, recurring scheduled objectives and changing user messages.
- Decisive decision or feedback right: choose the substantive answer/task output from the supplied objective, recalled context and skill instructions.
- Decision owner: the configured model actor reached through Holt's first-party direct-API brain path.
- Supporting / enforcement mechanisms: `runApiBrain`, `runTask`, REPL prompt/history construction, memory recall/persistence, routine resolution, OS timers, Telegram polling, file/Telegram output routing and trust/configuration checks.
- Closure path: user/schedule/Telegram trigger → Holt prompt + recalled state → direct model decision → returned output → Holt persists task/result memory and/or writes/sends the output → later Holt work can consume the resulting state.
- Boundary reachability: direct API brains are a documented standard Holt mode; the built-in REPL uses them when the selected brain has no interactive TUI, and `runTask` is the shared first-party engine behind `holt run`, scheduled jobs and Telegram.
- Why this is / is not agent-owned: the model actor owns the material output decision while Holt's deterministic runtime supplies transport, memory, scheduling and delivery. No Claude Code/Codex/Gemini CLI internals are needed for this positive mapping.
- Evidence: `src/apibrain.ts`; `src/commands/chat.ts`; `src/runner.ts`; `src/routines.ts`; `src/scheduler.ts`; `src/commands/telegram.ts`; pinned README direct-API/scheduled-work documentation.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the direct-API path is principally text/model-output agency rather than an unrestricted shell/tool loop; scheduled routines nonetheless close real first-party operational outcomes through persisted output/files/Telegram.

## S2 — Coordination

- State: —
- Function: no material first-party S2 relation among distinct Holt S1 units is established at the reviewed boundary.
- Disturbance / variety regulated: no concrete cross-S1 interference/conflict/oscillation plus attenuation loop was found.
- Decisive decision or feedback right: no S2-specific coordination discretion is supplied.
- Decision owner: not established.
- Supporting / enforcement mechanisms: OS schedules, routine lists, Telegram's single-busy guard, memory persistence and ordinary task sequencing.
- Closure path: no qualifying coordination-result → subsequent sibling-S1 behavior loop is evidenced.
- Why this is / is not agent-owned: timers, serialization and shared memory order work but are not tied to a demonstrated inter-S1 disturbance that the mechanism exists to damp.
- Evidence: `src/scheduler.ts`; `src/commands/schedule.ts`; `src/commands/telegram.ts`; `src/runner.ts`; routine implementation.
- Basis: structural absence.
- Confidence: high.
- Caveats: multiple schedules may coexist, but plurality plus timing is not an S2 witness.

### Absence scope

- Surfaces inspected: REPL/task runner, routines, OS scheduling, Telegram busy-state handling, memory/wiki persistence and built-in skills.
- Plausible first-party paths checked: overlapping scheduled/routine work, Telegram serialization, shared workspace/memory state and task ordering.
- Why no material first-party path remains: the reviewed code supplies sequencing/execution support but does not identify a specific sibling-S1 collision or oscillation and a relation designed to attenuate it with feedback into later S1 behavior.

## S3 — Inside-and-now control

- State: P
- Function: regulate the current Holt installation's usable operating capacity and automation state across memory, reach, skills, routines/schedules, brain/machine health and related first-party capabilities.
- Disturbance / variety regulated: current gaps or failures across what Holt knows, what environment it can reach, what repeatable work it can do, what unattended work is configured, and machine/brain/memory conditions that make the installation less capable than intended.
- Decisive decision or feedback right: choose the installation-wide next intervention — for example repair semantic recall, install/remove a hook, add/remove or correct a skill/routine/schedule, change a brain/configuration choice, or stop an unhealthy automation.
- Decision owner: the local self-hosted user/operator as legitimate parent actor.
- Supporting / enforcement mechanisms: `/skill audit` whole-setup review protocol, `holt doctor` probes/repair path, memory/voice/hook/skill/routine/schedule/wiki status commands, trust/configuration state and the corresponding mutation/removal commands.
- Closure path: current raw installation state → audit report identifies the lowest/broken gap and one corrective action → parent user chooses/runs the first-party control command → Holt changes the affected current capability/configuration/automation → subsequent operation occurs under the returned state.
- Boundary reachability: `audit` ships as a built-in skill and is advertised as the supported way to see what is missing; all cited inspection and corrective commands are ordinary installed Holt CLI surfaces.
- Why this is / is not agent-owned: the audit model may recommend a next intervention, but the shipped procedure explicitly leaves the corrective command to the user. The parent decides whether and how current installation capacity changes; deterministic commands merely apply that decision.
- Evidence: `skills/audit/SKILL.md`; `src/commands/doctor.ts`; `src/commands/hook.ts`; `src/commands/skill.ts`; `src/commands/routine.ts`; `src/commands/schedule.ts`; README four-rung operating workflow.
- Basis: explicit + structural.
- Confidence: medium.
- Caveats: this is an installation-health/current-capability S3 claim, not a claim that every preference or configuration edit is S3. The positive path relies on the shipped whole-setup audit/control ritual rather than isolated settings commands.
- Whole-system current view: the built-in audit deliberately spans the four operating rungs — Know, Reach, Do and Run — and requires current evidence from memory/facts, voice, hook, skills, routines, schedules, doctor and wiki state before naming the highest solid rung and lowest gap.
- Current-control decision scope: parent intervention over current memory/reach health, available repeatable capabilities, unattended commitments/schedules and the brain/machine conditions that support the installation as a whole.

## S3* — Complementary audit

- State: C
- Function: challenge ordinary assumptions that the Holt installation is actually healthy and operational by inspecting raw local state through a read-only, cross-surface audit procedure rather than trusting chat or configuration claims.
- Disturbance / variety regulated: silent degradation such as keyword-only recall, unembedded memory, hooks that are absent, only built-in rather than work-specific skills, routines that exist but never produced output, broken scheduled work, or automation layered over an empty memory.
- Decisive decision or feedback right: assess raw evidence across the four rungs, mark each `solid` / `thin` / `missing`, separate actively broken state from mere absence, and select the single next issue that should enter parent current control.
- Decision owner: constructor-level at the reviewed first-party boundary. Holt supplies the audit-specific evidence checklist and judgment protocol, but its own direct-API model mode lacks a first-party tool channel for autonomously executing the required local probes; fully autonomous probe access would require composition or borrowing an external CLI brain, which is outside credited ownership.
- Supporting / enforcement mechanisms: read-only `holt memory`, `memory facts`, `voice show`, `hook status`, `skill list`, `routine list`, `schedule list`, `doctor`, `wiki status`, local logs/status files and the built-in audit prompt.
- Closure path: complementary raw state is gathered → the audit protocol forms a strict health finding and one next fix → that finding is returned to the parent S3 path, where the user may apply the corresponding first-party control command.
- Boundary reachability: `/skill audit` is a built-in installed skill in the standard distribution, and every named probe is a first-party Holt command. The constructor classification deliberately avoids treating external Claude/Codex/Gemini shell-tool agency as Holt-owned closure.
- Why this is / is not agent-owned: the repository ships a function-specific audit construction rather than generic logs, but autonomous access/judgment closure is not completely first-party in the direct-API mode. This supports `C`, not `A`.
- Evidence: `skills/audit/SKILL.md`; `src/skills.ts`; `src/commands/doctor.ts`; read-only status/list commands for memory/hooks/skills/routines/schedules/wiki.
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: a tool-capable external CLI brain may be able to run the probes itself, but its autonomous tool use is excluded by the declared boundary. In direct-API mode the skill explicitly falls back to asking the user to paste raw outputs rather than guessing.
- Claim being audited: that the installed Holt setup really has usable Know/Reach/Do/Run capacity and that configured memory/automation is functioning rather than merely existing on disk.
- Ordinary reporting path: normal Holt chat/task outputs, existence of configured skills/routines/schedules, and ordinary status/configuration surfaces used during operation.
- Complementary access path: the audit procedure reads separate raw local evidence — actual memory facts/mode, hook installation state, skill inventory, routine/schedule inventory, doctor machine/brain/semantic-memory probes, wiki state and, where relevant, produced logs/output.
- Independence boundary: the audit is explicitly read-only and checks underlying Holt artifacts/status rather than accepting the ordinary model's success narrative; however autonomous execution of all probes is not owned by Holt's direct-API runtime, which is why the state remains constructor-level.
- Who acts on findings: the audit returns the lowest gap/breakage and one next command to the local parent operator; that parent owns the S3 corrective intervention.

## S4 — Outside-and-then intelligence

- State: A
- Function: adapt future Holt writing behavior from external evidence of how the user actually writes and wants to communicate.
- Disturbance / variety regulated: mismatch between generic/model-default prose and the user's evolving tone, formality, sentence rhythm, formatting, vocabulary, audience and real writing samples.
- Decisive decision or feedback right: infer a structured `StyleProfile` from supplied interview answers and/or real writing samples, including tone/formality/rhythm/formatting/signature moves/banned words/audience and related style distinctions.
- Decision owner: the configured model actor reached through Holt's first-party brain-call path; a direct API brain is sufficient and does not require external CLI-agent tools.
- Supporting / enforcement mechanisms: `holt voice` / `holt voice add`, sample consent/hash/excerpt handling, `synthesizeVoice`, persistent `~/.holt/voice.json`, `voicePromptBlock`, and `holt write` generation/self-check path.
- Closure path: new user writing/style evidence → model synthesis of a durable structured profile → Holt saves the profile → later `holt write` loads it into the generation prompt → subsequent operational writing behavior changes under the adaptation.
- Boundary reachability: voice interview/add and write are documented standard Holt commands; `synthesizeVoice` can call a configured direct API brain through first-party `runApiBrain`, and `holt write` consumes the saved profile through the same installed runtime.
- Why this is / is not agent-owned: the user chooses what evidence to share and triggers refresh, but the model actor makes the substantive interpretation from evidence into the structured future-behavior profile and Holt automatically closes that profile into later writing. User input therefore supplies environmental evidence rather than replacing the adaptation judgment.
- Evidence: `src/voice.ts`; `src/commands/voice.ts`; `src/commands/write.ts`; `src/apibrain.ts`; README voice capability.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: fact extraction and wiki synthesis are not separately counted as S4 because they primarily maintain memory. The built-in `level-up` skill supplies an additional explicitly parent-assisted capability-evolution ritual, but no `(P)` modifier is claimed here because it is a distinct adaptation path rather than an alternate ownership mode of the voice-synthesis decision used for the autonomous base claim.
- External distinction: interview answers and real writing samples expose user-environment distinctions about desired and actual communication style.
- Future / prospective distinction: the profile represents how future drafts should change so Holt remains fitted to that style rather than continuing generic model-default writing.
- Adaptation option generated: a model-selected structured `StyleProfile` with concrete prompt-relevant behavior such as tone, formality, sentence length, formatting, signature moves and banned words.
- Path back into current capability / S3: the profile is persisted globally and `holt write` injects it into later generation; the parent S3 operator can inspect, refresh, edit or clear the profile if the adapted behavior is unwanted.

## S5 — Policy and identity

- State: —
- Function: no runtime identity/ultimate-policy closure path is established at the declared Holt-installation recursion.
- Disturbance / variety regulated: the review looked for an identity- or ultimate-policy-level issue that can reach legitimate authority and return as a governing decision for subsequent Holt operation.
- Decisive decision or feedback right: no such first-party runtime identity-policy decision path was found.
- Decision owner: not established for qualifying S5.
- Supporting / enforcement mechanisms: static `HOLT_IDENTITY` branding, trust gates, brain/settings selection, onboarding facts/standing rules, voice preferences and user control over skills/routines/schedules.
- Closure path: these surfaces configure or constrain ordinary operation but do not form an identity-level issue → authority → authoritative decision → returned organization-wide policy loop.
- Why this is / is not agent-owned: `HOLT_IDENTITY` is developer-authored static prompt/context and therefore cannot establish S5 by itself. User preferences, trust choices and ordinary configuration likewise do not demonstrate ultimate-policy closure.
- Evidence: `src/commands/launch.ts`; `skills/onboard/SKILL.md`; `src/config.ts`; trust/settings/voice surfaces inspected alongside standard runtime paths.
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: Holt strongly brands external interactive brains as Holt and asks onboarding questions about standing rules, but prompt existence and stored preferences are explicitly insufficient for S5 without a runtime identity/ultimate-policy decision loop.

### Absence scope

- Surfaces inspected: `HOLT_IDENTITY` branding/injection, onboarding standing-rule capture, per-workspace config, trust boundary, voice profile, skills/routines/schedules and user settings/brain selection.
- Plausible first-party paths checked: identity branding/context files, user preference memory, voice/persona calibration, trusted-workspace authority and ordinary operator configuration.
- Why no material first-party path remains: the identity text is static developer policy and the mutable user surfaces regulate preferences/capabilities/tasks rather than a disputed identity/ultimate-policy matter with an authoritative return-to-operation closure.

## Recursion

The assessment treats one trusted Holt workspace installation as the viable system in focus. Scheduled runs, routines, chat turns and Telegram tasks can be distinct S1 operating instances without being separately viable recursive systems. External Claude Code/Codex/Gemini CLIs are adjacent agent runtimes and require their own boundaries rather than donating their internal autonomy to Holt.

## Variety and escalation

Holt attenuates operational variety through per-workspace trust, bounded recall, named routines, OS schedules, Telegram's busy guard and explicit operator configuration. It amplifies capability through selectable direct API brains, reusable skills, semantic memory, wiki synthesis and Telegram/file output. Installation-health exceptions surface through the audit procedure to the parent operator. Writing-style change enters the autonomous voice adaptation path and returns into future `holt write` behavior.

## Evidence gaps

- The S3 parent claim is scoped to the explicit installation-health/control ritual; isolated settings edits are not credited as S3.
- S3* is deliberately `C` rather than `A`: the audit protocol and independent raw-state surfaces are first-party, but Holt's direct-API model path cannot autonomously execute the local command probes, while external CLI-agent tooling is outside the ownership boundary.
- S4 is credited to the direct-API-compatible voice synthesis/return loop, not to generic fact extraction, wiki maintenance or memory growth.
- The separate `level-up` workflow is useful evidence of intentional future capability adaptation, but this assessment avoids converting it into `(P)` on top of the voice-specific autonomous S4 claim because the two paths regulate different adaptation decisions.

## Admission conclusion

Standalone vector at the pinned revision: `A — P C A —`.

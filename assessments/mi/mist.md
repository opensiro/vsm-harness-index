---
harness_id: mist
project_name: mist
repository: https://github.com/mist-agent-harness/mist-agent
review_ref: 4e87b332140ce3d2eabeff7b4e16532c2c56a6be
reviewed_at: 2026-11-11
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: A
---

# mist

## Review boundary

- System in focus: the shipped personal resident runtime and terminal onboarding in `mist-agent`, not the larger designed-but-unimplemented social world or its evaluation suites.
- Purpose and identity: sustain an individual model-backed conversational resident's identity, factual commitments and message history through dying/restarting conversation generations.
- Relevant environment: user-supplied persona proposal, model replies, ledger facts, user turns, interrupted writes, ambiguous retries, resident generation changes and provider/channel failure.
- Standard-distribution boundary: `npm run setup` and `npm run resident` onboarding/CLI, `ResidentRuntime`, `PiCliTransport`, identity registry, fact ledger, canonical one-stream writer and breath/handover lifecycle. The `pi` CLI is an external *tool-less model transport* (`--no-tools`, `--no-extensions`), not an imported external coding-agent operation loop.
- Credited operating / distribution surfaces: first-party `residentFromInstall` and model self-attestation, one-resident TUI/model reply sessions, durable fact/turn accounting, verified session-resumption and breath/handover procedures.
- Adjacent first-party surfaces excluded from ownership: `src/eval/resident-self-repair`, acceptance-only group-chat host/drivers, speculative design documents, unimplemented web frontend, repository CI and maintainer governance.
- First-party operating / deployment modes considered: newly installed resident creation with model attestation, `--resident` existing resident, authenticated fact ledger, terminal pause/restart, natural-turn and command-requested `/new`/`/clear`/`/compact` breath, optional synthetic transport in tests.
- Recursion level: one resident and its successive conversation generations; group-chat acceptance fixtures do not establish a deployed independent portfolio of operational agents.
- Reviewed revision: `4e87b332140ce3d2eabeff7b4e16532c2c56a6be`.
- Observation date: 2026-11-11.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

On first run the human submits a persona and model selection. The real `PiCliTransport` runs a subprocess with an explicit system prompt and no external tools/sessions/extensions, collects its generated answer, and `onboarding.ts` parses a strict first-line yes/no to decide whether a candidate may become an active resident. `ResidentIdentityStore.attestCandidate` atomically makes an accepted persona an active identity, or durably records rejection. Ordinary `ResidentRuntime.say` reads boot pack, history and fact-ledger state, obtains a model-generated reply, commits a canonical stream and settles delivery/turn receipts. Breath writes a handover letter before replacing a generation, and failures can block unsafe continuation. These are first-party persistent runtime/identity mechanisms rather than merely an external LLM wrapper. [onboarding](https://github.com/mist-agent-harness/mist-agent/blob/4e87b332140ce3d2eabeff7b4e16532c2c56a6be/src/resident-runtime/onboarding.ts), [identity registry](https://github.com/mist-agent-harness/mist-agent/blob/4e87b332140ce3d2eabeff7b4e16532c2c56a6be/src/resident-continuity/identity-store.ts), [runtime](https://github.com/mist-agent-harness/mist-agent/blob/4e87b332140ce3d2eabeff7b4e16532c2c56a6be/src/resident-runtime/runtime.ts), [transport](https://github.com/mist-agent-harness/mist-agent/blob/4e87b332140ce3d2eabeff7b4e16532c2c56a6be/src/resident-runtime/pi-transport.ts).

## Operational model

After a model decides to accept its proposed persona, the resident serves human conversational requests under a persistent identity; its model chooses the substantive reply while first-party runtime handles durable history, facts, idempotent turn delivery and generation continuity. There is no first-party tool selection in the currently deployed `pi` transport (`--no-tools`), so the credited S1 autonomy is **conversational response/action**, not autonomous filesystem/network execution. Unusually, first-party onboarding provides an explicit identity-level decision loop: a resident model can reject the human's persona proposal; only its accepted attestation is installed as the active identity. That is S5 at the **resident formation** boundary, not a claim of a general polity or future adaptation system. Single-resident locks and ordered turns are execution integrity, not coordination among S1 units or whole-system S3 control. Routine acceptance tests are not S3*.

## S1 — Operations

- State: A
- Function: formulate resident's response to live human messages using the current conversation, initial persona, factual commitments and handover information.
- Disturbance / variety regulated: varied questions and conversational inputs, changing facts, failed or duplicated deliveries, lost context and generation rollover.
- Decisive decision or feedback right: resident model chooses the substantive message text after receiving assembled boot pack and prior turn context; further human turns adapt its output.
- Decision owner: configured provider-backed model reached through first-party `ResidentRuntime` and tool-less `PiCliTransport`; no separate external `pi` agent tool loop is credited.
- Supporting / enforcement mechanisms: one-stream writer, turn IDs and idempotent receipts, fact-ledger `currentSet`, handover letters, limited transport credential routing and generation lifecycle.
- Closure path: human turn → one-resident boot/context assembly → model reply generation → durable user+assistant stream events and delivery receipt → subsequent conversation reads settled state.
- Boundary reachability: documented `npm run resident` terminal mode uses first-party assembly and model transport in supported API-key configuration.
- Why this is / is not agent-owned: the model selects response content rather than replaying a deterministic template; delivery and continuity safety gates remain software-owned.
- Evidence: [README real terminal runtime](https://github.com/mist-agent-harness/mist-agent/blob/4e87b332140ce3d2eabeff7b4e16532c2c56a6be/README.md), [model call and durable response path](https://github.com/mist-agent-harness/mist-agent/blob/4e87b332140ce3d2eabeff7b4e16532c2c56a6be/src/resident-runtime/runtime.ts), [tool-less `pi` CLI invocation](https://github.com/mist-agent-harness/mist-agent/blob/4e87b332140ce3d2eabeff7b4e16532c2c56a6be/src/resident-runtime/pi-transport.ts).
- Basis: explicit and structural.
- Confidence: medium-high.
- Caveats: S1 action space is text conversation rather than autonomous first-party tool execution; the source was not run against a paid/live model.

## S2 — Coordination

- State: —
- Function: no evidenced first-party inter-S1 disturbance attenuation in a supported multi-resident production mode.
- Disturbance / variety regulated: concurrent turns and writes for one resident may overlap, but a resident-scoped writer lock/serial queue protects one stream, not independent operating S1 units.
- Decisive decision or feedback right: fixed runtime lock and turn gate serialize the single-resident delivery path; no S2 agent chooses cross-resident operating relations.
- Decision owner: deterministic runtime code, not a separate inter-agent coordinator.
- Supporting / enforcement mechanisms: `ResidentHostLocks`, session turn gate, single canonical writer, canonical stream and idempotent delivery.
- Closure path: second writer/overlapping resident turn → wait or fail `writer-unavailable` → existing resident turn completes; no inter-S1 coordination change.
- Why this is / is not agent-owned: a lock within one resident is ordinary transaction discipline; designed group-chat/roster acceptance surfaces do not prove a shipped S2 operating path.
- Evidence: [runtime turn/host locks](https://github.com/mist-agent-harness/mist-agent/blob/4e87b332140ce3d2eabeff7b4e16532c2c56a6be/src/resident-runtime/runtime.ts), [README single-resident concurrency contract](https://github.com/mist-agent-harness/mist-agent/blob/4e87b332140ce3d2eabeff7b4e16532c2c56a6be/README.md), [group-chat acceptance host](https://github.com/mist-agent-harness/mist-agent/blob/4e87b332140ce3d2eabeff7b4e16532c2c56a6be/src/group-chat/host-process.ts).
- Basis: bounded negative.
- Confidence: medium-high.
- Caveats: future deployed multi-resident/group-chat paths may change the finding.

### Absence scope

- Surfaces inspected: resident CLI, host lock, turn gate, group-chat acceptance host, roster and setup/design docs.
- Plausible first-party paths checked: concurrent resident processes, same-resident turn ordering, group-chat broadcast/mention prototypes and sessions across generations.
- Why no material first-party path remains: only the one-resident operating path is demonstrated; acceptance harness interactions are not sufficient standard-distribution inter-S1 coordination.

## S3 — Inside-and-now control

- State: —
- Function: no actor with a whole-current portfolio view and consequential cross-unit operating control is established at the inspected recursion.
- Disturbance / variety regulated: unreconciled turns, ledger mismatch, aborted generation or malformed history are handled as local correctness/lifecycle failures.
- Decisive decision or feedback right: deterministic runtime blocks or retries one stream, may request human reconciliation, but does not make a whole-system current-allocation decision.
- Decision owner: fixed implementation and occasional human host operator for repairs, not an evidenced current portfolio controller.
- Supporting / enforcement mechanisms: `TurnReceiptStore`, `SessionRegistry`, canonical stream, fact delivery settlement and breath failure notices.
- Closure path: broken receipt/letter/stream → fail-closed refusal or human repair suggestion → retry/restart of that resident; no whole-system S3 current-control loop.
- Why this is / is not agent-owned: integrity gates and continuity notifications are strong reliability engineering, not metasystem management of a distributed set of operational cells.
- Evidence: [runtime write and reconciliation](https://github.com/mist-agent-harness/mist-agent/blob/4e87b332140ce3d2eabeff7b4e16532c2c56a6be/src/resident-runtime/runtime.ts), [generation breath failure paths](https://github.com/mist-agent-harness/mist-agent/blob/4e87b332140ce3d2eabeff7b4e16532c2c56a6be/src/session/breath-cycle.ts).
- Basis: bounded negative.
- Confidence: medium-high.
- Caveats: the user's control over one resident is not the same as first-party whole-system S3 at a multi-unit recursion.

### Absence scope

- Surfaces inspected: runtime assembly, TUI, breath cycle, fact ledger, turn receipts, installer and acceptance-only administration.
- Plausible first-party paths checked: runtime health/failure receipts, admin acceptance group-chat, retry gate, session generation replacement and handover handling.
- Why no material first-party path remains: all are single-resident state-integrity functions or nonproduction test controls; no live portfolio current view → authoritative intervention → changed S1 operating choice.

## S3* — Complementary audit

- State: —
- Function: no independent operational auditor challenges normal resident claims and returns a separate evidence-based correction to control.
- Disturbance / variety regulated: history corruption, ledger mismatches and repair failures have ordinary structural detection or independent test-suite evidence, but these are not live S3* auditing.
- Decisive decision or feedback right: source validators and acceptance/eval runners check contracts; no independently empowered resident auditor may override operating claims.
- Decision owner: deterministic contract checks, test drivers and external maintainers rather than a deployed complementary-audit S1/S3 separation.
- Supporting / enforcement mechanisms: ledger invariants, stream hygiene checks, `acceptance/` and `src/eval/resident-self-repair` outside the operating path.
- Closure path: observed invalid state → local refusal/reconciliation, or offline red/green evaluation; not a distinct independent finding → current-controller correction.
- Why this is / is not agent-owned: append-only records provide evidence potential but are not independent examination by themselves.
- Evidence: [README acceptance vs operational runtime distinction](https://github.com/mist-agent-harness/mist-agent/blob/4e87b332140ce3d2eabeff7b4e16532c2c56a6be/README.md), [runtime reconciliation](https://github.com/mist-agent-harness/mist-agent/blob/4e87b332140ce3d2eabeff7b4e16532c2c56a6be/src/resident-runtime/runtime.ts), [eval runner](https://github.com/mist-agent-harness/mist-agent/blob/4e87b332140ce3d2eabeff7b4e16532c2c56a6be/src/eval/resident-self-repair/runner.ts).
- Basis: bounded negative.
- Confidence: high.
- Caveats: external human audit and acceptance results may independently verify engineering quality but remain outside this agent operating recursion.

### Absence scope

- Surfaces inspected: one-stream integrity guards, independent acceptance declarations, self-repair eval runner, fact-ledger validator and TUI reports.
- Plausible first-party paths checked: independent review assertions, append-only historical auditability, runtime health/turn checks and failure notification.
- Why no material first-party path remains: the cited mechanisms are either routine consistency gates or offline experiments, without a separate operational auditor and returned S3*-specific authority.

## S4 — Outside-and-then intelligence

- State: —
- Function: no autonomous or parent-operated future-environment sensing and capability-adaptation loop is shown in the shipped runtime.
- Disturbance / variety regulated: future remembered commitments and context-window replacement are inside ongoing conversation continuity, not external scenario change.
- Decisive decision or feedback right: human may configure model or persona; resident generates ordinary text replies; no distinct future capability-option decision owner.
- Decision owner: installer choice and resident chat model, with no demonstrated S4 adaptive authority.
- Supporting / enforcement mechanisms: model selection, handover letter, current-fact pointer, lifetime threshold and session reconstruction.
- Closure path: context threshold → deterministic breath → new conversation receives prior letter and facts; does not select a strategic change in operational capacity from environmental alternatives.
- Why this is / is not agent-owned: a letter about future commitments is memory continuity, not Beer S4 outside-and-then intelligence.
- Evidence: [README handover and fact semantics](https://github.com/mist-agent-harness/mist-agent/blob/4e87b332140ce3d2eabeff7b4e16532c2c56a6be/README.md), [breath cycle](https://github.com/mist-agent-harness/mist-agent/blob/4e87b332140ce3d2eabeff7b4e16532c2c56a6be/src/session/breath-cycle.ts), [model transport](https://github.com/mist-agent-harness/mist-agent/blob/4e87b332140ce3d2eabeff7b4e16532c2c56a6be/src/resident-runtime/pi-transport.ts).
- Basis: bounded negative.
- Confidence: high.
- Caveats: future planned goals and modules in docs are not credited until a supported operating closure exists.

### Absence scope

- Surfaces inspected: handover letters, model/installer configuration, session expiration, `bootpack`, fact commitments and design/acceptance maps.
- Plausible first-party paths checked: long-term commitments, model switching, prospective memory fields, reset/compaction and intentional work reminders.
- Why no material first-party path remains: none carries external future scanning → option judgment → actual changed present operating capability.

## S5 — Policy and identity

- State: A
- Function: authorize or refuse the resident's foundational proposed identity before that resident may exist and operate, preserving the decision as the active governing persona.
- Disturbance / variety regulated: a human may submit an unacceptable persona; user or installer should not silently create an agent identity by projecting its own claimed consent.
- Decisive decision or feedback right: model receives proposed identity and explicit first-person attestation question, selects `认` (accept) or `不认` (reject); undecided output cannot open an active resident. The accepted decision becomes the registry's first persona, mandatory for later runtime entry.
- Decision owner: candidate resident model for this narrow formation-time identity decision, conditional on the human's choice to propose it and the fixed parser/registry recognizing a definitive answer.
- Supporting / enforcement mechanisms: live pi model request with submitted persona in boot pack, strict first-line verdict parser, `createCandidate` and `attestCandidate` registry transition, atomic resident-persona activation, `requireActiveResident` runtime gate.
- Closure path: human proposes foundational identity → model decides accept/reject → first-party registry records candidate rejection or creates active resident with approved persona → `npm run resident` opens ordinary chat only if active, carrying that identity in subsequent boot packs.
- Boundary reachability: documented `npm run setup` → `npm run resident` onboarding invokes the real model transport and same `ResidentIdentityStore` used to gate subsequent terminal use; no external governance process or acceptance driver is required.
- Why this is / is not agent-owned: the model's yes/no content is the decisive identity verdict, not merely a human approval or static system prompt; software enforces and persists its choice. This does **not** establish agent authority to modify every future identity or decide societal policies.
- Identity-level issue and authority: whether the proposed persona may define the resident's identity; only the candidate model's unambiguous self-attestation is recognized by the shipped onboarding flow.
- Return into subsequent operation: acceptance commits an active `ResidentRecord` with first persona version, and later `requireActiveResident` supplies that identity for every normal session; rejection prevents resident admission.
- Evidence: [production onboarding prompt/verdict and actual model invocation](https://github.com/mist-agent-harness/mist-agent/blob/4e87b332140ce3d2eabeff7b4e16532c2c56a6be/src/resident-runtime/onboarding.ts), [atomic active-persona admission](https://github.com/mist-agent-harness/mist-agent/blob/4e87b332140ce3d2eabeff7b4e16532c2c56a6be/src/resident-continuity/identity-store.ts), [README documented installation and subsequent entry](https://github.com/mist-agent-harness/mist-agent/blob/4e87b332140ce3d2eabeff7b4e16532c2c56a6be/README.md).
- Basis: explicit identity decision plus first-party authoritative return to subsequent operation.
- Confidence: medium-high.
- Caveats: it is a single initial identity-formation checkpoint, not a continuous system-wide policy balancing forum; actor attribution is based on transport response and a constructed candidate actor token, not a cryptographic proof of selfhood. The user controls the proposed persona and model provider.

## Distributed OSS parent arrangement

Maintainers publish the open-source harness and users install distinct resident instances. There is no shared cross-installation executive or policy board in the operating product; the resident's S5 is scoped to its own formation, not ecosystem governance.

## Self-hosted and non-human modes

First-time CLI onboarding carries the model's identity decision into the registry. Subsequent TUI text responses remain model-owned S1 and durability/integrity processes remain deterministic. The external pi CLI is configured without tools, skills, extensions or agent sessions in the operating mode, preventing inference of external agentic file actions into mist's S1.

## Recursion

One resident persists across multiple windows and generations; these are not independently governed S1 subunits. The identity decision is a narrow S5 at the resident level, while future group-chat organization is not claimed from acceptance-only drivers.

## Variety and escalation

Invalid identity answer cannot activate a candidate. Ambiguous same-turn ACK, ledger corruption and incomplete letter state fail closed with actionable human repair/retry; these local anomalies are not evidence for S3 or independent S3* without a separate current-control or audit pathway.

## Evidence gaps

No paid-provider live onboarding, crash-injection test or user-field study was performed. The assessment is based on production CLI wiring and source-level close of the identity decision and turn pipeline. It does not assess the subjective personhood of a model, only the coded right to accept/reject a resident persona. Group chat and planned frontend functions remain out of boundary.

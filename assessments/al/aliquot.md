---
harness_id: aliquot
project_name: Aliquot
repository: https://github.com/oneirum/aliquot
review_ref: 7ddf55990998cd33a76d181c24fd5727d4788bec
reviewed_at: 2026-11-03
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-11-03
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Aliquot

## Review boundary

- System in focus: Aliquot's installable lab knowledge and question-answering harness, including its own model/tool loop, gateway, data-class gate, worker, published agent cards, and run journal.
- Purpose and identity: Answer lab questions against authorized SOPs, data and literature while keeping restricted information out of disallowed model locations and recording the activity.
- Relevant environment: Lab staff and stewards, SOP/KB documents, local datasets, model endpoints and external agent CLIs, research APIs, data-class restrictions, PostgreSQL and optional sandbox.
- Standard-distribution boundary: Shipped Node/TypeScript core, web/front-door entry, job worker, first-party model-endpoint loop and optional explicitly confined external Claude Code/Codex backend. Default scripted demo illustrates wiring but does not prove live model quality.
- Credited operating / distribution surfaces: [loop.ts](https://github.com/oneirum/aliquot/blob/7ddf55990998cd33a76d181c24fd5727d4788bec/packages/core/src/loop.ts), [gateway.ts](https://github.com/oneirum/aliquot/blob/7ddf55990998cd33a76d181c24fd5727d4788bec/packages/core/src/gateway.ts), [agent.ts](https://github.com/oneirum/aliquot/blob/7ddf55990998cd33a76d181c24fd5727d4788bec/packages/core/src/agent.ts), [worker.ts](https://github.com/oneirum/aliquot/blob/7ddf55990998cd33a76d181c24fd5727d4788bec/packages/core/src/worker.ts), [gate.ts](https://github.com/oneirum/aliquot/blob/7ddf55990998cd33a76d181c24fd5727d4788bec/packages/core/src/gate.ts), [record.ts](https://github.com/oneirum/aliquot/blob/7ddf55990998cd33a76d181c24fd5727d4788bec/packages/core/src/record.ts).
- Adjacent first-party surfaces excluded from ownership: Scripted fake-model demo, tests and CI, research/evaluation scaffolds, lab staff publishing workflow as a human decision, model vendors and external Claude Code/Codex's independent internals. The last two are dependencies, not Aliquot-native agent governors.
- First-party operating / deployment modes considered: One lab question through a published agent using a first-party model endpoint; optional external agent-CLI backend with tool confinement; web/studio publication and class-gated KB; worker crash recovery from a durable journal.
- Recursion level: One lab-facing question/agent run within a lab deployment; tools, retries and worker leases are not separately viable operational units.
- Reviewed revision: `7ddf55990998cd33a76d181c24fd5727d4788bec`.
- Observation date: 2026-11-03.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The web/front-door classifies the incoming question before the worker asks a model. A published agent document pins model endpoint, data ceiling, knowledge bases, tools and limits. The first-party `loop.ts` restores journal state, prepares prompts, sends model requests, executes the selected tools and appends tool results before another model decision. `record.ts` uses a fenced lease and hash-chained events to recover after crashes; `gate.ts` and `dataclass.ts` refuse disallowed data egress. A separate supported mode confines an already-installed Claude Code or Codex process to an Aliquot tool bridge; that CLI's inner planning is not first-party Aliquot control. Studio publication requires a human role, draft validation and a version-head transaction; `router.ts` currently leaves model routing and overlap decisions unimplemented. [README](https://github.com/oneirum/aliquot/blob/7ddf55990998cd33a76d181c24fd5727d4788bec/README.md), [loop.ts#L75-L130](https://github.com/oneirum/aliquot/blob/7ddf55990998cd33a76d181c24fd5727d4788bec/packages/core/src/loop.ts#L75-L130), [router.ts](https://github.com/oneirum/aliquot/blob/7ddf55990998cd33a76d181c24fd5727d4788bec/packages/core/src/router.ts).

## Operational model

The substantive operational unit is one model-driven lab agent: it decides which authorized retrieval/research/data tool to use and interprets returned evidence for the question. A worker and retry controller preserve this loop, without deciding the content of the answer. A lab publisher controls which agent version is made live; that local human stewardship is an important boundary but does not by itself establish a whole-deployment VSM control, audit or identity-policy loop. Multiple configured agent cards do not by themselves provide a coordinated multi-agent S1 collective at this recursion.

## S1 — Operations

- State: A
- Function: Lab question-answering through a model-selected evidence and tool feedback loop.
- Disturbance / variety regulated: Unfamiliar SOP wording, changing questions, heterogeneous KB/research results, tool failures and authorization refusals.
- Decisive decision or feedback right: Interpret the request, choose permitted tools, inspect results, make subsequent inquiries and compose the answer.
- Decision owner: The configured model in the shipped first-party model-endpoint loop; the external model service supplies inference but not Aliquot's orchestration/authorization path.
- Supporting / enforcement mechanisms: Agent document and version hash, gateway, bounded step/token/time limits, gate, tool policies, journal and fenced worker lease.
- Closure path: Question → class gate → model prompt → model-chosen tool call → recorded tool result/refusal → next model decision or final reply.
- Boundary reachability: `drive()` and `next()` are invoked by the installable worker for a published agent on a direct model endpoint; this does not depend on the optional external agent-CLI backend or fake demo.
- Why this is / is not agent-owned: The model chooses substantive search and reasoning actions in a repeated closed loop; fixed data policy and the worker do not select which evidence answers the question.
- Evidence: [loop.ts#L75-L130](https://github.com/oneirum/aliquot/blob/7ddf55990998cd33a76d181c24fd5727d4788bec/packages/core/src/loop.ts#L75-L130), [loop.ts#L211-L320](https://github.com/oneirum/aliquot/blob/7ddf55990998cd33a76d181c24fd5727d4788bec/packages/core/src/loop.ts#L211-L320), [agent.ts#L110-L149](https://github.com/oneirum/aliquot/blob/7ddf55990998cd33a76d181c24fd5727d4788bec/packages/core/src/agent.ts#L110-L149).
- Basis: explicit + structural
- Confidence: high for shipped architectural loop; no claim of live model answer accuracy.
- Caveats: Requires deployment, model credentials or a local endpoint, database and selected tools; the fake-model demo is not evidence of externally served model quality.

## S2 — Coordination

- State: —
- Function: No shipped inter-S1 oscillation/conflict regulator for two distinct operating lab agents in the selected run boundary.
- Disturbance / variety regulated: Parallel independent questions could conflict on resources or answers, but the examined mechanisms chiefly serialize one run's writes and select a single published agent.
- Decisive decision or feedback right: Negotiate or change behaviour across multiple S1 agents following a detected conflict; no such shipped decision identified.
- Decision owner: No qualifying S2 owner. Worker lease and publication lock are deterministic transaction controls.
- Supporting / enforcement mechanisms: PostgreSQL run leases and inbox, tool policy, version-head publishing and channel binding.
- Closure path: One run's model/tool cycle is repaired locally; no cross-agent mutual adjustment is returned to two distinct S1 cells.
- Why this is / is not agent-owned: Multiple agent documents, model choices or isolated question runs do not themselves establish the four-part S2 conflict-and-attenuation witness.
- Evidence: [record.ts#L4-L19](https://github.com/oneirum/aliquot/blob/7ddf55990998cd33a76d181c24fd5727d4788bec/packages/core/src/record.ts#L4-L19), [publish.ts#L118-L170](https://github.com/oneirum/aliquot/blob/7ddf55990998cd33a76d181c24fd5727d4788bec/packages/core/src/publish.ts#L118-L170), [router.ts#L49-L69](https://github.com/oneirum/aliquot/blob/7ddf55990998cd33a76d181c24fd5727d4788bec/packages/core/src/router.ts#L49-L69).
- Basis: structural
- Confidence: medium-high in declared run boundary.
- Caveats: A lab could build a multi-agent work organization around Aliquot, but that is not evidenced as shipped S2 here.

### Absence scope

- Surfaces inspected: Agent/card schema, worker, run journal/inbox, publish/channel binding, router stubs, CLI bridge and README operational modes.
- Plausible first-party paths checked: Shared job queue/leases, channel collisions, cross-agent routing and configured multiple agent cards.
- Why no material first-party path remains: Those paths prevent technical duplicate writes or leave routing unfinished; none closes a specifically inter-S1 disturbance by feeding a coordination judgment back into distinct agent operations.

## S3 — Inside-and-now control

- State: —
- Function: No separate whole-current control over multiple operational cells with discretionary cross-unit resource/commitment regulation.
- Disturbance / variety regulated: Per-run limits, model outages, approval decisions and data-class restrictions are current operational constraints.
- Decisive decision or feedback right: Observe whole-deployment commitments and choose cross-run priorities, budgets or corrective reallocations; not supplied by the running agent harness.
- Decision owner: Human publisher selects versions and operator configures limits; fixed worker logic implements preselected constraints.
- Supporting / enforcement mechanisms: `Limits`, worker lease, per-class model routing, role-based publish gate and run status.
- Closure path: Fixed limits/errors return to the same S1 or a publisher updates a version; no distinct S3 whole-current decision returns to multiple S1 units.
- Why this is / is not agent-owned: Run supervision, a console and publish authorization do not prove whole-system management discretion.
- Evidence: [agent.ts#L27-L36](https://github.com/oneirum/aliquot/blob/7ddf55990998cd33a76d181c24fd5727d4788bec/packages/core/src/agent.ts#L27-L36), [roles.ts](https://github.com/oneirum/aliquot/blob/7ddf55990998cd33a76d181c24fd5727d4788bec/packages/core/src/roles.ts), [publish.ts](https://github.com/oneirum/aliquot/blob/7ddf55990998cd33a76d181c24fd5727d4788bec/packages/core/src/publish.ts).
- Basis: structural
- Confidence: medium-high.
- Caveats: The lab organization may have human governance outside this repository's deployable runtime; it cannot be borrowed into the harness state.

### Absence scope

- Surfaces inspected: Loop limits, worker schedules and leases, role/publish transactions, live agent head, router and run ledger.
- Plausible first-party paths checked: Per-run resource limits, publisher overrides, version rollout, channel routing and operational status.
- Why no material first-party path remains: No current whole-of-deployment view connected to a separately owned multi-cell allocation or intervention decision with returned closure was found.

## S3* — Complementary audit

- State: —
- Claim being audited: Whether lab answer/agent operation corresponds to primary data and to permitted handling rules.
- Ordinary reporting path: Model/tool events and tool payload references in the journal, with final reply and error/refusal record.
- Complementary access path: Hash-chain verification and audit-event inspection validate record integrity, but they are derived from the same operational recorder; no separately wired challenge of answer truth is returned as an auditor verdict.
- Independence boundary: Run-journal and out-of-run audit stream share first-party instrumentation; optional developer checks or lab review are not a shipped independent S3* owner.
- Who acts on findings: User may inspect the trace; no installed complementary reviewer controls a returned corrective re-execution decision.
- Function: No positively established independent complementary audit regulation of first-party S1 claims.
- Disturbance / variety regulated: Missing/altered logs and policy refusals are made visible or mechanically rejected, without a separate audit of actual task truth.
- Decisive decision or feedback right: Independently sample/reconcile operational reality, issue a finding and require a correction; not wired.
- Decision owner: None established; deterministic hash verification is support/integrity enforcement.
- Supporting / enforcement mechanisms: Append-only fenced journal, `verifyChain`, global audit events and publication validation.
- Closure path: Event → hash-chain record → human-visible record; no independent audit finding returns to change model behavior or deployed controls.
- Why this is / is not agent-owned: An immutable event log and conventional evaluation capability are not independent discretionary audit judgment.
- Evidence: [record.ts#L4-L19](https://github.com/oneirum/aliquot/blob/7ddf55990998cd33a76d181c24fd5727d4788bec/packages/core/src/record.ts#L4-L19), [audit.ts](https://github.com/oneirum/aliquot/blob/7ddf55990998cd33a76d181c24fd5727d4788bec/packages/core/src/audit.ts), [publish.ts#L18-L25](https://github.com/oneirum/aliquot/blob/7ddf55990998cd33a76d181c24fd5727d4788bec/packages/core/src/publish.ts#L18-L25).
- Basis: explicit + structural
- Confidence: medium-high for standard run and publication paths.
- Caveats: A separate downstream human auditor could use the record, but access to records alone does not establish first-party S3* closure.

### Absence scope

- Surfaces inspected: Run journal/chain verifier, global audit stream, publish validation, demo/test surfaces and lab record presentation.
- Plausible first-party paths checked: Tamper verification, recorded source/tool evidence, independent evaluation on publication and agent-CLI self-checks.
- Why no material first-party path remains: The deployed paths verify their own event consistency or validate configuration; they do not install a complementary independent judgment over S1 task reality and return actionable correction.

## S4 — Outside-and-then intelligence

- State: —
- Function: No first-party prospective external sensing → adaptation-option decision → current capability revision loop at this deployment recursion.
- Disturbance / variety regulated: Literature/search updates, changing lab knowledge and data sources are task inputs, not automatically strategic adaptation.
- Decisive decision or feedback right: Identify future environmental changes and choose enduring changes to the deployed lab agent capability; not wired into operations.
- Decision owner: A human steward or author may update agent cards/KBs; running models use research tools to answer current questions.
- Supporting / enforcement mechanisms: KB compilation, research APIs, versioned published documents, snapshots and model endpoint configuration.
- Closure path: New documents and edits are validated and published by people, while the agent's research result returns to one current answer, not a future-oriented capability-governance loop.
- Why this is / is not agent-owned: Retrieval from an external corpus and routine card publication are not a separate prospective adaptation decision owner.
- Evidence: [README](https://github.com/oneirum/aliquot/blob/7ddf55990998cd33a76d181c24fd5727d4788bec/README.md), [publish.ts#L102-L170](https://github.com/oneirum/aliquot/blob/7ddf55990998cd33a76d181c24fd5727d4788bec/packages/core/src/publish.ts#L102-L170), [kb-compile.ts](https://github.com/oneirum/aliquot/blob/7ddf55990998cd33a76d181c24fd5727d4788bec/packages/core/src/kb-compile.ts).
- Basis: structural
- Confidence: medium-high.
- Caveats: A separately governed laboratory can plan future KB changes; those decisions are not a shipped autonomous S4 mode.

### Absence scope

- Surfaces inspected: Research tool entry, knowledge publication, agent versions, router, run loop and lab author/steward roles.
- Plausible first-party paths checked: Model research search, coverage checks, human card iteration, feedback from run records and provider selection.
- Why no material first-party path remains: No first-party agent/parent loop transforms prospective outside distinctions into an authoritative persistent capability option and returns it to present operation.

## S5 — Policy and identity

- State: —
- Function: No first-party runtime closure of identity/ultimate-policy tensions at the selected agent deployment recursion.
- Disturbance / variety regulated: Restricted lab data, egress risk and publish authority are governed by configured roles and safety policy.
- Decisive decision or feedback right: Decide a disputed identity/ultimate-policy matter and return an authoritative amendment to operation; not implemented in the deployed run path.
- Decision owner: Lab administrators and data stewards externally set roles/classification and publish versions; class gates enforce those choices.
- Supporting / enforcement mechanisms: `roles.ts`, `gate.ts`, classified egress policy, publishing transaction and agent configuration.
- Closure path: A preselected role/classification produces permission/refusal at runtime; no identity-level appeal → legitimate parent judgment → returned new policy path is evidenced.
- Why this is / is not agent-owned: Strong static confidentiality rules are real safeguards, not S5 discretionary policy governance by an agent or complete parent mode.
- Evidence: [roles.ts](https://github.com/oneirum/aliquot/blob/7ddf55990998cd33a76d181c24fd5727d4788bec/packages/core/src/roles.ts), [gate.ts#L1-L100](https://github.com/oneirum/aliquot/blob/7ddf55990998cd33a76d181c24fd5727d4788bec/packages/core/src/gate.ts#L1-L100), [publish.ts](https://github.com/oneirum/aliquot/blob/7ddf55990998cd33a76d181c24fd5727d4788bec/packages/core/src/publish.ts).
- Basis: structural
- Confidence: medium-high for the deployed path.
- Caveats: A PI may legitimately control lab policy in a wider human organization; that wider recursion was not credited without explicit identity-decision return evidence.

### Absence scope

- Surfaces inspected: Role model, data-class gate, publish permissions, agent policy and versioning, runtime entry and lab README governance explanations.
- Plausible first-party paths checked: PI and steward roles, restricted-data refusal, publish approval, model-placement ceilings and operator configuration.
- Why no material first-party path remains: These paths enforce previously selected policies or authorize ordinary agent/document publication; no supported identity/ultimate-policy decision and return process is wired.

## Distributed OSS parent arrangement

Repository maintainers, lab publishers and different local lab administrators do not form an evidenced project-level S3/S4/S5 parent mode for this deployed agent run merely by configuring agent versions or publishing code. An independently governed lab may have those functions outside the examined system boundary.

## Self-hosted and non-human modes

Aliquot can route permitted classes to local model endpoints, while hosted model and separate agent CLI configurations remain subject to the same gate. Hosting location changes data eligibility, not the identified VSM owner or a separate autonomous non-human metasystem.

## Recursion

One question-answering agent run is the operational cell. Worker retries, model/tool calls, KB search and independent users of the installed service are not evidence of a second recursively viable operational organization.

## Variety and escalation

Model choice and search tools amplify answer repertoire; data-class gates attenuate unsafe egress; durable journal and lease fencing recover execution-state variety. Restricted requests are refused before model access; routine tool failure returns to the same S1 model, while publication changes belong to lab personnel. A refusal or dashboard flag is not itself an algedonic signal or S3/S5 right.

## Evidence gaps

- No live provider-backed lab task or independent audit run was executed in this assessment; reviewed source establishes supported organizational pathways, not answer accuracy or safety effectiveness.
- Lab-specific deployment, operator governance and outside reviewer practices may differ from the shipped default; they are not silently credited as first-party VSM ownership.

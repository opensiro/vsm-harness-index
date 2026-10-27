---
harness_id: manyhands
project_name: Manyhands
repository: https://github.com/mjoneill/manyhands
review_ref: 94010f1227d03152f6d745f7da2fd89ef06d0a96
reviewed_at: 2026-10-27
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: ?
---

# Manyhands

## Review boundary

- System in focus: the shipped Manyhands shared-work board and optional resident/guest agent runner, not its development organization.
- Purpose and identity: keep collaborative work, conversations and memory available across sessions and agent harnesses.
- Relevant environment: local human operators, peer seats, shared cards/graph, model endpoints and externally connected MCP clients.
- Standard-distribution boundary: self-hosted Node board, MCP adapter, documented guest-once runner and their shipped modules; optional graph-backed mode is considered with its documented installation limitations.
- Credited operating / distribution surfaces: README.md; server.js; mcp-server.mjs; scripts/guest-once.mjs; core/guest-loop.mjs; core/tool-loop.mjs; core/board-tools.mjs; core/agent-constraints.mjs; live agent registry/constraints/model-call routes.
- Adjacent first-party surfaces excluded from ownership: named maintainer development seats and their private harnesses, screenshot board history, graph trial bootstrap, seeding/measurement fixtures and tests. The graph trial API explicitly lacks checks on who may create grants/rules; do not treat its existence as legitimate ultimate authority.
- First-party operating / deployment modes considered: dependency-free local board, installed MCP adapter, configured resident runner, graph-backed operation where supported.
- Recursion level: one collaborative workspace; resident wakes are operational units. A private contributor organization is outside this recursion.
- Reviewed revision: 94010f1227d03152f6d745f7da2fd89ef06d0a96.
- Observation date: 2026-10-27.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The board persists cards, wiki and conversations with event history, optional RDF graph storage and a shared REST/MCP interface. The local quickstart alone is a work-state service, not an autonomous agent. However the repository also ships a resident runner: it resolves a configured agent, discovers mentions/deliveries, assembles bounded context and memory, calls a model adapter, executes granted tools across model turns and posts a result. Registry grants, budgets and prompt versions are read back at subsequent wakes. External Claude/Codex seats use their own harnesses and are not borrowed as the resident S1 owner. Claim and version checks address specific duplicate-work and lost-update hazards. Maintainer commentary and model-quality measurements describe adjacent development/evaluation, not autonomous product control.

## Operational model

A configured resident autonomously decides what to inspect and how to answer a wake, including self-state/memory actions; deterministic code enforces tool grants, hop limits and persistence. Shared-board claim/version rails expose a coordination-specific construction path to separately wired seats. A local operator can inspect cross-seat constraints/spend and change the agents' current budgets, grants or state. This supports a narrow parent-owned current-control mode; it does not prove autonomous whole-workspace management.

Primary evidence below uses immutable links at the reviewed SHA.

## S1 — Operations

- State: A
- Function: produce grounded collaborative responses and board-directed actions from a resident wake.
- Disturbance / variety regulated: varying requests, missing board facts, tool errors, bounded context and pending deliveries.
- Decisive decision or feedback right: choose queries/tool arguments and response/directives after seeing returned data.
- Decision owner: the model-backed resident agent.
- Supporting / enforcement mechanisms: mention/delivery scanner, model adapter, grant filtering, tool executor, hop ceiling, memory/ledger storage and publication outbox.
- Closure path: tool results enter the next model turn; the resulting post, own-state declaration or memory update changes shared work or subsequent wakes.
- Boundary reachability: scripts/guest-once.mjs wires the shipped model adapter and executor to core/guest-loop.mjs; core/tool-loop.mjs supplies call/execute/call. Configuring endpoint and seat does not require writing a new decision loop.
- Why this is / is not agent-owned: removing the model leaves scanning and enforcement but no discretionary query/response selection.
- Evidence: [runner](https://github.com/mjoneill/manyhands/blob/94010f1227d03152f6d745f7da2fd89ef06d0a96/scripts/guest-once.mjs#L23-L92), [resident loop](https://github.com/mjoneill/manyhands/blob/94010f1227d03152f6d745f7da2fd89ef06d0a96/core/guest-loop.mjs#L837-L890), [tool feedback](https://github.com/mjoneill/manyhands/blob/94010f1227d03152f6d745f7da2fd89ef06d0a96/core/tool-loop.mjs#L95-L177), [tool grants](https://github.com/mjoneill/manyhands/blob/94010f1227d03152f6d745f7da2fd89ef06d0a96/core/board-tools.mjs#L208-L216).
- Basis: structural.
- Confidence: high.
- Caveats: board-only quickstart has no autonomous S1; no live model-quality run was performed.

## S2 — Coordination

- State: C
- Function: prevent duplicate work and stale overwrites between peer operational seats.
- Disturbance / variety regulated: two seats claiming the same card, or replacing shared fields from stale snapshots.
- Decisive decision or feedback right: accept/yield a card claim and revise work after an incumbent/version conflict.
- Decision owner: configured participating seats must own the yielding/reselection behaviour; the board supplies specific claim/conflict feedback, not a centrally autonomous coordinator.
- Supporting / enforcement mechanisms: first-writer claim, 409 incumbent response, holder release, serialized writes and ifVersion checks.
- Closure path: MCP instruction explicitly says a 409 names the holder and means yield, not retry; conflict data is returned to the calling seat before further work.
- Boundary reachability: the installed MCP adapter intentionally exposes this claim protocol to peer agent clients; wiring those operational actors remains the consumer's responsibility.
- Distinct S1 units: independently connected work-producing peer seats.
- Inter-S1 disturbance: duplicate effort on one card and concurrent replacement of acceptance/blocker/check arrays.
- Attenuating coordination relation: claim-before-work, yield-on-conflict, fresh version before replacement.
- Feedback into subsequent S1 behaviour: incumbent/version feedback causes the consumer to yield or refresh rather than continue stale work.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the protocol identifies concrete collision types and prescribes a corrective return, beyond a mailbox or generic board.
- Why this is / is not agent-owned: the shipped resident does not independently demonstrate closed peer work arbitration; external consumer composition is still required, so A is not claimed.
- Evidence: [MCP coordination rail and claim handling](https://github.com/mjoneill/manyhands/blob/94010f1227d03152f6d745f7da2fd89ef06d0a96/mcp-server.mjs#L333-L408), [bounded conflict guarantees](https://github.com/mjoneill/manyhands/blob/94010f1227d03152f6d745f7da2fd89ef06d0a96/README.md#L174-L177), [server claim response boundary](https://github.com/mjoneill/manyhands/blob/94010f1227d03152f6d745f7da2fd89ef06d0a96/server.js#L1020-L1044).
- Basis: structural.
- Confidence: high.
- Caveats: cooperative claims do not prevent malicious writes; a deterministic lock is support rather than an agent owner.

## S3 — Inside-and-now control

- State: P
- Function: operator regulation of the currently running workspace's resident capacity and commitments.
- Disturbance / variety regulated: paid model use, unavailable seats and agents operating under unsuitable grants or limits.
- Decisive decision or feedback right: inspect current seat/spend/constraint data and change budget, grants, active state or hop allowance.
- Decision owner: the self-hosting workspace operator in this parent mode.
- Supporting / enforcement mechanisms: registry PATCH validation, per-agent constraints, ledger aggregation, budget precheck and resting/retired checks.
- Closure path: subsequent runner invocations read current registry values; breached budgets leave deliveries unclaimed, and retired agents are not woken. Rest/retire also reconciles outstanding claims.
- Boundary reachability: server list/constraints/PATCH routes and the runner's --seat mode are first-party operating interfaces; no development-only manager is credited.
- Whole-system current view: operator can list the workspace agents and model calls and inspect each seat's claims, current constraints and daily expenditure.
- Current-control decision scope: shared current agent capacity and spending commitments, including intervention on a particular seat for the workspace.
- Why this is / is not agent-owned: the operator selects revised constraints; no built-in agent is shown owning that cross-seat supervisory discretion. Runtime budget comparisons merely enforce the selected decision.
- Evidence: [registry/current constraints/intervention](https://github.com/mjoneill/manyhands/blob/94010f1227d03152f6d745f7da2fd89ef06d0a96/server.js#L5269-L5450), [spend and constraints projection](https://github.com/mjoneill/manyhands/blob/94010f1227d03152f6d745f7da2fd89ef06d0a96/core/agent-constraints.mjs#L80-L120), [current registry read](https://github.com/mjoneill/manyhands/blob/94010f1227d03152f6d745f7da2fd89ef06d0a96/scripts/guest-once.mjs#L62-L93), [budget before delivery claim](https://github.com/mjoneill/manyhands/blob/94010f1227d03152f6d745f7da2fd89ef06d0a96/scripts/guest-once.mjs#L349-L378).
- Basis: structural.
- Confidence: medium.
- Caveats: parent legitimacy is the local workspace operator's deployment authority; public project-level maintainer governance and external client limits are not credited.

## S3* — Complementary audit

- State: —
- Function: no shipped independently controlled complementary audit of residents' operational claims established.
- Disturbance / variety regulated: unsupported claims and unreliable reported work are relevant risks.
- Decisive decision or feedback right: no separate audit judgment and corrective return established.
- Decision owner: none established at this boundary.
- Supporting / enforcement mechanisms: tool-hop ledger, provenance guards, event history and tripwire checks.
- Closure path: routine grounding/refusal feedback exists inside production; it is not an independent audit channel.
- Why this is / is not agent-owned: recording rows and checking producer-authored claims does not supply a complementary autonomous auditor.
- Evidence: [production loop and its explicit limits](https://github.com/mjoneill/manyhands/blob/94010f1227d03152f6d745f7da2fd89ef06d0a96/core/tool-loop.mjs#L1-L29), [tripwire comparison](https://github.com/mjoneill/manyhands/blob/94010f1227d03152f6d745f7da2fd89ef06d0a96/core/check-compare.mjs#L1-L98), [development attribution boundary](https://github.com/mjoneill/manyhands/blob/94010f1227d03152f6d745f7da2fd89ef06d0a96/README.md#L194-L210).
- Basis: structural.
- Confidence: medium.
- Caveats: collaborators may audit independently outside the supplied resident path.

### Absence scope

- Surfaces inspected: resident/tool loops, board/MCP checks and model-call/event records; README development/evaluation account.
- Plausible first-party paths checked: hop provenance, card falsifier checks, graph comparison and named development seats reviewing one another.
- Why no material first-party path remains: checks are routine or authored through the same operating path; private development reviewers are outside the assessed distribution and no shipped independent audit actor/return is supplied.

## S4 — Outside-and-then intelligence

- State: —
- Function: no supported external/prospective adaptation loop into resident capability established.
- Disturbance / variety regulated: model/environment changes could demand future capability adaptation.
- Decisive decision or feedback right: no shipped prospective option-selection and current-capability return established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: model configuration, prompt versions, persistent memory and development research notes.
- Closure path: ordinary memory/context changes return to wakes, without a demonstrated externally oriented adaptation function.
- Why this is / is not agent-owned: configurable models and remembered conversation are not themselves outside-and-then intelligence.
- Evidence: [resident memory and prompt context](https://github.com/mjoneill/manyhands/blob/94010f1227d03152f6d745f7da2fd89ef06d0a96/core/guest-loop.mjs#L530-L708), [model/prompt operator changes](https://github.com/mjoneill/manyhands/blob/94010f1227d03152f6d745f7da2fd89ef06d0a96/server.js#L5308-L5450), [distribution modes](https://github.com/mjoneill/manyhands/blob/94010f1227d03152f6d745f7da2fd89ef06d0a96/README.md#L102-L110).
- Basis: structural.
- Confidence: medium.
- Caveats: human development of the project is adjacent rather than a product parent-adaptation mode.

### Absence scope

- Surfaces inspected: README modes, runner/loop/model adapter, registry prompt/model changes and memory/context handling.
- Plausible first-party paths checked: model replacement, memory revision, prompt grants and research/evaluation-led development.
- Why no material first-party path remains: these supply operating configuration or internal continuity; no packaged external sensing → future options → supervisory capability adoption path is supplied.

## S5 — Policy and identity

- State: ?
- Function: a plausible shipped decision/authority-to-resident return exists, but legitimate ultimate-policy closure is unresolved.
- Disturbance / variety regulated: conflicting remembered rulings and authoritative decisions about roles or standing.
- Decisive decision or feedback right: record or supersede a binding decision and determine which authority governs a topic.
- Decision owner: unresolved at ultimate workspace-policy recursion.
- Supporting / enforcement mechanisms: decision provenance fields, authority resolver statuses, live binding-ruling injection.
- Closure path: decisions matching seat/role/name are inserted into subsequent wake context as settled rulings; whether these derive from legitimate ultimate authority is not established by that transport.
- Why this is / is not agent-owned: authority resolution and a decidedBy string do not establish either autonomous S5 or legitimate parent ownership.
- Evidence: [binding rulings](https://github.com/mjoneill/manyhands/blob/94010f1227d03152f6d745f7da2fd89ef06d0a96/core/guest-loop.mjs#L418-L438), [return into wakes](https://github.com/mjoneill/manyhands/blob/94010f1227d03152f6d745f7da2fd89ef06d0a96/core/guest-loop.mjs#L690-L696), [decision creation](https://github.com/mjoneill/manyhands/blob/94010f1227d03152f6d745f7da2fd89ef06d0a96/server.js#L6808-L6944), [trial authority limitations](https://github.com/mjoneill/manyhands/blob/94010f1227d03152f6d745f7da2fd89ef06d0a96/docs/graph-slice-trial-api.md#L1-L12).
- Basis: unknown.
- Confidence: medium.
- Caveats: concrete unresolved in-boundary path warrants ?, rather than treating all policy as absent or crediting a trial resolver as legitimate governance.

## Distributed OSS parent arrangement

Maintainer-directed development seats and private harnesses are excluded. The S3 parent finding concerns the self-hosted workspace operator only. Multiple named contributors do not establish project-level S5.

## Self-hosted and non-human modes

Resident operation is optional and requires a configured model endpoint. Board-only mode and externally hosted cognitive agents are explicitly separated. No composite ownership state is claimed.

## Recursion

A resident has a local response/memory loop; this does not demonstrate a viable recursive organization with its own full metasystem.

## Variety and escalation

Bounded changes, grants, hop/price ceilings and pending outbox state attenuate context/cost/replay variety. Claim conflicts preserve the incumbent. Tool failures are returned to the model. These mechanisms do not themselves establish algedonic or ultimate-policy authority.

## Evidence gaps

The identity-level authority behind live decisions, particularly outside the explicitly limited graph trial, remains unresolved (S5=?). No empirical performance or causal VSM claim is made. Native deterministic tool-loop tests could not run on the inspection host because Node is unavailable; source includes scripted fake-model tests, but they are not reported as executed. Index/Skills validation is reported separately in the owning PR receipts.

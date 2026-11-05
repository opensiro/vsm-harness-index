---
harness_id: incidentops-ai
project_name: IncidentOps AI
repository: https://github.com/Maherimtiyaz/triage-agent
review_ref: e4c32e06756a546bb2c61cca22e8d184dbf56c17
reviewed_at: 2026-11-05
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# IncidentOps AI

## Review boundary

- System in focus: the shipped local incident-triage harness with configured real-model provider, tool feedback and structured incident report.
- Purpose and identity: investigate an alert using bounded diagnostic evidence and propose a cause/action for human consideration; optionally record approved incident facts.
- Relevant environment: alert text, sandboxed service fixture/files, diagnostic logs/deploy/metric tools, model services and operator-supplied incident records.
- Standard-distribution boundary: Python triage_agent CLI/run loop, registry/guardrails/output/provider adapters, context/memory loader and separate deterministic scribe.
- Credited operating / distribution surfaces: configured Anthropic or OpenAI-compatible model-backed run(), read-only tool dispatch and report/repair feedback. Mock/demo/replay is excluded from autonomous ownership.
- Adjacent first-party surfaces excluded from ownership: Switch-room integration/reviewer/reassignment diagram, simulated dashboard, golden eval cassettes, victim fault generator and maintainer CI. The README explicitly says no live Switch integration or separate running reviewer is implemented.
- First-party operating / deployment modes considered: local CLI with actual provider adapters, default scripted mock as a non-agentic contrast, replay/record and operator-approved scribe. No autonomous remediation is supplied.
- Recursion level: one investigation work cell; not the production service organization, Switch room or hypothetical multi-agent incident team.
- Reviewed revision: `e4c32e06756a546bb2c61cca22e8d184dbf56c17`.
- Observation date: 2026-11-05.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

loop.py owns bootstrap → budget/context checks → provider → guarded tool dispatch → observation feedback → schema-validated report. The model can choose diagnostic tools, hypotheses and when to return an answer. providers.py implements concrete Anthropic and stdlib OpenAI-compatible adapters, translating tool calls/results; provider transport does not supply another harness's unreviewed control semantics. MockProvider and CLI DEMO_SCRIPT are deliberately scripted and do not supply an A witness.

tools.py registers bounded query_logs/list_deploys/get_metric/read_file with deny-by-default policy, path sandboxing, timeouts and returned errors. Report validation returns malformed-output errors to the same actor for at most two retries. context.py deterministically summarizes old action history. The loop loads three recent local incident notes for citation. scribe.py is a separate deterministic approval-required Markdown writer using caller-provided cause/timeline/impact/resolution, exclusive writes and blameless-language refusal. It neither investigates nor remediates. README distinguishes this local fallback from proposed Switch role orchestration.

## Operational model

The autonomous operational outcome, in the actual-provider configuration, is a contextual diagnostic report. Read-only investigation can be agent-owned even though executing the suggested remediation is outside scope. A bounded model/tool loop supplies meaningful local discretion; a mock replay demonstrates mechanics rather than that discretion. The external service under investigation is an environment, so diagnostic querying it does not automatically become S3* for this harness.

## S1 — Operations

- State: A
- Function: investigate a supplied incident and produce a grounded causal/action proposal.
- Disturbance / variety regulated: different symptoms, deployment histories, log/metric evidence, tool errors and invalid report output.
- Decisive decision or feedback right: choose diagnostic queries, form/falsify a hypothesis and select report content/next proposed action.
- Decision owner: configured model triage actor; operator owns external remediation and supplied policy.
- Supporting / enforcement mechanisms: first-party run loop, provider translation, registry/schema, budget, sandbox, timeout/truncation and report validation.
- Closure path: alert → model selects tools → guarded dispatch appends observations → next model choice → validated IncidentReport; invalid output returns error feedback before bounded retry.
- Boundary reachability: CLI selects configured real provider via build_provider and calls run; both actual-provider adapters implement complete() with tool-result translation. No Switch actor is required.
- Why this is / is not agent-owned: model-dependent query/hypothesis choices disappear if the actor is removed; static mocks and schema/dispatch code cannot reproduce equivalent contextual discretion.
- Evidence: [src/triage_agent/loop.py](https://github.com/Maherimtiyaz/triage-agent/blob/e4c32e06756a546bb2c61cca22e8d184dbf56c17/src/triage_agent/loop.py); [src/triage_agent/providers.py](https://github.com/Maherimtiyaz/triage-agent/blob/e4c32e06756a546bb2c61cca22e8d184dbf56c17/src/triage_agent/providers.py); [src/triage_agent/cli.py](https://github.com/Maherimtiyaz/triage-agent/blob/e4c32e06756a546bb2c61cca22e8d184dbf56c17/src/triage_agent/cli.py); [src/triage_agent/tools.py](https://github.com/Maherimtiyaz/triage-agent/blob/e4c32e06756a546bb2c61cca22e8d184dbf56c17/src/triage_agent/tools.py).
- Basis: structural.
- Confidence: high for source wiring; not an empirical outcome claim.
- Caveats: A applies to configured real-model mode only. Default mock has no reasoning; live provider efficacy or production incident resolution is not claimed.

## S2 — Coordination

- State: —
- Function: inter-S1 conflict coordination
- Disturbance / variety regulated: candidate variety and checked alternatives are recorded below.
- Decisive decision or feedback right: no qualifying function-specific path established.
- Decision owner: ordinary operational agent, developer and caller rights do not establish this distinct function.
- Supporting / enforcement mechanisms: `src/triage_agent/loop.py`, `src/triage_agent/scribe.py`, `README.md`
- Closure path: The runtime contains one investigation actor. Tool-call iteration, read-only diagnosis and a separately invoked deterministic scribe are not multiple autonomous S1 units with an evidenced interference relation. Switch reviewer reassignment and room coordination are explicitly unimplemented.
- Why this is / is not agent-owned: positive and supported parent alternatives were tested before this bounded absence conclusion.
- Evidence: [src/triage_agent/loop.py](https://github.com/Maherimtiyaz/triage-agent/blob/e4c32e06756a546bb2c61cca22e8d184dbf56c17/src/triage_agent/loop.py); [src/triage_agent/scribe.py](https://github.com/Maherimtiyaz/triage-agent/blob/e4c32e06756a546bb2c61cca22e8d184dbf56c17/src/triage_agent/scribe.py); [README.md](https://github.com/Maherimtiyaz/triage-agent/blob/e4c32e06756a546bb2c61cca22e8d184dbf56c17/README.md).
- Basis: structural.
- Confidence: high for source wiring; not an empirical outcome claim.
- Caveats: Bounded to the reviewed supported distribution; custom future extensions are not evidence of a shipped path.

### Absence scope

- Surfaces inspected: src/triage_agent/loop.py, src/triage_agent/scribe.py, README.md, README and supported CLI/operator wiring.
- Plausible first-party paths checked: The runtime contains one investigation actor. Tool-call iteration, read-only diagnosis and a separately invoked deterministic scribe are not multiple autonomous S1 units with an evidenced interference relation. Switch reviewer reassignment and room coordination are explicitly unimplemented.
- Why no material first-party path remains: The inspected mechanisms implement ordinary operation or support; none closes inter-S1 conflict coordination at this boundary.

## S3 — Inside-and-now control

- State: —
- Function: whole-system inside-and-now control
- Disturbance / variety regulated: candidate variety and checked alternatives are recorded below.
- Decisive decision or feedback right: no qualifying function-specific path established.
- Decision owner: ordinary operational agent, developer and caller rights do not establish this distinct function.
- Supporting / enforcement mechanisms: `src/triage_agent/loop.py`, `src/triage_agent/guardrails.py`, `src/triage_agent/config.py`, `src/triage_agent/scribe.py`
- Closure path: Fixed steps/cost/tool allowlists and provider retry enforce caller configuration for one investigation. Human approval of a scribe write is an isolated artifact decision; no whole-system current commitments/resource view and function-specific supervisory return path is shipped.
- Why this is / is not agent-owned: positive and supported parent alternatives were tested before this bounded absence conclusion.
- Evidence: [src/triage_agent/loop.py](https://github.com/Maherimtiyaz/triage-agent/blob/e4c32e06756a546bb2c61cca22e8d184dbf56c17/src/triage_agent/loop.py); [src/triage_agent/guardrails.py](https://github.com/Maherimtiyaz/triage-agent/blob/e4c32e06756a546bb2c61cca22e8d184dbf56c17/src/triage_agent/guardrails.py); [src/triage_agent/config.py](https://github.com/Maherimtiyaz/triage-agent/blob/e4c32e06756a546bb2c61cca22e8d184dbf56c17/src/triage_agent/config.py); [src/triage_agent/scribe.py](https://github.com/Maherimtiyaz/triage-agent/blob/e4c32e06756a546bb2c61cca22e8d184dbf56c17/src/triage_agent/scribe.py).
- Basis: structural.
- Confidence: high for source wiring; not an empirical outcome claim.
- Caveats: Bounded to the reviewed supported distribution; custom future extensions are not evidence of a shipped path.

### Absence scope

- Surfaces inspected: src/triage_agent/loop.py, src/triage_agent/guardrails.py, src/triage_agent/config.py, src/triage_agent/scribe.py, README and supported CLI/operator wiring.
- Plausible first-party paths checked: Fixed steps/cost/tool allowlists and provider retry enforce caller configuration for one investigation. Human approval of a scribe write is an isolated artifact decision; no whole-system current commitments/resource view and function-specific supervisory return path is shipped.
- Why no material first-party path remains: The inspected mechanisms implement ordinary operation or support; none closes whole-system inside-and-now control at this boundary.

## S3* — Complementary audit

- State: —
- Function: complementary independent audit of the harness's operational claims
- Disturbance / variety regulated: candidate variety and checked alternatives are recorded below.
- Decisive decision or feedback right: no qualifying function-specific path established.
- Decision owner: ordinary operational agent, developer and caller rights do not establish this distinct function.
- Supporting / enforcement mechanisms: `src/triage_agent/loop.py`, `src/triage_agent/output.py`, `src/triage_agent/providers.py`, `README.md`
- Closure path: The actor's own falsification query is S1 investigation. Schema validation, cassette hash checks and golden evals are routine output/test integrity. README says the Reviewer is represented by a report/approval contract, not a separately executing agent; the report's waiting-for-review text is not a corrective independent audit loop.
- Why this is / is not agent-owned: positive and supported parent alternatives were tested before this bounded absence conclusion.
- Evidence: [src/triage_agent/loop.py](https://github.com/Maherimtiyaz/triage-agent/blob/e4c32e06756a546bb2c61cca22e8d184dbf56c17/src/triage_agent/loop.py); [src/triage_agent/output.py](https://github.com/Maherimtiyaz/triage-agent/blob/e4c32e06756a546bb2c61cca22e8d184dbf56c17/src/triage_agent/output.py); [src/triage_agent/providers.py](https://github.com/Maherimtiyaz/triage-agent/blob/e4c32e06756a546bb2c61cca22e8d184dbf56c17/src/triage_agent/providers.py); [README.md](https://github.com/Maherimtiyaz/triage-agent/blob/e4c32e06756a546bb2c61cca22e8d184dbf56c17/README.md).
- Basis: structural.
- Confidence: high for source wiring; not an empirical outcome claim.
- Caveats: Bounded to the reviewed supported distribution; custom future extensions are not evidence of a shipped path.

### Absence scope

- Surfaces inspected: src/triage_agent/loop.py, src/triage_agent/output.py, src/triage_agent/providers.py, README.md, README and supported CLI/operator wiring.
- Plausible first-party paths checked: The actor's own falsification query is S1 investigation. Schema validation, cassette hash checks and golden evals are routine output/test integrity. README says the Reviewer is represented by a report/approval contract, not a separately executing agent; the report's waiting-for-review text is not a corrective independent audit loop.
- Why no material first-party path remains: The inspected mechanisms implement ordinary operation or support; none closes complementary independent audit of the harness's operational claims at this boundary.

## S4 — Outside-and-then intelligence

- State: —
- Function: external and prospective capability adaptation
- Disturbance / variety regulated: candidate variety and checked alternatives are recorded below.
- Decisive decision or feedback right: no qualifying function-specific path established.
- Decision owner: ordinary operational agent, developer and caller rights do not establish this distinct function.
- Supporting / enforcement mechanisms: `src/triage_agent/loop.py`, `src/triage_agent/scribe.py`, `src/triage_agent/context.py`, `docs/ARCHITECTURE.md`
- Closure path: Three recent incident notes are injected as context and a human can record supplied facts through the deterministic scribe. Neither path develops and adopts future capability options from an outside-and-then model. Suggested incident remediation is current diagnostic output, not an implemented adaptation of this harness; extension instructions require new developer code.
- Why this is / is not agent-owned: positive and supported parent alternatives were tested before this bounded absence conclusion.
- Evidence: [src/triage_agent/loop.py](https://github.com/Maherimtiyaz/triage-agent/blob/e4c32e06756a546bb2c61cca22e8d184dbf56c17/src/triage_agent/loop.py); [src/triage_agent/scribe.py](https://github.com/Maherimtiyaz/triage-agent/blob/e4c32e06756a546bb2c61cca22e8d184dbf56c17/src/triage_agent/scribe.py); [src/triage_agent/context.py](https://github.com/Maherimtiyaz/triage-agent/blob/e4c32e06756a546bb2c61cca22e8d184dbf56c17/src/triage_agent/context.py); [docs/ARCHITECTURE.md](https://github.com/Maherimtiyaz/triage-agent/blob/e4c32e06756a546bb2c61cca22e8d184dbf56c17/docs/ARCHITECTURE.md).
- Basis: structural.
- Confidence: high for source wiring; not an empirical outcome claim.
- Caveats: Bounded to the reviewed supported distribution; custom future extensions are not evidence of a shipped path.

### Absence scope

- Surfaces inspected: src/triage_agent/loop.py, src/triage_agent/scribe.py, src/triage_agent/context.py, docs/ARCHITECTURE.md, README and supported CLI/operator wiring.
- Plausible first-party paths checked: Three recent incident notes are injected as context and a human can record supplied facts through the deterministic scribe. Neither path develops and adopts future capability options from an outside-and-then model. Suggested incident remediation is current diagnostic output, not an implemented adaptation of this harness; extension instructions require new developer code.
- Why no material first-party path remains: The inspected mechanisms implement ordinary operation or support; none closes external and prospective capability adaptation at this boundary.

## S5 — Policy and identity

- State: —
- Function: identity and ultimate-policy closure
- Disturbance / variety regulated: candidate variety and checked alternatives are recorded below.
- Decisive decision or feedback right: no qualifying function-specific path established.
- Decision owner: ordinary operational agent, developer and caller rights do not establish this distinct function.
- Supporting / enforcement mechanisms: `src/triage_agent/guardrails.py`, `src/triage_agent/scribe.py`, `src/triage_agent/loop.py`, `README.md`
- Closure path: Blameless wording rules, deny-by-default permissions, system prompt and approved write flag are fixed operational constraints. They do not identify an unresolved identity/policy tension, route it to legitimate ultimate authority and return an authoritative governance settlement.
- Why this is / is not agent-owned: positive and supported parent alternatives were tested before this bounded absence conclusion.
- Evidence: [src/triage_agent/guardrails.py](https://github.com/Maherimtiyaz/triage-agent/blob/e4c32e06756a546bb2c61cca22e8d184dbf56c17/src/triage_agent/guardrails.py); [src/triage_agent/scribe.py](https://github.com/Maherimtiyaz/triage-agent/blob/e4c32e06756a546bb2c61cca22e8d184dbf56c17/src/triage_agent/scribe.py); [src/triage_agent/loop.py](https://github.com/Maherimtiyaz/triage-agent/blob/e4c32e06756a546bb2c61cca22e8d184dbf56c17/src/triage_agent/loop.py); [README.md](https://github.com/Maherimtiyaz/triage-agent/blob/e4c32e06756a546bb2c61cca22e8d184dbf56c17/README.md).
- Basis: structural.
- Confidence: high for source wiring; not an empirical outcome claim.
- Caveats: Bounded to the reviewed supported distribution; custom future extensions are not evidence of a shipped path.

### Absence scope

- Surfaces inspected: src/triage_agent/guardrails.py, src/triage_agent/scribe.py, src/triage_agent/loop.py, README.md, README and supported CLI/operator wiring.
- Plausible first-party paths checked: Blameless wording rules, deny-by-default permissions, system prompt and approved write flag are fixed operational constraints. They do not identify an unresolved identity/policy tension, route it to legitimate ultimate authority and return an authoritative governance settlement.
- Why no material first-party path remains: The inspected mechanisms implement ordinary operation or support; none closes identity and ultimate-policy closure at this boundary.

## Distributed OSS parent arrangement

Maintainer/contributor governance is outside the investigation cell. The scribe approval flag does not establish organization-level parent VSM functions.

## Self-hosted and non-human modes

Actual Anthropic/OpenAI-compatible and local endpoints are supported execution seams. Mock/replay remain deterministic demonstration/testing modes. No parent S3/S4/S5 mode is inferred from configuration or approval.

## Recursion

The fixture service, tool handlers and scribe are not demonstrated recursively viable operational organizations.

## Variety and escalation

Tool errors become observations; budgets, provider failure, invalid output and stale cassettes return distinct status/reason artifacts. They improve local observability without automatically forming an algedonic channel.

## Evidence gaps

Native deterministic tests were run: 89 passed, golden cassette evals 3/3 passed. These verify mechanics only; no live real-model, Switch, production-service or remediation run occurred. Diagnostic correctness and causal benefit remain unmeasured.


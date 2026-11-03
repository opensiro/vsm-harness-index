---
harness_id: binny
project_name: BINNY
repository: https://github.com/openbin-ai/binny
review_ref: d0c2ae4c61d222421d1505986ac6e63b7ed799fa
reviewed_at: 2026-11-03
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# BINNY

## Review boundary

- System in focus: The shipped BINNY Go reverse-engineering agent harness for one analyst-selected sample/project and its supported investigation, on-demand Q&A and report-review modes.
- Purpose and identity: Investigate decompiled binary or Android application evidence with model-selected tools, capture findings and create an analyst-reviewable draft.
- Relevant environment: Analyst, sample/project and decompiler APIs, external LLM provider, Docker sandbox, changing malware/vulnerability evidence and report store.
- Standard-distribution boundary: BINNY TUI, `internal/agent` engine, first-party tool registry, playbooks, report state and sandbox with configured external provider; supported autonomous, supervised, collaborative and on-demand Q&A modes.
- Credited operating / distribution surfaces: [agent engine](https://github.com/openbin-ai/binny/blob/d0c2ae4c61d222421d1505986ac6e63b7ed799fa/internal/agent/engine.go), [Q&A prompt](https://github.com/openbin-ai/binny/blob/d0c2ae4c61d222421d1505986ac6e63b7ed799fa/internal/agent/prompt.go), [TUI agent](https://github.com/openbin-ai/binny/blob/d0c2ae4c61d222421d1505986ac6e63b7ed799fa/internal/tui/agent.go), [tools](https://github.com/openbin-ai/binny/tree/d0c2ae4c61d222421d1505986ac6e63b7ed799fa/internal/tools), and [README](https://github.com/openbin-ai/binny/blob/d0c2ae4c61d222421d1505986ac6e63b7ed799fa/README.md).
- Adjacent first-party surfaces excluded from ownership: Upstream OpenBin/OpenAPK project service, outside model provider, Ghidra/JADX engine, binary under analysis, GitHub CI/release and author maintenance. Separate examples/tests do not donate an organizational function.
- First-party operating / deployment modes considered: Autonomous triage→investigate→synthesize→review, supervised/collaborative checkpoints, `/ask` source-grounded skeptical Q&A against an existing report or sample, and `/save` draft handoff.
- Recursion level: One sample investigation/review session, not a fleet of independent investigators or the OpenBin company.
- Reviewed revision: `d0c2ae4c61d222421d1505986ac6e63b7ed799fa`.
- Observation date: 2026-11-03.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

`Engine.Step` streams an LLM request with a typed tool catalogue, executes selected tools, returns results into model context, enforces round/token budgets, and advances through triage, investigation, synthesis and review. An investigation object retains classification, objectives, findings, IOCs and draft sections. The Go TUI exposes autonomous or checkpointed operation, a separate on-demand Q&A start, restore and draft/save commands. Local decompilation and static sandbox are tool/evidence services, not further agent owners. [Engine loop](https://github.com/openbin-ai/binny/blob/d0c2ae4c61d222421d1505986ac6e63b7ed799fa/internal/agent/engine.go#L425-L578); [investigation store](https://github.com/openbin-ai/binny/blob/d0c2ae4c61d222421d1505986ac6e63b7ed799fa/internal/agent/investigation.go); [TUI](https://github.com/openbin-ai/binny/blob/d0c2ae4c61d222421d1505986ac6e63b7ed799fa/internal/tui/agent.go).

## Operational model

One model-driven investigation unit selects analysis tools and updates findings from the current sample. Playbooks and deterministic phase/cost gates constrain that unit. The user chooses when to launch and save a draft. The optional fresh skeptical Q&A mode treats an existing report as untrusted claims and asks a model to inspect primary decompilation evidence, but only when directed by an analyst; it is not a mandatory continuous audit.

## S1 — Operations

- State: A
- Function: Autonomous reverse-engineering investigation and evidence-backed draft construction.
- Disturbance / variety regulated: Unknown binary behaviour, contradictory strings/function evidence, tool failure, and incomplete classification or report sections.
- Decisive decision or feedback right: Model chooses evidence queries and investigation tool calls, revises hypotheses from results, and authors findings/report sections.
- Decision owner: The model actor inside the shipped `Engine.Step` loop, not deterministic phase transitions or the remote provider's service operator.
- Supporting / enforcement mechanisms: Tool registry, static sandbox, STIX/playbook prompts, objective tracking, token caps, context compaction and optional human checkpoints.
- Closure path: Model call→first-party tool execution→result in `e.messages`→subsequent model choice; stages culminate in reviewable draft sections and findings.
- Boundary reachability: The TUI's ordinary investigation command constructs the first-party engine with provider/tool registry and runs `Step`; no developer-authored coordinator is necessary.
- Why this is / is not agent-owned: Runtime selects budgets and legal tool boundaries, while only model reasoning selects semantically relevant operations against the sample.
- Evidence: [Engine Step](https://github.com/openbin-ai/binny/blob/d0c2ae4c61d222421d1505986ac6e63b7ed799fa/internal/agent/engine.go#L425-L578); [stage transitions](https://github.com/openbin-ai/binny/blob/d0c2ae4c61d222421d1505986ac6e63b7ed799fa/internal/agent/engine.go#L638-L700); [tool dispatch](https://github.com/openbin-ai/binny/blob/d0c2ae4c61d222421d1505986ac6e63b7ed799fa/internal/tools/tools.go).
- Basis: structural
- Confidence: high for shipped loop architecture.
- Caveats: No live third-party model calls or analyst-domain correctness tests were conducted.

## S2 — Coordination

- State: —
- Function: No distinct inter-S1 coordination function is shipped at this one-investigation recursion.
- Disturbance / variety regulated: Tool sequence and triage/investigate phase changes belong to one S1, not conflict between independent operational cells.
- Decisive decision or feedback right: No first-party ownership/adjustment of competing S1 work is exposed.
- Decision owner: None for S2.
- Supporting / enforcement mechanisms: Stage machine, token caps, project state and report objectives.
- Closure path: Tool and phase feedback returns to the same model actor; no inter-unit attenuation return exists.
- Why this is / is not agent-owned: Distinct sequential phases or API tools are not distinct S1 units.
- Evidence: [engine](https://github.com/openbin-ai/binny/blob/d0c2ae4c61d222421d1505986ac6e63b7ed799fa/internal/agent/engine.go), [README](https://github.com/openbin-ai/binny/blob/d0c2ae4c61d222421d1505986ac6e63b7ed799fa/README.md).
- Basis: structural
- Confidence: high for the reviewed distribution.
- Caveats: Separate analysts can run independent processes, without a shipped cross-run coordination system.

### Absence scope

- Surfaces inspected: Agent engine, TUI commands, investigation/report state, tool registry and README modes.
- Plausible first-party paths checked: Phase sequencing, multiple tool calls, persistent workspaces, sample/project selection and report review.
- Why no material first-party path remains: These paths regulate one investigation; no second operational agent and specific inter-unit interference/feedback relation is supplied.

## S3 — Inside-and-now control

- State: —
- Function: Whole-current management of distinct operational commitments/resources is not established.
- Disturbance / variety regulated: Per-task token limits, phase checkpoints and model refusals are local investigation constraints.
- Decisive decision or feedback right: No whole-current bargaining/reallocation or cross-S1 intervention right is present.
- Decision owner: Analyst selects autonomy/budgets and the engine enforces caps; model selects local evidence tools.
- Supporting / enforcement mechanisms: `maxRounds`, `maxTokens`, phase-gates, /autonomy and ContinuePastCap.
- Closure path: Cap reached→local pause/analyst extension or stop; no S3 return into an operational whole.
- Why this is / is not agent-owned: Budget enforcement and human override of one analysis are not a distinct S3 function or parent-governed S3 control.
- Evidence: [engine caps](https://github.com/openbin-ai/binny/blob/d0c2ae4c61d222421d1505986ac6e63b7ed799fa/internal/agent/engine.go#L425-L470), [TUI controls](https://github.com/openbin-ai/binny/blob/d0c2ae4c61d222421d1505986ac6e63b7ed799fa/internal/tui/agent.go).
- Basis: structural
- Confidence: high at the selected recursion.
- Caveats: Do not infer OpenBin enterprise project management from this CLI's project selector.

### Absence scope

- Surfaces inspected: Session/configuration, cap decisions, TUI runtime, investigation stages and resume flow.
- Plausible first-party paths checked: Analyst supervisory checkpoints, token allocation, report submission and cross-phase transitions.
- Why no material first-party path remains: Each is a local task choice/enforcement path; no whole-system view, current resource commitments and closed S3 right over distinct units is wired.

## S3* — Complementary audit

- State: A
- Claim being audited: Assertions in a previously produced sample report about functions, addresses, reachability and malware/vulnerability findings.
- Ordinary reporting path: The investigation model records findings and report sections during triage/investigate/synthesize, with ordinary tool results in its own context.
- Complementary access path: `StartQA(report)` creates an on-demand skeptical review context, loads report content as claims to check rather than facts and directs fresh raw function/string/xref/reachability reads against source evidence.
- Independence boundary: The Q&A mode does not inherit the original evidence as trusted prior work; the model must inspect independently retrieved sample evidence. It is procedural/mode separation, not a separate institution or mandatory different provider.
- Who acts on findings: Review-model feedback returns to the analyst; analyst can request recorded correction and `/save` a revised draft, or use the returned negative evidence for later investigation.
- Function: Complementary source-based challenge of ordinary report claims beyond trusting their original narrative.
- Disturbance / variety regulated: Plausible but false analysis claims, unsupported reachability or section assertions.
- Decisive decision or feedback right: In explicitly initiated verification, the model judges the actual sampled evidence as supporting/weakening/refuting a report claim.
- Decision owner: Q&A model actor for evidence judgment; analyst owns case selection and final report publication, engine just transports tool results and report edits.
- Supporting / enforcement mechanisms: `qaKickoff` skeptical prompt, source read tools, report snapshot and draft editing/saving.
- Closure path: Analyst asks to verify→separately started Q&A model reads source→returns a specific finding→analyst may direct corrections/write findings→draft `/save` returns corrected evidence into the project's output.
- Boundary reachability: `/ask` and `StartQA` are shipped user-facing operational modes, not a test fixture or maintainer-only check.
- Why this is / is not agent-owned: The model determines whether primary evidence falsifies the report; deterministic tools merely expose bytes/functions. This credits optional agent-owned audit judgment, not autonomous selection of audit targets or remediation.
- Evidence: [StartQA](https://github.com/openbin-ai/binny/blob/d0c2ae4c61d222421d1505986ac6e63b7ed799fa/internal/agent/engine.go#L297-L326); [skeptical Q&A instruction](https://github.com/openbin-ai/binny/blob/d0c2ae4c61d222421d1505986ac6e63b7ed799fa/internal/agent/prompt.go#L209-L270); [README /ask](https://github.com/openbin-ai/binny/blob/d0c2ae4c61d222421d1505986ac6e63b7ed799fa/README.md#L45-L53).
- Basis: explicit + structural
- Confidence: medium for optional complementary review topology.
- Caveats: No automatic audit after every draft, provider isolation attestation, or validated remediation was observed; audit depends on an analyst asking concrete questions.

## S4 — Outside-and-then intelligence

- State: —
- Function: No future-oriented external environmental sensing→adaptation options→present capability return is shipped.
- Disturbance / variety regulated: New malware class or vulnerability questions are investigated as the current deliverable.
- Decisive decision or feedback right: No standing prospective redesign of BINNY's own repertoire from environmental trends is exposed.
- Decision owner: Developers select playbooks/releases; model picks current-case observations.
- Supporting / enforcement mechanisms: STIX classification, playbook selection, provider switching and state persistence.
- Closure path: Classifier selects an existing playbook for the current sample; this is S1 task steering, not a forward capability-adaptation loop.
- Why this is / is not agent-owned: Planning and classifying the current case do not constitute externally informed S4 intelligence.
- Evidence: [playbooks](https://github.com/openbin-ai/binny/blob/d0c2ae4c61d222421d1505986ac6e63b7ed799fa/internal/playbook/playbook.go), [engine stages](https://github.com/openbin-ai/binny/blob/d0c2ae4c61d222421d1505986ac6e63b7ed799fa/internal/agent/engine.go#L661-L700).
- Basis: structural
- Confidence: medium-high.
- Caveats: An analyst may use results to change future practices externally; that arrangement is outside the assessed runtime.

### Absence scope

- Surfaces inspected: Playbook classification, resume/persistence, model selection, sandbox/tools and first-party prompts.
- Plausible first-party paths checked: Current threat typing, dynamic tool queries, plan brief generation, memory and user-selected models.
- Why no material first-party path remains: No distinct future-environment model with selected adaptation options and a return that changes current harness capability is wired.

## S5 — Policy and identity

- State: —
- Function: Identity/ultimate-policy closure for the agent harness is not supplied as a distinct organizational process.
- Disturbance / variety regulated: Tool risk, sample access, report publication and model-provider configuration.
- Decisive decision or feedback right: No legitimate ultimate mission/policy dispute and returned binding decision path is present.
- Decision owner: Analyst/developer selects mode and tool permissions; ordinary report approval is not ultimate authority over identity.
- Supporting / enforcement mechanisms: Sandbox restrictions, API auth, prompts, report draft gate and runtime settings.
- Closure path: Permission or save choices affect current case execution/publication; no identity-level governance return is shown.
- Why this is / is not agent-owned: Static security/configuration and one draft approval do not establish S5, including the parent mode.
- Evidence: [README](https://github.com/openbin-ai/binny/blob/d0c2ae4c61d222421d1505986ac6e63b7ed799fa/README.md), [sandbox](https://github.com/openbin-ai/binny/blob/d0c2ae4c61d222421d1505986ac6e63b7ed799fa/internal/sandbox/sandbox.go), [TUI](https://github.com/openbin-ai/binny/blob/d0c2ae4c61d222421d1505986ac6e63b7ed799fa/internal/tui/agent.go).
- Basis: structural
- Confidence: high.
- Caveats: This is not an assessment of the upstream organization or platform policies.

### Absence scope

- Surfaces inspected: Runtime sandbox, configuration, prompt, analyst modes and report handoff.
- Plausible first-party paths checked: Autonomy settings, safety/permission checks, refusal handling, save and budget extensions.
- Why no material first-party path remains: These are task-local controls and security conditions, not a first-party legitimate identity/policy judgment and returned changed purpose.

## Distributed OSS parent arrangement

No public first-party distributed operator governance is part of a standalone BINNY sample-session operating boundary. Maintainer releases and individual analysts are adjacent or higher recursions.

## Self-hosted and non-human modes

BINNY supports local/self-hosted providers and autonomous/supervised/collaborative execution of the same S1 loop. Those modes do not add distinct established parent-governed S3/S4/S5 functions at this recursion.

## Recursion

One model-guided investigation and optional source-grounded Q&A is the operational focus. A phase, tool call, report section or provider adapter is not a recursively viable sub-organization.

## Variety and escalation

Sample tools amplify observable function/string evidence; staged prompts attenuate sample variety into playbook objectives. Costs/refusals trigger a local pause and analyst choice. The optional skeptical Q&A path challenges claims from an alternate evidence stance but is not an institutionally independent security audit.

## Evidence gaps

Structural source assessment only; no provider-backed proof of report accuracy, cross-model independence or actual correction-to-save was executed. The optional S3* audit path is creditable as a shipped mode, while effectiveness and actual analyst take-up remain unverified.

## Verdict

**Include.** BINNY ships an autonomous model/tool investigation loop with an optional source-grounded skeptical audit mode. No distinct inter-agent coordination, whole-current control, future-capability adaptation or ultimate-policy closure was established at the declared sample-session boundary.

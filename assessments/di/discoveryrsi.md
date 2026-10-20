---
harness_id: discoveryrsi
project_name: DiscoveryRSI
repository: https://github.com/Gen-Verse/DiscoveryRSI
review_ref: 7389e0b58ae50486ab35aa3dcbfa2fa15fea1a91
reviewed_at: 2026-10-20
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

# DiscoveryRSI

## Review boundary

- System in focus: The shipped first-party `discovery-rsi` Python hypothesis-campaign harness: a bounded proposer–critic–selector–retainer model-driven research proposal cell, **not** the wider DiscoveryRSI paper/program.
- Purpose and identity: Turn an operator-selected research question and supplied context into model-proposed and model-critiqued falsifiable candidate hypotheses with versioned parent IDs and optional JSONL output.
- Relevant environment: Research question and user-supplied domain input; configured external inference endpoint, Codex or Claude CLI; local file system; operator deciding research topics and whether to trust/execute any proposed experiment.
- Standard-distribution boundary: Installable `discovery_rsi` package with `discovery-rsi campaign`, the `DiscoveryLoop` library call, model adapters, shipped prompt-role Markdown and configuration. `demo` is an illustrative deterministic mode and not autonomous S1 evidence.
- Credited operating / distribution surfaces: [cli.py](https://github.com/Gen-Verse/DiscoveryRSI/blob/7389e0b58ae50486ab35aa3dcbfa2fa15fea1a91/src/discovery_rsi/cli.py), [core.py](https://github.com/Gen-Verse/DiscoveryRSI/blob/7389e0b58ae50486ab35aa3dcbfa2fa15fea1a91/src/discovery_rsi/core.py), [harness.py](https://github.com/Gen-Verse/DiscoveryRSI/blob/7389e0b58ae50486ab35aa3dcbfa2fa15fea1a91/src/discovery_rsi/harness.py), [manifest.py](https://github.com/Gen-Verse/DiscoveryRSI/blob/7389e0b58ae50486ab35aa3dcbfa2fa15fea1a91/src/discovery_rsi/manifest.py), [providers.py](https://github.com/Gen-Verse/DiscoveryRSI/blob/7389e0b58ae50486ab35aa3dcbfa2fa15fea1a91/src/discovery_rsi/providers.py), [plugin.py](https://github.com/Gen-Verse/DiscoveryRSI/blob/7389e0b58ae50486ab35aa3dcbfa2fa15fea1a91/src/discovery_rsi/plugin.py), [tools.py](https://github.com/Gen-Verse/DiscoveryRSI/blob/7389e0b58ae50486ab35aa3dcbfa2fa15fea1a91/src/discovery_rsi/tools.py), [research_manifest.json](https://github.com/Gen-Verse/DiscoveryRSI/blob/7389e0b58ae50486ab35aa3dcbfa2fa15fea1a91/configs/research_manifest.json).
- Adjacent first-party surfaces excluded from ownership: deterministic fixtures and unit tests ([test_core.py](https://github.com/Gen-Verse/DiscoveryRSI/blob/7389e0b58ae50486ab35aa3dcbfa2fa15fea1a91/tests/test_core.py)); README's public live arena, the separate DFM-Bench evaluation repository, Hugging Face checkpoint/training program, paper's evolutionary training/Harbor research pipeline, project contributors, and downstream external scientist/lab decisions. Those claims are not wired as closed first-party functions in the inspected package.
- First-party operating / deployment modes considered: deterministic `demo`; configured `campaign` with OpenAI-compatible adapter; `campaign` with Codex or Claude-Code subprocess adapter; library `DiscoveryLoop` with injected proposer/critic; user-supplied GEO domain-demo. An externally hosted model supplies inference but is not imported as external governance.
- Recursion level: A single research hypothesis-development operational cell; no evidenced enclosing durable research organization with multiple independently viable S1 units.
- Reviewed revision: `Gen-Verse/DiscoveryRSI@7389e0b58ae50486ab35aa3dcbfa2fa15fea1a91` (public, nonfork, `main`; repository ID `1420168904`).
- Observation date: 2026-10-20.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

The CLI exposes a deterministic local demo, a configured `campaign`, and two domain-demo importers. In the actual model-backed campaign, `ResearchHarness._candidates` sends one JSON-output generation prompt via a `ModelAdapter`; `_critique` sends a separate scoring prompt through the same adapter for each proposal. `DiscoveryLoop.run` scores every candidate, selects the deterministic maximum by `(score,id)`, retains that candidate in memory, and appends each nonempty episode as JSONL when configured. The selection is implemented by Python; the candidate and critique contents are model decisions. No alternate model failure/retry policy is present beyond the adapter's subprocess/HTTP exceptions. [core.py](https://github.com/Gen-Verse/DiscoveryRSI/blob/7389e0b58ae50486ab35aa3dcbfa2fa15fea1a91/src/discovery_rsi/core.py); [harness.py](https://github.com/Gen-Verse/DiscoveryRSI/blob/7389e0b58ae50486ab35aa3dcbfa2fa15fea1a91/src/discovery_rsi/harness.py); [providers.py](https://github.com/Gen-Verse/DiscoveryRSI/blob/7389e0b58ae50486ab35aa3dcbfa2fa15fea1a91/src/discovery_rsi/providers.py); [cli.py](https://github.com/Gen-Verse/DiscoveryRSI/blob/7389e0b58ae50486ab35aa3dcbfa2fa15fea1a91/src/discovery_rsi/cli.py).

The `ResearchManifest` records question, domains, named roles/tools and candidate limit; `load_roles` reads Markdown role files and inserts truncated role descriptions into prompt context. These declarative roles are **not** independently executed model workers. The shipped `ToolRegistry` can be called directly as a library, but the production `ResearchHarness.run` only serializes descriptions into prompt text; it does not dispatch those tools as part of the model-driven loop. [manifest.py](https://github.com/Gen-Verse/DiscoveryRSI/blob/7389e0b58ae50486ab35aa3dcbfa2fa15fea1a91/src/discovery_rsi/manifest.py); [plugin.py](https://github.com/Gen-Verse/DiscoveryRSI/blob/7389e0b58ae50486ab35aa3dcbfa2fa15fea1a91/src/discovery_rsi/plugin.py); [tools.py](https://github.com/Gen-Verse/DiscoveryRSI/blob/7389e0b58ae50486ab35aa3dcbfa2fa15fea1a91/src/discovery_rsi/tools.py); [harness.py](https://github.com/Gen-Verse/DiscoveryRSI/blob/7389e0b58ae50486ab35aa3dcbfa2fa15fea1a91/src/discovery_rsi/harness.py).

Crucial loop limit: `_candidates(number, history)` reads the most recent selected candidate's **ID** to construct `parent=...`. It does not send the preceding claim, plan, alternatives, evidence, score or critique to the next proposal prompt. `ReplayBuffer.read` is available but is not used for campaign replay/resumption in this path. The original README's larger multi-agent evolutionary search, Harbor-task execution and Hypothesis Credit Optimization training descriptions are not proof that these mechanisms are shipped or exercised inside the assessed Python `campaign` mode. [harness.py](https://github.com/Gen-Verse/DiscoveryRSI/blob/7389e0b58ae50486ab35aa3dcbfa2fa15fea1a91/src/discovery_rsi/harness.py); [core.py](https://github.com/Gen-Verse/DiscoveryRSI/blob/7389e0b58ae50486ab35aa3dcbfa2fa15fea1a91/src/discovery_rsi/core.py); [README.md](https://github.com/Gen-Verse/DiscoveryRSI/blob/7389e0b58ae50486ab35aa3dcbfa2fa15fea1a91/README.md).

## Operational model

The operational output is a bounded succession of proposed research hypotheses and a local JSONL record, not a completed scientific experiment or validated discovery. There is **one** continuing research-proposal S1 workflow. Generation and critique are separate model invocations **inside** that one workflow, not two autonomous research departments. The model owns case-dependent claim/plan and critique judgments; Python owns top-score selection, iteration count and record writing. The human chooses the scientific question, data, model and subsequent experimental action outside the assessed standard-distribution loop. The CLI does not provide organizational portfolio management, field audit or ultimate research governance merely by using terms such as `lead` and `critic`.

## S1 — Operations

- State: A
- Function: Model-directed development and critique of candidate research hypotheses and investigation plans for a supplied research question, retaining a selected candidate over bounded iterations.
- Disturbance / variety regulated: Open-ended research question, multiple candidate designs, choice of comparator/falsification language, uncertain proposal quality and variable model outputs.
- Decisive decision or feedback right: The model generates candidate claims/plans/alternatives and assigns critique text and scores; Python selects the highest-scored candidate and governs a fixed iteration loop.
- Decision owner: The configured model-backed first-party proposer/critic role owns content-sensitive research-proposal and critique judgment; deterministic `DiscoveryLoop` owns top-score retention and stop iteration. The operator owns question and inference endpoint selection.
- Supporting / enforcement mechanisms: `ModelAdapter.complete`, JSON parsing/fallback, `Candidate` and `Episode` dataclasses, `max(candidates,key=(score,id))`, `ResearchManifest`, role text injection and JSONL `ReplayBuffer`.
- Closure path: `discovery-rsi campaign` → model-proposed JSON candidates → model critiques/scores each → deterministic selection → `self.history.append(selected)` and optional JSONL append → next bounded generation prompt (with selected parent **ID only**) → final episode summaries.
- Boundary reachability: `cli.py` instantiates `ResearchHarness(adapter_from_env(...))`; `ResearchHarness.run` wires its model-backed proposer and critic into first-party `DiscoveryLoop.run`. No external research coordinator is required for the model to make proposal-level judgments.
- Why this is / is not agent-owned: Removing the model leaves the wrapper able to loop/select/replay but not make case-dependent scientific claims or critique judgments. Model cognition is supplied through an external inference provider yet the first-party package implements and invokes the model-backed task loop. This establishes bounded S1 ownership, **not** validated hypothesis quality or recursive self-improvement.
- Evidence: [core.py](https://github.com/Gen-Verse/DiscoveryRSI/blob/7389e0b58ae50486ab35aa3dcbfa2fa15fea1a91/src/discovery_rsi/core.py); [harness.py](https://github.com/Gen-Verse/DiscoveryRSI/blob/7389e0b58ae50486ab35aa3dcbfa2fa15fea1a91/src/discovery_rsi/harness.py); [cli.py](https://github.com/Gen-Verse/DiscoveryRSI/blob/7389e0b58ae50486ab35aa3dcbfa2fa15fea1a91/src/discovery_rsi/cli.py); [providers.py](https://github.com/Gen-Verse/DiscoveryRSI/blob/7389e0b58ae50486ab35aa3dcbfa2fa15fea1a91/src/discovery_rsi/providers.py); [test_core.py](https://github.com/Gen-Verse/DiscoveryRSI/blob/7389e0b58ae50486ab35aa3dcbfa2fa15fea1a91/tests/test_core.py (deterministic behavior only).
- Basis: structural/explicit executable first-party path; no live externally hosted model run observed during this review.
- Confidence: high for shipped callable S1 loop; empirical scientific output quality untested.
- Caveats: Next-iteration payload contains parent ID but not previous critique/score/evidence; generated plans are not run; default `demo` is deterministic and does not establish model autonomy.

## S2 — Coordination

- State: —
- Function: No first-party inter-S1 mutual-adjustment system established at this single research-proposal-cell boundary.
- Disturbance / variety regulated: Potential proposal–critique disagreement and candidate competition occur inside one task; no evidenced oscillation/conflict between separate autonomous continuing S1 units.
- Decisive decision or feedback right: Fixed generation → per-candidate criticism → scoring/selection serializes stages; it does not negotiate conflicting commitments among independent S1s.
- Decision owner: Deterministic iteration sequence and model-backed task judgments; no separately owned S2 mutual-regulation choice is evidenced.
- Supporting / enforcement mechanisms: `DiscoveryLoop.run` ordering, history, manifest role-name configuration.
- Closure path: Candidate score → single task selected → next prompt; not cross-unit S1 interference → attenuation → reciprocal changed S1 operations.
- Why this is / is not agent-owned: Model generation and criticism are sequential roles in one research task; named `generation`, `critique` and `lead` Markdown snippets are not independent continuing operations.
- Evidence: [core.py](https://github.com/Gen-Verse/DiscoveryRSI/blob/7389e0b58ae50486ab35aa3dcbfa2fa15fea1a91/src/discovery_rsi/core.py); [harness.py](https://github.com/Gen-Verse/DiscoveryRSI/blob/7389e0b58ae50486ab35aa3dcbfa2fa15fea1a91/src/discovery_rsi/harness.py); [plugin.py](https://github.com/Gen-Verse/DiscoveryRSI/blob/7389e0b58ae50486ab35aa3dcbfa2fa15fea1a91/src/discovery_rsi/plugin.py); [manifest.py](https://github.com/Gen-Verse/DiscoveryRSI/blob/7389e0b58ae50486ab35aa3dcbfa2fa15fea1a91/src/discovery_rsi/manifest.py).
- Basis: bounded negative, function-first.
- Confidence: high for assessed operating cell.
- Caveats: A larger externally implemented research swarm could require S2; not part of packaged assessed runtime.

### Absence scope

- Surfaces inspected: `cli.py`, `core.py`, `harness.py`, `manifest.py`, `plugin.py`, `tools.py`, supplied roles/configs and representative tests.
- Plausible first-party paths checked: Sequential proposer/critic, `roles` names, shared `history`, hypothetical conflict between candidates, and model-adapter modes.
- Why no material first-party path remains: One proposal-production cell and a deterministic score/retain step supply no two separately viable S1 units and no interference-specific mutual adjustment returning to both units.

## S3 — Inside-and-now control

- State: —
- Function: No current whole-system resource/commitment management across independently continuing operational units.
- Disturbance / variety regulated: Candidate proliferation, poor proposal scores, excessive iterations and potentially wasteful model calls.
- Decisive decision or feedback right: Developer/operator configures `max_candidates` and `iterations`; code picks highest score, but does not dynamically bargain/allocate whole-system S1 resources or commitments.
- Decision owner: Operator/config author fixes limits; deterministic runtime enforces counts and selects scores; no agent or packaged parent holds evidenced organization-level S3 authority.
- Supporting / enforcement mechanisms: `ResearchManifest.max_candidates`, `ResearchHarness.iterations`, top-score selector and local replay.
- Closure path: Per-candidate selection changes the next **task proposal**; there is no organization-level present-state reporting → binding portfolio resource/commitment decision → enforced change across S1s.
- Why this is / is not agent-owned: A class called `ResearchHarness` or a `lead` prompt does not turn candidate ranking into current organizational management. Human choosing a research question or token budget is not an evidenced supported parent S3 mode.
- Evidence: [manifest.py](https://github.com/Gen-Verse/DiscoveryRSI/blob/7389e0b58ae50486ab35aa3dcbfa2fa15fea1a91/src/discovery_rsi/manifest.py); [core.py](https://github.com/Gen-Verse/DiscoveryRSI/blob/7389e0b58ae50486ab35aa3dcbfa2fa15fea1a91/src/discovery_rsi/core.py); [harness.py](https://github.com/Gen-Verse/DiscoveryRSI/blob/7389e0b58ae50486ab35aa3dcbfa2fa15fea1a91/src/discovery_rsi/harness.py); [cli.py](https://github.com/Gen-Verse/DiscoveryRSI/blob/7389e0b58ae50486ab35aa3dcbfa2fa15fea1a91/src/discovery_rsi/cli.py).
- Basis: bounded negative after checking positive and parent closure.
- Confidence: high for packaged mode.
- Caveats: A future external parent organization could impose budgets and priority governance; not imported.

### Absence scope

- Surfaces inspected: loop control, manifests/config, model call path, replay, role templates and CLI modes.
- Plausible first-party paths checked: `lead` model prompt, critic's score as an intervention, maximum candidate/iteration limits, human-configured campaign and potential parent-controlled runtime.
- Why no material first-party path remains: Limits are static and selection is task-local; neither whole-current S1 accountability nor resource/commitment authority/return loop is shipped.

## S3* — Complementary audit

- State: —
- Function: No evidenced complementary, sufficiently independent reality-access audit of ordinary S1/S3 claims.
- Disturbance / variety regulated: Unsupported hypothesis claims or overconfident model critique could be mistaken for actual evidence.
- Decisive decision or feedback right: The ordinary model critic assigns a score from proposal text; no separate auditor checks source artifacts or independent experiment outcomes.
- Decision owner: Same configured `ModelAdapter` for proposal and critique (separate calls), plus deterministic parser/selector; no independent audit judgment/return path.
- Supporting / enforcement mechanisms: `_critique` prompt, JSON score parsing, local replay and a `record_evidence` registry helper not invoked by the campaign.
- Closure path: Proposal → in-path critique → score → selection; there is no independent raw-data check → management corrective response beyond ordinary task selection.
- Why this is / is not agent-owned: A named `critic` is routine S1 quality checking and does not establish independent complementary access to operational reality.
- Evidence: [harness.py](https://github.com/Gen-Verse/DiscoveryRSI/blob/7389e0b58ae50486ab35aa3dcbfa2fa15fea1a91/src/discovery_rsi/harness.py); [core.py](https://github.com/Gen-Verse/DiscoveryRSI/blob/7389e0b58ae50486ab35aa3dcbfa2fa15fea1a91/src/discovery_rsi/core.py); [tools.py](https://github.com/Gen-Verse/DiscoveryRSI/blob/7389e0b58ae50486ab35aa3dcbfa2fa15fea1a91/src/discovery_rsi/tools.py); [test_core.py](https://github.com/Gen-Verse/DiscoveryRSI/blob/7389e0b58ae50486ab35aa3dcbfa2fa15fea1a91/tests/test_core.py).
- Basis: bounded negative after testing independence/closure.
- Confidence: high for inspected shipped `campaign` path.
- Caveats: External DFM-Bench or human scientist could audit outputs, but their independent judgment is not a wired first-party function in this system-in-focus.

### Absence scope

- Surfaces inspected: `ResearchHarness._critique`, `DiscoveryLoop.run`, `ToolRegistry`, `ReplayBuffer`, role prompts and tests.
- Plausible first-party paths checked: Separate critic call, `record_evidence` tool, source/evidence field on candidates, logs/replay, separate public DFM-Bench.
- Why no material first-party path remains: The score is ordinary in-loop self-evaluation, with no complementary source access or independent audit authority and no S3 corrective audit return. Tools are not invoked by campaign; adjacent evaluator is excluded.

## S4 — Outside-and-then intelligence

- State: —
- Function: No first-party S4 relation that develops future/environment adaptation options **for the current organizational control capability** and returns them to S3.
- Disturbance / variety regulated: Scientific uncertainty, changing domain evidence and alternative hypotheses; all can be part of the S1 research product, not automatically the harness's strategic adaptation.
- Decisive decision or feedback right: The model proposes externally oriented scientific claims, but no evidenced agent or parent right to update the harness's operating policy, capabilities, tools or research organization in response to environmental prospects.
- Decision owner: Model-backed S1 hypothesis generator for research-task content; human may act on its output outside the assessed runtime. There is no wired first-party strategic adaptation owner.
- Supporting / enforcement mechanisms: Manifest's supplied domains/evidence policy, candidates/alternatives, generation/evolution role instructions, parent IDs.
- Closure path: Research proposals may be future-looking but are output artifacts; no external sensing → future-relevant organizational option → S3 conversation → present capability change loop is supplied.
- Why this is / is not agent-owned: Hypothesis generation is the system's **primary operation** here, not proof of organizational S4. The README's recursive model-training program is adjacent; `ResearchHarness._candidates` does not feed past critique/evidence into autonomous capability adaptation.
- Evidence: [harness.py](https://github.com/Gen-Verse/DiscoveryRSI/blob/7389e0b58ae50486ab35aa3dcbfa2fa15fea1a91/src/discovery_rsi/harness.py); [core.py](https://github.com/Gen-Verse/DiscoveryRSI/blob/7389e0b58ae50486ab35aa3dcbfa2fa15fea1a91/src/discovery_rsi/core.py); [manifest.py](https://github.com/Gen-Verse/DiscoveryRSI/blob/7389e0b58ae50486ab35aa3dcbfa2fa15fea1a91/src/discovery_rsi/manifest.py); [role_evolution.md](https://github.com/Gen-Verse/DiscoveryRSI/blob/7389e0b58ae50486ab35aa3dcbfa2fa15fea1a91/plugins/discovery-rsi/roles/role_evolution.md); [README.md](https://github.com/Gen-Verse/DiscoveryRSI/blob/7389e0b58ae50486ab35aa3dcbfa2fa15fea1a91/README.md).
- Basis: bounded negative after testing autonomous and parent-governed adaptation.
- Confidence: medium-high at the pinned portable Python boundary, not a claim about the broader research program.
- Caveats: Some future-looking proposal content might be used as S4 input by a *different* higher-recursion research organization. That does not close S4 here.

### Absence scope

- Surfaces inspected: model proposal prompts, `history` use, `role_evolution.md`, manifests and tools, bounded episodes, README implementation distinction.
- Plausible first-party paths checked: Scientific foresight as S4, model self-improvement claims, parent ID/critique feedback, `evidence_policy`, runtime modification and human-led adaptation.
- Why no material first-party path remains: The shipped model loop generates research outputs without a current-S3 counterpart or capability-update return; parent ID-only next prompt is not strategic organizational adaptation.

## S5 — Policy and identity

- State: —
- Function: No first-party ultimate identity/policy decision and return-to-operation authority at a continuing research organization level.
- Disturbance / variety regulated: Research purpose, data authorization, permissible model, ethics and high-stakes deployment restrictions.
- Decisive decision or feedback right: Operator supplies research question, provider/credentials and domain evidence policy; README warns about human checking. No shipped runtime adjudication of ultimate policy conflicts at its recursion.
- Decision owner: External operator/developer chooses initial configuration; project maintainers govern open source development outside this deployed hypothesis cell. No autonomous or closed first-party parent mode is evidenced.
- Supporting / enforcement mechanisms: Static `ResearchManifest.evidence_policy`, role names, explicit CLI/provider environment configuration, README responsible-use statement.
- Closure path: Human initialization → fixed config → run is not an explicit identity/policy dispute → legitimate parent deliberation → returned authoritative decision changing subsequent operation.
- Why this is / is not agent-owned: Static guardrail wording, domain labels and data-policy strings do not own ultimate organizational identity decisions; model critique does not revise those rules.
- Evidence: [manifest.py](https://github.com/Gen-Verse/DiscoveryRSI/blob/7389e0b58ae50486ab35aa3dcbfa2fa15fea1a91/src/discovery_rsi/manifest.py); [cli.py](https://github.com/Gen-Verse/DiscoveryRSI/blob/7389e0b58ae50486ab35aa3dcbfa2fa15fea1a91/src/discovery_rsi/cli.py); [harness.py](https://github.com/Gen-Verse/DiscoveryRSI/blob/7389e0b58ae50486ab35aa3dcbfa2fa15fea1a91/src/discovery_rsi/harness.py); [README.md](https://github.com/Gen-Verse/DiscoveryRSI/blob/7389e0b58ae50486ab35aa3dcbfa2fa15fea1a91/README.md).
- Basis: bounded negative after checking agent and parent closure.
- Confidence: high for pinned first-party campaign boundary.
- Caveats: Real research institutions have external ethics and policy authorities, but no claimed first-party S5 closure path at this boundary.

### Absence scope

- Surfaces inspected: config schema, role files, CLI/provider paths, `ResearchHarness` prompts and README limits.
- Plausible first-party paths checked: `evidence_policy` string, role authority/lead label, operator configuration, high-stakes warning, maintainer/governance process outside production.
- Why no material first-party path remains: No code path elevates an ultimate-policy question to a legitimate parent with returned binding policy decisions, and no autonomous identity-governance path is wired.

## Recursion

One bounded model-driven research-proposal cell is observable. Candidate ancestry and episode numbers are data lineage, not viable-system recursion. The included claim here is limited to the configured first-party agentic S1 research loop; the separate labs, arena, benchmark and training organization are outside the assessed deployment.

## Variety and escalation

The configurable model can handle open-ended proposal variety; `max_candidates` and `iterations` bound runtime volume. JSON-fallback candidate generation and score-zero fallback exist, but there is no evidence of autonomous failed-source recovery, external fact verification, scientific experiment execution or ethical escalation within the loop. Provider exceptions may terminate a run; `ReplayBuffer` logs nonempty episodes but is not itself a resumption mechanism.

## Evidence gaps

- Source-level review, not a live hosted model trial; no observed model quality, reliability, tokens/cost, or actual hypothesis validation.
- No evidence in the inspected packaged Python runtime that claimed multi-agent evolutionary search, Harbor compilation, HCO training, independent judging or DFM-Bench execution is wired to `campaign`. The broader research paper/system may implement these *elsewhere*; this narrow absence is not an inference about their nonexistence.
- The next generation prompt includes only parent ID, not predecessor contents/score/critique, limiting observable critique-driven iterative adaptation in the shipped mode.
- The default `ToolRegistry` is callable directly, but does not supply model-driven live tool execution or data collection from the shipped `ResearchHarness.run`.
- No assumption of S3*/S4/S5 ownership imported from externally hosted inference providers, operators, laboratories, live arena, or benchmark evaluator.
- Proposal remains `status: proposed` pending Index admission, correct catalog allocation and repository validation; the vector must not be treated as a canonical indexed result until admitted.

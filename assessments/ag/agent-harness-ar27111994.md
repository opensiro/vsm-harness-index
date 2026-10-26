---
harness_id: agent-harness-ar27111994
project_name: Agent Harness (ar27111994)
repository: https://github.com/ar27111994/agent-harness
review_ref: 79e4db95dcf54e7c74a41b070f08843b760ac10a
reviewed_at: 2026-10-26
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Agent Harness (ar27111994)

## Review boundary

- System in focus: The published @ar27111994/agent-harness CLI and its first-party discovery, recommendation, mirror, staging, activation and host-wiring pipeline at the frozen commit.
- Purpose and identity: A reviewable supply chain for reusable agent assets, preparing inspectable inputs for an existing external agent host.
- Relevant environment: Workspace manifests/files, source catalogs, asset publishers, remote registries, host configuration, trust/quarantine evidence, stale installs and operator choices.
- Standard-distribution boundary: TypeScript CLI/library, seven host adapters, ARD discovery metadata, optional bounded model enrichment/recommendation review, lifecycle state and the documented maintenance workflows. An arbitrary downloaded agent/skill is an input, not automatically a first-party operational actor.
- Credited operating / distribution surfaces: [public scope and lifecycle](https://github.com/ar27111994/agent-harness/blob/79e4db95dcf54e7c74a41b070f08843b760ac10a/README.md#where-it-fits), [workspace pipeline](https://github.com/ar27111994/agent-harness/blob/79e4db95dcf54e7c74a41b070f08843b760ac10a/src/pipeline.ts), [host adapter registry](https://github.com/ar27111994/agent-harness/blob/79e4db95dcf54e7c74a41b070f08843b760ac10a/src/host-adapters/registry.ts), [package boundary](https://github.com/ar27111994/agent-harness/blob/79e4db95dcf54e7c74a41b070f08843b760ac10a/package.json).
- Adjacent first-party surfaces excluded from ownership: Repository development/release CI and tests, separate demo-video repository and any user-invoked AI assistant executing the maintenance prompt. Claude Code, Codex, Copilot, Cursor, Zed, OpenCode and Pi remain external hosts; their task reasoning/action loops cannot be inherited from writing their configuration.
- First-party operating / deployment modes considered: Preview/apply/reset CLI, workspace lifecycle, optional model enrichment and recommendation reranking, scheduled report maintenance and external-host wire-in. The enrichment paths were examined rather than dismissed solely from the README's no-runtime claim.
- Recursion level: Asset-management utility, not a running coding-agent organization and not the upstream maintainer organization.
- Reviewed revision: `79e4db95dcf54e7c74a41b070f08843b760ac10a`.
- Observation date: 2026-10-26.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The CLI scans workspace demand, harvests source metadata, constructs a catalog and selection, ranks recommendations, acquires pinned bundles, stages assets and materializes host-specific activation/wiring. runWorkspacePipeline explicitly invokes these fixed phases, checks deterministic progress/exit status, and repeats bounded acquire/install batches. Adapters own files/settings, native install actions and host readiness metadata; their executable/version/readiness fields do not instantiate a task-performing AI actor.

The optional model paths are material counterevidence to a simplistic “no model means excluded” argument. Discovery enrichment sends bounded demand/catalog inputs and expects a summary, recommendations and warnings. Recommendation AI review optionally applies bounded rerank adjustments to a report. They are model-assisted metadata transformations, not a model-selected environment/tool/action loop for carrying out arbitrary workspace tasks. Neither supplied response schema grants the model a tool repertoire or a continuing discretionary task execution protocol.

The workspace evolution playbook tells an external assistant or human which reports and commands to inspect. Quarantine/trust/native-install choices remain explicitly reviewed. Scheduled maintenance runs CLI commands and emits artifacts plus PR/issue intents; it does not silently instantiate that external assistant. The Codex ownership state machine protects host configuration files across install/reset transitions; “ownership” there means file provenance, not VSM organizational decision ownership.

## Operational model and admission decision

**Prospective canonical disposition: excluded-no-agentic-vsm.** The package is substantive adjacent agent infrastructure, but the assessed distribution does not establish autonomous first-party S1 operation under the selected general Index contract. This is a scope decision, not a product-quality judgment or a claim that the software has no useful automation.

The decisive distinction is between preparing a host's context and owning an agent's outcome-producing decision/action loop. Remove the external coding hosts: this CLI can still discover, score, mirror, quarantine, stage and wire assets, but it cannot independently choose and execute a coding task from observed project/tool feedback. Remove the optional model endpoint: the deterministic asset lifecycle remains. Add model enrichment: bounded report/rerank content changes, but no autonomous task actor/action loop is thereby installed. A user may assemble such an organization around these assets; that is a different, explicitly composed system boundary.

## S1 — Operations

- State: —
- Function: No material first-party autonomous task-performing operational unit in this asset utility.
- Disturbance / variety regulated: Source/asset drift and workspace demand are processed by configured lifecycle rules; ordinary coding/task variety remains with the external host agent.
- Decisive decision or feedback right: The user invokes pipeline/apply and chooses trust/install policy. Optional inference writes bounded enrichment or rerank results; it does not choose arbitrary project actions from successive tool feedback.
- Decision owner: Human/developer for lifecycle rules and approvals; external host for autonomous task execution. No first-party agent S1 owner is established here.
- Supporting / enforcement mechanisms: Catalog scoring, mirror locks, quarantine, installation state, host adapters, preview/apply/reset and model report validation.
- Closure path: Workspace/source input → prescribed pipeline → asset/configuration outputs; optional model response → validated report/adjusted ranking. Autonomous coding closure begins in an adjacent host rather than this package.
- Why this is / is not agent-owned: Executing many deterministic stages or calling an LLM once is not evidence of a supplied outcome-owning autonomous agent. The actual optional response/consumer paths were checked.
- Evidence: [explicit “does not run agents” boundary](https://github.com/ar27111994/agent-harness/blob/79e4db95dcf54e7c74a41b070f08843b760ac10a/README.md#where-it-fits), [fixed pipeline and progress loops](https://github.com/ar27111994/agent-harness/blob/79e4db95dcf54e7c74a41b070f08843b760ac10a/src/pipeline.ts), [enrichment schema/orchestration](https://github.com/ar27111994/agent-harness/blob/79e4db95dcf54e7c74a41b070f08843b760ac10a/src/domains/discovery/ai-enrichment.ts), [bounded optional reranking](https://github.com/ar27111994/agent-harness/blob/79e4db95dcf54e7c74a41b070f08843b760ac10a/src/recommend/ai-review.ts).
- Basis: explicit + structural.
- Confidence: High for this frozen package boundary.
- Caveats: This does not grade the independent hosts or a separately assembled agent organization using installed assets.

### Absence scope

- Surfaces inspected: README scope/lifecycle, package manifest, workspace pipeline, adapter registry, optional discovery enrichment/recommendation AI review, ownership contract and maintenance/evolution playbooks.
- Plausible first-party paths checked: workspace end-to-end execution, model-generated catalog enrichment, model rerank application, native-host readiness/install, generated agent assets and scheduled AI-agent maintenance prompt.
- Why no material first-party path remains: The shipped execution ends in metadata, configuration, asset state or bounded report transformations. An autonomous task/action owner is not instantiated or given a feedback-driven tool loop; the documented maintenance assistant and operational host remain external.

## Metasystem boundary checks

No positive S2–S5 ownership claims are published for an excluded system. Specific candidate paths were checked rather than inferred from terms such as control loop, AI review or ownership:

- S2: Host-file ownership/transition protection and catalog deduplication regulate asset/configuration consistency; no distinct first-party S1 task units and inter-S1 coordination/return relation are instantiated.
- S3: Recommendation budgets, trust tiers, quarantine and preview/apply are developer/operator lifecycle controls. No whole-current first-party agent organization with a substantive present-control owner is supplied.
- S3*: Optional AI recommendation review challenges ranking input, while report/manifest checks validate asset handling. These do not establish complementary audit of first-party autonomous operational claims with corrective control over such operations.
- S4: Demand/source-drift detection and workspace evolution propose asset maintenance, including useful externally derived changes. They do not cure the missing admitted autonomous S1 boundary or establish an internal organization-level prospective adaptation owner. No broader assembled host system is graded here.
- S5: Human quarantine decisions and Codex file-ownership transitions are trust/file management, not identity/ultimate-policy arbitration and returned governance for an autonomous organization.

Evidence: [workspace evolution and explicit external assistant prompt](https://github.com/ar27111994/agent-harness/blob/79e4db95dcf54e7c74a41b070f08843b760ac10a/docs/playbooks/WORKSPACE-EVOLUTION-PLAYBOOK.md), [scheduled maintenance and human review boundaries](https://github.com/ar27111994/agent-harness/blob/79e4db95dcf54e7c74a41b070f08843b760ac10a/docs/guides/MAINTENANCE-WORKFLOW.md), [Codex file ownership](https://github.com/ar27111994/agent-harness/blob/79e4db95dcf54e7c74a41b070f08843b760ac10a/CODEX-OWNERSHIP-TABLE.md), [host registry](https://github.com/ar27111994/agent-harness/blob/79e4db95dcf54e7c74a41b070f08843b760ac10a/src/host-adapters/registry.ts).

## Distributed OSS parent arrangement

Maintainers and users may govern development or local asset trust. That authority is separate from a function-specific parent mode in an admitted autonomous harness; no parent ownership states are inferred from it.

## Self-hosted and non-human modes

Local CLI use and optional configured inference endpoints do not supply an autonomous non-human organization. External-host integration is deliberately supported without taking ownership of those hosts' agent loops.

## Recursion

The lifecycle stages and host-adapter hierarchy are not recursive viable operational units.

## Variety and escalation

Pinned mirrors, trust evidence, quarantine and explicit operator review preserve asset provenance and uncertainty. These are useful supply-chain controls within the utility boundary, not automatic VSM grades.

## Evidence gaps

Static pinned-source inspection; no live model, host-agent or provider run. No upstream npm dependency installation/test run was performed. The rejection is supported by the inspected execution/response schemas, not by an unavailable runtime test. A later version supplying a first-party autonomous operational loop, or a separately declared assembled system, would require a new bounded assessment. Proposed lifecycle remains noncanonical until the separate exclusion transaction.

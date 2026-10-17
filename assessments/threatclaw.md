---
harness_id: threatclaw
project_name: ThreatClaw
repository: https://github.com/threatclaw/threatclaw
review_ref: 71540e5da1fc4dd5ff62c37842de25efab67a3f1
reviewed_at: 2026-10-17
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# ThreatClaw

## Review boundary

- System in focus: Shipped first-party ThreatClaw Rust incident monitoring/investigation/response organization, including its task queues and workers, intelligence cycle, ReAct and per-incident multi-step model investigation, deterministic verdict reconciler, configured autonomy modes, human-authorized remediation and signed-rule update components. Evaluation is at a single deployed SOC installation / incident-response organization, not at a supplier or customer's whole corporation.
- Purpose and identity: Monitor security assets/findings, investigate incidents, manage current incident-response workload, challenge model incident conclusions against alternative evidence and route human-approved defensive actions.
- Relevant environment: Assets and their telemetry; correlated Sigma/ML/CVE/KEV/graph findings; local/cloud LLM backends; incident records; configured SIEM/EDR/MCP tools; human responder; ongoing security threats; signed provider-managed threat intelligence.
- Standard-distribution boundary: The pinned Rust application and actual service boot/ticker wiring, first-party intelligence/agent/queue/remediation functions and supported modes. Exclude third-party scanner/SIEM/firewall/EDR and LLM internals; a rule feed/vendor decision is external even when its signed bytes are installed.
- Credited operating / distribution surfaces: [src/channels/web/handlers/threatclaw_api.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/channels/web/handlers/threatclaw_api.rs), [src/agent/intelligence_engine.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/intelligence_engine.rs), [src/agent/investigation.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/investigation.rs), [src/agent/react_runner.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/react_runner.rs), [src/agent/react_cycle.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/react_cycle.rs), [src/agent/task_queue/mod.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/task_queue/mod.rs), [src/agent/task_queue/pool.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/task_queue/pool.rs), [src/agent/task_queue/supervisor.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/task_queue/supervisor.rs), [src/agent/verdict_reconciler.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/verdict_reconciler.rs), [src/agent/evidence_tracker.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/evidence_tracker.rs), [src/agent/remediation_engine.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/remediation_engine.rs), [src/agent/remediation_guard.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/remediation_guard.rs), [src/agent/mode_manager.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/mode_manager.rs), [src/agent/rule_updater.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/rule_updater.rs), [src/agent/soul.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/soul.rs).
- Adjacent first-party surfaces excluded from ownership: Security marketing terminology (ClawMind/ClawShield), counts of bundled playbooks, release changelogs, simulations, unexecuted scripts, provider-hosted signed packs/LLMs and neighboring assessment systems. Evidence from tests and examples cannot replace demonstrated live installed paths.
- First-party operating / deployment modes considered: Booted Intelligence Engine and its adaptive cycle scheduling, autonomous model investigation and per-asset cooldown, typed reconciliation Off/Lenient/Strict, configured Analyst/Investigator/Responder/AutonomousLow runtime modes, protected human-in-the-loop remediation and optional managed rules updater.
- Recursion level: A single SOC installation with multiple asset/incident operations, a global first-party current-work scheduler, separate deterministic corroboration of claimed incidents and a configured human security operator. The outside organization and integrated EDRs are not granted first-party S5 or agent autonomy.
- Reviewed revision: `71540e5da1fc4dd5ff62c37842de25efab67a3f1` frozen in intake #186, batch #1648 row 3.
- Observation date: 2026-10-17.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

`start_background_services` in the installed ThreatClaw API starts the Intelligence Engine and related connector, scanning and investigation workers exactly once per process. The Intelligence Engine builds a whole-asset `SecuritySituation` from open findings/alerts and graph context, computes priorities, selects the highest-risk monitored asset for investigation, enforces inventory gates, active-investigation checks and verdict-dependent dedup cooldowns, and changes its next evaluation interval based on observed security conditions. This gives current-work regulation, not an agent making policy merely because the module is called an intelligence engine. [src/channels/web/handlers/threatclaw_api.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/channels/web/handlers/threatclaw_api.rs); [src/agent/intelligence_engine.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/intelligence_engine.rs).

`run_investigation` is the principal S1-reachable model agent path: build a real incident dossier, collect deterministic preflight skill evidence, query configured model, parse severity/confidence and model-requested skills, execute bounded requests, feed their results back into subsequent prompts, and terminate with a classified verdict. The separate `run_react_cycle` path builds observations, invokes a configured LLM, conditionally escalates to enriched or cloud reasoning and validates proposed actions. The model supplies task-level interpretation/skill selection; first-party code owns the iterative tools/feedback loop. Neither separately installed Ollama weights nor the external sensor performs the organization. [src/agent/investigation.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/investigation.rs); [src/agent/react_runner.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/react_runner.rs); [src/agent/react_cycle.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/react_cycle.rs).

Multiple investigations, graphical substeps and queued LLM calls can contend for scarce same-installation CPU-model inference and duplicate one asset's investigation. The globally shared `INVESTIGATION_SEMAPHORE` gates competing incident model calls at one permit, while asset/incident dedup and outcome-dependent cooldown stop repeated work from oscillating on the same event. The shipped task-queue worker pool also holds semaphore permits while tasks are claimed atomically, executed and completed/failed; configurable backpressure degrades or rejects overload. These are first-party structurally enforced coordination mechanisms, not separate LLM agents independently negotiating scheduling. [src/agent/intelligence_engine.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/intelligence_engine.rs); [src/agent/task_queue/supervisor.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/task_queue/supervisor.rs); [src/agent/task_queue/pool.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/task_queue/pool.rs); [src/agent/task_queue/backpressure.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/task_queue/backpressure.rs).

The distinct first-party `verdict_reconciler` accepts the model's verdict but recomputes credibility from real dossier evidence: independent Sigma alerts, CISA KEV/asset scores, graph lateral-movement context, typed validation errors, absence of executed investigations and citation checking. In enabled `Strict` mode it can override an LLM `confirmed`/false-positive verdict and the normal `run_investigation` implementation **applies** the reconciled fields into `parsed` before the downstream verdict object. In `Lenient` it records differences without applying them; in `Off` it does not do this. This provides a structurally independent **constructor-owned** complementary audit path when Strict is configured; the scorer/dossier input is not a second autonomous LLM critic. [src/agent/investigation.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/investigation.rs); [src/agent/verdict_reconciler.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/verdict_reconciler.rs); [src/agent/evidence_tracker.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/evidence_tracker.rs).

`AgentMode` is configured by the operator. Investigator mode can propose investigations/actions but not autonomously execute write remediation; Responder requires HITL; AutonomousLow permits some validated low-risk commands when the command does not require HITL. The separately enforced `remediation_engine` checks global pause, target protection, approval/rate/atomic execute-once status, and then calls installed provider adapters. Neither the mode switch, model action proposal nor static AGENT_SOUL integrity file is proof of ultimate S5 policy settlement. [src/agent/mode_manager.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/mode_manager.rs); [src/agent/react_cycle.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/react_cycle.rs); [src/agent/remediation_engine.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/remediation_engine.rs); [src/agent/remediation_guard.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/remediation_guard.rs); [src/agent/soul.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/soul.rs).

A signed versioned threat-data updater is reachable from an optional configured six-hour Intelligence ticker path and installs external supplier-chosen Sigma, KEV, MITRE, IOC or other packs after signature/hash checks. It changes detection inputs and may expand detection capability, but the reviewed path performs **supplier-manifest version synchronization** rather than a first-party organizational intelligence function comparing alternative future response strategies, deciding adaptations and returning chosen strategic options to ongoing S3. This is a bounded S4 non-finding, not denial that up-to-date threat information matters. [src/agent/rule_updater.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/rule_updater.rs); [src/agent/intelligence_engine.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/intelligence_engine.rs).

## S1 — Operations

- State: A
- Function: Autonomous bounded model-based incident investigation and evidence/tool selection with live feedback.
- Disturbance / variety regulated: Unknown incidents, evolving signals, noisy security telemetry, ambiguity about CVE/alert severity, missing evidence and failing skills.
- Decisive decision or feedback right: Configured first-party model-driven investigation decides whether more context is needed and names investigation skills/parameters; loop reinvokes model with executed skill results and returns a verdict. Distinct scheduled ReAct cycle also chooses model-driven threat correlation/actions.
- Decision owner: ThreatClaw-owned agent invocation and its configured model reasoning, with bounded prompts and tool dispatch; not an externally authored vendor agent.
- Supporting / enforcement mechanisms: Dossier, preflight enrichment, skill registry, timeouts, max iterations/max calls, typed response parser, security mode and safe-action whitelist.
- Closure path: asset dossier → model suspicion/skill request → first-party bounded skill execution → returned observation in following prompt → revised verdict/action proposal → recorded incident.
- Boundary reachability: Booted Intelligence ticker can launch `run_investigation` from selected current asset, with semaphore and incident store; `run_react_cycle` also has an installed ticker route.
- Why this is / is not agent-owned: The model decides actual investigative steps based on in-run observations rather than consuming only fixed rule tables; default preflight is deterministic and does not remove model discretion on subsequent skills.
- Evidence: [src/agent/investigation.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/investigation.rs); [src/agent/react_runner.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/react_runner.rs); [src/agent/intelligence_engine.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/intelligence_engine.rs); [src/agent/investigation_skills.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/investigation_skills.rs).
- Basis: Explicit reachable source-level model/skill/feedback loop.
- Confidence: High for the implemented configured model path; no live external inference or detection quality measured.
- Caveats: Operational mode and backend availability matter; Analyst mode disables ReAct, and malicious output is constrained by a separate guard.


## S2 — Coordination

- State: C
- Function: Prevent harmful concurrency and oscillation between distinct current incident/skill/model operations competing for one finite inference/worker resource or repeated asset claims.
- Disturbance / variety regulated: CPU-served Ollama cannot safely process unbounded concurrent investigations; simultaneous tasks could overload model service or duplicate work on a single incident/asset.
- Decisive decision or feedback right: First-party semaphore, atomic claim, queue capacity and cooldown rules determine when other in-flight S1 investigations may proceed; model does not choose conflict mitigation discretion.
- Decision owner: Deterministic first-party worker-pool/Intelligence admission and suppression paths under operator-provided limits.
- Boundary reachability: Standard service starts the Intelligence ticker and installed task pools; Intelligence spawns incident investigations under the global semaphore, the active registry checks for already investigated assets, and queue supervisors atomically claim and execute work. Their effects gate actual future agent investigation, not an unreachable utility module.
- Supporting / enforcement mechanisms: `INVESTIGATION_SEMAPHORE` with one permit across investigation requests, `WorkerPool` permits across task-kind workloads, atomic `claim_next_task`, retry-on-fail, asset dedup registry and versioned cooldown.
- Closure path: competing S1 submissions/active investigation status → permit or dedup/queue decision → task blocks/skips or is admitted → completion frees permit and updates task/asset state → subsequent S1 attempt changes.
- Distinct S1 units: Separately launched dossier investigation tasks and graph/LLM/skill workloads; each can execute model/tool-bearing incident operations.
- Inter-S1 disturbance: Simultaneous calls to scarce one-at-a-time CPU LLM and repeated evaluations of the same incident degrade reliability, create feedback storms and compete for active current security monitoring.
- Attenuating coordination relation: One-permit serialized model investigations, atomic claim/worker capacity, per-asset cooling and load-based admission.
- Feedback into subsequent S1 behaviour: Semaphores release on completion; verdict/error cooldowns are written back and gate future investigations; queued tasks enter running/done/failed states.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: These paths regulate concrete concurrency collisions and duplicate incident investigation, beyond data transport or merely sequencing a single authored workflow.
- Why this is / is not agent-owned: A statically configured bounded structure enforces noninterference; it is S2=C, not an agent self-negotiating arbitration.
- Evidence: [src/agent/intelligence_engine.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/intelligence_engine.rs); [src/agent/task_queue/pool.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/task_queue/pool.rs); [src/agent/task_queue/supervisor.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/task_queue/supervisor.rs); [src/agent/task_queue/backpressure.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/task_queue/backpressure.rs).
- Basis: Structural default operating concurrency and source-evidenced failure mode; even if a particular incident pair has not been reproduced in this review.
- Confidence: High for named shared LLM semaphore and atomic worker claims.
- Caveats: Does not prove distributed multi-replica safety or all races are eliminated; the asset dedup cache is in-memory.


## S3 — Inside-and-now control

- State: C
- Function: Current whole-installation prioritization, admission and escalation of monitored asset investigations from a global security situation and finite investigation capacity.
- Disturbance / variety regulated: Many simultaneous findings/alerts, competing asset risks, finite investigation throughput, alert fatigue and high-severity attack needing faster monitoring.
- Decisive decision or feedback right: First-party scoring/threshold scheduler reads the combined current asset picture, changes polling interval, selects the highest-risk monitored asset, starts/defers incident work, suppresses predictive-only/duplicate/unowned targets, and can propose HITL response.
- Decision owner: Deterministic first-party Intelligence Engine plus configured rules/operator mode. The incident model supplies conclusions but does not own whole-installation resource allocation.
- Boundary reachability: The production start_background_services launcher starts spawn_intelligence_ticker; the ticker awaits run_intelligence_cycle and uses the resulting global SecuritySituation to choose a next interval, highest-priority asset, inventory/dedup eligibility, incident creation and real run_investigation before the next cycle.
- Supporting / enforcement mechanisms: SecuritySituation aggregation, `decide_notification_level`, sorted/maximum risk asset selection, asset inventory gate, dedup/active registry, dynamic interval control, spawned investigation and remediation guard.
- Closure path: whole-installation findings/alerts/graph view → asset score and alert/priority selection → actual incident investigation/deferral with capacity guard → stored verdict/result → updated next-cycle current situation and scheduling.
- Whole-system current view: Aggregated findings/alerts grouped by canonical monitored asset, global score, attack flags and current investigation registry across the single SOC installation.
- Current-control decision scope: Present monitoring cadence, which asset is eligible for action now, when incident investigation is admitted, how duplicate/noise work is suppressed, and when the SOC operator receives an escalation.
- Why this is / is not agent-owned: The decisive selection is expressed in first-party rules (`max_by`, thresholds, cooldown, inventory membership), not dynamically chosen by an S3 policy model. The resident model controls a specific S1 dossier, not the overall current commitment selection; therefore S3=C.
- Evidence: [src/agent/intelligence_engine.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/intelligence_engine.rs); [src/channels/web/handlers/threatclaw_api.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/channels/web/handlers/threatclaw_api.rs); [src/agent/mode_manager.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/mode_manager.rs); [src/agent/remediation_engine.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/remediation_engine.rs).
- Basis: Installed reachable whole-SOC scoring/admission/intervention path.
- Confidence: Medium-high for bounded current priority regulator; not asserted as full staffed-SOC governance.
- Caveats: No first-party strategic budget bargaining or durable organizational project-level S3 autonomy. In default Investigator mode meaningful disruptive write remediation remains human authorized.


## S3* — Complementary audit

- State: C
- Function: Challenge the model investigator's incident claims with independent structured dossier/citation/telemetry evidence and feed a binding corrective verdict in enabled Strict mode.
- Disturbance / variety regulated: Model-fabricated CVEs, MITRE references or citations; confident unsupported 'confirmed' verdicts; erroneous false-positive dismissal despite Sigma/KEV/ML corroboration.
- Decisive decision or feedback right: Deterministic `reconcile_verdict_full` rules compare the model snapshot with score/Sigma/CISA KEV/graph, citation checks, actual skill-call counts, typed validation; Strict overrides the conclusion when justified.
- Decision owner: First-party deterministic reconciliation and separately computed corroborating signals, not another model auditor. Operator chooses `Strict`, `Lenient` or `Off` configuration.
- Boundary reachability: The actual incident run_investigation path parses the model answer, builds validators/citation report from stored dossier and evidence, invokes verdict_reconciler::reconcile_verdict_full and, whenever Strict outcome.apply is true, overwrites parsed verdict, severity and confidence before final incident state is emitted. This is not only an isolated unit test.
- Supporting / enforcement mechanisms: Typed validators, citation tracker, `SignalsSnapshot`, `rule_* ` adjustments and investigation result assembly.
- Closure path: model-issued verdict → alternative dossier/graph/ML/Sigma/citation/skill evidence and validation → reconciler chooses challenge → under Strict, revised severity/verdict/confidence overwrites `parsed` → final incident classification/escalation; discrepancies logged.
- Claim being audited: Whether the LLM's reported incident verdict and supporting evidence are credible enough to drive severity/escalation.
- Ordinary reporting path: Model-issued `parsed.verdict`, severity, confidence and narrative from iterative S1 investigation.
- Complementary access path: First-party independent deterministic alert/risk context, KEV presence, graph context, citation pointers verified against real dossier, actual executed-skill counter and typed structural checks.
- Independence boundary: Materially different *evidence and rules* compared to LLM self-judgment; not a separate human/reviewer deployment. The evidence is provided by the same installation and may be incomplete; rules skip missing graph context and do not establish independent source provenance for every field.
- Who acts on findings: `run_investigation` applies `outcome.log.reconciled` to its live `parsed` verdict only if `outcome.apply` (Strict); that final verdict feeds incident outcome. Lenient only logs and Off disables.
- Why this is / is not agent-owned: Rules bind correction from complementary data but no independent LLM agent chooses it, so S3*=C, not S3*=A.
- Evidence: [src/agent/investigation.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/investigation.rs); [src/agent/verdict_reconciler.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/verdict_reconciler.rs); [src/agent/evidence_tracker.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/evidence_tracker.rs); [src/agent/validators/mod.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/validators/mod.rs); [src/agent/validation_mode.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/validation_mode.rs).
- Basis: Explicit source-attested alternative-evidence challenge in actual investigation path, binding only under Strict mode.
- Confidence: High for existence of Strict-mode override; limited/conditional as audit coverage.
- Caveats: Default validation mode must not be assumed strict without checking runtime config; this is a **supported conditional** C path, not a mandatory protected independent auditor. An internal source bug could contaminate both the model dossier and verifier input.


## S4 — Outside-and-then intelligence

- State: —
- Function: No supported first-party strategic/prospective organizational adaptation decision with a two-way return to S3 established at this revision.
- Disturbance / variety regulated: Changing new IoCs, Sigma/MITRE/KEV feeds, future threats and feature/vendor rule updates are externally relevant, but ingestion alone does not prove S4.
- Decisive decision or feedback right: The optional updater follows an external supplier's signed pack manifest/version and installs verified bytes; it does not evaluate future alternatives, select a capability-investment/adaptation option or negotiate it with current control. Operational thresholds are prewritten rules.
- Decision owner: External supplier for package contents/version, administrator for support key/enablement, deterministic first-party signature/hash/version synchronizer for installation.
- Supporting / enforcement mechanisms: 6-hour updater schedule, signed-manifest verification, per-pack registry, anti-rollback and verified install, enrichment periodic resync.
- Closure path: External feed → validated data/rule pack → current detection configuration may change, but no first-party evidenced prospective option synthesis/selection → S3 dialogue → organizational adaptation decision/feedback cycle.
- Why this is / is not agent-owned: Automatic update is a supply synchronization mechanism, not an autonomous organization-level S4 regulator merely because it ingests evolving threats.
- Evidence: [src/agent/rule_updater.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/rule_updater.rs); [src/agent/intelligence_engine.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/intelligence_engine.rs); [src/agent/sigma_engine.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/sigma_engine.rs); [src/agent/mode_manager.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/mode_manager.rs).
- Basis: Bounded source review of strongest apparent candidate, signed pack updater, plus enrichment and mission/planning alternatives.
- Confidence: Medium; would change with explicit documented first-party adaptive option/test/apply path.
- Caveats: Operational detection improvement is possible through new signatures; the negative state is about missing **S4 organizational function**, not inability to update rules.

### Absence scope

- Surfaces inspected: Rule updater installers/signed manifest, intelligence tick/enrichment, task investigation, static agent rules, risk model and mode controls.
- Plausible first-party paths checked: Automated provider-threat-pack upgrades, IOC/CVE ingestion, changed scores/intervals, model escalation and periodic rule reload.
- Why no material first-party path remains: No observed agent/constructor option-development authority exploring future capability choices and returning a selected adaptation through an organization-level S3 loop; supplier-managed pack changes remain external-content updates.


## S5 — Policy and identity

- State: —
- Function: No first-party decisive ultimate identity/ethos/policy-setting and returned governance loop shown for this deployed SOC installation.
- Disturbance / variety regulated: Model safety, operator action privileges, immutable-soul tampering and tool permission boundaries are regulated by static configuration and enforced action checks.
- Decisive decision or feedback right: Project-supplied `AGENT_SOUL.toml` is hash-verified, while the operator sets autonomy mode/approval. Neither a live first-party final-policy conflict adjudicator nor binding identity-policy adaptation/return is shown.
- Decision owner: External project developer and site SOC administrator configure fixed identity and operational constraints; no dedicated S5 in assessed first-party runtime proven.
- Supporting / enforcement mechanisms: Compile-time soul hash, immutable_rules prompt injection, mode settings, whitelist, nonce/atomic approvals, protected infrastructure guard.
- Closure path: Static rule check or human consent gates a current command, but no first-party ultimate issue → responsible higher-level governing decision → identity/policy settlement → returned organizational response loop.
- Why this is / is not agent-owned: Static 'soul' data, boot hash and human approval do not themselves create Beer S5; S1 can propose actions but cannot redefine ultimate system identity.
- Evidence: [src/agent/soul.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/soul.rs); [AGENT_SOUL.toml](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/AGENT_SOUL.toml); [src/agent/mode_manager.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/mode_manager.rs); [src/agent/remediation_engine.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/remediation_engine.rs); [src/agent/remediation_guard.rs](https://github.com/threatclaw/threatclaw/blob/71540e5da1fc4dd5ff62c37842de25efab67a3f1/src/agent/remediation_guard.rs).
- Basis: Bounded negative analysis of first-party identity, security and approval surfaces.
- Confidence: Medium-high for reviewed operating scope.
- Caveats: A customer's actual security policy and supplier stewardship are separate organizations; don't inherit them into the installed software automatically.

### Absence scope

- Surfaces inspected: Compiled AgentSoul identity/integrity, operator mode configuration, HITL action approvals, remediation guard, supplied mission and packaging.
- Plausible first-party paths checked: Immutable rules, approval/nonce gates, pause/kill-switch, customer policy data and human privilege.
- Why no material first-party path remains: The available paths validate or enforce already selected constraints, rather than provide a first-party ultimate settlement of changing identity/policy alternatives and a corrective return.


## Distributed OSS parent arrangement

Open-source maintainer identity and the vendor-maintained rule-pack supply chain are external to each customer's deployed SOC. The application offers a configurable autonomous/parent-approval continuum for security actions, but there is no source-supported parent ultimate S5 or standing S4 adaptive identity settlement at this installed-software recursion. Whole-current S3 rule-based control and operator remediations must be kept distinct.

## Self-hosted and non-human modes

Security operation can be self-hosted with provider inference configured locally or by API. `Analyst` is deterministic; `Investigator` permits model analysis but human response; `Responder` HITL; `AutonomousLow` permits selected safer automatic actions while explicitly HITL-tagged commands still require approval. S1 model operation, S2/S3 constructors and conditional S3* do not imply model authorization for destructive response. The default `Investigator` limits are relevant but not exhaustive of supported modes.

## Recursion

Current asset/incident investigations are operational S1; multiple such activity lanes compete for SOC throughput. Semaphore/dedup S2 helps stabilize parallel work; the global intelligence engine's scoring/prioritization is constructor S3 at the one-installation level; deterministic corroboration can independently challenge model incident claims as S3*. The SOC operator, external EDR/SIEM and rule-pack supplier do not by naming become additional in-scope VSM decision owners.

## Variety and escalation

ThreatClaw amplifies investigation through model/skill actions and sensor data; attenuates variance with filters, validation, per-asset dedup and strict review. The intelligence cycle feeds highest-risk eligible incidents back into active investigation; critical situations escalate to human operator and guarded actions. Optional cloud reasoning and model confidence escalation are **task-level inference fallbacks**, not necessarily Beer-style metasystem authority. No live end-to-end SOC trace was produced.

## Evidence gaps

- No production security event, external model inference or threat-action run was executed. Claims are pinned first-party source reachability, not validation of actual detection efficacy or completeness of integrated firewalls.
- `S2=C` protects a concrete shared inference workload and duplicate incident processing in one runtime; this does not prove cross-node lock semantics for a distributed SOC fleet.
- `S3=C` relies on explicit installed global situation/regulation paths, not a model selecting institution-wide current work. The operator owns dangerous write authorizations in normal modes.
- `S3*=C` applies only to enabled `Strict` verdict validation; `Lenient` observes and `Off` bypasses. No independent reviewer model/person or tamper-proof sensor guarantee is claimed.
- `S4=—`, `S5=—` are bounded first-party function absences, not claims of impossibility or lack of future changes/security policy. No functionality is borrowed from the security vendor or its hosted rule packs.

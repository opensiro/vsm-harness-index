---
harness_id: akmatori
project_name: Akmatori
repository: https://github.com/akmatori/akmatori
review_ref: be62d926fe6d92dceb5cf12e9a95cb587433cdf1
reviewed_at: 2026-11-14
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: P
autonomy_s5: —
---

# Akmatori

## Review boundary

- System in focus: The self-hosted first-party Akmatori AIOps runtime: independently scoped incident investigation agents, alert correlation, optional post-investigation incident merger, post-incident evidence memory extraction and opt-in self-improvement proposal evaluation with operator approval.
- Purpose and identity: Diagnose real infrastructure incidents from alerts and tools, coordinate overlapping investigations and improve future diagnostic capability under operator supervision.
- Relevant environment: Monitoring alerts, host/Kubernetes/SSH telemetry, tool failures, repeated infrastructure incidents, operator feedback, runbooks, LLM/model provider responses and remediation risk.
- Standard-distribution boundary: Source-shipped API and services, agent worker, MCP Gateway, database and first-party seeded system cron modes. External monitoring systems, model providers, physical infrastructure, Slack and operator-provided credentials are environment, not attributed first-party decision owners.
- Credited operating / distribution surfaces: agent-worker/src/agent-runner.ts and orchestrator.ts; internal/services/alert_correlator.go, incident_merger.go, incident_memory_extractor.go, incident_memory_extraction_prompt.go, memory_extraction_apply.go, proposal_service.go; internal/database/db.go seeded improvement-evaluator; internal/handlers/alert_processor.go; mcp-gateway/internal/tools/proposals/proposals.go; first-party operator approval API.
- Adjacent first-party surfaces excluded from ownership: Repository contributor prompts/rules as governance evidence only; docs/plans and tests not executed as operational agent roles; external connector/tool implementations do not donate independent organizational decision rights; screenshots/demos are supplementary.
- First-party operating / deployment modes considered: Default incident response and enabled alert correlation; separate optional incident merge gate (disabled by default); enabled post-incident memory extraction; operator-opt-in improvement-evaluator cron (disabled by default); human approval/rejection of improvement proposals and risky remediation actions.
- Recursion level: One self-hosted Akmatori incident-response system with separate incident investigations as operational S1 units. Individual command executions and operator changes to one incident are not automatically separate higher-level VSM functions.
- Reviewed revision: be62d926fe6d92dceb5cf12e9a95cb587433cdf1.
- Observation date: 2026-11-14.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

Akmatori receives normalized alerts, creates or attaches incident records, dispatches LLM-based investigation via a separate agent worker and exposes infrastructure tools through the MCP gateway. Risky remediation can create operator-approved proposals instead of immediately executing. Alert correlation first compares incoming alerts to an existing investigation, with a model-based semantic matching decision and a deterministic confidence/UUID gate; an optional post-investigation merger can consolidate separately completed incidents when their diagnosed causes match. A separate post-closure LLM pass inspects source alerts, finished agent runs, tool log evidence and operator feedback, classifies durable memories with bounded evidence grades and writes back refreshed skill/memory manifests. An optional system cron named improvement-evaluator proposes prospective runbook/memory/cron/skill changes; the operator authoritatively approves or rejects them through first-party managers.

The code deliberately separates model-discretion from Go validation, database transitions, service-level gating, budget/tool access and human authority. [README](https://github.com/akmatori/akmatori/blob/be62d926fe6d92dceb5cf12e9a95cb587433cdf1/README.md), [main startup wiring](https://github.com/akmatori/akmatori/blob/be62d926fe6d92dceb5cf12e9a95cb587433cdf1/cmd/akmatori/main.go), [agent-runner](https://github.com/akmatori/akmatori/blob/be62d926fe6d92dceb5cf12e9a95cb587433cdf1/agent-worker/src/agent-runner.ts).

## Operational model

Independent incident investigations are the S1 operating units. An agent observes telemetry, selects tool calls and proposes diagnostic/remediation steps. Correlation and optional merge regulate interference among those investigations. Separate post-incident evidence passes question the reliability of the original investigator's causal account before producing memory for later work. Adaptation proposals concern changed future diagnostic capability and remain gated by a legitimate operator. This is not a claim that the system autonomously governs its constitutional identity.

## S1 — Operations

- State: A
- Function: Investigate and diagnose infrastructure incidents using agent-selected tool interactions.
- Disturbance / variety regulated: Diverse alerts, changing telemetry, uncertain root causes, tool errors and inconsistent infrastructure responses.
- Decisive decision or feedback right: The dispatched investigation agent chooses diagnostic hypotheses, tool calls and proposed corrective steps within its tool permissions.
- Decision owner: The incident-scoped autonomous agent running through the first-party worker.
- Supporting / enforcement mechanisms: WebSocket orchestration, MCP gateway, incident database, connectors, tool allowlists, monitoring feeds and remediation proposal gates.
- Closure path: Tool outputs and incident facts update the investigation; the agent returns a diagnosis, action proposal or resolution, while operator-gated remediation is applied only after separate permission.
- Boundary reachability: Supported self-hosted standard deployment runs the first-party agent worker from incident intake; its decisions are not merely a repository example.
- Why this is / is not agent-owned: Removing the agent leaves incident capture and connector code, but not task-specific investigation, diagnosis and proposed remediation choices.
- Evidence: [README#L20-L43](https://github.com/akmatori/akmatori/blob/be62d926fe6d92dceb5cf12e9a95cb587433cdf1/README.md#L20-L43), [agent-runner.ts](https://github.com/akmatori/akmatori/blob/be62d926fe6d92dceb5cf12e9a95cb587433cdf1/agent-worker/src/agent-runner.ts), [alert_processor.go](https://github.com/akmatori/akmatori/blob/be62d926fe6d92dceb5cf12e9a95cb587433cdf1/internal/handlers/alert_processor.go).
- Basis: structural
- Confidence: high
- Caveats: External infrastructure tools and the LLM model provider remain dependencies. This does not assert unsupervised authorization of high-risk remediation.

## S2 — Coordination

- State: A
- Function: Attenuate conflict and duplication among incident-scoped S1 investigation units.
- Disturbance / variety regulated: Related alerts can spawn redundant investigations with inconsistent incident ownership or duplicate work; completed investigations can duplicate the same root-cause incident.
- Decisive decision or feedback right: A first-party invoked LLM correlator decides whether a new alert belongs with a recent incident; supported opt-in merger separately chooses whether two already investigated incidents share a root cause.
- Decision owner: LLM-based correlation/merge agent in the shipped service; code checks confidence thresholds, existing UUIDs, candidate status and admissible state transitions.
- Supporting / enforcement mechanisms: Fingerprint fast-path, candidate incident selection, correlationThreshold, database relationships, status gates, incident attach/reparent transitions.
- Closure path: A confident correlation attaches the new alert to the selected incident instead of creating another standalone investigation; opt-in post-investigation merge reparents alerts and retains a surviving incident whose later memory extraction reads the incident family.
- Boundary reachability: AlertCorrelator is connected to normal alert intake, with enabled-by-default configuration; the additional incident merger is constructed by the normal server and activated by an explicit supported operator setting.
- Why this is / is not agent-owned: Deterministic fingerprint dedup alone is not the proof. Removing the one-shot model eliminates semantic judgment over distinct alert evidence and diagnosed root causes, while fixed gates only enforce admissibility.
- Distinct S1 units: Independently spawned incident investigation agents, each with own incident scope and evidence record; the optional merger handles already-investigated separate incidents.
- Inter-S1 disturbance: Redundant or overlapping investigations for one underlying failure can compete for incident identity and produce contradictory downstream work or memory.
- Attenuating coordination relation: Semantic incoming-alert-to-live-incident correlation plus optional post-investigation cross-incident merging.
- Feedback into subsequent S1 behaviour: New alerts follow an existing investigation context, while merged incidents stop being separate operational histories and are included in survivor memory/evidence processing.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The coordination decision resolves evidenced overlap in independent incident work instead of merely assigning a job to a worker or relaying a message.
- Evidence: [alert_correlator.go#L134-L247](https://github.com/akmatori/akmatori/blob/be62d926fe6d92dceb5cf12e9a95cb587433cdf1/internal/services/alert_correlator.go#L134-L247), [alert_processor.go#L108-L158](https://github.com/akmatori/akmatori/blob/be62d926fe6d92dceb5cf12e9a95cb587433cdf1/internal/handlers/alert_processor.go#L108-L158), [incident_merger.go](https://github.com/akmatori/akmatori/blob/be62d926fe6d92dceb5cf12e9a95cb587433cdf1/internal/services/incident_merger.go), [incident_merger_test.go#L67-L117](https://github.com/akmatori/akmatori/blob/be62d926fe6d92dceb5cf12e9a95cb587433cdf1/internal/services/incident_merger_test.go#L67-L117), [models_settings.go#L250-L353](https://github.com/akmatori/akmatori/blob/be62d926fe6d92dceb5cf12e9a95cb587433cdf1/internal/database/models_settings.go#L250-L353).
- Basis: structural
- Confidence: medium
- Caveats: Default correlation and optional post-investigation merge are separate modes. Merge is disabled by default; neither it nor a semantic correlation decision proves the effectiveness of the resulting incident diagnosis in production.

## S3 — Inside-and-now control

- State: —
- Function: Regulate current whole-system incident fleet commitments, budgets and interventions on behalf of multiple operational investigations.
- Disturbance / variety regulated: Concurrent incidents, operator response capacity, pending remediations and incident lifecycle failures could demand whole-system present control.
- Decisive decision or feedback right: No first-party whole-system S3 decision path, autonomous or parent-governed, was established from the inspected incident and approval services.
- Decision owner: Operators decide isolated remediation approvals, while runtime schedulers and status services enforce local rules; no separate agent-owned whole-fleet S3 decision right evidenced.
- Supporting / enforcement mechanisms: Incident state transitions, approval queue, worker orchestration, monitor sweeps, event ingestion, cron schedules and tool permission gates.
- Closure path: Local incident interventions change local state, but no evidenced first-party choice reallocates whole-fleet current commitments on a shared system view.
- Why this is / is not agent-owned: Dispatch, scheduling and approval of a single risky action are not the organizational whole-system control right described by S3.
- Whole-system current view: Operator dashboards show incidents and settings, but an integrated first-party decision/return path over multiple fleet commitments was not identified.
- Current-control decision scope: No evidenced actor renegotiates priorities or resources for the current incident-response organization as a whole.
- Evidence: [incident_service.go](https://github.com/akmatori/akmatori/blob/be62d926fe6d92dceb5cf12e9a95cb587433cdf1/internal/services/incident_service.go), [proposal_service.go](https://github.com/akmatori/akmatori/blob/be62d926fe6d92dceb5cf12e9a95cb587433cdf1/internal/services/proposal_service.go), [agent orchestrator](https://github.com/akmatori/akmatori/blob/be62d926fe6d92dceb5cf12e9a95cb587433cdf1/agent-worker/src/orchestrator.ts).
- Basis: structural
- Confidence: medium
- Caveats: An external SRE incident commander may perform S3 in a larger organization; this is not a shipped first-party parent-return mode merely because an operator dashboard is present.

### Absence scope

- Surfaces inspected: Incident services and lifecycle, alert correlation, agent worker orchestration, remediation proposal approval, cron and monitor sweeps, operator API.
- Plausible first-party paths checked: Incident queue, reparenting, approval decisions, scheduling, alert coalescing, operator dashboard intervention and tool-access rules.
- Why no material first-party path remains: The inspected paths regulate individual S1 cases or inter-S1 correlation (S2), and enforce fixed current constraints without an owner closing S3-wide resource/commitment discretion.

## S3* — Complementary audit

- State: A
- Function: Provide a complementary post-incident evidentiary check of operational diagnosis and claimed resolution, distinct from routine investigator self-report.
- Disturbance / variety regulated: An investigator may present an unsupported causal claim, incorrect timeline or false recovery assertion as a durable fact for the next incident.
- Decisive decision or feedback right: A separate post-closure LLM extraction pass compares operational facts, original alerts, tool outputs, timestamps and agent claims, then selects which durable observed facts and feedback should become memory.
- Decision owner: The independently invoked post-incident extraction model makes the evidence selection/judgment; Go service validates schema and assigns evidence grades, always leaving causal assertions unverified.
- Supporting / enforcement mechanisms: On-close extraction queue and wake-up, independent one-shot LLM caller, input redaction, evidence-grade restrictions, transactional memory writes, SKILL.md manifest refresh.
- Closure path: Separate extraction generates graded memories, writes them after closure with stale-claim guards, and refreshes manifests read by future incident agents, changing subsequent investigation context.
- Boundary reachability: Default server startup wires NewIncidentMemoryExtractor, close-path kickers and the extractor Run loop; this is an active first-party path, not a test or blog vignette.
- Why this is / is not agent-owned: Removing the separate extraction model leaves the original investigation self-report and fixed storage rules but not an independent semantic account of what was actually observed.
- Claim being audited: The original agent's root-cause story, resolved status and potential reusable observations are grounded in incident reality.
- Ordinary reporting path: The incident investigator's final response and run transcript.
- Complementary access path: Original alert text, incident timeline and close reason, finished run logs/tool outputs, operator feedback and related incident family evidence.
- Independence boundary: A separate post-incident model pass receives original artifacts in addition to the producing agent's answer; it distinguishes self-report from observed recovery, and code prevents it from declaring causal claims verified.
- Who acts on findings: MemoryService writes the graded output, then SkillService refreshes future agent context. This is a retrospective corrective feedback channel, not a remediation-veto gate.
- Evidence: [extraction prompt](https://github.com/akmatori/akmatori/blob/be62d926fe6d92dceb5cf12e9a95cb587433cdf1/internal/services/incident_memory_extraction_prompt.go), [evidence apply](https://github.com/akmatori/akmatori/blob/be62d926fe6d92dceb5cf12e9a95cb587433cdf1/internal/services/memory_extraction_apply.go), [extractor process](https://github.com/akmatori/akmatori/blob/be62d926fe6d92dceb5cf12e9a95cb587433cdf1/internal/services/incident_memory_extractor.go#L224-L277), [runtime wiring](https://github.com/akmatori/akmatori/blob/be62d926fe6d92dceb5cf12e9a95cb587433cdf1/cmd/akmatori/main.go#L399-L408), [worker start](https://github.com/akmatori/akmatori/blob/be62d926fe6d92dceb5cf12e9a95cb587433cdf1/cmd/akmatori/main.go#L538-L544).
- Basis: structural
- Confidence: medium
- Caveats: Independence is claim-relative; factual labeling and separate model reading are not a guarantee of true ground truth. No runtime test of future agent reliance on the graded memory was run for this assessment.

## S4 — Outside-and-then intelligence

- State: P
- Function: Analyze environmental incident patterns and operator feedback to propose future adaptations of response capability.
- Disturbance / variety regulated: Repeated failed/slow investigations, changed infrastructure symptoms, missing runbooks and ineffective skill instructions threaten future diagnostic fitness.
- Decisive decision or feedback right: Opt-in improvement-evaluator agent proposes runbook/memory/cron/skill changes; a legitimate operator approves, edits or rejects the adaptation and owns the final decision.
- Decision owner: Operator parent for the decisive adaptation authorization; the evaluator is a first-party option generator, not the owner of final strategy.
- Supporting / enforcement mechanisms: Seeded improvement-evaluator cron, incident/feedback retrieval tools, proposal gateway, staleness checks, review UI and first-party runbook/memory/cron/skill managers.
- Closure path: Operator-approved proposal is applied through managers and changes subsequent runs, runbooks, memory or permissible skills; rejected proposal leaves operating capability unchanged.
- Boundary reachability: First-party startup seeds the evaluator in a disabled-by-default but operator-enableable mode, and the existing proposal service can apply an approved proposed asset change.
- Why this is / is not agent-owned: Agent generates future options, but their adoption is reserved for the legitimate operator and remains unavailable without that parent decision.
- External distinction: Real incident histories, monitoring failures, different infrastructure conditions and operator feedback from actual work.
- Future / prospective distinction: Future response correctness, investigation latency and robustness of next incidents rather than repair of only the current alert.
- Adaptation option generated: New/updated runbook, memory, recurring cron task or non-system skill prompt.
- Path back into current capability / S3: Proposal review and apply update operational assets for later investigations; the operator closes the adaptation against currently authorized response capability rather than the software autonomously rewriting its mandate.
- Evidence: [improvement evaluator seed](https://github.com/akmatori/akmatori/blob/be62d926fe6d92dceb5cf12e9a95cb587433cdf1/internal/database/db.go#L1252-L1337), [proposal service approval](https://github.com/akmatori/akmatori/blob/be62d926fe6d92dceb5cf12e9a95cb587433cdf1/internal/services/proposal_service.go#L204-L241), [proposal application](https://github.com/akmatori/akmatori/blob/be62d926fe6d92dceb5cf12e9a95cb587433cdf1/internal/services/proposal_service.go#L351-L480), [proposal first-party tool](https://github.com/akmatori/akmatori/blob/be62d926fe6d92dceb5cf12e9a95cb587433cdf1/mcp-gateway/internal/tools/proposals/proposals.go).
- Basis: structural
- Confidence: medium
- Caveats: This is an opt-in mode: seed configuration is Enabled=false and tools_enabled=false. The assessment does not claim autonomous A, regular self-improvement on every installation, or a successful observed human approval in a production deployment.

## S5 — Policy and identity

- State: —
- Function: Resolve ultimate identity/policy disputes and authoritatively return those decisions into subsequent operation.
- Disturbance / variety regulated: Proposed changes to enduring mission, ultimate acceptable-remediation bounds or constitution of the agent organization could create identity-level conflict.
- Decisive decision or feedback right: No shipped identity-level escalation and authoritative return was established in the operating boundary.
- Decision owner: Operators and maintainers set policy externally; routine approval of an action and protected system-skill settings are not evidence of a first-party S5 owner/closure loop.
- Supporting / enforcement mechanisms: Tool authorization, proposal approval gates, administrator settings, system-skill protection and human-reviewed remediation.
- Closure path: Ordinary approvals apply or reject individual operations and S4 improvement proposals, not constitution-level changes that are returned as new system identity.
- Why this is / is not agent-owned: Agent and operator decisions are limited to tasks and permitted capability changes; an ultimate-policy decision path is not shipped.
- Identity / ultimate-policy issue: Who may change the organization-level purpose, hard risk boundaries or constitutional governance rules of the self-hosted response organization.
- Ultimate authority in each claimed mode: No first-party positive S5 mode; external human/maintainer ultimate authority cannot be borrowed without a function-specific returned decision path.
- Return-to-operation path: No traced identity-level escalation → legitimate parent judgment → revised policy governing the later operational runtime.
- Evidence: [proposal_service.go](https://github.com/akmatori/akmatori/blob/be62d926fe6d92dceb5cf12e9a95cb587433cdf1/internal/services/proposal_service.go), [proposals.go](https://github.com/akmatori/akmatori/blob/be62d926fe6d92dceb5cf12e9a95cb587433cdf1/mcp-gateway/internal/tools/proposals/proposals.go), [models_settings.go](https://github.com/akmatori/akmatori/blob/be62d926fe6d92dceb5cf12e9a95cb587433cdf1/internal/database/models_settings.go).
- Basis: structural
- Confidence: medium
- Caveats: Human retention of strategic authority is not a defect, but an ordinary approval or admin setting alone does not satisfy the Profile S5 witness.

### Absence scope

- Surfaces inspected: Proposal kinds and application restrictions, operator approval handlers, runtime/tool authorization, system skill protection and configuration settings.
- Plausible first-party paths checked: Remediation proposals, improvement proposal approvals, cron/skill changes, admin settings and change of protected system skills.
- Why no material first-party path remains: These are ordinary operational authorizations or bounded future-capability adaptations, without an established identity-level proposal and legitimate ultimate authority return path.

## Distributed OSS parent arrangement

The distributed upstream code contributors/maintainers are not treated as part of the deployed self-hosted incident-response organization. No project-wide distributed parent mode is inferred from their repository access.

## Self-hosted and non-human modes

The self-hosted operator controls deployments, credentials and approvals. S4=P is supported as an explicit optional parent-governed improvement mode; S3=P and S5=P are not inferred from operator presence, configuration or approval gates alone. Agent autonomy in S1, inter-incident coordination and post-incident audit does not imply autonomous ultimate policy.

## Recursion

The selected recursion is one Akmatori deployment, with incident investigations as operational units. The incident merger coordinates those units; the post-incident extractor provides complementary access to their claims; the prospective evaluator serves the larger response capability subject to parent authority. No inference is made that the software developer's company shares this recursion.

## Variety and escalation

New alerts may attach to ongoing investigations; uncertain/low-confidence correlation spawns a separate investigation instead of assuming a match. Risky remediation and future capability proposals escalate to an operator, with state and evidence returned to subsequent operation. An incident status or alert alone is not a separate algedonic VSM function.

## Evidence gaps

- The source supports first-party closure paths but this assessment does not run production incident simulation, remote infrastructure tools or LLM provider calls.
- S2's semantic coordination depends on the distinction between preventing overlapping investigations and general event routing; the opt-in merger supplies an additional witness after two independently investigated incidents exist.
- S3* is a retrospective knowledge/evidence correction mechanism, not a safety certification and not a pre-remediation independent veto.
- S4=P is an operator-enabled mode and must not be described as continuously running by default; the source seeds it disabled.

---
harness_id: tetriz-harness
project_name: Tetriz Harness
repository: https://github.com/tetriz-ai/tetriz-harness
review_ref: 2351654be1cb1a042387cad227a7f039d4260664
reviewed_at: 2026-11-18
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: P
autonomy_s5: P
---

# Tetriz Harness

## Review boundary

- System in focus: One deployed Tetriz harness-improvement and artifact-distribution organization, comprising its recommended-artifact engine and first-party control-plane server/agents, with a legitimate operator administering team placements.
- Purpose and identity: Inspect existing coding-agent harness instructions, propose improvements supported by coding signals, and distribute operator-selected artifact changes to identified developers or teams.
- Relevant environment: Repository configuration, development-session and review signals supplied by an organization, security findings, developer machine installations, central targeting changes and observed delivery state.
- Standard-distribution boundary: The Go `recommendations/` engine and optional bundled `tetriz-py` model service; `server/`, `agent/`, the published admin and agent APIs, reference host and configuration. The organization must supply data and model credentials for the DERIVED mode.
- Credited operating / distribution surfaces: DERIVED model-selected artifact proposals with durable task records; DETECTED scan/fix suggestions; administered artifact upsert/target changes and clients that reconcile local files and return installation reports.
- Adjacent first-party surfaces excluded from ownership: Contributor CI/test programs, sample and demo repositories, Product Hunt/marketing site, separate Agent Desk discovery and Session Intelligence upstream producers, third-party coding-agent runtime loops and external Gemini inference provider. The examples and mock rollout UI are not treated as a deployed production actor.
- First-party operating / deployment modes considered: On-disk DETECTED-only scan; configured organization's DERIVED model path; operator-approved control-plane artifact rollout and ongoing per-person observation; deployment pause/resume.
- Recursion level: One organization/team's installed harness-artifact rollout, not the full coding-work organization operated by downstream Claude Code/Codex/Cursor.
- Reviewed revision: `tetriz-ai/tetriz-harness@2351654be1cb1a042387cad227a7f039d4260664`.
- Observation date: 2026-11-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The repository ships Go recommendation components with both deterministic DETECTED checks and a configured DERIVED model leg. `Engine.Run` assembles project-specific evidence, calls `llmClient.DeriveArtifacts`, then grades and persists proposed artifacts; the separate `HarnessImproveEngine.Run` combines committed-file checks, optional LLM intent classification and grounded draft fixes. These are artifact-recommendation operations, not an installed controller of developers' external coding agents. The control plane is a Go server with administrator artifact/target operations, installation-state comparison and enforcement pause/resume; its Node client reconciles desired artifacts onto installed tools and reports state. The operator approves the eventual publication and target audience. Signal ingestion for DERIVED requires external organization-specific sources; no fresh checkout automatically creates those inputs. Sources: [recommendations architecture](https://github.com/tetriz-ai/tetriz-harness/blob/2351654be1cb1a042387cad227a7f039d4260664/recommendations/README.md), [derivation engine](https://github.com/tetriz-ai/tetriz-harness/blob/2351654be1cb1a042387cad227a7f039d4260664/recommendations/engine.go), [DETECTED engine](https://github.com/tetriz-ai/tetriz-harness/blob/2351654be1cb1a042387cad227a7f039d4260664/recommendations/harness_improve_engine.go), [admin service](https://github.com/tetriz-ai/tetriz-harness/blob/2351654be1cb1a042387cad227a7f039d4260664/server/service/admin.go), [install reconciler](https://github.com/tetriz-ai/tetriz-harness/blob/2351654be1cb1a042387cad227a7f039d4260664/agent/src/engine/converge.ts), [README deployment boundary](https://github.com/tetriz-ai/tetriz-harness/blob/2351654be1cb1a042387cad227a7f039d4260664/README.md).

## Operational model

S1 here is the first-party production of evidence-backed harness findings and model-selected artifact candidates. The operator-governed deployment service is the machinery by which those candidates may influence the team's installed harness; an external coding agent's implementation decisions are *not* part of Tetriz's S1. A team administrator has a cross-person current installation view and can redirect active artifact targeting; the same administrator makes prospective harness-adaptation and binding organization rollout-policy choices. No automatically adjudicating independent audit owner or S2-specific agent coordination is established by the included scanner, target set and collision guards.

## S1 — Operations

- State: A
- Function: Produce candidate harness improvements from project signals, and run first-party scanning/finding work.
- Disturbance / variety regulated: Changed source/config, missing/contradictory harness rules, review and session evidence, security flags.
- Decisive decision or feedback right: Within configured DERIVED operation, select proposed rule/skill/hook contents using the model response and persist evaluated proposals; DETECTED is a separate deterministic path.
- Decision owner: Configured agentic DERIVED producer, not the administrator who later approves rollout.
- Supporting / enforcement mechanisms: Repository context aggregator, `tetriz-py` LLM adapter, Go quality gate, durable task and artifact storage.
- Closure path: Project signal context → model-generated artifact candidates → source-grounded graded results → persisted proposed artifacts shown for review.
- Boundary reachability: Released CLI engine wiring supports the DERIVED mode with supplied organization's signal tables and configured model service; this is not mere documentation or an external coding-agent's decision.
- Why this is / is not agent-owned: A model-backed producer chooses substantive candidate content rather than only implementing a human-picked artifact; the deterministic scanner alone would not justify this A.
- Evidence: [DERIVED engine](https://github.com/tetriz-ai/tetriz-harness/blob/2351654be1cb1a042387cad227a7f039d4260664/recommendations/engine.go), [source-mode prerequisites](https://github.com/tetriz-ai/tetriz-harness/blob/2351654be1cb1a042387cad227a7f039d4260664/recommendations/README.md), [CLI wiring](https://github.com/tetriz-ai/tetriz-harness/blob/2351654be1cb1a042387cad227a7f039d4260664/recommendations/cmd/recommendations/main.go), [DERIVED tests](https://github.com/tetriz-ai/tetriz-harness/blob/2351654be1cb1a042387cad227a7f039d4260664/recommendations/engine_test.go).
- Basis: structural
- Confidence: moderate
- Caveats: This is bounded to recommendation production, not automatic adoption or external coding changes; model/service credentials and ingested project signals are prerequisites.


## S2 — Coordination

- State: —
- Function: Attenuate interference among distinct S1 operating units.
- Disturbance / variety regulated: Possible competing team members and duplicated artifact placements, but no verified S2-specific operating actor.
- Decisive decision or feedback right: No demonstrated choice that regulates a concrete observed clash among distinct first-party S1 recommendation producers.
- Decision owner: No evidenced coordinating agent or parent S2 owner in the assessed distribution.
- Supporting / enforcement mechanisms: Audience filtering, placement validation, client collision protection, recommendation dedup and run admission.
- Closure path: Static targeting and single-run guards prevent technical conflicts but do not constitute discretionary inter-S1 feedback regulation.
- Boundary reachability: The control-plane server and client are first party; their per-person placement control is real, but no distinct first-party S1 coordination loop is established.
- Why this is / is not agent-owned: Individual targeting, sequencing, idempotency and file-path safeguards are not by themselves distinct S1 interaction management.
- Evidence: [target API](https://github.com/tetriz-ai/tetriz-harness/blob/2351654be1cb1a042387cad227a7f039d4260664/server/service/admin.go), [client collision checks](https://github.com/tetriz-ai/tetriz-harness/blob/2351654be1cb1a042387cad227a7f039d4260664/agent/src/engine/converge.ts), [run admission](https://github.com/tetriz-ai/tetriz-harness/blob/2351654be1cb1a042387cad227a7f039d4260664/recommendations/dao/task_execution_repo.go).
- Basis: structural
- Confidence: moderate
- Caveats: A downstream enterprise could use the targeting interface to coordinate developers, but that organization-level S2 actor is not supplied as Tetriz S2.


### Absence scope

- Surfaces inspected: Recommendation/derivation flow, per-project and organization scans, server audience targeting, installation client, tests and supported operator modes.
- Plausible first-party paths checked: Search for distinct first-party S1 producers with a shared active-resource conflict, conflict-specific regulator and later S1 behaviour changed by its feedback.
- Why no material first-party path remains: No source-backed material S2-specific decision/feedback loop, rather than routing, dedup and deployment configuration, was reconstructed within this boundary.


## S3 — Inside-and-now control

- State: P
- Function: Regulate currently installed organization harness obligations and deliveries across targeted engineers.
- Disturbance / variety regulated: Missing/stale installations, wrong target population, changed present deployment conditions and pending or paused enforcement.
- Decisive decision or feedback right: Inspect desired-versus-reported artifact installation state; approve/reassign/remove the target audience or pause/resume current enforcement.
- Decision owner: Authorized team/organization administrator in the supported operator mode, not the model-selected DERIVED generator.
- Supporting / enforcement mechanisms: Admin `ListArtifacts`, `GetEnforcementStatus`, `SetTargets`, `PauseEnforcement`, `ResumeEnforcement`, client sync and state reporting.
- Closure path: Reported team installation state → administrator's current target/enforcement decision → changed desired placements → next client reconciliation and reported installation status.
- Boundary reachability: Admin API and reference host are packaged; clients report state back to the central service. This is one administrator-governed organizational installation cell, not a read-only dashboard.
- Why this is / is not agent-owned: The administrator owns allocation/intervention among current team deployments; deterministic reconciler and status grader execute/report that decision without making it autonomously.
- Evidence: [admin methods](https://github.com/tetriz-ai/tetriz-harness/blob/2351654be1cb1a042387cad227a7f039d4260664/server/service/admin.go), [agent reporting](https://github.com/tetriz-ai/tetriz-harness/blob/2351654be1cb1a042387cad227a7f039d4260664/server/service/agent.go), [rollout procedure](https://github.com/tetriz-ai/tetriz-harness/blob/2351654be1cb1a042387cad227a7f039d4260664/README.md), [per-person status grader](https://github.com/tetriz-ai/tetriz-harness/blob/2351654be1cb1a042387cad227a7f039d4260664/server/service/grade.go).
- Basis: structural
- Confidence: moderate
- Caveats: Current control is limited to the shipped harness-artifact deployment system, not all engineering work or project priorities.
- Whole-system current view: `ListArtifacts` and `GetEnforcementStatus` expose current desired placements and reported per-engineer installation results across this declared rollout organization.
- Current-control decision scope: The administrator can change currently targeted engineers/teams, remove placements, and pause or resume enforcement; clients subsequently consume changed desired state.


## S3* — Complementary audit

- State: —
- Function: Audit an S3 current-control claim using an independently owned complementary path.
- Disturbance / variety regulated: Potential mismatch between promised and actual installed rules, and unsafe generated recommendation content.
- Decisive decision or feedback right: No demonstrated separately deciding audit actor with independent access plus returned corrective finding, distinct from normal Tetriz delivery telemetry.
- Decision owner: No independent S3* auditor established.
- Supporting / enforcement mechanisms: Quality gates, grounded paths, client installation hashes, server status reports and ordinary operator inspections.
- Closure path: Detection/telemetry feed normal delivery/recommendation controls; there is no proved independent audit-to-correction decision path.
- Boundary reachability: These mechanisms ship, but client-reported state is ordinary reporting and Go quality gates sit inside the same primary producer.
- Why this is / is not agent-owned: Static validation or comparing expected content against the same reporting client does not alone establish a complementary, independently controlled audit.
- Evidence: [quality gate](https://github.com/tetriz-ai/tetriz-harness/blob/2351654be1cb1a042387cad227a7f039d4260664/recommendations/gate.go), [client reporting](https://github.com/tetriz-ai/tetriz-harness/blob/2351654be1cb1a042387cad227a7f039d4260664/agent/src/agent.ts), [state grader](https://github.com/tetriz-ai/tetriz-harness/blob/2351654be1cb1a042387cad227a7f039d4260664/server/service/grade.go).
- Basis: structural
- Confidence: moderate
- Caveats: A separate human/source audit could be composed later; do not credit a hypothetical independent reviewer.


### Absence scope

- Surfaces inspected: DERIVED grading and DETECTED findings, server status grading, client state reports, documented rollout tests.
- Plausible first-party paths checked: Check for a separate active audit access channel, independent adjudicator and returned corrective feedback against organizational operation.
- Why no material first-party path remains: Shipped checks appear in producer/delivery/telemetry paths; an independently owned complementary audit actor and decision loop were not established.


## S4 — Outside-and-then intelligence

- State: P
- Function: Adapt future harness capability using session/review/security signals and controlled deployment experiments.
- Disturbance / variety regulated: Prospective mismatches between current instructions and shifting coding practices, observed quality signals, emergent security problems.
- Decisive decision or feedback right: Review the model-suggested/method-generated artifact changes, choose which candidate to adopt, target an experiment audience, measure outcomes in the operator's analysis system, then decide to expand or withdraw.
- Decision owner: Organization's legitimate human harness administrator/owner; model DERIVED proposer provides options, not final adaptation deployment choice.
- Supporting / enforcement mechanisms: Session/VCS/security signal ingestion, DERIVED recommendations, `UpsertArtifact`/`SetTargets`, documented test/control rollout and enforcement status.
- Closure path: External/lagged coding signals → prospective recommendation → operator selection → updated artifact/targets → developer clients install new harness configuration for later work; subsequent observation can inform another selection.
- Boundary reachability: The repository supplies an explicit supported operator mode and working artifact/target return path; signal analysis and comparative outcome measurement are organization supplied and not bundled fully autonomously.
- Why this is / is not agent-owned: A human parent selects and applies the future capability change; model output alone is not a self-owned autonomous S4 loop, and external signal ingestion is a stated prerequisite.
- Evidence: [DERIVED semantics](https://github.com/tetriz-ai/tetriz-harness/blob/2351654be1cb1a042387cad227a7f039d4260664/recommendations/README.md), [rollout test/control procedure](https://github.com/tetriz-ai/tetriz-harness/blob/2351654be1cb1a042387cad227a7f039d4260664/README.md), [admin upsert and targets](https://github.com/tetriz-ai/tetriz-harness/blob/2351654be1cb1a042387cad227a7f039d4260664/server/service/admin.go).
- Basis: structural
- Confidence: moderate
- Caveats: Test/control experiment measurement and outcome comparison are explicitly external; do not credit automatic hypothesis selection, experiment judgement or S4=A.
- External distinction: Organization-supplied session analyses, code review themes, security incidents and external developer/tooling changes motivate candidate artifacts.
- Future / prospective distinction: Recommendations change instructions/rules/skills for future development sessions, not only recover failed present delivery.
- Adaptation option generated: DERIVED proposes net-new rules, skills and hooks; DETECTED suggests repairs; the operator decides to adopt, test or withdraw.
- Path back into current capability / S3: Operator-approved `UpsertArtifact`/`SetTargets` changes desired installed artifacts; subsequent `harness-agent` sync and reporting feed current deployment control.


## S5 — Policy and identity

- State: P
- Function: Define and retain the organization's ultimate harness configuration and enforcement mandate.
- Disturbance / variety regulated: Competing preferred rules, permission scope, adoption limits and risk tolerance across teams and tools.
- Decisive decision or feedback right: Decide what artifacts the organization will impose on which people, whether hooks are allowed, and when enforcement is paused or resumed.
- Decision owner: Authorized organization/team administrator, beyond a per-artifact click approver.
- Supporting / enforcement mechanisms: Central admin API and configured hook permission, artifact body/target store, adoption gate, per-client reconciliation.
- Closure path: Enduring human policy for allowed artifacts/audiences → stored definition/target and enforcement mode → subsequent clients enforce or cease enforcing policy.
- Boundary reachability: Operator-governed control-plane deployment is a first-party supported mode; persistent configuration and admin commands give the policy a durable return path.
- Why this is / is not agent-owned: Human parent, not model recommender or deterministic enforcement engine, owns organization-level identity/policy. There is no autonomous S5 decision owner.
- Evidence: [admin policy/targets and pause](https://github.com/tetriz-ai/tetriz-harness/blob/2351654be1cb1a042387cad227a7f039d4260664/server/service/admin.go), [control-plane description](https://github.com/tetriz-ai/tetriz-harness/blob/2351654be1cb1a042387cad227a7f039d4260664/docs/control-plane.md), [install reconciler](https://github.com/tetriz-ai/tetriz-harness/blob/2351654be1cb1a042387cad227a7f039d4260664/agent/src/engine/converge.ts).
- Basis: structural
- Confidence: moderate
- Caveats: This S5=P is limited to the declared artifact-distribution organization's harness-policy identity, not the downstream company's overall ultimate strategy.
- Identity / ultimate-policy issue: Which versioned rules, skills, hooks and permissions constitute the legitimate shared harness for this team's installed tools.
- Ultimate authority in each claimed mode: Human organizational administrator chooses and records lasting artifact target and enforcement policy; no alternative autonomous ultimate-policy mode demonstrated.
- Return-to-operation path: Admin writes artifact/target/pause decisions; server distributes desired state; client reconciles and reports later installation.


## Distributed OSS parent arrangement

Open-source contributors do not jointly operate a single default runtime. The parent modes above are supported for **one explicitly administered deployment** and are not inferred from project maintainers, CI, or independent forks. No ecosystem-level parent authority is claimed.

## Self-hosted and non-human modes

In deterministic DETECTED-only operation, no A claim is made from scanning alone. In configured signal-ingested DERIVED operation, a first-party model produces candidate artifacts (S1=A), but it does not automatically authorize deployment. A supported human-administered control-plane mode closes present control, future adaptation and ultimate rollout-policy selection (S3=P, S4=P, S5=P). A fully autonomous non-human enterprise exercising those three decisions is not evidenced.

## Recursion

The evaluated recursion is one team organization's harness-artifact selection and delivery system. Individual developers and their external IDE coding agents are environmental recipients, not silently included independent VSM functions. Downstream enterprise developer management remains outside this recursion.

## Variety and escalation

The scan/derive model attenuates variety in proposed harness artifacts; per-team targeting filters deployment reach, while installation reports help the administrator correct delivery. Source-grounding and enable/disable gates provide operational safeguards but cannot replace a missing independent S3* owner or independent S2 coordination. When model derivation lacks sufficient data or fails, the engine returns skipped/failed/no-visible outcomes rather than publishing a fictitious adopted change.

## Evidence gaps

No live external model invocation, tenant data ingestion or experimental rollout was performed for this source review. The packed mode is structurally reachable, but DERIVED requires separate organizational signals and provider key. S2 inter-unit conflict and independent S3* audit were not established from first-party packaged code; S4 outcome measurement is documented as external. Proposed grades are revision-relative, not a safety/performance certification.

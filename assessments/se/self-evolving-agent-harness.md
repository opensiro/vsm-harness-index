---
harness_id: self-evolving-agent-harness
project_name: Self-Evolving Agent Harness
repository: https://github.com/tylerelyt/self-evolving-agent-harness
review_ref: 5e2663e7b1f9679f1cb122f244d492ee28b6ccbe
reviewed_at: 2026-11-18
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: A
autonomy_s5: —
---

# Self-Evolving Agent Harness

## Review boundary

- System in focus: The repository's shipped on-call capstone, a two-instance Hermes incident investigation and SkillClaw learning harness, in its explicitly available live-model configuration.
- Purpose and identity: Patrol services, investigate incident evidence, hand off and verify recovery, then improve and redeploy a shared incident-response Skill from outcomes.
- Relevant environment: Two local HTTP service environments, human on-call operator, configured external model endpoint, local incident/version state, and separately packaged Hermes and SkillClaw dependencies.
- Standard-distribution boundary: Installed capstone patrol/learning service, incident and workbench control paths, built-in Skills and replay evaluator. Online provider is a configured external intelligence service rather than an OpenSiro first-party agent.
- Credited operating / distribution surfaces: `workshop/capstone/patrol` Hermes tools and session loop, `oncall_service.py`, `self_improvement_agent.py`, `workbench.py`, `workbench_rollback.py`, `patrol/skillclaw_evolve.py`, and `patrol/fleet_eval.py` in the documented supported live-model mode.
- Adjacent first-party surfaces excluded from ownership: Curriculum's incremental exercises, mock-model demo claims, manually injected faults, benchmark/enterprise scoring, GEPA and external optional integrations, repository CI and contributor governance. Their mechanisms may validate wiring but do not donate agent decisions to a scripted offline run.
- First-party operating / deployment modes considered: Offline scripted `make demo`/`make ui`, optional live-model on-call service, multi-instance patrol + learner, and workbench-supervised recovery/rollback.
- Recursion level: One on-call service managing two incident-patrol units and one shared learning/Skill distribution loop.
- Reviewed revision: `5e2663e7b1f9679f1cb122f244d492ee28b6ccbe`.
- Observation date: 2026-11-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

Each Hermes unit runs a provider-backed session whose tools expose the patrol Skill, current service metrics, historical measurements, and incident probes. An alert is steered into the same turn; the model's report is saved with source tool receipts. The native forked investigation feeds an operator page with a recovery recommendation. The operator's workbench validates the specific source report, incident scope and environment generation before accepting an explicitly confirmed local recovery; two later independent healthy checkpoints close the incident. Two archived first-party incident sessions feed a SkillClaw proposal; fixed native replay compares the baseline and candidate on the same cases; a passing revision is content-addressed and published to both agents, with subsequent adoption verification or rollback. The documented default demo substitutes a scripted model, not genuine discretionary LLM judgment. [workshop/capstone/README.md](https://github.com/tylerelyt/self-evolving-agent-harness/blob/5e2663e7b1f9679f1cb122f244d492ee28b6ccbe/workshop/capstone/README.md); [workshop/capstone/RUNNING.md](https://github.com/tylerelyt/self-evolving-agent-harness/blob/5e2663e7b1f9679f1cb122f244d492ee28b6ccbe/workshop/capstone/RUNNING.md#L72-L88); [workshop/capstone/patrol/patrol.py](https://github.com/tylerelyt/self-evolving-agent-harness/blob/5e2663e7b1f9679f1cb122f244d492ee28b6ccbe/workshop/capstone/patrol/patrol.py#L268-L412); [workshop/capstone/oncall_service.py](https://github.com/tylerelyt/self-evolving-agent-harness/blob/5e2663e7b1f9679f1cb122f244d492ee28b6ccbe/workshop/capstone/oncall_service.py#L254-L335).

## Operational model

There are two distinct Hermes service-patrol S1 units. Each may inspect current HTTP observations, use recent records, and generate an incident report in its own session; the source receipts and the model response are cross-checked. The shared learner observes outcomes from both, but configured replay/release checks enforce whether a model-proposed Skill is deployed. The workbench operator owns risk-bearing recovery/rollback approval. An HTTP fixture, fixed scripted model or evaluator alone does not establish agent-owned control. [workshop/capstone/patrol/patrol.py](https://github.com/tylerelyt/self-evolving-agent-harness/blob/5e2663e7b1f9679f1cb122f244d492ee28b6ccbe/workshop/capstone/patrol/patrol.py#L268-L412); [workshop/capstone/workbench.py](https://github.com/tylerelyt/self-evolving-agent-harness/blob/5e2663e7b1f9679f1cb122f244d492ee28b6ccbe/workshop/capstone/workbench.py#L761-L849); [workshop/capstone/patrol/fleet_eval.py](https://github.com/tylerelyt/self-evolving-agent-harness/blob/5e2663e7b1f9679f1cb122f244d492ee28b6ccbe/workshop/capstone/patrol/fleet_eval.py#L148-L203).

## S1 — Operations

- State: A
- Function: Carry out on-call patrol and incident investigation in the live provider-backed mode.
- Disturbance / variety regulated: Changing service health, alert timings, incident evidence and the relevance of historical observations.
- Decisive decision or feedback right: The Hermes model chooses the next available investigation tool calls and writes a report after reading a Skill and current HTTP evidence; an alert is offered during the running session.
- Decision owner: The configured model for each of the two patrol units, not the HTTP service fixture or deterministic alert validator.
- Supporting / enforcement mechanisms: `run_turn`, Skill view, real snapshot and probe tools, steer delivery, persisted session database, result/receipt consistency checks.
- Closure path: Model tool calls produce observations and incident reports which persist into inspection/incident records, paging and further patrol/recovery actions.
- Boundary reachability: `inspect_service` wires the model session, first-party tools and persisted report in the supported on-call runtime; `--live` enables the genuine model mode.
- Why this is / is not agent-owned: With the model removed, the fixed scripted offline examples can mimic a predetermined workflow but cannot make the live discretionary investigative decisions that the packaged runtime delegates to a model.
- Evidence: [workshop/capstone/patrol/patrol.py](https://github.com/tylerelyt/self-evolving-agent-harness/blob/5e2663e7b1f9679f1cb122f244d492ee28b6ccbe/workshop/capstone/patrol/patrol.py#L258-L412); [workshop/capstone/RUNNING.md](https://github.com/tylerelyt/self-evolving-agent-harness/blob/5e2663e7b1f9679f1cb122f244d492ee28b6ccbe/workshop/capstone/RUNNING.md#L36-L88).
- Basis: structural
- Confidence: High
- Caveats: No live provider execution was performed for this source-only assessment; offline scripted examples cannot independently establish model discretion.

## S2 — Coordination

- State: —
- Function: Attenuate operational interference between the two patrol units.
- Disturbance / variety regulated: Shared release-version adoption or concurrent incident work might create interference between agents.
- Decisive decision or feedback right: No shipped conflict-specific choice among competing operational assignments was identified. Version publication and adoption use deterministic lock and all-instance matching.
- Decision owner: The common learner serializes a publication transaction; each patrol's work scope is preassigned, with no demonstrated first-party conflict-adjustment owner.
- Supporting / enforcement mechanisms: Shared version state, `writer_lock`, separate Hermes homes, per-instance worker loops, two-instance adoption check.
- Closure path: Matching published versions alter future patrol behavior but do not resolve a particular conflict between independent S1 task choices.
- Why this is / is not agent-owned: A shared version gate and serialized release process are not evidence of feedback regulating inter-S1 interference.
- Evidence: [workshop/capstone/oncall_service.py](https://github.com/tylerelyt/self-evolving-agent-harness/blob/5e2663e7b1f9679f1cb122f244d492ee28b6ccbe/workshop/capstone/oncall_service.py#L188-L254); [workshop/capstone/oncall_service.py](https://github.com/tylerelyt/self-evolving-agent-harness/blob/5e2663e7b1f9679f1cb122f244d492ee28b6ccbe/workshop/capstone/oncall_service.py#L254-L335); [workshop/capstone/patrol/patrol.py](https://github.com/tylerelyt/self-evolving-agent-harness/blob/5e2663e7b1f9679f1cb122f244d492ee28b6ccbe/workshop/capstone/patrol/patrol.py#L426-L574).
- Basis: structural
- Confidence: Medium
- Caveats: A future user composition could implement conflict resolution; that is not credited to this frozen distribution.

### Absence scope

- Surfaces inspected: Multi-instance on-call runner, learning writer lock, per-instance patrol and adoption.
- Plausible first-party paths checked: Simultaneous patrol work, shared candidate publication and independent incident assignments.
- Why no material first-party path remains: The reviewed paths assign independent environments and serialize the shared update; they do not assess, attenuate and return a specific inter-unit operational conflict.

## S3 — Inside-and-now control

- State: P
- Function: Override current shared Skill commitments across the two running units after a verified operator request.
- Disturbance / variety regulated: A newly adopted common Skill may behave poorly despite passing its prior acceptance tests.
- Decisive decision or feedback right: A local operator decides to approve the rollback of the known adopted version to a specific former version after seeing the current and previous hashes.
- Decision owner: The legitimate local workbench operator; the validator and release transaction are deterministic execution/enforcement.
- Supporting / enforcement mechanisms: Version/state records, frozen hashes, operator request, write lock, content-addressed publication and per-instance verification.
- Closure path: Explicit approval triggers the shared version republish to both agents, changes the active version, and verifies fresh post-rollback patrol sessions and continued operation.
- Boundary reachability: The bundled workbench exposes rollback prepare/approve/execute and uses the same running learner/version store and two receiver paths.
- Why this is / is not agent-owned: The high-impact current commitment choice belongs to the operator, not to a model; the first-party connected parent mode is present in the installed control surface.
- Evidence: [workshop/capstone/workbench.py](https://github.com/tylerelyt/self-evolving-agent-harness/blob/5e2663e7b1f9679f1cb122f244d492ee28b6ccbe/workshop/capstone/workbench.py#L550-L565); [workshop/capstone/workbench_rollback.py](https://github.com/tylerelyt/self-evolving-agent-harness/blob/5e2663e7b1f9679f1cb122f244d492ee28b6ccbe/workshop/capstone/workbench_rollback.py#L72-L143); [workshop/capstone/workbench_rollback.py](https://github.com/tylerelyt/self-evolving-agent-harness/blob/5e2663e7b1f9679f1cb122f244d492ee28b6ccbe/workshop/capstone/workbench_rollback.py#L407-L479).
- Basis: structural
- Confidence: Medium
- Caveats: This is restricted to the shared deployed Skill of the on-call service, not arbitrary cross-service budget or scheduling control. No autonomous whole-current model decision path was established.
- Whole-system current view: `learning/state.json` identifies active and previous release, adoption/rollback status and both receivers; `Workbench` supplies the local operator's active-run and evolution status.
- Current-control decision scope: Approve replacement of the active Skill for the entire two-unit service after adopted-release and environment consistency preconditions; execute and verify a shared, not per-unit, override.

## S3* — Complementary audit

- State: —
- Function: Provide independent complementary challenge of current S1 operation and bind its corrective findings into ongoing control.
- Disturbance / variety regulated: Patrol reports or recovery claims may be wrong despite apparently valid traces.
- Decisive decision or feedback right: Evidence consistency checks and extra HTTP probes are shipped, but no separate independent auditor is shown making a discretionary complementary audit judgment over the whole current operation with a corrective S3 return.
- Decision owner: Runtime validators and fixed case comparators; the operator decides recovery/rollback separately.
- Supporting / enforcement mechanisms: SessionDB receipt cross-check, two healthy windows, independent evaluation/replay of Skill revisions.
- Closure path: Failed checks reject reports or Skill publication; these are routine correctness and adaptation gates, not an established complementary independent S3* feedback authority.
- Why this is / is not agent-owned: Data access and separate test runs alone do not prove a complementary independent audit decision and returned corrective responsibility at the assessed recursion.
- Evidence: [workshop/capstone/patrol/patrol.py](https://github.com/tylerelyt/self-evolving-agent-harness/blob/5e2663e7b1f9679f1cb122f244d492ee28b6ccbe/workshop/capstone/patrol/patrol.py#L365-L412); [workshop/capstone/workbench.py](https://github.com/tylerelyt/self-evolving-agent-harness/blob/5e2663e7b1f9679f1cb122f244d492ee28b6ccbe/workshop/capstone/workbench.py#L710-L759); [workshop/capstone/patrol/fleet_eval.py](https://github.com/tylerelyt/self-evolving-agent-harness/blob/5e2663e7b1f9679f1cb122f244d492ee28b6ccbe/workshop/capstone/patrol/fleet_eval.py#L148-L203).
- Basis: structural
- Confidence: Medium
- Caveats: The external operator can inspect source-linked evidence, but a manual review ability is not automatically a packaged independent audit loop.

### Absence scope

- Surfaces inspected: Patrol source receipt validation, follow-up healthy-window verification, frozen skill replay evaluator and workbench recovery/rollback proof.
- Plausible first-party paths checked: Separate investigation sessions, release qualification, incident verification and audit-looking trace evidence.
- Why no material first-party path remains: The shipped checks enforce local evidence consistency and post-change acceptance, not a distinct independent audit decision over current S1 truth whose findings regulate subsequent S3 action.

## S4 — Outside-and-then intelligence

- State: A
- Function: Generate and adopt a prospective incident response capability revision in response to field incidents and replay performance.
- Disturbance / variety regulated: Novel incident types expose insufficient or obsolete investigation methods; future patrols need improved Skill rules.
- Decisive decision or feedback right: In the live model mode SkillClaw's model uses archived incident sessions and structured analysis to generate a candidate method; a first-party release policy accepts it only if controlled native replay proves nonregression and actual improvement.
- Decision owner: The configured model proposes the future change; the runtime's predefined evaluator is a release veto, not a competing adaptive author.
- Supporting / enforcement mechanisms: Independent archived session inputs, engineering analysis, staged SkillClaw evolution, fixed replay evaluation, version hashes, two-agent adoption and rollback.
- Closure path: A qualified candidate becomes the common active Skill version; the next incident patrols load that version and their observed adoption is checked, or the shared version is restored.
- Boundary reachability: `oncall_service.learn_once` calls `skillclaw_evolve.evolve` with a model connection when live, evaluates the generated candidate and republishes to the actual two patrol receivers.
- Why this is / is not agent-owned: In the live mode the model supplies the altered prospective Skill content; in the default scripted mode the same pipeline is deterministic and should not be misreported as autonomous discovery.
- Evidence: [workshop/capstone/oncall_service.py](https://github.com/tylerelyt/self-evolving-agent-harness/blob/5e2663e7b1f9679f1cb122f244d492ee28b6ccbe/workshop/capstone/oncall_service.py#L238-L335); [workshop/capstone/patrol/skillclaw_evolve.py](https://github.com/tylerelyt/self-evolving-agent-harness/blob/5e2663e7b1f9679f1cb122f244d492ee28b6ccbe/workshop/capstone/patrol/skillclaw_evolve.py#L145-L277); [workshop/capstone/patrol/fleet_eval.py](https://github.com/tylerelyt/self-evolving-agent-harness/blob/5e2663e7b1f9679f1cb122f244d492ee28b6ccbe/workshop/capstone/patrol/fleet_eval.py#L148-L203); [workshop/capstone/RUNNING.md](https://github.com/tylerelyt/self-evolving-agent-harness/blob/5e2663e7b1f9679f1cb122f244d492ee28b6ccbe/workshop/capstone/RUNNING.md#L74-L88).
- Basis: structural
- Confidence: Medium
- Caveats: The evaluation policy is developer authored; no live model was executed in this review. Actual improvement is conditional on a genuinely passing candidate.
- External distinction: Previously encountered HTTP failures, observed investigation evidence and separate evaluation fixtures represent environment-dependent gaps in the existing response method.
- Future / prospective distinction: Candidate revision is proposed for the subsequent patrol session rather than merely addressing the incident just closed.
- Adaptation option generated: Candidate updated on-call Skill, retained only if the model-proposed content passes the pinned nonregression/improvement test.
- Path back into current capability / S3: Version is published to each receiver and later patrols must demonstrate adoption; failed adoption or explicitly approved rollback restores the previous version.

## S5 — Policy and identity

- State: —
- Function: Legitimately revise or settle standing identity and ultimate-policy decisions for the on-call service.
- Disturbance / variety regulated: Changing acceptable risk, approval scope or long-term obligations would require binding policy governance.
- Decisive decision or feedback right: No shipped standing policy issue→legitimate authority→new binding policy→return-to-operation transaction was verified.
- Decision owner: Developers supply fixed release policy; local operator approves particular incidents and rollbacks under that standing policy.
- Supporting / enforcement mechanisms: `release_allowed`, explicit approval and version-scope checks, configured model and service scopes.
- Closure path: A single approved recovery or version restoration executes an operating decision; it does not update ultimate policy or identity.
- Why this is / is not agent-owned: Static policy and task-specific approvals have no evidence of an internal model/governing parent taking and applying a new identity/ultimate-policy decision.
- Evidence: [workshop/capstone/self_improvement_agent.py](https://github.com/tylerelyt/self-evolving-agent-harness/blob/5e2663e7b1f9679f1cb122f244d492ee28b6ccbe/workshop/capstone/self_improvement_agent.py#L19-L29); [workshop/capstone/patrol/fleet_eval.py](https://github.com/tylerelyt/self-evolving-agent-harness/blob/5e2663e7b1f9679f1cb122f244d492ee28b6ccbe/workshop/capstone/patrol/fleet_eval.py#L148-L153); [workshop/capstone/workbench.py](https://github.com/tylerelyt/self-evolving-agent-harness/blob/5e2663e7b1f9679f1cb122f244d492ee28b6ccbe/workshop/capstone/workbench.py#L801-L849); [workshop/capstone/workbench_rollback.py](https://github.com/tylerelyt/self-evolving-agent-harness/blob/5e2663e7b1f9679f1cb122f244d492ee28b6ccbe/workshop/capstone/workbench_rollback.py#L124-L143).
- Basis: structural
- Confidence: Medium
- Caveats: Individual operator approvals are not reclassified as S5 policy decisions.

### Absence scope

- Surfaces inspected: Release policy, configured service scopes, local recovery confirmation and rollback approval flow.
- Plausible first-party paths checked: Model choice of policy, operator approval and globally updated constraints/identity.
- Why no material first-party path remains: Source offers fixed risk boundaries and bounded current-work intervention, not a reconstructable live governance loop for changing standing authority.

## Recursion

The two Hermes patrols are lower operational units within one local service. A human operator governs the common recovery/version rollback surface, while the learner modifies shared future Skill capability. Service-specific incident pages do not themselves imply additional S3/S5 recursion.

## Variety and escalation

Current HTTP health and incoming incident events are absorbed through model tool-use and persistent observation. Recovery is explicitly paged and approval-gated; an improvement proposal passes deterministic fixed-replay and multi-receiver adoption checks before it changes what future patrols do.

## Evidence gaps

This is a pinned **source-only** review. No model-provider live run, production deployment, independent semantic second review or independent operational S3* audit was performed. The offline script-driven demonstrations establish the wired paths and reproducibility, not autonomous behavior by themselves. External Hermes and SkillClaw internals were not credited as separate organizational functions beyond the first-party reachable configuration.

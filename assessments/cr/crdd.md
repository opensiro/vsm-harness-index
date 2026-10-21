---
harness_id: crdd
project_name: CRDD (Context Repository-Driven Development)
repository: https://github.com/qual-lab/CRDD
review_ref: e9947d4f733c3c46b90ee9f78c70898d1920bae9
reviewed_at: 2026-10-21
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-21
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# CRDD (Context Repository-Driven Development)

**Canonical disposition:** `included` as a narrowly bounded first-party model-driven task execution harness, not as a fully implemented autonomous enterprise organization. Index batch [#1827](https://github.com/opensiro/vsm-harness-index/issues/1827) row 5, original intake #1281 position 8.

## Review boundary

- System in focus: the released CRDD Coordinator Runtime / Project Runtime execution path, its verified task/object context and bounded effect/candidate return, distinct from broad human-centered CRDD development-methodology documents.
- Purpose and identity: preserve development intent and authority while delegating bounded specialist execution and independent task-local review to CLI-based model agents, returning candidate changes to responsible humans.
- Relevant environment: Git source repository with pinned revision, Windows local user, Docker Desktop, Node 24.12+, official Codex and Claude Code subscription sessions, signed CRDD distribution, project ownership and human candidate acceptance.
- Standard-distribution boundary: signed `v0.21.0` tag resolving to pinned `e9947d4f733c3c46b90ee9f78c70898d1920bae9` (annotated tag peeled to this commit), `40_Develop/coordinator` source, `template/tools` public entrypoints and shipped native `platform-access` carrier. A tag alone does not prove the signed artifact currently executes; releases must meet manifest, runtime identity, consent and host eligibility.
- Credited operating / distribution surfaces: Coordinator CLI `task` request; typed task runtime, subscription OAuth agent launch adapters, isolated workspace, selected independent verifier, candidate result and human-controlled integration paths; Project Runtime objective/decision public route with limited concurrent work and recovery.
- Adjacent first-party surfaces excluded from ownership: normative `04_Agent_Organization.md` role system not instantiated into continuing agent departments, non-normative future `05_Autonomous_Operation.md`, development tests, Checker independent artifact validation as organizational S3*, external model CLI reasoning as a full independent institution, unmeasured customer deployments and planned v0.22 Workbench scope.
- First-party operating / deployment modes considered: standard signed Windows/Node/Docker Codex/Claude Code constrained delegated task, single objective Project Runtime, candidate export/discard and human acceptance, failure/cancel/cleanup recovery, signed release path, non-effectful Checker; no assumed Linux/macOS or long-term unattended enterprise federation.
- Recursion level: single or limited concurrent human-authorized repository development work episodes, not a continuing multi-business VSM recursive organization.
- Reviewed revision: e9947d4f733c3c46b90ee9f78c70898d1920bae9 (official v0.21.0 tag also peels to this commit).
- Observation date: 2026-10-21.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The [README](https://github.com/qual-lab/CRDD/blob/e9947d4f733c3c46b90ee9f78c70898d1920bae9/README.md) sharply separates human decision authority and context repository methodology from a released Coordinator implementation. The [current behavior reference](https://github.com/qual-lab/CRDD/blob/e9947d4f733c3c46b90ee9f78c70898d1920bae9/05_SPEC/07_Current_Behavior_Reference.md) and [workflow](https://github.com/qual-lab/CRDD/blob/e9947d4f733c3c46b90ee9f78c70898d1920bae9/19_Workflows/01_Coordinator_Runtime.md) identify signed distribution, real subscription CLI providers, capability/consent/authority checks, task execution in isolated Docker/workspaces, candidate results and exact recovery. [Quality status](https://github.com/qual-lab/CRDD/blob/e9947d4f733c3c46b90ee9f78c70898d1920bae9/07_Quality/01_Quality_Center.md) records bounded real-provider 4/4 and seven recovery scenarios for an earlier or included release identity but explicitly declines overall Quality Ready because 22 v0.21 Hybrid/Manual items remain unobserved. These are bounded provenance statements, not replicated E2E results in this review.

The first-party `coordinator-task-runtime.ts` owns the actual task operation and connects provider-specific Codex and Claude runtime adapters, scoped repository projection, provider/task packet and structured results to a candidate store and recovery. `ProjectRuntimeCompositionRoot` builds public objective requests and separate acceptance decision channels. The model-backed executor can make semantic implementation choices and a separate reviewer can inspect them, but isolation, signed permission and final source promotion remain outside the model's discretionary authority. Evidence: [40_Develop/coordinator/src/security/coordinator-task-runtime.ts](https://github.com/qual-lab/CRDD/blob/e9947d4f733c3c46b90ee9f78c70898d1920bae9/40_Develop/coordinator/src/security/coordinator-task-runtime.ts); [40_Develop/coordinator/src/security/codex-docker-runtime-adapter.ts](https://github.com/qual-lab/CRDD/blob/e9947d4f733c3c46b90ee9f78c70898d1920bae9/40_Develop/coordinator/src/security/codex-docker-runtime-adapter.ts); [40_Develop/coordinator/src/security/claude-docker-runtime-adapter.ts](https://github.com/qual-lab/CRDD/blob/e9947d4f733c3c46b90ee9f78c70898d1920bae9/40_Develop/coordinator/src/security/claude-docker-runtime-adapter.ts); [40_Develop/coordinator/src/composition/project-runtime-composition-root.ts](https://github.com/qual-lab/CRDD/blob/e9947d4f733c3c46b90ee9f78c70898d1920bae9/40_Develop/coordinator/src/composition/project-runtime-composition-root.ts); [40_Develop/coordinator/src/security/project-runtime-candidate-integration-adapter.ts](https://github.com/qual-lab/CRDD/blob/e9947d4f733c3c46b90ee9f78c70898d1920bae9/40_Develop/coordinator/src/security/project-runtime-candidate-integration-adapter.ts); [40_Develop/coordinator/src/security/provider-task-structured-result.ts](https://github.com/qual-lab/CRDD/blob/e9947d4f733c3c46b90ee9f78c70898d1920bae9/40_Develop/coordinator/src/security/provider-task-structured-result.ts); [40_Develop/coordinator/src/security/external-send-consent-runtime.ts](https://github.com/qual-lab/CRDD/blob/e9947d4f733c3c46b90ee9f78c70898d1920bae9/40_Develop/coordinator/src/security/external-send-consent-runtime.ts).

A distinct bundled [platform-provisioner manifest](https://github.com/qual-lab/CRDD/blob/e9947d4f733c3c46b90ee9f78c70898d1920bae9/template/tools/coordinator/coordinator-package-manifest.json) contains an expiration timestamp and package-specific source identity that must not be substituted for the v0.21.0 overall signed release manifest. Similarly current quality evidence distinguishes source A, carrier B and runtime execution identity. This assessment does not assert present ability to launch a provider from our examination environment, nor claim live authenticated subscriptions or general production installation.

## Operational model

Human-authorized task and pinned repository → eligible signed Coordinator and consent/authority checks → isolated provider workspace → model-based executor/reviewer work under Codex/Claude CLI with tool results → structured receipts and candidate snapshot → separate human candidate export/acceptance (or discard) and exact recovery. The source-ground first-party operational path provides meaningful S1 at a configured provider boundary; review and Project Runtime don't automatically establish independent S2, whole S3, complementary S3*, future S4 or ultimate S5.
## S1 — Operations

- State: A
- Function: Complete a bounded human-authorized repository development task by directing configured model-backed Codex/Claude CLI workers to create, inspect and return an isolated code/artifact candidate.
- Disturbance / variety regulated: Changing repository context, open-ended task requirements and code/test/reviewer findings.
- Decisive decision or feedback right: Within the admitted task and scoped file/network authority, an external CLI agent chooses substantive source edits or review judgments based on task and tool feedback; the first-party runtime owns the signed release gate, task dispatch, isolation, effect boundaries, durable results and candidate return.
- Decision owner: The model-based executor/reviewer is launched by the CRDD first-party Coordinator; humans retain final canonical promotion/acceptance. The provider's own inference and account are dependencies, not first-party organizational governance.
- Supporting / enforcement mechanisms: Signed release and exact runtime identity, local consent/authority gate, context projection, task packets, Docker provider execution, structured result, independent reviewer where selected, candidate-store and explicit recovery.
- Closure path: Admitted task and authorized source snapshot → provider selection and isolated workspace → first-party launch of Codex/Claude worker → model-guided code/review work → bounded artifact/result return → candidate validation and human export/acceptance, not automatic repository write-through.
- Boundary reachability: Public Coordinator CLI/Project Runtime source has wired `startRuntimeOwnedCoordinatorTask`, provider prep, Docker process start, `TaskCompletionRecord` and Project Runtime wrappers. Official v0.21.0 annotated tag resolves to the frozen SHA, but runtime execution still depends on signed manifest identity, eligible host/provider and consent.
- Why this is / is not agent-owned: First-party task handoff, provider session creation, tool-result/candidate recording and explicitly bounded model choice constitute a supported model-owned coding work cell, while human final acceptance is not transferred.
- Evidence: [README.md](https://github.com/qual-lab/CRDD/blob/e9947d4f733c3c46b90ee9f78c70898d1920bae9/README.md); [19_Workflows/01_Coordinator_Runtime.md](https://github.com/qual-lab/CRDD/blob/e9947d4f733c3c46b90ee9f78c70898d1920bae9/19_Workflows/01_Coordinator_Runtime.md); [05_SPEC/07_Current_Behavior_Reference.md](https://github.com/qual-lab/CRDD/blob/e9947d4f733c3c46b90ee9f78c70898d1920bae9/05_SPEC/07_Current_Behavior_Reference.md); [40_Develop/coordinator/src/security/coordinator-task-runtime.ts](https://github.com/qual-lab/CRDD/blob/e9947d4f733c3c46b90ee9f78c70898d1920bae9/40_Develop/coordinator/src/security/coordinator-task-runtime.ts); [40_Develop/coordinator/src/security/codex-docker-runtime-adapter.ts](https://github.com/qual-lab/CRDD/blob/e9947d4f733c3c46b90ee9f78c70898d1920bae9/40_Develop/coordinator/src/security/codex-docker-runtime-adapter.ts); [40_Develop/coordinator/src/security/claude-docker-runtime-adapter.ts](https://github.com/qual-lab/CRDD/blob/e9947d4f733c3c46b90ee9f78c70898d1920bae9/40_Develop/coordinator/src/security/claude-docker-runtime-adapter.ts); [40_Develop/coordinator/src/composition/project-runtime-composition-root.ts](https://github.com/qual-lab/CRDD/blob/e9947d4f733c3c46b90ee9f78c70898d1920bae9/40_Develop/coordinator/src/composition/project-runtime-composition-root.ts); [40_Develop/coordinator/src/security/provider-task-structured-result.ts](https://github.com/qual-lab/CRDD/blob/e9947d4f733c3c46b90ee9f78c70898d1920bae9/40_Develop/coordinator/src/security/provider-task-structured-result.ts)
- Basis: structural and explicit.
- Confidence: moderate-high.
- Caveats: Source inspection only in this review; no Windows Docker, real Codex/Claude Subscription OAuth or release-signature E2E rerun. v0.21 quality report retains 22 unobserved Hybrid/Manual items; do not overclaim completeness.


## S2 — Coordination

- State: —
- Function: Attenuate conflicts between independent continuing viable S1 work cells and return changed commitments to them.
- Disturbance / variety regulated: Two agents may encounter shared files/intent contradictions or reviewer-executor disagreements.
- Decisive decision or feedback right: A first-party organizational S2 owner must detect a concrete inter-cell reciprocal disturbance, resolve it, and feed the decision back to independent S1 cells.
- Decision owner: Coordinator selects an executor and separately bounded reviewer for **one** submitted work item; this is a task pipeline, not an ongoing cross-unit S2 relation.
- Supporting / enforcement mechanisms: Provider eligibility, executor/reviewer separation, task segmentation, isolated candidate workspaces, limited Project Runtime concurrency and recovery locks.
- Closure path: A reviewer checks an executor candidate and returns task-local findings; the next task stage may retry or leave work for human review. No path establishes continuing S1 businesses with reciprocal interference and a first-party interdepartmental attenuation owner.
- Boundary reachability: The named organization in normative CRDD documents is a framework and future design. Execution wiring currently dispatches task episodes and does not instantiate ongoing independently viable departments.
- Why this is / is not agent-owned: Described control does not perform the required function-specific organizational decision or feedback at this recursion; static standards and per-task safeguards are not reclassified into VSM functions.
- Evidence: [40_Develop/coordinator/src/security/coordinator-task-runtime.ts](https://github.com/qual-lab/CRDD/blob/e9947d4f733c3c46b90ee9f78c70898d1920bae9/40_Develop/coordinator/src/security/coordinator-task-runtime.ts); [40_Develop/coordinator/src/composition/project-runtime-composition-root.ts](https://github.com/qual-lab/CRDD/blob/e9947d4f733c3c46b90ee9f78c70898d1920bae9/40_Develop/coordinator/src/composition/project-runtime-composition-root.ts); [04_Agent_Organization.md](https://github.com/qual-lab/CRDD/blob/e9947d4f733c3c46b90ee9f78c70898d1920bae9/04_Agent_Organization.md); [05_SPEC/07_Current_Behavior_Reference.md](https://github.com/qual-lab/CRDD/blob/e9947d4f733c3c46b90ee9f78c70898d1920bae9/05_SPEC/07_Current_Behavior_Reference.md); [19_Workflows/01_Coordinator_Runtime.md](https://github.com/qual-lab/CRDD/blob/e9947d4f733c3c46b90ee9f78c70898d1920bae9/19_Workflows/01_Coordinator_Runtime.md)
- Basis: structural and explicit.
- Confidence: moderate-high.
- Caveats: Actual isolated execution and independent review are real safeguards; they are not sufficient for S2 by themselves.

### Absence scope

- Surfaces inspected: Provider scheduler, optional reviewer, Project Runtime current task graph, candidate isolation, workflow docs and organization norms.
- Plausible first-party paths checked: Ongoing independently operating agentic S1 units with shared-commitment conflict, first-party resolution right and feedback changing each unit's behavior.
- Why no material first-party path remains: Only task-local reviewer/executor dependencies, capacity/admission, and source isolation are shown; no organizational cross-unit return path is established.

## S3 — Inside-and-now control

- State: —
- Function: Regulate present resources, priorities, commitments and exceptions for the continuing whole agent organization.
- Disturbance / variety regulated: Parallel project objectives, provider cost/eligibility, approval backlog and conflicting priorities would demand whole-system resource bargaining.
- Decisive decision or feedback right: Choose and revise organization-wide operating commitments and return decisions to constituent S1 units based on current performance.
- Decision owner: Caller human decides task scope/authority and accepts candidates; Coordinator enforces policy and runs one or limited concurrent bounded tasks, not a discretionary agent-managed whole-system controller.
- Supporting / enforcement mechanisms: Project Runtime objective intake, execution selection gate, model/provider eligibility, quotas, candidate store, effective consent, status projection, exact cancellation/recovery.
- Closure path: A task is accepted or fail-closed at its scope and returned as a candidate. Evidence of a continuing managerial resource allocation loop across viable operational departments and parent state return is missing.
- Boundary reachability: Even dynamic provider routing and project reports are an operation-level scheduler/admission function; the repository separates signed runtime from human purpose, acceptance and production promotion.
- Why this is / is not agent-owned: Described control does not perform the required function-specific organizational decision or feedback at this recursion; static standards and per-task safeguards are not reclassified into VSM functions.
- Evidence: [40_Develop/coordinator/src/composition/project-runtime-composition-root.ts](https://github.com/qual-lab/CRDD/blob/e9947d4f733c3c46b90ee9f78c70898d1920bae9/40_Develop/coordinator/src/composition/project-runtime-composition-root.ts); [40_Develop/coordinator/src/security/coordinator-task-runtime.ts](https://github.com/qual-lab/CRDD/blob/e9947d4f733c3c46b90ee9f78c70898d1920bae9/40_Develop/coordinator/src/security/coordinator-task-runtime.ts); [40_Develop/coordinator/src/security/provider-eligibility-runtime.ts](https://github.com/qual-lab/CRDD/blob/e9947d4f733c3c46b90ee9f78c70898d1920bae9/40_Develop/coordinator/src/security/provider-eligibility-runtime.ts); [05_SPEC/07_Current_Behavior_Reference.md](https://github.com/qual-lab/CRDD/blob/e9947d4f733c3c46b90ee9f78c70898d1920bae9/05_SPEC/07_Current_Behavior_Reference.md); [07_Quality/01_Quality_Center.md](https://github.com/qual-lab/CRDD/blob/e9947d4f733c3c46b90ee9f78c70898d1920bae9/07_Quality/01_Quality_Center.md)
- Basis: structural and explicit.
- Confidence: moderate.
- Caveats: Limited concurrency, controlled budgets and diagnostics are substantial first-party runtime controls but not a VSM S3 owner.

### Absence scope

- Surfaces inspected: Project Runtime public objective route, task provider selection, bounded concurrency, execution/cleanup/recovery, progress/status projection and human acceptance adapter.
- Plausible first-party paths checked: Whole-organization commitments/performance reports and decisive global priority/resource changes enacted into continuing independently viable S1 units.
- Why no material first-party path remains: Inspected first-party decisions concern whether/how an individual delegated objective proceeds; project-level views do not close an organizational managerial resource-feedback loop.

## S3* — Complementary audit

- State: —
- Function: Independently inspect operational truth beyond routine S3 reports and return discrepancies for corrective whole-system management.
- Disturbance / variety regulated: An executor's self-report might be wrong, or a signed artifact might not correspond to reality.
- Decisive decision or feedback right: Complementary auditor must choose a field inspection, compare it with normal management account and return a correction to a separate S3 owner.
- Decision owner: CRDD's selected independent reviewer and Checker verify bounded candidate/contracts; no independently constituted S3-account audit judgment/return owner is demonstrated.
- Supporting / enforcement mechanisms: Independent model reviewer, quality/checker tests, signed manifest and execution receipts, artifact provenance, structured candidate verification.
- Closure path: Reviewer feedback can reject a code candidate or cause task-local recovery, but does not constitute independent field audit over standing organizational S3 reporting.
- Boundary reachability: The code has real verification (including provider-backed four-path evidence) while repository Quality Center explicitly leaves 22 release-scope items without evidence. Do not equate more testing with S3*.
- Why this is / is not agent-owned: Described control does not perform the required function-specific organizational decision or feedback at this recursion; static standards and per-task safeguards are not reclassified into VSM functions.
- Evidence: [40_Develop/coordinator/src/security/coordinator-task-runtime.ts](https://github.com/qual-lab/CRDD/blob/e9947d4f733c3c46b90ee9f78c70898d1920bae9/40_Develop/coordinator/src/security/coordinator-task-runtime.ts); [40_Develop/checker/src/index.ts](https://github.com/qual-lab/CRDD/blob/e9947d4f733c3c46b90ee9f78c70898d1920bae9/40_Develop/checker/src/index.ts); [05_SPEC/07_Current_Behavior_Reference.md](https://github.com/qual-lab/CRDD/blob/e9947d4f733c3c46b90ee9f78c70898d1920bae9/05_SPEC/07_Current_Behavior_Reference.md); [07_Quality/01_Quality_Center.md](https://github.com/qual-lab/CRDD/blob/e9947d4f733c3c46b90ee9f78c70898d1920bae9/07_Quality/01_Quality_Center.md); [19_Workflows/01_Coordinator_Runtime.md](https://github.com/qual-lab/CRDD/blob/e9947d4f733c3c46b90ee9f78c70898d1920bae9/19_Workflows/01_Coordinator_Runtime.md)
- Basis: structural and explicit.
- Confidence: high.
- Caveats: Negative is limited to complementary organizational audit, not absence of safety engineering or an independent task-level reviewer.

### Absence scope

- Surfaces inspected: Independent executor/reviewer boundary, Checker, quality/evidence reports, release verification, candidate/runtime audit receipts.
- Plausible first-party paths checked: Separately mandated audit reaching operational ground truth rather than routine process output, contradictory findings and corrected S3 policy/control decision.
- Why no material first-party path remains: Review/Checker close the current artifact's accept/reject criterion; no independently returned S3 management-account correction is evidenced.

## S4 — Outside-and-then intelligence

- State: —
- Function: Sense future-relevant external changes and generate accepted adaptation to the operating organization's capabilities through strategic S3 conversation.
- Disturbance / variety regulated: Evolving provider model capabilities and requirements across projects could demand future capability investment.
- Decisive decision or feedback right: Propose/choose prospective organizational capability changes and return them to current S3 or legitimate governance.
- Decision owner: Versioned release, model/provider eligibility and documentation roadmap have human owners; runtime chooses current task providers without autonomous environmental strategy function.
- Supporting / enforcement mechanisms: Provider model eligibility and choice, future non-normative `05_Autonomous_Operation.md`, context/dependency docs, release/quality reports.
- Closure path: Provider routing and build verification handle current delegated work; roadmap and future governance are normative/design artifacts, with no executable outside-then prospective strategist linked back to an ongoing S3.
- Boundary reachability: Current code returns candidates and constrained task results, not strategic future option adoption.
- Why this is / is not agent-owned: Described control does not perform the required function-specific organizational decision or feedback at this recursion; static standards and per-task safeguards are not reclassified into VSM functions.
- Evidence: [05_Autonomous_Operation.md](https://github.com/qual-lab/CRDD/blob/e9947d4f733c3c46b90ee9f78c70898d1920bae9/05_Autonomous_Operation.md); [04_Agent_Organization.md](https://github.com/qual-lab/CRDD/blob/e9947d4f733c3c46b90ee9f78c70898d1920bae9/04_Agent_Organization.md); [40_Develop/coordinator/src/composition/project-runtime-composition-root.ts](https://github.com/qual-lab/CRDD/blob/e9947d4f733c3c46b90ee9f78c70898d1920bae9/40_Develop/coordinator/src/composition/project-runtime-composition-root.ts); [40_Develop/coordinator/src/security/provider-eligibility-runtime.ts](https://github.com/qual-lab/CRDD/blob/e9947d4f733c3c46b90ee9f78c70898d1920bae9/40_Develop/coordinator/src/security/provider-eligibility-runtime.ts); [05_SPEC/07_Current_Behavior_Reference.md](https://github.com/qual-lab/CRDD/blob/e9947d4f733c3c46b90ee9f78c70898d1920bae9/05_SPEC/07_Current_Behavior_Reference.md)
- Basis: structural and explicit.
- Confidence: moderate-high.
- Caveats: This does not deny human strategic work using CRDD's context repository.

### Absence scope

- Surfaces inspected: Model/provider selection rules, Project Runtime decision policies, release planning, roadmap and non-normative autonomy design.
- Plausible first-party paths checked: Accepted future environment-sensing options directed into a present organizational S3 and later S1 operating capability.
- Why no material first-party path remains: Proposed/provider-selection activities address runtime suitability for the current task or human-authored future process, not an agent-owned prospective adaptation closure.

## S5 — Policy and identity

- State: —
- Function: Legitimately adjudicate identity, ultimate purpose and constitutional policy for the agent organization and return the decision as active authority.
- Disturbance / variety regulated: Conflict between user intent, provider handling rights, acceptance boundaries and long-term mission could require ultimate policy judgment.
- Decisive decision or feedback right: Adopt/revise constitutional purpose, verify legitimate holder and return accepted policy to future S1 operations.
- Decision owner: CRDD principles explicitly reserve value, meaning, important decisions, risk acceptance and final accountability for humans; runtime implementation verifies signed release/consent and object-specific acceptance, not whole-agent-organization identity policy decisions.
- Supporting / enforcement mechanisms: Human scope/intent preservation, local consent, authority grant verifier, release manifest gate, object-specific candidate acceptance.
- Closure path: A human grants external send consent or promotes a candidate after review; the implementation enforces that scope, but no first-party ultimate purpose-policy adjudication and new active constitutional authority return is evidenced at the agent-organization recursion.
- Boundary reachability: Normative `04_Agent_Organization` sections 1–11 describe a philosophy, with section 12/future autonomous operation explicitly non-normative. The signed runtime is a tool under human authority, not a constitutional organization identity regulator.
- Why this is / is not agent-owned: Described control does not perform the required function-specific organizational decision or feedback at this recursion; static standards and per-task safeguards are not reclassified into VSM functions.
- Evidence: [04_Agent_Organization.md](https://github.com/qual-lab/CRDD/blob/e9947d4f733c3c46b90ee9f78c70898d1920bae9/04_Agent_Organization.md); [05_Autonomous_Operation.md](https://github.com/qual-lab/CRDD/blob/e9947d4f733c3c46b90ee9f78c70898d1920bae9/05_Autonomous_Operation.md); [40_Develop/coordinator/src/security/external-send-consent-runtime.ts](https://github.com/qual-lab/CRDD/blob/e9947d4f733c3c46b90ee9f78c70898d1920bae9/40_Develop/coordinator/src/security/external-send-consent-runtime.ts); [40_Develop/coordinator/src/security/project-runtime-acceptance-authority-adapter.ts](https://github.com/qual-lab/CRDD/blob/e9947d4f733c3c46b90ee9f78c70898d1920bae9/40_Develop/coordinator/src/security/project-runtime-acceptance-authority-adapter.ts); [40_Develop/coordinator/src/security/project-runtime-candidate-integration-adapter.ts](https://github.com/qual-lab/CRDD/blob/e9947d4f733c3c46b90ee9f78c70898d1920bae9/40_Develop/coordinator/src/security/project-runtime-candidate-integration-adapter.ts); [05_SPEC/07_Current_Behavior_Reference.md](https://github.com/qual-lab/CRDD/blob/e9947d4f733c3c46b90ee9f78c70898d1920bae9/05_SPEC/07_Current_Behavior_Reference.md)
- Basis: structural and explicit.
- Confidence: moderate-high.
- Caveats: Human legitimacy and useful authority enforcement remain meaningful, but task-scope permission/acceptance is not S5.

### Absence scope

- Surfaces inspected: Normative context/intent principles, local human consent, provider/repository grants, Project Runtime acceptance decision adapter and release signing.
- Plausible first-party paths checked: A legitimate ultimate identity/purpose policy dispute, adoption of new constitutional rule by an authenticated holder, and binding return to ongoing organization-level agent operations.
- Why no material first-party path remains: Reviewed rights bind a tool/task/candidate or its distribution identity, not a system-wide policy-identity conversation of a viable agent organization.
## Distributed OSS parent arrangement

The methodology's normative agent organization and maintained Git repository do not mean a self-contained continuing autonomous OSS organization runs inside Coordinator. The released v0.21 execution tool is assessed as task/candidate runtime, with human parent taking responsibility for value and acceptance. No multi-operator distributed authority governance inferred.

## Self-hosted and non-human modes

Normal signed release path requires authenticated Windows user, Node, Docker, official provider OAuth session and consent. The model's coding choices occur only inside the permissioned temporary execution boundary. Human candidate acceptance is external and explicit. No non-human ultimate policy authority is claimed; nor are developer tests or signed manifests counted as autonomous functions.

## Recursion

A front coordinator, model executor and separately selected reviewer are roles within one task workstream. They are not three independently viable recursive organizational units with their own metasystems. Isolated projects and project status reports are context partitions rather than proven viable nested recursions.

## Variety and escalation

Unrecognized execution/cleanup state, missing rights, stale provider identity or unknown recovery identifiers fail closed. These controls constrain an authorized task and can escalate to human recovery/acceptance, but don't prove an organization-level algedonic S3/S5 feedback circuit. Repo Context IDs, preserved intent and traceable decisions improve evidence quality without changing autonomy state by themselves.

## Evidence gaps

- Pinned source corresponds to official annotated release tag v0.21.0, but this review did not validate signatures, current non-expiry manifest, live provider authorization or Windows Docker execution. The bundled provisioner package manifest has its own identity/expiry and is not proof of general release validity.
- The Quality Center notes v0.21 selected provider E2E and recovery successes at an explicitly named earlier source/carrier execution identity; **22 Hybrid/Manual release-scope items remain unobserved**. These do not negate source-level reachability but prohibit an unqualified production claim.
- The published CRDD methods and planned autonomous roles cannot supply S2/S3/S3*/S4/S5 without traced first-party operating decision rights and return. Human user control over one candidate or OAuth consent is not automatic parent S5.
- No source modification, provider invocation, expensive release E2E or destructive effect was executed as part of this source-first assessment.

---
harness_id: kata-symphony
project_name: Kata Symphony
repository: https://github.com/gannonh/kata-symphony
review_ref: e7c160f5e4d485fdfb6d79296f56d36c8872b2a9
reviewed_at: 2026-10-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Kata Symphony

## Review boundary

- System in focus: a user-configured Symphony software-factory installation serving one repository/project, including independent issue workers, shared-context coordination and optional supervisor and structured review/verification stages.
- Purpose and identity: turn accepted tracker issues into source changes, pull requests and evidence-based review outcomes while preserving project-isolated workspace and publication controls.
- Relevant environment: source and tests, changing GitHub/Linear issue states, independent edits by parallel workers, PR diffs, review findings, stalled tool calls and operator interventions.
- Standard distribution: Rust `apps/symphony` orchestrator, Pi/Codex worker adapters, shipped workflow/prompt assets, first-party factory stage coordinators, optional event-driven supervisor, and supported tracker/project routing. The surrounding Kata planning CLI is adjacent, not automatically a Symphony controller.
- First-party operating modes considered: tracker-driven headless workers, concurrent workspaces, optional `supervisor.enabled`, optional factory A4 review in preview or automatic mode, optional A5 verification preview; these toggles default disabled where the shipped config says so.
- Adjacent first-party surfaces excluded: repo maintainers' product governance, demo scripts, CI workflows, the Kata Skills authoring workflow, fake-worker fixtures, the Pi/Codex provider model internals and human project decisions outside the packaged runtime.
- Recursion: independently bounded issue workers are operating S1 cells; a shared project orchestrator supplies cross-worker interfaces and lifecycle machinery. A worker process or staged model role is not by itself a full recursive viable system.
- Reviewed revision: `gannonh/kata-symphony@e7c160f5e4d485fdfb6d79296f56d36c8872b2a9`; source checkout exactly pinned, `apps/symphony/Cargo.toml` MIT.
- Observation date: 2026-10-29; Profile 0.2.4, released Methodology 0.3.7.

## Repository architecture

Symphony polls a configured tracker, selects routable issues, gives each a separate workspace, and drives Pi or Codex model sessions through issue-specific work, tests, PR creation and tracker updates. The normal issue-worker model owns source-specific tool and implementation choices. The Rust event loop, retry/backoff, concurrency slots, workspace lifecycle and issue-state transition logic provide deterministic support. [Public runtime entry](https://github.com/gannonh/kata-symphony/blob/e7c160f5e4d485fdfb6d79296f56d36c8872b2a9/apps/symphony/README.md), [orchestrator](https://github.com/gannonh/kata-symphony/blob/e7c160f5e4d485fdfb6d79296f56d36c8872b2a9/apps/symphony/src/orchestrator.rs), [workflow configuration](https://github.com/gannonh/kata-symphony/blob/e7c160f5e4d485fdfb6d79296f56d36c8872b2a9/apps/symphony/docs/WORKFLOW-REFERENCE.md).

In the supported opt-in supervisor, independent workers editing the same file are detected from actual tool events. The runtime writes a project-scoped shared-context warning and may emit a targeted steering event; subsequent worker prompts include shared project context. These are fixed code-path decisions (event classification, time window and canned guidance), even though the shipped prompt calls the component an agent and `model` is a configurable field reserved for future model decisions. [Supervisor implementation](https://github.com/gannonh/kata-symphony/blob/e7c160f5e4d485fdfb6d79296f56d36c8872b2a9/apps/symphony/src/supervisor.rs), [shared-context injection](https://github.com/gannonh/kata-symphony/blob/e7c160f5e4d485fdfb6d79296f56d36c8872b2a9/apps/symphony/src/orchestrator.rs), [file-overlap test](https://github.com/gannonh/kata-symphony/blob/e7c160f5e4d485fdfb6d79296f56d36c8872b2a9/apps/symphony/tests/supervisor_tests.rs).

The optional A4 worker is an isolated, read-only model review of the actual PR diff, accepted spec and implementation manifest. Its typed findings refer to the reviewed head/base, are schema-checked against real changed lines, and may publish a blocking review/route requiring corrections. A5 adds another evidence path: actual test command results, hashed evidence and a separately credential-isolated verifier's per-criterion judgment; a deterministic gate cannot convert failed commands or missing proof into success. These roles differ from the implementation owner's self-report, but their status is not proof of an external independent auditor. [A4 worker](https://github.com/gannonh/kata-symphony/blob/e7c160f5e4d485fdfb6d79296f56d36c8872b2a9/apps/symphony/src/review/worker.rs), [review coordinator](https://github.com/gannonh/kata-symphony/blob/e7c160f5e4d485fdfb6d79296f56d36c8872b2a9/apps/symphony/src/review/coordinator.rs), [A5 worker](https://github.com/gannonh/kata-symphony/blob/e7c160f5e4d485fdfb6d79296f56d36c8872b2a9/apps/symphony/src/verification/worker.rs), [verification gate](https://github.com/gannonh/kata-symphony/blob/e7c160f5e4d485fdfb6d79296f56d36c8872b2a9/apps/symphony/src/verification/gate.rs).

## Operational model

The issue worker chooses which code, command and test to run and reacts to observed tool and tracker results. Parallel workers can collide on a shared file; the optional supervisor senses this interference and publishes coordination guidance through project context at the next worker prompt. Separately enabled review/verification roles make a source/evidence-based judgment about an implementer's delivered artifact and produce findings that can block or re-route its ordinary work. The named supervisor is not an invoked model, and final task/PR/workflow policy remains configured or human-owned.

## S1 — Operations

- State: A
- Function: implement, test and submit a real tracker issue in an isolated project workspace.
- Disturbance / variety regulated: ambiguous issue requirements, evolving repository code, tool/test failure and shifting tracker feedback.
- Decisive decision or feedback right: Pi/Codex agent chooses source-specific inspection, edit, test, correction and PR actions.
- Decision owner: model-backed issue worker session; the parent Rust dispatcher chooses when and where, not what code to write.
- Supporting / enforcement mechanisms: tracker adapters, WORKFLOW prompt, workspace isolation, state transition guards, turn limits, retries and streamed events.
- Closure path: eligible issue → worker prompt and actual repo tools → changed code/tests/PR and tracker update → continued model session or terminal issue state.
- Boundary reachability: `symphony` binary and supported Pi/Codex runner mode, not only unit mocks.
- Why agent-owned: without a model, orchestration can route tickets but cannot choose appropriate issue-specific code changes.
- Evidence: [headless issue lifecycle](https://github.com/gannonh/kata-symphony/blob/e7c160f5e4d485fdfb6d79296f56d36c8872b2a9/apps/symphony/README.md), [session worker](https://github.com/gannonh/kata-symphony/blob/e7c160f5e4d485fdfb6d79296f56d36c8872b2a9/apps/symphony/src/orchestrator.rs), [implementation stage](https://github.com/gannonh/kata-symphony/blob/e7c160f5e4d485fdfb6d79296f56d36c8872b2a9/apps/symphony/src/implementation/coordinator.rs).
- Basis: shipped supported model invocation and work-loop structure; no paid provider E2E run.
- Confidence: high for reachable decision owner, unmeasured quality.

## S2 — Coordination

- State: C
- Function: attenuate conflicting edits from two separately executing issue workers in one project.
- Disturbance / variety regulated: two active independent workers both editing `src/auth.rs` within a short window, risking incompatible changes and lost context.
- Distinct S1 units: independent issue identities/workspaces such as `KAT-3001` and `KAT-3002`, not two turns of one worker.
- Inter-S1 interference: a source file overlap is identified from separate worker tool events rather than merely hypothesized from parallelism.
- Coordination relation: selected optional `SupervisorAgent` detects the overlap, records a project-scoped warning with both workers and emits a cooldown-bounded steer event.
- Feedback into S1: `build_shared_context_block_for_issue` injects project context into subsequent issue-worker prompts, enabling the later model to adjust its edits; immediate steer delivery to an already-running worker is not assumed.
- Decisive coordination right: choose the conflict class and fixed warning/steer policy; deterministic Rust conditions own this local decision. Worker model later chooses concrete edits.
- Decision owner: configured deterministic supervisor logic (C); `model` setting does not instantiate a model-driven supervisor.
- Supporting / enforcement: event hub, TTL shared-context store, prompt interpolation, cooldown/dedup windows and human escalation record.
- Closure: two distinct file-edit events → overlap detection → shared warning → next issue prompt includes conflict context → worker may coordinate or repair. This is a concrete inter-S1 correction channel, not a generic mailbox alone.
- Reachability: first-party `supervisor.enabled` opt-in; disabled by default. Shipped integration test asserts overlap event and shared-context entry.
- Why not A: `supervisor.rs` makes no model call for detection, action selection or revision; `prompts/supervisor.md` is a template, not the running decision owner.
- Evidence: [supervisor file-conflict branch](https://github.com/gannonh/kata-symphony/blob/e7c160f5e4d485fdfb6d79296f56d36c8872b2a9/apps/symphony/src/supervisor.rs), [shared context returned to workers](https://github.com/gannonh/kata-symphony/blob/e7c160f5e4d485fdfb6d79296f56d36c8872b2a9/apps/symphony/src/orchestrator.rs), [two-worker integration test](https://github.com/gannonh/kata-symphony/blob/e7c160f5e4d485fdfb6d79296f56d36c8872b2a9/apps/symphony/tests/supervisor_tests.rs), [future-model config comment](https://github.com/gannonh/kata-symphony/blob/e7c160f5e4d485fdfb6d79296f56d36c8872b2a9/apps/symphony/src/domain.rs).
- Confidence: high for deterministic selected-mode channel; end-to-end worker semantic resolution unmeasured.

## S3 — Inside-and-now control

- State: —
- Function: no autonomous whole-project discretionary resource/commitment authority demonstrated within the distributed issue-worker installation.
- Disturbance: ongoing failures, retries, worker saturation, project-wide systemic error patterns and priority conflicts.
- Decisive right: operator config fixes concurrency and issue eligibility; deterministic supervisor thresholds classify repetitive errors or escalate to an operator, while tracker workflow defines existing commitments.
- Owner: operator/deployment config and worker-local models; no evidenced model/parent whole-current manager that revises cross-issue budgets, priorities or delivery commitments.
- Support: central status snapshot, worker slots, backoff, escalation registry, supervisor error-pattern events and dashboards.
- Closure boundary: fixed timeout/routing/escalation does not prove that a project-wide discretionary allocation decision is returned into issue work.
- Evidence: [orchestration logic](https://github.com/gannonh/kata-symphony/blob/e7c160f5e4d485fdfb6d79296f56d36c8872b2a9/apps/symphony/src/orchestrator.rs), [fixed supervisor pattern/escalation](https://github.com/gannonh/kata-symphony/blob/e7c160f5e4d485fdfb6d79296f56d36c8872b2a9/apps/symphony/src/supervisor.rs), [runtime configuration](https://github.com/gannonh/kata-symphony/blob/e7c160f5e4d485fdfb6d79296f56d36c8872b2a9/apps/symphony/docs/WORKFLOW-REFERENCE.md).
- Confidence: medium after bounded negative search.

### Absence scope

- Surfaces: tracker poll/dispatch/slots, task lifecycle, dashboard, optional supervisor stuck/systemic detection, reviewer/verification stages and escalation registry.
- Plausible paths: supervisor named as an agent, optional `model` field, operator steering, stage review gates and human PR approval.
- Why no material path remains: the shipped supervisor is rule-driven, status/approval channels concern local work, and no evidenced returned whole-system discretionary resource/commitment control occurs.

## S3* — Complementary audit

- State: A
- Function: challenge a coding worker's self-reported implementation/PR success through a separately invoked, read-only source/evidence inspection.
- Claim: A3 implementation manifest and draft PR correspond to the accepted A2 spec and actual source/test results.
- Ordinary reporting: implementer manifest, PR body, its own test claims and tracker state.
- Complementary access: credential-isolated A4 model reads cloned repo and exact PR diff/changed lines, not just the self-report, and emits independently chosen typed findings; optionally A5 verifier sees recorded commands and immutable evidence, then judges every criterion.
- Independence: different read-only worker context excludes push/forge/tracker credentials and repo mutation; role/invocation separation is not independently governed external audit.
- Who acts on findings: A4 findings publication and configured changes-requested route can return work to the implementation lifecycle; A5 gate blocks unsupported/failed criteria from passing.
- Decisive right and owner: separate reviewer/verifier model judges source-specific fault or criterion sufficiency; Rust validates anchors and prevents fabricated pass results but does not choose the findings.
- Closure: implementation manifest/PR → new pinned review worker reads real source/diff → findings or verification result → formal review/changed state or blocked gate → subsequent corrective worker handling. A4 automatic corrective mode is optional, while preview-only publishes evidence without assuming automatic repair.
- Reachability: `review.enabled` / `verification.enabled` configurable first-party stage coordinators and live Pi/Codex invokers; both off by default.
- Evidence: [isolated review worker](https://github.com/gannonh/kata-symphony/blob/e7c160f5e4d485fdfb6d79296f56d36c8872b2a9/apps/symphony/src/review/worker.rs), [head SHA and findings route](https://github.com/gannonh/kata-symphony/blob/e7c160f5e4d485fdfb6d79296f56d36c8872b2a9/apps/symphony/src/review/coordinator.rs), [manifest diff anchors](https://github.com/gannonh/kata-symphony/blob/e7c160f5e4d485fdfb6d79296f56d36c8872b2a9/apps/symphony/src/review/manifest.rs), [isolated verifier](https://github.com/gannonh/kata-symphony/blob/e7c160f5e4d485fdfb6d79296f56d36c8872b2a9/apps/symphony/src/verification/worker.rs), [gate computation](https://github.com/gannonh/kata-symphony/blob/e7c160f5e4d485fdfb6d79296f56d36c8872b2a9/apps/symphony/src/verification/gate.rs).
- Basis: shipped mode and typed corrective feedback contract; not an observed paid live independent challenge.
- Confidence: medium-high for configured A4 automatic mode; A5 is evidence strengthening, not independent proof of outcome quality.

## S4 — Outside-and-then intelligence

- State: —
- Function: no persistent project-wide model of future external users, frameworks or market shifts coupled to an S3 capability adaptation right.
- Disturbance: external changes may enter individual issues/spec drafts, but are treated as current implementation requirements.
- Owner/closure: issue worker/spec model can plan an individual ticket; no evidenced S4→S3 future-options bargaining or change to ongoing project capabilities.
- Supporting mechanisms: spec drafting, tracker ingestion, reusable prompt/workflow config and backlog ordering.
- Evidence: [spec coordinator](https://github.com/gannonh/kata-symphony/blob/e7c160f5e4d485fdfb6d79296f56d36c8872b2a9/apps/symphony/src/spec/coordinator.rs), [triage coordinator](https://github.com/gannonh/kata-symphony/blob/e7c160f5e4d485fdfb6d79296f56d36c8872b2a9/apps/symphony/src/triage/coordinator.rs), [workflow reference](https://github.com/gannonh/kata-symphony/blob/e7c160f5e4d485fdfb6d79296f56d36c8872b2a9/apps/symphony/docs/WORKFLOW-REFERENCE.md).
- Confidence: medium-high within reviewed deployment.

### Absence scope

- Surfaces: intake/triage, spec draft/revise, stage prompts, dashboard, runtime config, review and verification.
- Plausible paths: advanced task/spec planning, tracker reprioritization and model configuration.
- Why no material path remains: they operate on current tickets/config; there is no independently evidenced external-and-prospective alternative evaluation returned into present whole-project capability control.

## S5 — Policy and identity

- State: —
- Function: no identity-level final project-policy adjudication and operational return path established inside Symphony's packaged harness.
- Disturbance: unsafe PR publication, approval/escalation disputes and workflow policy changes.
- Owner/closure: project owner/configurator selects tracker and branch/approval rules; ordinary PR review, model prompts and escalation replies do not themselves constitute ultimate policy conflict closure.
- Supporting mechanisms: human escalation registry, credential guards, approval settings, workflow file and publication gates.
- Evidence: [escalation and worker lifecycle](https://github.com/gannonh/kata-symphony/blob/e7c160f5e4d485fdfb6d79296f56d36c8872b2a9/apps/symphony/src/orchestrator.rs), [isolation](https://github.com/gannonh/kata-symphony/blob/e7c160f5e4d485fdfb6d79296f56d36c8872b2a9/apps/symphony/src/review/worker.rs), [workflow config](https://github.com/gannonh/kata-symphony/blob/e7c160f5e4d485fdfb6d79296f56d36c8872b2a9/apps/symphony/docs/WORKFLOW-REFERENCE.md).
- Confidence: medium after bounded negative search.

### Absence scope

- Surfaces: human approvals/escalations, PR publication, stages, config, supervisor, project prompts and Kata CLI integration.
- Plausible paths: human publication approval, escalation timeout fallback, policy-like workflow metadata and repository maintainers.
- Why no material path remains: reviewed human intervention concerns task/PR execution, not an identity-level exception with legitimate ultimate-authority decision returned into project operation; maintainers sit outside this deployment boundary.

## Distributed OSS parent arrangement

The public OSS contributor team develops Symphony but is not automatically the deployed end user's VSM parent. No observed runtime channel maps a system identity or future-strategy conflict to that organization and returns its policy ruling.

## Self-hosted and non-human modes

Running Symphony headlessly or from Pi preserves issue-worker task autonomy. The optional deterministic supervisor and model audit roles remain separately classified by their actual decision owners. Enabling a human PR gate does not upgrade S5; leaving supervisor/review disabled removes the respective positive modes from that deployment.

## Recursion

Each issue worker has its own goal, repository work context, tools and tracked result, but no complete S1-through-S5 internal viability is inferred. Symphony's project-level orchestration relates those operations; stage A4/A5 reviewers are complementary role invocations rather than an automatically separate recursive organization.

## Variety and escalation

Tracker status, repository state, file-overlap detection, test results and review artifacts compress disturbances into routable signals. Actual model correction occurs in issue workers and separate audit workers; the event-driven supervisor enforces its preselected conflict/stuck patterns. Human escalations expose unresolved choices without demonstrating policy or whole-system regulatory closure by themselves.

## Evidence gaps

- No external Pi/Codex provider was run; source-level reachable ownership and deterministic tests establish supported paths, not empirical correction success.
- Positive S2 relies on enabling the supervisor and on shared-context injection into a subsequent worker prompt; its real-time `supervisor_steer` event alone is not assumed to interrupt an active worker.
- Positive S3* relies on a configured A4 read-only review mode with actionable finding routes; A4/A5 are disabled by default. A5's deterministic gate cannot be mistaken for an autonomous verifier owner.
- A developer-supplied supervisor prompt names an agent, but the running supervisor loop uses rule conditions and a `model` field documented for future decisions; no model-backed supervisor ownership is credited.
- Source review does not establish external institutional audit independence, whole-project current resource governance, future-facing capability adaptation or ultimate-policy closure.

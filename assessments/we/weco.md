---
harness_id: weco
project_name: Weco
repository: https://github.com/WecoAI/weco-cli
review_ref: edd8859cb3d15831e119ad6daef1aaa6baeca58a
reviewed_at: 2026-10-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: excluded-no-agentic-vsm
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Weco

## Review boundary

- System in focus: the pinned public weco Python CLI/client, local evaluation consumer/slots, artifact and operator/dashboard bridges; not the remote Weco optimization service.
- Purpose and identity: connect user-supplied source/evaluation commands to Weco run APIs and manage local evaluation/execution evidence.
- Relevant environment: Weco cloud API, external model/coding-agent runtimes, independently downloaded Weco skill, user code/evaluation processes and dashboard/operator requests.
- Standard-distribution boundary: the weco package and documented CLI at this exact Git ref. Backend implementation and separately installed WecoAI/weco-skill/main are not part of this frozen source.
- Credited operating / distribution surfaces: weco/optimizer.py, parallel.py, slots.py, core/api.py, artifacts.py, observe/, commands/run, commands/start and commands/setup.
- Adjacent first-party surfaces excluded from ownership: examples/benchmarks and package CI/tests; separately distributed weco-skill and hosted service. Claude Code SDK/native model/tool-loop internals and user evaluation programs cannot donate first-party ownership.
- First-party operating / deployment modes considered: serial/K-parallel run/resume/local evaluation; status/results/review/instruct/derive/stop; setup-downloaded skills; TUI/headless Claude/dashboard bridge; observe integrations and API-key modes.
- Recursion level: one public-client installation and local evaluation consumer. Remote optimization organization and external coding-agent sessions are distinct systems.
- Reviewed revision: `WecoAI/weco-cli@edd8859cb3d15831e119ad6daef1aaa6baeca58a`, frozen intake #2412 / controller #2413.
- Observation date: 2026-10-30.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

[weco/core/api.py](https://github.com/WecoAI/weco-cli/blob/edd8859cb3d15831e119ad6daef1aaa6baeca58a/weco/core/api.py) implements HTTP request methods: start_run, generate_candidate and suggest submit to the remote API, rather than implementing candidate reasoning locally. [weco/optimizer.py](https://github.com/WecoAI/weco-cli/blob/edd8859cb3d15831e119ad6daef1aaa6baeca58a/weco/optimizer.py) claims tasks, applies received files, runs the user evaluator, submits output and stores/applies best artifacts. [weco/parallel.py](https://github.com/WecoAI/weco-cli/blob/edd8859cb3d15831e119ad6daef1aaa6baeca58a/weco/parallel.py) fairly schedules isolated evaluations; [weco/slots.py](https://github.com/WecoAI/weco-cli/blob/edd8859cb3d15831e119ad6daef1aaa6baeca58a/weco/slots.py) supplies copy/worktree slots and path protection. [weco/commands/start/cli.py](https://github.com/WecoAI/weco-cli/blob/edd8859cb3d15831e119ad6daef1aaa6baeca58a/weco/commands/start/cli.py) explicitly requires the separately installed Claude Code CLI; sdk_config.py appends bridge instructions to its native preset. [weco/commands/setup/install.py](https://github.com/WecoAI/weco-cli/blob/edd8859cb3d15831e119ad6daef1aaa6baeca58a/weco/commands/setup/install.py) downloads a different repository's moving main branch. That external skill is an identified dependency, not silently adopted as evidence at this ref.

## Operational model

Recommended canonical disposition: **excluded-no-agentic-vsm**. The public client contains substantial deterministic execution and control mechanisms; its own local workers do not select semantic coding/optimization actions. The agentic generator/scorer and native coding agent are outside this source boundary. This is not a claim about whether the complete hosted Weco product is agentic or effective; its unknown/private/independently versioned internals are not assessed here.

## S1 — Operations

- State: —
- Function: No first-party autonomous operational decision/action loop in the pinned CLI distribution.
- Disturbance / variety regulated: Local evaluation workers, remote candidate/suggestion generation, the Claude SDK bridge and installed skill were checked.
- Decisive decision or feedback right: no qualifying first-party autonomous, constructor or parent-mode closure established for an included agent organization at this boundary.
- Decision owner: operator and deterministic public client; semantic optimizer/native-agent decisions reside in separate systems.
- Supporting / enforcement mechanisms: weco/core/api.py, weco/optimizer.py, weco/commands/start/cli.py, weco/commands/setup/install.py
- Closure path: Candidate generation and scoring are remote API decisions. The CLI claims received candidate file maps, executes a caller-supplied evaluation command and submits output. The bridge requires separately installed Claude Code; setup downloads WecoAI/weco-skill/main, whose contents/revision are not bundled or pinned here. Neither remote service nor external native-agent autonomy is first-party code in this assessed distribution.
- Why this is / is not agent-owned: a local executor/HTTP bridge does not acquire the remote/native system's organizational discretion by transporting it.
- Evidence: [weco/core/api.py](https://github.com/WecoAI/weco-cli/blob/edd8859cb3d15831e119ad6daef1aaa6baeca58a/weco/core/api.py); [weco/optimizer.py](https://github.com/WecoAI/weco-cli/blob/edd8859cb3d15831e119ad6daef1aaa6baeca58a/weco/optimizer.py); [weco/commands/start/cli.py](https://github.com/WecoAI/weco-cli/blob/edd8859cb3d15831e119ad6daef1aaa6baeca58a/weco/commands/start/cli.py); [weco/commands/setup/install.py](https://github.com/WecoAI/weco-cli/blob/edd8859cb3d15831e119ad6daef1aaa6baeca58a/weco/commands/setup/install.py)
- Basis: structural
- Confidence: high
- Caveats: bounded public-source exclusion; not a negative grade of the hosted product or a verdict on external skill contents.

### Absence scope

- Surfaces inspected: weco/core/api.py, weco/optimizer.py, weco/commands/start/cli.py, weco/commands/setup/install.py, README supported modes, package manifest and relevant tests.
- Plausible first-party paths checked: Local evaluation workers, remote candidate/suggestion generation, the Claude SDK bridge and installed skill were checked.
- Why no material first-party path remains: Candidate generation and scoring are remote API decisions. The CLI claims received candidate file maps, executes a caller-supplied evaluation command and submits output. The bridge requires separately installed Claude Code; setup downloads WecoAI/weco-skill/main, whose contents/revision are not bundled or pinned here. Neither remote service nor external native-agent autonomy is first-party code in this assessed distribution.

## S2 — Coordination

- State: —
- Function: No qualifying inter-S1 agent coordination at this public-client boundary.
- Disturbance / variety regulated: K-parallel scheduler fairness, isolated copy/worktree slots, claim conflicts, cancellation and working-tree consumer locks were inspected.
- Decisive decision or feedback right: no qualifying first-party autonomous, constructor or parent-mode closure established for an included agent organization at this boundary.
- Decision owner: operator and deterministic public client; semantic optimizer/native-agent decisions reside in separate systems.
- Supporting / enforcement mechanisms: weco/parallel.py, weco/slots.py, weco/consumer_lock.py
- Closure path: These materially prevent evaluation-file contamination and capacity starvation, but local workers execute supplied evaluations deterministically, not distinct first-party autonomous operational cells. Remote generator/database decisions are not imported to manufacture S1/S2 ownership.
- Why this is / is not agent-owned: a local executor/HTTP bridge does not acquire the remote/native system's organizational discretion by transporting it.
- Evidence: [weco/parallel.py](https://github.com/WecoAI/weco-cli/blob/edd8859cb3d15831e119ad6daef1aaa6baeca58a/weco/parallel.py); [weco/slots.py](https://github.com/WecoAI/weco-cli/blob/edd8859cb3d15831e119ad6daef1aaa6baeca58a/weco/slots.py); [weco/consumer_lock.py](https://github.com/WecoAI/weco-cli/blob/edd8859cb3d15831e119ad6daef1aaa6baeca58a/weco/consumer_lock.py)
- Basis: structural
- Confidence: high
- Caveats: bounded public-source exclusion; not a negative grade of the hosted product or a verdict on external skill contents.

### Absence scope

- Surfaces inspected: weco/parallel.py, weco/slots.py, weco/consumer_lock.py, README supported modes, package manifest and relevant tests.
- Plausible first-party paths checked: K-parallel scheduler fairness, isolated copy/worktree slots, claim conflicts, cancellation and working-tree consumer locks were inspected.
- Why no material first-party path remains: These materially prevent evaluation-file contamination and capacity starvation, but local workers execute supplied evaluations deterministically, not distinct first-party autonomous operational cells. Remote generator/database decisions are not imported to manufacture S1/S2 ownership.

## S3 — Inside-and-now control

- State: —
- Function: No first-party autonomous or closed parent S3 organization established within the CLI.
- Disturbance / variety regulated: Run status/overview, finite budgets, stop/instruct/derive/review requests, automatic resume and best-code application were checked.
- Decisive decision or feedback right: no qualifying first-party autonomous, constructor or parent-mode closure established for an included agent organization at this boundary.
- Decision owner: operator and deterministic public client; semantic optimizer/native-agent decisions reside in separate systems.
- Supporting / enforcement mechanisms: weco/optimizer.py, weco/core/api.py, weco/commands/run/stop.py, weco/commands/run/instruct.py
- Closure path: Client controls serialize operator requests to the remote run authority; scheduler/retry code enforces transport/capacity rules. The public source does not implement the remote organizational decision/commitment system or provide an agent actor for that function. No positive ownership mode is published for this S1-excluded support distribution.
- Why this is / is not agent-owned: a local executor/HTTP bridge does not acquire the remote/native system's organizational discretion by transporting it.
- Evidence: [weco/optimizer.py](https://github.com/WecoAI/weco-cli/blob/edd8859cb3d15831e119ad6daef1aaa6baeca58a/weco/optimizer.py); [weco/core/api.py](https://github.com/WecoAI/weco-cli/blob/edd8859cb3d15831e119ad6daef1aaa6baeca58a/weco/core/api.py); [weco/commands/run/stop.py](https://github.com/WecoAI/weco-cli/blob/edd8859cb3d15831e119ad6daef1aaa6baeca58a/weco/commands/run/stop.py); [weco/commands/run/instruct.py](https://github.com/WecoAI/weco-cli/blob/edd8859cb3d15831e119ad6daef1aaa6baeca58a/weco/commands/run/instruct.py)
- Basis: structural
- Confidence: high
- Caveats: bounded public-source exclusion; not a negative grade of the hosted product or a verdict on external skill contents.

### Absence scope

- Surfaces inspected: weco/optimizer.py, weco/core/api.py, weco/commands/run/stop.py, weco/commands/run/instruct.py, README supported modes, package manifest and relevant tests.
- Plausible first-party paths checked: Run status/overview, finite budgets, stop/instruct/derive/review requests, automatic resume and best-code application were checked.
- Why no material first-party path remains: Client controls serialize operator requests to the remote run authority; scheduler/retry code enforces transport/capacity rules. The public source does not implement the remote organizational decision/commitment system or provide an agent actor for that function. No positive ownership mode is published for this S1-excluded support distribution.

## S3* — Complementary audit

- State: —
- Function: No complementary first-party agent audit loop established.
- Disturbance / variety regulated: Evaluation output, artifact persistence, observe integration, local code review and backend scoring were considered.
- Decisive decision or feedback right: no qualifying first-party autonomous, constructor or parent-mode closure established for an included agent organization at this boundary.
- Decision owner: operator and deterministic public client; semantic optimizer/native-agent decisions reside in separate systems.
- Supporting / enforcement mechanisms: weco/parallel.py, weco/artifacts.py, weco/observe/observer.py, weco/commands/run/review.py
- Closure path: Artifacts/observability and evaluator execution are ordinary pipeline evidence. Remote scoring/review semantics are not implemented here; no separate first-party auditor gains materially different operational access and returns an independent current-control finding.
- Why this is / is not agent-owned: a local executor/HTTP bridge does not acquire the remote/native system's organizational discretion by transporting it.
- Evidence: [weco/parallel.py](https://github.com/WecoAI/weco-cli/blob/edd8859cb3d15831e119ad6daef1aaa6baeca58a/weco/parallel.py); [weco/artifacts.py](https://github.com/WecoAI/weco-cli/blob/edd8859cb3d15831e119ad6daef1aaa6baeca58a/weco/artifacts.py); [weco/observe/observer.py](https://github.com/WecoAI/weco-cli/blob/edd8859cb3d15831e119ad6daef1aaa6baeca58a/weco/observe/observer.py); [weco/commands/run/review.py](https://github.com/WecoAI/weco-cli/blob/edd8859cb3d15831e119ad6daef1aaa6baeca58a/weco/commands/run/review.py)
- Basis: structural
- Confidence: high
- Caveats: bounded public-source exclusion; not a negative grade of the hosted product or a verdict on external skill contents.

### Absence scope

- Surfaces inspected: weco/parallel.py, weco/artifacts.py, weco/observe/observer.py, weco/commands/run/review.py, README supported modes, package manifest and relevant tests.
- Plausible first-party paths checked: Evaluation output, artifact persistence, observe integration, local code review and backend scoring were considered.
- Why no material first-party path remains: Artifacts/observability and evaluator execution are ordinary pipeline evidence. Remote scoring/review semantics are not implemented here; no separate first-party auditor gains materially different operational access and returns an independent current-control finding.

## S4 — Outside-and-then intelligence

- State: —
- Function: No first-party outside-and-then adaptation organization at this client boundary.
- Disturbance / variety regulated: Feedback-to-next-candidate requests, best-artifact reuse, instructions/derive, CLI/skill update checks and external optimization claims were checked.
- Decisive decision or feedback right: no qualifying first-party autonomous, constructor or parent-mode closure established for an included agent organization at this boundary.
- Decision owner: operator and deterministic public client; semantic optimizer/native-agent decisions reside in separate systems.
- Supporting / enforcement mechanisms: weco/core/api.py, weco/optimizer.py, weco/env.py, weco/commands/setup/install.py
- Closure path: The actual proposal/evaluation/search decisions occur in the remote service or separately downloaded skill/native agent. Local code transports results, manages evaluation slots and reports versions. This does not establish a first-party prospective adaptation owner/return loop in the fixed public-client source.
- Why this is / is not agent-owned: a local executor/HTTP bridge does not acquire the remote/native system's organizational discretion by transporting it.
- Evidence: [weco/core/api.py](https://github.com/WecoAI/weco-cli/blob/edd8859cb3d15831e119ad6daef1aaa6baeca58a/weco/core/api.py); [weco/optimizer.py](https://github.com/WecoAI/weco-cli/blob/edd8859cb3d15831e119ad6daef1aaa6baeca58a/weco/optimizer.py); [weco/env.py](https://github.com/WecoAI/weco-cli/blob/edd8859cb3d15831e119ad6daef1aaa6baeca58a/weco/env.py); [weco/commands/setup/install.py](https://github.com/WecoAI/weco-cli/blob/edd8859cb3d15831e119ad6daef1aaa6baeca58a/weco/commands/setup/install.py)
- Basis: structural
- Confidence: high
- Caveats: bounded public-source exclusion; not a negative grade of the hosted product or a verdict on external skill contents.

### Absence scope

- Surfaces inspected: weco/core/api.py, weco/optimizer.py, weco/env.py, weco/commands/setup/install.py, README supported modes, package manifest and relevant tests.
- Plausible first-party paths checked: Feedback-to-next-candidate requests, best-artifact reuse, instructions/derive, CLI/skill update checks and external optimization claims were checked.
- Why no material first-party path remains: The actual proposal/evaluation/search decisions occur in the remote service or separately downloaded skill/native agent. Local code transports results, manages evaluation slots and reports versions. This does not establish a first-party prospective adaptation owner/return loop in the fixed public-client source.

## S5 — Policy and identity

- State: —
- Function: No runtime identity/ultimate-policy closure in the pinned client.
- Disturbance / variety regulated: Model/billing setup, native tool approvals, extra run instructions, user authentication and maintainer governance were inspected.
- Decisive decision or feedback right: no qualifying first-party autonomous, constructor or parent-mode closure established for an included agent organization at this boundary.
- Decision owner: operator and deterministic public client; semantic optimizer/native-agent decisions reside in separate systems.
- Supporting / enforcement mechanisms: weco/commands/start/sdk_config.py, weco/commands/start/approval_router.py, weco/commands/run/instruct.py, weco/auth.py
- Closure path: Credentials, billing, prompts and tool approvals constrain requests. They do not carry an identity/ultimate-policy issue to legitimate authority and return a governance decision. Remote account policy and the separately installed host/skill are outside the licensed source boundary.
- Why this is / is not agent-owned: a local executor/HTTP bridge does not acquire the remote/native system's organizational discretion by transporting it.
- Evidence: [weco/commands/start/sdk_config.py](https://github.com/WecoAI/weco-cli/blob/edd8859cb3d15831e119ad6daef1aaa6baeca58a/weco/commands/start/sdk_config.py); [weco/commands/start/approval_router.py](https://github.com/WecoAI/weco-cli/blob/edd8859cb3d15831e119ad6daef1aaa6baeca58a/weco/commands/start/approval_router.py); [weco/commands/run/instruct.py](https://github.com/WecoAI/weco-cli/blob/edd8859cb3d15831e119ad6daef1aaa6baeca58a/weco/commands/run/instruct.py); [weco/auth.py](https://github.com/WecoAI/weco-cli/blob/edd8859cb3d15831e119ad6daef1aaa6baeca58a/weco/auth.py)
- Basis: structural
- Confidence: high
- Caveats: bounded public-source exclusion; not a negative grade of the hosted product or a verdict on external skill contents.

### Absence scope

- Surfaces inspected: weco/commands/start/sdk_config.py, weco/commands/start/approval_router.py, weco/commands/run/instruct.py, weco/auth.py, README supported modes, package manifest and relevant tests.
- Plausible first-party paths checked: Model/billing setup, native tool approvals, extra run instructions, user authentication and maintainer governance were inspected.
- Why no material first-party path remains: Credentials, billing, prompts and tool approvals constrain requests. They do not carry an identity/ultimate-policy issue to legitimate authority and return a governance decision. Remote account policy and the separately installed host/skill are outside the licensed source boundary.

## Distributed OSS parent arrangement

Repository maintenance does not supply runtime parent governance. Local operator commands are visible client-to-service requests; no service-side function is inferred from them.

## Self-hosted and non-human modes

The local consumer can run unattended, but this is deterministic execution of remote-supplied work. Overriding WECO_BASE_URL selects another service, not an included self-hosted optimization implementation. The Claude bridge retains the native-runtime boundary.

## Recursion

Parallel evaluation jobs and run lineages do not establish recursive viability or first-party autonomous cells.

## Variety and escalation

Locks/slot isolation, cancellation, fair generation dispatch, retries, heartbeat, conflict handling and explicit errors attenuate execution/transport variety. Remote API authority and ordinary error/status channels are kept separate from organizational function ownership.

## Evidence gaps

Remote service and separately fetched skill are outside the frozen evidence boundary, so their ownership is deliberately unclassified. Native artifact-persistence tests: 15 PASS after isolated editable installation supplied required package metadata. Broader slot tests could not collect because psutil is absent; no dependency/network expansion was attempted. Python compileall PASS. No model, backend optimization request, native coding agent, account/payment action or benchmark was run.

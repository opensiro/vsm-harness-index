---
harness_id: oswald
project_name: OSWALD
repository: https://github.com/Oswald-Agent/Oswald
review_ref: 5a2d6103c4c48735a909fd5ee78b0362fcbee993
reviewed_at: 2026-10-28
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

# OSWALD

## Review boundary

- System in focus: the supported, locally invoked OSWALD Python software-engineering agent pipeline, from committed task snapshot to saved patch, evidence and terminal result; not the envisioned whole web/API/service organization.
- Purpose and identity: fulfill a local software-change request by agent-authored planning, coding, testing and review while keeping VCS publication with the human.
- Relevant environment: a user-supplied Git repository and request, model-provider responses, filesystem/worktree, Docker sandbox, tests, code quality and operator evaluation of the saved result.
- Standard-distribution boundary: first-party `python -m oswald.cli` assembly, `Orchestrator` and shipped Planner/Coder/Tester/Reviewer adapters; a Docker sandbox and provider-backed LLM are external services used by this executable mode.
- Credited operating / distribution surfaces: [CLI composition](https://github.com/Oswald-Agent/Oswald/blob/5a2d6103c4c48735a909fd5ee78b0362fcbee993/src/oswald/cli/__main__.py), [orchestrator pipeline](https://github.com/Oswald-Agent/Oswald/blob/5a2d6103c4c48735a909fd5ee78b0362fcbee993/src/oswald/core/orchestrator/pipeline.py), the four [role modules](https://github.com/Oswald-Agent/Oswald/tree/5a2d6103c4c48735a909fd5ee78b0362fcbee993/src/oswald/core/agents), artifact store, Git worktree and Docker execution adapters.
- Adjacent first-party surfaces excluded from ownership: the expressly labeled **target end-state** HTTP API, queue/worker, database/web/remote approval and deployment architecture in [docs/architecture.md](https://github.com/Oswald-Agent/Oswald/blob/5a2d6103c4c48735a909fd5ee78b0362fcbee993/docs/architecture.md); integration/development tests, CI, and unshipped planned deployment surfaces are corroboration rather than credited runtime owners.
- First-party operating / deployment modes considered: documented local provider-backed CLI with all four roles; optional saved-plan/alternative planner adapters, offline fake-agent tests and task continuation; no deployed autonomous PR/merge mode.
- Recursion level: one end-to-end software-change task as the focal operational organization; role agents are subordinate task functions, not automatically independent viable organizations at higher recursion.
- Reviewed revision: `5a2d6103c4c48735a909fd5ee78b0362fcbee993`.
- Observation date: 2026-10-28.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The CLI creates a provider-neutral LiteLLM client, assembles distinct Planner, Coder, Tester and Reviewer agents, and passes them to `Orchestrator` with an isolated worktree, artifact store and Docker sandbox. The Planner uses read-only code-search tools to write a validated `PlanSpec`; the Coder uses a model/tool loop to edit production files; the Tester is separately permitted to author tests and execute commands in the sandbox; the Reviewer receives the specification, a **fresh cumulative worktree diff**, and actual test results, then issues a separate model-authored verdict. Pydantic artifacts are validated, stored, attributed to stages, and reused for bounded correction/continuation. Approval requires clean tests and Reviewer approval; one correction attempt per invocation is allowed. The pipeline persists a patch and run report and explicitly does **not** commit, push, merge or deploy. [CLI wiring](https://github.com/Oswald-Agent/Oswald/blob/5a2d6103c4c48735a909fd5ee78b0362fcbee993/src/oswald/cli/__main__.py#L35-L100), [pipeline stages and review](https://github.com/Oswald-Agent/Oswald/blob/5a2d6103c4c48735a909fd5ee78b0362fcbee993/src/oswald/core/orchestrator/pipeline.py#L275-L366), [patch/teardown](https://github.com/Oswald-Agent/Oswald/blob/5a2d6103c4c48735a909fd5ee78b0362fcbee993/src/oswald/core/orchestrator/pipeline.py#L400-L462), [documented shipped limits](https://github.com/Oswald-Agent/Oswald/blob/5a2d6103c4c48735a909fd5ee78b0362fcbee993/README.md#L85-L120).

The design specification also sketches HTTP services, queue workers, approval endpoints and Git publication. It calls itself a **target end-state specification** and cannot substitute for the supported local CLI or establish additional S3/S4/S5 modes. The human supplies the task and retains publication authority; the runtime's stage ordering, timeouts, artifact validation and sandbox containment are enforcement/support, not agent discretionary governance.

## Operational model

The end-to-end S1 outcome is a candidate source patch supported by tests and review. A Planner model chooses specification content, Coder selects edits/tool calls, Tester selects tests/commands, and Reviewer judges adequacy and blocking issues. These roles regulate distinct phases of one task and exchange explicit artifacts. The orchestrator deterministically sequences them, bounds two coding attempts, preserves the worktree snapshot and yields `SUCCEEDED`, `STOPPED`, `FAILED` or `CANCELLED`. A human decides whether to apply/publish the patch. Distinct roles alone do not prove an S2 interference-regulation function, nor does an automated stop/timeout own S3 current-control discretion. [Pipeline interface and outcomes](https://github.com/Oswald-Agent/Oswald/blob/5a2d6103c4c48735a909fd5ee78b0362fcbee993/src/oswald/core/orchestrator/pipeline.py#L28-L116), [decision/feedback branch](https://github.com/Oswald-Agent/Oswald/blob/5a2d6103c4c48735a909fd5ee78b0362fcbee993/src/oswald/core/orchestrator/pipeline.py#L280-L385).

## S1 — Operations

- State: A
- Function: execute software-change work by interpreting a task, inspecting context, modifying code, generating/testing acceptance evidence and deciding whether the resulting patch is adequate.
- Disturbance / variety regulated: variable user requests and codebases, code/tool/test failures, ambiguous specifications and review findings.
- Decisive decision or feedback right: Planner's task plan, Coder's source edits and next tool calls, Tester's test construction/execution, and Reviewer's acceptance or blocking critique within the task.
- Decision owner: distinct provider-backed role agents invoked in the first-party shipped CLI; model responses choose content and tool actions. The deterministic orchestrator bounds the lifecycle; the human still owns final external publication.
- Supporting / enforcement mechanisms: immutable worktree base, role-scoped tools, sandbox, artifact schema/persistence, stage timeout and two-attempt cap.
- Closure path: Planner spec → Coder model/tool edits → Tester authored/executed tests → Reviewer model verdict → success or findings returned to Coder for a second attempt, or reported stop with saved patch.
- Boundary reachability: the default local CLI explicitly constructs all four agent modules and runs them through `Orchestrator`; it is not an example-only or future-service path.
- Why this is / is not agent-owned: plans, edits, tests and review judgments are model-authored; deterministic stage gates implement those decisions rather than originate task-specific discretion.
- Evidence: [CLI roles](https://github.com/Oswald-Agent/Oswald/blob/5a2d6103c4c48735a909fd5ee78b0362fcbee993/src/oswald/cli/__main__.py#L53-L83), [Planner model/tools](https://github.com/Oswald-Agent/Oswald/blob/5a2d6103c4c48735a909fd5ee78b0362fcbee993/src/oswald/core/agents/planner.py#L218-L278), [Coder tool loop](https://github.com/Oswald-Agent/Oswald/blob/5a2d6103c4c48735a909fd5ee78b0362fcbee993/src/oswald/core/agents/coder.py#L334-L430), [Tester commands](https://github.com/Oswald-Agent/Oswald/blob/5a2d6103c4c48735a909fd5ee78b0362fcbee993/src/oswald/core/agents/tester.py#L200-L293), [orchestrator corrective feedback](https://github.com/Oswald-Agent/Oswald/blob/5a2d6103c4c48735a909fd5ee78b0362fcbee993/src/oswald/core/orchestrator/pipeline.py#L290-L386).
- Basis: structural.
- Confidence: high for shipped source and decision path; no live LLM/provider run performed.
- Caveats: fake test adapters and architecture diagrams do not attest to model quality or autonomous PR publication; operator must separately inspect/apply the saved patch.

## S2 — Coordination

- State: —
- Function: no distinct inter-S1 interference-attenuation loop established at the declared one-task boundary.
- Disturbance / variety regulated: compatibility between implementation, tests and review comments, rather than independently competing S1 units with an explicit oscillation/conflict regulation relation.
- Decisive decision or feedback right: role outputs and correction findings are routed in a fixed sequence; no separately established S2 right mediates a specific inter-unit disturbance.
- Decision owner: role agents own stage-level S1 choices and the deterministic pipeline sequences handoffs.
- Supporting / enforcement mechanisms: typed artifact handoffs, stage ordering, test/review gates and bounded retry.
- Closure path: a failed test or blocked review returns to the Coder inside the same task loop, not to two or more independently active S1 units through S2 coordination.
- Why this is / is not agent-owned: four named agents and a correction edge are not evidence of a separate interference-attenuation function; no first-party inter-S1 mutual adjustment witness is supplied.
- Evidence: [fixed pipeline and retry](https://github.com/Oswald-Agent/Oswald/blob/5a2d6103c4c48735a909fd5ee78b0362fcbee993/src/oswald/core/orchestrator/pipeline.py#L275-L386), [role binding](https://github.com/Oswald-Agent/Oswald/blob/5a2d6103c4c48735a909fd5ee78b0362fcbee993/src/oswald/cli/__main__.py#L53-L83).
- Basis: structural.
- Confidence: medium-high for supported local single-task CLI.
- Caveats: separately operated Oswald processes or future web workers are outside the reviewed first-party S2 boundary.

### Absence scope

- Surfaces inspected: local CLI role composition, orchestrator/continuation, role artifacts and README's current-versus-future deployment distinction.
- Plausible first-party paths checked: stage handoffs, model reviewer feedback, retry, workspace collision avoidance and target-state background worker design.
- Why no material first-party path remains: the shipped pipeline serializes functional stages of one software task; it does not supply distinct current S1 organizations plus a concrete inter-S1 disturbance and a feedback relation that attenuates it.

## S3 — Inside-and-now control

- State: —
- Function: no first-party whole-system discretionary current-control loop over a portfolio of operational commitments/resources is established.
- Disturbance / variety regulated: stage failure, timeout, unapproved code, worktree and sandbox cleanup, not dynamic whole-system resource allocation or accountable priority conflict.
- Decisive decision or feedback right: stage progression, retry and stop conditions are fixed in code; model actors can only make task-stage decisions; the operator controls the invocation and external publication.
- Decision owner: developer predefines lifecycle/limits; orchestrator enforces them; human retains final integration decision.
- Supporting / enforcement mechanisms: run status/metrics, `stage_timeout`, two-attempt correction, sandbox isolation, report persistence, cancellation and cleanup.
- Closure path: deterministic gate/stop and report/patch return, not a discretionary whole-system current-control decision returning to alter a multi-S1 operational portfolio.
- Why this is / is not agent-owned: the central `Orchestrator` is named like a manager but its current control is a fixed single-task state machine; progress telemetry does not transfer whole-system regulatory authority to an agent.
- Evidence: [lifecycle/limits](https://github.com/Oswald-Agent/Oswald/blob/5a2d6103c4c48735a909fd5ee78b0362fcbee993/src/oswald/core/orchestrator/pipeline.py#L64-L116), [stop, retry and status](https://github.com/Oswald-Agent/Oswald/blob/5a2d6103c4c48735a909fd5ee78b0362fcbee993/src/oswald/core/orchestrator/pipeline.py#L335-L390), [recorded run/metrics](https://github.com/Oswald-Agent/Oswald/blob/5a2d6103c4c48735a909fd5ee78b0362fcbee993/src/oswald/core/orchestrator/pipeline.py#L445-L496).
- Basis: structural.
- Confidence: medium-high for current CLI boundary.
- Caveats: human patch review and planned fleet services are not S3 parent modes in the shipped pipeline.

### Absence scope

- Surfaces inspected: Orchestrator, run progress/metrics, CLI configuration, README, published patch path and target-end-state architecture.
- Plausible first-party paths checked: task admission and prioritization, retry/timeout budgets, run telemetry, task continuation, human approval and projected multi-worker current control.
- Why no material first-party path remains: no supported whole-system view plus discretionary resource/commitment arbitration and returned operational control is wired into the credited local CLI; hard limits/stop do not own that decision.

## S3* — Complementary audit

- State: A
- Function: independently examine the Coder's proposed source changes and Tester evidence for acceptance against a specification, with a blocking corrective verdict.
- Disturbance / variety regulated: silent implementation defects, self-reported completion or tests that fail to support claimed acceptance.
- Decisive decision or feedback right: the separate Reviewer model chooses `APPROVED`, `CHANGES_REQUESTED` or rejection with blocking findings against the cumulative source diff, plan and tests.
- Decision owner: `ReviewerAgent` model in the shipped role wiring; the orchestrator validates the verdict and deterministically applies the gate, rather than authoring review judgment.
- Supporting / enforcement mechanisms: fresh `manager.get_diff()` captured after Tester edits, immutable `review_changes` artifact, read-only Reviewer tool boundary, typed verdict consistency checks and correction cap.
- Closure path: cumulative worktree diff plus test evidence → distinct read-only Reviewer model judgment → orchestrator veto or returned findings → Coder correction attempt/terminal fail, with review and patch saved for human inspection.
- Boundary reachability: the default CLI always assembles and invokes `ReviewerAgent` after actual test execution; the diff is freshly read from the worktree, not merely accepted from the Coder's own completion narrative.
- Why this is / is not agent-owned: the Reviewer produces substantive model-authored blocking issues, while deterministic checks reject internally inconsistent approvals; authoring and audit roles have different inputs/permissions.
- Claim being audited: Coder's source change satisfies the Planner's specified work and is supported by tests.
- Ordinary reporting path: Coder-produced `CodeChanges` and Tester-produced `TestResults` passed into the main pipeline.
- Complementary access path: direct cumulative worktree diff via `WorktreeManager.get_diff()` and separate read-only model inspection of `spec`, `changes` and `test_results`.
- Independence boundary: Reviewer is a distinct model invocation/role with no write or tool permissions, evaluates actual patch and test artifacts rather than relying solely on Coder status; not an external independent reviewer, separate provider, or independently reexecuted tests.
- Who acts on findings: the orchestrator returns review blocks to Coder for at most one correction, or refuses success and preserves the terminal report.
- Evidence: [fresh diff and Reviewer gate](https://github.com/Oswald-Agent/Oswald/blob/5a2d6103c4c48735a909fd5ee78b0362fcbee993/src/oswald/core/orchestrator/pipeline.py#L323-L385), [read-only model-authored verdict](https://github.com/Oswald-Agent/Oswald/blob/5a2d6103c4c48735a909fd5ee78b0362fcbee993/src/oswald/core/agents/reviewer.py#L37-L148), [reviewer composition](https://github.com/Oswald-Agent/Oswald/blob/5a2d6103c4c48735a909fd5ee78b0362fcbee993/src/oswald/cli/__main__.py#L72-L83).
- Basis: structural.
- Confidence: medium for installed complementary review/feedback topology; no real provider run or measured audit efficacy.
- Caveats: audit sees produced test results and patch rather than obtaining separate runtime probes; independence is role/access separation at source level, not an organizationally independent third-party semantic review. No automatic merge authority follows.

## S4 — Outside-and-then intelligence

- State: —
- Function: no external/prospective sensing → adaptation choice → durable current-capability change loop demonstrated in the supported CLI.
- Disturbance / variety regulated: unpredictable current software task and its failing tests are handled in S1, not future technology/environment adaptation of Oswald itself.
- Decisive decision or feedback right: Planner chooses task implementation approach, not a strategic future capability portfolio; no S4 adaptation owner or returned decision is wired.
- Decision owner: user selects tasks and maintainers evolve Oswald outside assessed runtime; the agent pipeline cannot promote its patch into Oswald capability autonomously.
- Supporting / enforcement mechanisms: task plan, correction findings, saved reports/patch, model-provider configuration and developer roadmap.
- Closure path: within-task corrections may improve a candidate patch but do not produce an external-and-future adaptation judgment applied to the harness's current operational capability.
- Why this is / is not agent-owned: code planning on a supplied request and a human-applied patch are local S1 work, not S4; planned architecture is adjacent.
- Evidence: [Planner request boundary](https://github.com/Oswald-Agent/Oswald/blob/5a2d6103c4c48735a909fd5ee78b0362fcbee993/src/oswald/core/agents/planner.py#L55-L118), [no-publish pipeline](https://github.com/Oswald-Agent/Oswald/blob/5a2d6103c4c48735a909fd5ee78b0362fcbee993/src/oswald/core/orchestrator/pipeline.py#L64-L67), [future architecture disclaimer](https://github.com/Oswald-Agent/Oswald/blob/5a2d6103c4c48735a909fd5ee78b0362fcbee993/docs/architecture.md#L1-L5).
- Basis: structural.
- Confidence: high for supported local mode.
- Caveats: third-party users can ask Oswald to implement strategic tooling, but this alone does not give the harness a self-directed S4 decision loop.

### Absence scope

- Surfaces inspected: Planner/Coder/Tester/Reviewer source, CLI, saved reports and architecture roadmap; current release operating documentation.
- Plausible first-party paths checked: task planning, failure-driven correction, saved patch, model config and future API/worker roadmap.
- Why no material first-party path remains: each candidate feedback loop terminates at the user-submitted software task or manual patch handoff; no shipped external-prospective adaptation owner and return into ongoing harness capability exists.

## S5 — Policy and identity

- State: —
- Function: no supported runtime loop for ultimate purpose/identity-policy conflict and authoritative closure at the assessed recursion.
- Disturbance / variety regulated: ordinary task request constraints, sandbox restrictions and code publication risk, rather than identity/charter tensions between inside-and-now and outside-and-then.
- Decisive decision or feedback right: task constraints are supplied by the human and enforced by runtime; no identity/ultimate-policy matter is routed to a legitimate parent decision and returned as a governing choice.
- Decision owner: user/maintainers choose task, models, sandbox and external patch disposition, but their role is not a first-party closed S5 mode of the task runtime.
- Supporting / enforcement mechanisms: configuration, role prompts, task schema, tool access, test/review gates and human post-run patch review.
- Closure path: approval/denial and failure return to the local task, not a policy-identity decision governing the future purpose of Oswald.
- Why this is / is not agent-owned: fixed prompts, sandbox/tool restrictions and a human hold before Git mutation are ordinary constraints; neither agent nor parent returns a runtime identity decision.
- Evidence: [CLI config and role wiring](https://github.com/Oswald-Agent/Oswald/blob/5a2d6103c4c48735a909fd5ee78b0362fcbee993/src/oswald/cli/__main__.py#L35-L91), [README human VCS boundary](https://github.com/Oswald-Agent/Oswald/blob/5a2d6103c4c48735a909fd5ee78b0362fcbee993/README.md#L50-L71), [no commit/merge orchestration](https://github.com/Oswald-Agent/Oswald/blob/5a2d6103c4c48735a909fd5ee78b0362fcbee993/src/oswald/core/orchestrator/pipeline.py#L64-L67).
- Basis: structural.
- Confidence: medium-high for supported CLI.
- Caveats: upstream OSS maintainer governance is adjacent, and the target end-state human approval API is not credited as an installed S5 parent mode.

### Absence scope

- Surfaces inspected: CLI settings/entry, role prompts, artifact/result contracts, human publication boundary, README and architecture disclaimer.
- Plausible first-party paths checked: approval/denial, role instructions, task escalation, model configuration and proposed human/API architecture.
- Why no material first-party path remains: the supported runtime has fixed purpose and task-scoped permissions, without a function-specific identity policy matter, legitimate decisive governance owner and return-to-operation closure.

## Recursion

The reviewed unit is one local end-to-end software task with specialized role agents. An isolated worktree and a role chain are not proof of separate recursive viable systems. No fleet-wide controller or distributed organization is credited from prospective API/worker diagrams.

## Variety and escalation

The Planner/Coder/Tester/Reviewer model turns absorb task/context and test/review variety. Open planning questions, Coder escalation, nonclean tests, Reviewer rejection, timeout, cancellation and workspace/cleanup errors become explicit stop/fail reports; bounded correction may return findings to Coder. The human receives a patch for publication judgment, but this does not create a first-party S3/S4/S5 parent closure. Deterministic limits implement the guardrails without taking ownership of role decisions.

## Evidence gaps

- No live provider-backed OSWALD execution or Docker coding task was run. Source wiring and maintainer documentation are the positive evidence; fake adapters and tests are corroboration, not model-quality claims.
- Native Python dependencies were installed from the locked `uv.lock`; a deterministic `pytest tests/unit -vv -x` run passed its first 30 cases but stalled at `test_filesystem_artifact_store_lifecycle_and_versioning` and was stopped after the bounded 55-second timeout. **Do not report the 357-case unit suite as passed**. This host/filesystem observation does not itself establish a product defect or change the source-based VSM vector.
- S3* = `A` credits a structurally wired model Reviewer with separate patch access and corrective return; its substantive audit effectiveness and stronger operational independence are not demonstrated by a provider run.

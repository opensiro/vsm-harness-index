---
harness_id: hyperscale-agent-meta-harness
project_name: Hyperscale Agent Meta Harness
repository: https://github.com/aws-samples/sample-hyperscale-agent-meta-harness
review_ref: 3f80c19d2007415b97dd446f7b55d00349dc714d
reviewed_at: 2026-11-11
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: P
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# Hyperscale Agent Meta Harness

## Review boundary

- System in focus: the first-party downloadable `ham` terminal plus AWS-installed remote-run control service, Step Functions run state machine and `agentd` worker driving pinned Cline/OpenCode engines, under the documented user-deployed sample mode.
- Purpose and identity: launch and oversee independent remote coding-agent jobs in isolated Amazon Bedrock AgentCore sessions, recover failures and deliver inspectable code artifacts.
- Relevant environment: varied coding tasks and remote repository state, Bedrock availability, per-run AWS compute, operator commitments, interrupted agents, malicious dependencies, test errors and repository output.
- Standard-distribution boundary: shipped `crates/ham-core`, `crates/agentd`, `crates/harness-protocol`, AWS Step Functions/Lambda scripts and pinned adapter configurations. Provider model and Cline/OpenCode implementation supply task-level cognition, not first-party higher-recursion functions by mere co-location.
- Credited operating / distribution surfaces: `ham` multi-run dashboard and per-run interventions, deployed AgentCore task runtime and recovery, shipped clean-checkout test-report module and downloadable evidence, optional Cline lifecycle instructions.
- Adjacent first-party surfaces excluded from ownership: local developer CI, deployment scanner kits and unrelated evaluation fixtures, aspirational additional engines, standalone AWS infrastructure governance and repository maintainer review not wired into installed runs.
- Deployment modes: configured AWS account/stage with Bedrock AgentCore, Cline default or OpenCode selection, S3-only artifacts and optionally allowlisted CodeCommit pull-request delivery; clean-test report enabled by default unless explicitly disabled.
- Recursion level: multiple independent model-owned remote coding sessions (S1) within one operator-managed deployment; `ham` shows the operator current multi-run outcomes/controls. The optional Cline helper agents are not treated as first-party HAM-managed organizations.
- Reviewed revision: `3f80c19d2007415b97dd446f7b55d00349dc714d` (source-static), 2026-11-11.
- Generated Profile version: 0.2.4; Methodology version: 0.3.8.
- Current Profile version: 0.2.4; Methodology version: 0.3.8.

## Repository architecture

The terminal authenticates against a user-deployed stage and sends a task and selected model to control-api; Step Functions/AgentCore starts a separate remote engine session. `agentd` drives a pinned Cline or OpenCode through ACP, saves snapshots, retries failed model routes, classifies stop reasons and sends commit bundle/S3 zip or an allowlisted CodeCommit PR back. The provider-backed engine chooses code edits, tools and optional helpers; the HAM platform explicitly adds no independent planner or assigned roles. The operator's run list/dashboard spans ongoing jobs and offers cancel, send, retry model, resume and follow-up commands. After a successful engine stop, a separate `agentd` report hook can check the delivered head in a clean copy, running the repository's own tests as an unprivileged user and attaching an observable, bounded results report without upgrading the model's outcome label. [README architecture](https://github.com/aws-samples/sample-hyperscale-agent-meta-harness/blob/3f80c19d2007415b97dd446f7b55d00349dc714d/README.md), [test-report hook](https://github.com/aws-samples/sample-hyperscale-agent-meta-harness/blob/3f80c19d2007415b97dd446f7b55d00349dc714d/crates/agentd/src/direct/report/mod.rs).

## Operational model

Model action selection is owned by the configured Cline/OpenCode engine, not the AWS state machine. Multiple jobs can run independently in isolated microVMs. The human operator observes the shared run fleet and can revise/terminate operational commitments using first-party `ham` controls; deterministic watchdogs, guards and model fallback enforce bounded recovery. The clean-checkout test report sees a fresh materialized artifact rather than only trusting agent narration, but does not automatically judge goal satisfaction or change the stop outcome. Lifecycle prompts, research search and same-agent review are not silently promoted to autonomous S4/S3* governance.

## S1 — Operations

- State: A
- Function: choose and perform coding/project work against variable tasks using model-backed tools, with progress returned through the remote session.
- Disturbance / variety regulated: user coding requirements, changing repository/test state, tool failures, provider context and interrupted sessions.
- Decisive decision or feedback right: configured Cline/OpenCode model chooses edits, commands, tools, possible Cline helpers and task continuation from observations.
- Decision owner: external Bedrock-served model via the pinned supported engine in the shipped `agentd` adapter; first-party HAM owns transport, protection, recovery and delivery, not semantic step choice.
- Supporting / enforcement mechanisms: ACP driver, per-run AgentCore microVM, snapshots, network firewall/STS restrictions, Step Functions state, evidence package and operator UI.
- Closure path: terminal prompt → API/Step Functions → model-backed Cline/OpenCode loop in microVM → file/tool feedback and subsequent model turns → bundle and status returned to `ham`.
- Boundary reachability: the first-party deployed app selects one of two shipped engine adapters and starts a model-backed coding run with its prompt; the documented quickstart activates this path without third-party orchestration code.
- Why this is / is not agent-owned: Cline/OpenCode selects coding work with model discretion; scheduled retries, provider route rotation and AWS state transitions are deterministic infrastructure.
- Evidence: [run scope and autonomy claims](https://github.com/aws-samples/sample-hyperscale-agent-meta-harness/blob/3f80c19d2007415b97dd446f7b55d00349dc714d/README.md#L64-L94), [agentd runtime code](https://github.com/aws-samples/sample-hyperscale-agent-meta-harness/tree/3f80c19d2007415b97dd446f7b55d00349dc714d/crates/agentd/src/direct), [engine selection contracts](https://github.com/aws-samples/sample-hyperscale-agent-meta-harness/blob/3f80c19d2007415b97dd446f7b55d00349dc714d/crates/harness-protocol/src/engine_profile.rs).
- Basis: supported configured Bedrock mode, structural; confidence: high.
- Confidence: high.
- Caveats: the reviewer did not create paid AWS resources or execute a live model run; no provider output quality is claimed.

## S2 — Coordination

- State: —
- Function: no first-party relationship specifically arbitrating interaction/conflict among separate model-driven coding agents is demonstrated at the HAM multi-run recursion.
- Disturbance / variety regulated: simultaneous runs can consume AWS quotas and isolated sessions could conceptually target the same codebase, but no first-party cross-run work collision/oscillation negotiation path is shown.
- Decisive decision or feedback right: each run gets its own session and output; Step Functions sequences that run's work, not a shared agent-to-agent coordination choice.
- Decision owner: AWS services deterministically isolate jobs; Cline internally owns optional helpers outside HAM's own coordination authority.
- Supporting / enforcement mechanisms: separate microVM, run id and state machine, CodeCommit allowlists, per-run credentials, idempotency and staged delivery.
- Closure path: per-run isolation and output policies handle local state; no resolved inter-agent interference decision is returned to change two competing S1 jobs.
- Why this is / is not agent-owned: multiple simultaneous runs and Cline's optional `spawn_agent` are not evidence of a HAM-provided S2 mediator with the required conflict-specific feedback.
- Evidence: [no planner/roles and helper provenance](https://github.com/aws-samples/sample-hyperscale-agent-meta-harness/blob/3f80c19d2007415b97dd446f7b55d00349dc714d/README.md#L70-L78), [multi-run isolation](https://github.com/aws-samples/sample-hyperscale-agent-meta-harness/blob/3f80c19d2007415b97dd446f7b55d00349dc714d/README.md#L100-L140), [run orchestration](https://github.com/aws-samples/sample-hyperscale-agent-meta-harness/blob/3f80c19d2007415b97dd446f7b55d00349dc714d/crates/harness-protocol/src/orchestration.rs).
- Basis: bounded negative; confidence: medium-high.
- Confidence: medium-high.
- Caveats: an operator or external workload scheduler can coordinate projects, but no specialized inter-agent collision loop is credited to this distribution.

### Absence scope

- Surfaces inspected: README project architecture and non-goals, per-run Step Functions protocol, agentd driver, multi-run terminal/status commands and Cline helper mode.
- Plausible first-party paths checked: concurrent AgentCore jobs, shared account quotas, CodeCommit branch delivery, lifecycle packs and Cline helpers.
- Why no material first-party path remains: no shipped relation detects a concrete inter-S1 conflict and returns a coordination-specific response to both work units; tenant isolation and single-run sequencing alone are insufficient.

## S3 — Inside-and-now control

- State: P
- Function: parent-operator current oversight and intervention across the deployment's portfolio of independent running coding-agent jobs.
- Disturbance / variety regulated: stalled/paused jobs, provider outages, time/cost exposure, blocked decisions, priorities among concurrent billable runs and work that should be stopped or resumed.
- Whole-system current view: `ham runs` and its Runs screen/dashboard list the operator's running and completed jobs and states across configured backends; current run details expose phase, costs and intervention-needed conditions.
- Current-control decision scope: human operator can end an active billable run (`ham cancel`), answer/steer a blocked job, change its model route, resume paused/stalled work individually or via `resume --all`, and start bounded follow-up commitments.
- Decisive decision or feedback right: operator chooses whether to continue, cancel, restart or reassign model choice based on current fleet view; AWS status and control handlers enforce the chosen effect.
- Decision owner: authenticated terminal human operating the deployment, not the automatic model failover or Step Functions state machine.
- Supporting / enforcement mechanisms: multi-backend runs board, per-run status/usage records, IAM-authenticated control API, pause/stop/resume commands, worker control envelopes and stored snapshots.
- Closure path: run events → current Runs/dashboard views and exception messages → operator selects cancel/resume/steer/model → control API changes the active remote job or follow-up run → outcome visible on subsequent `ham` readback.
- Boundary reachability: the shipped `ham` client routes both all-runs views and named-run mutations to the deployed stage; signed operator identity and runtime control endpoints are part of the standard install.
- Why this is / is not agent-owned: discretionary intervention remains with the human parent, so `P` only. Watchdogs and model routing do not amount to autonomous S3; a single kill API alone would not suffice without fleet-wide current view and return.
- Evidence: [multi-backend Runs screen, status view](https://github.com/aws-samples/sample-hyperscale-agent-meta-harness/blob/3f80c19d2007415b97dd446f7b55d00349dc714d/docs/user-guide.md#L1885-L1910), [operator cancel and resume](https://github.com/aws-samples/sample-hyperscale-agent-meta-harness/blob/3f80c19d2007415b97dd446f7b55d00349dc714d/docs/user-guide.md#L2890-L2935), [resume-all current intervention](https://github.com/aws-samples/sample-hyperscale-agent-meta-harness/blob/3f80c19d2007415b97dd446f7b55d00349dc714d/docs/user-guide.md#L5145-L5170), [control API](https://github.com/aws-samples/sample-hyperscale-agent-meta-harness/blob/3f80c19d2007415b97dd446f7b55d00349dc714d/crates/harness-protocol/src/api/v1.rs).
- Basis: structural operator-owned parent mode; confidence: medium.
- Confidence: medium.
- Caveats: no automatic fleet-wide priority optimization or capacity bargaining is claimed; interventions are operator-chosen, mostly per run, with an optional batch resume.

## S3* — Complementary audit

- State: C
- Function: first-party audit/evidence constructor to independently rerun delivered repository tests from a clean checkout rather than merely accept the coding model's reported test success.
- Disturbance / variety regulated: an agent may report its code or tests worked while uncommitted state, working-directory assumptions, broken setup or missing services conceal actual failure.
- Claim being audited: narrow repository test/build outcome on the delivered commit, not broad user task correctness or code quality.
- Ordinary reporting path: model/Cline's own statements, its test commands and normal stop labels, which expressly carry no quality judgment.
- Complementary access path: `agentd` report hook separately checks out the finalized bundle/head in a fresh directory, independently runs repository test commands as an unprivileged test user, and stores structured command/exit/count/output evidence in an attached report.
- Independence boundary: the audit copy and test runner are owned by HAM's post-engine report module, not the agent's chat loop; nevertheless test selection may rely on project tests or lifecycle hints the agent could have changed, so truth is limited to what actually ran.
- Who acts on findings: HAM surfaces the checked test report on `ham watch`/`ham pull` and in PR evidence; the operator can independently inspect the discrepancy and issue a supported `ham continue` follow-up, but no automatic task-goal verdict or mandatory corrective feedback is asserted.
- Decisive decision or feedback right: independent test-process exit results and count summaries, made visible to the human review/continuation path; no independent autonomous judge of substantive task correctness is credited.
- Decision owner: deterministic first-party report runner owns artifact observations; human operator is the potential auditor using them. Because the report is informational and does not itself close an autonomous corrective decision, only constructor `C` is claimed.
- Supporting / enforcement mechanisms: `direct/report` post-engine hook, clean checkout, isolated test user, test-command selection, time budget, `TestReport` schema, S3 pinned evidence object and terminal/PR delivery views.
- Closure path: agent finishes and bundles HEAD → independent report hook runs tests on a clean artifact → signed/pinned report copied to delivery and shown to parent → operator may open an additional run to correct findings. The last step is operator-composable, not automatically performed.
- Boundary reachability: the shipped `agentd` `on_report` path is enabled by default, `report_tests=false` explicitly disables it, and run-session imports the report into standard delivery and client views.
- Why this is / is not agent-owned: the separate report accesses actual delivered source and test results, not model-produced narration. It does not own broader audit judgment and does not turn routine model self-review into independent S3*.
- Evidence: [post-engine report boundary and non-gating limits](https://github.com/aws-samples/sample-hyperscale-agent-meta-harness/blob/3f80c19d2007415b97dd446f7b55d00349dc714d/crates/agentd/src/direct/report/mod.rs), [fresh checkout and test execution](https://github.com/aws-samples/sample-hyperscale-agent-meta-harness/blob/3f80c19d2007415b97dd446f7b55d00349dc714d/crates/agentd/src/direct/report/run.rs), [report schema, claim bounds](https://github.com/aws-samples/sample-hyperscale-agent-meta-harness/blob/3f80c19d2007415b97dd446f7b55d00349dc714d/crates/harness-protocol/src/test_report.rs), [report and continuation in UI](https://github.com/aws-samples/sample-hyperscale-agent-meta-harness/blob/3f80c19d2007415b97dd446f7b55d00349dc714d/README.md#L145-L160).
- Basis: structural specific first-party complementary evidence constructor; confidence: medium.
- Confidence: medium.
- Caveats: report may be skipped for cancelled/timed-out runs or insufficient remaining time; tests may be agent-controlled and can be meaningless. Report expressly never gates delivery or changes the run's label; the user must supply follow-up judgment if wanted. The same Cline self-review round is excluded from independent audit.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party prospective external trend/options decision with a return into shared current capability is shown.
- Disturbance / variety regulated: changing dependency/web information and model endpoint availability are relevant to current tasks, but their handling is immediate research/failover, not organizational future adaptation.
- Decisive decision or feedback right: a model chooses web/repository research for a user task, while fixed provider fallback follows configured routes; neither chooses future business/organizational options.
- Decision owner: model's current task reasoning or deterministic route selection; no distinct S4 option owner identified.
- Supporting / enforcement mechanisms: optional AgentCore/Tavily research proxy, immutable research evidence, Bedrock model catalog, route probes and rule/skill updates.
- Closure path: research data enters active coding decisions and failover restores the current run; no evidenced external foresight → evaluated adaptation alternatives → capability change through S3.
- Why this is / is not agent-owned: internet access and durable instructions do not inherently create a prospective intelligence function, even with an agent reading them.
- Evidence: [task research capability](https://github.com/aws-samples/sample-hyperscale-agent-meta-harness/blob/3f80c19d2007415b97dd446f7b55d00349dc714d/README.md#L145-L158), [research protocol](https://github.com/aws-samples/sample-hyperscale-agent-meta-harness/blob/3f80c19d2007415b97dd446f7b55d00349dc714d/crates/harness-protocol/src/research.rs), [model failover](https://github.com/aws-samples/sample-hyperscale-agent-meta-harness/blob/3f80c19d2007415b97dd446f7b55d00349dc714d/crates/ham-core/src/failover.rs).
- Basis: bounded negative; confidence: medium-high.
- Confidence: medium-high.
- Caveats: a human could use research output strategically after the run, but no first-party S4 conversation is established here.

### Absence scope

- Surfaces inspected: research proxy, model catalog/failover, lifecycle rule packs, client controls, state machine and roadmap.
- Plausible first-party paths checked: web search, external repository download, model route switches, rule updates and long-lived run recovery.
- Why no material first-party path remains: these support immediate task adaptation, while no actor selects future-environment options and changes shared current capability as an S3–S4 relation.

## S5 — Policy and identity

- State: —
- Function: no legitimate ultimate-identity/policy adjudication loop inside the installed remote coding-agent control plane established.
- Disturbance / variety regulated: cloud credentials, allowed network hosts, third-party code checks, risky tool actions and costs are deployment security policy, not an ultimate mission conflict.
- Decisive decision or feedback right: operator selects allowlists, stages and task constraints; no first-party escalation of an identity-level conflict to a legitimate authority and back.
- Decision owner: external AWS account owner/deployer sets software policies outside a shipped S5 identity judgment function.
- Supporting / enforcement mechanisms: STS session constraints, firewall rules, CodeCommit allowlist, secret scans, lifecycle markdown and final delivery labels.
- Closure path: IAM/firewall/scan violations may block an action or artifact; no new ultimate purpose decision governs subsequent organization operations.
- Why this is / is not agent-owned: strong boundary enforcement and human control rights do not imply S5 identity governance; the parent-control S3 mode is narrower.
- Evidence: [security and IAM model](https://github.com/aws-samples/sample-hyperscale-agent-meta-harness/blob/3f80c19d2007415b97dd446f7b55d00349dc714d/README.md#L80-L105), [request policy](https://github.com/aws-samples/sample-hyperscale-agent-meta-harness/blob/3f80c19d2007415b97dd446f7b55d00349dc714d/crates/harness-protocol/src/api/v1.rs), [delivery guard](https://github.com/aws-samples/sample-hyperscale-agent-meta-harness/blob/3f80c19d2007415b97dd446f7b55d00349dc714d/crates/harness-protocol/src/evidence.rs).
- Basis: bounded negative; confidence: medium-high.
- Confidence: medium-high.
- Caveats: the AWS account and its organization may exercise higher-recursion policy externally, but that cannot be imported as a first-party S5 capability.

### Absence scope

- Surfaces inspected: operator setup, IAM, network/budget restrictions, allowed deliverables, run rule configuration and terminal control routes.
- Plausible first-party paths checked: account owner authority, model selection, rule edits, secret scans, user cancellation and security gate refusals.
- Why no material first-party path remains: observed paths regulate permissions, risks and individual commitments, not a purpose/identity dispute requiring legitimate ultimate closure.

## Distributed OSS parent arrangement

This AWS sample's maintainer governance and AWS account security organization are external to the running model platform. The user-deployed stage offers operator-owned fleet current S3, not a proven ultimate S5 authority structure.

## Self-hosted and non-human modes

An operator deploys and pays for a stage; one model-backed Cline/OpenCode agent has task choice per run. The parent can monitor multiple jobs and intervene; absent the human, deterministic failover and watchdogs are not autonomous metasystem ownership. Clean-checkout audit evidence runs without a human but requires independent judgment for broader conclusions.

## Recursion

Individual remote coding runs are autonomous work cells with their own virtual machines and environments; their association under a common operator does not establish inter-S1 S2 negotiation. Cline-internal subagents belong to the imported engine and receive no additional first-party HAM governance credit.

## Variety and escalation

Firewalls, isolated credentials, watchdog stalls, snapshots, preserved git bundles and explicit correction actions attenuate operational uncertainty. Exception messages reach the operator, who can stop/resume affected runs. Separately produced clean-test evidence preserves a narrow external check without claiming goal correctness.

## Evidence gaps

- No paid AWS stage or real Bedrock model execution was launched; source-static analysis of a pinned public sample.
- S3 parent-control claim is bounded to operator's actual current fleet view and available per-run interventions; no autonomous fleet resource optimization is claimed.
- Clean-checkout tests are not a definitive task audit and do not automatically change outcomes. No independent provider audit judge or mission/policy S5 authority is inferred.

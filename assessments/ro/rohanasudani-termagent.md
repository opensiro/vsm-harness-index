---
harness_id: rohanasudani-termagent
project_name: TermAgent
repository: https://github.com/Rohanasudani/terminal-coding-agent
review_ref: 707fa15455d34e87fb30d929669f3b1b9a9f22e0
reviewed_at: 2026-10-24
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-24
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# TermAgent

## Review boundary

- System in focus: first-party Python TermAgent terminal coding agent for one trusted local repository, including the installed CLI/interactive application, one model-directed tool loop, controller, native tools, progress and completion controls.
- Purpose and identity: carry out a user-supplied repository repair or coding task, inspect real files and test failures, plan and preview edits, execute permitted commands, and report a verifiable final diff or an explicit blocker.
- Relevant environment: unknown repository structure, failing commands, potentially stale or unsafe edits, provider errors, time and cost limits, user task requirements, and host trust constraints.
- Standard-distribution boundary: pinned `src/termagent` source and shipped CLI wiring; `OpenAICompatibleProvider` and offline fixture provider are separate providers for the same Agent loop. Human-created project config and external model inference are dependencies, not standalone metasystems.
- Credited operating / distribution surfaces: `termagent run` and `termagent app`, `TerminalAgent`, tools, safety classifier, optional task-plan and strict-completion ledger, bounded deterministic controller recovery, one provider and its observation feedback, trace and current-task verifier checks.
- Adjacent first-party surfaces excluded from ownership: independent pristine-workspace `bench`/Harbor grading, experimental campaign comparisons, dataset export, release CI, wheel checks, reports, README quality claims and maintainer product strategy. These measure or maintain the agent from outside normal coding-session control.
- First-party operating / deployment modes considered: one-shot and interactive coding tasks, live OpenAI-compatible provider or offline scripted fixture (the latter not an autonomous general coding model), suggest/never/auto command permission policies, optional planning and strict completion, Harbor adapter and separate developer evaluations.
- Recursion level: one TermAgent coding run controlling one workspace task. The interactive prompt restarts a new `TerminalAgent` for each user request; benchmark trials create independent copies for grading, not concurrently coordinated S1 cells under one running TermAgent.
- Reviewed revision: `707fa15455d34e87fb30d929669f3b1b9a9f22e0` (batch #1013 row 10), observed 2026-10-24.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The `run` CLI constructs one `AgentConfig`, then `TerminalAgent.run()`. An OpenAI-compatible model supplies one structured tool action per step; a registered file/search/code-map/patch/shell/diff tool executes it and its actual result becomes the next observation. The controller enforces scoped paths, preview hashes before writes, shell command safety, resource budgets, fresh post-write verification and bounded discovery/stagnation recovery. Optional `set_task_plan` establishes expected output paths and acceptance checks; optional `submit_completion_review` makes the *same provider* cite acceptance evidence for a deterministic completion validator. All such control is inside one S1 loop rather than a second reviewer or organization.

The project contains an unusually clear external testing boundary. Its developer `bench`, Harbor and campaign runners instantiate separate evaluation jobs and an independent `grade_workspace` with pristine tests. That grader can challenge reported task success in experiments but is **not wired as an ongoing auditor with feedback rights in the ordinary `run` or `app` coding loop**. Its fixture provider is explicitly scripted for reproducible offline regression tests, not an independently operating second LLM agent.

Pinned primary source: [README](https://github.com/Rohanasudani/terminal-coding-agent/blob/707fa15455d34e87fb30d929669f3b1b9a9f22e0/README.md), [runtime Agent](https://github.com/Rohanasudani/terminal-coding-agent/blob/707fa15455d34e87fb30d929669f3b1b9a9f22e0/src/termagent/agent.py), [model/provider](https://github.com/Rohanasudani/terminal-coding-agent/blob/707fa15455d34e87fb30d929669f3b1b9a9f22e0/src/termagent/provider.py), [tools](https://github.com/Rohanasudani/terminal-coding-agent/blob/707fa15455d34e87fb30d929669f3b1b9a9f22e0/src/termagent/tools.py), [planning](https://github.com/Rohanasudani/terminal-coding-agent/blob/707fa15455d34e87fb30d929669f3b1b9a9f22e0/src/termagent/planning.py), [completion](https://github.com/Rohanasudani/terminal-coding-agent/blob/707fa15455d34e87fb30d929669f3b1b9a9f22e0/src/termagent/completion.py), [benchmark grading](https://github.com/Rohanasudani/terminal-coding-agent/blob/707fa15455d34e87fb30d929669f3b1b9a9f22e0/src/termagent/grading.py).

## Operational model

The human chooses a coding task and execution limits; the provider observes files, errors and tool results and chooses the next operation. The controller may redirect a repeated failed-verifier call to a code-map/read step, require a patch plan after exhausted discovery, block a write without an identical preview hash, or reject an unverified completion. These are fixed recovery and quality controls, not independent agents with a separate accountable S2–S5 mandate. No live provider, LLM-agent, browser or task-quality test was run for this assessment; evidence is pinned source plus deterministic Index scripts.

## S1 — Operations

- State: A
- Function: adapt coding and investigation actions to the real target repository until an accepted change or explicit stop.
- Disturbance / variety regulated: unfamiliar code, failing tests, invalid actions, stale planned writes, verification regressions, provider delays and cost limits.
- Decisive decision or feedback right: select tool invocations, target source files, synthesize replacement code and revise task steps after returned observations.
- Decision owner: the model-backed `OpenAICompatibleProvider` running inside one `TerminalAgent` under user task and deterministic controller limits.
- Supporting / enforcement mechanisms: structured tool definitions, repository-safe tool registry, content-hash preview contract, command classifier, optional task ledger and strict evidence gate, trace and cost limits.
- Closure path: user task and repository observations → provider-selected structured tool → actual file/search/patch/test action → recorded output/error → provider's next choice or verified completion.
- Boundary reachability: normal CLI `run` and interactive `app` construct the same `TerminalAgent`, and `run()` repeatedly invokes provider `next_action` and actual tools; offline scripted fixture provider is not used as autonomy proof.
- Why this is / is not agent-owned: concrete investigation and patch-content choices originate from the model; fixed guards can reject unsafe or stale actions but do not independently author the repair.
- Evidence: [CLI composition](https://github.com/Rohanasudani/terminal-coding-agent/blob/707fa15455d34e87fb30d929669f3b1b9a9f22e0/src/termagent/cli.py), [Agent loop](https://github.com/Rohanasudani/terminal-coding-agent/blob/707fa15455d34e87fb30d929669f3b1b9a9f22e0/src/termagent/agent.py), [provider tool protocol](https://github.com/Rohanasudani/terminal-coding-agent/blob/707fa15455d34e87fb30d929669f3b1b9a9f22e0/src/termagent/provider.py), [tool execution](https://github.com/Rohanasudani/terminal-coding-agent/blob/707fa15455d34e87fb30d929669f3b1b9a9f22e0/src/termagent/tools.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: this is an implemented decision right, not evidence of live repair success; benchmark and fixture outcomes are not used to assign S1.

## S2 — Coordination

- State: —
- Function: no first-party inter-S1 mutual-interference coordination relationship is established in the running coding session.
- Disturbance / variety regulated: one agent may encounter conflicting commands, stale writes or repeated inspections, but there are no separately accountable operating cells whose actions interfere with each other.
- Distinct S1 units: `TerminalAgent.run()` manages one model provider/action stream; each interactive input instantiates a separate consecutive run. Benchmark jobs and graders are external test runs, not a standard sibling-worker organization.
- Inter-S1 disturbance: no concurrently active independently deciding pair of coding S1 units inside one deployed TermAgent.
- Attenuating coordination relation: hash-matched patch previews, verifier freshness, command classification and stagnation limits constrain one work stream, not relations between multiple units.
- Feedback into subsequent S1 behaviour: one provider sees tool errors and controller guidance; another S1 cell has no own adaptation channel.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: a sequenced set of tool calls is one agent's workflow, while external benchmark repetitions merely measure experiments.
- Decisive decision or feedback right: no separate inter-agent adjustment, negotiated lock or collision-response right found.
- Decision owner: the single coding S1 and deterministic controller; no S2 owner in reviewed standard distribution.
- Supporting / enforcement mechanisms: `AgentState`, `ProgressLedger`, `ToolRegistry`, CLI task loop, per-run trace and workspace protections.
- Closure path: local tool conflict/staleness → tool rejection/observation → same model's later correction; no distinct S1↔S1 response closure.
- Why this is / is not agent-owned: mutual S1 regulation would require two operational actors; fixed tool serialization alone is not such an owner.
- Evidence: [single Agent iteration](https://github.com/Rohanasudani/terminal-coding-agent/blob/707fa15455d34e87fb30d929669f3b1b9a9f22e0/src/termagent/agent.py), [interactive sequential loop](https://github.com/Rohanasudani/terminal-coding-agent/blob/707fa15455d34e87fb30d929669f3b1b9a9f22e0/src/termagent/interactive.py), [bench runner scope](https://github.com/Rohanasudani/terminal-coding-agent/blob/707fa15455d34e87fb30d929669f3b1b9a9f22e0/src/termagent/bench.py).
- Basis: structural bounded absence review.
- Confidence: high.
- Caveats: another program could separately run multiple TermAgent instances, but the pinned first-party coding runtime does not wire their coordination.

### Absence scope

- Surfaces inspected: model/tool loop, interactive app, CLI run, workspace write policy and benchmark/Harbor task executors.
- Plausible first-party paths checked: multiple sequential interactive prompts as a team, benchmark parallel trials as operational cells, and deterministic patch contracts as an inter-agent synchronization mechanism.
- Why no material first-party path remains: each active coding task has one provider-owned operational loop; no included concurrent sibling commitments or mutual-interference feedback contract exists.

## S3 — Inside-and-now management

- State: —
- Function: no standing independent whole-current control authority allocates live resources or resolves competing S1 commitments across an operating organization.
- Disturbance / variety regulated: task stagnation, insufficient evidence, cost and completion risks are bounded within one work session.
- Decisive decision or feedback right: fixed step/cost/transition controls redirect or terminate one task; they do not choose and rebalance multiple S1 operating mandates.
- Decision owner: user-specified `AgentConfig` limits and developer-written controller rules, not an autonomous S3 manager.
- Supporting / enforcement mechanisms: `ProgressLedger`, provider loop controller recovery, task planning, cost guard, verifier freshness and strict completion.
- Closure path: a current S1 error/repeat → deterministic guard → model observes guidance and revises work; no portfolio-level S1 performance/budget integration and corrective resource reallocation.
- Why this is / is not agent-owned: the plan is self-authored by the same coding model and validated deterministically; it does not create a separate whole-current coordination authority.
- Evidence: [controller rules](https://github.com/Rohanasudani/terminal-coding-agent/blob/707fa15455d34e87fb30d929669f3b1b9a9f22e0/src/termagent/agent.py), [progress ledger](https://github.com/Rohanasudani/terminal-coding-agent/blob/707fa15455d34e87fb30d929669f3b1b9a9f22e0/src/termagent/planning.py), [cost/limits configuration](https://github.com/Rohanasudani/terminal-coding-agent/blob/707fa15455d34e87fb30d929669f3b1b9a9f22e0/src/termagent/models.py).
- Basis: structural bounded absence review.
- Confidence: high.
- Caveats: tracking progress and blocking poor completion are substantive runtime behavior but do not independently establish a management function.

### Absence scope

- Surfaces inspected: CLI composition, current-task planning, transition/stagnation controls, tester state, cost limits and budgeted evaluation campaigns.
- Plausible first-party paths checked: per-task plan as S3, controller-selected remediation as managerial reallocations and benchmark arm orchestration as S3 over deployed workers.
- Why no material first-party path remains: no independent standing current-portfolio manager, multi-S1 mandate set or across-cell corrective allocation loop is wired.

## S3* — Independent audit

- State: —
- Function: the normal coding run does not contain an independent complementary observer with an operating audit mandate and return channel.
- Disturbance / variety regulated: erroneous model completion assertions, brittle source edits and tests with insufficient behavioral coverage are checked by deterministic local verification; independently adjudicated quality in separately run benchmarks is outside the operating recursion.
- Independently sampled reality: the agent runs the configured verifier and inspects its own final diff; separate benchmark graders sample pristine test outcomes only in external evaluation workflows.
- Complementary audit channel: `submit_completion_review` is authored by the same coding model, and `assess_completion` deterministically validates declared evidence; neither introduces independent semantic judgment or a distinct reviewer identity.
- Independence boundary: `grading.py` and Harbor graders are credibly independent from an agent's claimed result, but operate in `bench`/external trial mode, not as a first-party ongoing S3* service governing the normal `run`/`app` session.
- Who acts on findings: the same model may act on routine verifier/controller errors; bench operators analyze separate reports to maintain the product, not to correct a current live S1 via an installed audit function.
- Decisive decision or feedback right: no independent model/person/service authority to audit a current operational coding commitment and require corrective return.
- Decision owner: same `TerminalAgent`/provider for self-review; deterministic completion validator for fixed checks; external experiment evaluator belongs to adjacent development recursion.
- Supporting / enforcement mechanisms: post-write verifier freshness, expected output paths, evidence per criterion, pristine grader and campaign manifests.
- Closure path: current verifier/final diff → same coding provider and fixed completion checker → completion or retry; experimental independent grader → benchmark report → developer analysis, without a normal-runtime auditor-to-management return.
- Why this is / is not agent-owned: a separate source of ground-truth test evidence is valuable but not a separately instantiated independent S3* organizational decision function in the reviewed runtime.
- Evidence: [self-authored completion submission](https://github.com/Rohanasudani/terminal-coding-agent/blob/707fa15455d34e87fb30d929669f3b1b9a9f22e0/src/termagent/agent.py), [fixed validation](https://github.com/Rohanasudani/terminal-coding-agent/blob/707fa15455d34e87fb30d929669f3b1b9a9f22e0/src/termagent/completion.py), [external pristine grader](https://github.com/Rohanasudani/terminal-coding-agent/blob/707fa15455d34e87fb30d929669f3b1b9a9f22e0/src/termagent/grading.py), [bench wiring](https://github.com/Rohanasudani/terminal-coding-agent/blob/707fa15455d34e87fb30d929669f3b1b9a9f22e0/src/termagent/bench.py).
- Basis: explicit + structural bounded absence review.
- Confidence: high.
- Caveats: not a claim that strict verification or external grading lack utility; no live agent-quality measurements performed in this Index review.

### Absence scope

- Surfaces inspected: optional strict completion, acceptance evidence, configured post-write verifier, benchmark/Harbor grader, developer campaign and CLI interface.
- Plausible first-party paths checked: independent pristine grader as embedded S3*, same-provider structured review as independent auditor, fixed verifier as autonomous quality assessor and CI as an installed run-time auditor.
- Why no material first-party path remains: the separately independent grader belongs to experimentation, while ordinary working-loop verification and judgment remain same-provider or deterministic without an independent audit-return owner.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party prospective environmental intelligence → alternative capability selection → adapted coding organization loop is instantiated.
- Disturbance / variety regulated: provider transport failures, code changes and benchmark findings are handled by bounded retry, normal task diagnosis or developer review.
- Decisive decision or feedback right: model ID and prompt profile are configured by the user/CLI; the running agent does not select future capabilities based on outside trends or learning from campaign results.
- Decision owner: model/product configuration and later improvements belong to operator/maintainers; no agent-owned S4 strategic option authority in runtime.
- Supporting / enforcement mechanisms: user-configured model and retries, logged costs, `experiments.py` compare reports, campaign control manifests and benchmarks.
- Closure path: current request failure → bounded retry/stop exists; external campaign result → separate developer analysis exists; continual future environment sensing → proposed alternative → tested adopted capability in current runtime is not wired.
- Why this is / is not agent-owned: static model selection and one-off provider retry or benchmark reporting do not establish self-directed prospective adaptation.
- Evidence: [provider model and bounded retry](https://github.com/Rohanasudani/terminal-coding-agent/blob/707fa15455d34e87fb30d929669f3b1b9a9f22e0/src/termagent/provider.py), [run configuration](https://github.com/Rohanasudani/terminal-coding-agent/blob/707fa15455d34e87fb30d929669f3b1b9a9f22e0/src/termagent/cli.py), [comparison workflow](https://github.com/Rohanasudani/terminal-coding-agent/blob/707fa15455d34e87fb30d929669f3b1b9a9f22e0/src/termagent/experiments.py).
- Basis: structural bounded absence review.
- Confidence: high.
- Caveats: evidence-based research and frozen campaigns are developer practice, not a first-party installed S4 of one coding session.

### Absence scope

- Surfaces inspected: provider build and retry paths, configured model IDs and prompt policies, campaign comparisons, evaluation logs and optional discovery mapping.
- Plausible first-party paths checked: model retries as capability strategy, planned repair as adaptation, benchmark experiment reports as autonomous environmental foresight.
- Why no material first-party path remains: no model/strategy capability alternatives are generated and adopted by a prospective runtime decision owner.

## S5 — Policy and identity

- State: —
- Function: no current first-party ultimate-purpose controversy and legitimate adjudication/return mechanism exists at the assessed coding-session recursion.
- Disturbance / variety regulated: unsafe commands, task scope, allowed network effects and execution constraints are handled as ordinary operator configuration, not constitutional disputes over organizational identity.
- Identity / ultimate-policy issue: TermAgent's purpose is to solve a user-assigned repository coding task; a new interactive request launches another task, rather than formally revising a durable session north-star or ultimate ethos.
- Ultimate authority in each claimed mode: none claimed. Human user chooses tasks and flags; developers specify safety policy and product behavior.
- Return-to-operation path: config and permission changes can alter subsequent command execution, but no identity-level decision with first-party persistent authoritative return exists.
- Decisive decision or feedback right: accept/reject a specific high-risk command by `approval_mode`, switch model/prompt or stop a run; these are not ultimate-mission adjudications.
- Decision owner: human task issuer and maintainers at adjacent recursion; no specific S5 operating role is instantiated.
- Supporting / enforcement mechanisms: fixed command classifier, `suggest`/`auto`/`never` policy, CLI configuration, task-specific plan and session trace.
- Closure path: per-tool or per-run constraint → deterministic guard/stop → optional operator rerun; an ultimate-policy dispute → authorized adjudication → binding identity return is not shown.
- Why this is / is not agent-owned: one prompt can redefine a task, but no installed constitutional authority or durable overarching purpose revision loop results.
- Evidence: [interactive per-request new Agent](https://github.com/Rohanasudani/terminal-coding-agent/blob/707fa15455d34e87fb30d929669f3b1b9a9f22e0/src/termagent/interactive.py), [policy classifier](https://github.com/Rohanasudani/terminal-coding-agent/blob/707fa15455d34e87fb30d929669f3b1b9a9f22e0/src/termagent/safety.py), [AgentConfig](https://github.com/Rohanasudani/terminal-coding-agent/blob/707fa15455d34e87fb30d929669f3b1b9a9f22e0/src/termagent/models.py).
- Basis: structural bounded absence review.
- Confidence: high.
- Caveats: no finding is made about the repository owner's own governance outside the coding agent runtime.

### Absence scope

- Surfaces inspected: interactive task lifecycle, command approval modes, task plan, optional strict completion, configuration persistence and contributor/security documents.
- Plausible first-party paths checked: user changed instructions as S5, command permission as policy adjudication, maintainer design documentation as running-session purpose management.
- Why no material first-party path remains: no separate ultimate-purpose adjudication authority and installed governing return path are shown.

## Distributed OSS parent arrangement

Multiple installations or evaluation instances are not one supplied hierarchical agent organization. The upstream maintainers can modify TermAgent in future releases, but neither their roadmap nor experiment reports are assigned the running coding session's S2–S5 ownership.

## Self-hosted and non-human modes

The normal terminal runtime acts locally on trusted repositories and requires external sandboxing for untrusted code. `run` and `app` share one active provider/tool loop per task. Scripted fixture and containerized Harbor adapter modes are explicit test harnesses, not a new autonomous multi-agent governance topology.

## Recursion

The model/tool loop is an S1 operational cell. Planning, completion review, verifier and safety modules are components of that cell, not viable autonomous child organizations. Human or external evaluation parents can review it, but their distinct formal VSM functions are outside the first-party installed operating boundary.

## Variety and escalation

Model-driven code discovery and patches amplify task response variety; structured tool schemas, preview hashes, fresh test evidence, cost/step budgets and deterministic stagnation recovery attenuate error and risk. Operational blockages return to the same agent or user. Independent grading can challenge experimental success claims, but is not wired as continuing runtime S3* oversight.

## Evidence gaps

- Frozen code directly establishes one model-selected action loop, but no live coding-quality, reliability or model/provider/Browser trials were executed by this assessment.
- Self-authored `submit_completion_review` and deterministic criterion checking do not demonstrate an independent complementary auditing decision-maker.
- External pristine grading is useful independent evidence in developer experiments, but no normal-operation feedback channel from that grader to an S3 owner or current S1 commitment was identified.
- Optional planning, strict completion and controller recovery strengthen S1 control and verification; they are not counted as distinct S2/S3/S4 systems.
- General user-composed multi-instance orchestrations are not included without first-party configured wiring.

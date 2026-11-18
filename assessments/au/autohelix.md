---
harness_id: autohelix
project_name: AutoHelix
repository: https://github.com/awslabs/AutoHelix
review_ref: 7ccc11341f16cfaa9039945b8bcb67684dba7a34
reviewed_at: 2026-11-18
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: P
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# AutoHelix

## Review boundary

- System in focus: One installed AutoHelix project with user-declared optimization protocol and one or more model-backed work runs, first-party attempt/evaluation orchestration, optional read-only judges and optional group peers.
- Purpose and identity: Iteratively generate and validate project changes against immutable user-defined goal, editable scope and checks, preserving results and returning evidence of accepted/rejected attempts.
- Relevant environment: Project source tree and git history, external model CLI responses, test/benchmark outcomes, reviewer verdicts, run statuses, resource budgets and human selection between live/finished work.
- Standard-distribution boundary: Python package AutoHelix CLI and launcher, protocol/iteration harness, first-party copied workspaces, gates/observe/metric checks, per-run refs, viewer, hint/stop/landing controls and shipped ask/review judge adapters; Claude Code, Codex and OpenCode model/tool runtime internals are external dependencies.
- Credited operating / distribution surfaces: Supported autohelix run/resume, model-agent iteration in isolated tree, config-scoped measurement/acceptance, optional read-only judge invoked through a gate, multi-run viewer, stop/hint/manual landing and read-only group sharing.
- Adjacent first-party surfaces excluded from ownership: Repository tests, examples and CI/release, development-level CLAUDE.md, unsupplied external judge scripts, arbitrary user-created governance programs, provider backends and outer software development organization.
- First-party operating / deployment modes considered: Installed local CLI with supported configured external model coding CLI; single run with optional judge gate; optionally multiple parallel group or independent runs plus attended operator view/stop/hint/manual landing.
- Recursion level: One project optimization/engineering cell containing one or more independently iterating coding runs, with a project operator exercising shared current management.
- Reviewed revision: 7ccc11341f16cfaa9039945b8bcb67684dba7a34.
- Observation date: 2026-11-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

An editable committed protocol gives the objective, editable source scope, gate checks, metric observations and selected coding-agent CLI. The Python Harness starts each iteration from an accepted revision in a new isolated agent copy, invokes the external model-backed coding agent and freezes its resulting candidate tree. Separate evaluation copies run immutable gate commands and observations; judge commands are first-party read-only model-review agents in separate restricted checkouts. Metric gate comparisons and yes/no judge verdicts determine acceptance of a tree on the run's ref or rejection with preserved evidence for the next prompt. Runs have independent budgets, statuses, notes and accepted code. Group members only share read-only snapshots of each other's progress. The project-wide viewer exposes multiple run status/metrics; the operator can stop/hint a run or choose a checked result to land.

## Operational model

S1 is each configured model-driven coding/optimization run: the agent decides actual changes against the declared project goal and receives prior attempts, failures, reviews and measured results. A fresh first-party read-only judge, when selected in an ask gate, decides whether candidate changes satisfy a substantive question and can force rejection, creating an independent complementary current-work check. The project operator sees the current multi-run portfolio, may halt misdirected work or send a new hint and choose a checked winner to land; these parent choices change subsequent execution and committed project state. Automated metric checks enforce constraints but are not independent S3 decision owners. Group sharing by itself is not conflict attenuation.

## S1 — Operations

- State: A
- Function: Make and iteratively improve project changes with a model-selected coding strategy.
- Disturbance / variety regulated: Defects, performance or feature demands against a changing source state and observed checks.
- Decisive decision or feedback right: Choose concrete edits and iteration strategy, including using rejected patches, prior metrics and notes to decide subsequent project actions.
- Decision owner: Configured model coding agent launched and scoped by the first-party AutoHelix harness.
- Supporting / enforcement mechanisms: CLI adapter, isolated agent copy, frozen editable scope, prompt with iteration feedback, check/observe pipeline, run ref and iteration records.
- Closure path: Agent edits project copy; AutoHelix captures its tree and checks, accepts validated outcomes to the run ref or records failure, then returns metrics/rejected diffs/feedback to the next agent iteration and optionally lands accepted work.
- Boundary reachability: Shipped autohelix run/resume with a configured supported coding-agent CLI launches the operational loop; external inference is a normal dependency, not an external orchestrator replacing the installed harness.
- Why this is / is not agent-owned: The agent selects substantive code/task interventions. The host's deterministic accept/deny rules constrain the agent's decisions but do not author them.
- Evidence: [agent CLI invocation](https://github.com/awslabs/AutoHelix/blob/7ccc11341f16cfaa9039945b8bcb67684dba7a34/src/autohelix/harness.py#L618-L737), [attempt/evaluation/accept cycle](https://github.com/awslabs/AutoHelix/blob/7ccc11341f16cfaa9039945b8bcb67684dba7a34/src/autohelix/harness.py#L757-L898), [project protocol](https://github.com/awslabs/AutoHelix/blob/7ccc11341f16cfaa9039945b8bcb67684dba7a34/src/autohelix/templates/config_template.yaml#L1-L54), [iterative artifact behavior](https://github.com/awslabs/AutoHelix/blob/7ccc11341f16cfaa9039945b8bcb67684dba7a34/docs/concepts.md#L3-L30).
- Basis: structural
- Confidence: high
- Caveats: A configured functioning Claude Code/Codex/OpenCode runtime is required. This review inspected source and contract, not a paid live optimization run.

## S2 — Coordination

- State: —
- Function: No independently evidenced conflict-attenuating relation between distinct current S1 runs; group peer visibility alone does not suffice.
- Disturbance / variety regulated: Group members editing shared project source can compete for the same files or produce mutually incompatible changes.
- Decisive decision or feedback right: A coordinator would need to resolve an actual inter-run conflict or conflict-derived priority and feed an attenuating choice back to each affected S1.
- Decision owner: Group runs independently select changes and have separate budgets; no S2-specific agent/controller is instantiated by membership.
- Supporting / enforcement mechanisms: Group membership, read-only peer snapshots, notes/history, frozen scopes and independent per-run Git refs.
- Closure path: Peer code can be copied and rechecked, but no first-party conflict arbitration or coordination feedback changes both operations as a result of their interference.
- Why this is / is not agent-owned: Sharing peers' notes/refs, lock safety and manual per-run landing do not themselves establish an attenuating S2 relationship between competing S1 agents.
- Evidence: [group semantics](https://github.com/awslabs/AutoHelix/blob/7ccc11341f16cfaa9039945b8bcb67684dba7a34/docs/cli.md#L428-L453), [peer snapshots in workspace](https://github.com/awslabs/AutoHelix/blob/7ccc11341f16cfaa9039945b8bcb67684dba7a34/src/autohelix/iteration.py#L212-L245), [run isolation and conflict warning](https://github.com/awslabs/AutoHelix/blob/7ccc11341f16cfaa9039945b8bcb67684dba7a34/docs/cli.md#L315-L324)
- Basis: structural
- Confidence: medium
- Caveats: Independent user-created coordination protocols could exist but are not credited here.

### Absence scope

- Surfaces inspected: Group peer snapshot construction, parallel runs, run selection/landing, warning and scope freeze.
- Plausible first-party paths checked: Checked for explicit interference signals (overlap, resource contention, dependency failure), selected resolution and downstream S1 feedback; only read-only sharing and individual run acceptance are shipped.
- Why no material first-party path remains: Sharing peers' notes/refs, lock safety and manual per-run landing do not themselves establish an attenuating S2 relationship between competing S1 agents.

## S3 — Inside-and-now control

- State: P
- Function: Parent operator manages current project-wide work commitments and the choice of which checked output enters the branch.
- Disturbance / variety regulated: Multiple live runs can consume budget, diverge, miss targets or propose competing project results under time pressure.
- Decisive decision or feedback right: Based on the current run portfolio, select a run to stop, alter its next-iteration direction with hint, resume it later or land a chosen validated winner rather than another run.
- Decision owner: Legitimate local project operator with authority over project run commands and target Git branch.
- Supporting / enforcement mechanisms: Project-wide run table/JSON viewer with live state, cost, progress/metrics and landing status; per-run stop request, appended hint file, manual land/archival and fast-forward checks.
- Closure path: Viewer reports run state and measurements; operator stops a selected run or appends a hint consumed in its next iteration, or lands a chosen checked tip into the project; runtime returns the authoritative change into future operational runs/branch.
- Boundary reachability: Installed CLI supports view without a run ID, stop RUN_ID..., hint --run ID and land RUN_ID on that same project checkout; group comparison and manual landing are documented operating modes.
- Why this is / is not agent-owned: The operator, not the coding agent or budget checker, makes project-wide intervention and acceptance choices; autonomous S3 is not established.
- Whole-system current view: Project-wide multi-run view exposes active/finished run IDs, phase, costs, metrics, group state and checked tip's landing condition at the assessed project recursion.
- Current-control decision scope: Stop or steer currently running S1 commitments and choose between validated results; landing modifies the current project's code basis for subsequent work.
- Evidence: [project-wide viewer](https://github.com/awslabs/AutoHelix/blob/7ccc11341f16cfaa9039945b8bcb67684dba7a34/docs/cli.md#L708-L741), [stop and returned state](https://github.com/awslabs/AutoHelix/blob/7ccc11341f16cfaa9039945b8bcb67684dba7a34/docs/cli.md#L583-L633), [hint writing and next-run consumption](https://github.com/awslabs/AutoHelix/blob/7ccc11341f16cfaa9039945b8bcb67684dba7a34/src/autohelix/cli.py#L1019-L1044), [prompt hint inclusion](https://github.com/awslabs/AutoHelix/blob/7ccc11341f16cfaa9039945b8bcb67684dba7a34/src/autohelix/prompt_template.py#L172-L195), [run comparison and winner landing](https://github.com/awslabs/AutoHelix/blob/7ccc11341f16cfaa9039945b8bcb67684dba7a34/docs/cli.md#L440-L448).
- Basis: structural
- Confidence: medium
- Caveats: Parent-controlled mode applies to an attended project with multiple runs and their same-project branch; it is not an autonomous portfolio controller. The frontend is read-only; interventions are through CLI.

## S3* — Complementary audit

- State: A
- Function: Independently inspect a coding agent's candidate change against an operator-defined correctness or policy question before it is accepted.
- Disturbance / variety regulated: A coding agent can produce plausible but wrong changes, including changes gaming ordinary tests or corrupting the check substrate.
- Decisive decision or feedback right: Separate read-only model judge decides a yes/no question with evidence about the whole candidate and its diff; a no/invalid/failed gate causes the candidate's rejection and returns result details.
- Decision owner: Distinct first-party launched read-only judge model session configured via built-in ask gate. The first-party harness enforces the returned gate verdict.
- Supporting / enforcement mechanisms: Separate checked checkout of frozen candidate, independent judge system prompt, JSON answer schema, read-only tools, DirectoryGuard mutation check, stable gate configuration and per-iteration evaluation.
- Closure path: Configured ask gate calls a new judge with candidate copy, receives a structured independent verdict; gate exit status enters evaluation and rejects incorrect changes, preserving reason/patch for the next S1 attempt. The judge cannot rewrite the candidate.
- Boundary reachability: Shipped protocol supports an ask gate; autohelix ask and judge_config are built-in and invoked by the run's gate evaluator in a fresh check copy with separate authorization from the editing agent.
- Why this is / is not agent-owned: The audit judgment comes from a distinct model-run reviewer with its own instructions and read-only access. Code running fixed tests is additional enforcement, not the basis of positive S3*.
- Claim being audited: Whether the coding agent's changed code satisfies the selected question (e.g. API compatibility or correctness) without altering the check target.
- Ordinary reporting path: Editing agent's final output, change summary and gate/benchmark observations used to select progress.
- Complementary access path: Independent judge's fresh, read-only candidate snapshot and complete diff; no producer conversation or agent-owned notes are supplied to the judge.
- Independence boundary: Distinct judge process, system instructions and model call, immutable candidate snapshot, read-only tools and file mutation guard; optional distinct model family. The configured human question scopes what is audited.
- Who acts on findings: Harness check gate rejects a no/failed verdict, and S1 receives rejected attempt reason/patch; project operator sees gate output through the viewer.
- Evidence: [built-in configurable ask gate](https://github.com/awslabs/AutoHelix/blob/7ccc11341f16cfaa9039945b8bcb67684dba7a34/src/autohelix/templates/config_template.yaml#L20-L30), [judge isolation and read-only agent](https://github.com/awslabs/AutoHelix/blob/7ccc11341f16cfaa9039945b8bcb67684dba7a34/src/autohelix/judge.py#L4-L26), [question and read-only config](https://github.com/awslabs/AutoHelix/blob/7ccc11341f16cfaa9039945b8bcb67684dba7a34/src/autohelix/judge.py#L63-L126), [actual judge run and write guard](https://github.com/awslabs/AutoHelix/blob/7ccc11341f16cfaa9039945b8bcb67684dba7a34/src/autohelix/judge.py#L267-L358), [candidate evaluation/rejection](https://github.com/awslabs/AutoHelix/blob/7ccc11341f16cfaa9039945b8bcb67684dba7a34/src/autohelix/harness.py#L940-L1029), [documented reviews versus gates](https://github.com/awslabs/AutoHelix/blob/7ccc11341f16cfaa9039945b8bcb67684dba7a34/docs/concepts.md#L271-L310).
- Basis: structural
- Confidence: high
- Caveats: This positive is mode-specific: requires an installed judge-compatible provider (Claude Code or Codex) and an operator-defined ask gate; without one, ordinary deterministic checks and optional non-gating reviews cannot be credited as S3*. A read-only LLM reviewer is fallible.

## S4 — Outside-and-then intelligence

- State: —
- Function: No distinct outside-and-future strategic sensing and system-capability adaptation loop is demonstrated.
- Disturbance / variety regulated: An evolving external environment could make project goals, provider strategy or constraints obsolete.
- Decisive decision or feedback right: An S4 actor would identify external prospective distinctions and author a new capability or strategic direction that is applied to later operations.
- Decision owner: Model agent improves current code under a static user-defined goal; operator may initiate a fresh run, not a shipped distinct S4 pathway.
- Supporting / enforcement mechanisms: Metrics, previous review counts, agent notes, group sharing, model feedback, run import and project protocol.
- Closure path: The next iteration improves the current goal and consumes prior results, but no outside-future signal is translated into an authoritative capability adaptation.
- Why this is / is not agent-owned: Iterative performance improvement and use of previous reviews are S1 improvement under current intent, not evidence of prospective environmental intelligence and returned S4.
- Evidence: [iteration feedback](https://github.com/awslabs/AutoHelix/blob/7ccc11341f16cfaa9039945b8bcb67684dba7a34/docs/concepts.md#L3-L29), [review previous state](https://github.com/awslabs/AutoHelix/blob/7ccc11341f16cfaa9039945b8bcb67684dba7a34/docs/concepts.md#L304-L351), [config protocol](https://github.com/awslabs/AutoHelix/blob/7ccc11341f16cfaa9039945b8bcb67684dba7a34/src/autohelix/templates/config_template.yaml#L10-L54)
- Basis: structural
- Confidence: medium
- Caveats: A user could design an S4-specific goal in a custom protocol; no shipped universal S4 decision owner is inferred.

### Absence scope

- Surfaces inspected: Iteration prompt feedback, review/observe, groups/imported runs, run metadata and CLI protocol settings.
- Plausible first-party paths checked: Sought environmental scanning plus future distinction, adaptation option and actual return into current organizational capabilities beyond refining the original goal.
- Why no material first-party path remains: Iterative performance improvement and use of previous reviews are S1 improvement under current intent, not evidence of prospective environmental intelligence and returned S4.

## S5 — Policy and identity

- State: —
- Function: The configured goal/scope/gates govern an optimization task but do not demonstrate a distinct ultimate policy or identity-issue decision function at the project-system recursion.
- Disturbance / variety regulated: Project-wide identity constraints and organizational mandates might conflict with locally chosen optimization goals.
- Decisive decision or feedback right: A legitimate S5 authority would adjudicate a distinct identity/ultimate-policy issue and return a binding decision governing project operations.
- Decision owner: Human project owner authors goals and acceptance thresholds, but no distinct S5 policy-issue review/decision path is established by the shipped harness.
- Supporting / enforcement mechanisms: Committed YAML goal, editable/frozen scope, test gates, budget, landing choice and operator run commands.
- Closure path: A new run copies the chosen protocol and enforces its constraints; no identity-policy conflict decision and returned ultimate mandate is operationally established.
- Why this is / is not agent-owned: A static task contract and config immutability are important constraints, but are not alone a first-party policy/identity closure process.
- Evidence: [protocol goal/scope/gates](https://github.com/awslabs/AutoHelix/blob/7ccc11341f16cfaa9039945b8bcb67684dba7a34/src/autohelix/templates/config_template.yaml#L9-L51), [immutability and run selection](https://github.com/awslabs/AutoHelix/blob/7ccc11341f16cfaa9039945b8bcb67684dba7a34/src/autohelix/harness.py#L198-L260), [gate contract](https://github.com/awslabs/AutoHelix/blob/7ccc11341f16cfaa9039945b8bcb67684dba7a34/src/autohelix/harness.py#L940-L968)
- Basis: structural
- Confidence: medium
- Caveats: Parent ownership of the external team's ultimate policy is not denied; it remains outside this task-level contract.

### Absence scope

- Surfaces inspected: YAML configuration, guardrails, runtime protocol, CLI setup assistant, human selection and branch land.
- Plausible first-party paths checked: Checked for actual ultimate-policy dispute/mandate owner/decision/returned governed operation distinct from operating-task configuration.
- Why no material first-party path remains: A static task contract and config immutability are important constraints, but are not alone a first-party policy/identity closure process.

## Distributed OSS parent arrangement

The Amazon/open-source contributor and release organization does not govern each installed project's runtime identity or control through a shipped path. The evaluated parent S3 is the legitimate owner of the local project who can inspect and alter its current run portfolio; no OSS maintainer approval is borrowed as runtime S5.

## Self-hosted and non-human modes

AutoHelix is locally executable with a supported external agent CLI. Agentic S1 and audit-judge S3* require a model session; the budget/metric gates are deterministic checks. A human parent can intervene using shipped CLI/project view, while autonomous portfolio governance is not claimed. Groups of agents can learn from each other's snapshots, but members are not a metasystem by default.

## Recursion

Each optimization run is an S1 operating unit at the selected project recursion. Separate judge calls are independent candidate assurance, not standalone project delivery units. The project operator can manage multiple runs; groups share context without creating a proven S2-specific arbitration structure.

## Variety and escalation

Model-driven edits address arbitrary workspace variety. Immutable scope and checks reject invalid changes; read-only judge assesses complementary evidence and rejects when configured. Multi-run metric status escalates to a parent who can change current commitments, attach hints or select a checked winner; larger policy and strategic adaptation remain external to the demonstrated operating boundary.

## Evidence gaps

Source-first pinned inspection only; no paid model or judge calls were made, and no independent second semantic reviewer confirmed the optional role separation. Negative states are bounded to the documented standard distribution and inspected sources, not all possible user-composed protocols. Dynamic concurrent-run conflict-resolution behavior beyond first-party sharing, and higher recursion identity-setting, remain outside positive claims.

---
harness_id: ainz
project_name: Ainz
repository: https://github.com/wess/ainz
review_ref: 26e02248344307679d510593138c9eb9601feb9e
reviewed_at: 2026-11-18
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: C
autonomy_s4: ?
autonomy_s5: —
---

# Ainz

## Review boundary

- System in focus: The installed Ainz coding harness including its CLI, agent library, optional named children and shipped opt-in improvement mode.
- Purpose and identity: Run workspace-directed tasks with model-selected tools and optionally evaluate proposed improvements to the installed harness.
- Relevant environment: Workspace files, user task stream, tool outputs, configured providers, installed skills and local operator decisions.
- Standard-distribution boundary: Shipped application, Rust agent runtime and opt-in experiment and evaluation modules. A connected Synapse service and independently authored plugins remain dependencies.
- Credited operating / distribution surfaces: [README.md](https://github.com/wess/ainz/blob/26e02248344307679d510593138c9eb9601feb9e/README.md), [src/main.rs](https://github.com/wess/ainz/blob/26e02248344307679d510593138c9eb9601feb9e/src/main.rs), [src/agent.rs](https://github.com/wess/ainz/blob/26e02248344307679d510593138c9eb9601feb9e/src/agent.rs), [src/agent/step.rs](https://github.com/wess/ainz/blob/26e02248344307679d510593138c9eb9601feb9e/src/agent/step.rs), [src/subagent.rs](https://github.com/wess/ainz/blob/26e02248344307679d510593138c9eb9601feb9e/src/subagent.rs), [docs/improve.md](https://github.com/wess/ainz/blob/26e02248344307679d510593138c9eb9601feb9e/docs/improve.md), [src/command/improve/perform.rs](https://github.com/wess/ainz/blob/26e02248344307679d510593138c9eb9601feb9e/src/command/improve/perform.rs), [src/eval/mod.rs](https://github.com/wess/ainz/blob/26e02248344307679d510593138c9eb9601feb9e/src/eval/mod.rs)
- Adjacent first-party surfaces excluded from ownership: Repository CI, exploratory manual evaluations and third-party service internals. The fixed behavioral evaluator is credited only where the normal improvement command invokes it.
- First-party operating / deployment modes considered: Interactive CLI, configured provider, one-shot and embedded agent loop, named child dispatch, optional Synapse connection and improvement review/acceptance.
- Recursion level: One installed harness operating the workspace with optional child runs. The improvement audit is mapped at the same installed harness boundary.
- Reviewed revision: `26e02248344307679d510593138c9eb9601feb9e`
- Observation date: 2026-11-18
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The Rust Agent implements tool-mediated turns, session state and a turn-state machine. Named children inherit runtime limits and may have narrower tools and distinct provider-model choices. The opt-in improvement worker evaluates baseline and candidate snapshots, recording a report and proposed skills for an operator decision.

## Operational model

The model chooses tools or stops. Ainz feeds call outputs to the model and permits operator steering or cancellation. A saved run can cause an enrolled workspace to launch an experiment. Candidate source and skills are reviewed with independent fixed probes before they can be accepted.

## S1 — Operations

- State: A
- Function: Operational task execution
- Disturbance / variety regulated: Requests, workspace state and tool feedback
- Decisive decision or feedback right: Choose the next workspace action and whether to answer or continue
- Decision owner: The model-backed session or named child agent
- Supporting / enforcement mechanisms: Provider adapter, tool registry, permission hooks and step machine
- Closure path: The results of tool calls reenter the model turn and the session retains state
- Boundary reachability: The shipped CLI and embedded API both invoke the Agent; named children invoke the same core with constrained options.
- Why this is / is not agent-owned: The model selects task actions and follow-ups. The runtime returns observations and enforces configured constraints.
- Evidence: [src/main.rs](https://github.com/wess/ainz/blob/26e02248344307679d510593138c9eb9601feb9e/src/main.rs), [src/agent.rs](https://github.com/wess/ainz/blob/26e02248344307679d510593138c9eb9601feb9e/src/agent.rs), [src/agent/step.rs](https://github.com/wess/ainz/blob/26e02248344307679d510593138c9eb9601feb9e/src/agent/step.rs), [src/subagent.rs](https://github.com/wess/ainz/blob/26e02248344307679d510593138c9eb9601feb9e/src/subagent.rs)
- Basis: Bounded inspection of pinned shipped implementation, manifests and operating instructions.
- Confidence: Medium-high within this boundary.
- Caveats: Source-only review of the declared operating surface.

## S2 — Coordination

- State: —
- Function: Attenuation of interference between distinct S1 units
- Disturbance / variety regulated: Potential concurrent workspace edits or overlapping work between child runs
- Decisive decision or feedback right: No first-party interference arbitration is supplied by the inspected child and mesh paths
- Decision owner: No qualifying owner shown
- Supporting / enforcement mechanisms: Named roles, collect/list commands, per-name task registry and optional peer messaging
- Closure path: Collected observations return to the parent agent; the mesh delivers messages
- Why this is / is not agent-owned: Dispatch, waiting and relaying can carry a coordination decision, but the installed logic does not decide a remedy for overlapping operational commitments.
- Evidence: [docs/agents.md](https://github.com/wess/ainz/blob/26e02248344307679d510593138c9eb9601feb9e/docs/agents.md), [src/subagent.rs](https://github.com/wess/ainz/blob/26e02248344307679d510593138c9eb9601feb9e/src/subagent.rs), [src/synapse.rs](https://github.com/wess/ainz/blob/26e02248344307679d510593138c9eb9601feb9e/src/synapse.rs), [docs/mcp.md](https://github.com/wess/ainz/blob/26e02248344307679d510593138c9eb9601feb9e/docs/mcp.md)
- Basis: Bounded inspection of pinned shipped implementation, manifests and operating instructions.
- Confidence: Medium-high within this boundary.
- Caveats: Source-only review of the declared operating surface.

### Absence scope

- Surfaces inspected: [docs/agents.md](https://github.com/wess/ainz/blob/26e02248344307679d510593138c9eb9601feb9e/docs/agents.md), [src/subagent.rs](https://github.com/wess/ainz/blob/26e02248344307679d510593138c9eb9601feb9e/src/subagent.rs), [src/synapse.rs](https://github.com/wess/ainz/blob/26e02248344307679d510593138c9eb9601feb9e/src/synapse.rs), [docs/mcp.md](https://github.com/wess/ainz/blob/26e02248344307679d510593138c9eb9601feb9e/docs/mcp.md)
- Plausible first-party paths checked: Check whether collecting a child, child naming, narrower role permissions or Synapse addressing resolves overlapping workspace work.
- Why no material first-party path remains: These paths return individual work and messages or constrain a role. No supplied cross-child conflict witness and corrective result are wired into subsequent child work.

## S3 — Inside-and-now control

- State: —
- Function: Whole-system current direction and resource or commitment intervention
- Disturbance / variety regulated: Potential contention for child capacity or workspace-wide active commitments
- Decisive decision or feedback right: No supplied organization-wide commitment or resource decision
- Decision owner: The caller selects a child task and options; the operator can steer or cancel a run
- Supporting / enforcement mechanisms: Run control, child roster, per-child model and turn limits, experiment budget
- Closure path: Steering/cancellation affects the selected run; child collection returns a result
- Why this is / is not agent-owned: Current choices regulate local task delegation and individual run limits. The roster displays state without a shared commitment intervention loop.
- Evidence: [src/control.rs](https://github.com/wess/ainz/blob/26e02248344307679d510593138c9eb9601feb9e/src/control.rs), [src/subagent.rs](https://github.com/wess/ainz/blob/26e02248344307679d510593138c9eb9601feb9e/src/subagent.rs), [docs/interface.md](https://github.com/wess/ainz/blob/26e02248344307679d510593138c9eb9601feb9e/docs/interface.md), [docs/agents.md](https://github.com/wess/ainz/blob/26e02248344307679d510593138c9eb9601feb9e/docs/agents.md), [src/improve/automatic.rs](https://github.com/wess/ainz/blob/26e02248344307679d510593138c9eb9601feb9e/src/improve/automatic.rs)
- Basis: Bounded inspection of pinned shipped implementation, manifests and operating instructions.
- Confidence: Medium-high within this boundary.
- Caveats: Source-only review of the declared operating surface.

### Absence scope

- Surfaces inspected: [src/control.rs](https://github.com/wess/ainz/blob/26e02248344307679d510593138c9eb9601feb9e/src/control.rs), [src/subagent.rs](https://github.com/wess/ainz/blob/26e02248344307679d510593138c9eb9601feb9e/src/subagent.rs), [docs/interface.md](https://github.com/wess/ainz/blob/26e02248344307679d510593138c9eb9601feb9e/docs/interface.md), [docs/agents.md](https://github.com/wess/ainz/blob/26e02248344307679d510593138c9eb9601feb9e/docs/agents.md), [src/improve/automatic.rs](https://github.com/wess/ainz/blob/26e02248344307679d510593138c9eb9601feb9e/src/improve/automatic.rs)
- Plausible first-party paths checked: Trace roster plus steering, model allocation per child and persistent experiment scheduling.
- Why no material first-party path remains: Child selection and cancellation are run-scoped. Experiment slots are preselected technical constraints. No whole-current portfolio allocation/priority closure was evidenced.

## S3* — Complementary audit

- State: C
- Function: Complementary evaluation of whether a candidate improvement preserves operational behavior before adoption.
- Disturbance / variety regulated: A repair agent claims an experimental source/skill bundle improves the harness despite incomplete or misleading reported results
- Decisive decision or feedback right: Compare reported success with artifact-based behavioral probes and use the independent decision path to constrain adoption
- Decision owner: In the stock path, fixed grading rules and the user reviewing the identified report. An embedding host can attach an autonomous audit judgment to the exposed independent report/check APIs.
- Supporting / enforcement mechanisms: Baseline and candidate source copies, fixed host-owned fixture probes and drift guards
- Closure path: A failing behavioral case leaves the bundle inadmissible; an embedding host receives the report and acceptance predicates for follow-up control
- Boundary reachability: The documented improvement command calls the bundled evaluator before approve. The public improve and eval modules expose baseline and candidate evaluation, acceptable verdict and review/approval for an embedding host.
- Why this is / is not agent-owned: An independently probing first-party decision surface exists. The ship supplies fixed tests and operator acceptance. Autonomous audit judgment at this scope requires composition by the embedding host.
- Evidence: [docs/improve.md](https://github.com/wess/ainz/blob/26e02248344307679d510593138c9eb9601feb9e/docs/improve.md), [src/command/improve/perform.rs](https://github.com/wess/ainz/blob/26e02248344307679d510593138c9eb9601feb9e/src/command/improve/perform.rs), [src/improve/behavior.rs](https://github.com/wess/ainz/blob/26e02248344307679d510593138c9eb9601feb9e/src/improve/behavior.rs), [src/eval/grade.rs](https://github.com/wess/ainz/blob/26e02248344307679d510593138c9eb9601feb9e/src/eval/grade.rs), [src/improve/review.rs](https://github.com/wess/ainz/blob/26e02248344307679d510593138c9eb9601feb9e/src/improve/review.rs)
- Basis: Bounded inspection of pinned shipped implementation, manifests and operating instructions.
- Confidence: Medium-high within this boundary.
- Caveats: This is the opt-in improvement gate. It does not audit general coding-task completion, and the fixed case suite is narrow.

- Claim being audited: The proposed source/skill bundle preserves required behavior.
- Ordinary reporting path: The repair agent's output, session report and candidate checks.
- Complementary access path: The harness-owned evaluator exercises frozen tasks and probes files and blocked decisions in a fresh workspace.
- Independence boundary: Fixtures and scoring are outside the candidate checkout, and changes to evaluated context and prior checks block approval.
- Who acts on findings: The runtime evaluator vetoes acceptance on failing cases and the operator or composed audit consumer acts on the reviewed report.

## S4 — Outside-and-then intelligence

- State: ?
- Function: External, prospective intelligence and adopted capability adaptation
- Disturbance / variety regulated: Future changes in user tasks, required behaviors or provider/tool conditions
- Decisive decision or feedback right: Generate and authorize a prospective capability change informed by evidence from outside current operation
- Decision owner: The improvement worker proposes a patch or skill; a local operator approves it before rebuild or next discovery
- Supporting / enforcement mechanisms: Saved workspace run excerpts, baseline/candidate comparison, timed worker and artifact review
- Closure path: Accepted skills can enter later sessions; accepted source requires rebuild
- Why this is / is not agent-owned: The owner and adoption path are reconstructable, but the reviewed trigger and excerpts are mainly retrospective and the fixed probes do not establish a continuing external and prospective sensing function.
- Evidence: [docs/improve.md](https://github.com/wess/ainz/blob/26e02248344307679d510593138c9eb9601feb9e/docs/improve.md), [src/improve/evidence.rs](https://github.com/wess/ainz/blob/26e02248344307679d510593138c9eb9601feb9e/src/improve/evidence.rs), [src/improve/mod.rs](https://github.com/wess/ainz/blob/26e02248344307679d510593138c9eb9601feb9e/src/improve/mod.rs), [src/improve/review.rs](https://github.com/wess/ainz/blob/26e02248344307679d510593138c9eb9601feb9e/src/improve/review.rs), [src/eval/cases.rs](https://github.com/wess/ainz/blob/26e02248344307679d510593138c9eb9601feb9e/src/eval/cases.rs)
- Basis: Bounded inspection of pinned shipped implementation, manifests and operating instructions.
- Confidence: Insufficient for a positive S4 claim.
- Caveats: The supported improvement loop is materially relevant; saved sessions can contain external user demand. A repeated path coupling changing demands to prospective alternatives was not corroborated.

## S5 — Policy and identity

- State: —
- Function: Resolution and return of ultimate identity or policy decisions
- Disturbance / variety regulated: Changes to the system's enduring purpose or ultimate rules
- Decisive decision or feedback right: No runtime standing mandate resolution and return loop shown
- Decision owner: Local operator/developer selects instructions, model, permission rules and optional integration
- Supporting / enforcement mechanisms: Settings, workspace instructions, named agent definitions and plugin configuration
- Closure path: Loader and gates apply configured constraints to later calls
- Why this is / is not agent-owned: Configured rules and individual improvement approval do not adjudicate conflicts over the harness's ultimate identity.
- Evidence: [README.md](https://github.com/wess/ainz/blob/26e02248344307679d510593138c9eb9601feb9e/README.md), [docs/permissions.md](https://github.com/wess/ainz/blob/26e02248344307679d510593138c9eb9601feb9e/docs/permissions.md), [docs/agents.md](https://github.com/wess/ainz/blob/26e02248344307679d510593138c9eb9601feb9e/docs/agents.md), [src/permission.rs](https://github.com/wess/ainz/blob/26e02248344307679d510593138c9eb9601feb9e/src/permission.rs), [src/improve/review.rs](https://github.com/wess/ainz/blob/26e02248344307679d510593138c9eb9601feb9e/src/improve/review.rs)
- Basis: Bounded inspection of pinned shipped implementation, manifests and operating instructions.
- Confidence: Medium-high within this boundary.
- Caveats: Source-only review of the declared operating surface.

### Absence scope

- Surfaces inspected: [README.md](https://github.com/wess/ainz/blob/26e02248344307679d510593138c9eb9601feb9e/README.md), [docs/permissions.md](https://github.com/wess/ainz/blob/26e02248344307679d510593138c9eb9601feb9e/docs/permissions.md), [docs/agents.md](https://github.com/wess/ainz/blob/26e02248344307679d510593138c9eb9601feb9e/docs/agents.md), [src/permission.rs](https://github.com/wess/ainz/blob/26e02248344307679d510593138c9eb9601feb9e/src/permission.rs), [src/improve/review.rs](https://github.com/wess/ainz/blob/26e02248344307679d510593138c9eb9601feb9e/src/improve/review.rs)
- Plausible first-party paths checked: Inspect standing permissions, named child inheritance, Synapse SOUL configuration and approval of a frozen improvement artifact.
- Why no material first-party path remains: These surfaces load constraints or consent to concrete artifacts. No supplied deliberation or escalation path resolves a constitutional policy issue and returns that decision.

## Recursion

Named agents execute distinct tasks with bounded tools and durable sessions. Their spawn/collect relationship does not by itself establish a recursively viable organization.

## Variety and escalation

Run steering, operator approvals, constrained role options and bounded experiments attenuate work variety. A rejected experiment retains its report for inspection.

## Evidence gaps

No live model or plugin evaluation was conducted. External-to-prospective sensing coupled to the optional improvement worker was unresolved. Synapse-internal decisions were excluded.

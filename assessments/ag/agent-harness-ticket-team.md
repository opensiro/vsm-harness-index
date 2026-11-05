---
harness_id: agent-harness-ticket-team
project_name: Agent Harness (ticket team)
repository: https://github.com/bondie/agent-harness
review_ref: 6c011629ecf3f0cb2cfd72084502e58a31ad3206
reviewed_at: 2026-11-05
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

# Agent Harness (ticket team)

## Review boundary

- System in focus: The first-party `agent-harness` Claude Code ticket-team plugin: its installed `/agent-harness:ticket` skill, four defined subagents and two configured hook scripts, acting on one ticket in a developer's target repository.
- Purpose and identity: Analyse a tracker ticket, forecast effort from precedent, obtain human approval, implement bounded code changes, independently review them, and hand control back to a human before external writes.
- Relevant environment: Human requester, ticket tracker/MCP, target Git repository and tests, precedent search service, Claude Code plugin host/model/subagent interface and untrusted ticket text.
- Standard-distribution boundary: The plugin installed by documented marketplace command, the first-party `skills/ticket/SKILL.md`, `agents/*.md`, `hooks/hooks.json` and hook scripts. The separate Python estimator backtest/evaluation CLI is not a live ticket-team decision loop.
- Credited operating / distribution surfaces: [installed skill](https://github.com/bondie/agent-harness/blob/6c011629ecf3f0cb2cfd72084502e58a31ad3206/skills/ticket/SKILL.md), [implementer](https://github.com/bondie/agent-harness/blob/6c011629ecf3f0cb2cfd72084502e58a31ad3206/agents/implementer.md), [reviewer QA](https://github.com/bondie/agent-harness/blob/6c011629ecf3f0cb2cfd72084502e58a31ad3206/agents/reviewer-qa.md), [hook registration](https://github.com/bondie/agent-harness/blob/6c011629ecf3f0cb2cfd72084502e58a31ad3206/hooks/hooks.json), [test hook](https://github.com/bondie/agent-harness/blob/6c011629ecf3f0cb2cfd72084502e58a31ad3206/hooks/run_tests.py), [tracker guard](https://github.com/bondie/agent-harness/blob/6c011629ecf3f0cb2cfd72084502e58a31ad3206/hooks/guard_tracker_writes.py).
- Adjacent first-party surfaces excluded from ownership: Offline backtesting and estimator evaluation, project-development CI, and internal Claude Code or ticket-precedent MCP functionality not implemented or wired by this plugin. Installed role prompts are instructions to a host, not proof of observed live runs.
- First-party operating / deployment modes considered: Ticket analysis and estimate-only stopping; approved implementation with project-configured tests; QA approval or corrective rework (up to two rounds); human-gated commit or tracker comment.
- Recursion level: One ticket-team organization, with analyst/estimator/implementer task operations and distinct reviewer reporting to the lead; no autonomous multi-team federation.
- Reviewed revision: `bondie/agent-harness@6c011629ecf3f0cb2cfd72084502e58a31ad3206` (MIT).
- Observation date: 2026-11-05.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

The installed skill instructs the main Claude Code session (team lead) to route a ticket to `jira-analyst` and `estimator`, then present a human plan/estimate gate. If the human approves implementation, the lead invokes `implementer`, then a distinct `reviewer-qa`; failed QA returns specific findings to the implementer, with two bounded re-review rounds. The reviewer directly inspects the uncommitted repository diff, contextual code, acceptance criteria and independently executed checks; it has no write/edit tools. A separate `PostToolUse` hook invokes the target project's configured test command for implementer edits if `HARNESS_TEST_COMMAND` is set. A `PreToolUse` hook denies subagent tracker-MCP writes, while the lead requests human approval before ticket writes or commits. These relationships are first-party installed plugin instructions and hooks, not a claim that the external Claude Code host is part of this repository. See [skill](https://github.com/bondie/agent-harness/blob/6c011629ecf3f0cb2cfd72084502e58a31ad3206/skills/ticket/SKILL.md), [reviewer](https://github.com/bondie/agent-harness/blob/6c011629ecf3f0cb2cfd72084502e58a31ad3206/agents/reviewer-qa.md), [hooks](https://github.com/bondie/agent-harness/blob/6c011629ecf3f0cb2cfd72084502e58a31ad3206/hooks/hooks.json).

## Operational model

The analyst interprets a tracker ticket; the estimator selects historical analogues and forecasts a range; the human approves, adjusts or stops. The implementer reasons about code, edits and tests against the approved approach, receiving test output after changes when the optional project test command is configured. The QA reviewer makes a distinct verdict from primary working-tree evidence and returns factual findings via the lead into implementer rework. The human then decides whether any external commit or tracker write occurs. Fixed gates and prompt delegation constrain operations without automatically establishing whole-organization S3 or S5 decision rights.

## S1 — Operations

- State: A
- Function: Model-directed analysis, effort estimation and approved ticket-specific code changes in a target project.
- Disturbance / variety regulated: Variable tracker requirements, codebase structure, acceptance criteria, failing tests, reference-ticket evidence and QA findings.
- Decisive decision or feedback right: The analyst/estimator interpret ticket content and choose analysis/forecast; the implementer chooses substantive code edits and next local repair from test or review feedback within the approved task.
- Decision owner: Instantiated Claude Code subagent models as operational actors, explicitly invoked by the installed ticket skill; human owns the scope gate, not code-level reasoning.
- Supporting / enforcement mechanisms: Task-specific agent instructions, project-test post-edit hook, configurable precedent MCP, approval gate and tracker-write guard.
- Closure path: Ticket → analyst/estimator choices → human-approved implementation → model-selected edits → repository/test observations → corrections → QA result and handover.
- Boundary reachability: `/agent-harness:ticket` is the advertised installed entry point and explicitly names the subagents; the implementer definition grants Read/Write/Edit/Bash and receives the project test hook when configured.
- Why this is / is not agent-owned: Remove the task-operating models and the prompt/hook package cannot interpret tickets or produce discretionary code changes; the host executes the tool choices but does not replace the task-local reasoning right.
- Evidence: [ticket skill](https://github.com/bondie/agent-harness/blob/6c011629ecf3f0cb2cfd72084502e58a31ad3206/skills/ticket/SKILL.md), [implementer](https://github.com/bondie/agent-harness/blob/6c011629ecf3f0cb2cfd72084502e58a31ad3206/agents/implementer.md), [test feedback](https://github.com/bondie/agent-harness/blob/6c011629ecf3f0cb2cfd72084502e58a31ad3206/hooks/run_tests.py).
- Basis: structural first-party installed workflow.
- Confidence: High for defined agent decision roles; medium for live host behavior not independently exercised.
- Caveats: Requires a configured external Claude Code runtime, tracker and target project; offline estimator experiments are not equivalent to live plugin decisions.

## S2 — Coordination

- State: —
- Function: No evidenced inter-operational-unit interference attenuation loop, distinct from sequential work handoff.
- Disturbance / variety regulated: A ticket can produce analyst/estimator/implementer disagreement, but no peer S1 oscillation or simultaneous incompatible commitments are detected and damped by a separate coordinator.
- Decisive decision or feedback right: The lead follows a prescribed sequence and human gate; it has no evidenced S2-specific adjustment right over independent peer operations.
- Decision owner: Lead role for local routing and human for plan changes; no separately demonstrated S2 owner.
- Supporting / enforcement mechanisms: Fixed role sequence, approval before implementation, bounded QA cycles and role write restrictions.
- Closure path: Task outputs pass to the next role; no qualifying peer-conflict signal → coordinating choice → adjusted peer behavior loop is established.
- Why this is / is not agent-owned: Delegating roles and handing a result forward is not by itself regulation of interaction-generated operational variety.
- Evidence: [installed skill steps](https://github.com/bondie/agent-harness/blob/6c011629ecf3f0cb2cfd72084502e58a31ad3206/skills/ticket/SKILL.md).
- Basis: bounded structural absence.
- Confidence: Medium-high.
- Caveats: Other multi-team integrations are outside this ticket-team boundary.

### Absence scope

- Surfaces inspected: Skill workflow, four agent definitions, hook registration and tracker-write guard.
- Plausible first-party paths checked: Lead as S2 coordinator, estimate/analysis role handoff, QA feedback and shared-repository edits.
- Why no material first-party path remains: The shipped mode is one serial ticket flow; QA addresses implementation conformance and fixed role ordering prevents overlap without a separately evidenced peer-interference regulation loop.

## S3 — Inside-and-now control

- State: —
- Function: No demonstrated discretionary whole-system present-control allocation or operational-portfolio commitment loop.
- Disturbance / variety regulated: Wrong estimates, implementation failures, failed tests and review findings are local task matters, not a cross-unit resource/commitment picture.
- Decisive decision or feedback right: Human approves scope and external writes; lead gates a prescribed ticket sequence. No agent legitimately revises whole-system operational allocations.
- Decision owner: Human for plan and write approval, implementer for task-local edits, prescribed skill for sequencing.
- Supporting / enforcement mechanisms: Human `AskUserQuestion` before implementation, two QA correction rounds, configurable test command, tracker MCP write guard.
- Closure path: Gate → approved individual ticket → implementation/review/handover; no cross-unit performance consolidation and current-control reallocation return.
- Why this is / is not agent-owned: The lead's management label and task handoffs do not establish S3 portfolio authority at this recursion.
- Evidence: [ticket skill](https://github.com/bondie/agent-harness/blob/6c011629ecf3f0cb2cfd72084502e58a31ad3206/skills/ticket/SKILL.md), [tracker guard](https://github.com/bondie/agent-harness/blob/6c011629ecf3f0cb2cfd72084502e58a31ad3206/hooks/guard_tracker_writes.py).
- Basis: bounded structural absence.
- Confidence: Medium-high.
- Caveats: The human manager of multiple unrelated tickets could implement an external S3 that this package does not define.

### Absence scope

- Surfaces inspected: Lead skill, analyst/estimator/implementer/reviewer instructions, configured hooks, README and estimator CLI boundary.
- Plausible first-party paths checked: Lead as portfolio manager, human plan approval as S3, estimate as resource control, QA correction as current control.
- Why no material first-party path remains: Decisions remain within one approved task; there is no first-party cross-operational current-control view, competing commitments or resource/priority bargain that closes into multiple S1 operations.

## S3* — Complementary audit

- State: A
- Function: Distinct independent read-only QA inspection of implementation assertions before human handover.
- Disturbance / variety regulated: Implementer claims of task completion despite erroneous code, missed acceptance criteria, missing tests or regressions.
- Decisive decision or feedback right: The reviewer chooses `approve` or `changes requested` and reports verified `path:line` defects plus checks and criterion status independently of the implementer's report.
- Decision owner: Separate `reviewer-qa` Claude Code subagent; the lead receives its verdict and routes requested corrections to the implementer.
- Supporting / enforcement mechanisms: Explicit review step, reviewer `disallowedTools: Write, Edit, NotebookEdit`, direct `git diff`/`git status` and code-context reading, independent test execution and up to two corrective rounds.
- Closure path: Implementer reports completion → distinct reviewer checks working-tree artifacts and runs validation → issue-specific verdict → lead sends defects back to implementer → new implementation and re-review → human sees evidence/verdict.
- Why this is / is not agent-owned: The reviewer's substantive assessment/verdict is agent judgment on direct source/test evidence; the skill-owned orchestration returns it to the lead and influences completion. This is separate from ordinary implementer self-tests or a deterministic linter.
- Claim being audited: Completed changes meet the ticket analysis and every acceptance criterion without production defects.
- Ordinary reporting path: Implementer summary of files, tests and criteria returned to the lead after edits.
- Complementary access path: Reviewer independently reads the actual uncommitted diff, status and surrounding files and executes read-only tests/linters/static checks.
- Independence boundary: Separate named model subagent without edit tools; cannot edit audited code or merely reuse implementer self-report. It remains subject to the same provider/host and its invocation depends on lead compliance with installed skill instructions.
- Who acts on findings: Lead routes verified QA findings into an implementer rework round and withholds final handover until the bounded review process completes or escalates to the human.
- Boundary reachability: The installed primary `/ticket` skill explicitly calls `reviewer-qa` after implementer and reruns it on change requests; the reviewer definition prescribes primary-artifact inspection, a verdict and line-level findings.
- Evidence: [independent reviewer](https://github.com/bondie/agent-harness/blob/6c011629ecf3f0cb2cfd72084502e58a31ad3206/agents/reviewer-qa.md), [review and correction steps](https://github.com/bondie/agent-harness/blob/6c011629ecf3f0cb2cfd72084502e58a31ad3206/skills/ticket/SKILL.md), [implementer report path](https://github.com/bondie/agent-harness/blob/6c011629ecf3f0cb2cfd72084502e58a31ad3206/agents/implementer.md).
- Basis: explicit + structural first-party audit path.
- Confidence: High for wired separation and corrective instructions, medium for compliance in unobserved live sessions.
- Caveats: Prompt-level reviewer separation, not a cryptographically isolated verifier or automatic no-bypass acceptance gate. Claims of tests passing do not replace actual project test command provisioning.

## S4 — Outside-and-then intelligence

- State: —
- Function: No autonomous prospective adaptation of the ticket-team's organizational capabilities.
- Disturbance / variety regulated: Historical ticket variability and changing complexity are used for current-task forecasting, not future operating-model change.
- Decisive decision or feedback right: Estimator forecasts current ticket hours from precedents; no owned decision to revise future team tools, policy, capacity or capability.
- Decision owner: Estimator for this task's prediction, user/developer for future plugin design and installed configuration.
- Supporting / enforcement mechanisms: Historical precedent MCP and estimate P25–P75, offline model-evaluation scripts, explicit approved approach.
- Closure path: Past tickets → estimate for the current task → human plan decision; no environment futures → strategic adaptation decision → operating-organization feedback.
- Why this is / is not agent-owned: Reference-class forecasting is anticipatory about this ticket's effort, but does not itself establish S4 future-environment/capability adaptation.
- Evidence: [estimation step](https://github.com/bondie/agent-harness/blob/6c011629ecf3f0cb2cfd72084502e58a31ad3206/skills/ticket/SKILL.md), [estimator role](https://github.com/bondie/agent-harness/blob/6c011629ecf3f0cb2cfd72084502e58a31ad3206/agents/estimator.md).
- Basis: bounded structural absence.
- Confidence: High.
- Caveats: External team planning informed by ticket forecasts could be a separate S4 outside this plugin.

### Absence scope

- Surfaces inspected: Estimator definition and reference-class workflow, standalone estimator evaluation CLI, main ticket skill, agent definitions and hooks.
- Plausible first-party paths checked: Historical analogous tickets as environmental sensing, forecast as strategic planning, review feedback as organizational learning.
- Why no material first-party path remains: Information is consumed for a single task estimate/repair; none of the inspected standard modes directs a future organizational capability change back into the installed ticket-team system.

## S5 — Policy and identity

- State: —
- Function: No evidenced first-party ultimate-purpose, organizational identity or constitutional arbitration loop.
- Disturbance / variety regulated: Risky code changes, tracker writes, plan deviations and unapproved commits are governed at an operational authorization level.
- Decisive decision or feedback right: Human may approve implementation and individual write actions; no actor resolves a dispute about the team's enduring ultimate policy or identity.
- Decision owner: Human requester for plan and action consent, installed rules/hooks for routine constraints; no packaged S5 owner.
- Supporting / enforcement mechanisms: Explicit `AskUserQuestion` plan gate, no commit/push without human consent, subagent tracker-write denial hook.
- Closure path: Proposed action → approval or denial → execute/stop; no identity/purpose dispute → legitimate policy-authority judgment → enduring organizational policy revision.
- Why this is / is not agent-owned: Read-only write restrictions and per-action consent protect execution boundaries, not an S5 policy identity feedback loop.
- Evidence: [human gates](https://github.com/bondie/agent-harness/blob/6c011629ecf3f0cb2cfd72084502e58a31ad3206/skills/ticket/SKILL.md), [tracker guard](https://github.com/bondie/agent-harness/blob/6c011629ecf3f0cb2cfd72084502e58a31ad3206/hooks/guard_tracker_writes.py).
- Basis: bounded structural absence.
- Confidence: High.
- Caveats: Host global instructions and organizational identity policies reside outside this plugin.

### Absence scope

- Surfaces inspected: Human plan/writing gates, reviewer and implementer constraints, tracker-write hook, plugin metadata and CLI boundary.
- Plausible first-party paths checked: Human approval as parent S5, tracker-write policy as constitution, lead as mission authority.
- Why no material first-party path remains: Each governs a particular ticket/action or static tool permission. No recurring ultimate-policy adjudication and authoritative identity-level return was found in the declared workflow.

## Recursion

Each named subagent is a functional role on one task. Distinct QA has complementary evidence access and corrective feedback, but the package does not present each subagent as a fully viable organization with its own metasystem. No second independent organizational recursion is credited.

## Variety and escalation

Agent specialization amplifies task-analysis and coding variety. Human plan approval constrains scope; the test hook gives operational feedback; the independent QA actor supplies complementary audit information through a correction loop. The guard prevents subagent tracker writes and the final human handoff restricts commit/external side effects. The two-round cap escalates unresolved QA changes to a human rather than pretending automatic acceptance.

## Evidence gaps

- Repository-first assessment of pinned installed plugin configuration; no authenticated Claude Code live ticket or tracker service execution performed. Claims of live test-hook E2E in README were not independently replicated.
- Reviewer independence is role/tool-context separation defined in first-party configuration; the external Claude Code implementation is excluded from owned mechanisms.
- `HARNESS_TEST_COMMAND` is operator/project-configured and optional; absent configuration means no per-edit test hook check, although the QA review instructions still request project checks.
- Negative findings are bounded to the shipped standard ticket-team mode, not every external Claude Code user organization.

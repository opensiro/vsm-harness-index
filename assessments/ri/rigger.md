---
harness_id: rigger
project_name: Rigger
repository: https://github.com/Borcioo/rigger-claude-code
review_ref: eda9361632b4097add3ba2c102f756a5e8ceb739
reviewed_at: 2026-11-27
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: P
autonomy_s5: P
---

# Rigger

## Review boundary

- System in focus: A Rigger plugin suite installed in Claude Code, in its coordinated software delivery mode.
- Purpose and identity: Run and oversee approved engineering work in consumer project repositories.
- Relevant environment: Claude Code host, local worktrees, project checks and model-backed side sessions or subagents.
- Standard-distribution boundary: The public plugin marketplace, documented dependencies and checked-in operating definitions at the pinned revision.
- Credited operating / distribution surfaces: Installed rigger-core, rigger-review, rigger-rules and rigger-lessons, with shipped coordinate command, hooks, state tooling and reviewer/worker definitions.
- Adjacent first-party surfaces excluded from ownership: Rigger's own contribution and release workflow, repository QA fixtures and unrelated desktop/WordPress or platform extensions. Claude host/model, superpowers and project infrastructure are dependencies.
- First-party operating / deployment modes considered: Desktop coordinator with side sessions, terminal or fallback coordinator with subagents, and owner-operated lesson/policy paths where the relevant plugins are enabled.
- Recursion level: One Rigger installation operating one approved plan across multiple builder units. The person operating it is the legitimate parent for reserved governance choices.
- Reviewed revision: eda9361632b4097add3ba2c102f756a5e8ceb739
- Observation date: 2026-11-27
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

Rigger supplies a first-party installable operating layer for Claude Code. Start hooks assemble defaults and scoped operating rules. The coordinate command owns an executable part-state ledger and defines task and review dispatch through the host. Model workers deliver project branches and evidence, while a separate review role inspects exact source changes. The optional lessons module proposes rule improvements and feeds adopted content through the installed rule loader.

## Operational model

A builder S1 unit takes an outcome-bearing brief, operates in its designated worktree and returns an attributable commit, checks or blocker. The coordinator selects current allocations and the reviewer independently tests readiness claims against the pinned changes. Separate operator decisions govern adoption of future rules and delegation of executable review authority.

## S1 — Operations

- State: A
- Function: Execute approved software work units in project branches and return evidence of code changes, testing or a blocker.
- Disturbance / variety regulated: Different task requirements, tool constraints, changed code and failed tests.
- Decisive decision or feedback right: Choose implementation, test, diagnosis and repair actions within a scoped brief.
- Decision owner: The model-backed worker or side-session operating agent supplied through the installed plugin.
- Supporting / enforcement mechanisms: First-party worker definition, staged coordinator briefs, tool/skill hooks, state records and project checks.
- Closure path: The worker reads and modifies its worktree, runs the named check, and returns head SHA and gate evidence. The coordinator can send corrections or advance the part through review and integration.
- Boundary reachability: The public marketplace carries the worker and coordinator. The host's Agent/session and workspace tools execute the supplied briefs. Rules are delivered through installed startup and subagent hooks.
- Why this is / is not agent-owned: The worker makes implementation decisions and adapts work from test results. The user authorizes the plan and reserves selected publication boundaries.
- Evidence: [.claude-plugin/marketplace.json](https://github.com/Borcioo/rigger-claude-code/blob/eda9361632b4097add3ba2c102f756a5e8ceb739/.claude-plugin/marketplace.json#L6-L30), [plugins/rigger-core/agents/worker.md](https://github.com/Borcioo/rigger-claude-code/blob/eda9361632b4097add3ba2c102f756a5e8ceb739/plugins/rigger-core/agents/worker.md#L1-L11), [plugins/rigger-core/hooks/hooks.json](https://github.com/Borcioo/rigger-claude-code/blob/eda9361632b4097add3ba2c102f756a5e8ceb739/plugins/rigger-core/hooks/hooks.json#L34-L53), [plugins/rigger-core/commands/coordinate.md](https://github.com/Borcioo/rigger-claude-code/blob/eda9361632b4097add3ba2c102f756a5e8ceb739/plugins/rigger-core/commands/coordinate.md#L71-L104)
- Basis: Pinned first-party source inspection.
- Confidence: high
- Caveats: The plugin depends on Claude Code and project tools. The assessment does not attribute their general capabilities to Rigger outside this assembled mode.

## S2 — Coordination

- State: A
- Function: Coordinate distinct building agents' concurrent use of files, ports, test data and resource slots.
- Disturbance / variety regulated: Parallel agents can overwrite the same files, contend for ports and shared databases, or distort tests through concurrent heavy work.
- Decisive decision or feedback right: Select a split, choose serial versus separate worktree/port/data execution, and dispatch or hold the next action.
- Decision owner: The active orchestrator agent in the installed orchestration workflow.
- Supporting / enforcement mechanisms: Worktree/port/scratch assignment, declared file scopes, run/gate locks, state-ledger dependencies and worker feedback.
- Closure path: The coordinator inspects active worktree and reported file state, keys the next brief to its assigned lane, and keeps overlapping or resource-conflicting work waiting. It checks altered work at return before integration.
- Boundary reachability: The installed coordinate command explicitly loads the orchestrating skill and initializes the current state ledger before dispatch.
- Why this is / is not agent-owned: The model selects a coordination treatment and revises execution on actual lane state. Locks and host tools enforce parts of the chosen arrangement.
- Distinct S1 units: Model-led builder lanes in separate sessions or subagents, with separate briefs and worktrees.
- Inter-S1 disturbance: Overlapping file edits, port/database interference, and competition for shared test capacity.
- Attenuating coordination relation: Allocate disjoint worktrees/ports/data or serialize overlapping work and shared resources.
- Feedback into subsequent S1 behaviour: Inspect active claims and failed or busy checks. Send revised briefs, defer a conflicting lane, or switch the shared test workload to an isolated/serial mode.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The protocol specifically checks and resolves interference between concurrent operating units before dispatch and integration.
- Evidence: [plugins/rigger-core/commands/coordinate.md](https://github.com/Borcioo/rigger-claude-code/blob/eda9361632b4097add3ba2c102f756a5e8ceb739/plugins/rigger-core/commands/coordinate.md#L23-L69), [plugins/rigger-core/skills/orchestrating-subagents/SKILL.md](https://github.com/Borcioo/rigger-claude-code/blob/eda9361632b4097add3ba2c102f756a5e8ceb739/plugins/rigger-core/skills/orchestrating-subagents/SKILL.md#L25-L71), [plugins/rigger-core/tools/coord-state/coord_state.py](https://github.com/Borcioo/rigger-claude-code/blob/eda9361632b4097add3ba2c102f756a5e8ceb739/plugins/rigger-core/tools/coord-state/coord_state.py#L236-L269)
- Basis: Pinned first-party source inspection.
- Confidence: high
- Caveats: Some coordination relies on following shipped instructions, rather than an all-cases scheduler. The positive finding is bounded to the first-party orchestrated mode.

## S3 — Inside-and-now control

- State: A
- Function: Regulate the active portfolio of parts in an approved coding plan.
- Disturbance / variety regulated: Blocked and silent lanes, failed hypotheses, lane dependencies, or a shortage of model and heavy-job capacity.
- Decisive decision or feedback right: Choose which parts to dispatch, which to keep waiting, how to split or reassign stalled work, and when to reopen, advance or integrate a part.
- Decision owner: The main coordinating model inside the approved plan envelope.
- Supporting / enforcement mechanisms: Current part states, assigned session and head, watchers, bounded capacity rules, transition validation and independent review findings.
- Closure path: The coordinator reconciles worker reports, current state, gate evidence and reviews; it returns a new assignment, fix round, block or permitted integration. Those decisions control the next dispatched work.
- Boundary reachability: The attached coordinate command creates the ledger and calls the host control surfaces. Agent choices are described for desktop and CLI/fallback modes.
- Why this is / is not agent-owned: The active coordinator selects resource and commitment interventions over distinct current lanes. The user supplies the plan's remit and separately approves protected actions.
- Whole-system current view: Current part states, dependencies, running session IDs, head SHAs, gate evidence, and outstanding review or capacity concerns across the approved plan.
- Current-control decision scope: Cross-lane dispatch, reuse of standby sessions/model capacity, split or reassignment after a failure, blocked/reopened state and integration eligibility.
- Evidence: [plugins/rigger-core/commands/coordinate.md](https://github.com/Borcioo/rigger-claude-code/blob/eda9361632b4097add3ba2c102f756a5e8ceb739/plugins/rigger-core/commands/coordinate.md#L23-L69), [plugins/rigger-core/commands/coordinate.md](https://github.com/Borcioo/rigger-claude-code/blob/eda9361632b4097add3ba2c102f756a5e8ceb739/plugins/rigger-core/commands/coordinate.md#L92-L119), [plugins/rigger-core/commands/coordinate.md](https://github.com/Borcioo/rigger-claude-code/blob/eda9361632b4097add3ba2c102f756a5e8ceb739/plugins/rigger-core/commands/coordinate.md#L125-L148), [plugins/rigger-core/skills/orchestrating-subagents/SKILL.md](https://github.com/Borcioo/rigger-claude-code/blob/eda9361632b4097add3ba2c102f756a5e8ceb739/plugins/rigger-core/skills/orchestrating-subagents/SKILL.md#L73-L86), [plugins/rigger-core/tools/coord-state/coord_state.py](https://github.com/Borcioo/rigger-claude-code/blob/eda9361632b4097add3ba2c102f756a5e8ceb739/plugins/rigger-core/tools/coord-state/coord_state.py#L236-L269)
- Basis: Pinned first-party source inspection.
- Confidence: high
- Caveats: The decision authority is confined to an approved plan and its integration branch. Owner consent for the plan or default-branch merge does not supply a separate parent-operated current-control mode.

## S3* — Complementary audit

- State: A
- Function: Independently check the evidence that a built part is ready to advance in the coordinator's plan.
- Disturbance / variety regulated: A producer's success report or a coordinator's built status can miss regressions, incomplete coverage or questionable tests.
- Decisive decision or feedback right: Issue a scoped finding or clean/partial verdict from direct evidence, then require its disposition before the coordinator advances the part.
- Decision owner: The separately invoked read-only reviewer agent in the default review slot, with the coordinator owning corrective action.
- Supporting / enforcement mechanisms: Dedicated reviewer role, base/head commit scope, independent diff and source access, closing contract validation and fresh re-review for qualifying risk.
- Closure path: The reviewer returns findings and coverage. The coordinator validates the result and either dispatches repair, blocks review, or performs the evidenced state transition to reviewed and eventual integration.
- Boundary reachability: The installed review plugin defines the default reviewer slot. The coordinate command directs independent review sessions and blocks advancement when the slot is absent.
- Why this is / is not agent-owned: A separate model examines the actual code and evidence outside the builder's report. It has its own judgment, and that judgment changes the organizational control decision.
- Claim being audited: That a specific built branch and pinned head are suitable for the coordinator to mark reviewed and integrate.
- Ordinary reporting path: A builder reports the commit, clean worktree and its gate results to the coordinator, which records the built state.
- Complementary access path: The reviewer accesses the pinned base/head diff and applicable source independently, reconstructing coverage and checks.
- Independence boundary: A lane may not review its own work. The reviewer role has restricted edit/dispatch access and qualifying changes get a fresh reviewer.
- Who acts on findings: The coordinator orders a fix round, re-review, block or reviewed transition before integration.
- Evidence: [plugins/rigger-core/commands/coordinate.md](https://github.com/Borcioo/rigger-claude-code/blob/eda9361632b4097add3ba2c102f756a5e8ceb739/plugins/rigger-core/commands/coordinate.md#L39-L43), [plugins/rigger-core/commands/coordinate.md](https://github.com/Borcioo/rigger-claude-code/blob/eda9361632b4097add3ba2c102f756a5e8ceb739/plugins/rigger-core/commands/coordinate.md#L83-L114), [plugins/rigger-core/rigger-defaults.json](https://github.com/Borcioo/rigger-claude-code/blob/eda9361632b4097add3ba2c102f756a5e8ceb739/plugins/rigger-core/rigger-defaults.json#L1-L10), [plugins/rigger-review/agents/reviewer.md](https://github.com/Borcioo/rigger-claude-code/blob/eda9361632b4097add3ba2c102f756a5e8ceb739/plugins/rigger-review/agents/reviewer.md#L1-L20), [plugins/rigger-review/skills/review/SKILL.md](https://github.com/Borcioo/rigger-claude-code/blob/eda9361632b4097add3ba2c102f756a5e8ceb739/plugins/rigger-review/skills/review/SKILL.md#L15-L30), [plugins/rigger-review/skills/review/SKILL.md](https://github.com/Borcioo/rigger-claude-code/blob/eda9361632b4097add3ba2c102f756a5e8ceb739/plugins/rigger-review/skills/review/SKILL.md#L55-L68), [plugins/rigger-core/skills/orchestrating-subagents/SKILL.md](https://github.com/Borcioo/rigger-claude-code/blob/eda9361632b4097add3ba2c102f756a5e8ceb739/plugins/rigger-core/skills/orchestrating-subagents/SKILL.md#L146-L172)
- Basis: Pinned first-party source inspection.
- Confidence: high
- Caveats: The independence is the first-party role and access design. Source inspection does not demonstrate a live review, and a separately configured command slot is not needed for this grade.

## S4 — Outside-and-then intelligence

- State: P
- Function: Adapt future operating rules and checks to evidenced recurring conditions across the projects where the harness operates.
- Disturbance / variety regulated: User corrections, project-specific test failures and independent review findings reveal that the same class of issue can recur across projects.
- Decisive decision or feedback right: Decide whether a tested generalization should change future rules or remain local, deferred or rejected.
- Decision owner: The operator of the installed harness approves or rejects the proposed change. The curation agent supplies exact edits and evidence.
- Supporting / enforcement mechanisms: Evidence-typed lesson inbox, cross-project recurrence rule, proposal review, optional background proposal generator and next-session rule loader.
- Closure path: A proposed rule or guard is reviewed against the current rule corpus and evidence. On operator approval, the curation flow writes the routed rule, and the enabled loader injects it into later working sessions.
- Boundary reachability: The plugin ships curation and a supported artifact that the paired rules plugin loads on startup. The standalone global case does not require maintainer publication.
- Why this is / is not agent-owned: The model detects and proposes improvements. Changing future operating capability through the documented curation flow requires the legitimate operator's decision.
- External distinction: Evidence can arrive from the toolchain and test behavior of multiple consuming projects and their users, outside the installed harness's own rules corpus.
- Future / prospective distinction: Curation checks whether the class will recur outside the original case and whether a future process guard would be worthwhile.
- Adaptation option generated: A scoped change to an operative rule or skill, or, on recurrence despite a rule, a proposed process guard with measured cost.
- Path back into current capability / S3: Approval writes local/global operating rules. The rule loader and subsequent project briefs apply them to new operations.
- Evidence: [plugins/rigger-lessons/rules/lessons.md](https://github.com/Borcioo/rigger-claude-code/blob/eda9361632b4097add3ba2c102f756a5e8ceb739/plugins/rigger-lessons/rules/lessons.md#L1-L42), [plugins/rigger-lessons/skills/curate-lessons/SKILL.md](https://github.com/Borcioo/rigger-claude-code/blob/eda9361632b4097add3ba2c102f756a5e8ceb739/plugins/rigger-lessons/skills/curate-lessons/SKILL.md#L38-L77), [plugins/rigger-lessons/README.md](https://github.com/Borcioo/rigger-claude-code/blob/eda9361632b4097add3ba2c102f756a5e8ceb739/plugins/rigger-lessons/README.md#L5-L21), [plugins/rigger-rules/README.md](https://github.com/Borcioo/rigger-claude-code/blob/eda9361632b4097add3ba2c102f756a5e8ceb739/plugins/rigger-rules/README.md#L35-L58)
- Basis: Pinned first-party source inspection.
- Confidence: high
- Caveats: Credits approved local/global curation and rule delivery, with the lessons and rules plugins enabled. The optional background batch stops at proposals.

## S5 — Policy and identity

- State: P
- Function: Set the ultimate authority for accepting executable project-level replacements of the installation's review policy.
- Disturbance / variety regulated: A consuming repository proposes to appoint an executable command as the review authority, which can conflict with the installation's default or personal review policy.
- Decisive decision or feedback right: Grant or withhold the repository-level power to set the reviewer command slot.
- Decision owner: The human installation owner via the personal trust configuration. The repository layer cannot confer that authority on itself.
- Supporting / enforcement mechanisms: Personal-only trust policy, review-slot defaults, filtered layered resolution, visible effective source and invocation-time snapshot enforcement.
- Closure path: A conflicting project slot is refused unless its named slot is entrusted at the personal layer. The next assembled session uses the authorized assignment, and the command runner rechecks the effective trusted slot when invoked.
- Boundary reachability: The shipped core assembler reads the policy layer and hands its resolved slot snapshot into the installed runtime. The coordinator uses the designated reviewer slot for review.
- Why this is / is not agent-owned: The personal decision determines which party appoints the continuing review authority in this configuration. The agent consumes the resolved policy.
- Identity / ultimate-policy issue: Which organizational layer has the right to designate executable oversight for the local Rigger workflow.
- Ultimate authority in each claimed mode: The installation owner, whose personal trust policy accepts or rejects delegation to project configuration.
- Return-to-operation path: Personal policy filters the project declaration at session assembly. Its resulting slot classification and trust are recorded and the runner enforces them when review is invoked.
- Evidence: [plugins/rigger-core/README.md](https://github.com/Borcioo/rigger-claude-code/blob/eda9361632b4097add3ba2c102f756a5e8ceb739/plugins/rigger-core/README.md#L112-L158), [plugins/rigger-core/tools/assemble/config.py](https://github.com/Borcioo/rigger-claude-code/blob/eda9361632b4097add3ba2c102f756a5e8ceb739/plugins/rigger-core/tools/assemble/config.py#L28-L44), [plugins/rigger-core/tools/assemble/slots.py](https://github.com/Borcioo/rigger-claude-code/blob/eda9361632b4097add3ba2c102f756a5e8ceb739/plugins/rigger-core/tools/assemble/slots.py#L170-L211), [plugins/rigger-core/tools/assemble/assemble.py](https://github.com/Borcioo/rigger-claude-code/blob/eda9361632b4097add3ba2c102f756a5e8ceb739/plugins/rigger-core/tools/assemble/assemble.py#L615-L630), [plugins/rigger-core/tools/slot-run/slot_run.py](https://github.com/Borcioo/rigger-claude-code/blob/eda9361632b4097add3ba2c102f756a5e8ceb739/plugins/rigger-core/tools/slot-run/slot_run.py#L398-L415), [plugins/rigger-core/commands/coordinate.md](https://github.com/Borcioo/rigger-claude-code/blob/eda9361632b4097add3ba2c102f756a5e8ceb739/plugins/rigger-core/commands/coordinate.md#L100-L114)
- Basis: Pinned first-party source inspection.
- Confidence: high
- Caveats: The finding is limited to the local authority over the reviewer appointment. It does not transfer Claude host policy or upstream maintainer authority to the plugin.

## Recursion

The unit of analysis is the installed harness. Builder lanes act as distinct S1 cells over their own parts, with the coordinator above them in the plan. The host, user and upstream maintainers are external authorities at their respective boundaries.

## Variety and escalation

Lane and review signals flow to the coordinator through reports, state and monitoring. Unavailable capacity or required approvals are surfaced to the operator at explicit stops. These paths establish the described decision return and scope for normal exception handling.

## Evidence gaps

Pinned source review only. The instruction-led operating modes, external Claude host and optional plugins were not executed. The shipped contracts support the described arrangement without evidence about empirical observance or effectiveness.

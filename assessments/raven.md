---
harness_id: raven
project_name: Raven
repository: https://github.com/EverMind-AI/Raven
review_ref: e6c0344cb7ce00db25d554e4bb671ec1909a8f9f
reviewed_at: 2026-09-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-29
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: P
---

# Raven

## Review boundary

- System in focus: the first-party `EverMind-AI/Raven` standard distribution at pinned revision `e6c0344cb7ce00db25d554e4bb671ec1909a8f9f`, centered on the Raven host/runtime, its `AgentLoop`, built-in/registered agent execution, DAG/subagent orchestration, shipped Playbooks including `mode: stint`, session/memory state, proactive runtime, and the standard operator-facing CLI/gateway surfaces that assemble those paths.
- Purpose and identity: provide one persistent host that can run agent turns, use tools, delegate to specialized agents, preserve state across sessions, and execute longer-horizon multi-agent work under first-party orchestration and governance mechanisms.
- Relevant environment: users/operators; target repositories and other task workspaces; model providers; MCP/plugin/tool services; remote or local agent backends; messaging channels; changing task state and evidence; Git/project specifications in `stint` mode.
- Standard-distribution boundary: the installed `raven` runtime and its shipped built-in Playbooks are inside. First-party tests, repository CI, benchmark harnesses, simulations, and development plans are corroborating/adjacent unless they are reachable through an ordinary shipped mode. `evolver/` is treated as a separate benchmark-driven development tool because Raven's own documentation says it consumes the subject harness and retains candidate changes rather than rewriting the production agent during chat. `experimental/curator/` and `experimental/simulation/` are excluded from ownership because the inspected imports remain in experimental/simulation/test surfaces rather than the standard runtime assembly.
- Credited operating / distribution surfaces: `README.md`; `CONTEXT.md`; `raven/agent/loop/`; `raven/agent/subagent/`; `docs-site/docs/orchestration.md`; `raven/playbook/`; the built-in `long-horizon-dev-stint` Playbook and `raven/stint/`; `docs-site/docs/proactivity.md`; ordinary gateway/CLI/runtime assembly.
- Adjacent first-party surfaces excluded from ownership: `evolver/`; `experimental/curator/`; `experimental/simulation/`; benchmarks; tests; repository-development CI; design/planning documents that are not themselves a reachable runtime path.
- First-party operating / deployment modes considered: direct host turns; built-in/registered agents; foreground/background `spawn`; `run_subagent_dag`; stored Playbooks; generated worker tables and Charters; `mode: stint` long-horizon development rounds; Sentinel/Cron/Heartbeat; operator-connected plugins/tools; human answer/decision return in `stint`.
- Recursion level: one Raven host executing a task/project. In `stint` mode, the project-level organization of Planner, Builder, Verifier and the legitimate human/project owner is analyzed as a supported first-party recursive operating mode inside that host. Upstream Raven repository development is not imported as the product's parent organization.
- Reviewed revision: `e6c0344cb7ce00db25d554e4bb671ec1909a8f9f`.
- Observation date: 2026-09-29.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Raven exposes a first-party agent runtime rather than only a workflow schema or coordination substrate. Its `AgentLoop` is the core processing engine used by entrances, and the repository's runtime/context documentation describes a turn as one complete agent reaction in which context is assembled, the model is driven through tool iterations, memory is consolidated, and deliverables are emitted. Raven can run its built-in specialized agents and third-party agents, and its host can delegate one task or submit a dependency graph of multiple sub-agent tasks.

The multi-agent path is explicitly layered. A roster determines which backends can execute work; an optional generated Worker Table gives task-specific labels and responsibilities for one host turn; a Charter narrows a dispatched worker's instructions/tools/checks/deadline; and `run_subagent_dag` validates a graph, dispatches ready nodes, records outputs, and exposes failure/replan controls. These mechanisms establish rich delegation and current-control surfaces, but the assessment keeps decision ownership separate from runtime enforcement.

A particularly strong metasystem witness is the shipped `long-horizon-dev-stint` Playbook. A `stint` compiles each round into an ordinary sub-agent graph and carries project state across rounds. Its Planner, Builder and fresh-session Verifier have distinct rights. The Planner decides what the round does and can add/assign/defer/reject/block backlog work. The Builder performs the project work. The Verifier reviews evidence the Builder could not independently validate, receives runtime-run checks, issues per-task verdicts, and can reopen regressions. Findings feed the next Planner round.

Raven also contains two tempting adaptation surfaces that are deliberately not borrowed into S4. `evolver/` is documented as a standalone benchmark-driven tool that evaluates candidate harness edits and retains them as Git commits; its own guide says it is not a production agent rewriting itself during chat and that promotion is not deployment. `experimental/curator/` is an experimental R&D surface whose inspected references are confined to experimental simulation and tests rather than the credited standard runtime. Sentinel is runtime-reachable, but its proactive reminders/task-discovery loop changes what work is attempted, not the harness's current capability, so it is not sufficient S4 evidence under Profile 0.2.4.

Primary evidence:

- [`README.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/README.md) — first-party host identity, built-in agents, multi-agent orchestration, and explicit separation of Raven Evolver.
- [`CONTEXT.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/CONTEXT.md) — runtime/turn/agent-loop model, worker tables, Charters, `stint`, path ownership, and experimental curator boundary.
- [`raven/agent/loop/main.py`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/raven/agent/loop/main.py) — first-party `AgentLoop` core processing engine.
- [`docs-site/docs/orchestration.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/docs-site/docs/orchestration.md) — DAG execution, worker/Charter semantics, concurrency, shared-work interference, verdicts, replanning and recovery.
- [`raven/playbook/builtin/long-horizon-dev-stint/playbook.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/raven/playbook/builtin/long-horizon-dev-stint/playbook.md) — shipped Planner/Builder/Verifier round structure and reachable `stint` mode.
- [`raven/templates/prompts/en/stint_orders_planner.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/raven/templates/prompts/en/stint_orders_planner.md) — Planner current-control rights and escalation boundaries.
- [`raven/templates/prompts/en/stint_orders_verifier.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/raven/templates/prompts/en/stint_orders_verifier.md) — fresh independent verification path and reopen authority.
- [`raven/stint/decisions.py`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/raven/stint/decisions.py) — human-only decision ledger, queued answers, round-boundary merge and unblock closure.
- [`docs-site/docs/proactivity.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/docs-site/docs/proactivity.md) — Sentinel/Cron/Heartbeat behavior and policy boundaries.
- [`docs-site/docs/evolver.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/docs-site/docs/evolver.md) — explicit standalone development-tool boundary for Evolver.

## Operational model

A normal Raven turn enters the host runtime, loads the selected agent/model/session context, and lets the first-party model loop choose tools and continue from observations until it produces the turn result. The same host can delegate operational work to registered agents through `spawn` or `run_subagent_dag`; DAG execution validates dependencies and backend capabilities, executes ready nodes, stores node artifacts, and can return failures to model-driven continue/abandon/replan decisions.

For long-horizon project work, the shipped `stint` mode adds a recursive organizational structure over the ordinary DAG path. Each round is planned from the project specification, backlog, human decisions, fix history and prior verification. The Builder then changes the project inside declared ownership constraints. A separate Verifier session gets runtime check results plus project evidence and adjudicates whether in-review tasks are proven. The next Planner consumes those findings and decides the next current-control response.

The system therefore has first-party operational autonomy, autonomous current control and complementary audit. Its anti-interference primitives are material but do not by themselves prove an autonomous S2 owner: the first-party runtime can enforce dependencies, instance serialization and authored responsibility boundaries, while the actual conflict-specific partition for parallel shared-work tasks still has to be composed into the graph/brief/working-copy layout. No standard-runtime outside-and-then capability-adaptation loop is established. Ultimate project-policy decisions in `stint` can, however, be escalated to the legitimate human and returned into subsequent rounds.

## S1 — Operations

- State: A
- Function: first-party agent loops directly perform the system's operational work by interpreting task context, choosing model/tool actions, observing results, and continuing until a deliverable or bounded failure state is reached.
- Disturbance / variety regulated: ambiguous user/task requests; changing tool and workspace state; model/provider outputs; tool failures; repository/filesystem observations; delegated worker results; session context and memory.
- Decisive decision or feedback right: choose the next substantive tool/model action and decide how to continue from the returned observation in pursuit of the task.
- Decision owner: the active Raven agent model in the first-party `AgentLoop`; specialized first-party/registered worker agents own the corresponding local delegated turns.
- Supporting / enforcement mechanisms: context assembly; tool registry and per-turn tool scope; provider routing; session/history/memory persistence; iteration limits; workspace/tool permissions; backend adapters; result and error transport.
- Closure path: task/turn request → context assembled → model chooses action/tool → tool/environment returns observation → model chooses the next action or finishes → result is emitted/persisted; delegated worker turns use the same basic action/observation closure inside their backend.
- Why this is / is not agent-owned: removing the model-driven `AgentLoop` while leaving the registries, memory, routing and tool machinery removes the actor that interprets changing observations and chooses the substantive next action; the remaining machinery cannot reproduce that discretion.
- Evidence: [`raven/agent/loop/main.py`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/raven/agent/loop/main.py); [`CONTEXT.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/CONTEXT.md); [`README.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: an individual spawned process is not automatically a recursive viable system; S1 credit comes from the first-party operational model/tool loop and supported specialized-agent execution, not from counting every DAG node as an S1.
- Boundary reachability: `AgentLoop` is the ordinary host execution shell used by Raven entrances and is assembled by the standard runtime; this is not benchmark/example-only behavior.

## S2 — Coordination

- State: C
- Function: Raven provides a first-party construction path for damping concrete shared-work interference among parallel operational workers by encoding dependency/order and responsibility/isolation choices into DAGs, worker briefs and execution layout.
- Disturbance / variety regulated: parallel agent nodes can operate against the same project/working directory and destructively overlap writes or depend on state that another worker has not yet produced; shared agent instances also create ordering/state-continuation interference.
- Decisive decision or feedback right: decide which workers may proceed independently, which must wait on dependencies, and how potentially overlapping work is partitioned across responsibilities or separate working copies.
- Decision owner: not established as an autonomous conflict-specific regulator in the standard distribution. Raven supplies the graph/worker/working-copy construction surfaces and deterministic enforcement; the caller, authored Playbook, or task-specific graph composition must encode the actual anti-interference response.
- Supporting / enforcement mechanisms: `depends_on`; DAG preflight and cycle/input validation; ready-node scheduling; shared concurrency semaphore; serialization of nodes sharing an `instance`; worker labels/briefs; Charters; explicit separate-working-copy/worktree guidance; `stint` path-ownership enforcement as a stronger specialized-mode example.
- Closure path: composition identifies shared-work ordering/ownership constraints → graph/brief/working-copy arrangement is encoded → Raven validates and enforces the resulting dependency/serialization boundary → workers execute only when ready and receive scoped responsibilities → subsequent worker behavior is changed by that coordination result.
- Why this is / is not agent-owned: the first-party relation is more than a message bus or generic edge because Raven's own orchestration documentation names the concrete shared-write hazard and the need to divide ownership or working copies. However the inspected standard path does not establish a distinct Raven agent that senses that interference and autonomously chooses/revises the conflict response; therefore the state is constructor-level `C`, not `A`.
- Evidence: [`docs-site/docs/orchestration.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/docs-site/docs/orchestration.md); [`CONTEXT.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/CONTEXT.md); [`raven/agent/subagent/dag_graph.py`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/raven/agent/subagent/dag_graph.py).
- Basis: explicit structural disturbance + first-party construction path.
- Confidence: medium-high.
- Caveats: ordinary task decomposition, DAG edges and shared state are not credited by themselves. The positive mapping depends on the repository's explicit shared-work collision model plus mechanisms that can be composed specifically to attenuate it. If a future first-party conflict-aware planner is shown to own this decision in the standard runtime, this state could require re-review.
- Boundary reachability: `run_subagent_dag`, worker labels/Charters and the relevant scheduling/serialization mechanisms are standard host tools; no external harness implementation is required to construct the relation.
- Distinct S1 units: registered Raven operational workers (including the shipped specialized agents) can execute separate model/tool loops on distinct delegated outcomes within the same host task/project.
- Inter-S1 disturbance: two independent workers can write the same working directory or consume shared session/project state in an unsafe order; Raven explicitly warns that parallel writing nodes do not automatically receive separate worktrees or exclusive locks.
- Attenuating coordination relation: authored dependencies, responsibility partitioning, instance serialization and separate working copies/worktrees can keep conflicting units from acting on the same mutable surface at the same time.
- Feedback into subsequent S1 behaviour: a dependency keeps a node pending until prerequisites complete; instance serialization delays competing continuations; scoped responsibility/working-copy choices change where and when workers act.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the credited relation is tied to an explicit destructive-interference mode—overlapping mutation/order of shared operational state—and the construction mechanisms are used to attenuate that disturbance, not merely to transmit results or assign subtasks.

## S3 — Inside-and-now control

- State: A
- Function: in the shipped `mode: stint` organization, the Planner regulates the project's current commitments and priorities across the operational round rather than merely decomposing one parent prompt.
- Disturbance / variety regulated: competing ready backlog items; previous Verifier findings; repeated regressions; deferred work; blockers; target gates; fix history; human requests and decisions; the amount of work that can coherently fit one round.
- Decisive decision or feedback right: choose what the current round does and exercise backlog authority to add, assign, defer, reject or block work under fixed specification/gate constraints.
- Decision owner: the first-party Planner role executed by a Raven-Code agent session in the built-in `long-horizon-dev-stint` Playbook.
- Supporting / enforcement mechanisms: persisted backlog; `.stint/SPEC.md`; `.stint/HUMAN_DECISIONS.md`; `.stint/FIXLOG.md`; previous verification report; runtime role/path guards; round compiler; DAG dispatch; verification gates and task-state transitions.
- Closure path: current project/backlog/finding state → Planner model reviews the whole round context → Planner chooses priorities/commitments and writes the round brief plus task-state transitions → Builder receives that brief and performs the work → Verifier results return into the next Planner cycle.
- Why this is / is not agent-owned: the runtime constrains which transitions and paths are legal, but the Planner model—not the deterministic backlog store—decides which ready work is taken, deferred, rejected or blocked in light of the whole current project state.
- Evidence: [`raven/playbook/builtin/long-horizon-dev-stint/playbook.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/raven/playbook/builtin/long-horizon-dev-stint/playbook.md); [`raven/templates/prompts/en/stint_orders_planner.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/raven/templates/prompts/en/stint_orders_planner.md); [`CONTEXT.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/CONTEXT.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: generic Raven delegation and concurrency limits are not independently counted as S3. The positive witness is the built-in `stint` current-control loop where whole-project state and real backlog authority are both present.
- Boundary reachability: `long-horizon-dev-stint` ships in the standard repository and is documented as invokable by name/CLI or natural trigger; it compiles each round through Raven's ordinary sub-agent graph path.
- Whole-system current view: the Planner is instructed to read the ready pool, prior Verifier report, deferred pile-up, regression/fix history, project specification and human decisions before choosing the round.
- Current-control decision scope: it can select current commitments, prioritize regressions/findings/gates, and apply `add`, `assign`, `defer`, `reject` and `block` transitions while leaving implementation detail to the Builder.

## S3* — Complementary audit

- State: A
- Function: the `stint` Verifier provides a complementary audit path that challenges the Builder's ordinary account of work through a fresh session, runtime-run checks and independent inspection of evidence the author could not validate for itself.
- Disturbance / variety regulated: false completion claims; missing self-check evidence; regressions; criteria drift; checks that merely reproduce the implementation's own mistake; visual/evidence discrepancies; nondeterministic or environment-dependent results.
- Decisive decision or feedback right: decide whether each task in review is proven by independent evidence, raise findings, and reopen work when a regression invalidates a previously accepted result.
- Decision owner: the first-party Verifier agent session; the Verifier prompt is explicitly `session: fresh` and grants verdict/reopen rights while withholding product-code/criteria authority.
- Supporting / enforcement mechanisms: runtime-run check table; Builder handoff/self-check report; evidence files; fresh verifier context; role-specific path ownership; task verdict/reopen transitions; severity/finding report; next-round Planner ingestion.
- Closure path: Builder submits work and its ordinary self-check → runtime runs declared checks and Verifier independently inspects evidence/edges/changed checks → Verifier records proven/not-proven verdicts and findings or reopens a regression → next Planner must dispose of findings and reprioritize subsequent work.
- Why this is / is not agent-owned: the runtime supplies check results and enforces role boundaries, but the complementary judgment over whether evidence supports the claim is made by a separate Verifier agent that is instructed to look specifically for what the author could not see.
- Evidence: [`raven/templates/prompts/en/stint_orders_verifier.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/raven/templates/prompts/en/stint_orders_verifier.md); [`raven/playbook/builtin/long-horizon-dev-stint/playbook.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/raven/playbook/builtin/long-horizon-dev-stint/playbook.md); [`raven/templates/prompts/en/stint_orders_planner.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/raven/templates/prompts/en/stint_orders_planner.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: ordinary per-node model verdicts in generic DAG execution are not used as the decisive S3* witness because they are part of the normal completion path and fail open on judge failure. The credited path is the stronger shipped `stint` audit structure.
- Boundary reachability: the Verifier is a declared role of the standard built-in `long-horizon-dev-stint` Playbook and executes through the ordinary Raven graph/runtime path.
- Claim being audited: the Builder's claim that current round tasks are implemented correctly and supported by the required project evidence/gates.
- Ordinary reporting path: `reports/round_{NN}.md`, including the Builder's `## Self-check`, plus the normal implementation/check results the Builder reports.
- Complementary access path: a fresh Verifier receives the runtime's independently executed check table, opens evidence itself, inspects areas the author could not independently validate, and reviews changed checks for self-confirming mistakes.
- Independence boundary: the Verifier starts with `session: fresh`, has separate owned report/evidence paths, cannot change product code or criteria, and is explicitly told not to accept the Builder's account as proof.
- Who acts on findings: the next Planner consumes every Verifier finding; severe/regression findings outrank ordinary work, and the Verifier can itself reopen a regressed task so it returns to the control loop.

## S4 — Outside-and-then intelligence

- State: —
- Function: no standard-runtime first-party path was established that models external/future-relevant change, develops a capability-adaptation option from it, and returns that option into Raven's current operating capability.
- Disturbance / variety regulated: Raven does observe users, conversations, tools, schedules, memory and task evidence, but the inspected credited runtime uses those distinctions for current task execution, reminders, task discovery and project control rather than a closed outside-and-then capability-adaptation conversation.
- Decisive decision or feedback right: choose a future-oriented change to the harness's capabilities/organization in response to external or prospective distinctions and return it into current operation.
- Decision owner: not established inside the credited standard runtime. Evolver can design/select harness changes but is explicitly a separate development tool; experimental curator surfaces are outside the credited standard boundary.
- Supporting / enforcement mechanisms: Sentinel planning, memory/attention state, Cron/Heartbeat, evaluation hooks, experimental curator machinery and Evolver benchmarks may supply sensing/evaluation or adjacent adaptation machinery, but none closes the required standard-runtime S4 path at this boundary.
- Closure path: no qualifying path established. Runtime observations can trigger present/follow-up work, while Evolver candidate promotion produces Git artifacts that still require separate review/deployment rather than feeding a standard Raven operating loop automatically.
- Why this is / is not agent-owned: proactive planning is not enough because it changes what work is attempted, not present capability; self-improvement tooling is not enough because the strongest first-party path is explicitly outside production runtime ownership.
- Evidence: [`docs-site/docs/proactivity.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/docs-site/docs/proactivity.md); [`docs-site/docs/evolver.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/docs-site/docs/evolver.md); [`CONTEXT.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/CONTEXT.md).
- Basis: explicit boundary statements + structural absence review.
- Confidence: medium-high.
- Caveats: Raven has unusually strong adjacent self-improvement R&D. A supported deployment that wires curator/evolver sensing, option generation and activation back into the live host could change this state; repository co-location alone is insufficient under Profile 0.2.4.

### Absence scope

- Surfaces inspected: README/runtime identity; `CONTEXT.md`; ordinary `AgentLoop`; subagent/DAG orchestration; built-in Playbooks and `stint`; Proactive Engine documentation; Evolver documentation; experimental curator/simulation import surface.
- Plausible first-party paths checked: Sentinel as prospective adaptation; memory/routine learning as S4; generic DAG replanning; `stint` multi-round project planning; Evolver as live self-improvement; `experimental/curator` as a standard deployed adaptation owner.
- Why no material first-party path remains: Sentinel and `stint` feed future/current work selection but do not adapt Raven capability; DAG replanning repairs a current task; Evolver is explicitly standalone and deployment-separated; the curator references inspected remain under experimental/simulation/test surfaces rather than an ordinary supported runtime assembly.

## S5 — Policy and identity

- State: P
- Function: the shipped `stint` mode contains a parent-governed closure for project-level specification/criteria/skeleton matters that agents are explicitly not authorized to settle; the legitimate person can answer, and that ruling returns into subsequent rounds.
- Disturbance / variety regulated: unresolved questions that would alter settled project decisions, criteria, or the plan skeleton; conflicts where current agent authority is intentionally insufficient to redefine what the project/run is trying to satisfy.
- Decisive decision or feedback right: make or revise the ultimate project-level ruling when the existing specification/settled decisions do not authorize the Planner to resolve the matter autonomously.
- Decision owner: the legitimate human/person running the `stint` project in the supported parent-governed mode. No autonomous Raven S5 owner is established for changing those ultimate criteria/skeleton decisions.
- Supporting / enforcement mechanisms: `.stint/HUMAN_DECISIONS.md` as a human-only decision file; Planner restrictions against changing criteria or skeleton; question ids and task blockers; pending-answer queue; round-boundary merge; automatic unblock of tasks whose human question has been answered; role/path enforcement.
- Closure path: agent encounters a specification/criteria/skeleton matter outside delegated authority → Planner records/raises a human question, optionally blocking affected tasks → legitimate person submits a ruling → answer is queued and merged before the next Planner round → human blockers are cleared and all roles read the returned decision → subsequent project operation follows the ruling.
- Why this is / is not agent-owned: the critical right is deliberately withheld from agents: the decision module describes `HUMAN_DECISIONS.md` as the one file no agent writes, while the Planner must escalate changes to skeleton/criteria rather than make them. The runtime transports and enforces the returned ruling but does not own it.
- Evidence: [`raven/templates/prompts/en/stint_orders_planner.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/raven/templates/prompts/en/stint_orders_planner.md); [`raven/stint/decisions.py`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/raven/stint/decisions.py); [`raven/playbook/builtin/long-horizon-dev-stint/playbook.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/raven/playbook/builtin/long-horizon-dev-stint/playbook.md).
- Basis: explicit + structural parent-closure path.
- Confidence: high for the `stint` parent mode; no autonomous S5 claim.
- Caveats: generic `confirm: true`, tool approvals, ordinary task feedback and user messages are not used as S5 evidence. The positive state is limited to questions that actually concern the project/run's ultimate specification, criteria or skeleton at this recursion.
- Boundary reachability: the human-decision ledger and answer-merge path are first-party parts of the shipped `stint` implementation and feed its ordinary next-round execution.
- Identity / ultimate-policy issue: changing settled specification/criteria or the plan skeleton that defines what the recursive project organization is allowed to pursue/accept, when that change cannot be derived from existing settled decisions.
- Ultimate authority in each claimed mode: Parent (`P`) mode — the legitimate human/person running the project; Base autonomous mode — no Raven agent is granted ultimate authority to rewrite these settled criteria/skeleton decisions.
- Return-to-operation path: human ruling is queued, merged into `.stint/HUMAN_DECISIONS.md` before the next Planner reads, any linked human blockers are removed, and the next round proceeds under the returned ruling.

## Distributed OSS parent arrangement

Raven's upstream maintainer organization, repository governance and code-review process are not imported as runtime S5. The assessment's parent claim is narrower and product-reachable: the `stint` project's legitimate person owns decisions agents are prohibited from making and can return those rulings through the shipped decision ledger. If a deployment substitutes an institution or higher-level service for that person, S5 ownership would have to be re-established for that deployment rather than inferred from GitHub maintainership.

The ordinary Raven operator also configures providers, channels, tools, permissions and Sentinel settings. Those configuration rights constrain the runtime but are not automatically S5; they become relevant only when they are the legitimate closure for an identity/ultimate-policy question at the declared recursion.

## Self-hosted and non-human modes

Raven can be self-hosted with local/remote providers and local or remote agent backends. That changes deployment ownership of infrastructure without changing the assessment logic: first-party `AgentLoop` S1 remains agent-owned when the model loop is active, deterministic permission/concurrency machinery remains supporting enforcement, and the `stint` Planner/Verifier roles retain their respective S3/S3* rights.

No non-human replacement for the `stint` parent S5 right was credited. A deployment could technically automate edits to configuration or decision files, but Profile 0.2.4 requires legitimate ultimate authority and a real policy/identity closure, not merely write access. Likewise, running Evolver or experimental curator beside a self-hosted Raven does not make S4 positive unless that deployment actually wires a qualifying outside-and-then adaptation loop into the assessed operating boundary.

## Recursion

Raven exposes several nested execution layers, but spawning or nesting alone is not treated as recursive viability. The main host turn is one operational recursion; specialized agents may be durable operational units when they own a meaningful local task environment. Generic DAG nodes remain delegated tasks unless the deployed organization gives them the durable contribution, identity and local regulatory capacity required by the Profile.

The strongest explicit recursive organization in the reviewed standard distribution is `mode: stint`: a project-level organization persists across rounds, carries backlog/journal/decision state, assigns current-control to Planner, operational implementation to Builder, complementary audit to Verifier, and retains a parent human decision path for matters outside delegated policy authority. This assessment credits the specific functions evidenced by that mode without asserting that each role is itself a complete viable system.

## Variety and escalation

Raven attenuates operational variety through context assembly, model/provider selection, tool registries, concurrency limits, worker rosters, DAG dependencies, Charters and role-specific path rights. It amplifies regulatory capacity through specialized agents, plugins/tools, persistent memory, background work, DAG fan-out and model-driven continuation/replanning.

The `stint` path has an explicit escalation hierarchy. Builder work is checked by the runtime and Verifier; Verifier findings return to Planner; regressions outrank ordinary work; questions outside delegated Planner authority can be recorded with a provisional ruling or block tasks for a person. Human answers are merged at a round boundary so policy changes do not race a role mid-turn. This preserves the distinction between current S3 control, S3* challenge, and parent S5 policy closure.

Generic failure/status events are not classified as algedonic channels merely because they are visible. A qualifying exceptional channel would need a demonstrated path that preserves the exceptional signal and reaches the authority appropriate to the type of issue. The `stint` regression/finding and blocked-human-question paths are stronger evidence of escalation structure, but the receiving function is still classified by the decision actually made.

## Evidence gaps

- S2 is the main classification edge. Raven has strong first-party DAG/worker primitives and explicitly documents the shared-write collision they must manage, but the frozen standard surface did not establish an autonomous conflict-specific S2 owner. The proposal therefore uses `C`; evidence that the host model systematically senses and resolves inter-worker interference could justify re-review.
- The repository contains substantial self-improvement work. The assessment deliberately does not borrow `evolver/` or `experimental/curator/` into standard-runtime S4. A public supported mode that activates those paths inside the normal host boundary would be material new evidence.
- Generic DAG completion verdicts are not used for S3* because the judge may fail open. The stronger `stint` Verifier path is the credited audit witness.
- S5=P is intentionally narrow: it depends on specification/criteria/skeleton questions in the recursive project organization. Generic approvals, `confirm: true`, permissions and operator configuration are not treated as S5 merely because a human can override them.
- The assessment is pinned to `e6c0344cb7ce00db25d554e4bb671ec1909a8f9f`; later upstream changes are outside this review boundary.

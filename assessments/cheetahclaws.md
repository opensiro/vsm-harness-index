---
harness_id: cheetahclaws
project_name: CheetahClaws
repository: https://github.com/SAIL-Research-Lab/cheetahclaws
review_ref: ec5d091b53c70f6685f1330f509b11c3a51aa214
reviewed_at: 2026-09-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-29
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: P
autonomy_s5: —
---

# CheetahClaws

## Review boundary

- System in focus: the first-party CheetahClaws installed/runtime distribution at frozen revision `ec5d091b53c70f6685f1330f509b11c3a51aa214`, including the ordinary agent/tool loop, bundled multi-agent/subagent tools, task state, Research Lab, and bundled trading workcell where those shipped modes are explicitly invoked.
- Purpose and identity: provide an extensible autonomous agent harness that can perform coding/general tool work and expose first-party multi-agent research/trading operating modes.
- Relevant environment: users, local repositories/filesystems, shells and web/search sources, external LLM providers, academic/search APIs, market data/outcomes, and optional external integrations.
- Standard-distribution boundary: CheetahClaws orchestration, agent loop, tool registry/dispatch, subagent manager, worktree creation/routing, task store, Research Lab orchestration/storage/meta-iteration, and bundled trading calibration/ML surfaces are inside. External model cognition, git itself, search/market-data providers, third-party sites, and the human operator are external actors even when first-party code routes decisions to/from them.
- Credited operating / distribution surfaces: ordinary model-driven tool turns; model-callable background subagents with optional git-worktree isolation; unattended Research Lab runs and optional `--iterate` daemon mode; bundled trading paper/calibration/ML workflow.
- Adjacent first-party surfaces excluded from ownership: repository development/governance, tests/CI, roadmap/spec documents, web UI observation by itself, deterministic quotas/permission checks by themselves, and domain labels such as PI/portfolio-manager unless the required VSM function is independently closed.
- First-party operating / deployment modes considered: interactive coding/general agent; parallel coder subagents using first-party worktree isolation; Research Lab single-run and queued daemon `--iterate`; trading paper/calibration/ML mode. These are supported alternative modes, not assumed to run simultaneously.
- Recursion level: the distribution is assessed as a harness capability surface. Parallel coder subagents are treated as temporary operational workcells only where they run full agent loops against separate repository workspaces and directly produce code outcomes. Research Lab and trading are recursive first-party workcells; their internal audit/adaptation paths are credited only where the path closes inside that shipped workcell.
- Reviewed revision: `ec5d091b53c70f6685f1330f509b11c3a51aa214`.
- Observation date: 2026-09-29.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

The ordinary CheetahClaws runtime is a model-driven agent loop. Each turn sends the active tool schemas to the configured model, records the returned tool calls, executes permitted tools, appends tool results to conversation state, and calls the model again until it returns without tool calls or a guard stops the loop. Permission checks, quota enforcement, retry/compaction and loop guards constrain this path but do not choose the agent's substantive next action.

The bundled multi-agent layer exposes `Agent`, `SendMessage`, `CheckAgentResult`, `ListAgentTasks` and related tools directly to the model. A spawned subagent runs the same first-party agent loop in its own history/thread. For parallel coding, the `Agent` tool supports `isolation="worktree"`: the runtime creates a separate git worktree/branch and routes that subagent's filesystem/shell context to it, explicitly for coding tasks that should not interfere.

Research Lab is a shipped multi-role workcell with Questioner, PI, Surveyor, Designer, Engineer, Analyst, Writer, reviewers and Lay Reader. Its normal pipeline includes producer/reviewer convergence. Separately, after finalization, `/lab iterate` (and the daemon for backlog rows queued with `--iterate`) runs a new final-report scoring pass across novelty/rigor/clarity/evidence; the weakest dimension deterministically selects an earlier stage, the run rewinds, and downstream artifacts are regenerated. The trading module is another bundled workcell: paper-trade outcomes feed calibration, and the documented operator workflow can train a persistent ML stacker on closed trades so future recommendations can have confidence overridden by empirical track record.

Primary evidence:

- [`README.md`](https://github.com/SAIL-Research-Lab/cheetahclaws/blob/ec5d091b53c70f6685f1330f509b11c3a51aa214/README.md)
- [`cheetahclaws/agent.py`](https://github.com/SAIL-Research-Lab/cheetahclaws/blob/ec5d091b53c70f6685f1330f509b11c3a51aa214/cheetahclaws/agent.py)
- [`cheetahclaws/multi_agent/tools.py`](https://github.com/SAIL-Research-Lab/cheetahclaws/blob/ec5d091b53c70f6685f1330f509b11c3a51aa214/cheetahclaws/multi_agent/tools.py)
- [`cheetahclaws/multi_agent/subagent.py`](https://github.com/SAIL-Research-Lab/cheetahclaws/blob/ec5d091b53c70f6685f1330f509b11c3a51aa214/cheetahclaws/multi_agent/subagent.py)
- [`cheetahclaws/task/tools.py`](https://github.com/SAIL-Research-Lab/cheetahclaws/blob/ec5d091b53c70f6685f1330f509b11c3a51aa214/cheetahclaws/task/tools.py)
- [`docs/guides/extensions.md`](https://github.com/SAIL-Research-Lab/cheetahclaws/blob/ec5d091b53c70f6685f1330f509b11c3a51aa214/docs/guides/extensions.md)
- [`docs/guides/research-lab.md`](https://github.com/SAIL-Research-Lab/cheetahclaws/blob/ec5d091b53c70f6685f1330f509b11c3a51aa214/docs/guides/research-lab.md)
- [`cheetahclaws/research/lab/orchestrator.py`](https://github.com/SAIL-Research-Lab/cheetahclaws/blob/ec5d091b53c70f6685f1330f509b11c3a51aa214/cheetahclaws/research/lab/orchestrator.py)
- [`cheetahclaws/research/lab/convergence.py`](https://github.com/SAIL-Research-Lab/cheetahclaws/blob/ec5d091b53c70f6685f1330f509b11c3a51aa214/cheetahclaws/research/lab/convergence.py)
- [`cheetahclaws/research/lab/iterate.py`](https://github.com/SAIL-Research-Lab/cheetahclaws/blob/ec5d091b53c70f6685f1330f509b11c3a51aa214/cheetahclaws/research/lab/iterate.py)
- [`docs/guides/trading.md`](https://github.com/SAIL-Research-Lab/cheetahclaws/blob/ec5d091b53c70f6685f1330f509b11c3a51aa214/docs/guides/trading.md)
- [`cheetahclaws/modular/trading/PLUGIN.md`](https://github.com/SAIL-Research-Lab/cheetahclaws/blob/ec5d091b53c70f6685f1330f509b11c3a51aa214/cheetahclaws/modular/trading/PLUGIN.md)
- [`cheetahclaws/modular/trading/agents/reflection.py`](https://github.com/SAIL-Research-Lab/cheetahclaws/blob/ec5d091b53c70f6685f1330f509b11c3a51aa214/cheetahclaws/modular/trading/agents/reflection.py)

## Operational model

In the ordinary agent mode, a user request enters a model/tool feedback loop and the model repeatedly decides which enabled tool to call after seeing prior results. The model may spawn one or more full-loop subagents, optionally in the background, inspect their status/results and send follow-up messages. In the parallel coding mode, it can place separate coder workcells in separate git worktrees so their concurrent file mutations do not collide. Research Lab and trading add first-party domain workcells with their own persistence and control loops, but domain planning/debate is not promoted to a metasystem function merely because role names sound managerial.

## S1 — Operations

- State: A
- Function: perform user-directed coding/general work through a closed autonomous model/tool loop.
- Disturbance / variety regulated: changing user requests, repository/file state, tool results, API errors, context pressure, external search results and intermediate execution failures.
- Decisive decision or feedback right: choose the next substantive tool/action or finish response after observing the current conversation and tool results.
- Decision owner: the configured model acting as the CheetahClaws agent.
- Supporting / enforcement mechanisms: active tool profiles, permission checks, quotas, retries, context compaction, parallel-safe dispatch, loop guards and persistent conversation state.
- Closure path: request → model decision/tool call → first-party dispatch → tool result appended to history → later model decision → outcome.
- Boundary reachability: this is the ordinary shipped `cheetahclaws` execution loop; no Research Lab/trading module or external child harness is required.
- Why this is / is not agent-owned: runtime code bounds and executes actions, but removing the model leaves no actor choosing materially equivalent substantive next actions.
- Evidence: [`cheetahclaws/agent.py`](https://github.com/SAIL-Research-Lab/cheetahclaws/blob/ec5d091b53c70f6685f1330f509b11c3a51aa214/cheetahclaws/agent.py); [`README.md`](https://github.com/SAIL-Research-Lab/cheetahclaws/blob/ec5d091b53c70f6685f1330f509b11c3a51aa214/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: provider internals are external; the credited autonomy is the first-party closed model/tool feedback path.

## S2 — Coordination

- State: A
- Function: attenuate destructive filesystem interference between distinct parallel coder operational workcells.
- Disturbance / variety regulated: two full-loop coder subagents working concurrently in the same repository can overwrite, dirty or otherwise interfere with the same working tree.
- Distinct S1 units: independently executing coder subagents, each with its own full CheetahClaws agent loop/history and bounded coding outcome.
- Inter-S1 disturbance: concurrent code/file mutations against one shared repository working tree.
- Attenuating coordination relation: the model-callable `Agent` tool exposes `isolation="worktree"`, explicitly intended for parallel coding tasks that should not interfere; the runtime creates a separate git worktree/branch and injects its path as the subagent's execution root.
- Feedback into subsequent S1 behaviour: the isolation decision changes where each subagent's Read/Write/Edit/Bash-style operations execute for the whole child run, so later actions occur against separate working copies; completion returns branch/worktree-associated results to the parent for later integration.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: credit is not for spawning or messaging workers. It is tied to an explicit parallel-file-mutation conflict and a first-party isolation mechanism whose purpose is to prevent that interference.
- Decisive decision or feedback right: decide whether a parallel coding child should be isolated in its own worktree rather than share the parent's workspace.
- Decision owner: the parent CheetahClaws agent model invoking the model-callable `Agent` tool and selecting the isolation mode.
- Supporting / enforcement mechanisms: `SubAgentManager`, git worktree creation/removal, per-child `_worktree_cwd`, background threads and result/status tracking.
- Closure path: anticipated parallel coding conflict → parent agent selects worktree isolation → runtime creates distinct workspaces/branches → child S1 tool activity is redirected → parent receives separated outcomes for subsequent integration.
- Boundary reachability: `Agent` is a shipped model-callable tool and worktree isolation is implemented by the first-party multi-agent package, not an example-only composition.
- Why this is / is not agent-owned: git/worktree machinery enforces separation, while the model owns the discretionary choice to invoke the S2 response for the parallel coding disturbance.
- Evidence: [`cheetahclaws/multi_agent/tools.py`](https://github.com/SAIL-Research-Lab/cheetahclaws/blob/ec5d091b53c70f6685f1330f509b11c3a51aa214/cheetahclaws/multi_agent/tools.py); [`cheetahclaws/multi_agent/subagent.py`](https://github.com/SAIL-Research-Lab/cheetahclaws/blob/ec5d091b53c70f6685f1330f509b11c3a51aa214/cheetahclaws/multi_agent/subagent.py); [`docs/guides/extensions.md`](https://github.com/SAIL-Research-Lab/cheetahclaws/blob/ec5d091b53c70f6685f1330f509b11c3a51aa214/docs/guides/extensions.md).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: ordinary subagent fan-out, message queues and task dependencies are not independently credited as S2; the positive witness is restricted to the explicit worktree-interference path.

## S3 — Inside-and-now control

- State: —
- Function: no material first-party autonomous or constructor path was established for whole-system current control over multiple operational units' shared resources, commitments, priorities or accountability at the reviewed boundary.
- Disturbance / variety regulated: not established beyond local parent-task decomposition, static budgets/permissions and deterministic workflow progression.
- Decisive decision or feedback right: not established.
- Decision owner: not applicable.
- Supporting / enforcement mechanisms: `Task*` state, `ListAgentTasks`, `CheckAgentResult`, `SendMessage`, quotas/permissions, Research Lab stage state/budgets and deterministic convergence thresholds provide useful execution control but do not establish the required S3 discretion.
- Closure path: not established.
- Why this is / is not agent-owned: the main agent can delegate, inspect worker status and send follow-ups, but Methodology 0.3.6 does not treat worker selection/delegation/result collection as S3 by itself. Research Lab's stage transitions are largely predetermined/deterministic workflow control rather than a whole-system resource/commitment bargaining function owned by a supervisor agent.
- Evidence: [`cheetahclaws/task/tools.py`](https://github.com/SAIL-Research-Lab/cheetahclaws/blob/ec5d091b53c70f6685f1330f509b11c3a51aa214/cheetahclaws/task/tools.py); [`cheetahclaws/multi_agent/tools.py`](https://github.com/SAIL-Research-Lab/cheetahclaws/blob/ec5d091b53c70f6685f1330f509b11c3a51aa214/cheetahclaws/multi_agent/tools.py); [`cheetahclaws/research/lab/orchestrator.py`](https://github.com/SAIL-Research-Lab/cheetahclaws/blob/ec5d091b53c70f6685f1330f509b11c3a51aa214/cheetahclaws/research/lab/orchestrator.py); [`cheetahclaws/research/lab/convergence.py`](https://github.com/SAIL-Research-Lab/cheetahclaws/blob/ec5d091b53c70f6685f1330f509b11c3a51aa214/cheetahclaws/research/lab/convergence.py).
- Basis: explicit + structural negative finding.
- Confidence: medium-high.
- Caveats: a developer could build a supervisor from generic task/subagent primitives, but general framework expressiveness is below the `C` threshold.

### Absence scope

- Surfaces inspected: ordinary agent loop; multi-agent spawn/status/message tools; task lifecycle/dependencies; quotas/permissions; Research Lab PI, stage driver, convergence/budget logic and continuous-run controls; bundled trading role pipeline.
- Plausible first-party paths checked: parent-agent worker supervision, task-board ownership, Research Lab PI decisions, deterministic stage/budget control, trading Portfolio Manager/Risk labels and operator controls.
- Why no material first-party path remains: the reviewed paths either decompose one parent operation, expose status/messaging, enforce preselected limits, or implement domain/workflow decisions. None supplies a whole-system present-tense S3 view plus an autonomous/current-control decision right over shared organizational commitments/resources with returned closure.

## S3* — Complementary audit

- State: A
- Function: challenge a finalized Research Lab operational artifact through a separate post-finalization quality audit and feed the finding back into corrective work.
- Disturbance / variety regulated: a paper can pass ordinary per-stage producer/reviewer convergence yet remain weak as an integrated final artifact in novelty, rigor, clarity or evidence.
- Claim being audited: the quality of the already-finalized report after the ordinary stage graph has completed.
- Ordinary reporting path: stage producers create artifacts; ordinary stage reviewers drive producer/revision convergence; finalization writes the report.
- Complementary access path: `/lab iterate` starts after finalization and asks a reviewer pool to score the complete final report independently across four explicit dimensions; documented model assignment prefers heterogeneous reviewer families to reduce shared blind spots.
- Independence boundary: the audit is a separate post-finalization pass, uses reviewer roles rather than the producing agent, operates over the integrated final artifact rather than one in-flight stage draft, and can use different model families. It is not credited from the ordinary mandatory stage reviewer loop alone.
- Who acts on findings: the reviewer agents supply the dimension scores; first-party meta-loop code aggregates them, selects the weakest dimension, rewinds to a mapped earlier stage and reruns downstream work. In daemon `--iterate` mode this closes unattended.
- Decisive decision or feedback right: independent reviewer agents judge the final artifact's novelty/rigor/clarity/evidence quality; deterministic routing translates the weakest returned judgment into the corrective stage.
- Decision owner: autonomous reviewer-model pool for the audit judgment.
- Supporting / enforcement mechanisms: `lab_iterations` history, score parsing/aggregation, dimension-to-stage map, persisted artifacts, `resume_run`, max/target/plateau/budget guards and backlog daemon.
- Closure path: finalized report → independent reviewer scores → weakest dimension → stage rewind → regenerated operational artifacts/report → later iteration re-audits the result.
- Boundary reachability: `/lab iterate` is a shipped command and the bundled daemon automatically invokes it for backlog work queued with `--iterate`; no development-only evaluator is borrowed.
- Why this is / is not agent-owned: runtime code routes and bounds the audit, but removing the reviewer models removes the substantive quality judgment that determines which dimension is weak.
- Evidence: [`docs/guides/research-lab.md`](https://github.com/SAIL-Research-Lab/cheetahclaws/blob/ec5d091b53c70f6685f1330f509b11c3a51aa214/docs/guides/research-lab.md); [`cheetahclaws/research/lab/iterate.py`](https://github.com/SAIL-Research-Lab/cheetahclaws/blob/ec5d091b53c70f6685f1330f509b11c3a51aa214/cheetahclaws/research/lab/iterate.py); [`cheetahclaws/research/lab/orchestrator.py`](https://github.com/SAIL-Research-Lab/cheetahclaws/blob/ec5d091b53c70f6685f1330f509b11c3a51aa214/cheetahclaws/research/lab/orchestrator.py).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: reviewers share possible pretrained blind spots, acknowledged by the project. Citation verification alone is not the closure witness because that stage records findings and advances; the positive path is the separate final-artifact audit with targeted rewind.

## S4 — Outside-and-then intelligence

- State: P
- Function: adapt the bundled trading workcell's future decision capability using empirical outcomes from the external market under an explicit operator-owned adaptation decision.
- Disturbance / variety regulated: the trading agents' confidence/recommendation process may be systematically miscalibrated as real market outcomes reveal whether past high/low-confidence calls carried signal.
- External distinction: closed paper-trade outcomes and market-relative performance provide empirical evidence about whether prior recommendations actually worked; calibration reports hit-rate/signal quality and the stacker trains on closed trades.
- Future / prospective distinction: the documented workflow evaluates historical performance specifically to decide whether to change future recommendation weighting rather than merely explain the completed trade.
- Adaptation option generated: train/persist the bundled LightGBM (sklearn fallback) stacker so future confidence can be overridden when historical track record argues against the LLM's confidence.
- Path back into current capability / S3: operator reviews calibration and invokes `/trading ml train`; first-party code persists `stacker.pkl`; subsequent trading analyses can use the trained model to change confidence presented to current decision-making.
- Decisive decision or feedback right: decide whether empirical calibration is sufficient to train/adopt the learned stacker into future operation.
- Decision owner: parent human/operator in the documented trading workflow; no autonomous first-party actor is shown owning the train/adopt decision.
- Supporting / enforcement mechanisms: paper-trade persistence, calibration metrics, closed-trade feature engineering, ML training/persistence and inference hooks.
- Closure path: external trade outcomes → calibration/performance distinction → operator adaptation judgment → `/trading ml train` → persisted stacker → future recommendation confidence altered.
- Boundary reachability: trading is a bundled first-party module with documented commands/storage and a recommended monthly calibration→train workflow; it is not repository-development learning.
- Why this is / is not agent-owned: market-facing analysis and BM25 memory are not themselves credited as S4. The evidenced adaptation decision that changes capability remains explicitly operator-triggered, so parent-only notation is appropriate.
- Evidence: [`docs/guides/trading.md`](https://github.com/SAIL-Research-Lab/cheetahclaws/blob/ec5d091b53c70f6685f1330f509b11c3a51aa214/docs/guides/trading.md); [`cheetahclaws/modular/trading/PLUGIN.md`](https://github.com/SAIL-Research-Lab/cheetahclaws/blob/ec5d091b53c70f6685f1330f509b11c3a51aa214/cheetahclaws/modular/trading/PLUGIN.md); [`cheetahclaws/modular/trading/agents/reflection.py`](https://github.com/SAIL-Research-Lab/cheetahclaws/blob/ec5d091b53c70f6685f1330f509b11c3a51aa214/cheetahclaws/modular/trading/agents/reflection.py).
- Basis: explicit + structural.
- Confidence: medium.
- Caveats: Research Lab literature search is operational research, not credited as S4; generic memory/reflection is not enough. The positive path is limited to the documented external-outcome calibration and parent-triggered capability adaptation.

## S5 — Policy and identity

- State: —
- Function: no material first-party runtime path was established for identity/ultimate-policy issues to reach legitimate ultimate authority and return as governing policy for subsequent CheetahClaws operation.
- Disturbance / variety regulated: not established at identity/ultimate-policy level.
- Decisive decision or feedback right: not established.
- Decision owner: not applicable.
- Supporting / enforcement mechanisms: permission modes, user confirmations, tool profiles, quotas, lab budgets/model overrides, prompts/configuration and trading risk limits constrain operation but do not by themselves supply S5 closure.
- Closure path: not established.
- Why this is / is not agent-owned: ordinary action approval/configuration and static policy-like limits remain below the S5 threshold; no shipped identity-level escalation/governance loop was found.
- Evidence: [`cheetahclaws/agent.py`](https://github.com/SAIL-Research-Lab/cheetahclaws/blob/ec5d091b53c70f6685f1330f509b11c3a51aa214/cheetahclaws/agent.py); [`docs/guides/research-lab.md`](https://github.com/SAIL-Research-Lab/cheetahclaws/blob/ec5d091b53c70f6685f1330f509b11c3a51aa214/docs/guides/research-lab.md); [`cheetahclaws/modular/trading/PLUGIN.md`](https://github.com/SAIL-Research-Lab/cheetahclaws/blob/ec5d091b53c70f6685f1330f509b11c3a51aa214/cheetahclaws/modular/trading/PLUGIN.md).
- Basis: explicit + structural negative finding.
- Confidence: medium-high.
- Caveats: users remain ultimate operators in practice, but Methodology 0.3.6 requires a first-party identity/ultimate-policy return loop rather than generic human control.

### Absence scope

- Surfaces inspected: ordinary permission/tool-profile/quota controls; subagent/task system; Research Lab roles, budgets, model overrides, abort/resume/daemon controls; trading risk/calibration/configuration surfaces; project docs describing supported modes.
- Plausible first-party paths checked: permission prompts, plan/accept-all modes, user configuration, PI/Portfolio Manager naming, lab budget/model control, trading risk verifier and operator commands.
- Why no material first-party path remains: these paths govern ordinary actions, workflow settings, resource ceilings or domain decisions. None reconstructs an identity- or ultimate-policy-level issue → legitimate authority → authoritative decision → returned governing policy loop at the assessed harness boundary.

## Recursion

The ordinary CheetahClaws agent is one S1 loop. Full-loop coder subagents can temporarily form multiple operational workcells; the S2 claim is limited to that explicit parallel-worktree mode and does not infer viability from spawning alone. Research Lab and trading are bundled recursive workcells with their own persistence and meta-loops. Their S3* and S4 witnesses are credited at those workcell recursions while remaining inside the first-party distribution boundary.

## Variety and escalation

Runtime variety is bounded with permissions, quotas, context compaction, retries, loop guards, tool-profile filtering, subagent depth/concurrency limits and Research Lab budget/round ceilings. These mechanisms are recorded as enforcement rather than automatically receiving VSM ownership. User permission denials and abort controls provide operational escalation/intervention but do not establish S5.

## Evidence gaps / terminal outcome

Proposed vector: `S1=A / S2=A / S3=— / S3*=A / S4=P / S5=—`.

The key distinctions are deliberately narrow. S2 is not inferred from fan-out or task dependencies; it rests on agent-selected worktree isolation for an explicit parallel coding interference mode. S3 is withheld because worker supervision and deterministic stage progression remain below whole-system current-control semantics. S3* rests on the optional post-finalization audit-and-rewind loop rather than routine stage review. S4 is limited to the parent-triggered empirical calibration→trained-stacker adaptation path; literature search and memory alone are not credited. S5 is not inferred from permissions, prompts, configuration or risk rules.
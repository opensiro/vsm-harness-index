---
harness_id: mingbird
project_name: Mingbird
repository: https://github.com/Mingbird/Mingbird-agent
review_ref: 2e62a735b212aee3c72bce83134042c9ca885237
reviewed_at: 2026-09-26
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-26
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Mingbird

## Review boundary

- System in focus: one first-party Mingbird local agent deployment at pinned revision `2e62a735b212aee3c72bce83134042c9ca885237`, including the ordinary model/tool execution loop, session/todo persistence, completion/anti-loop/time-budget guards, file/command/web/MCP/skill tools, safety/approval machinery, rollback paths, and the shipped optional parallel sub-agent dispatch/integration mode.
- Purpose and identity: complete user tasks on a local workstation through a small-model-oriented autonomous tool loop while the harness supplies context management, safety, progress/completion backstops and optional bounded parallel execution for simple independent work.
- Relevant environment: user objectives, local files/processes and working directory, local Ollama or optional configured model endpoint, configured MCP/web services, machine memory/capacity, and persisted session/todo state.
- Standard-distribution boundary: Apache-2.0 product/runtime code and documented first-party desktop, CLI and Web UI modes at the frozen revision. Benchmark runners/results, repository-development CI/tests, release engineering and arbitrary downstream MCP servers are adjacent unless the frozen product runtime directly wires their mechanism into ordinary execution.
- Credited operating / distribution surfaces: ordinary `ollama_agent.py` task/chat loop; built-in tools, context/session/todo machinery, finish/anti-loop/time-budget/safety gates; desktop/CLI/Web surfaces backed by that engine; configurable first-party parallel dispatch using `parallel_todo.py`, `parallel_probe.py`, `parallel_dispatch.py`, `parallel_safety.py` and `parallel_config.py`, including child partition directories, bounded child processes, acceptance, integration and serial fallback.
- Adjacent first-party surfaces excluded from ownership: LRAB/τ²/frontier-probe benchmark programs and benchmark scoring; repository pytest/CI and release checks; benchmark ablation infrastructure; documentation claims not corroborated by frozen product code; external model providers, search engines and arbitrary MCP servers as organizational owners.
- First-party operating / deployment modes considered: ordinary single-agent local/cloud-configured execution; resumed sessions; attended and unattended safety modes; offline mode; task timeboxing; and the shipped parallel-dispatch mode when explicitly configured with a child model and enabled. Parallel dispatch is off by default, but is a released first-party mode rather than test-only code.
- Recursion level: one Mingbird task/session. The main model/tool loop is an S1 operational unit. In enabled parallel mode, each bounded headless child agent executing a distinct todo item in its own partition directory is another temporary S1 operational unit for the duration of that batch. Metasystemic credit is assigned only where the relation among those operations meets the Profile threshold.
- Reviewed revision: `2e62a735b212aee3c72bce83134042c9ca885237`.
- Observation date: 2026-09-26.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Mingbird's normal runtime is a repeated model/tool feedback loop specialized for small local models. The model receives task/session context, selects substantive tool calls or output, the harness executes or refuses those actions under workspace/safety rules, and returned results/errors become later model evidence. Todo state, checkpoints/session history, context compaction, anti-loop recovery, precise failure feedback, task timeboxing and the finish gate support that S1 loop without replacing its substantive next-action judgment.

The released parallel path is first-party but deliberately disabled until configured. At the start of a fresh non-Q&A task, harness code can inspect the current todo set, classify only bounded mechanical single-file items as dispatchable, apply hard veto/safety checks, and verify machine/model capacity. It then spawns bounded headless child instances into separate partition directories with lower permissions, no nested dispatch and hard timeouts. Children therefore perform distinct bounded operational outcomes while being structurally prevented from editing one another's or the parent workspace directly.

The dispatcher/integrator closes a concrete coordination relation. Concurrent child outputs are first created in isolated partitions. The runtime deterministically checks process completion, child completion markers, audit state and claimed/actual artifacts; successful outputs are copied back only through the integrator. Existing parent files are not overwritten by default, conflicts remain unintegrated, accepted todo items are marked done, and failed children are retried once or returned to the main model for serial completion. This specifically attenuates cross-child/parent write collision and ambiguous integration rather than merely providing generic delegation. The decisive admission/isolation/integration response, however, is a configured deterministic policy; no autonomous agent owns that coordination discretion. Under Methodology 0.3.6 this is S2=`C`, not `A`.

The same machinery is not promoted to S3. It tracks child lifecycle and applies predefined timeout/retry/fallback/safety rules, but it does not expose to an autonomous controller a live whole-system current view with discretionary authority to renegotiate priorities, commitments or resources across the running organization. The main model gets the integrated/fallback summary after the dispatch path; it is intentionally unaware of the mechanism before dispatch and cannot list, steer, reassign or selectively interrupt live children. A generic user stop or fixed circuit breaker does not establish whole-system current control.

Nor is the deterministic acceptance pass promoted to S3*. It is the routine production integration path for the very child results being admitted. Artifact existence checks, completion markers and the child safety audit are ordinary validation/enforcement inside that path, not a materially independent complementary channel capable of challenging routine operational reporting from a separate access boundary. The delivery self-check similarly re-injects the original task into the same main model loop and is an S1 completion backstop rather than independent audit.

No qualifying S4 or S5 closure was found. Web/MCP/retrieval and model selection expand current task capability but do not close an outside-and-then organizational adaptation loop. Safety policy, permissions, offline mode, configuration and user confirmations constrain action but do not provide an identity/ultimate-policy issue path to legitimate authority and back into subsequent operation.

Primary evidence:

- [`ollama_agent.py`](https://github.com/Mingbird/Mingbird-agent/blob/2e62a735b212aee3c72bce83134042c9ca885237/ollama_agent.py) — ordinary model/tool loop and product guards; child mode; standard hook that invokes parallel planning, dispatch, integration and returns a summary to the main loop.
- [`parallel_todo.py`](https://github.com/Mingbird/Mingbird-agent/blob/2e62a735b212aee3c72bce83134042c9ca885237/parallel_todo.py) — deterministic todo classification, negative veto/safety precheck and dispatch-plan construction.
- [`parallel_dispatch.py`](https://github.com/Mingbird/Mingbird-agent/blob/2e62a735b212aee3c72bce83134042c9ca885237/parallel_dispatch.py) — child partitioning/lifecycle, hard timeout/abort, acceptance, retry/fallback, conflict-safe result integration and parent summary.
- [`parallel_safety.py`](https://github.com/Mingbird/Mingbird-agent/blob/2e62a735b212aee3c72bce83134042c9ca885237/parallel_safety.py) — lower-permission child boundary, path/command protection, audit records and severe-violation circuit breaker.
- [`parallel_config.py`](https://github.com/Mingbird/Mingbird-agent/blob/2e62a735b212aee3c72bce83134042c9ca885237/parallel_config.py) — released configurable parallel mode, default-off switch, child-model/capacity/concurrency limits, no-overwrite default and retry/depth/safety policy.
- [`tests/test_parallel_dispatch.py`](https://github.com/Mingbird/Mingbird-agent/blob/2e62a735b212aee3c72bce83134042c9ca885237/tests/test_parallel_dispatch.py) — verifies isolated child execution, deterministic acceptance, missing-artifact rejection, timeout/abort, retry/fallback, severe-violation handling and no-overwrite conflict behavior.
- [`README.md`](https://github.com/Mingbird/Mingbird-agent/blob/2e62a735b212aee3c72bce83134042c9ca885237/README.md) — supported product modes, task loop capabilities, completion/safety mechanisms and released parallel-subagent safety boundary.
- [`CHANGELOG.md`](https://github.com/Mingbird/Mingbird-agent/blob/2e62a735b212aee3c72bce83134042c9ca885237/CHANGELOG.md) — parallel dispatch as a released v1.3.0 feature, explicitly off by default, with partitioned lower-permission children, deterministic acceptance and serial fallback; delivery self-check/anti-loop history.
- [`AGENTS.md`](https://github.com/Mingbird/Mingbird-agent/blob/2e62a735b212aee3c72bce83134042c9ca885237/AGENTS.md) — standard autonomous task/tool operation, persistence, skills/MCP and supported CLI/product boundary.

## Operational model

The main Mingbird model is the ordinary S1 owner: it selects substantive actions and adapts from returned tool/environment evidence. In the optional parallel mode, the harness may temporarily create several lower-permission child S1s for mechanically bounded todo items. Deterministic first-party code decides which items are eligible, enforces partition isolation/capacity/safety, validates their outputs, prevents silent integration conflicts and returns accepted/fallback outcomes to the main loop. This provides an S2 constructor path but not an agent-owned coordinator or a live S3 controller.

## S1 — Operations

- State: A
- Function: transform a user task into file/process/research/data outcomes through repeated model-selected tool actions and feedback.
- Disturbance / variety regulated: changing task requirements, local workspace/process state, tool results and errors, model output, context pressure, safety refusals, user follow-up, time budget and resumed session state.
- Decisive decision or feedback right: choose the next substantive task action/tool and revise later action from returned operational evidence.
- Decision owner: the active Mingbird model agent in the main loop, and the bounded child model within its delegated child task when parallel mode is active.
- Supporting / enforcement mechanisms: tool registry, workspace/safety gates, todo/session persistence, context compaction, anti-loop and failure feedback, finish gate, task time budget, model/provider adapter and UI/CLI/Web front ends.
- Closure path: task/context enters the model loop → model selects an action/tool → runtime executes/refuses and returns exact result/error → the result becomes subsequent model context → model revises the next action → environment/task state changes until completion or bounded exit.
- Boundary reachability: `ollama_agent.py` is the shared product engine behind the documented source/CLI execution and is invoked by the released desktop/Web surfaces; parallel children invoke the same first-party agent entry under narrowed configuration.
- Why this is / is not agent-owned: deterministic guards decide whether an attempted action is permitted and supply recovery hints, but removing the model removes the substantive next-action selection and interpretation of tool feedback.
- Evidence: [`ollama_agent.py`](https://github.com/Mingbird/Mingbird-agent/blob/2e62a735b212aee3c72bce83134042c9ca885237/ollama_agent.py); [`README.md`](https://github.com/Mingbird/Mingbird-agent/blob/2e62a735b212aee3c72bce83134042c9ca885237/README.md); [`AGENTS.md`](https://github.com/Mingbird/Mingbird-agent/blob/2e62a735b212aee3c72bce83134042c9ca885237/AGENTS.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: Ollama or an optional cloud endpoint supplies inference, but Mingbird supplies the first-party loop, tool execution, state and feedback closure.

## S2 — Coordination

- State: C
- Function: attenuate interference among concurrently executing child S1s and the parent workspace by admitting only bounded independent work, isolating each child in a separate partition and integrating accepted outputs without silent overwrite.
- Disturbance / variety regulated: concurrently delegated child tasks could write into shared state, collide with one another or overwrite existing parent artifacts; failed/unsafe child work could also be integrated as if successful.
- Decisive decision or feedback right: determine which pending items are safe/independent enough for parallel dispatch, bind them to isolated child workspaces, accept/reject their outputs for integration and return failed/conflicting work to serial execution.
- Decision owner: no autonomous S2 actor owns this discretion in the shipped mode; eligibility, safety, isolation and integration follow configured deterministic first-party rules. Main-model `[simple]`/complexity annotations can only narrow eligibility and cannot override hard veto/safety rules.
- Supporting / enforcement mechanisms: `TodoProvider`, deterministic task classifier/safety precheck, capacity probe, one partition directory per child, lower-permission child sandbox, concurrency/depth caps, acceptance checks, `ResultIntegrator`, no-overwrite default, retry and fallback summary.
- Closure path: multiple pending todo items exist → deterministic classifier/safety/capacity path selects eligible independent items → dispatcher executes each child in a separate partition → acceptance/integration inspects completion/audit/artifacts and refuses conflicts → accepted artifacts enter the parent workspace while failed/conflicting items return to main-model serial work → subsequent S1 execution sees the integrated/fallback state.
- Boundary reachability: parallel dispatch is released product code documented in the v1.3.0 changelog and called directly from the ordinary main agent loop when the first-party `parallel` configuration is enabled; it does not require a downstream extension, although it is disabled by default and requires a configured child model.
- Distinct S1 units: the main model/tool loop plus two or more concurrently spawned headless child `ollama_agent.py` loops, each receiving one bounded todo item and its own partition directory/session under the same product runtime.
- Inter-S1 disturbance: without partition/integration control, concurrently writing children could alter shared files or produce outputs that conflict with one another or with an existing parent artifact; unsafe/failed children could also contaminate shared task state.
- Attenuating coordination relation: each child is structurally limited to its own partition; outputs are admitted only after deterministic acceptance; the integrator refuses overwrite conflicts by default and copies only accepted artifacts back to the parent workspace.
- Feedback into subsequent S1 behaviour: accepted work is copied into the parent workspace and todo state is marked complete; rejected, timed-out, conflicting or failed work is reported/fallen back to the main model, changing what the main S1 must execute next.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the credited path is tied to an evidenced multi-S1 shared-write/integration disturbance and specifically separates operational workspaces plus conflict-safe admission; parallel spawning or todo decomposition alone is not credited.
- Why this is / is not agent-owned: the first-party S2-specific relation is complete enough to regulate the disturbance, but the coordination choice is a deterministic/configured runtime policy rather than autonomous agent discretion. A downstream/developer composition would need to supply an autonomous coordinator/authority to move this path from `C` to `A`.
- Evidence: [`parallel_todo.py`](https://github.com/Mingbird/Mingbird-agent/blob/2e62a735b212aee3c72bce83134042c9ca885237/parallel_todo.py); [`parallel_dispatch.py`](https://github.com/Mingbird/Mingbird-agent/blob/2e62a735b212aee3c72bce83134042c9ca885237/parallel_dispatch.py); [`parallel_safety.py`](https://github.com/Mingbird/Mingbird-agent/blob/2e62a735b212aee3c72bce83134042c9ca885237/parallel_safety.py); [`parallel_config.py`](https://github.com/Mingbird/Mingbird-agent/blob/2e62a735b212aee3c72bce83134042c9ca885237/parallel_config.py); [`tests/test_parallel_dispatch.py`](https://github.com/Mingbird/Mingbird-agent/blob/2e62a735b212aee3c72bce83134042c9ca885237/tests/test_parallel_dispatch.py); [`CHANGELOG.md`](https://github.com/Mingbird/Mingbird-agent/blob/2e62a735b212aee3c72bce83134042c9ca885237/CHANGELOG.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: the mode is off by default and the runtime's configured policy, not a model agent, owns the coordination response; this is why the positive state is Constructor rather than Autonomous.

## S3 — Inside-and-now control

- State: —
- Function: no material first-party whole-system inside-and-now current-control loop is established over the temporary main/child organization.
- Disturbance / variety regulated: the dispatcher observes child lifecycle, safety violations, timeouts and success/failure, but these facts feed a fixed batch-execution policy rather than a current-control authority that regulates commitments/resources/priorities on behalf of the whole.
- Decisive decision or feedback right: not established for discretionary whole-system current control.
- Decision owner: none established for S3 at this boundary.
- Supporting / enforcement mechanisms: capacity calculation, hard concurrency cap, child status records, progress events, timeout/abort, retry, severe-violation circuit breaker, integration and fallback are deterministic batch-supervision machinery.
- Closure path: not applicable; there is no reviewed loop of whole-system current state → S3 judgment over shared commitments/resources/priorities → intervention/reallocation → renewed whole-system feedback.
- Whole-system current view: internal dispatcher state tracks pending/running/completed children and emits progress, but the standard model agent is intentionally not given a live child-control surface; it receives the dispatch/integration result after the path completes.
- Current-control decision scope: predefined code may kill a timed-out/unsafe child, retry, abort on load failure or fall back to serial execution, but there is no first-party agent/controller that can inspect the live organization and choose/revise priorities, assignments, budgets or interventions from that view.
- Why this is / is not agent-owned: the reviewed mechanisms enforce static configured batch rules. The Profile explicitly distinguishes such scheduler/kill/retry enforcement from ownership of a whole-system current-control decision.
- Evidence: [`parallel_dispatch.py`](https://github.com/Mingbird/Mingbird-agent/blob/2e62a735b212aee3c72bce83134042c9ca885237/parallel_dispatch.py); [`ollama_agent.py`](https://github.com/Mingbird/Mingbird-agent/blob/2e62a735b212aee3c72bce83134042c9ca885237/ollama_agent.py); [`tests/test_parallel_dispatch.py`](https://github.com/Mingbird/Mingbird-agent/blob/2e62a735b212aee3c72bce83134042c9ca885237/tests/test_parallel_dispatch.py).
- Basis: explicit + structural absence review
- Confidence: high
- Caveats: fixed exception handling is operationally useful and can stop/retry work, but the Methodology does not equate process supervision or a kill switch with S3.

### Absence scope

- Surfaces inspected: main agent loop, parallel trigger/dispatcher/integrator, child lifecycle/status/progress, capacity limits, timeout/abort/retry/fallback, todo/session state and user-facing desktop/CLI/Web product claims.
- Plausible first-party paths checked: live child-tree supervision by the main model, deployment-wide resource bargaining, dynamic child priority/reassignment/steering, operator whole-system current-control path and exception-driven reallocation.
- Why no material first-party path remains: the released parallel path deliberately hides child orchestration from the model until its result summary and supplies deterministic batch rules rather than a live whole-system discretionary control surface.

## S3* — Complementary audit

- State: —
- Function: no material first-party complementary-audit channel sufficiently independent of ordinary Mingbird production validation is established.
- Disturbance / variety regulated: completion errors and unsafe/missing/conflicting artifacts are checked, but the reviewed checks are ordinary admission/safety mechanisms inside the same production path rather than a complementary challenge to routine S1/S3 reporting.
- Decisive decision or feedback right: not established for an independent audit judgment.
- Decision owner: none established for S3*.
- Supporting / enforcement mechanisms: child audit log, deterministic `_judge` acceptance, artifact/claim existence checks, integration conflict detection, tests, delivery self-check and `.bak`/trash rollback.
- Closure path: not applicable as S3*; production checks can reject/retry/fallback work, but no materially independent audit access/judgment channel is established beyond the routine execution/integration path.
- Claim being audited: child completion/safety/artifact claims and main-agent task completion were the plausible audit targets inspected.
- Ordinary reporting path: child process exit/completion marker, produced artifacts/audit events and the main agent's normal finish path are the standard operational records used to decide continuation/integration.
- Complementary access path: no separate first-party auditor with an independent sensor/access boundary is wired into standard operation. The integrator reads the same child partition/output/audit data as part of mandatory admission, and the delivery self-check reuses the same main model loop.
- Independence boundary: not established; acceptance and finish checks belong to the production control path they validate, while repository benchmarks/pytest are adjacent development/evaluation systems.
- Who acts on findings: deterministic production code retries/rejects/falls back, and the main model continues from returned failures; no independent audit owner supplies a complementary finding.
- Why this is / is not agent-owned: because the complementary-audit function itself is not established, ownership is not promoted from routine deterministic validation.
- Evidence: [`parallel_dispatch.py`](https://github.com/Mingbird/Mingbird-agent/blob/2e62a735b212aee3c72bce83134042c9ca885237/parallel_dispatch.py); [`parallel_safety.py`](https://github.com/Mingbird/Mingbird-agent/blob/2e62a735b212aee3c72bce83134042c9ca885237/parallel_safety.py); [`ollama_agent.py`](https://github.com/Mingbird/Mingbird-agent/blob/2e62a735b212aee3c72bce83134042c9ca885237/ollama_agent.py); [`CHANGELOG.md`](https://github.com/Mingbird/Mingbird-agent/blob/2e62a735b212aee3c72bce83134042c9ca885237/CHANGELOG.md).
- Basis: explicit + structural absence review
- Confidence: high
- Caveats: this conclusion does not deny that the acceptance pass verifies reality; it says the verification is routine production admission rather than the Profile's complementary S3* relation.

### Absence scope

- Surfaces inspected: child safety audit, dispatch acceptance/integration, finish/delivery self-check, rollback, session history, benchmark/evaluation directories and regression tests.
- Plausible first-party paths checked: independent reviewer/evaluator actor, raw-artifact challenge distinct from ordinary admission, sampled replay/reconciliation, benchmark feedback into live control and a separate audit authority.
- Why no material first-party path remains: standard runtime validation is in-band and mandatory, while benchmark/pytest/evaluation surfaces are adjacent repository-development systems and are not wired as a complementary operational audit loop.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party outside-and-then organizational adaptation loop is established at the assessed session/deployment recursion.
- Disturbance / variety regulated: Mingbird can search/fetch the web, use MCP/skills, choose/configure models and preserve sessions, but these mechanisms support current tasks rather than prospective redesign of the harness organization.
- Decisive decision or feedback right: not established for selecting and adopting an organizational adaptation from external/future distinctions.
- Decision owner: none established for S4.
- Supporting / enforcement mechanisms: web tools, MCP, skills, model/configuration selection, memory/session state, benchmark/evaluation material and runtime caching.
- Closure path: not applicable; no reviewed standard path closes external/future sensing → adaptation option → present capability/S3 change → subsequent operational feedback.
- Why this is / is not agent-owned: a model may autonomously research an external fact for its current task, but that is S1 task activity without evidence that the organization itself is being prospectively adapted.
- Evidence: [`README.md`](https://github.com/Mingbird/Mingbird-agent/blob/2e62a735b212aee3c72bce83134042c9ca885237/README.md); [`AGENTS.md`](https://github.com/Mingbird/Mingbird-agent/blob/2e62a735b212aee3c72bce83134042c9ca885237/AGENTS.md); [`ollama_agent.py`](https://github.com/Mingbird/Mingbird-agent/blob/2e62a735b212aee3c72bce83134042c9ca885237/ollama_agent.py).
- Basis: explicit + structural absence review
- Confidence: high
- Caveats: the repository's benchmark-driven development history is evidence about project engineering, not an operational S4 owner in one frozen Mingbird deployment.

### Absence scope

- Surfaces inspected: web/search/fetch tools, MCP/skills, model/configuration controls, sessions/memory/context mechanisms, benchmark/ablation material and product changelog.
- Plausible first-party paths checked: environment monitoring, self-modification/capability selection from prospective evidence, benchmark-triggered runtime adaptation and operator adaptation loop.
- Why no material first-party path remains: external information enters current task execution or repository development, but no standard deployed path turns it into an organizational adaptation option that returns to alter current harness capability.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy decision loop is established at the assessed recursion.
- Disturbance / variety regulated: working-directory boundaries, safety rings, offline mode, configuration, confirmation prompts and unsafe escape hatches constrain operational actions but do not resolve identity/ultimate-policy tensions.
- Decisive decision or feedback right: not established for an identity-level policy matter.
- Decision owner: none established for S5.
- Supporting / enforcement mechanisms: safety policy/command/path guards, attended confirmations, default-deny child sandbox, offline switch, configuration precedence, `AGENT_UNSAFE`/mutation opt-ins and system/task prompt constraints.
- Closure path: not applicable; no reviewed path identifies an identity/ultimate-policy issue, escalates it to legitimate ultimate authority and returns an authoritative resolution that governs later operation.
- Why this is / is not agent-owned: model actions occur inside operator/developer-authored constraints, and ordinary confirmations may authorize a concrete action, but neither static rules nor generic action approval constitute S5 under the Profile.
- Evidence: [`README.md`](https://github.com/Mingbird/Mingbird-agent/blob/2e62a735b212aee3c72bce83134042c9ca885237/README.md); [`parallel_safety.py`](https://github.com/Mingbird/Mingbird-agent/blob/2e62a735b212aee3c72bce83134042c9ca885237/parallel_safety.py); [`parallel_config.py`](https://github.com/Mingbird/Mingbird-agent/blob/2e62a735b212aee3c72bce83134042c9ca885237/parallel_config.py); [`ollama_agent.py`](https://github.com/Mingbird/Mingbird-agent/blob/2e62a735b212aee3c72bce83134042c9ca885237/ollama_agent.py).
- Basis: explicit + structural absence review
- Confidence: high
- Caveats: the operator can change configuration and approve/refuse some current actions, but generic operational authority is not promoted to parent S5 without identity/ultimate-policy closure.

### Absence scope

- Surfaces inspected: main/child safety gates, permissions/confirmation, offline mode, configuration/env controls, unsafe escape hatches, system/task prompts and product operation modes.
- Plausible first-party paths checked: identity/purpose change, ultimate-risk-policy dispute, escalation to legitimate parent authority and returned identity-level policy update.
- Why no material first-party path remains: reviewed controls set or enforce operational bounds; no standard path distinguishes an identity/ultimate-policy issue and closes it through ultimate authority back into operation.

## Distributed OSS parent arrangement

Repository maintainer/contributor governance was not used to infer runtime VSM ownership. The assessed system is a local Mingbird deployment/session. Project benchmark/release decisions and repository development are adjacent unless a frozen first-party product path closes them back into the running organization.

## Self-hosted and non-human modes

Mingbird is local-first and can run offline or unattended. Human confirmations are part of selected operational safety paths; child agents deliberately have no approval-escalation channel and remain lower-permission. These choices constrain S1 operation but do not create S3/S4/S5 parent notation without the corresponding organizational function.

## Recursion

The focal recursion is one task/session. The main agent is an S1. Enabled parallel dispatch temporarily creates additional bounded child S1 loops, each with its own partition and session. Their concrete shared-state/interference problem is handled by the deterministic first-party S2 path. The children are not treated as independently viable recursive organizations merely because they are separate model processes.

## Variety and escalation

Mingbird attenuates operational variety through task classification, workspace boundaries, lower child permissions, context/tool slimming, anti-loop recovery, timeouts/timeboxing, no-overwrite integration, rollback and fixed retry/fallback rules. Failed or rejected child work returns to the main model for serial handling; exact tool failures and finish-gate feedback likewise return to S1. These are credited as S1 support or S2 coordination only where the mapped closure is established, rather than being promoted to higher VSM functions by feature name.

## Evidence gaps

- No live model/Ollama execution was run inside this assessment environment; positive claims rely on frozen first-party source, tests and released product wiring.
- S2=`C` depends on the released but default-off parallel mode being enabled/configured; ordinary single-agent operation has no multi-S1 S2 requirement at this recursion.
- The S2 result does not credit parallelism or delegation by themselves; it credits the concrete partition/isolation/acceptance/no-overwrite/fallback relation regulating concurrent child interference.
- S3 remains absent because fixed lifecycle supervision, limits, timeout/retry/abort and final summary do not expose a whole-system discretionary current-control loop.
- S3* remains absent because artifact/audit/finish checks are routine production admission/completion mechanisms rather than an independent complementary audit channel.
- S4 and S5 remain absent despite web/skills/configuration and strong safety controls because the required adaptation and identity/ultimate-policy closures were not established.

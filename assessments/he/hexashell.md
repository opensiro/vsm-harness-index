---
harness_id: hexashell
project_name: HexaShell
repository: https://github.com/HexaFuture/HexaShell
review_ref: e0190ddb757955131578e9f9071f4ee8e7113f7a
reviewed_at: 2026-11-10
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# HexaShell

## Review boundary

- System in focus: HexaShell's runnable single-episode robot coding-agent runtime, including its model/tool conversation, Python-cell sandbox, common robot/motion/perception API and supported simulator/real-robot session adapters.
- Purpose and identity: transform a natural-language robot manipulation task into model-selected Python cells and robot actions using visual/proprioceptive observations until success, a finish decision or episode budget limits.
- Relevant environment: simulator/real robot cameras, arm/base geometry, task card and step budget, external hosted model endpoint, SAM 3 segmentation service, benchmark verdict and physical safety envelope.
- Standard-distribution boundary: `hexashell.benches.run` or RoboDojo `play`/real-robot entry → first-party `Episode.run` → configured OpenAI-compatible/Anthropic model gateway → `python` or `finish` model tool → first-party `Kernel` with `robot.*` RPC → session adapter/host → sensor/tool feedback returned to model. Alternate `script` mode is fixed-cell replay, not a separate autonomous function.
- Credited operating / distribution surfaces: [README](https://github.com/HexaFuture/HexaShell/blob/e0190ddb757955131578e9f9071f4ee8e7113f7a/README.md), [Episode loop](https://github.com/HexaFuture/HexaShell/blob/e0190ddb757955131578e9f9071f4ee8e7113f7a/hexashell/runtime/episode.py), [conversation/picture window](https://github.com/HexaFuture/HexaShell/blob/e0190ddb757955131578e9f9071f4ee8e7113f7a/hexashell/runtime/conversation.py), [model gateway](https://github.com/HexaFuture/HexaShell/blob/e0190ddb757955131578e9f9071f4ee8e7113f7a/hexashell/runtime/llm.py), [session adapter contract](https://github.com/HexaFuture/HexaShell/blob/e0190ddb757955131578e9f9071f4ee8e7113f7a/hexashell/runtime/session.py), [benchmark entry](https://github.com/HexaFuture/HexaShell/blob/e0190ddb757955131578e9f9071f4ee8e7113f7a/hexashell/benches/run.py), [kernel host](https://github.com/HexaFuture/HexaShell/blob/e0190ddb757955131578e9f9071f4ee8e7113f7a/hexashell/kernel/host.py).
- Adjacent first-party surfaces excluded from ownership: benchmark dataset/scorer/leaderboard, evaluation script/report, external simulator and robot physics, hosted model weights, separate SAM 3 model, offline skill-authoring analysis/human review and previous TaskTools optimizer version. These do not automatically become live S2–S5 rights in the assessed episode.
- First-party operating / deployment modes considered: RoboDojo via XPolicyLab, RoboCasa, LIBERO-PRO, RoboTwin and real dual-arm robot adapters; common tool loop with or without pre-authored task skill; external model gateway; scripted fixed-cell playback.
- Recursion level: one robot episode with one model-based task actor controlling robot tools (possibly both arms). Multiple episodes/seeds are independent evaluations rather than a demonstrated autonomous organization of cooperating S1s.
- Reviewed revision: `e0190ddb757955131578e9f9071f4ee8e7113f7a` (Index intake #3035).
- Observation date: 2026-11-10.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The [README](https://github.com/HexaFuture/HexaShell/blob/e0190ddb757955131578e9f9071f4ee8e7113f7a/README.md) documents a single common harness with 14 robot tools across supported simulators and real robot sessions. The [benchmark CLI](https://github.com/HexaFuture/HexaShell/blob/e0190ddb757955131578e9f9071f4ee8e7113f7a/hexashell/benches/run.py) builds a benchmark-specific `Session` and instantiates `Episode`; RoboDojo and real robot modes supply different adapters. `Episode._setup` creates a task card and start pictures, an API gateway, persistent Python-cell kernel and per-episode record. `Episode._loop` asks the configured model for `python`/`finish`, executes cells in order via `_cell` and `Kernel`, dispatches `robot.*` through the session host, appends printed output/errors and pictures to the next model turn, and continues until the benchmark/agent/time/step stop. [Source](https://github.com/HexaFuture/HexaShell/blob/e0190ddb757955131578e9f9071f4ee8e7113f7a/hexashell/runtime/episode.py).

The [session interface](https://github.com/HexaFuture/HexaShell/blob/e0190ddb757955131578e9f9071f4ee8e7113f7a/hexashell/runtime/session.py) delegates physical state/actuation, success and camera details to adapters. The [gateway](https://github.com/HexaFuture/HexaShell/blob/e0190ddb757955131578e9f9071f4ee8e7113f7a/hexashell/runtime/llm.py) retries rate limits and transient network failures by fixed rules; the [conversation](https://github.com/HexaFuture/HexaShell/blob/e0190ddb757955131578e9f9071f4ee8e7113f7a/hexashell/runtime/conversation.py) trims older unpinned pictures for context. Task-specific skill Markdown is loaded as guidance if enabled; the [skills README](https://github.com/HexaFuture/HexaShell/blob/e0190ddb757955131578e9f9071f4ee8e7113f7a/skills/README.md) describes offline skills written/revised from earlier evaluation records, whose source records are not included. A separate automatic ongoing S4 skill-authoring pipeline is not inferred from these static assets.

## Operational model

- Actual outcome: model-selected manipulator motions and observations toward an episode-specific robot task, with a recorded result/trace and optional benchmark verdict.
- S1 units: one model-controlled robot episode/agent loop; arms, object trackers, kernel worker and motion planner are component tools of this S1, not separately deciding operational agents.
- Ownership split: model chooses Python cells, sensory requests, motion sequence and finish judgment; first-party runtime routes tool calls and manages timing; robot/simulator adapter executes and reports; benchmark/real-world success and human task selection are outside the agent's decisive loop.

## S1 — Operations

- State: A
- Function: autonomous visual/task-feedback-driven robot coding and manipulation within one episode.
- Disturbance / variety regulated: unknown object location, motion error, grasp failures, changing camera evidence, step budgets and manipulation uncertainty.
- Decisive decision or feedback right: choose successive Python-cell tool calls, robot actions/measurements and task termination after receiving actual printed/sensor observations.
- Decision owner: externally configured model acting through the *first-party model/tool loop* in `Episode._loop` (runtime owns how the model decisions are applied); the simulator or benchmark does not choose next actions.
- Supporting / enforcement mechanisms: `Gateway`/`AnthropicGateway`, `Conversation`, persistent `Kernel`, `Session` tool dispatch, fourteen robot APIs, motion kinematics and sandbox/step/time limits.
- Closure path: task card plus start pictures → model `python` code → kernel `robot.*` calls → robot host/simulator result and additional camera pictures → `Conversation.tool`/`user` → next model decision; `finish`/budget/episode-over closes the run.
- Boundary reachability: [bench CLI](https://github.com/HexaFuture/HexaShell/blob/e0190ddb757955131578e9f9071f4ee8e7113f7a/hexashell/benches/run.py) selects concrete `Session`; [Episode._setup/_loop/_answer/_cell](https://github.com/HexaFuture/HexaShell/blob/e0190ddb757955131578e9f9071f4ee8e7113f7a/hexashell/runtime/episode.py) instantiate the model and tool feedback; supported gateways and adapters are shipped.
- Why this is / is not agent-owned: without the model, a scripted replay can run predetermined cells but cannot make equivalent open-ended tool/action choices from fresh visual results. This is substantive S1 autonomy; sandbox and bridge enforcement are supporting mechanisms.
- Evidence: [episode model/cell loop](https://github.com/HexaFuture/HexaShell/blob/e0190ddb757955131578e9f9071f4ee8e7113f7a/hexashell/runtime/episode.py), [tool and embodiment architecture](https://github.com/HexaFuture/HexaShell/blob/e0190ddb757955131578e9f9071f4ee8e7113f7a/README.md), [session interface](https://github.com/HexaFuture/HexaShell/blob/e0190ddb757955131578e9f9071f4ee8e7113f7a/hexashell/runtime/session.py).
- Basis: structural with explicit documented operating modes.
- Confidence: high for model/tool/control closure, without executing a robot.
- Caveats: safe real-robot performance, benchmark outcome and external models/simulators require actual credentials, hardware and repeatable tests; README performance numbers were not verified by this assessment.

## S2 — Coordination

- State: —
- Function: no first-party autonomous attenuation of interference between *distinct model-owned S1 units* is established.
- Disturbance / variety regulated: two robot arms and concurrent simulator/benchmark episodes may contend for physical space or compute resources, but the arms are tools of one S1 actor and independent episodes are not supplied as coordinated agent teams.
- Decisive decision or feedback right: the one model chooses combined arm actions; host may serialize motion and enforce limits; no S2-specific controller negotiates conflicting decisions of independent S1 actors.
- Decision owner: single episode model for task-level motions; deterministic motion/robot host for safety/serialization and benchmark runner for job launches.
- Supporting / enforcement mechanisms: motion kinematics, robot `goto`/`wait`/`home` interface, one action at a time, per-episode kernel and simulator servers.
- Closure path: arm control errors and poses feed the same agent's next task action; there is no separate inter-agent conflict report→coordination adjustment returned to distinct operational agents.
- Why this is / is not agent-owned: joint control of two arms is not proof of two autonomous S1 decision owners; serializing actions or independent evaluation runs is infrastructure coordination, not model-owned S2.
- Evidence: [README two-arm tool description](https://github.com/HexaFuture/HexaShell/blob/e0190ddb757955131578e9f9071f4ee8e7113f7a/README.md), [episode loop](https://github.com/HexaFuture/HexaShell/blob/e0190ddb757955131578e9f9071f4ee8e7113f7a/hexashell/runtime/episode.py), [robot session contract](https://github.com/HexaFuture/HexaShell/blob/e0190ddb757955131578e9f9071f4ee8e7113f7a/hexashell/runtime/session.py).
- Basis: structural.
- Confidence: medium-high.
- Caveats: real multi-robot deployment could require coordination, but it is not an established first-party inter-S1 mode at this revision.

### Absence scope

- Surfaces inspected: episode tool schema and loop, bench/session adapters, motion API, robot host, benchmark entry and supported distributed environment descriptions.
- Plausible first-party paths checked: dual-arm motion, independent benchmark sessions, kernel workers, motion serialization, per-episode budget and skill prompts.
- Why no material first-party path remains: the only adaptive actor per episode controls tools inside one S1; neither independent S1 unit interaction nor a returned S2-specific conflict regulation loop is supplied.

## S3 — Inside-and-now control

- State: —
- Function: no whole-current supervisory allocation/commitment loop distinct from the episode S1 is established.
- Disturbance / variety regulated: episode stalls, API failures, time/step exhaustion, cell errors and simulator termination are bounded by fixed runtime rules.
- Decisive decision or feedback right: no first-party metasystem reviews multiple active operational commitments and adaptively reallocates priorities/resources or intervenes across sessions.
- Decision owner: model decides its own in-episode action; developer/operator selects settings and benchmark runs; runtime enforces fixed limits and retries.
- Supporting / enforcement mechanisms: max replies/time, gateway retry strategy, kernel CPU/idle/total limits, step/episode-over flags and result recording.
- Closure path: tool/budget state returns to the same agent or terminates its episode; no whole-system discretionary feedback path governs other S1 units.
- Why this is / is not agent-owned: a model deciding to stop its own episode is S1, not independent S3; fixed timeouts, retries and a benchmark driver do not own whole-current supervision.
- Evidence: [Episode budgets/stops](https://github.com/HexaFuture/HexaShell/blob/e0190ddb757955131578e9f9071f4ee8e7113f7a/hexashell/runtime/episode.py), [gateway failure handling](https://github.com/HexaFuture/HexaShell/blob/e0190ddb757955131578e9f9071f4ee8e7113f7a/hexashell/runtime/llm.py), [bench entry](https://github.com/HexaFuture/HexaShell/blob/e0190ddb757955131578e9f9071f4ee8e7113f7a/hexashell/benches/run.py).
- Basis: structural.
- Confidence: medium-high.
- Caveats: human trial design can schedule many episodes externally but does not establish a first-party operational S3=P parent loop.

### Absence scope

- Surfaces inspected: episode/session runtime, benchmark driver, model gateways, result records and operator settings.
- Plausible first-party paths checked: nudge/finish, limit enforcement, failure retry, simulator verdict and evaluation report aggregation.
- Why no material first-party path remains: no current whole-system view tied to discretionary priorities/commitments and a returned operational adjustment to S1 portfolio.

## S3* — Complementary audit

- State: —
- Function: no independent claim-relative operational audit that returns separate corrective findings into the active agent organization is established.
- Disturbance / variety regulated: grasp/placement failures and final task success are observed via model camera/robot outputs and benchmark scorer, but not separately audited during an ongoing decision loop.
- Decisive decision or feedback right: benchmark/session returns the final verdict; the agent can self-check with `robot.look` and tool results; no distinct first-party auditor judges an agent's operational claim with independent complementary evidence.
- Decision owner: benchmark evaluator and the same S1 model/user; post-episode reports are outside ongoing corrective agent control.
- Supporting / enforcement mechanisms: `Session.conclude`, `Episode._wrap_up`, per-cell recordings, simulator success tests, benchmark report scripts.
- Closure path: episode concludes → external benchmark scores/report records outcome; no finding is returned to an independent S3 actor to redirect the completed origin S1 run. In-episode camera checks are normal S1 observation.
- Why this is / is not agent-owned: self-evaluation and benchmark scoring can be empirically useful, but absent independent auditor ownership and returned control they are not an S3* loop.
- Evidence: [episode `_wrap_up`](https://github.com/HexaFuture/HexaShell/blob/e0190ddb757955131578e9f9071f4ee8e7113f7a/hexashell/runtime/episode.py), [session `conclude` contract](https://github.com/HexaFuture/HexaShell/blob/e0190ddb757955131578e9f9071f4ee8e7113f7a/hexashell/runtime/session.py), [README evaluation limitations](https://github.com/HexaFuture/HexaShell/blob/e0190ddb757955131578e9f9071f4ee8e7113f7a/README.md).
- Basis: structural.
- Confidence: medium-high.
- Caveats: published self-evaluated scores were not reproduced; their correctness is a separate empirical question.

### Absence scope

- Surfaces inspected: episode result/verdict, in-loop observations, logs/records, simulation scoring and benchmark reporting.
- Plausible first-party paths checked: `robot.state` and camera rechecks, sandbox errors, `Session.conclude`, score files and offline evaluation reports.
- Why no material first-party path remains: self-checks feed S1, and independent benchmark verdict occurs after a run without a sourced corrective audit return path.

## S4 — Outside-and-then intelligence

- State: —
- Function: no active first-party prospective adaptation loop for future harness capabilities is established at the shipped episode boundary.
- Disturbance / variety regulated: previous episode failures and unfamiliar tasks led to manually reviewed task skills during development, but installed episode runtime loads static skills and does not independently author/accept future rules.
- Decisive decision or feedback right: no shipped autonomous/human-parent decision cycle in which outside/future evidence is analyzed into options and authoritatively committed as durable runtime capabilities.
- Decision owner: external analysis agent and human authors in reported offline research workflow; operator switches `skills` on/off. Neither is an evidenced active first-party S4 runtime mode.
- Supporting / enforcement mechanisms: `skills/<bench>/<task>.md`, `prompts`, task-card loader, evaluation records and script-mode test playback.
- Closure path: operator selects prewritten skill → task-card context for the current episode; historical offline authoring/revisions are documented but their generator and acceptance/activation loop are not shipped as operational first-party S4.
- Why this is / is not agent-owned: learned task hints are *outputs* of a past research process, not proof of autonomous prospective environmental intelligence in the deployed agent. Normal revision of strategy during an episode is S1.
- Evidence: [skills README provenance](https://github.com/HexaFuture/HexaShell/blob/e0190ddb757955131578e9f9071f4ee8e7113f7a/skills/README.md), [README offline analysis and human review](https://github.com/HexaFuture/HexaShell/blob/e0190ddb757955131578e9f9071f4ee8e7113f7a/README.md), [episode fixed skill/card loading](https://github.com/HexaFuture/HexaShell/blob/e0190ddb757955131578e9f9071f4ee8e7113f7a/hexashell/runtime/episode.py).
- Basis: explicit mode separation + structural.
- Confidence: medium-high for shipped code; historical authoring records are not distributed.
- Caveats: a separate future skill-learning system could implement S4 and would require its own active boundary/authority evidence.

### Absence scope

- Surfaces inspected: README skills workflow, `skills/README`, static skill files, prompt/card loading, episode records and run CLI/configuration.
- Plausible first-party paths checked: task hint injection, offline evaluation-to-skill authoring claims, earlier TaskTools optimizer, scripted cells and adaptive in-task model action.
- Why no material first-party path remains: no shipped first-party option-generation/selection/activation loop using future environmental evidence; prior development/review is explicitly outside active episode operations.

## S5 — Policy and identity

- State: —
- Function: no first-party ultimate-policy/identity arbitration with an authoritative return path for the running robot-agent organization is established.
- Disturbance / variety regulated: safety limits, step budgets, sandbox permissions and robot admissibility are given constraints, not identity-level dilemmas routed for decision.
- Decisive decision or feedback right: developer/operator defines task, tools, model and safety constraints; model can choose local actions/finish but not legitimate ultimate policy for the overall harness.
- Decision owner: external robot operator, developers and simulator/task specifications; first-party runtime enforces predetermined bounds.
- Supporting / enforcement mechanisms: limited tool schema, sandbox without network/process/filesystem escape, motion and step limits, fixed prompt, API credentials outside the sandbox.
- Closure path: tool requests obey fixed kernel/robot constraints and errors return to S1; no identity/ultimate-policy proposal → legitimate parent decision → binding changed policy returned to operation.
- Why this is / is not agent-owned: structural safety and operator-set limits are not S5=A or S5=P without policy-level decision content/authority/return.
- Evidence: [README sandbox/tool contract](https://github.com/HexaFuture/HexaShell/blob/e0190ddb757955131578e9f9071f4ee8e7113f7a/README.md), [Episode tool schema and settings](https://github.com/HexaFuture/HexaShell/blob/e0190ddb757955131578e9f9071f4ee8e7113f7a/hexashell/runtime/episode.py), [sandbox worker](https://github.com/HexaFuture/HexaShell/blob/e0190ddb757955131578e9f9071f4ee8e7113f7a/hexashell/kernel/worker.py).
- Basis: structural.
- Confidence: medium-high.
- Caveats: additional legal/physical robot safety governance exists beyond this open-source software boundary and was not reviewed or imported as runtime S5.

### Absence scope

- Surfaces inspected: tool/prompt contracts, sandbox, robot safety/action bounds, run settings, benchmark judge and real-robot adapter descriptions.
- Plausible first-party paths checked: model finish choice, step budget, motion validation, user task instruction, offline task skills and simulator success specification.
- Why no material first-party path remains: these choose or constrain operational actions, not the organization identity/ultimate policy under an authoritative closed escalation/return channel.

## Recursion

HexaShell uses one model-backed agent per robot episode. Two arms, a segmentation server, motion/IK, persistent Python kernel and benchmark adapter are functional parts of the episode, not separately self-governing viable systems. Parallel independently launched test episodes are an evaluation cohort without an evidenced multi-agent metasystem. A configured external VLM supplies cognitive weights while the first-party episode code closes the S1 model/tool/feedback loop.

## Variety and escalation

Fresh camera images, state and tool failures return to S1 for further cell planning. Fixed step/turn/time budgets, robot motion validation and gateway retries attenuate operational risk; reaching a limit or simulator completion closes the episode, with verdict and trace recorded afterward. No separate S3/S3*/S5 escalation pathway is claimed from safety stops or benchmark scoring.

## Evidence gaps

- Static source-first assessment at the pinned revision: no GPU simulator, robot hardware, SAM 3 service or model credential was used, and no success-rate or physical-safety claim is independently validated.
- Offline analysis-agent skill authoring and human review are described but their development records/automation are not included; this bounds the negative S4 conclusion to the shipped first-party episode mode.
- Other robot adapters or unreleased runtime extensions could change a concrete deployment; none is presumed present without source evidence.

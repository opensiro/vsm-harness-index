---
harness_id: toolgen
project_name: ToolGen
repository: https://github.com/Reason-Wang/ToolGen
review_ref: 6839374a255810efe69deea4056eec5c55e25802
reviewed_at: 2026-09-27
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-27
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# ToolGen

## Review boundary

- System in focus: one first-party ToolGen `OpenAgent` task run at pinned revision `6839374a255810efe69deea4056eec5c55e25802`, including the shipped `ToolGen` agent, `SingleChainAgent` execution loop and first-party tool-wrapper interface used by the documented local runtime.
- Purpose and identity: accept a user task, repeatedly choose a relevant tool/action and its arguments, execute that action through the configured tool environment, observe the result, decide the next action from the changed conversation/state and finally return an answer or terminate/restart the attempt.
- Relevant environment: user query; downloaded ToolGen model/checkpoint and tool metadata; external ToolBench/StableToolBench service; API/tool providers and their changing responses/errors; local GPU/runtime dependencies; operator-supplied keys and model/configuration choices.
- Standard-distribution boundary: the first-party `OpenAgent/` runtime and the documented `ToolGen(...).start(...)` path. ToolBench, StableToolBench, downstream external tool services, Hugging Face model hosting, model-training pipelines and evaluation/pass-rate/win-rate infrastructure remain dependencies or adjacent systems rather than imported first-party organizational owners.
- Credited operating / distribution surfaces: `README.md`; `OpenAgent/agents/base.py`; `OpenAgent/agents/toolgen/toolgen.py`; `OpenAgent/agents/toolgen/inference.py`; `OpenAgent/tools/base.py`; `OpenAgent/tools/src/rapidapi/rapidapi.py`; and package exports required by the documented local example.
- Adjacent first-party surfaces excluded from ownership: `training/`; `evaluation/`; benchmark/inference result conversion, solvable-pass-rate and preference/win-rate scripts; training datasets/trajectories; research-paper assets; repository/project governance; external ToolBench/StableToolBench implementations.
- First-party operating / deployment modes considered: the documented local `ToolGen` mode instantiated with a first-party `RapidAPIWrapper` and started via `toolgen.start(single_chain_max_step=..., start_messages=...)`. Evaluation-only runners are inspected for possible organizational evidence but are not credited as the supported standalone runtime.
- Recursion level: one user task / one `SingleChainAgent` attempt is the system-in-focus. Individual tools are environmental capabilities invoked by the operational agent, not separate first-party S1 organizations merely because they expose distinct APIs.
- Reviewed revision: `6839374a255810efe69deea4056eec5c55e25802`.
- Observation date: 2026-09-27.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

ToolGen combines a trained model representation of a very large tool set with a first-party runtime that closes a conventional model → tool → observation → next-model-decision loop. The README's runnable example instantiates `ToolGen` with `RapidAPIWrapper`, supplies user messages, calls `restart()`, and then invokes `start()` with a maximum chain length.

`SingleChainAgent.start()` initializes a task tree and enters `do_chain()`. Each cycle calls the model-facing `parse()` path, which can generate planning text, choose an action/tool and generate its arguments. If a tool call is present, `take_action()` calls the current tool-state object's `call(action_name, action_input)`. The resulting observation/status is appended back to the conversation as a tool message. The loop then queries the model again from that changed state until a terminal/pruned condition is reached. This is a substantive autonomous S1 closure rather than a retrieval-only library.

ToolGen's specialization is how it selects tools. Its model generates action tokens under constrained decoding; those tokens map to ToolBench-style tool names, and the runtime retrieves the corresponding documentation before generating arguments. The model therefore owns both which available action to take and what arguments to supply. `RapidAPIWrapper` deterministically transports that selected call to the configured service and returns status/observation. External ToolBench/StableToolBench infrastructure supplies tool execution, but it does not choose the task-specific action.

No additional VSM function is established merely by this tool scale. There is one accountable operational agent, not a population of distinct first-party S1 units with an interference problem. The single-chain runtime and maximum-depth/status handling do not form a superior whole-system S3 manager. Tool-return validation/error codes are ordinary in-band S1 feedback rather than complementary audit. Training/tool-memorization/retrieval-training/agent-tuning are development-time processes outside the supported runtime, and runtime tool retrieval/action-token generation chooses means for the current task rather than prospectively modifying installed capability; no S4 closure is therefore published. User objective, model checkpoint, tool universe, keys, indexing mode and prompts remain externally configured rather than owned by a runtime S5 authority.

Primary evidence:

- [`README.md`](https://github.com/Reason-Wang/ToolGen/blob/6839374a255810efe69deea4056eec5c55e25802/README.md) — documented local `OpenAgent.ToolGen` runtime, `RapidAPIWrapper`, `restart()` / `start()` invocation and explicit separation of training/evaluation workflows.
- [`OpenAgent/agents/base.py`](https://github.com/Reason-Wang/ToolGen/blob/6839374a255810efe69deea4056eec5c55e25802/OpenAgent/agents/base.py) — `SingleChainAgent` task loop, model response, first-party tool execution, returned observation injection and repeated decision cycle.
- [`OpenAgent/agents/toolgen/toolgen.py`](https://github.com/Reason-Wang/ToolGen/blob/6839374a255810efe69deea4056eec5c55e25802/OpenAgent/agents/toolgen/toolgen.py) — ToolGen model loading, action-token/tool mapping, constrained action generation, documentation-conditioned argument generation and conversion to executable tool calls.
- [`OpenAgent/tools/base.py`](https://github.com/Reason-Wang/ToolGen/blob/6839374a255810efe69deea4056eec5c55e25802/OpenAgent/tools/base.py) — deterministic action dispatch and returned status/observation handling.
- [`OpenAgent/tools/src/rapidapi/rapidapi.py`](https://github.com/Reason-Wang/ToolGen/blob/6839374a255810efe69deea4056eec5c55e25802/OpenAgent/tools/src/rapidapi/rapidapi.py) — first-party wrapper loading the tool package, exposing tool metadata, dispatching selected actions to the configured external service and recognizing terminal `Finish` state.

## Operational model

The operator initializes ToolGen with a model, indexing mode and tool wrapper, then supplies a user task. The model forms the next step, generates a constrained action token representing a tool/API, receives that action's documentation, generates arguments, and hands the action to the first-party runtime. The wrapper calls the configured external tool service and returns an observation/status. That observation becomes model context for the next iteration. Tool errors such as invalid API names, timeouts, authorization failures or rate limits likewise become operational feedback. The agent continues until it emits `Finish`, gives up/restarts the attempt, or reaches the configured chain limit.

The deterministic runtime owns transport, constrained action vocabulary, tool metadata, status codes and stopping bounds. The contextual choice of what to do next, which tool to use, which arguments to provide and when sufficient evidence exists to finish is model-driven.

## S1 — Operations

- State: A
- Function: perform the user's substantive tool-using task through iterative model-selected actions, external tool effects/queries and result-conditioned next-action decisions.
- Disturbance / variety regulated: open-ended user requests; very large available tool space; uncertainty about which API/tool fits the current subproblem; action-argument requirements; returned data; invalid/hallucinated action names; external API failures/timeouts/rate limits; incomplete information requiring additional calls.
- Decisive decision or feedback right: choose the next task-relevant action/tool and its arguments from the live conversation/observations, interpret returned tool evidence/errors, and decide whether to take another action, answer, or abandon/restart the attempt.
- Decision owner: the first-party model-driven ToolGen `OpenAgent` path.
- Supporting / enforcement mechanisms: constrained action-token decoding, tool-token/name conversion, tool documentation lookup, `SingleChainAgent` state/tree, first-party action dispatch, RapidAPI/StableToolBench transport, observation truncation, status codes and maximum-chain-depth pruning.
- Closure path: user task/current conversation -> ToolGen model generates plan/action token/arguments -> `SingleChainAgent.take_action()` executes through the tool-state wrapper -> external tool result/status returns -> observation is appended to model context -> later model call changes the next action or terminates -> task progresses toward a final answer.
- Boundary reachability: the README's standard local example directly constructs `ToolGen` plus `RapidAPIWrapper`, calls `restart()` and `start()`, which reaches the credited `SingleChainAgent.do_chain()` / `parse()` / `take_action()` loop without requiring the repository's training or evaluation programs.
- Why this is / is not agent-owned: deterministic code constrains and executes the available interfaces, while the model selects the task-specific tool/action, generates its arguments and decides what follows from each returned observation. Removing the model decision path while leaving the wrapper/tool metadata in place would not produce materially the same operational choices.
- Evidence: [`README.md`](https://github.com/Reason-Wang/ToolGen/blob/6839374a255810efe69deea4056eec5c55e25802/README.md); [`OpenAgent/agents/base.py`](https://github.com/Reason-Wang/ToolGen/blob/6839374a255810efe69deea4056eec5c55e25802/OpenAgent/agents/base.py); [`OpenAgent/agents/toolgen/toolgen.py`](https://github.com/Reason-Wang/ToolGen/blob/6839374a255810efe69deea4056eec5c55e25802/OpenAgent/agents/toolgen/toolgen.py); [`OpenAgent/tools/src/rapidapi/rapidapi.py`](https://github.com/Reason-Wang/ToolGen/blob/6839374a255810efe69deea4056eec5c55e25802/OpenAgent/tools/src/rapidapi/rapidapi.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: actual tool effects depend on external ToolBench/StableToolBench/API services. Those dependencies supply environmental capability/execution but do not select the contextual operational action credited to ToolGen.

## S2 — Coordination

- State: —
- Function: no qualifying inter-S1 coordination function is established at the one-agent task boundary.
- Disturbance / variety regulated: none qualifying; multiple callable tools/APIs create action-choice variety but are not independently accountable first-party operational S1 units whose interaction creates a conflict/oscillation/interference problem.
- Decisive decision or feedback right: none established for S2.
- Decision owner: none established.
- Supporting / enforcement mechanisms: action-token constraints, tool lookup/routing, sequential tool calls and shared conversation state are present but do not establish S2.
- Closure path: no material inter-S1 disturbance -> coordination decision -> changed affected-S1 behaviour path closes.
- Why this is / is not agent-owned: tool selection/routing and sequencing belong to one S1's task execution; they are not an organizational coordination relation among distinct operations.
- Evidence: [`OpenAgent/agents/base.py`](https://github.com/Reason-Wang/ToolGen/blob/6839374a255810efe69deea4056eec5c55e25802/OpenAgent/agents/base.py); [`OpenAgent/agents/toolgen/toolgen.py`](https://github.com/Reason-Wang/ToolGen/blob/6839374a255810efe69deea4056eec5c55e25802/OpenAgent/agents/toolgen/toolgen.py).
- Basis: structural absence.
- Confidence: high.
- Caveats: large tool cardinality does not itself imply a population of S1 units.

### Absence scope

- Surfaces inspected: `SingleChainAgent`, ToolGen action generation, tool wrappers/routing, tool metadata/retrieval, runtime status handling and documented invocation/evaluation modes.
- Plausible first-party paths checked: multiple tool calls; parallel calls supported by the base loop; tool retrieval; API routing; tree/state machinery; evaluation multi-threading.
- Why no material first-party path remains: the supported ToolGen runtime presents tools as capabilities of one operational agent. No distinct first-party operational units plus an evidenced interference/conflict/oscillation and attenuation feedback relation were found.

## S3 — Inside-and-now control

- State: —
- Function: no distinct superior whole-system current-control function is established above the single ToolGen task operation.
- Disturbance / variety regulated: chain depth, status/error conditions and current tool results affect the current run, but these are either deterministic enforcement or ordinary S1 feedback.
- Decisive decision or feedback right: no separate actor forms a whole-system current view and exercises discretionary authority over shared resources, commitments, priorities, constraints or multiple operational units.
- Decision owner: none established for qualifying S3.
- Supporting / enforcement mechanisms: maximum step limit, tree/prune state, success/status codes, action constraints and process/runtime bookkeeping.
- Closure path: deterministic bounds enforce configured limits while the same S1 model chooses task actions; no superior current-management feedback loop closes.
- Why this is / is not agent-owned: `SingleChainAgent` is an orchestrator in the software sense, but its whole-run controls are pre-authored loop/stopping mechanics. The contextual decisions it carries are the S1 action choices, not a separately evidenced S3 management function.
- Evidence: [`OpenAgent/agents/base.py`](https://github.com/Reason-Wang/ToolGen/blob/6839374a255810efe69deea4056eec5c55e25802/OpenAgent/agents/base.py); [`OpenAgent/tools/base.py`](https://github.com/Reason-Wang/ToolGen/blob/6839374a255810efe69deea4056eec5c55e25802/OpenAgent/tools/base.py).
- Basis: structural absence.
- Confidence: high.
- Caveats: deterministic enforcement must not be promoted to S3 ownership merely because it controls execution.

### Absence scope

- Surfaces inspected: task loop, task tree/state, max-step pruning, success/restart status, tool dispatch, process counters and evaluation runtime variants.
- Plausible first-party paths checked: `SingleChainAgent` as manager; tree/prune machinery; parallel tool-call handling; process IDs; restart/success counters; external service limits.
- Why no material first-party path remains: the reviewed standard mode has one S1 task operation and no separate whole-system current view plus discretionary management authority over an operational whole.

## S3* — Complementary audit

- State: —
- Function: no qualifying complementary and sufficiently independent audit path is established in the standard `OpenAgent` runtime.
- Disturbance / variety regulated: invalid action names, API/tool errors and external failures are observed and can change later S1 behavior, but they arrive through the ordinary action/observation channel.
- Decisive decision or feedback right: no separately situated auditor independently checks operational reality and returns corrective findings into the task loop.
- Decision owner: none established for qualifying S3*.
- Supporting / enforcement mechanisms: wrapper status codes, tool observations, invalid-action handling and repository evaluation/pass-rate/preference programs.
- Closure path: ordinary tool execution -> ordinary tool observation/status -> same S1 model chooses next action; adjacent evaluation programs produce benchmark measurements rather than corrective runtime audit closure.
- Why this is / is not agent-owned: error observation and benchmark evaluation are valuable verification surfaces, but S3* requires complementary independent access and corrective feedback, not normal S1 observations or post-hoc scoring.
- Evidence: [`OpenAgent/agents/base.py`](https://github.com/Reason-Wang/ToolGen/blob/6839374a255810efe69deea4056eec5c55e25802/OpenAgent/agents/base.py); [`OpenAgent/tools/src/rapidapi/rapidapi.py`](https://github.com/Reason-Wang/ToolGen/blob/6839374a255810efe69deea4056eec5c55e25802/OpenAgent/tools/src/rapidapi/rapidapi.py); [`README.md`](https://github.com/Reason-Wang/ToolGen/blob/6839374a255810efe69deea4056eec5c55e25802/README.md).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: evaluation infrastructure is adjacent to the runtime boundary and is not wired as an independent corrective auditor for live ToolGen operation.

### Absence scope

- Surfaces inspected: action/status/observation return loop, invalid-action paths, `Finish`, evaluation directory/workflows and README pass-rate/win-rate instructions.
- Plausible first-party paths checked: API status/error checks as audit; success checker; tree terminal/prune checks; retrieval evaluation; solvable pass-rate; preference/win-rate evaluation.
- Why no material first-party path remains: runtime checks use the same ordinary tool channel and repository evaluation is post-hoc/adjacent; no complementary evidence channel plus independent audit judgment and return-to-operation loop is established.

## S4 — Outside-and-then intelligence

- State: —
- Function: no qualifying external-and-prospective adaptation loop that changes installed/current organizational capability is established in the supported runtime.
- Disturbance / variety regulated: the large external tool universe and returned information create current-task choice variety, while training processes can change future model capability offline; neither closes runtime S4 at this boundary.
- Decisive decision or feedback right: no runtime actor is shown sensing longer-horizon external conditions, generating a capability/posture adaptation option and adopting it back into current ToolGen capability.
- Decision owner: none established for qualifying S4.
- Supporting / enforcement mechanisms: action-token/tool retrieval, tool documentation, tool virtualization, memorization/retrieval/agent training, downloadable tool metadata and evaluation results.
- Closure path: runtime tool retrieval selects a means for the current task; offline training changes checkpoints before deployment. No supported live external sensing -> prospective adaptation option -> changed installed/current capability loop closes.
- Why this is / is not agent-owned: selecting among already available tools in response to the current query is S1 action selection. Training/tool memorization/retrieval training are developer/research processes outside the assessed operating mode and do not become S4 merely because they improve future performance.
- Evidence: [`README.md`](https://github.com/Reason-Wang/ToolGen/blob/6839374a255810efe69deea4056eec5c55e25802/README.md); [`OpenAgent/agents/toolgen/toolgen.py`](https://github.com/Reason-Wang/ToolGen/blob/6839374a255810efe69deea4056eec5c55e25802/OpenAgent/agents/toolgen/toolgen.py); repository `training/` and `evaluation/` boundaries documented in the README.
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: a future runtime that autonomously changes/persists its tool repertoire or model strategy from environmental evidence would require reassessment.

### Absence scope

- Surfaces inspected: runtime action retrieval/generation, tool metadata loading, model/checkpoint loading, training documentation, retrieval/agent-tuning surfaces and evaluation scripts.
- Plausible first-party paths checked: dynamic relevant-action selection; tool documentation retrieval; loading new tool metadata; tool virtualization; tool memorization/retrieval training; agent tuning; evaluation feedback.
- Why no material first-party path remains: runtime selection operates over a configured capability set for the current task, while capability-changing processes occur offline/development-time and are not autonomously closed back into the running organization.

## S5 — Policy and identity

- State: —
- Function: no first-party runtime identity/ultimate-policy authority is established.
- Disturbance / variety regulated: user objective, system prompt, checkpoint, indexing method, configured tool universe, credentials, external service endpoint and chain limit constrain behavior but are supplied by operator/developer/configuration.
- Decisive decision or feedback right: define or revise the ultimate purpose/identity/top-level policy governing the ToolGen organization independently of the supplied task/configuration.
- Decision owner: external user/developer/configuration; no qualifying runtime S5 owner is established.
- Supporting / enforcement mechanisms: static system prompt, model/checkpoint selection, tool-token mapping, API credentials, service URL and maximum-step configuration.
- Closure path: no runtime identity/policy issue -> authoritative S5 decision -> changed operational policy loop closes.
- Why this is / is not agent-owned: ToolGen decides how to pursue the supplied user task with configured tools, not what ultimate organizational identity/purpose it should adopt.
- Evidence: [`README.md`](https://github.com/Reason-Wang/ToolGen/blob/6839374a255810efe69deea4056eec5c55e25802/README.md); [`OpenAgent/agents/toolgen/toolgen.py`](https://github.com/Reason-Wang/ToolGen/blob/6839374a255810efe69deea4056eec5c55e25802/OpenAgent/agents/toolgen/toolgen.py); [`OpenAgent/agents/base.py`](https://github.com/Reason-Wang/ToolGen/blob/6839374a255810efe69deea4056eec5c55e25802/OpenAgent/agents/base.py).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: the static AutoGPT-style system prompt and `Finish` contract are behavioral constraints, not a runtime S5 authority.

### Absence scope

- Surfaces inspected: user/system message handling, ToolGen constructor/configuration, model/checkpoint loading, tool mapping, API wrapper configuration, task stopping/restart paths and training/evaluation boundaries.
- Plausible first-party paths checked: system prompt as policy; `Finish` as identity/purpose; model/indexing selection; configured tools/credentials; restart decision; training objectives.
- Why no material first-party path remains: all ultimate goals and top-level runtime constraints are externally authored/configured, while model discretion remains operational task execution beneath them.

## Recursion

One ToolGen user-task attempt is the assessed recursion. Tool APIs are capabilities/environmental actors called by that S1 rather than separately accountable first-party S1 organizations. ToolBench/StableToolBench, training infrastructure and benchmark/evaluation pipelines are adjacent systems and are not collapsed into the runtime organization merely because the repository integrates with or evaluates against them.

## Variety and escalation

ToolGen attenuates a very large action-space variety by encoding tools as model tokens, constraining action generation, providing selected tool documentation before argument generation and feeding concrete tool observations/errors back into the next model decision. Invalid/hallucinated actions and external-service failures are surfaced through status codes. The agent can eventually choose `Finish` with an answer or give-up/restart indication, while deterministic maximum-depth logic bounds the attempt. No separate metasystem escalation function beyond the one operational loop is established.

## Evidence gaps

- Structural review only; no model checkpoint, ToolBench key or StableToolBench service was executed during this assessment.
- External ToolBench/StableToolBench/API implementations are deliberately not used to infer additional first-party functions.
- The repository's offline training and evaluation surfaces may change/check future model performance, but they are adjacent development/evaluation systems rather than runtime S4/S3* closure in the declared standard distribution.
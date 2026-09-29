---
harness_id: ml-intern
project_name: ML Intern
repository: https://github.com/huggingface/ml-intern
review_ref: 3555becf822ab9b71be9678b2332f542a9fde0b5
reviewed_at: 2026-09-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-30
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# ML Intern

## Review boundary

- System in focus: the preserved first-party ML Intern CLI/agent runtime at frozen retirement revision `3555becf822ab9b71be9678b2332f542a9fde0b5`, including the agent loop, session/context manager, ToolRouter, built-in research/planning/Hugging Face/GitHub/local-or-sandbox tools, approval/budget guards, doom-loop correction, model routing and session persistence surfaces.
- Purpose and identity: autonomously research, implement and ship ML-related work through the Hugging Face ecosystem while retaining a conversational/headless execution loop and first-party tool feedback.
- Relevant environment: user ML-engineering goals, the local working directory or opted-in HF Space sandbox, Hugging Face documentation/papers/datasets/repos/jobs, GitHub repositories, provider responses, tool results/failures, approval decisions and spend/runtime constraints.
- Standard-distribution boundary: the preserved `ml-intern` CLI/runtime and its first-party Python modules are inside. Hugging Face hosted services, inference providers, GitHub, external MCP servers and HF Space/job execution substrates are dependencies. The retirement notice and archived maintenance state are provenance/current-relevance facts, not VSM functions.
- First-party operating modes considered: interactive CLI, headless auto-approve mode, local tool runtime, opted-in HF sandbox tools, local or hosted model providers, the built-in independent-context `research` subagent, planning, context compaction, approvals and session trace persistence.
- Recursion level: the focal ML Intern session is the assessed organization. The `research` tool can instantiate a separate read-only research actor with its own context, but its task is subordinate evidence gathering for the focal operation and does not by itself establish a same-recursion coordination/metasystem organization.
- Reviewed revision: `3555becf822ab9b71be9678b2332f542a9fde0b5`.
- Observation date: 2026-09-30.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

The preserved distribution contains a first-party agent loop rather than delegating the operational loop to another host agent. `agent/core/agent_loop.py` owns the session-turn cycle: model calls are made from current session/context state, model tool calls are parsed, approval/budget policy is applied, tools execute through the first-party `ToolRouter`, results are returned to context, and subsequent model turns react to those results until completion or the iteration bound.

`ToolRouter` registers first-party research, documentation, paper, dataset, planning, notification, HF jobs/repository, local/sandbox and MCP-backed tools. The built-in `research` tool is itself an independent-context model/tool loop with a read-only research tool subset; its explicit contract is to return concise research findings to the main agent so the focal agent can implement the solution.

The runtime also contains deterministic and human-governed safety/recovery mechanisms. The doom-loop detector hashes recent tool-call/result signatures, detects repeated calls or cycles and injects a corrective user-role system message into the same focal context. An unfinished-plan guard prevents premature completion; approval and YOLO-budget policy can pause or block costly/destructive operations; context compaction and session persistence preserve operating continuity. These mechanisms regulate the focal S1 loop but do not by themselves establish higher VSM functions.

The exact frozen commit explicitly retires the hosted app and CLI and preserves the repository as unsupported historical reference. The implementation remains present and assessable at that revision; retirement is therefore recorded as provenance rather than converted into a functional absence state.

Primary evidence:

- [`README.md`](https://github.com/huggingface/ml-intern/blob/3555becf822ab9b71be9678b2332f542a9fde0b5/README.md)
- [`agent/core/agent_loop.py`](https://github.com/huggingface/ml-intern/blob/3555becf822ab9b71be9678b2332f542a9fde0b5/agent/core/agent_loop.py)
- [`agent/core/tools.py`](https://github.com/huggingface/ml-intern/blob/3555becf822ab9b71be9678b2332f542a9fde0b5/agent/core/tools.py)
- [`agent/tools/research_tool.py`](https://github.com/huggingface/ml-intern/blob/3555becf822ab9b71be9678b2332f542a9fde0b5/agent/tools/research_tool.py)
- [`agent/core/doom_loop.py`](https://github.com/huggingface/ml-intern/blob/3555becf822ab9b71be9678b2332f542a9fde0b5/agent/core/doom_loop.py)

## Operational model

A user request enters the focal session. The first-party loop forms a provider request from current context and tool specifications, receives a model response, interprets tool calls, applies approval/budget constraints, executes the requested first-party or MCP tool, appends the observed result to context and repeats. Research can be delegated into an independent context and returned as a summary to the focal session. Repetition detection, incomplete-plan continuation and tool errors can alter the next focal model turn. Completion remains the result of the focal model-backed operational actor working inside this first-party feedback organization.

## S1 — Operations

- State: A
- Function: autonomously transform ML-engineering intent into research, code/artifact manipulation and Hugging Face/GitHub-oriented operational work through a first-party model/tool feedback loop.
- Disturbance / variety regulated: heterogeneous ML tasks, changing repository/data/documentation state, provider outputs, research findings, tool failures, execution evidence, approval constraints and intermediate implementation results.
- Decisive decision or feedback right: choose the next research/tool/code action from current evidence, revise the approach after tool results or corrective prompts, and decide when the requested turn is complete.
- Decision owner: the model-backed focal ML Intern agent operating through the first-party session and ToolRouter organization.
- Supporting / enforcement mechanisms: session/context manager; LiteLLM provider call; ToolRouter; planning tool; research subagent; local/sandbox execution; approval policy; spend/budget guards; doom-loop detector; unfinished-plan continuation; context compaction; session persistence and trace export.
- Closure path: user goal → focal model call from current context → selected tool/research action → first-party execution/approval handling → observed result returned into context → later model choice changes from that evidence → final response or artifact effect.
- Boundary reachability: this is the shipped interactive/headless CLI path. No downstream workflow composition is required to obtain the model→tool→feedback cycle.
- Why this is agent-owned: if the model-backed decision actor is removed while ToolRouter, approval checks, persistence and deterministic guards remain, the system loses contextual selection and sequencing of ML research/implementation actions. The decisive operational discretion is therefore agent-owned.
- Evidence: [`agent/core/agent_loop.py`](https://github.com/huggingface/ml-intern/blob/3555becf822ab9b71be9678b2332f542a9fde0b5/agent/core/agent_loop.py); [`agent/core/tools.py`](https://github.com/huggingface/ml-intern/blob/3555becf822ab9b71be9678b2332f542a9fde0b5/agent/core/tools.py); [`README.md`](https://github.com/huggingface/ml-intern/blob/3555becf822ab9b71be9678b2332f542a9fde0b5/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: external model inference and hosted execution/data services remain dependencies. The frozen project is retired/unsupported, but that does not erase the preserved autonomous loop at the reviewed revision.

## S2 — Coordination

- State: —
- Function: no complete first-party coordination function among distinct same-recursion S1 units was established.
- Disturbance / variety regulated: not established at S2 scope.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: the focal session can call an independent-context `research` subagent and can invoke multiple external tools/services, but no mechanism was found that detects/attenuates inter-S1 interference and returns the result into the affected units' subsequent behavior.
- Closure path: not established.
- Why this is / is not agent-owned: ownership is not classified because the S2 function itself is absent. Delegation of current-task research is decomposition, not evidence of inter-operational coordination.
- Evidence: [`agent/core/tools.py`](https://github.com/huggingface/ml-intern/blob/3555becf822ab9b71be9678b2332f542a9fde0b5/agent/core/tools.py); [`agent/tools/research_tool.py`](https://github.com/huggingface/ml-intern/blob/3555becf822ab9b71be9678b2332f542a9fde0b5/agent/tools/research_tool.py); [`README.md`](https://github.com/huggingface/ml-intern/blob/3555becf822ab9b71be9678b2332f542a9fde0b5/README.md).
- Basis: structural absence conclusion.
- Confidence: high.

### Absence scope

- Surfaces inspected: focal agent loop, ToolRouter/built-in tools, independent research subagent, planning state, local/sandbox runtime selection, session state and documentation architecture.
- Plausible first-party paths checked: research delegation, parallel/independent research context, tool plurality, plan items, hosted/local execution alternatives and messaging/notification surfaces.
- Why no material first-party path remains: none of these surfaces establishes a disturbance between distinct viable operational units plus an attenuation decision and returned behavioral feedback. The research subagent supplies evidence to the focal S1 rather than coordinating peer S1 activity.

## S3 — Inside-and-now control

- State: —
- Function: no boundary-reachable whole-system current-control function over the focal organization was established.
- Disturbance / variety regulated: repetition, unfinished plans, spend limits, approvals, tool/runtime failures and context pressure are regulated locally inside the focal operating loop, not through a separate whole-system current-control layer.
- Decisive decision or feedback right: not established at S3 scope.
- Decision owner: not established.
- Supporting / enforcement mechanisms: doom-loop correction; incomplete-plan continuation guard; approval policy; YOLO/session budget checks; usage thresholds; model/provider retry/switching; context compaction; session interruption/resume.
- Closure path: local guards return correction/block/continuation signals directly into the focal S1 cycle; no inspected path constructs an organization-wide current view and decides present resources, commitments, priorities or cross-unit intervention on behalf of the whole.
- Why this is / is not agent-owned: the strong recovery/safety mechanisms are either deterministic or part of the same S1 actor's operating feedback. They do not establish an S3 function merely because they regulate current execution.
- Evidence: [`agent/core/agent_loop.py`](https://github.com/huggingface/ml-intern/blob/3555becf822ab9b71be9678b2332f542a9fde0b5/agent/core/agent_loop.py); [`agent/core/doom_loop.py`](https://github.com/huggingface/ml-intern/blob/3555becf822ab9b71be9678b2332f542a9fde0b5/agent/core/doom_loop.py).
- Basis: structural absence conclusion.
- Confidence: high.

### Absence scope

- Surfaces inspected: repetition guard, plan continuation, approvals, spend/usage policy, provider retry/switching, submission/session lifecycle, research delegation and trace/event surfaces.
- Plausible first-party paths checked: runtime supervision, budget decisions, approval routing, automatic correction and model switching.
- Why no material first-party path remains: the inspected mechanisms constrain or repair individual focal operation. No whole-system current-control owner with the required global scope and decision closure was found.

## S3* — Complementary audit

- State: —
- Function: no materially independent complementary-audit function with findings entering subsequent control was established.
- Disturbance / variety regulated: not established at S3* scope.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: private session traces, tool evidence, approvals, the read-only research subagent and deterministic validation/error outputs.
- Closure path: not established.
- Why this is / is not agent-owned: the research subagent has an independent context, but its declared role is information gathering for the focal operation rather than challenging the focal agent's claims through a complementary audit path. Trace capture and human approvals likewise do not create independent challenge-and-return closure.
- Evidence: [`agent/tools/research_tool.py`](https://github.com/huggingface/ml-intern/blob/3555becf822ab9b71be9678b2332f542a9fde0b5/agent/tools/research_tool.py); [`README.md`](https://github.com/huggingface/ml-intern/blob/3555becf822ab9b71be9678b2332f542a9fde0b5/README.md).
- Basis: structural absence conclusion.
- Confidence: high.

### Absence scope

- Surfaces inspected: research subagent prompt/tools/output, approvals, tool-result validation/errors, trace upload/telemetry, planning and focal-loop recovery.
- Plausible first-party paths checked: independent research context, evidence collection, session trace review, user approval and tool-level validation.
- Why no material first-party path remains: no inspected actor independently audits a focal operational claim and returns an authoritative/challenging finding into later control. Independent context alone is insufficient when the function is ordinary research support.

## S4 — Outside-and-then intelligence

- State: —
- Function: no externally oriented prospective adaptation loop that changes future organizational capability was established.
- Disturbance / variety regulated: the agent performs extensive literature, web, documentation, repository and dataset research, but those observations are gathered to solve the present user task.
- Decisive decision or feedback right: not established for future capability adaptation.
- Decision owner: not established.
- Supporting / enforcement mechanisms: research subagent; paper/citation/web/docs tools; session history; context compaction; model selection/configuration; retained traces.
- Closure path: current external evidence can change current S1 implementation choices, but no path was found from prospective/environmental sensing through adaptation-option development into a durable change of present ML Intern organizational capability.
- Why this is / is not agent-owned: research breadth does not make a function S4 when the return path serves the current task rather than future organizational adaptation.
- Evidence: [`agent/tools/research_tool.py`](https://github.com/huggingface/ml-intern/blob/3555becf822ab9b71be9678b2332f542a9fde0b5/agent/tools/research_tool.py); [`agent/core/tools.py`](https://github.com/huggingface/ml-intern/blob/3555becf822ab9b71be9678b2332f542a9fde0b5/agent/core/tools.py); [`README.md`](https://github.com/huggingface/ml-intern/blob/3555becf822ab9b71be9678b2332f542a9fde0b5/README.md).
- Basis: structural absence conclusion.
- Confidence: high.

### Absence scope

- Surfaces inspected: literature/citation research, web/docs/GitHub/dataset tools, research-subagent recommendations, session persistence/compaction, configuration/model selection and trace retention.
- Plausible first-party paths checked: external sensing, recipe ranking, reusable information, persistence and model/runtime configuration.
- Why no material first-party path remains: research findings return to implementation of the current goal; persistence retains context/evidence; configuration changes are operator choices. No future-oriented adaptation loop that updates system capability was reconstructed.

## S5 — Policy and identity

- State: —
- Function: no identity/ultimate-policy decision loop was established at the assessed recursion.
- Disturbance / variety regulated: tool approvals, spending limits, headless auto-approval, provider/tool/runtime configuration and user task intent constrain operation but do not constitute identity-level policy closure.
- Decisive decision or feedback right: not established for identity/ultimate policy.
- Decision owner: not established.
- Supporting / enforcement mechanisms: approval policy; YOLO/budget controls; configuration files; user confirmations; model/runtime selection; retirement/maintainer governance outside the runtime organization.
- Closure path: not established.
- Why this is / is not agent-owned: operational permissions and human approval are not S5 unless identity/ultimate-policy matters are routed to a legitimate ultimate authority and returned as governing policy. No such first-party path was found.
- Evidence: [`agent/core/agent_loop.py`](https://github.com/huggingface/ml-intern/blob/3555becf822ab9b71be9678b2332f542a9fde0b5/agent/core/agent_loop.py); [`README.md`](https://github.com/huggingface/ml-intern/blob/3555becf822ab9b71be9678b2332f542a9fde0b5/README.md).
- Basis: structural absence conclusion.
- Confidence: high.

### Absence scope

- Surfaces inspected: approval and auto-approval rules, spend caps, provider/model/tool/runtime configuration, system/runtime prompts, user confirmations and repository retirement notice.
- Plausible first-party paths checked: human approvals, configuration authority, billing policy, scheduled-job safeguards and maintainer lifecycle decisions.
- Why no material first-party path remains: these are operational constraints or external project governance. No standard-distribution path closes an identity/ultimate-policy question and feeds the authoritative answer back into runtime governance.

## Distributed OSS parent arrangement

The frozen repository is a retired public OSS artifact. Contributor/maintainer decisions, including the retirement commit, govern the software project but are not imported into the running ML Intern session as S3/S4/S5 parent functions. No qualifying runtime parent notation is inferred.

## Self-hosted and non-human modes

The CLI can run interactively or headlessly, with local model endpoints and local tool execution or with external hosted providers/sandboxes. Headless auto-approval changes operational permission policy but does not add higher VSM functions. The preserved system remains autonomous at S1 in these modes where model/tool dependencies are available.

## Recursion

The research subagent is a separately contextualized model/tool actor, but its role is subordinate research decomposition and the evidence reviewed does not establish a recursively viable lower-level organization with its own metasystem. It is therefore not treated as proof of VSM recursion or S2 by topology alone.

## Variety and escalation

Tool plurality, MCP integration, local/sandbox alternatives and literature/code/data search amplify the focal agent's regulatory variety. Approval gates, spend caps, usage thresholds, iteration limits, doom-loop detection and context compaction attenuate unsafe or unproductive variety. Human confirmation can receive exceptional operations such as recurring or costly jobs. These are classified as mechanisms inside/around S1 unless the corresponding higher organizational function is independently established.

## Evidence gaps

- The assessment is anchored to the explicit retirement revision; no current maintenance/support claim is made.
- No runtime experiment was required because the preserved code and architecture documentation expose the first-party loop and supporting mechanisms directly.
- The independent research subagent is not credited as S2, S3* or S4 solely from separate context: its first-party contract is present-task research support, and no peer-interference, audit-challenge or prospective capability-adaptation closure was found.
- Doom-loop correction, unfinished-plan continuation, provider retry/switching, approvals and budget controls are strong operating controls but remain within/local to the focal S1 organization under Methodology 0.3.6.

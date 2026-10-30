---
harness_id: agent-harness-from-scratch
project_name: agent-harness-from-scratch
repository: https://github.com/sudhanshu-shivam-dev/agent-harness-from-scratch
review_ref: 2b5e810d1605fe416118bca88d9fcc006813a7a6
reviewed_at: 2026-10-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# agent-harness-from-scratch

## Review boundary

- System in focus: first-party Python ReActAgent in its supported OpenAILLM mode, with optional memory/compression/tool-output guard.
- Purpose and identity: demonstrate and execute bounded iterative tool-using agent tasks.
- Relevant environment: caller requests, registered tools, model responses, malformed tool calls, token/step exhaustion and untrusted observations.
- Standard-distribution boundary: Python agent modules and the documented USE_OPENAI construction path. Deterministic demo mode is considered separately.
- Credited operating / distribution surfaces: ReActAgent.run/step/think/act and OpenAILLM.chat; documented basic_tools.build_agent wires the supported real-model mode.
- Adjacent first-party surfaces excluded from ownership: offline MockLLM heuristic demo and browser mock playground do not supply autonomous ownership; EvalHarness/task scoring, tests and CI remain adjacent evaluation/development surfaces.
- First-party operating / deployment modes considered: Python real-model execution, optional memory/compression/guard, mock-only demonstration and separate evaluation runner.
- Recursion level: one task-solving agent run; shared memory may persist between calls in the same process.
- Reviewed revision: `2b5e810d1605fe416118bca88d9fcc006813a7a6`.
- Observation date: 2026-10-29.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

ReActAgent creates an ExecutionContext and repeatedly calls think/step/act until a model final answer or budget stop. Tool observations and retry guidance are appended to the transcript. OpenAILLM implements chat-completion tool calls and embeddings; MockLLM uses fixed task heuristics, and the browser playground is explicitly a deterministic mock. The documented build_agent supports an OpenAILLM branch selected by USE_OPENAI and credentials. This shipped branch, rather than the mock, supplies the S1 owner.

ExecutionContext records run/step IDs, state, token counts and trajectories. ShortTermMemory windows/summarizes context; LongTermMemory holds embeddings in process, recalls prior task/answer text and adds completed runs. ContextCompressor selects query-relevant text units, optionally using embeddings. ToolOutputGuard applies authored pattern redaction before observations reach the task model. EvalHarness creates fresh agents for fixed tasks, checks output/trajectory properties, optionally calls a judge and exports a scorecard; the normal agent run does not consume those findings as supervisory control.

## Operational model

The real-model mode delegates operational tool selection and answer judgment to the model-backed agent; tool registry, budget guard and output sanitization enforce caller/developer choices. The mock/browser modes do not independently justify S1 autonomy. No distinct S1 team is packaged. Memory retention, routine safety and external evaluation are analyzed on their actual functions and return paths.

## S1 — Operations

- State: A
- Function: solve caller tasks through a repeated think/act/observe loop.
- Disturbance / variety regulated: task uncertainty, actual tool results, malformed calls and incomplete answers.
- Decisive decision or feedback right: choose tool/arguments or final answer after observations.
- Decision owner: model-backed ReAct agent in OpenAILLM mode.
- Supporting / enforcement mechanisms: ToolRegistry dispatch, ExecutionContext, budgets/retry messages, context management and optional output guard.
- Closure path: act appends tool observations to context; the next think calls llm.chat on that context, until the model finishes.
- Boundary reachability: ReActAgent accepts the shipped OpenAILLM adapter, and examples/basic_tools.py documents and wires USE_OPENAI=1 with credentials. No external agent harness must be composed.
- Why this is / is not agent-owned: the real model supplies discretionary action selection; fixed mock heuristics and deterministic limits are explicitly not the credited owner.
- Evidence: [agent/agent.py](https://github.com/sudhanshu-shivam-dev/agent-harness-from-scratch/blob/2b5e810d1605fe416118bca88d9fcc006813a7a6/agent/agent.py); [agent/llm.py](https://github.com/sudhanshu-shivam-dev/agent-harness-from-scratch/blob/2b5e810d1605fe416118bca88d9fcc006813a7a6/agent/llm.py); [examples/basic_tools.py](https://github.com/sudhanshu-shivam-dev/agent-harness-from-scratch/blob/2b5e810d1605fe416118bca88d9fcc006813a7a6/examples/basic_tools.py); [README.md](https://github.com/sudhanshu-shivam-dev/agent-harness-from-scratch/blob/2b5e810d1605fe416118bca88d9fcc006813a7a6/README.md).
- Basis: structural.
- Confidence: high.
- Caveats: No live provider execution. The included finding is supported by the real-model mode, not default offline mock behavior.

## S2 — Coordination

- State: —
- Function: no first-party inter-S1 coordination relation is supplied.
- Disturbance / variety regulated: sequential tool observations belong to one task loop.
- Decisive decision or feedback right: no multi-unit collision/oscillation response exists in the inspected distribution.
- Decision owner: task model for local actions; caller for construction.
- Supporting / enforcement mechanisms: sequential registry dispatch, context state and per-step trajectory.
- Closure path: ordinary tool output returns to the same agent; no inter-unit corrective return.
- Why this is / is not agent-owned: a series of tool calls or fresh evaluation agents is not a coordinated operational organization.
- Evidence: [agent/agent.py](https://github.com/sudhanshu-shivam-dev/agent-harness-from-scratch/blob/2b5e810d1605fe416118bca88d9fcc006813a7a6/agent/agent.py); [agent/context.py](https://github.com/sudhanshu-shivam-dev/agent-harness-from-scratch/blob/2b5e810d1605fe416118bca88d9fcc006813a7a6/agent/context.py); [agent/tools.py](https://github.com/sudhanshu-shivam-dev/agent-harness-from-scratch/blob/2b5e810d1605fe416118bca88d9fcc006813a7a6/agent/tools.py); [README.md](https://github.com/sudhanshu-shivam-dev/agent-harness-from-scratch/blob/2b5e810d1605fe416118bca88d9fcc006813a7a6/README.md).
- Basis: structural.
- Confidence: high.
- Caveats: No S2 constructor from a generic registry or application-written extra agents.

### Absence scope

- Surfaces inspected: Complete Python module inventory, ReAct run/act dispatch, tool registry, context and EvalHarness fresh-agent loop.
- Plausible first-party paths checked: Multiple tool calls, shared memories/context, repeated evaluation instances and sequential execution.
- Why no material first-party path remains: These paths contain one S1 per task and no concrete inter-S1 interference with a function-specific attenuation/feedback relation.

## S3 — Inside-and-now control

- State: —
- Function: no whole-system current-control process is supplied.
- Disturbance / variety regulated: individual step/token exhaustion, tool failures and current prompt size.
- Decisive decision or feedback right: caller chooses limits and guard/compressor settings; no whole-system commitments/resources regulator.
- Decision owner: developer/caller for configured constraints; agent for task actions.
- Supporting / enforcement mechanisms: ExecutionContext.over_budget, force-finish, retry counters and compression threshold.
- Closure path: fixed limits stop the run or reduce prompt content; they do not return a discretionary whole-system allocation decision.
- Why this is / is not agent-owned: hard budgets and model task choice do not establish S3 ownership.
- Evidence: [agent/agent.py](https://github.com/sudhanshu-shivam-dev/agent-harness-from-scratch/blob/2b5e810d1605fe416118bca88d9fcc006813a7a6/agent/agent.py); [agent/context.py](https://github.com/sudhanshu-shivam-dev/agent-harness-from-scratch/blob/2b5e810d1605fe416118bca88d9fcc006813a7a6/agent/context.py); [agent/compression.py](https://github.com/sudhanshu-shivam-dev/agent-harness-from-scratch/blob/2b5e810d1605fe416118bca88d9fcc006813a7a6/agent/compression.py).
- Basis: structural.
- Confidence: high.
- Caveats: No parent mode from constructor parameters or running an evaluation command.

### Absence scope

- Surfaces inspected: Budget/finish/retry methods, context bookkeeping, optional memory/compression and documented construction.
- Plausible first-party paths checked: Budget trip, malformed-call retry, caller-selected caps and aggregate evaluation scorecards.
- Why no material first-party path remains: The supplied behavior is local execution enforcement and offline measurement, not a whole-system view with shared commitment/resource authority and returned current-control decision.

## S3* — Complementary audit

- State: —
- Function: no complementary audit with findings-to-control closure is wired into the agent runtime.
- Disturbance / variety regulated: task quality, expected tool use and trajectory errors are measured by a separate evaluation runner.
- Decisive decision or feedback right: no shipped auditor can challenge ordinary runtime claims and return authoritative corrective control.
- Decision owner: developer chooses tasks/judge and reads the scorecard; task model produces ordinary operations.
- Supporting / enforcement mechanisms: EvalHarness rule/trajectory checks, optional judge, dump_results and runtime trajectory IDs.
- Closure path: EvalHarness returns/exports a scorecard; ReActAgent.run does not consume it as a corrective supervisory decision.
- Why this is / is not agent-owned: an optional LLM judge and detailed trace do not supply an independent closed audit function at this operating boundary.
- Evidence: [agent/eval/harness.py](https://github.com/sudhanshu-shivam-dev/agent-harness-from-scratch/blob/2b5e810d1605fe416118bca88d9fcc006813a7a6/agent/eval/harness.py); [agent/agent.py](https://github.com/sudhanshu-shivam-dev/agent-harness-from-scratch/blob/2b5e810d1605fe416118bca88d9fcc006813a7a6/agent/agent.py); [agent/context.py](https://github.com/sudhanshu-shivam-dev/agent-harness-from-scratch/blob/2b5e810d1605fe416118bca88d9fcc006813a7a6/agent/context.py); [examples/run_eval.py](https://github.com/sudhanshu-shivam-dev/agent-harness-from-scratch/blob/2b5e810d1605fe416118bca88d9fcc006813a7a6/examples/run_eval.py).
- Basis: structural.
- Confidence: high.
- Caveats: The first-party evaluation subsystem is explicitly inspected rather than omitted because it is adjacent.

### Absence scope

- Surfaces inspected: Entire EvalHarness run/scoring/judge/export path, production run and trajectory/context interfaces.
- Plausible first-party paths checked: Alternative judge, raw trajectory scoring, scorecard export and any route back into production control.
- Why no material first-party path remains: The evaluation return ends at reporting; no first-party independent audit mandate and findings-to-control integration is supplied. Generic user consumption does not make an audit-specific constructor.

## S4 — Outside-and-then intelligence

- State: —
- Function: no prospective outside-and-then adaptation process is supplied.
- Disturbance / variety regulated: current context size and retrieval of previously solved tasks.
- Decisive decision or feedback right: no environmental/future distinctions generate capability options for adoption.
- Decision owner: caller chooses memory, compressor and model; agent makes current task decisions.
- Supporting / enforcement mechanisms: in-memory vector recall, task/answer insertion, summarization and query-aware extractive compression.
- Closure path: recalled text changes a future task prompt; no external/prospective adaptation-option judgment changes present capability.
- Why this is / is not agent-owned: memory reuse and compression are operational continuity rather than S4.
- Evidence: [agent/memory.py](https://github.com/sudhanshu-shivam-dev/agent-harness-from-scratch/blob/2b5e810d1605fe416118bca88d9fcc006813a7a6/agent/memory.py); [agent/compression.py](https://github.com/sudhanshu-shivam-dev/agent-harness-from-scratch/blob/2b5e810d1605fe416118bca88d9fcc006813a7a6/agent/compression.py); [agent/agent.py](https://github.com/sudhanshu-shivam-dev/agent-harness-from-scratch/blob/2b5e810d1605fe416118bca88d9fcc006813a7a6/agent/agent.py); [agent/eval/harness.py](https://github.com/sudhanshu-shivam-dev/agent-harness-from-scratch/blob/2b5e810d1605fe416118bca88d9fcc006813a7a6/agent/eval/harness.py).
- Basis: structural.
- Confidence: high.
- Caveats: Documentation cites research as implementation motivation; citations are not runtime environmental intelligence.

### Absence scope

- Surfaces inspected: Memory add/search/summarize, compressor, run memory writes, model selection and evaluation/reporting.
- Plausible first-party paths checked: Prior-task retrieval, summary update, query-aware text selection and offline scorecard-based improvement.
- Why no material first-party path remains: All shipped loops manage task context or measure outcomes; none supplies externally prospective distinctions, developed adaptation options and an adoption/return path into current capability, including a parent-governed alternative.

## S5 — Policy and identity

- State: —
- Function: no identity or ultimate-policy adjudication path is supplied.
- Disturbance / variety regulated: static system instructions and recognized injection directives in tool output.
- Decisive decision or feedback right: developer supplies prompt, guard patterns and allowed tools; no identity-level issue routing/return.
- Decision owner: developer/caller for static operating constraints.
- Supporting / enforcement mechanisms: ToolOutputGuard redaction, system prompt, tool schema and budget configuration.
- Closure path: sanitized text enters the normal task context; no ultimate authority decides a policy matter and returns it as governing identity.
- Why this is / is not agent-owned: safety enforcement and a system prompt do not establish S5.
- Evidence: [agent/safety.py](https://github.com/sudhanshu-shivam-dev/agent-harness-from-scratch/blob/2b5e810d1605fe416118bca88d9fcc006813a7a6/agent/safety.py); [agent/agent.py](https://github.com/sudhanshu-shivam-dev/agent-harness-from-scratch/blob/2b5e810d1605fe416118bca88d9fcc006813a7a6/agent/agent.py); [README.md](https://github.com/sudhanshu-shivam-dev/agent-harness-from-scratch/blob/2b5e810d1605fe416118bca88d9fcc006813a7a6/README.md).
- Basis: structural.
- Confidence: high.
- Caveats: No security efficacy or policy-authority claim from the guard's name.

### Absence scope

- Surfaces inspected: Default/custom instructions, guard pattern configuration, run construction and supported README modes.
- Plausible first-party paths checked: Injection detection/redaction, caller tool/prompt changes and evaluation feedback.
- Why no material first-party path remains: No supported identity/ultimate-policy issue → legitimate parent/internal authority → authoritative decision → governing return loop is shipped.

## Distributed OSS parent arrangement

Software-maintainer authority and CI are development surfaces, not a parent metasystem of installed agent runs. No project-recursion parent state is inferred.

## Self-hosted and non-human modes

The caller supplies credentials, tools and limits. The supported real-model branch establishes task agency; mock and browser demo modes remain deterministic. No function-specific S3/S4/S5 parent mode or non-human organization is established.

## Recursion

No recursively viable team or child system is supplied. Repeated calls and evaluation-created agents are not recursive viability.

## Variety and escalation

Tool error observations preserve repair choices for the model; static token/step limits, compression and injection redaction attenuate input/execution variety. Stop reasons, trajectories and scorecards are observability, not by themselves algedonic channels.

## Evidence gaps

Static source only; no provider/model E2E, browser or evaluation runs. Tool/model competence and security effectiveness are unmeasured. Memory is in process, not evidence of an autonomous adaptation organization. No concrete unresolved shipped higher-function path remains at the stated Python runtime boundary.

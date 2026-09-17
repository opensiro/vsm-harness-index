---
harness_id: haystack
project_name: Haystack
repository: https://github.com/deepset-ai/haystack
review_ref: 52df9672a7808e1091995f33189d1ff8e91b6998
reviewed_at: 2026-09-18
generated_profile_version: 0.2.2
generated_assessment_procedure_version: 0.3.1
profile_version: 0.2.2
assessment_procedure_version: 0.3.1
assessment_changed_at: 2026-09-18
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Haystack

## Review boundary

- System in focus: Haystack's first-party `Agent` runtime and supported `AgentTool` composition at pinned revision `52df9672a7808e1091995f33189d1ff8e91b6998`.
- Purpose: provide a reusable tool-using agent loop with typed state, configurable tools, hooks, stopping conditions, and agent-as-tool composition.
- Excluded from positive VSM claims: generic Pipeline/RAG infrastructure, external integrations/models, downstream application code, and user-authored hooks or specialist logic.
- Recursion level: one Haystack agent application; wrapped specialist Agents are considered only where first-party composition establishes a distinct organizational function.
- Generated/current Profile / Methodology: `0.2.2` / `0.3.1`.

## Primary evidence

- [`haystack/components/agents/agent.py`](https://github.com/deepset-ai/haystack/blob/52df9672a7808e1091995f33189d1ff8e91b6998/haystack/components/agents/agent.py) — first-party model/tool loop, typed State, stopping conditions, tool concurrency and hook points.
- [`haystack/tools/agent_tool.py`](https://github.com/deepset-ai/haystack/blob/52df9672a7808e1091995f33189d1ff8e91b6998/haystack/tools/agent_tool.py) — wraps an Agent as a callable tool for another Agent and returns the delegated Agent's final result.
- [multi-agent systems documentation](https://github.com/deepset-ai/haystack/blob/52df9672a7808e1091995f33189d1ff8e91b6998/docs-website/docs/concepts/agents/multi-agent-systems.mdx) — coordinator/specialist composition is explicitly implemented by delegation through `AgentTool`.
- [Agent hooks documentation](https://github.com/deepset-ai/haystack/blob/52df9672a7808e1091995f33189d1ff8e91b6998/docs-website/docs/pipeline-components/agents-1/hooks.mdx) — ready-made hooks cover compaction, human confirmation, tool-result offload and token budget; custom hooks may mutate live State and keep a run open.
- [agent-hooks release note](https://github.com/deepset-ai/haystack/blob/52df9672a7808e1091995f33189d1ff8e91b6998/releasenotes/notes/add-agent-hooks-4584408a3a2a2ad4.yaml) — documents a user-defined `GradeFinalAnswer` example that creates its own LLM judge and feeds failures back through `continue_run`.
- [`haystack/hooks/human_in_the_loop/hooks.py`](https://github.com/deepset-ai/haystack/blob/52df9672a7808e1091995f33189d1ff8e91b6998/haystack/hooks/human_in_the_loop/hooks.py) — built-in parent confirmation mechanism for pending tool calls.

## Repository architecture

The first-party Agent owns the iterative operational loop: it calls a chat generator, selects or receives tool calls, executes tools, merges their outputs into typed State, and continues until a configured exit condition or step budget is reached. Hook points can modify live State before LLM/tool calls, after tools, or at exit.

`AgentTool` composes another Haystack Agent as a tool. The documented multi-agent pattern uses a coordinator Agent to delegate focused tasks to specialist Agents while keeping specialist context isolated. The calling Agent receives the specialist's final reply rather than a persistent shared organizational control surface.

## S1 — Operations

- State: `A`.
- Function: autonomously execute a user goal by selecting tool calls, consuming tool results, updating state and iterating until completion.
- Decisive right / owner: the model-driven Agent decides which supplied tools to call and how to continue within its configured boundary.
- Closure: tool/state results return to subsequent model turns and change later operational behavior.
- Confidence: high.

## S2 — Coordination

- State: `—`.
- `AgentTool` can create coordinator/specialist topologies, but the first-party relation established at the pinned boundary is delegation: the coordinator gives one focused task to a wrapped Agent and receives its final result.
- No specific inter-S1 interference, oscillation or conflict plus an attenuation/feedback loop among independently operating specialist S1s was established.
- Tool concurrency limits, shared State, routing and context isolation are execution mechanisms, not S2 by themselves.
- Confidence: high.

## S3 — Inside-and-now control

- State: `—`.
- The coordinator label does not establish S3. The documented coordinator selects/delegates specialist work as part of its own task trajectory, but no distinct first-party actor was established that maintains a whole-system current view of multiple independently committed S1 units and exercises authority over their shared priorities/resources/commitments.
- Human confirmation of individual tool calls constrains one operational loop and is not whole-system S3 closure.
- Confidence: high.

## S3* — Complementary audit

- State: `—`.
- Hooks can observe or alter the normal run and can feed findings back through `continue_run`, but the standard distribution's ready-made hooks are compaction, HITL confirmation, result offload and token-budget controls rather than an independent complementary audit function.
- Haystack documentation shows how a user can write `GradeFinalAnswer` with a separate LLM judge. That demonstrates extensibility, but the judge itself and its audit decision are application-authored rather than a supplied first-party audit actor. Generic hook transport therefore is not promoted to constructor-owned S3*.
- Confidence: high.

## S4 — Outside-and-then intelligence

- State: `—`.
- An Agent may use search or other external-information tools and adapt its current task trajectory, but this remains S1 operational reasoning. No distinct first-party function was established that models future environmental change, develops organizational adaptation options, and closes them into changed future capability.
- Memory/state and hook extensibility do not establish S4 by themselves.
- Confidence: high.

## S5 — Policy and identity

- State: `—`.
- System prompts, exit conditions, tool sets, hook configuration and HITL policies are developer/operator-authored constraints. They do not establish a legitimate runtime identity/ultimate-policy decision loop.
- Human approval of individual tool calls is not S5 closure.
- Confidence: high.

## Recursion, variety, and escalation

Agent-as-tool composition permits nested operational specialization and context isolation, but delegation alone is not recursive viability. Tool catalogs, dynamic toolsets, state, concurrency controls and hooks expand/attenuate operational variety. HITL can escalate a tool decision to a human, but that escalation remains local execution authority rather than evidence of S3/S5 organizational closure.

## Admission conclusion

Canonical vector: `A — — — — —`.

Haystack clearly supplies an autonomous operational Agent runtime. Its multi-agent and hook surfaces are powerful construction primitives, but at the pinned standard-distribution boundary they do not themselves supply the disturbance-specific coordination, whole-system regulation, independent audit, prospective adaptation or ultimate-policy functions required for S2–S5.

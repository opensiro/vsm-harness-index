# OpenAI Agents SDK (2025)

## Review frame

- **System-in-focus:** the OpenAI Agents SDK's documented orchestration affordances, not a particular application or OpenAI as an organization
- **Repository:** <https://github.com/openai/openai-agents-python>
- **First public release:** [2025](https://openai.com/index/new-tools-for-building-agents/)
- **Reviewed version:** current documentation snapshot; release history around v0.22.x
- **Reviewed at:** 2026-09-12
- **Evidence scope:** official SDK documentation and release page; no deployed application behavior was observed

## Evidence mapping

| Function/property | Basis | Evidence and reasoning |
| --- | --- | --- |
| S1 | structural | [Agents and Runner](https://openai.github.io/openai-agents-python/) provide tool-using operational loops that act until final output, and agents can be composed as tools or handoff targets. This establishes operational capability at the framework boundary. |
| S2 | structural | [Agent orchestration](https://openai.github.io/openai-agents-python/multi_agent/) documents manager-owned specialists, handoffs, code orchestration, and parallel execution. These coordinate work, but damping of application-specific collisions and oscillation is not supplied as a whole organizational function. |
| S3 | structural | The [Runner lifecycle](https://openai.github.io/openai-agents-python/running_agents/) provides turn limits and execution control, while [usage tracking](https://openai.github.io/openai-agents-python/usage/) and guardrails contribute current regulation. Portfolio resource bargaining and whole-system operational authority remain application-defined. |
| S3* | structural | The orchestration guide documents an evaluator-agent loop that can test worker output. This can contribute to S3* when configured with sufficiently independent evidence and control. [Tracing](https://openai.github.io/openai-agents-python/tracing/) alone is observability, not independent audit, and the SDK does not establish the needed independence by default. |
| S4 | unknown | Tools could sense an environment and applications can build future-oriented intelligence, but the reviewed framework evidence does not establish an outside-and-then organizational function. |
| S5 | inferred | Instructions, guardrails, approvals, and application code can encode constraints. The [human-in-the-loop flow](https://openai.github.io/openai-agents-python/human_in_the_loop/) exposes approval authority, but identity and closure of S3–S4 tension remain with the application and its people. |
| Recursion | inferred | Nested agents-as-tools and handoffs support composition. The evidence does not show that a nested agent is a viable operational system with its own environment, autonomy, and metasystem. |
| Escalation | structural | [Human-in-the-loop interruptions](https://openai.github.io/openai-agents-python/human_in_the_loop/) can pause tool actions for approval or rejection across nested runs. Trigger policy and recipient authority are application-defined, and no general algedonic path is established. |
| Local autonomy | structural | Agents can choose tools, handoffs, and actions within instructions, but autonomy boundaries and parent-level cohesion depend on application design. |

## Interpretation

The SDK strongly supports operational agency and several orchestration patterns. It provides useful primitives for coordination, current control, evaluation, and human escalation, but it deliberately leaves organizational purpose and topology to application code. Consequently, S4 and full S5 cannot be inferred from the SDK, and evaluator or tracing features should not be promoted automatically to S3*.

## Uncertainty

The official documentation evolves quickly; the [release page](https://github.com/openai/openai-agents-python/releases) should be checked on the next review. A concrete deployed application could justify very different mappings.

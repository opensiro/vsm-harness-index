# Microsoft AutoGen AgentChat (2023)

## Review frame

- **System-in-focus:** AutoGen AgentChat's documented team and runtime affordances, not a configured team or Microsoft as an organization
- **Repository:** <https://github.com/microsoft/autogen>
- **First public release:** [2023](https://www.microsoft.com/en-us/research/blog/autogen-enabling-next-generation-large-language-model-applications/)
- **Reviewed version:** current stable documentation snapshot; Python release series around 0.7.x
- **Reviewed at:** 2026-09-12
- **Evidence scope:** official documentation and release page; no deployed application behavior was observed

## Evidence mapping

| Function/property | Basis | Evidence and reasoning |
| --- | --- | --- |
| S1 | structural | [AgentChat teams](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/teams.html) consist of agents working toward a goal, including specialist participants and tool-using agents. This establishes operational capability. |
| S2 | structural | Round-robin, selector, Magentic-One, and swarm team patterns select and constrain conversational participation. At the framework boundary these are explicit mechanisms for coordinating multiple operational actors, though their adequacy remains workload-specific. |
| S3 | structural | [Termination conditions](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/termination.html) regulate message, token, time, handoff, and external stop bounds; [team state](https://microsoft.github.io/autogen/dev/user-guide/agentchat-user-guide/tutorial/state.html) can be saved and restored. Whole-system resource bargaining and operational optimization are application-defined. |
| S3* | unknown | [Structured and trace logging](https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/framework/logging.html) exposes events, but observability does not establish an independent path able to challenge ordinary operational reporting. No sufficiently independent audit was established in the reviewed sources. |
| S4 | unknown | Agents can use external tools, but the framework documentation does not itself establish a future-oriented organizational intelligence function. |
| S5 | inferred | Team configuration, instructions, termination, and external control can realize policy constraints. The reviewed evidence does not establish organizational identity or closure of S3–S4 tension. |
| Recursion | inferred | Agents and teams can be composed, and release documentation describes agent/team tools. Technical nesting is evidenced; a nested viable system with its own environment and metasystem is not. |
| Escalation | structural | `HandoffTermination` can pause a run for application or user input, and `ExternalTermination` allows outside control. Whether the receiver has the required authority and whether a true algedonic bypass exists depend on the application. |
| Local autonomy | structural | Team participants can act and use tools under different team processes, while their decision rights and parent constraints are configured by the application. |

## Interpretation

AutoGen AgentChat provides unusually explicit multi-agent coordination and runtime stopping controls. Those are strong S2 evidence and partial S3/escalation evidence. Logging does not by itself justify S3*, and neither generic agents nor team composition establishes S4, S5, or recursive viability.

## Uncertainty

The stable and development documentation may describe different release points. Recheck the [release page](https://github.com/microsoft/autogen/releases) and pin a tag in a future source-code review.

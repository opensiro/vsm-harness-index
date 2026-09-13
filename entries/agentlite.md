# AgentLite (2024)

## Review frame

- **System-in-focus:** the AgentLite framework at its documented manager–worker examples, not a deployed application or Salesforce as an organization
- **Repository:** <https://github.com/SalesforceAIResearch/AgentLite>
- **First public release:** [2024](https://github.com/SalesforceAIResearch/AgentLite)
- **Reviewed version:** `main`; exact commit was unavailable in the reviewed source record
- **Reviewed at:** 2026-09-11
- **Evidence scope:** published source files and examples; no deployed application behavior was observed

## Evidence mapping

| Function/property | Basis | Evidence and reasoning |
| --- | --- | --- |
| S1 | structural | `BaseAgent.py` implements model-driven action loops with tools and memory; this is direct operational capability. |
| S2 | structural | `ManagerAgent.py` delegates task packages to labor agents. Delegation coordinates work, but the reviewed evidence does not establish robust damping of collisions or oscillation among autonomous units. |
| S3 | structural | Execution-step limits and manager control regulate current work. Resource bargaining, portfolio metrics, and evidence-backed whole-system intervention are weak. |
| S3* | unknown | Benchmark and logging material were found, but no sufficiently independent route to raw operational reality was established. Missing evidence is not converted to `no`. |
| S4 | unknown | The review found no evidence that external/future intelligence changes the framework's own priorities or premises. Applications may add it. |
| S5 | inferred | Agent roles and prompts can carry local constraints, but organizational identity and closure of S3–S4 tension were not demonstrated. |
| Recursion | inferred | Manager and worker loops show technical nesting. The evidence does not establish that workers are recursively viable systems with their own environments and metasystems. |
| Escalation | unknown | No bounded exception path to a recipient with demonstrated authority was established in the reviewed sources. |
| Local autonomy | structural | Workers perform delegated action loops, but the evidence does not fully establish negotiated autonomy within parent-level cohesion. |

## Interpretation

The reviewed sources support a manager–worker agent harness with strong operational capability and basic coordination. The most consequential gaps are independent S3* evidence, future-oriented S4, and demonstrated policy/escalation relationships.

## Evidence limitations

The source review used published `main` files without an exact commit. Re-review against a pinned commit before using the entry for longitudinal claims.

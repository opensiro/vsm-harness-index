# Benchmark ↔ system observation registry

Status: **generated, experimental, non-normative**

Generated from the raw JSON records in this directory by `render_registry.py`.
Numeric benchmark payloads remain only in the raw record; this table is an identity/provenance projection, not a second result database.

Raw observations: **7**

| System | Canonical harness | Observation | Benchmark surface(s) | Kind | Provenance | Compatibility | Raw record |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LLaMAR | [llamar](../../../assessments/llamar.md) | `llamar-agent-count-interference-mapthor-sar` | MAP-THOR / SAR | `native-disturbance-characterization` | `first-party-reported` | `native-system` | [llamar.json](llamar.json) |
| LLaMAR | [llamar](../../../assessments/llamar.md) | `llamar-mapthor-module-ablation-gpt4v` | MAP-THOR | `native-mechanism-ablation` | `first-party-reported` | `native-system` | [llamar.json](llamar.json) |
| Magentic-One | [autogen-agentchat](../../../assessments/autogen-agentchat.md) | `magentic-one-gpt4o-o1-test-results` | GAIA; AssistantBench; WebArena | `system-outcome` | `first-party-reported` | `native-system` | [magentic-one.json](magentic-one.json) |
| Magentic-One | [autogen-agentchat](../../../assessments/autogen-agentchat.md) | `magentic-one-gpt4o-test-results` | GAIA; AssistantBench; WebArena | `system-outcome` | `first-party-reported` | `native-system` | [magentic-one.json](magentic-one.json) |
| Magentic-One | [autogen-agentchat](../../../assessments/autogen-agentchat.md) | `magentic-one-simple-orchestrator-gaia-ablation` | GAIA | `native-mechanism-ablation` | `first-party-reported` | `native-system` | [magentic-one.json](magentic-one.json) |
| Squad | [squad](../../../assessments/squad.md) | `squad-marble-aligned-coordination-ablation` | MARBLE aligned four-domain re-run | `native-mechanism-ablation` | `first-party-reported` | `native-system` | [squad.json](squad.json) |
| Squad | [squad](../../../assessments/squad.md) | `squad-marble-completion-ablation` | MARBLE factorial ablation | `native-mechanism-ablation` | `first-party-reported` | `native-system` | [squad.json](squad.json) |

VSM-function relevance is intentionally absent from this generated registry. Derived/community interpretations reference the raw `observation_id` separately.

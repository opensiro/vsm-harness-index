# Benchmark ↔ system observation registry

Status: **generated, experimental, non-normative**

Generated from the raw JSON records in this directory by `render_registry.py`.
Numeric benchmark payloads remain only in the raw record; this table is an identity/provenance projection, not a second result database.

Raw observations: **11**

| System | Canonical harness | Observation | Benchmark surface(s) | Kind | Provenance | Compatibility | Raw record |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A-Evolve | [a-evolve](../../../assessments/a-evolve.md) | `a-evolve-harness-updating-2026` | A-Evolve harness-evolution study: SWE-bench Verified / MCP-Atlas / SkillsBench | `persistent-harness-update-study` | `first-party-reported` | `native-system` | [a-evolve.json](a-evolve.json) |
| KADATH | [kadath](../../../assessments/kadath.md) | `kadath-ten-epoch-native-evolution-2026` | KADATH operator-approved run-specific locked fitness benchmark | `longitudinal-population-evolution` | `first-party-reported` | `native-system` | [kadath.json](kadath.json) |
| LLaMAR | [llamar](../../../assessments/llamar.md) | `llamar-agent-count-interference-mapthor-sar` | MAP-THOR / SAR | `native-disturbance-characterization` | `first-party-reported` | `native-system` | [llamar.json](llamar.json) |
| LLaMAR | [llamar](../../../assessments/llamar.md) | `llamar-mapthor-module-ablation-gpt4v` | MAP-THOR | `native-mechanism-ablation` | `first-party-reported` | `native-system` | [llamar.json](llamar.json) |
| Magentic-One | [autogen-agentchat](../../../assessments/autogen-agentchat.md) | `magentic-one-gpt4o-o1-test-results` | GAIA; AssistantBench; WebArena | `system-outcome` | `first-party-reported` | `native-system` | [magentic-one.json](magentic-one.json) |
| Magentic-One | [autogen-agentchat](../../../assessments/autogen-agentchat.md) | `magentic-one-gpt4o-test-results` | GAIA; AssistantBench; WebArena | `system-outcome` | `first-party-reported` | `native-system` | [magentic-one.json](magentic-one.json) |
| Magentic-One | [autogen-agentchat](../../../assessments/autogen-agentchat.md) | `magentic-one-simple-orchestrator-gaia-ablation` | GAIA | `native-mechanism-ablation` | `first-party-reported` | `native-system` | [magentic-one.json](magentic-one.json) |
| Multi-Agent Orchestration Engine | [multi-agent-orchestration](../../../assessments/multi-agent-orchestration.md) | `multi-agent-orchestration-supervisor-ablation-2026-08` | Multi-Agent Orchestration supervisor ablation (54 scripted scenarios) | `native-mechanism-ablation` | `first-party-reported` | `native-system` | [multi-agent-orchestration.json](multi-agent-orchestration.json) |
| Squad | [squad](../../../assessments/squad.md) | `squad-marble-aligned-coordination-ablation` | MARBLE aligned four-domain re-run | `native-mechanism-ablation` | `first-party-reported` | `native-system` | [squad.json](squad.json) |
| Squad | [squad](../../../assessments/squad.md) | `squad-marble-completion-ablation` | MARBLE factorial ablation | `native-mechanism-ablation` | `first-party-reported` | `native-system` | [squad.json](squad.json) |
| TheAppliedScientist | [appliedscientist](../../../assessments/appliedscientist.md) | `appliedscientist-iterative-review-2026-09` | AppliedScientist iterative reviewer-guided revision study (30 papers) | `iterative-review-revision-study` | `first-party-reported` | `native-system` | [appliedscientist.json](appliedscientist.json) |

VSM-function relevance is intentionally absent from this generated registry. Derived/community interpretations reference the raw `observation_id` separately.

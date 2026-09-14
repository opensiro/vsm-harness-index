---
harness_id: agentsilex
project_name: AgentSilex
repository: https://github.com/howl-anderson/agentsilex
review_ref: cd529f2838151fd8a4f0d6b7054a45d829b3f78d
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: ?
autonomy_s3_star: C
autonomy_s4: ?
autonomy_s5: —
---

# AgentSilex

## Review boundary
AgentSilex at the pinned revision as a minimal agent framework with handoffs, agents-as-tools, tracing and a first-party evaluation framework.

## Repository architecture
Agents use tools/sessions and can hand off to specialist subagents. The framework includes OpenTelemetry traces and a dedicated evaluation package with tool-trajectory, response-matching and LLM-as-judge evaluators. HITL is roadmap-only at this revision.

## Primary evidence
- `README.md`: single/multi-agent execution, handoffs, agents-as-tools, tracing, evaluation framework and roadmap status.
- `src/agentsilex/evaluation/__init__.py`: exports `AgentEvaluator`, `ToolTrajectoryEvaluator` and response evaluators as first-party evaluation primitives.
- `src/agentsilex/evaluation/metric_evaluators/__init__.py`: exports `LLMJudgeEvaluator`, rubric-based evaluation and judge verdicts.
- `demo/eval_weather_agent.py`: composes an agent evaluator with an explicit `LLMJudgeEvaluator` threshold.

## Operational model
Agents are S1. Handoffs route/delegate work. The evaluation framework creates a distinct first-party path for judging trajectories/results, but independence and corrective authority are not closed out of the box.

## S1 — Operations
`A`: agents autonomously choose tools/actions toward tasks. Confidence: high.

## S2 — Coordination
`—`: documented handoffs are routing/delegation, not anti-oscillation among peer S1 units.

## S3 — Inside-and-now control
`?`: no autonomous whole-system regulator verified.

## S3* — Complementary audit
`C`: first-party evaluation explicitly exposes trajectory/result judging including LLM-as-judge, a complementary evidence path; a developer must still compose sufficient evaluator independence, alternative reality access where needed, and corrective feedback/authority. Confidence: high.

## S4 — Outside-and-then intelligence
`?`: no prospective environment/adaptation loop verified.

## S5 — Policy and identity
`—`: HITL/guardrails are not shipped at this revision and no runtime ultimate-policy closure is supplied.

## Recursion, variety, escalation
Specialist handoffs are operational decomposition, not recursion.
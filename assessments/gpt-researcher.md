---
harness_id: gpt-researcher
project_name: GPT Researcher
repository: https://github.com/assafelovic/gpt-researcher
review_ref: 6f998577d547b1e54ec662dac63583aa11e3b84b
reviewed_at: 2026-09-15
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# GPT Researcher

## Review boundary
GPT Researcher at the pinned revision, including its first-party multi-agent ChiefEditor workflow rather than only the top-level single-researcher path.

## Repository architecture
The multi-agent path creates Research, Editor, Writer, FactChecker, Visualizer, Publisher and Human agents and wires them into a LangGraph `StateGraph`. The graph is browser → planner → human → researcher → writer → fact_checker → visualizer → publisher, with bounded human-plan and fact-check revision loops. Parallel research is task fan-out managed by the editor path.

## Primary evidence
- `multi_agents/agents/orchestrator.py`: `ChiefEditorAgent` initializes the role agents and constructs the fixed `StateGraph`; conditional edges implement bounded plan-revision and fact-check-revision loops.
- `multi_agents/agents/fact_checker.py`: `FactCheckerAgent` reviews the assembled draft from the same shared `ResearchState`, returns issues or acceptance, and increments the fact-check revision count.
- `tests/test_multi_agents_route_bindings.py`: regression tests verify that the fact-check route is bound, respects the task-configured revision ceiling, and that the ChiefEditor workflow can be constructed.
- `README.md`: the planner generates research questions, execution agents gather information, and the publisher aggregates findings; this describes fan-out/fan-in task decomposition.

## Operational model
Research workers are S1 operations. The ChiefEditor graph assigns/sequences those roles and bounds revision loops. That is orchestration, but the inspected paths do not show mutual adjustment among S1s or whole-system resource bargaining. The FactChecker is a distinct model role, yet it is still a mandatory QA stage fed by the same production state rather than a complementary access path to operational reality.

## S1 — Operations
`A`: research/execution agents autonomously gather evidence and produce bounded research outputs. Confidence: high.

## S2 — Coordination
`—`: planner fan-out, parallel execution, graph edges and publisher fan-in assign or sequence work. No inspected first-party path regulates destructive interference among multiple S1 units through mutual adjustment or shared constraints. Confidence: high.

## S3 — Inside-and-now control
`—`: `ChiefEditorAgent` constructs and runs a static workflow and bounded revision routes, but does not hold the required whole-system authority over shared budgets, priorities, commitments or resources across S1s. Confidence: high.

## S3* — Complementary audit
`—`: FactChecker is specialized and can reject a draft, but it is an ordinary mandatory QA node in the same production graph and reads the same `ResearchState` produced by the research/writing path. The reviewed implementation provides no materially different or sufficiently independent access to operational reality. Confidence: high.

## S4 — Outside-and-then intelligence
`—`: web research is externally oriented but serves the current research question. It does not model future environmental change or develop adaptation options coupled back to present organizational control. Confidence: high.

## S5 — Policy and identity
`—`: the task, model, revision ceilings and human plan approval are supplied from outside the autonomous team. No runtime actor provides legitimate ultimate identity/policy closure. Confidence: high.

## Recursion, variety, escalation
Parallel researchers amplify evidence-gathering variety and bounded review loops attenuate output error. The Human node escalates to parent authority; role graphs and nested research tasks are not recursively viable systems by themselves.
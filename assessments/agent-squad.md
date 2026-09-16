---
harness_id: agent-squad
project_name: Agent Squad
repository: https://github.com/2FastLabs/agent-squad
review_ref: 31eccfeb0d546262d1d0ec2e2e5239186f8d2954
reviewed_at: 2026-09-15
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
last_checked_ref: 31eccfeb0d546262d1d0ec2e2e5239186f8d2954
last_checked_at: 2026-09-17
assessment_changed_at: 2026-09-15
last_reassessment_round: R2
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Agent Squad

## Review boundary
Agent Squad at the pinned revision across classifier orchestration and the first-party `SupervisorAgent` pattern.

## Repository architecture
Classifier routing selects specialized agents for ordinary conversations. Separately, `SupervisorAgent` wraps a lead LLM around a team: the lead can contact multiple specialists in parallel, retains per-agent conversation memory and acts as the sole intermediary when information has to move between otherwise unaware specialists.

## Primary evidence
- `python/src/agent_squad/agents/supervisor_agent.py`: the supervisor lead receives all team definitions and historical agent memory, selects which agents are necessary, sends parallel messages and forwards answers/questions between them.
- The supervisor prompt explicitly says team agents are unaware of each other and the lead must act as their sole intermediary, forwarding required context and using only necessary agents.
- `python/src/tests/agents/test_supervisor_agent.py` covers the first-party supervisor implementation at the pinned ref.

## Operational model
Specialized agents are S1. Basic classifier routing is only dispatch. The optional SupervisorAgent adds an active intermediary that regulates information exchange among multiple S1s, which crosses the S2 threshold but does not itself establish a whole-team S3 resource/accountability regulator.

## S1 — Operations
`A`: specialized agents independently process routed/delegated tasks with their tools. Confidence: high.

## S2 — Coordination
`C`: SupervisorAgent is a first-party composable coordination path: the lead mediates all cross-agent information, decides who needs contact and can fan out in parallel. It is optional rather than the default classifier path.

## S3 — Inside-and-now control
`—`: the lead delegates and aggregates around a user request but has no evidenced persistent whole-team task/resource ledger, commitment-reallocation authority or current organizational control comparable to S3.

## S3* — Complementary audit
`—`: GroundedAgent/presenter separation and ordinary specialist synthesis are production composition, not a distinct independent audit channel with corrective authority.

## S4 — Outside-and-then intelligence
`—`: no distinct prospective environment/adaptation function coupled back to S3 is established.

## S5 — Policy and identity
`—`: team membership, prompts, classifiers and supervisory rules remain application configured.

## Recursion, variety, escalation
Supervisor/team composition increases variety but does not by itself establish recursive viable-system closure.
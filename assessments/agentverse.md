---
harness_id: agentverse
project_name: AgentVerse
repository: https://github.com/OpenBMB/AgentVerse
review_ref: f90c4bd9680fdd3bcff8c52c9170911a59b23478
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# AgentVerse

## Review boundary
AgentVerse at the pinned revision, covering its task-solving and simulation frameworks for multiple LLM agents.

## Repository architecture
The repository explicitly deploys multiple LLM-based agents for collaborative task solving and environment simulation. The simulation environment supplies pluggable order rules that determine which agents may speak on a turn.

## Primary evidence
- `README.md`: multi-agent task-solving/simulation and a configured environment with bounded dialogue turns, sequential order and shared visibility.
- `agentverse/environments/simulation_env/rules/base.py`: the environment asks the order rule for the index of the next agent to speak.
- `agentverse/environments/simulation_env/rules/order/sequential.py`: a first-party round-robin conversation order.
- `agentverse/environments/simulation_env/rules/order/random.py` and `order/concurrent.py`: alternative first-party turn-selection/concurrency policies.

## Operational model
Role agents are S1 units. Environment/order protocols specifically constrain who interacts when and therefore expose a coordination path rather than mere tool routing.

## S1 — Operations
`A`: role agents autonomously perform bounded task/environment actions. Confidence: high.

## S2 — Coordination
`C`: first-party environment/order protocols expose turn-taking and interaction constraints that can damp collisions among S1 units, but the selected rule and wider coordination policy remain scenario-composed. Confidence: high.

## S3 — Inside-and-now control
`?`: chief/manager roles in examples do not establish a general autonomous whole-system resource/accountability regulator.

## S3* — Complementary audit
`?`: tester/reviewer roles may challenge work but routine QA in the production chain is not sufficient evidence of independent complementary audit.

## S4 — Outside-and-then intelligence
`?`: simulation environments provide external signals without proving a future-oriented adaptation loop coupled to S3.

## S5 — Policy and identity
`?`: roles/scenario configuration do not establish runtime ultimate policy.

## Recursion, variety, escalation
Multiple role agents are explicit, but a multi-agent simulation/task team is not assumed recursively viable without its own metasystemic closure.
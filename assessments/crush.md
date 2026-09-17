---
harness_id: crush
project_name: Crush
repository: https://github.com/charmbracelet/crush
review_ref: ef7bae117905a3927b177ed6923f36e811737d53
reviewed_at: 2026-09-17
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
last_checked_ref: ef7bae117905a3927b177ed6923f36e811737d53
last_checked_at: 2026-09-17
assessment_changed_at: 2026-09-17
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Crush

## Review boundary
Crush at the pinned current `main` revision, including the primary coding agent, task-agent tool, coordinator, hooks and permission service. The assessment treats parallel delegation and per-tool permission serialization as execution support unless a distinct VSM function is established.

## Repository architecture
Crush supplies an autonomous coding-agent loop and a first-party `agent` tool backed by a configured task agent. The tool uses a parallel-agent implementation, but each call remains scoped delegation from the primary S1 to a child S1. Separately, the permission service serializes pending tool permission requests and lets UI/hook policy grant or deny an individual tool action. That permission machinery is strong enforcement, but it does not by itself decide organization-wide resource/commitment policy.

## Primary evidence
- [`internal/agent/agent_tool.go`](https://github.com/charmbracelet/crush/blob/ef7bae117905a3927b177ed6923f36e811737d53/internal/agent/agent_tool.go): exposes the model-facing task-agent tool and delegates each prompt to a subagent through `runSubAgent`.
- [`internal/permission/permission.go`](https://github.com/charmbracelet/crush/blob/ef7bae117905a3927b177ed6923f36e811737d53/internal/permission/permission.go): serializes per-tool permission requests, supports first-writer-safe grant/deny, persistent grants, hook pre-approval and session auto-approval.
- Current upstream delta through `ef7bae117905a3927b177ed6923f36e811737d53` was reviewed; newer plan/main-agent surfaces do not establish an additional VSM metasystem function at this boundary.

## Operational model
The primary coding agent performs autonomous repository work and may delegate a bounded prompt to task agents. Hooks and the permission service constrain individual tool actions around those operational trajectories.

## S1 — Operations
`A`: the primary coding agent autonomously selects tools/actions and iterates from repository/tool feedback. Confidence: high.

## S2 — Coordination
`—`: parallel task-agent fan-out is delegation. No specific inter-S1 interference, oscillation or conflict plus a first-party attenuation/feedback relation was established. Serialized permission prompts concern tool authorization, not mutual adjustment among autonomous S1 units. Confidence: high.

## S3 — Inside-and-now control
`—`: the permission service grants or denies individual tool actions and the coordinator runs delegated agents, but no whole-system current view plus organizational authority over shared resources, commitments, priorities or accountability was established. Confidence: high.

## S3* — Complementary audit
`—`: hooks and permission checks sit in the normal execution/authorization path; no sufficiently independent complementary audit channel with alternative access to operational reality was established. Confidence: high.

## S4 — Outside-and-then intelligence
`—`: no prospective environment-facing adaptation loop was established. Confidence: high.

## S5 — Policy and identity
`—`: grant/deny decisions are operational tool permissions. They do not establish identity or ultimate-policy closure, so ordinary human permission prompts are not published as `S5=P`. Confidence: high.

## Recursion, variety, escalation
Task agents add bounded operational variety. Permission serialization and hooks attenuate execution risk, but the reviewed evidence does not establish S2–S5 organizational closure.

## Admission conclusion
Canonical vector at the pinned revision: `A — — — — —`. The prior `A C C — — P` proposal over-promoted parallel delegation and operational permission machinery.
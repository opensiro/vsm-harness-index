---
harness_id: microsoft-agent-framework
project_name: Microsoft Agent Framework
repository: https://github.com/microsoft/agent-framework
review_ref: 1cd06c5a2058a172eebadf5d9d7c3fa45c519520
reviewed_at: 2026-09-15
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Microsoft Agent Framework

## Review boundary
Deep review of the pinned orchestration package, especially the Magentic manager. Generic graph workflows are not enough for S2/S3; the positive classifications below come from explicit agent-owned regulation in the Magentic path.

## Repository architecture
Microsoft Agent Framework provides stateful operational agents and several orchestration patterns. The Magentic implementation is materially stronger than ordinary workflow routing: a manager maintains team-level facts, plan and progress, selects the next worker, detects lack of progress/repetitive behavior, and can reset/replan the team execution. This creates genuine metasystem decision rights over current multi-agent work.

## Primary evidence
- `python/packages/orchestrations/agent_framework_orchestrations/_magentic.py`: manager state includes facts, plan, progress and ledger-style team context.
- The manager selects the next participant/action from whole-team state and monitors execution progress.
- The implementation detects stalls/repetitive or non-progressing execution and triggers reset/replanning behavior rather than merely forwarding tasks.

## Operational model
Specialist agents perform operational work while an autonomous manager repeatedly interprets whole-team progress, regulates who acts next, and revises the current plan when execution fails to converge.

## S1 — Operations
`A`: specialist agents autonomously perform bounded tool/model work and return operational outcomes. Confidence: high.

## S2 — Coordination
`A`: the Magentic manager actively detects loop/stall/no-progress conditions and changes team execution to restore convergence. This is agent-owned regulation of instability among operational units, not static graph topology. Confidence: high.

## S3 — Inside-and-now control
`A`: the manager owns a whole-team current-state ledger of facts/plan/progress, chooses who acts next, and has reset/replan authority over current commitments. This is a genuine inside-and-now control function. Confidence: high.

## S3* — Complementary audit
`—`: the same manager that regulates current work observes progress; no organizationally distinct complementary audit channel with independent access/authority was established.

## S4 — Outside-and-then intelligence
`—`: replanning responds to current execution failure. The reviewed implementation does not establish a separate prospective external-environment intelligence function that adapts future system capability/strategy.

## S5 — Policy and identity
`—`: goals, participants, instructions and orchestration policy remain application-defined rather than autonomously owned as ultimate organizational identity/policy.

## Recursion, variety, escalation
Magentic closes more of the metasystem than ordinary agent frameworks: S2 and S3 are agent-owned around multiple S1s. It still lacks evidenced S3*, S4 and S5 closure.
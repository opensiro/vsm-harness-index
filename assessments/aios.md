---
harness_id: aios
project_name: AIOS
repository: https://github.com/agiresearch/AIOS
review_ref: 292d98f78c835499df18cdb6de6325bba1895862
reviewed_at: 2026-09-17
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
assessment_changed_at: 2026-09-17
status: excluded-no-agentic-vsm
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# AIOS

## Review boundary

- System in focus: the first-party AIOS Kernel/runtime at pinned revision `292d98f78c835499df18cdb6de6325bba1895862`.
- Standard-distribution boundary: AIOS-owned scheduling, context switching, LLM/memory/storage/tool queues and kernel services. Operational agents onboarded through Cerebrum or other agent frameworks are adjacent runtimes and are not inherited as AIOS-owned S1 actors.
- Reviewed revision: `292d98f78c835499df18cdb6de6325bba1895862`.
- Accepted recheck date: 2026-09-17.
- Accepted contract: Profile `0.2.1` / Methodology `0.3.1`.

## Repository architecture

AIOS supplies an agent-operating-system kernel: FIFO/round-robin scheduling, time slicing, context snapshot/restore, service queues, memory/storage/tool management and configurable runtime services. Those are substantial first-party infrastructure and regulation surfaces, but the domain-operational agent loops consuming them are onboarded from adjacent agent frameworks rather than implemented as first-party AIOS operational agents at this repository boundary.

## Operational model

The accepted same-ref recheck performed with batch #29 separated the kernel from Cerebrum/external agents. Removing the onboarded agent runtime while leaving the AIOS Kernel intact leaves scheduling, queues, context management and service infrastructure, but no first-party autonomous S1 actor that interprets arbitrary operational goals and closes the substantive model/tool/action loop. Constructor/control-plane capabilities are therefore not published as positive VSM autonomy states for an included autonomous harness.

## Exclusion conclusion

`excluded-no-agentic-vsm` at the repository-local AIOS Kernel boundary. The historical proposal vector `C C C — — C` is superseded by the accepted batch-#29 recheck recorded in Index PR #116: AIOS does not establish repository-local `S1=A`, so it does not satisfy the Index inclusion boundary. No positive autonomy claims are published for this excluded row.

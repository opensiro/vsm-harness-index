---
harness_id: aios
project_name: AIOS
repository: https://github.com/agiresearch/AIOS
review_ref: 292d98f78c835499df18cdb6de6325bba1895862
reviewed_at: 2026-09-16
status: proposed
autonomy_s1: C
autonomy_s2: C
autonomy_s3: C
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: C
---

# AIOS

## Review boundary
Pinned kernel/runtime hosting external/onboarded agents issuing syscalls.

## Repository architecture
AIOS supplies FIFO/RR scheduling, time slicing, LLM/memory/storage/tool queues, context snapshot/restore and scheduler configuration.

## Primary evidence
- Pinned deep review established syscall-hosted agents, RR/FIFO scheduling, time slicing, service queues and context snapshot/restore at `review_ref`.

## Operational model
Hosted agents provide domain cognition while the kernel regulates contention and resource/service access.

## S1 — Operations
`C`: hosted agents provide operational cognition through kernel services. Confidence: high.

## S2 — Coordination
`C`: round-robin/time-slice scheduling regulates contention among operations. Confidence: high.

## S3 — Inside-and-now control
`C`: resource/time-slice/service-queue control provides constructor-owned current regulation. Confidence: high.

## S3* — Complementary audit
`—`: no independent complementary audit channel was established. Confidence: high.

## S4 — Outside-and-then intelligence
`—`: no prospective organizational adaptation function was established. Confidence: high.

## S5 — Policy and identity
`C`: kernel/scheduler configuration is an executable constructor-owned policy surface. Confidence: medium-high.

## Recursion, variety, escalation
Scheduling and queues attenuate resource contention; context snapshot/restore preserves operational continuity but does not by itself establish recursion.

## Deep-review conclusion
Signature at the pinned revision: `C C C — — C`. AIOS is a kernel-like constructor closing coordination/current regulation around externally supplied agents.
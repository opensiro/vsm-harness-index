# Ouroboros — S1 capability evidence

## Frozen boundary

- repository: `razzant/ouroboros`
- review_ref: `86806ee123ce8e26cc063cc1a618f975eea64f26`
- canonical S1 state: `A`
- canonical assessment: [`assessments/ouroboros.md`](../../../assessments/ouroboros.md)

## Credited S1 boundary

- first-party S1 actor / loop: `OuroborosAgent` and the root task pipeline that owns task execution, state/evidence capture, terminalization, and final integration;
- environment-facing action path: admitted/direct task → first-party agent loop and tool execution → typed results/artifacts/evidence → root outcome and delivery path;
- external substrates: model/provider inference, operating-system and external tools, and Claudexor/connected coding harnesses when delegated coding or hosted-agent execution is used.

Delegated coding performed by Claudexor or another connected harness is not credited as native. Ouroboros's task ownership, evidence handling, acceptance, and integration around that execution are first-party transformations and therefore can be `mixed`.

## S1 evidence

| S1 dimension | Ownership | Evidence domain | Evidence type | Observation | Confidence |
| --- | --- | --- | --- | --- | --- |
| operational effectiveness | `mixed` | Coding / SWE; desktop-computer operation | matched-model/public benchmark artifacts, **self-reported** | The frozen README reports several model-matched Terminal-Bench 2.1 results with public runs, including Opus-4.8 `80.22%` vs Claude Code `78.9%` and GPT-5.5 `84.3%` vs Codex CLI `83.1%`; it also reports OSWorld and other campaigns with traces. Because the benchmark publication and interpretation are maintained by Ouroboros, these remain self-reported despite inspectable public artifacts. | medium-high |
| environment-interaction fidelity | `mixed` | general tool execution; Coding / SWE | executable/technical architecture + benchmark traces | The first-party loop records typed tool/error/evidence state and preserves execution outcomes. Direct execution is first-party; delegated coding execution may be supplied by Claudexor/another coding harness, so aggregate environment-facing capability is mixed. Benchmark success provides task-level evidence but does not isolate tool-call fidelity as its own ablation. | medium |
| operational state continuity | `native` | general | primary technical architecture | The root pipeline retains a delivery candidate before later verification/review, stores typed task results and artifacts, carries lifecycle/usage evidence, and checkpoints post-task work. These mechanisms preserve the current operational trajectory across later failures and terminalization paths. | high |
| recovery / resilience | `native` | general | primary technical architecture / executable paths | Provider death, retry-wall exhaustion, context-overflow/finalization paths, unresolved tool errors, deadlines, and cancellation are represented as distinct typed rails. A provider-death path may salvage useful text while still terminalizing the task as failed rather than fabricating success; retained delivery candidates prevent a later outage/reviewer failure from erasing usable work. No cohort-matched failure-injection rate was found. | high |
| operational result assurance | `native` | general; Coding / SWE | primary technical architecture | The root outcome path separates execution/objective/review/artifact axes, treats verify-before-done receipts and exact artifact references as host-attested evidence, and provides host-enforced task acceptance over observable effects and criteria. Independent reviewer existence is not counted by itself; credit is limited to the first-party root completion path that consumes verification/acceptance evidence before terminal delivery. | high |
| efficiency | `native` | general | implementation/technical documentation | The runtime tracks usage ledgers, transcript-prefix/cache continuity, budgets and retry walls. These are first-party resource-control mechanisms, but no frozen matched successful-work comparison isolates their resource savings. **insufficient evidence** for comparative efficiency. | medium |
| portability / robustness | `mixed` | Coding / SWE | multi-model matched benchmark series, **self-reported** | The same harness family reports Terminal-Bench 2.1 results with Opus-5, Opus-4.8, GPT-5.5 and Grok-4.5, plus additional task families. This is evidence that useful S1 operation survives several model substrates, but results remain self-reported and domain/task-family specific; remote/local model support alone is not counted as robustness. | medium |

## Specialized-domain witnesses

- Coding / SWE: strongest benchmark witness; Terminal-Bench 2.1 and SWE-bench Pro are reported with matched-model comparisons/public artifacts.
- Research / Science: **insufficient evidence** for a controlled projection in this batch.
- Government / Public Administration: **insufficient evidence**.
- other applicable domains: OSWorld-Verified supplies a desktop/computer-operation witness; it is not promoted into a universal S1 claim.

## Controlled / benchmark evidence

The frozen README explicitly describes these results as **self-reported**. Relevant examples include:

- Terminal-Bench 2.1, Claude Opus-5 high: `86.74%` after zeroing one disclosed reward-hack trial (raw `86.97%`), public submission/run linked;
- Terminal-Bench 2.1, Claude Opus-4.8 high: `80.22%` vs Claude Code `78.9%`, public run linked;
- Terminal-Bench 2.1, GPT-5.5: `84.3%` vs Codex CLI `83.1%`, public run linked;
- Terminal-Bench 2.1, Grok-4.5: `84.94%` after a reward-hack audit, submission linked;
- OSWorld-Verified: full-trace datasets are linked for Opus-5 and Sonnet-4.6;
- SWE-bench Pro matched pair: the README reports no significant difference between Ouroboros and Codex CLI for the cited GPT-5.6-luna run.

The public runs/traces improve inspectability, but this record does not relabel maintainer-reported results as independently reproduced.

## Unsupported or non-comparable claims

- Full-A status and S4/S5 closure provide no S1 capability credit here.
- Claudexor or a connected coding harness's own execution capability is not Ouroboros-native.
- Independent S3* reviewer presence is not counted as S1 assurance; only the demonstrated effect of verification/acceptance on the root completion path is credited.
- Benchmark leadership claims are not generalized beyond the specific model/task evidence.
- Rich typed failure rails demonstrate mechanisms, not a measured recovery percentage against another cohort member.

## Primary evidence

- [`README.md`](https://github.com/razzant/ouroboros/blob/86806ee123ce8e26cc063cc1a618f975eea64f26/README.md)
- [`docs/architecture/06-agent-core.md`](https://github.com/razzant/ouroboros/blob/86806ee123ce8e26cc063cc1a618f975eea64f26/docs/architecture/06-agent-core.md)
- [`assets/bench-terminal-bench.svg`](https://github.com/razzant/ouroboros/blob/86806ee123ce8e26cc063cc1a618f975eea64f26/assets/bench-terminal-bench.svg)

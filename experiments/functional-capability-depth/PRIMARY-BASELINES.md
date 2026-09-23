# Primary benchmark baseline selection

Status: **experimental, non-normative**

Tracking issue: #409

This file applies [`BASELINE.md`](BASELINE.md) to the benchmark families currently reviewed under `functional-capability-depth`.

The rule for the baseline view is simple:

```text
1 VSM function -> 1 primary benchmark
```

A primary is selected only when the current evidence can support a matched comparison of canonical harness systems. A direct VSM benchmark is not enough by itself if the benchmark scaffold supplies the target organizational function or if the published comparison varies only models rather than harnesses.

The generated current S1 projection is [`S1-BASELINE.md`](S1-BASELINE.md). It is derived from this selection record plus raw S1 observations; do not maintain benchmark values manually in this file.

## Selection gate

A primary family should be:

1. **function-valid** — it measures the target VSM function rather than a nearby feature label;
2. **matched-harness** — model/configuration, tasks, environment, evaluator and resource policy can be held fixed while the harness varies;
3. **canonical-linkable** — benchmarked systems can be linked to canonical Index harnesses without importing the target function from the benchmark scaffold;
4. **frozen-repertoire compatible** — ordinary baseline runs do not silently mix persistent self-improvement across benchmark tasks into the same score;
5. **public and reproducible** — the protocol and provenance are sufficient to preserve observation identity;
6. **scope-honest** — narrow applied-domain results remain domain projections rather than universal capability claims.

## Current selection

| Function | Baseline status | Primary family | Reference cell | Reason |
| --- | --- | --- | --- | --- |
| S1 | selected | PawBench v1.0 | `qwen3.6-35b-a3b` × QwenPaw / OpenClaw / Hermes | general Model × Harness design with three canonical `S1=A` systems under one 150-task evaluation surface |
| S2 | gap | — | — | DPBench is direct S2 evidence, but the coordination organization is benchmark-scaffolded rather than a native canonical-harness comparison |
| S3 | gap | — | — | ClawArena-Team directly tests team management, but the benchmark supplies the management organization/tools and varies the main-agent model |
| S3* | gap | — | — | TrueCall directly tests a composed audit path, but the audit function is supplied by the external TrueCall layer |
| S4 | gap | — | — | direct S4 families currently evaluate benchmark-defined/composed adaptation loops rather than matched native S4 across canonical harnesses |
| S5 | gap | — | — | no reviewed direct S5 benchmark currently closes legitimate ultimate-policy/identity authority and return to operation |

A `gap` is deliberate. It means the current evidence is not strong enough for the simple primary baseline view; it does not mean the function lacks benchmark evidence.

## S1 — selected general primary

### PawBench v1.0

Primary source: <https://github.com/agentscope-ai/PawBench>

PawBench is explicitly organized as a **Model × Harness** co-evaluation benchmark. Its v1.0 matrix covers 150 tasks, nine models and three harnesses. The benchmark supports holding one model fixed and comparing harnesses over the same task/evaluation surface.

The first reference cell is:

```text
model: qwen3.6-35b-a3b
benchmark: PawBench v1.0
harnesses:
  - qwenpaw
  - openclaw
  - hermes-agent
```

All three harnesses are canonical Index systems and all three currently have `S1=A`.

Why this is the general S1 primary rather than a Coding/SWE benchmark:

- PawBench mixes multiple task sources and capability slices rather than restricting the comparison to repository issue resolution;
- it is explicitly designed to inspect model and harness effects independently;
- it can later accept more harness adapters without changing the conceptual baseline;
- its Docker/task isolation is compatible with the frozen-repertoire baseline rule, subject to preserving exact run configuration and any external persistent state in future observation records.

### Limits

The selection is a benchmark-family choice, not a claim that the published May 2026 rows evaluate current September 2026 canonical revisions.

Published PawBench harness versions are historical relative to the current Index review refs. Raw observations must therefore preserve:

- the published harness version/configuration;
- the relationship to the current canonical lineage;
- the fixed model and provider/configuration;
- PawBench version/task set;
- grading mode, including automated / LLM-judge / hybrid behavior;
- any known environment or persistence caveats.

Numeric benchmark results do **not** belong in this selection file. They belong in the shared raw observation layer.

## S1 / Coding-SWE domain projection

### Claw-SWE-Bench — selected domain primary

Primary source: <https://claw-swe-bench.github.io/>

Claw-SWE-Bench is the selected Coding/SWE primary because it explicitly elevates the harness to the controlled variable: model, 350 SWE tasks, Docker runtime and the official SWE-bench evaluator are held fixed while the harness varies.

The cheap reference cell is:

```text
model: Qwen 3.6-flash
scope: Coding / SWE
full task set: 350
```

The published five-harness matrix includes OpenClaw and Hermes Agent, both canonical Index systems with admitted matched-model observations under this domain projection.

This benchmark is **not** promoted to the general S1 primary because its task distribution is intentionally software-engineering specific.

### FrontierHarness Eval — additional Coding/SWE evidence

Primary source: <https://github.com/frontier-harness-eval/eval>

FrontierHarness Eval is additional high-value domain evidence because it fixes Kimi K3 and the runtime while comparing a broad harness set including canonical Index systems Codex, Claude Code, Pi, oh-my-pi, OpenCode and Hermes.

Its v1.0 task set contains 21 Terminal-Bench 2.1 tasks and 9 DeepSWE v1.1 tasks. It therefore remains in the existing technical/Coding-SWE projection rather than becoming the general S1 baseline.

It is especially useful for:

- broad canonical harness overlap;
- cost/cache/time measurements alongside pass rate;
- fresh-restore task isolation;
- robustness checks beside the selected domain-primary Claw-SWE cell.

## S2 — primary gap

Reviewed direct family: **DPBench**.

Primary source: <https://github.com/najmulhasan-code/dpbench>

DPBench directly measures coordination under simultaneous shared-resource contention and reports deadlock, throughput, fairness and message-action consistency.

It is not selected as the canonical-harness S2 primary because the benchmark defines the multi-agent organization and interaction protocol itself. Published experiments primarily compare models and protocol conditions inside that benchmark organization; they do not yet provide a matched comparison among canonical harnesses that natively own S2.

DPBench remains direct S2 benchmark-family evidence.

## S3 — primary gap

Reviewed direct family: **ClawArena-Team**.

Primary source: <https://github.com/aiming-lab/ClawArena/tree/main/ClawArena-Team>

ClawArena-Team cleanly tests whole-team management by holding a fixed subagent pool constant while a main agent creates, empowers, schedules, inspects and integrates subagents.

It is not selected as the canonical-harness S3 primary because the benchmark supplies the management tool surface, worker pool and organization. Published comparison therefore isolates the main model's management ability inside a benchmark-defined organization rather than comparing native S3 implementations of canonical harnesses.

ClawArena-Team remains direct S3 benchmark-family evidence.

## S3* — primary gap

Reviewed direct family: **TrueCall silent-failure runtime verification**.

Primary source: <https://github.com/abhid1234/truecall>

TrueCall provides a deterministic post-condition audit layer and corrective return path, including adapters around more than one harness. That makes the composed audited system a direct S3* benchmark boundary.

It is not selected as the canonical-harness S3* primary because TrueCall itself supplies the complementary audit function. A wrapped Codex or Claude Code run therefore cannot be interpreted as measuring that harness's native S3* capability.

TrueCall remains direct composed S3* evidence and may later support controlled studies of how different S1 systems respond to the same external audit signal.

## S4 — primary gap

Reviewed direct families include:

- A-Evolve harness evolution;
- SkillEvolBench;
- EvoHarnessBench self-evolving mode.

These are valuable direct S4 benchmarks at their declared benchmark-defined/composed adaptation boundaries. They currently do not provide a matched comparison among canonical harnesses that natively own S4.

### Frozen-repertoire rule for S4

The ordinary capability baseline asks how good the **current S4 regulator** is.

That does not forbid S4 from doing its ordinary job. An existing S4 mechanism may sense the environment, generate adaptation options and cause changes elsewhere in the organization during an S4 benchmark.

What the ordinary baseline must not silently add is persistent improvement of **S4's own decision/feedback repertoire** across benchmark tasks. That belongs to the separate experimental self-organizing `S` question.

So:

```text
S4 uses its current repertoire to adapt another function
-> ordinary S4 capability may be measured

S4 changes how S4 itself learns / senses / generates adaptation
and carries that new regulator forward
-> separate self-organizing evidence
```

## S5 — primary gap

No reviewed benchmark family currently satisfies the direct S5 gate for the primary baseline.

A qualifying direct S5 benchmark must reach more than policy enforcement or value-conflict reasoning. It must expose legitimate ultimate-policy/identity authority at the declared recursion, an actual adjudication/ratification/revision decision, and return the newly decided policy into subsequent operation.

Current reviewed families remain proxy or unsuitable under that standard.

## Replacement and expansion rule

Primary selection is not permanent.

A new benchmark may replace a primary when it offers materially stronger:

- function validity;
- canonical harness coverage;
- matched-model comparability;
- reproducibility;
- frozen-repertoire control;
- domain breadth for a general baseline.

Replacing a primary changes the derived baseline view. It does not delete historical observations or secondary/domain evidence.

## Current evidence state

The first selected cells are now present in the shared S1 observation layer:

1. PawBench v1.0 `qwen3.6-35b-a3b` × QwenPaw / OpenClaw / Hermes — general S1 primary;
2. Claw-SWE-Bench `Qwen 3.6-flash` × canonical OpenClaw / Hermes rows — Coding/SWE domain primary;
3. FrontierHarness Eval v1.0 Kimi K3 × canonical Codex / Claude Code / Pi / Oh My Pi / OpenCode / Hermes rows — additional Coding/SWE evidence.

Claw-SWE-Bench also contains an admitted GLM 5.1 matched-model robustness cell. It remains additional evidence and is not substituted for the selected cheap Qwen 3.6-flash domain-primary cell.

Each numeric result is stored once in `s1-system-benchmarks/observations.jsonl`. The generated [`S1-BASELINE.md`](S1-BASELINE.md) projects those observations according to `primary-baselines.json`; it must not become an independently edited evidence source.

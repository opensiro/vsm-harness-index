# Direct S1 system benchmark observations

Status: experimental, non-normative.

Issue: #382

Parent benchmark-family review: `../vsm-benchmark-family-map/`

Primary-baseline selection: `../PRIMARY-BASELINES.md`

## Purpose

This layer records published benchmark observations for canonical Index systems only when:

1. the benchmark family is already reviewed as `direct` for S1;
2. the benchmark actually exercised the system's own operational implementation with `native-system` or defensible `adapter-preserved` compatibility.

It does not infer S1 from benchmark performance. Canonical VSM assessment remains authoritative for function and ownership.

## Source of truth

`observations.jsonl` is the machine-readable source of truth.

Each row is an observation of a concrete configuration:

```text
(canonical system, historical/current harness version, model, benchmark, config, date)
```

not a timeless score for the project.

When benchmark prose, live UI and an immutable committed result artifact disagree, prefer the immutable result artifact and preserve the discrepancy explicitly rather than silently reconciling it.

## Admitted systems

Current observations cover:

- `codex`;
- `openhands`;
- `swe-agent`;
- `qwenpaw`;
- `openclaw`;
- `hermes-agent`.

All are canonical Index systems with S1 established independently by their assessments.

## Benchmark families

Only reviewed direct S1 families are admitted here:

- SWE-bench Verified;
- Terminal-Bench / Harbor;
- PawBench v1.0;
- Claw-SWE-Bench, scoped to Coding/SWE.

Other coding or agent benchmarks may be useful later, but they must first pass the benchmark-family semantic review or the primary-baseline selection rules rather than being added here by reputation or naming similarity.

## System compatibility

### `native-system`

The benchmark submission directly identifies and runs the first-party system without an external adapter materially controlling the system setup boundary. Exact historical revision may still be unknown.

### `adapter-preserved`

An external benchmark adapter controls environment/setup/evaluation, but the operational S1 loop remains the first-party harness.

Harbor's Codex and OpenHands installed-agent paths qualify because they invoke the actual first-party Codex CLI/OpenHands tool rather than replacing the agent loop.

PawBench's QwenPaw, OpenClaw and Hermes Agent rows also qualify here: PawBench controls container lifecycle, installation/configuration, model binding, task environment and grading, while the operational loop itself remains the corresponding first-party harness runtime.

Claw-SWE-Bench's OpenClaw and Hermes Agent rows use the same boundary: the benchmark controls the SWE task membrane, prompt, container/workspace, timeout, patch extraction and evaluator, while the first-party harness performs the operational work.

### Not admitted

`benchmark-scaffolded` observations are not system-level S1 evidence for a canonical harness. `unclear` observations remain candidates/rejections until the boundary is recoverable.

## PawBench general S1 baseline group

The selected first general S1 primary family is PawBench v1.0.

Immutable benchmark revision:

```text
agentscope-ai/PawBench@0f794a8bb6c27aa9ee4091b2691fa30e4ed9cc8f
```

Matched reference cell:

```text
run: pawbench-4models-opusjudge-20260529
model: qwen3.6-35b-a3b
tasks: 150

QwenPaw      0.6828
OpenClaw     0.6779
Hermes Agent 0.5674
```

The group is marked `matched-model` and `adapter-preserved`: the same PawBench v1.0 run/model label and task/evaluation surface are used while the preserved first-party harness loop varies.

Pinned adapter evidence identifies the historical harness versions:

- QwenPaw `1.1.3`;
- OpenClaw `2026.4.24`;
- Hermes Agent `2026.4.23`.

The exact upstream git revisions of those historical package versions are not imported by inference, so observation identity remains `version-known` rather than `exact-historical`.

### Frozen-repertoire compatibility

The benchmark runs harnesses in isolated task environments; the QwenPaw adapter explicitly documents one fresh container per task. This is compatible with the ordinary frozen-repertoire baseline rule: persistent learning from one benchmark task is not credited as part of the next task's baseline state.

This does not prohibit ordinary within-task reasoning, tool use, retry or recovery.

### Source discrepancy

For the OpenClaw row, PawBench README prose reports `68.2`, while the committed submission artifact reports:

```text
overall = 0.6779
```

and the live leaderboard rounds that artifact-backed value to `67.8`.

`observations.jsonl` therefore stores `0.6779`. The immutable committed submission is treated as the result source of truth; the README discrepancy is retained in the observation notes.

### Non-claims

PawBench exposes slices named `Planning`, `Self_Verification`, `Skill_Use`, `Workflow and Agent Orchestration` and similar capability labels. Those names must not be converted directly into VSM functions.

In particular:

- `Planning` does not establish S3;
- `Self_Verification` does not establish S3*;
- `Skill_Use` does not establish S4 or experimental self-organizing `S`;
- orchestration-labelled tasks do not establish S2/S3 ownership.

The imported rows are S1 system-performance evidence because canonical S1 has already been established independently.

## Claw-SWE-Bench Coding/SWE matched-model groups

Claw-SWE-Bench is a direct S1 family only for the Coding/SWE domain. It is therefore stored as a domain projection beside the general PawBench baseline, not as a replacement for universal S1 capability.

Immutable sources:

```text
TokenRhythm/claw-swe-bench@fcece5f4c0817430ce953b52c80c931a40cd9b83
claw-swe-bench/claw-swe-bench.github.io@191d0c62a0f72fb0bc1f0eb47b6f1e15950e725f
```

The committed leaderboard identifies the fixed-model section as `Same Model × Different Claws` and records the 350-task full-set results.

### Qwen 3.6-flash

```text
model: Qwen 3.6-flash
tasks: 350

OpenClaw     66.0%   231 / 350   $71.5    636.0 s
Hermes Agent 62.6%   219 / 350   $103.3   638.6 s
```

### GLM 5.1

```text
model: GLM 5.1
tasks: 350

OpenClaw     73.4%   257 / 350   $277.0   586.8 s
Hermes Agent 71.1%   249 / 350   $330.6   675.1 s
```

Both groups are stored as:

```text
comparison.mode: matched-model
comparison.scope: coding-swe
system_compatibility: adapter-preserved
```

The benchmark implementation holds the task set, prompting contract, Docker/workspace membrane, standard timeout, runner-side patch collection and official SWE-bench evaluator fixed while the harness varies. Each instance starts in a fresh container, and OpenClaw additionally receives a throwaway agent per instance.

The pinned sources do not establish exact historical OpenClaw or Hermes Agent upstream versions/revisions for these runs. Those fields remain `null`, with `revision_match: unknown`; current canonical `assessment_ref` is used only as the lineage anchor.

The two model cells are robustness evidence for the same applied domain. They must not be averaged into a composite score or used to claim an overall harness ranking.

### Coding/SWE non-claims

- Coding/SWE performance is not universal S1 capability.
- A test, review, planning, recovery or tooling step inside a coding task does not establish S3*, S3, S4 or another VSM function by vocabulary association.
- Fresh-container evaluation does not establish or test experimental self-organizing `S`; it intentionally prevents persistent cross-task adaptation from contaminating the ordinary baseline.
- These scores do not determine `A/C/P/—/?` ownership states.

## Previous SWE-bench comparison group

The earlier cross-system comparison is:

```text
SWE-bench Verified, 500 tasks
model: claude-4-sonnet-20250514

OpenHands  → 70.4% resolved
SWE-agent  → current official leaderboard: 66.6% resolved
```

Both submissions are marked `checked: true`, `os_system: true`, and use one attempt per task. The exact OpenHands historical commit is published; the SWE-agent submission identifies `SWE-agent 1.0` and a concrete config but does not publish an exact git revision.

The pair therefore remains `partially-matched`, not `matched-model`: the model and benchmark match, but complete harness/configuration equivalence cannot be established.

There is also a source discrepancy for SWE-agent: its submission README records an internal `345/500 = 69%`, while the current official leaderboard displays `66.6%`. `observations.jsonl` uses the current official leaderboard value and preserves the README value as an unresolved discrepancy rather than silently choosing a causal interpretation.

## Harbor parity evidence

Harbor's SWE-bench Verified parity data provides strong adapter-boundary checks:

- `codex@0.2.0` + `o4-mini`: 53.11 reference and 53.11 adapted result;
- historical OpenHands commit `c677f7284ee6e1e80ece4fe63a470912325cfe6a` + Claude 4 Sonnet: 66.8 reference and 67.0 adapted result.

These are valuable because parity directly tests whether the external execution membrane materially changed the benchmark outcome. They remain historical S1 evidence; they are not scores for the current canonical assessment revisions.

## Terminal-Bench evidence

Two public Terminal-Bench 4.0.0 Codex jobs are included:

- GPT-5.6 Sol / Codex: average reward 0.37 across 330 finished trials;
- GPT-5.6 Terra / Codex: average reward 0.22 across 330 finished trials.

The exact Codex CLI version used by those public jobs was not recovered, so revision matching remains `unknown`. They are useful descriptive evidence and a within-harness model-sensitivity example, not a cross-system harness comparison.

## Comparison modes

- `matched-model`: same benchmark/variant and sufficiently matched model/configuration across systems;
- `partially-matched`: important matching dimensions exist, but configuration/revision differences remain;
- `descriptive-only`: valid system observation but not a defensible cross-system system-effect comparison.

Raw metrics from different benchmark families must never be normalized into a single S1 score.

## Relationship to feature evidence

This experiment intentionally stops before explaining *why* one system differs from another.

```text
canonical S1 + ownership
        ↓
feature/mechanism evidence ──┐
                            ├── later capability synthesis
benchmark observations ─────┘
```

Retry, planner, verifier, context management, delegation, tool routing, memory and similar mechanisms remain separate repository-grounded evidence until a later attribution experiment.

## Rejections / gaps

See `REJECTIONS.md` for observations that were inspected but not admitted or not promoted into a stronger comparison class.

## Mutation boundary

Nothing here changes canonical assessments, autonomy states, catalog data, TLDR/rankings, Profile semantics or Skills methodology.

# Direct S1 system benchmark observations

Status: experimental, non-normative.

Issue: #382

Parent benchmark-family review: `../vsm-benchmark-family-map/`

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

## Initial admitted systems

The first pass admits observations for:

- `codex`;
- `openhands`;
- `swe-agent`.

All three are canonical Index systems with S1 established independently by their assessments.

## Benchmark families

Only reviewed direct S1 families are admitted here:

- SWE-bench Verified;
- Terminal-Bench / Harbor.

Other coding or agent benchmarks may be useful later, but they must first pass the benchmark-family semantic review rather than being added here by reputation or naming similarity.

## System compatibility

### `native-system`

The benchmark submission directly identifies and runs the first-party system. Exact historical revision may still be unknown.

### `adapter-preserved`

An external benchmark adapter controls environment/setup/evaluation, but the operational S1 loop remains the first-party harness. Harbor's Codex and OpenHands installed-agent paths qualify because they invoke the actual first-party Codex CLI/OpenHands tool rather than replacing the agent loop.

### Not admitted

`benchmark-scaffolded` observations are not system-level S1 evidence for a canonical harness. `unclear` observations remain candidates/rejections until the boundary is recoverable.

## First comparison group

The strongest initial cross-system comparison is:

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

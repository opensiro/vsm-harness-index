# Grit — S2 public-evidence review

Status: **admit direct family; do not admit observation**

Repository: `rtk-ai/grit`  
Reviewed revision: `0f3c9d04abe9525b1884f3a0ade890e54a6d9ffe`

## Decision

Grit qualifies as a **direct S2 disturbance/attenuation family at its own first-party product boundary**.

The relevant organization is not inferred from the product's use of the word coordination. The first-party system owns a concrete inter-worker regulation path:

```text
parallel coding workers
→ concurrent edits against one shared repository
→ merge / shared-symbol contention
→ Grit claim + symbol-level locking + isolated worktrees + serialized merge
→ conflicting work is blocked / isolated before destructive integration
→ later work returns to the shared repository through the regulated merge path
```

This is S2-shaped variety attenuation: otherwise useful parallel S1 activity creates interaction-specific merge contention, and the product supplies a recurring relation that constrains that interaction before return to the common codebase.

## Public benchmark surface

The pinned repository includes first-party benchmark scripts for:

- synthetic merge-conflict stress;
- throughput sweeps over multiple agent counts/projects;
- real Claude/Gemini agent runs;
- raw-git versus Grit comparison.

The throughput benchmark explicitly branches raw-git workers from one baseline, attempts later sequential merges, records conflicts/lost work, and compares that with workers using the first-party `grit claim` → isolated worktree → `grit done` path.

The repository also commits `tests/gen_graph.py`, which contains per-iteration benchmark counts used to generate the published result graphic. For the embedded 5-iteration × 5-round series, raw-git failures are recorded across worker-count levels while the plotted Grit failure series is zero.

These artifacts are enough to classify the family as direct S2 evidence at the Grit product boundary.

## Why no observation is admitted

The benchmark scripts write timestamped run outputs under `scripts/*/results/`, and the repository explicitly ignores those directories via `scripts/.gitignore`.

Therefore the public repository does **not** preserve the original immutable run ledger that produced the summary/graph. `tests/gen_graph.py` preserves per-iteration numbers, but it is a derived committed artifact rather than the underlying timestamped run outputs.

This is the same provenance principle already applied to CooperBench: a committed report or summary can establish a direct benchmark family while still failing the stricter observation-admission gate when the run artifacts it summarizes are not pinned.

Accordingly:

- no new row is added to `observations.json`;
- no causal effect size is admitted;
- no exact runtime/environment/model provenance is invented;
- the README's aggregate tables are not silently treated as raw observations.

## System boundary

Grit is a public first-party coordination substrate for parallel coding agents, but it is not currently a canonical VSM Harness Index system.

Therefore:

- `canonical_harness_id = null`;
- no autonomy state is inferred;
- system compatibility is `native-system` at the external Grit product boundary;
- canonical direct S2 observation count remains unchanged.

## Effect on S2 depth

Grit adds:

- one direct S2 family;
- one external native-product coverage case.

It does **not** add:

- a direct observation registry row;
- a canonical native S2 observation;
- a matched cross-harness primary cell;
- a scalar S2 score.

The S2 primary remains `gap`.

## Primary sources

- `https://github.com/rtk-ai/grit/tree/0f3c9d04abe9525b1884f3a0ade890e54a6d9ffe`
- `https://github.com/rtk-ai/grit/blob/0f3c9d04abe9525b1884f3a0ade890e54a6d9ffe/README.md`
- `https://github.com/rtk-ai/grit/blob/0f3c9d04abe9525b1884f3a0ade890e54a6d9ffe/scripts/README.md`
- `https://github.com/rtk-ai/grit/blob/0f3c9d04abe9525b1884f3a0ade890e54a6d9ffe/scripts/throughput/bench.sh`
- `https://github.com/rtk-ai/grit/blob/0f3c9d04abe9525b1884f3a0ade890e54a6d9ffe/scripts/.gitignore`
- `https://github.com/rtk-ai/grit/blob/0f3c9d04abe9525b1884f3a0ade890e54a6d9ffe/tests/gen_graph.py`

# Grit public S2 evidence review

Status: **reviewed candidate — no admitted observation**

Tracking issue: #619  
Source: `rtk-ai/grit@0f3c9d04abe9525b1884f3a0ade890e54a6d9ffe`

## Functional fit

Grit is a first-party coordination substrate for parallel coding agents. Its public product path owns symbol-level claims/locks, contested-symbol queues, isolated worktrees, serialized merge, and release.

That gives the public benchmark design a plausible direct S2 shape:

```text
parallel coding workers
        ↓
shared-code contention / conflicting concurrent edits
        ↓
Grit claim + lock + queue + worktree + merge relation
        ↓
contested work is blocked/queued and merge activity is serialized
        ↓
subsequent worker operation changes
```

This is stronger S2 semantics than a generic teamwork or throughput benchmark. The blocker is **result provenance and comparison design**, not lack of a coordination mechanism.

## Public result surfaces reviewed

The repository README publishes first-party tables comparing raw git with Grit across agent counts up to 50 and reports zero merge failures for Grit in the shown sweeps.

The repository also commits the benchmark implementations:

- `scripts/synthetic/bench.sh` — synthetic merge-contention stress test;
- `scripts/throughput/bench.sh` — feature-throughput comparison;
- `scripts/ai-agents/bench.sh` — real Claude/Gemini workers coordinated through Grit;
- `scripts/README.md` — benchmark usage and result-directory contract.

These are useful primary sources for what the benchmark is intended to measure. They are not sufficient to admit the README summary as an immutable observation.

## Why no observation is admitted

### 1. Raw run artifacts are not committed

`scripts/README.md` says each run creates timestamped result directories containing agent logs and CSV summaries. But `scripts/.gitignore` contains:

```text
*/results/
```

So the raw result corpus underlying the published README tables is absent from the pinned repository revision. The tables are public first-party claims, but the individual runs, seeds/assignments, logs, and CSV rows cannot be independently recovered from the reviewed commit.

### 2. Synthetic control is deliberately confounded

The raw-git arm in `scripts/synthetic/bench.sh` adds a file-level header to every modified file and explicitly states that this **guarantees conflicts** when multiple branches modify the same file from one base.

The Grit arm does not run the same edit assignment under a single changed coordination relation. It obtains a separate shuffled symbol list, partitions those symbols among agents, and uses Grit claims/worktrees.

Therefore:

```text
raw git vs Grit
```

is not equivalent to:

```text
same workers + same edits + same disturbance
with only the S2 relation varied
```

The reported delta cannot be attributed solely to Grit's coordination mechanism.

### 3. Throughput arms also use independent allocations

`throughput/bench.sh` separately selects/partitions symbols for the raw-git and Grit arms. Its feature implementation also adds file-level headers/import-like edits, increasing line-level contention.

The benchmark is informative product testing, but it does not satisfy the experiment's materially matched comparison rule.

### 4. Real-agent benchmark has no matched control

`scripts/ai-agents/bench.sh` does exercise real Claude or Gemini workers through Grit and records conflicts/merges. However, at the reviewed revision it is a Grit-only treatment surface; it does not publish a matched no-Grit real-agent arm.

Its logs and summary CSV are also written beneath the ignored results directory.

## Boundary classification

Grit is not currently a canonical Index harness/system boundary. It is reviewed here as a **first-party coordination substrate**, not silently promoted into the canonical harness corpus.

Accordingly this review does not create:

- a canonical S2 observation;
- a new canonical harness id;
- a primary S2 baseline;
- a new direct-family count;
- an `observations.json` row.

Current S2 evidence counts remain unchanged.

## Disposition

```text
benchmark fit:          candidate-direct
source class:           first-party-reported
boundary:               non-canonical coordination substrate
family promotion:       no
observation admission:  no
primary baseline:       gap
```

The candidate can be reopened if Grit publishes immutable raw result artifacts tied to an exact revision and a materially matched public control where workload/edit assignment is held constant while the Grit coordination relation is the intended varying factor.

This is a fail-closed provenance decision, not a claim that Grit lacks coordination capability.

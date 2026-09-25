# Grit S2 public-evidence review

Status: **reviewed candidate; not admitted**  
Tracking issue: #651  
Function: `S2`  
Reviewed repository: `rtk-ai/grit`  
Reviewed revision: `0f3c9d04abe9525b1884f3a0ade890e54a6d9ffe`

## Disposition

Grit exposes a first-party coordination substrate with direct S2 semantics, but the currently published benchmark evidence is not admitted into the counted direct-family set or `observations.json`.

This is a provenance/comparison-quality decision, not a claim that the product lacks S2-relevant capability.

## Functional mapping

The product path is directly S2-shaped at the Grit product boundary:

```text
parallel workers on one codebase
        ↓
competing or overlapping edit / integration variety
        ↓
claim + lock + queue + isolated worktree + serialized merge
        ↓
conflicting work is blocked / serialized
        ↓
workers return to continued operation on a coordinated repository state
```

Primary product evidence at the reviewed revision includes:

- `README.md` — describes Grit as a coordination layer for parallel AI agents and publishes benchmark summary tables;
- `scripts/synthetic/bench.sh` — synthetic raw-git versus Grit conflict stress test;
- `scripts/sweep/bench.sh` — multi-count/project synthetic sweep;
- `scripts/ai-agents/bench.sh` — first-party live Claude/Gemini agent path using Grit claims and merges;
- `scripts/README.md` — describes benchmark output artifacts.

The organizational function is therefore not inferred from the word "coordination" alone. The first-party mechanism actually attenuates interaction variety among concurrent workers through admission/locking/queueing and controlled integration.

## Why the published benchmark is not admitted

### 1. Raw result artifacts are not committed

The scripts write timestamped CSV/log result directories, while `scripts/.gitignore` excludes:

```text
*/results/
```

The reviewed repository therefore preserves benchmark code and summary prose, but not the raw per-run corpus behind the README tables.

No release asset reviewed for this revision supplies the missing benchmark result corpus.

### 2. The synthetic comparison is asymmetric

`scripts/synthetic/bench.sh` explicitly adds a shared file header to each raw-git agent branch and comments that this **guarantees conflicts**. The Grit arm does not receive the same injected header disturbance.

This makes the published raw-git-versus-Grit failure-rate contrast unsuitable as a matched causal coordination ablation.

### 3. The sweep does not keep task assignment identical across arms

`scripts/sweep/bench.sh` constructs the raw-git and Grit workloads through separate randomized symbol orderings and different allocation logic. The two arms therefore do not preserve an identical worker-task assignment cell.

The sweep remains useful product stress evidence, but not a sufficiently matched comparison for admission into the current direct observation layer.

### 4. The real-agent path has no uncoordinated control

`scripts/ai-agents/bench.sh` launches Claude or Gemini workers with explicit instructions to use Grit. It records merges, conflicts, locks and queue state, but it does not publish a corresponding same-task/same-model no-Grit arm.

That path can support descriptive mechanism evidence if immutable run artifacts become public, but the current repository does not preserve those result directories.

## Relationship to the current S2 evidence layer

No current experimental counts change:

```text
direct benchmark families:        7
direct observations:              3
canonical direct observations:    0
native proxy projections:         2
primary baseline:                 gap
```

Grit is not a canonical Index harness and this review does not create a canonical identity or autonomy state.

## Reopen conditions

Re-review Grit for counted direct-family / observation admission if public upstream evidence adds at least one of:

1. an immutable committed or release-hosted raw benchmark result corpus tied to an exact Grit revision and exact benchmark configuration;
2. a matched raw-git-versus-Grit experiment that preserves the same worker tasks, disturbance injection, project state, agent count and repetition policy in both arms;
3. a first-party live-agent result corpus with exact model/configuration provenance and a matched uncoordinated control;
4. an independent third-party result exercising Grit's first-party coordination path under an explicit inter-S1 disturbance.

Do not reopen merely for another README summary table without recoverable run provenance.

## Non-claims

- This review is not a zero S2 capability score.
- It does not claim the README results are false.
- It does not run or reproduce Grit benchmarks.
- It does not modify `observations.json`, canonical assessments, rankings or primary baselines.
- It does not infer that Grit is an in-scope canonical harness merely because it provides an agent coordination layer.

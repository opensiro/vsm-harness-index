# S2 primary-search closure

Status: experimental, non-normative.  
Tracking issue: #564  
Current-state update: #586  
Canonical delta review: #592  
Benchmark-family review: #622  
Scope: current public evidence reviewed through 2026-09-25.

## Result

```text
direct S2 benchmark families               5
direct S2 observations                     1
canonical native direct S2 observations    0
canonical native S2 quantitative proxies   2
matched canonical-native S2 primary        not available
S2 primary baseline                        gap
```

This closes the current public-evidence search transaction, not the possibility of future matched S2 evidence.

## Direct benchmark evidence

Five reviewed families directly exercise S2-shaped disturbance/attenuation relations at benchmark- or product-defined boundaries:

- **DPBench** — simultaneous shared-resource contention and coordination failure;
- **STALE** — semantic interference among individually-correct parallel patches, with controlled communication conditions that attenuate the interference;
- **Nool fleet coordination** — concurrent coding workers contend on one shared codebase while pre-start footprint gating is enabled or removed under a controlled same-model/same-workload experiment;
- **Twining Benchmark conflict-resolution** — two implementers deliberately introduce incompatible architectural choices and a third resolver must detect the conflict and unify the shared codebase;
- **Grit parallel-agent merge-contention** — parallel coding workers branch from shared repository state while first-party claims/queues/worktrees/serialized integration attenuate merge-contention interference.

These direct-family classifications do not by themselves establish canonical harness S2 ownership. Nool supplies the one admitted direct non-canonical observation. Twining does not add another observation because its committed result does not recover the exact Twining MCP/plugin treatment revision. Grit does not add another observation because its run-level benchmark result directories are intentionally gitignored and it is not an admitted canonical Index harness.

## Direct non-canonical observation — Nool Track D

Pinned benchmark revision:

```text
noolinc/nool_long_eval_bench
126d69b5921be71daffd38c70ec4aa77252b4f39
```

The pre-registered Track D scale-up creates three explicit contention clusters inside a 20-ticket shared-codebase workload and runs N=10 coding workers. Prompts, model (`claude-sonnet-5`), worker count and worktree isolation are held fixed. The changed relation is whether overlapping tickets are allowed to start blind or are held until the prior overlapping ticket has integrated.

The primary comparison reported in the committed findings and replication manifest is:

| Arm | Run | Accepted | Clean merges | Final main |
| --- | --- | ---: | ---: | --- |
| uncoordinated git | `fleet_git_fleet_9a6eb70f` | 1/20 | 14/20 | broken |
| uncoordinated git | `fleet_git_fleet_803f2288` | 13/20 | 13/20 | green |
| coordinated | `fleet_nool_fleet_cb7ccf72` | 19/20 | 20/20 | green |
| coordinated | `fleet_nool_fleet_2a51582f` | 19/20 | 20/20 | green |

Every conflict in the two primary uncoordinated runs occurs on the second or third member of a designed contention cluster. In the coordinated arm, same-footprint work is delayed until the previous overlapping ticket is integrated, so later work begins from changed shared state rather than racing from the stale base.

A known gate-hole run (`fleet_nool_fleet_16e2e1b0`) is retained in the raw ledger and explicitly excluded from the primary comparison. The benchmark later reports that a git-only scheduler using the same pre-start check-in relation can match the coordinated arm when declared footprints are accurate. That control is important: the direct S2 claim is about **attenuating inter-worker interference**, not about the Nool product name.

Raw provenance remains in the benchmark repository:

```text
results/trackc/fleet_runs.jsonl
results/replications/MANIFEST.md
docs/findings/2026-08-21-findings.md
```

The public repository is the benchmark/evidence package. It does not expose a canonical open-source Nool runtime assessment boundary, so the observation is recorded as direct **non-canonical** S2 evidence.

## Direct family without admitted observation — Twining

Pinned benchmark review revision:

```text
daveangulo/twining-benchmark
b6a4d5e5890c5617376ba5c8fb7a628014296663
```

The conflict-resolution scenario creates a concrete architectural disturbance: Agent A implements event-driven notifications while Agent B implements direct service calls. Agent C must detect the incompatible patterns, choose one, unify the codebase, preserve tests and document the decision. Conflict detection, resolution quality and decision documentation are scored separately.

A completed committed result exists for run `66312b64-0422-40c4-883f-4e16060b9977`, with benchmark harness commit `63004a1f7697c64a78bc9c83b6cafd461887bc75`. However, saved metadata records an empty `twiningMcpVersion`. At the pinned harness ref, full Twining invokes bare `npx -y twining-mcp` and can resolve a user-installed Claude plugin path, so the exact treatment revision used by the result is not recoverable.

The result therefore does not enter `observations.json` under the existing provenance gate. `twining-mcp` is also not promoted into the canonical Index merely to create canonical linkage.

## Direct family without admitted observation — Grit

Pinned repository revision:

```text
rtk-ai/grit
0f3c9d04abe9525b1884f3a0ade890e54a6d9ffe
```

Grit owns a first-party coordination relation for parallel coding workers: symbol-level claims and queues attenuate overlapping work before execution, per-agent worktrees isolate concurrent mutation, and serialized integration attenuates merge races on return. The repository includes synthetic, throughput, sweep, and real-agent benchmark scripts, and immutable commit `a2c48735e0a16c49ca1541c4865fce438c479405` records first-party benchmark summary claims.

That is sufficient to classify the benchmark family as direct S2 at the Grit product-defined coordination boundary. It is not sufficient for an observation registry row. `scripts/.gitignore` explicitly excludes `*/results/`, while `scripts/README.md` says those run directories contain the raw logs and CSV summaries. The run-level ledgers needed by the current observation-provenance gate are therefore not public in the pinned repository.

Grit is also not an admitted canonical Index harness. No `observation_ref` or canonical S2 attribution is created by this review.

## Native quantitative evidence

Two canonical systems have useful native quantitative proxy evidence:

- **AutoGen / Magentic-One** — native orchestrator ablations change task performance, but the ablation spans S2 and S3 mechanisms and the task set does not instantiate an explicit S2 disturbance;
- **Squad / MARBLE** — same-model/same-task factorial coordination ablations exercise canonical Squad's native coordination path, but published outcomes are broad collaborative completion/quality rather than a measured inter-S1 disturbance and its attenuation.

These are real capability observations, but promoting them to direct S2 would change the functional criterion after seeing the data.

## Other reviewed routes

### Matched framework campaigns

Astra and Agent Framework Benchmark provide useful matched framework/runtime comparisons. Their organizations are benchmark-authored and/or deliberately sequentialize work, so recurring inter-S1 interference is absent or not isolated.

### Native mechanism without direct result

DeepSeek Agent Teams exposes a canonical native S2 path, but the public benchmark entry point does not exercise that path directly. C.A.D.I.S. and ARES were separately re-reviewed after their canonical admission in #592; their public result surfaces still do not provide direct native inter-S1 disturbance-to-attenuation observations.

### MAO-Bench

MAO-Bench is structurally promising: parallel/sequential tiers, adversarial failure/conflict tasks, topology metrics and an adapter interface. Its public seeded leaderboard does not yet contain multi-orchestrator baseline results, so no matched canonical cell exists to admit.

## Why the gap is evidence-backed

The evidence separates four layers that should not be conflated:

```text
benchmark directly measures S2 disturbance/attenuation
        but may lack observation-grade provenance

benchmark publishes an immutable direct result
        but the measured organization is not canonical

canonical harness runs its native coordination path
        but published metric is only a broad proxy

matched canonical native S2 comparison
        still absent
```

A primary requires the fourth layer, not merely more evidence in the first three.

The coverage record inspects 13 representative canonical S2 systems across shared-resource contention, write collisions, semantic staleness, team-loop interference and host-resource admission mechanisms. The absence of a direct native result is therefore a reviewed empirical gap, not an unsearched placeholder.

## Reopen rule

Reopen when new public primary evidence supplies at least one of:

1. a canonical S2 system measured on an explicit native disturbance → attenuation protocol;
2. a common benchmark with two or more canonical systems exercising their native/adapter-preserved S2 paths under the same disturbance definition;
3. published MAO-Bench or equivalent multi-orchestrator rows with immutable system/model/configuration provenance and direct S2 semantics.

Do not reopen merely for another benchmark-scaffolded or non-canonical direct family without canonical linkage, another team-success score, topology comparison, communication-count metric or framework throughput benchmark without explicit native S2 closure.

## Consequence

```text
S2 primary baseline = gap
```

This is an evidence state, not a zero score and not a statement that canonical S2 systems lack coordination capability.

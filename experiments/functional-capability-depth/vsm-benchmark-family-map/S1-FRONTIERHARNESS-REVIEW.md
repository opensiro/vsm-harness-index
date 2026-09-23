# FrontierHarness Eval — S1 applied-domain review

Status: experimental, non-normative.

Tracking issue: #419

Reviewed source:

```text
frontier-harness-eval/eval@e837a70bd6beb4e72eeeda62dd06e3bd34f6cb63
```

## Result

```text
function: S1
fit: direct
domain_scope: coding-swe
system_linkage: observation-specific
```

The `coding-swe` projection is retained because `../primary-baselines.json` already places FrontierHarness Eval there as additional evidence. The benchmark itself is broader than pure software engineering: 21 of 30 tasks come from Terminal-Bench 2.1 and 9 come from DeepSWE v1.1. Results therefore describe this mixed technical terminal/SWE task distribution, not universal S1 capability.

## Benchmark boundary

`benchmark.json` freezes FrontierHarness Eval v1 with:

```text
model: Kimi K3
model provider: Fireworks
tasks: 30
  Terminal-Bench 2.1: 21
  DeepSWE v1.1: 9
harnesses: 9
configurations: 12
evaluations: 360
canonical selection: first valid attempt 1
```

The evaluated harness receives an executable technical task and performs the primary transformation through its operational loop. Success is determined from task execution rather than from the presence of planning, review, delegation, tool-use or other vocabulary.

This is direct S1 at the benchmark boundary because the benchmark asks the harness to do the operational work and grades the resulting environment/task outcome.

## Matched-harness design

The historical published baseline fixes Kimi K3 and the task set while changing the harness/configuration.

The repository states that, for each task, harnesses and the task environment are prepared once as a golden checkpoint and every run starts from a fresh restore with identical vCPU, memory, disk size, disk contents and memory state.

That design is compatible with a matched-model harness comparison and with the ordinary frozen-repertoire baseline rule: persistent changes from one task do not become the starting repertoire for later tasks.

Fresh restore does not itself establish experimental self-organizing `S`.

## Public artifacts

The pinned repository publishes:

- `benchmark.json` — frozen benchmark definition;
- `metadata/harness-versions.json` — historical harness versions/revisions where recovered;
- `results/eval-data.json` — aggregate and task-level normalized results;
- task prompts and public task metadata;
- an evaluation/reproduction workflow.

The published results include pass rate, cost, cache behavior, duration and task-level outcomes.

## System linkage

Benchmark-family fit and canonical-system attribution remain separate.

A displayed harness row can be linked to an Index system only after repository/version identity and the adapter boundary are independently checked. Expected compatible rows are normally `adapter-preserved`: FrontierHarness supplies the external runtime/evaluation membrane while the first-party harness retains its operational loop.

A matching display name alone is insufficient.

## Historical reproduction limits

The current repository explicitly records an important limitation: the published baseline did not preserve its applied egress allowlist. New runs therefore default to `methodology_comparable: false`, and a matched control run is required before claiming that a new run is comparable with the historical baseline.

This does not invalidate comparisons among the already-published historical baseline rows, which were produced inside the same frozen evaluation campaign. It limits later reproduction and extension claims.

The DeepSWE definition also records a reproduction caveat: the published dataset label and the pinned reproduction ref use separate-verifier images that differ from the frozen public task metadata. Future reproduction evidence must preserve that distinction rather than silently treating the environments as identical.

## Function-first non-claims

FrontierHarness Eval does **not** establish:

- universal S1 capability outside its mixed technical terminal/SWE task distribution;
- S2 from multi-step interaction or coordination vocabulary;
- S3 from planning, control-flow or task-management behavior;
- S3* from tests, review or verification vocabulary;
- S4 from retry, replanning, context use or recovery inside a task;
- S5 from prompts, policy or permissions;
- experimental self-organizing `S` from ordinary task execution;
- any `A`, `C`, `P`, `—`, or `?` ownership state from benchmark performance.

The benchmark's own qualitative winner labels are also not OpenSiro conclusions. OpenSiro stores configuration-specific observations and matched comparison groups without turning them into an overall political-style or product-quality verdict.

## Admission consequence

FrontierHarness Eval adds a fourth reviewed direct S1 family, with the applied-domain scope above:

```text
S1  4
S2  1
S3  1
S3* 1
S4  3
S5  0
```

System-level rows, if admitted, belong in the shared S1 system-observation layer and require their own canonical identity/provenance review.
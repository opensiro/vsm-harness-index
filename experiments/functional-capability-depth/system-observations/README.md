# Shared system benchmark observations

Status: experimental, non-normative.

Issue introducing this layer: #403

## Purpose

Some published benchmark results are relevant to more than one VSM function-specific capability analysis. Raw benchmark metrics should not be copied independently into each function directory because that would create multiple manually maintained sources of truth.

This directory therefore stores **raw published system/configuration observations without assigning them a VSM score**.

Function-specific layers may reference observation IDs and interpret them independently:

```text
published system observation
        ↓
shared raw record
        ├── S2 proxy projection
        ├── S3 proxy projection
        └── other future function-specific projection
```

The raw layer answers:

```text
what system/configuration was run?
on what benchmark?
with what metric/result/provenance?
what ablation was performed?
```

It does **not** answer:

```text
which VSM function exists?
who owns it?
is the benchmark direct/proxy for a specific VSM function?
```

Those questions remain in canonical assessments and function-specific benchmark layers.

## Boundary requirements

Each raw record should preserve where possible:

- published system name/version/revision;
- relationship to a current canonical Index system;
- exact model/configuration;
- benchmark split and metric;
- confidence interval/replication information;
- publisher relation;
- raw ablation definition;
- revision/version mismatch between historical benchmarked system and current canonical assessment;
- primary-source provenance;
- explicit non-claims preventing causal over-interpretation.

A historical first-party result may be linked to a current canonical system lineage, but it must not be presented as if the current pinned assessment revision itself was benchmarked.

## Source-of-truth rule

A numeric result belongs in one raw observation record. Function-specific projection files should reference `observation_id` / `ablation_id` rather than copying benchmark metrics.

This layer is experimental infrastructure, not a second canonical assessment database and not a leaderboard.

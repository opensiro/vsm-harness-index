# Functional capability depth — migrated

Status: **migrated / historical pointer**

The active experimental capability corpus has moved to [`opensiro/vsm-harness-capability`](https://github.com/opensiro/vsm-harness-capability).

This path is retained only as a stable migration pointer. It is no longer an active evidence registry, benchmark/VSM interpretation surface, baseline source of truth, or CI-owned experiment in the VSM Harness Index.

## Migration boundary

The extraction was bootstrapped from this repository at pinned revision:

```text
3446fe77e031878dc8ad4edfb857b608a7a6b26f
```

The Capability repository preserves:

- the neutral public system-observation corpus;
- derived VSM-function projections;
- general-capability baselines and evidence frontier;
- predecessor checksums and source-ref provenance;
- predecessor experiment-specific tests as historical artifacts;
- Batch 01, Batch 02, LoopX and the frozen predecessor synthesis as historical artifacts.

The migrated corpus preserved **53 unique raw observation IDs** at extraction.

## Source-of-truth split

- VSM semantics → [`opensiro/vsm-harness-profile`](https://github.com/opensiro/vsm-harness-profile)
- assessment procedure → [`opensiro/vsm-harness-skills`](https://github.com/opensiro/vsm-harness-skills)
- canonical repository-relative assessments → this Index
- experimental general functional capability → [`opensiro/vsm-harness-capability`](https://github.com/opensiro/vsm-harness-capability)

Canonical Index assessments, catalog state, TLDR, rankings and autonomy states were not migrated and remain owned by this repository.

Capability remains **experimental and non-normative**. Its existence does not by itself change the bounded `vsm-oss-organization` system boundary.

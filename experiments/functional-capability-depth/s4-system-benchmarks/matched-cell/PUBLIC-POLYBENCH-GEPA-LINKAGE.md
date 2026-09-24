# Public PolyBench GEPA linkage refinement

Status: experimental, non-normative.  
Tracking issue: #551  
Refines: `PUBLIC-POLYBENCH-PAPER-CONTROLS.md`

## Question

Can the Adaptive Auto-Harness paper's `GEPA` PolyBench row be linked to an immutable native or adapter-preserved GEPA system strongly enough to enter a matched canonical S4 cell?

## Result

```text
paper-level matching                     satisfied
GEPA adapter identity                    satisfied
upstream GEPA project/API identity       satisfied
exact evaluated GEPA version/revision    BLOCKED
canonical GEPA S4 ownership              not reached
matched canonical S4 cell                not admitted
S4 primary baseline                      gap
```

This is stronger than the original #538 state, but it is still not enough for canonical capability attribution.

## What the pre-release tree establishes

The public A-Evolve pre-release revision:

```text
e4f70b949989e0abf08532e8223cb9eab447e971
```

contains `agent_evolve/algorithms/gepa/engine.py`.

That adapter does not locally recreate the full GEPA search algorithm. It imports:

```python
from gepa.optimize_anything import (
    EngineConfig,
    GEPAConfig,
    ReflectionConfig,
    optimize_anything,
)
```

and calls `optimize_anything()` directly. A-Evolve supplies the integration membrane around it:

```text
A-Evolve workspace
        ↓ serialize
GEPA candidate dict
        ↓
upstream optimize_anything()
        ↓ evaluate through A-Evolve TrialRunner
selected GEPA candidate
        ↓ restore
A-Evolve workspace
```

The accompanying first-party documentation describes the same relationship: `GEPAEngine` bridges A-Evolve workspace layers and TrialRunner into GEPA's public optimization API.

Primary evidence:

- `A-EVO-Lab/a-evolve@e4f70b.../agent_evolve/algorithms/gepa/engine.py`
- `A-EVO-Lab/a-evolve@e4f70b.../docs/algorithms/gepa.md`
- upstream `gepa-ai/gepa`

This closes the earlier ambiguity between a method-family label and a wholly benchmark-local reimplementation.

## Remaining blocker — immutable evaluated GEPA revision

The same pre-release tree declares only:

```text
gepa>=0.1.0
```

There is no exact package pin in `pyproject.toml`, and the inspected public comparison lineage does not expose a lock file or committed run metadata that identifies the exact GEPA package version or `gepa-ai/gepa` commit used for the reported PolyBench row.

Therefore:

```text
known adapter revision
    + known upstream project/API
    + common paper-level experiment membrane

    !=

immutable evaluated upstream GEPA revision
```

The reported GEPA row remains inadmissible as canonical-native or adapter-preserved GEPA capability evidence until primary evidence closes that binding.

## Why canonical S4 is still not inferred

GEPA clearly contains an adaptation/search mechanism. That does not by itself assign a VSM state.

A standalone Index assessment would still need to establish the declared system boundary, S1 admission, the S4 organizational function and its decision right independently from benchmark performance. No assessment or catalog entry is created by this refinement.

## Relation to the other PolyBench refinements

- #534 established the public cross-method candidate and the original provenance blocker.
- #538 established that the **paper-level experiment membrane is materially matched**: model policy, temperatures, chronological task stream, batch loop and result surface.
- #547 established canonical `Continual Harness` identity and `S4=A`, but its paper row still lacks evaluated implementation binding.
- #551 establishes the complementary GEPA result: an actual adapter-to-upstream implementation path is public, but its exact evaluated upstream version/revision is not pinned.

These are distinct failure modes and are kept separate.

## Admission rule

Do not add the GEPA PolyBench row to `canonical_observations.json` and do not select an S4 primary until all of the following are established:

1. exact evaluated upstream GEPA version or immutable revision;
2. independent canonical system assessment and S4 ownership;
3. proof that the reported row exercises that native/adapter-preserved S4 path under the already-reviewed common paper membrane;
4. ordinary-S4 regulator freeze at the evaluated boundary.

Until then:

```text
S4 primary baseline = gap
```

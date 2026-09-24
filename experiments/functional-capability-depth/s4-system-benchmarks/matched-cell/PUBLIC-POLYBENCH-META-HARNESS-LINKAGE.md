# Public PolyBench Meta-Harness linkage refinement

Status: experimental, non-normative.  
Tracking issue: #553  
Refines: `PUBLIC-POLYBENCH-PAPER-CONTROLS.md`

## Question

Can the Adaptive Auto-Harness paper's `Meta-Harness` PolyBench row be linked to the public upstream Meta-Harness system strongly enough to enter a matched canonical S4 cell?

## Result

```text
paper-level matching                       satisfied
Meta-Harness paper/method identity         satisfied
design correspondence                      satisfied
upstream/native implementation identity    BLOCKED
immutable evaluated upstream revision      not reached
canonical Meta-Harness S4 ownership        not reached
matched canonical S4 cell                  not admitted
S4 primary baseline                        gap
```

The important distinction is:

```text
implements the Meta-Harness paper design
        !=
runs the upstream Meta-Harness implementation
```

## Local PolyBench implementation

A-Evolve pre-release revision:

```text
e4f70b949989e0abf08532e8223cb9eab447e971
```

contains:

```text
agent_evolve/algorithms/meta_harness/engine.py
```

The file explicitly describes itself as implementing the Meta-Harness search framework (Lee et al., 2026). It includes recognizable design elements:

- an agentic proposer;
- a persistent archive of prior candidate source, scores and traces;
- multiple candidate proposals per cycle;
- candidate validation and evaluation;
- Pareto-aware selection;
- persistent selected mutations returned to the A-Evolve workspace.

This is strong **design correspondence**.

## Upstream/reference Meta-Harness

The paper is:

```text
Meta-Harness: End-to-End Optimization of Model Harnesses
arXiv:2603.28052
```

The public reference repository is:

```text
stanford-iris-lab/meta-harness
```

At inspected revision:

```text
0cbc31e97c9e6d24232d1dc754827c02e1ec415c
```

the experimental Harbor runtime exposes a `BaseAgent` outer loop with a bounded `evaluate_harness` tool. The outer model edits `/app/harness.py`, requests hidden-suite evaluation through the tool, receives reward/verifier evidence and iterates under a configured evaluation budget.

That is not the implementation surface used by A-Evolve's PolyBench comparison row.

## Blocking distinction

The A-Evolve implementation is its own `MetaHarnessEngine` built around:

```text
A-Evolve AgentWorkspace
A-Evolve TrialRunner
Claude Code CLI proposer
A-Evolve candidate archive
A-Evolve validation / leakage audit
A-Evolve Pareto selection
A-Evolve diff application
```

The inspected engine does not import or invoke `stanford-iris-lab/meta-harness`, nor does it vendor that runtime.

Therefore:

```text
same named method family
+ recognizable paper design
+ common PolyBench experiment membrane

!=

native / adapter-preserved upstream Meta-Harness execution
```

This is a stronger negative result than simple missing provenance: the available code establishes a benchmark-local implementation boundary.

## Canonical consequence

A future standalone assessment of `stanford-iris-lab/meta-harness` may be useful on its own merits. It would still be a separate system-in-focus and would **not** retroactively turn the A-Evolve paper row into native Meta-Harness capability evidence.

The reported row may remain useful as a matched **algorithm/design comparison** inside the Adaptive Auto-Harness paper, but not as a matched canonical-harness S4 cell.

## Relation to other PolyBench refinements

- #538 established the materially matched paper-level model/task/batch/metric membrane.
- #547 established canonical Continual Harness identity and `S4=A`, but its paper row lacks immutable implementation binding.
- #551 established that the GEPA row uses an adapter around the upstream GEPA package, but the exact evaluated GEPA package/revision is not pinned.
- #553 establishes a different failure mode for Meta-Harness: the public row implementation is a local design-faithful implementation rather than the upstream runtime.

These failure modes should not be collapsed.

## Admission rule

Do not add the PolyBench Meta-Harness row to `canonical_observations.json`, and do not select an S4 primary, unless new primary evidence demonstrates that the evaluated row actually exercised an independently reviewed canonical system's native or adapter-preserved S4 implementation.

Until then:

```text
S4 primary baseline = gap
```

# Public PolyBench SkillOS linkage refinement

Status: experimental, non-normative.  
Tracking issue: #555  
Refines: `PUBLIC-POLYBENCH-PAPER-CONTROLS.md`

## Question

Can the Adaptive Auto-Harness paper's `SkillOS` PolyBench row be linked to a public SkillOS implementation strongly enough to enter a matched canonical S4 cell?

## Result

```text
paper-level matching                       satisfied
SkillOS paper/method identity              satisfied
evaluated implementation identity          BLOCKED
immutable evaluated revision               not reached
canonical SkillOS S4 ownership             not reached
matched canonical S4 cell                  not admitted
S4 primary baseline                        gap
```

The important distinction is:

```text
paper cites SkillOS and reports a SkillOS row
        !=
public evidence identifies the implementation that produced that row
```

## Paper identity

Adaptive Auto-Harness identifies the baseline as:

```text
SkillOS: Learning Skill Curation for Self-Evolving Agents
Ouyang et al. (2026)
arXiv:2605.06614
```

The paper-level experiment membrane is already materially matched by #538/#539: common chronological task order, common PolyBench batch loop, Claude Sonnet 4.6 solver unless specified, Claude Opus 4.6 evolver, zero temperatures, and the common Accuracy / coverage-scaled Return result surface.

This establishes **method identity and comparison controls**, not implementation provenance.

## Public implementation search

The public AdaptiveHarness release at:

```text
c1ea7d60c009519f5c037f7db9d47e97063bb353
```

explicitly states in `agent_evolve/algorithms/__init__.py` that comparison baselines including:

```text
gepa
meta_harness
skillos
continual_harness
mas_adaptive_skill
```

are not shipped in the released version.

We also inspected the richer public A-Evolve pre-release revision:

```text
e4f70b949989e0abf08532e8223cb9eab447e971
```

Its recursive tree exposes recoverable GEPA and Meta-Harness implementations, but no `skillos` implementation path. Repository commit-history search likewise did not recover a SkillOS-producing implementation binding.

## Why third-party repositories do not close the gap

Public GitHub search surfaces repositories named SkillOS, including later independent reproductions of arXiv:2605.06614. Those are useful projects in their own right, but a reproduction or same-name repository cannot be substituted for the implementation used to generate Adaptive Auto-Harness Table 2.

The required evidence is first-party provenance that binds:

```text
reported SkillOS row
        ↓
actual evaluated implementation
        ↓
immutable repository/package revision
```

That binding is currently absent.

## Canonical consequence

A future standalone assessment of a first-party SkillOS implementation may establish S4 ownership for that repository-relative system. It would still not retroactively make the Adaptive Auto-Harness row native capability evidence unless the row is bound to that implementation/revision.

Therefore the reported SkillOS numbers remain useful as a matched **paper-level method comparison**, but not as a matched canonical-harness S4 observation.

## Relation to other PolyBench refinements

The current baseline rows fail for different reasons:

- **Continual Harness:** canonical identity and `S4=A` are established, but row → producing implementation/revision binding is missing.
- **GEPA:** a real adapter invokes upstream GEPA, but the exact evaluated GEPA version/revision is not pinned.
- **Meta-Harness:** a public local implementation follows the paper design but is not the upstream Meta-Harness runtime.
- **SkillOS:** the cited method identity is explicit, but the producing comparison implementation itself is absent from the inspected public artifacts.

These provenance failures must remain distinct.

## Admission rule

Do not add the PolyBench SkillOS row to `canonical_observations.json`, and do not select an S4 primary, unless new primary evidence establishes both the producing implementation identity and an immutable evaluated revision, followed by an independent canonical ownership review of that system.

Until then:

```text
S4 primary baseline = gap
```

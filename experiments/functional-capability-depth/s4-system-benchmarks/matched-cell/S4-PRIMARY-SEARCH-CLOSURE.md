# S4 primary-search closure

Status: experimental, non-normative.  
Tracking issue: #558  
Scope: current public evidence reviewed through 2026-09-24.

## Result

```text
canonical native S4 observations        available
matched paper-level S4 comparison       available
matched canonical-harness S4 primary    not available
S4 primary baseline                     gap
```

This closes the **current search transaction**, not the research question forever.

The evidence state is now strong enough to distinguish an actual public-evidence gap from an unreviewed TODO.

## Native evidence already available

Two canonical systems already have direct native S4 observations:

- `a-evolve` — first-party harness-evolution measurements across SWE-bench Verified, MCP-Atlas and SkillsBench;
- `kadath` — a ten-epoch locked-benchmark evolutionary run with persistent population improvement.

Those observations establish that canonical native S4 capability evidence exists. They do not form a matched cell because their tasks, benchmark definitions, models/configurations and result surfaces differ.

## Reviewed routes to a matched primary

### A-Evolve × Exo / SkillsBench

The first explicit matched-cell protocol established:

- independently canonical S4 ownership;
- a common persistent target (`skills`);
- first-party SkillsBench provenance.

It fails closed at the exact common model/provider gate: the pinned A-Evolve native SkillsBench solver is Strands + Bedrock, while the reviewed Exo native model route does not establish the same exact provider/model cell.

Disposition: **blocked common execution membrane**.

### Adaptive Auto-Harness / PolyBench

The paper provides the strongest public comparison membrane reviewed so far:

- common chronological PolyBench task stream;
- common batch loop and temporal-reveal policy;
- Claude Sonnet 4.6 solver unless specified;
- Claude Opus 4.6 evolver;
- zero solver/evolver temperatures;
- common Accuracy / coverage-scaled Return result surface.

That closes the paper-level matching question. The remaining failures are implementation provenance, and they differ by row.

#### Continual Harness

Canonical `continual-harness` independently establishes `S4=A`, but public evidence does not bind the paper row to the canonical upstream runtime or another immutable evaluated native/adapter-preserved implementation revision.

Disposition: **row → implementation binding blocked**.

#### GEPA

The public A-Evolve adapter genuinely calls the upstream `gepa.optimize_anything` API, so this is stronger than a method-name or local-paper imitation. The evaluated dependency is only constrained as `gepa>=0.1.0`; no lock/run artifact fixes the exact package version or upstream commit used for the reported row.

Disposition: **exact evaluated upstream revision blocked**.

#### Meta-Harness

The public PolyBench implementation is an A-Evolve-local `MetaHarnessEngine` that intentionally follows the Meta-Harness paper design, but does not invoke or vendor the public upstream Meta-Harness runtime.

Disposition: **upstream/native implementation identity blocked**.

#### SkillOS

The Adaptive Auto-Harness paper explicitly identifies SkillOS as Ouyang et al. (2026), but the released comparison implementation is omitted. The inspected richer pre-release tree also contains no SkillOS implementation path, and no immutable producing revision can be recovered from the inspected public lineage.

Disposition: **evaluated implementation identity blocked**.

## Why this is a valid negative result

The reviewed routes fail at different gates:

```text
common model/provider
implementation binding
exact upstream revision
native runtime identity
producing implementation identity
```

That diversity matters. It means the remaining gap is not one arbitrary requirement applied after seeing results; it is the consequence of the pre-existing primary-selection contract:

```text
function-valid
+ matched-harness
+ canonical-linkable
+ frozen-repertoire-compatible
+ public-reproducible
+ scope-honest
```

Weakening one gate merely to obtain a positive S4 primary would change the experiment after observing the evidence.

## Reopen rule

Reopen the S4 primary search when new **public primary evidence** materially changes one of the blocked gates, for example:

1. an immutable producing implementation/revision appears for an existing matched row;
2. a new public study evaluates at least two independently canonical-linkable S4 systems under one benchmark/model/configuration cell;
3. an adapter-preserved common execution membrane is established for existing canonical systems.

Do **not** reopen merely because another heterogeneous single-system result, benchmark-defined evolver, or method-name match appears.

## Consequence

```text
S4 primary baseline = gap
```

Here `gap` is an **evidence-backed empirical disposition**. It does not mean zero S4 capability, absence of S4 benchmarks, or absence of canonical native observations.

Future evidence can supersede this closure through a new reviewed transaction. Historical negative preflights remain part of the provenance trail.

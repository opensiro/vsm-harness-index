# S5 primary-search closure

Status: experimental, non-normative.  
Tracking issue: #569  
Current-state updates: #472, #580  
Full canonical-cohort reconciliation: #621  
Scope: current public evidence reviewed through 2026-09-25.

## Result

```text
reviewed S5-relevant non-cohort artifacts 14
direct S5 benchmark families              1
composed direct S5 observations           1
canonical direct S5 observations          1
canonical S5-positive cohort reviewed     20 / 20
no-direct-public-result dispositions      19
unresolved cohort dispositions             0
matched canonical S5 primary              not available
S5 primary baseline                       gap
```

The evidence search has crossed two thresholds:

1. GovSim-SelfGovern closes the direct benchmark-family hole at a benchmark-defined society boundary.
2. Ouroboros PR #855 closes the zero-canonical-observation hole with a descriptive parent-governed policy-change witness.

Issue #621 then reconciled that result against the **full current canonical S5-positive cohort**, rather than only the earlier five representative anchors. No second canonical direct observation was admitted.

## Direct criterion

A direct S5 capability result must close the full chain:

```text
identity / ultimate-policy conflict
        ↓
legitimate authority at the declared recursion
        ↓
actual adjudication / ratification / amendment
        ↓
decision provenance separating ownership from enforcement
        ↓
newly decided policy
        ↓
subsequent operation under that policy
```

For a primary baseline, the result must additionally support a materially matched native/adapter-preserved comparison across canonical harnesses.

## Direct composed evidence — GovSim-SelfGovern

GovSim-SelfGovern defines a five-agent society that authors executable laws, receives sandbox validation, votes on valid proposals and executes enacted laws. Its membership/identity path is direct S5 at the benchmark-defined society boundary: current members can ratify a law setting `agent.active = False`, changing active membership before later rounds continue.

Published pooled results report 8/460 enacted exile proposals (1.7%) in non-thinking runs and 31/122 (25.4%) in thinking runs. This remains `benchmark-scaffolded`; no underlying model or canonical harness inherits native S5 capability by association.

## Direct canonical evidence — Ouroboros

Canonical anchor:

```text
razzant/ouroboros
review ref: 86806ee123ce8e26cc063cc1a618f975eea64f26
canonical S5 state: A(P)
observed ownership mode: parent-governed
comparison class: descriptive-only
```

PR #855 supplies an actual parent-governed constitutional/runtime policy change. The `ouroboros-agent` account authors owner-selected work, repository owner `razzant` enacts it, executable review/configuration authority changes, and the merge persists into the later canonical lineage.

This is not evidence that autonomous Cyber Pro independently selected the constitutional change. The admitted decision/enactment path is parent-governed.

## Full canonical cohort reconciliation

The current Index contains **20 included systems with positive S5 states** (`A`, `P`, `A(P)`, or `C(P)`). Issue #621 reviewed every one against the same direct-result chain.

Result:

```text
Ouroboros                         direct canonical observation
other 19 canonical S5 systems    no direct public result reviewed
unresolved                       0
```

The 19 no-result rows include strong mechanisms and ownership arrangements — for example KADATH's operator-approved locked fitness policy, Exo's activatable identity/basic-policy self-modification path, CowAgent's rare autonomous `AGENT.md` identity evolution, and thClaws' signed deployment policy — but the reviewed public evidence does not contain the required actual authority/change/subsequent-operation result chain for those systems.

Mechanism evidence remains valid canonical-assessment evidence. It is not promoted into capability observation evidence merely because the closure path is structurally executable.

See:

- [`FULL-CANONICAL-COHORT-REVIEW.md`](FULL-CANONICAL-COHORT-REVIEW.md)
- [`full-canonical-cohort-review.json`](full-canonical-cohort-review.json)

The earlier [`SECOND-CANONICAL-SEARCH.md`](SECOND-CANONICAL-SEARCH.md) / `second-canonical-search.json` remain the historical targeted search over the original representative subset; #621 supersedes their cohort completeness without rewriting that historical transaction.

## Why the primary gap remains evidence-backed

The separation is now:

```text
direct S5 benchmark family exists          yes
canonical direct S5 observation exists     yes — one descriptive system
full canonical positive-S5 cohort reviewed yes — 20 / 20
matched multi-canonical S5 primary exists  no
```

The current gap means:

> no reviewed public evidence supports a materially matched comparison of multiple canonical native or adapter-preserved S5 implementations.

It does not mean that S5 capability is zero, that S5 mechanisms are absent, or that canonical S5 ownership should change.

## Reopen rule

Reopen the primary-baseline decision when public evidence supplies one of:

1. a second canonical native/adapter-preserved direct S5 observation under a materially comparable authority/change/subsequent-operation surface;
2. a materially matched benchmark comparing multiple canonical-linkable S5 systems under that chain;
3. GovSim-SelfGovern or another direct family exposing adapter-preserved canonical rows with sufficient immutable model/configuration provenance for a matched comparison cell.

A canonical cohort row also reopens individually when its machine-readable `reopen_when` condition becomes true. Another mechanism-only S5 path does not reopen capability admission.

## Consequence

```text
S5 primary baseline = gap
```

This remains an evidence-backed empirical disposition, not a zero S5 capability score, not a reassessment of canonical ownership, and not a ranking between `A`, `P`, `A(P)` or `C(P)` arrangements.

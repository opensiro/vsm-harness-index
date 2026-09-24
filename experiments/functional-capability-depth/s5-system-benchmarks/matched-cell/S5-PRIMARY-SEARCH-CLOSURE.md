# S5 primary-search closure

Status: experimental, non-normative.  
Tracking issue: #569  
Current-state updates: #472, #580  
Scope: current public evidence reviewed through 2026-09-25.

## Result

```text
reviewed S5-relevant artifacts           14
direct S5 benchmark families             1
composed direct S5 observations          1
canonical direct S5 observations         1
matched canonical S5 primary             not available
S5 primary baseline                      gap
```

The evidence search has now crossed two distinct thresholds:

1. GovSim-SelfGovern closes the direct benchmark-family hole at a benchmark-defined society boundary.
2. Ouroboros PR #855 closes the zero-canonical-observation hole with a descriptive parent-governed policy-change witness.

The matched canonical-primary hole remains open.

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

Primary source: `arXiv:2609.22600v1`.

GovSim-SelfGovern defines a five-agent society that authors executable laws, receives sandbox validation, votes on valid proposals and executes enacted laws. Its direct S5 witness is the membership/identity path: current members can ratify an executable law that sets `agent.active = False`, thereby expelling a member and changing the active system boundary before subsequent rounds continue.

Published pooled results report 8/460 enacted exile proposals (1.7%) in non-thinking runs and 31/122 (25.4%) in thinking runs. The observation remains `benchmark-scaffolded`; no underlying model or canonical harness inherits native S5 capability by association.

## Direct canonical evidence — Ouroboros parent-governed policy change

Canonical anchor:

```text
razzant/ouroboros
review ref: 86806ee123ce8e26cc063cc1a618f975eea64f26
canonical S5 state: A(P)
observed ownership mode: parent-governed
comparison class: descriptive-only
```

The canonical assessment independently identifies Constitution/identity/settings authority as S5 and distinguishes autonomous Cyber Pro authority from ordinary parent-governed authority. Capability evidence does not create that ownership state.

The admitted observation is deliberately limited to the parent-governed path:

```text
ultimate internal review/configuration authority question
        ↓
agent-authored constitutional/runtime proposal
        ↓
explicit owner-selected issue work
        ↓
repository owner razzant merges PR #855
        ↓
BIBLE.md + executable runtime policy change
        ↓
Cyber Pro review/configuration authority changes in first-party code
        ↓
merge persists into later canonical lineage and subsequent operation
```

The constitutional change is preserved in commit `25fbd3615a97e6ec3277c470eac9862d448aee10`. PR #855 is authored from the `ouroboros-agent` fork, explicitly describes the sprint as owner-selected work, and is merged by repository owner `razzant` as merge commit `dd5aded8fef7884774e2ccba3802f4bf0200d124`.

The PR changes executable authority paths as well as documentation:

- `runtime_mode_policy.py` gives Cyber Pro unrestricted internal action authority while preserving independent findings as evidence;
- `config.py` keeps context/safety lowering owner-only outside Cyber Pro while permitting Cyber Pro to author those settings;
- `tests/test_review_cyber_authority.py` exercises continuation/commit behavior under failed or pending review without erasing review facts.

The merge commit is an ancestor of canonical review ref `86806ee123ce8e26cc063cc1a618f975eea64f26`; the later revision is 673 commits ahead and retains the executable policy. This supplies the return-to-operation/persistence leg of the S5 chain.

This is **not** evidence that autonomous Cyber Pro independently selected the constitutional change. The legitimate decision/enactment evidence here is parent authority: owner-selected work plus owner merge.

## Reviewed nearby evidence

The coverage layer continues to preserve fixed-policy enforcement/governance, value/policy reasoning proxies, live constitutional-process evidence, parent-escalation protocols, native constitutional mechanisms and constitution-optimization evidence separately from direct observations.

These categories remain useful but do not become a matched primary merely through S5-shaped vocabulary or mechanism existence.

## Why the primary gap remains evidence-backed

The separation is now:

```text
direct S5 benchmark family exists          yes
canonical direct S5 observation exists     yes — one descriptive system
matched multi-canonical S5 primary exists  no
```

Ouroboros provides one canonical native descriptive witness, but there is no second canonical native or adapter-preserved S5 system under a materially comparable authority/change/subsequent-operation surface. GovSim-SelfGovern is direct but benchmark-scaffolded and therefore cannot itself supply the missing canonical comparison row.

The present `gap` therefore means:

> no reviewed public evidence currently supports a materially matched comparison of multiple canonical native or adapter-preserved S5 implementations.

It does not mean direct S5 evidence or canonical direct S5 evidence is absent.

## Reopen rule

Reopen the primary-baseline decision when public evidence supplies one of:

1. a second canonical native/adapter-preserved direct S5 observation under a materially comparable authority/change/subsequent-operation surface;
2. a materially matched benchmark comparing multiple canonical-linkable S5 systems under that chain;
3. GovSim-SelfGovern or another direct family exposing adapter-preserved canonical rows with sufficient immutable model/configuration provenance for a matched comparison cell.

Another heterogeneous single-system policy-change history can increase evidence depth but does not by itself establish a matched primary.

## Consequence

```text
S5 primary baseline = gap
```

This remains an evidence-backed empirical disposition, not a zero S5 capability score, not a reassessment of canonical ownership, and not a ranking between `A`, `P`, `A(P)` or other S5 ownership arrangements.

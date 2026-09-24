# S3* primary-search closure

Status: experimental, non-normative.  
Tracking issue: #561  
Scope: current public evidence reviewed through 2026-09-24.

## Result

```text
canonical native S3* observations        available
composed direct S3* evidence             available
matched whole-system comparison          available
matched canonical-native S3* primary     not available
S3* primary baseline                     gap
```

This closes the current search transaction, not the possibility of future matched evidence.

## Native evidence already available

Two canonical systems have direct native S3* evidence:

- **AppliedScientist** — quantitative fresh-review → corrective revision → fresh-review closure over 30 scientific-revision trajectories, including 128/150 resolved execution weaknesses;
- **data-to-paper** — a first-party published reviewer-feedback → performer-revision → review-completion witness, preserved as descriptive-only because no aggregate S3*-specific score is reported.

They cannot form a matched cell. Their task surfaces, models, evaluator designs and result shapes differ.

## Composed direct evidence

TrueCall, SWE-Review and harness-bench demonstrate that complementary audit and review→correction→re-verification can be benchmarked directly. They are useful direct S3* families at their declared composed boundaries.

They do not establish a comparison of multiple canonical harnesses exercising their **own** S3* paths. The auditor/reviewer organization is supplied by the benchmark/composition.

## Strongest matched public negative control

`Can AI Evaluate AI Scientists?` (arXiv:2607.28631) evaluates Sakana v1, Sakana v2, CycleResearcher and Data-to-Paper on a common set of 15 research proposals with a common automated multi-model paper-quality evaluation surface.

That makes it a strong whole-system comparison, but not a native S3* comparison.

The paper's own architecture table reports:

| System | Integrated Review |
| --- | --- |
| Sakana v1 | No |
| Sakana v2 | No |
| CycleResearcher | Yes |
| Data-to-Paper | No |
| FARS reference | Yes |

Canonical `data-to-paper` independently has `S3*=A`, but the evaluated configuration in this matched study is explicitly characterized as **without integrated review**. Therefore the common paper-quality scores cannot be attributed to data-to-paper's canonical reviewer→revision S3* path.

This provides a useful negative control:

```text
same systems + same proposals + same evaluator
        !=
matched S3* capability
```

unless the native complementary-audit path is actually active.

## Why the current gap is evidence-backed

The strongest available evidence fails in different ways:

```text
AppliedScientist ↔ data-to-paper
    native S3* exists on both sides
    but measurement surfaces are heterogeneous

TrueCall / SWE-Review / harness-bench
    direct review/audit capability is measured
    but the S3* organization is benchmark-defined/composed

AI-scientist head-to-head
    cross-system matching exists
    but canonical data-to-paper native S3* is not active in the evaluated configuration
```

Weakening any of these distinctions would collapse whole-system quality, external review capability and native complementary-audit capability into one metric.

## Reopen rule

Reopen when new public primary evidence provides at least one materially matched cell where:

1. two or more systems are independently canonical-linkable with S3*;
2. each evaluated configuration actually activates its native/adapter-preserved S3* path;
3. tasks, model/configuration and evaluator surface are materially matched;
4. discrepancy detection returns corrective information into current control;
5. corrected operation/artifact is re-verified or otherwise closes the audit loop.

Do not reopen merely for another external reviewer benchmark, whole-system output-quality leaderboard, or heterogeneous single-system result.

## Consequence

```text
S3* primary baseline = gap
```

Here `gap` is an evidence-backed empirical disposition. It is not a zero capability result and does not erase the two canonical native observations or the direct composed benchmark evidence.

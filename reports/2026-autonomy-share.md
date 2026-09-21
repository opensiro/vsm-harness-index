# 2026 YTD autonomous-ownership share

Snapshot report for the VSM Harness Index.

- **Index revision:** `eebe516174b712a144b143da7afd7b636f6e070b`
- **Snapshot date:** 2026-09-21
- **Temporal field:** GitHub repository creation time from `data/catalog.psv:repository_created_at`
- **Cohort:** canonical `status: included` harnesses whose repository was created in calendar year 2026
- **Cohort size:** **59 harnesses**
- **Semantic contract at snapshot:** Profile 0.2.3 / Methodology 0.3.5

This is a descriptive temporal projection of canonical assessment states. It is not a product-quality, maturity, or VSM-viability score.

## Result

| VSM function | Strict `A` | Strict `A` share | Base `A` (`A` + `A(P)`) | Base `A` share |
| --- | ---: | ---: | ---: | ---: |
| S1 | 59 / 59 | **100.0%** | 59 / 59 | **100.0%** |
| S2 | 15 / 59 | **25.4%** | 15 / 59 | **25.4%** |
| S3 | 14 / 59 | **23.7%** | 20 / 59 | **33.9%** |
| S3* | 18 / 59 | **30.5%** | 18 / 59 | **30.5%** |
| S4 | 5 / 59 | **8.5%** | 6 / 59 | **10.2%** |
| S5 | 1 / 59 | **1.7%** | 1 / 59 | **1.7%** |

`A(P)` is separated in the strict column but counts as base `A` in the base-ownership column, matching the existing `RANKINGS.md` rule that `A(P)` has base state `A`. Methodology does not apply `A(P)` to S2 or S3*.

## Full-A incidence

No canonical 2026-created harness at this snapshot has base-agent-owned `A` coverage across all six functions:

- **Full-A:** `0 / 59` — **0.0%**
- **5 / 6 base-agent-owned functions:** `2 / 59` — **3.4%**

The two 5/6 systems are Headcount (`A A A C A A`) and oh-my-agent (`A A A A A —`). This is a statement about their canonical vectors at the pinned Index snapshot, not an overall ordering of product quality or maturity.

## Distribution by base-agent-owned function count

| Base `A` functions | Harnesses | Share of 2026 cohort |
| ---: | ---: | ---: |
| 6 / 6 | 0 | 0.0% |
| 5 / 6 | 2 | 3.4% |
| 4 / 6 | 10 | 16.9% |
| 3 / 6 | 6 | 10.2% |
| 2 / 6 | 10 | 16.9% |
| 1 / 6 | 31 | 52.5% |

## Interpretation boundaries

### S1 is selection-sensitive

The 100% S1 share should not be read as evidence that every 2026 agent project has autonomous S1. The canonical Index is an admitted harness corpus; a sufficient first-party operational boundary is part of admission. The S1 percentage therefore reflects the corpus boundary as well as the ecosystem.

### Metasystem autonomy remains uncommon in this cohort

Within the admitted 2026-created cohort, base-agent-owned closure is much less frequent outside S1: S2 is 25.4%, S3 is 33.9%, S3* is 30.5%, S4 is 10.2%, and S5 is 1.7%.

These shares describe independently assessed ownership arrangements. They do not form a maturity ladder: `A`, `C`, and parent-governed states represent different ownership/closure configurations, and `—` is boundary-relative absence rather than a claim that a function cannot be added downstream.

### 2026 is year-to-date

The snapshot is taken on 2026-09-21. Calendar 2026 is incomplete, and Q3 itself is still open. The 2026 figures should therefore be treated as **YTD**, not directly compared with a complete historical year without controlling for the observation window and continuing Index admission.

Issue [#242](https://github.com/opensiro/vsm-harness-index/issues/242) tracks a deterministic quarter-granularity projection derived from the existing `repository_created_at` field, so future temporal analysis can distinguish closed quarters from partial periods without duplicating catalog metadata.

## Reproduction logic

The report uses existing source-of-truth relationships only:

```text
data/catalog.psv
  repository_created_at -> temporal cohort

assessments/*.md
  status: included + S1/S2/S3/S3*/S4/S5 states
        |
        v
RANKINGS.md base-state convention
  A(P) -> A
  C(P) -> C
        |
        v
2026 YTD descriptive aggregation
```

No assessment state is inferred from repository age. Repository creation time only selects the temporal cohort; all VSM states come from canonical standalone assessments.

## Calculation notes

Percentages use the 59 included 2026-created harnesses as denominator and are rounded to one decimal place.

- strict `A` counts literal `A` only;
- base `A` counts `A` and `A(P)`;
- `C`, `C(P)`, `P`, `—`, and `?` do not count as autonomous ownership;
- Full-A requires base `A` on all six functions;
- additions, reassessments, or same-ref corrections after the pinned Index revision can change later snapshots.

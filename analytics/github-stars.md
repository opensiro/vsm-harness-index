# GitHub star distribution (non-canonical)

![Histogram of OpenSiro included harnesses by GitHub stars](github-stars.svg)

A **point-in-time external popularity snapshot**, not an autonomy score, quality
rating, VSM ownership measurement, or admission criterion. GitHub stars change,
and GitHub popularity is neither an assessment criterion nor evidence of S1–S5.

- Included-cohort boundary: `data/catalog.psv` joined to `data/signatures.psv`
  at commit `46219bf103b0b122d86abc3ca70ae3d8bc820e2c`. Proposed and excluded rows are not counted.
- GitHub observation window (UTC): 2026-11-09T13:51:48Z to 2026-11-09T13:52:32Z.
- Included: **1 060**; observed: **1 050**;
  unavailable: **10** (shown as missing, *not* zero).
- Median: **54.0** stars; mean: **6 762** stars.
- Under 10: **370** (35.2%);
  under 100: **574** (54.7%);
  at least 10,000: **115** (11.0%).
- Unavailable repository: [headcount](https://github.com/cbrock84/headcount), [veritas](https://github.com/matiasrodlo/veritas), [korus](https://github.com/surefire-ai/korus), [visvoai](https://github.com/VisvoAI/visvoai), [shelracode](https://github.com/Shelra/ShelraCode), [qcode](https://github.com/fwtllh-png/QCode), [gopi](https://github.com/cgund98/gopi), [setup-ai-core](https://github.com/kartalbas/setup-ai-core), [agent-harness-cmabery](https://github.com/CMABERY/agent-harness), [rubin-johnson-maestro](https://github.com/rubin-johnson/maestro).

## Histogram

| GitHub stars (bin) | Harnesses | Share of observed |
| --- | ---: | ---: |
| 0 | 136 | 13.0% |
| 1–4 | 153 | 14.6% |
| 5–9 | 81 | 7.7% |
| 10–24 | 85 | 8.1% |
| 25–49 | 64 | 6.1% |
| 50–99 | 55 | 5.2% |
| 100–249 | 105 | 10.0% |
| 250–499 | 62 | 5.9% |
| 500–999 | 60 | 5.7% |
| 1k–2.5k | 68 | 6.5% |
| 2.5k–5k | 25 | 2.4% |
| 5k–10k | 41 | 3.9% |
| 10k–25k | 45 | 4.3% |
| 25k–50k | 36 | 3.4% |
| 50k–100k | 16 | 1.5% |
| 100k+ | 18 | 1.7% |

Bins are **unequal-width categories**; bars show the number of projects in
each category, not a density and not a continuous linear-scale histogram.
The external snapshot is machine-readable at
[`data/github-stars.json`](../data/github-stars.json).

## Refresh and validation

```bash
python scripts/github_stars.py refresh   # network required; uses GITHUB_TOKEN if set
python scripts/github_stars.py render    # offline, from committed snapshot
python scripts/github_stars.py check     # offline; fails if generated outputs drift
python -m unittest tests/test_github_stars.py
```

`refresh` uses GitHub REST API with `GITHUB_TOKEN`, otherwise public GitHub
repository pages. A 404 records `stars: null`, never zero; transient/API
errors **fail the refresh** rather than silently producing partial data.
The source revision and UTC observation window are pinned in the snapshot.
Scheduled refresh automation proposes a separate PR for review; it does not
edit canonical VSM assessments or the main branch directly.

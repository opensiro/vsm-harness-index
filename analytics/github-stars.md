# GitHub star distribution (non-canonical)

![Histogram of OpenSiro included harnesses by GitHub stars](github-stars.svg)

A **point-in-time external popularity snapshot**, not an autonomy score, quality
rating, VSM ownership measurement, or admission criterion. GitHub stars change,
and GitHub popularity is neither an assessment criterion nor evidence of S1–S5.

- Included-cohort boundary: `data/catalog.psv` joined to `data/signatures.psv`
  at commit `b48b13e74d6938f833094d3f9afc1a11e61a8515`. Proposed and excluded rows are not counted.
- GitHub observation window (UTC): 2026-10-19T10:44:26Z to 2026-10-19T10:44:53Z.
- Included: **581**; observed: **577**;
  unavailable: **4** (shown as missing, *not* zero).
- Median: **189** stars; mean: **11 448** stars.
- Under 10: **165** (28.6%);
  under 100: **252** (43.7%);
  at least 10,000: **107** (18.5%).
- Unavailable repository: [veritas](https://github.com/matiasrodlo/veritas), [korus](https://github.com/surefire-ai/korus), [visvoai](https://github.com/VisvoAI/visvoai), [qcode](https://github.com/fwtllh-png/QCode).

## Histogram

| GitHub stars (bin) | Harnesses | Share of observed |
| --- | ---: | ---: |
| 0 | 45 | 7.8% |
| 1–4 | 77 | 13.3% |
| 5–9 | 43 | 7.5% |
| 10–24 | 37 | 6.4% |
| 25–49 | 23 | 4.0% |
| 50–99 | 27 | 4.7% |
| 100–249 | 46 | 8.0% |
| 250–499 | 34 | 5.9% |
| 500–999 | 41 | 7.1% |
| 1k–2.5k | 49 | 8.5% |
| 2.5k–5k | 15 | 2.6% |
| 5k–10k | 33 | 5.7% |
| 10k–25k | 39 | 6.8% |
| 25k–50k | 35 | 6.1% |
| 50k–100k | 16 | 2.8% |
| 100k+ | 17 | 2.9% |

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

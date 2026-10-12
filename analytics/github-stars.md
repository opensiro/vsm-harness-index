# GitHub star distribution (non-canonical)

![Histogram of OpenSiro included harnesses by GitHub stars](github-stars.svg)

A **point-in-time external popularity snapshot**, not an autonomy score, quality
rating, VSM ownership measurement, or admission criterion. GitHub stars change,
and GitHub popularity is neither an assessment criterion nor evidence of S1–S5.

- Included-cohort boundary: `data/catalog.psv` joined to `data/signatures.psv`
  at commit `ab469d23d6efcae3f0d6deedbeca07473ce7d5b8`. Proposed and excluded rows are not counted.
- GitHub observation window (UTC): 2026-10-12T13:09:00Z to 2026-10-12T13:09:24Z.
- Included: **483**; observed: **481**;
  unavailable: **2** (shown as missing, *not* zero).
- Median: **250** stars; mean: **12 920** stars.
- Under 10: **146** (30.4%);
  under 100: **202** (42.0%);
  at least 10,000: **103** (21.4%).
- Unavailable repository: [korus](https://github.com/surefire-ai/korus), [visvoai](https://github.com/VisvoAI/visvoai).

## Histogram

| GitHub stars (bin) | Harnesses | Share of observed |
| --- | ---: | ---: |
| 0 | 41 | 8.5% |
| 1–4 | 71 | 14.8% |
| 5–9 | 34 | 7.1% |
| 10–24 | 22 | 4.6% |
| 25–49 | 13 | 2.7% |
| 50–99 | 21 | 4.4% |
| 100–249 | 38 | 7.9% |
| 250–499 | 27 | 5.6% |
| 500–999 | 33 | 6.9% |
| 1k–2.5k | 42 | 8.7% |
| 2.5k–5k | 12 | 2.5% |
| 5k–10k | 24 | 5.0% |
| 10k–25k | 36 | 7.5% |
| 25k–50k | 35 | 7.3% |
| 50k–100k | 16 | 3.3% |
| 100k+ | 16 | 3.3% |

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

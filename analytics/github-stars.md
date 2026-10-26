# GitHub star distribution (non-canonical)

![Histogram of OpenSiro included harnesses by GitHub stars](github-stars.svg)

A **point-in-time external popularity snapshot**, not an autonomy score, quality
rating, VSM ownership measurement, or admission criterion. GitHub stars change,
and GitHub popularity is neither an assessment criterion nor evidence of S1–S5.

- Included-cohort boundary: `data/catalog.psv` joined to `data/signatures.psv`
  at commit `bb01978d5553f1db429b2dc3c196ee02c0eb9764`. Proposed and excluded rows are not counted.
- GitHub observation window (UTC): 2026-10-26T11:04:36Z to 2026-10-26T11:04:59Z.
- Included: **711**; observed: **703**;
  unavailable: **8** (shown as missing, *not* zero).
- Median: **137** stars; mean: **9 657** stars.
- Under 10: **220** (31.3%);
  under 100: **332** (47.2%);
  at least 10,000: **111** (15.8%).
- Unavailable repository: [veritas](https://github.com/matiasrodlo/veritas), [korus](https://github.com/surefire-ai/korus), [aesop](https://github.com/matt82198/aesop), [gyrfalcon](https://github.com/cargopete/gyrfalcon), [visvoai](https://github.com/VisvoAI/visvoai), [shelracode](https://github.com/Shelra/ShelraCode), [qcode](https://github.com/fwtllh-png/QCode), [gopi](https://github.com/cgund98/gopi).

## Histogram

| GitHub stars (bin) | Harnesses | Share of observed |
| --- | ---: | ---: |
| 0 | 70 | 10.0% |
| 1–4 | 94 | 13.4% |
| 5–9 | 56 | 8.0% |
| 10–24 | 45 | 6.4% |
| 25–49 | 32 | 4.6% |
| 50–99 | 35 | 5.0% |
| 100–249 | 62 | 8.8% |
| 250–499 | 39 | 5.5% |
| 500–999 | 48 | 6.8% |
| 1k–2.5k | 56 | 8.0% |
| 2.5k–5k | 22 | 3.1% |
| 5k–10k | 33 | 4.7% |
| 10k–25k | 42 | 6.0% |
| 25k–50k | 36 | 5.1% |
| 50k–100k | 15 | 2.1% |
| 100k+ | 18 | 2.6% |

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

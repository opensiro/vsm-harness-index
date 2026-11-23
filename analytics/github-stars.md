# GitHub star distribution (non-canonical)

![Histogram of OpenSiro included harnesses by GitHub stars](github-stars.svg)

A **point-in-time external popularity snapshot**, not an autonomy score, quality
rating, VSM ownership measurement, or admission criterion. GitHub stars change,
and GitHub popularity is neither an assessment criterion nor evidence of S1–S5.

- Included-cohort boundary: `data/catalog.psv` joined to `data/signatures.psv`
  at commit `a3fcf7c156ef4d1132680890bc11544681fd30c0`. Proposed and excluded rows are not counted.
- GitHub observation window (UTC): 2026-11-23T15:56:14Z to 2026-11-23T15:57:00Z.
- Included: **1 224**; observed: **1 206**;
  unavailable: **18** (shown as missing, *not* zero).
- Median: **49.5** stars; mean: **6 036** stars.
- Under 10: **408** (33.8%);
  under 100: **679** (56.3%);
  at least 10,000: **117** (9.7%).
- Unavailable repository: [microsoft-agent-framework](https://github.com/microsoft/agent-framework), [proliferate](https://github.com/proliferate-ai/proliferate), [headcount](https://github.com/cbrock84/headcount), [veritas](https://github.com/matiasrodlo/veritas), [korus](https://github.com/surefire-ai/korus), [codehamr](https://github.com/plaxtoris/codehamr), [visvoai](https://github.com/VisvoAI/visvoai), [shelracode](https://github.com/Shelra/ShelraCode), [qcode](https://github.com/fwtllh-png/QCode), [gopi](https://github.com/cgund98/gopi), [dtadpole-heddle](https://github.com/dtadpole/heddle), [setup-ai-core](https://github.com/kartalbas/setup-ai-core), [inkpi](https://github.com/MeiSiristhebest/inkpi), [agent-harness-cmabery](https://github.com/CMABERY/agent-harness), [gifford](https://github.com/smellak/gifford), [nipus-harness](https://github.com/cUDGk/nipus-harness), [rubin-johnson-maestro](https://github.com/rubin-johnson/maestro), [quickcode](https://github.com/devincii-io/QuickCode).

## Histogram

| GitHub stars (bin) | Harnesses | Share of observed |
| --- | ---: | ---: |
| 0 | 138 | 11.4% |
| 1–4 | 171 | 14.2% |
| 5–9 | 99 | 8.2% |
| 10–24 | 111 | 9.2% |
| 25–49 | 84 | 7.0% |
| 50–99 | 76 | 6.3% |
| 100–249 | 115 | 9.5% |
| 250–499 | 74 | 6.1% |
| 500–999 | 74 | 6.1% |
| 1k–2.5k | 76 | 6.3% |
| 2.5k–5k | 27 | 2.2% |
| 5k–10k | 44 | 3.6% |
| 10k–25k | 47 | 3.9% |
| 25k–50k | 33 | 2.7% |
| 50k–100k | 19 | 1.6% |
| 100k+ | 18 | 1.5% |

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

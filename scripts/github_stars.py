#!/usr/bin/env python3
"""Refresh and deterministically render non-canonical GitHub-stars analytics.

Network access is restricted to "refresh". "render" and "check" are offline.
Run from the repository root, or pass --root for tests/local fixtures.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import csv
import html
import io
import json
import os
import re
import statistics
import subprocess
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

BINS = [
    ("0", 0, 1), ("1–4", 1, 5), ("5–9", 5, 10), ("10–24", 10, 25),
    ("25–49", 25, 50), ("50–99", 50, 100), ("100–249", 100, 250),
    ("250–499", 250, 500), ("500–999", 500, 1000),
    ("1k–2.5k", 1000, 2500), ("2.5k–5k", 2500, 5000),
    ("5k–10k", 5000, 10000), ("10k–25k", 10000, 25000),
    ("25k–50k", 25000, 50000), ("50k–100k", 50000, 100000),
    ("100k+", 100000, float("inf")),
]
USER_AGENT = "OpenSiro-VSM-Index-GitHub-Stars/1.0"
JSON_PATH = "data/github-stars.json"
DOC_PATH = "analytics/github-stars.md"
SVG_PATH = "analytics/github-stars.svg"
REPO_PATTERN = re.compile(r"^https://github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)/?$")


def included_rows(root: Path) -> list[dict[str, str]]:
    """Only canonical included rows; proposed/excluded must never leak in."""
    with (root / "data/catalog.psv").open(encoding="utf-8", newline="") as f:
        catalog = list(csv.DictReader(f, delimiter="|"))
    with (root / "data/signatures.psv").open(encoding="utf-8", newline="") as f:
        signatures = list(csv.DictReader(f, delimiter="|"))
    ids = {row["harness_id"] for row in signatures}
    if len(ids) != len(signatures):
        raise ValueError("duplicate included harness_id in signatures.psv")
    rows = [row for row in catalog if row["harness_id"] in ids]
    if len(rows) != len(ids):
        raise ValueError("catalog/signatures cohort mismatch")
    return rows


def request_stars(repo: str, token: str | None) -> tuple[int | None, str]:
    """Use authenticated REST when available; HTML otherwise. 404 != 0 stars."""
    url = ("https://api.github.com/repos/" if token else "https://github.com/") + repo
    headers = {"User-Agent": USER_AGENT, "Accept": "application/vnd.github+json" if token else "text/html"}
    if token:
        headers["Authorization"] = "Bearer " + token
        headers["X-GitHub-Api-Version"] = "2022-11-28"
    for attempt in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=35) as response:
                body = response.read().decode("utf-8", errors="replace")
            if token:
                count = json.loads(body).get("stargazers_count")
            else:
                found = re.search(r'"stargazerCount":(\d+)', body)
                count = int(found.group(1)) if found else None
            if type(count) is not int or count < 0:
                raise ValueError("missing/non-numeric GitHub star count for " + repo)
            return count, "ok"
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                return None, "not_found"
            if exc.code not in (429, 500, 502, 503, 504) and exc.code != 403:
                raise RuntimeError(f"GitHub HTTP {exc.code} for {repo}") from exc
            if attempt == 3:
                raise RuntimeError(f"GitHub HTTP {exc.code} after retries for {repo}") from exc
        except (urllib.error.URLError, TimeoutError) as exc:
            if attempt == 3:
                raise RuntimeError(f"GitHub fetch failed after retries for {repo}") from exc
        if attempt != 3:
            time.sleep(min(2 ** attempt, 8))
    raise RuntimeError("retry loop exhausted for " + repo)


def refresh(root: Path, workers: int) -> None:
    cohort = included_rows(root)
    repos = []
    for row in cohort:
        match = REPO_PATTERN.fullmatch(row["repository"])
        if not match:
            raise ValueError(f"invalid GitHub URL for {row['harness_id']}: {row['repository']}")
        repos.append(match.group(1))
    token = os.environ.get("GITHUB_TOKEN") or None
    source_sha = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=root, text=True
    ).strip()
    started = datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
        results = list(pool.map(lambda repo: request_stars(repo, token), repos))
    finished = datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")
    snapshot = {
        "schema_version": 1,
        "source": "GitHub repository stargazerCount / REST stargazers_count",
        "cohort": "canonical included at source_commit; catalog order",
        "source_commit": source_sha,
        "started_at_utc": started,
        "finished_at_utc": finished,
        "records": [
            {
                "harness_id": row["harness_id"],
                "project_name": row["project_name"],
                "repository": row["repository"],
                "stars": count,
                "fetch_status": status,
            }
            for row, (count, status) in zip(cohort, results, strict=True)
        ],
    }
    (root / JSON_PATH).write_text(json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Captured {len(cohort)} included harnesses; {sum(v[0] is None for v in results)} unavailable", flush=True)
    render(root, check=False)


def summarize(snapshot: dict) -> dict:
    if snapshot.get("schema_version") != 1 or not snapshot.get("source_commit"):
        raise ValueError("unsupported or incomplete stars snapshot")
    records = snapshot["records"]
    if not isinstance(records, list) or not records:
        raise ValueError("empty stars snapshot")
    ids = set()
    values = []
    unavailable = []
    for record in records:
        ident = record["harness_id"]
        if ident in ids:
            raise ValueError("duplicate harness_id: " + ident)
        ids.add(ident)
        count, status = record["stars"], record["fetch_status"]
        if count is None and status == "not_found":
            unavailable.append(record)
        elif type(count) is int and count >= 0 and status == "ok":
            values.append(count)
        else:
            raise ValueError("invalid star count / status pairing: " + ident)
    values.sort()
    bars = [{"label": label, "count": sum(lo <= value < hi for value in values)}
            for label, lo, hi in BINS]
    if sum(row["count"] for row in bars) != len(values):
        raise ValueError("star histogram does not cover the observed cohort")
    return {
        "total": len(records), "counted": len(values), "unavailable": unavailable,
        "median": statistics.median(values), "mean": round(statistics.mean(values)),
        "bars": bars, "under_100": sum(v < 100 for v in values),
        "under_10": sum(v < 10 for v in values),
        "over_10000": sum(v >= 10000 for v in values),
    }


def fmt(value: int | float) -> str:
    return f"{value:,}".replace(",", " ")


def markdown(snapshot: dict, summary: dict) -> str:
    count = summary["counted"]
    rows = "\n".join(
        f"| {bar['label']} | {bar['count']} | {100 * bar['count'] / count:.1f}% |"
        for bar in summary["bars"]
    )
    bad = ", ".join(
        f"[{rec['harness_id']}]({rec['repository']})"
        for rec in summary["unavailable"]
    ) or "None"
    return f"""# GitHub star distribution (non-canonical)

![Histogram of OpenSiro included harnesses by GitHub stars](github-stars.svg)

A **point-in-time external popularity snapshot**, not an autonomy score, quality
rating, VSM ownership measurement, or admission criterion. GitHub stars change,
and GitHub popularity is neither an assessment criterion nor evidence of S1–S5.

- Included-cohort boundary: `data/catalog.psv` joined to `data/signatures.psv`
  at commit `{snapshot['source_commit']}`. Proposed and excluded rows are not counted.
- GitHub observation window (UTC): {snapshot['started_at_utc']} to {snapshot['finished_at_utc']}.
- Included: **{fmt(summary['total'])}**; observed: **{fmt(count)}**;
  unavailable: **{len(summary['unavailable'])}** (shown as missing, *not* zero).
- Median: **{fmt(summary['median'])}** stars; mean: **{fmt(summary['mean'])}** stars.
- Under 10: **{fmt(summary['under_10'])}** ({summary['under_10'] / count:.1%});
  under 100: **{fmt(summary['under_100'])}** ({summary['under_100'] / count:.1%});
  at least 10,000: **{fmt(summary['over_10000'])}** ({summary['over_10000'] / count:.1%}).
- Unavailable repository: {bad}.

## Histogram

| GitHub stars (bin) | Harnesses | Share of observed |
| --- | ---: | ---: |
{rows}

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
"""


def svg(snapshot: dict, summary: dict) -> str:
    width, height = 1100, 805
    left, right, top, step = 180, 80, 130, 38
    max_count = max(bar["count"] for bar in summary["bars"])
    usable = width - left - right - 55
    title = "OpenSiro: GitHub stars per included harness (snapshot)"
    output = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        f'  <title id="title">{html.escape(title)}</title>',
        f'  <desc id="desc">Horizontal bar chart across 16 unequal-width star bins; {summary["counted"]} included harnesses observed, {len(summary["unavailable"])} unavailable. Stars retrieved {html.escape(snapshot["finished_at_utc"])}.</desc>',
        f'  <rect width="{width}" height="{height}" fill="#ffffff"/>',
        '  <style>text{font-family:system-ui,-apple-system,Segoe UI,sans-serif} .axis{fill:#334155;font-size:17px} .value{fill:#0f172a;font-size:16px;font-weight:650}</style>',
        '  <text x="48" y="50" fill="#0f172a" font-family="system-ui,-apple-system,Segoe UI,sans-serif" font-size="28" font-weight="700">GitHub stars across OpenSiro harnesses</text>',
        f'  <text x="48" y="84" class="axis">{summary["counted"]} observed of {summary["total"]} included · {html.escape(snapshot["finished_at_utc"][:10])} · unequal star bins</text>',
    ]
    for i, bar in enumerate(summary["bars"]):
        y = top + i * step
        length = round(usable * bar["count"] / max_count) if max_count else 0
        output.extend([
            f'  <text class="axis" x="{left - 18}" y="{y + 20}" text-anchor="end">{html.escape(bar["label"])}</text>',
            f'  <rect x="{left}" y="{y}" width="{usable}" height="28" rx="4" fill="#e2e8f0"/>',
            f'  <rect x="{left}" y="{y}" width="{length}" height="28" rx="4" fill="#2563eb"/>',
            f'  <text class="value" x="{left + usable + 12}" y="{y + 21}">{bar["count"]}</text>',
        ])
    output.append('  <text x="48" y="778" class="axis">Counts per category · popularity only, not VSM autonomy or quality</text>')
    output.append('</svg>')
    return "\n".join(output) + "\n"


def render(root: Path, check: bool) -> None:
    snapshot = json.loads((root / JSON_PATH).read_text(encoding="utf-8"))
    summary = summarize(snapshot)
    for name, content in [(DOC_PATH, markdown(snapshot, summary)), (SVG_PATH, svg(snapshot, summary))]:
        path = root / name
        if check:
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                raise ValueError(f"{name} differs; run python scripts/github_stars.py render")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
    print(f"{'Checked' if check else 'Rendered'} {summary['counted']} observed / {summary['total']} included", flush=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("refresh", "render", "check"))
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--workers", type=int, default=8)
    args = parser.parse_args()
    if args.workers < 1 or args.workers > 16:
        parser.error("--workers must be between 1 and 16")
    if args.action == "refresh":
        refresh(args.root, args.workers)
    else:
        render(args.root, check=(args.action == "check"))


if __name__ == "__main__":
    main()

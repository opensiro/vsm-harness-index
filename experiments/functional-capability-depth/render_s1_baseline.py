#!/usr/bin/env python3
"""Render the experimental S1 capability baseline from selection + raw evidence."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SELECTION = HERE / "primary-baselines.json"
OBSERVATIONS = HERE / "s1-system-benchmarks" / "observations.jsonl"
OUTPUT = HERE / "S1-BASELINE.md"
ASSESSMENTS = ROOT / "assessments"

FRONTMATTER = re.compile(r"^---\n(.*?)\n---\n", re.S)
FUNCTION_ORDER = ("S1", "S2", "S3", "S3*", "S4", "S5")
ESTABLISHED_S1 = {"A", "C", "P", "A(P)", "C(P)"}


def fail(message: str) -> None:
    raise SystemExit(f"error: {message}")


def parse_frontmatter(path: Path) -> dict[str, str]:
    if not path.exists():
        fail(f"missing canonical assessment: {path.relative_to(ROOT)}")
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER.match(text)
    if not match:
        fail(f"assessment has no front matter: {path.relative_to(ROOT)}")
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip()
    return fields


def canonical(harness_id: str) -> dict[str, str]:
    fields = parse_frontmatter(ASSESSMENTS / f"{harness_id}.md")
    if fields.get("status") != "included":
        fail(f"{harness_id}: canonical assessment is not included")
    if fields.get("autonomy_s1") not in ESTABLISHED_S1:
        fail(f"{harness_id}: canonical assessment does not establish S1")
    return fields


def load_observations() -> list[dict]:
    rows: list[dict] = []
    seen: set[str] = set()
    for lineno, raw in enumerate(
        OBSERVATIONS.read_text(encoding="utf-8").splitlines(), start=1
    ):
        if not raw.strip():
            continue
        try:
            row = json.loads(raw)
        except json.JSONDecodeError as exc:
            fail(f"observations.jsonl:{lineno}: {exc}")
        rid = row.get("record_id")
        if not isinstance(rid, str) or not rid:
            fail(f"observations.jsonl:{lineno}: missing record_id")
        if rid in seen:
            fail(f"duplicate observation record_id: {rid}")
        seen.add(rid)
        rows.append(row)
    return rows


def matching(
    rows: list[dict], *, family: str, model: str, scope: str
) -> list[dict]:
    out: list[dict] = []
    for row in rows:
        benchmark = row.get("benchmark") or {}
        observation = row.get("observation") or {}
        comparison = row.get("comparison") or {}
        if benchmark.get("family_id") != family:
            continue
        if observation.get("model") != model:
            continue
        if comparison.get("mode") != "matched-model":
            continue
        if comparison.get("scope") != scope:
            continue
        out.append(row)
    return out


def expected_cell(
    rows: list[dict],
    *,
    family: str,
    model: str,
    scope: str,
    harness_ids: list[str],
) -> list[dict]:
    candidates = matching(rows, family=family, model=model, scope=scope)
    by_harness: dict[str, list[dict]] = {}
    for row in candidates:
        by_harness.setdefault(row.get("harness_id"), []).append(row)

    selected: list[dict] = []
    for harness_id in harness_ids:
        matches = by_harness.get(harness_id, [])
        if len(matches) != 1:
            fail(
                f"{family}/{model}/{scope}: expected exactly one observation for "
                f"{harness_id}, found {len(matches)}"
            )
        selected.append(matches[0])
    return sorted(selected, key=lambda row: row["harness_id"])


def extra_cell(
    rows: list[dict], *, family: str, model: str, scope: str
) -> list[dict]:
    selected = matching(rows, family=family, model=model, scope=scope)
    if len({row.get("harness_id") for row in selected}) < 2:
        fail(f"{family}/{model}/{scope}: additional matched evidence needs >=2 systems")
    return sorted(selected, key=lambda row: row["harness_id"])


def validate_row(row: dict) -> tuple[dict[str, str], dict, dict]:
    harness_id = row.get("harness_id")
    if not isinstance(harness_id, str) or not harness_id:
        fail("matched observation missing harness_id")
    fields = canonical(harness_id)
    if row.get("canonical_repository") != fields.get("repository"):
        fail(f"{harness_id}: canonical_repository drift")
    if row.get("assessment_ref") != fields.get("review_ref"):
        fail(f"{harness_id}: assessment_ref drift")

    observation = row.get("observation") or {}
    identity = row.get("identity") or {}
    if identity.get("system_compatibility") not in {"native-system", "adapter-preserved"}:
        fail(f"{harness_id}: invalid system compatibility for baseline view")
    if identity.get("revision_match") not in {
        "exact-historical",
        "version-known",
        "unknown",
    }:
        fail(f"{harness_id}: invalid revision_match")
    if not isinstance(observation.get("metric"), str) or not observation["metric"]:
        fail(f"{harness_id}: missing observation metric")
    if not isinstance(observation.get("value"), (int, float)):
        fail(f"{harness_id}: missing numeric observation value")
    return fields, observation, identity


def project_label(fields: dict[str, str], harness_id: str) -> str:
    return fields.get("project_name") or harness_id


def revision_label(observation: dict, identity: dict) -> str:
    version = observation.get("harness_version")
    revision = observation.get("harness_revision")
    match = identity.get("revision_match")
    if revision:
        prefix = revision[:12]
        if version:
            return f"`{version}` @ `{prefix}` · {match}"
        return f"`{prefix}` · {match}"
    if version:
        return f"`{version}` · {match}"
    return f"N/A · {match}"


def result_label(observation: dict) -> str:
    metric = observation["metric"]
    value = observation["value"]
    if metric == "overall_score":
        return f"`{value:.4f}`"
    if metric.endswith("_percent"):
        return f"`{value:.1f}%`"
    if metric == "pass_rate":
        passed = observation.get("passed")
        valid = observation.get("valid")
        if isinstance(passed, int) and isinstance(valid, int) and valid:
            return f"`{passed}/{valid}` ({value * 100:.1f}%)"
        return f"`{value:.4f}`"
    return f"`{value}`"


def render_rows(rows: list[dict]) -> list[str]:
    lines = [
        "| Harness | Canonical S1 | Historical benchmark identity | Result | Compatibility |",
        "| --- | --- | --- | ---: | --- |",
    ]
    for row in rows:
        fields, observation, identity = validate_row(row)
        harness_id = row["harness_id"]
        lines.append(
            "| "
            + " | ".join(
                [
                    f"{project_label(fields, harness_id)} (`{harness_id}`)",
                    f"`{fields['autonomy_s1']}`",
                    revision_label(observation, identity),
                    result_label(observation),
                    f"`{identity['system_compatibility']}`",
                ]
            )
            + " |"
        )
    return lines


def render() -> str:
    selection = json.loads(SELECTION.read_text(encoding="utf-8"))
    functions = selection.get("functions") or {}
    rows = load_observations()

    s1 = functions.get("S1") or {}
    if s1.get("status") != "selected":
        fail("S1 primary baseline is not selected")

    primary = s1.get("primary") or {}
    general_family = primary.get("benchmark_id")
    general_model = primary.get("reference_model")
    general_ids = primary.get("canonical_harness_ids")
    if not isinstance(general_family, str) or not general_family:
        fail("S1 primary benchmark_id missing")
    if not isinstance(general_model, str) or not general_model:
        fail("S1 primary reference_model missing")
    if not isinstance(general_ids, list) or not general_ids:
        fail("S1 primary canonical_harness_ids missing")

    domain = ((s1.get("domains") or {}).get("coding_swe") or {})
    domain_primary = domain.get("primary") or {}
    domain_family = domain_primary.get("benchmark_id")
    domain_model = domain_primary.get("reference_model")
    domain_ids = domain_primary.get("verified_canonical_harness_ids")
    if not isinstance(domain_family, str) or not domain_family:
        fail("coding_swe primary benchmark_id missing")
    if not isinstance(domain_model, str) or not domain_model:
        fail("coding_swe primary reference_model missing")
    if not isinstance(domain_ids, list) or not domain_ids:
        fail("coding_swe verified_canonical_harness_ids missing")

    general_rows = expected_cell(
        rows,
        family=general_family,
        model=general_model,
        scope="general-baseline",
        harness_ids=general_ids,
    )
    domain_rows = expected_cell(
        rows,
        family=domain_family,
        model=domain_model,
        scope="coding-swe",
        harness_ids=domain_ids,
    )

    additional_specs = domain.get("additional_evidence") or []
    additional: list[tuple[dict, list[dict]]] = []
    for spec in additional_specs:
        family = spec.get("benchmark_id")
        model = spec.get("reference_model")
        if not isinstance(family, str) or not family:
            fail("coding_swe additional evidence missing benchmark_id")
        if not isinstance(model, str) or not model:
            fail(f"{family}: additional evidence missing reference_model")
        additional.append(
            (spec, extra_cell(rows, family=family, model=model, scope="coding-swe"))
        )

    lines = [
        "# S1 Capability Baseline",
        "",
        "Generated experimental projection from `primary-baselines.json`, canonical assessments, and `s1-system-benchmarks/observations.jsonl`.",
        "",
        "This is not a global harness ranking. Canonical VSM ownership and benchmark performance remain separate evidence layers. Rows are ordered by harness ID, never by score.",
        "",
        "## Function baseline availability",
        "",
        "| Function | Status | Primary family | Reference model |",
        "| --- | --- | --- | --- |",
    ]

    for function in FUNCTION_ORDER:
        item = functions.get(function) or {}
        status = item.get("status", "gap")
        if status == "selected":
            p = item.get("primary") or {}
            family_name = p.get("benchmark_name") or p.get("benchmark_id") or "N/A"
            model = p.get("reference_model") or "N/A"
        else:
            family_name = "—"
            model = "—"
        lines.append(f"| {function} | `{status}` | {family_name} | {model} |")

    lines += [
        "",
        "A `gap` means no primary matched canonical-harness baseline has been selected for that function yet. It is not a zero score and does not mean the function has no benchmark evidence.",
        "",
        "## S1 general primary",
        "",
        f"**{primary.get('benchmark_name', general_family)}** · model `{general_model}` · scope `general-baseline`",
        "",
        *render_rows(general_rows),
        "",
        "Only this selected family/cell is the current general S1 baseline. Other S1 observations remain secondary or domain evidence.",
        "",
        "## S1 / Coding-SWE domain primary",
        "",
        f"**{domain_primary.get('benchmark_name', domain_family)}** · model `{domain_model}` · scope `coding-swe`",
        "",
        *render_rows(domain_rows),
        "",
        "This table is a Coding/SWE projection of S1 capability. It must not be promoted to universal S1 capability.",
    ]

    for spec, extra_rows in additional:
        lines += [
            "",
            "## Additional Coding-SWE evidence",
            "",
            f"**{spec.get('benchmark_name', spec['benchmark_id'])}** · model `{spec['reference_model']}` · scope `coding-swe`",
            "",
            *render_rows(extra_rows),
            "",
            "This is additional matched evidence, not another primary and not an input to a composite score.",
        ]

    lines += [
        "",
        "## Reading rule",
        "",
        "```text",
        "canonical VSM state",
        "        ↓",
        "selected function/domain baseline",
        "        ↓",
        "additional benchmark evidence",
        "",
        "separate track:",
        "self-organizing adaptation evidence",
        "```",
        "",
        "Ordinary baseline observations use the frozen-repertoire rule. Adaptive/self-organizing runs belong to a separate evidence class and are not mixed into these cells.",
        "",
        "Do not average PawBench, Claw-SWE-Bench, FrontierHarness, or other benchmark families into one S1 or overall harness score.",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    rendered = render()
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != rendered:
            raise SystemExit(
                "S1-BASELINE.md is stale; run "
                "experiments/functional-capability-depth/render_s1_baseline.py"
            )
    else:
        OUTPUT.write_text(rendered, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

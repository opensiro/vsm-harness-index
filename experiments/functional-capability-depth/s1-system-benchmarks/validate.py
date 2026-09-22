#!/usr/bin/env python3
"""Validate direct S1 system benchmark observations against canonical assessments."""

from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import urlparse

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
OBS = HERE / "observations.jsonl"

ALLOWED_COMPAT = {"native-system", "adapter-preserved"}
ALLOWED_REVISION = {"exact-historical", "version-known", "unknown"}
ALLOWED_COMPARE = {"matched-model", "partially-matched", "descriptive-only"}
ALLOWED_FAMILIES = {"swe-bench", "terminal-bench"}
FRONTMATTER = re.compile(r"^---\n(.*?)\n---\n", re.S)


def fail(msg: str) -> None:
    raise SystemExit(f"error: {msg}")


def https(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


def assessment_fields(harness_id: str) -> dict[str, str]:
    path = ROOT / "assessments" / f"{harness_id}.md"
    if not path.exists():
        fail(f"missing canonical assessment for {harness_id}")
    match = FRONTMATTER.match(path.read_text(encoding="utf-8"))
    if not match:
        fail(f"assessment {path} has no front matter")
    out: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        out[key.strip()] = value.strip()
    return out


def main() -> None:
    records: list[dict] = []
    for lineno, raw in enumerate(OBS.read_text(encoding="utf-8").splitlines(), start=1):
        if not raw.strip():
            continue
        try:
            record = json.loads(raw)
        except json.JSONDecodeError as exc:
            fail(f"observations.jsonl:{lineno}: {exc}")
        records.append(record)

    if not records:
        fail("no observations")

    seen_ids: set[str] = set()
    systems: set[str] = set()
    groups: dict[str, list[dict]] = {}

    for idx, rec in enumerate(records, start=1):
        rid = rec.get("record_id")
        if not isinstance(rid, str) or not rid:
            fail(f"record {idx}: missing record_id")
        if rid in seen_ids:
            fail(f"duplicate record_id: {rid}")
        seen_ids.add(rid)

        if rec.get("function") != "S1":
            fail(f"{rid}: function must be S1")

        harness_id = rec.get("harness_id")
        if not isinstance(harness_id, str) or not harness_id:
            fail(f"{rid}: missing harness_id")
        systems.add(harness_id)

        assessment = assessment_fields(harness_id)
        if assessment.get("status") != "included":
            fail(f"{rid}: canonical assessment is not included")
        if assessment.get("autonomy_s1") not in {"A", "C", "P"}:
            fail(f"{rid}: canonical assessment does not establish S1")
        if rec.get("canonical_repository") != assessment.get("repository"):
            fail(f"{rid}: canonical_repository drift")
        if rec.get("assessment_ref") != assessment.get("review_ref"):
            fail(f"{rid}: assessment_ref drift")

        benchmark = rec.get("benchmark") or {}
        if benchmark.get("family_id") not in ALLOWED_FAMILIES:
            fail(f"{rid}: benchmark family is not an accepted direct S1 family")
        for key in ("primary_source", "artifact_source"):
            if not https(benchmark.get(key)):
                fail(f"{rid}: {key} must be https")

        observation = rec.get("observation") or {}
        if not isinstance(observation.get("model"), str) or not observation["model"]:
            fail(f"{rid}: model is required")
        if not isinstance(observation.get("metric"), str) or not observation["metric"]:
            fail(f"{rid}: metric is required")
        if not isinstance(observation.get("value"), (int, float)):
            fail(f"{rid}: numeric metric value is required")

        identity = rec.get("identity") or {}
        if identity.get("system_compatibility") not in ALLOWED_COMPAT:
            fail(f"{rid}: invalid system_compatibility")
        if identity.get("revision_match") not in ALLOWED_REVISION:
            fail(f"{rid}: invalid revision_match")

        comparison = rec.get("comparison") or {}
        mode = comparison.get("mode")
        group = comparison.get("group")
        if mode not in ALLOWED_COMPARE:
            fail(f"{rid}: invalid comparison mode")
        if not isinstance(group, str) or not group:
            fail(f"{rid}: comparison group required")
        groups.setdefault(group, []).append(rec)

        notes = rec.get("notes")
        if not isinstance(notes, str) or len(notes.strip()) < 20:
            fail(f"{rid}: explicit interpretation notes required")

    partially_matched_cross_system = 0
    for group, members in groups.items():
        modes = {m["comparison"]["mode"] for m in members}
        member_systems = {m["harness_id"] for m in members}
        if "matched-model" in modes and len(member_systems) < 2:
            fail(f"{group}: matched-model requires at least two systems")
        if "partially-matched" in modes and len(member_systems) >= 2:
            partially_matched_cross_system += 1

    print(f"ok: {len(records)} observations across {len(systems)} canonical S1 systems")
    print(f"comparison groups: {len(groups)}")
    print(f"cross-system partially-matched groups: {partially_matched_cross_system}")


if __name__ == "__main__":
    main()

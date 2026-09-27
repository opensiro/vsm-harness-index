#!/usr/bin/env python3
"""Render neutral public-evidence registry, including row-oriented benchmark records."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import render_registry_core as core

HERE = Path(__file__).resolve().parent
RegistryError = core.RegistryError


def _jsonl_rows(seen: set[str]) -> list[core.RegistryRow]:
    rows: list[core.RegistryRow] = []
    for path in sorted(HERE.glob("*.jsonl")):
        record_ref = path.name
        for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if not raw.strip():
                continue
            source_ref = f"{record_ref}:{lineno}"
            try:
                record = json.loads(raw)
            except json.JSONDecodeError as exc:
                raise core.RegistryError(f"{source_ref}: invalid JSON: {exc}") from exc
            if not isinstance(record, dict):
                raise core.RegistryError(f"{source_ref}: row must be a JSON object")
            if not isinstance(record.get("schema_version"), int) or record["schema_version"] < 1:
                raise core.RegistryError(f"{source_ref}: schema_version must be an integer >= 1")
            for forbidden in ("function", "benchmark_fit", "vsm_interpretation"):
                if forbidden in record:
                    raise core.RegistryError(f"{source_ref}: neutral row must not contain {forbidden}")

            oid = record.get("observation_id")
            if not isinstance(oid, str) or not core.ID_RE.fullmatch(oid):
                raise core.RegistryError(f"{source_ref}: observation_id must match {core.ID_RE.pattern}")
            if oid in seen:
                raise core.RegistryError(f"duplicate observation_id {oid!r}: JSON object record and {source_ref}")
            seen.add(oid)

            system = record.get("system_name")
            harness = record.get("canonical_harness_id")
            assessment = record.get("canonical_assessment_ref")
            review = record.get("canonical_review_ref")
            if not isinstance(system, str) or not system.strip():
                raise core.RegistryError(f"{source_ref}: system_name must be a non-empty string")
            if not isinstance(harness, str) or not harness.strip():
                raise core.RegistryError(f"{source_ref}: canonical_harness_id must be a non-empty string")
            if not isinstance(assessment, str) or not assessment.startswith("assessments/"):
                raise core.RegistryError(f"{source_ref}: canonical_assessment_ref must be under assessments/")
            if not (core.ROOT / assessment).is_file():
                raise core.RegistryError(f"{source_ref}: canonical assessment does not exist: {assessment}")
            if not isinstance(review, str) or not core.HEX40_RE.fullmatch(review):
                raise core.RegistryError(f"{source_ref}: canonical_review_ref must be 40-hex")

            source_class = record.get("evidence_source_class")
            if source_class not in core.SOURCE_CLASSES:
                raise core.RegistryError(f"{source_ref}: invalid evidence_source_class")
            impl = record.get("published_implementation")
            if not isinstance(impl, dict) or impl.get("system_compatibility") not in core.SYSTEM_COMPATIBILITY:
                raise core.RegistryError(f"{source_ref}: invalid published_implementation")
            compatibility = impl["system_compatibility"]

            benchmark = record.get("benchmark")
            if not isinstance(benchmark, dict):
                raise core.RegistryError(f"{source_ref}: benchmark must be an object")
            label = benchmark.get("name")
            if not isinstance(label, str) or not label.strip():
                raise core.RegistryError(f"{source_ref}: benchmark.name must be non-empty")
            for key in ("primary_source", "artifact_source"):
                if not core._valid_https(benchmark.get(key)):
                    raise core.RegistryError(f"{source_ref}: benchmark.{key} must be public HTTPS")

            result = record.get("result")
            if not isinstance(result, dict):
                raise core.RegistryError(f"{source_ref}: result must be an object")
            if not isinstance(result.get("model"), str) or not result["model"]:
                raise core.RegistryError(f"{source_ref}: result.model is required")
            if not isinstance(result.get("metric"), str) or not result["metric"]:
                raise core.RegistryError(f"{source_ref}: result.metric is required")
            if not isinstance(result.get("value"), (int, float)):
                raise core.RegistryError(f"{source_ref}: result.value must be numeric")

            values = (oid, system, harness, assessment, label, source_class, compatibility, record_ref)
            if any("|" in v or "\n" in v or "\r" in v for v in values):
                raise core.RegistryError(f"{source_ref}: registry fields cannot contain pipe/newline")
            rows.append(core.RegistryRow(
                observation_id=oid,
                system_name=system.strip(),
                canonical_harness_id=harness.strip(),
                canonical_assessment_ref=assessment,
                evidence_surfaces=label.strip(),
                kind="system-benchmark-result",
                evidence_source_class=source_class,
                system_compatibility=compatibility,
                record_ref=record_ref,
            ))
    return rows


def collect_rows() -> list[core.RegistryRow]:
    rows = core.collect_rows()
    seen = {row.observation_id for row in rows}
    rows.extend(_jsonl_rows(seen))
    return sorted(rows, key=lambda row: (row.system_name.lower(), row.observation_id))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    rows = collect_rows()
    psv = core.render_psv(rows)
    markdown = core.render_markdown(rows).replace(
        "raw JSON records in this directory", "raw JSON/JSONL records in this directory"
    )
    if args.check:
        stale = []
        if not core._check(core.PSV_PATH, psv):
            stale.append(core.PSV_PATH.name)
        if not core._check(core.MARKDOWN_PATH, markdown):
            stale.append(core.MARKDOWN_PATH.name)
        if stale:
            raise SystemExit("generated registry is stale: " + ", ".join(stale) + "; run render_registry.py")
        print(f"ok: generated neutral registry is current ({len(rows)} observations)")
        return
    core.PSV_PATH.write_text(psv, encoding="utf-8")
    core.MARKDOWN_PATH.write_text(markdown, encoding="utf-8")
    print(f"rendered {len(rows)} neutral public-evidence system observations")


if __name__ == "__main__":
    main()

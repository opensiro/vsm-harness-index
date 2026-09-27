#!/usr/bin/env python3
"""Render the neutral benchmark <-> system observation registry from raw records."""

from __future__ import annotations

import argparse
import csv
import io
import json
import re
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlparse

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PSV_PATH = HERE / "registry.psv"
MARKDOWN_PATH = HERE / "REGISTRY.md"

SOURCE_CLASSES = {
    "external-reproduced",
    "first-party-reported",
    "mechanism-only",
}
SYSTEM_COMPATIBILITY = {
    "native-system",
    "adapter-preserved",
    "benchmark-scaffolded",
    "unclear",
}
ID_RE = re.compile(r"^[a-z0-9][a-z0-9._-]*$")
HEX40_RE = re.compile(r"^[0-9a-f]{40}$")


class RegistryError(ValueError):
    pass


@dataclass(frozen=True)
class RegistryRow:
    observation_id: str
    system_name: str
    canonical_harness_id: str
    canonical_assessment_ref: str
    benchmark_labels: str
    kind: str
    evidence_source_class: str
    system_compatibility: str
    record_ref: str


def _valid_https(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


def _raw_json_paths() -> list[Path]:
    return sorted(path for path in HERE.glob("*.json") if path.is_file())


def _raw_jsonl_paths() -> list[Path]:
    return sorted(path for path in HERE.glob("*.jsonl") if path.is_file())


def _benchmarks(observation: dict, record_ref: str) -> list[str]:
    labels: list[str] = []

    benchmark = observation.get("benchmark")
    if benchmark is not None:
        if not isinstance(benchmark, str) or not benchmark.strip():
            raise RegistryError(
                f"{record_ref}:{observation.get('observation_id')}: benchmark must be a non-empty string"
            )
        labels.append(benchmark.strip())

    benchmark_results = observation.get("benchmark_results")
    if benchmark_results is not None:
        if not isinstance(benchmark_results, list) or not benchmark_results:
            raise RegistryError(
                f"{record_ref}:{observation.get('observation_id')}: benchmark_results must be a non-empty list"
            )
        for result in benchmark_results:
            if not isinstance(result, dict):
                raise RegistryError(
                    f"{record_ref}:{observation.get('observation_id')}: benchmark_results entries must be objects"
                )
            label = result.get("benchmark")
            if not isinstance(label, str) or not label.strip():
                raise RegistryError(
                    f"{record_ref}:{observation.get('observation_id')}: benchmark_results entry lacks benchmark identity"
                )
            labels.append(label.strip())

    unique: list[str] = []
    for label in labels:
        if label not in unique:
            unique.append(label)
    if not unique:
        raise RegistryError(
            f"{record_ref}:{observation.get('observation_id')}: no benchmark identity is recoverable"
        )
    return unique


def _canonical_link(record: dict, record_ref: str) -> tuple[str, str]:
    canonical_harness_id = record.get("canonical_harness_id")
    if canonical_harness_id is None:
        canonical_harness_id = ""
    elif not isinstance(canonical_harness_id, str) or not canonical_harness_id.strip():
        raise RegistryError(
            f"{record_ref}: canonical_harness_id must be null or a non-empty string"
        )
    else:
        canonical_harness_id = canonical_harness_id.strip()

    canonical_assessment_ref = record.get("canonical_assessment_ref")
    canonical_review_ref = record.get("canonical_review_ref")
    if canonical_harness_id:
        if not isinstance(canonical_assessment_ref, str) or not canonical_assessment_ref.startswith("assessments/"):
            raise RegistryError(
                f"{record_ref}: canonical linkage requires canonical_assessment_ref under assessments/"
            )
        if not (ROOT / canonical_assessment_ref).is_file():
            raise RegistryError(
                f"{record_ref}: canonical_assessment_ref does not exist: {canonical_assessment_ref}"
            )
        if not isinstance(canonical_review_ref, str) or not HEX40_RE.fullmatch(canonical_review_ref):
            raise RegistryError(
                f"{record_ref}: canonical linkage requires a 40-hex canonical_review_ref snapshot"
            )
    else:
        canonical_assessment_ref = ""

    return canonical_harness_id, canonical_assessment_ref or ""


def _append_row(
    *,
    rows: list[RegistryRow],
    seen: dict[str, str],
    observation_id: object,
    system_name: object,
    canonical_harness_id: str,
    canonical_assessment_ref: str,
    benchmarks: list[str],
    kind: object,
    source_class: object,
    compatibility: object,
    record_ref: str,
) -> None:
    if not isinstance(observation_id, str) or not ID_RE.fullmatch(observation_id):
        raise RegistryError(f"{record_ref}: observation_id must match {ID_RE.pattern}")
    if observation_id in seen:
        raise RegistryError(
            f"duplicate observation_id {observation_id!r}: {seen[observation_id]} and {record_ref}"
        )
    seen[observation_id] = record_ref

    if not isinstance(system_name, str) or not system_name.strip():
        raise RegistryError(f"{record_ref}: system_name must be a non-empty string")
    if not isinstance(kind, str) or not kind.strip():
        raise RegistryError(f"{record_ref}:{observation_id}: kind must be a non-empty string")
    if source_class not in SOURCE_CLASSES:
        raise RegistryError(
            f"{record_ref}: evidence_source_class must be one of {sorted(SOURCE_CLASSES)}"
        )
    if compatibility not in SYSTEM_COMPATIBILITY:
        raise RegistryError(
            f"{record_ref}: system_compatibility must be one of {sorted(SYSTEM_COMPATIBILITY)}"
        )

    values = (
        observation_id,
        system_name,
        canonical_harness_id,
        canonical_assessment_ref,
        "; ".join(benchmarks),
        kind,
        source_class,
        compatibility,
        record_ref,
    )
    if any("|" in value or "\n" in value or "\r" in value for value in values):
        raise RegistryError(
            f"{record_ref}:{observation_id}: generated registry fields cannot contain pipe/newline characters"
        )

    rows.append(
        RegistryRow(
            observation_id=observation_id,
            system_name=system_name.strip(),
            canonical_harness_id=canonical_harness_id,
            canonical_assessment_ref=canonical_assessment_ref,
            benchmark_labels="; ".join(benchmarks),
            kind=kind.strip(),
            evidence_source_class=source_class,
            system_compatibility=compatibility,
            record_ref=record_ref,
        )
    )


def _collect_object_records(rows: list[RegistryRow], seen: dict[str, str]) -> None:
    for path in _raw_json_paths():
        record_ref = path.name
        try:
            record = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise RegistryError(f"{record_ref}: invalid JSON: {exc}") from exc

        if not isinstance(record, dict):
            raise RegistryError(f"{record_ref}: raw record must be a JSON object")
        if not isinstance(record.get("schema_version"), int) or record["schema_version"] < 1:
            raise RegistryError(f"{record_ref}: schema_version must be an integer >= 1")

        canonical_harness_id, canonical_assessment_ref = _canonical_link(record, record_ref)
        source_class = record.get("evidence_source_class")
        implementation = record.get("published_implementation")
        if not isinstance(implementation, dict):
            raise RegistryError(f"{record_ref}: published_implementation must be an object")
        compatibility = implementation.get("system_compatibility")

        sources = record.get("primary_sources")
        if not isinstance(sources, list) or not sources:
            raise RegistryError(f"{record_ref}: primary_sources must be a non-empty list")
        if any(not _valid_https(source) for source in sources):
            raise RegistryError(f"{record_ref}: every primary source must be a public HTTPS URL")

        observations = record.get("observations")
        if not isinstance(observations, list) or not observations:
            raise RegistryError(f"{record_ref}: observations must be a non-empty list")

        for observation in observations:
            if not isinstance(observation, dict):
                raise RegistryError(f"{record_ref}: every observation must be an object")
            _append_row(
                rows=rows,
                seen=seen,
                observation_id=observation.get("observation_id"),
                system_name=record.get("system_name"),
                canonical_harness_id=canonical_harness_id,
                canonical_assessment_ref=canonical_assessment_ref,
                benchmarks=_benchmarks(observation, record_ref),
                kind=observation.get("kind"),
                source_class=source_class,
                compatibility=compatibility,
                record_ref=record_ref,
            )


def _collect_row_records(rows: list[RegistryRow], seen: dict[str, str]) -> None:
    for path in _raw_jsonl_paths():
        for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if not raw.strip():
                continue
            record_ref = path.name
            source_ref = f"{record_ref}:{lineno}"
            try:
                record = json.loads(raw)
            except json.JSONDecodeError as exc:
                raise RegistryError(f"{source_ref}: invalid JSON: {exc}") from exc
            if not isinstance(record, dict):
                raise RegistryError(f"{source_ref}: row must be a JSON object")
            if not isinstance(record.get("schema_version"), int) or record["schema_version"] < 1:
                raise RegistryError(f"{source_ref}: schema_version must be an integer >= 1")
            for forbidden in ("function", "benchmark_fit", "vsm_interpretation"):
                if forbidden in record:
                    raise RegistryError(f"{source_ref}: neutral row must not contain {forbidden}")

            canonical_harness_id, canonical_assessment_ref = _canonical_link(record, source_ref)
            implementation = record.get("published_implementation")
            if not isinstance(implementation, dict):
                raise RegistryError(f"{source_ref}: published_implementation must be an object")
            compatibility = implementation.get("system_compatibility")

            benchmark = record.get("benchmark")
            if not isinstance(benchmark, dict):
                raise RegistryError(f"{source_ref}: benchmark must be an object")
            benchmark_name = benchmark.get("name")
            if not isinstance(benchmark_name, str) or not benchmark_name.strip():
                raise RegistryError(f"{source_ref}: benchmark.name must be a non-empty string")
            for key in ("primary_source", "artifact_source"):
                if not _valid_https(benchmark.get(key)):
                    raise RegistryError(f"{source_ref}: benchmark.{key} must be a public HTTPS URL")

            result = record.get("result")
            if not isinstance(result, dict):
                raise RegistryError(f"{source_ref}: result must be an object")
            if not isinstance(result.get("model"), str) or not result["model"]:
                raise RegistryError(f"{source_ref}: result.model is required")
            if not isinstance(result.get("metric"), str) or not result["metric"]:
                raise RegistryError(f"{source_ref}: result.metric is required")
            if not isinstance(result.get("value"), (int, float)):
                raise RegistryError(f"{source_ref}: result.value must be numeric")

            _append_row(
                rows=rows,
                seen=seen,
                observation_id=record.get("observation_id"),
                system_name=record.get("system_name"),
                canonical_harness_id=canonical_harness_id,
                canonical_assessment_ref=canonical_assessment_ref,
                benchmarks=[benchmark_name.strip()],
                kind="system-benchmark-result",
                source_class=record.get("evidence_source_class"),
                compatibility=compatibility,
                record_ref=record_ref,
            )


def collect_rows() -> list[RegistryRow]:
    rows: list[RegistryRow] = []
    seen_observation_ids: dict[str, str] = {}
    _collect_object_records(rows, seen_observation_ids)
    _collect_row_records(rows, seen_observation_ids)
    return sorted(rows, key=lambda row: (row.system_name.lower(), row.observation_id))


def render_psv(rows: list[RegistryRow]) -> str:
    buffer = io.StringIO()
    writer = csv.writer(buffer, delimiter="|", lineterminator="\n")
    writer.writerow(
        [
            "observation_id",
            "system_name",
            "canonical_harness_id",
            "benchmark_labels",
            "kind",
            "evidence_source_class",
            "system_compatibility",
            "record_ref",
        ]
    )
    for row in rows:
        writer.writerow(
            [
                row.observation_id,
                row.system_name,
                row.canonical_harness_id,
                row.benchmark_labels,
                row.kind,
                row.evidence_source_class,
                row.system_compatibility,
                row.record_ref,
            ]
        )
    return buffer.getvalue()


def _escape_md(value: str) -> str:
    return value.replace("|", "\\|")


def render_markdown(rows: list[RegistryRow]) -> str:
    lines = [
        "# Benchmark ↔ system observation registry",
        "",
        "Status: **generated, experimental, non-normative**",
        "",
        "Generated from the raw JSON/JSONL records in this directory by `render_registry.py`.",
        "Numeric benchmark payloads remain only in the raw record; this table is an identity/provenance projection, not a second result database.",
        "",
        f"Raw observations: **{len(rows)}**",
        "",
        "| System | Canonical harness | Observation | Benchmark surface(s) | Kind | Provenance | Compatibility | Raw record |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in rows:
        if row.canonical_harness_id:
            harness = (
                f"[{_escape_md(row.canonical_harness_id)}]"
                f"(../../../{row.canonical_assessment_ref})"
            )
        else:
            harness = "—"
        lines.append(
            "| "
            + " | ".join(
                [
                    _escape_md(row.system_name),
                    harness,
                    f"`{_escape_md(row.observation_id)}`",
                    _escape_md(row.benchmark_labels),
                    f"`{_escape_md(row.kind)}`",
                    f"`{_escape_md(row.evidence_source_class)}`",
                    f"`{_escape_md(row.system_compatibility)}`",
                    f"[{_escape_md(row.record_ref)}]({row.record_ref})",
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "VSM-function relevance is intentionally absent from this generated registry. Derived/community interpretations reference the raw `observation_id` separately.",
            "",
        ]
    )
    return "\n".join(lines)


def _check(path: Path, expected: str) -> bool:
    return path.is_file() and path.read_text(encoding="utf-8") == expected


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    rows = collect_rows()
    psv = render_psv(rows)
    markdown = render_markdown(rows)

    if args.check:
        stale: list[str] = []
        if not _check(PSV_PATH, psv):
            stale.append(PSV_PATH.name)
        if not _check(MARKDOWN_PATH, markdown):
            stale.append(MARKDOWN_PATH.name)
        if stale:
            raise SystemExit(
                "generated registry is stale: " + ", ".join(stale) + "; run render_registry.py"
            )
        print(f"ok: generated neutral registry is current ({len(rows)} observations)")
        return

    PSV_PATH.write_text(psv, encoding="utf-8")
    MARKDOWN_PATH.write_text(markdown, encoding="utf-8")
    print(f"rendered {len(rows)} neutral benchmark-system observations")


if __name__ == "__main__":
    main()

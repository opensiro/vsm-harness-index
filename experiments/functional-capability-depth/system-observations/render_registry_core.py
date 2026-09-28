#!/usr/bin/env python3
"""Render the neutral public-evidence <-> system observation registry from raw JSON records."""

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
FORBIDDEN_VSM_VALUE_RE = re.compile(
    r"(?<![A-Za-z0-9])(?:S3\*|S[1-5]|VSM|Viable System Model)(?![A-Za-z0-9])",
    re.IGNORECASE,
)


class RegistryError(ValueError):
    pass


FORBIDDEN_VSM_KEYS = {
    "function",
    "benchmark_fit",
    "vsm_interpretation",
    "function_interpretation",
    "mixed_function_caveat",
    "aggregate_s3star_metric_reported",
    "canonical_state_at_review",
    "canonical_states_at_review",
    "canonical_system_eligible",
    "coverage_class",
}


def _forbidden_vsm_key(key: str) -> bool:
    return (
        key in FORBIDDEN_VSM_KEYS
        or key.startswith("autonomy_s")
        or key.startswith("vsm_")
        or re.match(r"^canonical_.*state", key) is not None
    )


def _validate_vsm_neutral(value: object, record_ref: str, path: str = "$") -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{path}.{key}"
            if _forbidden_vsm_key(key):
                raise RegistryError(
                    f"{record_ref}:{child_path}: raw neutral evidence must not encode VSM-function/state attribution"
                )
            _validate_vsm_neutral(child, record_ref, child_path)
    elif isinstance(value, list):
        for idx, child in enumerate(value):
            _validate_vsm_neutral(child, record_ref, f"{path}[{idx}]")


@dataclass(frozen=True)
class RegistryRow:
    observation_id: str
    system_name: str
    canonical_harness_id: str
    canonical_assessment_ref: str
    evidence_surfaces: str
    kind: str
    evidence_source_class: str
    system_compatibility: str
    record_ref: str


def _valid_https(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


def _raw_paths() -> list[Path]:
    return sorted(
        path
        for path in HERE.glob("*.json")
        if path.is_file()
    )


def _evidence_surfaces(observation: dict, record_ref: str) -> list[str]:
    labels: list[str] = []

    benchmark = observation.get("benchmark")
    if benchmark is not None:
        if isinstance(benchmark, str):
            if not benchmark.strip():
                raise RegistryError(
                    f"{record_ref}:{observation.get('observation_id')}: benchmark must be non-empty"
                )
            labels.append(benchmark.strip())
        elif isinstance(benchmark, dict):
            label = benchmark.get("name")
            if not isinstance(label, str) or not label.strip():
                raise RegistryError(
                    f"{record_ref}:{observation.get('observation_id')}: structured benchmark lacks name"
                )
            for key in ("primary_source", "artifact_source"):
                if not _valid_https(benchmark.get(key)):
                    raise RegistryError(
                        f"{record_ref}:{observation.get('observation_id')}: benchmark.{key} must be public HTTPS"
                    )
            labels.append(label.strip())
        else:
            raise RegistryError(
                f"{record_ref}:{observation.get('observation_id')}: benchmark must be a string or object"
            )

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

    evidence_surface = observation.get("evidence_surface")
    if evidence_surface is not None:
        if not isinstance(evidence_surface, str) or not evidence_surface.strip():
            raise RegistryError(
                f"{record_ref}:{observation.get('observation_id')}: evidence_surface must be a non-empty string"
            )
        labels.append(evidence_surface.strip())

    evidence_surfaces = observation.get("evidence_surfaces")
    if evidence_surfaces is not None:
        if not isinstance(evidence_surfaces, list) or not evidence_surfaces:
            raise RegistryError(
                f"{record_ref}:{observation.get('observation_id')}: evidence_surfaces must be a non-empty list"
            )
        for surface in evidence_surfaces:
            if not isinstance(surface, str) or not surface.strip():
                raise RegistryError(
                    f"{record_ref}:{observation.get('observation_id')}: evidence_surfaces entries must be non-empty strings"
                )
            labels.append(surface.strip())

    unique: list[str] = []
    for label in labels:
        if label not in unique:
            unique.append(label)
    if not unique:
        raise RegistryError(
            f"{record_ref}:{observation.get('observation_id')}: no public evidence-surface identity is recoverable"
        )
    return unique


def collect_rows() -> list[RegistryRow]:
    rows: list[RegistryRow] = []
    seen_observation_ids: dict[str, str] = {}

    for path in _raw_paths():
        record_ref = path.name
        try:
            record = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise RegistryError(f"{record_ref}: invalid JSON: {exc}") from exc

        if not isinstance(record, dict):
            raise RegistryError(f"{record_ref}: raw record must be a JSON object")
        _validate_vsm_neutral(record, record_ref)
        if not isinstance(record.get("schema_version"), int) or record["schema_version"] < 1:
            raise RegistryError(f"{record_ref}: schema_version must be an integer >= 1")

        system_name = record.get("system_name")
        if not isinstance(system_name, str) or not system_name.strip():
            raise RegistryError(f"{record_ref}: system_name must be a non-empty string")

        source_class = record.get("evidence_source_class")
        if source_class not in SOURCE_CLASSES:
            raise RegistryError(
                f"{record_ref}: evidence_source_class must be one of {sorted(SOURCE_CLASSES)}"
            )

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

        implementation = record.get("published_implementation")
        if not isinstance(implementation, dict):
            raise RegistryError(f"{record_ref}: published_implementation must be an object")
        compatibility = implementation.get("system_compatibility")
        if compatibility not in SYSTEM_COMPATIBILITY:
            raise RegistryError(
                f"{record_ref}: system_compatibility must be one of {sorted(SYSTEM_COMPATIBILITY)}"
            )

        historical_relation = implementation.get("historical_relation")
        if historical_relation is not None:
            if not isinstance(historical_relation, str) or not historical_relation.strip():
                raise RegistryError(
                    f"{record_ref}: published_implementation.historical_relation must be a non-empty string when present"
                )
            if FORBIDDEN_VSM_VALUE_RE.search(historical_relation):
                raise RegistryError(
                    f"{record_ref}: published_implementation.historical_relation must remain implementation-independent and VSM-neutral"
                )

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

            observation_id = observation.get("observation_id")
            if not isinstance(observation_id, str) or not ID_RE.fullmatch(observation_id):
                raise RegistryError(
                    f"{record_ref}: observation_id must match {ID_RE.pattern}"
                )
            if observation_id in seen_observation_ids:
                previous = seen_observation_ids[observation_id]
                raise RegistryError(
                    f"duplicate observation_id {observation_id!r}: {previous} and {record_ref}"
                )
            seen_observation_ids[observation_id] = record_ref

            kind = observation.get("kind")
            if not isinstance(kind, str) or not kind.strip():
                raise RegistryError(f"{record_ref}:{observation_id}: kind must be a non-empty string")

            surfaces = _evidence_surfaces(observation, record_ref)
            for value in (
                observation_id,
                system_name,
                canonical_harness_id,
                canonical_assessment_ref or "",
                "; ".join(surfaces),
                kind,
                source_class,
                compatibility,
                record_ref,
            ):
                if "|" in value or "\n" in value or "\r" in value:
                    raise RegistryError(
                        f"{record_ref}:{observation_id}: generated registry fields cannot contain pipe/newline characters"
                    )

            rows.append(
                RegistryRow(
                    observation_id=observation_id,
                    system_name=system_name.strip(),
                    canonical_harness_id=canonical_harness_id,
                    canonical_assessment_ref=canonical_assessment_ref or "",
                    evidence_surfaces="; ".join(surfaces),
                    kind=kind.strip(),
                    evidence_source_class=source_class,
                    system_compatibility=compatibility,
                    record_ref=record_ref,
                )
            )

    return sorted(rows, key=lambda row: (row.system_name.lower(), row.observation_id))


def render_psv(rows: list[RegistryRow]) -> str:
    buffer = io.StringIO()
    writer = csv.writer(buffer, delimiter="|", lineterminator="\n")
    writer.writerow(
        [
            "observation_id",
            "system_name",
            "canonical_harness_id",
            "evidence_surfaces",
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
                row.evidence_surfaces,
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
        "# Public evidence ↔ system observation registry",
        "",
        "Status: **generated, experimental, non-normative**",
        "",
        "Generated from the raw JSON records in this directory by `render_registry.py`.",
        "Raw evidence payloads remain only in the raw record; this table is an identity/provenance projection, not a second result database.",
        "",
        f"Raw observations: **{len(rows)}**",
        "",
        "| System | Canonical harness | Observation | Evidence surface(s) | Kind | Provenance | Compatibility | Raw record |",
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
                    _escape_md(row.evidence_surfaces),
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
    print(f"rendered {len(rows)} neutral public-evidence system observations")


if __name__ == "__main__":
    main()

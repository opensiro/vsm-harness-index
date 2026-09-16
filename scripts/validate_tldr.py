#!/usr/bin/env python3
"""Parse and validate standalone harness assessments."""
from __future__ import annotations
from datetime import date
from pathlib import Path
import re

SYSTEM_KEYS = ("s1", "s2", "s3", "s3_star", "s4", "s5")
ALLOWED = {"A", "A(P)", "C", "C(P)", "P", "—", "?"}
PARENT_MODE_STATES = {"A(P)", "C(P)", "P"}
PARENT_MODE_KEYS = {"s3", "s4", "s5"}
ALLOWED_STATUSES = {"included", "excluded-no-agentic-vsm", "proposed"}
FRESHNESS_KEYS = (
    "last_checked_ref",
    "last_checked_at",
    "assessment_changed_at",
    "last_reassessment_round",
)
SPEC_PROVENANCE_KEYS = (
    "profile_version",
    "assessment_procedure_version",
)
GENERATION_PROVENANCE_KEYS = (
    "generated_profile_version",
    "generated_assessment_procedure_version",
)
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?$")


def parse_assessment(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: missing frontmatter")
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        raise ValueError(f"{path}: malformed frontmatter")
    row: dict[str, str] = {}
    for line in parts[1].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            row[key.strip()] = value.strip()
    row["path"] = str(path)
    return row


def load_assessments(directory: Path) -> dict[str, dict[str, str]]:
    rows: dict[str, dict[str, str]] = {}
    for path in sorted(directory.glob("*.md")):
        row = parse_assessment(path)
        harness_id = row.get("harness_id", "")
        if not harness_id or harness_id in rows:
            raise ValueError(f"{path}: missing or duplicate harness_id")
        rows[harness_id] = row
    return rows


def vector(row: dict[str, str]) -> list[str]:
    return [row.get(f"autonomy_{key}", "") for key in SYSTEM_KEYS]


def semver_core(value: str) -> tuple[int, int, int] | None:
    if not value or not SEMVER_RE.fullmatch(value):
        return None
    core = re.split(r"[-+]", value, maxsplit=1)[0]
    major, minor, patch = core.split(".")
    return int(major), int(minor), int(patch)


def require_iso_date(row: dict[str, str], key: str) -> None:
    value = row.get(key, "")
    try:
        date.fromisoformat(value)
    except ValueError as exc:
        raise ValueError(f"{row.get('harness_id')}: {key} must be YYYY-MM-DD") from exc


def validate_version_pair(row: dict[str, str], keys: tuple[str, str], label: str) -> list[str]:
    present = [key for key in keys if row.get(key)]
    if present and len(present) != len(keys):
        missing = [key for key in keys if not row.get(key)]
        raise ValueError(f"{row['harness_id']}: {label} metadata must be complete; missing {missing}")
    for key in present:
        if not SEMVER_RE.fullmatch(row[key]):
            raise ValueError(f"{row['harness_id']}: {key} must be a semantic version such as 0.2.0")
    return present


def validate_parent_mode_states(row: dict[str, str], states: list[str]) -> None:
    """Enforce the Methodology boundary for parent-mode notation."""
    if row["status"] == "proposed":
        # Proposed files are review artifacts and may contain claims admission
        # is expected to reject or correct. Canonical invariants apply on admission.
        return

    methodology = semver_core(row.get("assessment_procedure_version", ""))
    for key, state in zip(SYSTEM_KEYS, states):
        if state in PARENT_MODE_STATES and key not in PARENT_MODE_KEYS:
            raise ValueError(
                f"{row['harness_id']}: {state} is valid only for S3, S4, or S5 under Methodology 0.3+"
            )

        if state in {"A(P)", "C(P)"}:
            if methodology is None or methodology < (0, 3, 0):
                raise ValueError(
                    f"{row['harness_id']}: {state} requires assessment_procedure_version >= 0.3.0"
                )

        if key in {"s3", "s4"} and state == "P":
            if methodology is None or methodology < (0, 3, 0):
                raise ValueError(
                    f"{row['harness_id']}: {key.upper()}=P requires assessment_procedure_version >= 0.3.0"
                )


def validate_assessment(row: dict[str, str]) -> None:
    for key in ("harness_id", "project_name", "repository", "review_ref", "reviewed_at", "status"):
        if not row.get(key):
            raise ValueError(f"{row.get('path')}: missing {key}")
    if row["status"] not in ALLOWED_STATUSES:
        raise ValueError(
            f"{row['harness_id']}: invalid status {row['status']!r}; expected one of {sorted(ALLOWED_STATUSES)}"
        )
    if len(row["review_ref"]) != 40:
        raise ValueError(f"{row['harness_id']}: review_ref must be 40 characters")
    require_iso_date(row, "reviewed_at")

    states = vector(row)
    if any(state not in ALLOWED for state in states):
        raise ValueError(f"{row['harness_id']}: invalid autonomy state")

    present_spec = validate_version_pair(row, SPEC_PROVENANCE_KEYS, "spec provenance")
    present_generation = validate_version_pair(row, GENERATION_PROVENANCE_KEYS, "generation provenance")
    if present_generation and not present_spec:
        raise ValueError(
            f"{row['harness_id']}: generation provenance requires current Profile/procedure provenance"
        )

    validate_parent_mode_states(row, states)

    if row["status"] == "included" and states[0] != "A":
        raise ValueError(f"{row['harness_id']}: included harness must establish S1 · A")

    present_freshness = [key for key in FRESHNESS_KEYS if row.get(key)]
    if present_freshness and len(present_freshness) != len(FRESHNESS_KEYS):
        missing = [key for key in FRESHNESS_KEYS if not row.get(key)]
        raise ValueError(
            f"{row['harness_id']}: reassessment freshness metadata must be complete; missing {missing}"
        )
    if present_freshness:
        if row["status"] == "proposed":
            raise ValueError(f"{row['harness_id']}: proposed assessment cannot carry canonical reassessment freshness")
        if len(row["last_checked_ref"]) != 40:
            raise ValueError(f"{row['harness_id']}: last_checked_ref must be 40 characters")
        require_iso_date(row, "last_checked_at")
        require_iso_date(row, "assessment_changed_at")
        if not row["last_reassessment_round"].startswith("R") or not row["last_reassessment_round"][1:].isdigit():
            raise ValueError(f"{row['harness_id']}: last_reassessment_round must look like R1")
        if row["assessment_changed_at"] > row["last_checked_at"]:
            raise ValueError(
                f"{row['harness_id']}: assessment_changed_at cannot be later than last_checked_at"
            )


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    rows = load_assessments(repo / "assessments")
    for row in rows.values():
        validate_assessment(row)
    print(f"Validated {len(rows)} standalone assessment(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

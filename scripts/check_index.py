#!/usr/bin/env python3
"""Validate registry, assessments, reassessment history, signatures, and generated views."""
from __future__ import annotations
import csv
from datetime import date
from pathlib import Path
from validate_tldr import SEMVER_RE, load_assessments, validate_assessment
from render_tldr import render_tldr, render_rankings

CATALOG_FIELDS = [
    "catalog_position",
    "harness_id",
    "project_name",
    "repository",
    "repository_created_at",
    "source_membership",
    "review_ref",
    "pinned_at",
]

REASSESSMENT_FIELDS = [
    "round_id",
    "harness_id",
    "previous_review_ref",
    "checked_ref",
    "accepted_review_ref",
    "checked_at",
    "profile_version",
    "assessment_procedure_version",
    "outcome",
    "changed_functions",
    "evidence",
]

REASSESSMENT_OUTCOMES = {
    "no-upstream-change",
    "no-material-change",
    "reassessed-unchanged",
    "reassessed-changed",
    "same-ref-correction",
    "blocked",
}


def read_psv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="|")
        if path.name == "catalog.psv" and reader.fieldnames != CATALOG_FIELDS:
            raise SystemExit(
                "catalog schema mismatch: expected discovery/order/provenance fields only; "
                f"got {reader.fieldnames}"
            )
        if path.name == "reassessment-history.psv" and reader.fieldnames != REASSESSMENT_FIELDS:
            raise SystemExit(
                "reassessment history schema mismatch: "
                f"expected {REASSESSMENT_FIELDS}, got {reader.fieldnames}"
            )
        return list(reader)


def validate_reassessment_history(
    rows: list[dict[str, str]],
    catalog: dict[str, dict[str, str]],
    assessments: dict[str, dict[str, str]],
) -> None:
    seen: set[tuple[str, str]] = set()
    latest_event: dict[str, dict[str, str]] = {}
    latest_successful: dict[str, dict[str, str]] = {}

    for row in rows:
        harness_id = row["harness_id"]
        round_id = row["round_id"]
        key = (round_id, harness_id)
        if key in seen:
            raise SystemExit(f"duplicate reassessment event: {round_id}/{harness_id}")
        seen.add(key)

        if harness_id not in catalog or harness_id not in assessments:
            raise SystemExit(f"reassessment history references unknown or incomplete harness: {harness_id}")
        if assessments[harness_id]["status"] == "proposed":
            raise SystemExit(f"reassessment history cannot reference proposed assessment: {harness_id}")
        if not round_id.startswith("R") or not round_id[1:].isdigit():
            raise SystemExit(f"invalid reassessment round id: {round_id}")
        if row["outcome"] not in REASSESSMENT_OUTCOMES:
            raise SystemExit(f"{round_id}/{harness_id}: invalid outcome {row['outcome']}")
        for ref_key in ("previous_review_ref", "checked_ref", "accepted_review_ref"):
            if len(row[ref_key]) != 40:
                raise SystemExit(f"{round_id}/{harness_id}: {ref_key} must be 40 characters")
        try:
            date.fromisoformat(row["checked_at"])
        except ValueError as exc:
            raise SystemExit(f"{round_id}/{harness_id}: checked_at must be YYYY-MM-DD") from exc
        for version_key in ("profile_version", "assessment_procedure_version"):
            if not SEMVER_RE.fullmatch(row[version_key]):
                raise SystemExit(
                    f"{round_id}/{harness_id}: {version_key} must be a semantic version such as 0.2.0"
                )

        previous = latest_event.get(harness_id)
        if previous and row["previous_review_ref"] != previous["accepted_review_ref"]:
            raise SystemExit(
                f"{round_id}/{harness_id}: previous_review_ref does not continue prior accepted boundary"
            )

        outcome = row["outcome"]
        if outcome in {"no-upstream-change", "no-material-change", "blocked"}:
            if row["accepted_review_ref"] != row["previous_review_ref"]:
                raise SystemExit(
                    f"{round_id}/{harness_id}: {outcome} cannot advance accepted_review_ref"
                )
        elif outcome == "same-ref-correction":
            if row["checked_ref"] != row["previous_review_ref"] or row["accepted_review_ref"] != row["previous_review_ref"]:
                raise SystemExit(
                    f"{round_id}/{harness_id}: same-ref correction must keep the review boundary"
                )
        elif outcome in {"reassessed-unchanged", "reassessed-changed"}:
            if row["accepted_review_ref"] != row["checked_ref"]:
                raise SystemExit(
                    f"{round_id}/{harness_id}: accepted new-ref reassessment must use checked_ref"
                )
            if row["accepted_review_ref"] == row["previous_review_ref"]:
                raise SystemExit(
                    f"{round_id}/{harness_id}: new-ref reassessment must advance the review boundary"
                )

        latest_event[harness_id] = row
        if outcome != "blocked":
            latest_successful[harness_id] = row

    for harness_id, event in latest_successful.items():
        assessment = assessments[harness_id]
        if assessment.get("last_reassessment_round") != event["round_id"]:
            raise SystemExit(f"{harness_id}: last_reassessment_round differs from latest successful history event")
        if assessment.get("last_checked_ref") != event["checked_ref"]:
            raise SystemExit(f"{harness_id}: last_checked_ref differs from latest successful history event")
        if assessment.get("last_checked_at") != event["checked_at"]:
            raise SystemExit(f"{harness_id}: last_checked_at differs from latest successful history event")
        if assessment["review_ref"] != event["accepted_review_ref"]:
            raise SystemExit(f"{harness_id}: canonical review_ref differs from latest successful reassessment ref")
        if assessment.get("profile_version") != event["profile_version"]:
            raise SystemExit(f"{harness_id}: profile_version differs from latest successful reassessment event")
        if assessment.get("assessment_procedure_version") != event["assessment_procedure_version"]:
            raise SystemExit(
                f"{harness_id}: assessment_procedure_version differs from latest successful reassessment event"
            )

    for harness_id, event in latest_event.items():
        if event["outcome"] != "blocked":
            continue
        assessment = assessments[harness_id]
        if assessment["review_ref"] != event["accepted_review_ref"]:
            raise SystemExit(f"{harness_id}: blocked event cannot change canonical review_ref")


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    catalog_rows = read_psv(repo / "data" / "catalog.psv")
    positions = [int(row["catalog_position"]) for row in catalog_rows]
    if positions != list(range(1, len(catalog_rows) + 1)):
        raise SystemExit("catalog positions must be contiguous from 1")
    if len({row["harness_id"] for row in catalog_rows}) != len(catalog_rows):
        raise SystemExit("catalog harness_id values must be unique")
    by_id = {row["harness_id"]: row for row in catalog_rows}

    assessments = load_assessments(repo / "assessments")
    canonical_assessments: dict[str, dict[str, str]] = {}
    for harness_id, assessment in assessments.items():
        validate_assessment(assessment)
        source = by_id.get(harness_id)
        if assessment["status"] == "proposed":
            # Proposed is an intake/review artifact, not an admitted Index fact.
            # It may coexist with an older catalog record while deep review
            # updates the project label, repository target, or pinned ref. Cross-
            # artifact equality is therefore intentionally deferred to admission,
            # where the accepted proposal must update/agree with catalog atomically.
            continue
        if source is None:
            raise SystemExit(f"canonical assessment missing catalog row: {harness_id}")
        for key in ("project_name", "repository", "review_ref"):
            if assessment[key] != source[key]:
                raise SystemExit(f"{harness_id}: {key} differs from catalog")
        canonical_assessments[harness_id] = assessment

    # Admission is intentionally sparse with respect to catalog_position. The
    # catalog is an immutable discovery/order ledger, while proposed assessments
    # can remain unresolved as later positions are admitted. If an earlier
    # proposal is admitted later, cohort-relative signatures at later positions
    # must be re-synthesized; repository-relative assessments do not move.

    reassessment_history = read_psv(repo / "data" / "reassessment-history.psv")
    validate_reassessment_history(reassessment_history, by_id, canonical_assessments)

    signatures = read_psv(repo / "data" / "signatures.psv")
    signature_ids = {row["harness_id"] for row in signatures}
    included = {h for h, row in canonical_assessments.items() if row["status"] == "included"}
    if signature_ids != included:
        signature_only = sorted(signature_ids - included)
        missing_signatures = sorted(included - signature_ids)
        raise SystemExit(
            "signatures must cover exactly included canonical assessments; "
            f"signature_only={signature_only}; missing_signatures={missing_signatures}"
        )
    for row in signatures:
        if int(row["catalog_position"]) != int(by_id[row["harness_id"]]["catalog_position"]):
            raise SystemExit(f"{row['harness_id']}: signature position mismatch")

    generated = {repo / "TLDR.md": render_tldr(repo), repo / "RANKINGS.md": render_rankings(repo)}
    for path, expected in generated.items():
        if not path.exists() or path.read_text(encoding="utf-8") != expected:
            raise SystemExit(f"{path.name} is stale; run scripts/render_tldr.py")
    proposed_count = sum(1 for row in assessments.values() if row["status"] == "proposed")
    print(
        f"Validated {len(canonical_assessments)} canonical assessment(s), {proposed_count} proposed intake assessment(s), "
        f"{len(reassessment_history)} reassessment event(s) across {len(catalog_rows)} catalog candidates"
    )
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

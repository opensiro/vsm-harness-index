#!/usr/bin/env python3
"""Fail-closed validator for the self-organizing-autonomy fixture coverage snapshot."""

from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
STATUS_PATH = HERE / "corpus-status.json"
DOC_PATH = HERE / "CORPUS-STATUS.md"
STATUS = json.loads(STATUS_PATH.read_text(encoding="utf-8"))
DOC = DOC_PATH.read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


CURRENT_SKILLS = "8ab5fcbcb96e38eb02be4a6157c5d4a48cd39b23"
SNAPSHOT = "0ec71f3dddb16b5eb61d624a13420561a69a74da"
REQUIRED = {
    "clear-c": "chief",
    "clear-a": "trueforge",
    "self-modifying-non-s": "harness-evolver",
    "escalation-boundary-shift": "synthetic-s1-escalation-shift",
    "repertoire-change-non-recursive": "scion",
    "recursive-realization": "megaagent",
    "s3star-counterexample": "synthetic-s3star-independence-loss",
    "s5-counterexample": "synthetic-s5-parent-authority",
}

require(STATUS["schema_version"] == 1, "corpus-status schema_version drift")
require(STATUS["status"] == "experimental-non-normative", "corpus status boundary drift")
require(STATUS["tracking_issue"] == 732, "tracking issue drift")
require(STATUS["snapshot_index_revision"] == SNAPSHOT, "frozen Index snapshot drift")
require(
    STATUS["current_skills_contract"]["revision"] == CURRENT_SKILLS,
    "current Skills contract revision drift",
)
require(
    STATUS["current_skills_contract"]["fixtures_path"]
    == "experiments/self-organizing-autonomy/FIXTURES.md",
    "Skills fixture contract path drift",
)

summary = STATUS["summary"]
require(summary["required_fixture_class_count"] == 8, "required fixture-class count drift")
require(summary["required_fixture_classes_with_frozen_packet"] == 8, "frozen packet count drift")
require(summary["packet_class_coverage_complete"] is True, "packet coverage must be complete")
require(summary["uniform_current_protocol_alignment"] is False, "protocol alignment must remain explicitly incomplete")
require(summary["independent_review_complete"] is False, "independent reviews are not complete")
require(summary["reproducibility_grade_corpus"] is False, "corpus is not yet reproducibility-grade")
require(summary["stability_gates_complete"] is False, "stability gates are not complete")
require(summary["experiment_stable"] is False, "experiment must remain non-stable")

rows = STATUS["required_classes"]
require(len(rows) == 8, "required class row count drift")
actual = {row["class_id"]: row["fixture_id"] for row in rows}
require(actual == REQUIRED, "required class-to-fixture mapping drift")

for row in rows:
    packet_path = HERE / row["fixture_path"]
    require(packet_path.is_file(), f"missing frozen packet: {row['fixture_path']}")
    packet = packet_path.read_text(encoding="utf-8")
    require(row["packet_status"] == "frozen", f"packet status drift: {row['class_id']}")
    require(
        row["pinned_skills_revision"] in packet,
        f"packet does not contain declared pinned Skills revision: {row['class_id']}",
    )
    require(
        row["review_status"] != "complete",
        f"coverage snapshot must not silently claim completed review: {row['class_id']}",
    )
    if row["pinned_skills_revision"] == CURRENT_SKILLS:
        require(
            row["current_protocol_alignment"] == "current",
            f"current-protocol packet mislabeled: {row['class_id']}",
        )
    else:
        require(
            row["current_protocol_alignment"] == "not-revalidated-against-current-revision",
            f"older packet must retain explicit protocol-drift boundary: {row['class_id']}",
        )

additional = STATUS["additional_candidates"]
require(len(additional) == 1, "additional candidate set drift")
ouroboros = additional[0]
require(ouroboros["fixture_id"] == "ouroboros", "Ouroboros additional candidate missing")
require(ouroboros["required_class_slot"] is None, "Ouroboros must not silently fill a required class slot")
require((HERE / ouroboros["fixture_path"]).is_file(), "Ouroboros packet missing")

for phrase in (
    "required fixture classes represented: 8 / 8",
    "uniform current-protocol alignment: no",
    "independent-review completion: no",
    "reproducibility-grade corpus: no",
    "experiment stable: no",
    "8 / 8 packet classes",
    "must never be summarized as",
    "canonical assessments",
):
    require(phrase in DOC, f"CORPUS-STATUS.md lost required boundary text: {phrase}")

for claim in STATUS["non_claims"]:
    require(claim, "empty non-claim entry")
require(
    any("current-protocol alignment" in claim for claim in STATUS["non_claims"]),
    "protocol-alignment non-claim missing",
)
require(
    any("real public harness" in gate for gate in STATUS["remaining_gates"]),
    "real-system positive-witness stability gate missing",
)
require(
    any("parent-governed" in gate for gate in STATUS["remaining_gates"]),
    "parent-governed composition gate missing",
)

print("self-organizing autonomy corpus status validation passed")

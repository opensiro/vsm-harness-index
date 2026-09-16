#!/usr/bin/env python3
"""Validate the machine-readable Profile/procedure/Index compatibility contract."""

from __future__ import annotations

import json
from pathlib import Path

from validate_tldr import (
    FRESHNESS_KEYS,
    GENERATION_PROVENANCE_KEYS,
    SEMVER_RE,
    SPEC_PROVENANCE_KEYS,
)


SCHEMA_ID = "assessment-frontmatter"
SCHEMA_REVISION = 1
RELEASE_FLAGS = ("planned", "merged", "tagged", "active_for_new_assessments")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def require_semver(value: object, label: str) -> str:
    require(isinstance(value, str) and bool(SEMVER_RE.fullmatch(value)), f"{label} must be semantic version")
    return value


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    path = repo / "compatibility.json"
    data = json.loads(path.read_text(encoding="utf-8"))

    require(data.get("contract_version") == 1, "unsupported compatibility contract_version")

    schema = data.get("index_schema", {})
    require(schema.get("id") == SCHEMA_ID, f"index schema id must be {SCHEMA_ID}")
    require(schema.get("revision") == SCHEMA_REVISION, f"index schema revision must be {SCHEMA_REVISION}")

    metadata = schema.get("metadata_contract", {})
    require(
        metadata.get("current_semantic_provenance_pair") == list(SPEC_PROVENANCE_KEYS),
        "compatibility current semantic provenance fields differ from Index parser",
    )
    require(
        metadata.get("generation_origin_pair") == list(GENERATION_PROVENANCE_KEYS),
        "compatibility generation provenance fields differ from Index parser",
    )
    require(
        metadata.get("reassessment_freshness_group") == list(FRESHNESS_KEYS),
        "compatibility reassessment freshness fields differ from Index parser",
    )
    require(
        metadata.get("generation_origin_immutable_once_recorded") is True,
        "compatibility contract must declare recorded generation provenance immutable",
    )
    require(
        metadata.get("legacy_generation_omission_allowed") is True,
        "compatibility contract must preserve unknown legacy generation provenance",
    )

    active = data.get("active_for_new_assessments", {})
    active_profile = require_semver(active.get("profile_version"), "active profile_version")
    active_procedure = require_semver(
        active.get("assessment_procedure_version"), "active assessment_procedure_version"
    )
    require(
        active.get("index_schema_revision") == SCHEMA_REVISION,
        "active compatibility pair must use current Index schema revision",
    )

    supported = data.get("supported_pairs")
    require(isinstance(supported, list) and bool(supported), "supported_pairs must be a non-empty list")
    active_matches = 0
    seen: set[tuple[str, str, int]] = set()
    for entry in supported:
        require(isinstance(entry, dict), "supported_pairs entries must be objects")
        profile = require_semver(entry.get("profile_version"), "supported profile_version")
        procedure = require_semver(
            entry.get("assessment_procedure_version"), "supported assessment_procedure_version"
        )
        revision = entry.get("index_schema_revision")
        require(revision == SCHEMA_REVISION, "supported pair references unknown Index schema revision")
        key = (profile, procedure, revision)
        require(key not in seen, f"duplicate compatibility pair: {key}")
        seen.add(key)
        require(
            isinstance(entry.get("active_for_new_assessments"), bool),
            f"compatibility pair {key} must declare active_for_new_assessments",
        )
        if key == (active_profile, active_procedure, SCHEMA_REVISION):
            require(
                entry["active_for_new_assessments"] is True,
                "top-level active compatibility pair is not active in supported_pairs",
            )
            active_matches += 1
    require(active_matches == 1, "top-level active compatibility pair must appear exactly once")

    release = data.get("release_state", {})
    require(set(release) == {"profile", "assessment_procedure", "index_schema"}, "release_state components mismatch")
    require(release["profile"].get("version") == active_profile, "Profile release state version mismatch")
    require(
        release["assessment_procedure"].get("version") == active_procedure,
        "procedure release state version mismatch",
    )
    require(
        release["index_schema"].get("revision") == SCHEMA_REVISION,
        "Index schema release state revision mismatch",
    )
    for component, state in release.items():
        for flag in RELEASE_FLAGS:
            require(isinstance(state.get(flag), bool), f"{component}: release flag {flag} must be boolean")
        if state["active_for_new_assessments"]:
            require(state["planned"] and state["merged"], f"{component}: active release must be planned and merged")

    print(
        "Validated compatibility contract: "
        f"Profile {active_profile} / procedure {active_procedure} / {SCHEMA_ID} r{SCHEMA_REVISION}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

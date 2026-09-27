from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EXP = ROOT / "experiments" / "functional-capability-depth"
RAW = EXP / "system-observations"
S2 = EXP / "s2-system-benchmarks"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def by_id(rows: list[dict], observation_id: str) -> dict:
    matches = [row for row in rows if row.get("observation_id") == observation_id]
    assert len(matches) == 1, (observation_id, len(matches))
    return matches[0]


# 1) Generalize generated neutral registry from benchmark-only labels to generic evidence surfaces.
renderer_path = RAW / "render_registry.py"
text = renderer_path.read_text(encoding="utf-8")
text = text.replace(
    '"""Render the neutral benchmark <-> system observation registry from raw JSON records."""',
    '"""Render the neutral public-evidence <-> system observation registry from raw JSON records."""',
    1,
)
text = text.replace("benchmark_labels: str", "evidence_surfaces: str", 1)
text = text.replace("def _benchmarks(observation: dict, record_ref: str) -> list[str]:", "def _evidence_surfaces(observation: dict, record_ref: str) -> list[str]:", 1)

anchor = '''    benchmark_results = observation.get("benchmark_results")
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
'''
assert anchor in text
replacement = '''    benchmark_results = observation.get("benchmark_results")
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
'''
text = text.replace(anchor, replacement, 1)
text = text.replace(
    'f"{record_ref}:{observation.get(\'observation_id\')}: no benchmark identity is recoverable"',
    'f"{record_ref}:{observation.get(\'observation_id\')}: no public evidence-surface identity is recoverable"',
    1,
)
text = text.replace("benchmarks = _benchmarks(observation, record_ref)", "surfaces = _evidence_surfaces(observation, record_ref)", 1)
text = text.replace('"; ".join(benchmarks),', '"; ".join(surfaces),', 1)
text = text.replace('benchmark_labels="; ".join(benchmarks),', 'evidence_surfaces="; ".join(surfaces),', 1)
text = text.replace('"benchmark_labels",', '"evidence_surfaces",', 1)
text = text.replace("row.benchmark_labels,", "row.evidence_surfaces,", 2)
text = text.replace('"# Benchmark ↔ system observation registry",', '"# Public evidence ↔ system observation registry",', 1)
text = text.replace(
    '"Numeric benchmark payloads remain only in the raw record; this table is an identity/provenance projection, not a second result database.",',
    '"Raw evidence payloads remain only in the raw record; this table is an identity/provenance projection, not a second result database.",',
    1,
)
text = text.replace("| System | Canonical harness | Observation | Benchmark surface(s) | Kind | Provenance | Compatibility | Raw record |", "| System | Canonical harness | Observation | Evidence surface(s) | Kind | Provenance | Compatibility | Raw record |", 1)
text = text.replace('print(f"rendered {len(rows)} neutral benchmark-system observations")', 'print(f"rendered {len(rows)} neutral public-evidence system observations")', 1)
renderer_path.write_text(text, encoding="utf-8")

validate_path = RAW / "validate.py"
text = validate_path.read_text(encoding="utf-8")
text = text.replace('"""Validate the neutral public benchmark <-> system observation registry."""', '"""Validate the neutral public-evidence <-> system observation registry."""', 1)
text = text.replace('print("ok: neutral benchmark-system registry validated")', 'print("ok: neutral public-evidence system registry validated")', 1)
validate_path.write_text(text, encoding="utf-8")

# 2) Migrate the two descriptive operational S2 witnesses without inventing benchmark identities.
obs_path = S2 / "observations.json"
rows = load(obs_path)

squad_id = "squad-shared-state-conflict-attenuation-2026-03"
squad = by_id(rows, squad_id)
assert squad.get("benchmark_id") is None
assert "raw_observation_ref" not in squad
squad_raw = {
    "schema_version": 1,
    "recorded_at": "2026-09-27",
    "evidence_source_class": squad["evidence_source_class"],
    "system_name": "Squad",
    "canonical_harness_id": "squad",
    "canonical_assessment_ref": "assessments/squad.md",
    "canonical_review_ref": squad["canonical_assessment_ref"],
    "canonical_states_at_review": {"S2": squad["canonical_state_at_review"]},
    "published_implementation": {
        "system_compatibility": squad["system_compatibility"],
        "source_revision": squad["canonical_assessment_ref"],
        "historical_relation": "The cited operational commits and public case study are preserved as historical evidence linked to the canonical Squad lineage; the raw record does not assign VSM-function meaning.",
    },
    "primary_sources": squad["primary_sources"],
    "observations": [
        {
            "observation_id": squad_id,
            "kind": "operational-history-witness",
            "evidence_surface": squad["evidence_surface"],
            "comparison_class": squad["comparison_class"],
            "operational_commits": squad["operational_commits"],
            "case_study_date": squad["case_study_date"],
            "observed_events": [
                "First-party history records consolidation of per-agent decision inboxes into canonical project decision state.",
                "Later first-party multi-PR release work continues with shared team state preserved through the documented merge behavior.",
            ],
            "comparison_limitation": squad["comparison_limitation"],
        }
    ],
}
dump(RAW / "squad-operational-history.json", squad_raw)

th_id = "thclaws-team-workspace-interference-attenuation-2026"
th = by_id(rows, th_id)
assert th.get("benchmark_id") is None
assert "raw_observation_ref" not in th
th_raw = {
    "schema_version": 1,
    "recorded_at": "2026-09-27",
    "evidence_source_class": th["evidence_source_class"],
    "system_name": "thClaws",
    "canonical_harness_id": "thclaws",
    "canonical_assessment_ref": "assessments/thclaws.md",
    "canonical_review_ref": th["canonical_assessment_ref"],
    "canonical_states_at_review": {"S2": th["canonical_state_at_review"]},
    "published_implementation": {
        "system_compatibility": th["system_compatibility"],
        "source_revision": th["canonical_assessment_ref"],
        "historical_relation": "The cited incidents, hardening commits, assessed runtime source and later Agent Teams reports are preserved as one first-party operational evidence lineage; the raw record does not assign VSM-function meaning.",
    },
    "primary_sources": th["primary_sources"],
    "observations": [
        {
            "observation_id": th_id,
            "kind": "operational-history-witness",
            "evidence_surface": th["evidence_surface"],
            "comparison_class": th["comparison_class"],
            "operational_commits": th["operational_commits"],
            "operational_issues": th["operational_issues"],
            "observed_events": [
                "First-party history records a cross-branch hard reset wiping another teammate worktree and destructive workspace operations terminating teammate worktrees/processes.",
                "The assessed runtime applies role-specific command guards before shell execution and includes bounded retry handling for the shared git index-lock race.",
                "Later first-party Agent Teams reports show teammates booting, changing status, exchanging mailbox messages, and participating in task and shutdown lifecycle.",
            ],
            "comparison_limitation": th["comparison_limitation"],
        }
    ],
}
dump(RAW / "thclaws-operational-history.json", th_raw)

# Keep function interpretation in the S2 layer; remove duplicated operational evidence identity/payload.
for row, filename in ((squad, "squad-operational-history.json"), (th, "thclaws-operational-history.json")):
    row["raw_observation_ref"] = f"../system-observations/{filename}#{row['observation_id']}"
    for key in ("evidence_surface", "operational_commits", "case_study_date", "operational_issues"):
        row.pop(key, None)
dump(obs_path, rows)

# 3) Bring generated registry tests onto generic evidence-surface naming.
test_path = ROOT / "tests" / "test_system_observation_registry.py"
text = test_path.read_text(encoding="utf-8")
text = text.replace('self.assertIn("benchmark_labels", fields)', 'self.assertIn("evidence_surfaces", fields)', 1)
text = text.replace('"benchmark_labels",', '"evidence_surfaces",', 1)
test_path.write_text(text, encoding="utf-8")

# Replace the temporary exclusion assertion introduced by #797 with the now-supported operational migration contract.
s2_test_path = ROOT / "tests" / "test_s2_neutral_registry_migration_797.py"
text = s2_test_path.read_text(encoding="utf-8")
old = '''    def test_descriptive_nonbenchmark_witnesses_remain_function_specific(self) -> None:
        squad = by_id(self.derived, "squad-shared-state-conflict-attenuation-2026-03")
        thclaws = by_id(self.derived, "thclaws-team-workspace-interference-attenuation-2026")
        self.assertNotIn("raw_observation_ref", squad)
        self.assertNotIn("raw_observation_ref", thclaws)
        self.assertIsNone(squad.get("benchmark_id"))
        self.assertIsNone(thclaws.get("benchmark_id"))
'''
assert old in text
new = '''    def test_descriptive_nonbenchmark_witnesses_reference_neutral_operational_records(self) -> None:
        squad = by_id(self.derived, "squad-shared-state-conflict-attenuation-2026-03")
        thclaws = by_id(self.derived, "thclaws-team-workspace-interference-attenuation-2026")
        self.assertEqual(
            squad["raw_observation_ref"],
            "../system-observations/squad-operational-history.json#squad-shared-state-conflict-attenuation-2026-03",
        )
        self.assertEqual(
            thclaws["raw_observation_ref"],
            "../system-observations/thclaws-operational-history.json#thclaws-team-workspace-interference-attenuation-2026",
        )
        self.assertIsNone(squad.get("benchmark_id"))
        self.assertIsNone(thclaws.get("benchmark_id"))
        for row in (squad, thclaws):
            self.assertNotIn("evidence_surface", row)
            self.assertNotIn("operational_commits", row)
'''
text = text.replace(old, new, 1)
s2_test_path.write_text(text, encoding="utf-8")

# Dedicated regression for non-benchmark neutral evidence surfaces.
new_test = ROOT / "tests" / "test_operational_evidence_surfaces_799.py"
new_test.write_text('''from __future__ import annotations

import csv
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "experiments" / "functional-capability-depth" / "system-observations"


def load(name: str) -> dict:
    return json.loads((RAW / name).read_text(encoding="utf-8"))


class OperationalEvidenceSurfaces799Tests(unittest.TestCase):
    def test_operational_records_are_neutral_and_nonbenchmark(self) -> None:
        expected = {
            "squad-operational-history.json": "squad-shared-state-conflict-attenuation-2026-03",
            "thclaws-operational-history.json": "thclaws-team-workspace-interference-attenuation-2026",
        }
        for filename, observation_id in expected.items():
            record = load(filename)
            self.assertEqual(len(record["observations"]), 1)
            observation = record["observations"][0]
            self.assertEqual(observation["observation_id"], observation_id)
            self.assertTrue(observation["evidence_surface"])
            self.assertNotIn("benchmark", observation)
            self.assertNotIn("benchmark_results", observation)
            for forbidden in ("function", "benchmark_fit", "vsm_interpretation"):
                self.assertNotIn(forbidden, record)
                self.assertNotIn(forbidden, observation)

    def test_generated_registry_uses_generic_evidence_surface_field(self) -> None:
        with (RAW / "registry.psv").open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle, delimiter="|"))
        self.assertTrue(rows)
        self.assertIn("evidence_surfaces", rows[0])
        self.assertNotIn("benchmark_labels", rows[0])
        by_id = {row["observation_id"]: row for row in rows}
        self.assertIn("repository history", by_id["squad-shared-state-conflict-attenuation-2026-03"]["evidence_surfaces"])
        self.assertIn("operational", by_id["thclaws-team-workspace-interference-attenuation-2026"]["evidence_surfaces"].lower())

    def test_existing_benchmark_rows_still_project_as_evidence_surfaces(self) -> None:
        with (RAW / "registry.psv").open(encoding="utf-8", newline="") as handle:
            rows = {row["observation_id"]: row for row in csv.DictReader(handle, delimiter="|")}
        self.assertEqual(
            rows["grit-synthetic-merge-contention-2026-04"]["evidence_surfaces"],
            "Grit synthetic merge-contention sweep",
        )
        self.assertEqual(
            rows["squad-marble-completion-ablation"]["evidence_surfaces"],
            "MARBLE factorial ablation",
        )


if __name__ == "__main__":
    unittest.main()
''', encoding="utf-8")

# 4) Minimal contract/doc alignment: benchmark is one evidence-surface type, not a universal requirement.
contract = EXP / "BENCHMARK-SYSTEM-REGISTRY.md"
text = contract.read_text(encoding="utf-8")
old = "- **benchmark identity** — family, version/variant, task set/split, metric;"
assert old in text
text = text.replace(old, "- **evidence-surface identity** — benchmark family/version/task split when benchmarked, or an explicit paper/repository/operational surface when not benchmark-based;", 1)
anchor = "## Result provenance classes\n"
assert anchor in text
insert = '''## Non-benchmark evidence surfaces

The neutral layer also accepts public system evidence that is not a benchmark result, such as immutable repository history, public operational incident/case-study evidence, or another explicitly named evidence surface.

Such an observation MUST use `evidence_surface` or `evidence_surfaces` rather than inventing a benchmark label. Function-specific interpretation remains downstream exactly as it does for benchmark observations.

'''
text = text.replace(anchor, insert + anchor, 1)
contract.write_text(text, encoding="utf-8")

readme = RAW / "README.md"
text = readme.read_text(encoding="utf-8")
old = "what benchmark/version was used?"
assert old in text
text = text.replace(old, "what public evidence surface was used (benchmark, paper, repository history, operational evidence)?", 1)
readme.write_text(text, encoding="utf-8")

public = EXP / "PUBLIC-EVIDENCE.md"
text = public.read_text(encoding="utf-8")
old = "2. identify the benchmark family, version, task set/split, metric, model, and published system configuration;"
assert old in text
text = text.replace(old, "2. identify the public evidence surface; for benchmarked results preserve family, version, task set/split, metric, model and published system configuration; for non-benchmark evidence preserve the explicit repository/paper/operational surface identity;", 1)
public.write_text(text, encoding="utf-8")

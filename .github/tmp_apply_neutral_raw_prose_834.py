from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "experiments" / "functional-capability-depth" / "system-observations"
RENDER = RAW / "render_registry_core.py"
TESTS = ROOT / "tests"
BASE_REF = "8fb9de2275d7b2f2df57d7a0785fd466f710d5dc"

TOKEN_RE = re.compile(
    r"(?<![A-Za-z0-9])(?:S3\*|S[1-5]|VSM|Viable System Model)(?![A-Za-z0-9])",
    re.IGNORECASE,
)

# Exact, reviewed old -> new mappings. Do not broaden this into a regex rewrite.
MAPPINGS = [
    (
        "a-evolve.json", "$.observations[0].metric_note",
        "The publication defines harness-updating capability as mean pairwise evolution gain across fixed anchor agents and reports pass-rate gains in percentage points. These values are preserved as a vector of reported observations, not collapsed into a global S4 score.",
        "The publication defines harness-updating capability as mean pairwise evolution gain across fixed anchor agents and reports pass-rate gains in percentage points. These values are preserved as a vector of reported observations, not collapsed into a single global capability score.",
    ),
    (
        "a-evolve.json", "$.observations[0].non_claim",
        "These heterogeneous gains are not a global harness score and do not determine canonical VSM autonomy states.",
        "These heterogeneous gains are not a global harness score and do not determine downstream canonical organizational classifications.",
    ),
    (
        "appliedscientist.json", "$.observations[0].external_validation_surface",
        "Stanford Reviewer scores saved human-initialized versions independently and is never shown to the Scientist; it is supporting validation, not the native S3* owner.",
        "Stanford Reviewer scores saved human-initialized versions independently and is never shown to the Scientist; it is supporting validation, not the owner of the native independent-review loop.",
    ),
    (
        "appliedscientist.json", "$.observations[0].comparison_scope_note",
        "The paper compares reviewer-guided revision with fixed-prompt self-revision inside AppliedScientist. The weakness-resolution counts are aggregate closure evidence for the native review-guided loop, not a matched cross-harness S3* score.",
        "The paper compares reviewer-guided revision with fixed-prompt self-revision inside AppliedScientist. The weakness-resolution counts are aggregate closure evidence for the native review-guided loop, not a matched cross-harness independent-review score.",
    ),
    (
        "appliedscientist.json", "$.observations[0].non_claim",
        "This result does not establish a cross-harness ranking, does not prove an exact run revision, and does not determine any canonical VSM autonomy state.",
        "This result does not establish a cross-harness ranking, does not prove an exact run revision, and does not determine any downstream canonical organizational classification.",
    ),
    (
        "claude-code-benchmark-results-external-reproduced-adapter-preserved.json", "$.observations[0].notes",
        "FrontierHarness pins historical Claude Code 2.1.237 and preserves the first-party operational loop behind an external Runta/Harbor evaluation membrane. The 30-task mix is broader than pure SWE but remains a technical Coding/SWE projection, not universal S1 capability. The published baseline did not record its applied egress allowlist; future reproductions require a matched control for methodology comparability. No higher VSM function, ownership state, or self-organizing S claim is inferred.",
        "FrontierHarness pins historical Claude Code 2.1.237 and preserves the first-party operational loop behind an external Runta/Harbor evaluation membrane. The 30-task mix is broader than pure SWE but remains a technical Coding/SWE projection, not universal operational capability. The published baseline did not record its applied egress allowlist; future reproductions require a matched control for methodology comparability. No broader organizational-function, ownership-state, or self-organizing claim is inferred.",
    ),
    (
        "codex-benchmark-results-external-reproduced-adapter-preserved.json", "$.observations[0].notes",
        "Harbor's installed Codex agent explicitly uses OpenAI's Codex CLI and installs the requested @openai/codex version. The parity result is therefore adapter-preserved S1 evidence rather than a Harbor-owned substitute agent loop. Historical version differs from the current canonical assessment revision.",
        "Harbor's installed Codex agent explicitly uses OpenAI's Codex CLI and installs the requested @openai/codex version. The parity result is therefore adapter-preserved operational evidence rather than a Harbor-owned substitute agent loop. Historical version differs from the current canonical assessment revision.",
    ),
    (
        "codex-benchmark-results-external-reproduced-adapter-preserved.json", "$.observations[3].notes",
        "FrontierHarness pins historical Codex 0.148.0 and preserves the first-party operational loop behind an external Runta/Harbor evaluation membrane. This mixed technical task set contains 21 Terminal-Bench and 9 DeepSWE tasks, so it is Coding/SWE-domain evidence rather than universal S1 capability. The published baseline did not record its applied egress allowlist; future reproduction runs need a matched control before claiming methodology comparability. No S2-S5, ownership, or self-organizing S inference follows from this result.",
        "FrontierHarness pins historical Codex 0.148.0 and preserves the first-party operational loop behind an external Runta/Harbor evaluation membrane. This mixed technical task set contains 21 Terminal-Bench and 9 DeepSWE tasks, so it is Coding/SWE-domain evidence rather than universal operational capability. The published baseline did not record its applied egress allowlist; future reproduction runs need a matched control before claiming methodology comparability. No broader organizational-function, ownership, or self-organizing inference follows from this result.",
    ),
    (
        "data-to-paper-review-revision.json", "$.observations[0].metric_note",
        "The publication demonstrates native reviewer-feedback-to-revision closure but does not report an aggregate S3*-specific detection, correction, or re-verification score for this loop.",
        "The publication demonstrates native reviewer-feedback-to-revision closure but does not report an aggregate independent-review-specific detection, correction, or re-verification score for this loop.",
    ),
    (
        "data-to-paper-review-revision.json", "$.observations[0].comparison_scope_note",
        "This is a direct descriptive within-system closure witness. It is not a quantitative comparison with AppliedScientist or any other harness and must not be normalized into a common S3* score.",
        "This is a direct descriptive within-system closure witness. It is not a quantitative comparison with AppliedScientist or any other harness and must not be normalized into a common independent-review score.",
    ),
    (
        "evoharnessbench.json", "$.observations[0].mode_boundary",
        "Only self-evolving adaptation is classified direct. Deployment-only evaluation without persistent inner adaptation is a retention/robustness control, not direct S4.",
        "Only self-evolving adaptation is classified direct. Deployment-only evaluation without persistent inner adaptation is a retention/robustness control, not direct adaptation evidence.",
    ),
    (
        "govsim-selfgovern.json", "$.observations[0].broader_g1_result.scope_note",
        "This aggregate governance gain mixes multiple mechanisms and is not an S5-only effect.",
        "This aggregate governance gain mixes multiple mechanisms and is not attributable to membership-policy authority alone.",
    ),
    (
        "harness-bench-pilot4.json", "$.observations[0].publisher_boundary_note",
        "The README describes the benchmark reviewer/harness as a minimal clean-room implementation of production patterns rather than production Telos code. No native Telos or Claude Code S3* ownership is inferred.",
        "The README describes the benchmark reviewer/harness as a minimal clean-room implementation of production patterns rather than production Telos code. No native Telos or Claude Code independent-review ownership is inferred.",
    ),
    (
        "hermes-agent-benchmark-results-external-reproduced-adapter-preserved.json", "$.observations[0].notes",
        "Pinned PawBench adapter code installs Hermes Agent 2026.4.23 and runs the native hermes CLI. This is historical adapter-preserved S1 evidence relative to the current canonical September 2026 review ref. PawBench capability slice labels do not establish S2, S3, S3*, S4 or S5 ownership or capability by naming alone.",
        "Pinned PawBench adapter code installs Hermes Agent 2026.4.23 and runs the native hermes CLI. This is historical adapter-preserved operational evidence relative to the current canonical September 2026 review ref. PawBench capability slice labels do not establish organizational-function ownership or capability by naming alone.",
    ),
    (
        "hermes-agent-benchmark-results-external-reproduced-adapter-preserved.json", "$.observations[1].notes",
        "Claw-SWE-Bench preserves the first-party Hermes Agent operational loop behind an external adapter/evaluation membrane and uses a fresh container per instance. Historical Hermes version/revision is not published in the pinned benchmark sources and is not inferred. This is Coding/SWE-specific S1 evidence, not universal S1 capability, and it does not establish S2-S5 or self-organizing S.",
        "Claw-SWE-Bench preserves the first-party Hermes Agent operational loop behind an external adapter/evaluation membrane and uses a fresh container per instance. Historical Hermes version/revision is not published in the pinned benchmark sources and is not inferred. This is Coding/SWE-specific operational evidence, not universal operational capability, and it does not establish broader organizational-function or self-organizing claims.",
    ),
    (
        "hermes-agent-benchmark-results-external-reproduced-adapter-preserved.json", "$.observations[3].notes",
        "FrontierHarness publishes Hermes Agent 0.20.4 with exact source revision 044acf2bf700b8452e903f035406091146eb0245, so this row is exact-historical rather than merely version-known. The external benchmark membrane preserves the first-party operational loop. This mixed Terminal-Bench/DeepSWE result is Coding/SWE-domain evidence only; the historical campaign's unrecorded egress allowlist limits future reproduction comparability. No S2-S5, ownership, or self-organizing S inference follows.",
        "FrontierHarness publishes Hermes Agent 0.20.4 with exact source revision 044acf2bf700b8452e903f035406091146eb0245, so this row is exact-historical rather than merely version-known. The external benchmark membrane preserves the first-party operational loop. This mixed Terminal-Bench/DeepSWE result is Coding/SWE-domain evidence only; the historical campaign's unrecorded egress allowlist limits future reproduction comparability. No broader organizational-function, ownership, or self-organizing inference follows.",
    ),
    (
        "kadath.json", "$.observations[0].comparability_limitation",
        "The fitness benchmark is generated from the user goal and explicitly approved and locked per run. The published proof does not expose enough run metadata to reconstruct a common model/goal/population/configuration cell with A-Evolve or another canonical S4 system. Preserve this as a heterogeneous within-system observation, not a matched cross-harness score.",
        "The fitness benchmark is generated from the user goal and explicitly approved and locked per run. The published proof does not expose enough run metadata to reconstruct a common model/goal/population/configuration cell with A-Evolve or another canonical adaptation system. Preserve this as a heterogeneous within-system observation, not a matched cross-harness score.",
    ),
    (
        "kadath.json", "$.observations[0].non_claim",
        "This longitudinal within-system result is not a matched cross-harness score and does not determine canonical VSM autonomy states.",
        "This longitudinal within-system result is not a matched cross-harness score and does not determine downstream canonical organizational classifications.",
    ),
    (
        "llamar.json", "$.observations[0].non_claim",
        "These module-ablation results are proxy evidence. They do not isolate a pure S3 causal effect, do not quantify S3 capability as a scalar, and do not establish canonical S3=A, which is determined independently from repository evidence.",
        "These module-ablation results are proxy evidence. They do not isolate a pure current-control causal effect, do not quantify current-control capability as a scalar, and do not establish a downstream canonical current-control classification, which is determined independently from repository evidence.",
    ),
    (
        "llamar.json", "$.observations[1].non_claim",
        "The agent-count comparison does not disable or enable LLaMAR's native anti-blocking coordination relation and therefore is not an S2 attenuation treatment or direct S2 capability observation.",
        "The agent-count comparison does not disable or enable LLaMAR's native anti-blocking coordination relation and therefore is not a coordination-attenuation treatment or direct coordination-capability observation.",
    ),
    (
        "magentic-one.json", "$.observations[0].non_claim",
        "These end-task outcomes do not isolate S2 or S3 and must not be converted into a VSM function score.",
        "These end-task outcomes do not isolate coordination or current-control effects and must not be converted into an organizational-function score.",
    ),
    (
        "magentic-one.json", "$.observations[1].non_claim",
        "Differences from the GPT-4o-only configuration are model-configuration effects inside the same system and do not isolate a harness or VSM-function effect.",
        "Differences from the GPT-4o-only configuration are model-configuration effects inside the same system and do not isolate a harness or organizational-function effect.",
    ),
    (
        "magentic-one.json", "$.observations[2].non_claim",
        "The 31% end-task performance drop is not '31% of S2' or '31% of S3'. The ablation changes mechanisms relevant to both functions and GAIA is not a direct S2/S3 benchmark.",
        "The 31% end-task performance drop is not '31% of coordination capability' or '31% of current-control capability'. The ablation changes mechanisms relevant to both organizational functions and GAIA is not a direct coordination/current-control benchmark.",
    ),
    (
        "multi-agent-orchestration.json", "$.observations[0].non_claim",
        "This within-system ablation does not establish a cross-harness ranking and does not by itself determine any canonical VSM autonomy state.",
        "This within-system ablation does not establish a cross-harness ranking and does not by itself determine any downstream canonical organizational classification.",
    ),
    (
        "oh-my-pi-benchmark-results-external-reproduced-adapter-preserved.json", "$.observations[0].notes",
        "FrontierHarness pins historical Oh My Pi 17.4.0 while the external Runta/Harbor membrane supplies the matched runtime and evaluation boundary. This is technical Coding/SWE-domain S1 evidence only; the mixed task set and historical missing egress allowlist must remain visible when interpreting or reproducing it. No higher VSM function, ownership state, or self-organizing S claim follows from the score.",
        "FrontierHarness pins historical Oh My Pi 17.4.0 while the external Runta/Harbor membrane supplies the matched runtime and evaluation boundary. This is technical Coding/SWE-domain operational evidence only; the mixed task set and historical missing egress allowlist must remain visible when interpreting or reproducing it. No broader organizational-function, ownership-state, or self-organizing claim follows from the score.",
    ),
    (
        "omnigent-child-session-recovery.json", "$.observations[0].scope_note",
        "The SQLite latency benchmark reported on PR #7662 is not used as an S3 capability metric; the S3 observation is the recovery decision and preserved continuation of current child commitments.",
        "The SQLite latency benchmark reported on PR #7662 is not used as a current-control capability metric; the retained organizational observation is the recovery decision and preserved continuation of current child commitments.",
    ),
    (
        "openclaw-benchmark-results-external-reproduced-adapter-preserved.json", "$.observations[0].notes",
        "Pinned PawBench adapter code installs OpenClaw 2026.4.24 and runs the native openclaw CLI. The committed submission artifact reports overall=0.6779 with one missing task; PawBench README prose reports 68.2 for this cell, so the immutable submission artifact is used and the discrepancy is preserved. This is historical adapter-preserved S1 evidence; PawBench slice names do not establish any other VSM function.",
        "Pinned PawBench adapter code installs OpenClaw 2026.4.24 and runs the native openclaw CLI. The committed submission artifact reports overall=0.6779 with one missing task; PawBench README prose reports 68.2 for this cell, so the immutable submission artifact is used and the discrepancy is preserved. This is historical adapter-preserved operational evidence; PawBench slice names do not establish any other organizational function.",
    ),
    (
        "openclaw-benchmark-results-external-reproduced-adapter-preserved.json", "$.observations[1].notes",
        "Claw-SWE-Bench preserves the first-party OpenClaw operational loop behind an external adapter/evaluation membrane and runs each instance in a fresh container; OpenClaw also receives a throwaway agent per instance. Historical OpenClaw version/revision is not published in the pinned benchmark sources and is not inferred. This is Coding/SWE-specific S1 evidence, not universal S1 capability, and it does not establish S2-S5 or self-organizing S.",
        "Claw-SWE-Bench preserves the first-party OpenClaw operational loop behind an external adapter/evaluation membrane and runs each instance in a fresh container; OpenClaw also receives a throwaway agent per instance. Historical OpenClaw version/revision is not published in the pinned benchmark sources and is not inferred. This is Coding/SWE-specific operational evidence, not universal operational capability, and it does not establish broader organizational-function or self-organizing claims.",
    ),
    (
        "opencode-benchmark-results-external-reproduced-adapter-preserved.json", "$.observations[0].notes",
        "FrontierHarness pins historical OpenCode 1.18.19 and preserves the first-party operational loop behind the common benchmark membrane. The result is a Coding/SWE-domain observation across the frozen 30-task technical set, not universal S1 capability. The original campaign's applied egress allowlist was not recorded, so future reproductions are not automatically methodology-comparable. No S2-S5 or self-organizing S inference is made.",
        "FrontierHarness pins historical OpenCode 1.18.19 and preserves the first-party operational loop behind the common benchmark membrane. The result is a Coding/SWE-domain observation across the frozen 30-task technical set, not universal operational capability. The original campaign's applied egress allowlist was not recorded, so future reproductions are not automatically methodology-comparable. No broader organizational-function or self-organizing inference is made.",
    ),
    (
        "openhands-benchmark-results-external-reproduced-adapter-preserved.json", "$.observations[0].notes",
        "Harbor's installed OpenHands agent uses the first-party OpenHands tool. This parity record is adapter-preserved evidence for a historical OpenHands S1 implementation, not a measurement of the full current Agent Canvas boundary. Model-label normalization differs between Harbor's parity JSON and README and is preserved explicitly.",
        "Harbor's installed OpenHands agent uses the first-party OpenHands tool. This parity record is adapter-preserved evidence for a historical OpenHands operational implementation, not a measurement of the full current Agent Canvas boundary. Model-label normalization differs between Harbor's parity JSON and README and is preserved explicitly.",
    ),
    (
        "openhands-benchmark-results-external-reproduced-native-system.json", "$.observations[0].notes",
        "Native historical OpenHands run with an exact reproducibility commit. The current canonical OpenHands assessment boundary has since evolved to Agent Canvas plus first-party SDK/server surfaces, so this result describes historical OpenHands S1 execution and must not be treated as a score for every current first-party surface.",
        "Native historical OpenHands run with an exact reproducibility commit. The current canonical OpenHands assessment boundary has since evolved to Agent Canvas plus first-party SDK/server surfaces, so this result describes historical OpenHands operational execution and must not be treated as a score for every current first-party surface.",
    ),
    (
        "pi-benchmark-results-external-reproduced-adapter-preserved.json", "$.observations[0].notes",
        "FrontierHarness identifies this configuration as pi-responses and pins Pi 0.84.2. The external benchmark membrane controls runtime/evaluation while the first-party Pi operational loop remains the S1 implementation under test. The task mix is a Coding/SWE projection only, and the unrecorded historical egress allowlist limits future reproduction comparability without a matched control. No S2-S5 or self-organizing S inference is made.",
        "FrontierHarness identifies this configuration as pi-responses and pins Pi 0.84.2. The external benchmark membrane controls runtime/evaluation while the first-party Pi operational loop remains the operational implementation under test. The task mix is a Coding/SWE projection only, and the unrecorded historical egress allowlist limits future reproduction comparability without a matched control. No broader organizational-function or self-organizing inference is made.",
    ),
    (
        "qwenpaw-benchmark-results-first-party-reported-adapter-preserved.json", "$.observations[0].notes",
        "Pinned PawBench adapter code installs and drives first-party QwenPaw 1.1.3 and documents one fresh container per task. This is historical adapter-preserved S1 evidence relative to the current canonical September 2026 review ref. PawBench capability slice labels such as Planning, Self_Verification or Skill_Use must not be mapped directly to VSM S3, S3*, S4 or other organizational functions.",
        "Pinned PawBench adapter code installs and drives first-party QwenPaw 1.1.3 and documents one fresh container per task. This is historical adapter-preserved operational evidence relative to the current canonical September 2026 review ref. PawBench capability slice labels such as Planning, Self_Verification or Skill_Use must not be mapped directly to organizational functions by naming alone.",
    ),
    (
        "squad.json", "$.observations[0].non_claim",
        "The controlled coordination effect is native Squad evidence, but MARBLE scores broad collaborative task outcomes rather than an explicit inter-S1 interference/oscillation quantity. These values are not an S2 score and do not determine canonical S2=A.",
        "The controlled coordination effect is native Squad evidence, but MARBLE scores broad collaborative task outcomes rather than an explicit inter-worker interference/oscillation quantity. These values are not a coordination score and do not determine the downstream canonical coordination classification.",
    ),
    (
        "squad.json", "$.observations[1].non_claim",
        "Completion measures whether usable output was produced within the benchmark budget. It supports the native coordination ablation but does not directly measure VSM S2 disturbance attenuation.",
        "Completion measures whether usable output was produced within the benchmark budget. It supports the native coordination ablation but does not directly measure coordination disturbance attenuation.",
    ),
    (
        "supervisoragent-smas.json", "$.observations[0].ownership_caveat",
        "The SupervisorAgent relation is added around the base MAS. The result must not be attributed as native S3 capability of Smolagent, AWorld, OAgents or another wrapped system by association.",
        "The SupervisorAgent relation is added around the base MAS. The result must not be attributed as native current-control capability of Smolagent, AWorld, OAgents or another wrapped system by association.",
    ),
    (
        "thclaws-operational-history.json", "$.observations[0].comparison_limitation",
        "This is descriptive canonical direct evidence from operational history and first-party runtime behavior, not a matched benchmark comparison or a causal numeric uplift estimate. The incident/guard and index-race paths are concrete S2 attenuation evidence but do not make thClaws materially matched to Squad or any external benchmark family.",
        "This is descriptive canonical direct evidence from operational history and first-party runtime behavior, not a matched benchmark comparison or a causal numeric uplift estimate. The incident/guard and index-race paths are concrete interference-attenuation evidence but do not make thClaws materially matched to Squad or any external benchmark family.",
    ),
]

if len(MAPPINGS) != 37:
    raise SystemExit(f"expected 37 explicit prose mappings, got {len(MAPPINGS)}")


def path_tokens(path: str) -> list[str | int]:
    if not path.startswith("$"):
        raise ValueError(path)
    tokens: list[str | int] = []
    for key, index in re.findall(r"\.([A-Za-z0-9_]+)|\[(\d+)\]", path[1:]):
        tokens.append(key if key else int(index))
    return tokens


def get_at(root: object, path: str) -> object:
    current = root
    for token in path_tokens(path):
        current = current[token]  # type: ignore[index]
    return current


def set_at(root: object, path: str, value: object) -> None:
    tokens = path_tokens(path)
    current = root
    for token in tokens[:-1]:
        current = current[token]  # type: ignore[index]
    current[tokens[-1]] = value  # type: ignore[index]


by_file: dict[str, list[tuple[str, str, str]]] = {}
for filename, path, old, new in MAPPINGS:
    if not TOKEN_RE.search(old):
        raise SystemExit(f"{filename}:{path}: old value unexpectedly has no explicit VSM/function token")
    if TOKEN_RE.search(new):
        raise SystemExit(f"{filename}:{path}: new value still has explicit VSM/function token: {new!r}")
    by_file.setdefault(filename, []).append((path, old, new))

for filename, changes in by_file.items():
    target = RAW / filename
    data = json.loads(target.read_text(encoding="utf-8"))
    for path, old, new in changes:
        actual = get_at(data, path)
        if actual != old:
            raise SystemExit(
                f"{filename}:{path}: exact old-value precondition failed\nEXPECTED: {old!r}\nACTUAL:   {actual!r}"
            )
        set_at(data, path, new)
    target.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# Expand the neutral raw validator from key-level neutrality plus historical_relation
# to a generic prose-value ownership boundary.
text = RENDER.read_text(encoding="utf-8")
anchor = '''FORBIDDEN_VSM_KEYS = {\n    "function",\n    "benchmark_fit",\n    "vsm_interpretation",\n    "function_interpretation",\n    "mixed_function_caveat",\n    "aggregate_s3star_metric_reported",\n    "canonical_state_at_review",\n    "canonical_states_at_review",\n    "canonical_system_eligible",\n    "coverage_class",\n}\n'''
insert = anchor + '''\nNEUTRAL_PROSE_FIELDS = {\n    "historical_relation",\n    "notes",\n    "non_claim",\n    "metric_note",\n    "comparison_scope_note",\n    "scope_note",\n    "external_validation_surface",\n    "mode_boundary",\n    "publisher_boundary_note",\n    "comparability_limitation",\n    "ownership_caveat",\n    "comparison_limitation",\n}\n'''
if text.count(anchor) != 1:
    raise SystemExit("render_registry_core.py forbidden-key anchor drift")
if "NEUTRAL_PROSE_FIELDS" in text:
    raise SystemExit("render_registry_core.py prose guard already present")
text = text.replace(anchor, insert, 1)

anchor = '''            if _forbidden_vsm_key(key):\n                raise RegistryError(\n                    f"{record_ref}:{child_path}: raw neutral evidence must not encode VSM-function/state attribution"\n                )\n            _validate_vsm_neutral(child, record_ref, child_path)\n'''
insert = '''            if _forbidden_vsm_key(key):\n                raise RegistryError(\n                    f"{record_ref}:{child_path}: raw neutral evidence must not encode VSM-function/state attribution"\n                )\n            if key in NEUTRAL_PROSE_FIELDS and isinstance(child, str) and FORBIDDEN_VSM_VALUE_RE.search(child):\n                raise RegistryError(\n                    f"{record_ref}:{child_path}: neutral prose must remain implementation-independent and VSM-neutral"\n                )\n            _validate_vsm_neutral(child, record_ref, child_path)\n'''
if text.count(anchor) != 1:
    raise SystemExit("render_registry_core.py recursive neutrality anchor drift")
text = text.replace(anchor, insert, 1)
RENDER.write_text(text, encoding="utf-8")

# Regression: against the exact pre-transaction main, raw JSON may differ only at
# these 37 string leaves; all guarded prose is token-neutral afterward.
expected_targets = [(filename, path) for filename, path, _, _ in MAPPINGS]
(TESTS / "test_neutral_raw_prose_values_834.py").write_text(
    f'''from __future__ import annotations\n\nimport json\nimport re\nimport subprocess\nimport unittest\nfrom pathlib import Path\n\nROOT = Path(__file__).resolve().parents[1]\nRAW = ROOT / "experiments" / "functional-capability-depth" / "system-observations"\nBASE_REF = "{BASE_REF}"\nTOKEN_RE = re.compile(\n    r"(?<![A-Za-z0-9])(?:S3\\*|S[1-5]|VSM|Viable System Model)(?![A-Za-z0-9])",\n    re.IGNORECASE,\n)\nPROSE_FIELDS = {{\n    "historical_relation", "notes", "non_claim", "metric_note",\n    "comparison_scope_note", "scope_note", "external_validation_surface",\n    "mode_boundary", "publisher_boundary_note", "comparability_limitation",\n    "ownership_caveat", "comparison_limitation",\n}}\nEXPECTED_TARGETS = {{tuple(item) for item in {expected_targets!r}}}\n\n\ndef old_json(path: Path):\n    rel = path.relative_to(ROOT).as_posix()\n    text = subprocess.check_output(["git", "show", f"{{BASE_REF}}:{{rel}}"], cwd=ROOT, text=True)\n    return json.loads(text)\n\n\ndef leaf_diffs(before, after, path="$"):\n    if type(before) is not type(after):\n        return [(path, before, after)]\n    if isinstance(before, dict):\n        if set(before) != set(after):\n            return [(path, before, after)]\n        out = []\n        for key in before:\n            out.extend(leaf_diffs(before[key], after[key], f"{{path}}.{{key}}"))\n        return out\n    if isinstance(before, list):\n        if len(before) != len(after):\n            return [(path, before, after)]\n        out = []\n        for index, (left, right) in enumerate(zip(before, after)):\n            out.extend(leaf_diffs(left, right, f"{{path}}[{{index}}]"))\n        return out\n    return [] if before == after else [(path, before, after)]\n\n\ndef walk(value, path="$"):\n    if isinstance(value, dict):\n        for key, child in value.items():\n            child_path = f"{{path}}.{{key}}"\n            yield key, child_path, child\n            yield from walk(child, child_path)\n    elif isinstance(value, list):\n        for index, child in enumerate(value):\n            yield from walk(child, f"{{path}}[{{index}}]")\n\n\nclass NeutralRawProseValues834Tests(unittest.TestCase):\n    def test_exact_37_raw_string_leaves_changed_and_nothing_else(self):\n        actual = set()\n        for path in sorted(RAW.glob("*.json")):\n            before = old_json(path)\n            after = json.loads(path.read_text(encoding="utf-8"))\n            for json_path, old, new in leaf_diffs(before, after):\n                actual.add((path.name, json_path))\n                self.assertIsInstance(old, str, (path.name, json_path))\n                self.assertIsInstance(new, str, (path.name, json_path))\n                self.assertIsNotNone(TOKEN_RE.search(old), (path.name, json_path, old))\n                self.assertIsNone(TOKEN_RE.search(new), (path.name, json_path, new))\n        self.assertEqual(actual, EXPECTED_TARGETS)\n        self.assertEqual(len(actual), 37)\n\n    def test_all_guarded_neutral_prose_is_free_of_explicit_vsm_tokens(self):\n        hits = []\n        for path in sorted(RAW.glob("*.json")):\n            data = json.loads(path.read_text(encoding="utf-8"))\n            for key, json_path, value in walk(data):\n                if key in PROSE_FIELDS and isinstance(value, str) and TOKEN_RE.search(value):\n                    hits.append((path.name, json_path, value))\n        self.assertEqual(hits, [])\n\n\nif __name__ == "__main__":\n    unittest.main()\n''',
    encoding="utf-8",
)

print(f"prepared #834: rewrote {len(MAPPINGS)} exact neutral raw prose values across {len(by_file)} records")

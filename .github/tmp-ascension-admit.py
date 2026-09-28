from pathlib import Path
import csv
import subprocess

repo = Path(__file__).resolve().parents[1]
assessment = repo / "assessments" / "ascension.md"
text = assessment.read_text(encoding="utf-8")
old = "status: proposed"
if text.count(old) != 1:
    raise SystemExit("expected exactly one proposed status in Ascension assessment")
assessment.write_text(text.replace(old, "status: included", 1), encoding="utf-8")

catalog_path = repo / "data" / "catalog.psv"
with catalog_path.open(encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f, delimiter="|"))
if any(r["harness_id"] == "ascension" for r in rows):
    raise SystemExit("Ascension already present in catalog")
positions = [int(r["catalog_position"]) for r in rows]
if max(positions) != 286:
    raise SystemExit(f"expected catalog tail 286, got {max(positions)}")
with catalog_path.open("a", encoding="utf-8", newline="") as f:
    f.write("287|ascension|Ascension|https://github.com/AI-Ascension/sts2-harness|2026-09-02T05:59:59Z|index-addition|53312ddbb074f7c187e5f59d88b6585da797fe17|2026-09-28\n")

signature_path = repo / "data" / "signatures.psv"
with signature_path.open(encoding="utf-8", newline="") as f:
    sig_rows = list(csv.DictReader(f, delimiter="|"))
if any(r["harness_id"] == "ascension" for r in sig_rows):
    raise SystemExit("Ascension already present in signatures")
with signature_path.open("a", encoding="utf-8", newline="") as f:
    f.write("287|ascension|Ascension closes autonomous S1 through its bounded model-driven episode loop and exposes whole-run current control as constructor plus authenticated parent-governed S3. Co-op protocol does not establish qualifying S2, settlement verification remains ordinary S1 feedback rather than S3*, and no deployed S4 or S5 closure is established.\n")

for cmd in [
    ["python", "scripts/render_tldr.py"],
    ["python", "scripts/render_metrics.py"],
    ["python", "scripts/sync_metrics_readme.py"],
    ["python", "scripts/render_full_a.py"],
    ["python", "scripts/check_index.py"],
    ["python", "scripts/render_tldr.py", "--check"],
    ["python", "scripts/render_metrics.py", "--check"],
    ["python", "scripts/sync_metrics_readme.py", "--check"],
    ["python", "scripts/render_full_a.py", "--check"],
    ["python", "-m", "unittest", "discover", "-s", "tests"],
]:
    print("+", " ".join(cmd), flush=True)
    subprocess.run(cmd, cwd=repo, check=True)

from pathlib import Path
import importlib.util
import sys

workspace = Path(sys.argv[1]).resolve()
spec = importlib.util.spec_from_file_location("text_utils", workspace / "text_utils.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
slugify = module.slugify

cases = {
    "Hello World": "hello-world",
    "  Hello   World  ": "hello-world",
    "Already--Slugged": "already-slugged",
    "---A  B---": "a-b",
    "A---B   C": "a-b-c",
    "abc": "abc",
    "  123 -- Test  ": "123-test",
    "": "",
    "---": "",
}

for raw, expected in cases.items():
    actual = slugify(raw)
    if actual != expected:
        raise SystemExit(f"FAIL slugify({raw!r}): expected {expected!r}, got {actual!r}")

print("PASS")

from pathlib import Path

state = Path(".verify-state")
if not state.exists():
    state.write_text("transient-failure-observed\n", encoding="utf-8")
    print("temporary verifier unavailable; retry verification")
    raise SystemExit(75)

from text_utils import slugify

assert slugify("Hello World") == "hello-world"
assert slugify("  Hello   World  ") == "hello-world"
assert slugify("Already--Slugged") == "already-slugged"
assert slugify("---A  B---") == "a-b"

print("ok")

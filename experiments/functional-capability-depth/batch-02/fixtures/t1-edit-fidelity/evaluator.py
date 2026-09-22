from pathlib import Path
import importlib.util
import sys

workspace = Path(sys.argv[1]).resolve()
spec = importlib.util.spec_from_file_location("math_utils", workspace / "math_utils.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
clamp = module.clamp

cases = [
    ((5, 1, 10), 5),
    ((-100, 1, 10), 1),
    ((100, 1, 10), 10),
    ((10, 1, 10), 10),
    ((1, 1, 10), 1),
    ((3, 3, 3), 3),
    ((2.5, 1.0, 3.0), 2.5),
    ((9.0, 1.0, 3.0), 3.0),
]

for args, expected in cases:
    actual = clamp(*args)
    if actual != expected:
        raise SystemExit(f"FAIL {args}: expected {expected!r}, got {actual!r}")

try:
    clamp(0, 2, 1)
except ValueError:
    pass
else:
    raise SystemExit("FAIL lower > upper did not raise ValueError")

print("PASS")

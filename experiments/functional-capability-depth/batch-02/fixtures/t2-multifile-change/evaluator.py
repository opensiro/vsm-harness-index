from pathlib import Path
import importlib.util
import sys

workspace = Path(sys.argv[1]).resolve()


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

settings = load("settings", workspace / "settings.py")
sys.modules["settings"] = settings
worker = load("worker", workspace / "worker.py")

cases = {
    None: 3,
    "": 3,
    " ": 3,
    "0": 0,
    "1": 1,
    "3": 3,
    "5": 5,
    "-1": 3,
    "6": 3,
    "100": 3,
    "abc": 3,
    "2.5": 3,
}

for raw, expected in cases.items():
    env = {} if raw is None else {"APP_RETRIES": raw}
    actual = settings.parse_retries(env)
    if actual != expected:
        raise SystemExit(f"FAIL parse_retries({raw!r}): expected {expected}, got {actual!r}")

for raw, expected in [("2", 2), ("bad", 3), ("7", 3), ("0", 0)]:
    job = worker.build_job({"APP_RETRIES": raw})
    if job != {"name": "sync", "retries": expected}:
        raise SystemExit(f"FAIL build_job({raw!r}): got {job!r}")

print("PASS")

#!/usr/bin/env python3
"""Reject edits to an assessment's already-recorded generation provenance."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


GENERATION_KEYS = (
    "generated_profile_version",
    "generated_assessment_procedure_version",
)


def git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    return result.stdout


def parse_frontmatter(text: str, source: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError(f"{source}: missing frontmatter")
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        raise ValueError(f"{source}: malformed frontmatter")
    row: dict[str, str] = {}
    for line in parts[1].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            row[key.strip()] = value.strip()
    return row


def generation_pair(row: dict[str, str], source: str) -> tuple[str, str] | None:
    present = [key for key in GENERATION_KEYS if row.get(key)]
    if not present:
        return None
    if len(present) != len(GENERATION_KEYS):
        missing = [key for key in GENERATION_KEYS if not row.get(key)]
        raise ValueError(f"{source}: incomplete generation provenance; missing {missing}")
    return row[GENERATION_KEYS[0]], row[GENERATION_KEYS[1]]


def base_assessments(base_ref: str) -> dict[str, tuple[str, dict[str, str]]]:
    paths = [
        line.strip()
        for line in git("ls-tree", "-r", "--name-only", base_ref, "--", "assessments").splitlines()
        if line.strip().endswith(".md")
    ]
    rows: dict[str, tuple[str, dict[str, str]]] = {}
    for path in paths:
        text = git("show", f"{base_ref}:{path}")
        row = parse_frontmatter(text, f"{base_ref}:{path}")
        harness_id = row.get("harness_id", "")
        if not harness_id:
            raise ValueError(f"{base_ref}:{path}: missing harness_id")
        if harness_id in rows:
            raise ValueError(f"{base_ref}: duplicate harness_id {harness_id}")
        rows[harness_id] = (path, row)
    return rows


def current_assessments(repo: Path) -> dict[str, tuple[str, dict[str, str]]]:
    rows: dict[str, tuple[str, dict[str, str]]] = {}
    for path in sorted((repo / "assessments").glob("*.md")):
        rel = path.relative_to(repo).as_posix()
        row = parse_frontmatter(path.read_text(encoding="utf-8"), rel)
        harness_id = row.get("harness_id", "")
        if not harness_id:
            raise ValueError(f"{rel}: missing harness_id")
        if harness_id in rows:
            raise ValueError(f"current tree: duplicate harness_id {harness_id}")
        rows[harness_id] = (rel, row)
    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-ref", required=True, help="Commit/ref representing the comparison base")
    args = parser.parse_args()

    repo = Path(__file__).resolve().parents[1]
    try:
        base = base_assessments(args.base_ref)
        current = current_assessments(repo)
    except (subprocess.CalledProcessError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1

    failures: list[str] = []
    guarded = 0
    for harness_id, (old_path, old_row) in base.items():
        try:
            old_pair = generation_pair(old_row, f"{args.base_ref}:{old_path}")
        except ValueError as exc:
            failures.append(str(exc))
            continue
        if old_pair is None:
            # Legacy origin was never recorded; this guard does not invent one.
            continue
        guarded += 1

        current_entry = current.get(harness_id)
        if current_entry is None:
            # Deletion/admission lifecycle is validated elsewhere; immutability applies
            # when the same assessment identity remains present.
            continue
        new_path, new_row = current_entry
        try:
            new_pair = generation_pair(new_row, new_path)
        except ValueError as exc:
            failures.append(str(exc))
            continue
        if new_pair != old_pair:
            failures.append(
                f"{harness_id}: immutable generation provenance changed: "
                f"{old_pair!r} -> {new_pair!r}"
            )

    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    print(f"Verified immutable generation provenance for {guarded} assessment(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

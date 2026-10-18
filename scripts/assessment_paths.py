"""Deterministic Index-local assessment layout, compatible with flat and sharded trees.

Index #55. Keep file discovery independent of the physical directory shape,
without accepting misplaced or deeply nested canonical records silently.
"""

from pathlib import Path


def shard(slug: str) -> str:
    """The fixed shallow shard for an assessment slug."""
    if not slug or slug != slug.lower() or any(c not in "abcdefghijklmnopqrstuvwxyz0123456789-_" for c in slug):
        raise ValueError(f"invalid assessment slug: {slug!r}")
    return slug[:2]


def flat_path(directory: Path, slug: str) -> Path:
    return directory / f"{slug}.md"


def sharded_path(directory: Path, slug: str) -> Path:
    return directory / shard(slug) / f"{slug}.md"


def paths(directory: Path) -> list[Path]:
    """Discover both layouts; fail closed for unexpected nesting or wrong shards."""
    result = []
    for path in sorted(directory.rglob("*.md")):
        if path.parent == directory:
            pass  # pre-migration flat layout
        elif path.parent.parent == directory and path.parent.name == shard(path.stem):
            pass  # stable shallow sharded layout
        else:
            raise ValueError(f"assessment path is not in its expected shard: {path}")
        result.append(path)
    return result


def is_sharded(directory: Path) -> bool:
    """New records go to shards after the atomic migration starts."""
    return any(child.is_dir() for child in directory.iterdir()) if directory.is_dir() else False

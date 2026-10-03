#!/usr/bin/env python3
"""Validate live candidate queues against canonical Index repository identities.

The validator is intentionally discovery-only. It does not mutate GitHub.
It checks open candidate/assessment batches and evidence-intake queues for:

- repositories already admitted as canonical `status: included` assessments;
- repositories already present in the catalog;
- the same repository queued in more than one active queue;
- rename/transfer aliases among active queue entries and canonical current names;
- declared active queue occupancy that disagrees with the candidate table.

Frozen batches are historical intake artifacts. Rows that later become catalogued or
canonical remain in those issues for provenance, but are no longer active queue rows.
Unprocessed rows in the same frozen batch remain active for deduplication.

`status: proposed` overlaps are reported as warnings because a proposed artifact can
legitimately coexist with the queue that is currently reviewing it, but discovery
must not queue that repository into another queue.
"""
from __future__ import annotations
import argparse
from concurrent.futures import ThreadPoolExecutor
import csv
import json
import os
import re
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path


QUEUE_TITLE_RE = re.compile(
    r"\[(?:(?:candidate|assessment)(?:-| )batch|evidence(?:-| )intake)\]",
    re.IGNORECASE,
)
REMAINING_OCCUPANCY_RE = re.compile(
    r"Remaining active candidate occupancy:\s*\*{0,2}(\d+)/10",
    re.IGNORECASE,
)
BATCH_OCCUPANCY_RE = re.compile(r"Batch occupancy:\s*\*{0,2}(\d+)/10", re.IGNORECASE)
FROZEN_QUEUE_RE = re.compile(r"\bbatch\b[^\n]{0,120}\bfrozen\b", re.IGNORECASE)
GITHUB_URL_RE = re.compile(r"(?:https://github\.com/)?([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)")


@dataclass(frozen=True)
class QueueEntry:
    issue_number: int
    issue_title: str
    repository: str
    frozen: bool = False


class GitHubAPIError(RuntimeError):
    def __init__(self, message: str, *, status_code: int | None = None) -> None:
        super().__init__(message)
        self.status_code = status_code


RETRYABLE_STATUS_CODES = {429, 500, 502, 503, 504}


def normalize_repo(value: str) -> str:
    value = value.strip().strip("`").rstrip("/")
    value = value.removeprefix("https://github.com/")
    if value.endswith(".git"):
        value = value[:-4]
    match = GITHUB_URL_RE.fullmatch(value)
    if not match:
        raise ValueError(f"not a GitHub owner/repo identity: {value!r}")
    return f"{match.group(1)}/{match.group(2)}"


def is_tracked_queue_title(title: str) -> bool:
    return bool(QUEUE_TITLE_RE.search(title))


def is_frozen_queue(body: str) -> bool:
    return bool(FROZEN_QUEUE_RE.search(body))


def declared_active_occupancy(body: str) -> int | None:
    match = REMAINING_OCCUPANCY_RE.search(body) or BATCH_OCCUPANCY_RE.search(body)
    return int(match.group(1)) if match else None


def declared_remaining_active_occupancy(body: str) -> int | None:
    match = REMAINING_OCCUPANCY_RE.search(body)
    return int(match.group(1)) if match else None


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end < 0:
        return {}
    result: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip().strip('"').strip("'")
    return result


def load_assessments(repo_root: Path) -> dict[str, list[str]]:
    by_status: dict[str, list[str]] = {"included": [], "proposed": []}
    for path in sorted((repo_root / "assessments").glob("*.md")):
        meta = parse_frontmatter(path)
        status = meta.get("status")
        repository = meta.get("repository")
        if status in by_status and repository:
            by_status[status].append(normalize_repo(repository))
    return by_status


def load_catalog(repo_root: Path) -> list[str]:
    with (repo_root / "data" / "catalog.psv").open(encoding="utf-8", newline="") as handle:
        rows = csv.DictReader(handle, delimiter="|")
        return [normalize_repo(row["repository"]) for row in rows if row.get("repository")]


def table_cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def parse_candidate_repositories(body: str) -> list[str]:
    lines = body.splitlines()
    repositories: list[str] = []
    for index, line in enumerate(lines):
        if not line.lstrip().startswith("|"):
            continue
        header = [cell.lower() for cell in table_cells(line)]
        if "project" not in header or "review ref" not in header:
            continue
        repo_index = next(
            (i for i, cell in enumerate(header) if cell in {"repository", "canonical repository"}),
            None,
        )
        if repo_index is None:
            continue
        row_index = index + 2  # skip markdown separator
        while row_index < len(lines) and lines[row_index].lstrip().startswith("|"):
            cells = table_cells(lines[row_index])
            if repo_index < len(cells):
                cell = cells[repo_index].strip().strip("`")
                match = GITHUB_URL_RE.search(cell)
                if match:
                    repositories.append(f"{match.group(1)}/{match.group(2)}")
            row_index += 1
        break
    return repositories


class GitHubAPI:
    def __init__(self, token: str | None) -> None:
        self.token = token
        self.repo_cache: dict[str, tuple[int, str]] = {}
        self.cache_lock = threading.Lock()

    def get(self, path: str, *, max_attempts: int = 3) -> object:
        request = urllib.request.Request(
            f"https://api.github.com{path}",
            headers={
                "Accept": "application/vnd.github+json",
                "User-Agent": "opensiro-discovery-dedupe-check",
                **({"Authorization": f"Bearer {self.token}"} if self.token else {}),
            },
        )
        for attempt in range(1, max_attempts + 1):
            try:
                with urllib.request.urlopen(request, timeout=30) as response:
                    return json.load(response)
            except urllib.error.HTTPError as exc:
                remaining = exc.headers.get("X-RateLimit-Remaining", "unknown")
                reset = exc.headers.get("X-RateLimit-Reset", "unknown")
                retry_after = exc.headers.get("Retry-After", "unknown")
                error = GitHubAPIError(
                    f"GitHub API {path} failed with HTTP {exc.code} "
                    f"(remaining={remaining}, reset={reset}, retry-after={retry_after})",
                    status_code=exc.code,
                )
                if exc.code in RETRYABLE_STATUS_CODES and attempt < max_attempts:
                    time.sleep(min(2 ** (attempt - 1), 4))
                    continue
                raise error from exc
            except (TimeoutError, urllib.error.URLError) as exc:
                if attempt < max_attempts:
                    time.sleep(min(2 ** (attempt - 1), 4))
                    continue
                raise GitHubAPIError(
                    f"GitHub API {path} failed after {max_attempts} attempts: {exc}"
                ) from exc
        raise AssertionError("unreachable")

    def open_issues(self, repository: str) -> list[dict[str, object]]:
        owner, repo = repository.split("/", 1)
        issues: list[dict[str, object]] = []
        page = 1
        while True:
            query = urllib.parse.urlencode({"state": "open", "per_page": 100, "page": page})
            payload = self.get(f"/repos/{owner}/{repo}/issues?{query}")
            assert isinstance(payload, list)
            page_items = [item for item in payload if "pull_request" not in item]
            issues.extend(page_items)
            if len(payload) < 100:
                break
            page += 1
        return issues

    def repository_identity(self, repository: str) -> tuple[int, str] | None:
        key = repository.lower()
        with self.cache_lock:
            cached = self.repo_cache.get(key)
        if cached is not None:
            return cached
        try:
            payload = self.get(f"/repos/{repository}")
        except GitHubAPIError as exc:
            if exc.status_code == 404:
                return None
            raise
        assert isinstance(payload, dict)
        identity = (int(payload["id"]), normalize_repo(str(payload["full_name"])))
        with self.cache_lock:
            self.repo_cache[key] = identity
        return identity

    def repository_identities(
        self, repositories: list[str], workers: int = 4
    ) -> list[tuple[int, str] | None]:
        if not repositories:
            return []
        with ThreadPoolExecutor(max_workers=min(workers, len(repositories))) as pool:
            return list(pool.map(self.repository_identity, repositories))


def active_queue_entries(
    api: GitHubAPI, index_repo: str
) -> tuple[list[QueueEntry], dict[int, int], list[str]]:
    entries: list[QueueEntry] = []
    remaining_occupancies: dict[int, int] = {}
    errors: list[str] = []
    for issue in api.open_issues(index_repo):
        title = str(issue.get("title", ""))
        if not is_tracked_queue_title(title):
            continue
        number = int(issue["number"])
        body = str(issue.get("body") or "")
        repositories = parse_candidate_repositories(body)
        if not repositories:
            errors.append(f"#{number}: tracked queue has no parseable candidate table")
            continue
        remaining_occupancy = declared_remaining_active_occupancy(body)
        if remaining_occupancy is not None:
            remaining_occupancies[number] = remaining_occupancy
        else:
            occupancy = declared_active_occupancy(body)
            if occupancy is not None and occupancy != len(repositories):
                errors.append(f"#{number}: declared occupancy {occupancy}/10 != {len(repositories)}/10 table rows")
        frozen = is_frozen_queue(body)
        for repository in repositories:
            entries.append(QueueEntry(number, title, repository, frozen=frozen))
    return entries, remaining_occupancies, errors


def classify_queue_entries(
    entries: list[QueueEntry],
    included: dict[str, str],
    proposed: dict[str, str],
    catalog_names: dict[str, str],
) -> tuple[list[QueueEntry], list[str], list[str]]:
    active: list[QueueEntry] = []
    errors: list[str] = []
    warnings: list[str] = []
    for entry in entries:
        key = entry.repository.lower()
        completed_in_frozen_batch = entry.frozen and (key in included or key in catalog_names)
        if completed_in_frozen_batch:
            continue

        active.append(entry)
        if key in included:
            errors.append(f"#{entry.issue_number}: {entry.repository} is already canonical status=included")
        if key in catalog_names:
            errors.append(f"#{entry.issue_number}: {entry.repository} is already present in data/catalog.psv")
        if key in proposed:
            warnings.append(
                f"#{entry.issue_number}: {entry.repository} already has status=proposed; do not queue it elsewhere"
            )
    return active, errors, warnings


def validate_remaining_occupancies(
    active_entries: list[QueueEntry], remaining_occupancies: dict[int, int]
) -> list[str]:
    active_counts: dict[int, int] = {}
    for entry in active_entries:
        active_counts[entry.issue_number] = active_counts.get(entry.issue_number, 0) + 1

    errors: list[str] = []
    for issue_number, declared in remaining_occupancies.items():
        actual = active_counts.get(issue_number, 0)
        if declared != actual:
            errors.append(
                f"#{issue_number}: declared remaining active occupancy {declared}/10 != {actual}/10 active rows"
            )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--index-repo",
        default=os.environ.get("GITHUB_REPOSITORY", "opensiro/vsm-harness-index"),
        help="GitHub repository containing the Index and candidate issues",
    )
    parser.add_argument(
        "--no-github-id-resolution",
        action="store_true",
        help="Only compare normalized owner/repo strings; intended for offline debugging",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    assessments = load_assessments(repo_root)
    catalog = load_catalog(repo_root)
    included = {repo.lower(): repo for repo in assessments["included"]}
    proposed = {repo.lower(): repo for repo in assessments["proposed"]}
    catalog_names = {repo.lower(): repo for repo in catalog}

    api = GitHubAPI(os.environ.get("GITHUB_TOKEN"))
    entries, remaining_occupancies, errors = active_queue_entries(api, args.index_repo)
    active_entries, classification_errors, warnings = classify_queue_entries(
        entries, included, proposed, catalog_names
    )
    errors.extend(classification_errors)
    errors.extend(validate_remaining_occupancies(active_entries, remaining_occupancies))

    by_name: dict[str, list[QueueEntry]] = {}
    for entry in active_entries:
        by_name.setdefault(entry.repository.lower(), []).append(entry)

    for repository, matches in by_name.items():
        issue_numbers = sorted({entry.issue_number for entry in matches})
        if len(issue_numbers) > 1:
            errors.append(f"{repository}: queued in multiple active candidate batches {issue_numbers}")

    if not args.no_github_id_resolution:
        canonical_names = set(included) | set(catalog_names)
        queued_ids: dict[int, list[QueueEntry]] = {}
        queue_identities = api.repository_identities([entry.repository for entry in active_entries])
        for entry, identity in zip(active_entries, queue_identities, strict=True):
            if identity is None:
                warnings.append(
                    f"#{entry.issue_number}: {entry.repository} returned HTTP 404 during GitHub identity "
                    "resolution; retaining string-based dedupe only"
                )
                continue
            repo_id, full_name = identity
            queued_ids.setdefault(repo_id, []).append(entry)
            resolved_key = full_name.lower()
            if resolved_key in canonical_names:
                canonical_name = included.get(resolved_key) or catalog_names[resolved_key]
                errors.append(
                    f"#{entry.issue_number}: {entry.repository} resolves to {full_name}, "
                    f"already canonical as {canonical_name}"
                )

        for repo_id, matches in queued_ids.items():
            issue_numbers = sorted({entry.issue_number for entry in matches})
            if len(issue_numbers) > 1:
                names = sorted({entry.repository for entry in matches})
                errors.append(
                    f"GitHub repository id {repo_id} ({names}) is queued in multiple active batches {issue_numbers}"
                )

    if warnings:
        print("Discovery queue warnings:")
        for warning in sorted(set(warnings)):
            print(f"  WARN: {warning}")

    if errors:
        print("Discovery queue validation failed:", file=sys.stderr)
        for error in sorted(set(errors)):
            print(f"  ERROR: {error}", file=sys.stderr)
        return 1

    print(
        f"Validated {len(active_entries)} active candidate queue entr{'y' if len(active_entries) == 1 else 'ies'} "
        f"({len(entries) - len(active_entries)} completed frozen rows ignored) "
        "against catalog, assessments, cross-queue identity, and GitHub repository IDs"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

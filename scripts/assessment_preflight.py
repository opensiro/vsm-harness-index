#!/usr/bin/env python3
"""Print the bounded task envelope for one sequential assessment batch issue.

This tool intentionally does not perform VSM interpretation. It only assembles
facts already owned by the Index issue and local active-contract registry.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
import urllib.error
import urllib.request
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

DEFAULT_REPOSITORY = "opensiro/vsm-harness-index"
ROOT = Path(__file__).resolve().parents[1]
ACTIVE_CONTRACT = ROOT / "data" / "active-contract.psv"

BOARD_ROW = re.compile(
    r"^\|\s*(?P<row>\d+)\s*\|\s*(?P<project>[^|]+?)\s*\|\s*`(?P<ref>[0-9a-f]{40})`\s*\|\s*\*\*?NEXT\*\*?\s*\|\s*$",
    re.MULTILINE | re.IGNORECASE,
)
CANDIDATE_ROW = re.compile(
    r"^\|\s*(?P<row>\d+)\s*\|\s*(?P<project>[^|]+?)\s*\|\s*`(?P<repository>[^`|]+/[^`|]+)`\s*\|\s*`(?P<ref>[0-9a-f]{40})`\s*\|",
    re.MULTILINE,
)


class PreflightError(RuntimeError):
    pass


@dataclass(frozen=True)
class TaskEnvelope:
    issue_number: int
    issue_title: str
    task_type: str
    row: int
    project: str
    repository: str
    review_ref: str
    assessment_path: str
    assessment_path_state: str
    profile_version: str
    methodology_version: str


def read_active_contract(path: Path = ACTIVE_CONTRACT) -> tuple[str, str]:
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="|"))
    if len(rows) != 1:
        raise PreflightError(f"{path} must contain exactly one contract row")
    row = rows[0]
    profile = (row.get("profile_version") or "").strip()
    methodology = (row.get("methodology_version") or "").strip()
    if not profile or not methodology:
        raise PreflightError(f"{path} is missing profile_version or methodology_version")
    return profile, methodology


def slugify_project(project: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", project.lower()).strip("-")
    if not slug:
        raise PreflightError(f"cannot derive assessment id from project label {project!r}")
    return slug


def _request_json(url: str, token: str | None = None) -> Any:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "opensiro-vsm-assessment-preflight",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            return json.load(response)
    except urllib.error.HTTPError as exc:
        raise PreflightError(f"GitHub API returned HTTP {exc.code} for {url}") from exc
    except urllib.error.URLError as exc:
        raise PreflightError(f"could not reach GitHub API for {url}: {exc.reason}") from exc


def fetch_issue(repository: str, issue_number: int) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    base = f"https://api.github.com/repos/{repository}"
    token = os.environ.get("GITHUB_TOKEN")
    issue = _request_json(f"{base}/issues/{issue_number}", token)
    comments: list[dict[str, Any]] = []
    page = 1
    while True:
        chunk = _request_json(f"{base}/issues/{issue_number}/comments?per_page=100&page={page}", token)
        if not isinstance(chunk, list):
            raise PreflightError("unexpected GitHub comments response")
        comments.extend(chunk)
        if len(chunk) < 100:
            break
        page += 1
    return issue, comments


def extract_next_row(texts: list[str]) -> tuple[int, str, str]:
    for text in reversed(texts):
        if "Manual assessment board" not in text:
            continue
        match = BOARD_ROW.search(text)
        if match:
            return int(match.group("row")), match.group("project").strip(), match.group("ref")
    raise PreflightError("no Manual assessment board row marked NEXT was found")


def extract_candidate(issue_body: str, row_number: int, review_ref: str) -> tuple[str, str]:
    for match in CANDIDATE_ROW.finditer(issue_body):
        if int(match.group("row")) != row_number:
            continue
        if match.group("ref") != review_ref:
            raise PreflightError(
                f"row {row_number} board ref {review_ref} disagrees with frozen candidate ref {match.group('ref')}"
            )
        return match.group("project").strip(), match.group("repository").strip()
    raise PreflightError(f"could not resolve frozen candidate row {row_number} from the issue body")


def build_envelope(
    issue_number: int,
    issue: dict[str, Any],
    comments: list[dict[str, Any]],
    root: Path = ROOT,
    contract_path: Path = ACTIVE_CONTRACT,
) -> TaskEnvelope:
    title = str(issue.get("title") or "").strip()
    body = str(issue.get("body") or "")
    if not title.startswith("[Assessment batch]"):
        raise PreflightError(f"issue #{issue_number} is not an [Assessment batch]: {title or '<untitled>'}")

    texts = [body] + [str(comment.get("body") or "") for comment in comments]
    row_number, board_project, review_ref = extract_next_row(texts)
    candidate_project, repository = extract_candidate(body, row_number, review_ref)
    if candidate_project.casefold() != board_project.casefold():
        raise PreflightError(
            f"row {row_number} project mismatch: board={board_project!r}, candidate={candidate_project!r}"
        )

    profile, methodology = read_active_contract(contract_path)
    assessment_path = f"assessments/{slugify_project(candidate_project)}.md"
    state = "existing" if (root / assessment_path).exists() else "new"

    return TaskEnvelope(
        issue_number=issue_number,
        issue_title=title,
        task_type="standalone-assessment",
        row=row_number,
        project=candidate_project,
        repository=repository,
        review_ref=review_ref,
        assessment_path=assessment_path,
        assessment_path_state=state,
        profile_version=profile,
        methodology_version=methodology,
    )


def render_text(task: TaskEnvelope) -> str:
    return "\n".join(
        [
            "Assessment preflight",
            f"issue: #{task.issue_number} — {task.issue_title}",
            f"task: {task.task_type}",
            f"NEXT row: {task.row} — {task.project}",
            f"repository: {task.repository}",
            f"frozen review_ref: {task.review_ref}",
            f"assessment path: {task.assessment_path} ({task.assessment_path_state})",
            f"active contract: Profile {task.profile_version} / Methodology {task.methodology_version}",
            "",
            "Read before semantic work:",
            "- https://github.com/opensiro/vsm-harness-profile/tree/main",
            "- https://github.com/opensiro/vsm-harness-skills/tree/main",
            "- the current assessment batch issue and Manual assessment board",
            "",
            "Task boundary:",
            "- assess only the current NEXT row",
            "- do not silently repin the frozen review_ref",
            "- fix the first-party system boundary before functional mapping",
            "- map organizational function first; classify autonomy second",
            "- do not advance the board unless the task explicitly grants that authority",
            "",
            "Final gates:",
            f"- python ../vsm-harness-skills/scripts/check_assessment_contract.py {task.assessment_path}",
            "- python scripts/render_tldr.py",
            "- python scripts/check_index.py",
        ]
    )


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("issue_number", type=int, help="assessment batch issue number")
    parser.add_argument("--repository", default=DEFAULT_REPOSITORY, help="GitHub repository owner/name")
    parser.add_argument("--json", action="store_true", dest="as_json", help="emit machine-readable JSON")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv if argv is not None else sys.argv[1:])
    try:
        issue, comments = fetch_issue(args.repository, args.issue_number)
        task = build_envelope(args.issue_number, issue, comments)
    except PreflightError as exc:
        print(f"assessment preflight failed: {exc}", file=sys.stderr)
        return 2

    if args.as_json:
        print(json.dumps(asdict(task), indent=2, sort_keys=True))
    else:
        print(render_text(task))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

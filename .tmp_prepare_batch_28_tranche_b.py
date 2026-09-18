#!/usr/bin/env python3
from pathlib import Path

catalog = Path("data/catalog.psv")
signatures = Path("data/signatures.psv")

catalog_rows = [
    "124|chief|Chief|https://github.com/SmileLikeYe/agent-chief|2026-07-04T15:28:56Z|adapted-source|d46072a804ff16aa7ce87751b82178f13fb973be|2026-09-18",
    "125|paperclip|Paperclip|https://github.com/paperclipai/paperclip|2026-03-02T15:01:51Z|adapted-source|352153b5edf02ff4262210c7bd5bfa94bcf37c7c|2026-09-18",
    "126|lobehub|LobeHub|https://github.com/lobehub/lobehub|2023-05-21T07:19:12Z|adapted-source|3af256caae11796da471bec5f57d882853f30f19|2026-09-18",
    "127|parlant|Parlant|https://github.com/emcie-co/parlant|2024-02-15T20:16:15Z|adapted-source|ea737442b8ae65854a842542e544fbe7e6144bad|2026-09-18",
    "128|maestro|Maestro|https://github.com/RunMaestro/Maestro|2025-11-23T01:59:55Z|adapted-source|32ecbc14fe832138e9a7af4f263d1026a8aa8a5b|2026-09-18",
]
signature_rows = [
    "124|chief|Chief autonomously classifies and acts on attention-bearing events; its explicit dispatch acceptance loop supplies a constructor S3* path because the standard resident runtime does not wire an autonomous verifier, while no separate S2, S3, S4 or S5 closure is established.",
    "125|paperclip|Paperclip runs autonomous worker agents under CEO/manager coordination and current control, supports an independent agent-review loop, and retains board-governed current-control and ultimate company-goal/strategy authority; no shipped external/prospective S4 closure is established.",
    "126|lobehub|LobeHub runs autonomous specialist agents under a model-driven Group Supervisor that selects sequential, parallel and other collaboration modes; documented iterative reviewer workflows expose a constructor S3* path, while no separate S3, S4 or S5 closure is established.",
    "127|parlant|Parlant runs an autonomous customer-facing conversational operation under contextual matching, guidelines, journeys and tool control; those intra-agent controls, traces and developer-authored policies do not establish separate S2-S5 organizational functions at the pinned boundary.",
    "128|maestro|Maestro runs autonomous coding-agent sessions and a model-driven Group Chat moderator; its default busy-agent hold explicitly attenuates concurrent same-file edit interference, establishing S2, while fleet dashboards, retries and configuration do not establish separate S3-S5 closure.",
]

def append_unique(path: Path, rows: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    existing = set(text.splitlines())
    additions = [row for row in rows if row not in existing]
    if additions:
        if text and not text.endswith("\n"):
            text += "\n"
        text += "\n".join(additions) + "\n"
        path.write_text(text, encoding="utf-8")

append_unique(catalog, catalog_rows)
append_unique(signatures, signature_rows)

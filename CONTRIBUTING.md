# Contributing to VSM Harness Index

VSM Harness Index uses an assessment-first workflow. Repository evidence is the source of truth; `TLDR.md` and `RANKINGS.md` are derived views.

## Quick start

You usually do **not** need to choose catalog order, invent a ranking, or design a batch yourself.

### Review a queued batch

1. Open the repository Issues page and look for an open issue whose title starts with `[Index batch]`.
2. Pick an unclaimed batch whose issue says it is ready for review.
3. Comment that you are taking it, or ask to be assigned.
4. Follow the exact repositories, pinned revisions, outputs, and acceptance checks in that issue.
5. Submit one PR for the batch unless the issue says otherwise.

A batch may be completed by a human contributor, a human using coding/research agents, or an autonomous agent. The acceptance contract is the same: pinned primary evidence, reviewable assessments, deterministic validation, and a normal PR.

### Suggest a harness

Open an issue whose title starts with `[Harness suggestion]`. Include the primary repository URL and a short explanation of why it belongs in an agent-harness index. You do not need to know its VSM classification or catalog position. Maintainers own catalog placement, provenance normalization, and batching.

Useful optional material includes links to first-party architecture docs, runtime code, policy/control paths, tests, or other primary evidence.

### Correct an assessment

Open an issue whose title starts with `[Assessment correction]` if you find stronger primary evidence or disagree with a VSM mapping. Include the harness, affected function (`S1`, `S2`, `S3`, `S3*`, `S4`, or `S5`), current interpretation, proposed interpretation, and exact primary evidence.

Do not edit generated rankings as the primary fix.

## Maintainer / full assessment workflow

The detailed workflow below applies when creating or integrating an assessment rather than merely suggesting a candidate.

1. Check out `vsm-harness-profile`, `vsm-skills`, and `vsm-harness-index` as siblings.
2. Confirm or add the discovery row in `data/catalog.psv`; preserve provenance, exact `review_ref`, `reviewed_at`, and chronological ordering.
3. Process candidates in ascending `catalog_position`. During migration, assessments must form a contiguous prefix from position 1.
4. Use `assess-vsm-harness` to write `assessments/<harness_id>.md` from pinned primary evidence.
5. Only after the assessment is complete, compare it with all earlier completed assessments and add its cohort-relative signature to `data/signatures.psv`.
6. Run `python scripts/render_tldr.py` to regenerate `TLDR.md` and `RANKINGS.md`.
7. Run `python scripts/check_index.py`.

Do not hand-author a TLDR classification independently from repository evidence.

## Assessment requirements

- State system-in-focus, purpose, environment, standard-distribution boundary, recursion level, exact ref, and review date.
- Describe enough repository architecture to preserve why the VSM mapping was made.
- Map the organizational function before classifying agent ownership.
- Record primary evidence, basis, confidence, and caveats for material positive claims.
- Keep agent decision rights separate from deterministic support mechanisms and configuration-time authorship.
- Keep unknown evidence (`?`) distinct from a reviewed no-path result (`—`).
- Do not infer S2 from delegation, S3 from a manager label, S3* from routine verification, S4 from planning or learning alone, S5 from prompts/policies alone, or recursion from nesting.

## Signature requirements

A signature is a derived comparison artifact, not repository evidence. Preserve the assessment vector exactly and describe the smallest informative architectural distinction relative to earlier catalog positions. Duplicate vectors are allowed.

## Ranking requirements

Do not manually score harnesses. `RANKINGS.md` is generated deterministically from recorded states and measures only out-of-box agent ownership coverage.

## Migration

The old `vsm_tldr` column remains temporarily in `data/catalog.psv` for history. Do not use it as evidence for a new assessment; rebuild each row from its pinned primary sources.

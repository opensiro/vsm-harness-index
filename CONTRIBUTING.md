# Contributing an assessment

The index uses an assessment-first workflow. Do not hand-author a TLDR classification independently from repository evidence.

## Required workflow

1. Check out `vsm-harness-profile`, `vsm-skills`, and `vsm-harness-index` as siblings.
2. Confirm or add the discovery row in `data/catalog.psv`; preserve provenance, exact `review_ref`, `reviewed_at`, and chronological ordering.
3. Process candidates in ascending `catalog_position`. During migration, assessments must form a contiguous prefix from position 1.
4. Use `assess-vsm-harness` to write `assessments/<harness_id>.md` from pinned primary evidence.
5. Only after the assessment is complete, compare it with all earlier completed assessments and add its cohort-relative signature to `data/signatures.psv`.
6. Run `python scripts/render_tldr.py` to regenerate `TLDR.md` and `RANKINGS.md`.
7. Run `python scripts/check_index.py`.

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

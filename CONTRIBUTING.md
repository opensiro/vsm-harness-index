# Contributing an assessment

The index follows a source-to-projection workflow. Do not hand-author scores independently from the assessment evidence.

## Required workflow

1. Check out `vsm-harness-profile`, `vsm-skills`, and `vsm-harness-index` as siblings.
2. Add or refresh the discovery row in `data/catalog.psv`, retaining source
   provenance and sorting by `repository_created_at`, then repository URL.
3. Generate its provisional TL;DR in chronological order and compare it with all
   lower positions. `harness_id` is stable; `catalog_position` is a derived ordinal
   and shifts when an older repository is backfilled.
4. For a detailed assessment, use `vsm-skills/skills/assess-vsm-harness` against a
   pinned harness tag or commit and save the JSON under
   `data/assessments/<slug>/<date>-<ref>.json`. Its position must match the catalog.
5. Regenerate tables:

   ```bash
   python ../vsm-skills/skills/assess-vsm-harness/scripts/upsert_harness.py \
     data/assessments/<slug>/<assessment>.json --output-dir data
   ```

6. Regenerate the README and newest-first TL;DR projections:

   ```bash
   python scripts/render_readme.py
   ```

7. Add or update `entries/<slug>.md` and its qualitative README comparison row.
8. Run:

   ```bash
   python scripts/check_index.py
   ```

## Review requirements

- Declare the system boundary, observation date, exact ref, and rubric version.
- Declare every assessment frame; target projections also require a named scenario and explicit assumptions.
- Record the harness's first public release year in a detailed assessment and cite
  an authoritative source; do not infer it from repository creation time.
- Keep catalog positions ordered, unique, and contiguous from 1.
- Write all six TL;DR systems in canonical order; use `—` when no
  autonomy-centered claim is asserted, without implying proven absence.
- Confirm that S1 contains an autonomous agent decision/action loop supported by
  harness state, tools, delegation, or feedback—not merely a model call or workflow.
- Prefer maintainer documentation, source, traces, and observable behaviour.
- Cite every positive or partial mapping.
- Keep `unknown` distinct from zero and `no`.
- Do not infer S3* from logging, S4 from planning, S5 from prompting, or recursion from nesting.
- Preserve raw sub-scores so percentages can be reconstructed.
- Reassess compared harnesses with the same rubric version when a scoring change is material.

Catalog-only TL;DR rows are source-derived hypotheses, not completed assessments.
The current JSON structure is an internal index artifact, not a required harness
manifest or external VSM standard.

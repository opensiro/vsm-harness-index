# Contributing an assessment

The index follows a source-to-projection workflow. Do not hand-author derived comparison data independently from the assessment evidence.

## Required workflow

1. Check out [vsm-harness-profile](https://github.com/opensiro/vsm-harness-profile), [vsm-skills](https://github.com/opensiro/vsm-skills), and [vsm-harness-index](https://github.com/opensiro/vsm-harness-index) as siblings.
2. Add or refresh the discovery row in `data/catalog.psv`, retaining source
   provenance and sorting by `repository_created_at`, then repository URL.
3. Generate its reviewed TL;DR in chronological order and compare it with all
   lower positions. `harness_id` is stable; `catalog_position` is a derived ordinal
   and shifts when an older repository is backfilled.
4. Reconstruct the fingerprint from pinned primary project sources using the assessment skill.
5. Regenerate the newest-first TL;DR projection:

   ```bash
   python scripts/render_tldr.py
   ```

6. Run:

   ```bash
   python scripts/check_index.py
   ```

## Review requirements

- Record the review date and exact ref, and keep the standard-distribution boundary explicit.
- Keep catalog positions ordered, unique, and contiguous from 1.
- Write all six TL;DR systems in canonical order; use `—` when no
  autonomy-centered claim is asserted, without implying proven absence.
- Confirm that S1 contains an autonomous agent decision/action loop supported by
  harness state, tools, delegation, or feedback—not merely a model call or workflow.
- Prefer maintainer documentation, source, traces, and observable behaviour.
- Support every positive or composable mapping with primary project evidence.
- Keep `unknown` distinct from zero and `no`.
- Do not infer S3* from logging, S4 from planning, S5 from prompting, or recursion from nesting.
- Reassess compared harnesses with the same method when a classification change is material.

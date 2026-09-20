# Contributing to VSM Harness Index

VSM Harness Index uses an assessment-first workflow. Repository evidence is the source of truth; `TLDR.md` and `RANKINGS.md` are derived views.

## Quick start

You usually do **not** need to choose catalog order, invent a ranking, or design a batch yourself.

### Review queued assessment work

Assessment queues are usually tracked in issues titled `[Assessment batch] ...`. Discovery-only queues may still be titled `[Candidate batch] ...` until they are frozen and given an active manual assessment board.

For the normal sequential assessment workflow:

1. Open the repository Issues page and choose a frozen batch that says manual assessment is ready or in progress.
2. Read the batch's **Manual assessment board** and find the row marked `NEXT`.
3. Claim that `NEXT` row in a comment, or ask to be assigned. The batch is the queue/container; the default contribution unit is the current `NEXT` row, not the whole batch.
4. Re-read current `main` of `opensiro/vsm-harness-profile` and `opensiro/vsm-harness-skills`, then follow the exact frozen repository revision, system-boundary reminders, outputs, and acceptance checks in the issue.
5. Assess only that row unless the issue explicitly authorizes a different unit of work. Do not silently repin it and do not advance to later queued rows.
6. Submit a reviewable PR for the row's canonical admission or terminal resolution. Advance exactly one row only through the batch workflow after the current `NEXT` reaches a terminal state.

A batch may ultimately be completed by one or many contributors, including humans using coding/research agents or autonomous agents. The acceptance contract is the same: pinned primary evidence, reviewable assessments, deterministic validation, and normal PR review.

If you arrive without a pre-assigned task, start from an open frozen `[Assessment batch]` with an active Manual assessment board rather than choosing an arbitrary candidate from a partial discovery queue.

### Suggest a harness

Open an issue whose title starts with `[Harness suggestion]`. Include the primary repository URL and a short explanation of why it belongs in an agent-harness index. You do not need to know its VSM classification or catalog position. Maintainers own catalog placement, provenance normalization, and batching.

Useful optional material includes links to first-party architecture docs, runtime code, policy/control paths, tests, or other primary evidence.

### Request an assessment re-review

Open an issue whose title starts with `[Assessment re-review]` when you find stronger primary evidence, disagree with a VSM mapping, or want an existing harness reassessed after a relevant upstream change.

A request must identify:

- the harness and current assessment;
- the affected function or functions (`S1`, `S2`, `S3`, `S3*`, `S4`, `S5`);
- the current interpretation or vector being challenged;
- the exact primary evidence path(s) and pinned revision;
- why the current mapping may be incomplete, inconsistent, or stale;
- the proposed interpretation if you have one. A final replacement state is optional at issue-opening time.

There are two re-review kinds:

1. **Same-ref correction.** Re-evaluate the existing assessment at the same `review_ref`. This is appropriate when the evidence was missed or interpreted incorrectly. `data/catalog.psv` does not change. Inside a reassessment round, the reviewer may also inspect a newer upstream `checked_ref`; when that newer ref does not materially change the corrected assessment, keep `accepted_review_ref` / canonical `review_ref` on the old boundary while allowing `last_checked_ref` to record the newer successful freshness check.
2. **New-ref reassessment.** Re-evaluate a newer upstream commit because relevant architecture or runtime behavior changed. Update the catalog `review_ref` and `pinned_at` only after the new assessment boundary is accepted; the assessment's own `reviewed_at` records when the reassessment was performed.

Do not edit generated rankings as the primary fix and do not open a ranking-only PR.

### Work on a reassessment round

Periodic longitudinal review is organized into dated reassessment rounds under `reassessments/`. A round has a frozen scope and cutoff date and may be split into multiple batch issues or PRs.

For every harness assigned to a round batch:

1. start from the currently accepted assessment and `review_ref`;
2. inspect upstream changes through the round cutoff and record the newest exact `checked_ref` actually reviewed;
3. decide whether those changes are VSM-relevant before rewriting the assessment;
4. record exactly one round outcome: `no-upstream-change`, `no-material-change`, `reassessed-unchanged`, `reassessed-changed`, `same-ref-correction`, or `blocked`;
5. append the event to `data/reassessment-history.psv`;
6. update the round progress table;
7. update the assessment freshness fields for every successfully checked harness;
8. update `review_ref`, `reviewed_at`, catalog pinning, signatures, and generated views only where the accepted reassessment requires them;
9. run `python scripts/check_index.py`.

A round check is useful even when the assessment does not change. In that case `last_checked_ref` and `last_checked_at` advance while the accepted `review_ref` can remain unchanged. The same freshness rule applies when a semantic error is corrected at the old accepted ref: `same-ref-correction` records where the corrected classification is evidenced, while a newer `checked_ref` may separately record that later upstream was inspected and did not require a new accepted boundary.

### Claim a re-review as a contributor

A contributor may claim an open `[Assessment re-review]` issue in a comment. The contributor's PR should:

1. reproduce the current mapping from the pinned evidence rather than starting from the requested replacement grade;
2. inspect the strongest first-party implementation/docs/tests for the disputed function;
3. perform an adversarial recheck that actively looks for evidence against the proposed change;
4. update the standalone assessment only where the evidence changes the interpretation;
5. update the catalog ref/pin date only for a **new-ref reassessment**;
6. if the work belongs to a reassessment round, append its longitudinal event and update freshness metadata;
7. re-check the changed harness's cohort-relative signature and any later signatures whose distinction depends on it;
8. regenerate `TLDR.md` and `RANKINGS.md` when canonical assessment data changes;
9. run `python scripts/check_index.py`.

The issue author and implementation contributor may be the same person. The final merge review should still independently verify the disputed VSM function rather than treating the issue's proposed grade as authoritative.

## Re-review acceptance contract

A re-review is complete only when the reviewer can answer all of the following from primary evidence:

1. **Function:** is the VSM function actually present at the declared system boundary?
2. **Actor:** which actor or mechanism performs it?
3. **Decision right / feedback path:** what authority or complementary access makes the mapping material?
4. **Ownership:** is the mapped function agent-owned (`A`), deliberately composable (`C`), parent-governed for S5 (`P`), absent in the reviewed standard distribution (`—`), or still unresolved (`?`)?
5. **Closure:** is the path actually closed in the standard distribution or merely exposed as a primitive/configuration surface?
6. **Counter-evidence:** what code, tests, defaults, or boundary facts argue against the proposed state?

For disputed positive metasystem mappings, apply the negative rules strictly: delegation is not S2 without interference regulation; a manager is not S3 without whole-system current authority; routine verification is not S3* without materially complementary and sufficiently independent access; planning/learning/event reaction is not S4 without external-and-prospective adaptation; static policy/config is not S5 closure.

If the re-review cannot distinguish between two states after the strongest available primary evidence has been inspected, prefer `?` over forced certainty.

## Maintainer / full assessment workflow

The detailed workflow below applies when creating or integrating an assessment rather than merely suggesting a candidate.

1. Check out `vsm-harness-profile`, `vsm-harness-skills`, and `vsm-harness-index` as siblings.
2. Confirm or add the discovery row in `data/catalog.psv`; preserve provenance, exact `review_ref`, `pinned_at`, and chronological ordering.
3. Use `assess-vsm-harness` to write `assessments/<harness_id>.md` from pinned primary evidence.
4. Only after the assessment is complete, compare it with all earlier completed assessments and add or update its cohort-relative signature in `data/signatures.psv`.
5. If an existing assessment changes, inspect later signatures for dependency on the changed distinction; update only those whose cohort-relative statement is no longer true.
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

For a newly created baseline assessment, set `assessment_changed_at` equal to `reviewed_at`. Legacy baseline assessments may omit reassessment freshness metadata until first touched by a reassessment round.

After the first round check, the complete freshness set is required:

```yaml
last_checked_ref: <40-character commit>
last_checked_at: YYYY-MM-DD
assessment_changed_at: YYYY-MM-DD
last_reassessment_round: R1
```

`last_checked_*` describes verification freshness. `assessment_changed_at` describes the most recent material change to the canonical assessment. Do not advance `assessment_changed_at` for a `no-material-change` result.

## Signature requirements

A signature is a derived comparison artifact, not repository evidence. Preserve the assessment vector exactly and describe the smallest informative architectural distinction relative to earlier catalog positions. Duplicate vectors are allowed.

## Ranking requirements

Do not manually score harnesses. `RANKINGS.md` is generated deterministically from recorded states and measures only out-of-box agent ownership coverage.

## Catalog role

`data/catalog.psv` is the discovery/order/provenance registry. It stores repository identity, chronology, source membership, and the pinned review boundary (`review_ref`, `pinned_at`). VSM classifications and assessment review dates belong only in standalone assessments and generated views, never in the catalog registry.

Longitudinal check history does not belong in the catalog either. Store it in `data/reassessment-history.psv`; the canonical assessment carries only its current boundary plus the latest freshness fields.
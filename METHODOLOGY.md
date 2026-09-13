# Indexing policy

`vsm-harness-index` does not maintain a second VSM methodology. It applies:

1. `vsm-harness-profile/PROFILE.md` for the meaning of organizational functions;
2. `vsm-skills/skills/assess-vsm-harness` for evidence collection, confidence, and TL;DR reconstruction;
3. this document only for index-specific publication rules.

## Entry boundary

Each entry assesses a named harness at a pinned tag or commit where possible. A framework, a deployed application, and the vendor organization are different systems-in-focus and must not be mixed.

The index uses an agent-autonomy lens: it asks which autonomous agent absorbs
variety and holds each VSM decision right. Deterministic framework mechanisms and
human gates are supporting infrastructure, not autonomous enactment by themselves.

Reviews distinguish observed current behavior, the standard distribution boundary,
and any named target projection while preparing evidence. The published index retains
only the categorical autonomy fingerprint so readers do not have to reconcile parallel
symbol, score, or artifact systems.

## Discovery cohort

The catalog may use a curated secondary source to discover candidates and form a
reproducible review queue. Each TL;DR fingerprint must then be independently
reconstructed from primary project sources at the pinned `review_ref`.

The current cohort is adapted from the pinned source documented in
[`SOURCES.md`](SOURCES.md). It retains loop-owning, non-evaluation projects and sorts
them by GitHub repository creation timestamp, with repository name as the tie-breaker.
That timestamp is a reproducible ordering proxy; it is not the date when autonomous
functionality first appeared. Local additions must identify their provenance and join
the same sort before positions are regenerated.

## TL;DR review order and evidence

Review catalog candidates by ascending `catalog_position`, beginning at position 1. Record the pinned `review_ref` and `reviewed_at` boundary before assigning categorical autonomy states. After the forward pass, compare each fingerprint with all later positions and retain the most informative evidenced distinction. Display order may remain newest-first; it does not change review order.

`tldr_status: excluded-no-agentic-vsm` records candidates whose standard documented setup does not establish an autonomous decision/action loop. A documented core runtime dependency may carry that loop; an optional third-party plugin or merely compatible API may not. Excluded candidates remain in the discovery catalog but are not rendered as fingerprints.

## Published autonomy states

| State | Index meaning |
| --- | --- |
| `A` | Ready agent-owned enactment is available through the standard documented setup. |
| `C` | A first-party primitive is supplied, but the developer must compose the agent, authority, or feedback loop. |
| `P` | Parent-assisted runtime closure returns an identity or ultimate-policy decision to subsequent operation; valid only for S5. |
| `—` | No material first-party path is supplied inside the review boundary; this does not claim that one can never be built. |
| `?` | The reviewed primary evidence cannot establish the state. |

Every positive assertion requires a primary source. Missing documentation remains
`?`. `A / C / P / — / ?` is the only published comparison notation.

## Data ownership

- `data/catalog.psv` is the single source of truth for cohort provenance, chronology, review refs, review dates, statuses, and fingerprints.
- `TLDR.md` is the generated newest-first public projection.

Neither file is a harness manifest, VSM standard, score, or benchmark leaderboard.

## Review rule

A contribution must use the same assessment method across harnesses it compares,
identify evidence coverage, and keep unavailable evidence distinct from absence.
Longitudinal comparisons must pin reviewed refs and review dates.

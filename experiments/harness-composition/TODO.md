# Harness composition TODO

This backlog is **experiment-local and non-canonical**. Completion here does not change standalone Index assessments.

- [ ] Test **ownership lift through composition**: whether a function that is constructor-owned (`C`) in a base harness can become agent-owned (`A`) at a newly declared composed boundary by adding a specialized harness that owns the decisive decision right, while retaining the original `C` mechanism as deterministic enforcement/support.

  Do not mechanically combine standalone vectors. For each proposed lift, define a fresh system-in-focus and verify the complete closure path:

  ```text
  relevant disturbance / external distinction
          ↓
  evidence reaches the specialized component
          ↓
  specialized agent owns the decisive decision / feedback right
          ↓
  decision crosses the composition boundary
          ↓
  base operation actually changes
          ↓
  feedback closes into later operation
  ```

  Raven is now a canonical Index input after merged PR #939:

  ```text
  S1=A / S2=C / S3=A(P) / S3*=C / S4=A / S5=P
  ```

  Raven therefore has two direct constructor-to-agent ownership-lift targets (`S2`, `S3*`), one higher-risk ultimate-policy target (`S5`), and no S4 gap.

  Initial Raven trials:

  - [ ] `Raven + Maestro` — primary S2 ownership-lift trial. Maestro's model-driven moderator should own which Raven workers run/continue while Raven's read-ledger stale-edit guard remains deterministic enforcement. Preregistered as [Trial 001](trials/001-raven-maestro-s2/CONTRACT.md), governed by Index issue #950. Execution is fail-closed on proving a real Raven↔Maestro participant seam.
  - [ ] `Raven + redteam reviewer` — primary S3* ownership-lift trial. A distinct reviewer should inspect actual Raven-produced branch evidence and return a binding `APPROVED` / `CHANGES_REQUESTED` / escalation verdict into Raven current control; Raven's Harness Manifest remains complementary machine evidence.
  - [ ] `Raven + Maestro + Grit` — S2 separation trial: Maestro owns the coordination decision, while Grit adds claim/worktree/merge enforcement below it. Compare with Raven's native stale-edit guard rather than assuming multiple C mechanisms automatically improve S2.
  - [ ] `Raven + Maestro + redteam reviewer` — combined two-function trial only after the single-function S2 and S3* loops close independently.
  - [ ] `Raven + HugAgentOS reviewer` — alternative S3* donor trial using a read-only artifact-inspection reviewer; compare independence and adapter cost with redteam.
  - [ ] `Raven + HugAgentOS policy layer` — low-confidence S5 experiment. Do **not** credit an S5 lift unless a model-owned policy actor becomes legitimate ultimate authority over the composed Raven identity/policy and the decision returns into Raven's live context/permission path. A policy file or `/init` capability alone is insufficient.

  S4 comparison / duplicate-function trials — **not ownership lifts** because Raven already has `S4=A`:

  - [ ] `Raven + A-Evolve` — compare Raven's evaluator → Analyst → Curator → install loop with A-Evolve's benchmark/evidence → evolver → workspace reload loop. Define explicit arbitration if both can mutate the same harness.
  - [ ] `Raven + Continual Harness` — compare Raven's source-mode RSI with reset-free trajectory-driven prompt/subagent/skill/memory evolution.
  - [ ] `Raven + Utah` — compare Raven's general Harness curation with narrower durable skill/event-function creation and hot loading.

  Counterfactual owner tests for every donor composition:

  ```text
  remove donor agent
      -> the same discretionary target-function decision should disappear
         even if deterministic enforcement remains

  remove deterministic enforcement
      -> the donor decision may still exist,
         but safe/reliable execution should weaken
  ```

  If removing the donor leaves materially the same decision, the donor is not the owner. If the donor merely recommends and Raven/operator chooses the binding outcome, do not publish `A` for the composed target function.

  Experimental question:

  > Can constructor-owned control functions be lifted into agent-owned functions by composing specialized harnesses, while retaining the original constructor mechanisms as enforcement?

  Duplicate-function question:

  > When two independently agent-owned implementations of the same VSM function are composed, what explicit arbitration or scope split is required to avoid ambiguous ownership?

- [ ] Implement the first minimal composition only after the component interface is declared explicitly.
- [ ] For each executable composition, preserve a frozen system boundary, component revisions, adapter revision, trace/evidence packet and experiment-local finding.
- [ ] Keep findings outside canonical assessment state unless a future Skills/Profile change explicitly admits composed systems.
- [ ] If the experiment grows into independently evolving adapters, runners, traces and reusable methodology, reconsider extracting it into a dedicated repository then — not before.

## Promotion split

Presentation artifacts stay in `opensiro/opensiro-promotion`:

- video/demo concept;
- posters/storyboards;
- HTML/MP4/GIF renders;
- social/launch copy;
- thin links back to this technical experiment.

The technical source of truth while this remains an Index experiment is this directory.

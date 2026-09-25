# Execution harness status

Tracking issues: #612, #616, #617

Lifecycle: **retired historical experiment artifact — no live execution planned**.

This package contains the preregistration, identifiability work, fake/stub artifacts, and execution-harness engineering produced while exploring a controlled LoopX S2 comparison.

Current state:

- live model execution: **not performed and not planned for capability-depth**;
- direct S2 observation: **not admitted**;
- canonical LoopX assessment: **unchanged (`S2=A`)**;
- observation registry: **unchanged**;
- scalar S2 score: **not defined**;
- CI surface: deterministic, model-free historical identifiability checks only;
- live execution issue #616: **closed `not_planned`** after the public-evidence-only operating model was reaffirmed in #617.

The files in this directory are retained under `experiments/` as research history. They may be useful for understanding identifiability, adapter-preservation, fixture design, and why an Opensiro-operated reproduction would not be an appropriate capability-depth admission path.

They are **not capability evidence** and must not be used to fill the S2 primary gap.

The active capability-depth workflow resumes from already-public upstream or third-party evidence under [`../../PUBLIC-EVIDENCE.md`](../../PUBLIC-EVIDENCE.md).

`run_local.py`, `execution-plan.json`, fake artifacts, and related code are historical implementation artifacts. Their presence does not authorize or schedule a live harness run.

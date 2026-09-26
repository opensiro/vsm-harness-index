# SWE Atlas — S1 Coding/SWE benchmark-family review

Status: experimental, non-normative.

Tracking issue: #717

Reviewed source:

```text
scaleapi/SWE-Atlas@49e4af3b6c803dd54a1cd60ead703aac25de4e21
paper: arXiv:2605.08366
```

## Result

```text
function: S1
fit: direct
domain_scope: coding-swe
system_linkage: observation-specific
evaluation_mode: execution-grounded
```

SWE Atlas directly evaluates the operational coding-agent / harness loop inside real software repositories. The evaluated system must investigate repository state and produce task-relevant operational output: answer codebase questions, write tests, or refactor code. The benchmark then grades those outputs through component-specific tests and engineering rubrics.

That is direct S1 at the benchmark boundary. The classification is grounded in the operational transformation being performed, not in planning, tool-use, exploration, testing, review, recovery, or context-management vocabulary.

## Reviewed task surface

The pinned repository exposes three released dataset families under `data/`:

- Codebase QnA (`data/qa`);
- Test Writing (`data/tw`);
- Refactoring (`data/rf`).

The reviewed release contains 284 tasks in total:

```text
Codebase QnA  124
Test Writing   90
Refactoring    70
----------------
Total         284
```

The repository packages task instructions, environments, solutions and evaluators through Harbor-compatible dataset manifests. Test Writing and Refactoring additionally restrict network access during the agent phase; published run configurations also restrict agent web-search surfaces where relevant.

The task mix is intentionally broader than issue resolution. It probes software-engineering operation across comprehension, test construction and code transformation rather than treating one issue-resolution metric as the whole S1 domain.

## Evaluation boundary

SWE Atlas uses Harbor as the evaluation/runtime membrane. The repository provides run configurations for different agent/model combinations and documents Harbor v0.18.0 as the execution substrate for the reviewed release.

The benchmark remains `execution-grounded` for this mapping because the system under evaluation operates inside a repository/task environment and must produce the operational artifact or answer being evaluated. Grading is not uniform across every component: rubric/judge-based evaluation can be part of the scoring path, including the documented use of Claude Opus 4.5 as an LLM judge for rubric grading.

That evaluator layer grades S1 output. Its existence does not by itself establish S3* for the evaluated system because the benchmark judge is external to that system's organizational boundary and does not establish a resident independent corrective-return path.

## System linkage

Benchmark-family fit and canonical-system attribution are separate questions.

The public leaderboards report model-plus-scaffold configurations, including native coding-agent scaffolds and generic controls. A leaderboard display label does not establish a canonical Index identity, exact historical repository revision, or preservation of the first-party organizational boundary.

A later observation transaction must independently recover, where public evidence permits:

- exact scaffold / harness identity and version or a defensible historical-lineage link;
- exact model and materially relevant model configuration;
- benchmark component and task set;
- evaluator / judge configuration and run policy;
- network/tool restrictions;
- whether the benchmark exercised the system's own operational loop (`native-system`) or preserved it through an adapter (`adapter-preserved`).

If those facts are not recoverable, the benchmark family remains valid S1 evidence while the particular leaderboard row remains unlinked or weaker evidence.

## Primary-baseline boundary

Admitting SWE Atlas as a direct S1 family does **not** replace PawBench v1.0 as the selected general S1 primary and does not replace Claw-SWE-Bench as the current Coding/SWE domain primary.

The current selected PawBench cell is a matched-model comparison across multiple canonical harnesses. Claw-SWE-Bench likewise has an established Coding/SWE matched canonical projection. SWE Atlas enters as an additional direct Coding/SWE family; any later promotion requires a separate observation review and the existing primary-selection gate.

No leaderboard result is admitted in this transaction.

## Function-first non-claims

SWE Atlas does **not** establish:

- universal S1 capability outside the released software-engineering task surface;
- S2 from multi-step work, tool use, parallelism, or coordination terminology;
- S3 from planning, task management, control-flow, retry, or recovery behavior;
- S3* from benchmark tests, rubrics, judges, review, or verification terminology;
- S4 from exploration, context use, learning-like behavior, or within-task replanning;
- S5 from prompts, policies, permissions, network restrictions, or benchmark rules;
- experimental self-organizing `S` from successful task execution;
- any `A`, `C`, `P`, `—`, or `?` ownership state from benchmark performance.

## Admission consequence

SWE Atlas is admitted only to the experimental benchmark-family map as another direct S1 family with `coding-swe` scope and observation-specific system linkage.

This issue does not add raw system observations, duplicate public leaderboard numbers into Index data, modify canonical assessments, or change the selected primary baseline. A later transaction may review public Codex/native-scaffold rows or same-model cross-scaffold cells if their historical provenance is recoverable.
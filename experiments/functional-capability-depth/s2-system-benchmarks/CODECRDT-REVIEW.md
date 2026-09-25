# CodeCRDT — S2 public-evidence review

Status: **admit direct descriptive non-canonical observation**

Tracking issue: #640  
Repository: `spugachev/CodeCRDT`  
Reviewed revision: `8fa5a307062025c900e9de27696f4e804a0a7809`  
Paper: `arXiv:2510.18893`

## Decision

CodeCRDT provides **direct S2 evidence at its own product-defined multi-agent coding boundary**.

The relevant organization is not inferred from the word “coordination”. The first-party system actually supplies a shared CRDT state used by parallel coding agents to observe concurrent edits, skip already completed work, integrate context and converge without a separate merge-resolution step.

The function chain is:

```text
parallel coding S1s
→ concurrent updates to one shared code artifact
→ interaction-specific integration / merge variety
→ first-party observation-driven CRDT shared-state relation
→ deterministic convergence of concurrent edits
→ composed code state returned to continued operation
```

That is an S2 relation: the measured mechanism attenuates variety created by interaction among otherwise useful concurrent S1 activities.

## Public provenance

The reviewed repository commits both the implementation and the evaluation corpus. At the pinned revision, `evaluation/evaluation_results/` includes:

- `checkpoint.json` — approximately 14 MB of evaluation checkpoint data;
- `environment_info.json` — platform and experiment configuration;
- `evaluation_report.json` and `evaluation_report.yaml`;
- `objective_metrics.csv` plus corrected objective analyses;
- generated report artifacts.

The report records **600 evaluations**: six prompts, 50 runs per prompt in each of sequential and parallel modes. The environment record fixes `runs_per_prompt=50`, `max_concurrent_requests=1`, random seed `42`, temperature `0.0`, and Bonferroni-corrected statistical analysis. The accompanying first-party paper/research material identifies the model as Claude Sonnet 4.5.

The first-party scientific record states that strong eventual consistency yields **100% convergence with zero merge failures** in the evaluated CodeCRDT organization. It also reports residual semantic conflicts in preliminary inspection; that residual is a limitation, not a success metric.

## Comparison boundary

The public evaluation is **descriptive direct evidence**, not a matched causal ablation of coordination.

The reported experiment compares:

```text
sequential generation
vs
parallel CodeCRDT-coordinated generation
```

It does **not** include a matched `parallel-without-CodeCRDT` arm. Therefore this review does not claim that the difference between sequential and parallel outcomes estimates the causal effect of CodeCRDT S2.

In particular:

- response-time or quality differences between sequential and parallel modes are not used as an S2 uplift estimate;
- `100% convergence / zero merge failures` is retained as a first-party descriptive property of the coordinated parallel runs;
- no counterfactual “without coordination” rate is invented;
- the preliminary semantic-conflict estimate is retained only as a reported limitation.

## System boundary

The S2 path is **native to the public CodeCRDT product boundary**, but CodeCRDT is not currently a canonical VSM Harness Index system.

Therefore:

- `canonical_harness_id = null`;
- `canonical_system_eligible = false` for this observation;
- system compatibility is `native-system` at the external product boundary;
- evidence source is `first-party-reported`;
- comparison class is `descriptive-only`;
- no canonical autonomy state is assigned or inferred.

This distinction is why the coverage layer needs a separate `direct-native-noncanonical` class rather than misclassifying CodeCRDT as benchmark-scaffolded.

## Effect on S2 depth

If represented in the current capability-depth corpus, CodeCRDT adds:

- one direct S2 family;
- one direct non-canonical descriptive observation.

It does **not** add:

- a canonical native S2 observation;
- a matched cross-harness primary cell;
- a causal coordination effect size;
- a global S2 score.

The S2 primary therefore remains `gap`.

## Primary sources

- `https://github.com/spugachev/CodeCRDT/tree/8fa5a307062025c900e9de27696f4e804a0a7809`
- `https://github.com/spugachev/CodeCRDT/blob/8fa5a307062025c900e9de27696f4e804a0a7809/evaluation/README.md`
- `https://github.com/spugachev/CodeCRDT/blob/8fa5a307062025c900e9de27696f4e804a0a7809/evaluation/evaluation_results/environment_info.json`
- `https://github.com/spugachev/CodeCRDT/blob/8fa5a307062025c900e9de27696f4e804a0a7809/evaluation/evaluation_results/evaluation_report.yaml`
- `https://github.com/spugachev/CodeCRDT/tree/8fa5a307062025c900e9de27696f4e804a0a7809/evaluation/evaluation_results`
- `https://github.com/spugachev/CodeCRDT/blob/8fa5a307062025c900e9de27696f4e804a0a7809/SCIENCE.md`
- `https://arxiv.org/abs/2510.18893`

No Opensiro-operated reproduction was performed or is required for this admission.

# VSM benchmark-family mapping experiment

Status: experimental, non-normative.

Issue: #371

## Question

Can different VSM organizational functions be paired with different real benchmark families so capability evidence is gathered against the function under study, without collapsing VSM semantics into benchmark scores?

The experiment does **not** require one universal benchmark for S1-S5.

```text
canonical assessment
        ↓
function present at declared boundary
        ↓
benchmark family appropriate to that function
        ↓
behavioral capability evidence
        ↕
repository-grounded feature/mechanism evidence
```

The evidence channels stay separate:

- canonical assessment establishes organizational function and ownership;
- feature/mechanism evidence establishes how that function is implemented at the declared boundary;
- benchmark evidence observes behavior under a concrete `(system, model, config, benchmark)` evaluation.

Benchmark performance must not be used to infer `A`, `C`, `P`, `—`, or `?`.

## Initial candidate map

These are candidates for semantic review, not accepted equivalences.

| VSM function | Capability target | Candidate benchmark families | Initial fit |
| --- | --- | --- | --- |
| S1 — Operations | autonomous execution, tool/environment interaction, iterative operational correction, task completion | Terminal-Bench / Harbor; SWE-bench Pro; other execution-grounded domain benchmarks | `direct-candidate` |
| S2 — Coordination | interference attenuation, shared-resource coordination, distributed-state integration, deadlock/oscillation handling | DPBench; SILO-BENCH; alem; MultiAgentBench | `direct-candidate`, boundary review required |
| S3 — Inside-and-now control | current regulation of active units, priorities, commitments/resources, organization-wide intervention | ClawArena-Team | `proxy-candidate` |
| S3* — Complementary audit | independent challenge channel, evidence gathering outside the operating path, detection and corrective feedback | AuditBench | `proxy-candidate` |
| S4 — Outside-and-then intelligence | evolving-environment sensing, prospective modelling, belief updating, adaptation of future action | FutureSim; ClawArena; BTF/FutureBench; AdaPlanBench; CostBench | FutureSim `direct-candidate`; others mostly `proxy-candidate` |
| S5 — Policy and identity | legitimate ultimate-policy resolution, identity preservation, authoritative constraints/decision rights, return to operations | AgentGovBench and related governance evaluations | `proxy-candidate`; likely public benchmark gap |

## Primary candidate sources

### S1

- Terminal-Bench / Harbor: https://www.tbench.ai/
- Terminal-Bench repository: https://github.com/harbor-framework/terminal-bench
- SWE-bench family: https://www.swebench.com/

Terminal-Bench directly evaluates agents on end-to-end work in terminal environments and verifies resulting task state. This is a plausible operational-capability surface, but each result still belongs to a concrete system/model/configuration.

### S2

- DPBench: https://arxiv.org/abs/2602.13255
- DPBench code: https://github.com/najmulhasan-code/dpbench
- SILO-BENCH: https://aclanthology.org/2026.acl-long.1354/
- alem: https://arxiv.org/abs/2606.08340
- MultiAgentBench: https://aclanthology.org/2025.acl-long.421/

DPBench is especially relevant because it varies simultaneous resource contention and reports deadlock, throughput, fairness, and message/action consistency. SILO-BENCH tests distributed coordination when agents hold fragmented information and distinguishes active communication from successful distributed computation.

Do not treat communication, role assignment, delegation, or topology alone as S2 evidence. The benchmark must exercise an actual interference/shared-constraint relation.

### S3

- ClawArena-Team paper: https://arxiv.org/abs/2606.31174
- ClawArena-Team code/docs: https://github.com/aiming-lab/ClawArena/tree/main/ClawArena-Team

ClawArena-Team fixes the worker pool and evaluates a manager that creates, empowers, schedules, and integrates subagents across dynamic tasks. This is relevant to current regulation, but it is not automatically S3: delegation and orchestration vocabulary are insufficient. Semantic review must establish whether benchmark tasks/metrics materially exercise whole-system current-control rights.

### S3*

- AuditBench: https://alignment.anthropic.com/2026/auditbench/

AuditBench evaluates investigator agents that use configurable tools to uncover hidden behavior in target models. It is a useful independent-audit capability proxy, but the audited object is not necessarily the organization's own S1 operations and therefore does not itself prove VSM S3* closure.

### S4

- FutureSim: https://openforecaster.github.io/futuresim/
- ClawArena: https://www.clawarena.cc/
- ClawArena paper: https://arxiv.org/abs/2604.04202
- BTF-2 forecasting benchmark: https://futuresearch.ai/btf2-dataset-release/
- AdaPlanBench: https://arxiv.org/abs/2606.05622
- CostBench: https://aclanthology.org/2026.acl-long.584/

FutureSim is particularly relevant because agents operate through a chronological real-world environment, decide when to update forecasts, and adapt beliefs as new information arrives. It is still necessary to inspect whether and how prospective intelligence couples back into changed action before calling it a direct S4 measurement.

ClawArena directly tests dynamic belief revision under staged environmental updates, but belief revision alone is not the complete S4 organizational function.

### S5

- AgentGovBench: https://github.com/agentic-control-plane/agentgovbench

AgentGovBench tests governance infrastructure such as identity propagation, policy enforcement, delegated-subagent controls, and auditability. These are relevant to S5-adjacent capability, but policy enforcement is not equivalent to ultimate policy/identity authority. No direct public S5 benchmark is accepted at this stage.

## Benchmark-fit vocabulary

After semantic review, classify each function/benchmark pairing as exactly one of:

- `direct` — tasks and metrics materially exercise the target VSM function at a compatible system boundary;
- `proxy` — benchmark measures a relevant capability but not the full organizational function;
- `unsuitable` — benchmark vocabulary appears related but the evaluated behavior is not the VSM function;
- `unknown` — insufficient evidence.

During discovery only, `direct-candidate` and `proxy-candidate` may be used to avoid prematurely freezing the classification.

## Review requirements

Before accepting a benchmark family for a function, record:

1. benchmark revision/version/date;
2. primary source;
3. evaluated object/system boundary;
4. task structure;
5. metrics and what behavior they actually measure;
6. evaluation mode: execution-grounded, judge-based, human-rated, self-reported, or mixed;
7. model/configuration dependence;
8. public traces/artifacts availability;
9. `direct/proxy/unsuitable/unknown` fit;
10. explicit function-first argument linking measured behavior to the Profile function;
11. explicit non-claims preventing vocabulary shortcuts.

## System comparisons

Once a benchmark family is accepted for a VSM function, canonical Index systems may be linked to published benchmark observations where the evaluated boundary is compatible.

Comparisons are only valid inside defensible comparability groups. Prefer matched model/configuration when studying harness/system effects, but do not require the same benchmark across different VSM functions.

The intended shape is:

```text
S1 systems → S1 benchmark family/families
S2 systems → S2 benchmark family/families
S3 systems → S3 benchmark family/families
S3* systems → S3* benchmark family/families
S4 systems → S4 benchmark family/families
S5 systems → S5 benchmark family/families
```

A system may therefore have evidence from several different benchmark families because it closes several different organizational functions.

## Feature/mechanism evidence remains mandatory

Benchmark observations and repository evidence answer different questions.

```text
canonical function + ownership
            ↓
feature/mechanism evidence ──┐
                            ├── capability interpretation
benchmark evidence ─────────┘
```

This permits conclusions such as:

- observed capability is largely inherited from a host/runtime;
- first-party mechanisms are rich but public benchmark evidence is weak;
- different harnesses produce different outcomes under matched model conditions;
- a benchmark is informative only as a proxy for the VSM function.

Do not turn the synthesis into a scalar maturity score or reinterpret `A/C/P` as an ordinal ladder.

## First phase

1. Semantically review the candidate benchmark families from primary sources.
2. Produce a function→benchmark map using `direct/proxy/unsuitable/unknown`.
3. Identify canonical Index systems that have published results in accepted families.
4. Preserve benchmark/model/configuration/system-boundary/revision provenance.
5. Produce an evidence-gap report, especially for S3, S3*, and S5.
6. Do not attribute observed performance to individual features yet.

Feature-level attribution is a later phase after the system/function benchmark layer is stable.

## Boundary

This experiment may add notes/data/validators under `experiments/functional-capability-depth/` only.

It must not modify canonical assessments, catalog data, TLDR, rankings, Full-A projections, Profile semantics, Skills methodology, existing Batch 01/02 results, or upstream harness repositories.

# First semantic review of benchmark families

Status: experimental, non-normative.

Issue: #371

This review applies the current `vsm-harness-profile` function definitions before interpreting benchmark vocabulary. It does not change canonical assessments or Profile semantics.

## Reviewed map

| VSM function | Benchmark family | Fit | Why |
| --- | --- | --- | --- |
| S1 — Operations | Terminal-Bench / Harbor | `direct` | Agents perform end-to-end work in a real terminal environment; task state is externally graded. This directly exercises operational execution, tool use, environment feedback, and task completion. |
| S1 — Operations | SWE-bench family | `direct` | An agent receives a real repository issue, edits a checked-out repository, and is graded by issue-specific tests. This is direct evidence of software-engineering operational capability. |
| S2 — Coordination | DPBench | `direct` | The benchmark structurally creates multiple operational actors under simultaneous shared-resource contention and measures deadlock/coordination outcomes. This supplies the specific interference/oscillation witness required by the Profile rather than treating communication as coordination by name. |
| S2 — Coordination | SILO-BENCH | `proxy` | It measures distributed collaboration under fragmented information and exposes a communication-reasoning gap, but the primary disturbance is information separation rather than a clearly identified recurring inter-S1 interference/oscillation relation. |
| S2 — Coordination | alem | `proxy` | Long-horizon teams must communicate, specialise, trade and execute shared plans, but the published benchmark-level description does not by itself establish the specific disturbance-plus-attenuation relation required for direct S2 mapping. Task-level review could promote particular coordination goals later. |
| S2 — Coordination | MultiAgentBench | `proxy` | Collaboration/competition, topology and milestone metrics are relevant, but broad collaboration quality is not equivalent to S2 disturbance attenuation. |
| S3 — Inside-and-now control | ClawArena-Team | `direct` | At the benchmark-defined boundary, the main agent has whole-team visibility and actual authority over subagent creation, tool subsets, workspace whitelists, foreground/background execution, inspection, scheduling and dynamic workflow composition. The direct mapping is based on those current-control rights, not on the words manager/orchestrator/delegation. |
| S3 — Inside-and-now control | EnterpriseArena | `proxy` | It directly stresses scarce-resource allocation under uncertainty, an S3-relevant capability, but the single CFO-style decision loop blends resource regulation with prospective/environmental reasoning and does not cleanly expose a multi-S1 whole-system control boundary. |
| S3* — Complementary audit | AuditBench | `proxy` | The investigator agent obtains alternative evidence about hidden target-model behaviour, so it is a strong audit-capability test. The audited object is an external target model, however, and the benchmark does not establish ordinary reporting vs complementary access inside the same viable system or closure from findings into S3 control. |
| S4 — Outside-and-then intelligence | FutureSim | `proxy` | It directly exercises chronological external sensing, forecast revision and belief adaptation. The Profile additionally requires development of adaptation options and a path back into present capability/S3; FutureSim primarily closes on updated forecasts, not organizational adaptation. |
| S4 — Outside-and-then intelligence | ClawArena | `proxy` | It stresses multi-source conflict reasoning and dynamic belief revision under staged updates, but belief revision by itself is not the complete external-and-prospective adaptation loop. |
| S4 — Outside-and-then intelligence | AdaPlanBench | `unsuitable` | The agent replans the current task when hidden world/user constraints are revealed after plan violations. This is reactive operational planning, which the Profile explicitly excludes from S4 unless it participates in an external-and-prospective adaptation loop. |
| S4 — Outside-and-then intelligence | CostBench | `unsuitable` | Dynamic tool failures/cost changes force replanning of the current travel task. This is useful S1 planning/adaptation evidence but does not establish prospective environmental intelligence coupled to organizational adaptation. |
| S5 — Policy and identity | AgentGovBench | `unsuitable` | The benchmark measures identity propagation, policy enforcement, delegation provenance, scope/rate-limit inheritance, audit completeness, fail-mode discipline and tenant isolation. Those are governance/enforcement mechanisms. The Profile explicitly separates enforcement from ownership of legitimate ultimate-policy/identity decisions. |
| S5 — Policy and identity | RoleCDE | `proxy` | Structured conflicts between role-specific values and alignment constraints make it relevant to identity/value-conflict reasoning, but it is a role-playing model benchmark with no legitimate organizational ultimate authority or return-to-operation closure. |

## Function-first reasoning

### S1

Terminal-Bench and SWE-bench are direct because their evaluated object performs the primary transformation in an environment and receives execution-grounded feedback. A benchmark result still belongs to a concrete `(system, model, configuration, benchmark revision)` and must not be converted into an autonomy state.

Primary sources:

- Terminal-Bench datasets / Harbor: https://hub.harborframework.com/datasets/terminal-bench
- SWE-bench: https://www.swebench.com/
- Harbor SWE-bench Verified adapter/parity: https://hub.harborframework.com/datasets/swe-bench/swe-bench-verified

### S2

DPBench is the strongest direct candidate found so far because the disturbance itself is explicit: simultaneous agents contend for shared resources and can deadlock. Sequential vs simultaneous conditions and communication interventions change the coordination problem, and deadlock/throughput/fairness expose whether the disturbance was attenuated.

SILO-BENCH, alem and MultiAgentBench are valuable coordination benchmarks in the ordinary multi-agent sense, but VSM S2 is narrower. Communication density, role allocation or collaboration score does not by itself establish a concrete interference/oscillation relation.

Primary sources:

- DPBench: https://arxiv.org/abs/2602.13255
- SILO-BENCH: https://aclanthology.org/2026.acl-long.1354/
- alem: https://arxiv.org/abs/2606.08340
- MultiAgentBench: https://aclanthology.org/2025.acl-long.421/

### S3

ClawArena-Team crosses the threshold from generic delegation into direct S3 capability at its own benchmark boundary. The main agent can:

- create specialised subagents;
- grant/restrict tool subsets and workspace paths;
- run them foreground/background;
- inspect live configuration, status and history;
- schedule and compose parallel/pipelined workflows;
- react to staged updates and background completions;
- integrate the team's outputs.

The decisive evidence is whole-team visibility plus live authority over operational constraints and scheduling. Merely selecting a worker or merging its output would not be sufficient.

EnterpriseArena is retained as a proxy for the resource-allocation dimension of S3, not a direct S3 benchmark.

Primary sources:

- ClawArena-Team paper: https://arxiv.org/abs/2606.31174
- ClawArena-Team implementation/docs: https://github.com/aiming-lab/ClawArena/tree/main/ClawArena-Team
- EnterpriseArena: https://arxiv.org/abs/2603.23638

### S3*

AuditBench is a strong test of autonomous investigation with materially different access to a target's behaviour. It does not, however, place that audit channel beside routine S1-S3 reporting inside the same system-in-focus, nor require findings to change subsequent system control. It therefore remains a proxy for S3* capability rather than a direct VSM S3* benchmark.

Primary source:

- AuditBench: https://alignment.anthropic.com/2026/auditbench/

### S4

FutureSim is deliberately dynamic and chronological: agents see dated world information, decide which forecasts to revisit and update beliefs over months. This directly covers important S4 ingredients, but the benchmark's closed loop is forecasting accuracy/belief revision. It does not require a two-way S3-S4 conversation or adaptation options that alter present organizational capability, so the full function fit remains `proxy`.

ClawArena is similarly useful for dynamic belief revision but stops short of full S4 closure.

AdaPlanBench and CostBench are rejected for S4 at this level because both primarily test current-task replanning when constraints, failures or costs change. The Profile explicitly states that internal planning or reaction to an external event is not S4 by itself.

Primary sources:

- FutureSim: https://openforecaster.github.io/futuresim/
- FutureSim code/harness integration: https://github.com/OpenForecaster/futuresim
- ClawArena: https://arxiv.org/abs/2604.04202
- AdaPlanBench: https://arxiv.org/abs/2606.05622
- CostBench: https://aclanthology.org/2026.acl-long.584/

### S5

No direct public S5 benchmark was established in this review.

AgentGovBench is deliberately classified `unsuitable` as a direct S5 measurement despite its governance vocabulary. Its scenarios deterministically test whether a pre-existing policy/identity/governance decision is propagated and enforced. That can benchmark supporting mechanisms around S5, S3 or S3*, but it does not test who legitimately owns ultimate policy/identity authority or how unresolved S3-S4 tension reaches that authority and returns to govern operation.

RoleCDE is retained only as a proxy for one narrower ingredient: reasoning under identity/value conflict. It still lacks organizational authority and closure.

Primary sources:

- AgentGovBench: https://github.com/agentic-control-plane/agentgovbench
- RoleCDE: https://aclanthology.org/2026.findings-acl.106/

## System-boundary compatibility

Semantic fit of a benchmark family is not enough to attribute a result to a canonical Index system. Record a second, independent compatibility field when linking observations:

- `native-system` — the benchmark actually runs the canonical/first-party harness or a recoverable version of it;
- `adapter-preserved` — an adapter is used, but the relevant native function path remains materially intact and can be evidenced;
- `benchmark-scaffolded` — the benchmark supplies its own control/coordination/audit scaffold and mainly evaluates a model or policy inside that scaffold;
- `unclear` — the published evidence is insufficient.

Only `native-system` and carefully justified `adapter-preserved` observations should normally support system-level capability comparisons in the Index experiment.

A `direct` benchmark with `benchmark-scaffolded` system compatibility measures the VSM capability **in the benchmark's organization**, not in the canonical harness being compared.

## Existing canonical-system anchors

### S1: usable native/adapter evidence already exists

Harbor's SWE-bench Verified parity records explicitly include:

- `codex@0.2.0` with `o4-mini` over 500 tasks;
- `openhands@c677f728` with `claude-4-sonnet` over 500 tasks.

The official SWE-bench leaderboard also contains OpenHands and SWE-agent entries, and current Harbor/Terminal-Bench public jobs contain Codex runs. These are suitable starting points for S1 linkage once exact benchmark revision, model, harness version and adapter boundary are preserved.

### S2: direct benchmark, weak canonical-system linkage

DPBench's published experiments primarily evaluate model agents inside the DPBench multi-agent environment rather than first-party Index harness coordination paths. It is therefore `direct` for S2 capability semantics but currently `benchmark-scaffolded` for most canonical-system attribution.

### S3: direct benchmark, benchmark-defined organization

ClawArena-Team is `direct` for S3 capability at its benchmark boundary, but its fixed worker pool and CapitalCase management tools define the organization under test. Its published model leaderboard must not be silently attributed to Codex, Gemini CLI, LangGraph, AutoGen or another Index harness merely because tool/provider names resemble them.

### S3*: proxy and benchmark-defined investigator

AuditBench uses its own investigator scaffold. It does not currently provide direct canonical-harness S3* measurements.

### S4: useful historical native-harness anchor, but only proxy fit

FutureSim explicitly supports and reports native CLI harnesses. Its released setup names Codex, Claude Code and OpenCode backends; published reproduction metadata identifies Codex version `0.125.0` for the original GPT-5.5 runs. This makes FutureSim unusually useful for studying how a real harness behaves on an S4-adjacent capability while still preserving the conclusion that the benchmark itself is only a `proxy` for full S4 closure.

This is also a useful negative-control example: a harness can perform well on an S4-proxy benchmark even when its canonical VSM assessment does not establish S4 at the assessed boundary.

### S5: governance-framework results must not be mislabeled as S5 results

AgentGovBench publishes framework integrations/results for systems including Codex CLI, OpenAI Agents SDK, CrewAI and LangGraph. Those results may later be useful for governance-mechanism analysis, but under the current Profile they are not S5 capability results because the benchmark fixes the governing policy and scores enforcement/propagation rather than ultimate-policy ownership.

## Evidence gaps after the first review

1. **S1 has the strongest real-system evidence.** Mature execution benchmarks frequently run actual harnesses and retain version/model metadata.
2. **S2 has a strong direct benchmark but poor native-harness coverage.** DPBench measures the right disturbance, but current runs mostly use benchmark-owned topology.
3. **S3 now has a plausible direct benchmark family.** ClawArena-Team exercises whole-team control, but currently evaluates a benchmark-defined organization rather than native Index S3 implementations.
4. **S3* lacks a direct same-system benchmark.** AuditBench measures investigator skill, not complementary audit closure inside an operating organization.
5. **S4 has strong behavioral proxies and unusually good harness integration, but no reviewed benchmark closes the required S3↔S4 adaptation loop.**
6. **S5 remains the clearest benchmark gap.** Existing governance benchmarks test enforcement, identity plumbing, compliance or role-value reasoning rather than legitimate ultimate-policy authority and return-to-operation closure.

## Consequence for the next phase

Do not build a universal leaderboard.

The next data layer should be keyed by both function fit and system compatibility:

```text
VSM function
  ↓
reviewed benchmark family: direct / proxy / unsuitable / unknown
  ↓
benchmark observation
  ↓
system compatibility: native-system / adapter-preserved / benchmark-scaffolded / unclear
  ↓
feature/mechanism evidence
  ↓
function-specific capability synthesis
```

This keeps three different questions separate:

1. does the canonical system actually implement the VSM function? — canonical assessment;
2. does the benchmark actually exercise that function? — benchmark semantic review;
3. did the benchmark actually exercise this system's own implementation of that function? — system-boundary compatibility.

No benchmark result may answer question 1 by itself, and no benchmark-scaffolded run may answer question 3 by name association alone.

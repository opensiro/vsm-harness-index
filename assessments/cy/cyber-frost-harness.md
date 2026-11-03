---
harness_id: cyber-frost-harness
project_name: Cyber-Frost Harness
repository: https://github.com/Blackfrost-AI/Cyber-Frost-Harness
review_ref: 54a7e28baac28f740601dd576e21674a513cd844
reviewed_at: 2026-11-03
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# Cyber-Frost Harness

## Review boundary

- System in focus: First-party Python security-agent runner and session/tool bridge for one native vulnerable target task, including documented red/blue/purple task modes; not the outside benchmark administrator.
- Purpose and identity: Let a configured model investigate a native security target, run bounded experiments, preserve evidence, select candidate payloads/patches and report a result.
- Relevant environment: Vulnerable task image, native tools, source/coverage/crash evidence, remote model endpoint, Docker host and independently administered hidden fixed-image grader.
- Standard-distribution boundary: `cyber_frost_harness` CLI `run-task` → one `SecurityAgent` tool loop in an isolated target container, supplied task metadata, skills and evidence/session ledger; an intentional outside submission-script adapter may return independent verification results.
- Credited operating / distribution surfaces: [agent.py](https://github.com/Blackfrost-AI/Cyber-Frost-Harness/blob/54a7e28baac28f740601dd576e21674a513cd844/src/cyber_frost_harness/agent.py), [CLI run task](https://github.com/Blackfrost-AI/Cyber-Frost-Harness/blob/54a7e28baac28f740601dd576e21674a513cd844/src/cyber_frost_harness/cli.py#L396-L451), [tools.py](https://github.com/Blackfrost-AI/Cyber-Frost-Harness/blob/54a7e28baac28f740601dd576e21674a513cd844/src/cyber_frost_harness/tools.py), [session.py](https://github.com/Blackfrost-AI/Cyber-Frost-Harness/blob/54a7e28baac28f740601dd576e21674a513cd844/src/cyber_frost_harness/session.py), [architecture](https://github.com/Blackfrost-AI/Cyber-Frost-Harness/blob/54a7e28baac28f740601dd576e21674a513cd844/docs/ARCHITECTURE.md).
- Adjacent first-party surfaces excluded from ownership: CI/release, `results/` benchmark outcome artifacts, `scripts/run_manifest.py` evaluator analysis and project maintenance. The external model, native target and hidden fixed-image grader supply evidence/dependencies but do not become first-party autonomous audit decision owners.
- First-party operating / deployment modes considered: CLI `run-task` with red/blue/purple agent mode, Docker target commands, lazy built-in skills, optional external task-local grader script and explicit candidate submission/finish. Separate `smoke-task`, analysis and offline benchmark reports are not credited as operating S-functions.
- Recursion level: One security target task/run; phases/tools, benchmark cases and external grader are not automatically subordinate viable S1 units.
- Reviewed revision: `54a7e28baac28f740601dd576e21674a513cd844`.
- Observation date: 2026-11-03.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

`command_run_task` prepares a native isolated target and task inventory, constructs `RunSession`, `SkillLibrary`, `ToolRegistry`, `OpenAICompatibleClient`, and one `SecurityAgent`, then runs it to a terminal payload. `SecurityAgent.run` delegates semantic tool selection to the configured model; typed tool calls are checked and executed, observations appended as tool messages, repeated calls bounded and context compacted. RunSession persists events/artifacts and can submit exact candidate bytes to a task-local shell verifier with a returned response. The private fixed-image grader is supplied by the benchmark/task owner, not this repository. [architecture](https://github.com/Blackfrost-AI/Cyber-Frost-Harness/blob/54a7e28baac28f740601dd576e21674a513cd844/docs/ARCHITECTURE.md), [run loop](https://github.com/Blackfrost-AI/Cyber-Frost-Harness/blob/54a7e28baac28f740601dd576e21674a513cd844/src/cyber_frost_harness/agent.py#L309-L390).

## Operational model

One security-analysis S1 pursues task evidence through inspect/load-skill, command/search, corpus, fuzz/replay, patch, finding, candidate and finish tools. Container limits and budgets enforce previously configured constraints. The repository exposes a function-specific submission bridge to a separate grader, but no independent first-party audit model or grading authority; its verdict may be used by the S1 to revise a candidate where the task package supplies this verifier.

## S1 — Operations

- State: A
- Function: Autonomous security-task investigation, candidate generation and evidence-led completion.
- Disturbance / variety regulated: Unknown exploit path, wrong target architecture, malformed inputs, crashes, failed native commands, incomplete root-cause or patch verification.
- Decisive decision or feedback right: Choose which tool/skill/evidence experiment to run, what candidate to submit and when to finish after observing results.
- Decision owner: Model actor within the first-party `SecurityAgent.run` loop, not deterministic command validation or outside benchmark scorekeeper.
- Supporting / enforcement mechanisms: Task container, model client, tool registry, skill catalogue, source/corpus/replay operations, token/step caps, compaction and evidence ledger.
- Closure path: Model response→validated first-party tool call→native result/recorded evidence→tool message→next model step or final selected candidate.
- Boundary reachability: Normal `run-task` CLI instantiates the agent and tool loop with the provided task/container; this is not benchmark-only postprocessing.
- Why this is / is not agent-owned: Hard guardrails execute preselected limits; the model decides task-specific investigative hypotheses and subsequent actions.
- Evidence: [agent.py#L309-L390](https://github.com/Blackfrost-AI/Cyber-Frost-Harness/blob/54a7e28baac28f740601dd576e21674a513cd844/src/cyber_frost_harness/agent.py#L309-L390), [cli.py#L396-L451](https://github.com/Blackfrost-AI/Cyber-Frost-Harness/blob/54a7e28baac28f740601dd576e21674a513cd844/src/cyber_frost_harness/cli.py#L396-L451), [tools.py](https://github.com/Blackfrost-AI/Cyber-Frost-Harness/blob/54a7e28baac28f740601dd576e21674a513cd844/src/cyber_frost_harness/tools.py).
- Basis: structural
- Confidence: high for first-party execution loop, not task win rate.
- Caveats: Requires a configured external LLM, target Docker host and benchmark task package; no paid/model-backed run was made.

## S2 — Coordination

- State: —
- Function: No first-party relation regulating interference among distinct operational agent units in one task.
- Disturbance / variety regulated: Sequential candidate experiments and repeated identical tool calls are intra-S1 process stability, not inter-agent oscillation.
- Decisive decision or feedback right: No conflict-resolution choice among independently operating S1 peers is supplied.
- Decision owner: None for S2 at the run boundary.
- Supporting / enforcement mechanisms: Per-command process tags, agent call-history and session submission limits.
- Closure path: Tool conflicts and command statuses feed one model, with no separate S1-to-S1 coordination feedback.
- Why this is / is not agent-owned: Modes called red, blue and purple are alternative behaviours of a single worker, not concurrently coordinated agent cells.
- Evidence: [agent.py](https://github.com/Blackfrost-AI/Cyber-Frost-Harness/blob/54a7e28baac28f740601dd576e21674a513cd844/src/cyber_frost_harness/agent.py), [architecture](https://github.com/Blackfrost-AI/Cyber-Frost-Harness/blob/54a7e28baac28f740601dd576e21674a513cd844/docs/ARCHITECTURE.md).
- Basis: structural
- Confidence: high for supported single-task mode.
- Caveats: An external batch runner can launch many independent cases without making them this harness's coordinated S1 units.

### Absence scope

- Surfaces inspected: CLI task entry, agent loop, skills, tools, session ledger, container transport and mode definitions.
- Plausible first-party paths checked: Multiple security modes, command serialization, repeated-call blocking and manifest batch execution.
- Why no material first-party path remains: These do not establish two distinct S1 agents with a specific interference and corrective coordination return.

## S3 — Inside-and-now control

- State: —
- Function: No distinct whole-current management of several operational units/commitments is established.
- Disturbance / variety regulated: Model step limits, attempt counts and container resource ceilings govern one task's execution safety.
- Decisive decision or feedback right: No agent/human current resource bargaining or intervention over a multi-unit whole is wired into runtime.
- Decision owner: Operator sets configuration; Python engine and Docker enforce hard limits; model owns local experiments.
- Supporting / enforcement mechanisms: `max_steps`, submission cap, CPU/memory/PID limits and per-command deadlines.
- Closure path: Limit or task failure halts/returns one worker's local operation; no separate S3 reallocation to other S1 units.
- Why this is / is not agent-owned: Deterministic enforcement is not the organizational current-control choice; ordinary operator config is not a closed parent S3 mode.
- Evidence: [config.py](https://github.com/Blackfrost-AI/Cyber-Frost-Harness/blob/54a7e28baac28f740601dd576e21674a513cd844/src/cyber_frost_harness/config.py), [agent.py](https://github.com/Blackfrost-AI/Cyber-Frost-Harness/blob/54a7e28baac28f740601dd576e21674a513cd844/src/cyber_frost_harness/agent.py).
- Basis: structural
- Confidence: high at task recursion.
- Caveats: Benchmark administration may oversee a cohort externally, but that is not this runtime's S3 authority.

### Absence scope

- Surfaces inspected: CLI run task, run configuration, session/candidates, native transport and toolkit gates.
- Plausible first-party paths checked: Budget controls, task target selection, retry/compaction, candidate selection and manifest-level evaluation.
- Why no material first-party path remains: No established whole-current operational-view/commitment decision with return into distinct agent units.

## S3* — Complementary audit

- State: C
- Claim being audited: Candidate input/patch claimed by the S1 to demonstrate a bug or a fixed-image regression result.
- Ordinary reporting path: Model-visible source/sanitizer/fuzzer and replay output plus its own findings and candidate rationale.
- Complementary access path: `RunSession._submit_bytes` preserves exact bytes, calls a task-local submission script outside the target container and parses its independently supplied verification response.
- Independence boundary: Docker/model container lacks the grader's hidden fixed image and credentials. The repository bridges an independent check but cannot supply or control the outside grading authority; source-only reading cannot assert its actual quality.
- Who acts on findings: The task's external verifier decides the hidden comparison; first-party submit tool returns the parsed response and records it for the model to consider or revise the candidate.
- Function: Complementary independent test of selected candidate reality beyond the model's own local narrative.
- Disturbance / variety regulated: Locally plausible exploits/patches that fail on the hidden fixed task, accidental candidate-byte mismatch, false self-reported success.
- Decisive decision or feedback right: Independent grader verdict at submit time, externally owned; first-party adapter specifically exposes the resulting corrective feedback, not grader autonomy.
- Decision owner: External task/benchmark verifier decides correctness; Cyber-Frost ships the candidate/response integration constructor only.
- Supporting / enforcement mechanisms: Hashed candidate preservation, task-local `submit` script invocation, parsed response, artifact ledger and final selection.
- Closure path: Model prepares candidate→first-party submit tool preserves and sends bytes→external verifier returns fresh result→parsed tool result enters model context→model can change candidate or finish.
- Boundary reachability: The normal `run-task` session wires `RunSession` into tool registry; `submit_candidate` is a shipped model-callable tool, not only an offline results script. A concrete grader must be provided by the task package.
- Why this is / is not agent-owned: The complementary auditor is independent, but not a first-party agent owned by the harness; `C` credits an explicitly audit-specific first-party composition path, **not** an automatic `A` or proof that every deployed task supports a valid grader.
- Evidence: [session.py#L144-L230](https://github.com/Blackfrost-AI/Cyber-Frost-Harness/blob/54a7e28baac28f740601dd576e21674a513cd844/src/cyber_frost_harness/session.py#L144-L230), [tools.py#L673-L677](https://github.com/Blackfrost-AI/Cyber-Frost-Harness/blob/54a7e28baac28f740601dd576e21674a513cd844/src/cyber_frost_harness/tools.py#L673-L677), [architecture](https://github.com/Blackfrost-AI/Cyber-Frost-Harness/blob/54a7e28baac28f740601dd576e21674a513cd844/docs/ARCHITECTURE.md).
- Basis: structural
- Confidence: medium; first-party audit handoff is proven, actual grader correctness/execution is not.
- Caveats: Hidden fixed-image verification is outside the repository's trust boundary, and no live grader transaction was reproduced. This `C` does not imply independent first-party audit ownership.

## S4 — Outside-and-then intelligence

- State: —
- Function: No independent prospective environmental learning→adaptation option→changed current capability is wired.
- Disturbance / variety regulated: Target-specific crash/corpus discoveries are immediate task evidence.
- Decisive decision or feedback right: No persistent future-oriented adaptation decision for the harness's own operational repertoire exists.
- Decision owner: Developers maintain skills/benchmarks, model chooses current task experiments.
- Supporting / enforcement mechanisms: Lazy skill loading, target triage, source audit, crash evidence, compaction and experiment scripts.
- Closure path: New sample facts affect the current task's next model turn, not a durable external-future option returned into present S3 capability.
- Why this is / is not agent-owned: Adaptive experimentation within a target and author-side benchmark refinement are not shipped S4 governance.
- Evidence: [skills.py](https://github.com/Blackfrost-AI/Cyber-Frost-Harness/blob/54a7e28baac28f740601dd576e21674a513cd844/src/cyber_frost_harness/skills.py), [agent.py](https://github.com/Blackfrost-AI/Cyber-Frost-Harness/blob/54a7e28baac28f740601dd576e21674a513cd844/src/cyber_frost_harness/agent.py), [evaluation docs](https://github.com/Blackfrost-AI/Cyber-Frost-Harness/blob/54a7e28baac28f740601dd576e21674a513cd844/docs/EVALUATION.md).
- Basis: structural
- Confidence: medium-high.
- Caveats: Developer research after failed benchmark runs is adjacent, not automatically an S4 owner in a shipped run.

### Absence scope

- Surfaces inspected: Agent, skills, target inventory, evidence records, model compaction and benchmark analysis scripts.
- Plausible first-party paths checked: Red/blue/purple switches, skill selection, evaluation feedback, failure-analysis reports and revised target hypotheses.
- Why no material first-party path remains: No explicit long-horizon external-environment option selection and return to whole-system present capability was found.

## S5 — Policy and identity

- State: —
- Function: Ultimate-policy and organizational-identity decision closure is not supplied at the task-agent boundary.
- Disturbance / variety regulated: Unsafe commands, protected grader secrets, credential exposure and tool misuse are operational risk controls.
- Decisive decision or feedback right: No identity/mission dispute route to a legitimate ultimate authority with returned binding policy change.
- Decision owner: Task package/operator/developer chooses immutable sandbox and model-tool rules.
- Supporting / enforcement mechanisms: Network isolation, Docker capabilities, static system prompt, excluded grader secret, command/CPU budgets and credentials separation.
- Closure path: Security checks block or constrain particular tool actions; no returned ultimate-policy decision governs future organizational identity.
- Why this is / is not agent-owned: Static constraints and a benchmark scoring rule do not become first-party S5, including parent governance.
- Evidence: [architecture](https://github.com/Blackfrost-AI/Cyber-Frost-Harness/blob/54a7e28baac28f740601dd576e21674a513cd844/docs/ARCHITECTURE.md), [transport.py](https://github.com/Blackfrost-AI/Cyber-Frost-Harness/blob/54a7e28baac28f740601dd576e21674a513cd844/src/cyber_frost_harness/transport.py), [config.py](https://github.com/Blackfrost-AI/Cyber-Frost-Harness/blob/54a7e28baac28f740601dd576e21674a513cd844/src/cyber_frost_harness/config.py).
- Basis: explicit + structural
- Confidence: high at task recursion.
- Caveats: This finding says nothing about the parent benchmark owner's actual governance organization.

### Absence scope

- Surfaces inspected: Security documentation, CLI/config, model system prompt, transport privileges and candidate finalization.
- Plausible first-party paths checked: Mode choice, sandbox policy, task owner constraints, candidate approval and release/update practices.
- Why no material first-party path remains: All are current task/security configuration or external development controls rather than a closed identity-level policy process.

## Distributed OSS parent arrangement

No public distributed-operator parent S3/S4/S5 arrangement is packaged into the runtime; maintainer and benchmark-owner choices remain outside the selected task recursion.

## Self-hosted and non-human modes

The runner accepts local or remote OpenAI-compatible models but the same S1 loop applies. Human operator config controls enforcement; no distinct parent-governed S3/S4/S5 mode is established from that configuration alone.

## Recursion

The model and target tools compose one task agent. A tool call, skill, Docker process, task dataset row or red/blue mode does not itself define another recursively viable system.

## Variety and escalation

Typed tools and native target inventory amplify observations; output bounds, repeated-call rejection and sandbox limits attenuate hazardous variety. Model errors and completion caps return to local retries or terminal best-effort results. Candidate grader feedback can challenge local model evidence in supported benchmark tasks but its outside authority is not a first-party autonomous meta-agent.

## Evidence gaps

Source-pinned review without live model-provider or hidden fixed-image grader transaction. Dynamic grader trust, actual solution rates, cross-case portfolio control and host isolation quality are not claimed; the S3* constructor grade is narrowly limited to the shipped submission/feedback integration path.

## Verdict

**Propose inclusion.** First-party source establishes one autonomous security-model/tool S1 plus a specific constructor for independent task-grader feedback. No separate inter-S1 coordination, current-control manager, outside-and-then capability adaptation or ultimate-policy closure is established.

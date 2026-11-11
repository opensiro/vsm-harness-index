---
harness_id: gamai-trust-layer-rush
project_name: gamAI Trust Layer / rush
repository: https://github.com/gamai-io/evidence-first-agent-runtime
review_ref: 0e02276df1c99c572949bec59fb8e7d20609a109
reviewed_at: 2026-11-11
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# gamAI Trust Layer / rush

## Review boundary

- System in focus: the repository's shipped `rush` FastAPI task/agent app integrated with first-party trust primitives in its standard checkout, not an assumed enterprise organization of all separately published gamAI components.
- Purpose and identity: accept natural-language sandbox tasks, obtain a bounded optional model-generated command plan, gate commands, execute in a sandbox and return evidence about actual exit results.
- Relevant environment: untrusted user tasks, adversarial instruction patterns, model inference API, Docker/SRT/disposable remote executor, subprocess outputs, false-success claims and human operator deployment.
- Standard-distribution boundary: shipped `rush/agent.py`, `rush/llm.py`, `rush/guard.py`, `rush/executor.py`, `rush/evidence.py`, `rush/app.py` with importable `proofgate` and `agent-immunity`; no claim that separate pip packages, unrelated demos or crossnode benchmark execute inside an ordinary rush task.
- Credited operating / distribution surfaces: `rush` API/UI, optional Vultr model planning, deterministic command and task guards, sandbox executor, chained evidence ledger, proofgate runtime result check and active immunity task scoring.
- Adjacent first-party surfaces excluded from ownership: standalone `crossnode-bench`, benchmark/evaluation corpora, `repro.sh`/GitHub CI, labs, separate deployment demonstrations, developer roadmaps, independent `effect-broker` examples and separately distributed packages not imported into `rush`.
- First-party operating / deployment modes considered: optional configured `VULTR_INFERENCE_KEY` dynamic model planner plus Docker/SRT/Vultr sandbox; no-key deterministic demo fallback; synchronous `/api/run` and streaming `/api/run/stream` interfaces.
- Recursion level: one `rush.Agent.run` task and its bounded command steps; independent web requests may run concurrently but do not automatically become coordinated organizations.
- Reviewed revision: `0e02276df1c99c572949bec59fb8e7d20609a109` (source-static), observation date 2026-11-11.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

The FastAPI endpoint constructs a fresh `Agent` and isolated executor for each task. The agent rejects unsafe task text, asks `VultrInference` to propose at most five shell steps when an API key exists, then checks each proposed command before calling the sandbox. Command outcomes, denial decisions and exit status are emitted, appended to a per-run hash-chained ledger and passed as observed `rc_zero` claims into `proofgate`. On refusal or failed command, execution stops; it does not ask the model to replan. Without inference credentials, `llm.plan` deliberately falls back to fixed deterministic commands, which are not model-owned. Separate agent-immunity, proofgate, crossnode benchmark and effect-broker packages can be used by other harnesses but do not jointly instantiate a metasystem inside rush. [Rush runtime](https://github.com/gamai-io/evidence-first-agent-runtime/blob/0e02276df1c99c572949bec59fb8e7d20609a109/rush/agent.py), [planner](https://github.com/gamai-io/evidence-first-agent-runtime/blob/0e02276df1c99c572949bec59fb8e7d20609a109/rush/llm.py), [app](https://github.com/gamai-io/evidence-first-agent-runtime/blob/0e02276df1c99c572949bec59fb8e7d20609a109/rush/app.py), [architecture/non-goals](https://github.com/gamai-io/evidence-first-agent-runtime/blob/0e02276df1c99c572949bec59fb8e7d20609a109/docs/ARCHITECTURE.md).

## Operational model

In the supported configured-inference mode, one model decides a short command plan for the task; the `rush` deterministic runner may refuse or terminate but does not own plan content. The sandbox is an execution/evidence source, not a second AI S1. `proofgate` evaluates supplied actual return codes; a hash-chain ledger protects event integrity but does not attest the truth of an upstream observation. No-key fallback is deterministic and does not itself establish agent-owned decisions. Independently available trust tools are adjacent consumable primitives unless demonstrably wired into the assessed app.

## S1 — Operations

- State: A
- Function: generate actionable task steps with a model and execute allowed commands in a sandbox to return a task result.
- Disturbance / variety regulated: variable natural-language task demands, model-proposed commands, environment execution errors and safe-action constraints.
- Decisive decision or feedback right: in the configured inference mode, model selects the command sequence and reasons for each step from the user task; fixed runtime then executes/denies each one.
- Decision owner: configured Vultr-hosted LLM for plan selection, invoked by the first-party `llm.plan` path; first-party `Agent` owns deterministic execution and proof reporting.
- Supporting / enforcement mechanisms: injection and destructive-command guard, Docker/SRT/Vultr executor, `Run`/`StepResult`, event emission and proofgate.
- Closure path: `POST /api/run` or SSE → `Agent.run` → `llm.plan` with user task → up to five `Step` commands → guard/executor results → report returned and archived in `RUNS`.
- Boundary reachability: shipped `rush/app.py` creates `Agent()`, whose default `VultrInference` uses a supported environment API key. The dynamic branch calls the model, parses steps and returns them to the packaged runner, unlike a hypothetical unshipped plugin.
- Why this is / is not agent-owned: plan selection can be discretionary in the configured model mode; deterministic no-key sample fallback, sandbox/guard and proof evaluation are not credited as AI cognition.
- Evidence: [model planner and fallback](https://github.com/gamai-io/evidence-first-agent-runtime/blob/0e02276df1c99c572949bec59fb8e7d20609a109/rush/llm.py), [agent execution](https://github.com/gamai-io/evidence-first-agent-runtime/blob/0e02276df1c99c572949bec59fb8e7d20609a109/rush/agent.py#L65-L144), [supported HTTP entrypoints](https://github.com/gamai-io/evidence-first-agent-runtime/blob/0e02276df1c99c572949bec59fb8e7d20609a109/rush/app.py).
- Basis: structural shipped optional model mode; confidence: medium-high.
- Confidence: medium-high.
- Caveats: the model is consulted only once; there is no demonstrated adaptive multi-round replan after failed tool feedback. No credentialed inference execution was repeated during this source-static review.

## S2 — Coordination

- State: —
- Function: no coordination function regulating interaction between distinct S1 operating agents is supplied by the selected rush distribution.
- Disturbance / variety regulated: multiple web requests and sandbox containers may coexist; no demonstrated inter-agent contention, negotiated conflict attenuation or returned operational coordination path is packaged.
- Decisive decision or feedback right: independent requests create their own agent/executor; the five commands within a task are a serial plan of one S1, not five S1 units.
- Decision owner: the app's request/worker mechanics are deterministic and per-run; no first-party cross-unit coordination agent or S2-specific constructor identified.
- Supporting / enforcement mechanisms: per-task Docker volume naming and worker thread/queue transport, executor cleanup, single-run command ordering.
- Closure path: each request returns independent evidence; none exchanges inter-S1 conflict feedback with another task's next operation.
- Why this is / is not agent-owned: infrastructure separation and sequential tool commands do not prove two autonomous S1 cells plus a regulated interference relation.
- Evidence: [app request scope](https://github.com/gamai-io/evidence-first-agent-runtime/blob/0e02276df1c99c572949bec59fb8e7d20609a109/rush/app.py), [single-run loop](https://github.com/gamai-io/evidence-first-agent-runtime/blob/0e02276df1c99c572949bec59fb8e7d20609a109/rush/agent.py).
- Basis: bounded structural absence; confidence: medium-high.
- Confidence: medium-high.
- Caveats: crossnode test rigs are adjacent assessment software, not coordinating two shipped rush operational agents.

### Absence scope

- Surfaces inspected: rush task entrypoints, worker/volume creation, plan/step execution, executor selection, crossnode architecture and integration docs.
- Plausible first-party paths checked: concurrent HTTP runs, Docker volume isolation, sequential step plan, `crossnode-bench` multiple node adapters.
- Why no material first-party path remains: no shipped inter-S1 disturbance-specific arbitration, response owner and return to changed work of two independent S1s; crossnode is a benchmark not rush coordination.

## S3 — Inside-and-now control

- State: —
- Function: no first-party inside-and-now whole-system current resource/commitment negotiation or intervention loop.
- Disturbance / variety regulated: unsafe commands, inference availability, sandbox limits and task failure are locally controlled; no multi-task portfolio control is demonstrated.
- Decisive decision or feedback right: static guard rules and Docker limits enforce configured constraints; request failure ends its run rather than invoking a whole-system current manager.
- Decision owner: developer/operator chooses rules/infrastructure; runtime executes tests and boundaries, not current discretionary tradeoffs across a whole set of operational units.
- Supporting / enforcement mechanisms: `check_task`, `check_command`, 5-step cap, sandbox memory/network policy and return-code halts.
- Closure path: local refusal or stop enters the run report and is sent to one caller; no first-party whole-current decision loops back across operational tasks.
- Why this is / is not agent-owned: enforcement of preselected limits and a task-level stop are not S3 authority over organizational resource/commitment varieties.
- Evidence: [guard rules](https://github.com/gamai-io/evidence-first-agent-runtime/blob/0e02276df1c99c572949bec59fb8e7d20609a109/rush/guard.py), [executor isolation](https://github.com/gamai-io/evidence-first-agent-runtime/blob/0e02276df1c99c572949bec59fb8e7d20609a109/rush/executor.py), [per-run handling](https://github.com/gamai-io/evidence-first-agent-runtime/blob/0e02276df1c99c572949bec59fb8e7d20609a109/rush/agent.py).
- Basis: bounded negative; confidence: medium-high.
- Confidence: medium-high.
- Caveats: operator cloud capacity planning is outside the observed app-level decision loop.

### Absence scope

- Surfaces inspected: `RUNS` registry, app request handling, planner, guard, executor, ledger and deployment modes.
- Plausible first-party paths checked: per-run sandbox resource caps, destructive-command refusal, model step limit, streamed error status and run result ledger.
- Why no material first-party path remains: none supplies an owner with a whole-system current operational view and discretionary action on shared commitments/priorities with returned multi-S1 effect.

## S3* — Complementary audit

- State: —
- Function: no audit-specific complementary, sufficiently independent operational observation and judgment-to-control loop established for live rush beyond its ordinary result check.
- Disturbance / variety regulated: a model may claim a command succeeded incorrectly, addressed by first-party `rc_zero` production verification and ledger integrity checking; these are ordinary result validation, not a separate complementary audit path.
- Decisive decision or feedback right: proofgate deterministically checks `observed` return codes supplied by the same runner, while crossnode independently evaluates node claims only in an adjacent benchmark.
- Decision owner: normal runner/proofgate controls its own task report; crossnode benchmark judge is not part of rush's runtime audit authority.
- Supporting / enforcement mechanisms: `proofgate.check`, hash-chain `Ledger.verify`, separate crossnode test tools/CI.
- Closure path: routine validation creates the final same-run report; no separate auditor acquires independent operational reality and returns a corrective intervention into later task control.
- Why this is / is not agent-owned: a proof hash proves integrity of claimed data, not independent truth of the observation. The standalone benchmark cannot donate an in-boundary S3* actor.
- Evidence: [proofgate claim predicate](https://github.com/gamai-io/evidence-first-agent-runtime/blob/0e02276df1c99c572949bec59fb8e7d20609a109/proofgate/proofgate.py), [ledger and actual wiring](https://github.com/gamai-io/evidence-first-agent-runtime/blob/0e02276df1c99c572949bec59fb8e7d20609a109/rush/agent.py), [architecture trust boundaries](https://github.com/gamai-io/evidence-first-agent-runtime/blob/0e02276df1c99c572949bec59fb8e7d20609a109/docs/ARCHITECTURE.md).
- Basis: bounded negative distinguishing ordinary verification from complementary audit; confidence: medium.
- Confidence: medium.
- Caveats: the adjacent `crossnode-bench` does possess independent ground-truth tests for its own evaluation purpose, not first-party rush S3* closure.

### Absence scope

- Surfaces inspected: proofgate, ledger, rush output/evidence path, crossnode judge, test/CI and architecture trust boundaries.
- Plausible first-party paths checked: `rc_zero` proof checks, hash-chain verification, streamed evidence, crossnode false-success scoring and CI `repro.sh`.
- Why no material first-party path remains: checks inside ordinary reporting merely validate its own supplied execution data; complementary crossnode tests are not installed into rush as independent corrective feedback.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party prospective external-environment analysis, future options generation and return to current capability in the shipped rush task loop.
- Disturbance / variety regulated: malicious prompts and model API failure are observed as immediate task conditions; historical antibody signatures can improve future filters but do not form a prospective S4 options decision.
- Decisive decision or feedback right: `guard.check_task` scores a current prompt; `agent-immunity` contains learning/decay primitives but rush does not operate a first-party external trend/options-to-capability governance circuit.
- Decision owner: developer/operator defines guard thresholds and code; no autonomous or parent prospective adaptation actor/closure supplied.
- Supporting / enforcement mechanisms: immunity threat score, signature/antibody store, deterministic fallback plan, test corpora and proposed skill-evolve utility.
- Closure path: current bad input may be refused; there is no demonstrated future-oriented option selection returning a changed capability through S3 to normal tasks.
- Why this is / is not agent-owned: reactive recognition and stored antibodies alone are not outside-and-then intelligence; adjacent research scripts are not a shipped runtime adaptation mode.
- Evidence: [rush guard](https://github.com/gamai-io/evidence-first-agent-runtime/blob/0e02276df1c99c572949bec59fb8e7d20609a109/rush/guard.py), [antibody store](https://github.com/gamai-io/evidence-first-agent-runtime/blob/0e02276df1c99c572949bec59fb8e7d20609a109/agent-immunity/immunity.py), [architecture and scope](https://github.com/gamai-io/evidence-first-agent-runtime/blob/0e02276df1c99c572949bec59fb8e7d20609a109/docs/ARCHITECTURE.md).
- Basis: bounded negative; confidence: medium.
- Confidence: medium.
- Caveats: future product integration could be added without retrospectively establishing S4 at this ref.

### Absence scope

- Surfaces inspected: rush planner/guard, immunity memory and decay, separate capability demos, lab scripts, trust architecture and roadmap.
- Plausible first-party paths checked: task filtering, antibody learning, adaptive signature matching, model API fallback and standalone skill-evolve scripts.
- Why no material first-party path remains: no reachable first-party outside/future distinctions → alternative adaptations → selected option → changed current-capability return is provided in rush.

## S5 — Policy and identity

- State: —
- Function: no first-party ultimate mission/identity policy adjudication and authoritative return path for the installed rush system.
- Disturbance / variety regulated: destructive commands and prompt injection are refused by static risk policies; these are action-level constraints rather than questions about ultimate system identity.
- Decisive decision or feedback right: whoever deploys the app may alter its code/rules, but no runtime path takes an identity-policy dispute to a legitimate authority and returns an operative new policy.
- Decision owner: external operator/developer owns purpose and guard design; shipped model only chooses task commands within its predetermined policy.
- Supporting / enforcement mechanisms: denylist regexes, injection scoring, sandbox restrictions and mandatory result reporting.
- Closure path: guard refusal changes one command/task, not the governing mission of the next task or the resolution of S3/S4 tension.
- Why this is / is not agent-owned: immutable-ish constraints and refusal outputs do not possess identity-level authority just because they are strict.
- Evidence: [guard](https://github.com/gamai-io/evidence-first-agent-runtime/blob/0e02276df1c99c572949bec59fb8e7d20609a109/rush/guard.py), [sandbox policy](https://github.com/gamai-io/evidence-first-agent-runtime/blob/0e02276df1c99c572949bec59fb8e7d20609a109/rush/executor.py), [README non-goals](https://github.com/gamai-io/evidence-first-agent-runtime/blob/0e02276df1c99c572949bec59fb8e7d20609a109/README.md).
- Basis: bounded negative; confidence: medium-high.
- Confidence: medium-high.
- Caveats: human policy making may govern a deployment, but the first-party closed parent S5 route is not supplied.

### Absence scope

- Surfaces inspected: guard/policy rules, planner prompt, executor configuration, run ledger/report, trust architecture and public project governance docs.
- Plausible first-party paths checked: sandbox policy, owner deployment settings, static instruction policy, task refusal and integrity report.
- Why no material first-party path remains: none delegates or closes an ultimate identity/mission policy judgment that returns to govern subsequent operations.

## Distributed OSS parent arrangement

The source repository's multiple research/test subsystems and contributors do not imply a shared operational VSM parent for rush. Any operator/developer policy choices above an installed app remain external unless a function-specific returned governance mode is shipped.

## Self-hosted and non-human modes

Rush may run under Docker, SRT or a remote disposable sandbox; a configured external model owns command-plan selection in the positive S1 mode. With no inference key it uses fixed fallback commands, so an offline deterministic demo alone is not evidence of S1 `A`. No distinct supported parent S3/S4/S5 mode closes the relevant function merely through guard configuration.

## Recursion

The model planner and bounded command executor form one operational work unit. Multiple commands, worker threads, different sandbox backends and independent trust libraries do not establish viable nested S1 units or a first-party metasystem on their own.

## Variety and escalation

Guard rejections, sandbox isolation, finite plans, execution stop-on-failure, rc checks, evidence hashing and optional antibody memory attenuate risk and false-success varieties. A refusal is recorded and returned to the caller rather than automatically becoming a strategic or ultimate-policy escalation.

## Evidence gaps

- No live Vultr inference, Docker/SRT/Vultr cloud session or independent audit reviewer was executed during this source-static assessment.
- No-key deterministic fallback is explicitly separated from supported configured model planning; observed task-output quality is not scored.
- Trust libraries are useful first-party products, but only verified runtime wiring into the declared rush boundary can establish a positive S-function for this general assessment.

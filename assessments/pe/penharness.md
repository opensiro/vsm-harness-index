---
harness_id: penharness
project_name: PenHarness
repository: https://github.com/morphllm/PenHarness
review_ref: 83c540fa9fe9f65b75d949b44e9199f02eb2bea6
reviewed_at: 2026-11-19
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: ?
autonomy_s4: —
autonomy_s5: —
---

# PenHarness

## Review boundary

- System in focus: shipped opencode-based authorized-hunt composition: installed lead/worker/lane roles, continuation plugin, fleet scripts and engagement artifacts.
- Purpose and identity: produce reproducible evidence-graded authorized investigation outcomes and a consolidated report.
- Relevant environment: explicitly authorized target/source evidence, local operator, model provider, optional cloud sandboxes and worker/task state.
- Standard-distribution boundary: root opencode config/AGENTS/skills/plugin, fleet.py bootstrap and role prompts, hunt templates; optional queue-backed shell operating mode inspected separately.
- Credited operating / distribution surfaces: configured native lead composition, bootstrapped worker/lane roles, status/proposal/harvest/steer/resource controls, shared evidence/ownership doctrine.
- Adjacent first-party surfaces excluded from ownership: historical target/hunt outcome anecdotes, reference-case performance claims, generic opencode internals, cloud/browser provider internals and repository maintainer governance. Outward security audit is S1 product work, not automatically the harness's S3*.
- First-party operating / deployment modes considered: default local lead/subagents; boat/fly fleet with fresh HTTP worker sessions and reactive lanes; documented manual operator fleet CLI; optional legacy queue scripts distinguished from main HTTP dispatch.
- Recursion level: one bounded engagement with operational investigation cells and local operator parent; no vendor or OSS organization governance borrowed.
- Reviewed revision: `83c540fa9fe9f65b75d949b44e9199f02eb2bea6`.
- Observation date: 2026-11-19.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

PenHarness is a first-party installed composition over external opencode execution, not a reimplementation of that engine. Root config binds provider and skills; AGENTS and the hunt skill specify operational roles, evidence contract, ownership and control. An idle-event plugin resumes the same prepared root session, excludes child/one-shot/other-project sessions and uses bounded backoff. The lead model remains the decision owner; repeating a prompt is deterministic support.

fleet.py bootstraps the supplied role/skill/plugin/config into provider workers, starts one fresh model session per task, maintains lane sessions and returns mailbox/proposal/health/finding state. Harvest centralizes worker artifacts with ID deduplication; down harvests before destroying resources. Model doctrine requires disjoint topics, checking dead ends and lead-owned central merges. The optional shell mode uses flock to claim queued tasks. These are documented supported modes, without certifying perfect synchronization or legal/security enforcement. The source-visible tree has no identified license; this assessment quotes no implementation payload and grants no reuse/contribution right.

Primary sources: [fleet lifecycle/roles/harvest](https://github.com/morphllm/PenHarness/blob/83c540fa9fe9f65b75d949b44e9199f02eb2bea6/fleet.py), [installed lead doctrine](https://github.com/morphllm/PenHarness/blob/83c540fa9fe9f65b75d949b44e9199f02eb2bea6/AGENTS.md), [hunt workflow](https://github.com/morphllm/PenHarness/blob/83c540fa9fe9f65b75d949b44e9199f02eb2bea6/skills/whitehat-hunt/SKILL.md), [idle continuation plugin](https://github.com/morphllm/PenHarness/blob/83c540fa9fe9f65b75d949b44e9199f02eb2bea6/.opencode/plugins/hunt-loop.js), [default provider/skill binding](https://github.com/morphllm/PenHarness/blob/83c540fa9fe9f65b75d949b44e9199f02eb2bea6/opencode.json), [worker provider configuration](https://github.com/morphllm/PenHarness/blob/83c540fa9fe9f65b75d949b44e9199f02eb2bea6/fly/opencode.json), [supported deployment/manual CLI](https://github.com/morphllm/PenHarness/blob/83c540fa9fe9f65b75d949b44e9199f02eb2bea6/README.md), [queue worker](https://github.com/morphllm/PenHarness/blob/83c540fa9fe9f65b75d949b44e9199f02eb2bea6/skills/whitehat-hunt/ops/worker.sh), [atomic queue append](https://github.com/morphllm/PenHarness/blob/83c540fa9fe9f65b75d949b44e9199f02eb2bea6/skills/whitehat-hunt/ops/enqueue.sh), [optional queue-backed mode](https://github.com/morphllm/PenHarness/blob/83c540fa9fe9f65b75d949b44e9199f02eb2bea6/skills/whitehat-hunt/ops/README.md), [engagement boundary template](https://github.com/morphllm/PenHarness/blob/83c540fa9fe9f65b75d949b44e9199f02eb2bea6/hunts/TEMPLATE/scope.md), [hunt state layout](https://github.com/morphllm/PenHarness/blob/83c540fa9fe9f65b75d949b44e9199f02eb2bea6/hunts/TEMPLATE/README.md).

## Operational model

Native configured models own investigation decisions. The installed lead also chooses disjoint ownership and current collective capacity/priorities from shared state. Fleet/provider machinery transports or enforces decisions. External opencode/provider internal VSM functions are not inherited. Ordinary proof/control generation belongs to production; the separate independent-verification wording is preserved as a concrete S3* uncertainty.

## S1 — Operations

- State: A
- Function: produce evidence-graded authorized security investigation findings and reports through model-led task cells.
- Disturbance / variety regulated: unknown target behavior/source, false hypotheses, failures and evidence that changes an investigation.
- Decisive decision or feedback right: choose the next scoped investigation action, falsify a hypothesis and report a supported outcome.
- Decision owner: configured lead/lane/worker models in the first-party installed composition; opencode supplies the external execution engine.
- Supporting / enforcement mechanisms: opencode HTTP/CLI transport, packaged roles/skills/provider config, fresh sessions, fleet scripts, file artifacts and idle continuation.
- Closure path: worker actions produce evidence/files; harvest and mailbox reports reach the lead, which chooses new task cells, correction or termination.
- Boundary reachability: default opencode.json binds supplied skills/model, the plugin resumes prepared root sessions, and fleet bootstrap copies AGENTS/skills/plugin/config into workers before native fresh-session prompts. This is a shipped composition, not a claim about all opencode internals.
- Why this is / is not agent-owned: the models choose task-dependent investigations and evidence disposition; HTTP dispatch, JSON parsing and repeat ticks transport their choices.
- Evidence: [default provider/skill binding](https://github.com/morphllm/PenHarness/blob/83c540fa9fe9f65b75d949b44e9199f02eb2bea6/opencode.json), [installed lead doctrine](https://github.com/morphllm/PenHarness/blob/83c540fa9fe9f65b75d949b44e9199f02eb2bea6/AGENTS.md), [hunt workflow](https://github.com/morphllm/PenHarness/blob/83c540fa9fe9f65b75d949b44e9199f02eb2bea6/skills/whitehat-hunt/SKILL.md), [idle continuation plugin](https://github.com/morphllm/PenHarness/blob/83c540fa9fe9f65b75d949b44e9199f02eb2bea6/.opencode/plugins/hunt-loop.js), [fleet lifecycle/roles/harvest](https://github.com/morphllm/PenHarness/blob/83c540fa9fe9f65b75d949b44e9199f02eb2bea6/fleet.py), [worker provider configuration](https://github.com/morphllm/PenHarness/blob/83c540fa9fe9f65b75d949b44e9199f02eb2bea6/fly/opencode.json)
- Basis: structural.
- Confidence: medium-high.
- Caveats: source-only assessment of the supplied workflow. No target, model, cloud fleet, credential or security test was used; prompt-based control is not a security-enforcement guarantee.

## S2 — Coordination

- State: A
- Function: attenuate overlapping investigation ownership, duplicate work and conflicting central-ledger writes among work cells.
- Disturbance / variety regulated: parallel lanes/workers can reopen already falsified hypotheses, duplicate probes and contend over shared findings.
- Decisive decision or feedback right: choose disjoint task ownership and revise/deduplicate proposed work against the shared proven/dead state before dispatch.
- Decision owner: installed lead model and worker/lane models following the packaged coordination role; fixed queues/parser support those decisions.
- Supporting / enforcement mechanisms: one-topic ownership, lead-only central merge, per-worker artifacts, shared dead-end ledger, fresh-session identity, optional flock-backed task dequeue and project-local plugin filtering.
- Closure path: workers/lanes inspect existing results before work; proposals and findings return through harvest/mailbox; lead deduplication and new disjoint dispatch change subsequent work.
- Boundary reachability: lead doctrine, worker/lane prompts and bootstrap supply the specific anti-duplication/ownership loop; optional queue scripts add mechanical exclusive task claims.
- Why this is / is not agent-owned: the model chooses topic/ownership changes from actual shared evidence. Queue locks, single merge writer and session filters do not themselves own that choice; delegation alone is not the witness.
- Evidence: [installed lead doctrine](https://github.com/morphllm/PenHarness/blob/83c540fa9fe9f65b75d949b44e9199f02eb2bea6/AGENTS.md), [hunt workflow](https://github.com/morphllm/PenHarness/blob/83c540fa9fe9f65b75d949b44e9199f02eb2bea6/skills/whitehat-hunt/SKILL.md), [fleet lifecycle/roles/harvest](https://github.com/morphllm/PenHarness/blob/83c540fa9fe9f65b75d949b44e9199f02eb2bea6/fleet.py), [queue worker](https://github.com/morphllm/PenHarness/blob/83c540fa9fe9f65b75d949b44e9199f02eb2bea6/skills/whitehat-hunt/ops/worker.sh), [atomic queue append](https://github.com/morphllm/PenHarness/blob/83c540fa9fe9f65b75d949b44e9199f02eb2bea6/skills/whitehat-hunt/ops/enqueue.sh), [idle continuation plugin](https://github.com/morphllm/PenHarness/blob/83c540fa9fe9f65b75d949b44e9199f02eb2bea6/.opencode/plugins/hunt-loop.js)
- Basis: structural.
- Confidence: medium-high.
- Caveats: prose coordination and lead discipline are not a global atomic reservation guarantee. Main HTTP dispatch does not implement the optional shell queue; JSONL append/harvest are not certified race-free.

- Distinct S1 units: separate model-backed lane/worker task sessions contributing evidence to one engagement.
- Inter-S1 disturbance: duplicate/reopened probes waste shared target/compute allowance, while multiple writers could corrupt or contradict the central findings view.
- Attenuating coordination relation: disjoint topic ownership, shared dead-end/proven evidence before proposing work, lead deduplication, worker-local outputs and one central merge owner.
- Feedback into subsequent S1 behaviour: harvested findings/proposals/dead ends alter the next work inventory and prevent redispatch of known-dead or already-owned work.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the installed instructions tie these channels to concrete duplicate-work and shared-ledger interference, with changed later work; mailbox existence alone is not credited.

## S3 — Inside-and-now control

- State: A(P)
- Function: regulate current hunt commitments and fleet capacity from collective health/progress/evidence.
- Disturbance / variety regulated: idle/unhealthy workers, saturated lanes, changing priorities and continuing cloud cost across the active engagement.
- Decisive decision or feedback right: base: choose capacity, lane priorities, dispatch/reseed/steer and teardown; parent: inspect fleet status and exercise the same documented operator resource/commitment commands.
- Decision owner: base: installed lead model. Parent mode: authorized engagement operator holding the local fleet controls.
- Supporting / enforcement mechanisms: fleet-state.json, status health/session/finding summaries, proposal/mailbox return, up/lane/dispatch/steer/harvest/down and TTL.
- Closure path: lead loop reads current ledger/status/harvest and chooses further allocation/intervention; up/down actually provision/destroy workers, steer changes a live lane's next turn. Operator commands return durable fleet state/status and change active work.
- Boundary reachability: the idle plugin explicitly asks the installed lead to inspect current state and select parallel next actions; fleet.py binds those choices to native provider/session actions. README documents manual CLI operation as another supported control mode.
- Why this is / is not agent-owned: model/operator owns resource/priority choices. TTL, round-robin placement, health probes and destruction APIs execute/enforce them; neither mere initial task decomposition nor a machine named lead establishes S3.
- Evidence: [idle continuation plugin](https://github.com/morphllm/PenHarness/blob/83c540fa9fe9f65b75d949b44e9199f02eb2bea6/.opencode/plugins/hunt-loop.js), [installed lead doctrine](https://github.com/morphllm/PenHarness/blob/83c540fa9fe9f65b75d949b44e9199f02eb2bea6/AGENTS.md), [hunt workflow](https://github.com/morphllm/PenHarness/blob/83c540fa9fe9f65b75d949b44e9199f02eb2bea6/skills/whitehat-hunt/SKILL.md), [fleet lifecycle/roles/harvest](https://github.com/morphllm/PenHarness/blob/83c540fa9fe9f65b75d949b44e9199f02eb2bea6/fleet.py), [supported deployment/manual CLI](https://github.com/morphllm/PenHarness/blob/83c540fa9fe9f65b75d949b44e9199f02eb2bea6/README.md)
- Basis: structural.
- Confidence: medium-high.
- Caveats: A refers to the admitted lead composition, not an autonomous cloud account authority or externally hosted agent internals. P is local engagement operation, not project-wide governance.

- Whole-system current view: fleet-state inventory, per-machine health/session activity/finding counts, lane proposals/mailboxes and merged proven/dead evidence.
- Current-control decision scope: present worker capacity, lane priorities/commitments, reseeding and end-of-engagement resource release.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Installed lead model | Current fleet state, health, returned lane evidence/proposals, idle/saturated capacity | Chooses up/dispatch/steer/reseed/down; returned state/evidence governs the next loop | [idle continuation plugin](https://github.com/morphllm/PenHarness/blob/83c540fa9fe9f65b75d949b44e9199f02eb2bea6/.opencode/plugins/hunt-loop.js), [installed lead doctrine](https://github.com/morphllm/PenHarness/blob/83c540fa9fe9f65b75d949b44e9199f02eb2bea6/AGENTS.md), [fleet lifecycle/roles/harvest](https://github.com/morphllm/PenHarness/blob/83c540fa9fe9f65b75d949b44e9199f02eb2bea6/fleet.py) |
| Parent (`P`) | Authorized local operator | Documented manual inspection of fleet status and current engagement work | Manual capacity/steer/down commands affect actual worker resources and lane sessions | [supported deployment/manual CLI](https://github.com/morphllm/PenHarness/blob/83c540fa9fe9f65b75d949b44e9199f02eb2bea6/README.md), [fleet lifecycle/roles/harvest](https://github.com/morphllm/PenHarness/blob/83c540fa9fe9f65b75d949b44e9199f02eb2bea6/fleet.py) |

## S3* — Complementary audit

- State: ?
- Function: a concrete independent-verification instruction exists, but complementary audit ownership/closure cannot be reconstructed unambiguously.
- Disturbance / variety regulated: a composer's proposed chain or reported evidence can be unsupported by the underlying observations.
- Decisive decision or feedback right: which separate actor owns a complementary claim-relative audit, rather than ordinary production proof/control generation, is unresolved.
- Decision owner: not established for S3*; lead, composers and workers are named but no distinct verifier authority is bound.
- Supporting / enforcement mechanisms: fresh worker sessions, raw proof/control artifacts, candidate queue and central ledger admission.
- Closure path: workflow says composer output must not enter the ledger until independently verified and can become fleet queue work; source does not specify the verifying actor/evidence-selection independence sufficiently to establish positive audit or bounded absence.
- Why this is / is not agent-owned: ordinary worker controls and outward audits of the target are S1. The explicit independent composer-verification path is specific enough to prevent simply publishing absence, but generic fresh-session dispatch is not sufficient C/A evidence.
- Evidence: [hunt workflow](https://github.com/morphllm/PenHarness/blob/83c540fa9fe9f65b75d949b44e9199f02eb2bea6/skills/whitehat-hunt/SKILL.md), [fleet lifecycle/roles/harvest](https://github.com/morphllm/PenHarness/blob/83c540fa9fe9f65b75d949b44e9199f02eb2bea6/fleet.py), [installed lead doctrine](https://github.com/morphllm/PenHarness/blob/83c540fa9fe9f65b75d949b44e9199f02eb2bea6/AGENTS.md)
- Basis: structural.
- Confidence: medium-high.
- Caveats: No live trace is required by this assessment as a new threshold. The gap is source-level role/claim/independence/return interpretation of the shipped independent-verification step; separate contexts alone do not settle it.

## S4 — Outside-and-then intelligence

- State: —
- Function: no supplied prospective adaptation loop for the harness's future organizational capability.
- Disturbance / variety regulated: new target/source/advisory facts alter the current investigation plan.
- Decisive decision or feedback right: no harness-capability option selection and prospective adoption return established.
- Decision owner: models choose investigation tasks/lanes; methodology/configuration changes remain developer/operator inputs.
- Supporting / enforcement mechanisms: external source reading, advisory lookup, current lane invention, evidence ledger/dead ends and fixed skill/config files.
- Closure path: external facts grow the next hunt actions/chains, the primary product outcome; no first-party reusable capability/strategy evaluation and adoption loop alters the harness for future environments.
- Why this is / is not agent-owned: external reconnaissance and discovering new investigation branches are S1, not automatically S4; a skill authored from a past engagement is historical development evidence.
- Evidence: [hunt workflow](https://github.com/morphllm/PenHarness/blob/83c540fa9fe9f65b75d949b44e9199f02eb2bea6/skills/whitehat-hunt/SKILL.md), [idle continuation plugin](https://github.com/morphllm/PenHarness/blob/83c540fa9fe9f65b75d949b44e9199f02eb2bea6/.opencode/plugins/hunt-loop.js), [installed lead doctrine](https://github.com/morphllm/PenHarness/blob/83c540fa9fe9f65b75d949b44e9199f02eb2bea6/AGENTS.md), [fleet lifecycle/roles/harvest](https://github.com/morphllm/PenHarness/blob/83c540fa9fe9f65b75d949b44e9199f02eb2bea6/fleet.py), [hunt state layout](https://github.com/morphllm/PenHarness/blob/83c540fa9fe9f65b75d949b44e9199f02eb2bea6/hunts/TEMPLATE/README.md)
- Basis: structural.
- Confidence: medium-high.
- Caveats: the target's possible future risks are part of the investigation product; they do not establish adaptation of this harness.

### Absence scope

- Surfaces inspected: lead/worker/lane prompts, hunt loop, task/proposal/ledger flow, setup/skill/configuration surfaces and fleet lifecycle.
- Plausible first-party paths checked: new lanes, externally sourced advisory/source facts, accumulated dead ends and past-hunt methodology improvements.
- Why no material first-party path remains: these close the engagement's current investigative work without a supplied external/prospective distinction→harness capability options→returned adaptation decision; hypothetical self-rewriting would require additional composition.

## S5 — Policy and identity

- State: —
- Function: no runtime identity/ultimate-policy adjudication and governing return established.
- Disturbance / variety regulated: engagement scope, authorized targets/credentials, fixed red lines and publication permission constrain work.
- Decisive decision or feedback right: no explicit ultimate-policy issue-resolution path, as distinct from missing task authorization or credentials.
- Decision owner: user writes initial scope and approves publication; static safety/mission rules come from the supplied role.
- Supporting / enforcement mechanisms: scope/brief files, fixed red list, model instructions and plugin readiness/pause/blocked notes.
- Closure path: missing scope/credentials causes planning/stop/notes; supplying task scope or ordinary permission does not implement an identity-policy dispute resolution.
- Why this is / is not agent-owned: a written authorization file and final human permission are not sufficient S5 evidence. The plugin checks readiness, not legitimate policy authority.
- Evidence: [engagement boundary template](https://github.com/morphllm/PenHarness/blob/83c540fa9fe9f65b75d949b44e9199f02eb2bea6/hunts/TEMPLATE/scope.md), [installed lead doctrine](https://github.com/morphllm/PenHarness/blob/83c540fa9fe9f65b75d949b44e9199f02eb2bea6/AGENTS.md), [hunt workflow](https://github.com/morphllm/PenHarness/blob/83c540fa9fe9f65b75d949b44e9199f02eb2bea6/skills/whitehat-hunt/SKILL.md), [idle continuation plugin](https://github.com/morphllm/PenHarness/blob/83c540fa9fe9f65b75d949b44e9199f02eb2bea6/.opencode/plugins/hunt-loop.js), [hunt state layout](https://github.com/morphllm/PenHarness/blob/83c540fa9fe9f65b75d949b44e9199f02eb2bea6/hunts/TEMPLATE/README.md)
- Basis: structural.
- Confidence: medium-high.
- Caveats: scope controls here are largely instruction-based, not a claim of comprehensive enforcement. No external target permission is inferred or exercised by this assessment.

### Absence scope

- Surfaces inspected: scope/brief templates, red-list/authorization instructions, setup/readiness, pause/blocked reporting, lead and worker operating roles.
- Plausible first-party paths checked: out-of-scope stops, user-written scope updates, publication consent, missing-credential questions and pause/resume as possible parent-policy channels.
- Why no material first-party path remains: none supplies a function-specific identity/ultimate-policy matter→legitimate adjudicator→authoritative governing return; external vendor/institution governance is not wired into this runtime.

## Distributed OSS parent arrangement

Only the authorized local engagement operator is a reconstructed parent in the manual current-control mode. No distributed project-recursion governance follows from public contributors or the target's ownership.

## Self-hosted and non-human modes

Local and remote modes use supplied roles. The main lead may regulate work autonomously within an authorized engagement; manual CLI fleet operation is a distinct P mode. Provider access/permissions and target authorization are prerequisites, not granted by running a script.

## Recursion

Lead/lanes/workers form task and control relationships; hierarchy, fresh contexts and model tiers do not prove recursively viable organizations.

## Variety and escalation

Shared evidence narrows repeated work; lane mailboxes return findings/blockers/proposals to current control. Missing credentials/scope stop active work. Runtime readiness and pause files are not automatically algedonic or S5 channels. Source instructions are evidence of the supported composition, not commands executed by this assessment.

## Evidence gaps

All 31 pinned blobs inventoried; roles/skill, complete plugin, fleet lifecycle/dispatch/status/harvest, queue scripts/config/templates inspected. S3* retains a specific unresolved independent-composer-verification interpretation. No target request, investigation, model call, fleet provisioning or independent secondary review was executed; no historical security-outcome or safety claim is adopted.

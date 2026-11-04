---
harness_id: plumb
project_name: Plumb
repository: https://github.com/Inception3D/Plumb
review_ref: 02ea0be7f4a17cd04e8569dbc9749c3ebf18faf4
reviewed_at: 2026-11-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Plumb

## Review boundary

- System in focus: One task-directory coding agent reconstructing one real-world scene in MuJoCo from a video under the first-party Plumb task prompt, installed `real2sim` skill and GPU perception/tool environment. The agent is an externally launched Codex or Claude session; its model/tool cycle is in scope when run in the shipped task environment, but its provider's unrelated orchestration is not credited.
- Purpose and identity: Produce an executable, editable, physically causal reconstruction from a single video with `scene.xml`, an initial state, parameters, a self-contained passive simulation program and a full-length preview.
- Relevant environment: Input video, temporal frames, occlusions and contacts, SAM3 segmentation and Pi3X geometry estimates, physical constraints, MuJoCo rollout, finite GPU capacity, human research operators and offline benchmark datasets.
- Standard-distribution boundary: First-party task-directory generator copies `PROMPT.md`, read-only skills/tool helpers and local `r2s` package. The operator then launches Codex/Claude in that directory and separately runs a host GPU queue service; the code-generation model itself is external.
- Credited operating / distribution surfaces: [README execution recipe](https://github.com/Inception3D/Plumb/blob/02ea0be7f4a17cd04e8569dbc9749c3ebf18faf4/README.md), [task setup](https://github.com/Inception3D/Plumb/blob/02ea0be7f4a17cd04e8569dbc9749c3ebf18faf4/src/harness/new_task.py), [agent task contract](https://github.com/Inception3D/Plumb/blob/02ea0be7f4a17cd04e8569dbc9749c3ebf18faf4/src/prompts/task.md), [real2sim skill](https://github.com/Inception3D/Plumb/blob/02ea0be7f4a17cd04e8569dbc9749c3ebf18faf4/src/SKILL.md), [GPU service](https://github.com/Inception3D/Plumb/blob/02ea0be7f4a17cd04e8569dbc9749c3ebf18faf4/src/harness/gpu_service.py), [tool request/response loop](https://github.com/Inception3D/Plumb/blob/02ea0be7f4a17cd04e8569dbc9749c3ebf18faf4/src/tools/_gpu_call.py), [simulation comparators](https://github.com/Inception3D/Plumb/blob/02ea0be7f4a17cd04e8569dbc9749c3ebf18faf4/src/r2s/sim.py), [deliverable checks](https://github.com/Inception3D/Plumb/blob/02ea0be7f4a17cd04e8569dbc9749c3ebf18faf4/src/r2s/deliver.py), [offline benchmark](https://github.com/Inception3D/Plumb/blob/02ea0be7f4a17cd04e8569dbc9749c3ebf18faf4/benchmark/README.md).
- Adjacent first-party surfaces excluded from ownership: SAM3 and Pi3X third-party model weights and inference internals, MuJoCo as external physics simulator, Codex/Claude provider governance, independent university/research-paper evaluation, optional benchmark scoring after task delivery and any unspecified external agent coordination.
- First-party operating / deployment modes considered: Single video/task agent; multiple task directories with a shared GPU service; host GPU slots `0,0,1` and bounded FIFO; optional CLI tools and repeated offline fitting; benchmark loop over fifty videos with a separate evaluator.
- Recursion level: One video reconstruction cell; higher-level laboratory or benchmark batch ownership remains with a human/operator script, not with a first-party supervising model.
- Reviewed revision: `02ea0be7f4a17cd04e8569dbc9749c3ebf18faf4`.
- Observation date: 2026-11-04.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

`new_task.py` sets up a directory with a single immutable input video, a strict reconstruction prompt and a read-only model/tool reference. An external coding-agent CLI is invoked inside that workspace and may choose how to inspect images, call tools, infer mechanism geometry, write physics XML/Python and repeatedly test offline renders against the video. The Pi3X/SAM3 tools write JSON requests to `.gpu/requests`; the host GPU service validates all paths remain in the task, schedules a free GPU slot under a lock, runs the relevant external perception worker and returns JSON results via `.gpu/results`. The tool client content-deduplicates requests, attaches to pending jobs and retries failed results. Helpers expose video timeline/track inspection, rendered comparison and passive rollout; `r2s deliver --validate-only` checks structural and dynamic output constraints. The optional fifty-video benchmark loops separately started Codex sessions and evaluates exported scenes, including a held-out second camera; this is an experiment, not a standing supervisor inside the agent's current task.

## Operational model

The only credited autonomous S1 operation is the configured single-video coding model using observations, perception tools and MuJoCo feedback to reconstruct a physical scene. Multiple videos are distinct S1 cells when an external operator launches them, but Plumb supplies no supervising model that regulates their priorities or resolves cross-cell conflicts. The GPU queue owns deterministic slot allocation and protection of local paths; it has no authority to decide a physical model or adjust an organizational mission. The operator chooses videos, CLI/model, available GPU slots and benchmark evaluation. Static causal constraints in `PROMPT.md` govern a run, not a shown S5-level identity-decision loop.

## S1 — Operations

- State: A
- Function: Reconstruct one observed physical scene into an executable MuJoCo model under causal and deliverable constraints.
- Disturbance / variety regulated: Partial video observation, uncertain camera geometry, object segmentation, hidden forces and mechanisms, initial conditions, contact parameters and simulation mismatch.
- Decisive decision or feedback right: The running coding model chooses which video/perception/geometry tools to invoke, which scene assumptions to make, how to modify `scene.xml`/initial state/parameters and when to rerun comparison and deliver.
- Decision owner: Codex/Claude model in the provided task workspace, once installed and launched by an operator; not the Pi3X/SAM3 perception models by themselves.
- Supporting / enforcement mechanisms: `PROMPT.md` physical restrictions, read-only `real2sim` tool reference, path-scoped GPU JSON queue, MuJoCo rollout, track-compare tools and deterministic deliverable validator.
- Closure path: Read video and timestamps → call Pi3X/SAM3 → infer and write physics scene → simulate and compare predicted frames/tracks → revise scene assumptions and parameters or deliver a constrained reconstruction.
- Boundary reachability: The README explicitly launches `codex exec ... < PROMPT.md` or `claude -p ...` after generating the task; the prompt requires both GPU tools and grants writing output files. The model-bearing cycle is supplied by those standard CLI agents inside the first-party environment.
- Why this is / is not agent-owned: Choices among observations, tool requests and iterative model edits are assigned to the coding model; the GPU executor and numerical checkers return measurements but do not choose reconstruction policy.
- Evidence: [README launch and outputs](https://github.com/Inception3D/Plumb/blob/02ea0be7f4a17cd04e8569dbc9749c3ebf18faf4/README.md), [agent reconstruction instructions](https://github.com/Inception3D/Plumb/blob/02ea0be7f4a17cd04e8569dbc9749c3ebf18faf4/src/prompts/task.md), [tool/feedback reference](https://github.com/Inception3D/Plumb/blob/02ea0be7f4a17cd04e8569dbc9749c3ebf18faf4/src/SKILL.md), [simulation comparisons](https://github.com/Inception3D/Plumb/blob/02ea0be7f4a17cd04e8569dbc9749c3ebf18faf4/src/r2s/sim.py).
- Basis: explicit + structural.
- Confidence: high for the documented and implemented model/tool operating path; no live gated SAM3/Codex execution was performed for this review.
- Caveats: Execution requires separately provisioned model API/CLI, CUDA weights and GPU environments; success or reconstruction quality is not inferred from documentation alone.

## S2 — Coordination

- State: —
- Function: No active first-party peer-regulation loop among simultaneously acting independent reconstruction agents is established.
- Disturbance / variety regulated: Competing GPU usage among parallel tasks is serialized by fixed slots; task result/assumption conflict between agents is not agent-managed.
- Decisive decision or feedback right: Resolve cross-task or inter-agent incompatibilities and feed coordinated changes to the participating S1 units; not supplied.
- Decision owner: Deterministic GPU worker queue allocates available hardware slots. No model-bearing S2 coordinator decides conflict remedies.
- Supporting / enforcement mechanisms: Per-task filesystem containment, SHA-keyed request deduplication, host `free` slot list and lock, result files and bounded waiting.
- Closure path: Queue contention → scheduling/waiting → worker result; this is resource enforcement for tools, not agent-led peer conflict recognition and correction.
- Boundary reachability: The README offers multi-task GPU service and the benchmark starts one independent agent per directory; it does not expose cross-agent negotiation, collision classification or reallocation of S1 commitments.
- Why this is / is not agent-owned: `threading.Lock`, fixed GPU slots and per-task file separation have no semantic discretion over inter-S1 work.
- Evidence: [multi-task host slots](https://github.com/Inception3D/Plumb/blob/02ea0be7f4a17cd04e8569dbc9749c3ebf18faf4/src/harness/gpu_service.py), [GPU request idempotence](https://github.com/Inception3D/Plumb/blob/02ea0be7f4a17cd04e8569dbc9749c3ebf18faf4/src/tools/_gpu_call.py), [benchmark sequential task launch](https://github.com/Inception3D/Plumb/blob/02ea0be7f4a17cd04e8569dbc9749c3ebf18faf4/benchmark/README.md).
- Basis: structural + explicit.
- Confidence: high for the shipped distribution.
- Caveats: An external lab could build its own S2 layer; it is not bundled or evidenced by Plumb.

### Absence scope

- Surfaces inspected: Task prompt, standalone coding-agent launcher, GPU queue, deduplication client, multi-task GPU slots and fifty-video benchmark script.
- Plausible first-party paths checked: GPU scheduling as coordination; multiple task directories as agent team; shared perception workers as a conflict regulator; benchmark loop as a task society.
- Why no material first-party path remains: All paths either isolate single-video agents, deterministically queue a GPU function, or serially run unrelated episodes; no inter-agent disturbance diagnosis → corrective coordination decision → adjusted S1 behavior is present.

## S3 — Inside-and-now control

- State: —
- Function: No separate active whole-current management of the multi-video system or independent operational cells.
- Disturbance / variety regulated: Concurrent workload/GPU contention and within-scene fitting are visible as low-level resource or S1 execution issues; a first-party current whole-system controller is not implemented.
- Decisive decision or feedback right: Reallocate priorities, commitments, monitoring or recovery between multiple active task agents with feedback to those agents; not demonstrated.
- Decision owner: Human/research operator launches tasks and chooses GPU slots; the GPU service follows fixed first-available order, and each coding model regulates only its own video.
- Supporting / enforcement mechanisms: Host queue and log, per-task process launch, JSON output status and final deliverable checks.
- Closure path: Per-task progress/timeout → shell retry or human operator action; no first-party whole-system control decision returns into the allocation of task commitments.
- Boundary reachability: The provided benchmark loop executes task directories independently, and `gpu_service.py` has neither model-bearing whole-current policy nor authority to redirect coding agents.
- Why this is / is not agent-owned: Within-task model self-correction is S1; deterministic GPU slot management and external human choice do not establish a separately reachable S3 manager or a complete parent S3 loop at project recursion.
- Evidence: [batch evaluation protocol](https://github.com/Inception3D/Plumb/blob/02ea0be7f4a17cd04e8569dbc9749c3ebf18faf4/benchmark/README.md), [host GPU queue](https://github.com/Inception3D/Plumb/blob/02ea0be7f4a17cd04e8569dbc9749c3ebf18faf4/src/harness/gpu_service.py), [task setup](https://github.com/Inception3D/Plumb/blob/02ea0be7f4a17cd04e8569dbc9749c3ebf18faf4/src/harness/new_task.py).
- Basis: structural.
- Confidence: high for shipped first-party control routes.
- Caveats: Generic external CLI agent planning is not a whole-system S3 claim.

### Absence scope

- Surfaces inspected: One-video prompt, task generator, GPU service, CLI launch, offline benchmark runner and output validation.
- Plausible first-party paths checked: A coding-agent internal work plan; host GPU slot list as central resource authority; research benchmark as a project controller; manual ability to stop and restart an individual job.
- Why no material first-party path remains: These control one S1 task, enforce hardware budgets, or describe separate manual research steps; no actionable multi-cell view and corrective whole-current owner is established at the declared recursion.

## S3* — Complementary audit

- State: —
- Function: No sufficiently independent complementary audit of operational claims that returns a corrective judgment to a distinct in-boundary controlling authority is established.
- Disturbance / variety regulated: Scene/video mismatch and non-physical output are measured by normal task tools; held-out benchmark evaluation occurs after tasks, without an operating audit-to-control return path.
- Decisive decision or feedback right: Independently access actual operating evidence beyond routine reports, flag a specific suspect claim and deliver findings for corrective current control; not present as a shipped organizational relation.
- Decision owner: In-task coding agent may invoke `r2s check`/`deliver` validation; external benchmark evaluation is initiated by a research operator.
- Supporting / enforcement mechanisms: Independent SAM3/Pi3X perceptual data, rendered centroid/IoU comparisons, finite-run checks and benchmark second-view metrics.
- Closure path: Agent's own iterative check measurements feed the same S1 reconstruction; benchmark scores can be read offline but do not trigger an installed supervisory/audit correction path.
- Boundary reachability: `r2s deliver --validate-only` runs in the task and `benchmark/evaluate.py` after task completion, but neither is a separate operational inspector with a return to an accountable manager.
- Why this is / is not agent-owned: Objective camera/physics evidence improves S1 measurements but routine verification or an external paper benchmark is not by itself S3* ownership.
- Evidence: [MuJoCo/video comparison](https://github.com/Inception3D/Plumb/blob/02ea0be7f4a17cd04e8569dbc9749c3ebf18faf4/src/r2s/sim.py), [deliverable validator](https://github.com/Inception3D/Plumb/blob/02ea0be7f4a17cd04e8569dbc9749c3ebf18faf4/src/r2s/deliver.py), [second-view benchmark isolation](https://github.com/Inception3D/Plumb/blob/02ea0be7f4a17cd04e8569dbc9749c3ebf18faf4/benchmark/README.md).
- Basis: explicit + structural.
- Confidence: medium-high; the benchmark has genuinely independent measurements but is outside the on-task organizational audit loop.
- Caveats: A future integrated live evaluator with independent evidence and returned control could change the classification; it is not evidenced at this pinned revision.

### Absence scope

- Surfaces inspected: Agent loop, SAM3/Pi3X outputs, `r2s check`/`deliver` validators, fifty-video benchmark and unseen-camera evaluator.
- Plausible first-party paths checked: Objective perception as independent audit; model reading QA as S3*; final file format and physics validation; offline held-out view evaluation.
- Why no material first-party path remains: All in-task measurements are the agent's ordinary self-checking path; held-out metrics are post-hoc research scores without a first-party independent audit actor, decision and corrective return to current operations.

## S4 — Outside-and-then intelligence

- State: —
- Function: No standing prospective intelligence function mapping external change into later operating capability.
- Disturbance / variety regulated: The model faces uncertainty within an input video's past physical events, not environmental futures or organizational adaptation options.
- Decisive decision or feedback right: Select and integrate adaptation options responding to future external changes in users, physical domains, models or GPU tools; not established.
- Decision owner: No first-party S4 model or parent adaptation-governance route; operators independently update dependencies/configuration.
- Supporting / enforcement mechanisms: The task prompt allows offline scene fitting; tools accept geometry/segmentation parameters; benchmark examines generalization quality.
- Closure path: Observed frames → current scene parameter repair is S1 feedback, not an outside-and-then options loop returned to S3.
- Boundary reachability: No active watchdog or strategist consumes deployment trends/anticipated futures and changes subsequent task capacities.
- Why this is / is not agent-owned: Forecasting object motion inside a reconstruction is task-domain simulation, not adaptation of Plumb's organizational capacity to a changing external future.
- Evidence: [single-video scope and fixed simulation requirements](https://github.com/Inception3D/Plumb/blob/02ea0be7f4a17cd04e8569dbc9749c3ebf18faf4/src/prompts/task.md), [skill/tool interface](https://github.com/Inception3D/Plumb/blob/02ea0be7f4a17cd04e8569dbc9749c3ebf18faf4/src/SKILL.md), [benchmark scope](https://github.com/Inception3D/Plumb/blob/02ea0be7f4a17cd04e8569dbc9749c3ebf18faf4/benchmark/README.md).
- Basis: structural.
- Confidence: high for standard distribution.
- Caveats: Research on inverse physics may inform future product development, but there is no such live first-party adaptation loop in this harness.

### Absence scope

- Surfaces inspected: Task prompt, scene fitting, rollout/evaluation, benchmark research workflow, GPU configuration and launch recipe.
- Plausible first-party paths checked: Predicting physical trajectories; changing model parameters offline; testing fifty source videos; manual model/dependency upgrades.
- Why no material first-party path remains: All are current reconstruction operation, post-hoc research, or human maintenance; none builds prospective external options and returns a capability adjustment to a current whole-system S3 authority.

## S5 — Policy and identity

- State: —
- Function: No active first-party organizational identity/ultimate-policy decision and authoritative return path at a distinct S5 recursion.
- Disturbance / variety regulated: A fixed strict reconstruction brief constrains tools and physical realism; changes to enduring organizational purpose or contested ultimate priorities are not routed through any governing function.
- Decisive decision or feedback right: Resolve identity/policy-level tradeoffs and make returned binding decisions for future operations; not established.
- Decision owner: Repository maintainer/operator wrote `PROMPT.md` and may edit configurations outside this execution; the model may not negotiate physics constraints.
- Supporting / enforcement mechanisms: Rules forbidding fabricated hidden mechanisms, sandbox and path restrictions, restricted deliverables, and setup-time prompt copying.
- Closure path: Fixed task requirements are injected once into Codex/Claude; no identity-level issue → legitimate governance authority → decision → changed subsequent operating policy loop is implemented.
- Boundary reachability: The task contract says not to ask for relaxed constraints and supplies no identity escalation endpoint or project policy-decision channel.
- Why this is / is not agent-owned: Strong prompt boundaries are static operating instructions and safety constraints; they do not establish an ongoing S5 deliberation/control function simply because humans authored them.
- Evidence: [strict prompt and no relaxation clause](https://github.com/Inception3D/Plumb/blob/02ea0be7f4a17cd04e8569dbc9749c3ebf18faf4/src/prompts/task.md), [one-time task prompt copy](https://github.com/Inception3D/Plumb/blob/02ea0be7f4a17cd04e8569dbc9749c3ebf18faf4/src/harness/new_task.py), [README self-hosted CLI recipe](https://github.com/Inception3D/Plumb/blob/02ea0be7f4a17cd04e8569dbc9749c3ebf18faf4/README.md).
- Basis: structural + explicit.
- Confidence: high for this distribution boundary.
- Caveats: External university governance and a research team's choice of ethics/purpose are out of scope without a shipped operational decision/return relation.

### Absence scope

- Surfaces inspected: Agent identity/task prompt, per-task setup and deployment, fixed constraints, operator setup, batch workflow and benchmark.
- Plausible first-party paths checked: Prompt rules as a constitution; operator modifying the brief; task refusal to relax constraints; repository authors' collective research aims.
- Why no material first-party path remains: None provides a reachable identity dispute, named legitimate deciding authority and binding decision returned to future execution; rules alone constrain S1 rather than closing S5.

## Distributed OSS parent arrangement

Plumb is open-source research software that operators run as isolated local video reconstruction agents. Named authors and many benchmark tasks do not constitute a shared model-bearing OSS operating organization. Repository maintainer and human experimenter authority is not inferred as a parent S3/S4/S5 mode unless the function's required current-control, future-adaptation or identity closure is supported at this recursion. No such parent-owned mode is established in the inspected launch, task and benchmark paths.

## Recursion

At the inner recursion, a single coding-agent session revises one MuJoCo reconstruction and forms one S1. At the outer task-batch level, a human launches many independent sessions and a deterministic GPU queue shares model inference; neither constitutes an autonomous manager, coordinating peer society or S5 identity governor. A separate research benchmark can observe delivered results after the fact; it is not an in-operation complementary audit loop of this agent organization.

## Variety and escalation

Perception workers lower raw-video variety into masks, object members and 3D geometry. Simulation comparators provide numeric mismatch that can inform an S1 agent's next edit. GPU queueing, request deduplication and file validation attenuate computing and file-system risk without owning model-level organizational decisions. An unavailable GPU, missing checkpoint or failed output may block or require manual operator repair, but no automatic escalation to a distinct S2/S3/S3*/S4/S5 owner is provided. The researcher's post-hoc second-view evaluation remains external to the agent's task.

## Evidence gaps

- No provider-backed Codex/Claude task execution, gated SAM3 model download or GPU benchmark replay was conducted in this source review; operating-loop reachability follows pinned first-party setup/prompt/tool code.
- No direct first-party mechanism was found for model-bearing cross-task arbitration, whole-current allocation or independently corrective audit. These are scoped to the pinned distributed harness, not statements about possible third-party wrappers.
- The source includes high-quality objective evaluation that is materially distinct from the reconstructed scene; it cannot be promoted into S3* without showing a live independent audit owner and a control return path.
- The profile describes governance of a running reconstruction agent, not the quality or scientific novelty of the physics reconstruction paper.

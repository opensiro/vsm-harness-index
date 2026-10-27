---
harness_id: anima-sdk
project_name: anima_sdk
repository: https://github.com/Rai220/anima_sdk
review_ref: b6451ef44d2f97959fe7bfaab32c27907c9ddd77
reviewed_at: 2026-10-27
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# anima_sdk

## Review boundary

- System in focus: One copied anima_sdk long-task experiment using the current root run.sh/loop.sh/meta_loop.sh and a supported real agent CLI adapter. Root templates and task-local generation copies are distinguished. Historical/individual example experiments are adjacent systems, not inherited SDK governance.
- Purpose and identity: Sustain autonomous work over repeated short agent turns and clean generation restarts, with durable file artifacts.
- Relevant environment: Task directory, files and goals, selected external coding-agent CLI/model, shell process failures, operator inbox and generation-local context.
- Standard-distribution boundary: One copied anima_sdk long-task experiment using the current root run.sh/loop.sh/meta_loop.sh and a supported real agent CLI adapter. Root templates and task-local generation copies are distinguished. Historical/individual example experiments are adjacent systems, not inherited SDK governance.
- Credited operating / distribution surfaces: Current root scripts, harnesses/{free_code,claude,codex,deepagents,grok,custom}.sh plus lib.sh, task MAIN_GOAL/AGENTS template and generation copying semantics.
- Adjacent first-party surfaces excluded from ownership: examples/anima-legacy is explicitly old-runtime material; become-sentient, agent-self-evolution, benchmark-validation and other example agents/logs/essays have their own goals and generated mechanisms. Their self-audit, predictions, strategic claims and self-written tools do not automatically belong to the generic root SDK. GitHub presentation workflows are also adjacent.
- First-party operating / deployment modes considered: Supported local self-hosted runtime and operator-supervised configuration; no custom external composition is credited.
- Recursion level: One runtime/project deployment; nested task agents are not presumed recursively viable.
- Reviewed revision: b6451ef44d2f97959fe7bfaab32c27907c9ddd77
- Observation date: 2026-10-27
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

run.sh resolves task directory/config/prompt and locates a built-in harness adapter. The adapter invokes a configured external agent CLI with the task prompt and model/options. loop.sh serially re-invokes one run until a local STOP file. meta_loop.sh creates generation_N directories, reuses previous generation's AGENTS/run/loop/env copies, restores MAIN_GOAL from the task root, empties INBOX, copies harness templates and starts the next loop. Agent-owned file memory and tool descriptions survive only through explicitly retained task-root files or copied instructions. The shell runtime transports/restarts work; actual task/action discretion is owned by the selected CLI agent. AGENTS directs short steps, artifact checking, reading INBOX/LESSONS and documenting reusable tools. No shared multi-agent team or separate supervisory/audit/adaptation actor is installed by these scripts.

## Operational model

The configured CLI agent chooses how to advance the long task, produces files, records memory and can signal a stopped generation. A fresh generation continues the durable task under the root goal. Serial generations are lifecycle instances of this operational contribution, not concurrent viable systems or independent metasystem owners. Shell restart rules and user-written inbox clarifications remain distinct from organizational decision ownership.

## S1 — Operations

- State: A
- Function: Autonomous long-task artifact production across short turns
- Disturbance / variety regulated: Task uncertainty, context exhaustion and interrupted local reasoning
- Decisive decision or feedback right: Select task/tool actions, durable notes and when the present generation should stop
- Decision owner: Selected real coding-agent CLI invoked by a first-party adapter
- Supporting / enforcement mechanisms: run.sh adapter resolution, CLI/tool harness, file memory and repeat/generation shell loops
- Closure path: Changed task files and copied instructions inform subsequent turns/generations; CLI results return through process status
- Why this is / is not agent-owned: Selected real coding-agent CLI invoked by a first-party adapter; The CLI/model is an explicit configured dependency. Deterministic fixtures exercised transport only; no actual agent execution or long-task success is claimed.
- Evidence: [run.sh](https://github.com/Rai220/anima_sdk/blob/b6451ef44d2f97959fe7bfaab32c27907c9ddd77/run.sh); [harnesses/claude.sh](https://github.com/Rai220/anima_sdk/blob/b6451ef44d2f97959fe7bfaab32c27907c9ddd77/harnesses/claude.sh); [harnesses/codex.sh](https://github.com/Rai220/anima_sdk/blob/b6451ef44d2f97959fe7bfaab32c27907c9ddd77/harnesses/codex.sh); [loop.sh](https://github.com/Rai220/anima_sdk/blob/b6451ef44d2f97959fe7bfaab32c27907c9ddd77/loop.sh); [meta_loop.sh](https://github.com/Rai220/anima_sdk/blob/b6451ef44d2f97959fe7bfaab32c27907c9ddd77/meta_loop.sh); [AGENTS.md](https://github.com/Rai220/anima_sdk/blob/b6451ef44d2f97959fe7bfaab32c27907c9ddd77/AGENTS.md)
- Basis: structural
- Confidence: high
- Caveats: The CLI/model is an explicit configured dependency. Deterministic fixtures exercised transport only; no actual agent execution or long-task success is claimed.
- Boundary reachability: Current root scripts, harnesses/{free_code,claude,codex,deepagents,grok,custom}.sh plus lib.sh, task MAIN_GOAL/AGENTS template and generation copying semantics. The cited decision path is shipped in this mode and returns through run.sh adapter resolution, CLI/tool harness, file memory and repeat/generation shell loops.

## S2 — Coordination

- State: —
- Function: No inter-S1 interference coordination supplied
- Disturbance / variety regulated: Conflicts between distinct operational agents
- Decisive decision or feedback right: No conflict-sensitive coordination decision or feedback path established
- Decision owner: None established
- Supporting / enforcement mechanisms: Serial loop, generation directory separation, file notes and inbox
- Closure path: Only one generation loop runs at a time; STOP and copying replace a lifecycle instance without coordinating concurrent operational units
- Why this is / is not agent-owned: None established; Nested shells/generations are not distinct S1 units; external CLI subagent features are not borrowed into the SDK's organization.
- Evidence: [loop.sh](https://github.com/Rai220/anima_sdk/blob/b6451ef44d2f97959fe7bfaab32c27907c9ddd77/loop.sh); [meta_loop.sh](https://github.com/Rai220/anima_sdk/blob/b6451ef44d2f97959fe7bfaab32c27907c9ddd77/meta_loop.sh); [AGENTS.md](https://github.com/Rai220/anima_sdk/blob/b6451ef44d2f97959fe7bfaab32c27907c9ddd77/AGENTS.md)
- Basis: structural
- Confidence: medium
- Caveats: Nested shells/generations are not distinct S1 units; external CLI subagent features are not borrowed into the SDK's organization.

### Absence scope

- Surfaces inspected: [loop.sh](https://github.com/Rai220/anima_sdk/blob/b6451ef44d2f97959fe7bfaab32c27907c9ddd77/loop.sh); [meta_loop.sh](https://github.com/Rai220/anima_sdk/blob/b6451ef44d2f97959fe7bfaab32c27907c9ddd77/meta_loop.sh); [AGENTS.md](https://github.com/Rai220/anima_sdk/blob/b6451ef44d2f97959fe7bfaab32c27907c9ddd77/AGENTS.md); runtime entry, roles/tools, supported configuration and operating documentation within the declared boundary.
- Plausible first-party paths checked: Serial loop, generation directory separation, file notes and inbox; autonomous and operator-governed alternatives were checked for no inter-s1 interference coordination supplied.
- Why no material first-party path remains: Only one generation loop runs at a time; STOP and copying replace a lifecycle instance without coordinating concurrent operational units Nested shells/generations are not distinct S1 units; external CLI subagent features are not borrowed into the SDK's organization. This is a bounded shipped-distribution conclusion, not impossibility of an extension.

## S3 — Inside-and-now control

- State: —
- Function: No whole-system current-control function supplied
- Disturbance / variety regulated: Shared commitments/resources requiring whole-system intervention
- Decisive decision or feedback right: No shipped global current view plus discretionary current regulator established
- Decision owner: None established
- Supporting / enforcement mechanisms: STOP file, shell exit status, environment/model settings and generation restart
- Closure path: The shell applies a preselected restart rule; user inbox clarifies the current task, without an evidenced whole-system accountability/resource bargaining loop
- Why this is / is not agent-owned: None established; A script named meta_loop does not become S3; neither automatic restart nor changing a local task setting establishes an S3 constructor/parent loop.
- Evidence: [meta_loop.sh](https://github.com/Rai220/anima_sdk/blob/b6451ef44d2f97959fe7bfaab32c27907c9ddd77/meta_loop.sh); [loop.sh](https://github.com/Rai220/anima_sdk/blob/b6451ef44d2f97959fe7bfaab32c27907c9ddd77/loop.sh); [anima.env.example](https://github.com/Rai220/anima_sdk/blob/b6451ef44d2f97959fe7bfaab32c27907c9ddd77/anima.env.example); [AGENTS.md](https://github.com/Rai220/anima_sdk/blob/b6451ef44d2f97959fe7bfaab32c27907c9ddd77/AGENTS.md)
- Basis: structural
- Confidence: medium
- Caveats: A script named meta_loop does not become S3; neither automatic restart nor changing a local task setting establishes an S3 constructor/parent loop.

### Absence scope

- Surfaces inspected: [meta_loop.sh](https://github.com/Rai220/anima_sdk/blob/b6451ef44d2f97959fe7bfaab32c27907c9ddd77/meta_loop.sh); [loop.sh](https://github.com/Rai220/anima_sdk/blob/b6451ef44d2f97959fe7bfaab32c27907c9ddd77/loop.sh); [anima.env.example](https://github.com/Rai220/anima_sdk/blob/b6451ef44d2f97959fe7bfaab32c27907c9ddd77/anima.env.example); [AGENTS.md](https://github.com/Rai220/anima_sdk/blob/b6451ef44d2f97959fe7bfaab32c27907c9ddd77/AGENTS.md); runtime entry, roles/tools, supported configuration and operating documentation within the declared boundary.
- Plausible first-party paths checked: STOP file, shell exit status, environment/model settings and generation restart; autonomous and operator-governed alternatives were checked for no whole-system current-control function supplied.
- Why no material first-party path remains: The shell applies a preselected restart rule; user inbox clarifies the current task, without an evidenced whole-system accountability/resource bargaining loop A script named meta_loop does not become S3; neither automatic restart nor changing a local task setting establishes an S3 constructor/parent loop. This is a bounded shipped-distribution conclusion, not impossibility of an extension.

## S3* — Complementary audit

- State: —
- Function: No complementary independent audit of SDK operations supplied
- Disturbance / variety regulated: Truth of long-task agent completion or progress claims
- Decisive decision or feedback right: No separate audit owner/access/judgment returning corrective control established
- Decision owner: None established
- Supporting / enforcement mechanisms: Agent self-check instruction, output/log rendering, benchmark-validation example
- Closure path: The producer is told to check its own work; benchmark audit is a distinct experiment's S1 task, not a packaged independent audit of generic SDK operations
- Why this is / is not agent-owned: None established; Example self_audit tools and benchmark titles are not credited to this base distribution.
- Evidence: [AGENTS.md](https://github.com/Rai220/anima_sdk/blob/b6451ef44d2f97959fe7bfaab32c27907c9ddd77/AGENTS.md); [harnesses/lib.sh](https://github.com/Rai220/anima_sdk/blob/b6451ef44d2f97959fe7bfaab32c27907c9ddd77/harnesses/lib.sh); [README.md](https://github.com/Rai220/anima_sdk/blob/b6451ef44d2f97959fe7bfaab32c27907c9ddd77/README.md) examples boundaries
- Basis: structural
- Confidence: medium
- Caveats: Example self_audit tools and benchmark titles are not credited to this base distribution.

### Absence scope

- Surfaces inspected: [AGENTS.md](https://github.com/Rai220/anima_sdk/blob/b6451ef44d2f97959fe7bfaab32c27907c9ddd77/AGENTS.md); [harnesses/lib.sh](https://github.com/Rai220/anima_sdk/blob/b6451ef44d2f97959fe7bfaab32c27907c9ddd77/harnesses/lib.sh); [README.md](https://github.com/Rai220/anima_sdk/blob/b6451ef44d2f97959fe7bfaab32c27907c9ddd77/README.md) examples boundaries; runtime entry, roles/tools, supported configuration and operating documentation within the declared boundary.
- Plausible first-party paths checked: Agent self-check instruction, output/log rendering, benchmark-validation example; autonomous and operator-governed alternatives were checked for no complementary independent audit of sdk operations supplied.
- Why no material first-party path remains: The producer is told to check its own work; benchmark audit is a distinct experiment's S1 task, not a packaged independent audit of generic SDK operations Example self_audit tools and benchmark titles are not credited to this base distribution. This is a bounded shipped-distribution conclusion, not impossibility of an extension.

## S4 — Outside-and-then intelligence

- State: —
- Function: No externally prospective adaptation loop supplied
- Disturbance / variety regulated: Changing future operating environment or capability needs
- Decisive decision or feedback right: No first-party outside/future options-to-current-capability adaptation decision path established
- Decision owner: None established
- Supporting / enforcement mechanisms: LESSONS, self-created tools, preserved local AGENTS and fresh generations
- Closure path: Instructions retain discovered task/environment lessons and reusable tools; no required prospective environmental model/options conversation with current control is supplied
- Why this is / is not agent-owned: None established; Generic self-improvement and recovery can support task work without supplying S4. Prospective experiments in adjacent examples do not automatically upgrade the SDK.
- Evidence: [AGENTS.md](https://github.com/Rai220/anima_sdk/blob/b6451ef44d2f97959fe7bfaab32c27907c9ddd77/AGENTS.md) tools/lessons; [meta_loop.sh](https://github.com/Rai220/anima_sdk/blob/b6451ef44d2f97959fe7bfaab32c27907c9ddd77/meta_loop.sh); [MAIN_GOAL.md](https://github.com/Rai220/anima_sdk/blob/b6451ef44d2f97959fe7bfaab32c27907c9ddd77/MAIN_GOAL.md)
- Basis: structural
- Confidence: medium
- Caveats: Generic self-improvement and recovery can support task work without supplying S4. Prospective experiments in adjacent examples do not automatically upgrade the SDK.

### Absence scope

- Surfaces inspected: [AGENTS.md](https://github.com/Rai220/anima_sdk/blob/b6451ef44d2f97959fe7bfaab32c27907c9ddd77/AGENTS.md) tools/lessons; [meta_loop.sh](https://github.com/Rai220/anima_sdk/blob/b6451ef44d2f97959fe7bfaab32c27907c9ddd77/meta_loop.sh); [MAIN_GOAL.md](https://github.com/Rai220/anima_sdk/blob/b6451ef44d2f97959fe7bfaab32c27907c9ddd77/MAIN_GOAL.md); runtime entry, roles/tools, supported configuration and operating documentation within the declared boundary.
- Plausible first-party paths checked: LESSONS, self-created tools, preserved local AGENTS and fresh generations; autonomous and operator-governed alternatives were checked for no externally prospective adaptation loop supplied.
- Why no material first-party path remains: Instructions retain discovered task/environment lessons and reusable tools; no required prospective environmental model/options conversation with current control is supplied Generic self-improvement and recovery can support task work without supplying S4. Prospective experiments in adjacent examples do not automatically upgrade the SDK. This is a bounded shipped-distribution conclusion, not impossibility of an extension.

## S5 — Policy and identity

- State: —
- Function: No ultimate identity/policy adjudication loop supplied
- Disturbance / variety regulated: Ultimate goal/identity conflict at the task-system boundary
- Decisive decision or feedback right: No identity issue routed to legitimate authority and returned as adjudicated ultimate policy
- Decision owner: Task owner selects root goal/configuration; no qualifying S5 closure established
- Supporting / enforcement mechanisms: MAIN_GOAL template, root-goal copying, INBOX clarifications and base agent rules
- Closure path: Root goal is copied as a fixed task constraint; inbox receives unspecified clarifications, without a function-specific ultimate-policy issue/decision/return protocol
- Why this is / is not agent-owned: Task owner selects root goal/configuration; no qualifying S5 closure established; Selfhood/sentience narratives and local editable identity files in examples are not runtime S5. Generic human instruction remains insufficient.
- Evidence: [MAIN_GOAL.md](https://github.com/Rai220/anima_sdk/blob/b6451ef44d2f97959fe7bfaab32c27907c9ddd77/MAIN_GOAL.md); [meta_loop.sh](https://github.com/Rai220/anima_sdk/blob/b6451ef44d2f97959fe7bfaab32c27907c9ddd77/meta_loop.sh); [AGENTS.md](https://github.com/Rai220/anima_sdk/blob/b6451ef44d2f97959fe7bfaab32c27907c9ddd77/AGENTS.md); [README.md](https://github.com/Rai220/anima_sdk/blob/b6451ef44d2f97959fe7bfaab32c27907c9ddd77/README.md) quick start/inbox
- Basis: structural
- Confidence: medium
- Caveats: Selfhood/sentience narratives and local editable identity files in examples are not runtime S5. Generic human instruction remains insufficient.

### Absence scope

- Surfaces inspected: [MAIN_GOAL.md](https://github.com/Rai220/anima_sdk/blob/b6451ef44d2f97959fe7bfaab32c27907c9ddd77/MAIN_GOAL.md); [meta_loop.sh](https://github.com/Rai220/anima_sdk/blob/b6451ef44d2f97959fe7bfaab32c27907c9ddd77/meta_loop.sh); [AGENTS.md](https://github.com/Rai220/anima_sdk/blob/b6451ef44d2f97959fe7bfaab32c27907c9ddd77/AGENTS.md); [README.md](https://github.com/Rai220/anima_sdk/blob/b6451ef44d2f97959fe7bfaab32c27907c9ddd77/README.md) quick start/inbox; runtime entry, roles/tools, supported configuration and operating documentation within the declared boundary.
- Plausible first-party paths checked: MAIN_GOAL template, root-goal copying, INBOX clarifications and base agent rules; autonomous and operator-governed alternatives were checked for no ultimate identity/policy adjudication loop supplied.
- Why no material first-party path remains: Root goal is copied as a fixed task constraint; inbox receives unspecified clarifications, without a function-specific ultimate-policy issue/decision/return protocol Selfhood/sentience narratives and local editable identity files in examples are not runtime S5. Generic human instruction remains insufficient. This is a bounded shipped-distribution conclusion, not impossibility of an extension.

## Distributed OSS parent arrangement

Public contributors and maintainers are outside this deployed-runtime recursion. Local operator decisions do not imply project-wide or organization-wide parent governance.

## Self-hosted and non-human modes

Self-hosted operation is the assessed mode; parent notation is used only for the explicitly established function-specific loop, if any. No intentionally non-human governing organization is supplied.

## Recursion

Agents, tasks and sessions may be nested, but this does not establish independent viable systems with their own complete metasystem.

## Variety and escalation

Task directory, files and goals, selected external coding-agent CLI/model, shell process failures, operator inbox and generation-local context. The configured CLI agent chooses how to advance the long task, produces files, records memory and can signal a stopped generation. A fresh generation continues the durable task under the root goal. Serial generations are lifecycle instances of this operational contribution, not concurrent viable systems or independent metasystem owners. Shell restart rules and user-written inbox clarifications remain distinct from organizational decision ownership.

## Evidence gaps

Frozen-source review plus deterministic native shell fixtures, without a model. bash -n passed on all 10 root/adapter scripts. A throwaway custom-command fixture verified exactly one loop step followed by STOP. A second fixture verified generation_2 creation after generation_1 STOP, inherited modified AGENTS, root-restored MAIN_GOAL, empty/new inbox semantics and deliberate subprocess failure propagation (expected exit 23). Reproducible fixture and receipt are preserved in evidence/b2147/. No real CLI, provider, consciousness claim, long-run performance or independent semantic review is claimed.

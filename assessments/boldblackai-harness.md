---
harness_id: boldblackai-harness
project_name: boldblackai Harness
repository: https://github.com/boldblackai/harness
review_ref: 868c5ba0ec3ff08e9526d04b93b0743e35709fc7
reviewed_at: 2026-10-16
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-16
status: proposed
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# boldblackai Harness

## Review boundary

- System in focus: the first-party `@boldblackai/harness` containerized coding-agent launcher, CLI/adapters, container image recipes, entrypoints, mounts, persistence, environment/tool configuration, runtime selection and image verification at frozen Git commit `868c5ba0ec3ff08e9526d04b93b0743e35709fc7`. The agent implementations installed into images are **third-party executables**.
- Purpose and identity: give operators a repeatable, restricted environment in which separately implemented terminal coding agents can run with bounded project-directory access.
- Relevant environment: the user's project files, host Docker or Apple container runtime, local or remote model endpoint, downloaded container images, operator-selected prompts, provider credentials, and the selected external coding-agent binary.
- Standard-distribution boundary: first-party published Node/TypeScript CLI and images, including `src/harness.ts`, `Dockerfile`, `Dockerfile.opencode`, `Dockerfile.hermes`, and entrypoint scripts. A prebuilt image contains a *packaged dependency*, not a first-party authored model/tool reasoning loop.
- Credited operating / distribution surfaces: container/image selection and verification, CLI argument processing, project/skills/context mounts, adapter command construction, environment and credential forwarding, session persistence mounts, restrictive container settings and process exit propagation.
- Adjacent first-party surfaces excluded from ownership: GitHub Actions and security attestation CI, e2e tests, example configs, documentation, release automation and local development scripts. The imported `pi`, `opencode`, and `hermes` runtimes and their internal provider/tool/agent loops are adjacent third-party agent implementations, irrespective of whether an image bundles their binaries.
- First-party operating / deployment modes considered: default `pi` container, selectable `opencode` and `hermes` containers; one-shot and interactive commands; persistent or ephemeral container state; local model service vs credentialed cloud provider; Docker and Apple container invocation.
- Recursion level: one local first-party *launcher/container environment* for a selected external coding agent, not the combined multi-project governance of unrelated hosted agent instances and not the third-party agent implementation itself.
- Reviewed revision: `868c5ba0ec3ff08e9526d04b93b0743e35709fc7` (default `main` frozen on 2026-10-16).
- Observation date: 2026-10-16.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The [README](https://github.com/boldblackai/harness/blob/868c5ba0ec3ff08e9526d04b93b0743e35709fc7/README.md) describes a drop-in container wrapper around three named coding agents, not a first-party replacement for their reasoning/tool loops. [`package.json`](https://github.com/boldblackai/harness/blob/868c5ba0ec3ff08e9526d04b93b0743e35709fc7/package.json) distributes a TypeScript/Node CLI, depending at runtime on `minimist` for argument parsing rather than shipping a model inference/tool-execution framework.

In [`src/harness.ts`](https://github.com/boldblackai/harness/blob/868c5ba0ec3ff08e9526d04b93b0743e35709fc7/src/harness.ts), `PiAdapter.buildCommand` constructs `pi -p <prompt>` or `pi`; `OpenCodeAdapter.buildCommand` constructs `opencode run <prompt>` or `opencode`; and `HermesAdapter.buildCommand` constructs `hermes chat [-m model] [-q prompt]`. The first-party `run(prompt)` selects host container runtime and image, optionally verifies the image, builds mounts/permissions/provider flags, calls `runtime.runArgs({...,containerCmd})`, then delegates the process to `spawn(runtime.binary(), args, {stdio: "inherit"})`. On child exit it propagates the exit status. It does **not** parse the child model's tool calls, execute the child's selected tools, feed observations back to the child model, or autonomously choose substantive next coding actions.

The [base `Dockerfile`](https://github.com/boldblackai/harness/blob/868c5ba0ec3ff08e9526d04b93b0743e35709fc7/Dockerfile) globally installs `@earendil-works/pi-coding-agent`; [`Dockerfile.opencode`](https://github.com/boldblackai/harness/blob/868c5ba0ec3ff08e9526d04b93b0743e35709fc7/Dockerfile.opencode) installs `opencode-ai`, and [`Dockerfile.hermes`](https://github.com/boldblackai/harness/blob/868c5ba0ec3ff08e9526d04b93b0743e35709fc7/Dockerfile.hermes) configures Hermes dependencies. The [`entrypoint.sh`](https://github.com/boldblackai/harness/blob/868c5ba0ec3ff08e9526d04b93b0743e35709fc7/entrypoint.sh) initializes local defaults before `exec "$@"`, transferring control to the external agent command. Separate entrypoints perform analogous setup for the selected agent. The first-party code actively improves isolation, reproducibility and provenance, but these mechanisms support someone else's operational agent.

## Operational model

The operator selects a prompt, coding-agent adapter, project mount, model/provider and permissions. The CLI verifies/configures a suitable container image and invokes the host container runtime with a command to run the selected third-party agent. **Inside the launched agent dependency**, that agent may independently call a model, plan, read/write files, run tools, interpret observations and continue. The first-party wrapper cannot be credited with decisions taken by `pi`, `opencode` or `hermes` simply because those executables are installed in its images. Once the child starts, the wrapper's observed return is its exit status, not a feedback loop governing the child's next cognitive/tool decision.

The counterfactual owner test is decisive: remove the three third-party agent executables while leaving `src/harness.ts`, image verification, runtime choice, mounts, policy and persistence in place. The first-party harness can still prepare a sandbox and launch a process, but cannot perform autonomous coding-agent task interpretation and model-chosen action/observation continuation. Conversely, one of those agent executables running without this wrapper retains its own model/tool loop. The first-party S1 operational owner therefore belongs outside the assessed repository boundary.

## Exclusion conclusion

**Proposed terminal disposition: `excluded-no-agentic-vsm`** at this frozen first-party launcher boundary. This is a scope/ownership determination, not an assessment of the quality, safety, popularity or technical value of boldblackai Harness, and not a declaration that the assembled product cannot run an autonomous agent. It *can* run an externally implemented autonomous agent, but the first-party source assessed here does not own that operational S1.

The provisional all-`—` vector expresses no credited first-party agentic function at this assessed boundary. It is not a grade assigned to the embedded third-party pi/OpenCode/Hermes agents, which require distinct repository-relative assessments.

## S1 — Operations

- State: —
- Function: the substantive coding-task operation is performed by an imported external coding-agent executable, not by the first-party launcher.
- Disturbance / variety regulated: coding-task uncertainty and changed repository state are interpreted by the selected child agent; the first-party launcher regulates image/container environment and entry configuration.
- Decisive decision or feedback right: choose the next task-relevant model/tool operation after observing a tool result.
- Decision owner: `pi`, `opencode` or `hermes` child runtime (third-party), not `@boldblackai/harness`.
- Supporting / enforcement mechanisms: CLI adapter dispatch, container/image checks, mount and environment flags, process spawning, exit reporting and persistent agent-directory volumes.
- Closure path: wrapper: configure → spawn child → exit status; model→tool→result→next model action closes within the excluded child agent.
- Why this is / is not agent-owned: the first-party CLI does not interpret model responses or own a task-level adaptive action policy. Packaging the dependencies is a deployment mechanism rather than authorship of that loop.
- Evidence: [`src/harness.ts`](https://github.com/boldblackai/harness/blob/868c5ba0ec3ff08e9526d04b93b0743e35709fc7/src/harness.ts), [`package.json`](https://github.com/boldblackai/harness/blob/868c5ba0ec3ff08e9526d04b93b0743e35709fc7/package.json), [`Dockerfile`](https://github.com/boldblackai/harness/blob/868c5ba0ec3ff08e9526d04b93b0743e35709fc7/Dockerfile), [`entrypoint.sh`](https://github.com/boldblackai/harness/blob/868c5ba0ec3ff08e9526d04b93b0743e35709fc7/entrypoint.sh).
- Basis: explicit source and counterfactual runtime-boundary test.
- Confidence: high for source-level authorship boundary; no live container run claimed.
- Caveats: images do package powerful external agents; the conclusion is repository-relative, not a claim about the runnable integrated deployment lacking any agentic activity.

### Absence scope

- Surfaces inspected: README/packaging, `src/harness.ts` adapters and `run`, container runtime abstraction, images/entrypoints and first-party tests.
- Plausible first-party paths checked: CLI prompt parsing, adapter selection, image composition, container execution and session persistence.
- Why no material first-party path remains: every documented autonomous coding loop is provided by a third-party agent binary; the wrapper forwards arguments and stream/exit status without implementing that loop.

## S2 — Coordination

- State: —
- Function: no in-boundary coordination among distinct first-party agentic S1 units, because no such first-party operational population is established.
- Disturbance / variety regulated: shared workspace contention or concurrent independent agent tasks could arise in a larger system; the first-party image/process wrappers instead configure one selected child per invocation.
- Decisive decision or feedback right: detect and attenuate specific interference between first-party S1 units and return a coordination choice into those units.
- Decision owner: no first-party S2-specific owner established; any cooperation/conflict of child agents belongs to their separate runtimes/operators.
- Supporting / enforcement mechanisms: mount configuration, per-agent persistence directories, selected adapter and host process execution.
- Closure path: no evidenced inter-first-party-agent corrective regulation; any model-driven coordination would close outside.
- Why this is / is not agent-owned: separate adapter options and per-agent state directories are not feedback-mediated inter-S1 disturbance attenuation.
- Evidence: [`src/harness.ts`](https://github.com/boldblackai/harness/blob/868c5ba0ec3ff08e9526d04b93b0743e35709fc7/src/harness.ts), [README](https://github.com/boldblackai/harness/blob/868c5ba0ec3ff08e9526d04b93b0743e35709fc7/README.md).
- Basis: structural bounded absence.
- Confidence: high.
- Caveats: external agent fleets are outside the reviewed distribution boundary.

### Absence scope

- Surfaces inspected: adapters, runtime command assembly, persistent mounts, CLI behavior and container mode documentation.
- Plausible first-party paths checked: multiple supported agent types, shared project volume, persistence and container policies.
- Why no material first-party path remains: facilities select and isolate a child runtime; they do not observe inter-agent disturbances and decide returned coordination for first-party S1s.

## S3 — Inside-and-now control

- State: —
- Function: no whole-current first-party organization/resource/commitment control established.
- Disturbance / variety regulated: container startup, image authenticity and per-process resource/sandbox constraints.
- Decisive decision or feedback right: view current organization-wide operations and decide accountable interventions, resources, priorities or commitments that feed back into S1.
- Decision owner: operator chooses options; deterministic launcher enforces startup constraints. No first-party S3 holder.
- Supporting / enforcement mechanisms: runtime/image selection, cosign verification, container capabilities, environment/mount restrictions, exit propagation.
- Closure path: admission of one container run, then external execution; no first-party current-portfolio decision returning adjusted agent operations.
- Why this is / is not agent-owned: an image-policy gate is a fixed launch-time control, not a whole-current decision authority.
- Evidence: [`src/harness.ts`](https://github.com/boldblackai/harness/blob/868c5ba0ec3ff08e9526d04b93b0743e35709fc7/src/harness.ts), [`docs/security.md`](https://github.com/boldblackai/harness/blob/868c5ba0ec3ff08e9526d04b93b0743e35709fc7/docs/security.md).
- Basis: structural bounded absence.
- Confidence: high.
- Caveats: external deployment controllers may manage many runs, but their S3 would not belong to this launcher.

### Absence scope

- Surfaces inspected: CLI run/runtime selection, container image verification, runtime options, docs/security and tests.
- Plausible first-party paths checked: provider/model choice, run-time safety checks, resource restrictions, and operator decisions.
- Why no material first-party path remains: there is no current whole-system operational view linked to an authoritative discretionary intervention and return to multiple first-party S1s.

## S3* — Complementary audit

- State: —
- Function: image signatures, supply-chain provenance and CI do not establish a complementary operational audit of first-party S1 output.
- Disturbance / variety regulated: malicious image/supply-chain modification and runtime isolation risk, not an independently reviewed organizational operating result.
- Decisive decision or feedback right: independently inspect agent-produced operational artifacts, make a corrective judgment and return it to S1/S3 authority.
- Decision owner: no shipped complementary organizational audit actor established; CI and cosign are verification/maintenance facilities.
- Supporting / enforcement mechanisms: cosign signature checks, image attestations, immutable tags/digests, test/CI and container security mechanisms.
- Closure path: failed image verification can stop a run; no separate first-party auditor of agent work returns corrective decision to first-party S1/S3.
- Why this is / is not agent-owned: validating a container image's origin is not a complementary audit of the coding operation and its corrective governance.
- Evidence: [`src/harness.ts`](https://github.com/boldblackai/harness/blob/868c5ba0ec3ff08e9526d04b93b0743e35709fc7/src/harness.ts), [`Dockerfile`](https://github.com/boldblackai/harness/blob/868c5ba0ec3ff08e9526d04b93b0743e35709fc7/Dockerfile), [`docs/security.md`](https://github.com/boldblackai/harness/blob/868c5ba0ec3ff08e9526d04b93b0743e35709fc7/docs/security.md).
- Basis: structural bounded absence.
- Confidence: high.
- Caveats: supply-chain verification has independent security utility but is not itself VSM S3* at the declared boundary.

### Absence scope

- Surfaces inspected: image verification, reproducibility measures, CI files, tests and supported runtime invocation.
- Plausible first-party paths checked: security verification as audit; agent-output review; independent operational artifact inspection and returned remediation.
- Why no material first-party path remains: no first-party operational audit owner or correcting return path is present; supply-chain gates act before external-agent work.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party environment-sensing, prospective adaptive-organization loop.
- Disturbance / variety regulated: changing tool and model ecosystems, image dependencies and future security needs.
- Decisive decision or feedback right: interpret external/future threats/opportunities, select capability adaptation and return it to current operation.
- Decision owner: developers update images and operators choose models, agent types and settings; no first-party S4 actor or closed parent-governed loop.
- Supporting / enforcement mechanisms: configurable agent adapter, model arguments, pinned dependencies and manually updated container builds.
- Closure path: published image update or new selected model may alter external child execution after developer/operator intervention; no supported first-party prospective adaptation judgment to returned capability established.
- Why this is / is not agent-owned: options and human software maintenance alone do not demonstrate S4.
- Evidence: [README](https://github.com/boldblackai/harness/blob/868c5ba0ec3ff08e9526d04b93b0743e35709fc7/README.md), [`Dockerfile`](https://github.com/boldblackai/harness/blob/868c5ba0ec3ff08e9526d04b93b0743e35709fc7/Dockerfile), [`src/harness.ts`](https://github.com/boldblackai/harness/blob/868c5ba0ec3ff08e9526d04b93b0743e35709fc7/src/harness.ts).
- Basis: structural bounded absence.
- Confidence: high.
- Caveats: operator or downstream agent can be placed in a separate adaptation workflow not implemented here.

### Absence scope

- Surfaces inspected: model/provider/agent selection, pinned images and dependencies, configuration docs, CI and runtime entrypoint.
- Plausible first-party paths checked: runtime model selection as adaptation; image-update schedule; developer-maintained compatibility; external threat scanning.
- Why no material first-party path remains: available options are selected by operator or maintained out of band and do not constitute prospective sensing → autonomous/parent-decision → applied capability change.

## S5 — Policy and identity

- State: —
- Function: no first-party legitimate organizational ultimate-policy/identity adjudication at the declared local-launcher boundary.
- Disturbance / variety regulated: filesystem and network access, permitted commands, image trust and externally supplied agent context.
- Decisive decision or feedback right: decide disputed ultimate purpose/identity/authority and return a binding policy resolution to agent operation.
- Decision owner: operator sets CLI flags, mount and provider choices; first-party CLI enforces those constraints mechanically. No S5 closure path.
- Supporting / enforcement mechanisms: context-file mounts, container capabilities, process user isolation, image verification and user-chosen runtime parameters.
- Closure path: supplied launch settings → container enforcement; no identity dispute → legitimate ultimate-policy parent → authoritative decision → returned changed operation.
- Why this is / is not agent-owned: no first-party governance decision is formed by selecting Docker security arguments or forwarding AGENTS.md to an external runtime.
- Evidence: [`src/harness.ts`](https://github.com/boldblackai/harness/blob/868c5ba0ec3ff08e9526d04b93b0743e35709fc7/src/harness.ts), [`docs/security.md`](https://github.com/boldblackai/harness/blob/868c5ba0ec3ff08e9526d04b93b0743e35709fc7/docs/security.md).
- Basis: structural bounded absence.
- Confidence: high.
- Caveats: operators may be legitimate parents of their own *larger organizations*, but no function-specific first-party S5 return is established by this launcher.

### Absence scope

- Surfaces inspected: configuration and context mounts, operator flags, runtime security options, image verification, first-party CLI and documentation.
- Plausible first-party paths checked: AGENTS.md/CLAUDE.md transfer, user-configured security policy, provider access, runtime errors and operator permissions.
- Why no material first-party path remains: the first-party system enforces given launch constraints but has no demonstrated ultimate-policy issue admission, legitimate adjudication or returned organizational policy change.

## Recursion

The local wrapper selects **one external coding agent per execution**. That child runtime may be agentic in its own right at a different assessment boundary. Selecting an agent type or storing its state does not establish first-party operational S1, inter-S1 S2, current-control S3, independent operational S3*, prospective S4 or ultimate-policy S5 in the wrapper's organization.

## Variety and escalation

First-party regulation absorbs deployment/supply-chain/security and local configuration variety. Container or image failure stops or rejects launch; child process exit is returned to the operator. The external agent absorbs engineering task and model/tool interaction variety. These error/launch surfaces are not automatically algedonic VSM channels or metasystem decisions.

## Evidence gaps

- No live Docker/Apple-container execution and no live provider-backed run was conducted in this source-only assessment. The external agent dependencies' exact tool behavior was not assessed.
- No claim is made that a third-party agent executing within the image lacks S1; its repository owns its own system-relative assessment.
- If future first-party source adds its own substantive model response→tool call→observation continuation or genuinely internal operating agent actor, a **new-ref reassessment** could revisit this exclusion rather than retroactively altering this frozen source.

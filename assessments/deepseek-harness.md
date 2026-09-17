---
harness_id: deepseek-harness
project_name: DeepSeek Harness
repository: https://github.com/deepseek-ai/deepseek-harness
review_ref: ddefc45fbc7f8e46dd73185e68295696d1297887
reviewed_at: 2026-09-18
generated_profile_version: 0.2.2
generated_assessment_procedure_version: 0.3.1
profile_version: 0.2.2
assessment_procedure_version: 0.3.1
assessment_changed_at: 2026-09-18
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# DeepSeek Harness

## Review boundary

- System in focus: the first-party DeepSeek Harness runtime, Agent loop, Session/subagent/workflow surfaces, and published first-party deployment/profile layers at pinned revision `ddefc45fbc7f8e46dd73185e68295696d1297887`.
- Purpose: run tool-using agents in persistent Sessions and let a deployment compose tools, subagents, workflows, permissions, goals, and optional multi-agent Team control.
- Standard-distribution boundary: first-party packages and published profile bundles shipped by `deepseek-ai/deepseek-harness`, including published opt-in experimental Agent Teams/Agent Teams Web/Auto Review layers. External model providers and the separately vendored/framework Cordis semantics are supporting environment, not credited as DeepSeek Harness organizational actors.
- First-party modes considered:
  1. ordinary base/headless/Web Agent runtime;
  2. published opt-in experimental Agent Teams Host profile;
  3. published opt-in Agent Teams Web profile exposing parent task-board control;
  4. experimental Auto Review and Ralph/workflow modes as negative-boundary checks.
- Recursion level: one Harness-controlled agent organization. Team Lead and durable teammates are the relevant multiple S1 units in the Team mode; generic child spawning by itself is not VSM recursion.
- Generated/current Profile / Methodology: `0.2.2` / `0.3.1`.

## Primary evidence

- [`packages/core/agent-loop/README.md`](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45fbc7f8e46dd73185e68295696d1297887/packages/core/agent-loop/README.md) — concrete autonomous Agent driver: model request, tool execution, durable Session facts, bounded parallel tool calls, continuation and cancellation.
- [`packages/experimental/agent-team/README.md`](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45fbc7f8e46dd73185e68295696d1297887/packages/experimental/agent-team/README.md) — durable roster, peer mailbox, dependency-aware shared task board, ownership/reassignment, CAS updates, overlap warnings and Lead authority.
- [`packages/experimental/tool-agent-team/README.md`](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45fbc7f8e46dd73185e68295696d1297887/packages/experimental/tool-agent-team/README.md) — model-facing Team tools and fixed coordination policy; model Lead creates/interrupts teammates and Team members coordinate through tasks/messages.
- [`packages/experimental/tool-agent-team/src/index.ts`](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45fbc7f8e46dd73185e68295696d1297887/packages/experimental/tool-agent-team/src/index.ts) — exact Team policy instructing disjoint write scopes, dependency ordering, stale-version recovery, messaging/wait closure and Lead final integration.
- [Agent Teams decision](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45fbc7f8e46dd73185e68295696d1297887/.agents/notes/implemented/feature/2026-08-05-agent-teams.md) — explicit disturbance: same-process Agents share one checkout; task ownership alone is not a file lock; durable task/mailbox semantics plus Lead coordination reduce conflicts while preserving the remaining boundary.
- [`packages/experimental/agent-team-profile/README.md`](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45fbc7f8e46dd73185e68295696d1297887/packages/experimental/agent-team-profile/README.md) — published opt-in first-party profile layer that activates Team domain/tools over `dsh-base`.
- [`packages/experimental/client-ui-agent-team/README.md`](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45fbc7f8e46dd73185e68295696d1297887/packages/experimental/client-ui-agent-team/README.md) — parent Web view of roster/task state and direct user create/edit/assign/unassign/complete/reopen/delete task control.
- [`packages/experimental/agent-team-web-profile/README.md`](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45fbc7f8e46dd73185e68295696d1297887/packages/experimental/agent-team-web-profile/README.md) — published first-party Web profile composing Host Team state with the parent task-board UI.
- [`packages/experimental/auto-review/README.md`](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45fbc7f8e46dd73185e68295696d1297887/packages/experimental/auto-review/README.md) — pre-execution per-tool risk/authorization review; useful negative boundary for S3*.
- [`packages/workflow/tool-ralph/README.md`](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45fbc7f8e46dd73185e68295696d1297887/packages/workflow/tool-ralph/README.md) — fresh-agent iterative loop whose completion/blocker result is explicitly worker self-report, not independent evaluation.

## Repository architecture

The ordinary Harness owns a persistent Session-centered Agent loop. A model receives derived history and visible tool schemas, chooses tool calls, consumes durable results, and repeats. Subagent and workflow packages add child-agent and scripted fan-out primitives, but the base composition does not by those mechanisms alone establish S2 or S3.

The published experimental Agent Teams profile is materially different. It overlays a durable Team domain on the base runtime: one root Agent is the Team Lead, named autonomous teammates are continuable child Agents, members share a persistent mailbox and versioned task board, task dependencies gate readiness, and the Lead owns teammate creation/interruption and cross-member assignment. The corresponding Web profile adds a first-party parent control surface over the same authoritative Team task state.

## S1 — Operations

- State: `A`.
- Function: autonomously pursue repository/general tasks through repeated model decisions, tool calls, Session state and subsequent turns.
- Decisive right / owner: the model-driven Agent chooses operational actions from the supplied tool surface.
- Closure: accepted tool/results and Session events enter later model requests and alter subsequent action.
- Supporting mechanisms: Agent loop, Session persistence, tool registry, provider adapters, cancellation and optional subagents.
- Confidence: high.

## S2 — Coordination

- State: `A`.
- Positive mode: published opt-in Agent Teams.
- Distinct S1 units: Team Lead plus named teammate Agents working in one shared checkout.
- Concrete disturbance: concurrent members can contend over shared files and stale task/assignment state. The first-party design explicitly notes that Bash, generators and external writers can bypass file stale-version fences, so coordination rather than false locking is required.
- Coordination relation:
  - shared tasks have owners, dependency DAGs, readiness and advisory write scopes;
  - blocked tasks cannot be claimed until dependencies complete;
  - stale task revisions fail instead of silently overwriting newer assignment state;
  - overlapping in-progress write scopes are surfaced as warnings;
  - peer messages steer running members or resume idle/inactive teammates;
  - the fixed Team policy directs members to partition writes, order dependent work and rebase after stale-file feedback.
- Feedback closure: board/list/get results, overlap warnings, rejected stale mutations and peer messages return into Team-member model contexts; members subsequently claim/release/complete work, message peers, or alter task structure.
- Decisive right / owner: Agents choose task decomposition, dependencies, write scopes, claims and peer coordination; deterministic CAS/DAG/mailbox machinery enforces those decisions. The organizational coordination right is therefore agent-owned, not merely runtime-owned.
- Caveat: write scopes are advisory rather than filesystem locks, so S2 attenuates shared-checkout interference without eliminating every external-write collision.
- Confidence: high.

## S3 — Inside-and-now control

- State: `A(P)`.
- Autonomous Team mode:
  - the Lead can inspect roster/task state;
  - only the Lead creates and interrupts teammates;
  - the Lead may assign/reassign tasks across members;
  - the Team policy requires the Lead to wait for required work, inspect the final diff and run tests before the final answer.
- Whole-system current disturbance: active/inactive/stuck workers, assignment gaps, dependency readiness, overlapping intended writes and incomplete Team commitments.
- Agent-owned closure: the Lead observes current Team state and can spawn, message, assign/reassign, interrupt, wait and integrate; those interventions change subsequent teammate work and Team commitments. This establishes `A`.
- Parent mode: the published Agent Teams Web profile lets a user inspect the authoritative roster/task board and create, edit, assign/unassign, complete, reopen and delete Team tasks. Mutations use revision-checked Remote methods and the UI reloads the complete Team view after success or conflict. Agents subsequently read the same authoritative task board, so parent decisions return into current operation. This separately establishes first-party parent-governed S3 and yields `A(P)`.
- Supporting/enforcement mechanisms: Team service, task CAS/DAG validation, Remote API, browser Client and Session persistence.
- Caveat: the Web parent panel cannot itself spawn or interrupt teammates; its parent S3 authority is task/commitment regulation rather than the full Lead lifecycle surface.
- Confidence: high.

## S3* — Complementary audit

- State: `—`.
- A teammate can be asked to review a diff, but generic role delegation does not by itself supply a distinct independent audit function.
- Experimental Auto Review performs a separate model call before each pending tool body and gates execution according to risk/authorization policy. This is pre-action permission control, not complementary independent access to operational reality after or outside the normal control channel.
- Ralph explicitly states that completion/blocker outcomes are worker reports and are not independently verified; its documentation defers an independent evaluator.
- No first-party mode was established that supplies a sufficiently independent audit actor with its own operational evidence and audit-to-correction closure.
- Confidence: high.

## S4 — Outside-and-then intelligence

- State: `—`.
- Web search, goals, workflows, Ralph rounds, Session history and plugin composition can change a current task trajectory. None establishes a distinct first-party function that monitors the external future environment, develops organizational adaptation options and closes them into changed future capability.
- Plugin installation/update is operator/deployment configuration rather than autonomous S4.
- Confidence: high.

## S5 — Policy and identity

- State: `—`.
- Permission presets, Auto Review risk rules, system/persona prompts, plugin/profile selection and explicit-human Team activation are constraints and deployment choices. They do not establish a runtime identity/ultimate-policy function that resolves organizational policy tensions at the declared recursion.
- Generic human approval or profile choice is not promoted to parent S5.
- Confidence: high.

## Recursion, variety, and escalation

The Harness supports nested child agents, workflows and fresh-agent loops, but spawning alone is not VSM recursion. Agent Teams is treated here as one organization containing multiple operational Agent S1s because its roster, shared commitments and Lead regulation establish that functional boundary.

Operational variety expands through tools, subagents, workflows and plugins. Team task DAGs, ownership, CAS, write-scope diagnostics and peer messages attenuate coordination variety. Team Web task mutations provide a separately evidenced parent intervention path. Tool permission failures, Team conflicts/stale revisions, blocked dependencies and teammate status become explicit feedback rather than silent state mutation.

## Admission conclusion

Canonical vector: `A A A(P) — — —`.

The positive metasystem states come specifically from the published opt-in Agent Teams modes, not from generic plugin, subagent or workflow vocabulary. Team members own S2 coordination through persistent shared commitments and feedback, the model Lead owns autonomous S3 current regulation, and the first-party Web task-board surface establishes a separate parent-governed S3 mode. No independent S3*, prospective S4 or ultimate-policy S5 closure is established at the pinned boundary.

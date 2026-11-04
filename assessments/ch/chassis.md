---
harness_id: chassis
project_name: Chassis
repository: https://github.com/theo-kirby/chassis
review_ref: b9350031580d58328849184974e1368d082f4892
reviewed_at: 2026-11-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A(P)
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Chassis

## Review boundary

- System in focus: the published Chassis Docker agent-fleet framework with Pi by default, its seeded interactive `driver` agent, user-defined scheduled/triggered agents, privileged tool dispatcher, status/dashboard and optional supervised reporting-job installation.
- Purpose and identity: run a persistent local fleet of user-configured task agents with validated tools, cron/completion triggers, protected secrets and explicit human/driver control over the fleet's present operation.
- Relevant environment: container agent directory, task instructions and model settings, scheduled occurrences, upstream completion/verdict output, read/write tools, dispatcher audit, run logs, host Docker/scheduling and operator permissions.
- Standard-distribution boundary: first-party Docker image, `/home/agent` agent/task definitions, Pi runner/extension, `run-agent` trigger implementation, seeded `driver` persona, `chassis` CLI, dispatcher and opt-in supervisor. External Pi/Claude/Codex runtime/model inference supplies decision execution in the specified installed adapter mode; no unrelated provider agent organization is credited.
- Credited operating / distribution surfaces: [README](https://github.com/theo-kirby/chassis/blob/b9350031580d58328849184974e1368d082f4892/README.md), [seeded driver](https://github.com/theo-kirby/chassis/blob/b9350031580d58328849184974e1368d082f4892/harness/agent-template/driver/SYSTEM.md), [runtime and trigger implementation](https://github.com/theo-kirby/chassis/blob/b9350031580d58328849184974e1368d082f4892/harness/run-agent), [CLI/host controls](https://github.com/theo-kirby/chassis/blob/b9350031580d58328849184974e1368d082f4892/chassis), and [supervised jobs](https://github.com/theo-kirby/chassis/blob/b9350031580d58328849184974e1368d082f4892/docs/supervised-jobs.md).
- Adjacent first-party surfaces excluded from ownership: documentation/example-only `writer ↔ reviewer` configuration without an installed reviewer agent, this repository's internal AGENTS.md/governance/CI, notebook-private enabled jobs/OAuth credentials and local trial conclusions not distributed with the repository, host platform systemd administration, and independent runtime/provider internal governance.
- First-party operating / deployment modes considered: default Pi scheduled/triggered fleet with interactive driver, alternative published harness branches as documented, host operator CLI/dashboard, and optional `jobs/` supervisor with read-only reporting policy and Codex adapter. The three public supervised examples ship *paused*; notebook-specific active jobs do not count as automatic standard deployments.
- Recursion level: one local Chassis container/fleet with many task agents and a legitimate host operator, not the author's private notebook or public OSS maintainer organization.
- Reviewed revision: `theo-kirby/chassis@b9350031580d58328849184974e1368d082f4892` (MIT).
- Observation date: 2026-11-04.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

An installed Chassis container has an unprivileged `agent` home containing `SYSTEM.md`, `agent.json` and per-task instruction/cron/trigger files. `run-agent` starts the configured coding-agent runtime in an interactive or non-interactive task mode, collects per-run verdicts and launches other tasks when their exact trigger conditions match. Root owns tool implementations and secrets; the dispatcher validates schemas and supplies bounded secrets to invoked tools, recording redacted audit. A seeded `driver` agent sees all local agent/task definitions and run logs, and is specifically instructed to inspect past operations and edit agent definitions when needed. On the host, the legitimate operator starts and stops runs, examines dashboards/logs, installs agent directories, edits protected tools and reloads cron. Optional supervised jobs use per-job disposable containers and a fixed tool allowlist/SQLite history; their schema validator is deterministic and substantive validation remains human. [README](https://github.com/theo-kirby/chassis/blob/b9350031580d58328849184974e1368d082f4892/README.md), [driver persona](https://github.com/theo-kirby/chassis/blob/b9350031580d58328849184974e1368d082f4892/harness/agent-template/driver/SYSTEM.md), [supervisor docs](https://github.com/theo-kirby/chassis/blob/b9350031580d58328849184974e1368d082f4892/docs/supervised-jobs.md).

## Operational model

A configured model agent carries out its task using the registered tools and system/task instructions. Scheduled runs and completion-triggered runs may continue across many episodes without a live human. The `driver` is deliberately a distinct whole-fleet interactive control mode: the user starts it, then the model can inspect collective run/audit records and author/delete/revise other agent prompts, models, and task definitions, affecting later actual runs. A legitimate human can also directly choose run/stop, agent installation, tools/permissions and cron refresh. These closures are distinct from deterministic runtime dispatch, scheduled triggers, and per-run JSON verdict comparisons. The optional supervisor retains a constrained read-only profile, but no independent semantic reviewer is packaged with it.

## S1 — Operations

- State: A
- Function: execute model-led tasks such as research, coding, reporting and tool-based work in scheduled, triggered or interactive runs.
- Disturbance / variety regulated: variable task inputs, changing external research observations, file/tool outputs and success/failure results.
- Decisive decision or feedback right: each configured model agent chooses task-specific reasoning, tool calls and its returned report/verdict while running its own SYSTEM/INSTRUCTIONS context.
- Decision owner: Pi or supported configured coding-agent/LLM runtime operating as the Chassis task agent; Chassis supplies accessible prompts and validated tools rather than precomputing the task response.
- Supporting / enforcement mechanisms: `run-agent`, Pi extension, cron launcher, trigger router, tool dispatcher, audited tool results and isolated optional supervised jobs.
- Closure path: task instruction/cron or earlier trigger → model agent run → inspected data/tools and outcome judgment → returned result/verdict and optional follow-on triggered tasks.
- Boundary reachability: first-party Docker image seeds an agent runtime and driver; `chassis run`, cron and triggers are documented first-party execution modes, while the optional supervised job path is separately documented and implemented.
- Why this is / is not agent-owned: a scheduler and schema-checked dispatcher can run or reject tools, but cannot choose the substantive task analysis or output, which remains with the configured LLM agent.
- Evidence: [README agent/task architecture and runtime](https://github.com/theo-kirby/chassis/blob/b9350031580d58328849184974e1368d082f4892/README.md), [agent launch and feedback triggers](https://github.com/theo-kirby/chassis/blob/b9350031580d58328849184974e1368d082f4892/harness/run-agent), [driver starter](https://github.com/theo-kirby/chassis/blob/b9350031580d58328849184974e1368d082f4892/harness/agent-template/driver/SYSTEM.md).
- Basis: explicit and structural.
- Confidence: high.
- Caveats: credentials/model endpoint and individual task definitions must be provisioned; distributed examples do not include private notebook pilot configurations.

## S2 — Coordination

- State: —
- Function: no independently established agent-owned coordination regulator of disturbances among multiple live S1 operations.
- Disturbance / variety regulated: model task outputs may depend on one another, and badly configured trigger cycles can cause runaway repeated jobs; existing routing remains user-configured deterministic conditions.
- Decisive decision or feedback right: no shipped autonomous coordinator judging current cross-agent interference and returning a corrective relation between still-operating units; trigger predicates merely apply preauthored conditions to prior verdict values.
- Decision owner: operator-provided trigger graph plus `run-agent` parser/dispatcher; model agents own their individual verdict content, not the inter-unit coordination policy.
- Supporting / enforcement mechanisms: per-task cron/trigger definitions, `after/on_success/on_failure` conditions and `verdict` K/V comparisons, detached `setsid` launch, optional single-worker supervisor limit.
- Closure path: agent completion/verdict → configured predicate → following task is launched or skipped; generic event feedback does not by itself demonstrate S2 regulation of an inter-S1 interference/oscillation.
- Why this is / is not agent-owned: the README's hypothetical writer/reviewer cycle is a user-composed workflow example; the shipped system does not define an S2-specific autonomous decision right over fleet interactions.
- Evidence: [README triggers and illustrative writer/reviewer flow](https://github.com/theo-kirby/chassis/blob/b9350031580d58328849184974e1368d082f4892/README.md), [trigger evaluator](https://github.com/theo-kirby/chassis/blob/b9350031580d58328849184974e1368d082f4892/harness/run-agent), [supervisor one-slot policy](https://github.com/theo-kirby/chassis/blob/b9350031580d58328849184974e1368d082f4892/docs/supervised-jobs.md).
- Basis: structural.
- Confidence: medium.
- Caveats: an operator can design a specific conflict-regulating multi-agent workflow using triggers, but generic condition-based event routing alone is insufficient for published `C`.

### Absence scope

- Surfaces inspected: trigger parser, agent verdict tool, seeded driver persona, scheduled fleet, example writer/reviewer cycle, supervisor concurrency policy.
- Plausible first-party paths checked: score-routed feedback loops, error triggers, overlapping scheduled runs, run logs and driver editing of individual agent definitions.
- Why no material first-party path remains: the examples and fixed fan-out predicates do not demonstrate a configured S2 agent receiving concrete cross-S1 interference and returning a new attenuation decision to participating S1 units; the driver is a whole-fleet S3 controller when invoked.

## S3 — Inside-and-now control

- State: A(P)
- Function: current whole-fleet supervision, revision of agent/task commitments and intervention in which operational agents and tools may act.
- Disturbance / variety regulated: agent outputs or run failures may show that instructions, tool availability, scheduled work or current fleet priorities no longer satisfy the local operator's goal.
- Decisive decision or feedback right: in the agent-owned Conductor-like **driver** mode, the seeded model examines whole-fleet logs and definitions, chooses which agents/tasks need changes, and writes new prompts/configuration that subsequent model runs use; in the legitimate parent mode, the human independently chooses current runs, agent installation/definitions and protected tool/cron changes through host controls.
- Decision owner: autonomous seeded `driver` AI when interactively invoked for its bounded editable agent-definition surface; the host operator in the distinct direct CLI/control mode. Root-enforced tool and cron restrictions remain constraints in both modes.
- Supporting / enforcement mechanisms: shared `/home/agent` registry, per-agent run logs, dispatcher audit, agent definition files, `chassis run/kill/runs/install-agent/reload-cron`, dashboard and root tool gate.
- Closure path: observed current fleet results/operating constraints → driver or human judges necessary agent/task changes → definitions, run state or refreshed cron/tools are changed through their respective permitted paths → subsequent task agents launch with updated commitments.
- Boundary reachability: the official Docker image ships `harness/agent-template/driver/SYSTEM.md` and supports `chassis run driver`; the host `chassis` CLI and dashboard are part of the same published standard mode. Neither decision right is borrowed from source maintainer governance.
- Why this is / is not agent-owned: the driver model chooses material changes to other agents' roles/tasks after inspecting the fleet, while deterministic cron/parser and secret protection cannot make this judgment; the human mode retains different, direct parent authority.
- Whole-system current view: all local `/home/agent` definitions, aggregate agent run summaries, cron and dispatcher audit; host control additionally sees current containers, active/detached runs, dashboard status and protected configuration.
- Current-control decision scope: fleet agent/task definitions, model choices and instructions under driver write scope; parent controls concrete run/stop, tooling, protected secrets, cron refresh and installation.
- Evidence: [seeded driver decisive rights and limits](https://github.com/theo-kirby/chassis/blob/b9350031580d58328849184974e1368d082f4892/harness/agent-template/driver/SYSTEM.md), [main execution/CLI controls](https://github.com/theo-kirby/chassis/blob/b9350031580d58328849184974e1368d082f4892/chassis), [README driver/fleet](https://github.com/theo-kirby/chassis/blob/b9350031580d58328849184974e1368d082f4892/README.md).
- Basis: explicit and structural.
- Confidence: medium.
- Caveats: driver is *interactive/operator-invoked*, not an always-on self-starting fleet overseer; model edits to cron require separate operator `reload-cron`. The `A(P)` describes alternative supported ownership closures, not simultaneous ultimate authorities.

### S3 ownership mode matrix

| Mode | Decisive owner | Trigger | Closure / return | Evidence |
| --- | --- | --- | --- | --- |
| Autonomous driver (`A`) | Invoked seeded driver model | Operator starts `chassis run driver`, model sees fleet logs/agent definitions | Agent judges and edits agent/task definitions directly; later operational agents load changed instructions | [`driver/SYSTEM.md`](https://github.com/theo-kirby/chassis/blob/b9350031580d58328849184974e1368d082f4892/harness/agent-template/driver/SYSTEM.md), [`run-agent`](https://github.com/theo-kirby/chassis/blob/b9350031580d58328849184974e1368d082f4892/harness/run-agent) |
| Parent-governed direct fleet mode (`P`) | Legitimate host operator | Human inspects current runs/dashboard and decides intervention | `chassis run/kill/install-agent`, protected tool update or cron reload changes the next task operations | [`chassis` CLI](https://github.com/theo-kirby/chassis/blob/b9350031580d58328849184974e1368d082f4892/chassis), [README operator workflow](https://github.com/theo-kirby/chassis/blob/b9350031580d58328849184974e1368d082f4892/README.md) |

## S3* — Complementary audit

- State: —
- Function: no bundled agent-owned independent audit of fleet control or operations with complementary access and returned corrective decision.
- Disturbance / variety regulated: bad reports or a mistaken driver configuration could need independent checking, but the ordinary fleet does not ship an autonomous auditor that can judge those claims.
- Decisive decision or feedback right: none established beyond the original agent's verdicts, deterministic schema/exit checks and optional human review.
- Decision owner: task agents emit verdicts; operator reads dashboards/reports; supervisor validates structure, not semantic truth.
- Supporting / enforcement mechanisms: dispatch audit, trigger logs, model per-run records, structured supervised job reports, SQLite history and host Gmail summaries.
- Closure path: run outputs and logs → optional human inspection or schema checks; no first-party independent reviewer agent judging raw evidence and returning corrections to S3 is packaged.
- Why this is / is not agent-owned: a user can *configure* a separate reviewer in the generic trigger graph, but README's illustration does not ship the reviewer actor, independent evidence access and feedback authority as a standard-deployment mode.
- Evidence: [README example review flow](https://github.com/theo-kirby/chassis/blob/b9350031580d58328849184974e1368d082f4892/README.md), [supervisor report validation caveat](https://github.com/theo-kirby/chassis/blob/b9350031580d58328849184974e1368d082f4892/docs/supervised-jobs.md), [runtime log/trigger model](https://github.com/theo-kirby/chassis/blob/b9350031580d58328849184974e1368d082f4892/harness/run-agent).
- Basis: explicit and structural.
- Confidence: medium.
- Caveats: this does not claim that custom user-authored reviewer agents are impossible; they are outside a bundled independent audit route.

### Absence scope

- Surfaces inspected: seeded driver, current runtime, optional supervisor/report profiles, audit/dashboard, README writer/reviewer example and trigger code.
- Plausible first-party paths checked: score-based reviewer example, run receipts, report schema validation, Gmail notifications and operator monitoring.
- Why no material first-party path remains: no actual shipped reviewer prompt/session with raw evidence access and independent corrective return is configured; mechanical checks and operator monitoring do not establish autonomous S3*.

## S4 — Outside-and-then intelligence

- State: —
- Function: no separate prospective environmental sensing, adaptation option and adoption loop established for Chassis's future capability.
- Disturbance / variety regulated: external changes and the future operating environment may require new agent behaviors, but the driver is instructed to repair observed current fleet performance, not to conduct autonomous future-environment intelligence.
- Decisive decision or feedback right: no dedicated first-party future-oriented external analysis/adoption mandate established.
- Decision owner: human defines future task lineup, external tool/secret expansions and maintenance; driver handles operator-invoked observed current agent-definition adjustments.
- Supporting / enforcement mechanisms: editable agent prompts/models, scheduled tasks, public web tools, user configuration and optional notebook watch jobs.
- Closure path: current operation feedback → possible present driver correction; no separately evidenced outside/future distinction → prospective adaptation option → changed capability feedback loop.
- Why this is / is not agent-owned: the ability to edit task prompts or research the web *if asked* is not proof of a shipped S4 agent with future-environment responsibility.
- Evidence: [driver task/permission boundary](https://github.com/theo-kirby/chassis/blob/b9350031580d58328849184974e1368d082f4892/harness/agent-template/driver/SYSTEM.md), [supervisor development status and next steps](https://github.com/theo-kirby/chassis/blob/b9350031580d58328849184974e1368d082f4892/docs/supervised-jobs.md).
- Basis: structural.
- Confidence: medium.
- Caveats: a particular deployed research fleet could form an S4 loop; the bundled framework and paused job examples do not establish that standing function at this boundary.

### Absence scope

- Surfaces inspected: driver persona, public tool list, task scheduling/triggering, optional supervised watch/research jobs and README configuration.
- Plausible first-party paths checked: prompt self-edit, monitoring logs, periodic web research, adding agents, human rollout and report-driven future changes.
- Why no material first-party path remains: the source specifies present-task/control and user-configurable future work but no first-party owned intelligence mandate for external-and-then adaptation with a decisive adoption loop into current capability.

## S5 — Policy and identity

- State: —
- Function: no runtime ultimate-purpose/identity policy adjudication for the local fleet.
- Disturbance / variety regulated: secret leakage, permission boundaries, unauthorized tool calls and operator instructions need enforcement but do not by themselves produce a genuine identity-level dispute.
- Decisive decision or feedback right: no agent/parent S5 matter with authoritative policy decision returned to the whole fleet; the host operator sets static permissions and operating configuration.
- Decision owner: parent human maintains tool/secret control outside the agent-user runtime, while privileged dispatcher enforces declared rules.
- Supporting / enforcement mechanisms: two-user filesystem, root-owned `.env`, strict tools JSON schema, sudo allowlist, root-only supervised policy and audits.
- Closure path: permission/tool policy → dispatcher validation or refusal → task result/audit; no identity-level issue escalates to legitimate ultimate authority for a new binding policy decision.
- Why this is / is not agent-owned: safety boundaries and static purpose in `SYSTEM.md` constrain agents rather than endowing one with ultimate-policy adjudication rights.
- Evidence: [README security and scope](https://github.com/theo-kirby/chassis/blob/b9350031580d58328849184974e1368d082f4892/README.md), [dispatcher implementation](https://github.com/theo-kirby/chassis/blob/b9350031580d58328849184974e1368d082f4892/harness/run-tool), [supervised allowlist enforcement](https://github.com/theo-kirby/chassis/blob/b9350031580d58328849184974e1368d082f4892/docs/supervised-jobs.md).
- Basis: structural.
- Confidence: medium.
- Caveats: the user can change tool/secret policy on the host, but that is a protected operational configuration action rather than a reconstructed S5 identity-policy loop.

### Absence scope

- Surfaces inspected: driver role/limits, tool dispatcher, host operator control, supervisor fixed policy, security and status surfaces.
- Plausible first-party paths checked: sensitive tool access, model choice, permission edits, agent persona, user approval and source maintainer governance.
- Why no material first-party path remains: a static gate plus ordinary operator control contains no function-specific identity/ultimate-policy conflict, authoritative adjudication and returned governing decision at the assessed fleet boundary.

## Distributed OSS parent arrangement

The public framework can be cloned by independent operators into separate Chassis containers; no shared public runtime state or cross-contributor fleet governance is established by the source repository. `S3=A(P)` refers to the seeded local driver and the legitimate local host operator. The author/developer's notebook operations and project CI are not attributed as this fleet's S4 or S5 owners.

## Self-hosted and non-human modes

The default installed Pi agent fleet uses the local container and external model credentials. A published alternate Claude runtime branch uses the same task/trigger structure. The opt-in supervised job mode creates a separate container per bounded read-only report with human-reviewed reports; three public job definitions ship paused, unlike author's documented private enabled notebook state. No implicit always-on independent reviewer or future-adaptation agent is inferred.

## Recursion

Configured agents each carry separate tasks; scheduled and trigger-linked runs are operational cells. The seeded driver, unlike an arbitrary task, has explicit whole-fleet observable and edit permissions. It can revise agent definitions, but cannot access root-owned tools/secrets or independently reload protected cron; the parent controls those surfaces. Task nesting and cycles alone do not establish another full viable recursion.

## Variety and escalation

Cron and deterministic verdict conditions manage scheduling and output-triggered follow-on runs. Root dispatcher/secret segregation attenuates tool risk; the supervisor applies run/memory/CPU/call limits, retries conservatively and reports unknown outcomes on crashes. The driver can inspect aggregate failures and alter subsequent task instructions, while host operator controls remaining protected constraints. These safeguards are not automatically S2 coordination, independent S3* auditing or S5 ultimate-policy resolution.

## Evidence gaps

- Driver whole-fleet control is supported as an **operator-invoked interactive** agent; there is no claim that it polls continuously or launches any task without the host operator. Its ability to change agent definitions directly is the relevant current-control closure.
- The writer/reviewer `verdict` cycle in README is illustrative; no independently functioning reviewer identity, raw-evidence path and returned audit obligation are bundled by default, hence no S3* positive state.
- Real provider credentials, private enabled supervisor jobs, Gmail delivery and the notebook operator's files are not public assessment evidence. Code and documented standard modes are assessed, not live task success or independent model behavior.

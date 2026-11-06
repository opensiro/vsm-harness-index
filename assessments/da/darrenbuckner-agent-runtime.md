---
harness_id: darrenbuckner-agent-runtime
project_name: agent-runtime (darrenbuckner)
repository: https://github.com/darrenbuckner/agent-runtime
review_ref: cf9e59b2175c4f6a57cc3368bf61568d00d43d16
reviewed_at: 2026-11-06
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

# agent-runtime (darrenbuckner)

## Review boundary

- System in focus: installable `agent_runtime` Python package running one agent cycle from a mission-bearing Git working tree, not the separate `tsharp/agent-runtime` indexed harness or the developer's example/fork management organization.
- Purpose and identity: execute periodic autonomous mission-directed file-work and optional human-reviewed correspondence using a provider-neutral tool loop, durable cycle memory and Git commits.
- Relevant environment: a local checked-out agent repository, existing mission/config files, Git remote updates, inbound mail, externally hosted LLM APIs, configured email provider, schedule triggers and human approval labels.
- Standard-distribution boundary: `src/agent_runtime/` package and `agent-cycle` entrypoint invoked in a mission/config-bearing agent checkout. The separately referenced `ai-agent-template` supplies a deployer's mission, workflow schedule and webhook but is not itself part of this repository's reviewed source.
- Credited operating / distribution surfaces: `run_cycle` with configured Anthropic adapter or optional OpenAI adapter, bounded tool loop, local workspace guards, cycle log, Git commit/push, and optional first-party GitHub Issue email-review client.
- Adjacent first-party surfaces excluded from ownership: the external template fork's specific mission, cron YAML and inbound webhook implementation; project tests with fake LLM/Git remotes; provider vendors; developer changelog and CI outside the installed runtime.
- First-party operating / deployment modes considered: installed scheduled/dispatch cycle with mission/config and authenticated provider, local `AGENT_PUSH=0` development mode, configured optional direct-email mode versus GitHub approval-gated email mode, and Anthropic versus OpenAI-compatible provider adapter. No second model-worker or cross-agent S2 mode is shipped in the package.
- Recursion level: one mission-bound agent whose heartbeat starts one executable S1 cycle and whose subsequent cycles share persisted Git workspace/cycle notes; repeated invocations do not automatically count as independent S1 agents.
- Reviewed revision: `cf9e59b2175c4f6a57cc3368bf61568d00d43d16`.
- Observation date: 2026-11-06.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The CLI reads a user-controlled `MISSION.md` and `config.yaml` from an existing checkout. `run_cycle` constructs an inventory of workspace paths, recent cycle-log decisions, current time, and optionally inbound email; starts an actual configured provider; iterates model-selected file or email tool calls; and appends a `finish_cycle`/failure record. The one commit per cycle is pushed with bounded retry/rebase when another writer has moved the same branch. `Workspace` blocks path traversal and hard-protected mission/config/workflow/log files, while mail recipient and optional GitHub Issue approval are fixed by configuration. A failed run is recorded and exits non-zero; successful delivery of approved email is confirmed before closing the approval Issue. The package exposes adapters/constructors for different models but does not ship the external cron/webhook/template repository. Evidence: [README](https://github.com/darrenbuckner/agent-runtime/blob/cf9e59b2175c4f6a57cc3368bf61568d00d43d16/README.md), [cycle loop](https://github.com/darrenbuckner/agent-runtime/blob/cf9e59b2175c4f6a57cc3368bf61568d00d43d16/src/agent_runtime/loop.py), [tools](https://github.com/darrenbuckner/agent-runtime/blob/cf9e59b2175c4f6a57cc3368bf61568d00d43d16/src/agent_runtime/tools.py), [workspace](https://github.com/darrenbuckner/agent-runtime/blob/cf9e59b2175c4f6a57cc3368bf61568d00d43d16/src/agent_runtime/workspace.py), [Git commits](https://github.com/darrenbuckner/agent-runtime/blob/cf9e59b2175c4f6a57cc3368bf61568d00d43d16/src/agent_runtime/git.py), [review gate](https://github.com/darrenbuckner/agent-runtime/blob/cf9e59b2175c4f6a57cc3368bf61568d00d43d16/src/agent_runtime/email.py).

## Operational model

The running model chooses substantive workspace edits and optional messages in response to the mission, file manifest, prior cycle notes and tool errors. The human/operator installs a template, writes the immutable-to-agent mission and config, schedules the heartbeat and may approve outbound drafts. Runtime guardrails, Git synchronization, email recipient constraints and failure handling enforce those prior decisions but do not autonomously define higher-level policy or current portfolio management. `AGENT_PUSH=0` leaves changes in a local checkout and does not change who selects operational actions. The source's presence of a GitHub review Issue makes email consent observable; it does not convert an ordinary outbound message decision into S5.

## S1 — Operations

- State: A
- Function: execute mission-bound file-work and optional correspondence through open-ended model-selected actions each heartbeat cycle.
- Disturbance / variety regulated: changing repository files and inbound messages, missing prior artifacts, provider stop/refusal, unexpected tool failures, Git conflicts, draft approvals and differing mission-specific subtasks.
- Decisive decision or feedback right: select read/create/modify/delete/email calls and arguments, decide the final cycle summary and subsequent notes, and choose a new action after tool feedback.
- Decision owner: configured Anthropic or OpenAI provider model within the first-party runtime; deployer/recipient approval restricts some side effects, and the code owns invariant validation.
- Supporting / enforcement mechanisms: provider adapter, `ToolContext` dispatch, `Workspace` protection, max tool rounds, cycle-log persistence, Git commit/push with rebase retry, and optional email Issue labels.
- Closure path: checkout mission/manifest/cycle-log → model step → first-party file/email tool result → provider `add_tool_results` → next model step; on `finish_cycle`, notes/edits persist as a Git commit and become inputs to subsequent externally triggered cycles.
- Boundary reachability: installed `agent-cycle`/`python -m agent_runtime` directly executes `run_cycle`, `make_provider`, the tool registry and local workspace, requiring only a legitimate deployer's mission/config/checkout/provider. Tests and the separate template are not borrowed as a decision owner.
- Why this is / is not agent-owned: without the model `provider.step`, the guard/checkpoint/Git machinery cannot choose arbitrary mission edits or adapt to new tool observations; fixed file guards still protect mission boundaries.
- Evidence: [runtime cycle](https://github.com/darrenbuckner/agent-runtime/blob/cf9e59b2175c4f6a57cc3368bf61568d00d43d16/src/agent_runtime/loop.py), [model tool spec/execute](https://github.com/darrenbuckner/agent-runtime/blob/cf9e59b2175c4f6a57cc3368bf61568d00d43d16/src/agent_runtime/tools.py), [mission prompt](https://github.com/darrenbuckner/agent-runtime/blob/cf9e59b2175c4f6a57cc3368bf61568d00d43d16/src/agent_runtime/prompt.py), [entrypoint](https://github.com/darrenbuckner/agent-runtime/blob/cf9e59b2175c4f6a57cc3368bf61568d00d43d16/src/agent_runtime/__main__.py), [provider adapters](https://github.com/darrenbuckner/agent-runtime/tree/cf9e59b2175c4f6a57cc3368bf61568d00d43d16/src/agent_runtime/llm).
- Basis: structural.
- Confidence: high for the shipped wiring.
- Caveats: no live API/model or scheduled GitHub Actions run was exercised in this Index review. The README identifies Anthropic as in-production and the OpenAI adapter as tested with a fake client only; provider modes are not equated as proven reliable.

## S2 — Coordination

- State: —
- Function: no cross-agent coordination loop between separate first-party S1 units is supplied in this runtime package.
- Disturbance / variety regulated: concurrent Git changes from an external webhook/source writer may race the agent's final push; this is a Git integration collision, not proof of multiple runtime-owned agent S1 units.
- Decisive decision or feedback right: fixed push/fetch/rebase retries preserve commits; no agent decides a mutual plan or interference response for two autonomous S1 work cells.
- Decision owner: deterministic Git push policy and external source writers, not a first-party S2 coordinator.
- Supporting / enforcement mechanisms: per-cycle Git commit, `PUSH_ATTEMPTS`, fetch/rebase conflict detection, workspace restrictions and optional email queue.
- Closure path: failed push triggers a local fetch/rebase/retry; there is no demonstrated feedback regulating distinct agent S1 operations together.
- Why this is / is not agent-owned: a second external webhook writer and conflict-preserving Git operations do not constitute two model-owned S1 cells with a coordination decision path at this package recursion.
- Evidence: [Git retry](https://github.com/darrenbuckner/agent-runtime/blob/cf9e59b2175c4f6a57cc3368bf61568d00d43d16/src/agent_runtime/git.py), [cycle contract](https://github.com/darrenbuckner/agent-runtime/blob/cf9e59b2175c4f6a57cc3368bf61568d00d43d16/src/agent_runtime/loop.py), [README template separation](https://github.com/darrenbuckner/agent-runtime/blob/cf9e59b2175c4f6a57cc3368bf61568d00d43d16/README.md).
- Basis: structural negative.
- Confidence: medium-high.
- Caveats: a deployment can compose multiple forks/agents around GitHub, but that external organization is not a first-party coordinated mode proven by this source.

### Absence scope

- Surfaces inspected: package loop/tools/Git/error paths, README, provider adapters, mail approval client and tests' documented fixture boundaries.
- Plausible first-party paths checked: repeated cron cycles, webhook vs cycle pushes, retry/rebase, separate provider choice and email review queue as candidates for cross-S1 conflict regulation.
- Why no material first-party path remains: only one mission-running model loop is first-party; the external webhook and independent template forks are adjacent, so no two runtime S1 units and returned inter-S1 regulation are established.

## S3 — Inside-and-now control

- State: —
- Function: no distinct whole-system managerial current-control decision loop over an agent portfolio's resources/commitments is wired.
- Disturbance / variety regulated: token/round limits, failed cycles, protected files and Git push conflicts are handled per cycle by rules, without aggregate resource negotiation.
- Decisive decision or feedback right: the deployer fixes model/rounds/mission and schedule, and failures mark the run red; no first-party owner revises whole-system commitments based on a current control view.
- Decision owner: external operator/config for ceilings; deterministic runtime for enforcement; model for S1 operational choices.
- Supporting / enforcement mechanisms: config `max_tokens`/`max_tool_rounds`, append-only cycle logs, failure nonzero exit, protected paths, Git retries and GH Actions host status.
- Closure path: a cycle is bounded or fails, and future cycles read the log, but no separate S3 allocation/intervention judgment returns to regulate the entire active portfolio.
- Why this is / is not agent-owned: after conceptually removing the model, the same fixed limits and failure transitions apply; that does not prove autonomously chosen whole-system present priorities.
- Evidence: [configuration](https://github.com/darrenbuckner/agent-runtime/blob/cf9e59b2175c4f6a57cc3368bf61568d00d43d16/src/agent_runtime/config.py), [loop enforcement](https://github.com/darrenbuckner/agent-runtime/blob/cf9e59b2175c4f6a57cc3368bf61568d00d43d16/src/agent_runtime/loop.py), [cycle log](https://github.com/darrenbuckner/agent-runtime/blob/cf9e59b2175c4f6a57cc3368bf61568d00d43d16/src/agent_runtime/cyclelog.py).
- Basis: structural negative.
- Confidence: medium-high.
- Caveats: a repository owner may externally operate a fleet or revise a particular mission; that current-control authority is not a shipped runtime management loop.

### Absence scope

- Surfaces inspected: config, model loop, cycle logger, Git push/exception rules, CLI, provider interface and README host/runtime contract.
- Plausible first-party paths checked: max rounds, error escalation to GitHub Actions, cycle history, owner-protected config/mission and per-cycle email gating.
- Why no material first-party path remains: all evidenced mechanisms are local S1 constraints or adjacent host/owner actions, without a whole-system current view and distinct decisive intervention path at this boundary.

## S3* — Complementary audit

- State: —
- Function: no independently sourced complementary assessment of the cycle's operational success claims is part of the installed agent loop.
- Disturbance / variety regulated: model-written summaries might misstate actual code changes or correspondence; the package does not send them for an independent audit decision.
- Decisive decision or feedback right: first-party runtime reports file-tool outcomes and Git push status; no independent auditor judges the mission result and returns a finding to present control.
- Decision owner: absent in the shipped runtime; the operator may inspect Git history outside this distribution.
- Supporting / enforcement mechanisms: append-only cycle log, Git commit lineage, error codes and test fixtures; GitHub email review is a normal consent gate, not complementary audit of completed work.
- Closure path: log and commits are observable but no complementary review verdict arrives through a first-party feedback path.
- Why this is / is not agent-owned: the same operational path authors the cycle narrative and tool transcript; Git push confirmation checks transport, not task truth.
- Evidence: [cycle log](https://github.com/darrenbuckner/agent-runtime/blob/cf9e59b2175c4f6a57cc3368bf61568d00d43d16/src/agent_runtime/cyclelog.py), [loop](https://github.com/darrenbuckner/agent-runtime/blob/cf9e59b2175c4f6a57cc3368bf61568d00d43d16/src/agent_runtime/loop.py), [Git](https://github.com/darrenbuckner/agent-runtime/blob/cf9e59b2175c4f6a57cc3368bf61568d00d43d16/src/agent_runtime/git.py), [email approval](https://github.com/darrenbuckner/agent-runtime/blob/cf9e59b2175c4f6a57cc3368bf61568d00d43d16/src/agent_runtime/email.py).
- Basis: structural negative.
- Confidence: medium-high.
- Caveats: the external template deployment could add branch protection, human code review or independent CI; none is borrowed into this source-only runtime assessment.

### Absence scope

- Surfaces inspected: loop output and failure paths, cycle log, Git commit/rebase, mail review, README, package tests and external-template boundaries.
- Plausible first-party paths checked: Git push success, Actions red/green signal, email-draft human approval, cycle-log facts and test suite as candidate independent access.
- Why no material first-party path remains: operational transport verification, task consent and developer tests lack a separate independent audit judgment and feedback loop for deployed cycle outcomes.

## S4 — Outside-and-then intelligence

- State: —
- Function: no specifically prospective external-environment modeling and capability-adaptation loop is shipped for the harness.
- Disturbance / variety regulated: new inbound requests, clock time and repository changes are inputs to current mission execution rather than an independently owned future-option/capability revision cycle.
- Decisive decision or feedback right: the model chooses the next file/email task given a pre-existing mission; it does not have a first-party path to make legitimate future harness capability/adaptation decisions.
- Decision owner: model for S1 mission work; template/mission author for changing product or policy capability outside the package.
- Supporting / enforcement mechanisms: timed cycle invocation by adjacent cron workflow, current-time prompt, previous notes, file manifest and inbound snapshots.
- Closure path: a subsequent cron cycle consumes notes and updated files as ordinary S1 context; no prospective option is selected and returned as a change to present system capability under S4 authority.
- Why this is / is not agent-owned: planning the next mission action or persisting next-cycle notes does not establish an external-and-then intelligence function.
- Evidence: [prompt assembly](https://github.com/darrenbuckner/agent-runtime/blob/cf9e59b2175c4f6a57cc3368bf61568d00d43d16/src/agent_runtime/prompt.py), [cycle loop](https://github.com/darrenbuckner/agent-runtime/blob/cf9e59b2175c4f6a57cc3368bf61568d00d43d16/src/agent_runtime/loop.py), [cycle persistence](https://github.com/darrenbuckner/agent-runtime/blob/cf9e59b2175c4f6a57cc3368bf61568d00d43d16/src/agent_runtime/cyclelog.py).
- Basis: structural negative.
- Confidence: medium-high.
- Caveats: a deployer may supply a mission expressly about research or coding future features, but that changes the concrete mission-specific composition and cannot be inferred for every standard-distribution agent-runtime install.

### Absence scope

- Surfaces inspected: mission prompt, time and inbound handling, cycle-log next notes, tool surface, protected mission config and provider extension notes.
- Plausible first-party paths checked: time-sensitive autonomous tasks, persistent next-cycle notes, optional inbound correspondence, provider extensibility and future mission files.
- Why no material first-party path remains: observed paths regulate current S1 tasks; no shipped future-environment modeling, adaptation right and resulting updated present capability loop is established at this recursion.

## S5 — Policy and identity

- State: —
- Function: no first-party identity/ultimate-policy deliberation-and-return path is evidenced beyond static parent-provided mission constraints.
- Disturbance / variety regulated: risky or misdirected model actions are attenuated through protected mission/config files, path restrictions and email recipient/approval rules, but conflicts about the agent's identity or ultimate policy are not adjudicated in the runtime.
- Decisive decision or feedback right: a human deployer edits `MISSION.md`/`config.yaml` outside model-write capability and may label ordinary email drafts approved; no in-runtime identity-policy escalation to a legitimate parent is supplied.
- Decision owner: external owner for static setup and routine email authorization; no evidenced first-party S5 decision process with returned identity-policy closure.
- Supporting / enforcement mechanisms: `HARD_PROTECTED`, invalid-config failure, prompt rules, fixed `to_address`, GitHub `email-draft`/`approved` labels and workspace path guards.
- Closure path: the next cycle reads whatever mission/config the owner installed, but there is no runtime identity-policy proposal → legitimate authority's adjudication → returned decision loop; email approval operates at task-action level.
- Why this is / is not agent-owned: the model cannot edit the mission or guardrails. Human ability to change configuration does not alone satisfy a supported S5 parent mode under the released Methodology.
- Evidence: [hard-protected config](https://github.com/darrenbuckner/agent-runtime/blob/cf9e59b2175c4f6a57cc3368bf61568d00d43d16/src/agent_runtime/config.py), [workspace guard](https://github.com/darrenbuckner/agent-runtime/blob/cf9e59b2175c4f6a57cc3368bf61568d00d43d16/src/agent_runtime/workspace.py), [prompt](https://github.com/darrenbuckner/agent-runtime/blob/cf9e59b2175c4f6a57cc3368bf61568d00d43d16/src/agent_runtime/prompt.py), [email consent](https://github.com/darrenbuckner/agent-runtime/blob/cf9e59b2175c4f6a57cc3368bf61568d00d43d16/src/agent_runtime/email.py).
- Basis: structural negative.
- Confidence: medium-high.
- Caveats: the external GitHub repository owner has ultimate identity authority over the installed fork, but the source does not document a function-specific parent governance return loop distinct from normal file/config maintenance.

### Absence scope

- Surfaces inspected: mission and config loading, protected path checks, prompt, mail review issue client, Git push and README distribution model.
- Plausible first-party paths checked: human-owned `MISSION.md`, `config.yaml`, protected workflows, automatic failure propagation and email approval label.
- Why no material first-party path remains: these show static bounds and ordinary operational authorization, not a first-party identity-policy escalation/adjudication channel with returned closure at the assessed recursion.

## Recursion

Cycle invocations share mission and Git memory and can absorb local task variety, but they are repeated operation of one work unit rather than separate independently viable subsystems. Independent forks/tenants/owners can deploy multiple instances, yet this package does not provide their shared metasystem, so multi-agent organizational functions are not inferred.

## Variety and escalation

The model's open-ended file tools and remembered cycle notes amplify operational response variety; hard-protected paths, fixed recipient, bounded rounds and single-email limit attenuate unsafe or unintended choices. Tool errors are returned to the model, while unhandled failures become a red run/log for operator awareness. That exception surface is not independently proved to be an algedonic channel or S3–S5 response authority.

## Evidence gaps

- Source-only review of the pinned Python package. No live Anthropic/OpenAI key, Actions heartbeat, webhook/Resend sender, human email approval or Git push to an external owner was exercised here.
- The concrete template fork and owner-specific MISSION policy are separate repositories/modes; no imported S2/S3/S3*/S4/S5 closure is claimed from them.
- The configured Anthropic mode is documented as in production; the OpenAI integration is only fake-client tested at the pinned source. No blanket provider parity or sustained operational viability claim follows.

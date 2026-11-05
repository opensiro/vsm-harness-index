---
harness_id: agent-control-tower
project_name: agent-control-tower
repository: https://github.com/evolution301/agent-control-tower
review_ref: 14c6c98aa3ab741a5fe42afe10021d3b16deeb4d
reviewed_at: 2026-11-05
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: P
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# agent-control-tower

## Review boundary

- System in focus: one locally installed control-tower workspace, its role agents, file-backed task board, report verification and human/operator CLI.
- Purpose and identity: dispatch role-specific work to model-backed sessions, persist claims and artifacts, independently check work products and allow the operator to accept or rework.
- Relevant environment: several role agents, conflicting file edits, unverifiable completion claims, failed work, lost context and operator attention.
- Standard-distribution boundary: `tower` Python CLI, its shipped `openai`, `dsh`, `cli`, and `mock` adapters, task board, verifier, role configuration and local dashboard; the `mock` adapter is not itself autonomous.
- Credited operating / distribution surfaces: [CLI and control operations](https://github.com/evolution301/agent-control-tower/blob/14c6c98aa3ab741a5fe42afe10021d3b16deeb4d/src/control_tower/cli.py), [model adapter](https://github.com/evolution301/agent-control-tower/blob/14c6c98aa3ab741a5fe42afe10021d3b16deeb4d/src/control_tower/adapters/openai_compat.py), [dispatch](https://github.com/evolution301/agent-control-tower/blob/14c6c98aa3ab741a5fe42afe10021d3b16deeb4d/src/control_tower/dispatch.py), [board](https://github.com/evolution301/agent-control-tower/blob/14c6c98aa3ab741a5fe42afe10021d3b16deeb4d/src/control_tower/board.py), [verifier](https://github.com/evolution301/agent-control-tower/blob/14c6c98aa3ab741a5fe42afe10021d3b16deeb4d/src/control_tower/verify.py) and [documented operating modes](https://github.com/evolution301/agent-control-tower/blob/14c6c98aa3ab741a5fe42afe10021d3b16deeb4d/README.md).
- Adjacent first-party surfaces excluded from ownership: tests, offline mock demo, screenshots, example `tower.toml` files, packaging/release code and the private internal capabilities of any DSH/Claude/Codex session connected through an adapter.
- First-party operating / deployment modes considered: local OpenAI-compatible model-and-shell loop; DSH or external CLI-backed role; human dispatch/accept/rework, local read-only panel, serial batch and optional verification commands.
- Recursion level: one installed multi-role control-tower workspace. Role-executing models are S1 components, not automatically separate S3–S5 owners at tower recursion.
- Reviewed revision: `14c6c98aa3ab741a5fe42afe10021d3b16deeb4d`.
- Observation date: 2026-11-05.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The Python CLI loads a YAML-style `tower.toml` with roles, allowed write scopes, adapters and verification requirements. A dispatch creates a task and renders its role-specific prompt; the first-party `openai` adapter conducts a bounded model/tool conversation with a shell tool, while the DSH/CLI adapters invoke configured external sessions. An append-only JSONL ledger and per-task materialized files record progress, reports, attempts and assignments. A terminal board, attention command and read-only web panel expose all roles, current tasks and exceptions. `tower accept` checks report structure, existence of claimed files and optional actual workspace commands; failures return the task to rework. `tower batch` iterates role dispatches, optionally adding a delay; it is not an inter-agent negotiation controller. [README](https://github.com/evolution301/agent-control-tower/blob/14c6c98aa3ab741a5fe42afe10021d3b16deeb4d/README.md); [CLI](https://github.com/evolution301/agent-control-tower/blob/14c6c98aa3ab741a5fe42afe10021d3b16deeb4d/src/control_tower/cli.py); [board](https://github.com/evolution301/agent-control-tower/blob/14c6c98aa3ab741a5fe42afe10021d3b16deeb4d/src/control_tower/board.py).

## Operational model

The role model owns steps and tool choices inside a delegated brief. The local operator owns role definitions, task intent, assignment and whether evidence is sufficient to accept or rework. The verifier is a first-party deterministic post-report checker; its optional commands independently observe the workspace rather than merely copying model assertions. Thus the installed tower has agent-owned task execution and an operator-governed current-work loop, but no first-party agent deciding portfolio-wide priorities or long-term identity. [Model loop](https://github.com/evolution301/agent-control-tower/blob/14c6c98aa3ab741a5fe42afe10021d3b16deeb4d/src/control_tower/adapters/openai_compat.py); [CLI commands](https://github.com/evolution301/agent-control-tower/blob/14c6c98aa3ab741a5fe42afe10021d3b16deeb4d/src/control_tower/cli.py#L134-L291).

## S1 — Operations

- State: A
- Function: configured role model performs a delegated task with context and workspace tools, reporting the resulting work product.
- Disturbance / variety regulated: ambiguous brief, changing code/file contents and command feedback encountered within a role assignment.
- Decisive decision or feedback right: the first-party OpenAI-compatible model loop selects tool calls and the next work step based on returned outputs, within a configured step budget.
- Decision owner: role model in the supported OpenAI-compatible adapter; externally configured CLI/DSH agents also have task-local discretion, but their private internal autonomy is not imputed to the tower.
- Supporting / enforcement mechanisms: role prompt with mandate/write scopes, model-chat tool loop, shell execution, task assignment, artifacts and report intake.
- Closure path: operator dispatches work → role model requests tool calls → host returns workspace observations → model adapts tool calls and returns a result → board records the report and the operator may accept or rework.
- Boundary reachability: `dispatch` selects the shipped `openai` adapter and calls its own model-to-`run_shell` loop; it is executable with a user-supplied compatible API endpoint and key, not merely an abstract pluggable interface.
- Why this is / is not agent-owned: the model chooses the substantive implementation steps; neither the CLI nor the operator predetermines each tool call.
- Evidence: [adapter model/tool loop](https://github.com/evolution301/agent-control-tower/blob/14c6c98aa3ab741a5fe42afe10021d3b16deeb4d/src/control_tower/adapters/openai_compat.py#L47-L144); [dispatch integration](https://github.com/evolution301/agent-control-tower/blob/14c6c98aa3ab741a5fe42afe10021d3b16deeb4d/src/control_tower/dispatch.py#L85-L133); [README modes](https://github.com/evolution301/agent-control-tower/blob/14c6c98aa3ab741a5fe42afe10021d3b16deeb4d/README.md).
- Basis: first-party control flow in a supported installed mode.
- Confidence: high for reachable decision structure; no paid model execution claimed.
- Caveats: mock-mode deterministic completion is not S1 evidence, and the shell tool is a host-enforced mechanism rather than an S1 decision owner.

## S2 — Coordination

- State: —
- Function: no materially closed, function-specific feedback relation regulating disturbances *between* distinct S1 units was established.
- Disturbance / variety regulated: potential collisions when roles edit the same workspace and receive overlapping instructions.
- Decisive decision or feedback right: role assignments and write-scope advice are configured by the operator; the CLI iterates a static batch and never detects or resolves competing edits across S1 agents.
- Decision owner: no first-party S2 owner shown for inter-S1 disturbance feedback.
- Supporting / enforcement mechanisms: per-role workspace paths, instruction-level write scopes, optional batch spacing and task-key idempotency.
- Closure path: dispatch routes tasks to roles and records status; no observed conflict-feedback → changed inter-role behavior relation is implemented.
- Why this is / is not agent-owned: routing, sequential iteration, distinct directories and prompts alone do not evidence autonomous/constructed S2 coordination.
- Evidence: [batch loop and serial gap](https://github.com/evolution301/agent-control-tower/blob/14c6c98aa3ab741a5fe42afe10021d3b16deeb4d/src/control_tower/cli.py#L174-L210); [prompt write-scope text](https://github.com/evolution301/agent-control-tower/blob/14c6c98aa3ab741a5fe42afe10021d3b16deeb4d/src/control_tower/dispatch.py#L69-L83); [role/task states](https://github.com/evolution301/agent-control-tower/blob/14c6c98aa3ab741a5fe42afe10021d3b16deeb4d/src/control_tower/board.py).
- Basis: bounded structural negative, not a statement that coordinated external agent teams are impossible.
- Confidence: medium-high.
- Caveats: configured external DSH sessions may coordinate themselves, but their private inter-agent control is outside this boundary.

### Absence scope

- Surfaces inspected: dispatch, batch CLI, board, role configuration, README, architecture and first-party adapters.
- Plausible first-party paths checked: serialized batch, role write-scope instructions, duplicate dispatch key, per-role directories and ledger feedback.
- Why no material first-party path remains: none compares concurrent S1 claims/changes, supplies conflict detection to a distinct coordinating owner, or closes inter-S1 disturbance feedback; they only separate or order work by configured convention.

## S3 — Inside-and-now control

- State: P
- Function: a human lead supervises the entire local work portfolio and intervenes in role commitments, acceptance and rework.
- Disturbance / variety regulated: unfinished tasks, failures, evidence gaps and attention overload across active roles.
- Decisive decision or feedback right: operator chooses role and brief, changes the role roster, sees all task statuses and attention, accepts or sends work back for another attempt.
- Decision owner: local lead/operator in the documented self-hosted mode; not the model running a delegated S1 task.
- Supporting / enforcement mechanisms: full board/snapshot, attention list, inbox, audit ledger, role-add/remove and `accept`/`rework` commands.
- Closure path: operator inspects whole-board/attention state → assigns new work or selects rework, acceptance and role setup → mutated task/role state governs next dispatch and future capacity allocation.
- Boundary reachability: the same CLI exposes both a complete task-role view and actionable role/dispatch/rework commands against the same persisted board used by actual adapters.
- Why this is / is not agent-owned: the lead owns cross-role current commitments; transitions, status views and retry counters are deterministic supporting mechanics, not autonomous resource decisions.
- Whole-system current view: `build_snapshot`/`tower board` aggregates role states, tasks in flight and attention across the workspace, not just an individual report.
- Current-control decision scope: selection/assignment of current work to roles, who remains active on the roster, acceptance of commitments and intervention on rework/escalation.
- Evidence: [board and attention commands](https://github.com/evolution301/agent-control-tower/blob/14c6c98aa3ab741a5fe42afe10021d3b16deeb4d/src/control_tower/cli.py#L218-L291); [dispatch/accept/rework](https://github.com/evolution301/agent-control-tower/blob/14c6c98aa3ab741a5fe42afe10021d3b16deeb4d/src/control_tower/cli.py#L134-L210); [role roster commands](https://github.com/evolution301/agent-control-tower/blob/14c6c98aa3ab741a5fe42afe10021d3b16deeb4d/src/control_tower/cli.py#L396-L460); [board task state](https://github.com/evolution301/agent-control-tower/blob/14c6c98aa3ab741a5fe42afe10021d3b16deeb4d/src/control_tower/board.py).
- Basis: complete first-party operator control loop.
- Confidence: medium-high.
- Caveats: human acceptance alone would not be S3; the claim also requires the whole-role view and operational role/assignment changes. The dashboard is read-only; decisions return through CLI.

## S3* — Complementary audit

- State: C
- Function: a separately invoked verification path checks report claims against actual workspace artifacts and configured executable commands before acceptance.
- Disturbance / variety regulated: false positive claims that files exist or checks passed when no underlying artifact/output supports them.
- Decisive decision or feedback right: configured verifier requirements select mandatory report evidence, filesystem checks and optional real commands; the operator invokes acceptance and determines subsequent rework.
- Decision owner: first-party deterministic verification constructor plus explicit human acceptance owner; no independently deciding AI auditor is bundled.
- Supporting / enforcement mechanisms: `verify_report`, file existence checks, subprocess command execution, structured findings and mandatory rejection-to-rework path.
- Closure path: agent submits ordinary markdown report → accept invokes verifier's **workspace filesystem and real commands** → failed independent observations produce problems → CLI transitions to `rework`; passing checks allow `accepted` → affected task's next execution/acceptance changes.
- Boundary reachability: verification is called directly in shipped `cmd_accept` and `cmd_dispatch`; optional `verify_commands` are supported configuration, with non-optional file-existence checks always executed.
- Why this is / is not agent-owned: complementary observations are independent of the report text but the checks are deterministic/configured and the ultimate decision is human; hence constructor-mode `C`, not autonomous `A`.
- Claim being audited: a role's report that an artifact exists and specified checks were performed and succeeded.
- Ordinary reporting path: `parse_report` ingests model-authored sections (`Files`, `Checks`, `Summary`, `Status`) into task/report and inbox.
- Complementary access path: verifier reads actual workspace paths and executes configured shell verification commands with return codes and recorded output tails.
- Independence boundary: filesystem and command exit codes do not rely on the model's natural-language claim; however same workspace is writable by the agent and config may omit executable checks, so this is limited evidence of artifact existence/command results, not independent work-quality certification.
- Who acts on findings: `cmd_accept` refuses transition to accepted and puts the task into rework; operator can re-dispatch under configured round limit.
- Evidence: [verification implementation](https://github.com/evolution301/agent-control-tower/blob/14c6c98aa3ab741a5fe42afe10021d3b16deeb4d/src/control_tower/verify.py#L31-L98); [accept and rework control](https://github.com/evolution301/agent-control-tower/blob/14c6c98aa3ab741a5fe42afe10021d3b16deeb4d/src/control_tower/cli.py#L265-L291); [reported-content parsing](https://github.com/evolution301/agent-control-tower/blob/14c6c98aa3ab741a5fe42afe10021d3b16deeb4d/src/control_tower/dispatch.py#L135-L174).
- Basis: real alternate evidence path and mandatory gate; constructor classification.
- Confidence: medium.
- Caveats: a malicious role could manipulate shared files, and the verifier does not independently understand semantic correctness; stronger audit requires configured commands or an independent reviewer with separate trust boundary.

## S4 — Outside-and-then intelligence

- State: —
- Function: no shipped loop senses external/future changes and revises the tower's capability or operating model as an adaptation decision.
- Disturbance / variety regulated: future environmental change is not an independent monitored input into tower adaptation.
- Decisive decision or feedback right: missing; an operator can modify role configuration and agents can be asked to research, but no built-in future/environment intelligence owner returns adopted changes.
- Decision owner: no S4 actor in the assessed tower.
- Supporting / enforcement mechanisms: manually edited roles/config, briefs, history and optional external model work.
- Closure path: no first-party external/prospective sensing → adaptive option → decided capability change loop.
- Why this is / is not agent-owned: model-generated suggestions within a task and generic ability to edit configuration do not establish a returned future-directed adaptation function.
- Evidence: [configuration](https://github.com/evolution301/agent-control-tower/blob/14c6c98aa3ab741a5fe42afe10021d3b16deeb4d/src/control_tower/config.py); [role setup and manual CLI changes](https://github.com/evolution301/agent-control-tower/blob/14c6c98aa3ab741a5fe42afe10021d3b16deeb4d/src/control_tower/cli.py#L396-L460); [architecture](https://github.com/evolution301/agent-control-tower/blob/14c6c98aa3ab741a5fe42afe10021d3b16deeb4d/docs/architecture.md).
- Basis: bounded source negative.
- Confidence: high for inspected first-party behavior.
- Caveats: a separately created strategy role is theoretically possible but not instantiated as S4 closure.

### Absence scope

- Surfaces inspected: README, architecture, board, dispatch, config, adapters, role administration and verification.
- Plausible first-party paths checked: operator role edits, task portfolio reports, attention alerts and arbitrary research tasks.
- Why no material first-party path remains: these implement present task processing or open-ended external composition without a packaged distinction of future threats/options and return of a selected adaptation to tower capability.

## S5 — Policy and identity

- State: —
- Function: no function-specific ultimate-policy/identity conflict resolution loop with legitimate authority and return is furnished.
- Disturbance / variety regulated: competing ultimate mandates or exceptional organizational policy issues are not represented as a distinct operating transaction.
- Decisive decision or feedback right: operator supplies briefs and role policies in configuration, but no S5 question-to-final-authority-and-back path is established.
- Decision owner: operator controls the config outside any demonstrated S5 procedure.
- Supporting / enforcement mechanisms: static role descriptions, `mandate` metadata (`requester`, `strength`, `policy`) and user-issued task commands.
- Closure path: ordinary task mandates are persisted and read during execution; no ultimate-policy issue → adjudication → authoritative resolution → governed future operation loop is implemented.
- Why this is / is not agent-owned: passing an operator policy string to a role and enforcing task-specific rounds is not deciding collective identity.
- Evidence: [mandate creation](https://github.com/evolution301/agent-control-tower/blob/14c6c98aa3ab741a5fe42afe10021d3b16deeb4d/src/control_tower/cli.py#L152-L164); [board mandate storage](https://github.com/evolution301/agent-control-tower/blob/14c6c98aa3ab741a5fe42afe10021d3b16deeb4d/src/control_tower/board.py#L43-L164); [role configuration](https://github.com/evolution301/agent-control-tower/blob/14c6c98aa3ab741a5fe42afe10021d3b16deeb4d/src/control_tower/config.py).
- Basis: bounded structural negative.
- Confidence: high for installed tower.
- Caveats: the human operator has ultimate out-of-band control of a local installation, but authority alone does not prove a first-party S5 feedback loop.

### Absence scope

- Surfaces inspected: full tower CLI commands, task/mandate state, role configuration, prompts and verifier.
- Plausible first-party paths checked: mandate metadata, role charter, acceptance/rework/escalation, operator settings and audit ledger.
- Why no material first-party path remains: these are task- or current-work decisions; the product does not create and resolve an identity/ultimate-policy issue or feed an authoritative S5 judgment back as a governing operating decision.

## Recursion

The local workspace is the chosen recursion; external DSH sessions or API models may have internal roles of their own, but only their task-local execution is credited. `tower board` observes local roles and task states, not a larger multi-project organization. The independent review of a role report is one function in the tower, not automatically a complete second viable system.

## Variety and escalation

Briefs, named roles and write scopes constrain operational variety. The structured report can raise attention states `ready`, `blocked` and `failed`; unsuccessful report verification returns work to rework and the round budget stops endless retries. The independent artifact check is limited to existence and optional commands and cannot guarantee semantically sound delivery. Operator attention is a current-control exception path rather than proof of S4 or S5.

## Evidence gaps

- This assessment is based on pinned source and documented modes. `pytest` is not installed in the available review runtime (`python -m pytest` returned `No module named pytest`); no upstream test-pass assertion is made.
- No paid OpenAI-compatible or DSH model session was executed; first-party model/tool loop and adapter reachability are source-grounded.
- The positive S3* state claims a constructed independent observation path, not an independently autonomous audit agent or protection against an agent editing the same checked workspace.
- Concurrency and write-scope advice were inspected; without an inter-S1 conflict-feedback closure they were not upgraded to S2.

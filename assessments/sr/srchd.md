---
harness_id: srchd
project_name: srchd
repository: https://github.com/dust-tt/srchd
review_ref: 4b5ffb44bdc6bb1d2181d746ec951dd30f89ed08
reviewed_at: 2026-11-10
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: C
autonomy_s5: —
---

# srchd

## Review boundary

- System in focus: A first-party `srchd` experiment operating several independently model-driven research agents against a shared experiment database, publication/review workflow and optional agent-owned research computer. The running CLI/runner and deliberately composable exported self-edit MCP server are distinguished as separate operating/constructor surfaces.
- Purpose and identity: Search hard research/reasoning problems through independent agent investigation, peer-reviewed publications, citations and reported solutions, with experiment-level human setup.
- Relevant environment: Research problem and findings, conflicting submissions, unverified proofs/code, reviewer disagreement, new publications, agent feedback, token/cost pressure and agent-computer artifacts.
- Standard-distribution boundary: `src/srchd.ts agent run` instantiates multiple `Runner`s, each with a model/tool loop and always-on publication and goal-solution MCP servers; review requests and verdicts persist in SQLite. The `research` profile adds independent computer/web tools. The separately exported `createSystemPromptSelfEditServer()` is reviewed only as an S4-specific constructor, **not** as an active default CLI feature.
- Credited operating / distribution surfaces: [CLI and experiment orchestration](https://github.com/dust-tt/srchd/blob/4b5ffb44bdc6bb1d2181d746ec951dd30f89ed08/src/srchd.ts), [agent tick/feedback](https://github.com/dust-tt/srchd/blob/4b5ffb44bdc6bb1d2181d746ec951dd30f89ed08/src/runner/index.ts), [publication and review tools](https://github.com/dust-tt/srchd/blob/4b5ffb44bdc6bb1d2181d746ec951dd30f89ed08/src/tools/publications.ts), [review persistence/admission](https://github.com/dust-tt/srchd/blob/4b5ffb44bdc6bb1d2181d746ec951dd30f89ed08/src/resources/publication.ts), [agent evolution constructor](https://github.com/dust-tt/srchd/blob/4b5ffb44bdc6bb1d2181d746ec951dd30f89ed08/src/tools/system_prompt_self_edit.ts).
- Adjacent first-party surfaces excluded from ownership: `x/anas/` benchmark runners and hidden-test validation, `examples` and `problems` experiment-specific data, external security-disclosure human review, public talk/demo, repository maintainer/release processes and any external solver/scoring authority. Benchmark evaluation does not automatically become a live system-wide S3*.
- First-party operating / deployment modes considered: Multiple independent agents in one experiment (`agent run all`), default four reviewers per publication (operator configurable including zero), research profile with computer-backed evidence checking, citation/solution reporting, optional models, and exported self-edit server requiring host composition. Note: ordinary `createServer()` and `DEFAULT_TOOLS` do **not** register self-edit.
- Recursion level: A research experiment and its distinct operational researcher agents; individual tool calls are operational actions, peer-review choices have specific inter-agent coordination/audit roles, and the human running a CLI is outside the autonomous closure unless a parent mode is independently demonstrated.
- Reviewed revision: `dust-tt/srchd@4b5ffb44bdc6bb1d2181d746ec951dd30f89ed08` (frozen source checkout).
- Observation date: 2026-11-10; pinned static source/docs inspection without running paid models/Kubernetes.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

The CLI creates multiple `Runner`s for experiment agents and advances each loop independently. Each `tick()` loads a problem/system prompt and stored message history, invokes a model, executes MCP tool calls and persists response/tool results and usage. Per-agent computer pods provide separate execution contexts where configured. The default tools include publications and solution reporting; publication submission chooses non-author reviewer agents, records requested reviews and gives reviewers access to the content and optional attached files. When all assigned reviewers grade, any rejection rejects the submission; otherwise it becomes published and its citations join the shared graph. [`srchd.ts`](https://github.com/dust-tt/srchd/blob/4b5ffb44bdc6bb1d2181d746ec951dd30f89ed08/src/srchd.ts), [`runner/index.ts`](https://github.com/dust-tt/srchd/blob/4b5ffb44bdc6bb1d2181d746ec951dd30f89ed08/src/runner/index.ts), [`publication.ts`](https://github.com/dust-tt/srchd/blob/4b5ffb44bdc6bb1d2181d746ec951dd30f89ed08/src/resources/publication.ts).

`SystemPromptSelfEditServer` can append/edit an agent's prompt through `AgentResource.evolve()`, persisting an evolution row; subsequent `Runner.tick()` reads `agent.toJSON().system`. However `src/tools/index.ts` has no matching `createServer` switch case and `src/tools/constants.ts` excludes this server from `DEFAULT_TOOLS` and `ALL_TOOLS`; nothing at the frozen source ref invokes its factory in the standard CLI. The S4 classification therefore reflects a specific first-party *constructor* requiring developer composition, not an already operating self-adaptive experiment. [`system_prompt_self_edit.ts`](https://github.com/dust-tt/srchd/blob/4b5ffb44bdc6bb1d2181d746ec951dd30f89ed08/src/tools/system_prompt_self_edit.ts), [`tools/index.ts`](https://github.com/dust-tt/srchd/blob/4b5ffb44bdc6bb1d2181d746ec951dd30f89ed08/src/tools/index.ts), [`resources/agent.ts`](https://github.com/dust-tt/srchd/blob/4b5ffb44bdc6bb1d2181d746ec951dd30f89ed08/src/resources/agent.ts).

## Operational model

Agents autonomously choose research actions, papers, reviews and reported solution beliefs. A system-level publication gate mediates what enters shared scientific knowledge, with independent peers deciding acceptance and returning their findings to authors. Application/CLI manages the number of agents, reviewers and experiment budgets mechanically, but it is not a discretionary whole-current S3 actor. Source-level S4 evolution is distinct from S5 legitimate control of enduring research mission/policy.

## S1 — Operations

- State: A
- Function: Conduct an individual research task by model-directed investigation, computer/web operations, publications and follow-up work.
- Disturbance / variety regulated: Hard/open-ended research goals, novel findings, failed hypotheses, tool outputs, reviewers' feedback and task continuation.
- Decisive decision or feedback right: Choose next research step/tool call, content of a submission, review response and reported solution belief.
- Decision owner: Each experiment agent's model in `Runner.tick()`; host fixes problem, profile and model/tool access.
- Supporting / enforcement mechanisms: Stored conversation, model invocation, MCP tool execution, per-agent pod, token usage, repeated ticks and publication/solution APIs.
- Closure path: Experiment goal → agent model reasoning/action → tool result and research evidence → message persistence → later model ticks and publication/research decisions.
- Boundary reachability: Default `agent run all` builds real runners for the experiment's agents and ticks them continuously; publication/goal tools are in `DEFAULT_TOOLS`, no separate benchmark harness is needed.
- Why this is / is not agent-owned: Agents exercise open-ended operational research judgment; infrastructure configures execution and stores artifacts but does not pick research claims or action sequences.
- Evidence: [`runner/index.ts` tick](https://github.com/dust-tt/srchd/blob/4b5ffb44bdc6bb1d2181d746ec951dd30f89ed08/src/runner/index.ts), [CLI agent run](https://github.com/dust-tt/srchd/blob/4b5ffb44bdc6bb1d2181d746ec951dd30f89ed08/src/srchd.ts), [research agent profile](https://github.com/dust-tt/srchd/blob/4b5ffb44bdc6bb1d2181d746ec951dd30f89ed08/agents/research/prompt.md).
- Basis: First-party reachable model/tool loop and research workflow.
- Confidence: High in architectural ownership; no outcome-quality claims from README benchmarks.
- Caveats: Requires configured LLM credentials and, for computer profiles, Kubernetes resources; no paid run performed here.

## S2 — Coordination

- State: A
- Function: Dampen competing/unreviewed research claims and organize reuse of findings across distinct researcher S1s through publication, peer decision and citations.
- Disturbance / variety regulated: Contradictory or low-quality results flooding a shared corpus, unfulfilled reviewer commitments and duplicated investigations without reliable shared references.
- Decisive decision or feedback right: Reviewer agents choose `ACCEPT`/`REJECT` grades and evidence-bearing comments; their verdicts decide whether a paper enters the shared published set and becomes citable/discoverable.
- Decision owner: Assigned peer reviewer models, not merely database routing; deterministic publication rule aggregates actual agent grades.
- Supporting / enforcement mechanisms: Non-author reviewer pool, assigned reviews, pending-review-before-submission gate, `submit_review`, unanimous non-rejection publication rule, citation graph and advisory/status feedback.
- Closure path: Researcher submits paper → other agent reviewers are assigned → their discretionary grades/comments → publication accepted/rejected → author receives status and other agents discover/cite the accepted corpus.
- Boundary reachability: `createPublicationsServer` is registered in `DEFAULT_TOOLS`, invoked by each `Runner`, and `PublicationResource` persists reviewer selection/grades/status; default CLI reviewer count is four with an explicit zero-reviewer exception.
- Why this is / is not agent-owned: Reviewer models decide paper acceptability; random assignment and status transition are deterministic infrastructure, but the inter-S1 attenuation judgment comes from peer agents.
- Distinct S1 units: Author researcher and distinct reviewer researchers inside the same experiment.
- Inter-S1 disturbance: Incompatible/unverified publications competing for shared recognition and follow-on research attention.
- Attenuating coordination relation: Reviewer assignments, evidence-bearing grades and shared publication status/citations regulate which claims can circulate as published work.
- Feedback into subsequent S1 behaviour: Acceptance/rejection and review content are persisted/exposed to author and peers, shaping later revisions, citations and solution reports.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: Peer grades alter the **admissibility of shared research contributions** and impose review work before new submissions, attenuating a defined multi-researcher disturbance; mere messages or parallel execution would not.
- Evidence: [`tools/publications.ts` submit/review gates](https://github.com/dust-tt/srchd/blob/4b5ffb44bdc6bb1d2181d746ec951dd30f89ed08/src/tools/publications.ts), [`resources/publication.ts` reviewer/grade/status](https://github.com/dust-tt/srchd/blob/4b5ffb44bdc6bb1d2181d746ec951dd30f89ed08/src/resources/publication.ts), [`runner/advisory.ts`](https://github.com/dust-tt/srchd/blob/4b5ffb44bdc6bb1d2181d746ec951dd30f89ed08/src/runner/advisory.ts).
- Basis: Source-wired multi-S1 publication/coordination loop.
- Confidence: Medium-high; effectiveness of scientific consensus not experimentally established.
- Caveats: If operator configures zero reviewers, papers publish directly and this peer S2 mode is absent. Advisory injection occurs only in certain tool-result branches; status/content remains queryable from DB tools.

## S3 — Inside-and-now control

- State: —
- Function: Would decide a whole experiment's current resources, cross-agent commitments, priorities or corrective intervention.
- Disturbance / variety regulated: Live multi-agent resource contention, blocked research lines, portfolio priority conflicts and aggregate delivery shortfalls.
- Decisive decision or feedback right: No source-backed autonomous or parent whole-current discretionary controller managing a collective commitment portfolio.
- Decision owner: CLI operator chooses agent counts, reviewer quota and max-cost/token caps; code independently ticks each agent and stops at thresholds.
- Supporting / enforcement mechanisms: Concurrent runner promises, experiment usage aggregates, UI status, publication status and best-solution reports.
- Closure path: Aggregate cost can stop process; agent-declared best solution is stored as a report, not a centralized decision reallocating work or committing whole-experiment capacity.
- Why this is / is not agent-owned: Publication peers control knowledge quality, not the ongoing organization-wide allocation of active research commitments; deterministic runner ceilings do not qualify.
- Evidence: [`src/srchd.ts` independent tick loops/ceilings](https://github.com/dust-tt/srchd/blob/4b5ffb44bdc6bb1d2181d746ec951dd30f89ed08/src/srchd.ts), [`resources/solutions.ts`](https://github.com/dust-tt/srchd/blob/4b5ffb44bdc6bb1d2181d746ec951dd30f89ed08/src/resources/solutions.ts), [`tools/goal_solution.ts`](https://github.com/dust-tt/srchd/blob/4b5ffb44bdc6bb1d2181d746ec951dd30f89ed08/src/tools/goal_solution.ts).
- Basis: Bounded absence.
- Confidence: Medium-high at experiment boundary.
- Caveats: A human operator can manually adjust a run, but there is no first-party closed parent S3 mode over system-wide decisions.

### Absence scope

- Surfaces inspected: Agent run CLI, separate runner loops, usage caps, experiment UI, publications, solution reports and resource schema.
- Plausible first-party paths checked: Whole-current commitment view, cross-S1 resource/prioritization judgment, intervention owner, durable assignment update and return into running agents.
- Why no material first-party path remains: Runtime runs independent agents and enforces configured caps; reviewer consensus and solution reports do not form an authority that manages the whole active research portfolio.

## S3* — Complementary audit

- State: A
- Function: Subject an author's claimed research result to separately assigned peers' step-by-step verification and allow their findings to change publication status.
- Disturbance / variety regulated: False proofs, incorrect observed outputs, unsound methods and unsupported publication claims missed by the producing researcher.
- Decisive decision or feedback right: Peer reviewer models make grade/critique judgments distinct from the author's self-report; a rejection prevents a claimed result from entering published research.
- Decision owner: Assigned other experiment agents, with individually stored reviews and a deterministic status aggregator.
- Supporting / enforcement mechanisms: Non-author reviewer selection, `get_publication` full content/reviews, optional attachment download into reviewer-owned computer, research profile's independent verification instructions, `submit_review` and `maybePublishOrReject`.
- Closure path: Author's paper/attached code → separately assigned reviewer reads it and can investigate/reproduce in own computer → independent grade and verification commentary → recorded review → acceptance/rejection returned to author and corpus.
- Boundary reachability: `research` is a shipped profile with `computer-process`; `createPublicationsServer` exposes `download_publication_attachments` in that mode, and its default review tools are wired through the standard runner. The reviewer is excluded from the author's own reviewer pool.
- Why this is / is not agent-owned: Reviewer models independently judge claims using publication details and optional direct artifact/computer access, not merely echo the author's reported success; deterministic aggregation enforces their verdict.
- Claim being audited: A submitted paper's mathematical, scientific or code-execution claims and cited evidence.
- Ordinary reporting path: Author's generated paper, rationale, attachments and output claims stored in publication record.
- Complementary access path: Another agent's read access to full publication and attachments plus its own sandbox/computer tools to check assertions, run code or examine artifacts; the profile requests stepwise verification logs.
- Independence boundary: Reviewer is a different agent ID, not the author; it has its own model context and optionally isolated computer pod. Shared experiment/problem and models do not guarantee epistemic success.
- Who acts on findings: `PublicationResource.maybePublishOrReject` applies the review grades and persists the status, which changes author feedback and shared discoverability.
- Evidence: [`tools/publications.ts` get/attachment/review](https://github.com/dust-tt/srchd/blob/4b5ffb44bdc6bb1d2181d746ec951dd30f89ed08/src/tools/publications.ts), [`resources/publication.ts` reviewer exclusion and verdict](https://github.com/dust-tt/srchd/blob/4b5ffb44bdc6bb1d2181d746ec951dd30f89ed08/src/resources/publication.ts), [research profile verification expectations](https://github.com/dust-tt/srchd/blob/4b5ffb44bdc6bb1d2181d746ec951dd30f89ed08/agents/research/prompt.md).
- Basis: Source-wired independent peer audit with an alternative artifact-inspection path in the standard research-computer mode.
- Confidence: Medium; code provides independence/reality access, not proof every actual review uses it rigorously.
- Caveats: Default peer review grade can be based only on paper text; the stronger complementary artifact path depends on configured computer profile and available attachments. A zero-reviewer mode has no S3* peer audit.

## S4 — Outside-and-then intelligence

- State: C
- Function: Permit an agent to incorporate newly learned strategies from outside research into a durable system-prompt capability for later work.
- Disturbance / variety regulated: Changing research knowledge, repeated failure modes and novel methods requiring future reusable adaptation rather than another immediate tool call.
- Decisive decision or feedback right: In a manually composed self-edit mode, the agent can choose `append`/`edit` of its future operating instructions; actual author/decision is model-based, while activation is an explicit host composition task.
- Decision owner: A model researcher when the first-party `createSystemPromptSelfEditServer` is mounted; the standard CLI does not mount it, so no unqualified S4=A claim.
- Supporting / enforcement mechanisms: Dedicated MCP prompt append/edit tools, `AgentResource.evolve()` append-only prompt evolution records, `toJSON().system` and `Runner.tick()` use of the current evolved prompt.
- Closure path: Agent investigates publications/failures → in a developer-composed future-learning mode chooses a durable prompt change → evolution row stored → subsequent runner tick sees amended instructions and changes future research actions.
- Boundary reachability: The first-party factory `createSystemPromptSelfEditServer(agent)` exposes explicit S4-specific write tools, while `Runner.initialize(experiment, agent, mcpClients, model)` accepts caller-composed MCP clients and reads the same evolving `AgentResource`. This is a constructor route; `createServer()`/`DEFAULT_TOOLS` omissions prevent treating it as an activated default.
- Why this is / is not agent-owned: The configured agent may propose/execute future reusable capability edits; the shipped system supplies a specific persistent tool-to-next-tick path, but host activation prevents direct autonomous `A` classification.
- External distinction: Cross-agent publications, new discovered research methods, tool/computer results and external web evidence that can motivate a future strategy change.
- Future / prospective distinction: The edited system prompt is used by later ticks, beyond the current question/answer.
- Adaptation option generated: Revised persistent research strategy/instruction text authored by the agent.
- Path back into current capability / S3: `evolve` stores a new revision and the next `Runner.tick` uses `agent.toJSON().system`; no S3 allocation layer is required for this local capability change.
- Evidence: [`system_prompt_self_edit.ts` constructor](https://github.com/dust-tt/srchd/blob/4b5ffb44bdc6bb1d2181d746ec951dd30f89ed08/src/tools/system_prompt_self_edit.ts), [`resources/agent.ts` evolution](https://github.com/dust-tt/srchd/blob/4b5ffb44bdc6bb1d2181d746ec951dd30f89ed08/src/resources/agent.ts), [`runner/index.ts` prompt read](https://github.com/dust-tt/srchd/blob/4b5ffb44bdc6bb1d2181d746ec951dd30f89ed08/src/runner/index.ts), [`tools/index.ts` missing default binding](https://github.com/dust-tt/srchd/blob/4b5ffb44bdc6bb1d2181d746ec951dd30f89ed08/src/tools/index.ts).
- Basis: Function-specific first-party constructor with explicit missing ordinary-run activation.
- Confidence: Medium for C; not evidence of an executed self-improvement cycle.
- Caveats: Neither README claims nor the existing unused source file establish live S4 in `agent run all`. Concrete selection quality and long-term benefit remain untested.

## S5 — Policy and identity

- State: —
- Function: Would decide legitimate ultimate mission/identity disputes and return authoritative constitutional policy into the research organization.
- Disturbance / variety regulated: Conflict about the experiment's enduring purpose, constitutional authority, permissible research and who may revise it.
- Decisive decision or feedback right: No first-party legitimacy/adjudication owner over experiment identity. Even an optionally composed prompt self-edit is local instruction change, not an authoritative constitutional decision.
- Decision owner: Human operator selects experiment problem/profiles/tool and resource configuration; no closed ultimate-policy parent process is installed.
- Supporting / enforcement mechanisms: Initial experiment goal and system profile, limited prompt evolution constructor, CLI options, database schema and sandbox policy.
- Closure path: A caller can create a new problem or update a profile; no named identity dispute goes to a legitimate parent/agent authority and returns a binding policy revision to all researchers.
- Why this is / is not agent-owned: Researchers act within an externally chosen goal, and editing a personal prompt does not grant the right to redefine the legitimate mission of the whole experiment.
- Evidence: [`Runner.tick` goal framing](https://github.com/dust-tt/srchd/blob/4b5ffb44bdc6bb1d2181d746ec951dd30f89ed08/src/runner/index.ts), [`src/srchd.ts` setup](https://github.com/dust-tt/srchd/blob/4b5ffb44bdc6bb1d2181d746ec951dd30f89ed08/src/srchd.ts), [`system_prompt_self_edit.ts` local scope](https://github.com/dust-tt/srchd/blob/4b5ffb44bdc6bb1d2181d746ec951dd30f89ed08/src/tools/system_prompt_self_edit.ts).
- Basis: Bounded absence.
- Confidence: Medium-high.
- Caveats: Operators or maintainers may govern their institutions externally; repository governance is not a first-party experiment S5 return path.

### Absence scope

- Surfaces inspected: Experiment creation/goal, profile config, operator CLI, prompt self-edit constructor, publication review, solution reports and resource permissions.
- Plausible first-party paths checked: Collective identity issue, legitimate ultimate authority, binding decision, durable policy update and return into later agent work.
- Why no material first-party path remains: Shipped decisions concern research papers, task operations and an optional individual's prompt, not authoritative experiment-level identity/policy adjudication.

## Distributed OSS parent arrangement

Upstream developers maintain srchd source and example experiments. The installed experiment consists of operators plus researchers whose persistent publications/reviews exist in one database; that does not make upstream GitHub maintainers an operational parent. The CLI operator's setup and budget stop are not a proven S3/S4/S5 parent cycle.

## Self-hosted and non-human modes

Self-hosted Node/SQLite plus optional Kubernetes pods supports independent nonhuman researchers and peer-review/audit loops, using configured providers. Reviewer count zero disables peer checks; ordinary positive S2/S3* claims refer to the documented default multi-reviewer research mode. Self-edit source exists only as a manually composed constructor, not the default self-improvement advertised in README.

## Recursion

Individual researchers are S1 units. Publication review regulates shared research claims (S2) and independently verifies submitted evidence (S3*) within the experiment; the two functions share events but have distinct disturbance/decision tests. The experiment has no evidenced whole-current S3 or constitutional S5. The optional single-agent future-instruction constructor is local S4 C rather than an experiment-wide autonomous strategy office.

## Variety and escalation

Research variety is propagated via persistent agent/tool turns. Review assignments, grades and citation visibility attenuate conflicting scientific contributions; independent reviewers can access direct artifacts in their own computers and return a verdict. Human experiment limits can stop resource use, but lack discretionary whole-control feedback. Evolution source permits persistent agent capability change only if manually wired; unreviewed claims of automatic self-evolution are excluded.

## Evidence gaps

- No live provider/Kubernetes exercise, independent review of scientific correctness or empirical evaluation of consensus outcomes.
- `Advisory.pop` is processed only on a tool-result branch; publication status and reviews remain retrievable in DB, but immediate notification delivery is conditional.
- The self-edit constructor is exported and structurally coherent but not registered by `createServer` or `DEFAULT_TOOLS`; do not claim regular CLI S4=A until source wiring or a supported composed execution is independently demonstrated.
- An operator-selected zero-reviewer mode bypasses peer validation, and reviewed research might have no independently executable artifacts; positive audit is limited to the supported research-computer path.

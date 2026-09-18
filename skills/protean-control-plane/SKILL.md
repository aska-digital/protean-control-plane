---
name: protean-control-plane
description: "Use for any dispatch, rotation, concurrency, GitHub workflow, or learning decision. Compact trigger index; load only the bundle the task names."
version: 1.5.0
author: the Protean publication
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Orchestration, Dispatch, Rotation, Concurrency, Gates, SOP]
    related_skills: [protean-operating-doctrine, draft-review-html, github-pr-audit, github-issues, external-writing-discipline]
---

# Control plane - the one canonical procedure home

Two entry points lead into the same system. A cross-project **relay** role
coordinates several coordinator instances across projects and sessions. An
in-project **coordinator** orchestrates the specialist roles inside one project or
session. The coordinator never bypasses the QA gate and the final review. The
relay never performs in-project specialist work and never silently merges
conflicts.

This is the procedure half of the control plane (the law). The state half (the
records) is append-only under `records/` in the installed kit, or under
`$PROTEAN_RECORDS_ROOT` when one is set: `ROTATION-STATE.md`, `INFLIGHT.md`,
`LEARNINGS.md`, `DISPATCH-LEDGER.md`, `OWNERSHIP-MATRIX.md`,
`CONTRIB-STATE.md`. Ownership: the
coordinator owns this skill and the records, QA owns gate verdicts and may not
author the fixes it reviews, build maintains the gates.

This skill is the record. It cites other procedures by their public slug and the
record gates by their ingredient-relative path; it ships no architecture document
of its own.

## A. Trigger index (first screen - route here, nowhere else)

**Load the minimum bundle; do not load all skills.** These entries are triggers;
the named skills are the procedures they activate. A trigger never duplicates
procedure text.

| intent (what was asked) | minimum skill bundle | roles involved | mandatory gates |
|---|---|---|---|
| GitHub notification triage - "address my last N GitHub notifications" | the authenticated GitHub read path; `github-issues` or the code-review procedure as applicable; `github-pr-audit` for any review or merge decision; `external-writing-discipline` for human-facing text; `draft-review-html` for every draft intended for operator review | research writes, build implements, QA audits, the coordinator integrates | no posting or merge without explicit approval plus post-action read-back; the prose gate; the draft pipeline gates |
| GitHub pull request or issue draft | `draft-review-html` - one command `scripts/protean-drafts/draft_pipeline.py`, start from the shipped templates, `--owners <poster-handle>` for external repositories, omit `--owners` for internal drafts | one role authors, a second audits (an author never audits their own writing) | quote-integrity (slice, never retype), prose gate, the pipeline's own gate list |
| GitHub merge or review decision | `github-pr-audit` - live-head audit, repository tests, evidence-register check, formal review protocol, merge method from history | QA audits, the coordinator integrates | post-action read-back of the exact head and body; no merge without approval |
| New external source, repository, or URL ingestion | the knowledge-ingestion procedure; a batch of five or more sources uses the batch form; a capability audit precedes adopting any external tool | research ingests; the external knowledge base is the home for external data | external data goes to the knowledge base only; internal procedure goes to a skill; one fact, one home |
| Any multi-agent project | `protean-operating-doctrine` plus the platform's own launch and supervision mechanics; just-in-time file handoff per section B | the coordinator dispatches, QA gates, the coordinator gives final review | launch through the platform's own profile mechanism, never a cross-profile delegation call; the model receipt; the rotation, inflight, and learnings gates |
| Major decision (any change to a canonical home, layer model, gate, dispatch rule, public surface, credential or model policy, or anything irreversible without a user action) | this row plus the decision's own bundle | design renders the report, the coordinator approves | the decision report must exist and be linked before the change lands |
| Continual contribution mode - idle-time work on a repository we own or depend on, delivered as a pull request, an issue, or a pull-request review | this skill's section G (the rule), the contribution-state record and its gate (the value), the GitHub workflow pack's contribution procedure (the mechanics), and the draft pipeline for anything a human approves | build implements, QA audits every contribution, the coordinator integrates | an evidenced gap plus a duplicate search before anything is drafted; the contribution-state gate green with the intended target and action class; an independent QA verdict on every contribution; exact-byte approval before any external write |
| Contribution entry state - is this contribution a draft or a ready pull request | this skill's section G (the rule and the entry state) and `protean-github-flow` (the state semantics, the CLI and API forms, and the transition rules) | build implements and opens, QA audits the exact live head, the coordinator integrates | draft at entry for anything large or high-attention; ready only for a small fix in a repository we administer and only after the independent pre-post verdict; the ready transition is a separate approved step with its own head read-back |
| A structured team council - convene a bounded deliberation with a written decision record | the council procedure (`skills/protean-control-plane/references/council.md`) and its templates | the facilitator plus research and QA at minimum; the other seats as the bounded question names | exactly one bounded question fixed in the convening brief; every factual claim carries a source and dissents are recorded, never averaged away; owner-held gates restated verbatim in the decision record; no canonical edits while a ruling is open; outputs enter the relay's live-state record (section J) and the ops records (section B) |

## B. Mandatory preflight (before the first write of any dispatch)

1. Read the rotation state, inflight leases, and ownership matrix records.
2. Declare in the brief: role, allowed decisions, forbidden decisions, owned
   files, upstream stable handoff, and exit evidence. A dispatch without this
   receipt is invalid.
3. Acquire and verify an inflight claim covering the exact file set before the
   first write, and record the conflict check taken immediately before each
   write.
4. Read the target role's own configuration immediately before dispatching it,
   never a remembered model.
5. Record the provider and model in the ledger row, and verify them afterwards
   against the target's own usage record. Configuration, ledger, and usage must
   agree, or the row becomes an unresolved decision.
6. Prefer a different capable worker from the previous one; never interrupt a
   healthy worker.
7. Never prewrite a launch session id: write the ledger row with the session id
   pending, then fill the id captured from the worker's own output log. A row
   whose launch id was not captured from its output log is invalid.

## C. Automatic GitHub workflow

1. Triage notifications into: pull request review, issue response, merge or
   release, reference-only.
2. Pull live state first: repository, head SHA, body. Never trust a pasted
   snapshot.
3. If text will be shown to a human before posting, produce the HTML artifact
   with the draft pipeline. Never hand-render and never paste raw markdown as the
   review copy.
4. External drafts pass `--owners <poster-handle>`. Internal drafts omit it and
   use the renderer's neutral chain. Never put internal role names on an external
   post.
5. The pipeline's gates run in one pass and must all pass: prose, identifier
   sweep, verbatim-quote integrity, oversight blockquote, render fidelity,
   palette, self-containment, chrome, change banner.
6. A second-member proofread plus fact audit is mandatory. The author never
   audits their own writing. QA is the independent gate; the coordinator gives
   the final integration review.
7. No external side effect without explicit user approval, unless that action
   was authorized in advance. After every external write, read back the exact
   target, head, and body, and diff against the approved draft.

## D. Firm failure policy

- A gate failure blocks advancement. Gates are never silently skipped.
- A stale or ambiguous claim becomes unverified, not evidence. Read-back
  outranks any self-report.
- A model or provider mismatch between the ledger, the configuration, and the
  usage record becomes an unresolved decision. Never silently substitute a
  model; rotate only within the role's configured set.
- A stale, expired, or crashed inflight claim blocks overlapping writes on its
  paths until it is classified. Do not route around the flag.
- If no relevant skill exists for a recurring task, record one skill-gap
  learning in the learnings record: one canonical home, one enforcement surface,
  one independent verifier.
- Recovery from a dead or stalled worker: one steer or one bounded restart with
  the same launch invocation and backoff, then escalate to the coordinator. Never
  loop.

## E. Minimal-context rule

First load, and only first load: this trigger index, then the exact role module,
then the selected procedure skills, then the direct evidence files for the task.
A handoff carries references and decisions, never copied payload. Durable facts,
project history, and long procedure text never enter an identity or memory hot
path.

## F. Flywheel rule

Every material failure becomes exactly one bounded learning row in the learnings
record: incident, root cause, one rule, one canonical home, one enforcement
surface, one independent verifier. A rule without an enforcement command is a
preference, not a law, and the learnings gate rejects it.

## G. Contribution mode

Two modes, one flag, one home. The rule is here. The value is a record the
`protean-ops` ingredient owns and its gate reads, and the bounded numbers stay
there too: this section states the law, not the counters.

- **Internal mode is always on.** Contribution work against a repository the
  operator administers needs no toggle and no per-action approval. It is gated by
  evidence, the lane cap, the independent QA gate, and the repository's own
  continuous integration, and by nothing else.
- **External mode is off by default.** Contribution work whose target is not such
  a repository is off unless the operator turns on one flag. Off means no remote
  write of any kind, including a push to a fork. A local branch, a commit, a test
  run, and a rendered draft stay allowed, and the unpushed branch is the
  deliverable.
- **One flag, fail closed.** The kill switch is the single header field
  `external_contrib: on|off` in the contribution-state record. An absent record, an
  unreadable record, or a value outside `{on, off}` all read as `off`.

Law that holds whatever the toggle says:

- Every contribution carries an evidenced gap and a duplicate search before
  anything is drafted. A candidate that cannot show both does not ship.
- The always-on half is asserted, never assumed: the gate refuses the internal
  toggle being off unless the record cites the decision that recorded it.
- Lanes are bounded. The lane cap, the rate windows, the quiet-hours window, the
  per-thread write limit, the per-repository burst detector, and the grant rules
  are recomputed by the gate from timestamped rows, never from memory, and a
  process-local counter is not admissible evidence.
- Backlog governors and thread attention are live reads, not stored counters. A
  lane reads the target repository's own numbers at post time and records the raw
  output with the contribution.
- No pings, no content-free writes, and no attention manufactured to justify a
  write. A comment carries a new fact or it is not posted.
- A high-traffic thread takes no unsolicited write. The permitted forms are an
  update to our own live item carrying a new fact, an invited review, an
  operator-approved contribution, or a bounded grant that names the thread.
- Every contribution, internal or external, pull request or issue or review,
  passes the independent QA gate before it is posted, pushed, or merged. The
  author never audits their own work.
- Approval binds to exact bytes: a draft is hashed at approval and recomputed at
  post time, and a mismatch returns for re-approval instead of posting.
- A contribution lane is bounded to one gap and one action, and it terminates
  with a receipt. A second gap it finds is recorded, never worked in-run.

**Entry state: draft or ready.** A contribution's first platform decision is the
state it opens in, and one rule covers it. A large or high-attention contribution
is a draft at entry and is never opened ready. A small fix in a repository we
administer may open ready, and only after the independent pre-post verdict has
passed. On a target we do not administer the entry state is a local draft while
remote writes are off, then a GitHub draft once the exact bytes are approved, and
the ready transition is a separate step covered by its own approval or grant. The
platform procedure, the exact state semantics, and the transition rules are the
GitHub workflow pack's; this section states the law and points there.

Read live, never assume: whether checks or Actions run on a draft, and how draft
state interacts with branch protection, rulesets, required checks, or merge
queues. The documentation that defines the draft rules states neither, so no lane
may claim either. A ready state is not an approval and not a green check, and a
draft cannot be merged.

**Preflight addition.** Before the first remote write of a dispatch, read the
contribution-state record and record its value, its file md5, and the UTC read
time in the lane receipt, then run the contribution-state gate with the intended
target and action class. Run it again immediately before the write. A value read
earlier in the lane is not authority.

**Idle trigger.** The mode is entered from a machine-checked idle predicate: the
running lane set is empty, no waiting item is unblocked, and no live claim is
open. Exactly one evaluator per project evaluates it, claims the epoch before
dispatching, and then dispatches immediately, with no operator question, because
internal mode is always on and the external gate is what holds a draft back. A
contribution lane never dispatches a lane, never evaluates the predicate, and
never acts on a finding inside its own run.

## H. End-of-turn worker-completion check

The idle trigger is a rule about state; this section is the rule about *turns*. It binds the
project's single idle evaluator. On every worker-completion turn and on the first
return-from-absence turn, the evaluator runs this checklist *before it replies*. A completion
notification is a trigger to evaluate, never proof that work is done.

1. **Snapshot.** Read the project's task-home record and the ops inflight and rotation records.
2. **Classify by poll, never by notification.** A lane row is live only while its process handle
   appears in the process-registry listing (a read-only poll of a specific handle is admissible;
   it does not consume the completion event). A row is closed only when the handle is absent and
   the lane directory's receipt ends, on its last non-empty line, in a terminal marker
   (`STABLE`, `CLOSED`, `PASS`, or `COMPLETE`); a receipt whose last non-empty line is anything
   else is not terminal. A handle absent for two consecutive classification rounds with no receipt
   is stale, not running, and must not flip status on transient registry noise.
3. **One closure pass, bounded.** Move bookkeeping-complete rows to closed with the UTC closure
   time and the receipt path. If the pass changed the file, re-read it once and re-count. At most
   one closure pass per evaluation; a second pass is a loop.
4. **Three-way decision, exactly one branch, before the reply.**
   - **(a) A lane is live or its terminality is unknown** — stop dispatching, continue the live
     lane, and report from the poll evidence.
   - **(b) An owner-waiting item is unblocked** — its blocking artifact exists, readable and
     non-empty, or its blocking decision is recorded — dispatch that work immediately, before any
     contribution work.
   - **(c) Otherwise** — claim the idle epoch, then dispatch contribution work per section G, in
     the same turn, with no waiting and no internal asking.
5. **Budget exit is explicit, never silence.** A row whose handle is absent and whose lane
   directory holds no receipt (or does not exist) is a budget exit: never treat it as still
   running and never treat it as done. Handle it before any contribution dispatch — relaunch that
   lane if it is relaunchable, highest priority first, otherwise dispatch the next owner task.
   Ending a completion turn with a bare reply or with silence is a procedural violation by
   definition.
6. **Anti-storm guard.** Before dispatching, append the epoch claim keyed by the idle fingerprint
   and read it back. At most one new lane per idle epoch; exactly one evaluator per project — a
   second evaluator that finds a live epoch claim on the same fingerprint exits as a lost race
   without dispatching.
7. **Evidence.** The reply cites the classification actually performed: the registry poll, the
   per-lane statuses, any rows closed, the branch taken, and the epoch claim read-back. A reply
   with no poll and no predicate result cannot be verified and does not close the turn.

## J. Relay live state (seat, events, handoff)

The relay role's live state lives in one canonical append-only state home, owned
by the relay. Concurrent relay sessions coordinate through it: readers are free,
exactly one writer holds the seat. The rule is here; the tool, its file contract,
and its invariants own the numbers.

- A relay session never hand-edits a shared status file as the source of truth.
  It claims the seat through the state CLI, writes events through the CLI, and
  reads the compact projection at session start - never an old transcript.
- Concurrent sessions: readers are free; exactly one seat holder writes. A stale
  seat is claimable with the takeover recorded; forcing a live seat is an
  explicit steal and is recorded. A revision conflict exits with a distinct
  code - reconcile and retry, never force.
- The overview reads the compact projection first, falling back to the legacy
  task-home file only while the migration window is open.
- Everything belongs in the state record except what is deliberately excluded:
  credentials, tokens, transcripts, logs, caches, and scratch never enter the
  state, the events, the projections, or a handoff bundle. The state is
  single-machine scope; filesystem permissions and backups are part of the
  contract.
- The full operator guide - commands, exit codes, seat semantics, TTL and
  recovery, verification and rollback - is published separately as its own
  canonical document; this section restates no bounded value.

## Gate commands

The record gates belong to the `protean-ops` ingredient and are cited here, never
copied. This skill declares `requires` on that ingredient for exactly this
reason.

| gate | command |
|---|---|
| rotation | `python3 scripts/protean-ops/check-rotation.py` |
| inflight | `python3 scripts/protean-ops/check-inflight.py` |
| learnings | `python3 scripts/protean-ops/check-learnings.py` |
| decision report | `python3 scripts/protean-ops/check-decision-report.py <report.html> [--manifest M] [--evidence E]` |
| hot-path freeze | `python3 scripts/protean-ops/check-hotpath-freeze.py <manifest> [--allow-change <receipt>]` |
| contribution state | `python3 scripts/protean-ops/check-contrib-state.py <records>/CONTRIB-STATE.md [--target internal\|external --repo <owner/name> --action pr\|issue\|comment\|review\|merge]` |

Record resolution defaults to `./records` and can be redirected with
`$PROTEAN_RECORDS_ROOT`. The wrapper at
`gates/protean-control-plane/check-control-plane-gates.py` runs these gates when
the ops ingredient is installed beside this one, and reports each of them as
`unavailable` without failing when it is not: a control plane installed alone is
installed in degraded mode, and it says so.

All gate scripts are read-only, stdlib-only, `--help`-able, and fixture-tested.

## Limits

- The wrapper reports cited gates as `unavailable` in degraded mode. It does not
  invent a substitute check, and it does not fail for a missing dependency it was
  installed without.
- This skill states the procedure. The platform mechanics for launching a worker
  on a given surface, and the supervision and recovery steps, are owned by that
  surface and are deliberately not restated here: a citation to a document that
  does not ship would be a dangling reference.

---
name: protean-control-plane
description: "Use for any dispatch, rotation, concurrency, GitHub workflow, or learning decision. Compact trigger index; load only the bundle the task names."
version: 1.0.0
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
`LEARNINGS.md`, `DISPATCH-LEDGER.md`, `OWNERSHIP-MATRIX.md`. Ownership: the
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

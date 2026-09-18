# Council procedure — structured meeting and decision system (v1.0.0)

One canonical procedure for convening a bounded, evidence-led team council and
recording what it decides. The control-plane trigger index (section A, row "A
structured team council") routes here; the templates beside this file own the
formats. The council advises and records - it never bypasses owner gates, QA
verdicts, external-write approval, or production promotion.

Provenance: distilled from a piloted brainstorm-and-execute council pair
(convening session plus a bounded execution pass) and versioned from that
experience.

## 1. Purpose and when to convene

A council is a bounded deliberation with a written decision record. Convene one
when ALL of these hold:

- The question is strategic or cross-domain, not one specialist's bounded task.
- The operator asked for team judgment, sequence, or priority - not just execution.
- The answer changes what several lanes do next (an ordering or dependency effect).

Do not convene a council for a task one seat already owns, for an emergency
(steer the live lane through the platform's own adjustment channel instead), or
for a decision the operator has already made (record it; do not re-litigate).

## 2. Roles

| seat | duty |
|---|---|
| facilitator (the coordinator, or the relay across projects) | owns the bounded question, dispatches seats, merges outputs, writes the decision record; never overrules evidence by authority |
| research | inventories current state from live sources; flags stale assumptions and contradictions |
| analysis | sequences, dependencies, tradeoffs, kill conditions |
| design | surface and UX implications; renders the decision report where the decision-report gate requires one |
| build | feasibility and cost of each recommendation; no implementation during deliberation |
| QA | verifies evidence claims and audits the record; the auditor never authors the recommendation it verifies |

A seat with nothing to add on the bounded question is skipped, and the agenda
records why. Minimum viable council: facilitator + research + QA.

## 3. Agenda and the bounded question

The facilitator dispatches a convening brief (template `council-brief.md`) that
fixes exactly one bounded question, in quotes, plus the context each seat needs.
No seat may expand scope. Context rules:

- Current state is stated as verifiable facts with sources; stale or contested
  items are labeled as such, never presented as ground truth.
- Items explicitly out of scope (closed blockers, settled decisions) are listed
  so the council does not tunnel on or re-open them.
- Output-form constraints (separate horizons; a bounded action list; at least
  one option outside the current queue) are stated in the brief so the seat
  outputs are comparable.

## 4. Evidence and dissent capture

- Every factual claim in a seat's output carries its source (a live read, a
  file, an artifact). An unverifiable claim is marked `unverified`, never
  silently normalized.
- Disagreement is captured as a named dissent in the evidence register
  (`evidence-register.md`): who dissents, against which claim, on what evidence.
  A dissent is never averaged away; it either resolves on evidence or becomes
  an explicit open item or operator question.
- The facilitator may not drop a dissent from the record.

## 5. Decision record, recommendations, operator-held gates

The deliberation's output is a decision record (`decision-record.md`) with:

- the bounded question verbatim;
- the recommendation set - for a brainstorm council a small bounded action
  list (the pilot used five), each action carrying an owner lane, an
  acceptance signal, and a stop condition;
- the explicit split between what the team executes autonomously and what
  waits on an operator decision (promotion of a staging surface to production,
  canonical naming or voice, external posts, irreversible changes);
- dissents and open items, verbatim-sourced;
- a model receipt recording which configuration served which seat.

Operator-held gates are restated verbatim in the record. A recommendation that
crosses one is marked `GATED: <gate>` and cannot be executed by the council.

## 6. Execution handoff

Execution runs through the normal pipeline - the doctrine stages, inflight
claims, rotation - never as free-form follow-ups:

1. The facilitator opens an execution brief per recommendation cluster, citing
   the decision record path and the exact recommendation text.
2. Each cluster produces its receipt in the execution lane directory, ending in
   a fixed terminal line (`COUNCIL EXECUTION COMPLETE <path>` or
   `BLOCKED <reason>`).
3. Read-back discipline: every seat receipt is read back on disk with its
   terminal marker before the integrator reports completion, and the integrator
   re-runs checkable tools itself rather than trusting the receipt.

## 7. Action and receipt tracking

- Each accepted action gets one tracked row: action id, owner lane, decision
  record reference, receipt path, terminal marker, read-back date
  (`follow-up-action.md`).
- The tracking rows live in the execution lane's journal and the ops records;
  they reference lanes, they do not lease files - the inflight record stays the
  only lease authority.
- A follow-up either cites the receipt that authorized it, or it is a new
  decision.

## 8. No silent canonical edits while rulings are unresolved

While a council ruling on a canonical surface (public copy, naming or voice, a
canonical home, promotion) is OPEN, no lane edits that surface - not even an
obviously correct fix. The procedure is: present the bounded decision pack, the
operator picks, and only then does a lane edit canonical bytes. Emergency
repairs go through the operator, not around the ruling.

## 9. How council outputs enter the shared records

- The decision record path and terminal markers are appended to the relay's
  live state through the state CLI (section J), by the seat holder - never by
  hand-editing state files.
- Dispatch preflight, claim, and release rows follow section B in the ops
  records.
- A material failure the council surfaces becomes exactly one bounded learning
  row (section F).
- The council writes records and pointers only; it never writes an identity or
  memory hot path.

## 10. Limits

The council advises and records. It does not:

- bypass operator gates - promotion, canonical naming, external writes (section 5);
- substitute for QA - every executed cluster still gets an independent QA
  verdict (section 6);
- approve external posts - those need the operator's exact-byte approval and
  the contribution gate (section G);
- perform production promotion - that is always an operator action;
- override a live lane - running workers are steered through the platform's own
  adjustment channel, not by council vote.

A council recommendation without a decision-record path and a receipt is a
preference, not an outcome.

## Templates

Beside this file, in `council-templates/`: `council-brief.md`, `agenda.md`,
`decision-record.md`, `evidence-register.md`, `execution-receipt.md`,
`follow-up-action.md`.

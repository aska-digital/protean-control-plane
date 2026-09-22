# Changelog

All notable changes to this repository are recorded here. The format is a short
entry per release: what changed, why, and how it was verified.

## 1.6.0

- **What:** section J (*Relay live state*) restated for the git-substrate
  multi-writer store: readers are free, every session stages writes on its
  own proposal branch, and exactly one merge-seat holder merges to the main
  line (gate, then merge, then regenerate the projection). Same-record
  conflicts are refused before any merge attempt with a distinct exit code.
  The law stays generic — no backend token, no bounded value copied. The
  skill frontmatter, the ingredient descriptor, the installer banner, and
  this changelog bumped in the same change.
- **Why:** the 1.5.0 law ("exactly one writer holds the seat") describes the
  retired single-writer model; after the cutover it would read as current
  while being false. A stale law is worse than no law.
- **How verified:** internal-names and control-plane gates run clean on the
  changed tree; the installer dry-run writes the same three-ingredient plan;
  link check over the changed markdown is clean; no unresolved item added.
- **License:** MIT. The committed `LICENSE` file is authoritative.

## 1.5.0

- **What:** (a) one trigger-index row routing "a structured team council" to a new
  shipped council procedure (`references/council.md` + six templates in
  `references/council-templates/`); (b) a new section J, *Relay live state*, stating
  the live-state law for concurrent relay sessions (one canonical state home, one
  writer seat, CLI-written events, handoff without transcript import), stated as law
  with the tool's own document owning the numbers; (c) the skill frontmatter, the
  ingredient descriptor, the installer banner, and this changelog bumped in the same
  change (the installer-banner drift lesson from 1.3.0 applied).
- **Why:** the council system was piloted but had no published procedure, so a
  convening brief, its bounded question format, evidence and dissent capture, and the
  execution handoff were undefined; and the live-state section existed in the internal
  procedure but not in this projection, leaving concurrent relay sessions without a
  public statement of the seat and handoff rules.
- **Division of the feature:** the council procedure and its templates ship here and
  are cited from the trigger index; the relay live-state section states the law only -
  the operator guide, commands, exit codes, and invariants are published separately as
  their own canonical document and are cited, not copied. Section J adds no gate and
  no bounded value.
- **How verified:** internal-names and control-plane gates run clean on the changed
  tree; the installer dry-run writes the same three-ingredient plan; link check over
  the changed markdown is clean; no unresolved item added.
- **License:** MIT. The committed `LICENSE` file is authoritative.

## 1.3.0

- **What:** add one trigger-index row and an entry-state paragraph to section G, *Contribution
  mode*. The row routes the draft-versus-ready decision to this skill's section G and the
  `protean-github-flow` ingredient, which owns the platform procedure and the state semantics. The
  paragraph states the law: a large or high-attention contribution is a draft at entry and is never
  opened ready; a small fix in a repository we administer may open ready only after the independent
  pre-post verdict; on a target we do not administer the entry state is a local draft, then a GitHub
  draft once the exact bytes are approved, with the ready transition a separate approved step. It
  also names the two things to read live rather than assume: whether checks or Actions run on a
  draft, and how draft state interacts with branch protection, rulesets, required checks, or merge
  queues.
- **Why:** the control plane routed contribution work but had no row for the state a contribution
  opens in, so the entry state was unaddressed at the point where the lane is defined. A draft that
  can be read as a review request, or a ready pull request that can be read as a verdict, is a
  procedure gap with a real cost.
- **Division of the feature:** the law is stated here because the permission to write is what a lane
  needs first. The draft and ready semantics, the CLI and API forms, and the transition rules stay
  with the `protean-github-flow` ingredient, and the lane composition stays with the doctrine. This
  change adds no gate, no counter, and no bounded value.
- **How verified:** internal-names and control-plane gates run clean on the changed tree; skill
  frontmatter version, the ingredient descriptor, the installer banner, and this changelog bumped
  in the same change (the installer banner had drifted at 1.2.0).
- **License:** MIT. The committed `LICENSE` file is authoritative.

## 1.2.0

- **What:** add section H, *End-of-turn worker-completion check*, to the control-plane skill.
  Section G states the idle predicate as a rule about state; section H binds it to conversation
  turns: on every worker-completion turn and the first return-from-absence turn, the project's
  single evaluator runs a bounded checklist before it replies — snapshot, classify by process
  registry poll (a completion notification is a trigger, never proof of done; a receipt is
  terminal only when its last non-empty line is a terminal marker), one closure pass, then
  exactly one of continue-live-lane, dispatch-unblocked-owner-work, or claim-epoch-and-dispatch-
  contribution. A budget-exited lane (dead handle, no receipt, missing lane directory) must be
  handled in the same turn by relaunch or next owner task, never by silence. One closure pass and
  one new lane per claimed epoch bound the response against dispatch storms.
- **Why:** an observed production incident: two workers finished, the orchestrator received both
  completion notifications, polled, replied briefly, and dispatched nothing — and stayed idle until
  the operator asked. Every element of the idle predicate existed in the procedure, but no rule
  attached it to the completion turn, so the turn ended lawfully with zero dispatch actions.
- **How verified:** internal-names and control-plane gates run clean on the changed tree; skill
  frontmatter version, the ingredient descriptor, and this changelog bumped in the same change.

## 1.1.0

- **What:** add section G, *Contribution mode*, to the control-plane skill, one row to the
  trigger index, and one row to the gate table. Section G states the law for continual
  contribution: internal mode is always on and needs no toggle, external mode is off by
  default behind one flag, an absent or unreadable state record reads as off, and every
  contribution carries an evidenced gap, a duplicate search, an independent QA verdict, and
  exact-byte approval before any external write. It also carries the preflight addition (read
  the state record, record its value and md5, run the gate before the write and again at the
  write) and the idle-trigger rule (one evaluator per project, a machine-checked predicate, a
  claimed epoch, immediate dispatch). The gate table gains the contribution-state gate G-14,
  and the wrapper that runs the cited ops gates now covers it.
- **Why:** contribution work against repositories we do not administer is an external side
  effect, and the control plane's own rule is that no external side effect happens without
  explicit approval. A procedure for continual contribution without a stated default, a
  kill switch, and an enforcement command would be a preference, not law.
- **Division of the feature:** the rule lives here because a permission must be readable
  before any state exists; the value, the counters, and the bounded numbers stay in the
  contribution-state record of the `protean-ops` ingredient, which ships the schema, the
  gate, and the fixtures. One fact, one home: this skill cites the gate by its
  ingredient-relative path and restates no value.
- **Verification:** `python3 gates/protean-control-plane/check-internal-names.py .`,
  `python3 gates/protean-control-plane/check-control-plane-gates.py`, and
  `python3 -m unittest discover -s tests` pass from a clean checkout of this commit; the
  wrapper test asserts six available gates when the ops ingredient is present.
- **License:** MIT. The committed `LICENSE` file is authoritative.

## 1.0.0

- **What:** the first release of the `protean-control-plane` ingredient: the capability payload,
  the machine descriptor `protean-ingredient.json`, the standalone installer
  `install.sh`, the declared gates under `gates/protean-control-plane/`, and the test suite under
  `tests/`.
- **Why:** the capability was previously reachable only from inside a private
  working tree. This repository is its single public home, installable on its own.
- **Verification:** the declared gates and `python3 -m unittest discover -s tests`
  pass from a clean checkout of this commit. See the pull request body for the
  commands and their output.
- **Contract:** `The control-plane skill pack: one canonical procedure home that routes a request to the minimum skill bundle, with the gate table and failure policy.`
- **License:** MIT. The committed `LICENSE` file is authoritative.

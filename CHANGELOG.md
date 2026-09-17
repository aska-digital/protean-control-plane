# Changelog

All notable changes to this repository are recorded here. The format is a short
entry per release: what changed, why, and how it was verified.

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

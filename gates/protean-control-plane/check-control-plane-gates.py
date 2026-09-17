#!/usr/bin/env python3
"""check-control-plane-gates.py - run the record gates the control plane cites.

The control plane cites the record gates; it does not own them. This wrapper
locates the `protean-ops` ingredient and runs its gates, and reports each gate as
`unavailable` without failing when the ingredient is not installed, which is the
degraded mode a single-ingredient install produces.

Ops gate discovery order:
  1. $PROTEAN_OPS_GATES       explicit directory
  2. <repo>/scripts/protean-ops          sibling checkout
  3. <target>/scripts/protean-ops        installed beside this ingredient
     ($PROTEAN_TARGET, else --target)

Usage:
  check-control-plane-gates.py [--records DIR] [--target DIR] [--help]
Exit: 0 all available gates passed (or none available); 1 an available gate failed.
"""
import os
import subprocess
import sys

GATES = ("check-rotation.py", "check-inflight.py", "check-learnings.py",
         "check-hotpath-freeze.py", "check-decision-report.py")
HELP_ONLY = {"check-hotpath-freeze.py", "check-decision-report.py"}


def candidate_dirs(target):
    out = []
    env = os.environ.get("PROTEAN_OPS_GATES")
    if env:
        out.append(env)
    repo = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    out.append(os.path.join(repo, "scripts", "protean-ops"))
    root = target or os.environ.get("PROTEAN_TARGET")
    if root:
        out.append(os.path.join(root, "scripts", "protean-ops"))
    return out


def main(argv):
    if "--help" in argv or "-h" in argv:
        print(__doc__.strip())
        return 0
    records = None
    target = None
    args = list(argv)
    for flag in ("--records", "--target"):
        if flag in args:
            k = args.index(flag)
            if k + 1 >= len(args):
                print("FAIL: %s requires a path argument" % flag)
                return 1
            if flag == "--records":
                records = args[k + 1]
            else:
                target = args[k + 1]
            del args[k:k + 2]
    ops_dir = None
    for cand in candidate_dirs(target):
        if cand and os.path.isfile(os.path.join(cand, "check-rotation.py")):
            ops_dir = cand
            break
    if ops_dir is None:
        for gate in GATES:
            print("unavailable: %s (protean-ops is not installed; degraded mode)" % gate)
        print("check-control-plane-gates: PASS  available=0  unavailable=%d  degraded=yes"
              % len(GATES))
        return 0
    unavailable, ran, failed = [], 0, 0
    for gate in GATES:
        script = os.path.join(ops_dir, gate)
        if not os.path.isfile(script):
            unavailable.append(gate)
            print("unavailable: %s (not present in %s)" % (gate, ops_dir))
            continue
        if records and gate not in HELP_ONLY:
            record = os.path.join(records, gate.split("check-", 1)[1]
                                  .replace(".py", "").upper().replace("-", "-") + ".md")
            cmd = [sys.executable, script, record]
            if not os.path.isfile(record):
                cmd = [sys.executable, script, "--help"]
        else:
            cmd = [sys.executable, script, "--help"]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        ran += 1
        status = "PASS" if result.returncode == 0 else "FAIL"
        if result.returncode != 0:
            failed += 1
        print("%s: %s (%s)" % (gate, status, " ".join(cmd[2:]) or "no arguments"))
    print("check-control-plane-gates: %s  available=%d  unavailable=%d  failed=%d  degraded=%s"
          % ("FAIL" if failed else "PASS", ran, len(unavailable), failed,
             "yes" if unavailable else "no"))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

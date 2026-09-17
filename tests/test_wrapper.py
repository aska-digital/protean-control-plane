#!/usr/bin/env python3
"""Exercises the control-plane wrapper: degraded mode, then the available path."""
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WRAPPER = os.path.join(ROOT, "gates", "protean-control-plane",
                       "check-control-plane-gates.py")


def run(*args, env=None):
    environment = dict(os.environ)
    environment.pop("PROTEAN_OPS_GATES", None)
    environment.pop("PROTEAN_TARGET", None)
    if env:
        environment.update(env)
    return subprocess.run([sys.executable, WRAPPER] + list(args),
                          capture_output=True, text=True, env=environment,
                          timeout=120)


class TestWrapper(unittest.TestCase):
    def test_degraded_mode_reports_unavailable(self):
        result = run()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("unavailable", result.stdout)
        self.assertIn("degraded=yes", result.stdout)

    def test_runs_gates_when_ops_is_present(self):
        with tempfile.TemporaryDirectory() as tmp:
            ops = os.path.join(tmp, "scripts", "protean-ops")
            os.makedirs(ops)
            for name in ("check-rotation.py", "check-inflight.py", "check-learnings.py",
                         "check-hotpath-freeze.py", "check-decision-report.py",
                         "check-contrib-state.py"):
                shutil.copy2(os.path.join(ROOT, "tests", "fixtures", "fake-gate.py"),
                             os.path.join(ops, name))
            result = run(env={"PROTEAN_OPS_GATES": ops})
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("available=6", result.stdout)

    def test_help(self):
        result = run("--help")
        self.assertEqual(result.returncode, 0)
        self.assertIn("Usage", result.stdout)


if __name__ == "__main__":
    unittest.main(verbosity=2)

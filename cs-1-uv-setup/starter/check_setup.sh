#!/usr/bin/env bash
# Setup checklist for lesson 1.1. Run from the project folder: bash check_setup.sh
pass=0; fail=0
check() { # check "label" command...
  label="$1"; shift
  if "$@" >/dev/null 2>&1; then echo "PASS  $label"; pass=$((pass+1)); else echo "FAIL  $label"; fail=$((fail+1)); fi
}
check "1 uv is installed"                       uv --version
check "2 .python-version says 3.14"             grep -q '^3\.14' .python-version
check "3 pyproject has requires-python >=3.14"  grep -q 'requires-python = ">=3.14"' pyproject.toml
check "4 pytest is in the dev group"            grep -q 'pytest' pyproject.toml
check "5 uv.lock exists"                        test -f uv.lock
check "6 .venv is ignored by git"               grep -q '^\.venv' .gitignore
check "7 lock matches pyproject"                uv lock --check
check "8 at least one test file exists"         bash -c 'ls tests/test_*.py'
check "9 tests pass with the one command"       uv run --locked pytest -q
check "10 README mentions uv run"               grep -q 'uv run' README.md
echo "passed: $pass, failed: $fail"
[ "$fail" -eq 0 ]

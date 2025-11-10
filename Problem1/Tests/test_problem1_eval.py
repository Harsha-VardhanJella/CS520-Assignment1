# Problem1/Tests/test_problem1_eval.py
from pathlib import Path
import importlib.util
import importlib
import sys
import pytest

ROOT = Path(__file__).resolve().parents[1]
HELPER = ROOT / "eval1.py"

# Which folder to sweep (change if needed)
CODE_DIR = ROOT / "Codes" / "llama" / "Self_debug"

# Which filename patterns to include (edit if you want fewer/more)
PATTERNS = ["solution*.py", "upsolution*.py", "up2solution*.py"]

def _load_helper(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, str(path))
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)  # type: ignore
    return mod

# Build the list of module names to import (so coverage sees them)
FILES = []
for pat in PATTERNS:
    FILES.extend(sorted(CODE_DIR.glob(pat)))
MODULE_NAMES = [p.stem for p in FILES]  # e.g., "upsolution1"

# store results for a clean summary at the end
_results = {}

@pytest.mark.parametrize("modname", MODULE_NAMES, ids=lambda n: n)
def test_every_solution(modname: str):
    """Import each candidate as a normal module so pytest-cov tracks it,
    then run the evaluator's 100-case loop and record the pass count."""
    helper = _load_helper(HELPER, "helper")

    # put code folder on sys.path so importlib can import by module name
    sys.path.insert(0, str(CODE_DIR))
    try:
        candidate = importlib.import_module(modname)  # e.g., import upsolution1
    finally:
        # clean sys.path so we don't leak state
        if str(CODE_DIR) in sys.path:
            sys.path.remove(str(CODE_DIR))

    # some files might be empty placeholders; handle gracefully
    passed = 0
    try:
        passed = helper.run_humaneval_32(candidate)
    except AttributeError:
        # missing required functions (poly/find_zero) → 0/100
        passed = 0

    print(f"\n✅ {modname}.py: {passed}/100\n")  # visible with -s
    _results[f"{modname}.py"] = passed

    # Do NOT fail the test; we want the run to complete for all files
    assert True

def pytest_terminal_summary(terminalreporter):
    if _results:
        terminalreporter.write_line("\n=== Per-file test pass counts ===")
        for name, passed in sorted(_results.items()):
            terminalreporter.write_line(f"✅ {name}: {passed}/100")

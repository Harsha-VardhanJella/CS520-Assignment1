# Problem2/Tests/test_problem2_eval.py
from pathlib import Path
import importlib.util
import importlib
import sys
import pytest

ROOT = Path(__file__).resolve().parents[1]
HELPER = ROOT / "eval2.py"   # evaluator for Problem 2

# Directory containing solutions (adjust if needed)
CODE_DIR = ROOT / "Codes" / "llama" / "COT"

# Include whichever patterns you want to measure
PATTERNS = ["solution*.py", "upsolution*.py", "up2solution*.py"]

def _load_helper(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, str(path))
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)  # type: ignore
    return mod

# Discover all candidate files & module names
FILES = []
for pat in PATTERNS:
    FILES.extend(sorted(CODE_DIR.glob(pat)))
MODULE_NAMES = [p.stem for p in FILES]  # e.g., "upsolution2"

_results = {}

@pytest.mark.parametrize("modname", MODULE_NAMES, ids=lambda n: n)
def test_every_solution(modname: str):
    helper = _load_helper(HELPER, "helper")

    # Import candidate as a NORMAL module so pytest-cov can attribute lines correctly
    sys.path.insert(0, str(CODE_DIR))
    try:
        candidate = importlib.import_module(modname)
    finally:
        if str(CODE_DIR) in sys.path:
            sys.path.remove(str(CODE_DIR))

    # Run fixed test set in eval2.py and capture count
    try:
        passed = helper.run_tests(candidate)  # returns 0..5
    except Exception:
        passed = 0

    print(f"\n✅ {modname}.py: {passed}/5\n")
    _results[f"{modname}.py"] = passed
    assert True  # do not fail; we want the full sweep

def pytest_terminal_summary(terminalreporter):
    if _results:
        terminalreporter.write_line("\n=== Problem 2 • Per-file pass counts ===")
        for name, passed in sorted(_results.items()):
            terminalreporter.write_line(f"✅ {name}: {passed}/5")

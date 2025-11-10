# Problem3/Tests/test_problem3_eval.py
from pathlib import Path
import importlib.util
import importlib
import sys
import pytest

ROOT = Path(__file__).resolve().parents[1]
HELPER = ROOT / "eval3.py"   # 👈 evaluator for Problem 3

# Folder containing all candidate solutions
CODE_DIR = ROOT / "Codes" / "llama" / "COT"   # 👈 adjust if your path differs

# Filename patterns to include
PATTERNS = ["solution*.py", "upsolution*.py", "up2solution*.py"]

def _load_helper(path: Path, name: str):
    """Loads the evaluator module (eval3.py)."""
    spec = importlib.util.spec_from_file_location(name, str(path))
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)  # type: ignore
    return mod

# Discover all solution files
FILES = []
for pat in PATTERNS:
    FILES.extend(sorted(CODE_DIR.glob(pat)))
MODULE_NAMES = [p.stem for p in FILES]

_results = {}

@pytest.mark.parametrize("modname", MODULE_NAMES, ids=lambda n: n)
def test_every_solution(modname: str):
    """Import each candidate as a normal module so pytest-cov tracks it,
    run the evaluator tests, and record the pass count."""
    helper = _load_helper(HELPER, "helper")

    sys.path.insert(0, str(CODE_DIR))
    try:
        candidate = importlib.import_module(modname)
    finally:
        if str(CODE_DIR) in sys.path:
            sys.path.remove(str(CODE_DIR))

    try:
        # 👇 replace run_tests(...) with your actual evaluator function name
        passed = helper.run_tests(candidate)
    except Exception:
        passed = 0

    print(f"\n✅ {modname}.py: {passed} tests passed\n")
    _results[f"{modname}.py"] = passed
    assert True  # always succeed so every file runs

def pytest_terminal_summary(terminalreporter):
    if _results:
        terminalreporter.write_line("\n=== Problem 3 • Per-file test pass counts ===")
        for name, passed in sorted(_results.items()):
            terminalreporter.write_line(f"✅ {name}: {passed}")

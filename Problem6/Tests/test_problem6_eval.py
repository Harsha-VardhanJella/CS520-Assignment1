# Problem6/Tests/test_problem6_eval.py
from pathlib import Path
import importlib.util
import importlib
import sys
import pytest

ROOT = Path(__file__).resolve().parents[1]
HELPER = ROOT / "eval6.py"   # evaluator for Problem 6

# Folder containing solutions (change if different, e.g., llama/Self_debug)
CODE_DIR = ROOT / "Codes" / "llama" / "Self_debug"

# Which solution filenames to include
PATTERNS = ["solution*.py", "upsolution*.py", "up2solution*.py"]

def _load_helper(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, str(path))
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)  # type: ignore
    return mod

# Discover all candidate files and module names
FILES = []
for pat in PATTERNS:
    FILES.extend(sorted(CODE_DIR.glob(pat)))
MODULE_NAMES = [p.stem for p in FILES]

_results = {}

@pytest.mark.parametrize("modname", MODULE_NAMES, ids=lambda n: n)
def test_every_solution(modname: str):
    helper = _load_helper(HELPER, "helper")

    # Import as a normal module so pytest-cov attributes coverage correctly
    sys.path.insert(0, str(CODE_DIR))
    try:
        candidate = importlib.import_module(modname)
    finally:
        if str(CODE_DIR) in sys.path:
            sys.path.remove(str(CODE_DIR))

    # Run Problem 6 tests and capture count
    try:
        passed = helper.run_tests(candidate)   # <-- change if your entry is named differently
    except Exception:
        passed = 0

    print(f"\n✅ {modname}.py: {passed} tests passed\n")
    _results[f"{modname}.py"] = passed
    assert True  # never fail—collect all files

def pytest_terminal_summary(terminalreporter):
    if _results:
        terminalreporter.write_line("\n=== Problem 6 • Per-file test pass counts ===")
        for name, passed in sorted(_results.items()):
            terminalreporter.write_line(f"✅ {name}: {passed}")

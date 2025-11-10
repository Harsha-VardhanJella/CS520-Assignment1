# Problem8/Tests/test_problem8_eval.py
from pathlib import Path
import importlib.util
import importlib
import sys
import pytest

ROOT = Path(__file__).resolve().parents[1]
HELPER = ROOT / "eval8.py"   # evaluator for Problem 8

# Folder containing solutions (adjust if needed, e.g., llama/Self_debug)
CODE_DIR = ROOT / "Codes" / "llama" / "COT"

# Which solution files to include
PATTERNS = ["solution*.py", "upsolution*.py", "up2solution*.py"]

def _load_helper(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, str(path))
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)  # type: ignore
    return mod

# Discover solution modules
FILES = []
for pat in PATTERNS:
    FILES.extend(sorted(CODE_DIR.glob(pat)))
MODULE_NAMES = [p.stem for p in FILES]  # e.g., "upsolution3"

_results = {}

@pytest.mark.parametrize("modname", MODULE_NAMES, ids=lambda n: n)
def test_every_solution(modname: str):
    helper = _load_helper(HELPER, "helper")

    # Import as a normal module so pytest-cov attributes coverage correctly
    sys.path.insert(0, str(CODE_DIR))
    try:
        candidate = importlib.import_module(modname)
        print("Running:", candidate.__file__)   # handy to confirm the file
    finally:
        if str(CODE_DIR) in sys.path:
            sys.path.remove(str(CODE_DIR))

    try:
        passed = helper.run_tests(candidate)    # must return an int
    except Exception:
        passed = 0

    print(f"\n✅ {modname}.py: {passed} tests passed\n")
    _results[f"{modname}.py"] = passed
    assert True  # don't fail; we want a full sweep

def pytest_terminal_summary(terminalreporter):
    if _results:
        terminalreporter.write_line("\n=== Problem 8 • Per-file test pass counts ===")
        for name, passed in sorted(_results.items()):
            terminalreporter.write_line(f"✅ {name}: {passed}")

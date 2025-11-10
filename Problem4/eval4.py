import importlib.util
import sys
from pathlib import Path

def load_module(path: Path):
    spec = importlib.util.spec_from_file_location("candidate", str(path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def run_tests(candidate_module):
    tests = [
        ("", 0),
        ("x", 1),
        ("asdasnakj", 9),
    ]
    passed = 0
    for inp, expected in tests:
        try:
            got = candidate_module.strlen(inp)
            if got == expected:
                passed += 1
            else:
                print(f" input={inp!r} -> got {got}, expected {expected}")
        except Exception as e:
            print(f" input={inp!r} -> raised {e.__class__.__name__}: {e}")
    print(f"\n Passed {passed}/{len(tests)} tests")
    return passed

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python evaluate_strlen.py <candidate_path.py>")
        sys.exit(1)
    mod = load_module(Path(sys.argv[1]))
    run_tests(mod)

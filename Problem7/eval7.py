import importlib.util
import sys
from pathlib import Path

def load_module(path: Path):
    spec = importlib.util.spec_from_file_location("candidate", str(path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def run_tests(mod):
    tests = [
        ([], []),
        ([1, 2, 3, 4], [1, 2, 3, 4]),
        ([1, 2, 3, 2, 4, 3, 5], [1, 4, 5]),
    ]
    passed = 0
    for inp, expected in tests:
        try:
            got = mod.remove_duplicates(inp)
            if got == expected:
                passed += 1
            else:
                print(f" input={inp} -> got {got}, expected {expected}")
        except Exception as e:
            print(f" input={inp} -> raised {e.__class__.__name__}: {e}")
    print(f"\n Passed {passed}/{len(tests)} tests")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python evaluate_remove_duplicates.py <candidate_path.py>")
        sys.exit(1)
    mod = load_module(Path(sys.argv[1]))
    run_tests(mod)

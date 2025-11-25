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
        (1, []),
        (0, []),
        (-5, []),

        (2, [2]),
        (3, [3]),
        (4, [2, 2]),
        (6, [2, 3]),
        (8, [2, 2, 2]),
        (9, [3, 3]),

        (12, [2, 2, 3]),
        (15, [3, 5]),
        (16, [2, 2, 2, 2]),
        (18, [2, 3, 3]),
        (25, [5, 5]),

        (37, [37]),
        (49, [7, 7]),
        (60, [2, 2, 3, 5]),
        (84, [2, 2, 3, 7]),

    ]

    passed = 0
    for n, expected in tests:
        try:
            got = mod.factorize(n)
            if got == expected:
                passed += 1
            else:
                print(f" n={n} -> got {got}, expected {expected}")
        except Exception as e:
            print(f" n={n} -> raised {e.__class__.__name__}: {e}")
    print(f"\n Passed {passed}/{len(tests)} tests")
    return passed

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python evaluate_factorize.py <candidate_path.py>")
        sys.exit(1)
    mod = load_module(Path(sys.argv[1]))
    run_tests(mod)

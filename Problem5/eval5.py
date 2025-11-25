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
        (2, 1),
        (3, 1),
        (4, 2),
        (6, 3),
        (9, 3),
        (10, 5),
        (12, 6),
        (15, 5),
        (16, 8),
        (21, 7),
        (25, 5),
        (27, 9),
        (28, 14),
        (49, 7),

    ]
    passed = 0
    for n, expected in tests:
        try:
            got = mod.largest_divisor(n)
            if got == expected:
                passed += 1
            else:
                print(f" n={n} -> got {got}, expected {expected}")
        except Exception as e:
            print(f" n={n} -> raised {e.__class__.__name__}: {e}")
    print(f"\n✅ Passed {passed}/{len(tests)} tests")
    return passed

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python evaluate_largest_divisor.py <candidate_path.py>")
        sys.exit(1)
    mod = load_module(Path(sys.argv[1]))
    run_tests(mod)

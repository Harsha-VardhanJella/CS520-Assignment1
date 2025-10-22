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
        ([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3, True),
        ([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.05, False),
        ([1.0, 2.0, 5.9, 4.0, 5.0], 0.95, True),
        ([1.0, 2.0, 5.9, 4.0, 5.0], 0.8, False),
        ([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.1, True),
        ([1.1, 2.2, 3.1, 4.1, 5.1], 1.0, True),
        ([1.1, 2.2, 3.1, 4.1, 5.1], 0.5, False),
    ]

    passed = 0
    for arr, threshold, expected in tests:
        try:
            got = mod.has_close_elements(arr, threshold)
            if got == expected:
                passed += 1
            else:
                print(f" input={arr}, threshold={threshold} -> got {got}, expected {expected}")
        except Exception as e:
            print(f" input={arr}, threshold={threshold} -> raised {e.__class__.__name__}: {e}")
    print(f"\n Passed {passed}/{len(tests)} tests")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python evaluate_has_close_elements.py <candidate_path.py>")
        sys.exit(1)
    mod = load_module(Path(sys.argv[1]))
    run_tests(mod)

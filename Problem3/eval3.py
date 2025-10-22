import importlib.util
import sys
from pathlib import Path

def load_module(path):
    """Dynamically import a .py file"""
    spec = importlib.util.spec_from_file_location("candidate", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def run_tests(candidate):
    """Exact HumanEval/22 tests"""
    tests = [
        ([], []),
        ([4, {}, [], 23.2, 9, "adasd"], [4, 9]),
        ([3, "c", 3, 3, "a", "b"], [3, 3, 3]),
    ]

    passed = 0
    for inp, expected in tests:
        try:
            result = candidate.filter_integers(inp)
            if result == expected:
                passed += 1
            else:
                print(f" Input {inp} → got {result}, expected {expected}")
        except Exception as e:
            print(f" Input {inp} → raised {e}")

    print(f"\n Passed {passed}/{len(tests)} tests")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python evaluate_filter_integers.py <candidate_path>")
        sys.exit(1)

    path = Path(sys.argv[1])
    mod = load_module(path)
    run_tests(mod)

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
    """Run the HumanEval/20 tests"""
    tests = [
        ([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], (3.9, 4.0)),
        ([1.0, 2.0, 5.9, 4.0, 5.0], (5.0, 5.9)),
        ([1.0, 2.0, 3.0, 4.0, 5.0, 2.2], (2.0, 2.2)),
        ([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], (2.0, 2.0)),
        ([1.1, 2.2, 3.1, 4.1, 5.1], (2.2, 3.1)),
    ]

    passed = 0
    for nums, expected in tests:
        try:
            result = candidate.find_closest_elements(nums)
            if result == expected:
                passed += 1
            else:
                print(f" Input {nums} → got {result}, expected {expected}")
        except Exception as e:
            print(f"Input {nums} → raised {e}")
    print(f"\n✅ Passed {passed}/{len(tests)} tests")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python evaluate_find_closest.py <candidate_path>")
        sys.exit(1)

    path = Path(sys.argv[1])
    mod = load_module(path)
    run_tests(mod)

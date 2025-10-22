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
        ('(()()) ((())) () ((())()())', ['(()())', '((()))', '()', '((())()())']),
        ('() (()) ((())) (((())))',     ['()', '(())', '((()))', '(((())))']),
        ('(()(())((())))',              ['(()(())((())))']),
        ('( ) (( )) (( )( ))',          ['()', '(())', '(()())']),
    ]
    passed = 0
    for s, expected in tests:
        try:
            got = mod.separate_paren_groups(s)
            if got == expected:
                passed += 1
            else:
                print(f" input={s!r} -> got {got!r}, expected {expected!r}")
        except Exception as e:
            print(f" input={s!r} -> raised {e.__class__.__name__}: {e}")
    print(f"\n Passed {passed}/{len(tests)} tests")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python evaluate_separate_paren_groups.py <candidate_path.py>")
        sys.exit(1)
    mod = load_module(Path(sys.argv[1]))
    run_tests(mod)

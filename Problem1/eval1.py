# Problem1/eval_he32.py
import argparse
import importlib.util
import math
import random
import sys
import types
import copy
from pathlib import Path
from typing import List

def load_module(path: Path) -> types.ModuleType:
    spec = importlib.util.spec_from_file_location("candidate", str(path))
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)  # type: ignore
    return mod

def run_humaneval_32(candidate_module: types.ModuleType) -> int:
    """
    Returns number of passed cases out of 100 for HumanEval/32.
    Candidate module MUST define:
      - poly(xs: list, x: float) -> float
      - find_zero(xs: list) -> float
    """
    if not hasattr(candidate_module, "poly") or not hasattr(candidate_module, "find_zero"):
        raise AttributeError("Candidate must define BOTH `poly(xs, x)` and `find_zero(xs)`.")

    poly = candidate_module.poly
    find_zero = candidate_module.find_zero

    rng = random.Random(42)
    passed = 0
    for _ in range(100):
        ncoeff = 2 * rng.randint(1, 4)  # even degree: 2, 4, 6, 8
        coeffs: List[int] = []
        for _ in range(ncoeff):
            coeff = rng.randint(-10, 10)
            if coeff == 0:
                coeff = 1
            coeffs.append(coeff)
        x = find_zero(copy.deepcopy(coeffs))
        if math.fabs(poly(coeffs, x)) < 1e-4:
            passed += 1
    return passed

def eval_one(path: Path) -> None:
    try:
        mod = load_module(path)
        passed = run_humaneval_32(mod)
        print(f"{path}: Passed {passed}/100")
    except Exception as e:
        print(f"{path}: ERROR -> {e}")

def main():
    ap = argparse.ArgumentParser(description="Evaluate LLM code on HumanEval/32")
    ap.add_argument("--candidate", type=str, help="Path to a single candidate .py file")
    ap.add_argument(
        "--glob",
        type=str,
        default="Problem1/Codes/**/*.py",
        help="Glob to evaluate many files (ignored if --candidate is given)",
    )
    args = ap.parse_args()

    if args.candidate:
        eval_one(Path(args.candidate))
    else:
        files = sorted(Path().glob(args.glob))
        if not files:
            print("No files found. Adjust --glob or pass --candidate.")
            sys.exit(1)
        for f in files:
            # only evaluate solution files if you like:
            if f.name.startswith("solution") and f.suffix == ".py":
                eval_one(f)

if __name__ == "__main__":
    main()

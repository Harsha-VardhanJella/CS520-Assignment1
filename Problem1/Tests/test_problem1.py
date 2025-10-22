def check(candidate):
    import math
    import random
    rng = random.Random(42)
    import copy

    fails = 0  # ✅ Define before the loop

    for i in range(100):
        ncoeff = 2 * rng.randint(1, 4)
        coeffs = []
        for _ in range(ncoeff):
            coeff = rng.randint(-10, 10)
            if coeff == 0:
                coeff = 1
            coeffs.append(coeff)

        solution = candidate(copy.deepcopy(coeffs))
        val = poly(coeffs, solution)
        if math.fabs(val) >= 1e-4:
            fails += 1
            print(f"❌ Fail {i}: coeffs={coeffs}, x={solution}, poly(xs,x)={val}")

    print(f"✅ Total fails: {fails}")

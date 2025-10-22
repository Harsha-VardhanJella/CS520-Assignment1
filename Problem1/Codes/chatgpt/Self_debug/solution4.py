import math

def poly(xs: list, x: float):
    return sum(coeff * math.pow(x, i) for i, coeff in enumerate(xs))

def find_zero(xs: list):
    # Initial guess
    a, b = -1.0, 1.0
    fa, fb = poly(xs, a), poly(xs, b)

    # Expand interval until a sign change is found
    step = 1.0
    max_expand = 1e6
    while fa * fb > 0 and step < max_expand:
        a -= step
        b += step
        fa, fb = poly(xs, a), poly(xs, b)
        step *= 2

    # If no sign change found, return 0 as fallback
    if fa * fb > 0:
        return 0.0

    # Bisection method
    tol = 1e-12
    while b - a > tol:
        c = (a + b) / 2
        fc = poly(xs, c)
        if abs(fc) < tol:
            return c
        if fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc
    return (a + b) / 2

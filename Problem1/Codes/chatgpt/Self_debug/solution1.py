import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    Example: if xs = [a0, a1, a2], returns a0 + a1*x + a2*x**2
    """
    return sum(coeff * math.pow(x, i) for i, coeff in enumerate(xs))

def find_zero(xs: list):
    """
    Return one real x such that poly(xs, x) ≈ 0.
    Uses interval expansion + bisection for robustness.
    """
    # Initial guess and expansion parameters
    a, b = -1.0, 1.0
    max_expand = 1e6
    factor = 2.0

    # Expand interval until a sign change is found
    while poly(xs, a) * poly(xs, b) > 0 and abs(a) < max_expand and abs(b) < max_expand:
        a *= factor
        b *= factor

    # If unable to bracket root, fallback to 0
    if poly(xs, a) * poly(xs, b) > 0:
        return 0.0

    # Bisection method
    tol = 1e-12
    while abs(b - a) > tol:
        c = (a + b) / 2.0
        fc = poly(xs, c)
        if abs(fc) < tol:
            return c
        if poly(xs, a) * fc < 0:
            b = c
        else:
            a = c
    return (a + b) / 2.0

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
    Use a robust numerical method: bracket a sign change by expanding an initial interval,
    then apply bisection until the interval is sufficiently small.
    """
    # Define the initial interval and expansion factor
    a = -1.0
    b = 1.0
    factor = 2.0
    max_iter = 1000
    tol = 1e-12

    # Bracket the root
    while poly(xs, a) * poly(xs, b) > 0:
        if abs(poly(xs, a)) < abs(poly(xs, b)):
            a -= (b - a) * factor
        else:
            b += (b - a) * factor

    # Apply bisection
    for _ in range(max_iter):
        c = (a + b) / 2
        if poly(xs, c) == 0 or (b - a) / 2 < tol:
            return c
        if poly(xs, a) * poly(xs, c) < 0:
            b = c
        else:
            a = c

    # If max_iter reached, return the best estimate
    return (a + b) / 2
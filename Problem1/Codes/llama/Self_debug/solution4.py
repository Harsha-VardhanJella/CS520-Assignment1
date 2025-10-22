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
    # Initial interval
    x0 = 0.0
    if poly(xs, x0) == 0:
        return x0
    
    # Find the direction to expand the interval
    step = 1.0
    if poly(xs, x0) < 0:
        x1 = x0 + step
        while poly(xs, x1) < 0:
            x1 += step
    else:
        x1 = x0 - step
        while poly(xs, x1) > 0:
            x1 -= step

    # Ensure x0 and x1 bracket the root
    if x1 > x0:
        a, b = x0, x1
    else:
        a, b = x1, x0

    # Apply bisection
    while b - a > 1e-6:
        c = (a + b) / 2
        if poly(xs, c) == 0:
            return c
        elif poly(xs, c) < 0:
            a = c
        else:
            b = c

    return (a + b) / 2
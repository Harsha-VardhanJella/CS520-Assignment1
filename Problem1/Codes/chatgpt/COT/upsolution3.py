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
    tol = 1e-12
    max_iter = 1000
    a, b = -1.0, 1.0
    fa, fb = poly(xs, a), poly(xs, b)

    # Expand interval until a sign change is found
    expand_factor = 2.0
    while fa * fb > 0:
        a *= expand_factor
        b *= expand_factor
        fa, fb = poly(xs, a), poly(xs, b)

    # Bisection method
    for _ in range(max_iter):
        c = (a + b) / 2.0
        fc = poly(xs, c)
        if abs(fc) < tol or (b - a) / 2 < tol:
            return c
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    return (a + b) / 2.0
